# Compute and costs

You do not need a GPU laptop. fast.ai's official line: "You don't need any special hardware or software." Classical ML runs on any CPU. Prioritise RAM over GPU if buying a laptop. Rent a GPU by the hour only when a specific project needs one.

Prices below were checked in the first week of November 2026 and move monthly. Treat them as a planning range and re-check at signup.

## Free tier, enough for the first 6 to 12 months

| Service | What you get | Notes |
|---|---|---|
| Google Colab (free) | T4-class GPU, up to 12h sessions | Limits are unpublished and fluctuate. Fine for Zero to Hero, Raschka's book, smol-course. |
| Kaggle Notebooks | About 30 GPU-hours a week (dynamic), T4x2 or P100, 12h sessions | No credit card. Check your account page for the current quota. |
| Modal (Starter) | $30 a month in free credits, no base fee | Per-second billing. Enough for several fine-tuning runs a month. |
| Lightning AI (Free) | One-time credits worth about 50 interruptible GPU-hours, plus a free CPU workspace | Changed in September 2026 from monthly to one-time. Older guides are wrong. |

Rule: Colab free plus Kaggle plus Modal's $30 covers everything in Path A modules 1 to 4 except the nanochat run. Pay only when a project needs more than a T4 for more than about 12 hours.

## Paid, per GPU-hour (early November 2026)

| Provider | T4 | L4 | RTX 4090 | A100 | H100 | 8xH100 node |
|---|---|---|---|---|---|---|
| Modal | $0.59 | $0.80 | | $2.50 (80GB) | $3.95 | ~$31.60 |
| RunPod Community | | $0.44 | $0.34 | $1.19 (PCIe) | $1.99 PCIe / $2.69 SXM | ~$21.50 |
| Vast.ai marketplace | | | ~$0.36 | | ~$1.73 to $2.14 | varies; interruptible 50%+ cheaper |
| Lambda (from 16 Nov 2026) | | | | $1.99 (40GB) | $4.29 | $31.92 |
| Lightning AI | $0.55 | $0.79 | | $2.19 (40GB) | $5.45 | |
| Colab Pro | $9.99/month for 100 compute units (a T4 burns about 1.76 units an hour) | | | | | |

## What the course's projects cost

| Project | Hardware | Cost |
|---|---|---|
| Zero to Hero, Raschka book 1, smol-course, ARENA chapters | Free Colab / Kaggle | $0 |
| Tabular project, RAG project, agent project | Laptop CPU plus API calls | $5 to $30 in API usage |
| nanochat GPT-2-grade speedrun | 8xH100, about 2 to 3 hours | $48 on demand per the README; about $15 on spot; Karpathy quoted about $73 for a 3h run in Jan 2026 |
| nanochat larger tiers (optional) | 8xH100, 12 to 33 hours | $300 to $800 |
| SFT and GRPO on your nanochat model | 1 to 8 GPUs, a few hours | $10 to $50 |
| LoRA fine-tune of a 7B to 8B model | One A100 or RTX 4090, 2 to 4 hours | $3 to $10 |
| GRPO on a 1.5B to 4B model with LoRA | One 48GB GPU, several hours | $10 to $40 |
| KV-cache and kernel benchmarks | One GPU, hours | $5 to $20 |

A realistic whole-course budget is $100 to $300 of GPU time plus $50 to $150 of API calls over the course and the first year after it. The Redditor who trained three LLMs from scratch spent about $750; that is the upper end.

## Spot and interruptible instances

Spot pricing cuts cost by half or more but the machine can be taken away. Checkpoint every 10 to 15 minutes and write a resume script before you start. nanochat supports resuming.

## Use other people's money

- Ask your employer for a learning budget tied to a pilot project (median learning spend per employee fell to about $299 in 2026, so ask early and be specific).
- Hugging Face, Modal and most clouds run periodic credit programs for open-source and student work.
- MATS pays about $2,000 a week in compute to fellows.

## Sources

- fast.ai hardware guidance: https://course.fast.ai/
- Colab FAQ: https://research.google.com/colaboratory/faq.html
- Modal pricing: https://modal.com/pricing
- RunPod pricing (updated 2026-11-04): https://www.runpod.io/pricing
- Vast.ai pricing: https://vast.ai/pricing
- Lambda pricing: https://lambda.com/service/gpu-cloud
- Lightning AI pricing: https://lightning.ai/pricing
- Colab alternatives comparison (vendor, 2026-10-09): https://www.thundercompute.com/blog/google-colab-alternatives
- nanochat README: https://github.com/karpathy/nanochat
- Karpathy on nanochat cost, Jan 2026: https://x.com/karpathy/status/2017703360393318587
- LoRA cost ranges (vendor, July 2026): https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026
- SHRM 2026 L&D benchmarking: https://www.shrm.org/in/topics-tools/research/2026-ld-executives-benchmarking--developing-critical-talent/full-report
