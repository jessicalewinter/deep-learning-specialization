# 12 — Comparing Means (t-Test)

## TL;DR

The **t-test** compares means when you have small samples and don't know the population standard deviation. It's the workhorse test for "is the average of group A different from group B?" — which in ML translates to "is model A's average performance genuinely different from model B's?"

## Why it matters

You trained two models and got accuracy 0.87 vs 0.85 on 10 cross-validation folds. Is that a real difference or just noise? A paired t-test on the fold-level scores answers this directly. Without it, you're deploying models based on random fluctuation.

## Core concept

### Why not just use a z-test?

The z-test requires knowing σ (population std dev). In practice, you estimate it from data with s (sample std dev). For large n, s ≈ σ and z works fine. But for small n (< 30), s is unreliable — it might be too small by chance, making your test too aggressive.

The t-distribution accounts for this extra uncertainty. It has heavier tails than the normal — more probability of extreme values — and the heaviness depends on **degrees of freedom** (df = n-1). As df → ∞, t → z.

### One-sample t-test

"Is the population mean μ equal to some value μ₀?"

```
t = (x̄ - μ₀) / (s / √n),  df = n - 1
```

### Two-sample t-test (independent groups)

"Do groups A and B have the same mean?"

```
t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)
```

df is approximated by the Welch-Satterthwaite formula (don't memorize it — scipy handles it).

### Paired t-test

When observations are matched (same subject before/after, or same data evaluated by two models):

```
d = differences (x₁ᵢ - x₂ᵢ)
t = d̄ / (s_d / √n),  df = n - 1
```

**This is the one you'll use most in ML** — comparing models on the same cross-validation folds.

### Signal-to-noise ratio

The t-statistic is essentially:

```
t = signal / noise = (observed difference) / (uncertainty in that difference)
```

Large |t| → the signal is much bigger than the noise → reject H₀.

## Math

**Worked example:** Two models evaluated on 5 CV folds.

| Fold | Model A | Model B | Difference (A-B) |
|---|---|---|---|
| 1 | 0.88 | 0.85 | 0.03 |
| 2 | 0.86 | 0.84 | 0.02 |
| 3 | 0.90 | 0.87 | 0.03 |
| 4 | 0.85 | 0.86 | -0.01 |
| 5 | 0.89 | 0.85 | 0.04 |

```
d̄ = (0.03 + 0.02 + 0.03 - 0.01 + 0.04) / 5 = 0.022
s_d = 0.0192 (sample std of differences)
t = 0.022 / (0.0192 / √5) = 0.022 / 0.0086 = 2.56
df = 4, critical t at α=0.05 two-tailed ≈ 2.78
```

Since 2.56 < 2.78, we fail to reject H₀. Not enough evidence (with only 5 folds) that A is truly better than B.

## Code example

```python
import numpy as np
from scipy import stats

# Paired t-test: two models on same CV folds
model_a = np.array([0.88, 0.86, 0.90, 0.85, 0.89, 0.87, 0.91, 0.86, 0.88, 0.90])
model_b = np.array([0.85, 0.84, 0.87, 0.86, 0.85, 0.84, 0.88, 0.83, 0.86, 0.87])

# Paired t-test (recommended for same folds)
t_stat, p_value = stats.ttest_rel(model_a, model_b)
print(f"Paired t-test: t = {t_stat:.3f}, p = {p_value:.4f}")

# Interpret
alpha = 0.05
if p_value < alpha:
    print(f"Reject H₀: Model A is significantly better (p={p_value:.4f})")
else:
    print(f"Fail to reject H₀: no significant difference (p={p_value:.4f})")

# One-sample t-test: is the mean accuracy > 0.85?
t_stat, p_value = stats.ttest_1samp(model_a, 0.85)
p_one_sided = p_value / 2  # one-sided: is it GREATER than 0.85?
print(f"\nOne-sample: t = {t_stat:.3f}, p (one-sided) = {p_one_sided:.4f}")

# Two-sample independent t-test (Welch's)
group1 = np.random.normal(100, 15, size=25)
group2 = np.random.normal(110, 15, size=30)
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)  # Welch's
print(f"\nWelch's t-test: t = {t_stat:.3f}, p = {p_value:.4f}")
```

## Common pitfalls

- **Using independent t-test when data is paired** — if both models saw the same fold, the observations are NOT independent. Paired test removes fold-to-fold variability and gives more power.
- **One-sided vs two-sided** — "is A better than B?" is one-sided. "Is A different from B?" is two-sided. scipy gives two-sided by default; halve p for one-sided.
- **Tiny samples, tiny p** — with n=3, even a large observed difference might not be significant because df=2 makes the t-distribution very wide. More folds = more power.
- **Assuming equal variances** — the classic t-test assumes σ₁ = σ₂. Welch's t-test (the default in most software) doesn't. Always use Welch's unless you have strong reason to assume equal variances.

## Further reading

- Freedman, Pisani & Purves, Chapter 26
- Dietterich, "Approximate statistical tests for comparing supervised classification learning algorithms" (1998)
- scipy.stats: `ttest_1samp`, `ttest_ind`, `ttest_rel`
