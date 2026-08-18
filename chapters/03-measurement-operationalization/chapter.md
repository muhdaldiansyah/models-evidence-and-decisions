---
chapter: 3
part: 1
title: "Measurement and Operationalization"
status: drafted
---

# Chapter 3: Measurement and Operationalization

## 1. The Number and the Thing

In Chapter 2 you built a role table for the water utility's zones.
One of its rows read:

| Part | What it does | Role | Grain |
|---|---|---|---|
| Zone pressure | what customers experience | observed | per zone, **adequate or not** |

Look at the last two words.

They carry a decision, and Chapter 2 walked past it deliberately.
*Adequate* is not something you read off an instrument.
Somebody has to decide what it means before any instrument can report it.

The utility's drought plan has the same gap.
It requires that service pressure remain **"adequate"** and never says what that is.

That is not negligence, and this chapter will not treat it as such.
It is the normal condition of a word everybody believes is obvious.

### Before reading further: define it

Take about **six minutes**.

Write a definition of *adequate service pressure* precise enough that two people, measuring independently, would get the same answer.

Do not look ahead.
Keep what you write; you will come back to it at the end of the chapter.

---

Whatever you wrote, you made at least three choices.

**Where** the pressure is measured.
**When** it is measured.
**How much** counts as enough.

Most requirements written in the world make none of those three explicit, and most people reading a number that resulted from them never learn which choices were made.

That is this chapter's subject.

It is worth seeing straight away that the problem is not about water.

*Waiting time* sounds like something a clock settles, until you ask whether the clock starts when a patient arrives, when they are booked in, or when someone first assesses them — three defensible answers that produce very different numbers from the same afternoon.

*Unemployment* sounds like counting, until you ask whether someone who has given up looking is unemployed, and whether four hours of work a week counts as employed.

*Air quality* sounds like a sensor reading, until you ask which pollutant, averaged over what period, measured where in the room.

In each case the word feels solid, the number arrives looking definite, and the decision that produced it happened somewhere nobody is looking.

Chapter 2 asked which quantities belong in a representation and at what grain.
It settled that *Hillcrest demand* belongs, at zone level, per day.
It said nothing whatever about whether the number **0.9** attached to that row means what you think it means.

> What does a number stand for, and how well?

By the end of this chapter you should be unable to write a figure into a representation without asking what procedure produced it, what that procedure decided on your behalf, and what the resulting number can and cannot be interpreted as.

### Why these failures are hard to see

One more thing before you start, because it explains why a whole chapter is needed for something that sounds like carefulness.

Measurement failures do not announce themselves.

A representation that leaves something out at least leaves a visible hole — Chapter 2's aggregate could not answer *who loses service first*, and you could tell, because there was no *who* in it. A measurement failure produces a number. The number has the right units, sits in the right column, moves plausibly over time, and is very often correct about something.

It is simply correct about something other than what you are reading it as.

So there is nothing to notice. The dashboard does not blink. Nobody files a complaint, because the people affected are not in the record. And every downstream calculation — the representation, the plan, the threshold, the report — inherits the problem silently and adds its own confidence to it.

That is the shape of nearly every failure in this chapter. Not a wrong number in an obvious sense. A right number, read as an answer to a question it was never measuring.

## 2. From Construct to Score

### Four rungs

Between a thing you care about and a number on a page there are four steps, and most measurement arguments happen at the second one without anybody noticing.

> **construct → working definition → measure → score**

A **construct** is the thing you are trying to measure.
Adequate service pressure. Storage. Waiting time. Air quality.

A **working definition** is the specific formulation you adopt for this analysis — usually one explicit sentence.

A **measure** is the procedure that produces numbers or classifications.

A **score** is what the procedure returns for a particular case.

This ladder is adapted from a four-level scheme in the measurement-validity literature, where the rungs are called the *background concept*, the *systematized concept*, the *indicator*, and the *scores for cases* [@adcock2001validity, p. 530].
Those are the source's terms and this chapter will not use them again; *working definition* says the same thing in plainer language and carries a useful hint, which is that the definition is revisable.

One boundary is worth taking from that source directly.
Measurement, as it defines the word, covers "the interaction among levels 2 to 4" [@adcock2001validity, p. 530] — the working definition, the measure, and the scores.

Arguing about what *adequate* ultimately ought to mean, in general, for all utilities, is a different activity.
It is a dispute about the concept, and it is not measurement.
Chapter 3 is about the three lower rungs.

### Telling a construct from a working definition

The most common failure with this ladder is believing you are on rung two when you are still on rung one.

A loose idea can be surprisingly articulate. "Adequate pressure means customers get enough water at usable pressure" is a whole sentence, sounds like a definition, and settles nothing — because two people applying it would still measure in different places, at different times, against different thresholds.

The test is not whether you can say something about the construct. It is whether what you have said **determines a number**.

Ask three things of any candidate definition:

- **Where** does this tell me to measure?
- **When** does it tell me to measure?
- **How much** does it tell me counts as enough?

If any of the three is missing, you are still holding a construct. That is not a failure — it is where everybody starts — but writing the missing answer down is a decision, and someone is going to make it. Better you, on purpose, than an instrument's location, by default.

### The utility's working definition

The utility does have one, buried in its operating procedures.

> Adequate pressure means **at least 20 metres of head at the fixed monitoring point**.

