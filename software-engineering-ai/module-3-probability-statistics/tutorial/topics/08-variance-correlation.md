# 08 — Variance and Correlation

## TL;DR

**Variance** measures how spread out a single variable is. **Covariance** measures whether two variables move together. **Correlation** is covariance normalized to [-1, 1] so you can compare across different scales.

## Why it matters

In ML: variance of predictions relates to overfitting. Correlation between features tells you about redundancy (highly correlated features carry the same information). The covariance matrix is the foundation of PCA, Gaussian processes, and every multivariate model.

## Core concept

### Variance (recap + deeper)

```
Var(X) = E[(X - μ)²] = E(X²) - μ²
```

Where μ = E(X). Standard deviation σ = √Var(X) gives you spread in original units.

**Key properties:**
- Var(X) ≥ 0 always
- Var(c) = 0 (a constant has no spread)
- Var(aX + b) = a² × Var(X) (shifting doesn't change spread; scaling squares)
- Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)

That last formula is why covariance matters — you can't just add variances unless the variables are uncorrelated.

### Covariance

Measures the *direction* of the linear relationship between X and Y:

```
Cov(X, Y) = E[(X - μₓ)(Y - μᵧ)] = E(XY) - E(X)E(Y)
```

- Cov > 0: X and Y tend to increase together
- Cov < 0: when X increases, Y tends to decrease
- Cov = 0: no *linear* relationship (but there might be a non-linear one!)

### Correlation coefficient (Pearson's r)

Covariance depends on the scale of X and Y. Correlation normalizes it:

```
r = Cov(X, Y) / (σₓ × σᵧ)
```

- r = 1: perfect positive linear relationship
- r = -1: perfect negative linear relationship
- r = 0: no linear relationship
- |r| is the *strength*; sign is the *direction*

### Coefficient of contingency

For categorical variables (where Pearson's r doesn't apply), use the contingency coefficient based on chi-square:

```
C = √(χ² / (χ² + n))
```

This measures association between two categorical variables.

## Math

**Worked example:** Given X = {1, 2, 3, 4, 5} and Y = {2, 4, 5, 4, 5}:

```
E(X) = 3, E(Y) = 4
E(XY) = (1×2 + 2×4 + 3×5 + 4×4 + 5×5)/5 = (2+8+15+16+25)/5 = 66/5 = 13.2
Cov(X,Y) = 13.2 - 3×4 = 1.2

Var(X) = E(X²) - 9 = (1+4+9+16+25)/5 - 9 = 11 - 9 = 2
σₓ = √2 ≈ 1.414

Var(Y) = E(Y²) - 16 = (4+16+25+16+25)/5 - 16 = 17.2 - 16 = 1.2
σᵧ = √1.2 ≈ 1.095

r = 1.2 / (1.414 × 1.095) ≈ 0.775
```

Strong positive correlation — as X grows, Y tends to grow too.

## Code example

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Variance
print(f"Var(X) = {np.var(x, ddof=1):.4f}")  # sample variance (ddof=1)

# Covariance matrix
cov_matrix = np.cov(x, y)  # ddof=1 by default
print(f"Cov(X,Y) = {cov_matrix[0,1]:.4f}")

# Correlation
corr_matrix = np.corrcoef(x, y)
print(f"r = {corr_matrix[0,1]:.4f}")

# Or using pandas
import pandas as pd
df = pd.DataFrame({'x': x, 'y': y})
print(df.corr())  # full correlation matrix
```

## Common pitfalls

- **"Correlation = causation"** — the oldest statistical sin. Ice cream sales correlate with drowning deaths (both increase in summer). Correlation ≠ causation.
- **"r = 0 means no relationship"** — it means no *linear* relationship. X and X² have r ≈ 0 for symmetric data around 0, but they're perfectly related.
- **Using Pearson's r for non-linear relationships** — if the scatter plot is curved, r understates the strength. Use Spearman's rank correlation instead.
- **Forgetting Var(X+Y) includes covariance** — diversification in finance works because Cov is often negative between asset types.

## Further reading

- Freedman, Pisani & Purves, *Statistics*, Chapters 8–9
- Khan Academy, "Covariance and correlation"
- For ML: the covariance matrix is the heart of PCA (Topic to be added)
