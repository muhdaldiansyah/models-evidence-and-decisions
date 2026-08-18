---
chapter: 2
part: 1
title: "Representation, Mechanisms, and Scale"
status: drafted
---

# Chapter 2: Representation, Mechanisms, and Scale

## 1. The Same System, Two Questions

In Chapter 1 a small municipal water utility entered a seven-day heatwave.
An independent tank-level check put verified usable storage at **9.9 ML**, against a drought-plan operating reserve of **4.5 ML** supplied by that case.
Treated-water input ran at **8.4 ML per day**, and forecast demand for the first day was **9.0 ML**.

You worked out whether the reserve would be breached within seven days.
To do that you used a representation, though nothing in Chapter 1 asked you to look at it.

The representation was this: **one tank, one inflow, one demand number.**

It was a good representation.
Its arithmetic was correct, it used every fact that mattered, and it answered the question it was built for.

Now here is a different question about the same utility.

> If supply has to be restricted, who loses service first?

Read that question against the representation you just used.
The representation has one tank and one demand number.
It contains no *who*.

### Before reading further: sketch what would be needed

Take about **eight minutes**.
Without looking ahead, write short answers to two things.

1. Sketch what a representation of this utility would have to contain in order to answer the second question. A labelled box-and-arrow diagram with a few notes is enough.
2. Name one thing the Chapter 1 representation cannot tell you, and say why it cannot.

Keep what you write.
You will come back to it at the end of the chapter, and the comparison is more useful than a score.

---

The gap you have just found is the subject of this chapter.

Two questions about one utility needed different things inside the model.
Nothing about the town changed between them.
What changed was what was being asked.

There is something else worth noticing about Chapter 1, and it is the more uncomfortable point.

Nobody ever wrote that representation down.

It was not stated, not justified, and not labelled.
It arrived with the problem — a storage figure, an inflow, a demand table — and everything after that inherited it.
That is the normal condition of analysis, and it is exactly what makes representation worth a chapter.
A representation you never stated is one you cannot check, cannot defend, and cannot notice the limits of.

The whole of Chapter 1's analysis was conducted inside a picture that no one had chosen on purpose.

This chapter's claim is that **what belongs inside a representation, and at what grain, is settled by the stated purpose** — not by the system, and not by how much happens to be known about it.

That claim is not this book's invention, and it is worth seeing early how ordinary it is.
An engineering textbook states it as a working fact: "The model we choose depends on the questions we wish to answer, and so there may be multiple models for a single dynamical system, with different levels of fidelity depending on the phenomena of interest" [@astrom2008feedback, p. 27].
An agency standard requires that a documented intended use state what is represented [@nasa2024models, §4.1.1.1].
A biologist arguing about method put it as a matter of survival for the working scientist, which we will come to shortly [@levins1966strategy, pp. 421–422].

By the end of this chapter you should be able to take an unfamiliar system and two different purposes, build a defensible representation for each, and say what each one can and cannot answer.

## 2. Boundary: What the Question Puts Inside

### The thing and the model of the thing

A **representation** stands for a selected part or aspect of the world.
The part of the world it stands for is the **target system** [@frigg2025models, §1].

Notice that *selected* is doing work in that definition.
Selection is not a compromise that a better modeller would avoid.
It is what makes something a representation rather than a duplicate.

Three things must be kept apart: the target system, the representation of it, and any description of that representation.
They come apart easily under inspection — a model of the solar system consists of orbiting spheres, but it makes no sense to say that about a description of the model [@frigg2025models, §2.4].

In this book, `model` and `representation` mean the same thing.
This chapter mostly says `representation`, because that word keeps selection and purpose in view.

One caution about vocabulary.
Chapter 1 used `target` for what an inquiry is trying to determine.
`Target system` is a different idea: the part of the world being represented.
They often coincide, and they are not the same.
Here, the target system is the utility and its network; the target of the second question is which customers lose service first.

### The boundary is a cut you make

Every representation has a **boundary**: what is inside it and what is outside.

The boundary is an analytical cut, not a physical edge.
Nothing about a town tells you whether customer behaviour is inside your model of it.
A pipe has a wall; a representation does not.

This matters because boundaries are routinely mistaken for features of the world, and the mistake is invisible.
A representation that excludes something does not announce the exclusion.
It simply has nothing to say.

### Why more is not better

Suppose you could avoid the problem by including everything.

Richard Levins considered exactly that option and rejected it in three moves.
The brute-force approach, he wrote, "would be to set up a mathematical model which is a faithful, one-to-one reflection of this complexity" [@levins1966strategy, p. 421].
It fails, he argued, because there are too many parameters to measure, because the equations exceed what can be solved, and — decisively — because "even if soluble, the result expressed in the form of quotients of sums of products of parameters would have no meaning for us" [@levins1966strategy, p. 421].

Take the third reason seriously.
It is not about cost or effort.
A fully detailed representation can fail by being **uninterpretable**: correct, complete, and useless, because no human being can read an answer out of it.

Detail is not free, and it is not automatically realism, and realism is not automatically adequacy.
Åström and Murray open their modelling chapter with the same warning in the form of an anecdote: Fermi, told of a good fit, asked how many arbitrary parameters had been used, and recalled von Neumann's remark that with four parameters one can fit an elephant, and with five make him wiggle his trunk [@astrom2008feedback, p. 27].

### Three boundary questions on the utility

The second question — who loses service first — forces boundary decisions that Chapter 1 never had to make.

**Is customer response inside?**
Chapter 1 ended with an observation: after a voluntary conservation request, demand came in at **8.6 ML** against a **9.0 ML** no-action forecast.
If customers respond, and if you want to know who loses service first, then response is part of what determines the answer.
Leaving it outside is defensible only if you say what you are giving up.

**Is the emergency interconnection inside?**
The case supplies an interconnection with a neighbouring system, capable of **1.5 ML per day**, requiring **12 hours** to activate under a mutual-aid agreement.
Put it outside the boundary and it does not exist for your analysis.
Put it inside and a new alternative appears — one you could not otherwise have considered, because a representation can only contain alternatives it can express.

