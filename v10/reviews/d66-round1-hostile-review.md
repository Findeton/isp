# D66 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D66 "the arbitration crystal" —
`note-d66-arbitration-crystal-pin.md` (STRICT, committed at c4d0352, before
the receipt), `note-d66-arbitration-crystal-result.md` (GREEN-UNREVIEWED),
`code/d66_arbitration_crystal_exact.py` + `data/d66_arbitration_crystal_exact.out`
(20 PASS / 0 FAIL, exit 0), LOG #471.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`indep.py` / `mycoc.py` / `dg.py` / `cc.py` / `run1.py` …
`run16.py`, scratch under
`/private/tmp/claude-501/.../scratchpad/d66rev/`): my own record driver
re-typed from the note's blueprint prose, my own immediate-predecessor
relation `P`, my own transitive closure, my own longest-chain heights, my own
SKY-B, covers, profile, width histograms, my own port conventions and wire
words, my own fibre-map / classify / cocycle / coboundary / parity /
free-relabelling code, my own menu driver and full-menu replay. The only
object I share with the unit is the layer under test (`d42b1`'s
`candidates_for` / `admissible` / `regs_of` / `vname` / `View` / `V0`).
Calibration: `reviews/d63-round1-hostile-review.md`,
`reviews/d64-round1-hostile-review.md`, `reviews/d65-round1-hostile-review.md`.

**VERDICT: REVISE. 1 BLOCKER / 5 MAJOR / 8 MINOR / 4 NIT.**

**The arithmetic is completely sound.** I rebuilt all fifteen conflict
configurations from the note's blueprint description with my own driver and
measured them with my own instrument: **every figure in every table of the
note and the receipt reproduces exactly** — the headline `RING(6,10)` at 117
events / arb `10/39` / homogeneity `9/13` / `|D| ≥ 4` `0.2308` / `max 4` /
`ω 0.7500`; the three-variant table including the `sticky = 0` collapse
(90 events, arb `1/3`, homogeneity `3/5`, `max |D| = 2`); every width
histogram; `GRID(3,·)` at `max 6` and `GRID(4,4)` at `max 8`; the whole A4
census (`GRID(3,10)` 92 charts / 27 wide / 90 pairs / 61 triples, REG
identity 63 + length-changing 27, ARBLOSE identity 22 + other 41, zero
obstructions by all three routes at all five conventions); the ring
obstruction counts 5 and 9 and the `d = 3` parity counts 20 and 36; the
`RING(6,10)` witness edge (charts 100/104, both arbitrations at height 25,
both width 4, transition τ); the seven blind ROLE cells; the A5 mass census
including the off-ladder `13/12` and `19/16`. **The `|D| = 8` witness is
real**: event 4 of `GRID(4,4)` is a 4-proposer arbitration at height 1 whose
eight directions are pairwise distinct, all at height 3, all in the future
cone of the committed order, with role words `(p, 0)` and `(p, 1)`,
`p = 0..3` — exactly as printed. The receipt reruns 20 PASS / 0 FAIL,
exit 0, byte-identical to the committed `.out` apart from timings.
**W4c's bound is correct and I could not break it**; better, I proved its
missing step and I *saturated* it.

**The BLOCKER is what saturating it costs the unit.** `max |D| = 2k` is not a
law about `k`-proposer crystals — it is a fact about *these* schedules. The
true ceiling is W4c's own `k²`, and I attain it: a forced, menu-offered,
C1-graded conflict crystal whose 3-proposer arbitrations carry
**`|D| = 9` at `d = 2`**, three of them per round, in a record with **zero
in-round deliveries** and an arbitration share that **saturates `1/(k+1)`**.
The same construction refutes the unit's design finding — the delivery is
*not* what gives the crystal its second direction; a second concurrent
conflict group does it better — and it answers the unit's own residue 2 at
`d = 3`.

---

## BLOCKER 1 — `max |D| = 2k` is not a law: `k²` is realized, W4c's bound is TIGHT, and the "mechanism legible in the chart" is a property of these schedules only

