# Decision 0022: Chapter 15 Strategic Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

**Four clauses need author attention beyond the usual**, and one of them is a book-level governance matter rather than a chapter choice.

- **Clause 5** proposes the **fourth notation extension** in the book, and the first in four chapters.
- **Clause 7** records **three "as reported at" uses in one chapter**, all three for concepts named in governed text.
- **Clause 8** proposes a **bounded exception to the pagination rule** adopted in Chapter 9.
- **Clause 9** records a **candidate fifth instance of the demonstrate-because-unsourced disposition**, states that the standing instruction to reopen research was followed, records how the reopening failed, and refers the question to the author.

Evidence base: `../chapters/15-strategic-interaction/research-01-strategic-games-and-equilibrium.md`, `research-02-goodhart-mechanisms.md`, `research-03-endogenous-response.md`, `research-04-discriminator-and-examples.md`.

## Decision

Chapter 15's organizing claim is:

> A measured relationship is a fact about a world in which nobody was being measured for consequences — and once consequences attach, that relationship is not evidence about the new world but a relic of the old one.

### 1. Thirteen competences, one claim and a vocabulary

**1.1** `README.md`'s Chapter 15 core competence names **thirteen** things, the largest count in the book. Chapter 8 named eight, Chapter 13 nine, Chapter 14 seven.

**1.2** **They are not thirteen topics.** Seven — endogenous response, metric gaming, Goodhart-type failures, Campbell's law, the Lucas critique, manipulation of evidence, and performativity in its formal dress — are the organizing claim seen from different directions.

**1.3** The remaining six — strategic dependence, incentives, equilibrium as consistency, commitment, information asymmetry, principal-agent relationships, and delegation — are **the machinery for reasoning about why it happens**, taught as a working vocabulary with **one worked instance each on the chapter's own case**.

**1.4** **The manuscript says this to the reader**, so that a reader checking the chapter against the book's own architecture can see that nothing was dropped.

### 2. Strategic dependence and the strategic game

**2.1** Taught from [@osborne2004game, p. 11]: a strategic game is a model of interacting decision-makers, and the model "captures interaction between the players by allowing each player to be affected by the actions of all players, not only her own action."

**2.2** **This is what every chapter before Part IV assumed away**, and the manuscript says so once: the reservoir was affected by the utility's action and by nothing that had an opinion.

**2.3** The three ingredients are given, with emphasis on the third: preferences over **profiles**, not over one's own action alone.

### 3. Equilibrium as consistency, and the collision with Chapter 13

**3.1** `canon/terminology.md`'s `equilibrium` entry has recorded both senses since Chapter 1, with the instruction that they must not be conflated. Chapter 13 closed the dynamic sense. **Chapter 15 closes the strategic sense.**

**3.2** Taught from [@osborne2004game, p. 20]'s two components: each player chooses rationally given their belief, **and** every player's belief about the others is correct. **The second component is the whole of the phrase the governed competence uses.**

**3.3** The definition of Nash equilibrium is **paraphrased and not quoted**; it carries an asterisked profile and player subscripts. Third time the standing rule from Chapter 8 has cost the book a definition rather than a flourish, after Chapter 14's observability.

**3.4** The steady-state and social-norm readings are quoted, as is "expectations are coordinated".

**3.5** **The distinction is stated as a four-row table, once**, and the manuscript closes it with the book's own line: a pendulum has an equilibrium and has no beliefs.

**3.6** **An equilibrium is not a good outcome**, and the case's equilibrium is worse for both parties than the situation before anybody optimised anything.

**3.7 The source's own caution travels with the concept** [@osborne2004game, p. 20]: whether Nash equilibrium is appropriate "in any given situation is a matter of judgment". **Fourth time a source in this book has disqualified its own generality on the page that introduces it**, after `greenland2016misinterpretations`, `deaton2016rct`, and `sutton2018reinforcement`. Named in prose, once.

### 4. Goodhart-type failures, taught as four things

**4.1** Taught from [@manheim2019goodhart, p. 2]: Regressional, Extremal, Causal, Adversarial.

**4.2** **This is why the chapter needs four names rather than one.** *Gaming* covers only the fourth, and treating all four as gaming sends an organisation looking for bad actors when the first two need none.

**4.3** **Regressional Goodhart cannot be avoided** [@manheim2019goodhart, p. 2], and the manuscript connects it backwards: Chapter 3's score-is-not-the-construct plus Chapter 8's estimator properties, meeting selection.

**4.4** **The diagnostic sentence is [@manheim2019goodhart, p. 1]**: importance "depends on the amount of power directed towards optimizing the proxy". The failure is not caused by having a metric; it is caused by pushing on one, and it scales.

**4.5** All four are shown on the case, because the source says they usually occur together.

### 5. Notation — a two-player payoff table, proposed

