# Quiz 02 — Learning Paradigms

## Q1
Classify each task as supervised, unsupervised, or reinforcement learning:

a) Predicting house prices from features
b) Grouping customers into segments based on purchase history
c) Teaching a robot to walk by giving it +1 each step it stays upright
d) Predicting tomorrow's stock price from historical data
e) Generating new images of faces

<details><summary>Answer</summary>
a) Supervised (regression — labels are prices) · b) Unsupervised (clustering — no labels) · c) Reinforcement (rewards from actions in environment) · d) Supervised (regression with temporal data — be careful with the split) · e) Unsupervised in spirit (generative modeling); modern implementations often use self-supervised techniques.
</details>

## Q2
What's the key difference between supervised classification and supervised regression?

<details><summary>Answer</summary>
The output type. Classification predicts a discrete label (cat/dog/bird, spam/not-spam). Regression predicts a continuous value (price, temperature). They use different loss functions (cross-entropy vs MSE) and different evaluation metrics (accuracy/F1 vs MSE/MAE).
</details>

## Q3
Why is unsupervised learning generally considered "harder" than supervised learning?

<details><summary>Answer</summary>
Because there's no ground truth label to compare against, so "success" is ambiguous. You can compute supervised accuracy mechanically. With clustering, who decides if your clusters are "right"? You need external validation, domain expertise, or downstream tasks to judge. Two reasonable algorithms can give very different — and both "valid" — answers.
</details>

## Q4
Self-supervised learning is described as "supervised learning where labels come for free." Give an example of how that works.

<details><summary>Answer</summary>
Language modeling: take any text, hide the next word, train the model to predict it. The "label" is just the next word in the corpus — no human labeling required. Same for masked language modeling (BERT) where you mask a word in the middle, or next-sentence prediction. In vision: predict a missing patch, predict the rotation of an image, predict whether two crops come from the same image. The labels are generated mechanically from the data structure itself.
</details>

## Q5
You're building a recommendation system. What paradigm could each of these approaches use?

a) Predicting whether a user will click on an item from past click logs
b) Grouping users by similar viewing habits
c) Optimizing recommendations to maximize long-term user retention based on observed engagement

<details><summary>Answer</summary>
a) Supervised (clicks are labels) · b) Unsupervised (clustering by behavior) · c) Reinforcement learning — long-term retention is a reward signal, the system's recommendations change which data it gets to see (the action affects the environment).
</details>

## Q6
Why do practitioners often warn newcomers away from RL even when it "fits" the problem?

<details><summary>Answer</summary>
Because RL is famously brittle: rewards can be sparse or delayed, the agent's actions change the data distribution (non-stationary problem), exploration vs exploitation is hard to balance, and reward misspecification can produce bizarre policies (the agent finds shortcuts that hit the reward without solving the actual task — "reward hacking"). If your problem can be reformulated as supervised, the engineering pain is dramatically lower.
</details>
