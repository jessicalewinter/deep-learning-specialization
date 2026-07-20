# 05 — Probability Spaces (Formal)

## TL;DR

A **probability space** is the mathematical triple (Ω, F, P) that makes probability rigorous: the sample space, the collection of events you're allowed to ask about, and the probability measure that assigns numbers to those events.

## Why it matters

Topics 01–02 gave you the intuition. This topic gives you the formal framework that makes everything *consistent*. You need this when working with continuous distributions (where "probability of a single exact value" = 0), or when someone asks "but what *is* a probability, technically?"

## Core concept

### The triple (Ω, F, P)

| Component | What it is | Example (fair die) |
|---|---|---|
| **Ω** (sample space) | All possible outcomes | {1, 2, 3, 4, 5, 6} |
| **F** (σ-algebra) | Collection of "askable" events | All subsets of Ω (64 subsets) |
| **P** (probability measure) | Function: F → [0,1] | P({k}) = 1/6 for each k |

### σ-algebra (sigma-algebra)

A σ-algebra F is a collection of subsets of Ω that is:
1. **Contains Ω**: Ω ∈ F (you can always ask "did *something* happen?")
2. **Closed under complement**: if A ∈ F, then Aᶜ ∈ F (if you can ask about A, you can ask about "not A")
3. **Closed under countable union**: if A₁, A₂, ... ∈ F, then A₁ ∪ A₂ ∪ ... ∈ F

**Intuition:** the σ-algebra defines what questions you're *allowed to ask*. For finite sample spaces, it's usually "all subsets" and you don't think about it. For continuous spaces (like all real numbers), you need to be more careful — not every subset is "measurable."

### Probability measure P

A function P: F → [0,1] satisfying:
1. P(Ω) = 1
2. P(A) ≥ 0 for all A ∈ F
3. **Countable additivity** (σ-additivity): for disjoint events A₁, A₂, ...:
   P(A₁ ∪ A₂ ∪ ...) = P(A₁) + P(A₂) + ...

This is a stronger version of the additivity axiom from Topic 02 — it works for infinitely many disjoint events, not just two.

## Math

For a **discrete uniform** probability space on a finite Ω:

```
P(A) = |A| / |Ω|
```

For a **non-uniform** discrete space, assign weights p₁, p₂, ..., pₙ where Σpᵢ = 1:

```
P(A) = Σᵢ∈A pᵢ
```

### Probability mass function (PMF)

For discrete spaces, the PMF f(x) = P({x}) gives the probability of each individual outcome. It fully determines P:

```
P(A) = Σ_{x∈A} f(x)
```

## Code example

```python
# A non-uniform discrete probability space
# Loaded die: 6 appears twice as often
outcomes = [1, 2, 3, 4, 5, 6]
weights = [1, 1, 1, 1, 1, 2]  # raw weights
total = sum(weights)
pmf = {x: w/total for x, w in zip(outcomes, weights)}

print("PMF of loaded die:")
for outcome, prob in pmf.items():
    print(f"  P({outcome}) = {prob:.4f}")

# P(even) = P(2) + P(4) + P(6)
event_even = {2, 4, 6}
p_even = sum(pmf[x] for x in event_even)
print(f"\nP(even) = {p_even:.4f}")  # 4/7 ≈ 0.5714

# Verify axioms
print(f"\nSum of all P = {sum(pmf.values()):.4f}")  # must be 1.0
print(f"All P >= 0: {all(p >= 0 for p in pmf.values())}")
```

## Common pitfalls

- **Thinking σ-algebras are overkill** — for finite spaces, yes. But the moment you work with continuous random variables (heights, temperatures, neural network outputs), you need this machinery to avoid paradoxes.
- **Confusing PMF with PDF** — PMF is for discrete variables (gives actual probabilities). PDF is for continuous variables (gives density — you integrate to get probability). We'll cover PDF later.
- **"Probability of a single point is 0 in continuous spaces"** — this is correct and confusing at first. If you pick a random real number between 0 and 1, P(exactly 0.5) = 0, but P(between 0.4 and 0.6) = 0.2. Intervals have probability; points don't.

## Further reading

- Ross, *A First Course in Probability*, Chapter 2
- Blitzstein & Hwang, Chapter 1 (the axioms)
- Wikipedia, "Probability space" — surprisingly good for the formal definition
