# Working glossary

## The model

**Token:** the unit the model reads and writes; a subword chosen by the tokenizer, not a word. Cost and context limits count tokens.

**Byte-pair encoding (BPE):** a tokenizer trained by repeatedly merging the most frequent adjacent pair; more merges mean a larger vocabulary and shorter sequences.

**Next-token objective:** the training loss, cross-entropy on the next token; the only thing a language model is trained to do (Principle 1).

**Logits:** the raw scores over the vocabulary before the softmax.

**Temperature:** a divisor on the logits before the softmax; low sharpens, high flattens; it never adds knowledge.

**Embedding:** the vector a token id becomes; the unembedding maps the final vector back to logits.

**Attention:** a weighted average of value vectors where weights come from query-key similarity; the causal mask hides the future; the sqrt(d) scaling keeps the softmax from saturating (Principle 4).

**Residual stream:** the vector carried through the layers that each block adds to; why deep Transformers train.

**KV cache:** the stored keys and values of earlier positions so each decode step computes one new row (Principle 5). Size per token = 2 x layers x KV heads x head size x bytes.

**Grouped-query attention (GQA):** fewer KV heads than query heads; shrinks the KV cache and multiplies the feasible batch.

**Prefill and decode:** processing the prompt all at once (compute-bound) versus producing tokens one at a time (bandwidth-bound at small batch).

**Scaling law:** loss as a power law in data, parameters and compute; Chinchilla gives the compute-optimal split (Principle 7).

**Pretraining:** next-token training on a large corpus; gives knowledge and a prior.

**Supervised fine-tuning (SFT):** training on instruction-response pairs; changes format and behaviour, not reliably facts (Principles 8, 10).

**Direct preference optimisation (DPO):** training on preferred-versus-rejected pairs without a separate reward model.

**RLVR and GRPO:** reinforcement learning with verifiable rewards; GRPO uses group-relative baselines; the KL penalty keeps the policy near the reference.

**Reward hacking:** the policy finding a loophole in the reward specification; lab 09's "please" spam.

**LoRA:** low-rank adapters trained while base weights stay frozen; cheap fine-tuning that fits one GPU.

**Inference-time scaling:** best-of-N, majority voting, self-refinement; buys quality with compute at inference, sometimes negatively.

## Systems

**Retrieval-augmented generation (RAG):** putting retrieved documents into the context so the model can answer from them (Principle 9).

**Hybrid search:** lexical (BM25) plus vector retrieval, fused by rank.

**Reciprocal rank fusion:** combining ranked lists by summing 1/(k + rank); robust to score scales.

**Reranker:** a second model that reorders the top results; costs latency.

**Golden set:** a versioned set of real questions with expected sources; the yardstick for retrieval (Principle 13).

**Context window:** the finite attention budget; every token competes (Principle 9).

**Context engineering:** choosing the smallest set of high-signal tokens: system-prompt altitude, tool design, just-in-time retrieval, compaction, notes outside the context, sub-agents.

**Compaction:** summarising history to fit the context; can raise cost by breaking the cached prefix and cut recall.

**Prompt caching:** reusing the computation for a stable prefix; put dynamic content at the end.

**Agent:** a loop in which the model proposes, code validates, a tool runs, and the result returns as tokens; rules live in code.

**Tool invariant:** a condition checked in code before a tool executes; schema validation is not safety.

**Model Context Protocol (MCP):** a protocol for exposing tools to models; pin tool definitions, least-privilege tokens, never forward the client token upstream.

**Lethal trifecta:** private data, untrusted content and an outbound channel in one agent; remove one leg in code (Principle 16).

**Prompt injection:** instructions arriving as data (documents, tool results) that the model may follow; prompts are not a security boundary.

**Roofline:** the plot of achievable throughput against arithmetic intensity; says whether a kernel is bound by bandwidth or compute (Principle 18).

**Speculative decoding:** a small draft model proposes tokens the large model verifies in one pass; the benefit depends on the acceptance rate.

**Paged attention:** managing the KV cache in fixed-size blocks like virtual memory; the vLLM idea.

## Measurement

**Error analysis:** reading 20 to 50 outputs by hand, labelling pass/fail, grouping notes into failure categories; precedes tooling (Principle 12).

**Code grader:** a deterministic check (parses, cites, abstains); used wherever a rule can catch the failure.

**LLM-as-judge:** a model grading outputs; a model with error rates that needs calibration (Principle 14).

**True-positive and true-negative rate (TPR, TNR):** how often the judge passes real passes and fails real failures, against human labels.

**Groundedness:** whether an answer is supported by a retrieved chunk it cites.

**Abstention:** saying "I don't know" when retrieval returns nothing relevant; the measured answer to "how did you measure hallucinations".

**recall@k:** the fraction of golden questions whose relevant chunk is in the top k results.

**pass@k and pass^k:** the probability that any of k trials succeeds versus that all do; capability versus reliability (Principle 15).

**Noise band:** the spread of a suite's score across repeated runs of the same model; a difference inside it is sampling (Principle 19).

**Regression suite:** cases from past failures run on every change; overfit to the incumbent model unless tagged and re-baselined.

**Leakage:** test information reaching training or tuning; group-aware and time-ordered splits prevent it.

**p50 and p95:** median and 95th-percentile latency; users feel p95.

**Time to first token (TTFT) and time per output token (TPOT):** the two latency numbers a serving benchmark must report.

## Career

**Adjacent role:** a job that touches AI without an AI title; the most common route into ML in the evidence.

**Public record:** posts, repos and talks a stranger can cite; what produces referrals.

**Depth probe:** the interview round that asks "why" five levels deep on one thing you built.

**Expert markers:** own a problem end to end; known outside the company; arbitrarily deep under questioning; learn on a cadence.
