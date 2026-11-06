"""Lab 13: models change under you; measure noise before calling a regression (Principle 19).

Two "model versions" are simulated as systems with different per-task pass
probabilities. The same 60-task suite is run twice against v1 to measure how much
the score moves on its own, then once against v2. A difference smaller than the
noise band is not a regression. Pure Python.

Run: python lab13_model_upgrade.py
"""
import random
import statistics

random.seed(0)
TASKS = list(range(60))


def model(version):
    # v2 is better on most tasks but worse on the 10 "injection" tasks (50 to 59), like a real upgrade
    def p(task):
        if version == 1:
            return 0.80 if task < 50 else 0.94
        return 0.88 if task < 50 else 0.71
    return p


def run_suite(p, trials=3):
    """pass^k over trials per task, averaged over tasks (reliability, not capability)."""
    scores = []
    for t in TASKS:
        scores.append(all(random.random() < p(t) for _ in range(trials)))
    return sum(scores) / len(scores)


def run_subset(p, tasks, trials=3):
    return sum(all(random.random() < p(t) for _ in range(trials)) for t in tasks) / len(tasks)


if __name__ == "__main__":
    v1, v2 = model(1), model(2)
    runs = [run_suite(v1) for _ in range(10)]
    noise = statistics.pstdev(runs)
    print(f"v1 run 10 times on the same suite: mean {statistics.mean(runs):.3f}, std {noise:.3f}  <- the noise band")
    s2 = run_suite(v2)
    print(f"v2 once: {s2:.3f}; overall difference {s2 - statistics.mean(runs):+.3f} vs noise {noise:.3f}")

    cap = [t for t in TASKS if t < 50]; inj = [t for t in TASKS if t >= 50]
    c1, c2 = statistics.mean(run_subset(v1, cap) for _ in range(10)), run_subset(v2, cap)
    i1, i2 = statistics.mean(run_subset(v1, inj) for _ in range(10)), run_subset(v2, inj)
    print(f"capability tasks: v1 {c1:.2f} -> v2 {c2:.2f}; injection-resistance tasks: v1 {i1:.2f} -> v2 {i2:.2f}")
    assert c2 > c1, "v2 should look better on capability"
    assert i2 < i1 - 3 * noise, "v2's safety regression is far outside the noise band and would be missed by the overall score"
    print("the overall number hid a safety regression; tag suites by failure mode and compare each against its noise")
    print("OK")
