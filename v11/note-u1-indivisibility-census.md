# U1 — result: **U1-BRIDGE-AT-ADJACENT-SCOPE, with the null attached.** At cut grain, on conditioning cuts that are *not* division events, the generated record state is a non-lumpable function of the divisible click law, and its `Gamma` family admits no column-stochastic interpolant at fifteen triples — ten distinct windows, every one carrying an independently verified exact Farkas certificate. That property is shared with, and held *less strongly than*, a uniformly random partition of the same prefixes into the same class sizes: coarse-graining a divisible chain is what produces it. At every conditioning cut that **is** a division event — the only cuts `[B3]` p.9 admits, and the grain paper 0 §4 puts the law at — the law **divides exactly**, and that now includes the pinned non-degenerate renewal-to-renewal triple, which divides by exact Chapman-Kolmogorov on a rank-one renewal transfer. Descent failure is **necessary but not sufficient** for cut-indivisibility, and DC2's failure and the interpolant census are one fact read by two instruments.

**Status:** GREEN-UNREVIEWED-REPAIRED, STRICT, 2026-07-27.  TERMINAL is
conferred by a delta round, not here.  Pin
`note-u1-indivisibility-census-pin.md` (frozen before the receipt
existed).  Binding specification: paper 0 §7 (U1), §6 constraints 1/4/6,
§10, §3, §4; `[V11-CAT]` §4.5, §4.9-preamble, §7 ranks 1 and 4.  Parents:
D70 (relative-horizon kernels), D72/D74 (the transport square census and
the 44 descent-obstruction squares), D62 row R4, D49/D43b (the `Zhat`
completion), paper 31 §4.3 / d43c (Born = K1), the D75 audit pin (b) Arm
0, `[B3]` eqs. 22–23 and p.9.  Receipt
`v11/code/u1_indivisibility_census_exact.py`, output
`v11/code/u1_output.txt` — **44 PASS / 0 FAIL / 0 ANCHOR-FAIL,
exit 0, 815 s wall clock, single-threaded**, exact `Fraction`
arithmetic throughout (`Q(sqrt 2)` for the Arm-0 amplitudes; no float
appears in any substantive computation).  Committed v10 layers are
single-sourced by text-slice with exit-freedom gated and by AST
extraction (d42b1, d42b3, D74's census machinery, D46b's kernel objects),
under an AST signature pass; exit 1 is reserved for anchor failure.

---

## 1. The verdict

> **U1-BRIDGE-AT-ADJACENT-SCOPE** `[MEASURED, at the declared scope and
> caps]`
>
> **At cut grain, off the division events.**  On the transport families
> read at record grain through the committed relative-horizon kernel,
> **fifteen composable cut triples admit no column-stochastic
> intermediate at all** — not merely a pseudo-stochastic algebraic one —
> each with an independently verified exact Farkas certificate, printed
> entry by entry.  Fifteen counts *verdicts*: the same window read by the
> two configuration maps counts twice, and the distinct `(arm, window)`
> pairs behind them are **10** (§5.4).  Every one of them has its first cut *strictly between*
> division events.
>
> **At division-event grain, the law divides.**  Split the whole census
> by `[B3]` p.9's own conditioning rule — the admissible conditioning
> times are the division events, which paper 0 §4 identifies with
> renewals — and it separates completely: **34 triples whose first
> cut is a division event, of which 30 are structurally vacuous and 4
> divide, and NOT ONE is indivisible.**  The
> pinned case is among them: the **non-degenerate renewal-to-renewal
> triple** (ARM-C2, §5.5) divides by exact Chapman-Kolmogorov.
>
> **The null.**  A uniformly random partition of the same prefixes into
> `alpha_sigma`'s own class sizes — identical granularity, zero record
> content — is obstructed on **more** target configurations than the
> record map is, at both seeds (§6).  Indivisibility at cut grain is what
> coarse-graining a divisible chain generically does; the record map
> holds the property *less* strongly than noise of its own granularity.
>
> The `[B3]` eq. 22 algebraic reading, run under a declared
> identity-padding convention, is **pseudo-stochastic on 13 of 20 triples
> with 1,103 negative entries counted exactly under that convention**, and
> is weaker than the feasibility reading in one exhibited direction.

