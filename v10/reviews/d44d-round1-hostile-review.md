# D44d round 1 — hostile review (independent rebuild + mutation battery)

**Reviewer:** hostile referee, round 1 (commissioned at LOG #350).
**Object:** `v10/code/d44d_slab_kappa_exact.py` (receipt, commit 0bd927c),
`v10/data/d44d_slab_kappa_exact.out`, pin + amendments
`v10/note-d44d-slab-smeared-theorem-kappa-m.md` (§1–3 pin, §4 A1–A6),
LOG #350. Ancestry consulted: d43a receipt/.out/note (frozen round),
v2 p1 §5/§7–9, root validator
`validate_minimal_interacting_gauge_matter_benchmark.py`.

## VERDICT: PASS-AS-RESCOPED

**0 BLOCKER / 1 MAJOR / 2 minor / 5 nit.**

All four headlines survived independent recomputation in EXACT rational
arithmetic (a from-scratch pipeline, zero floats, no recognition layer):
KG2's quartic is exact and holds even at six OFF-GRID masses; KG1's
composite-arm collapse, block-arm ((w+1)/2)^2 law, support lemma, wrap
exclusion, and A4/A5 amendments all verified exactly; KG3's
DIVERGENT/DIVERGENT reproduced exactly and shown collar-convention-robust.
The one MAJOR is interpretive: a g = 0 control (this reviewer's probe)
shows the KG3 divergence is **grain-inherited, not interaction-specific**
— the pin's "this decides whether free-core ray universality arrives at
the interacting fixture" oversells what the raw-bracket instrument can
decide, and the conversion note must carry the free baseline. No code or
number changes are required; the rescope is textual (conversion note +
LOG forward-note).

---

## Findings

### MAJOR-1 (interpretive rescope; KG3). The DIVERGENT verdict is real and convention-robust, but it is NOT an interacting-fixture discriminant: the same instrument returns DIVERGENT at g = 0.

- **What the receipt claims** (receipt lines 1097–1103; .out line 209;
  LOG #350 "KG3 — the interacting cross-check: DIVERGENT at both cells"):
  "at the raw singleton-bracket grain the free-core bracket-ray
  universality does NOT arrive at the interacting fixture". The pin §1
  KG3 frames the unit as "This decides whether the free-core ray
  universality even ARRIVES at the interacting fixture's grain."
- **What I verified:** my exact-rational rebuild (probe 3, conventions
  re-derived from the root validator, classification exact with NO
  tolerance) reproduces DIVERGENT at both cells under the receipt's A6
  collar, and the verdict is unchanged under two alternative reasonable
  collars: (V1) the validator's own bonds-only region split (all diagonal
  stays in B — the split the validator itself uses for its region
  checks), and (V2) the full-dependence collar (mass at n0 + ALL electric
  terms of index s >= n0 + incident bonds — the unique split under which
  B acts trivially on site n0, i.e. the true analogue of the free-core
  B_R property). The receipt's declared collar is a legitimate middle
  choice and the verdict is convention-robust. **The receipt's headline
  number is correct.**
- **The problem:** the same probe run at **g = 0** (interaction OFF, same
  fixture, same collar, same pairs) is ALSO DIVERGENT at both cells
  (per-N-sector non-proportional, exact). And the free Dirac core's own
  raw brackets were already DIVERGENT at d = 1, 2 (d43a T4, committed
  .out line 10). So the raw singleton-bracket grain carries no
  rule-proportionality even in free models; "universality" in this
  program is a property of the SMEARED tau/D identification (d43a
  T5/B4), which KG3 deliberately does not run. A DIVERGENT reading at
  the interacting point therefore cannot be attributed to the
  interaction, and the pinned instrument could never have measured the
  "arrival" of a property that its own grain does not carry in the free
  case. The receipt's scoping clause ("at the raw singleton-bracket
  grain"; "the smeared interacting identification remains the declared
  successor") is honest, but neither the pin, the receipt, nor LOG #350
  states the free baseline, and LOG #350's framing ("the interacting
  cross-check: DIVERGENT ... does NOT arrive at the interacting
  fixture") invites reading the divergence as an interacting-fixture
  fact.
- **Prescribed fix (textual only):** (i) the §5 conversion note and the
  LOG forward-note must state next to KG3: "the free-core raw brackets
  are themselves DIVERGENT (d43a T4, d = 1, 2), and a g = 0 control on
  this fixture is also DIVERGENT — the raw-bracket grain is not the
  universality-carrying object anywhere; KG3 confirms this persists at
  the interacting fixture rather than deciding an interaction question";
  (ii) the successor pin (smeared interacting identification) should
  include a g = 0 control column so the interaction's specific effect is
  isolable. Optionally adopt the g = 0 control into a repair rev of the
  receipt (cheap: same code path, one extra point).

### minor-1 (record honesty; KG2). The printed census says "scan order declared above" but the scan order is not in the printed record.

- Receipt line 793 prints "ansatz census (scan order declared above)";
  the actual order (x-poly deg 0–7, then m-poly deg 0–13, then x-rat,
  then m-rat by total degree with den deg 1–6 / num deg 0–6,
  >= 2x-overdetermination skip rule, first exact hit stops) lives only
  in a CODE comment (receipt lines 716–719). The .out (committed record)
  never states it; in the green run the census shows only
  "x-poly[0]: no; x-poly[1]: no; x-poly[2]: EXACT", so a reader of the
  .out cannot audit what would have been tried next or in what order —
  which is exactly what makes a first-hit-stops scan pre-registered
  rather than post-hoc.
- **Fix:** print the full scan-order declaration in the banner (or in
  the KG2 header) so the .out is self-contained. (My M8 mutant run shows
  the full census does print in the non-fit branch — 105 forms — so
  only the green-path declaration is missing.)

### minor-2 (gating epistemics; KG1). Pin §2 "each cell a gate" is not what the receipt implements, and the exit code alone cannot certify the KG1 headline.

- Pin §2: "SG1–SG3: KG1/KG2/KG3 as pinned above, each cell a gate." The
  receipt exit-gates per-cell EXTRACTION (ray shape, completeness slot,
  recognition — KG1-C, receipt lines 595–599) and the w = 1 anchors
  (KG1-A), but the CONSTANT values on w >= 2 cells feed only the
  non-exit-gating verdict lines (receipt lines 601–627). Mutation
  evidence: my M5 mutant (smear normalization dropped) passes **17/17
  PASS, exit 0**, with the damage visible only as `[KG1 THEOREM] ...
  FAILED at composite cells` plus 28 changed table lines. This IS the
  pre-registered discipline (banner lines 301–302; pin §1 "any
  w-dependence is a delivered finding, not a failure"), so it is a pin
  wording tension, not a receipt defect — but it means byte-diff of the
  .out against the committed record is LOAD-BEARING verification, not a
  nicety.
- **Fix:** forward-correct pin §2's sentence to "each cell an
  extraction gate; cell constants are delivered verdict content at
  exit 0 per §1", and record in the conversion note that the
  verification protocol for this unit is exit code + byte-identity
  (LOG #350 already practiced this; state it).

### nit-1. KG2 header "28 rational masses on (0, 2]" (receipt line 639) — the grid spans [1/16, 2]; the verdict line correctly claims only the hull. Reword the header to "[1/16, 2]".

### nit-2. KG3's verdict set adds BOTH-ZERO to the pin's four classes (receipt lines 1005, 1067). Harmless completion of the case analysis, declared only in the check label; A6 should have listed it.

### nit-3. EXC order-1 sub-onset is gated at KG3 (receipt line 996) but not at KG1 slab scope (KG1-B gates LT orders 1–3 only). Structurally trivial (Gamma has no order-1 term for real-diagonal H), so no exposure; note it in the conversion note or add the one-line gate on a repair pass.

### nit-4. `direct_bisect_64` (receipt lines 878–895): a kappa that is exactly 0 AT a grid point makes `ka * kb >= 0` skip that sign change entirely, and the `fm == 0` mid-point path delivers a width-0 bracket. Dead in the green run (my M8 mutant proves the branch otherwise live and clean); tighten if the fallback is ever promoted.

### nit-5. `recognize()` soundness margin is data-dependent: with cap 1e15 and gate 1e-30, two distinct in-cap rationals can in principle be ~1e-30 apart, so the gate is marginal only if true denominators approach the cap. Here the actual max denominator is 2.4e9 (SG4 census, .out line 203), leaving ~6 orders of margin, and my exact-arithmetic rebuild confirms every recognized rational is the true value — no exposure in this receipt. Consider printing the margin (cap x max_den vs 1/TOL) in SG4.

---

## Independent recomputation inventory

All probes are from-scratch implementations in EXACT complex-rational
arithmetic (`fractions.Fraction` pairs; zero floats anywhere; no
`limit_denominator`, no tolerance in any comparison — equality of
rationals only). Probe scripts in the session scratchpad
(`probe1_exact_kappa.py`, `probe2_slab.py`, `probe3_kg3.py`); conventions
taken from the d43a pin text and the root validator, not from the receipt.

### KG2 — the kappa(m) pipeline (probe 1): **CONFIRMED, strengthened**

| mass | my exact kappa_LT | = (9m^4-15m^2+4)/144? | EXC = 1? | note |
|---|---|---|---|---|
| 1/2 | 13/2304 | yes | yes | anchor |
| 1 | -1/72 | yes | yes | anchor |
| 1/3 | 11/648 | yes | yes | **off-grid** |
| 2/5 | 143/11250 | yes | yes | **off-grid** |
| 3/5 | -73/45000 | yes | yes | **off-grid** |
| 4/5 | -299/22500 | yes | yes | **off-grid** |
| 7/5 | 2867/45000 | yes | yes | **off-grid** |
| 9/5 | 15587/45000 | yes | yes | **off-grid** |
| 1/16 | 258313/9437184 | yes | yes | = receipt's recognized rational |
| 13/24 | 13777/5308416 | yes | yes | = receipt's recognized rational |
| 2 | 11/18 | yes | yes | = receipt's recognized rational |

Exact ray collapse D = kappa (I - sigma_x) at all 11 masses, both rules.
The quartic holds at six masses the receipt never touched (inside the
hull), so the identification is not an artifact of the 28-point grid; the
receipt's recognized rationals are the TRUE exact values (the
limit_denominator hazard is dead); and the solve/verify split is genuine
— I read the code path: `try_poly` solves a 3x3 exact-Fraction system on
`pts[:3]` (receipt lines 720–724) and verifies with `==` on all 28
(line 725), so 25 points are honest zero-tolerance verification, not fit
targets. Crossing brackets [9/16, 37/64] and [73/64, 37/32] re-derived by
hand from floor(64 sqrt(x)); `bracket_64`'s isqrt-of-floor is provably
floor(sqrt(y)) (no float enters). Quartic anchors re-derived by hand:
kappa(1/2) = (13/16)/144 = 13/2304, kappa(1) = -2/144 = -1/72,
kappa(2) = 88/144 = 11/18 — the d43a committed values.

### KG1 — slabs, support lemma, A2–A5 (probe 2): **CONFIRMED**

- (L=12, m=1/2, w=2), all four cells exact: COMPOSITE LT 13/2304,
  COMPOSITE EXC 1, BLOCK LT 13/2304, BLOCK EXC **9/4** (the
  ((w+1)/2)^2 law at w=2, as commissioned); slots exactly zero (empty
  commutator dicts, not small numbers).
- (L=16): COMPOSITE w=3 LT = 13/2304 (the clean twin of the excluded
  cell); BLOCK w=3 EXC = 4; BLOCK w=4 EXC = 25/4.
- **Support lemma (A3):** kernel site-supports computed exactly:
  singleton LT = [b-2, b+2], block w=2 LT = [b-2, b+3], singleton
  EXC = [b-1, b+1], block w=2 EXC = [b-1, b+2] — exactly the declared
  spans [b-2, b+w+1] / [b-1, b+w]; hence r_max = w+3 / w+1 (A2) is the
  exact commutator-support bound, and the census rule
  `wrapped iff r_max >= L - (w+3)` reduces to L=12, w in {3,4}, LT —
  exactly the 8 excluded cells.
- **The commissioned marginal cell** (w=2 LT at L=12: pair (0, r=5),
  kernels {10..3} and {3..8}, one spare site): recomputed at **L=18** —
  same 13/2304 exactly, both arms. No hidden wrap.
- **Wrap reproduction:** the excluded cell (L=12, m=1/2, w=3, COMPOSITE
  LT) reproduces the receipt's contaminated value **3229/278784 exactly**,
  with a NONZERO completeness slot — the wrap witness is real.
- **A5 (weight-family independence):** three alternative families at
  (L=16, w=3, m=1/2) — uniform (1/3,1/3,1/3), reversed-log
  (2/11,3/11,6/11), and (1/2,1/3,1/6) — all give c = 13/2304 exactly.
  The declared translation-covariance claim holds empirically.
- **A4 (ORD reduction):** at a SECOND cell (block w=2 LT, L=12), the
  Delta^4 coefficient at ORD=4 and ORD=8 is IDENTICAL entrywise in exact
  rationals (36 entries). Together with the receipt's own ORD-12-vs-4
  gate (KG1-T) and the structural argument (Cauchy lower-triangularity;
  Gamma(U_free) - I is O(Delta^2), so the Neumann sum I - N + N^2 is the
  exact inverse at ORD 4 — and the loop budget ORD//2+1 suffices), the
  truncation-exactness claim stands. My M3 mutant confirms the gate trips
  when the Neumann sum is genuinely short.
- **A1 (which arm carries the theorem):** read v2 p1 §7 directly
  (lines 325–348): the corpus slab observable is
  J[N] = exp(a sum_n N(an) log J_n) — built from SINGLETON maps under a
  lapse weight; at leading coefficient order (§8: log J_n =
  c Delta^2 A_n + remainder) this IS the phi-weighted
  singleton-coefficient sum, i.e. the COMPOSITE arm. A1's attachment of
  the theorem to COMPOSITE is correct; the BLOCK arm is the pin's
  literal-wording reading and its EXC law is properly a delivered
  finding. (Note §7's weights a N(an) are not sum-normalized; the
  receipt's sum(phi)=1 normalization is the right fixture-scale
  rendering and is immaterial by the now-probe-verified A5.)
- **Port fidelity (SG0-PF):** mechanically diffed the 18 shared
  machinery functions between d43a and d44d — all VERBATIM; the
  generalized `build_H_R` is gated against `build_H` in-receipt and my
  probes independently reproduce its block outputs.

### KG3 — interacting fixture (probe 3): **CONFIRMED at the number level; see MAJOR-1 for scope**

Fixture rebuilt from the validator's own formulas (`particle_basis`
MSB order, `reduced_diagonal_energy` mass/electric structure including
the vacuum electric offset, `-t` hop on occupation-differing bonds;
validator lines 142–176; committed point (m,g) = (7/10, 1/2), t = 1,
lambdas (9/10, -2/5, 11/10, 1/5) = validator lines 299–303). H exactly
real-symmetric; sub-onset orders vanish exactly; all four leading
coefficients exactly N-block-diagonal (matching KG3-B). Verdicts, exact
classification:

| collar split | d=1 | d=2 |
|---|---|---|
| V0 receipt's (A6: mass n0 + electric index n0 + incident bonds) | DIVERGENT | DIVERGENT |
| V1 validator-style (bonds only) | DIVERGENT | DIVERGENT |
| V2 full-dependence (electric s >= n0; B trivial on n0) | DIVERGENT | DIVERGENT |
| **V0 at g = 0 (control)** | **DIVERGENT** | **DIVERGENT** |

The receipt's verdict is exactly right and convention-robust; the g = 0
row is MAJOR-1's evidence that it is not interaction-specific.

### SG0 / determinism / hygiene

- Rerun 1 (repo root, PYTHONHASHSEED=0): exit 0, **byte-identical** to
  the committed .out. Rerun 2 (cwd = `v10/`, PYTHONHASHSEED=7): exit 0,
  **byte-identical** — cwd-robust (the receipt does no file I/O; grep
  confirms no `open(`, no `random`, no `time`).
- No `check(True)` or vacuous gates; the two count-style gates (KG1-C
  `len(cells) == 56`, KG3-C `len == 2`) are paired with content gates
  and declared as delivery counters.
- Banner float-entry enumeration is complete: series mpf (covers the
  fr2mp'd PHI weights), the recognition layer, the KG3 decimal
  constants; `math.isqrt`/`bracket_64` are pure-integer; remaining
  floats are presentation-layer only (dict keys 0.5/1.0 are exact
  binary).
- .out internally consistent with the code's prints; spot-checked
  kappa(5/8) = -1991/589824 against the quartic by hand; d43a REF_LT
  tables carried into d44d are identical to the committed d43a values.
- LOG #350 audit: 17/17, byte-identity claim, 9.3x overdetermination,
  "solved from 3 / verified on 25", 11/18 hand-check, hull discipline,
  wrap census, block-arm law — all match the artifacts. The KG3
  sentence inherits MAJOR-1's framing (forward-note prescribed); no
  numerical overstatement found anywhere in the row.

---

## Mutation table (8 mutants, receipt copied to scratchpad, one exact-string substitution each)

| # | mutation | expectation | result |
|---|---|---|---|
| M1 | KAPPA_REF 13/2304 -> 13/2303 | anchor gates trip | **exit 1**, 2 FAIL (T5, KG1-A). Note KG2-A holds its own inline 13/2304 literal — redundant anchoring, good. |
| M2 | D first moment `+ delta_*v` -> `- delta_*v` | tau/D construction gated | **exit 1**, 4 FAIL (T5, KG1-A, KG2-A, KG2-B) |
| M3 | Neumann loop `ORD//2+1` -> `ORD//2-1` | truncation gate trips | **exit 1**, 2 FAIL (KG1-T dev 0.375 vs 1e-40 gate; KG1-C) |
| M4 | KG3 hop made direction-dependent | Hermiticity gate real | **exit 1**, 1 FAIL (KG3-A, max dev 1.0) |
| M5 | smear normalization dropped (phi unnormalized) | per pre-registration: delivered, not exit-gated | **exit 0, 17/17 PASS**; `[KG1 THEOREM] FAILED at composite cells` + 28 table lines change (composite EXC -> H_w^2 values 9/4, 121/36, 625/144). LOUD in the .out, invisible to the exit code — minor-2's evidence. Not silent. |
| M6 | `wrapped()` -> always False | slot gate must catch the 8 wrap cells | **exit 1**, 1 FAIL (KG1-C: nonzero slots on the formerly-excluded cells — the support-lemma witness has teeth) |
| M7 | DEN_CAP 1e15 -> 1e3 | recognition gate real | **exit 1**, 4 FAIL (KG1-C, KG2-A, KG2-C, KG2-D) |
| M8 | one grid kappa corrupted (KTAB[5/8] denominator +1) | identification must demote, not lie | **exit 0, 17/17 PASS**; scan finds NO form (105-form census prints), KG2-D delivers the pre-registered non-fit branch with exact-bisection brackets (9/16, 37/64), (73/64, 37/32); KG2 VERDICT -> "no scanned form fits". Proves the fallback branch is LIVE, and that a single corrupted input demotes the claim rather than producing a false quartic. LOUD in the .out. |

**No silent-green mutant.** Every mutation either exits 1 or loudly
rewrites delivered verdict lines that byte-diff verification catches.
M5/M8 are the pre-registered exit-0 delivery paths behaving as declared.

---

## Reproduction appendix

```
cd /Users/felixrobles/workspace/isp
# receipt rerun (both byte-identical to v10/data/d44d_slab_kappa_exact.out, exit 0):
PYTHONHASHSEED=0 python3 v10/code/d44d_slab_kappa_exact.py > /tmp/r0.out
cd v10 && PYTHONHASHSEED=7 python3 code/d44d_slab_kappa_exact.py > /tmp/r7.out
# probes (session scratchpad): probe1_exact_kappa.py (exit 0, "ALL EXACT
# MATCHES"); probe2_slab.py (exit 0, "ALL OK"); probe3_kg3.py (verdict
# table as above); make_mutants.py + 8 mutant runs (exit codes as tabled).
# Probe runtimes: ~1-4 min each (exact Fraction arithmetic).
```

Environment: python 3.8.20, mpmath 1.3.0 (receipt); probes use stdlib
`fractions` only.

## What was attacked and held

- **KG2 exactness/circularity:** attacked by rebuilding the entire
  pipeline in exact rationals with no recognition layer, at 6 off-grid
  masses — the quartic held to the digit; the solve-3/verify-25 split is
  genuine; M8 shows the scan cannot be pushed into a false positive by a
  corrupted input.
- **KG1 theorem arm:** attacked via §7 source reading, three alternative
  weight families, an L=18 wrap trap on the tightest clean cell, exact
  slot audits, and exact reproduction of a contaminated cell — the
  composite-arm collapse and the exclusion lemma held everywhere.
- **A4 truncation:** attacked mechanically at a second cell at ORD 8 in
  exact arithmetic and by the M3 under-truncation mutant — exact.
- **KG3:** attacked as a possible collar artifact with two alternative
  splits — the verdict is robust; the surviving weakness is
  interpretive (MAJOR-1), not numerical.

---

# DELTA VERIFICATION (round-1 repairs, LOG #352, commit bce458e)

**Delta verdict: DELTA-CLEAN.** All findings discharged as applied; the
rescoped KG3 wording is accurate claim-by-claim; no new findings above
nit (none at nit either). The terminal condition is met from this
referee's side.

## Discharge audit

- **MAJOR-1 — DISCHARGED.** The new KG3 verdict line (receipt lines
  1112–1120; .out line 214) was audited claim-by-claim: (i)
  "divergence PERSISTS at the interacting point" — receipt cells +
  my round-1 exact reproduction; (ii) "the free core is ALSO divergent
  at this grain — d43a T2/T4" — verified against the committed d43a
  .out: T4 is DIVERGENT at exactly the KG3 cells d = 1, 2 (d = 3 is
  SUPPORT-MISMATCH, correctly not claimed), T2 DIVERGENT at d = 2, 3;
  (iii) "the round's g = 0 control on this fixture concurs" — I re-ran
  probe 3 at delta time: output identical to the frozen round's
  (DIVERGENT/DIVERGENT at g = 0, receipt collar, exact classification).
  I am comfortable with the record-citation: it is tagged as the
  round's control, the frozen round-1 body above documents the probe
  (collar, pairs, exact classification, reproduction appendix), and
  the attribution chain (receipt line -> pin §5 B1 -> this file)
  follows the d43a "cited to the report" precedent; (iv)
  "grain-inherited, not an interaction effect" follows from (ii)+(iii);
  (v) "RAY-level ... UNDECIDED ... successor with a g = 0 column"
  matches pin §5 B1. Pin §5 B1 owns the pin's oversold §1 clause by
  name; LOG #352 retires #350's KG3 sentence verbatim and states the
  corrected reading. This is the full prescription of MAJOR-1,
  including the successor g = 0 column.
- **minor-1 — DISCHARGED.** The scan order is now printed in the KG2
  section header (.out line 135), BEFORE the table and census, and I
  verified it against the implementation loop-by-loop: x-poly
  `range(0, 8)` = deg 0..7; m-poly `range(0, 14)` = deg 0..13;
  rationals `tot in range(1, 13)`, `dd in range(1, 7)`,
  `dn = tot - dd` with 0 <= dn <= 6 = den deg 1..6 / num deg 0..6 by
  total degree, x then m; the `NPTS >= 2*(#unknowns)` skip rule; first
  exact hit stops (each later family runs only `if hit is None`). The
  census's "(scan order declared above)" now has a true referent in
  the printed record.
- **minor-2 — DISCHARGED.** The banner statement (.out lines 9–12) was
  checked against the full 17-gate inventory: every exit gate falls
  under the enumerated anchors/extraction/recognition/collapse-form
  taxonomy (SG0-PF, AN1–AN4, T5, KG1-T/A/B/C, KG2-A/B/C/D,
  KG3-A/B/C), and the complementary claim — clean-cell collapse
  constants and verdict lines are delivered content whose integrity
  rides on SG5 byte-identity — is exactly the M5/M8 mutant behavior
  demonstrated in round 1. One taxonomy observation, no action needed:
  KG2-B's "EXC constant = 1 at every grid mass" is a constant gate,
  classifiable under "anchors" (the d43a mass-independent EXC anchor
  extended); the banner's error direction, if any, is conservative
  (understates what is exit-gated).
- **nit-1 — DISCHARGED.** KG2 header now "the hull [1/16, 2]".
- **nit-4 — DISCHARGED.** `direct_bisect_64` now delivers an exact
  grid-point root explicitly (receipt lines 892–896). The
  unreachability comment is TRUE: the identified quartic's roots
  m = 1/sqrt(3), 2/sqrt(3) are irrational while every grid mass is
  rational, so `KTAB.get(m) == 0` cannot fire for this receipt (and
  `None == 0` is False, so the guard is type-safe). The branch is dead
  in the green run — confirmed by byte-identity of the KG2-D region.
- **kg3_arrive removal — verified**: the variable's only use was the
  retired verdict sentence; no other reference existed.
- **B3 residual disposition — ACCEPTED.** BOTH-ZERO class listing,
  the structurally-trivial EXC order-1 slab-scope sub-onset gate, and
  the recognize() margin are recorded in pin §5 B3 as known residuals
  with no code change. All three were no-exposure nits in round 1;
  recording without code churn is the right disposition.

## Mechanical verification

- `git diff 0bd927c bce458e` on the d44d paths contains EXACTLY the
  enumerated repairs and nothing else: receipt = 4 hunks (banner
  insert; KG2 header + scan-order print; direct_bisect_64 guard; KG3
  verdict rewrite + kg3_arrive deletion — no arithmetic touched);
  .out = the three matching regions; pin = §5 B1–B3 appended (§1–4
  untouched); LOG = additive (#351 D44c is a different unit, touching
  no d44d path). This round-1 review body was committed BYTE-INTACT
  (316 lines, zero worktree-vs-bce458e diff above this delta section).
- Repaired receipt re-run twice at delta time: PYTHONHASHSEED=0 from
  repo root and PYTHONHASHSEED=7 from `v10/` — both exit 0, 17
  PASS / 0 FAIL, both BYTE-IDENTICAL to the committed
  `v10/data/d44d_slab_kappa_exact.out`.
- Probe 3 re-run: byte-identical to the round-1 output (g = 0 control
  stands).
- LOG #352's summary of the round (11 masses / 6 off-grid, 9 KG1
  cells, L=18 trap, 3 weight families, 18/18 verbatim port, 8 mutants
  0 silent-green, M5/M8 by-design) matches the frozen round-1 body;
  the forward-correction of #350 quotes and retires the exact
  sentence this round faulted.

## Terminal-statement check

The stamped conversion statement was audited against the artifacts:
the composite-arm slab-width independence (ray and constant), the
factorization (3m^2-1)(3m^2-4)/144 = (9m^4-15m^2+4)/144 with
crossings 1/sqrt(3), 2/sqrt(3) (the points where the LT tangential
coefficient vanishes), the hull scoping [1/16, 2], the block-arm EXC
((w+1)/2)^2 law, the grain-inherited reading with the g = 0
concurrence, and the undecided ray-level successor with its g = 0
column — every clause is supported by the receipt, the frozen round,
and this delta. No objection to conversion on this statement.

**DELTA-CLEAN — d44d may convert to TERMINAL.**
