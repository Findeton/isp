# D44d (successor 4) — the slab smeared theorem, exact kappa(m), and the interacting cross-check

**Status:** CAMPAIGN PIN (strict), 2026-07-19.  Parents: d43a
TERMINAL (#340; B4's named successors: the LT log-smeared finite-slab
theorem; kappa(m) as an exact function with its zero crossing; the
interacting p15-fixture cross-check); the v2 p1 §5 continuum
identification as ported in the d43a receipt; the root validator
(`validate_minimal_interacting_gauge_matter_benchmark.py`, read-only
conventions source).  Receipt: `v10/code/d44d_slab_kappa_exact.py`
(exact order-12 series arithmetic — the d43a machinery; mp.dps 50 /
1e-30 only where floats enter).  Execution gated on paper-31
terminal.

## 1. The three deliverables

**KG1 (the slab arm — the theorem's mechanical content).**  d43a
proved the ray collapse for SINGLETON regions.  Promote to slabs:
regions R = contiguous blocks of width w in {1, 2, 3, 4} at
L in {12, 16}, with the smeared identification (the tau first-moment
construction applied to the slab defect channels, log-uniform test
weights over the slab — the weights pinned in-receipt before
verdicts).  Gate: for EVERY (w, L, m) cell, both rules' identified
tangential operators collapse onto the SAME ray K_par with a
w-INDEPENDENT constant equal to the singleton kappa(m) (EXC: 1;
LT: kappa(m)).  Slab-width independence of the constant IS the
fixture-scale content of the finite-slab theorem; the accompanying
§5 proof note (written at conversion, only on green) states the
cancellation-order argument [THEOREM at fixture scale].  Any
w-dependence is a delivered finding, not a failure — it would scope
the singleton result and must be logged as such.

**KG2 (kappa(m) exact + the zero crossing).**  kappa(m) computed
exactly at a rational mass grid of >= 25 points covering (0, 2]
(including 1/2 and 1 as regression anchors: 13/2304 and -1/72).
Then: identify a closed form by exact ansatz — rational function of
m (and, if the series structure indicates, of m^2) with degree
scanned upward; coefficients solved exactly from a minimal subset
and VERIFIED on the full remaining grid (overdetermination factor
>= 2; zero tolerance).  On an identified form: the zero crossing =
the exact root of the numerator polynomial inside the sign-change
bracket ((1/2, 1) initially, since kappa(1/2) > 0 > kappa(1)).  If
NO scanned form fits exactly: deliver the grid, the sign-change
bracket refined to width <= 1/64 by exact bisection on grid points,
and the non-fit census (degrees tried) — [EXACT either way; the
closed form is a target, not a promise].

**KG3 (the interacting cross-check).**  The bracket-level comparison
(the d43a T4 object: one-region coefficient commutators, both rules)
on the root validator's minimal interacting gauge-matter fixture at
one committed (m, g) point, singleton regions, d in {1, 2}:
PROPORTIONAL / STRUCTURED / DIVERGENT / SUPPORT-MISMATCH per cell,
pre-registered open.  This decides whether the free-core ray
universality even ARRIVES at the interacting fixture's grain; the
smeared interacting identification is declared a successor, not
attempted here.

## 2. Gates

- **SG0 (regression):** the d43a anchors re-run (AN1-AN4; the
  singleton kappa values; tau tables delta-odd) — the machinery is
  the same code path, re-anchored.
- **SG1-SG3:** KG1/KG2/KG3 as pinned above, each cell a gate.
- **SG4 (precision honesty):** exact series everywhere; float
  entry points enumerated in the banner; thresholds printed.
- **SG5 (determinism):** rerun byte-identical.

## 3. Scope

Free core at slab scope (KG1/KG2); ONE interacting point (KG3) —
the interacting result, whatever it is, is a single-fixture
statement.  No continuum claim beyond the identification the corpus
already owns; no claim about masses outside the grid's hull.
