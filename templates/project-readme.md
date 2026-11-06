# Project README template

Copy this into a new repository. Fill every line with a number or a link; a line you cannot fill is a line the project has not earned yet.

## One-line result

<metric> <value> on <described test set> at <cost per request> and <p95 latency>. Example: recall@5 0.84 on a 60-question versioned golden set, $0.004 per query, p95 1.2 s.

## What it does and for whom

Two sentences. Who uses it (count and period: "ten users for three weeks").

## Architecture

A diagram or five lines: ingestion, retrieval, generation, tools, evals, monitoring.

## Evaluation

| Metric | Baseline | This system | Test set | Noise band |
|---|---|---|---|---|
| | | | | |

Retrieval and generation measured separately. Judge TPR and TNR against N human labels. How the golden set is versioned.

## Cost and latency

Cost per request and p50/p95 latency, with the date and model version.

## Where this breaks

The failure categories from error analysis, with counts and one example each. The cases you chose not to fix and why.

## Decisions reversed

What you changed your mind about and the measurement that drove it.

## Run it

Three commands from a clean clone.

## What is mine

If this builds on something else, say exactly which part is yours.
