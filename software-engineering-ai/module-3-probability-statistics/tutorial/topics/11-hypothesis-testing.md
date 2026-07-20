# 11 — Hypothesis Testing and Chi-Square

## TL;DR

**Hypothesis testing** is a framework for deciding whether observed data is consistent with a claim (null hypothesis) or provides enough evidence to reject it. The **chi-square test** applies this to categorical data — testing whether observed frequencies match expected ones.

## Why it matters

In ML: "Is model A significantly better than model B?" is a hypothesis test. A/B testing in production is hypothesis testing. Without it, you'll ship changes that were just noise. The chi-square test specifically is used for feature selection (is this categorical feature related to the target?) and goodness-of-fit testing.

## Core concept

### The hypothesis testing framework

1. **State hypotheses:**
   - H₀ (null): nothing interesting is happening (no effect, no difference)
   - H₁ (alternative): something is happening (there IS an effect)

2. **Choose significance level α** (usually 0.05): the probability of rejecting H₀ when it's actually true (false positive rate).

3. **Compute a test statistic** from your data (z, t, χ², etc.)

4. **Find the p-value**: probability of seeing a test statistic this extreme (or more) if H₀ were true.

5. **Decide**: if p-value < α, reject H₀. Otherwise, fail to reject (NOT "accept H₀").

### Comparing two population means

If you have samples from two populations X₁ and X₂:

- H₀: μ₁ = μ₂ (no difference)
- H₁: μ₁ ≠ μ₂ (there is a difference)

Test statistic (known σ):
```
z = (x̄₁ - x̄₂) / √(σ₁²/n₁ + σ₂²/n₂)
```

### Chi-square test

For categorical data, tests whether observed counts differ from expected counts:

```
χ² = Σ (Observed - Expected)² / Expected
```

Two main uses:
- **Goodness of fit**: does data follow a specific distribution? (Is this die fair?)
- **Test of independence/heterogeneity**: are two categorical variables related? (Is treatment related to outcome?)

Degrees of freedom:
- Goodness of fit: df = (number of categories - 1)
- Independence: df = (rows - 1) × (columns - 1)

### p-value interpretation

| p-value | Evidence against H₀ |
|---|---|
| > 0.10 | Weak (don't reject) |
| 0.05 – 0.10 | Marginal |
| 0.01 – 0.05 | Moderate (reject at α=0.05) |
| < 0.01 | Strong |
| < 0.001 | Very strong |

## Math

**Chi-square example:** A die is rolled 60 times. Expected: 10 per face. Observed: {8, 12, 9, 11, 7, 13}.

```
χ² = (8-10)²/10 + (12-10)²/10 + (9-10)²/10 + (11-10)²/10 + (7-10)²/10 + (13-10)²/10
   = 4/10 + 4/10 + 1/10 + 1/10 + 9/10 + 9/10
   = 28/10 = 2.8
```

df = 6 - 1 = 5. Critical value at α=0.05 is 11.07. Since 2.8 < 11.07, fail to reject H₀. The die appears fair.

## Code example

```python
import numpy as np
from scipy import stats

# Chi-square goodness of fit: is this die fair?
observed = np.array([8, 12, 9, 11, 7, 13])
expected = np.array([10, 10, 10, 10, 10, 10])

chi2_stat = np.sum((observed - expected)**2 / expected)
df = len(observed) - 1
p_value = 1 - stats.chi2.cdf(chi2_stat, df)
print(f"χ² = {chi2_stat:.2f}, df = {df}, p-value = {p_value:.4f}")
# p ≈ 0.73 → no evidence die is unfair

# Or use scipy directly
chi2, p = stats.chisquare(observed, expected)
print(f"scipy: χ² = {chi2:.2f}, p = {p:.4f}")

# Chi-square test of independence (contingency table)
# Drug vs placebo: did patients improve?
#              Improved  No change
# Drug            40        10
# Placebo         25        25
table = np.array([[40, 10], [25, 25]])
chi2, p, df, expected = stats.chi2_contingency(table)
print(f"\nIndependence test: χ² = {chi2:.2f}, p = {p:.4f}")
print(f"Expected under H₀:\n{expected}")
```

## Common pitfalls

- **"p > 0.05 means H₀ is true"** — no! It means you don't have enough evidence to reject it. Absence of evidence ≠ evidence of absence.
- **Multiple testing** — if you test 20 hypotheses at α=0.05, you expect 1 false positive by chance. Use Bonferroni correction or control FDR.
- **Low expected counts in chi-square** — the approximation breaks down when expected counts < 5. Use Fisher's exact test instead.
- **"Statistically significant = practically important"** — with n=10 million, you can detect a 0.001% difference. That difference might be meaningless in practice.

## Further reading

- Freedman, Pisani & Purves, Chapters 26–29
- Khan Academy, "Hypothesis testing" and "Chi-square test"
- ASA Statement on p-values (2016) — what they actually mean
