# D64 — result: **G3. THE ATLAS CARRIES A G-STRUCTURE — Z/2, and the coupling changed WHICH involution it is.**

**Status: GREEN-UNREVIEWED, 2026-07-26.**  An independent hostile round
follows and nothing here is terminal.  Pin `note-d64-cocycle-pin.md`
(STRICT, frozen and committed before this file existed).  Receipt
`v10/code/d64_cocycle_exact.py`, output
`v10/data/d64_cocycle_exact.out` — **12 PASS / 0 FAIL, exit 0, ~60 s
wall clock** (run from the repo root).  Parents: D63 (the substrate,
TERMINAL), D58 (the atlas and its containment theorem), W4b (the
branching bound), D42b1 (the transport grammar and `event_poset`).

---

## 1. Which outcome fired, and at which labeling

The pin pre-registered three outcomes and let the census decide.

> **G3 FIRED — at the canonical (ROLE) wire-word labeling, on the wide
> crystal, at d = 2.**  Of the **172 overlapping chart pairs** of
> DOUBLE-RING(8, 10, 8) (charts sharing ≥ 2 directions), **57 carry the
> identity transition and 115 carry a NON-IDENTITY one**; on the **wide
> subatlas** — the 137 pairs both of whose charts have `|D| = 4`, the
> delivery grammar's ceiling — the split is **29 identity / 108
> non-identity**.  All **111** chart triples with pairwise overlaps and
> a non-empty triple intersection are testable at the fibre-map level
> and **all 111 satisfy the cocycle; zero violations**.  The
> length-preserving transitions are **CLOSED under composition** and
> every one of them is a restriction of the identity or of **τ**, the
> **first-letter wire transposition** `(b₁, b₂) ↦ (1 − b₁, b₂)` — in
> words: *the direction chart `e` leaves by the wire it SENT on, chart
> `e′` leaves by the wire it RECEIVED on*.  **The group generated is
> Z/2 = ⟨τ⟩**, a fixed-point-free involution of the 4-point wire fibre
> `{0,1}²`, i.e. the double transposition `(00 10)(01 11)` in S₄.

**The outcome is NOT read at the RAW labeling, and the receipt says why
before it says anything else** (C2b, PROBE 2).  On every grammar
substrate at both depths, *every* overlapping chart pair has base
events with **disjoint register sets**; a raw wire word's first letter
is always a register of its own base event; therefore raw labels can
*never* agree and RAW's "non-identity at 172/172" is a **tautology of
the labeling**, not a fact about the atlas.  A G3 read at RAW would be
an instrument artifact and is refused.

The mirror probe does **not** fire: **no labeling on any substrate at
any depth is blind** (C2b, PROBE 1 — at every one of the 22 cells some
direction carries different labels in different charts).  So a G1
reading, had the census produced one, would *not* have been an artifact
of a labeling that cannot see transitions.  The ROLE labeling is the
one that is neither forced nor blind, and it is where the outcome is
read.

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

**FIRST-role reproduces ROLE exactly at d = 2 and not at d = 3**: at
depth 2 *all* the transition content sits in the first wire letter; at
depth 3 the later letters carry content too.  That is a measured fact
about this substrate, not a theorem.

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

Sprinkling parameters printed by the receipt: d55c's repaired `latt`,
`N = 120`, `box = 60` (M²⁺¹) and `box = 48` (M³⁺¹), `seed = 8`,
`T = 4·box`, orders by `mink4`.

## 3. The three findings, and two of them run against the guess

**(a) A NON-IDENTITY ATLAS IS THE GENERIC CASE HERE, NOT WHAT THE
COUPLING BOUGHT.**  Not one control is flat.  D60's uncoupled brick and
the uncoupled double ring have **zero** identity transitions at both
depths (58/58, 56/56, 68/68, 61/61 non-identity), and the two genuine
sprinklings are non-identity at 244/247, 382/383, 366/370, 516/518.
What the *wide crystal alone* has is (i) a substantial **identity**
fraction — 57 of 172 pairs, the only substrate in this census with a
trivializable part; (ii) the **wide subatlas**: pairs of 4-direction
charts, which at d = 2 exist **only** on the coupled substrate (brick
0, uncoupled double ring 0, substrate 137), so only there is this a
transition between charts of the delivery grammar's *maximal* width;
and (iii) a **different structure group**.

