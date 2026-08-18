# Research 03 — Reliability, Error, Accuracy, Trueness, Precision

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision.

Cluster R03 of `research-plan.md` §6. Research conducted 2026-08-18.

Sources inspected: `jcgm2012vim` §§2.13–2.16 (consulted through the official interactive VIM), `adcock2001validity` pp. 531–532.

## 1. Q1–Q2 — What the standard actually says

The VIM entries are unusually blunt, and the bluntness is what makes them useful to a teaching chapter.

| Term | VIM definition | Is it a number? |
|---|---|---|
| **accuracy** (§2.13) | "closeness of agreement between a measured quantity value and a true quantity value of a measurand" | **No.** Note 1: accuracy "is not a quantity and is not given a numerical quantity value" |
| **trueness** (§2.14) | "closeness of agreement between the average of an infinite number of replicate measured quantity values and a reference quantity value" | **No.** Not a quantity, not expressed numerically; ISO 5725 supplies measures |
| **precision** (§2.15) | "closeness of agreement between indications or measured quantity values obtained by replicate measurements on the same or similar objects under specified conditions" | **Yes.** Expressed by standard deviation, variance, or coefficient of variation |
| **error** (§2.16) | "measured quantity value minus a reference quantity value" | Yes, where a reference value exists |

### The three prohibitions, stated by the standard itself

- §2.13 Note 2: "measurement accuracy" should not be used for measurement trueness, nor for measurement precision, "although it does relate to both these concepts".
- §2.14: "measurement accuracy" should not be used for trueness.
- §2.15 Note 4: "measurement precision" is sometimes **erroneously** used to mean measurement accuracy.

A standards body writing three separate prohibitions against the same family of confusions is itself evidence that the confusion is common. Chapter 3 may point at the prohibitions; it may not cite the VIM for a claim about how often practitioners get it wrong.

### The asymmetry worth teaching

Precision is the one you can put a number on. Accuracy and trueness are not.

This is a small fact with a large consequence: **the reportable quantity is not the one you care about.** An instrument's specification sheet will quote a precision figure because precision is quotable. Nothing about that figure tells you whether the readings are centred on the right value.

### Trueness and error

§2.14: trueness is **inversely related to systematic measurement error** and is **not related to random measurement error**.

§2.16 Note 1 makes error's knowability conditional: it is known when a single reference value exists — through calibration against a standard of negligible uncertainty, or through a conventional value — and unknown when the measurand is taken to have a unique true value that is not available.

§2.16 Note 2: measurement error "should not be confused with production error or mistake". Useful for a general reader, who will otherwise hear "error" as "someone made a mistake".

## 2. Q3 — How the two vocabularies relate

`adcock2001validity` p. 531 gives the social-science version in one sentence: "Measurement error may be systematic—in which case it is called bias—or random. Random error, which occurs when repeated applications of a given measurement procedure yield inconsistent results, is conventionally labeled a problem of reliability."

Lining the two up:

| Idea | Metrology (`jcgm2012vim`) | Social science (`adcock2001validity`) |
|---|---|---|
| Consistent offset in one direction | systematic measurement error; low trueness | bias |
| Scatter on repetition | random measurement error; low precision | a problem of reliability |
| Reference against which offset is defined | reference quantity value / true quantity value | the systematized concept |

The first two rows map well. **The third does not**, and it is the chapter's central sourcing hazard.

Metrology defines error against a reference quantity value that a calibration chain can in principle deliver. For *adequate service pressure* or *housing need*, no such reference exists. What plays the role of the reference is a chosen systematized concept — and a choice is not a standard.

**Chapter 3 must teach both and must not merge them.** Where a reference standard exists, the metrology vocabulary applies cleanly. Where the concept is chosen, "error" language should be used with visible care, because there is nothing to subtract from.

## 3. Q4 — What more measurements do and do not fix

Directly derivable from the verified entries, and the single most useful practical result in this cluster.