**One fact, two instruments — said once.**  Arm 1's interpolant census
and Arm 2's DC2 failure are not two results.  Both are the
**non-lumpability of the ported state under deliveries**: DC2 measures it
per step, the interpolant census measures what it does to a window.  The
agreement table (§10) is the relation between two readings of that single
fact, not corroboration of one reading by the other, and nothing in this
note treats them as independent evidence.

Two subsidiary results carry independently of the verdict.

> **The renewal reset is delivery-conditioned, not grammatical.**
> `[MEASURED + constructed witness]`  D62 row R4's corollary — every
> pair-arbitration returns the serialised state to the root — ports to
> transport scope and holds at every reachable cap (`1264/1264`
> in-family; `2032/2032` at closed scope).  It is **false in general**:
> an eight-event admissible chain, priced event by event against the
> committed layer, ends in a pair-arbitration whose post-state carries
> two token records.
>
> **Boundary sufficiency, a theorem at closed scope, fails at transport
> scope.** `[MEASURED]`  (H1)+(H2) make `sigma` a sufficient boundary
> statistic in the delivery-free grammar.  With deliveries the same
> statistic is insufficient from depth 2 onward: `4 / 8 / 12` of the
> `11 / 19 / 32` configuration classes at depths 2/3/4 contain histories
> with different next-configuration laws.  This is the same fact the
> interpolant census reads at window scale.

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
datum.

**What the scope of the quantifier does not decide.**  (D2) is a property
of a *cut triple*, and `[B3]` p.9 does not admit every cut: the
conditioning times of an indivisible stochastic process are its division
events, and paper 0 §4 fixes those to be the renewals.  A triple whose
first cut is not a division event is therefore a statement about a
coarse-graining evaluated at a time the law does not condition at.  Both
classes are censused here and they are kept apart throughout (§7).

The feasibility form is the decisive instrument, for a reason that is
measured rather than assumed: on this carrier the configuration support
**strictly grows** with the cut (`1, 5, 11, 19, 32, 54` for the
D62-faithful map; `1, 5, 13, 37, 97, 185` for the enriched one), so
`Gamma(c' <- c)` is never square on the supports and eq. 22's algebraic
form is inapplicable as written.  The algebraic arm is run anyway under a
declared convention (§5.6) because the pin asks for exact negative-entry
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

**The state is a function of the actor pool, and the memo says so.**
`[GATE SIG.1]`  Token records name their holders, so the same event word
read in the `(A,B)` pool and in the `(A,B,C)` pool carries different
ported states — at the root already, and on 65 of the 69
shared words to depth 2.  The receipt's memo key is
`(history, actor tuple, map)`; a key that dropped the pool would serve
two-actor state to the three-actor arm on every shared word, and the gate
exists to make that impossible to do silently.

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
**supplied-with-a-boundary**; §13 records what PORT-3 owes forward, and
to which paper-0 lines.

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
marginals are the cut marginals.  Cuts are cuts of the generated order;
configurations are the ported state, both ways.

### 5.2 The instrument, and what a cap can and cannot hide

Each triple is decided in this order: structural vacuity; exact
Chapman-Kolmogorov (does the process's own conditional already
interpolate?); the algebraic interpolant where `Gamma(c'<-c)` is square
and invertible; the **row certificate** (does some target configuration
admit no non-negative row at all?); the **full feasibility LP**; and,
where the full system exceeds the plain cap, the **reduced system**.

The row certificate is *sufficient* for indivisibility and **not
necessary**.  A triple can be indivisible with every row individually
solvable, the obstruction living only in the column-stochasticity that
couples the rows.  **A cap can therefore hide an indivisible triple
exactly as easily as a divisible one**, and this census contains the
witness: `(1,4,5)` under `alpha_sigma` passes the row certificate with
no obstruction and is **indivisible on the full system**.

The reduced system is the full system rewritten by two reductions, each
proved feasibility-preserving in both directions inside the receipt:

- **implied zeros** — if some `i` has `A[j,i] > 0` while `B[k,i] = 0`,
  then `sum_j' X[k,j'] A[j',i] = 0` is a sum of non-negative terms and
  `X[k,j] = 0` in every solution; the variable and the now-trivial
  equation are deleted;
