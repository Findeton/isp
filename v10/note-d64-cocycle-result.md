# D64 — result: **the transitions are non-trivial pair by pair, the cocycle is clean, and THE CLASS IS A COBOUNDARY — H¹ = 0, the atlas is globally trivializable by a per-chart port choice.**

**Status: ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.**  Round 1
(`reviews/d64-round1-hostile-review.md`, independent Opus 5 worker, own
record builder, own poset, own sky, own cocycle code) returned
**REVISE — 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT**, and its one-line
result is the honest summary of this unit: *the referee reproduced every
number in the receipt and refuted the interpretation built on them.*
Every finding was verified and every one is applied here.  Pin
`note-d64-cocycle-pin.md` (STRICT, frozen and committed before the first
receipt existed).  Receipt `v10/code/d64_cocycle_exact.py`, output
`v10/data/d64_cocycle_exact.out` — **15 PASS / 0 FAIL, exit 0, ~61 s wall
clock** (run from the repo root).  Parents: D63 (the substrate,
TERMINAL), D58 (the atlas and its containment theorem), W4b (the
branching bound), D42b1 (the transport grammar and `event_poset`).

---

## 1. Which outcome fired, and what it means

The pin pre-registered three outcomes and let the census decide.  The
census fired **G3's letter**.  A computation the first build never ran —
now C7 — shows that **G1's sentence** is the true one.

