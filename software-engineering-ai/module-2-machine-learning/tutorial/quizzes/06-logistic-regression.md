# Quiz 06 — Logistic Regression & Cross-Entropy

## Q1
Logistic regression is sometimes called "linear" — but it predicts probabilities, not lines. What's "linear" about it?

<details><summary>Answer</summary>
The *score* `z = w·x + b` is a linear function of the inputs and weights — that's what makes the model "linear." The sigmoid is a fixed, non-learned squashing function that just maps that score into (0, 1). Crucially, the **decision boundary** (the set of points where the model outputs 0.5) is `w·x + b = 0`, which is a hyperplane — geometrically straight. So the model is "linear" in both the parameter sense and the decision-boundary sense, even though the output curve is sigmoid-shaped.
</details>

## Q2
Why don't we use mean squared error as the loss for logistic regression?

<details><summary>Answer</summary>
Two main reasons: 1) MSE on top of sigmoid is **non-convex** in the parameters and has flat regions where gradients vanish — gradient descent can get stuck or progress glacially. Cross-entropy is convex and has well-behaved gradients everywhere. 2) MSE doesn't punish overconfidence the right way — predicting 0.99 vs 0.9 when the true label is 1 looks "almost the same" to MSE, but cross-entropy says 0.99 is dramatically better. For probabilistic classification, that's the correct behavior. Bonus: cross-entropy is the negative log-likelihood under a Bernoulli model — it's principled, not just a hack.
</details>

## Q3
Cross-entropy for binary classification is `-[y·log(ŷ) + (1-y)·log(1-ŷ)]`. Why does it go to infinity when the model is confidently wrong?

<details><summary>Answer</summary>
If true label is `y=1` and model predicts `ŷ → 0`, then `-y·log(ŷ) = -log(0+) → +∞`. The log function blows up at zero. This is exactly what we want: a confident, wrong prediction should be penalized arbitrarily heavily. Compare with MSE, where the maximum penalty is bounded by 1 — a confidently wrong probability prediction is treated as merely "off by 1." Cross-entropy's unboundedness is a feature, not a bug.
</details>

## Q4
The gradient of cross-entropy with respect to weights for logistic regression turns out to be `(ŷ - y) · x`. Why is that surprising / elegant?

<details><summary>Answer</summary>
It's the *exact same form* as the gradient for linear regression with MSE — `(prediction - target) · input`. Despite a totally different loss and a non-linear sigmoid in the way, the chain rule has the sigmoid's derivative cancel cleanly with the log's derivative, leaving a simple "error times input" expression. This isn't coincidence: cross-entropy + sigmoid (and softmax + categorical cross-entropy) is a *principled pairing* — both come from the same maximum likelihood framework, and the math reflects that. It's also why you should never split sigmoid and cross-entropy into separate steps in code (PyTorch's `BCEWithLogitsLoss` combines them for numerical stability).
</details>

## Q5
You train a logistic regression on a dataset where 95% of examples are class 0. The model achieves 95% accuracy. Should you celebrate?

<details><summary>Answer</summary>
No — predicting "always class 0" gets 95% accuracy without learning anything. With imbalanced data, accuracy is a misleading metric. Look at: precision (of those I called positive, how many were?), recall (of all true positives, how many did I find?), F1 (harmonic mean), AUC-ROC (threshold-independent). For an imbalanced fraud detection problem, recall on the positive class is usually the metric that matters. Also try: setting `class_weight='balanced'` in sklearn, oversampling the minority class, or using SMOTE.
</details>

## Q6
What's the relationship between binary logistic regression and softmax regression (multi-class)?

<details><summary>Answer</summary>
Softmax regression is the multi-class generalization. Where binary logistic uses sigmoid to squash one score into (0, 1), softmax takes K scores and squashes them into a probability distribution over K classes that sums to 1. Loss generalizes from binary cross-entropy to categorical cross-entropy: `-Σₖ yₖ·log(ŷₖ)` where `y` is one-hot. Mathematically, binary logistic regression is the special case `K=2` of softmax (with one redundant degree of freedom — that's why binary uses one weight vector and softmax uses K). The output layer of every classification neural network is exactly this — a linear transformation followed by softmax (or sigmoid for binary).
</details>
