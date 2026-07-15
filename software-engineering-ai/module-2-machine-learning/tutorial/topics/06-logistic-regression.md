# 06 — Logistic Regression & Cross-Entropy

## TL;DR

Logistic regression is **linear regression squashed into a probability**. You compute a linear score `w·x + b`, pass it through a sigmoid to get a number in (0, 1), and interpret that as `P(y=1 | x)`. The loss is **cross-entropy**, not MSE — and there's a sharp reason why.

## Why it matters

- It's the standard baseline for binary classification
- It's the *exact* output layer of every neural-network classifier — softmax is the multi-class generalization
- It's where you learn why classification needs a different loss than regression
- It's interpretable: the weights tell you which features push the prediction toward "yes"

If you can derive cross-entropy and explain why MSE is wrong here, you understand more than half of beginner ML.

## The model

```
z   = w·x + b              ← linear score (any real number)
ŷ   = σ(z) = 1 / (1 + e⁻ᶻ)  ← squashed into (0, 1) — interpret as P(y=1)
```

`σ` is the **sigmoid** function. Its shape:

```
        1 ─┤              ╭───────
           │            ╭─╯
        0.5┤          ╭─╯
           │        ╭─╯
        0  ┤────────╯
           └────────┼───────────
                    z = 0
```

- `z = 0` → `ŷ = 0.5` (the decision boundary)
- `z` very positive → `ŷ ≈ 1`
- `z` very negative → `ŷ ≈ 0`

To make a hard prediction: `ŷ ≥ 0.5` → predict class 1, else class 0. (You can move that threshold to trade precision for recall — see evaluation metrics later.)

## The loss: cross-entropy

For a single example with true label `y ∈ {0, 1}` and prediction `ŷ`:

```
L = -[ y · log(ŷ) + (1-y) · log(1-ŷ) ]
```

Read it: when `y = 1`, only the first term survives → `-log(ŷ)`. When `y = 0`, only the second → `-log(1-ŷ)`. Both go to **0 when correct, infinity when confidently wrong**.

This is the *only* loss function in this curriculum that's worth memorizing immediately.

## Why not MSE for classification?

You *can* train a classifier with MSE. It just works much worse. Two reasons:

### 1. The optimization is bad

MSE on top of sigmoid creates a **non-convex** loss surface with flat regions where gradients vanish. Cross-entropy on top of sigmoid is **convex** in the parameters and has well-behaved gradients everywhere.

### 2. It punishes the wrong things

MSE treats `ŷ = 0.9` and `ŷ = 0.99` (true label 1) as nearly equivalent — both have small error. Cross-entropy treats `ŷ = 0.99` as **much** better, because `-log(0.99)` is way smaller than `-log(0.9)`. For probabilistic classification, this is what you want — confidence matters.

The math: cross-entropy is the negative log-likelihood under a Bernoulli model. So minimizing cross-entropy = maximum likelihood estimation. MSE has no such interpretation for classification.

## Gradient (the beautiful part)

Despite the scary-looking loss, the gradient with respect to weights is shockingly clean:

```
∂L/∂w = (ŷ - y) · x
```

That's the *same form* as linear regression. The sigmoid and the log "cancel" in a precise way during the chain rule. This is one of the great pedagogical moments in ML.

## Worked example

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss

X, y = make_classification(n_samples=1000, n_features=4, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

probs = model.predict_proba(X_test)[:, 1]   # P(y=1) for each example
preds = model.predict(X_test)

print(f"Accuracy:     {accuracy_score(y_test, preds):.3f}")
print(f"Cross-entropy: {log_loss(y_test, probs):.3f}")
print(f"Weights: {model.coef_[0]}")
```

The weights are interpretable: a large positive `wⱼ` means "feature `j` going up makes class 1 more likely."

## Multi-class: softmax

For more than two classes, generalize:

```
zₖ = wₖ·x + bₖ           for each class k
ŷₖ = e^(zₖ) / Σⱼ e^(zⱼ)   ← softmax: normalizes to a probability distribution
```

Loss becomes **categorical cross-entropy**: `-Σₖ yₖ log(ŷₖ)` where `y` is one-hot.

This is *literally* the output layer of every classification neural network you'll ever train.

## Decision boundary

Logistic regression produces a **linear** decision boundary — the set of points where `w·x + b = 0` is a straight line (or hyperplane). If your classes can't be separated by a line, logistic regression can't separate them either. The fix: feature engineering, kernel tricks, or a non-linear model.

## Common pitfalls

- **Using accuracy as the only metric** — for imbalanced data (95% negatives), predicting "always negative" hits 95% accuracy and is useless. Use precision, recall, F1, AUC.
- **Ignoring class imbalance** — set `class_weight='balanced'` or oversample the minority class
- **Treating probabilities as calibrated** — sklearn's `predict_proba` gives you numbers in (0, 1), but `0.7` doesn't necessarily mean "70% chance." Calibrate if you need real probabilities.
- **Forgetting regularization** — logistic regression overfits with many features. sklearn's default already has L2; don't accidentally turn it off with `C=∞`.

## Further reading

- Bishop, *Pattern Recognition and Machine Learning*, Ch. 4 — the rigorous derivation
- Géron, *Hands-On ML*, Ch. 4
- Andrew Ng's CS229 notes on logistic regression — best concise treatment online
