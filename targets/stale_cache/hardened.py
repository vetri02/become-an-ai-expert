"""Your hardened decoder. Replace every ``NotImplementedError``.

Keep the public interface exactly as below; the grader in ``check.py``
calls only these. You may add private helpers and attributes.

Contract:

- ``__init__(max_ctx=512)``: ``max_ctx`` is the most cache entries one
  request may hold (prompt plus generated tokens).
- ``start(request_id, prompt)``: begin a request with its own cache,
  filled with the prompt's contributions at their positions.
- ``step(request_id)``: produce the next token for that request only,
  using ``model.next_token`` over that request's contributions, then
  cache the new token's contribution at its position. One ``model.g``
  call per step.
- ``finish(request_id)``: release the request's cache entries.
- ``generate(prompt, n)``: start, step n times, finish; return the n tokens.
- ``cache_entries()``: total entries held across all live requests.

Outputs must equal ``model.reference_generate`` for every prompt.
"""
from . import model  # noqa: F401


class HardenedDecoder:
    def __init__(self, max_ctx=512):
        self.max_ctx = max_ctx
        raise NotImplementedError("build your decoder here")

    def start(self, request_id, prompt):
        raise NotImplementedError

    def step(self, request_id):
        raise NotImplementedError

    def finish(self, request_id):
        raise NotImplementedError

    def generate(self, prompt, n):
        raise NotImplementedError

    def cache_entries(self):
        raise NotImplementedError


DECODER = HardenedDecoder
