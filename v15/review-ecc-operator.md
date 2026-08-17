# ECC (paper-46) — OPERATOR seat review (K1) — FROZEN

**Seat:** K1 / OPERATOR (hostile). **Unit:** v15/paper-46-ecc.md `61d330d13fe0`,
v15/code/ecc_exact.py `4d2034429d21`, v15/code/ecc_output.txt `3034f0028bb3`,
v15/code/ecc_receipt.json `ea24c1fc2340`; pin v15/note-ecc-pin.md `04874b01e241`
(all digests re-verified by this seat before reading). Parents re-verified at
their sealed digests: paper-43 `0c8d1a687b14`, paper-47 `5da53943c6f7`,
paper-44 `0d677a4cbe97`, paper-45 `fa0268d99524`.

**Method.** Every load-bearing number was rebuilt FROM SCRATCH in this seat's
own code (scratch dir `…/scratchpad/ecc_k1/`: `k1_chart_lp.py`, `k1_seam.py`,
`k1_psi_misc.py`, `k1_gap16.py`, comparators), written from the parents'
committed definitions — CONTRACT's constructors (arena, cells, five declared
amplitudes, coin ring, Grover-at-tripled-scale), DISC's coin orders and PR5,
AUTOGLUE's union/seam-form/successor definitions, ARITY's a = 2 branch — never
from the unit's functions. Exact arithmetic only (`int` + `fractions.Fraction`);
own Eisenstein-integer arithmetic; own two-phase full-tableau simplex (Bland);
own Gaussian rank/nullspace; own per-column implicit-zero programme; own
canonical orders. Results compared row-by-row against the delivered receipt.

## VERDICT: **ACCEPT**

No false number found. ~1,450 independent exact value-comparisons, all EXACT.
Every charge item verified. No major. Observations below are disclosures the
paper itself already carries, recorded here for the adjudicator.

---

## Recomputation ledger (claimed vs rebuilt)

### 1. The committed-row LP (charge 1) — EXACT
Walk's start state = DISC PR5 = one basis vector at the origin's first
declared direction = CONTRACT's A-SINGLE-CELL-AMPLITUDE; initial record;
delivered order G.D (per DISC's head; at R0 the two orders coincide —
verified: 2-member target).

| class | claimed | rebuilt |
|---|---|---|
| E-BLOCK | INFEASIBLE, qmax 4/9, gap 4 | EXACT |
| E-LINE-DECLARED | INFEASIBLE, qmax 4/9, gap 4 | EXACT |
| E-LINE-COSET | INFEASIBLE, qmax 4/9, gap 3 | EXACT |
| E-TRIPLE | INFEASIBLE, qmax 4/9, gap 7/3 | EXACT |

The four gaps were additionally derived BY HAND from the support structure
(post-coin weights (1/9, 4/9, 4/9) on the start site's three cells = the
Grover column, norms (1,4,4)/9; every block/declared line through the support
writes a zero-weight cell, so p ≡ 0 and gap = 1/3+4/3+4/3+1 = 4; the three
coset zero-writer lines can carry the unit mass, gap = 3; one triple writes
exactly the two support cells {cell0, cell1} at cap 1/3, gap = 3 − 2/3 = 7/3).
The hand values agree with both the receipt and my solver.

### 2. The ceiling theorem (charge 2) — EXACT, mechanism verified
Claimed: feasibility ⇒ every Born weight ≤ 1/3; checked at 156 rows,
exceptions 0. Rebuilt: 156 rows, 0 exceptions — no row is feasible with
qmax > 1/3. Mechanism as stated is a correct theorem at all four committed
classes: every incidence matrix is 0/1, so the inclusion marginal
(Mp)_c = Σ_{e∋c} p_e ≤ Σ p = 1 = the total, and (Mp)_c = 3·q_c forces
q_c ≤ 1/3. The committed start carries 4/9 > 1/3 on two cells — the row
census and the proof agree.

### 3. The census (charge 3) — EXACT at every row
156 rows = 39 distinct targets × 4 classes; row-by-row against the receipt:
**936 field comparisons (word, qmax, gap, ceiling-witness, dim, implicit at
each of 156 rows), 0 diffs**; all 156 (class, member-multiset) keys match.

