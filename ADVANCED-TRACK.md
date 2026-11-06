# Advanced tracks: from the core to a specialism

Choose depth after the core. Stage 5 gave you one module in one track; this page is the multi-year plan for each, kept as the course's reference. Do one. Read the other two once so you know what you are not doing.

## Choose depth after the core

| If you... | Track |
|---|---|
| Liked shipping to users and arguing about product trade-offs | A. Applied AI engineer |
| Liked the KV-cache and roofline labs most and enjoy making things fast | B. Inference and GPU engineering |
| Liked the GRPO ablation most and can accept that research roles are scarcer without a PhD | C. Research engineering |

Pay signals from 2026: level-controlled, ML roles pay about 1.3x comparable non-AI roles and the premium has stopped growing; inference and infrastructure specialists sit at the top of the band; "Machine Learning Engineer" titles pay well above "AI Engineer" titles for similar work. Pick by aptitude; the gap between the median and the top of any one track is larger than the gap between tracks.

## Track A: applied AI engineer

**Who it is for:** backend and full-stack engineers; people who like shipping and have product sense. This is where most of the jobs are.
**Time to employable depth:** 6 to 12 months after the core modules. Years to expert.

### Depth targets

By the end of this track you should be able to say "yes, I have done that" to each:

1. **Own the eval and observability stack for a production agent.** Golden sets, regression suites in CI, tracing of every tool call, dashboards for quality, cost and latency. You are the person who says whether a model upgrade is safe to ship.
2. **Design for model swaps and deprecations.** Prompts and tools regression-tested across at least two providers. A model change should cost you a config change and an eval run.
3. **Security.** Auth and RBAC enforced in the retrieval and tool layers, tool invariants checked in code before execution, prompt-injection defences you have actually tested with adversarial inputs.
4. **One vertical.** Legal, healthcare, finance, voice, logistics, education. Hiring threads say domain plus ML beats generic ML. Learn the vertical's data, regulations, and what "good" means to its users.
5. **Cost engineering as a habit.** Prompt caching, routing, batching, token budgets, small-model fallbacks. Know the cost per task of everything you run.

### Learning plan

**Months 1 to 3: take your agent to real users.**
- Take your Project 9 agent (A5b on the Novice track) to at least 10 real users and iterate from feedback for 3 months. Keep a changelog of what users broke and what you changed.
- Instrument everything. Add tracing (OpenTelemetry or any LLM observability tool; the method matters more than the vendor). Build the dashboard.
- Read Anthropic's context-engineering guide again and apply each principle: system prompt at the right altitude, minimal high-signal tokens, just-in-time retrieval, compaction, structured notes outside the context, sub-agents for focused work.

**Months 4 to 6: contribute upstream.**
- Contribute evals or tooling to an open-source agent or eval project (promptfoo, inspect-ai, smolagents, an MCP server). A merged PR in a project your target employers use is worth more than another demo.
- Learn MCP properly: build one server with real auth and one client that uses it.

**Months 7 to 12: go vertical and go public.**
- Build a second system in your chosen vertical with its real constraints (PII handling, audit trails, regulatory language).
- Write three posts: one on an eval method, one on a cost cut with numbers, one on a security failure you found and fixed.
- Give a talk.

### Production lessons from 2026, with numbers