> **WHAT WAS MEASURED.**  Of the **172 overlapping chart pairs** of
> DOUBLE-RING(8, 10, 8) at SKY-B depth **d = 2** at the canonical (ROLE)
> wire-word labeling, **57 carry the identity transition and 115 carry a
> non-identity one**; on the **wide subatlas** (the 137 pairs both of
> whose charts have `|D| = 4`, the delivery grammar's ceiling) the split
> is **29 / 108**.  All **111** testable chart triples satisfy the
> cocycle; **zero violations**.  So the pin's G3 predicate —
> non-identity transitions *and* a clean cocycle — is what the census
> computes.
>
> **WHAT THAT DOES NOT ESTABLISH.**  Non-identity transitions plus a
> clean cocycle do not distinguish a non-trivial bundle from a trivial
> one.  The decisive question is whether the Z/2-valued 1-cochain `g` is
> a **coboundary**: is there a 0-cochain `ε: charts → Z/2` with
> `g_ac = ε_a + ε_c`?  **IT IS.**  On the 138 length-preserving
> classified overlaps, over 60 charts in 9 components, the propagation
> finds **0 obstructions**, with `ε` = **32 charts at 0 / 28 at 1**; and
> the independent verification — the whole transition census re-run with
> that relabelling applied — turns **all 108 τ pairs into the identity**,
> leaving **165 of 172 pairs identity** and **0 surviving non-identity
> length-preserving transitions**.  The only survivors are the 7
> length-changing correspondences, which are not fibre maps at all.  The
> referee's cleaner Čech form `g_ik = g_ij + g_jk` agrees: **108 triples,
> 0 violations**.  It is not a REG artefact: at REGA, **0 obstructions**
> as well (`ε` = 40 / 20, 0 survivors); on both grammar controls the
> question is vacuous for a reason that is itself a finding (§3(b)).
>
> **THEREFORE.**  `H¹ = 0`.  The atlas is **globally trivializable** at
> this labeling by a per-chart choice of which of the base delivery's two
> wires is "port 0".  The holonomy of every loop in the nerve is trivial.
> The transitions are **pure gauge**.

**The pin's trichotomy has a gap, and it is the gap this unit landed in.**
G1's *predicate* is "all transitions are identity"; G1's *sentence* is
"the atlas is globally trivializable at this labeling".  The measured
cell — *non-identity transitions, clean cocycle, cohomologically trivial
class* — is in none of G1/G2/G3 by predicate, and is G1 by sentence.  The
pin gets the credit here: its trichotomy was sharp enough that the gap is
visible rather than hidden, and its G1 sentence was already written in
the form the measurement needed.

**The outcome is NOT read at the RAW labeling, and the receipt says why
before it says anything else** (C2b, PROBE 2).  On every grammar
substrate at both depths, *every* overlapping chart pair has base events
with **disjoint register sets**; a raw wire word's first letter is always
a register of its own base event; therefore raw labels can *never* agree
and RAW's "non-identity at 172/172" is a **tautology of the labeling**.
A G3 read at RAW would be an instrument artifact and is refused.  The
mirror probe does **not** fire: **no labeling on any substrate at any
depth is blind** (PROBE 1), so a G1 reading, had the census produced one,
would not have been an artifact of a labeling that cannot see
transitions.  Both probes survive round 1 intact and the referee credits
PROBE 2 as the best thing in the first build.

## 2. The censuses (all d = 2 unless labelled; "REG" = the canonical labeling)

**The substrate, DOUBLE-RING(8, 10, 8)** — 177 events, 16 actors, 141
charts (`|D| ≥ 2`), **59 wide charts** (`|D| = 4`), 172 overlapping
pairs, 137 of them wide–wide, 111 triples.

| labeling | d = 2 id / non-id | wide–wide | d = 3 id / non-id | wide–wide |
|---|---|---|---|---|
| RAW (registers) | 0 / 172 **(tautology)** | 0 / 137 | 0 / 273 | 0 / 263 |
| **ROLE (canonical ports)** | **57 / 115** | **29 / 108** | 54 / 219 | 54 / 209 |
| FIRST-raw | 0 / 172 | 0 / 137 | 0 / 273 | 0 / 263 |
| FIRST-role | 57 / 115 | 29 / 108 | 148 / 125 | 148 / 115 |

**The 115 and the 108 are different populations, and this is said once,
here, correctly** (round-1 MINOR 6).  The **115** non-identity pairs are
**108** pairs carrying a τ-classified fibre map **plus 7** carrying a
*length-changing* correspondence, which is a permutation of nothing and
belongs to no group.  Every group-level sentence below ranges over the
**108**; every census-level sentence over the 115.  A further 27 pairs
carry no single-valued correspondence at all, and are counted as
"identity" in the label-set census (they are 27 of the 57).

**FIRST-role reproduces ROLE exactly at d = 2 and not at d = 3**: at
depth 2 *all* the transition content sits in the first wire letter; at
depth 3 the later letters carry content too.  A measured fact about this
substrate, not a theorem.

**The controls, both columns** (C5).  `REG` for grammar substrates;
sprinklings carry only the register-free `COV` surrogate, because a
sprinkling *has* no register alphabet — a fact about the objects, not a
cut.

| substrate | d | pairs | ROLE id | ROLE non-id | wide pairs | cocycle viol. |
|---|---|---|---|---|---|---|
| **DR(8,10,8)** (substrate) | 2 | 172 | **57** | 115 | 137 | 0 |
| DR(8,10,8) | 3 | 273 | 54 | 219 | 263 | 0 |
| BRICK(8,14) (D60's brick) | 2 | 58 | **0** | 58 | **0** | 0 |
| BRICK(8,14) | 3 | 56 | **0** | 56 | 52 | 0 |
| DR(8,10,0) (uncoupled ring pair) | 2 | 68 | **0** | 68 | **0** | 0 |
| DR(8,10,0) | 3 | 61 | **0** | 61 | 56 | 0 |
| M²⁺¹ sprinkling (COV) | 2 | 247 | 3 | 244 | 153 | 0 |
| M²⁺¹ (COV) | 3 | 383 | 1 | 382 | 279 | 0 |
| M³⁺¹ sprinkling (COV) | 2 | 370 | 4 | 366 | 217 | 0 |
| M³⁺¹ (COV) | 3 | 518 | 2 | 516 | 484 | 0 |

**Coverage, which every universal statement about a cell ranges over**
(round-1 MINOR 3): pairs carrying a single-valued transition at all —
substrate 145 of 172 (84%) at d = 2 and 4 of 273 (1%) at d = 3; brick 19
of 58 (33%) and 0 of 56; uncoupled double ring 22 of 68 (32%) and 1 of
61.

Sprinkling parameters printed by the receipt: d55c's repaired `latt`,
`N = 120`, `box = 60` (M²⁺¹) and `box = 48` (M³⁺¹), `seed = 8`,
`T = 4·box`, orders by `mink4`.

**The coboundary computation, every grammar cell** (C7):

| substrate | inst | d | generator | charts | labelled overlaps | components | **obstructions** | ε 0 / 1 | surviving non-id | Čech triples / viol. |
|---|---|---|---|---|---|---|---|---|---|---|
| **DR(8,10,8)** | **REG** | **2** | **τ** | **60** | **138** | **9** | **0** | **32 / 28** | **0** | **108 / 0** |
| DR(8,10,8) | REGA | 2 | τ | 60 | 138 | 9 | 0 | 40 / 20 | 0 | 108 / 0 |
| DR(8,10,8) | REG/REGA | 3 | — | 4 | 2 | 2 | 0 | 4 / 0 | 0 | 0 / 0 |
| BRICK(8,14) | REG | 2 | σ | 38 | 19 | 19 | 0 | 19 / 19 | 0 | 0 / 0 |
| DR(8,10,0) | REG | 2 | σ | 44 | 22 | 22 | 0 | 22 / 22 | 0 | 0 / 0 |

## 3. The three findings, all three corrected by the round

**(a) A NON-IDENTITY ATLAS IS THE GENERIC CASE HERE — AND THE
SUBSTRATE'S IDENTITY FRACTION IS CHART DUPLICATION, NOT
TRIVIALIZABILITY.**  Not one control is flat: D60's uncoupled brick and
the uncoupled double ring have **zero** identity transitions at both
depths (58/58, 56/56, 68/68, 61/61), and the two genuine sprinklings are
non-identity at 244/247, 382/383, 366/370, 516/518.  What the wide
crystal alone has is (i) **duplicate charts** and (ii) the **wide
subatlas**.

The first of those is the correction (round-1 MAJOR 2).  On this
substrate at `d = 2` the identity/non-identity dichotomy is an **exact
biconditional**, both ways over all 172 pairs, with a property of the
charts that has nothing to do with labels:

> **two charts transition by the identity IF AND ONLY IF they have the
> identical direction set** — `{(same D, identity): 57,
> (different D, non-identity): 115}`, 172 of 172.

The controls' "0 identity" is exactly their having no such pairs at all
(brick `{(different, non-identity): 58}`, uncoupled ring
`{…: 68}`).  So finding (a) says: *the wide crystal is the only substrate
in this census with distinct base events carrying the whole same `d = 2`
chart.*  That is duplication, not "the only substrate with a
trivializable part" — the phrase the first build used, now withdrawn.
And it is **not a theorem**: at `d = 3` the biconditional fails in both
directions (substrate `{(same, non-identity): 1}`; brick 52 pairs with
identical direction sets and **non**-identity transitions).

The second survives: pairs of 4-direction charts exist at `d = 2` **only**
on the coupled substrate (brick 0, uncoupled double ring 0, substrate
137), so only there is this a transition between charts of the delivery
grammar's *maximal* width.

**(b) THE CONTROLS' σ AND THE SUBSTRATE'S τ — A REG-CONVENTION
OBSERVATION, EXPLICITLY LABELLED AS ONE.**  At the canonical labeling
every length-preserving transition of the two uncoupled controls is a
restriction of **σ**, the all-letter flip `(b₁,b₂) ↦ (1−b₁, 1−b₂)`, and
none is a restriction of τ; on the substrate none is a restriction of σ.
That much is measured.  **What it is not is a structural claim**, and the
first build's sentence "the coupling changed which involution the atlas
carries" is **withdrawn** (round-1 MAJORs 3 and 4).  Four things stand
against it, all now in the receipt:

1. **It holds at REG only.**  At REGA the controls become
   `{other 14, σ 5}` and `{other 16, σ 6}`, and at COV — this unit's own
   register-free surrogate, the instrument that makes the sprinkling and
   grammar columns commensurable — they are `{other 19}` and
   `{other 22}`.  Under either, no group can be named for a control at
   all.  A fourth convention the referee built (port index read at the
   *target* of each P-edge) dissolves the separation entirely, putting σ
   on 54 substrate pairs; the referee's own argument that that
   convention is forced is noted and is not this unit's to claim, because
   PROBE 2 as implemented cannot detect that class of forcing.
2. **It is width-confounded.**  Every τ pair is a **(4,4)** wide–wide
   pair (`{(τ,(4,4)): 108, (identity,(4,4)): 29, (identity,(2,2)): 1,
   (no-correspondence,(2,2)): 27, (length-changing,(4,2)): 7}`), and the
   controls have **no** wide charts at `d = 2` at all.  The comparison is
   τ-on-maximal-width against σ-on-narrow, and no matched comparison
   exists anywhere in this census.
3. **It rests on 41 pairs of 126** (19/58 and 22/68).
4. **The controls' σ graph is a perfect matching.**  38 charts / 19
   overlaps / 19 components, and 44 / 22 / 22 — every component of size
   2.  No two σ-overlaps share a chart: there is no composition, no
   triple, no cocycle and no closure content behind "the controls close
   to ⟨σ⟩".  The measured statement is *"each control transition is a
   σ-restriction, pairwise"*, and nothing more.  (The substrate, by
   contrast, has 138 overlaps over 60 charts in 9 components — the
   genuine connectivity that makes C7's coboundary question meaningful
   there and vacuous here.)

**(c) THE PIN'S LEAN: ONE HALF IS A FACT ABOUT WHICH PAIRS EXIST, THE
OTHER IS UNTESTED.**  The pin leaned on "a non-identity wire
transposition at COUPLED wires, because even and odd height
neighbourhoods are not congruent".

- **The parity half is confirmed as a PAIR-POPULATION fact, not a
  transition-value fact** (round-1 MAJOR 5).  Every one of the 115
  non-identity pairs sits in an **odd** height layer, and the per-layer
  census alternates `4 identity / 16 non-identity`, `4 / 0`.  But the
  even layers contain almost no transitions *to be* non-identity: pairs
  by (parity, class) are `{(even, identity): 1,
  (even, no-correspondence): 27, (odd, identity): 29, (odd, τ): 108,
  (odd, length-changing): 7}`, and **all 137 wide–wide pairs are odd**.
  "Every non-identity pair sits at odd height" is therefore equivalent to
  a placement fact about the blueprint — the inter-ring deliveries land
  in the even layers and the ring deliveries' wide charts in the odd ones
  — established before any labeling is chosen.  The alternation is the
  alternation of the population.
- **The coupled-wire half is UNTESTED, not "refuted and inverted".**  The
  27 pairs both of whose base events are inter-ring deliveries are
  **exactly** the 27 pairs that carry no single-valued correspondence at
  all — the receipt now gates that the two sets are *identical*.  So at
  the coupled wires there is no fibre map to be non-identity, and the
  lean cannot be evaluated there.  The first build reported these same 27
  pairs twice, once as a refutation ("27 of 27 are IDENTITY") and once as
  a limitation ("27 carry no single-valued correspondence"), without
  disclosing they are one set.  They are.
- What survives: the transposition is carried by the brick circuit's own
  direction alternation on wide charts, and the coupling's own wires are
  silent at the fibre-map level.

## 4. The licensed claim, no wider than the measured census

> **THE LICENSED CLAIM.**  On the substrate DOUBLE-RING(8, 10, 8), at
> SKY-B depth **d = 2**, at the canonical wire-word labeling: the
> overlapping-chart transitions are **not all identity** (115 of 172
> pairs, of which 108 carry a length-preserving fibre map and 7 are
> length-changing); they **satisfy the cocycle** on every one of the 111
> testable triples; **every length-preserving transition is a partial
> map on 2 of the 4 fibre points**; and **their Z/2 class is a
> COBOUNDARY** — an explicit per-chart port choice `ε` (32 charts at 0,
> 28 at 1) makes all 108 of them the identity, `H¹ = 0`, at REG and at
> REGA alike.  **NO NON-TRIVIAL STRUCTURE GROUP IS EXHIBITED ON THE
> DELIVERY CRYSTAL AT THIS LABELING.**  The tensor/curvature programme
> starts at **zero** here.  This is a **width-≤ 4** statement (W4b caps
> chart width at `B^d = 4` on every delivery substrate), about **this
> substrate at this labeling at this depth**, and no wider.

**And the name of the group is undetermined by the data anyway**
(round-1 MAJOR 1).  No transition is a total permutation, so "the group"
is reached only by *extending* 2-point partial bijections to elements of
S₄, and the extension is not unique.  Exhaustively (C4b): of the 30
subgroups of S₄, **10 are consistent with every observed
length-preserving map**, and **two of those are minimal by inclusion —
and they are incomparable**:

```
   { e, (00 10)(01 11) }                              = Z/2 = <tau>
   { e, (00 01)(10 11), (00 10 01 11), (00 11 01 10) } = Z/4
```

`⟨τ⟩` is the smallest by **order**; it is not the unique minimal by
**inclusion**.  **0 of the 108** τ-classified transitions is uniquely τ —
every one is equally a restriction of an order-4 element — and the Z/4
reading passes the cocycle on the same 108 triples with 0 violations, so
no test in this unit discriminates.  "The group generated is Z/2 = ⟨τ⟩,
*the* fixed-point-free involution of the 4-point fibre" is therefore
retracted: it was a minimality convention wearing a definite article.
**The convention-robust statement is: non-identity partial transitions
exist and are mutually consistent.**  (Note the asymmetry against this
unit's interest, which the referee found and which is reproduced in C4b:
on the two controls ⟨σ⟩ *is* the unique minimal-by-inclusion consistent
subgroup, so the σ naming is better founded than the τ naming that
carried the original headline.)

Five limits, all measured, all reported whichever way they landed:

1. **The non-identity maps are PARTIAL.**  Every τ-transition is defined
   on **2 of the 4** fibre points; the only transitions defined on all
   four are the 29 identity ones.  Partiality is why the group cannot be
   named (above) and it is why "restriction of" can never be dropped.
2. **7 transitions are LENGTH-CHANGING and belong to no permutation
   group.**  They exist because P has edges that **skip a height** — C0b
   counts 7 on the substrate (335 P-edges vs 328 covers; 3 on the brick,
   7 on the uncoupled ring pair) — so one chart reaches a shared
   direction in *one* P-step where the other needs two.  Excluded from
   the group **by name**, counted, and they are the *only* transitions
   that survive the ε relabelling.
3. **27 of the 172 pairs carry no single-valued correspondence at all**
   ("ambiguous"), rising to 261 of 273 at `d = 3` — which is why —
4. **the cocycle test has NO CONTENT at d = 3, and none on the two
   grammar controls**, and **what content it has on the substrate has
   exactly one shape** (round-1 MINOR 2).  Of the 111 tested triples,
   **108 are (identity, τ, τ)** and **3 are (identity, length-changing,
   length-changing)**; every one tests **2 fibre points** (222 in all).
   So "all 111 triples cocycle-clean" means: *`τ ∘ τ = id` was verified
   108 times on 2 points each, and nothing else was verified.*  There is
   no `(id, id, id)` triple and no `(τ, τ, τ)` triple.  Note also that
   the cocycle's scope and the group's scope differ: 3 of the tested
   triples are triples of maps C4 excludes from the group by name.
   Across the whole census 993 triples were tested and 4,776 undefined;
   **zero violations**.
5. **The port-order convention matters to the SPLIT, not to the
   EXISTENCE — and not to the TRIVIALITY.**  REGA gives 85/87 instead of
   57/115 at `d = 2`, and dissolves the controls' σ classification.  What
   is convention-robust across REG, REGA and COV: **non-identity
   transitions exist, and the cocycle is clean**.  What is
   convention-robust across REG and REGA: **the class is a coboundary**
   (0 obstructions in both).  What is not robust: the identity/
   non-identity *ratio*, the *name* of the group, and the substrate/
   control involution contrast.  This unit argues the layer's own
   delivery tuple order `(sender, receiver)` is the canonical one
   *because it is the layer's own*, prints the alternative beside it, and
   notes that this argument fixes the order *within* an event's register
   tuple and does **not** fix which endpoint of a P-edge the port index
   is read at — a gap the referee exhibited with a fourth convention.

**And on "the honest size of a Z/2 gauge structure": that was the wrong
worry.**  The first build's closing paragraph said Z/2 is discrete, not
GL(n), not a Lorentz group, and that any tensor sentence must start from
that.  The right worry is one level down: the class is **trivial**, so
there is no gauge structure to be small.  Nothing here is a structure
group of any size.

## 5. Instrument hygiene and validation

- **Single sources (C0a).**  The transport grammar by text-slice from
  committed d42b1 (cut at its own banner print); the sky instrument
  (d47a), the repaired sprinkling generator (d55c), the atlas (d58),
  D60's blueprint machinery and **D63's own `double_ring` /
  `wide_brick`** by AST extraction.  The substrate this unit charts is
  D63's function object, not a re-typing of it — the referee's
  independent re-typing produces the same 177 events.  Exit-freedom of
  the slice and of all 55 extracted bodies is **gated**, and the gate now
  flags a bare NAME/ATTRIBUTE reference to `exit`/`quit`/`_exit`, not
  only a call, so an aliased exit is caught; the slice is checked by AST
  as well as textually (round-1 NIT 3).  Its scope is stated in the gate:
  a syntactic scan for three names, deciding no reachability.
- **The anchor (exit 1 on breakage).**  `double_ring(8, 10, 8)`
  reproduces D63's committed row exactly at both depths: 177 events,
  d = 2 homogeneity **47/59** (≈ 0.7966), `|D| ≥ 4` at **1/3**,
  `max |D| = 4`, mean ω **100/137** (≈ 0.7299); d = 3 **137/177** and
  **119/177** with `max |D| = 4`.  The brick control is D60's brick
  **event for event**, reproducing 10/13, 125/192, 0, 3.  No refusals.
- **THE INSTRUMENT IS VALIDATED, NOT ASSERTED (C0b).**  `reg_tuple` is
  `regs_of` with an order — same set at every event of every record; each
  event has at most `|regs_of|` P-successors (W4b's joint); and **the
  transitive closure of P EQUALS the committed order `poset_of`** on all
  three grammar substrates.  That last is the gate that makes the wire
  words a *reading of the committed layer* rather than a new structure.
  The covering relation is contained in P, and the COV surrogate's own
  closure is the committed order on **every** substrate including the
  sprinklings.  *This gate earned its keep: it caught a real bug in the
  first build (a closure accumulated in index order, which is not a
  topological order on a sprinkling) before any census was read.*
- **Two structural facts gated in passing (C1).**  The P-path enumeration
  reaches **exactly** SKY-B's `D_e(d)` at every base event of every
  substrate at both depths; and **every overlapping chart pair is
  same-height**, so the pair census is layer-local — 0 cross-height
  overlapping pairs across all 22 cells.
- **THE ARTIFACT PROBES SURVIVE THE ROUND (C2b), and they are the best
  thing in this unit.**  PROBE 2 (forced non-identity ⇒ G2/G3 is an
  artifact) fires against RAW, on every grammar substrate at both depths,
  and the outcome is refused there.  PROBE 1 (blind labeling ⇒ G1 is an
  artifact) fires nowhere.  **But PROBE 2's reach is narrower than its
  name**: as implemented it measures `|regs(e) ∩ regs(e′)|`, and its
  argument is written for RAW's first letter — it cannot detect a
  convention that forces non-identity by some other route (the referee
  exhibited one), and it was never applied to the *controls*, whose 0/58
  and 0/68 have the operational signature of a forced labeling and whose
  candidate mechanism §3(a) now supplies.  A **general** forcedness test,
  applied to the controls, is a residue.
- **The set-level cocycle column is GONE (round-1 MINOR 1).**  The labels
  are defined pointwise from one global record, so the set-level
  correspondence composes by construction; the first build printed a
  column for it whose predicate was literally `x == x`.  The tautology is
  now stated in words in C3's preamble and nothing is printed as if it
  had been measured.  The gated test is the **fibre-map** form, where
  each pair's transition is condensed to one partial map determined by
  the pair's *whole* overlap — that can fail, and it is what is measured.
- **Vacuous `all()` halves are printed as vacuous (round-1 MINOR 4).**  A
  cell with zero length-preserving maps no longer prints "inside ⟨τ⟩ =
  True, inside ⟨σ⟩ = True"; it prints that both are vacuous and neither
  is evidence, and such cells are excluded from the control flag.  C4's
  own gate no longer requires the length-changing class to be *non-empty*
  (round-1 NIT 4): a cleaner substrate with no height-skipping P-edges
  must be able to pass.
- **No invented thresholds.**  `|D| ≥ 2` and `|D| ≥ 4` are D58's own
  columns; the overlap predicate (≥ 2 shared directions) and the triple
  predicate (pairwise overlaps, ≥ 1 shared direction) are the pin's.
  Nothing else is used anywhere.
- **Nothing cut; caps printed.**  22 measurement cells, 3,582 overlapping
  pairs and 5,769 triples examined; group-closure caps (3,000 maps /
  3,000,000 compositions) printed, and the four sprinkling cells where a
  cap bound **name no group and say so in their own line**.  No cap binds
  anywhere a result is read.
- **Determinism is gated — ON THE SUBSTRATE'S REG CELLS ONLY, and the
  label now says so** (round-1 MINOR 7).  The substrate census — charts,
  pairs, triples, all four labelings, statuses, cocycle counts and the
  full map multiset — is recomputed in probe mode under
  `PYTHONHASHSEED` 0 / 7 / 999, byte-identical stdout at both depths.
  It does **not** cover the two grammar controls (where §3(b)'s demoted
  observation lives) or the REGA/COV instruments; the round-1 referee
  reports an external hash-seed check of the full substrate-plus-control
  census, and this gate is not it.  Noted in passing and not a bug here:
  `regs_of` breaks an `'r'` event's tie with `next(iter(...))` where this
  receipt's `reg_tuple` sorts by `repr` — a *different* tie-break,
  harmless only because every arbitration in these records has a single
  proposer, and C0b would catch a divergence.
- **AST anti-vacuity in d47a's SG8 form** (round-1 NIT 2): every
  `check()` predicate is a bare constant nowhere *and* references at
  least one run-bound name.  Its scope is stated (LOG #403 MA-2): it
  enforces exactly that and detects no vacuous gate in arbitrary
  syntactic form — C4's own vacuous halves were found by a referee, not
  by this scan.
- **Exit protocol.**  Exit 1 only on **anchor breakage — the C0 family**:
  C0 (the substrate reproduces D63's row), C0a (single sources), C0b
  (instrument validation), the three gates carrying `anchor=True`.  The
  pin's "exit 1 only on C0" names this family; code, note and pin now
  agree (round-1 NIT 1).  Every substantive negative — including C7's
  verdict, whichever way it had landed — exits 0.  The run exits 0.

## 6. Scope, held (pin §5)

Grammar layer; the five swept substrates only.  **No measure claim**
(transport scope has none — B1) and therefore **no typicality claim**.
**No physical-object claim** (#440, the scale doctrine).  Chart width is
capped at 4 by W4b on every delivery substrate, so **every tensor
sentence this licenses is a width-≤ 4 statement** — and after C7 it
licenses none.  Transfer to the identified interactive click law runs
through paper 29's missing map (D59) and is **not** claimed.  D63's ends
caveat applies to any band-membership sentence — this unit makes none.
ω is never invoked here; D58's containment theorem is used only as the
motivation the pin gives it (chart-pair inclusions are identity as set
maps, so the transition content must live in the coordinates), and this
unit confirms that reading by finding the content exactly there — and
then finding that the content is gauge.

## 7. Residues

1. **THE SUCCESSOR QUESTION, SHARPENED.**  Not "is Z/2 enough".  The
   question is: **can ANY substrate carry a transition class that is NOT
   a coboundary?**  Everything measured here — non-identity transitions,
   a clean cocycle, a closure, even a group name if one had been
   determined — is compatible with `H¹ = 0` and was, so none of it is
   the test.  The test is the obstruction count.  The **arbitration
   crystal** (D63 residue 1, the only species that can exceed width 4)
   inherits the question, and there is a *stated reason* to attack it
   there rather than a promise: what makes ε available here is that the
   fibre of a delivery event has exactly two ports with no intrinsic
   asymmetry, so "which is port 0" is free per chart; an arbitration
   event's conflict structure breaks that symmetry, and a labeling with
   no free per-chart Z/2 is the first place a non-trivial class could
   live.  Whether it does is unmeasured.
2. **The ambiguous pairs.**  27 of 172 at `d = 2` and 261 of 273 at
   `d = 3` carry a shared direction with two wire words in *both* charts,
   so the correspondence is not determined by the direction alone —
   and at `d = 2` those 27 are exactly the both-coupled pairs (§3(c)).
   Whether a finer labeling (an order on the word set, or a chart notion
   that splits such directions) resolves them is open.  It is the single
   biggest gap between this unit and a genuine manifold statement, and it
   is also what makes the pin's lean untestable at the coupled wires.
3. **A GENERAL forcedness test, applied to the controls.**  PROBE 2 is
   RAW-specific (§5).  The controls' 0-identity-at-100%-of-pairs has the
   signature of a forced labeling and was read as a finding.  A
   convention-independent test of forcedness, run on every cell, is
   owed before any substrate/control labeling contrast is asserted again.
4. **Full overlap ⟹ identity, on this substrate** (was: "no overlap
   exhibits a total fibre permutation").  This substrate **does** have 29
   wide–wide overlaps sharing all four directions, and every one of them
   carries the **identity** — so the measured fact is the *negative*
   answer: full overlap forces triviality here.  The sharp open question
   is whether a substrate exists whose wide–wide overlaps share all four
   directions and carry a **non-identity** total permutation.  That, not
   partiality as such, is what would turn "restriction of a group" into
   "element of a group".
5. **The length-changing transitions.**  7 pairs, from the 7 P-edges that
   skip a height; not fibre permutations; the COV surrogate does not
   remove them, and they are the only transitions that survive the ε
   relabelling.  Whether a regraded height or a cover-only relation
   removes them without changing the census is open.
6. **The cocycle at d = 3 and on the controls is untested** — not
   negative, undefined — and where it *is* tested it has one shape
   (§4 limit 4).  Making it testable requires residue 2.
7. **Which port convention is canonical.**  REG, REGA and COV disagree on
   the split and on the controls' classification, and the referee's
   fourth convention (port index read at the P-edge's target) disagrees
   with all three on the substrate.  The argument for REG is a reading,
   not a theorem, and it does not by itself select the endpoint at which
   the index is read.  The triviality of the class is the one outcome
   that so far survives every convention this unit has run.
8. **Size.**  177 events against 120-point sprinklings; D63's size
   residue is inherited.
