# Quiz 04 — Descriptive Statistics

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
Dataset: [2, 3, 5, 7, 8, 10, 12, 100]. Calculate the mean and median. Which one better represents the "typical" value? Why?

<details><summary>Answer</summary>
Mean = (2+3+5+7+8+10+12+100)/8 = 147/8 = 18.375
Median = (7+8)/2 = 7.5

The median (7.5) is far more representative. The mean (18.375) is inflated by the outlier 100. Seven out of eight values are ≤ 12, so 18.4 is misleading as a "typical" value. This is why income and house prices are reported as medians.
</details>

## Q2
Why does the formula for sample variance divide by (n-1) instead of n?

<details><summary>Answer</summary>
Bessel's correction. When you compute deviations from the sample mean x̄ (instead of the true population mean μ), you systematically underestimate the spread — because x̄ is chosen to be as close to the data as possible, making deviations artificially small. Dividing by (n-1) corrects this bias, giving an unbiased estimator of σ².

Technically: the n deviations from x̄ always sum to zero (they're constrained), so you only have (n-1) independent pieces of information (degrees of freedom).
</details>

## Q3
Compute the IQR of: [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]. Would a value of 100 be considered an outlier by the 1.5×IQR rule?

<details><summary>Answer</summary>
Q1 = 20 (25th percentile), Q3 = 50 (75th percentile). IQR = 50 - 20 = 30.

Outlier threshold (upper): Q3 + 1.5×IQR = 50 + 45 = 95.
Since 100 > 95, yes — it would be flagged as an outlier.

Lower threshold: Q1 - 1.5×IQR = 20 - 45 = -25 (no lower outliers possible with positive data).
</details>

## Q4
A distribution has mean = 70, median = 70, mode = 70. What can you say about its shape?

<details><summary>Answer</summary>
It's symmetric (or very close to it). When mean = median = mode, the distribution is unimodal and symmetric. The classic example is the normal distribution. However, this alone doesn't guarantee normality — a uniform distribution also has mean = median (though it has no clear single mode).
</details>

## Q5
Your dataset of test scores has mean = 75 and standard deviation = 10. Without assuming any particular distribution, what can you guarantee about the percentage of scores between 55 and 95?

<details><summary>Answer</summary>
By Chebyshev's inequality: at least 1 - 1/k² of data lies within k standard deviations of the mean. Here k = 2 (since 75±20 = [55, 95] = mean ± 2σ).

At least 1 - 1/4 = 75% of scores are between 55 and 95.

This works for ANY distribution. If we additionally assume normality, the 68-95-99.7 rule gives ~95%. But Chebyshev makes no distributional assumptions.
</details>

## Q6
You have two datasets with the same mean (50): Dataset A has std = 2, Dataset B has std = 15. Describe in words what each dataset "looks like."

<details><summary>Answer</summary>
Dataset A (std=2): values are tightly clustered around 50. Most values fall between ~46 and ~54. Very homogeneous — like measuring the same thing repeatedly with a precise instrument.

Dataset B (std=15): values are widely spread. They range roughly from 20 to 80 (mean ± 2σ). Much more variability — like measuring different people's ages in a workplace.

Same center, completely different spreads. The mean alone tells you very little about a distribution.
</details>

## Q7
In NumPy, `np.std(data)` and `np.std(data, ddof=1)` give different results. Which should you use when computing from a sample, and what's the numerical difference for a dataset of n=5?

<details><summary>Answer</summary>
Use `ddof=1` for sample standard deviation (Bessel's correction — divides by n-1).

For n=5: `ddof=0` divides by 5, `ddof=1` divides by 4. The ddof=1 version is always larger: specifically, std_sample = std_population × √(n/(n-1)) = std_population × √(5/4) ≈ 1.118× larger.

Note: Pandas `.std()` defaults to ddof=1 (correct for samples). NumPy `.std()` defaults to ddof=0 (population). This inconsistency trips people up constantly.
</details>

## Q8
A box plot shows: min=20, Q1=35, median=50, Q3=65, max=80, with one dot at 120. Interpret this visualization.

<details><summary>Answer</summary>
- The box (Q1 to Q3) spans 35–65, containing the middle 50% of data. IQR = 30.
- The median line at 50 is centered in the box, suggesting symmetry in the middle half.
- Whiskers extend to 20 and 80 (within 1.5×IQR = 45 of the box edges).
- The dot at 120 is an outlier (120 > Q3 + 1.5×IQR = 65 + 45 = 110).
- Overall: roughly symmetric distribution with one high outlier. The outlier is worth investigating — is it a data entry error, or a genuinely unusual observation?
</details>
