"""Lab 08: loss falls as a power law in data (Principle 7).

Generates text from a hidden Markov source, trains bigram models on growing amounts
of it, measures held-out cross-entropy, and fits loss(N) = L_inf + A * N^(-alpha).
This is the shape of the scaling-law plots in the papers; here you can see the
whole mechanism (more data -> better count estimates -> lower loss, with diminishing
returns toward the irreducible entropy of the source). NumPy only.

Run: python lab08_scaling_law.py
"""
import numpy as np

rng = np.random.default_rng(0)
V = 50


def make_source():
    """A random Markov chain over V tokens with peaked transitions."""
    P = rng.dirichlet(np.full(V, 0.3), size=V)
    return P


def sample_chain(P, n):
    toks = np.empty(n, dtype=int)
    toks[0] = rng.integers(V)
    for i in range(1, n):
        toks[i] = rng.choice(V, p=P[toks[i - 1]])
    return toks


def train_bigram(toks, alpha=0.5):
    C = np.full((V, V), alpha)
    np.add.at(C, (toks[:-1], toks[1:]), 1)
    return C / C.sum(1, keepdims=True)


def cross_entropy(model, toks):
    return -np.mean(np.log(model[toks[:-1], toks[1:]]))


def source_entropy(P, toks):
    return -np.mean(np.log(P[toks[:-1], toks[1:]]))


if __name__ == "__main__":
    P = make_source()
    test = sample_chain(P, 20000)
    L_inf_true = source_entropy(P, test)
    sizes = [100, 300, 1000, 3000, 10000, 30000, 100000]
    losses = []
    for n in sizes:
        m = train_bigram(sample_chain(P, n))
        losses.append(cross_entropy(m, test))
        print(f"  N={n:>7d} tokens  held-out loss {losses[-1]:.3f} nats")
    losses = np.array(losses)
    assert all(np.diff(losses) < 0), "loss should fall monotonically with data"

    # Fit log(loss - L_inf) = log A - alpha log N  (excess loss is a power law)
    excess = losses - L_inf_true
    slope, intercept = np.polyfit(np.log(sizes), np.log(excess), 1)
    alpha = -slope
    print(f"irreducible loss (entropy of the source) = {L_inf_true:.3f}; fitted excess-loss exponent alpha = {alpha:.2f}")
    assert 0.5 < alpha < 1.3, "excess loss should fall roughly like 1/N for a count-based estimator"
    print("ten times the data cuts the excess loss by about", f"{10**alpha:.1f}x, not to zero: that is the diminishing return")
    print("OK")
