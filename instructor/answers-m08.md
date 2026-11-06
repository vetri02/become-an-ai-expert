### Answer key: Module 08

### Quiz answers and reasoning

1. Metrics are proxies chosen before the failure modes are known; the failure modes are only visible in the outputs. A metric chosen first measures the failures you imagined, not the ones you have.
2. Code when an objective rule can detect the failure (parsing, citations, tool arguments, abstention). An LLM judge only for failures that need judgment, one per failure mode, calibrated against human labels.
3. Not yet meaningful: 80% agreement could be 100% on passes and 60% on failures. Report TPR and TNR separately, look at the disagreements, refine the judge prompt or split the failure mode, and re-measure on the held-out test labels.
4. pass@k = 1 - (1-p)^k = 1 - 0.4^4 = 0.974; pass^k = p^k = 0.6^4 = 0.130. Capability is high; reliability is low.
5. Run the same suite at least twice against the same model and take the spread. A change smaller than that spread is sampling, not a regression. Lab 13 shows a 0.08 band on a 60-task suite.
6. Regression cases grow from the incumbent's past failures, so a challenger with different weaknesses scores lower on them even if it is better overall. Tag regression versus capability cases, give each model its own best prompt, compare error distributions by severity, and re-baseline the regression layer after migration.
7. Groundedness: does the answer cite a retrieved chunk that supports it (code grader on citations plus a judge for support). Abstention: on queries where retrieval returns nothing relevant, how often the system says it does not know. Report both; track them in production.

### Lab assessment and mastery gate

The reviewer injects a regression (for example, breaks the citation) and checks CI fails. They ask to see the raw outputs behind one category. TPR and TNR must be stated with the label count.

### How to use this key

Open after the quiz. Question 7 is the single most asked 2026 interview question; practise it aloud.