**More measurements improve precision.** Precision is agreement among replicates (§2.15), so averaging more replicates tightens it.

**More measurements do nothing for trueness.** Trueness is defined as closeness of *the average of an infinite number of replicates* to a reference value (§2.14). If that average is off, taking more readings converges on the wrong number faster. §2.14's statement that trueness is inversely related to systematic error and unrelated to random error is exactly this point.

This is why Chapter 1's water case works so well here. The dashboard read **10.8 ML**; the independent check found **9.9 ML**. That 0.9 ML gap was a systematic offset from a transmitter reading high. No number of dashboard readings would have revealed it, because every one of them would have been high by about the same amount.

### The reliability trap

Combining the two vocabularies gives the reader a checkable warning: an instrument can be **highly repeatable and consistently wrong**. In metrology terms, high precision and poor trueness. In social-science terms, reliable and biased.

`adcock2001validity` p. 532 records that methodologists differ on how reliability relates to validity — on one account "unreliable scores may still be correct 'on average' and in this sense valid"; on another, reliability is "a necessary but not sufficient condition of measurement validity". Chapter 3 should present the disagreement rather than pick a side, because the reader's practical lesson — reliable does not mean valid — survives either account.

## 4. Q5 — Which terms a core reader needs

Proposal, with reasoning.

| Term | Recommendation | Why |
|---|---|---|
| **precision** | teach | reportable, ubiquitous on specification sheets, and routinely misread as accuracy |
| **trueness** | teach | it is the thing precision is mistaken for; without it the confusion cannot be named |
| **accuracy** | teach as the **pair**, not as a third thing | the VIM treats it as relating to both; teaching it as separate invites the conflation |
| **systematic error / bias** | teach | the operative concept, and the one with decision consequences |
| **random error** | teach | needed to make the contrast |
| **reliability** | teach | the reader will meet the word constantly |
| **measurement error** | teach, with the reference-value caveat | §2.16's conditional knowability matters |
| **calibration** | teach at recognition depth only | needed to explain how a systematic offset is found; full traceability is depth curriculum |
| **repeatability / reproducibility** | do not teach | ISO 5725 conditions; specialist |
| **measurement uncertainty** | do not teach | Chapter 8 |
| **measurand** | signpost only | see R01 |

## 5. Cautions — claims the manuscript must NOT make

1. Do not report accuracy or trueness as numbers. VIM §§2.13, 2.14 forbid it.
2. Do not say precision and accuracy are "basically the same". §2.15 Note 4 calls that erroneous.
3. Do not present measurement error as always knowable. §2.16 Note 1 conditions it on a reference value.
4. Do not let "error" be heard as "mistake". §2.16 Note 2.
5. Do not apply the metrology vocabulary to chosen constructs without flagging that there is no reference standard behind it.
6. Do not resolve the reliability/validity disagreement recorded at `adcock2001validity` p. 532.
7. Do not cite the VIM for how frequently practitioners confuse these terms.
8. Do not teach uncertainty evaluation, coverage intervals, ISO 5725 statistics, or traceability chains.

## 6. Verdict on the stop condition

`research-plan.md` §6 requires that the controlled vocabulary be choosable and the "precise but wrong" demonstration be sourceable.

**Met on both.** The vocabulary set is proposed in §4. The demonstration is sourced from §2.14 (trueness unrelated to random error) plus §2.15 (precision is what replication improves), and is already instantiated in the book's own Chapter 1 case facts.

## 7. Unresolved author decisions

1. Are all three of accuracy, trueness, and precision named, or only precision and trueness with accuracy taught as their combination?
2. Is `bias` or `systematic error` the preferred term, given the two traditions use different words?
3. Is `calibration` reader-facing?
4. Is the reliability/validity disagreement shown to the reader, or is only the practical lesson given?
5. How visibly does the chapter mark the no-reference-standard problem for chosen constructs — a caution, or a structural feature of the chapter?

Decision 5 is the consequential one. Treated as a caution it will be forgotten; treated structurally it shapes the anchor case.
