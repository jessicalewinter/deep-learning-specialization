# 02 — Supervised vs. Unsupervised vs. Reinforcement Learning

## TL;DR

Three flavors, distinguished by **what the model gets to see**:

- **Supervised** — inputs *with* correct answers. Most of what people call "ML" today.
- **Unsupervised** — inputs *without* answers. The model finds structure on its own.
- **Reinforcement** — no labels at all, just a reward signal from acting in an environment.

## Why it matters

The paradigm dictates everything downstream — what data you collect, what algorithms apply, what "success" means. Mismatch the paradigm to the problem and nothing else you do will save you.

## Supervised learning

You have `(x, y)` pairs and want to learn `f(x) ≈ y`.

- **Classification** — `y` is a discrete label (spam / not-spam, cat / dog / bird)
- **Regression** — `y` is continuous (price, temperature, time-to-failure)

Examples:
- Image → "cat" (classification)
- House features → price (regression)
- Email → spam probability (classification, but with probabilistic output)

This is where ~80% of practical ML lives because labeled data exists for many problems and the success criterion is unambiguous: did `f(x_test)` match `y_test`?

## Unsupervised learning

You have only `x` — no labels. The model has to find structure.

- **Clustering** — group similar items (k-means, DBSCAN)
- **Dimensionality reduction** — compress high-dim data while preserving information (PCA, t-SNE, autoencoders)
- **Density estimation** — model `P(x)` (GMMs, normalizing flows)
- **Generative modeling** — sample new `x` similar to training data (VAEs, GANs, diffusion)

Trickier than supervised because "success" is fuzzy. There's no label to check against; you're measuring how well the structure the model found matches some intuition.

## Reinforcement learning

An *agent* takes *actions* in an *environment* and gets *rewards*. It learns a *policy* — a strategy for picking actions — that maximizes expected long-run reward.

- Game-playing (AlphaGo, Atari, chess)
- Robotics (locomotion, manipulation)
- Recommendation with feedback loops
- LLM alignment (RLHF — Reinforcement Learning from Human Feedback)

Hardest paradigm to get right: rewards can be sparse, delayed, or misspecified, and the agent itself changes the data distribution as it learns.

## The map

```
┌─────────────────────────────────────────────────┐
│                  What you have                  │
├──────────────┬──────────────┬───────────────────┤
│ (x, y) pairs │   only x     │ environment +      │
│              │              │ reward signal     │
├──────────────┼──────────────┼───────────────────┤
│  Supervised  │ Unsupervised │   Reinforcement   │
└──────────────┴──────────────┴───────────────────┘
```

## Beyond the textbook trio

Real systems often blend paradigms:

- **Self-supervised** — generate labels from the data itself (predict the next word, predict a masked patch). This is how modern LLMs and vision models pre-train.
- **Semi-supervised** — small labeled set + huge unlabeled set
- **Contrastive learning** — learn by deciding which pairs of inputs are "similar"

Self-supervised is arguably the dominant paradigm in 2026 — it's what makes models like GPT and CLIP possible. Technically it's a clever form of supervised learning where the labels come for free from the data.

## Common pitfalls

- **Forcing supervised when labels don't exist** — if labeling is impossibly expensive, look at self-supervised first
- **Treating unsupervised output as ground truth** — clusters are *hypotheses*, not facts
- **Overestimating RL** — RL is glamorous and brittle; if your problem can be supervised, do it supervised

## Further reading

- Russell & Norvig, *AI: A Modern Approach*, Ch. 18–22
- Sutton & Barto, *Reinforcement Learning: An Introduction* (free online)
