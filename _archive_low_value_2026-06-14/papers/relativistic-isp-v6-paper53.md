# The Geometry Side: the Static Two-Wedge Modular Congruence Carries the Rotation Sector, Not the Graviton

**Relativistic ISP — SHARD v6, Paper 53**

## Summary

Paper 52 proved that the static modular charge of a *single* region is the
boost = energy generator (Bisognano–Wichmann), built from the trace (∇φ)², and is
blind to the traceless spin-2 stress T_ij^TL — the graviton degree of freedom. By
the Jacobson division of labor, that is the structurally correct place for the
matter currency to stop: the graviton is not a matter charge but the emergent
geometric response of a *congruence* of regions. This paper asks the sharp
successor question: does T_ij^TL reappear in the **congruence** — the variation of
the modular Hamiltonian across differently-oriented regions — even though it is
absent from each single region's charge?

For the **static, two-wedge, spatial congruence** built here, the answer is
**GEOMETRY-BLIND**, and it rests on two legs of *different kinds*, which we are
careful to weight correctly.

The congruence of two wedges boosted in orthogonal directions (A: x-boost,
B: y-boost) supplies two genuinely new cross-region objects: the *antisymmetric*
commutator B_AB = ½(K_A K_B − K_B K_A) and the *symmetric* product
C_AB = ½(K_A K_B + K_B K_A).

- **The antisymmetric sector is settled by a selection rule (lattice-exact, but
  not contingent).** B_AB is exactly antisymmetric (the antisymmetrized product of
  two real symmetric kernels), and the spin-2 shear source is exactly symmetric,
  so their contraction is *identically* zero — antisym·sym = 0. The numerical
  "Berry traceless amplitude" (7×10⁻¹⁵ → 3×10⁻¹⁴, at the float64 roundoff floor) is
  therefore an algebraic consistency check, **not** a physics measurement: it
  would vanish for any symmetric kernels. Its physical content is only the
  *continuum identification* of that sector — the commutator of two boosts is a
  rotation, [K_x, K_y] → −iJ_z — which places the antisymmetric channel in the
  **spin-1 rotation** sector, orthogonal to the symmetric spin-2 shear and inside
  the orientation-reversing circulation sector barred by Paper 42 (det(JR) = −1).

- **The symmetric sector is the genuine, contingent, load-bearing result.** C_AB
  *is* symmetric and *can* couple to spin-2 (sym·sym). What it does is a real
  lattice measurement, not forced by any identity: the C_AB traceless coupling,
  normalized by its (nonzero) energy charge, never exceeds — in fact falls
  *below* — the same-cut baseline ½(K_A² + K_B²), with the cross-excess
  **negative and growing more negative under refinement, −0.30 → −0.35 → −0.44**
  across L = 12, 16, 20. Adding the second boost direction opens **no** new spin-2
  channel; the symmetric cross coupling is weaker than what a single direction's
  kernel-square already supplies. This is the result that decides FORK G.

The symmetric channel is a *live* instrument, not a dead one: C_AB carries a
nonzero energy (trace) charge — it prices symmetric energy input — so its spin-2
coupling falling below baseline is a structural statement about the spin-2 sector,
not an artifact of a silent operator. (The antisymmetric CAL-LIVE contrast,
−10.55 vs 5×10⁻¹⁶, is likewise symmetry-forced and certifies only that the
rotation/spin-1 channel is open — which was never in doubt.)

The natural route by which a *ball* congruence could instead source spin-2 —
FGHMVR's entanglement-equilibrium — is **holographic**: it recovers linearized
Einstein in a *bulk* dual. The record lattice is a boundary field theory with no
bulk, so the first law δS = δ⟨K⟩ holds at first order with no residual and carries
no geometric constraint there.

**Scope (stated honestly).** This establishes GEOMETRY-BLIND for the *static,
two-wedge, spatial* congruence. The ball-family (FGHMVR), the Lorentzian /
boosted timelike-separated region pair, and the second-variation (Raychaudhuri /
focusing) objects are **gated — untested, not refuted**. The one experiment that
could flip the verdict to VISIBLE/MIXED is the boost-angle-sweep of the symmetric
cross-coupling on a Lorentzian region pair; we name it and gate it.

