# Source note: `boyd2004convex`

## Bibliographic record

Boyd, Stephen, and Lieven Vandenberghe. 2004. *Convex Optimization*. Cambridge: Cambridge University Press. ISBN 9780521833783. Seventh printing with corrections, 2009.

Read from the authors' freely distributed PDF, **which reproduces the published pagination**. Printed page numbers were mapped against the PDF: printed page = PDF page − 14, checked against running headers.

## Verification status

Read directly at printed **pp. 7–9, 241, and 250–252**. **The remaining seven hundred-odd pages were not read**, and nothing in this book characterises them.

This is a graduate mathematics text. **This book uses four ideas from it and none of its machinery** — no duality theory, no KKT conditions, no algorithms — per `../chapters/12-optimization-robustness/research-plan.md` and the governed word "intuition" in Chapter 12's core competence.

## Verified locators

### Convexity, and what fails without it

- **p. 8**: "Using convex optimization is, at least conceptually, very much like using least-squares or linear programming. If we can formulate a problem as a convex optimization problem, then we can solve it efficiently, just as we can solve a least-squares problem efficiently. With only a bit of exaggeration, we can say that, if you formulate a practical problem as a convex optimization problem, then you have solved the original problem."
- **p. 8**: "Recognizing a least-squares problem is straightforward, but recognizing a convex function can be difficult... Recognizing convex optimization problems, or those that can be transformed to convex optimization problems, can therefore be challenging."
- **p. 8**: interior-point methods "are quite reliable. We can easily solve problems with hundreds of variables and thousands of constraints on a current desktop computer, in at most a few tens of seconds."
- **p. 9**: "Nonlinear optimization (or nonlinear programming) is the term used to describe an optimization problem when the objective or constraint functions are not linear, but not known to be convex. Sadly, there are no effective methods for solving the general nonlinear programming problem. Even simple looking problems with as few as ten variables can be extremely challenging, while problems with a few hundreds of variables can be intractable."
- **p. 9**: "In local optimization, the compromise is to give up seeking the optimal x, which minimizes the objective over all feasible points. Instead we seek a point that is only locally optimal, which means that it minimizes the objective function among feasible points that are near it, but is not guaranteed to have a lower objective value than all other feasible points."
- **p. 9**: "Little information is provided about how far from (globally) optimal the local solution is."
- **p. 9**: "The methods require an initial guess for the optimization variable. This initial guess or starting point is critical, and can greatly affect the objective value of the local solution obtained."

### Shadow prices

- **p. 241**: "we can interpret a dual optimal λ⋆ as a set of prices for which there is no advantage to the firm in being allowed to pay for constraint violations (or receive payments for nontight constraints). For this reason a dual optimal λ⋆ is sometimes called a set of shadow prices for the original problem."
- **p. 251**: "the results are not symmetric with respect to loosening or tightening a constraint."
- **p. 252**, **paraphrased** because the source's sentence carries symbols: the optimal multiplier on a constraint tells you how active it is — a small one means the constraint can be loosened or tightened a little without much effect on the optimal value; a large one means the effect will be great.
- **p. 252**: an inactive constraint "can be tightened or loosened a small amount without affecting the optimal value."

## Role in Chapter 12

- supplies the shadow-price interpretation, with its locality and asymmetry cautions;
- supplies the consequence of nonconvexity that a general reader can act on: a local answer depends on where you started and does not tell you how far off it might be;
- supplies the solver-handoff position — the solving is a solved problem for convex cases, the recognising is not.

## Cautions

**Only four ideas are used.** Anyone extending this book's use of the source must read the relevant chapters; nothing here licenses claims about duality, algorithms, or the book's technical content.

**The symbol-bearing sentence at p. 252 is paraphrased, not quoted**, per the book's standing extraction rule.

**`shadow price` has a second sense** in cost-benefit analysis — the shadow price of capital, a discounting concept, which appears in `epa2010economic`'s contents at §6.2.4. **That section was not read.** This book uses only the optimization sense and the canon entry says so.

**Do not present convexity as a property a reader can check.** The source says recognising it "can be difficult", and this book teaches only the consequence of its presence or absence.
