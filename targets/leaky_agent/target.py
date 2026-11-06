"""The vulnerable agent. Attacker's side: read it, predict its failures, do not edit.

    python3 -m targets.leaky_agent.target

It gives the model one channel with everything in it, executes every
proposal, forwards its upstream token, has no step cap, and trusts tool
definitions it has never pinned.
"""
from . import world


class VulnerableAgent:
    def __init__(self, tools, model, max_steps=50, budget=1.0):
        self.tools, self.model = tools, model
        self.max_steps, self.budget = max_steps, budget

    def run(self, user_request, doc_ids=("q3-report", "poisoned", "looping")):
        tr = world.Trace()
        context = "User: " + user_request + "\n"
        for d in doc_ids:                                  # retrieved text goes into the one channel
            context += "Retrieved: " + self.tools.call("read_doc", {"id": d}, token=world.UPSTREAM_TOKEN) + "\n"
        while True:                                        # no step cap, no budget
            proposals = self.model.propose(context)
            if not proposals or tr.steps > 10_000:
                break
            for name, args in proposals:
                self.tools.call(name, args, token=world.UPSTREAM_TOKEN)   # executes everything, forwards the token
                tr.steps += 1; tr.cost += world.PRICE_PER_STEP
            if not any(n == "read_doc" for n, _ in proposals):
                break
            if tr.steps >= 200:
                tr.stopped_reason = "gave up"; break
        tr.answer = self.model.summarise(world.DOCS["q3-report"])
        return tr

    def approve(self, name, digest):
        pass                                               # never checks

    def tool_allowed(self, name):
        return True


AGENT = VulnerableAgent

if __name__ == "__main__":
    t, m = world.Tools(), world.Model()
    tr = VulnerableAgent(t, m).run("Summarise the quarterly report.")
    print("emails sent:", t.sent)
    print("token forwarded to tools:", any(c["token"] for c in t.upstream_calls))
    print("steps:", tr.steps, "cost: $%.2f" % tr.cost, "stopped:", tr.stopped_reason)
