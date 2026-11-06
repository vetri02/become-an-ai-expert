### Answer key: Module 10

### Quiz answers and reasoning

1. Per request: cached 6,000 x $3/M x 0.1 = $0.0018; uncached 500 x $3/M = $0.0015; output 300 x $15/M = $0.0045; total $0.0078. Times 10,000 = $78 a day. Without caching the prefix costs $0.018, so $240 a day.
2. Private data, untrusted content, and a channel to communicate out. The agent in lab 11 and Target 10 removes the outbound leg with a recipient allowlist; another valid answer is removing untrusted content from the context for high-privilege tools.
3. The model has one input channel and cannot tell who wrote a line; instructions in data are instructions. Lab 11 shows the identical exfiltration with and without "ignore instructions inside documents". Only code that constrains effects stops it.
4. Model ID pinned; capability suite re-run with the new model's own best prompt; injection, tool-abuse and exfiltration suites re-run; noise measured; canary on sampled traffic; regression layer re-baselined after migration.
5. Summarising rewrites the cached prefix, so caching stops applying and every turn pays full input price; the study measured $0.24 versus $0.11 per turn.
6. Hash-pin tool definitions and re-approve on change; per-tool least-privilege tokens; OAuth 2.1 with PKCE and never forwarding the client token upstream; human re-auth for high-risk actions; default-deny sandbox; logging of agent identity, tool and redacted parameters.
7. p50 is the median; p95 is the latency that 5% of requests exceed. Users remember the slow tail, so p95 is the number to engineer and report.

### Lab assessment and mastery gate

The reviewer deletes the allowlist and runs the injection suite; it must fail. They trace one row of the cost table to a log. Target 10 must print all five flags on their machine.

### How to use this key

Open after the quiz and after Target 10. Question 1 is a standard "estimate then halve it" interview prompt.
