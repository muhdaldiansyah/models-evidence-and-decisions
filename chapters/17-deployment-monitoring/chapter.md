---
chapter: 17
part: 5
title: "Deployment, Monitoring, and Revision"
status: drafted
---

# Chapter 17: Deployment, Monitoring, and Revision

## 1. Eighteen Months Later

Chapter 16 ended by saying that its analysis was a photograph of a system that was moving while it was photographed.

**Sixteen chapters have built things.** A representation, a set of estimates, a portfolio, a rule, a routing record. **Not one of them has asked whether a built thing is still working**, and that question is the whole of this chapter.

### The water case comes back, for the last time

Chapter 16 set the water utility aside deliberately, because a chapter about unfamiliar problems cannot be taught on the most familiar one.

**It returns here, for its thirteenth and final appearance**, and it returns in order to have its own Chapter 12 output examined.

### Before reading further

Here is the adaptive plan Chapter 12 wrote, quoted unchanged.

> **Watch.** Peak-week demand against the Chapter 1 forecast, reported each September. Heat events per year, already counted for the regulator.
>
> **If.** Peak-week demand exceeds the forecast by more than four per cent in two consecutive summers, **or** heat events exceed six in a single year, stage 2 of the trunk reinforcement enters the following year's programme at an assumed **£1,150k**.
>
> **Owner.** The asset planning lead reports both signposts to the capital committee each October, whether or not either has triggered.

**Four years have passed.
Here is what happened.**

| Year | Peak-week demand vs forecast | Heat events |
|---|---:|---:|
| 2023 | +1.8% | 4 |
| 2024 | **+5.2%** | 5 |
| 2025 | +2.9% | **7** |
| 2026 | **+4.6%** | 5 |

**Allow about twelve minutes and write two things down.**

**What should the October report have said, each year?**

**And what, in this plan, would have counted as a signal?**

Do this before reading on.
The second question is where the chapter lives, and §3 will make it harder than it currently looks.

### Why this chapter is last

There is a reason this comes at the end rather than after Chapter 5, where the questions first appear.

**You cannot ask whether a deployed thing is still working until you can say what it was supposed to do**, and that took Chapters 1 to 3. **You cannot say which stage a failure entered through** until the stages exist, which took until Chapter 15. **And you cannot tell a signal from ordinary variation** without Chapter 8's habit about spreads.

**So this chapter is short because most of it was built elsewhere.** What is genuinely new here is four pages long, and the rest is sixteen chapters pointed at a thing that is already running.

### What you will be able to do

Say whether a threshold is a **trigger** or a **timer**, which is four lines of arithmetic and is almost never done.

Tell a **signal** from **ordinary variation** — and know that neither can be recognised without a baseline.

Say what a monitoring arrangement can see and what it constitutionally cannot, which is a different question from whether it is well designed.

Diagnose a failure by the stage it **entered** through rather than the stage it **appeared** in, which are usually far apart.

And know that a deployed thing is not a thing that was checked.
It is a thing that has to be checked again, each time it is used.

## 2. Deployment Is Not a State

The activity has a name in this book and the book has already defined it, in a place most readers will not have looked.

**`monitoring`** is what `canon/terminology.md` records, under Chapter 8's `model checking`, as "**the same activity after the model is in use**."

**That is a smaller distinction than it sounds, and the chapter should not inflate it.** The questions are the ones Chapter 5 asked: does this still do what it was built to do, and what would show that it does not.

**Three things change, and none of them is the method.**

**The stakes.** Something is now running on it.

**The audience.** The people who will read the answer did not build the thing and may not know what it was for.

**And somebody has to be assigned.** Chapter 12 established that a signpost without an owner is a diary entry; **an indicator nobody is named against is not monitored**, whatever the dashboard says.

### What "deployed" means in a standard that says so

There is a NASA standard for models and simulations, and it is unusually clear about the boundary this chapter sits on.

Its life cycle has two halves:

> "The life cycle of a model or simulation, like that of any system, has two general parts: M&S development, which includes M&S initiation, concept development, M&S design, M&S construction, and M&S testing; and M&S application, which includes use (or operation) and M&S archiving (including the associated artifacts, products, and analysis performed during a specific use)." [@nasa2024models, p. 86]

**Chapters 1 to 16 of this book are the first half.
This chapter is the second.**

And release is not a certificate:

