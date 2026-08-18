# Chapter 9 Cold-Transfer Task — Form B

Status: reader-delivery copy. Governed by `spec.md` (Transfer target) and `transfer.md`.

Without consulting the Chapter 9 chapter text, the water case, or the rubric, work the situation below.

**You are the analyst.** Produce a written assessment for the committee.

Every fact you need is supplied. Do not look anything up; if something you need is missing, say what it is and whether it would change your answer.

Current pilot target: **45 minutes**. This is a design parameter pending pilot evidence, not a universal standard.

## The decision

A bank is entering a new market and is deciding whether to deploy a **real-time fraud-screening rule** it uses at home: the rule holds a suspect transaction for ninety seconds and queries a shared interbank registry before releasing it.

The risk committee meets next month. Five sources have been assembled.

## The five sources

All estimates are the percentage change in **fraud losses per million transactions** after deployment. Negative means fewer.

| | Source | Size | Estimate |
|---|---|---:|---:|
| **A** | The bank's own home-market pilot | 3 regions | **−22%** |
| **B** | The vendor's study across client banks | 15 banks | **−35%** |
| **C** | An industry loss-reporting consortium | 620 institutions | **−5%** |
| **D** | The vendor's laboratory benchmark | 10 test suites | **−48%** |
| **E** | An internal risk panel of four analysts | — | **−15%** |

## Five supplied facts

**1. How the bank chose its pilot regions.** The three regions were the three with the highest fraud losses in the preceding year.

**2. What the vendor's client banks are.** All fifteen run the vendor's own card-processing platform, which carries a transaction identifier the rule uses. The bank entering the new market runs a different platform there.

**3. What the consortium records.** Membership is voluntary. There is no enforced definition of "fraud loss" — some members report gross attempted fraud, others only net write-offs after recovery.

**4. What the laboratory benchmark measures.** Synthetic transaction streams replayed against the rule, scored on how many flagged records match injected fraud patterns. There are no customers, no merchants, and no ninety-second hold.

**5. What the rule needs in order to work.** The ninety-second hold is useful only where a **shared interbank registry** can be queried within that window. The home market has one, operated by the central bank, with mandatory participation. **The new market has no such registry**; institutions there exchange fraud data in nightly batches.

**6. Two further facts about the sources.** The vendor sits on the consortium's data-standards committee and helped write its loss-reporting definitions. Two of the four panel members ran the home-market pilot.

For reference: `(3 × −22 + 15 × −35 + 620 × −5 + 10 × −48) ÷ 648`.

## Produce

Write a response containing all seven items.

1. **State the quantity the committee needs**, with its population, comparison, and variable.
2. **For each of the five sources, say what quantity it is an estimate of.** Mark which are about the committee's quantity and which are not.
3. **Compute at least three ways of combining the five**, including one that weights by size. State each result and what the rule assumes.
4. **Say what the size-weighted rule does**, and why that matters here.
5. **Identify the dependencies** among the five sources, and say what they do to the appearance of agreement.
6. **Name the support factor** the effect requires, and say whether the new market has it.
7. **State what would settle the question**, and for each thing you name say whether the bank could establish it this month, this year, or not at all.

Finish with **the paragraph you would put in front of the committee**: no more than five sentences, containing no single combined number.

**Stop when your response is complete. Do not open the rubric until then, and do not open Form A at all.**
