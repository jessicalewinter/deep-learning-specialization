# 02 — Random Experiments and Probability

## TL;DR

A **random experiment** is any process whose outcome you can't predict with certainty. **Probability** is a function that assigns a number between 0 and 1 to each event, following three axioms. Conditional probability answers: "given that I *know* something happened, how does that change what else I expect?"

## Why it matters

Every ML model outputs probabilities (or things we interpret as probabilities). Understanding what probability *is* — and especially conditional probability — is the foundation for Bayes' theorem, likelihood, and every probabilistic model you'll encounter.

## Core concept

### The three axioms of probability

Any probability function P must satisfy:

1. **Non-negativity**: P(A) ≥ 0 for any event A
2. **Normalization**: P(Ω) = 1 (something must happen)
3. **Additivity**: If A and B are mutually exclusive, P(A ∪ B) = P(A) + P(B)

From just these three rules, everything else follows.

### Immediate consequences

- P(∅) = 0 (impossible event has zero probability)
- P(Aᶜ) = 1 - P(A)
- P(A ∪ B) = P(A) + P(B) - P(A ∩ B) (inclusion-exclusion)

### Conditional probability

The probability of A *given that B happened*:

```
P(A|B) = P(A ∩ B) / P(B),  provided P(B) > 0
```

**Intuition:** once you know B happened, your new "universe" shrinks from Ω to just B. The conditional probability is the fraction of B that also belongs to A.

### Multiplication rule

Rearranging the conditional probability formula:

```
P(A ∩ B) = P(A|B) × P(B) = P(B|A) × P(A)
```

This is the gateway to Bayes' theorem.

## Math

**Example:** A bag has 3 red and 7 blue balls. You draw two without replacement.

P(2nd is red | 1st was red) = 2/9

Because after removing one red ball, you have 2 red out of 9 remaining.

P(both red) = P(1st red) × P(2nd red | 1st red) = (3/10) × (2/9) = 6/90 = 1/15

## Code example

```python
import random

def simulate_conditional(n_trials=100_000):
    """Estimate P(sum >= 9 | first die is 5) by simulation."""
    count_b = 0  # first die is 5
    count_ab = 0  # first die is 5 AND sum >= 9

    for _ in range(n_trials):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == 5:
            count_b += 1
            if d1 + d2 >= 9:
                count_ab += 1

    return count_ab / count_b

estimated = simulate_conditional()
exact = 4/6  # given d1=5, need d2>=4, so {4,5,6} → 3... wait
# given d1=5, need d2>=4: {4,5,6} = 3 outcomes out of 6 → 3/6 = 0.5
exact = 3/6
print(f"Simulated: {estimated:.4f}")
print(f"Exact:     {exact:.4f}")
```

## Common pitfalls

- **Confusing P(A|B) with P(B|A)** — the "prosecutor's fallacy." P(evidence|guilty) ≠ P(guilty|evidence). This confusion has literally sent innocent people to prison.
- **Applying additivity to non-exclusive events** — P(A or B) = P(A) + P(B) only works when A∩B = ∅.
- **Ignoring the denominator in conditional probability** — "given B" means you've restricted your universe. The denominator P(B) is doing real work.

## Further reading

- DeGroot & Schervish, Chapters 1–2
- Blitzstein & Hwang, *Introduction to Probability*, Chapter 2
- 3Blue1Brown, "Bayes theorem" (YouTube) — starts from conditional probability
