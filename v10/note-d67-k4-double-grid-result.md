# D67 — result: **K-III. SPRINKLING-GRADE WIDTH FROM PURE INTERACTION.** The k = 4 double grid forces, tiles delivery-free at an arbitration share of exactly `1/5`, and carries **`max |D| = 16 = k²` — W4c's ceiling SATURATED at k = 4, inside the genuine sprinkling range `[10, 17]` for the first time in the campaign**. Uniformity is the price: no *whole* k = 4 record is in band at either depth, though the interior of `DOUBLE-GRID(4, 2)` is — in band at `d = 3` while sixteen directions wide.

**Status: GREEN-UNREVIEWED, 2026-07-27.**  No independent hostile round
has been run on this unit; the green-unreviewed discipline is in force
and every sentence below is the receipt's, not a referee's.  Pin
`note-d67-k4-double-grid-pin.md` (STRICT, FROZEN AND COMMITTED before
this file or its receipt existed).  Receipt
`v10/code/d67_k4_double_grid_exact.py`, output
`v10/data/d67_k4_double_grid_exact.out` — **26 PASS / 0 FAIL, exit 0,
1328.8 s wall clock** (run from the repo root).  Parents: D66 (TERMINAL —
the width ceiling is `k·b ≤ k²`, saturated at 9 by `DOUBLE-GRID(3, R)`;
crossed conflict is the mechanism), W4c (the dead-wire theorem: width is
bought by PROPOSER count, not register count), D64/D65 (the coboundary
instrument and the descent defect), D63/D60/D58/D47a/D55c (the wide
crystal, the tiling blueprints, the atlas, the sky, the sprinkling
controls), D42b1 (the transport grammar).

---

## 1. Which outcome fired

The pin pre-registered three outcomes and let the sweep decide.

> **K-III FIRED.**  The four-proposer schedule **forces** — nine
> configurations, 1,040 events, **zero refusals**, every event offered by
> the committed layer's own menu and specified by its FULL EVENT TUPLE,
> max menu hits per specification = 1 everywhere.  It tiles with **ZERO
> in-round deliveries** at an arbitration share of **exactly `1/5` =
> `1/(k+1)`, the budget bound SATURATED**.  And it carries **`max |D| =
> 16` at `d = 2` and at `d = 3`** — `k² = 16`, **W4c's own ceiling,
> SATURATED at `k = 4`** — which is at or above the re-run genuine
> sprinkling floor of **10** and inside the measured sprinkling range
> **`[10, 17]`**.  The pin's **K-I does not fire** (the schedule forces)
> and **K-II does not fire** (the width is not short of the floor).

The pin declined a lean on the width verdict and took an honest lean on
the band question: *band membership should get HARDER as `k` grows.*
That lean is **confirmed for whole records and refuted on the interior**
— §4 states both halves.

## 2. The design problem the pin named, and the four schedules

A `k = 4` arbitration needs **four live proposals on one shared base**.
On a 4 × 4 actor grid, row `r`'s four actors must all hold the row base,
column `c`'s four must all hold the column base, and the minted version
goes to **all four proposers** (`View.holdings`), so a group that
arbitrates together needs no re-supply.  What costs deliveries is
rotation — and the pin asked whether the row/column rotation at `k = 4`
forces a two-base holding pattern or a delivery bill.  It forces the
two-base pattern, and the grammar itself is what forces it.

| variant | forces? | in-round deliveries | arb share | `max |D|` d2 / d3 |
|---|---|---|---|---|
| **V1 `DOUBLE-GRID(4, R)`** mints-first, phase-separated | **yes** | **0** (24 in the bootstrap, once) | **1/5 — SATURATED** | **16 / 16** |
| V2 `SHARED-BASE(4)` one lineage | **NO — REFUSES** | — | — | — |
| V3 `CONFLICT-GRID(4, R)` rotation, delivery-supplied | yes | **12 per round after the first, forever** (36 at R=4, 60 at R=6) | 4/29, 2/15 | 8 / 8 |
| V4 `DOUBLE-GRID(4, R, order='inter')` interleaved arbitrations | yes | 0 | 1/5 | **7 / 7** |

