# D58 — result: THE ATLAS GAP IS REAL. The homogeneity leg survives; the overlap leg is a chart-size ratio and its flagged finding REVERSES.

**Status:** ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.  Round 1 was
an independent Opus 5 hostile batch review, frozen at
`v10/reviews/batch-round1-d50-to-d60.md` — for D58, REVISE, 1
BLOCKER / 2 MAJOR / 5 MINOR / 3 NIT.  The reviewer rebuilt the entire
atlas (own poset closure, heights, SKY-B, cover enumeration, overlap)
and **reproduced every committed number exactly**, including the
committed Fractions `73489/613800` and `1022991/1895092`.  What did
not survive is the M³⁺¹ control and the description of what ω is.
Repairs applied; this note is one of them (round-1 MINOR 5: D58
shipped as pin + receipt + LOG, and D60 cited its numbers from
there).  Pin `note-d58-atlas-instrument-pin.md` (LOG #438, committed
before code).  Receipt: `v10/code/d58_atlas_instrument_exact.py`
(8 PASS / 0 FAIL, exit 0), output under `v10/data/`.  An independent
hostile round is required before anything here is citable.

## 1. A2 — the durable content: the atlas gap

> **Against the CORRECTED sprinkling family — eleven genuine
> configurations, homogeneity band [0.6417, 0.8000] — the grammar's
> engineered shatter records sit at 0.357–0.386 and the generic
> 2-actor walk at 0.067.  The pre-registered conclusion holds: the
> grammar's shatter records are the OPPOSITE of atlases.**

This is the unit's durable content and round 1 confirms it survives
every correction in the round.  Round-1 MINOR 3: the committed A2
gated `all(k in R for k in ('SH4','SH5','WALK'))` — true by
construction three lines after the assignments — with the actual
comparison living in the detail string.  The comparison is now the
predicate.  Round-1 MINOR 4: the "sprinkling homogeneity floor 0.64"
was a two-point floor over two records, one of them invalid; it is
now a measured BAND over eleven.

## 2. A1 — the M³⁺¹ control was not a sprinkling, and the flagged finding REVERSES

Round-1 BLOCKER 1.  `latt4` drew each coordinate as `s % box` from an
LCG mod 2³¹.  The low `k` bits of that LCG have period `2^k`, and
each point consumes four draws, so a coordinate slot's low-`k`-bit
subsequence has period `2^{k−2}`.  **At `box = 32` — the committed
control — the "sprinkling" is 32 distinct spacetime locations wearing
120 labels**, eight spatial values per axis, ~3.75 mutually
incomparable coincident events per location, max poset height 4.
(At *every* box the committed generator samples a spacing-4
sublattice, so no box gave a free sprinkling.)

The generator is repaired in `d55c` (high-bit draw) and
single-sourced from there; the defective one is kept as
`latt4_committed` so the degeneracy is **exhibited**, not asserted:

```
  committed (120, 32, 8): distinct points =  32/120, distinct x-values =  8
  repaired  (120, 32, 8): distinct points = 120/120, distinct x-values = 31
```

The chart statistics were correspondingly deformed — mean chart width
**15.02** against 3.3–6.4 for genuine records, max 31 against 10–17 —
and the flagged finding candidate reverses:

| record | homog (d=2) | \|D\|≥4 | mean \|D\| | max | mean ω | pairs |
|---|---|---|---|---|---|---|
| M21 N=120 box=60 (committed) | 0.6417 | 0.4250 | 3.26 | 11 | **0.1197** | 465 |
| M31 box=32 **[DEGENERATE]** | 0.7333 | 0.4750 | 15.02 | 31 | **0.5398** | 2108 |
| M31 genuine, boxes 20–90 | 0.683–0.767 | 0.500–0.650 | 4.3–6.4 | 14–17 | **0.048–0.100** | 700–800 |

> **The M21-vs-M31 overlap difference is real, it is in the OPPOSITE
> direction from the one flagged, and it is NOT density-confounded.
> The residue LOG #439 left open is CLOSED, with the sign flipped.**

WITHDRAWN: every M³⁺¹ number of the committed run (73% / 0.54 /
0.94), the "FINDING CANDIDATE" framing, and the density diagnosis.
What survives of A1 is the *homogeneity* validation — and it survives
better than before, on eleven configurations instead of two.

## 3. A1b — what ω IS: the containment theorem

Round-1 MAJOR 2.

