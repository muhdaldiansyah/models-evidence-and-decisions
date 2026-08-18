# Research 04: Policy Resistance, the Chapter's Case, and Exercise Design

Cluster 4 of four. Source locators were taken from reading the documents directly. Case arithmetic was computed and checked by simulation before this dossier was written.

## 1. Policy resistance — the definition, coming due

`../../sources/sterman2002models.md` records this locator, verified during Chapter 2 research, together with the instruction that Chapter 2 record it and not use it.

`sterman2002models` p. 504:

> "policy resistance, the tendency for interventions to be defeated by the response of the system to the intervention itself."

**Note what the definition does not say.** It does not say the system is perverse, or that the intervention was bad, or that someone failed to anticipate something. It says the response defeats the intervention — and a system that responds is doing what a system does.

`sterman2006evidence` p. 505 gives the cause:

> "Policy resistance arises from a narrow, reductionist worldview. We have been trained to view our situation as the result of forces outside ourselves, forces largely unpredictable and uncontrollable."

And the sharpest sentence in either paper, p. 505:

> "But there are no side effects—just effects. Those we expected or that prove beneficial we call the main effects and claim credit."

**Note the variant.** `sterman2002models` p. 505 has "There are no side effects—only effects", which Chapter 2 quoted for a boundary point. The 2006 wording is used here so the two chapters quote different sentences for different purposes.

`sterman2006evidence` p. 507:

> "Policy resistance arises because we do not understand the full range of feedbacks surrounding—and created by—our decisions."

And p. 507, on why:

> "Counterintuitive. In complex systems, cause and effect are distant in time and space, whereas we tend to look for causes near the events we seek to explain. Our attention is drawn to the symptoms of difficulty rather than the underlying cause."

## 2. The examples box

`sterman2006evidence` p. 506 gives a boxed list of instances. Three are usable and one is near-adjacent to the book's own case:

> "Road building programs designed to reduce congestion have increased traffic, delays, and pollution."

> "Forest fire suppression causes greater tree density and fuel accumulation, leading to larger, hotter, and more dangerous fires, often consuming trees that previously survived smaller fires unharmed."

> "Flood control efforts, such as levee and dam construction, have led to more severe floods by preventing the natural dissipation of excess water in flood plains. The cost of flood damage has increased as flood plains were populated in the belief they were safe."

**The flood-control instance is water infrastructure and belongs in the chapter**, with the note that it is the source's example and not the book's case. The forest-fire instance is the clearest illustration of an *accumulation* driving resistance — suppression accumulates fuel — and pairs with §2.

**The chapter should use two, not ten.** A list of ten reads as a genre, and the reader stops examining the mechanism.

## 3. Blame, and the sentence that keeps the chapter honest

`sterman2006evidence` p. 510 addresses the reading this material invites — that if structure drives behaviour, nobody is responsible:

> "Recognizing the power of system structure to shape behavior does not relieve us of personal responsibility for our actions. To the contrary, it enables us to focus our efforts where they have highest leverage—the design of systems in which ordinary people can achieve extraordinary results."

**This belongs in the manuscript.** A chapter that teaches policy resistance without it teaches a reader to explain away every failure as systemic.

Same page, on the failure mode in the other direction:

> "others to dispositional rather than situational factors; that is, to character and especially character flaws rather than the system in which they are embedded—the 'fundamental attribution error.'"

## 4. Simulation, and its pitfall

Chapter 6 taught Monte Carlo. Chapter 13 runs a trajectory. `sterman2006evidence` p. 512 supplies the warning the chapter must carry:

> "The most insightful model accomplishes nothing if the interface is obscure and the protocol for its use ineffective. The converse is worse: a poor model embedded in a potent interface may teach harmful lessons more effectively than ever before."

And p. 512 on what makes a model testable — which is Chapter 5's and Chapter 8's material arriving from a fourth direction:

> "For the testing process to be effective, models must be fully documented so that independent third parties can replicate the results, carry out sensitivity analysis, try alternative theories, and subject the model to extreme conditions."

## 5. The chapter's case — design constraints and the arithmetic

**The tenth recurrence of the water anchor, and the first run forward in time.**

Constraints from `readiness-audit.md` §8, all met:

