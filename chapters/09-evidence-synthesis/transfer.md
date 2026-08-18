# Chapter 9 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0016-chapter9-synthesis-terminology-and-boundary.md`.

## Transfer target

Per `spec.md`:

> Given several sources bearing on one decision, with sizes, estimates, and stated defects, determine which are about the same quantity, produce at least two weighting rules and their answers, identify a dependence, name the support factor that decides whether any of them transfers, and state what would have to be true of the target setting.

## The changed task shape

Chapter 8 asked the reader to **rewrite a summary**. Chapter 9 asks them to **write the paragraph that goes in front of a committee, containing no single combined number.**

That constraint is the form's sharpest instrument. A reader who has absorbed the chapter and still ends with "approximately −20%" has reproduced the failure in a shorter sentence, and the constraint catches it without any judgment call by the marker.

## Form design

Both forms supply the same six things, in the same order:

1. **A decision with a date**, so that "more research" is visibly not an answer.
2. **Five sources** with sizes spanning three orders of magnitude and estimates spanning a factor of seven or more.
3. **A largest-and-worst source** whose defect is stated: voluntary participation and no enforced definition of the variable.
4. **A source measuring a different quantity entirely** — a rig or a synthetic benchmark with no people in it.
5. **Two dependencies**, each answerable by asking rather than by computing.
6. **A support factor absent from the target setting**, stated as a physical or institutional fact rather than as a caveat.

| | Form A | Form B |
|---|---|---|
| Domain | Hospital estates | Banking risk |
| Sources | 2 / 12 / 900 / 8 wards, sites, wards, rigs | 3 / 15 / 620 / 10 regions, banks, institutions, suites |
| Estimates | −18, −31, −4, −52, −12 | −22, −35, −5, −48, −15 |
| Simple average | **−23.4%** | **−25%** |
| Median | **−18%** | **−22%** |
| Size-weighted | **−4.8%** | **−6.4%** |
| Drop C, average rest | **−33.7%** | **−35%** |
| Largest source's weight share | **97.6%** | **95.7%** |
| Different-quantity source | drop rig, no person | synthetic streams, no customers |
| Support factor | continuous floor coverage | a shared interbank registry |
| Target lacks it because | fixed equipment limits coverage to ~60% | the new market has none |

Units, magnitudes, and counts differ so that a reader working both forms cannot carry an answer across. Every structural feature is matched.

### Deliberate difficulty features

**The size-weighted answer is nearest to zero in both forms.** A reader who uses the most principled-sounding rule concludes the intervention barely works, which is the opposite of what three of the four rules say. The error is consequential, not cosmetic.

**The support factor is buried in fact 5**, presented as an operational detail rather than flagged as decisive. It is the last supplied fact and reads like housekeeping.

**Both dependencies involve people rather than data**, so no data check would find them. They are found by asking who was involved, which is Chapter 4's discipline applied to authors.

**The different-quantity source has the largest effect.** Readers who drop it lose the most dramatic number; readers who keep it inflate the average. Either way it should be reclassified rather than admitted or rejected — which is what the rubric rewards.

**The committee paragraph forbids a combined number.** No partial credit is available for a well-hedged single figure.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising.

**One judgment recorded.** Form A is set in a hospital, and Chapter 4's contrast domain was hospital emergency department waiting time. The two share only the building type: that case was about how waiting-time records come to exist, this one about combining five sources on a capital purchase. No quantity, actor, or question is shared. Flagged rather than left for a reader to notice.

**One deliberate near-miss.** Form A concerns patient falls, which is a domain where real harm is at stake. The form takes no position on flooring, presents no value as typical, and asks only what a set of sources can support. Judged non-sensitive in the sense `spec.md` uses, and the judgment is recorded rather than assumed.

## What a strong Form A answer should notice

