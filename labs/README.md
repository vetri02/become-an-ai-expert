# Set up the lab

Do this before Module 01. About two hours. Everything runs on a laptop; no GPU.

## Get the code

Everything you run in this course, the thirteen labs, the three targets with their graders, the templates and the tutor skill, is public on GitHub at [github.com/vetri02/become-an-ai-expert](https://github.com/vetri02/become-an-ai-expert). Clone it:

```
git clone https://github.com/vetri02/become-an-ai-expert.git
```

or download it as a zip, [become-an-ai-expert.zip](https://github.com/vetri02/become-an-ai-expert) (about 2.5 MB), and unzip it anywhere. Either way the folder is `become-an-ai-expert`, and every command in the course runs from inside that folder. You need Python 3.10 or newer and nothing else; the first run installs NumPy into a virtual environment inside `labs/`.

## Quick start

```
cd become-an-ai-expert/labs
./run_all.sh
```

The script creates a virtual environment with NumPy on first run and executes all thirteen labs. Every lab prints the measurement that backs one first principle and fails loudly if it does not hold. Expect `PASS` thirteen times. If any fails, your environment is wrong; fix that before anything else.

## What is in the lab

| Lab | Principle | Module |
|---|---|---|
| 01 gradient descent by hand | 3 | 02 |
| 02 causal attention with scaling checks | 4 | 04 |
| 03 the KV cache, identical outputs, measured speedup | 5 | 05 |
| 04 eval harness: recall@k, code grader, judge calibration, pass@k vs pass^k | 11, 13, 14, 15 | 08 |
| 05 BPE tokenizer from scratch | 2 | 03 |
| 06 serving memory math | 6 | 05, Track B |
| 07 next-token distribution and sampling | 1 | 03 |
| 08 loss as a power law in data | 7 | 05 |
| 09 RL reward hacking and the KL leash | 8 | 06 |
| 10 attention dilution and request cost | 9, 17 | 07, 10 |
| 11 prompt injection defeated in code | 16 | 10 |
| 12 roofline and a measured batch effect | 18 | Track B |
| 13 model-upgrade noise versus regression | 19 | 08, 17 |

## The targets

Three planted-bug programs in `targets/`. Each prints flags as you fix it. They are used after Modules 05, 08 and 10. Run them only when the module says to; the first run is meant to fail.

## Accounts and keys

None of these is needed today. Set each one up when you reach the module named.

- One LLM API key (any major provider) for Modules 07 to 11. Set it as an environment variable; never commit it. About $50 to $150 over the course.
- A free Weights & Biases account for Module 05 and 06 logging.
- A GPU rental account for Module 05 (nanochat). See the compute appendix for free tiers and prices. About $50 to $200 over the course, most of it in Module 05.
- A GitHub account with a free GitHub Pages blog. Every module ends with something public.

## What is NOT in the lab

The labs run on NumPy alone, so each principle is visible without a GPU, a hosted model or a vector database. The projects in each module use real tools; the modules name them.

## Test evidence

The verification report page is regenerated on each build with the lab results, the target checks and the citation check. If what you see on your machine differs from it, open an issue in your own fork and record it; disagreement with the report is itself evidence of something.