With that scope, the demarcation is complete on the static side: Paper 51 (the
dynamics reaches the generic multipole structure but not gravitational quadrupole
dominance), Paper 52 (the single-region charge prices energy and momentum but not
the traceless spin-2 stress), and Paper 53 (the static two-wedge congruence
carries the rotation sector but not spin-2). The scalar record-dynamics program
reaches all of *matter* (energy–momentum) and stops precisely at the graviton —
which requires either an emergent holographic bulk (absent here) or the
Lorentzian/dynamical sector (Paper 51, gated). On the static side, the program is
honestly **capped at the scalar energy–momentum first law.**

---

## 1. The question

Papers 44–52 built a scalar modular currency and mapped exactly where it reaches.
Paper 48 priced the **energy** T₀₀ (the modular first law δ⟨K⟩ = δS, the
boost-weighted charge δK = 2π∫(x−x_cut)δT₀₀). Paper 49 priced the **momentum**
T₀ᵢ through the boost *flow* (the K_p sector, sector-universal with energy at the
10⁻⁴ level). Paper 52 proved the **traceless spin-2 stress** T_ij^TL =
∂ᵢφ∂ⱼφ − ½δᵢⱼ(∇φ)² is projected out of any single region's static charge — by
Bisognano–Wichmann the static modular Hamiltonian is the boost = energy generator,
built from the trace (∇φ)², and the traceless combination is Frobenius-orthogonal
to it (confirmed by a floor-verified 14.6× collapse under matched-depth
refinement).

Paper 52 closed with the Jacobson placement: a blind matter currency is
structurally correct, because the graviton is the emergent geometric response of a
*congruence* of regions, not a matter charge. This paper tests that other half:

> Does T_ij^TL reappear in the congruence — the variation of the modular
> Hamiltonian across a family of differently-oriented regions — even though it is
> absent from each single region's static charge?

A spin-2 signal in the congruence would not contradict the single-region blindness
(a different observable — the cross-region variation, not the charge of one
region), exactly as Paper 49's momentum (reached by the flow) did not contradict
the static charge's blindness to T₀ᵢ.

**FORK G** (pre-registered): **GEOMETRY-VISIBLE** (the congruence's traceless
coupling exceeds the single-region/same-cut baseline *and* survives refinement →
the linearized spin-2 source is recoverable); **GEOMETRY-BLIND** (it never exceeds
the baseline, or collapses → capped at the scalar first law); **MIXED** (stable
but coefficient-unmatched or partial). The operative gate is whether the
congruence *opens a new symmetric channel* beyond the same-cut baseline; the
verdict is decided by that, not by the antisymmetric sector (which a selection
rule fixes regardless).

Two traps must be disarmed. The **trivial-BLIND trap** (a dead instrument rather
than a structural fact) is disarmed for the spin-2 channel by C_AB carrying a
nonzero energy charge — it is a live instrument for symmetric input (§3). The
**insertion trap** (smuggled geometry) would be disarmed, had a positive arisen,
by the combinatorial-only region family and the requirement that any recovered
coupling match the independently-measured G = 1/(4ν); it does not arise here.

---

## 2. The two cross-region objects and the selection rule

The congruence of two wedges cut along orthogonal directions — A = {x ≥ j}
(modular flow ≈ boost in x) and B = {y ≥ j} (boost in y) — supplies two
genuinely new objects beyond any single region's kernel:

  C_AB = ½(K_A K_B + K_B K_A)  (symmetric cross product),
  B_AB = ½(K_A K_B − K_B K_A)  (antisymmetric commutator).

These split the question cleanly by symmetry, and the two halves are settled by
*different kinds* of argument.

