# D67 — result: **K-III. CROSSED CONFLICT REACHES BAND UNIFORMITY *AND* THE `k²` CEILING IN ONE WHOLE RECORD.** `DOUBLE-GRID(4, 4)` forces, tiles delivery-free, carries **`max |D| = 16 = k²`** and sits inside **both** `d = 3` sprinkling band columns **as a whole record** — so the width-uniformity frontier at `k = 4` does not exist. The `k²` ceiling is realized at **`k = 3, 4, 5` and `6`**, and the mechanism is **height-levelling**, which the grammar's own idle event supplies.

**Status: ROUND-1 REVIEWED AND REPAIRED, 2026-07-27.**  An independent
hostile review — `v10/reviews/d67-round1-hostile-review.md`, a worker
with no prior context and no loyalty to the unit, every number
recomputed with its own driver and its own instrument — returned
**REVISE: 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT**, reproduced **every
published figure of the first version exactly** (all 554 lines of the
receipt, byte for byte after normalising timings), confirmed the
`|D| = 16` witness event by event against the committed `sky` and the
committed order, and then **inverted the unit's flagship with three
constructions of its own**.  All seventeen findings are carried below;
§9 is the corrections section and names what is **WITHDRAWN**, verbatim.
**The first version's headline negative was false, and its refutation is
the better result.**  Pin `note-d67-k4-double-grid-pin.md` (STRICT,
FROZEN AND COMMITTED before this file or its receipt existed).  Receipt
`v10/code/d67_k4_double_grid_exact.py`, output
`v10/data/d67_k4_double_grid_exact.out` — **30 PASS / 0 FAIL, exit 0,
2937.9 s wall clock** (run from the repo root; 26 PASS before the
repair, and four of the thirty gates are new).  Parents: D66 (TERMINAL —
the width ceiling is `k·b ≤ k²`, saturated at 9 by `DOUBLE-GRID(3, R)`;
crossed conflict is the mechanism), W4c (the dead-wire theorem: width is
bought by PROPOSER count, not register count), D64/D65 (the coboundary
instrument and the descent defect), D63/D60/D58/D47a/D55c (the wide
crystal, the tiling blueprints, the atlas, the sky, the sprinkling
controls), D42b1 (the transport grammar).

**THE THREE ROUND-SUPPLIED CONSTRUCTIONS**, credited to the round,
rebuilt here with this unit's own driver and **gated like any other
object** — every one of them reproduces the review's figures exactly:

| object | round-1 finding | what it does |
|---|---|---|
| **`DOUBLE-GRID(4, 4)`** | BLOCKER 1 | one more round than the first version's sweep afforded — and the whole record is **in band on both `d = 3` columns while 16 wide** |
| **`ARBCHAIN**(k)`** | MAJOR 1 | `ARBCHAIN*(k, k)` height-levelled by the grammar's own `('n', a)` idles — realizes `k²` at `k = 3, 4, 5, 6` |
| **`LEVELLED-DGRID(4, 2)`** | NIT 2 | the same levelling pass on the DOUBLE-GRID bootstrap — recovers the lost fourth chart and raises homogeneity at both depths |

---

## 1. Which outcome fired

The pin pre-registered three outcomes and let the sweep decide.

> **K-III FIRED.**  The four-proposer schedule **forces** — eleven
> configurations, 1,520 events, **zero refusals**, every event offered
> by the committed layer's own menu and specified by its FULL EVENT
> TUPLE, max menu hits per specification = 1 everywhere.  It tiles with
> **ZERO in-round deliveries** at a **total** arbitration share of
> exactly `1/5 = 1/(k_conflict + 1)` at every `R`.  And it carries
> **`max |D| = 16` at `d = 2` and at `d = 3`** — `k² = 16`, **W4c's own
> ceiling, realized at `k = 4`** — which is at or above the re-run
> genuine sprinkling floor of **10** and inside the measured **hull**
> `[10, 17]` of the sprinkling maxima.  The pin's **K-I does not fire**
> (the schedule forces) and **K-II does not fire** (the width is not
> short of the floor).

**And the pin's honest lean on K4 — *band membership should get HARDER
as `k` grows* — is REFUTED, in the direction of this unit's own
interest.**  `DOUBLE-GRID(4, 4)`, a **whole** record, is inside the
`d = 3` homogeneity band at `29/40 = 0.7250` **and** inside the `d = 3`
`|D| ≥ 4` band at `0.6350`, while carrying `max |D| = 16 = k²`.  D66's
`k = 3` flagship is in band on **one** of those two columns.  §4 states
the whole sweep, because the honest form of the result is a **crossing**
and not a match.

## 2. The design problem the pin named, and the four schedules

A `k = 4` arbitration needs **four live proposals on one shared base**.
On a 4 × 4 actor grid, row `r`'s four actors must all hold the row base,
column `c`'s four must all hold the column base, and the minted version
goes to **all four proposers** (`View.holdings`), so a group that
arbitrates together needs no re-supply.  What costs deliveries is
rotation — and the pin asked whether the row/column rotation at `k = 4`
forces a two-base holding pattern or a delivery bill.  It forces the
two-base pattern, and the grammar itself is what forces it.

| variant | forces? | in-round deliveries | total arb share | `max |D|` d2 / d3 |
|---|---|---|---|---|
| **V1 `DOUBLE-GRID(4, R)`** mints-first, phase-separated | **yes** | **0** (24 in the bootstrap, once) | **1/5** | **16 / 16** |
| V2 `SHARED-BASE(4)` one *shared base* | **the 19-event stub refuses** | — | — | — |
| V3 `CONFLICT-GRID(4, R)` rotation, delivery-supplied, **one lineage per actor** | **yes** | **12 per round after the first, forever** (36 at R=4, 60 at R=6) | 4/29, 2/15 | 8 / 8 |
| V4 `DOUBLE-GRID(4, R, order='inter')` interleaved arbitrations | yes | 0 | 1/5 | **7 / 7** |
| **V5 `LEVELLED-DGRID(4, 2)`** [round-supplied] | yes | 0 (24 + 20 idle pads in the bootstrap) | 6/35 | **16 / 16** |

