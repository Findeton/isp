# U1b — result: **N2 — MAP-ROBUST DIVISIBILITY WITH BITE, AND THE REASON IT CANNOT BE OTHERWISE AT THE REACHABLE CLASS.** The whole kinematically admissible class of renewal-grain configuration maps is swept — 1,024 candidate maps over four ensembles, three of them carrying interval patterns or cut triples ARM-C2 never reached. The renewal payload chain is **exactly i.i.d. uniform on eight labels at every interval pattern measured**, minimal (3,3) and unequal (4,3) and unequal (3,4) alike, so ARM-C2's uniformity is not an artefact of minimal-interval conditioning and the unequal-interval half of the inherited question closes negatively: **no admissible map has bite on any cut triple that begins at the first renewal.** Shifting the cut triple one renewal past genesis makes base-retaining maps admissible for the first time, and **74 of them do have bite — and all 74 divide**, each with two exhibited interpolants verified entry by entry. The reason is measured, not assumed, and it is the load-bearing qualification on this result: the fixedness gate bounds the retained base-chain lag by (first cut's renewal index − 1), and at lag ≤ 1 the label chain carries one-step memory and **no two-step memory**, so `Gamma(cut3<-cut1)` is column-constant for **every** admissible map of **every** ensemble and DIVISIBLE is forced before any test runs. The one door left in the class is a map reading base-chain lag ≥ 2, which is fixed only on a cut triple beginning at the third renewal — depth 15 in this grammar, not enumerated here. The null points the other way and is scored through the same bite gate: **10 of 10 biting matched-size random controls REFUSE where 74 of 74 biting record maps DIVIDE.**

**Status:** GREEN-UNREVIEWED, STRICT.  Pin
`note-u1b-renewal-beables-pin.md` (frozen before this receipt existed).
Binding context: U1 TERMINAL (v11 LOG #11–#14, the delta round's
mechanism finding), paper 0 §4 (division events are the renewals) and
§9b.  Parents: ARM-C2's telescoped construction
(`v11/code/u1_indivisibility_census_exact.py`, sliced by this receipt),
`v10/code/d42b1_transport_exact.py` (the committed token structure),
D62 row R4, PORT-1/2/3, `[B3]` p.9 and eqs. 22–23.  Receipt
`v11/code/u1b_renewal_class_sweep_exact.py`, output
`v11/code/u1b_output.txt` — **36 PASS / 0 FAIL / 0 ANCHOR-FAIL, exit 0,
1,001 s wall clock, single-threaded**, exact `Fraction` arithmetic
throughout; no float appears in any substantive computation.  Committed
layers are single-sourced by text-slice with exit-freedom gated and by
AST extraction under an AST signature pass (d42b1's token structure,
D74's enumerator, and the terminal U1 receipt's own `sigmaT`,
`payload_of`, `is_R4`, exact Phase-I simplex, Farkas verification,
reduced system, `Gamma` machinery and `decide_triple` — the simplex and
its Farkas verification are lifted but **unexercised** here, §9).
Exit 1 is reserved for anchor failure.

---

## 1. The verdict

> **N2 — bite + all divide** `[MEASURED, at the declared class, ensembles
> and caps]`
>
> **The sweep.**  `1,024` candidate maps × `4` ensembles = `4,096`
> candidate cells.  The fixedness gate admits `176`; the bite gate calls
> `102` of those DEGENERATE and excludes them from every verdict row;
> `74` verdict rows remain.  **DIVISIBLE `74` / INDIVISIBLE `0`**, with
> no row left to a cap.
>
> **The unequal-interval half of the inherited question: closed
> negatively.**  At minimal intervals `(3,3)`, at unequal `(4,3)` and at
> unequal `(3,4)`, the joint law over the three renewal cuts under
> `alpha_sigma+` is **exactly uniform, `1/512` on all 512 cells** — the
> renewal payload chain is i.i.d. uniform on eight labels in every case.
> No lag-0 map acquires bite from an unequal interval, and on all three
> r1-first ensembles **every one of the 16 admissible maps is
> degenerate**.
>
> **The base-retaining half: bite exists, and everything divides.**  On
> the ensemble whose cut triple begins at the second renewal,
> base-retaining maps are admissible and `74` of `128` have a
> non-column-constant renewal transfer.  Every one divides, by **exact
> Chapman-Kolmogorov**, and each carries two interpolants exhibited and
> re-verified from scratch — the process's own conditional
> `Gamma(cut3<-cut2)` and the structural `X = Gamma(cut3<-cut1).1^T` —
> column sums exactly 1, every entry `>= 0`, equation satisfied entry by
> entry.
>
> **The qualification, stated with the result and not after it.**  The
> second transfer `Gamma(cut3<-cut1)` is column-constant for **all 176**
> admissible maps of all four ensembles.  By (D-2) of §5 that **forces**
> DIVISIBLE before any test is run.  What the sweep establishes is that
> **no map in the reachable class escapes that structure** — not that
> each row was decided against a live alternative.
>
> **The null.**  Matched-size random partitions of the same cut
> populations, two printed seeds, scored through the same bite gate:
> `10` biting control runs, **`10` REFUSE**, against `74` biting record
> maps of which **`0`** refuse.  At renewal grain, as at cut grain in
> U1 §6, the record map is far closer to divisible than noise of its own
> granularity.

