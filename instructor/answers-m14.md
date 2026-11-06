### Answer key: Module 14

### Quiz answers and reasoning

1. Regression cases accumulate from the incumbent's failures, so a challenger with different weaknesses scores lower on them. Tag regression versus capability cases, score challengers on capability cases with their own best prompt, compare error distributions by severity, A/B on sampled traffic, then re-baseline the regression layer.
2. Private data, untrusted content, outbound communication. For an agent that must send email, remove untrusted content from the context of the email tool (only approved, structured inputs reach it) and constrain recipients with an allowlist; the outbound leg cannot be removed, so the other two must be.
3. Pass rate per failure category over time, by model version; cost per task; p95 latency; abstention and injection-resistance rates. Per category because an aggregate hides a regression in one category behind gains in others (lab 13).
4. Because the vertical's definition of "good", its data shapes and its regulations are what make a system usable, and hiring threads report domain plus ML beats generic ML; generic agents are a commodity.
5. It is small, obviously correct, tested, follows the project's contributing guide (RFC first for large changes), discloses AI use, and every line was reviewed by you. Benchmarks, bug reproductions and doc drift fit all of these.

### Lab assessment and mastery gate

The reviewer asks you to switch model versions and watches what changes: if anything beyond config and an eval run, the gate fails. They read the tool layer for the allowlist.

### How to use this key

Open after the quiz. Questions 1 and 2 are the senior-level applied interview.
