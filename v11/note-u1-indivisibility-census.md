# U1 — result: **U1-BRIDGE.** The generated record law is indivisible. On the committed transport grammar, read at record grain through the committed relative-horizon kernel, there are composable cut triples at which **no stochastic intermediate matrix exists at all** — not merely a pseudo-stochastic algebraic one — with an exact Farkas certificate on every one. This is the corpus's first generated indivisible bridge, and the first indivisibility witness of any kind since v1's two abandoned ones. The everywhere-form is false: the same census contains divisible triples. Descent failure is **necessary but not sufficient** for cut-indivisibility, so the two instruments stand in a measured containment rather than a split.

**Status:** RESULT, STRICT, 2026-07-27.  Pin
`note-u1-indivisibility-census-pin.md` (frozen before the receipt
existed).  Binding specification: paper 0 §7 (U1), §6 constraints 1/4/6,
§10, §3, §4; `[V11-CAT]` §4.5, §4.9-preamble, §7 ranks 1 and 4.  Parents:
D70 (relative-horizon kernels), D72/D74 (the transport square census and
the 44 descent-obstruction squares), D62 row R4, D49/D43b (the `Zhat`
completion), paper 31 §4.3 / d43c (Born = K1), the D75 audit pin (b) Arm
0, `[B3]` eqs. 22–23.  Receipt
`v11/code/u1_indivisibility_census_exact.py`, output
`v11/code/u1_output.txt` — **36 PASS / 0 FAIL / 0 ANCHOR-FAIL, exit 0,
242 s wall clock, single-threaded, exact `Fraction` arithmetic
throughout** (`Q(sqrt 2)` for the Arm-0 amplitudes; no float appears in
any substantive computation), **byte-identical under `PYTHONHASHSEED`
0 / 7, timing lines excepted**.  Committed v10 layers are single-sourced
by text-slice with exit-freedom gated and by AST extraction (d42b1,
d42b3, D74's census machinery, D46b's kernel objects), under an AST
signature pass; exit 1 is reserved for anchor failure and no anchor
failed.

---

## 1. The verdict

> **U1-BRIDGE** `[MEASURED, at the declared scope and caps]`
>
> On the two-actor transport family to depth 5, with configurations read
> by the D62 field set ported to transport scope, **6 of the 10
> non-degenerate cut triples admit no column-stochastic intermediate**:
> `(1,2,3)`, `(1,3,4)`, `(2,3,4)`, `(2,3,5)`, `(2,4,5)`, `(3,4,5)`.  Two
> triples are divisible, two are excluded by the declared LP cap, and ten
> are structurally vacuous.  The payload-enriched configuration map
> returns the same verdicts wherever both are decided; the three-actor
> pool returns 2 indivisible triples of its own; the renewal-started
> window returns 1.  **14 indivisible triples across all arms and both
> configuration maps, every one carrying a verified Farkas certificate.**
>
> The `[B3]` eq. 22 algebraic reading, run under a declared
> fixed-configuration-space convention, is **pseudo-stochastic on 13 of
> 20 triples with 1,103 exactly-counted negative entries** — and is
> strictly weaker than the feasibility reading in both directions, which
> the census exhibits rather than assumes.

Two subsidiary results carry independently of the verdict.

> **The renewal reset is delivery-conditioned, not grammatical.**
> `[MEASURED + constructed witness]`  D62 row R4's corollary — every
> pair-arbitration returns the serialised state to the root — ports to
> transport scope and holds at every reachable cap (`1264/1264`
> in-family; `2032/2032` at closed scope).  It is **false in general**:
> an eight-event admissible chain, priced event by event against the
> committed layer, ends in a pair-arbitration whose post-state carries
> two token records.  Paper 0 §4's `[POSIT]` that the division-event
> configuration space is fixed is therefore a property of the
> delivery pattern, not a theorem of the grammar.
>
> **Boundary sufficiency, a theorem at closed scope, fails at transport
> scope.** `[MEASURED]`  (H1)+(H2) make `sigma` a sufficient boundary
> statistic in the delivery-free grammar.  With deliveries the same
> statistic is insufficient from depth 2 onward: `4 / 8 / 12` of the
> `11 / 19 / 32` configuration classes at depths 2/3/4 contain histories
> with different next-configuration laws.

## 2. The preamble — v1 paper 22's definition, repaired

