# Quiz 01 — What is Machine Learning?

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
What's the core difference between traditional programming and machine learning?

<details><summary>Answer</summary>
Traditional programming: you write the rules, the computer applies them to data to produce answers. ML: you provide data and answers, and the computer produces the rules (model). The "rule-finding" is what training does.
</details>

## Q2
Tom Mitchell defined learning as improving at a task **T** with respect to a measure **P** as experience **E** grows. For a spam classifier, identify each component.

<details><summary>Answer</summary>
T = classify emails as spam/not-spam · P = some metric like accuracy or F1 on held-out emails · E = labeled emails the model gets to see during training. The point of the framing is that without all three, you don't have a learning problem.
</details>

## Q3
True or false: a model that achieves 99% accuracy on its training data is necessarily a good model.

<details><summary>Answer</summary>
False. It might just be memorizing — overfitting. The only meaningful accuracy is on data the model has never seen. This is why we have train/val/test splits.
</details>

## Q4
What are the three irreducible ingredients of any ML system?

<details><summary>Answer</summary>
Data, a model (a function with tunable parameters), and a loss (a measure of how wrong the model is). Training adjusts model parameters to minimize loss on the data.
</details>

## Q5
Why is the statement "more data fixes everything" misleading?

<details><summary>Answer</summary>
Bad data scaled up is still bad. Mislabeled examples, biased samples, or systematic noise all hurt at any scale. More data helps when the issue is variance/sample-size — it doesn't help when the issue is data quality, biased sampling, or a model that's fundamentally mis-specified for the task.
</details>

## Q6
Why does Domingos (and most senior ML practitioners) push so hard on baselines?

<details><summary>Answer</summary>
Because complexity has costs (engineering, debugging, deployment, interpretability) and you only know if those costs are worth paying when you measure against a dumb baseline. Predicting the mean (regression) or the majority class (classification) often gets shockingly close — if your fancy model barely beats it, the fancy model is probably wrong, broken, or pointless.
</details>
