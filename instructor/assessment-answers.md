# Assessment answer key

Keys for the entry diagnostic and the final scenario exam. Open after the attempt.

## Diagnostic key

Mark a question right only if your written answer contains the core idea.

1. List lookup by value is linear; dict lookup is a hash and roughly constant. It matters when you search repeatedly inside a loop over large data.
2. DNS resolves the host; TCP and TLS handshakes; the browser sends an HTTP request with method, path and headers; your server routes it to a handler; the handler returns status, headers and body; the browser parses the response.
3. A virtual environment isolates Python packages per project. Docker isolates the whole runtime (OS libraries, binaries, environment) so it runs the same elsewhere.
4. The error was raised at `handlers.py` line 42; `app.py` line 17 is the caller. The dict indexed there has no `user_id` key.
5. `SELECT customer_id, COUNT(*) AS n FROM orders WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01' GROUP BY customer_id ORDER BY n DESC LIMIT 3;`
6. The probability of data at least this extreme if the null hypothesis were true. Not the probability the hypothesis is true.
7. Accuracy is dominated by the majority class. Use precision, recall, F1 or ROC-AUC with a confusion matrix, weighed by the cost of each error type.
8. The vector of partial derivatives of the loss with respect to each parameter; it points uphill, so stepping against it lowers the loss.
9. 2x1.
10. Merge keeps both histories with a merge commit; rebase rewrites your commits on top of the target for a linear history; rebase shared branches with care.

Tasks are pass/fail. Task 4 passes if you can say the line fit converged to about w=2, b=1 with loss falling about 250x, and that the 15x learning rate diverged.

Readiness: 8+ right and all tasks: Module 01. 5 to 7, or one task failed: Foundation bridge. Below 5, or two tasks failed: Path A (A1 to A5), then join at Module 03.

## Final exam key

Six points for mechanism and measurement, two for evidence, two for assumptions.

1. Check retrieval (recall@k on that query; was the right chunk in the top k), context (was it diluted or badly chunked; lab 10), and abstention (did anything relevant exist). If retrieval was right and the answer wrong: groundedness grader and judge on that case, then prompt altitude, chunk boundaries, and whether the model needed the chunk re-ranked to the top. Evidence: the trace, the golden-set entry, the before/after number.
2. Pin the model ID; re-run capability evals with the new model's own best prompt; re-run injection, tool-abuse and exfiltration suites; measure noise by running the incumbent twice; compare per category against the noise band; canary; re-baseline. Stop if any safety category falls beyond the noise band, regardless of the overall gain (lab 13). Evidence: the per-category table with the noise band.
3. Unknown: whether the 18% disagreement is on passes or failures. Report TPR and TNR separately on a held-out label set; 100 to 200 labels per failure mode, split train/dev/test; replace the judge with code the moment a rule can detect the failure. Evidence: the confusion matrix against human labels.
4. Measure first: tokens per task by input (prefix, retrieved, history), output, and tool results. Levers: cache the stable prefix (41 to 80% on input); cap tool outputs and trim history (the compaction study's 38%); route simple requests to a smaller model; cap output length. Prove with the Module 08 suite inside the noise band. Refuse: summarising the cached prefix (raises cost and cuts recall) or dropping evals to save money.
5. Retrieval returns the document; it enters the context; the model, having one channel, may propose the email tool call; the tool layer's recipient allowlist (or the rule that retrieved text never reaches an outbound tool) blocks it in code; the attempt is logged. The design removes the outbound leg for untrusted content. A stronger prompt changes nothing because the model cannot tell who wrote a line (lab 11).
6. Facts are distributed across many weights from many contexts; a small fine-tuning set gives few, correlated steps that move format more than knowledge; general ability can degrade. Alternative: retrieval. Experiment: prompt-only, retrieval-plus-prompt, fine-tuned, same golden set and graders, quality, cost and latency for each. A fine-tuned variant that wins on quality within noise at acceptable cost would change the decision.
7. The RL objective rewards only the math outcome; nothing protects general ability, so weights move wherever the reward points (Principle 8, lab 09). The KL term pulls the policy toward the reference and caps the reward it can collect. Reward change: add a fluency or general-ability term, or penalise length. Evaluation change: keep separate capability and general columns and report reward variance within groups.
8. Weights 140 GB bf16; KV per token 320 KB (80 layers, 8 KV heads, 128 head size); at 4k context 1.25 GB per sequence, 62.5 GB for 50; total about 200 GB plus overhead. Start with two to four 80 GB GPUs with tensor parallelism, or INT4 weights (about 35 GB) on fewer. Decode at batch 50 is below the crossover (about 300 on an H100), so bandwidth-bound. Measure prefix caching and speculative decoding first; quantisation if quality allows.
9. Named problem with hours per week it costs; one tool; a 30-day pilot under a few hundred dollars; data stays in-house or goes to a provider with a data-processing agreement, no customer PII in prompts; the three numbers: task success on a golden set, cost per task, hours saved per week.
10. Any artifact qualifies; the answer is graded on whether each "why" level is answered with a mechanism or a measurement from the learner's own work, and whether the level-six question is specific and the plan to answer it is a concrete experiment.

## Scoring

Add the ten scores. 80 or more, with every mastery gate met, passes. Below 80, re-sit the failed scenarios after a week; the reasoning must come from your own artifacts, not from this key.