- **The four rules: −23.4%, −18%, −4.8%, −33.7%.** At least three of them.
- **Source C takes 97.6% of the size-weighted total**, and its variable is undefined — "injurious" means different things to different reporters.
- **Source D is not about falls.** A drop rig measures impact force on a dummy; there is no person, no ward, and no fall.
- **Source A's two wards were the two worst**, which is a Chapter 7 problem the reader should recognise unaided.
- **The lead author of B chairs the group that wrote C's definitions**, and two panel members ran A's pilot. Neither is visible in any number.
- **The support factor is continuous coverage**, and the trust can cover about 60% of a bay with the gaps along the bedsides — where a person falling out of bed lands.
- **A strong answer notices that D is the most useful unsuitable source**: it quantifies what the surface does per impact, which is one term in a coverage argument the trust could make this month.

## What a strong Form B answer should notice

- **The four rules: −25%, −22%, −6.4%, −35%.**
- **Source C takes 95.7%**, with "fraud loss" meaning gross attempted fraud to some members and net write-offs to others — a difference that could be larger than the effect.
- **Source D has no customers in it**, and no ninety-second hold, so it measures detection rather than loss prevention.
- **Source B's fifteen banks all run the vendor's platform**, which carries the identifier the rule uses. The bank does not run it in the new market — so B is arguably a different-quantity source too, and a reader who spots this has done more than required.
- **The vendor sits on the consortium's standards committee**, and two panel members ran the pilot.
- **The support factor is the shared registry**, and the new market has none. Nightly batches cannot answer a ninety-second query.
- **A reader may object that fraud losses are the wrong variable**, since the bank also cares about false-positive friction on legitimate customers. That is an item-1 observation and should be credited.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Supplied facts | 6 | 6 | ✓ |
| Produce items | 7 + paragraph | 7 + paragraph | ✓ |
| Sources | 5 | 5 | ✓ |
| Size span | 2 to 900 | 3 to 620 | ✓ |
| Estimate span | factor of 13 | factor of 9.6 | ✓ close |
| Largest source's weight | 97.6% | 95.7% | ✓ |
| Size-weighted is nearest zero | ✓ | ✓ | ✓ |
| Different-quantity source has the largest effect | ✓ | ✓ | ✓ |
| Dependencies | 2, both people | 2, both people | ✓ |
| Support factor is physical/institutional | physical | institutional | ✓ by design |
| Combined number forbidden in the close | ✓ | ✓ | ✓ |
| Word count | comparable | comparable | ✓ |

Arithmetic for both forms was computed and checked before the forms were written; the values in `transfer-rubric.md` are the checked values, including the weight shares.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| Same-question check first | 2 |
| Multiple rules | 3 |
| Size rejected as a weight | 4 |
| Dependence | 5 |
| Replication's limits | the closing paragraph, and diagnosis 3 in §6 |
| Support factor | 6 |
| Verdict | 7 and the closing paragraph |

**One dimension is only partly exercised.** *Replication's limits* has no dedicated Produce item, because neither form supplies a replication history — adding one would have made the forms longer than 45 minutes allows.

It is exercised in the chapter's §6 diagnosis task instead, and this mismatch is recorded here rather than left for a reader to find, following the practice `../07-targets-identification/transfer.md` adopted after the Chapter 6 rubric mismatch. **Two options are available and this file does not choose between them:** drop the dimension from the rubric, or add a sixth supplied fact giving a replication history and accept a longer form.

## Pilot notes

Untested. Four things a pilot should measure.

**Time.** 45 minutes for seven items plus a committee paragraph. Shorter than Chapters 7 and 8 at 50, matching the chapter's smaller budget.

**Whether readers run the same-question check first.** If most produce a weighting and then notice the sources differ, the ordering discipline did not land and the fix is in §2 of the chapter, not in the form.

**Whether the support factor is found without prompting.** It is fact 5 of six and is written as an operational detail. If most readers miss it, the forms should flag it less rather than more — the chapter's claim is that it reads as housekeeping in real reports.

**Whether the no-combined-number constraint holds.** If readers produce a hedged single figure anyway, that is the most informative possible pilot result and belongs in the chapter rather than the form.
