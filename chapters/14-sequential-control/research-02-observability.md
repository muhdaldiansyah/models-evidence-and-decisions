# Research 02: Observability

Cluster 2 of four. Every locator below was taken from reading the document directly.

**Edition note.** `astrom2008feedback` is the 2008 first edition; printed page equals PDF page minus 12, calibrated in Chapter 2 and re-used since.

## 1. The definition, and why it is paraphrased

`astrom2008feedback` p. 202 states it as Definition 7.1. The definition contains a quantifier, an inequality, and an interval, so under the standing rule from Chapter 8 it **may not be quoted**.

**The paraphrase, declared as one:** a system is observable if the state at any chosen time can be determined from the record of its inputs and its measured outputs over an interval.

Same page, immediately after, on how far the idea reaches:

> "The definition above holds for nonlinear systems as well, and the results discussed here have extensions to the nonlinear case."

## 2. The prose that carries the chapter

`astrom2008feedback` p. 202:

> "The problem of observability is one that has many important applications, even outside feedback systems. If a system is observable, then there are no 'hidden' dynamics inside it; we can understand everything that is going on through observation (over time) of the inputs and outputs. As we shall see, the problem of observability is of significant practical interest because it will determine if a set of sensors is sufficient for controlling a system."

**Three usable claims in three sentences.**

**"No hidden dynamics inside it."** The right intuition, and it is the source's own phrase rather than a pedagogical invention.

**"Over time."** Observability is not about a single reading. A state can be unrecoverable from today's instruments and recoverable from a week of them, which is why the concept belongs after Chapter 13's delays.

**"Whether a set of sensors is sufficient for controlling a system."** This is the sentence that makes observability a decision question rather than a mathematical one, and it is what licenses §6's instrument purchase.

And the extension that connects to Chapters 3 and 4:

> "Sensors combined with a mathematical model can also be viewed as a 'virtual sensor' that gives information about variables that are not measured directly. The process of reconciling signals from many sensors with mathematical models is also called sensor fusion."

**Handle with care.** Chapter 3 taught that a score is not the construct and Chapter 4 taught that records exist because of a process. A "virtual sensor" is a model output being treated as a measurement, and the book has spent two chapters on why that substitution needs watching. The chapter should use the term and immediately note the tension.

## 3. Where the chapter stops

`astrom2008feedback` p. 201 states what Chapter 7 of that book goes on to do:

> "In this chapter we show how to use output feedback to modify the dynamics of the system through the use of observers. We introduce the concept of observability and show that if a system is observable, it is possible to recover the state from measurements of the inputs and outputs to the system."

**Chapter 14 takes the first half of the second sentence and refuses the rest.** Whether the state *could* be recovered is the question; recovering it is state estimation, and `README.md` excludes filtering.

The rank test at pp. 202–203 was read only far enough to confirm it is a test and is not taught. The observer construction, the separation principle, and Kalman filtering were not read.

## 4. Why the concept is not "did anyone measure it"

The distinction the chapter must protect, built from the source and stated as the book's own:

**A state is unobservable when two different states produce identical records.** No amount of care with the existing instruments separates them, because there is nothing in the record to separate. Adding an instrument may fix it; reading the existing ones harder cannot.

**That makes observability a property of the pairing of a system with a set of instruments**, not a property of either alone — which is the same shape as Chapter 3's `validity` (a property of an interpretation, not of an instrument) and Chapter 9's `transportability` (a relation, not a property). **Third instance of that shape**, and the manuscript should name it in prose.

## 5. What the chapter takes

| Claim | Locator |
|---|---|
| The definition, paraphrased | p. 202 |
| The definition extends to nonlinear systems | p. 202 |
| No hidden dynamics; understand everything through observation over time | p. 202 |
| Observability determines whether a set of sensors is sufficient | p. 202 |
| Virtual sensors and sensor fusion | p. 202 |
| Observability is the prior question to state recovery | p. 201 |

## 6. What was not taken

- Definition 7.1 verbatim — comparison symbols.
- The observability rank test, pp. 202–203.
- Observers, state estimation, the separation principle, Kalman filtering, pp. 206–219.
- Reachability and state feedback, Chapter 6 of the source, entirely.
