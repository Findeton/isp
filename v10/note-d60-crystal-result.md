# D60 — result: THE GRAMMAR TILES. The crystal is admissible, forced, and sprinkling-grade on homogeneity and overlap — with THIN charts.

**Status:** ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.  Round 1 was
an independent Opus 5 hostile batch review of seven units, frozen at
`v10/reviews/batch-round1-d50-to-d60.md` — for D60, REVISE, 0
BLOCKER / 3 MAJOR / 5 MINOR / 3 NIT.  **The object survived
completely**: the brick record was rebuilt from the pin with an
independent driver, re-run with all eight actors offered at every one
of the 65 steps, and every specification matched exactly one menu
entry — the record is FORCED.  The findings hit what the numbers were
compared to, what they are a function of, and which metric was
chosen.  Repairs applied; this note is one of them (round-1 MINOR 5:
D60 shipped as pin + receipt + LOG, with the verdict living only in a
`print()` block).  Pin `note-d60-crystal-question-pin.md` (LOG #447,
committed before code).  Receipt: `v10/code/d60_crystal_exact.py`
(10 PASS / 0 FAIL, exit 0), output under `v10/data/`.  An independent
hostile round is required before anything here is citable.

## 1. C1/C2 — the object

> **CRYSTAL-1D (the brick wall): 65 events over 8 ring actors, 14
> rounds of alternating re-deliveries, every event offered by the
> layer's own menu, and every specification matched by EXACTLY ONE
> candidate — the record is FORCED, nothing was tie-broken.**
> **CRYSTAL-2D (the grid): 46 events over 9 actors, 12 phases, no
> refusal.**

The pre-registered lean (admissibility YES, strong) held.  Round 1
re-derived the blueprint independently and reproduced the poset
(1,830 ordered pairs), the heights, the covers and every atlas
number.  Reported per round-1 NIT 3: at `K = 3` the grid's phase
generator degenerates — `range(0, K-1, 2)` and `range(1, K-1, 2)`
each yield a single index, so the 12 phases reduce to **4 distinct
pair sets** of 3 deliveries each.  The grid is a smaller object than
"3×3, 46 events" suggests, which reinforces the unit's own "size is
the named residue".

## 2. C3/C4/C5 — the atlas verdict, RESTATED

The committed LOG said "homogeneity 77% — ABOVE the sprinkling floor
(64%, M21) and above M31's 73%; mean overlap 0.65 — above BOTH
sprinkling comparators (0.12 / 0.54)".  Both M31 comparators came
from D58's degenerate control (32 distinct points wearing 120
labels — D58's round-1 BLOCKER 1).  The comparators are now
**recomputed with D58's own repaired instrument** on eleven genuine
sprinkling configurations rather than re-typed from a floor-rounded
printout (round-1 MINOR 1):

| | homogeneity (d = 2) | mean ω (d = 2) | \|D\| ≥ 4 | max \|D\| |
|---|---|---|---|---|
| brick m = 8 (65 events) | **0.7692** | **0.6510** | **0.0000** | **3** |
| grid 3×3 (46 events) | 0.5000 | 0.3915 | 0.0000 | 3 |
| genuine sprinklings (11 configs) | 0.6417 – 0.8000 | 0.0481 – 0.1329 | 0.425 – 0.650 | 10 – 17 |
| engineered shatter records | 0.357 – 0.386 | 0.467 – 0.473 | 0.000 | 3 |
| generic 2-actor walk | 0.0667 | 1.0000 (2 pairs) | 0.000 | 2 |

Three separate corrections land here.

- **The overlap claim STRENGTHENS** (MAJOR 1): 0.651 against
  0.048–0.133, not against 0.54.  Good news from a corrected
  comparator.
- **The homogeneity claim does NOT** (MAJOR 1): "above M31's 73%" was
  a claim against a non-sprinkling.  Against genuine M³⁺¹ the brick's
  0.769 sits **inside** the band and below the box-48 configuration.
  The licensed statement is the one pin §3 actually pre-registered —
  *comparable to the sprinkling band* — and the committed LOG
  overstated its own pin.
- **"Sprinkling-grade on both metrics" is not "sprinkling-grade"**
  (MAJOR 3).  On a third, equally natural metric — chart WIDTH, the
  thing `|D| ≥ 2` is a threshold of — the brick is at the floor at
  d = 2: **no 4-direction chart anywhere, at any parameter setting
  tried**, against the sprinklings' 42–65%.  D58 computed that column
  at every record and never printed it (its round-1 MINOR 1); it is
  printed on both sides now.  Reported whichever way it lands: at
  d = 3 the brick does reach `|D| ≥ 4` (38/65), inside the d = 3
  sprinkling band, so the width shortfall is a **d = 2** statement —
  exactly as the homogeneity ordering is (round-1 MINOR 4: at d = 3
  the brick's 0.7385 sits *below* M21's 0.7500 and the ordering
  reverses; the overlap ordering holds at both depths).

