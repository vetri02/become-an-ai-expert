# Module 10: Cost, latency and security

## Prerequisites and measurable objectives

Prerequisite: Module 09. By the end you can:

1. State your system's cost per request and p95 latency, and halve the cost without hurting the eval.
2. Defend an agent against prompt injection by removing one leg of the lethal trifecta in code, and prove it with a red-team suite in CI.
3. Pin model versions and re-run capability and safety suites on every upgrade.

**Primary resource:** Simon Willison, The lethal trifecta (https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), with labs 10, 11 and 13. The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 9 guided: 8 on the concept blocks, 1 on the lab, Target 10 and the first pass of the build. Unguided practice on top is yours.

## Why these three are one module

They are the same arithmetic and the same discipline. Cost is tokens times price (Principle 17); the cheapest token is the one you do not send, which is also the one that cannot carry an injection. One candidate's best offer in a 15-interview run came from explaining a 60% inference-cost cut. A documented model upgrade dropped injection resistance from 94% to 71%; the fix that held was in code.

## Concepts, in order

1. **Cost arithmetic** (1 hour): input and output tokens, prefill and decode latency, p50 and p95. Lab 10 part 2. Measure your Project 8 and 9 systems first; do not optimise what you have not measured.
2. **Caching** (1 hour): prompt caching of the stable prefix (41 to 80% cost reduction measured on 500+ agent sessions), response caching, why dynamic content goes at the end.
3. **Routing and budgets** (1 hour): small models for simple requests, escalation on uncertainty, token budgets per task, capping tool outputs (38% cost cut at identical accuracy in the compaction study).
4. **Prompt injection** (2 hours): the lethal trifecta (private data, untrusted content, outbound channel); why a stronger prompt changes nothing; tool invariants, recipient allowlists, human re-auth for high-risk actions, default-deny sandboxes. Lab 11. Simon Willison's rule that a guardrail claiming 95% is a failing grade.
5. **MCP in production** (1 hour): a May 2026 study found 40% of nearly 8,000 live remote MCP servers exposed tools with no authentication. Hash-pin tool definitions, least-privilege tokens per tool, OAuth 2.1 with PKCE, never forward the client's token upstream, log agent identity and redacted parameters.
6. **Model upgrades** (1 hour): pin model IDs; canary with sampled traffic; re-run capability, injection and tool-abuse suites; measure noise; re-baseline. Lab 13.
7. **Observability** (1 hour): instrument once with OpenTelemetry, treat the backend as swappable, redact prompts and responses.

## Lab

`labs/lab10_context_and_cost.py` (part 2), `labs/lab11_prompt_injection.py`, `labs/lab13_model_upgrade.py`. Expected observations: a 6,500-token request 68% cheaper with the prefix cached; an injected instruction exfiltrating data, unchanged by a stronger prompt, blocked by a code allowlist; a safety regression hidden inside an improved overall score. Then **Target 10: the leaky agent**, which you fix until its five flags print.

## Build

**Project 10: a cost cut with numbers.** On Project 8 or 9: measure cost per request and p95; apply caching, routing and output caps; halve the cost; show the eval unchanged within the noise band. Write it up with the before/after table.

**Project 9 (part 3): the red-team suite.** Direct and indirect injection cases, tool-abuse cases and an exfiltration case, all in CI; the trifecta broken in code; a model-upgrade checklist run once against a second model version.

**Deliverables:** the cost post; the red-team suite in the repo with its pass rate.

## Mastery gate

Cost halved with the eval inside the noise band, in a table your reviewer can trace. Target 10's five flags print. The injection suite fails when the reviewer removes your allowlist.

## Quiz

1. Compute the cost of 10,000 requests a day with a 6,000-token cached prefix, 500 uncached input tokens and 300 output tokens at $3 and $15 per million, with a 90% cache discount.
2. Name the three legs of the lethal trifecta and say which one your Project 9 agent removes.
3. Why does a stronger system prompt not fix injection?
4. What must be true of a model upgrade before you ship it? List the suites.
5. Why can summarisation raise your bill?
6. Name four MCP controls that matter in production.
7. What is the difference between p50 and p95, and which one your users feel?

## Primary-source reading

- Simon Willison, The lethal trifecta: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Model upgrades break agent safety (promptfoo, 2025-12-08): https://www.promptfoo.dev/blog/model-upgrades-break-agent-safety/
- "Don't Break the Cache", arXiv 2601.06007: https://arxiv.org/abs/2601.06007
- MCP authentication study, arXiv 2605.22333: https://arxiv.org/abs/2605.22333
- CSA agentic MCP security best practices: https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/
- Context engineering cost study: https://www.louisbouchard.ai/context-engineering-2026/
- 15 interviews, the 60% cost-cut offer: https://www.reddit.com/r/deeplearning/comments/1swxb2k/
- AI Security Engineering, the sibling course on securing AI applications, agents and model lifecycles (same author, same structure; where this module's security thread continues): https://aisec.engineering/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me to trace my cost-halving table row by row and name the noise band.
2. Suppose my allowlist were removed. Ask me what the injection suite would do and why.
3. Help me with the leaky-agent target by asking which invariant each failing flag names.
