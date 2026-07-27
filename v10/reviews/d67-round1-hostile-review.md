# D67 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-27.
**Unit under review:** D67 "the k = 4 double grid" —
`note-d67-k4-double-grid-pin.md` (STRICT, committed at 15a90a0, before the
receipt), `note-d67-k4-double-grid-result.md` (GREEN-UNREVIEWED),
`code/d67_k4_double_grid_exact.py` + `data/d67_k4_double_grid_exact.out`
(26 PASS / 0 FAIL, exit 0), LOG #475.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`mylib.py` / `dg.py` / `an42.py` / `ac5.py` / `verify5.py` /
`run44.py` / `level.py` / `inter.py`, scratch under
`/private/tmp/claude-501/.../scratchpad/d67rev/`): my own record driver
re-typed from the note's blueprint prose, my own immediate-predecessor
relation `P`, my own transitive closure, my own longest-chain heights, my own
SKY-B, my own profile and width histograms, my own interior excision, my own
menu driver and full-menu replay. The only objects I share with the unit are
the layer under test (`d42b1`'s `candidates_for` / `admissible` / `regs_of` /
`vname` / `View` / `V0` / `event_poset`) and, for cross-checking only, the
committed `d47a` `heights` / `sky`.
Calibration: `reviews/d66-round1-hostile-review.md` and its DELTA,
`reviews/d63/d64/d65-round1-hostile-review.md`.

**VERDICT: REVISE. 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT.**

**The arithmetic is completely sound.** I rebuilt the whole DOUBLE-GRID
family from the note's blueprint prose with my own driver and measured it
with my own instrument: **every figure in every table of the note and the
receipt reproduces exactly** — `(3,2)` at 72 events / arb `1/4` / 12
bootstrap deliveries / `d2` homogeneity `4/9` / `max 9`; `(3,4)` at 120 /
`31/60` / `d3 47/60` and the committed width histogram
`{0:10, 1:48, 2:5, 3:46, 4:2, 9:9}`; `(4,1)` `0.3250` / `max 4`; the
headline `(4,2)` at 120 events / arb `1/5` / 24 bootstrap deliveries /
`d2 49/120` `max 16` `{0:28, 1:43, 2:7, 3:10, 4:29, 16:3}` / `d3 13/24`
`max 16`; `(4,3)` `73/160` and `{0:28, 1:59, 2:7, 3:10, 4:49, 16:7}`; the
interleaved control at `9 → 5`; zero refusals and menu hits `min = max = 1`
at every step of every record I built. **The `|D| = 16` witness is real**:
events 73/74/75 are `r`-events at height 10 with four distinct proposers and
live out-degree 4, their four depth-1 successors 76–79 are four-proposer
arbitrations with out-degrees `[4,4,4,4]`, and the sixteen directions 80–95
are pairwise distinct `p`-events at height exactly 12, all ordered after the
base in my closure — which I verified **equals the committed `event_poset`
order event for event**, with **zero disagreements against the committed
`d47a.sky` at every event of the record at both depths**. W4c is never
violated; every version register occurs in exactly one `regs_of`. The
`ARBCHAIN*` correction to D66's blueprint is **right**, correctly scoped,
and I confirm textually that D66's `arbchain` hardcodes three-proposer
secondaries and that D66 only ever ran it at `k = 3`.

**What the round breaks is what the unit built the headline out of.** Three
things, all by construction rather than by argument:

1. **The note's flagship negative — "no *whole* `k = 4` record is in band at
   either depth" — is false one `R` past where the sweep stopped.** I built
   `DOUBLE-GRID(4, 4)` with the unit's own blueprint: 200 events, forced,
   zero in-round deliveries, `max |D| = 16`, and `d = 3` homogeneity
   `29/40 = 0.7250` — **inside the band as a whole record**, and inside the
   second band column (`|D| ≥ 4` at `0.6350`) as well. The §4 "frontier" and
   §7(v) go with it.
2. **The `k = 5` "obstruction" is a design failure, not a wall.** I built a
   forced, **C1-complete** (full-menu replay 157/157, widest menu 2,125)
   `k = 5` record with **`|D_e(2)| = 25 = k²`**, and a `k = 6` one with
   **36**. Residue 1 is closed in the direction the note guessed, and the
   `k = 5` shortfall belongs to `ARBCHAIN*`'s bootstrap ordering.
3. **Which makes "sprinkling-grade width" the wrong headline.** Width in
   this mechanism is `k²` with `k` a free design parameter; at `k = 5` and
   `k = 6` the same mechanism produces 25 and 36, **above the entire
   sprinkling range**. And on every width column except the extremal one the
   headline record is far *below* the sprinkling population, whose range
   `[10, 17]` is itself **bimodal by spacetime dimension** (`M21`: `[10,11]`;
   `M31`: `[14,17]` — 16 is not inside the 2+1 mode at all).

---

## BLOCKER 1 — "no whole `k = 4` record is in band at either depth" is false: `DOUBLE-GRID(4, 4)` is in the `d = 3` band as a WHOLE record at `max |D| = 16`

