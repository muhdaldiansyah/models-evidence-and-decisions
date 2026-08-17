# Research 03 — Abstraction, Idealization, Aggregation, Grain, and Scale

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision. Written under the no-write boundary in `research-plan.md` §12.

Cluster R03 of `research-plan.md` §6. Researched 2026-08-18, after R04 per the sequencing note in §9.

Sources inspected: `levins1966strategy` (primary, page-verified), `weisberg2007idealization`, `frigg2025models`, `machamer2000mechanisms`, `astrom2008feedback`.

## 1. Q1 — Abstraction versus idealization

### The distinction, and who owns it

Two independent sources report the same distinction, and both attribute it to the same third author.

`weisberg2007idealization`, footnote 14: "Martin Jones has cogently argued that **abstraction is best seen as a kind of omission, whereas idealization is the assertion of falsehood**. Cartwright's and Jones' proposal is perfectly reasonable — omission and distortion are distinguishable practices."

`frigg2025models` §1: "Jones (2005) and Godfrey-Smith (2009) offer an analysis of abstraction in terms of truth: while an abstraction remains silent about certain features … it does not say anything false."

So the distinction is:

| | What it does | Truth status |
|---|---|---|
| **Abstraction** | leaves a feature out | says nothing about it — silence |
| **Idealization** | puts a false feature in | asserts something untrue |

This is clean, teachable, and checkable by the reader: *did I leave it out, or did I put in something I know is wrong?*

### Where the sources are contested

Weisberg reports the distinction and then declines to adopt it: he argues for pluralism and says he sees "no reason why we should not treat minimalist modeling as a form of idealization." `frigg2025models` §1 separately records Aristotelian idealization as "stripping away … all properties from a concrete object that we believe are not relevant to the problem" — which is *omission* filed under the heading *idealization*.

**Finding: the terms overlap in the literature, and the boundary is not settled.** The omission/distortion cut is defensible and useful, but it is one position, not a consensus.

## 2. Q2 — Does the core chapter need both terms?

R03's recommendation is **yes, but asymmetrically.**

Argument for both: the two practices carry different obligations. An omission can be defended by showing the feature does not bear on the question. A distortion cannot — it must be defended by showing the error it introduces is tolerable for the use, which is a strictly harder argument. A reader who cannot tell them apart cannot tell which defence they owe.

Argument against both: terminology budget, and the literature's own overlap.

The asymmetry that resolves it: **`abstraction` earns controlled-vocabulary status; `idealization` earns a named contrast but not a full apparatus.** The reader needs to recognise when they have asserted something false, and to know that this is a different and heavier commitment. They do not need Galilean/minimalist/multiple-models taxonomy — that is depth-curriculum material.

**Corroborating distinction, from a different tradition.** `machamer2000mechanisms` p. 16 supplies a second cut that must not be confused with the first: "Degrees of abstraction should not be confused with degrees of generality or scope. Abstraction is an issue of the amount of detail included in the description of one or more mechanism instances. The generality of a schema is the scope (small or large) of the domain in which it can be instantiated."

So there are three separable dials, not one:

1. **how much detail** (abstraction);
2. **whether anything false was asserted** (idealization);
3. **how wide a domain it covers** (generality).

A reader who conflates these will think "simpler" and "more general" are the same move. They are not. This is the sharpest correction R03 produces.

## 3. Q3 — Aggregation and coarse-graining at representation level

### What was found

`machamer2000mechanisms` p. 16 gives the constructive procedure: "Abstractions may be constructed by taking an exemplary case or instance and removing detail. For example, a constant can be made into a variable."

`astrom2008feedback` p. 34 gives the grain decision directly: "A key issue in modeling is to decide how accurately this storage has to be represented."

`levins1966strategy` p. 421 gives the reason the maximal option is not available even in principle: a "faithful, one-to-one reflection" fails because parameters are unmeasurable, equations insoluble, and — decisively for this book — "Even if soluble, the result expressed in the form of quotients of sums of products of parameters would have no meaning for us."

That third reason is the one Chapter 2 should lead with. **A fully detailed model can fail not by being wrong but by being uninterpretable.**

### What was NOT found — recorded gap

No source inspected in this pass defines **aggregation** as a representational operation, nor supplies criteria for when lumping heterogeneous entities into one aggregate is legitimate.

Sources considered and deliberately not used:

- Robinson's ecological-fallacy literature concerns inference from aggregate *data* to individuals. That is Chapter 4 (observation processes) and Chapter 9 (transport), not Chapter 2. Citing it here would create exactly the collapse the readiness audit lists as high-risk #6.
- Levins's coarse-/fine-grained environment vocabulary at p. 424 is about environmental heterogeneity relative to an organism, not about model resolution. Same word, different concept.

### Recommended disposition of the gap

Chapter 2 should teach aggregation failure **by worked demonstration in its own case rather than by citation.** If the chapter's anchor shows, arithmetically, that an aggregate hides a difference that matters to the stated decision, the reader can verify it on the page. A self-evidencing demonstration needs no source, and inventing one would be worse than not having one.

This is a legitimate answer to a sourcing gap, but it must be a deliberate choice, so it is flagged in §8.

## 4. Q4 — Vocabulary for grain and resolution

Candidate terms and their evidenced status:

| Term | Status in inspected sources | Recommendation |
|---|---|---|
| **abstraction** | defined, contrasted with generality (`machamer2000mechanisms` p. 16) | **adopt** as controlled vocabulary |
| **idealization** | defined, but contested boundary (§1) | adopt as **named contrast only** |
| **grain** | used by `levins1966strategy` p. 424 in a *different* sense | usable as ordinary language; **do not cite Levins for it** |
| **resolution** | not defined in any inspected source | ordinary language only |
| **fidelity** | used by `astrom2008feedback` pp. 27, 32 for level of model detail | usable, engineering-flavoured |
| **level** | not defined; heavily overloaded (level of detail, organisational level, level of a variable) | **avoid** |
| **scale** | not defined in any inspected source | see §5 |
| **coarse-graining** | not defined in any inspected source | **avoid**; physics-specific |
| **aggregation** | not defined at representation level (§3) | needed, but unsourced |
| **generality / scope** | defined (`machamer2000mechanisms` p. 16) | **adopt**, precisely to keep it apart from abstraction |

The strongest evidenced pair is **abstraction versus generality**. The weakest area is **scale**, which no inspected source defines.

## 5. Q5 — How scale changes what a model can answer

### What is evidenced

`astrom2008feedback` p. 29: "Adding the input makes the model richer and allows new questions to be posed." Changing what is represented changes the answerable question set — stated plainly by an engineering text.

`astrom2008feedback` p. 27: "there may be multiple models for a single dynamical system, with different levels of fidelity depending on the phenomena of interest."

`levins1966strategy` p. 423 supplies the reader-facing image, and it is the best teaching device found in this cluster:

> doubt about whether a result depends on essentials or on simplifying details "does not arise in the more familiar models, such as the geographic map, where we all know that contiguity on the map implies contiguity in reality, relative distances on the map correspond to relative distances in reality, but color is arbitrary and a microscopic view of the map would only show the fibers of the paper on which it is printed. But, in the mathematical models of population biology, it is not always obvious when we are looking at too high a magnification."

Two lessons in one passage: some features of a representation carry meaning and others are artifacts; and on a map you know which is which, while in a model you often do not.

### What is not evidenced

No inspected source treats **spatial, temporal, organisational, and population scale as distinct axes**. That fourfold split is currently the book's own organising device, not a sourced taxonomy, and must be labelled accordingly if used.

## 6. Q6 — Failure modes from aggregating heterogeneous things

Under-sourced, as recorded in §3. What *is* available:

- `levins1966strategy` pp. 421–422: legitimacy of a simplification "depends not only on the reality to be described but also on the state of the science" — and the Haldane/Fisher/Wright case shows the same simplification passing for one question and failing for another;
- `machamer2000mechanisms` p. 3: an unspecifiable activity "leaves an explanatory gap" — the mechanism-side analogue of an aggregate that hides the step that matters.

Chapter 2 can therefore say, with support, that an aggregation is defensible only relative to a question, and can demonstrate a failure arithmetically. It cannot present a sourced taxonomy of aggregation errors.

## 7. Cautions — claims the manuscript must NOT make

1. Do not present omission/distortion as settled. Weisberg reports it and declines it; Aristotelian idealization is omission filed under idealization.
2. Do not attribute the distinction to Weisberg or to Frigg and Hartmann. It is Jones's (2005); Godfrey-Smith (2009) is also cited by SEP.
3. Do not cite `levins1966strategy` p. 424 for `grain` in the Chapter 2 sense. Different concept, same word.
4. Do not present the generality/realism/precision trade-off as proven. It is Levins's influential strategy argument and is disputed in the later literature — literature which was **not** inspected and must not be cited unread.
5. Do not import the ecological-fallacy literature. It concerns inference from aggregate data, which is Chapters 4 and 9.
6. Do not use `level` as controlled vocabulary. It is overloaded past repair at this depth.
7. Do not claim a sourced taxonomy of aggregation errors, or of scale axes. Neither exists in the inspected evidence.
8. Do not quote "our truth is the intersection of independent lies" as general epistemology. It is a claim about robust theorems across models sharing a common assumption.

## 8. Verdict on the stop condition

`research-plan.md` §6 requires the author to be able to choose among abstraction, idealization, aggregation, coarse-graining, scale, level, grain, resolution.

**Met, with one flagged gap.** The evidence supports:

- **adopt as controlled vocabulary:** `abstraction`, `generality`/`scope`;
- **adopt as named contrast only:** `idealization`;
- **use as ordinary careful language:** `grain`, `resolution`, `fidelity`, `aggregation`, `scale`;
- **avoid:** `level`, `coarse-graining`.

The gap is `aggregation`, which Chapter 2 needs and which no inspected source defines representationally. §3 proposes teaching it by self-evidencing demonstration.

## 9. Unresolved author decisions raised by R03

1. Adopt the omission/distortion cut as the reader-facing distinction, knowing it is one position rather than consensus?
2. Is `idealization` named at all, or is the idea taught as "putting in something you know is false"?
3. Is the abstraction-versus-generality separation taught explicitly? It is the best-evidenced correction available, but it costs a paragraph the reader may not expect.
4. Accept the demonstrate-don't-cite disposition for aggregation, or reopen R03 for an aggregation source?
5. Are the four scale axes used as an organising device, and if so, are they labelled as the book's own device rather than established taxonomy?
6. Does the map analogy from `levins1966strategy` p. 423 become a recurring chapter device, or a single illustration?

Question 4 is the one that changes the chapter's evidence posture and should be decided first.