- Words: INFEASIBLE 136 / UNIQUE 8 / MANY 6 (all dim 8) / FIBER-FEASIBLE 6 — EXACT.
- Target family: 82 target rows (5 amps × R0 × 2 orders + uniform × 36
  round-fields × 2 orders), 2 TARGET-UNDEFINED (zero amplitude), 39 distinct
  defined targets — EXACT, including the member-multisets: the 38-member
  uniform target (D.G record-blind — verified at every amplitude and record),
  and the non-trivial 3-member coincidence ALTERNATING-ROOTS@R0 ≡
  uniform@ROUND-0/G.D — **verified as an exact 27-component equality**.
- Deficient-writer theorem: E-TRIPLE writer census {0:3, 2:54, 3:27} — 57
  deficient writers; my per-column maximization finds exactly those 57
  columns forced to zero on every E-TRIPLE MANY row (implicit = 57), and the
  polytope collapses onto the E-BLOCK family at the same dimension 8 — EXACT.
  The mechanism (Σ_e p_e(3−w_e) = 0 with non-negative terms) checks as a
  theorem.
- a = 2 branch: DEGENERATE-IDENTITY at 39/39 (marginal map = identity;
  q ≥ 0, Σq = 1 at every defined target) — EXACT; branch kept apart at
  every row (arm labels verified).
- Controls: forced-feasible → MANY, forced-infeasible → INFEASIBLE with
  ceiling witness — EXACT through my own predicates.
- Normalization: per-class writer censuses (E-BLOCK 3×27; E-LINE-DECLARED
  3×9; E-LINE-COSET 0×3 + 3×9, identity fails; E-TRIPLE 0×3 + 2×54 + 3×27,
  identity fails) — EXACT; free two-stage vacuous at 27/27 covered cells —
  EXACT (every cell lies in 3 blocks / 1 declared line / 7 triples —
  rebuilt).
- Round-fiber gap census (my extra check, not in the paper):
  E-BLOCK {32/27×18, 16/9×9, 8/9×6}, E-LINE-DECLARED {40/27×18, 16/9×15},
  E-LINE-COSET {10/9×18, 4/3×15}, E-TRIPLE {8/27×18, 4/9×9, 2/9×6} —
  matches the receipt value-for-value.

### 4. The seam decision (charge 4) — EXACT at every number
Own union construction (two AG(2,3) charts glued along the first
fourth-class line):

- Substrate: 15 carriers, 54 realised pairs, 455 groups, 288 seam-spanning,
  profile census (0,0,3):54, (0,1,2):108, (0,3,0):5, (1,0,2):108,
  (2,0,1):108, (2,1,0):72 — EXACT (matches receipt and AUTOGLUE's sealed
  profiles).
- Completion lattice at the committed all-simple counts: 31 points, kernel
  4, widened re-run 31 (box does not bind) — EXACT.
- Every-leg standard: lawful 162, lawful crossings 108, successor multiset
  4-valued at 81 / 8-valued at 243 over 324 seam slots, 1-valued at none,
  per-crossing size patterns (4,8,8)×81 and (8,8,8)×27, staylable 27 —
  EXACT.
- Preparedness: 29791 states, histogram (0:20100, 1:6804, 2:2034, 3:622,
  4:153, 5:18, 6:52, 9:8), best 9 at 8 states, absorbable 27 — EXACT; my 8
  best states match AUTOGLUE's published table byte-for-byte, including the
  2 carrying one completion at every seam.
- Probe family: 11 (8 best + direct-sum triple + first/last lattice points);
  the modal allowed-set relation takes exactly **2** values over them
  (allowed-set of 9 staylable crossings at the 8 best; empty at the 3
  extras) — EXACT.
- Two-step census from ALL 108 first crossings: RE-SOLVED fiber
  **(25,9),(26,36),(27,24),(28,12),(41,9),(43,18)** — EXACT, and equals
  AUTOGLUE's sealed §4.5 table collapsed over the kept column (25:3+6,
  26:24+12, 41:6+3, 43:12+6 — re-derived from the parent's own bytes).
  PERSIST-FIT differs at 108/108, PERSIST-KEPT at 108/108 — EXACT.
  **Per-crossing granularity: all 108 receipt rows (re_solved, persist_fit,
  persist_kept) reproduced exactly — 324 values, 0 diffs** (including e.g.
  51/115 fit and 6/8/10/16 kept values).
- Downstream stamp count 215 = 156 + 39 + 18 + 2 — verified.

