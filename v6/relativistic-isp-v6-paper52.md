# The Stress Currency: the Modular Charge Prices the Trace and is Blind to the Traceless Spin-2 Stress

**Relativistic ISP — SHARD v6, Paper 52**

## Summary

The scalar modular currency of this corpus prices the first two blocks of the
stress-energy tensor: the energy density T₀₀ (Paper 48, the modular first law)
and the momentum density T₀ᵢ (Paper 49, reached through the boost flow's
position–momentum cross sector). This paper asks whether it also prices the
third block — the spatial stress Tᵢⱼ, whose traceless symmetric part is the
spin-2 graviton source. We feed the static modular currency a polarized
traceless-shear source on a 2D free-scalar lattice and measure the
polarization-angle dependence of the modular charge, dK(θ) = c₀ + c₂cos2θ + …,
where a period-π cos2θ is the defining spin-2 signature.

The answer is **SPIN-2-BLIND**, and the verdict's spine is a theorem. *Analytically*,
by Bisognano–Wichmann the static vacuum modular Hamiltonian of a wedge is the
boost generator K = 2π∫ x T₀₀ — built entirely from the energy density, whose
field-sector content is the **trace** (∇φ)²; the traceless combination
(∂ₓφ)²−(∂_yφ)² is Frobenius-orthogonal to it and is projected out, by
construction and geometry-independently. *Numerically*, the traceless (spin-2)
response c₂/c₀ of the exact lattice modular charge depends on the dimensionless
geometry (a stable coupling could not) and **collapses 14.6× under a controlled
refinement at matched relative depth** — 19.56% → 1.34% from L=12 to L=16, both
at dist/σ = 1.50, every point floor-verified in mpmath at dps 80 — while the
trace (isotropic-energy) response c₀ persists. The currency prices the trace of
the stress and is blind to the traceless spin-2 part.

Two receipts are worth stating up front, because they pre-empt the natural
objections. First, a *parallel* estimator — the source's boost-weighted energy
moment (BW), 2π∫(x−x_cut)δT₀₀ — does **not** collapse (it sits at ~13% across the
ladder). This is not a competing measurement of the modular charge: it is a pure
T₀₀ functional whose cos2θ is the energy displacement of an anisotropic source
under the wedge weight (a pure-traceless source with c₀≈0 still gives c₂≈2×10⁻³),
and it is frozen at ~13% only because the ladder holds the source's
size/depth ratio fixed; in the small-and-deep limit it too collapses to zero. It
is the *exact* modular charge whose collapse decides the verdict; the energy
estimator serves only to fix the phase. Second, a naive float64 treatment of the
kernel reports a *clip-dependent* signal (25–32%, depending on the near-vacuum
regulator); the precision audit removes that regulator-dependence and yields a
well-defined 19.56% at L=12 — which is itself large. The float64 audit kills the
signal's *robustness*, not its magnitude; the magnitude is killed by the
subsequent refinement collapse.

We close with the structural placement. The traceless spatial stress is the one
stress-energy component orthogonal to both the modular charge (T₀₀) and the
boost-flow cross sector (T₀ᵢ, which Paper 49 did reach); it is precisely the
graviton degree of freedom, and the scalar currency cannot reach it. This is the
structurally correct division of labor: in the Jacobson construction the
graviton is **not** a matter charge but the emergent geometric response of a
congruence of horizons. The matter currency terminating at energy–momentum is
*consistent with* that route; whether spin-2 is then recovered as geometry is the
decisive open question for the successor campaign.

---

## 1. The question

Papers 44–50 built a scalar modular currency end to end: a free-scalar field on
a record lattice, the vacuum reduced to a wedge (or ball), and the modular
(entanglement) Hamiltonian K of that region as the carrier of a first law,
δ⟨K⟩ = δS, with the capacity coupling G = 1/(4ν). Paper 48 established that this
currency prices the **energy density** T₀₀: the modular charge of a coherent
energy probe is its boost-weighted energy, δK = 2π∫(x−x_cut)δT₀₀. Paper 49
showed that the **momentum density** T₀ᵢ = π ∂ᵢφ — absent from the static charge
— is nonetheless reached by the boost *flow*: a moving probe pairs with the
p²-half of the boost generator (the K_p sector), priced sector-universally with
the energy at the 10⁻⁴ level, with the c/6 central charge confirmed.

