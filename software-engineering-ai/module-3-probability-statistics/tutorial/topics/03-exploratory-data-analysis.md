# 03 — Exploratory Data Analysis

## TL;DR

Before modeling, **look at your data**. EDA means understanding what types of variables you have, how they're distributed, and whether anything looks weird — all before fitting a single model.

## Why it matters

"Garbage in, garbage out" is the oldest rule in data science. EDA catches problems that no amount of fancy modeling can fix: missing values, outliers, mislabeled categories, imbalanced classes. In ML pipelines, the quality of your EDA directly determines whether your model learns signal or noise.

## Core concept

### Types of variables

| Type | Subtype | Example | What you can do with it |
|---|---|---|---|
| **Qualitative** | Nominal | Color (red, blue, green) | Count, mode |
| **Qualitative** | Ordinal | Education (high school < bachelor < master) | Count, mode, median |
| **Quantitative** | Discrete | Number of children (0, 1, 2, ...) | All math operations |
| **Quantitative** | Continuous | Height (1.72m) | All math operations |
| **Special** | Dichotomous | Yes/No, 0/1 | Treat as discrete or categorical |

Why this matters: the variable type determines which summary statistics make sense. The "mean" of {red, blue, green} is nonsense.

### Frequency tables

- **Absolute frequency**: raw count (42 people said "yes")
- **Relative frequency**: proportion (42/100 = 0.42)

### Class intervals (binning)

For continuous data, group values into intervals (bins) to build histograms:

```
[0, 10), [10, 20), [20, 30), ...
```

**Frequency density** = relative frequency / bin width. This makes histograms comparable across different bin sizes.

### Histograms

The fundamental EDA visualization. Each bar's *area* (not height!) represents the proportion of data in that bin. This is why density histograms use frequency density on the y-axis.

## Code example

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load some data
df = pd.DataFrame({
    'age': [22, 25, 27, 30, 35, 40, 42, 55, 60, 65],
    'income': [30, 35, 40, 50, 55, 70, 72, 90, 95, 100],
    'education': ['bachelor', 'master', 'bachelor', 'phd', 'master',
                  'phd', 'master', 'bachelor', 'phd', 'master']
})

# Variable types
print(df.dtypes)
print(df.describe())  # summary stats for numeric columns

# Frequency table for categorical variable
print(df['education'].value_counts())
print(df['education'].value_counts(normalize=True))  # relative frequency

# Histogram for continuous variable
plt.hist(df['age'], bins=5, edgecolor='black', density=True)
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('Age Distribution')
plt.show()
```

## Common pitfalls

- **Skipping EDA** — jumping straight to modeling is the #1 beginner mistake. You'll waste hours debugging a model when the problem was a column of strings mixed with numbers.
- **Confusing bar charts with histograms** — bar charts are for categorical data (gaps between bars). Histograms are for continuous data (no gaps, area = proportion).
- **Ignoring scale** — a histogram with 3 bins and one with 100 bins tell very different stories about the same data. Try multiple bin sizes.

## Further reading

- Tukey, *Exploratory Data Analysis* (1977) — the original
- Pandas documentation: `df.describe()`, `df.value_counts()`
- Seaborn gallery for visualization ideas
