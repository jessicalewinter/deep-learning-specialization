# Quiz 03 — Train / Validation / Test Split

## Q1
What's the role of each split?

<details><summary>Answer</summary>
Train: fits the model parameters. Validation: used to make decisions *about* the model — picking hyperparameters, comparing architectures, deciding when to stop training. Test: held out for one final, unbiased estimate of generalization. The model parameters are touched only by training; validation and test are never used to update parameters directly.
</details>

## Q2
You've trained 20 models with different hyperparameters and reported the test accuracy of the best one. Why is this number probably optimistic?

<details><summary>Answer</summary>
Because you used the test set to *select* a model, you've effectively turned it into a validation set. With enough trials, one of them will look better on test by chance. The reported number reflects both real performance and luck — and you have no remaining held-out set to measure how much was luck. The fix: pick the best model on validation, then evaluate that one model on test, exactly once.
</details>

## Q3
You're predicting next month's sales from historical data. Why is a random 80/20 split a bad idea?

<details><summary>Answer</summary>
Because random splitting lets training data come from *after* test data in time. The model gets to "see the future" in training, which inflates metrics absurdly (it might learn that a competitor went bankrupt next year). For temporal data, always split chronologically: train on past, validate on near-future, test on far-future.
</details>

## Q4
You scale your features using `StandardScaler.fit_transform(X)` on the entire dataset, then split into train/test. What's wrong?

<details><summary>Answer</summary>
You've leaked test set statistics into training. The mean and standard deviation used to scale come from the *entire* dataset including test, so the model has implicit information about the test distribution. The fix: split first, fit the scaler on train only, then transform train, val, and test using that fitted scaler. Same applies to imputation, target encoding, feature selection, and basically any preprocessing step.
</details>

## Q5
You have 500 examples in a binary classification problem with 95% / 5% class imbalance. What split strategy makes sense?

<details><summary>Answer</summary>
Stratified k-fold cross-validation. With only 500 examples and 5% positives (~25 positive examples total), a single train/val/test split risks getting 0–2 positives in test by chance, which makes metrics meaningless. Stratification preserves class proportions in each fold; cross-validation reuses data so you're not throwing away precious examples. You'd still hold out a small final test set if you can, but the bulk of evaluation happens via CV.
</details>

## Q6
A coworker says: "I don't bother with a test set — I just look at validation accuracy." What's the actual harm?

<details><summary>Answer</summary>
The validation set gets used for many decisions over a project's lifetime: hyperparameter sweeps, architecture choices, early stopping, whether to deploy. Each decision is a tiny "fit" to the validation set. After enough decisions, validation accuracy overestimates true generalization — same way a test set overestimates if you peek at it. Without a separate, untouched test set, you have no clean measurement of what will happen in production. You'll find out the hard way.
</details>
