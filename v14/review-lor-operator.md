# LOR (paper-30) — OPERATOR-LENS HOSTILE REVIEW (K1)

**Seat:** K1 OPERATOR, panel protocol ledger v14 #253 (launch corrected at
#257; protocol unchanged).
**Object under test, at commit `2369290`, hashes verified at start AND at end
of this review, unchanged:** `v14/paper-30-lor.md` `f3e9e9df2c70` /
`v14/code/lor_exact.py` `878e6007b785` / `v14/code/lor_output.txt`
`427a5da397aa` / `v14/code/lor_receipt.json` `8b4ca74d954c`; pin
`v14/note-lor-pin.md` `5239c4671f1a`.
**Parents read at their terminal commits, hashes verified:** paper-21
`ef4a8c35a0c4`, paper-04 `dfa5090f26b1`, paper-06 `c350caab17ee`, paper-09
`006f96aaa2ff`, paper-19 `50bb81e67942`.
**Method:** every decisive target rebuilt from nothing with my own machinery
(`int` + `Fraction` only), from the PARENTS' committed definitions.
`lor_exact.py` was never used as an oracle for a number; it was read only to
locate two mutation sites and to learn the driver's interface. The weld
detector was re-implemented from paper-19's committed `count_field` / fiber
semantics in `v14/code/r3_weld_exact.py`, not from the delivered code.
Interpreter `/opt/homebrew/bin/python3.13`.

---

## VERDICT

**GRADE: AWF (ACCEPT WITH FIXES).**

The verdict stands unmoved in all four segments. Every decisive target
reproduces exactly. **Zero false numbers**: of the ~226 independent
recomputations below, every published numeral in the object under test that
bears on a measurement was reproduced from scratch and agreed. The two
mismatches my rebuild threw were my own errors (a wrong guess at I7's declared
count box, and a malformed transitivity predicate), both resolved against the
parents' committed declarations. One measured discrepancy remains and it is a
**stamping** discrepancy, not a false number — MINOR-1 below, which requires a
head-segment fix.

**Recomputations: 226.**
Stage 1 (substrate/arena/laws/SIG/ceiling) 80 + 3 box; stage 2 (refinement
step, extended-carrier weld, completions) 63; stage 3 (cut loci, footprint
census, abstract-vs-dictionary, compatibility, DIA) 43; stage 4 (driven W6,
my own driver over the committed grammar) 14; base-map probe 7; verbatim
provenance 8; numeral sweep 84 distinct literals / 662 occurrences; byte
reproduction 2; out-of-harness mutants 2.

---

## 1. Target-by-target

