"""Lab 10: context is a finite attention budget, and cost is tokens times price (Principles 9 and 17).

Part 1: a query attends over retrieved chunks with the softmax attention from lab 02.
Adding irrelevant chunks lowers the weight on the relevant one, because softmax
weights must sum to one. That is the mechanism behind "every token competes".
Part 2: cost and latency arithmetic for a request, with and without prefix caching.
NumPy only.

Run: python lab10_context_and_cost.py
"""
import numpy as np

rng = np.random.default_rng(0)
D = 64


def softmax(x):
    x = x - x.max(); e = np.exp(x); return e / e.sum()


def weight_on_relevant(n_distractors, relevance=3.0):
    q = rng.normal(0, 1, D)
    relevant = q / np.linalg.norm(q) * relevance + rng.normal(0, 0.5, D)  # similar to the query
    distractors = rng.normal(0, 1, (n_distractors, D))                      # unrelated
    keys = np.vstack([relevant, distractors])
    w = softmax(keys @ q / np.sqrt(D))
    return w[0]


def cost(prompt_tokens, output_tokens, price_in, price_out, cached_tokens=0, cache_discount=0.9):
    """Prices per million tokens. Cached input tokens are billed at (1 - discount)."""
    uncached = prompt_tokens - cached_tokens
    return (uncached * price_in + cached_tokens * price_in * (1 - cache_discount) + output_tokens * price_out) / 1e6


if __name__ == "__main__":
    print("attention weight on the one relevant chunk as distractors are added (mean of 200 draws):")
    prev = 1.0
    for n in (0, 2, 8, 32, 128):
        w = np.mean([weight_on_relevant(n) for _ in range(200)])
        print(f"  {n:3d} distractors -> weight {w:.2f}")
        assert w <= prev + 1e-9
        prev = w
    assert prev < 0.5, "with 128 distractors the relevant chunk should get a minority of the attention"

    # Cost: a 6,000-token system prompt + 500-token question, 300-token answer, at $3/M in, $15/M out
    full = cost(6500, 300, 3, 15)
    cached = cost(6500, 300, 3, 15, cached_tokens=6000)
    print(f"request cost: ${full:.4f} without caching, ${cached:.4f} with the 6,000-token prefix cached ({(1-cached/full)*100:.0f}% cheaper)")
    assert 0.55 < 1 - cached / full < 0.75
    # Latency: prefill is one pass over the prompt; decode is one pass per output token
    prefill_ms, decode_ms_per_tok = 6500 * 0.05, 25
    print(f"latency: prefill ~{prefill_ms:.0f} ms + decode 300 x {decode_ms_per_tok} ms = {prefill_ms + 300*decode_ms_per_tok:.0f} ms; halving the output saves {150*decode_ms_per_tok} ms")
    print("OK")