- **aggregation** — configurations with the same column `a_j` may be
  averaged over without changing any row sum or column sum, and so may
  targets with the same row `b_k`; one variable per (target-group,
  configuration-group) then suffices, carrying the group sizes.

Feasibility of the reduced system lifts to an explicit `X`, which the
receipt re-verifies from scratch — every entry `>= 0`, every column sum
exactly 1, `X.Gamma(c'<-c) = Gamma(c''<-c)` entry by entry.
Infeasibility of the reduced system carries a Farkas vector, printed as
exact `Fraction`s.  **Every triple of every arm is decided: the census
has no EXCLUDED-BY-CAP entry.**

### 5.3 The four depth-indexed arms and their caps

| arm | family | cuts | configuration supports |
|---|---|---|---|
| **ARM-A** record grain | (A,B) transport, 30,729 histories, depth `<=5` | 0..5 | `1,5,11,19,32,54` / `1,5,13,37,97,185` |
| **ARM-B** division-event grain | 16 renewal bases, 16,368 histories, depth `<=6` | 3..6 | `1,5,11,19` / `8,40,76,148` |
| **ARM-C** renewal-to-renewal | inside ARM-B | renewal 0,1,2 | `1`, `8`, `8` |
| **ARM-C2** renewal-to-renewal, non-degenerate | 4,096 depth-9 histories, conditioned | renewal 1,2,3 | `1,1,1` / `8,8,8` |
| **ARM-D** pool control | (A,B,C) transport, 50,617 histories, depth `<=4` | 0..4 | `1,7,22,51,120` |

ARM-B conditions on a **past** event only — that the depth-3 prefix ends
in a pair-arbitration — with the initial distribution taken as the
horizon-6 measure's own conditional, so no future information enters.
ARM-C2's conditioning is on a future event and is declared as such
(§5.5).

### 5.4 The censuses, both ways

**ARM-A, winner-invisible map.**

| triple | verdict | instrument | detail |
|---|---|---|---|
| `(0,*,*)` ×10 | VACUOUS | — | first cut carries one configuration; **first cut IS a division event** |
| `(1,2,3)` | **INDIVISIBLE** | exact LP infeasibility, Farkas verified | 209 vars × 106 rows |
| `(1,2,4)` | DIVISIBLE | exact LP feasibility, interpolant exhibited | 352 vars × 171 rows |
| `(1,2,5)` | DIVISIBLE | exact LP feasibility, interpolant exhibited | 594 vars × 281 rows |
| `(1,3,4)` | **INDIVISIBLE** | exact LP infeasibility, Farkas verified | 608 vars × 179 rows |
| `(1,3,5)` | DIVISIBLE | reduced LP feasibility, interpolant lifted and re-verified | 1,026 → 342 vars |
| `(1,4,5)` | **INDIVISIBLE** | reduced LP infeasibility, Farkas verified | 1,728 → 443 vars; **row certificate clean** |
| `(2,3,4)` | **INDIVISIBLE** | row certificate, Farkas verified | **12 of 32** target configurations admit no non-negative row |
| `(2,3,5)` | **INDIVISIBLE** | row certificate, Farkas verified | **14 of 54** |
| `(2,4,5)` | **INDIVISIBLE** | row certificate, Farkas verified | **12 of 54** |
| `(3,4,5)` | **INDIVISIBLE** | row certificate, Farkas verified | **13 of 54** |

**Census: INDIVISIBLE 7, DIVISIBLE 3, VACUOUS 10.**

**ARM-A, payload-enriched map.**  INDIVISIBLE 5 — `(1,2,3)` by full LP
infeasibility (481 vars × 198 rows), and `(2,3,4)`, `(2,3,5)`, `(2,4,5)`,
`(3,4,5)` by row certificate with `6/97`, `4/185`, `18/185`, `24/185`
obstructed rows.  DIVISIBLE 5 — `(1,2,4)`, `(1,2,5)`, `(1,3,4)`,
`(1,3,5)`, `(1,4,5)`, each with an exhibited and re-verified
column-stochastic interpolant.  VACUOUS 10.

**The two maps oppose, at exactly two triples, in the artefact
direction.**  `(1,3,4)` and `(1,4,5)` are INDIVISIBLE under
`alpha_sigma` and **DIVIDE** under `alpha_sigma+`.  Every opposition has
the same sign: the coarser map calls the triple indivisible, the finer
map exhibits an interpolant for it.  That is the direction in which
indivisibility is an artefact of discarding information rather than a
property of the process, and it is why no anti-artefact conclusion is
drawn from the two-map comparison anywhere in this note (§10, AG2).

