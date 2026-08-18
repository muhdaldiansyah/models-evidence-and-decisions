# Research 02 — Association, Intervention, Counterfactual

Cluster R02 of `research-plan.md`. Closed.

Sources read directly: `pearl2009causal` printed pp. 99–101, 107–110. `shmueli2010predict` as already verified for Chapter 1.

## 1. The demarcation line

`pearl2009causal` §2.2, printed p. 99, gives a criterion sharp enough to apply:

> "An associational concept is any relationship that can be defined in terms of a joint distribution of observed variables, and a causal concept is any relationship that cannot be defined from the distribution alone."

The same section lists both sides. Associational: "correlation, regression, dependence, conditional independence, likelihood, collapsibility, propensity score, risk ratio, odds ratio, marginalization, conditionalization, 'controlling for,'" [@pearl2009causal, pp. 99–100]. Causal: "randomization, influence, effect, confounding, 'holding constant,' disturbance, spurious correlation, faithfulness/stability, instrumental variables, intervention, explanation, attribution" [@pearl2009causal, p. 100].

**Two entries on that second list should stop the reader.** `confounding` and `randomization` are causal concepts, not statistical ones. A great deal of applied practice treats both as things you handle with a statistical procedure.

The chapter should use the demarcation line as a **test the reader can run**, not as a taxonomy to memorise: could this concept be written down using only the distribution of what you observe? If not, it is causal, and it will need an assumption from outside the data.

## 2. Why the distinction is not a technicality

`pearl2009causal` p. 99 states the consequence in a sentence the chapter should quote:

> "There is nothing in the joint distribution of symptoms and diseases to tell us that curing the former would or would not cure the latter."

And generalises it on the same page: "there is nothing in a distribution function to tell us how that distribution would differ if external conditions were to change".

Then the principle, p. 99:

> "one cannot substantiate causal claims from associations alone, even at the population level—behind every causal conclusion there must lie some causal assumption that is not testable in observational studies."

The article calls this its golden rule and restates it at p. 100: "behind any causal conclusion there must be some causal assumption, untested in observational studies."

### The consequence that will most disturb readers

`pearl2009causal` p. 100, on confounding:

> "confounding bias cannot be detected or corrected by statistical methods alone; one must make some judgmental assumptions regarding causal relationships in the problem before an adjustment (e.g., by stratification) can safely correct for confounding bias."

The argument for this is short and worth reproducing rather than asserting. If confounding could be defined associationally, you could find confounders in observational data, adjust for them, and obtain unbiased causal estimates — which would produce a causal conclusion with no causal assumption, contradicting the golden rule. The page says so directly: "Hence the definition must be false."

The chapter can carry that argument. It requires no notation.

## 3. The testability asymmetry

`pearl2009causal` §2.4, printed p. 101, is the single most useful passage in the article for this book:

> "Associational assumptions, even untested, are testable in principle, given sufficiently large sample and sufficiently fine measurements. Causal assumptions, in contrast, cannot be verified even in principle, unless one resorts to experimental control."

And, on the same page, the point about sample size:

> "the sensitivity to these priors tends to diminish with increasing sample size. In contrast, sensitivity to prior causal assumptions, say that treatment does not change gender, remains substantial regardless of sample size."

**This is the fourth instance of the book's recurring shape, and the first that arrives cited.**

| Chapter | More of this improves | And does nothing for |
|---|---|---|
| 3 | measurements | precision, not trueness |
| 4 | records | sampling variability, not the data-quality term |
| 6 | simulation runs | Monte Carlo error, not model error |
| 7 | sample size | associational uncertainty, not sensitivity to causal assumptions |

Chapters 3, 4, and 6 each observed the pattern from their own material; the book supplied the pattern. Here a source supplies it. The manuscript should say so, because a reader who has met the shape three times deserves to know that the fourth is not the book pushing an analogy.

**Handling note.** Chapter 6 §7 already carries a three-row version of this table. Chapter 7 must extend it rather than restate it, and `../../decisions/0014` should record which chapter owns the canonical version. Recommendation: Chapter 7 owns the four-row table, Chapter 6's three-row version stands as written.

## 4. The two mental barriers

The same section, p. 101, names what stops people crossing:

> "The preceding two requirements: (1) to commence causal analysis with untested, theoretically or judgmentally based assumptions, and (2) to extend the syntax of probability calculus, constitute the two main obstacles to the acceptance of causal analysis among statisticians and among professionals with traditional training in statistics."

This matters for the chapter's design in a direct way. **The book's readers face exactly these two barriers**, and the second one has been institutional policy for six chapters. Chapter 6 opened a bounded notation exception and announced it; Chapter 7 must decide whether to extend it, and the honest framing is the one the source supplies: the notation exists because the distinction cannot be made in the existing syntax.

`pearl2009causal` p. 100 puts the necessity plainly: "any mathematical approach to causal analysis must acquire new notation for expressing causal relations – probability calculus is insufficient."

The chapter should quote that when it announces its notation, exactly as Chapter 6 gave its reason before its bar.

## 5. Where the boundary with Chapter 6 sits

Chapter 6 taught conditioning: `P(A | B)`, updating on an observation. Chapter 6 §3 also stated, once, that conditioning is not intervening, and routed the argument here.

The distinction the chapter must install:

- **Observing** that the pump was replaced tells you something about the zones in which pumps get replaced.
- **Intervening** to replace the pump asks what happens when the replacement is imposed rather than selected.

`pearl2009causal` p. 101 records both established notations for the second — subscripted potential outcomes and the `do(·)` form — and p. 109 works an example in which the two coincide, showing that the intervention distribution equals the conditional distribution *under stated assumptions*, which is exactly the point: they can be equal, and whether they are is an assumption, not a default.

That is the cleanest available statement of the Chapter 6 / Chapter 7 line, and it is worked rather than asserted.

## 6. The third level

`pearl2009causal` §3.4 (printed pp. 119–121) treats counterfactuals in structural models. The chapter needs the *distinction* and none of the machinery.

- **Association**: among zones that had upgrades, how often did complaints fall?
- **Intervention**: if we upgrade Hillcrest, what happens to complaints?
- **Counterfactual**: Hillcrest was not upgraded and complaints rose; would they have risen if it had been?

The third is about a case whose actual outcome you already know, which is why it needs more than the second does. p. 121 records that "attributional queries are generally not identifiable in nonparametric models", which the chapter can use to make one honest point: **the third question is harder than the second, and frequently unanswerable, and it is the one management most often asks.**

Do not develop probabilities of causation. `pearl2009causal` §5.2 is out of scope by the research plan.

## 7. The prediction leg

`shmueli2010predict`, verified in Chapter 1, supports the claim that a predictive relationship may capture association without causal interpretation and that a useful predictor is not automatically a causal lever.

Chapter 7 needs it once. A model that predicts Hillcrest's pressure drops accurately is not thereby a guide to what happens if you act on any of its inputs, and prediction being Chapter 6's home means the reader has just spent 12,000 words getting good at exactly the thing that does not answer this chapter's question.

## 8. Stop condition

Met. Demarcation line, golden rule, confounding consequence, testability asymmetry, the two barriers, and the three levels are all recorded with locators from direct reading.

Not read for this cluster: `pearl2009causal` §§4–6 (printed pp. 126–139), beyond the p. 122 spine already recorded in R01.