**(b) THE CONTROLS CARRY THE OTHER INVOLUTION.**  At the canonical
labeling every length-preserving transition of the uncoupled brick and
of the uncoupled double ring is a restriction of **σ**, the
**all-letter flip** `(b₁, b₂) ↦ (1 − b₁, 1 − b₂)` — the *other*
fixed-point-free involution of `{0,1}²`, the double transposition
`(00 11)(01 10)` — and **none** is a restriction of τ; on the substrate
**none** is a restriction of σ.  Both groups are Z/2; they are
**different subgroups of S₄**.  So the coupling did not create a
transition structure — **it changed which involution the atlas
carries**, and it added the chart width the transition acts on.

**(c) THE PIN'S LEAN LANDS SPLIT, AND BOTH HALVES ARE REPORTED.**  The
pin leaned on "a non-identity wire transposition at COUPLED wires,
because even and odd height neighbourhoods are not congruent".

- **CONFIRMED, the parity half.**  Every single one of the 115
  non-identity pairs sits in an **odd** height layer; the identity
  pairs split 28 even / 29 odd.  The per-layer census alternates
  cleanly from h = 23 upward: odd layers `4 identity / 16
  non-identity`, even layers `4 identity / 0 non-identity`.
- **REFUTED, the coupled-wire half — and inverted.**  Every pair *both*
  of whose base events is an inter-ring (coupled) delivery is
  **identity** (27 of 27).  108 of the 115 non-identity pairs have **no**
  coupled base at all; the remaining 7 are *mixed* pairs (one coupled
  base, one not).  The wire transposition is a property of the brick
  circuit's own direction alternation, which the coupling stitches
  together — not of the coupling wires.

## 4. The licensed claim, no wider than the measured census

> **THE LICENSED CLAIM.**  On the substrate DOUBLE-RING(8, 10, 8), at
> SKY-B depth **d = 2**, at the canonical wire-word labeling: the
> overlapping-chart transitions are **not all identity** (115 of 172
> pairs, 108 of 137 wide–wide pairs), they **satisfy the cocycle** on
> every one of the 111 testable triples, and the length-preserving ones
> **close** to the group **Z/2 = ⟨τ⟩**, τ the first-letter wire
> transposition, a fixed-point-free involution of the 4-point wire
> fibre.  This is a **width-≤ 4** statement (W4b caps chart width at
> `B^d = 4` on every delivery substrate), about **this substrate at this
> labeling at this depth**, and no wider.

Five limits, all measured, all reported whichever way they landed:

1. **The non-identity maps are PARTIAL.**  Every τ-transition is
   defined on **2 of the 4** fibre points; the only transitions defined
   on all four are the 29 identity ones.  So the licensed sentence is
   *"every length-preserving transition is a restriction of an element
   of ⟨τ⟩, and ⟨τ⟩ is the smallest group containing them"* — **not**
   that any single overlap exhibits a total fibre permutation.
2. **7 transitions are LENGTH-CHANGING and belong to no permutation
   group.**  They exist because P has edges that **skip a height** —
   C0b counts 7 such on the substrate (335 P-edges vs 328 covers; 3 on
   the brick, 7 on the uncoupled ring pair) — so one chart reaches a
   shared direction in *one* P-step where the other needs two.  They
   are excluded from the group **by name**, not by silence, and counted.
3. **27 of the 172 pairs carry no single-valued correspondence at
   all** ("ambiguous": a shared direction carrying two wire words in
   *both* charts, so words cannot be paired by the direction alone).
   At d = 3 this rises to 261 of 273, which is why —
