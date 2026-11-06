"""Lab 07: a language model is a next-token distribution (Principle 1).

Builds a trigram model from text, then produces "chat" by sampling one token at a
time and appending. Shows that the model is nothing but P(next | previous) and that
temperature only reshapes that distribution. Pure Python.

Run: python lab07_next_token.py
"""
import math
import random
from collections import Counter, defaultdict

random.seed(0)

TEXT = """
the model predicts the next token . the next token is sampled from a distribution .
the distribution depends on the previous tokens . a chat is many next tokens in a row .
an agent is a chat that calls tools . tools return text . the text becomes previous tokens .
the model does not know what it has not seen . retrieval puts text into the previous tokens .
""".split()


def train(tokens, n=3):
    counts = defaultdict(Counter)
    for i in range(len(tokens) - n + 1):
        ctx, nxt = tuple(tokens[i : i + n - 1]), tokens[i + n - 1]
        counts[ctx][nxt] += 1
    return counts


def next_token_distribution(counts, ctx, vocab, temperature=1.0, alpha=0.01):
    c = counts.get(ctx, Counter())
    logits = {w: math.log(c[w] + alpha) / temperature for w in vocab}  # add-alpha smoothing
    m = max(logits.values())
    z = sum(math.exp(v - m) for v in logits.values())
    return {w: math.exp(v - m) / z for w, v in logits.items()}


def sample(dist):
    r, acc = random.random(), 0.0
    for w, p in dist.items():
        acc += p
        if r <= acc:
            return w
    return w


def generate(counts, vocab, prompt, n_new, temperature=1.0):
    toks = list(prompt)
    for _ in range(n_new):
        dist = next_token_distribution(counts, tuple(toks[-2:]), vocab, temperature)
        toks.append(sample(dist))
    return toks


if __name__ == "__main__":
    vocab = sorted(set(TEXT))
    counts = train(TEXT)
    d = next_token_distribution(counts, ("the", "next"), vocab)
    top = sorted(d.items(), key=lambda kv: -kv[1])[:3]
    print("P(next | 'the next') top 3:", [(w, round(p, 2)) for w, p in top])
    assert top[0][0] == "token" and abs(sum(d.values()) - 1) < 1e-9

    out = generate(counts, vocab, ["the", "model"], 12)
    print("sampled at T=1.0:", " ".join(out))
    cold = generate(counts, vocab, ["the", "model"], 12, temperature=0.05)
    print("sampled at T=0.05:", " ".join(cold))
    # Low temperature should make generation (near) deterministic: repeat and compare
    cold2 = generate(counts, vocab, ["the", "model"], 12, temperature=0.05)
    assert cold == cold2, "near-zero temperature should be repeatable"

    # The model has no notion of 'facts' beyond counts: an unseen word gets only smoothing mass
    unseen = next_token_distribution(counts, ("the", "model"), vocab)["agent"]
    seen = next_token_distribution(counts, ("the", "model"), vocab)["predicts"]
    print(f"P('predicts' | 'the model') = {seen:.3f}; P('agent' | 'the model') = {unseen:.4f} (never seen, smoothing only)")
    assert seen > 20 * unseen
    print("OK")
