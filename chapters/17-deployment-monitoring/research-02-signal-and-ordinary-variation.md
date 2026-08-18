# Research 02: Signal Against Ordinary Variation

Cluster 2 of four. Every locator below was taken from reading the document directly.

## 1. What the architecture permits, and what the chapter takes

`README.md`'s Chapter 17 block is the only chapter block in the book with permissive phrasing:

> "Concept-level monitoring machinery may include common-cause versus special-cause variation and control-chart reasoning where appropriate."

**"May include" and "where appropriate."**

The governed core competence names "**distinguish signal from ordinary variation**". **That is the distinction, not the technique**, and `../../decisions/0024` clause 2 records the choice to take the first and refuse the second.

**What is refused, specifically:** centre lines, control limits, run rules, chart types, sampling plans, and every named chart. The chapter says the architecture permitted them and explains why it did not use them.

## 2. The source, and its limits

`sumanprajapati2018control` — Suman and Prajapati, "Control chart applications in healthcare: a literature review", *International Journal of Metrology and Quality Engineering* 9, 5 (2018), open access under a Creative Commons licence stated on its first page.

**Printed page numbers appear in the running heads on even pages and equal the PDF pages.** Read at p. 1 only.

**It is a literature review of healthcare applications.** It is used for two things and nothing else.

## 3. The attribution

`sumanprajapati2018control` p. 1:

> "The concept of Statistical process control (SPC) was given by the physicist Walter Shewhart in order to improve the industrial manufacturing."

**Shewhart (1931) was not obtained**, so the distinction below is used **as reported at** this review — the device this book has used since Chapter 6.

## 4. The distinction

`sumanprajapati2018control` p. 1:

> "SPC can help in determining the source of errors by identifying the special and common causes of variations."

> "The SPC is based on theory of variation i.e., common and special causes of variations."

**Extraction note.** This source renders `fi` as a ligature that extracts as a single character — *firstly* as *ﬁrstly*, *defined* as *deﬁned*. **No quotation taken from it contains an `fi`**, and both sentences above are clean.

## 5. What the book makes of it

**The distinction, in the book's own words**, and flagged as the book's own framing rather than the source's:

**Ordinary variation** is what a process produces when nothing in particular is happening. It has a range, and that range is a fact about the process which can be measured before anything goes wrong.

**A signal** is a value that ordinary variation does not readily produce.

**And the operative consequence, which is the chapter's:** a threshold is only a trigger if it sits outside the range of ordinary variation. **A threshold set inside that range is a timer** — it will fire eventually whether or not anything has happened, and the interval between firings is a fact about the process rather than about the world.

**That reframing is the book's own.** The source supplies the distinction and the attribution; the consequence for signposts is derived here and is stated as derived.

## 6. Why this arrives so late in the book

The chapter should note the connection backwards, once.

**Chapter 8** taught that a number carries an interval and that a threshold verdict throws away most of what the number contains.

**Chapter 12** designed signposts with thresholds and said, in its own text, that "those numbers are arguable, and being arguable is the property that matters."

**Chapter 17 argues with them**, using Chapter 8's habit on Chapter 12's output. **The material for this criticism has been in the book since Chapter 8**, and the case shows that nobody applied it.

## 7. What was not taken

- Every healthcare application in the review, which is its actual subject.
- Every chart type, control limit, and run rule.
- The review's account of SPC's history beyond the Shewhart attribution.
- Any claim about healthcare, quality improvement, or manufacturing.

## 8. What the chapter takes

| Claim | Locator |
|---|---|
| Statistical process control originates with Shewhart | p. 1 |
| It rests on the theory of variation — common and special causes | p. 1 |
| It identifies the source of errors by separating the two | p. 1 |
