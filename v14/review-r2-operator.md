# R2 — HOSTILE REVIEW, OPERATOR LENS

**Reviewer:** R1 (operator).  **Object:** the frozen R2 delivery — paper
`cc78e9373bbe`, code `36a10324b93f`, output `cb8493a13c39`, receipt
`7b128499b246` (commit c129ab5).  **Protocol:** `v14/note-r2-hostile-protocol.md`
(`3768846aebe9`), K1–K5 binding.  **Pin:** `v14/note-r2-manifold-pin.md`
(`76d42dfbc900`).  **Criterion/recipe source:** `v14/note-r1-adjudication.md`
(`4115dcd83cfa`) + `v14/note-r0-founding-pin.md` + the LOG #4 erratum.
**Anchors traced to source:** `v13/code/tb3_third_base_receipt.json`
(`c9bc956fe751`), `v13/code/top_topology_receipt.json` (`65bb1fc5231f`).
**All eight hashes verified before and after this run — unchanged.**

**Method (operator lens).**  A from-scratch instrument
(`scratchpad/r2op/{op,census,crosscheck,links,deep,k4}.py`): permutations as
dicts, group closure by product-set saturation, orbits by union–find,
components by BFS, GF(2) rank by set-elimination — every primitive different
from the unit's, **nothing imported from the unit**, the unit's code never
executed.  B and B₂ rebuilt from the I6 declarations read by JSON path; the
109-rule grid **derived** from the declared lattices (counts not copied); the
full 218-measurement census recomputed; a **third, analytic route** the unit
does not have (the coset-index/circulant formula of §1) run against all 218.

**Recomputations: 197,129** (op 121 · census 898 · crosscheck 3,056 · links
244 · deep 192,182 · k4 628; 605 of these are the anchor/grid recomputations
repeated once per run).  Includes the full 40,320-action R2-A sweep, 144,339
partition-rule measurements, a 6,895-configuration theorem sweep, and
**2,703 delivered numbers checked one by one against the receipt**.

**Headline standing.** *Every stored number in the delivery is correct.*
2,703/2,703 receipt values reproduce on an independent instrument; the class
table, all 14 census rows, all 14 b₁ values, all 80 link profiles, all 109×2
block-constant rows, the five REFUSES, the 14/14 B₂ rows, and every control
(positive 6/10, scramble 81/81, parity 90/78/4000, alt-draw 0/0) reproduce
exactly.  Eight of the verdict's nine segments rebuild **byte-for-byte** from
my own census.  What fails is not arithmetic: it is **which of those numbers
are measurements**, two false sentences in the paper's prose, and one segment
whose unit is misstated.

**Grade: ACCEPT-WITH-FIXES.**

---

## 1. K1 — THE CIRCULANT THEOREM (my decisive contribution)

The delivery's census is not an experimental result.  It is a corollary of
the grid declaration, and here is the corollary.

### Theorem R2-OP-1 (sliding-window drawn graph)

Let `T = ⟨γ⟩` have order *n* acting on labels *L*; let *R* be a **regular**
orbit (|R| = n).  Let *H* be the declared subgroup, its orbits ("cosets")
`c₀ … c_{k−1}` ordered by minimum label, and let `SLIDING` declare the *k*
cyclic windows `W_i = c_i ∪ … ∪ c_{i+c−1}` (indices mod *k*), `2 ≤ c ≤ k`.
Write `ι(x)` for the coset index of *x*, `S = ι(R) ⊆ Z_k`,
`w_i = |c_i ∩ R|`, and `d_k` for cyclic distance.

1. **Structure.**  The drawn graph on *R* is the lexicographic blow-up of the
   induced circulant `W = C_k(1,…,c−1)[S]` by cliques `K_{w_i}`:
   > `x ~ y  ⟺  d_k(ι(x), ι(y)) ≤ c − 1`   (distance 0 included).

   *Proof.*  By R2-A a pair is drawable iff both lie in *R*.  Two indices lie
   in a common window of *c* consecutive positions iff `d_k ≤ c−1`. ∎