**What the delta round left open, and what is left now.**  U1's ARM-C2
ran the pinned triple exhaustively and returned a test without bite, for
a reason the delta round identified exactly: `payload_of` drops the arb
token's **base**, and the base of a renewal token is the previous
renewal's token — the only object linking consecutive renewals.  U1b
does not choose a different map; it sweeps the lattice those fields
generate.  The result is that the base **can** be retained inside a
fixed label set, that retaining it **does** give the test bite, and that
the test then **does not refuse**.  The residual is named in §9 and is a
depth cap, not a structural obstruction.

## 2. The class — the field lattice, declared and swept

A candidate map assigns each renewal cut a label computed from committed
`d42b1` token fields only.  The declared generators, each cited to its
source, are:

| field | source |
|---|---|
| `state` | `sigmaT(h, AB, enriched=False)` — the D62-faithful post-renewal serialized state (u1 receipt:1154) |
| `value@l` | `tkn[2] = value_of(tkn)`, d42b1:53 and :60–62, read through `anc(tkn,l)` |
| `authors@l` | `tkn[3]`, d42b1:54 (provenance component), read through `anc(tkn,l)` |
| `init@l` | `tkn[4]`, d42b1:55 (provenance component), read through `anc(tkn,l)` |

`anc(tkn,l)` follows the committed base field `tkn[1]` `l` times; genesis
is absorbing.  Lags `0,1,2` are carried, so the field set has
`1 + 3x3 = 10` generators and **the class is all `2^10 = 1,024`
subsets**, enumerated by bitmask in a fixed order and printed in full.

**`sigma` and `sigma+` are members of the class, by exact identity.**
`[GATE F2]`  Mask 1 = `{state}` **is** `alpha_sigma`.  Mask 15 =
`{state, value@0, authors@0, init@0}` **is** `alpha_sigma+`: at a renewal
the ported state carries a single token record, so the payload-enriched
state is exactly that record with `payload_of(renewal token)` appended,
and the two maps induce the same partition of every renewal cut.
Verified on **209,200 distinct cut histories** across the four
ensembles.

**Predictive sufficiency is not an admissibility criterion and is not
used as one anywhere.**  Screening-off is the phenomenon under
measurement, not a filter.

**Two generators that are not generators, measured rather than
assumed.**

- `[GATE F0]`  The D62-faithful serialized state is the **root** at
  every renewal cut of every ensemble — one distinct state over all
  cuts, 0 non-root records.  So `state` partitions nothing here and
  `alpha_sigma` is the one-label map: ARM-C2's structural vacuity,
  now measured at three interval patterns and at a shifted cut triple.
- `[GATE F1]`  The arbitration event's `ckey` adds nothing.  Over every
  renewal cut of every leaf of all four ensembles the competing-value
  multiset, the proposer set and the number of distinct bases in the
  `ckey` take exactly **one** value each — `((0,1), (A,B), 1)`.  What the
  `ckey` carries that `payload_of` does not is the **base**, and that is
  already a generator at every lag.
- `[GATE F3]`  No merge token appears on any base chain of any ensemble:
  every chain is arbitration tokens down to genesis, so the merge branch
  of the payload record is declared and unexercised.

## 3. The four ensembles, and the exhaustiveness gates

Every ensemble is a set of leaves of the committed transport grammar
carrying renewals at declared positions, reached by the **same
telescoping ARM-C2 uses**: at horizon `D` the relative-horizon leaf
measure is `P(leaf) = prod_t q_t / G(root,D)` because `G(leaf,0) = 1`, so
the law conditioned on a set of leaves needs only those leaves' raw
weight products and the normaliser cancels.  No sampling, no truncation.

