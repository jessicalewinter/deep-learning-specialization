# Quiz 03 — Exploratory Data Analysis

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
Classify each variable: (a) eye color, (b) temperature in Celsius, (c) education level (high school / bachelor / master / PhD), (d) number of siblings.

<details><summary>Answer</summary>
(a) Qualitative nominal — categories with no natural order.
(b) Quantitative continuous — can take any value in a range.
(c) Qualitative ordinal — categories with a meaningful order but no fixed distance between them.
(d) Quantitative discrete — countable whole numbers.
</details>

## Q2
You have 200 data points and the values range from 10 to 90. If you create a histogram with 8 equal-width bins, what is the width of each bin?

<details><summary>Answer</summary>
Width = (max - min) / number of bins = (90 - 10) / 8 = 80 / 8 = 10. Each bin covers a range of 10 units: [10,20), [20,30), ..., [80,90].
</details>

## Q3
A bin in a histogram contains 40 out of 200 data points and has width 10. What is its frequency density?

<details><summary>Answer</summary>
Relative frequency = 40/200 = 0.20.
Frequency density = relative frequency / bin width = 0.20 / 10 = 0.02.

The density is what goes on the y-axis of a proper density histogram, making the area of the bar equal to the proportion (0.02 × 10 = 0.20 = 20% of data in this bin).
</details>

## Q4
What's the difference between a bar chart and a histogram? When would you use each?

<details><summary>Answer</summary>
Bar chart: for categorical/discrete data. Bars have gaps between them (the x-axis is not a continuous scale). Order of bars is arbitrary for nominal data.

Histogram: for continuous data. Bars touch (the x-axis IS a continuous scale). Order matters. Area of each bar represents proportion.

Use a bar chart for: favorite color, programming language used, country of origin.
Use a histogram for: heights, salaries, response times, model predictions.
</details>

## Q5
You're exploring a dataset and find a column called "satisfaction_score" with values 1, 2, 3, 4, 5. Is this quantitative or qualitative? Does it matter?

<details><summary>Answer</summary>
It's ambiguous — and yes, it matters. If 1-5 represents a Likert scale ("strongly disagree" to "strongly agree"), it's ordinal (qualitative) — the distances between levels aren't necessarily equal. Computing a mean of ordinal data is technically invalid (is the "distance" from 1→2 the same as 4→5?).

In practice, many researchers treat 5-point scales as approximately quantitative, but it's a strong assumption. The safe choice: report median and mode, not mean. If you do report mean, acknowledge the assumption.
</details>

## Q6
You run `df.describe()` in pandas and get: mean=50, std=10, min=5, 25%=45, 50%=52, 75%=57, max=90. What does this suggest about the distribution shape?

<details><summary>Answer</summary>
The distribution is likely left-skewed (or has a low outlier). Evidence:
- Mean (50) < Median (52): the mean is pulled left by low values.
- The distance from min to Q1 (5→45 = 40) is much larger than Q3 to max (57→90 = 33), but more importantly, min=5 is very far from Q1=45, suggesting a long left tail or extreme low outlier.
- Q1 to median (7 units) vs median to Q3 (5 units) are similar, so the middle 50% is roughly symmetric.

This pattern (mean < median, long left tail) is typical of exam scores where most people do well but a few do very poorly.
</details>

## Q7
Why should you ALWAYS do EDA before building an ML model? Give at least two specific problems EDA can catch.

<details><summary>Answer</summary>
1. **Data quality issues**: missing values coded as -999 or "N/A" strings, duplicate rows, impossible values (negative ages, heights of 9999cm).
2. **Feature problems**: highly correlated features (redundant information), features with zero variance (constant column), features with extreme skew needing transformation.
3. **Class imbalance**: 99% negative, 1% positive — a model predicting "always negative" gets 99% accuracy but is useless.
4. **Outliers**: a single salary of $10M in a dataset of $40k-$80k salaries will dominate the mean and distort model training.
5. **Data leakage**: a feature that perfectly correlates with the target because it was computed FROM the target.

Any two of these (or similar) is correct. The point: debugging a model is 10x harder than catching data problems early.
</details>
