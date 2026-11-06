# A1. Code and systems foundations

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 60 guided hours (six weeks at 10). Skip anything you can already do.
**Goal:** Write, test, debug and deploy a small Python service without help. Everything later in the course assumes this.
**Principles:** Principle 20 (an AI system is a distributed system). Read the [First principles](../FIRST-PRINCIPLES.md) page before this module; every Path A module names the principles it teaches, and the labs that demonstrate them run on your laptop.

## Why this comes first

An AI/ML engineering manager in a September 2026 hiring thread said they reject candidates who "vibe-code" and cannot explain an abstract class or how memory works. Senior interviewers say software fundamentals are 90% of the job even on LLM teams. The biggest 2026 hiring thread (1,500+ upvotes, r/ExperiencedDevs) argues that developers who cannot tell good AI-generated code from bad are becoming a net negative. You will use AI assistants constantly in this course. This module is what lets you check their work.

## Learn, in this order

1. **Python properly.** Variables, functions, classes, modules, virtual environments, typing, exceptions. Then testing with pytest, debugging with breakpoints, and reading a traceback top to bottom.
   - Free course: Harvard CS50P (Introduction to Programming with Python) or the official Python tutorial.
   - Practice: solve 30 small problems on Exercism's Python track. Do not skip the mentoring feedback.
2. **The terminal and Git.** Navigate, pipe, grep. Clone, branch, commit, push, open a pull request. Resolve one merge conflict on purpose.
   - Free: "The Missing Semester of Your CS Education" (MIT), lectures 1 to 6.
3. **SQL.** SELECT, JOIN, GROUP BY, window functions. Load a CSV into SQLite or Postgres and answer ten questions about it.
   - Free: SQLBolt, then Mode's SQL tutorial.
4. **CS fundamentals, just the load-bearing parts.** Lists vs dicts vs sets and why lookups differ, recursion, big-O at the "which of these is 1000x slower" level, how memory and the stack work, what a process and a thread are, what HTTP, JSON and a REST API are.
   - Free: CS50x weeks 0 to 6 if you want structure. Otherwise "Think Python" chapters on data structures plus any HTTP explainer.
5. **Packaging, Docker and one cloud.** Build a FastAPI app, put it in a Dockerfile, run it locally, push it to a cloud VM (AWS EC2, GCP Compute, or a $5 VPS), SSH in, and hit it from your phone.
   - Free: FastAPI official tutorial, Docker "Getting started", your cloud's free tier docs.
6. **Using AI assistants without losing the plot.** Rule for this course: every line an assistant writes, you must be able to explain. Ask it to explain principles back to you. Never paste code you cannot read.

## Build

**Project A1: a deployed API with tests.**
A small FastAPI service (any domain you care about: recipes, bookmarks, workouts) backed by SQLite, with:
- At least 5 endpoints and 10 pytest tests
- A Dockerfile and a README that explains how to run it
- Running on a cloud VM with a public URL
- One profiling session where you found and fixed something slow

**Done when:** a stranger can clone the repo, run the tests, and hit your live URL. You can explain every function without opening the file.

## Skip for now

- Deep algorithm grinding (LeetCode hard). 2026 ML interviews ask for Python/PyTorch on the fly and system design, not LeetCode hard.
- Any ML library. Not yet.
- Frameworks like LangChain. Practitioners say framework knowledge without fundamentals is worthless.

## Checkpoint (answer out loud, no notes)

1. What is the difference between a list and a dict lookup, and when does it matter?
2. What happens, step by step, when your browser requests your API's URL?
3. Why do we use virtual environments and Docker? What problem does each solve?
4. Read a traceback from a failing test and say which line caused it and why.
5. Explain what an abstract class is and when you would use one.

## Sources

- Hiring manager on fundamentals and "vibe-coding": r/MachineLearningJobs, Sep 2026, https://www.reddit.com/r/MachineLearningJobs/comments/1wllx1m/comment/pccba9q/
- 1,500-upvote thread on reviewing AI output: r/ExperiencedDevs, Sep 2026, https://www.reddit.com/r/ExperiencedDevs/comments/1wql3g2/comment/pc51suc/
- Interview format in 2026 (Python/PyTorch, not LeetCode): r/learnmachinelearning, Apr 2026, https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/odzfxx9/
- Roadmap thread, "software fundamentals first": r/learnmachinelearning, Jul 2026, https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owbthwt/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Quiz me on the A1 checkpoint out loud, one question at a time.
2. Here is my first repo. Pick a function and make me explain it line by line.
3. Set me one terminal-and-Git task and check my commands before I run them.
