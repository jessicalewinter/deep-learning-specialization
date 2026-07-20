# 01 — What is Machine Learning?

## TL;DR

Machine learning is a way of writing programs by **showing examples instead of writing rules**. You give the computer data and a goal, and it finds the pattern that turns inputs into outputs.

## Why it matters

Traditional programming hits a wall on problems where you can't enumerate the rules — recognizing a cat in a photo, translating Portuguese to English, deciding which email is spam. ML bypasses the rule-writing problem by *learning* the rules from data.

The classic Tom Mitchell definition (1997):

> A program is said to learn from experience **E** with respect to some task **T** and performance measure **P**, if its performance at **T**, as measured by **P**, improves with **E**.

Concretely: spam classifier (T) gets better at flagging spam (P) as you give it more labeled emails (E).

## Core concept

Three ingredients, always:

| Component | What it is | Example |
|---|---|---|
| **Data** | Examples (inputs, often with labels) | 10,000 emails marked spam/not-spam |
| **Model** | A function with tunable parameters | Logistic regression with weights `w` |
| **Loss** | How wrong the model is | Cross-entropy loss |

Training = adjusting model parameters to minimize loss on the data.

## The mental shift

Coming from software engineering, the hardest mental shift is: **the model is not the program**. The model is what comes out *after* you run a training program. You write the training procedure and the architecture; the parameters get learned.

```
Traditional code:  rules + data → answers
Machine learning:  data + answers → rules (the trained model)
```

## Code example

The simplest possible ML program — fit a line to some points:

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# data: years of experience → salary
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([35, 40, 50, 60, 70])

model = LinearRegression()
model.fit(X, y)            # this is "learning" — finds slope and intercept

print(model.predict([[6]]))  # → ~80
print(f"slope={model.coef_[0]:.2f}, intercept={model.intercept_:.2f}")
```

That `.fit()` call is the entire essence of ML in three letters: it found the slope and intercept that minimize the squared error to your data. Everything else in this curriculum is variations on that idea — different models, different losses, different data.

## Common pitfalls

- **"More data fixes everything"** — false. Garbage data scaled up is still garbage. Bad labels, biased samples, and label noise hurt at any scale.
- **Confusing the model with the algorithm** — "logistic regression" is a model family; the algorithm that fits it (e.g., gradient descent) is separate.
- **Skipping the baseline** — always measure against a dumb baseline (predict the mean, predict the majority class). If your fancy model barely beats it, something's off.

## Further reading

- Mitchell, *Machine Learning* (1997), Chapter 1
- Domingos, ["A Few Useful Things to Know About Machine Learning"](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — short, classic, opinionated
- Géron, *Hands-On ML*, Chapter 1
