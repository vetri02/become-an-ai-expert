"""Lab 03: the KV cache (Module 05, or A4 on the Novice track; Principle 5).

A toy decoder-only model (random weights, one attention layer) generates tokens two ways:
  A. recompute attention over the full sequence every step (O(n^2) total work)
  B. cache K and V and only compute the new row (O(n) total work)
Checks that both produce identical tokens and measures the speedup.

Run: python lab03_kv_cache.py
"""
import time

import numpy as np

rng = np.random.default_rng(0)
V, D = 64, 64  # vocab, model width
E = rng.normal(0, 0.5, (V, D))     # embeddings
Wq, Wk, Wv, Wo = (rng.normal(0, 0.2, (D, D)) for _ in range(4))
Wout = rng.normal(0, 0.2, (D, V))  # unembedding


def softmax(x):
    x = x - x.max(-1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(-1, keepdims=True)


def logits_full(tokens):
    """Recompute everything for the whole sequence; return logits for the last position."""
    x = E[tokens]
    Q, K, Vv = x @ Wq, x @ Wk, x @ Wv
    T = len(tokens)
    s = Q @ K.T / np.sqrt(D)
    s = np.where(np.triu(np.ones((T, T), bool), 1), -np.inf, s)
    h = softmax(s) @ Vv
    return (x + h @ Wo)[-1] @ Wout


def generate_no_cache(prompt, n):
    toks = list(prompt)
    for _ in range(n):
        toks.append(int(np.argmax(logits_full(np.array(toks)))))
    return toks


def generate_with_cache(prompt, n):
    toks = list(prompt)
    x = E[np.array(toks)]
    Kc, Vc = x @ Wk, x @ Wv            # the cache, filled during "prefill"
    Q = x @ Wq
    T = len(toks)
    s = Q @ Kc.T / np.sqrt(D)
    s = np.where(np.triu(np.ones((T, T), bool), 1), -np.inf, s)
    last = (x + (softmax(s) @ Vc) @ Wo)[-1] @ Wout
    for _ in range(n):
        t = int(np.argmax(last))
        toks.append(t)
        xt = E[t]                          # one row of work per step
        q, k, v = xt @ Wq, xt @ Wk, xt @ Wv
        Kc = np.vstack([Kc, k]); Vc = np.vstack([Vc, v])
        s = q @ Kc.T / np.sqrt(D)          # attend over cached keys; no mask needed, all are past
        h = softmax(s) @ Vc
        last = (xt + h @ Wo) @ Wout
    return toks


if __name__ == "__main__":
    prompt = [1, 2, 3]
    n = 400
    t0 = time.perf_counter(); a = generate_no_cache(prompt, n); ta = time.perf_counter() - t0
    t0 = time.perf_counter(); b = generate_with_cache(prompt, n); tb = time.perf_counter() - t0
    assert a == b, "cached and uncached generation diverged"
    print(f"{n} tokens: no cache {ta*1000:.0f} ms, with cache {tb*1000:.0f} ms, speedup {ta/tb:.1f}x, outputs identical")
    kv_bytes = 2 * len(b) * D * 8  # K and V, float64, one layer
    print(f"cache size after {len(b)} tokens, one layer, float64: {kv_bytes/1024:.1f} KB (grows linearly with context)")
    assert ta / tb > 3, "expected a clear speedup from the cache"
    print("OK")
