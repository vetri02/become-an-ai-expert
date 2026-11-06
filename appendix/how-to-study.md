# How to study: the method that makes this course work

Read this before Module 01, or before A1 on the Novice track. Everything here comes from people who did it or who teach it (Karpathy, Raschka, Chip Huyen, Nathan Lambert, Vicki Boykis, Hamel Husain) plus the vetted Reddit stories.

## The ten rules

1. **Work long, not hard.** Nathan Lambert (post-training lead at Ai2): "You can change the world working 4 hours a day" if you keep stacking small steps in one direction. Most people fail by not working long enough, not by not working hard enough. The vetted stories ran 2 to 5 hours a day for 1.5 to 3+ years.
2. **Pick one resource per topic and finish it.** Raschka: "start with one resource and stick to it." Karpathy: "It feels bad to bounce from material." This course names one primary resource per module for that reason.
3. **It should feel like effort.** Karpathy: learning is "the mental equivalent of sweating." If a module feels easy, you are watching, not learning. Close the video and type the code from memory.
4. **Learn depth-first, on demand.** Pick a concrete project, learn what it needs, finish it, then widen. Karpathy's three rules: iterate on concrete projects, teach or summarise everything in your own words, compare yourself only to your younger self.
5. **Build end to end, for a real person.** Chip Huyen: "Doesn't matter what you build, as long as you do it end to end: starting from an idea and deploying it so that a friend can use it." But "learning only by building is like learning a new language only by speaking," so pair each project with its module's book or course.
6. **Try first, then read the solution.** Raschka: "you learn better if you try first and then appreciate the solution." Attempt every exercise and every "build" item before looking anything up.
7. **Write to remember.** Lambert wrote his widely read RLHF post before he had fully read the literature, as a way to learn it. Every module in this course ends with a short write-up. Keep them on a free GitHub Pages blog from day one. They become your portfolio.
8. **Look at your data.** Hamel Husain's single most repeated rule. Read 20 to 50 raw outputs by hand before trusting any metric. This habit starts in Module 02 (A3 on the Novice track) and carries through every eval you ever build.
9. **Teach it back.** Self-test rule: you have learned something only if you can explain it in your own words, defend it against questions, and reproduce the reasoning with the AI closed. That is what the module quizzes (and the Novice pages' checkpoints) are for.
10. **Be generous.** The most upvoted self-taught story in the research credits "being generous helping others" for every opportunity he got. Answer questions in your community weekly.

## Escaping tutorial hell

- Watch at most one lecture before doing the matching build. Never two in a row.
- Reproduce 2 to 3 end-to-end projects yourself before asking for help (Vicki Boykis), so you learn the whole workflow: data, analysis, model choice, training, reading the loss.
- Pick tutorials that force you to change something and debug it. If you can copy-paste it, it is not teaching you.
- Keep a "frustration log" for a week (Chip Huyen). Pick one annoyance and ship a fix a friend can use. That is a better project than any tutorial.
- Failed projects count. Write up what broke.

## Using an AI assistant without losing the ability to think

- **Bring specific material.** Karpathy: "if you go to ChatGPT and you say, teach me AI... it's going to give you some slop." Paste the chapter, the repo, the error. Ask about that.
- **Ask for the next step, not the answer.** Raschka's prompt: "Don't give me the full solution, but what is something I could try?"
- **Use the tutor modes.** ChatGPT Study mode and Claude's Learning mode are built to guide instead of answer. Claude Code's "Learning" output style leaves pieces of the code for you to write.
- **Add friction.** Vicki Boykis: review the diff, run the SQL yourself, write the key parts by hand. "You should be learning, not the machine."
- **Do not let it write your curriculum.** Learn from vetted human material (the resources in this course). Use the model to explain, walk through examples, and quiz you.
- **Explain every line it writes.** Hiring managers reject people who cannot. The 1,500-upvote r/ExperiencedDevs thread is interviewers venting about exactly this.

## Reading a paper or a primary source

Every module ends with primary-source reading, and Track C replicates a paper. Read each one with four questions on a single page, in this order:

1. **Problem.** What was broken or unknown before this, in one sentence?
2. **Mechanism.** What does the method actually do, step by step, to the numbers? If you cannot draw it, you have not read it.
3. **Evidence.** Which table or figure carries the claim, what was the baseline, and how big is the gap compared with the noise?
4. **Limits.** What did the authors not test, and where would it break for your system?

Twenty minutes per paper is enough for the first pass. Save the page; the Module 13 depth probe and the Track C ablation both start from it.

## Memory

Spaced repetition works for the vocabulary and the derivations (attention formula, KV-cache size math, precision/recall definitions, the GRPO objective). Use Anki with one fact per card and do not create hundreds in one sitting. Put derivations on cards so they resurface while you are solving problems. The real practice happens in the projects, not the cards.

## A weekly routine that fits a job

Based on the roughly 10 hours a week the course assumes:

| Day | Time | What |
|---|---|---|
| Mon | 1 to 1.5h | Learn: one lecture or chapter section, notes in your own words |
| Tue | 1 to 1.5h | Build: the matching exercise, no video open |
| Wed | 1 to 1.5h | Build |
| Thu | 1 to 1.5h | Learn |
| Fri | 30 min | Anki, plus answer one question in your community |
| Sat | 3 to 4h | Build: the module project |
| Sun | 2 to 3h | Build, then 20 min writing up what you did and what broke |

Budget one bad week in four. If you miss a week, do not try to catch up. Resume.

Full-time learners should double the build time and leave the learn time alone.

## Sources

- Nathan Lambert, "My path into AI", 2025-05-14: https://www.interconnects.ai/p/my-path-into-ai
- Karpathy on Dwarkesh Podcast, 2025-10-17: https://www.dwarkesh.com/p/andrej-karpathy
- Karpathy's three learning rules, 2020: https://x.com/karpathy/status/1325154823856033793
- Raschka on Lex Fridman #490, Feb 2026: https://lexfridman.com/ai-sota-2026-transcript
- Chip Huyen, Business Insider, 2025-10-24: https://www.aol.com/articles/want-upskill-ai-former-nvidia-171247423.html
- Vicki Boykis, "How to learn ML in 2026", 2026-10-17: https://vickiboykis.com/2026/10/17/how-to-learn-ml-in-2026-interview/
- Hamel Husain and Shreya Shankar on evals, 2025-09-25: https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill
- ChatGPT Study mode: https://openai.com/index/chatgpt-study-mode/
- Anki background: https://docs.ankiweb.net/background.html
- Generosity (u/certain_entropy): https://www.reddit.com/r/MachineLearning/comments/ojp76r/comment/h546lvl/
