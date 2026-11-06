# Target: the leaky agent

Module 10 companion. Time: four to six hours. Standard-library Python; no model, no network.

## Scenario

A support agent reads documents, sends email and queries a customer database. One retrieved document carries an instruction addressed to the agent. The model has a single input channel and follows any instruction-shaped line it is shown (Principle 16). The vulnerable agent puts the user's request and every retrieved document into that one channel, executes every proposal, forwards its upstream API token into every tool call, has no step cap or budget, and trusts tool definitions it never pinned. It exfiltrates the customer list and the token on its first run.

The model here is a regular expression on purpose. Nothing about the fix depends on how clever the model is.

## Watch it fail

```bash
python3 -m targets.leaky_agent.target
```

One benign request sends mail to an attacker, with the token in the body. Read `target.py` and `world.py` before you run it and write down which line causes each of the five failures.

## Your task

Implement `HardenedAgent` in `hardened.py`, following the contract in its docstring, then run:

```bash
python3 -m targets.leaky_agent.check
```

| Stage | Invariant | Hint |
| --- | --- | --- |
| 1 | Retrieved text never becomes an action | Two channels: `model.propose` sees only the user's request; retrieved documents go to `model.summarise`, which cannot propose. Lab 11 is the smaller version. |
| 2 | Recipients are an allowlist, and benign mail still flows | Check the recipient in code before `send_email`; record refusals; an agent that refuses everything has traded one failure for another. |
| 3 | The upstream token never leaves the host | Never pass it to `tools.call`; scan arguments for it before any call. The model will try to put it in a body when a document asks. |
| 4 | Steps and dollars are capped in code | Check before each call, not after; stop with `stopped_reason = "budget"`. A request to keep re-reading is never satisfied by an observation, so only the cap ends it. |
| 5 | A changed tool definition is a new tool | Pin `Tools.digest(description)` for every tool at construction; refuse a tool whose current digest differs until `approve` is called with the new digest. |

## Deliverables

1. `hardened.py` passing all five stages, with your name on it.
2. The prediction list you wrote before running the vulnerable build, marked right or wrong.
3. Three negative tests the grader does not run. Suggestions: a user request that itself asks to email an outside address; a document that spells the instruction differently; a budget of zero.
4. A limits paragraph. What does a passing grader not prove? At minimum: a real model can be steered by content the regex does not match; the allowlist is a policy, not a proof; summarise-as-data still lets content influence the answer text; and the token check is string matching.

## What this target does not do

The target has no real model, MCP transport or OAuth behind it, and nothing leaves your machine. The five invariants (channel separation, effect allowlists, secret containment, budgets in code, pinned definitions) are the ones Module 10's production notes and the Cloud Security Alliance's MCP guidance describe, reduced to a hundred lines you can read in one sitting. Module 14 applies them to your real agent.
