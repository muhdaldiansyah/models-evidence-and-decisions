# Research 02 — Shadow Prices and Convexity

Cluster R02 of `research-plan.md`. Closed.

Source read directly: `boyd2004convex` printed pp. 7–9, 241, 250–252.

## 1. What a constraint is worth

The interpretation this chapter needs is given as a price story.

> "we can interpret a dual optimal λ⋆ as a set of prices for which there is no advantage to the firm in being allowed to pay for constraint violations (or receive payments for nontight constraints). For this reason a dual optimal λ⋆ is sometimes called a set of **shadow prices** for the original problem." [@boyd2004convex, p. 241]

And the sensitivity statement, which is the usable form. Paraphrased because the source's sentence carries symbols:

> The optimal multiplier on a constraint tells you how active that constraint is: if it is small, the constraint can be loosened or tightened a little without much effect on the optimal value; if it is large, loosening or tightening it a little has a large effect. [@boyd2004convex, p. 252]

The same page records that an **inactive** constraint "can be tightened or loosened a small amount without affecting the optimal value" [@boyd2004convex, p. 252].

**So a shadow price answers a question Chapter 10 could not**: not *is this constraint real*, but *what would it be worth to move it*.

Two cautions the source supplies and the chapter must carry.

**It is local.** The statement is about loosening or tightening "a small amount".

**And it is asymmetric.** "the results are not symmetric with respect to loosening or tightening a constraint" [@boyd2004convex, p. 251]. What you would gain from an extra pound is not the mirror image of what you would lose from one fewer.

## 2. Why convexity matters

The source's account of nonconvex problems is blunt and is the chapter's pivot.

> "Nonlinear optimization (or nonlinear programming) is the term used to describe an optimization problem when the objective or constraint functions are not linear, but not known to be convex. **Sadly, there are no effective methods for solving the general nonlinear programming problem.** Even simple looking problems with as few as ten variables can be extremely challenging, while problems with a few hundreds of variables can be intractable." [@boyd2004convex, p. 9]

And what you settle for instead:

> "In local optimization, the compromise is to give up seeking the optimal x, which minimizes the objective over all feasible points. Instead we seek a point that is only **locally optimal**, which means that it minimizes the objective function among feasible points that are near it, but is not guaranteed to have a lower objective value than all other feasible points." [@boyd2004convex, p. 9]

**The consequence that matters most for a general reader**, on the same page:

> "**Little information is provided about how far from (globally) optimal the local solution is.**"

And:

> "The methods require an initial guess for the optimization variable. This initial guess or starting point is critical, and can greatly affect the objective value of the local solution obtained." [@boyd2004convex, p. 9]

**So a nonconvex answer depends on where you started, and does not tell you how wrong it might be.** That is a property a reader can check for and act on without any mathematics.

## 3. Solver handoff

The claim the governed core competence's phrase "computational solver handoff" points at:

> "Using convex optimization is, at least conceptually, very much like using least-squares or linear programming. If we can formulate a problem as a convex optimization problem, then we can solve it efficiently... With only a bit of exaggeration, we can say that, **if you formulate a practical problem as a convex optimization problem, then you have solved the original problem.**" [@boyd2004convex, p. 8]

**And where the difficulty actually lies:**

> "**Recognizing a least-squares problem is straightforward, but recognizing a convex function can be difficult.** In addition, there are many more tricks for transforming convex problems than for transforming linear programs. Recognizing convex optimization problems, or those that can be transformed to convex optimization problems, can therefore be challenging." [@boyd2004convex, p. 8]

The same page notes that interior-point methods "are quite reliable" and can solve problems "with hundreds of variables and thousands of constraints on a current desktop computer, in at most a few tens of seconds" [@boyd2004convex, p. 8].

**The handoff rule the chapter can teach**: the solving is a solved problem and the recognising is not. A reader's job is to know which kind of problem they have, and to know that the answer to a nonconvex one comes with no guarantee attached.

## 4. What this chapter does not take

The source develops duality, KKT conditions, and algorithms. **None is used**, per the research plan and the governed word "intuition".

The chapter states no formulation, writes no objective function, and names no method beyond saying that reliable ones exist for convex problems and do not for the general case.

## 5. The collision to name

`shadow price` has a second sense in cost-benefit analysis — the **shadow price of capital**, a discounting concept, which appears in `epa2010economic`'s contents at §6.2.4.

**That section was not read and is not characterised.** The canon entry records that the two senses exist, that this book uses only the optimization sense, and that the other is a different concept sharing the words.

## 6. Stop condition

Met. The shadow-price interpretation recorded with its locality and asymmetry cautions; the local-versus-global consequence recorded including the how-far-off warning; the recognition-is-the-hard-part claim recorded; the collision identified.

Not read: `boyd2004convex` beyond pp. 7–9 and 241–252, which is the overwhelming majority of a 700-page book.
