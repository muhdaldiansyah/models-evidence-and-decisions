# Decision 0017: Chapter 10 Values Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 10 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 5 resolves a boundary that two governing documents divide differently**, and is the clause most in need of attention.

Evidence base: `../chapters/10-values-alternatives/research-01-values-objectives-alternatives.md`, `research-02-what-counts-as-an-objective.md`, `research-03-stakeholders-and-constraints.md`, `research-04-alternatives-and-examples.md`.

## Decision

Chapter 10's organizing claim is:

> The option set you were handed is already a claim about what matters, made by whoever drafted it — and writing down what actually matters produces options nobody listed.

### 1. The Keeney handling

**1.1** `../sources/keeney1996valuefocused.md` prohibits attributing value-focused procedures, objective hierarchies, or alternative-generation methods to that article without full-text verification.

**1.2** **Full-text verification was attempted and failed** — four routes. The prohibition therefore stands unmodified and Chapter 10 honours it. Nothing is attributed to `keeney1996valuefocused` beyond its verified abstract.

**1.3** The framework is taken **as reported at** `bradley2016structured` pp. 5–8 and 49–54, a 248-page EPA report obtained in full and read at those pages, which carries its own attributions to Keeney (1992, 2007), Gregory et al. (2012), and Carriger and Benson (2012).

**1.4** **This is not an instance of the demonstrate-because-unsourced disposition** that `README.md` in this directory has on notice at four instances. There, a practice was taught with no source at all. Here, a well-sourced framework is cited through a source that reports it — the same device used for Brier (Chapter 6), Matrixx (Chapter 8), and Russell (Chapter 9). **The count stays at four.**

### 2. Values, objectives, alternatives

**2.1** The three-term relationship is taught from [@bradley2016structured, p. 5], quoted.

**2.2** The alternative-focused/value-focused contrast is taught as the **default failure**, not an aberration: it is "the more common" approach on the source's own page.

**2.3** The chapter's central move is that **values are always present and the question is whether they were written down** — the same structure as Chapter 6's unstated conditioning, Chapter 7's unstated identifying assumption, and Chapter 8's unstated analytic conduct.

**2.4** The source's own concession is carried: value-focused thinking adds a step. The chapter does not present the discipline as free.

**2.5** The source's own scope limit is carried: "single issue, well-defined decisions do not need a formal methodology" [@bradley2016structured, p. 7]. A book that told readers to build a hierarchy before choosing lunch would be teaching ceremony.

### 3. What counts as an objective

**3.1** The two-part format is taught as a **test**: an objective has an item of value and a direction of preference [@bradley2016structured, p. 50].

**3.2** The "why is this important" test distinguishes fundamental from means objectives [@bradley2016structured, p. 51].

**3.3** The six properties of good objectives are **quoted once, attributed, and only two are developed** — Fundamental and Independent. Gregory et al. (2012) was not obtained and the report gives no gloss; inventing definitions for *Sensitive* and *Concise* would attribute content to an unobtained source.

**3.4** `attribute` and `objective` are paired as "what will be assessed" and "what is valued" [@bradley2016structured, p. 51], and the pairing is linked **once** to Chapter 3's construct/measure ladder.

**3.5** `metric` is introduced with its Chapter 15 forward reference intact, as canon already records.

### 4. Stakeholders and constraints

**4.1** Stakeholders are those **affected**, and the qualification for having a value is being affected rather than expertise [@bradley2016structured, p. 7].

**4.2** The four traps are quoted and attributed [@bradley2016structured, p. 7]. The illustrations attached to them in the manuscript are **the book's own** and are labelled.

**4.3** The constraint practice — ask of each stated constraint who set it and what would change it — is **derived from a named trap in a read source**. The two-bucket sorting the chapter uses is the book's own illustration, labelled. **This is not a fifth instance of the disposition under notice**, and clause 1.4's distinction applies.

**4.4** No facilitation technique, elicitation protocol, or workshop design. Both sources are written by people who run deliberative processes; the book is not a manual for running them.

### 5. The Part III boundary — a conflict resolved

