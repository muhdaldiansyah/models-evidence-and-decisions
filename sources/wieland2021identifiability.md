# Source Note: wieland2021identifiability

## Citation

Franz-Georg Wieland, Adrian L. Hauber, Marcus Rosenblatt, Christian Tönsing, and Jens Timmer. 2021. "On structural and practical identifiability." *Current Opinion in Systems Biology* 25: 60–69.

## Verification

**Obtained in full and read directly.** The typeset article was used, with printed page numbers in the running heads — "On structural and practical identifiability Wieland et al. 61" on odd pages and "62 Mathematical Modelling" on even. **Printed page equals PDF page plus 59.**

Read at pp. 60–64 of 60–69.

## Role in Chapter 14

This source closes `structural identifiability`, which has stood in `../canon/terminology.md` as `TODO — verify against canonical sources` since Chapter 1, and which `../decisions/0014` clause 3 reserved for Chapter 14.

It also supplies a term the book's architecture did not anticipate: **`practical identifiability`**, which is what Chapter 8 was working with and had no name for.

## Not the primary source

The term originates with **Bellman and Åström (1970), "On structural identifiability", *Mathematical Biosciences* 7:329–339**, confirmed from `astrom2008feedback`'s own bibliography at printed p. 378.

**That paper could not be obtained.** No route to a copy with checkable pagination was found. The book therefore teaches the concept from a 2021 review rather than from the paper that named it, which is a weaker position than the book's source discipline prefers. Recorded here, in `../chapters/14-sequential-control/research-plan.md`, and in `../decisions/0021`.

## Verified locators

- p. 60, abstract: "We discuss issues of structural and practical identifiability of partially observed differential equations, which are often applied in systems biology."
- p. 60, abstract: "Practical nonidentifiability, on the other hand, has not been investigated at the same conceptually clear level."
- p. 61, **the distinction the chapter is built on**: "Concerning identifiability, one distinguishes between structural identifiability dealing with inherently indeterminable parameters because of the model structure itself, and practical identifiability, dealing with insufficiently informative measurements to determine the parameters with adequate precision."
- p. 61: "A model is structurally identifiable if a unique parameterization exists for any given model output."
- p. 61, the mechanism of failure, operative clause: a parameter is structurally non-identifiable when changing it need not alter the model's trajectory, "because the changes can be fully compensated by altering other parameters."
- p. 61, section heading: "Definition of structural identifiability and connection to observability"; the section records that on the surface of parameter values producing identical outputs the model's internal variables can change without the observations changing, and that "This is denoted as nonobservability."
- p. 63, **practical identifiability**: "we consider a combination of model and data as practically identifiable if the confidence intervals of all estimated parameters are of finite size"
- p. 64, **the repair, and it is a decision**: "one has two principal options to tailor the model complexity to the information content of the data: (1) measure additional data, corresponding to an increase of the dimension of the observation function g in Equation (2) or (2) reduce the model complexity according to the available data, corresponding to a decrease of the dimension of the parameter space"

## Cautions

- **Written for systems biology.** Every example is a cell-signalling model. The book applies the structural/practical distinction across domains, and that widening is the book's own pedagogical synthesis, stated as such in the manuscript.
- **A review, not the primary source.** See above.
- **The profile-likelihood machinery at pp. 62–64 is the source's principal contribution and is not taught.** The Fisher-information critique on those pages was read and is not used; using it would require estimation theory Chapter 8 declined to teach.
- **The source's framing of "bad, good, and useful models" at p. 60 is normative about modelling practice and the book does not adopt it.** Chapter 5 has its own account of model adequacy and it is not this one.
- **Two of the source's sentences carry parameter symbols** and are paraphrased rather than quoted, with the paraphrase declared in the manuscript.
- **One quoted word was rejoined across a line break.** The p. 61 distinction quote reads "insuffi-ciently" in the extracted text, hyphenated at a column break; it is quoted as "insufficiently". The rejoining is unambiguous, and it is recorded here because the book's standing rule is to quote only what survives extraction cleanly, and this is the boundary of that rule rather than an exception to it.
- pp. 65–69 unread.
