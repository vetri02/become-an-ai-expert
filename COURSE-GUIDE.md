# Course guide: Become an AI Expert

## Why this course exists

Most "learn AI" material teaches you to call an API and build a demo. The people who hire in 2026 say that is the problem: a hiring manager rejects candidates who cannot explain an abstract class, a 1,500-upvote thread of senior developers says people who cannot judge AI-generated code are becoming a net negative, and interviewers ask "how did you measure hallucinations?" rather than for a proof. The self-taught people who made it to DeepMind, FAANG staff level and Anthropic did the opposite of the demo route: they built things from scratch, published them, and measured everything.

This course is the from-scratch, measured route, compressed into 200 guided hours for someone who already works in software or data. The evidence says the whole transition takes 18 months to 3 years; the difference between that and 200 hours is the unguided practice, the real-user periods, the job search and the track depth that follow the guided core, which the course scopes but does not count.

## The course promise

If you do the work, at the end you will have: a small LLM you trained and post-trained yourself with a written post-mortem; a retrieval system and an agent, each with a golden set, calibrated graders and a CI regression suite, used by real people; a documented cost cut; three public posts and a talk; one artifact in your chosen specialism; and a capstone a reviewer scored against a rubric. That is the evidence base that gets referrals and offers.

## Audience and tracks

Working professionals with no prior ML background: software engineers, data analysts and scientists, data and platform engineers. The entry diagnostic checks the assumed base (Python, Git, HTTP, SQL, basic probability). If it shows gaps, the optional Foundation bridge (40 hours) fills them, and Path A, the 210-hour on-ramp from zero (A1 to A5), exists for readers who need more; they join the numbered modules at Module 03 and skip Stage 1, which the on-ramp covers. Choosing Novice in the sidebar puts the on-ramp into the path and recounts the hours.

After the core, Stage 5 is a choice of one of three specialisms. You do one; the other two are listed as optional so you can read them before choosing.

## Workload and sequence

200 hours at about 10 hours a week is 20 weeks. Stage boundaries below fall where the running total of hours crosses a whole week, so a stage of 59 hours gets five weeks and one of 24 hours gets three. Full-time learners can halve the calendar but not the hours.

| Stage | Weeks | Modules | Hours |
|---|---|---|---|
| 1 · Foundations for AI systems | 1 to 2 | 01, 02 | 20 |
| 2 · The model from the inside | 3 to 7 | 03 to 06 | 45 |
| 3 · AI engineering with measurements | 8 to 12 | 07 to 11 | 59 |
| 4 · Getting in | 13 to 14 | 12, 13 | 18 |
| 5 · Depth in one track | 15 to 17 | 14 (or 15 or 16) | 24 |
| 6 · Capstone and beyond | 18 to 20 | 17, capstone, final exam | 34 |
| | | **Total** | **200** |

Milestones A to E sit at the end of Stages 1 to 5. Each is a submission checklist reviewed under the peer-review protocol. Three hands-on targets (after Modules 05, 08 and 10) are planted-bug programs you fix until their checks print.

## How to learn a module

Each module page has the same shape: prerequisites and measurable objectives; why it matters, with the evidence; concepts in order with one primary resource; a lab you run; a build with deliverables; a mastery gate; a quiz; primary-source reading; and curated media. The answer key is collapsed at the bottom and should be opened only after you have attempted the quiz and lab. In the course folder the answer keys are `instructor/answers-mNN.md` and the media list is `MEDIA-INDEX.md`; the website folds both into each module page.

Suggested routine for a typical 10 to 16 hour module over one to two weeks, at roughly 10 hours a week (scale it for the 4-hour Module 17 and the 24-hour track modules; `templates/weekly-log.md` is the log):

| Hours per week | Activity |
|---|---|
| 2 | Concepts and readings, notes in your own words |
| 5 | Build and experiment, no video open |
| 2 | Lab, target, quiz |
| 1 | Write up evidence, publish, answer one community question |

Budget one bad week in four. If you miss a week, resume; do not try to catch up.

## Assessment and grading

- **Quizzes** are self-marked against the answer key. They test whether you can explain, not whether you remember.
- **Mastery gates** are the conditions for marking a module complete. They are things a reviewer could check: a number, a repo, a plot, a recording.
- **Milestones** are scored under the peer-review protocol's 20-point rubric, by a peer or by yourself one week later using the solo variant. 14 of 20 passes.
- **The final exam** is ten scenarios answered in writing, self-marked against the key with a stated pass bar.
- **The capstone** is scored against a 100-point rubric with mandatory no-go conditions and oral-defense prompts.

There are no certificates. The evidence is the certificate.

## Environment and spending

Everything runs on a laptop except the model-training runs. Budget $100 to $300 of GPU time and $50 to $150 of API calls over the course. The compute appendix lists free tiers and current prices. The thirteen labs need Python 3 and NumPy only.

## Evidence and limitations

Every claim links to its source. The evidence is practitioner opinion, self-reported stories and official resource pages, not a hiring-outcome dataset. Prices, pay and tool names are dated. Survivorship bias is stated where it applies. The course does not promise a job; it builds the record that the evidence says gets people hired.

## After the course

The Advanced tracks page turns your chosen specialism into a multi-year plan. The expert markers in Module 17 are the standard: own a problem end to end, be known outside your company for one artifact, go arbitrarily deep under questioning, and re-run your evals on every model release.

## Version notes

- **1.0 (2026-11-05):** Two paths, three tracks, seven appendices, published as one page.
- **1.1 (2026-11-05):** First principles, 13 labs, capabilities file, hour budget, citation check.
- **2.0 (2026-11-05):** Restructured as a staged path: 17 modules with quizzes and answer keys, 5 milestones, 3 targets, entry diagnostic, foundation bridge, peer review, capstone, final exam, media library, templates, glossary, verification report, handbook PDF.
- **2.1 (2026-11-05):** Resized to 200 guided hours at the owner's request; every module, concept block and the capstone rescaled; the evidence on real transition timelines kept. Added the Novice track chooser, the tutor skill downloads, follow-up prompts on every module, and the FAQ.