That is the general point, and it runs the opposite way from the usual worry about model size.
Widening a boundary does not merely add work.
"Adding the input makes the model richer and allows new questions to be posed" [@astrom2008feedback, p. 29].

**Is the pump's electrical supply inside?**
Hillcrest is served by a pump.
A pump needs power, power comes from a grid, and grids are themselves stressed by heatwaves.
Here the honest answer is probably no — not because the dependency is unreal, but because following it leads to a representation of the regional electricity system, and the question does not require one.

You have just made three boundary decisions with three different justifications.
None of them was read off the town.

The first was included because it changes the answer.
The second was included because it creates an option.
The third was excluded because chasing it would replace the question with a bigger one.

Those are three different kinds of reason, and it is worth being able to tell which you are giving.

### Produced inside, or arriving from outside

Once a boundary exists, everything in the representation falls into one of two kinds.

Some things the representation **produces**.
The volume in the Hillcrest tank tomorrow morning is produced: it follows from today's volume, what the pump delivered, and what customers drew.

Other things **arrive from outside**.
Tomorrow's temperature arrives. The representation does not generate it; it accepts it and reacts.

This distinction sounds bookkeeping-like and is not.
Whatever arrives from outside is, by construction, something your representation cannot explain, cannot predict, and cannot help you influence.
Moving something from outside to inside is often the single most consequential change you can make to a representation.

Consider customer demand.
Chapter 1 treated it as arriving from outside — a forecast table, generated by weather.
Then a conservation request was issued and demand came in at **8.6 ML** instead of **9.0 ML**.

At that moment demand stopped being purely something that arrives.
It became partly something the utility's own actions produce.
The representation that treated demand as external could record the surprise but could not have anticipated it, because the pathway by which a request changes demand was not in the picture at all.

A representation cannot be surprised by something it contains.
It can only be surprised by what it left outside.

### Writing the boundary down

Because a boundary is a decision, it can be recorded, and recording it costs almost nothing.

A serviceable boundary note is three lines:

- **Purpose.** The question this representation is being built to answer.
- **Inside, and why.** The things included, each with the reason it earns its place.
- **Outside, and what that costs.** The things excluded, each with what you are giving up by excluding it.

The third line is the one people omit, and it is the one that pays.
"Customer response is outside; this representation therefore cannot tell us whether a conservation request would relieve Hillcrest" is a sentence that will save someone from reading an answer the model never gave.

### What the cut can change

It is tempting to think of a boundary as controlling only how *much* is in the model.
It can also change what is inside it.

Åström and Murray give a concrete case from compositional modelling: "states may disappear when components are connected. This implies that the internal description of a component may change when it is connected to other components" [@astrom2008feedback, p. 33].
Two capacitors, each with its own state, are joined in parallel; one of the states is gone.

So where you cut can alter the internal description, not only its size.
That is worth holding on to when you are tempted to treat boundary-drawing as bookkeeping.

### What narrow boundaries hide

The characteristic failure of a boundary drawn too tight is not visible error.
It is silence about consequences that arrive later or elsewhere.

Policies can produce delayed and distal effects, and interventions can trigger responses that undermine what they were meant to achieve; narrow boundaries can hide both [@sterman2006evidence].

There is a sharper way to put this, and it is worth sitting with because it reframes a word you use constantly.

> "There are no side effects—only effects. Those we thought of in advance, the ones we like, we call the main, or intended, effects, and take credit for them. The ones we didn't anticipate, the ones that came around and bit us in the rear—those are the 'side effects'." [@sterman2002models, p. 505]

Read that as a claim about boundaries, which is how it is meant.

A *side effect* is not a special kind of effect that behaves differently from the main one. It is an ordinary effect that fell outside the boundary somebody drew. The world does not sort consequences into main and side; a representation does, by what it included.

Which means the phrase is doing something unhelpful whenever it is used. Calling an outcome a side effect describes your model, not the world — and it quietly transfers responsibility from the modeller to reality. The same source is blunt about it: when we blame outside shocks and side effects for a policy's failure, "we think we are describing a capricious and unpredictable reality. In fact, we are highlighting the limitations of our mental models" [@sterman2002models, p. 505].

Two cautions before you carry that too far.

The passage comes from system dynamics, a tradition that pushes hard toward putting more inside the boundary — its own section heading is "(Almost) nothing is exogenous" [@sterman2002models, p. 505]. That is an argument for widening, and it is a good one, but this chapter has just spent several pages establishing that some exclusions are correct. A representation that includes everything answers nothing, as Levins's brute-force case showed. Take the passage as a reason to check your exclusions, not as a rule that there should not be any.

And it is a prize lecture rather than a research result. It asserts from long experience; it does not demonstrate.

This is also why a boundary is always provisional.
You draw it from the purpose you have, and you redraw it when the analysis shows you something the cut was hiding.

### When to redraw

"Provisional" is easy to say and hard to act on, so here are four signals that a boundary needs moving.

**The answer is dominated by something arriving from outside.**
If almost all the variation in your result is driven by a quantity your representation simply accepts, you have drawn the boundary around the part that does not matter.

**A decision-maker keeps asking a question you cannot answer.**
Not a question you answer badly — one the representation cannot express. That is the signal from §1, and it is the reliable one.

**Something you excluded turns out to respond to what you do.**
Chapter 1's demand forecast was built on no new action, and then an action was taken. Anything that reacts to the analysis or to the decision is a candidate for coming inside.

**Your recommended action works through a pathway you did not represent.**
If the reason a proposal is supposed to help lies outside the boundary, the representation cannot support the proposal, whatever its arithmetic says.

Redrawing on any of these is not a correction.
It is the normal operation of the method.

### Pause: why is the boundary a decision rather than a discovery?

Write two or three sentences before reading on.
Then check them against what you have just read.

If your answer is that a boundary is a decision *because you can always change it*, you have named a symptom.
The reason is that nothing in the target system determines the cut.
The cut follows from what you are trying to answer, and two people answering different questions about one town will correctly draw it differently.

### Task: one inclusion, one exclusion

