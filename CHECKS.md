# Citation check

Run on 2026-11-06 against 230 distinct URLs in 418 citations.

| Status | Count |
|---|---|
| OK | 175 |
| BLOCKED | 55 |

OK: reachable by this script. BLOCKED: the host refuses scripted clients (Reddit, X, Medium and similar); these were opened by hand during the research on 2026-11-04 and 2026-11-05. DEAD: 404 or 410, needs fixing. ERROR: timeout or TLS problem; retry before judging.


## BLOCKED, verified by a second method

These hosts refuse the plain checker and are not re-fetched with a disguised client. Every Reddit thread is cross-referenced against the research captures of 2026-11-04 (title, date, score as captured); every other URL carries a manual record of when and how it was verified. Methods: fetch-tool 1, research-capture 54.

| URL | Method | Evidence | Cited in |
|---|---|---|---|
| https://gordicaleksa.medium.com/how-i-got-a-job-at-deepmind-as-a-research-engineer-without-a-machine-learning-degree-1a45f2a781de | research-capture | research-capture on 2026-11-04: Opened in a browser during the vetting research on 2026-11-04 and recorded as the primary source for Aleksa Gordic in research/self_taught_ai_experts_reddit_vetted.json (vetting.status 'verified'); Medium returns HTTP 403 to both the plain checker and the fetch tool on 2026-11-05, so the page was not re-read today. | ADVANCED-TRACK.md, appendix/stories.md, modules/12-internal-move-and-public-work.md, modules/16-track-c-research.md, path-a-foundations/A6-get-in-the-door.md |
| https://news.ycombinator.com/item?id=49768826 | fetch-tool | fetch-tool on 2026-11-05: Read with the sanctioned fetch tool: title 'Ask HN: How do you interview devs in a post-AI world?', posted about 45 days before 2026-11-05; discussion of AI-allowed take-homes, explain-your-solution rounds and work trials, which is what Module 13 cites. The plain checker gets HTTP 419 (rate limit). | modules/13-interviews-2026.md |
| https://openai.com/index/chatgpt-study-mode/ | research-capture | research-capture on 2026-11-05: Fetched by the research agent on 2026-11-05 and recorded in research/practical_tips_beginner_2026-11-05.md item 16 (Study mode launched 2025-07-29, free tier included); openai.com returns HTTP 403 to the plain checker and the fetch tool, so the page was not re-read by this script. | appendix/how-to-study.md |
| https://www.reddit.com/r/AI_Agents/comments/1ta1cye/ | research-capture | thread 1ta1cye captured in research/ai_expert_path_2026.json on 2026-11-04: "10 things I'd tell anyone starting to build AI agents in production", posted 2026-05-11, score 9 | modules/09-agents-and-context.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/AI_Agents/comments/1xee1sh/ | research-capture | thread 1xee1sh captured in research/ai_expert_path_2026.json on 2026-11-04: 'A year away from agent work: how would you rebuild current depth in ag', posted 2026-10-24, score 2 | ADVANCED-TRACK.md |
| https://www.reddit.com/r/CUDA/comments/1t5txel/comment/oker8gc/ | research-capture | thread 1t5txel captured in research/ai_expert_path_2026.json on 2026-11-04: 'Building a career in AI infrastructure and inference engineering ,what', posted 2026-05-06, score 70 | ADVANCED-TRACK.md |
| https://www.reddit.com/r/CUDA/comments/1uwlc0r/comment/oxk528y/ | research-capture | thread 1uwlc0r captured in research/ai_expert_path_2026.json on 2026-11-04: 'Where would you get started with CUDA in 2026?', posted 2026-07-14, score 41 | ADVANCED-TRACK.md, modules/15-track-b-infra.md |
| https://www.reddit.com/r/CUDA/comments/1uwlc0r/comment/oxlicdi/ | research-capture | thread 1uwlc0r captured in research/ai_expert_path_2026.json on 2026-11-04: 'Where would you get started with CUDA in 2026?', posted 2026-07-14, score 41 | path-a-foundations/A7-choose-a-track.md |
| https://www.reddit.com/r/CUDA/comments/1vtngli/ | research-capture | thread 1vtngli captured in research/ai_expert_path_2026.json on 2026-11-04: 'What kind of projects actually stand out for GPU / compiler roles in 2', posted 2026-08-20, score 41 | ADVANCED-TRACK.md |
| https://www.reddit.com/r/ExperiencedDevs/comments/1wql3g2/comment/pc51suc/ | research-capture | thread 1wql3g2 captured in research/ai_expert_path_2026.json on 2026-11-04: 'Interviewed candidates for “AI engineer” roles this week, my god is th', posted 2026-09-26, score 1548 | appendix/stop-doing.md, modules/01-software-fundamentals.md, path-a-foundations/A1-code-and-systems.md |
| https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p01xbed/ | research-capture | thread 1v7z7e7 captured in research/ai_expert_path_2026.json on 2026-11-04: "What's the next high ticket skill for AI/LLM engineers?", posted 2026-07-27, score 36 | ADVANCED-TRACK.md |
| https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p03i3np/ | research-capture | thread 1v7z7e7 captured in research/ai_expert_path_2026.json on 2026-11-04: "What's the next high ticket skill for AI/LLM engineers?", posted 2026-07-27, score 36 | appendix/stop-doing.md, path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/LLMDevs/comments/1v7z7e7/comment/p052pym/ | research-capture | thread 1v7z7e7 captured in research/ai_expert_path_2026.json on 2026-11-04: "What's the next high ticket skill for AI/LLM engineers?", posted 2026-07-27, score 36 | appendix/stop-doing.md, modules/09-agents-and-context.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/LocalLLaMA/comments/1vi8jlr/comment/p2btrbo/ | research-capture | thread 1vi8jlr captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'Got job as Director of AI and Systems development self-taught', posted 2026-08-07, score 795 | appendix/stories.md, modules/11-fine-tuning.md, path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/MLQuestions/comments/1uhxdj3/comment/oulo013/ | research-capture | thread 1uhxdj3 captured in research/ai_expert_path_2026.json on 2026-11-04: 'Mid/Senior AI Engineers: What skills actually matter now?', posted 2026-06-28, score 21 | modules/17-expert-markers.md |
| https://www.reddit.com/r/MLQuestions/comments/1uhxdj3/comment/oun9yqi/ | research-capture | thread 1uhxdj3 captured in research/ai_expert_path_2026.json on 2026-11-04: 'Mid/Senior AI Engineers: What skills actually matter now?', posted 2026-06-28, score 21 | path-a-foundations/A7-choose-a-track.md |
| https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojovnqx/ | research-capture | thread 1t2n760 captured in research/ai_expert_path_2026.json on 2026-11-04: 'ML Career advice I wish I had as a FAANG engineer', posted 2026-05-03, score 54 | modules/17-expert-markers.md, path-a-foundations/A7-choose-a-track.md, path-a-foundations/A8-employed-to-expert.md |
| https://www.reddit.com/r/MLjobs/comments/1t2n760/comment/ojpng9u/ | research-capture | thread 1t2n760 captured in research/ai_expert_path_2026.json on 2026-11-04: 'ML Career advice I wish I had as a FAANG engineer', posted 2026-05-03, score 54 | ADVANCED-TRACK.md, modules/14-track-a-applied.md, path-a-foundations/A7-choose-a-track.md |
| https://www.reddit.com/r/MachineLearning/comments/1t6zdj6/comment/okm2arl/ | research-capture | thread 1t6zdj6 captured in research/ai_expert_path_2026.json on 2026-11-04: 'Disillusionment with mechanistic interpretability research [D]', posted 2026-05-08, score 74 | ADVANCED-TRACK.md, modules/16-track-c-research.md |
| https://www.reddit.com/r/MachineLearning/comments/ojp76r/comment/h546lvl/ | research-capture | thread ojp76r captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'Self Taught Machine Learning Engineers: Tell us how did you land a job', posted 2021-07-13, score 49 | appendix/how-to-study.md, appendix/stories.md, modules/12-internal-move-and-public-work.md, modules/17-expert-markers.md, path-a-foundations/A6-get-in-the-door.md, path-a-foundations/A8-employed-to-expert.md |
| https://www.reddit.com/r/MachineLearningJobs/comments/1u032xt/ | research-capture | thread 1u032xt captured in research/ai_expert_path_2026.json on 2026-11-04: 'What AI/ML projects actually impress recruiters in 2026?', posted 2026-06-08, score 12 | appendix/project-ladder.md |
| https://www.reddit.com/r/MachineLearningJobs/comments/1wllx1m/comment/pccba9q/ | research-capture | thread 1wllx1m captured in research/ai_expert_path_2026.json on 2026-11-04: 'AI/ML industry in 2026: What skills are companies looking for?', posted 2026-09-20, score 55 | modules/01-software-fundamentals.md, path-a-foundations/A1-code-and-systems.md |
| https://www.reddit.com/r/Rag/comments/1shqrwv/comment/ofhe7tp/ | research-capture | thread 1shqrwv captured in research/ai_expert_path_2026.json on 2026-11-04: 'Production RAG stack in 2026 what are people ACTUALLY running', posted 2026-04-10, score 87 | modules/07-retrieval.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/Rag/comments/1wbhsdi/comment/p8pycuc/ | research-capture | thread 1wbhsdi captured in research/ai_expert_path_2026.json on 2026-11-04: 'RAG vs Fine-tuning: What actually works better in production?', posted 2026-09-09, score 37 | appendix/stop-doing.md, modules/07-retrieval.md, modules/11-fine-tuning.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/datascience/comments/1hp7pim/ | research-capture | thread 1hp7pim captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'My Data Science Manifesto from a Self Taught Data Scientist', posted 2024-12-29, score 2077 | appendix/stories.md, path-a-foundations/A3-classical-ml.md |
| https://www.reddit.com/r/datascience/comments/713hnw/ | research-capture | thread 713hnw captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'How I went from no coding or machine learning experience to data scien', posted 2017-09-19, score 729 | appendix/stories.md, path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/deeplearning/comments/1swxb2k/ | research-capture | thread 1swxb2k captured in research/ai_expert_path_2026.json on 2026-11-04: 'I did 15 AI Engineer interviews in the last 6 months', posted 2026-04-27, score 447 | appendix/stop-doing.md, modules/10-cost-latency-security.md, modules/13-interviews-2026.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/ | research-capture | thread 1d1u2aq captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'I started my ML journey in 2015 and changed from software developer to', posted 2024-05-27, score 586 | path-a-foundations/A8-employed-to-expert.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/ | research-capture | thread 1d1u2aq captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'I started my ML journey in 2015 and changed from software developer to', posted 2024-05-27, score 586 | appendix/stories.md, modules/02-math-and-classical-ml.md, modules/04-attention-and-transformer.md, modules/12-internal-move-and-public-work.md, path-a-foundations/A2-just-enough-math.md, path-a-foundations/A4-llm-from-inside.md, path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1l4y3yy/comment/mwcpwb2/ | research-capture | thread 1l4y3yy captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'I started my ML journey in 2015 and changed from software engineer to ', posted 2025-06-06, score 356 | modules/17-expert-markers.md, path-a-foundations/A8-employed-to-expert.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1muc3g7/comment/n9jexx9/ | research-capture | thread 1muc3g7 captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'ML job without a degree', posted 2025-08-19, score 15 | modules/17-expert-markers.md, path-a-foundations/A8-employed-to-expert.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1nexb3h/ | research-capture | thread 1nexb3h captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'I self-taught myself math from zero to study ML at Uni, these are the ', posted 2025-09-12, score 522 | appendix/stories.md, path-a-foundations/A2-just-enough-math.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1pzcw2y/ | research-capture | thread 1pzcw2y captured in research/ai_expert_path_2026.json on 2026-11-04: 'From Software Developer to AI Engineer: The Exact Roadmap I Followed (', posted 2025-12-30, score 464 | appendix/stop-doing.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/odzfxx9/ | research-capture | thread 1sayf50 captured in research/ai_expert_path_2026.json on 2026-11-04: 'What should I actually know for ML Engineer interviews? (Looking for a', posted 2026-04-03, score 87 | appendix/project-ladder.md, modules/13-interviews-2026.md, path-a-foundations/A1-code-and-systems.md, path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/oe1p2gc/ | research-capture | thread 1sayf50 captured in research/ai_expert_path_2026.json on 2026-11-04: 'What should I actually know for ML Engineer interviews? (Looking for a', posted 2026-04-03, score 87 | path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1sayf50/comment/ofjavn4/ | research-capture | thread 1sayf50 captured in research/ai_expert_path_2026.json on 2026-11-04: 'What should I actually know for ML Engineer interviews? (Looking for a', posted 2026-04-03, score 87 | modules/05-training-scaling-inference.md, path-a-foundations/A4-llm-from-inside.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1t81t7i/comment/okswmh3/ | research-capture | thread 1t81t7i captured in research/ai_expert_path_2026.json on 2026-11-04: 'How do AI engineers actually evaluate LLM/RAG systems in practice?', posted 2026-05-09, score 52 | modules/08-evals.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1umfxxp/ | research-capture | thread 1umfxxp captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'For those who learned ML & got hired in the past 2-3 years - what actu', posted 2026-07-03, score 116 | modules/02-math-and-classical-ml.md, path-a-foundations/A2-just-enough-math.md, path-a-foundations/A7-choose-a-track.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owbthwt/ | research-capture | thread 1uqymz7 captured in research/ai_expert_path_2026.json on 2026-11-04: 'AI/ML Engineers: If you had to start from scratch in 2026, what roadma', posted 2026-07-08, score 51 | path-a-foundations/A1-code-and-systems.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owbvvsd/ | research-capture | thread 1uqymz7 captured in research/ai_expert_path_2026.json on 2026-11-04: 'AI/ML Engineers: If you had to start from scratch in 2026, what roadma', posted 2026-07-08, score 51 | path-a-foundations/A4-llm-from-inside.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owc6cz1/ | research-capture | thread 1uqymz7 captured in research/ai_expert_path_2026.json on 2026-11-04: 'AI/ML Engineers: If you had to start from scratch in 2026, what roadma', posted 2026-07-08, score 51 | appendix/stop-doing.md, modules/02-math-and-classical-ml.md, modules/09-agents-and-context.md, path-a-foundations/A3-classical-ml.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1vkco40/ | research-capture | thread 1vkco40 captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'Senior ML Engineers, how did you get your first ML job? Was it project', posted 2026-08-10, score 43 | path-a-foundations/A3-classical-ml.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1vkco40/comment/p2uj57j/ | research-capture | thread 1vkco40 captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'Senior ML Engineers, how did you get your first ML job? Was it project', posted 2026-08-10, score 43 | modules/12-internal-move-and-public-work.md, path-a-foundations/A6-get-in-the-door.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/ | research-capture | thread 1vqrx1n captured in research/ai_expert_path_2026.json on 2026-11-04: 'I trained three LLMs from scratch (353M–672M) and served them on HF Sp', posted 2026-08-17, score 159 | modules/05-training-scaling-inference.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/comment/p48miv4/ | research-capture | thread 1vqrx1n captured in research/ai_expert_path_2026.json on 2026-11-04: 'I trained three LLMs from scratch (353M–672M) and served them on HF Sp', posted 2026-08-17, score 159 | ADVANCED-TRACK.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1vqrx1n/comment/p494xck/ | research-capture | thread 1vqrx1n captured in research/ai_expert_path_2026.json on 2026-11-04: 'I trained three LLMs from scratch (353M–672M) and served them on HF Sp', posted 2026-08-17, score 159 | modules/06-post-training.md, path-a-foundations/A4-llm-from-inside.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1wwa0yj/comment/pdiwbwt/ | research-capture | thread 1wwa0yj captured in research/ai_expert_path_2026.json on 2026-11-04: "I was told MLOps is dead. I haven't even gotten the chance to learn ML", posted 2026-10-03, score 63 | appendix/stop-doing.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1xfkwyp/comment/19rnuzo541r8k/ | research-capture | thread 1xfkwyp captured in research/ai_expert_path_2026.json on 2026-11-04: 'SWE struggling to become productive in ML inference infrastructure. Ho', posted 2026-10-26, score 25 | ADVANCED-TRACK.md, modules/15-track-b-infra.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1xfkwyp/comment/19rnvkbisy9es/ | research-capture | thread 1xfkwyp captured in research/ai_expert_path_2026.json on 2026-11-04: 'SWE struggling to become productive in ML inference infrastructure. Ho', posted 2026-10-26, score 25 | ADVANCED-TRACK.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1xjpfuv/comment/19rwfb092sew5/ | research-capture | thread 1xjpfuv captured in research/ai_expert_path_2026.json on 2026-11-04: 'Title: AI Engineers working on RAG projects for 2–3 years, what do you', posted 2026-10-30, score 47 | modules/07-retrieval.md, path-a-foundations/A5-ai-engineering.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1xjpfuv/comment/19rxgf6mnaa1x/ | research-capture | thread 1xjpfuv captured in research/ai_expert_path_2026.json on 2026-11-04: 'Title: AI Engineers working on RAG projects for 2–3 years, what do you', posted 2026-10-30, score 47 | ADVANCED-TRACK.md, modules/14-track-a-applied.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1xn1n85/ | research-capture | thread 1xn1n85 captured in research/ai_expert_path_2026.json on 2026-11-04: 'Best resources to learn ML and AI engineering from scratch in 2026', posted 2026-11-03, score 49 | path-a-foundations/A3-classical-ml.md |
| https://www.reddit.com/r/learnmachinelearning/comments/1xn1n85/comment/19s3bs96u6ngj/ | research-capture | thread 1xn1n85 captured in research/ai_expert_path_2026.json on 2026-11-04: 'Best resources to learn ML and AI engineering from scratch in 2026', posted 2026-11-03, score 49 | path-a-foundations/A2-just-enough-math.md |
| https://www.reddit.com/r/phcareers/comments/vgfpw8/ | research-capture | thread vgfpw8 captured in research/self_taught_ai_experts_reddit_vetted.json on 2026-11-04: 'Self taught Data Scientist scores senior role', posted 2022-06-20, score 284 | path-a-foundations/A3-classical-ml.md |
| https://www.reddit.com/r/research/comments/1xlxffr/comment/19s151f29jrk3/ | research-capture | thread 1xlxffr captured in research/ai_expert_path_2026.json on 2026-11-04: 'How can I get into ML research as an 18-year-old CS student from a tie', posted 2026-11-02, score 2 | ADVANCED-TRACK.md |

