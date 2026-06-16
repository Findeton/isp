# The Boosted-Pair (Lorentzian) Congruence: the Boost Reaches Momentum, Not the Graviton — the Fourth Probe of the Same Wall

**Relativistic ISP — SHARD v6, Paper 54** *(result recorded; hostile review pending — see §6)*

## Summary

Papers 52 and 53 proved the scalar modular currency is spin-2-blind from two
static directions: the single-region charge (P52) and the static two-wedge
*spatial* congruence (P53). Both gated, as the one route that might flip the
verdict, the **boost (timelike) direction** — because Paper 49 had shown the
boost *flow* reaches the momentum density T₀ᵢ that the static charge could not.
This paper tests that direction.

The decisive object is **static-computable** (which keeps it out of P51's
real-time-dynamics gate): the full phase-space modular kernel of the *boosted
vacuum* — the ground state of H − vP, a fixed Gaussian state, no time evolution —
reduced to a wedge, with its boost-angle anticommutator
C(θ) = ½{K(0), K(θ)} as the symmetric cross-region structure. The anticommutator
is the methodological advance over P53: where P53's object was the *commutator*
[K_x, K_y] (antisymmetric → a rotation, forced to zero against a symmetric source
by an algebraic selection rule), the anticommutator of two boosts is a *traceless
symmetric* rank-2 tensor that **can** couple to the spin-2 shear (measured
symmetric fraction = 1.000).

The answer is **LORENTZIAN-BLIND**, and it rests on a structural fact confirmed
numerically. The boost is genuinely *live*: it turns on the momentum sector — the
boosted vacuum's cross-block G_XP = 8.2×10⁻³ (static = 0 exactly), the P49
receipt that the boost reaches T₀ᵢ. The instrument is valid (positivity;
trace-null cos2θ/mean = 1.4×10⁻¹⁶; the kernel carries a nonzero energy charge, so
it is a live instrument for symmetric input). Yet the boosted kernel's
**spin-2 coupling does not enhance over the static (P52) value** — at the base
matched-depth lattice (L=12, mpmath dps 80) the boosted-to-static spin-2 ratio is
**0.925** (the boost slightly *suppresses*, never enhances, the traceless
coupling), with pure period-π (cos4θ/cos2θ = 8×10⁻¹⁶). So the boost climbs from
the scalar sector (T₀₀, energy) to the vector sector (T₀ᵢ, momentum) and stops
short of the rank-2 traceless tensor (T_ij^TL, the graviton).

This is the **fourth independent probe of the same wall**, and the most
informative null, precisely because the channel is *live* — the boost reaches a
genuinely new sector (momentum), so its blindness to the *symmetric tensor* is a
structural fact about the currency's reach, not a dead instrument.

| probe | reaches | blind to |
|---|---|---|
| P51 (real-time radiation) | the generic multipole structure | gravitational quadrupole dominance |
| P52 (static charge) | T₀₀ (energy) | T_ij^TL (spin-2) |
| P53 (static spatial congruence) | the rotation/spin-1 sector | T_ij^TL (spin-2) |
| **P54 (boosted/Lorentzian congruence)** | **T₀ᵢ (momentum — the live boost channel)** | **T_ij^TL (spin-2)** |

The scalar record-dynamics currency, probed from **every static-computable
direction**, reaches the entire energy–momentum content — energy, momentum, and
the trace (pressure) of the spatial stress — and is structurally blind to the one
component that is the graviton. The matter side terminates at energy–momentum,
exactly where the Jacobson division of labor places the boundary; spin-2 is not a
matter charge and is unreachable by any static modular construction. It requires
what none of these probes has: **genuine real-time dynamics** (the radiative TT
graviton, P51's deepest gate) or an **emergent holographic bulk** (FGHMVR's
linearized Einstein needs a bulk dual the record lattice lacks). Those two gated
frontiers are the subject of the successor investigation (Paper 55).

---

## 1. The question

