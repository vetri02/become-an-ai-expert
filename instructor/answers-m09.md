### Answer key: Module 09

### Quiz answers and reasoning

1. The model follows instructions probabilistically and treats all context text alike (Principle 16); a rule in the prompt holds most of the time, a rule in code holds always. Example: "never refund more than $500 without approval" must be a check in the refund tool, not a sentence in the prompt.
2. Specific enough to guide behaviour, flexible enough to leave room for judgment. Too low: a brittle if-else list of every case. Too high: "be helpful and careful". Start minimal with the best model and add only for observed failures.
3. Summarising rewrites the stable prefix, so prompt caching stops applying and every turn pays full price; the study measured $0.11 per turn with full history versus $0.24 with summarise-and-clear, and recall of planted facts falling from 92% to 38%.
4. Two tools whose descriptions could both apply to the same request. The agent then chooses inconsistently and wastes calls; if a human could not pick the right tool from the descriptions, neither can the model.
5. A well-formed request can still be harmful (a valid email to the wrong recipient, a valid SQL statement that deletes). Safety needs invariants about effects: allowlists, limits, approvals, idempotency.
6. You know capability (pass@1 about 0.9) but not reliability. Run each task several times, report pass^k, and measure noise; a single pass per task cannot distinguish a 90% system from a lucky 60% one.
7. For focused work that would pollute or exhaust the main context (a long search, a large file analysis). It must return a condensed summary with the evidence the lead needs, not its full transcript.

### Lab assessment and mastery gate

The reviewer picks an unfixed failure and asks for the trace and the reason it was left. They check that the budget and step cap are in code by reading it, not by asking.

### How to use this key

Open after the quiz. Question 6 is the difference between an agent demo and an agent product.