## OK

| URL | Cited in |
|---|---|
| https://aimatterin.substack.com/p/a-codex-loop-ran-1500-submissions | ADVANCED-TRACK.md |
| https://aisec.engineering/ | ADVANCED-TRACK.md, README.md, modules/10-cost-latency-security.md |
| https://anirudhs16.github.io/ai-systems/2026/08/29/triton-first-gpu-kernel/ | ADVANCED-TRACK.md, modules/15-track-b-infra.md |
| https://arxiv.org/abs/1706.03762 | modules/04-attention-and-transformer.md |
| https://arxiv.org/abs/2001.08361 | modules/05-training-scaling-inference.md |
| https://arxiv.org/abs/2203.02155 | modules/06-post-training.md |
| https://arxiv.org/abs/2203.15556 | modules/05-training-scaling-inference.md |
| https://arxiv.org/abs/2406.03980 | ADVANCED-TRACK.md, modules/16-track-c-research.md |
| https://arxiv.org/abs/2501.12948 | modules/06-post-training.md |
| https://arxiv.org/abs/2601.06007 | ADVANCED-TRACK.md, modules/10-cost-latency-security.md |
| https://arxiv.org/abs/2605.22333 | ADVANCED-TRACK.md, modules/10-cost-latency-security.md |
| https://arxiv.org/abs/2607.16241 | ADVANCED-TRACK.md, appendix/resources.md, modules/15-track-b-infra.md |
| https://becomeaiexpert.com | deploy/cloudflare/README.md |
| https://blog.modelcontextprotocol.io/posts/2026-07-28/ | ADVANCED-TRACK.md, appendix/resources.md, modules/09-agents-and-context.md |
| https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/ | appendix/resources.md, modules/17-expert-markers.md |
| https://blog.nilenso.com/blog/2026/05/18/training-a-small-model-to-write-better-ocaml-with-rlvr-and-grpo/ | ADVANCED-TRACK.md, appendix/resources.md, modules/06-post-training.md, modules/16-track-c-research.md |
| https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf | modules/04-attention-and-transformer.md |
| https://chiraghasija.cc/posts/how-to-interview-ai-engineer-role-2026/ | appendix/stop-doing.md, modules/08-evals.md, modules/13-interviews-2026.md |
| https://course.fast.ai/ | appendix/compute-and-costs.md |
| https://creativecommons.org/licenses/by/4.0/ | LICENSE.md |
| https://creativecommons.org/licenses/by/4.0/legalcode | LICENSE.md |
| https://cs336.stanford.edu/ | appendix/resources.md, modules/05-training-scaling-inference.md, modules/06-post-training.md, path-a-foundations/A4-llm-from-inside.md |
| https://cs336.stanford.edu/spring2025/ | MEDIA-LIBRARY.md |
| https://cs50.harvard.edu/python/ | appendix/resources.md |
| https://developer.nvidia.com/blog/topping-the-gpu-mode-kernel-leaderboard-with-nvidia-cuda-compute/ | ADVANCED-TRACK.md, modules/15-track-b-infra.md |
| https://developers.openai.com/learn/evals | appendix/resources.md |
| https://discord.com/servers/gpu-mode-1189498204333543425 | appendix/communities.md |
| https://discuss.vllm.ai/t/where-to-start-for-implementing-custom-memory-block-aware-scheduling-in-vllm/2157 | ADVANCED-TRACK.md |
| https://docs.ankiweb.net/background.html | appendix/how-to-study.md |
| https://docs.docker.com/get-started/ | modules/01-software-fundamentals.md |
| https://docs.pytest.org/ | modules/01-software-fundamentals.md |
| https://docs.python.org/3/tutorial/ | modules/01-software-fundamentals.md |
| https://docs.vllm.ai/ | ADVANCED-TRACK.md, appendix/resources.md, modules/05-training-scaling-inference.md, modules/15-track-b-infra.md |
| https://docs.vllm.ai/en/stable/contributing/ | ADVANCED-TRACK.md, appendix/resources.md, modules/12-internal-move-and-public-work.md, modules/15-track-b-infra.md |
| https://eleuther.ai/community/ | ADVANCED-TRACK.md, appendix/communities.md, appendix/resources.md |
| https://evanjayconway.com/posts/2026/mats-application/ | ADVANCED-TRACK.md, appendix/communities.md, modules/16-track-c-research.md |
| https://example.com | deploy/cloudflare/README.md |
| https://exercism.org/docs/using/feedback/guide-to-being-mentored | appendix/communities.md |
| https://exercism.org/tracks/python | appendix/resources.md |
| https://fastapi.tiangolo.com/tutorial/ | modules/01-software-fundamentals.md |
| https://forums.fast.ai/t/fast-ai-discord/122405 | appendix/communities.md |
| https://georglange.com/post/ai-safety-application-guide/ | ADVANCED-TRACK.md, appendix/communities.md, appendix/project-ladder.md, appendix/resources.md, modules/12-internal-move-and-public-work.md, modules/16-track-c-research.md |
| https://github.com/alexeygrigorev/ai-engineering-field-guide | appendix/resources.md, modules/13-interviews-2026.md |
| https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/05-trends.md | modules/13-interviews-2026.md |
| https://github.com/gpu-mode/lectures | ADVANCED-TRACK.md, MEDIA-LIBRARY.md, appendix/resources.md, modules/15-track-b-infra.md |
| https://github.com/gpu-mode/lectures/tree/main/lecture_001 | MEDIA-LIBRARY.md |
| https://github.com/gpu-mode/lectures/tree/main/lecture_004 | MEDIA-LIBRARY.md |
| https://github.com/gpu-mode/popcorn-cli | ADVANCED-TRACK.md, appendix/resources.md, modules/15-track-b-infra.md |
| https://github.com/gpu-mode/reference-kernels | ADVANCED-TRACK.md |
| https://github.com/karpathy/nanochat | appendix/compute-and-costs.md, appendix/resources.md, modules/05-training-scaling-inference.md, path-a-foundations/A4-llm-from-inside.md |
| https://github.com/louisfb01/start-ai-engineering | appendix/project-ladder.md |
| https://github.com/pgvector/pgvector | modules/07-retrieval.md |
| https://github.com/rasbt/LLMs-from-scratch | MEDIA-LIBRARY.md |
| https://github.com/rasbt/reasoning-from-scratch | MEDIA-LIBRARY.md |
| https://github.com/stanford-cs336/assignment2-systems | ADVANCED-TRACK.md, appendix/resources.md, modules/15-track-b-infra.md |
| https://github.com/stanford-cs336/spring2025-lectures/blob/61eddac004df975466cff0329b615f2d24230069/nonexecutable/2025%20Lecture%2015%20-%20RLHF%20Alignment.pdf | MEDIA-LIBRARY.md |
| https://github.com/stanford-cs336/spring2025-lectures/blob/e94e33f433985e57036b25215dff2a4292e67a4f/nonexecutable/2025%20Lecture%2016%20-%20RLVR.pdf | MEDIA-LIBRARY.md |
| https://github.com/stanford-cs336/spring2025-lectures/blob/fb79eb018fa047bf99c4c785dcbbd62fff361e54/nonexecutable/2025%20Lecture%209%20-%20Scaling%20laws%20basics.pdf | MEDIA-LIBRARY.md |
| https://github.com/stanford-cs336/spring2025-lectures/blob/main/nonexecutable/2025%20Lecture%205%20-%20GPUs.pdf | MEDIA-LIBRARY.md |
| https://github.com/vetri02/become-an-ai-expert | AGENTS.md, ASSISTANT.md, README.md, labs/README.md, targets/README.md |
| https://github.com/vetri02/become-an-ai-expert.git | labs/README.md |
| https://github.com/vetri02/become-an-ai-expert/issues | LICENSE.md, README.md |
| https://hamel.dev/blog/posts/evals-faq/ | appendix/resources.md, modules/08-evals.md, path-a-foundations/A5-ai-engineering.md |
| https://hf.co/learn/agents-course | appendix/resources.md, modules/09-agents-and-context.md, path-a-foundations/A5-ai-engineering.md |
| https://hotfix.jobs/blog/ai-engineer-salary-2026 | path-a-foundations/A7-choose-a-track.md |
| https://huggingface.co/learn/agents-course/en/unit0/discord101 | appendix/communities.md |
| https://huggingface.co/learn/smol-course/en/unit0/1 | ADVANCED-TRACK.md, appendix/resources.md, modules/06-post-training.md, modules/11-fine-tuning.md, path-a-foundations/A4-llm-from-inside.md |
| https://karpathy.ai/zero-to-hero.html | MEDIA-LIBRARY.md, appendix/resources.md, modules/03-tokens-and-next-token.md, path-a-foundations/A4-llm-from-inside.md |
| https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/ | ADVANCED-TRACK.md, appendix/resources.md, modules/10-cost-latency-security.md, modules/14-track-a-applied.md |
| https://labscommunity.cohere.com/get-started | appendix/communities.md |
| https://lambda.com/service/gpu-cloud | appendix/compute-and-costs.md |
| https://langchain.com/state-of-agent-engineering | ADVANCED-TRACK.md, modules/07-retrieval.md, modules/14-track-a-applied.md |
| https://learn.arena.education/ | ADVANCED-TRACK.md, appendix/resources.md, modules/16-track-c-research.md |
| https://letsdatascience.com/news/levelsfyi-tells-lds-the-ai-pay-premium-has-stopped-growing-a893d96e | modules/13-interviews-2026.md, path-a-foundations/A7-choose-a-track.md |
| https://lexfridman.com/ai-sota-2026-transcript | ADVANCED-TRACK.md, appendix/how-to-study.md, appendix/project-ladder.md, appendix/stop-doing.md, modules/04-attention-and-transformer.md |
| https://lightning.ai/pricing | appendix/compute-and-costs.md |
| https://missing.csail.mit.edu/ | appendix/resources.md, modules/01-software-fundamentals.md |
| https://mml-book.github.io | appendix/resources.md, modules/02-math-and-classical-ml.md |
| https://modal.com/pricing | appendix/compute-and-costs.md |
| https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer | appendix/stories.md, modules/12-internal-move-and-public-work.md, modules/13-interviews-2026.md |
| https://podcasts.apple.com/us/podcast/108-chris-olah-on-working-at-top-ai-labs-without-an/id1245002988?i=1000531710782 | appendix/stories.md, modules/17-expert-markers.md, path-a-foundations/A8-employed-to-expert.md |
| https://research.google.com/colaboratory/faq.html | appendix/compute-and-costs.md |
| https://scikit-learn.org/stable/common_pitfalls.html | modules/02-math-and-classical-ml.md |
| https://scikit-learn.org/stable/getting_started.html | appendix/resources.md |
| https://sebastianraschka.com/llms-from-scratch | appendix/resources.md, modules/03-tokens-and-next-token.md, modules/04-attention-and-transformer.md, modules/11-fine-tuning.md, path-a-foundations/A4-llm-from-inside.md |
| https://sebastianraschka.com/reasoning-from-scratch | ADVANCED-TRACK.md, appendix/resources.md, modules/06-post-training.md, modules/16-track-c-research.md, path-a-foundations/A4-llm-from-inside.md |
| https://simonwillison.net/ | modules/17-expert-markers.md |
| https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | ADVANCED-TRACK.md, appendix/resources.md, modules/10-cost-latency-security.md, modules/14-track-a-applied.md |
| https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional | modules/17-expert-markers.md |
| https://tianpan.co/blog/2026/07/03/your-eval-suite-is-overfit-to-your-incumbent-model | ADVANCED-TRACK.md, modules/08-evals.md, modules/14-track-a-applied.md |
| https://vast.ai/pricing | appendix/compute-and-costs.md |
| https://vickiboykis.com/2026/10/17/how-to-learn-ml-in-2026-interview/ | appendix/communities.md, appendix/how-to-study.md, appendix/project-ladder.md, modules/03-tokens-and-next-token.md |
| https://vllm.ai/blog/2026-03-13-p-eagle | ADVANCED-TRACK.md, modules/15-track-b-infra.md |
| https://www.3blue1brown.com/topics/linear-algebra | appendix/resources.md, modules/02-math-and-classical-ml.md |
| https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | ADVANCED-TRACK.md, appendix/resources.md, modules/08-evals.md, modules/09-agents-and-context.md, modules/14-track-a-applied.md, path-a-foundations/A5-ai-engineering.md |
| https://www.anthropic.com/research/AI-resistant-technical-evaluations | modules/13-interviews-2026.md |
| https://www.anthropic.com/research/effective-context-engineering-for-ai-agents | ADVANCED-TRACK.md, appendix/resources.md, modules/07-retrieval.md, modules/09-agents-and-context.md, path-a-foundations/A5-ai-engineering.md |
| https://www.aol.com/articles/want-upskill-ai-former-nvidia-171247423.html | appendix/how-to-study.md, appendix/project-ladder.md |
| https://www.arena.education/ | ADVANCED-TRACK.md, appendix/communities.md, modules/16-track-c-research.md |
| https://www.coursera.org/specializations/machine-learning-introduction | appendix/resources.md, modules/02-math-and-classical-ml.md |
| https://www.dataquest.io/blog/machine-learning-projects-for-beginners-to-advanced/ | appendix/project-ladder.md |
| https://www.dwarkesh.com/p/andrej-karpathy | appendix/how-to-study.md, appendix/stop-doing.md |
| https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0 | ADVANCED-TRACK.md, appendix/resources.md, modules/15-track-b-infra.md |
| https://www.firsttimersonly.com/ | appendix/communities.md |
| https://www.interconnects.ai/p/my-path-into-ai | appendix/how-to-study.md, appendix/stories.md |
| https://www.latent.space/p/fastai | appendix/stories.md |
| https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill | appendix/how-to-study.md, appendix/project-ladder.md |
| https://www.lesswrong.com/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher | ADVANCED-TRACK.md, appendix/resources.md, modules/16-track-c-research.md |
| https://www.louisbouchard.ai/context-engineering-2026/ | ADVANCED-TRACK.md, modules/09-agents-and-context.md, modules/10-cost-latency-security.md |
| https://www.matsprogram.org/ | ADVANCED-TRACK.md, appendix/resources.md |
| https://www.matsprogram.org/faq/getting-into-mats | ADVANCED-TRACK.md, appendix/communities.md, appendix/resources.md, modules/16-track-c-research.md |
| https://www.neelnanda.io/whirlwind-slides | MEDIA-LIBRARY.md |
| https://www.oreilly.com/library/view/ai-engineering/9781098166298 | appendix/resources.md, modules/07-retrieval.md, path-a-foundations/A5-ai-engineering.md |
| https://www.promptfoo.dev/blog/model-upgrades-break-agent-safety/ | ADVANCED-TRACK.md, modules/10-cost-latency-security.md, modules/14-track-a-applied.md |
| https://www.promptfoo.dev/docs/category/guides/ | appendix/resources.md, modules/08-evals.md, path-a-foundations/A5-ai-engineering.md |
| https://www.runpod.io/pricing | appendix/compute-and-costs.md |
| https://www.shrm.org/in/topics-tools/research/2026-ld-executives-benchmarking--developing-critical-talent/full-report | appendix/compute-and-costs.md |
| https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026 | appendix/compute-and-costs.md, modules/11-fine-tuning.md |
| https://www.thundercompute.com/blog/google-colab-alternatives | appendix/compute-and-costs.md |
| https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr | MEDIA-LIBRARY.md |
| https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=237Hf7Q3lgg | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=3E_jDJST69s | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=46f2QTDB08Q | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=4jRBRDbJemM | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=4sgKnKbR-WE | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=4yNswvhPWCQ | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=5ZlavKF_98U | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=6OBtO9niT00 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=6Q-ESEmDf4Q | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=7xTGNNLPyMI | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=9-Jl0dxWQs8 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=9tvJ_GYJA-o | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=9wNAgpX6z_4 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=BJua0yjO5dk | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=BsWxPI9UM4c | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=D7_ipDqhtwk | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=Dfu7vC9jo4w | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=E8Mju53VB00 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=EuBBz3bI-aA | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=FgxwCaL6UTA | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=GL0XhAj5LPE | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=Kdsp6soqA7o | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=LCEmiRjPEtQ | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=LuhJEEJQgUM | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=NQ-0D5Ti2dc | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=P6sfmUTpUmc | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=PaCmpygFfXo | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=SQ3fZ1sAqXI | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=TCH_1BHY58I | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=VMj-3S1tku0 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=XQylGyG7yp8 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=YEaKXjHENyQ | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=YpY83-kA7Bo | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=aircAruvnKk | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=eMlx5fFNoYc | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=fZH97QHHYjY | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=fcgPYo3OtV0 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=icGHT7MiaFY | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=jQcsVk0KWiQ | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=jryZvCuA0Uc | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=kCc8FmEb1nY | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=l8pRSuU81PU | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=lTmYrKwjSOU | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=qbvY0dQgSJ4 | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=quh7z1q7-uc | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=uhJJgc-0iTQ | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=veT2VI4vHyU | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=wjZofJX0v4M | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=x-R5l2HsXqM | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=ysPbXH0LpIE | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=zduSFxRajkE | MEDIA-LIBRARY.md |
| https://www.youtube.com/watch?v=zjkBMFhNj_g | MEDIA-LIBRARY.md |
| https://x.com/karpathy/status/1325154823856033793 | appendix/how-to-study.md |
| https://x.com/karpathy/status/2017703360393318587 | appendix/compute-and-costs.md |
