"""Lab 12: memory-bound vs compute-bound (Principle 18).

Part 1: the arithmetic. Decoding one token for a batch of b sequences reads every
weight once (bytes) and does 2 * params * b FLOPs. Arithmetic intensity = FLOPs/byte
grows with batch, so small-batch decode is bandwidth-bound and large-batch is
compute-bound. The crossover batch depends only on the hardware's FLOPs/bandwidth ratio.
Part 2: measure it on your CPU. Matrix-vector (batch 1) achieves far fewer GFLOP/s
than matrix-matrix (batch 64) with the same weights, because the weight read dominates.

Run: python lab12_roofline.py
"""
import time

import numpy as np

H100 = {"flops": 990e12, "bandwidth": 3.35e12}  # bf16 dense, HBM3; published spec figures


def arithmetic_intensity(batch, bytes_per_param=2):
    # FLOPs per weight byte for one decode step: 2 FLOPs per param per sequence / bytes per param
    return 2 * batch / bytes_per_param


def crossover_batch(hw, bytes_per_param=2):
    return hw["flops"] / hw["bandwidth"] * bytes_per_param / 2


def measure(n, batch, reps=5):
    W = np.random.default_rng(0).standard_normal((n, n), dtype=np.float32)
    X = np.random.default_rng(1).standard_normal((n, batch), dtype=np.float32)
    W @ X
    t0 = time.perf_counter()
    for _ in range(reps):
        W @ X
    dt = (time.perf_counter() - t0) / reps
    return 2 * n * n * batch / dt / 1e9  # GFLOP/s


if __name__ == "__main__":
    ridge = H100["flops"] / H100["bandwidth"]
    print(f"H100: {ridge:.0f} FLOPs per byte at the ridge; decode becomes compute-bound above batch ~{crossover_batch(H100):.0f}")
    for b in (1, 8, 64, 512):
        ai = arithmetic_intensity(b)
        print(f"  batch {b:3d}: intensity {ai:5.0f} FLOP/byte -> {'bandwidth-bound' if ai < ridge else 'compute-bound'}")
    assert arithmetic_intensity(1) < ridge < arithmetic_intensity(512)

    n = 2048
    g1, g64 = measure(n, 1), measure(n, 64)
    print(f"your CPU, {n}x{n} float32 weights: batch 1 = {g1:.1f} GFLOP/s, batch 64 = {g64:.1f} GFLOP/s ({g64/g1:.1f}x)")
    assert g64 > 2 * g1, "the same weights should deliver several times the FLOP/s at batch 64 than at batch 1"
    print("same weights, same FLOPs per sequence: the small batch is waiting on memory, not arithmetic")
    print("OK")
