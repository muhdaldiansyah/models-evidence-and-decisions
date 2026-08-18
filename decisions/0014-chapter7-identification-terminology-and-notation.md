# Decision 0014: Chapter 7 Identification Terminology and Notation

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `research-plan.md` and `readiness-audit.md` §9 reserve these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 7 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 2 extends the notation exception that Decision 0013 clause 2 opened, which is itself still unadjudicated.** Adjudicating this record without adjudicating 0013 first would be incoherent.

Evidence base: `../chapters/07-targets-identification/research-01-targets-and-estimands.md`, `research-02-association-intervention-counterfactual.md`, `research-03-identification.md`, `research-04-designs-and-examples.md`.

## Decision

Chapter 7's organizing claim is:

> Whether evidence can establish a causal claim is settled by the question and the assumptions, not by the data — so it can be settled before any data is collected, and frequently the answer is that it cannot.

### 1. The chapter's spine is taken, not invented

**1.1** Chapter 7 is organized on the four steps at [@pearl2009causal, p. 122]: **Define, Assume, Identify, Estimate.** Steps 1–3 are the chapter; step 4 is Chapter 8.

**1.2** The spine is **attributed at the point of use** and is not presented as the book's own device. This differs from Chapter 5, which had to add a fourth step to Platt's three; here the source supplies all four.

**1.3** The Chapter 7 / Chapter 8 boundary is therefore stated in the source's own terms, and [@pearl2009causal, p. 117] §3.3.3 "From identification to estimation" is cited for it rather than an assertion of the book's.

### 2. Notation — a second bounded exception

**2.1** Decision 0013 permitted `P(A | B)` and odds as `3 : 1`, and nothing else. Chapter 7 cannot make its central distinction inside that permission, for the reason the source gives: "any mathematical approach to causal analysis must acquire new notation for expressing causal relations – probability calculus is insufficient" [@pearl2009causal, p. 100].

**2.2** Permitted additions, and only these:

- **`do(·)` inside Chapter 6's bar** — `P(pressure recovers | do(replace the pump))` as distinct from `P(pressure recovers | the pump was replaced)`. The bar is already the reader's; `do(·)` marks the one difference the chapter exists to teach.
- **Arrows for causal structure**, written inline as `heat → demand → pressure`. No boxes, no formal diagram conventions, no error terms.

**2.3** Not permitted: potential-outcome superscripts or subscripts; do-calculus rules; d-separation, blocking, or collider vocabulary as machinery; the back-door criterion stated as a criterion; summation, integration, or any notation refused by Decision 0013 clause 2.3.

**2.4** The exception is **announced to the reader** with its reason, at the moment of first use, in the same way Chapter 6 announced its bar. The announcement quotes [@pearl2009causal, p. 100] for why prose is insufficient.

**2.5** `do(·)` is chosen over potential-outcome notation on one ground: it is the smaller change. It reuses a symbol the reader already reads fluently and adds one marker inside it. Potential outcomes would require a new object with its own indexing conventions. **This is a pedagogical choice, not a claim that one framework is better**, and the manuscript says so.

### 3. The two frameworks, named and not adjudicated

**3.1** The chapter names that a potential-outcome tradition and a graphical/structural tradition both exist, and that they have well-known proponents who disagree in print.

**3.2** **The book does not adjudicate the argument**, on the same grounds Decision 0013 clause 1 declined the frequency/degree-of-belief argument: the chapter's work can be done from either, and both traditions define the chapter's central concept compatibly ([@pearl2009causal, p. 109]; [@hernan2019whatif, p. 27]).

**3.3** The chapter says the two definitions agree. It does not say the frameworks are equivalent, which is a stronger claim it has not researched.

### 4. Identification

**4.1** Three senses are distinguished by name and never used unqualified:

- **statistical identifiability** — whether parameters are pinned down by the distribution the model implies;
- **causal identification** — whether a causal quantity is pinned down by the observable distribution *together with causal assumptions*;
- **structural identifiability** — deferred to Chapter 14 by `README.md`; **named in one paragraph and not taught.**

**4.2** The reader-facing formulation — *if two states of the world would produce the same data forever and give different answers, no amount of that data settles it* — is **the book's own phrasing of a sourced idea** and is labelled as such per `../canon/pedagogy.md`.

**4.3** Identification is taught as **relative to assumptions**, never as a property a quantity has on its own. [@hernan2019whatif, p. 27]: "we need an assumption external to the data, an identifying assumption."

