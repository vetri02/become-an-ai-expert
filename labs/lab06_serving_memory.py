"""Lab 06: serving memory math (Module 05 and Track B, or A4 on the Novice track; Principle 6).

Computes weight memory and KV-cache memory for a transformer from its config,
and finds the largest batch that fits on a given GPU. Pure Python.

The formulas:
  weights_bytes   = n_params * bytes_per_param
  kv_per_token    = 2 (K and V) * n_layers * n_kv_heads * head_dim * bytes_per_value
  kv_total        = kv_per_token * context_len * batch

Run: python lab06_serving_memory.py
"""

GB = 1024 ** 3

MODELS = {
    # name: (params, layers, kv_heads, head_dim). Llama-3-8B uses grouped-query attention (8 KV heads).
    "7B-class (32 KV heads, MHA)": (7e9, 32, 32, 128),
    "8B-class (8 KV heads, GQA)": (8e9, 32, 8, 128),
    "70B-class (8 KV heads, GQA)": (70e9, 80, 8, 128),
}


def kv_per_token_bytes(layers, kv_heads, head_dim, bytes_per_value=2):
    return 2 * layers * kv_heads * head_dim * bytes_per_value


def max_batch(params, layers, kv_heads, head_dim, context, gpu_gb, bytes_per_param=2, overhead_gb=2):
    weights = params * bytes_per_param
    free = gpu_gb * GB - weights - overhead_gb * GB
    per_seq = kv_per_token_bytes(layers, kv_heads, head_dim) * context
    if free <= 0:
        return 0, weights, per_seq
    return int(free // per_seq), weights, per_seq


if __name__ == "__main__":
    context, gpu = 4096, 80
    print(f"GPU {gpu} GB, bf16 weights, bf16 KV cache, context {context}, 2 GB overhead")
    for name, (p, L, H, d) in MODELS.items():
        b, w, per_seq = max_batch(p, L, H, d, context, gpu)
        print(f"  {name:30s} weights {w/GB:6.1f} GB | KV per token {kv_per_token_bytes(L,H,d)/1024:6.0f} KB | KV per {context}-token seq {per_seq/GB:5.2f} GB | max batch {b}")
    # Checks against hand computation
    assert kv_per_token_bytes(32, 32, 128) == 2 * 32 * 32 * 128 * 2 == 524288      # 512 KB/token for a 7B MHA model
    assert kv_per_token_bytes(32, 8, 128) == 131072                                 # 128 KB/token with GQA: 4x smaller
    b8, _, _ = max_batch(8e9, 32, 8, 128, 4096, 80)
    b7, _, _ = max_batch(7e9, 32, 32, 128, 4096, 80)
    assert b8 > 3 * b7, "GQA should allow several times the batch of MHA at the same context"
    b70, w70, _ = max_batch(70e9, 80, 8, 128, 4096, 80)
    assert b70 == 0 and w70 / GB > 80, "a 70B model in bf16 does not fit on one 80 GB GPU"
    print("  (70B in bf16 needs >1 GPU or quantization: at INT4 the weights are ~35 GB)")
    print("OK")
