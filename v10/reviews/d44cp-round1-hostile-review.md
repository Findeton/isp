# D44c-P — round 1, hostile review

**Frozen 2026-07-25.**  Subject: `d44cp_funnel_lemma_exact.py`
(27 PASS / 0 FAIL, exit 0), LOG #406 (pin) / #407 (result), note
`note-d44cp-funnel-lemma-result.md`.  This round is the condition
paper 32's §6 item 7 amendment was queued behind.

---

## MAJOR P1 — FG5/FG6's 67,403 certifications are THEOREM-PASSES, not evidence

**The finding.**  The receipt reports that 67,403 arb-induced
subposets were certified dimension <= 2 by explicit realizer, with
the g2 oracle agreeing on every one.  The number is large and the
objects are not.  Measured over the width-3, cap-6 family, the
distribution of arb-subposet SIZE is:

| arb subposet size | count |
|---|---|
| 1 | 40,368 |
| 2 | 9,012 |
| 3 | 183 |

**Maximum: 3 elements.**

**Why that empties the gate.**  The smallest poset of order
dimension greater than 2 is the 3-crown S3, which has **six**
elements.  Every poset on five or fewer elements therefore has
dimension <= 2 **by cardinality alone**, with no reference to the
grammar, the confinement clauses, or the forest property.  FG5 and
FG6 certified 67,403 objects whose verdict was fixed before the
receipt looked at them.

**This is a discipline the parent receipt already had and this one
dropped.**  D44c's AG2d explicitly tags width <= 2 rows
`[theorem, not evidence]` and AG4 gates a non-empty EVIDENCE
stratum for exactly this reason.  D44c-P applies no analogous
cardinality stratification.

**What survives.**  T2's HYPOTHESIS gate is unaffected and remains
live: the forest property is not automatic at small cardinality —
a 3-element V poset violates it, and FG7(b) demonstrates the gate
firing on precisely that shape.  The 23,226 incomparable arb pairs
are a genuine stratum.  What is NOT supported is the impression
that the dimension conclusion was tested in-family; it was not.
The dimension content of T2 comes from the WRITTEN PROOF plus
FG9's grammar-independent enumeration, and from nowhere else.

**Required repair.**  Stratify FG5/FG6 by arb-subposet cardinality;
report how many certifications lie at size >= 6 (the minimum at
which the verdict could have gone the other way); and if that
stratum is empty, say so in the gate text and in the note.

---

## MODERATE P2 — "machine-verified ⇒ licenses the word THEOREM" overclaims

FG9's text says the enumeration of rooted forests on <= 8 nodes
"is what licenses the word THEOREM for the implication".  It is
not.  A finite enumeration to n = 8 licenses a statement about
n <= 8; what licenses THEOREM for all n is the **proof** in note
§2, which the enumeration corroborates.  The receipt has the proof
and should credit it.

Sharpened by P1: n <= 8 is precisely the range in which the
in-family objects live, so the enumeration and the family cover the
same small regime and neither reaches the interesting one.

**Required repair.**  Restate FG9 as corroboration of a proved
implication, not as its license.

---

## CLEAN, and one gap closed in the parent's favour

**R-B — the dedup convention is now MEASURED, not just declared.**
D44c deduplicates by the register-word class on the declared
ground that "event_poset is a function of the regs_of sequence;
vname registers are single-writer, hence pred-inert".  D44c-P's own
L3 result appeared to sit awkwardly with that: 23,844 causal pairs
share NO actor register, so some links are carried by vname
registers alone.  Direct check over the width-3, cap-6 family:

> **230,706 cover pairs; cover pairs with disjoint actor register
> sets: 0.**

Every cover shares an actor register.  The actor-word therefore
determines the cover relation and hence the poset, and the L3
violations are all transitive — consistent with the receipt's own
finding that zero of them are covers.  **The parent's declared
convention is thereby confirmed by measurement rather than
assumption**, which it had not previously been.

Also checked and clean:
- FG9's enumeration count: sum of n! for n = 1..8 = 46,233 —
  matches the receipt exactly; the parent(i) < i labelling is a
  topological one, so every rooted forest is reached.
- The near-miss mutant FG7(d) genuinely discriminates: reversing
  only the child order fails on a two-root forest.
- The run-1 dedup defect and the run-1 FG8 self-defeating gate are
  both owned in the note §6; the resample gate that caught the
  first is retained and reads zero.
- T1/L3/L1 falsifications are reported as deliverables at exit 0,
  and the L3 triple-coincidence is explained structurally rather
  than shipped.
- The distinction between falsifying THIS receipt's reconstruction
  and falsifying the round's own pool-laminarity route is stated
  correctly and repeatedly.

## Verdict

**REPAIRS REQUIRED before the paper-32 amendment is applied.**  P1
(stratify by cardinality; the dimension certification is a
theorem-pass at the observed sizes) and P2 (FG9 corroborates, the
proof licenses).  T2 survives as a theorem — its proof and its
hypothesis gate are both intact — but the note and the amendment
must not imply the dimension conclusion was tested on the
families.

---

# DELTA — repairs verified, 2026-07-25

**P1 REPAIRED.**  FG5/FG6 now stratify by arb-subposet cardinality
and print the distribution: sizes {1: 44,546, 2: 19,796,
3: 3,061}, **maximum 3**, EVIDENCE stratum (size >= 6) = **0**.
The gate states in its own text that **all 67,403 certifications
are THEOREM-PASSES, not evidence**, that their verdicts were fixed
by cardinality before the receipt looked, and that T2's dimension
content comes from the proof plus FG9 and from nowhere else.  The
note §2 carries the same correction.

**P2 REPAIRED.**  FG9's text now says a finite enumeration to
n = 8 licenses a statement about n <= 8 and nothing more, that the
PROOF licenses THEOREM, and that the enumeration is
grammar-independent corroboration — with P1's sharpening noted
(n <= 8 is exactly the in-family range).

**Post-repair state.**  28 PASS / 0 FAIL, exit 0.  Note status
changed from GREEN-UNREVIEWED to ROUND-1 REVIEWED AND REPAIRED.

**Unchanged:** the entry-condition discharge (sixth clause and
up-cone confinement over 23,226 live pairs), T2's proof and
hypothesis gate, the T1/L3/L1 falsifications, the triple-coincidence
explanation, and the reconstruction-vs-round's-route distinction.

**TERMINAL** for round 1.  **The paper-32 §6 item 7 amendment is
hereby UNBLOCKED**, in the four-clause form of note §5, with one
addition forced by P1: the amendment must not imply the dimension
conclusion was tested in-family.