4. **the cocycle test has NO CONTENT at d = 3, and none on the two
   grammar controls.**  There every triple is "undefined" (some pair's
   correspondence is not single-valued, or the composed domain is
   empty).  Across the whole census 993 triples were tested with a
   defined composition and 4,776 were undefined; **zero violations**.
   "The cocycle holds" is therefore a statement about the substrate at
   **d = 2** and about the two sprinklings — on the controls it is
   *untested*, not confirmed.
5. **The port-order convention matters to the SPLIT, not to the
   EXISTENCE.**  Running the same instrument with registers sorted by
   name instead of the layer's own tuple order (REGA) gives 85/87
   instead of 57/115 at d = 2, and dissolves the controls' clean σ
   classification (14 of 19 brick pairs become unclassified "other").
   What is convention-robust across REG, REGA and the register-free COV
   surrogate: **non-identity transitions exist, and the cocycle is
   clean**.  What is not: the identity/non-identity *ratio*, and the
   *name* of the group.  This unit argues the layer's own delivery
   tuple order `(sender, receiver)` is the canonical one *because it is
   the layer's own*, and prints the alternative beside it.

**And the honest size of "G-structure": Z/2 is a DISCRETE group.**  It
is a genuine structure group and it is the object the tensor programme
asked for, but it is not GL(n), not a Lorentz group, and carries no
continuous parameter.  What the wide crystal's atlas has at this
labeling is a **Z/2 gauge structure at width ≤ 4**, and any sentence
about tensors, curvature or connections must start from that and not
from more.

## 5. Instrument hygiene and validation

- **Single sources (C0a).**  The transport grammar by text-slice from
  committed d42b1 (cut at its own banner print); the sky instrument
  (d47a), the repaired sprinkling generator (d55c), the atlas (d58),
  D60's blueprint machinery and **D63's own `double_ring` /
  `wide_brick`** by AST extraction.  The substrate this unit charts is
  D63's function object, not a re-typing of it.  Exit-freedom of the
  slice and of all 55 extracted bodies is **gated**, not asserted.
- **The anchor (C0, exit 1 on breakage).**  `double_ring(8, 10, 8)`
  reproduces D63's committed row exactly at both depths: 177 events,
  d = 2 homogeneity **47/59** (≈ 0.7966), `|D| ≥ 4` at **1/3**,
  `max |D| = 4`, mean ω **100/137** (≈ 0.7299); d = 3 **137/177** and
  **119/177** with `max |D| = 4`.  The brick control is D60's brick
  **event for event**, reproducing 10/13, 125/192, 0, 3.  No refusals.
- **THE INSTRUMENT IS VALIDATED, NOT ASSERTED (C0b).**  `reg_tuple` is
  `regs_of` with an order — same set at every event of every record;
  each event has at most `|regs_of|` P-successors (W4b's joint, the D63
  round-1 referee's own section-G check); and **the transitive closure
  of P EQUALS the committed order `poset_of`** on all three grammar
  substrates.  That last is the gate that makes the wire words a
  *reading of the committed layer* rather than a new structure.  The
  covering relation is contained in P, and the COV surrogate's own
  closure is the committed order on **every** substrate including the
  sprinklings.  *This gate earned its keep: it caught a real bug in the
  first build (a closure accumulated in index order, which is not a
  topological order on a sprinkling) before any census was read.*
- **Two structural facts gated in passing (C1).**  The P-path
  enumeration reaches **exactly** SKY-B's `D_e(d)` at every base event
  of every substrate at both depths; and **every overlapping chart pair
  is same-height** (`D_e(d)` lies in the single layer `h[e] + d`), so
  the pair census is layer-local — 0 cross-height overlapping pairs
  across all 22 cells.
- **The cocycle test's tautological half is named as such (C3).**  The
  labels are defined pointwise from one global record, so the
  *set-level* correspondence composes by construction; the receipt
  computes it and reports it as a tautology.  The gated test is the
  **fibre-map** form, where each pair's transition is condensed to one
  partial map determined by the pair's *whole* overlap (larger than the
  triple intersection) — that can fail, and it is what is measured.