Take the purpose: *decide, today, whether to ask for voluntary conservation across the town.*

1. Name one thing you would put **inside** your boundary, and defend it in one sentence by reference to that purpose.
2. Name one thing you would deliberately leave **outside**, and defend it the same way.

Now change the purpose to: *decide which zone to restrict first if restriction becomes necessary.*

3. Which of your two decisions changes, and why?

If neither changes, one of your two purposes has not been stated precisely enough to constrain anything.

## 3. Parts, Roles, and What Must Be Carried Forward

A boundary tells you what is in play.
It does not tell you what the things inside are, or which of them you need to keep track of.

### Parts and what they do

A representation contains parts, and parts do things.

The mechanistic literature defines these together and defines them by role rather than by substance: "Activities are the producers of change. Entities are the things that engage in activities" [@machamer2000mechanisms, p. 3].

That is convenient for us, because this book's parts are rarely objects in the tidy sense.
A reservoir is a part.
So is a pump station, a pressure zone, a customer class, and — if your boundary includes it — a mutual-aid agreement.

### The role table

For the rest of this chapter, when you build a representation, write it down like this.

| Part | What it does | Role | Grain |
|---|---|---|---|
| Main reservoir | stores treated water | carried forward | one volume |
| Hillcrest tank | stores water for the high zone | carried forward | one volume |
| Duty pump | moves water from reservoir to Hillcrest tank | acted on from outside | capacity per day |
| Lowfield demand | draws water | acted on from outside | one volume per day |
| Millbrook demand | draws water | acted on from outside | one volume per day |
| Hillcrest demand | draws water | acted on from outside | one volume per day |
| Zone pressure | what customers experience | observed | per zone, adequate or not |

Three roles are enough at this stage.
Something is **carried forward** if you have to know it now in order to say what happens next.
Something is **acted on from outside** if it arrives into the representation rather than being produced by it.
Something is **observed** if you learn about it but it does not itself drive anything.

The important property of this table is that the roles are assigned **within a representation**.
They are not properties of the world.
The very same quantity can be carried forward in one representation, arrive from outside in a second, and merely be observed in a third — and none of those is a mistake.

### The same quantity, three roles

That claim is easy to nod at and easy to forget, so watch one quantity move.

Take **Hillcrest demand**.

In the representation you are building — *which zone runs short first* — Hillcrest demand arrives from outside. It is driven by weather, and the representation accepts it as given.

Now build a different representation, for the purpose *would a targeted conservation request in Hillcrest relieve the zone?*
Customer response is now inside the boundary, so Hillcrest demand is no longer simply given: it is produced, in part, by what the utility asks for.
Same quantity, different role, because the boundary moved.

Now build a third, for the purpose *is our zone metering working?*
Here Hillcrest demand is neither carried forward nor an external driver.
It is the thing being observed, and the object of interest is whether the observation is any good.

Three representations of one town, one quantity, three roles, no error anywhere.

If you find yourself asking "but what *is* Hillcrest demand, really?", the question has no answer at this level, and needing one is a sign of the first collapse this chapter is trying to prevent.
Hillcrest demand is a quantity in the world.
Its **role** is something a representation assigns.

### State: what must be carried forward

The things carried forward have a name.

The **state** is the collection of quantities that summarize the past well enough to answer what comes next.

Control theory has used this idea for a long time, and its standard definition is worth reading closely, because the purpose is inside the definition: "The state of a system is a collection of variables that summarize the past of a system for the purpose of predicting the future" [@astrom2008feedback, p. 34].

Not *the variables that change*.
Not *the important variables*.
The ones that summarize the past **for the purpose of predicting the future** — and which those are depends on what you are trying to predict.

The same source adds where to look for them in a physical system: the state consists of the variables needed to account for storage of mass, momentum and energy, and "a key issue in modeling is to decide how accurately this storage has to be represented" [@astrom2008feedback, p. 34].

Look for what accumulates.
Water in a tank accumulates. Applications in a queue accumulate. Heat in a building's walls accumulates.

### The state test

This gives you something to apply rather than a slogan.

> A quantity belongs to the state only if you must know it now to answer what comes next.
> If it can be recomputed from the others, or if it does not bear on what comes next, it is not state.

Work three candidates from the utility.

**Today's forecast high temperature.**
It matters — it drives demand.
But it arrives into the representation from outside rather than being carried within it.
Not state.

**Current pump flow rate.**
Recomputable from the pump setting and whether the pump is running.
Not state.

**Total system storage.**
This one repays attention.
In Chapter 1's single-tank representation, total system storage *was* the state — it was the one thing you carried from day to day.
In the zone representation it is the sum of the main reservoir volume and the Hillcrest tank volume, so it can be recomputed from them.
It is **not** state here.

Nothing about the water changed.
The same quantity is state in one representation and not in another, because state is a property of the representation relative to what is to be predicted.

That is the sharpest available answer to the most common error with this word, which is to use `state` for any variable that happens to move.

### Grain

The role table has a last column, and it is the one people skip.

Hillcrest demand is represented as **one volume per day**.
It could have been represented per property, per hour, per customer class.
The choice of grain is a decision, and it decides what becomes answerable.

At zone grain you can ask which zone runs short.
At property grain you could ask which households run short — and you would need household-level data you do not have, for a question nobody asked.
At system grain, which is what Chapter 1 used, you cannot ask either.

Grain is not a dial that runs from worse to better.
It runs from *answers one set of questions* to *answers a different set*.

Set the three side by side.

| Grain of demand | Makes answerable | Makes unanswerable |
|---|---|---|
| Whole town, per day | Will the reserve be breached this week? | Which zone runs short; where to target a restriction |
| Per zone, per day | Which zone runs short first; where a restriction would bite | Which streets or properties fail; what happens during the evening peak |
| Per property, per hour | Peak-hour behaviour; individual exposure | Nothing further that this decision needs — and it demands data the utility does not hold |

The bottom row is the interesting one.

Finer is not better once the grain has passed what the question needs.
It costs data you may not have, it costs interpretation you may not be able to give, and it can quietly change the question — a per-property representation invites questions about individual customers that the decision at hand was never about.

