# D45a round 1 — hostile review (independent symbolic rebuild + out-of-hull battery + 10 mutants)

**Reviewer:** hostile referee, round 1 (commissioned at LOG #357).
**Object:** `v10/code/d45a_symbolic_kappa_exact.py` (receipt, commit fd91814),
`v10/data/d45a_symbolic_kappa_exact.out`, pin + amendments
`v10/note-d45a-symbolic-m-kappa-closure.md` (§1–4 pin, §5 A1–A2), LOG #357.
Ancestry consulted: `v10/code/d44d_slab_kappa_exact.py` +
`v10/data/d44d_slab_kappa_exact.out` (TERMINAL #353),
`v10/reviews/d44d-round1-hostile-review.md` (frozen round + delta),
`v10/code/d43a_lie_trotter_exact.py`, `v10/note-d44d-slab-smeared-theorem-kappa-m.md`
(the cited A5 note verified present, lines 101–104), git history
(pin pre-registration checked at 2f1a3cc).

## VERDICT: PASS-AS-RESCOPED

**0 BLOCKER / 1 MAJOR / 2 minor / 4 nit.**

All four headlines survived an independent from-scratch SYMBOLIC rebuild
(sympy Gaussian-rational engine, my own collar construction, full 5-term
Neumann sum with a product-equals-identity gate the receipt lacks): the tau
channel polynomials, both D collapses, kappa(m) = (9m^4 − 15m^2 + 4)/144 =
(3m^2 − 1)(3m^2 − 4)/144 as the zero-difference polynomial, the YG3-C
factorization algebra, completeness, sub-onset, realness, and delta-oddness
all reproduce identically in m. The all-m claim's untested territory was
attacked directly: at eight fresh masses — six far ABOVE the d44d hull
(m = 3, 7/2, 5, 8/3, 23/8, 9), one BELOW it (1/32), and one NEGATIVE
(m = −1) — both my exact rebuild and the COMMITTED d44d numeric pipeline
(its own source, exec'd unmodified) match the quartic and every channel
polynomial exactly. Ten mutants, all exit 1, zero silent-green. Reruns
byte-identical under seeds 0/7/unseeded from repo root and from `v10/`.

The one MAJOR is gate accounting, not mathematics: YG4-B is a hardcoded
`check(..., True)` — the "GREEN 20/20" ledger contains one PASS that no
computation feeds and that could not have failed under any circumstances.
Its content claims are all TRUE (each verified externally by this round),
so the rescope is record-level: the headline count must be read as 19
computed gates + 1 declared-protocol line, and the receipt or the
conversion note must say so (or the gate must be made self-verifying on a
repair rev). No number anywhere in the unit is wrong.

---

## Findings

### MAJOR-1 (gate accounting / record integrity). YG4-B is a synthetic PASS: `check(..., True)` — one of the headline 20 gates is unfalsifiable by construction.

- **Where:** receipt lines 868–872 — the second argument is the literal
  `True`. The label asserts (i) every gate above is exact polynomial-pair
  equality, (ii) "no TOL constant exists in this receipt", (iii) no
  RNG/wall-clock/environment reads, sorted prints, and (iv) "rerun
  byte-identical (verified externally with PYTHONHASHSEED 0 and 7)".
- **Why it matters:** the PASS/FAIL ledger is this campaign's currency
  (".out SUMMARY 20 PASS / 0 FAIL"; LOG #357 headline "GREEN 20/20"). A
  gate that prints `[PASS]` regardless of the world inflates the count: if
  a rerun were NOT byte-identical, or if someone later added a TOL
  constant above it, YG4-B would still stamp PASS. The d44d round-1 review
  explicitly recorded "No check(True) or vacuous gates" as a hygiene
  criterion for this line of receipts, and the d44c round (F1, LOG #354)
  established that exit/ledger accounting defects are round-grade findings
  even when every underlying number is true. That is the situation here.
- **What I verified (all four content claims are true):** (i) confirmed by
  reading all 20 gates — every comparison is `==` on Fraction tuples /
  dicts, no tolerance anywhere; (ii) grep: the string TOL occurs ONLY
  inside YG4-B's own label (receipt line 869); (iii) grep: no
  `random`/`time`/`os.environ`/`open(` anywhere; all printed iterations
  sorted (verified at every print site); (iv) three reruns —
  PYTHONHASHSEED=0 from repo root, PYTHONHASHSEED=7 from `v10/`, and
  unseeded — all exit 0 and BYTE-IDENTICAL to the committed .out (~0.5 s
  each, matching LOG #357's runtime claim).
- **Prescribed fix (either, cheap):** (a) make the gate self-verifying:
  read `__file__`, assert the source contains no `TOL` token and no
  float-literal pattern outside docstrings, keep the mpmath check (already
  real in YG4-A), and move the external byte-identity claim into the
  banner as declared-protocol text (the d44d minor-2 precedent: byte-diff
  is the round's job, not a self-award); or (b) leave the code frozen and
  forward-correct the record: conversion note + LOG state "19 computed
  gates + 1 declared external-protocol line; byte-identity verified by
  the builder pre-commit (#357) and by round 1". Do not re-headline
  "20/20" without one of these.

### minor-1 (unsound printed inference; YG3). "disc not a perfect square ⇒ irreducible over Q" is invalid for the quartic in m as printed; the claim happens to be true here.

- **Where:** .out lines 117–120 (factor_report on tau(±2, same)); receipt
  lines 738–740 and 753–754 (the printing branches); the YG3 VERDICT
  (.out line 151, receipt lines 887–890: "tau(2) = (36m^4 − 60m^2 +
  7)/2304 IRREDUCIBLE over Q"); pin §5 A2 (note lines 89–91); LOG #357
  ("tau(2,s) irreducible over Q").
- **The gap:** a non-square discriminant of the quadratic IN x proves
  irreducibility of the x-polynomial only. For the quartic in m the
  inference is invalid in general: m^4 + 4 = (m^2 − 2m + 2)(m^2 + 2m + 2)
  over Q while its x-form x^2 + 4 has non-square discriminant −16 —
  `factor_report` fed that polynomial would print "irreducible over Q"
  falsely. The receipt's verdict-level claim is about the m-quartic and is
  therefore not established by the printed route.
- **What I verified:** the claim is TRUE for this input — sympy
  `factor_list(36*m**4 - 60*m**2 + 7)` returns it irreducible over Q, and
  by hand the only other biquadratic factorization pattern
  (am^2 + bm + c)(am^2 − bm + c) requires 36·7 = 252 to be a rational
  square, which it is not; there are no rational m-roots since both
  x-roots are irrational. So: true claim, unsound printed justification,
  gated nowhere (YG3-C gates expansions and recombinations only —
  correctly).
- **Prescribed fix:** either scope the print and the verdict to
  "irreducible over Q as a quadratic in x = m^2" (one wording change,
  fully supported by the disc route), or add the even-quartic
  second-pattern check (252 non-square — one integer test) /
  a CAS-grade factorization gate on a repair rev. Same wording fix in the
  pin §5 A2 sentence at conversion time.

### minor-2 (ungated precondition; the Neumann layer). The 3-term budget's sufficiency rests on the Δ^1-freeness of N, which is never gated; Gfi·Γ == I is never checked; mutation shows a broken free inverse leaves kappa(m) EXACTLY unchanged and is caught by ONE gate only.

- **Where:** receipt lines 196–217. The in-function assert (lines
  208–209) gates the Δ^0 precondition only. `range(ORD // 2 + 1)` (line
  213) = 3 iterations is complete at ORD 4 iff N = Γ(U_free) − I starts
  at Δ^2; the Δ^1 vanishing (true structurally: H diagonal real ⇒ no Δ^1
  cross term; off-diagonals of |U|^2 start at Δ^2) is nowhere asserted,
  and the inverse is never verified as an inverse.
- **Mutation evidence (M5):** cutting the budget to one term (out = I − N,
  wrong at Δ^4) leaves the DERIVED kappa(m) exactly the correct quartic —
  YG0, YG1-A/B/C/D, YG2-A/B/C/D, YG3-A/B/C all PASS (19/20); the defect
  enters A(0) and A(r) as the same site-independent Δ^4 shift and cancels
  channel-by-channel in the tau/D assembly. The ONLY failing gate is
  YG2-E (LT completeness slot: 172 nonzero entries), exit 1. Not silent —
  but a single gate is the entire margin between that defect class and a
  green receipt.
- **What I verified:** my rebuild asserts BOTH preconditions (Δ^0 and Δ^1
  of N zero — both hold) and gates `Γ · Γ^{-1} == I` as truncated series
  (holds, all entries); so the receipt's inverse is correct as committed.
- **Prescribed fix:** two one-liners on a repair rev: extend the assert
  to `t[1]` (Δ^1-freeness), and add a PIPE-3 gate
  `m_mul_sym(Gam_free, Gfi) == identity-series`. Record in the conversion
  note that YG2-E is load-bearing for free-inverse defects (this round's
  M5).

### nit-1. YG4-A's "a recursive type walk over every retained object" overstates the walk set.

`U_free` and `Gam_free` are retained at module scope but not walked
(receipt lines 856–861 walk H, tau tables, D matrices, kappa, target,
JCACHE, Gfi — exactly the parenthetical's list, which is accurate).
Coverage is transitively effective — a float in Γ would propagate into
the walked Gfi/tau/D through Fraction-float contagion — and the walk's
counts reproduce (0 floats / 1590 Fractions; LOG's "1,590" matches). Say
"every retained load-bearing object (list)" or add the two structures.

### nit-2. YG3-A's label "reassembled independently from the printed channel polynomials" — the reassembly reads the same in-memory tau objects, not the printed record.

Receipt lines 766–784: `same_terms`/`flip_comb` are recombined from
`tauL` itself and compared to `DL` built from the same `tauL` by
`tau_D_pairs_sym`. This verifies the delta-weighted-assembly arithmetic
(a real check), not an independent source. This round's rebuild performs
the genuinely independent version (it agrees). Reword on conversion.

### nit-3. YG2-B's realness loop covers sites `range(5)` for both rules; LT site 5 (used by YG2-E's slot) is not realness-checked.

Receipt lines 597–600. No exposure: `slotL5 == {}` is gated (an entry
with a nonzero imaginary polynomial would make the slot nonempty), and
site 5's J feeds nothing else. One-character widen if ever touched.

### nit-4. The banner's "an m-dependent division would raise TypeError" is asserted, not demonstrated; the YG3 helper machinery contains branches dead for every input in this receipt.

Claim verified by this round: `Fraction / tuple` raises TypeError, and
the polynomial layer defines no division (receipt lines 84–125 — audit
confirms pin §5 A1: the only divisions anywhere are `cre / fact`,
`cim / fact` (Fraction/int, line 294) and integer-argument Fraction
constructions in the YG3 helpers; `p_scale` by Fr constants is
multiplication). `strip_rational_roots` (lines 676–701) and the
degree->3 residual branches of `factor_report` never execute for these
inputs — harmless delivered-print helpers, but untested code adjacent to
gated prints. No action required; noted for any future reuse (minor-1's
fix touches this function anyway).

---

## Independent recomputation inventory

Probe scripts in the session scratchpad
(`indep_sympy.py`, `committed_pipeline_fresh.py`, `make_mutants.py` +
`mut_m*.py`): engine = sympy 1.13.3 exact Gaussian-rational arithmetic
(no (re, im) Fraction-pair layer, no recognition, no tolerance anywhere);
constructions written from the d44d conventions docstring (periodic L=12,
beta = sigma_z, hopping ∓i/2; collar built as C-then-B = H − C rather than
weight-zeroed builders; FULL 5-term Neumann with asserted Δ^0- AND
Δ^1-freeness and a gated product == I).

**Symbolic (m formal), ORD 4, L 12, both rules — CONFIRMED IDENTICALLY:**

| object | receipt | my rebuild | match |
|---|---|---|---|
| EXC tau table (8 channels) | constants ∓1/2, ±1/4 | same | polynomial-identical |
| LT tau(±1,f) | ∓(3m²−1)(24m²−5)/2304 | same | polynomial-identical |
| LT tau(±2,s) | ±(36m⁴−60m²+7)/2304 | same | polynomial-identical |
| LT tau(±3,f) | ±(3m²−1)/256 | same | polynomial-identical |
| LT tau(±4,s) | ±1/512 | same | polynomial-identical |
| EXC D | 1·(I − σx) identically | same | yes |
| LT D | kappa(m)·(I − σx) | same | yes |
| kappa(m) | (1/36) − (5/48)m² + (1/16)m⁴ | m⁴/16 − 5m²/48 + 1/36 | zero difference |
| kappa − (9m⁴−15m²+4)/144 | zero polynomial | zero polynomial | yes |
| factor(kappa) | (3m²−1)(3m²−4)/144 | same (sympy factor) | yes |
| 4τ(2,s)+8τ(4,s) − kappa; 2τ(1,f)+6τ(3,f) + kappa | 0; 0 | 0; 0 | yes |
| EXC slots r=3,4; LT slot r=5 | empty | empty | yes |
| sub-onset (EXC 1; LT 1–3), Δ^0 == I | zero/I | zero/I | yes |
| realness; delta-odd | all channels | all channels | yes |

**YG3-C algebra re-derived by hand:** (3m²−1)(24m²−5) = 72m⁴−39m²+5 ⇒
−(...)/2304 = −5/2304 + (13/768)m² − (1/32)m⁴ = printed τ(+1,f); discs
2592 = 3600−1008 (non-square), 81 = 1521−1440 = 9² with x-roots 5/24 and
1/3, kappa-disc 81 = 225−144 with x-roots 1/3 and 4/3; 8τ(4) = 36/2304
folds into the 4·(...) bracket as +9, 7 → 16, and 4(3m²−1)(3m²−4) =
36m⁴−60m²+16 exactly; 2τ(1)+6τ(3) = (3m²−1)(−48m²+64)/2304 =
−(3m²−1)(3m²−4)/144 = −kappa — and the weights 2 and 6 are exactly
D(0,1) = Σ_δ δ·τ under delta-oddness (1·τ1 + (−1)(−τ1) + 3·τ3 +
(−3)(−τ3)), so the identity's weighting is consistent with the pipeline's
D = Σ δ·τ convention and the (I − σx) sign structure. All consistent
with the committed REF_LT values at m = 1/2 and 1 (recomputed by hand:
1/9216, −23/9216, −1/1024, 1/512; −19/1152, −17/2304, 1/128, 1/512).

**Out-of-hull / fresh masses (the all-m claim's new territory), TWO
engines:**

| mass | region | my exact rebuild kappa | committed d44d pipeline kappa | = quartic? | EXC = 1? | ray | all LT+EXC channels = polys? |
|---|---|---|---|---|---|---|---|
| 3 | ABOVE hull | 299/72 | 299/72 | yes | yes | yes | yes |
| 7/2 | ABOVE hull | 18733/2304 | 18733/2304 | yes | yes | yes | yes |
| 5 | ABOVE hull | 2627/72 | 2627/72 | yes | yes | yes | yes |
| 8/3 | ABOVE hull | 793/324 | 793/324 | yes | yes | yes | yes |
| 23/8 | ABOVE hull | 2027113/589824 | 2027113/589824 | yes | yes | yes | yes |
| 9 | ABOVE hull | 28919/72 | 28919/72 | yes | yes | yes | yes |
| 1/32 | BELOW hull | 4178953/150994944 | 4178953/150994944 | yes | yes | yes | yes |
| −1 | NEGATIVE m | −1/72 | — | yes | yes | yes | yes |

The committed-pipeline column is the d44d source exec'd unmodified up to
its banner and driven exactly per its own `kappa_pipeline` /
`tau_D_pairs` call pattern (ORD 4, L 12), with every tau channel
individually recognized and compared against the d45a channel polynomials
evaluated at that mass — channel-level agreement, not just the headline
constant. Triple concordance (receipt / my engine / committed engine) at
masses no prior run ever touched, including the m → −m even-symmetry
branch.

**Equivalence to the committed pipeline (attack surface: silent
divergence):** 11 load-bearing construction constants extracted
mechanically from both sources and matched — ORD 4 / L 12; EXC read at
Δ², LT at Δ⁴; rs = (1,2,3,4); collar lam = 1 via the region builder; LT
product order exp(B)·exp(C); delta wrap `> L//2 ⇒ −L`; Neumann budget
ORD//2+1; hopping ∓i/2; tau weight r; D weight delta. Declared deviations
(pin §5 A1) verified real and inert: exact-zero drops replace the
1e-45/1e-30 numeric dust drops (no exact-nonzero channel entry evaluates
below those thresholds at any tested mass — nothing was hidden);
singleton-only scope with slab arms inheriting per #353 + the d44d A5
note (verified present). PF1/PF2's port-fidelity content reproduces in my
rebuild (72 nonzero H entries; Hermiticity; mass-linearity).

**YG0 anchors vs committed record:** all 7 KREF rows (receipt lines
355–361) are byte-equal to the d44d .out KG2 table (lines 137–164);
REF_LT (receipt 363–370) is value-identical to d44d's committed T5 table
(d44d receipt 445–452). The pin's "m = 1/2 and 1 plus >= 3 more" is
exceeded (5 more).

**Pin hygiene:** `git show 2f1a3cc` — §1–4 (target, feasibility, gates
YG0–YG4, scope) committed BEFORE the receipt existed; fd91814 adds only
§5 A1–A2. A1's division-audit claim verified line-by-line (nit-4); A2's
beyond-pin status for YG3-C is honestly labeled in the pin, the .out
("gated at YG3-C"), and LOG #357 ("the beyond-pin YG3-C").

**LOG #357 vs artifacts:** every claim checked — 20/20 (carries MAJOR-1's
reading), 1,590 Fraction coefficients (reproduced), zero floats / no
mpmath (verified by grep + runtime walk), 7 grid masses (verified), the
quartic/factorization/channel statements (all verified above), seeds
0/7 + unseeded byte-identical (reproduced), ~0.5 s (reproduced), "the
symbolic tau channels hand-checked against the committed numeric tables
at m = 1/2 — all four match" (the four |delta| channels — verified). The
scope phrase "THEOREM for ALL m at fixture scale" is properly scoped
everywhere it appears (.out YG1 VERDICT, LOG). No numerical overstatement
found.

---

## Mutation table (10 mutants, receipt copied to scratchpad, one exact-string substitution each; REQUIRED: exit 1, no silent green)

| # | mutation | expectation | result |
|---|---|---|---|
| M1 | Hamiltonian coefficient: `_pc_mass` gains +m²/1000 (all diagonals) | H-shape gates trip | **exit 1**, 1 FAIL (PF2). Instructive: this corruption is a multiple-of-identity shift ⇒ pure phase ⇒ Γ kills it — kappa is UNCHANGED, and PF2's mass-linearity shape gate is the only catcher for this class. It caught it. |
| M2 | i² sign: `pc_mul` real part p_sub → p_add | complex arithmetic gated | **exit 1**, 9 FAIL (first YG0-A; PIPE-2 stays blind because (a²−b², 0) is still formally real — the damage is caught by value gates) |
| M3 | reference quartic tilted: KAPPA_TARGET 1/36 → 1/35 | YG1-C must bite | **exit 1**, exactly 1 FAIL (YG1-C, difference polynomial printed). Proves the all-m identity gate compares for real, and that no other gate depends on the target literal |
| M4 | drop the \|delta\| = 4 channel from tau accumulation | combination gated | **exit 1**, 8 FAIL (first YG0-A) |
| M5 | Neumann budget `ORD//2+1` → `ORD//2−1` | inverse-defect caught | **exit 1**, 1 FAIL — YG2-E ONLY (LT slot 172 entries); kappa(m) comes out EXACTLY correct. minor-2's evidence: single-gate margin for this defect class |
| M6 | D weight `delta_` → `abs(delta_)` | assembly gated | **exit 1**, 7 FAIL (D collapses to zero by delta-oddness; EXC ≠ 1) |
| M7 | anchored KREF corrupted: 13/2304 → 13/2303 | regression teeth | **exit 1**, 1 FAIL (YG0-A). With M3: the two anchor layers are independently gated, no shared literal |
| M8 | LT read at Δ² (EXTRACT_ORD) | wrong-order read caught | **exit 1**, 5 FAIL (first YG0-A: sub-onset zero matrices ⇒ empty D) |
| M9 | (−i)³ phase entry sign in MINUS_I_POW | exp assembly gated | **exit 1**, 8 FAIL (incl. YG1-C, difference polynomial (1/6) − (1/6)m² printed) |
| M10 | conjugation dropped in `s_conj` (Γ = U² not \|U\|²) | Γ = re²+im² gated at the polynomial level | **exit 1**, 11 FAIL (first PIPE-2 — the symbolic realness gate has teeth) |

**No silent-green mutant.** Every corruption of the Hamiltonian build,
the complex kernel, the exponential phase table, the Γ definition, the
Neumann inverse, the tau/D weights, the extraction order, and both anchor
layers exits 1.

---

## Reproduction appendix

```
cd /Users/felixrobles/workspace/isp
# receipt reruns (all exit 0, all BYTE-IDENTICAL to v10/data/d45a_symbolic_kappa_exact.out):
PYTHONHASHSEED=0 python3 v10/code/d45a_symbolic_kappa_exact.py > /tmp/r0.out   # ~0.5 s
cd v10 && PYTHONHASHSEED=7 python3 code/d45a_symbolic_kappa_exact.py > /tmp/r7.out
python3 v10/code/d45a_symbolic_kappa_exact.py > /tmp/ru.out                    # unseeded
# pin pre-registration:
git show 2f1a3cc:v10/note-d45a-symbolic-m-kappa-closure.md   # == current §1–4; §5 added at fd91814
# probes (session scratchpad, python 3.8.20, sympy 1.13.3):
#   indep_sympy.py               — symbolic rebuild + 8 fresh-mass exact runs ("ALL INDEPENDENT
#                                  CHECKS PASSED", ~7 s)
#   committed_pipeline_fresh.py  — d44d source exec'd, 7 fresh masses, channel-level
#                                  comparison ("ALL ... PASSED", ~6 s)
#   make_mutants.py + mut_m{1..10}.py — exit codes as tabled
# hygiene greps: float literals / imports / TOL / check( / sys.exit — results as cited above
```

## What was attacked and held

- **The derivation itself:** rebuilt from scratch on a different exact
  engine with a stricter Neumann layer — every polynomial identical; the
  hull caveat is genuinely closed (the identity holds at masses far
  outside [1/16, 2], below it, and at negative m, on two engines
  including the committed one).
- **The poly-complex kernel:** audited line-by-line (i² bookkeeping,
  conj, cscale, (−i)^k table, Cauchy truncation, Γ as z·conj(z) =
  (a²+b², 0) at the pair level, Neumann Δ⁰ assert) and attacked by M2,
  M9, M10 — all caught.
- **The zero-float claim:** no float literal outside a docstring
  reference; no mpmath/numpy; `math` usage integer-only (gcd, isqrt);
  runtime walk reproduces 0/1590 — with nit-1's wording caveat.
- **Equivalence to the committed pipeline:** 11 construction constants
  mechanically matched; semantic equivalence established at channel level
  at fresh masses; declared deviations verified inert.
- **YG3-C's algebra:** every expansion, disc, root, bracket-shift, and
  recombination re-derived by hand and CAS; the surviving weakness is
  minor-1's inference wording, not any number.
- **The record:** anchors byte-checked against committed artifacts;
  LOG #357 faithful; the surviving weakness is MAJOR-1's synthetic PASS
  in the ledger, repairable without touching a single number.

---

# DELTA VERIFICATION (round-1 repairs, LOG #360, commit 4edc109)

**Delta verdict: DELTA-CLEAN.** All six findings discharged as applied;
the repaired YG4-B is a genuine gate with demonstrated teeth; M5 is now
caught by PIPE-4; the biquadratic split check is sound and complete for
its branch; the record corrections are faithful. One NEW finding at nit
(delta-nit-1: an uppercase-`1J` complex literal evades the token scan —
demonstrated live, no exposure in the committed source, one-character
fix). The terminal condition is met from this referee's side.

## Discharge audit

- **MAJOR-1 — DISCHARGED.** YG4-B (receipt lines 917–940) is now a
  token-level self-scan: `tokenize` over `open(__file__)`, NAME tokens
  intersected with {TOL, mpmath, random, datetime, getenv, environ},
  non-hex/oct/bin NUMBER tokens required free of `.eEj`; strings and
  comments excluded by the tokenizer so the probe's own label (which
  names TOL and mpmath) cannot self-trip — verified working: the
  committed run is green while the label mentions both. **Teeth
  demonstrated on the repaired receipt:** delta-mutant MD1
  (`_SMUGGLED = 1.5` inserted) → exit 1, YG4-B FAIL; MD2 (`TOL = 10`)
  → exit 1, YG4-B FAIL. My independent stricter scan of the committed
  source confirms: 421 NUMBER tokens (matches the printed count), zero
  containing any of `. e E j J`, banned-name intersection empty. The
  byte-identity claim is correctly OUT of the gate (an external
  protocol line, seeds 0/7 — which this delta re-verified). Note §6 B1
  owns the violation in full — including that pre-commit PASS-count
  verification cannot catch gate vacuity (protocol note) — and its
  cited precedent is real (LOG 6130: d43b F-B3, a check(True)
  conviction). LOG #360 forward-corrects #357's "GREEN 20/20" to "19
  computed + 1 declared as committed; 22 computed as repaired."
- **The commissioned attack on the new gate — CAN it be fooled?** At
  the margins, yes, and one route is live: **delta-nit-1 (NEW, nit).**
  The literal scan checks the character set `.eEj` but Python also
  accepts uppercase-J complex literals: delta-mutant MD3
  (`_SMUGGLED = 1J`) runs **22/22 PASS, exit 0 — silent green** while
  the gate's label claims "NO float or complex NUMBER literal". The
  runtime walk is also blind to it (complex is neither float nor
  Fraction; unknown leaf types are silently ignored). No exposure: the
  committed source is clean under my J-inclusive scan, and FLOAT
  literal coverage is complete (Python float literals require `.` or
  `e/E`, both checked). Fix: one character (`.eEjJ`, or lower() the
  token string) at next touch.
  **Deny-list judgment (as commissioned):** for THIS receipt the
  deny-list + runtime walk combination closes the routes that matter —
  the walk now spans the ENTIRE dataflow chain end-to-end (H → U_free →
  Gam_free → Gfi → every cached J → tau/D/kappa/target; FRACS 1590 →
  2886), every gate compares walked structures, and any runtime-
  constructed float retained anywhere in that chain is counted
  (np.float64 included — it subclasses float). The residual structural
  gaps are: transient floats used only in a condition (none exist; all
  gate inputs are walked structures), and non-float-subclass numeric
  types (complex, Decimal, np.float32, mpf) which the walk ignores
  rather than rejects. **Prescribed allow-list form (successor-binding,
  optional here):** invert `type_walk` — count every leaf NOT in
  {Fraction, int, str} as a violation and gate the count == 0. One-line
  change; converts the walk from "no floats seen" to "nothing but exact
  types present", closing every type-smuggling route this referee can
  construct, including MD3's class if such a value ever reached a
  walked structure.
- **minor-1 — DISCHARGED.** The disc print is now scoped ("irreducible
  over Q AS A QUADRATIC IN x = m^2 ... the m-quartic could a priori
  still split — checked next", .out lines 120/123) and the biquadratic
  m-split check runs in-receipt (receipt lines 760–781), printing NONE
  for both tau(±2, same) rows. **Algebra audited:** the check tests
  a2(m² + cm + d)(m² − cm + d) via d² = a0/a2, c² = 2d − a1/a2, both
  signs of d, rational-square tests by exact isqrt on reduced
  numerator/denominator (Fraction auto-reduction makes the
  per-component square test valid), c ≠ 0 enforced via c² > 0 (c = 0
  is the even-even split, already refuted by the non-square disc in
  this branch). **Branch-context completeness verified:** with a
  non-square x-disc there are no rational x-roots, hence no linear
  m-factors and no even-even quadratic splits; a 1×3 split forces
  m | q, i.e. a0 = 0, which never reaches this branch (a0 = 0 ⇒ disc =
  a1², a perfect square); so the conjugate pair is the ONLY remaining
  factorization pattern — exactly what is tested. **Mechanically
  cross-checked against sympy factor_list on 6 cases** including the
  round's counterexample class: m⁴+4 → EXISTS (reducible), m⁴+2m²+9 →
  EXISTS, m⁴+m²+1 → EXISTS, m⁴−3m²+1 → EXISTS, 4m⁴+8m²+9 → EXISTS
  (all confirmed reducible by sympy), 36m⁴−60m²+7 → NONE (confirmed
  irreducible) — 6/6 agreement. The YG3 VERDICT's "IRREDUCIBLE over Q"
  for tau(2,same) is now supported by in-receipt computation.
- **minor-2 — DISCHARGED.** PIPE-3 (Δ¹-freeness of Γ(U_free) as a
  polynomial statement) and PIPE-4 (Gfi · Γ(U_free) == I as a
  truncated series, diagonal Δ⁰ == 1 with higher orders zero AND all
  off-diagonal entries zero; absent-entry-as-zero semantics correct)
  are real gates at receipt lines 453–466. **M5 re-run against the
  repaired receipt: exit 1 with 2 FAILs — PIPE-4 AND YG2-E** — the
  round's single-gate margin is now two independent gates, one of them
  (PIPE-4) directly at the defect's site rather than four stages
  downstream.
- **nits 1–3 — DISCHARGED.** YG4-A walks U_free/Gam_free (label
  updated and now accurate; the printed count moved 1590 → 2886,
  consistent with the two added structures; LOG #360 carries the
  forward-correction context). YG2-B covers LT site 5 (`range(6)` for
  LT — the realness sweep now spans every retained site of both
  rules). YG3-A's label now says "recombined from the retained channel
  objects ... the independent rebuild is the frozen round's" — exactly
  the honest description.
- **nit-4 — residual disposition ACCEPTED.** The round required no
  action; the biquadratic addition touches `factor_report` but
  introduces no NEW green-executed dead code beyond the inherent
  reducible-case arms (the EXISTS path and the square-r0 sub-branches
  are unreachable for these inputs by mathematical necessity — a
  checker for reducibility must contain the reducible arm). Those arms
  were exercised externally by this delta's 6-case battery. The
  TypeError banner claim stands as round-1 verified.

## Mechanical verification

- `git diff fd91814 4edc109` on the d45a paths contains EXACTLY the
  enumerated repairs and nothing else: receipt = 6 hunks (PIPE-3/4
  insert; YG2-B widen + label; factor_report scope wording + split
  check; YG3-A label; YG4-A walk + label; YG4-B rebuild — no
  arithmetic upstream of the tau/D derivation touched); .out = the
  matching regions only (PIPE lines, YG2-B/YG3-A/YG4 labels, the two
  scoped disc lines + two NONE lines, SUMMARY 20 → 22); note = §6
  B1–B4 appended, §1–5 byte-untouched; LOG additive. This round-1
  review body was committed BYTE-INTACT at 4edc109 (341 lines; zero
  worktree-vs-commit diff before this delta section was appended).
- Repaired receipt re-run twice at delta time: PYTHONHASHSEED=0 from
  repo root and PYTHONHASHSEED=7 from `v10/` — both exit 0, **22 PASS
  / 0 FAIL**, both **BYTE-IDENTICAL** to the committed
  `v10/data/d45a_symbolic_kappa_exact.out`. The new `open(__file__)`
  self-read is invocation-relative and cwd-robust as exercised (the
  v10/ run is the witness).
- LOG #360's summary of the round is faithful row-by-row: the sympy
  rebuild (own collar, 5-term Neumann WITH product gate), the 8 fresh
  masses by name, channel-level triple concordance on two engines,
  10/10 mutants, the referee-proved irreducibility, the 0B/1M/2m/4n
  tally, and the ownership framing of the MAJOR (including the
  protocol note that pre-commit verification cannot catch vacuity).

## Delta mutation table (repaired receipt, scratchpad copies)

| # | mutation | expectation | result |
|---|---|---|---|
| M5 (re-run) | Neumann budget `ORD//2+1` → `ORD//2−1` | PIPE-4 must now catch it | **exit 1**, 2 FAIL (PIPE-4 + YG2-E) — margin closed |
| MD1 | `_SMUGGLED = 1.5` inserted | YG4-B literal scan | **exit 1**, 1 FAIL (YG4-B) |
| MD2 | `TOL = 10` inserted | YG4-B name scan | **exit 1**, 1 FAIL (YG4-B) |
| MD3 | `_SMUGGLED = 1J` inserted | label says complex excluded | **exit 0, 22/22 — SILENT GREEN**: delta-nit-1's live demonstration (`.eEj` misses uppercase J; walk blind to complex) |

## Terminal-statement check

The stamped conversion statement was audited clause-by-clause against
the artifacts: the identity kappa(m) = (9m⁴ − 15m² + 4)/144 =
(3m² − 1)(3m² − 4)/144 derived as an exact all-m polynomial identity at
fixture scale (ORD 4, L 12) — round-1 rebuild + this delta's 22/22;
"zero floats" — the repaired self-scan + the full-dataflow runtime walk
+ this referee's J-inclusive independent scan; the ray collapse and all
auxiliary vanishings as polynomials — YG1/YG2 + the frozen round's
independent reproduction; the channel-resolved factor origins
((3m² − 1) common to the flip sector; (3m² − 4) combination-only; the
tau(4) bracket shift 7 → 16) — YG3-C + the round's hand/CAS rederivation;
the hull-caveat closure with the 28-point verification as the identity's
shadow — YG0's exact regression plus the round's out-of-hull triple
concordance at 8 fresh masses. Every clause is supported. No objection
to conversion on this statement. Recorded for the terminal row:
delta-nit-1 (the one-character `J` fix) and the allow-list walk as the
successor-binding purity-gate form.
