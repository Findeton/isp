# v12 W1′ — THE THREE-CLASS THEOREM, THE COMPLETENESS OF Q_corr,
# THE ANTI-CORRELATION EXHIBIT, AND THE Δᴮ CENSUS

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-28.
**Pin:** note-w1p-three-class-pin.md, including its AMENDMENT of
2026-07-28 (LOG #4, the second external review [REV2] adopted
mid-construction).
**Binding:** paper 0 v2.1 §1 (T2′ Δᴮ and the three-defect distinction;
T3′ records defined independently), §3 (the convexified skeleton and
the completeness target), §4 (W1′, W2a), §5 (non-claims); LOG #3, #4.
Paper 0 v2.1 binds where it and the pin body differ.
**Receipt:** `v12/code/w1p_three_class_exact.py` →
`v12/code/w1p_output.txt`.  20 anchors, **121 gates, 121 pass,
0 fail**; runtime 41.7 s; deterministic across runs.
**Verdict:** **W1′-PROVEN.**

Arithmetic: `fractions.Fraction` for every rational; the cyclotomic
fields ℚ(ζ₈), ℚ(ζ₁₂), ℚ(ζ₁₆) (canonical representation modulo Φ_N, so
tuple equality *is* field equality) for every complex algebraic
quantity; a multivariate polynomial ring over ℚ for every symbolic
identity; ℚ(√2) with an exact sign oracle for every order comparison.
No float in any substantive path; no tolerance anywhere.  Substantive
negatives exit 0; exit 1 is anchor-only.

---

## 1. The chain, over convex bodies

On the CHSH correlator projection, with
P(x,y|a,b) = ¼(1 + xy·E_ab) and S = E₀₀ + E₀₁ + E₁₀ − E₁₁:

    L_corr  := conv{ E_ab = s_a t_b : s_a, t_b ∈ {±1} }
    Q_corr  := conv{ E_ab = Re(z_a conj(w_b)) : z_a, w_b ∈ U(1) }
    NS_corr := [−1, 1]⁴

    L_corr ⊊ Q_corr ⊊ NS_corr,   max S = 2,  2√2,  4.

A linear functional attains its maximum over a compact convex set at
an extreme point, and max over conv(S) = max over S for any S [CVX];
so each body's maximum is the maximum over its generating set.

| body | maximum | proof method | receipt |
|---|---|---|---|
| L_corr | **2** | exhaustive over the 16 sign patterns + linearity over the hull | A1, A6 |
| Q_corr | **exactly 2√2** | four exact polynomial certificates + a saturating instance in ℚ(ζ₈) | A2, A6 |
| NS_corr | **4** | the elementary correlator bound + the cube vertices | A3, A6 |

**(i) 2.**  The 16 sign patterns give 8 distinct correlator vectors;
max S = 2 and min S = −2 on all four CHSH functionals (64 exact
rational evaluations).  Linearity and the bound are gated pointwise
on 3876 exact rational hull points × 4 functionals, weights in
(1/4)ℤ.

**(ii) 2√2.**  Four certificates, each an exact polynomial identity
over ℚ:

- **CERT-0** (the operator regrouping, 8 real variables)
  S = Re(conj(z₀)(w₀+w₁)) + Re(conj(z₁)(w₀−w₁)).
- **CERT-1** (unit-modulus Cauchy–Schwarz)
  (cx+sy)² + (cy−sx)² = (c²+s²)(x²+y²), so with |z| = 1,
  Re(conj(z)u)² ≤ |u|², i.e. S ≤ |w₀+w₁| + |w₀−w₁| =: p + q.
- **CERT-2** (parallelogram)
  |v₀+v₁|² + |v₀−v₁|² = 2|v₀|² + 2|v₁|², so p² + q² = 4.
- **CERT-3** (sum-of-squares)
  8 − (p+q)² = (p−q)² + 2(4 − p² − q²), which on p² + q² = 4 reads
  8 − (p+q)² = (p−q)² ≥ 0, i.e. p + q ≤ 2√2 with equality iff
  p = q = √2.

