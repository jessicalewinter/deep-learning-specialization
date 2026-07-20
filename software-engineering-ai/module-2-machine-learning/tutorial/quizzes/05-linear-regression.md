# Quiz 05 — Linear Regression

## Q1
What does linear regression's loss function (MSE) actually compute, in plain English?

<details><summary>Answer</summary>
The average squared distance between predicted values and true values. "Squared" matters: it makes large errors disproportionately costly, makes the loss differentiable everywhere, and gives a closed-form solution. The downside is sensitivity to outliers — one extreme point can dominate the loss because its error is squared.
</details>

## Q2
Linear regression has a closed-form solution: `w = (XᵀX)⁻¹ Xᵀy`. Why don't we always use it instead of gradient descent?

<details><summary>Answer</summary>
Three reasons: 1) Computing the matrix inverse is O(n³) in the number of features — fine for hundreds, brutal for hundreds of thousands. 2) `XᵀX` can be ill-conditioned (singular or near-singular when features are correlated), making the inverse numerically unstable. 3) The closed form is unique to linear regression with MSE — almost no other ML model has one. Learning gradient descent on linear regression sets you up for everything else where it's the *only* option.
</details>

## Q3
Why is feature scaling important for linear regression with gradient descent, but irrelevant for the closed-form solution?

<details><summary>Answer</summary>
The closed form algebraically finds the optimal weights regardless of feature scale — it's invariant to scaling. Gradient descent isn't: when features have wildly different scales (say, 0–1 and 0–1,000,000), the loss surface becomes highly elongated. The gradient points mostly along the large-scale direction, so the optimizer takes tiny steps in the small-scale direction. Result: convergence is glacially slow, or you need a learning rate so small it's useless. Standardizing features makes the loss surface roughly spherical and gradient descent converges fast.
</details>

## Q4
You fit a linear regression and get an R² of 0.95 on training data. Can you conclude the model is good?

<details><summary>Answer</summary>
No. R² on training data tells you nothing about generalization — a sufficiently complex model fits training data perfectly and generalizes terribly. Always evaluate on held-out validation/test data. Also: even on test, R² can be misleading. It can be high while predictions are systematically biased in some range. Always plot residuals (predicted vs actual, or residual vs predicted) to check for patterns.
</details>

## Q5
What's the difference between Ridge (L2) and Lasso (L1) regularization, and when would you pick one over the other?

<details><summary>Answer</summary>
Ridge adds `λ·Σwⱼ²` to the loss; Lasso adds `λ·Σ|wⱼ|`. Ridge shrinks all weights smoothly toward zero but rarely makes them exactly zero. Lasso can drive weights to *exactly* zero, doing automatic feature selection. Pick Lasso when you suspect many features are irrelevant and want sparsity. Pick Ridge when you think most features matter a little and want stability against multicollinearity. Elastic Net combines both — useful when groups of correlated features should be selected together.
</details>

## Q6
You fit a linear model to predict house prices from `square_footage`. The R² is 0.4 and residuals show a clear curved pattern when plotted against `square_footage`. What does this suggest, and what would you try?

<details><summary>Answer</summary>
The linear assumption is violated — the true relationship is non-linear. Curved residuals are the signature: a correctly-specified linear model has residuals scattered randomly around zero. Options: 1) Add polynomial features (`square_footage²`) — turns it into polynomial regression, still linear in parameters · 2) Try `log(square_footage)` if the relationship looks logarithmic · 3) Switch to a non-linear model (tree, neural net) · 4) Add other features (location, age, condition) that the linear-in-square-footage assumption was implicitly conflating with size. Almost always, real housing prices need many features and interactions, not just one.
</details>
