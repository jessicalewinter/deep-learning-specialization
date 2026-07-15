# Quiz 06 — Discrete Probability Distributions

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
A classifier has 80% accuracy. You classify 10 independent samples. What distribution models the number of correct classifications? What are its parameters?

<details><summary>Answer</summary>
Binomial(n=10, p=0.8). Each classification is an independent Bernoulli trial (correct/incorrect) with P(correct) = 0.8. The count of successes in n independent trials with the same probability is binomial.
</details>

## Q2
For X ~ Binomial(10, 0.8), calculate P(X = 10) — the probability of getting all 10 correct.

<details><summary>Answer</summary>
P(X=10) = C(10,10) × 0.8¹⁰ × 0.2⁰ = 1 × 0.8¹⁰ × 1 = 0.8¹⁰ ≈ 0.1074.

About 10.7% — even with 80% accuracy per sample, getting a perfect streak of 10 is not that likely.
</details>

## Q3
What's the expected value and standard deviation of Binomial(100, 0.3)?

<details><summary>Answer</summary>
E(X) = np = 100 × 0.3 = 30
Var(X) = np(1-p) = 100 × 0.3 × 0.7 = 21
SD(X) = √21 ≈ 4.58

So in 100 trials with 30% success rate, you'd expect about 30 successes, typically ranging from about 21 to 39 (mean ± 2σ).
</details>

## Q4
You roll a fair die. What distribution does this follow? Calculate P(X ≤ 3).

<details><summary>Answer</summary>
Discrete Uniform on {1, 2, 3, 4, 5, 6}. Each outcome has probability 1/6.

P(X ≤ 3) = P(X=1) + P(X=2) + P(X=3) = 1/6 + 1/6 + 1/6 = 3/6 = 0.5.

This is the CDF evaluated at 3: F(3) = 0.5.
</details>

## Q5
Explain the difference between PMF and CDF. If P(X=0) = 0.2, P(X=1) = 0.5, P(X=2) = 0.3, what are F(0), F(1), F(2)?

<details><summary>Answer</summary>
PMF (f): gives probability of EXACTLY that value. f(1) = P(X = 1) = 0.5.
CDF (F): gives probability of AT MOST that value. F(1) = P(X ≤ 1).

F(0) = P(X ≤ 0) = P(X=0) = 0.2
F(1) = P(X ≤ 1) = P(X=0) + P(X=1) = 0.2 + 0.5 = 0.7
F(2) = P(X ≤ 2) = 0.2 + 0.5 + 0.3 = 1.0

The CDF is always non-decreasing and ends at 1.
</details>

## Q6
A rare disease affects 1 in 1000 people. You test 5000 people. Using Binomial(5000, 0.001), what's the expected number of cases? Would this be well-approximated by a Poisson distribution? If so, with what parameter?

<details><summary>Answer</summary>
E(X) = np = 5000 × 0.001 = 5 cases expected.

Yes — when n is large and p is small (so np is moderate), the Binomial is well-approximated by Poisson(λ = np) = Poisson(5). This is the "law of rare events."

The Poisson approximation works well when n ≥ 20 and p ≤ 0.05 (or more practically, when np ≤ 10 and n is large).
</details>

## Q7
You're building a spam classifier. For a single email, the model outputs P(spam) = 0.7. If you classify it as spam when P(spam) ≥ 0.5, what's the probability of a correct classification? What distribution models this single decision?

<details><summary>Answer</summary>
The decision is Bernoulli(p = 0.7). Since P(spam) = 0.7 ≥ 0.5, you classify as spam. The probability of being correct IS 0.7 (the model's confidence).

The single binary outcome (correct/incorrect) with fixed probability is the definition of a Bernoulli trial. If you did this for n emails independently (each with possibly different p), the total correct classifications would NOT be binomial (because p varies) — it would be a Poisson-binomial distribution.
</details>

## Q8
Why does the binomial formula include C(n,k)? Explain with the example of getting exactly 2 heads in 3 flips.

<details><summary>Answer</summary>
C(n,k) counts the NUMBER OF WAYS to arrange k successes in n trials:
- HHT (heads, heads, tails)
- HTH
- THH

There are C(3,2) = 3 ways. Each specific sequence has probability p²(1-p)¹ = 0.5² × 0.5 = 0.125. Since there are 3 such sequences:

P(X=2) = C(3,2) × 0.5² × 0.5¹ = 3 × 0.125 = 0.375.

Without C(n,k), you'd only be computing the probability of ONE specific ordering (like HHT), not ALL orderings that give 2 heads.
</details>
