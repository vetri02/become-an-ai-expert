"""Your hardened agent. Replace every ``NotImplementedError``.

Keep the public interface exactly as below; the grader in ``check.py``
calls only these. You may add private helpers and attributes.

Contract:

- ``__init__(tools, model, max_steps=50, budget=1.0)``: ``tools`` is a
  ``world.Tools``; ``model`` is a ``world.Model`` with ``propose(text)``
  (follows instructions in whatever text it is given) and
  ``summarise(text)`` (data only, never proposes). Pin every tool
  definition's digest at construction.
- ``run(user_request, doc_ids=(...))``: return a ``world.Trace``. Only the
  user's request may drive proposals; retrieved documents are data and go
  through ``summarise``. Before any tool call: the tool is pinned and
  approved; ``send_email`` recipients end with ``@example.com``; no
  argument contains ``world.UPSTREAM_TOKEN``; ``steps < max_steps`` and
  ``cost + PRICE_PER_STEP <= budget``, else stop with
  ``stopped_reason = "budget"``. Never pass the upstream token to
  ``tools.call``. Record refusals in ``trace.blocked``.
- ``approve(name, digest)``: accept a new definition digest for a tool.
- ``tool_allowed(name)``: True only if the tool's current digest equals
  the pinned or approved one.
"""
from . import world  # noqa: F401


class HardenedAgent:
    def __init__(self, tools, model, max_steps=50, budget=1.0):
        self.tools, self.model = tools, model
        self.max_steps, self.budget = max_steps, budget
        raise NotImplementedError("build your agent here")

    def run(self, user_request, doc_ids=("q3-report", "poisoned", "looping")):
        raise NotImplementedError

    def approve(self, name, digest):
        raise NotImplementedError

    def tool_allowed(self, name):
        raise NotImplementedError


AGENT = HardenedAgent
