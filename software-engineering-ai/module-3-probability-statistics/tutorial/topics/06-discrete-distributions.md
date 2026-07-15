# 06 — Discrete Probability Distributions

## TL;DR

A discrete distribution tells you the probability of each possible value a random variable can take. The big three are: **Uniform** (all outcomes equally likely), **Bernoulli** (single yes/no trial), and **Binomial** (count of successes in n trials).

## Why it matters

Classification in ML is fundamentally about discrete distributions: "what's the probability this email is spam?" is a Bernoulli question. "How many of these 100 transactions are fraudulent?" is binomial. Understanding these distributions lets you reason about model outputs and design appropriate loss functions.

## Core concept

### Random variable (quick definition)

A random variable X is a function that maps outcomes to numbers. Roll a die → X = the number shown. Flip 10 coins → X = count of heads.

### Discrete uniform distribution

Every outcome has the same probability.

```
X ~ Uniform({1, 2, ..., n})
P(X = k) = 1/n for each k
```

Example: fair die → P(X = k) = 1/6.

### Bernoulli distribution

A single trial with two outcomes: success (1) with probability p, failure (0) with probability 1-p.

```
X ~ Bernoulli(p)
P(X = 1) = p
P(X = 0) = 1 - p
```

Example: flip a fair coin → Bernoulli(0.5). A classifier's prediction for one sample is Bernoulli.

### Binomial distribution

Count the number of successes in n independent Bernoulli trials.

```
X ~ Binomial(n, p)
P(X = k) = C(n,k) × pᵏ × (1-p)ⁿ⁻ᵏ
```

Where C(n,k) = n! / (k! × (n-k)!) is "n choose k."

**Intuition:** if you flip a coin 10 times (n=10, p=0.5), what's the probability of getting exactly 7 heads?

### p-quantile of discrete distributions

The p-quantile is the smallest value x such that P(X ≤ x) ≥ p.

For Binomial(10, 0.5): the 0.5-quantile (median) is 5.

## Math

**Binomial worked example:** 10 coin flips, P(exactly 3 heads)?

```
P(X = 3) = C(10,3) × 0.5³ × 0.5⁷
         = 120 × 0.125 × 0.0078125
         = 0.1172
```

About 11.7% chance — not that common despite being close to "average."

## Code example

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Bernoulli: single coin flip
p = 0.7  # biased coin
bern = stats.bernoulli(p)
print(f"P(X=1) = {bern.pmf(1):.2f}")  # 0.70
print(f"P(X=0) = {bern.pmf(0):.2f}")  # 0.30

# Binomial: 20 trials, p=0.3
n, p = 20, 0.3
binom = stats.binom(n, p)

k_values = np.arange(0, n+1)
probabilities = binom.pmf(k_values)

# Plot the distribution
plt.bar(k_values, probabilities, edgecolor='black')
plt.xlabel('Number of successes (k)')
plt.ylabel('P(X = k)')
plt.title(f'Binomial(n={n}, p={p})')
plt.show()

# Key statistics
print(f"Expected value: {binom.mean():.1f}")  # n*p = 6
print(f"Std deviation:  {binom.std():.2f}")   # sqrt(n*p*(1-p))
print(f"P(X <= 5) = {binom.cdf(5):.4f}")      # cumulative
print(f"Median = {binom.median()}")
```

## Common pitfalls

- **"Binomial requires independence"** — if trials influence each other (drawing cards without replacement), it's not binomial. Use hypergeometric instead.
- **Confusing P(X = k) with P(X ≤ k)** — the PMF gives the probability of *exactly* k. The CDF gives *at most* k. In Python: `binom.pmf(k)` vs `binom.cdf(k)`.
- **Forgetting C(n,k)** — there are multiple *ways* to get k successes in n trials. The combinatorial coefficient counts them.
- **"Rare event = impossible"** — P(X=0) for Binomial(100, 0.01) = 0.366. Even with 1% chance per trial, there's a 37% chance of zero successes in 100 trials!

## Further reading

- Blitzstein & Hwang, Chapters 3–4
- scipy.stats documentation: `bernoulli`, `binom`, `randint` (discrete uniform)
- Khan Academy, "Binomial distribution"
