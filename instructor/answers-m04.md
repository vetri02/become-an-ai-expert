### Answer key: Module 04

### Quiz answers and reasoning

1. Projections of each token's vector: a query (what I am looking for), a key (what I contain), a value (what I pass on). Q·K is a similarity score between a query position and each key position.
2. A dot product of d terms has spread proportional to sqrt(d), so for large heads the scores become large and the softmax saturates to one-hot, killing gradients and averaging. Lab 02 measured entropy about 2.7 with scaling versus 0.0 without at d=256.
3. It sets future positions' scores to minus infinity so a position cannot attend ahead; training processes the whole sequence at once and would otherwise leak the answer. In cached decoding only the new token's query is computed and every cached key is in the past, so no mask is needed.
4. The block learns a change to the input rather than a replacement, so the identity path lets gradients flow straight through many layers, and each layer starts near the identity.
5. It can still model a bag of tokens (what co-occurs with what) but cannot distinguish orderings; "dog bites man" and "man bites dog" produce the same representation.
6. Input 8x128x768 (12 heads x 64). Q, K, V each 8x12x128x64. Scores 8x12x128x128. Weights the same shape. Output of attention 8x12x128x64, reassembled to 8x128x768.
7. The MLP transforms each position independently, adding capacity and (empirically) storing much of the model's factual associations.

### Lab assessment and mastery gate

The whiteboard walk-through must include shapes at every step and the reviewer should interrupt with "why" at least twice. The loss plot must show validation loss and the three sample checkpoints must be in the README.

### How to use this key

Open after writing all seven answers. Question 6 is the most common on-the-spot coding interview check.
