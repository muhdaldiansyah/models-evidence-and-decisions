# Research 01: Deployment, Permissible Use, and the Life Cycle

Cluster 1 of four. Every locator below was taken from reading the document directly.

## 1. The source, and why its pagination needs no exception

`nasa2024models` — *NASA-STD-7009B: Standard for Models and Simulations*, approved 5 March 2024, 88 pages, freely available from the NASA technical standards system.

**Its pagination is checkable against itself.** The standard's own table of contents lists section 4 at p. 18, Appendix A at p. 39, and Appendix F at p. 86; those are exactly the PDF pages on which they appear. **Printed page equals PDF page**, verified at six separate entries.

**Chapter 1 read this source for `intended use` and cited it by file page.** Chapter 17 reads it for deployment and cites printed pages, having established that the two coincide.

## 2. The life cycle has two parts, and the second is this chapter

`nasa2024models` p. 86, Appendix F:

> "The life cycle of a model or simulation, like that of any system, has two general parts: M&S development, which includes M&S initiation, concept development, M&S design, M&S construction, and M&S testing; and M&S application, which includes use (or operation) and M&S archiving (including the associated artifacts, products, and analysis performed during a specific use)."

**Chapters 1 to 16 of this book are the first part. Chapter 17 is the second.**

## 3. What release consists of

`nasa2024models` p. 87:

> "This testing identifies the M&S' limits of operation, i.e., where the M&S is known to work correctly (i.e., verified and validated). At the end of M&S testing, the M&S' capabilities, assumptions, and limits of operation are recorded and assessed with respect to acceptance criteria [M&S 43] to determine the permissible uses of the M&S."

> "Once M&S testing is successfully completed, the M&S is released, along with guidance of the M&S' capabilities and domain of permissible use, ending M&S development."

**`permissible use` is the term**, and note what it is a property of: not the model, but **the pairing of a model with a proposed application** — the same relation-not-property shape the book met at Chapter 3's `validity`, Chapter 9's `transportability`, and Chapter 14's `observability`. **Fourth appearance.**

## 4. The sentence this chapter turns on

`nasa2024models` p. 87:

> "During the use (or operations) phase, the M&S may or may not be used by those who developed it. In both cases, and especially the latter case, the use of an M&S starts with an assessment of whether or not the proposed use of the M&S sufficiently matches the permissible use."

And, more strongly:

> "Each application of the M&S restarts the M&S use/operation with an assessment of permissible uses against the needs of that specific proposed use."

**"Each application restarts."**

**This is a requirement that deployment is not a state but a repeated act.** A model that was validated is not therefore a model that is validated for what somebody is about to do with it, and the standard puts the check at every use rather than at release.

And the consequence when the check fails, same page:

> "If the proposed M&S use does not meet the defined permissible use, the proposed use will either be rejected or possibly allowed with the appropriate restrictions, caveats, or placarding required."

**"Placarding"** is worth having. It names a third option between rejecting a use and permitting it silently.

## 5. Revision, in the standard's own words

`nasa2024models` p. 18, explaining the form its requirements take:

> "maintenance of the record implies that the outcome or product is re-established as a result of any changes to either the RWS or the M&S."

**Two directions, both named.** The world changes, or the model changes. Either re-establishes the record.

**That is a revision trigger**, and it is broader than Chapter 12's signposts, which watch the world only.

## 6. The plan the standard requires, and the word nobody uses

`nasa2024models` p. 39, requirement [M&S 41]:

> "A plan for the acquisition, development, operation, maintenance, and retirement of the M&S (including identifying the responsible organizations) shall be maintained."

**Five verbs, and the fifth is `retirement`.**

**Almost no organisation has a retirement plan for its models**, and this book has not mentioned one in sixteen chapters. The standard requires it at the same level as acquisition, and the chapter should close on it.

**Note also "including identifying the responsible organizations".** Chapter 12's signpost needed an owner; the standard requires one for the whole life cycle.

## 7. The waterfall, refused by a standards body

`nasa2024models` p. 88, in a note appended to the life-cycle appendix:

> "The classic waterfall life cycle is idealized as a linear flow, though reverse-flow loops to previous phases are possible (even expected) if problems in M&S development or use occur."

**"Possible (even expected)."**

Chapter 16 worked two backward revisions and quoted this book's own specification on treating the teaching order as a waterfall. **Here is a NASA standard saying the same thing about its own process**, which is worth one sentence and no more.

## 8. What was not taken

- The credibility assessment scales in Appendix E, and the criticality assessment in Appendix D. Both were seen and neither is read or claimed.
- The requirements matrix beyond [M&S 41].
- Section 4.2's development requirements, which belong to Chapters 2 to 8.
- The uncertainty-characterisation requirements at p. 30, which belong to Chapter 8.
- Anything about NASA, spaceflight, or programme management.
- The standard's assurance architecture, its tailoring provisions, and its waiver process.

## 9. What the chapter takes

| Claim | Locator |
|---|---|
| The life cycle has two parts; application includes use and archiving | p. 86 |
| Testing identifies limits of operation and determines permissible uses | p. 87 |
| Release comes with guidance on the domain of permissible use | p. 87 |
| Use starts with an assessment of proposed against permissible use | p. 87 |
| **Each application restarts that assessment** | p. 87 |
| A use outside the domain may be rejected, restricted, caveated, or placarded | p. 87 |
| The record is re-established on any change to the world or the model | p. 18 |
| A plan for operation, maintenance, and **retirement**, with named organisations | p. 39 |
| Reverse-flow loops are possible and expected | p. 88 |
