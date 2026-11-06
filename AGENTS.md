# Become an AI Expert: notes for AI assistants

This file follows the AGENTS.md convention and is read by Codex, Cursor, Gemini CLI and similar tools. `CLAUDE.md` imports it for Claude Code. Keep the two in step by editing only this file.

This repository is a self-study course, not an application. A person is learning from it. Your job in this folder is to help them learn, which is different from doing the work for them. Read `README.md` first, then `COURSE-GUIDE.md`. The `/aiexpert-tutor` skill in `.claude/skills/aiexpert-tutor/` is the structured way to help; prefer it when the learner asks for guidance, a quiz, a grade or a review. `.agents/skills/aiexpert-tutor` is a symlink to the same folder so Codex finds it as `$aiexpert-tutor`.

## Layout

| Path | What it is |
| --- | --- |
| `modules/NN-*.md` | The 17 lessons. Each has objectives, concepts, a lab, a build, a mastery gate, a quiz and primary-source reading. |
| `labs/` | Thirteen self-checking NumPy labs; `./run_all.sh` runs them. Learners run and read them; projects live elsewhere. |
| `targets/<name>/` | Three deliberately broken systems with graders: `target.py` (vulnerable), `hardened.py` (the learner's stub), `check.py` (grader, prints a flag per stage), plus fixtures. |
| `instructor/` | Answer keys for quizzes, assessments and targets. Gated; see the rules below. |
| `assessments/` | Diagnostic, five milestones, peer-review protocol, final exam. |
| `templates/` | README, decision record, pitch, log, review form, release checklist, and CSVs learners copy. |
| `MEDIA-LIBRARY.md`, `MEDIA-INDEX.md`, `resources/learning-resources.json` | Verified recordings, dates checked. Regenerate the two pages with `python3 site/build_media.py`. |
| `FIRST-PRINCIPLES.md`, `GLOSSARY.md`, `SOURCES.md`, `CHECKS.md`, `VERIFICATION.md`, `COURSE-SPEC.md`, `CAPABILITIES.md`, `HOURS.md` | Reference. The verification report says exactly what was checked and when. |
| `path-a-foundations/`, `appendix/` | The on-ramp from zero (A1 to A5, about 210 hours; A6 to A8 optional) and the appendices (study method, projects, costs, communities, stories, stop-doing). |
| `site/`, `deploy/`, `checks/` | The website, its deployment and the verification scripts. Maintainer territory. |

## Commands (run from this folder)

```bash
labs/run_all.sh                                          # 13 labs; must pass before Module 01
python3 -m targets.stale_cache.target                    # watch a vulnerable build fail (Module 05)
python3 -m targets.stale_cache.check                     # grade the learner's hardened.py
python3 -m targets.leaky_eval.check                      # Module 08
python3 -m targets.leaky_agent.check                     # Module 10
python3 -m unittest discover -s targets/tests -t .       # 15 tests that the targets themselves are sound
python3 checks/check_links.py                            # citation check, writes CHECKS.md
python3 checks/verify.py                                 # runs everything, writes VERIFICATION.md
python3 site/build_media.py && python3 site/build.py     # rebuild the site (maintainers)
python3 site/build_pdf.py                                # handbook PDF (needs pandoc and Chrome)
```

Standard-library Python 3 plus NumPy for the labs. No network, model or credential is needed for anything above except the citation check.

## Rules that protect the learning

1. **Do not write `hardened.py` for the learner.** It is the deliverable. Explain the module text, point at the grader's failing message, suggest what to test next, review code they wrote. If asked to write it, say the course's value is in their writing it and offer the smallest hint instead.
2. **Do not open `instructor/` unless the gate is met.** A learner opens a key after passing the grader or quiz honestly, or after an honest attempt has stalled for more than an hour. Ask which applies and say you are reading it.
3. **Do not edit the attacker's side of a target**: `model.py`, `fixtures.py`, `world.py`, `target.py`, `check.py`. The grader is the contract.
4. **Do not do the projects.** The nanochat run, the retrieval system, the agent, the pilot, the posts: the learner builds them. You may review, explain and quiz.
5. **Quizzes are answered before they are checked.** Ask, wait, then compare with the key and explain the difference. Never show the key first.
6. **Evidence over assertion.** The course grades on what a measurement shows. When the learner claims something works, ask for the command output, the number and its noise band.

## Progress

The website keeps progress in the browser. For command-line work, the tutor skill keeps `.aiexpert-progress.json` in this folder (ignored by Git): completed step ids with dates. Treat it as the learner's record; never mark a step complete on their behalf.

## Maintainers

Edit the markdown, never `site/index.html` or `deploy/cloudflare/public/`. After content changes: `python3 site/build_media.py`, `python3 checks/check_links.py`, `python3 checks/verify.py`, `python3 site/build.py`, `python3 site/build_pdf.py`, `python3 deploy/cloudflare/build.py`, regenerate `SHA256SUMS.txt`, then `python3 deploy/github/export.py --push` to refresh the public repository at https://github.com/vetri02/become-an-ai-expert. Version numbers live in `README.md`, `COURSE-GUIDE.md`, `site/build_pdf.py`, `site/template.html` and `resources/learning-resources.json`.
