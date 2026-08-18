# Source Note: perdomo2020performative

## Citation

Juan Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt. 2020. “Performative Prediction.” *Proceedings of the 37th International Conference on Machine Learning*, Proceedings of Machine Learning Research 119: 7599–7609.

## Verification

Verified against the official PMLR publication page and its supplied BibTeX/metadata.

Verified metadata:
- Proceedings of the 37th International Conference on Machine Learning;
- PMLR volume 119;
- pages 7599–7609;
- year 2020.

The inspected abstract states that predictions used to support decisions can influence the outcomes they aim to predict and that ignoring this interaction can appear as distribution shift. The paper formalizes performative prediction and includes strategic feedback effects.

## Role in Chapter 1

This source supports the Chapter 1 deployment warning:

A prediction, model, metric, rule, or policy can become part of the process after deployment. If decisions or behavior respond to it, the future data-generating environment may differ from the historical environment used to construct or evaluate the analysis.

This is particularly relevant to the water-supply anchor, where a conservation action can change demand and therefore invalidate a forecast that assumed unchanged behavior.

## Cautions

- `performative prediction` is a field-specific term and is not required Chapter 1 vocabulary.
- Do not label every distribution shift performative; environmental, technological, population, measurement, and other changes can also alter distributions.
- The book generalizes the deployment warning beyond machine learning as a pedagogical synthesis; formal strategic and performative analysis remains Chapter 15.

## Role in Chapter 15

**Upgraded 2026-08-18 during Chapter 15 research.** Chapter 1 used this source at abstract level. The official PMLR PDF was subsequently obtained and read at the Abstract and §1.

`../decisions/0007` assigns this source to Chapter 15 by name: "formal strategic and performative analysis remains Chapter 15."

### A pagination problem, and how it is handled

**The PDF carries no printed page numbers**, only the running head "Performative Prediction". The published page range 7599–7609 is verified metadata from the PMLR publication page and is not visible in the document.

Chapter 9 met this before — with the Pearl and Bareinboim transportability paper — and **declined the source** under the standing rule that the book cites the version whose pagination it can see. **That option is not available here**, because the architecture assigns this source to this chapter by name and it has been in the bibliography since Chapter 1.

**The chapter therefore cites by numbered section and by Abstract**, both of which are visible in the document and checkable by any reader holding it. Recorded at `../decisions/0022` clause 8, which proposes this as a bounded exception rather than a general relaxation.

### Verified locators

- Abstract: "When ignored, performativity surfaces as undesirable distribution shift, routinely addressed with retraining."
- Abstract: "A conceptual novelty is an equilibrium notion we call performative stability."
- Abstract: "Performative stability implies that the predictions are calibrated not against past outcomes, but against the future outcomes that manifest from acting on the prediction."
- Abstract, **the scope claim**: "Performativity is a well-studied phenomenon in policy-making that has so far been neglected in supervised learning."
- §1, **the definition**: "We call such predictions performative; the prediction causes a change in the distribution of the target."
- §1: "Once recognized, performativity turns out to be ubiquitous."
- §1: "recommendations shape preferences and thus consumption, stock price prediction determines trading activity and hence prices."
- §1: "Retraining is often considered an undesired—yet necessary—cat and mouse game of chasing a moving target."
- §1: "Performativity therefore suggests a different perspective on retraining, exposing it as a natural equilibrating dynamic rather than a nuisance."
- §1: "we formalize performative prediction, tying together conceptual elements from statistical decision theory, causal reasoning, and game theory."

### Chapter 15 cautions

- **Extraction hazard.** The typesetting renders `fi` and `ffi` as single characters: *influence* extracts as *inﬂuence*, *sufficient* as *sufﬁcient*, *traffic* as *trafﬁc*. Under the standing rule from Chapters 7 and 8, **no quotation taken from this source contains an `fi`**, and several good sentences were lost to it — including the opening sentence of §1.
- **Read at two of twelve pages.** Everything after §1 is the formalisation — the distribution map, repeated risk minimisation, repeated gradient descent, the convergence theorems — and **none of it is read, claimed, or taught**.
- **The scope claim must travel with the term.** The authors say performativity is well studied in policy-making and had been neglected in supervised learning. A reader who meets the term in a machine-learning paper will otherwise take it for a machine-learning problem, and the chapter's point is that it is a general one.
- **`performative` here has no relation to its ordinary English sense**, where it means done for show. The manuscript says so once; the collision is severe and the ordinary sense is far commoner.
- **Not every distribution shift is performative**, as the Chapter 1 caution already records. The source says performativity *surfaces as* distribution shift, not the converse.
- **Performativity is not Chapter 13's policy resistance.** Policy resistance needs no agent who knows the policy exists — a reservoir resists by physics. Performativity runs through somebody acting on the prediction. Chapter 15 states the difference once and does not reuse Chapter 13's sources.
