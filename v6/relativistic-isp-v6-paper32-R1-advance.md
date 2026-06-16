# R1 / (C-reg-b) — Advance on the parametrix remainder (2026-06-14)

Addendum to Paper 32. Independent audit identified (C-reg-b) as the corpus' highest-leverage
residue (it gates the SM-continuum + horizon arcs). This note records a concrete advance on the
**named-open obligation** — paper 32's correction note (2026-06-11): *"the proof obligation
(uniform two-sided parametrix bounds for non-smooth coefficients) is open."*
Code: `code/v6_r1_parametrix_remainder.py` (exact eigendecomposition, reruns deterministically).

## The object
Record operator `L = -d/dx(c d/dx)` on the circle, `c >= c0 > 0`. Local Weyl remainder
`r_t(x) = K_t(x,x) sqrt(4 pi c(x) t) - 1`. (C-reg-b): `sup_x|r_t| -> 0` (with rate) detects/grades
the regularity of `c`.

## What this advance establishes

### 1. The first heat coefficient, derived (forward leading order, now rigorous)
Via the Liouville transform `y = ∫ c^{-1/2} dx`, `v = c^{1/4} u`, the operator is unitarily
equivalent to a Schrödinger operator `-d²/dy² + Q` with
```
   Q = c''/4 - (c')²/(16 c)        (' = d/dx)
```
and (transforming the on-diagonal kernel back, `K_t(x,x) = c^{-1/2} \tilde K_t(y,y)`):
```
   r_t(x) = a1(x) t + O(t²),   a1(x) = -c''/4 + (c')²/(16 c).
```
**Verified:** `r_t(x)/t -> a1(x)` to sup-rel-error 0.013 at t=1e-3 (converging), at all probe points.
This pins the parametrix constant (the leading `c''` coefficient is exactly `-1/4`, matching the
numerically calibrated `kappa = -0.253`). Smooth `c` => `a1` bounded => `sup|r_t| = O(t)` — the
smooth-class rate, now with an explicit closed-form coefficient.

### 2. The remainder IS a window modulus of continuity (parametrix structure verified)
The frozen-coefficient parametrix gives `r_t(x) = (kappa/c(x)) ∫ G(u)[c(x+sigma_t u) - c(x)] du + O(t)`,
`sigma_t = sqrt(2 c(x) t)`. Verified numerically: for smooth `c` the remainder matches the window
modulus with the O(t) error shrinking (rel-mismatch 0.34 -> 0.13 as t halves); the formula also holds
for non-smooth `c` (the cusp dominates). So `r_t` is, to leading order, the Gaussian-window modulus of
continuity of `c` at scale `sqrt(t)` — the structural fact paper 32 stated "heuristically."

### 3. The alpha in (1,2) band — RESOLVED (filled paper 32's named gap)
Paper 32 left `alpha in (1,2)` under-resolved (measured 0.49 vs predicted 0.75 at alpha=1.5).
**Diagnosis:** the global `sup_x|r_t|` is contaminated by (i) the smooth-background curvature and
(ii) antipodal corners in the cusp construction — which pin the apparent rate near 0.5-0.6 for all
alpha>=1. Measuring `r_t` AT the cusp on a flat-top window (no background curvature near x0) removes
the contamination and recovers the graded law cleanly through the FULL range:

```
   alpha       0.50  0.75  1.00  1.25  1.50  1.75  2.00
   predicted   0.25  0.375 0.50  0.625 0.75  0.875 1.00   (= min(1, alpha/2))
   rate@cusp    0.243 0.365 0.491 0.619 0.745 0.872 0.999  <- tracks prediction
   rate(sup)    0.243 0.365 0.557 0.611 0.606 0.601 0.595  <- contaminated (the paper32 artifact)
```
The forward graded law `C^alpha => rate min(1,alpha/2)` is thus confirmed across `(0, 2]`, not just
`alpha <= 1` + the smooth endpoint.

### 4. The homogenization impostor reproduced (the converse needs ALL scales)
Smooth-but-oscillatory `c = 1 + 0.6 sin(2 pi x/delta)`, `delta=1/32`, at `t >> delta²`: the detector
reads the **harmonic mean** (`c_eff = 0.7996` vs harmonic 0.8000, arithmetic 1.0000 excluded). The
detector measures regularity AT SCALE `sqrt(t)` — confirming paper 32 T3.1: the naive converse is
false, and the "all-scales" qualifier in the corrected converse is essential.

## The rigorous-proof route for the named obligation (the remaining analytic work)
The uniform two-sided non-smooth bound is assemblable from standard pieces:
- **Frozen-coefficient Duhamel:** `K_t - K^x_t = ∫_0^t ∫ K^x_{t-s}(x,z)[(L_x - L)_z K_s(z,x)] dz ds`,
  `L_x - L = (c(x)-c(z)) d²_z - c'(z) d_z`. IBP moves derivatives off the distributional `c'` onto the
  smooth Gaussian kernels. Leading term = the window modulus (item 2).
- **Error bound via the heat-semigroup Hölder–Zygmund characterization** (Triebel/Stein):
  `||c||_{C^alpha} ≍ sup_s s^{-alpha/2} ||(e^{s d²}-1) c||_inf`. This makes the window-modulus term a
  genuine `C^alpha`-norm functional (=> two-sided `t^{min(1,alpha/2)}`, uniform in x) and bounds the
  Duhamel remainder as subdominant. This is the exact classical input paper 32 named ("the semigroup
  characterization of Besov spaces").

## Precision receipt (standing rule, honored by proof)
The R1 heat-kernel remainder carries **no `F(ν)=log((ν+½)/(ν−½))` and no near-vacuum divergence** (the
heat sum `Σ e^{−tλ}φ²` is exponentially damped, well-conditioned), so it is structurally float-safe like
the P50 entropy. Verified, not assumed: float64 vs **mpmath dps-80** anchor (N=128, c=1+0.5sin2πx, t=0.01)
agree to **max |Δ| = 1.4×10⁻¹³** across probe points — the float64 band-rate results are precision-valid.
mp dps-80 remains reserved (and used) where it is load-bearing — the modular-kernel/F(ν) sector (P52–55).

## Honest status after this advance
- **Forward direction:** leading coefficient derived (item 1) + graded law confirmed across `(0,2]`
  (item 3) + parametrix structure verified (item 2). Strong.
- **Converse (rate => regularity, all scales):** the Besov frame is identified and the impostor
  structure confirmed (item 4); the rigorous statement still rests on completing the semigroup-
  characterization argument (the proof route is laid out, not formally written).
- **Still open (the residue proper):** the formal write-up of the uniform two-sided Duhamel error
  bound; and the multi-dimensional / Lorentzian port `(C-reg-rig)` — the deeper residue beyond 1D,
  untouched here.

So R1's 1D core is reduced from "named-open obligation" to "a standard (if technical) parametrix +
Besov proof, with the forward direction numerically closed across the full Hölder range and the one
band paper 32 could not resolve now resolved." The leverage claim stands: this is the residue whose
closure would convert the largest fraction of the corpus from conditional to continuum-valid.