> "This testing identifies the M&S' limits of operation, i.e., where the M&S is known to work correctly (i.e., verified and validated). At the end of M&S testing, the M&S' capabilities, assumptions, and limits of operation are recorded and assessed with respect to acceptance criteria to determine the permissible uses of the M&S." [@nasa2024models, p. 87]

> "Once M&S testing is successfully completed, the M&S is released, along with guidance of the M&S' capabilities and domain of permissible use, ending M&S development." [@nasa2024models, p. 87]

**`permissible use`** is the domain within which the thing has been shown to work — **and it is a property of a pairing**, a model with a proposed application, rather than of the model.

**That is the fourth time this book has met that shape.** Chapter 3's `validity` was a property of an interpretation.
Chapter 9's `transportability` was a relation between a study and a target.
Chapter 14's `observability` was a property of a system paired with instruments.
Each time, a word that sounds like a badge turns out to be a relation, and each time the failure is the same: somebody asks whether the thing is good, when the question is whether it is good **for this**.

### The sentence this chapter turns on

> "During the use (or operations) phase, the M&S may or may not be used by those who developed it. In both cases, and especially the latter case, the use of an M&S starts with an assessment of whether or not the proposed use of the M&S sufficiently matches the permissible use." [@nasa2024models, p. 87]

And then, more strongly:

> "Each application of the M&S restarts the M&S use/operation with an assessment of permissible uses against the needs of that specific proposed use." [@nasa2024models, p. 87]

**Each application restarts.**

**Deployment is not a state.
It is a repeated act.**

A model that was validated is not thereby a model that is validated for what somebody is about to do with it this morning, and the standard puts the check at every use rather than at release.

**That is a demanding requirement and most organisations do not meet it.** What most organisations have is a decision, taken once, that the thing is approved — after which the question of whether this particular use is inside the domain never arises again, because nobody is asked.

### And a third option worth having

When a proposed use is outside the domain, the standard does not offer two choices:

> "If the proposed M&S use does not meet the defined permissible use, the proposed use will either be rejected or possibly allowed with the appropriate restrictions, caveats, or placarding required." [@nasa2024models, p. 87]

**Placarding.** A label attached to the thing, travelling with it, saying what it is not for.

**Between refusing a use and permitting it silently there is a third thing**, and most organisations have only the first two.

### Revision triggers, in two directions

Chapter 12 gave you signposts: an observable quantity, a threshold, an owner, and a frequency.

**A `revision trigger` is the same object with one addition**, and the standard supplies it in a sentence about record-keeping:

> "maintenance of the record implies that the outcome or product is re-established as a result of any changes to either the RWS or the M&S." [@nasa2024models, p. 18]

**Changes to the world, or changes to the model.**

**Chapter 12's signposts watch only the first.** Peak-week demand and heat events are facts about the world.
Nothing in that plan fires when somebody revises the demand forecast the plan is measured against — and somebody will, because forecasts are reissued.

### Task: a change to the model

Name one change to the water utility's *analysis* — not to the weather, not to the network — that should reopen the Chapter 12 plan.

Two minutes.

## 3. Signal, or Ordinary Variation

Before the case, something about what this chapter is not going to do.

**The book's own architecture permits more machinery here than the chapter uses.** The Chapter 17 entry says that concept-level monitoring machinery "may include common-cause versus special-cause variation and control-chart reasoning where appropriate" — the only permissive clause of its kind in the book.

**The chapter takes the distinction and declines the charts.**

**Specifically declined:** centre lines, control limits, run rules, chart types, sampling plans, and every named chart.
Those are one apparatus for applying a distinction, and the governed competence names the distinction.

**That is a choice and it could have gone the other way.** The reason it did not is that adding the apparatus would have made this the only chapter in the book to teach a technique it does not then use on its own case.

### Why this is the chapter's most portable idea

Most of what this book contains is tied to a stage.
Identification belongs to a causal question, optimisation to a constrained one, strategic response to a system with people in it.

**This one attaches to any number anybody proposes to act on.**

Somebody says: if this exceeds forty, we escalate. **The question is always the same** — what has this been, when nothing in particular was happening? — and it is usually answerable from records already held, in minutes, by anybody.

**And it is almost never asked**, for a reason worth naming: a threshold arrives in a document as a decision that has already been made.
It is in the plan, the plan was approved, and asking where the number came from feels like reopening something settled rather than like checking an input.

**The check is small enough to do anyway**, and §4 shows what four years of not doing it looks like.