There is a matching failure in the other direction, and it is the one this chapter's case turns on.
A grain too coarse does not produce a wrong answer.
It produces no answer, in a form that looks like reassurance.

### A note on time

Grain is not only spatial or organizational.

The utility's representation runs in days, because the drought plan runs in days and the seven-day forecast arrives in days.
That is a choice, and it is invisible until it fails.

A daily representation cannot see an evening peak.
If Hillcrest's pressure problem appeared for two hours each evening and recovered overnight, a representation that works in daily totals would show a zone comfortably supplied and would be, in the only sense that matters, blind.

Whenever you fix a grain in time, ask what happens **inside** one of your time steps that the representation will never see.

### Where this stops

You now have quantities that must be carried forward.
You do not have any rule for how they move.

That rule — how a state evolves, what equilibrium means, when a system is stable, what happens when effects feed back on their own causes — is Chapter 13.
How to infer a state you cannot observe directly, and how to act on it through time, is Chapter 14.

Chapter 2 stops at knowing what must be carried and at what grain.
That is a real stopping point, not a gesture: you can complete a representation without any evolution law, and you cannot write an evolution law without first knowing what is being evolved.

### Task: role table and state test

1. Complete a role table for the utility under the purpose *decide which zone to restrict first*.
2. Apply the state test to two quantities of your own choosing, one of which should fail it. Say in one sentence why it fails.

## 4. Mechanism: What Would Have to Be True

A representation with parts and roles can tell you what is present.
It does not yet say how the parts produce the behaviour you care about.

### What a mechanism is

A **mechanism** for a phenomenon is a set of parts whose activities and interactions are organized so as to be responsible for that phenomenon [@craver2026mechanisms, §2].

Three components, and a demand.
Parts, what they do, and how they are arranged — organized *so as to be responsible for* the phenomenon.

That last clause is where the trouble lives, and we will come back to it.

### There is no mechanism of a system

You cannot draw the mechanism of a water utility.

You can only draw the mechanism of something the utility does.

This is not a quibble.
It is a standing feature of the concept: "All mechanisms are mechanisms *of* some phenomenon" [@craver2026mechanisms, §2.1.1], and mechanisms "are defined only relative to the phenomenon they cause, underlie, or otherwise explain" [@craver2026mechanisms, §5.1].
Change the phenomenon and the correct decomposition of the same system changes with it.

You have seen this shape before.
In §2 the boundary followed the question.
Here the mechanism follows the phenomenon.

This book treats those as the same lesson and generalises them into one: **representations follow purpose**.
That generalisation is worth naming as what it is.
The sources say a mechanism is relative to a *phenomenon*; extending that to purposes generally is this book's own pedagogical move, not something the mechanistic literature asserts.
It holds up well, and it is ours rather than theirs.

### Naming the phenomenon

For the utility, the phenomenon is this:

> During a heatwave, Hillcrest loses pressure before the other zones.

Now a mechanism can be drawn, because there is something for it to be a mechanism of.

### Mechanism A: pump capacity

In prose: hot weather raises demand in every zone.
Hillcrest's supply arrives only through the duty pump, which has a fixed capacity of **1.1 ML per day**.
When the zone's draw exceeds what the pump can replace, the hilltop tank falls.
As the tank falls, pressure at the top of the zone falls with it.

As a diagram, four boxes in a line — reservoir, pump, hilltop tank, customers — with an arrow from hot weather into the customer box, and an arrow from the tank box to a labelled outcome, *zone pressure*.

Every arrow has an activity you can name: pumping, storing, drawing.

### Mechanism B: the feeder main

Now a second one, from facts the case also supplies.

Hillcrest's feeder main is the oldest in the system.
Water moving through a pipe loses pressure along the way, and the loss grows sharply with flow.
On a hot afternoon, when flow is high, the loss along an old undersized main could be enough to drop pressure at the top of the zone — while the hilltop tank still holds water.

This mechanism also has nameable activities.
It also explains the phenomenon.
It is also drawable from supplied facts.

And it points at a different repair.
Under Mechanism A you would add pump capacity.
Under Mechanism B a bigger pump would push more water through the same constricted main and might change very little.

### The four-sign check

You now have two drawings, both plausible, pointing at different actions.
Something has to tell you what a drawing has actually established.

Four signs that a drawn mechanism is still a hypothesis.

**An arrow you cannot name an activity for.**
If you cannot say what the arrow *does*, you have asserted a connection you have not described.
A missing arrow — "the inability to specify an activity" — "leaves an explanatory gap in the productive continuity of the mechanism" [@machamer2000mechanisms, p. 3].

**A black box.**
A sketch is an abstraction "for which bottom out entities and activities cannot (yet) be supplied or which contains gaps in its stages"; the gaps are "black boxes, which we do not yet know how to fill in", and the sketch "serves to indicate what further work needs to be done" [@machamer2000mechanisms, p. 18].
A black box is not a failure. It is a marker of what remains to be found.

**It shows how the phenomenon could be produced, not that it is.**
A model can describe an organization that *could* produce the phenomenon, or one that *actually* does; these are different achievements [@craver2026mechanisms, §3.3].
Both Mechanism A and Mechanism B are currently the first kind.

**No intervention has tested it.**
This is the decisive one, and it comes from the mechanists themselves.
While a mechanism is operating, an experimenter "may intervene to alter some part of the mechanism and observe the changes in a termination condition"; changes produced by such interventions "can provide evidence for the hypothesized schema" [@machamer2000mechanisms, p. 17].

The diagram is the hypothesis.
The intervention is the evidence.

For the utility, that would mean running the duty pump at elevated output through one hot afternoon and recording zone pressure.
The case does not tell you the result, because you have not run it.

### Running the check on your own two drawings

Apply the four signs to Mechanism A and Mechanism B and see where each stands.

| | Mechanism A (pump capacity) | Mechanism B (feeder main) |
|---|---|---|
| Every arrow has a nameable activity? | Yes — pumping, storing, drawing | Yes — flowing, losing pressure along the main |
| Any black box? | Yes: *how far does the tank have to fall before customers notice?* | Yes: *how much loss does this main actually produce at this flow?* |
| Could-produce, or does-produce? | Could | Could |
| Intervention run? | No | No |