**Where.** Note **title line** ("Uniformity is the price: no *whole* `k = 4`
record is in band at either depth, though the interior of
`DOUBLE-GRID(4, 2)` is"); §1 ("That lean is **confirmed for whole records**
and refuted on the interior"); §4(i) ("**Whole records: no `k = 4` record is
in band at either depth.**"); §4's FRONTIER box ("At `k = 4` width 16 and
`d = 3` band membership compose **only on the interior**"); §7 licensed claim
(v) ("uniformity does **not** survive the width at `k = 4` on the **whole**
record at either depth"); receipt K4 gate ("(i) NO swept `k = 4` record is
inside the recomputed sprinkling homogeneity band at either depth, so the
pin's honest lean is CONFIRMED for whole records"); LOG #475 ("THE BAND: no
whole `k = 4` record is in band at either depth (the pin's lean held)").

**Defect.** The sweep stops at `R = 3` and the note reports the trend that
kills its own conclusion in the same sentence: `d = 3` homogeneity runs
`0.4625 → 0.5417 → 0.6562` at `R = 1, 2, 3` against a band whose floor is
`0.6833`. That is a monotone sequence one step below the floor, with the
increments *growing* (`+0.0792`, `+0.1145`). The note protects itself with
"still below at the largest `R` this receipt could afford" — but the four
sentences quoted above, and LOG #475, drop the scope and state the negative
as a property of `k = 4`. It is a property of `R ≤ 3`. The cost of the
missing row was one build.

**Recomputation (mine).** `run44.py`, my own driver, the same blueprint,
`R = 4`:

```
  DOUBLE-GRID(4, 4)   n = 200 events, 16 actors, arb share 1/5,
                      24 deliveries — ALL in the bootstrap, ZERO in any round,
                      menu hits [min, max] = [1, 1], NO refusal, 1133.0 s

    d = 2  homogeneity  97/200 = 0.4850   below [77/120, 4/5]
           |D| >= 4     0.4000            below [17/40, 13/20]
           max |D| = 16
           histogram {0:28, 1:75, 2:7, 3:10, 4:69, 16:11}

    d = 3  homogeneity  29/40  = 0.7250   *** INSIDE [41/60, 49/60] ***
           |D| >= 4     0.6350            *** INSIDE [3/5, 91/120] ***
           max |D| = 16
           histogram {0:34, 1:21, 2:12, 3:6, 4:73, 5:1, 6:3, 7:2, 16:48}
```

**A whole `k = 4` record, built by the unit's own blueprint with one more
round, is inside the `d = 3` homogeneity band while carrying
`max |D| = 16 = k²` — and, unlike the interior cell the unit shipped, it is
inside the second band column too** (MAJOR 4). The trend continued exactly:
the homogeneity numerators run 37/80, 65/120, 105/160, **145/200**.

**What must change.** The title line, §1, §4(i), §4's FRONTIER box, §7(v),
the K4 gate and LOG #475 must be restated. The honest form the data support
is the *opposite* of the one shipped, and it is the better result: **at
`k = 4`, width 16 and `d = 3` band membership DO compose on the whole
record, at `R = 4` — the same `R` at which D66's `k = 3` flagship achieves
it — and the `R = 2` interior result is that same phenomenon seen two rounds
early.** The pin's honest lean ("band membership should get HARDER as `k`
grows") is then **refuted in the direction of the unit's own interest**: at
`R = 4` the `k = 4` record is in band on both `d = 3` columns while the
`k = 3` flagship is in band on one. The whole §4 "frontier" — width and
uniformity composing only on the interior at `k = 4` — does not exist. See
also MAJOR 5, which says what "in band" is worth at all once you notice that
the family sweeps monotonically *through* the band.

---

## MAJOR 1 — the `k = 5` ceiling is reached: `k²` is realized at `k = 5` (25) and `k = 6` (36) by a forced, C1-COMPLETE record, so residue 1's "height alignment obstructs" is a design failure of `ARBCHAIN*`, not a wall

**Where.** Note §3 ("**AND THE CEILING IS NOT REACHED AT `k = 5` BY ANYTHING
BUILT HERE.** … the honest statement of the ladder is: `k²` is REALIZED at
`k = 3` and `k = 4` and UNREALIZED at `k = 5` by every schedule this unit
built; whether some `k = 5` schedule reaches 25 is open (§8)"); §8 residue 1
("`ARBCHAIN*(m, 5)` tops out at 18 … The obstruction measured here is
**height alignment**, not the bound: a schedule that keeps all `k` depth-1
successors at height + 1 at `k = 5` would give 25. D66's residue 6 is
therefore **closed at `k = 4` and re-opened at `k = 5`**"); LOG #475
("`k²` NOT reached at `k = 5` by anything built (18 vs 25 — height alignment
obstructs, not the bound; D66 residue 6 closed at `k = 4`, REOPENED at
`k = 5`)").

**Defect.** The note diagnoses the cause correctly and then files it as an
open residue instead of removing it. The cause is entirely inside
`ARBCHAIN*`'s own bootstrap: `S_i` supplies `A_i` **and** all `k − 2`
helpers `T_ij` by a serial delivery chain on register `S_i`, so
`p(S_i, Y_i, 0)` sits `k − 1` layers above the mint, and at `k = 5` two of
the five secondary arbitrations land at offset 2 from THE ARBITRATION. That
is a property of the ordering of a bootstrap, and the grammar's own idle
event levels it in one line. The reopening of D66's residue 6 is therefore
not warranted.

**Recomputation (mine)** — `ac5.py` / `verify5.py`. `ARBCHAIN**(k)`: the same
shape as `ARBCHAIN*(k, k)`, with every auxiliary register **height-levelled
by `('n', a)` idles** (the same event kind the committed blueprints already
use for their tails) before the proposals, so that all `k` depth-1
consumers sit at exactly height + 1:

```
  ARBCHAIN**(k=3): n= 47 actors= 9  hits[1,1]  h(e)= 8  D(1) 3 x 'r' outdeg [3,3,3]  |D_e(2)| =  9 = k^2
  ARBCHAIN**(k=4): n= 90 actors=16  hits[1,1]  h(e)=10  D(1) 4 x 'r' outdeg [4,4,4,4]  |D_e(2)| = 16 = k^2
  ARBCHAIN**(k=5): n=157 actors=25  hits[1,1]  h(e)=12  D(1) 5 x 'r' outdeg [5,5,5,5,5]  |D_e(2)| = 25 = k^2
  ARBCHAIN**(k=6): n=254 actors=36  hits[1,1]  h(e)=14  D(1) 6 x 'r' outdeg [6]*6      |D_e(2)| = 36 = k^2

  ARBCHAIN**(5), verified to the D66-round standard:
    my closure == the committed `event_poset` on all 157 events: True
    committed d47a `heights` == mine: True
    |D_e(2)| read from the COMMITTED `sky(C, e, 'B', 2)`: 25
    25 pairwise-distinct events, ALL ordered after the base in the committed
      order, ALL at height exactly 12 + 2 = 14, P-paths printed
      (five per secondary arbitration, one per proposer register)
    Bl = 5; W4c violations at d = 1, 2, 3: 0
    version registers occurring more than once: 0
    FULL-MENU REPLAY (D60's C1 grade, ALL 25 actors offered at every step):
      OK 157/157, max hits per specification = 1, widest full menu = 2,125
```

So the `k = 5` record that saturates `k²` carries a **complete** C1 grade —
a **higher** forcedness grade than the unit's own headline record, whose
replay is budget-cut at 71/120 (MAJOR 3).

**Scope of my counter-construction, stated so it is not over-read.**
`ARBCHAIN**` is a *smallest-witness* record of exactly the class the unit's
own `ARBCHAIN*` is — not a tiling crystal. Whether a **tiling** `k = 5`
schedule (a `DOUBLE-GRID(5, R)`) exists and reaches 25 remains untested by
me as well; that half of residue 1 stands. What does not stand is "`k²` is
UNREALIZED at `k = 5`", "the ceiling is not reached at `k = 5`", and the
reopening of D66's residue 6 — all three are statements about the ceiling,
and the ceiling is reached.

**What must change.** §3's ladder paragraph and §8 residue 1 must be
restated: `k²` is realized at `k = 3, 4, 5, 6`; the shortfall the unit
measured is `ARBCHAIN*`'s bootstrap ordering; D66's residue 6 stays **closed**,
not reopened; the surviving open question is the *tiling* one. And §7(iv)'s
attribution of the width to **phase separation**
must be weakened accordingly — `ARBCHAIN**` has no phase separation at all
and reaches the ceiling; the general lever is exactly the one the note's own
refined sentence names, *the `k` depth-1 consumers must sit at height + 1*,
and it is reachable by levelling, not only by a row/column phase split.

---

## MAJOR 2 — "sprinkling-grade width" is a one-column, one-`k` label: the comparison population is bimodal by dimension, the record is below the sprinkling population on every non-extremal width column, and the same mechanism overshoots the whole range at `k = 5`

**Where.** Note **title** ("**K-III. SPRINKLING-GRADE WIDTH FROM PURE
INTERACTION**"); §1 ("inside the genuine sprinkling range `[10, 17]` for the
first time in the campaign"); §7(iii); receipt K3a/K6a; LOG #475 ("**THE
FIRST SPRINKLING-GRADE WIDTH IN THE CAMPAIGN, from crossed conflict
alone.**").

**Defect, three parts.**

**(a) The range is a union of two dimensionally distinct clusters.** The
eleven genuine configurations are five `M21` (2+1) and six `M31` (3+1)
sprinklings, all at `N = 120`. Their `max |D|` at `d = 2`, read off the
receipt's own K0c block:

```
  M21 (2+1):  11, 11, 10, 11, 11      -> range [10, 11]
  M31 (3+1):  15, 14, 17, 15, 16, 14  -> range [14, 17]
```

`[10, 17]` is the hull of two disjoint clusters. **16 is not inside the
`M^{2+1}` cluster at all** — it sits in the 3+1 cluster. In a campaign whose
own instrument line (D55/D58) reads chart width as a dimension proxy, a
headline that says "inside the genuine sprinkling range" without saying
*which sprinklings* is exactly the unlabelled-population move D63 round-1
MAJOR 1 and D66 round-1 MAJOR 2 both struck out.

**(b) `max` is the only column on which the record touches the
population.** Every other width column the receipt itself prints puts the
headline record far below the sprinklings, at both depths, whole *and*
interior (my own recomputation, `an42.py`):

```
                                  d = 2                      d = 3
                          mean|D|   homog    |D|>=4      homog    |D|>=4
  DOUBLE-GRID(4,2) full     2.09    0.4083   0.2667      0.5417   0.3917
  DOUBLE-GRID(4,2) interior   —     0.4125   0.2000      0.7500   0.5875
  DOUBLE-GRID(4,4) full [mine] —    0.4850   0.4000      0.7250   0.6350
  sprinkling population   3.26-6.41
  sprinkling BAND                 [.6417,.8000] [.4250,.6500] [.6833,.8167] [.6000,.7583]
```

At `d = 2` — the depth at which the width verdict is read and at which
"sprinkling-grade" is claimed — the headline record is below the band on
**both** columns, whole and interior, and its mean chart is 2.09 directions
against the sprinklings' 3.26–6.41, with **three events of 120** carrying
the 16-wide chart. (At `d = 3` and `R = 4` the record does reach the
population on both columns — BLOCKER 1 — but that is not the depth the
width headline is about.) The claim that *is* supported is the one §7(iii)
almost makes: *the maximum chart width reaches a value inside the hull of
the sprinkling maxima.*

**(c) The number 16 is a choice, not a finding.** By MAJOR 1 the width
mechanism delivers `k²` whenever the `k` depth-1 consumers are levelled;
`k = 5` gives 25 and `k = 6` gives 36, both **above** the whole sprinkling
range, in records of exactly the class the unit's own smallest witness
belongs to. "The first sprinkling-grade width in the campaign" therefore
reads as a coincidence discovered when it is a parameter picked. The
mechanism sentence that survives is: **crossed conflict realizes W4c's `k²`
at every `k` anyone has built, and the sprinkling maxima happen to bracket
the `k = 4` value.**

**What must change.** The title, §1, §7(iii), K3a/K6a and LOG #475 must scope
"sprinkling-grade" to the measured statistic (`max |D|` at `d = 2`), name the
bimodality of the comparison population, and drop "for the first time in the
campaign" as a milestone claim about the mechanism.

---

## MAJOR 3 — the C1 grade is claimed for 1,040 events and delivered for 231; the pin's K1 asked for the headline record and the headline record was cut at 71/120

**Where.** §7 licensed claim (i) ("a four-proposer conflict crystal **exists
and forces** — 1,040 events, zero refusals, **C1-graded**"); §1 ("nine
configurations, 1,040 events, **zero refusals**, every event offered by the
committed layer's own menu"); pin §3 K1 ("forcedness at C1 grade (**full-menu
replay on the headline record**)").

**Defect.** Two different grades are welded into one sentence. The 1,040
events carry the **restricted-menu** grade (each event offered to its own
initiator). D60's C1 grade — all actors offered at every step — was run on
**four** records totalling 231 steps, of which:

```
  ARBCHAIN*(m=0,k=4)     22/ 22  complete   (k = 4, 4 directions)
  ARBCHAIN*(m=4,k=4)     66/ 66  complete   (k = 4, THE 16-direction witness)
  DOUBLE-GRID(3,2)       72/ 72  complete   (k = 3, the ANCHOR)
  DOUBLE-GRID(4,2)       71/120  BUDGET-CUT (k = 4, THE HEADLINE)
```

Of the **nine swept configurations**, exactly **one** — `DOUBLE-GRID(3,2)`,
a `k = 3` anchor — is C1-complete. `DOUBLE-GRID(4,1)`, `(4,3)`,
`DGRID-INTERLEAVED(3,2)`, `(4,2)`, `CONFLICT-GRID(4,4)` and `(4,6)` were
**never full-menu replayed at all** — including `DOUBLE-GRID(4,3)`, the
*second* record carrying `max |D| = 16`, and both interleaved records on
which the V4 mechanism finding is read. The pin named the headline record
specifically and it is the one that was cut.

The note discloses the cut (§6, residue 5) and says where the prefix bites,
which is why this is MAJOR and not BLOCKER. What it does not do is stop
§7(i) from reading as though 1,040 events are C1-graded. Compounding it:
**every one of the three grammar cells that carry a non-zero parity
obstruction in K5** (`DOUBLE-GRID(4,2)`, `(4,1)`, `(3,4)`) is a record whose
C1 grade is a prefix or absent — D66 round-1 MINOR 1, repeated verbatim in
the same corpus.

**Recomputation (mine).** My `ARBCHAIN**(5)` is 157/157 C1-complete at
widest menu 2,125 in 530 s (MAJOR 1), and `DOUBLE-GRID(3,2)` replays 72/72
in my driver too. The budget is not the wall the receipt's 150 s suggests;
the wall is that 150 s was the number chosen.

**What must change.** §7(i) must separate the two grades and give the
C1-graded event count; and the K1d budget should be stated as what it is — a
receipt-runtime choice, not a property of the object.

---

## MAJOR 4 — "in band" is read on one of the two band columns the receipt itself computes, and on the other one the interior of `DOUBLE-GRID(4, 2)` is BELOW the band at both depths

**Where.** §1 ("the interior of `DOUBLE-GRID(4, 2)` is — in band at `d = 3`
while sixteen directions wide"); §4(ii); §7(v); K4's gate; LOG #475.

**Defect.** K0c computes and prints **two** sprinkling bands at each depth:
homogeneity (`|D| ≥ 2`) and `|D| ≥ 4`. Every in-band / below verdict in the
unit is read on the homogeneity column alone. On the `|D| ≥ 4` column the
headline record's interior is **outside** the band at both depths.

**Recomputation (mine)**, `an42.py`, D60's own `interior_of` (`lo + 2 ≤ h ≤
hi − 3`; `lo = 0`, `hi = 15`, interior = 80 of 120 events, heights 2..12):

```
  DOUBLE-GRID(4,2) interior, d = 3:  homogeneity 60/80 = 3/4   IN  [0.6833, 0.8167]
                                     |D|>=4      47/80 = 0.5875 BELOW [0.6000, 0.7583]
  DOUBLE-GRID(4,2) interior, d = 2:  homogeneity 33/80 = 0.4125 BELOW [0.6417, 0.8000]
                                     |D|>=4      16/80 = 0.2000 BELOW [0.4250, 0.6500]
  interior width histograms:  d = 2 {0:16, 1:31, 2:7, 3:10, 4:13, 16:3}
                              d = 3 {0:9, 1:11, 2:8, 3:5, 4:33, 5:1, 6:3, 7:2, 16:8}
```

So the one cell in the whole unit that is "in band" is in band on one column
of two, and below on the other. (The same is true of D66's committed `k = 3`
flagship: `DOUBLE-GRID(3,4)` is at `|D| ≥ 4` `13/40 = 0.325` at `d = 3`,
far below `[0.6, 0.7583]` — so this is a corpus-level habit that D67
inherits rather than invents. It should be said once, here, and then carried.)

The contrast is sharpened by BLOCKER 1: `DOUBLE-GRID(4,4)` as a **whole**
record is in band on **both** `d = 3` columns (`0.7250` and `0.6350`). So
the cell the unit chose to ship is the weaker of the two available, on the
weaker of the two available columns.

**What must change.** Every "in band" sentence must name the column, and
§4(ii) must report the `|D| ≥ 4` reading beside the homogeneity reading —
the receipt already computes it.

---

## MAJOR 5 — the interior verdict is a monotone crossing, not a match: the family sweeps THROUGH the band and out the top, and the note reports the trend without drawing the consequence

**Where.** §4(ii) ("`DOUBLE-GRID(4, 3)` overshoots to `0.8333` (above), as
D66's `k = 3` records do at `0.9333` and `0.9677`"); §4's FRONTIER box
("the failure at `k = 4` is an **ends effect at the same grade of evidence at
which D66 closed its residue 2**"); LOG #475 ("in-band and 16-wide **at the
same evidence grade as D66's flagship**").

**Defect.** The unit's own table shows the interior `d = 3` homogeneity of
the `k = 4` family running `0.6154 → 0.7500 → 0.8333` at `R = 1, 2, 3`
against a band `[0.6833, 0.8167]`: the family **enters** the band at `R = 2`
and **leaves** it at `R = 3`. The `k = 3` family is already above it at both
swept `R` (`0.9333`, `0.9677`). **Band membership in this family is where a
monotone one-parameter sweep happens to be, not a property of the object.**
A one-parameter family monotone in a statistic crosses any interval at some
parameter; reporting the crossing as "IN BAND" and its two neighbours as
"below" and "ABOVE" — which is literally the shape of the unit's own K2c
table — turns a tuning coincidence into a verdict. The same objection
applies to the whole-record `k = 3` flagship D66 shipped (`0.6389` at
`R = 2`, `0.7833` at `R = 4`) and now, by BLOCKER 1, to `k = 4`.

Second half of the same defect: LOG #475's "**at the same evidence grade as
D66's flagship**" is not what §4 says. D66's flagship was in band **as a
whole record**; D67's is an interior average. The note's own §4 is careful
("at the same grade of evidence at which D66 closed its *residue 2*"); the
LOG entry upgrades it one notch and the two sentences of LOG #475 then
contradict each other ("no whole `k = 4` record is in band … BUT … at the
same evidence grade as D66's flagship").

**Recomputation (mine).** My own excision on the records I rebuilt —
`DOUBLE-GRID(4,1)` interior `d = 2` `21/52 = 0.4038`, `d = 3`
`8/13 = 0.6154`; `(4,2)` interior `33/80` and `3/4`; and, new, `(4,4)`
interior `81/160` and **`7/8 = 0.8750`** — all reproducing the receipt where
it has a row. Laid out, both sequences are monotone and each crosses the
`d = 3` band `[0.6833, 0.8167]` at a different `R`:

```
  R =                     1        2        3        4
  WHOLE record  d = 3   0.4625   0.5417   0.6562   0.7250  <- enters at R = 4
  INTERIOR      d = 3   0.6154   0.7500   0.8333   0.8750  <- enters at R = 2,
                                                              leaves at R = 3
```

So "in band" names the round number, not the object: at `R = 2` the
interior is in band and the whole record is not; at `R = 4` the whole record
is in band and the interior is above. The unit read one cell of this table
and called it a frontier.

**What must change.** §4 must state the sweep, not the point: the interior
`d = 3` homogeneity is monotone in `R` and the band is an interval it
crosses. LOG #475's "same evidence grade as D66's flagship" must be
corrected to the note's own weaker sentence — or, after BLOCKER 1, replaced
by the whole-record result.

---

## MINOR 1 — "the budget bound SATURATED at `1/5`" is neither the conflict share nor this record's applicable bound, and the receipt's VERDICT block miscounts the arbitrations

**Where.** §1 ("an arbitration share of **exactly `1/5` = `1/(k+1)`, the
budget bound SATURATED**"); §7(i); receipt K1c's headline ("**THE CONFLICT
SHARE AT k = 4 IS EXACTLY 1/5, THE BUDGET BOUND, SATURATED**"); the receipt's
VERDICT block ("**24 arbitrations of FOUR proposers each**"); LOG #475
("saturates the conflict budget at exactly `1/5 = 1/(k+1)`").

**Recomputation (mine)**, `DOUBLE-GRID(4,2)`, my own census:

```
  arbitrations by proposer count: {1: 8, 4: 16}
     — 8 of the 24 are the ONE-PROPOSER bootstrap mints ('r', sd, {t}, {t})
  proposals 72, deliveries 24, idles 0, events 120
  total arbitration share        24/120 = 1/5
  CONFLICT-arbitration share     16/120 = 2/15   (NOT 1/5)
  sum of proposer counts         72 = #proposals  (the gated equality: TRUE)
  k_min over the record          1  ->  the record's OWN applicable budget
                                        bound is 1/(k_min + 1) = 1/2
```

**Defect.** (a) The receipt's VERDICT block states a falsehood: 8 of the 24
arbitrations have one proposer, not four. (b) "the conflict share" is
`2/15`, not `1/5`. (c) `1/5` does not saturate the bound that applies to
*this* record — with `k_min = 1` the bound is `1/2` — it equals the bound
that would apply to a record all of whose arbitrations had four proposers,
which this one is not. D66's round-1 delta already split these two readings
("`k_min = 1` general `1/2`; conflict groups `1/4`") and D67 re-merges them.
What is genuinely gated and genuinely nice is the **equality**
`#proposals = Σ_arb k_arb = 72` with no consumed triple repeated — and the
*mechanism* behind the `1/(g+1)` coincidence, which the unit could state and
does not: the bootstrap is `2g` mint-proposals + `2g` mint-arbitrations +
`2g(g−1)` deliveries = `2g(g+1)` events with `2g` arbitrations, and each
round is `2g²` proposals + `2g` arbitrations = `2g(g+1)` events with `2g`
arbitrations, so **both phases sit at `1/(g+1)` for unrelated reasons** and
the total is `1/(g+1)` at every `R`. That is the real finding in this row.

---

## MINOR 2 — "three charts of width 16" is ONE direction set seen from three bases

**Where.** §3 ("`DOUBLE-GRID(4, 2)` carries **three charts of width 16**, at
base events 73, 74 and 75"); K3a's witness block; LOG #475 ("Witness: three
16-wide charts").

**Recomputation (mine).**

```
  bases with |D_e(2)| = 16: [73, 74, 75]
  distinct DIRECTION SETS among them: 1   ({80,...,95} for all three)
  their D(1) sets: [76, 77, 78, 79] for ALL THREE — and for base 72 as well
```

All four round-0 row arbitrations share the same four successors (the four
column arbitrations), so the record contains **exactly one** 16-element
`d = 2` chart, and three of its 120 events see it. "Three charts of width 16"
is literally true and materially misleading; the sentence should say that
the three bases carry the *same* chart. (At `d = 3` there are eight such
bases, heights 9 and 10 — again a small number of bases over a shared
structure.)

---

## MINOR 3 — "the transition class of every `k = 4` wide record is trivial … at all 74 census cells": `DOUBLE-GRID(4,3)`, the other 16-wide record, is not in the census

**Where.** §7 licensed claim (vi); §5.

`K5SET = [HEAD, ('DG',4,1), ('DG',3,4), ('CG',4,4), ('INTER',4,2)]` — five of
the nine swept records, plus `ARBCHAIN*(4,4)`, `DR(8,10,8)` and two
sprinklings = the nine substrates and 74 cells. `DOUBLE-GRID(4,3)`, which
carries `max |D| = 16` at both depths with **seven** wide charts, is not
among them, and neither are `DOUBLE-GRID(3,2)`, `DGRID-INTERLEAVED(3,2)` or
`CONFLICT-GRID(4,6)`. "Every `k = 4` wide record" should be "both censused
`k = 4` records" or the census should be extended.

## MINOR 4 — "the one-lineage alternative refuses at its 18th event" is contradicted by the unit's own V3, and V2 is a 19-event stub rather than a schedule

**Where.** §7(ii); §2's variant table row "V2 `SHARED-BASE(4)` one lineage —
**NO — REFUSES**".

`shared_base(g)` mints one version, spreads it to fifteen actors, then makes
**one actor propose twice on that base back to back** and stops. That is a
correct and useful *demonstration* of `prop_options_in_view` — I reproduce
the empty option list, at prefix 18, in my own driver — but it is not an
alternative schedule that was driven and failed; it stops nineteen events in,
by construction, and it never attempts an arbitration. Meanwhile
V3 `CONFLICT-GRID(4, R)` **is** a one-lineage-per-actor design and it does
**not** refuse: it forces, tiles, and reaches width 8. §2's mechanism box has
the scope right ("a grid whose rows and columns conflict **concurrently**");
§7(ii) drops "concurrently" and thereby contradicts the unit's own V3 row.

## MINOR 5 — the inference "two live bases per actor, *i.e.* `2g` independent lineages" skips the step that makes it true

**Where.** §2's THE REFUSAL IS THE MECHANISM box; §7(ii).

"An actor may hold at most one live proposal per base" gives *two bases per
actor*, not *`2g` lineages*. The missing step — which is true, and which I
checked against the layer — is that **two concurrent groups cannot share a
base**: `admissible` requires `triples(view, comp) == ckey` for a *whole*
component, `View.components()` groups live proposals by base, and on one
base the payload-0/payload-1 conflict graph of two groups is connected, so
one base admits exactly one arbitration per generation. Hence `g` row bases
+ `g` column bases, all distinct because every `(r, c)` cell sits in one of
each. Print the step, or drop the "i.e." and claim only what the refusal
shows.

## MINOR 6 — the interior is a population, not an object, and the K4 gate calls it one

**Where.** K4's gate text ("so **the campaign's first sprinkling-grade-wide-
AND-in-band OBJECT exists** at the SAME grade of evidence…"); §4(ii).

`interior_of` returns the **full** closure and a subset of events; `profile`
then averages over that subset while every chart is still computed on the
whole record — a base at height `hi − 3` still reads directions at `hi − 1`,
inside the excised layers. The interior is a conditional average over 80 of
120 events, not a record, not a sub-poset, and not an object. (The excision
is D60's and D66 used it the same way, so the instrument is not at issue —
the word "object" is.) Related: because the excision is a population
restriction, the sentence "no wide chart in this unit is a boundary
artefact" tests only that the *base* is off the boundary; the chart's
contents are not excised. I confirm the base test passes — bases 73/74/75
(height 10) and all eight `d = 3` wide bases (heights 9 and 10) are inside
`[2, 12]` — but the claim should be worded as what it measures.

## MINOR 7 — two of the 26 PASSes carry their own disqualifier in the parenthesis rather than in the label

K5e(ii) is labelled "**TRIVIAL BY C7 AND BY FREE RELABELLING AT EVERY CELL
OF THE CENSUS**" and its detail string reads "headline `k = 4` record
trivial at every convention and route = **False**". The predicate really
gated is the route-agreement, and that is defensible — but a PASS whose own
parenthesis says `False` about the object in its title is the kind of line a
reader will quote without the parenthesis. K6d PASSes "DETERMINISM IS GATED"
with a scope that excludes **the headline record and the entire K5 census**
— i.e. the determinism gate does not cover either of the two things the unit
is claiming. Both are disclosed; both belong in the label.

---

## NIT 1 — "the second concurrent consumer must sit at height + 1" cannot fail

§2's refinement box and §7(iv). `SKY-B(2)` counts events at **exactly**
height + 2, so a successor `y` at offset 1 contributes its `b(y)` successors
while a successor at offset 2 contributes only *itself* (its own successors
land at offset ≥ 3 and are not counted) — and `b(e) ≤ Bl = k`, so the
offset-2 route can never yield more than `k`. "The consumers must sit at
height + 1 to realize `Σ_y b(y)`" is therefore the instrument's definition
plus one inequality, not a mechanism that could have come out otherwise. I
tried to build a counterexample and there is none to build: the statement is
true because `SKY-B` says so. What *is* empirical, and worth the box, is the V4
control (`16 → 7`, `9 → 5`): that the *order of arbitrations inside a round*
changes which successors are at offset 1. I reproduce both interleaved
controls exactly: `DGRID-INTERLEAVED(3,2)` `max |D|` `5` / `6`, homogeneity
`0.2361` / `0.2917`, histogram `{0:31, 1:24, 2:6, 3:6, 4:3, 5:2}`; and
`DGRID-INTERLEAVED(4,2)` `max |D|` `7` at both depths, homogeneity `0.2583` /
`0.3250`, histogram `{0:58, 1:31, 2:10, 3:11, 4:6, 5:1, 6:1, 7:2}` — the
`16 → 7` collapse is real, and it is the empirical half of the box.

## NIT 2 — residue 2's "unbuilt" bootstrap costs one levelling pass

§8 residue 2 asks whether a bootstrap exists that levels the first round's
four row arbitrations. `level.py` (mine) inserts idle events after the
bootstrap to bring every actor register to a common height, then runs the
ordinary phase-separated rounds:

```
  LEVELLED-DGRID(4,2): n = 140 (20 idle pads), hits [1,1], no refusal
     d = 2  homogeneity 61/140 = 0.4357 (was 0.4083), max |D| = 16,
            histogram {0:12, 1:67, 2:7, 3:10, 4:40, 16:4}
            -> FOUR charts of width 16 per round instead of three:
               the row-0 arbitration now realizes its whole budget
     d = 3  homogeneity 17/28 = 0.6071 (was 0.5417), max |D| = 16,
            {0:25, 1:30, 2:10, 3:6, 4:43, 5:1, 6:3, 7:2, 16:20}
     interior (100 of 140):  d = 2 0.4500,  d = 3 0.8000  [IN BAND]
```

So residue 2's conjecture is right on both halves — the levelling recovers
the fourth chart *and* raises homogeneity at both depths — and it costs one
pass of the grammar's own idle event. It does not by itself put the whole
record in band (that is BLOCKER 1's `R = 4`), and it dilutes the `1/(g+1)`
arbitration share to `6/35`, which is the trade the note should record.

## NIT 3 — the sprinkling comparison's population, not its size, is what needed the label

To the unit's credit the comparison **is** size-matched: all eleven genuine
configurations are `N = 120` and the headline record is 120 events, so the
extreme-order-statistic objection I expected does not apply. The label that
is missing is the dimensional one (MAJOR 2a), not a size one. Said here so
the repair does not add the wrong caveat.

## NIT 4 — the exit-freedom scan carries D63/D64/D66's declared narrowness

`_no_exit` is the widened Name/Attribute form with its scope stated in the
gate; a `getattr`-reached exit would still survive. Disclosed, so a note
only.

---

## Checked and CLEAN (D67)

Everything below is my own recomputation unless stated.

**A. Receipt rerun.** 26 PASS / 0 FAIL, exit 0, 1,370.3 s. The output diff
against the committed `.out` is **empty** after normalising the timing
figures — all 554 lines, every census, every histogram, every
witness block and every obstruction count reproduces byte for byte. The
exit line matches the code (`sys.exit(1 if ANCHOR_FAIL else 0)`) and
`anchor broken = False`.

**B. The instrument, rebuilt from the committed definitions.** My own `P`
(immediate predecessor per register, mirroring `event_poset`'s `last`
bookkeeping over the committed `regs_of`), my own memoised closure, my own
longest-chain heights, my own SKY-B, my own profile and histograms, my own
interior excision. On `DOUBLE-GRID(4,2)`: **my closure equals the committed
`event_poset` on all 120 events**, the committed `d47a.heights` equals mine,
and **my SKY-B agrees with the committed `d47a.sky(C, e, 'B', d)` at every
event at both depths, zero disagreements**. The same three checks pass on my
`ARBCHAIN**(5)`.

**C. The sweep, rebuilt.** Seven configurations re-driven from the note's
blueprint prose with my own driver (plus the two new ones of BLOCKER 1 and
NIT 2), **every published row reproducing to the last Fraction at both
depths**:

```
  DGRID(3,2)  n= 72 arb 1/4 dels 12 | d2 4/9   ge4 5/72   max 9  {0:10,1:30,2:5,3:22,4:2,9:3}
                                    | d3 23/36              max 9
  DGRID(3,4)  n=120 arb 1/4 dels 12 | d2 31/60 ge4 11/120 max 9  {0:10,1:48,2:5,3:46,4:2,9:9}
                                    | d3 47/60              max 9
  DGRID(4,1)  n= 80 arb 1/5 dels 24 | d2 13/40 ge4 9/80    max 4  {0:27,1:27,2:7,3:10,4:9}
                                    | d3 37/80              max 7
  DGRID(4,2)  n=120 arb 1/5 dels 24 | d2 49/120 ge4 4/15   max 16 {0:28,1:43,2:7,3:10,4:29,16:3}
                                    | d3 13/24  ge4 47/120 max 16 {...,16:8}
  DGRID(4,3)  n=160 arb 1/5 dels 24 | d2 73/160 ge4 7/20   max 16 {0:28,1:59,2:7,3:10,4:49,16:7}
                                    | d3 21/32              max 16
  DGRID-INTERLEAVED(3,2) n=72       | d2 0.2361 max 5 {0:31,1:24,2:6,3:6,4:3,5:2} | d3 0.2917 max 6
  DGRID-INTERLEAVED(4,2) n=120      | d2 0.2583 max 7 {0:58,1:31,2:10,3:11,4:6,5:1,6:1,7:2} | d3 0.3250 max 7
  [NEW] DGRID(4,4)  n=200 arb 1/5 dels 24 | d2 97/200 max 16 {0:28,1:75,2:7,3:10,4:69,16:11}
                                          | d3 29/40  max 16 {0:34,1:21,2:12,3:6,4:73,5:1,6:3,7:2,16:48}
  [NEW] LEVELLED-DGRID(4,2) n=140         | d2 61/140 max 16 {0:12,1:67,2:7,3:10,4:40,16:4}
```

Zero refusals; menu hits `min = max = 1` at every step of every record (I
gated the minimum too, which the receipt does not). The `(3,2)` and `(3,4)`
rows are D66's committed rows, including `(3,4)`'s committed histogram — so
**K0d's anchor holds in an independent driver**, not only against D66's own
function object.

**D. The width witness, verified event by event.** `DOUBLE-GRID(4,2)`,
bases 73/74/75: `r`-events by `D11`/`D22`/`D33`, height 10, 5 registers,
**4 distinct proposers**, live out-degree 4; `D(1) = [76,77,78,79]`, all four
`r`-events with out-degrees `[4,4,4,4]`, `Σ_y b(y) = 16 = k²`;
`D(2) = {80,…,95}`, **sixteen pairwise-distinct `p`-events by the sixteen
distinct actors `D00…D33`, every one at height exactly 12 = 10 + 2, every
one ordered after the base in the committed order**, read from the committed
`sky`. Not an instrument artefact and not a chart-counting convention.

**E. The bounds.** W4b's `B^d` and W4c's `Bl^d` hold with zero violations at
`d = 1, 2, 3` on every record I built (including my `ARBCHAIN**` family at
`Bl = 3, 4, 5, 6`); every version register occurs in exactly one event's
`regs_of` on every record; the exact containment `D_e(2) ⊆ succ(e) ∪ ⋃ succ(y)`
holds everywhere. `Bl` measures 3 and 4 exactly as published.

**F. The unfilled-successor census.** Reproduced exactly, including the
characterisation:

```
  base 72 h= 9 b=4 succ [76,77,78,79] offsets [2] SUM b(y) 16 |D(2)| =  4  <- the one shortfall
  base 73 h=10 b=4 succ [76,77,78,79] offsets [1] SUM b(y) 16 |D(2)| = 16
  base 74 h=10 b=4 succ [76,77,78,79] offsets [1] SUM b(y) 16 |D(2)| = 16
  base 75 h=10 b=4 succ [76,77,78,79] offsets [1] SUM b(y) 16 |D(2)| = 16
  bases 76-79 h=11 offsets [1] SUM 4  |D(2)| = 4 ;  112-115 SUM 0 ; 116-119 b = 0
```

The loser is the row-0 arbitration of the first round, one height layer
below its three siblings (9 against 10) because the bootstrap depresses it —
exactly as §3 says; and the chart counts `g(R−1)` at `g = 3` (3 at `R = 2`,
9 at `R = 4`) and `g(R−1) − 1` at `g = 4` (3 at `R = 2`, 7 at `R = 3`) are
right — and the formula **extrapolates correctly to the row the unit did not
build**: my `DOUBLE-GRID(4,4)` carries `4·3 − 1 = 11` charts of width 16,
which its histogram shows as `16:11`. The one-chart-per-record cost, not
one per round, is confirmed.

**G. The `ARBCHAIN` correction to D66 (claim vii, first half).** Verified at
source: D66's `arbchain(m, k)` builds
`gi = [[(S[i],Y[i],0), (A[i],Y[i],1), (T[i],Y[i],1)] …]` — literally three
proposers whatever `k` is — while its module docstring claims
`k·m + 2(k−m)` "sweeps the WHOLE interval `[2k, k²]`". D66's receipt calls it
only at `arbchain(m, 3)` (one call site, line 1590) and its `.out` prints
only `k = 3` rows, so **nothing gated in D66 is invalidated**, exactly as
the note says. D67's `ARBCHAIN*` reproduces `6, 7, 8, 9` at `k = 3`. My own
independent `ARBCHAIN**(3)` also gives `9` at `m = k = 3`. The correction is
right and correctly scoped, and it is reported against the unit's own
parent — which is the discipline this corpus is supposed to have.

**H. The anchors.** K0b (D63's `DR(8,10,8)` row and D60's brick event for
event), K0c (the eleven genuine sprinkling configurations, bands
`[77/120, 4/5]` and `[17/40, 13/20]` at `d = 2` and `[41/60, 49/60]`,
`[3/5, 91/120]` at `d = 3`, and the max `|D|` ranges `[10,17]` / `[11,17]`),
K0d (D66's committed DOUBLE-GRID rows — reproduced in my own driver as
well), K0e (hoisted SKY-B vs committed `sky` — I reproduce the agreement
independently), K5a (closure of `P` = the committed order) and K5e(i)
(D64's committed C7 row) all hold in the rerun and, where I could rebuild
them, in my own code.

**I. Forcedness (restricted menu).** 1,040 events, nine records, zero
refusals, hits exactly 1 — reproduced. The V2 refusal reproduces **in my own
driver, to the index**: refusal at prefix 18, `prop_options_in_view(view,
S01) = []`, menu kinds `['n', 'r']`, 1 live triple — the layer's own option
list, not a missing menu hit. The pin's K-I correctly does not fire.

**J. The gauge census.** I did not rebuild D64's cocycle instrument (D66's
round-1 did, cell for cell, and found it correct); I read the 74-cell table
and checked its internal consistency and its scoping. C7 and FREE are zero
at every cell; PARITY is non-zero at exactly ten, six of them grammar cells
at ARBLOSE on `DOUBLE-GRID(3,4)`, `(4,1)`, `(4,2)` and four of them
sprinkling cells at COV. The note's §5 discloses the sprinkling cells, the
ARBLOSE domain shrink (133 → 29 edges) and the two grounds carried from
D64/D66 without re-measurement; it names no magnitude and does not claim
`H¹ ≠ 0`. **The reading that this is a schedule-plus-convention property and
not a `k = 4` phenomenon is warranted by the `k = 3` cell**, which is the
one that could have killed it. PROBE 1's blind cells are printed and
excluded by name; nothing is read at RAW; the two added routes carry a true
positive and a true negative. Subject to MINOR 3's population, this section
is the cleanest in the unit.

**K. Determinism, caps, exit protocol.** The hash-seed probe is real and its
scope is stated aloud (it does **not** cover the `g = 4` builds or the K5
census — see MINOR 7). Swept ranges, both depths, the cost curve, the
replay budgets and the one binding cut are all printed; the threshold
inventory is honest ("the K3 verdict is read against the RE-RUN sprinkling
floor 10, not against the pin's prose"). Six gates carry `anchor=True` and
the exit line is `sys.exit(1 if ANCHOR_FAIL else 0)`, which is exactly pin
K0/K6. AST anti-vacuity is d47a's SG8 form with its scope stated.

**L. Provenance and pin discipline.** The pin (77 lines, STRICT) is
committed at 15a90a0, before the receipt and the result note; its
K-I/K-II/K-III disjunction is the receipt's actual `OUTCOME` predicate; the
pin declined a lean on the width verdict and took an honest one on the band
question, and the note reports the band lean as half wrong **against the
unit's own interest**. Six residues are filed, including the two (the
budget-cut replay, the `k = 5` gap) that this round turned into findings.
That discipline is exactly why BLOCKER 1 and MAJOR 1 were worth building
rather than assuming — the note told me where to dig.

**M. Scope.** Pin §5's clauses are all carried in note §6/§7 — grammar
layer, the swept family, #440's mechanism-not-objects, no measure claim at
transport scope, no typicality, `ω` per D58's reading, D59's missing map
untouched. Subject to BLOCKER 1 and MAJOR 1–2, which are sentences stated
more widely than the sweep supports, no claim exceeds the family.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-27)

**Verification of the BLOCKER and MAJOR 1.**  The referee's three
constructions are GATED IN THE RECEIPT (rerun 29 PASS / 0 FAIL,
3,291 s), verified by me directly against the fresh output:
DOUBLE-GRID(4,4) — 200 events, forced, zero in-round deliveries,
max |D| = 16 at both depths, d = 3 homogeneity 29/40 = 0.7250 [IN]
and |D|>=4 = 0.6350 [IN] on BOTH published band columns AS A WHOLE
RECORD; ARBCHAIN**(k) — height-levelled by the grammar's own idle
events — realizes the ceiling at k = 5 (|D| = 25, 157 events,
FULL-MENU REPLAYED 157/157 at widest menu 2,125 — a higher C1 grade
than any double grid here) and k = 6 (|D| = 36); LEVELLED-DGRID
closes the unit's residue 2.  **The width-uniformity frontier at
k = 4 does not exist, and the k-ceiling question is closed at every
k tried (3, 4, 5, 6).**

**Repairs applied (note retitled to the corrected positive):** the
false negative struck and carried in the corrections section; the
"sprinkling-grade" label scoped (one column, one k, per-dimension
figures); THE C1 ACCOUNTING AS A NUMBER (380 C1-graded steps of
1,380 swept; four complete records named; "1,040 events C1-graded
was never true and is not said here" — printed in the receipt);
both band columns wherever "in band" appears; the interior verdict
restated as a monotone crossing on a population; the budget-bound
and four-proposer mislabels fixed; the V2/V3 scoping; the
height + 1 sentence marked DEFINITIONAL (SKY-B's definition plus
one inequality) with the empirical content (the V4 collapse and
that a schedule CAN satisfy it at every k) separated; the parent
corrections carried; exit-scan widened.

**Verdict after repairs: the unit stands as the corrected positive —
crossed conflict reaches band uniformity AND the k² ceiling in one
whole record, and the ceiling is realized at every k tried, with
height-levelling (supplied by the grammar's own idles) as the
mechanism.**  TERMINAL for round 1.
