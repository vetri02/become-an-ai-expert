# Module 11: Fine-tuning for behaviour

## Prerequisites and measurable objectives

Prerequisite: Modules 06 and 08. By the end you can:

1. Decide, with evidence, when to fine-tune and when not to.
2. Run a LoRA fine-tune of a small open model for a format or behaviour target, evaluated against a prompt-only baseline.
3. Explain why fine-tuning does not reliably add facts.

**Primary resource:** Raschka, Build a Large Language Model (From Scratch), chapters 6 and 7 (https://sebastianraschka.com/llms-from-scratch). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 8 guided: 7 on the concept blocks, 1 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why this is the shortest Stage 3 module

Because the main skill is knowing when not to. Principle 10: fine-tuning changes behaviour, not reliably knowledge. 57% of surveyed production teams do not fine-tune. The cases where it wins are specific: a strict output format, a house style, a narrow classification at low latency, or a small model replacing a large one on a well-defined task.

## Concepts, in order

1. **The decision** (1 hour): prompt first with the best model; retrieval for knowledge; fine-tune only when a measured gap remains in behaviour or format, or when cost and latency demand a small model. Write the decision down (the architecture-decision template).
2. **LoRA and QLoRA** (2 hours): low-rank adapters; why they fit on one GPU; rank and target modules; merging. Costs a few dollars for a 7B to 8B model (two to four hours on a rented GPU).
3. **Data** (2 hours): a few hundred to a few thousand clean examples beat tens of thousands of noisy ones; a learner's whole career started with six months of hand-built datasets. Deduplicate; hold out; version.
4. **Evaluation against the baseline** (1 hour): the same golden set and graders as Module 08, run on prompt-only, retrieval-plus-prompt, and fine-tuned variants; report quality, cost and latency for each.
5. **What goes wrong** (1 hour): catastrophic forgetting on general ability; overfitting to the format; the new facts that did not stick. Keep the general-ability eval from Module 06.

## Lab

No new lab. Re-run `labs/lab09_rl_reward_hacking.py` and note that SFT is the same gradient machinery without the reward: it moves what the data moves and nothing else.

## Build

**Project 11: fine-tune versus not.** Pick a behaviour target from your Project 9 agent (a structured output, a classification step, a style). Build the three variants, run the Module 08 harness on all three, and decide. Cost should be under $20.

**Deliverables:** an architecture decision record with the numbers; the adapter in your repo if it won; a post either way, "Why I did (not) fine-tune".

## Mastery gate

Your decision record shows three variants with quality, cost and latency, and your reviewer agrees the decision follows from the numbers.

## Quiz

1. Give two cases where fine-tuning is the right call and two where it is wrong.
2. What does LoRA change, and why is it cheap?
3. Why did the fact you fine-tuned in not stick, mechanically?
4. You fine-tuned for JSON output and the model got worse at reasoning. Name the failure and the eval that would have caught it.
5. How many examples do you need, and what matters more than the count?

## Primary-source reading

- Raschka, chapters 6 and 7 (fine-tuning): https://sebastianraschka.com/llms-from-scratch
- smol-course instruction-tuning unit: https://huggingface.co/learn/smol-course/en/unit0/1
- RAG vs fine-tuning in production: https://www.reddit.com/r/Rag/comments/1wbhsdi/comment/p8pycuc/
- Data quality beats scale (u/bralynn2222): https://www.reddit.com/r/LocalLLaMA/comments/1vi8jlr/comment/p2btrbo/
- LoRA cost ranges (vendor, July 2026): https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Read my decision record and argue for the variant I rejected. Make me defend my choice with the numbers.
2. Ask me when fine-tuning wins and when retrieval wins, with one example of each from my project.
3. Quiz me on what SFT moves and what it does not.