Both drawings pass the first test and fail the last two.
Neither has a nameable-activity problem; both have a black box; and neither has been tested.

Notice what the black boxes are telling you.
They are not decoration and they are not embarrassment — each names the specific measurement that would move that drawing forward.
A sketch, on the mechanists' own account, "serves to indicate what further work needs to be done."
Yours have just told you what to go and find out.

### Association will not close the gap either

You might hope that data could settle it without an intervention — that if pressure and pump load move together, Mechanism A is confirmed.

It cannot, and this is one of the load-bearing distinctions in the book.
Association alone does not establish what would happen under an intervention; causal conclusions require causal assumptions or design information that association by itself does not supply [@pearl2009causal].

How mechanisms and causation relate is, in fact, still argued about among the people who work on mechanisms [@craver2026mechanisms, §2.1.3].
This chapter does not settle it and does not need to.

### The same shape, without any pipes

Strip out the engineering and the structure survives.

A shop notices that customers who use its loyalty app spend more than customers who do not.
Someone draws a mechanism: the app sends reminders, reminders bring people in more often, more visits mean more spending.
Every arrow has a nameable activity. It is a good drawing.

Now draw the other one.
People who already shop often are the ones who bother to install a loyalty app; the spending brings the app, not the app the spending.
Every arrow in that one has a nameable activity too.

Two mechanisms, opposite directions, one association, both drawable.
Nothing about the drawing decides between them.

### Pause: what would have to happen first?

Before reading on, write one or two sentences answering this:

> What would have to happen before you could write *"the pump capacity is the reason Hillcrest loses pressure first"*?

Then check your answer against the four signs.
If your answer is "collect more pressure data", look again at the previous section.

### How to write it

Until an intervention has been run, write the weaker sentence, and write it deliberately.

Permitted: *a proposed mechanism*; *on this representation, the pump limits refill*; *this is how the shortfall could be produced*.

Not permitted: *the mechanism is*; *the pump causes the pressure loss*; *therefore adding pump capacity will fix it*.

This is not timidity.
Between Mechanism A and Mechanism B lies a real decision about spending money on a pump or on a pipe, and the drawing does not decide it.

Chapter 7 is where the machinery for closing that gap lives — what would have to be true for evidence to establish a causal claim, and what designs can supply it.
Chapter 2's job is to get you to the edge of that gap knowing you are standing at it.

## 5. Leaving Out, Making Up, and Lumping Together

Every representation you have built so far is simpler than the town.
This section is about the three different ways it is simpler, and why the difference decides what you owe by way of defence.

### Leaving something out

The first way is **abstraction**: you leave a feature out.

The useful property of an omission is that it is silent.
A representation that omits something has not said anything untrue about it.
On one influential analysis, abstraction "remains silent about certain features … it does not say anything false" [@frigg2025models, §1].

The same distinction is reported in the idealization literature, where abstraction is "a kind of omission" and idealization "the assertion of falsehood" — "omission and distortion are distinguishable practices" [@weisberg2007idealization, fn. 14].

Both of those reports attribute the distinction to the same source, Martin Jones's 2005 framework, which this chapter has not read directly.
And the boundary is not settled: Weisberg reports the distinction and then declines to adopt it, and one long-standing sense of "idealization" — stripping away properties believed irrelevant to the problem — is plainly omission wearing the other word [@frigg2025models, §1].

Treat omission-versus-distortion as a **useful cut you can apply**, not as a fact everyone agrees on.

### Making something up

The second way is **idealization**: you put in something you know is false.

Frictionless planes, point masses, instantaneous transfers, perfectly informed customers.
These are not gaps. They are assertions, and they are wrong on purpose.

### Why the difference is the whole point

Here is why this is not vocabulary for its own sake.

**An omission is defended by showing the feature does not bear on the question.**
That is often easy. Sometimes it is obvious.

**A distortion is defended by showing that the error it introduces is tolerable for the use.**
That is a strictly harder argument, because you have to say how big the error is and why it does not change the answer.

Two simplifications, two different debts.
A reader who cannot tell which one they have made cannot tell which debt they owe.

Work both on the utility.

**Zone-level demand is an omission.**
The representation treats Hillcrest as one demand quantity. Individual properties, meters, and households are not in it.
Defence: the question is which *zone* runs short, and household variation does not bear on that.
This is easy to defend, and it is defended by the purpose.

**Instantaneous lossless transfer is a distortion.**
The representation treats water moving from the main reservoir to the hilltop tank as arriving at once and complete.
It does not. There is a pump start-up period, and there is friction loss along the way.
The representation asserts something false.

Defending that is harder, and notice you cannot defend it by saying it does not matter.
Mechanism B in §4 was *entirely about* friction loss along the feeder main.
The same distortion is tolerable when you are asking how long the tank lasts and intolerable when you are asking why pressure falls.

### Simpler is not more general

One more distinction, because it is quietly responsible for a lot of confused modelling.

Reducing detail and widening scope are different moves.

The mechanistic literature separates them explicitly: "Degrees of abstraction should not be confused with degrees of generality or scope. Abstraction is an issue of the amount of detail included in the description of one or more mechanism instances. The generality of a schema is the scope (small or large) of the domain in which it can be instantiated" [@machamer2000mechanisms, p. 16].

Two dials, not one.

A representation of *this* utility's Hillcrest zone can be extremely detailed and apply to nothing else.
A representation of *hilltop zones fed by a single pump* can be sparse and apply to hundreds of towns.
You can turn either dial without touching the other, and "let's simplify it so it applies more widely" quietly turns both while pretending to turn one.

All four combinations exist, and each is right for something.

| | Narrow scope | Wide scope |
|---|---|---|
| **Much detail** | This town's Hillcrest zone, modelled pipe by pipe — for designing the actual upgrade | A detailed model of every pumped zone in the region — expensive, and rarely worth building |
| **Little detail** | Hillcrest as one tank and one pump — what you built for this week's decision | *A pumped zone fails when draw exceeds pump capacity* — a sentence that travels everywhere |

