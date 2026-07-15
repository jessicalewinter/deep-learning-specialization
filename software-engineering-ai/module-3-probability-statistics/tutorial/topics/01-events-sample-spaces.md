# 01 — Events and Sample Spaces

## TL;DR

A **sample space** is the set of all possible outcomes of an experiment. An **event** is any subset of those outcomes you care about. Everything in probability is built on these two ideas.

## Why it matters

Before you can compute any probability, you need to precisely define *what could happen* (sample space) and *what you're asking about* (event). Sloppy definitions here lead to paradoxes and wrong answers downstream — especially in ML when defining what "success" means for a classifier.

## Core concept

### Sample space (Ω)

The complete set of possible outcomes. Examples:

| Experiment | Sample space Ω |
|---|---|
| Flip a coin | {H, T} |
| Roll a die | {1, 2, 3, 4, 5, 6} |
| Pick a random pixel color | {(r,g,b) : 0 ≤ r,g,b ≤ 255} |

Each individual outcome is a **sample point**.

### Events

An event is any subset of Ω. If Ω = {1,2,3,4,5,6}:
- A = "roll an even number" = {2, 4, 6}
- B = "roll greater than 4" = {5, 6}

### Operations on events

| Operation | Notation | Meaning |
|---|---|---|
| Union | A ∪ B | A happens OR B happens (or both) |
| Intersection | A ∩ B | A AND B both happen |
| Complement | Aᶜ (or Ā) | A does NOT happen |

### Special relationships

- **Mutually exclusive**: A ∩ B = ∅ (they can't both happen). Rolling a 2 and rolling a 5 on a single die are mutually exclusive.
- **Independent**: knowing A happened doesn't change the probability of B. Flipping heads on coin 1 tells you nothing about coin 2.

## Math

For mutually exclusive events:
```
P(A ∪ B) = P(A) + P(B)
```

For any two events (inclusion-exclusion):
```
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
```

For the complement:
```
P(Aᶜ) = 1 - P(A)
```

## Code example

```python
# Simulating events with Python sets
sample_space = {1, 2, 3, 4, 5, 6}

A = {2, 4, 6}       # even numbers
B = {5, 6}          # greater than 4

union = A | B        # A ∪ B = {2, 4, 5, 6}
intersection = A & B # A ∩ B = {6}
complement_A = sample_space - A  # Aᶜ = {1, 3, 5}

print(f"P(A) = {len(A)}/{len(sample_space)} = {len(A)/len(sample_space):.2f}")
print(f"P(A ∪ B) = {len(union)}/{len(sample_space)} = {len(union)/len(sample_space):.2f}")
print(f"P(A ∩ B) = {len(intersection)}/{len(sample_space)} = {len(intersection)/len(sample_space):.2f}")
```

Output:
```
P(A) = 3/6 = 0.50
P(A ∪ B) = 4/6 = 0.67
P(A ∩ B) = 1/6 = 0.17
```

## Common pitfalls

- **Confusing mutually exclusive with independent** — they're opposite! If A and B are mutually exclusive and both have nonzero probability, they *cannot* be independent (knowing A happened means B definitely didn't).
- **Forgetting to subtract the intersection** — P(A ∪ B) ≠ P(A) + P(B) unless they're mutually exclusive. Double-counting the overlap is the #1 beginner mistake.
- **Vague sample spaces** — "the weather tomorrow" isn't a sample space. {sunny, cloudy, rainy, snowy} is. Precision matters.

## Further reading

- DeGroot & Schervish, *Probability and Statistics*, Chapter 1
- Khan Academy, "Basic probability" series
- 3Blue1Brown, "But what is probability?" (YouTube)
