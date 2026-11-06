# Module 16: Track C, research engineering

## Prerequisites and measurable objectives

Prerequisite: Milestone D. Choose one of Modules 14, 15 and 16. By the end of this one you can:

1. Replicate a recent paper exactly, then run a controlled ablation and write up negative results.
2. Implement GRPO-style post-training from scratch with a results table across settings.
3. Produce one research-grade artifact that an external reviewer has read, and apply to a fellowship.

**Primary resource:** ARENA curriculum, chapters 1 to 3 (https://learn.arena.education/). Finish it before adding anything from the reading list.
**Hours:** 24 guided, all inside the concept blocks above (the build is one of them); the lab run is counted there too.

## Who this track is for

People who want to be near the frontier and can run careful experiments. Be honest: Research Scientist roles at top labs still mostly want PhDs; Research Engineer roles and safety fellowships are open to strong self-taught people. Aleksa Gordić got a DeepMind Research Engineer role without an ML degree and says a Research Scientist role would likely have needed a PhD. Your public output must be research, not demos. 24 hours here, then a fellowship or an equivalent artifact.

## Concepts, in order

1. **Feedback-loop staging** (1 hour): Neel Nanda's method: a month of basics, then 1 to 5 day mini-projects, then 1 to 2 week sprints, continuing only the best; skills grouped by loop length (minutes: run and debug; weeks: when to pivot; months: ideas). "Gain surface area": explore a confusing system holding about four loosely held hypotheses; check toy theories against real messy models.
2. **ARENA chapters 1 to 3** (9 hours): interpretability (probes, sparse autoencoders, circuits), RL up to LLM post-training, evals. Free and self-paced; apply to a cohort via expression of interest.
3. **GRPO from scratch with ablations** (6 hours): Raschka chapters 6 to 8; your own GRPO notebook on a 1.5B to 4B model with LoRA on one GPU; ablate reward shaping, KL coefficient, group size; inspect completions not metrics; track reward variance within a group; evaluate intermediate checkpoints. A consultancy engineer's honest write-up (compile rate 2 in 10 to 7 in 10, with reward hacking) is the model artifact.
4. **Replicate, then ablate** (5 hours): one recent paper in your sub-area, replicated exactly; one question it did not answer, answered with one changed variable; a paper-style write-up with a limitations section and the negative results.
5. **The research record** (2 hours): externally reviewed output, then a strong first-author post on LessWrong or the Alignment Forum, then nothing, is how MATS reviewers rank applicants. Share in the communities where the work happens (EleutherAI, ARENA alumni, the paper's authors).
6. **Applying** (1 hour): MATS from a 2026 admit: a two-hour application, a 1.5-hour coding test on evaluating LLM outputs, a 1.5-hour research-taste test, stream essays of 4,500 words; 3 to 5 streams; rejected by 8 of 9 and still in; 35 to 40 hours total; acceptance 4 to 7%. Practise everyday Python without an assistant; avoid AI-written text in the application.

## Lab

`labs/lab08_scaling_law.py` and `labs/lab09_rl_reward_hacking.py` as the smallest ablation and RL harness; extend lab 09's ablation to three KL settings and plot.

## Build

**Project 15, Track artifact C:** the replication-plus-ablation write-up with negative results; the from-scratch GRPO notebook with a results table across settings; an interpretability probe or SAE study on a small open model with one clear finding (optional); one merged contribution to an evals library (inspect-ai) or a post-training library (TRL); a fellowship application submitted.

**Deliverables:** the write-up, the notebook, the PR, the application.

## Mastery gate

Someone outside your circle has reviewed the write-up in writing; the ablation changes exactly one variable; the results table includes the settings that did not work.

## Quiz

1. Why continue only the best mini-projects, and what tells you to pivot?
2. What is wrong with "GRPO improved the score from 0.41 to 0.57" as a result?
3. What is reward variance within a group a signal of, and why is it more useful than loss?
4. Why do negative results matter more in this track than elsewhere?
5. How do MATS reviewers rank applicants, and what does that imply for the next six months?
6. What makes an ablation controlled, and what breaks it?

## Primary-source reading

- Neel Nanda, how to become a mech interp researcher: https://www.lesswrong.com/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher
- ARENA: https://learn.arena.education/ and https://www.arena.education/
- Raschka, Build a Reasoning Model (From Scratch): https://sebastianraschka.com/reasoning-from-scratch
- nilenso GRPO write-up: https://blog.nilenso.com/blog/2026/05/18/training-a-small-model-to-write-better-ocaml-with-rlvr-and-grpo/
- MATS application write-up (Conway, 2026): https://evanjayconway.com/posts/2026/mats-application/
- MATS admissions FAQ: https://www.matsprogram.org/faq/getting-into-mats
- Lange, application guide: https://georglange.com/post/ai-safety-application-guide/
- Position: Embracing Negative Results in ML: https://arxiv.org/abs/2406.03980
- Gordić on RE vs RS: https://gordicaleksa.medium.com/how-i-got-a-job-at-deepmind-as-a-research-engineer-without-a-machine-learning-degree-1a45f2a781de
- Disillusionment with mech interp (required reading): https://www.reddit.com/r/MachineLearning/comments/1t6zdj6/comment/okm2arl/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me which one variable my ablation changes and what I would conclude if the result flipped.
2. Play the outside reviewer of my write-up and ask for the settings that did not work.
3. Make me state the paper's problem, mechanism, evidence and limits from my reading page.
