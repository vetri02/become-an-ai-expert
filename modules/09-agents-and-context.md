# Module 09: Agents and context engineering

## Prerequisites and measurable objectives

Prerequisite: Module 08. By the end you can:

1. Build a tool-using agent whose rules are enforced in code, with state outside the model and deterministic checks before any tool runs.
2. Apply the context-engineering principles: system prompt at the right altitude, minimal high-signal tokens, distinct tools, just-in-time retrieval, compaction, notes outside the context, sub-agents.
3. Measure the agent with outcome-graded tasks, pass@k and pass^k, and a regression suite.

**Primary resource:** Anthropic, Effective context engineering for AI agents (https://www.anthropic.com/research/effective-context-engineering-for-ai-agents). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 13 guided: 12 on the concept blocks, 1 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why agents are an engineering problem, not a prompting problem

An experienced engineer called prompt engineering "never a real role"; context engineering and evals replaced it. Senior engineers say there is "no roadmap anymore" for agent frameworks because they change too fast, and the answer is system design. Several production teams moved to minimal custom code. Interviewers read seniority from how you design the loop.

## Concepts, in order

1. **The loop** (1 hour): model proposes, harness parses, code validates, tool runs, result returns as tokens, repeat with a step cap and a budget. One agent, one task. Principle 1 again.
2. **Context engineering** (3 hours): Anthropic's guide, applied: altitude of the system prompt; the smallest set of high-signal tokens; token-efficient, non-overlapping tools; a few canonical examples rather than every edge case; just-in-time retrieval; metadata and progressive disclosure; compaction tuned for recall then precision; structured notes outside the context; sub-agents with clean contexts returning condensed summaries.
3. **Compaction costs** (1 hour): an eleven-configuration study found summarise-and-clear doubled cost per turn and dropped memory recall from 92% to 38% because it rewrote the cached prefix, while capping tool outputs cut cost 38% at identical accuracy. Probe planted facts, not overall quality.
4. **Tool design and MCP** (2 hours): schemas, idempotency, timeouts, least privilege per tool; the Model Context Protocol; build one MCP server with real auth and one client.
5. **State and determinism** (2 hours): state lives in your database, not the transcript; every tool call passes a deterministic check first; schema validation is not safety.
6. **Agent evals** (3 hours): 20 to 50 tasks from real failures; outcome grading; partial credit; pass@k and pass^k; clean environment per trial; the documented list of unfixed failures.

## Lab

No new lab; reuse `labs/lab04_eval_harness.py` (pass@k and pass^k) and read `labs/lab11_prompt_injection.py` ahead of Module 10.

## Build

**Project 9 (part 2): the agent with its harness.** A tool-using agent for a real task (support triage, document extraction, a research assistant over your Project 8 corpus):

- At least three tools with schemas, deterministic pre-checks, step cap and dollar budget enforced in code
- State in a database; the transcript is disposable
- An MCP server for one tool, with authentication
- 20 to 50 outcome-graded tasks; task success, tool-call precision and recall, pass@3 and pass^3 reported
- A regression suite in CI; a documented list of cases it still fails and why you left them
- At least five real users for two weeks and a changelog of what they broke

**Deliverables:** repo; a post on one decision you reversed, with the measurements.

## Mastery gate

Your reviewer reads the unfixed-failures list and picks one; you show the trace and explain why it is left. pass^3 is in the README with the trial count.

## Quiz

1. Why "rules in code, not in the prompt"? Give one rule that must be code.
2. What does "system prompt at the right altitude" mean? Give an example of too low and too high.
3. Why can compaction raise cost? What did the study measure?
4. What makes two tools "overlapping", and why is that bad for the agent?
5. Why is schema validation not safety?
6. Your agent passes 9 of 10 tasks once each. What do you not yet know, and how do you find out?
7. When would you use a sub-agent, and what must it return?

## Primary-source reading

- Anthropic, Effective context engineering: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Anthropic, Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Context engineering cost study (Bouchard, 2026-08-18): https://www.louisbouchard.ai/context-engineering-2026/
- MCP specification: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Hugging Face Agents Course: https://hf.co/learn/agents-course
- 10 things for agents in production: https://www.reddit.com/r/AI_Agents/comments/1ta1cye/
- "No roadmap anymore" (29 pts): https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owc6cz1/
- Prompt engineering "never a real role": https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p052pym/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Read my unfixed-failures list, pick one, and make me explain its trace.
2. Ask me where my budget and step cap live, and make me show the code.
3. Ask me to compute pass^3 from my trial counts, then challenge whether the trial count is enough.