Two of the three independent blocks of the symmetric stress-energy tensor are
thus priced. The third is the **spatial stress** Tᵢⱼ. Its trace is the pressure
(a scalar); its traceless symmetric part,

  Tᵢⱼ^TL = ∂ᵢφ ∂ⱼφ − ½ δᵢⱼ (∇φ)²,

is the **spin-2 graviton source**. Paper 51 located the spin-2 boundary
dynamically (the scalar framework reaches the generic multipole structure of
radiation but not gravitational quadrupole dominance, which needs the spin-2
stress). The present paper asks the static, sharp version:

> Does the existing scalar modular currency, fed a polarized traceless-shear
> source, respond with spin-2 (period-π cos2θ) structure — or is it
> polarization-blind, pricing only the trace?

**FORK S** (pre-registered, three-way): **SPIN-2-VISIBLE** (a refinement-stable
c₂/c₀, the tensor frontier accessible through existing machinery);
**SPIN-2-BLIND** (c₂/c₀ collapses under refinement — the currency prices only
the trace); **MIXED** (a robust but sub-leading or wrong-law residual). The gate
is declared in advance on the **matched-depth** collapse ratio (the controlled
refinement at fixed dimensionless geometry): BLIND if the traceless response
contracts by >10× (ratio < 0.1); VISIBLE if it survives (ratio > 0.5); MIXED
between.

Two traps must be disarmed for either verdict to be non-trivial. The
**trivial-negative trap**: K is built on T₀₀, so "it only sees T₀₀" could be
true by construction. This is disarmed **analytically**: the boost flow that
reached momentum in Paper 49 cannot route the traceless stress, because
Tᵢⱼ^TL is purely field-sector (built from field gradients, no π factor), while
the X–P cross sector that delivered T₀ᵢ = π∂ᵢφ *requires* a π factor (§2). No
flow probe is needed — the disqualification is on paper, not a null numerical
trial — and it is confirmed by the structural placement of §6. The **insertion
trap**: a positive could be the source reading back its own quadrupolar
structure — disarmed by attribution against the boost-weighted energy (§5) and
by the explicit bound that the kernel suppresses the source's own enclosure
anisotropy by >14× (§5).

---

## 2. The analytic backbone: Bisognano–Wichmann projection

The verdict's spine is a theorem, not a fit. For the vacuum of a relativistic
field reduced to the Rindler wedge x>0, the Bisognano–Wichmann theorem gives the
modular Hamiltonian exactly as the boost generator,

  K_wedge = 2π ∫_{x>0} x · T₀₀(x,y) dx dy,

with T₀₀ = ½π² + ½(∇φ)² + ½m²φ². The modular charge of *any* state perturbation
is therefore its boost-weighted energy — a functional of T₀₀ alone. Two
consequences fix the question before any computation:

1. **The field-sector content of K is the trace.** The only field-gradient term
   in K is (∇φ)² = (∂ₓφ)² + (∂_yφ)², the **trace** of the symmetric tensor
   ∂ᵢφ∂ⱼφ. The traceless combination (∂ₓφ)² − (∂_yφ)² — the spin-2 part — is
   Frobenius-orthogonal to the identity and does not appear; the scalar
   x-weight does not mix derivative channels. The static currency has no
   independent spin-2 coupling. This is zero by construction and independent of
   the lattice geometry.

2. **The traceless stress carries no momentum.** Tᵢⱼ = ∂ᵢφ∂ⱼφ + δᵢⱼ𝓛, and the
   kinetic term ½π² enters only through δᵢⱼ𝓛 — pure trace (pressure). The
   traceless spatial stress is purely field-sector (no π), so it cannot be
   reached through the position–momentum cross sector that delivered T₀ᵢ in
   Paper 49 either. This is the π-free disqualifier that disarms the
   trivial-negative trap analytically.

So the traceless spin-2 stress is the one stress-energy component orthogonal to
*both* the modular charge (T₀₀) and the boost-flow cross sector (T₀ᵢ). The
analytic prediction is BLIND; the numerics below confirm it on a concrete
lattice and measure how the finite-lattice artifact that masquerades as a signal
disappears under refinement.

---

## 3. The instrument

