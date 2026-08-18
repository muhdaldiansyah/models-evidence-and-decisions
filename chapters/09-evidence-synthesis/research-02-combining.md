# Research 02 — Combining

Cluster R02 of `research-plan.md`. Closed.

Source: `meng2018paradox` printed pp. 685–687, already verified for Chapter 4. The locators below are those recorded in `../../sources/meng2018paradox.md` from that direct reading.

## 1. The claim Chapter 4 recorded and did not use

The abstract's fourth numbered insight:

> "When combining data sources for population inferences, those relatively tiny but higher quality ones should be given far more weights than suggested by their sizes." [@meng2018paradox, p. 685]

**This is the only published statement in the book's bibliography that speaks directly to how sources should be weighted**, and Chapter 4 could not use it because Chapter 4 was about one dataset. It comes due here.

Note precisely what it says. Not that size is irrelevant — that tiny high-quality sources deserve **far more** weight than size suggests. It is a claim about the direction and the magnitude of the correction.

## 2. How large the discrepancy can get

The same page records a worked instance:

> estimates from the CCES "suggest a ρ_{R,X} ≈ −0.005 for self-reporting to vote for Donald Trump. Because of LLP, this seemingly minuscule data defect correlation implies that the simple sample proportion of the self-reported voting preference for Trump from 1% of the US eligible voters, that is, n ≈ 2,300,000, has the same mean squared error as the corresponding sample proportion from a genuine simple random sample of size n ≈ 400, a 99.98% reduction of sample size" [@meng2018paradox, p. 685]

**2,300,000 records worth 400.** A ratio of about 5,750 to 1, produced by a defect correlation of −0.005.

If a size-weighting rule had been applied to combine that dataset with a small clean survey, the large source would have received essentially all the weight and deserved almost none.

### The cautions, carried intact

`../../sources/meng2018paradox.md` records four constraints and every one binds this chapter as it bound Chapter 4:

- **Do not say "big data is bad".** The claim is conditional on data quality not being taken into account; a large dataset with the defect correlation near zero is excellent.
- **Do not attribute the 400-equivalent figure to any dataset other than the CCES 2016 self-reported Trump preference.**
- **The −0.005 is a data defect correlation**, not a bias, a rate, or a percentage.
- **Do not state the identity as a formula.** Chapter 4 declined it and Chapter 8 declined it; Chapter 9 declines it a third time.

## 3. What follows for a reader with five reports

The general lesson, stated as the book's own and labelled:

> **Sample size is a measure of how much of a source you have, not of how much it is worth.**

The rule most people apply — weight by size — is exactly the rule the source's insight (IV) says is wrong, and it is wrong in the direction that matters, because the largest sources are frequently the ones assembled with the least control over who is in them.

**Which is not an argument for weighting by quality instead**, because quality is not a number you have. It is an argument for the thing §3 of the manuscript does: compute several defensible weightings, see how far apart they land, and treat that spread as the finding.

## 4. Dependence, which no source in this book addresses

Five reports are not five independent pieces of evidence when:

- two of them analyse the same underlying dataset;
- one cites another as its prior;
- three were produced by people trained in the same place, using the same software defaults;
- all five assume the same measurement definition, which came from the same standard.

**Agreement among dependent sources is cheap**, and it is indistinguishable from agreement among independent ones when all you see is five numbers.

**No source in this book's bibliography was found for this.** It is stated as the book's own reasoning, follows directly from what dependence means, and is flagged here rather than asserted in the manuscript without attribution.

This is the **fourth** time the book has taught a practice by demonstration because no source was obtained for it — the pattern `../../decisions/README.md` put on notice after three, with the standing instruction that if a further chapter reaches for the disposition, **research should be reopened rather than precedent invoked.**

`../../decisions/0016` clause 6 records this explicitly and refers it to the author. The chapter's treatment is deliberately short — one page, no taxonomy — pending that adjudication.

## 5. The anchor's arithmetic

Five sources bearing on what a pump upgrade does to complaints per heat event. Four defensible ways of combining them:

| Rule | Result |
|---|---:|
| Simple average of all five | **−2.48** |
| Median of all five | **−2.40** |
| Weight by sample size | **−0.70** |
| Drop the source with the known defect, average the rest | **−3.43** |

Computed and checked. The size-weighted rule gives the largest source **95.8%** of the weight, and that source is the one with a stated participation defect.

**Four rules, a range of −0.70 to −3.43** — a factor of nearly five, from one set of five reports, with no arithmetic error anywhere.

## 6. Stop condition

Met. Insight (IV) recorded with locator; the equivalence figure restated with all four cautions; dependence flagged as unsourced and referred for adjudication; the anchor's four rules computed and checked.

Not read beyond `meng2018paradox` p. 687, as in Chapter 4.
