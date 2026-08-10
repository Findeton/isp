# WELD 2 (paper-13, the carrier census) — OPERATOR-LENS HOSTILE REVIEW

**Reviewer:** OPERATOR lens (the from-scratch rebuild).
**Protocol:** `v14/note-w2-hostile-protocol.md` (`e7b99e05557d`, commit
`331dae7`), rows K1–K4.
**Object, hash-verified at start and unchanged at end:** paper
`535e288ff412`, code `290149118b9d`, output `5e35e7a0115f`, receipt
`bacdb7a5e985`; pin `9d19515cb3ae`.

## GRADE: **ACCEPT-WITH-FIXES**

**Recomputations: 115.** Every delivered number I could rebuild
reproduced exactly — **0 of the unit's numbers diverged from my
rebuild.** The verdict `WELD2-EMPTY-AT-THE-DECLARED-FAMILY-
THE-ARITY-CYCLICITY-SCISSORS` is **confirmed**, and the mechanism is
**strengthened** by this review at three points (§B below), including the
one experiment §9.3(i) registered as able to move it.

Two defects earn the FIXES: the census's `×2 carriers` axis is **inert**
(the 60 candidates are 30 computations run twice under two labels, and the
paper describes them as separately built), and one prose cell in the §2.2
ruling-properties table carries a number **the program never computes**.
Neither moves the verdict; both are describable and cheaply repaired.

---

## A. WHAT I REBUILT, AND HOW IT DIFFERS

I imported nothing from `w2_census_exact.py`. The grammar and the record
builders come from the **original committed sources**, so that a drift
between the unit's transcription and the definitional layer would show up
as a numeric divergence:

| object | my source | unit's source |
|---|---|---|
| transport grammar | `v10/code/d42b1_transport_exact.py`, text-sliced at its own banner print | re-typed into `w2_census_exact.py` §2 |
| family enumeration | d42b1's own `enumerate_family` | the unit's `build_family` |
| crystal builders | `d66_arbitration_crystal_exact.py` `double_grid` / `conflict_grid`, `d60_crystal_exact.py` `B`/`dl`, by AST extraction | re-typed |
| the walk | `d58_atlas_instrument_exact.py` `walk2` | re-typed |

Different primitives and construction orders throughout:

- **MENU key**: canonical sorted tuple / recursive sorted string encoding
  (unit: `frozenset` + `sk`).
- **CONG**: splitter-queue refinement with string signatures, then
  **verified directly** to be a congruence (same class ⇒ same labelled
  successor classes *and* weights) and to refine MENU — a check the unit
  does not make.
- **Squares**: from **family membership** plus cached weights, calling no
  admissibility predicate and re-deriving no menu (unit: re-calls
  `admissible()` four times per pair).
- **Cyclicity**: **Tarjan SCC**, which decides cyclicity at **every**
  length at once (unit: Kahn sort, plus a comparator bounded at length 6).
- **Isomorphisms**: **brute force over all 9! = 362 880 bijections**, no
  backtracking, no pruning (unit: backtracking).
- **Holonomy rank**: fraction-free Gaussian elimination on the exponent
  matrix (unit: integer row reduction with a min-pivot rule).

**Fidelity of the unit's transcriptions.** A normalised diff of the
unit's §2 grammar block against d42b1 lines 50–382 shows **only cosmetic
differences** (PEP-8 re-wrapping, `F`→`Fr`); the crystal and walk builders
are faithful to d66/d60/d58. No transcription drift.

**One correction inside my own work, disclosed.** My first pass keyed
events by `repr()`, which D74 documents as PYTHONHASHSEED-dependent for
frozensets. It reproduced d≤4 exactly (113/185) but gave **268/470** at
d≤5. Re-run with a canonical order-independent key it gives **265/462** —
D74's committed row exactly. The 268/470 was a false number of *mine*; it
never reached a finding. Every d≤5 figure below is from the canonical-key
run.

**Discipline.** Read-only git (`log`/`show`/`rev-parse`). The unit was
never run in-repo: it ran in an off-tree scratch mirror (top-level dirs
symlinked, `.git` a gitfile so `git show` resolves), and the mirror's plain
run is **BYTE-IDENTICAL** to both committed artifacts
(`5e35e7a0115f`, `bacdb7a5e985`). Repo hashes unchanged after all work.