2. **Connectivity.**  `W` is connected ⟺ **at most one** cyclic gap of *S*
   exceeds `c−1`.  (An edge crossing two large gaps would need an arc through
   one of them, of length > `c−1` either way.)

3. **Completeness threshold.**  A component is incomplete ⟺ it contains a
   pair at cyclic distance ≥ *c*.  If `W` is connected:
   > **LOCALITY  ⟺  c ≤ diam_k(S)**.

4. **Cycle rank.**
   `|E| = Σ_{i∈S} C(w_i,2) + Σ_{i<j∈S, d_k≤c−1} w_i w_j`, and on a connected
   component `b₁ = |E| − n + 1`.

5. **The other modes are theorems too.**  `ALL`: any two coset indices lie in
   a common *c*-subset (k ≥ c ≥ 2), so the drawn graph on *R* is `K_n` —
   clique-only, always.  `BLOCKWISE`: cells partition the cosets hence *L*, so
   the partition corollary applies — clique-only, always.  Orbit classes:
   likewise.

**Verification (mine, independent).**  Route-3 (the formula) agrees with the
cell-enumeration route at **218/218** measurements.  Criteria (2) and (3)
swept over every `(k, S, c)` with `3 ≤ k ≤ 9`: **6,895/6,895** for both.
R2-A itself: **40,320/40,320** actions, 0 counterexamples; the partition
corollary: **144,339** partition-rule measurements over all 40,320 actions,
**0** incomplete components (the unit swept the drawing relation only — my
sweep is strictly stronger).

### The 14 rows, derived not measured

| rule | k | S | w | c | diam | c ≤ diam | E (mine = measured) | b₁ (mine = measured) |
|---|---|---|---|---|---|---|---|---|
| R005/R030 | 8 | Z₈∖{0} | 1⁷ | 2 | 4 | ✔ | 6 = 6 | 0 = 0 |
| R008/R033 | 8 | Z₈∖{0} | 1⁷ | 3 | 4 | ✔ | 12 = 12 | 6 = 6 |
| R011/R036 | 8 | Z₈∖{0} | 1⁷ | 4 | 4 | ✔ | 18 = 18 | 12 = 12 |
| R048 | 7 | {1..6} | 2,1⁵ | 2 | 3 | ✔ | 7 = 7 | 1 = 1 |
| R051 | 7 | {1..6} | 2,1⁵ | 3 | 3 | ✔ | 14 = 14 | 8 = 8 |
| R063/R088 | 8 | {2,3,4,5} | 1⁴ | 2 | 3 | ✔ | 3 = 3 | 0 = 0 |
| R066/R091 | 8 | {2,3,4,5} | 1⁴ | 3 | 3 | ✔ | 5 = 5 | 2 = 2 |
| R106 | 7 | {1,2,3,4} | 1⁴ | 2 | 3 | ✔ | 3 = 3 | 0 = 0 |
| R109 | 7 | {1,2,3,4} | 1⁴ | 3 | 3 | ✔ | 5 = 5 | 2 = 2 |

**Closed forms.**  For `S = Z_k∖{pt}`, `w ≡ 1`, `c−1 < k/2`:
`|E| = (c−1)(k−2)`, `b₁ = (c−2)(k−2)` — at `k = 8`, **`b₁ = 6(c−2)` = 0, 6, 12**.
For *S* a contiguous arc of length *m*: `|E| = (c−1)m − C(c,2)`,
`b₁ = |E| − m + 1` — at `m = 4`, **0, 2**.  For T7's Σ-cosets:
**1, 8**.  The protocol's `(0,6,12; 1,8; 0,2)` are exactly these three
formulas' outputs.  All **30** SLIDING rules in the grid (local and non-local)
match the threshold prediction: **0 mismatches**.

