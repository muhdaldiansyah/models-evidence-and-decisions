# Research 01 — Targets and Estimands

Cluster R01 of `research-plan.md`. Closed.

Sources read directly: `fda2021estimands` printed pp. 9–10; `hernan2019whatif` printed pp. 37–38; `pearl2009causal` printed p. 122.

## 1. The step that comes before everything

`pearl2009causal` p. 122 sets out what it calls "the four major steps that should be part of every exercise in causal inference":

> 1. Define: Express the target quantity Q as a function Q(M) that can be computed from any model M.
> 2. Assume: Formulate causal assumptions using ordinary scientific language and represent their structural part in graphical form.
> 3. Identify: Determine if the target quantity is identifiable.
> 4. Estimate: Estimate the target quantity if it is identifiable, or approximate it, if it is not.

**This is the chapter's spine and it is not the book's invention.** Steps 1–3 restate the governed central question — *could ideal evidence establish the target, and under what assumptions* — and step 4 is Chapter 8. `../../CLAUDE.md` requires established structure to be used where established structure exists, so the manuscript takes this one rather than constructing a four-step device of its own, as Chapter 5 had to.

The same page states the ordering discipline: the structural approach "insists on defining the target quantity, in our case 'causal effect,' before specifying the process of treatment selection, and without making functional form or distributional assumptions" [@pearl2009causal, p. 122].

**Define comes before design.** That is the sentence the chapter's §2 exists to install.

Note also what step 4 says about failure: *approximate it, if it is not*. Non-identification is not the end of the exercise in the source that supplies the spine. Collapse 8 of the readiness audit is defeated by the spine itself.

## 2. What has to be specified — an authoritative list, and its limits

`fda2021estimands` §III.C "Estimand Attributes (A.3.3)", printed pp. 9–10, opens: "The attributes below are used to construct the estimand, defining the treatment effect of interest."

The attributes, as the document presents them:

| # | Attribute | Wording anchor |
|---|---|---|
| 1 | **Treatment** | "The treatment condition of interest and, as appropriate, the alternative treatment condition to which comparison will be made" (p. 9) |
| 2 | **Population** | "The population of patients targeted by the clinical question" (p. 9) |
| 3 | **Variable** | "The variable (or endpoint) to be obtained for each patient that is used to address the clinical question" (p. 9) |
| 4 | **Intercurrent events** | handled by the strategies at §III.B — "treatment policy, hypothetical or while on treatment" (p. 10) |
| 5 | **Population-level summary** | "Finally, a population-level summary for the variable should be specified, providing a basis for comparison between treatment conditions." (p. 10) |

And a warning worth carrying, p. 10:

> "When defining a treatment effect of interest, it is important to ensure that the definition identifies an effect because of treatment and not because of potential confounders such as differences in duration of observation or patient characteristics."

### The limit on this list, restated

`../../sources/fda2021estimands.md` already records the constraint and it binds this chapter:

> Do not present it as the book's universal cross-disciplinary definition of `estimand`.

The document is regulatory guidance for clinical trials. Every attribute is phrased in terms of patients and treatments. The chapter may present it as **what one field settled on when forced to be precise**, and may generalise the *shape* — but generalising the shape is pedagogical synthesis and must be labelled as such per `../../canon/pedagogy.md`.

Attribute 4 in particular does not generalise cleanly. *Intercurrent event* is a defined clinical-trial term for something that happens after treatment starts and affects interpretation. The general version — things that happen between the intervention and the measurement that change what your number means — is real but the book should reach it by demonstration on the anchor, not by asserting that ICH's category transfers.

## 3. A second tradition, arriving independently

`hernan2019whatif` §3.6 "The target trial", printed p. 37, describes specifying "the key components of its protocol: eligibility criteria, interventions (or treatment strategies), outcome, follow-up, causal contrast, and statistical analysis."

Set the two lists side by side.

| ICH E9(R1), p. 9–10 | Target trial protocol, p. 37 |
|---|---|
| Treatment | interventions / treatment strategies |
| Population | eligibility criteria |
| Variable | outcome |
| Intercurrent events | follow-up |
| Population-level summary | causal contrast |
| — | statistical analysis |

**The correspondence is close and it is not a coincidence to be waved at.** Both are answers to the same question — *what do you have to write down before you have asked something* — reached by a regulator and by a methods textbook working in overlapping but distinct traditions.

What the chapter may say: two independent attempts to make causal questions precise converge on roughly the same set of specifications, which is evidence that the set is about the problem rather than about either field's habits.

What the chapter may **not** say: that the lists are the same list, that either is complete, or that a row-by-row mapping is exact. The table above is the book's alignment, not either source's, and the manuscript must present it as such.

## 4. Target, target quantity, estimand — the relationship

Three words, three homes, and the book has already committed to two of them.

- **`target`** — Chapter 1's informal organizing word for what an inquiry is trying to determine. Canon records it as pedagogical synthesis and warns that the noun following it carries the meaning. Unchanged.
- **`target quantity`** — `pearl2009causal` p. 122's term for the thing defined at step 1. Framework-neutral; does not presuppose a population, a treatment, or a statistical model. This is the term the chapter should use as its general one.
- **`estimand`** — the specified target of estimation, with its attributes filled in. Field-specific in its authoritative form, generalisable in shape.

Proposed hierarchy for `../../decisions/0014`: `target` (Chapter 1, informal) → `target quantity` (Chapter 7, general) → `estimand` (Chapter 7, the specified form) → `estimator`, `estimate` (Chapter 8).

The chapter must not blur `estimand` into `estimator`. `../../sources/fda2021estimands.md` records the source separating the target of estimation, the method, and the numerical result, and Chapter 1 already told the reader they are three things.

## 5. What this cluster settles for the anchor

The utility's sentence is *replacing the pump will stop the pressure drops at Hillcrest.*

Run the five attributes at it and every one is missing.

| Attribute | What the sentence says | What it needs |
|---|---|---|
| Treatment | "replacing the pump" | which of four options, compared with what |
| Population | none | Hillcrest only, or all pumped zones |
| Variable | "stop the pressure drops" | complaints, head at the top of the zone, hours below threshold |
| In-between events | none | a conservation request, a mains renewal, another hot spell |
| Summary | none | mean per heat event, or probability of any breach |

**Five attributes, five blanks.** That is the §2 opening demonstration, and it is why the chapter can spend six pages on a step most readers think they have already done.

## 6. Stop condition

Met. Attributes recorded verbatim in structure with locators; target-trial components recorded; the relationship between the lists stated as the book's own alignment; the three-term hierarchy proposed for adjudication.

Not read: `fda2021estimands` beyond pp. 9–10 for this cluster; `hernan2019whatif` beyond pp. 37–38.
