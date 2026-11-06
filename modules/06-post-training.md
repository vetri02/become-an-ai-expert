# Module 06: Post-training: SFT, preference and RL

## Prerequisites and measurable objectives

Prerequisite: Module 05. By the end you can:

1. Explain what pretraining, supervised fine-tuning and RL post-training each change, and what data each needs.
2. Run SFT and a GRPO-style RL run on your nanochat model, with evals before and after.
3. Explain reward hacking and the KL penalty from a run you did yourself.

**Primary resource:** Raschka, Build a Reasoning Model (From Scratch), chapters 3 to 7 (https://sebastianraschka.com/reasoning-from-scratch). Finish it before adding anything from the reading list.
**Hours:** 12 guided: 11 on the concept blocks, 1 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why this is where models become products

A pretrained model completes text; post-training makes it answer, follow a format, and reason. It is also where things go wrong quietly: a learner who trained three models for $750 found GRPO degrading general ability at small scale; a 2026 GRPO write-up found the policy spamming comments to game a compile reward. Principle 8: RL optimises the reward and can degrade anything the reward does not measure.

## Concepts, in order

1. **Supervised fine-tuning** (2 hours): instruction data, chat templates, loss masking on the prompt, what changes (format, behaviour) and what does not (knowledge). Raschka chapters 6 and 7; smol-course unit on instruction tuning.
2. **Preference optimisation** (2 hours): pairs, DPO in one page, why it is cheaper than RLHF. smol-course unit on preference alignment.
3. **RL with verifiable rewards** (3 hours): policy gradient, REINFORCE, group-relative baselines (GRPO), the KL penalty to a reference, reward design, format rewards. Raschka, "Build a Reasoning Model (From Scratch)" chapters 6 and 7. Lab 09. CS336 lectures 15 and 16.
4. **Inference-time scaling** (1 hour): best-of-N, majority voting, self-refinement and when it makes answers worse. Raschka chapters 4 and 5.
5. **Evaluation by capability** (2 hours): a reasoning eval, a format eval and a general-ability eval kept separate; why one aggregate score hides the trade-off. Hamel Husain's rule that generic metrics are exploration signals, not quality.
6. **Reward hacking in the wild** (1 hour): the nilenso OCaml write-up, inspecting completions rather than metrics, tracking reward variance within a group.

## Lab

`labs/lab09_rl_reward_hacking.py`. Expected observations: with a count reward and no KL penalty, reward reaches 8 of 8, held-out loss rises from about 1.28 to about 3.4, and every token is "please"; with a KL coefficient of 2, reward about 1.2 and loss about 1.29.

## Build

**Project 5b: post-train your model.** On the nanochat model from Module 05:

- One SFT run on a small instruction set; a format eval before and after
- One GRPO run with a verifiable reward (math or a code check); a capability eval and a general-ability eval before and after
- A write-up of what broke: the trade-off between the rewarded capability and general ability, and what the KL coefficient did when you changed it once

**Project 7: one ablation.** One variable (KL coefficient, group size, reward shaping), three settings, one plot, one paragraph.

**Deliverables:** the post-training write-up as a post, with the eval table across stages; the ablation plot in your repo.

## Mastery gate

Your eval table has pretrain, SFT and RL rows with separate capability and general-ability columns, and you can explain, from your own run, why the RL row moved the way it did.

## Quiz

1. What does SFT change in a model, and why is it a poor way to add facts?
2. Write the REINFORCE gradient in words: what gets pushed up and what gets pushed down?
3. What does the group-relative baseline in GRPO do, and why does it reduce variance?
4. Why does a KL penalty to the reference model limit degradation, and what does it cost?
5. Describe one reward-hacking failure you have seen (in lab 09 or your own run) and the reward change that would prevent it.
6. Why evaluate by capability rather than one aggregate score?
7. When does best-of-N help and when does self-refinement hurt?

## Primary-source reading

- Raschka, Build a Reasoning Model (From Scratch): https://sebastianraschka.com/reasoning-from-scratch
- smol-course units on instruction tuning, preference alignment, RL: https://huggingface.co/learn/smol-course/en/unit0/1
- CS336 lectures 15 and 16: https://cs336.stanford.edu/
- DeepSeek-R1 (GRPO at scale): https://arxiv.org/abs/2501.12948
- InstructGPT: https://arxiv.org/abs/2203.02155
- nilenso GRPO write-up (2026-05-18): https://blog.nilenso.com/blog/2026/05/18/training-a-small-model-to-write-better-ocaml-with-rlvr-and-grpo/
- GRPO degrading general ability at small scale: https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/comment/p494xck/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me, from my own run, why the RL row moved and what the general-ability column shows.
2. Design a reward with me that the policy could game, then ask how I would detect the gaming.
3. Quiz me on what SFT can change and what RL can change, with one example each.