### The distinction, and where it comes from

The apparatus is called statistical process control, and its origin is not in doubt:

> "The concept of Statistical process control (SPC) was given by the physicist Walter Shewhart in order to improve the industrial manufacturing." [@sumanprajapati2018control, p. 1]

> "The SPC is based on theory of variation i.e., common and special causes of variations." [@sumanprajapati2018control, p. 1]

**Shewhart's own 1931 book could not be obtained**, so both sentences are quoted from a review that could be — the same arrangement this book has used since Chapter 6.

### Two words

**`Ordinary variation` is what a process produces when nothing in particular is happening.**

It has a range, and that range is **a fact about the process**, measurable before anything goes wrong.
The field's terms for the two kinds are *common cause* and *special cause*; this book says ordinary variation and signal, because the reader will meet both pairs and only one of them is self-explanatory.

**A `signal` is a value that ordinary variation does not readily produce.**

**Which means a signal cannot be recognised without a baseline.** Not a threshold — a baseline.
A threshold is somebody's number; a baseline is what the process actually did.

### Now the utility's baseline

The utility had seven years of both series before the plan was written, and neither appears anywhere in the Chapter 12 papers.

**Peak-week demand against the Chapter 1 forecast:**

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---:|---:|---:|---:|---:|---:|---:|
| +0.4% | −1.2% | +2.1% | −0.8% | +1.6% | +3.3% | −0.5% |

**Mean +0.70%. Standard deviation 1.55. Maximum +3.3%.**

**Heat events per year:**

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 5 | 2 | **7** | 4 | 3 | 5 |

**Mean 4.14. Standard deviation 1.55. Maximum 7.**

### Pause: is seven a signal?

Heat events reached **seven** in 2025, and the plan says the trigger fires when they exceed six.

**Is seven a signal?**

Write an answer, with a reason, before reading on.
Two minutes.

### One limb was a trigger. The other was a timer.

**The demand limb.** Four per cent sits **2.12 standard deviations** above the baseline mean, and **was never reached in seven baseline years.** A value past it is genuinely unusual.
That is a threshold doing what a threshold is for.

**The heat-events limb.** "Exceeds six" fires on seven — **and seven occurred once in the seven baseline years.**

**That is a rate of one in seven per year.** Over the fifteen-year horizon the plan was written for, it is **2.1 expected firings from baseline variation alone**, whether or not anything changes.

**A threshold set inside the range of ordinary variation is not a trigger.
It is a timer.**

It will fire eventually regardless, and the interval between firings is a fact about the process rather than about the world.

**And the 2025 value of seven, specifically, sits 1.84 standard deviations above the baseline mean and equals the baseline maximum.** It is not evidence that anything has changed.
It is the sort of year the utility has already had.

### What a baseline is not

Three things a baseline is not, because each is what gets substituted for one.

**It is not a target.** The utility's operating target is 220 ML; that is what somebody decided should happen.
A baseline is what did happen, whether or not anybody wanted it.

**It is not a forecast.** The Chapter 1 demand forecast is a prediction; the baseline here is the record of how far that prediction was out, year after year, which is a different object and the more useful one for this purpose.

**And it is not the whole history.** Seven years is enough to see a range and not enough to see a rare event. **A baseline tells you what ordinary looks like; it does not tell you what the worst case is**, and a threshold set to fire only outside seven years of experience will be silent through the eighth-year event nobody has seen.

**Which is the cost the reader task at the end of this section is about.** A threshold far enough out to avoid being a timer is also far enough out to be late, and there is no setting that avoids both.

### Four lines of arithmetic

**Everything above comes from seven numbers the utility already held**, twice, and it took four lines.

**Nobody did it.** Not when the plan was written, not in any of the four October reports, and not in the committee minute.

**And this book is implicated.** Chapter 8 gave you the habit — a number carries a spread, and a threshold verdict discards most of what the number contains.
Chapter 12 then wrote two thresholds without checking either against a baseline, and said in its own text that the numbers were "arguable, and being arguable is the property that matters."

**This is the argument.** It was available nine chapters earlier and it was not made.

### Task: a threshold that would be a trigger

Set a heat-event threshold that would be a trigger rather than a timer.

Say what value you chose, why, and **what it costs** — because a threshold that never fires on ordinary variation also fires late on real change.

## 4. A Trigger That Was a Timer

Now what actually happened.

