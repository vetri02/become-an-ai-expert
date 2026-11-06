"""Lab 09: RL post-training optimises the reward and degrades what it does not measure (Principle 8).

A tiny policy (a softmax over bigram logits, initialised from "pretraining" counts)
is trained with REINFORCE to maximise a reward: "contain the word 'please'".
Watch three things:
  1. reward rises (the policy learns the behaviour)
  2. held-out likelihood of ordinary text falls (general ability degrades)
  3. the policy reward-hacks: it says 'please' far more than any polite sentence would
A KL penalty against the pretrained policy limits the damage. NumPy only.

Run: python lab09_rl_reward_hacking.py
"""
import numpy as np

rng = np.random.default_rng(0)

CORPUS = ("please pass the salt . pass the salt please . the salt is here . here is the salt . "
          "could you pass the salt . the salt please . pass it here . it is here .").split()
vocab = sorted(set(CORPUS)); V = len(vocab); idx = {w: i for i, w in enumerate(vocab)}
toks = np.array([idx[w] for w in CORPUS])


def pretrain_logits():
    C = np.full((V, V), 0.5)
    np.add.at(C, (toks[:-1], toks[1:]), 1)
    return np.log(C / C.sum(1, keepdims=True))


def softmax(z):
    z = z - z.max(-1, keepdims=True); e = np.exp(z); return e / e.sum(-1, keepdims=True)


def sample_seq(logits, length=8):
    seq, logps = [idx["the"]], []
    for _ in range(length):
        p = softmax(logits[seq[-1]])
        t = rng.choice(V, p=p)
        logps.append((seq[-1], t))
        seq.append(t)
    return seq, logps


def reward(seq):
    """Reward = number of 'please' tokens. A loosely specified reward: the designer wanted politeness,
    the policy will discover that spamming the word pays more. This is what reward hacking is."""
    return float(sum(t == idx["please"] for t in seq[1:]))


def heldout_loss(logits):
    lp = np.log(softmax(logits))
    return -np.mean(lp[toks[:-1], toks[1:]])


def kl_grad(theta_s, base_s):
    """Gradient wrt logits of KL(p_theta || p_base) at one state: p * (log p - log q - KL)."""
    p, q = softmax(theta_s), softmax(base_s)
    lr_ = np.log(p) - np.log(q)
    return p * (lr_ - (p * lr_).sum())


def train(kl_coef, steps=300, lr=0.5, batch=32):
    base = pretrain_logits(); theta = base.copy()
    baseline = 0.0
    for _ in range(steps):
        grad = np.zeros_like(theta); rewards = []; visited = set()
        samples = [sample_seq(theta) for _ in range(batch)]
        rewards = [reward(seq) for seq, _ in samples]
        baseline = 0.9 * baseline + 0.1 * np.mean(rewards)      # moving-average reward baseline
        for (seq, pairs), r in zip(samples, rewards):
            adv = r - baseline
            for s, t in pairs:
                g = -softmax(theta[s]); g[t] += 1               # d log p(t|s) / d theta[s]  (REINFORCE)
                grad[s] += adv * g
                visited.add(s)
        grad /= batch
        for s in visited:                                        # explicit KL-to-reference penalty, as in RLHF/GRPO
            grad[s] -= kl_coef * kl_grad(theta[s], base[s])
        theta += lr * grad
    return theta, np.mean(rewards)


if __name__ == "__main__":
    base = pretrain_logits()
    print(f"pretrained: held-out loss {heldout_loss(base):.3f}, reward {np.mean([reward(sample_seq(base)[0]) for _ in range(200)]):.2f}")
    for kl in (0.0, 2.0):
        th, r = train(kl)
        please_rate = np.mean([sum(t == idx['please'] for t in sample_seq(th)[0]) for _ in range(200)])
        print(f"RL with KL coef {kl}: reward {r:.2f}, held-out loss {heldout_loss(th):.3f}, 'please' per 8 tokens {please_rate:.2f}")
        if kl == 0.0:
            no_kl = (r, heldout_loss(th), please_rate)
        else:
            with_kl = (r, heldout_loss(th), please_rate)
    assert no_kl[0] > 2.0, "RL should learn the rewarded behaviour"
    assert no_kl[1] > heldout_loss(base) + 0.3, "unconstrained RL should degrade likelihood of ordinary text"
    assert no_kl[2] > 2.0, "without a KL penalty the policy spams the rewarded token (reward hacking); no polite sentence says it 2+ times in 8 words"
    assert with_kl[1] < no_kl[1] - 0.1 and with_kl[0] > 0.5, "KL penalty should limit degradation while keeping some reward"
    print("the reward went up, ordinary-text likelihood went down, and the policy found the loophole in the reward; the KL term is the leash")
    print("OK")
