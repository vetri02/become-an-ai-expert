# Study with an AI assistant

You will use an assistant throughout the course. These are the rules that keep it a tutor rather than a substitute, drawn from Karpathy, Raschka and Vicki Boykis, and from the hiring managers who reject people who cannot explain their own code.

## What the assistant does

- Explains a specific passage, error or line of code you paste in.
- Quizzes you on a module's quiz questions and grades your spoken answers.
- Suggests the next thing to try when you are stuck, without giving the solution.
- Reviews a write-up for clarity.

## What it will not do here

- Write your curriculum. The modules name vetted human material; the assistant explains it.
- Write the labs, targets, milestones or capstone for you. Every line you submit, you must be able to explain to a reviewer.
- Replace error analysis. You read the 20 to 50 outputs yourself. The assistant can help categorise after you have labelled.

## Setting it up

Use a tutor mode where one exists: ChatGPT Study mode, Claude's Learning mode, or Claude Code's "Learning" output style, which leaves pieces of code for you to write. Otherwise start every session with this instruction:

```
You are my tutor for a self-study course in AI engineering. Do not give full solutions.
When I am stuck, ask me what I have tried, then suggest one next step.
When I paste code, ask me to explain it before you comment.
Quiz me on concepts in my own words and tell me what I got wrong.
```

## In Claude Code or Codex

The course ships a tutor skill that knows the modules, the labs, the graders and the rules above. It is one markdown file, and there are two ways to get it.

1. **Get the whole course**: clone [github.com/vetri02/become-an-ai-expert](https://github.com/vetri02/become-an-ai-expert) or download it as a zip, [become-an-ai-expert.zip](https://github.com/vetri02/become-an-ai-expert). Open the folder in Claude Code or Codex, and the skill is already in place at `.claude/skills/aiexpert-tutor/` (Codex reads the same file through `.agents/skills/aiexpert-tutor/`). The folder also holds the labs, the targets and `AGENTS.md`, which tells any assistant not to do your work for you.
2. **Download only the skill**: [SKILL.md](.claude/skills/aiexpert-tutor/SKILL.md). Save it as `.claude/skills/aiexpert-tutor/SKILL.md` (Claude Code) or `.agents/skills/aiexpert-tutor/SKILL.md` (Codex) inside the folder where you keep your course work. The skill expects the course files beside it, so the clone or the zip is the better route.

Open the folder, and `/aiexpert-tutor` appears in Claude Code's skill list.

Start:

```
/aiexpert-tutor I am new. Give me the diagnostic, then tell me where to start.
```

Resume in a later session:

```
/aiexpert-tutor Read my progress file and resume the next unfinished step. Quiz me on the last module before we move on.
```

Every module ends with three follow-up prompts written for this skill: a quiz, a review of what you built, and a role-play. In Codex, write `$aiexpert-tutor` in place of `/aiexpert-tutor`. The skill keeps your progress in `.aiexpert-progress.json` and only marks a step complete when you say you have met its mastery gate.

## How to use it well

- Bring specific material. "Teach me AI" produces slop; "explain line 31 of this attention function" produces learning.
- Raschka's prompt: "Don't give me the full solution, but what is something I could try?"
- Add friction: review the diff, run the SQL yourself, retype the key parts by hand.
- Close the assistant for the quiz, the mastery gate and the exam. If you cannot do it with the assistant closed, you have not learned it yet.
- For peer review, the assistant may play reviewer only in the solo variant and only after you have scored yourself first.
