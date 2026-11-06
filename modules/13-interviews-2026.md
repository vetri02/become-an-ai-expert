# Module 13: Interviews the 2026 way

## Prerequisites and measurable objectives

Prerequisite: Module 12. By the end you can:

1. Answer the 2026 question bank with numbers from your own projects.
2. Draw an ML system design for a GenAI app, a recommendation pipeline and an inference service, in under 20 minutes each.
3. Code attention, a training loop, a tokenizer and the eval metrics from memory while narrating, with or without an assistant on screen.

**Primary resource:** Alexey Grigorev, AI engineering field guide, interview trends (https://github.com/alexeygrigorev/ai-engineering-field-guide). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 8 guided: 7 on the concept blocks, 1 on the lab and the first pass of the build. Unguided practice on top is yours.

## What the rounds look like

A candidate who did 15 AI engineer interviews in six months reports the questions were "why RAG instead of fine-tuning?" and "how did you measure hallucinations?", not math proofs or LeetCode; the best offer came from explaining a 60% cost cut. Another who interviewed at 46 companies saw every format: LeetCode, system design, take-home builds, long LLM discussions. There is no standard loop. Prepare for the software loop plus your own LLM projects.

## Concepts, in order

1. **The decisions round** (1 hour): for every project, the three hardest decisions, the numbers, the failures you did not fix, and the decision you reversed. Lead with trade-offs.
2. **ML system design** (2 hours): a GenAI app end to end (ingestion, retrieval, generation, evals, monitoring, cost); a recommendation or ranking system; an inference service for a 70B model at a latency target and budget. The seniority signal is designing the loop (chunking, context effects, output validation, feedback that improves retrieval), not the prompt. One borderline senior got a soft no for forcing an LLM onto a regression problem.
3. **Coding, with AI in the room** (1 hour): "AI allowed, but explain every line" is the dominant take-home format; some companies run one AI-assisted and one AI-banned round; some hand you an unfamiliar repo and grade how you steer the agent, rejecting most candidates; some plant a bad decision to see if you push back. Ask whether AI is allowed. Narrate while you code. Anthropic rebuilt its take-home into puzzles with no debugger that score whether you build your own tools.
4. **The depth probe** (1 hour): interviewers pick one resume item and go as deep as they can; a staff MLE rejected candidates who ran out. Know every project to the bottom. Say "I don't know" and reason aloud rather than bluff.
5. **The question bank** (1 hour): "Is the model upgrade better, how do you decide before rollout?"; "this RAG answer is confident and wrong, debug it"; "agent or fixed pipeline?"; "estimate per-request cost, then halve it"; "when would you fine-tune?"; "how did you measure hallucinations?" (abstention rate plus a calibrated judge). Red flags: vibes, unbounded loops, cheaper-model-before-measuring, transformer math for an applied role.
6. **Titles and pay** (1 hour): level-controlled, the ML premium has plateaued near 1.3x; infra and inference roles sit at the top of the band; "Machine Learning Engineer" titles pay well above "AI Engineer" for similar work, so negotiate the title; every offer in the stories was negotiated and a second offer is the only reliable lever. Decline take-homes that are deployable product work or arrive before any human conversation.

## Lab

No lab. Do a timed mock interview with your peer reviewer using the question bank.

## Build

**Project 14: the application kit.** A portfolio page with three projects, each led by a measured result; a resume where every bullet has a number; ten system-design prompts drawn and timed; attention, a GPT block, a training loop with eval, BPE basics, recall@k and pass@k implemented from memory; memory and cost math for 7B and 70B serving; one mock interview recorded.

**Deliverables:** the kit, the recording, and a one-page "decisions and numbers" sheet per project.

## Mastery gate

Your reviewer runs the depth probe on one project for 20 minutes, five levels deep, and you do not run out; the from-memory implementations run.

## Quiz

1. How do you answer "how did you measure hallucinations?" in 60 seconds?
2. A candidate is asked to debug a confident wrong RAG answer. List the three causes to check first.
3. What is the seniority signal in LLM system design?
4. What do you do when a take-home is deployable product work?
5. Compute serving memory for a 70B model in bf16 at 4k context, batch 8, 8 KV heads, 80 layers, head size 128, and say what hardware it needs.
6. Why negotiate the title and not just the number?

## Primary-source reading

- 15 interviews write-up (447 pts): https://www.reddit.com/r/deeplearning/comments/1swxb2k/
- Kalra on 46 interviews: https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer
- Hiring managers on post-AI interviews (HN, Sep 2026): https://news.ycombinator.com/item?id=49768826
- Anthropic on AI-resistant take-homes: https://www.anthropic.com/research/AI-resistant-technical-evaluations
- Grigorev field guide, interview trends: https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/05-trends.md
- Interviewer's question bank (Hasija, 2026): https://chiraghasija.cc/posts/how-to-interview-ai-engineer-role-2026/
- MLE interview prep (35 pts): https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/odzfxx9/
- Levels.fyi on the AI premium: https://letsdatascience.com/news/levelsfyi-tells-lds-the-ai-pay-premium-has-stopped-growing-a893d96e

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Run the depth probe on my Project 9 for 20 minutes and tell me where I ran out.
2. Ask me the 2026 interview questions from this module and grade each answer for mechanism and measurement.
3. Give me one from-memory implementation to type with the assistant closed, then review it.