### 5. Psi-independence (charge 5) — EXACT; accessor audited
All THREE carriers rebuilt in this seat's own code (charge asked for two):
amplitude vector; density operator ρ = ψψ† evolved by full-matrix
conjugation (diagonal read off and normalised); configuration-level process
law (transition-amplitude table, single-time marginal). At all 18 delivered
rows (5 amps × R0 × 2 orders + {uniform, single-cell} × 2 round-records × 2
orders): byte-identical Fraction tuples at every defined row, zero-amplitude
rows undefined on all three routes — 18/18 agreements, 0 separating. EXACT.
Code audit: `stamps_reach_audit` walks the call graph and requires
`measure_lp`, `measure_lp_controls`, `lp_row`, `measure_carrier`,
`born_target`, `build_targets`, `measure_debt` to reach no psi face region
and no seam machinery (debt excepted for `seam_counts`/`cross_index`,
correctly, since its census reads the union record); `psi_regions` reports
zero cross-face calls; G-PSI-EQUAL binds the three faces plus the
full-vs-block channel route. Audited and confirmed (observation 4 below).

### 6. Carrier + debt (charge 6) — EXACT
Host 4/4 (canonical 27→28 inclusion re-verified an exact isometry;
fixed-mask hosting by policy); express 2/4 (3 branches with 3 distinct
records at the committed row — rebuilt; register ⇔ express); evolve 0/4
(see observation 3); 36/36 cross pairs directionless (inside neither chart
image — rebuilt); coin family typed on 3-direction site blocks. Debt: chart
menu 27 cells, union menu 54 realised pairs, menu∩cross 0/36 (no realised
pair is a cross pair — rebuilt), frozen creation admits 54 events, all
profile (0,0,3), hence 0/288 seam-spanning (rebuilt), unit-mass amplitudes
4/4 with 4 nonzero at R0/G.D (rebuilt), a = 2 arm: 36 seam-spanning
pair-events, 0 realised cross pairs (rebuilt; ARITY's sentence located in
its bytes).

### 7. The interface table's 18 computed rows (charge 7) — EXACT
All 18 COMPUTED-HERE extents re-derived from the parents' constructors:
ACTOR 9, CELL 27, DIRECTION 3, PARALLEL-CLASS 4, LINE 12, DIVISION-EVENT
84, GROUPING 280, ADMISSIBLE-ROUND 36, RECORD-BLOCK 27 (= transversal
triangles, two routes equal — verified), QUANTUM-STATE 27, BRANCH-WEIGHT 1,
MENU 6 (coset partitions of the translation subgroups — rebuilt), COIN 6
classes (covariant census re-enumerated over Z[ω]: 36 solutions, 6 classes,
1 ±Grover), UNION-CARRIER 15, UNION-PAIR 54, CONFLICT-GROUP 455,
SEAM-COMPLETION 4 (cross-block kernel), SEAM-STATE-SPACE 29791 = 31³. The 5
SEALED-CITATION extents (30, 5784, 36, 1296, 1) match CONTRACT's own sealed
fence, re-read from its bytes. 23 = 18 + 5; four classes used; no
PRIMITIVE row; senses 6; free declarations 15 in 6 categories (list
identical to CONTRACT's free rows); fork 2 arms, grains {2,3}; maps 3.

### 8. Everything else rebuilt (charge 8)
Born sweep 370 rows / 296 defined; order fiber D.G-record-blind and
G.D-record-moves at every amplitude and record with R0 members coinciding
(370 functionals compared); residue screen (field + q on one cell ⇒
byte-identical functionals, both orders, all amplitudes); coupled-coin
unitarity at the tripled scale (norm ×9, both orders); circularity graph
from CONTRACT's 12-edge table — simple cycles are exactly {3-edge dynamical
loop, 4-edge actor-record circle, one 5-cycle}, head lengths 4 and 3
confirmed; W3 arithmetic 4 member-specific + 1 family-level (ceiling
exceptions 0 ⇒ family label earned by the computed rule); prereg witness
pairs (23/0, 0/2, 0/18, INFEASIBLE/8, 12/0) consistent with the rebuilt
measurements; stamps 215; head-fence weld: the paper's 5 fenced verdicts
byte-identical to output.txt's and to the receipt comparator's segments;
object-under-test digest in the receipt equals the actual paper sha256-12;
ledger head printed = receipt head = receipt recomputed
(`e448f3d941059c5a`); all 9 verbatim parent quotes the unit consumes were
located in the parents' own bytes by this seat (persistence row, unposed
question, packing rule (whitespace-canonicalised), coset conditional,
a = 2's 36, emission read point, alternative-order mechanism,
ensemble-side bookkeeping, grain tension).