**The two thresholds have different causes** — the paper reports one effect.
`c ≥ 5` at T7 because `diam(Z₈∖{0}) = ⌊k/2⌋ = 4`; `c ≥ 4` at T4 because *R* is
a contiguous **arc** of length 4 and `diam = m−1 = 3`.  As inequalities in
(n, c): a transport with a single non-regular label gives locality ⟺
`c ≤ ⌊(n+1)/2⌋`; a transport whose regular orbit is a label-contiguous arc
gives locality ⟺ `c ≤ n−1`.

**Local dimensions are a closed form too.**  Local dim at chart *X* in cell
*W* is `|R ∩ W| − 1` (the slice is complete), so the realised set is
`{|R ∩ W| − 1 : |R ∩ W| ≥ 2}` = `{c−2, c−1}∖{0}` for the trivial-H family:
`{1}`, `{1,2}`, `{2,3}` at c = 2,3,4 — the delivered
`LOCAL-DIMENSIONS=1+2+3` verbatim.

### K1 adjudication

(a) **PROVED** — non-completeness holds iff a stated inequality in the
declaration (`c ≤ diam_k(S)`, with the connectivity proviso), specialising to
`c ≤ ⌊(n+1)/2⌋` and `c ≤ n−1` for the two declared transports.
(b) **PROVED** — the measured b₁ values are the circulant formula's output at
14/14.
(c) **YES — the entire 14-of-109 census is derivable from the grid
declaration without running the atlas.**  Evaluating it needs only `ord(γ)`,
the orbit partitions of `⟨γ⟩` and *H*, the min-label coset order, and *c*.

**What remains measured** (state exactly this): the **grid** (its coordinate
list and size), the **drawing relation** (R2-A, itself a theorem, verified by
sweep), and the **values** of `E_N`, `F`, `F_coh` and the two densities.
**Which rules are local is FORCED**, and so are `MECHANISM`, the
`NONCOMPLETE-COMPONENT-SIZES`, `RULES-WITH-NONTRIVIAL-B1`, and
`LOCAL-DIMENSIONS`.  Per #208 the `RULES`, `MECHANISM`, `COMPONENTS` and the
`LOCAL-DIMENSIONS` part of `STANDARDS` reclassify from measured to forced,
with the forcing stated.  **The locality is not killed** — it is real at
exactly those 14 declared coordinates; its epistemic label changes from
*discovered by census* to *computed from the declaration*.

---

## 2. K2 — THE MOTIVATION QUESTION, ANSWERED WITH MEASUREMENTS

The protocol asks whether any of the 14 rules' cell structure is expressible
from I6's own declared objects without new choices.  I enumerated the
candidates and tested expressibility mechanically.

| test | result |
|---|---|
| cell family stabilised by the declared transport γ | **45 of 109 rules; 0 of the 14** |
| cell family stabilised by Σ | 68 of 109; 4 of the 14 (R048, R051, R106, R109 — **vacuous**: their cosets *are* the Σ-orbits, so Σ acts trivially on the coset set) |
| cross-tab (γ-stable × locality) | (T,T) **0** · (T,F) 45 · (F,T) **14** · (F,F) 50 |
| is the 8-label cyclic successor `i ↦ i+1 mod 8` (the map that *defines* SLIDING) in `⟨γ,Σ⟩`? | **NO at T7** (order 5040, fixes 0) and **NO at T4** (order 240) |
| can *any* permutation realise the min-label cyclic order on the Σ-cosets? | **NO** — the cosets have unequal sizes ({1,3} against six singletons), so no permutation cyclically permutes them |

