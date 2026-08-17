# Chapter 2 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five defects in §6.

For each item: the defect, what it stops the representation from answering, and a repair. Your wording will differ; what matters is whether you found the same fault.

## 1. "More realistic than working in zones"

**Defect.** A representation is being defended by appeal to realism with no purpose stated. Detail is being treated as a virtue in itself.

**What it costs.** Property-level representation demands data the utility does not hold, and it answers a question nobody asked. Levins's third objection applies directly: a fully detailed result can be correct and still be unreadable. The defence also cannot be evaluated, because without a purpose there is no standard against which "enough detail" could be judged.

**Repair.** Ask what decision the representation is for. If the decision is which zone to restrict, zone grain is not a compromise — it is the grain the question specifies. If the colleague genuinely needs property grain, they are answering a different question and should say which.

**Note.** Property grain is not wrong. It is unjustified. Those are different criticisms, and the second is the one to make.

## 2. "Pump capacity is the cause of low pressure in Hillcrest"

**Defect.** A drawn mechanism is captioned as an established causal claim.

**What it costs.** The caption forecloses Mechanism B — the old undersized feeder main — which is drawable from the same supplied facts and points at a different repair. Acting on the caption means buying a pump when the constraint may be a pipe.

**Repair.** Rewrite as a proposed mechanism: *on this representation, pump capacity limits refill of the Hillcrest tank.* Then state what would test it: running the duty pump at elevated output through one hot afternoon and recording zone pressure. Until that intervention has been run, the diagram is a hypothesis.

**Note.** Nothing is wrong with the drawing. The defect is entirely in the caption — which is why this one is easy to miss.

## 3. "9.9 ML against 9.0 ML daily demand, so supply is secure through tomorrow"

**Defect.** An aggregate is being read against a question it cannot express.

**What it costs.** Hillcrest holds 0.6 ML and draws 0.9 ML per day. With no pump, that zone is out in about sixteen hours. The town-level figures cannot show this, because they contain no zones.

**Repair.** Either disaggregate the storage and demand by zone, or state explicitly that this conclusion is about total volume and says nothing about where or when supply fails.

**Note.** The arithmetic in the briefing note is correct. Marking this as an arithmetic error is itself a miss. The failure is that a correct aggregate calculation was read as an answer to a question the representation cannot pose — and an aggregate that gives no answer looks exactly like an aggregate that says nothing is wrong.

## 4. "The boundary stops at the property line of the treatment works"

**Defect.** An analytical boundary has been set by a physical or legal edge.

**What it costs.** Almost everything that matters for supply — the distribution network, the pumps, the zones, the customers — is outside a boundary drawn at the works' fence. The representation can describe production and nothing about delivery.

**Repair.** Set the boundary from the purpose. If the question is whether the reserve will be breached, the boundary needs storage, inflow, and demand. If the question is who loses service first, it needs the zones and the pump. Neither cut has anything to do with who owns the land.

**Note.** Legal and physical edges are frequently *convenient* boundaries, and sometimes the right ones. The defect is treating the edge as the reason.

## 5. State listed as reservoir volume, Hillcrest tank volume, and total system storage

**Defect.** A listed state variable is recomputable from the others.

**What it costs.** Less than the others, and it is worth being honest about that: nothing here produces a wrong answer. What it produces is a representation that has not been thought through, and the same looseness applied to a larger model creates redundant quantities that can silently disagree with each other.

**Repair.** Apply the state test. Total system storage is the sum of the two tank volumes, so it need not be carried — it can be computed whenever it is wanted. The state is the two tank volumes.

**Note.** Total system storage **was** the state in Chapter 1's single-tank representation. It is not state here. If you marked this item as correct because it was state before, you have found the exact place where role and representation come apart.

## After you have compared

Do not simply correct your answers.

Pick the one you got most wrong and write two sentences on **why that defect was invisible to you**. The failure modes in this chapter are not hard to state; they are hard to notice while you are busy building something.
