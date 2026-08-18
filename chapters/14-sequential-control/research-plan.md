# Chapter 14 Bounded Research Plan

Status: working control. Governs what was researched before drafting and what was deliberately not.

Written after `readiness-audit.md` and executed against it.

## Standing rules carried forward

1. **Every locator must come from reading the document directly.** A fetch summary is a lead, not evidence. (Chapter 5.)
2. **Quote only prose that survives text extraction cleanly.** No quotation may contain a comparison symbol. (Chapters 7 and 8.)
3. **Cite the version whose pagination you can see.** (Chapter 9.)

**Rule 2 is strained in a new way in this chapter.** `sutton2018reinforcement` is typeset with an `ff` ligature that extracts as a stray character: *trade-off* becomes *trade-o↵*, *different* becomes *di↵erent*, *effective* becomes *e↵ective*. The substitution is deterministic and unambiguous, unlike the Greenland case that produced the rule — but the rule as adopted is strict, and **no quotation taken from this source contains an `ff`**. Several excellent sentences were left unquoted for this reason and are paraphrased instead, with the paraphrase declared.

## What this chapter needed and did not have

| Cluster | Source | State before this chapter |
|---|---|---|
| Policies; exploration versus exploitation | `sutton2018reinforcement` | **not in bibliography** |
| Observability | `astrom2008feedback` | read at pp. 1–4, 17–24, 27–34, 98–104; **the observability chapter unread** |
| Structural identifiability | `wieland2021identifiability` | **not in bibliography**; the term registered as `TODO` since Chapter 1 |
| Practical identifiability | same | **not anticipated by the architecture at all** |
| Information acquisition | `colyvan2016voi` | in bibliography from Chapter 11; not re-read |
| Control | `astrom2008feedback` | pp. 3–4 verified during Chapter 13 research |

## What was obtained, and how

**`sutton2018reinforcement`** — *Reinforcement Learning: An Introduction*, second edition, MIT Press, © 2018, 2020, obtained as the publisher-licensed PDF. Printed page numbers appear in the running heads; printed page equals PDF page minus 22, calibrated against the head on printed p. 2. Read at pp. 2–3, 25–28, and 58.

**`wieland2021identifiability`** — *Current Opinion in Systems Biology* 25:60–69, obtained as the typeset article with printed page numbers in the running heads. Printed page equals PDF page plus 59. Read at pp. 60–64.

**`astrom2008feedback`** — the first-edition PDF already in use since Chapter 2, extended to pp. 201–202. Printed page equals PDF page minus 12.

**`colyvan2016voi`** — not re-read. Chapter 11 verified its locators and Chapter 14 reuses the ceiling argument rather than the machinery.

## Bounds — what was deliberately not researched

`README.md` states this chapter's exclusions itself, which no other chapter's block does. Each was honoured and each is recorded here with what was read up to the line.

**Dynamic programming.** Not researched. `sutton2018reinforcement` Chapter 4 was not opened. The chapter teaches that a policy is the object of choice and does not teach how to compute an optimal one.

**Filtering.** Not researched. `astrom2008feedback` §7.2 (state estimation) and §7.4 (Kalman filtering) were not read. The chapter teaches that observability determines whether the state *could* be recovered and stops before recovering it.

**LQR and MPC.** Not researched at all.

**POMDPs.** Not researched. The chapter's observability failure is described in words and no partially-observed formalism is introduced.

**Reinforcement-learning algorithms.** `sutton2018reinforcement` §2.2 onward was read only far enough to establish where the line falls. No action-value method, no epsilon-greedy update rule, no bandit algorithm is taught. The k-armed bandit is **named once** as the setting in which the dilemma was studied.

**Additionally not researched:** reachability and state feedback (`astrom2008feedback` Chapter 6); the observability rank test at pp. 202–203; profile-likelihood methods (`wieland2021identifiability` pp. 62–64 read for the definitions, not for the methods); Bayesian sequential design; optimal stopping.

## Sources considered and declined

**Bellman and Åström (1970), "On structural identifiability", *Mathematical Biosciences* 7:329–339.** The origin of the term, confirmed from `astrom2008feedback`'s own bibliography at printed p. 378. **Not obtained** — paywalled, and no route to a copy with checkable pagination was found. `wieland2021identifiability` is used instead and is a review rather than the primary source. **Recorded as this chapter's principal source gap.**

**Villaverde, Barreiro and Papachristodoulou (2016), "Structural Identifiability of Dynamic Systems Biology Models", *PLoS Computational Biology*.** Obtained and read at the abstract. **Declined** in favour of `wieland2021identifiability`, which carries printed page numbers in its running heads and makes the structural/practical distinction the chapter needs. Recorded rather than left silent.

**Howard's value-of-information papers.** Unobtained since Chapter 11 and not re-attempted.

**Bertsekas, *Dynamic Programming and Optimal Control*.** Not sought; `README.md` excludes the material.

## Known gaps carried forward

1. **Bellman and Åström (1970) not obtained** — the chapter teaches structural identifiability from a 2021 review rather than from the paper that named it. This is the chapter's largest source gap.
2. **`wieland2021identifiability` is written for systems biology**, and the book applies its distinction across domains as its own synthesis. Stated in the manuscript.
3. **`sutton2018reinforcement` read at five pages of about 550.** Nothing is claimed about reinforcement learning as a field beyond what those pages state.
4. **`astrom2008feedback` observability read at pp. 201–202 only**; the rank test and the observer construction are unread.
5. **The `ff`-ligature extraction problem** in `sutton2018reinforcement`, which cost several quotable sentences.
6. **`practical identifiability` was not anticipated by `README.md`'s Chapter 14 block.** It is registered on the strength of the source and is flagged for author review, because the governed core competence does not name it.
7. The **Chapter 14 case is the water anchor's eleventh recurrence**, and Chapter 1's Gate 1 remains open.