Attainment: α = (π/4, −π/4), β = (0, π/2), i.e.
(z₀,z₁,w₀,w₁) = (ζ₈, ζ₈⁷, 1, ζ₈²), correlators
(√2/2, √2/2, √2/2, −√2/2) ∈ ℚ(√2), S = 2√2 exactly.  The instance
saturates CERT-3 and realizes the equality case of CERT-1.
Corroboration: the exhaustive π/4 grid, 8⁴ = 4096 quadruples, exact
ℚ(√2) comparison — no point exceeds 2√2 and the grid maximum is 2√2.

**(iii) 4.**  For any normalized non-negative table |E_ab| ≤ 1, so
|S| ≤ 4; this is the complete proof and uses no polytope theory.  The
24 no-signaling vertices [NS] are enumerated exactly and each verified
non-negative, normalized and no-signaling on both wings; local
vertices give max 2, each of the 8 PR vertices attains 4 on one of the
8 signed CHSH functionals, and no local vertex attains 4 on any.  On
the cube NS_corr the maximum 4 is attained only at (+1,+1,+1,−1).

**Both inclusions strict.**  L ⊆ Q: the 16 generators of L are
generators of Q.  Strict: Q contains a point at 2√2 > 2 (exact ℚ(√2)
comparison).  Q ⊆ NS: every Gram correlator lies in [−1,1]⁴.  Strict:
the PR vertex has S = 4 > 2√2 = max over Q_corr, so it cannot lie in
Q_corr.  At the *generating-class* level the exclusion is sharper —
see §3.

## 2. A+ — the completeness of Q_corr

**Theorem (gated).**  In the CHSH (2,2,2) correlator projection,
Q_corr is the whole quantum correlator body.

By Tsirelson's theorem [T] — cited, not proven here — the quantum
correlator set is Q = { E_ab = ⟨u_a, v_b⟩ : u_a, v_b unit vectors in a
real Hilbert space }, of unbounded dimension.  The theorem is that the
planar (dim ≤ 2) configurations already generate it.  Four exact
steps, each gated:

1. For any λ ∈ ℝ⁴ and fixed v₀, v₁,
   Σ_ab λ_ab⟨u_a,v_b⟩ = ⟨u₀, λ₀₀v₀+λ₀₁v₁⟩ + ⟨u₁, λ₁₀v₀+λ₁₁v₁⟩ — an
   identity gated in ℝⁿ with *symbolic* λ.  Lagrange's identity
   ‖u‖²‖r‖² − ⟨u,r⟩² = Σ_{i<j}(u_i r_j − u_j r_i)², gated in ℝⁿ, gives
   ⟨u,r⟩ ≤ ‖r‖ with maximizer r/‖r‖.  **So the optimal u_a lie in
   span{v₀,v₁}, of dimension at most 2.**
2. ‖x v₀ + y v₁‖² = x²‖v₀‖² + y²‖v₁‖² + 2xy⟨v₀,v₁⟩, gated in ℝⁿ: on
   unit v's the optimum depends on (v₀,v₁) **only through
   t = ⟨v₀,v₁⟩**.
3. Every t ∈ [−1,1] is realized by unit vectors in ℝ².  The rational
   circle parametrization t = (1−m²)/(1+m²), s = 2m/(1+m²) is gated
   exactly on 3240 rational slopes (t² + s² = 1 exactly, t ∈ [−1,1]);
   surjectivity onto [−1,1] is continuity.
4. Hence the support function of Q equals that of the planar family
   for **every** λ.  Q and Q_corr are compact convex [CVX], so equal
   support functions give **Q = Q_corr**.

Steps 1–3 are gated in ℝⁿ for n = 2, 3, 4, 5, 6 and hold for every n
by the same expansion.

**A corollary worth engraving:** the parallelogram identity holds in
ℝⁿ for every n, so CERT-0/1/2/3 prove **Tsirelson's bound in every
dimension**, not only in the plane.  The 2√2 needs no dimension
restriction and no Hilbert-space hypothesis beyond real inner
products.