> **THE REFUSAL IS THE MECHANISM, AT THE SCOPE IT ACTUALLY HAS (V2;
> round-1 MINOR 4).**  Mint ONE version, spread it to all sixteen
> actors, and let rows and columns conflict on **that one base**: the
> record **breaks at its 18th event**, at the second proposal of the
> first actor.  The gate is not "the menu had no hit" but the layer's
> own option list: `prop_options_in_view(view, S01)` returns **`[]`**,
> because d42b1 skips a base on which the actor already has a live
> proposal, and the whole menu offered to that actor has kinds
> `['n', 'r']` — **no proposal of any kind**.
>
> **What V2 is NOT.**  `shared_base(4)` mints, spreads to fifteen
> actors, has one actor propose twice on that base back to back, and
> **stops by construction**: it is a 19-event **demonstration of
> `prop_options_in_view`**, not an alternative schedule that was driven
> and failed, and it never attempts an arbitration.  **It says nothing
> against one lineage PER ACTOR**: V3 `CONFLICT-GRID(4, R)` *is* a
> one-lineage-per-actor design and it does **not** refuse — it forces,
> tiles and reaches width 8.  The claim is, and is only, that a grid
> whose rows and columns conflict **concurrently** cannot run on one
> shared base.

> **THE `2g` LINEAGES, WITH THE STEP THAT MAKES IT TRUE (round-1
> MINOR 5).**  (1) A `k`-proposer conflict needs `k` live proposals on
> one base and one actor may hold at most one live proposal per base —
> that gives **two bases per actor**, not yet `2g` lineages.  (2) **The
> missing step:** two concurrent groups **cannot share a base**.
> `admissible` requires `triples(view, comp) == ckey` for a *whole*
> component, `View.components()` groups live proposals by base, and on
> one base the payload-0/payload-1 conflict graph of two groups is
> **connected** — so one base admits exactly one arbitration per
> generation.  (3) Hence `g` row bases + `g` column bases, pairwise
> distinct because every `(r, c)` cell sits in one of each: `2g`
> lineages.  **V1's mints-first bootstrap is forced by the grammar, not
> chosen for convenience.**

> **THE DELIVERY ECONOMICS, MEASURED.**  The concurrent schedule pays
> `2g(g−1) = 24` deliveries **once**, in the bootstrap, and **zero** in
> every round thereafter, at every `R` swept.  The rotating schedule
> pays `g(g−1) = 12` deliveries **every round after the first** — 36 at
> `R = 4`, 60 at `R = 6`.  At `k = 4` the rotation is not merely more
> expensive, it is asymptotically more expensive — **and it buys less
> width, 8 against 16**, because in it every depth-1 successor of an
> arbitration is a DELIVERY, so its measured `Σ_y b(y)` is `2k = 8`
> even though the record's own live `Bl` is 4: precisely the `Bl = 2`
> corner D66 identified, now exhibited at `k = 4`.

> **THE ARBITRATION ORDER IS LOAD-BEARING, AND THE CONTROL IS A ONE-LINE
> CHANGE (V4).**  V4 has the same actors, the same eight lineages, the
> same bootstrap, the same 32 proposals and 8 arbitrations per round, and
> the same zero in-round deliveries.  It differs from V1 in **nothing but
> the order of the arbitrations inside a round** (row 0, col 0, row 1,
> col 1, … instead of all rows then all columns).  Interleaving them
> **destroys the width**: `9 → 5` at `g = 3` and **`16 → 7` at `g = 4`**.
> That is the empirical content of this box.
>
> **AND WHAT IS *NOT* EMPIRICAL, MARKED AS SUCH (round-1 NIT 1).**  The
> refinement sentence *"the second concurrent consumer must sit at
> height + 1"* **cannot fail**.  `SKY-B(2)` counts events at *exactly*
> height + 2, so a successor at offset 1 contributes its `b(y)`
> successors while a successor at offset 2 contributes only **itself**
> (its own successors land at offset ≥ 3 and are not counted), and
> `b(e) ≤ Bl = k` caps that route at `k`.  The sentence is **the
> instrument's definition plus one inequality — DEFINITIONAL** — and it
> is labelled definitional wherever it appears here.  What is empirical
> is (a) that the *order* decides which successors sit at offset 1
> (V4), and (b) that a schedule **can** meet the condition at every `k`
> (§3b).

## 3. The width verdict, exhibited — and scoped to the statistic it measures

`max |D|` at `d = 2`, whole sweep, beside the re-run controls:

| record | `k` | `B` (W4b `B²`) | live `Bl` (W4c `Bl²`) | measured max `Σ_y b(y)` | max `|D|` d2 / d3 |
|---|---|---|---|---|---|
| `DOUBLE-GRID(4, 1)` | 4 | 5 (25) | 4 (16) | 4 | 4 / 7 |
| `DOUBLE-GRID(4, 2)` | **4** | 5 (25) | **4 (16)** | **16** | **16 / 16** |
| `DOUBLE-GRID(4, 3)` | **4** | 5 (25) | **4 (16)** | **16** | **16 / 16** |
| **`DOUBLE-GRID(4, 4)`** [the flagship] | **4** | 5 (25) | **4 (16)** | **16** | **16 / 16** |
| **`LEVELLED-DGRID(4, 2)`** | **4** | 5 (25) | **4 (16)** | **16** | **16 / 16** |
| `DOUBLE-GRID(3, 2)` [D66 anchor] | 3 | 4 (16) | 3 (9) | 9 | 9 / 9 |
| `DOUBLE-GRID(3, 4)` [D66 anchor] | 3 | 4 (16) | 3 (9) | 9 | 9 / 9 |
| `DGRID-INTERLEAVED(3, 2)` | 3 | 4 (16) | 3 (9) | 9 | 5 / 6 |
| `DGRID-INTERLEAVED(4, 2)` | 4 | 5 (25) | 4 (16) | 16 | 7 / 7 |
| `CONFLICT-GRID(4, 4)` / `(4, 6)` | 4 | 5 (25) | 4 (16) | 8 | 8 / 8 |
| `DR(8,10,8)` [D63 delivery control] | — | 2 (4) | 2 (4) | 4 | 4 / 4 |
| genuine sprinklings (11 configurations) | — | — | — | — | **hull [10, 17] / [11, 17]** |

