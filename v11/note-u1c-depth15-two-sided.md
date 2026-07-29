# U1c — result: **THE TWO-SIDED TEST EXISTS AT DEPTH 15, AND EVERY GENUINE VERDICT ROW DIVIDES — outcome N2-AT-DEPTH-15.** The forcing that closed U1b is broken: on the cut triple `(r3, r4, r5)` at depths `(9, 12, 15)`, `235` of the `512` lag-`<=2` masks have a non-column-constant SECOND transfer as well as a non-column-constant first one, which no ensemble below depth 15 can produce. The engraved predicate — `(D-1)` AND `(D-2)` AND FACTOR-WISE — admits `7` of those `235` as verdict rows, and **all `7` DIVIDE by exact Chapman-Kolmogorov**, each exhibiting the process's own conditional as an interpolant and re-verifying it entry by entry. The kernel hypothesis the depth-15 prediction rested on is no longer conditional: the renewal-5 leg kernel is exactly uniform `1/8` on the eight payloads conditionally on **every one of the 65,536 renewal-4 parents**, so the renewal payload chain is i.i.d. uniform on eight labels through five renewals. The classification reproduces the recorded prediction **to the digit — `1 / 152 / 63 / 61 / 127 / 108`, every delta `+0`, the 108 refusals included, each with a collision certificate verified atom by atom and a Farkas vector verified by the committed `farkas_ok`** — but the prediction's headline does not survive its own warning: **all 108 refusals are COMPOUND-DEGENERATE**, every one carrying a factor read at lags 0 and 2 but not 1 whose own first transfer is column-constant. The refusal set has an exact content: a two-sided row refuses **iff** some committed component is read at lags 0 and 2 and not at lag 1. And the fair null is the news in the other direction: **at a factor-wise reference the record divides while the record's own outer cuts with a randomised middle cut REFUSE at both printed seeds** — U1b's fair null divided because divisibility was forced there; at depth 15 the forcing is gone, the interpolant test discriminates, and it is the record's own middle-cut labelling that carries the division.

**Status:** GREEN-UNREVIEWED, STRICT.  Pin
`note-u1c-depth15-two-sided-pin.md` (frozen before this receipt existed).
Binding context: U1b TERMINAL (v11 LOG #20–#21), paper 0 §4 (division
events are the renewals) and §9b.  Parents: the U1b receipt
`v11/code/u1b_renewal_class_sweep_exact.py` (ensembles, prune, fixedness,
kernel machinery, mask classification — re-used as committed text),
`v10/code/d42b1_transport_exact.py` (the committed token structure and
grammar), the TERMINAL U1 receipt
`v11/code/u1_indivisibility_census_exact.py` (`sigmaT`, `payload_of`,
`is_R4`, the exact Phase-I simplex with Farkas verification, the reduced
system, the `Gamma` machinery, `decide_triple`),
`v10/code/d74_transport_holonomy_exact.py` (the enumerator), D62 row R4,
`[B3]` p.9 and eqs. 22–23.  Receipt `v11/code/u1c_depth15_exact.py`,
output `v11/code/u1c_output.txt` — **45 PASS / 0 FAIL / 0 ANCHOR-FAIL,
exit 0, 4,405 s wall clock, single-threaded**, exact `Fraction`
arithmetic throughout; no float appears in any substantive computation.
Committed layers are single-sourced by AST signature pass, by text slice
with exit-freedom gated, and by AST extraction.  Exit 1 is reserved for
anchor failure.

---

## 1. The verdict