- **Observability is table stakes; evals are the gap.** In a 1,340-response survey (late 2025), 89% of teams had observability and 62% detailed tracing, but only 52% ran evals. Quality was the top production blocker. Over 75% used multiple models and 57% did not fine-tune. Being the person who owns evals is the differentiator.
- **Cache the stable prefix; keep dynamic tool results out of it.** Across the three major APIs, prompt caching cut cost 41 to 80% and time-to-first-token 13 to 31% on 500+ agent sessions. Put dynamic content at the end of the system prompt. Naive full-context caching was less consistent and sometimes slower.
- **Compaction can double your bill and halve recall.** In an eleven-configuration study on one tutor agent, keeping full history cost $0.11 a turn with 92% memory recall; the summarize-and-clear preset cost $0.24 with 38% recall, because summarising rewrote the cached prefix. Capping tool outputs cut cost 38% with identical accuracy. Probe planted facts, not just overall quality: an overall-quality judge scored 97 to 99% while recall was 58%.
- **Re-run safety evals on every model upgrade and pin model IDs.** One documented upgrade dropped prompt-injection resistance from 94% to 71% because the newer model followed embedded instructions more literally. Canary with sampled traffic; keep failures as CI regressions.
- **Your eval suite is overfit to the incumbent model.** Regression cases grow from the current model's failures, so a challenger with different weaknesses scores lower. Tag regression vs capability cases, give each model its own best prompt, compare error distributions by severity, and re-baseline after migration.
- **Measure eval noise before claiming a regression.** Run the same set twice against the current model to learn how much outputs move on their own.
- **Prompt-injection defence means removing one leg of the "lethal trifecta":** private data, untrusted content, and the ability to communicate externally. If an agent has all three, it is exploitable. Vendor guardrails claiming 95% are, in Simon Willison's words, "a failing grade."
- **MCP in production:** a May 2026 measurement found 40% of nearly 8,000 live remote MCP servers exposed tools with no authentication, and every testable OAuth implementation had at least one flaw. Controls that matter: hash-pin tool definitions and re-approve on change; per-tool least-privilege tokens; OAuth 2.1 with PKCE and never forward the client's token upstream; human re-auth for high-risk actions; default-deny sandboxing; log agent identity, tool and redacted parameters.
- **Instrument once with OpenTelemetry** and treat the backend as swappable. The GenAI semantic conventions were still moving in mid-2026, so expect to adjust. Plan prompt and response redaction, because traces carry personal data.

### Projects that stand out

