### Answer key: Module 15

### Quiz answers and reasoning

1. Small-batch decode reads every weight per token with few FLOPs per byte, so it sits left of the ridge: bandwidth-bound. Large-batch prefill does many FLOPs per byte read, right of the ridge: compute-bound. Lab 12 measured a 47x throughput difference on the same weights.
2. Library reductions are already near the hardware limit and tested; NVIDIA's team won most leaderboard problems that way. Hand-write for a novel algorithm, tight fusion with surrounding ops, or an unusual memory pattern.
3. Unrealistic baselines (fp32 instead of TF32), test inputs the kernels had been tuned on, and hard-coded bypasses for specific tensor values. Hidden distributions and library baselines removed the illusion.
4. Ridge = 990e12 / 3.35e12 ≈ 296 FLOPs per byte; decode intensity is 2 x batch / 2 bytes = batch, so the crossover is about batch 296.
5. It trades extra draft compute for fewer sequential steps; the benefit depends on the acceptance rate, which collapses on adversarial or out-of-distribution prompts and when the draft model diverges from the target.
6. Engine version, hardware, TTFT, TPOT, p99 latency, VRAM, batch size, and output quality. One throughput number hides the latency tail, the memory cost and whether quality was traded away.

### Lab assessment and mastery gate

The reviewer runs the benchmark on a hidden input set and compares against the library baseline. A kernel that only beats a naive loop fails. They ask for the roofline placement on paper.

### How to use this key

Open after the quiz. Question 1 is the first question in every inference interview.
