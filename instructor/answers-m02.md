### Answer key: Module 02

### Quiz answers and reasoning

1. 2x1. The matrix maps a point in 3-dimensional space to a point in 2-dimensional space; each output component is a dot product of a row with the vector.
2. The vector of partial derivatives of the loss with respect to each parameter. It points in the direction of steepest increase, so for a small enough step, moving against it lowers the loss (first-order Taylor argument). Too large a step overshoots, which lab 01 shows.
3. The majority-class predictor already scores 99%, so accuracy says nothing. Use precision, recall, F1 or ROC-AUC with a confusion matrix, chosen by the cost of false positives versus false negatives.
4. A straight line through curvy data misses the shape everywhere (high bias, underfit). A wiggly curve through every point follows the noise and changes completely with a new sample (high variance, overfit). The right complexity sits between, found with validation data.
5. (a) Target leakage: a feature that encodes the label (an "account closed" flag predicting churn); detect by asking whether it is known at prediction time. (b) Train/test contamination: duplicates or the same entity in both; detect with group-aware splits. (c) Temporal leakage: future rows in training; detect with time-ordered splits and features computed only from the past.
6. It depends on the decision. Precision 0.9, recall 0.2 is fine for a system that flags a few sure fraud cases for manual review, and terrible for a screening test that must not miss cases.
7. Cross-validation uses every row for validation across folds, so the estimate has less variance than one split. It still misleads with leakage across folds (grouped or time data), with tuning on the folds (needs nested CV), and when the data is not representative of production.

### Lab assessment and mastery gate

The reviewer picks one feature and asks "would you know this at prediction time?"; a wrong answer fails the gate. They pick one number from the write-up and trace it to the notebook. They ask for the gradient-descent drawing.

### How to use this key

Open after writing all seven answers. Strict marking. Question 5 is asked in nearly every interview.
