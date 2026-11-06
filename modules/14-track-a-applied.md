# Module 14: Track A, applied AI engineer

## Prerequisites and measurable objectives

Prerequisite: Milestone D. Choose one of Modules 14, 15 and 16; the other two are optional reading. By the end of this one you can:

1. Own the eval and observability stack for a production agent, so that a model upgrade is a config change plus an eval run.
2. Break the lethal trifecta in code and prove it with a red-team suite that runs on every model version.
3. Deliver in one vertical with its real constraints and get one upstream contribution merged.

**Primary resource:** Anthropic, Demystifying evals for AI agents (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 24 guided, all inside the concept blocks above (the build is one of them); the lab run is counted there too.

## Who this track is for

Backend and full-stack engineers; people who like shipping and arguing about product trade-offs. Most of the jobs are here. Hiring threads say domain plus ML beats generic ML, so you keep your vertical. 24 hours over about three weeks, then it continues for years; the Advanced tracks page has the long plan.

## Concepts, in order

1. **Real users for real** (6 hours): take your Project 9 agent to at least ten users and iterate for the whole module; keep a changelog of what they broke. Instrument everything with tracing; build the dashboard of pass rate per failure category over time, across model versions.
2. **Model swaps as config** (4 hours): prompts and tools regression-tested across two providers; each model gets its own best prompt; capability and regression cases tagged; noise measured; a documented upgrade run end to end with the Module 10 checklist.
3. **Security owned, not assumed** (4 hours): RBAC in the retrieval and tool layers; tool invariants in code; a prompt-injection red-team suite (direct, indirect, tool-abuse, exfiltration) in CI; the trifecta broken; MCP controls applied to your server.
4. **Cost as a habit** (2 hours): prompt caching, routing, batching, output caps; the cost per task of everything you run, on the dashboard.
5. **One vertical** (4 hours): legal, healthcare, finance, voice, logistics, education; the vertical's data, regulations and what "good" means to its users; a second system or a major feature built under those constraints (PII handling, audit trails, regulatory language).
6. **Upstream** (4 hours): one merged PR to an eval or agent project your target employers use (promptfoo, inspect-ai, smolagents, an MCP server). Benchmarks and bug reproductions are the easiest first PRs.

## Lab

Re-run `labs/lab13_model_upgrade.py` and reproduce its result on your own suite with two real model versions.

## Build

**Project 15, Track artifact A:** the agent in production with a public dashboard of pass rate over time across at least two model versions; the red-team suite with its pass rate; a write-up of a 50%-plus cost reduction with the before/after breakdown; three posts (an eval method, the cost cut, a security failure you found and fixed); a talk.

**Deliverables:** dashboard link, repo, posts, the merged PR.

## Mastery gate

A model upgrade on your system is demonstrably a config change plus an eval run; the trifecta is broken in code your reviewer can read; the PR is merged.

## Quiz

1. Why is your eval suite overfit to the incumbent model, and what do you do about it before a migration?
2. What are the three legs of the trifecta, and which one would you remove for a customer-support agent that must send email?
3. What goes on the production dashboard, and why per failure category?
4. Why does domain expertise multiply this track?
5. What makes a first upstream PR likely to merge?

## Primary-source reading

- Anthropic, Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Applied track targets from RAG engineers' daily work: https://www.reddit.com/r/learnmachinelearning/comments/1xjpfuv/comment/19rxgf6mnaa1x/
- Domain + ML beats generic ML: https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojpng9u/
- Model upgrades break agent safety: https://www.promptfoo.dev/blog/model-upgrades-break-agent-safety/
- Eval suites overfit to the incumbent: https://tianpan.co/blog/2026/07/03/your-eval-suite-is-overfit-to-your-incumbent-model
- The lethal trifecta: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- CSA MCP security practices: https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/
- LangChain agent engineering survey (vendor): https://langchain.com/state-of-agent-engineering

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me what in my system changes when the model ID changes and what stays the same.
2. Make me show, in code, where the lethal trifecta is broken.
3. Review my pull request description as the upstream maintainer.
