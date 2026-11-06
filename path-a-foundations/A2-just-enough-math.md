# A2. Just-enough math

**Track:** Novice (Path A, the on-ramp from zero)
**Time:** about 20 guided hours, run alongside A1. Longer if you are starting from arithmetic.
**Goal:** Understand what a model is doing when it trains. Not prove theorems.
**Principles:** Principle 3 (learning is gradient descent through the chain rule). Lab 01 shows it.

## How much is enough

The vetted stories split cleanly. For engineering roles, a staff ML engineer at a FAANG company says he mostly uses algebra plus intro statistics day to day. The highest-voted answer (124 points) in the 2026 "what actually worked" thread says learn just enough, then fill gaps when a project demands it. For research roles the answer is different: deep math matters, and the one person who went from no schooling past 6th grade to studying ML at ETH Zurich did it by re-learning math from arithmetic up with Khan Academy mastery challenges and textbooks.

This module targets the engineering level. Module A7 track C tells you how to go further if you choose research.

## Learn

1. **Linear algebra, as intuition.** Vectors, matrices, matrix multiplication as transformation, dot products as similarity. This is what embeddings and attention are.
   - 3Blue1Brown, "Essence of Linear Algebra" (about 3 hours of video). Watch each episode, then write the idea in your own words.
2. **Calculus, just gradients.** What a derivative is, the chain rule, what a gradient is and why we step against it.
   - 3Blue1Brown, "Essence of Calculus" episodes 1 to 4, then the neural network series (4 videos).
3. **Probability and statistics, the parts models use.** Probability distributions, expectation, conditional probability, Bayes' rule, mean/variance, the normal distribution, sampling. Then the applied ML stats: bias/variance, overfitting, p-values at the "what does it mean" level, and metrics (precision, recall, F1, ROC-AUC).
   - Khan Academy "Statistics and probability" units on probability and distributions.
   - StatQuest (Josh Starmer) videos on bias/variance, ROC, and confusion matrices.
4. **If you need to go from zero.** Khan Academy from pre-algebra up, using mastery challenges, before any of the above. Budget 3 to 6 months. One Redditor did exactly this to pass a university entrance exam at 29.
5. **Reference book to keep open.** "Mathematics for Machine Learning" (Deisenroth, Faisal, Ong), free PDF. Do not read it cover to cover. Open it when a later module uses a term you do not know.

## Build

**Project A2: gradient descent by hand.**
In a notebook with only NumPy:
- Fit a straight line to 50 noisy points by computing the gradient of mean squared error yourself and stepping
- Plot the loss curve and the fitted line
- Then fit a 2-feature logistic regression the same way
- Write one paragraph explaining what the learning rate did when you set it 10x too high

**Done when:** you can draw, on paper, what gradient descent is doing and why the loss curve bends.

**Runnable reference:** `labs/lab01_gradient_descent.py` does exactly this (line fit, logistic fit, and a divergence at 15x learning rate) with assertions. Run it, read it, then write yours without looking.

## Skip for now

- Full calculus or linear algebra courses before touching a project.
- Measure theory, information theory, convex optimization. Only Track C needs these.
- Proving anything.

## Checkpoint

1. Multiply a 2x3 matrix by a 3x1 vector on paper. What shape comes out and why?
2. What is a gradient? Why do we subtract it?
3. Your model scores 99% accuracy on a dataset where 99% of rows are one class. What is wrong, and which metric would you use instead?
4. Explain bias vs variance using a story about fitting a curve.

## Sources

- Staff MLE: "mostly algebra plus intro stats": r/learnmachinelearning AMA 2024/2025, https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/
- "Just enough math" top answer (u/patternpeeker, 124 pts) in "what actually worked" thread, Jul 2026, https://www.reddit.com/r/learnmachinelearning/comments/1umfxxp/
- Math from zero to ETH entrance exam (u/obolli): r/learnmachinelearning, Sep 2025, https://www.reddit.com/r/learnmachinelearning/comments/1nexb3h/
- 2026 roadmap thread, 3Blue1Brown and Khan Academy recommendations: https://www.reddit.com/r/learnmachinelearning/comments/1xn1n85/comment/19s3bs96u6ngj/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me to explain a derivative, a dot product and a conditional probability in plain words, then correct me.
2. Give me three gradient-descent problems to work by hand and check my steps.
3. Ask questions until we find the math gap behind my A2 build.
