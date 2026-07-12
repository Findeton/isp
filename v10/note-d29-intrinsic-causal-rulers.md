# D29 — intrinsic causal rulers, validation-first

**Status:** PIN (pre-receipt), 2026-07-12; committed before `code/d29_ruler_validation.py` runs. Provenance labels per D20. This is the instrument stage of the D28→D30 arc: every estimator is validated on synthetic ground truth BEFORE any grown web is touched — the repair of the v9 instrument failure, executed as the standing discipline. **The D28b prerequisite is in force:** the input order for grown webs is the EVENT order (D28b part 1 — a strict partial order); the influence instruments fix the alphabets per D28 §2's kickback pin.

## 1. The instruments (order-only; no coordinates consulted)

- **Dimension d̂_MM:** the Myrheim–Meyer ordering-fraction estimator (the fraction of comparable pairs in an interval, inverted through the exact d-dependent closed form); cross-check: midpoint scaling (|interval| halving under midpoint splits).
- **Proper time τ̂:** longest-chain length through an interval, calibrated per dimension (the Brightwell–Gregory constant absorbed into the validation bands — we calibrate, not assume).
- **Spatial distance:** the Rideout–Wallden **2-link** construction between spacelike pairs (naive common-past/common-future minimization is EXCLUDED — their own failure result; carried from the D28 pin).
- **Cone instruments:** on the event order with declared alphabets — the support front, the ε-front and quantile fronts, and the weighted anisotropy profile (never the bare maximum; the D28 §2 reporting pin).
- **Direction (two arms, strictly ordered):** the dimension-NEUTRAL arm (dimension and front shape from causal order alone) runs first; the conditional-S² arm (comparison with the corpus's celestial bridge) is licensed ONLY where the neutral arm reads d̂ ≈ 4 — the anti-insertion discipline (3+1 must not be assumed into the ruler).

## 2. The validation suite (synthetic ground truth; PASS criteria pre-registered)

Poisson sprinklings into causal intervals of M^d: **d ∈ {2, 3, 4}, N ∈ {256, 512, 1024}, 20 seeds per cell** (pilot scale; escalation only if bands demand it — declared budget). Controls that must be handled correctly: **(a) window geometry** (interval vs box — boundary-effect disclosure); **(b) missing-record noise** (delete fraction p = 0.1 — band shift measured, not assumed); **(c) the polyhedral control** (a finite-C dominance web — the ruler must NOT read it as manifoldlike-4d); **(d) the non-manifoldlike control** (transitive percolation random orders — must be REJECTED by the joint signature). PASS criteria, pre-registered: d̂_MM within ±0.35 of true d at N = 1024 (mean over seeds; the d = 2 small-N bias disclosed if seen); τ̂ linear in the interval height with per-d calibration constants stable across N at the ±10% level; 2-link distance monotone in the true spacelike separation on calibrated pairs; both controls rejected by the pre-registered discriminator (ordering-fraction + chain-length joint signature outside all manifold bands).

## 3. Precision and discipline declarations

**Float64 Monte Carlo is the declared arithmetic for sprinkling statistics** (standard for causal-set numerics; the corpus's mpmath ≥ dps-80 rule binds modular-kernel/near-vacuum chains, which this is not — stated so the precision memory is honored, not brushed); all order combinatorics are exact per sample; all RNG seeds fixed and printed; outputs = the **instrument card** (`data/d29_instrument_card.json`: per-(d, N) bands for every estimator + the control signatures) to be consumed by D30 UNCHANGED — the card freezes before any kernel web is measured. V9 discipline verbatim: no v9 measurement reused; these are new implementations validated on synthetic ground truth only; grown webs enter only in D30.

## 4. Round-1 fronts (pinned)

(F1) The MM estimator's small-N and d = 2 biases — bands honest? (F2) Boundary effects: interval-sprinkling edge corrections vs the box control. (F3) The 2-link constant's N-drift. (F4) Is the joint control-rejection discriminator sharp enough (could a tuned percolation order sneak inside the manifold bands)? (F5) The noise band at p = 0.1 — linear response or threshold? (F6) D28b's hostile pass rides with this round (declared): the event-influence conjecture's battery scope and K_flat's canonicalization (note-d28b §4 F1–F5).
