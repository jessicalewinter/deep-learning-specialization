# Quiz 02 — Random Experiments and Probability

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
State the three axioms of probability in your own words.

<details><summary>Answer</summary>
1. Probabilities are never negative (P(A) ≥ 0 for any event).
2. The probability of the entire sample space is 1 (something must happen).
3. For mutually exclusive events, the probability of their union equals the sum of their individual probabilities.

These three rules — plus the definition of sample space and events — are enough to derive every other probability rule.
</details>

## Q2
P(A) = 0.4, P(B) = 0.5, P(A ∩ B) = 0.2. Calculate P(A|B).

<details><summary>Answer</summary>
P(A|B) = P(A ∩ B) / P(B) = 0.2 / 0.5 = 0.4. Interesting: P(A|B) = P(A) = 0.4, which means knowing B happened doesn't change the probability of A. This means A and B are independent in this case.
</details>

## Q3
A medical test has: P(positive | disease) = 0.95 and P(positive | no disease) = 0.05. The disease prevalence is 1%. You test positive. What's the probability you actually have the disease?

<details><summary>Answer</summary>
Using Bayes' theorem (or just careful conditional probability):
P(disease | positive) = P(positive | disease) × P(disease) / P(positive)

P(positive) = P(pos|disease)×P(disease) + P(pos|no disease)×P(no disease)
            = 0.95 × 0.01 + 0.05 × 0.99 = 0.0095 + 0.0495 = 0.059

P(disease | positive) = 0.0095 / 0.059 ≈ 0.161 (about 16%)

Despite the test being 95% accurate, there's only a 16% chance you have the disease. This is because the disease is rare (1%), so most positives are false positives. This is the base-rate fallacy.
</details>

## Q4
You draw two cards from a standard deck without replacement. What's P(both are aces)?

<details><summary>Answer</summary>
P(both aces) = P(1st ace) × P(2nd ace | 1st ace) = (4/52) × (3/51) = 12/2652 = 1/221 ≈ 0.0045.

The multiplication rule: P(A∩B) = P(A) × P(B|A). After removing one ace, there are only 3 left among 51 cards.
</details>

## Q5
True or false: P(A|B) = P(B|A) when P(A) = P(B).

<details><summary>Answer</summary>
True. P(A|B) = P(A∩B)/P(B) and P(B|A) = P(A∩B)/P(A). If P(A) = P(B), the denominators are equal, so both expressions equal P(A∩B)/P(A). In general P(A|B) ≠ P(B|A) — confusing them is the prosecutor's fallacy.
</details>

## Q6
A box has 4 red and 6 blue balls. You draw one ball, note its color but DON'T replace it, then draw another. What's P(2nd ball is red)?

<details><summary>Answer</summary>
Use the law of total probability:
P(2nd red) = P(2nd red | 1st red)×P(1st red) + P(2nd red | 1st blue)×P(1st blue)
            = (3/9)×(4/10) + (4/9)×(6/10)
            = 12/90 + 24/90 = 36/90 = 4/10 = 0.4

Interesting: P(2nd red) = P(1st red) = 4/10. The marginal probability is the same regardless of position — even without replacement!
</details>

## Q7
Explain the difference between P(rain | cloudy) and P(cloudy | rain) using a real-world example.

<details><summary>Answer</summary>
P(rain | cloudy) = probability it rains given that it's cloudy. This could be moderate (maybe 30% — many cloudy days don't have rain).

P(cloudy | rain) = probability it's cloudy given that it's raining. This is nearly 100% — it's almost always cloudy when it rains.

These are very different numbers! Confusing them is like saying "most criminals have tattoos" (P(tattoo|criminal)) is the same as "most people with tattoos are criminals" (P(criminal|tattoo)). The base rates (how common each group is) make these very different.
</details>
