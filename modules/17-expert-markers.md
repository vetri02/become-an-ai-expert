# Module 17: Expert markers and staying current

## Prerequisites and measurable objectives

Prerequisite: Milestone E. By the end you can:

1. State the four expert markers and the evidence you have for each today.
2. Run a model-release checklist on your own systems in under a day.
3. Keep up with the field in 20 minutes a day from primary sources, and plan one long study a year.

**Primary resource:** Atharva Raykar, How I keep up with AI progress (https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 4 guided, which the concept blocks above account for in full; the lab run and the build fit inside them.

## The markers

From the people who got there: you own a problem end to end and your manager can state your impact in one sentence (the FAANG MLE says visibility, not raw skill, is how promotions happen); people outside your company know your work through one artifact (a used repo, a reference write-up, a course module, a talk, a paper); you can go arbitrarily deep in one area under questioning; you learn on a cadence. And you are generous: the most upvoted self-taught story credits helping others for every opportunity.

## Concepts, in order

1. **The cadence** (1 hour): every model release, re-run your evals and update your mental model; every quarter, one paper replicated or one upstream contribution; every year, one long study outside your comfort zone (the DeepMind hire's three-month blocks); weekly, answer questions in your community and read one primary source.
2. **The model-release checklist** (1 hour): pin the new model ID; re-run capability evals with the model's own best prompt; re-run safety and injection suites; measure noise by running the current model twice; re-baseline the regression layer; canary. Lab 13; `templates/model-release-checklist.md` is the form. Keep a tiny harness so a new model can be tried the day it ships (Simon Willison's approach).
3. **Sources, not feeds** (1 hour): one practitioner's list: Willison's blog as the single starting stream; Karpathy; the lab blogs and model cards; practitioners who show their work (Husain, Shankar, Liu, Yan, Huyen, Khattab, Bergum, Lambert); one digest if you want no social feeds. Treat second-hand reporting as wrong by default. Twenty minutes a day. Production experience with your own data beats all of it; a 30,000-developer survey found hands-on experimentation, not newsletters, is how people learn what new models can do.
4. **The honest counterpoints** (1 hour): a master's is close to the minimum filter at many companies and even the self-taught staff engineer feels bias without one; if affordable and employer-paid once you are employed, it removes a filter and teaches less than the projects did. Survivorship bias: of the famous "self-taught" names only Olah, Radford and Hotz truly lack degrees; the repeatable path is the one you just took.

## Lab

`labs/lab13_model_upgrade.py`, then the real checklist on your Track artifact with a new model version.

## Build

**Project 16: the yearly plan.** One page: the four markers with your current evidence for each, the gap, the one artifact that closes the biggest gap, the long study for next year, your three sources, and the date of your next model-release run.

**Deliverables:** the page, published.

## Mastery gate

Your release checklist has been run once end to end on a real system with results, and your plan names a specific artifact and date.

## Quiz

1. State the four expert markers and give the weakest piece of evidence you have for each.
2. What is the model-release checklist, in order?
3. Why "primary sources, second-hand reporting wrong by default"?
4. What is the honest answer on the master's question?
5. What does survivorship bias change about which stories to copy?

## Primary-source reading

- FAANG MLE on visibility and cadence: https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojovnqx/
- Senior AI engineers on what matters now: https://www.reddit.com/r/MLQuestions/comments/1uhxdj3/comment/oulo013/
- Raykar, how I keep up with AI progress: https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/
- Simon Willison: https://simonwillison.net/
- Stack Overflow 2026 survey: https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional
- Master's as filter: https://www.reddit.com/r/learnmachinelearning/comments/1muc3g7/comment/n9jexx9/ and https://www.reddit.com/r/learnmachinelearning/comments/1l4y3yy/comment/mwcpwb2/
- Chris Olah background (80,000 Hours): https://podcasts.apple.com/us/podcast/108-chris-olah-on-working-at-top-ai-labs-without-an/id1245002988?i=1000531710782
- Generosity (u/certain_entropy): https://www.reddit.com/r/MachineLearning/comments/ojp76r/comment/h546lvl/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me for the evidence behind each of the four markers and tell me which is weakest.
2. Walk through my model-release checklist with me on a real system, one step at a time.
3. Read my yearly plan and ask whether the artifact and the date are specific enough for a stranger to check.
