# D63 — result: **F3. THE WIDE CRYSTAL EXISTS.** Tiling homogeneity and chart width COMPOSE — and the new ceiling is a theorem, not a parameter.

**Status:** GREEN-UNREVIEWED, 2026-07-26.  Pin
`note-d63-wide-crystal-pin.md` (STRICT, committed before this file
existed).  Receipt `v10/code/d63_wide_crystal_exact.py`
(11 PASS / 0 FAIL, exit 0, ~5 min), output
`v10/data/d63_wide_crystal_exact.out`.  An independent hostile round
is required before anything here is citable.

---

## 1. Which falsifier fired

The pin pre-registered three outcomes and let the sweep decide.

> **F3 FIRED.**  Of 38 swept configurations, **14 sit INSIDE the
> recomputed sprinkling homogeneity band AND carry `|D| ≥ 4` charts at
> d = 2** — across BOTH object families (9 double-rings, 5 wide
> bricks).  D60's residue 2 — `max |D| = 3` at every `(M, R)` tried —
> was a property of the 1+1 brick's light cone, not of tiling records
> as such.

Neither wall stands: F1 (the grammar wall) is refuted by the 26 swept
configurations that reach `|D| ≥ 4` at all, and F2 (the trade-off
wall) by the 14 of those that do so *without* leaving the homogeneity
band.

**The witness (the substrate the cocycle unit asked for):**