Pressure here is given in **metres of head** — the height of water standing above the point being measured.
It is used throughout this chapter because it turns every calculation into a subtraction.

That single sentence made all three choices.

**Where:** the fixed monitoring point.
**When:** unstated, which in practice means whenever the reading is taken.
**How much:** 20 metres.

Now the part that matters.

The monitoring point was not selected because it represents Hillcrest customers.
It was selected because it already had an instrument on it.

That is not a scandal. It is how most measurement procedures come to exist — the working definition follows the instrument that happens to be available, rather than the instrument following the definition. But the consequence is real, and here it is arithmetic.

### The same zone, two answers

The case supplies the elevations.

| Item | Elevation |
|---|---:|
| Hillcrest tank water surface, tank full | **96 m** |
| Fixed monitoring point | **62 m** |
| Highest connected property | **84 m** |

Static head is the tank surface minus the property elevation.

At the monitoring point: `96 − 62 = 34 m`.
At the highest connected property: `96 − 84 = 12 m`.

Against a 20-metre threshold, the first is comfortably adequate and the second fails.

Now take the evening peak, when demand is high.
The case supplies that friction along the Hillcrest feeder main costs **6 m** at peak flow, and that the tank surface falls **3 m** by the end of the peak.

At the monitoring point: `96 − 3 − 62 − 6 = 25 m`. Still adequate.
At the highest connected property: `96 − 3 − 84 − 6 = 3 m`.

Three metres of head, at the top of the zone, on the evening when demand is highest.

The utility's records say Hillcrest is adequately served.
The records are not falsified, miscalculated, or badly maintained.
They are the correct output of a working definition that measures somewhere the problem is not.

### Pause: what did the definition decide?

Before reading on, write two or three sentences.

> Both numbers — 25 metres and 3 metres — are correct. Neither instrument is faulty. What exactly did the working definition decide?

If your answer is "it decided where to measure", you have half of it.

It decided **which customer the utility is answerable to**.
A definition that measures at 62 metres of elevation is a definition under which the household at 84 metres does not appear. Not appears-and-fails — does not appear.

That is what a working definition does. It does not describe a construct. It selects, out of everything the construct might have covered, the part that will produce numbers.

### Operationalization

The move from a working definition to a measure has a name, and it is in this chapter's title.

**Operationalization** is developing, from a working definition, a procedure that produces scores.

It is worth being precise about what it is *not*.

Operationalization is not "turning a vague idea into a number".
That description collapses two rungs into one and hides the step where the real choice was made.
The vagueness went away when someone wrote *20 metres at the monitoring point*. Operationalization is what happens after that: siting the sensor, fixing the reading interval, deciding what to do when a reading is missing.

Those last items are not administrative detail. A measure is a **procedure**, and a procedure has to say what happens in the awkward cases, because the awkward cases are where the numbers come from.

The utility's measure reads pressure every fifteen minutes. That interval is a choice with consequences: a dip lasting four minutes may or may not appear in the record, depending on when it falls relative to the reading clock. A procedure that says nothing about missing readings will have them filled in by whoever notices — carried forward from the last value, or left blank, or averaged across the gap — and each of those is a different measure producing different scores.

If someone else could follow your written procedure and get a different number, you have not finished specifying the measure.

### Choosing a measure does not define the construct

This is the section's load-bearing claim, and it needs stating plainly because the opposite is a comfortable place to end up.

It is tempting, having settled on a measure, to treat the measure as what the construct *means*. Adequate pressure just is 20 metres at the monitoring point. That has an attractive tidiness: no more arguments, and the measurement can never be wrong.

That last part is the giveaway.

If a measure defined its construct, a measurement could never be mistaken — only different. And the literature is explicit that this is not how it works: interpretations of scores in relation to concepts should be treated as "falsifiable claims", as "tentative statements that require supporting evidence" [@adcock2001validity, p. 532].

A stipulation cannot be falsified.
A claim can.

When the utility records Hillcrest as adequately served, it is not stipulating. It is claiming that its scores can be read as telling you about service adequacy in that zone. That claim is wrong, and it is wrong in a way you have just checked with subtraction.

There was once a serious position in the philosophy of science holding that a concept simply *is* the operations used to measure it. It is not the position the measurement literature works from today, and this chapter does not attempt to characterize it further.

### The ladder runs both ways

One more property, and it is the reason the second rung is called a *working* definition.

The scheme this ladder comes from includes upward tasks as well as downward ones: refining indicators in light of observed scores, modifying the working definition in light of what the indicators reveal, and revisiting the underlying concept [@adcock2001validity, p. 530].

The same source quotes Kaplan's paradox of conceptualization: "Proper concepts are needed to formulate a good theory, but we need a good theory to arrive at the proper concepts. … The paradox is resolved by a process of approximation" [@adcock2001validity, p. 532].

So the honest picture is not a staircase you descend once.
Having discovered the 3-metre figure at the top of Hillcrest, the utility should revise its working definition — and that revision is the ladder working, not a sign it was built wrong.

### A note from the other tradition

Physical metrology arrived at the same gap independently and gave it a different name.

The **measurand** is the quantity *intended* to be measured, and the international vocabulary is careful to warn that the quantity actually measured can differ from it [@jcgm2012vim, §2.3].