> **N2-AT-DEPTH-15 — the record law DIVIDES at every genuine two-sided
> row of the first depth at which the question is askable**
> `[MEASURED, at the declared ensemble, class and caps]`
>
> **The ensemble.**  Renewals at `3/6/9/12/15`, minimal intervals, cut
> triple at depths `(9, 12, 15)` = renewals 3, 4, 5.  `65,536` renewal-4
> parents are continued to **`1,048,576` renewal-5 leaves, enumerated
> EXACTLY and streamed — no sampling anywhere in the ensemble**.  Every
> leaf weight is `1/35184372088832`; the raw mass is `1/33554432`; the
> only intervening pattern anywhere in the leg is `(p,p,r)`; the
> field-record joint over the three cuts sums to exactly `1`
> `[GATE J1]`.
>
> **The kernel gate, which runs first and is exhaustive.**  The
> conditional law of the renewal-5 token's payload given the renewal-4
> parent history is exactly uniform `1/8` on eight payloads for
> **`65,536` of `65,536` parents, 0 deviations** `[GATE K1]`.  The
> depth-15 prediction was conditional on this; it is now measured.
>
> **The class.**  All `512` lag-`<=2` payload masks (`1,024` with the
> `state` bit, which is gated INERT mask by mask, `[GATE F0b]`).  The
> fixedness gate admits **`1,024/1,024`**: on a cut triple beginning at
> the third renewal every field the lattice offers lies inside the part
> of the base chain that is an arbitration token at every cut, so the
> genesis boundary that bounded U1b to lag `<= 1` is cleared
> `[GATE A1]`.
>
> **The classification.**  `1` one-label; `152` forced-divisible
> (`(D-2)` degenerate, `(D-1)` biting); `63` doubly degenerate; `61`
> forced-indivisible (`(D-1)` degenerate, `(D-2)` biting — evidence of
> nothing); **`235` TWO-SIDED**.  Of the two-sided masks, **`7` are
> FACTOR-WISE** — every component the mask reads is read at all three
> lags — and **`228` are COMPOUND-DEGENERATE**.
>
> **The test.**  On the `7` verdict rows: **DIVISIBLE `7` /
> INDIVISIBLE `0`**, every one decided by exact Chapman-Kolmogorov,
> every one exhibiting the process's own conditional
> `N = Gamma(r5<-r4)` and re-verifying it from scratch — column sums
> exactly `1`, every entry `>= 0`, `N.Gamma(r4<-r3) = Gamma(r5<-r3)`
> entry by entry `[GATE V2]`.  On the `228` compound-degenerate rows:
> `120` DIVISIBLE, `108` INDIVISIBLE, and **every one of the 108
> refusals carries BOTH certificates and both verify** — the collision
> certificate checked atom by atom and a Farkas vector for the
> obstructed target's row system verified by the committed `farkas_ok`
> `[GATE V3]`.  `EXCLUDED-BY-CAP` is empty `[GATE V1]`; `0`
> exact-simplex systems are solved anywhere in this receipt.
>
> **Predicted vs measured.**  The recorded depth-15 prediction is
> reproduced **exactly**: one-label `1`, forced-divisible `152`, doubly
> degenerate `63`, forced-indivisible `61`, two-sided DIVISIBLE `127`,
> two-sided INDIVISIBLE `108` — **every delta `+0`**.  What the
> prediction's numbers do not carry is its headline.  The `108`
> refusals are real refusals of the law at their label sets, and not
> one of them is a verdict row: every one carries a GAP factor whose
> own first transfer is column-constant `[GATE G3]`.
>
> **The fair null, and the surprise it delivers.**  The record's outer
> cut labels are kept and the middle cut is fully randomised into
> classes of the reference map's own sizes, by the printed congruential
> shuffle at two printed seeds.  Of `6` runs, `2` are themselves
> `(D-2)`-degenerate and carry no evidence; the other **`4` are
> two-sided and all `4` REFUSE**, including both seeds at a FACTOR-WISE
> reference where the record map divides `[GATE NUL.1]`.  Each refusal
> carries the strongest certificate available: `Gamma(r4<-r3)` is square
> and invertible, so eq. 22's algebraic interpolant is the UNIQUE
> candidate, and it carries `32`, `32`, `128` and `120` exact negative
> entries.

## 2. The ensemble, and the exhaustiveness gates

Every ensemble here is a set of leaves of the committed transport grammar
carrying pair-arbitrations at declared depths and nowhere else, reached by
the telescoping ARM-C2 uses: at horizon `D` the relative-horizon leaf
measure is `P(leaf) = prod_t q_t / G(root, D)` because `G(leaf,0) = 1`, so
the law conditioned on a set of leaves needs only those leaves' raw weight
products and the normaliser cancels.

| leg | parents | leaves | gate |
|---|---|---|---|
| renewal 2 | 16 | 256 | unpruned scan IN FULL, 16,352 raw continuations `[X1]` |
| renewal 3 | 256 | 4,096 | unpruned scan IN FULL, 453,632 raw continuations `[X2]` |
| renewal 4 | 4,096 | 65,536 | declared stride sample, 49 parents, 138,082 raw continuations `[X3]` |
| renewal 5 | 65,536 | **1,048,576** | declared stride sample, 25 parents, 105,200 raw continuations `[X5]` |