| Year | Demand vs forecast | Heat events | The October report |
|---|---:|---:|---|
| 2023 | +1.8% | 4 | Neither signpost triggered |
| 2024 | **+5.2%** | 5 | Demand exceeded four per cent; not two consecutive summers; no trigger |
| 2025 | +2.9% | **7** | **Heat events exceeded six** |
| 2026 | **+4.6%** | 5 | Demand exceeded four per cent; not consecutive with 2024; no trigger |

### The demand limb never fired, and Chapter 12 said it might not

**Demand exceeded four per cent in two of the four years — and never in consecutive ones.**

Chapter 12 wrote, in the paragraph headed *What this plan gives up*:

> If demand jumps in a single year rather than two, stage 1 will be inadequate and the trigger will not have fired.

**The rule behaved exactly as written, and exactly as its author warned.** That is not a failure of the signpost.
It is the cost that was named when it was designed, arriving.

### The heat limb fired, and nothing happened

**In 2025 heat events reached seven.** The threshold was six.
The report recorded it.

**The committee minute reads: "signposts reported; no action required."**

The plan says stage 2 "enters the following year's programme at an assumed £1,150k".
It did not.

### Pause: what should the committee have done?

You have the plan, the four years, and §3's baseline.

**What should the committee have done in October 2025?**

Three minutes, before reading on.

### Why nothing happened, and it is not carelessness

The report presented both signposts on one page, as the plan required.

**One limb had been watched closely for two years and had not fired.** Everybody in the room had been following the demand figure since the +5.2% in 2024, and everybody knew it needed a second consecutive year.

**The heat figure was the other line on the page.**

**And the rule said "or".**

**It was read as "and".**

That is a documented failure mode of written rules and it needs no unusual carelessness to produce.
A disjunction reported alongside a conjunction-like expectation gets read as the thing the room was already thinking about.

### And now the uncomfortable part

**Given §3's arithmetic, not acting was defensible.**

Seven heat events is a one-in-seven-year value that had already occurred once in the baseline.
Committing £1,150k on the strength of it would have been acting on ordinary variation.

**So the committee reached a defensible answer.**

**And nobody in the room could have said so**, because nobody had the baseline — and the reason they reached it was that they misread a two-line rule.

**A right answer reached by misreading is not a right answer.** It is an accident that will not repeat, and the next time the limb fires the same room may act on it for exactly the same reason it did not this time.

### What a report would have to look like

The October report did what the plan asked: it presented both signposts, whether or not either had triggered.

**Three things would have made the misreading unavailable**, and none of them requires a new system.

**State the rule's logic in the report, not just its result.** "Either limb triggers on its own" is seven words, and it removes the ambiguity the room supplied.

**Report each limb's status separately and finish each with a verdict.** *Demand limb: not triggered.
Heat limb: triggered.* Two lines that cannot be read as one.

**And state what happens next, in the report rather than in the plan.** The plan says stage 2 enters the following year's programme.
The report said the value. **The distance between those two sentences is where four years went.**

**None of this is governance.** It is how one page is laid out, and the plan — which specified an owner, a frequency, and a threshold — did not specify it.

### The word for acting on ordinary variation

**`Tampering` is adjusting a stable process in response to variation that was always there.**

The mechanism is Chapter 13's, and Chapter 13 sourced it:

> "decision makers often continue to intervene to correct apparent discrepancies between the desired and actual state of the system even after sufficient corrective actions have been taken to restore equilibrium. The result is overshoot and oscillation" [@sterman2006evidence, p. 508]

**Chapter 17 adds the precondition.** Chapter 13's overshoot came from correcting through a delay, after enough correction had been applied. **Tampering is worse: if the discrepancy you are correcting is ordinary variation, then every correction is an overshoot, because there was nothing to correct.**

**A committee that acted on every firing of the heat limb would be tampering.** Not because £1,150k of trunk main is a bad idea, but because the thing prompting it would be the weather doing what the weather does.

*One note on the word.* **`tampering` is named in this book's architecture and no source for it was obtained.** The mechanism is sourced — the passage above — but the name is the book's own, and the chapter's decision record says so rather than letting the term look better attested than it is.

### Task: rewrite the rule

Rewrite the plan's **If** clause so that it cannot be read as a conjunction.

One sentence.
Then say what else you would change about it, given §3.

## 5. What Monitoring Cannot See

Chapter 16 left an automated tool running. **Eighteen months of monitoring later, here is what the authority was looking at.**