**Independent corroboration.**  Exhaustive sweeps over exact rational
unit vectors: 26 vectors in ℝ³ (denominators ≤ 9) and 26 in ℝ⁴
(denominators ≤ 5), 456 976 four-vector configurations each, all
correlators exact rationals.  No configuration exceeds 2√2; the maxima
reached are 68/27 (ℝ³) and 58/25 (ℝ⁴).

**Scope tag, engraved with the theorem:** this is the CHSH (2,2,2)
correlator projection, after convexification.  It says nothing about
full behaviours including marginals, nothing about scenarios with more
settings, parties or outcomes, and it does not claim that the
un-convexified U(1)-Gram generating class is the quantum set — §3
proves that class is not even convex.

## 3. The generating class is not convex — and the sharp exclusion

E = (1,0,0,0) is the mean of four deterministic vertices, so it lies
in L_corr ⊆ Q_corr.  It is **not** a U(1)-Gram generator: E₀₀ = 1
forces z₀ = w₀; E₀₁ = 0 forces w₁ = μ i z₀; E₁₀ = 0 forces
z₁ = ε i z₀; then E₁₁ = εμ ∈ {+1,−1}, never 0 — all four sign branches
gated in ℚ(ζ₈).  So the U(1)-Gram **generating class** is not convex.
This is why paper 0 v2.1's convexification is load-bearing rather than
cosmetic: the *class* chain and the *body* chain are different
statements and only the body chain is a chain of convex sets.

**The sharp exclusion at the class level.**  Every {±1}-valued
U(1)-Gram point satisfies

    E₀₀ E₀₁ E₁₀ E₁₁ = +1                                        (∗)

Proof: CERT-1 with |z| = |w| = 1 gives Re(z conj(w)) = ε ∈ {±1} ⇒
Im(z conj(w)) = 0 ⇒ z = ε w; reading z_a = E_ab w_b at b = 0 and b = 1
gives w₁ = E_a0 E_a1 w₀ for both a, hence E₀₀E₀₁ = E₁₀E₁₁, hence (∗).
The PR correlators (1,1,1,−1) have product −1, so **PR admits no
U(1)-Gram representation at all** — not merely a point outside a
convex body.  Gated: the lemma in-field on the π/4 unit pairs (16 of
64 have Re = ±1, all satisfy z = εw); and exhaustively on the 16 sign
vectors, the 8 with product +1 are exactly the {±1}-factorizable ones
and the 8 with product −1 are exactly the non-factorizable ones.

**(∗) is the 4-cycle holonomy of the sign pattern** — gated as an
identity on all 16 patterns: E₀₀E₀₁E₁₀E₁₁ = g₀₀ g₁₀⁻¹ g₁₁ g₀₁⁻¹.  The
invariant that excludes PR from the Gram class is the same invariant
Arm B computes.

**Q_corr ⊆ NS_corr, constructively.**  P(x,y|a,b) = ¼(1 + xy E_ab) is
normalized, has both marginals ≡ ½ and reproduces E — all three are
polynomial identities in E, gated symbolically, so no-signaling holds
for *every* correlator vector; non-negativity is the only inequality
and |E_ab| ≤ 1 is gated by the sign oracle on all 4096 π/4 grid
points, with 512 rational-correlator tables built and fully checked.

## 4. The anti-correlation exhibit

**The singlet amplitude model** ψ_xy(a,b) = (z_a − xy·w_b)/(2√2),
z_a = e^{ia}, w_b = e^{ib}.  The Born identity

    P(x,y|a,b) = |ψ_xy(a,b)|² = ¼(1 − xy·cos(a−b))

is gated as CERT-4, a polynomial identity
|z − εw|² = |z|² + ε²|w|² − 2ε Re(z conj(w)), and instantiated at two
declared algebraic angle families: the **π/4 family in ℚ(ζ₈)** (all 8
angles, 256 exact gates) and the **π/8 family in ℚ(ζ₁₆)** (all 16
angles, 1024 exact gates).  ℚ(ζ₁₆) is the declared carrier for the π/8
family — it contains cos(π/8) and √2 and needs no nested radical.  The
resulting tables are valid no-signaling tables (4096 π/4 quadruples
non-negativity-gated, 512 tables built and fully checked).

