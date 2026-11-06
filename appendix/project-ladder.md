# The project ladder

Every project in the course, in order, with what it teaches, a time estimate, and the "done when" bar. Both tracks climb the same ladder; the Module column says where each rung is built, with the Novice page in parentheses. Project numbers are the ones the modules use.

The ladder follows the practitioners' order: a tiny model from scratch (Raschka: "implementing a simple model from scratch that you can run on your computer"), then reproduce end-to-end projects yourself (Boykis), then ship something a friend uses (Huyen), then an LLM app where you do error analysis by hand (Husain), then projects that "break in interesting ways" with evals, tracing and deployment.

| # | Project | Module | Teaches | Time | Done when |
|---|---|---|---|---|---|
| 1 | Deployed Python service with tests and Docker | 01 (A1) | Software fundamentals, deployment, reading tracebacks | 20 to 35h | A stranger can clone, test and hit the live URL |
| 2 | Gradient descent from memory in NumPy | 02 (A2) | What training is | 4 to 6h | Both fits converge; you can draw it on paper |
| 3 | Tabular project with cross-validation and error analysis | 02 (A3) | Framing, leakage, metrics, looking at your data | 15 to 25h | You can say with numbers why it beats the baseline and where it fails |
| 4a | Your own tokenizer and n-gram model | 03 (A4) | Tokens, the next-token objective | 6 to 10h | Lossless round trip; the vocabulary trade-off table |
| 4b | Your GPT, retyped from memory, trained and sampling | 04 (A4) | The Transformer | 15 to 20h | It trains and samples; the forward pass whiteboarded with shapes |
| 5a | nanochat run with eval table and one measured change | 05 (A4) | Pretraining, scaling laws, cost | 20 to 40h plus $20 to $75 compute | Eval numbers, loss curve, cost line, written up with what broke |
| 6 | KV cache in your GPT with speedup numbers | 05 (A4) | Inference, memory | 6 to 10h | Identical outputs proved; before/after timing in the README |
| 5b | SFT and GRPO on your model with separate eval columns | 06 (A4) | Post-training | 15 to 25h plus compute | Capability and general-ability columns per stage, and what the KL coefficient did |
| 7 | One ablation (one variable, three settings, one plot) | 06 (A4; Track C) | Experimental method | 6 to 10h | A plot and a paragraph someone else can check |
| 8 | Retrieval over a messy corpus with a 50-question golden set | 07 (A5) | Retrieval, evals, permissions, cost | 30 to 50h | recall@k before/after one change; five real users for two weeks |
| 9 | The harness (part 1), the agent (part 2), the red-team suite (part 3) | 08, 09, 10 (A5) | Evals, agents, context engineering, security | 40 to 60h | pass@3 and pass^3 reported; unfixed failures documented; the suite in CI |
| 10 | A cost cut with numbers | 10 (A5) | Caching, routing, token budgets | 8 to 15h | Cost per request halved without hurting the eval |
| 11 | Fine-tune versus not: three variants and a decision record | 11 (A5) | When fine-tuning wins | 10 to 15h plus under $20 | Quality, cost and latency for each variant; the decision follows the numbers |
| 12 | The pilot: pitch, delivery, results memo | 12 (A6) | The internal move | 20 to 40h | Eval numbers, cost and failure cases in the memo |
| 13 | The public record: three posts, a finished README, a talk, one PR opened | 12 (A6) | Being known | 15 to 25h | A stranger has starred, cited or commented |
| 14 | The application kit: portfolio page, numbered resume, timed design prompts | 13 (A6) | Getting hired | 10 to 15h | Three referral conversations, one interview |
| 15 | Track artifact (A: agent in production with a dashboard; B: Triton kernel with a fair speedup; C: replication plus ablation) plus one merged upstream PR | 14, 15 or 16 (A7) | Depth | 24h guided, then months | As the track module defines it; the PR is merged |
| 16 | The yearly plan | 17 (A8) | Staying current | 2 to 4h | Names an artifact and a date a stranger can check |

## Project ideas that are not "chat with your PDF"

From the research, projects that practitioners say teach something and "break in interesting ways":

- Document Q&A with citations and an eval set over a corpus people actually ask questions about (a club's rules, a product's manuals, a city's council minutes)
- A support-ticket triage workflow with tools and structured outputs, graded on routing accuracy
- A receipt or invoice parser with validation and a measured error rate per field
- A small agent that plans, acts, checks and retries within a token and dollar budget, with the budget enforced in code
- Churn or fraud prediction on real business-shaped data, which forces class imbalance and a cost-weighted metric
- Anything with time in it (stock prices, sensor data), which forces you to learn temporal leakage the hard way
- Something from your own frustration log that a friend will use

## What makes a project read as finished

Reviewers of 2026 portfolios converge on this. A project with none of it "reads as unfinished."

- One-line result with a number at the top of the README
- An eval table against a baseline, on a described and versioned test set
- p50 and p95 latency and cost per request
- A "where this breaks" section with real failure cases
- Decisions you reversed and the measurements that drove them
- A live URL or a one-command run. An un-runnable project reads as broken.
- Clear statement of what is yours if it builds on something else. Do not post course exercises as projects.

## Sources

- Raschka on starting from scratch (Lex #490, Feb 2026): https://lexfridman.com/ai-sota-2026-transcript
- Boykis on reproducing projects: https://vickiboykis.com/2026/10/17/how-to-learn-ml-in-2026-interview/
- Huyen on end-to-end and frustration logs: https://www.aol.com/articles/want-upskill-ai-former-nvidia-171247423.html
- Husain and Shankar on error analysis: https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill
- Projects that break in interesting ways (Bouchard; funnels to paid courses): https://github.com/louisfb01/start-ai-engineering
- Time estimates (Dataquest, vendor, Mar 2026): https://www.dataquest.io/blog/machine-learning-projects-for-beginners-to-advanced/
- README expectations (Lange, MATS reviewer): https://georglange.com/post/ai-safety-application-guide/
- "One documented project beats five demos": https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/odzfxx9/
- What impresses recruiters in 2026: https://www.reddit.com/r/MachineLearningJobs/comments/1u032xt/