**The measured statement.**  Every γ-stable atlas in the grid is clique-only;
every locality-bearing atlas is one the substrate's own transport does not
preserve.  The cyclic order that makes "sliding" meaningful is imported from
the **integer labelling**, not from `⟨γ,Σ⟩`, the ladder, the defect law or the
record layer — and for the Σ-coset rules it is not induced by any symmetry
whatever.  Locality here is produced by a mechanism chosen because it produces
locality (R2-A's recipe), whose key ingredient is a label artefact.  This is
the RSQ precedent exactly.

**Verdict wording (my ruling): `LOCALITY-DECLARABLE`.**  The honest claim is
an existence statement about atlas space — *the criterion is satisfiable, by a
construction with a closed-form threshold* — not a statement about the
substrate.  `LOCALITY-FOUND` is not earned and, on this evidence, cannot be
earned by any rule of this grid.

*Credit where due:* the paper's §10 already says "No claim that locality here
is substrate content… a declaration effect with a measured mechanism."  The
fix is to move that from the *does-not-claim* list into the **verdict head**,
where the reader meets it first.

---

## 3. K3 — THE STANDARDS, AND WHETHER A CONSISTENT DIMENSION IS REACHABLE

**Verified.** `LINK-CIRCLES = 1 of 80 charts`, the single circle at **R051
chart 4, link (5,5,1,1)** ✔.  `DIMREAD = INCONSISTENT` at 14/14 ✔ (12 rules
with every chart distinct; 6-of-7 at R048 and R051) ✔.  Local dimensions
{1}, {1,2}, {2,3} tracking c ✔.  Per-c link claims: c=3 "b₁ = 0 at five of six,
reaching 2 at R051" ✔; c=4 "connected, b₁ from 2 to 7" ✔.  **One false**: see
F6.

**Then three things the unit did not see.**

1. **The reading was computed on a filtered population.**  The unit evaluates
   `standards()` only at the 14 locality rules.  Run over all 109:
   **`CONSISTENT` is attained at 22 rules** (R001, R019, R022, R023, R026,
   R027, R044, R052, R056, R065, R071, R074, R077, R080, R082, R083, R085,
   R090, R096, R099, R102, R105) — every one an orbit-partition or
   `BLOCKWISE` rule — and **the intersection with the 14 is empty**.  The
   informative result is a **mutual-exclusion theorem**, not "INCONSISTENT at
   14/14".

2. **`INCONSISTENT` at a sliding rule is forced.**  `dimprofile[X]` is a
   vector indexed by **cell position**, so two charts have equal profiles only
   if they lie in exactly the same cells.  Under SLIDING that means the same
   coset — and then the drawn slice is a clique and there is no locality.
   > **Theorem R2-OP-2.**  In this grid class no `SLIDING` rule can read
   > `CONSISTENT` unless every chart-with-a-link lies in one coset, in which
   > case the component is complete.  Hence locality and `DIMREAD=CONSISTENT`
   > are mutually exclusive **for every (n, c) and every H**.

3. **The estimator is not relabelling-invariant, and I have the witness.**  I
   built a fixed-point-free transport (the 8-cycle) with trivial-H sliding.
   At c = 2,3,4 the drawn graph is the genuine circulant `C₈(1..c−1)`:
   non-complete, **vertex-transitive, every chart's star and link identical**
   ((2,0,2,0) / (4,3,1,0) / (6,12,1,7)).  The unit's estimator still returns
   **INCONSISTENT** — 8 distinct profiles over 8 charts — because only the
   cell **indexing** separates them.  Replace the cell-indexed vector by the
   **multiset** of local dimensions (same triple otherwise) and the probe
   reads **CONSISTENT** at c = 2,3,4, while all **14 grid rules still read
   INCONSISTENT** (2–5 distinct profiles).  The repair is therefore not a
   whitewash: it separates *forced by indexing* from *really inhomogeneous*.

**No positive control exists for this measure.**  `ported_standard_controls()`
computes Betti numbers and link profiles for the tetrahedron/torus/pinch
controls but never exercises `reading` or `dimprofile` — so the instrument
never demonstrates on any input that `CONSISTENT` is attainable at all.

### The successor requirement (concrete)

To **earn** a consistent dimension a rule must supply, together:
(i) a transport acting **regularly on the whole label set** (no fixed points,
no short orbits) so that `S = Z_k` and the atlas's cyclic symmetry acts
transitively on charts; and (ii) a **relabelling-invariant** reading (profiles
compared up to the atlas's own symmetry, e.g. the multiset form).
**Inside the declared grid: provably unreachable** — both declared transports
have non-regular labels (T7 fixes 0; T4 fixes 0 and 1 and carries the 2-orbit
{6,7}), so `S ⊊ Z_k` always and R2-OP-2 bites.  **Inside the grid *class*:
reachable**, and the 8-cycle probe is a worked example.  That is the exact
statement the successor should inherit.

---

## 4. K4 — SCOPE

- **The transport decision (T7 + T4) is sound and I endorse it.**  Transport
  is a declaration; a census true at one value only would be an artefact.
  Both are read from I6 by exact path and both verify
  (`witness_system_part` = (0,2,3,4,5,6,7,1), order 7;
  `lex_first_Q_per_order['4']` = (0,1,3,4,5,2,7,6) = (2 3 4 5)(6 7), order 4;
  Σ = (1 3)).  The strict T7-only sub-census is separable and I confirm it:
  **8 of 51**.
- **Σ-lattice scoping** (7 declared words + the whole group, minus the whole
  group for the ORBITS class ⇒ 7) is correct and reproduces.  Only `⟨e⟩`
  (order 1) and `⟨s⟩` (order 2) survive `c·|H| < 8`, giving 18 + 6 = 24 union
  rules at each transport — derived, matches.
- **The 5 REFUSES verify** and are exactly the atlases with no cell holding
  two labels of a regular orbit: R002, R021 (trivial cells at T7), R054, R079
  (trivial cells at T4), R081 (T4 Σ-orbits: the only 2-element cell is {1,3},
  and 1 ∉ the regular orbit {2,3,4,5}).
- **B₂ doubling verifies at 14/14** — and is **forced**.  I tested it
  structurally: the B₂ measurement is an **exact function of the B
  measurement at 109 of 109 rules** (component sizes = B's doubled plus the
  isolated basepoint; edges, `E_N`, `F` doubled; completeness identical).
  With transport **and** atlas declared block-locally, transports cannot cross
  blocks and cells cannot straddle, so "block addition copies locality" is a
  one-line theorem, not a measurement.
- **The cross-block falsifier the protocol asks for is absent — so I ran
  one.**  A straddling atlas on B₂ (sliding windows over all 17 labels, blocks
  allowed to interact through the cell structure) leaves the locality census
  untouched (still 2 non-complete components — regular orbits cannot cross
  blocks) but **moves the block constants**: at T7 per-incidence
  `5/18 → 5/17` (c=3) and `5/9 → 9/16` (c=4).  So the two clauses have
  different standings: *locality copies* is forced by the transport;
  *densities constant B→B₂* is forced by the **block-local atlas** and is
  falsifiable — the unit's 109-of-109 measures the declaration, not the
  substrate.
- **The coherence corollary is correctly classified.**  `F_coh = F_N` at all
  218 measurements ✔; the proof is right (a drawn pair forces `Stab(a) = 1` in
  `T`, and the composite lies in `T` and fixes *a*); the paper already enters
  it as a **disclosure** per #208 and the scramble control (81/81, both
  directions) shows the instrument is non-vacuous.  **This is the unit's
  cleanest piece of epistemic hygiene** — and the model the B₂/constants
  clauses should have followed.

---

## 5. K5 — VERDICT REBUILD FROM MY OWN CENSUS

I rebuilt the complete string from my independent census by the unit's stated
derivation.  **Eight of nine segments match byte-for-byte on the first
attempt** (`RULES`, `GRID`, `MECHANISM`, `COMPONENTS`, `STANDARDS`,
`B2-PERSISTENCE`, `REFUSES`, `BLOCK-CONSTANTS`).

**`NULL` does not.**  Mine: `G0-CLIQUE-ONLY-AT-2-OF-2;…-AT-19-OF-19`.
Emitted: `…AT-4-OF-4;…AT-38-OF-38`.  The emitted values are reproduced
**only** by counting rule×arena **measurements** (2 G0 rules × 2 arenas = 4;
19 orbit-partition rules × 2 = 38).  Substituting that semantics, the string
matches **byte-for-byte**.  See F7 — the paper states the wrong unit, and the
gate `G-R2A-NULL-CLIQUE-ONLY` asserts `len(g0) == 2 * len(transports)`, an
invariant that is right only by the coincidence *#arenas = #transports = 2*.

One structural observation on the verdict gate: `G-VERDICT-STRING-EQUALITY`
compares `build_verdict(payload)` against `build_verdict(payload)` — the same
pure function on the same dict.  It is a tautology except under the
`verdict-pair-swap` mutant.  The #10 engraving asks for a rebuild **from the
measured values**; a genuine rebuild would re-derive each segment from
`R["census_rows"]`/`R["standards"]` rather than from the pre-assembled
`payload`.  My rebuild above is that missing test, and it caught F7.

---

## 6. FINDINGS

### MAJOR

**F1 — The census is a theorem; four verdict segments are forced clauses.**
*Evidence:* §1 above — closed-form threshold `c ≤ diam_k(S)`, 218/218 analytic
agreement, 6,895/6,895 criterion sweep, 30/30 sliding-rule predictions, closed
forms for `|E|` and `b₁` at 14/14, and `LOCAL-DIMENSIONS = {c−2,c−1}∖{0}`.
*Repair (definite):* enter Theorem R2-OP-1 (or the worker's own derivation of
it) in the paper as §3.4; reclassify `RULES`, `MECHANISM`, `COMPONENTS` and
the `LOCAL-DIMENSIONS` component of `STANDARDS` as **forced**, with the
forcing stated per #208; keep the numbers.  State in the verdict derivation
that what is measured is *the grid and the drawing relation*, and that *which
rules are local is computed from the declaration*.

**F2 — `DIMREAD=INCONSISTENT` is forced, filtered, and over-read.**
*Evidence:* Theorem R2-OP-2; `CONSISTENT` attained at **22 of 109** rules,
intersection with the 14 **empty**; the 8-cycle probe is vertex-transitive
with identical links at every chart and still reads INCONSISTENT; under a
multiset (relabelling-invariant) reading the probe reads CONSISTENT while all
14 still read INCONSISTENT; `ported_standard_controls()` never exercises
`reading`, so the measure has **no positive control**.
*Repair (definite):* run `standards()` at **all 109 rules** and report the
mutual-exclusion result (22 CONSISTENT / 14 local / intersection ∅); mark
`DIMREAD` forced-at-sliding with R2-OP-2 stated; add a positive control that
returns CONSISTENT (the 8-cycle probe, or a single-cell arena); soften §9.3
and §11 from "width-based overlap will not do it" to "the estimator as
defined cannot return CONSISTENT at any sliding rule — the successor
requirement is (i) a fixed-point-free transport and (ii) a
relabelling-invariant reading."

**F3 — `LOCALITY-DECLARABLE`, measured; the verdict head should say so.**
*Evidence:* §2 — 0 of 14 locality rules is γ-stable; all 45 γ-stable atlases
are clique-only; the SLIDING successor is in neither `⟨γ,Σ⟩`; no permutation
realises the Σ-coset order.
*Repair (definite):* rename the head
`R2-LOCALITY-DECLARABLE-AT<…>` and add a computed segment
`EXPRESSIBILITY=GAMMA-STABLE-AT-0-OF-14;GAMMA-STABLE-ATLASES-CLIQUE-ONLY-AT-45-OF-45;SLIDING-ORDER-NOT-IN-<G,SIGMA>`,
derived in-gate and flippable.

**F4 — `B2-PERSISTENCE` and `BLOCK-CONSTANTS` are forced by the block-local
declaration, and the falsifier is missing.**
*Evidence:* B₂ = exact function of B at **109/109**; my straddling control
moves the per-incidence density (`5/18 → 5/17`, `5/9 → 9/16` at T7) while
leaving the census fixed.
*Repair (definite):* demote both segments to disclosures with the forcing
stated (this is the R1 adjudication's own order R-R1-3 applied to R2); ship
the straddling atlas as a **negative control** showing what the block-local
declaration is buying; restate §9 findings 4 and 6 as consequences of the
declaration, not discoveries.

### MODERATE

**F5 — FALSE NUMBER: the per-incidence span.**  Paper §6.1 fact 2: "The
per-incidence density runs from 0/1 to 25/18 across the grid."  Measured
range: **0 to 5/3**, attained at **R001 and R022**, and printed in the
paper's own §6.1 table (R001 row = 5/3) and in output §8.  25/18 is the
maximum over the *union* classes only (R018/R020/R043/R045).  No span is
computed anywhere in the instrument — the number is hand-typed prose and
ungated.  *Repair:* compute the span in-gate and print it; the sentence
becomes "runs from 0 to 5/3 across the grid (0 to 25/18 within the union
classes)".

**F6 — FALSE NUMBER: R048's link edges.**  Paper §5: "at c=2 every link is
edgeless except at R048, where **two** charts carry one link edge apiece."
Measured: **three** charts do — 1: (2,1,1,0), 2: (3,1,2,0), 3: (2,1,1,0).
R048 has exactly one 2-cell ({1,2,3}), which necessarily contributes one link
edge at each of its three vertices.  Two charts share the *profile* (2,1,1,0);
three carry an edge.  *Repair:* "three charts carry one link edge apiece (two
of them with the same profile)".