At the review's settings (a₀,a₁; b₀,b₁) = (0, π/2; π/4, −π/4) the
correlators are E_ab = −cos(a−b) and

    S = −2√2  exactly,   |S| = 2√2 = max over Q_corr.

The sign belongs to the functional, not the model: w_b ↦ −w_b stays in
the class and carries the instance to +2√2 (gated).

**The holonomy, one line.**  With g_ab = z_a conj(w_b),

    g₀₀ g₁₀⁻¹ g₁₁ g₀₁⁻¹
      = (z₀ conj z₀)(z₁ conj z₁)(w₀ conj w₀)(w₁ conj w₁) = 1

identically — every factorized edge phase is a coboundary, so its
holonomy around any cycle is 1.  Gated on 4096 quadruples of the π/4
family (exhaustive) and 4096 of the π/8 family (a₀ = 0 fixed; the
holonomy is invariant under z_a ↦ λz_a and w_b ↦ μw_b separately,
since each z_a and each w_b occurs once with each exponent sign).

**The PR edge-phase pattern** (γ₀₀,γ₀₁,γ₁₀,γ₁₁) = (1,1,1,−1).  The
table is a valid no-signaling table with uniform marginals on both
wings, correlators (1,1,1,−1), S = 4 exactly, and 4-cycle holonomy −1:
not a coboundary, so the edge phases do not factorize.

**THE ENGRAVED TABLE**

| model | 4-cycle holonomy | CHSH |
|---|---|---|
| singlet (U(1)-Gram, Tsirelson-saturating) | **trivial** ( = 1) | 2√2 |
| PR edge-phase (1,1,1,−1) | **nontrivial** ( = −1) | 4 |

The v1 identification "quantum ⟺ nontrivial class" is anti-correlated
with quantumness in these two natural models.  This is an exhibit —
two named models with opposite pairing — not a theorem about all
models, and it establishes no replacement correlation between class
and CHSH.  It is the concrete form of [AMB]'s caution that a
cohomological class is a sufficient witness, not an equivalence.

## 5. The Δᴮ census

Δᴮ(U₂,U₁) := B(U₂U₁) − B(U₂)B(U₁) with B(U)_ij = |U_ij|².

**The cross-term identity** [B1]:

    Δᴮ_ij = Σ_{k≠ℓ} (U₂)_ik (U₁)_kj · conj( (U₂)_iℓ (U₁)_ℓj ),

i.e. the defect is exactly the off-diagonal interference terms of the
entrywise expansion.  Gated entrywise against the definition on four
named pairs — H∘H and H∘W in ℚ(ζ₈), F₃∘F₃ and F₃∘F₃† in ℚ(ζ₁₂) — and
on **every** census pair below (9216 + 3969 pairs, 0 mismatches).
ℚ(ζ₁₂) is the declared carrier for DFT₃: it contains both ζ₃ and √3,
where ℚ(ζ₃) contains ζ₃ but not the normalization √3.

**The census.**  Two families, all ordered pairs swept, no sampling.

| family | matrices | monomial-seeded | ordered pairs |
|---|---|---|---|
| 𝔉₂ ⊂ U(2) over ℚ(ζ₈): P·diag(μ₄) and diag(1,μ₈)·H·diag(1,μ₈) | 96 | 32 | 9216 |
| 𝔉₃ ⊂ U(3) over ℚ(ζ₁₂): P·diag(1,μ₃,μ₃) and diag(1,μ₃,1)·F₃·diag(1,μ₃,1) | 63 | 54 | 3969 |

Every member is verified unitary in exact arithmetic.

| | cond & Δᴮ=0 | cond & Δᴮ≠0 | free & Δᴮ=0 | free & Δᴮ≠0 |
|---|---|---|---|---|
| 2×2 | 5120 | **0** | 1024 | 3072 |
| 3×3 | 3888 | **0** | 54 | 27 |

where *cond* = "U₂ has at most one nonzero per row **or** U₁ has at
most one nonzero per column".

- **Sufficiency, gated:** *cond* ⇒ Δᴮ = 0, with 0 counterexamples in
  9008 conditioned pairs; the k ≠ ℓ sum is empty.  Covers permutation
  × anything and diagonal-phase × anything, in either slot.
