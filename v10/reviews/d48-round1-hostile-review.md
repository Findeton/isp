# D48 — round 1, hostile review

**Frozen 2026-07-25.**  Subject: `d48_composite_line_exact.py`
(9 PASS / 0 FAIL, exit 0), LOG #413 (pin) / #414 (result).

---

## MAJOR D1 — the merge test decides a question about LABELS, not about CAUSAL ORDER

**The finding.**  CG3 declares admissibility of the *literal*
renamed event sequence.  That is a statement about the record's
bookkeeping — mint chains, base version names — and this program's
own thesis is that the physics is the **causal order**.  The
labelled test and the causal test are different questions and the
receipt runs only the first.

**The control.**  For every fine record whose literal image fails,
ask instead: is the image's causal poset realized, up to
isomorphism, by SOME admissible coarse record of the same length?

| cap | failing images | causal poset realized by an admissible coarse record |
|---|---|---|
| 4 | 10,608 | **10,608 (100%)** |
| 5 | 196,304 | **196,304 (100%)** |

**Zero exceptions in 206,912 cases.**  At the level of causal
structure, actor-merging never produces an unrealizable shape.

**Consequence.**  D48's headline "ACTORS ARE NOT AGGREGABLE" is
**too strong as stated**.  What is established is that the
*labelled record* does not aggregate — the mint chain breaks — and
that says nothing directly about whether the causal order does.

**The counter-consideration, which must be reported with it.**  The
coarse world is causally impoverished: it has only 1, 2, 3, 5, 8
poset iso-classes at lengths 1–5, so a "match" is cheap and the
causal test discriminates weakly.  Cheapness cuts both ways,
though — it is itself the finding, see D2.

---

## MAJOR D2 — the real obstruction is LOSS, and it was never measured

Counting causal poset iso-classes on both sides:

| length | FINE (4 actors) | COARSE (2 actors) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 4 | 3 |
| 4 | 9 | 5 |
| 5 | **19** | **8** |

Coarse-graining collapses 19 distinct causal shapes onto 8 at
length 5, and the gap widens with length.  **The coarse
description is never impossible — it is massively lossy.**

That relocates the d41c blocker onto firmer ground.  The bridge
does not fail because the layer forbids describing a composite as
one line; it fails because that description **discards most of the
causal structure**, so any bound extracted through it is a bound
on the coarse world and not on the fine one.  A declaration whose
observable is computed after a lossy projection cannot be read
back as a statement about the underlying record.

**Required repair.**  Add both measurements to the receipt, narrow
the headline to the labelled record, and restate the d41c
disposition in terms of loss rather than impossibility.

---

## Checked and CLEAN

- **The controls are real and they held.**  Identity and bijective
  renaming both return 21,428/21,428.  Equivariance under actor
  *names* is genuinely established, so the merge result is about
  cardinality and not labelling conventions.
- **CG4's mechanism is correct and exhibited**: two actors
  proposing on the same base, merged into one actor proposing
  twice on a base its own line has left.  The mint chain is indeed
  the obstruction.
- **CG5's monotone fall is real** (100 → 88 → 70 → 48%), though it
  should be flagged that a monotone fall is partly what one
  expects combinatorially once any breaking pair suffices — the
  receipt should not lean on the *shape* of the curve.
- **CG6 was written as an assertion, it FIRED, and the assertion
  was withdrawn** rather than the gate weakened.  Correct
  handling; the surjectivity result (1,190/1,190) stands and is
  consistent with D1.
- **The scope discipline is exemplary and must be preserved**: the
  actor-to-constituent step is declared an unsigned bridge in the
  pin, in the receipt banner, and in the verdict.  Nothing in
  either review finding touches it.

## Verdict

**REPAIRS REQUIRED.**  D1 (the headline overstates: labels, not
causal order) and D2 (measure and report the loss; restate the
d41c disposition around it).  The unit's value is not reduced —
D2 gives the blocker a better foundation than the one it had.

---

# DELTA — repairs verified, 2026-07-25

**D1 REPAIRED.**  New gate CG8 asks the causal-order question
directly and in-receipt: of the 10,608 records whose literal merged
image is inadmissible at CAP 4, **all 10,608** have a causal poset
realized by some admissible coarse record — zero exceptions.  The
CAP-5 figure (196,304, also 100%) is carried in the receipt as
REFEREE-CARRIED from this frozen round.  The headline is narrowed
from "ACTORS ARE NOT AGGREGABLE" to **"THE LABELLED RECORD DOES
NOT AGGREGATE, BUT THE CAUSAL ORDER DOES"**, in the gate text, the
verdict and the note.

**D2 REPAIRED.**  New gate CG9 measures the loss in-receipt: fine
(4-actor) causal poset classes 1, 2, 4, 9 at lengths 1–4 against
coarse (2-actor) 1, 2, 3, 5 — a gap of 4 at length 4, with the
widening to 19 vs 8 at length 5 carried as REFEREE-CARRIED.  The
d41c disposition is restated: **the blocker stands ON LOSS, not on
impossibility.**

**Post-repair state.**  11 PASS / 0 FAIL, exit 0.

**TERMINAL** for round 1.  Residue: the loss is measured in poset
iso-class COUNTS, which is a crude information measure; a
per-record loss (how many fine records share one coarse image) is
the natural refinement and is not done here.