- An agent with a published eval harness and a public dashboard of its pass rate over time, across model versions.
- A write-up of a 50%+ cost reduction with the before/after breakdown (the best offer in one candidate's 15-interview run came from exactly this).
- A prompt-injection red-team of your own system with the fixes.

### Interview prep specific to this track

- ML system design: a GenAI app end to end (ingestion, retrieval, generation, evals, monitoring, cost). Practice on a whiteboard.
- "Why RAG instead of fine-tuning?" and "How did you measure hallucinations?" with numbers from your own project.
- Be ready to critique AI-generated code and a badly designed agent loop.

### Sources

- LangChain State of Agent Engineering survey (vendor-run, Jun 2026): https://langchain.com/state-of-agent-engineering
- AI Security Engineering, the sibling course (security depth for this track): https://aisec.engineering/
- "Don't Break the Cache", arXiv 2601.06007 (Jan 2026): https://arxiv.org/abs/2601.06007
- Context engineering cost study (Bouchard, 2026-08-18): https://www.louisbouchard.ai/context-engineering-2026/
- Model upgrades break agent safety (promptfoo, 2025-12-08): https://www.promptfoo.dev/blog/model-upgrades-break-agent-safety/
- Eval suites overfit to the incumbent (Tian Pan, 2026-07-03): https://tianpan.co/blog/2026/07/03/your-eval-suite-is-overfit-to-your-incumbent-model
- The lethal trifecta (Willison, 2025-06-16): https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- MCP authentication measurement study, arXiv 2605.22333 (May 2026): https://arxiv.org/abs/2605.22333
- CSA agentic MCP security best practices (2026-03-27): https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/
- Applied track targets from RAG engineers' daily work: https://www.reddit.com/r/learnmachinelearning/comments/1xjpfuv/comment/19rxgf6mnaa1x/
- Domain + ML beats generic ML: https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojpng9u/
- Next high-ticket skill thread, Jul 2026: https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p01xbed/
- Rebuilding depth in agent evaluation, Oct 2026: https://www.reddit.com/r/AI_Agents/comments/1xee1sh/
- Anthropic, Effective context engineering: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Anthropic, Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- MCP specification: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Track B: inference and GPU engineering

**Who it is for:** people who like systems, C/C++, performance, and finding out why something is slow. The FAANG MLE post says this end of the barbell has the strongest compensation growth.
**Time to employable depth:** 9 to 18 months after the core modules. Years to expert.

### Depth targets

1. **Trace one request through vLLM end to end** in a debugger: scheduling, continuous batching, paged KV cache, the forward pass, sampling. You should be able to explain where the time goes.
2. **Profile before optimizing.** torch.profiler and Nsight Systems. Form a falsifiable hypothesis (launch-bound vs memory-bound vs compute-bound), then measure. A software engineer struggling to become productive in inference infra was told in October 2026 (11 upvotes) that this habit is the whole job.
3. **Write and benchmark kernels.** Triton first, then CUDA C++. Understand the GPU memory hierarchy, occupancy, coalescing, shared memory, tensor cores.
4. **Distributed training basics.** Data, tensor and pipeline parallelism; FSDP; what breaks at 8 GPUs vs 64.
5. **Quantization and decoding tricks.** FP8 and INT4 formats, speculative decoding, prefix caching, and what each costs in accuracy.

### Learning plan

**Months 1 to 2: measure things.**
- Two-week artifact: a benchmark harness measuring time-to-first-token and tokens per second for one model across batch sizes, on one GPU, with vLLM. Publish the table.
- GPU MODE lectures 1 to 4 (profiling CUDA in PyTorch, PMPP recap, getting started with CUDA, compute and memory architecture). Join the GPU MODE Discord.
- CS336 lectures 5 and 6 (GPUs/TPUs, kernels and Triton).

**Months 3 to 6: write kernels.**
- Work through "Programming Massively Parallel Processors" (PMPP, 4th edition) chapters 1 to 6 alongside the GPU MODE recap lectures. Still the standard text per r/CUDA in 2026.
- CS336 assignment 2: reimplement FlashAttention2 in Triton and show the speedup against the naive version. Then build the distributed-training part.
- Enter one kernel competition (GPU MODE runs them). Losing is fine; the write-up is the point.

**Months 7 to 12: go inside a serving engine.**
- Read the vLLM (or SGLang) scheduler and KV-cache manager source. Write a post explaining paged attention from the code, not the paper.
- Reproduce one optimization: add prefix caching or speculative decoding to a small from-scratch server and measure it.
- A GRPO or SFT run where you cut cost by profiling and fixing the bottleneck. Numbers before and after.

**Months 12 to 18: contribute.**
- One merged PR to vLLM, SGLang, llama.cpp, Triton or a quantization library. Start with a benchmark or a bug reproduction; maintainers notice those.

### Practical tips from 2026 practitioners

- **Triton first, CUDA when Triton leaves performance on the table.** Vector add, then a matmul where memory access patterns matter. Triton handles coalescing, shared memory and scheduling for you; drop to CUDA, CUTLASS or ThunderKittens only when you need to.
- **Study vLLM by file, not by docs.** Start at the V1 scheduler (`vllm/v1/core/sched/scheduler.py`) and the KV-cache manager (`vllm/v1/core/kv_cache_manager.py`), then the engine core's busy loop and step function, then the process split between the API server and the engine. For SGLang, read the mini-sglang teaching implementation first, then the real scheduler.
- **Enter the GPU MODE leaderboard.** Install popcorn-cli, register through the Discord, pull a problem's submission file from the reference-kernels repo, and submit in test, benchmark and leaderboard modes against A100, H100, B200 and L4. The profiler returns Nsight Compute artifacts. Submissions are effectively unlimited.
- **Lesson from the team that topped that leaderboard** (NVIDIA's CUDA core libraries team, February 2026): for sort, scan, reduce and histogram, start from a proven library and hand-write only for novel algorithms, tight fusion or unusual memory patterns. Where they lost, it was to problem-size-specialised or inline-PTX kernels.
- **An agent loop can climb the leaderboard, but domain knowledge writes the prompts.** One hobbyist ran a coding agent through 1,500 submissions in 14 days and reached 12th of 183 on a QR-decomposition problem. He credits tight feedback loops and his own understanding of the algorithm, and he ran out of compute credits.
- **Do not trust kernel speedups at face value.** Under a verified protocol (realistic baselines, hidden test distributions, memory metrics), the best model's "1.43x faster than PyTorch" became 0.88x. Models hard-code bypasses for specific tensor values. Any kernel claim you publish needs a fair baseline and hidden tests.
- **Speculative decoding is now a config flag**, so the differentiator is understanding acceptance rates and when they collapse. Low-precision formats (FP8, NVFP4) claim near-parity accuracy at much higher throughput; verify on your own evals, not the vendor's.
- **Projects that read as GPU-role-ready start from a named bottleneck** (the paged-attention decode kernel, fused RMSNorm, HBM-bound attention at small batch) and show a profiler-backed before and after.
- **Benchmark write-ups need the fields reviewers expect:** engine version, hardware, time-to-first-token, time-per-output-token, p99, VRAM, and output quality. Never a single throughput number.

### Projects that stand out

Per the August 2026 r/CUDA thread on what stands out for GPU and compiler roles: a kernel with a benchmark against the library baseline, a profiler-driven optimization write-up, and a contribution to a real serving engine. Not "I did the CUDA course".

### Interview prep specific to this track

- Explain the roofline model and place your kernel on it.
- "Why is this kernel slow?" given a profiler trace.
- Design an inference service for a 70B model at a given latency target and budget.
- Memory math: parameters, KV cache size per token, batch size limits.

### Sources

- Triton-first kernel path (2026-08-29): https://anirudhs16.github.io/ai-systems/2026/08/29/triton-first-gpu-kernel/
- vLLM forum on where to start in the scheduler: https://discuss.vllm.ai/t/where-to-start-for-implementing-custom-memory-block-aware-scheduling-in-vllm/2157
- GPU MODE popcorn-cli and reference kernels: https://github.com/gpu-mode/popcorn-cli and https://github.com/gpu-mode/reference-kernels
- NVIDIA on topping the GPU MODE leaderboard (2026-02-18): https://developer.nvidia.com/blog/topping-the-gpu-mode-kernel-leaderboard-with-nvidia-cuda-compute/
- Agent loop on the leaderboard (2026-08-17): https://aimatterin.substack.com/p/a-codex-loop-ran-1500-submissions
- KernelBench-Verified, arXiv 2607.16241 (June 2026): https://arxiv.org/abs/2607.16241
- vLLM P-EAGLE speculative decoding (2026-03-13): https://vllm.ai/blog/2026-03-13-p-eagle
- vLLM contributing guide: https://docs.vllm.ai/en/stable/contributing/
- SWE closing inference-infra gaps, Oct 2026: https://www.reddit.com/r/learnmachinelearning/comments/1xfkwyp/comment/19rnuzo541r8k/ and https://www.reddit.com/r/learnmachinelearning/comments/1xfkwyp/comment/19rnvkbisy9es/
- Inference engineering problems that matter, May 2026: https://www.reddit.com/r/CUDA/comments/1t5txel/comment/oker8gc/
- Where to start with CUDA in 2026 (25 pts): https://www.reddit.com/r/CUDA/comments/1uwlc0r/comment/oxk528y/
- Projects that stand out for GPU/compiler roles, Aug 2026: https://www.reddit.com/r/CUDA/comments/1vtngli/
- vLLM docs: https://docs.vllm.ai/
- GPU MODE lectures: https://github.com/gpu-mode/lectures
- PMPP 4th ed.: https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0
- CS336 assignment 2: https://github.com/stanford-cs336/assignment2-systems

## Track C: research engineering

**Who it is for:** people who want to be near the frontier and can run careful experiments. Be honest with yourself: Research Scientist roles at top labs still mostly want PhDs and publications. Research Engineer roles and safety fellowships are open to strong self-taught people. Aleksa Gordić got a DeepMind Research Engineer role without an ML degree; he says a Research Scientist role would likely have needed a PhD.
**Time to employable depth:** 12 to 18 months after the core modules, plus a fellowship or an equivalent piece of research-grade work.

### Depth targets

1. **Replicate a recent paper exactly, then run a controlled ablation.** Change one variable at a time. Report what did not work. One well-run ablation is worth more than ten demos.
2. **Post-training from scratch.** SFT, DPO, GRPO/RLVR implemented yourself; reward design; KL tuning; evaluating by capability rather than one aggregate score.
3. **Interpretability basics.** Transformers from scratch, linear probes, sparse autoencoders, circuit analysis. Know the faithfulness debate (a May 2026 r/MachineLearning thread on disillusionment with mechanistic interpretability is required reading, including the replies).
4. **Research writing.** Clear write-ups with negative results, plots that answer one question each, and code someone else can run.
5. **Deeper math than the engineering tracks.** Probability, linear algebra and optimization at textbook level. The self-taught research stories all stress this.

### Learning plan

**Months 1 to 4: ARENA, self-paced.**
The Alignment Research Engineer Accelerator curriculum is free and updated for 2026. Chapters: 0 Fundamentals (skip if Modules 03 to 06, or A4, are done), 1 Interpretability (13 sections), 2 RL (8 sections, ending at LLM post-training techniques), 3 Evals (5 sections, including agents), 4 Alignment Science. Do chapters 1 to 3 in order. Budget 10 to 15 hours a week.

**Months 3 to 6: GRPO from scratch with ablations.**
- Raschka's "Build a Reasoning Model (From Scratch)" chapters 6 to 8: RL with verifiable rewards, GRPO-style policy optimization, distillation.
- Then write your own GRPO notebook on a small model (Qwen3 0.6B class) and run ablations: reward shaping, KL coefficient, group size, format rewards. Several r/reinforcementlearning and r/LocalLLaMA posters did this in 2026. Publish the notebook and the negative results.
- CS336 lectures 15 and 16 and assignment 5 (alignment and reasoning RL).

**Months 6 to 12: one research-grade artifact.**
- Pick one recent paper in your sub-area. Replicate it. Then ask one question it did not answer and run the ablation. Write it up as a short paper-style post with a limitations section.
- Share it in the communities where that work happens (EleutherAI Discord, LessWrong/Alignment Forum for safety work, the paper authors by email).

**Months 9 to 18: apply.**
- MATS Fellowship: 12 weeks in Berkeley or London, $1,250 a week stipend plus $2,000 a week compute, no PhD required, with a 6 to 12 month funded extension possible. The Residency expects you already have one research-grade piece of work. Check application windows early; the Winter 2027 cohort closed before November 2026.
- Also look at: lab residency programs, Research Engineer postings at labs and at applied research teams in industry, and open-research collectives.

### Practical tips from researchers and 2026 applicants

- **Stage your self-study by feedback-loop length.** Neel Nanda (DeepMind interpretability lead, MATS mentor): about a month of basics, then 1 to 5 day mini-projects, then 1 to 2 week research sprints, continuing only the best. Skills group by how long their feedback loop is: minutes (running and debugging experiments), weeks (knowing when to pivot), months (generating ideas). Use LLMs heavily while learning.
- **"Gain surface area."** Nanda's most productive mode is exploring a confusing system without a fixed hypothesis, holding about four loosely held hypotheses and noting what surprises him. Check every toy-model theory against a real, messy model.
- **A budget GRPO project that is honest about failure is a strong artifact.** A consultancy engineer trained a 1.5B coding model with LoRA on one rented 48GB GPU and 10k problems: compile rate went from 2 in 10 to 7 in 10, with reward hacking (comment spam, markdown spam), local optima from graduated rewards, and regressions on standard-library use. His lessons: inspect completions, not metrics; track reward variance within a prompt group (more useful than loss); evaluate intermediate checkpoints; expect most of the effort to go into the reward pipeline.
- **GRPO on one GPU:** use a model of at least 1.5B parameters so it reliably emits reasoning tokens; LoRA and QLoRA work; co-locate the inference engine for rollouts. A 4B model with LoRA fits in 40 to 48 GB.
- **MATS, from a 2026 admit:** about two hours for the initial application, then a 1.5-hour coding test on evaluating LLM outputs, a 1.5-hour research-taste test, and stream essays of about 4,500 words (20 to 25 hours). Apply to 3 to 5 streams, pick a less crowded topic, make proposals specific (which models, what intermediate results would mean, which evals). He was rejected by 8 of 9 streams and still got in. Budget 35 to 40 hours. Acceptance runs about 4 to 7%.
- **What MATS reviewers weigh:** externally reviewed output, then a strong first-author post on LessWrong or the Alignment Forum, then nothing. Front-load your strongest point. Avoid AI-written text in the application. Practise everyday Python fluency without an assistant for the coding screen. Career-changers need a clear "why now."
- **ARENA runs several short cohorts a year** and takes expressions of interest when closed. **EleutherAI's** entry point is showing up in the Discord and messaging project leads; their FAQ at the time of this research said they have "many more beginners than beginner-friendly tasks," so bring a specific skill (the FAQ page has since been folded into their community page). Their mentored summer research program is the structured route.
- **Write up negative results.** The field's reluctance to publish them has a chilling effect even on personal blogs. A clear write-up of what did not work, and why, is rarer and more useful than another positive demo.
- **Raschka's warning:** do not read raw RLHF papers cold; "you would be spending two years." Use a from-scratch book or course as the ramp, then the papers.

### Projects that stand out

- A replication plus ablation with negative results, clearly written.
- A from-scratch GRPO implementation with a results table across settings.
- An interpretability probe or SAE study on a small open model with a clear finding.
- A merged contribution to an evals library (inspect-ai) or a post-training library (TRL).

### The honest part

A PhD holder in an adjacent field could not get ML roles without ML-centred work on his profile. An 18-year-old at a tier-3 college asking how to get into research in November 2026 was told: do real work in public and find a mentor; the credential gap is real but public work closes it. If you want this track, your public output must be research, not demos.

### Sources

- Neel Nanda, how to become a mech interp researcher (updated 2025-09-02): https://www.lesswrong.com/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher
- nilenso, small model with RLVR and GRPO (2026-05-18): https://blog.nilenso.com/blog/2026/05/18/training-a-small-model-to-write-better-ocaml-with-rlvr-and-grpo/
- Evan Conway, MATS application write-up (2026-08-23): https://evanjayconway.com/posts/2026/mats-application/
- Georg Lange, application guide (2025-10-26): https://georglange.com/post/ai-safety-application-guide/
- MATS admissions FAQ: https://www.matsprogram.org/faq/getting-into-mats
- ARENA: https://www.arena.education/
- EleutherAI FAQ: https://eleuther.ai/community/
- Position: Embracing Negative Results in ML: https://arxiv.org/abs/2406.03980
- Raschka on Lex Fridman #490 (Feb 2026): https://lexfridman.com/ai-sota-2026-transcript
- Gordić on Research Engineer vs Research Scientist: https://gordicaleksa.medium.com/how-i-got-a-job-at-deepmind-as-a-research-engineer-without-a-machine-learning-degree-1a45f2a781de
- Lessons from training three LLMs, ablation advice: https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/comment/p48miv4/
- Disillusionment with mech interp, May 2026: https://www.reddit.com/r/MachineLearning/comments/1t6zdj6/comment/okm2arl/
- ML research from a tier-3 college, Nov 2026: https://www.reddit.com/r/research/comments/1xlxffr/comment/19s151f29jrk3/
- ARENA curriculum (chapters verified Nov 2026): https://learn.arena.education/
- MATS program (stipend verified Nov 2026): https://www.matsprogram.org/
- Raschka, reasoning from scratch: https://sebastianraschka.com/reasoning-from-scratch
- smol-course RL unit: https://huggingface.co/learn/smol-course/en/unit0/1

## Build projects

Self-directed work after the core, any track:

- A public eval dashboard for one open-source agent, updated on each model release, with the noise band shown.
- A reproduction of one serving optimisation with a fair benchmark and hidden test set.
- A from-scratch post-training notebook with an ablation table and negative results.
- A domain assistant in a regulated vertical with audit trails, permissions and a red-team suite.
- A contribution to an evals library that adds a calibrated judge with reported TPR and TNR.

## Continuing practice

Every model release: re-run your evals. Every quarter: one replication or one upstream PR. Every year: one long study outside your track. The Module 17 plan is the template.
