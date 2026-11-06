### Answer key: Module 07

### Quiz answers and reasoning

1. Embeddings miss exact identifiers, codes, names and rare terms that lexical matching finds; lexical misses paraphrase. Real queries contain both, so hybrid retrieval wins on recall.
2. Each result's score is the sum over retrievers of 1/(k + rank). It uses ranks, not raw scores, so a BM25 score and a cosine similarity can be combined without normalisation.
3. Attention weights sum to one; every extra chunk takes weight from the relevant one. Lab 10 shows the relevant chunk's weight falling to 0.10 with 128 distractors. More chunks also cost more and push the answer toward the generic.
4. In the retrieval query, by the caller's identity, before the model sees anything. The prompt is not a security boundary (Principle 16): any text in the context can be extracted by a sufficiently crafted request.
5. The fraction of golden questions for which a relevant chunk appears in the top k results. Measured separately because a system can retrieve correctly and answer badly, or answer plausibly from the wrong chunk, and you need to know which to fix.
6. Chunks too small (answers split across boundaries; symptom: partial answers); too large (dilution and cost; symptom: generic answers and high latency); boundaries ignoring structure (tables and lists broken; symptom: wrong numbers quoted).
7. Content-hash each chunk and re-embed only changed or new chunks; track source timestamps; run the golden set after each refresh to catch regressions.

### Lab assessment and mastery gate

The reviewer runs the permission test and one golden-set query, then asks why the "after" number is better. A number without a stated change fails the gate.

### How to use this key

Open after the quiz. Questions 3 and 4 are what interviewers mean by "debug a confident wrong answer".
