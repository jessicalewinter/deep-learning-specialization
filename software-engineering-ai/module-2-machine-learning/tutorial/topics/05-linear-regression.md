# 05 — Linear Regression

## TL;DR

Linear regression assumes the relationship between inputs and output is a **straight line** (or hyperplane in higher dimensions). It fits the line by minimizing the sum of squared errors. Simple, fast, interpretable — and the conceptual ancestor of nearly every other ML model.

## Why it matters

Even when the truth isn't linear, linear regression is:

- A baseline you should always run first
- A diagnostic tool — if linear fits well, you might not need a fancy model
- A building block — neural network layers are essentially stacked linear regressions with non-linearities between them
- The cleanest place to learn loss functions, gradient descent, regularization, and the train/val/test discipline

If you understand linear regression deeply, half of "modern" ML is just notation.

## The model

For a single input `x`, predict:

```
ŷ = w·x + b
```

Two parameters: `w` (slope, "weight") and `b` (intercept, "bias"). Multiple inputs:

```
ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
  = w·x + b      (in vector form)
```

That's it. The whole model is a dot product plus a constant.

## The loss

We want `ŷ` close to `y` on average. Use **mean squared error**:

```
MSE = (1/N) · Σ (yᵢ - ŷᵢ)²
```

Why squared and not absolute value?
- Squared error is differentiable everywhere → gradient methods work cleanly
- It punishes big errors more than small ones (often what you want)
- Has a closed-form solution (see below)

The downside: MSE is sensitive to outliers, because squaring makes big errors *very* big.

## Two ways to fit it

### 1. Closed form (the "normal equation")

For linear regression, you can solve for the optimal weights directly:

```
w* = (XᵀX)⁻¹ Xᵀy
```

One line of NumPy:

```python
w = np.linalg.inv(X.T @ X) @ X.T @ y
```

This is exact, no iteration, no learning rate. So why doesn't everyone use it?

- The matrix inversion is `O(n³)` in the number of features — fine for 100 features, brutal for 100,000
- It only works for linear regression with MSE — most other models don't have closed forms
- Numerical issues when `XᵀX` is ill-conditioned

In practice, `np.linalg.lstsq` is preferred over the literal formula — same answer, more numerically stable.

### 2. Gradient descent

Start with random weights, repeatedly nudge them in the direction that reduces loss:

```
w := w - η · ∂Loss/∂w
```

`η` (eta) is the learning rate. For MSE on linear regression, the gradient is:

```
∂MSE/∂w = (2/N) · Xᵀ(Xw - y)
```

This is the *only* method that scales to deep networks and most other modern models. Linear regression is where you learn it cleanly.

## A worked example

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Synthetic data: y = 3x + 5 + noise
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3 * X.ravel() + 5 + np.random.randn(100) * 2

model = LinearRegression()
model.fit(X, y)

print(f"Learned slope:     {model.coef_[0]:.3f}  (true: 3.0)")
print(f"Learned intercept: {model.intercept_:.3f}  (true: 5.0)")
print(f"R² on training:    {model.score(X, y):.3f}")
```

Expected output: slope close to 3.0, intercept close to 5.0, R² in the 0.95+ range.

## Assumptions (and what breaks if they're violated)

Linear regression *technically* assumes:

1. **Linearity** — the true relationship is linear
2. **Independence** — observations are independent of each other
3. **Homoscedasticity** — error variance is constant across `x`
4. **Normality of errors** — for confidence intervals, not the prediction itself

Violations:

- Non-linear truth → systematic prediction errors. Fix: feature engineering (add `x²`, `log(x)`, interactions) or use a non-linear model.
- Heteroscedasticity → predictions still unbiased but error bars wrong
- Highly correlated inputs (multicollinearity) → unstable weights, hard to interpret. Fix: drop redundant features, use regularization (Ridge/Lasso).

## Variants

- **Ridge regression (L2):** add `λ·Σ wⱼ²` to the loss → shrinks weights, fights overfitting and multicollinearity
- **Lasso (L1):** add `λ·Σ|wⱼ|` → can drive weights to *exactly* zero, doing feature selection
- **Elastic Net:** L1 + L2 combined
- **Polynomial regression:** linear regression with engineered features `x, x², x³, ...` — still "linear in the parameters"

## Common pitfalls

- **Forgetting to scale features** — if `x₁` ranges 0–1 and `x₂` ranges 0–1,000,000, gradient descent gets miserable. Standardize first.
- **Using R² as the only metric** — R² can be high while predictions are systematically biased. Always plot residuals.
- **Extrapolating beyond training range** — linear models predict happily outside the data; the predictions are usually wrong.
- **Reporting training MSE** — meaningless. Always validation/test.

## Further reading

- Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning*, Ch. 3 — definitive statistical treatment
- Géron, *Hands-On ML*, Ch. 4
- 3Blue1Brown's series on linear algebra — helps if `XᵀX` looks like noise to you