---

## B. WHAT THE REBUILD ADDS (new, in the unit's favour)

**B1 — THE SCISSORS SURVIVES AT d ≤ 5, MEASURED.** §9.3(i) registers
"does the class-extension graph acquire directed cycles on distinct
vertices at depth ≥ 5?" as an experiment that *would move the verdict*.
I ran it. It does not move:

| | classes | edges | self-loops | non-trivial SCCs | acyclic at **every** length |
|---|---|---|---|---|---|
| MENU @ d≤5 | **265** | 575 | 113 | **0** | **yes** |
| CONG @ d≤5 | **462** | 991 | **0** | **0** | **yes** |

and the ACTOR-PAIR generator still has exactly **2** objects (18 000
division-event instances at d≤5, 4 560 of them touching both actors). The
265/462 reproduce D74's committed `(A,B) d≤5` row from this unit's own
definitions, which is itself a first: the paper cites that row (§8.3) but
does not re-derive it.

**B2 — ACYCLICITY HOLDS AT EVERY LENGTH, NOT ONLY 2–6.** Tarjan SCC on
both graphs at both depths returns **0 non-trivial strongly connected
components**. The unit's proof (the completed Kahn sort) is already
unbounded and sound; the length-6 comparator is only a comparator. The
bound therefore does **not** limit the claim, and Z₃ in particular is
covered — but the paper's §5.1 table row ("0 simple cycles at lengths
2–6") is the weaker of the two statements it owns and reads as the
operative one. Prefer the SCC/topological-sort form in the table.

**B3 — THE MECHANISM BEHIND THE SELF-LOOPS, AND A THEOREM THE UNIT CAN
HAVE.** Measured: **every extension edge raises history length by exactly
1** (0 exceptions, d≤4). Hence:

> If every class of a quotient is length-homogeneous, the class-extension
> graph is graded by length and is acyclic at every length — **by
> identity of the definition, with no computation.**

Measured: **CONG-185 is length-homogeneous** (0 classes span more than one
history length) at d≤4 **and** at d≤5. So the CONG blade is a *theorem*
at both depths, not merely a measurement. And MENU's self-loop classes are
**exactly** its multi-length classes — 45 of 45 at d≤4, the two sets
**identical**; 113 of 113 at d≤5. That is why the self-loops exist, and it
is the sentence §5.1 is missing.

**B4 — THE CHARITABLE-RECONSTRUCTION ATTACK FAILS.** K2 asks for a
generator combination or quotient object outside the checked set that is
both ≥9-object and cyclic. I rebuilt every cell the unit kills on TYPE
grounds under the **most generous relation anyone could defend**, and
materialised the two rows the unit discharges by a grading *argument*
(Deviation 2):

| charitable reconstruction | objects (d≤4 / d≤5) | cyclic on distinct vertices? |
|---|---|---|
| ACTOR × COVER-PAIR — family-wide union of the records' poset covers, pushed to initiators | 2 / 2 | yes |
| ACTOR × EXTENSION-EDGE — history ↦ initiator of its last event | 2 / 2 | yes |
| EVENT-SUBSET × ACTOR-PAIR — actor ↦ its own division-event set | 2 / 2 | yes |
| EVENT-SUBSET × EXTENSION-EDGE — **realised**, not waived | **25 / 65** | **no** |
| ULAM-PREFIX × EXTENSION-EDGE — **realised**, not waived | **3969 / 30729** | **no** |
| ACTOR × ACTOR-PAIR (the short blade) | 2 / 2 | yes |

Every reconstruction is either 2-object-and-cyclic or many-object-and-
acyclic. **The scissors is robust to the unit's own typing choices**, and
the two waived rows can be replaced by measurements at no cost to the
fates. Note the realised subset count (25) against the declared arity
(2²⁰): even reading the site set as the *realised* objects, the fates are
unchanged (25 ≠ 9 ⇒ ARITY-DEAD; with the restriction, acyclic ⇒
STRUCT-DEAD, now measured rather than argued).

