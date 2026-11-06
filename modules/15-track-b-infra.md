# Module 15: Track B, inference and GPU engineering

## Prerequisites and measurable objectives

Prerequisite: Milestone D. Choose one of Modules 14, 15 and 16. By the end of this one you can:

1. Trace one request through a serving engine end to end and explain where the time goes.
2. Profile before optimising, form a falsifiable hypothesis (bandwidth- or compute-bound), and write a Triton kernel with a fair benchmark.
3. Reproduce one serving optimisation (prefix caching or speculative decoding) and measure it.

**Primary resource:** GPU MODE lectures 1 to 4 (https://github.com/gpu-mode/lectures). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 24 guided, all inside the concept blocks above (the build is one of them); the lab run is counted there too.

## Who this track is for

People who like systems, C and C++, and finding out why something is slow. The FAANG MLE post says this end of the barbell has the strongest pay growth, and 2026 posted ranges put inference engineers at the top of the band. 24 hours here, then years.

## Concepts, in order

1. **Measure first** (4 hours): a benchmark harness for time-to-first-token and tokens per second across batch sizes on one GPU with vLLM, reporting engine version, hardware, TTFT, TPOT, p99, VRAM and output quality. GPU MODE lectures 1 to 4; CS336 lectures 5 and 6. Labs 06 and 12.
2. **Read the engine by file** (4 hours): vLLM's V1 scheduler and KV-cache manager, then the engine core's busy loop and step function, then the process split; for SGLang, the mini teaching implementation first. Write a post explaining paged attention from the code.
3. **Kernels** (8 hours): Triton first (vector add, then a matmul where memory access matters), CUDA when Triton leaves performance on the table; PMPP chapters 1 to 6 with the GPU MODE recap; CS336 assignment 2: FlashAttention2 in Triton with a speedup against the naive version; enter one GPU MODE leaderboard problem through popcorn-cli. The team that topped that leaderboard started from a proven library for sort, scan, reduce and histogram and hand-wrote only for novel patterns.
4. **Fair benchmarks** (2 hours): under a verified protocol, a model's "1.43x faster than PyTorch" became 0.88x; hidden test distributions and library baselines are mandatory for any speedup you publish.
5. **Reproduce an optimisation** (5 hours): add prefix caching or speculative decoding to a small from-scratch server and measure; understand acceptance rates and when they collapse; FP8 and NVFP4 claims verified on your own evals.
6. **Distributed basics** (1 hour): data, tensor and pipeline parallelism; FSDP; what breaks at 8 GPUs versus 64. CS336 lectures 7 and 8.

## Lab

`labs/lab06_serving_memory.py` and `labs/lab12_roofline.py`, then reproduce lab 12's batch effect on a real GPU.

## Build

**Project 15, Track artifact B:** the benchmark table; FlashAttention2 in Triton with a fair baseline; a Nsight-backed before/after on one named bottleneck (paged-attention decode, fused RMSNorm, HBM-bound attention at small batch); a GRPO or SFT run where you cut cost by profiling; one merged PR to vLLM, SGLang, llama.cpp, Triton or a quantisation library.

**Deliverables:** repo with benchmarks, the kernel post, the PR.

## Mastery gate

Your speedup survives a hidden test distribution and a library baseline; you place your kernel on the roofline for your reviewer; the PR is merged.

## Quiz

1. Place small-batch decode and large-batch prefill on the roofline and say what each is bound by.
2. Why start from a proven library for a reduction, and when do you hand-write?
3. What made the KernelBench speedups disappear under verification?
4. Compute the crossover batch for a GPU with 990 TFLOP/s and 3.35 TB/s at bf16.
5. What does speculative decoding trade, and what collapses its benefit?
6. What fields must a benchmark table carry, and why is one throughput number worthless?

## Primary-source reading

- vLLM docs and contributing guide: https://docs.vllm.ai/ and https://docs.vllm.ai/en/stable/contributing/
- GPU MODE lectures and leaderboard: https://github.com/gpu-mode/lectures and https://github.com/gpu-mode/popcorn-cli
- PMPP 4th ed.: https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0
- CS336 assignment 2: https://github.com/stanford-cs336/assignment2-systems
- NVIDIA on topping the GPU MODE leaderboard: https://developer.nvidia.com/blog/topping-the-gpu-mode-kernel-leaderboard-with-nvidia-cuda-compute/
- KernelBench-Verified: https://arxiv.org/abs/2607.16241
- Triton-first kernel path: https://anirudhs16.github.io/ai-systems/2026/08/29/triton-first-gpu-kernel/
- vLLM P-EAGLE: https://vllm.ai/blog/2026-03-13-p-eagle
- SWE closing inference-infra gaps (Oct 2026): https://www.reddit.com/r/learnmachinelearning/comments/1xfkwyp/comment/19rnuzo541r8k/
- Where to start with CUDA in 2026: https://www.reddit.com/r/CUDA/comments/1uwlc0r/comment/oxk528y/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me to place my kernel on the roofline and explain which wall it hits.
2. Challenge my speedup with a hidden test distribution and a library baseline.
3. Quiz me on prefill versus decode and what the KV cache costs at my batch size.
