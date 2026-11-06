"""Tests for the targets themselves: the vulnerable builds must fail their
graders, the learner stubs must fail cleanly, and the reference solutions
must pass every stage.

    python3 -m unittest discover -s targets/tests -t . -v
"""
import unittest

from targets.stale_cache import check as sc_check, model as sc_model, target as sc_target
from targets.leaky_eval import check as le_check, fixtures as le_fx, target as le_target
from targets.leaky_agent import check as la_check, world as la_world, target as la_target


class StaleCacheTarget(unittest.TestCase):
    def test_second_prompt_is_wrong(self):
        d = sc_target.VulnerableDecoder()
        d.generate(sc_model.PROMPTS[0], 8)
        got = d.generate(sc_model.PROMPTS[1], 8)
        self.assertNotEqual(got, sc_model.reference_generate(sc_model.PROMPTS[1], 8))

    def test_nothing_is_evicted(self):
        d = sc_target.VulnerableDecoder()
        for p in sc_model.PROMPTS:
            d.generate(p, 5)
        self.assertGreater(d.cache_entries(), 0)

    def test_grader_fails_the_vulnerable_build(self):
        results = sc_check.run("targets.stale_cache.target")
        self.assertGreaterEqual(sum(1 for _, ok, _ in results if not ok), 3)

    def test_stub_fails_cleanly(self):
        results = sc_check.run("targets.stale_cache.hardened")
        self.assertTrue(all(not ok and "not implemented" in msg for _, ok, msg in results))

    def test_solution_passes(self):
        results = sc_check.run("instructor.targets.stale_cache_solution")
        self.assertTrue(all(ok for _, ok, _ in results), results)


class LeakyEvalTarget(unittest.TestCase):
    def test_leak_inflates_score(self):
        h = le_target.VulnerableHarness(le_fx.System(base_recall=0.5))
        h.tune()
        self.assertGreater(h.score(), 0.7)

    def test_reliability_is_really_pass_at_k(self):
        h = le_target.VulnerableHarness(le_fx.System())
        self.assertAlmostEqual(h.reliability(le_fx.TRIALS), 0.8)

    def test_grader_fails_the_vulnerable_build(self):
        results = le_check.run("targets.leaky_eval.target")
        self.assertGreaterEqual(sum(1 for _, ok, _ in results if not ok), 4)

    def test_stub_fails_cleanly(self):
        results = le_check.run("targets.leaky_eval.hardened")
        self.assertTrue(all(not ok and "not implemented" in msg for _, ok, msg in results))

    def test_solution_passes(self):
        results = le_check.run("instructor.targets.leaky_eval_solution")
        self.assertTrue(all(ok for _, ok, _ in results), results)


class LeakyAgentTarget(unittest.TestCase):
    def test_vulnerable_exfiltrates(self):
        t, m = la_world.Tools(), la_world.Model()
        la_target.VulnerableAgent(t, m).run("Summarise the quarterly report.")
        self.assertTrue(any(to == "attacker@evil.example" for to, _ in t.sent))
        self.assertTrue(any(la_world.UPSTREAM_TOKEN in body for _, body in t.sent))

    def test_vulnerable_forwards_token(self):
        t, m = la_world.Tools(), la_world.Model()
        la_target.VulnerableAgent(t, m).run("Summarise the quarterly report.")
        self.assertTrue(all(c["token"] == la_world.UPSTREAM_TOKEN for c in t.upstream_calls))

    def test_grader_fails_the_vulnerable_build(self):
        results = la_check.run("targets.leaky_agent.target")
        self.assertGreaterEqual(sum(1 for _, ok, _ in results if not ok), 4)

    def test_stub_fails_cleanly(self):
        results = la_check.run("targets.leaky_agent.hardened")
        self.assertTrue(all(not ok and "not implemented" in msg for _, ok, msg in results))

    def test_solution_passes(self):
        results = la_check.run("instructor.targets.leaky_agent_solution")
        self.assertTrue(all(ok for _, ok, _ in results), results)


if __name__ == "__main__":
    unittest.main()