**ARM-B.**  Winner-invisible: 3 vacuous (the renewal cut carries the
single root configuration) and `(4,5,6)` divisible by
Chapman-Kolmogorov.  Enriched: `(3,4,5)` and `(3,4,6)` divisible by
Chapman-Kolmogorov, `(3,5,6)` divisible on the reduced system, `(4,5,6)`
**indivisible** with 64 of 148 rows obstructed.

*What ARM-B's window can and cannot compare.*  It runs three steps past
the division event, so ARM-A's triples beginning at relative depth `>= 2`
would need depths 5,6,7 and are beyond the cap.  ARM-A's two indivisible
triples that begin at relative depth **1** — `(1,2,3)` and `(1,3,4)` —
do have their post-renewal analogue inside the window: it is ARM-B's
`(4,5,6)`.  It **divides** under the D62-faithful map, with exact
Chapman-Kolmogorov, and is **indivisible** under the payload-enriched
one.  So the one comparison this arm can make is map-dependent, and for
the coarse map it points in the artefact direction.  Both readings are
printed and neither is preferred.

**ARM-C.**  The mass reaching a second renewal inside the ARM-B cap is
`1/257`.  Conditioned on that, the renewal-2 configuration distribution
is the **same** from all 8 renewal-1 configurations: the
renewal-to-renewal transfer is rank-one, `R^2 = R`.  The triple
`(0,1,2)` is structurally vacuous under the winner-invisible map at
every reachable cap, because renewal cut 0 is the root.

**ARM-D (three actors).**  Supports `1,7,22,51,120`.  INDIVISIBLE 2 —
`(1,2,3)` on the reduced system (1,122 → 154 vars, Farkas verified) and
`(2,3,4)` with 18 of 120 obstructed rows.  DIVISIBLE 2 — `(1,2,4)` and
`(1,3,4)`, interpolants exhibited.  VACUOUS 6.  No verdict rests on a
two-actor accident, and none rests on a cap.

**The whole census, all arms, both configuration maps: INDIVISIBLE 15,
DIVISIBLE 15, EXCLUDED-BY-CAP 0, VACUOUS 30.**  Restricted to the four
depth-indexed arms (i.e. excluding ARM-C2): **INDIVISIBLE 15, DIVISIBLE
14, EXCLUDED-BY-CAP 0, VACUOUS 29.**

**The double count, carried with the number.**  "Fifteen indivisible"
counts *verdicts*, and the same (arm, window) read by the two
configuration maps is counted twice.  The distinct `(arm, window)` pairs
behind the fifteen are **10**, and the distinct cut triples **8**.  The
thirty vacuous verdicts stand on **20** distinct `(arm, window)` pairs.
The caveat travels with the headline number everywhere it appears.

### 5.5 ARM-C2 — the pinned renewal-to-renewal triple, run

The cut triple is `(renewal 1, renewal 2, renewal 3)`: three division
events, the grain paper 0 §4 places the law at, with a first cut that is
**not** the root.  Depth 9 is not enumerated — the two-actor transport
family has of order `10^8` histories there.  It is reached by
**conditioning**, and the conditioning is what makes it exact rather
than sampled.

- At horizon `D` the relative-horizon leaf measure telescopes:
  `P(leaf) = prod_t q_t / G(root, D)`, because `G(leaf, 0) = 1`.  The law
  *conditioned* on any set of depth-`D` leaves therefore needs only those
  leaves' raw weight products; the normaliser cancels.  No sampling and
  no truncation.
- A pair-arbitration needs two proposals in its ckey.  At a renewal the
  ported state is the root, which carries **no live operations**
  (gated: C2a).  So a renewal three events after a renewal forces the two
  intervening events to be proposals, and the depth-9 leaves carrying
  renewals at 3, 6 and 9 are enumerable **exhaustively**: 16 renewal-1
  bases → 256 renewal-2 histories → **4,096 renewal-3 histories**, raw
  mass `1/32768`.

