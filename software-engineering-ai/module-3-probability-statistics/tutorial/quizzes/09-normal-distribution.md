# Quiz 09 — The Normal Distribution

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
Heights of adult women in Brazil follow approximately N(160, 6²) (mean 160cm, std 6cm). What percentage of women are between 154cm and 166cm?

<details><summary>Answer</summary>
154 = 160 - 6 = μ - 1σ, and 166 = 160 + 6 = μ + 1σ.

By the 68-95-99.7 rule: approximately 68% of women have heights between 154cm and 166cm. This is the "within 1 standard deviation" range.
</details>

## Q2
Using the same height distribution N(160, 6²): a woman is 175cm tall. What is her z-score? How unusual is this height?

<details><summary>Answer</summary>
z = (X - μ) / σ = (175 - 160) / 6 = 15/6 = 2.5

A z-score of 2.5 means she is 2.5 standard deviations above the mean. Only about 0.62% of women are taller (looking up P(Z > 2.5) ≈ 0.0062 in a z-table or using scipy). She'd be taller than roughly 99.4% of women — quite unusual.
</details>

## Q3
The PDF of a normal distribution at μ is about 0.4/σ. For N(0, 0.25²), the peak is 0.4/0.25 = 1.6. Does this mean P(X = 0) = 1.6?

<details><summary>Answer</summary>
NO. The y-axis of a PDF is DENSITY, not probability. For continuous distributions, P(X = any specific value) = 0 always. The density can exceed 1 without violating any rule.

What f(0) = 1.6 means: in a tiny interval around 0 (say [−ε, ε]), the probability is approximately 1.6 × 2ε. Only areas (integrals) give probabilities. The total area under the curve is still exactly 1.
</details>

## Q4
You measure the average test score of 36 students. The population has μ=70 and σ=12. What's the probability that your sample mean exceeds 74?

<details><summary>Answer</summary>
By CLT: x̄ ~ N(μ, σ²/n) = N(70, 144/36) = N(70, 4), so SE = σ/√n = 12/6 = 2.

z = (74 - 70) / 2 = 2.0

P(x̄ > 74) = P(Z > 2) ≈ 0.0228 (about 2.3%).

It's unlikely (but not impossible) to get a sample mean of 74 when the true mean is 70 with n=36 students. This is the foundation of hypothesis testing.
</details>

## Q5
Which of these scenarios would NOT be well-modeled by a normal distribution? (a) Heights of adults, (b) Income, (c) Measurement errors, (d) IQ scores.

<details><summary>Answer</summary>
(b) Income is NOT well-modeled by a normal distribution. Income is strongly right-skewed (a few very high earners pull the tail far right) and cannot be negative. It's better modeled by a log-normal distribution.

The others ARE approximately normal: (a) heights are roughly symmetric around a mean, (c) measurement errors are classic normal by CLT, (d) IQ is designed to be N(100, 15²).

Key giveaway: if the variable can't be negative and has no upper bound, it's probably not normal.
</details>

## Q6
Explain the Central Limit Theorem in one sentence. Why is it "the most important theorem in statistics"?

<details><summary>Answer</summary>
The CLT says: the average of n independent observations approaches a normal distribution as n grows, REGARDLESS of the original distribution's shape.

It's the most important theorem because it justifies using normal-based methods (z-tests, confidence intervals, etc.) even when the underlying data isn't normal — as long as your sample is large enough. It's why the normal distribution appears everywhere in nature: anything that results from adding many small independent effects ends up approximately normal.
</details>

## Q7
Two ML models produce prediction errors. Model A: errors ~ N(0, 2²). Model B: errors ~ N(0.5, 1²). Which model has (a) less bias? (b) less variance? (c) smaller mean squared error?

<details><summary>Answer</summary>
(a) Less bias: Model A (mean error = 0 vs 0.5). It's centered on the truth.
(b) Less variance: Model B (σ² = 1 vs 4). Its predictions are more consistent.
(c) MSE = Var + Bias² (the bias-variance decomposition!):
   - Model A: MSE = 4 + 0² = 4
   - Model B: MSE = 1 + 0.5² = 1.25

Model B has smaller MSE despite being biased! This illustrates the bias-variance tradeoff: a small amount of bias can be worth it if it substantially reduces variance.
</details>
