# Capabilities and evidence

The course is passed by producing evidence, not by finishing videos. Each row names a capability, the artifact that proves it, and the bar it must clear. A reviewer (a mentor, a community member, or you in a month) should be able to check every row from the artifact alone.

"Lab" means the runnable scripts in `labs/`. "Project" means the numbered rungs in the project ladder appendix.

## Core (both paths)

| # | Capability | Evidence artifact | Passes when | Module | Principle |
|---|---|---|---|---|---|
| C1 | Build, test and deploy a small Python service | Repo with Dockerfile, 10+ pytest tests, live URL | A stranger clones, tests pass, URL responds; you explain any function without opening the file | A1 / Stage 1 | 20 |
| C2 | Explain and implement gradient descent | Lab 01 run plus your own NumPy notebook (Project 2) | Both converge; you can state what a 15x learning rate does and show it | A2 / Stage 1 | 3 |
| C3 | Frame, train, evaluate and error-analyse a tabular model | Project 3 notebook | Baseline stated, cross-validated comparison, metric justified, 30 worst cases categorised, one fix measured, leakage note per feature | A3 / Stage 1 | 12, 13 |
| C4 | Implement a tokenizer | Lab 05 plus your own BPE on a text of your choice | Round trip is lossless; you show sequence length falling as merges rise | A4 / Stage 2 | 2 |
| C5 | Implement causal attention and a GPT block | Lab 02 plus your re-typed GPT (Project 4) | Causality and scaling checks pass; your model trains and samples text | A4 / Stage 2 | 1, 4 |
| C6 | Implement a KV cache and measure it | Lab 03 plus Project 6 in your own model | Outputs identical with and without cache; speedup and cache size reported | A4 / Stage 2 | 5 |
| C7 | Pretrain, post-train and evaluate a small LLM | Labs 07, 08, 09 run and explained, then Project 5 write-up (nanochat run, SFT, GRPO) | Eval numbers at each stage; one thing that broke documented; cost stated; you can say why RL degraded something and what the KL term does | A4 / Stage 2 | 1, 7, 8 |
| C8 | Run a controlled ablation | Project 7 | One variable, three settings, one plot, one paragraph a stranger can check | Stage 2 / Track C | 13 |
| C9 | Build retrieval with a measured golden set | Project 8 | 50+ versioned questions; recall@k before and after one change; permissions enforced in the retrieval layer | A5 / Stage 3 | 9, 11 |
| C10 | Build an eval harness with calibrated graders | Labs 04, 10, 11, 13 plus Project 9's harness | Code graders where a rule exists; any LLM judge reports TPR and TNR against 100+ human labels; pass@k and pass^k reported; suite runs in CI | A5 / Stage 3 | 12, 14, 15 |
| C11 | Ship to real users and iterate | Projects 8 and 9 user logs | At least five users for two weeks; a changelog of what they broke and what you changed | A5 / Stage 3 | 19 |
| C12 | Cut cost with numbers | Project 10 | Cost per request halved; eval unchanged within measured noise; levers named | Stage 3 / Track A | 17 |
| C13 | Defend a design decision with measurements | Project 9 (part 2) post | A decision you reversed, the numbers that drove it, published | A5 / Stage 3 | 12 |
| C14 | Review AI-generated code | Any PR in your repos | You can point to a bug the assistant introduced and explain the fix | A1 / Stage 1 | 20 |
| C15 | Explain serving memory and the roofline | Labs 06 and 12 plus the Module 05 mastery gate | You compute weights plus KV cache for a given model, context and batch, by hand, and say whether a given decode batch is bandwidth- or compute-bound | Stage 2 / Track B | 6, 18 |

## Getting hired

| # | Capability | Evidence artifact | Passes when | Module |
|---|---|---|---|---|
| H1 | A public record someone can refer you on | Blog with 3+ posts, one runnable repo, one talk | A person outside your company has cited or starred it | A6 / Stage 4 |
| H2 | An internal AI project pitched and delivered | Pitch doc plus results | Pitched with a dollar cost; delivered with eval numbers and failure cases | Stage 4 |
| H3 | ML system design under time | Ten prompts drawn and timed | A reviewer agrees each covers ingestion, retrieval, generation, evals, monitoring and cost | A6 / Stage 4 |
| H4 | Interview-grade depth on your own work | Mock interview recording | You answer "why" five levels deep on one project for 20 minutes without running out | A6 / Stage 4 |

## Track depth (one track)

| Track | Capability | Evidence artifact | Passes when |
|---|---|---|---|
| A | Own the eval and observability stack for a production agent | Dashboard of pass rate over time across model versions; a prompt-injection red-team with fixes | A model upgrade is a config change plus an eval run; the trifecta is broken in code |
| B | Profile-driven kernel or serving optimisation | FlashAttention2 in Triton with a fair baseline; a Nsight-backed before/after on a named bottleneck; a benchmark table with engine version, hardware, TTFT, TPOT, p99, VRAM and quality | Speedup survives a hidden test distribution and a library baseline |
| C | A replication plus ablation with negative results | Paper-style write-up with limitations; from-scratch GRPO notebook with a results table | Someone outside your circle has reviewed it; it would be accepted as a LessWrong or workshop-grade post |
| All | One merged upstream contribution | PR link | Merged, and you reviewed every line yourself |

## Expert markers

| Marker | Evidence |
|---|---|
| You own a problem end to end | Your manager states your impact in one sentence |
| People outside your company know your work | A repo, write-up, talk or paper cited by strangers |
| You go arbitrarily deep under questioning | A recorded talk on one topic in your track (the capstone defence) in which questioning goes five levels deep |
| You learn on a cadence | Evals re-run and a note written on each model release; one long study per year, published |

## How to use this file

Keep it as a checklist. For each row, link the artifact. A row with no link is not done, regardless of how much you read.
