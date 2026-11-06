# Module 12: The internal move and public work

## Prerequisites and measurable objectives

Prerequisite: Milestone C. By the end you can:

1. Pitch and deliver a 30-day AI pilot at your current job with a dollar cost, eval numbers and failure cases.
2. Publish a public record (three posts, one runnable repo, one talk) that a stranger could refer you on.
3. Write a README that a reviewer of 2026 portfolios would call finished.

**Primary resource:** Janvi Kalra on The Pragmatic Engineer, From Software Engineer to AI Engineer (https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 10 guided, which the concept blocks above account for in full; the lab run and the build fit inside them.

## Why this is the highest-probability route

Of the twenty-plus people in the vetted stories, nine got into ML by taking an adjacent job and moving sideways inside the company, including the DeepMind and FAANG staff hires. A senior MLE in August 2026 says ML roles are not junior-friendly and this is how most people become MLEs. Janvi Kalra, now at OpenAI, was rejected by her company's AI team, became its go-to LLM person through side projects, and was an easy hire when it expanded: "it's much easier to transfer internally." Every verified referral came from someone who already knew the person's public work.

## Concepts, in order

1. **Find the unsolved problem** (1 hour): something your company pays for in human hours that your Stage 3 skills can do: triage, extraction, search over internal docs, summarising tickets. One person automated a boring part of his job and was invited onto the ML team; another pitched a model on the company's energy data as a money-maker.
2. **Pitch a pilot, not a career change** (1 hour): one named problem with a dollar cost, one tool, 30 days, a budget under a few hundred dollars, the data-security question answered first. Position as a senior engineer adding AI, not a junior ML hire. A backend-shaped first project is an internal LLM gateway with timeouts, retries, idempotency, cost tracking and tracing; companies now staff such teams.
3. **Deliver with evals from day one** (2 hours): the Module 08 harness on the pilot; report results with eval numbers, cost, and failure cases; expect role blur and be ready to throw work away when a new model makes it obsolete.
4. **Ask for the title** (1 hour): after one successful project, ask for AI in your title or a transfer; if the company has nothing AI-adjacent, move to one that does in your current role and repeat.
5. **Public work** (3 hours): a free GitHub Pages blog; three posts with numbers (the nanochat write-up, the cost cut, the reversed decision); one runnable repo; one talk at a meetup or recorded; one upstream contribution; answering questions in a community weekly. The DeepMind hire built a YouTube channel and open-source repos per topic for 1.5 years. Generosity created the opportunities in the most upvoted self-taught story.
6. **The README that reads as finished** (1 hour): one-line result with a number; architecture diagram; eval table against a baseline on a described, versioned set; p50/p95 and cost per request; a "where this breaks" section; reversed decisions; three commands to run. Make clear what is yours; never post course exercises as projects. Start from `templates/project-readme.md`.
7. **Contributing upstream without wasting a maintainer's time** (1 hour): "good first issue" labels; doc drift as a first PR; RFC before large changes; disclose AI use; review every line yourself. Maintainers spot AI-generated PRs.

## Lab

No lab. The artifact is the pilot and the public record.

## Build

**Project 12: the pilot.** A pitch document (the pilot-pitch template in `templates/pilot-pitch.md`) with the dollar cost; the delivered pilot with its harness; a results memo with eval numbers, cost and failure cases; the title conversation had.

**Project 13: the public record.** Three posts, one runnable repo with the finished README, one talk, one upstream PR opened.

**Deliverables:** the pitch and results memo (redacted if needed); links to the posts, repo, talk and PR.

## Mastery gate

A person outside your company has starred, cited or commented on your work, and your pilot results memo has eval numbers your reviewer can trace.

## Quiz

1. What are the three parts of a pilot pitch that get approved, and what gets one rejected?
2. Why position as a senior engineer adding AI rather than a junior ML hire?
3. What belongs in the first line of a finished README?
4. Why does doc drift make a good first upstream PR?
5. Name three things reviewers of 2026 portfolios say make a project read as unfinished.
6. What did the DeepMind hire do in each three-month block, and why did it work?

## Primary-source reading

- Janvi Kalra, Pragmatic Engineer, 2025-05-28: https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer
- Adjacent-role pattern, senior MLE: https://www.reddit.com/r/learnmachinelearning/comments/1vkco40/comment/p2uj57j/
- Gordić on public work and the referral: https://gordicaleksa.medium.com/how-i-got-a-job-at-deepmind-as-a-research-engineer-without-a-machine-learning-degree-1a45f2a781de
- Staff MLE on blogs and referrals: https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/
- Volunteered for DL, became the DL guy (81 pts): https://www.reddit.com/r/MachineLearning/comments/ojp76r/comment/h546lvl/
- vLLM contributing guide: https://docs.vllm.ai/en/stable/contributing/
- What reviewers judge repos on (Lange): https://georglange.com/post/ai-safety-application-guide/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Review my pilot pitch as the sceptical manager who has to fund it.
2. Ask me what a stranger would cite in my public post and whether every number in it is traceable.
3. Rehearse the title conversation with me. You play the manager.
