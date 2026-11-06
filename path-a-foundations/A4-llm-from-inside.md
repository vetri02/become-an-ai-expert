# A4. Understand the model from the inside

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 50 guided hours; the longest on-ramp module and the one that matters most. Unguided practice on top is expected.
**Goal:** Build a small GPT-class model end to end so you understand tokenization, attention, training, post-training (SFT and RL), evaluation and inference. Hiring managers in 2026 say this is what separates "the API-calling crowd" from engineers they trust.
**Principles:** Principles 1, 2, 4, 5, 6, 7 and 8 (the model). Labs 02, 03, 05, 06, 07, 08 and 09 demonstrate them; run each one as you reach it.

## Learn, in this order

1. **Karpathy, Neural Networks: Zero to Hero (about 14.5 hours of video).** Watch each lecture, then re-type the code yourself from memory, pausing the video. Order: micrograd, makemore 1 to 5, "Let's build GPT", "Let's build the GPT tokenizer". A staff MLE said he spent three months on the Transformer and two weeks building one from scratch, after which GPT and Llama papers "became quick reads".
2. **Sebastian Raschka, "Build a Large Language Model (From Scratch)".** Work through the book's code. It builds a GPT-2 class model, loads pretrained weights, then fine-tunes for classification and instruction following. Runs on a laptop.
3. **The breakthrough papers only.** "Attention Is All You Need", GPT-2, GPT-3 (skim), scaling laws (Kaplan or Chinchilla), InstructGPT/RLHF, DeepSeek-R1/GRPO. Read each twice. Skim the derivatives. Senior people warn against reading every new arXiv paper.
4. **Stanford CS336, Language Modeling from Scratch (Spring 2026, public lectures).** Lectures 1 to 3 (tokenization, PyTorch resource accounting, architectures), 9 and 11 (scaling laws), 10 (inference), 12 (evaluation), 15 and 16 (SFT/RLHF and RLVR). Assignment 1 is a great self-test. Prerequisites are real: do not start this before Zero to Hero and the Raschka book.
5. **Hugging Face smol-course v2 (free).** Units on instruction tuning, evaluation and preference alignment (DPO). Hands-on with TRL on a small model.
6. **Raschka, "Build a Reasoning Model (From Scratch)" (2026).** Chapters 3 to 7: evaluation, inference-time scaling (best-of-N, majority voting), RL with verifiable rewards, GRPO. Starts from a pretrained Qwen3-class model, so it is fast to run.

## Build

**Project A4a: train your own GPT with nanochat.**
Karpathy's nanochat runs the full pipeline (tokenizer, pretraining, SFT, eval, inference) on an 8xH100 node. GPT-2 grade costs about $48 on demand (about 2 hours) or about $15 on a spot instance. The CPU/Apple Silicon script trains a toy model for free if you want to test the pipeline first.
- Run the speedrun. Save the eval numbers.
- Then do one SFT run and one GRPO run on your model. Write up what broke and what changed in the evals. A Redditor did this for three models at about $750 total and found GRPO degraded general ability at small scale. That write-up is the kind of artifact that gets interviews.
- Keep a held-out eval set from day one and log everything (Weights & Biases is free for individuals).

**Project A4b: implement a KV cache and measure the speedup.**
Add a KV cache to your from-scratch GPT. Measure generation time for 100 tokens before and after. One learner went from 278 seconds to 28 seconds. Put the numbers in your README.

**Runnable references in `labs/`:** `lab05_bpe_tokenizer.py` (BPE train, encode, decode, and the vocabulary-size vs sequence-length trade-off), `lab02_attention.py` (causal attention with checks for averaging, causality and the sqrt(d) scaling), `lab03_kv_cache.py` (cached vs uncached generation, identical outputs, measured speedup). Run all three before Zero to Hero so you know what you are looking for.

**Done when:** you can draw the Transformer forward pass on a whiteboard, explain what SFT and GRPO each change, and show your own eval numbers before and after each step.

## Skip for now

- Training only on MNIST or Titanic.
- Reading every paper. Breakthroughs only.
- Multi-node distributed training. That is Track B.

## Checkpoint

1. What does a tokenizer do, and why does vocabulary size matter for cost?
2. Walk through attention: what are Q, K, V, and why divide by sqrt(d)?
3. What does the KV cache store and why does it make generation faster?
4. What is the difference between pretraining, SFT and RL post-training? What data does each need?
5. Your GRPO run improved the math eval and hurt the general eval. Name two possible reasons.

## Sources

- $750 three-model training write-up and lessons, Aug 2026: https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/comment/p494xck/
- "Build a small GPT end to end" advice, Jul 2026: https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owbvvsd/
- KV cache 278s to 28s: https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/ofjavn4/
- Staff MLE's 3 months on the Transformer: https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/
- nanochat README (costs verified Nov 2026): https://github.com/karpathy/nanochat
- CS336 Spring 2026 schedule (verified): https://cs336.stanford.edu/
- Zero to Hero: https://karpathy.ai/zero-to-hero.html
- Raschka, LLMs from scratch: https://sebastianraschka.com/llms-from-scratch
- Raschka, reasoning from scratch: https://sebastianraschka.com/reasoning-from-scratch
- smol-course: https://huggingface.co/learn/smol-course/en/unit0/1

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me to explain micrograd's backward pass from memory.
2. Make me trace tensor shapes through my small transformer.
3. Quiz me on why the causal mask matters and what lab 02 proves about it.
