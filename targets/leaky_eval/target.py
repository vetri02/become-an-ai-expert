"""The vulnerable harness. Attacker's side: read it, predict its failures, do not edit.

    python3 -m targets.leaky_eval.target

It tunes on the questions it then reports on, mixes retrieval and generation
into one score, trusts an uncalibrated judge, calls any drop a regression,
and reports pass@k as if it were reliability.
"""
from . import fixtures as fx


class VulnerableHarness:
    def __init__(self, system):
        self.system = system
        self.dev = self.test = list(fx.GOLDEN)      # same questions on both sides: the leak

    def split(self, golden):
        self.dev = list(golden); self.test = list(golden)
        return self.dev, self.test

    def tune(self):
        self.system.tune(self.dev)

    def score(self, seed=0):
        """One number for everything."""
        ok = 0
        for q in self.test:
            chunks = self.system.retrieve(q, 5, seed)
            ans = self.system.answer(q, chunks, seed)
            ok += fx.judge_llm(ans)                  # judge decides, never calibrated
        return ok / len(self.test)

    def report(self, seed=0):
        return {"score": self.score(seed)}

    def calibrate(self, labels):
        return {"agreement": sum(fx.judge_llm(a) == h for a, h in labels) / len(labels)}

    def is_regression(self, before, after):
        return after < before                        # any drop at all

    def reliability(self, trials):
        return sum(any(t) for t in trials.values()) / len(trials)   # that is pass@k, not pass^k


HARNESS = VulnerableHarness

if __name__ == "__main__":
    h = VulnerableHarness(fx.System())
    h.tune()
    print("score after tuning on the test set:", round(h.score(), 2), "(the leak makes it look perfect)")
    print("judge agreement:", h.calibrate(fx.LABELS), "(one number hides that it misses 30% of failures)")
    print("'reliability':", h.reliability(fx.TRIALS), "(this is pass@k)")
