"""Reference solution for the leaky-agent target. Open after passing, or after an honest hour."""
from targets.leaky_agent import world

ALLOWED_DOMAIN = "@example.com"


class HardenedAgent:
    def __init__(self, tools, model, max_steps=50, budget=1.0):
        self.tools, self.model = tools, model
        self.max_steps, self.budget = max_steps, budget
        self.pinned = {n: world.Tools.digest(d) for n, d in tools.definitions().items()}

    # ---- policy, in code ----
    def approve(self, name, digest):
        self.pinned[name] = digest

    def tool_allowed(self, name):
        current = self.tools.definitions().get(name)
        return current is not None and world.Tools.digest(current) == self.pinned.get(name)

    def _refuse(self, tr, name, args):
        if not self.tool_allowed(name):
            return "tool definition changed and not approved"
        if name == "send_email" and not str(args.get("to", "")).endswith(ALLOWED_DOMAIN):
            return "recipient outside allowlist"
        if world.UPSTREAM_TOKEN in str(args):
            return "secret in arguments"
        return None

    def _call(self, tr, name, args):
        if tr.steps >= self.max_steps or tr.cost + world.PRICE_PER_STEP > self.budget + 1e-12:
            tr.stopped_reason = "budget"
            return None, True
        why = self._refuse(tr, name, args)
        if why:
            tr.blocked.append((name, dict(args), why))
            return None, False
        tr.steps += 1; tr.cost += world.PRICE_PER_STEP
        return self.tools.call(name, args, token=None), False   # the token stays in the host

    # ---- the loop ----
    def run(self, user_request, doc_ids=("q3-report", "poisoned", "looping")):
        tr = world.Trace()
        docs = []
        for d in doc_ids:                                      # retrieval is data: read, never obey
            out, stop = self._call(tr, "read_doc", {"id": d})
            if stop:
                return tr
            docs.append(out or "")
        context = "User: " + user_request + "\n"               # only the user's words drive actions
        while True:
            proposals = self.model.propose(context)
            if not proposals:
                break
            for name, args in proposals:
                _, stop = self._call(tr, name, args)
                if stop:
                    return tr
                outcome = "blocked" if tr.blocked and tr.blocked[-1][0] == name and tr.blocked[-1][1] == args else "ok"
                context += "Observation: %s %s\n" % (name, outcome)   # metadata only; never document text
        tr.answer = self.model.summarise(docs[0] if docs else "")
        return tr


AGENT = HardenedAgent
