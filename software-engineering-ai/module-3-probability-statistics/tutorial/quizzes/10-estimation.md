# Quiz 10 — Point and Interval Estimation

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
You sample 50 people and find a mean height of 168cm with s = 8cm. Compute the 95% confidence interval for the population mean. (Use z ≈ 1.96 since n is large.)

<details><summary>Answer</summary>
CI = x̄ ± z × (s/√n) = 168 ± 1.96 × (8/√50) = 168 ± 1.96 × 1.131 = 168 ± 2.22

95% CI: (165.78, 170.22)

We're 95% confident that the true population mean height is between 165.78cm and 170.22cm. (More precisely: if we repeated this sampling 100 times, about 95 of the resulting intervals would contain the true μ.)
</details>

## Q2
Your colleague says "there's a 95% probability that the true mean is between 165.78 and 170.22." What's wrong with this statement?

<details><summary>Answer</summary>
The true mean μ is a fixed (unknown) number — it either IS or ISN'T in the interval. There's no probability about it. The 95% refers to the PROCEDURE, not this specific interval.

Correct interpretation: "If we repeated this study many times, 95% of the confidence intervals we'd construct would contain the true μ." This particular interval either captured μ or it didn't — we just don't know which.

This is a subtle but fundamental point in frequentist statistics. (Bayesian credible intervals DO allow the probabilistic interpretation, which is partly why some prefer them.)
</details>

## Q3
You want to estimate a population proportion (e.g., fraction of users who click a button). You sample 400 users and 120 click. Give the 95% confidence interval for the true proportion.

<details><summary>Answer</summary>
p̂ = 120/400 = 0.30
SE = √(p̂(1-p̂)/n) = √(0.30 × 0.70 / 400) = √(0.000525) ≈ 0.0229

CI = p̂ ± z × SE = 0.30 ± 1.96 × 0.0229 = 0.30 ± 0.045

95% CI: (0.255, 0.345) or equivalently (25.5%, 34.5%)

The true click rate is likely between 25.5% and 34.5%.
</details>

## Q4
You currently have n=100 samples and a CI width of ±5. Your boss wants the CI width to be ±2.5 (half as wide). How many samples do you need?

<details><summary>Answer</summary>
CI width is proportional to 1/√n. To halve the width, you need to quadruple n.

n_new = 100 × (5/2.5)² = 100 × 4 = 400 samples.

This is the "√n penalty" — doubling precision requires 4× the data. It's why very precise estimates are expensive. Going from ±5 to ±2.5 costs 300 extra samples; going from ±2.5 to ±1.25 would need 1600 total.
</details>

## Q5
What does it mean for an estimator to be "unbiased"? Is the sample mean an unbiased estimator of the population mean? What about the sample standard deviation?

<details><summary>Answer</summary>
Unbiased means E(estimator) = true parameter. On average, across many samples, the estimator hits the right target.

- Sample mean (x̄): YES, unbiased for μ. E(x̄) = μ always.
- Sample variance (s² with n-1): YES, unbiased for σ².
- Sample standard deviation (s = √s²): actually slightly BIASED for σ! E(√s²) ≠ √E(s²) because of Jensen's inequality (square root is concave). The bias is small for large n and usually ignored.

Unbiased doesn't mean accurate for any single sample — it means no systematic over/under-estimation across many samples.
</details>

## Q6
You're comparing two ML models. Model A: accuracy 0.87 with 95% CI (0.84, 0.90). Model B: accuracy 0.85 with 95% CI (0.82, 0.88). Can you conclude A is better?

<details><summary>Answer</summary>
No — the confidence intervals overlap substantially. (0.84, 0.90) and (0.82, 0.88) share the range (0.84, 0.88). Overlapping CIs suggest the difference might not be statistically significant.

However, overlapping CIs don't prove NO difference either (the threshold is more nuanced). The proper test is a direct comparison — a paired t-test on fold scores, or a CI on the difference (A - B). If the CI for (A - B) includes 0, you can't conclude a difference.

Key lesson: always test the DIFFERENCE directly rather than eyeballing overlap of individual CIs.
</details>

## Q7
Why is the t-distribution used instead of the normal when n is small (say n=10)?

<details><summary>Answer</summary>
When n is small, the sample standard deviation s is an unreliable estimate of σ — it might be too small by chance, making the CI too narrow and the test too aggressive (rejecting H₀ too often).

The t-distribution has heavier tails than the normal, accounting for this extra uncertainty. With df=9 (n-1), the critical value for 95% is t ≈ 2.26 (vs z=1.96), giving a wider, more honest CI.

As n → ∞, s → σ, the extra uncertainty vanishes, and t → z. For n > 30, the difference is negligible.
</details>