**B5 — THE CONTROLS BRUTE-FORCED.** Over **all 362 880** bijections:
exactly **72** carry the crystal's co-division incidence onto the
2-link lattice, and exactly **0** carry it onto I7's 3-link lattice. Both
delivered numbers are confirmed by the strongest available method. (For
the record, 72 = |Aut(K₃□K₃)| = 3!·3!·2 — the crystal's co-division graph
*is* the 3×3 rook's graph, which *is* the Cayley graph of (Z₃)² on
{e₁,e₂}; the 3-link target is 6-regular against the source's 4-regular, so
0 is forced.)

**B6 — THE EMPTY DIAGONAL, INDEPENDENTLY.** I rebuilt **four of the five**
crystals from d66's originals. Every event/division count and every count
field reproduces, including `n_{e₁+e₂} ≡ 0 at 9/9 sites`:
DOUBLE-GRID(3,2) 72/18 → 2,2,**0**; DOUBLE-GRID(3,3) 96/24 → 3,3,**0**;
CONFLICT-GRID(3,2) 30/6 → 1,1,**0**; CONFLICT-GRID(3,4) 66/12 → 2,2,**0**.
The measurement stands. Its licensed reading is exactly the paper's:
q₁₂ is unfixable *from the committed crystal family*, because a
row/column arbitration's register footprint never meets a diagonal pair.

---

## C. FINDINGS

### MAJOR-1 — the `×2 carriers` axis is inert; the 60 is 30 counted twice

**Measured.** All 30 rows stamped `@MENU` are **identical** to the 30
stamped `@CONG` after dropping the `arena` and `carrier` label fields —
identical in every field, including `site_arity`, `link_acyclic`,
`acyclicity_basis`, `fate` and `reason` (verified over the receipt's
`census_rows`: 30 of 30 identical, **zero fields ever differ**).

**Cause, in the code.** The census loop builds
`car = {... "cache": cache, "menu": menu, "cong": cong, ...}` and varies
only `name` and `carrier` (lines 2342–2356). `arena_linkrel` then selects
the class map by the **site generator** — `Q = arena["menu"] if sgen ==
"MENU-CLASS" else arena["cong"]` (line 1568) — never by `arena["carrier"]`.
The carrier stamp enters no computation anywhere in `detect`.

**What is actually true.** Both carriers' class graphs *are* built and
both *are* acyclic — but via the SITE axis (`MENU-CLASS` and `CONG-CLASS`),
inside each carrier block. The substance of `@BOTH` survives; the stated
reason does not.

**Consequences.**
1. §5's sentence — *"The verdict is carrier-stamped `@BOTH` for that
   reason, and not because the carriers were assumed interchangeable: the
   link relations were built separately on each carrier's own class
   graph"* — **mis-describes the instrument.** The link relations are not
   built separately per carrier; the two blocks are the same computation.
2. *"The two carriers return identical fate distributions"* is true **by
   construction**. It cannot fail, so it is not a measurement — and the
   unit itself carries HA §14 requirement 3 verbatim (V05) against exactly
   this.
3. `CANDIDATES=60` over-counts: the pin's vocabulary yields **30 distinct
   candidates**, each emitted twice.
4. §9's carrier-relativity bullet — *"The two carriers returned identical
   fates here, so this unit adds no evidence either way… That silence is a
   result"* — is right in its conclusion but wrong in its grounds. The
   silence is not a measured null; the instrument is **constitutionally
   incapable** of returning different fates at the two carriers.

**Exact repair (no re-run needed for 1/3/4; 2 needs one line of code).**
- §5, replace the quoted sentence with: *"The candidate family is
  enumerated once and stamped at both carriers. Both carriers' class
  graphs are exercised — as the `MENU-CLASS` and `CONG-CLASS` site
  generators, inside each block — and both are acyclic; the two stamped
  copies are the same 30 computations, so the identical fate
  distributions are a fact about the enumeration, not a comparison."*
- §7 verdict string: `CANDIDATES=60` → `CANDIDATES=30-DISTINCT-x2-CARRIER-
  STAMPS(60-ROWS)`, or keep 60 and add `|DISTINCT=30`.
