# Decision 0016: Chapter 9 Synthesis Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 9 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 6 records a fourth instance of the disposition `decisions/README.md` put on notice**, with the standing instruction that research be reopened rather than precedent invoked. It is referred to the author rather than resolved here.

Evidence base: `../chapters/09-evidence-synthesis/research-01-same-question.md`, `research-02-combining.md`, `research-03-replication.md`, `research-04-transport-and-examples.md`.

## Decision

Chapter 9's organizing claim is:

> Combining evidence is not averaging it, and transporting a result is not assuming it holds — and both failures turn on things no amount of the evidence can show.

### 1. The em dash is the chapter

**1.1** The governed central question is *What do many imperfect sources jointly support — here?* The chapter treats the two halves as **one question**, not two topics: the word after the dash is what makes the first half hard.

**1.2** Section ordering is therefore fixed: **whether the sources are about the same quantity comes before any weighting.** Placing weighting first would structurally commit the error the chapter exists to prevent.

### 2. No synthesis method is taught

**2.1** The governed core competence says "at an appropriate conceptual level". That is read as a licence and a limit.

**2.2** **No inverse-variance weighting, no random-effects model, no heterogeneity statistic, no funnel plot.** The chapter demonstrates that weighting rules disagree; teaching one would be teaching the rule whose failure is the demonstration.

**2.3** This is why 28 pages suffices where Chapters 7 and 8 needed 38 and 40.

### 3. Notation

**3.1** **None is added.** The book's notation stays where Decisions 0013 and 0014 left it, with 0015's refusal standing.

**3.2** No selection diagrams, no transport formulas. `bareinboim2016fusion` develops both on pages this book did not read.

**3.3** The three-decision notation sequence ends here without further comment to the reader; Chapter 8 already stated the position and Chapter 9 has no promise outstanding.

### 4. `external validity` is registered and criticised

**4.1** The term is introduced because readers will meet it everywhere.

**4.2** It is immediately criticised from the source: the binary concept "asks the results of an RCT to satisfy a condition that is neither necessary nor sufficient for a trial to be useful" [@deaton2016rct, p. 27].

**4.3** Same disposition Chapter 8 took toward `statistical significance`: register the term as a hazard, so the reader recognises it without organising their thinking around it.

**4.4** `transportability` is the preferred term for the substantive question.

### 5. Replication

**5.1** Both directions are taught from the source: successful replication "tells us little either for or against simple generalization", and "Nor do failures of replication make the original result useless" [@deaton2016rct, p. 27].

**5.2** The Russell's-chicken illustration is used **as reported at** [@deaton2016rct, p. 28]. Russell (1912) was not obtained and nothing is claimed about it.

**5.3** "Anecdotal causality" is quoted as the authors' phrase, not adopted.

### 6. Dependence between sources — an unsourced practice, flagged

**6.1** The chapter teaches that agreement among dependent sources is cheap — shared data, shared assumptions, shared training, shared measurement standards.

**6.2** **No source in this book's bibliography was found for it.** It follows directly from what dependence means and is the book's own reasoning.

**6.3** This is the **fourth** instance of the disposition recorded at `README.md` in this directory, after Decisions 0009 clause 6.3, 0011 clause 4.4, and 0012 clause 4.2. The standing instruction there is that **if a further chapter reaches for the disposition, research should be reopened rather than precedent invoked.**

**6.4** The chapter's treatment is therefore deliberately minimal — roughly one page, no taxonomy, no method — **pending author adjudication of whether research should now be reopened at book level.** This clause exists to make that decision unavoidable rather than to pre-empt it.

### 7. Transport

**7.1** `support factor` is taught from [@deaton2016rct, p. 28], with the source's own television example.

**7.2** The consequence for averages is taught from [@deaton2016rct, p. 29]: two populations share an average effect only if they share the average net effect of the support factors, and those are exactly the factors likely to differ.

**7.3** The second tradition's version is given from [@bareinboim2016fusion, p. 7350], and the manuscript notes that two traditions which disagree about method agree on the conclusion.

**7.4** Chapter 3's contextual specificity is **extended into transportability here**, which `../decisions/0010` clause 2.4 explicitly reserved for this chapter.

**7.5** **The Chapter 7 positivity / Chapter 9 transport identity is stated once, and labelled as the book's own observation.** Neither source draws it.

### 8. Expert judgment

**8.1** Treated as a source like any other, roughly two pages.

**8.2** **Chapter 6 is reused, not re-taught.** A panel that has never been scored is in exactly the position of Chapter 6's unscored forecaster, and the remedy is the same: a record.

**8.3** No elicitation protocols, no aggregation methods, no weighting-by-expertise schemes.

### 9. Vocabulary

**9.1** Introduced here: `evidence synthesis`, `heterogeneity`, `dependence`, `replication`, `external validity` (as a hazard), `transportability`, `support factor`, `expert judgment`.

**9.2** Closed here: `target population`, whose Chapter 1 entry records that "formal development in Chapters 7 and 9" was outstanding.

### 10. What Chapter 9 does not do

- Teach any synthesis or pooling method.
- Teach selection diagrams, transport formulas, or any graphical machinery.
- Teach elicitation or expert-aggregation methods.
- Characterise the replication-crisis literature — Chapter 8 declined this and Chapter 9 does not reopen it.
- Teach publication bias beyond naming it.
- Reopen Chapter 6's declined argument about what probability is.
- Recommend an action — Chapter 11.
- Treat choosing an action robust to source disagreement — Chapter 12.
- Treat whether a transported result held after deployment — Chapter 17.

## Sources promoted

`bareinboim2016fusion` is new to `references.bib`. `deaton2016rct` is extended from pp. 7–11 to pp. 26–29 — reading that two earlier chapters recorded as belonging here. `meng2018paradox` insight (IV) is used for the first time, having been recorded in Chapter 4 and left unused.

## Known gaps carried forward

1. **Pearl and Bareinboim's transportability paper obtained but declined**, for want of checkable pagination. Recorded in `../sources/bareinboim2016fusion.md`.
2. **Russell (1912), Mackie (1974), and Cartwright and Hardie (2012)** are cited within `deaton2016rct` and were not obtained.
3. **`deaton2016rct` remains an unrefereed working paper**, and pp. 12–25 and 30–70 are unread.
4. **`bareinboim2016fusion` read at pp. 7345, 7350, 7352 only.**
5. **No source found for source dependence** — clause 6.
6. Silberzahn et al. (2018), Wasserstein and Lazar (2016), Holland (1986), Rubin (1976) all remain unobtained.
7. The **Chapter 9 case is the water anchor's ninth recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields. Chapter 9 closes Part II as the architecture specifies.
