# Module 02: Math and classical ML as table stakes

## Prerequisites and measurable objectives

Prerequisite: Module 01. By the end you can:

1. Explain gradients, matrix multiplication as transformation, and the applied statistics (bias/variance, leakage, precision/recall/ROC-AUC) in your own words and on paper.
2. Frame a prediction problem, train a baseline and two models with cross-validation, choose a metric for a stated reason, and do error analysis on the worst cases.
3. Detect data leakage in grouped and time-ordered data.

**Primary resource:** Andrew Ng's Machine Learning Specialization, courses 1 and 2 (https://www.coursera.org/specializations/machine-learning-introduction). The concept block that names it says how much of it fits the guided hours; do that part before anything from the reading list, and treat the rest of it as unguided practice.
**Hours:** 10 guided: 9 on the concept blocks, 1 on the lab and the first pass of the build. Unguided practice on top is yours.

## Why only 10 hours

A machine learning engineer with ten years' experience said in July 2026 that 98% of classical model-tuning use cases went to cheap LLM API calls, and the middle of the market is being squeezed. But every interviewer still expects train/test splits, cross-validation, leakage and metrics cold, and the error-analysis habit you form here is the core of every LLM evaluation later. For the math, a FAANG staff engineer says he uses algebra plus intro statistics day to day; the 124-upvote top answer in the 2026 "what actually worked" thread says learn just enough and fill gaps as projects demand. That is the level here. Track C needs more and says so.

## Concepts, in order

1. **Linear algebra as intuition** (1 hour): vectors, matrices as transformations, dot products as similarity. 3Blue1Brown Essence of Linear Algebra, then write each idea in your own words.
2. **Just gradients** (1 hour): derivative, chain rule, gradient, why we step against it, what the learning rate does. 3Blue1Brown Essence of Calculus episodes 1 to 4 and the neural network series. Lab 01.
3. **Probability and applied statistics** (2 hours): distributions, expectation, conditional probability, Bayes, mean and variance, sampling; then bias/variance, overfitting, what a p-value means, precision, recall, F1, ROC-AUC, calibration. Khan Academy units and StatQuest.
4. **Classical ML the way scikit-learn does it** (3 hours): Andrew Ng's Machine Learning Specialization, course 1 weeks 1 and 2 at 1.5x with their labs inside these three hours, the rest of courses 1 and 2 as unguided viewing over the next weeks; scikit-learn pipelines, ColumnTransformer, cross_validate, the "Common pitfalls" page.
5. **Evaluation discipline** (1 hour): splits, stratification, k-fold, leakage in time series and grouped data, class imbalance, choosing the metric that matches the business decision.
6. **Error analysis** (1 hour): take the 30 worst predictions, read them one by one, categorise why they failed. This habit is what senior people say separates engineers from course-completers, and it carries straight into Module 08.

## Lab

`labs/lab01_gradient_descent.py`. Run it, read it, then write your own version from memory that fits a line and a logistic regression with NumPy only. Expected observations: the line converges to about w=2, b=1; the loss falls by about 250x; a 15x learning rate diverges to a loss above 10^20.

## Build

**Project 2: gradient descent from memory.** Your own NumPy version of lab 01: a line and a logistic regression that converge, and the 15x learning-rate divergence reproduced. This is the notebook Capability C2 asks for.

**Project 3: one tabular project done properly.** A messy real dataset (not Titanic or Iris; a city open-data portal, a low-activity Kaggle dataset, or data from your job):

- Problem framing in two paragraphs: unit of prediction, label, when it is known, the decision it drives, the cost of each error type
- A baseline (majority class or mean), two models compared with cross-validation, a metric chosen for a stated reason
- Error analysis: 30 worst cases categorised, one fix attempted, its effect measured
- A leakage note per feature: would this be known at prediction time?
- The best model behind an endpoint on your Module 01 service

**Deliverables:** the notebook, the endpoint, and a post explaining the biggest failure category and what you tried.

## Mastery gate

You can say, with numbers, why your model beats the baseline, where it fails, and what you would try next. You have also drawn gradient descent on paper for your reviewer.

## Quiz

1. Multiply a 2x3 matrix by a 3x1 vector on paper. What shape comes out, and what does the operation do geometrically?
2. What is a gradient, and why does subtracting a multiple of it reduce the loss?
3. Your model scores 99% accuracy on a 99/1 dataset. What is wrong and which metric would you use?
4. Explain bias versus variance with a story about fitting a curve to noisy points.
5. Describe three ways leakage happens and how to detect each.
6. Your precision is 0.9 and recall 0.2. Is that good? For which business would it be?
7. Why is cross-validation better than one split, and when can it still mislead you?

## Primary-source reading

- 3Blue1Brown linear algebra: https://www.3blue1brown.com/topics/linear-algebra
- Mathematics for Machine Learning (free PDF): https://mml-book.github.io
- Andrew Ng, Machine Learning Specialization: https://www.coursera.org/specializations/machine-learning-introduction
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- Staff MLE on day-to-day math: https://www.reddit.com/r/learnmachinelearning/comments/1d1u2aq/comment/l5wl4af/
- "Just enough math" top answer: https://www.reddit.com/r/learnmachinelearning/comments/1umfxxp/
- Classical ML squeezed: https://www.reddit.com/r/learnmachinelearning/comments/1uqymz7/comment/owc6cz1/

## Follow-ups

When you finish this module, paste one of these into your assistant. In Claude Code write `/aiexpert-tutor` before it; in Codex write `$aiexpert-tutor`.

1. Ask me to explain gradient descent in words, then correct what I got wrong.
2. Here is my baseline-versus-model table. Ask me where leakage could hide in my split.
3. Give me three leakage scenarios from my own project domain and let me find the split that avoids each.
