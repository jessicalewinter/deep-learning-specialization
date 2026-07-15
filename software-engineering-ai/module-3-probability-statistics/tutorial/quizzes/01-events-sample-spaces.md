# Quiz 01 — Events and Sample Spaces

> The skill should ask these one at a time, in order. Don't show all answers up front.

## Q1
You flip two coins. Write out the complete sample space Ω.

<details><summary>Answer</summary>
Ω = {HH, HT, TH, TT}. There are 4 sample points. Note that HT and TH are distinct outcomes (order matters: first coin vs second coin).
</details>

## Q2
Using the two-coin sample space: Let A = "at least one head" and B = "both coins show the same face." Are A and B mutually exclusive? Why or why not?

<details><summary>Answer</summary>
No. A = {HH, HT, TH} and B = {HH, TT}. Their intersection A ∩ B = {HH} ≠ ∅. Mutually exclusive means they can never happen together, but "at least one head" AND "both same" can both be true when both coins are heads.
</details>

## Q3
If P(A) = 0.6 and P(B) = 0.3, and A and B are mutually exclusive, what is P(A ∪ B)?

<details><summary>Answer</summary>
P(A ∪ B) = P(A) + P(B) = 0.6 + 0.3 = 0.9. Since they're mutually exclusive, there's no overlap to subtract.
</details>

## Q4
If P(A) = 0.6 and P(B) = 0.3, and P(A ∩ B) = 0.1, what is P(A ∪ B)?

<details><summary>Answer</summary>
P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 0.6 + 0.3 - 0.1 = 0.8. The inclusion-exclusion formula subtracts the overlap to avoid double-counting the outcomes in both A and B.
</details>

## Q5
True or false: if two events are mutually exclusive and both have probability > 0, they must be dependent.

<details><summary>Answer</summary>
True. If A and B are mutually exclusive, P(A ∩ B) = 0. For independence, we'd need P(A ∩ B) = P(A) × P(B) > 0 (since both have nonzero probability). Since 0 ≠ P(A)×P(B), they cannot be independent. Knowing A happened means B definitely didn't — that's dependence.
</details>

## Q6
A bag has 5 red, 3 blue, and 2 green marbles. What is P(not green)?

<details><summary>Answer</summary>
P(not green) = 1 - P(green) = 1 - 2/10 = 8/10 = 0.8. Using the complement is often easier than counting all the non-green outcomes directly (though here both work: (5+3)/10 = 8/10).
</details>

## Q7
You roll a fair die. Let A = "result is even" and B = "result > 3." Calculate P(A ∩ B) and determine whether A and B are independent.

<details><summary>Answer</summary>
A = {2,4,6}, B = {4,5,6}, A∩B = {4,6}. P(A∩B) = 2/6 = 1/3. For independence: P(A) × P(B) = (3/6) × (3/6) = 1/4. Since 1/3 ≠ 1/4, A and B are NOT independent. Knowing the result is >3 makes "even" more likely (2 out of 3 vs 3 out of 6).
</details>

## Q8
What's wrong with defining the sample space for "tomorrow's weather" as Ω = {good, bad}?

<details><summary>Answer</summary>
It's subjective and imprecise — "good" and "bad" aren't well-defined outcomes. A proper sample space needs unambiguous, mutually exclusive, collectively exhaustive outcomes. Better: Ω = {sunny, partly cloudy, overcast, light rain, heavy rain, snow} or use measurable quantities like temperature ranges. The outcomes must be precise enough that any observer would agree which one occurred.
</details>
