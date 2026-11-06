# Hands-on targets

The labs show you a principle holding. The targets do the opposite: each is a small, deliberately broken system that you must fix until a grader stops finding holes. They sit after the three modules where the course's measurement and engineering claims are most often got wrong: Module 05 (the KV cache), Module 08 (the eval harness) and Module 10 (the agent's boundaries).

Everything is standard-library Python running on synthetic data inside your own machine. Nothing here needs a model, a network connection or a credential. The "model" in the agent target is a regular expression on purpose, because none of the fixes depend on how clever the model is.

## Rules of engagement

- Work in your own copy of the course folder (the `become-an-ai-expert` folder from [GitHub](https://github.com/vetri02/become-an-ai-expert) or [the zip](https://github.com/vetri02/become-an-ai-expert)). Commands run from that folder, the course root, not from inside `targets/`.
- Read the vulnerable build first and predict every way it fails before you run it. Write the predictions down; Milestone B or C scores them.
- Edit only the `hardened.py` stub in each target. The grader imports it by name. Do not edit `model.py`, `fixtures.py`, `world.py`, `target.py` or `check.py`; those are the attacker's side of the table.
- Each grader stage prints a flag when its invariant holds. Flags are fixed strings and prove nothing on their own; the deliverable is the code and your explanation of why each stage passes.
- Reference solutions live under `instructor/targets/`. Open them after you pass, or after an honest attempt has stalled for more than an hour.

## The targets

| Target | Module | Vulnerable build | Grader | Stages |
| --- | --- | --- | --- | --- |
| Target 05, [Stale cache](stale_cache/README.md) | 05 | `python3 -m targets.stale_cache.target` | `python3 -m targets.stale_cache.check` | cached equals uncached; requests do not share a cache; a new prompt starts clean; memory is bounded; one call per step |
| Target 08, [Leaky harness](leaky_eval/README.md) | 08 | `python3 -m targets.leaky_eval.target` | `python3 -m targets.leaky_eval.check` | the test set was never tuned on; retrieval and generation apart; a judge has two error rates; noise before regression; reliability is pass^k |
| Target 10, [Leaky agent](leaky_agent/README.md) | 10 | `python3 -m targets.leaky_agent.target` | `python3 -m targets.leaky_agent.check` | retrieved text never becomes an action; recipient allowlist with benign mail flowing; the token never leaves; steps and dollars capped; a changed definition is a new tool |

## Verifying the targets themselves

```bash
python3 -m unittest discover -s targets/tests -t . -v
```

The suite checks that the vulnerable builds fail the graders, that the untouched stubs fail cleanly, and that the reference solutions pass every stage. Fifteen tests. Run it before you start so a broken environment is not mistaken for a broken solution.

## How the targets are graded in the course

A passed grader is the entry ticket, not the grade. Milestone B (after Module 06) scores the Target 05 write-up and Milestone C (after Module 11) scores Targets 08 and 10. They score the written parts: the prediction list, the explanation of each invariant, the negative tests you added beyond the grader's, and the limits paragraph, using the rubric in the [peer-review protocol](../assessments/peer-review.md).