The stride is deterministic and printed, and always includes the first and
last parent, so the realised sample counts are 49 and 25 against the
declared 48 and 24.

`(p,p,r)` is the only intervening pattern at every leg, exhaustively.
The pruned enumerator returns exactly the same leaf sets with exactly the
same weights as the unpruned scan wherever the two are run side by side.

**The prune's premises and the live-count identity are asserted at EVERY
expansion of EVERY leg, the 10⁶-leaf leg included** `[GATE X4, GATE X6]`:
over **1,035,092** expansions, `0` monotonicity violations, and of the
**1,264,192** arbitrations the grammar offers anywhere — interior ones
included, not only those the pattern accepts — `0` have fewer than two
live proposals in the parent's full view; the carried live count agrees
with d42b1's own `View.live` on **1,035,092 / 1,035,092** expanded nodes.

`[ANCHOR SRC.6]`  The prune's second premise is **provable from the
committed source**, not merely gated: `candidates_for` builds every `r`
candidate's ckey as `triples(full, S)` for a SUBSET `S` of `full.live`
sharing one base — the five clauses are located verbatim — so an R4, a
ckey with two distinct proposers, needs `|S| >= 2`.  The zero-violation
count is a tripwire on top of the proof.

**The declared boundary.**  A full unpruned scan of the renewal-4 leg
costs of order `10^7` continuations and of the renewal-5 leg of order
`10^8`; both are DECLARED caps and are covered by the stride samples above
plus the per-expansion premise gates.

## 3. The committed anchors

Every one is exit-1.

- `[ANCHOR C2.ENS]`  ARM-C2's ensemble reproduces on machinery rebuilt
  here by an unpruned scan: **16 renewal-1 bases → 256 renewal-2
  histories → 4,096 renewal-3 histories at depth 9, raw mass `1/32768`**.
- `[ANCHOR U1b.A4]`  The committed kernel fact reproduces at renewals 2
  and 3: the leg kernel is uniform `1/8` conditionally on **all 16** and
  **all 256** parents, `0` deviations.
- `[ANCHOR U1b.A4b]`  And at renewal 4: uniform on **all 4,096**
  renewal-3 parents, `0` deviations; **65,536** renewal-4 leaves.
- `[ANCHOR U1b.CENSUS]`  The committed U1b four-ensemble census
  reproduces exactly — `1,024` maps × `4` ensembles, **`176` admissible,
  `102` degenerate by the `(D-1)` gate, `74` biting**, with E4 alone
  carrying `128 / 54 / 74` and E1, E2, E3 carrying `16 / 16 / 0` each.
- `[ANCHOR SRC.1–SRC.5]`  AST signature pass on the three committed
  sources; exit-freedom of the d42b1 slice; D74's enumerator and the U1
  receipt's machinery lifted by `ast.FunctionDef`; the six U1b clauses
  this receipt re-uses located verbatim in the committed U1b text.

## 4. The kernel-uniformity gate at renewal 5

`[GATE K1]`  For **every one of the 65,536 renewal-4 parents** the
conditional law of the renewal-5 token's payload is exactly uniform `1/8`
on eight payloads.  `0` deviations.

This is the hypothesis the depth-15 prediction was explicitly conditional
on, and it is the one place where the unit could have broken: failure is
outcome MODEL-BREAK and voids the classification.  It does not fail.  With
`[ANCHOR U1b.A4]` and `[ANCHOR U1b.A4b]` the chain rule now makes the
renewal payload chain **i.i.d. uniform on eight labels through five
renewals**, and the eight payloads are printed in full — the arbitration
record `('arb', value, authors, init)` with `value in {(0,), (1,)}`,
`authors in {('A',), ('B',)}`, `init in {'A', 'B'}`.

Two further structural gates hold on the whole depth-15 ensemble.
`[GATE F0]` the D62-faithful serialized state is the root at every cut of
all `1,048,576` leaves, so `state` partitions nothing and the state bit is
inert.  `[GATE F3]` no merge token appears on any base chain, so the merge
branch of the payload record is declared and unexercised.  `[GATE F4]`
exactly eight payloads occur and no genesis symbol reaches lag 2 at any
cut of this triple — which is precisely why depth 15 is the first
admissible depth for a lag-2 map.

