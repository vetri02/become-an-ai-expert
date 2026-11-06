# Sources and version notes

Prepared 5 November 2026. Every URL in the course was fetched by `checks/check_links.py`; the result is in [CHECKS.md](CHECKS.md). Hosts that refuse scripted clients (Reddit, X, Medium and similar) were opened by hand on 4 and 5 November 2026.

## The evidence base

- `../research/ai_expert_path_2026.json`: 28 Reddit threads dated October 2025 to November 2026, every named resource verified on the web; the roadmap's structure and the "stop doing" list come from here.
- `../research/self_taught_ai_experts_reddit_vetted.json`: 22 threads, 2017 to 2026; each named person checked against primary sources (personal sites, interviews, Wikipedia, 80,000 Hours); anonymous accounts labelled unverified.
- `../research/practical_tips_beginner_2026-11-05.md` and `../research/practical_tips_professional_2026-11-05.md`: about 90 tips from practitioner write-ups, podcasts and lab guides, with vendor sources flagged.

## Primary resources, by stage

Full table with verified status: [appendix/resources.md](appendix/resources.md).

- Foundations: Python tutorial, pytest, FastAPI, Docker, MIT Missing Semester, Exercism; 3Blue1Brown; Khan Academy; StatQuest; Mathematics for Machine Learning (free PDF); Andrew Ng's Machine Learning Specialization; scikit-learn's common pitfalls.
- The model: Karpathy's Zero to Hero and nanochat; Raschka's two from-scratch books; Stanford CS336 (Spring 2026 lectures and assignments); Hugging Face smol-course; the Transformer, GPT-2, Chinchilla, InstructGPT and DeepSeek-R1 papers.
- AI engineering: Hamel Husain and Shreya Shankar's evals FAQ; Anthropic's agent-evals and context-engineering guides; Chip Huyen's AI Engineering; promptfoo; the MCP specification; Simon Willison on the lethal trifecta; the Cloud Security Alliance's MCP guidance; the prompt-caching and compaction-cost studies; the MCP authentication measurement study.
- Infrastructure: vLLM docs and contributing guide; GPU MODE lectures and leaderboard; PMPP; CS336 assignment 2; KernelBench-Verified.
- Research: ARENA; Neel Nanda's guide; MATS and its admissions FAQ; Georg Lange's application guide; the nilenso GRPO write-up.
- Careers: Pragmatic Engineer (Janvi Kalra); Hacker News hiring-manager thread (September 2026); Anthropic on AI-resistant take-homes; Grigorev's field guide; Levels.fyi and posted-range analyses.

## Dated and contingent claims

Prices (compute appendix), pay (Modules 13 and 17, ADVANCED-TRACK), demand signals and tool names carry the date they were checked. Treat anything older than six months as a prompt to re-check.

## Vendor and promotional sources

Marked where used: course vendors for time estimates, GPU clouds for prices, a tool vendor's agent-engineering survey, a payments-era recruiter blog on take-homes, and speakers who sell a book or a course. Their mechanisms are used; their numbers are cross-checked or flagged.

## Version notes

- 1.0, 2026-11-05: two paths, three tracks, seven appendices.
- 1.1, 2026-11-05: first principles, 13 labs, capabilities, hours, citation check.
- 2.0, 2026-11-05: restructured as a staged path with 17 modules, quizzes and keys, 5 milestones, 3 targets, diagnostic, bridge, peer review, capstone, final exam, media catalogue (54 recordings), templates, glossary, verification report, handbook PDF, tutor skill.
- 2.1, 2026-11-05: resized to 200 guided hours; modules, concept blocks and capstone rescaled.