- **No invented thresholds.**  `|D| ≥ 2` and `|D| ≥ 4` are D58's own
  columns; the overlap predicate (≥ 2 shared directions) and the triple
  predicate (pairwise overlaps, ≥ 1 shared direction) are the pin's.
  Nothing else is used anywhere.
- **Nothing cut; caps printed.**  22 measurement cells, 3,582
  overlapping pairs and 5,769 triples examined; group-closure caps
  (3,000 maps / 3,000,000 compositions) printed, and the four
  sprinkling cells where a cap bound **name no group and say so in
  their own line**.  Determinism is **gated**: the whole substrate
  census — charts, pairs, triples, all four labelings, correspondence
  statuses, cocycle counts and the full map multiset — recomputed in
  probe mode under `PYTHONHASHSEED` 0 / 7 / 999, byte-identical stdout
  at both depths.
- **Exit protocol.**  Exit 1 only on C0/C0a/C0b anchor breakage;
  substantive negatives exit 0.  The run exits 0.

## 6. Scope, held (pin §5)

Grammar layer; the five swept substrates only.  **No measure claim**
(transport scope has none — B1) and therefore **no typicality claim**.
**No physical-object claim** (#440, the scale doctrine): an atlas with a
structure group is a MECHANISM certificate, never an object.  Chart
width is capped at 4 by W4b on every delivery substrate, so **every
tensor sentence this licenses is a width-≤ 4 statement** and must say
so.  Transfer to the identified interactive click law runs through
paper 29's missing map (D59) and is **not** claimed.  D63's ends caveat
applies to any band-membership sentence — this unit makes none.  ω is
never invoked here; D58's containment theorem is used only as the
motivation the pin gives it (chart-pair inclusions are identity as set
maps, so the transition content must live in the coordinates), and this
unit confirms that reading by finding the content exactly there.

## 7. Residues

1. **The ambiguous pairs.**  27 of 172 at d = 2 and 261 of 273 at d = 3
   carry a shared direction with two wire words in *both* charts, so
   the correspondence is not determined by the direction alone.
   Whether a finer labeling (an order on the word set, or a chart notion
   that splits such directions) resolves them — and whether the
   ambiguity localizes where a finer chart notion is *needed*, which is
   what the pin's G2 branch was for — is open.  It is the single
   biggest gap between this unit and a genuine manifold statement.
2. **The length-changing transitions.**  7 pairs, from the 7 P-edges
   that skip a height.  They are not fibre permutations and the COV
   surrogate does not remove them.  Whether a regraded height, or a
   cover-only relation with a compensating definition, removes them
   without changing the census is open.
3. **The cocycle at d = 3, and on the controls, is untested.**  Not
   negative — undefined.  Making it testable requires residue 1.
4. **Partiality.**  No overlap exhibits a total fibre permutation: the
   τ-transitions see 2 of 4 fibre points, the 4-point transitions are
   all identity.  Whether a substrate exists whose wide–wide overlaps
   share all four directions — which would force a total permutation
   and turn "restriction of ⟨τ⟩" into "element of ⟨τ⟩" — is open and
   sharp.
5. **The parity mechanism is measured, not proved.**  Every
   non-identity pair sits at odd height and the layers alternate; the
   co-occurrence with the brick's `t % 4` direction alternation is
   evident but no proof that the alternation *forces* the transposition
   is given (the same shape D63's residue 3 has for its layer census).
6. **Which port convention is canonical.**  REG and REGA disagree on
   the split and on the controls' classification.  The argument for REG
   (it is the layer's own tuple order) is a reading, not a theorem.
7. **Z/2 is discrete.**  The tensor/curvature programme now has *an*
   object, but a Z/2 gauge structure at width ≤ 4 is a long way from a
   connection.  What a continuous structure group would require — and
   whether the arbitration crystal (D63 residue 1, the only species that
   can exceed width 4) could carry one — is the successor question, and
   it is now sharp.
8. **Size.**  177 events against 120-point sprinklings; D63's size
   residue is inherited.