That is the working-definition-versus-measure gap, in metrology's vocabulary.

The two vocabularies do not translate cleanly, and this chapter will not pretend otherwise. A measurand is a *quantity*. A working definition need not be quantitative at all — "adequate" is a threshold on a quantity, but "eligible for assistance" is a classification. The term is signposted here so you recognize it elsewhere, and then set aside.

### Task: place and produce

**Placement.** For each statement, say which rung it is about — construct, working definition, measure, or score.

1. "Hillcrest customers should have enough pressure."
2. "Adequate means at least 20 metres of head at the fixed monitoring point."
3. "The reading at 18:40 was 25 metres."
4. "Pressure is logged every fifteen minutes at the monitoring point."
5. "Nobody agrees what counts as adequate service."
6. "The highest property recorded 3 metres at peak."

**Production.** Write a second working definition of adequate service pressure — one that would have caught the Hillcrest problem — and compute what it returns at the evening peak. State the disagreement between your definition and the utility's as a number.

## 3. What "Valid" Is a Property Of

### A question you should stop asking

Here is a question that sounds sensible and is not:

> Is the monitoring-point sensor valid?

Nothing about the sensor can answer it.

The sensor is well made. It reads pressure at the place it is bolted to. Nothing it does is in error. And you have just seen it support a badly wrong conclusion about whether Hillcrest customers are adequately served.

The sensor is not the thing that went wrong. What went wrong is the interpretation being placed on the numbers it produced.

### Where validity lives

The literature is direct about this.

Valid measurement is achieved "when scores (including the results of qualitative classification) meaningfully capture the ideas contained in the corresponding concept" [@adcock2001validity, p. 530].

Sharpened: measurement is valid when the scores, derived from a given measure, "can meaningfully be interpreted in terms of" the working definition that the measure was built to operationalize — and the focus of assessment "is on the conjunction of these components" [@adcock2001validity, p. 531].

**Conjunction** is the operative word.

Validity is a relation among three things: a measure, the scores it produces, and the construct those scores are being read as. Remove any one and there is nothing left to be valid or invalid. A sensor sitting in a warehouse, attached to no interpretation, is neither.

The same source states the consequence from the other direction: "Scores are never examined in isolation; rather, they are interpreted and given meaning in relation to the systematized concept" [@adcock2001validity, p. 531].

So the malformed question has a well-formed replacement:

> Are these scores interpretable as this construct, for this use?

Every part of that carries weight. *These scores*, not that instrument. *This construct*, not measurement in general. *For this use* — because the same scores can support one interpretation and not another.

### Pause: what would you be buying?

Before reading on:

> If validity is not a property of an instrument, what would it mean to buy a "validated" pressure sensor?

The honest answer is that you would be buying evidence about the instrument's behaviour — that it responds to pressure in a known way, within known limits, when installed as specified.

That is worth having and it is not validity in the sense used here. It tells you the sensor reports pressure at its own location. It cannot tell you that pressure at that location is interpretable as service adequacy for Hillcrest, because the vendor has never heard of Hillcrest.

The certificate travels with the device. The interpretation does not.

### Validity is a claim, so go and get evidence

If interpretations of scores are falsifiable claims, then something follows that makes this section practical rather than merely cautionary.

You can go and test them.

"Scholars should treat these claims just as they would any casual hypothesis, that is, as tentative statements that require supporting evidence. Validity assessment is the search for this evidence" [@adcock2001validity, p. 532].

That formulation is credited by those authors to Messick's earlier work, which has not been consulted directly here; it is reported as they report it.

Notice the shape. In Chapter 2 you learned that drawing a mechanism produces a hypothesis, and that intervention supplies the evidence. Here, interpreting a score as a construct produces a hypothesis, and validity assessment supplies the evidence. In both cases you are handed something to do rather than something to worry about.

### Task: state the claim, then try to break it

The utility's records say Hillcrest is adequately served.

1. Write, in one sentence, what would have to be true for the monitoring-point scores to support that interpretation.
2. Name one observation that would count **against** it.
3. Say whether that observation is available to the utility today.

Your answer to 2 is likely to be some version of *a reading taken at the top of the zone during peak demand*. Your answer to 3 tells you something uncomfortable: the utility has never taken one, so the claim has never been at risk.

An interpretation that could never have been contradicted has not been supported. It has merely gone unchallenged.

### What evidence actually looks like

"Go and get evidence" is only useful if you know what you would be collecting. Four kinds are available to the utility without any new theory, and they generalize.

**Coverage.** Does the measure reach the whole of what the working definition claims to cover?

The utility's definition speaks of pressure in Hillcrest. Its measure reaches one point at 62 metres, in a zone spanning to 84 metres. A quick elevation survey — which the utility already has, since it built the network — shows immediately that most of the zone's elevation range is unrepresented. That is evidence, it took an afternoon, and it bears directly on the interpretation.

**Behaviour.** Do the scores move the way the construct should move?

If these readings track service adequacy, they should fall when demand rises. Pull the monitoring-point log against the demand log for a hot week. If pressure at the monitoring point barely moves while the zone is under obvious stress, the scores are not tracking what they are being read as.

**Agreement across routes.** Do independent ways of getting at the construct agree?

