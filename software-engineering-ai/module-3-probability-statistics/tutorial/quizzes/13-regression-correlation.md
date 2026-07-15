# Quiz 13 — Regression and Correlation

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
You fit a linear regression and get Ŷ = 10 + 3X. Interpret the slope and intercept in plain language.

<details><summary>Answer</summary>
Intercept (10): when X = 0, the predicted Y is 10. It's the starting point / baseline value.
Slope (3): for every 1-unit increase in X, Y increases by 3 units on average.

Example context: if X = years of experience and Y = salary (in thousands):
- A person with 0 years experience earns ~$10k (intercept — may or may not be meaningful depending on whether X=0 is in your data range)
- Each additional year of experience is associated with ~$3k more salary (slope)

"Associated with" — not "causes." The slope is a correlation-based prediction, not a causal claim.
</details>

## Q2
Your regression has SST = 1000, SSE = 250. What is R²? What does it mean?

<details><summary>Answer</summary>
R² = 1 - SSE/SST = 1 - 250/1000 = 0.75

Or equivalently: SSR = SST - SSE = 750, so R² = SSR/SST = 750/1000 = 0.75.

Interpretation: 75% of the variability in Y is "explained" by the linear relationship with X. The remaining 25% is unexplained (residual variation). This is a reasonably good fit — X is a strong predictor of Y but doesn't tell the whole story.
</details>

## Q3
You compute r = 0.5 between study hours and exam scores. What is R² and what does the difference between r and R² tell you?

<details><summary>Answer</summary>
R² = r² = 0.5² = 0.25

r = 0.5 sounds decent — "moderate positive correlation." But R² = 0.25 reveals that study hours explain only 25% of the variance in exam scores. 75% is due to other factors (innate ability, sleep, test anxiety, etc.).

The lesson: r overstates the "explanatory power." r = 0.5 is halfway between 0 and 1, suggesting a middling relationship. But R² = 0.25 shows X explains only a quarter of Y's behavior. Always think in terms of R² for practical interpretation.
</details>

## Q4
Your residual plot shows a clear U-shape (residuals are negative in the middle and positive at the extremes). What does this tell you?

<details><summary>Answer</summary>
The relationship between X and Y is NOT linear — it's curved (probably quadratic or exponential). The linear model systematically underpredicts in the middle range and overpredicts at the extremes.

What to do:
1. Try a polynomial regression (add X² term)
2. Try a log transformation of X or Y
3. Use a non-linear model

A good residual plot should show random scatter around zero with no pattern. Any visible pattern = model misspecification. The linear model's R² might still be decent, but you're leaving predictive power on the table.
</details>

## Q5
Dataset: X = [1, 2, 3, 4, 5], Y = [2, 4, 6, 8, 100]. The last point is clearly an outlier. How will it affect the regression line?

<details><summary>Answer</summary>
The outlier will dramatically pull the regression line upward, especially at the right end. The slope will be inflated (steeper than the true relationship for the majority of data), and R² will be misleading.

Why: least squares minimizes the SUM of squared residuals. The outlier's residual is huge, so the line bends to reduce it — at the cost of fitting the other 4 points poorly. One point gets disproportionate influence.

Solutions:
- Remove the outlier (if it's a data error)
- Use robust regression (e.g., RANSAC, Huber loss) that downweights outliers
- Report results with and without the outlier to show its impact

This is why EDA (plotting your data!) before modeling is essential.
</details>

## Q6
Can R² ever decrease when you add more predictor variables to a multiple regression?

<details><summary>Answer</summary>
No — R² can never decrease when you add variables. Even a completely random/useless variable will increase R² slightly (or keep it the same) because the model has more flexibility to fit the training data.

This is why R² alone is misleading for model selection. Use instead:
- Adjusted R² = 1 - (1-R²)(n-1)/(n-k-1), which penalizes extra variables
- AIC/BIC (information criteria)
- Cross-validation R² (can definitely decrease with useless variables)

A model with 100 random features and R²=0.95 on training data might have R²=0.02 on test data. This is overfitting, and regular R² hides it completely.
</details>

## Q7
You fit a regression predicting house price from square footage using houses from 800-3000 sq ft. A client asks you to predict the price of a 10,000 sq ft mansion. What's the problem?

<details><summary>Answer</summary>
EXTRAPOLATION. The model was trained on 800-3000 sq ft. Predicting at 10,000 sq ft assumes the linear relationship continues far beyond the observed range — which is almost certainly wrong.

Problems:
- The price-per-sqft likely changes at high values (diminishing returns, different market segment entirely)
- The model has NO data in that range to learn from
- The confidence interval at X=10000 would be enormous (uncertainty grows with distance from x̄)
- Luxury mansions are priced by features (view, architect, land) that a simple sqft model doesn't capture

Rule: only predict within (or very close to) the range of your training data. Extrapolation is speculation dressed up as statistics.
</details>

## Q8
scipy's `linregress` returns a p-value for the slope. What hypothesis is this testing? If p < 0.05, what can you conclude?

<details><summary>Answer</summary>
It tests H₀: β₁ = 0 (the true slope is zero — there is NO linear relationship between X and Y) vs H₁: β₁ ≠ 0.

If p < 0.05: reject H₀. There IS statistically significant evidence of a linear relationship between X and Y. The slope is significantly different from zero.

But this does NOT mean:
- The relationship is strong (could be r=0.1 with n=10000)
- The relationship is linear (could be curved with a nonzero linear component)
- X causes Y
- The model is useful for prediction (R² might still be low)

A significant slope means "something is there" — not "it's useful" or "it's the right model."
</details>
