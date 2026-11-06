# Capstone: build, measure and operate an LLM product

## Objective and workload

28 hours over about three weeks (plus the two-hour final exam), as a sprint on top of what Stage 3 already built. Build one LLM product end to end for real users, with the measurement discipline of the whole course, then defend it. The product is yours to choose; the constraints are not.

## Scenario

A small organisation you have access to (your employer, a club, a non-profit, an open-source project) has a corpus of documents and a recurring task people do by hand: answering questions from the corpus, triaging requests, extracting structured data, or drafting responses. Build the assistant that does it, with retrieval, at least two tools, per-user permissions, an eval harness, a cost model, and at least ten real users for the last two weeks.

## Minimum engineering scope

- Ingestion with chunking and metadata, re-runnable; hybrid retrieval; permissions enforced in the retrieval query.
- An agent loop with rules in code: step cap, dollar budget, deterministic pre-checks on every tool call, state in a database.
- A golden set of 60 or more real questions, versioned; recall@k; a code grader for groundedness and abstention; one calibrated judge with TPR and TNR.
- Noise measured; a regression suite in CI; a red-team suite (direct and indirect injection, tool abuse, exfiltration) with the trifecta broken in code.
- Cost per task and p95 latency on a dashboard; prompt caching; one documented cost cut.
- A model-upgrade run: two model versions compared per category against the noise band.

## Part 1: design and baseline, 7 hours

Problem framing with the cost of the manual task in hours. Architecture decision record. Ingestion and retrieval with the first golden set of 30 and recall@k. A prompt-only baseline answer path. The first error analysis of 30 outputs.

## Part 2: the agent and the harness, 7 hours

Tools, pre-checks, budget and state. The golden set grown to 60 from real failures. Graders and the judge calibrated. CI with the regression suite and the noise band. The red-team suite. First five users.

## Part 3: operate and optimise, 7 hours

Ten users for two weeks with a changelog. The dashboard. The cost cut with before/after. The model-upgrade run. The fine-tune-or-not decision record if a behaviour gap remains.

## Part 4: write-up and defence, 7 hours

The README that reads as finished: one-line result, architecture, eval table against the baseline, cost and p95, where it breaks, decisions reversed, three commands. A public post. A 20-minute recorded talk. The oral defence with your reviewer.

## Capstone rubric: 100 points

| Criterion | Points | 0 | Half | Full |
|---|---|---|---|---|
| Measurement | 25 | Eyeballed | Golden set and recall@k; no judge calibration or noise | Retrieval and generation separate; judge TPR/TNR; noise band; CI gate proven by an injected regression |
| Real use | 15 | No users | Fewer than ten, or under two weeks | Ten users, two weeks, changelog with what changed because of them |
| Engineering | 15 | Rules in prompts | Some checks in code | Step cap, budget, pre-checks, permissions and state all in code and tested |
| Security | 15 | No suite | Injection cases exist | Red-team suite in CI; trifecta broken in code; reviewer's removal of a guard makes the suite fail |
| Cost and operations | 10 | No numbers | Cost known | Cost cut documented inside the noise band; dashboard; upgrade run per category |
| Explanation | 10 | Cannot explain | Two "why" levels | Five levels on any component, from your own artifacts |
| Write-up | 10 | Missing parts | README complete | Finished README, public post, talk |

## Mandatory no-go conditions

Any of these fails the capstone regardless of score: a forbidden document reachable through the retrieval path; a tool that executes without a code-level check; a claimed number with no reproducible path to it; "shipped" with no users; a judge used without calibration labels.

## Oral defence prompts

1. Pick the number on your dashboard you trust least and say why.
2. What did the users break that you did not predict?
3. Remove your recipient allowlist. What happens, and how do you know?
4. Which model upgrade would you refuse today, from your own table?
5. What would you build differently if the corpus were ten times larger?
6. What is the one thing in this system you cannot yet explain five levels deep?
