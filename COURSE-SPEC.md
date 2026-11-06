# Course specification

This file fixes what the course is, who it is for, how big it is, and the standards every page is held to. Everything else in the folder is checked against it.

The three values below were supplied by the course owner on 2026-11-05: **subject "AI engineering with LLMs"; audience "working professionals with no prior ML background"; size 200 hours** (the owner first confirmed 500 and then asked for a shorter course; 200 is the guided core). The owner registered the seven standards below as the ones that govern every decision.

## Subject

**AI engineering with LLMs**: how large language models work from the inside, how to build systems on them (retrieval, agents, fine-tuning), how to evaluate and operate those systems with measurements, and how to go deep in one of three specialisms (applied products, inference infrastructure, research engineering). The working title is "Become an AI Expert"; "expert" means the top of one specialism.

## Audience

**Working professionals with no prior ML background.** Software engineers, data analysts and scientists, data and platform engineers. They can learn a library in a weekend and have never trained a model or built an evaluation. The numbered modules are the Professional track; the Novice track (Path A) is the on-ramp into it.

Path A is an optional on-ramp for readers who do not yet have the professional's software and math base. It adds about 210 hours of foundations (code and systems, just-enough math, classical ML) in front of the same core, and is kept in the folder because the research shows beginners reach the same place by the same route, more slowly. It is not part of the 200-hour course.

## Size

**200 hours.** That budget delivers: employable in an AI engineering role or an adjacent role that leads to one; a chosen specialism; a public record of evaluated work. HOURS.md allocates it per module and sums exactly.

Track depth after the core is open-ended (300 to 900 hours to employable depth in the specialism, years to expert) and is scoped in the track guides rather than counted here. The Path A on-ramp adds about 210 hours in front for readers starting from zero.

## Standards that govern every decision

1. **First principles over received claims.** FIRST-PRINCIPLES.md holds the 20 facts the subject rests on, each derived from how the thing works, mapped to the module that teaches it, the lab that demonstrates it, and the best single source. Any module claim that contradicts a principle is wrong.

2. **Everything described must run or be reproducible.** Every procedure the course tells the learner to do is either a lab in `labs/` that runs with one command on a laptop, or a project with a stated environment, cost and "done when" bar. `labs/run_all.sh` must pass before any publish.
3. **Everything cited must be checked.** Every resource was verified to exist and be current at the dates stated. `checks/check_links.py` fetches every URL in the course and writes CHECKS.md; dead or blocked links are listed there, not hidden.
4. **Capability with evidence, not recitation.** CAPABILITIES.md lists what the learner must be able to do, the artifact that proves each one, and the bar it must clear. Checkpoint questions are oral, with nothing open.
5. **Dated, sourced, and honest about evidence quality.** Prices, pay, tools and timelines are contingent and carry a date. Anonymous and vendor sources are labelled. Survivorship bias is stated where it applies.
6. **One primary resource per topic.** Every module opens with a "Primary resource" line naming the one thing to finish; the reading list is optional, because the practitioners the course draws on say bouncing between resources is the common failure.
7. **Build before breadth.** Every module ends in an artifact a stranger can run or read, and the public trail of those artifacts is the hiring strategy.

## Files

| File | Role |
|---|---|
| COURSE-SPEC.md | This file |
| FIRST-PRINCIPLES.md | Standard 1 |
| labs/ and targets/ | Standard 2 |
| checks/ and CHECKS.md | Standard 3 |
| CAPABILITIES.md | Standard 4 |
| HOURS.md | Size |
| README.md, COURSE-GUIDE.md, modules/, assessments/, labs/, targets/, CAPSTONE.md | The 200-hour course |
| path-a-foundations/ | The optional on-ramp |
| site/build.py, site/template.html, site/index.html | The browsable version |
| ../research/ | The evidence base |