- **Not necessary, gated:** 1024 (2×2) and 54 (3×3) unconditioned
  pairs have Δᴮ = 0.  Named counterexample: Δᴮ(H, W) = 0 with
  H = (1/√2)[[1,1],[1,−1]] and W = (1/√2)[[1,i],[i,1]], both fully
  unbiased.
- **Δᴮ ≠ 0 exhibits:** Δᴮ(H,H) = [[½,−½],[−½,½]]; Δᴮ(F₃,F₃) ≠ 0
  (B(F₃²) is the permutation j ↦ −j mod 3 while B(F₃)B(F₃) = J/3).

**The unbiased sub-census, decided in closed form and gated.**  For
unbiased factors B(U₂) = B(U₁) = J/n, so Δᴮ = 0 ⟺ B(U₂U₁) = J/n ⟺ the
product is again unbiased; outer diagonals do not change moduli, so Δᴮ
depends only on the interleaving phase between the blocks.

- 2×2, U₂ = diag(1,ζ₈ˢ)·H·diag(1,ζ₈ᵗ), U₁ = diag(1,ζ₈ᵘ)·H·diag(1,ζ₈ᵛ):
  **Δᴮ = 0 ⟺ t+u ≡ ±2 (mod 8)** — the interleaving phase is a quarter
  turn.  Gated on all 8⁴ = 4096 parameter quadruples, 1024 with
  Δᴮ = 0, prediction exact.  (H, W) is the case t+u = 2.
- 3×3, U₂ = D(a₂)·F₃·D(b₂), U₁ = D(a₁)·F₃·D(b₁) with
  D(m) = diag(1, ω^m, 1): **Δᴮ = 0 ⟺ b₂+a₁ ≢ 0 (mod 3)** — F₃D(m)F₃ is
  a complex Hadamard matrix for m ≠ 0 and has zero entries for m = 0
  (where it is the permutation j ↦ −j).  Gated on all 3⁴ = 81
  parameter quadruples, 54 with Δᴮ = 0, prediction exact.

**The sharpening, engraved:** Δᴮ = 0 is a *phase-alignment*
condition, not a support condition.  The support criterion is
sufficient and strictly weaker.  In the 2×2 case the obstruction is
Re(A_i B_j) = 0 with A_i = (U₂)_i0 conj((U₂)_i1) and
B_j = (U₁)_0j conj((U₁)_1j).

## 6. C+1 — the three-defect separation

Three objects are distinguished and never conflated:

    Δᴮ(U₂,U₁) = B(U₂U₁) − B(U₂)B(U₁)      the Born-shadow defect
    D₂₁₀      = Γ₂₀ − Γ₂₁Γ₁₀              the residual of a DECLARED law
    d_div     = inf over stochastic K of ‖Γ₂₀ − KΓ₁₀‖   existential

The counterexample is exact and rational.  For the real rotation
R(θ) = [[c,−s],[s,c]] with c²+s² = 1 and
S(x) := ½[[1+x, 1−x],[1−x, 1+x]]:

- **B(R(θ)) = S(cos 2θ)** — gated symbolically; the residual of the
  entrywise identity is exactly (c²+s²−1)/2, vanishing on the unit
  circle.
- **S(c)S(d) = S(cd)** — gated as an entrywise polynomial identity in
  ℚ[c,d].
- U₁ = R(θ₁) with (cos θ₁, sin θ₁) = (24/25, 7/25) and U₂ = R(θ₂) with
  (4/5, 3/5), both exact rational unit vectors.  Then c₁ = 527/625,
  c₂ = 7/25 and c_tot = −7/25, all gated.
- **Δᴮ ≠ 0:** S(−7/25) ≠ S(7/25 · 527/625) = S(3689/15625); the exact
  defect entry is Δᴮ₀₀ = −4032/15625.  With the declared intermediate
  law Γ₂₁ = B(U₂) the actual residual D₂₁₀ equals Δᴮ, so it is nonzero
  too.
