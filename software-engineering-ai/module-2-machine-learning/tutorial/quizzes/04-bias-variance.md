# Quiz 04 — Bias–Variance Tradeoff

## Q1
Diagnose each scenario as bias problem, variance problem, both, or fine:

a) Train acc 99%, val acc 71%
b) Train acc 73%, val acc 71%
c) Train acc 96%, val acc 94%
d) Train acc 60%, val acc 45%

<details><summary>Answer</summary>
a) Variance — huge gap, model memorized · b) Bias — both bad, gap small means model can't even fit training · c) Fine, slight variance · d) Both — high training error (bias) AND a 15-point gap (variance). The model is too weak *and* overfitting what little it learns. Probably wrong architecture or terrible features.
</details>

## Q2
You have a high-bias model. Which of these will help, and which will make it worse?

- More training data
- Adding L2 regularization
- Increasing model capacity
- Adding dropout
- Better features

<details><summary>Answer</summary>
Help: increasing model capacity, better features. Won't help: more training data (the model already can't fit what it has — more won't change that). Make it worse: L2 regularization and dropout (both are variance-reducing techniques that add bias).
</details>

## Q3
What is "irreducible noise" and why does it matter for goal-setting?

<details><summary>Answer</summary>
It's variance in the labels that no model could predict — caused by inherent randomness, label noise, or features the data doesn't contain. It sets a hard ceiling on achievable performance. If human experts disagree on 8% of cases, you shouldn't expect a model to exceed 92% accuracy — chasing higher numbers means you're fitting noise. Estimating this floor (often via human-level performance benchmarks) is how Andrew Ng frames a lot of practical ML strategy.
</details>

## Q4
Why does the bias–variance decomposition use the *expected* prediction over training sets, not just one training run?

<details><summary>Answer</summary>
Variance is by definition about how predictions change *across different training sets*. If you only train once, you can't observe variance — you just get one prediction. The decomposition is a statistical statement: imagine training your same model architecture on many different samples from the data distribution. Bias is how far the average prediction is from truth; variance is how much that prediction wobbles. In practice you can't actually train on infinite samples, but you can approximate variance via cross-validation or bootstrap.
</details>

## Q5
You have a model with high variance. List three things you could try, in rough order of "easiest first."

<details><summary>Answer</summary>
1) Stronger regularization (turn up weight decay, dropout) — usually a one-line change · 2) Reduce model capacity (smaller network, fewer features) · 3) Get more training data, including augmentation if collecting new data is hard · Bonus: ensemble multiple models (averaging reduces variance). The "easiest" depends on context, but regularization is usually the cheapest first move.
</details>

## Q6
True or false: with enough training data, you can always reduce variance to zero.

<details><summary>Answer</summary>
True in the limit (with infinite data and a well-specified model class), but irreducible noise σ² remains. Variance decreases roughly like 1/N (for many models), so doubling the data halves the variance. But you'll hit diminishing returns and never break the noise floor. Also, "well-specified" matters: if your model class is wrong (e.g., fitting a line to a parabola), more data reduces variance but bias remains constant — your line will just be the *consistent average* wrong line.
</details>
