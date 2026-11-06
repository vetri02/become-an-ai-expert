# Model release checklist

Run on every model version change. Date and sign each line.

- [ ] New model ID pinned in config; old ID retained for rollback.
- [ ] Incumbent model run twice on the full suite; noise band recorded: <value>.
- [ ] Capability suite run on the new model with its own best prompt; per-category table attached.
- [ ] Regression suite run; cases tagged regression vs capability.
- [ ] Safety suites run: direct injection, indirect injection, tool abuse, exfiltration, abstention. Per-category results attached.
- [ ] Any category down by more than 2x noise: STOP and record why, or fix and re-run.
- [ ] Cost per request and p95 measured on the new model.
- [ ] Canary on <n>% of traffic for <period>; dashboard watched.
- [ ] Regression layer re-baselined after full migration.
- [ ] One paragraph on what changed in the model's behaviour, added to the yearly plan.
