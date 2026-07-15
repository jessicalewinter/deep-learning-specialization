# Quiz 12 — Comparing Means (t-Test)

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
You have 10 cross-validation scores for Model A: [0.82, 0.85, 0.83, 0.86, 0.84, 0.87, 0.83, 0.85, 0.84, 0.86]. Test whether the true mean accuracy is greater than 0.80. (One-sample t-test, α = 0.05.)

<details><summary>Answer</summary>
x̄ = 0.845, s ≈ 0.0158, n = 10
t = (x̄ - μ₀) / (s/√n) = (0.845 - 0.80) / (0.0158/√10) = 0.045 / 0.005 = 9.0

df = 9. Critical value t(9, 0.05) one-tailed ≈ 1.833.

Since 9.0 >> 1.833, reject H₀ strongly. The model's accuracy is significantly greater than 0.80 (p < 0.0001). This is not even close to borderline — the evidence is overwhelming.
</details>

## Q2
When should you use a paired t-test instead of an independent two-sample t-test?

<details><summary>Answer</summary>
Use a paired t-test when observations are MATCHED — each measurement in group 1 has a natural partner in group 2:

- Same subjects measured before and after treatment
- Same cross-validation folds evaluated by two different models
- Same cities measured in two different years
- Left eye vs right eye of the same patients

The paired test is more powerful because it eliminates between-subject variability. If folds 1-10 vary in difficulty, the paired test removes that source of noise by looking at the DIFFERENCE within each fold.

Use independent t-test when groups have no natural pairing (different people in each group, different random samples).
</details>

## Q3
Model A scores: [0.88, 0.86, 0.90, 0.85, 0.89]. Model B scores on same folds: [0.85, 0.84, 0.87, 0.86, 0.85]. Compute the t-statistic for the paired test.

<details><summary>Answer</summary>
Differences d = A - B: [0.03, 0.02, 0.03, -0.01, 0.04]
d̄ = (0.03+0.02+0.03-0.01+0.04)/5 = 0.11/5 = 0.022

s_d = √[Σ(dᵢ - d̄)²/(n-1)]
Deviations from d̄: [0.008, -0.002, 0.008, -0.032, 0.018]
Squared: [0.000064, 0.000004, 0.000064, 0.001024, 0.000324]
Sum = 0.00148, s_d² = 0.00148/4 = 0.00037, s_d ≈ 0.01924

t = d̄ / (s_d/√n) = 0.022 / (0.01924/√5) = 0.022 / 0.0086 = 2.56

df = 4. Critical t(4, 0.05) two-tailed ≈ 2.776. Since 2.56 < 2.776, fail to reject H₀ (barely). With only 5 folds, we don't have enough power to confirm Model A is better, even though it looks better on 4/5 folds.
</details>

## Q4
Why is the t-distribution wider (heavier-tailed) than the normal? Draw the connection to sample size.

<details><summary>Answer</summary>
The t-distribution is wider because it accounts for UNCERTAINTY IN ESTIMATING σ. With small n, the sample standard deviation s is unreliable — it might be too small by chance, which would make the test statistic look larger than it should.

The heavier tails say: "extreme values of the test statistic are more likely than a normal would predict, because s might be off." This prevents us from being overconfident with small samples.

As n → ∞, s → σ (the estimate becomes reliable), the extra uncertainty vanishes, and t → N(0,1). For n > 30, the difference is barely noticeable. For n = 5, it's substantial (critical value ~2.78 vs 1.96).
</details>

## Q5
You run a Welch's t-test comparing two groups and get p = 0.048. Your colleague argues you should use the equal-variance t-test instead, which gives p = 0.042. Which should you report?

<details><summary>Answer</summary>
Report Welch's (p = 0.048). The equal-variance (pooled) t-test ASSUMES σ₁ = σ₂. If this assumption is wrong, the pooled test can give misleading results (either too liberal or too conservative).

Welch's t-test makes no assumption about equal variances and is always valid. When variances ARE equal, Welch's is only slightly less powerful than the pooled test. When they're NOT equal, the pooled test can be seriously wrong.

Default rule: always use Welch's unless you have strong, independent evidence that variances are equal. The difference in this case (0.048 vs 0.042) is trivial and both barely cross α=0.05 — this borderline case should make you cautious about claiming significance regardless of which test you use.
</details>

## Q6
You want to compare 5 models simultaneously. Why can't you just run 10 pairwise t-tests?

<details><summary>Answer</summary>
Multiple comparisons problem. With 10 tests at α=0.05, the probability of at least one false positive is:
1 - (1 - 0.05)¹⁰ ≈ 0.40 (40%!)

You have a 40% chance of "finding" a difference that doesn't exist. This is like testing 10 people for a rare disease with a 5% false-positive rate — you expect half a false positive.

Solutions:
- Bonferroni: use α/10 = 0.005 per test (conservative)
- Tukey's HSD: designed for all pairwise comparisons
- ANOVA first: test "is there ANY difference?" before pairwise comparisons
- Friedman test: non-parametric alternative for repeated measures

In ML: Demšar (2006) recommends Friedman test + Nemenyi post-hoc for comparing multiple classifiers.
</details>

## Q7
Your paired t-test gives t = 1.5 with df = 4 (p ≈ 0.21). You can't reject H₀. Does this prove the models are equally good?

<details><summary>Answer</summary>
NO. "Fail to reject H₀" ≠ "H₀ is true." It means you lack sufficient evidence to conclude they're different. With only 5 folds (df=4), you have very low statistical power — you might miss a real difference.

Possible reasons for non-significance:
1. The models truly perform the same (H₀ is true)
2. There IS a difference but n=5 is too small to detect it (low power)
3. The variability across folds is too high relative to the effect

What to do: report the confidence interval for the difference. If it's wide (like -0.02 to +0.06), that shows your uncertainty is too large to conclude anything. Consider using more folds (10-fold CV), more repeated runs, or larger datasets to increase power.
</details>
