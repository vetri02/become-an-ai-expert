# Module 07: Retrieval done properly

## Prerequisites and measurable objectives

Prerequisite: Module 06. By the end you can:

1. Build hybrid retrieval (full-text plus vectors) over a messy real corpus with per-user permissions enforced in the retrieval layer.
2. Measure recall@k on a versioned golden set and show the effect of one change.
3. Explain why the context is a finite attention budget and what that implies for how much you retrieve.

**Primary resource:** Chip Huyen, AI Engineering, the retrieval chapter (https://www.oreilly.com/library/view/ai-engineering/9781098166298). Finish it before adding anything from the reading list.
**Hours:** 13 guided: 9 on the concept blocks, 4 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why retrieval and not fine-tuning

Principle 9: the model knows nothing after its training data; retrieval puts facts into the context. Principle 10: fine-tuning is a poor way to add facts. Production teams in September 2026 say RAG for knowledge, fine-tuning for behaviour; 57% of surveyed teams do not fine-tune at all. Engineers with two to three years on retrieval say the first pipeline is the easy part: ingestion, failure analysis and evaluation are the job.

## Concepts, in order

1. **What retrieval is for** (1 hour): lexical versus semantic matching; where each fails; why hybrid wins on real queries. Postgres full-text plus pgvector is enough.
2. **Ingestion** (2 hours): parsing messy sources, chunking strategies and their trade-offs, metadata, keeping data fresh, deduplication. This is most of the work.
3. **Ranking** (2 hours): BM25, embeddings, reciprocal rank fusion, rerankers, and when reranking is worth its latency.
4. **Permissions** (1 hour): the retrieval layer filters by the caller's identity before anything reaches the model. A document the user may not read must never be in the context. Principle 16 begins here.
5. **The attention budget** (1 hour): why more retrieved chunks can make answers worse; lab 10's dilution curve; retrieving fewer, better chunks; just-in-time retrieval from Anthropic's context-engineering guide.
6. **Measuring retrieval separately** (2 hours): recall@k and whether the right chunk was cited, measured apart from generation (Principle 11). The golden set as a versioned artifact. Error analysis on the misses.

## Lab

`labs/lab10_context_and_cost.py` (part 1) and `labs/lab04_eval_harness.py` (retrieval part). Expected observations: attention weight on the relevant chunk falls from about 1.0 to 0.10 as 128 distractors are added; recall@1 0.83 and recall@3 1.00 on the toy golden set.

## Build

**Project 8: retrieval over a messy real corpus.** A corpus with real mess (a wiki export, council minutes, product manuals, your own notes):

- Ingestion with chunking and metadata, re-runnable
- Hybrid search with reciprocal rank fusion; a reranker behind a flag
- A golden set of 50 or more real questions with expected source chunks, versioned in the repo
- recall@k measured before and after one change (hybrid versus lexical, or reranking on versus off), numbers in the README
- Per-user permissions enforced in the retrieval query, with a test that proves a forbidden chunk never returns
- Error analysis of the 20 worst misses, categorised
- Five real users for two weeks, with a changelog of what they broke and what you changed (the same users carry on into Project 9)

**Deliverables:** repo with the golden set and numbers; a post on the one change and its effect.

## Mastery gate

Your README states recall@5 before and after one change on a versioned golden set, and your reviewer ran the permission test and saw it pass.

## Quiz

1. Why does a lexical index still matter when you have embeddings?
2. What is reciprocal rank fusion and why is it robust to score scales?
3. You retrieve 20 chunks and answers get worse than with 5. Explain using lab 10.
4. Where must permissions be enforced, and why is "the prompt says not to reveal it" not enough?
5. Define recall@k for retrieval and explain why it is measured separately from answer quality.
6. Name three ways chunking can go wrong and the symptom of each.
7. How do you keep a retrieval index fresh without re-embedding everything daily?

## Primary-source reading

- Chip Huyen, AI Engineering (O'Reilly), retrieval chapter: https://www.oreilly.com/library/view/ai-engineering/9781098166298
- Anthropic, Effective context engineering (just-in-time retrieval): https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Production RAG stack 2026: https://www.reddit.com/r/Rag/comments/1shqrwv/comment/ofhe7tp/
- RAG engineers' daily work (54 pts): https://www.reddit.com/r/learnmachinelearning/comments/1xjpfuv/comment/19rwfb092sew5/
- RAG vs fine-tuning in production: https://www.reddit.com/r/Rag/comments/1wbhsdi/comment/p8pycuc/
- LangChain State of Agent Engineering (57% do not fine-tune; vendor survey): https://langchain.com/state-of-agent-engineering
- pgvector: https://github.com/pgvector/pgvector

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Review my golden set. Ask how the questions were chosen and what recall@5 counts as a hit.
2. Walk me through the permission test and make me predict the result before I run it.
3. My recall changed after one chunking change. Ask me whether the change is inside the noise band.