**The antisymmetric sector — a selection rule.** K_A and K_B are real symmetric
matrices, so (K_A K_B)ᵀ = K_B K_A and B_AB is *exactly* antisymmetric. The spin-2
shear source S_+ = gₓgₓᵀ − g_yg_yᵀ and S_× = gₓg_yᵀ + g_ygₓᵀ are *exactly*
symmetric. Therefore B_AB · S = 0 identically — an algebraic selection rule
(antisymmetric · symmetric = 0), true for *any* symmetric kernels, carrying no
contingent information about modular physics. The physical content of this sector
is its *continuum identification*: the commutator of two boost generators is a
rotation, [K_x, K_y] = −iJ_z. So the antisymmetric channel is the **spin-1
rotation** sector — orthogonal to the symmetric spin-2 shear, and exactly the
orientation-reversing circulation sector Paper 42's no-go bars (det(JR) = −1, the
twisted-mirror obstruction). Two cautions, stated plainly: (i) the lattice kernels
are only *approximately* the continuum boost generators (Bisognano–Wichmann is a
continuum theorem; finite L, m² = 10⁻⁴, discretization and the floor regulator add
corrections), so [K_A, K_B] = −iJ_z is a continuum-limit *identification*, not a
verified lattice equality; (ii) the vanishing of B_AB · S is forced by matrix
antisymmetry, not by the kernel literally being J_z. The rigorous, lattice-exact
fact is the selection rule; the J_z reading is the continuum interpretation that
ties it to Paper 42's barred sector.

**The symmetric sector — the contingent question.** C_AB is symmetric and *can*
couple to the symmetric spin-2 shear (sym · sym ≠ 0 in general). Whether it *does*
— whether adding the second boost direction opens a spin-2 channel a single
direction lacks — is not fixed by any identity. It is a genuine lattice
measurement, and it is what decides the verdict (§4).

There is also a scope point on the alternative route. The way a *ball* congruence
recovers linearized Einstein — FGHMVR's entanglement-equilibrium (δS_EE = δ⟨K⟩ for
balls of all sizes) — is **holographic**: the Einstein equation emerges in a *bulk*
dual, with δS_EE the bulk area and δ⟨K⟩ the boundary stress. The record lattice is
the boundary theory; it has no bulk, so there the first law holds at first order
with no residual and constrains nothing. This route is gated, not built (§5).

---

## 3. The instrument and its calibration

We use the 2D free-scalar chassis of Paper 52. The modular **kernels** are
computed in **mpmath at dps 80** (≈266 bits) — this is the precision-critical
step: the Williamson reduction's F(ν) = log((ν+½)/(ν−½)) diverges as ν → ½, and
the deep-bulk modes run there (min(ν−½) reaches 1.1×10⁻⁵³ at L=20), so the
eigendecomposition and F(ν) evaluation must be dps-80 to resolve them. The kernels
are then cast to float64, and the **congruence products and contractions
(K_A K_B, the commutator, the source contractions) are float64**. This is a sound
float-safe use: the kernels are well-conditioned, the decisive C_AB signal is
O(1), and the products carry no F(ν) divergence. (The one cancellation object, the
commutator B_AB, gives a value at the float64 roundoff floor ~5×10⁻¹³ — but its
true value is zero by the selection rule, so float64 is adequate there too.) The
claim is therefore precise: **dps-80 for kernel construction, float-safe float64
for the congruence algebra** — not "dps-80 for the whole chain."

The congruence is A = {x ≥ j}, B = {y ≥ j} sharing the overlap corner; the kernels
K_A, K_B are lifted to the global field space; C_AB and B_AB are formed; the
polarized traceless source S(θ) = cos2θ·S_+ + sin2θ·S_× (pure field-sector, no π,
trace = 0) is priced and normalized by the trace (energy) charge — the
spin-2-to-energy ratio R2.

**Instrument receipts.**
- *Positivity:* all ν ≥ ½ across both regions and all lattices.
- *Has curvature:* ‖[K_A, K_B]‖ ≠ 0 — the flows genuinely do not commute.
- *Trace-null:* a pure-trace source gives machine-flat congruence response
  (cos2θ/mean < 10⁻⁹) — no spurious angular structure manufactured.
- **The symmetric channel is live (the spin-2 dead-instrument disarm).** C_AB
  carries a nonzero energy (trace) charge — it is the denominator of the C_AB R2
  (3.85% / 1.45% / 4.62% across the ladder, all nonzero) — so C_AB is a *working*
  instrument for symmetric input. Its spin-2 coupling falling below the same-cut
  baseline is therefore a structural statement about the spin-2 sector, not the
  silence of a dead operator. (A separate **CAL-LIVE** contrast — the commutator
  responds −10.55 to an antisymmetric rotation probe while a single region gives
  5×10⁻¹⁶ — is *symmetry-forced* and certifies only that the spin-1/rotation
  channel is open; it does not bear on the symmetric spin-2 channel and is reported
  as a wiring check on the rotation sector, not as the decisive control.)

