# Course verification report

Prepared 2026-11-06 by `checks/verify.py`. Every number below was produced by a command run on that date in this build environment.

## Labs

- `labs/run_all.sh`: 13 passed, 0 failed (exit 0). Python 3.14.6, NumPy only.

- lab01_gradient_descent.py: logistic: w=[5.49 5.35] (direction should be ~[1,1]), accuracy 0.995, loss 0.693 -> 0.090
- lab02_attention.py: entropy of the last row's attention over 32 positions at d_head=256: scaled 2.68, unscaled 0.00 (max possible 3.47)
- lab03_kv_cache.py: cache size after 403 tokens, one layer, float64: 403.0 KB (grows linearly with context)
- lab04_eval_harness.py: agent with per-trial success 0.75: pass@3 = 0.98 (capability), pass^3 = 0.42 (reliability)
- lab05_bpe_tokenizer.py: longest learned token after 40 merges: 'model predicts the next token. the next token depends on'
- lab06_serving_memory.py: (70B in bf16 needs >1 GPU or quantization: at INT4 the weights are ~35 GB)
- lab07_next_token.py: P('predicts' | 'the model') = 0.426; P('agent' | 'the model') = 0.0042 (never seen, smoothing only)
- lab08_scaling_law.py: ten times the data cuts the excess loss by about 4.5x, not to zero: that is the diminishing return
- lab09_rl_reward_hacking.py: the reward went up, ordinary-text likelihood went down, and the policy found the loophole in the reward; the KL term is the leash
- lab10_context_and_cost.py: latency: prefill ~325 ms + decode 300 x 25 ms = 7825 ms; halving the output saves 3750 ms
- lab11_prompt_injection.py: the trifecta (private data + untrusted content + outbound channel) was broken in code, not in the prompt
- lab12_roofline.py: same weights, same FLOPs per sequence: the small batch is waiting on memory, not arithmetic
- lab13_model_upgrade.py: the overall number hid a safety regression; tag suites by failure mode and compare each against its noise

## Targets

- Target self-tests: ran 15, OK (exit 0).
- stale_cache: vulnerable build 1 of 5 stages passed; reference solution 5 of 5 stages passed.
- leaky_eval: vulnerable build 0 of 5 stages passed; reference solution 5 of 5 stages passed.
- leaky_agent: vulnerable build 0 of 5 stages passed; reference solution 5 of 5 stages passed.

## Citations

- `checks/check_links.py` last run 2026-11-06: 229 distinct URLs in 416 citations; ok 175, blocked 54.
- BLOCKED means the host refuses the plain checker. Each such URL has a second-method record in CHECKS.md: Reddit threads are matched to the research captures of 2026-11-04 (title, date, score); the rest carry a dated manual record in checks/manual-verification.json. No disguised client is used. Second-method tally: fetch-tool 1, research-capture 53; 0 unverified.

## Content counts

- 17 modules, 107 quiz questions, 17 answer-key files, 5 milestones, 1 capstone, 10 exam scenarios.
- 54 recordings in the media catalogue, each fetched on 2026-11-05 and confirmed playable by page metadata; none watched in full.
- 20 first principles; 17 have a runnable lab (FIRST-PRINCIPLES.md has the coverage table).

## Standard 6: one primary resource per module

- `checks/check_primary.py`: 0 module(s) violate standard 6 (exit 0). Each module carries exactly one primary-resource line naming one URL that also appears in its reading list.

## Limitations

- The labs demonstrate mechanisms with NumPy on a laptop; no GPU training, hosted model or vector database was run in this environment. The nanochat, LoRA and GRPO runs in Modules 05, 06 and 11 are learner-run and their costs are quoted from the sources named there.
- The targets use a toy decoder, a synthetic eval system and a regular-expression model. Passing a grader proves the invariant against the fixtures, not a property of any real model or product.
- Prices, pay and tool names are dated in the modules and the compute appendix; re-check at signup.
- The evidence base is practitioner opinion, vetted self-reported stories and official resource pages, not a hiring-outcome dataset.