> **DOUBLE-RING(M = 8, R = 10, coupling = 8): 177 events over 16
> actors — two 8-actor rings, each running D60's brick circuit, with
> all 8 inter-ring deliveries per round.  Every event offered by the
> layer's own menu, every specification matched by EXACTLY ONE
> candidate with ALL SIXTEEN ACTORS OFFERED AT EVERY ONE OF THE 177
> STEPS (widest full menu 528 candidates) — the record is FORCED, and
> nothing was tie-broken.  At d = 2: homogeneity 47/59 ≈ 0.7966,
> INSIDE the band [77/120, 4/5] = [0.6417, 0.8000]; `|D| ≥ 4` at 1/3
> of its events (the brick's is 0 at every parameter); max `|D|` = 4;
> mean ω 0.7299.  At d = 3: homogeneity 0.7740 (in the d = 3 band) and
> `|D| ≥ 4` at 0.6723 — INSIDE the d = 3 sprinkling width band
> [0.6000, 0.7583] as well.**

The pre-registered lean (pin §4: couriers should raise `max |D|` above
3 at some homogeneity cost, the open question being whether the cost
stays inside the band) held — and the cost is smaller than leaned:
the coupled-ring route buys width while homogeneity *rises*, provided
the coupling is complete.

## 2. The frontier (all figures d = 2; "band" = the W3 re-run
sprinkling band, "wide" = D58's `|D| ≥ 4` column, nothing else)

**WIDE-BRICK(M, R, C)** — D60's brick + C couriers on ring chords
`k ↦ (k mod M, (k + M/2) mod M)`, one courier phase after every brick
round:

| (M, R) | C = 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| (8, 14) | **0.7692** / 0.0000 / 3 | 0.6022 / 0 / 3 | 0.7355 / 0.0992 / 4 | 0.8658 / 0.1544 / 4 | 0.7062 / 0.1073 / 4 |
| (6, 10) | 0.7027 / 0 / 3 | 0.6491 / 0 / 3 | 0.8182 / 0.1039 / 4 | 0.5258 / 0.0103 / 4 | — |
| (10, 14) | 0.7531 / 0 / 3 | 0.5138 / 0 / 3 | 0.6788 / 0.0803 / 4 | 0.7758 / 0.1333 / 4 | — |

(homogeneity / `|D| ≥ 4` fraction / `max |D|`.  Cadence probe:
`(8, 14, C = 2)` at half cadence reads 0.7849 / 0.0538 / 4.)

**DOUBLE-RING(M, R, cpl)** — two M-rings, `cpl` inter-ring deliveries
per round:

| (M, R) | cpl = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| (8, 10) | 0.6907 / 0 / 3 | 0.3645 / 0 / 3 | 0.4530 / 0.0684 | 0.5433 / 0.1102 | 0.5912 / 0.1460 | 0.6735 / 0.2041 | 0.7261 / 0.2484 | 0.7485 / 0.2275 | **0.7966 / 0.3333** |
| (6, 14) | 0.7835 / 0 / 3 | 0.4054 / 0 / 3 | 0.5520 / 0.0960 | 0.6763 / 0.1727 | 0.7647 / 0.2418 | 0.7844 / 0.2635 | 0.8619 / 0.3923 | — | — |
| (4, 14) | 0.8000 / 0 / 3 | 0.5570 / 0 / 3 | 0.7204 / 0.1398 | 0.7383 / 0.2243 | 0.8760 / 0.4050 | — | — | — | — |

`max |D| = 4` at every `cpl ≥ 2` entry.  Rounds sweep at full coupling
`(M = 4, cpl = 4)`: `R = 10` 0.8315 / 0.3708, `R = 14` 0.8760 / 0.4050,
`R = 20` 0.9112 / **0.4320**, `R = 26` 0.9309 / **0.4470** — the last
two are inside the sprinkling `|D| ≥ 4` band [0.4250, 0.6500], at
homogeneity that has climbed above the band's top.

**Two shapes in this table are findings in their own right.**

1. **Coupling is not monotone, and one courier / one coupled position
   is WORSE THAN NONE.**  Every family dips at `C = 1` / `cpl = 1`
   (0.7692 → 0.6022; 0.6907 → 0.3645) and only recovers from `2`
   upward.  A partial coupling breaks the lattice's height regularity
   without buying a second direction everywhere; a complete coupling
   restores it and buys the direction.  Width, homogeneity and overlap
   all follow that shape.
2. **The whole width column jumps from 0 to positive exactly when the
   second direction becomes available at every wire** — `C = 2` on an
   8-ring, `cpl = 2` on a coupled pair — and never returns to 0.

## 3. The licensed claim, and the three ways it is limited

> **THE LICENSED CLAIM: inside the swept `(M, R, C, cpl)` family, the
> tiling mechanism and the width mechanism COMPOSE — a delivery
> circuit can tile at sprinkling-band homogeneity while carrying
> 4-direction charts at a third of its events.**  A MECHANISM
> statement at grammar layer, about the swept family and no wider
> (pin §4's instruction).

Three limits, all measured, all reported whichever way they landed:

- **At d = 2 no configuration is inside both sprinkling bands at
  once.**  The `|D| ≥ 4` fraction reaches the sprinkling band only in
  the rounds sweep, where homogeneity has already risen above the
  band's top.  **At d = 3 exactly two configurations do sit inside
  both**: the winner DR(8, 10, 8) at 0.7740 / 0.6723 and DR(4, 10, 4)
  at 0.8090 / 0.7303, against the d = 3 bands [0.6833, 0.8167] and
  [0.6000, 0.7583].  The depths disagree, as they did in D60.
- **The `max |D|` column never approaches sprinkling values** (4
  against 10–17) — and §4 shows it *cannot*.
- **ω must still be read as D58's round-1 MAJOR 2 requires** — a
  chart-size ratio along covers, not a symmetric overlap.  The wide
  records' ω (0.43–0.75, against the sprinklings' 0.048–0.133) is
  still far above the comparators, but the ordering means less here
  than it did for the brick: the statistic favours thin charts, and
  these records are the less thin ones.

## 4. Why the width stops at 4: THE BRANCHING BOUND `[THEOREM, verified]`

> **Theorem.**  Let every event of a record carry at most `B`
> registers (`regs_of`).  Then for every event `e` and every depth
> `d ≥ 1`, the SKY-B chart obeys `|D_e(d)| ≤ B^d`.
>
> *Proof.*  Write `R_e(k) = {f : e ≤ f, h[f] = h[e] + k}` for the
> reflexive `k`-layer, so `R_e(0) = {e}`, `R_e(k) = D_e(k)` for
> `k ≥ 1`, and `R_e(k) = ∅` for `k < 0`.  `event_poset` sets
> `pred[j] = ⋃_{r ∈ regs(j)} (pred[last[r]] ∪ {last[r]})`, so the order
> is the transitive closure of `P`: `x P y` iff `x` is the immediately
> preceding event on some register of `y`.  Each `P`-step raises height
> by at least 1, and each `x` has at most `|regs(x)| ≤ B`
> `P`-successors — one per register, the next event on that wire.
> Every `f > e` is reached from `e` by a `P`-path, whose first step is
> some `y` with `e P y`, so for `k ≥ 1`
> `R_e(k) = ⋃_{y : e P y} R_y(k − (h[y] − h[e]))`.  Induct on `k`: the
> union has at most `B` terms, each of size at most `B^{k−1}` because
> `h[y] − h[e] ≥ 1`.  Hence `|R_e(k)| ≤ B^k` and `D_e(d) = R_e(d)`.  ∎

Verified with zero violations on all 38 records built by this unit,
and **saturated** by 26 of them: a record of deliveries has `B = 2`
(carriers `{s, r}`), so `max |D| ≤ 4` at d = 2 — the double rings hit
`4 = 2²` exactly.

> **THE MECHANISM STATEMENT THIS UNIT CERTIFIES (the scale doctrine's
> ask): 3 was the brick's cone, 4 is the delivery grammar's ceiling.
> NO delivery circuit whatever can reach the sprinklings' `max |D|`
> 10–17 at d = 2.  Chart width past 4 is bought with ARBITRATION over
> conflicts, not with transport** — the layer has exactly one event
> species carrying more than 2 registers, the arbitration over a
> component with `k ≥ 2` distinct proposers (`regs` = proposers ∪ {new
> version}), and the receipt exhibits an admissible 3-register one
> (`q = 1/8`).

This turns D60's residue 2 from an open empirical ceiling into a
decided pair: the empirical ceiling is beaten (3 → 4), and the
remaining one is proved.

## 5. The interior control (D60's C7), on the frontier's key points

| record | FULL | INTERIOR |
|---|---|---|
| C = 0 anchor (D60's brick) | 65 ev, 0.7692 / 0.0000 | 51 ev, 0.9020 / 0.0000 |
| WIDE-BRICK(8, 14, C = 2) | 121 ev, 0.7355 / 0.0992 | 109 ev, 0.8165 / 0.1101 |
| **THE WINNER** DR(8, 10, 8) | 177 ev, 0.7966 / 0.3333 | 151 ev, 0.8808 / 0.3907 |
| DOUBLE-RING(6, 14, 6) | 181 ev, 0.8619 / 0.3923 | 161 ev, 0.9317 / 0.4410 |
| DOUBLE-RING(4, 26, 4) | 217 ev, 0.9309 / 0.4470 | 203 ev, 0.9754 / 0.4778 |

Excising the bottom two and top three height layers **raises both
columns at every key point**.  So the width is the circuit's, not the
prefix's — and, reported against the unit's own interest, **"inside
the band" is in part a property of the record's ENDS**: the winner's
interior leaves the band through the top (0.8808 against 0.8000),
exactly as D60's C7 predicted for homogeneity.  The mechanism
statement is D60's, now with width attached: the shortfall from 1 is
boundary, and the wide charts survive the excision.

## 6. Instrument hygiene and forcedness

- **Anchors (W0).**  The `C = 0` WIDE-BRICK is D60's brick three ways:
  the event list is IDENTICAL to `d60_crystal_exact.brick(8, 14)`
  called in this process; the exact Fractions reproduce the published
  row (10/13, 125/192, 0, 3); the four decimals (0.7692 / 0.6510 /
  0.0000 / 3) come out unchanged.  Exit 1 was reserved for breaking
  this.
- **Single sources.**  The transport grammar by text-slice from
  d42b1 (exit-freedom of the slice and of every AST-extracted body is
  GATED, not asserted); the sky instrument (d47a), the repaired
  sprinkling generator (d55c), THE ATLAS (d58) and **D60's own
  blueprint machinery — `B`, `mint_and_spread`, `dl`, `brick`,
  `profile`** by AST extraction.  The brick this unit widens is D60's
  function object, not a re-typing of it.
- **Comparators RE-RUN (W3).**  D58's `atlas` re-run in this process
  on the same eleven genuine sprinkling configurations; the band comes
  out as D60's committed `[77/120, 4/5]` and `|D| ≥ 4` `[17/40,
  13/20]`.  No threshold in this unit is anything but one of these
  measured numbers.
- **Forcedness (W1/W1b).**  Across all 38 records (4,604 events) no
  specification ever matched more than one menu candidate and no step
  was refused.  Three records were additionally replayed with ALL
  actors offered at every step — the anchor (65 events / 8 actors,
  menus to 136), WIDE-BRICK C = 2 (121 / 10, menus to 210) and the
  winner (177 / 16, menus to 528) — every specification still matching
  exactly one candidate.  **The pin's pre-registered hard part (design
  the courier cadence so the record stays FORCED) did not bite: no
  re-specification was needed, and there is no ambiguity or refusal to
  report.**  The reason is structural and worth recording: a delivery
  is specified by its full tuple `('d', s, r, v)`, so a matching menu
  entry is unique whenever it exists, and re-delivery is admissible
  whenever the sender holds `v` — which every ring actor does after the
  spread and every courier does after its first reception.
- **Nothing was cut** for runtime; every swept range and cap is
  printed (W6).  Total wall clock ≈ 5 minutes, and the run is
  deterministic across `PYTHONHASHSEED`.
- **One declared deviation from the pin's exit protocol.**  Pin W6
  says exit 1 only on W0 anchor breakage; the receipt also exits 1 if
  W3's comparator reproduction breaks (the band must come out as
  D60's committed `[77/120, 4/5]`).  Reason: if the imported
  instrument no longer reproduces the committed band, every ordering
  in this unit is measured against something other than the committed
  comparators, which is anchor breakage in the same sense.  It is
  printed by the receipt's own exit line, not silent.

## 7. Scope, held (pin §5)

Grammar layer.  The claim is about the swept `(M, R, C, cpl)` family
and no wider; the branching bound of §4 is the only statement here
that is universal, and it is a theorem with its hypothesis (`≤ B`
registers per event) said aloud.  No measure claim — transport scope
has none (B1) — and therefore no typicality claim.  No
physical-object claim: a crystal is a MECHANISM certificate, never an
object (#440, the scale doctrine).  Transfer to the identified
interactive click law runs through paper 29's missing map (D59) and is
not claimed.  ω is a chart-size ratio along covers (D58 round-1
MAJOR 2), never a symmetric overlap.

## 8. Residues

1. **The arbitration route to width > 4.**  §4 says where the next
   width lives: events with 3+ registers, i.e. conflicts resolved by
   arbitration.  Whether a record can carry them *at tiling cadence* —
   a crystal made of conflicts rather than deliveries — is the
   successor question, and it is now sharp.
2. **Both bands at d = 2.**  No swept configuration is inside the
   homogeneity band and the `|D| ≥ 4` band simultaneously at d = 2
   (at d = 3 two are).  Whether a larger `(M, R)` reaches it is
   open; the trend (width rises with rounds, homogeneity rises faster)
   suggests it may not be reachable in this family, which would itself
   be worth proving.
3. **The `cpl = 1` dip** is unexplained beyond "partial coupling
   breaks height regularity"; a height-layer census would decide it.
4. **Size.**  The records run to 217 events; the sprinkling
   comparators are 120-point sets.  D60's size residue is inherited,
   and the receipt's cost grows steeply (the winner's full-menu
   replay is 88 s).
5. **The cocycle unit's substrate is named** (§1's witness).  What it
   still lacks is a non-identity transition between overlapping wide
   charts — D58's containment theorem says ω-overlaps are nested, so
   the cocycle unit must find its non-identity elsewhere than in the
   `ω` pairs.
