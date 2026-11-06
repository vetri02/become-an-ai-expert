"""Your hardened harness. Replace every ``NotImplementedError``.

Keep the public interface exactly as below; the grader in ``check.py``
calls only these. You may add private helpers and attributes.

Contract:

- ``__init__(system)``: ``system`` has ``tune(questions)``,
  ``retrieve(q, k, seed)`` and ``answer(q, chunks, seed)``.
- ``split(golden)``: return ``(dev, test)``, disjoint, grouped by ``doc``
  (no document appears on both sides), test at least 30% of questions.
  Store them; ``tune()`` uses dev only.
- ``tune()``: tune the system on dev.
- ``report(seed=0)``: a dict with ``retrieval.recall_at_5`` (fraction of
  test questions whose ``doc`` is in the top 5) and
  ``generation.groundedness`` (fraction grounded per ``fixtures.grounded``),
  computed on the test split, separately.
- ``calibrate(labels)``: run ``fixtures.judge_llm`` on each labelled answer
  and return ``{"tpr": ..., "tnr": ..., "n": ...}``.
- ``judge_ok(cal)``: True only if ``tpr >= 0.9`` and ``tnr >= 0.8``.
- ``noise(runs=5)``: population standard deviation of ``generation.groundedness``
  over seeds 0..runs-1.
- ``is_regression(before, after, noise)``: True only if ``before - after > 2 * noise``.
- ``reliability(trials)``: fraction of tasks whose trials ALL passed (pass^k).
- ``capability(trials)``: fraction of tasks with ANY passing trial (pass@k).
"""
from . import fixtures as fx  # noqa: F401


class HardenedHarness:
    def __init__(self, system):
        self.system = system
        raise NotImplementedError("build your harness here")

    def split(self, golden):
        raise NotImplementedError

    def tune(self):
        raise NotImplementedError

    def report(self, seed=0):
        raise NotImplementedError

    def calibrate(self, labels):
        raise NotImplementedError

    def judge_ok(self, cal):
        raise NotImplementedError

    def noise(self, runs=5):
        raise NotImplementedError

    def is_regression(self, before, after, noise):
        raise NotImplementedError

    def reliability(self, trials):
        raise NotImplementedError

    def capability(self, trials):
        raise NotImplementedError


HARNESS = HardenedHarness
