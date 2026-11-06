# Module 05: Training, scaling laws and inference

## Prerequisites and measurable objectives

Prerequisite: Module 04. By the end you can:

1. Run a GPT-2-grade pretraining with nanochat, log it, and read the loss curve.
2. Explain scaling laws and compute-optimal allocation, and show a power-law fit on your own data.
3. Implement a KV cache, prove outputs are identical, and measure the speedup; compute serving memory for any model config.

**Primary resource:** Karpathy, nanochat, read end to end then run (https://github.com/karpathy/nanochat). Finish it before adding anything from the reading list.
**Hours:** 13 guided: 9 on the concept blocks, 4 on the lab, Target 05 and the first pass of the build. Unguided practice on top is yours.

## Why training and inference are one module

Training produces the weights; inference is what you pay for. The same arithmetic (parameters, tokens, bytes) governs both, and the KV cache is where Principle 5 (sequential generation) meets Principle 6 (memory bounds inference). A learner who measured a KV cache going from 278 seconds to 28 seconds for 100 tokens had a better interview story than most courses produce.

## Concepts, in order

1. **The training loop as a system** (2 hours): data loading, batching, the optimiser (AdamW in one page), learning-rate schedules, gradient clipping, mixed precision, checkpointing, logging to Weights & Biases. CS336 lecture 2 (resource accounting) is the model.
2. **Scaling laws** (2 hours): loss as a power law in data, parameters and compute; Chinchilla's compute-optimal split; why small models on more tokens keep matching large ones. Lab 08. CS336 lectures 9 and 11.
3. **GPUs and memory in one afternoon** (2 hours): where a training step's memory goes (weights, gradients, optimiser state, activations); why bf16; what an 8xH100 node is. CS336 lecture 5.
4. **Inference** (2 hours): prefill versus decode; the KV cache and why it is linear not quadratic; cache size per token; batching; what a serving engine does. Labs 03 and 06. CS336 lecture 10.
5. **Evaluation during training** (1 hour): a held-out set from day one; what perplexity does and does not tell you; CORE-style benchmark suites. CS336 lecture 12.
6. **Run nanochat** (4 hours including the run): read the repo end to end first. Run the CPU script to test the pipeline. Then the speedrun on an 8xH100 node (about 2 to 3 hours, $15 to $75 depending on spot). Save every eval number.

## Lab

`labs/lab03_kv_cache.py`, `labs/lab06_serving_memory.py`, `labs/lab08_scaling_law.py`. Expected observations: identical tokens with a 10x-plus speedup; a 7B model in bf16 serving batch 32 at 4k context on 80 GB, and GQA multiplying that; held-out loss falling as a power law with an exponent near 0.65 toward the source entropy.

Then the target. Run `python3 -m targets.stale_cache.target`, write down every way you predict it fails, then fix `targets/stale_cache/hardened.py` until `python3 -m targets.stale_cache.check` prints all five flags. This is Target 05; Milestone B scores the write-up.

## Build

**Project 5a: the nanochat run.** The speedrun completed with your eval table, your loss curve, and a cost line. Then one change (learning rate, tokenizer size, or data mix) and the effect, in a plot.

**Project 6: KV cache in your own GPT.** From Module 04's model: add the cache, prove identical outputs on 100 tokens, report before/after time and cache size.

**Deliverables:** the run write-up as a post, "I trained a GPT-2 for $X and here is what I learned", and the KV-cache numbers in your repo's README.

## Mastery gate

The nanochat eval table exists with your numbers. The KV cache proof and timing are in your repo. You compute from memory the memory needed to serve an 8B GQA model at batch 16 with 4k context.

## Quiz

1. Where does the memory go in one training step of a 1B-parameter model with AdamW in mixed precision? Give the multiples of the parameter count.
2. State Chinchilla's result in one sentence and say what it implies for a fixed budget.
3. Why is decode at small batch bandwidth-bound while prefill is compute-bound?
4. Compute the KV cache per token for 32 layers, 8 KV heads, head size 128, bf16.
5. Your loss curve plateaus early. Name three things to check, in order.
6. What does the power-law exponent in lab 08 tell you about the value of ten times more data?
7. Why keep a held-out set from day one even for a toy model?

## Primary-source reading

- nanochat: https://github.com/karpathy/nanochat
- CS336 Spring 2026 (lectures 2, 5, 9, 10, 11, 12): https://cs336.stanford.edu/
- Hoffmann et al., Chinchilla: https://arxiv.org/abs/2203.15556
- Kaplan et al., Scaling laws: https://arxiv.org/abs/2001.08361
- vLLM paged attention docs: https://docs.vllm.ai/
- Three LLMs from scratch for $750, lessons: https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/
- KV cache 278s to 28s: https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/ofjavn4/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Give me a model size, batch and context length. Make me compute the serving memory on paper, then check it against lab 06.
2. Review my nanochat eval table and ask me for the noise band on each number.
3. Help me with the stale-cache target by asking what the failing grader stage says. Do not write hardened.py.