> **WHAT "SPRINKLING-GRADE" IS AND IS NOT (round-1 MAJOR 2).**
> **(a) The comparison range is a hull of two dimensionally distinct
> clusters.**  The eleven genuine configurations are five `M21` (2+1)
> and six `M31` (3+1) sprinklings, all at `N = 120`.  Their `max |D|` at
> `d = 2`: `M21` `[10, 11]`, `M31` `[14, 17]`.  **16 is not inside the
> 2+1 cluster at all** — it sits in the 3+1 one.  Every sentence in this
> unit that compares to "the sprinkling range" now names which
> sprinklings.
> **(b) `max` is the only column on which the record touches the
> population.**  At `d = 2` the `k = 4` records are *below* the
> homogeneity band and *below* the `|D| ≥ 4` band, whole and interior;
> the headline's mean chart is 2.09 directions against the sprinklings'
> 3.26–6.41; and three events of 120 carry the 16-wide chart.  The
> supported claim is about **the maximum, at one depth, at one `k`**.
> **(c) 16 is a parameter picked, not a coincidence discovered.**  By
> §3b the mechanism delivers `k²` whenever the `k` depth-1 consumers are
> levelled: 25 at `k = 5` and 36 at `k = 6`, **above the whole hull**.
> The surviving mechanism sentence is: *crossed conflict realizes W4c's
> `k²` at every `k` anyone has built, and the sprinkling maxima happen
> to bracket the `k = 4` value.*  **"The first sprinkling-grade width in
> the campaign" is withdrawn as a milestone claim about the mechanism.**
> **(d) NOT a size objection (round-1 NIT 3).**  All eleven
> configurations are at `N = 120` and the headline record is 120 events:
> the comparison **is** size-matched and no extreme-order-statistic
> caveat applies.  What needed the label was the dimensional population.

**The witnesses are exhibited, not counted** (the D66-round standard) —
**and counted correctly** (round-1 MINOR 2).  `DOUBLE-GRID(4, 2)` has
**three bases** whose `d = 2` chart has width 16, at events 73, 74 and
75 — and those three bases carry **ONE direction set**, `{80, …, 95}`,
because all four round-0 row arbitrations share the same four column
arbitrations as successors.  The record contains **exactly one 16-wide
chart, seen from three bases**; "three charts of width 16" was literally
true and materially misleading.  Each base is an `r`-event by `D11`,
`D22`, `D33`, at height 10, with **5 registers and 4 distinct
proposers** and live out-degree `b(e) = 4`, whose four depth-1
successors are events 76–79, **all four of them four-proposer
ARBITRATIONS with out-degrees `[4, 4, 4, 4]`**, so `Σ_y b(y) = 16 = k²`.
Every one of the sixteen directions (events 80–95) is read from the
**committed `d47a.sky`**, verified **ordered after the base in the
committed `poset_of` order** and **at exactly height + 2**, and its
`P`-path is printed.  The flagship `DOUBLE-GRID(4, 4)` carries
**11 bases** of width 16 (`g(R−1) − 1 = 11`), exhibited the same way,
one direction set per round with the repeats named as repeats.

**The shortfall is characterised, not hidden.**  The `R = 2` record has
16 conflict arbitrations, and the receipt reports **three different
counts rather than one**: **15 realize their whole `Σ_y b(y)` budget**
(including the ones whose budget is itself small), **1 falls short of
it**, and **3 attain the ceiling `k² = 16`**.  Round 0 has four row
arbitrations (events 72–75) and four column arbitrations (76–79); three
of the four row arbitrations attain the ceiling, and the one that falls
short — base 72, the row-0 arbitration by `D00` — has the same
`Σ_y b(y) = 16` and realizes only 4.  The census prints why: **its
successor height offsets are `[2]`, not `[1]`**.  It costs **exactly one
chart in the whole record, not one per round**: the `g = 3` family
realizes `g(R−1)` charts of width 9, the `g = 4` family `g(R−1) − 1`
(3 at `R = 2`, 7 at `R = 3`, **11 at `R = 4`**), and the loser is the
row-0 arbitration of the FIRST round, sitting one height layer below its
three siblings (9 against 10) because the bootstrap depresses it.
**§4b removes it.**

**The smallest witnesses, and a correction to a committed parent.**
`ARBCHAIN*(m, k)` — one `k`-proposer arbitration whose `k` proposer
registers are consumed by `m` further **`k`-proposer** arbitrations and
by `k − m` deliveries — realizes `k·m + 2(k − m)` **exactly** at
`k = 3, 4`:

| `k` | m = 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 3 (D66's committed values) | 6 | 7 | 8 | 9 | — | — |
| **4** | **8** | **10** | **12** | **14** | **16 = k²** | — |
| 5 (refined prediction 10, 13, 16, 19, 22, 25) | 10 | 9 | 12 | 15 | 18 | 17 |

> **D66's OWN `arbchain(m, k)` DOES NOT GENERALIZE, and this is said
> plainly.**  Its docstring claims `|D_e(2)| = k·m + 2(k − m)` "sweeps
> the WHOLE interval `[2k, k²]` as `m` runs `0..k`", but its secondary
> arbitrations are hardcoded to **three** proposers whatever `k` is.
> Re-run here at `k = 4` it gives **8, 9, 10, 11, 12 = `3m + 2(k − m)`**,
> with out-degree columns reading 3 and never 4.  **Nothing gated in D66
> is wrong**: its receipt only ever ran `k = 3`, where the two formulas
> coincide, and its note's table is a `k = 3` table.  What is corrected
> is the **blueprint's claim to general `k`**, and D67 supplies the
> corrected object, which reproduces D66's 6, 7, 8, 9 exactly at `k = 3`.

> **AND THE `k = 5` SHORTFALL IS A BOOTSTRAP ORDERING, NOT A WALL.**
> `ARBCHAIN*` at `k = 5` realizes 10, 9, 12, 15, 18, 17 against the
> ceiling 25.  **The cause is inside `ARBCHAIN*`'s own bootstrap:**
> `S_i` supplies `A_i` **and** all `k − 2` helpers `T_ij` by a serial
> delivery chain on register `S_i`, so `p(S_i, Y_i, 0)` sits `k − 1`
> layers above its mint and at `k = 5` two of the five secondary
> arbitrations land at height offset 2 from THE ARBITRATION.  That is a
> property of the **ordering of a bootstrap**, and one levelling pass
> removes it.  §3b is the removal.

## 3b. The ceiling ladder — `k²` at `k = 3, 4, 5, 6` (round-1 MAJOR 1)

**`ARBCHAIN**(k)`** is `ARBCHAIN*(k, k)` with every actor register
**height-levelled by the grammar's own `('n', a)` idle event** — the
same event kind the committed blueprints already use for their tails —
inserted between the bootstrap and the proposals, so that all `k`
depth-1 consumers sit at exactly height + 1.  Nothing else changes: no
new lineage, no delivery, no arbitration.

| `k` | events | actors | levelling idles | common height | `h(e)` | `D(1)` | out-degrees | **`|D_e(2)|`** | `k²` |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 47 | 9 | 6 | 5 | 8 | 3 × `r` at offset 1 | `[3,3,3]` | **9** | 9 |
| 4 | 90 | 16 | 24 | 7 | 10 | 4 × `r` at offset 1 | `[4,4,4,4]` | **16** | 16 |
| **5** | **157** | **25** | 60 | 9 | 12 | 5 × `r` at offset 1 | `[5]×5` | **25** | 25 |
| **6** | **254** | **36** | 120 | 11 | 14 | 6 × `r` at offset 1 | `[6]×6` | **36** | 36 |

Forced at every `k`: menu hits `min = max = 1`, no refusal.  **The
`k = 5` member is verified to the D66-round standard**: the closure of
`P` **equals the committed `event_poset`** on all 157 events; the
committed heights equal ours; `|D_e(2)| = 25` is read from the
**committed `d47a.sky`**; the 25 directions are pairwise distinct, **all
ordered after the base in the committed order** and **all at height
exactly 12 + 2 = 14**, with their `P`-paths printed; `Bl = 5`; **W4c
holds at `d = 1, 2, 3` with zero violations**; every version register
occurs in exactly one `regs_of`.  And it carries **a complete C1
grade** — full-menu replay **157/157**, widest full menu **2,125
candidates** — a *higher* forcedness grade than any DOUBLE-GRID record
in this unit (§6).

> **WHAT THIS SETTLES.**  `k²` is **REALIZED at `k = 3, 4, 5 and 6`**.
> **Height alignment is a DESIGN REQUIREMENT that the grammar's own
> idles satisfy, not an obstruction.**  **D66's residue 6 stays CLOSED**
> and is *not* reopened.  The `k`-ceiling question is closed at every
> `k` anyone has built; what remains is the *general-`k`* proof, and one
> named tiling question (§8).
>
> **AND THE ATTRIBUTION TO PHASE SEPARATION IS WEAKENED ACCORDINGLY.**
> `ARBCHAIN**` has **no phase separation of any kind** and reaches the
> ceiling at every `k`.  The general lever is the definitional condition
> — *the `k` depth-1 consumers must sit at height + 1* — and phase
> separation is how the *tiling* schedule meets it, levelling is
> another way, and the **condition** is what is load-bearing.

## 4. The band question — the whole-record result, on both columns, as a crossing

**ROUND-1 BLOCKER 1, SAID FIRST.**  The first version stopped the sweep
at `R = 3`, reported the `d = 3` homogeneity trend
`0.4625 → 0.5417 → 0.6562` against a floor of `0.6833` — *a monotone
sequence one step below the floor with growing increments* — and then
stated the negative as a property of `k = 4`.  **It is a property of
`R ≤ 3`.**  The cost of the missing row was one build.

- **(i) WHOLE RECORDS: `DOUBLE-GRID(4, 4)` IS IN BAND, ON BOTH `d = 3`
  COLUMNS, AT `max |D| = 16`.**  200 events, 16 actors, forced, menu
  hits `[1, 1]`, **zero in-round deliveries**, total arbitration share
  `1/5`, `max |D| = 16` at both depths.

  | | `d = 2` homogeneity | `d = 2` `|D| ≥ 4` | `d = 3` homogeneity | `d = 3` `|D| ≥ 4` |
  |---|---|---|---|---|
  | `DOUBLE-GRID(4, 4)` | `97/200 = 0.4850` below | `0.4000` below | **`29/40 = 0.7250` IN** | **`0.6350` IN** |
  | re-run sprinkling band | `[0.6417, 0.8000]` | `[0.4250, 0.6500]` | `[0.6833, 0.8167]` | `[0.6000, 0.7583]` |

  Width histograms: `d = 2` `{0:28, 1:75, 2:7, 3:10, 4:69, 16:11}`,
  `d = 3` `{0:34, 1:21, 2:12, 3:6, 4:73, 5:1, 6:3, 7:2, 16:48}`.
  **This is more than D66's `k = 3` flagship achieves**, which is in
  band on the homogeneity column and at `|D| ≥ 4` `13/40 = 0.325` at
  `d = 3`, far below `[0.6, 0.7583]`.
- **(ii) BOTH COLUMNS, EVERYWHERE (round-1 MAJOR 4).**  K0c computes
  **two** sprinkling bands at each depth and the first version read
  every verdict on the first alone.  On the second column the cell the
  first version shipped — the **interior** of `DOUBLE-GRID(4, 2)` — is
  **below** the band at both depths: `d = 3` homogeneity `60/80 = 3/4`
  **IN**, `d = 3` `|D| ≥ 4` `47/80 = 0.5875` **BELOW** `[0.6, 0.7583]`;
  `d = 2` `0.4125` and `0.2000`, both **below**.  It was in band **on
  one column of two**.  The same is true of D66's committed flagship, so
  this is a **corpus-level habit this unit inherited rather than
  invented** — said once, here, and carried.
- **(iii) IT IS A CROSSING, NOT A MATCH (round-1 MAJOR 5).**  Both `d = 3`
  homogeneity sequences are **monotone in `R`** and the band is an
  interval each **crosses**, at a different `R`:

  | `R` = | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | **WHOLE record**, `d = 3` | 0.4625 | 0.5417 | 0.6562 | **0.7250 IN** |
  | **INTERIOR population**, `d = 3` | 0.6154 | **0.7500 IN** | 0.8333 ABOVE | 0.8750 ABOVE |

  So **"in band" names a round number**: at `R = 2` the interior is in
  band and the whole record is not; at `R = 4` the whole record is in
  band and the interior is above.  A one-parameter family monotone in a
  statistic crosses any interval somewhere.  **The first version read
  one cell of this table and called it a frontier.**  What survives is
  the crossing, reported as a crossing — **and the fact that at `R = 4`
  the crossing happens on both columns while the record carries `k²`.**
- **(iv) THE INTERIOR IS A POPULATION, NOT AN OBJECT (round-1 MINOR 6).**
  `interior_of` returns the **full** closure and a **subset of events**;
  `profile` then averages over that subset while every chart is still
  computed on the whole record — a base at height `hi − 3` still reads
  directions at `hi − 1`, inside the excised layers.  An interior figure
  is a **conditional average over 80 of 120 events**: not a record, not
  a sub-poset, and **not an object**.  The word *object* is withdrawn.
  For the same reason, "no wide chart is a boundary artefact" tests that
  the **base** is off the boundary — which it is, all wide bases sit at
  heights 9–10 inside `[2, 12]` — and **not** that the chart's contents
  are.

> **THE FRONTIER DOES NOT EXIST.**  At `k = 3` width 9 and `d = 3` band
> membership compose on the whole record.  **At `k = 4` width 16 and
> `d = 3` band membership also compose on the whole record, at `R = 4`,
> on BOTH band columns — the same `R` at which D66's `k = 3` flagship
> achieves it on one.**  The `R = 2` interior result is that same
> phenomenon seen two rounds early.  At `d = 2` nothing in this unit is
> in band, whole or interior, at either `k` — that is residue 3 and it
> is untouched.

The mechanism is measured rather than guessed: the budget bound thins
conflict from `1/4` to `1/5`, and the width histograms show where the
homogeneity goes — the `k = 4` records carry a large population of
width-0 and width-1 charts (`{0: 28, 1: 43, …}` at `R = 2`) against a
handful of very wide ones.  **A wider record at *fixed round count* is a
more heterogeneous record — and the remedy is more rounds, which is
exactly what the `R = 4` row is.**

## 4b. The levelling lever — residue 2 closed (round-1 NIT 2)

The first version filed as **unbuilt** the question whether a bootstrap
exists that **levels** the first round's four row arbitrations.  Round 1
built it in one pass of the grammar's own idle event; it is rebuilt and
gated here.

| | events | width-16 charts (d = 2) | `d = 2` homog | `d = 3` homog | interior `d = 3` homog | total arb share |
|---|---|---|---|---|---|---|
| `DOUBLE-GRID(4, 2)` | 120 | **3** | `49/120 = 0.4083` | `13/24 = 0.5417` | `0.7500` IN | `1/5` |
| **`LEVELLED-DGRID(4, 2)`** | 140 (20 idle pads) | **4** | `61/140 = 0.4357` | `17/28 = 0.6071` | **`4/5 = 0.8000` IN** | `6/35` |

Width histograms: `d = 2` `{0:12, 1:67, 2:7, 3:10, 4:40, 16:4}`,
`d = 3` `{0:25, 1:30, 2:10, 3:6, 4:43, 5:1, 6:3, 7:2, 16:20}`.  The
row-0 arbitration of the first round — the one that realized 4 of its
16 — now realizes its whole budget: **four width-16 charts per round
instead of three**, and homogeneity rises at **both** depths.  **Residue
2's conjecture is right on both halves and it cost one pass of the
grammar's own idle event.**  **The trade, recorded:** the pad dilutes
the `1/(g+1)` arbitration-share coincidence from `1/5` to `6/35`.  It
does **not** by itself put the whole record in band — that is §4's
`R = 4` row.

## 5. The coboundary battery — and D66's residue 5, swept

The whole D64 instrument is re-run unmodified and **anchored**: on
`DOUBLE-RING(8, 10, 8)` at REG and `d = 2` it reproduces every committed
figure (60 charts, 138 labelled overlaps, 9 components, 0 obstructions,
`ε` = 32/28, 0 survivors, 108 Čech triples / 0 violations, split 57/115,
REGA `ε` = 40/20).  **The census now contains BOTH 16-wide records**
(round-1 MINOR 3): `DOUBLE-GRID(4, 3)`, which carries `max |D| = 16` at
both depths with seven wide charts, was outside the first version's
census while its claim (vi) said *"every `k = 4` wide record"*.  It is a
substrate here.

- **D64's own C7 returns ZERO obstructions at every cell of the
  census**, and so does the **FREE-RELABELLING** route — the largest
  possible gauge group, validated here to have a true positive and a
  true negative before being pointed at data.  **No non-trivial
  structure group is exhibited by `k = 4` conflict either**: D64's
  successor question is answered NEGATIVELY again, on the widest
  substrate the campaign has built.
- **What is NOT zero is the PARITY route, at ARBLOSE and nowhere else**
  — the winner/loser port order, on the DOUBLE-GRID schedule, plus the
  sprinkling cells at COV.  **D66's residue 5 named exactly that
  convention and asked for a sweep.  The sweep is here**, and the answer
  is that ARBLOSE obstructs on the DOUBLE-GRID schedule at **`k = 3` as
  well** (on `DOUBLE-GRID(3, 4)`, a record D66 never put through its own
  A4 census): **it is a property of the schedule and of that port
  convention, not of the proposer count.**  C7 does not see it because
  it drops the `other` class by construction — its ARBLOSE domain
  shrinks from 133 edges to 29 on the `R = 2` record.
- **It is reported and NOT claimed as `H¹ ≠ 0`**, on grounds this
  receipt measures: the free-relabelling route trivializes every one of
  those cells; and the genuine sprinklings carry non-zero parity
  obstructions too at COV, so on this statistic the DOUBLE GRID sits
  with the sprinklings and against the delivery crystal, which is zero
  everywhere.  Two further grounds are **carried from D64/D66 and NOT
  re-measured here**: that the `Z/2` name is itself a convention (D64's
  C4b extension census) and that the obstruction count is not an
  invariant magnitude.  This unit names no magnitude; the only statement
  it makes is `≠ 0`.
- **PROBE 1 (D64's C2b artefact probe) is printed per substrate and
  depth** and the blind ROLE cells are listed and **excluded by name**
  from every convention-robustness sentence.  No outcome anywhere is
  read at RAW.
- **THE DISQUALIFIER IS IN THE LABEL** (round-1 MINOR 7): the gate's own
  parenthesis reads "headline `k = 4` record trivial at every convention
  and route = **False**", and the predicate actually gated is the
  **route-agreement**, not the triviality.  The label now says so.

## 6. Forcedness, the C1 accounting, instrument hygiene, scope

- **K1a, the restricted-menu drive:** 11 configurations, 1,520 events,
  0 refusals, max menu hits per specification = 1 at every step of every
  record.  Uniqueness is structural; the gated content is that the event
  was OFFERED.  **Scope of the prefix rows:** `DOUBLE-GRID(4, 1)`,
  `(4, 2)` and `(4, 3)` are read off the flagship's own drive by the
  **R-prefix lemma** (below), so their forcedness is that drive's, step
  for step, and not a separate claim.
- **THE R-PREFIX LEMMA, a runtime economy that is GATED and not
  assumed.**  `dgrid` appends rounds, so the `R`-round record is a
  **prefix** of the `R'`-round record for `R < R'`.  The identity is
  checked **event for event at `g = 3`**, between two *separate* builds
  both of which K0d gates against d66's own function object; at `g = 4`
  the lemma buys the flagship's extra round — `DOUBLE-GRID(4, 4)` is
  built once and the three shorter records are read off its prefixes —
  and **every one of those three rows reproduces the round-1 committed
  row**, each of which round 1 reproduced again in a driver of its own.
  The economy changes the runtime and nothing else.
- **K1d, D60's C1 grade — THE TWO GRADES SEPARATED, AND THE NUMBER
  PRINTED (round-1 MAJOR 3).**  The whole sweep carries the
  **restricted-menu** grade of K1a.  D60's C1 grade — *all* actors
  offered at every step — is a different and strictly stronger property,
  it is expensive, and it was run on **five records totalling 406
  steps**:

  | record | replay | note |
  |---|---|---|
  | `ARBCHAIN*(0, 4)` | 22/22 (widest menu 164) | complete |
  | `ARBCHAIN*(4, 4)` | 66/66 (widest menu 896) | **complete; the 16-direction witness** |
  | **`ARBCHAIN**(5)`** | **157/157 (widest menu 2,125)** | **complete; the 25-direction witness** |
  | `DOUBLE-GRID(3, 2)` | 72/72 (widest menu 536) | complete; D66's committed figures to the digit |
  | `DOUBLE-GRID(4, 2)` | **71/120, BUDGET-CUT** (widest menu 1,056) | printed 150 s budget |

  **"1,040 events, C1-graded" was never true and is not said here.**  Of
  the eleven swept configurations, one — `DOUBLE-GRID(3, 2)`, a `k = 3`
  anchor — is C1-complete; `DOUBLE-GRID(4, 1)`, `(4, 3)`, `(4, 4)`,
  `LEVELLED-DGRID(4, 2)`, both interleaved records and both
  CONFLICT-GRIDs were **never full-menu replayed at all**.
  **The pin's K1 named the headline record and the gap is carried as a
  limitation, not papered over:** `DOUBLE-GRID(4, 2)` is cut at 71/120,
  and the budget is a **receipt-runtime choice**, not a property of the
  object — the 157-event `ARBCHAIN**(5)` replays *complete* in this same
  receipt at a larger printed budget.  What is delivered instead is
  **two complete C1 records that carry the `k²` ceiling** (16 and 25
  directions), so the C1 grade for a ceiling-carrying record does not
  rest on the cut record at all.  **What is still missing is a
  C1-complete *tiling* record at `k = 4`.**  That is a limitation of
  this receipt and is filed as residue 5.
- **THE ARBITRATION SHARE, IN ITS THREE SEPARATE READINGS (round-1
  MINOR 1).**  The `R = 2` record's **24 arbitrations are 16
  FOUR-proposer conflict arbitrations and 8 ONE-proposer bootstrap
  mints** — *not* "24 arbitrations of four proposers each".  Its
  **CONFLICT-arbitration share is `2/15`**, not `1/5`.  Its `k_min` is
  1, so **its own applicable budget bound is `1/2` and is NOT
  saturated**; what `1/5` equals is `1/(k_conflict + 1)`, the bound for
  a record all of whose arbitrations carry four proposers, which this
  one is not.  **"The budget bound SATURATED" is withdrawn.**  What is
  genuinely gated is the strictly stronger equality `#proposals =
  Σ_arb k_arb = 72` with no consumed triple repeated — **and the
  mechanism behind the `1/(g+1)` coincidence, which the first version
  left unstated**: the bootstrap is `2g` mint-proposals + `2g`
  mint-arbitrations + `2g(g−1)` deliveries = `2g(g+1)` events with `2g`
  arbitrations, and each round is `2g²` proposals + `2g` arbitrations =
  `2g(g+1)` events with `2g` arbitrations, so **both phases sit at
  `1/(g+1)` for unrelated reasons** and the total is `1/(g+1)` at every
  `R`.  Levelling breaks the coincidence exactly as it should (§4b).
- **Single sources, gated.**  The transport grammar by text-slice from
  committed d42b1 (cut at its own banner print); d47a, d55c, d58, D60's
  blueprint machinery, D63's `double_ring`/`wide_brick`, **D64's entire
  cocycle instrument** and **D66's own `double_grid`, `conflict_grid`,
  `arbchain`, `_pick`, `_skyB`, `my_ord_tuple`, `uf_trivialize`,
  `parity_obstruction`, `_c7_edges`, `interior_of` and
  `full_menu_replay`** by AST extraction.  This unit re-implements no
  committed layer and no committed instrument.  **THE EXIT SCAN IS
  WIDENED (round-1 NIT 4):** besides the `exit`/`quit`/`_exit` name scan
  in CALL and bare NAME/ATTRIBUTE form, every top-level body containing
  a **reflective construct** (`getattr` / `setattr` / `eval` / `exec` /
  `__import__` / `compile` / `vars` / `globals` / `locals`) is now
  reported **by name**, and the gate is that **none of them is a body
  this unit binds**.  Every hit lives in the committed `_ext` extraction
  helpers, which this unit never calls: the declared hole is not merely
  disclosed, it is **empty on the bodies actually called**.
- **The blueprint anchor is the strong form.**  `dgrid(3, R, 'phase',
  'mints')` produces the **same event list, event for event**, as the
  committed `d66.double_grid(3, R)` function object, and both reproduce
  D66's committed `(3, 2)` and `(3, 4)` rows exactly, including
  `(3, 4)`'s full width histogram `{0:10, 1:48, 2:5, 3:46, 4:2, 9:9}`.
- **Anchors (exit 1 reserved for these):** K0a single sources **and the
  reflective-body scan**; K0b D63's `DR(8,10,8)` row and D60's brick
  event for event; K0c the eleven genuine sprinkling configurations
  reproducing `[77/120, 4/5]`, `[17/40, 13/20]`, the max `|D|` range
  `[10, 17]` **and its two dimensional clusters `M21 [10, 11]` /
  `M31 [14, 17]`**; K0d D66's committed DOUBLE-GRID rows; **K0f the
  R-prefix lemma and the round-1 committed `g = 4` rows**; K5a D64's C0b
  instrument validation; K5e(i) D64's committed C7 row.
- **Determinism gated, WITH THE SCOPE IN THE LABEL (round-1 MINOR 7):**
  the `g = 3` double grid, its interleaved variant, `ARBCHAIN*(m, 4)` at
  `m = 0, 2, 4`, the SHARED-BASE refusal index and **`ARBCHAIN**(3)` and
  `ARBCHAIN**(4)` with their pad counts, levelling heights, `h(e)` and
  `|D_e(2)|`**, rebuilt under `PYTHONHASHSEED` 0 / 7 / 999,
  byte-identical stdout.  **IT DOES NOT COVER** the `g = 4` DOUBLE-GRID
  builds (including the flagship), `LEVELLED-DGRID`, `ARBCHAIN**(5)/(6)`
  or the K5 census.
- **Scope (pin §5).**  Grammar layer; the swept `(g, R, order, boot,
  level)` family and the ARBCHAIN\* / ARBCHAIN\*\* families, and no
  wider.  A crystal certifies MECHANISMS, never objects (#440).  No
  measure claim at transport scope and therefore no typicality.  `ω` is
  D58's chart-size ratio along covers, never a symmetric overlap.  Every
  width claim carries the record's own `B`, its live `Bl`, its
  **measured** `Σ_y b(y)` and both bounds; every gauge sentence carries
  the convention table; every band sentence carries its **column**.
  Transfer to the identified interactive click law runs through paper
  29's missing map (D59) and is not claimed; the missing map is not
  touched.
- **What bounded the sweep, printed rather than elided.**  The `g = 4`
  DOUBLE-GRID cost curve is `15.1 s → 107.9 s → 399.9 s → ~1,164 s` at
  `R = 1, 2, 3, 4` — which is why the R-prefix lemma is worth gating:
  the flagship is built once and pays only its own last round.
  `DOUBLE-GRID(5, R)` is still **out of this receipt's reach**, so the
  `k = 5` **ceiling** question is carried by `ARBCHAIN**(5)` and the
  `k = 5` **tiling** question is left open by name (§8).

## 7. The licensed claim

> **THE LICENSED CLAIM.**  Inside the swept family, at grammar layer:
> **(i)** a four-proposer conflict crystal **exists and forces** — 11
> configurations, 1,520 events, zero refusals at the **restricted-menu**
> grade, of which **406 steps across 5 records** carry D60's C1 grade
> and **4 of those records are C1-complete** — and it is
> **delivery-free after a once-paid bootstrap**, at a **total**
> arbitration share of exactly `1/(k_conflict + 1) = 1/5` at every `R`
> (its **conflict** share is `2/15`; its own applicable bound, with
> `k_min = 1`, is `1/2` and is not saturated); **(ii)** the mints-first,
> two-base-per-actor bootstrap is **forced by the grammar**, since
> `prop_options_in_view` offers no second live proposal on one base and
> two concurrent groups cannot share a base — a claim about ONE SHARED
> BASE, not about one lineage per actor, which forces (V3);
> **(iii)** chart width reaches **`max |D| = 16 = k²`**, W4c's ceiling
> realized at `k = 4`, at or above the re-run genuine sprinkling floor
> of 10 and inside the **hull** `[10, 17]` of the sprinkling maxima —
> a hull of the `M21` cluster `[10, 11]` and the `M31` cluster
> `[14, 17]`, so 16 sits in the 3+1 cluster and outside the 2+1 one —
> with every witnessing chart verified event by event against the
> committed sky, the committed order and its `P`-paths, and with
> `ARBCHAIN*(m, 4)` occupying the whole interval `[2k, k²] = [8, 16]` in
> a 66-event record that is C1-complete; **(iv)** the width is a
> property of **the arbitration order meeting a definitional height
> condition**, not of concurrency alone — interleaving the row and
> column arbitrations, changing nothing else, collapses 16 to 7 and 9 to
> 5 — and **phase separation is not the general lever**: `ARBCHAIN**`
> has none and reaches `k²`; **(v) UNIFORMITY SURVIVES THE WIDTH AT
> `k = 4` ON THE WHOLE RECORD**: `DOUBLE-GRID(4, 4)` is inside **both**
> `d = 3` sprinkling band columns (homogeneity `0.7250`, `|D| ≥ 4`
> `0.6350`) while carrying `max |D| = 16`, which is more than D66's
> `k = 3` flagship achieves — reported as a **crossing** of a monotone
> one-parameter family, not as a property of an object, and at `d = 2`
> nothing here is in band at either `k`; **(vi)** `k²` is realized at
> **`k = 3, 4, 5, 6`** by forced, menu-offered records, the `k = 5` one
> C1-complete at 157/157 — so **height alignment is a design
> requirement the grammar's own idles satisfy** and D66's residue 6
> stays closed; and **(vii)** the transition class of **both censused
> `k = 4` wide records** is **trivial by C7 and by free relabelling at
> every cell of the census**, with a non-zero **PARITY** obstruction at
> **ARBLOSE only** that also occurs at `k = 3` and is therefore a
> property of the schedule and the convention, reported and **not**
> claimed as `H¹ ≠ 0`.

## 8. Residues

1. **Is `k²` attainable by a *tiling* `k = 5` schedule?**  The
   **ceiling** question is closed: `ARBCHAIN**` realizes `k²` at
   `k = 3, 4, 5, 6`, and D66's residue 6 stays closed.  What is untested
   — by this unit and by round 1 — is whether a `DOUBLE-GRID(5, R)`
   exists, forces and reaches 25; it is out of this receipt's
   computational reach.  And the ladder is four data points, not a
   theorem: **a general-`k` proof that levelling always meets the
   height condition is the remaining residue.**
2. **The `d = 2` band is untouched by everything in this unit.**
   Nothing here, at `k = 3` or `k = 4`, whole or interior, is inside the
   `d = 2` homogeneity band while wide.  D66's residue 2 asked exactly
   this and it remains open.  *(The first version's residue 2 — the
   unbuilt levelled bootstrap — is CLOSED; see §4b.)*
3. **The ARBLOSE parity obstruction now has a third substrate and no
   proof.**  It fires on the DOUBLE GRID at `k = 3` and `k = 4` and on
   the rings (D66) with an odd pair count; what it is an obstruction
   *of*, given that the free-relabelling route is clean everywhere and
   the Čech behaviour is uninformative, is unanswered.
4. **No *tiling* `k = 4` record is C1-complete.**  The C1-complete
   ceiling-carrying records are `ARBCHAIN*(4, 4)` and `ARBCHAIN**(5)`;
   a C1-complete `DOUBLE-GRID(4, R)` needs either a bigger budget or a
   cheaper menu enumeration.  The pin's K1 named the headline record and
   this is the gap.
5. **Size, inherited and now dominant.**  ~1,164 s for a 200-event
   record at 16 actors is the binding constraint on this whole line; the
   R-prefix lemma buys one round and no more.  D60/D63/D66's size
   residue is now the thing that decides which questions can be asked.
6. **Determinism does not cover the flagship.**  The hash-seed probe
   covers the `g = 3` family and the small ARBCHAINs; the `g = 4`
   DOUBLE-GRID builds, `LEVELLED-DGRID` and the K5 census are outside
   it, for cost.

## 9. Corrections — what round 1 withdrew, verbatim

Round 1 reproduced **every published figure** of the first version of
this note and of its receipt — all 554 lines, every census, every
histogram, every witness block and every obstruction count, byte for
byte after normalising timings — confirmed the `|D| = 16` witness event
by event against the committed `sky` and the committed `event_poset`,
confirmed W4c, the anchors, the unfilled-successor census, both
interleaved controls, the V2 refusal *to the index*, and the ARBCHAIN
correction to D66.  **The arithmetic was completely sound.**  It then
broke what the unit built its headline out of, **by construction rather
than by argument**, three times.  All three constructions are credited
to the round, rebuilt here with this unit's own driver and **gated**;
every figure of all three reproduces the review's exactly.

**WITHDRAWN 1 — the flagship negative (BLOCKER 1).**

> ~~"Uniformity is the price: no *whole* `k = 4` record is in band at
> either depth, though the interior of `DOUBLE-GRID(4, 2)` is"~~ ;
> ~~"That lean is **confirmed for whole records**"~~ ;
> ~~"**(i) Whole records: no `k = 4` record is in band at either
> depth.**"~~ ; ~~"At `k = 4` width 16 and `d = 3` band membership
> compose **only on the interior**"~~ ; ~~"uniformity does **not**
> survive the width at `k = 4` on the **whole** record at either
> depth"~~ ; ~~receipt K4's "(i) NO swept `k = 4` record is inside the
> recomputed sprinkling homogeneity band at either depth, so the pin's
> honest lean is CONFIRMED for whole records"~~

are **false**.  They are properties of `R ≤ 3`, one build short of the
row that refutes them.  `DOUBLE-GRID(4, 4)` — the unit's own blueprint,
one more round — is inside the `d = 3` homogeneity band at
`29/40 = 0.7250` **and** inside the `d = 3` `|D| ≥ 4` band at `0.6350`,
**as a whole record**, at `max |D| = 16 = k²`.  Replaced by §4: **the
width-uniformity frontier at `k = 4` does not exist**, and the corrected
statement is a **crossing** — the whole-record sequence enters the band
at `R = 4`, the interior enters at `R = 2` and leaves at `R = 3`.
**LOG #475's "THE BAND: no whole `k = 4` record is in band at either
depth (the pin's lean held)" is superseded by this note**; so is its
"in-band and 16-wide **at the same evidence grade as D66's flagship**",
which upgraded §4's own careful sentence by a notch and then
contradicted the first half of the same entry.  The corrected headline
is: **at `R = 4` the `k = 4` record is in band on both `d = 3` columns
while the `k = 3` flagship is in band on one.**

**WITHDRAWN 2 — the `k = 5` obstruction and the reopening of D66's
residue 6 (MAJOR 1).**

> ~~"**AND THE CEILING IS NOT REACHED AT `k = 5` BY ANYTHING BUILT
> HERE.**"~~ ; ~~"`k²` is REALIZED at `k = 3` and `k = 4` and
> UNREALIZED at `k = 5` by every schedule this unit built"~~ ;
> ~~"D66's residue 6 is therefore **closed at `k = 4` and re-opened at
> `k = 5`**"~~

are **false as statements about the ceiling**.  The unit diagnosed the
cause correctly — height alignment — and then filed it as an open
residue instead of removing it.  The cause is entirely inside
`ARBCHAIN*`'s own bootstrap ordering, and one pass of the grammar's own
idle event removes it: `ARBCHAIN**` realizes `k²` at `k = 3, 4, 5, 6`
(§3b), and its `k = 5` member is C1-complete.  **D66's residue 6 stays
CLOSED.**  The surviving open question is the *tiling* one (residue 1).
LOG #475's "`k²` NOT reached at `k = 5` by anything built … D66 residue
6 closed at `k = 4`, REOPENED at `k = 5`" is superseded.

**WITHDRAWN 3 — "sprinkling-grade width", as a milestone claim about the
mechanism (MAJOR 2).**

> ~~"**K-III. SPRINKLING-GRADE WIDTH FROM PURE INTERACTION**"~~ as a
> title ; ~~"inside the genuine sprinkling range `[10, 17]` for the
> first time in the campaign"~~ ; ~~LOG #475's "**THE FIRST
> SPRINKLING-GRADE WIDTH IN THE CAMPAIGN, from crossed conflict
> alone**"~~

overstate a one-column, one-`k` measurement.  `[10, 17]` is the **hull**
of two dimensionally distinct clusters (`M21 [10, 11]`, `M31 [14, 17]`)
and 16 is not in the 2+1 one; `max` is the only column on which the
record touches the population, and on every other width column it is far
below at both depths; and by §3b the mechanism gives 25 at `k = 5` and
36 at `k = 6`, **above the whole hull**, so 16 is a parameter picked and
not a coincidence discovered.  Replaced by §3's scoped form: *the
maximum chart width reaches a value inside the hull of the sprinkling
maxima*, and *crossed conflict realizes W4c's `k²` at every `k` anyone
has built*.

**WITHDRAWN 4 — three accounting sentences (MAJOR 3, MINOR 1, MINOR 2).**

> ~~"a four-proposer conflict crystal exists and forces — 1,040 events,
> zero refusals, **C1-graded**"~~ — the 1,040 events carry the
> **restricted-menu** grade; C1 was delivered on 231 of them and the
> headline record was budget-cut at 71/120.  Replaced by §6's table and
> the printed C1 step count.
> ~~"an arbitration share of **exactly `1/5` = `1/(k+1)`, the budget
> bound SATURATED**"~~ and the receipt's ~~"**24 arbitrations of FOUR
> proposers each**"~~ — 8 of the 24 are one-proposer bootstrap mints,
> the conflict share is `2/15`, and with `k_min = 1` this record's own
> bound is `1/2` and is not saturated.  Replaced by §6's three readings
> and by the `1/(g+1)` mechanism the first version left unstated.
> ~~"`DOUBLE-GRID(4, 2)` carries **three charts of width 16**"~~ — three
> **bases** carry **one** direction set.  Replaced in §3.

**Round-1 findings carried without a withdrawal:** MAJOR 4 (both band
columns now reported everywhere, and the interior's `|D| ≥ 4` reading
printed beside its homogeneity reading — §4(ii)); MAJOR 5 (the verdict
restated as a monotone crossing, and LOG #475's "same evidence grade as
D66's flagship" superseded — §4(iii)); MINOR 3 (`DOUBLE-GRID(4, 3)`
added to the gauge census — §5); MINOR 4 (V2 scoped to what it shows,
against V3 — §2); MINOR 5 (the load-bearing step printed — §2);
MINOR 6 (the interior is a population, not an object — §4(iv));
MINOR 7 (both disqualifiers moved into their labels — §5, §6); NIT 1
(the height + 1 sentence marked definitional — §2); NIT 2 (residue 2's
"unbuilt" corrected and the object gated — §4b); NIT 3 (the
size-matching noted so the repair did not add the wrong caveat — §3);
NIT 4 (the exit scan widened — §6).  **No finding of round 1 was
rejected.**
