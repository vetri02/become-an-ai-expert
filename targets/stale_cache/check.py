"""Grader for the stale-cache target.

    python3 -m targets.stale_cache.check
    python3 -m targets.stale_cache.check --solution targets.stale_cache.target

Each stage prints a flag when its invariant holds. The flags are fixed
strings; the invariant is the point.
"""
import argparse
import importlib
import sys

from . import model

FLAGS = {
    1: "FLAG{sc1-cached-equals-uncached}",
    2: "FLAG{sc2-requests-do-not-share-a-cache}",
    3: "FLAG{sc3-a-new-prompt-starts-clean}",
    4: "FLAG{sc4-memory-is-bounded}",
    5: "FLAG{sc5-one-call-per-step}",
}


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def stage_1(cls):
    """Cached generation equals the uncached reference for every prompt, in sequence."""
    d = cls()
    for p in model.PROMPTS:
        got, want = d.generate(p, 24), model.reference_generate(p, 24)
        check(got == want, "prompt %r: cached %r != reference %r" % (p, got[:6], want[:6]))


def stage_2(cls):
    """Two interleaved requests produce what each would produce alone."""
    d = cls()
    a, b = model.PROMPTS[0], model.PROMPTS[2]
    d.start("A", a); d.start("B", b)
    out_a, out_b = [], []
    for _ in range(20):
        out_a.append(d.step("A")); out_b.append(d.step("B"))
    d.finish("A"); d.finish("B")
    check(out_a == model.reference_generate(a, 20), "request A was contaminated by B: %r" % out_a[:6])
    check(out_b == model.reference_generate(b, 20), "request B was contaminated by A: %r" % out_b[:6])


def stage_3(cls):
    """A new prompt after a finished one starts from a clean cache."""
    d = cls()
    d.generate(model.PROMPTS[3], 30)
    got = d.generate(model.PROMPTS[1], 10)
    check(got == model.reference_generate(model.PROMPTS[1], 10),
          "second prompt saw stale state from the first: %r" % got)


def stage_4(cls):
    """Cache entries are released on finish and bounded by live requests."""
    d = cls(max_ctx=64)
    for i in range(200):
        d.generate(model.PROMPTS[i % len(model.PROMPTS)], 20)
    check(d.cache_entries() == 0, "after 200 finished requests, %d entries remain" % d.cache_entries())
    d.start("X", model.PROMPTS[0])
    for _ in range(10):
        d.step("X")
    check(d.cache_entries() == len(model.PROMPTS[0]) + 10,
          "one live request holds %d entries, expected %d" % (d.cache_entries(), len(model.PROMPTS[0]) + 10))
    d.finish("X")


def stage_5(cls):
    """One contribution call per generated token: the cache does the work."""
    d = cls()
    p = model.PROMPTS[4]
    n = 256
    model.COUNTER["g"] = 0
    d.generate(p, n)
    calls = model.COUNTER["g"]
    budget = len(p) + n
    check(calls <= 2 * budget, "generation of %d tokens made %d contribution calls; a cache needs about %d" % (n, calls, budget))


def run(module_name="targets.stale_cache.hardened"):
    mod = importlib.import_module(module_name)
    cls = getattr(mod, "DECODER")
    try:
        cls()
    except NotImplementedError as e:
        return [(n, False, "not implemented: %s" % e) for n in FLAGS]
    return [_attempt(n, fn, cls) for n, fn in ((1, stage_1), (2, stage_2), (3, stage_3), (4, stage_4), (5, stage_5))]


def _attempt(n, fn, *args):
    try:
        fn(*args)
        return (n, True, fn.__doc__.split("\n")[0])
    except Exception as e:  # the learner's code may raise anything
        return (n, False, "%s: %s" % (type(e).__name__, e))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--solution", default="targets.stale_cache.hardened", help="module exposing DECODER")
    args = p.parse_args(argv)
    results = run(args.solution)
    passed = 0
    for n, ok, msg in results:
        if ok:
            passed += 1
            print("stage %d  PASS  %s\n         %s" % (n, msg, FLAGS[n]))
        else:
            print("stage %d  FAIL  %s" % (n, msg))
    print("%d of %d stages passed" % (passed, len(results)))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