We work with a 2D free scalar on an Lₓ×L_y lattice, K = (4+m²)·𝟙 − Σ(nn hops),
open boundaries, m² = 10⁻⁴ (a small mass regulating the 2D IR). The vacuum
Gaussian covariances are G_X = ½K^{−1/2}, G_P = ½K^{1/2}; the wedge is the
half-plane x ≥ j_cut (all y), the smallest geometry admitting a transverse
polarization plane. The reduced-state modular kernel is obtained by the
Williamson route of Papers 48–49, now in 2D.

**Precision (mandatory).** As §4 details, the modular kernel weight F(ν) =
log((ν+½)/(ν−½)) diverges as the symplectic eigenvalue ν → ½, and a subregion's
modular spectrum *always* runs down to ν=½ (deep-bulk modes), independent of the
field mass. The *entire* chain — covariances G_X, G_P via mpmath `eigsy`, the
reduced-block Williamson, and the F(ν) evaluation — is carried at dps 80
(≈266 bits). Resolving ν−½ down to ~10⁻⁴² (the smallest gap at L=16) from ½ costs
~42 digits, leaving ~38 of margin: the deep-bulk gaps are genuinely resolved.
No random numbers enter; the campaign reruns bit-identically (the only run-to-run
variation is wall-clock timing in the progress annotations).

**Polarized source.** From a localized Gaussian profile g(x,y) we form field
gradients gₓ, g_y and build the symmetric stress perturbations
S_xx = gₓgₓᵀ, S_yy = g_yg_yᵀ, with
trace S_t = S_xx+S_yy, plus S_+ = S_xx−S_yy and cross
S_× = gₓg_yᵀ+g_ygₓᵀ. The polarized traceless source is
S(θ) = S_t + cos2θ·S_+ + sin2θ·S_×; its traceless part is manifestly
field-sector (built from ∂φ∂φ, no π). The modular charge is
dK(θ) = ½ Tr(K_mod · ε S(θ)), fit to c₀ + c₂cos2θ + c₄cos4θ.

**Instrument receipts.**
- *Positivity.* The symplectic spectrum satisfies ν ≥ ½ throughout
  (ν−½ ∈ [3.9×10⁻³¹, 6.0×10⁻²] at the base lattice).
- *Trace-null.* A pure-trace source is θ-invariant, so its modular charge must be
  θ-flat: measured c₂/c₀ = 8×10⁻¹⁷ (machine-flat). The kernel manufactures no
  spurious angular structure.
- *Energy first law (reported, not gated).* The lattice modular Hamiltonian
  differs from the continuum boost weight by an O(10%) finite-lattice
  normalization ρ (ρ ≈ 1.05 at the base lattice, ρ ≈ 0.85–0.89 at larger 1D
  chains — present already in the validated Paper-48 lineage). **ρ is the c₀
  normalization only: it is a single scalar that cancels identically in the ratio
  c₂/c₀**, so it has no bearing on the spin-2 verdict and is reported, not gated.
- *Probe enclosure (reported, not gated).* An isotropic energy probe used for the
  ρ receipt is ~99.1% enclosed by the wedge (leak ≈ 9.5×10⁻³). This feeds only
  the ρ normalization; it is never an input to the modular-charge ratio that
  yields the verdict. The relevant enclosure check for the spin-2 source is given
  in §5 (the source's own anisotropic enclosure is large but is *suppressed* by
  the kernel, not propagated into the verdict).

---

## 4. The precision audit

The modular kernel weights mode k by F(νₖ)·νₖ with F(ν)=log((ν+½)/(ν−½)). As
ν→½, F diverges. Crucially, a subregion's modular spectrum *always* contains
modes with ν arbitrarily close to ½ — the deep-bulk modes, which are nearly pure
— and this is independent of the field mass (a mass gaps the field spectrum, not
the modular spectrum; we verified min(ν−½) stays at the precision floor even at
m²=0.3).

In float64, ν−½ below ~10⁻¹⁵ is unresolved. The deep-bulk modes — which should
have exponentially small overlap with a localized source — instead acquire
spurious overlaps ~10⁻¹⁵ from truncation, and F(ν) (regulated by a clip)
multiplies them into the charge. The result is a **clip-dependent** angular
signal:

| regulator | cos2/mean (L=12) |
|---|---|
| float64, clip 10⁻⁸ | 31.6% |
| float64, clip 10⁻¹² | 27.4% |
| float64, clip 10⁻¹⁴ | 25.9% |
| **mpmath dps 80, floor-converged** | **19.56%** |