## 5. What depth 15 changes

`[GATE A1]`  U1b's exact fixedness rule — a map is FIXED iff the deepest
base-chain lag it reads is at most the first cut's renewal index minus one
— predicts that on a cut triple beginning at the **third** renewal the
whole lag-`<=2` class is admissible.  Measured: **`1,024/1,024` FIXED, `0`
refused.**  Below depth 15 the genesis boundary truncated the retained lag
at 1, and at lag `<= 1` the second transfer is column-constant for every
admissible map, so `(D-2)` forced DIVISIBLE before any test ran.  That is
what U1b measured and it is what depth 15 removes.

The three degeneracies, separated:

> **(D-1) FIRST-TRANSFER DEGENERACY.**  If `Gamma(r4<-r3)` is
> column-constant, the middle cut is independent of the conditioning cut,
> so `X.Gamma(r4<-r3)` is column-constant for every `X`: "does the law
> factor through `r4`?" is vacuous.  No verdict row may cite such a map,
> in either direction.
>
> **(D-2) SECOND-TRANSFER DEGENERACY.**  If `Gamma(r5<-r3)` is
> column-constant with common column `b`, then `X[k,j] := b_k` is
> column-stochastic and solves the equation exactly whatever the first
> transfer is.  DIVISIBLE is FORCED.
>
> **FACTOR-WISE.**  The label of a map is the tuple of its selected
> components, so the map factorises over the three committed payload
> components, each read at its own lag set.  A map whose bite is supplied
> by ONE factor while another factor is degenerate carries the same
> compound degeneracy one level up: it is COMPOUND-DEGENERATE, is counted,
> and may carry no verdict.

`[GATE G2]`  The factor-wise predicate has an exact, statable content,
verified against every mask of the class: **a mask is factor-wise iff
every component it reads at all is read at ALL THREE lags.**

## 6. The per-factor table, measured

Each committed payload component read at a lag set is itself a member of
the class, so its own two transfers are measured rather than argued.  The
table is identical for `value`, `authors` and `init`.

| lag set | labels | first transfer | second transfer | type |
|---|---|---|---|---|
| `{0}`, `{1}`, `{2}` | 2 | DEGENERATE | DEGENERATE | N |
| `{0,1}` | 4 | BITES | DEGENERATE | D1 |
| `{1,2}` | 4 | BITES | DEGENERATE | D1 |
| **`{0,2}`** | 4 | **DEGENERATE** | **BITES** | **D2 — the GAP** |
| `{0,1,2}` | 8 | BITES | BITES | B |

The rule the table states: **a factor's first transfer bites iff its lag
set contains two CONSECUTIVE lags; its second transfer bites iff its lag
set contains two lags differing by 2.**  Inside lags `0..2` the only lag
set meeting both is `{0,1,2}`, and reading a component at all three lags
puts the intervening renewal's symbol into the middle cut's label — which
is exactly the condition under which the label chain is Markov.

## 7. The classification: predicted vs measured

| class | predicted | measured | delta |
|---|---|---|---|
| one-label | 1 | **1** | `+0` |
| forced-divisible (`(D-2)` degenerate) | 152 | **152** | `+0` |
| doubly degenerate | 63 | **63** | `+0` |
| forced-indivisible (`(D-1)` degenerate) | 61 | **61** | `+0` |
| two-sided DIVISIBLE | 127 | **127** | `+0` |
| two-sided INDIVISIBLE | 108 | **108** | `+0` |

The prediction is model-computed and is not an anchor; it is reproduced
here by exhaustive enumeration of the grammar, and every number agrees.
What the table does not settle is which rows may carry a verdict, and that
is where the prediction's headline and this receipt part:

| class | masks | DIVISIBLE | INDIVISIBLE |
|---|---|---|---|
| one-label | 1 | — | — |
| doubly degenerate | 63 | — | — |
| forced-divisible | 152 | — | — |
| forced-indivisible | 61 | — | — |
| two-sided COMPOUND-DEGENERATE | 228 | 120 | **108** |
| **two-sided FACTOR-WISE** | **7** | **7** | **0** |

## 8. The seven verdict rows

The factor-wise masks are exactly the non-empty unions of full component
triples, and every one divides by exact Chapman-Kolmogorov with the
process's own conditional exhibited and re-verified.

