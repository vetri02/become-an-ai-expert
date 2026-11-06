"""Lab 02: attention from scratch (Module 04, or A4 on the Novice track; Principle 4).

Single-head causal self-attention in NumPy. Checks the three facts that matter:
  1. Each output row is a weighted average of value rows (weights sum to 1, non-negative).
  2. The causal mask makes position t depend only on positions <= t.
  3. Dividing by sqrt(d) keeps the softmax from saturating as d grows.

Run: python lab02_attention.py
"""
import numpy as np

rng = np.random.default_rng(0)


def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)


def causal_attention(x, Wq, Wk, Wv, scale=True):
    T, _ = x.shape
    Q, K, V = x @ Wq, x @ Wk, x @ Wv
    d = Q.shape[-1]
    scores = Q @ K.T
    if scale:
        scores = scores / np.sqrt(d)
    mask = np.triu(np.ones((T, T), dtype=bool), k=1)  # True above the diagonal = future
    scores = np.where(mask, -np.inf, scores)
    weights = softmax(scores)
    return weights @ V, weights


if __name__ == "__main__":
    T, d_model, d_head = 6, 16, 8
    x = rng.normal(0, 1, (T, d_model))
    Wq, Wk, Wv = (rng.normal(0, 0.3, (d_model, d_head)) for _ in range(3))

    out, w = causal_attention(x, Wq, Wk, Wv)
    print("attention weights (rows sum to 1, upper triangle is 0):")
    print(np.round(w, 2))

    # 1. weighted average
    assert np.allclose(w.sum(axis=1), 1.0) and (w >= 0).all()
    # 2. causality: changing a future token must not change earlier outputs
    x2 = x.copy()
    x2[-1] += 10.0
    out2, _ = causal_attention(x2, Wq, Wk, Wv)
    assert np.allclose(out[:-1], out2[:-1]), "earlier positions saw the future"
    assert not np.allclose(out[-1], out2[-1])
    print("causality holds: editing token 6 changed only output 6")

    # 3. scaling: q.k is a sum of d_head products, so its spread grows like sqrt(d_head).
    #    Without /sqrt(d) the softmax saturates toward one-hot as d grows; with it, the spread stays ~1.
    Tb, dm, dh = 32, 64, 256
    xb = rng.normal(0, 1, (Tb, dm))
    Wq_b, Wk_b, Wv_b = (rng.normal(0, 1 / np.sqrt(dm), (dm, dh)) for _ in range(3))  # q, k entries ~ N(0,1)
    _, w_scaled = causal_attention(xb, Wq_b, Wk_b, Wv_b, scale=True)
    _, w_unscaled = causal_attention(xb, Wq_b, Wk_b, Wv_b, scale=False)
    def mean_entropy(W):
        last = W[-1]  # the last row attends over all Tb positions
        p = last[last > 0]
        return float(-(p * np.log(p)).sum())
    es, eu = mean_entropy(w_scaled), mean_entropy(w_unscaled)
    print(f"entropy of the last row's attention over {Tb} positions at d_head={dh}: scaled {es:.2f}, unscaled {eu:.2f} (max possible {np.log(Tb):.2f})")
    assert eu < es / 2, "unscaled softmax should be far more peaked"
    assert es > 1.5, "scaled attention should stay spread out"
    print("OK")
