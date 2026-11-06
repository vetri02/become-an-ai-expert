# A7. Choose a track and go deep

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 5 hours to choose. The depth itself is 6 to 18 months to employable, years to expert.
**Goal:** Pick one end of the barbell and become the person who can go arbitrarily deep in it.
**Optional:** the professional path covers this in Stage 5 and the Advanced tracks page.
**Principles:** Principle 18 if you choose Track B, 8 if Track C, 16 and 19 if Track A.

## The barbell

A FAANG machine learning engineer described the 2026 market as a barbell. One end is foundation-model and infrastructure engineers: distributed training, kernels, inference. The other end is AI engineers shipping LLM products with eval harnesses, RAG and agent loops. The middle (train a classical model, ship it, monitor it) is being squeezed.

Senior people in 2026 threads agree that depth in one direction beats breadth. Shallow knowledge of five frameworks is worth less than deep knowledge of one stack. "Expert" in this course means the top of one track, not breadth across all three.

## How to choose

Answer these honestly after Milestone D, when you are choosing Module 14, 15 or 16:

| If you... | Track |
|---|---|
| Liked shipping to users, iterating on feedback, and arguing about product trade-offs | A. Applied AI engineer |
| Liked the KV-cache project most, enjoy profiling and making things fast, are curious about C++ or GPUs | B. AI infrastructure / inference / GPU |
| Liked the GRPO ablation most, want to run controlled experiments and write them up, can accept that pay and roles are scarcer without a PhD | C. Research engineer / post-training / interpretability |

Also weigh: Track B has the strongest compensation growth per the FAANG MLE post. Track C has the hardest entry (Research Scientist roles still mostly want PhDs; Research Engineer and safety fellowships are open). Track A has the most jobs.

Pay signals from 2026, for what they are worth: level-controlled, ML roles pay about 1.3x comparable non-AI software roles and that premium has stopped growing; inference and infrastructure specialists sit at the top of the band; "Machine Learning Engineer" titles pay well above "AI Engineer" titles for similar work; and "AI Engineer" is the fastest-growing title in postings. Pick by aptitude first. The pay gap between tracks is smaller than the gap between the median and the top of any one track.

Domain expertise multiplies any track. Hiring threads say domain plus ML beats generic ML. If you already know law, healthcare, finance, logistics or voice, keep it.

## What to do next

Open the track guide and follow it:

- [Track A: Applied AI engineer](../ADVANCED-TRACK.md#track-a-applied-ai-engineer)
- [Track B: AI infrastructure, inference and GPU](../ADVANCED-TRACK.md#track-b-inference-and-gpu-engineering)
- [Track C: Research engineer, post-training, interpretability](../ADVANCED-TRACK.md#track-c-research-engineering)

You can switch once. People do. But switching twice means you never got deep.

## Build

**Project A7: the two-week artifact.** Track B's guide names a two-week artifact (the benchmark table); for Track A it is the measured model swap in Module 14, for Track C the replication in Module 16. Build the one for your track, date it, and put it where a stranger can run or read it. Done when someone outside your circle has opened it and you have written down what they said.

## Sources

- Barbell description, FAANG MLE, May 2026: https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojovnqx/
- Depth beats breadth: https://www.reddit.com/r/MLQuestions/comments/1uhxdj3/comment/oun9yqi/ and https://www.reddit.com/r/CUDA/comments/1uwlc0r/comment/oxlicdi/
- Domain + ML beats generic ML: https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojpng9u/
- Levels.fyi on the AI premium (2026-08-26): https://letsdatascience.com/news/levelsfyi-tells-lds-the-ai-pay-premium-has-stopped-growing-a893d96e
- Posted-range analysis (2026-07-10): https://hotfix.jobs/blog/ai-engineer-salary-2026
- Niche depth as the top answer (u/weird_limbs, 61 pts) in "what actually worked": https://www.reddit.com/r/learnmachinelearning/comments/1umfxxp/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me the questions on this page and tell me which track my answers point to.
2. Challenge my track choice with the strongest case for each of the other two.
3. Help me plan the two-week artifact for my track, with a date.