---

## 4. The decisive measurement: the symmetric cross-excess

The verdict is decided in the symmetric sector. Across a matched-depth refinement
ladder we report the single-region R2 (the Paper-52 baseline), the symmetric cross
coupling C_AB R2, the same-cut baseline ½(K_A² + K_B²) R2, and the **cross-excess**
(C_AB R2 minus the same-cut baseline) — the genuine new-direction (not
single-region) signal. The antisymmetric Berry amplitude is listed only as the
selection-rule consistency check.

| L | min(ν−½) | single R2 | C_AB R2 | same-cut baseline | cross-excess | Berry (selection-rule check) |
|---|---|---|---|---|---|---|
| 12 | 3.9×10⁻³¹ | 6.09×10⁻² | 3.85×10⁻² | ~0.33 | **−0.295** | 7×10⁻¹⁵ |
| 16 | 2.2×10⁻⁴² | 6.85×10⁻² | 1.45×10⁻² | ~0.36 | **−0.345** | 1.5×10⁻¹⁴ |
| 20 | 1.1×10⁻⁵³ | 1.12×10⁻¹ | 4.62×10⁻² | ~0.49 | **−0.444** | 3.0×10⁻¹⁴ |

The decisive fact is contingent and lattice-measured: **the cross-excess is
negative at every lattice and grows more negative under refinement**, −0.30 →
−0.35 → −0.44. The symmetric cross coupling does not merely fail to exceed the
same-cut baseline — it falls *below* it, and falls further as a→0. Adding the
second boost direction opens no new spin-2 channel; the cross coupling is weaker
than what a single direction's kernel-square already supplies (and that baseline
is itself only the Paper-52 energy-displacement artifact, not a spin-2 charge). So
FORK G fires on the operative criterion: the congruence does **not** exceed the
baseline → GEOMETRY-BLIND.

The Berry column is machine-zero by the selection rule (§2), as it must be; it
carries no independent weight and is shown only to confirm the antisymmetrization
is correct. (A note on framing: the single-region R2 *grows* mildly under
refinement — this is the Paper-52 energy-displacement moment, an artifact of the
anisotropic source's boost-weighted energy, not a spin-2 coupling; it is not, and
is not presented as, the "inverse of P52's collapse." The load-bearing statement
is the *symmetric cross-excess staying below baseline*, which is normalization-
robust because the same-cut baseline uses the same kernel-square construction.)

---

## 5. Scope and no-go

The traceless spin-2 shear is a *symmetric*, volume-preserving strain
(det = +0.75 for the example deformation) — outside Paper 42's antisymmetric
circulation no-go, on the open exact-Williamson route. But the congruence's one
new *antisymmetric* object [K_x, K_y] → J_z is precisely the det(JR) = −1 rotation
sector that no-go bars. So the new structure the congruence supplies in the
antisymmetric channel is the barred sector, and the open (symmetric, spin-2)
channel receives nothing beyond the single-direction baseline.

**Declared GATED — untested, not refuted** (matching Papers 50/51/52):
- The **ball-family (FGHMVR)** entanglement-equilibrium route — and its
  holographic Einstein recovery, which needs a bulk the record lattice lacks (§2).
- The **Lorentzian / boosted timelike-separated** region pair. The spatial
  congruence's antisymmetric curvature vanishing is consistent with the Paper-49
  zero-law block structure; a genuine spin-2 signal, if it exists, may require the
  boost (timelike) direction, which is the Paper-51 gated dynamical sector. **The
  boost-angle-sweep of the symmetric cross-coupling on a Lorentzian region pair is
  the one experiment that could flip this verdict to VISIBLE/MIXED;** it is named
  here and gated.
- The **second-variation (Raychaudhuri / focusing)** object — the genuine
  entropy-focusing quantity, which this operator-product congruence does not build.