**5.1** **This is the fourth notation extension in the book and the first since Decision 0018**, which permitted a decision table with one act per row and one inline tree. Decisions 0019, 0020, and 0021 each added nothing.

**5.2** **What is proposed:** a two-by-two table with one player's actions as rows, the other's as columns, and a pair of numbers in each cell. The convention is taken from [@osborne2004game, p. 19], Figure 19.1.

**5.3** **Why it is needed rather than convenient.** `strategic dependence` and `equilibrium as consistency` are both claims about how one party's payoff depends on another's action. In prose, the reader has to hold four outcomes and two orderings in mind at once. The table is the object the concept is about.

**5.4** **What is not proposed:** no payoff functions, no best-response notation, no mixed strategies, no extensive form, no solution concept beyond the paraphrased definition. **One table, four cells, in one section.**

**5.5** The notation sequence now spans **five records** — 0013 opens, 0014 extends, 0015 declines, 0018 extends, 0022 extends — and they must still be adjudicated in order.

### 6. Endogenous response and performativity

**6.1** Taught from [@perdomo2020performative, §1]: "the prediction causes a change in the distribution of the target."

**6.2** **The scope claim is quoted** [@perdomo2020performative, Abstract]: performativity "is a well-studied phenomenon in policy-making that has so far been neglected in supervised learning." Without it, a reader takes performativity for a machine-learning problem.

**6.3** **The calibration sentence connects to Chapter 6** [@perdomo2020performative, Abstract]: predictions calibrated "not against past outcomes, but against the future outcomes that manifest from acting on the prediction."

**6.4** **The retraining reframing is carried** [@perdomo2020performative, §1] — a model that keeps needing refitting may be a system converging rather than maintenance falling behind.

**6.5** **`performative` is flagged as colliding with its ordinary English sense**, once. This is a different kind of collision from the book's other six — it is technical-against-vernacular rather than technical-against-technical — and it is noted rather than counted among them.

**6.6 Performativity is not Chapter 13's policy resistance**, and the manuscript states the difference once: policy resistance needs no agent who knows the policy exists. **Chapter 13's sources are deliberately not reused here.**

### 7. Three unobtainable primary sources, all named in governed text

**7.1 This clause needs author attention.**

**7.2** `README.md`'s Chapter 15 core competence names **Goodhart-type failures**, **Campbell's law**, and the **Lucas critique**. **None of the three originals could be obtained**, after multiple documented attempts recorded in `research-plan.md`.

**7.3** Goodhart's law and Campbell's law are used **as reported at** [@manheim2019goodhart, p. 1 n.1 and p. 8 n.5], which quotes both verbatim with full references.

**7.4** **The Lucas critique is neither quoted nor obtained.** It is named at [@manheim2019goodhart, p. 1 n.1] as a closely related formulation and not stated there. **The chapter names it, states its content in the book's own words, and says plainly that it has not read Lucas (1976).** Nothing is attributed to Lucas beyond the existence of the critique.

**7.5** **Three "as reported at" uses in one chapter is more than any previous chapter has needed** — the book's earlier uses were one per chapter — and it is recorded as this chapter's principal source gap.

**7.6** [@manheim2019goodhart, p. 1 n.1]'s own caveat is carried into the manuscript: "the categories proposed do not match what was originally discussed."

### 8. A bounded exception to the pagination rule

**8.1 This clause needs author attention.**

**8.2** The standing rule adopted in Chapter 9 is: **cite the version whose pagination you can see.** Chapter 9 applied it by **declining** a source — the Pearl and Bareinboim transportability paper — that it had obtained.

**8.3** `perdomo2020performative` **carries no printed page numbers.** Declining it is not available: `../decisions/0007` assigns it to Chapter 15 by name and it has been in the bibliography since Chapter 1.

**8.4** **The chapter cites it by numbered section and by Abstract**, both visible in the document and checkable by any reader holding it.

**8.5** **This is proposed as a bounded exception, not a relaxation.** The rule's purpose is that a locator be checkable, and a section number is checkable. **What is not proposed is that page numbers from a publication record be attached to a document that does not display them**, which is what the rule was adopted to prevent.

**8.6** If the author declines, the alternative is to paraphrase throughout without locators and say so — which is worse, and the record says why.

### 9. A candidate fifth instance, with the reopening documented

**9.1 This clause is a book-level governance matter and needs author attention.**

**9.2** `README.md`'s Chapter 15 core competence names **principal-agent relationships** and **information asymmetry**. **No source for either was obtained.**

**9.3** `decisions/README.md` carries a standing instruction, on notice since Decision 0012 and invoked at Decision 0016: **if a further chapter reaches for the demonstrate-because-unsourced disposition, research should be reopened rather than precedent invoked.**