**Result.**  Under the winner-invisible map all three renewal cuts carry
the single root configuration and the triple is structurally vacuous.
Under the payload-enriched map the supports are `8, 8, 8` — the first
cut carries **eight** configurations, which is exactly what makes the
test non-degenerate — and **Chapman-Kolmogorov holds exactly**: the
triple is **DIVISIBLE**, the process's own renewal-to-renewal conditional
interpolates it, and both `Gamma(r2<-r1)` and `Gamma(r3<-r1)` have a
single distinct column, so the renewal transfer is rank-one and
`R^2 = R`.  The renewal chain forgets its configuration in one step.

**The declared boundary, and the successor.**  Conditioning on a third
renewal by depth 9 forces every renewal interval to its shortest length,
so this is the **minimal-interval** sub-ensemble — the same
future-conditioning ARM-C declares, one renewal further on.  A renewal
chain with **unequal** intervals is reached neither by this conditioning
nor by enumeration at this cap.  That is the named successor computation,
**U1b**, and it is the only part of the pinned question this receipt
leaves open.

### 5.6 The `[B3]` eq. 22 algebraic arm, and exactly how weak it is

Barandes' eq. 22 needs a square `Gamma`, i.e. his kinematical axiom: one
fixed configuration space for all cuts.  This carrier has none away from
renewals (§2).  The arm is run under a declared convention — the
configuration space is the union `X` of the three cuts' supports, and a
configuration not yet realised at a cut is held fixed by the law (an
identity column) — which makes every `Gamma` square.  Exact rational
inversion; every column sum of `Gammabar` verified to be exactly 1.

**Census: pseudo-stochastic 13, stochastic 7, singular 0, excluded 0;
1,103 negative entries counted exactly.**  That count is **relative to the
identity-padding convention** and is not an invariant of the process: a
different padding gives a different count, and the number is quoted with
its convention everywhere it appears, including §1.  Representative
most-negative entries: `-1/584` at `(0,3,4)`, `-66/12593` at `(1,2,3)`,
`-5528/518885` at `(2,3,4)`, `-60454377/7356440080` at `(3,4,5)`.

Cross-tabulated against the feasibility verdict:
`PSEUDO-STOCHASTIC / INDIVISIBLE` 7, `PSEUDO-STOCHASTIC / DIVISIBLE` 3,
`PSEUDO-STOCHASTIC / VACUOUS` 3, `STOCHASTIC / VACUOUS` 7.

**The gap is exhibited in one direction only.**  There are triples where
the algebraic reading is pseudo-stochastic while a genuine stochastic
interpolant provably exists — counting negative entries in `Gammabar` is
therefore *not* the same test as asking whether the process divides, once
the configuration space is not fixed.  The converse cell,
`STOCHASTIC / INDIVISIBLE`, is **empty on this census**: nothing here
exhibits the algebraic reading missing an indivisibility, so no
two-directional claim is made.  The `PSEUDO / VACUOUS` and
`STOCHASTIC / VACUOUS` cells are a **cap-and-degeneracy consistency
observation and not evidence of anything**: a vacuous triple divides for
a structural reason that has nothing to do with eq. 22, and it is listed
only so the cross-tabulation adds up.

## 6. The null — the coarse-graining control battery

Every verdict in §5 is a verdict about a coarse-graining of a **divisible
click law**, and the question a census cannot answer about itself is how
much of the result is the *record* and how much is coarse-graining as
such.  The battery answers it: same family, same horizon measure, same
cuts, same instrument, four control maps with the record content removed
and the granularity kept.  The comparison is on the row-certificate
count — obstructed target configurations — because that is the one number
all six maps can be scored on at the same cost.

**The shuffle is printed, not seeded from the clock:**
`x <- (1103515245 x + 12345) mod 2^31`, seeds `20260727` and `11`,
Fisher-Yates over the `sk()`-sorted prefix list, the shuffled list then
cut into blocks of `alpha_sigma`'s own class sizes at that depth.  No
call to any random module; no dependence on the hash seed or the clock.

