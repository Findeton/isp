# R5M HOSTILE REVIEW — SEAT K1, THE OPERATOR LENS

**Unit under review:** R5M, `v14/paper-23-measure.md` (the configuration
measure), delivered and committed as-is at `33da839` (v14 ledger #181);
battery green at #183.
**Protocol:** v14 ledger #183, row **K1 OPERATOR** — rebuild the 8-candidate
census from nothing, with this seat's own machinery, never the delivered code
as oracle.
**Objects, sha256-12, verified at review start and again at review end
(identical both times):** `v14/paper-23-measure.md` `9249dda1c0a3`;
`v14/code/r5m_measure_exact.py` `f7de59960fe6`;
`v14/code/r5m_measure_output.txt` `8ee12d000bad`;
`v14/code/r5m_measure_receipt.json` `1e794bd7f5fb`;
pin `v14/note-r5m-pin.md` `e5e09f65f83b`.
**Repo writes by this seat:** this file only. No LOG/STATUS/RUNBOOK edit. All
execution in `…/scratchpad/r5m-op/` (own kit + a provisioned off-tree mirror).
Git read-only throughout.

---

## GRADE: **AWF** — ACCEPT WITH FIXES

**Zero false numbers.** Every delivered quantity this seat could reach was
rebuilt from the parent's declared definitions with an independent
$\mathbb{Q}(\zeta_8)$ implementation, an independent chart/gauge action, an
independent Burnside, an independent Born layer and an independent parent
census — **61 delivered quantities recomputed, 61 exact, 0 disagreements**,
including both 89-digit full-space orbit integers character-for-character. The
head is right, the fiber statement is right, and the two objects the head turns
on (120 orbits at chart-128, 208 at chart-32) are right by a group action built
here from scratch.

Two defects are **MAJOR** and both are prose/scope defects that leave the head
and every measured number standing: the unit's advertised reachability of
`MEASURE-DERIVED` is **not wired to any measurement** (§5's "would have emitted
`MEASURE-DERIVED`" is false of this instrument, twice over), and the
correspondence **enumeration is incomplete** — two zero-free-item `FOUND`
controls sit in a receipt this instrument itself reads and are neither counted
nor named. Five MINORs are exactly liftable. All seven repairs are given
verbatim below.

**Recomputations / independent comparisons:** **63** (enumerated in §6).
**Instrument executions:** 6 (1 off-tree `--no-write`, 3 by-hand mutants,
2 in-process gate probes).

---

## 1. WHAT WAS REBUILT FROM NOTHING

No object below was imported from the delivered program or from any repo
module. The field is a fresh integer-tuple implementation of
$\mathbb{Q}(\zeta_8)$ over $(1,z,z^2,z^3)$ mod $z^4+1$ in lowest terms; the
alphabet is rebuilt from "zero together with $\zeta_8^t$ at the three declared
moduli"; the coin family is enumerated **exhaustively over $25^4 = 390625$
matrices** with a unitarity predicate and nothing else.

| object | this seat, from scratch | delivered | verdict |
|---|---|---|---|
| alphabet | 25 (moduli² multiset 8×1, 8×½, 8×¼, 1×0) | 25 | ✅ |
| coin family, exhaustive over $25^4$ | 640 | 640 | ✅ |
| sectors | 64 / 64 / 512 | 64 / 64 / 512 | ✅ |
| $UU^\dagger = I$, second route | 0 failures | 0 | ✅ |
| chart orders | 32 / 128 | 32 / 128 | ✅ |
| link orbits (transitivity) | 1 / 1 | 1 / 1 | ✅ |
| elements reversing ≥1 link | 0 / 96 | 0 / 96 | ✅ |
| elements with an odd-parity cycle | 0 / 12 | 0 / 12 | ✅ |
| coins with $U = XUX$ | 32 (8+8+16) | 32 | ✅ |
| chart-fixed locus | 640 uniform at **655360 of 655360** | 655360/655360 | ✅ |
| extension-fixed locus | 32 (2621440 checks) | 32 | ✅ |
| realisable constant twists | $\{0,2,4,6\}$ | $[0,2,4,6]$ | ✅ |
| residual group on the slice | 4 / 8 | 4 / 8 | ✅ |
| **orbits on the slice** | **208** (64×1, 144×4) | 208, same histogram | ✅ |
| **orbits on the slice** | **120** (8×1, 28×2, 24×4, 60×8) | 120, same histogram | ✅ |
| simplex dimensions | 207 / 119 | 207 / 119 | ✅ |
| Burnside, full space, chart-32 | 1961594…3040000 (89 digits) | identical | ✅ |
| Burnside, full space, chart-128 | 4903985…1520000 (88 digits) | identical | ✅ |
| group order divides the fixed-point total | both | both | ✅ |
| sector multisets on 32 links | 561 = $\binom{34}{2}$ | 561 | ✅ |
| products staying in the family | **278528 of 409600** | 278528/409600 | ✅ |
| by-sector-pair closure (9 cells) | all 9 identical | receipt's table | ✅ |
| monomial coins / closure / inverse | 128 / 0 / 0, identity present | 128 / 0 / 0 | ✅ |
| interfering coins adjoinable | 0 of 512 (BFS escape each) | 0 of 512 | ✅ |
| defect-carrying, $B(U^2)\neq B(U)^2$ | 384, all balanced | 384 | ✅ |
| defect ∩ Haar carrier | 0 | 0 | ✅ |
| $\Delta^B(H,H)$ seed witness | $\pm\tfrac12$ half-and-minus-half | R5's witness | ✅ |
| finite cyclic group inside the family | 384 of 640 | 384 of 640 | ✅ |
| non-flat / non-commuting | 632 (56/64/512) / 576 (0/64/512) | 632 / 576 | ✅ |
| Born images / fibres | 3 / 64, 64, 512; doubly stochastic 640/640 | 3 / same | ✅ |
| pushforward support bound | $640-113 = 527$ | 527 | ✅ |

**The null-dependence table, rebuilt cell by cell** (mass = full orbits in the
set ÷ orbits; every set verified a union of orbits at both readings, **0
partial** at 8 of 8 (reading, set) rows):

| set | n | counting | orbit null, chart-32 | orbit null, chart-128 |
|---|---|---|---|---|
| NON-FLAT | 632 | 79/80 | 25/26 | 23/24 |
| NON-COMMUTING | 576 | **9/10** | **9/13** | **7/10** |
| DEFECT-CARRYING | 384 | 3/5 | 6/13 | 7/15 |
| DIAGONAL | 64 | 1/10 | 4/13 | 3/10 |

All twelve fractions reproduce exactly. Spread on NON-COMMUTING = **27/130**,
exact. Invariance of the nulls: **2624** (orbit, group element) images checked
under the 8-element group across both orbit systems — $(208+120)\times 8$,
matching the delivered denominator exactly — **0 failures**; a further 1312
checks under the 4-element group, 0 failures.

**Off-tree reproduction.** The instrument was run from a provisioned mirror
outside the repo, with no version control present: exit 0, and
`v14/code/r5m_measure_output.txt` reproduced **byte-identical** to the pinned
artifact.

---

## 2. FINDINGS

### MAJOR-1 — `MEASURE-DERIVED` is not reachable by this instrument; §5 says it is

**The delivered sentence (§5):** "Run on a synthetic arena whose declared group
**is** transitive, the same predicate returns 1 orbit and *would have emitted*
`MEASURE-DERIVED`." And §1's table: "`MEASURE-DERIVED` via invariance —
**genuinely reachable**", "`MEASURE-DERIVED` via pushforward — **genuinely
reachable**", under the column heading *on this arena*, introduced by
"Reachability by the law is not reachability on this arena, and **the
difference is measured** rather than left for a reader to notice".

**Measured.** The difference is *not* measured; it is asserted. Every
candidate's price is a **typed constant** in the source — `free_items` at lines
1264, 1499, 1661, 1672, 1808, 1813, 1817, 1851 — and not one of them is a
function of any quantity the run measures. `head_law` takes its `DERIVED`
branch only on `free_items == 0`, and `uniqueness` enters that branch only as a
`UNIQUE`/`NOT-UNIQUE` decoration *after* the branch has been chosen.

Two independent demonstrations, both run in-process against the pinned module:

1. **The head law itself.** Handed this arena's eight candidate rows with
   candidate (c) still priced at 1 free item, but with **both readings
   transitive** (`orbits = 1`, `unique_invariant_measure = True`,
   `simplex_dimension = 0`), `head_law` returns

   ```
   MEASURE-DECLARATION-REQUIRED-<ONE-POINT-OF-A-0-SIMPLEX-ON-1-ORBITS-AT-THE-CHART-128-READING;0-SIMPLEX-ON-1-ORBITS-AT-THE-CHART-32-READING>
   ```

   — i.e. on a transitive arena the law would call a **uniquely determined**
   measure "declaration-required", and would price the declaration at a
   0-simplex, which is a point. It returns `MEASURE-DERIVED-<AN-INVARIANCE-
   CHARACTERISED-MEASURE;UNIQUE>` only when the candidate's price is
   *separately* set to 0 by hand.

2. **The run would not get that far.** `price_the_fibre` gates
   `all(r["orbits"] > 1) and len(rows) == 2` (G-FIBRE-PRICED, gate **46**),
   which closes **before** the head is built (G-HEAD-STRING-EQUALITY, gate 50).
   Called with `orbits = 1` at both readings it **REFUSES**:
   `G-FIBRE-PRICED :: … :: [('CHART-128', 1, 0), ('CHART-32', 1, 0)]`. A
   transitive arena therefore produces exit 1, not `MEASURE-DERIVED`.

What *is* demonstrated is narrower and true: `orbits_of` returns 1 on a
synthetic 4-point cyclic arena (G-UNIQUENESS-GATE-CAN-PASS), and `head_law`
emits all three heads when handed **synthetic census rows**
(G-HEAD-LAW-REACHABILITY). Neither touches the wiring from a *measurement* to a
*price*. The consequence for the unit's own falsifiability claim ("The
falsifiability of this unit therefore lives in the orbit census and in the
correspondence census. Both could have gone the other way.") is that the orbit
census can move the head's **numbers** but can never move its **branch**.

**Verdict impact: none.** This arena is genuinely not transitive — 208 and 120
orbits, rebuilt here independently — so the delivered head is correct.

**Exact repair (prefer both; (b) alone is sufficient to make every delivered
sentence true).**

(a) *Code, 2 lines + 1 gate + 1 mutant.* In `measure_invariance`, replace
```
        "free_items": 1,
```
in the `S["candidate_invariance"]` block by
```
        "free_items": 0 if any(v["unique_invariant_measure"]
                               for v in uniq.values()) else 1,
```
and relax G-FIBRE-PRICED's predicate from `all(r["orbits"] > 1) and
len(rows) == 2` to `len(rows) == 2 and (all(r["orbits"] > 1)
or any(r["orbits"] == 1 for r in rows))`, with the detail string unchanged.
Declare `MUT-INVARIANCE-PRICE-UNWIRED` (target: a new
`G-THE-INVARIANCE-PRICE-IS-MEASURED` gate asserting
`(candidate_invariance["free_items"] == 0) == any(transitive)`), so that the
wiring itself has a falsifier.

(b) *Prose.* §5, replace the last two sentences by: "Run on a synthetic arena
whose declared group **is** transitive, the same orbit predicate returns 1
orbit inside a gate, and the head law, handed a census row priced at zero free
items, returns `MEASURE-DERIVED` inside another. Both halves of the inference
are demonstrated; on this arena the group is measured not to be transitive, so
the negative is a property of the arena and not of the instrument's standard."
§1's table, change the two `MEASURE-DERIVED` cells from "genuinely reachable"
to "**reachable by the law; the candidate prices are declared readings of each
construction and are not computed from the census**", and add one sentence
after the table: "Each candidate's price in free items is a declared reading of
its construction, gated for non-negativity and totality but not derived from a
measurement; what the measurements move is the fibre, not the branch."

---

### MAJOR-2 — the correspondence enumeration omits two zero-free-item `FOUND` controls, and the "one dictionary" gate does not test "one"

**The delivered claims (§4.1).** "**The pinned correspondences are enumerated,
and the enumeration is the finding.**" … "And the corpus's one *found*
dictionary, weld 3's …". Verdict segment:
`WELD3-IS-THE-ONE-FOUND-DICTIONARY`.

**Measured.** The weld-2 receipt that this instrument reads as a pinned source
(`S-W2-RECEIPT`, `payload/controls`) carries **two** rows at fate
`FOUND-candidate` with `free_items: []` — *zero free items at the RSQ
standard*, the census's own definition of FOUND — built from **the same
generators the pushforward would need**:

| control | arena | site ← | link ← | count ← | free items |
|---|---|---|---|---|---|
| `FOUND_at_crystal` | `CRYSTAL/DOUBLE-GRID(3,2)` | ACTOR | ACTOR-PAIR | DIV-COUNT-BETWEEN-DECLARED-ARB-CUTS | **0** |
| `FOUND_at_I7_target_declared_probe` | `DECLARED-PROBE/CAYLEY-AT-I7` | ACTOR | ACTOR-PAIR | DIV-COUNT-BETWEEN-DECLARED-ARB-CUTS | **0** |

Neither is mentioned in paper-23; the receipt contains the string `crystal`
**0 times**. The instrument *does* reach into the same `controls` block for
`PV-W2-ACTORS` (`payload/mechanism/actor_site_objects`, used for the arity
blade), so the omission is not one of access.

The gate that carries the word is **G-WELD3-IS-THE-ONE-FOUND-DICTIONARY**, and
its predicate is `len(carrier_dead) >= 2 and w3["counts"]["weld_found"] > 0`:
it tests the dead list and the existence of found rows, and **never tests
uniqueness at all**. The word "ONE" in the gate name and in the verdict is
carried by nothing.

**Verdict impact: none, and this is measurable rather than hopeful.** Both
controls land on nine-site arenas — `DOUBLE-GRID(3,2)` reports its whole
census at 9/9 sites, and the I7 probe is at I7's own nine-site record lattice —
so both die at exactly the site-count blade already used against weld 3 (9
against this arena's 16). The
`NO-PINNED-CORRESPONDENCE-TO-THIS-ARENA` segment survives the enumeration being
completed. What does not survive is the sentence "the enumeration is the
finding": an enumeration that omits the two rows nearest the claim is not one.

**Exact repair.** (i) Add one path-value anchor
`("PV-W2-FOUND-CONTROLS", "S-W2-RECEIPT", "payload/controls", …)` and a gate
`G-EVERY-FOUND-ROW-IN-THE-CORPUS-IS-ENUMERATED` whose predicate walks **every**
row of both weld receipts whose fate begins `FOUND` — weld 3's 6 found rows and
weld 2's 2 controls — and requires each one's target site count to differ from
`len(lat.sites)`; publish the enumeration as a receipt table. (ii) Rename
`G-WELD3-IS-THE-ONE-FOUND-DICTIONARY` to
`G-WELD3-IS-THE-ONE-FOUND-DICTIONARY-AT-A-COMMITTED-RECORD-ARENA`, and in the
verdict segment write
`WELD3-IS-THE-ONE-FOUND-DICTIONARY-AT-A-COMMITTED-RECORD-ARENA;WELD2s-TWO-FOUND-CONTROLS-ARE-DECLARED-PROBES-AND-BOTH-CARRY-9-SITES`.
(iii) §4.1, after "the corpus's one *found* dictionary", add: "— one, at a
committed record arena: weld 2's own two `FOUND` rows are positive controls on
a declared probe and a crystal, both at nine sites, and both die at the same
site-count blade."

---

### MINOR-1 — `WIDEST-DISAGREEMENT=27/130-ON-DIAGONAL` is an undisclosed alphabetical tie-break

Recomputed here: the spread 27/130 is attained **twice** — DIAGONAL
($4/13 - 1/10 = 27/130$) and NON-COMMUTING ($9/10 - 9/13 = 27/130$). The
builder's `max(spreads, key=…)` returns the **first** maximal row in
`sorted(sets.items())` order, i.e. `DIAGONAL`. §7's prose attributes the same
27/130 to NON-COMMUTING ("R5's headline … a spread of 27/130"), so the verdict
and the prose name different sets for one number and a reader has no way to see
that they agree.

**Repair.** Report the tie: verdict segment
`WIDEST-DISAGREEMENT=27/130-ATTAINED-ON-DIAGONAL-AND-ON-NON-COMMUTING`, and in
`measure_comparison["widest"]` publish `{"spread": …, "sets": [all argmax]}`
rather than a single name. One line in the gate detail:
`"widest disagreement %s, attained on %d of %d sets"`.

### MINOR-2 — `PV-W3-DIVISIONS` is bound to a field that is not the site count

The anchor reads `arena/divisions` (= 9). In weld 3 that field is the number of
**division events** per record — its own paper: "48 events with 9 division
events". Its consumer, `G-WELD3-TARGET-IS-NOT-THIS-ARENA`, binds it as `sites3`
and prints "the dictionary's target carries **%d sites**". The same receipt
carries the actual site count at `arena/posdef_sites` (= 9). The number is
right; the (path, consumer) pair is not, which is precisely what the unit's own
#87 discipline forbids.

**Repair.** Repoint to `("PV-W3-SITES", "S-W3-RECEIPT", "arena/posdef_sites",
9, "G-WELD3-TARGET-IS-NOT-THIS-ARENA", …)`. No number moves.

### MINOR-3 — "the ones that leave are exactly the interfering ones" over-reads its own table

§4.4 and the `G-FAMILY-IS-NOT-A-GROUP` claim text. Measured here (and published
in the unit's own `closure_by_sector_pair`): every leaving product has both
factors interfering, but only **131072 of the 262144** ordered
interfering×interfering pairs leave — exactly half. The natural reading of the
sentence is false; the intended one is a one-way containment.

**Repair.** §4.4: "…278528 of 409600 products stay inside the family, and every
product that leaves has **both** factors interfering — 131072 of the 262144
interfering pairs, and no other pair at all." Same substitution in the gate
claim.

### MINOR-4 — the load-bearing no-reversal fact is measured, published, and ungated

§3: "at the anchored reading no chart element reverses a link" is what makes
the chart-fixed locus the **640** uniform configurations rather than the 32
swap-fixed ones (the extension reading is the counter-example in the same
section). `rev32` is computed at line 1012 and published as
`elements_reversing_at_least_one_link_chart: 0`, but a grep shows it appears
**only** at its definition and in the receipt — no gate predicate consumes it,
and no mutant plants a reversal. The 655360 checks verify only the
"every uniform configuration is fixed" direction (this seat's rebuild confirms
that is what the loop does); the "exactly" direction rests on transitivity —
gated — **and** on no-reversal — not gated.

**Repair.** Extend G-CHART-FIXED-LOCUS-IS-THE-SWEPT-SLICE's predicate to
`failures == 0 and checked == … and rev32 == 0`, extend its detail to
`"%d fixed-locus checks, %d failures, %d anchored-chart elements reversing a
link"`, and declare `MUT-ANCHORED-REVERSAL` (flip one `rev` flag in `p32`)
against it.

### MINOR-5 — "$B$ is a distribution over the carrier's 16 states"

§4.7. The object `measure_born_layer` actually measures is the **coin's 2×2
Born matrix** (`b = tuple(to_fraction(fnormsq(x)) for x in m)`) — a doubly
stochastic *kernel* on the two states of a link's own domino. `carrier_states:
16` is published beside it but is not the space $B$ lives on, and $B$ is not a
distribution. The verdict segment says only `LANDS-ON-THE-STATES`, so nothing
else in the unit depends on the wording; the fibre statement (3 images, 64/64/
512) is exactly right and reproduces here.

**Repair.** §4.7: "$B(U) = \lvert U\rvert^{\circ 2}$ is a doubly stochastic
**kernel on the two states of a link's own domino** — a probability over the
carrier's states, not over the configurations; and its fibre over the
configuration space is enormous …".

---

## 3. WHAT THIS SEAT TRIED TO BREAK AND COULD NOT

- **The two orbit counts.** Built the residual group twice — once as the
  even-twist subgroup obtained by *propagating a site phase around the torus*
  (closure exactly at $4c \equiv 0 \bmod 8$, giving $\{0,2,4,6\}$), once as an
  explicit permutation group of the 640 coins (orders 4 and 8). 208 and 120,
  with the delivered size histograms to the last orbit.
- **The fixed locus.** 655360 = $640 \times 32 \times 32$ reproduces exactly,
  including the arithmetic of the denominator; the extension value 32 is
  independently the set $\{U : U = XUX\}$, split 8+8+16 across the sectors.
- **The Burnside integers.** Rebuilt the cycle-with-parity factorisation
  independently ($640$ per even-parity cycle, $32$ per odd) and got both
  89-/88-digit integers character-for-character, with the group order dividing
  the fixed-point total in both cases. The ratio is *not* exactly 4
  ($\lfloor N_{32}/N_{128}\rfloor = 3$), which is what containment
  $G_{32} \subset G_{128}$ requires and a typed pair would probably have gotten
  wrong.
- **The Haar closure.** 278528 by two arithmetic representations (a
  gcd-normalised 5-tuple field and a fixed-denominator-4 integer field with a
  divisibility assertion on every product), cross-checked on 3000 random pairs
  with 0 disagreements.
- **The parent census.** Rebuilt 16-dimensional sparse link operators and
  plaquette holonomies from R5's definition
  $W_p = L_4^{-1}L_3^{-1}L_2L_1$, checked $W_p$ unitary at all 640, and
  recovered 632 / 576 with R5's own by-sector split (56/64/512 and 0/64/512),
  and 384 defect coins from
  $\Delta^B(U,U) = B(U^2) - B(U)B(U)$ — the last of which required carrying
  $|e|^2$ in $\mathbb{Q}(\zeta_8)$ rather than $\mathbb{Q}$, since $U^2$ leaves
  the family and its moduli are irrational.
- **The three by-hand mutants** (driven by setting the module switch and
  calling `run()` directly — `run_mutant` was **not** used, so the harness's own
  attribution is not being trusted): `MUT-BORN-STOCHASTIC` → raised at
  `G-BORN-LAYER-IS-A-MEASURE`; `MUT-UNIQUENESS` → `G-UNIQUENESS-GATED`;
  `MUT-RESIDUAL-GROUP` → `G-ORBIT-CENSUS-EXACT`. **3 of 3 on their declared
  target**, each raising after a different number of gates (36, 33, 16), so
  none is dying early by accident.
- **The eight verbatim windows** quoted in the paper were located in their
  pinned sources under whitespace/markdown normalisation: 8 of 8 present, once
  each.
- **The gate arithmetic.** A clean in-process run closes **56** gates in
  `run()` plus `G-SEAL-COMPLETE` in `finish()`; the receipt discloses
  `gates_in_the_sealed_snapshot: 56`, `late_gates: 2`
  (`G-SEAL-COMPLETE`, `G-ARTIFACT-INTEGRITY`) with the warrant, and §10 states
  the snapshot convention. The paper's "56 gates" is the snapshot count and is
  consistent with everything published. **Not a finding.**
- **The withheld segment,** from the operator side only: 38 top-level receipt
  keys, 0 matching the banned expectation vocabulary; no expectation of any
  kind appears anywhere in this seat's own reading of the census. (The
  mechanism's *sufficiency* — top-level keys only, `FunctionDef` names only —
  is K3's row and is flagged there rather than charged here.)

---

## 4. THE HEAD, ADJUDICATED

`MEASURE-DECLARATION-REQUIRED-<ONE-POINT-OF-A-119-SIMPLEX-ON-120-ORBITS-AT-THE-CHART-128-READING;207-SIMPLEX-ON-208-ORBITS-AT-THE-CHART-32-READING>`
**stands, at full strength.** Its two orbit counts, both simplex dimensions,
its census denominator (8 candidates), its numerator (0 derive) and every one
of the eight segment values reproduce from an independent rebuild. The three
sub-claims this seat was sent to break all survive:

1. **"The measured symmetry fixes a support and not a measure."** Confirmed
   twice: invariant ⟺ orbit-constant, unique ⟺ transitive, and the group is
   measured not transitive at either reading; while the fixed **locus** is
   exactly R5's swept slice. The distinction §2 insists on is real and is
   correctly drawn.
2. **"Granted everything, the residual is a point mass."** Confirmed from the
   weld-3 receipt directly: 27 of 27 realised cells at count 1 (the cells are
   (site, direction) pairs, $9 \times 3$), so a constant link datum induces a
   single uniform configuration; and $640 - 113 = 527$ is the right support
   bound for a class-grain pushforward off a 113-class finest cut.
3. **"Where the measure is free the quantum layer is absent."** Confirmed: the
   128 monomial coins are a group (0 closure failures, 0 inverse failures,
   identity present), no interfering coin can be adjoined (0 of 512, by BFS
   escape in every case), and the carrier contains 0 of the 384 defect-carrying
   coins. This is, as the unit says, its most transferable finding, and it is
   clean.

---

## 5. THE REPAIR LIST — LIFTABLE, PRIORITISED

| # | severity | repair | cost |
|---|---|---|---|
| 1 | MAJOR-1 | §5 + §1-table restatement (b), and ideally the 2-line price wiring + relaxed G-FIBRE-PRICED + `MUT-INVARIANCE-PRICE-UNWIRED` (a) | prose 1 para; code ~8 lines |
| 2 | MAJOR-2 | enumerate weld 2's two `FOUND` controls, add `G-EVERY-FOUND-ROW-IN-THE-CORPUS-IS-ENUMERATED` with the site-count kill, rescope the gate name and the verdict segment | 1 anchor, 1 gate, 1 sentence |
| 3 | MINOR-1 | publish the argmax **set**; verdict `…-ATTAINED-ON-DIAGONAL-AND-ON-NON-COMMUTING` | 3 lines |
| 4 | MINOR-2 | repoint `PV-W3-DIVISIONS` → `arena/posdef_sites`, rename `PV-W3-SITES` | 1 line, no number moves |
| 5 | MINOR-3 | one-way wording in §4.4 and in `G-FAMILY-IS-NOT-A-GROUP` | 2 sentences |
| 6 | MINOR-4 | gate `rev32 == 0` inside the fixed-locus gate; `MUT-ANCHORED-REVERSAL` | 4 lines |
| 7 | MINOR-5 | §4.7 "doubly stochastic kernel on the two states of a link's own domino" | 1 sentence |

None of the seven moves a published number. Nos. 1 and 2 move sentences the
unit's own standards make load-bearing.

---

## 6. RECOMPUTATION LEDGER — **63**, COUNTED HONESTLY

Alphabet size (1); modulus² multiset (2); exhaustive $25^4$ coin enumeration
(3); sector split (4); $UU^\dagger$ second route (5); 2×2 Born images (6); Born
fibres (7); double stochasticity at 640 (8); chart order 32 (9); extension
order 128 (10); link orbits chart (11); link orbits extension (12); reversals
chart (13); reversals extension (14); total link reversals 2048 (15);
odd-parity elements chart (16); odd-parity extension (17); swap-fixed coins
with sector split (18); fixed-locus checks 655360 (19); fixed-locus failures
(20); extension fixed locus (21); the 8 twists permute the family (22);
realisable constant twists by torus propagation (23); residual order 4 (24);
residual order 8 (25); orbits 208 (26); orbit histogram chart (27); orbits 120
(28); orbit histogram extension (29); simplex dims (30); Burnside chart-32
(31); Burnside chart-128 (32); Burnside divisibility ×2 (33); sector multisets
561 (34); products-in-family 278528, route A (35); route B with exactness
assertion (36); slow/fast cross-check on 3000 pairs (37); by-sector-pair table
(38); monomial closure (39); monomial inverses (40); identity in the carrier
(41); adjoinability 0 of 512 (42); defect census 384 (43); defect sector split
(44); defect ∩ carrier (45); $\Delta^B(H,H)$ witness (46); finite-order 384
(47); finite-order sector/order histogram (48); non-flat 632 with split (49);
non-commuting 576 with split (50); holonomy unitarity (51); orbit-closure 8
rows (52); the 12 mass fractions (53); the 12 pairwise spreads incl. the tie
(54); 2624 invariance checks (55); 1312 further checks (56); counting-measure
invariance (57); support bound 527 (58); the two big integers compared
character-exact against the paper's bytes (59); off-tree byte-identical output
(60); three by-hand mutants (61); clean-run gate count (62); the eight verbatim
windows located in their sources (63).

**Delivered quantities compared: 61. Exact: 61. Numerical disagreements: 0.**

---

## 7. HOUSEKEEPING

- Hashes verified identical at review start and review end (§ header). The
  targets are untouched in the working tree.
- Concurrent seats: no file other than this one was written by this seat; no
  uncommitted sibling state was read.
- The pin's must-nots hold in this seat's own reading: no expectation of any
  kind was computed by this review either, and nothing here asserts an area
  law, a string tension, a potential or a confinement claim.
- **Between delivery and adjudication every headline is a candidate reading**,
  including the two MAJORs above.