| Indicator | 2022 | 2024 | Read as |
|---|---|---|---|
| Weekly job volume | 1,180–1,290 | 1,180–1,290 | stable |
| Repairs completed within target time | 94.1% | **95.6%** | **improved** |
| Tenant satisfaction | 81% | 82% | flat |

**All three reported monthly to the housing committee.
All three fine or better.**

**And the completion figure improved for a reason.** Routing more jobs as emergencies gets them attended sooner, and attended-sooner is what that target measures. **The indicator moved in the right direction *because of* the thing that was wrong.**

### Why these three indicators, and why they were reasonable

It is worth saying that these were sensible choices, because the reflex on seeing a monitoring failure is to assume the monitoring was thoughtless.

**Volume** tells you whether demand on the service has changed. **Completion within target** is the authority's statutory performance measure, and it is what it is judged on. **Tenant satisfaction** is the outcome the service exists for, asked of the people who receive it.

**Between them they cover input, process, and outcome**, which is the shape a competent monitoring designer would produce and roughly what any textbook would recommend.

**And all three moved in the right direction or not at all**, throughout a period in which the thing being monitored was going wrong.

**That is the finding, and it is not about these three indicators.** Any three output measures would have done the same, because the failure was upstream of every output.

### The number nobody reported

| | 2022 | 2024 | Change |
|---|---:|---:|---:|
| Emergency jobs | 4,180 | 5,100 | +22% |
| Statutory hazard referrals | 612 | 631 | +3.1% |
| **Ratio** | **6.83** | **8.08** | **+18.3%** |

**Both numbers were collected.** Emergency jobs by the repairs team.
Statutory hazard referrals by environmental health.

**Neither team reported the ratio, because the ratio is nobody's report.**

**That is the second time this book has arrived at exactly that sentence.** Chapter 15's utility had a count and a complaint volume that met only in a ratio nobody owned, and the ratio moved for four years unnoticed. **Same shape, different organisation, and it is worth noticing that the shape is about how organisations divide work rather than about anybody's competence.**

### Drift, and why detecting it is not diagnosing it

A monitoring arrangement that watches for change will eventually see some, and **seeing it is less useful than it feels.**

> "When ignored, performativity surfaces as undesirable distribution shift, routinely addressed with retraining." [@perdomo2020performative, Abstract]

> "Performativity therefore suggests a different perspective on retraining, exposing it as a natural equilibrating dynamic rather than a nuisance." [@perdomo2020performative, §1]

**`Drift` is a change over time in the relationship a deployed thing depends on.** Detecting it tells you the world and the model disagree. **It does not tell you which one moved, or why, or whether refitting is maintenance or convergence toward somewhere nobody wants.**

**And there is one instrument in this book that produces a signal automatically.** Chapter 6's calibration: a forecast that was calibrated over its first two years and is not over its third has told you something without anybody deciding to look.
Nothing else in these sixteen chapters does that unprompted.

### And the other thing monitoring cannot see

There is a second blind spot, quieter than the first, and Chapter 15 named its mechanism.

**Monitoring watches what somebody decided to watch**, which means the choice of indicator is itself a decision made at a particular time by particular people with particular concerns.

**The authority chose volume, completion, and satisfaction in 2022**, before the tool existed, for a service run by schedulers. **Nothing in that set was chosen with an automated router in mind**, and nothing in it would be.

**So the monitoring is answering questions from the previous arrangement.** It is not wrong; it is dated, in the specific sense that its subject changed and its indicators did not.

**This is the same shape as §2's permissible use**, arriving about the monitoring rather than the model: the indicators were validated for a service, and the service is not the one they are now watching.

### The claim this chapter exists for

**Monitoring observes outputs.**

**So it detects failures that change outputs, and is constitutionally incapable of detecting failures in what the thing was built to represent — because those produce outputs that look right.**

| Failure enters at | Would monitoring show it? |
|---|---|
| 1 — the question | **No.** Everything downstream answers the wrong question competently |
| 3 — what a number stands for | **No** |
| 4 — why the records exist | **No.** Outputs match the label by construction |
| 7 — identification | **No.** Predictions can be fine |
| 8 — estimation | Sometimes, and late |
| 13 — dynamics | **Yes.** Waiting times move |
| 15 — strategic response | **Yes, if the right ratio is watched** |

**The early stages are invisible and the late ones are visible.**

