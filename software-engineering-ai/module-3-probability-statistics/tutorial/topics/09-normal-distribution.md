# 09 — The Normal Distribution

## TL;DR

The **normal (Gaussian) distribution** is the bell curve — defined by its mean μ and standard deviation σ. It appears everywhere because of the Central Limit Theorem: averages of many independent things tend toward normal, regardless of the underlying distribution.

## Why it matters

Half of ML assumes normality somewhere: linear regression assumes normal errors, Gaussian Naive Bayes assumes normal features, batch normalization pushes activations toward normal, and the VAE's latent space is explicitly Gaussian. Even when you don't assume it, the normal distribution is the default mental model for "well-behaved data."

## Core concept

### The probability density function (PDF)

```
f(x) = (1 / (σ√(2π))) × exp(-(x - μ)² / (2σ²))
```

Two parameters completely define it:
- **μ** (mu): the center — where the peak is
- **σ** (sigma): the spread — how wide the bell is

### Key properties

- Symmetric around μ
- Mean = median = mode = μ
- ~68% of data falls within μ ± σ
- ~95% within μ ± 2σ
- ~99.7% within μ ± 3σ (the "68-95-99.7 rule")

### Standard normal Z ~ N(0, 1)

Any normal X ~ N(μ, σ²) can be converted to standard normal:

```
Z = (X - μ) / σ
```

This **z-score** tells you "how many standard deviations from the mean." A z-score of 2 means you're 2σ above the mean — in the top ~2.5%.

### Why "density" not "probability"?

For continuous distributions, P(X = exactly 3.7) = 0. You can only ask about intervals:

```
P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx
```

The PDF gives *density* — probability per unit. The area under the curve gives probability.

### The Central Limit Theorem (preview)

If you take the average of n independent observations (from *any* distribution with finite variance), that average ≈ Normal as n grows large. This is why the normal distribution is everywhere.

## Code example

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Standard normal
z = stats.norm(0, 1)

# Plot PDF
x = np.linspace(-4, 4, 200)
plt.plot(x, z.pdf(x), label='N(0,1)')
plt.fill_between(x, z.pdf(x), where=(x >= -1) & (x <= 1), alpha=0.3, label='±1σ (68%)')
plt.legend()
plt.title("Standard Normal Distribution")
plt.show()

# Z-scores: if heights ~ N(170, 8), how unusual is 190cm?
mu, sigma = 170, 8
height = 190
z_score = (height - mu) / sigma
print(f"Z-score of {height}cm: {z_score:.2f}")  # 2.5
print(f"% taller than {height}cm: {(1 - stats.norm.cdf(z_score))*100:.2f}%")  # ~0.62%

# The 68-95-99.7 rule
for k in [1, 2, 3]:
    prob = stats.norm.cdf(k) - stats.norm.cdf(-k)
    print(f"P(|Z| ≤ {k}) = {prob*100:.1f}%")
```

## Common pitfalls

- **"Everything is normal"** — income, file sizes, network traffic, survival times... many real distributions are *not* normal. They're often skewed or heavy-tailed. Always check with a histogram before assuming.
- **Confusing σ with σ²** — N(μ, σ²) uses variance as the second parameter. Some textbooks write N(μ, σ) meaning std dev. Know which convention your source uses.
- **Reading probability from the PDF's y-axis** — the y-axis is density, not probability. A PDF can exceed 1 (e.g., N(0, 0.1) has peak density ≈ 4). Only areas give probabilities.
- **"Normal approximation always works"** — it needs sufficient n (CLT) or the data must actually be normally distributed. For small samples from skewed distributions, the normal approximation fails.

## Further reading

- Blitzstein & Hwang, Chapter 5
- 3Blue1Brown, "But what is the Central Limit Theorem?" (YouTube)
- Khan Academy, "Normal distribution and z-scores"