> **THE REFUSAL IS THE MECHANISM (V2).**  Mint ONE version, spread it to
> all sixteen actors, and let rows and columns conflict on that base:
> the record **breaks at its 18th event**, at the second proposal of the
> first actor.  The gate is not "the menu had no hit" but the layer's own
> option list: `prop_options_in_view(view, S01)` returns **`[]`**, because
> d42b1 skips a base on which the actor already has a live proposal, and
> the whole menu offered to that actor has kinds `['n', 'r']` — **no
> proposal of any kind**.  A `k`-proposer conflict needs `k` live
> proposals ON ONE BASE and one actor may hold at most one live proposal
> per base; a grid whose rows and columns conflict **concurrently**
> therefore needs **two distinct unsuperseded bases per actor**, i.e.
> `2g` independent lineages.  **V1's mints-first bootstrap is forced by
> the grammar, not chosen for convenience.**

> **THE DELIVERY ECONOMICS, MEASURED.**  The concurrent schedule pays
> `2g(g−1) = 24` deliveries **once**, in the bootstrap, and **zero** in
> every round thereafter, at every `R` swept.  The rotating schedule pays
> `g(g−1) = 12` deliveries **every round after the first** — 36 at
> `R = 4`, 60 at `R = 6`.  At `k = 4` the rotation is not merely more
> expensive, it is asymptotically more expensive — **and it buys less
> width, 8 against 16**, because in it every depth-1 successor of an
> arbitration is a DELIVERY, so its measured `Σ_y b(y)` is `2k = 8`
> even though the record's own live `Bl` is 4: precisely the `Bl = 2`
> corner D66 identified, now exhibited at `k = 4`.

> **THE PHASE SEPARATION IS LOAD-BEARING, AND THE CONTROL IS A ONE-LINE
> CHANGE (V4).**  V4 has the same actors, the same eight lineages, the
> same bootstrap, the same 32 proposals and 8 arbitrations per round, and
> the same zero in-round deliveries.  It differs from V1 in **nothing but
> the order of the arbitrations inside a round** (row 0, col 0, row 1,
> col 1, … instead of all rows then all columns).  Interleaving them
> **destroys the width**: `9 → 5` at `g = 3` and **`16 → 7` at `g = 4`**.
>
> **So D66's design finding is refined rather than repeated.**  D66:
> *"what a second direction needs is a second CONCURRENT consumer of the
> proposer's register."*  D67: **the consumer must also sit at height +
> 1.**  Only the phase-separated order puts every row arbitration exactly
> one layer below every column arbitration of the same round; only then
> is each proposer register of a row arbitration consumed by a
> `k`-proposer arbitration **at height + 1**, and only directions at
> **exactly** height + 2 are in the chart.

## 3. The width verdict, exhibited

`max |D|` at `d = 2`, whole sweep, beside the re-run controls:

| record | `k` | `B` (W4b `B²`) | live `Bl` (W4c `Bl²`) | measured max `Σ_y b(y)` | max `|D|` d2 / d3 |
|---|---|---|---|---|---|
| `DOUBLE-GRID(4, 1)` | 4 | 5 (25) | 4 (16) | 4 | 4 / 7 |
| **`DOUBLE-GRID(4, 2)`** | **4** | 5 (25) | **4 (16)** | **16** | **16 / 16** |
| **`DOUBLE-GRID(4, 3)`** | **4** | 5 (25) | **4 (16)** | **16** | **16 / 16** |
| `DOUBLE-GRID(3, 2)` [D66 anchor] | 3 | 4 (16) | 3 (9) | 9 | 9 / 9 |
| `DOUBLE-GRID(3, 4)` [D66 anchor] | 3 | 4 (16) | 3 (9) | 9 | 9 / 9 |
| `DGRID-INTERLEAVED(3, 2)` | 3 | 4 (16) | 3 (9) | 9 | 5 / 6 |
| `DGRID-INTERLEAVED(4, 2)` | 4 | 5 (25) | 4 (16) | 16 | 7 / 7 |
| `CONFLICT-GRID(4, 4)` / `(4, 6)` | 4 | 5 (25) | 4 (16) | 8 | 8 / 8 |
| `DR(8,10,8)` [D63 delivery control] | — | 2 (4) | 2 (4) | 4 | 4 / 4 |
| genuine sprinklings (11 configurations) | — | — | — | — | **range [10, 17] / [11, 17]** |

