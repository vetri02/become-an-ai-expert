# A5. AI engineering core: build systems you can measure

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 40 guided hours.
**Goal:** Ship one LLM system to real users and defend every trade-off (RAG vs fine-tune vs prompt, model choice, cost, latency) with numbers. In 2026 interviews this is the main round.
**Principles:** Principles 9 to 17 and 19 (retrieval, measuring, cost, security and change). Labs 04, 10, 11 and 13.

## What 2026 interviews actually ask

A candidate who did 15 AI engineer interviews in six months (447 upvotes, April 2026) reports the questions were "why RAG instead of fine-tuning?" and "how did you measure hallucinations?", not math proofs or LeetCode. Their best offer came from explaining a 60% inference-cost cut. Interviewers in r/LLMDevs call "shipped" projects nobody uses a red flag.

## Learn

1. **Retrieval done properly.** Hybrid search (Postgres full-text plus pgvector is enough), chunking strategies, reranking, per-user permissions, keeping data fresh. Engineers with 2 to 3 years on RAG say the first pipeline is the easy part; ingestion, failure analysis and evaluation are the job.
2. **Evals as a discipline.** This is the core skill of the module.
   - Start with error analysis: read 20 to 50 real outputs by hand before buying any tool (Hamel Husain's evals FAQ).
   - Build a versioned "golden set" of real queries with expected sources.
   - Measure retrieval (recall@k, did it cite the right chunk) separately from generation (groundedness, rubric grading).
   - Use binary pass/fail labels. Use code-based checks whenever a rule can catch the failure. Use LLM-as-judge only for subjective parts, one judge per failure mode, always spot-checked against human labels.
   - Run the set in CI and fail the build on regressions in quality, cost or latency.
   - Anthropic's agent-evals guide: 20 to 50 tasks drawn from real failures is a great start; a 0% pass rate usually means a broken task, not a bad agent.
3. **Agents and context engineering.** One agent, one task. Rules enforced in code, not prompts. Trim context per call. State lives outside the model. Deterministic checks before any tool executes (schema validation is not safety). Read Anthropic's "Effective context engineering for AI agents" and learn the Model Context Protocol (MCP) basics.
4. **Cost and latency engineering.** Caching (prompt caching and response caching), routing cheap models to simple tasks, token budgets, batching, hybrid local/cloud. Know your own system's cost per request and p95 latency.
5. **Fine-tuning for behaviour, not facts.** LoRA on a small open model to fix format or style. Know when not to fine-tune: production teams in a September 2026 thread say RAG wins for knowledge, fine-tuning for behaviour.
6. **Read:** Chip Huyen, "AI Engineering" (O'Reilly), cited in 2026 threads as the reference for evaluating every layer. Hugging Face Agents Course for a structured agent build.

## Build

**Project A5a: a RAG system over a messy real corpus.**
Pick a corpus with real mess: a wiki export, your city's council minutes, a set of manuals, your own notes.
- 50+ test questions with expected source chunks (the golden set)
- recall@k measured before and after one change (hybrid search or reranking), with the numbers in the README
- Per-user permissions enforced in the retrieval layer
- A cost and latency dashboard (even a notebook plot counts)
- At least five real users for two weeks, and what you changed because of them

**Project A5b: a tool-using agent with an eval harness.**
- 20 to 50 tasks drawn from real failures, graded on outcome
- Task success, tool-call precision/recall, pass@k and pass^k reported
- A regression suite in CI
- A documented list of cases it still fails and why you left them

**Project A5c: a short public post about a decision you reversed.**
For example "I dropped fine-tuning for RAG" with the measurements. This is your first piece of public work. Put it on a free GitHub Pages blog.

**Runnable reference:** `labs/lab04_eval_harness.py` is a hundred-line harness showing recall@k, a code-based groundedness grader, judge calibration (TPR/TNR against human labels) and pass@k vs pass^k, on a toy system. Replace the toy retriever and generator with yours and keep the measurements.

**Done when:** you can state, from memory, your system's recall@k, cost per query, p95 latency, and the three failure modes you have not fixed.

## Skip for now

- "Chat with your PDF" demos with no evaluation.
- Prompt engineering as a job. An experienced engineer called it "never a real role"; context engineering and evals replaced it.
- Heavy orchestration frameworks. Several production teams report moving to minimal custom code.
- Fine-tuning to add knowledge.

## Checkpoint

1. Why measure retrieval and generation separately? Give an example where one is fine and the other is broken.
2. When would you use an LLM judge, and how do you know the judge is right?
3. A product manager asks you to fine-tune the model on the company wiki. What do you say?
4. How would you cut your agent's cost by half without hurting task success? Name three levers.
5. What is a prompt-injection attack on your agent, and which check in your code stops it?

## Sources

- 15 interviews in 6 months, Apr 2026 (447 pts): https://www.reddit.com/r/deeplearning/comments/1swxb2k/
- RAG engineers' daily work, Oct 2026 (54 pts): https://www.reddit.com/r/learnmachinelearning/comments/1xjpfuv/comment/19rwfb092sew5/
- How engineers evaluate RAG in practice, May 2026: https://www.reddit.com/r/learnmachinelearning/comments/1t81t7i/comment/okswmh3/
- Production RAG stack 2026: https://www.reddit.com/r/Rag/comments/1shqrwv/comment/ofhe7tp/
- RAG vs fine-tuning in production, Sep 2026: https://www.reddit.com/r/Rag/comments/1wbhsdi/comment/p8pycuc/
- 10 things for agents in production: https://www.reddit.com/r/AI_Agents/comments/1ta1cye/
- Prompt engineering "never a real role": https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p052pym/
- Hamel Husain and Shreya Shankar, AI Evals FAQ: https://hamel.dev/blog/posts/evals-faq/
- Anthropic, Demystifying evals for AI agents (Jan 2026): https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic, Effective context engineering (Sep 2025): https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- promptfoo guides: https://www.promptfoo.dev/docs/category/guides/
- Chip Huyen, AI Engineering: https://www.oreilly.com/library/view/ai-engineering/9781098166298
- HF Agents Course: https://hf.co/learn/agents-course

## Where to go next

You have the base the professional path assumes. Join it at Module 03 and finish it: the same model, engineering and hiring material, now with measurements, targets and milestones. A6 to A8 are optional; they tell the career material of Modules 12 to 17 the way the on-ramp sees it.

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Review my golden set and ask me what recall@k counts as a hit.
2. Pick one of my agent's unfixed failures and make me explain it.
3. Ask me for my judge's TPR and TNR and what I would do if they were both 0.7.
