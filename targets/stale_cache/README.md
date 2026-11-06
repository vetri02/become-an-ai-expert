# Target: the stale cache

Module 05 companion. Time: three to five hours. Standard-library Python; no model, no network.

## Scenario

A serving process decodes tokens for many users at once. A KV cache makes each step cheap by remembering what every earlier position contributed (Principle 5). The vulnerable decoder has one cache for the whole process: it is never reset between prompts, never evicted when a request finishes, and shared between requests that are in flight at the same time. It is fast. It is also wrong in four distinct ways, and one of them leaks one user's context into another's output.

The model here is a toy: a next token computed from the sum of per-position contributions, with a counter so the grader can measure work without timing. The cache invariants are the real ones.

## Watch it fail

```bash
python3 -m targets.stale_cache.target
```

The second prompt's output differs from the reference because the first prompt's contributions are still in the cache. Read `target.py` before you run it and write down which line causes each of the four failures.

## Your task

Implement `HardenedDecoder` in `hardened.py`, following the contract in its docstring, then run:

```bash
python3 -m targets.stale_cache.check
```

| Stage | Invariant | Hint |
| --- | --- | --- |
| 1 | Cached equals uncached | Positions matter: `g(token, position)`. A cache keyed by request that records where each token sat gives the reference answer; lab 03 is the same idea with real attention. |
| 2 | Requests do not share a cache | One cache per request id. If a step for A can see B's entries, you have one cache with two names. |
| 3 | A new prompt starts clean | `start` creates; it never appends to what a finished request left behind. |
| 4 | Memory is bounded | `finish` releases. After 200 finished requests, `cache_entries()` is 0; a live request holds exactly prompt plus generated. |
| 5 | One call per step | The grader counts `model.g` calls. If you recompute the prefix, you have an uncached decoder with a cache-shaped variable. |

## Deliverables

1. `hardened.py` passing all five stages, with your name on it.
2. The prediction list you wrote before running the vulnerable build, marked right or wrong.
3. Three negative tests the grader does not run. Suggestions: a `step` on an unknown request id; a prompt longer than `max_ctx`; `finish` called twice.
4. A limits paragraph. What does a passing grader not prove? At minimum: this is not attention, there is no batching or paging, no eviction policy under memory pressure is tested, and timing was not measured.

## What this target does not do

The model is a hash, not a Transformer; the cache holds integers, not key and value tensors; there is no batching. The invariants transfer unchanged: per-request isolation, position-correct entries, release on completion, and one unit of work per step are exactly what a serving engine's KV-cache manager enforces. Module 15 reads the real one.
