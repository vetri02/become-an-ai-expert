### Answer key: Module 05

### Quiz answers and reasoning

1. Weights in bf16 (2 bytes/param), gradients in bf16 (2), AdamW's two moments in fp32 (8), and often an fp32 master copy (4): about 16 bytes per parameter, so about 16 GB for 1B parameters before activations, which depend on batch and sequence length.
2. For a fixed compute budget, loss is minimised by scaling parameters and training tokens together, about 20 tokens per parameter; earlier models were undertrained. With a fixed budget, train a smaller model on more data than people used to.
3. Decode processes one token per sequence per step and must read every weight once; with few sequences there are few FLOPs per byte read, so bandwidth limits it. Prefill processes the whole prompt at once, so arithmetic per byte is high and compute limits it (lab 12).
4. 2 x 32 x 8 x 128 x 2 bytes = 131,072 bytes, 128 KB per token. At 4,096 tokens that is 512 MB per sequence.
5. Learning rate (too low or schedule decayed too early), data (repeated or too small for the model), and a bug (loss on the wrong targets, no gradient flowing, dropout left on at eval). Check in that order; the bug check is cheapest if you have a tiny overfit test.
6. Excess loss falls by roughly 10^0.65, about 4.5x, for ten times the data; returns diminish toward the irreducible entropy of the source.
7. Because the only way to know whether the model is learning or memorising is to measure on data it has not seen, and because every later decision (which checkpoint, which change) needs a stable yardstick.

### Lab assessment and mastery gate

The reviewer asks for the serving-memory calculation on paper and checks it against lab 06's formula. The nanochat eval table and cost must be in the post. The KV-cache proof must include the identical-output assertion, not just timings.

### How to use this key

Open after the quiz. Questions 1, 3 and 4 are the standard inference-interview trio.