| map | supports 0..5 | `(1,2,3)` | `(2,3,4)` | `(2,3,5)` | `(2,4,5)` | `(3,4,5)` |
|---|---|---|---|---|---|---|
| **`alpha_sigma` — the record map** | `1,5,11,19,32,54` | 0/19 | **12/32** | **14/54** | **12/54** | **13/54** |
| full prefix (finest, Markov) | `1,8,60,452,3448,26760` | 0/452\* | 0/3448\* | 0/26760\* | 0/26760\* | 0/26760\* |
| **random partition, seed 20260727** | `1,5,11,19,32,54` | **10/19** | **28/32** | **40/54** | **42/54** | **54/54** |
| **random partition, seed 11** | `1,5,11,19,32,54` | **9/19** | **30/32** | **42/54** | **39/54** | **54/54** |
| kinematic tag multiset | `1,3,7,12,19,28` | 0/12 | 5/19 | 3/28 | 9/28 | 9/28 |
| actor sequence | `1,2,4,8,16,32` | 0/8\* | 0/16\* | 0/32\* | 0/32\* | 0/32\* |

`*` marks a triple where Chapman-Kolmogorov holds exactly, so the
process's own conditional already interpolates and the triple divides.

- **The pipeline's own sanity check passes** `[GATE N1]`: under the
  finest map — `alpha(h) = h`, for which the law is a chain rule —
  Chapman-Kolmogorov holds **exactly** at every test triple and every
  triple divides.  Every indivisibility this receipt reports is therefore
  a property of a coarse-graining and of nothing else.
- **The null out-scores the record map** `[GATE N2]`: a uniformly random
  partition into `alpha_sigma`'s own class sizes — zero record content,
  identical granularity — is obstructed on **more** target
  configurations than `alpha_sigma`, at both seeds — **174 against 51**
  summed over the five test triples, and 54/54 against 13/54 at
  `(3,4,5)`.  Indivisibility at
  cut grain is what coarse-graining a divisible chain generically does,
  and the record map holds the property **less strongly** than noise of
  its own granularity.
- **The lumpable end of the scale divides.**  The actor-sequence map is
  lumpable on this family — Chapman-Kolmogorov holds exactly at every
  test triple — and every triple divides, which is the textbook
  implication run as a control rather than assumed.  The kinematic
  tag-multiset map is obstructed at 4 of the 5 test triples, so a map
  that reads the grammar and carries no record at all is not
  systematically weaker than the record map either.

This is the direction opposite to a bridge headline, and it is the reason
this unit's verdict is scoped rather than asserted.  It is also
`[B3]`'s own position: Barandes takes **unistochasticity**, not
indivisibility, as the quantum criterion — indivisibility per se is
generic for classical coarse-grainings, which N2 measures directly.  The
unistochasticity screen is U3's and is reported unadjudicated in §3.

## 7. The division-event table

`[B3]` p.9 admits conditioning **only at division events**, and paper 0
§4 identifies division events with renewals.  The census of §5 is
therefore two censuses, and only one of them is the law's own.  A triple
is **division-event-conditioned** iff its first cut is a division event
for *every* history of its ensemble: the initial cut, where the process
sits at the root by construction; ARM-B's cut 3, where the ensemble is
conditioned on a pair-arbitration at depth 3; and ARM-C2's renewal cuts.

| first conditioning cut | INDIVISIBLE | DIVISIBLE | EXCLUDED-BY-CAP | VACUOUS | total |
|---|---|---|---|---|---|
| **IS a division event** | **0** | 4 | 0 | 30 | 34 |
| **is NOT a division event** | **15** | 11 | 0 | 0 | 26 |

The split is total.  **At a division-event conditioning cut there is no
indivisible triple at all.**  The winner-invisible readings are
structurally vacuous there for a structural reason — a renewal resets to
the root, so the first cut carries one configuration — and every
non-vacuous one divides, two of them by exact Chapman-Kolmogorov, with
the pinned renewal-to-renewal triple of §5.5 among them.  Every
indivisible triple in this receipt has its first cut strictly *between*
division events: that is cut grain, not record grain.

## 8. Arm 1 (c) — the geography, as input to U2

**The 44 descent-obstruction squares are named first and in full in the
receipt** (`u1_output.txt`, block `[A1-PRIME]`), each with its base
history, both events, the exact four step weights and the ratio.  Their
base-depth census is `{1: 4, 2: 40}`; all 44 carry kinds `(r,d)` and
ratio `1/2` forward.  D74's committed `44 + 44` split reproduces exactly
(menu quotient 113 classes, coarsest congruence 185, both closing the
same 44), and so does ABC3's `0 of 12`.