That is the reverse of where attention goes.
Monitoring is designed at the end of a project, by people thinking about outputs, and the failures it cannot see were installed at the beginning by people thinking about something else.

## 6. Diagnosis by Stage

### Pause: where did it enter?

The symptom in Case 2 is a queue: emergency jobs up 22% against a fixed servicing capacity.

**Where did the failure enter?**

Two minutes.

### Chapter 4. Nine stages and eighteen months earlier.

**The tool was trained on a label that is a scheduler's decision**, which Chapter 16 established at its identification stage and which nothing in eighteen months of monitoring could have revealed.

**A failure is diagnosed where it entered, not where it was noticed**, and the two are usually far apart.

### The counterpart of Chapter 16

**Chapter 16 routed forward from a problem**: which of these fifteen stages does this need?

**Chapter 17 routes backward from a symptom**: which of these fifteen stages did this enter through?

**Same categories, opposite directions**, and the second is harder only because by the time you are doing it, something has already gone wrong and somebody wants it fixed by Friday.

### Why this direction is harder than Chapter 16's

Routing forward and routing backward use the same categories, and the second is harder for three reasons that have nothing to do with the categories.

**Something has already gone wrong**, so the work is being done under a pressure Chapter 16's was not.

**Somebody is at fault, or believes they will be found to be.** The people who can tell you what the label was are the people who chose it, and diagnosis-by-stage lands on their stage.

**And the evidence is worse than it was at the start.** Eighteen months of operation have produced records shaped by the thing being diagnosed — Chapter 4's problem, arriving about the diagnosis itself.

**The defence against all three is to do the diagnosis before anything has gone visibly wrong**, which is what §5's table is for: it can be filled in on the day of deployment, and the rows marked "no" are the ones to check by other means.

### And the monitoring was not inadequate

**No arrangement could have caught this.** A tool that reproduces its label produces outputs that look right by construction, and the authority's three indicators were reasonable choices reported reliably.

**Saying so matters**, because the reflex after a failure is to add indicators.
Adding a fourth output measure to this system would have detected nothing, and it would have felt like a response.

### One sentence from the standard

The book's own specification called treating the teaching order as a waterfall a major category error, and Chapter 16 worked two backward revisions to show it.

Here is a standards body on the same point:

> "The classic waterfall life cycle is idealized as a linear flow, though reverse-flow loops to previous phases are possible (even expected) if problems in M&S development or use occur." [@nasa2024models, p. 88]

**Possible, even expected.**

### Task: diagnose five defects

Each statement below contains one defect — **except that one of them correctly identifies a monitoring gap and then proposes a monitoring fix for a failure no monitoring could catch**, which is a different kind of failure and the one this chapter exists to prevent.

Write the defect, what it stops you concluding, and a repair.

1. *"Heat events exceeded six, which is what the plan said to watch for, so the trigger fired correctly."*
2. *"The committee didn't act on a fired trigger. This is a governance failure and needs a stronger escalation process."*
3. *"All three monitored indicators were stable or improving, so the tool was working."*
4. *"We missed the emergency-jobs problem because we weren't monitoring the right things. We should add the ratio to the monthly pack."*
5. *"The model was validated before deployment, so what we need now is periodic revalidation on a schedule."*

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md).

## 7. Retirement

There is one more item, and this book has not mentioned it once in sixteen chapters.

> "A plan for the acquisition, development, operation, maintenance, and retirement of the M&S (including identifying the responsible organizations) shall be maintained." [@nasa2024models, p. 39]

**Five verbs.
This book has discussed four of them.**

**`Retirement` is the planned end of a working life**, and the standard requires a plan for it at the same level as acquisition — with the responsible organisation named, which is the same discipline Chapter 12 applied to signposts.

**And notice what the requirement implies about everything before it.** A plan that names a retirement condition is a plan that admits the thing will stop being right — which is a different posture from the one most model documentation takes, where the model is correct and the documentation explains why.

**Almost nobody has one.** Models are commissioned, built, validated, deployed, monitored, occasionally revised, and then they continue — through staff changes, through the departure of everybody who knew what they were for, through reorganisations that leave nobody able to say who owns them.

**A model nobody has retired is not thereby still fit for use.** It is a model nobody has looked at.

**And the check is the one from §2**, asked once more: is this use inside the domain the thing was released for? A model that has been running for eleven years is being used by people who were not there when that domain was written down, on problems that were not in it.

**Retirement is what you plan so that the answer is not always no by default.**

