"""Lab 01: gradient descent by hand (Module 02, or A2 on the Novice track; Principle 3).

Fits a line and then a logistic regression using only NumPy and the chain rule.
No autograd. Prints the loss curve and checks the fit against the known truth.

Run: python lab01_gradient_descent.py
"""
import numpy as np

rng = np.random.default_rng(0)


def fit_line(lr=0.1, steps=300):
    # Ground truth: y = 2x + 1 plus noise
    x = rng.uniform(-1, 1, 50)
    y = 2 * x + 1 + rng.normal(0, 0.1, 50)
    w, b = 0.0, 0.0
    losses = []
    for _ in range(steps):
        pred = w * x + b
        err = pred - y
        loss = np.mean(err ** 2)
        # d loss / d w = mean(2 * err * x); d loss / d b = mean(2 * err)   (chain rule)
        gw = np.mean(2 * err * x)
        gb = np.mean(2 * err)
        w -= lr * gw
        b -= lr * gb
        losses.append(loss)
    return w, b, losses


def fit_logistic(lr=0.5, steps=500):
    # Two features; true boundary x0 + x1 > 0
    X = rng.normal(0, 1, (200, 2))
    y = (X[:, 0] + X[:, 1] > 0).astype(float)
    w = np.zeros(2)
    b = 0.0
    losses = []
    for _ in range(steps):
        z = X @ w + b
        p = 1 / (1 + np.exp(-z))
        eps = 1e-9
        loss = -np.mean(y * np.log(p + eps) + (1 - y) * np.log(1 - p + eps))
        # For sigmoid + cross-entropy, d loss / d z = (p - y) / n   (the famous simplification)
        dz = (p - y) / len(y)
        gw = X.T @ dz
        gb = dz.sum()
        w -= lr * gw
        b -= lr * gb
        losses.append(loss)
    acc = np.mean(((X @ w + b) > 0) == (y == 1))
    return w, b, losses, acc


if __name__ == "__main__":
    w, b, losses = fit_line()
    print(f"line: w={w:.3f} (true 2), b={b:.3f} (true 1), loss {losses[0]:.3f} -> {losses[-1]:.4f}")
    assert abs(w - 2) < 0.1 and abs(b - 1) < 0.1, "line fit did not converge"
    assert losses[-1] < losses[0] / 10, "loss did not fall"

    # What happens with a learning rate 15x too high: the loss should blow up or oscillate
    _, _, bad = fit_line(lr=1.5, steps=50)
    print(f"line with lr 15x too high: loss after 50 steps = {bad[-1]:.3g} (divergence expected)")
    assert bad[-1] > losses[-1] * 10

    w2, b2, l2, acc = fit_logistic()
    print(f"logistic: w={np.round(w2, 2)} (direction should be ~[1,1]), accuracy {acc:.3f}, loss {l2[0]:.3f} -> {l2[-1]:.3f}")
    assert acc > 0.95
    assert abs(w2[0] - w2[1]) / abs(w2).mean() < 0.3, "weights should be roughly equal"
    print("OK")