- **The indivisible windows are bridge windows.** The mass of the
  ensemble carrying **any** division event inside an indivisible window
  is `16/4173`, `16/1391`, `7/321` or `25/1391` — **the maximum is
  `7/321` = 2.18% exactly**, so the bridge mass is **at least `314/321`
  = 97.82%** of every indivisible window and no larger
  claim may be made.  This is a **measured co-location** offered as U2's
  input; the J-conjecture is not tested here.
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

## 9. Arm 2 — the four descent conditions, on the same family at the same caps

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

**DC2 — boundary sufficiency.** Fails, as §1 records — and it is the same
non-lumpability the interpolant census reads at window scale, not a
second finding.  This is the sharpest single difference from closed
scope, where DC2 is exactly (H1)+(H2) and is a theorem.

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

## 10. The agreement census

Arm 1's instrument is per-window; Arm 2's are per-step.  A triple
`(l0, l', l'')` is *Arm-2 defective* iff some DC1 or DC2 failure occurs
at a depth in `[l0, l''-1]`.  DC1 failures by parent depth: `1: 4`,
`2: 84`, `3: 872`.  DC2 failures by depth: `2: 4`, `3: 8`, `4: 12`.

| | Arm 2 DEFECTIVE | Arm 2 CLEAN |
|---|---|---|
| **Arm 1 INDIVISIBLE** | **7** | **0** |
| **Arm 1 DIVISIBLE** | **3** | 0 |

**Descent failure is necessary but not sufficient for
cut-indivisibility on this family.**  Arm 2 is defective on every window
of the family, including all ten vacuous triples, so at window scale it
has no resolving power; Arm 1 resolves.  The witness class that would
have made this a genuine **U1-SPLIT** — an indivisible triple in a clean
window, putting the instruments in opposite directions on one object — is
**empty, 0 of 10**.  Because both instruments read the same
non-lumpability fact (§1), this containment is the relation between two
readings of one thing and not two agreeing measurements.

**AG2 — the two configuration maps.**  They **oppose on 2 of the 20**
ARM-A triples, at `(1,3,4)` and `(1,4,5)`, and every opposition is
coarse-INDIVISIBLE / fine-DIVISIBLE — the artefact direction.  No
anti-artefact reading is available from this comparison and none is made;
in particular, the two opposed triples are exactly the two the plain LP
cap cannot reach, so a cap-limited census would read as agreement for the
wrong reason.

## 11. What this does and does not say

- **It is not a CP-divisibility test.**  (D1)–(D4) are statements about
  factorisation of column-stochastic matrices.  No completely positive
  map, no divisibility of a dynamical map on operators, and no CP
  criterion of any kind appears anywhere in the receipt.
  CP-divisibility and Barandes-indivisibility are orthogonal axes and
  this unit does not cross them.
- **No Bell or locality claim is made or implied.**  Bell is settled and
  closed; indivisibility pays the outcome-independence price and buys no
  locality result.  Nothing here is framed as one.
- **Indivisibility is not claimed to be a quantum signature.**  `[B3]`'s
  criterion is unistochasticity, not indivisibility, and §6 measures
  directly why: a random coarse-graining of the same granularity is
  *more* obstructed than the record map.
- **No resource-theoretic advantage is claimed.**  Magic `!=`
  indivisibility.
- **No exact covariance is claimed anywhere**, per L-1: at renewal grain
  the configuration space is fixed and finite, which is precisely the
  hypothesis under which exact covariance by invertible stochastic maps
  forces permutations.  At most statistical Lorentz invariance is
  available there, and this unit claims none.
- **The indivisibility that survives is of the cut-grain reading, not of
  the record law.**  v10's per-click law is divisible on histories by
  construction — it is a chain rule, and §6's finest map re-verifies it.
  What §5 measures is what that same process looks like read through a
  coarse configuration map at cuts the law does not condition at.  At the
  cuts the law *does* condition at, it divides (§7, §5.5).
- **Nothing is claimed at infinite volume**, and no measure-existence
  claim is made: D70's bound is open and this unit does not touch it.

## 12. Scope

