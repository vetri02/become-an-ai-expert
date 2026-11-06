# Peer review protocol

Every milestone and the capstone are reviewed. A review is the cheapest way to get the "people better than me consistently reviewed my code" effect that Vicki Boykis credits for her growth, and it is practice for the depth probe in interviews.

## Why a review loop

Self-taught learners stall when nobody checks their work. A reviewer who follows this procedure catches the two failures the course cares about most: claims without numbers, and numbers without a method.

## Pairing

Find a partner in the communities appendix (Hugging Face Discord, the study servers, a local meetup) who is within two stages of you. Swap milestone submissions. If you cannot find one, use the solo variant.

## The reviewer's procedure

1. Read the submission checklist first and tick what is present. Score missing items zero rather than estimating them.
2. Run anything runnable. A repo that does not run in three commands fails criterion 3.
3. Pick one number in the write-up and trace it to the code or data that produced it.
4. Ask three "why" questions in writing. The author answers in writing.
5. Score with the rubric. Write one paragraph: the strongest thing, the weakest thing, one change that would raise the score most.

## Rubric, twenty points

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 1. Evidence: every claim has a number or an artifact | Claims only | Some numbers, method unclear | Numbers with method and data stated |
| 2. Evaluation: held-out, versioned, measured separately where the course requires | Eyeballed | A test set exists | Golden set versioned; retrieval and generation separate; judge calibrated if used |
| 3. Reproducibility: a stranger can run it | Does not run | Runs with help | Three commands, documented |
| 4. Failure analysis: what breaks and why | None | A list | Categorised with examples and what was tried |
| 5. Explanation: the author can answer "why" three levels deep | Cannot | Two levels | Three levels, in writing |

14 of 20 passes. Below 14, the author revises and resubmits once.

## Calibration, before the first review

Both partners score the same sample milestone (one partner's Milestone A submission, scored against the criteria on the milestones page) independently and compare. Disagreements of more than 2 points on any criterion are discussed until the criterion is understood the same way.

## Author's response

Within a week, the author writes what they changed and what they chose not to change, with reasons. This response is part of the public record.

## Solo variant

If you have no partner: wait seven days after finishing a milestone, then review it yourself using the procedure, with the assistant playing the questioner for step 4 only. Be harsher than you want to be. Record the score.

## What the loop does not do

It does not certify you. It does not replace a real code review at work. It makes your evidence legible, which is the point.
