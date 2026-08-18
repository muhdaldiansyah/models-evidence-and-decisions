# Chapter 17 Bounded Research Plan

Status: working control. Governs what was researched before drafting and what was deliberately not.

Written after `readiness-audit.md` and executed against it.

## Standing rules carried forward

1. **Every locator must come from reading the document directly.** (Chapter 5.)
2. **Quote only prose that survives text extraction cleanly.** No quotation may contain a comparison symbol. (Chapters 7 and 8.)
3. **Cite the version whose pagination you can see.** (Chapter 9; bounded exception proposed at `../../decisions/0022` clause 8 and applied once more at `0023` clause 6.)

**Rule 3 needs no exception in this chapter.** Both new readings have pagination that is visible and independently checkable, and `../../decisions/0024` clause 8 records that the exception is **not** extended further.

## What was obtained, and how

**`nasa2024models` — upgraded from four locators to a substantial reading.**

*NASA-STD-7009B: Standard for Models and Simulations*, approved 5 March 2024, obtained in full from the NASA technical standards system — 88 pages, freely available.

**Its pagination is checkable against itself.** Every entry in the standard's own table of contents matches the corresponding PDF page exactly: section 4 at p. 18, Appendix A at p. 39, Appendix F at p. 86. **Printed page equals PDF page**, verified at six points.

Read at pp. 18, 22, 30, 39, and 86–88 — the requirements framing, the programmatic requirements, section 4.3 on M&S use, the requirements matrix, and Appendix F on the M&S life cycle.

**Chapter 1 read this source for `intended use` and cited it by file page.** Chapter 17 reads it for deployment, permissible use, life cycle, and retirement, and cites printed pages, having established that the two coincide.

**`sumanprajapati2018control` — new to the bibliography.**

Suman and Prajapati, "Control chart applications in healthcare: a literature review", *International Journal of Metrology and Quality Engineering* 9, 5 (2018). Open access under a Creative Commons licence stated on its first page.

**Printed page numbers appear in the running heads on even pages** — 2, 4, 6, 8 — and equal the PDF pages. Read at p. 1.

**It is a literature review of healthcare applications**, not a conceptual treatment, and it is used for exactly two things: the attribution of statistical process control to Shewhart, and the statement that the method rests on the common-cause/special-cause distinction. **Nothing else is taken from it.**

## Two sources already read, reused

**`perdomo2020performative`**, read at Abstract and §1 for Chapter 15, supplies drift that is caused by deployment. **Cited by section**, as Chapter 15 established.

**`gneiting2007scoring`**, read for Chapter 6, supplies calibration and sharpness as the standing instrument for monitoring a forecast. **Nothing new is claimed from it**; Chapter 6's locators and cautions stand.

## Sources sought and not obtained

**Shewhart (1931), *Economic Control of Quality of Manufactured Product*.** The origin of the common-cause/special-cause distinction, confirmed from `sumanprajapati2018control` p. 1. **Not obtained.** The distinction is used **as reported at** that review, which is the device this book has used since Chapter 6.

**Deming, on tampering and the funnel experiment.** Two routes attempted, both failed. **`tampering` is named in this chapter's governed core competence and no source for it was obtained** — see below.

**Benneyan, Lloyd and Plsek (2003)** and two other BMJ Quality and Safety papers on statistical process control: all three returned 403.

**A Minnesota Department of Health control-chart handout** was obtained and **declined**: three pages, no named author, no journal, no printed pagination. It is clearer than the review on the mechanics and weaker on everything the book cares about, and grey literature of that kind is not what this book cites.

## The term with no source

**`tampering`** is named in `README.md`'s Chapter 17 core competence — "recognize drift and tampering" — and no source for the term was obtained.

**It is registered as the book's own controlled term**, and `../../decisions/0024` clause 6 records three things about that.

**The mechanism it names is already sourced.** Chapter 13 established, from `sterman2006evidence` p. 508, that decision-makers "continue to intervene to correct apparent discrepancies... even after sufficient corrective actions have been taken to restore equilibrium", and that the result is overshoot and oscillation. **Tampering is that mechanism applied to a stable process**, and the book has the mechanism verbatim.

**So this is not a new instance of the demonstrate-because-unsourced disposition**, which concerns practices taught with no source behind them. What is unsourced here is a **name**, not a claim.

**And it is flagged rather than smoothed over**, because the name is in governed text.

## Bounds — what was deliberately not researched

**No control-chart construction.** No centre lines, no control limits, no run rules, no chart types, no sampling plans. `README.md` permits this machinery "where appropriate"; the audit's finding is that the core competence names the **distinction** and not the technique, and `../../decisions/0024` clause 2 records the choice.

**No statistical process control literature beyond the attribution.** One page of one review was read.

**No drift-detection methods.** No distribution-shift tests, no change-point detection, no CUSUM, no sequential analysis.

**No governance or assurance frameworks.** `nasa2024models` was read for its life cycle, not for its assurance architecture; `fda2023credibility`, `asme2025credibility`, and `nrc2012reliability` were **not re-read**, and Chapter 1's locators for all three stand unchanged.

**No machine-learning monitoring literature**, for the same reason Chapter 16 sought none: `README.md` records that AI in this book is an application and a stress test.

**No reliability engineering, no maintenance scheduling, no condition monitoring.**

## Known gaps carried forward

1. **Shewhart (1931) not obtained**; the common-cause distinction is used as reported at a 2018 review.
2. **No source for `tampering`**, which is in governed text — see above and `../../decisions/0024` clause 6.
3. **`sumanprajapati2018control` is a healthcare literature review**, read at one page, and used for two claims only.
4. **`nasa2024models` read at seven of eighty-eight pages**; nothing is claimed about the standard's assurance architecture, its criticality assessment, or its credibility scales.
5. **No pilot data exists for any transfer form in this book**, including this chapter's.
6. **The case is the water anchor's sixteenth and final appearance**, and Chapter 1's Gate 1 remains open across all sixteen.
