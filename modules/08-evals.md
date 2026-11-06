# Module 08: Evals as a discipline

## Prerequisites and measurable objectives

Prerequisite: Module 07. By the end you can:

1. Run error analysis by hand, derive failure categories, and turn them into graders.
2. Build an eval harness with code-based graders, calibrated LLM judges (TPR and TNR against human labels), pass@k and pass^k, and a regression suite in CI.
3. Measure eval noise and tell a regression from sampling.

**Primary resource:** Hamel Husain and Shreya Shankar, AI Evals FAQ (https://hamel.dev/blog/posts/evals-faq/). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 16 guided: 12 on the concept blocks, 4 on the lab, Target 08 and the first pass of the build. Unguided practice on top is yours.

## Why this is the core skill

The 2026 interview round is "how did you measure hallucinations?". In a 1,340-team survey, 89% had observability but only 52% ran evals; quality was the top production blocker. Hamel Husain's rule is to start with error analysis and look at your data before building any infrastructure. Principles 11 to 15 and 19 are all measurement principles, and this module is where they become habits.

## Concepts, in order

1. **Error analysis first** (3 hours): read 20 to 50 real outputs, binary pass/fail, notes on each, group the notes into categories (open then axial coding), stop at saturation. One domain expert decides. Delay the rubric. Hamel Husain and Shreya Shankar's FAQ.
2. **Code graders** (1 hour): when a rule can detect the failure (JSON parses, cites a retrieved chunk, calls the allowed tool), write code. Groundedness as a code check.
3. **LLM judges, calibrated** (2 hours): one judge per failure mode; 100 to 200 labelled examples split train/dev/test; report true-positive and true-negative rates; position-swap to reduce bias; never trust a generic "helpfulness" score. Lab 04.
4. **Agent evals** (2 hours): 20 to 50 tasks from real failures; grade outcomes not paths; partial credit; pass@k for capability and pass^k for reliability; a 0% pass rate usually means a broken task; clean environment per trial; saturated evals move to the regression suite. Anthropic's guide.
5. **Noise and regressions** (2 hours): run the same suite twice to learn the noise band; tag regression versus capability cases; your suite is overfit to the incumbent model; re-baseline after migration. Lab 13.
6. **Evals in CI** (1 hour): the golden set runs on every change; the build fails on quality, cost or latency regressions beyond the noise band; a dashboard of pass rate over time.
7. **Abstention** (1 hour): how often the system says "I don't know" when retrieval returns nothing relevant. This is the answer interviewers want to "how did you measure hallucinations".

## Lab

`labs/lab04_eval_harness.py` and `labs/lab13_model_upgrade.py`. Expected observations: groundedness about 0.78 with a 20% hallucinating generator; judge TPR 0.89 and TNR 0.71 on 400 labels; pass@3 0.98 versus pass^3 0.42 at p=0.75; a v2 model whose overall score rises while injection resistance falls from 0.91 to 0.30.

Then the target. Run `python3 -m targets.leaky_eval.target`, predict every wrong number before you look, then fix `targets/leaky_eval/hardened.py` until `python3 -m targets.leaky_eval.check` prints every flag. This is Target 08; Milestone C scores the write-up.

## Build

**Project 9 (part 1): the harness for your retrieval system.** On Project 8:

- Error analysis of 50 outputs with categories and counts
- A code grader for groundedness and one for abstention
- One LLM judge for the failure mode code cannot catch, calibrated on 100 labelled examples with TPR and TNR reported
- Noise measured by two runs; a regression suite in CI that fails beyond the noise band
- A dashboard (a notebook plot counts) of pass rate per category across three changes

**Deliverables:** the harness in the repo; a post, "What 50 outputs taught me that my metric did not".

## Mastery gate

Your reviewer picks one category and you show the raw outputs that defined it. Your judge's TPR and TNR are in the README. Your CI fails when they inject a regression.

## Quiz

1. Why error analysis before tooling? What does a metric chosen first miss?
2. When do you use a code grader versus an LLM judge?
3. Your judge agrees with humans 80% of the time. Is that good? What would you do next?
4. Explain pass@k versus pass^k and compute both for p=0.6, k=4.
5. How do you measure eval noise, and why must you before claiming a regression?
6. Why is your eval suite overfit to the incumbent model, and what do you do before a migration?
7. How would you measure hallucination rate in a retrieval system? Include abstention.

## Primary-source reading

- Hamel Husain and Shreya Shankar, AI Evals FAQ: https://hamel.dev/blog/posts/evals-faq/
- Anthropic, Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Eval suites overfit to the incumbent (Tian Pan, 2026-07-03): https://tianpan.co/blog/2026/07/03/your-eval-suite-is-overfit-to-your-incumbent-model
- promptfoo guides: https://www.promptfoo.dev/docs/category/guides/
- Interviewer's question bank (abstention eval): https://chiraghasija.cc/posts/how-to-interview-ai-engineer-role-2026/
- How engineers evaluate RAG in practice: https://www.reddit.com/r/learnmachinelearning/comments/1t81t7i/comment/okswmh3/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Pick one of my error categories and make me show the raw outputs that defined it.
2. Ask me for my judge's TPR and TNR, and what 80% agreement with humans would mean.
3. Help me with the leaky-eval target by reading the failing grader stage with me. Do not write the fix.
