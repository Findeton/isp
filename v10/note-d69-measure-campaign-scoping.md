# D69 — THE MEASURE CAMPAIGN: the walls, the assets, the routes (SCOPING SURVEY)

**Status: SURVEY / SCOPING NOTE, 2026-07-27.  NOT a pin, NOT a receipt,
NOT a result.**  Nothing below is new evidence; every number is quoted
from a committed receipt or a terminal note and is attributed by file
and gate.  The one forward-looking object here is §5, which is a
**draft pin** offered for the principal to freeze, amend or discard.

**Campaign opened at LOG #481** (the frontier synthesis): *"we have a
space-MAKING mechanism (engineered, not emergent); dimensionality is
unselected (k is a dial); grid typicality is UNPOSABLE without a
measure; the quantum layer is excluded at proven scope.  ALL FOUR are
the same missing object — A MEASURE AT TRANSPORT SCOPE — the thing B1's
walls proved cannot be built the naive way.  The next campaign is the
measure itself, attacked from what B1 left standing."*

This note's whole job is to make **"what B1 left standing"** exact.

**Provenance labels used here** (book §0.1 convention): `[THEOREM]` /
`[EXACT]` = argued depth-free and gated; `[MEASURED]` = true on a
declared finite window, never a premise; `[OPEN]`; `[MY READING]` =
this note's inference, load-bearing on nothing.  Where the corpus is
ambiguous the note says so in place rather than resolving it.

---

## §1. THE WALLS, EXACT

Five distinct negative results bear on a transport-scope measure.  They
are of **three different evidential grades**, and the campaign will
mis-plan if they are quoted at one grade.

### 1.0 Standing of the sources, first

| wall | source | grade | committed as |
|---|---|---|---|
| W-A the self-arbitration ladder | `note-d56-transport-sigma-probe.md` §4; `v10/code/d56_transport_sigma_probe.py`; LOG #432 | `[EXACT, depth-free]` | **PROBE / ADVISORY** — no pin, no ledger unit, "nothing here is citable" (its own §0 banner, caveat C6).  The **two load-bearing claims were independently re-verified against the committed layer by the principal before acceptance** (LOG #432: "both reproduce exactly").  Book §B9 carries the same banner. |
| W-B menus run on per-actor views | same probe, §1.2 / M2 | `[MEASURED, depth ≤ 5]` | same |
| W-C sector-exact at `(actor, type)` | `v10/code/d57_sector_exact_refinement.py`, gates **S2 / S3 / S4**; `note-d57-sector-exact-pin.md`; LOG #436 | `[MEASURED, caps 3–6, counts are lower bounds]` | **pinned unit, batch-round reviewed and repaired**; one of its two published grounds **withdrawn** in that round |
| W-D no menu-shape transfer | D44b TERMINAL, LOG #374; paper 32 §2.3 | `[MEASURED]` | pinned, terminal |
| W-E the intrinsic chain escapes its windows | D44b TERMINAL, LOG #374 | `[MEASURED, at the feasible caps]` | pinned, terminal |

> **The asymmetry that must be carried at every citation.**  W-A is an
> **exact, depth-free obstruction** from an **advisory probe**.  W-C is a
> **measurement over reachable depths** from a **reviewed unit**.  The
> book states this explicitly (§A9.4, §B9.4b): *"the sector-exact escape
> is closed on measured evidence at this granularity, not by an
> obstruction."*  Neither may be upgraded to the other's grade.

---

### 1.1 W-A — THE SELF-ARBITRATION LADDER `[EXACT, depth-free]`

**Construction** (`note-d56` §4, book §B9.1).  `v_0 = genesis`; rung
`k+1` is `('p','A',v_k,0)` followed by the blind self-arb
`('r','A',{(A,v_k,0)},{(A,v_k,0)})`, minting
`v_{k+1} = vname(v_k, {(A,v_k,0)}, 'A')`.

Mechanically verified in the committed layer for `k = 1..10`:

| rung | `|holdings(A)|` | delivery options | weight each | sector total |
|---|---|---|---|---|
| 1 | 2 | 2 | `1/8` | `1/4` |
| 2 | 3 | 3 | `1/12` | `1/4` |
| 3 | 4 | 4 | `1/16` | `1/4` |
| … | … | … | … | … |
| 10 | 11 | 11 | `1/44` | `1/4` |

The induction is depth-free: `v_{j+1}` has strictly greater nesting
depth than `v_j`, so `v_0..v_k` are pairwise distinct; `A` proposed in
every rung's component key so `holdings(A) ⊇ {v_0,…,v_k}`; only
`v_0..v_{k−1}` are superseded, so the next propose is admissible; and
**`deliver_options_in_view` enumerates over the WHOLE holdings set**,
superseded members included (source, `v10/code/d42b1_transport_exact.py`:
`sorted(((r, v) for r in actors if r != a for v in view.holdings(a)), …)`).

> **THE WALL, verbatim (`note-d56` §4; book §B9.1):** *"No bounded
> menu-exact local-state abstraction exists at transport scope, for any
> design.  D52's T2 is answered: BLOW-UP, and by an obstruction, not by
> a growth curve."*

**Exactly what design space this kills.**  Any map `sigma : histories →
S` with `|S| < ∞` such that `sigma(h)` determines `menu(h)` as a
**renamed event multiset with exact weights**.  The proof is a
cardinality argument: menus take infinitely many values in their
cardinality *and* in their multiset of rational weights, and no renaming
moves either.

**Exactly what it provably does NOT kill** (the probe's own caveat C1,
reproduced in book §B9.5, and §A9.5's closing paragraph):

1. **Sector-level descriptions** — aggregated bookkeeping (this is what
   W-C then attacks at *one* granularity, and only one).
2. **Lumped chains** — and the probe *measured* two positive
   lumpability facts (§1.3 below).
3. **Level-structured descriptions — QBD / R-matrix / Martin-boundary**
   — named by the probe's §7 G6 as the alternative to Perron, with
   `|holdings|` as the level.
4. **Anything that is not a bounded abstraction at all.**  A measure is
   a function on histories or on record cylinders; the wall is about
   **finite summaries that reproduce menus**, which is a property the
   Perron *method* needed and a measure as such does not.  Book §B9.6
   states the cost in exactly this form: *"the method that settled the
   dichotomy at d42a — finite menu-exact quotient + Perron — provably
   cannot transfer"*; and §A9.5: *"What this chapter does NOT claim:
   that the delivery-scope theory has no tractable description."*
5. **Inexact abstractions** — anything that reproduces less than the
   full weighted menu.

**Width stability of the wall** `[MEASURED, SAMPLED]`: at three actors
the ladder has `(n−1)·|H|` delivery options — **4, 6, 8, 10, 12** at
`1/16, 1/24, 1/32, 1/40, 1/48`, **sector total exactly `1/4`
throughout**.  Sampled arm: 200 deterministic walks to depth 10, seed
`20260726` printed; sampled counts are **lower bounds only**.

**The wall's one un-audited joint** (probe caveat C3, binding): the
**join-view lattice completeness** — that every view `admissible()`
builds is the join of its actors' own views — is `[MEASURED to depth 5]`,
**0 exceptions over 243,768 candidate views**, with the *arb-renewal
register* escape identified as a real structural possibility that this
window did not exhibit.  **A pinned unit must rule it out or add those
views.**  This does not touch the ladder (which needs no lattice), but
it touches every `sigma` built on top.

---

### 1.2 W-B — MENUS RUN ON PER-ACTOR VIEWS, NOT ON THE WORLD `[MEASURED]`

The design the probe was *instructed* to use — D51's four projections
(`holdings`, `superseded`, `live`/`props`, `components()`) on the FULL
view — was implemented verbatim as `sigma(mode='full0')` and **refuted**:
**3,656 violations over 30,454 equal-sigma pairs** (probe M2).

Named witness (probe §1.2; book §B3.3, §B9.2):

```
W1 = [ p(B,v0,1), selfarb(B) ]
W2 = W1 + [ d(B→A, v0) ]
```

Identical full-view four projections — the delivery moves no holding,
mints nothing, supersedes nothing.  It moves only **who knows**.  Menus
differ: `('n','A')` `1/2 → 3/4`; `('p','A',w0,0/1)` `1/8 each → absent`.

> **`[MEASURED]` D51's four-projection reduction does not lift to
> transport scope.  Any pinned unit that reuses it will be measuring a
> non-object.**

**What this kills:** every world-state (as opposed to knowledge-state)
abstraction at transport scope.  **What it does not kill:** the
join-view lattice replacement, which *is* menu-exact on the whole
depth-5 family (**0 violations / 30,188 pairs over 541 classes**), with
transition determinism gated (**1,540 (state, event) pairs over 30,728
transitions, depth ≤ 4 exhaustive, 0 nondeterministic**).  So the
refined object exists and is correct — it is merely **infinite**, which
is W-A's business, not W-B's.

**And the trap this table sets, gated as a correction** (probe M1, §5;
book §B9.3): `cumulative == per-depth` does **not** mean "no state ever
recurs" — the per-depth sets are **nested** (appending `('n',a)` changes
no projection), so recurrence is **total**.  D52's published reading was
**backwards** and is forward-corrected.  Only the NEW column informs:
`1, 4, 12, 44, 130, 350, 1026` (×≈2.9, no turn-over).  BFS with a
printed cap of 20,000 states / 480 s: `5, 17, 61, 191, 541, 1567, 4679,
14413, 20000 (CAP)` at level 9, **5,587 unexpanded frontier states**.

