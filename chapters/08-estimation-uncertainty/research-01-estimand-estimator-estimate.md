# Research 01 — Estimand, Estimator, Estimate

Cluster R01 of `research-plan.md`. Closed.

Sources: `fda2021estimands` as verified in Chapters 1 and 7; `../07-targets-identification/research-01-targets-and-estimands.md`; `greenland2016misinterpretations` read directly at pp. 339–340.

## 1. Two canon entries, open since Chapter 1

`../../canon/terminology.md` has carried `estimator` and `estimate` at `Definition status: TODO — verify against canonical sources` since the Chapter 1 block was written. Chapter 7 closed `statistical identifiability` and `causal identification` from the same backlog. These two are the remainder.

Chapter 1 already told the reader they are three different things, and `../../sources/fda2021estimands.md` records the source separating the target of estimation, the method of estimation, and the numerical result.

## 2. The separation, stated without notation

- **`estimand`** — the specified target of estimation. Chapter 7's formal home. *What you want to know.*
- **`estimator`** — the procedure applied to data to produce a number. *How you work it out.*
- **`estimate`** — the number that procedure produced on the data you actually have. *What you got.*

Three things, and the reader needs to hold all three because **every failure this chapter treats is a confusion between two of them.**

| Confusion | What it produces |
|---|---|
| estimate treated as estimand | "the effect is 1.8" — a number reported as the thing itself |
| estimator treated as estimand | the question quietly becomes whatever the method computes |
| estimand treated as estimator | a target defined by what is convenient to calculate |
| estimator's properties attributed to the estimate | "this is an unbiased estimate" — a category error, see §4 |

## 3. Which estimator properties a general reader needs

Textbook treatments give many. Three are worth a general reader's attention and the rest are depth curriculum.

**Bias.** Whether the procedure, applied over and over to fresh data from the same process, centres on the estimand. A property of the procedure.

**Variance.** How much the procedure's output moves between such applications. Also a property of the procedure.

**Consistency.** Whether the procedure converges on the estimand as the amount of data grows without limit.

**All three are properties of the procedure, not of your number**, and that is the whole reason to name them. It is the same structure Chapter 6 established for calibration and Chapter 7 for balance: a property defined over an ensemble, routinely read off a single instance.

Chapter 8 is therefore the **third** appearance of that shape, and the manuscript should say so once.

## 4. The category error worth naming

"This is an unbiased estimate."

Strictly, no. Unbiasedness is a property of the estimator. The estimate is one number, and one number is neither biased nor unbiased — it is simply the number the procedure gave on the data at hand, which may be far from the estimand even when the procedure is unbiased.

This is not pedantry about wording. The sentence licenses a reader to treat the number as trustworthy in a way that nothing about it supports, and the licence comes from grammar rather than evidence.

**Chapter 3's parallel.** A calibrated instrument is not a correct reading. Chapter 3 established that trueness is a property of the instrument and a given reading still carries random error. Same structure, different vocabulary.

## 5. The `consistency` collision

`consistency` here means the estimator property in §3.

`consistency` in Chapter 7 means the causal identifiability condition — that the observed outcome under the treatment received equals the counterfactual outcome under that treatment, which requires the intervention to be well defined.

**These have nothing in common beyond the word.**

`../../canon/terminology.md` already flags the collision from the Chapter 7 side: the entry reads "**consistency of an estimator (Chapter 8), which is an unrelated concept sharing the word**". Chapter 8 completes the pair.

Handling: announce once, at the point of use, both senses stated, as Chapter 6 did for `calibration` and Chapter 5 for `validation`. This is the fourth such announcement and the manuscript may note that the book keeps meeting them, because it works across fields that borrowed each other's words without coordinating.

## 6. And one word the chapter should decline

`confidence`, in the technical sense, is worse than a collision — the ordinary word promises exactly what the technical term withholds.

The source is explicit that this is a known problem: statistical usages of "significance" and "confidence" are "at odds with other authors and with ordinary English definitions" [@greenland2016misinterpretations, p. 339].

**Recommendation for `../../decisions/0015`:** the book uses `interval estimate` in its own prose, introduces `confidence interval` once as the term the reader will meet everywhere else, and never uses `confidence` alone to mean the technical thing.

This is the same disposition Chapter 3 took toward `validation` — decline the word, name why, and route the reader to what they will encounter elsewhere.

## 7. Stop condition

Met. The three-term separation is stateable without notation; three estimator properties are selected and the rest deferred; the collision is documented from both sides; a recommendation on `confidence` is on the record for adjudication.