v1 paper 22 Definition 2 states indivisibility twice, and the two
statements are not equivalent: the first sentence quantifies universally
over the intermediate, the "equivalently" clause existentially.  The D75
audit flags the defect and reads the corpus as proving only the
existential form.  The definition is restated with the quantifiers
separated and each named.

Let `Gamma(c' <- c)` be the transition family of a process indexed by
cuts of a partial order, `Gamma_{ji} = P(config j at c' | config i at
c)`, columns summing to 1.

- **(D1) LOCAL DIVISIBILITY at a composable triple `(c, c', c'')`:**
  there **exists** a column-stochastic `X` with
  `X . Gamma(c' <- c) = Gamma(c'' <- c)`.  When `Gamma(c' <- c)` is
  square and invertible, `X` is unique and equals `[B3]` eq. 22's
  algebraic interpolant `Gammabar = Gamma(c'' <- c) Gamma(c' <- c)^-1`,
  so (D1) is then exactly *"`Gammabar` has no negative entry"*.  When
  `Gamma(c' <- c)` is singular the algebraic form does not apply and (D1)
  is a linear feasibility question.
- **(D2) INDIVISIBLE AT A TRIPLE:** (D1) fails there.
- **(D3) INDIVISIBLE (process-level, existential):** (D2) holds for
  **some** composable triple of the declared cut family.
- **(D4) EVERYWHERE-INDIVISIBLE (the universal form):** (D2) holds for
  **every** composable triple.

(D3) and (D4) are the two readings v1 conflated.  Every verdict here is
stated in the (D2)/(D3) form; the (D4) form is reported separately and
never inferred from (D3).  **Degeneracy, declared:** at a triple whose
first cut carries a single configuration, `X = Gamma(c'' <- c) . 1^T`
satisfies (D1) for any `Gamma(c' <- c)`, so such a triple can never be
indivisible; it is reported **structurally vacuous**, not as a divisible
datum.  Ten of the twenty ARM-A triples are vacuous for exactly this
reason, and none of them is counted as evidence of divisibility.

The feasibility form is the decisive instrument throughout, for a reason
that is measured rather than assumed: on this carrier the configuration
support **strictly grows** with the cut (`1, 5, 11, 19, 32, 54` for the
D62-faithful map; `1, 5, 13, 37, 97, 185` for the enriched one), so
`Gamma(c' <- c)` is never square on the supports and eq. 22's algebraic
form is inapplicable as written.  The algebraic arm is run anyway under a
declared convention (§5.4) because the pin asks for exact negative-entry
counts; the convention is labelled a convention, and the feasibility form
— which quantifies over **all** stochastic intermediates rather than the
unique algebraic one — carries every verdict.

## 3. Arm 0 — Born = K1 in exact arithmetic, and the `Zhat` sibling

**The committed pair exhibit re-runs.** `[ANCHOR]`  A's arbitration menu
is one event at the early cut and three at the join; full per-actor sums
`1` and `5/4`; the pair branches inadmissible early.

**The isometry defect is exactly 0.**  The family
`V_C = Acceptance o OpeningClick` is rebuilt in `Q(sqrt 2)`, where the
amplitude `1/sqrt(2)` is exactly representable: `V_pair` (`4x1`),
`V_single` (`2x1`) and both factors of each satisfy `M^T M - I = 0`
identically.  The committed receipt gates `1e-40` in `mpmath`; the same
object has an exact algebraic zero, and the upgrade costs nothing.

**Born = K1 exactly.**  The squared branch amplitudes of `V_pair` are the
rationals `1/2` and `1/2`, equal to `PK1` on the 2-conflict recomputed
from the committed layer; `V_single`'s branch is deterministic and equals
`PK1` on the singleton.

**Menu reconstruction at both cuts, from the same matrices.**
(past-local admissible-ckey index `x` budget share `1/4 / #components`)
`x` (the `V_C` Born splits) `=` the committed menus: `1/4` on the
arbitration sector at the early cut, `1/4 + 1/8 + 1/8` at the join.  What
differs between the cuts is the classical index set (`{single}` vs
`{single, pair}`), not the operator.

