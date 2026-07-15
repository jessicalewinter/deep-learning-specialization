# 13 — Regression and Correlation

## TL;DR

**Regression** fits a line (or curve) to data so you can predict one variable from another. **R²** tells you what fraction of the variation in Y is "explained" by X. This is the statistical foundation for the linear regression you've already seen in ML — here we focus on the inference side.

## Why it matters

Linear regression is both the simplest ML model and a core statistical inference tool. Understanding it statistically — residuals, R², confidence intervals on coefficients — lets you interpret models, diagnose problems, and know when to trust predictions.

## Core concept

### The model

```
Y = β₀ + β₁X + ε
```

- β₀: intercept (Y when X = 0)
- β₁: slope (how much Y changes per unit of X)
- ε: error term (what the model can't explain) — assumed Normal(0, σ²)

### Fitting: least squares

Find β₀ and β₁ that minimize the sum of squared residuals:

```
SSE = Σ(yᵢ - ŷᵢ)² = Σ(yᵢ - β₀ - β₁xᵢ)²
```

Solution:
```
β₁ = Cov(X,Y) / Var(X) = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
β₀ = ȳ - β₁x̄
```

### Decomposition of variance

| Component | Name | Meaning |
|---|---|---|
| SST = Σ(yᵢ - ȳ)² | Total sum of squares | Total variability in Y |
| SSR = Σ(ŷᵢ - ȳ)² | Regression sum of squares | Variability explained by the model |
| SSE = Σ(yᵢ - ŷᵢ)² | Error sum of squares | Unexplained variability (residuals) |

**SST = SSR + SSE** (always)

### R² (coefficient of determination)

```
R² = SSR / SST = 1 - SSE/SST
```

- R² = 1: model explains everything (perfect fit)
- R² = 0: model explains nothing (just predicting the mean)
- R² = 0.75: model explains 75% of the variability in Y

For simple linear regression (one X): R² = r² (correlation squared).

### Population regression function

The true relationship E(Y|X=x) = β₀ + β₁x is the **population regression function**. What we compute from data (b₀ + b₁x) is an *estimate* of it. With more data, our estimates converge to the true values.

## Math

**Worked example:** Hours studied vs exam score.

| Hours (X) | Score (Y) |
|---|---|
| 1 | 50 |
| 2 | 60 |
| 3 | 65 |
| 4 | 70 |
| 5 | 80 |

```
x̄ = 3, ȳ = 65
Σ(xᵢ - x̄)(yᵢ - ȳ) = (-2)(-15) + (-1)(-5) + (0)(0) + (1)(5) + (2)(15) = 30+5+0+5+30 = 70
Σ(xᵢ - x̄)² = 4+1+0+1+4 = 10

β₁ = 70/10 = 7.0
β₀ = 65 - 7×3 = 44.0

Model: Ŷ = 44 + 7X
Interpretation: each extra hour of studying → +7 points on the exam.
```

## Code example

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([50, 60, 65, 70, 80, 85, 90, 95])

# Fit using scipy (gives slope, intercept, r, p-value, std error)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Ŷ = {intercept:.2f} + {slope:.2f}X")
print(f"R² = {r_value**2:.4f}")
print(f"p-value for slope: {p_value:.6f}")
print(f"Std error of slope: {std_err:.4f}")

# Predictions
y_pred = intercept + slope * x
residuals = y - y_pred

# SST, SSR, SSE
sst = np.sum((y - y.mean())**2)
ssr = np.sum((y_pred - y.mean())**2)
sse = np.sum(residuals**2)
print(f"\nSST = {sst:.2f}")
print(f"SSR = {ssr:.2f}")
print(f"SSE = {sse:.2f}")
print(f"R² = SSR/SST = {ssr/sst:.4f}")

# Plot
plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, 'r-', label=f'Fit: Ŷ = {intercept:.1f} + {slope:.1f}X')
plt.xlabel('Hours studied')
plt.ylabel('Exam score')
plt.legend()
plt.show()
```

## Common pitfalls

- **Extrapolation** — the model is only valid in the range of observed X. Predicting exam score for 100 hours of study with a model trained on 1–8 hours is nonsense.
- **"High R² = good model"** — R² always increases when you add more predictors, even useless ones. Use adjusted R² for multiple regression. Also, R² = 0.95 on training data means nothing if it's 0.3 on test data.
- **Ignoring residual patterns** — if residuals show a curve or funnel shape, the linear model is wrong. Always plot residuals.
- **Confusing correlation with slope** — r tells you about *strength* of the relationship. The slope tells you the *rate of change*. High correlation + tiny slope is possible (very tight cluster around a nearly flat line).
- **Regression to the mean** — extreme observations tend to be followed by less extreme ones. This is a statistical phenomenon, not a real effect.

## Further reading

- Freedman, Pisani & Purves, Chapters 10–12
- Khan Academy, "Linear regression and correlation"
- Scikit-learn: `LinearRegression`, `r2_score`
- For ML: connect this to topic 05 (Linear Regression) in the ML curriculum
