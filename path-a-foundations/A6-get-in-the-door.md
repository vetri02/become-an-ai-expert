# A6. Get in the door

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 20 hours, spread out. Optional; start during A5, not after.
**Goal:** Convert skills into a role, then let the role compound your skills.
**Optional:** the professional path covers this in Modules 12 and 13; read this for the slower version.
**Principles:** No new principles. Interviewers will probe 1, 11, 12 and 19 from your projects.

## The one pattern that holds across every story

Of the 20+ people profiled in the vetted research, the most common route by far was: take an adjacent job (software engineer, data analyst, developer, project manager), then move sideways into ML inside the company. Nine of the profiled people did this, including the ones who ended up at DeepMind and at FAANG staff level. A senior MLE in an August 2026 thread says ML roles are not junior-friendly and this is how most people become MLEs, even at FAANG.

So the plan is not "study until an ML job appears". It is:

1. Get any job where you write code or handle data, ideally on a team that touches LLMs, data pipelines or MLOps.
2. Find an unsolved problem at that job and solve it with ML or an LLM. Three profiled people got promoted this way: one automated a boring part of his job and was invited onto the ML team; one pitched a project on the company's own energy data as a money-maker; one volunteered to build the deep learning feature nobody owned.
3. Become "the AI person" there. Then either move internally or leave with a title.

## Tactics that the evidence supports

- **One deeply documented project beats five demos.** README with eval results, cost/latency numbers, failure cases and the trade-offs you chose. Your A5 projects are this.
- **Make your work public.** A free GitHub Pages blog, short posts, a talk at a local meetup. Every verified referral in the research came from someone who already knew the person's public work (the DeepMind referral came after a YouTube channel and open-source repos; the FAANG referral came through friends who knew his blog). One commenter says a referral "10x's your callback rate" compared with spraying applications.
- **Apply where there are fewer applicants.** Small companies, unglamorous industries, local firms. One person got his first ML job at a small company by playing up a physics minor and two intro projects.
- **Consulting as a side door.** One 21-year-old with no degree released a fine-tuned coding model, got an unpaid open-source role, started consulting for small businesses at about $3k/month, and a repeat client hired him full time. It worked, but the first role paid under market. Treat it as a way in, not a destination.
- **Negotiate every offer.** One person's pay went 47k to 65k to 90k to 115k over 20 months by changing jobs quickly and negotiating each time.
- **Never claim "shipped" for things nobody uses.** Interviewers call it a red flag. Ten real users is enough to say shipped.

## Interview the 2026 way

- Lead with decisions and trade-offs. "I chose hybrid search because recall@10 went from 0.61 to 0.84; reranking added 200ms so I only use it for long queries."
- Narrate while coding. Expect Python/PyTorch on the fly, not LeetCode hard.
- Expect ML system design: a recommendation system, a ranking pipeline, an inference service, a GenAI app. Practice drawing these.
- Know your own numbers: cost per request, latency, eval scores, dataset size.
- Research every interviewer and their work beforehand (the DeepMind hire did exactly this).
- Be ready to review AI-generated code live and say what is wrong with it.

## Build

**Project A6: the application kit.**
- A one-page portfolio site listing 3 projects, each with one measured result in the first line
- A resume where every bullet has a number
- Five target companies and one person at each you can reach through public work (their blog, a repo you contributed to, a meetup)
- A 10-minute talk on one of your projects, given at a meetup or recorded

**Done when:** you have had three conversations with people who could refer you, and one interview.

## Sources

- Adjacent-job pattern, senior MLE: https://www.reddit.com/r/learnmachinelearning/comments/1vkco40/comment/p2uj57j/
- Referral "10x's callback rate", "one documented project": https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/odzfxx9/
- Interview style 2026: https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/oe1p2gc/
- "Shipped" red flag: https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p03i3np/
- Director of AI at 21, consulting route: https://www.reddit.com/r/LocalLLaMA/comments/1vi8jlr/comment/p2btrbo/
- DeepMind research engineer without an ML degree (Aleksa Gordić): https://gordicaleksa.medium.com/how-i-got-a-job-at-deepmind-as-a-research-engineer-without-a-machine-learning-degree-1a45f2a781de
- Staff MLE AMA, referrals and networking: https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/
- 20-month data science transition, job-hopping and negotiation: https://www.reddit.com/r/datascience/comments/713hnw/
- Solve a problem at work (u/certain_entropy, 81 pts): https://www.reddit.com/r/MachineLearning/comments/ojp76r/comment/h546lvl/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Review my public post as a stranger who might cite it.
2. Rehearse an informational chat with me. You play the person I am messaging.
3. Ask me which of my projects a recruiter could run in five minutes, and what they would see.
