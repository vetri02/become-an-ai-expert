### Answer key: Module 13

### Quiz answers and reasoning

1. "Two numbers. Groundedness: a code grader checks that every claim cites a retrieved chunk, and a judge calibrated on 120 human labels (TPR 0.91, TNR 0.84) checks the chunk supports it. Abstention: on the 40 golden queries with no relevant document, the system says it doesn't know 92% of the time. Both run in CI; a model upgrade dropped abstention to 70% and we caught it before rollout."
2. Retrieval returned the wrong chunk (check recall@k on that query); the right chunk was retrieved but diluted or chunked badly (check what was in the context); nothing relevant was retrieved and the system did not abstain (check the abstention path). Vocabulary mismatch between query and document is the common root cause.
3. Designing the loop: chunking and its trade-offs, context-window effects, output validation, and a feedback loop that improves retrieval from failures. Juniors talk prompts; mid-levels explain embeddings and RAG.
4. Decline, politely, and say why: experienced engineers treat deployable work and take-homes sent before any conversation as free labour. Offer a time-boxed alternative or a walkthrough of an existing project.
5. Weights 140 GB; KV per token 2 x 80 x 8 x 128 x 2 = 327,680 bytes, 320 KB; per sequence at 4,096 tokens 1.25 GB; batch 8 is 10 GB; total about 150 GB plus overhead. Two 80 GB GPUs with tensor parallelism, or one at INT4 (about 35 GB weights) with room to spare.
6. Because titles carry across employers and set the band for the next negotiation; "Machine Learning Engineer" medians run far above "AI Engineer" for similar work, and the title is cheap for the employer to grant.

### Lab assessment and mastery gate

The reviewer runs the depth probe: five "why" levels on one project. Running out at level three fails. The from-memory implementations must execute.

### How to use this key

Open after the mock interview. Rehearse question 1 until it is 60 seconds without notes.