> **THEOREM (of the committed SKY-B definition).**  For a cover pair
> `e ⋖ e'`: if `h[e'] − h[e] = 1` then `D_{e'}(d−1) ⊆ D_e(d)`, so
> `ω(e,e') = |D_{e'}(d−1)| / |D_e(d)|`; otherwise the two sets are
> DISJOINT and `ω = 0` identically.
>
> *Proof.* `D_e(d) = {f : e < f, h[f] = h[e]+d}` and
> `D_{e'}(d−1) = {f : e' < f, h[f] = h[e']+d−1}`.  If `h[e'] = h[e]+1`
> the height conditions coincide and `e < e' < f ⇒ e < f`; otherwise
> the height conditions are incompatible. ∎

Verified with zero violations over every cover pair of every record
measured here, and independently: the Jaccard index `|A∩B|/|A∪B|`
equals ω to the last Fraction on all of them, which is only possible
under containment.

Consequences, both against the pin's framing: there is **no two-way
overlap anywhere in the instrument** — the intersection is always the
whole successor chart — so "the transition is the identity on their
intersection" and "the cocycle question becomes real once
non-identity transitions exist" have nothing to act on.  ω is a
**chart-size ratio along covers**, and it systematically favours
**thin-charted** records.  That is exactly the asymmetry between D60's
brick and the sprinklings, and D60's reading of its 0.651 must carry it.

## 4. A1c — the height-gap census: the pin's premise is false

Round-1 MAJOR 1.  Pin §2 asserted that for a cover pair the two chart
sets "live at the SAME height layer".  They do iff the height gap is
1, which a cover does not guarantee (a cover's height can jump if it
has a taller incomparable predecessor):

```
  M21 N=120 box=60, d=2: gaps {1:180, 2:173, 3:69, 4:35, 5:7, 6:1}
                         285 of 465 measured pairs (61%) are STRUCTURAL ZEROS
  M31 box=40 (genuine) : structural-zero share 0.627
```

So the reported ω is largely a measurement of **how chain-like the
poset is**, not of how much charts overlap.  Both the unconditioned
and the gap-1-conditioned statistic are now reported for every
record — and conditioned on gap 1 the M21-vs-M31 ordering shows the
**same reversal by an independent route**: M21 0.3093 against genuine
M³⁺¹ 0.170–0.253.

## 5. A3/A4 — reporting hygiene

- **A3** is labelled a REPORTING gate (it always was in the committed
  receipt — the right house style) and every mean now carries the
  population it is a mean over (round-1 MINOR 2).  The generic walk's
  `ω = 1.00`, the highest value in the whole table, rests on **two
  pairs**; LOG #439 did not say so.
- **A4** is new (round-1 MINOR 1): the `|D| ≥ 4` column was computed
  at every record and never compared.  Genuine sprinklings carry
  4-direction charts at 42–65% of events and reach max `|D|` of
  10–17; the engineered records and the generic walk carry none, and
  neither does D60's brick at d = 2.  **It is the column that
  qualifies D60's verdict, and it was one line away in this unit.**
- Every reported figure carries its exact Fraction (round-1 NIT 1/NIT
  2: `2/30` was reported as "6%", "0.07" and `7/100` in three places,
  and `100*w2//n` floor-rounded `77/120` to "64%", which became D60's
  hard-coded comparator in the direction that made it easier to
  clear).  D60 now imports the comparators by re-running this file's
  `atlas`, so nothing is re-typed.

## 6. Scope, held

Charts = SKY-B(d) direction sets, `d ∈ {2, 3}`.  Sprinkled records at
exact integer coordinates, one seed per configuration; no typicality
claim.  Homogeneity is validated on controls; overlap is REPORTED,
never thresholded (the A1 self-correction that withdrew a hard-pinned
1/3 floor as an invented constant is what kept BLOCKER 1's damage
bounded, and it is not counted against the unit).

## 7. Residues

1. The overlap population is conditioned on the SOURCE chart only
   (`len(DIRS[e]) < 2: continue` never filters `e'`) — a
   self-selected subpopulation, now annotated but not removed.
2. Whether any grammar record can reach sprinkling-grade chart WIDTH
   (A4's column) — the sharp question D60 inherits.
3. The atlas/cocycle language beyond ω: with containment there is no
   non-trivial transition to study at this definition, so a genuine
   cocycle question needs a *different* chart notion, not a deeper `d`.