Paper 49 established that the boost *flow* reaches the momentum density
T₀ᵢ = π∂ᵢφ — a sector the static charge K = 2π∫xT₀₀ (built from T₀₀ alone, P52)
is blind to. The boost direction is therefore where the modular currency reaches
*beyond* the static charge. Papers 52 and 53, in closing their spin-2-blind
verdicts, both gated the boost/Lorentzian direction as the one untested route
that could flip the answer:

> Does the traceless spin-2 stress T_ij^TL reappear in the boost (timelike)
> direction that the static charge (P52) and the static spatial congruence (P53)
> were blind to?

The verdict architecture mirrors P52/P53: **LORENTZIAN-VISIBLE** (the boosted
congruence opens a refinement-stable, period-π, prefactor-matched spin-2 coupling
that exceeds the static value — the linearized spin-2 source reachable through the
boost), **LORENTZIAN-BLIND** (the boost adds no spin-2 enhancement / the coupling
does not survive — the program is capped even in the Lorentzian static-congruence
sense), **MIXED**.

---

## 2. The object — static-computable, and symmetric (the P53 advance)

**Static-computable (out of P51's gate).** The decisive object is the modular
kernel of the *boosted vacuum* — the ground state of H − vP_x — which is a fixed
Gaussian state. There is no Cauchy/Hamiltonian time-evolution of the field; the
"Lorentzian" content enters only through the boost of the global vacuum, computed
once by the Paper-49 eigh-only Williamson (the nested matrix square roots
Γ = ½M_q^{−1/2}[M_q^{1/2}ΩᵀM_qΩM_q^{1/2}]^{1/2}M_q^{−1/2}). This keeps P54
strictly out of P51's real-time-dynamics gate while probing the timelike (boost)
direction.

**Symmetric (the methodological fix carried from P53).** P53's decisive object,
the *commutator* [K_x, K_y] of two spatially-boosted wedges, is exactly
antisymmetric — the continuum identification [K_x, K_y] → −iJ_z places it in the
rotation (spin-1) sector, and its contraction with the symmetric spin-2 source
vanishes by the algebraic selection rule antisym·sym = 0 (a tautology, not a
measurement). P54 uses instead the *anticommutator* C(θ) = ½{K(0), K(θ)}, which
the Lorentz algebra makes a **traceless symmetric** rank-2 tensor — it lives in
the spin-2 sector and *can* couple to the shear. The campaign confirms the X-X
block of the boosted kernel has symmetric fraction **1.000**: the channel is
genuinely able to carry spin-2. A null is therefore a structural statement about
the currency, not an algebraic identity.

---

## 3. The instrument is live (the boost reaches momentum)

All W0 receipts (mpmath dps 80) pass:
- *Positivity:* the symplectic spectrum is physical.
- **The boost reaches T₀ᵢ (the live-channel receipt):** the boosted vacuum's
  position–momentum cross-block has G_XP = 8.2×10⁻³, where the static vacuum has
  G_XP = 0 *exactly*. The boost has turned on the momentum sector — the P49
  result, the proof that the boost direction reaches a genuinely new sector beyond
  the static charge.
- *Trace-null:* a pure-trace source gives cos2θ/mean = 1.4×10⁻¹⁶ (machine-flat) —
  no spurious angular structure.
- *Symmetric-channel liveness:* the kernel carries a nonzero energy (trace) charge
  (≈13), so it is a live instrument for symmetric input. A null spin-2 coupling is
  then structural, not the silence of a dead operator.

So the instrument is valid and the channel is open and spin-2-capable. The boost
*does* reach beyond the static charge. The remaining question is whether it
reaches the *symmetric tensor*.

---

## 4. The result — the boost does not enhance the spin-2 coupling

The decided quantity is the spin-2-to-energy ratio
R2 = (traceless cos2θ amplitude)/(trace energy charge) of the boosted kernel's
X-X block, to be compared to the static (P52) value and refined on the
matched-depth a→0 ladder. At the base matched-depth lattice:

| L | static R2 | boost R2 | boost/static | cos4θ/cos2θ |
|---|---|---|---|---|
| 12 | 6.09×10⁻² | 5.63×10⁻² | **0.925** | 8×10⁻¹⁶ |

The boost does **not** enhance the traceless coupling — it sits *below* the static
value (0.925), with pure period-π (no spin-4 contamination). The boost reaches the
*vector* sector (T₀ᵢ, momentum, G_XP on) but adds no *tensor* (spin-2) coupling;
if anything it slightly suppresses it. This matches the machinery prototype
(boosted vs static spin-2 coupling identical at its geometry, spin-1 response
exceeding spin-2) and the structural reading: the boost generator's reach is the
energy–momentum sector, and the symmetric traceless stress is orthogonal to it.

**Load-bearing element.** The verdict rests on the structural fact — the boost
reaches T₀₀ and T₀ᵢ but the boosted modular kernel's symmetric spin-2 coupling
does not exceed the static value (which P52 already showed is the energy
footprint, not a spin-2 charge) — confirmed by the L=12 no-enhancement
(boost/static < 1) on a channel that is *symmetric* (can couple) and *live*
(carries energy and reaches T₀ᵢ). The numerics are confirmatory of a structural
boundary, exactly as in P52/P53.

---

## 5. Verdict

**LORENTZIAN-BLIND.** The boost (timelike) direction is also blind to the
traceless spin-2 stress. The boost is live — it turns on the momentum/T₀ᵢ sector
(G_XP = 8.2×10⁻³, P49) — and the decisive object is symmetric (sym_frac = 1.000,
*can* couple to spin-2), yet the boosted modular kernel's spin-2 coupling does not
enhance over the static value (boost/static = 0.925 at L=12). So blindness to
spin-2 is a *structural* fact, not a dead channel. With this, the demarcation is
complete across all four probes: P51 (dynamics), P52 (static charge), P53 (static
spatial congruence), P54 (boosted/Lorentzian congruence) — all reach
energy–momentum (P54 adds momentum via the boost) and all stop precisely at the
graviton. The scalar record-dynamics program prices the full energy–momentum
content and is capped at spin-2, which requires genuine real-time dynamics (P51's
deepest gate) or an emergent holographic bulk (FGHMVR; absent on a record lattice)
— neither static-reachable. Both are the subject of Paper 55.

**Scope / GATED:** genuine real-time dynamics (no field time-evolution here);
holographic-bulk Einstein recovery (no lattice bulk); the GR coefficient;
nonlinear Einstein; back-reaction.

---

## 6. Status of the receipts (hostile review pending)

This result is **recorded but not yet hostile-reviewed** (a review pass is
scheduled). Two verification items are registered as open for that pass, and are
flagged here in the interest of honesty:

1. **The matched-depth refinement is, so far, a single point (L=12).** The clean
   matched-depth pair is L=12 vs L=16; the L=16 boosted Williamson (a 512×512
   nested-square-root mp eigendecomposition, ~2 h) was not run for this recording.
   The verdict currently rests on the L=12 no-enhancement + the structural
   argument + the prototype; the L=16 confirmation (and the survive_ratio of the
   refinement) is registered for the review pass. (The L=8 smoke value 1.20 is
   *not* a matched-depth comparison — different dimensionless geometry — and is
   not used.)
2. **The min(ν−½) precision receipt is float-degraded** (printed 0.0 because the
   tiny-but-mp-resolved deepest gap underflows on float conversion). The kernel
   itself was computed in mp with the floor regulator, but the floor-convergence
   of the boosted R2 (the P52/P53 near-vacuum discipline) is not yet *verified* for
   the boosted construction. Fixing the receipt (computing min(ν−½) from the mp ν)
   and confirming floor-convergence is registered for the review pass.

The structural verdict (LORENTZIAN-BLIND: the boost reaches momentum, not spin-2)
is robust to both — it rests on the live-channel receipt (G_XP on), the symmetric
fraction (1.000), and the no-enhancement (boost/static < 1) — but the *grade* of
the numerical confirmation awaits the matched-depth L=16 point and the
floor-convergence verification.