- §9, carrier-relativity bullet: replace *"adds no evidence either way"*
  with *"cannot bear on the carrier-relativity open: the census's carrier
  stamp enters no computation, so the identical fates are forced. A
  carrier-discriminating census would have to vary the object the link
  relation is built on, not its label."*
- Optionally, make the duplication honest in code: emit 30 rows and stamp
  the verdict `@BOTH` from the two site generators.

### MAJOR-2 — one prose cell in §2.2 is not rendered from the receipt (#20)

The ruling-properties table's **P4 row, MENU-113 column**, asserts
`{2,3}, rank 2`. **The program never computes the MENU q-reading.** Line
1916 computes `reading(cache, cong, …, "q")`; line 1927 computes
`reading(cache, menu, …, "k")` — there is no `reading(cache, menu, …,
"q")` anywhere, `menu_properties` carries only
`descent_nonconstant_horizons`, `multivalued_weights_targets`,
`k_primes`, `k_rank`, `ck`, and no gate or anchor mentions it. Every
other MENU cell in that table (P1 `4`, P2 `0/4`, P3 `44; 1402 of 1546`,
P5 `{2,3,5,13} rank 3`, P6 `6 of 10`) *is* backed. This one is not.

**The value is correct** — my independent rebuild gives MENU q-holonomy
primes `{2,3}`, rank `2`. So this is an **unbacked** number, not a false
one. It is nonetheless the single prose cell in the paper with no
computation behind it, in an era whose stated failure mode is that false
paper claims are all prose.

**Exact repair.** Two lines: `sl_qm, rk_qm, ob_qm, val_qm =
reading(cache, menu, closed, G, "q")`; `ps_qm, rk_group_qm =
group_rank(val_qm)`; add `"q_primes": ps_qm, "q_rank": rk_group_qm` to
`PAYLOAD["menu_properties"]` and render the cell from it. (Expected:
`[2, 3]`, `2`.) If a re-run is not wanted, mark the cell
`— (not computed)`.

### MINOR-1 — the fourth axis is not in the pin's vocabulary

Pin R3 declares **three** generator axes: site (5), link (3), count (1) —
15 combinations, 30 with the carrier stamp. The census multiplies by a
fourth, `arity treatment ∈ {NONE, DECLARED-RESTRICTION}`, and
`G-CENSUS-COMPLETE` attributes all four to *"the pin's declared generator
vocabulary"*. The widening is *licensed* by pin R3's sentence that arity
obstructions are measured outcomes rather than skipped cells, and it can
only add candidates, never hide a FOUND — but the attribution is
inaccurate. **Repair:** *"the pin's three generator axes, plus the arity
treatment the census offers each cell"*, in §3 and in the gate statement.

### MINOR-2 — the kill criterion and the admit criterion are not the same predicate

Census candidates die at `STRUCT-DEAD` by **directed** acyclicity
(`has_distinct_vertex_cycle`, which drops self-loops and asks for a
directed cycle on distinct vertices). The FOUND control is admitted by
**undirected** incidence isomorphism (`graph_isomorphisms` symmetrises
*both* source and target, lines 1370–1384). The kill criterion is the
strictly stronger of the two: a directed-acyclic relation can have an
undirected version full of cycles. The kill is sound under the directed
reading the count field itself uses (`out[(x,ℓ)] = rel[(u,v)]` with
`v = site(x+ℓ)`), so no verdict moves — 0 candidates reach the
isomorphism test. But K3's rule ("are FOUND and EMPTY both genuinely
reachable BY THE SAME instrument?") is satisfied only modulo this
asymmetry: **the positive control passes a weaker gate than the one that
kills the census.**

Two further same-standard gaps, both in the control's favour and both
disclosed-adjacent rather than disclosed:
- the crystal FOUND runs at a **2-link** target, so `I-DIRECTION-LABEL`
  ranges over `2! = 2` label permutations; a census candidate at I7 would
  face `3! = 6`. The control's choice group is 72×2×2 = 288 against a
  census candidate's isos×6×2.