| ensemble | renewals | cut triple | cut intervals | leaves | raw mass |
|---|---|---|---|---|---|
| **E1** | 3, 6, 9 | 3, 6, 9 | (3,3) | 4,096 | `1/32768` |
| **E2** | 3, 7, 10 | 3, 7, 10 | (4,3) | 57,344 | `1/8192` |
| **E3** | 3, 6, 10 | 3, 6, 10 | (3,4) | 73,728 | `1/8192` |
| **E4** | 3, 6, 9, 12 | 6, 9, 12 | (3,3) | 65,536 | `1/1048576` |

E1 is ARM-C2 re-anchored.  E2 and E3 are the two required unequal
patterns, complementary in which leg is long.  E4 exists for a reason
declared before it is built: **the base of the first renewal's token is
the genesis version `v0`** — there is no other version at depth 3 — so
on any cut triple beginning at renewal 1 a base-reading map carries the
genesis symbol at cut 1 and a real payload at cuts 2 and 3, its label
set differs across the cuts, and it fails the fixedness gate.  E4 shifts
the cut triple one renewal forward so that every cut's base is an
arbitration token.

**The intervening structure, enumerated exhaustively.**  A renewal three
events after a renewal forces `(p,p,r)` and nothing else.  A renewal
four events after a renewal admits exactly five intervening patterns —
`(d,p,p,r)`, `(n,p,p,r)`, `(p,n,p,r)`, `(p,p,d,r)`, `(p,p,n,r)` —
each with exactly two proposals plus one delivery or one idle.  Counts
are printed per leg.

**Anchor `C2.ENS`.**  ARM-C2's ensemble reproduces exactly on machinery
rebuilt here — an unpruned scan, not the committed `_ppr`: **16 renewal-1
bases → 256 renewal-2 histories → 4,096 renewal-3 histories at depth 9,
raw mass `1/32768`**, against the committed `16 / 256 / 4,096` and
`1/32768`.  Exit 1 on mismatch.