---

### 1.3 W-C — SECTOR-EXACT AT `(actor, type)` GRANULARITY `[MEASURED]`

Receipt `v10/code/d57_sector_exact_refinement.py`, **3 PASS / 0 FAIL**,
exit 0, caps 3/4/5/6 **exhaustive** (**521 / 3,969 / 30,729 / 243,769**
histories).  The pinned question (`note-d57-sector-exact-pin.md` §1):
does the **coarsest** partition `R` of histories on which the aggregated
transfer `T_s(h,c) = Σ{ q(e|h) : e ∈ s, class(h+e) = c }` is
class-determined stay finite?

**Ground (2), the surviving ground — gate S2.**  Per-depth fixpoint
counts across caps, read as **lookahead convergence** (the first run's
"any growth is blow-up" reading was too crude and was corrected in
round; the decider as implemented is *"for every depth carrying at least
three cap values, do the LAST TWO cap values agree?"*):

| depth | cap 3 | cap 4 | cap 5 | cap 6 |
|---|---|---|---|---|
| 3 | 7 | 16 | 16 | **17** |
| 4 | — | 9 | 23 | **27** |
| 5 | — | — | 11 | **33** |

Even depth 3 creeps at cap 6.  Gate **S3** exhibits the split (the pin
had promised a witness and the committed first receipt had not supplied
one): a cap-5 class of double-digit membership splits at cap 6 — *"not a
marginal one-off"*.  Gate **S4**, the **trivial-boundary control**,
re-runs the whole refinement with the cap layer lumped into ONE class
and finds `cap-C-with-signature == cap-(C+1)-with-trivial` on every
shared depth, so **both truncations UNDER-refine** and the printed
counts are **LOWER BOUNDS** — *"observed growth is genuine growth, and
the blow-up reading is the CONSERVATIVE one."*

> **VERDICT (LOG #436, book §B9.4b): the sector-exact escape, AS PINNED
> (sector = `(actor, event-type)`), is CLOSED — on ONE ground, at caps
> 3–6, with the counts as lower bounds.**

**Ground (1) — SECTOR QUANTIZATION — WAS PUBLISHED AND IS WITHDRAWN.**
The first published verdict also claimed the **sector alphabet is not
finite** (totals in `{k/(4m)}`, `m` = component count, growing with
depth).  The round refuted the inference: the arbitration denominator is
`|comps| + |merge_pairs|`, and in the unit's own exhaustive data
**`max |comps| = 1` at every depth**, while at two-actor scope
**`merge_pairs ≤ 1` is proven** — so the observed `{1/2, 1/4, 1/8}`
**may be the complete alphabet**.

> **`[OPEN]` The finite-alphabet prerequisite is NOT refuted at this
> scope.  What is refuted is the claim that it fails.**  And the
> corollary: the `1/4` delivery-sector constant of W-A is a fact about
> the **delivery** sector, not a law of sectors (book §B9.4, glossary
> entry *sector*).

**Exactly what W-C kills:** finiteness of the **coarsest** lumpable
partition **for the sector map `s = (initiator, event-type)`**, on the
two-actor family at caps 3–6.

**Exactly what it does NOT kill** (the unit's own residue list, LOG
#436, book §B9.4b): *"(i) coarser aggregations (type-only sectors;
total-budget-only) — untested; (ii) abstractions that give up exactness
for the completion's OBSERVABLE demands only."*  Named residues:
**depth 7**; an **actor-swap quotient** (counts `≤ 2×`, so it cannot
rescue the trend alone).  Note that "coarsest" is coarsest **for a fixed
sector map** — a coarser *sector map* induces a different, coarser
coarsest partition, and W-C says nothing about it.  This is the single
most important scope clause in this section.

**The positive lumpability facts W-C does not touch** (probe §5,
`[MEASURED]`, depth ≤ 5 / ≤ 4):

* with `lump` = `sigma` with each holdings set replaced by
  `(non-superseded part, min(|holdings|, T))`, the **non-delivery menu
  factors through `lump` exactly** — `T=2`: 0 / 30,236 pairs; `T=3`:
  0 / 30,228;
* the **delivery-LUMPED step distribution** is a function of the lump
  state — **0 violations over 3,782 same-state pairs, 187 lump states**
  (probabilistic bisimulation on that window);
* and it still does not close: lumped BFS at `T=2` gives
  `1, 5, 17, 61, 187, 493, 1223, 3099, 8241, 20000 (CAP)`.

> **The probe's own summary, which the campaign should carry as a
> planning constraint:** *"killing the counter is NECESSARY and
> demonstrably NOT SUFFICIENT.  The residual explosion is the
> view-product structure"* — i.e. the per-actor knowledge lag, measured
> as the fastest-growing component at reachable depths (`live`/`comps`:
> 284 / 288 distinct values at depth 6, versus 123 for the version layer
> and 13 for the holdings counter).

---

### 1.4 W-D — NO MENU-SHAPE TRANSFER FROM d42a `[MEASURED]`

D44b TERMINAL (LOG #374), paper 32 §2.3, book §B6.14: **zero of the
3,969 transport menus match any delivery-free menu shape**.  Any
construction that hopes to import the d42a six-state chain or its menu
alphabet by shape-matching is dead on arrival.  Deliveries also **reopen
the absorbing sector**: 1,044 diverged histories, 124 reconverging
`(history, delivery)` pairs over 84 distinct diverged prefixes, 4
distinct minimal 3-event chains all at exact weight `1/256`; *"the d42a
absorption is a DELIVERYLESSNESS ARTIFACT."*

### 1.5 W-E — THE INTRINSIC CHAIN ESCAPES ITS WINDOWS `[MEASURED]`

Same unit: the intrinsic transport chain is window-consistent at six
`len ≤ 2` classes (*an ECHO of, not identical to, the d42a six*) but
**escapes** — 68 transitions from shallow parents land in 5 classes
first realized at length 3.  *"No closed exact transfer at the feasible
caps; the Perron branch live but unfired BY MEASUREMENT."*  W-A later
converted "unfired by measurement" into "impossible by obstruction" for
the menu-exact granularity only.

### 1.6 THE SCOPE LEDGER, IN ONE TABLE

| candidate object | killed? | by what | grade |
|---|---|---|---|
| finite menu-exact state summary, any design | **YES** | W-A | `[EXACT, depth-free]` |
| finite transfer matrix + Perron at transport | **YES** (corollary) | W-A | `[EXACT]` |
| full-view (world-state) abstraction | **YES** | W-B | `[MEASURED]` |
| finite coarsest lumping at sector = `(actor, type)` | **YES** | W-C | `[MEASURED, caps 3–6, lower bounds]` |
| finite lumping at **type-only** sectors | **NO** | — | untested |
| finite lumping at **budget-only** sectors | **NO** | — | untested |
| infinite chain with level structure (QBD / R-matrix) | **NO** | — | untested; machinery imported (D46b) |
| Martin-boundary / potential-ratio description | **NO** | — | untested as a *boundary*; kernels computed (D46b) |
| horizon-indexed (depth-graded) measures and their limit | **NO** | — | computed at ARM-1T caps (D46b, D46d) |
| regenerative / atom-based construction | **NO** | — | never posed |
| inexact, observable-demands-only description | **NO** | — | untested; the demands are not yet a defined list |
| a measure on record classes at transport scope | **NO** | — | untested at transport; exists as an object at d42a (D65) |
| finite alphabet of sector totals | **NOT DECIDED** | ground (1) withdrawn | `[OPEN]` |

---

## §2. THE ASSETS

What the closed-scope line hands any transport construction.  These are
**not** transferable results — every one of them is scoped to two-actor
delivery-free d42a unless stated — but they are the shapes to build
toward and the constraints to respect.

### 2.1 The boundary machinery: `sigma`, (H0)/(H1)/(H2), and the update table

`note-d61-h1-closure-result.md` + `v10/code/d61_h1_closure_exact.py`
(12 PASS / 0 FAIL); `note-d62-h2-update-table.md` +
`v10/code/d62_h2_update_table_exact.py` (24 PASS / 0 FAIL); book
§B6.13 / §B6.13b; LOG #455 → #460.

* **`[THEOREM, two-actor delivery-free d42a]` (H1):** equal canonical
  `sigma` ⟹ identical canonical menu.  Engine: the **own-view
  dichotomy** — a candidate's own view is either the initiator's
  register cone or the FULL view, no third case (34,374 transitions:
  cone 32,342, full 2,032, **third case 0**), which is a theorem of
  `regs_of` **together with** `arb_components_in_view`'s **proposer
  test**.
* **`[THEOREM, same scope]` (H2), the update table:** five rows
  R1/R2/R2′/R3/R4 partitioning the event alphabet by
  `(tag, base ∈ refs?, |proposers(ckey)|)` with no fall-through; every
  row a `[PROOF]` from a quoted line of the committed layer or a named
  lemma; **no step is an induction on depth and no step reads the
  history.**  Obligations O1 (dropped-base determinism, 9,656
  instances, 0 violations), O2 (mint non-collision — *excluded by
  admissibility, not by luck*; 44,356 admissible arbs, 0 collisions;
  49,964 adversarial re-mints all refused), O3 (Row 0,
  `comps(Σ) = f(live)`).
* **⟹ D44a's closure theorem is UNCONDITIONAL at that scope**; 36 states,
  176 transition keys; independently re-implemented with **0 mismatches
  on 4,778,310 transitions into depth 9**.

**What transport must supply in each slot, and where each breaks.**

| closed-scope ingredient | transport status |
|---|---|
| the own-view dichotomy (Lemma 2) | **breaks already at three actors** — the third case becomes admissible (5,904 views at depth ≤ 4), *"with only Lemma 2 breaking; the rigidity invariants survive"*.  The **proposer test is the load-bearing clause any successor must re-examine** (§B6.13, explicit). |
| `sigma` finite (36) | **impossible** — W-A |
| the five-row update | shape survives in principle (the rows are local), but there is no transport analogue built; **deliveries add a sixth species that moves only knowledge** (W-B) |
| **R4: every pair-arb is a RENEWAL to the root state** | **the single most reusable row.**  `hold = {A:v, B:v}`, `live = ()`, `comps = ()`, `refs = {v}`, `flag(v) = False` — serialisation-identical to `sigma([])`.  *"D44a's renewal/pumping structure is a ROW OF THE TABLE, derived rather than measured."*  See §3 R5. |
| the quarter law as a theorem of `G` | see §2.3 |

### 2.2 `Zhat`'s descent shape, and the repair-cone hierarchy

`note-d65-descent-conditions-result.md`;
`v10/code/d65_descent_conditions_exact.py` (39 PASS / 3 FAIL — the FAILs
are the pre-registered negative); book §B2.10; LOG #465 → #468.

* **`[EXACT]` `Zhat` genuinely descends.** `ker(T − 2I)` is
  one-dimensional with a **strictly positive** generator, values
  `{1, 4/3, 7/3}` at multiplicities `{29, 5, 2}` (= D49's
  `f = (4,4,3,7,3,3)/3`); `ker(T − I)` mixed-sign; `ker(T − 5/2 I)` and
  `ker(T − 9/4 I)` empty.  `Zhat(h) = 2^(−|h|) f(sigma(h))` has **zero**
  harmonicity violations, and `μ_Zhat = q·Zhat` is **constant on all
  5,548 record classes**.
* **The shape a transport analogue would have to have:** a positive
  `λ`-harmonic function of a *state*, times `λ^(−depth)`.  At transport
  there is no finite state — so the analogue must be a positive harmonic
  function on the **history tree**, i.e. exactly a **Martin-boundary
  object**, not a Perron eigenvector.  *(This is the corpus's own
  redirect: book §B9.6, probe §7 G6.)*
* **`[EXACT]` The hierarchy, and what selects the corpus's completion:**
  at the depth-4 truncation, repair cone **573** ⊃ repairs that also
  descend **205** ⊃ the `(depth, sigma)` family **28** ⊃ **one ray**
  (`Zhat`).  At `D = 5`: 3,053 / — / 32 / 1,138 record-constant; **the
  gap WIDENS with depth**.  *"The object that collapses 573 to 1 is
  D50's FORM choice, not descent."*
* **Two exact positive witnesses, both reconstructed in-receipt:** one
  **repairs every one of the 403 squares and does not descend**; one
  **descends and does not repair** — *a measure on refined record
  cylinders, constant on all 427 depth-≤4 record classes*.  **Neither
  property implies the other.**  The second witness is the existence
  proof that **record-level measures are a non-empty object class
  independent of the kernel** (relevant to §3 R8).
* **`[EXACT]` The descent defect is a coboundary:** the raw cocycle holds
  on **all 665,286** commuting pairs; the entire defect lives in the
  normalization and equals `M(sigma(Hb))/M(sigma(Ha))`, spectrum
  `{1, 4/5, 5/4}`, confined to 6 of the 36 states.  DC1's load-bearing
  census: **32,256 failures of 425,334** refined-record-identical
  ordered pairs.
* **Residue (2) is a binding warning for this campaign:** *"whether the
  defect's coboundary form survives beyond this scope … at three actors
  or with delivery the mass spectrum changes and the statement must be
  **re-derived, not carried**."*

### 2.3 The quarter law, the mass ladder, and their exact transport status

* **`[THEOREM at d42a scope]`** per-actor menu mass in `{1, 5/4}`,
  **derived** from the closed form `G` (propose `1/8`, self-arb `1/4`,
  pair-arb `1/8` in twos; blind groups summing exactly `1/4`), zero
  off-law points; and the totals are **`2` or `5/2`**, with `9/4`
  unreachable (§B6.13).
* **At transport, two-actor (ARM-1T)** `[MEASURED]`, D46b gate **MB1**:
  the per-history menu weight sum takes **exactly** `{2: 3757,
  5/2: 212}` across the whole ARM-1T family — *"the quarter-quantized
  ladder is NOT a deliverylessness artifact."*
* **At transport, `M` actors** `[MEASURED]`, D66 gate **A5**: the total
  sits at `M` at most prefixes and rises where an unarbitrated conflict
  group is visible — `RING(6,10)`: `{6: 87, 19/3: 3, 13/2: 27}`, excess
  in quarters `{0: 87, 4/3: 3, 2: 27}`.  **The `2 → 5/2` values are NOT
  reproduced and the bridge is explicitly not made.**  And the
  **per-actor ladder does not hold** — sums of `13/12` and `19/16` occur
  (d42b1's own declared **N1** leak: *"the general-depth ladder is FALSE
  under current pricing"*).
* **`[MY READING, load-bearing on nothing]`** the commensurable quantity
  across all three scopes is *the excess above the actor count, in
  quarters, counting visible conflict groups*.  Any transport measure
  will have this as its local mass function; it is **not** quantized on
  a ladder, and a construction that assumes quantization will be
  building on d42b1's known leak.

### 2.4 The transport-scope Martin/R machinery ALREADY BUILT

`note-d46b-martin-at-transport.md`, TERMINAL 2026-07-19 (LOG #384 →
#398 → #400, three round-1 reversals, delta CLEAN);
`v10/code/d46b_martin_transport_exact.py` (12 → 19 gates, 0 FAIL).
**This is the campaign's largest unspent asset and it is four months
old.**

* **The object:** relative-horizon potentials `G(h, r)` and kernels
  `k_r(e|h) = q(e|h)·G(h+e, r−1)/G(h, r)`.
* **MB4, both families to `D = 6`:** transport `G_D` = `257/32`,
  `1035/64`, `4173/128`, `134587/2048`; ratios `2.007812`, `2.013619`,
  `2.015942` (**peak**), `2.015741` (**down**).  **DELIVERIES REDUCE
  finite-horizon branching** (the first pass had this sign backwards).
  `λ = 2` is relabelled an **asymptotic Perron eigenvalue**, not
  comparable to finite-horizon ratios.
* **MB3, the pinned object:** the **sector-normalized conditional at the
  root has drift EXACTLY ZERO at `r = 1..6`**; off-root its sup
  contracts `1/18, 4/171, 8/741, 176/32877`; the **family-uniform sup**
  runs `3/110, 3/253, 373/69230, 2333/1838829`; L∞, L1 and sector-L∞
  give **exactly equal** sequences; the ratio sequence is
  `0.738, 0.399, 0.086` — **"not a rate"** (the note's own word).
* **MB5, reversed and gated:** **root = renewal DOES transfer at matched
  horizon** — a **necessary-not-sufficient** agreement, with the
  non-sufficiency censused (8,196/30,728 at `r = 1`; 1,060/3,968 at
  `r = 2`; 104/520 at `r = 3` histories share the root's masses).
* **Properness:** the kernel candidates are **proper at every COMPUTED
  relative horizon** — `r = 1..6` at the root, **`r = 1, 2` family-wide**.
* **MB6, binding:** *"no infinite-volume claim under any outcome (the
  caps bind; a horizon-stable kernel at `D ≤ 4` is a computed fact, not
  a boundary theorem)."*

**And the reading doctrine this machinery inherits (D44f, LOG #370):**
the absolute completed weights are **horizon-bound**; the
**horizon-stable forced object is the SECTOR CONDITIONAL** (at the join
fixture: `(1/2, 1/4, 1/4)`, identical at depth 4 and depth 5 while the
absolute `q'` differs).  **Two independent lines therefore point at the
same object**: D50's *"record-level observables are the AGGREGATED
ones"* (book §B6.12) and D44f/D46b's *"the horizon-stable object is the
sector conditional"*.

### 2.5 The typicality instrument, and its withdrawn premise

`note-d46d-typicality.md`, TERMINAL 2026-07-19 (LOG #398 → #400);
`v10/code/d46d_typicality_exact.py` (11 → 17 gates, 0 FAIL).

* An exact arm under the **LOOKAHEAD-COMPLETED** law and a sampled arm
  under the **LOCAL-NORMALIZED** law, **calibrated** at three printed
  anchors: `3457/9464832` (pool 4/depth 3), `1539/5646080` (pool 5/depth
  3), `5451/19210880` (pool 6/depth 3).  The calibration horn *"did NOT
  fire … and could not be made to grow."*
* **Its BLOCKER B2 is the campaign's charter:** *"'the theory's OWN law'
  is not established"* — the committed d42b1 docstring says **"NO
  MEASURE CLAIM"**, and the unit used two different normalizations.
  Withdrawn: *"every typicality statement must name the exact
  normalization it is taken under."*  **This is exactly the deficiency
  the measure campaign exists to remove.**
* **Its surviving content, which is the shape of the typicality
  frontier:** the discriminating scalings — at fixed depth 8 across
  pools 3–8 the full-width mass falls `0.963, 0.782, 0.568, 0.333,
  0.137, 0.037` (touched) and `0.525, 0.238, 0.105, 0.030, 0.005,
  0.003` (delivery-joined) — deliver *"what is typical-in-the-making is
  ORDER DIMENSION ≥ 3, not unbounded dimension"*, with width ≥ 4
  **necessary-not-sufficient** and therefore an **upper bound** on the
  dimension mass.
* **Method assets to reuse verbatim:** the exact/sampled separation as a
  gate; seeds and pools printed; three proxies side by side; and the
  round's lesson that **a monotone-by-construction statistic is not
  evidence** (touched-width is monotone in depth, so "width spreads with
  depth" *cannot fail*).

### 2.6 The grammar-side constraints any typical record must respect

These are `[THEOREM]`s about the **grammar**, independent of any
measure, and they are what a measure's typical records will be scored
against.

* **The conflict budget bound** `[THEOREM, verified; D66 §2]`: an
  arbitration's `ckey` is a set of `k` live proposal triples and no
  triple is consumed twice (the register argument closes the
  view-relativity gap), so `#proposals ≥ k·#arbs` and **the arbitration
  share of any record is at most `1/(k+1)`**, `k` the smallest proposer
  count.  Deliveries only lower it.  **Three readings, never merged**
  (glossary): the delivery-free ring saturates `1/3` at `k_min = 2`; a
  double grid's bootstrap makes `k_min = 1` so its own bound is `1/2`
  and is *not* saturated; its conflict share is a third number (`2/15`
  at `k = 4`).
* **W4c, the dead-wire refinement** `[THEOREM, proved from the committed
  layer]`: the version register an arbitration mints is a **dead wire**,
  so the operative branching factor is the **live** out-degree `Bl`, the
  bound is `|D_e(d)| ≤ Bl^d`, an arbitration branches by its **proposer
  count**, and *"3+ registers"* is corrected to **"3+ PROPOSERS"**.
  Depth-2 ceiling `k·Bl ≤ k²`, **realized at `k = 3, 4, 5, 6` — 9, 16,
  25, 36** (D67, LOG #476).
* **The width mechanism** (D67 gate **K3c**): width lives in the
  **arbitration order meeting a height condition** — same actors,
  lineages, events, **zero deliveries**, only the order changed, and
  width collapses **16 → 7**.  Height-levelling by the grammar's own
  `('n', a)` idle is the mechanism.
* **Uniformity survives width on a whole record** (D67): `DOUBLE-GRID(4,4)`
  — 200 events, forced, zero in-round deliveries — sits inside **both**
  `d = 3` sprinkling band columns (`0.7250` / `0.6350`) at
  `max |D| = 16`.

> **`[MY READING]` The measure's job, stated as a scorecard.**  A
> transport measure decides the four frontiers only if it can answer:
> what mass sits on records whose arbitration share approaches
> `1/(k+1)`; whether height-levelled schedules (the width mechanism) are
> typical or engineered; and whether `k` is selected or free.  None of
> these is posable today, and each is a *ratio of masses*, i.e. an
> **aggregated** observable — consistent with §2.4's convergence.

### 2.7 Method assets

Reusable, and each earned by a round: pre-registration before any
receipt exists (every unit since D60); **lower-bound controls** so that a
negative is the conservative reading (D57 **S4**); **anti-vacuity AST
scans** over `check()` predicates (D57 **S5**, with its own carried
defect — the scanner is defeated by hoisting, D46b's carried finding);
**mutant batteries** where each mutant must fail its owning gate (D62,
eleven mutants); **determinism under `PYTHONHASHSEED` 0/7/999**
(D63 **W6b**); **negative controls that prove the instrument can fail**
(D68 **F5**; the probe's `full0` row); **exit 0 for substantive
negatives, exit 1 only on anchor breakage**; and the discipline that a
receipt's printed numbers are authoritative over its note (LOG #477's
four-figure forward correction).

---

## §3. THE ROUTES THAT REMAIN

Nine.  Each with **(a)** the idea, **(b)** why the walls don't kill it,
**(c)** its most likely failure mode, **(d)** what a STRICT pin for it
would gate.

---

### R1 — TYPE-ONLY AGGREGATION

**(a)** Replace D57's sector map `s = (initiator, event-type)` by the
**actor-blind** map `s = event-type` (five types: `p`, `r`, `n`, `d`,
`m`), and recompute the **coarsest** partition on which the aggregated
transfer is class-determined.  Named by D57's own residue list and by
book §A9.4/§B9.4b as untested.

**(b)** W-A is about per-option exactness and is silent.  W-C computed
the coarsest partition **for one sector map only**; a coarser sector map
induces a coarser coarsest partition, and D57's counts say nothing about
it.  The corpus's independent argument (D50, book §B6.12) that
record-level observables are **aggregated** applies a fortiori.

**(c)** The knowledge-lag explosion is the measured driver (probe M4),
and it is **not** a per-actor-label artifact — the W1/W2 witness
distinguishes histories that differ only in *who knows*, and no
actor-blind aggregation removes that distinction from the **successor
class**.  Most likely outcome: the same creep, one level later.  The
corpus's own quantitative hint is the actor-swap quotient residue:
counts `≤ 2×`, *"so it cannot rescue the trend alone."*

**(d)** D57's receipt verbatim at the new sector map: exhaustive caps
3/4/5/6; per-depth fixpoint counts across caps with the **last-two-caps**
decider stated as implemented; the **S3 witness** for the first split at
each cap; the **S4 trivial-boundary control** so the counts are lower
bounds; and the finite-alphabet prerequisite gated **first and
separately**, with D57's precedent (a pre-registered prerequisite
refuted, then its refutation withdrawn) printed in the pin.

---

### R2 — BUDGET-ONLY AGGREGATION

**(a)** Coarser still: one sector per **weight budget** — the four
budgets propose / arbitrate-and-merge / deliver / idle (glossary entry
*sector*) — or, in the extreme, a single sector carrying the whole menu
mass, with the transfer aggregated to `T(h, c) = Σ_e q(e|h)·[class(h+e)
= c]`.  This is the "total-budget-only" residue.

**(b)** Same as R1.  Additionally: W-A's ladder leaves the **delivery
budget total constant at `1/4`** at every rung — the coordinate that
provably explodes is invisible at budget granularity.

**(c)** Two failure modes, and the second is the serious one.  (i) The
successor-class refinement still splits (R1's mode).  (ii) **Vacuity**:
at maximal coarseness the aggregated transfer is close to a statement
about total mass alone, and a "closure" there may carry no
menu-determining content — i.e. it could be finite and useless.  A pin
must decide **in advance** what a closure at this granularity would
license, or it will produce a number nobody can spend.

**(d)** As R1, **plus** an explicit *usefulness gate* written before the
run: state the object that a finite budget-lumped chain would let one
compute (candidate: the record-class transition probabilities of §2.6's
scorecard), and gate that this object is **recoverable** from the lumped
chain — with a negative control showing the gate can fail.

---

### R3 — SECTOR-LUMPING DONE COARSER IN THE OTHER TWO DIRECTIONS

**(a)** D57 fixed three choices at once: the sector map, the successor
**class** granularity (the partition being refined), and the family
(two actors, caps 3–6).  R3 varies the *second* and *third*: the
actor-swap quotient (identify histories under actor renaming), depth 7,
and coarser successor classes (e.g. classify successors by *record
class* rather than by lumped state).

**(b)** W-C's negative is a statement about a specific fixpoint; the
actor-swap quotient and depth 7 are its **own named residues**.  The
successor-class coarsening is a genuinely different fixpoint.

**(c)** The corpus already prices two of the three: actor-swap gives
`≤ 2×`, depth 7 is one more level of the same creep.  The
record-class-successor variant is the only one with real headroom, and
its likely failure is that the record functor **separates the ladder's
rungs** (each rung mints a distinct version, so the records differ), so
the counter reappears.

**(d)** Cheapest possible pin: run all three variants in one receipt,
each against D57's committed depth-3/4/5 rows as anchors, with the
**S4** control on each; pre-register that a `≤ 2×` improvement is
**not** a closure and name the number that would count as one.

---

### R4 — THE DEPTH-GRADED / PROJECTIVE-LIMIT (HORIZON-LIMIT) ROUTE

**(a)** Stop asking for a state summary.  Build the measure as the
**limit of a horizon-indexed family**: D46b's relative-horizon kernels
`k_r(e|h) = q(e|h)·G(h+e, r−1)/G(h, r)`, each of which is a bona-fide
conditional law on histories at every finite `r`, and ask whether the
family is **Cauchy uniformly over the history family** as `r → ∞`,
whether the limit is **independent of the truncation/boundary
convention**, and whether it is **proper**.  A uniform limit gives a
consistent family of conditionals, hence (Kolmogorov/projective limit) a
measure on infinite histories — **with no bounded abstraction anywhere
in the construction.**

**(b)** W-A kills finite summaries that determine menus; `k_r` is
defined **per history** and determines nothing finitely.  W-B and W-C
are about abstractions.  W-E's "escape" is about the intrinsic chain's
windows.  **None of the five walls touches a per-history kernel.**  And
the corpus's own closing sentence names this route: *"level-structured
(QBD / R-matrix / Martin-boundary) description … which connects to the
already-built D46b transport-scope Martin/R-theory machinery rather than
to Perron"* (probe §7 G6; book §B9.6, §A9.5).

**(c)** Three, in order of likelihood.  (i) **The limit is measured, not
proved.**  A contracting four-term sequence is not convergence — this is
exactly the error D46d's BLOCKER B1 convicted (*"a control that cannot
fail is not evidence"*) and D57's S2 label corrected.  Without a
contraction **lemma**, the deliverable is a Cauchy table, not a measure.
(ii) **The limit depends on the truncation convention** — which is not a
failure but the **imported-completion horn** (book §B6.7 horn (I)) one
scope up, and then D50's price applies: the measure exists and is a
**choice**.  (iii) **Properness fails family-wide** at `r ≥ 3` (it is
gated only at `r = 1, 2` family-wide today).

**(d)** See §5 — this is the drafted pin.

---

### R5 — THE REGENERATIVE / ATOM ROUTE `[the route the corpus implies and has never named]`

**(a)** An infinite chain does not need a finite state space to have a
measure; it needs a **recurrent atom**.  The corpus has one in every
place it has looked: D62's row **R4** proves *"every pair-arb is a
RENEWAL to the root state"* — serialisation-identical to `sigma([])` —
**derived, not measured**; d44a's renewal/pumping structure is that row;
and D46b's **MB5**, after its round-1 reversal, gates that **root =
renewal transfers at matched horizon at transport scope**.  If a
renewal-shaped event recurs with weight bounded below along the
histories a measure would charge, the process decomposes into i.i.d.-like
cycles, and the measure is built cycle by cycle — a **regenerative /
Doeblin-minorization** construction rather than an eigenvector one.

**(b)** Nothing in W-A through W-E is about recurrence.  W-A's ladder is
in fact the *complement* of this route's object: the ladder is a
**transient, never-regenerating** cylinder (`A` self-arbitrates forever
and nothing resolves), so the ladder and the renewal structure are about
disjoint parts of the tree — **which is precisely why the ladder can be
unbounded while a regenerative decomposition survives.**

**(c)** The minorization is what fails.  At transport there is no
two-actor pair-arb theorem; the transport renewal candidate is
`root = renewal` **at matched horizon**, gated as
**necessary-not-sufficient** with the non-sufficiency censused
(8,196/30,728 at `r = 1`).  So the likely finding is: renewal states
exist and recur, but **the return weight is not bounded below uniformly**
— the ladder can be padded arbitrarily between renewals, driving the
expected cycle length (and possibly its mass) out of control.

**(d)** A strict pin would gate: (i) the transport renewal predicate,
**defined from D62's R4 serialisation** and verified against the
committed layer at every occurrence; (ii) the **return-weight census** —
the total weight of cylinders from a renewal state back to a renewal
state, by cycle length, exactly, at declared caps and actor pools; (iii)
whether the ladder's cylinders carry vanishing or non-vanishing weight
(the exact question the `1/(4(k+1))` per-option split raises); (iv) a
**minorization attempt with its bound printed, or an explicit
empty-return** — the honest outcome being "no bound exhibited"; (v) the
positive control that the same machinery reproduces d42a's renewal
structure and `λ = 2`.

---

### R6 — LEVEL-STRUCTURED (QBD / R-MATRIX) DESCRIPTION

**(a)** Take `|holdings|` (the provably unbounded coordinate) as a
**level**, and the residual join-view structure as the **phase**; ask
whether the transition law is level-independent above some level — the
QBD / matrix-geometric shape, whose stationary object is `R`-matrix
theory rather than a finite Perron eigenvector.

**(b)** Explicitly listed as not excluded by the probe's caveat **C1**
and named in its §7 **G6** as the alternative replacement object.

**(c)** The phase must be finite for QBD to buy anything, and the
**phase is the knowledge-lag structure**, which is the *measured*
fastest-growing component (probe **M4**: `live`/`comps` at 284/288
distinct values by depth 6 versus 13 for the holdings counter).  So R6
most likely reduces to "the counter is level, the phase is still
infinite" — i.e. probe §5's verdict again: *killing the counter is
necessary and not sufficient.*

**(d)** Gate level-independence directly: for each level `ℓ ≥ ℓ₀`, is
the transition kernel between phases identical (exact Fractions,
renamed)?  A pin should pre-register that **failure of
level-independence is the expected finding** and that the deliverable is
then the exact **level-dependence census** — which is what R4 needs
anyway as a diagnostic.

---

### R7 — INEXACT / OBSERVABLE-DEMANDS-ONLY DESCRIPTION

**(a)** Give up exactness entirely.  D50 (book §B6.12) established that
*"what is observable is the probability of moving from one class of
situation to another, and a per-event demand would be a demand on
unobservable event labels."*  So build an abstraction that reproduces
**only the completion's observable demands** — and nothing else.

**(b)** Named as the second surviving crack by D57's residue list and by
book §A9.4/§B9.4b/§D4 item 6.  All five walls are about **exact**
reproduction of something.

**(c)** **The demands are not a defined list.**  The corpus has never
written down what a transport-scope completion must reproduce; §B9.4b's
own warning is that *"the aggregated reading is the correct one for
STATING demands and is also what makes an exact aggregated bookkeeping
hard to build."*  So the likely failure is definitional, not
computational: the unit produces an object whose adequacy nobody can
adjudicate.  Second failure mode: an inexact abstraction that matches on
the computed window and is unfalsifiable off it.

**(d)** A pin must be a **definitional** unit first: enumerate the
demands (candidates: additivity along cuts; record-class constancy;
harmonicity at the measured growth rate; the §2.6 scorecard ratios),
each with the receipt that would test it, **before** any abstraction is
proposed — and gate that the list is closed under the corpus's own
citations.

---

### R8 — THE RECORD-SIDE CONSTRUCTION

**(a)** Build the measure **on record classes at transport scope**
directly — `canon` classes, not histories — rather than deriving it from
a history kernel.  D65 proves such objects exist as a class at d42a: its
second exact witness is *"a measure on refined record cylinders,
constant on all 427 depth-≤4 record classes, that breaks
`sigma`-commuting squares"*, and `μ_Zhat` is constant on all 5,548
classes.

**(b)** The walls constrain **history-level abstractions determining
menus**.  A record-class measure is a different object; and D65 proved
**"repairs the squares" and "descends to a record measure" are two
different linear systems** — neither implies the other — so the record
side is not a corollary of the kernel side.

**(c)** The ladder mints a distinct version at every rung, so **the
record functor separates the rungs** and the record classes at transport
are at least as numerous as the histories that generate them; a
record-side construction inherits an infinite index set with no obvious
extra structure.  Second mode: **the choice of record functor is
interpretive** — D65 residue (3): *"`canon` was CHOSEN as the
record-identity functor … verified for this functor, not a general
fact."*  A record-side measure would then be a measure *relative to a
chosen functor*, and the campaign would have moved the arbitrariness
rather than removed it.

**(d)** Gate the record functor's status **first** (which canon; is
refined ⊆ `sigma`-commuting at transport, and by what argument); then the
linear-systems separation at transport (does repair-vs-descend still
decouple?); then existence of a positive record-cylinder measure with a
declared consistency condition, with its dimension counted exactly
(D65's method — exact rational rank over a truncation).

---

### R9 — THE CONVENTION CONTROL (**not an escape — a scope diagnostic**)

**(a)** W-A rests on one line of the committed layer:
`deliver_options_in_view` enumerates over `view.holdings(a)` **including
superseded members**, while `prop_options_in_view` **skips** them — and
that asymmetry is the entire reason d42a closes and transport does not
(probe §4: *"Why d42a escapes it"*; and the resulting verdict that
*"the 36-state closure is a starvation artifact"*).  R9 asks, purely as
a diagnostic: is the ladder a fact about **transport**, or a fact about
**one enumeration convention**?

**(b)** It is not blocked because it is not a construction: it changes
nothing and claims nothing.  It is the same species of question as
D50's *"the form is a CHOICE"* — asked of the grammar rather than of the
completion.

**(c)** **This route's failure mode is that it is mistaken for an
escape.**  Adopting a restricted enumerator would be **a different
theory**, not a solution: every transport-scope number in the corpus
(D44b, D46b, D46d, D54, D60, D63, D66, D67) is computed at the committed
layer, and none of them would survive the change without re-derivation.
The corpus's standing practice with known pricing defects is to
**carry** them into the completion problem rather than patch them (book
§D4 item 10: `h12`, the general-depth ladder, the `1/16` vs `1/24`
merge).

**(d)** Not its own unit.  It should ride **inside** the first pin as a
one-gate diagnostic: recompute the ladder with the delivery enumerator
restricted, report whether unboundedness survives, and print, in the
gate's own label, that the committed layer is unchanged and that no
other number in the receipt uses the restricted enumerator.  If the
ladder **survives** the restriction, W-A hardens from "a fact about one
line" to "a fact about transport" — which is worth a great deal for
free.  If it does not, the campaign has learned exactly which line of
the grammar carries the wall, which is worth more.

---

## §4. THE RANKING

Judged on three axes: **falsifiability** (can the unit return a clean
negative?), **cost** (can it be built on committed machinery?), and
**decidingness** (how much of the four-frontier question does either
answer settle?).

| # | route | falsifiability | cost | decides the four frontiers? |
|---|---|---|---|---|
| **1** | **R4 horizon-limit** (+ R5 as its proof engine, R6 as its diagnostic) | **high** — exact rational Cauchy tables, a convention-independence comparison, and a properness gate, each able to fail | **low-medium** — D46b's machinery is built and terminal; D46d's sampler is calibrated | **yes, either way** |
| 2 | R1 + R2 coarse aggregation, as ONE unit | high — D57's method transfers verbatim | **lowest** — one receipt, two sector maps | partially: a closure reopens Perron; a blow-up completes the wall |
| 3 | R5 regeneration, standalone | high | medium — the renewal predicate exists (D62 R4); the census does not | yes if it fires (it would upgrade R4 from measured to proved) |
| 4 | R8 record-side | medium — needs a functor decision first | medium | yes if it fires, but on a chosen functor |
| 5 | R3 lumping variants | high | lowest | no — the corpus already prices two of three at `≤ 2×` |
| 6 | R6 QBD standalone | medium | medium | no — expected to reduce to the known phase explosion |
| 7 | R7 observable-only | **low as posed** — no demand list exists | low as a *definitional* unit, high as a construction | yes eventually; not yet posable |
| — | R9 convention control | high | trivial | no — but it re-grades W-A itself |

**Why R4 first, in one paragraph.**  It is the only route that does not
need finiteness *anywhere*, so it is the only one the exact wall cannot
reach even in principle; the corpus's own two independent lessons
converge on its object (**D50**: record-level observables are aggregated;
**D44f/D46b**: the horizon-stable forced object is the sector
conditional), so it is building the thing two terminal units already
identified; its machinery is **built, reviewed, terminal, and unspent
for four months**; every one of its gates is an exact-rational
comparison that can fail; and each of its four pre-registered outcomes
is worth having — a limit gives the measure, a convention-dependence
gives the **imported-completion horn at transport scope** (which is the
completion dichotomy re-posed where the geometry lives, and would make
D50's price a program-wide statement), a properness failure names the
exact defect, and a non-Cauchy family closes the route by measurement
and promotes R1/R2/R8.  By contrast route 2 is cheaper but decides less
(its best case only restores a *method*), route 5 is the strongest
possible result and the least likely to fire alone, and route 7 cannot
be pinned at all until somebody writes the demand list.

**What R4 does NOT do, said now so the pin cannot over-claim.**  A
horizon limit is not a *root-free* completion by itself — root-freeness
is the **convention-independence** gate, and if that gate goes the other
way the outcome is horn (I), not a failure.  And no outcome of R4 makes
a dimension claim, a typicality claim beyond its declared family, or any
statement about the identified law: the missing map is untouched.

---

## §5. THE FIRST PIN, DRAFTED

> **This is a DRAFT for the principal to freeze, amend or discard.  The
> unit number is the principal's to assign; `D70` is used below as a
> placeholder.  Nothing in §5 has been run.  Written to the standard of
> `note-d68-functional-slot-pin.md` and `note-d66-arbitration-crystal-pin.md`:
> objects, gates, pre-registered outcomes, falsifiers, exit protocol,
> scope, and no unfounded lean.**

---

# D70 — THE HORIZON LIMIT: is there a measure at transport scope that needs no bounded abstraction? (DRAFT PIN)

**Status:** DRAFT PIN, STRICT, 2026-07-27.  **Parents:** B1/D56 probe
(LOG #432 — no bounded menu-exact abstraction at transport scope, for
any design; the two load-bearing claims independently verified);
D57 (LOG #436 — sector-exact closed at `(actor, type)` on ground (2)
alone, counts as lower bounds; residues: type-only, budget-only,
untested); **D46b TERMINAL** (LOG #384 → #398 → #400 — relative-horizon
potentials and kernels, three round-1 reversals, delta CLEAN);
**D44f** (LOG #370 — the horizon-stable forced object is the SECTOR
CONDITIONAL; absolute weights are horizon-bound); **D50** (LOG
#421/#422 — record-level observables are the AGGREGATED ones; the form
is a CHOICE); D44b (LOG #374 — the transport chain escapes its windows;
no menu-shape transfer); D62 (LOG #460 — row R4: every pair-arb is a
renewal to the root state); D65 (LOG #468 — `Zhat`'s descent and the
573 ⊃ 205 ⊃ 28 ⊃ 1 hierarchy); D46d (LOG #398/#400 — BLOCKER B2:
*"the theory's own law" is not established*).  **Campaign opened at LOG
#481.**

## 1. The question

Every settled measure result in the corpus was bought with a **finite
menu-exact quotient plus Perron**, and B1 proves that method cannot
transfer.  But a measure is not a quotient.  This unit asks whether the
object D46b already computes — the relative-horizon kernel

```
    k_r(e | h)  =  q(e | h) · G(h + e, r − 1) / G(h, r)
```

— has a **limit** as the remaining horizon `r → ∞`, uniformly over a
declared family; whether that limit is **independent of the truncation
convention** (the transport analogue of root-freeness); and whether it
is **proper** (a probability at every history).  A uniform,
convention-independent, proper limit is a consistent family of
conditionals and hence a measure on transport-scope histories — **built
without any bounded abstraction, and therefore untouched by every wall
the corpus owns.**

A secondary arm, cheap and independent, settles the two remaining
aggregation residues in the same receipt (§3, gate HZ5).

## 2. The objects

- **The layer:** the committed `v10/code/d42b1_transport_exact.py`,
  exec'd path-anchored, AST/text-slice verified.  Admission and pricing
  are **never** re-implemented.
- **The families:** ARM-1T (2 actors) exhaustively to its committed
  caps; and declared 3-actor and 4-actor pools to printed depths.  Every
  cap printed by the receipt.  Sampled arms, if any, labelled
  `[SAMPLED]` and never conflated with exact rows (D46d's method gate).
- **The kernels:** `G(h, r)` by exact backward recursion; `k_r(e|h)` in
  exact `Fraction`s; and the **sector-normalized conditional** of
  D44f/D46b as the *pinned* object (the absolute weights are carried as
  context, per the D44f lesson).
- **The drift norms:** L∞, L1 and sector-L∞ — the three D46b used, which
  gave exactly equal sequences at the root; reported separately, never
  merged.
- **The truncation conventions:** at least two declared terminal
  treatments of the cap layer (the committed one, plus a second — e.g.
  the D57 **S4** pattern of a maximally coarse terminal), each carried
  through the whole computation independently.

## 3. Gates

- **HZ0 — ANCHORS.**  Committed layer by AST/text-slice.  Reproduce, in
  this receipt's own process: the ARM-1T cumulative census
  `[1, 9, 69, 521, 3969, 30729]` and **243,769** to depth 6 (the D56
  probe's M1 anchors); the ladder `{2: 3757, 5/2: 212}` (D46b MB1);
  the transport potentials `G_3 = 257/32`, `G_4 = 1035/64`,
  `G_5 = 4173/128`, `G_6 = 134587/2048` and **both** ratio columns
  (delivery-free and transport) exactly; the root sector-normalized
  drift **exactly zero at `r = 1..6`**; the off-root sup sequence
  `1/18, 4/171, 8/741, 176/32877`; and the family-uniform sup
  `3/110, 3/253, 373/69230, 2333/1838829`.  **Exit 1 only here.**
- **HZ1 — PROPERNESS, EXTENDED.**  `Σ_e k_r(e|h) = 1` exactly, for every
  `h` in each declared family, at `r = 1..R` with `R` printed.  D46b has
  this family-wide only at `r = 1, 2`.  A failure is a **first-class
  finding** (outcome HZ-IV), not an error.
- **HZ2 — THE CAUCHY TABLE (the unit's core).**  The family-uniform sup
  of `‖k_{r+1} − k_r‖` in the three norms, over each declared family,
  extended in `r` **and in actor pool**, as exact rationals.  **No fitted
  rate, no extrapolation, no invented threshold.**  The word "converges"
  may not appear in any label unless HZ4 supplies a bound; otherwise the
  deliverable is the table and the word is "contracts over the computed
  horizons".  *(This clause exists because D46d's BLOCKER B1 convicted
  exactly this inference and D57's S2 label had to be corrected for a
  threshold "justified nowhere".)*
- **HZ3 — TRUNCATION-CONVENTION INDEPENDENCE (the horn gate).**  The
  same kernels under at least two declared terminal conventions,
  compared **at matched relative horizon**, entrywise in exact
  `Fraction`s, at the root **and** family-wide at the reachable `r`.
  Equal, and staying equal as `r` grows = evidence of root-freeness at
  transport.  Different, and **not** shrinking in `r` = **the imported
  completion horn (I)**, and the difference is the deliverable.
- **HZ4 — THE LEMMA SLOT (proof-shaped; may return empty, and saying so
  is a result).**  Attempt a **contraction / minorization bound** rather
  than a measurement, on the corpus's own named candidate: D62's row R4
  (every pair-arb is a renewal to the root state, derived), plus D46b's
  **MB5** (root = renewal transfers at matched horizon,
  necessary-not-sufficient with the non-sufficiency censused
  8,196/30,728, 1,060/3,968, 104/520).  Gate: (i) the transport renewal
  predicate defined from R4's serialisation and verified at every
  occurrence against the layer; (ii) the exact return-weight census from
  renewal to renewal by cycle length; (iii) whether the **B1 ladder's**
  cylinders (which never regenerate) carry vanishing total weight;
  (iv) a printed minorization constant **or** an explicit "no bound
  exhibited".  **No outcome here may upgrade HZ2's labels unless a bound
  is printed.**
- **HZ5 — THE AGGREGATION ARM (secondary, cheap, independent).**  D57's
  coarsest-lumpable fixpoint recomputed at two strictly coarser sector
  maps — **TYPE-ONLY** (`s = event-type`) and **BUDGET-ONLY** (`s = the
  weight budget`) — at caps 3/4/5/6, with D57's **S4** trivial-boundary
  control so the counts are lower bounds, and D57's **S3** split witness
  at each cap.  Its finite-alphabet prerequisite gated first and
  separately.  **Declared droppable** if the runtime budget binds — with
  the drop printed, never silent.
- **HZ6 — CONTROLS AND ANTI-VACUITY.**  (i) **Negative control:** a
  deliberately perturbed weight law must break contraction — an
  instrument that cannot fail is not evidence (D68 **F5**; the probe's
  `full0` row).  (ii) **Positive control:** the delivery-free d42a
  family through the same pipeline must reproduce `Zhat`'s known objects
  — `f = (4,4,3,7,3,3)/3`, values `{1, 4/3, 7/3}` at multiplicities
  `{29, 5, 2}`, and `λ = 2` as an **asymptotic** eigenvalue (never
  compared to a finite-horizon ratio — D46b's own relabelling).
  (iii) **AST anti-vacuity scan** over every `check()` predicate (D57
  **S5**), with the hoisting defect D46b carried named in the label so
  the scan is not sold as more than it is.  (iv) **Determinism** under
  `PYTHONHASHSEED` 0/7/999, byte-identical stdout (D63 **W6b**).
- **HZ7 — THE WALL CONTROL (diagnostic; changes nothing).**  Re-derive
  the B1 ladder with `deliver_options_in_view` restricted to
  non-superseded holdings, **as a diagnostic only**, and report whether
  unboundedness survives.  The gate label must print: *the committed
  layer is unchanged; no other number in this receipt uses the
  restricted enumerator; adopting it would be a different theory and is
  not proposed.*
- **HZ8 — DOCTRINE.**  No infinite-volume claim from finite horizons
  (D46b **MB6**, binding).  Every statement horizon-scoped and
  pool-scoped.  Every normalization named at every use (D46d **B2**).
  Sampled never conflated with exact (D46d **TY3/TY5**).  No dimension
  claim and no typicality claim of any kind in this unit.  Scale
  doctrine, LOG #440.  No claim about the identified law: the missing
  map is untouched.  Caps and runtime printed by the receipt itself.

## 4. Pre-registered outcomes (any is the result)

- **HZ-I — NOT CAUCHY.**  The family-uniform drift stops contracting at
  reachable `r`, or contracts at the root while failing family-wide, or
  fails at wider pools.  Then the horizon-limit route is **closed by
  measurement**: the finite-horizon measures are horizon artifacts,
  D46d's typicality numbers stay horizon-scoped permanently, and the
  campaign's weight moves to R1/R2 (HZ5's arm) and R8.  A first-class
  negative and the cheapest one to reach.
- **HZ-II — CONVERGENT BUT CONVENTION-DEPENDENT (horn I at transport).**
  HZ2 contracts and HZ3 separates.  Then a measure at transport scope
  exists but is an **imported completion**, and D50's *"the form is a
  CHOICE"* becomes a program-wide statement rather than a d42a one.
  **This is the most informative outcome for the four frontiers**, since
  every frontier question becomes "under which completion?" — a
  well-posed question with a priced answer.
- **HZ-III — CONVERGENT AND CONVENTION-INDEPENDENT.**  A root-free
  measure at transport scope, obtained without any bounded abstraction —
  the walls confirmed to bite the **reduction** and not the **object**.
  Then dimension typicality, grid typicality and the transport-scope
  functional slot become posable immediately.  **This outcome may be
  claimed only with HZ4's bound printed**; without it the label is
  "root-free over the computed horizons", explicitly not a boundary
  theorem.
- **HZ-IV — CONVERGENT BUT NOT PROPER / NOT A MEASURE.**  HZ1 fails
  family-wide, or the limit is a kernel that is not additive along cuts
  — the transport analogue of §B2.10's cut-mass non-additivity
  (`1, 2, 4, 257/32, 1037/64, 2101/64, 68313/1024` at d42a).  Then the
  defect is named exactly and the completion problem is re-posed with
  its transport shape known.
- **HZ5-a / HZ5-b:** a coarser sector granularity **closes** (Perron
  reopens in aggregated form; the D57 wall is granularity-specific) /
  **blows up** (the aggregation wall extends to the two named residues
  and routes R1/R2 close).

**LEAN — stated exactly, and narrowly.**  *(The campaign's record: D57
pre-registered two expectations and both were refuted, one of the
refutations then withdrawn; D46d's lean produced a blocker; D68 declined
to bet and was right to.)*

- **HZ1 (properness at `r ≥ 3` family-wide): weak lean POSITIVE**, on
  the ground that it is proved by construction at the root for
  `r = 1..6` and gated family-wide at `r = 1, 2`.  Gated **first**, as
  the prerequisite; its failure is outcome HZ-IV.
- **HZ2 at the two-actor arm: weak lean CONTRACTING**, on the ground of
  D46b's gated four-term family-uniform sequence
  `3/110, 3/253, 373/69230, 2333/1838829` — **and the pin records that
  this is four terms at small caps at two actors, that the sequence is
  explicitly "not a rate" in its own source, and that a contracting
  finite sequence is not a limit.**
- **HZ3 (the horn), HZ2 at wider pools, HZ4 (the bound), HZ5: NO LEAN.**
  These are the questions the unit exists to answer and the pin declines
  to bet on any of them.

## 5. Falsifiers, named

1. **The instrument cannot fail** — if the perturbed-law control
   (HZ6-i) still shows contraction, every HZ2 number is void.
2. **The root is not the family** — if drift is zero at the root and
   non-contracting family-wide, "horizon-stable" was a root artifact
   (this is precisely the reversal D46b's round-1 already performed once
   in the other direction, and the reason MB5-c exists).
3. **The convention gate collapses** — if the two terminal conventions
   differ by an amount that does **not** shrink in `r`, HZ-III is
   excluded no matter how good the Cauchy table looks.
4. **Pool dependence** — if the drift's contraction rate degrades
   systematically with actor pool, the two-actor arm was measuring the
   ARM-1T family and not transport.
5. **Ladder mass** — if the B1 ladder's non-regenerating cylinders carry
   non-vanishing weight under the limit candidate, no regenerative
   argument (HZ4) can ever supply the bound, and HZ-III is
   permanently out of reach by this route.
6. **Anchor breakage** — any committed D46b number failing to reproduce
   invalidates the unit (exit 1).

## 6. Scope, binding at every citation

Transport scope, the **declared families and caps only**; exact
`Fraction`s throughout.  **No infinite-volume claim under any outcome.**
The pinned object is the **sector-normalized conditional**; absolute
completed weights are horizon-bound (D44f) and are context.  No claim
that any limit is *the* click law's measure — the identified law is
reached only through the missing map (D59/D65), untouched here.  No
dimension, typicality or quantum-layer claim of any kind; those are the
**consequences** this unit would unblock, not its content.  Scale
doctrine (LOG #440): this unit certifies a **mechanism** — the existence
or non-existence of a horizon-limit measure — never an object.  (H1)/(H2)
and the 36-state closure remain **two-actor delivery-free d42a**; nothing
here extends them, and the own-view dichotomy's **proposer test** is
known to break at three actors.

## 7. Exit protocol

Exit **0** for every substantive negative, including HZ-I, HZ-IV and
HZ5-b — these are results.  Exit **1** only on **HZ0** anchor breakage,
i.e. if the committed layer or a committed D46b/D57 number fails to
reproduce in-process.  Every cap, seed, pool, runtime and dropped arm
printed by the receipt itself.  Pin frozen and committed **before** any
code is written; the note names the receipt path before it exists.

---

## §6. WHAT THIS NOTE DOES NOT DO

- It **proposes no new numbers** and closes no question.
- It does **not** adjudicate the ambiguity it found in the corpus: D57's
  ground (1) is withdrawn, so **whether the sector-total alphabet at
  transport scope is finite is `[OPEN]`**, and both the pin's HZ5 arm
  and any future citation must treat it as open rather than as either
  settled direction.
- It does **not** rank the **TRIPLE-GRID** construction (book §D4 item 2,
  `[NOT BUILT]`) against the measure campaign; that is a construction
  front, not a measure front, and the two are independent.
- It takes no position on the **Lean-grade mechanization** residue, on
  the two empty bridges (§C5, §C6.11), or on the demand's-uniqueness
  computation (book §D4 item 1a) — the last of which is *cheaper* than
  anything in §5 and belongs to the missing-map front rather than to
  this campaign.