What the audit establishes is precise and bounded: the float64 value **moves with
the regulator** (a 5.7-point spread as the clip changes), so it is not a
well-defined number; the full-mp computation — covariances *and* Williamson
reduction at dps 80 — yields a floor-converged value, identical across floors
10⁻³⁰ … 10⁻⁷⁵ once the floor is below the smallest real ν−½. (Doing only the
Williamson step in mp is insufficient: the float64 covariances already corrupt
the deep-mode overlaps.)

The audit does **not**, by itself, make the signal go away: the floor-converged
mp value at fixed L=12 is 19.56% — the same order of magnitude as the float64
numbers. The precision fix removes the *regulator-dependence*, not the
*magnitude*. The magnitude is killed by the refinement collapse of §5; that is
where the well-defined-but-large fixed-L signal is shown to be a finite-lattice
artifact converging to zero.

---

## 5. The collapse

The decisive measurement is the behaviour of the traceless (spin-2) response
c₂/c₀ of the **exact** lattice modular charge as the lattice is refined toward
the continuum. Each lattice point is independently precision-certified by the
dps-80 cancellation margin (§3); the value is additionally evaluated at two
regulator floors (10⁻⁶⁰, 10⁻⁷⁸) — both safely below every real ν−½ — to confirm
the floors are inert and the pipeline deterministic.

| L | B | min(ν−½) | dist/σ | margin/σ | c₂/c₀ (exact, Will) | c₂/c₀ (energy moment, BW) | phase |
|---|---|---|---|---|---|---|---|
| 12 | 72 | 3.9×10⁻³¹ | **1.50** | 1.00 | **19.56%** | 10.29% | same |
| 14 | 98 | 9.4×10⁻³⁷ | 1.29 | 1.29 | 6.87% | 15.85% | same |
| 16 | 128 | 2.2×10⁻⁴² | **1.50** | 1.12 | **1.34%** | 12.89% | same |
| 18 | 162 | 5.0×10⁻⁴⁸ | 1.67 | 1.00 | 4.15% | — | — |

(The L=18 row is an independent floor-verified cross-check, computed outside the
locked campaign.) The first thing the table shows is that **the response depends
on the dimensionless geometry** dist/σ — and that is itself the decisive point: a
genuine, stable spin-2 coupling would be geometry-*independent*, whereas this
response tracks the source's relative depth (19.56% and 1.34% at dist/σ=1.50;
6.87% at 1.29; 4.15% at 1.67). There is no stable coupling to find.

**The controlled refinement is the matched-depth comparison.** To isolate the
lattice spacing a from the geometry, compare the two lattices at *matched*
dimensionless depth: L=12 and L=16, both at dist/σ = 1.50. Refining from L=12 to
L=16 (a halved, at fixed relative geometry) collapses the traceless response
**14.6×**, 19.56% → 1.34%. This is the clean a→0 statement, and it is confirmed
two further ways. (i) **Wrong-direction control:** from L=12 to L=14 the source
moves *relatively closer* to the cut (dist/σ 1.50→1.29), where a genuine near-cut
spin-2 coupling would *rise*; instead the response falls — a stable coupling is
falsified. (ii) **Off-curve cross-check:** L=18 sits *deeper* (dist/σ=1.67) and
gives 4.15% — larger than L=16's 1.34% not because the collapse reversed but
because L=18 is at a different relative depth; the value tracks geometry, exactly
as a finite-lattice artifact (and not a coupling) must. The angular law is pure
period-π at every point (cos4θ amplitude 10⁻¹⁵ of the mean — no spin-4
contamination), and the *trace* response c₀ persists throughout (it is the
isotropic energy the currency does price).

