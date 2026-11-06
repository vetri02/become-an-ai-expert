### Answer key: Module 03

### Quiz answers and reasoning

1. The harness concatenates system prompt, user turns, assistant turns and tool results into one sequence with role markers; the model only ever sees tokens and predicts the next one. Roles are conventions in the text, not separate channels.
2. Temperature rescales the logits before the softmax, flattening (high) or sharpening (low) the distribution. It does not change the ranking of tokens or add knowledge.
3. More merges mean longer tokens, so the same text needs fewer of them. Costs: a larger embedding and output matrix, rarer tokens with fewer training examples each, and worse handling of unusual strings.
4. The model sees tokens, not letters; "strawberry" may be two or three tokens whose letter composition is not represented directly. Counting requires reasoning about sub-token structure it was never shown.
5. 6,000 x 10,000 = 60 million tokens a day; at $3 per million that is $180 a day, $65,700 a year, before output tokens. Prefix caching cuts most of it (Module 10).
6. Add-alpha smoothing assigns a small count to every word. The LLM equivalent is that the softmax never gives exactly zero, so any token can be sampled with some probability; "hallucination" is sampling a plausible continuation the training data does not support.

### Lab assessment and mastery gate

The reviewer asks for Principle 1 in one sentence and for the non-engineer explanation. The trade-off table must have three vocabulary sizes with bytes per token.

### How to use this key

Open after the quiz. If you missed question 1 or 2, redo lab 07 before moving on.
