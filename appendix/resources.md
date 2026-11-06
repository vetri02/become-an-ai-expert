# Resources, with status as of November 2026

Only resources that were checked to exist and be current. One primary resource per module; the rest are optional. Prices are free unless stated.

## Foundations

| Resource | Use in | Status |
|---|---|---|
| Harvard CS50P (Python) or the official Python tutorial | A1 | Current |
| MIT, The Missing Semester of Your CS Education | A1 | Current, lectures 1 to 6 |
| Exercism Python track (free mentoring) | A1 | Current |
| SQLBolt, then Mode SQL tutorial | A1 | Current |
| FastAPI tutorial, Docker Getting Started | A1 | Current |
| 3Blue1Brown, Essence of Linear Algebra, Essence of Calculus, Neural Networks | A2 | Current; intuition only, not standalone if you have no math background |
| Khan Academy (from pre-algebra if needed; statistics and probability units) | A2 | Current |
| StatQuest (Josh Starmer) | A2, A3 | Current |
| Mathematics for Machine Learning (Deisenroth, Faisal, Ong), free PDF at mml-book.github.io | A2 reference | Current |
| Andrew Ng, Machine Learning Specialization (Coursera, audit free) | A3; Module 02 | Still recommended in Nov 2026 threads |
| scikit-learn Getting Started and Common Pitfalls docs | A3; Module 02 | Current |

## LLM internals

| Resource | Use in | Status |
|---|---|---|
| Karpathy, Neural Networks: Zero to Hero (about 14.5h video) | A4; Modules 03 to 06 | Current; prerequisites: Python, derivatives, Gaussian |
| Karpathy, nanochat | A4; Modules 03 to 06 | Verified Nov 2026: GPT-2 grade for about $48 on 8xH100 (about $15 spot); CPU script for a toy run |
| Sebastian Raschka, Build a Large Language Model (From Scratch), Manning | A4; Modules 03 to 06 | Current; paid book, code free on GitHub |
| Sebastian Raschka, Build a Reasoning Model (From Scratch), Manning | A4; Modules 03 to 06; Track C | Published 2026 (listings show June to November 2026); chapters verified: evaluation, inference-time scaling, RLVR, GRPO, distillation; paid book, code free |
| Stanford CS336, Language Modeling from Scratch, Spring 2026 | A4; Modules 03 to 06; Track B | Verified: 19 lectures on YouTube, 5 assignments on GitHub; heavy prerequisites |
| Hugging Face smol-course v2 | A4; Modules 03 to 06; Track C | Verified free with free certification; units: instruction tuning, evaluation, preference alignment, VLMs, RL, synthetic data |
| Breakthrough papers: Attention Is All You Need; GPT-2; Chinchilla; InstructGPT; DeepSeek-R1 | A4; Modules 03 to 06 | |

## AI engineering