Send someone to the top of the zone during the evening peak with a portable gauge. If the fixed point says 25 metres and the top of the zone says 3, you have learned something no amount of monitoring-point data could have told you. This is the same move that found the storage discrepancy in Chapter 1, and it is the most informative thing on this list.

**Discrimination.** Does the measure separate cases that ought to be separated?

Run the same measure in Lowfield and Hillcrest. If it returns comfortable numbers for both, when one is flat and the other spans twenty-two metres of elevation, then the measure is not sensitive to the thing that distinguishes them.

None of these requires apparatus the utility does not own. What they require is treating the interpretation as something that might be wrong.

There is a substantial literature giving these kinds of evidence names and organizing them into recognized procedures. This book does not teach it, and you do not need it to do the four things above.

Notice what all four have in common. Each compares the scores against something outside the procedure that produced them. That is the only way evidence about an interpretation can be gathered, and it is why sitting with the existing log and studying it harder will never do.

### Valid here does not mean valid there

The same measure can support an interpretation in one setting and fail to in another.

This is called **contextual specificity**, and the literature describes it as arising "when a measure that is valid in one context is invalid in another" [@adcock2001validity, p. 530].

The utility supplies a clean case.

Lowfield is flat. There, a fixed monitoring point represents its neighbours well, because the elevation spread across the zone is small and any point is much like any other. The 20-metre working definition works in Lowfield.

Hillcrest is not flat. Elevation runs from below the monitoring point to twenty-two metres above it. The same working definition, transplanted, measures one household and speaks for none of the others.

Nobody made an error when the definition was carried from one zone to the other. That is exactly what makes contextual specificity dangerous: the transplant is invisible, because the words did not change.

This is a Chapter 3 concern — *this measure, this construct, this setting*. Whether a **finding** established in one population or setting carries to another is a different and larger question, and it is Chapter 9's.

### One validity, several kinds of evidence

A warning about the literature you will meet.

The authors of the framework used here report finding **37 different adjectives** attached to the word "validity" in discussions of conceptualization and measurement [@adcock2001validity, p. 530].

Their resolution is the one this book adopts: these procedures supply "different *types of evidence for validity*", not "multiple independent *types of validity*" [@adcock2001validity, p. 530].

There is one thing you are asking about — whether these scores support this interpretation — and many different ways to bring evidence to bear on it.

If you meet a claim that something has "face validity" or "criterion validity", read it as naming a kind of evidence, not a kind of validity. The distinctions behind the adjectives are real and useful; the proliferation is what makes them confusing.

### One word, two practices

A collision to be named once and then avoided.

In measurement, **validation** names the procedures for assessing whether evidence supports an interpretation of scores.

In computational modelling, **validation** names something else: assessing whether a model is adequate for a stated context of use — a practice with its own standards and vocabulary [@asme2025credibility; @fda2023credibility], which Chapter 5 treats properly.

These are different activities that share a word.

Because merging them causes real confusion, this chapter does not use *validation* again. Where it needs the idea, it says **assessing the evidence for an interpretation**.

A related boundary, from the same source: measurement validity is distinct from the validity of causal inference, and although "measurement validity is interconnected with causal inference, it stands as an important methodological topic in its own right" [@adcock2001validity, p. 529]. Whether a measurement means what you think is Chapter 3. Whether an effect has been identified is Chapter 7.

### The same shape, three times

You have now met the same structural move three times, and it is worth naming, because it is the habit this book is trying to build.

| Chapter | What is not self-standing | What it is relative to |
|---|---|---|
| 1 | whether an answer is adequate | the stated intended use |
| 2 | what belongs in a representation | the purpose; the specified phenomenon |
| 3 | whether a measurement is valid | the interpretation being placed on the scores |

Each of those three claims is established in its own field, and none was invented here.

The observation that they share a shape is this book's own, and it is offered as a working habit rather than a theory: when something looks like a property of an object — this answer, this model, this instrument — check whether it is really a property of a relation between that object and a purpose.

## 4. Reliable, Precise, and Wrong

The last section was about what your numbers are being read as.
This one is about the numbers themselves, and about two confusions that between them account for an enormous amount of misplaced confidence.

### Consistency is not correctness

Start with the word people reach for first.

**Reliability** concerns whether repeated applications of a procedure give consistent results. In the standard formulation, "Random error, which occurs when repeated applications of a given measurement procedure yield inconsistent results, is conventionally labeled a problem of reliability" [@adcock2001validity, p. 531].

Measurement error, in the same passage, "may be systematic—in which case it is called bias—or random" [@adcock2001validity, p. 531].

So there are two ways a number can be off, and they behave completely differently.

**Random error** scatters. Repeat the measurement and the readings dance around some centre.

**Systematic error** — bias — leans. Repeat the measurement and every reading is off in the same direction by about the same amount.

Now the contrast that matters.

> A tape measure with the first two centimetres worn off gives you the same wrong answer every time you use it.

It is perfectly reliable. Every measurement agrees with every other. And every one of them is two centimetres short.

Reliable, and wrong. Those are not opposites, and treating consistency as evidence of correctness is one of the most expensive habits in applied work.

### The relation is genuinely disputed

It would be convenient to say that reliability is necessary for validity and leave it there. The literature does not permit it.

The authors of the framework used here record two positions. On one, "unreliable scores may still be correct 'on average' and in this sense valid". On another, scholars "view reliability as a necessary but not sufficient condition of measurement validity" [@adcock2001validity, p. 532].

