# Decision 0024: Chapter 17 Deployment Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

**This is the last chapter's record**, and three clauses need author attention: clause 2, which declines machinery the architecture permits; clause 6, which registers a term named in governed text with no source; and clause 10, which concerns how the book ends.

Evidence base: `../chapters/17-deployment-monitoring/research-01-deployment-and-permissible-use.md`, `research-02-signal-and-ordinary-variation.md`, `research-03-drift-tampering-and-blind-spots.md`, `research-04-cases-and-exercises.md`.

## Decision

Chapter 17's organizing claim is:

> Monitoring catches failures that show up in outputs, and is constitutionally incapable of catching failures in what the thing was built to represent — because those produce outputs that look right.

### 1. Two inherited cases, and no new ones

**1.1** `canon/terminology.md`'s `signpost` entry assigns the operation of Chapter 12's signposts here. `../chapters/16-integration-full-loop/chapter.md` hands over its own automated tool by name.

**1.2** **The chapter takes both and invents nothing.** A closing chapter that introduced a fresh case would be starting rather than finishing.

**1.3** **Case 1 is the water anchor's thirteenth and final appearance**, and the manuscript says so. Chapter 16 set the anchor aside deliberately; this chapter brings it back in order to criticise Chapter 12's own output.

**1.4** **Chapter 12 invited the criticism in its own text**: "those numbers are arguable, and being arguable is the property that matters."

### 2. The permitted machinery is declined

**2.1 This clause needs author attention.**

**2.2** `README.md`'s Chapter 17 block is the only chapter block in the book with permissive phrasing: "Concept-level monitoring machinery **may** include common-cause versus special-cause variation and control-chart reasoning **where appropriate**."

**2.3** **The chapter takes the distinction and refuses the technique.** The governed core competence names "distinguish signal from ordinary variation", which is the distinction. Control charts are one apparatus for applying it.

**2.4** **What is refused, specifically:** centre lines, control limits, run rules, chart types, sampling plans, and every named chart.

**2.5** **The manuscript says the architecture permitted more and explains why it did not use it**, so that the omission reads as a decision rather than a gap.

**2.6** If the author disagrees, the material is a section rather than a rewrite — but adding it would make this the only chapter in the book to teach a technique it does not use on its own case.

### 3. Signal, ordinary variation, and the finding that a threshold can be a timer

**3.1** The distinction and its attribution to Shewhart come from [@sumanprajapati2018control, p. 1], **as reported at** that review; Shewhart (1931) was not obtained.

**3.2** **The consequence is the book's own and is stated as such.** A threshold is only a trigger if it sits outside the range of ordinary variation. **A threshold set inside that range is a timer**, firing at a rate that is a fact about the process rather than about the world.

**3.3** The case demonstrates it with arithmetic: one limb of Chapter 12's signpost sits 2.12 standard deviations above its baseline mean and never fired in seven baseline years; the other fires on a value that occurred once in those seven years, which is **2.1 expected firings over the plan's fifteen-year horizon from baseline variation alone.**

**3.4** **The material for this criticism has been in the book since Chapter 8**, and the case shows that nobody applied it. The manuscript makes that point about the utility and about itself.

### 4. Deployment is a repeated act

**4.1** Taught from [@nasa2024models, p. 87]: "Each application of the M&S restarts the M&S use/operation with an assessment of permissible uses against the needs of that specific proposed use."

**4.2** **`permissible use` is a property of a pairing** — a model with a proposed application. **Fourth appearance of the relation-not-property shape**, after `validity` (Chapter 3), `transportability` (Chapter 9), and `observability` (Chapter 14). Named in prose, once.

**4.3** `placarding` is taken from the same page as the third option between refusing a use and permitting it silently.

**4.4** **Revision triggers are broader than Chapter 12's signposts.** [@nasa2024models, p. 18] requires the record to be "re-established as a result of any changes to either the RWS or the M&S" — the world changing **or** the model changing. Chapter 12's signposts watch only the first.

**4.5** **`retirement` is registered** because [@nasa2024models, p. 39] requires a plan for it at the same level as acquisition, and because **this book has not mentioned it in sixteen chapters.** The chapter closes on it.

### 5. Diagnosis by stage, and the counterpart of Chapter 16

**5.1** **Chapter 16 routes forward from a problem. Chapter 17 routes backward from a symptom.** Same fifteen categories, opposite directions, and the manuscript says so once.

**5.2** **A failure is diagnosed where it entered, not where it was noticed.** In the chapter's case the symptom appears at Chapter 13 and the failure entered at Chapter 4 — nine stages and eighteen months apart.

**5.3** **The central claim follows**: monitoring observes outputs, so it detects failures that change outputs and cannot detect failures in what the thing was built to represent.

**5.4** The chapter carries a table of which stages are visible to monitoring and which are not. **The early stages are invisible and the late ones are visible**, which is the reverse of where attention usually goes.

### 6. `tampering` — named in governed text, and unsourced

**6.1 This clause needs author attention.**

**6.2** `README.md`'s Chapter 17 core competence names "recognize drift and **tampering**". **No source for the term was obtained**; Deming was sought twice.

