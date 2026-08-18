# Chapter 15 Bounded Research Plan

Status: working control. Governs what was researched before drafting and what was deliberately not.

Written after `readiness-audit.md` and executed against it.

## Standing rules carried forward

1. **Every locator must come from reading the document directly.** A fetch summary is a lead, not evidence. (Chapter 5.)
2. **Quote only prose that survives text extraction cleanly.** No quotation may contain a comparison symbol. (Chapters 7 and 8.)
3. **Cite the version whose pagination you can see.** (Chapter 9.)

**Rule 3 forces a new device in this chapter.** `perdomo2020performative` was obtained as the official PMLR PDF, and **it carries no printed page numbers**. Chapter 9 met this before and *declined* the source; that is not available here, because `../../decisions/0007` assigns this source to Chapter 15 by name and it is already in the bibliography. The chapter therefore **cites it by numbered section and by Abstract**, which are visible and checkable, and records the device. See `../../decisions/0022` clause 8.

**Rule 2 is strained again, differently.** `perdomo2020performative` renders `fi` and `ffi` as ligatures that extract as single characters: *influence* becomes *inﬂuence*, *sufficient* becomes *sufﬁcient*. **No quotation taken from that source contains an `fi`**, and several good sentences were left unquoted for it.

## What this chapter needed and did not have

| Cluster | Source | State before this chapter |
|---|---|---|
| Strategic dependence; equilibrium as consistency | `osborne2004game` | **not in bibliography** |
| Goodhart-type failures; metric gaming | `manheim2019goodhart` | **not in bibliography** |
| Endogenous response; performativity | `perdomo2020performative` | in bibliography since Chapter 1, **read at abstract level only** |
| Goodhart's law, Campbell's law, Lucas critique — the originals | — | **none obtained; see below** |
| Principal-agent; information asymmetry | — | **none obtained; see below** |

## What was obtained, and how

**`osborne2004game`** — the author-hosted draft of Chapter 2, *Nash Equilibrium: Theory*, from *An Introduction to Game Theory* (Oxford University Press, 2004). Printed page numbers appear in the running heads and feet; **printed page equals PDF page plus 10**, calibrated against the footer on printed p. 11. Read at pp. 11, 19–20.

**`manheim2019goodhart`** — "Categorizing Variants of Goodhart's Law", arXiv:1803.04585v4, 24 February 2019. Printed page numbers appear in the footers; **printed page equals PDF page**. Read at pp. 1–2 and §§1–4.

**`perdomo2020performative`** — the official PMLR PDF, *Proceedings of the 37th International Conference on Machine Learning*, PMLR 119. Read at the Abstract and §1. **Cited by section; see above.**

## Three primary sources named in governed text and not obtained

`README.md`'s Chapter 15 core competence names **Goodhart-type failures**, **Campbell's law**, and the **Lucas critique**. All three originals were sought and none was obtained.

**Goodhart (1975), "Problems of Monetary Management: The U.K. Experience".** Confirmed to exist from `manheim2019goodhart`'s reference [1], which gives the full citation. Not obtainable.

**Campbell (1979), "Assessing the impact of planned social change", *Evaluation and Program Planning* 2(1): 67–90.** Four routes attempted, including two repositories advertising full text; all returned HTML or 404.

**Lucas (1976), "Econometric Policy Evaluation: A Critique".** A scanned PDF was obtained and **contains no extractable text** — it is an unOCR'd image. Four further routes returned 404 or 403.

**All three are used through the "as reported at" device**, which this book has used since Chapter 6 — Brier through `gneiting2007scoring`, Matrixx through `greenland2016misinterpretations`, Russell through `deaton2016rct`, Keeney through `bradley2016structured`, Savage and Dewar through `lempert2003shaping`.

**Three in one chapter is more than any previous chapter has needed**, and it is recorded as this chapter's principal gap.

## Two terms in governed text with no source at all

`principal-agent relationships` and `information asymmetry` are named in the governed core competence.

**Research was reopened rather than precedent invoked**, which is what `../../decisions/README.md` requires of any chapter reaching for the demonstrate-because-unsourced disposition. Four acquisition attempts were made across three routes: Holmström (1979) via JSTOR, Akerlof (1970) via a course repository, and the Nobel Committee's 2016 scientific background on contract theory. **The first two were paywalled; the third was obtained and its text extraction is unusable** — search terms present in the document return nothing, and page footers extract as private-use characters, so nothing in it can be quoted under rule 2.

**The reopening failed.** `../../decisions/0022` clause 9 records this as a **candidate fifth instance** of the disposition, states that the standing instruction was followed rather than the precedent invoked, keeps the treatment to about one page, and refers the question to the author rather than resolving it.

## Bounds — what was deliberately not researched

**No mechanism design.** `../../decisions/0007` defers it and nothing was read on it.

**No formal game theory beyond the strategic form.** `osborne2004game` §§2.7–2.10 — examples of Nash equilibrium, best response functions, dominated actions, symmetric equilibria — were **not read**. No mixed strategies, no extensive form, no subgame perfection, no repeated games, no bargaining.

**No contract theory.** No optimal contracts, no incentive-compatibility constraints, no participation constraints.

**No performative-prediction mathematics.** `perdomo2020performative` §§2 onward — the distribution map, repeated risk minimisation, repeated gradient descent, the convergence theorems — were **not read** beyond noting that they exist.

**No Goodhart mathematics.** `manheim2019goodhart`'s formal treatments within each of its four sections were read only far enough to state what each mechanism is.

**No auction theory, no voting theory, no social choice.**

## Sources considered and declined

**The Nobel Committee's 2016 scientific background on contract theory.** Obtained; **declined for unusable text extraction**. Recorded rather than left silent.

**Kerr (1975), "On the folly of rewarding A, while hoping for B".** The classic on incentive misalignment. Three routes attempted, all failed.

**Strathern (1997)**, source of the popular formulation of Goodhart's law. Not obtained; the chapter uses the original formulation as reported at `manheim2019goodhart` instead, which is closer to Goodhart.

**Sterman's policy-resistance material** (`sterman2002models`, `sterman2006evidence`), already read and used in Chapter 13. **Not reused here**, because Chapter 13 owns it and Chapter 15's subject is agents who respond to the rule *because it is the rule*, which policy resistance does not require.

## Known gaps carried forward

1. **Goodhart (1975), Campbell (1979), and Lucas (1976) all unobtained** — three "as reported at" uses in one chapter, the most in the book.
2. **No source for `principal-agent` or `information asymmetry`**, after a documented reopening. `../../decisions/0022` clause 9.
3. **`perdomo2020performative` has no printed pagination**, and is cited by section.
4. **`osborne2004game` is a draft chapter posted by the author**, not the published book. The text is the author's own and the pagination matches the book's, but it is a pre-publication draft and the source note says so.
5. **`manheim2019goodhart` is an arXiv preprint**, not peer-reviewed, and its own framing is oriented toward artificial-intelligence alignment. The book uses its taxonomy and not its framing.
6. **`perdomo2020performative` read at two of twelve pages**; nothing is claimed about its results.
7. **`osborne2004game` read at three pages of forty-two**; nothing is claimed about game theory beyond the strategic form and the definition of equilibrium.
8. The **Chapter 15 case is the water anchor's twelfth recurrence**, and Chapter 1's Gate 1 remains open.
