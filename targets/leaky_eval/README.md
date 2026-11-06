# Target: the leaky harness

Module 08 companion. Time: four to six hours. Standard-library Python; no model, no network.

## Scenario

A team has an eval harness and a dashboard that says 0.96. The harness tunes the retriever on the same questions it then reports on, folds retrieval and generation into one number, trusts an LLM judge nobody has calibrated, raises an alarm on any drop at all, and reports "reliability" that is really pass@k. Every number on the dashboard is wrong in a different way, and each wrong number has a Principle (11 to 15, and 19) behind it.

The system under test is synthetic: twenty documents, four questions each, a retriever whose recall you control and a judge with a known error profile, so the grader can check your arithmetic exactly.

## Watch it fail

```bash
python3 -m targets.leaky_eval.target
```

It reports a near-perfect score, an 80-ish% "agreement" that hides the judge missing 30% of failures, and a reliability of 0.8 that is pass@k. Read `target.py` before you run it and write down which line causes each failure.

## Your task

Implement `HardenedHarness` in `hardened.py`, following the contract in its docstring, then run:

```bash
python3 -m targets.leaky_eval.check
```

| Stage | Invariant | Hint |
| --- | --- | --- |
| 1 | The test set was never tuned on | Split by document, not by question: four questions share a document, and tuning on one leaks to its siblings. Principle 13. |
| 2 | Retrieval and generation are measured apart | Two keys in the report. The grader hands you a system that retrieves perfectly and never grounds; it must read 1.0 and 0.0. Principle 11. |
| 3 | A judge has two error rates | Compute TPR on the human-pass labels and TNR on the human-fail labels; refuse a judge whose TNR is below 0.8. Principle 14. |
| 4 | Noise before regression | Run the same report over five seeds and take the population standard deviation; a drop inside twice that band is sampling. Principle 19. |
| 5 | Reliability is pass^k | All trials pass, per task. The fixtures give five tasks; one passes every trial. Principle 15. |

## Deliverables

1. `hardened.py` passing all five stages, with your name on it.
2. The prediction list you wrote before running the vulnerable build, marked right or wrong.
3. Three negative tests the grader does not run. Suggestions: a golden set with one document; labels with no failures (TNR undefined); a `noise` call with one run.
4. A limits paragraph. What does a passing grader not prove? At minimum: the fixture judge's error profile is known while a real one must be labelled; groundedness via citation is a proxy; five seeds is a small noise estimate; pass^k with three trials cannot show rare failures.

## What this target does not do

Nothing here calls a model. The retriever is a coin, the judge is a coin with a bias, and the labels are synthetic. The arithmetic, the split rule, the two-rate calibration and the noise band are exactly what Module 08 asks you to build against your real system in Project 9.
