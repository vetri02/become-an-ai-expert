### Answer key: Module 11

### Quiz answers and reasoning

1. Right: a strict output schema the prompt keeps breaking; a narrow classifier where a 1B model fine-tuned beats a prompted 70B on cost and latency. Wrong: injecting the company wiki (use retrieval); fixing a behaviour you have not measured with a prompt-only baseline.
2. It freezes the base weights and trains small low-rank matrices added to selected layers, so there are few trainable parameters, less optimiser memory, and the adapter is a small file to store and swap.
3. A fact is distributed across many weights learned from many contexts; a few examples give few, correlated gradient steps that mostly shift style. Retrieval places the fact in context at inference, which the model uses reliably.
4. Catastrophic forgetting (or over-specialisation). A general-ability eval kept from Module 06, run before and after, would have shown the drop.
5. Hundreds to a few thousand clean, deduplicated, representative examples. Quality, coverage of the real distribution, and a held-out split matter more than the count.

### Lab assessment and mastery gate

The reviewer checks that the three variants share the same golden set and graders. A decision record whose conclusion does not follow from its own table fails.

### How to use this key

Open after the quiz. Question 1 is the "when would you fine-tune" interview question.