**4.4** **Not identified is taught as a result, not a failure.** [@pearl2009causal, p. 122] step 4 includes approximating a non-identified quantity, and the chapter's verdict format requires saying which assumption would change the answer.

### 5. The three conditions

**5.1** `exchangeability`, `positivity`, and `consistency` are introduced from [@hernan2019whatif, p. 26] with their source names.

**5.2** The source's own characterisation — that the conditions are "often heroic" [@hernan2019whatif, p. 26] — is carried into the manuscript. **They are not presented as a checklist.**

**5.3** `consistency` **collides** with the statistical sense Chapter 8 needs. Handled exactly as Chapter 6 handled `calibration` and Chapter 5 handled `validation`: announced once, at the point of use, with both senses stated and the reader told the book will use both.

**5.4** The conditions are demonstrated on the anchor, not on the sources' medical examples. `research-04` §6 prohibits medical examples in the body.

### 6. Randomization

**6.1** What randomization buys is stated from [@deaton2016rct, p. 10] and what it does not buy is stated from the same page and p. 11.

**6.2** The chapter uses a **documented published overstatement** rather than a straw man, quoted **as reported at** [@deaton2016rct, p. 10]. The underlying manual was not obtained and is never cited directly.

**6.3** `deaton2016rct` is described in the manuscript as a working paper whose cover states it has not been peer-reviewed. Its stronger claim — that randomization is "generally inferior to good control" — is **attributed to its authors, not asserted**.

**6.4** The chapter must not leave the reader concluding that only experiments establish causes. [@hernan2019whatif, p. 25] is cited against that conclusion.

### 7. The recurring shape, fourth instance

**7.1** [@pearl2009causal, p. 101] supplies the fourth instance: sensitivity to causal assumptions "remains substantial regardless of sample size."

**7.2** **Chapter 7 owns the four-row version of the table.** Chapter 6 §7's three-row version stands as written and is not edited. The manuscript states that the first three instances were the book's own observation and the fourth arrives cited.

### 8. Vocabulary

**8.1** Introduced here: `target quantity`, `identifying assumption`, `exchangeability`, `positivity`, `consistency` (causal sense), `target trial`, `confounding`.

**8.2** Closed here, from `Definition status: TODO`: `statistical identifiability`, `causal identification`.

**8.3** Specialised here from Chapter 1 previews: `estimand`, `intervention`, `counterfactual`, and the Chapter 7 half of `target`.

**8.4** The hierarchy `target` → `target quantity` → `estimand` → `estimator`/`estimate` is adopted, with the last two remaining Chapter 8's.

**8.5** The ICH attribute list is **not** promoted to the book's universal definition of `estimand`, per the standing caution in `../sources/fda2021estimands.md`. Its generalisation is labelled pedagogical synthesis.

**8.6** The alignment between the ICH attributes and the target-trial protocol components is **the book's own table** and is presented as such. Neither source draws it.

### 9. What Chapter 7 does not do

- No estimator, standard error, interval, or model check — Chapter 8.
- No do-calculus, d-separation, or back-door criterion as machinery.
- No instrumental variables beyond one naming sentence.
- No mediation, direct or indirect effects, or probabilities of causation.
- No propensity scores, IP weighting, standardization, or matching.
- No transportability or external validity beyond one sentence routing to Chapter 9.
- No claim that any design is best.
- No decision recommendation — Chapter 11.
- No treatment of strategic response to intervention — Chapter 15.
- No structural identifiability — Chapter 14.

## Sources promoted

`hernan2019whatif` and `deaton2016rct` are new to `references.bib`, each with a source note recording exactly what was read and what was not. `pearl2009causal` is promoted from a Chapter 1 supporting citation to a Chapter 7 load-bearing one, and was re-read at pp. 99–101, 107–110, 113–117, and 122 for the purpose.

## Known gaps carried forward

1. **Holland (1986) not obtained.** The fundamental problem of causal inference is stated from `hernan2019whatif` and no claim is made about Holland's contents.
2. **The published Deaton and Cartwright not obtained.** Working paper only.
3. **`hernan2019whatif` read at pp. 25–38 only**, in a dated manuscript version whose pagination does not match the printed edition.
4. **`deaton2016rct` read at pp. 7–11 of 70 only.**
5. **Rubin (1976) still unobtained**, as since Chapter 4.
6. The **Chapter 7 case is the water anchor's seventh recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields. The structural-identifiability deferral to Chapter 14 is followed, not revised.