The bottom-right cell is worth a moment.
It contains almost no detail and applies almost everywhere, and it is genuinely useful — it tells you what to check first in a town you have never visited.
It also cannot tell you whether Hillcrest is in trouble tomorrow.

When someone objects that a representation is "too simple", find out which dial they mean.
If they mean it lacks detail the question needs, they are right.
If they mean it applies to too few situations, that is a different complaint — and it may not be a complaint at all, since you were only ever asked about this town.

### The pendulum, twice

The cheapest possible demonstration that content follows purpose.

To answer *how long is one swing*, a pendulum is a length and a gravitational constant; air resistance is omitted.
To answer *why does it eventually stop*, air resistance and pivot friction are the entire subject.

Same object, two entity sets, both correct.

### Lumping things together

The third way a representation is simpler is **aggregation**: treating distinguishable things as one.

Chapter 1's representation had one demand number for the whole town.
That is an aggregation, and it was made before anyone collected anything.

Say clearly what kind of aggregation this chapter means, because the word does double duty.
**Representational aggregation** is a modelling choice made when the representation is built.
Aggregation can also happen in the records — data reported monthly instead of daily, by district instead of by address, already summed before you ever see it.
That second kind is the observation process, and it is Chapter 4's subject.

The two can point in opposite directions.
You can aggregate in your representation while holding disaggregated records, and you can be forced into an aggregate by records that arrived pre-summed.
Keep them apart.

They also fail differently, and the repairs are not the same.

Suppose the utility's zone meters record every zone separately, every hour, and always have.
If your representation still carries one town-wide demand number, that is **your** aggregation.
The information was there. You chose not to represent it, and you can choose otherwise this afternoon at no cost but effort.

Now suppose the opposite.
Suppose the zone meters were only installed in Lowfield, and Hillcrest's use has always been estimated by subtracting metered zones from the town total.
Then a Hillcrest demand figure exists in your representation, but the record behind it was produced by a process that does not measure Hillcrest at all.

That second problem does not go away by redrawing your representation.
It is a fact about how the numbers came to exist, and no amount of care in modelling will conjure a measurement that was never taken.

This chapter is about the first kind.
The second — why these records and not others came to exist, and in this form — is Chapter 4, and it is not a smaller problem.
The reason to separate them now is that they feel identical when you meet them and require entirely different responses.

### Task: do the arithmetic

Do this before reading on.
It is four lines and the point does not survive being read instead of done.

The case supplies, for 08:25 on day one:

| | Value |
|---|---:|
| Main reservoir | 9.3 ML |
| Hillcrest tank | 0.6 ML |
| Total verified storage | 9.9 ML |
| Treated-water input | 8.4 ML/day |
| Day-1 demand, whole town | 9.0 ML |
| Day-1 demand, Hillcrest only | 0.9 ML |
| Hillcrest duty pump capacity | 1.1 ML/day |

The case also supplies that Hillcrest's standby pump is under maintenance and unavailable for three days, and that the duty pump has just failed.

1. Using the whole-town numbers only, work out storage at the end of day one, and roughly how many days at that rate until the **4.5 ML** reserve.
2. Using the Hillcrest numbers only, work out how long the hilltop tank lasts with no pump.

### What the arithmetic says

**Whole town.**

`9.9 + 8.4 − 9.0 = 9.3 ML` at the end of day one.

Net drawdown is 0.6 ML per day.
From 9.9 ML to the 4.5 ML reserve is 5.4 ML, so roughly **nine days**.

Nothing about tomorrow looks urgent.

**Hillcrest.**

The tank holds 0.6 ML and the zone draws 0.9 ML per day. With no pump, nothing refills it.

`0.6 ÷ 0.9 = 0.67 days`, about **sixteen hours**.

Hillcrest is out of water tomorrow morning while total system storage is still above 9 ML.

### Pause: the aggregate arithmetic was correct

Before reading on, write two or three sentences on this:

> Both calculations are right. The town-level one is not an error. Why did it mislead?

The answer is not that the aggregate was wrong, and it is not that averages are bad.
The aggregate was computed correctly from correct facts, and for the question *will we breach the reserve this week* it remains the right calculation.

It misled because it was read against a question it cannot express.
The whole-town representation has one storage number and one demand number.
There is no Hillcrest in it. There is no *first* in it.
Asked who runs out first, it does not give a wrong answer — it gives no answer, and an aggregate that gives no answer looks exactly like an aggregate that says nothing is wrong.

### The same failure, from the other side

The aggregation also hides what to do.

Suppose the utility asks every customer in town to cut use by 10%.

System-wide saving: `9.0 × 0.10 = 0.9 ML per day`.
Saving in Hillcrest: `0.9 × 0.10 = 0.09 ML per day`.

Hillcrest's shortfall without its pump is 0.9 ML per day.
A saving of 0.09 ML per day does not touch it.

A representation with one demand number cannot even pose the question of where to target, because it has nowhere to target.

### Knowing which features mean something

Levins put the underlying difficulty better than anyone since.

In a familiar model, he wrote, we know which features carry meaning and which are artifacts: on a geographic map, "contiguity on the map implies contiguity in reality, relative distances on the map correspond to relative distances in reality, but color is arbitrary and a microscopic view of the map would only show the fibers of the paper on which it is printed."
The trouble is that in mathematical models "it is not always obvious when we are looking at too high a magnification" [@levins1966strategy, p. 423].

That is the skill this section is trying to build.
Not "use less detail" — but knowing which parts of your representation are load-bearing for the question and which are paper fibres.

### A note on words

Several words in this area are used loosely, and this book is deliberate about which it relies on.

**Abstraction**, **idealization**, **generality** and **aggregation** carry the weight, in the senses defined above.

**Grain**, **resolution**, **fidelity** and **scale** are used as ordinary careful language.
Grain and resolution both mean how finely something is represented; fidelity is the engineering word for the same idea.

