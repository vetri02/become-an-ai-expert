"""Reference solution for the stale-cache target. Open after passing, or after an honest hour."""
from targets.stale_cache import model


class HardenedDecoder:
    def __init__(self, max_ctx=512):
        self.max_ctx = max_ctx
        self._caches = {}   # request id -> list of contributions, one per position

    def start(self, request_id, prompt):
        if len(prompt) > self.max_ctx:
            raise ValueError("prompt longer than max_ctx")
        self._caches[request_id] = [model.g(t, i) for i, t in enumerate(prompt)]

    def step(self, request_id):
        cache = self._caches[request_id]
        if len(cache) >= self.max_ctx:
            raise RuntimeError("context full")
        t = model.next_token(cache)
        cache.append(model.g(t, len(cache)))
        return t

    def finish(self, request_id):
        self._caches.pop(request_id, None)

    def generate(self, prompt, n):
        rid = object()
        self.start(rid, prompt)
        try:
            return [self.step(rid) for _ in range(n)]
        finally:
            self.finish(rid)

    def cache_entries(self):
        return sum(len(c) for c in self._caches.values())


DECODER = HardenedDecoder