**Total: ≈1,450 independent exact comparisons; 0 discrepancies surviving.**

---

## Discrepancies

**None surviving.** One transient, owned by this seat, disclosed for the
record: my first quick phase-1 solver kept no artificial columns, so
artificials could never re-enter the basis; it terminated prematurely on 16
round-fiber rows (5 E-BLOCK, 11 E-TRIPLE), reporting gaps strictly LARGER
than delivered (e.g. 40/27 vs 32/27). A sound full-tableau solver — and an
independent 16-row re-solve — reproduces the delivered values exactly at
all 16. The delivered instrument's simplex permits artificial re-entry and
is correct on every row I checked. The 4 committed-row gaps are also
confirmed by hand-derivation.

## Majors

None.

## Minors / observations (no false number in any of these)

1. **The observable sweep is structurally tautological, as the paper
   discloses.** `measure_obs_sweep` evaluates each observable once per probe
   on the SAME (geometry, record) arguments — the completion is not an
   input, so `value_set_size == 1` cannot fail. The paper says exactly this
   ("the sweep could not have read otherwise") and rests the certificate on
   the AST domain audit plus the modal-relation contrast (2 values —
   independently rebuilt). Adequately priced in-paper; no action required.
2. **`frozen_creation_admits_seam` is computed by an unsatisfiable filter**
   (`profile[0] > 0 and profile == (0,0,3)`). The published 0-of-288 is
   necessarily true (the frozen NONE rule admits only (0,0,3) profiles,
   which never span) and I verified it independently from the profile
   census; but the delivered expression is vacuous rather than a live
   measurement. Cosmetic.
3. **`evolves_across_creation` is assigned False, not computed by a
   predicate.** The paper prices this honestly (S-4: "the exclusion here is
   type-level, not a search") and the evidence it rests on (36/36
   directionless cross cells; coin family typed on 3-direction blocks) is
   measured and was rebuilt. Fine as disclosed; a successor wanting
   0-of-4 as a live census would need a typed predicate.
4. **The one Born accessor (`born_target`) is a code twin of face 1
   (`psi_ontic_q`), and their equality is by construction, not gated.**
   G-PSI-EQUAL binds the three faces to each other; the reach audit keeps
   consumers out of the face regions; but no gate compares the accessor's
   output with the faces'. Mathematically forced (same definition) and
   verified by this rebuild at every delivered row; noted as a weld a
   hostile future editor could exploit in a mutated tree.
5. **Fiber-feasible rows carry no polytope dimension** — the unit's own
   deviation #4, disclosed and priced; my rebuild confirms the word logic
   at those 6 rows (E-LINE-DECLARED comes back UNIQUE at both feasible
   rounds because its system has nullity 0 before the fiber branch).

## Seat summary

The OPERATOR seat rebuilt ECC's entire numeric surface from the four sealed
parents' committed definitions in independent code — chart, Born
functional, LP census, seam substrate, lattice, lawful/preparedness
censuses, two-step reading family, psi carriers, carrier/debt, interface
extents — roughly 1,450 exact comparisons, and found not one false number:
the committed row is INFEASIBLE at all four committed classes with qmax
4/9 and exact gaps 4, 4, 3, 7/3 (also derived by hand); the ceiling is a
correct theorem for the 0/1 incidence classes and its 156-row census has
zero exceptions; the census words split 136/8/6/6 with the MANY family at
dimension 8 and the deficient-writer collapse at exactly 57 implicit
zeroes; the a = 2 branch degenerates to the identity at 39/39; the
re-solved two-step fiber reproduces AUTOGLUE's sealed table exactly and
the persist members differ at 108/108 with all 324 per-crossing values
matching; the three psi carriers emit byte-identical functionals at all 18
rows; the carrier/debt numbers (4/4, 2/4, 0/4, 0/36, 0/288, 4/4) and all
18 computed interface extents reproduce. The five observations above are
disclosures the paper already carries or cosmetic formalization notes, none
touching a published value. The unit's defensible sentence survives this
seat's attack. Verdict: **ACCEPT**.