- the stock is **usable stored water**, known since Chapter 1;
- the reader works **one accumulation by hand**;
- there are **two delays of different kinds** — a two-day verification lag on storage readings, and a two-day physical lag on production changes;
- the overshoot follows from a **written operating rule**, not from an error;
- the policy-resistance instance uses **Chapter 7's sixty-eight-year-old main** and adds no new physical fact.

### The three trajectories

All figures in ML. Reservoir capacity **260**, target **220**, critical level **120**, starting storage **220**, standing production **100**.

Demand over the heatwave: **118, 124, 128, 126, 120, 112, 104**, then **100** from day 8.

| | Do nothing | Stock-triggered rule | Flow-triggered rule |
|---|---:|---:|---:|
| Minimum storage | **88** (day 7) | **88** (day 7) | **124** (day 4) |
| Days below the critical level | day 5 onward, permanently | days 5–7 | **none** |
| Extra production | 0 | **202** | **216** |
| Spilled over the weir | 0 | **30** | **44** |
| Storage at day 18 | **88** | 260 | 260 |

### The four facts the chapter is built on

**Peak demand is day 3. Minimum storage is day 7.** Four days apart, and the gap is the whole of §3.

**Storage crosses the critical level on day 5** — two days *after* demand peaked and began falling.

**Doing nothing does not recover.** From day 8 production and demand are both 100, the system is in equilibrium, and storage sits at 88 forever. The flows re-balanced; the stock did not refill. This is `sterman2006evidence` p. 507's "doing and undoing have fundamentally different time constants" on the book's own case.

**The stock-triggered rule cannot work, and the reason is arithmetic.** The rule fires when verified storage falls below 150. Actual storage first goes below 150 on day 4; with a two-day verification lag the utility sees that on day 6; with a two-day production lag the water arrives on day 8 — **one day after the trough**. Every megalitre of the intervention arrives too late to prevent what it was ordered to prevent, and 30 of them go over the weir.

### And the repair is not free

The flow-triggered rule keys on demand rather than storage. Demand rises on day 1, so the rule fires on day 3 and water arrives on day 5. **Storage never goes below 124.**

It also spills **44** rather than 30 — about half as much again.

**Neither rule dominates.** The stock rule wastes less and does not protect; the flow rule protects and wastes more. The chapter must present this as a choice with a cost, not as a solution, or it teaches that dynamic problems have right answers.

## 6. The policy-resistance instance

Restoring pressure at the Hillcrest inlet, on the sixty-eight-year-old main Chapter 7 identified.

| Step | Extra delivered to Hillcrest | Extra leakage | Total extra draw | Share delivered |
|---|---:|---:|---:|---:|
| First pressure increase | **3.0** | **4.0** | **7.0** | **43%** |
| Second increase | **2.0** | **6.0** | **8.0** | **25%** |
| Both | **5.0** | **10.0** | **15.0** | **33%** |

**The loop.** Higher inlet pressure delivers more water to Hillcrest households *and* drives more water out through the main's existing defects. The lost water lowers pressure downstream, which is the observation that prompts the next increase.

**This is policy resistance in `sterman2002models` p. 504's exact sense** — the intervention is defeated by the system's response to the intervention itself — and it needs no new physical fact, because Chapter 7 established the pipe's age and Chapter 12's scheme B established that pressure management changes leakage.

**Two thirds of the water drawn to fix Hillcrest never reaches Hillcrest.**

## 7. Exercise design notes

**The accumulation task must come before the vocabulary.** `boothsweeney2000bathtub` measured what people do unaided; a reader who has been told the answer cannot discover that they would have got it wrong. The opening task therefore gives the seven days of demand and asks for the storage trajectory and the day of minimum storage, before §2 defines a stock.

**The predicted error is specific and should be checked for.** `boothsweeney2000bathtub` p. 278: "Many subjects appear to believe that the stock trajectory should have the same qualitative shape as the net rate." On this case that means turning storage upward on day 4, when demand peaks. The correct trough is three days later.

**The diagnosis task should include one statement that is dynamically fine and rhetorically bad**, so that the exercise does not train readers to find a fault in every sentence.

**The transfer forms need a stock, two delays of different lengths, a written trigger rule that fires too late, and a flow-keyed alternative that protects at a cost.** Both forms must be solvable with arithmetic on a table of at most a dozen rows.
