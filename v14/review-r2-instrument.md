# R2 — HOSTILE REVIEW, INSTRUMENT LENS (R3)

**Protocol:** `v14/note-r2-hostile-protocol.md` (`3768846aebe9`), K5 primary, all
kill-shots at instrument depth.  **Pin:** `v14/note-r2-manifold-pin.md`
(`76d42dfbc900`).  **Object:** the frozen R2 delivery, hashes verified before
any work and re-verified after all of it — paper `cc78e9373bbe`, code
`36a10324b93f`, output `cb8493a13c39`, receipt `7b128499b246`: **all four
unchanged**.  The five anchor targets are also unchanged
(`4115dcd83cfa`, `c9bc956fe751`, `65bb1fc5231f`, `379194959fbc`, and the pin).
**Discipline:** scratch-only; nothing imported from the unit's code; subprocess
invocation of its CLI only; read-only git; `v14/paper-01-*` and `v14/code/r1_*`
never opened.  This file is my single repo write.

**GRADE: ACCEPT-WITH-FIXES.**

The measurement is right and it is right everywhere I could reach.  A
from-scratch re-implementation written from the pin's and paper's declared spec,
importing nothing, reproduces the grid (109 rules, coordinate set **and**
order), the census (14 of 109, the five REFUSES, every component size and
completeness fraction), the standards (1-of-80 circle links, the single
exception at chart 4 of R051, INCONSISTENT at 14 of 14, local dimensions
{1,2,3}), the block constants at both arenas, the b₁ table, the B₂ persistence
table, the 40,320-action sweep, and the controls: **3,770 receipt/paper cells
recomputed, zero mismatches against the receipt.**  Two plain runs are
byte-identical to the committed artifacts.  All 14 mutants die exactly as
declared.

What fails is the **protection**, and it fails harder than R1's did.  All five
R1 injection classes survive against this unit, plus six of the seven
unit-specific classes — **11 of 13 executed injection classes reach a delivered
artifact at exit 0 with 42/42 gates passing**.  The unit's central compliance
claim — that it is born compliant with the two #10 engravings — is true of the
render gate for the two tables it covers and **false of the verdict gate**: the
"segment-by-segment rebuild" is the same function called twice on the same
input, so a *fully typed* nine-segment verdict naming a rule that does not exist
passes every gate.  In addition the paper carries **two false numbers by value**
and two mislabelled denominators.  Every repair below is definite and small.

---

## Execution counts

| | |
|---|---|
| plain delivery runs on the scratch copy | **3** (all byte-identical, and identical to the committed artifacts) |
| CLI-contract probes (`--list-mutants`, unknown arg, unknown mutant) | **3** |
| independent 14-mutant falsifier audit (my own runs) | **14** |
| `--selftest` (1 top-level + 14 spawned subprocesses) | **15** |
| crafted injections (16 source patches + 1 on-disk data corruption) | **17** |
| **total process-level executions of the unit's CLI** | **52** |
| independent measurements rebuilt from scratch (rule × arena) | **218** |
| receipt/paper cells recomputed independently | **3,770** (0 mismatches) |
| R2-A actions swept by my own implementation | **40,320** (0 counterexamples) |
| SLIDING rules checked against a closed-form circulant prediction | **30** (60 predicates, 0 mismatches) |
| anchors traced to pinned bytes | **5** |
| verdict rebuilds from the receipt alone | **1** (9 segments, byte-identical) |

---

# FINDINGS, most severe first

## M1 (MAJOR) — the verdict gate is a self-comparison; the #10 engraving is met in letter and defeated in substance. §8's description of it is a false gate claim.

`G-VERDICT-STRING-EQUALITY` reads:

```
head, segs, full = build_verdict(payload, swap_pairing=(MUTANT == "verdict-pair-swap"))
rebuilt = head + "<" + "|".join([s[1] for s in build_verdict(payload)[1]]) + ">"
gate("G-VERDICT-STRING-EQUALITY", ..., full == rebuilt, ...)
```

The "rebuild" is **the same function on the same payload**.  It compares the
audited component against a copy of itself routed through the audited component
— the #219 disease, recurred at exactly the gate the #10 engraving created, and
therefore a MAJOR by default under the #313 addendum.  Its only discriminating
bit is `swap_pairing`, a parameter that exists solely to be the declared
mutant.  Everything upstream of `build_verdict` is invisible to it.

Measured, each a complete plain run — `exit 0`, **42/42 gates PASS, 0 FAIL, 0
tracebacks, both artifacts written**:

| id | corruption (applied to `payload`, i.e. to the measured values) | emitted result |
|---|---|---|
| **INJ1** | swap the B2 and CONSTANTS segment **values** between their **names** (R1's INJ_B) | `…\|B2-PERSISTENCE=DENSITIES-CONSTANT-B-TO-B2-AT-109-OF-109;UNDEFINED-B2-DENSITY-AT-28\|…\|BLOCK-CONSTANTS=SURVIVES-AT-14-OF-14;COMPONENTS-DOUBLE-AT-14>` — **survives** |
| **INJ2** | type the STANDARDS segment (R1's INJ_C) | `STANDARDS=LINK-CIRCLES=80-OF-80-CHARTS;DIMREAD=CONSISTENT;LOCAL-DIMENSIONS=2;…` — **survives** |
| **INJ3** | append a qualifier to MECHANISM (R1's INJ_E) | `…(CLASSES=G2+G3-UNIONS;MODES=SLIDING)-AND-SUBSTRATE-MOTIVATED` — **survives** |
| **INJ16** | replace **all nine** segments with literals | `R2-LOCALITY-AT<RULES=1-OF-1:R999\|GRID=TYPED\|MECHANISM=TYPED\|COMPONENTS=TYPED\|STANDARDS=TYPED\|B2-PERSISTENCE=TYPED\|NULL=TYPED\|REFUSES=0-OF-1\|BLOCK-CONSTANTS=TYPED>` — **survives** |

INJ2 is the sharpest publishable failure: the unit's headline negative finding
(`DIMREAD=INCONSISTENT`, links circles at 1 of 80) is emitted **inverted** with a
green receipt.  INJ16 settles the question of how much the gate knows about the
measurement: **nothing**.

`G-VERDICT-SEGMENTS-FLIPPABLE` does not help.  Its nine perturbations append
`-PERTURBED`/`;PERTURBED` or change a count, and `build_verdict` is string
concatenation, so all nine flips are **True for every input**: the gate tests
that the string builder is injective, never that a segment carries measured
content.  It passed unchanged under INJ16.  `G-VERDICT-BOTH-HEADS-REACHABLE` is
the same class — it synthesises two payloads and checks the `if locality_rules`
branch, which cannot fail.

**Repair (definite, one function).**  Build the comparator from the receipt-side
objects, not from `payload`: rebuild each of the nine segments inside the gate
directly from `census_rows`, `standards`, `b2_persistence`, `block_constants`,
`grid` and `r2a_verification` — the derivation I performed in K5(d) below,
which reproduces the emitted string byte-identically — and gate
`rebuilt == full`.  Then add a mutant that perturbs one *measured* input (not
the pairing flag) and confirm the gate fires.  Until that is done, §8's sentence
"the **complete** emitted string is compared for equality against a
segment-by-segment rebuild" is **a false claim about the instrument**, and the
compliance sweep's `#10 containment is not equality → G-VERDICT-STRING-EQUALITY`
row is false with it.

---

## M2 (MAJOR) — `G-RENDER-FROM-GATED-OBJECT` covers 10 fields of ~40 rendered ones; every other table is an ungated render path (R1's INJ_D class, recurred)

`render_check` compares exactly `block_constants[i]["B"]` on
`{E_N, F, F_COH, edges}` and `census_rows` on
`{cells, edges, components, component_sizes, completeness, status}`.  It touches
**none** of: the whole `B2` column of `block_constants`; `b2_density`,
`ncoh_per_incidence`, `ncoh_per_pair`, `b2_coh`; `census_rows.noncomplete_components`;
`standards` (paper §5, output §6); `b1_per_component` (§6.2, output §7);
`b2_persistence` (§7.1, output §9); `positive_control`; `scramble_control`;
`parity_witness`; `mode_probe`; `alt_drawing_group_probe`; `arena_declaration`;
`grid`; `r2a_verification`; `verdict`.

**INJ4** (one plain run, `exit 0`, 42/42 PASS) corrupts seven of those cells
after measurement.  All seven reach the delivered receipt **and** the delivered
`output.txt`:

```
block_constants[0].B.b2_density         99/100     (true 4/7)
block_constants[0].B.ncoh_per_incidence 7/3        (true 5/3)
block_constants[0].B2.E_N               999        (true 42)
standards.R005.reading                  CONSISTENT (true INCONSISTENT)
standards.R005.links_that_are_circles   77         (true 0)
b1_per_component.R005.b1_of_N           4242       (true 0)
b2_persistence.R005.completeness_B2     1/1        (true 2/7)
```

Two further runs show the same path reaching the **verdict**, not just the
tables:

- **INJ9** — corrupt `b2_persistence[R005].survives/doubles` after
  `G-B2-PERSISTENCE-MEASURED`: emitted
  `B2-PERSISTENCE=SURVIVES-AT-13-OF-14;COMPONENTS-DOUBLE-AT-13`, `exit 0`.
- **INJ15** — flip `consts[0]["densities_constant_B_to_B2"]` after
  `G-COPY-REDUCTION`: emitted
  `BLOCK-CONSTANTS=DENSITIES-CONSTANT-B-TO-B2-AT-108-OF-109`, `exit 0`.

**Repair.**  Make `render_check` total: iterate every key of every rendered
object and compare it to the live measurement, or (better) derive the rendered
objects from `census` at render time rather than accumulating them in `R` and
checking a subset.  The two declared mutants (`table-corrupt`,
`census-row-corrupt`) both aim at the covered 10 fields and so certify only
those.

---

## M3 (MAJOR) — the 2-cell census has no independent route; a per-block-uniform 2-cell drop rewrites §6.1 wholesale and moves two verdict segments (R1's M1, recurred)

`G-COHERENCE-FORCED` compares `F_COH` against the **unfiltered** `F_N`, so the
first direction of R1's M1 (a coherent cell wrongly *excluded* from the filtered
list) **is** repaired — my **INJ13** (drop one entry from `coh`) dies `exit 1` on
`G-COHERENCE-FORCED`.  Good.  But `F_N` itself has no comparator.

**INJ5** drops the first 2-cell of each **block** (per-block-uniform, exactly
R1's INJ_A design).  `exit 0`, 42/42 PASS, both artifacts written.  `G-COPY-REDUCTION`
passes because the drop is per-block uniform; `G-STANDARDS-IDENTITIES` passes
because `star_F` is summed from the same reduced list; `G-COHERENCE-FORCED`
passes because `coh` is filtered from it; `G-BOUNDARY-PARITY` only requires a
non-zero delta somewhere.  Delivered:

```
block_constants[0].B  F 35 -> 34 , F_COH 35 -> 34 , b2_density 4/7 -> 19/34 ,
                      ncoh_per_incidence 5/3 -> 34/21 ;  B2.F 70 -> 68
verdict STANDARDS   : LINK-CIRCLES=1-OF-80-CHARTS -> 6-OF-80-CHARTS
verdict CONSTANTS   : UNDEFINED-B2-DENSITY-AT-28 -> AT-35
```

So the §6.1 table, the §5 headline and one verdict segment all move on a
corruption that nothing sees.

**Repair.**  Recount the 2-cells by a second route that does not share the
enumeration — e.g. for every cell, count triangles of the *drawn-pair graph
restricted to that cell* by an independent triangle enumeration, and gate the
total against `len(twocells)`; the OR/XOR parity probe already walks the same
triples and could carry the AND count for free.

---

## M4 (MAJOR) — the locality flag and the REFUSES flag are single unguarded bits; one flip removes a rule from the headline census and ships a self-contradictory receipt

`any_noncomplete` and `refuses` are booleans derived once and then consumed by
`locality_B`, `census_rows.status`, `render_check`'s expectation, and
`G-COUNTS-COMPUTED` — all of which read **the same bit**, so they agree with each
other whatever it says.

- **INJ8** sets `any_noncomplete = False` at R005/B only.  `exit 0`, 42/42 PASS.
  Emitted: `RULES=13-OF-109` (R005 gone),
  `STANDARDS=LINK-CIRCLES=1-OF-73-CHARTS`,
  `B2-PERSISTENCE=SURVIVES-AT-13-OF-13;COMPONENTS-DOUBLE-AT-13`.  The delivered
  receipt then carries, **simultaneously**:
  `census_rows[R005].status = "clique-only"` and
  `census_rows[R005].noncomplete_components = [{size 7, edges 6, pairs 21, …}]`.
  A component that is not complete, in a rule labelled clique-only, in a
  green receipt.
- **INJ7** sets `refuses = False` everywhere.  `exit 0`, 42/42 PASS, emitted
  `REFUSES=0-OF-109` while five rules genuinely draw nothing.  The declared
  `refuses-skip` mutant catches the *skip* (returning `None`), never the
  *reclassification*.
- **INJ10** zeroes every positive `b1_graph`.  `exit 0`, 42/42 PASS, emitted
  `RULES-WITH-NONTRIVIAL-B1=0`, `b1_nontrivial_at = []` — §6.2's entire finding
  erased — and the receipt ships the arithmetically impossible row
  `b1_per_component.R008 = [[7, 12, 0], …]` (7 vertices, 12 edges, cycle rank 0).

**Repair.**  Derive `status`, `any_noncomplete`, `refuses` and `b1_graph` afresh
inside the gate from `per_component`/`edges` rather than reading the stored
flags: gate `any_noncomplete == any(not c["complete"] for c in per_component)`,
`refuses == (edges == 0)`, and `b1_graph == edges - size + 1` per component.
Each is one line and each currently has zero falsifiers.

---

## M5 (MAJOR) — the grid gate checks coordinates, not cells; a silently dropped sliding window survives with the grid reported complete

`G-GRID-CELL-COMPLETE` compares the enumerated **coordinate** set against
`expected_grid_coords`, which is genuinely independent (divisor arithmetic) —
good.  But nothing compares the **cells a rule generates**.

**INJ6b** drops one interior sliding window inside `cells_from_orbits`.
`exit 0`, 42/42 PASS; `grid.size = 109`, `G-GRID-CELL-COMPLETE` and
`G-GRID-NO-DUPLICATES` both green, `G-MODES-DISTINCT` green (it compares two
equally-corrupted constructions through the same function).  Delivered:

```
COMPONENTS=NONCOMPLETE-COMPONENT-SIZES=3+4+5+6+7   (true 4+7)
COMPONENTS=…;RULES-WITH-NONTRIVIAL-B1=8            (true 9)
STANDARDS=LINK-CIRCLES=2-OF-77-CHARTS              (true 1-OF-80)
BLOCK-CONSTANTS=…;UNDEFINED-B2-DENSITY-AT-29       (true 28)
```

Four verdict clauses moved on a dropped cell that the "cell-completeness" gate
does not look at.  (A first attempt, INJ6, dropped the wrap-around window; that
window always contains the transport's fixed point, whose pairs are never drawn,
so it executed with no measurable effect — reported here for honesty, not as a
finding.)

**Repair.**  Extend the completeness comparator one level down: rebuild each
rule's cell set from the declaration (`|cells| = M` for SLIDING, `C(M,c)` for
ALL, `⌈M/c⌉` for BLOCKWISE, before dedup) and gate the count and the multiset of
cell sizes against `rule_cells_on_block`.

---

## M6 (MEDIUM) — falsifier coverage: 30 of 42 gates have no falsifier, four of them cannot fail at all, and the receipt carries no never-falsified census

All 14 mutants die on exactly their declared gate (my own runs, §"what I could
not break"), but they name only **12 distinct** gates.

**Falsified — 12 of 42:**

| gate | falsifier(s) |
|---|---|
| `G-FLOATGUARD` | `float-leak` |
| `A-R0-I6` | `anchor-hash` (and my INJ12, a real on-disk value edit) |
| `G-GRID-CELL-COMPLETE` | `grid-drop` |
| `G-EVERY-RULE-RECORDED` | `refuses-skip` |
| `G-DRAW-TWO-ROUTES` | `census-corrupt`, `orbit-corrupt` |
| `G-R2A-NULL-CLIQUE-ONLY` | `locality-inject` |
| `G-COMPLETENESS-TWO-ROUTES` | `complete-flip` |
| `G-POSITIVE-CONTROL` | `toy-broken` |
| `G-MODES-DISTINCT` | `locality-erase` |
| `G-SCRAMBLE-CONTROL` | `scramble-inert` |
| `G-VERDICT-STRING-EQUALITY` | `verdict-pair-swap` (vacuously — see M1) |
| `G-RENDER-FROM-GATED-OBJECT` | `table-corrupt`, `census-row-corrupt` |

**Never falsified — 30 of 42, with an honest denominator and a reason each:**

| class | gates | why |
|---|---|---|
| **cannot fail on any input (dead predicate)** — 4 | `G-ANCHOR-COUNT` (`verify_anchors` raises on the first bad anchor, so `all(a["ok"])` is always True), `G-B2-PERSISTENCE-MEASURED` (`len(persist) == len(locality_B)` where `persist` is built by iterating `locality_B`), `G-VERDICT-SEGMENTS-FLIPPABLE` (string concatenation is injective in each coordinate), `G-VERDICT-BOTH-HEADS-REACHABLE` (checks the `if/else` branch it just took) | #208: these are not gates |
| **analytically forced (a theorem check, not a measurement)** — 5 | `G-R2A-EXHAUSTIVE`, `G-R2A-AT-THIS-UNITS-ACTIONS`, `G-ORBIT-CLASSES-CLIQUE-ONLY`, `G-COHERENCE-FORCED`, `G-ALT-DRAW-PROBE` | each has implementation-comparator teeth (two routes / actual map composition) but can never report a fact about the substrate; the paper is honest about R2-A and coherence, silent about the other three |
| **shadowed** — 2 | `G-R2A-AT-THIS-UNITS-ACTIONS`, `G-R2A-EXHAUSTIVE` are unreachable by `orbit-corrupt` because `G-DRAW-TWO-ROUTES` fires earlier in `run()` | ordering artefact, not a defect |
| **anchors with no mutant** — 4 | `A-PIN-R2`, `A-R1-ADJ`, `A-R0-I3`, `A-ERRATUM-TOP-PAPER` | exit-1-only; the pin asks for "anchor-hash corruption for every I-row used" and it is met 1-of-5 by name |
| **genuinely unfalsified** — 15 | `G-BLOCKSIZE-FROM-I6`, `G-GROUP-CAP`, `G-ARENA-DECL-MATCHED`, `G-GRID-NO-DUPLICATES`, `G-GRID-NOT-TRUNCATED`, `G-COMPONENTS-TWO-ROUTES`, `G-UNDEFINED-PATH-LIVE`, `G-STANDARDS-CONTROLS`, `G-STANDARDS-CONTROL-BETTI`, `G-STANDARDS-IDENTITIES`, `G-COPY-REDUCTION`, `G-SYMMETRY-SELFTEST`, `G-CACHE-EXERCISED`, `G-BOUNDARY-PARITY`, `G-LATTICE-CROSSCHECK`, `G-COUNTS-COMPUTED`, `G-NO-FLOATS-IN-RECEIPT` | no declared mutant reaches them |

(The last row lists 17 names; two of them, `G-GRID-NOT-TRUNCATED` and
`G-COUNTS-COMPUTED`, are additionally near-dead: the first compares a
hard-set literal `truncated = False` against `False` and otherwise duplicates
`G-GRID-CELL-COMPLETE`; the second compares totals against counts derived from
the same objects the totals were derived from.  Net distinct never-falsified
gates: **30**.)

**The era's standard is falsified-or-waived-with-the-waiver-censused.  Neither
holds here: there is no waiver list and no `never_falsified` field in the
receipt.**  R1's instrument carried one and it was EMPTY; R2 carries none and
its true value is 30 of 42.  **Repair:** compute and emit the never-falsified
set beside the gate census, and add falsifiers for at least
`G-COPY-REDUCTION`, `G-COMPONENTS-TWO-ROUTES`, `G-STANDARDS-IDENTITIES`,
`G-SYMMETRY-SELFTEST`, `G-BOUNDARY-PARITY` and `G-LATTICE-CROSSCHECK`, and an
anchor mutant per remaining anchor row.

---

## M7 (MEDIUM) — two false numbers in the paper, by value, plus two mislabelled denominators

The receipt is clean: 3,770 cells recomputed independently, **zero false
numbers**.  The paper is not.

1. **§6.1, fact 2 — FALSE BY VALUE.**  "The per-incidence density runs from
   **0/1 to 25/18** across the grid."  Measured over all 109 rules (receipt
   `block_constants`, independently reproduced): minimum **0/1**, maximum
   **5/3**, attained at R001, R022 and others.  25/18 is merely the
   *second*-largest distinct value (the sorted top is 5/3, 25/18, 4/3, 10/9, …).
   The paper's own §6.1 table prints `R001 … per-incidence 5/3` four lines
   above.  **The correct sentence is "from 0/1 to 5/3".**
2. **§5, first bullet — FALSE BY VALUE.**  "At c = 2 every link is edgeless
   except at R048, where **two charts** carry one link edge apiece."  R048's
   links are, per chart 1…7: `(2,1,1,0) (3,1,2,0) (2,1,1,0) (2,0,2,0) (2,0,2,0)
   (2,0,2,0) (1,0,1,0)`.  **Three charts** — 1, 2 and 3 — carry exactly one link
   edge.  (Everything else in that bullet checks out: b₁ = 0 throughout at
   c = 2; at c = 3 b₁ = 0 at five of six rules and R051 reaches 2; at c = 4 every
   link has b₀ = 1 and b₁ runs 2, 4, 6, 7.)
3. **§3.2 — mislabelled denominator.**  "**G0 clique-only at 4 of 4** rules."
   The gate's own predicate is `len(g0) == 2*len(transports)` over
   `census.items()`, i.e. **4 rule-arena measurements over 2 rules**; §4's table
   says "G0 | rules at B | 2" three pages later.  The value 4 is right, the unit
   is wrong.
4. **§9, finding 2 — same mislabel.**  "every orbit-partition **rule** (38 of
   38)".  The orbit-partition family is 2 + 3 + 14 = **19 rules**, measured at
   two arenas = 38 measurements.

Nothing else moved.  I traced every number of §§1–11 — the transports and their
orders (7, 4, 2), |⟨γ,Σ⟩| = 5040 and 240, the grid decomposition
(1+1+18+7+24 / 1+2+24+7+24 = 109), the §4 class table (2/2/0/0, 3/1/2/0,
42/37/0/5, 14/11/3/0, 48/39/0/9, 109/90/5/14), all 14 rows of the §4 detail
table, the c ≥ 5 (T7) / c ≥ 4 (T4) disappearance thresholds, the §5 distinct-
reading counts (12 rules with every chart distinct; best case 6 over 7 at R048
and R051), the local-dimension pattern by c, all five §6.1 rows, all seven §6.2
rows, §7.1 (14/14/14), §7.2 (size 5, 6 of 10), §7.3 (81 of 81), §7.4 (1289 /
212 / 48; 78 of 90; delta 4000), §7.5 (0 at 5040, 0 at 240), §8 (42 / 5 / 14) —
**all confirmed.**

---

## M8 (MEDIUM) — the anchor binds the file, not the read value; a JSON-path drift is invisible

The unit reads five values out of I6 by exact path and the file is byte-anchored
(`A-R0-I6`).  I confirmed the byte read is real: **INJ12** rewrote
`tables.the_ladder.the_embedding.the_witness_system_part` to another permutation
on disk and the run died `exit 1` on `A-R0-I6`
(`measured bda62165…`, expected `c9bc956fe751`), no artifacts written.  I also
confirmed all five read values against the pinned receipt by hand:
`witness_system_part = [0,2,3,4,5,6,7,1]`,
`lex_first_Q_per_order["4"] = [0,1,3,4,5,2,7,6]`,
`the_declared_completion_transposition = [0,3,2,1,4,5,6,7]`,
`system_triple_dimension = 8` — all exact, and the paper's §2.2 provenance
sentences are faithful to the receipt's own key names.

But nothing gates the **path** or the **value**.  **INJ11** changed one path
component, `lex_first_Q_per_order["4"] → ["6"]`.  `exit 0`, 42/42 PASS, **5/5
anchors green**, and the unit delivered an entirely different study:

```
T4 gamma = [0,1,3,2,5,4,7,6]  (order 2, not 4)
grid = 115 rules, TOTAL=115, REFUSES=6-OF-115
RULES=8-OF-115 , COMPONENTS=NONCOMPLETE-COMPONENT-SIZES=7 ,
STANDARDS=LINK-CIRCLES=1-OF-56-CHARTS , UNDEFINED-B2-DENSITY-AT-74
```

The receipt is self-disclosing (it prints `gamma_order: 2`), but no gate binds
the read value to the declaration the paper makes about it ("order 4", "the
lex-first completion permutation at defect order 4"), and those two facts are
typed in the paper, not computed.  `G-BLOCKSIZE-FROM-I6` checks only
`len(gamma) == 8`.

**Repair.**  Gate the read values, not just the file: assert
`perm_order(gamma7) == 7`, `perm_order(gamma4) == 4`, `perm_order(sigma) == 2`,
the cycle types, and `|⟨γ,Σ⟩| ∈ {5040, 240}` as declared coordinates matched at
every coordinate (§15), and print the paths beside them.  Cost: five lines.

---

## M9 (MEDIUM) — the delivered artifacts carry no falsification evidence (regression against R1)

R1's instrument ran the whole mutant table inside the delivery run (its G33) and
put the outcome, plus a `never_falsified` set, into the receipt.  R2 does not:
`R["mutants"]` is the **declaration** table only, output §13 is headed "MUTANTS
DECLARED (14) — each must exit 1 on a NAMED gate" and lists names with no
outcome, and the deaths exist only in `--selftest`'s stdout, which is written
nowhere.  A reader of `r2_manifold_receipt.json` has no evidence that any mutant
was ever run.  §8's "14 declared mutants, all dead" is true — I verified it
twice, once by my own 14 runs and once via `--selftest` — but it is not carried
by the artifacts.

**Repair.**  Run the table in-delivery (guarded by `if not MUTANT`) and record
per-mutant exit code, named gate, and the computed never-falsified set.

---

## M10 (MINOR) — forced clauses in must-pass position (#208), and one overclaimed "two routes"

- `G-COHERENCE-FORCED` is registered as a raising gate.  The paper's §3.3 is
  scrupulous ("true by algebra for every input, so per RUNBOOK §14 (#208) it is
  a **disclosure**"), but mechanically it is a must-pass gate that aborts the
  run.  #208's text is "analytically-forced clauses … are disclosures, **not
  must-pass gates**".  Form, not substance — and the gate does have
  implementation teeth (`F_COH` is computed by actually composing the three
  drawn maps and compared against the unfiltered `F_N`; my INJ13 kills it, and
  the scramble control moves it at 81 of 81).  Same class, less honestly
  labelled: `G-ORBIT-CLASSES-CLIQUE-ONLY` (the partition corollary is proved in
  §3.2) and `G-ALT-DRAW-PROBE` (the receipt's own `reason` field states the
  algebra: |⟨γ,Σ⟩| > 8 ⇒ no regular orbit ⇒ nothing drawn).
- **§4's "two routes" for completeness is one route.**  `G-COMPLETENESS-TWO-ROUTES`
  recomputes `scan` by iterating the same `_edges` over the same pairs with the
  same nested loop as `got` in `measure_rule`.  It is a stored-flag-versus-
  recomputation *tamper* check (which is why `complete-flip` dies on it), not
  two independent computations.  `G-COMPONENTS-TWO-ROUTES` (union–find vs
  |V| − rank ∂₁ over 𝔽₂) and `G-DRAW-TWO-ROUTES` (orbit/stabiliser vs brute
  force) **are** genuinely two routes; I verified both independently.
- **The compliance sweep is typed prose.**  Nineteen of its twenty `status`
  strings are literals; only one is computed (`"G-VERDICT-STRING-EQUALITY" in
  names`).  Two of the literals are, as measured above, false: the #10
  containment row (M1) and "#208 forced clauses are disclosures" (they are
  gates).  This is R1's M8 class.

---

## M11 (MINOR) — the 40,320 denominator counts permutations, not actions

`G-R2A-EXHAUSTIVE` sweeps one cyclic action per permutation of 8 labels.  I
reproduced it: 40,320 sweeps, 0 counterexamples — but the number of **distinct**
cyclic groups ⟨p⟩ so obtained is **14,170**, because ⟨p⟩ is generated by φ(ord p)
elements.  The paper's wording is honest ("one per permutation, 40,320
actions"); the verdict segment's `40320-SWEPT-ACTIONS` is not, and it is
flippable: **INJ14** truncated the sweep to 100 permutations and delivered
`R2-A-VERIFIED-10-UNIT-ACTIONS-AND-100-SWEPT-ACTIONS-0-COUNTEREXAMPLES` at
`exit 0`, 42/42 PASS.  **Repair:** emit the distinct-group count beside the
permutation count, and gate `sweep_actions == factorial(blocksize)` rather than
`> 0`.

---

# What I could not break — confirmations

- **The CLI contract is exactly as documented, verified in code before use.**
  No args → delivery, both artifacts written, `exit 0`, and every gate runs
  before any write (`open(OUT_TXT,"w")` is the last statement of `deliver()`).
  `--mutant NAME` → `exit 1` on a named gate with no write; a *surviving* mutant
  would return 3 with `MUTANT … SURVIVED` on stderr (never observed).
  `--list-mutants` → 14 names, `exit 0`.  `--selftest` → 14 subprocesses, all
  DEAD, artifacts byte-unchanged, `exit 0`.  Unknown argument and unknown mutant
  → `exit 2`.
- **The 14-mutant table is honest to the row.**  My own 14 independent runs:
  every mutant `exit 1`, **zero tracebacks**, each dying on **exactly** the gate
  its row declares, and both on-disk artifacts byte-unchanged after each.  No
  gate predicate references mutant identity (grep-verified: all 14 `MUTANT ==`
  sites live inside measured functions or the derivation, none inside a `gate()`
  argument) — the letter of #208 holds.
- **Two-run byte-identity, reproduced.**  Two plain runs on the scratch copy
  emit `cb8493a13c39` / `7b128499b246` — identical to the committed artifacts —
  and byte-identical stdout.  A third run, after the full 14-mutant audit and
  the selftest, gives the same two hashes again.
- **The verdict rebuilds from the receipt alone, byte-identically.**  I
  reconstructed all nine segments from `locality_census`, `grid`, `census_rows`,
  `b1_nontrivial_at`, `standards`, `b2_persistence`, `r2a_verification` and
  `block_constants` and got `rebuilt == verdict.string` exactly.  The paper's
  quoted verdict equals the emitted string exactly (line breaks removed as
  stated), and `output.txt` carries the same line.  This is precisely why M1's
  repair is available: the honest comparator exists, the unit just does not use
  it.
- **The anchor byte-read is sound** (INJ12) and all five anchors trace to the
  pinned bytes, re-confirmed after all work.  The `A-ERRATUM-TOP-PAPER` row
  carries the LOG #4 erratum's corrected companion hash `379194959fbc` and it
  matches disk.
- **The UNDEFINED path is live and honest**: 28 rules with `F_COH = 0` reach it,
  each with `b2_density_undefined_reason` set; independently reproduced.
- **The controls are real.**  Tetrahedron (4,6,4; b = 1,0,1), 9-vertex torus
  (9,27,18; 1,2,1), pinch point (7,12,8; 1,0,2) — all reproduced from my own
  implementation, and the pinch point correctly fails every-link-a-circle.  The
  positive control (cells {1,2,3}, {3,4,5}, shared label 3) returns a component
  of size 5 with 6 of 10 pairs: reproduced.
- **The scramble and parity controls have declared, unselected tested sets**:
  81 rules with F(N) > 0 and 90 rules with a cell of ≥ 3 labels — both
  reproduced exactly, as are `moved = 81/81`, `fixed = 81/81`, `78 of 90` and
  `total delta 4000`.
- **`G-CACHE-EXERCISED` is non-vacuous** (`hits > 0 AND misses > 0`; measured
  1289/212) and the symmetry self-test really does bypass the memo
  (`f2_rank(fresh=True)`, 48 fresh evaluations gated non-zero).

---

# K1–K5 at instrument depth

**K1 — the circulant question.  ANSWERED: the census is a theorem of the
declaration.**  Write the rule's cosets in the canonical min-label order
P₀ … P_{M−1} and let pos(x) be the index of x's coset.  For a SLIDING rule of
width c, a and b are co-celled iff their cyclic coset-distance is ≤ c − 1; by
R2-A they are drawn iff additionally they share a **regular** orbit.  Hence

> E(rule) = #{ {a,b} ⊆ one regular orbit : min(|pos a − pos b|, M − |pos a − pos b|) ≤ c − 1 }

I tested this prediction against the measured edge count **and** the measured
non-completeness verdict at **all 30 SLIDING rules of the grid: 30/30 and 30/30,
zero mismatches** — no atlas run required.  Consequences, all recomputed:

- (a) **Non-completeness is an inequality in the declaration.**  The
  non-complete component is always the regular orbit; completeness holds iff
  every pair of its labels lies within cyclic coset-distance c − 1.  For T7
  (regular orbit = 7 of the 8 singleton cosets, one fixed point removed) the
  max distance on the 8-cycle is 4, so locality ⟺ c ≤ 4, i.e. it vanishes at
  **c ≥ 5** — the measured threshold.  For T4 (regular orbit {2,3,4,5}, max
  distance 3) locality ⟺ c ≤ 3, vanishing at **c ≥ 4** — the measured
  threshold.  Both derived, both matched.
- (b) **The measured b₁ values are the formula's output.**  b₁ = E − V + 1 with
  E from the formula: T7 trivial-H gives E = 6(c−1) → 6, 12, 18 and b₁ = 6c − 12
  → **0, 6, 12**; T7 with H = ⟨Σ⟩ (M = 7 cosets, the pair {1,3} sharing a
  coset) gives 7, 14 and b₁ = **1, 8**; T4 gives 3, 5 and b₁ = **0, 2**.  Exactly
  the delivered triples.
- (c) **The whole 14-of-109 census is derivable from the grid declaration
  without running the atlas** — I did it, above, for every SLIDING rule, and the
  non-SLIDING classes are settled by the partition corollary (which is itself a
  theorem).

Per #208 the epistemic labels must move: **measured** = the grid, the coset
order convention, and the drawing relation (i.e. the declaration); **forced** =
which rules are local, their component sizes, their completeness fractions and
their b₁.  The locality is not killed — it is real, and satisfiable — but the
census clauses of the verdict (`RULES=14-OF-109`, `COMPONENTS=…SIZES=4+7;
RULES-WITH-NONTRIVIAL-B1=9`) are consequences of the declaration, not
observations about the substrate, and the verdict should say so.

**K2 — motivation.**  The instrument's own data supports the sceptical reading.
`G-LATTICE-CROSSCHECK` shows the Σ-mixed lattice's trivial subgroup reproduces
the cyclic lattice's exactly — so 6 of the 14 locality rules (R030, R033, R036,
R088, R091 and their partners) are *duplicates* of G2 rules under a differently
named lattice, and nothing in I6's own structure distinguishes them.  The only
Σ-derived content in the whole census is the coset {1,3} of ⟨Σ⟩, which is what
makes R048/R051 differ from R005/R008 (7 and 14 edges instead of 6 and 12) —
and Σ enters *only* as a cell generator, never as a drawing group
(`G-ALT-DRAW-PROBE`: 0 pairs at both transports).  So the substrate contributes
the orbit structure; the window width, the mode, and the coset ordering are all
free choices, and the measured fact is that **the census is a function of those
choices alone** (K1).  That is an instrument-level argument for
LOCALITY-DECLARABLE over LOCALITY-FOUND; the adjudication is R1-lens/R2-lens
work, not mine.

**K3 — the standards.**  Verified in full and independently: link profiles at
all 80 charts, the single circle at chart 4 of R051 with link (5,5,1,1),
INCONSISTENT at 14 of 14, 12 rules where every chart is distinct, the best case
6 over 7 at R048 and R051, local dimensions {1} → {1,2} → {2,3} tracking c.  One
paper-level correction (M7.2: three charts, not two, carry a link edge at
R048).  A consistency requirement is reachable in principle only if every chart
of the component has the same (dimprofile, star, link) triple; K1's formula
makes that a statement about vertex-transitivity of the coset-position
circulant restricted to the regular orbit — and the restriction is exactly what
breaks it, since removing the fixed point's coset destroys the circulant's
vertex-transitivity.  Within this grid class the reading can therefore be
consistent only if the regular orbit is the *whole* label set, which the arena
forbids (the transports fix label 0).  That is a provable no, inside the grid.

**K4 — scope.**  Two transports, both printed, census reported at both, both
named in the verdict — a strict T7-only sub-census is recoverable from
`census_rows` and gives 8 locality rules of 51.  The five REFUSES are recorded
and reproduced (R002, R021, R054, R079, R081).  **B₂ component accounting
verified exactly**: at all 109 rules `E_N`, `F`, and drawn-pair counts double
exactly and all three densities are unchanged (109/109, reproduced); at the 14
locality rules the non-complete component count doubles 14/14 and componentwise
completeness is unchanged 14/14.  The mechanism is disjointness — no block
interaction is possible here, because `cells_on_arena` copies cells block-locally
and the lifted transport never crosses blocks, so B₂ is a disjoint sum by
construction and additivity of b₀/b₁/b₂ over disjoint sums makes the doubling
forced.  The unit measures it rather than assuming it, which is right, but "a
case where blocks could interact" **does not exist in this construction** — the
pin's control question is unanswerable inside the declared arena, and the paper
should say that rather than reporting 14/14 as evidence.  **The coherence
corollary**: N_coh = N at **218 of 218**, independently reproduced; it is
forced, the paper says so, and `G-COHERENCE-FORCED` is nonetheless a must-pass
gate (M10).

**K5 — instrument.**  (a) CLI contract confirmed in code, then exercised: 52
process-level executions.  (b) Falsifier audit clean and honest, 14/14; coverage
audit in M6 — **30 of 42 never falsified, four of them unfalsifiable.**  (c)
Injections: **13 executed classes, 11 survive undetected** (M1 ×4, M2 ×3, M3,
M4 ×3, M5, M8, M11 — INJ1/2/3/16, INJ4/9/15, INJ5, INJ7/8/10, INJ6b, INJ11,
INJ14), **2 die as designed** (INJ12 anchor, INJ13 coherence), 1 executed with
no measurable effect and is not counted (INJ6).  (d) Verdict rebuilt from the
receipt alone, byte-identical, all nine segments derivable; each segment then
flipped by a targeted input — **nine of nine flips reached a delivered artifact
at exit 0**, and the only clause anywhere in the verdict with a real falsifier
is NULL's `G0-CLIQUE-ONLY` (via `locality-inject`), whose sibling clause
`…-SWEPT-ACTIONS` is itself flippable (INJ14).  (e) Anchors: 5 of 5 traced to
pinned bytes, read values checked against the pinned receipt by path, byte-read
proven live, path/value drift unprotected (M8); the LOG #4 erratum companion
matches.  (f) Paper↔output↔receipt: 3,770 cells, **zero false numbers in the
receipt, two false numbers by value in the paper** (5/3 not 25/18; three charts
not two) and two mislabelled denominators.  (g) Two-run byte-identity
reproduced; **all repo hashes re-verified unchanged after all work.**

---

# Verdict-segment falsifier map (for the adjudicator)

| segment | computed correctly? | declared falsifier? | survives a targeted flip? |
|---|---|---|---|
| RULES | yes | `locality-inject` (changes the list, dies on the null gate) | **YES — INJ8 (13-OF-109)** |
| GRID | yes | `grid-drop` → `G-GRID-CELL-COMPLETE` | **YES — INJ11 (TOTAL=115), INJ6b (cells)** |
| MECHANISM | yes | none | **YES — INJ3** |
| COMPONENTS | yes | none | **YES — INJ10, INJ6b** |
| STANDARDS | yes | none | **YES — INJ2, INJ5** |
| B2-PERSISTENCE | yes | none | **YES — INJ9** |
| NULL | yes | `locality-inject` → `G-R2A-NULL-CLIQUE-ONLY` (clique clause only) | **YES — INJ14 (sweep count)** |
| REFUSES | yes | `refuses-skip` → `G-EVERY-RULE-RECORDED` (skip only) | **YES — INJ7 (0-OF-109)** |
| BLOCK-CONSTANTS | yes | none | **YES — INJ15, INJ5** |

---

# Required fixes (ranked)

1. **M1** — rebuild the verdict comparator from the receipt-side objects and
   gate equality against *that*; add a mutant that perturbs a measured input.
   Correct §8's description and the compliance sweep's #10 row.
2. **M2** — make `render_check` total over every rendered field of every
   rendered object.
3. **M3** — give the 2-cell census an independent route.
4. **M4** — recompute `status`, `any_noncomplete`, `refuses` and `b1_graph`
   inside the gate instead of trusting the stored bits.
5. **M5** — extend cell-completeness one level down, from coordinates to cells.
6. **M6** — compute and emit the never-falsified set; add falsifiers for the
   six named gates and an anchor mutant per anchor row.
7. **M7** — fix the two false paper numbers (0/1 to **5/3**; **three** charts at
   R048) and the two "rules" denominators (4 and 38 are measurements over 2 and
   19 rules).
8. **M8** — gate the read values (orders, cycle types, group orders), not only
   the file bytes.
9. **M9** — run the mutant table in-delivery and record the outcome.
10. **M10–M11** — demote the forced gates to disclosures, stop calling the
    completeness check "two routes", compute the compliance statuses, and emit
    the distinct-group count beside 40,320.

None of these impeaches a measured number: I verified 3,770 of them
independently and every one is right.  They are protection defects — but M1 is
more than that, because the unit's paper states as fact a property of its
verdict gate that the gate does not have, and the unit's whole claim to
birth-compliance rests on it.
