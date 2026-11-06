# Module 04: Attention and the Transformer

## Prerequisites and measurable objectives

Prerequisite: Module 03. By the end you can:

1. Implement causal self-attention from scratch and verify its three properties (weighted average, causality, scaling).
2. Draw the full GPT forward pass on a whiteboard: embeddings, positional information, attention, MLP, residuals, layer norm, unembedding.
3. Train a small GPT on text and sample from it.

**Primary resource:** Raschka, Build a Large Language Model (From Scratch), chapters 3 to 5 (https://sebastianraschka.com/llms-from-scratch). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 14 guided, which the concept blocks above account for in full; the lab run and the build fit inside them.

## Why this is the hinge of the course

Nathan Lambert (Ai2): "The Transformer architecture is as fundamental today as deep learning was in the past, and people need to learn it." A FAANG staff engineer spent three months on it and two weeks building one, after which every later paper "became quick reads". Fourteen hours here save months later.

## Concepts, in order

1. **Attention as a weighted average** (2 hours): queries, keys, values; softmax rows sum to one; the causal mask; why divide by the square root of the head size. Lab 02. Principle 4.
2. **Multi-head attention and the block** (2 hours): heads as parallel subspaces; the MLP; residual connections and why depth trains; layer norm; the whole block. Raschka chapter 3 and 4, or Karpathy "Let's build GPT".
3. **Positions** (1 hour): learned positions, then rotary embeddings in one page. Why a Transformer without position information is a bag of tokens.
4. **Build GPT** (5 hours): Karpathy "Let's build GPT" retyped from memory; Raschka chapters 4 and 5 are the unguided reading beside it. Train on a small corpus on a laptop or free Colab. Load GPT-2 weights and generate.
5. **The breakthrough papers** (2 hours): "Attention Is All You Need" and GPT-2, read twice each. Skim the derivatives; Lambert says some areas "might only have three papers you need to read".
6. **Zero to Hero makemore 4 and 5** (2 hours): backprop by hand through a network, then a WaveNet-style deepening. This is where backprop stops being magic.

## Lab

`labs/lab02_attention.py`. Expected observations: rows sum to one; editing token 6 changes only output 6; entropy of the last row about 2.7 scaled versus 0.0 unscaled at head size 256.

## Build

**Project 4b: your GPT.** A from-scratch decoder-only Transformer in PyTorch, trained on a corpus of your choice (a few megabytes), with:

- A plot of training and validation loss
- Samples at three checkpoints showing the model getting better
- A written walk-through of the forward pass for one token with tensor shapes at every step
- GPT-2 weights loaded into your architecture, with a generated paragraph

**Deliverables:** repo, plot, and the shape walk-through as a post.

## Mastery gate

Whiteboard the forward pass for your reviewer, with shapes, from memory, in under ten minutes. Your model trains and samples.

## Quiz

1. What are Q, K and V, and what does Q·K measure?
2. Why divide by sqrt(d)? What goes wrong without it, and what did lab 02 measure?
3. What does the causal mask do and why is it needed in training but not in cached decoding?
4. Why do residual connections make deep networks trainable?
5. A Transformer with no positional information: what can it still do and what can it not?
6. Give the tensor shapes for a batch of 8 sequences of 128 tokens through one attention layer with 12 heads of size 64.
7. What is the role of the MLP in a block, in one sentence?

## Primary-source reading

- Vaswani et al., Attention Is All You Need: https://arxiv.org/abs/1706.03762
- GPT-2 paper: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- Raschka, chapters 3 to 5: https://sebastianraschka.com/llms-from-scratch
- Lambert on the Transformer as fundamental (Lex Fridman #490): https://lexfridman.com/ai-sota-2026-transcript
- Staff MLE on three months with the Transformer: https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Time me whiteboarding the forward pass with shapes, and stop me the moment a shape is wrong.
2. My GPT training loss is flat. Ask what I have tried before you suggest one thing.
3. Quiz me on why residual connections and layer norm let depth train.