This chapter does not adjudicate between them, because the practical lesson survives either.

**Reliable does not mean valid.** That holds on both accounts, and it is what you need.

### The three words the standard separates

Physical metrology has its own vocabulary for the same territory, defined in an international standard with unusual bluntness. It is worth reading closely, because the definitions do work that ordinary usage will not do for you.

**Precision** is "closeness of agreement between indications or measured quantity values obtained by replicate measurements on the same or similar objects under specified conditions" [@jcgm2012vim, §2.15].

**Trueness** is "closeness of agreement between the average of an infinite number of replicate measured quantity values and a reference quantity value" [@jcgm2012vim, §2.14].

**Accuracy** is "closeness of agreement between a measured quantity value and a true quantity value of a measurand" [@jcgm2012vim, §2.13].

The standard then does something you rarely see a standard do. It forbids the confusions explicitly, three separate times.

Accuracy "should not be used for" trueness, nor for precision, "although it does relate to both these concepts" [@jcgm2012vim, §2.13]. Trueness likewise must not be called accuracy [@jcgm2012vim, §2.14]. And the entry for precision records that "measurement precision" is sometimes **erroneously** used to mean measurement accuracy [@jcgm2012vim, §2.15].

A standards committee writing three prohibitions against one family of confusions tells you how often it is met.

### Only one of them is a number

Here is the fact that does the most work in this chapter, and it takes a moment to sink in.

**Precision is expressed numerically** — by a standard deviation, a variance, or a coefficient of variation [@jcgm2012vim, §2.15].

**Trueness is not a quantity** and is not expressed numerically [@jcgm2012vim, §2.14].

**Accuracy is not a quantity** and "is not given a numerical quantity value"; a measurement is simply said to be more accurate when it offers a smaller measurement error [@jcgm2012vim, §2.13].

Now think about what appears on a specification sheet.

Manufacturers quote precision figures, because precision is the one that can be quoted. What you are handed as a number is the property that describes how tightly readings cluster — and tells you nothing about whether they cluster around the right value.

**The quotable figure is not the one you care about.**

If a data sheet quotes something as "accuracy: ±0.4%", it is not using the word the way the standard defines it. It may be quoting precision. It may be quoting a manufacturing tolerance. Whatever it is, the standard is explicit that accuracy is not a number, so a number labelled accuracy is something else wearing the label.

### The utility's sensor

The pump-station pressure sensor, from the case:

| Property | Value |
|---|---|
| Display resolution | **0.01 bar** |
| Repeatability | **±0.02 bar** |
| Offset found at the last calibration check | **0.15 bar high** |

The case supplies that 1 bar is about 10.2 metres of head, so that offset is roughly **1.5 metres**.

Read the three rows together.

The sensor displays two decimal places. It repeats to within 0.02 bar. By any reasonable use of the word, it is precise — and its readings are consistently about a metre and a half of head too high.

Precise. Repeatable. Wrong.

And note where the trap is. The two-decimal display is the most visible feature of that sensor and the least informative. Resolution — how finely a device can display — is not trueness, and adding decimal places to a biased reading produces a more finely specified wrong answer.

### Pause: what have 200 readings told you?

Before reading on:

> You have 200 readings from this sensor, all within 0.02 bar of each other. What have you learned, and what have you not?

You have learned that the sensor is precise. Two hundred readings is strong evidence of that, and each additional reading strengthens it.

You have learned **nothing whatever** about the 1.5-metre offset.

### Why more measurements will not help

This is not a rule of thumb. It follows from the definitions.

Trueness is defined as closeness of the average of an **infinite** number of replicates to a reference value, and the standard states that trueness is inversely related to systematic measurement error and **not related to random measurement error** [@jcgm2012vim, §2.14].

Read that as an instruction about what averaging does.

Averaging attacks scatter. As you take more readings, the average settles down — that is precision improving, and it is real. But it settles down onto whatever value the procedure is centred on. If that centre is 1.5 metres high, more readings deliver a beautifully stable estimate of a number that is 1.5 metres high.

> More measurements improve precision.
> More measurements do nothing for trueness.

Which means that the standard remedy for uncertainty — take more data — is precisely useless against the error most likely to change your decision.

### You have already seen this happen

Turn back to Chapter 1.

The utility's dashboard reported **10.8 ML** of storage. An independent check, using a different observation path, found **9.9 ML**.

That gap is **0.9 ML**, and it was in one direction, because the remote transmitter was reading high.

Ask what would have happened if, instead of an independent check, the operator had done what feels careful: refreshed the dashboard, taken readings every few minutes through the morning, and averaged them.

Every one of those readings would have been about 0.9 ML high.
The average would have been about 0.9 ML high.
The scatter would have looked reassuringly small — and would have been reported as confidence.

The independent check found the problem precisely because it was a **different** observation path, not more of the same one. That is the only thing that works against systematic error: a route to the quantity that does not share the suspect procedure's assumptions.

### What "error" does and does not mean

Two clarifications from the standard, both of which prevent ordinary usage from misleading you.

Measurement error is defined as "measured quantity value minus a reference quantity value" [@jcgm2012vim, §2.16] — and the entry is careful to note that it "should not be confused with production error or mistake".

Nobody blundered. A biased sensor is not a careless sensor.

