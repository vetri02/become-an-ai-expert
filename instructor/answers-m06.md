### Answer key: Module 06

### Quiz answers and reasoning

1. It shifts the model toward the format, style and behaviour of the instruction data (answer rather than continue, use the chat template). A few hundred examples give few, correlated contexts for any fact, so knowledge is learned unreliably; retrieval supplies facts without touching weights.
2. For each sampled token, increase its log-probability in proportion to the advantage (reward minus baseline); if the advantage is negative, decrease it. Tokens in rewarded sequences become more likely; tokens in penalised sequences less.
3. It subtracts the mean reward of the group of samples for the same prompt, so the update depends on whether a sample was better than its siblings rather than on the absolute reward. That removes prompt-difficulty variance from the gradient.
4. It adds a term pulling the policy's distribution back toward the reference at every visited state, so the policy cannot drift far to exploit the reward. The cost is a cap on how much reward it can collect: lab 09 shows reward 1.2 instead of 8 with the leash on.
5. Example: reward = count of "please" led to every token being "please". Fix: reward presence rather than count, cap it, or add a fluency term (likelihood under the reference), which is what the KL penalty approximates.
6. Because RL moves capabilities in different directions; an aggregate can rise while a capability you care about falls (lab 13 shows the same effect for a model upgrade). Separate evals show the trade-off; an aggregate hides it.
7. Best-of-N helps when you have a verifier or a good selector and the model sometimes gets it right. Self-refinement hurts when the model cannot judge its own output and "refines" a correct answer into a wrong one, which Raschka's experiments document.

### Lab assessment and mastery gate

The reviewer checks that the eval table has separate capability and general-ability columns and asks what the KL coefficient did. "It got better" with one number fails the gate.

### How to use this key

Open after the quiz and after your own GRPO run. Questions 2 to 4 are what Track C interviews probe.