- **Yet the shadow divides:** K = S(−175/527) is a valid stochastic
  matrix (entries (1±c)/2 ≥ 0, columns summing to 1) with
  **K·B(U₁) = B(U₂U₁) exactly**, since
  S(−175/527)S(527/625) = S(−175/625) = S(−7/25).  And K ≠ B(U₂): the
  divisor exists but is not the Born shadow of the second step.
- **So d_div = 0 while Δᴮ ≠ 0.**  Gated in general for rotations:
  |c_tot| ≤ |c₁| ⇒ K = S(c_tot/c₁) divides, verified on 1256 exact
  rational (c₁, c_tot) pairs.

**Engraved:** Δᴮ is an amplitude-level coherence measure.  It is not
a divisibility measure, not a witness of indivisibility, and not the
residual of any declared stochastic law unless that law is declared to
be B(U₂).  Nothing in this receipt equates them.

## 7. C+2 — the coherence law (W2a's seed)

    Δᴮ(U₃U₂,U₁) + Δᴮ(U₃,U₂)B(U₁) = Δᴮ(U₃,U₂U₁) + B(U₃)Δᴮ(U₂,U₁)

Both sides equal B(U₃U₂U₁) − B(U₃)B(U₂)B(U₁).  The derivation uses
only associativity and distributivity of matrix algebra, so it is an
identity in **formal** matrices, and that is how it is gated:
independent polynomial variables for every entry of B(U₁), B(U₂),
B(U₃), B(U₂U₁), B(U₃U₂), B(U₃U₂U₁) — 24 variables at 2×2, 54 at 3×3 —
with no property of B assumed.  Both the law and the reduction of each
side to the common form are gated entrywise.

Corroborated on exact matrices: all ordered triples from a declared
subfamily of each census family — 14 matrices / 2744 triples (2×2 over
ℚ(ζ₈)) and 9 matrices / 729 triples (3×3 over ℚ(ζ₁₂)), 0 failures.

The law is an identity, not a theorem about quantum mechanics.  It
constrains the Δᴮ family; it selects nothing.  W2a takes it from here.

## 8. The record example (reporting-only; feeds W3′)

**The record is defined first, with no reference to any defect**, per
v2.1 T3′: R is the intermediate configuration variable, whose values
are the mutually exclusive sectors {|k⟩⟨k|}; the reading of R is the
dephasing channel D that kills coherences between sectors and leaves
each sector's weight untouched.  D is record-preserving by
construction.  Nothing here treats erasure or sector-recombining
operations.

Running the exact density-matrix computation ρ₀ = |j⟩⟨j| →
U₁ρ₀U₁† → D → U₂(·)U₂† and reading the diagonal gives, on both worked
examples (H∘H over ℚ(ζ₈), F₃∘F₃ over ℚ(ζ₁₂)):

    shadow(U₂ ∘ D ∘ U₁)  =  B(U₂) · B(U₁)   exactly,

while the same computation without D returns B(U₂U₁), whose defect
against B(U₂)B(U₁) is nonzero on both examples.  The D-interleaved
shadow is a genuine stochastic matrix (rational, non-negative, columns
summing to 1).

Reading it per T3′: reading R at the intermediate cut induces a law on
the commutative record algebra — from j, R takes value k with
probability B(U₁)_kj, then the final configuration is i with
probability B(U₂)_ik — and that composite law is B(U₂)B(U₁), whose
actual residual D₂₁₀ with the declared Γ₂₁ = B(U₂) is identically
zero.  **The recorded law divides at the cut, and it is exactly the
Born shadow of the physical channel U₂∘D∘U₁.**

Scope: one worked example, reporting-only.  It does not prove T3′ in
general, treats no partial or approximate record, no erasure, no
sector-recombining operation.  It does **not** say that Δᴮ ≠ 0 means
the shadow fails to divide — §6 exhibits a pair where Δᴮ ≠ 0 and the
shadow divides anyway.  W3′ is the general theorem.

## 9. Antecedents

Every theorem used carries its citation in the receipt output at the
gate where it is used.  The unit claims **assembly and receipts**, not
novelty of the chain.

