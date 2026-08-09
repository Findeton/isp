# R1 — HOSTILE REVIEW, INSTRUMENT LENS (R3)

**Protocol:** `v14/note-r1-hostile-protocol.md` (`0647aeba4d9e`), K5 primary,
all kill-shots at instrument depth.  **Object:** the frozen R1 delivery,
hashes verified at the start and re-verified after all work:
paper `2c75772098eb`, code `7c04500ec178`, output `624ab5236ea1`,
receipt `2130abe58b9e` — **all four unchanged**; git working tree clean.
**Discipline:** scratch-only recomputation; nothing imported from the unit's
code; subprocess invocation of its CLI only; read-only git.

**GRADE: ACCEPT-WITH-FIXES.**

The delivered numbers are right.  A from-scratch re-implementation of the
atlas and the five invariants, written from the declared spec and importing
nothing, reproduces **every** cell of §4, §5, §7, §9, §10 and §11; the
paper↔output↔receipt sweep is **168/168 with zero false numbers**; all 60
anchors trace to the pinned bytes; the 47-mutant table is honest to the row;
two plain runs are byte-identical to the committed artifacts.  What fails is
not the measurement but its **protection**: three bug classes at the level of
the delivered claim survive a passing run, each demonstrated here with a
working exit-0 exploit.  All three repairs are definite and small.

---

## Execution counts

| | |
|---|---|
| top-level invocations of the unit's CLI | **79** |
| mutant subprocess invocations (spawned by 3 full delivery runs) | **141** |
| total process-level executions | **220** |
| independent 47-mutant falsifier audit (my own runs, untruncated) | **47** |
| crafted source injections (8 bug-class + 1 gate-ablation probe) | **9** |
| paper↔output↔receipt↔independent number checks | **168** |
| anchors traced (declared vs computed vs disk/pinned bytes) | **60** |
| scale-threshold cells recomputed from the extracted rule | **28** |
| arenas fully re-measured by independent code (A₁–A₅, L₁₀, L₁₂, W₅–W₇) | **10** |
| verdict rebuilds from the receipt alone | **1** (5 segments) |
| brute-force algebraic checks for forced-clause claims | **~20 000** |

---

# FINDINGS, most severe first

## M1 (MAJOR) — the two headline values are unprotected against any per-block-uniform corruption of the atlas

**The exploit.** A four-line edit inside `geometric_cells` that drops exactly
one coherent 2-cell **per block**:

```
     F, Fcoh = [], []
+    _skip = {}
     for k in sorted(bykey):
...
                 if cell_is_coherent(p1, p2, p3, n):
-                    Fcoh.append(key)
+                    if _skip.get(k):
+                        Fcoh.append(key)
+                    else:
+                        _skip[k] = True
```

**Measured outcome (INJ_A).** `exit 0`; **32/32 gates PASS, 0 FAIL; 60
anchors, 0 failures; 0 tracebacks**; and the emitted verdict becomes

> `R1-STABILIZES-AT-<NCOH_DENSITY=4/3;B2_DENSITY=19/36|…>`

against the delivered `37/27` / `20/37`.  The trajectory row moves at every
member (`NCOH_DENSITY 19/8, 9/10, 4/3, 4/3, 4/3`; `B2_DENSITY 64/95, 1/3,
19/36, 19/36, 19/36`), proving the corrupted path executed.  Nothing catches it.

**Why every comparator misses it.**

- **G16's "independent recount"** iterates over `faces_coh` — the list the
  construction *already filtered*.  It can only confirm that flagged cells are
  coherent; it structurally cannot detect a coherent cell wrongly **excluded**.
  This is #219's disease in its second direction.
- **G24** (per-block equality) passes because the corruption is per-block
  uniform: 36 coherent cells per block at A₃/A₄/A₅ alike.
- **G30** (L₁₀/L₁₂ robustness) reproduces the corrupted value for the same reason.
- **No anchor touches this unit's own atlas.**  G10 calibrates the homology
  *identities* against I3's published counts and explicitly states "nothing of
  I3's atlas is rebuilt here" — so the machinery is externally calibrated and
  the **atlas is not**.

