"""Synthetic system and data for the leaky-harness target. Attacker's side: do not edit.

Twenty documents, four questions each (80 golden questions, grouped by
document), a retriever and a generator with controllable noise, a human
label set for judge calibration, and a judge with a known error profile.
"""
import random

DOCS = {"d%02d" % i: "document %d about topic %d" % (i, i % 7) for i in range(20)}
GOLDEN = [{"qid": "q%03d" % (4 * i + j), "doc": "d%02d" % i, "text": "question %d about topic %d" % (4 * i + j, i % 7)}
          for i in range(20) for j in range(4)]


class System:
    """A fake retrieval-plus-generation system.

    ``tuned_on`` is the set of question ids the system was tuned with; it
    retrieves those perfectly (that is the leak). Everything else retrieves
    the right document with probability ``base_recall`` and otherwise a
    wrong one from the same topic. Generation is grounded with probability
    ``grounded_rate`` when the right document is present.
    """

    def __init__(self, base_recall=0.7, grounded_rate=0.8):
        self.base_recall = base_recall
        self.grounded_rate = grounded_rate
        self.tuned_on = set()

    def tune(self, questions):
        self.tuned_on |= {q["qid"] for q in questions}

    def retrieve(self, q, k=5, seed=0):
        rng = random.Random("%s|%s" % (seed, q["qid"]))
        if q["qid"] in self.tuned_on or rng.random() < self.base_recall:
            top = [q["doc"]]
        else:
            top = []
        topic = int(q["doc"][1:]) % 7
        others = [d for d in DOCS if d != q["doc"] and int(d[1:]) % 7 == topic]
        rng.shuffle(others)
        return (top + others)[:k]

    def answer(self, q, chunks, seed=0):
        rng = random.Random("%s|%s|gen" % (seed, q["qid"]))
        if q["doc"] in chunks and rng.random() < self.grounded_rate:
            return "answer from %s [cite:%s]" % (q["doc"], q["doc"])
        return "answer with no support [cite:%s]" % (chunks[0] if chunks else "none")


def grounded(answer, chunks):
    """Code grader: does the answer cite a chunk that was retrieved and is the right one?"""
    cited = answer.split("[cite:")[-1].rstrip("]")
    return cited in chunks and "no support" not in answer


# Human labels for calibrating the judge: (answer_text, human_pass)
LABELS = []
_r = random.Random(7)
for i in range(200):
    good = i % 2 == 0
    LABELS.append(("a grounded answer %d" % i if good else "an unsupported answer %d" % i, good))


def judge_llm(answer):
    """A judge with a known error profile: catches 70% of failures, passes 95% of good answers."""
    rng = random.Random("judge|" + answer)
    if "unsupported" in answer or "no support" in answer:
        return rng.random() < 0.30     # says PASS on 30% of real failures
    return rng.random() < 0.95


# Agent trial outcomes for the reliability stage: task -> list of trial results
TRIALS = {"t1": [True, False, True], "t2": [True, True, True], "t3": [False, False, True],
          "t4": [True, True, False], "t5": [False, False, False]}