Second, and more consequential: the same entry makes the error **knowable only where a reference value exists** — through calibration against a standard of negligible uncertainty, or through a conventional value [@jcgm2012vim, §2.16].

That condition is doing a great deal of quiet work, and it brings us to the seam running through this whole chapter.

### Two kinds of construct in one system

Look at the two things this chapter has been measuring.

**Stored volume** has a reference value. There is a fact about how much water is in that tank. A calibrated check can get at it, which is exactly how the 0.9 ML discrepancy was found. Here the whole metrology vocabulary applies cleanly: there is a true value, so there is an error, so trueness is a meaningful property.

**Adequate service pressure** has no reference value.

There is a fact about the pressure at any given point — that part is measurable. But *adequate* is a threshold somebody chose. There is no fact of the matter that adequate is 20 metres rather than 18 or 25. No calibration laboratory can settle it, because it is not the kind of thing a laboratory settles.

So when the utility's working definition misleads, it is not because the definition is *wrong* in the way a biased sensor is wrong. There is nothing to subtract it from.

This is not a defect in the chapter's example. It is the ordinary situation, and it is why measurement demands more than good instruments. Where the construct is chosen rather than standardized, the vocabulary of error still applies to the *instrument* — the sensor really is 1.5 metres high — but not to the *definition*. What you can say about a definition is that it is defensible or indefensible for the interpretation you want to place on it, which is §3's question, not §4's.

Keep the two straight. A great deal of confused argument comes from demanding a true value for something nobody ever standardized, or from assuming that because a threshold was chosen, any threshold will do.

### Calibration, and what it cannot do

**Calibration** is how a systematic offset is found: you compare the instrument against a reference and characterize the difference.

It is how the utility knows its pump-station sensor sits 0.15 bar high, and how it knew the storage transmitter was reading high.

And it has a hard limit, which the whole of §3 has already prepared you for.

Calibrating an instrument tells you that it reports its own quantity correctly.
It cannot tell you that its quantity is the one you want.

Send the monitoring-point sensor away for calibration and it will come back certified. It will then continue to report, very accurately, the pressure at 62 metres of elevation — while the household at 84 metres continues to receive 3 metres of head at peak.

A calibration certificate is evidence about an instrument.
It is not evidence about an interpretation.

## 5. Proxies, Units, and the Cost of Standing In

### Measuring something else on purpose

Sometimes you cannot measure the construct at all, and you measure something else instead, knowing it is something else.

That substitute is a **proxy**.

The utility has one, and it is on every screen in the control room.

Customer pressure is not measured continuously anywhere in Hillcrest. The monitoring point reports every fifteen minutes at one location; the top of the zone is not instrumented at all. But **tank level** is measured continuously, has been for years, and is already displayed.

So tank level stands in for whether customers are being adequately served.

This is not a lazy choice. The proxy is cheap, continuous, already paid for, and genuinely related to the thing it stands in for. Most proxies you meet will have that character: they are reasonable, and their reasonableness is what makes them dangerous.

### When a proxy works and when it breaks

A proxy earns its place under conditions, and the discipline is to state the conditions rather than the proxy.

**Tank level tracks customer pressure when the tank is the binding constraint.** If the zone is short of water, the tank falls, and pressure falls with it. Under those conditions the proxy is informative and cheap, and using it is good practice.

**It breaks when friction is the binding constraint.**

You met that case in Chapter 2 as Mechanism B: pressure lost along an old, undersized feeder main. Friction loss grows with flow, so it is largest exactly when demand is highest.

Put the numbers together. At the evening peak the tank surface falls **3 m**, while friction along the main costs **6 m**.

The larger of the two effects is the one the proxy cannot see.

So the control-room screen shows a tank that has come down a little and is still comfortably full, at the precise hour when the top of the zone is at three metres of head.

### The failure is structured, not random

This is the property that distinguishes proxy failure from the errors of §4, and it is why the two demand different responses.

Random error scatters, so averaging helps.
Systematic error leans, so a different observation path helps.

**Proxy failure happens under identifiable conditions.** It is not noise and it is not a constant offset. It is a relationship that holds in one regime and stops holding in another.

Which means neither remedy from §4 works here. More tank-level readings do not repair it — you can log every second for a year and learn nothing about friction loss. And recalibrating the tank-level sensor does not repair it either, because the sensor was never wrong. It reported tank level correctly the entire time.

What repairs it is knowing the conditions.

So when you accept a proxy — and you often should — write down the sentence that goes with it:

> Tank level stands in for customer pressure. It is informative when the tank is the binding constraint, and uninformative when friction along the feeder main is. It is least informative at evening peak.

That sentence costs nothing and is the difference between a proxy and a mistake.

### Units, briefly

A short note, because units are usually treated as bookkeeping and are not.

This chapter has used **metres of head** throughout. It could have used bar, or pounds per square inch, and the case supplies the conversion: one bar is about 10.2 metres of head.

Metres of head was chosen because it makes the relevant arithmetic subtraction. A property twenty-two metres above the monitoring point has twenty-two metres less head — you can see the Hillcrest problem in a single subtraction. In bar, the same relationship requires a conversion at every step, and the conversion is where the elevation quietly stops being visible.

The general point is that a unit choice makes some relationships obvious and others invisible. That is not a reason to distrust units; it is a reason to notice which relationship yours has made easy to see.