| Resource | Use in | Status |
|---|---|---|
| Hamel Husain and Shreya Shankar, AI Evals FAQ | A5; Modules 07 to 11 | Free; verified current. Paid cohort exists; free materials cover the method |
| Anthropic, Demystifying evals for AI agents (Jan 2026) | A5; Modules 07 to 11; Track A | Current |
| Anthropic, Effective context engineering for AI agents (Sep 2025) | A5; Modules 07 to 11; Track A | Current |
| Chip Huyen, AI Engineering (O'Reilly) | A5; Modules 07 to 11 | Paid; cited in 2026 threads as the reference |
| promptfoo guides (RAG, agents, LLM-as-judge) | A5; Modules 07 to 11 | Updated Oct 2026 |
| OpenAI evals guides and cookbook | A5; Modules 07 to 11 | Current |
| Hugging Face Agents Course | A5; Modules 07 to 11 | Current |
| Model Context Protocol spec (2026-07-28) | A5; Modules 07 to 11; Track A | Current |
| Simon Willison, The lethal trifecta (prompt injection) | Track A | 2025-06-16 |
| Cloud Security Alliance, Agentic MCP security best practices | Track A | 2026-03-27 draft |
| Alexey Grigorev, AI engineering field guide (interview trends) | Module 13 | 2026 |

## Infrastructure

| Resource | Use in | Status |
|---|---|---|
| vLLM docs and contributing guide | Track B | Current |
| GPU MODE lectures, Discord, popcorn-cli leaderboard | Track B | Current |
| Programming Massively Parallel Processors (PMPP), 4th ed. | Track B | Paid; still the standard text per r/CUDA 2026 |
| CS336 assignment 2 (systems: Triton FlashAttention2, distributed) | Track B | Current |
| KernelBench-Verified paper (why kernel speedups need hidden tests) | Track B | June 2026 |

## Research

| Resource | Use in | Status |
|---|---|---|
| ARENA curriculum (chapters 0 to 4) | Track C | Verified free, self-paced, updated 2026 |
| Neel Nanda, How to become a mechanistic interpretability researcher | Track C | Updated 2025-09-02 |
| MATS program and admissions FAQ | Track C | Verified: $1,250/week stipend plus compute; no PhD required |
| Georg Lange, AI safety application guide | Track C | 2025-10-26 |
| nilenso, training a small model with RLVR and GRPO | Track C | 2026-05-18 |
| EleutherAI FAQ and Summer of Open AI Research | Track C | 2026 |

## Staying current (pick three)

Simon Willison's blog; Karpathy; the engineering blogs of Anthropic, OpenAI, DeepMind and the open-weight labs; Nathan Lambert's Interconnects; Hamel Husain and Shreya Shankar; Eugene Yan; Chip Huyen; Latent Space and the smol.ai digest if you want one aggregator. Fifteen to twenty minutes a day. Production experience with your own data beats all of it.

## Links

- CS50P: https://cs50.harvard.edu/python/
- Missing Semester: https://missing.csail.mit.edu/
- Exercism Python: https://exercism.org/tracks/python
- 3Blue1Brown linear algebra: https://www.3blue1brown.com/topics/linear-algebra
- MML book: https://mml-book.github.io
- Ng ML Specialization: https://www.coursera.org/specializations/machine-learning-introduction
- scikit-learn: https://scikit-learn.org/stable/getting_started.html
- Zero to Hero: https://karpathy.ai/zero-to-hero.html
- nanochat: https://github.com/karpathy/nanochat
- Raschka LLMs from scratch: https://sebastianraschka.com/llms-from-scratch
- Raschka reasoning from scratch: https://sebastianraschka.com/reasoning-from-scratch
- CS336: https://cs336.stanford.edu/
- smol-course: https://huggingface.co/learn/smol-course/en/unit0/1
- Evals FAQ: https://hamel.dev/blog/posts/evals-faq/
- Anthropic evals: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic context engineering: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Chip Huyen, AI Engineering: https://www.oreilly.com/library/view/ai-engineering/9781098166298
- promptfoo: https://www.promptfoo.dev/docs/category/guides/
- OpenAI evals: https://developers.openai.com/learn/evals
- HF Agents Course: https://hf.co/learn/agents-course
- MCP spec: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Lethal trifecta: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- CSA MCP security: https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/
- Grigorev field guide: https://github.com/alexeygrigorev/ai-engineering-field-guide
- vLLM: https://docs.vllm.ai/ and https://docs.vllm.ai/en/stable/contributing/
- GPU MODE: https://github.com/gpu-mode/lectures and https://github.com/gpu-mode/popcorn-cli
- PMPP: https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0
- CS336 assignment 2: https://github.com/stanford-cs336/assignment2-systems
- KernelBench-Verified: https://arxiv.org/abs/2607.16241
- ARENA: https://learn.arena.education/
- Nanda guide: https://www.lesswrong.com/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher
- MATS: https://www.matsprogram.org/ and https://www.matsprogram.org/faq/getting-into-mats
- Lange guide: https://georglange.com/post/ai-safety-application-guide/
- nilenso GRPO: https://blog.nilenso.com/blog/2026/05/18/training-a-small-model-to-write-better-ocaml-with-rlvr-and-grpo/
- EleutherAI: https://eleuther.ai/community/
- Keeping up (Raykar): https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/
