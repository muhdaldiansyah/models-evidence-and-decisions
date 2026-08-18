# SME Review Packet — The Unfamiliar Cases

Status: **provisional.** Built on [Decision 0025](../decisions/0025-validation-architecture.md), **PROPOSED and not author-adjudicated**. Ready to send.

Three cases in the book are **not** the water anchor, and they need reviewers the water packet cannot supply. This file covers all three and is written so that each reviewer can read only their own section.

| Case | Where | Reviewer wanted |
|---|---|---|
| A repairs triage tool | Chapter 16, Problem A · Chapter 17, Case 2 | social housing or property maintenance |
| A charity appeal's timing | Chapter 16, Problem B | fundraising or direct marketing |

**These cases do not inherit Chapter 1's Gate 1.** They open gates of their own, and Chapter 16 is the only chapter in the book that is not downstream of the water anchor.

## What every reviewer is being asked

Whether the story is coherent, whether it sounds like the work actually sounds, and whether anything could be read as implying unsafe practice or as describing a **real** organisation, tool, or vendor.

## What no reviewer is being asked

To validate any figure as typical, or to judge whether the reasoning the book teaches is correct. Every number is synthetic and instructional.

---

# Part 1 — The repairs triage tool

**For a social-housing or property-maintenance reviewer.** About 25 minutes.

Read [`../chapters/16-integration-full-loop/case-data.md`](../chapters/16-integration-full-loop/case-data.md), Problem A, and [`../chapters/17-deployment-monitoring/case-data.md`](../chapters/17-deployment-monitoring/case-data.md), Case 2.

## The story

A social landlord deploys an automated tool that assigns priority codes to repair requests. It was trained on **96,400 historical jobs**. Eighteen months after deployment, someone asks whether it is working.

Chapter 16 asks which analytical machinery the question needs. Chapter 17 asks a narrower question: three indicators were monitored, all looked fine or better, and the failure was somewhere else entirely.

## Questions

**Q1 — Scale and shape.** Is a tool trained on 96,400 historical jobs, assigning priority codes for a landlord of this size, a realistic deployment? Is the volume coherent with the stock implied?

**Q2 — The downstream indicators.** The case turns on **emergency jobs** rising 22% and **hazard referrals** rising 3.1%. Are those two quantities the right pair to watch? Would they in practice be held by different teams, so that **their ratio is nobody's report**? That last point is the case's central claim about why nobody noticed.

**Q3 — Cost.** **£148 for an emergency attendance against £62 for a scheduled one.** Is that ratio plausible in direction and rough magnitude?

**Q4 — The improving indicator.** Chapter 17's case has completion-within-target **improving** from 94.1% to 95.6% *because* of the failure — jobs miscoded to a lower priority get longer target times and are therefore completed within them. Is that a mechanism you recognise? Would a real service report it as an improvement?

**Q5 — Safety and identification.** Could anything be read as implying that automated priority coding is a practice this book recommends, that a real tool or vendor is being described, or that hazard referrals are a thing an algorithm should be trusted to route? Please quote the sentence and suggest the smallest repair.

---

# Part 2 — The appeal timing

**For a fundraising or direct-marketing reviewer.** About 15 minutes.

Read [`../chapters/16-integration-full-loop/case-data.md`](../chapters/16-integration-full-loop/case-data.md), Problem B.

## The story

A charity is deciding when to send its main annual appeal. Six October sends averaged a 3.52% response rate; two November sends averaged 4.00%. Someone proposes moving the appeal to November on the strength of that difference. The mailing is **90,000 records at a £27.40 mean gift**, and a split test would cost about **£4,800**.

## Questions

**Q1 — Scale.** Is a 90,000-record appeal at a £27.40 mean gift a coherent combination for a charity of the size implied?

**Q2 — Response rates.** Are 3.52% and 4.00% plausible for a warm-list appeal? Is a difference of that size the kind of thing a team would in practice be shown and asked to act on?

**Q3 — The comparison as presented.** Six sends against two, across different years. Is being handed exactly this comparison, in exactly this form, realistic? **The case depends on it being ordinary rather than negligent.**

**Q4 — The split test.** Is **£4,800** plausible for a split test on a list this size? The book says it buys about 40% of the disputed difference, and that this is the number that makes it worth doing.

**Q5 — Identification.** Could anything be read as describing a real charity, campaign, or supplier?

---

# Response format, both parts

**Overall disposition:** **PASS** · **PASS WITH WORDING CHANGES** · **REVISE MECHANISM**.

| Case | Location | Current wording / issue | Why it matters | Suggested minimal repair | Severity |
|---|---|---|---|---|---|

## What a PASS does not certify

That the tool or the appeal reflects good practice; that any figure is typical; that the analysis the book performs on the case is correct; or that either chapter is ready to publish.

It closes only the **realism and accidental-implication gate** for two fictional instructional cases.

## After the review

1. Adjudicate every material comment.
2. Update `../chapters/16-integration-full-loop/case-data.md` first; **Chapter 17's Case 2 depends on it** and must be re-checked against any change.
3. Record unresolved disagreement explicitly.
4. Update [gate-status.md](gate-status.md), and only that file, for gate status.
