# 04 — Descriptive Statistics

## TL;DR

Descriptive statistics compress a dataset into a few numbers that tell you **where the center is** (mean, median, mode) and **how spread out it is** (variance, standard deviation, IQR). These are the building blocks for everything that follows.

## Why it matters

In ML, you normalize features using mean and standard deviation. You detect outliers using IQR. You judge model performance using summary statistics. Without understanding these measures, you're blindly applying transformations you can't interpret.

## Core concept

### Measures of position (center)

| Measure | What it is | When to use |
|---|---|---|
| **Mean** (x̄) | Sum of all values / count | Symmetric data, no extreme outliers |
| **Median** | Middle value when sorted | Skewed data, robust to outliers |
| **Mode** | Most frequent value | Categorical data or multimodal distributions |

**Key insight:** mean is pulled by outliers, median isn't. Salaries: mean = $80k (pulled up by CEOs), median = $55k (what most people actually earn).

### Measures of spread (dispersion)

| Measure | Formula | Intuition |
|---|---|---|
| **Range** | max - min | Simplest, but one outlier ruins it |
| **Variance** (σ²) | avg of squared deviations from mean | Average "squared distance" from center |
| **Std deviation** (σ) | √variance | Same units as the data |
| **IQR** | Q3 - Q1 | Width of the middle 50% |

### Why we square in variance

If you just average the deviations (value - mean), positives and negatives cancel out → always zero. Squaring makes everything positive. Standard deviation brings it back to original units by taking the square root.

### Quantiles and quartiles

- **p-quantile**: the value below which p% of data falls
- **Q1** (25th percentile): 25% of data is below this
- **Q3** (75th percentile): 75% of data is below this
- **IQR** = Q3 - Q1: the "spread" of the middle half

### Box plots

A box plot shows: min, Q1, median, Q3, max — plus outliers as individual dots beyond 1.5×IQR from the box edges. It's the most compact way to compare distributions across groups.

### Symmetry

- **Symmetric**: mean ≈ median (normal distribution)
- **Right-skewed**: mean > median (income, house prices — long tail to the right)
- **Left-skewed**: mean < median (exam scores when most people do well)

## Code example

```python
import numpy as np

data = [22, 25, 27, 30, 35, 40, 42, 55, 60, 65]

mean = np.mean(data)
median = np.median(data)
std = np.std(data, ddof=1)  # ddof=1 for sample std deviation
variance = np.var(data, ddof=1)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print(f"Mean:     {mean:.1f}")
print(f"Median:   {median:.1f}")
print(f"Std dev:  {std:.1f}")
print(f"Variance: {variance:.1f}")
print(f"Q1:       {q1:.1f}")
print(f"Q3:       {q3:.1f}")
print(f"IQR:      {iqr:.1f}")

# Box plot
import matplotlib.pyplot as plt
plt.boxplot(data)
plt.title("Box Plot")
plt.show()
```

## Common pitfalls

- **Using mean on skewed data** — report median instead (or both). Income, wait times, and file sizes are almost always right-skewed.
- **Forgetting ddof=1** — NumPy defaults to population variance (ddof=0). For samples, use ddof=1 (Bessel's correction). Pandas defaults to ddof=1.
- **Ignoring units** — variance is in squared units (meters² if your data is in meters). Standard deviation brings you back to meters. Always use std dev when communicating spread.
- **"Low variance = good"** — not always. A model that predicts the mean for everything has zero variance in its predictions but is useless.

## Further reading

- Khan Academy, "Descriptive statistics" series
- Pandas: `df.describe()`, `df.quantile()`, `df.boxplot()`
- Freedman, Pisani & Purves, *Statistics*, Chapters 4–5