**5.1** `decisions/0006` states that "Chapter 10 owns formal value structuring, objectives, measurable attributes or metrics, systematic alternative generation, **and trade-off structure**." `README.md`'s governed block for Chapter 11 assigns trade-offs and value of information there.

**5.2** **These divide the boundary differently and the conflict must be surfaced rather than silently resolved.**

**5.3** The resolution proposed follows the generic process table at [@bradley2016structured, p. 8]: **Chapter 10 owns Decision context, Objectives, and Alternatives. Chapter 11 owns Prospects, Trade-offs, and Recommendations.**

**5.4** Chapter 10 therefore establishes **that objectives conflict and that trade-offs will be required**, and stops. No weighting, scoring, ranking, or preference method appears.

**5.5** If the author prefers 0006's division, Chapter 10 gains a section and Chapter 11 loses one, and `README.md`'s Chapter 11 block would need revisiting. **That is an architectural change and is not made here.**

### 6. Alternatives

**6.1** Generation is taught as **derivation from objectives**, not brainstorming, per the ordering rule at [@bradley2016structured, p. 54].

**6.2** The three evaluation dimensions — complexity, effectiveness, consequences to other objectives — are taught as a way of examining an alternative, not scoring one.

**6.3** **The chapter states once that one of its generated alternatives is an act the book already produced for a different reason.** Chapter 7 §6 proposed arranging one comparison deliberately as an identification strategy; Chapter 9 §5 repeated it; here it arrives as a decision alternative derived from objectives. Two framings, one act — **the book's own observation**, and the second of its kind after the Chapter 7 positivity / Chapter 9 transport identity.

### 7. Notation

**7.1** **None is added.** Fourth consecutive chapter. The book's notation stays where Decisions 0013 and 0014 left it.

### 8. Vocabulary

**8.1** Introduced here: `value`, `fundamental objective`, `means objective`, `attribute`, `stakeholder`, `constraint`.

**8.2** Closed here, from `Definition status: TODO` since Chapter 1: `objective`, `metric`.

**8.3** `alternative` is specialised from its Chapter 1 entry, which recorded that "systematic alternative generation remains Chapter 10".

### 9. What Chapter 10 does not do

- Weigh, score, rank, or trade off — Chapter 11.
- Treat utility, preference elicitation, or value of information — Chapter 11.
- Optimise over the alternative set — Chapter 12.
- Treat metric gaming — Chapter 15.
- Treat implementation and monitoring beyond naming the loop — Chapter 17.
- Enter moral philosophy. `nasem2026decisionmaking` has a values-and-ethics section; the chapter uses the practical separation only.
- Teach the DPSIR device, which is domain-specific to the source.
- Recommend an action for the utility.

## Sources promoted

`bradley2016structured` is extended from the Chapter 1 sections recorded in its source note to printed pp. 5–8 and 49–54, read directly. `nasem2026decisionmaking` is reused as verified, with both its recorded cautions inherited. `keeney1996valuefocused` remains at abstract-level verification and is **not** relied on for procedures.

## Known gaps carried forward

1. **`keeney1996valuefocused` full text not obtained**, after four attempts. The existing prohibition stands.
2. **Keeney (1992), Keeney (2007), Gregory et al. (2012), Carriger and Benson (2012), Carriger et al. (2013)** are all cited within `bradley2016structured` and none was obtained.
3. **`nasem2026decisionmaking` free PDF could not be downloaded in this pass**; only the sections already recorded in its source note are used.
4. **`bradley2016structured` read at pp. 5–8 and 49–54** for this chapter, plus the Chapter 1 sections previously recorded.
5. The constraint sorting and the trap illustrations are **the book's own** and are labelled.
6. The **Chapter 10 case is the water anchor's tenth recurrence**, and Chapter 1's Gate 1 remains open.

## Architecture note

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields.

**It does resolve a conflict between two existing governing documents** — clause 5 — in favour of `README.md`, which the authority order in `CLAUDE.md` makes controlling. `decisions/0006`'s wording would need amending to match if the author accepts the resolution, and that amendment is **not** made here.
