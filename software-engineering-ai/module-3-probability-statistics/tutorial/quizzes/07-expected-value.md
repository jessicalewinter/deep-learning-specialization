# Quiz 07 — Expected Value

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
A game costs $5 to play. You roll a fair die: if you get 6, you win $20; otherwise you win nothing. What's the expected net gain per game? Should you play?

<details><summary>Answer</summary>
Net gain = winnings - cost.
E(net gain) = (1/6 × $20 + 5/6 × $0) - $5 = $3.33 - $5 = -$1.67

No, you should NOT play. On average you lose $1.67 per game. The game has negative expected value — the house always wins in the long run.
</details>

## Q2
True or false: E(X + Y) = E(X) + E(Y) requires X and Y to be independent.

<details><summary>Answer</summary>
FALSE. Linearity of expectation holds ALWAYS — no independence required. E(X + Y) = E(X) + E(Y) even if X and Y are completely dependent. This is one of the most powerful and surprising facts in probability. It's why computing expected values of complicated sums is often easy.

Independence IS required for: Var(X + Y) = Var(X) + Var(Y).
</details>

## Q3
You have a random variable with PMF: P(X=-1) = 0.3, P(X=0) = 0.4, P(X=2) = 0.3. Calculate E(X) and E(X²).

<details><summary>Answer</summary>
E(X) = (-1)(0.3) + (0)(0.4) + (2)(0.3) = -0.3 + 0 + 0.6 = 0.3
E(X²) = (-1)²(0.3) + (0)²(0.4) + (2)²(0.3) = 0.3 + 0 + 1.2 = 1.5

Note: E(X²) = 1.5 ≠ [E(X)]² = 0.09. This is always true unless X is constant. The difference E(X²) - [E(X)]² = 1.5 - 0.09 = 1.41 is the variance.
</details>

## Q4
100 people each flip a fair coin. Let X = total number of heads across all people. What is E(X)? You don't need to know the distribution of X to answer this.

<details><summary>Answer</summary>
E(X) = E(X₁ + X₂ + ... + X₁₀₀) = E(X₁) + E(X₂) + ... + E(X₁₀₀) = 100 × 0.5 = 50.

By linearity of expectation, you just add the individual expectations. You don't need to reason about the binomial distribution at all — linearity makes this trivial. (Of course, X ~ Binomial(100, 0.5) and E = np = 50 gives the same answer.)
</details>

## Q5
A machine learning model gives P(class A) = 0.7 and P(class B) = 0.3. If correctly predicting A earns you 1 point and correctly predicting B earns you 3 points (because it's rare), what prediction maximizes your expected score?

<details><summary>Answer</summary>
E(score | predict A) = 1 × P(A) + 0 × P(B) = 1 × 0.7 = 0.7
E(score | predict B) = 0 × P(A) + 3 × P(B) = 3 × 0.3 = 0.9

Predict B! Even though A is more likely, the asymmetric payoff makes predicting B optimal in expectation. This is exactly why ML uses cost-sensitive classification for imbalanced datasets — the "rare" class might be much more valuable to catch correctly.
</details>

## Q6
Explain in one sentence why E(f(X)) ≠ f(E(X)) in general. Give a simple counterexample.

<details><summary>Answer</summary>
Because expectation is a linear operator but most functions are nonlinear — the average of the outputs ≠ the output of the average.

Counterexample: X takes values 0 and 2 with equal probability. E(X) = 1. f(x) = x². Then f(E(X)) = 1² = 1, but E(f(X)) = E(X²) = (0² + 2²)/2 = 2. They're different because squaring is convex (Jensen's inequality: E(f(X)) ≥ f(E(X)) for convex f).
</details>

## Q7
You run a simulation 10,000 times and compute the sample mean. The Law of Large Numbers says this should be close to E(X). How close? What determines the precision?

<details><summary>Answer</summary>
By the Central Limit Theorem, the sample mean x̄ has standard error = σ/√n = σ/√10000 = σ/100.

The precision depends on:
1. The standard deviation σ of X (more variable X → less precise estimate)
2. The number of samples n (more samples → more precision, but only as √n)

For n=10,000: if σ=1, your estimate is accurate to about ±0.01 (one std error). Quadrupling n only halves the error — diminishing returns. This is the fundamental tradeoff in Monte Carlo simulation.
</details>
