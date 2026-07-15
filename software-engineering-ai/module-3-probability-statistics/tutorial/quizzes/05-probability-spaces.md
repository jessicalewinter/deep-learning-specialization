# Quiz 05 — Probability Spaces (Formal)

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
What are the three components of a probability space? Give a concrete example for flipping a fair coin.

<details><summary>Answer</summary>
(Ω, F, P) where:
- Ω = {H, T} (sample space — all possible outcomes)
- F = {∅, {H}, {T}, {H,T}} (σ-algebra — all subsets, i.e., all questions you can ask)
- P: P({H}) = 0.5, P({T}) = 0.5, P({H,T}) = 1, P(∅) = 0

For a finite sample space, the σ-algebra is typically the power set (all possible subsets), which has 2ⁿ elements where n = |Ω|.
</details>

## Q2
A σ-algebra must be closed under complementation and countable unions. Why is this needed? What goes wrong without it?

<details><summary>Answer</summary>
Without closure under complements: if you can ask "what's P(rain)?", you should be able to ask "what's P(not rain)?". If "rain" is a valid event but "not rain" isn't, the axiom P(Aᶜ) = 1 - P(A) breaks.

Without closure under unions: if A and B are events, A ∪ B should also be an event (you should be able to ask "what's the probability of A or B?"). Without this, you can't do basic probability calculations.

These closure properties ensure that any logical combination of "askable" questions remains askable — the system is self-consistent.
</details>

## Q3
For a loaded die with P(6) = 1/3 and all other faces equally likely, write out the full PMF.

<details><summary>Answer</summary>
Since all probabilities must sum to 1:
P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = 1
5×P(other) + 1/3 = 1
P(other) = (2/3)/5 = 2/15

PMF:
f(1) = f(2) = f(3) = f(4) = f(5) = 2/15 ≈ 0.133
f(6) = 1/3 ≈ 0.333

Check: 5×(2/15) + 1/3 = 10/15 + 5/15 = 15/15 = 1 ✓
</details>

## Q4
Why is P(X = exactly 0.5) = 0 for a continuous uniform distribution on [0,1], even though 0.5 is clearly a possible outcome?

<details><summary>Answer</summary>
For continuous distributions, probability is defined over intervals, not points. There are uncountably many points in [0,1], and if each had positive probability, the total would be infinite (violating P(Ω) = 1).

The probability of any single point is 0, but the probability of an interval [a,b] = b - a > 0. It's like asking "what fraction of a line segment is one specific point?" — zero, because a point has no length.

This is why we use PDF (density) not PMF for continuous variables: f(0.5) = 1 (the density), but P(X = 0.5) = 0.
</details>

## Q5
Verify that the function f(x) = x/10 for x ∈ {1, 2, 3, 4} is a valid PMF. If not, explain why and fix it.

<details><summary>Answer</summary>
Check: f(1) + f(2) + f(3) + f(4) = 1/10 + 2/10 + 3/10 + 4/10 = 10/10 = 1.
Also: all values are non-negative (1/10, 2/10, 3/10, 4/10 ≥ 0).

Yes, it IS a valid PMF. It satisfies both requirements: (1) f(x) ≥ 0 for all x, and (2) Σf(x) = 1. This describes a distribution where larger values are more likely — x=4 is four times as likely as x=1.
</details>

## Q6
What's the difference between σ-additivity (countable additivity) and finite additivity? Why does it matter?

<details><summary>Answer</summary>
Finite additivity: P(A₁ ∪ A₂ ∪ ... ∪ Aₙ) = P(A₁) + ... + P(Aₙ) for finitely many disjoint events.

σ-additivity: the same rule holds for countably infinite disjoint events (A₁, A₂, A₃, ...).

It matters for continuous distributions and infinite sample spaces. For example, the probability of a geometric random variable: P(X=1) + P(X=2) + P(X=3) + ... must equal 1. σ-additivity guarantees this infinite sum behaves correctly. Without it, you can construct paradoxical probability assignments on infinite spaces.
</details>