**The witnesses are exhibited, not counted** (the D66-round standard).
`DOUBLE-GRID(4, 2)` carries **three charts of width 16**, at base events
73, 74 and 75 — `r`-events by `D11`, `D22`, `D33`, each at height 10,
each with **5 registers and 4 distinct proposers** and live out-degree
`b(e) = 4`, whose four depth-1 successors are events 76–79, **all four
of them four-proposer ARBITRATIONS with out-degrees `[4, 4, 4, 4]`**, so
`Σ_y b(y) = 16 = k²`.  Every one of the sixteen directions (events
80–95) is read from the **committed `d47a.sky`**, verified **ordered
after the base in the committed `poset_of` order** and **at exactly
height + 2**, and its `P`-path is printed: they are the sixteen
proposals of the next round, one per actor, with role words `(i, j)`
running over the whole 4 × 4 grid.

**The shortfall is characterised, not hidden.**  The headline record has
16 conflict arbitrations, and the receipt reports **three different
counts rather than one**: **15 realize their whole `Σ_y b(y)` budget**
(including the ones whose budget is itself small), **1 falls short of
it**, and **3 attain the ceiling `k² = 16`**.  Round 0 has four row
arbitrations (events 72–75) and four column arbitrations (76–79); three
of the four row arbitrations attain the ceiling, and the one that falls
short — base 72, the row-0 arbitration by `D00` — has the same
`Σ_y b(y) = 16` and realizes only 4.  The census prints why: **its
successor height offsets are `[2]`, not `[1]`** — its four column-arb
successors sit *two* layers above it, so their successors land at height
+ 3 and contribute nothing at depth 2.  This is exactly the
height-skipping exception D66's repair characterised.  It costs
**exactly one chart in the whole record, not one per round**: the
`g = 3` family realizes `g(R−1)` charts of width 9, the `g = 4` family
`g(R−1) − 1` charts of width 16 (**3 at `R = 2`, 7 at `R = 3`**), and
the census identifies the loser as the row-0 arbitration of the FIRST
round, sitting one height layer below its three siblings (9 against
10) because the bootstrap depresses it.

**The smallest witnesses, and a correction to a committed parent.**
`ARBCHAIN*(m, k)` — one `k`-proposer arbitration whose `k` proposer
registers are consumed by `m` further **`k`-proposer** arbitrations and
by `k − m` deliveries — realizes `k·m + 2(k − m)` **exactly**:

| `k` | m = 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 3 (D66's committed values) | 6 | 7 | 8 | 9 | — | — |
| **4** | **8** | **10** | **12** | **14** | **16 = k²** | — |
| 5 (predicted 10, 13, 16, 19, 22, 25) | 10 | 9 | 12 | 15 | 18 | **17 — NOT the ceiling** |

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

> **AND THE CEILING IS NOT REACHED AT `k = 5` BY ANYTHING BUILT HERE.**
> `ARBCHAIN*` at `k = 5` realizes 10, 9, 12, 15, 18, 17 against the
> refined prediction 10, 13, 16, 19, 22, 25 and the ceiling 25.  The
> reason is the same height mechanism: the longer bootstrap delivery
> chains at `k = 5` push some depth-1 successors off height + 1.  So the
> honest statement of the ladder is: **`k²` is REALIZED at `k = 3` and
> `k = 4` and UNREALIZED at `k = 5` by every schedule this unit built**;
> whether some `k = 5` schedule reaches 25 is open (§8).

Both bounds hold everywhere, event by event: W4b's `B^d`, W4c's `Bl^d`,
the **exact containment** `D_e(2) ⊆ succ(e) ∪ ⋃_y succ(y)` at every
event of every record with zero violations, and the sharp sum form with
its exceptions counted and characterised.  Every version register occurs
in exactly one event's `regs_of` on every record built here — W4c's
dead-wire step, measured again on `k = 4` substrates.  The interior
control (D60's C7 excision, run on **every** swept record at **both**
depths) leaves `max |D|` unchanged everywhere: **no wide chart in this
unit is a boundary artefact.**

## 4. The band question, both halves

**The pin's honest lean is confirmed for whole records and refuted on
the interior, and both are stated.**

- **(i) Whole records: no `k = 4` record is in band at either depth.**
  `DOUBLE-GRID(4, R)` homogeneity runs `0.3250 → 0.4083 → 0.4562` at
  `d = 2` and `0.4625 → 0.5417 → 0.6562` at `d = 3` for `R = 1, 2, 3`,
  against the re-run bands `[77/120, 4/5] = [0.6417, 0.8000]` and
  `[41/60, 49/60] = [0.6833, 0.8167]`.  Rising with `R`, still below at
  the largest `R` this receipt could afford.  The same pipeline, the same
  band and the same depth put D66's committed `k = 3` flagship
  `DOUBLE-GRID(3, 4)` **INSIDE** the `d = 3` band at `47/60 = 0.7833`
  while it carries `max |D| = 9` — so the `k = 4` rows are a
  measurement, not a blind spot, and the gate is written against exactly
  that control.
- **(ii) Interiors: `DOUBLE-GRID(4, 2)` IS in band at `d = 3` while
  sixteen directions wide.**  Under D60's own interior excision — the
  control D66 used to **answer** its own residue 2 — its `d = 3`
  homogeneity moves `0.5417 → 0.7500`, inside the band, with `max |D|`
  unchanged at 16.  `DOUBLE-GRID(4, 3)` overshoots to `0.8333` (above),
  as D66's `k = 3` records do at `0.9333` and `0.9677`.

> **THE FRONTIER, STATED AT THE GRADE THE EVIDENCE SUPPORTS.**  At
> `k = 3` width 9 and `d = 3` band membership compose **on the whole
> record**.  At `k = 4` width 16 and `d = 3` band membership compose
> **only on the interior**.  The direction of the pin's lean is right —
> uniformity gets harder as `k` grows — but the failure at `k = 4` is
> an **ends effect at the same grade of evidence at which D66 closed its
> residue 2**, not a collapse.  At `d = 2` nothing in this unit is in
> band, whole or interior, at either `k`.

The mechanism is measured rather than guessed: the budget bound thins
conflict from `1/4` to `1/5`, and the width histograms show where the
homogeneity goes — the `k = 4` records carry a large population of
width-0 and width-1 charts (the bootstrap deliveries and the round's
proposals: `{0: 28, 1: 43, 2: 7, 3: 10, 4: 29, 16: 3}` at `R = 2`)
against a handful of very wide ones.  **A wider record at fixed round
count is a more heterogeneous record.**

## 5. The coboundary battery — and D66's residue 5, swept

The whole D64 instrument is re-run unmodified and **anchored**: on
`DOUBLE-RING(8, 10, 8)` at REG and `d = 2` it reproduces every committed
figure (60 charts, 138 labelled overlaps, 9 components, 0 obstructions,
`ε` = 32/28, 0 survivors, 108 Čech triples / 0 violations, split 57/115,
REGA `ε` = 40/20).  **74 measurement cells** over 9 substrates × up to 5
port conventions × 2 depths (the two sprinklings carry only the
register-free COV instrument, since a sprinkling has no `H`), 9,163
overlapping pairs, 19,201 triples.

- **D64's own C7 returns ZERO obstructions at every one of the 74
  cells**, and so does the **FREE-RELABELLING** route — the largest
  possible gauge group, validated here to have a true positive and a
  true negative before being pointed at data.  **No non-trivial
  structure group is exhibited by `k = 4` conflict either**: D64's
  successor question is answered NEGATIVELY again, on the widest
  substrate the campaign has built.
- **What is NOT zero is the PARITY route, at ARBLOSE and nowhere else.**
  Ten cells of the 74 carry a non-zero obstruction and **every grammar
  one of them is at ARBLOSE** — the winner/loser port order:
  `DOUBLE-GRID(4, 2)` at 51 (`d = 2`) and 64 (`d = 3`),
  `DOUBLE-GRID(4, 1)` at 2 and 10, and **`DOUBLE-GRID(3, 4)` at 33 and
  60** — plus the four sprinkling cells at COV.  **D66's residue 5
  named exactly that convention as the one that behaves differently and
  asked for a sweep.  The sweep is here**, and the answer is that
  ARBLOSE obstructs on the DOUBLE-GRID schedule at **`k = 3` as well**
  (on `DOUBLE-GRID(3, 4)`, a record D66 never put through its own A4
  census): **it is a property of the schedule and of that port
  convention, not of the proposer count.**  C7 does not see it because
  it drops the `other` class by construction — its ARBLOSE domain
  shrinks from 133 edges to 29 on the headline record.
- **It is reported and NOT claimed as `H¹ ≠ 0`**, on grounds this
  receipt measures: the free-relabelling route — the largest possible
  gauge group — trivializes every one of those cells; and the genuine
  sprinklings carry non-zero parity obstructions too at COV (10, 2, 19,
  34), so on this statistic the DOUBLE GRID sits with the sprinklings
  and against the delivery crystal, which is zero everywhere.  Two
  further grounds are **carried from D64/D66 and NOT re-measured here**:
  that the `Z/2` name is itself a convention (D64's C4b extension
  census) and that the obstruction count is not an invariant magnitude.
  This unit names no magnitude; the only statement it makes is `≠ 0`.
- **PROBE 1 (D64's C2b artefact probe) is printed per substrate and
  depth** and the blind ROLE cells — the cells where the read labeling
  could not have shown a transition, so that a flat reading there is an
  artefact — are listed and **excluded by name** from every
  convention-robustness sentence.  No outcome anywhere is read at RAW.

## 6. Forcedness, instrument hygiene, scope

- **K1a, the restricted-menu drive:** 9 configurations, 1,040 events,
  0 refusals, max menu hits per specification = 1 at every step of every
  record.  Uniqueness is structural (menu events are pairwise distinct
  and a specification is a full event tuple); the gated content is that
  the event was OFFERED.
- **K1d, D60's C1 grade (full-menu replay, all actors offered at every
  step):** `ARBCHAIN*(0, 4)` 22/22 (widest menu 164), **`ARBCHAIN*(4, 4)`
  66/66 (widest menu 896) — a COMPLETE `k = 4` record carrying a
  16-direction chart, replayed end to end**, and `DOUBLE-GRID(3, 2)`
  72/72 at widest menu **536**, reproducing D66's committed replay
  figures to the digit.  The headline `DOUBLE-GRID(4, 2)` is
  **BUDGET-CUT at step 71 of 120** against a printed 150 s budget
  (widest menu 1,056), and every step it reached was offered and unique.
  **Where the prefix bites, said out loud:** the C1 grade for a complete
  16-direction record rests on `ARBCHAIN*(4, 4)`, which is in the K5
  census; the restricted-menu drive already establishes admissibility of
  every event of the headline against its whole prefix, so what the cut
  tail lacks is exactly the "offered among ALL actors" property.
- **Single sources, gated.**  The transport grammar by text-slice from
  committed d42b1 (cut at its own banner print); d47a, d55c, d58, D60's
  blueprint machinery, D63's `double_ring`/`wide_brick`, **D64's entire
  cocycle instrument** and **D66's own `double_grid`, `conflict_grid`,
  `arbchain`, `_pick`, `_skyB`, `my_ord_tuple`, `uf_trivialize`,
  `parity_obstruction`, `_c7_edges`, `interior_of` and
  `full_menu_replay`** by AST extraction.  This unit re-implements no
  committed layer and no committed instrument.  Exit-freedom of the
  slice and of every extracted body is gated; **SCOPE**, said in the
  gate: a syntactic scan for `exit`/`quit`/`_exit` in CALL or bare
  NAME/ATTRIBUTE form, deciding no reachability.
- **The blueprint anchor is the strong form.**  `dgrid(3, R, 'phase',
  'mints')` produces the **same event list, event for event**, as the
  committed `d66.double_grid(3, R)` function object — not merely the
  same profile columns, which is all D66's own A1(d) could gate for its
  duplicate — and both reproduce D66's committed (3, 2) and (3, 4) rows
  exactly, including `(3, 4)`'s full width histogram
  `{0:10, 1:48, 2:5, 3:46, 4:2, 9:9}`.  **So the `g = 4` rows are
  produced by the object that reproduces the committed `g = 3` ones.**
- **Anchors (exit 1 reserved for these):** K0a single sources; K0b D63's
  `DR(8,10,8)` row exact at both depths and D60's brick event for event;
  K0c the eleven genuine sprinkling configurations reproducing
  `[77/120, 4/5]`, `[17/40, 13/20]` **and the max `|D|` range `[10, 17]`
  against which the K3 verdict is read**; K0d D66's committed
  DOUBLE-GRID rows; K5a D64's C0b instrument validation (closure of `P`
  equals the committed order on every `k = 4` substrate); K5e(i) D64's
  committed C7 row.
