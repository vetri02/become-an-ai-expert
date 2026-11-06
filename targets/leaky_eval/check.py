"""Grader for the leaky-harness target.

    python3 -m targets.leaky_eval.check
    python3 -m targets.leaky_eval.check --solution targets.leaky_eval.target
"""
import argparse
import importlib
import statistics
import sys

from . import fixtures as fx

FLAGS = {
    1: "FLAG{le1-the-test-set-was-never-tuned-on}",
    2: "FLAG{le2-retrieval-and-generation-are-measured-apart}",
    3: "FLAG{le3-a-judge-has-two-error-rates}",
    4: "FLAG{le4-noise-before-regression}",
    5: "FLAG{le5-reliability-is-pass-hat-k}",
}


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def fresh(cls):
    return cls(fx.System())


def stage_1(cls):
    """The split is disjoint by document and the reported recall is not the leaked 1.0."""
    h = fresh(cls)
    dev, test = h.split(fx.GOLDEN)
    check(len(test) >= 0.3 * len(fx.GOLDEN), "test split too small: %d" % len(test))
    check(not ({q["doc"] for q in dev} & {q["doc"] for q in test}), "a document appears in both dev and test")
    check(not ({q["qid"] for q in dev} & {q["qid"] for q in test}), "a question appears in both dev and test")
    h.tune()
    r = h.report()["retrieval.recall_at_5"]
    check(r < 0.95, "recall@5 on the test split is %.2f: the system was tuned on it" % r)
    check(0.4 < r, "recall@5 %.2f is implausibly low; check the top-5 membership test" % r)


def stage_2(cls):
    """Retrieval and generation are separate numbers, and a right-chunk-wrong-answer case shows it."""
    h = fresh(cls)
    h.split(fx.GOLDEN); h.tune()
    rep = h.report()
    check("retrieval.recall_at_5" in rep and "generation.groundedness" in rep, "report lacks the two separate keys: %r" % sorted(rep))
    # a system that retrieves perfectly but never grounds
    s = fx.System(base_recall=1.0, grounded_rate=0.0)
    h2 = cls(s); h2.split(fx.GOLDEN); h2.tune()
    rep2 = h2.report()
    check(rep2["retrieval.recall_at_5"] > 0.99 and rep2["generation.groundedness"] < 0.01,
          "perfect retrieval with no grounding should read 1.0 / 0.0, got %r" % rep2)


def stage_3(cls):
    """Judge calibration reports true-positive and true-negative rates and refuses a bad judge."""
    h = fresh(cls)
    cal = h.calibrate(fx.LABELS)
    tp = sum(1 for a, g in fx.LABELS if g and fx.judge_llm(a)); fn = sum(1 for a, g in fx.LABELS if g and not fx.judge_llm(a))
    tn = sum(1 for a, g in fx.LABELS if not g and not fx.judge_llm(a)); fp = sum(1 for a, g in fx.LABELS if not g and fx.judge_llm(a))
    check(abs(cal["tpr"] - tp / (tp + fn)) < 0.01, "tpr %r, expected %.3f" % (cal.get("tpr"), tp / (tp + fn)))
    check(abs(cal["tnr"] - tn / (tn + fp)) < 0.01, "tnr %r, expected %.3f" % (cal.get("tnr"), tn / (tn + fp)))
    check(cal["n"] == len(fx.LABELS), "n should be the label count")
    check(h.judge_ok(cal) is False, "this judge misses about 30%% of failures (tnr %.2f) and must not be accepted" % cal["tnr"])
    check(h.judge_ok({"tpr": 0.95, "tnr": 0.9, "n": 200}) is True, "a judge at tpr 0.95 / tnr 0.9 should be accepted")


def stage_4(cls):
    """Noise is measured from repeated runs and a regression must exceed it."""
    h = fresh(cls)
    h.split(fx.GOLDEN); h.tune()
    nz = h.noise(runs=5)
    vals = [h.report(seed=s)["generation.groundedness"] for s in range(5)]
    check(abs(nz - statistics.pstdev(vals)) < 1e-9, "noise %r != pstdev of five runs %.4f" % (nz, statistics.pstdev(vals)))
    check(h.is_regression(0.80, 0.79, 0.03) is False, "a 0.01 drop inside a 0.03 noise band is not a regression")
    check(h.is_regression(0.80, 0.70, 0.03) is True, "a 0.10 drop beyond a 0.03 noise band is a regression")


def stage_5(cls):
    """Reliability is pass^k; capability is pass@k; they are different numbers."""
    h = fresh(cls)
    check(abs(h.reliability(fx.TRIALS) - 0.2) < 1e-9, "pass^k over the fixtures is 1 of 5 tasks = 0.2, got %r" % h.reliability(fx.TRIALS))
    check(abs(h.capability(fx.TRIALS) - 0.8) < 1e-9, "pass@k over the fixtures is 4 of 5 tasks = 0.8, got %r" % h.capability(fx.TRIALS))


def run(module_name="targets.leaky_eval.hardened"):
    mod = importlib.import_module(module_name)
    cls = getattr(mod, "HARNESS")
    try:
        cls(fx.System())
    except NotImplementedError as e:
        return [(n, False, "not implemented: %s" % e) for n in FLAGS]
    return [_attempt(n, fn, cls) for n, fn in ((1, stage_1), (2, stage_2), (3, stage_3), (4, stage_4), (5, stage_5))]


def _attempt(n, fn, *args):
    try:
        fn(*args)
        return (n, True, fn.__doc__.split("\n")[0])
    except Exception as e:
        return (n, False, "%s: %s" % (type(e).__name__, e))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--solution", default="targets.leaky_eval.hardened", help="module exposing HARNESS")
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