A harder version of the same problem arrives when quantities are not on a scale that supports the operation being performed on them. Averaging a set of temperatures in Celsius is fine. Averaging a set of rankings is not obviously fine, and averaging a set of categories is not fine at all. There is a substantial theory about which operations are meaningful on which kinds of scale; this book does not teach it, and where you find yourself doing arithmetic on scores whose spacing nobody defined, that is the signal to go and read it.

### Two numbers that look comparable

The neighbouring utility publishes that **95%** of its properties are adequately served.

Our utility, on the figures you will work through in the next section, can report about **91%**.

Ninety-five is more than ninety-one. It is tempting to conclude that the neighbour is doing better, and a great many published comparisons are exactly this.

Here is the neighbour's working definition: **at least 15 metres of head, measured at midday.**

Ours: at least 20 metres of head, at the monitoring point, with the failing figure computed at evening peak.

A lower threshold. A different time of day. A different location.

The two numbers share a shape, a unit, and a percentage sign, and they are not measuring the same thing. There is no conversion between them, because the difference is not one of scale — it is a difference in what was decided at rung two.

And it is worth being explicit about what has *not* happened here. The neighbour is not misreporting. Their definition may be entirely appropriate for a flat service area. They are answering a different question, correctly, and the failure is in the comparison rather than in either measurement.

A score without its working definition is not a rough number.
It is an uninterpretable one.

## 6. The Utility's Pressure Problem

### Four measures, one decision

The decision: whether to record Hillcrest as adequately served in the drought report.

Four defensible operationalizations, all of the same construct.

| Operationalization | At evening peak | Verdict | What it is good for |
|---|---:|---|---|
| Pressure at the pump station discharge | high | adequate | knowing what the utility is producing |
| Pressure at the fixed monitoring point | **25 m** | adequate | a single representative location, cheaply |
| Pressure at the highest connected property | **3 m** | **inadequate** | knowing the worst-served customer |
| Share of properties above threshold at peak | **≈ 91%** | **partly inadequate** | knowing the distribution of service |

None of these is a mistake. Each answers a real question, and the questions are different.

The third and fourth rows are the ones that bear on whether anyone is going without water tonight, and neither is what the utility measures.

### Which one should it use?

The honest answer is that the question is incomplete, and by now you should expect that.

*Use for what?*

For **operating the pumps hour to hour**, discharge pressure is the right measure. It is what the operator can act on, it responds immediately, and nothing else on the list does.

For **reporting service adequacy to a regulator**, the share of properties above threshold is the right measure. It is the only one that speaks about customers rather than about locations.

For **deciding whether to restrict Hillcrest tonight**, pressure at the highest connected property is the right measure. The decision is about who loses service first, and that is the household in question.

For **detecting a developing problem cheaply and continuously**, the monitoring point earns its place — provided somebody has written down what it cannot see.

Four measures, four uses, no winner. The utility's mistake was never choosing the monitoring point. It was using one measure, chosen for one purpose, to answer a question it was not built for — and then writing the answer into a plan.

Notice that this is Chapter 2's lesson arriving again in different clothing. There, a representation adequate for one purpose could not express another. Here, a measure adequate for one purpose cannot support another. Neither is a defect to be corrected; both are conditions to be stated.

### Where the 91% comes from

Work it rather than read it.

A property fails the 20-metre threshold at peak when its own elevation is high enough that the water above it falls short. With the tank surface at 96 m, down 3 m at peak, and 6 m lost to friction, the head available at elevation *E* is `96 − 3 − 6 − E`.

Setting that below 20 metres gives `E > 67 m`.

The case supplies that **31 of 340** properties sit above 78 m — comfortably above the 67 m line, so all 31 certainly fail.

`31 ÷ 340 ≈ 0.091`

So at least **9%** of Hillcrest properties are below threshold at peak, and about **91%** are above it.

One caution, and it is the sort worth building a habit around. The case does **not** say how many properties lie between 67 m and 78 m. Some of them fail too. So 91% is an **upper bound**, not a computed figure, and writing it as "91% of properties are adequately served" would state more than the data supports. Where the supplied facts run out, say so rather than filling the gap.

### What the plan can contain

Chapter 2 ended on a finding about the drought plan: it has a system-wide reserve and no zone-level trigger, because a plan can only contain triggers that its representation can express.

Chapter 3 adds the companion.

> A plan can only contain thresholds that its measures can evaluate.

The utility's plan says pressure must remain adequate. The only instrument that can pronounce on adequacy is at the monitoring point. So *adequate* came to mean *adequate at the monitoring point* — not by decision, but by the absence of one.

Follow that chain backwards and you arrive somewhere uncomfortable: the household at 84 metres is invisible in the utility's records because of where a technician could conveniently park a van.

### Task: diagnose five defects

Each of the five items below contains one defect. For each, write three things: the defect, what it stops you from being able to conclude, and a repair.

1. An engineering report states: "The monitoring-point sensor is validated, so the adequacy figure is reliable."
2. A sensor specification sheet quotes: "Accuracy: ±0.4%."
3. An operator proposes resolving the storage discrepancy by taking dashboard readings every two minutes for an hour and averaging them.
4. An operating procedure states: "Adequate pressure is what the monitoring point records."
5. A regional summary places the neighbouring utility's 95% and our 91% in the same column of a table.