**Where.** Note **title** ("`max |D| = 2k` at `d = 2` for a `k`-proposer
crystal, against 4 for any delivery circuit"); §1 ("THE WIDTH DOOR OPENS");
§3's mechanism sentence ("**The mechanism is legible in the chart itself:
each proposer contributes one direction per wire of its next delivery, so
`max |D_e(2)| = 2k`**"); §7 licensed claim (iii) ("at `max |D| = 2k` for a
`k`-proposer crystal"); receipt VERDICT block ("The measured law in this
family is max |D| = 2k at d = 2 for a k-proposer grid"); LOG #471
("**THE WIDTH DOOR OPENS: max |D| = 2k at d = 2 for a k-proposer crystal**").

**Defect.** W4c says `|D_e(d)| ≤ Bl^d`, so for a `k`-proposer arbitration in
a record with `Bl = k` the `d = 2` ceiling is `k²`, not `2k`. The unit reads
`2k` off two schedules in which **every depth-1 successor of an arbitration
is a delivery** (live out-degree 2), and then states the sharp equality as a
law and as a mechanism. The grammar does not force it. An arbitration's
proposer register can be consumed by *another arbitration* — an actor may
hold two live proposals on two distinct unsuperseded bases
(`prop_options_in_view` blocks only a second live proposal on the *same*
base), and the second arbitration then has the first as its immediate
predecessor on that register. Each such successor contributes `k` directions,
not 2. Nothing in the note, the receipt or the pin tests this, and it is the
computation that decides the headline.

**Recomputation (mine).** Three records, all built with my own driver by the
layer's own restricted menu, every event specified by its full tuple, **hits
= 1 at every step, no refusal**, my closure of `P` verified equal to the
committed `event_poset` on every one:

```
  (1) run3.py — 26 events, 17 actors.  A 3-proposer arbitration (index 15,
      height 7, 4 registers, live out-degree 3) whose proposer A is
      immediately followed by a SECOND 3-proposer arbitration:
         D(1) = [16 'r', 17 'd', 18 'd']        (out-degrees 3, 2, 2)
         |D_e(2)| = 7   >   2k = 6              (W4c bound 9)

  (2) run4.py — 44 events, 24 actors.  ALL THREE proposer registers
      consumed by 3-proposer arbitrations:
         D(1) = [32 'r', 33 'r', 34 'r']
         |D_e(2)| = 9  =  k^2  =  W4c's bound, SATURATED
      (2k would be 6; the unit's widest chart anywhere is 8)

  (3) dg.py — DOUBLE-GRID(3, R), a TILING conflict crystal: rows AND
      columns conflict CONCURRENTLY, every actor carrying two live
      conflicts, so no delivery is needed in any round.
         R = 2:  72 events, hits [1,1], no refusal, arb share 1/4
         R = 4: 120 events, hits [1,1], no refusal, arb share 1/4
         deliveries: 12, ALL in the bootstrap; zero in every round
         d = 2: homogeneity 31/60 = 0.5167, |D| >= 4 at 0.0917,
                max |D| = 9, omega 0.5566
                width histogram {0:10, 1:48, 2:5, 3:46, 4:2, 9:9}
                — NINE charts of width 9, three per round
         d = 3: homogeneity 47/60 = 0.7833  [INSIDE the d=3 band],
                |D| >= 4 at 0.3250, max |D| = 9
         W4c never violated (Bl = 3, bound 9, attained);
         every version register occurs in exactly one event's regs_of.

  FULL-MENU REPLAY (D60's C1 grade), all 9 actors offered at every step:
      DOUBLE-GRID(3,2): OK, 72/72 steps, max hits per specification = 1,
      widest full menu 536 candidates, 94 s.
  So the counterexample carries the same forcedness grade as the unit's
  own records — and a HIGHER one than the unit's wide record, whose
  replay is budget-cut at 108/174.
```

**What must change.** The correct statement, which the unit's own data
supports and which is worth more than the false one, is the two-line
refinement of W4c: `|D_e(2)| ≤ Σ_{y ∈ succ(e)} b(y) ≤ b(e)·Bl`, i.e. for a
`k`-proposer arbitration `|D_e(2)| ≤ k·Bl`; **`2k` is the case `Bl = 2`,
i.e. the case where every proposer's next event is a two-register event
(a delivery), which is what the RING and GRID blueprints impose.** The
title, §1, §3's mechanism box, §7 (iii), the receipt's VERDICT block and
LOG #471 must be restated as "these schedules realize `2k`; the bound is
`k²` and it is attained by a conflict schedule in which an arbitration's
successors are arbitrations". The genuine, stronger headline available here
is: **W4c's bound is tight, and the widest chart in the campaign is 9.**

---

## MAJOR 1 — the design finding is refuted: the delivery is NOT what gives the crystal a second direction, and the maximum-conflict schedule is NOT the one that cannot tile widely

**Where.** Note §2, the bolded design finding ("**The delivery is not a tax
on the conflict engine; it is what gives the crystal a second direction.**
That is the design finding, and it is the reason the arb share peaks at
25.6% rather than 33.3% in the records that tile"); §1 ("the schedule that
maximises the conflict share is the one that *cannot* tile widely"); §7
claim (i) ("saturating it when no rotation is required"); LOG #471 (same
sentence, bolded).

**Defect.** The evidence is a single schedule — `sticky = 0`, in which each
actor has exactly ONE conflict lineage, so its propose/arbitrate cycle is a
chain of diamonds and the depth-2 layer is a single event. That is a
property of *one live conflict per actor*, not of delivery-freeness. Give
each actor **two standing conflicts** and the deliveries vanish, the share
saturates, and the width comes back.

**Recomputation (mine).** `cc.py` — CONFLICT-CYCLE(M, R): every *edge* of the
M-cycle is a standing two-proposer conflict group with its own version
lineage; edges 2-coloured so each round has two arbitration layers; after
the bootstrap **no delivery is ever needed** (`View.holdings` hands the
minted version to both proposers, exactly as the unit observed).

```
  CONFLICT-CYCLE(6, 6): 126 events, hits [1,1], no refusal
     arb share = 1/3  — SATURATED, the same value as the collapsed ring
     deliveries = 6, ALL in the bootstrap; zero in every round
     d = 2: homogeneity 0.5317, |D| >= 4 at 0.1111, max |D| = 4, Bl = 2
     d = 3: homogeneity 0.7778, |D| >= 4 at 0.3254, max |D| = 4

  and DOUBLE-GRID(3,4) above: arb share 1/4 = the k = 3 bound, SATURATED,
     zero in-round deliveries, max |D| = 9.
```

So the maximum-conflict record at `k = 2` reaches the `k = 2` ceiling 4, and
the maximum-conflict record at `k = 3` reaches the `k = 3` ceiling 9. "The
delivery is what gives the crystal a second direction" is false; what gives
the second direction is **a second consumer of the proposer's register**, and
a concurrent arbitration is a better one than a delivery. The honest form of
the finding is the one the unit's own no-delivery ring supports and no more:
*a schedule in which each actor carries only one conflict lineage collapses
to width 2 and cannot be widened without a second consumer; rotation buys
that consumer with a delivery, and concurrency buys it for free.*

**Second half of the same defect.** §7 claim (ii) sells the rings as tiling
"with **conflict, not delivery, as its engine**" — but 27 of the headline
ring's 117 events (23%) are deliveries, and by the unit's own mechanism the
*width* half of its F3 pattern is carried by exactly those delivery wires
(the 4 directions are the two wires of each proposer's next delivery). The
tiling is conflict-driven; the width is delivery-driven. My delivery-free
`CONFLICT-CYCLE(6,6)` keeps the width (max 4) and **loses the band**
(0.5317 at `d = 2`), so the truly conflict-only F3 pattern is *not* exhibited
anywhere — by the unit or by me.

---

## MAJOR 2 — the anti-correlation finding and residue 2 are `d = 2` statements presented without the label, and the unit's own interior control at `d = 3` refutes them

**Where.** Note §3 ("**No swept configuration is both inside the homogeneity
band and past the ceiling.**" — no depth label); §3's preceding sentence
("the grids' interiors stay below the band (0.5646, 0.5263), so their
shortfall is **not** an ends effect"); §8 residue 2 ("Every `k ≥ 3` grid is
below the homogeneity band at `d = 2` and stays below under the interior
excision — unlike D63's ends effect"); LOG #471 ("width and tiling
homogeneity ANTI-CORRELATE across the sweep — no configuration is both
in-band and past 4"). Receipt A2(c) runs the interior control on **5 of 15**
records and at **`d = 2` only**.

**Defect.** This is D63 round-1 MAJOR 1 repeated in the same corpus: a
depth-conditional novelty sentence shipped without its depth. At `d = 3` the
excision the unit itself calls the mechanism-level reading puts two of the
three `k = 3` grids **inside** the band while they carry `max |D| = 6`.

**Recomputation (mine)** — D60's `C7` excision (`lo + 2 ≤ h ≤ hi − 3`), my
own instrument, on **all fifteen** records and at **both** depths:

```
                       d=2 FULL -> INTERIOR        d=3 FULL -> INTERIOR   max
  GRID(3,6)     0.5098[below] -> 0.5733[below]   0.6275[below] -> 0.6933[IN ]   6
  GRID(3,10)    0.5287[below] -> 0.5646[below]   0.6667[below] -> 0.7075[IN ]   6
  GRID(3,4)     0.4848[below] -> 0.5897[below]   0.5758[below] -> 0.6667[below] 6
  GRID(4,4)     0.4483[below] -> 0.5263[below]   0.5517[below] -> 0.5789[below] 8
  every rotating RING  0.65-0.71[in] -> 0.7500[in]   0.83-0.93[ABOVE] -> 1.0000  4
  RING sticky=0 0.6000[below] -> 0.6957[IN ]      0.2667[below] -> 0.3043[below] 2
  (d = 3 band [41/60, 49/60] = [0.6833, 0.8167], recomputed from the
   eleven genuine sprinklings in my own run.)

  and my DOUBLE-GRID(3,4), a k = 3 crystal:
      d = 3 FULL homogeneity 0.7833 [INSIDE the band], |D| >= 4 at 0.3250,
      max |D| = 9  — in the band AND past the ceiling, at once.
```

Three consequences. (a) The unlabelled "No swept configuration is both
in-band and past the ceiling" is a `d = 2` sentence and must carry the label.
(b) "their shortfall is **not** an ends effect the way D63's band membership
was" is refuted at `d = 3` for `GRID(3,6)` and `GRID(3,10)`: the excision
moves them into the band, exactly D63's ends effect. (c) Residue 2's open
question ("whether a schedule exists with `k ≥ 3` arbitrations at in-band
homogeneity") is **answered at `d = 3`** by the unit's own grids under its
own control, and answered outright by DOUBLE-GRID(3,4). Symmetrically, the
rings' in-band property is `d = 2` only — their `d = 3` interiors are at
homogeneity **1.0000**, above the band, at every one of them.

---

## MAJOR 3 — W4c is tagged `[THEOREM, verified]` and its load-bearing step is neither proved nor correctly stated; the theorem is TRUE and here is the proof

**Where.** Note §3 W4c box ("the version register an arbitration mints is a
**birth wire**: `regs_of` places a version name in exactly one event's
register set, so it has **no P-successor**" … "Gated, not asserted: across
every record built here every version register occurs in exactly one event's
`regs_of`"); receipt A2(b) gate; §7 claim (iii); LOG #471 ("[THEOREM,
verified]").

**Defect.** As written, the reason is at the wrong level. `regs_of` is a
function of one event; whether a *name* occurs in one or two events' register
sets is a property of the **record**, and the printed warrant for it is a
per-record census ("12–42 version registers per record, zero occurring
twice") — a measurement, not a proof. The campaign's own standard (D63's W4b,
proved and then attacked joint by joint) is that a `[THEOREM]` tag carries an
argument. Under a hostile reading the whole `Bl = #proposers` chain — and
therefore the "two-proposer records cannot exceed 4" corollary that is
claim (iii)'s correction of D63 — rests on 17 records.

**Recomputation (mine), and the repair.** The claim is *true* and provable in
four lines from the committed layer; I checked every step against the
committed source and by construction attempts:

1. **Versions occupy a register only where they are born.** `regs_of` gives
   `{a}` for `p`/`n`, `{sender, receiver}` for `d`, `{a, ('mw', a, pk)}` for
   `m`, and `props ∪ {vname(base, wkey, init)}` for `r`. **A delivery of
   version `v` therefore carries `v` in its payload (`op[3]`) and does NOT
   occupy `v`'s register** — that is exactly why the wire is dead, and it is
   the sentence the note should print. Merge-created names (`mname`) never
   appear in any `regs_of` at all.
2. So a version register recurs **iff two distinct arbitration events mint
   the same `vname`**, i.e. share `base`, the winner key's value tuple, the
   winner key's author tuple, and the initiator.
3. Two such arbitrations share at least one proposer register (the winner
   authors, and the initiator, are proposers of both). In `event_poset`, once
   an event touches register `r` it becomes `last[r]`, and every later event
   touching `r` inherits its whole past — so the later arbitration has the
   earlier one in its causal past.
4. The later one's `View` therefore contains the earlier arbitration, so
   `base ∈ view.superseded`; `arb_components_in_view` skips components whose
   base is superseded, `admissible` finds no matching component and returns
   `False`. **The second arbitration is inadmissible. QED.**

I also tried to build the collision directly (distinct triple sets with equal
author/value tuples on a common base) and the supersession step blocks every
attempt, as the proof says it must. **Verdict: W4c stands, its consequence
stands, and the note must (i) replace "`regs_of` places a version name in
exactly one event's register set" with the delivery-payload sentence plus
steps 2–4, or (ii) drop the `[THEOREM]` tag and call it what the receipt
gates: a measured fact about seventeen records.**

---

## MAJOR 4 — the wide record's "non-vacuous triviality" is carried by the wrong column: at four conventions the C7 cochain is IDENTICALLY ZERO, and at ARBLOSE the C7 route drops exactly the 41 maps the sentence invokes

**Where.** Note §4.1 ("**The triviality is not vacuous.** At four
conventions every length-preserving transition is outright the identity,
**with 52 testable Čech triples**; at ARBLOSE **41 of the 90 pairs carry a
non-identity map and the class is a coboundary anyway**" — followed by "That
… is the strongest single line in §4.1"); the A4(e) gate text; LOG #471
("non-vacuous: 52 testable Cech triples; ARBLOSE has 41 non-identity pairs
and is still a coboundary").

**Defect.** Two different vacuity problems, both inside the load-bearing
sentence.

**Recomputation (mine), `GRID(3,10)`, `d = 2`, my own cochain:**

```
  REG:      kinds {identity 63, length-changing 27}
            C7 cochain: 63 edges, of which NON-IDENTITY 0  -> obstruction 0
            PARITY:     63 edges, 0 non-identity           -> 0
            FREE: 81 classes, 0 obstructions;  PROBE 1 does not fire
  ARBLOSE:  kinds {identity 22, length-changing 27, other 41}
            C7 cochain: 22 edges, of which NON-IDENTITY 0  -> obstruction 0
            PARITY:     63 edges, of which NON-IDENTITY 41 -> obstruction 0
            FREE: 81 classes, 0 obstructions
```

(a) At REG / REGA / ARBVFIRST / COV the `Z/2` cochain is the **zero
cochain**: there is nothing to trivialize, and the 52 Čech triples test
`0 = 0 + 0`. That is D64's G1 sentence ("the atlas is flat at this
labeling"), and citing the triple count as evidence of non-vacuity is exactly
the move D64's round-1 MINOR 1 struck out ("a dead test"). What *is*
non-vacuous there is PROBE 1's failure to fire — the labeling could have
shown a transition and did not — and that is the sentence the note should
carry.

(b) At ARBLOSE, D64's `cochain` **drops the `other` class by construction**,
so the C7 column's "0" is computed on 22 identity edges and says nothing
about the 41 non-identity maps. The only computation on the wide record that
actually trivializes a non-trivial cochain is the unit's own **PARITY**
route (63 edges, 41 of them `g = 1`, obstruction 0) — and, independently, the
FREE route. The strongest line in §4.1 is defensible **only** when attributed
to PARITY/FREE; as printed it credits C7.

The A-IIIa verdict itself survives all of this — I reproduce zero
obstructions by all three routes at all five conventions and both depths, and
PROBE 1 does not fire at any wide-record cell (my own blindness test agrees
with the receipt's, cell for cell).

---

## MAJOR 5 — the odd-ring residue's own experiment costs 13 seconds, and it CONFIRMS the parity reading; the counts 5 and 9 are `R − 1`, not a ring quantity

**Where.** Note §4.2 ("the rotating `M = 6` rings … obstruct at both `R = 6`
and `R = 10` … **three sizes do not establish it**"); §8 residue 1 ("it needs
`M = 10, 12, 14` and a proof, not three sizes"); LOG #471 ("the ODD-RING
HOLONOMY residue").

**Defect.** The residue names a computation that the receipt could have run
in the time it spends printing about it, and the unit's own framing of the
magnitudes invites a misreading.

**Recomputation (mine)** — my own driver, my own census, REG, `d = 2`;
`RING(M, R)` costs 1–51 s per configuration:

```
  RING(M= 4,R= 6)  2 pairs/round  edges 23  non-id  3   obstructions 0
  RING(M= 6,R= 6)  3 pairs/round  edges 30  non-id 11   obstructions 5
  RING(M= 8,R= 6)  4 pairs/round  edges 40  non-id 16   obstructions 0
  RING(M=10,R= 6)  5 pairs/round  edges 50  non-id 21   obstructions 5
  RING(M=12,R= 6)  6 pairs/round  edges 60  non-id 26   obstructions 0
  RING(M= 6,R=10)  3 pairs/round  edges 54  non-id 19   obstructions 9
  RING(M=10,R=10)  5 pairs/round  edges 90  non-id 37   obstructions 9
```

**The parity reading survives at five ring sizes, not three:** odd
`M/2` (M = 6, 10) obstructs, even `M/2` (M = 4, 8, 12) is clean, and the
`M = 12` clean row is the one that could have killed it. Residue 1 should be
restated with these rows (and its remaining content is the *proof*, not more
sizes).

**And the magnitudes are not what they look like.** The obstruction count is
`5` at `R = 6` and `9` at `R = 10` **for both `M = 6` and `M = 10`** — it is
`R − 1`, a count of rounds, independent of the ring. Presenting "5 (R = 6)
and 9 (R = 10)" as the ring's obstruction invites reading a magnitude that
is not a ring quantity and not a cohomological one; the only invariant
statement available is `≠ 0`. (I did check that the count is not a
spanning-forest artefact: under six randomised DFS orders it is stable at 5,
5, 9, 9, 0, 0, 0 for the seven configurations above — so the *number* is
reproducible, it just is not about `M`.)

**On the disposition the task asks about: "filed, not claimed" is right.**
I confirm all four of the unit's reasons against the claim, with my own code:
the free-relabelling route returns 0 at every ring cell; the ring's chart
triples all have empty triple intersections at `d = 2` (0 testable, against
36 on `RING(4,10)` and 108 on the delivery crystal); the τ naming is a
convention; and the sprinkling controls obstruct too. I add the mechanism
that makes routes (b) and the free route consistent — the fibre maps are
*partial* and, with no 2-skeleton, the odd cycle's composite has empty
domain, so a global relabelling exists while the port cochain is not a
coboundary. What is over-stated is only the sentence "**the campaign's first
non-zero obstruction**" as a §4 heading: in the same run the genuine
sprinklings carry non-zero parity obstructions (10, 2, 19, 34), which the
note discloses in item 4 but not in the heading.

---

## MINOR 1 — the decisive A4 records are the ones whose C1 grade is a prefix or missing, and the one fully-replayed wide record is not in the A4 census

`A4SET` is `{HEAD, RING(4,10), RING(6,6), RING(8,10), RING(6,10,R),
RING(6,10,sticky=0), GRID(3,6), GRID(3,10), GRID(4,4)}`. The A-IIIa verdict
is read on `GRID(3,10)` (full-menu replay **BUDGET-CUT at 108/174**) and on
`GRID(3,6)` and `GRID(4,4)` (**never full-menu replayed at all**). The one
complete wide record that *is* replayed end to end, `GRID(3,4)` (66/66,
widest menu 530 — I reproduce it), is **not** in the A4 census. The cut is
printed and residue 4 admits the prefix, so this is honest; what is missing
is the sentence that says where the prefix bites. Mitigation, in the unit's
favour: the restricted-menu drive already establishes admissibility of every
event against the whole prefix, so the untested tail lacks only the
"offered among all actors" property — but that is precisely what D60's C1
grade *is*.

## MINOR 2 — the interior control runs on 5 of 15 records and at one depth

D63's round-1 MAJOR 3 forced its unit to run the excision on **every** member
of the pattern set; here it runs on five named records and only at `d = 2`,
while the note draws a mechanism conclusion from it ("their shortfall is not
an ends effect"). My full table is in MAJOR 2; the missing rows are the ones
that refute the conclusion.

## MINOR 3 — the budget bound's printed proof skips the step that carries it

A1(b) and §2 argue "a proposal is resolved by at most one arbitration
(`View.resolved`)". `View.resolved` is **view-relative** — it is rebuilt from
the arbitrations in one event's causal past — so as printed the argument does
not exclude two causally *incomparable* arbitrations each seeing the same
triple live. The bound is nevertheless true, by the same register argument as
in MAJOR 3 step 3: two arbitrations sharing a proposal share that proposer's
register, hence are comparable, hence the later one sees the triple resolved
and is inadmissible. I verified the conclusion numerically on all fifteen
records with my own count: `#proposals = Σ k` **and** the multiset of
consumed triples has no repeats (24/24, 40/40, 36/36, 60/60, 84/84, 80/80,
60/60, 60/60, 60/60, 60/60, 40/40, 36/36, 54/54, 90/90, 64/64).

## MINOR 4 — "`g = 2` reproduces `CONFLICT-RING(4, R)` exactly (gated)" — there is no such gate

The receipt's module docstring (line 40) claims a gate; no predicate anywhere
in the file tests it. And the strong form is false: the two event lists are
**not** equal (different actor names, `G00…` vs `C0…`), though the profile
rows do coincide exactly (n = 78, arb 10/39, homogeneity 9/13, `max 4`,
`ω 3/4`, both depths — I checked). Either gate the isomorphism or drop
"(gated)".

## MINOR 5 — "the in-band records are exactly the `k = 2` rings" is not what the census says

§3. The in-band ∩ wide set has ten members and one of them is
`GRID(g=2, R=10)`, which the note elsewhere presents as a *grid*. (It is a
`k = 2` object, so the substance is right; the sentence is not.)

## MINOR 6 — "all five port conventions" is four identical readings plus one

On the wide record at `d = 2`, REG, REGA, ARBVFIRST and COV return the same
number in **every** column (63/27, 0/0/0, 52 or 61 triples); only ARBLOSE
differs. The conventions *are* genuinely distinct labelings — I checked, and
they disagree with REG on 108 (REGA), 157 (ARBLOSE), 230 (ARBVFIRST) and 18
(COV) of the 284 (chart, direction) cells — so this is not a wasted census,
but the robustness sentence should say that the wide record admits **two**
distinct readings, not five.

## MINOR 7 — "against 4 for any delivery circuit" is a `d = 2` comparator, and D63's corrected census contradicts it at `d = 3`

The note's title and §3 table row ("any delivery circuit (D63) … measured
`max |D|` 4") carry the depth label in the title's first clause only. D63's
round-1 delta added the `d = 3` census in which **18 of 38** delivery
configurations exceed 4, with fourteen 5s and four 6s. The comparator row
must be depth-labelled where it is used, or it re-asserts a number its parent
already corrected.

## MINOR 8 — "the ring sits with the sprinklings" is a COV-only statement

§4.2 item 4 compares the ring's parity obstructions against the
sprinklings'. Sprinklings have no `H`, so only the COV instrument is defined
on them: the ring's four other conventions have no sprinkling counterpart.
The comparison is sound at COV (ring 9 vs sprinkling 10/2/19/34 vs delivery
crystal 0) and should say so.

## NIT 1 — "an arbitration's live out-degree IS its proposer count" is an inequality

A2(b)'s gate text and §3. It is `≤`: the last arbitration of each group at
the record's end has live out-degree **0**. My count of arbitrations with
`b < #proposers`: 2, 2, 3, 3, 3, 4, 3, 3, 3, 3, 2, 3, 3, 3, 4 across the
fifteen records. Nothing turns on it (the bound uses the max), but the gate
label states an equality the data refute.

## NIT 2 — A1(b)'s printed bound and its predicate are different statements

The prose says `#proposals ≥ k · #arbs` with `k` the smallest proposer count;
the gate checks the strictly stronger `#proposals = Σ k` (per-arbitration).
House style is to label a gate for what it measures.

## NIT 3 — "fifteen conflict configurations" contains one duplicate object

`GRID(g=2,R=10)` and `RING(M=4,R=10)` are the same record up to actor
renaming (identical event shapes, identical every column). D63 round-1
MINOR 8 asked for exactly this to be said out loud.

## NIT 4 — the exit-freedom scan carries D63/D64's declared narrowness

`_no_exit` is the widened Name/Attribute form and its scope is stated in the
docstring; a `getattr`-reached exit would still survive. Disclosed, so a note
only.

---

## Checked and CLEAN (D66)

Everything below is my own recomputation unless stated.

**A. Receipt rerun.** 20 PASS / 0 FAIL, exit 0, 652.5 s. Output diffs
**empty** against the committed `.out` after normalising the timing figures.

**B. The instrument, rebuilt from the committed definitions.** My own `P`
(immediate predecessor per register, mirroring `event_poset`'s `last`
bookkeeping), my own memoised closure, my own longest-chain heights, my own
SKY-B (`{f : C[e][f] and h[f] − h[e] = d}`), my own covers and my own profile.
My closure **equals** the committed `event_poset` on every record I built,
including the four adversarial ones. My `h2` / `h4` / `max` / `ω` columns are
D58's `atlas` columns on the same population (all events) at the same
depths — no population drift, no depth drift; the SKY-B statistic here is the
same statistic D58/D60/D63 used.

**C. The whole sweep, rebuilt.** All fifteen configurations re-driven from
the note's blueprint prose with my own driver: **every published row
reproduces to the last Fraction** at both depths — `n`, arb share,
homogeneity, `|D| ≥ 4`, `max |D|`, mean `|D|`, `ω`, and the full width
histograms (e.g. `GRID(4,4)` `{0:24, 1:40, 2:35, 4:11, 6:3, 8:3}`;
`GRID(3,10)` `{0:9, 1:73, 2:46, 3:19, 4:9, 5:9, 6:9}`). 1,593 events,
**zero refusals**, and at every step of every record the menu hits were
`min = max = 1` (I gated the minimum too, which the receipt does not).
The three-variant table and the `sticky = 0` collapse reproduce exactly, as
does the winner-convention invariance (`win = R` and `win = ALT` agree with
`win = S` in every column).

**D. The width witness, verified event by event against my own sky and my own
order.** `GRID(4,4)`, event 4: an `r`-event by `G00`, height 1, 5 registers,
**4 distinct proposers**, live out-degree 4. `D(1) = {20, 28, 36, 44}` (four
deliveries at height 2); `D(2) = {21, 24, 29, 31, 37, 39, 45, 47}` — **eight
pairwise-distinct events, every one at height exactly 3 = 1 + 2, every one
ordered after the base in my own closure (which equals the committed
order)**, with role words `(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0),
(3,1)`. The chart is not an instrument artefact and not a chart-counting
convention. The `|D| = 6` charts on `GRID(3,·)` reproduce identically.

**E. W4b and W4c, attacked and standing.** `|D_e(d)| ≤ Bl^d` holds with zero
violations at `d = 1, 2, 3` on every record I built, including the three
adversarial ones; `Bl` measured 2 / 3 / 4 exactly as published. Every version
register occurs in exactly one event's `regs_of` in every record — and I now
know *why* (MAJOR 3). The correction of D63's necessity statement is right:
3+ registers is necessary and not sufficient; 3+ **proposers** is what buys
width past 4 — and (BLOCKER 1) the ceiling it buys is `k²`, not `2k`.

**F. Forcedness.** Two full-menu replays of my own beyond the receipt's five
(`DOUBLE-GRID(3,2)` 72/72, widest menu 536; and the restricted-menu drive of
all fifteen records with the minimum hit count gated): no step anywhere was
refused or ambiguous. The receipt's own five replays reproduce, including the
budget cut at 108/174 with its printed budget.

**G. The A4 census, rebuilt from scratch.** My own port conventions, wire
words, fibre maps, classification, cocycle, coboundary DFS, parity route and
free-relabelling route reproduce **every cell** of the receipt's ring and
grid tables I checked: `RING(6,10)` 81 charts / 27 wide / 54 pairs / 35
identity / 19 τ / 0 triples / C7 9 / PARITY 9 / FREE 0 at REG, REGA, ARBLOSE
and COV, with ARBVFIRST's τ route vacuous at 0 and its parity route at 9;
`RING(6,6)` at 5 and 20; `RING(4,10)` clean with 25 non-identity pairs and 36
testable triples; `RING(8,10)` clean; the delivery-free ring blind at all
five; `GRID(3,10)` and `GRID(4,4)` trivial everywhere. The seven blind ROLE
cells are exactly the seven the receipt names. The witness edge (charts
100/104) is exactly as printed.

**H. The anchors.** The receipt reproduces D63's `DR(8,10,8)` row and D60's
brick event-for-event, the eleven genuine sprinkling configurations and the
bands `[77/120, 4/5]` and `[17/40, 13/20]` (I recomputed the bands
independently in my own run and got the same fractions at both depths), and
D64's committed C7 row (60 charts, 138 labelled overlaps, 9 components, 0
obstructions, ε 32/28, 0 survivors, 108 Čech triples, split 57/115, REGA
40/20). The instrument-validation gate (closure of `P` = the committed order)
holds on every substrate in my own recomputation too, including the two
sprinklings under COV.

**I. The budget bound.** Equality `#proposals = Σ k` on all fifteen records,
no consumed triple repeated, `1/3` attained exactly by the delivery-free ring
and (my addition) by `CONFLICT-CYCLE`, `1/4` by `DOUBLE-GRID`. The bound
itself is correct once the register argument is supplied (MINOR 3).

**J. The mass census (A5).** Recomputed independently for `RING(4,6)` and
`GRID(3,4)`: total masses `{4:34, 13/3:2, 9/2:10}` and `{9:46, 28/3:2,
19/2:6, 81/8:3, 43/4:9}`, ladder excesses and per-actor sums identical to the
receipt's, **including the off-ladder `13/12` and `19/16`** that reproduce
d42b1's committed N1 leak. The scope difference from D65 is stated in the
note rather than elided, and the labelling is honest.

**K. PROBE hygiene.** PROBE 1's firing cells are printed and excluded by
name; no outcome is read at RAW; the decisive wide-record cells are not
blind (my own blindness test agrees). The two added routes are validated with
a constructed true positive and true negative before use, exactly per d47a's
doctrine — and I confirm both validations (parity 1/0, free 1/0).

**L. Determinism, caps, exit protocol.** The hash-seed probe covers a ring
and a grid with its scope said aloud; the swept ranges, both depths, both
replay budgets, the only binding cut and the threshold inventory are all
printed; five anchors carry `anchor=True` and the exit line matches the code
(`sys.exit(1 if ANCHOR_FAIL else 0)`), which is exactly pin A0/A6. AST
anti-vacuity is the SG8 form with its scope stated.

**M. Scope.** Pin §5's clauses are all carried in note §6/§7 — grammar layer,
the swept family, #440's mechanism-not-objects, no measure at transport scope
(B1), no typicality, ω per D58's reading, D59's missing map untouched. The
note does **not** overgeneralise D64's successor question: it says the
question "stays open with its first non-trivial data point", not that no
substrate can carry a class. Subject to BLOCKER 1 and MAJOR 1–2, which are
mechanism sentences stated more widely than the sweep, no claim exceeds the
family.

**N. Provenance.** The pin (109 lines, STRICT) is committed at c4d0352,
before the receipt and the result note; its A-I/A-II/A-IIIa/A-IIIb
disjunction is the receipt's actual `OUTCOME` predicate; the pin's stated
lean ("tiling is the hard part") is reported as half wrong against the unit's
own interest; and the three limits in §3 plus six residues are all reported
against it as well. That discipline is why the two constructions in BLOCKER 1
and MAJOR 1 were worth building rather than assumed.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

**Verification of the BLOCKER.**  The referee's constructions are now
GATED IN THE RECEIPT, rebuilt independently by the repair pass with
EXACT MATCH on every published figure: DOUBLE-GRID(3,2/4) — 72/120
events, C1-grade full-menu replay 72/72 (widest menu 536), zero
in-round deliveries, arb-group share 1/4, NINE |D| = 9 charts (three
per round, each verified against the committed sky() and poset,
out-degrees [3,3,3]), W4c's ceiling k·Bl = 9 SATURATED, d = 3
homogeneity 47/60 = 0.7833 IN BAND with max |D| = 9.  The 2k "law"
is restated as a property of the swept RING/GRID schedules; the
ARBCHAIN(m,3) family gated occupying the whole interval |D| = 6..9.
Two schedule variants REFUSE (the mints-first design is forced),
gated.  **THE REPAIR FOUND A DEFECT IN THE REVIEW ITSELF**: the
stated refinement |D_e(2)| <= sum_y b(y) has 7 exceptions
(height-skipping P-edges into terminal arbs) — the airtight
containment D_e(2) ⊆ succ(e) ∪ ⋃succ(y) is gated instead, with
every exception characterised; the k² ceiling rests on W4c's Bl^d,
zero violations.  One disclosed discrepancy: RING(4,6)'s two
auxiliary columns (edges/non-id 35/15 vs the review's 23/3) — the
committed RING(4,10) row scales to the repair's numbers, the
obstruction count AGREES (0), the parity reading is untouched;
printed and disclosed.

**Repairs applied (receipt 29 PASS / 0 FAIL, 962 s, sweep 21
configurations / 2,325 events; note retitled):** the width law
corrected everywhere (ceiling k·b <= k², saturated); the design
finding inverted (delivery is NOT the second direction — a second
CONCURRENT CONFLICT AXIS is; the sticky = 0 collapse was the
pair-ring diamond's); depth labels (the anti-correlation was a d = 2
statement — at d = 3 the double grid is in-band AND wide, ANSWERING
residue 2); W4c's four-line structural proof written in and each
step quoted against d42b1 (payload-vs-register; vname recurrence
forces causal comparability, hence refusal — the D62 O2 pattern);
A4 accounting fixed (C7 zero at all five conventions, two reasons;
ARBLOSE domain shrink gated); the odd-ring residue = parity
(counts = R − 1, the referee's experiment gated); budget bound both
readings (k_min = 1 general 1/2; conflict groups 1/4); all
MINORs/NITs.  Both refuted mechanism sentences carried verbatim,
struck, in the note's §9.

**Verdict after repairs: the unit stands as restated — and the
round's constructive contribution is the campaign's strongest
geometric object: a delivery-free conflict crystal, in-band at
d = 3, saturating the true width ceiling.**  TERMINAL for round 1.