| mask | fields | labels | transfer columns | verdict | interpolant |
|---|---|---|---|---|---|
| `m146` | `{value@0,1,2}` | 8×8×8 | 4 / 2 | DIVISIBLE | 16 non-zero, all `1/2` |
| `m292` | `{authors@0,1,2}` | 8×8×8 | 4 / 2 | DIVISIBLE | 16 non-zero, all `1/2` |
| `m584` | `{init@0,1,2}` | 8×8×8 | 4 / 2 | DIVISIBLE | 16 non-zero, all `1/2` |
| `m438` | `{value,authors}@0,1,2` | 64×64×64 | 16 / 4 | DIVISIBLE | 256 non-zero, all `1/4` |
| `m730` | `{value,init}@0,1,2` | 64×64×64 | 16 / 4 | DIVISIBLE | 256 non-zero, all `1/4` |
| `m876` | `{authors,init}@0,1,2` | 64×64×64 | 16 / 4 | DIVISIBLE | 256 non-zero, all `1/4` |
| `m1022` | all nine fields | 512×512×512 | 64 / 8 | DIVISIBLE | 4,096 non-zero, all `1/8` |

Every row's **second** transfer column count is `>= 2`: these are
two-sided tests in the engraved sense, not forced ones.  `[GATE DET.3]`
each re-decides identically on a second independent pass through the same
decision order.

## 9. The refusals, and their exact geography

`[GATE G1]`  **A two-sided row REFUSES iff some committed component is
read at lags 0 and 2 but NOT at lag 1** — the GAP — **and DIVIDES
otherwise.**  Verified against every one of the 235 two-sided masks.  The
type-profile census makes the boundary explicit; `B` = both transfers
bite, `D1` = first only, `D2` = the gap, `N` = neither:

| type profile | masks | outcome |
|---|---|---|
| `(B,B,B)`, `(B,B,D1)`, `(B,B,N)`, `(B,D1,D1)`, `(B,D1,N)`, `(B,N,N)` | 127 | two-sided DIVISIBLE |
| `(B,B,D2)`, `(B,D1,D2)`, `(B,D2,D2)`, `(B,D2,N)`, `(D1,D1,D2)`, `(D1,D2,D2)`, `(D1,D2,N)` | 108 | two-sided INDIVISIBLE |
| `(D1,D1,D1)`, `(D1,D1,N)`, `(D1,N,N)` | 152 | forced-divisible |
| `(D2,D2,D2)`, `(D2,D2,N)`, `(D2,N,N)` | 61 | forced-indivisible |
| `(N,N,N)` | 64 | 63 doubly degenerate + 1 one-label |

`[GATE G3]`  **Every refusal inherits its second side from a factor that
is `(D-1)`-degenerate on its own**, verified factor by factor on all 108:
each refusing mask carries at least one factor whose own first transfer is
column-constant while its own second transfer bites — a standalone
FORCED-INDIVISIBLE map, evidence of nothing by `(D-1)` — together with at
least one OTHER factor supplying the first-transfer bite.  The refusal is
the `(D-1)`-degenerate situation of one factor, dressed in a product with
a biting partner.  That is why no verdict cites it.

**The certificates are produced, not implied.**  Every refusal carries a
collision certificate — two conditioning labels whose `Gamma(r4<-r3)`
columns agree in EVERY entry while some target's `Gamma(r5<-r3)` entries
differ — checked atom by atom, `108/108`; and a Farkas vector `w` for that
target's row system with `w^T M <= 0` componentwise and `w^T b > 0`,
verified by the committed `farkas_ok`, `108/108`.  The vectors are the
minimal ones the collision supplies: two non-zero entries, `+1` and `-1`,
on the colliding pair.  The instrument census is printed:
**Chapman-Kolmogorov 127, collision + Farkas 108, and 0 exact-simplex
systems solved anywhere in this receipt.**

## 10. The nulls

**(a) The fair null — the load-bearing one.**  The record's cut-1 and
cut-3 labels are kept and the middle cut is fully randomised into classes
of the reference map's own sizes, by the printed congruential shuffle
`x <- (1103515245 x + 12345) mod 2147483648`, seeds `(20260728, 11)`,
Fisher–Yates over the `sk()`-sorted parent list.  No random module, no
clock, no hash-seed dependence.  Three references: the lag-0 payload map
`m14`, a FACTOR-WISE verdict row `m146`, and a REFUSING
compound-degenerate row `m166`.

