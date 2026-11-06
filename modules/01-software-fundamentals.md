# Module 01: Software fundamentals for AI systems

## Prerequisites and measurable objectives

Prerequisite: the entry diagnostic passed, or the Foundation bridge exit gate. By the end you can:

1. Build, test, containerise and deploy a small Python service that a stranger can run in three commands.
2. Read any traceback to its cause and any unfamiliar function to its purpose without an assistant.
3. Review code an assistant wrote for you and name the bug it introduced.

**Primary resource:** the official Python tutorial (https://docs.python.org/3/tutorial/). Finish it before adding anything from the reading list.
**Hours:** 10 guided: 8 on the concept blocks, 2 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why this is Module 01

An AI system is a distributed system with a probabilistic component (Principle 20). An AI/ML engineering manager said in September 2026 that they reject candidates who vibe-code and cannot explain an abstract class or how memory works. Senior interviewers say fundamentals are 90% of the job even on LLM teams. The biggest 2026 hiring thread argues that developers who cannot judge AI output are becoming a net negative. You will use an assistant constantly in this course; this module is what lets you check its work.

## Concepts, in order

1. **Python as a professional writes it** (2 hours): Typing, dataclasses, exceptions, modules and packaging, virtual environments, logging. pytest with fixtures and parametrised tests. Debugging with breakpoints. Profiling with cProfile and reading the output. Primary resource: the official Python tutorial plus the pytest docs; 20 Exercism problems with mentor feedback.
2. **Memory and data structures at the level interviews probe** (1 hour): Lists vs dicts vs sets and why lookups differ; what the stack and heap are; what a process and a thread are; the GIL in one sentence; why a list of a million floats is slow and a NumPy array is not.
3. **Networking and APIs** (1 hour): HTTP methods and status codes, JSON, REST, timeouts, retries with backoff, idempotency. These are the failure modes of every LLM call you will ever make.
4. **Git as a daily tool** (1 hour): Branches, pull requests, rebase vs merge, bisect once, a merge conflict resolved on purpose.
5. **Docker and one cloud** (2 hours): A Dockerfile for your service, a container running on a cloud VM you SSHed into, a public URL. AWS, GCP or a $5 VPS.
6. **Working with an assistant without losing the plot** (1 hour): The rules in the Study with an AI assistant page. The test is that you can explain every line.

## Lab

No NumPy lab; the lab for this module is the service itself. Run `labs/run_all.sh` once anyway and read lab 01: it is the smallest complete Python program in the course and shows the style the rest expect (pure functions, assertions, a `__main__` block that prints evidence).

## Build

**Project 1: a deployed API with tests.** A FastAPI service in a domain you care about, backed by SQLite:

- Five or more endpoints, ten or more pytest tests, one test that exercises a failure path
- A Dockerfile and a README with the three commands
- Running on a cloud VM with a public URL
- One profiling session: a slow endpoint found, fixed, and the before/after timing in the README
- One commit where an assistant wrote the first draft and your review comment names the bug you found in it

**Deliverables:** the repo URL, the live URL, and a 300-word post on your blog titled "What the assistant got wrong".

## Mastery gate

Mark complete only when a stranger (your peer reviewer) has cloned the repo, run the tests green, and hit the live URL. You have also explained, on a recorded call or in writing, every function without opening the file.

## Quiz

1. Why does a dict lookup not get slower as the dict grows, and what has to be true of the keys?
2. Your API call to a model provider times out one request in fifty. What do you do, in code, and what must be true of the request for a retry to be safe?
3. What does a virtual environment not isolate that Docker does?
4. A test passes locally and fails in CI. Name three likely causes in order of probability.
5. Explain the GIL in two sentences and say when it matters for an LLM-serving process.
6. An assistant wrote a function that opens a file without closing it and swallows all exceptions. What breaks, and how would you have caught it?

## Primary-source reading

- Python tutorial: https://docs.python.org/3/tutorial/
- pytest: https://docs.pytest.org/
- FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
- Docker Getting Started: https://docs.docker.com/get-started/
- MIT Missing Semester: https://missing.csail.mit.edu/
- Hiring manager on fundamentals: https://www.reddit.com/r/MachineLearningJobs/comments/1wllx1m/comment/pccba9q/
- Reviewing AI-generated code (1,500 upvotes): https://www.reddit.com/r/ExperiencedDevs/comments/1wql3g2/comment/pc51suc/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Quiz me on Module 01 one question at a time, and do not show the key until I have answered.
2. Here is my Project 1 repo. Pick three functions at random and make me explain each one without opening the file.
3. Run labs/run_all.sh with me and explain the first lab's output line by line.