> **THE LICENSED CLAIM, CORRECTED: the grammar admits records that
> tile at sprinkling-grade HOMOGENEITY and above-sprinkling OVERLAP,
> WITH THIN CHARTS.**  A tiling-capacity MECHANISM statement at
> grammar layer, and nothing more.

D58's own round-1 MAJOR 2 qualifies the overlap leg further: ω is not
a two-way overlap but a **chart-size ratio along covers** (the
containment theorem), and it systematically favours thin-charted
records.  The brick's 0.651 must be read with that.

## 3. C6/C7 — 77% is a parameter, and the mechanism claim that replaces it

Round-1 MAJOR 2: the pin committed "**m** ring actors" and an
unspecified number of rounds; the receipt hard-coded `M = 8`,
`ROUNDS = 14`, and neither was gated.  Both are swept and printed
now:

```
  ROUNDS at M = 8 :  R=4  0.4400 | R=8  0.6341 | R=14 0.7692 | R=20 0.8315
                     R=30 0.8837 | R=50 0.9282        (|D|>=4 = 0 throughout)
  RING WIDTH at 14:  M=4  0.7879 | M=6  0.7755 | M=8  0.7692 | M=10 0.7531
                     M=12 0.7320 | M=16 0.6822        (|D|>=4 = 0 throughout)
```

Homogeneity rises without bound in rounds and falls in ring width.
**0.769 is not a property of the mechanism; it is a property of
(M = 8, R = 14).**  What the sweeps license instead is the
asymptotic statement, and C7 pins down where the shortfall lives:

```
  brick FULL          (65 ev): d=2 homog 0.7692  omega 0.6510
  brick CIRCUIT-ONLY  (56 ev): d=2 homog 0.7857  omega 0.6420
  brick PREFIX-ONLY   ( 9 ev): d=2 homog 0.6667  omega 0.7500
  brick INTERIOR      (51 ev): d=2 homog 0.9020  omega 0.6496   (d=3: 0.9216)
```

The non-lattice mint-and-spread prefix **deflates** the headline — the
circuit alone reads higher than the published figure — and dropping
the bottom two and top three height layers takes the interior to
0.902.

> **THE MECHANISM STATEMENT, which is what the scale doctrine asks
> this unit to certify: the shortfall from 1 is entirely BOUNDARY, so
> a re-delivery circuit's homogeneity tends to 1 as it runs.**
> `0.769` is a snapshot.

Round 1 also settled the fairness question the brief raised: the
brick's homogeneity is strongly size-dependent while the
sprinklings' is nearly size-independent, so the smaller record is the
handicapped one, and size-matched at N = 65 the brick still clears
`[REFEREE-CARRIED, batch round 1]`.

## 4. Instrument hygiene (round-1 MINOR 1/2/3, NIT 1)

Comparators are now imported by re-running D58's own `atlas` rather
than re-typed as two-digit decimals (one of which, `SPRINKLE_FLOOR =
64/100 < 77/120`, rounded in the unit's own favour).  The dead `WALK`
variable is read by a predicate.  The two theorem-passes — C5's
`wmax1 >= 2` and C4's `om1 is not None`, both implied by C3 having
found any 2-direction chart at all — are gone, replaced by the width
comparison and the recomputed-comparator ordering.  Every figure
carries its exact Fraction, so the receipt no longer reports the same
number as 76% and 77% five lines apart.  C8 gates that the
population-restricted profile used for the circuit/interior controls
reproduces D58's atlas exactly when the population is every event.

## 5. Scope, held

Grammar layer.  Transfer to the identified interactive click law runs
through paper 29's missing map (D59).  No typicality claim (there is
no measure at transport scope).  No dimension claim beyond the
measured `|D|` census — and that census is now the honest one, with
the width shortfall stated.  No physical-object claim (#440).

## 6. Residues

1. **Size.**  Both crystals are small; the grid is smaller than it
   looks (§1).  A larger grid at `K ≥ 5` would test the 2+1 analogue
   properly.
2. **The width ceiling.**  `max |D| = 3` at every `(M, R)` tried, at
   d = 2.  Whether ANY grammar record can carry sprinkling-grade
   chart WIDTH is now the sharp open question, and it is the one D58's
   `|D| ≥ 4` column poses.
3. **The asymptotic claim** (homogeneity → 1) is established by a
   six-point sweep and the interior control, not by a proof.