**Scale** needs one more paragraph, because it is the word most often assumed to mean one thing.

A representation has a scale in at least four independent senses, and this book uses those four because they are a convenient way to interrogate a representation — not because they are an established taxonomy.

| Sense | For the utility | Change it and you can newly ask |
|---|---|---|
| Spatial | town / zone / street | which zone, then which street, runs short |
| Temporal | week / day / hour | what happens during the evening peak |
| Organizational | utility / department / operator on shift | who would actually have to act, and when they are on duty |
| Population | all customers / customer class / individual property | whether a hospital or a dialysis patient is among those losing pressure |

These move independently.
The representation you built is fine-grained spatially, coarse temporally, silent organizationally, and coarse by population.
That combination was chosen — or, more honestly, it was chosen for you the moment you decided the question was about zones and days.

The last row deserves a mark against it.
A representation that stops at "Hillcrest, 0.9 ML per day" cannot see that some customers in Hillcrest are affected differently by losing pressure than others.
That may be entirely correct for the decision at hand.
It is also exactly the kind of thing worth writing on the third line of your boundary note.

**Level** is avoided entirely.
It means level of detail, and organizational level, and the value of a variable, and in this chapter that is three meanings too many.

## 6. Three Representations of One Utility

You have built the pieces separately.
This section puts them side by side, because comparison is where the chapter's claim becomes checkable.

### Three representations

**Storage-only.** One tank, one inflow, one demand number. This is Chapter 1's.

**Treatment-and-demand.** Adds the treatment process, its permitted temporary output of **8.8 ML/day**, the **six-hour** production ramp-up, and the **$2,000 per day** incremental cost.

**Network by zone.** Adds three pressure zones, two tanks, the duty pump, and per-zone demand.

### Three purposes

1. Will the operating reserve be breached within seven days?
2. Can output be raised enough to matter, and at what cost?
3. If supply must be restricted, who loses service first?

### What each can answer

| | 1. Reserve in seven days | 2. Raise output? | 3. Who loses first? |
|---|---|---|---|
| **Storage-only** | **Adequate.** Contains exactly what the question needs | Cannot answer — no treatment process in it | **Cannot answer** — no zones, no *who* |
| **Treatment-and-demand** | Adequate, and adds the ramp-up delay | **Adequate.** Contains output limits, delay, cost | Cannot answer — still one demand number |
| **Network by zone** | Adequate, at more cost in effort | Partly — has zones but not the cost structure | **Adequate.** Contains zones, storage per zone, and the pump |

Read the first column and the last together.

The storage-only representation is **adequate** for purpose 1 and **cannot answer** purpose 3.
Its arithmetic was never wrong.
Nothing about it was sloppy.
The verdict on it flipped because the question changed underneath it.

That is the chapter's claim, and you have now watched it happen on numbers you checked yourself.

### What each one costs

Adequacy is not the only axis. Representations cost something to build and to keep.

| | What it needs | What it costs |
|---|---|---|
| Storage-only | one storage figure, one inflow, one demand forecast | almost nothing; a reader can check it in a minute |
| Treatment-and-demand | treatment limits, ramp-up time, cost data | modest; the numbers exist but must be maintained |
| Network by zone | per-zone storage, per-zone demand, pump capacity and status | substantial; needs zone metering and someone to keep it current |

This is why the storage-only representation is not simply an inferior version of the network one.
It is cheap, it is checkable by hand, and it answers a question the utility asks every week.
The network representation answers a question the utility asks rarely and hopes never to need.

Building the most detailed representation you can and using it for everything is not caution.
It is a standing cost paid to avoid making a choice.

### Task: find the simplification that flips

Before reading on, do this one. It is the chapter's competence in a single question.

Look at the storage-only representation and these two purposes:

- **Purpose A:** will the reserve be breached within seven days?
- **Purpose C:** if supply must be restricted, who loses service first?

Name **one specific simplification** in that representation which is defensible under Purpose A and indefensible under Purpose C.
Write one sentence defending it under A, and one sentence condemning it under C.

If you can only write the condemning sentence, you have not yet got the point.
The simplification has to be genuinely fine under the first purpose, or you are describing a mistake rather than a purpose-relative choice.

### This is how working scientists talk about it

Levins gives the cleanest historical version of the same flip.

Early population geneticists — Haldane, Fisher, Wright — assumed a constant environment, "although each author was aware that environments are not constant."
Levins's defence of them is not that they were approximately right.
It is that "the problem at hand was: Could weak natural selection account for evolutionary change? For the purposes of this problem, a selection coefficient that varies between .001 and .01 will have effects somewhere between constant selection pressures at those values, and would be an unnecessary complication" [@levins1966strategy, p. 422].

And then, in the next breath, the flip: "But, for us today, environmental heterogeneity is an essential ingredient of the problems and therefore of our mathematical models" [@levins1966strategy, p. 422].

The same simplification.
Legitimate for one question, not legitimate for another.
Levins's summary is worth keeping: the difference between legitimate and illegitimate simplifications "depends not only on the reality to be described but also on the state of the science" [@levins1966strategy, pp. 421–422].

### The plan had a representation too

Look again at the drought plan.

It supplies a **4.5 ML** system-wide operating reserve.
It contains no zone-level trigger at all.

That is not an oversight by careless people.
A plan can only contain triggers that its representation can express, and this plan was written against a single-tank picture of the town.
There is no zone in the representation, so there is no zone in the plan.

This is the most consequential thing in the chapter.
Representation choice does not stay inside the analysis.
It propagates into the plans, the thresholds, the dashboards, and the alarms that get built on top of it — and once it does, the thing the representation cannot see becomes the thing nobody is watching.

### Why you should build more than one

If a representation is chosen for a purpose, why not choose one and get on with it?

Because agreement across differently simplified representations is itself evidence.

Levins again: treat the same problem "with several alternative models each with different simplifications but with a common biological assumption. Then, if these models, despite their different assumptions, lead to similar results we have what we can call a robust theorem which is relatively free of the details of the model. Hence our truth is the intersection of independent lies" [@levins1966strategy, p. 423].