- `I-SITE-ASSIGNMENT = 1` at the crystal is a statement that the *induced
  field* is invariant under the 72 assignments, not that the assignment is
  unique. The paper says so two sentences later ("the whole isomorphism
  orbit collapses to one field"), but §4.1's *"nothing is chosen"* is
  loose — 72 things are chosen; nothing the reading sees is.

**Repair.** In §4/§5.1: name the structure gate as the **directed**
criterion and the isomorphism test as the **undirected** one, state that
the former implies the latter's failure but not conversely, and note the
2-vs-3 link asymmetry in the control's choice group. Change §4.1's
"nothing is chosen" to *"nothing the reading sees is chosen"*.

### MINOR-3 — `I-ORIENT` never returns its other value anywhere in the run

The inventory has three items. `I-SITE-ASSIGNMENT` is exhibited at 1 and
at 6; `I-DIRECTION-LABEL` at 1 and at 2; **`I-ORIENT` is 1 in every row
that reaches the inventory** (`free_item_fibers`: both entries `1`), and
no census candidate reaches it. By the unit's own carried standard —
V05, *"A predicate that cannot return its other value anywhere in the
declared arena is not a measurement"* — the third inventory item is
undischarged. Mechanically it is close to forced: the co-division
relation is symmetric by construction, so orientation can only re-index
cells, and on a homogeneous field it cannot re-index anything at all.
**Repair:** either exhibit an arena where `I-ORIENT > 1`, or reclassify it
as *declared, with its vacuity at ACTOR-PAIR disclosed* alongside the
window and the division predicate in §6.

### MINOR-4 — "336 in each direction" double-reports one population

Abstract: *"The (A,B) channel carries 336 division events in each
direction"*; §5.1: *"A→B (336 division events) and B→A (336)"*. The
relation is `rel[(u,v)] = #{e : u ∈ regs(e) and v ∈ regs(e)}` — symmetric
in `u,v` by construction. Those are the **same 336 events entered twice**,
not 672. My rebuild: 1536 arbitration instances in the family, **336** of
which touch both actors. A reader may take the total as 672.

The same symmetry makes the short blade generic rather than surprising:
for *any* symmetric incidence relation with at least one realised edge,
every realised edge is a 2-cycle, so "the actor pair carries directed
cycles" is automatic. That does not weaken the scissors — it makes the
long blade (acyclicity at 113/185/265/462 objects) carry all the content.
**Repair:** *"336 co-division events on the (A,B) channel; the relation is
symmetric, so every realised edge is a 2-cycle"*, and in §5.1 fold the two
table entries into one.

### MINOR-5 — two waived rows can be measured instead of argued

Deviation 2 discharges EVENT-SUBSET and ULAM-PREFIX by a grading theorem
and marks it in the waiver census. The **realised** relations are small
and were computed here in seconds: EVENT-SUBSET × EXTENSION-EDGE has
**25** realised objects at d≤4 (65 at d≤5) and is acyclic; ULAM-PREFIX ×
EXTENSION-EDGE has **3969** and is acyclic. **Repair (optional, strictly
strengthening):** materialise both, report the realised counts next to the
declared arities (2²⁰ / 3969), and retire one waiver.

### MINOR-6 — the pin and the artifact disagree on one git-show route

Pin R1 records `paper-12-gamma-main.md` as *"read at commit 822bb15 via
git show"*; the delivered run reads it via `git show 95c3b77:`
(`PIN_COMMITS = ["95c3b77", "822bb15"]`, first match wins). I verified
both commits carry the pinned digest `d85a629a9378` byte-for-byte, so
nothing substantive follows. **Repair:** one clause in §8.5 noting that
both declared commits carry the pinned bytes and the run took the first.

**Not a finding, checked:** the scout note's amendment (#89) is a **pure
19-line append**; the pinned pre-amendment bytes `e1f771a9d0ed` are a
prefix of the current file, V09's quote `NO-SEED-AT-THE-CARRIER` survives
verbatim, and the addendum states *"No reversal — every verdict stands"*.
Reading the pinned bytes is harmless and §8.5 discloses it.

---

## D. PROSE AUDITED AGAINST THE RECEIPT

Every numeric token in the paper, checked against `w2_census_receipt.json`
and against my rebuild. **One cell unbacked (MAJOR-2). No false number.**

| paper claim | receipt | my rebuild |
|---|---|---|
| 32 gates / 0 failures; 7 numeric + 11 verbatim anchors / 0 failures; 3 waivers; 13 mutants | 32/0, 7, 11, 3, 13 | — |
| 3969 histories; MENU 113; unweighted 113 | ✓ ✓ ✓ | 3969, 113, 113 |
| CONG 185 in 5 rounds | ✓ | 185, 5 rounds; **verified to be a congruence and to refine MENU** |
| 1546 closed / 88 defective, spectrum {1/2:70, 2:10, 3/2:6, 2/3:2} | ✓ | ✓ (sums to 88) |
| P1 MENU: `G(·,2)` non-constant on **4** classes; CONG 0 | ✓ | ✓ |
| P2 CONG 0/0; MENU 0/4 | ✓ | ✓ |
| P3 CONG closes 44 of 88 and 1362 of 1546; 44 self-loops {1/2:26, 2:10, 3/2:6, 2/3:2}; obstruction 44; MENU 44, 1402 of 1546 | ✓ | ✓ (self-loops sum to 44) |
| P4 CONG {2,3} rank 2 | ✓ | ✓ |
| **P4 MENU {2,3} rank 2** | **absent** | **{2,3}, rank 2 — value right, provenance missing (MAJOR-2)** |
| P5 CONG {2,3} rank 2; MENU {2,3,5,13} rank 3 | ✓ | ✓ |
| P6 CONG 10 of 10; MENU 6 of 10 | ✓ | ✓ |
| 1536 selected events all tagged; 20 distinct arbitrations; 8 pair | ✓ | 1536, 20, 8 |
| 36 refinements; additivity 972 of 972, 0 violations | ✓ | 36, 972, 0 |
| I7: 9 sites, 3 links, 27 cells, 11 records, 9 admissible, 6 splittable; unsplittable {G-ANISO, G-CURVED, G-FLAT} | ✓ | ✓ |
| site arities 2 / 113 / 185 / 1 048 576 / 3969; by depth 1, 8, 60, 452, 3448; "no depth gives 9" | ✓ | ✓ (sums to 3969) |
| crystal table: 72/18, 96/24, 30/6, 66/12, 46/1; axis counts 2,3,1,2,0; diagonal **0 at 9/9** in 5/5 | ✓ | 4 of 5 rebuilt, all exact; D60-GRID(3,12) not rebuilt |
| FOUND: 72 isomorphisms, fibers 1/1/1, zero free items | ✓ | **72 of 362 880 brute-forced**; 1/1/1 |
| falsifier: UNMOTIVATED, I-SITE-ASSIGNMENT 6, I-DIRECTION-LABEL 2 | ✓ | 72 isos, 6, 2, I-ORIENT 1 |
| crystal at I7: **0 of the 9!** | ✓ | **0 of 362 880 brute-forced** |
| walk: 30 events, 4 divisions, 0 on the (A,B) channel | ✓ | ✓ |
| MENU 45 self-loops, CONG 0; 0 simple cycles len 2–6 at both | ✓ | 45 / 0; **0 non-trivial SCCs — acyclic at every length** |
| 336 division events on the (A,B) channel | ✓ | 336 — but symmetric, see MINOR-4 |
| fates 36 / 12 / 2 / 10; per carrier 18 / 6 / 1 / 5 | ✓ | re-derived by hand from the typing rules, then measured |
| §8.3 d≤5: **265 MENU / 462 CONG** (cited from D74, not run) | not computed | **265 / 462 — confirmed, and the scissors survives there (B1)** |

**K1's fate arithmetic, re-derived independently of the code.** From the
forced-map table alone: 9 (site, link) cells have no pinned map or no
family-level referent × 2 repairs = **18 TYPE-DEAD**; 6 well-typed cells
at `repair = NONE` with arity ≠ 9 = **6 ARITY-DEAD**; the one cell with
arity **below** 9 offered a restriction = **1 ARITY-DEAD-BELOW**; the 5
well-typed over-large cells offered a restriction, all acyclic = **5
STRUCT-DEAD**. 18+6+1+5 = 30 per carrier, ×2 = **36/12/2/10**. Matches.
No combination is silently skipped: the loop is a full product and every
row carries a fate.

**ARITY-DEAD-BELOW's separation is principled.** `ARITY-DEAD` = "arity ≠
|X| and no repair was declared"; `ARITY-DEAD-BELOW` = "arity < |X| *and* a
restriction was declared, which can only shrink a site set, so no repair
exists even in principle". The two fates are distinguished by whether the
offered repair is *conceivable*, not by how it happened to fail. It fires
on exactly the one site generator with arity below 9 (ACTOR, and the D58
walk in the controls). Correct and non-redundant.

---

## E. THE HEADLINE, AUDITED (the candidate-readings rule)

| headline component | verdict of this lens |
|---|---|
| `EMPTY-AT-THE-DECLARED-FAMILY` | **CONFIRMED.** 0 FOUND / 0 UNMOTIVATED / 0 SMUGGLED reproduces; every fate re-derived twice, once by hand from the typing rules and once by measurement. |
| `THE-ARITY-CYCLICITY-SCISSORS` | **CONFIRMED AND EXTENDED.** Both blades hold at d≤4 and now at **d≤5**; acyclicity holds at **every** length, not 2–6; the mechanism survives every charitable reconstruction of the type-killed cells; and the long blade acquires a theorem (length-grading, B3). |
| `@BOTH:MENU-113+CONG-185` | **EARNED IN SUBSTANCE, NOT BY THE STATED ROUTE.** Both class graphs are built and both are acyclic — but by the site axis, not the carrier axis, which is inert (MAJOR-1). |
| `CANDIDATES=60` | **OVER-COUNTED.** 30 distinct candidates, emitted twice. |
| `CONTROLS=…FOUND-AT-CRYSTAL / FALSIFIER-FLIPS / EMPTY-AT-WALK / CRYSTAL-AT-I7` | **CONFIRMED**, all four, with the isomorphism counts brute-forced; the FOUND branch passes a weaker gate than the kill criterion (MINOR-2). |
| `INGREDIENT=…ADDITIVITY-972-OF-972 / DIVISION=ARBITRATION-TAG-FORCED` | **CONFIRMED** (36 builds, 972 checks, 0 violations; 1536/1536 tagged, 20 distinct, 8 pair). |
| `CARRIER-RE-DERIVATION=CONG-185-SIX-OF-SIX` | **CONFIRMED**, six of six, with two properties the unit does not check (it *is* a congruence; it *does* refine MENU) added. |
| the empty diagonal | **CONFIRMED** at 4 of 5 crystals rebuilt from d66's originals. Licensed reading is the paper's; the over-reading to guard against is "no grammar record can supply q₁₂" — the measurement is over the *committed* family only, and §9 already says so. |

**Nothing in the delivered verdict is false.** The fixes are one
mis-described instrument axis, one over-counted headline integer, one
unbacked prose cell, and five minors.

---

## F. RECOMPUTATION COUNT

**115**, counted honestly: 42 on the d≤4 carrier (family, both partitions,
squares, six properties, both class graphs, division census, Ulam), 35 on
the controls and crystals (five records, two brute-force isomorphism
censuses over 362 880 bijections each, both inventories, the walk, I7's
arena, additivity), 23 on the d≤5 extension and the charitable
reconstructions, and 15 structural (byte-identity ×2, the 30-vs-30 row
identity, the hand-derived fate arithmetic, gate/anchor/waiver/mutant
counts, the d42b1/d66/d60/d58 transcription diffs, the pinned-source and
scout-amendment checks).

**Divergences from the unit: 0.** One false number was found and killed in
**my own** rebuild before it reached a finding (the `repr`-keyed 268/470 at
d≤5, corrected to 265/462 with a hash-independent key).

---

## G. RECOMMENDATION

**ACCEPT-WITH-FIXES.** MAJOR-1 and MAJOR-2 are mandatory: the first
because the paper describes an instrument it does not have and reports a
candidate count that double-counts, the second because it is the one prose
number with no computation behind it. MINOR-1 through MINOR-6 are cheap
and all improve the paper. B1–B4 should be folded in as strengthenings —
in particular **B1 discharges §9.3(i)'s registered experiment in the
unit's favour**, and B3 turns the long blade's CONG half into a theorem.
