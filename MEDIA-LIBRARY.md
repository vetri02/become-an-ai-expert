# Curated media library

Course version 2.0. Every recording was checked on 2026-11-05 by fetching its page and reading the title, channel and length from the page metadata. No recording was watched in full. Playlists were verified by page title.

## How to use the library

- Core recordings play on their module page under "Watch first" and can replace part of the module's concept-reading block. Recommended and optional items are enrichment.
- Several speakers sell a course, a book or a product; those entries say so in their "why" line. The mechanism they explain is what matters; verify any numbers against primary sources.
- Do not treat a recording as evidence about a current product or price; the modules carry the dated claims.

## A short starting path

1. V13 for the one-hour map, before Module 03.
2. V15 and V16 for attention, alongside Module 04.
3. V17 and V18 with Modules 04 and 05: build GPT, then reproduce GPT-2.
4. V26 and V27 for evals, alongside Module 08.
5. V31 for injection, alongside Module 10.
6. V34 before Module 12.

## Videos

### V01

**[Essence of linear algebra (playlist, 16 videos)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)**

- Creator/source: 3Blue1Brown.
- Published: 2016. Duration: about 180 min.
- Use: core. Modules: 02.

**Why it belongs:** Builds the geometric intuition for vectors, matrices and dot products that every attention and embedding diagram assumes.

**Do this after watching:** After each video, write one sentence on where that idea shows up in an LLM (for example, dot product = similarity score).

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V02

**[Essence of calculus (playlist, 12 videos)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)**

- Creator/source: 3Blue1Brown.
- Published: 2017. Duration: about 180 min.
- Use: optional. Modules: 02.

**Why it belongs:** Gives just enough derivative and chain-rule intuition to understand backpropagation.

**Do this after watching:** Watch chapters 1 to 4 and 6 only; sketch the chain rule for f(g(x)) by hand before V07.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V03

