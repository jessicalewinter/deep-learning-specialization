# 10 — Point and Interval Estimation

## TL;DR

**Estimation** is the bridge from sample to population. A **point estimate** gives you a single best guess (the sample mean estimates the population mean). A **confidence interval** gives you a range that likely contains the true value, quantifying your uncertainty.

## Why it matters

Every ML metric you compute (accuracy, loss, F1) is a point estimate from a finite test set. Without confidence intervals, you can't tell whether "model A got 0.87 and model B got 0.85" is a real difference or just noise. Understanding estimation separates rigorous ML practice from guessing.

## Core concept

### Point estimation

An **estimator** is a formula applied to data to approximate a population parameter:

| Parameter | Estimator | Formula |
|---|---|---|
| Population mean μ | Sample mean x̄ | Σxᵢ / n |
| Population variance σ² | Sample variance s² | Σ(xᵢ - x̄)² / (n-1) |
| Population proportion p | Sample proportion p̂ | count / n |

### Properties of good estimators

- **Unbiased**: E(estimator) = true parameter. The sample mean is unbiased for μ. The sample variance with n-1 (not n) is unbiased for σ².
- **Consistent**: as n → ∞, the estimator converges to the true value.
- **Efficient**: smallest variance among unbiased estimators.

### Bias

```
Bias = E(estimator) - true parameter
```

If bias = 0, the estimator is unbiased. This is why we divide by (n-1) in sample variance — dividing by n gives a biased estimator that systematically underestimates σ².

### Sampling distribution

If you took many samples and computed x̄ each time, those x̄ values would form a distribution. This is the **sampling distribution** of the mean:

```
x̄ ~ N(μ, σ²/n)    (by CLT, for large n)
```

The standard deviation of x̄ is σ/√n — called the **standard error**.

### Confidence intervals

A 95% confidence interval for μ (when σ is known):

```
x̄ ± z₀.₀₂₅ × (σ / √n) = x̄ ± 1.96 × (σ / √n)
```

**Correct interpretation:** if we repeated this procedure many times, 95% of the resulting intervals would contain the true μ.

**Wrong interpretation:** "there's a 95% probability that μ is in this interval." (μ is fixed; the interval is random.)

When σ is unknown (usual case), replace z with the t-distribution:

```
x̄ ± t_{n-1, α/2} × (s / √n)
```

### Confidence interval for proportions

For a sample proportion p̂ from n observations:

```
p̂ ± z_{α/2} × √(p̂(1-p̂) / n)
```

## Code example

```python
import numpy as np
from scipy import stats

# Simulate: true population mean = 50, std = 10
np.random.seed(42)
population_mean = 50
sample = np.random.normal(50, 10, size=30)

# Point estimates
x_bar = sample.mean()
s = sample.std(ddof=1)
se = s / np.sqrt(len(sample))
print(f"Sample mean (point estimate): {x_bar:.2f}")
print(f"Sample std: {s:.2f}")
print(f"Standard error: {se:.2f}")

# 95% confidence interval using t-distribution
confidence = 0.95
alpha = 1 - confidence
t_crit = stats.t.ppf(1 - alpha/2, df=len(sample)-1)
margin = t_crit * se
ci = (x_bar - margin, x_bar + margin)
print(f"95% CI: ({ci[0]:.2f}, {ci[1]:.2f})")
print(f"True μ={population_mean} in CI? {ci[0] <= population_mean <= ci[1]}")

# Or use scipy directly
ci_scipy = stats.t.interval(confidence, df=len(sample)-1, loc=x_bar, scale=se)
print(f"scipy CI: ({ci_scipy[0]:.2f}, {ci_scipy[1]:.2f})")
```

## Common pitfalls

- **Misinterpreting confidence intervals** — a 95% CI does NOT mean "95% probability the parameter is in here." It means: the procedure produces intervals that capture the truth 95% of the time across repeated sampling.
- **Using z when you should use t** — if n < 30 and σ is unknown, you must use the t-distribution. For large n, z and t are nearly identical.
- **"Larger CI = worse"** — a larger CI means more uncertainty, often because n is small. It's *honest*, not bad. Reporting a point estimate without a CI is what's bad.
- **Ignoring standard error** — two models with accuracy 0.87 ± 0.05 and 0.85 ± 0.05 are NOT meaningfully different. Their CIs overlap completely.

## Further reading

- Freedman, Pisani & Purves, *Statistics*, Chapters 21–23
- Khan Academy, "Confidence intervals"
- For ML: bootstrap confidence intervals (resample to estimate uncertainty without assuming normality)
