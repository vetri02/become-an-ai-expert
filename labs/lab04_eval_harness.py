"""Lab 04: an eval harness in about a hundred lines (Module 08, or A5 on the Novice track; Principles 11, 13, 14 and 15).

Pure Python. Demonstrates the four measurements the course insists on:
  1. recall@k for retrieval, measured separately from generation
  2. a code-based grader for generation (groundedness: did the answer cite a retrieved chunk)
  3. judge calibration: true-positive and true-negative rate of a "judge" against human labels
  4. pass@k vs pass^k for an agent task with per-trial success p

The "system" here is a deliberately simple keyword retriever and a fake generator,
so the harness logic is what you are studying. Swap in your own system.

Run: python lab04_eval_harness.py
"""
import math
import random

random.seed(0)

CORPUS = {
    "c1": "Prompt caching stores the stable prefix so repeated calls are cheaper.",
    "c2": "recall@k measures whether the relevant chunk appears in the top k results.",
    "c3": "A KV cache stores keys and values so each decode step only computes one new row.",
    "c4": "LoRA fine-tuning changes behaviour and format; it is a poor way to add facts.",
    "c5": "pass^k is the probability that all k independent trials succeed.",
}

# Golden set: real-looking questions with the chunk that answers them. Version it.
GOLDEN_V1 = [
    {"q": "why does prompt caching save money", "expect": "c1"},
    {"q": "what does recall at k measure", "expect": "c2"},
    {"q": "what does a kv cache store", "expect": "c3"},
    {"q": "should I fine-tune to add facts", "expect": "c4"},
    {"q": "what is pass hat k", "expect": "c5"},
    {"q": "how do I make decoding faster", "expect": "c3"},
]


def retrieve(query, k):
    """Keyword overlap retriever. Deliberately weak so recall@1 < recall@3."""
    qw = set(query.lower().split())
    scored = sorted(CORPUS, key=lambda c: -len(qw & set(CORPUS[c].lower().split())))
    return scored[:k]


def recall_at_k(golden, k):
    hits = sum(1 for g in golden if g["expect"] in retrieve(g["q"], k))
    return hits / len(golden)


def generate(query, chunks):
    """Fake generator: answers from the top chunk, sometimes hallucinates."""
    if random.random() < 0.2:
        return "The answer is 42. [no citation]"
    return f"{CORPUS[chunks[0]]} [cite:{chunks[0]}]"


def grounded(answer, chunks):
    """Code-based grader: a rule can detect this failure, so no LLM judge needed."""
    return any(f"[cite:{c}]" in answer for c in chunks)


def judge_calibration(human_labels, judge_labels):
    tp = sum(1 for h, j in zip(human_labels, judge_labels) if h and j)
    fn = sum(1 for h, j in zip(human_labels, judge_labels) if h and not j)
    tn = sum(1 for h, j in zip(human_labels, judge_labels) if not h and not j)
    fp = sum(1 for h, j in zip(human_labels, judge_labels) if not h and j)
    tpr = tp / (tp + fn) if tp + fn else float("nan")
    tnr = tn / (tn + fp) if tn + fp else float("nan")
    return tpr, tnr


def pass_at_k(p, k):
    """P(at least one of k trials succeeds)."""
    return 1 - (1 - p) ** k


def pass_hat_k(p, k):
    """P(all k trials succeed)."""
    return p ** k


if __name__ == "__main__":
    r1, r3 = recall_at_k(GOLDEN_V1, 1), recall_at_k(GOLDEN_V1, 3)
    print(f"retrieval: recall@1 = {r1:.2f}, recall@3 = {r3:.2f}  (golden set v1, n={len(GOLDEN_V1)})")
    assert r3 >= r1

    # Generation measured separately from retrieval, with a code-based grader
    n_trials, ok = 200, 0
    for _ in range(n_trials):
        g = random.choice(GOLDEN_V1)
        chunks = retrieve(g["q"], 3)
        ok += grounded(generate(g["q"], chunks), chunks)
    print(f"generation: groundedness = {ok/n_trials:.2f} over {n_trials} trials (code grader; fake generator hallucinates ~20%)")
    assert 0.7 < ok / n_trials < 0.9

    # Judge calibration: a judge that misses 30% of failures and passes 10% of good outputs
    human = [random.random() < 0.5 for _ in range(400)]       # True = pass
    judge = [(h and random.random() > 0.10) or ((not h) and random.random() < 0.30) for h in human]
    tpr, tnr = judge_calibration(human, judge)
    print(f"judge: TPR (catches real passes) = {tpr:.2f}, TNR (catches real failures) = {tnr:.2f} against {len(human)} human labels")
    assert 0.8 < tpr < 1.0 and 0.6 < tnr < 0.8

    # Reliability compounds
    p = 0.75
    print(f"agent with per-trial success {p}: pass@3 = {pass_at_k(p,3):.2f} (capability), pass^3 = {pass_hat_k(p,3):.2f} (reliability)")
    assert math.isclose(pass_hat_k(0.75, 3), 0.421875)
    print("OK")