**9.4 Research was reopened.** Four acquisition attempts across three routes, recorded in `research-plan.md`: Holmström (1979) via JSTOR, Akerlof (1970) via a course repository, and the Nobel Committee's 2016 scientific background on contract theory. The first two were paywalled. **The third was obtained and its text extraction is unusable** — search terms known to be present return nothing and page footers extract as private-use characters, so nothing in it can be quoted under the standing rule from Chapter 7.

**9.5 The reopening failed.** This is therefore a **candidate fifth instance**, and it differs from the first four in one respect that the author should weigh: **in those four the disposition was adopted without a documented search. Here the search happened, was recorded, and did not succeed.**

**9.6** **The treatment is kept to about one page**, as Decision 0016 clause 6.4 kept Chapter 9's. Both terms are named, defined in one sentence each **from the case rather than from a definition**, and nothing procedural is taught — no contracts, no incentive-compatibility, no participation constraints, no mechanism design.

**9.7** **Referred to the author, not resolved here.** The two live options are to accept a fifth instance with the reopening on record, or to cut the two terms from the chapter and amend the governed core competence — which is an architecture change and is not the drafting agent's to make.

### 10. The discriminator Chapter 4 asked for

**10.1** `../chapters/04-observation-provenance/spec.md` L36 requires the distinction "in a form the reader can apply, since institutional purpose and strategic response look identical from inside a dataset."

**10.2** **The discriminator is a date.** Find the moment the measure acquired consequences; look for a discontinuity at that moment and not before.

**10.3** **Three properties make it applicable**: the date is usually documentary; the check needs no counterfactual, only the record compared with itself; and it fails safely.

**10.4** **The failure mode is stated to the reader.** A discontinuity at the date is strong evidence of response. **No discontinuity is weak evidence of anything** — the response may be gradual or the measure anticipated — and a discriminator presented as decisive would be worse than none.

### 11. Vocabulary

**11.1** Introduced here: `strategic game`, `strategic dependence`, `incentive`, `commitment`, `information asymmetry`, `principal-agent`, `delegation`, `endogenous response`, `performativity`, `metric gaming`, `Goodhart effect`.

**11.1a `performativity` is not named in `README.md`'s Chapter 15 core competence.** It is registered because it is the sources' own formal statement of `endogenous response`, which the competence does name, and because a reader meeting the term elsewhere needs it. **This is the second time a chapter has registered a term its governed competence does not name** — Chapter 14's `practical identifiability` was the first, under Decision 0021 clause 6 — and the manuscript flags it to the reader in §2 rather than slipping it in. Referred to the author on the same footing.

**11.2** Closed here: `equilibrium`'s **strategic sense**, reserved for this chapter since Chapter 1.

**11.3** **The registry's one remaining `TODO` is untouched.** `utility` belongs to the drafted Chapter 11 and is not this chapter's to close.

### 12. What Chapter 15 does not do

- Teach mechanism design, auction theory, voting theory, or social choice.
- Teach any game theory beyond the strategic form: no mixed strategies, no extensive form, no subgame perfection, no repeated games, no bargaining, no best-response functions.
- Teach contract theory: no optimal contracts, no incentive-compatibility or participation constraints.
- Teach the mathematics of performative prediction, or any result from it.
- Teach the formal models inside `manheim2019goodhart`'s four sections.
- Claim anything about Lucas (1976), Goodhart (1975), or Campbell (1979) beyond what the reporting source states.
- Present strategic response as dishonesty. **The case is legal, documented, and compliant throughout.**
- Re-teach Chapter 13's policy resistance, or reuse its sources.
- Reopen Chapter 3's or Chapter 4's findings; it re-describes them.
- Treat whether a deployed rule is still working after the response — Chapter 17.

## Sources promoted

`osborne2004game` and `manheim2019goodhart` are new to `references.bib`. `perdomo2020performative` is upgraded from abstract level to Abstract and §1, discharging a Chapter 1 deferral.

## Known gaps carried forward

1. **Goodhart (1975), Campbell (1979), and Lucas (1976) all unobtained** — clause 7.
2. **No source for `principal-agent` or `information asymmetry`**, after a documented reopening — clause 9.
3. **`perdomo2020performative` has no printed pagination** — clause 8.
4. **`osborne2004game` is a pre-publication draft chapter**, read at three pages of forty-two.
5. **`manheim2019goodhart` is a preprint** whose taxonomy originates in blog posts, which the source states openly.
6. **`perdomo2020performative` read at two of twelve pages**; nothing claimed about its results.
7. **The case's payoff numbers are the book's own construction**, not derived from any source, and `case-data.md` says so.
8. The **Chapter 15 case is the water anchor's twelfth recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields.

**Clause 9.7 identifies one option that would be an architecture change** — cutting two terms from a governed core competence — and explicitly declines to take it, referring it to the author instead.
