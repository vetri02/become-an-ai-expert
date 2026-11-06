"""Reference solution for the leaky-harness target. Open after passing, or after an honest hour."""
import statistics

from targets.leaky_eval import fixtures as fx


class HardenedHarness:
    def __init__(self, system):
        self.system = system
        self.dev, self.test = [], []

    def split(self, golden):
        docs = sorted({q["doc"] for q in golden})
        test_docs = set(docs[::3])                       # every third document, about 33%
        self.test = [q for q in golden if q["doc"] in test_docs]
        self.dev = [q for q in golden if q["doc"] not in test_docs]
        return self.dev, self.test

    def tune(self):
        self.system.tune(self.dev)

    def report(self, seed=0):
        hits = grounded = 0
        for q in self.test:
            chunks = self.system.retrieve(q, 5, seed)
            hits += q["doc"] in chunks
            grounded += fx.grounded(self.system.answer(q, chunks, seed), chunks)
        n = len(self.test)
        return {"retrieval.recall_at_5": hits / n, "generation.groundedness": grounded / n, "n": n}

    def calibrate(self, labels):
        tp = fn = tn = fp = 0
        for answer, human_pass in labels:
            j = fx.judge_llm(answer)
            if human_pass:
                tp += j; fn += not j
            else:
                fp += j; tn += not j
        return {"tpr": tp / (tp + fn) if tp + fn else float("nan"),
                "tnr": tn / (tn + fp) if tn + fp else float("nan"), "n": len(labels)}

    def judge_ok(self, cal):
        return bool(cal["tpr"] >= 0.9 and cal["tnr"] >= 0.8)

    def noise(self, runs=5):
        return statistics.pstdev(self.report(seed=s)["generation.groundedness"] for s in range(runs))

    def is_regression(self, before, after, noise):
        return bool(before - after > 2 * noise)

    def reliability(self, trials):
        return sum(all(t) for t in trials.values()) / len(trials)

    def capability(self, trials):
        return sum(any(t) for t in trials.values()) / len(trials)


HARNESS = HardenedHarness
