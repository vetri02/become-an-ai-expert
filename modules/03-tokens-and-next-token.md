# Module 03: Tokens and the next-token objective

## Prerequisites and measurable objectives

Prerequisite: Module 02, or A5 on the Novice track. By the end you can:

1. Explain Principle 1 (a language model is a next-token distribution; everything else is repeated sampling) and demonstrate it with code you wrote.
2. Implement byte-pair encoding, encode and decode losslessly, and show how vocabulary size trades off against sequence length and cost.
3. Explain why a model cannot know facts outside its training data and what temperature does to sampling.

**Primary resource:** Karpathy, Neural Networks: Zero to Hero, the makemore and tokenizer lectures (https://karpathy.ai/zero-to-hero.html). Finish it before adding anything from the reading list.
**Hours:** 6 guided: 5 on the concept blocks, 1 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why this comes before attention

If you do not have Principle 1 and Principle 2 cold, every later topic (RAG, agents, cost, evals) is mysterious. With them, most of the field is obvious. Hiring managers in 2026 distinguish engineers who understand the model from "the API-calling crowd" on exactly this.

## Concepts, in order

1. **The objective** (1 hour): next-token cross-entropy. A trigram model is a language model. Sampling, greedy decoding, temperature, top-k and top-p as reshapings of one distribution. Chat is tokens appended in a loop; a tool call is tokens the harness parses. Lab 07.
2. **Tokens** (2 hours): bytes, characters, words, subwords. Byte-pair encoding: merge the most frequent pair, repeat. Vocabulary size versus sequence length. Why "strawberry" has a letter-count problem and why numbers tokenize badly. Karpathy, "Let's build the GPT tokenizer". Lab 05.
3. **Embeddings** (1 hour): a token id becomes a vector; similarity as a dot product; the unembedding at the end. This is the first half of Module 04.
4. **Cost as tokens** (1 hour): input and output tokens, prices per million, why a verbose system prompt costs money on every call. Count tokens for one of your own documents with a provider's tokenizer.
5. **Karpathy, Zero to Hero: micrograd and makemore 1 to 3** (2 hours of video, watched in pieces, code retyped from memory). Makemore is a character-level next-token model; it is Principle 1 at the smallest scale.

## Lab

`labs/lab07_next_token.py` and `labs/lab05_bpe_tokenizer.py`. Expected observations: P("token" | "the next") about 0.85; near-zero temperature is repeatable; an unseen word gets only smoothing mass; 40 bytes become about 20 tokens after 100 merges with a lossless round trip.

## Build

**Project 4a: your own tokenizer and n-gram model on your own text.** Take a corpus you care about (your emails, a book, your project's docs). Train BPE with 500 merges; report bytes per token at 0, 100, 500 merges. Train a trigram model; sample 200 tokens at three temperatures; write up what is wrong with the samples and why a trigram cannot fix it. Count the cost of sending the corpus to a provider at current prices.

**Deliverables:** a notebook and a 400-word post, "What a language model actually is".

## Mastery gate

You can state Principle 1 without notes, explain to a non-engineer why the model "makes things up" using only the words "probability" and "training data", and show your tokenizer's trade-off table.

## Quiz

1. Why is a chat transcript just one long token sequence from the model's point of view?
2. What does temperature change and what does it not change?
3. Why does a bigger vocabulary make sequences shorter, and what is the cost of a bigger vocabulary?
4. Why does the model struggle to count letters in a word?
5. A 6,000-token system prompt is sent on every request. Compute the daily input cost at 10,000 requests and $3 per million tokens.
6. Why does an unseen word get non-zero probability in lab 07, and what is the LLM equivalent?

## Primary-source reading

- Karpathy, Zero to Hero: https://karpathy.ai/zero-to-hero.html
- Raschka, Build a Large Language Model (From Scratch), chapter 2: https://sebastianraschka.com/llms-from-scratch
- Boykis on learning the same fundamentals in 2026: https://vickiboykis.com/2026/10/17/how-to-learn-ml-in-2026-interview/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Make me state Principles 1 and 2 from memory, then keep asking why until I run out.
2. Here is my tokenizer trade-off table. Ask me what a bigger vocabulary costs and what it buys.
3. Play a non-engineer and ask me why the model makes things up. Grade my answer against the module.