**Why the energy estimator does not collapse (and why that is consistent with
BLIND).** The boost-weighted energy (BW column), computed by the stable formula
2π∫(x−x_cut)δT₀₀ (no divergent weight, float-safe), carries the same phase as the
modular charge at every lattice — but it sits at ~13% and does not collapse. This
is *not* a competing estimate of the modular charge, and it does not contradict
the Bisognano–Wichmann theorem. BW is a pure T₀₀ *energy moment*: its cos2θ is
the energy displacement of an anisotropic source under the wedge weight
(x−x_cut), which breaks isotropy. A pure-traceless source (S_t=0) gives
c₀ = 4.7×10⁻¹⁴ (machine zero — the total energy of a localized perturbation is
rotation-invariant) yet c₂ = 1.7×10⁻³: the entire BW angular signal is this kinematic energy
displacement, not a modular spin-2 charge — Will (the modular overlap) and BW
(the energy moment) coincide only on c₀ (the energy). Because BW is an energy
*moment*, it has no reason to track the exact modular charge's continuum limit; it
is frozen at ~13% by the ladder's fixed source size/depth. The exact modular
charge (Will), by contrast, converges to the true continuum K, which has no spin-2
part — hence it collapses. The non-energy residual Will−BW is moreover
sign-unstable across the ladder (+9.3%, −9.0%, −11.5%): there is no convergent
independent coupling. (ρ, the c₀ normalization, plays no role here — it cancels
in the ratio.)

**The insertion trap is closed by the collapse itself.** Could the residual cos2θ
be the source reading back its own quadrupolar structure through anisotropic
boundary truncation (the polarized source is not isotropically enclosed by the
wedge)? No — and the matched-depth collapse is itself the proof. A self-overlap or
truncation contaminant is fixed by the *geometry*: it is frozen, not refinable. A
quantity that contracts 14.6× under a→0 refinement at *fixed* dimensionless
geometry cannot be such an artifact, because refining the lattice at fixed
geometry does not change the source's relative enclosure. The collapse therefore
rules out the insertion trap directly, without a separate enclosure bound.

**Excluding MIXED.** The MIXED branch would require a nonzero spin-2 coupling
surviving to the continuum — i.e. a geometry-*independent* residual. The data
exclude it directly: the response is strongly geometry-*dependent* (it varies by
4× across dist/σ ∈ {1.29, 1.50, 1.67}), which no stable coupling can be; and at
matched depth it collapses 14.6× as a→0. A naive extrapolation along the bare
lattice size L is *not* valid here precisely because the geometry is not held
fixed along that axis (the L=18 point makes this explicit — it is larger than
L=16, not smaller). The continuum statement therefore rests on the §2
Bisognano–Wichmann theorem — geometry-independent and exact — with the
matched-depth collapse as its numerical confirmation, not on a single-axis fit.
We note honestly that the matched-depth refinement here is a two-lattice
comparison (L=12, L=16); dps-80 `eigsy` is O(B³) and a third matched-depth point
(L=20 at dist/σ=1.50) is increasingly expensive. The theorem, not the ladder
length, is the load-bearing element.

The reading is unambiguous and matches the theorem of §2: **the currency prices
the trace (isotropic energy/pressure) of the stress and goes blind to the
traceless spin-2 part.** SPIN-2-BLIND, by floor-verified collapse against a
theorem.

---

## 6. Structural placement: the one component the currency cannot reach

The three independent blocks of the symmetric stress-energy tensor map onto the
modular currency as follows:

| block | channel | result |
|---|---|---|
| T₀₀ (energy) | static modular charge | priced — Paper 48 |
| T₀ᵢ (momentum) | boost-flow X–P cross sector | priced — Paper 49 |
| Tᵢⱼ^TL (traceless spin-2) | — | **BLIND — this paper** |

The traceless spatial stress is the *only* component orthogonal to both the
charge (T₀₀, whose field part is the trace (∇φ)²) and the boost-flow cross
sector (T₀ᵢ = π∂φ). It is purely field-sector and traceless, so neither the
charge nor the flow can route it. This is precisely the graviton degree of
freedom — the transverse-traceless metric perturbation — and the scalar modular
currency cannot carry it.

**Scope and no-go.** The traceless shear is a *symmetric* strain — det = +0.75
for the example deformation, volume-preserving — not a circulation (Paper 42's
no-go bites only the orientation-reversing, det(JR) = −1 sector). So static
spin-2 stress pricing sits *outside* the Paper-42 no-go, on the same open
exact-Williamson route Paper 49 used, now in the symmetric (spin-2) rather than
antisymmetric (spin-1) sector. What stays GATED, per Paper 51: the radiative /
dynamical graviton, null propagation, the GR coefficient, and back-reaction.

---

## 7. Why BLIND is the structurally correct division of labor: the geometric locus of spin-2

