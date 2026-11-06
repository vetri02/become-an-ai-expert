# Become an AI Expert: understand, build, measure

A self-study course in AI engineering with large language models for working professionals with no prior ML background. 200 guided hours. You build a small language model from the inside, ship an evaluated LLM system to real users, get into an AI role, and go deep in one specialism. Free, with no sign-up.

The question running through every module: **when the model is wrong, how do you know, what does it cost, and what evidence proves your system works?**

## What you will be able to do

- Explain what a language model is doing from tokens to sampling, and draw the Transformer on a whiteboard.
- Train, post-train and evaluate a small LLM yourself, and write up what broke.
- Build retrieval and agents with a versioned golden set, calibrated graders, pass@k and pass^k, and a regression suite in CI.
- State your own system's recall@k, cost per request and p95 latency from memory, and halve the cost without hurting the eval.
- Defend every design decision with a measurement, in an interview or a pitch.
- Pick one of three specialisms (applied products, inference infrastructure, research engineering) and produce one artifact a stranger would cite.

## How it is built

Every claim links to its source: two vetted Reddit research sets from November 2026, about ninety practitioner write-ups, and the official pages of every resource named. Twenty first principles, each derived from how the thing works, anchor the course; seventeen of them have a lab you run on your laptop in minutes. Thirteen labs and three hands-on targets are self-checking. A citation check and a verification report are regenerated on every build.

This is the sibling of [AI Security Engineering](https://aisec.engineering/), the same author's course on securing AI applications, agents and model lifecycles. The two share their structure and apparatus; Module 10 here teaches the security every AI engineer needs and hands off to the sibling for depth. The course material, every page plus the labs, targets, templates and tutor skill, is public at [github.com/vetri02/become-an-ai-expert](https://github.com/vetri02/become-an-ai-expert); the build and deploy source stays private. Corrections and questions go to [the issue tracker](https://github.com/vetri02/become-an-ai-expert/issues). The course is also distributed through this site, the zip on the Study with an AI assistant page, and the handbook PDF.

## Novice or professional?

The course has two ways in, and the entry diagnostic tells you which is yours.

- **Professional track (the 200-hour path):** you already write code or work with data. Start at the diagnostic, then Module 01. This is the main path in the sidebar: Stages 1 to 6, five milestones, three targets, the capstone.
- **Novice track (the on-ramp from zero):** you are new to coding or your math stops before gradients. Choose **Novice** in the sidebar and the **On-ramp from zero (Path A)** group appears right after Get started: five modules (code and systems, just-enough math, classical ML, then the LLM and the engineering material at a slower pace), about 210 hours. Then you join the professional path at Module 03 and finish it. A6 to A8 are optional reading beside Modules 12 to 17. If you only have small gaps, the 40-hour Foundation bridge is the short version.

Both tracks start from the same twenty first principles, read before the first module, and share the labs, targets, milestones, capstone and media library. Each Path A page names the principles it teaches and the lab that demonstrates them.

## How to start

1. Read **How the course works**, then **First principles**, the twenty facts every module builds on.
2. Take the **Entry diagnostic**. It tells you whether to start at Module 01, do the Foundation bridge first, or take the Novice track from A1.
3. Set up the lab: get the course code from [GitHub](https://github.com/vetri02/become-an-ai-expert) (or the [zip](https://github.com/vetri02/become-an-ai-expert)) and run the thirteen labs once.
4. Start Module 01 (Professional) or A1 (Novice). Mark each step complete at the bottom of its page; progress and your track are saved in this browser.
5. Optional: open the folder from step 3 in Claude Code or Codex and the tutor skill from **Study with an AI assistant** is already there; use the three follow-up prompts at the end of every module.

Terms you do not know yet are in the **Glossary** under Reference; every one of them is taught in the module that needs it.

## Questions people ask

### Is the course free?

Yes. The code is MIT, the writing is CC BY 4.0, and there is no sign-up. The labs, targets and reading cost nothing and run on a laptop. A few projects spend money: plan on about $50 to $200 of GPU time (most of it the nanochat training run in Module 05) and $50 to $150 of API calls over the whole course; the optional larger training runs cost more. The [compute appendix](appendix/compute-and-costs.md) lists every figure with the date it was checked. The recordings in the media library are public videos by their original authors.

### How long does it take?

200 guided hours on the professional track, about 20 weeks at 10 hours a week. The novice track adds about 210 hours of on-ramp first, so about 390 hours in total. Full-time learners can halve the calendar but not the hours.

### Do I need a GPU or a paid API key?

Not for the labs and targets. Everything that self-checks runs on a laptop with Python 3 and NumPy. The projects in Modules 05, 06 and 11 use rented GPU time or free Colab; the compute appendix quotes the costs, dated.

### What do I need to know before I start?

Python, Git, HTTP, SQL and basic probability. The entry diagnostic checks these in thirty minutes and routes you to Module 01, the 40-hour Foundation bridge, or the novice on-ramp.

### Can a complete beginner do it?

Yes, on the Novice track: five on-ramp modules (code and systems, just-enough math, classical ML, the model from the inside, AI engineering) and then the professional path from Module 03.

### What will I be able to do at the end?

Train and evaluate a small language model, ship a retrieval system and an agent with a versioned golden set, calibrated graders and a regression suite in CI, state your system's recall@k, cost per request and p95 latency from memory, and defend every design decision with a measurement. The capabilities page lists each outcome with its evidence and pass bar.

### How is this different from other AI courses?

It starts from twenty first principles, seventeen of which have a lab you run in minutes. Every claim links to a checked source and the citation report is regenerated on each build. Three graded targets make you fix broken systems until a grader stops finding holes. Measurement, not demos, is the grade.

### Can I use ChatGPT or Claude while I learn?

Yes, as a tutor. The course ships a tutor skill for Claude Code and Codex that quizzes, reviews your code and refuses to do the projects for you. Get it from the [Study with an AI assistant](ASSISTANT.md) page, which links the whole course as a zip (the skill is inside, ready to use) and the skill file on its own, with the start and resume commands.

### Is there a companion course on AI security?

Yes. [AI Security Engineering](https://aisec.engineering/) is the same author's course on securing AI applications, agents and model lifecycles, built the same way. Module 10 here covers the security basics every AI engineer needs; the sibling course goes deep.

### Is there a certificate?

No. The evidence is your artifacts: five milestones scored by a peer reviewer, a capstone scored against a 100-point rubric, and a final scenario exam. Those are what referrals and interviews run on.