Take the last sentence in the sense he meant it.
It is a claim about conclusions that survive across models sharing a common assumption — not a general theory of truth, and not permission to build arbitrary alternatives and see what sticks.

In engineering practice the same habit shows up without the epigram: "it is common to use a hierarchy of models having different complexity and fidelity" [@astrom2008feedback, p. 32].

The practical version for you: if a conclusion holds in the storage-only and the network representation, you can lean on it. If it holds in only one, you have learned where to look next.

### Try it on the utility

Take three conclusions and check each against all three representations.

**"The town will not run out of water this week."**
Storage-only: supported. Treatment-and-demand: supported, more strongly, since output can be raised. Network: supported for the town as a whole.
Holds everywhere. Lean on it.

**"No action is needed before tomorrow."**
Storage-only: supported — nine days of margin. Treatment-and-demand: supported. Network: **contradicted** — Hillcrest has about sixteen hours.
Fails in one representation, and the one where it fails is the one built for the question actually being asked. This is not a tie to be split. It is a conclusion that survives only where the relevant distinction is invisible.

**"A town-wide conservation request is the right first move."**
Storage-only: supported, since there is one demand to reduce. Treatment-and-demand: supported. Network: **weakened** — the saving reaching Hillcrest is 0.09 ML per day against a 0.9 ML per day shortfall.
Not contradicted, but shown to be aimed at the wrong place.

The exercise takes ten minutes and it does something no single representation can do: it tells you which of your conclusions are artifacts of how you drew the picture.

### Changing your mind is not an admission

One last thing, because it stops people from doing this well.

When the purpose changes and you rebuild the representation, you have not confessed to an earlier error.
You have done the thing this chapter is about.

Chapter 1's single-tank representation does not become wrong when you draw the zones.
It becomes a representation for a different question than the one you are now asking.

### Task: diagnose five defects

Below are five short representation summaries.
Each contains one defect.

For each, write three things: the defect, what it stops the representation from answering, and a repair.

1. A colleague proposes representing every property in town individually. Asked why, they say it is more realistic than working in zones.
2. A diagram of the Hillcrest zone is captioned: *"Pump capacity is the cause of low pressure in Hillcrest."*
3. A briefing note reports that the town holds 9.9 ML against 9.0 ML daily demand, and concludes that supply is secure through tomorrow.
4. A representation of the utility is drawn to stop at the property line of the treatment works, on the grounds that this is where the utility's land ends.
5. A zone model lists as its state: main reservoir volume, Hillcrest tank volume, and total system storage.

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md) and compare.

## 7. Cold-Start Practice and Retrieval

### Return to your eight-minute sketch

Find what you wrote at the start of §1.

Do not score it.
Read it against three questions.

- Did you draw a boundary, and did you say why it was there?
- Did you say what would have to be carried forward?
- Did you distinguish what you left out from what you assumed?

Most first sketches contain parts and arrows and no boundary justification.
If yours did, that is the specific thing this chapter has added.

Two other patterns are common in opening sketches, and both are worth naming.

Some sketches list everything the writer knows about water utilities.
That is not a representation; it is an inventory, and it has no purpose to constrain it.

Others draw the answer rather than the machinery — a box labelled *Hillcrest fails* with arrows pointing at it.
That is a conclusion wearing a diagram's clothes.

Neither is a bad start.
Both are what happens when you are asked to represent something before anyone has told you that purpose does the selecting.

### Independent transfer

Now build representations for a system you have not seen, without the utility case, this chapter's checklists, or any worked answer in front of you.

You have been assigned **one** of the two forms below.
Open only that one.

- [Form A — Regional blood supply](transfer-form-a.md)
- [Form B — City rental-assistance programme](transfer-form-b.md)

Allow about **40 minutes**.
Every fact you need is supplied in the form; no specialist knowledge is required, and you should not look anything up.

Do not open the other form.
You will be asked to work it later, and it only tests anything if you have not seen it.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it dimension by dimension.

### Retrieve it from memory

Before you look back at the chapter, write down the questions you would ask in order to build a representation of anything.

Aim for the sequence, not the wording.
Then compare with what you produced and repair what you missed.

For reference, after you have tried:

1. What is the purpose, stated precisely enough to constrain what goes in?
2. What is the target system, and where is the boundary — what is one thing inside and one thing deliberately outside?
3. What are the parts, what does each do, and what role does each play?
4. What must be carried forward, and does each candidate pass the state test?
5. At what grain, and what does that grain make answerable and unanswerable?
6. For which phenomenon is a mechanism being drawn, and what has drawing it established?
7. What is omitted, what is asserted falsely, and what is lumped together — and what defends each?
8. What would a different representation of this same system make easy, or impossible?

Do not memorise the wording.
The order matters more than the phrasing, and the first question matters more than the other seven, because everything after it is decided by the answer.

### If the transfer task went badly

It often does, the first time, and the useful thing is to find out in which specific way.

- **You produced one representation instead of two.** The purposes were not distinct enough in your mind to force different content. Go back and write the two purposes as two sentences before drawing anything.
- **You produced two drawings but could not name a simplification whose verdict flips.** This is the most common outcome and the most informative. You varied the pictures without varying what they are for.
- **You drew a mechanism and wrote that something causes something.** Reread the four signs. Ask what intervention would have had to happen.
- **You could not decide what counted as state.** Ask what you would need to write on a card tonight so that someone else could carry on tomorrow morning.
- **You ran out of time on detail.** Look at where the detail went. It usually went somewhere the stated purpose did not require.

None of these is a failure of intelligence.
Each is a specific missing move, and each has a specific repair.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Between now and then, do not reread this chapter immediately beforehand, and do not look at the form you have not done.
The point of the delay is to find out what survived it.

### What Chapter 3 asks next

You can now build a representation and say what it can answer.

Your representation of the utility contains a quantity called *Hillcrest demand*, measured in megalitres per day.
This chapter has said a great deal about whether that quantity belongs in the representation and at what grain.

It has said nothing about whether the number attached to it means what you think it means.

Where does that number come from, what exactly does it stand for, and how well?
That is Chapter 3.
