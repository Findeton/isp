# v12 W1′ — THE THREE-CLASS THEOREM + the anti-correlation exhibit
# + the Δ census (PIN)

**Status:** PIN, STRICT, 2026-07-28.  Supersedes
note-w1-reconstruction-pin.md (whose worker was stopped before
receipt; its questions are answered analytically by the external
review, LOG #3 — this pin turns those answers into theorems with
receipts).  **Binding:** paper 0 v2 §3–§4 (W1′), the review's
constructions verbatim (hand-verified LOG #3).  Lean NONE — every
gate's failure is a first-class finding against the v2 skeleton.

## The unit

- **Arm A — THE CHAIN, exactly.**  Three model classes on CHSH:
  (i) {±1}-factorization: E_ab = u_a·v_b with u_a, v_b ∈ {±1} —
  class maximum 2, proven by exhaustive enumeration (16 sign
  patterns) + the convexity statement; (ii) U(1)-Gram:
  E_ab = Re(z_a·conj(w_b)), z_a, w_b ∈ U(1) — class maximum EXACTLY
  2√2, proven by the unit-circle inequality
  |v₀+v₁| + |v₀−v₁| ≤ 2√2 (derived exactly in-receipt: the
  parallelogram identity + concavity, no floats — work in exact
  algebraic form; exhibit the saturating instance at the Tsirelson
  angles in ℚ(√2)); (iii) no-signaling: maximum 4, exhibited by the
  PR table, with the LP/vertex argument for the bound.  The chain
  2 < 2√2 < 4 with STRICT inclusions exhibited (a Gram instance
  outside the classical polytope; a no-signaling table outside the
  Gram class — prove the PR table admits NO U(1)-Gram
  representation: Re(z·conj(w)) = ±1 forces alignment, derive the
  contradiction exactly).
- **Arm B — THE ANTI-CORRELATION EXHIBIT.**  The review's two
  constructions, in-receipt, exact: (i) the singlet model
  ψ_xy(a,b) = (z_a − xy·w_b)/(2√2): gate
  P(x,y|a,b) = ¼(1 − xy·cos(a−b)) identically at the declared
  algebraic angles, CHSH = 2√2 at the Tsirelson settings, AND the
  natural relative phase g_ab = z_a·conj(w_b) has 4-cycle holonomy
  EXACTLY 1 (coboundary — factorized phases always do; state the
  one-line proof); (ii) the PR edge-phase pattern
  (γ₀₀,γ₀₁,γ₁₀,γ₁₁) = (1,1,1,−1): valid no-signaling table,
  CHSH = 4, 4-cycle holonomy −1.  THE TABLE (trivial class ↔ 2√2;
  nontrivial class ↔ 4) is the unit's engraved exhibit: the v1
  identification anti-correlated with quantumness.
- **Arm C — THE Δ CENSUS.**  The composition defect
  Δ(U₂,U₁) = B(U₂U₁) − B(U₂)B(U₁) on minimal exact examples:
  (i) reproduce [B1]'s interference identification (the cross-term
  identity, gated entrywise on an exact 2×2 and 3×3 pair);
  (ii) census when Δ = 0 exactly (commuting-in-modulus cases;
  permutation factors; the classical family) vs Δ ≠ 0 (the Hadamard
  pair; the DFT pair) — small, exact, both ways; (iii) the record
  connection stated (reporting-only, feeds W3′): conditioning that
  kills Δ on the recorded algebra, exhibited on one worked example
  (a measurement channel between the two steps making the shadow
  compositional — the decoherence identity, exact).
- **Arm D — honesty gates.**  (i) The antecedent attribution gate:
  every theorem used carries its citation ([F]/[AB]/[T]/[W]) in the
  receipt output where used; the unit claims ASSEMBLY + receipts,
  not novelty of the chain.  (ii) The scope gate: no claim about
  nature; no claim that the Gram class IS quantum mechanics (it is
  the correlation-set boundary at this scenario); the
  higher-scenario question (where real-vs-complex separates and
  where the Gram class deviates from the quantum set) is NAMED as
  out of scope, not silently ignored.

## Pre-registered outcomes (lean NONE)

- **W1′-PROVEN:** all three maxima and both exhibits gate exactly —
  the v2 skeleton stands; W2′/W3′ open on the user's word.
- **W1′-BROKEN-AT-⟨class⟩:** any maximum ≠ its claimed value or
  either exhibit fails — the v2 skeleton is wrong at that joint;
  the failure census is the deliverable and the programme halts for
  re-adjudication.

## Receipt rules

Exact arithmetic end-to-end (ℚ(√2), cyclotomics; the 2√2 bound via
exact algebraic inequalities, not numerics); enumeration where the
class is finite; no floats in substantive paths; determinism; caps
printed; substantive negatives exit 0; runtime < ~15 min, progress
prints (no silent interval > 8 min); STRICT, GREEN-UNREVIEWED, no
leans; antecedents cited in-output.

## AMENDMENT (2026-07-28, LOG #4 — the second external review
## [REV2] adopted mid-construction; transparent per house rules)

The construction worker is notified of these amendments by message;
the original arms stand except as amended here.

1. **Arm A CONVEXIFIED:** the three classes are the convex bodies
   L_corr = conv{s_a·t_b}, Q_corr = conv{Re(z_a·conj(w_b))},
   NS_corr = [−1,1]⁴ on the correlator projection; the maxima
   2 / 2√2 / 4 are over the convex bodies (linear functionals
   attain maxima at extreme points — state it).  NEW GATE A+:
   **the completeness of Q_corr** — every supporting hyperplane of
   the general quantum correlator set attains its maximum on planar
   unit vectors (optimal u_a ∈ span{v₀, v₁}, dim ≤ 2): derive
   exactly; the convexified U(1) family IS the quantum correlator
   body at this scenario.
2. **Arm C EXTENDED, two new gates:**
   **C+1 THE THREE-DEFECT SEPARATION** — gate the exact rational
   counterexample: with B(R(θ)) = S(cos 2θ), S(c)S(d) = S(cd)
   (gate both identities symbolically), take U₁ = R(θ₁) with
   (cos θ₁, sin θ₁) = (24/25, 7/25) and U₂ = R(θ₂) with
   (4/5, 3/5): then c₁ = cos 2θ₁ = 527/625,
   c_tot = cos 2(θ₁+θ₂) = −7/25, Δᴮ ≠ 0
   (S(−7/25) ≠ S(7/25 · 527/625) = S(3689/15625)) — YET
   K = S(−175/527) is a valid stochastic matrix with
   K·B(U₁) = S(−175/527 · 527/625) = S(−7/25) = B(U₂U₁): **Δᴮ ≠ 0
   with a stochastic factorization exhibited — Δᴮ, D₂₁₀, and d_div
   are three different objects, gated.**
   **C+2 THE COHERENCE LAW** — gate the identity
   Δᴮ(U₃U₂,U₁) + Δᴮ(U₃,U₂)B(U₁) = Δᴮ(U₃,U₂U₁) + B(U₃)Δᴮ(U₂,U₁)
   entrywise-symbolically on the exact 2×2 and 3×3 pairs already in
   Arm C (both sides = B(U₃U₂U₁) − B(U₃)B(U₂)B(U₁)) — W2a's seed.
3. **Language:** Δ is written Δᴮ throughout and never equated with
   stochastic indivisibility; the note's verdict cites paper 0
   v2.1's three-defect distinction; the record example in Arm C
   (iii) is framed per the v2.1 T3′ (record defined independently;
   record-preserving operations only).
4. Paper 0 v2.1 is the binding text where it and the original pin
   body differ.
