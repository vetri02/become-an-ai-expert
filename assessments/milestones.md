# Five performance milestones

Each milestone is scored out of twenty under the peer-review protocol: five criteria, 0 to 4 each. Score 0 for missing evidence, 1 to 2 for an incomplete artifact, 3 for a sound artifact with limited measurement, and 4 for reproducible evidence with the measurement, its noise and its limitations stated. 14 of 20 passes. A high score never overrides a failed mastery gate.

## Milestone A: foundations, after Module 02

Five four-point criteria:

- A deployed service a stranger runs in three commands, with tests that exercise a failure path.
- A profiling before/after with numbers, and one assistant-written bug you caught and explained.
- A tabular project with a baseline, cross-validated comparison and a metric chosen for a stated reason.
- Error analysis of the 30 worst cases, categorised, with one fix measured.
- A leakage note per feature and a drawing of gradient descent that a reviewer accepts.

Challenge: your model is 94% accurate and your reviewer says "so what?". Answer with the baseline, the metric that matches the decision, and the biggest failure category.

## Milestone B: the model from the inside, after Module 06

- A from-scratch GPT that trains and samples, with the forward pass whiteboarded with shapes.
- The nanochat run: eval table, loss curve, cost line, and one change with its measured effect.
- A KV cache with the identical-output proof, timing and cache size.
- SFT and GRPO runs with separate capability and general-ability columns, and what the KL coefficient did.
- One ablation: one variable, three settings, one plot, one paragraph.
- Target 05 (stale cache): all five flags print, and the repo holds your prediction list, an explanation of each invariant, the negative tests you added beyond the grader's, and a limits paragraph.

Challenge: your GRPO row improved the math eval and hurt the general eval. Explain the mechanism (Principle 8), what the KL term does, and what you would change in the reward.

## Milestone C: AI engineering with measurements, after Module 11

- Retrieval over a messy corpus with a versioned golden set and recall@k before and after one change; a permission test that proves a forbidden chunk never returns.
- An eval harness: error-analysis categories with raw examples, a code grader, a judge with TPR and TNR against 100+ labels, noise measured, a CI gate that fails on injected regressions.
- An agent with rules in code, a step cap and budget, pass@3 and pass^3 reported, and a documented list of unfixed failures with reasons.
- A cost cut: cost per request halved, the eval unchanged within the noise band, the levers named; the injection suite in CI with the trifecta broken in code; Targets 08 and 10 with every flag printing and, for each, the prediction list, invariant explanations, extra negative tests and limits paragraph in the repo.
- A fine-tune-or-not decision record with three variants and quality, cost and latency for each; at least five real users for two weeks with a changelog.

Challenge: a model upgrade raises your overall score by 5 points. Show, from your own suite, how you would know whether a safety category regressed, and what you do before rollout.

## Milestone D: getting in, after Module 13

- A pilot pitch with a dollar cost and a delivered pilot with eval numbers and failure cases.
- Three public posts with numbers, one runnable repo with the finished README, one talk.
- One upstream PR opened, following the project's contributing guide, with every line reviewed by you.
- The application kit: portfolio page, numbered resume, ten timed system-design prompts.
- A recorded mock interview in which the depth probe runs five levels deep on one project for 20 minutes without you running out.

Challenge: an interviewer asks "how did you measure hallucinations?". Answer in 60 seconds with your own numbers; your reviewer times it.

## Milestone E: track depth, after Module 14, 15 or 16

- The track artifact, complete as the module defines it.
- One merged upstream contribution.
- Track A: a model upgrade demonstrated as config plus eval run, and the trifecta broken in code. Track B: a speedup that survives a hidden test distribution and a library baseline, placed on the roofline. Track C: a replication plus one-variable ablation with negative results, reviewed by someone outside your circle.
- A public write-up of the artifact with numbers and a limitations section.
- A talk given, or a cohort or fellowship application submitted.

Challenge: a stranger reads your write-up and asks the hardest "why" you can imagine. Write the question and your answer.

## Submission checklist

For each milestone include: commit identifier; environment and setup; exact commands; the measurement, its denominator and its noise; what you expected before running; what you observed; limitations; next steps. Anything not run (a GPU run you could not afford, users you could not recruit) must say "not done", not be implied. Grade reasoning and reproducibility, not screenshots.

Use the instructor keys for module reasoning and [the capstone](../CAPSTONE.md) for the final practical assessment.