- **[F]** Fine, PRL 48, 291 (1982) — the local set as the hull of the
  16 deterministic assignments.  Used at A1, A5.
- **[T]** Tsirelson's bound, and Tsirelson's theorem that the (2,2,2)
  quantum correlator set is exactly the real unit-vector Gram set.
  The characterization is **cited**; A+ derives from it that planar
  vectors already suffice.  Used at A2, A+.
- **[CVX]** Standard convexity: extreme-point attainment;
  max over conv(S) = max over S; equal support functions ⇒ equal
  compact convex sets; convexity and compactness of the quantum
  correlator set; Carathéodory.  Used at A6, A+.
- **[NS]** Popescu–Rohrlich (1994); Barrett–Linden–Massar–Pironio–
  Popescu–Roberts, PRA 71, 022101 (2005) — the PR box and the 24
  vertices.  Used at A3, A6, B2.
- **[B1]** Barandes, arXiv 2302.10778 — the identification of the
  Born-projection cross terms with interference.  Reproduced at
  C1/C2, not originated here.
- **[AMB]** Abramsky–Mansfield–Barbosa, arXiv 1111.3620 — the
  cohomological obstruction as a sufficient witness, not an
  equivalence.  Used at B3.
- **[AB]** Abramsky–Brandenburger, NJP 13, 113036 (2011) — the exact
  global-section formulation.  Named.
- **[REV]** the first external hostile review, LOG #3 — both Arm B
  constructions are its.  Used at B1, B2, B3.
- **[REV2]** the second external hostile review, LOG #4 — the
  convexification, the completeness target, the three-defect
  counterexample and the coherence law.  Gates A+, C+1, C+2 are its.
- **[W]** Weyl relations / noncommutative torus.  **Named only**, used
  at no gate: it is W2b/W2c's object.

## 10. Scope

1. **No claim about nature.**  Every result is a statement about three
   declared convex bodies on one declared scenario.
2. **Q_corr IS the quantum correlator body — with its scope tag:** in
   the CHSH (2,2,2) correlator projection, after convexification, and
   resting on Tsirelson's characterization [T], which is cited and not
   proven here.  The un-convexified U(1)-Gram generating class is not
   the quantum set: it is not even convex (§3).  Nothing is claimed
   about full behaviours including marginals.
3. **Δᴮ is not a divisibility measure.**  Δᴮ ≠ 0 does not imply
   stochastic indivisibility (§6).  Δᴮ, D₂₁₀ and d_div are three
   different objects and are never conflated in this receipt.
4. **Out of scope, named:** (a) higher scenarios — more settings,
   parties or outcomes — where the planar argument of A+ does not
   apply and where real-vs-complex separates; (b) the NPA hierarchy
   and Tsirelson-from-principles (IC/ML/LO), neither used nor
   advanced; (c) the projective multiplier [ω] ∈ H²(ℤ², U(1)) and the
   Weyl phase θ — that is W2b/W2c, untouched here, and the Born
   projection annihilates scalar multipliers (B(ωU) = B(U)), so that
   bridge must be built, not assumed; (d) T3′ in general — §8 is one
   worked example.
5. **The anti-correlation table is an exhibit**, not a theorem about
   all models, and it establishes no replacement correlation.
6. **The coherence law is an identity**, not a theorem about quantum
   mechanics.  It constrains the Δᴮ family; it selects nothing.
7. Paper 0 v2.1 §5's non-claims stand unmodified.

## 11. What this unit hands over

- The v2.1 skeleton's three maxima, both review constructions, and the
  completeness of Q_corr are receipted.  §3's non-convexity of the
  generating class is the reason the convexification is load-bearing.
- **W2a** receives §7's coherence law, gated as a formal-matrix
  identity and corroborated on 3473 exact triples.
- **W3′** receives §8's record example as its constructive seed, §5's
  phase-alignment criterion as the shape of the general Δᴮ = 0
  condition, and §6's separation as the boundary it must respect: the
  theorem it wants is about D₂₁₀ or d_div on the record algebra, not
  about Δᴮ.
- **W2b/W2c** receive nothing from this unit: [W] is named and
  untouched.
