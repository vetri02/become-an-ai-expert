# First principles

Twenty facts the subject rests on. Each is stated, then derived from how the thing works rather than from who said it, then tied to the module that teaches it on each track (the novice on-ramp A1 to A5, then the numbered modules from 03), the lab that demonstrates it where one exists, and the best single source. If a later claim in this course contradicts one of these, the claim is wrong.

The labs are in `labs/` and run with `labs/run_all.sh` (Python 3 and NumPy only; no GPU). Each prints the measurement that backs its principle and fails if the measurement does not hold.

## The build path: watch a language model get built

The principles below are easiest to hold if you have watched someone build the thing. These recordings, in this order, are that build path; each is verified in the media library and plays on its module page.

1. [V13 Intro to Large Language Models](MEDIA-LIBRARY.md#v13), one hour, before Module 03: the map.
2. [V07 micrograd](MEDIA-LIBRARY.md#v07) and [V08 makemore](MEDIA-LIBRARY.md#v08), Modules 02 and 03: backprop and the next-token objective (Principles 1, 3).
3. [V11 the GPT tokenizer](MEDIA-LIBRARY.md#v11), Module 03: Principle 2.
4. [V15](MEDIA-LIBRARY.md#v15) and [V16](MEDIA-LIBRARY.md#v16), 3Blue1Brown on Transformers and attention, then [V17 Let's build GPT](MEDIA-LIBRARY.md#v17), Module 04: Principle 4.
5. [V18 Let's reproduce GPT-2](MEDIA-LIBRARY.md#v18), [V19 scaling laws](MEDIA-LIBRARY.md#v19) and [V20 inference](MEDIA-LIBRARY.md#v20), Module 05: Principles 5, 6, 7.
6. [V14 Deep dive into LLMs](MEDIA-LIBRARY.md#v14), [V22 RLVR](MEDIA-LIBRARY.md#v22) and [V23 GRPO from scratch](MEDIA-LIBRARY.md#v23), Module 06: Principle 8.
7. [V26](MEDIA-LIBRARY.md#v26) and [V27](MEDIA-LIBRARY.md#v27) on evals, Module 08: Principles 11 to 15.
8. [V31 Prompt injection, explained](MEDIA-LIBRARY.md#v31), Module 10: Principle 16.

## The model

**1. A language model is a function from a token sequence to a probability distribution over the next token. Everything else is sampling from it repeatedly.**
Derivation: the training objective is next-token cross-entropy. Chat, reasoning traces, tool calls and agent loops are all produced by appending the sampled token and calling the function again. There is no other mechanism inside the model.
Novice A4; Module 03. Lab 03 generates tokens this way. Source: Karpathy, "Let's build GPT" (Zero to Hero).

**2. Text enters the model as tokens, not words, and the tokenizer determines sequence length and therefore cost.**
Derivation: byte-pair encoding merges the most frequent adjacent pair repeatedly; more merges means a bigger vocabulary and shorter sequences. Compute and price scale with token count, so the tokenizer sets the bill.
Novice A4; Module 03. Lab 05 trains a BPE tokenizer and shows 40 bytes becoming 20 tokens as merges increase. Source: Karpathy, "Let's build the GPT tokenizer".

**3. Learning is minimising a loss by stepping against its gradient; the chain rule makes the gradient computable through any composition of differentiable pieces.**
Derivation: a network is a composition of functions; the derivative of a composition is the product of the derivatives. A learning rate too large overshoots and diverges; too small never arrives.
Novice A2; Module 02. Lab 01 fits a line and a logistic regression by hand and shows divergence at a 15x learning rate. Source: Karpathy, "micrograd"; 3Blue1Brown, neural networks series.

**4. Attention is a weighted average of value vectors, with weights from query-key similarity. The causal mask stops a position from seeing its future, and dividing by the square root of the head size stops the softmax from saturating.**
Derivation: softmax rows sum to one and are non-negative, so the output is an average. A dot product of d independent terms has spread proportional to sqrt(d); without the division, larger heads produce near-one-hot weights.
Novice A4; Module 04. Lab 02 verifies all three properties numerically. Source: Vaswani et al., "Attention Is All You Need"; Raschka, "Build a Large Language Model (From Scratch)", chapter 3.

**5. Generation is sequential. Caching keys and values turns each decode step from recomputing the whole sequence into one new row, trading memory for compute.**
Derivation: at step t only the new token's query is needed; the keys and values of earlier tokens do not change. Storing them makes each step linear in context length instead of quadratic over the whole generation.
Novice A4; Module 05. Lab 03 shows identical outputs with a 10x-plus speedup, and that the cache grows linearly. Source: a learner's 278-second to 28-second measurement, r/learnmachinelearning, Apr 2026; CS336 lecture 10.

**6. Inference is usually bounded by memory, not arithmetic. Weights plus KV cache must fit, and KV cache per token equals two times layers times KV heads times head dimension times bytes per value.**
Derivation: each layer stores K and V for every token; the batch you can serve is the free memory after weights divided by cache per sequence. Grouped-query attention cuts KV heads and therefore multiplies the feasible batch.
Novice A4; Module 05; Track B (Module 15). Lab 06 computes this for 7B, 8B and 70B configurations and shows the 70B model does not fit on one 80 GB GPU in bf16. Source: vLLM docs on paged attention; CS336 lecture 10.

**7. Training loss falls predictably with compute, data and parameters, so a fixed budget has a best split between model size and tokens.**
Derivation: fitted power laws across many runs; the Chinchilla result says most earlier models were too large for their data. This is why small models trained on more tokens keep matching larger ones.
Novice A4; Module 05. Source: Hoffmann et al., "Training Compute-Optimal Large Language Models" (Chinchilla); CS336 lectures 9 and 11.

**8. Pretraining gives knowledge and a prior; supervised fine-tuning changes format and behaviour; reinforcement learning optimises a reward and can degrade anything the reward does not measure.**
Derivation: each stage updates the same weights toward a different objective. An objective that scores only math answers has no term that protects general ability, so general ability can fall. Reward functions are specifications and get gamed where they are loose.
Novice A4; Module 06; Track C (Module 16). Evidence: a learner's GRPO run degrading general ability at small scale (r/learnmachinelearning, Aug 2026); reward hacking by comment spam in a 2026 GRPO write-up (nilenso). Source: Raschka, "Build a Reasoning Model (From Scratch)", chapters 6 and 7.

**9. The model knows nothing after its training data. Retrieval puts facts into the context, and the context is a finite attention budget in which every token competes.**
Derivation: weights are fixed after training; the only inputs at inference are the tokens in the context. Attention has a fixed capacity, so irrelevant tokens dilute relevant ones and raise cost.
Novice A5; Modules 07 and 09. Source: Anthropic, "Effective context engineering for AI agents" (Sep 2025).

**10. Fine-tuning is a poor way to add facts and a good way to change behaviour, because a few hundred gradient steps shift style and format far more reliably than they encode new knowledge.**
Derivation: facts are distributed across many weights learned from many contexts; a small fine-tuning set gives few, correlated contexts. Retrieval supplies facts at inference without touching weights.
Novice A5; Modules 07 and 11. Source: production teams in r/Rag, Sep 2026; LangChain survey (57% of teams do not fine-tune).

## Measuring

**11. Retrieval quality and generation quality are separate failure modes and must be measured separately.**
Derivation: a system can retrieve the right chunk and still answer wrongly, or answer plausibly from the wrong chunk. One end-to-end score cannot tell you which to fix.
Novice A5; Module 08. Lab 04 measures recall@k and groundedness independently. Source: Hamel Husain and Shreya Shankar, AI Evals FAQ.

**12. A metric you have not checked against raw outputs is a hypothesis. Error analysis precedes tooling.**
Derivation: metrics are proxies chosen before you know the failure modes; the failure modes are only visible in the outputs. Reading 20 to 50 outputs reveals the categories the metric should have.
Novice A3 and A5; Modules 02 and 08. Source: Evals FAQ ("start with error analysis, not infrastructure"); Anthropic agent-evals guide.

**13. An evaluation that influenced the thing it evaluates measures overfitting, not quality. Test sets must be held out and versioned, and leakage inflates every metric.**
Derivation: any signal from the test set used in training or prompt-tuning is a signal the model has already seen. Grouped and time-ordered data leak through features that would not be known at prediction time.
Novice A3 and A5; Modules 02 and 08. Source: scikit-learn "Common pitfalls"; a 2026 post on eval suites overfit to the incumbent model (Tian Pan).

**14. A judge built from a model is itself a model with error rates. It needs a true-positive and true-negative rate against human labels before its scores mean anything.**
Derivation: a judge that misses 30% of failures reports a system as 30% better than it is. Only a labelled set reveals that.
Novice A5; Module 08. Lab 04 calibrates a judge against 400 labels. Source: Evals FAQ (100 to 200 labels per failure mode, report TPR and TNR).

**15. Reliability compounds. If one step succeeds with probability p, k independent steps all succeed with probability p to the k. Agents must be measured with pass^k, not only pass@k.**
Derivation: independence multiplies probabilities. A 75% step over three trials gives 42% all-pass. Capability (any success) and reliability (every success) are different numbers.
Novice A5; Modules 08 and 09. Lab 04 computes both. Source: Anthropic, "Demystifying evals for AI agents" (Jan 2026).

**16. Prompts are not a security boundary. Any text in the context, including retrieved documents and tool results, can act as instructions. Enforcement belongs in code.**
Derivation: the model has one input channel and cannot distinguish instructions from data by origin. An agent with private data, untrusted content and a way to communicate out is exploitable by construction.
Novice A5; Module 10; Track A (Module 14). Source: Simon Willison, "The lethal trifecta" (Jun 2025); promptfoo's measured drop in injection resistance after a model upgrade (Dec 2025).

## Cost and change

**17. Cost is tokens times price and latency is prefill plus decode steps. The levers are fewer tokens, cheaper tokens, cached tokens and shorter outputs.**
Derivation: follows from principles 1, 2 and 5. Caching the stable prefix avoids recomputing it; routing simple requests to small models cuts price per token; capping outputs cuts decode steps.
Novice A5; Module 10. Evidence: prompt caching cut cost 41 to 80% on 500+ agent sessions (arXiv 2601.06007); summarising a cached prefix doubled a tutor agent's cost (Bouchard, Aug 2026).

**18. GPU work is bound by whichever of memory bandwidth or arithmetic runs out first. Profile before optimising, because intuition about which one is wrong most of the time.**
Derivation: the roofline model. Decode at small batch reads every weight once per token and does little arithmetic per byte, so it is bandwidth-bound; large-batch prefill is compute-bound. The fix differs completely between the two.
Module 15 (Track B). Source: GPU MODE lecture 1 (profiling); CS336 lectures 5 and 6; KernelBench-Verified (June 2026) on why unverified speedups mislead.

**19. Models change under you. Every statement about a system is true for a model version, so evals must be re-run on each release with the model ID pinned.**
Derivation: a model upgrade changes the function in principle 1; nothing downstream is guaranteed to hold. A documented upgrade dropped injection resistance from 94% to 71%.
Novice A8; Modules 13 and 17; Track A (Module 14). Source: promptfoo (Dec 2025); FAANG MLE on re-running evals each release (r/MLjobs, May 2026).

**20. An AI system is a distributed system with a probabilistic component. The software fundamentals (types, tests, memory, networking, deployment) are not a prerequisite to the subject; they are most of it.**
Derivation: everything above runs as services exchanging tokens over networks with budgets and failure modes. Hiring managers reject candidates who can build a demo and cannot explain an abstract class, because the demo is the smaller part.
Novice A1; Module 01. Source: r/MachineLearningJobs hiring manager, Sep 2026; r/ExperiencedDevs 1,500-upvote thread, Sep 2026.

## Coverage: which lab demonstrates which principle

| Principle | Lab | What the lab measures |
|---|---|---|
| 1 next-token distribution | lab07_next_token.py | Trigram P(next | previous); sampling; temperature; unseen words get only smoothing mass |
| 2 tokens and cost | lab05_bpe_tokenizer.py | BPE merges; 40 bytes become 20 tokens; lossless round trip |
| 3 gradient descent | lab01_gradient_descent.py | Line and logistic fits by hand; divergence at a 15x learning rate |
| 4 attention | lab02_attention.py | Rows average to one; causality; entropy 2.68 scaled vs 0.00 unscaled at d=256 |
| 5 KV cache | lab03_kv_cache.py | Identical outputs; 10x-plus speedup; linear cache growth |
| 6 serving memory | lab06_serving_memory.py | Weights plus KV cache for 7B, 8B and 70B; GQA multiplies batch; 70B bf16 does not fit 80 GB |
| 7 scaling laws | lab08_scaling_law.py | Held-out loss vs data size on a Markov source; fitted power-law exponent; irreducible floor |
| 8 post-training and reward | lab09_rl_reward_hacking.py | REINFORCE raises reward, degrades held-out likelihood, over-produces the rewarded token; KL penalty limits it |
| 9 finite attention budget | lab10_context_and_cost.py | Softmax weight on the relevant chunk falls from ~1.0 to 0.10 as 128 distractors are added |
| 10 fine-tuning vs facts | none | Rests on cited production evidence; a faithful demonstration needs a real model and is Project 5's SFT step |
| 11 retrieval vs generation | lab04_eval_harness.py | recall@k and groundedness measured separately |
| 12 error analysis first | none (method) | Practised in Projects 3, 8 and 9; the lab harness only measures what error analysis found |
| 13 held-out and versioned | lab04_eval_harness.py | Golden set is versioned; lab13 shows noise measurement |
| 14 judge calibration | lab04_eval_harness.py | TPR and TNR of a judge against 400 human labels |
| 15 reliability compounds | lab04_eval_harness.py | pass@3 = 0.98 vs pass^3 = 0.42 at p = 0.75 |
| 16 prompts are not security | lab11_prompt_injection.py | Injected instruction exfiltrates data; a stronger prompt changes nothing; a code allowlist blocks it |
| 17 cost and latency | lab10_context_and_cost.py | Request cost with and without prefix caching (68% cheaper); prefill plus decode latency |
| 18 roofline | lab12_roofline.py | Arithmetic intensity vs the H100 ridge; measured 47x GFLOP/s gain from batch 1 to 64 on the same weights |
| 19 models change | lab13_model_upgrade.py | Noise band from ten runs; an upgrade that improves the overall score while injection resistance falls 0.91 to 0.30 |
| 20 software fundamentals | none (practice) | Demonstrated by Capability C1, a deployed and tested service; the lab suite itself is a small example |

Seventeen of twenty principles have a runnable demonstration. The three without (10, 12, 20) are methods or require a real model, and each names the project that provides its evidence.

## How these were chosen

A fact made the list only if it can be derived from the mechanism, if the course would be wrong without it, and if at least one module depends on it. Claims that are true but contingent (which framework is popular, which model is best this month, what a role pays) are kept out of this file and dated wherever they appear in the modules.
