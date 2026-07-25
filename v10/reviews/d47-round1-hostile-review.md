# D47 (a + b) — round 1, hostile review

**Frozen 2026-07-25.**  Subject: `d47a_sky_instrument_exact.py`
(19 PASS / 0 FAIL) and `d47b_transport_skies_exact.py` (13 PASS /
0 FAIL), LOG #409/#410.  Pin `note-d47-sphere-rung-pin.md` §7
requires a round after D47b regardless of outcome.

Both receipts exit 0 with every gate green.  **Two MAJOR findings
below survive; both are gates that pass while measuring something
other than what they claim.**  Neither invalidates the unit's
headline, and one of them sharpens it.

---

## MAJOR R1 — TG5's "construction-matched null" is BOTH miswired AND vacuous by design

**The wiring bug.**  `null_of` identifies an event's actor by
scanning the event tuple for the first single alphabetic character.
Transport events look like `('d', 'B', 'D', ('v','v0'))` and
`('p', 'A', ('v','v0'), 1)` — so the first single alphabetic
character is the EVENT TYPE (`'d'`, `'p'`, `'r'`, `'n'`), never the
actor.  Measured over 720 sampled events: **the extraction returns
the type on 100% of events and the actor on none.**  The object
TG5 calls "an interaction-free per-actor chain null" is in fact a
"same-event-type chain" null — a different construction entirely.

**The deeper defect, which the bug conceals.**  Fixing the
extraction would not rescue the gate.  ANY null built as a
disjoint union of totally ordered groups gives every element
exactly one cover, so its maximum sky size is **1 by
construction**, for any grouping whatever.  TG5 therefore *cannot
fail*: it compares transport's 4 against a null that is
arithmetically incapable of exceeding 1.

**Consequence.**  TG5's conclusion — "the sky sizes are produced by
cross-actor causation and are not a construction tautology of
carrier size" — **is not supported by the gate that claims it.**
The claim may well be true; nothing in D47b establishes it.  This
is precisely the D46f failure mode the gate was written to prevent,
reproduced inside the prevention.

**Required repair.**  A null that COULD produce large skies if the
effect were an artifact: same event count and same number of cover
relations as the real record, but the relations rewired under a
random linear order.  Only such a null makes the comparison
informative.

---

## MAJOR R2 — SG10's capacity law confounds POINT COUNT with DENSITY

**The finding.**  `lattice_points(N)` draws N points from a box
whose extent scales with N (`t < 4N`, `x, y < N`).  The box volume
therefore grows as ~4N³ while the point count grows as N, so the
sprinkling gets **sparser** as N increases.  SG10's table is not a
measurement of "sky size versus record size"; it is a measurement
of sky size versus two variables moving in opposite directions.

**The control.**  Re-run with the box HELD FIXED at 160:

| N | max \|SKY-A\| (growing box, SG10) | max \|SKY-A\| (fixed box) | decidable (fixed box) |
|---|---|---|---|
| 20 | 3 | **4** | 4/20 |
| 40 | 8 | 7 | 12/40 |
| 80 | 10 | 9 | 48/80 |
| 160 | 14 | 14 | 120/160 |

**At fixed box, N = 20 already decides** — where SG10 reported 3
directions and zero decidable base events.

**Consequence.**  SG10's headline number, "shatter-4 first becomes
decidable at N ~ 40", is **an artifact of the box-scaling choice**
and must be withdrawn as stated.  It is carried into D47b's TG6
and into the result note §4, both of which inherit the defect.

**What survives, and is sharpened.**  The correct variable for
Minkowski is DENSITY, not point count.  The unit's central
contrast then reads more sharply, not less: **Minkowski buys sky
size with DENSITY; transport buys it with ACTOR WIDTH.**  The
"depth cannot buy what only width can" result for transport is
untouched — TG2 holds actor width fixed and varies depth directly,
with no analogous confound.

---

## Checked and CLEAN

- **The demotion (SG3b) is sound.**  554 decidable pairs, 121
  circular-ones rejections of genuine 2+1 skies, zero shatterings.
  The conclusion that arc-realizability is not a usable 2+1 proxy
  follows, and does not depend on either defect above.
- **SG0's separator is genuinely constructed.**  Arc and cap
  systems built and tested in exact Fractions; the opposite-edge
  certificate verifies.
- **SG3's vacuity gate is honest** and correctly refuses to let a
  0-of-54 pass read as confirmation.
- **TG2's actor-width measurement is not confounded**: depth is
  varied at fixed width and the sky does not move.
- **TG2(c)'s in-receipt retraction of the plateau** is a correct
  self-catch; the "no ceiling" statement is properly scoped.
- **SKY-B's directions do form an antichain** (equal global height
  implies incomparability), so the definition is well-formed even
  though "height difference d" is not "distance d from e" — a
  definitional caveat worth stating, not an error.
- The AST anti-vacuity scans carry their LOG #403 MA-2 scoping
  correctly in both receipts.

## Verdict

**REPAIRS REQUIRED before terminal.**  R1 (rebuild the null so it
can fail) and R2 (report both scalings; withdraw "N ~ 40" as
stated and restate the Minkowski variable as density).  The unit's
headline — the sky is an actor-width phenomenon, and the
one-sidedness doctrine is empirically necessary — survives both.

---

# DELTA — repairs verified, 2026-07-25

**R1 REPAIRED, AND IT REVERSED A HEADLINE.**  The null is rebuilt
as a link-count-matched random DAG (same carrier size, same cover
count, relations re-drawn under a random linear order — a
construction that CAN concentrate covers).  It reaches **7
directions with 362 decidable triples** against transport's **4**.

So the comparison came out the OTHER WAY.  The original TG5 claim
— "the sky sizes are produced by cross-actor causation" — is
**WITHDRAWN**.  The correct statement is that **transport skies
are NARROWER THAN CHANCE**: the law constrains sky size below the
generic value at matched carrier and link count.  TG5(b) is
written to report whichever direction the comparison takes, and it
took this one.

This strengthens the unit's headline: the actor-width bound is a
real restriction imposed by the law, not a by-product of record
size.

**R2 REPAIRED.**  SG10 now reports both scalings side by side.
Fixed box (160): max |SKY-A| = 4, 7, 9, 14 at N = 20, 40, 80, 160,
**decidable already at N = 20**.  Growing box: 3, 8, 10, 14, first
decidable at 40.  The headline "N ~ 40" is withdrawn as stated and
the Minkowski variable is restated as **DENSITY**.

**Post-repair state.**  D47a 20 PASS / 0 FAIL, D47b 14 PASS / 0
FAIL, both exit 0.  Note updated: §4 rewritten in density terms
with the withdrawal recorded, §6 rewritten around the reversal,
status line changed from GREEN-UNREVIEWED to ROUND-1 REVIEWED AND
REPAIRED.

**Unchanged and still clean:** the demotion (SG3b), SG0's
constructed separator, SG3's vacuity gate, TG2's actor-width
measurement, TG2(c)'s in-receipt plateau retraction.

**TERMINAL** for round 1.  Residues carried to the note §9, plus
one new one: the rebuilt null is crude (it matches carrier size and
link count but not height/width profile), so "narrower than chance"
is established against THAT null and not against every reasonable
one.
