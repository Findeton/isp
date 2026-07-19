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

## 4. First-run amendments (2026-07-19, pre-round; the receipt's
## declared deviations, owned as pin gaps)

**A1 (two-arm KG1).** The pin's "regions = contiguous blocks" and
B4's log-smeared slab (v2 p1 §7 builds slabs from SINGLETON maps
under a test-weight profile) are DIFFERENT constructions. The
receipt runs both, pinned in-banner: COMPOSITE (the §7 reading — the
theorem arm) and BLOCK (the literal reading). The theorem statement
attaches to the COMPOSITE arm; the BLOCK arm's EXC = ((w+1)/2)^2
exact collar-length-square normalization is a delivered finding.

**A2 (separation range).** r_max = w+1 (EXC) / w+3 (LT) — the exact
kernel-support bound — with an r_max+1 completeness slot gated zero
on clean cells. The pin left the r-range unspecified.

**A3 (wrap exclusion).** At L = 12 the LT kernel span [b-2, b+w+1]
meets the periodic seam for w in {3,4}; those 8 LT cells are
seam-contaminated (support lemma; the completeness slot's nonzero
value is the empirical wrap witness), excluded from the theorem gate
and delivered exactly; the L = 16 twins are clean. The pin's grid
implicitly assumed all L = 12 cells usable.

**A4 (ORD = 4 beyond KG2).** The pin's order-reduction clause named
KG2 only; the receipt runs KG1/KG3 at ORD 4 as an EXACT truncation
(gated: ORD-12 vs ORD-4 leading-coefficient deviation = 0.0 at
1e-40); SG0 stays at ORD 12.

**A5 (weight-family independence).** By translation covariance the
phi-weighted mean pair separation equals r exactly, so the
composite-arm collapse constant is weight-family independent at this
moment order — declared in-banner; log-uniform
(phi_j = (1/(j+1))/H_w) is the pinned instance actually run. This is
the cancellation-order content for the §5 conversion note.

**A6 (KG3 conventions).** Collar = mass at n0 + the electric term of
index n0 (the gauge string through n0) + incident bonds; pairs
({1},{2}) and ({1},{3}); STRUCTURED = per-N-sector proportionality;
the validator's committed point (m, g) = (7/10, 1/2), t = 1,
lambda = (9/10, -2/5, 11/10, 1/5). The pin left these to the
receipt.

## 5. Round-1 amendments (2026-07-19; round frozen at
## reviews/d44d-round1-hostile-review.md: PASS-AS-RESCOPED,
## 0B/1M/2m/5n)

**B1 (MAJOR-1 — the KG3 framing rescoped; the finding accepted in
full).** The DIVERGENT/DIVERGENT verdict is exactly reproduced and
collar-convention-robust (three collar conventions agree), BUT the
round's g = 0 control on the same fixture is ALSO divergent, and the
free core was already divergent at this grain (d43a T2/T4). The
divergence is GRAIN-INHERITED, not interaction-specific; the pin §1
KG3 clause "decides whether the free-core ray universality even
ARRIVES at the interacting fixture's grain" OVERSOLD the instrument.
Corrected reading (now in the receipt's KG3 verdict line): the raw
singleton-bracket divergence persists at the interacting point
exactly as at g = 0; whether RAY-level universality survives
interaction is UNDECIDED here and belongs to the smeared interacting
identification — the declared successor, whose pin must include a
g = 0 column. LOG #350's KG3 sentence is forward-corrected at #352.

**B2 (minor-1/minor-2 — self-auditability).** The KG2 ansatz scan
order is now PRINTED in the .out (was code-comment-only); the banner
now states as designed that clean-cell collapse constants and
verdict lines are DELIVERED-VERDICT content whose integrity rides on
byte-identical determinism (the M5/M8 mutant class flips text, not
exit — caught by byte-diff), with the exit-gated layer enumerated.

**B3 (nits owned).** The KG2 header now prints the true hull
[1/16, 2] (was "(0, 2]"); direct_bisect_64 now handles an exact
grid-point root explicitly (unreachable for the identified quartic —
roots irrational — guarded anyway); the BOTH-ZERO verdict class
omission from A6, the structurally-trivial ungated EXC order-1
sub-onset at slab scope, and the data-dependent recognize() margin
(6 orders spare here, auditable) are recorded as known residuals —
no code change.