**The exhaustiveness gates (U1-delta's m2, discharged in-receipt).**

- `[GATE X1]`  Every 3-event and every 4-event continuation of all 16
  renewal-1 bases is generated with **no prune** and only then filtered:
  **16,352** and **152,416** raw continuations scanned.  The pruned
  enumerator returns exactly the same leaf sets with exactly the same
  weights.
- `[GATE X2]`  Every 3-event continuation of all 256 renewal-2 histories
  likewise: **453,632** raw continuations scanned, `(p,p,r)` the only
  intervening pattern, 4,096 leaves, identical to the pruned result.
- `[GATE X3]`  The prune's two premises hold on **every expansion of
  every leg** — 177,664 expansions gated, **0** monotonicity violations,
  and of the **208,896** arbitrations the grammar offers anywhere in any
  leg (interior ones included, not only those the pattern accepts)
  **0** have fewer than two live proposals in the parent view.
- `[GATE X4]`  The live count the prune reads is `d42b1`'s own
  `View.live`, re-evaluated on the event list rather than by rebuilding
  a View; the re-evaluation agrees with the committed object on
  **6,912 / 6,912** expanded nodes of exactly the populations the
  unpruned scan covers.

**The declared boundary of the gate, stated plainly.**  The unpruned
scans cover leg 1 of all four ensembles and leg 2 of E1 and E4 —
**622,400 raw continuations in total**, the sum of the three counts the
receipt prints (`16,352 + 152,416 + 453,632`).  The three deeper legs (E2's
3-event leg from 3,584 renewal-2 histories, E3's 4-event leg from 256,
E4's 3-event leg from 4,096) are enumerated with the prune, whose
premises are gated on every expansion actually performed rather than on
a sample.  An unpruned scan there costs of order `5x10^6` continuations
per leg and is a declared cap, not a silent one.

`[GATE J.*]`  Each ensemble's field-record joint over the three renewal
cuts sums to exactly 1.

## 4. Admissibility — the fixedness gate, and the genesis boundary

| ensemble | class | FIXED | refused | refused by deepest lag read |
|---|---|---|---|---|
| E1 | 1,024 | 16 | 1,008 | lag 1: 112, lag 2: 896 |
| E2 | 1,024 | 16 | 1,008 | lag 1: 112, lag 2: 896 |
| E3 | 1,024 | 16 | 1,008 | lag 1: 112, lag 2: 896 |
| E4 | 1,024 | **128** | 896 | lag 2: 896 |

`[GATE A1]`  **The gate has an exact, statable content, verified against
the measured admissibility of all 1,024 maps on all four ensembles:** a
map is FIXED on an ensemble **iff every field it reads lies inside the
part of the base chain that is an arbitration token at every cut of the
triple** — lag `<= 0` when the first cut is renewal 1, lag `<= 1` when it
is renewal 2.  The obstruction is the genesis boundary and nothing else,
and **no interval pattern moves it**.

**The structural price, stated where it is measured.**  The only object
linking consecutive renewals is the base, and the base's own label set
**grows with the renewal index** — renewal `k`'s base chain is `k` tokens
long.  A map that retains the whole link therefore can never be fixed,
and the truncations that are fixed retain at most lag (first cut's
renewal index − 1).  Paper 0 §4's fixedness and unbounded cross-renewal
memory are in tension at renewal grain.  That is a fact about the
**class**, not about a chosen map.

## 5. The bite table — and the two degeneracies, separated

The delta round's B1 is made structural here, and made exact: the
round's one-line reason is the weaker half of the fact, and the class
sweep contains maps that carry one degeneracy and not the other.

> **(D-1) FIRST-TRANSFER DEGENERACY — the pin's bite gate.**  If
> `Gamma(c'<-c)` is column-constant then the middle cut is
> **independent** of the conditioning cut, so `X.Gamma(c'<-c)` is
> column-constant for every `X` and the triple divides **iff**
> `Gamma(c''<-c)` is column-constant too.  Either way the test measures
> nothing about the middle cut's role: "does the law factor through
> `c'`?" is vacuous when `c'` remembers nothing of `c`.  DEGENERATE; **no
> verdict row may cite it, in either direction**.
>
> **(D-2) SECOND-TRANSFER DEGENERACY.**  If `Gamma(c''<-c)` is
> column-constant with common column `b`, then `X[k,j] := b_k` is
> column-stochastic and `X.Gamma(c'<-c) = Gamma(c''<-c)` **exactly**,
> whatever the first transfer is.  DIVISIBLE is forced.

ARM-C2 carried both at once, which is why the delta round could quote
either.  They are separated here.

| ensemble | admissible | one-label | DEGENERATE (first transfer) | **WITH BITE** | of those, second transfer column-constant |
|---|---|---|---|---|---|
| E1 | 16 | 2 | 16 | **0** | 0 |
| E2 | 16 | 2 | 16 | **0** | 0 |
| E3 | 16 | 2 | 16 | **0** | 0 |
| E4 | 128 | 2 | 54 | **74** | 74 |

`[ANCHOR C2.DEG]`  ARM-C2's degeneracy reproduces exactly on E1 under
`alpha_sigma+`: supports `8/8/8`, the joint over the three renewal cuts
exactly uniform at `1/512` on 512 cells, `Gamma(r2<-r1)` column-constant
with exactly one distinct column.  Exit 1 on mismatch.

`[GATE A2]`  **The bite table has an exact, statable content**, verified
against every admissible map on every ensemble: the renewal transfer
bites **iff the map reads the same committed component at two
consecutive lags** — a token field and the same field of that token's
base.  Reading a component only at lag 0, or only at lag 1, or reading
two *different* components at lags 0 and 1, all leave the transfer
column-constant.  Nothing else in the lattice links consecutive renewal
cuts, at any interval pattern.

`[GATE A3]`  **The second transfer is column-constant for all 176
admissible maps of all four ensembles** — 0 exceptions.  By (D-2) this
forces DIVISIBLE on every admissible map before any test is run, and it
is the load-bearing qualification on §6.

`[GATE A4]`  **The renewal payload chain is exactly i.i.d. uniform on
eight labels at every interval pattern measured** — the `alpha_sigma+`
joint is `1/512` on 512 cells on E1, E2, E3 and E4 alike.

**`alpha_sigma` and `alpha_sigma+` on every ensemble.**  `alpha_sigma`
carries labels `[1,1,1]` and one transfer column on all four;
`alpha_sigma+` carries `[8,8,8]` and one transfer column on all four.
**Both are DEGENERATE everywhere in this unit, and no verdict cites
either.**

## 6. The census, both ways

| ens | class | FIXED | refused | 1-label | DEGEN | BITE | DIV | IND |
|---|---|---|---|---|---|---|---|---|
| E1 | 1024 | 16 | 1008 | 2 | 16 | 0 | 0 | 0 |
| E2 | 1024 | 16 | 1008 | 2 | 16 | 0 | 0 | 0 |
| E3 | 1024 | 16 | 1008 | 2 | 16 | 0 | 0 | 0 |
| E4 | 1024 | 128 | 896 | 2 | 54 | **74** | **74** | **0** |

The 74 verdict rows carry label spaces of sizes `4` (6 rows), `8` (24),
`16` (30), `32` (12) and `64` (2), and first/second transfer column
counts `2/1` (54 rows), `4/1` (18) and `8/1` (2).

- **Every row is decided by exact Chapman-Kolmogorov** — the process's
  own intermediate conditional interpolates, i.e. the renewal label
  chain is Markov at every biting map in the class.  `EXCLUDED-BY-CAP`
  is empty `[GATE V1]`.
- **`[B3]` eq. 22 is run beside the feasibility test on every row and is
  SILENT on all 74**: `Gamma(c'<-c)` is singular in every case, so there
  is no unique algebraic interpolant and the algebraic reading says
  nothing at all.  The existence reading carries the census alone
  `[GATE V2]`.  No identity-padding convention is needed anywhere in
  this unit — the fixedness gate has already put every `Gamma` on one
  label set, so this is not U1 §5.6's convention-relative comparison.
- **`[GATE V3]`  Gate A3's consequence is exhibited, not asserted:** on
  all `74/74` rows the structural interpolant
  `X = Gamma(cut3<-cut1).1^T` is built and re-verified from scratch —
  column sums exactly 1, every entry `>= 0`, `X.Gamma(cut2<-cut1) =
  Gamma(cut3<-cut1)` entry by entry.  Every divisibility here therefore
  has **two** exhibited interpolants, and the second would have existed
  whatever the first transfer had been.

## 7. The null

Same ensembles, same cuts, same instrument; the distinct cut histories
at each renewal cut are dealt into classes with **exactly the reference
map's class sizes at that cut** by the printed congruential shuffle
`x <- (1103515245 x + 12345) mod 2147483648`, seeds `(20260728, 11)`,
Fisher–Yates over the `sk()`-sorted cut-history list.  No random module,
no clock, no hash-seed dependence.  References: `alpha_sigma+` on every
ensemble, plus a biting map on E4 inside the declared class cap.

**Result, scored through the same bite gate `[GATE NUL.1]`:** `10`
control runs, **all 10 with bite** (none degenerate, so none is
excluded), **all 10 INDIVISIBLE**.  Against them, `74` biting record
maps of which `0` refuse.

**Every control refusal carries its certificate, in the strongest form
available.**  On each of the ten runs `Gamma(c'<-c)` is square and
**invertible** — the determinant is printed — so `[B3]` eq. 22's
algebraic interpolant `Gammabar = Gamma(c''<-c).Gamma(c'<-c)^-1` is the
**unique** candidate, and it carries **1, 12, 17, 21, 23, 27, 28, 29, 96
and 115 negative entries** respectively, with column sums all exactly 1
and the most-negative entries printed as exact `Fraction`s.  No Farkas
vector is needed: a unique candidate that fails positivity refutes
existence outright, which is a stronger refutation than separating a
cone, not a weaker one.

**The comparison is the point.**  A random partition of the same cut
populations at the same granularity refuses on every run; the record map
divides on every run.  This is the direction U1 §6's battery found at
cut grain, reproduced at renewal grain, and it is the reason no bridge
is claimed here: indivisibility at these grains is what coarse-graining
a divisible chain generically produces, and the record map does **not**
produce it.

## 8. The map-dependence structure

- **Fixedness** is moved by exactly one thing: the deepest base-chain lag
  the map reads, against the renewal index of the ensemble's first cut.
  No other field combination refuses, and no interval pattern changes it
  (`A1`).
- **Bite** is moved by exactly one thing: whether some committed
  component is read at two consecutive lags (`A2`).  The fields whose
  addition or removal flips the bite gate somewhere are exactly the six
  payload fields at lags 0 and 1, and only on E4.
- **The verdict** is moved by **nothing** in this class: no single-field
  addition or removal flips a verdict anywhere, on any ensemble.  There
  is no selection problem to pose at this class — outcome N4 is not
  met, and the reason it is not met is `A3`, not a coincidence of the
  sample.

## 9. What this does and does not say

- **It does not claim the record law is divisible at renewal grain in
  general.**  It claims that on the four declared ensembles, over the
  whole fixed class the committed fields generate, every biting map
  divides, and that this is forced by a measured structural fact (`A3`)
  rather than discovered row by row.
- **The residual is named exactly.**  A class member reading base-chain
  lag `>= 2` is fixed only on a cut triple beginning at the **third**
  renewal — depth 15 in this grammar — which this receipt does not
  enumerate.  That is the only door left in the class, and it is a depth
  cap, not a structural obstruction.  A lag-2 map is precisely what
  could give `Gamma(cut3<-cut1)` a non-constant column, because two cuts
  two renewals apart read overlapping blocks of the payload sequence
  only from lag 2 onward.
- **It is not a CP-divisibility test.**  No completely positive map and
  no CP criterion appears anywhere.  CP-divisibility and
  Barandes-indivisibility are orthogonal axes and this unit does not
  cross them.
- **No Bell or locality claim** is made or implied.
- **Indivisibility is not treated as a quantum signature.**  `[B3]`'s
  criterion is unistochasticity, and §7 measures again why: a random
  coarse-graining of the same granularity refuses where the record map
  divides.
- **No exact covariance is claimed**, per L-1: the renewal-grain label
  sets swept here are fixed finite sets, which is exactly the hypothesis
  of the finite-stochastic Lorentz no-go.  At most statistical Lorentz
  invariance is available at that grain and this unit claims none.
- **No certificate is claimed that was not produced** `[GATE NUL.2]`.
  The instrument census is printed: **74 record-map rows by exact
  Chapman-Kolmogorov, 10 control rows by the eq. 22 algebraic reading,
  and 0 exact-simplex systems solved anywhere in this receipt.**  Every
  row is decided strictly earlier in the decision order than the
  feasibility LP; the exact Phase-I simplex and its Farkas verification
  are lifted, available and **unexercised** here, and no Farkas vector
  is reported anywhere.

## 10. Scope

Transport scope (`d42b1`) only; the two-actor pool only; the four
declared ensembles and no others — renewals at 3/6/9, 3/7/10, 3/6/10 and
3/6/9/12, with cut triples at depths (3,6,9), (3,7,10), (3,6,10) and
(6,9,12).  The field lattice reads the base chain to lag 2 and the class
is its 1,024 subsets; **lag `>= 2` is admissible on no reachable cut
triple** and is a declared cap.  Exact LP caps 700 variables / 400
constraints on the full system and 5,000 / 1,200 on the reduced one
(unexercised, §9); the eq. 22 inversion runs to 64 labels; a null
reference map carries at most 16 classes; certificate prints are digests
capped at 24 non-zero entries, with the verification on the full vector.
The unpruned exhaustiveness scan covers 16 depth-3 bases at `L=3` and
`L=4` and 256 depth-6 renewal histories at `L=3`; the three deeper legs
carry the gated prune (§3).  Renewal grain per paper 0 §4's `[POSIT]`;
no claim about non-renewal division-event candidates.  No
unistochasticity claim — that is U3's.  No measure-existence claim, no
infinite-volume claim, no CP, Bell, locality or covariance claim.

## 11. Handover

- **To paper 0 §9b and the Phase II board:** U1b does **not** reverse
  the enrichment fork.  The record-grain question is answered at the
  reachable class — divisible, map-robustly, wherever the test bites —
  and the residual is a single named computation at depth 15.  Paper 0's
  line that U1b "carries the WHOLE pinned question" is discharged for
  the unequal-interval half outright (`A4`) and for the base-retaining
  half up to base-chain lag 1.
- **To U2 (the J-conjecture):** the geography U1 handed still stands
  untouched by this unit, and U1b adds one constraint on any weld: at
  renewal grain there is **no** indivisibility to locate — the 74 biting
  rows all divide, and the only indivisibility this unit produces is the
  null's.  A weld that predicts renewal-grain indivisibility at lag
  `<= 1` is already refuted.
- **To U4 (sparse records on the crystals):** the renewal sublattice's
  label sets are fixed finite sets at every reachable cut triple, with
  the exact fixedness rule of `A1`; the renewal payload chain is i.i.d.
  uniform on eight labels at three distinct interval patterns, which is
  the statistical input any Lorentz-statistics test of the renewal
  sublattice will need.
- **The one open computation, stated so it can be picked up as written:**
  build the ensemble with five renewals at 3/6/9/12/15, take the cut
  triple `(r3, r4, r5)`, and sweep the lag-`<= 2` sublattice.  That is
  the smallest ensemble on which a map with a non-column-constant
  **second** transfer is admissible, and therefore the smallest on which
  the interpolant test at renewal grain can refuse at all.