**F7 — The `NULL` segment's unit is unstated and the paper states it wrong.**
`4-OF-4` and `38-OF-38` count **rule×arena measurements**; the paper §3.2
calls them "rules" — but the grid has **2** G0 rules (the paper's own §4 table
says so) and **19** orbit-partition rules.  Every other `N-OF-M` in the
verdict counts rules, so the string is internally inconsistent in its units.
*Repair (definite):* emit
`G0-CLIQUE-ONLY-AT-2-OF-2-RULES(4-OF-4-MEASUREMENTS);ORBIT-PARTITION-CLASSES-CLIQUE-ONLY-AT-19-OF-19-RULES(38-OF-38-MEASUREMENTS)`;
fix §3.2's two sentences; replace the gate's `len(g0) == 2*len(transports)`
with `len(g0) == n_G0_rules * n_arenas`.

**F8 — The headline count is inflated by structural duplication.**  The 109
declared coordinates carry only **66 distinct (transport, cell-family)
structures**: 39 duplicate groups, 43 rules that are exact repeats of another
rule at the same transport.  The G3 lattice's `⟨e⟩` reproduces the cyclic
lattice's trivial subgroup wholesale (R005≡R030, R008≡R033, R011≡R036,
R063≡R088, R066≡R091), so **the 14 locality rules are 9 distinct atlases**;
`⟨g⟩`'s G3-ORBITS rule reproduces G0 (R001≡R022, R052≡R080); at c=7,
`SLIDING ≡ ALL` (the unit's own `mode_probe` records this at 4 coordinates).
`G-GRID-NO-DUPLICATES` checks **coordinate** uniqueness only.  The unit uses
the duplication deliberately as a cross-check (`G-LATTICE-CROSSCHECK`) but
never censuses its effect on the headline.  *Repair:* census distinct cell
families and print both figures — "14 of 109 declared coordinates = **9 of 66
distinct atlases**"; carry the distinct-structure count as a grid coordinate.

### MINOR

**F9 — The `c·|H| < block size` filter is a proxy that does not express its
stated purpose.**  For `H = ⟨Σ⟩` (order 2, orbits of sizes 2,1,1,1,1,1,1) it
truncates *c* at 3 although *c* ≤ 6 still gives proper subsets of the block.
Consequence: the Σ-family's own width threshold is never exercised inside the
grid.  By R2-OP-1 it is `c ≥ 4 ⇒ complete` (diam = 3 at both transports) — the
missing rows are predictable, and the paper's width-effect sentence is
correctly scoped to the trivial-subgroup family, so nothing false follows.
*Repair:* state the filter as a declaration with its rationale, and print the
predicted Σ-family threshold as a disclosure.

**F10 — Vacuous dedup.**  In `measure_rule`, the "deduplicate to geometric
edge-triples (I3's convention)" step cannot fire: `itertools.combinations`
already yields each triple once per cell, and the dedup key includes the cell
index.  Dead code with a misleading comment.

**F11 — A dimensionally confused gate.**  `G-R2A-NULL-CLIQUE-ONLY` gates
`len(g0) == 2 * len(transports)`, comparing a measurement count against a
transport count; it passes only because #arenas = #transports = 2 here, and
would misfire on a third arena.

**F12 — The symmetry self-test is a covariance check, not an invariance
check.**  It conjugates the transport **and transports the cells with it**, so
it cannot detect F3's finding that the cell families are not γ-stable.  Sound
as far as it goes; the paper should say which of the two it is.

### NOTE

- **N1.** All 2,703 delivered numbers reproduce; **zero false numbers in the
  receipt**.  Every error found is in the paper's **prose** (F5, F6, F7),
  which is the one surface not rendered from the gated object — the #13
  engraving covers rendered table cells, not sentences.  Worth an addendum.
- **N2.** My grid enumeration derived the counts (T7 1+1+18+7+24 = 51; T4
  1+2+24+7+24 = 58; by class 2/3/42/14/48) and **predicted all fourteen rule
  IDs from the declaration before measuring anything** — independent
  corroboration of F1.
- **N3.** I did not execute the unit's code (single-file-write discipline plus
  the concurrent R1 repair worker); byte-identity stands on the adjudicator's
  #13 verification.
- **N4.** Credit: the drawing relation is computed by two genuinely
  independent routes at every rule and arena (218), REFUSES is recorded rather
  than skipped, the UNDEFINED path is live at 28 rules, both denominator
  conventions are printed, the coherence corollary is entered as a disclosure
  with a non-vacuous scramble control, and the alt-drawing-group reading is
  disclosed rather than left implicit.  This unit's discipline is visibly
  ahead of R1's at delivery.

---

## 7. GRADE

**ACCEPT-WITH-FIXES.**

No head flips: locality *is* present at exactly the 14 declared coordinates,
the recipe *did* work, the null *is* clean, and every stored number survives
an independent from-scratch instrument (2,703/2,703).  What must change is the
**epistemic layer**: the census is a corollary of the declaration (F1), the
dimension reading is forced and was measured on a filtered population (F2),
the locality is declarable rather than found and the head should say so (F3),
and two segments are forced by the block-local declaration (F4) — plus two
false prose numbers (F5, F6), one mislabelled unit (F7), and an inflated
headline denominator (F8).

Re-verified after this run, unchanged: paper `cc78e9373bbe`, code
`36a10324b93f`, output `cb8493a13c39`, receipt `7b128499b246`; anchors
`c9bc956fe751`, `65bb1fc5231f`; protocol `3768846aebe9`; pin `76d42dfbc900`.

**Single repo file written: `v14/review-r2-operator.md`.  Nothing else in the
repository was created, modified, or executed.**
