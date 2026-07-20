# Quiz 11 — Hypothesis Testing and Chi-Square

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
You're testing whether a new recommendation algorithm increases click-through rate (currently 5%). State H₀ and H₁.

<details><summary>Answer</summary>
H₀: p = 0.05 (the new algorithm has no effect — CTR stays at 5%)
H₁: p > 0.05 (the new algorithm increases CTR)

This is a one-sided test because we're specifically interested in whether CTR INCREASED (not just changed). If we wanted to detect any change (increase or decrease), H₁ would be p ≠ 0.05 (two-sided).
</details>

## Q2
You get a p-value of 0.03. Your significance level is α = 0.05. What do you conclude? What does the p-value actually mean?

<details><summary>Answer</summary>
Since p = 0.03 < α = 0.05, reject H₀. There is statistically significant evidence that the new algorithm increases CTR.

What p = 0.03 means: IF H₀ were true (IF the algorithm had no effect), there's only a 3% chance of observing data this extreme or more extreme. It's NOT "3% chance H₀ is true" — a crucial distinction.

The p-value is the probability of the DATA given H₀, not the probability of H₀ given the data.
</details>

## Q3
You test 20 independent hypotheses at α = 0.05 and find 3 significant results. Should you be concerned about false positives? How many false positives would you expect by chance?

<details><summary>Answer</summary>
Yes! Expected false positives = 20 × 0.05 = 1. Finding 3 is somewhat more than expected by chance, but finding 1-2 "significant" results is completely normal even when ALL null hypotheses are true.

This is the multiple testing problem. Solutions:
- Bonferroni correction: use α/20 = 0.0025 per test (conservative)
- Benjamini-Hochberg FDR: controls the proportion of false discoveries (less conservative)

Never run many tests and report only the significant ones without correction — this is p-hacking.
</details>

## Q4
A die is rolled 120 times with results: {1: 25, 2: 17, 3: 15, 4: 23, 5: 22, 6: 18}. Perform a chi-square goodness-of-fit test. Is the die fair? (Critical value χ²(5, 0.05) = 11.07)

<details><summary>Answer</summary>
Expected under H₀ (fair die): 120/6 = 20 for each face.

χ² = (25-20)²/20 + (17-20)²/20 + (15-20)²/20 + (23-20)²/20 + (22-20)²/20 + (18-20)²/20
   = 25/20 + 9/20 + 25/20 + 9/20 + 4/20 + 4/20
   = 76/20 = 3.80

df = 6 - 1 = 5. Since 3.80 < 11.07 (critical value), fail to reject H₀. No evidence the die is unfair.

The deviations from 20 are within what you'd expect from random variation with 120 rolls.
</details>

## Q5
What's the difference between a Type I error and a Type II error? Which one does α control?

<details><summary>Answer</summary>
Type I error (false positive): rejecting H₀ when it's actually true. "Crying wolf." α directly controls this — it's the maximum probability of Type I error you'll tolerate.

Type II error (false negative): failing to reject H₀ when it's actually false. "Missing the wolf." Its probability is β. Power = 1 - β = probability of correctly detecting a true effect.

The tradeoff: lowering α (stricter threshold) reduces Type I errors but increases Type II errors (you become harder to convince, so you miss real effects). There's no free lunch.

In ML terms: α relates to false positive rate; power relates to recall/sensitivity.
</details>

## Q6
You have a contingency table from an A/B test:

|  | Clicked | Didn't click |
|--|---------|-------------|
| Version A | 45 | 455 |
| Version B | 60 | 440 |

Perform a chi-square test of independence. (Calculate χ² and interpret.)

<details><summary>Answer</summary>
Total: 1000. Row totals: A=500, B=500. Column totals: Clicked=105, Not=895.

Expected values (row total × col total / grand total):
E(A,Click) = 500×105/1000 = 52.5
E(A,NoClick) = 500×895/1000 = 447.5
E(B,Click) = 52.5
E(B,NoClick) = 447.5

χ² = (45-52.5)²/52.5 + (455-447.5)²/447.5 + (60-52.5)²/52.5 + (440-447.5)²/447.5
   = 56.25/52.5 + 56.25/447.5 + 56.25/52.5 + 56.25/447.5
   = 1.071 + 0.126 + 1.071 + 0.126 = 2.394

df = (2-1)(2-1) = 1. Critical value χ²(1, 0.05) = 3.84.

Since 2.394 < 3.84, fail to reject H₀. No statistically significant difference in click rates between versions A and B (9% vs 12%, p > 0.05). Need more data to detect this size difference.
</details>

## Q7
A result is "statistically significant" (p = 0.001) but the effect size is tiny (Model B is 0.1% better than Model A). Should you deploy Model B?

<details><summary>Answer</summary>
Probably not. Statistical significance ≠ practical significance.

With enough data, you can detect arbitrarily small differences. A 0.1% improvement might be:
- Smaller than natural variation in production
- Not worth the engineering cost of deploying a new model
- Within measurement error for any individual user

Always ask: "Is this difference big enough to MATTER?" Consider:
- Business impact (0.1% on 100M users might matter; on 1000 users, no)
- Cost of deployment vs benefit
- Effect size metrics (Cohen's d, relative improvement)

p-values tell you IF an effect exists; effect size tells you if you should CARE.
</details>