- **The hoisted SKY-B** is gated against the committed `d47a.sky` event
  for event on two whole records at both depths, one of them the
  headline `k = 4` record; every chart the unit EXHIBITS is read from
  the committed `sky` directly.
- **Determinism gated:** the `g = 3` double grid, its interleaved
  variant, `ARBCHAIN*(m, 4)` at `m = 0, 2, 4` (the 16-direction witness
  included) and the SHARED-BASE refusal index, rebuilt under
  `PYTHONHASHSEED` 0 / 7 / 999, byte-identical stdout — with the scope
  said aloud: it does **not** cover the `g = 4` DOUBLE-GRID builds or
  the K5 census.
- **Scope (pin §5).**  Grammar layer; the swept `(g, R, order, boot)`
  family and the ARBCHAIN\* families, and no wider.  A crystal certifies
  MECHANISMS, never objects (#440).  No measure claim at transport scope
  and therefore no typicality.  `ω` is D58's chart-size ratio along
  covers, never a symmetric overlap.  Every width claim carries the
  record's own `B`, its live `Bl`, its **measured** `Σ_y b(y)` and both
  bounds; every gauge sentence carries the convention table.  Transfer
  to the identified interactive click law runs through paper 29's
  missing map (D59) and is not claimed; the missing map is not touched.
- **What bounded the sweep, printed rather than elided.**  The cost
  curve of the DOUBLE-GRID builds is `15.1 s → 107.9 s → 399.9 s` for
  `g = 4` at `R = 1, 2, 3` (and `9.1 s → 84.5 s` at `g = 3` for
  `R = 2, 4`): the layer's own menu enumeration grows with the base
  count and every arbitration mints a version (D66's residue 7).
  `R` values swept in the DOUBLE-GRID family = `{1, 2, 3, 4}`; `g = 4`
  at larger `R`, and `DOUBLE-GRID(5, R)`, are **out of this receipt's
  reach**, so the `k = 5` probe the pin allowed is carried by
  `ARBCHAIN*(m, 5)` instead — which is why the `k = 5` result of §3 is a
  statement about *this unit's schedules* and not about `k = 5`.

## 7. The licensed claim

> **THE LICENSED CLAIM.**  Inside the swept family, at grammar layer:
> **(i)** a four-proposer conflict crystal **exists and forces** — 1,040
> events, zero refusals, C1-graded — and it is **delivery-free after a
> once-paid bootstrap**, at an arbitration share of exactly
> `1/(k+1) = 1/5`, the budget bound saturated; **(ii)** the mints-first,
> two-base-per-actor bootstrap is **forced by the grammar**, since
> `prop_options_in_view` offers no second live proposal on one base, and
> the one-lineage alternative refuses at its 18th event; **(iii)** chart
> width reaches **`max |D| = 16 = k²`**, W4c's ceiling **saturated at
> `k = 4`**, at or above the re-run genuine sprinkling floor of 10 and
> inside the range `[10, 17]` — with every witnessing chart verified
> event by event against the committed sky, the committed order and its
> `P`-paths, and with `ARBCHAIN*(m, 4)` occupying the whole interval
> `[2k, k²] = [8, 16]` in a 66-event record that is C1-complete;
> **(iv)** the width is a property of the schedule's **phase
> separation** and not of concurrency alone — interleaving the row and
> column arbitrations, changing nothing else, collapses 16 to 7 and 9 to
> 5 — so D66's design finding is refined to *the second concurrent
> consumer must sit at height + 1*; **(v)** uniformity does **not**
> survive the width at `k = 4` on the **whole** record at either depth,
> while under D60's own interior excision `DOUBLE-GRID(4, 2)` **is**
> inside the `d = 3` band at `max |D| = 16`; and **(vi)** the transition
> class of every `k = 4` wide record is **trivial by C7 and by free
> relabelling at all 74 census cells**, with a non-zero **PARITY**
> obstruction at **ARBLOSE only** that also occurs at `k = 3` and is
> therefore a property of the schedule and the convention, reported and
> **not** claimed as `H¹ ≠ 0`.

## 8. Residues

1. **Is `k²` attainable at `k = 5`?**  `ARBCHAIN*(m, 5)` tops out at 18
   (at `m = 4`, and 17 at `m = 5`) against the ceiling 25, and
   `DOUBLE-GRID(5, R)` is out of this receipt's computational reach.
   The obstruction measured here is **height alignment**, not the bound:
   a schedule that keeps all `k` depth-1 successors at height + 1 at
   `k = 5` would give 25.  D66's residue 6 is therefore **closed at
   `k = 4` and re-opened at `k = 5`**.
2. **The one row arbitration that loses its 16.**  Exactly one
   arbitration in the whole record — the row-0 arbitration of the first
   round — sits a height layer below its siblings, so its successors
   skip a layer and it realizes 4 of its 16.  Whether a bootstrap exists
   that levels the first round's four row arbitrations — which would
   also raise the record's homogeneity — is unbuilt, and it is the
   obvious next lever on §4's band question.
3. **The band at `d = 2` is untouched by everything in this unit.**
   Nothing here, at `k = 3` or `k = 4`, whole or interior, is inside the
   `d = 2` homogeneity band while wide.  D66's residue 2 asked exactly
   this and it remains open.
4. **The ARBLOSE parity obstruction now has a second substrate and no
   proof.**  It fires on the DOUBLE GRID at `k = 3` and `k = 4` and on
   the rings (D66) with an odd pair count; what it is an obstruction
   *of*, given that the free-relabelling route is clean everywhere and
   the Čech behaviour is uninformative, is unanswered.
5. **The headline's full-menu replay is still a prefix** (71 of 120).
   The C1-complete `k = 4` wide record is `ARBCHAIN*(4, 4)`; a
   C1-complete DOUBLE-GRID(4, R) needs either a bigger budget or a
   cheaper menu enumeration.
6. **Size, inherited and now dominant.**  400 s for a 160-event record
   at 16 actors is the binding constraint on this whole line; D60/D63/D66's
   size residue is now the thing that decides which questions can be
   asked.