| # | target | verdict |
|---|---|---|
| 1 | the (2,2,2) arena from concatenation; weld zero-free; splittable census at n=2 | **REPRODUCED** |
| 2 | 04's dyadic 27/27 at raw fiber 1; 06's unique 27/27; 09's emptiness in {1,2} | **REPRODUCED** |
| 3 | one-step commutation: additivity 27/27, restriction 27/27, readout 9/9 | **REPRODUCED** |
| 4 | **the extended-carrier weld (hardest)** | **REPRODUCED, every clause** |
| 5 | the process-supplied halves: cut loci, R=9 control, footprints | **REPRODUCED** (+MINOR-3) |
| 6 | abstract-vs-dictionary: 864 / 72 / the two dead classes' 432 | **REPRODUCED** |
| 7 | the completion census: 36/36 admissible, UNMOTIVATED at 24/3/2 | **REPRODUCED** (+MINOR-1, MINOR-2) |
| 8 | compatibility: 06's support = 04's fiber 27/27; 108/108 | **REPRODUCED** |
| 9 | ceiling/ladder: one step; R=12; L_max = 3·2^⌊log₂ m⌋ | **REPRODUCED** |
| 10 | SIG feed (det 3 → 3/4 = 2^d; (+,+) 36/36; paper-19's 3/4); DIA rows | **REPRODUCED** |
| 11 | W6: 16 driven; every other column exhaustive | **REPRODUCED**, license clean |
| 12 | two mutants outside the harness; the 771-numeral sweep | **BOTH DIE**; sweep clean |

### 1.1 The arena (target 1)

Rebuilt from d66's own object: 9 actors on (Z₃)², link set {(1,0),(0,1),(1,1)},
27 (site,link) cells, the declared pair of a cell = {x, x+ℓ}.

- partitions of nine into three triples: **280**, twice (exhaustive
  enumeration; and 9!/(3!³·3!) from a factorial computed in my run).
- incidence spectrum **{0:1, 4:27, 6:54, 7:162, 9:36}**, sums to 280.
- **36** saturating partitions; and I verify the equivalence the paper leans
  on but does not state: *saturating ⟺ all three groups are declared triples*.
- the budget theorem: max 9 incidences per round, 6×9 = 54 = 27×2.
- the 72 I7-STRICT triples by **two routes that share no code** — the summed
  incidence field ≡ 1, and the pair-cover-once route that forms no incidence
  vector. Both **72**; the two sets are equal. 36³ = **46,656** pay the full
  27; **1 in 648**.
- 72² = **5,184** ordered concatenations; per-cell count **2 at all 27 cells**
  at **5,184 of 5,184**, each tested independently.
- the coarse weld re-verified zero-free in-arena with my own detector:
  **1,296** isomorphisms (= |Aut K₃,₃,₃| = 3!·(3!)³), fibers **1/1/1**,
  FOUND-candidate. Recomputed under the plain name order: **1,296** again, so
  the connected pruning order is not one of the values the instrument returns.
- I independently confirm the co-division relation IS K₃,₃,₃, its three parts
  being the three (1,2)-lines — the 9 undeclared pairs are exactly the missing
  direction's.
- splittable census at n = 2: fiber (1,1) at every one of the 27 intervals,
  raw product **1**; the R = 4 counterfactual product **0**.

### 1.2 The laws (target 2)

- **paper-06**: at count 2 the fiber is one point, orbits 1, simplex dimension
  0 = n−2, pinned-transitive — read off paper-06's committed per-interval law,
  not off the delivered code. Unique at **27 of 27**, hence at the record
  level. Against **9 of 27** at R = 4.
- **paper-04**: dyadic raw fiber **1**, subdivides **27 of 27**.
- **paper-09**: support holes {1,2}; this record carries only count 2, so
  **all 27** intervals sit in the hole; empty. Checked against paper-09's own
  committed `SUPPORT-HOLES={1,2}` segment.
- I7's declared count box, taken from HA's committed declaration
  (1 ≤ n_e1, n_e2 ≤ 6; 1 ≤ n_diag ≤ 12; positive definite): **361** admissible,
  **261** splittable, and **exactly one** point with a single-point raw fiber,
  namely **(2,2,2)** — paper-06's committed `LATTICE=SPLITTABLE-261-OF-361|
  PINNED-TRANSITIVE-1` reproduced independently.

### 1.3 The step and the new places (target 3)

Refined lattice (Z₆)², 36 sites, 108 slots. Image map x ↦ 2x; interior site of
[x,x+ℓ] is 2x+ℓ. Every refined site classified exactly once:
**IMAGE 9 / MID(1,0) 9 / MID(0,1) 9 / MID(1,1) 9**, zero left over.
Determined slots **54**, free **54**, partition of the 108 exact — and this
reproduces paper-04's own committed "54 of the 108 refined links lie on no
coarse interval" one arena down.
Additivity **27/27**, restriction **27/27** under BOTH declared completions,
I7 readout recovered at **9/9** sites. Record-IS-metric commutes, shown.

### 1.4 The extended-carrier weld — the hardest target (target 4)

Every clause rebuilt per object, none assumed:

- the carrier ACTOR ⊕ CO-DIVISION-PAIR → SITE (9 + 27 = 36) is a **bijection**
  onto the 36 refined sites. The pair ↔ cell correspondence is itself a
  bijection because 2ℓ is not declared for any declared ℓ.
- the **54** determined links are **exactly** the 54 actor-in-pair incidences
  (27 pairs × 2), verified link by link, zero exceptions.
- the **54** free links each join two pairs whose union is a **non-collinear
  declared triangle**, **3 per triangle**, all **18** triangles carrying 3, and
  **no** free link's union is one of the 9 declared lines. Zero off-rule links.
- **Aut = 432**, by my own isomorphism search AND by an independent
  factorisation: 36 translations × a point stabiliser I measure to be 12.
- fibers **1/1/1**, **zero free items**, FOUND-candidate at the
  process-supplied completion; base-map invariant at all 432.
- the bare nine-actor carrier against the 36-site target: **ARITY-DEAD**.
- the fiber theorem's premise checked rather than cited: the refined arena is
  **vertex-transitive** (one vertex orbit of 36) and **edge-transitive** (one
  edge orbit of **108**), so an Aut-invariant count field is constant. The
  paper asserts this; I measured it.

### 1.5 The process-supplied halves (target 5)

- 18 division events, **17** loci. Exhaustive over all **5,184** witnesses:
  the live-locus set is **{9}** at **5,184 of 5,184**, and the split there is
  **(1,1) at 27 of 27**. Second route, sharing no state: the counting identity.
- R = 9 control: raw split fiber (3−1)²⁷ = **134,217,728**; live loci
  **{9,…,18}**, **ten**, on every sampled three-block record.
- the footprint census, exhaustive over 5,184, reproduces **all nine classes
  with all nine counts exactly**, summing to 5,184; canonical-carrier
  isomorphism at **72**; edge-count census **{81: 432, 99: 3,888, 108: 864}**;
  **864** right-shaped, **792** right-shaped without the carrier.

### 1.6 Abstract vs dictionary (target 6)

Confirmed at the level the paper claims and one level deeper. The two dead
classes `triangles-9|lines-9` and `triangles-12|lines-6` each admit **432**
abstract isomorphisms onto the refined lattice with fibers **1/1/1**, while
the canonical carrier on them induces **27** and **18** zero cells
respectively. The result is real: structural isomorphism is not the dictionary.

Two mechanisms I derived that the paper does not state and which make the
census forced rather than fitted (offered as strengthening, not correction):

1. **the closed form** `edges = 54 + 3·(distinct triangles) + 3·(distinct
   lines)` accounts for all nine classes and for the whole edge-count census.
2. **the resolution composition.** The 72 triples are 12 unordered
   resolutions, and I measure their composition to be exactly
   **2 all-triangle (9,0), 1 all-line (0,9), 9 mixed (6,3)**. The entire
   census follows: 18|0 = the two all-triangle resolutions crossed with each
   other, 6·6 twice = **72**; 9|0 = each all-triangle resolution with itself,
   2 × 36 = **72**; 0|9 = the single all-line resolution, 6·6 = **36**.

### 1.7 Ceiling, ladder, SIG, DIA (targets 9, 10)

⌊log₂ 2⌋ = 1; after the step min n = 1, ceiling 0; a second step needs min n = 4
⟹ R = 12. Ladder rows (m, R, ceiling, refined side, places) reproduced at
**(1,3,0,3,9) (2,6,1,6,36) (3,9,1,6,36) (4,12,2,12,144) (8,24,3,24,576)**, and
I verify the two claims the table only illustrates: L_max ≤ R for all m ≤ 64,
with **equality exactly at the dyadic m** — the dyadic budgets in 1..64 being
{3,6,12,24,48,96,192}, of which the paper tabulates [3,6,12,24].

SIG: coarse q = [[2,−1],[−1,2]], det **3**; refined q = [[1,−1/2],[−1/2,1]],
det **3/4**; ratio **4** = 2^d at d = 2, exactly, as Fractions; signature
(+,+) unmoved, positive definite at **36 of 36**; the refined det is exactly
paper-19's committed **3/4**. Under paper-04's completion the spectrum is
**{3/4, 1, 7/4}**; all three posdef.

DIA: withdrawing the diagonal leaves **18** coarse intervals and **9** refined
sites on no coarse interval, and I confirm they are **exactly the odd-odd
parity class**; each declared direction buys **9**; site-complete at 36 with
the diagonal. Paper-04's committed 27-of-216 at d = 3 reproduced as a citation.

### 1.8 The W6 window (target 11)

I wrote **my own** schedule driver to d66's `conflict_grid(3,R)` cycle over the
**committed** d42b1 grammar and d60's `B`, and declared **my own** 16-schedule
window (6 surviving stratum, 8 one per dead class, 2 seed-fan) without reading
the delivered window. Result at all 16: **18 divisions**, footprint sizes [3],
**every footprint exactly its conflict group**, **maxhits 1**, **no refusal**,
driven link field = combinatorial field at **432 of 432** compared cells, event
lengths spanning **99…102**. My independently-chosen surviving-stratum
schedules landed on the same canonical triples the delivered rows carry.

**The window license is clean.** Every other column I checked is exhaustive
over an object the window does not cap, and I re-ran each exhaustively: 280
partitions, 36 saturating, 46,656 full-payers, 72 triples (two routes), 5,184
witnesses (per-cell count, cut loci, footprint census), 361/261 box points,
108 slots, 36 sites, 432 base maps. The head's `@WINDOW-16-DRIVEN-OF-5,184-
WITNESSES` stamp is accurate and is the only windowed column.

### 1.9 Instrument, byte reproduction, mutants (target 12)

- Ran the delivered code in a clean provisioned mirror containing only the 19
  pinned sources. Exit 0; both artifacts **byte-identical** to the committed
  ones (`427a5da397aa`, `8b4ca74d954c`).
- **Two mutants outside the declared 41.** Neither target is named by any
  declared mutant's `corrupts` field.
  - **MUT-OP-1** — the non-collinearity predicate, `TRIANGLES` widened to all
    27 declared triples. **Exit 1, artifacts byte-unchanged.** Note: it dies by
    an uncaught `IndexError` at `full_run` line 1645 rather than at a named
    gate. The write discipline holds (nothing is written), but the geometry is
    load-bearing enough that its corruption makes the run impossible rather
    than wrong; no gate names it.
  - **MUT-OP-2** — paper-04's transcribed minimal completion, K: 1 → 2. Dies
    at **G-PAPER-CLAIMS** (`claims 14, missing ['refined_weld']`), artifacts
    byte-unchanged. The paper-04 completion numbers ARE gated, through the
    rendered sentence.
- **Numeral sweep.** 84 distinct numeral literals, 662 occurrences, over the
  whole object including fenced blocks and inline spans. Every one is either
  in my independently verified ledger or is a paper number, ledger number,
  hash prefix or date. **No unverified physics numeral.**
- **Verbatim provenance.** All 8 block quotes accounted for: 7 word-for-word
  in a pinned parent (paper-21 ×2, paper-04 ×3, paper-06 ×1, and the RSQ
  theorem verbatim in `r4dec_receipt.json`), 1 this unit's own rendered
  measured claim (`paper_claims/rendered/carrier`). **Zero unsourced.**

---

## 2. Findings

### MAJOR — none.

### MINOR-1 (REQUIRED FIX, head-bearing) — the label fiber at paper-04's completion is base-map-VARIANT and is published unstamped

**Measured.** I re-read the I-DIRECTION-LABEL fiber at **all 432** base maps
under paper-04's declared minimal completion. It is **not constant**:

| fiber value | base maps |
|---|---|
| 6 | **360 of 432** |
| 3 | **72 of 432** |

The I-ORIENT fiber is 2 at all 432; I-SITE-ASSIGNMENT is 24 by construction
(a count over all maps). My own detector, at its own base map, returns **6**.

**The instrument is honest.** `lor_receipt.json` publishes
`label_fiber_spread: [3, 6]`, `fibers_base_map_invariant: false`, and
`free_items_at_every_base_map: 3`. **The paper is not.** Head segment 3 carries
`UNMOTIVATED(FIBERS-24/3/2)` and §6.5 says "the same carrier returns
UNMOTIVATED with fibers 24/3/2" — with no stamp anywhere, and 3 is the value at
one base map in six. §10's choice-inventory row 11 is likewise silent.

This matters because **paper-19, the direct precedent and a pinned source of
this unit, was made to state the invariance explicitly** by its own operator
round — the repair note is still in `r3_weld_exact.py` at the fiber
computation, and paper-19 §5.4 reads "both are re-read at every one of the
1,296 base maps and both are constant". LOR re-reads at 432, finds them NOT
constant, and does not say so in prose.

**The verdict is unaffected**: the fate is UNMOTIVATED at every base map, and
the receipt's own `free_items_at_every_base_map: 3` establishes that all three
items are free everywhere. This is a stamping defect on a head numeral, not a
false number.

**Exact repair.**
1. Head segment 3: replace
   `UNMOTIVATED(FIBERS-24/3/2)`
   with
   `UNMOTIVATED(FIBERS-24/3-OR-6/2:LABEL-FIBER-BASE-MAP-VARIANT-SPREAD-[3, 6];FREE-AT-EVERY-BASE-MAP-3)`
   (and the same in §11's repeat of the segment).
2. §6.5, after "…returns UNMOTIVATED with fibers 24/3/2", add: "The
   site-assignment fiber 24 is a count over all base maps and the orient fiber
   is 2 at every one; the label fiber is **base-map-variant**, 3 at 72 of the
   432 base maps and 6 at the other 360, and the run publishes the spread.
   What is base-map-invariant is the fate: all three items are free at every
   one of the 432, so UNMOTIVATED does not depend on the reading base map."
3. §10 row 11: add the stamp to the "where it binds" cell.

### MINOR-2 (REQUIRED FIX) — "designed to put each refined site on the diagonal locus" is contradicted by this unit's own measurement at 9 sites

§6.5 says "Paper-04's own minimal completion was designed to put each refined
site on the diagonal locus". That is a faithful report of paper-04's committed
`make_free` docstring, but the design is **not achieved** at this arena, and
the paper's own §6.6 det spectrum {3/4, 1, 7/4} already records it. Measured:

| site class | code | q₁₂ | on the diagonal locus (q₁₂ = 0)? |
|---|---|---|---|
| IMAGE (9) | (1,1,1) | −1/2 | no (not completed) |
| MID(1,0), MID(0,1) (18) | (1,1,2) | **0** | **yes** |
| MID(1,1) (9) | (2,2,1) | **−3/2** | **no** |

The rule reaches the locus at **18 of the 27 sites it completes** and 18 of 36
refined sites. At the diagonal-midpoint sites the known count is the diagonal
one (c = 1), so the rule's third branch sets a = b = c + K = 2 and c = a + b is
unreachable — a and b would have to sum to 1.

**Exact repair.** Replace with: "Paper-04's own minimal completion was designed
to put each completed refined site on the diagonal locus; measured here it
reaches it at 18 of the 27 sites it completes — at the 9 diagonal-midpoint
sites the known count is the diagonal one, so the rule's own branch returns
(2,2,1) with q₁₂ = −3/2 and the locus is unreachable. It is admissible at all
36 sites and it makes the refined record inhomogeneous…"

### MINOR-3 (STRENGTHENING) — the cut-locus results are counting theorems and should be stated as such

§6.3 presents the unique live locus as measured "at all 5,184 witnesses" and
the R = 9 control's ten as a contingent fact. Both are one-line theorems, and
saying so strengthens the unit rather than weakening it. Because every group of
an I7-STRICT triple is a declared triple, each division event deposits exactly
3 cell-incidences, so cutting after k events puts Σ_cells a = 3k. Strict
positivity of both halves at an all-count-n record requires 1 ≤ a ≤ n−1 at each
of the 27 cells, hence **27 ≤ 3k ≤ 27(n−1)**. At n = 2 that is 3k = 27, so
**k = 9 uniquely**, and k = 9 IS live exactly because block 1 covers every cell
once — which is the I7-STRICT condition itself. At n = 3 it is 9 ≤ k ≤ 18,
**exactly ten**, and I verify every one of those ten is in fact live.

**Exact repair.** Add after the "Measured, by two routes…" sentence in §6.3:
"The count also settles it as a theorem: each event deposits three cell
incidences, so a cut after k events distributes 3k over 27 intervals, and
strict positivity at an all-count-n record forces 27 ≤ 3k ≤ 27(n−1). At n = 2
that is k = 9 alone; at n = 3 it is the ten loci 9…18, all of which are
measured live. The exhaustive census over the 5,184 witnesses confirms it
rather than discovering it."

### MINOR-4 (COSMETIC) — a dangling "respectively"

§6.4's "the field it induces carries 27 and 18 zero cells respectively" refers
to no preceding ordered list. Read off the §6.4 table's own order
(`triangles-9|lines-9` before `triangles-12|lines-6`) the sentence is
**correct**; the receipt's `abstractly_isomorphic_dead_arenas` lists them the
other way round. **Exact repair:** name them — "…carries 27 zero cells at
`triangles-9|lines-9` and 18 at `triangles-12|lines-6`."

---

## 3. What I could not fault

- The four verdict segments' arithmetic, in full. Every count, every ratio,
  every fraction.
- The extended-carrier weld, the unit's hardest and newest object: the
  36-bijection, the 54 determined = actor-in-pair incidences, the 54 free =
  3 per triangle across all 18, Aut 432, fibers 1/1/1, the bare carrier's
  arity-death. Rebuilt clause by clause with an independent detector; nothing
  moved.
- The completion relativity, which is the honest core of the paper: the
  link-constant completion IS unique (the determined half is already 1 at all
  54 slots, so link-constancy leaves nothing free), it IS the one under which
  the weld carries zero free items, and paper-04's own declared completion IS
  equally admissible at 36/36 and does not. Reported as a relativity, not
  resolved. Correct.
- The abstract ≠ dictionary result, which is the paper's own claim to be the
  thing it did not anticipate. It survives at full strength.
- Reproducibility: byte-identical from a clean 19-source mirror; both
  out-of-harness mutants die with artifacts untouched.
- The window license and the exhaustive columns.
- The walls. No expansion reading, no cosmological reading, no Lorentzian
  reading is taken anywhere in the object, and the naming in §6.6 is explicit.

---

*Operator seat closed. Object hashes re-verified unchanged at the end of the
review; no repo state outside this file was written.*