## 8. Cold-Start Practice, and What This Book Has Not Established

### Return to your twelve-minute answer

Find what you wrote in §1 and compare it with §§3 and 4. **Do not score it.**

**Did you check the thresholds against anything?** Most first answers assess the values against the thresholds, which is what the utility did and what produces a right answer to the wrong question.

**And did you notice the "or"?** If you read the rule correctly on a cold reading, you did something four October reports and one committee did not — which says more about how rules are read in rooms than about you.

### Independent transfer

Now work an unfamiliar situation, without this chapter or its cases in front of you.

You have been assigned **one** of the forms below.
Open only that one.

- [Form A — A water company's leakage programme and its automated controller](transfer-form-a.md)
- [Form B — A school trust's attendance plan and its automated absence flag](transfer-form-b.md)

Allow about **50 minutes**.
Every fact you need is supplied.
Do not look anything up.

Do not open the other form.
You will work it after a delay.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it.

### Retrieve the procedure from memory

Close the chapter.
From memory, write the five steps.

1. **Get the baseline** for anything you intend to set a threshold on. Seven numbers is usually enough to tell a trigger from a timer.
2. **Check every threshold against it.** A threshold inside the range of ordinary variation is a timer.
3. **Ask what the monitoring can see** — and list the stages it cannot, which will be the early ones.
4. **Write a revision trigger in both directions**: what change in the world, and what change in the model.
5. **When something goes wrong, diagnose where it entered**, not where it appeared.

Check against §§2–6. Steps 1 and 3 are the ones people drop.

### If the transfer went badly

If you assessed values against thresholds without a baseline, reread §3. It is four lines of arithmetic and it is the chapter's most portable result.

If you proposed better monitoring for a failure that entered at an early stage, reread §5 — and note that this is the defect the diagnosis task singled out, because it is the one that feels most like a solution.

### Delayed retest

After at least a week, work the other form.
Do not reread this chapter first.

---

### What this book has not established

This is the last section of the last chapter, and it is not a summary.

**No pilot data exists for any exercise in this book.** Every chapter's transfer design carries a line forbidding a claim of durable far transfer, and every one of those lines is still true.
The two studies underlying the exercise architecture were verified at abstract level and neither was read in full.

**Gate 1 has been open since Chapter 1.** The water-utility anchor — which has now appeared in thirteen chapters and finished its work in this one — has never been reviewed by a subject-matter expert.
Everything built on it is internally consistent and externally unchecked.

**Sixteen decision records are unadjudicated.** Every chapter from 2 to 17 rests on a proposed record that no author has ruled on, and the terminology, scope boundaries, and example architecture of all sixteen inherit that status.

**One registry entry does not close.** `utility` is recorded as belonging to Chapter 11, Chapter 11 did not define it, and **there is no later chapter to close it in.** It was noticed in Chapter 13's research and has been carried forward four times since, which is what an open item looks like when the chapters run out.

**And three concepts in this book rest on sources it could not obtain**, quoted instead through works that could be: Goodhart, Campbell, and the categorization finding this book's own triage chapter is built on.

### What the book does claim

Against that list, it is worth being precise about what is left, because it is not nothing.

**Every claim in these seventeen chapters that rests on a source has a locator, and every locator was taken from reading the document.** Where a source could not be obtained, the book says so and names what it used instead.
Where a quotation would not survive being lifted from the page, it was paraphrased and the paraphrase was declared.

**Every case figure was computed before it was written**, and the arithmetic is in each chapter's frozen case data where anybody can check it.

**And where the book departed from its own architecture, it recorded the departure** rather than smoothing it — a term registered outside a governed competence, a pagination rule bent twice, a concept taught from a review, a name with no source at all.

**That is a claim about method rather than about effect**, and it is the only kind this book is in a position to make.

### The last item

Section 7 named five verbs and observed that this book had discussed four.

**The fifth was retirement**, and the observation applies to the book as much as to anything in it.
Nothing here says when a chapter's account should stop being used, what would show that it had, or who would notice.

**The honest close is that the reasoning in this book is deployed the moment somebody uses it**, which puts it under §2's requirement rather than outside it: each application restarts the assessment, and the domain of permissible use is whatever a reader can establish for the problem in front of them.

**That is not a modest ending chosen for effect.** It is the same standard the book has applied to a reservoir, a pump, a portfolio, a rule, and a tool that scored repairs — applied, finally, to itself.