**Repair (definite).** Two options, either sufficient, the first preferable:

1. Rebuild I3's own base atlas inside this instrument and anchor the rebuilt
   census against the pinned receipt's `V=36, E=5436, F=204384,
   F_coh=84720, b2=199123/79480`.  That converts G10 from an identity check
   into an external calibration of the construction itself.
2. Make the recount independent in the #219 sense: recompose the three drawn
   maps over **all** of `F`, count the coherent ones, and gate that count
   against `len(Fcoh)`.  Verified sufficient: under INJ_A this yields 222
   against `len(Fcoh)=216` and kills G16.

---

## M2 (MAJOR) — G22 is a substring-containment check, not a derivation; three qualifier corruptions survive

`derived_ok` asks only that each computed fragment **appears somewhere in**
the emitted string.  Three consequences, each measured with a passing run
(all: `exit 0`, 32/32 gates PASS, 60 anchors clean):

| id | corruption | emitted verdict segment | outcome |
|---|---|---|---|
| **INJ_B** | swap the two stabilised **values** between their names | `NCOH_DENSITY=20/37;B2_DENSITY=37/27` | **survives** — G22 checks `canon(stab[nm]) in verdict`, never *against its own name* |
| **INJ_C** | type the gateway segment | `R2-GATEWAY=A3` (computed gateway is A₁) | **survives** — G22 never inspects the gateway segment at all; G23 checks only the computed variable |
| **INJ_E** | append text to every divergence mode | `PHI:STRICTLY-DECREASING-AND-CONVERGENT`, … | **survives** — containment is satisfied by the prefix |

INJ_B is the sharpest: the paper's headline pair would be published swapped,
with a green receipt.  This is #234's own failure mode ("an ungated verdict is
a typo away from fiction") in the containment direction.

**Repair (definite).** G22 must **rebuild** the verdict string inside the gate
from the measured table and gate `rebuilt == verdict` (string equality), not
containment.  I confirmed the rebuild is exact: from the receipt alone, by the
unit's stated derivation, I reconstructed the verdict **byte-identically**,
all five segments derivable (see K5(b)).  Add one `verdict-string` mutant that
perturbs a single emitted character, so the equality clause has a falsifier.

---

## M3 (MAJOR) — the emitted trajectory table is not gated against the measured values

**The exploit (INJ_D).** One cell of `TABLES["trajectory"]["rows"]` is
rewritten (`PHI` at A₃ → `6/44`).  G20's completeness predicate reads the
**live** `rows` dict, never the emitted copy.

**Measured outcome at full delivery strength** — not a probe run: a complete
plain run, `exit 0`, **both artifacts written**, **33/33 gates pass including
G33** (all 47 declared mutants still die, `never_falsified` still EMPTY).
The delivered receipt then contains, simultaneously:

```
tables.trajectory.rows.PHI  = ['7/9', '1/4', '6/44', '3/25', '2/19']
gates.G15.value.A3          = {'PHI': '6/43', 'route_2': '6/43', ...}
gates.G23.value.phi.A3      = '6/43'
tables.measurements.A3.PHI  = '6/43'
G20.value cells_present/forced = 25 / 25   passed: True
```

Paper §7's table is rendered from exactly the corrupted object, so a false
number reaches the paper through a green receipt.

**Repair.** Evaluate G20's completeness **and a value-equality clause** on
`TABLES["trajectory"]["rows"]` itself, compared against `canon()` of the live
measurements.

---

## M4 (MEDIUM) — forced clauses inside a must-pass gate (#208), and the spectral "anchor chain" is one of them

G17's per-row predicate carries two clauses that are **true by algebra for
every input**:

- `eigenvalue_1_present` is `mu1 >= 1`, and `mu1` is the readout's cycle
  count.  Measured: over **all** permutations of every n ≤ 7 the minimum cycle
  count is 1.  Independently, G08 gates `Sigma[0] == 0`, so every readout
  fixes the basepoint and `mu1 ≥ 1` twice over.
- `degree_check`, i.e. Σ_d φ(d)·mult(Φ_d) = n, is a permutation identity:
  **0 violations over all permutations, n ≤ 7**.

#208: "analytically-forced clauses (true by algebra for every input) are
disclosures, not must-pass gates."  The measured consequence: the declared
`spec-anchor` mutant is killed **only** by the gate's calibration probe
(`spectral_anchor_chain(0) is False`), never by the data.  The paper's "I2's
eigenvalue-1 row rides along as an anchor at every readout of every member"
therefore records a forced fact about permutation matrices, not a measurement
of this substrate.

**Repair.** Move `eigenvalue_1_present` and `degree_check` into a disclosure
carrying their measured multiplicities; keep in the must-pass predicate only
the genuine two-route agreement (`mu1_cycles == mu1_kernel`, an
implementation comparator) and the calibration probe.

**Same class, at the verdict.** Given G24's own measured facts, the two
stabilisations are **algebraic, not independent observations**.  Measured
exactly, at every grown member and both robustness members:

| member | blocks b | 1-cells | coherent | b₂(N_coh) | per block |
|---|---|---|---|---|---|
| A₃ | 6 | 162 | 222 | 120 | 27 / 37 / 20 |
| A₄ | 7 | 189 | 259 | 140 | 27 / 37 / 20 |
| A₅ | 8 | 216 | 296 | 160 | 27 / 37 / 20 |
| L₁₀ | 10 | 270 | 370 | 200 | 27 / 37 / 20 |
| L₁₂ | 12 | 324 | 444 | 240 | 27 / 37 / 20 |

1-cells = 27b, coherent = 37b, b₂(N_coh) = 20b **exactly**, so
NCOH_DENSITY = 37b/27b and B2_DENSITY = 20b/37b are 37/27 and 20/37 for *any*
b.  Once G24 passes, both stabilisations are forced.  The genuinely measured
content is (i) that the blocks are isomorphic and (ii) that b₂ is additive
over the disjoint sum.  **This is the instrument's contribution to K1** and,
by #208, the forced part belongs in a disclosure rather than in the
stabilisation clause.

---

## M5 (MEDIUM) — the registered invariant's declared denominator is not the computed one

Pin §3.2 registers NCOH_DENSITY as "coherence classes **per drawn chart
pair**"; the code's own `DECL` glosses that as `|F(N_coh)|` over `|E(N)|`, and
`|E(N)|` is the **coordinate-resolved** 1-cell count (one per drawn pair *per
coordinate cell*), not the drawn chart-pair count (the overlap-graph edges).
Measured at every grown member:

| member | coherent | drawn chart pairs (overlap edges) | ratio | 1-cells \|E(N)\| | ratio |
|---|---|---|---|---|---|
| A₃ | 222 | 126 | **37/21** | 162 | **37/27** |
| A₄ | 259 | 147 | 37/21 | 189 | 37/27 |
| A₅ | 296 | 168 | 37/21 | 216 | 37/27 |

The stabilisation survives either reading (both are exactly constant on the
tail); only the **published value** differs.  This is a fidelity defect, not
a numerical error.  **Repair:** either state the denominator as the
coordinate-resolved 1-cell count in the pin's own words, or emit both
readings.  The paper's §5 formula and its prose currently disagree.

---

## M6 (MEDIUM) — the R0 hash literals are typed, contradicting the code's own provenance claim

`r0_rows()`'s docstring says the eight sha256-12 values are "read from
`v14/note-r0-founding-pin.md` itself."  They are **hard-coded literals**; the
pin file is only `sha12`'d (line 558) and never parsed — confirmed by grep,
no parse of the pin exists anywhere in the file.  The unit therefore verifies
*code literal == disk bytes*, not *pin table == disk bytes*.  That is exactly
the drift class LOG #4 records for the companions, and #24's rule is "counts
computed, never typed."

The byte-read itself is sound and I proved it: **INJ_H** rebuilt the whole v13
tree as real files with a single space appended to
`v13/code/ha_successor_receipt.json`; the run died `exit 1` naming
`A-R0-I7` and `G02`.  The hash check reads the bytes.

**Repair (cheap, definite).** Parse the seven-row table out of the pin's
markdown and gate that the parsed `(row, artifact, sha12)` set equals the
typed set — which is what the docstring already promises.

---

## M7 (MEDIUM) — two anchors have an analytically forced computed side

`A-LCB-A1-FIX` and `A-LCB-A2-FIX` compare I5's recorded `delta_fixed_points`
(= 1) against a recomputation of |{q : δ(q) = q}| with δ(q) = σ(q)⁻¹q.  But
δ(q) = q ⟺ σ(q) = 1 ⟺ q = 1, for **every** Σ.  Measured over all
14 976 (Σ, q) pairs in S₄ and S₅: distinct counts = **{1}**, non-identity
fixed points = **0**.  These anchors can therefore only ever test that the
pinned value is 1; they carry no information about A₁ or A₂ and should not be
counted as arena calibration.  (Not vacuous as inheritance checks — a drifted
receipt would still be caught.)

---

## M8 (MINOR) — typed counts inside disclosure and gate prose

`X-REAL-EMPTY`'s statement **string** types four ratios: "96 of 160 at A1 and
222 of 438, 259 of 511, 296 of 584 at the grown members."  They are correct as
delivered (verified against `tables.measurements`).  They are also literals:
under INJ_A the true counts became 95/160, 216/438, 252/511, 288/584 and the
disclosure text was **unchanged**, delivering four false numbers in a passing
run.  Paper §4 reproduces the same four literals.  Same class, lower stakes:
G27's claim text asserts "the coherent 2-cell count falls to zero" as prose,
while only the moved/fixed sets are in the predicate — the receipt does at
least carry `B2_DENSITY_is_undefined_after_the_scramble: true` as a value,
which is the right form.  **Repair:** build these statements from the measured
values.

---

## M9 (MINOR) — declared-falsifier coverage gaps, censused

- **R0 row I2 has no dedicated anchor mutant** (7 of the 8 rows do).
  `A-R0-I2` is never exercised.  The pin's "anchor-hash corruption for every
  I-row used" is met 7-of-8 by name.  (Cosmetic: I1 and I2 name the same
  artifact and the same hash.)
- **26 of the 60 anchors are never exercised by any declared mutant**: the 14
  `A-RSQ-EA/DV` threshold anchors, the 6 `A-LCB` rebuild anchors,
  `A-TB3-WINGS`, `A-TOP-COORD`, `A-R0-I2`, `A-R0-CHARTER`, `A-R0-PIN`,
  `A-R1-PIN`.  Exposure is bounded because anchors are exit-1-only, but the
  count should be in the receipt beside the gate census.
- **The pin's "verdict flips on … each qualifier" is not fully met.**
  Segment-by-segment: WINDOW has `qual-flip`; FUNCTORIALITY and R2-GATEWAY have
  falsifiers at the *computed* level only (G09, G23); the **DIVERGENT segment
  has none**; and no mutant exercises the emitted-string level of any segment.
  INJ_B/C/E measure the consequence.

---

## M10 (MINOR) — an atlas parameter is chosen, not derived

The S₃ element realising Σ on the growth family is hard-coded as the 3-cycle
`(1,2,0)`; the pinned rule text says only "S_3 acting on the F_2^3 factor."
Measured sensitivity at A₃/A₄/A₅ with my own implementation:

| choice | (NCOH_DENSITY, B2_DENSITY) on the tail | ord Σ | constant? |
|---|---|---|---|
| `(1,2,0)` — the unit's | **37/27, 20/37** | 3 | yes |
| `(2,0,1)` — other 3-cycle | 37/27, 20/37 | 3 | yes |
| `(0,2,1)` — a transposition | **45/31, 8/15** | 2 | yes |

In mitigation, §15's coordinate table **does** print Σ's order and cycle type
(3; {1,3}), which discriminates the transposition, and the two 3-cycles are
conjugate and agree.  The residual is that the rule text does not determine
the element and the unit's choice is consequential; it should be printed as
its own declared coordinate.  (Serves K4; that lens is R2's primary.)

---

# What I could not break — confirmations

- **The 47-mutant table is honest to the row.**  My own 47 independent runs:
  every mutant `exit 1`, **zero tracebacks**, every one reached the totals
  block, and the falsified gate/anchor sets match the receipt **exactly, 47/47,
  zero divergences**.  32/32 must-pass gates falsified; `never_falsified`
  EMPTY.  The receipt's own disclosure that G01/G02/G03/G31/G32 are falsified
  *only by waivers* is accurate and correctly separated from the computation
  denominator (27 of 32).
- **G33's self-exclusion is legitimate — and redundant.**  `must` is built
  *before* `gate("G33", …)` appends, so `GATES` holds only G01–G32 at that
  moment; and G33 cannot run inside a mutant process (`run_mutant_table` is
  guarded by `if not MUTANT`).  Denominator 32, totals 33, both stated in the
  paper.  No self-exemption.
- **The boundary-parity degenerate probe is a real death certificate.**  On the
  realised cells the OR/XOR rank delta is measured **0 at all five members**
  (31/31, 18/18, 102/102, 119/119, 136/136), so that clause alone has no
  teeth.  I ablated **only** `probe == probe_xor and probe_xor != probe_or`
  from G14 and re-ran the declared `parity-lax` mutant: it **survived, exit 0,
  zero failed gates**.  With the clause present it dies on G14.  The probe
  carries the entire kill — precisely what the 2026-08-09 addendum demands.
- **Cache-exercise gating is non-vacuous.**  INJ_G (stop counting lookups)
  kills G06.  `lookups > 0` is load-bearing; this is not zero-of-zero.
- **X-REAL-EMPTY is a disclosure, not a must-pass gate** — #208-compliant.
  Its content verified independently: at A₂ the REAL transport has order 10 on
  a Σ-saturation of exactly 7 labels `{1,2,3,4,5,8,12}` and draws 0 pairs at
  every block.
- **The scramble's UNDEFINED path is measured, not accidental.**  Shift 6
  recomputed independently from the receipt's own `DECL["controls"]`; 240
  drawn maps moved (independently reproduced); coherent 2-cells → 0; the b₂
  denominator vanishes and `None` is recorded; PHI, DIMENSION_PROFILE and
  SPECTRAL_PROFILE fixed.  The pin's declared split is exactly reproduced.
- **UNDEFINED-AT-A-MEMBER is derivable but not deliverable.**  INJ_F forced a
  `None` cell into the main family: the verdict string *did* compute
  `B2_DENSITY:UNDEFINED-AT-A-MEMBER`, and the run then died at G19/G20/G30,
  `exit 1`.  So the declared failure mode is reachable in the derivation and
  can never appear in a delivered artifact.  Scope note, not a defect — but the
  paper should say so.
- **Two-run byte-identity, reproduced.**  Two independent plain runs on the
  scratch copy both emit `624ab5236ea1` / `2130abe58b9e`, identical to the
  committed artifacts.  Further, the `--mutant __probe__` report is identical
  to the delivered `output.txt` except for the G33 block, the two totals lines
  and §9 — which validated the whole injection methodology.

---

# K1–K5 at instrument depth

**K1 — the copying question.**  The instrument *does* measure the mechanism
(G24), and that gate has teeth (killed by `arena-a2`, `arena-sigma`, `b0-lax`,
`blocks-lax`, `drawn-lax`).  But the measured per-block table (M4 above) shows
1-cells = 27b, coherent = 37b, b₂ = 20b **exactly**, so both stabilised
densities are algebraic consequences of facts the same run reports.  What is
measured is that the blocks are isomorphic and that b₂ is additive; what is
forced is the constancy.  By #208 the forced part is a disclosure.  I found
**no registered quantity that is not per-block-copied and stabilises** — the
three that are label-normalised all drift, exactly as the disjoint-sum
algebra predicts.  The instrument has no probe for "any other natural
quantity", so it cannot settle the sharpest form; that is the adjudicator's.

**K2 — family legitimacy.**  The trajectory table is independently recomputed
at every member and agrees in all 25 cells.  The K = 3 window covers exactly
A₃/A₄/A₅ — the homogeneous, functorially-connected tail — and restricting to
that tail changes nothing (37/27, 20/37 there, and again at L₁₀/L₁₂).  The
window qualifier is computed and correct, but **no computed qualifier states
that the window coincides with the functorial sub-chain**; the two facts sit
in different segments of the verdict and the reader must join them.

**K3 — invariant definitions.**  b₂ density is genuinely partial: handled by
measurement under the scramble, but not deliverable in the main family
(INJ_F).  The eigenvalue-1 chain is a **forced surrogate**, not a confirmation
of I2's wall (M4).  NCOH_DENSITY's denominator is not the pin's stated
quantity (M5).  The DIMENSION_PROFILE exclusion of the raw estimator **is**
honoured everywhere: the raw counts appear only inside the negative control
(`negative_control_estimators`), never in the trajectory table, and
`neg-lax` — which swaps them for the normalised ones — dies on G26.

**K4 — atlas-relativity.**  One alternative declared parameter measured
(M10): a transposition in place of the 3-cycle moves the stabilised pair to
45/31 and 8/15, still constant.  Within the declared conjugacy class the
values are stable, and §15's printed Σ order and cycle type do discriminate
the alternative — so §12's disclosure is *not* empty, but the parameter
itself should be printed as a coordinate.

**K5 — instrument.**  (a) Falsifier audit complete and clean: 47/47 reproduce
the receipt exactly; census gaps recorded in M9.  Injections: **8 bug-class
injections, 5 survive undetected** (M1, M2×3, M3), 3 die as designed.  (b)
Verdict rebuilt from the receipt alone, **byte-identical**, all five segments
derivable — which is precisely why G22 should gate equality rather than
containment.  (c) The 28 scale-threshold cells trace to `85f3cf809544` and to
my own recomputation of `L_m = 7m+1`, `m*(p) = min{m : 7m ≥ 6p}` (rank 6
derived from the receipt's first threshold row); the I6 width cross-anchor
traces to `c9bc956fe751` (system-triple dimension 8, wings 3, width 7,
L₁ = 8); the I5 rebuilds trace to `3e502f685ab3` (40 320 = 8!, 125 = 5³,
rank 3, p 5, n 16, Legendre exponents 3 and 1, arena rule 16/22).  The
`X-COMPANION-HASH` disclosure matches the LOG #4 erratum **exactly**:
recorded `07bea42728a2` / `4e4cd4f11bab`, measured `f80317a25037` /
`379194959fbc`, both re-confirmed against disk bytes.  (d) **Zero false
numbers**, 168/168.  (e) Two-run byte-identity reproduced.

---

# Verdict-segment falsifier map (for the adjudicator)

| segment | computed correctly? | protected by a declared falsifier? | survives a typo? |
|---|---|---|---|
| stabilised values | yes | head only (`verdict-flip`, `row-drop`) | **YES — INJ_B** |
| DIVERGENT modes | yes | **none** | **YES — INJ_E** |
| WINDOW | yes | `qual-flip` → G22, `k-window` → G21 | no |
| FUNCTORIALITY | yes | `embed-*`/`map-func` → G09 (computed level) | untested |
| R2-GATEWAY | yes | `gateway-lax` → G23 (computed level) | **YES — INJ_C** |

---

# Required fixes (ranked)

1. **M1** — externally calibrate the atlas (rebuild I3's base census and anchor
   it), or make the coherent recount range over all of `F`.
2. **M2** — G22 rebuilds the verdict string and gates **equality**; add a
   `verdict-string` mutant.
3. **M3** — gate `TABLES["trajectory"]["rows"]` for completeness *and* value
   equality against the live measurements.
4. **M4** — demote `eigenvalue_1_present` and `degree_check` to disclosures;
   state the forced part of the stabilisation as a disclosure per #208.
5. **M5** — reconcile NCOH_DENSITY's denominator with the pin's words, or emit
   both readings.
6. **M6** — parse the R0 table out of the pin and gate it against the typed set.
7. **M7–M10** — record the forced anchors, compute the disclosure prose, close
   the anchor-mutant census (add `anchor-I2`), print the Σ-element coordinate.

None of these impeaches a delivered number: I verified all 168 independently.
They are protection defects, and the unit's own standard is that a claim is
only as good as the falsifier that could have killed it.