**6.3** **What is missing is a name, not a claim.** The mechanism has been sourced since Chapter 13: decision-makers "continue to intervene to correct apparent discrepancies... even after sufficient corrective actions have been taken to restore equilibrium" [@sterman2006evidence, p. 508]. **Tampering is that mechanism applied to a process that was not in trouble.**

**6.4** **This is therefore not a new instance of the demonstrate-because-unsourced disposition**, which `decisions/README.md` puts on notice and which concerns *practices taught with nothing behind them*. The practice here is Chapter 13's and is sourced.

**6.5** It is registered as **the book's own controlled term**, built on Chapter 13, and flagged because the word is in governed text.

**6.6** **And it makes clause 3 operational.** Knowing whether a value is a signal or ordinary variation is what tells you whether to act at all; acting on ordinary variation is how a stable process is made worse by somebody trying to help.

### 7. Two sources reused, nothing new claimed

**7.1** `perdomo2020performative`, read for Chapter 15 and **cited by section**, supplies drift caused by deployment. Chapter 15's cautions stand.

**7.2** `gneiting2007scoring`, read for Chapter 6, supplies calibration as a standing monitoring instrument. **Chapter 6's locators and cautions stand unchanged**, and the use is one sentence.

### 8. The pagination exception is not extended

**8.1** `0022` clause 8 proposed a bounded exception and `0023` clause 6 applied it a second time.

**8.2** **Chapter 17 needs no exception.** `nasa2024models` has pagination verifiable against its own table of contents at six entries; `sumanprajapati2018control` carries printed page numbers in its running heads.

**8.3** **The one source cited by section — `perdomo2020performative` — is the same source `0022` clause 8 was written for**, reused rather than newly excepted.

**8.4** **The count of exceptions therefore remains at two**, and one source was declined in this chapter's research on ordinary grey-literature quality rather than on pagination.

### 9. Vocabulary

**9.1** Introduced here: `monitoring`, `ordinary variation`, `signal`, `drift`, `tampering`, `revision trigger`, `permissible use`, `retirement`.

**9.2** **Six of the eight are the book's own or extend its own.**

**9.3** **No collision requiring announcement.** The second chapter in a row with none.

**9.4** The registry's one remaining `TODO` — `utility`, belonging to the drafted Chapter 11 — **is untouched, and after this chapter there is no later chapter to close it.** It now stands as an open item against a finished draft.

### 10. How the book ends

**10.1 This clause needs author attention.**

**10.2** This is the last chapter, and its final section is the book's final section.

**10.3** **It closes on what has not been established**, not on what has. Specifically: that no pilot data exists for any exercise in the book; that Gate 1 has been open since Chapter 1 and is now fourteen chapters deep; that sixteen decision records remain unadjudicated; and that the book's own claims about transfer are, correctly, nil.

**10.4** **And it closes on retirement** — the one item in [@nasa2024models, p. 39]'s five-verb plan that nothing in this book has discussed, which is a fair note for a last page.

**10.5** **What it does not do is congratulate the reader.** Chapter 16's `../decisions/0023` clause 5.4 already forbade a transfer claim, and the last chapter is where the temptation is greatest.

### 11. What Chapter 17 does not do

- Teach control charts, control limits, run rules, chart types, or sampling plans.
- Teach drift-detection methods: no distribution-shift tests, no change-point detection, no CUSUM, no sequential analysis.
- Teach governance or assurance frameworks. `fda2023credibility`, `asme2025credibility`, and `nrc2012reliability` were **not re-read**.
- Teach machine-learning monitoring, for the reason `README.md` gives about AI in this book.
- Teach reliability engineering, condition monitoring, or maintenance scheduling.
- Introduce a new case, or a new body of machinery, or any notation.
- Re-teach Chapter 5's model checking, which the canon already records as the same activity earlier.
- Claim that this book produces transfer, or that the reader has acquired anything by reading.
- Claim anything about Shewhart (1931) beyond what the reporting review states.

## Sources promoted

`sumanprajapati2018control` is new to `references.bib`. `nasa2024models` is upgraded from four Chapter 1 locators to a substantial reading at pp. 12, 18, 30, 39, and 86–88, with its pagination established against the standard's own contents.

## Known gaps carried forward

1. **Shewhart (1931) not obtained**; the common-cause distinction is used as reported at a 2018 review.
2. **No source for `tampering`**, which is in governed text — clause 6.
3. **`sumanprajapati2018control` read at one page of twenty-one**, and used for two claims.
4. **`nasa2024models` read at seven pages of eighty-eight**; nothing claimed about its assurance architecture, criticality assessment, or credibility scales.
5. **No pilot data exists for any transfer form in this book**, including this chapter's.
6. **The case is the water anchor's thirteenth and final appearance**, and Gate 1 remains open across all thirteen.
7. **`utility` remains open in the registry** and there is no later chapter to close it.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields.

**Clause 2 declines machinery the architecture permits**, which is the closest it comes, and the permission is discretionary by its own wording.