**[But what is a neural network? (Deep learning chapter 1)](https://www.youtube.com/watch?v=aircAruvnKk)**

- Creator/source: 3Blue1Brown.
- Published: 2017. Duration: about 19 min.
- Use: core. Modules: 02.

**Why it belongs:** The clearest visual explanation of layers, weights, biases and activations.

**Do this after watching:** Draw a 2-layer network for a 3-pixel input and count its parameters.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V04

**[Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA)**

- Creator/source: StatQuest with Josh Starmer.
- Published: 2018. Duration: about 7 min.
- Use: core. Modules: 02.

**Why it belongs:** Explains overfitting versus underfitting, the lens for reading every training and validation loss curve.

**Do this after watching:** Explain in two sentences why a train/validation gap matters when you fine-tune.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V05

**[Machine Learning Fundamentals: The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o)**

- Creator/source: StatQuest with Josh Starmer.
- Published: 2018. Duration: about 7 min.
- Use: core. Modules: 02.

**Why it belongs:** Defines TP, FP, TN and FN, the vocabulary behind precision and recall in evals.

**Do this after watching:** Build a confusion matrix for a toy spam classifier with 10 examples.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V06

**[ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM)**

- Creator/source: StatQuest with Josh Starmer.
- Published: 2019. Duration: about 16 min.
- Use: core. Modules: 02, 08.

**Why it belongs:** Shows how thresholds trade off false positives and negatives, which is how you tune LLM-judge cutoffs.

**Do this after watching:** Compute precision and recall at two thresholds for your V05 toy example.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V07

**[The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0)**

- Creator/source: Andrej Karpathy.
- Published: 2022. Duration: about 146 min.
- Use: core. Modules: 02.

**Why it belongs:** Implements autograd from scratch in about 100 lines of Python, so backprop stops being magic.

**Do this after watching:** Code along; then add a ReLU op and verify gradients numerically.

**Slides or code:** https://karpathy.ai/zero-to-hero.html

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V08

**[The spelled-out intro to language modeling: building makemore](https://www.youtube.com/watch?v=PaCmpygFfXo)**

- Creator/source: Andrej Karpathy.
- Published: 2022. Duration: about 118 min.
- Use: core. Modules: 03.

**Why it belongs:** Introduces the next-character objective, bigram counts and negative log-likelihood, the core of all LLM training.

**Do this after watching:** Code along; train the bigram model on your own list of words and sample from it.

**Slides or code:** https://karpathy.ai/zero-to-hero.html

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V09

**[Building makemore Part 2: MLP](https://www.youtube.com/watch?v=TCH_1BHY58I)**

- Creator/source: Andrej Karpathy.
- Published: 2022. Duration: about 76 min.
- Use: core. Modules: 03.

**Why it belongs:** Adds embeddings, a hidden layer, mini-batches and the train/dev/test split.

**Do this after watching:** Plot loss versus learning rate as in the video and pick a learning rate yourself.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V10

**[Building makemore Part 3: Activations and Gradients, BatchNorm](https://www.youtube.com/watch?v=P6sfmUTpUmc)**

- Creator/source: Andrej Karpathy.
- Published: 2022. Duration: about 116 min.
- Use: optional. Modules: 04.

**Why it belongs:** Covers activation and gradient health in deep networks.

**Do this after watching:** Reproduce the activation histograms and explain what a dead neuron is.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V11

**[Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)**

- Creator/source: Andrej Karpathy.
- Published: 2024. Duration: about 134 min.
- Use: core. Modules: 03.

**Why it belongs:** Builds byte-pair encoding from scratch and explains why tokenization causes many LLM quirks.

**Do this after watching:** Train a BPE tokenizer on a text of your choice; tokenize a URL, some code and non-English text and inspect the results.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V12

**[CS336 Spring 2025, Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI)**

- Creator/source: Stanford Online (Percy Liang).
- Published: 2025. Duration: about 79 min.
- Use: core. Modules: 03.

**Why it belongs:** Frames the whole build-an-LM-from-scratch stack (data, systems, scaling, alignment) and formalises BPE.

**Do this after watching:** Write a one-page map of the LLM pipeline using the lecture's outline.

**Slides or code:** https://cs336.stanford.edu/spring2025/

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V13

**[[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)**

- Creator/source: Andrej Karpathy.
- Published: 2023. Duration: about 60 min.
- Use: core. Modules: 03.

**Why it belongs:** Non-technical but precise tour: pretraining, fine-tuning, RLHF, scaling, tool use and security.

**Do this after watching:** Watch first in the course; list three questions you want answered by the end.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V14

**[Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI)**

- Creator/source: Andrej Karpathy.
- Published: 2025. Duration: about 211 min.
- Use: core. Modules: 06.

**Why it belongs:** End-to-end explanation of pretraining, SFT, RLHF and reasoning RL with concrete examples of hallucination and tokenization effects.

**Do this after watching:** Watch in three sittings; after each, write a five-bullet summary you could give a colleague.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V15

**[Transformers, the tech behind LLMs (Deep Learning chapter 5)](https://www.youtube.com/watch?v=wjZofJX0v4M)**

- Creator/source: 3Blue1Brown.
- Published: 2024. Duration: about 27 min.
- Use: core. Modules: 04.

**Why it belongs:** Visualises embeddings, the residual stream, the unembedding and softmax with temperature.

**Do this after watching:** Explain temperature in one paragraph using the video's softmax picture.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V16

**[Attention in transformers, step-by-step (Deep Learning chapter 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc)**

- Creator/source: 3Blue1Brown.
- Published: 2024. Duration: about 26 min.
- Use: core. Modules: 04.

**Why it belongs:** The best visual derivation of queries, keys, values, masking and multi-head attention.

**Do this after watching:** Hand-compute attention weights for a 3-token example with 2-dimensional Q and K.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V17

**[Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY)**

- Creator/source: Andrej Karpathy.
- Published: 2023. Duration: about 116 min.
- Use: core. Modules: 04.

**Why it belongs:** Implements a decoder-only transformer (nanoGPT) line by line, including causal self-attention.

**Do this after watching:** Code along; then change context length and head count and observe loss and speed.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V18

**[Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)**

- Creator/source: Andrej Karpathy.
- Published: 2024. Duration: about 241 min.
- Use: core. Modules: 05.

**Why it belongs:** Full pretraining run with mixed precision, torch.compile, flash attention, learning-rate schedules and evaluation.

**Do this after watching:** Watch fully; run at least the first hour's code on any GPU and record tokens per second before and after each optimisation.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V19

**[CS336 Spring 2025, Lecture 9: Scaling laws 1](https://www.youtube.com/watch?v=6Q-ESEmDf4Q)**

- Creator/source: Stanford Online (Tatsunori Hashimoto).
- Published: 2025. Duration: about 65 min.
- Use: core. Modules: 05.

**Why it belongs:** Explains Chinchilla-style compute-optimal training and how labs decide model versus data size.

**Do this after watching:** Given a fixed compute budget, estimate parameters and tokens using the lecture's rule of thumb.

**Slides or code:** https://github.com/stanford-cs336/spring2025-lectures/blob/fb79eb018fa047bf99c4c785dcbbd62fff361e54/nonexecutable/2025%20Lecture%209%20-%20Scaling%20laws%20basics.pdf

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V20

**[CS336 Spring 2025, Lecture 10: Inference](https://www.youtube.com/watch?v=fcgPYo3OtV0)**

- Creator/source: Stanford Online (Percy Liang).
- Published: 2025. Duration: about 83 min.
- Use: core. Modules: 05.

**Why it belongs:** Derives why decoding is memory-bound, and covers the KV cache, batching, speculative decoding and quantisation.

**Do this after watching:** Compute the KV-cache size in GB for a given model and context length, then explain why batch size raises throughput.

**Slides or code:** https://cs336.stanford.edu/spring2025/

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V21

**[CS336 Spring 2025, Lecture 15: Alignment, SFT and RLHF](https://www.youtube.com/watch?v=Dfu7vC9jo4w)**

- Creator/source: Stanford Online (Tatsunori Hashimoto).
- Published: 2025. Duration: about 75 min.
- Use: core. Modules: 06.

**Why it belongs:** Covers instruction-tuning data, reward models, PPO and DPO in one lecture.

**Do this after watching:** Write the DPO objective in words and explain what it removes relative to PPO.

**Slides or code:** https://github.com/stanford-cs336/spring2025-lectures/blob/61eddac004df975466cff0329b615f2d24230069/nonexecutable/2025%20Lecture%2015%20-%20RLHF%20Alignment.pdf

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V22

**[CS336 Spring 2025, Lecture 16: Alignment, RL 1 (RLVR)](https://www.youtube.com/watch?v=46f2QTDB08Q)**

- Creator/source: Stanford Online (Tatsunori Hashimoto).
- Published: 2025. Duration: about 81 min.
- Use: core. Modules: 06.

**Why it belongs:** Explains reinforcement learning with verifiable rewards, policy gradients and GRPO as used in reasoning models.

**Do this after watching:** List two tasks in your domain with verifiable rewards and two without.

**Slides or code:** https://github.com/stanford-cs336/spring2025-lectures/blob/e94e33f433985e57036b25215dff2a4292e67a4f/nonexecutable/2025%20Lecture%2016%20-%20RLVR.pdf

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V23

**[Build A Reasoning Model From Scratch 6: Implementing GRPO for RLVR](https://www.youtube.com/watch?v=237Hf7Q3lgg)**

- Creator/source: Sebastian Raschka.
- Published: 2026. Duration: about 87 min.
- Use: core. Modules: 06, 16.

**Why it belongs:** Hands-on GRPO implementation in PyTorch with a math-answer verifier as the reward.

**Do this after watching:** Run the companion code; change the group size and note the effect on reward variance.

**Slides or code:** https://github.com/rasbt/reasoning-from-scratch

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V24

**[The unreasonable effectiveness of BM25 for agentic search](https://www.youtube.com/watch?v=fZH97QHHYjY)**

- Creator/source: AI Engineer (Jo Kristian Bergum).
- Published: 2026. Duration: about 18 min.
- Use: core. Modules: 07.

**Why it belongs:** Shows with real search traces why lexical retrieval and hybrid search matter when the user is an agent. Speaker is a vendor CEO; content is conceptual.

**Do this after watching:** Add a BM25 index next to your vector index and compare top-5 results on 10 queries.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V25

**[How to look at your data (Jeff Huber and Jason Liu)](https://www.youtube.com/watch?v=jryZvCuA0Uc)**

- Creator/source: AI Engineer.
- Published: 2025. Duration: about 19 min.
- Use: core. Modules: 07, 08.

**Why it belongs:** Practical method for improving RAG by inspecting retrieval inputs and outputs and measuring per-query-type failures.

**Do this after watching:** Sample 30 queries, cluster them by type, and estimate recall per cluster.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V26

**[Why AI evals are the hottest new skill for product builders](https://www.youtube.com/watch?v=BsWxPI9UM4c)**

- Creator/source: Lenny's Podcast (Hamel Husain, Shreya Shankar).
- Published: 2025. Duration: about 107 min.
- Use: core. Modules: 08.

**Why it belongs:** The full error-analysis-first eval workflow: open coding, taxonomies, code versus LLM-judge evals, judge validation. Promotes their paid course.

**Do this after watching:** Do a one-hour error analysis on 20 traces of any LLM app and write a failure taxonomy.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V27

**[LLM Evals: Common Mistakes](https://www.youtube.com/watch?v=GL0XhAj5LPE)**

- Creator/source: Hamel Husain.
- Published: 2025. Duration: about 28 min.
- Use: core. Modules: 08.

**Why it belongs:** Short list of anti-patterns: generic metrics, unvalidated judges, no error analysis.

**Do this after watching:** Audit an existing eval setup against the mistakes listed.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V28

**[Evals in Action: From Frontier Research to Production Applications](https://www.youtube.com/watch?v=YEaKXjHENyQ)**

- Creator/source: OpenAI (Tejal Patwardhan, Henry Scott-Green).
- Published: 2025. Duration: about 22 min.
- Use: optional. Modules: 08.

**Why it belongs:** How a frontier lab thinks about evals, then how app builders should. The second half demos a vendor product.

**Do this after watching:** Note the three grader types mentioned and map them to your own use case.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V29

**[How We Build Effective Agents (Barry Zhang, Anthropic)](https://www.youtube.com/watch?v=D7_ipDqhtwk)**

- Creator/source: AI Engineer.
- Published: 2025. Duration: about 15 min.
- Use: core. Modules: 09.

**Why it belongs:** Distils the building-effective-agents post: workflows versus agents, keep it simple, think from the model's point of view.

**Do this after watching:** Decide for one of your use cases whether it needs a workflow or an agent, and justify it.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V30

**[Prompting 101](https://www.youtube.com/watch?v=ysPbXH0LpIE)**

- Creator/source: Anthropic (Code with Claude).
- Published: 2025. Duration: about 25 min.
- Use: optional. Modules: 09.

**Why it belongs:** Structured prompt anatomy with a live worked example. Vendor talk; the structure transfers.

**Do this after watching:** Rewrite one of your prompts using the template and A/B it on 10 inputs.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V31

**[Prompt Injection, explained](https://www.youtube.com/watch?v=FgxwCaL6UTA)**

- Creator/source: Simon Willison.
- Published: 2023. Duration: about 12 min.
- Use: core. Modules: 10.

**Why it belongs:** The canonical explanation of why untrusted text in the context is a security problem with no complete fix.

**Do this after watching:** List every untrusted input your app puts into a prompt and what a worst-case injection could do.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V32

**[Mastering LLM Inference Optimization: From Theory to Cost-Effective Deployment (Mark Moyou)](https://www.youtube.com/watch?v=9tvJ_GYJA-o)**

- Creator/source: AI Engineer.
- Published: 2025. Duration: about 34 min.
- Use: optional. Modules: 10, 15.

**Why it belongs:** Connects model size, precision, KV cache and batching to dollars per token and latency targets. Speaker is at NVIDIA; content is largely vendor-neutral.

**Do this after watching:** Estimate cost per million tokens for one model on one GPU using the talk's arithmetic.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V33

**[Build an LLM from Scratch 7: Instruction Finetuning](https://www.youtube.com/watch?v=4yNswvhPWCQ)**

- Creator/source: Sebastian Raschka.
- Published: 2025. Duration: about 106 min.
- Use: core. Modules: 11.

**Why it belongs:** Full SFT loop on a small GPT: formatting instruction data, masking, training and evaluating with an LLM judge.

**Do this after watching:** Run the chapter notebook; swap in 50 instruction examples from your domain.

**Slides or code:** https://github.com/rasbt/LLMs-from-scratch

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V34

**[From Software Engineer to AI Engineer, with Janvi Kalra](https://www.youtube.com/watch?v=3E_jDJST69s)**

- Creator/source: The Pragmatic Engineer (Gergely Orosz).
- Published: 2025. Duration: about 70 min.
- Use: core. Modules: 12, 13.

**Why it belongs:** An OpenAI AI engineer on moving from software engineering to AI, what interviews looked like, and what the job is.

**Do this after watching:** Write your own six-month transition plan with the projects you would show in interviews.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V35

**[AI Engineering 101 with Chip Huyen](https://www.youtube.com/watch?v=qbvY0dQgSJ4)**

- Creator/source: Lenny's Podcast.
- Published: 2025. Duration: about 83 min.
- Use: core. Modules: 14.

**Why it belongs:** The author of AI Engineering on the applied stack: RAG versus fine-tuning, evaluation-driven development, failure modes. Promotes her book.

**Do this after watching:** List which of the techniques discussed your organisation needs, in priority order.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V36

**[Keynote: Build and keep your context window (PyData Amsterdam 2023)](https://www.youtube.com/watch?v=icGHT7MiaFY)**

- Creator/source: PyData (Vicki Boykis).
- Published: 2023. Duration: about 38 min.
- Use: optional. Modules: 17.

**Why it belongs:** A practitioner's view on learning ML deeply amid hype: fundamentals, writing, and managing your own attention.

**Do this after watching:** Pick one fundamental topic to go deep on this month and schedule it.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V37

**[Lecture 1: How to profile CUDA kernels in PyTorch](https://www.youtube.com/watch?v=LuhJEEJQgUM)**

- Creator/source: GPU MODE (Mark Saroufim).
- Published: 2024. Duration: about 56 min.
- Use: core. Modules: 15.

**Why it belongs:** Shows how to time and profile PyTorch ops and load a custom CUDA kernel.

**Do this after watching:** Profile a matmul and a softmax with the PyTorch profiler and identify the slowest kernel.

**Slides or code:** https://github.com/gpu-mode/lectures/tree/main/lecture_001

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V38

**[Lecture 2: Chapters 1 to 3 of PMPP](https://www.youtube.com/watch?v=NQ-0D5Ti2dc)**

- Creator/source: GPU MODE (Andreas Koepf).
- Published: 2024. Duration: about 52 min.
- Use: optional. Modules: 15.

**Why it belongs:** Recap of the first three chapters of Programming Massively Parallel Processors: threads, blocks, grids.

**Do this after watching:** Sketch how a 1024-element vector add maps to blocks and threads.

**Slides or code:** https://github.com/gpu-mode/lectures

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V39

**[Lecture 3: Getting Started With CUDA for Python Programmers](https://www.youtube.com/watch?v=4sgKnKbR-WE)**

- Creator/source: GPU MODE (Jeremy Howard).
- Published: 2024. Duration: about 78 min.
- Use: core. Modules: 15.

**Why it belongs:** Writes a first CUDA kernel from a Python mindset: simulate in Python, then port.

**Do this after watching:** Follow along and write an RGB-to-grayscale kernel, then a matmul kernel.

**Slides or code:** https://github.com/gpu-mode/lectures

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V40

**[Lecture 4: Compute and Memory Basics](https://www.youtube.com/watch?v=lTmYrKwjSOU)**

- Creator/source: GPU MODE (Thomas Viehmann).
- Published: 2024. Duration: about 57 min.
- Use: core. Modules: 15.

**Why it belongs:** Explains the GPU memory hierarchy, occupancy and why memory bandwidth bounds most LLM kernels.

**Do this after watching:** Compute arithmetic intensity for a matmul versus an elementwise op and say which is memory-bound.

**Slides or code:** https://github.com/gpu-mode/lectures/tree/main/lecture_004

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V41

**[CS336 Spring 2025, Lecture 5: GPUs](https://www.youtube.com/watch?v=6OBtO9niT00)**

- Creator/source: Stanford Online (Tatsunori Hashimoto).
- Published: 2025. Duration: about 74 min.
- Use: core. Modules: 05, 15.

**Why it belongs:** Roofline model, tensor cores, FLOPs accounting, and why training is compute-bound and inference memory-bound.

**Do this after watching:** Estimate MFU for a training run given tokens per second, parameters and GPU peak FLOPs.

**Slides or code:** https://github.com/stanford-cs336/spring2025-lectures/blob/main/nonexecutable/2025%20Lecture%205%20-%20GPUs.pdf

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V42

**[Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U)**

- Creator/source: Anyscale (Woosuk Kwon, Zhuohan Li).
- Published: 2023. Duration: about 32 min.
- Use: core. Modules: 15.

**Why it belongs:** The vLLM authors explain KV-cache fragmentation and how paged attention raises serving throughput.

**Do this after watching:** Explain paged attention to a colleague using the OS virtual-memory analogy.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V43

**[Lecture 22: Hacker's Guide to Speculative Decoding in vLLM](https://www.youtube.com/watch?v=9wNAgpX6z_4)**

- Creator/source: GPU MODE (Cade Daniel).
- Published: 2024. Duration: about 69 min.
- Use: core. Modules: 15.

**Why it belongs:** Explains draft-and-verify speculative decoding, its acceptance math and the vLLM implementation.

**Do this after watching:** Compute expected speedup for a given acceptance rate and draft length.

**Slides or code:** https://github.com/gpu-mode/lectures

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V44

**[Neel Nanda: Mechanistic Interpretability, A Whirlwind Tour](https://www.youtube.com/watch?v=veT2VI4vHyU)**

- Creator/source: FAR.AI.
- Published: 2024. Duration: about 22 min.
- Use: core. Modules: 16.

**Why it belongs:** Concise introduction to circuits, features and the grokking case study from a leading practitioner.

**Do this after watching:** Read the slides and run one TransformerLens demo notebook on an induction head.

**Slides or code:** https://www.neelnanda.io/whirlwind-slides

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V45

**[Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)**

- Creator/source: Y Combinator.
- Published: 2025. Duration: about 40 min.
- Use: core. Modules: 17.

**Why it belongs:** Software 3.0 framing: LLMs as a new computer, partial autonomy and building for agents.

**Do this after watching:** Write down one product in your organisation and sketch its autonomy slider.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V46

**[Build A Reasoning Model From Scratch 2: Loading a Base Model, Text Generation, and KV Caching](https://www.youtube.com/watch?v=BJua0yjO5dk)**

- Creator/source: Sebastian Raschka.
- Published: 2026. Duration: about 97 min.
- Use: recommended. Modules: 05.

**Why it belongs:** Text generation and the KV cache implemented on a real base model.

**Do this after watching:** Compare the video's cache with your lab 03 implementation and list the differences.

**Slides or code:** https://github.com/rasbt/reasoning-from-scratch

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V47

**[Building LLMs from the Ground Up: A 3-hour Coding Workshop](https://www.youtube.com/watch?v=quh7z1q7-uc)**

- Creator/source: Sebastian Raschka.
- Published: 2024. Duration: about 165 min.
- Use: recommended. Modules: 04.

**Why it belongs:** A single-sitting walk through the book's architecture code.

**Do this after watching:** Use as a review after Module 04 if the whiteboard walk-through is shaky.

**Slides or code:** https://github.com/rasbt/LLMs-from-scratch

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V48

**[Building more effective AI agents (Erik Schluntz with Alex Albert)](https://www.youtube.com/watch?v=uhJJgc-0iTQ)**

- Creator/source: Anthropic.
- Published: 2025. Duration: about 19 min.
- Use: recommended. Modules: 09.

**Why it belongs:** Short vendor conversation on agent design trade-offs.

**Do this after watching:** Note one claim to test in your own agent harness.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V49

**[CS336 Spring 2025, Lecture 12: Evaluation](https://www.youtube.com/watch?v=x-R5l2HsXqM)**

- Creator/source: Stanford Online.
- Published: 2025. Duration: about 81 min.
- Use: recommended. Modules: 08.

**Why it belongs:** How model builders evaluate; the benchmarks, their failure modes and contamination.

**Do this after watching:** Pick one benchmark and write what it would and would not tell you about your product.

**Slides or code:** https://cs336.stanford.edu/spring2025/

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V50

**[CS336 Spring 2025, Lecture 6: Kernels, Triton](https://www.youtube.com/watch?v=E8Mju53VB00)**

- Creator/source: Stanford Online.
- Published: 2025. Duration: about 80 min.
- Use: recommended. Modules: 15.

**Why it belongs:** Triton kernels explained in the context of training an LM.

**Do this after watching:** Write the vector-add kernel from the lecture before CS336 assignment 2.

**Slides or code:** https://cs336.stanford.edu/spring2025/

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V51

**[GPU MODE Lecture 35: SGLang](https://www.youtube.com/watch?v=XQylGyG7yp8)**

- Creator/source: GPU MODE.
- Published: 2024. Duration: about 45 min.
- Use: optional. Modules: 15.

**Why it belongs:** The second serving engine the track reads, from its authors.

**Do this after watching:** List two design differences from vLLM after watching.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V52

**[A Taxonomy for Next-gen Reasoning (Nathan Lambert)](https://www.youtube.com/watch?v=jQcsVk0KWiQ)**

- Creator/source: AI Engineer.
- Published: 2025. Duration: about 19 min.
- Use: recommended. Modules: 06.

**Why it belongs:** A post-training lead's map of reasoning methods.

**Do this after watching:** Place GRPO, DPO and best-of-N on the taxonomy.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V53

**[How might LLMs store facts (Deep Learning chapter 7)](https://www.youtube.com/watch?v=9-Jl0dxWQs8)**

- Creator/source: 3Blue1Brown.
- Published: 2024. Duration: about 23 min.
- Use: recommended. Modules: 04, 11.

**Why it belongs:** Why facts live in the MLP layers, which is the mechanism behind fine-tuning not adding knowledge reliably.

**Do this after watching:** Explain to a colleague why a few fine-tuning examples do not install a fact.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

### V54

**[2025 in LLMs so far, illustrated by Pelicans on Bicycles (Simon Willison)](https://www.youtube.com/watch?v=YpY83-kA7Bo)**

- Creator/source: AI Engineer.
- Published: 2025. Duration: about 18 min.
- Use: recommended. Modules: 17.

**Why it belongs:** A model of keeping a personal benchmark and running it on every release.

**Do this after watching:** Define your own pelican: one task you will run on every new model.

**Verification:** YouTube watch page fetched on 2026-11-05: playability OK, title, channel and length read from page metadata. Playlists verified by page title. Not watched in full. Checked 2026-11-05.