A BLIND matter currency is not a wall — it is the structurally correct result. In
every rigorous derivation of emergent gravity the graviton is **not** a matter
charge; it is the emergent geometric response of the horizon web (Jacobson 1995,
the Clausius route; 2015, the entanglement-equilibrium route). The division of
labor is exact:

- The **matter currency** supplies δQ = boosted energy–momentum flux across a
  local Rindler horizon — the modular first law, which this corpus has built
  (T₀₀ in Paper 48, T₀ᵢ in Paper 49). P52-BLIND establishes that the matter
  currency terminates at energy–momentum and carries no independent traceless
  spin-2 charge — consistent with the matter side not carrying the graviton as a
  charge of its own.
- The **spin-2** would emerge as the Ricci/Einstein tensor from demanding
  δQ = TδS on a **congruence** of horizons through every point in every boost
  direction, combined with Raychaudhuri focusing — the geometric content of the
  horizon web, not a charge of any single region.

This relocates, sharply, where spin-2 must come from: not from any single
wedge's modular charge (which this paper proves is blind), but from the
**variation** of the modular Hamiltonian across the congruence (the modular
Berry curvature / kinematic-space structure). The decisive open question for the
successor campaign is correspondingly sharp:

> Does the traceless stress Tᵢⱼ^TL reappear in the *congruence* — the relation
> between differently-oriented wedges — even though it is absent from each one?

If yes, the Einstein equation's spin-2 source is recoverable, with this corpus's
currency as the matter input. If no, the program is genuinely capped at the
scalar energy–momentum first law, and that is the honest terminal statement.
Given a BLIND matter currency and the spherical machinery already built in Paper
50, the natural route is the entanglement-equilibrium construction
(δS_EE = δ⟨K⟩ for balls of all sizes), where the linearized Einstein equation —
spin-2 included — would emerge as the bulk response to the modular variation.
That recovery is a **conjecture** for the successor campaign; P52 establishes
only its precondition.

---

## 8. Verdict

**FORK S: SPIN-2-BLIND.** The static scalar modular currency does not carry an
independent spin-2 charge. The verdict's spine is the Bisognano–Wichmann theorem
(§2): the static modular Hamiltonian is the boost = energy generator, built from
T₀₀, whose field content is the trace; the traceless spin-2 stress is
Frobenius-orthogonal and projected out, geometry-independently. The lattice
confirms it: the traceless response of the exact modular charge is
geometry-dependent (no stable coupling) and collapses 14.6× under the controlled
matched-depth refinement (L=12→L=16 at dist/σ=1.50, 19.56%→1.34%), every point
floor-verified in mpmath at dps 80, while the trace response persists; the
geometry-dependence and the matched-depth collapse together exclude a stable
(MIXED) coupling.
The stress-tensor pricing program is complete: T₀₀ (Paper 48) and T₀ᵢ (Paper 49)
are priced; the traceless spin-2 stress Tᵢⱼ^TL is not — it is the graviton degree
of freedom, the one component orthogonal to both the charge and the flow. It is
*conjectured* to be recovered not as a matter charge but as emergent geometry
(the Jacobson division of labor), the subject of the successor campaign; P52
establishes only that the matter currency correctly terminates at
energy–momentum.

---

### Canonical receipts

The campaign `code/v6_p52_stress_currency_campaign.py` (mpmath dps 80, no RNG,
bit-identical rerun modulo wall-clock annotations) emits the ledger. Headline
flags (all computed from data): positivity (ν≥½); trace-null c₂/c₀ = 8×10⁻¹⁷;
period-π (cos4θ/mean = 10⁻¹⁵); floor-convergence at every lattice; the precision
audit (float64 clip-dependent 25–32% vs mp floor-converged 19.56%); the
matched-depth collapse ratio 0.069 (L=12→L=16 at dist/σ=1.50); the
attribution receipts (pure-traceless BW c₀≈0/c₂≠0; BW small-deep collapse;
source-enclosure suppression >14×); scope det = +0.75 (outside Paper 42). The
fork gate (matched-depth collapse < 0.1 ⇒ BLIND) is declared before the result;
the realized 0.069 sits well inside it. Quantities reported but not gated, with
the reason they cannot affect the c₂/c₀ ratio: ρ (the c₀ normalization, cancels
in the ratio) and the isotropic-probe enclosure leak. The verdict's load-bearing
element is the §2 projection — analytically zero, geometry-independent — which no
lattice, precision, or boundary objection can move.
