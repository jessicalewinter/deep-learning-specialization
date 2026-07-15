# 03 — Train / Validation / Test Split

## TL;DR

Split your data into three parts: **train** (fit the model), **validation** (tune hyperparameters and pick architectures), **test** (one final, untouched check). The point is to get an honest estimate of how the model will perform on data it has never seen.

## Why it matters

A model that "works" on training data is meaningless — it might just be memorizing. The whole goal of ML is **generalization**, and the only way to measure that is to hide some data from the model during training and see how it does.

Skip this and you get one of the two most expensive bugs in ML:
1. **Optimistic results** that don't survive deployment
2. **Wasted weeks** debugging a "good" model that was actually overfit

## The three sets

| Set | Used for | Touched during training? | Touched during tuning? |
|---|---|---|---|
| **Train** | Fitting model parameters | Yes, every epoch | — |
| **Validation** | Picking hyperparameters, early stopping, model selection | No | Yes, repeatedly |
| **Test** | Final unbiased estimate of performance | No | No — *touch it once* |

The mental model: train teaches the model, validation grades your *decisions about the model*, test grades the final result.

## Typical splits

- Small dataset (~10k examples): 60 / 20 / 20
- Medium (~100k): 80 / 10 / 10
- Big (~1M+): 98 / 1 / 1 — even 1% is plenty when the absolute count is large

There's no universal rule. What matters is that validation and test are big enough that your metric isn't dominated by noise.

## The cardinal sin: test set leakage

Once you start making decisions based on test performance — "let me try a different model and see how test does" — your test set is no longer a test set. It's a second validation set, and you've lost your unbiased estimate.

Common ways to leak:

- **Looking at test results** between training runs and reacting to them
- **Tuning hyperparameters on test** instead of validation
- **Computing features (e.g., mean, std) using the full dataset** before splitting — the model "knows" something about test distribution
- **Time series split done wrong** — sorting randomly when there's a temporal ordering
- **Duplicate or near-duplicate examples** spanning train and test

The first three are the common ones. The temporal one bites everyone exactly once.

## How to split

```python
from sklearn.model_selection import train_test_split

# 80% train, 20% temp → split temp into 50/50 → 80/10/10 overall
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)
```

`stratify=y` is important for classification — it preserves class proportions in each split. Without it, a 5%-positive class can end up 8% in one split and 2% in another.

## Time-series caveat

If your data has time ordering (stock prices, sensor logs, user behavior), **don't split randomly**. Use a chronological split: train on past, validate on near-future, test on far-future. Random splitting lets the model "see" the future during training, and your metrics will be wildly optimistic.

## When you don't have enough data

Use **k-fold cross-validation**: split into k folds, train k times, each time holding out one fold as validation. Average the metrics. You still set aside a separate test set if you can.

## Common pitfalls

- **No test set at all** — "I just used train and validation" is the most common professional mistake
- **Test set used as a second validation set** — same effect as having no test set
- **Random split on temporal data** — silently catastrophic
- **Preprocessing fit on full data** — fit scalers/encoders on train *only*, then apply to val/test

## Further reading

- Géron, *Hands-On ML*, Ch. 2 (the housing example walks through this carefully)
- Andrew Ng, *Machine Learning Yearning* — opinionated takes on dev/test set composition