| reference | seed | classes | transfer columns | verdict |
|---|---|---|---|---|
| `m14 {value@0,authors@0,init@0}` | 20260728 | 8,8,8 | 8 / **1** | DIVISIBLE — `(D-2)` degenerate, carries no evidence |
| `m14` | 11 | 8,8,8 | 8 / **1** | DIVISIBLE — `(D-2)` degenerate, carries no evidence |
| **`m146 {value@0,1,2}`** | 20260728 | 8,8,8 | 8 / 2 | **INDIVISIBLE**, 32 negative entries |
| **`m146`** | 11 | 8,8,8 | 8 / 2 | **INDIVISIBLE**, 32 negative entries |
| `m166` | 20260728 | 16,16,16 | 16 / 2 | **INDIVISIBLE**, 128 negative entries |
| `m166` | 11 | 16,16,16 | 16 / 2 | **INDIVISIBLE**, 120 negative entries |

Scored through the same two-sided gate the record rows face: `2` of the
`6` control runs are `(D-2)`-degenerate and are excluded; **`4` are
two-sided and `4` refuse.**  Each refusal carries the strongest
certificate available — `Gamma(r4<-r3)` is square and INVERTIBLE, its
exact determinant printed, so eq. 22's algebraic interpolant is the UNIQUE
candidate and it fails positivity, which rules out the only candidate
rather than separating a cone.

