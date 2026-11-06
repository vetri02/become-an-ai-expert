"""The vulnerable decoder. Attacker's side: read it, predict its failures, do not edit.

    python3 -m targets.stale_cache.target

One shared cache for every request, never reset, never evicted.
"""
from . import model


class VulnerableDecoder:
    def __init__(self, max_ctx=512):
        self.max_ctx = max_ctx
        self.cache = []          # one list for everyone
        self.live = {}

    def start(self, request_id, prompt):
        # Appends to whatever is already there: a second prompt sees the first.
        for t in prompt:
            self.cache.append(model.g(t, len(self.cache)))
        self.live[request_id] = True

    def step(self, request_id):
        # Reads the whole shared cache: two interleaved requests contaminate each other.
        t = model.next_token(self.cache)
        self.cache.append(model.g(t, len(self.cache)))
        return t

    def finish(self, request_id):
        self.live.pop(request_id, None)   # nothing is evicted

    def generate(self, prompt, n):
        rid = object()
        self.start(rid, prompt)
        out = [self.step(rid) for _ in range(n)]
        self.finish(rid)
        return out

    def cache_entries(self):
        return len(self.cache)


DECODER = VulnerableDecoder

if __name__ == "__main__":
    d = VulnerableDecoder()
    for p in model.PROMPTS[:2]:
        got, want = d.generate(p, 8), model.reference_generate(p, 8)
        print("prompt", p, "cached", got, "reference", want, "SAME" if got == want else "DIFFERENT")
    print("cache entries after two requests:", d.cache_entries(), "(nothing was evicted)")