When you have written all five, and not before, open [`diagnosis-feedback.md`](diagnosis-feedback.md) and compare.

### Task: place four items on the line

Chapter 4 is about why particular records exist rather than others. This chapter has been about whether the numbers in existing records mean what you think.

The test:

> **Chapter 3:** the number is here — does it mean what I think?
> **Chapter 4:** why is this number here, and not another?

Place each item.

1. The pump-station sensor reads 0.15 bar high.
2. Pressure sensors exist only at pump stations, and nowhere in the zones.
3. "Adequate" was defined as 20 metres of head at the monitoring point.
4. The monitoring point was sited where a technician could park a van.

The first three have answers. The fourth does not, and you should not force one — it is genuinely both a choice about measurement procedure and a fact about which records came to exist. Write down which way you lean and what makes it hard. Being able to see why a case is on a boundary is worth more than a confident placement.

## 7. Cold-Start Practice and Retrieval

### Return to your six-minute definition

Find what you wrote at the start of §1.

Read it against four questions, and do not score it.

- Did you say **where** the measurement is taken?
- Did you say **when**?
- Did you say **how much** counts as enough?
- Did you say what your definition would *fail* to notice?

Almost nobody answers the fourth on a first attempt, and that is the specific thing this chapter has added. The first three make a definition operable. The fourth makes it honest.

Two other patterns are common and worth naming.

Some first definitions name a threshold and no location — "at least 20 metres of head" — which is not measurable until someone decides where. Others name an instrument rather than a construct: "adequate pressure is what the sensor reads". You now know that the second is not a definition at all; it is rung three standing in for rung two.

### Independent transfer

Now work an unfamiliar construct, without this chapter, the water case, or any rubric in front of you.

You have been assigned **one** of the forms below. Open only that one.

- [Form A — Indoor air quality in a school](transfer-form-a.md)
- [Form B — Hospital emergency department waiting time](transfer-form-b.md)

Allow about **40 minutes**.
Every fact you need is supplied. Do not look anything up.

Do not open the other form. You will work it after a delay, and it tests nothing if you have seen it.

When your response is complete — and only then — use [`transfer-rubric.md`](transfer-rubric.md) to review it dimension by dimension.

### Retrieve the questions from memory

Before looking back at the chapter, write down the questions you would ask about any number that arrives in front of you.

Aim for the sequence, not the wording. Then compare and repair what you missed.

For reference, after you have tried:

1. What is the construct — the thing this number is about?
2. What is the working definition, and what did it decide about where, when, and how much?
3. What is the measure — the actual procedure — and what does it do when things go wrong?
4. What interpretation is being placed on these scores, and for what use?
5. What evidence would count against that interpretation, and does it exist?
6. Is the procedure consistent, and is that being mistaken for being correct?
7. Is there a systematic offset, and would more measurement find it? (It would not.)
8. Is this a proxy, and under what conditions does the substitution break?
9. Does this construct have a reference standard, or was its threshold chosen?
10. Would this measure still support this interpretation in a different setting?

Question 4 is the one to keep if you keep only one. Almost every failure in this chapter can be reached by skipping it.

A caution about the list, though, in the spirit of the chapter.

Ten questions asked mechanically will produce ten mechanical answers, and a document that has been through such a checklist can look thoroughly examined while nothing was actually at risk. The work is not in asking the questions. It is in being willing to get an answer you did not want — that the offset is systematic, that the proxy breaks at exactly the wrong moment, that the interpretation everyone has been relying on has never once been tested.

If running the list never changes anything you do, you are not running it.

### If the transfer went badly

It often does the first time, and the useful thing is to find out in which specific way.

- **You produced one operationalization instead of two.** You treated the working definition as given rather than as a choice. Go back and write the definition as a sentence with three decisions in it.
- **You named an offset but called it noise.** Ask whether repeating the measurement would reveal it. If not, it is systematic, and it needs a different observation path rather than more of the same.
- **You wrote that an instrument is or is not valid.** Reread §3. Name the interpretation, then the use.
- **You could not find a proxy.** Ask what is actually measured continuously versus what is actually cared about. The gap between those two is almost always where the proxy is.
- **You placed the boundary item confidently.** Look again. Confidence on a genuinely mixed case usually means one of the two readings was not seen.

None of these is a failure of intelligence. Each is a specific missing move with a specific repair.

### Delayed retest

After the interval your reading plan specifies, you will work the other form.

Do not reread this chapter immediately beforehand, and do not look at the form you have not done. The delay is the measurement, and rereading first would be measuring the wrong construct — which, by now, you should find an unpleasant thought.

### What Chapter 4 asks next

You can now take a number and ask what it stands for and how well.

Your representation of the utility contains *Hillcrest demand: 0.9 ML per day*. You can now ask what "Hillcrest demand" was defined to be, what procedure produced 0.9, and what that figure can be interpreted as.

Here is the question this chapter has not touched.

Hillcrest has no zone meter. That figure was produced by taking the town total and subtracting the zones that **are** metered.

So the record exists, it has a number in it, and the number was never measured at all — it is what was left over after measuring somewhere else.

Why does that record exist, in that form, rather than another? Which measurements got made, by whom, for what purpose, and what never got recorded because nobody needed it at the time?

That is Chapter 4.