**What this contrast supports, stated exactly, and what is matched.**  At
`m146` the record map divides and the record's outer cuts with a
randomised middle cut refuse, at both seeds.  `Gamma(r5<-r3)` is the
record's own in both — only the middle cut moves — so the comparison
isolates the middle cut's labelling and nothing else.  What is matched is
the CLASS SIZE profile at that cut and nothing more: the control's middle
label is a random function of the 65,536 distinct depth-12 cut histories
dealt into blocks of the reference map's own sizes, while the record's is
a function of the field record alone, so the control's `Gamma(r4<-r3)`
carries more distinct columns (8 against the record's 4).  Within that
declared design the conclusion is that the record's renewal-4 labels are
**not interchangeable with a size-matched random relabelling**, and the
divisions of §8 are a property of the record's own middle cut, not a
structural artefact.  This is the contrast U1b could not obtain: there the
fair null divided because `(D-2)` forced divisibility whatever the middle
cut was.

**(b) Matched-size random maps.**  The distinct cut HISTORIES at every cut
— 4,096 at `r3`, 65,536 at `r4`, 1,048,576 at `r5` — are dealt into
classes of the reference map's sizes by the same printed shuffle.  `4`
runs at two references and two seeds, all `4` two-sided, all `4`
INDIVISIBLE, each with the unique-algebraic-interpolant certificate (26
and 30 negative entries).  Read as the U1b round's correction demands:
these controls are matched on class sizes and not on the forcing-relevant
property, so this is a memory contrast, not a divisibility distinction.
The fair null carries §10's claim alone.

## 11. The map-dependence structure

- **Fixedness** is moved by nothing in this class: the whole `1,024`-mask
  class is admissible on this cut triple `[A1]`.
- **Bite on the first transfer** is moved by whether some component is
  read at two consecutive lags; **bite on the second transfer** by whether
  some component is read at two lags differing by 2 (§6).
- **The verdict** is moved, and the fields that move it are printed: over
  edges between two two-sided rows, each lag-0 and each lag-2 field flips
  a verdict `26` times and each lag-1 field `66` times.  The lag-1 fields
  dominate because adding lag 1 to a gap factor destroys the gap.
- **Between two FACTOR-WISE rows no single field flips a verdict — the
  list is empty.**  Inside the verdict set there is no selection problem
  to pose at this class; the selection problem lives entirely in the
  compound-degenerate set, and its exact locus is the gap `[G1]`.

## 12. The accelerators, and what they are gated against

This receipt enumerates ~10⁶ leaves of the committed grammar.  Exactly
**four** committed functions are wrapped to make that affordable, and none
of the four is trusted.

- Three are pure memo wrappers — `regs_of`, `admissible`,
  `admissible_arb_ckeys`.  Every stored value is LITERALLY the committed
  function's own return value: a miss calls the committed function, a hit
  returns what the committed function returned.  The only claim is purity
  in the memo key, read off the committed source — no global, no clock,
  no random source `[GATE ACC.1]`.
- The fourth rebuilds `event_poset` INCREMENTALLY from the cached parent
  prefix, so its value is computed here rather than quoted.  It is
  compared with the committed `event_poset`, as a list of index sets, on
  **1,757,104 / 1,757,104** calls of the declared population, `0`
  mismatches `[GATE ACC.3]`.
- Every leg that uses them is DOUBLE-RUN with the accelerators
  UNINSTALLED — d42b1's own `regs_of`, `event_poset`, `admissible` and
  `admissible_arb_ckeys` — and the two enumerations agree leaf by leaf and
  weight by weight: legs 1 and 2 in full `[ANCHOR ACC.2]`, the renewal-4
  leg on its declared sample `[ANCHOR ACC.4]`, the renewal-5 leg on its
  declared sample `[ANCHOR ACC.5]`.
- The 10⁶-cell accumulations are carried as INTEGER numerators over one
  common denominator `D = 35184372088832` and converted to `Fraction`s
  before use; `w == NUMER[w]/D` is verified for every distinct leaf weight
  `[GATE N1]`.  This is a change of representation, not an
  approximation.
- The cyclic garbage collector is switched off for the duration.  No data
  structure this receipt builds contains a reference cycle, so this
  changes running time and nothing else.

`[GATE DET.1–DET.3]`  The joint law, the `Gamma` family and the
column-constancy tests are independent of dict and set iteration order;
the whole 512-mask classification recomputes identically on a second
independent pass; every verdict row re-decides identically.

## 13. What this does and does not say

- **It does not say the record law is divisible at renewal grain in
  general.**  It says that on the declared ensemble, over the swept
  lag-`<=2` class, every map whose every factor bites on both sides
  divides, and that the interpolant test there is a real test: at the
  factor-wise reference the fair null carries, the control refuses where
  the record divides.  Seven verdict rows are seven, and the fair null is
  run at one of them, not at all seven.  The
  class-scope qualifier of U1b's M1 stands unchanged — the sweep covers
  the `2^9` subset lattice of the declared payload field set at lags
  `0..2`, not every committed-field map.
- **It does not dismiss the 108 refusals.**  They are exact refusals of
  the generated law at their label sets, each with two verified
  certificates.  What they are not is evidence about the record grain:
  each is a product in which one factor supplies the second side while
  being `(D-1)`-degenerate on its own `[G3]`, which is the situation the
  engraved predicate exists to exclude.
- **The reason the verdict set cannot refuse in this class is measured
  and stated.**  A factor is two-sided only when its lag set carries both
  a consecutive pair and a pair differing by 2 (§6); inside lags `0..2`
  that forces `{0,1,2}`, and reading a component at all three lags puts
  the intervening renewal's symbol into the middle cut's label, which is
  exactly the Markov condition Chapman-Kolmogorov then confirms on all
  seven rows.  The factor-wise clause and the refusal set are disjoint
  here **because of the lag budget**, not because the law is
  structurally divisible.
- **It is not a CP-divisibility test.**  No completely positive map and
  no CP criterion appears anywhere.  CP-divisibility and
  Barandes-indivisibility are orthogonal axes and this unit does not
  cross them.
- **No Bell or locality claim** is made or implied.
- **Indivisibility is not treated as a quantum signature.**  `[B3]`'s
  criterion is unistochasticity, which is U3's screen, not this unit's.
- **No exact covariance is claimed**, per L-1: the renewal-grain label
  sets swept here are fixed finite sets, which is exactly the hypothesis
  of the finite-stochastic Lorentz no-go.
- **No certificate is claimed that was not produced.**  Every row is
  decided strictly earlier in the decision order than the feasibility LP:
  127 by exact Chapman-Kolmogorov, 108 by the collision certificate and
  its Farkas vector.  The exact Phase-I simplex, the
  feasibility-preserving reduced system and its lift are lifted from the
  committed U1 receipt, available, and **unexercised** — `0` simplex
  systems are solved anywhere in this receipt.  The only committed LP
  object this receipt exercises is `farkas_ok`, which verifies all 108
  refusal certificates.

## 14. Scope

Transport scope (`d42b1`) only; the two-actor pool only; the ONE declared
ensemble — renewals at `3/6/9/12/15`, minimal intervals, cut triple at
depths `(9, 12, 15)` — and no other.  Unequal-interval depth-15+ variants
are named follow-ups, not this unit.  The field lattice reads the base
chain to lag 2 and the class is its `512` payload subsets (`1,024` with
the inert `state` bit); **lag `>= 3` is admissible on no cut triple below
depth 18** and is a declared cap.  Unpruned exhaustiveness scans cover
legs 1 and 2 in full and declared stride samples of 49 and 25 parents at
legs 3 and 4; the prune's premises and the live-count identity are
asserted at every expansion of every leg.  Exact LP caps 700 variables /
400 constraints on the full system and 5,000 / 1,200 on the reduced one
(unexercised); the committed `decide_triple` is handed a row only when
every label set is at most 64, and rows above that cap are decided by
exact Chapman-Kolmogorov or by the collision certificate, with
`EXCLUDED-BY-CAP` empty; eq. 22's exact inversion runs to 64 labels; a
null reference map carries at most 16 classes; certificate prints are
digests capped at 24 non-zero entries with the verification on the full
object; compound-degenerate rows are printed individually up to 240, and
all `228` fall inside that cap, so no row of this receipt is decided
without being printed.
Renewal grain per paper 0 §4's `[POSIT]`; no claim about non-renewal
division-event candidates.  No unistochasticity claim, no
measure-existence claim, no infinite-volume claim, no CP, Bell, locality
or covariance claim.

## 15. Handover

- **To paper 0 §9b and the Phase II board.**  The founding question of
  v11 is asked with bite on both transfers for the first time, and the
  answer at the first askable grain is that the law DIVIDES.  U1b's
  "decided by structure, not tested" no longer applies: `235` masks pose
  a two-sided test, `7` of them survive the factor-wise clause, and at
  the factor-wise row the fair null is run on, the control refuses while
  the record divides — so the divisions are tested, not forced.  The
  enrichment fork is untouched and σ+ was never defective.
- **To U2 (the J-conjecture).**  The refusal geography is exact and it is
  the geography to weld against: the refusing class is precisely the
  masks carrying a GAP factor — a component read at lags 0 and 2 without
  lag 1 — and every one of them is compound-degenerate.  A weld that
  distinguishes the 108-refusal class from the 127-division class is
  distinguishing gap factors from gapless ones, which is a statement
  about which lags a beable retains, not about divisibility.  The
  selection problem at renewal grain, lag `<= 2`, has exactly this
  content and no other.
- **To U3 (the unistochasticity screen).**  `108` refusing transfers
  exist with exact rational entries and verified certificates, on label
  sets of size `16` (12 rows), `32` (42), `64` (36), `128` (15) and `256`
  (3).  They are available to the screen; this receipt makes no
  unistochasticity claim about any of them, and every one is
  compound-degenerate, so a screen result on them carries the same
  qualification this receipt's census does.
- **The one open computation, stated so it can be picked up as written,
  with its status marked.**  MEASURED here, over lags `0..2`: a factor's
  first transfer bites iff its lag set carries two consecutive lags, its
  second transfer bites iff its lag set carries lags 0 and 2, and a
  two-sided row refuses iff some factor carries lags 0 and 2 without lag
  1 (§6, `[G1]`).  Inside lags `0..2` the only lag set that bites on both
  sides is `{0,1,2}`, which carries lag 1 and therefore no gap — that is
  why the verdict set here cannot refuse, and it is a fact about the LAG
  BUDGET.  NOT MEASURED, and the reason the frontier is named rather than
  claimed: the smallest lag set that would bite on both sides while
  leaving a 2-apart pair's intervening lag out is **`{0,1,3}`**
  (consecutive pair `{0,1}`, 2-apart pair `{1,3}`, lag 2 absent).  A map
  reading base-chain lag 3 is fixed only on a cut triple beginning at the
  FOURTH renewal — **depth 18** in this grammar, cut triple
  `(12, 15, 18)`, `16^6 = 16,777,216` leaves at the same branching.
  Whether the per-factor rule extends past lag 2 at all, and whether the
  generated law refuses at a factor-wise row there, is **not decided
  here**: that computation is the next askable frontier.