- **Nonlinear Einstein**, the **GR coefficient** (Paper 50's ν is l_c-consistent,
  not converged), and **back-reaction**.

---

## 6. The demarcation (on the static side) is complete

Three independent probes locate the same wall:

| probe | reaches | blind to |
|---|---|---|
| Paper 51 (dynamics) | the generic centrifugal-barrier multipole law P_ℓ ∼ Ω^(2ℓ+2) | gravitational quadrupole dominance |
| Paper 52 (single-region charge) | T₀₀ (energy), T₀ᵢ (momentum, via flow) | T_ij^TL (spin-2) |
| Paper 53 (static two-wedge congruence) | the rotation/spin-1 antisymmetric sector | T_ij^TL (spin-2) in the symmetric channel |

The scalar record-dynamics program reaches all of *matter* — the full
energy–momentum content — and, on the static side, stops at the graviton. The
single-region charge, the boost flow, and the static two-wedge congruence between
them exhaust what the static scalar machinery prices, and the traceless spin-2
stress is orthogonal to all of it (the antisymmetric channel by a selection rule,
the symmetric channel by the measured below-baseline cross-excess). Spin-2
requires what the static scalar lattice lacks — an emergent holographic bulk, or
the Lorentzian/dynamical sector — both gated. This is the structurally correct
division of labor (the matter side terminates at energy–momentum, where Jacobson
places the boundary) and the honest terminal statement of the geometry side: **on
the static side, the program is capped at the scalar energy–momentum first law.**

---

## 7. Verdict

**FORK G: GEOMETRY-BLIND** (for the static, two-wedge, spatial congruence). The
congruence supplies two new cross-region objects, and neither carries the spin-2
graviton. The *antisymmetric* commutator is the rotation sector — orthogonal to
the symmetric spin-2 shear by an exact selection rule (antisym · sym = 0), with
[K_x, K_y] → −iJ_z the continuum identification placing it in Paper 42's barred
det(JR) = −1 circulation sector. The *symmetric* cross channel — the one place
spin-2 could live — is a live instrument (nonzero energy charge) whose spin-2
coupling, measured on the lattice, falls *below* the same-cut baseline and falls
further under refinement (cross-excess −0.30 → −0.44): adding the second boost
direction opens no spin-2 channel. The ball-family, Lorentzian-pair, and
second-variation routes are gated — untested, not refuted — with the
boost-angle-sweep on a Lorentzian region pair named as the experiment that could
flip the verdict. With that scope, the demarcation is complete: single region (P52)
and static two-wedge congruence (P53) are both blind to spin-2; the program
reaches all of energy–momentum and stops at the graviton, which requires an
emergent holographic bulk (absent) or the Lorentzian/dynamical sector (P51,
gated). On the static side, the scalar record-dynamics program is capped at the
energy–momentum first law.

---

### Canonical receipts

The campaign `code/v6_p53_congruence_campaign.py` (modular kernels mpmath dps 80,
congruence algebra float-safe float64, no RNG, bit-identical rerun modulo
wall-clock annotations) emits the ledger. Flags (computed): positivity (ν≥½);
has-curvature (‖[K_A,K_B]‖≠0); trace-null (cos2θ/mean < 10⁻⁹). The **load-bearing
result** is the symmetric cross-excess (C_AB R2 minus same-cut baseline): negative
at every lattice and growing under refinement, −0.295 → −0.345 → −0.444, so the
congruence does not exceed the baseline and FORK G fires GEOMETRY-BLIND. Reported
as analytic consistency checks (not contingent measurements): the Berry traceless
amplitude (antisym·sym = 0 selection rule, ~float64 roundoff floor) and the
antisymmetric CAL-LIVE contrast (symmetry-forced, certifying only the rotation
channel is open). The symmetric channel's liveness is the nonzero C_AB energy
charge. Precision: dps-80 is load-bearing for the kernel construction (resolving
min(ν−½) to 1.1×10⁻⁵³ at L=20); the regulator floor is inactive at every tested
lattice (an underflow safety net, not a binding precision test). Scope:
GEOMETRY-BLIND is for the static two-wedge spatial congruence; the ball/Lorentzian/
second-variation routes are gated.
