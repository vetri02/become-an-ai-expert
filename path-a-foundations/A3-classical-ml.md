# A3. Classical ML as table stakes

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 40 guided hours.
**Goal:** Frame a problem, train a baseline, evaluate it honestly, and explain what went wrong. This is the vocabulary every later module uses. It is not the career.
**Principles:** Principles 12 and 13 (error analysis before tooling; held-out, versioned test sets). Lab 04 demonstrates 13; 12 is a method, practised in Project 3.

## Why only six weeks

A machine learning engineer with ten years of experience said in a July 2026 thread (29 upvotes) that 98% of the classical model-tuning use cases went to cheap LLM API calls, and that the "middle" of the market (train a classical model, ship it, monitor it) is being squeezed. But every interviewer still expects you to know train/test splits, cross-validation, leakage and metrics cold. So learn it well and move on.

## Learn

1. **Andrew Ng, Machine Learning Specialization (Coursera, audit free).** Courses 1 and 2. Still the standard intro in November 2026 threads. Do the labs; do not just watch.
2. **scikit-learn in practice.** Pipelines, ColumnTransformer, cross_validate, GridSearchCV. Read the "Getting started" and "Common pitfalls" pages of the official docs.
3. **The discipline of evaluation.** Train/validation/test splits, k-fold cross-validation, stratification, data leakage (and how it hides in time-series and grouped data), class imbalance, calibration, choosing a metric that matches a business decision.
4. **Error analysis.** Take the 50 worst predictions, read them one by one, and categorize why they failed. This habit is what senior people say separates engineers from course-completers, and it carries straight into LLM evals in A5.
5. **Framing.** For any problem: what is the unit of prediction, what is the label, when is it known, what decision does the prediction drive, what is the cost of each error type.

## Build

**Project A3: one tabular project done properly.**
Pick a messy real dataset (not Titanic, not Iris; try a city open-data portal, Kaggle datasets with low activity, or data from your own life or job).
- A notebook with: problem framing in two paragraphs, a baseline (majority class or mean), two models compared with cross-validation, a metric chosen for a stated reason
- An error-analysis section: 30 worst cases, categorized, with one fix attempted and its measured effect
- A leakage check: one sentence per feature on whether it would be known at prediction time
- Deploy the best model behind your A1 FastAPI service

**Done when:** you can say, with numbers, why your model is better than the baseline, where it fails, and what you would try next.

## Skip for now

- Deep learning. It arrives in A4 and you will understand it better for having done this.
- Kaggle leaderboard chasing. Competitions helped some people get a first job (one got a data science role from a DrivenData placement), but an ex-FAANG MLE calls them "basically useless" for big-tech MLE roles. Use Kaggle for datasets and notebooks to read, not for ranking.
- AutoML tools.

## Checkpoint

1. Describe three ways data leakage can happen and how you would detect each.
2. Why is cross-validation better than a single split? When can it still mislead you?
3. Your model's precision is 0.9 and recall 0.2. Is that good? For which business would it be?
4. Walk through the error analysis of your project. What was the biggest failure category?

## Sources

- 10-YOE MLE on classical ML being squeezed: https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owc6cz1/
- Andrew Ng still recommended, Nov 2026 resources thread: https://www.reddit.com/r/learnmachinelearning/comments/1xn1n85/
- Framing and evaluation matter most (u/irndk10, 2,000+ upvote manifesto): https://www.reddit.com/r/datascience/comments/1hp7pim/
- Kaggle as a mixed signal: https://www.reddit.com/r/learnmachinelearning/comments/1vkco40/
- Low-activity Kaggle datasets tip (u/InSandAndTea): https://www.reddit.com/r/phcareers/comments/vgfpw8/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me how I split my data and where leakage could hide.
2. Make me explain precision and recall using my own confusion matrix.
3. Review my one-page evaluation report as a hiring manager would.