**The `Zhat`-completed sibling, built to the audit's specification.**  The
closed-scope family reproduces d43b's census `[1,7,39,215,1191,6471,
34375]`; the uniform-lookahead intrinsic partition stabilises at six
states at lookahead 2 (tables `[4,4,5,5,5] / [4,5,6,6] / [4,5,6]`); the
exact `6x6` transfer is well-defined per state on all 215 depth-`<=3`
members and equals the committed matrix entry for entry, with row sums
`(2,2,2,5/2,2,2)`.  With the committed Perron data (`T f = 2 f` exactly,
`f = (4,4,3,7,3,3)/3`, `lambda = 2`) the completion
`Zhat(i->j) = T_ij f_j / (lambda f_i)` is:

| from \ to | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 3/4 | 1/4 | · | · | · | · |
| **1** | · | 3/4 | 3/64 | 7/64 | 3/32 | · |
| **2** | · | · | 3/4 | · | · | 1/4 |
| **3** | **1/7** | · | · | **3/4** | · | **3/28** |
| **4** | · | · | · | · | 3/4 | 1/4 |
| **5** | · | · | 1/8 | · | 1/8 | 3/4 |

Every row sums to exactly 1 with every entry non-negative; the conflict
row is exactly `{0: 1/7, 3: 3/4, 5: 3/28}`, total mass exactly 1 — the
row the D75 audit specified to the receipt.  **The two anchor matrices
handed to U3 are `{V_single, V_pair}` and this transfer.**  Its column
sums are `25/28, 1, 59/64, 55/64, 31/32, 19/14`: the completed chain is
row-stochastic and **not** doubly stochastic, hence not unistochastic.
That is the audit's pin (b) Arm 1 screen; it is **reported here and left
for U3 to adjudicate**, because the necessity-of-`i` question is U3's
unit and not this one's.

## 4. Arm 1 (a) — the D62-R4 renewal predicate, ported and verified

**The predicate.**  D62 selects rows by `(event tag, base in refs?,
|proposers(ckey)|)`, a partition with no fall-through; R4 is the pair-arb
— tag `'r'` with two proposers in the ckey.  The predicate is purely
syntactic and reads no state; it ports verbatim.

**The state.**  D62's `sigma` is `(hold, live, comps, refs, sup|refs)`
with tokens renamed canonically.  Two things change at transport scope
and both are declared: an actor may hold several non-superseded versions
once deliveries exist, so `hold` becomes the **set** of alive holdings
(at closed scope it is a singleton by D62 (5a) and the definitions
agree); and tokens are renamed by **role** rather than by name — the
state is the sorted multiset of token records `(holders, superseded?,
live triples on it)` — which is D62's canonical renaming made
permutation-safe.  `comps` is not carried: by D62 Row 0 it is a function
of `live`, which the token records contain.  `refs` is D62's F2, so a
superseded unheld token is dropped exactly as in the table.  The receipt
runs this map **both ways**: winner-invisible (D62-faithful, by D62's own
corollary that `sigma(h+e)` does not depend on the arbitration winner)
and payload-enriched, each token carrying `(value, authors, initiator)`.

**The port verification, three ways.**

| gate | population | result |
|---|---|---|
| PORT-1, closed scope, depth `<=6` | 34,375 histories | **2,032 / 2,032** pair-arbs return to the root state |
| PORT-2, transport scope, depth `<=5` | 30,729 histories | **1,264 / 1,264** return to root; **1** distinct post-renewal state |
| PORT-3, constructed chain | 8 events, all admission-checked | post-state carries **2** token records — **not** the root |

PORT-3's chain is: blind self-arbitration by both actors (which the
grammar admits, because neither cone sees the other's supersession),
diverging the holdings; one delivery, giving B a second alive token; two
proposals on the delivered token; the pair-arbitration that follows
supersedes only its own base.  Weights, in order:
`1/8, 1/4, 1/8, 1/4, 1/8, 1/8, 1/16, 1/8`.

**Consequence.**  The renewal-grain configuration space is `{root}` under
the winner-invisible map and has **8 elements** under the enriched map
— (winning value) `x` (winning author) `x` (initiator), each realised 158
times in-family.  It is fixed and finite at every reachable cap, and it
is not fixed in general.  Paper 0 §4's `[POSIT]` is scored
**supplied-with-a-boundary**.

**L-1's bound, quoted where it bites.**  The renewal-grain configuration
space just measured *is* a fixed finite set at this cap, which is exactly
the hypothesis of the finite-stochastic Lorentz no-go.  No exact
covariance may be claimed for any law built on it: at most
statistical/approximate Lorentz invariance is available at renewal grain,
never exact covariance, and this unit claims none.

## 5. Arm 1 (b) — the `Gamma` family and the interpolant census

### 5.1 The construction

The raw generated menus are not a stochastic matrix — they sum to `2`
(29,605 histories) or `5/2` (1,124) on the ARM-A family — which is the
D75 audit §5.3 point and the reason a `Gamma` family needs a
normalisation before it exists at all.  The normalisation is the
committed one: D46b's relative-horizon objects, lifted by AST from the
terminal D46b receipt exactly as D70 lifts them —
`G(h,0) = 1`, `G(h,r) = sum_e q(e|h) G(h+e, r-1)`, and
`k_r(e|h) = q(e|h) G(h+e, r-1) / G(h, r)` with `r = D - |h|` at the
family's own declared cap `D`.  Gated exactly: the one-step kernel sums
to 1 at every history and the induced cut marginal is 1 at every depth,
on every arm.

`Gamma(c' <- c)_{ji} = P(alpha = j at c' | alpha = i at c)` is then the
exact conditional of that process, computed from the leaves so that its
marginals are the cut marginals.  Cuts are depths of the generated order;
configurations are the ported state, both ways.

### 5.2 The four arms and their caps

| arm | family | cuts | configuration supports |
|---|---|---|---|
| **ARM-A** record grain | (A,B) transport, 30,729 histories, depth `<=5` | 0..5 | `1,5,11,19,32,54` / `1,5,13,37,97,185` |
| **ARM-B** division-event grain | 16 renewal bases, 16,368 histories, depth `<=6` | 3..6 | `1,5,11,19` / `8,40,76,148` |
| **ARM-C** renewal-to-renewal | inside ARM-B | renewal 0,1,2 | `1`, `8`, `8` |
| **ARM-D** pool control | (A,B,C) transport, 50,617 histories, depth `<=4` | 0..4 | `1,8,27,59,124` |

ARM-B conditions on a **past** event only — that the depth-3 prefix ends
in a pair-arbitration — with the initial distribution taken as the
horizon-6 measure's own conditional, so no future information enters.

### 5.3 The censuses, both ways

**ARM-A, winner-invisible map.**

| triple | verdict | instrument | detail |
|---|---|---|---|
| `(0,*,*)` ×10 | VACUOUS | — | first cut carries one configuration |
| `(1,2,3)` | **INDIVISIBLE** | exact LP infeasibility, Farkas verified | 209 vars × 106 rows, 335 pivots |
| `(1,2,4)` | DIVISIBLE | exact LP feasibility | a stochastic intermediate exists but is **not** the process's own conditional |
| `(1,2,5)` | DIVISIBLE | exact LP feasibility | as above |
| `(1,3,4)` | **INDIVISIBLE** | exact LP infeasibility, Farkas verified | 608 vars × 179 rows, 3,216 pivots |
| `(1,3,5)` | EXCLUDED-BY-CAP | row certificate only | 1,026 vars × 289 rows |
| `(1,4,5)` | EXCLUDED-BY-CAP | row certificate only | 1,728 vars × 302 rows |
| `(2,3,4)` | **INDIVISIBLE** | row certificate, Farkas verified | **12 of 32** target configurations admit no non-negative row |
| `(2,3,5)` | **INDIVISIBLE** | row certificate, Farkas verified | **14 of 54** |
| `(2,4,5)` | **INDIVISIBLE** | row certificate, Farkas verified | **12 of 54** |
| `(3,4,5)` | **INDIVISIBLE** | row certificate, Farkas verified | **13 of 54** |

**Census: INDIVISIBLE 6, DIVISIBLE 2, EXCLUDED-BY-CAP 2, VACUOUS 10.**

**ARM-A, payload-enriched map.** INDIVISIBLE 5 — `(1,2,3)` by full LP
infeasibility (481 vars × 198 rows, 841 pivots), and `(2,3,4)`,
`(2,3,5)`, `(2,4,5)`, `(3,4,5)` by row certificate with `6/97`, `4/185`,
`18/185`, `24/185` obstructed rows — EXCLUDED-BY-CAP 5, VACUOUS 10.
No triple receives opposed substantive verdicts under the two maps; the
three differing entries are all cap exclusions under the larger map.  The
census is therefore not an artefact of D62's winner-invisibility
corollary — and the enriched map is decided on fewer triples, which is a
cap fact and is printed.

**ARM-B.**  Winner-invisible: 3 vacuous (the renewal cut carries the
single root configuration) and `(4,5,6)` divisible by Chapman-Kolmogorov.
Enriched: `(3,4,5)` and `(3,4,6)` divisible by Chapman-Kolmogorov,
`(3,5,6)` excluded by cap, `(4,5,6)` **indivisible** with 64 of 148 rows
obstructed.  **The window is three steps long.**  ARM-A's indivisible
triples all begin at relative depth `>= 2`, so testing them after a
division event needs depths 5,6,7 — beyond this cap.  ARM-B's
divisibility is a *window* fact and is not evidence that renewal restores
divisibility; the receipt says so at the point of reading.

**ARM-C.**  The mass reaching a second renewal inside the cap is
`1/257`.  Conditioned on that, the renewal-2 configuration distribution
is the **same** from all 8 renewal-1 configurations: the
renewal-to-renewal transfer is rank-one, `R^2 = R`, and every renewal
triple factors through it — a genuine renewal process at this scope.
This conditions on a future event and is labelled as such.  The
renewal-to-renewal triple `(0,1,2)` is **structurally vacuous at every
reachable cap**: renewal cut 0 is the root, a single configuration.  A
non-degenerate renewal triple needs three renewals, i.e. depth `>= 9` in
this grammar.  **The renewal-grain interpolant test is not run, not
passed**, and the reason is printed with the cap.

**ARM-D (three actors).** INDIVISIBLE 2 — `(1,3,4)` with 2 of 124
obstructed rows and `(2,3,4)` with 34 of 124 — EXCLUDED-BY-CAP 2,
VACUOUS 6.  The verdict does not rest on a two-actor accident.

**All arms, all maps: INDIVISIBLE 14, DIVISIBLE 5, EXCLUDED-BY-CAP 10,
VACUOUS 29.**

### 5.4 The `[B3]` eq. 22 algebraic arm, and exactly how weak it is

Barandes' eq. 22 needs a square `Gamma`, i.e. his kinematical axiom: one
fixed configuration space for all cuts.  This carrier has none away from
renewals (§2).  The arm is run under a declared convention — the
configuration space is the union `X` of the three cuts' supports, and a
configuration not yet realised at a cut is held fixed by the law (an
identity column) — which makes every `Gamma` square.  Exact rational
inversion; every column sum of `Gammabar` verified to be exactly 1.

**Census: pseudo-stochastic 13, stochastic 7, singular 0, excluded 0;
1,103 negative entries counted exactly.**  Representative most-negative
entries: `-1/584` at `(0,3,4)`, `-66/12593` at `(1,2,3)`,
`-5528/518885` at `(2,3,4)`, `-60454377/7356440080` at `(3,4,5)`.

Cross-tabulated against the feasibility verdict:
`PSEUDO-STOCHASTIC / INDIVISIBLE` 6, `PSEUDO-STOCHASTIC / DIVISIBLE` 2,
`PSEUDO-STOCHASTIC / EXCLUDED` 2, `PSEUDO-STOCHASTIC / VACUOUS` 3,
`STOCHASTIC / VACUOUS` 7.  **The algebraic reading is pseudo-stochastic
on five triples where a genuine stochastic interpolant provably exists or
where the triple is degenerate.**  Counting negative entries in
`Gammabar` is therefore *not* the same test as asking whether the process
divides, once the configuration space is not fixed — and on this carrier
it is not.

## 6. Arm 1 (c) — the geography, as input to U2

**The 44 descent-obstruction squares are named first and in full in the
receipt** (`u1_output.txt`, block `[A1-PRIME]`), each with its base
history, both events, the exact four step weights and the ratio.  Their
base-depth census is `{1: 4, 2: 40}`; all 44 carry kinds `(r,d)` and
ratio `1/2` forward.  D74's committed `44 + 44` split reproduces exactly (menu
quotient 113 classes, coarsest congruence 185, both closing the same 44),
and so does ABC3's `0 of 12`.

- **The indivisible windows are bridge windows.** The mass of the
  ensemble carrying **any** division event inside an indivisible window
  is `16/4173`, `16/1391`, `7/321` or `25/1391` — at most `1.8%`.  Over
  `98%` of the mass of every indivisible window lies strictly between
  division events, which is where paper 0 §4 places the anomalies.  This
  is a **measured co-location** offered as U2's input; the J-conjecture
  is not tested here.
- **The 44 sit on the lumpability defect.** 32 of the 44 have their base
  in a configuration class whose members carry different
  next-configuration laws.
- **The lumpability defect by depth:** `0/1`, `0/5`, `4/11`, `8/19`,
  `12/32` classes at depths 0..4.
- **One further co-location, recorded and not interpreted.** LD's
  obstruction has a one-kind address — a square's reversed image is
  priced iff its record carries no arbitration event
  (`17,277/17,277`, `note-ld-last-door.md`) — and every one of the 44
  descent-obstruction squares carries an arbitration event.  Two
  independent instruments localise on the arbitration-carrying locus.
  No claim is attached.

## 7. Arm 2 — the four descent conditions, on the same family at the same caps

**DC1 — the commuting-square identity** `P(a|H)P(b|Ha) = P(b|H)P(a|Hb)`,
over every ordered pair at every parent of depth `<=3` (squares to depth
5), exhaustive and unsampled.  Three normalisations are carried, because
the transport grammar admits three honest ones: the raw weights, D65's
own `p = q/M`, and the relative-horizon kernel `k_r`.

| population | raw | D65 `q/M` | horizon `k_r` |
|---|---|---|---|
| wider `sigma`-commuting census (11,814 ordered pairs) | **960** fail | **2,236** fail | **1,000** fail |
| DC1(f), refined-record identical (3,317 pairs) — Theorem 1's own hypothesis | 0 fail | **352** fail | 0 fail |

Exact ratio spectra: raw `{1: 10854, 1/2: 654, 2: 130, 2/3: 58,
3/2: 118}`; `q/M` adds `{4/5: 634, 5/4: 642}`; `k_r` adds
`{32/33: 6, 33/32: 2, 64/65: 24, 65/64: 8}`.  **The instrument does not
agree with itself across normalisations**, and that is reported rather
than averaged.  The failure D65 measured at closed scope (32,256 of
425,334 refined-identical pairs, under `q/M`) reappears here in the same
normalisation and the same class.

Two identifications are gated.

- **DC1's raw defect census *is* D72/D74's square census, to the unit.**
  Over every closed exchange square of the (A,B) transport family to
  depth 5 the raw identity fails exactly **960** times — D74's committed
  depth-5 defect count — and the failures split **604 curvature-type /
  356 descent-obstruction-type**, D74's committed proportions.  `[ANCHOR]`
- **The horizon normalisation changes the DC1 ratio exactly when the two
  orders carry different records.**  `G` is constant on
  refined-record-identical endpoint pairs, so on Theorem 1's own
  hypothesis class paper 29's descent condition and D72's square census
  are literally the same number.  Off that class they are different
  numbers, and both are printed.

**DC2 — boundary sufficiency.** Fails, as §1 records.  This is the
sharpest single difference from closed scope, where DC2 is exactly
(H1)+(H2) and is a theorem.

**DC3 — the five durable-record hypotheses.** (1) exclusive-and-exhaustive
alternatives: the normalised menu sums to exactly 1 at every history —
gated, but the same gate as the kernel construction, so reporting-only.
(2) decoherence of the queried algebra: trivially satisfied and trivially
uninformative, because the generated law is a stochastic process on
records; this is where the map's remaining segment lives, and U1 creates
no functional level.  (3) common refined cylinder = DC1.  (4) positivity
of every displayed conditioning cylinder: **0 non-positive weights over
243,768 priced candidates**.  (5) sufficient declared boundary = DC2, and
it fails.

**DC4 — the supplied-vs-derived ledger, re-scored at transport scope.**
The **boundary state** moves *back* to SUPPLIED: D65 moved it to DERIVED
at closed scope via DC2, and DC2 fails here.  The **measure** stays
SUPPLIED at finite horizon: the relative-horizon normalisation supplies a
probability law at every finite cap, and D70's infinite-horizon bound is
open.  **Renormalization, record instrument, clock dictionary and the
functional level** all stand as supplied.  **New item:** the **renewal
reset** is scored SUPPLIED-WITH-A-BOUNDARY (§4).

## 8. The agreement census

Arm 1's instrument is per-window; Arm 2's are per-step.  A triple
`(l0, l', l'')` is *Arm-2 defective* iff some DC1 or DC2 failure occurs
at a depth in `[l0, l''-1]`.  DC1 failures by parent depth: `1: 4`,
`2: 84`, `3: 872`.  DC2 failures by depth: `2: 4`, `3: 8`, `4: 12`.

| | Arm 2 DEFECTIVE | Arm 2 CLEAN |
|---|---|---|
| **Arm 1 INDIVISIBLE** | **6** | **0** |
| **Arm 1 DIVISIBLE** | **2** | 0 |

**Descent failure is necessary but not sufficient for
cut-indivisibility on this family.**  Arm 2 is defective on every window
of the family, including all ten vacuous triples, so at window scale it
has no resolving power; Arm 1 resolves.  The witness class that would
have made this a genuine **U1-SPLIT** — an indivisible triple in a clean
window, putting the instruments in opposite directions on one object — is
**empty, 0 of 8**.  The verdict is U1-BRIDGE with a characterised
containment, and the containment is itself a first-class result: the two
instruments measure different scales of the same defect, and neither is
redundant.

## 9. What this does and does not say

- **It is not a CP-divisibility test.**  (D1)–(D4) are statements about
  factorisation of column-stochastic matrices.  No completely positive
  map, no divisibility of a dynamical map on operators, and no CP
  criterion of any kind appears anywhere in the receipt.
  CP-divisibility and Barandes-indivisibility are orthogonal axes and
  this unit does not cross them.
- **No Bell or locality claim is made or implied.**  Bell is settled and
  closed; indivisibility pays the outcome-independence price and buys no
  locality result.  Nothing here is framed as one.
- **No resource-theoretic advantage is claimed.**  Magic `!=`
  indivisibility.
- **No exact covariance is claimed anywhere**, per L-1: at renewal grain
  the configuration space is fixed and finite, which is precisely the
  hypothesis under which exact covariance by invertible stochastic maps
  forces permutations.  At most statistical Lorentz invariance is
  available there, and this unit claims none.
- **The indivisibility is of the record-grain law, not of the
  realizer.**  v10's per-click law is divisible on histories by
  construction — it is a chain rule.  Paper 0 §3 assigns that law to the
  realizer stratum; U1 measures what the same process looks like read at
  the record's own grain, and it does not divide.  The two statements are
  consistent and the distinction is load-bearing.
- **Nothing is claimed at infinite volume**, and no measure-existence
  claim is made: D70's bound is open and this unit does not touch it.

## 10. Scope

Transport scope (d42b1) only; the declared families and caps only:
(A,B) depth `<=5`, the renewal-started window to depth `<=6`, (A,B,C)
depth `<=4`, D72/D74's own anchor windows at depth `<=4` and `<=3`,
closed scope to depth 6, DC1 parents to depth 3.  Exact rational LP caps
700 variables / 400 constraints, set by measured cost — an excluded
triple still gets the row certificate, so a cap can hide a *divisibility*
verdict but cannot hide an *indivisible* one; every exclusion is printed
with its size.  The eq. 22 algebraic arm runs on fixed configuration
spaces of size `<=100` under a declared convention.  Renewal grain per
paper 0 §4's `[POSIT]`, which PORT-3 shows is delivery-conditioned rather
than grammatical.  The renewal-to-renewal interpolant test is **not run**
(depth `>= 9` required).  No infinite-volume claim; no measure-existence
claim; no CP, Bell, locality or covariance claim.  The J-conjecture is
not tested — that is U2.  The unistochasticity screen is reported and not
adjudicated — that is U3.

## 11. Handover

- **To U2 (the J-conjecture):** the 44 named descent-obstruction squares
  with full step weights; the `604 / 356` split at the depth-5 window;
  the bridge-mass geography of every indivisible triple (`<=1.8%`
  division-event mass); the lumpability defect by depth; and the
  measured containment "descent failure `=>` nothing, cut-indivisibility
  `=>` descent failure", which is the shape any weld must respect.
- **To U3 (the minimal quantum record):** `{V_single, V_pair}` in exact
  `Q(sqrt 2)` with defect 0 and Born `= K1`; the `6x6` `Zhat` transfer
  with its column sums `25/28, 1, 59/64, 55/64, 31/32, 19/14` — the
  doubly-stochastic screen, reported, unadjudicated.
- **To U4 (sparse records on the crystals):** PORT-1/2/3 — the renewal
  predicate ports, the reset holds at every reachable cap and fails on a
  constructed admissible chain; the renewal sublattice's configuration
  space is `{root}` winner-invisibly and 8-element with payload; and
  L-1's bound already applies to it.
