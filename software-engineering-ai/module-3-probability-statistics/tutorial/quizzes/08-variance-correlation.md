# Quiz 08 — Variance and Correlation

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
X has E(X) = 5 and E(X²) = 30. What is Var(X)?

<details><summary>Answer</summary>
Var(X) = E(X²) - [E(X)]² = 30 - 25 = 5.

This computational formula (E(X²) - μ²) is almost always easier than computing Σ(xᵢ - μ)² directly.
</details>

## Q2
If Y = 3X + 7, and Var(X) = 4, what is Var(Y)?

<details><summary>Answer</summary>
Var(aX + b) = a² × Var(X).

Var(Y) = 3² × 4 = 9 × 4 = 36.

The additive constant (+7) doesn't affect variance — shifting data doesn't change its spread. The multiplier (×3) gets squared because variance uses squared deviations.
</details>

## Q3
Two stocks have: Var(A) = 100, Var(B) = 100, Cov(A,B) = -50. What is Var(A + B)? Why is this relevant to portfolio diversification?

<details><summary>Answer</summary>
Var(A + B) = Var(A) + Var(B) + 2×Cov(A,B) = 100 + 100 + 2×(-50) = 100.

The portfolio's variance (100) is LESS than the sum of individual variances (200). Negative covariance means when A goes up, B tends to go down — they partially cancel each other's risk. This is diversification: combining negatively correlated assets reduces overall portfolio variance. If Cov were 0 (independent), Var(A+B) = 200. If Cov were +50, Var(A+B) = 300 — worse than holding either alone!
</details>

## Q4
Dataset: X = [1, 2, 3, 4, 5], Y = [5, 4, 3, 2, 1]. Without computing, what is the correlation coefficient r? Why?

<details><summary>Answer</summary>
r = -1 (exactly).

Y is a perfect linear function of X: Y = -X + 6. When the relationship is a perfect downward line (every point exactly on the line), correlation is -1. The sign tells direction (negative = inverse relationship), and the magnitude tells strength (1 = perfect linear).
</details>

## Q5
You compute r = 0.02 between "number of ice cream shops in a city" and "number of drowning deaths." Can you conclude these are unrelated?

<details><summary>Answer</summary>
No, for two reasons:
1. r ≈ 0 means no LINEAR relationship, but there could be a non-linear one.
2. More importantly: both variables are likely driven by a confounding variable — city population (or temperature/summer season). Larger cities have more of everything. This is why "correlation ≠ causation" and why you need to control for confounders.

In this case, the low r might be because the relationship is mediated through population size rather than direct. Per-capita rates might show a very different picture.
</details>

## Q6
You're selecting features for an ML model. Feature A has correlation 0.95 with the target, and Feature B has correlation 0.93 with the target. Features A and B have correlation 0.99 with each other. Should you include both? Why or why not?

<details><summary>Answer</summary>
Probably not. Features A and B are nearly identical (r=0.99), so they carry almost the same information. Including both:
- Adds almost no predictive power
- Increases model complexity and risk of overfitting
- Can cause multicollinearity issues in linear models (unstable coefficients)

Better approach: pick the one with higher correlation to the target (A, at 0.95) and drop the other. Or use PCA to combine them into one component. The marginal gain from B is tiny because anything B "knows" about the target, A already knows too.
</details>

## Q7
Var(X) = 0. What does this tell you about X?

<details><summary>Answer</summary>
X is a constant (with probability 1). If Var(X) = E[(X-μ)²] = 0, then (X-μ)² = 0 always (since it's a non-negative quantity whose average is 0). Therefore X = μ always — there is no randomness.

In data terms: every value in the dataset is identical. In ML: a feature with zero variance carries no information and should be dropped.
</details>
