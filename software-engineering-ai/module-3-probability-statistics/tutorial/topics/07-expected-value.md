# 07 — Expected Value

## TL;DR

The **expected value** E(X) is the long-run average of a random variable — what you'd get if you repeated the experiment infinitely many times and averaged the results. It's the single most important number summarizing a distribution.

## Why it matters

Loss functions in ML are expected values. When you minimize "average loss over the training set," you're approximating E[L(model, data)]. The bias-variance decomposition, risk minimization, and decision theory all rest on expected value.

## Core concept

### Definition (discrete case)

For a discrete random variable X with possible values x₁, x₂, ... and PMF P(X = xᵢ):

```
E(X) = Σᵢ xᵢ × P(X = xᵢ)
```

**Intuition:** it's a weighted average of outcomes, where the weights are probabilities.

### Example: fair die

```
E(X) = 1×(1/6) + 2×(1/6) + 3×(1/6) + 4×(1/6) + 5×(1/6) + 6×(1/6) = 3.5
```

You'll never roll a 3.5, but on average that's what you get.

### Properties of expected value

| Property | Formula | Why it matters |
|---|---|---|
| Linearity | E(aX + b) = aE(X) + b | Scaling and shifting are easy |
| Additivity | E(X + Y) = E(X) + E(Y) | Always true, even if X,Y are dependent! |
| Constant | E(c) = c | A certain outcome has that value as its expectation |

**Linearity is the superpower.** E(X + Y) = E(X) + E(Y) requires NO assumptions about independence. This makes many hard problems easy.

### Expected value of common distributions

| Distribution | E(X) |
|---|---|
| Bernoulli(p) | p |
| Binomial(n, p) | np |
| Uniform({1,...,n}) | (n+1)/2 |

### Connection to variance

Variance is defined using expected value:

```
Var(X) = E[(X - E(X))²] = E(X²) - [E(X)]²
```

The second form (computational formula) is usually easier to calculate.

## Math

**Worked example:** You bet $1 on a game. With probability 0.4 you win $2 (net +$2). With probability 0.6 you lose your $1 (net -$1).

```
E(net gain) = 2×0.4 + (-1)×0.6 = 0.8 - 0.6 = 0.2
```

Positive expected value → on average you profit $0.20 per game. Play this game!

**Another:** E(X²) for fair die:

```
E(X²) = 1²×(1/6) + 2²×(1/6) + ... + 6²×(1/6) = 91/6 ≈ 15.17
Var(X) = E(X²) - [E(X)]² = 91/6 - (7/2)² = 91/6 - 49/4 = 35/12 ≈ 2.92
```

## Code example

```python
import numpy as np

# Expected value by simulation (Law of Large Numbers)
np.random.seed(42)
die_rolls = np.random.randint(1, 7, size=100_000)
print(f"Simulated E(X) for fair die: {die_rolls.mean():.4f}")  # ≈ 3.5

# Expected value by formula
outcomes = np.array([1, 2, 3, 4, 5, 6])
probs = np.array([1/6] * 6)
expected_value = np.sum(outcomes * probs)
print(f"Exact E(X): {expected_value:.4f}")  # 3.5

# The betting game
outcomes_game = np.array([2, -1])
probs_game = np.array([0.4, 0.6])
ev_game = np.sum(outcomes_game * probs_game)
print(f"E(net gain) = ${ev_game:.2f}")  # $0.20

# Variance via E(X²) - [E(X)]²
e_x_squared = np.sum(outcomes**2 * probs)
variance = e_x_squared - expected_value**2
print(f"Var(X) for fair die: {variance:.4f}")  # 2.9167
```

## Common pitfalls

- **"E(X) is the most likely outcome"** — false. For a fair die, E(X) = 3.5, which is impossible. E(X) is a center of mass, not a mode.
- **E(f(X)) ≠ f(E(X))** — Jensen's inequality. E(X²) ≠ [E(X)]². This trips people up when computing variance. The only exception is linear functions.
- **"Expected value = what I expect to happen"** — it's a long-run average. In any single trial, you might be far from E(X). The Law of Large Numbers says the sample mean converges to E(X) as trials → ∞.

## Further reading

- Blitzstein & Hwang, Chapter 4
- Khan Academy, "Expected value"
- The concept of "risk" in statistical decision theory = expected loss
