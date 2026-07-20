# 04 — Bias–Variance Tradeoff

## TL;DR

A model's error on new data comes from three sources: **bias** (wrong assumptions about the problem), **variance** (over-sensitivity to the specific training data), and **irreducible noise** (no model can fix this). Reducing one usually increases the other — that's the tradeoff.

## Why it matters

Almost every "is my model good?" question reduces to a bias–variance diagnosis:

- Training error high, validation error high → **bias problem** (model too simple / underfitting)
- Training error low, validation error high → **variance problem** (model too complex / overfitting)
- Both low → 🎉
- Both high but close → bias problem
- Both high and far apart → both problems

Knowing which one you have tells you what to try next. Most beginner mistakes come from applying a variance fix (more data, regularization) to a bias problem, or vice versa.

## Intuition

Imagine fitting curves to a noisy parabola.

- **High bias (underfit):** you fit a straight line. Wrong shape, no matter the data. Predictions are systematically off.
- **High variance (overfit):** you fit a degree-15 polynomial that wiggles through every point — including the noise. Different training samples produce wildly different curves.
- **Sweet spot:** a parabola. Captures the real pattern, ignores the noise.

```
Underfit (bias)    Just right       Overfit (variance)
   ___                ___                  ___
  /                 /  \              /\/\/  \/\
 /                 /    \            /         \/\
                                                 \
```

## The decomposition (math sketch)

For a model `f̂(x)` trained on a random dataset, the expected squared error on a new point `x` decomposes as:

```
E[(y - f̂(x))²]  =  Bias[f̂(x)]²  +  Var[f̂(x)]  +  σ²
                   ↑                ↑              ↑
              wrong on average    unstable      noise floor
```

- **Bias:** how far the *average* prediction (over many training sets) is from the truth
- **Variance:** how much the prediction *jumps around* between different training sets
- **σ²:** noise inherent in the data — irreducible

You can't make σ² smaller. You can trade bias against variance by changing model complexity.

## What knobs control which?

| Action | Effect on bias | Effect on variance |
|---|---|---|
| Use a more complex model (deeper net, higher-degree polynomial) | ↓ | ↑ |
| Use a simpler model | ↑ | ↓ |
| Add more training data | — | ↓ |
| Add regularization (L2, dropout, weight decay) | ↑ | ↓ |
| Add more / better features | ↓ | sometimes ↑ |
| Train longer | ↓ | ↑ (eventually) |

This is your decision tree:
- **High bias?** → bigger model, train longer, better features
- **High variance?** → more data, regularize, simpler model, ensembling

## Worked diagnosis

You train a classifier. Results:
- Training accuracy: 99%
- Validation accuracy: 71%

That gap of 28 points is screaming **variance problem**. Don't reach for a bigger model. Try:
1. More training data (even augmented data)
2. Stronger regularization (increase dropout, weight decay)
3. A simpler model (smaller hidden layers, fewer features)

Compare with:
- Training accuracy: 73%
- Validation accuracy: 71%

Both bad, gap is small → **bias problem**. The model can't even fit the training data. Try:
1. A more expressive model
2. Train longer (maybe you stopped too early)
3. Better features / less aggressive regularization

## The modern wrinkle: double descent

The classic story says complexity goes up → variance goes up → test error eventually grows. With *very* large neural networks, recent research shows test error can actually drop again past the interpolation threshold. The tradeoff is real but the curve isn't always U-shaped at extreme scales. Worth knowing exists; safe to ignore for everything outside the "billion-parameter" regime.

## Common pitfalls

- **Treating validation gap as inevitable** — a 5-point gap might be fine; a 30-point gap is a signal you should act on
- **Adding regularization to a bias-limited model** — makes everything worse
- **Adding more data when you have a bias problem** — won't help; the model can't learn the shape
- **Confusing irreducible noise with bias** — if humans can only score 90%, don't expect 99%

## Further reading

- Geman, Bienenstock, Doursat, *Neural Networks and the Bias/Variance Dilemma* (1992) — original treatment
- Ng, *Machine Learning Yearning*, Ch. 20–27 — practical bias/variance debugging
- Belkin et al., *Reconciling modern ML practice and the classical bias-variance tradeoff* (2019) — double descent