Transport scope (d42b1) only; the declared families and caps only:
(A,B) depth `<=5`, the renewal-started window to depth `<=6`, (A,B,C)
depth `<=4`, ARM-C2's conditioned depth-9 minimal-interval sub-ensemble,
D72/D74's own anchor windows at depth `<=4` and `<=3`, closed scope to
depth 6, DC1 parents to depth 3.  Exact rational LP caps 700 variables /
400 constraints on the full system and 5,000 / 1,200 on the reduced one;
**the row certificate is sufficient and not necessary for
indivisibility, so a cap can hide an indivisible verdict as easily as a
divisible one** — which is why every triple here is decided on a system
and none is left to the row certificate alone.  The eq. 22 algebraic arm
runs on fixed configuration spaces of size `<=100` under a declared
identity-padding convention, and its negative-entry count is relative to
that convention.  Renewal grain per paper 0 §4's `[POSIT]`, which PORT-3
shows is delivery-conditioned rather than grammatical.  The
renewal-to-renewal interpolant test is **run** at minimal intervals
(§5.5) and **not run** for unequal intervals (U1b).  No infinite-volume
claim; no measure-existence claim; no CP, Bell, locality or covariance
claim.  The J-conjecture is not tested — that is U2.  The
unistochasticity screen is reported and not adjudicated — that is U3.

## 13. Owed forward corrections, named and routed

PORT-3's constructed chain refutes, **at transport scope**, two paper-0
lines that are imported from closed scope without a scope tag.  The
paper-0 edit is not this unit's to make; the loci are named here so the
Phase-I-end pass can make it.

- **`relativistic-isp-v11-paper0-the-indivisible-record-law.md:136`,
  `[THEOREM]` "Every pair-arbitration returns the serialized state to the
  root".**  True at closed scope (D62 row R4; PORT-1, `2032/2032`) and
  true in-family at transport scope at every reachable cap (PORT-2,
  `1264/1264`).  **False in general at transport scope** (PORT-3).  The
  line needs a scope tag; the theorem itself is untouched at its own
  scope.
- **`…:143`, `[THEOREM-GRADE CONVERGENCE]` "the configuration space at
  division events is small, fixed, and identical across runs".**  Its
  premise is :136's corollary, so it inherits the same scope condition:
  it is a delivery-conditioned property of the transport grammar, not a
  grammatical one.
- **The `[POSIT]` at `…:139` is not what PORT-3 hits.**  "Division events
  are the renewal events" is a definitional choice and stands; what
  fails is the imported guarantee that the renewal-grain configuration
  space is fixed.  The correction belongs at :136 and :143 and nowhere
  else.

## 14. Handover

- **To U2 (the J-conjecture):** the 44 named descent-obstruction squares
  with full step weights; the `604 / 356` split at the depth-5 window;
  the bridge-mass geography of every indivisible triple (division-event
  mass at most `7/321` = 2.18%, i.e. bridge mass at least
  `314/321` = 97.82%); the lumpability defect by depth; and
  the measured containment "descent failure `=>` nothing,
  cut-indivisibility `=>` descent failure", which is the shape any weld
  must respect — with §1's warning that the two instruments read one
  fact.
- **To U3 (the minimal quantum record):** `{V_single, V_pair}` in exact
  `Q(sqrt 2)` with defect 0 and Born `= K1`; the `6x6` `Zhat` transfer
  with its column sums `25/28, 1, 59/64, 55/64, 31/32, 19/14` — the
  doubly-stochastic screen, reported, unadjudicated.  §6 sharpens why
  this screen and not indivisibility is the criterion to press.
- **To U4 (sparse records on the crystals):** PORT-1/2/3 — the renewal
  predicate ports, the reset holds at every reachable cap and fails on a
  constructed admissible chain; the renewal sublattice's configuration
  space is `{root}` winner-invisibly and 8-element with payload; the
  renewal transfer is rank-one with `R^2 = R` at two consecutive
  renewals; and L-1's bound already applies to it.
- **To U1b (the named successor):** the renewal-to-renewal triple with
  **unequal** renewal intervals.  ARM-C2 decides the minimal-interval
  case exactly and it divides; the unequal-interval case is reached
  neither by ARM-C2's conditioning nor by enumeration at depth 9
  (of order `10^8` histories).  It is the only part of the pinned
  question left open, and it is the decisive one for whether the record
  law divides at its own grain in general.
