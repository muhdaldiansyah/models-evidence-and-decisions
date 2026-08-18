# Research 02: Goodhart-Type Failures and Their Mechanisms

Cluster 2 of four. Every locator below was taken from reading the document directly.

**Source note.** `manheim2019goodhart` is arXiv:1803.04585v4, dated 24 February 2019. Printed page numbers appear in the footers; **printed page equals PDF page**. It is a preprint and is not peer-reviewed, and its own framing is oriented toward artificial-intelligence alignment. **The book uses its taxonomy and not its framing.**

## 1. Three laws the book could not obtain, carried by one source it could

`README.md`'s Chapter 15 core competence names **Goodhart-type failures**, **Campbell's law**, and the **Lucas critique**. None of the three originals was obtainable — see `research-plan.md`. All three are used **as reported at** this source, which is the device this book has used since Chapter 6.

**Goodhart's law**, quoted at `manheim2019goodhart` p. 1, footnote 1:

> "any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."

The footnote gives the reference, and the source's own bibliography carries it in full: Charles E. Goodhart, *Problems of Monetary Management: The U.K. Experience*, 1975, Papers in Monetary Economics, Reserve Bank of Australia.

**Campbell's law**, quoted at `manheim2019goodhart` p. 8, footnote 5:

> "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."

Reference given in full: Donald T. Campbell, "Assessing the impact of planned social change", *Evaluation and Program Planning* 2(1): 67–90.

**The Lucas critique** is **named and not quoted** at `manheim2019goodhart` p. 1, footnote 1, alongside Campbell's law, as one of the "closely related formulations". **The book therefore names it and states its content in its own words**, saying that it has not read Lucas (1976). Nothing is quoted and nothing is attributed to Lucas beyond the fact that the critique exists and is closely related.

**Note what the footnote also says**, and the chapter should carry it:

> "Because none of the terms were laid out formally, the categories proposed do not match what was originally discussed."

**A source telling you that the categories it is about to give you do not match the originals** is doing the reader a service, and the book should not tidy it away.

## 2. What a Goodhart effect is

`manheim2019goodhart` p. 1:

> "As used in this paper, a Goodhart effect is when optimization causes a collapse of the statistical relationship between a goal which the optimizer intends and the proxy used for that goal."

**Three parts, and the chapter should separate them.** A goal. A proxy. And **optimization**, which is what turns the second into a substitute for the first.

Same page, on when it matters:

> "The importance of Goodhart effects depends on the amount of power directed towards optimizing the proxy"

**This is the most practically useful sentence in the source.** It says the failure is not caused by having a metric; it is caused by pushing on one, and it scales with how hard you push. That converts a slogan into a diagnostic question: *how much force is being applied to this number?*

## 3. The four mechanisms

`manheim2019goodhart` p. 2:

> "1) Regressional, where selection for an imperfect proxy necessarily also selects for noise, 2) Extremal, where selection for the metric pushes the state distribution into a region where old relationships no longer hold, 3) Causal, where an action on the part of the regulator causes the collapse, and 4) Adversarial, where an agent with different goals than the regulator causes the collapse."

Same page:

> "These varied forms often occur together, but defining them individually is useful."

**This is why the chapter needs four names rather than one.** *Gaming* covers only the fourth, and treating all four as gaming leads an organisation to look for bad actors when the first two need none.

### Regressional, and the fact that it cannot be avoided

`manheim2019goodhart` p. 2:

> "No matter what measure is chosen for optimization, an inexact metric necessarily leads to a divergence between the goal and the metric in the tail."

And the source calls it "the most fundamental: it cannot be avoided."

**Note the connection backwards.** Chapter 3 taught that a score is not the construct. Chapter 8's estimator properties were about behaviour over repetitions. **Regressional Goodhart is those two facts meeting selection**: choose the top of a noisy proxy and you have chosen partly for noise, and the noise does not persist.

### Adversarial, and Campbell's law inside it

`manheim2019goodhart` p. 8:

> "Adversarial Misalignment Goodhart - The agent applies selection pressure knowing the regulator will apply different selection pressure on the basis of the metric"

> "Campbell's Law - Agents select a metric knowing the choice of regulator metric. Agents can correlate their metric with the regulator's metric, and select on their metric. This further reduces the usefulness of selection using the metric for acheiving the original goal."

**The typographical error in the source ("acheiving") is reproduced as it stands**, per the book's practice of quoting what is on the page.

The source also names the **Cobra Effect** at p. 8, with its reference, and the book uses the name once without claiming anything about the historical episode, which the source itself calls "a supposed situation".

## 4. The formal parts, read and not taken

Each of the four sections carries a "Simple Model" with equations. Several contain comparison symbols and set membership. **None is quoted and none is taught.** The chapter uses the four names and the four one-line characterisations.

## 5. Cautions

- **Preprint, not peer-reviewed.** The chapter says so.
- **Written for AI alignment**, which is not the book's subject. Its taxonomy transfers; its motivation does not, and the manuscript does not import it.
- **The source's own caveat** — the categories do not match the original formulations — is carried into the manuscript rather than suppressed.
- **Reference [2] is a blog post** and reference [5] is two blog posts. The taxonomy's origin is informal, which the source states openly. The book uses this source as the citable, structured statement of an idea that originated informally, and says so.

## 6. What the chapter takes

| Claim | Locator |
|---|---|
| Goodhart's law, as reported at | p. 1 n.1 |
| Campbell's law, as reported at | p. 8 n.5 |
| The Lucas critique named as a related formulation | p. 1 n.1 |
| The categories do not match the original formulations | p. 1 n.1 |
| A Goodhart effect is a collapse of the goal–proxy relationship under optimization | p. 1 |
| Importance scales with the power directed at optimizing the proxy | p. 1 |
| The four mechanisms | p. 2 |
| The forms often occur together | p. 2 |
| Regressional Goodhart cannot be avoided | p. 2 |
| Adversarial misalignment; Campbell's law as a case of it | p. 8 |
