# Walsh Delta Global-Optimality — Solve Log

Working log for the attack on the Global Delta Optimality Problem
(`walsh-delta-global-optimality-problem.md`). Newest entries at the bottom.

## 2026-07-02 — Session start: state absorption

Read §1–10 and §45–47 of the problem file. Current state of the problem
document:

- **Proved**: uniqueness at maximal depth (easy lemma); convex-dual form
  (sealed point = critical point of `K_σ(u) = F*(σ⊙u) + Σ(u log u − u)`);
  Schur-complement localization; tropical boundary sign cone
  `S_a ŵ(a) ≤ 0` excluding non-delta-aligned coset collapse (§9.7);
  projection decomposition (47.1); universal Shearer redundancy `R₂ ≥ 0`;
  projection nullspace = translated deltas (§47.5).
- **False**: pointwise DCT (§46 — scalar all-active branch passes through
  uniform, certificate changes sign); common-scalar-Bregman-square route to
  RAC/GERAB (§45 — Hessian curl obstruction on m_L=1,2 lines).
- **Open (live targets)**: RAC endpoint residual cut (§45–46); Sealed
  Projection-Stability SPS-1/SPS-2 (§47.6).

## Key reformulations found on first pass (mine, to verify)

Let `X = N·P_ε`, `x_a = X̂(a) = σ_a u_a`, `g_a = \widehat{log X}(a) = σ_a h_a`,
`h_a = −log u_a > 0`. Then:

1. **Convex unconstrained form of the seal.** The sealed ℓ = g is the unique
   global minimizer of the smooth strictly convex function
   `G_ε(ℓ) = F(ℓ) + Σ_a exp(−ε_a ℓ_a)` over ℓ ∈ R^{N−1}
   (F = log-partition). No constraints. This makes numerics trivial
   (Newton on a convex function) and gives a variational principle per
   orientation.
2. **Three-divergence identity.** At any sealed point:
   `D(P‖U) + D(U‖P) = Σ_a h_a e^{−h_a}`, i.e. the Jeffreys divergence equals
   `Σ φ(h_a)`, `φ(h) = h e^{−h} ≤ 1/e`. (From
   `E[(X−1)log X] = Σ_a x_a g_a` and the seal.)
3. **First-order convexity bound.** For every spike s⋆:
   `D(ε) − D_δ ≥ h⋆·[A⋆ − X_ε(s⋆)] + (1/2N)‖x_ε − x_δ‖²`,
   A⋆ = 1−(N−1)u⋆ = delta min value. So the hard case is X_ε bounded away
   from 0 everywhere (flat-ish sealed laws) — consistent with the doc's
   boundary-channel analysis.
4. **Scale of the SPS split.** `γ_n|𝓛| = n/2`, so
   `R₂(X_δ) = D_δ − (n/2)·D_{L,⋆} ≈ D_δ` (since D_{L,⋆} ≈ (3/2)u⋆²
   ≪ u⋆ ≈ D_δ). Hence SPS-2 carries almost the whole weight; SPS-1's
   threshold `Σ_L D_{L,⋆} = (n/2)/γ_n·…` is comparatively small.
   Linewise Pinsker gives `Σ_L D_L ≥ (ρ/6)χ²`, ρ = (N−2)/2, so **SPS-1
   follows from a sealed χ² floor** `χ²(X_ε) ≥ ~3(N−1)u⋆²` for non-delta ε.
   Question: is the factor-3 χ² floor true? → numerics.
5. **Warning found for SPS-2**: uniform-on-affine-subspace densities have
   R₂ = 0 but D large — so SPS-2 is NOT slack-protected against
   subspace-concentration; it needs the seal (the §9.7 sign cone should
   exclude sealed laws approaching coset measures — check whether that
   argument covers this).

## Immediate plan

1. Spawn readers to extract precise proven/false/open claims from §11–44
   (esp. §13 closed scalar endpoint, §14 finite-n no-collapse, §20 rank-one
   base case, §41–44 closure-gap machinery).
2. Numerics: exhaustive orientation scan n=2,3 (float64 Newton on G_ε),
   n=4 all 32768 orientations; per orientation compute D, D̄=D(U‖P), χ²,
   Σ_L D_L, R₂, min X, and check: delta minimality, SPS-1, SPS-2, χ² floor
   factor, second-lowest values. mpmath (dps ≥ 60) re-verification of all
   near-marginal cases per standing precision policy.
3. Attack SPS-1 via χ² floor; attack SPS-2 perturbatively + boundary
   exclusion; log everything.

Status: **in progress** — setting up readers + numerics now.

## 2026-07-02 — Numerics: exhaustive n=2,3,4 + document digest complete

Readers extracted the full §11–44 status. Proven unconditionally in the doc:
§13 closed scalar endpoint comparison (all-plus vs delta, D_+ > D_δ for
Q ≥ 4, with scale separation 1/Q < D_δ(Q) < log(Q/(Q−1)) < 1/(Q−1));
§14 minus-branch no-collapse; §20 rank-one (|M|=1) killed base case
D > D_δ(N); §22 translated-delta null ℰ_{M_{t₀}}(2α⋆1) = 0; §23 two-layer
nullspace; §25–29 line-incidence/max-flow scaffolding; §35–40 row audit +
boundary-zero payment. Open critical obstruction on RAC side: unit-scale
closure ⇔ (SC_ε) ⇔ (RC), with two explicit bad cones (§43.4–43.5).

Exhaustive scans (float64 Newton on the convex G_ε; all orientations):

| n | D_δ | min non-δ D | ratio | SPS-1 viol | SPS-2 viol | χ² floor ratio |
|---|------|------------|-------|-----------|-----------|---------------|
| 2 | 0.266653 | 0.459889 | 1.72 | 0 | 0 | 3.45 |
| 3 | 0.133531 | 0.595770 | 4.46 | 0 | 0 | 7.87 |
| 4 | 0.064539 | 0.328048 | 5.08 | 0 | 0 | 9.00 |

**Both halves of SPS (§47.6) hold exhaustively for n ≤ 4.** SPS-2 margin is
thin at n=3 (R₂ = 0.0842 vs 0.0818) but comfortable at n=4 (0.192 vs 0.051).

Defect-class structure (|M| = Hamming distance of τ to nearest character =
first-order RM decoding): runner-up is |M|=1 at n=2, |M|=2 at n=3, |M|=4 at
n=4 (i.e. |M| = 2^{n−2}), NOT |M|=1 (whose min D grows: 0.46, 0.68, 0.73).
Runner-up at n=4 has THREE astronomically deep points (X ≈ 3.6e−10) and a
two-level h-spectrum — multi-spike structures are the real competitors, and
the seal punishes them through near-cancelling Fourier coefficients.

## 2026-07-02 — New exact identities (verified numerically to machine precision)

Notation: u_a = e^{−h_a} = |x̂_a|, h_a = |ĝ_a| where g = log X,
D̄ = D(U‖P) = −E_U log X, w(s) = log N − log X(s) ≥ 0,
M(s) = {a ≠ 0 : σ_a = χ_a(s)} (defect set of σ vs the delta at s),
m(s) = 2 Σ_{a∈M(s)} h_a, z(s) = 1 − T_σ(s) (even integers, Σ_s z = N,
Σ_s z² = N²; z = N·1_{s⋆} iff delta).

1. **Jeffreys identity:** D + D̄ = Σ_a h_a e^{−h_a} = Σ_a φ(h_a), φ ≤ 1/e.
2. **Depth–defect identity:** for EVERY s:
   w(s) + m(s) = B, B := Σ_a h_a + log N + D̄ = E_U[w·z].
   (Verified: runner-up n=4, both sides 11.542266465 at argmin X.)
   Consequences: max_s w = B − min_s m(s); for NON-delta σ every s has
   M(s) ≠ ∅, so **max_s w ≤ B − 2h_min** where h_min = min_a h_a.
3. **Exact delta-comparison:** for every center s⋆:
   D(ε) − D_δ = D(P_ε‖P_δ) − h⋆·(X_ε(s⋆) − A⋆). Equivalent statement of the
   whole theorem: no non-delta sealed law is "nearly uniform".
4. **Bhatia–Davis constraint (♦):** since w ∈ [0, max w], E w = log N + D̄,
   Var w = Σ_a h_a²: Σ_a h_a² ≤ (log N + D̄)(max_s w − log N − D̄)
   ≤ (log N + D̄)(Σ_a h_a − 2h_min) for non-delta.
5. **Flat-spectrum rigidity lemma:** if all h_a are equal, the sealed law is
   a delta. (log X and X both affine in z ⇒ strict concavity of log forces z
   two-valued; counting Σz = N, Σz² = N² + integrality/impossibility of
   constant-modulus indicator spectra forces z = N·1_{s⋆}.)

**Reformulated target (T2):** ∃ c₀ > 1/31 such that for all n ≥ 5, every
non-delta orientation has D(ε) ≥ c₀. Combined with D_δ < log(N/(N−1)) <
1/(N−1) ≤ 1/31 (§13's scale separation) and the exhaustive n ≤ 4 scans,
T2 ⇒ full Global Delta Optimality. Numerical support: min non-δ D ≥ 0.33
for n ≤ 4. Next: probe n=5,6 minima by structured + random local search.

## 2026-07-02 — BREAKTHROUGH: reduction to a single spectral stability lemma

Chain of new exact reductions (all elementary, to be written up rigorously):

1. **Gibbs form of the seal.** X(s) = e^{m(s)} / E_U[e^m] where
   m(s) = 2Σ_{a∈M(s)} h_a and M(s) = {a: σ_a = χ_a(s)}. So the sealed law is
   the Gibbs measure of the defect-mass function m, and
   D = E_P[m] − log E_U[e^m] **depends only on the LAW μ of m under U**
   via the Gibbs-gap functional Φ(μ) = E_μ[me^m]/E_μ[e^m] − log E_μ[e^m] ≥ 0
   (zero iff μ = point mass).
2. **Spectrum of m:** m − E m = Σ_a σ_a h_a χ_a — a Walsh polynomial whose
   N−1 nonzero coefficients ALL have modulus h_a ≥ h_min, where (Pinsker +
   seal) h_min ≥ ½ log(1/(2D)).
3. **Deep-pair exclusion (Lemma DP):** m(s) + m(s') ≥ 2H_{s+s'} where
   H_t = Σ_{χ_a(t)=−1} h_a ≥ (N/2)h_min. So at most ONE point can have
   m < (N/2)h_min: near-uniform sealed laws have exactly one candidate dip
   point — the delta center candidate.
4. **Φ-small structure:** D < c₀ forces law(m) = "one narrow band + small
   deep dip set". The exact two-point law ((N−1)/N at λ, 1/N at λ−drop) is
   achieved ONLY by m̂(a) = const·(−χ_a(s₀)) — i.e. flat spectrum + delta
   signs (this re-proves the flat-rigidity lemma and identifies the
   equality configuration).
5. **Dichotomy mechanism for non-delta (flat-h picture):** off the dip,
   m(s) = const + 2h̄·Y_{M₀}(s), Y_{M₀} = Σ_{a∈M₀}χ_a. Either Y_{M₀} splits
   the bulk into balanced levels ≥ 2h_min apart (D ≳ log cosh-type cost,
   Θ(1)), or M₀∪{0} is subgroup-like and the Gibbs mass concentrates on the
   small dual coset W^⊥ (D ≥ ~log|W| ≥ log 2). Only M₀ = ∅ escapes. This is
   exactly the structure of the observed runner-ups (|M| = 2^{n−2},
   subgroup-type defect sets, 3 deep points at n=4).

**Everything therefore reduces to:**

> **Lemma X (Spectral one-dip stability).** Let f = Σ_{a≠0}c_aχ_a on F₂ⁿ
> with |c_a| ≥ h_min for ALL a ≠ 0. Then either the sign pattern of c is
> delta-aligned (c_a ∝ −χ_a(s₀), flat), or
> Φ(law of f) ≥ floor(h_min) with floor(h_min) > c₀ for the required range.

Constants matter: need floor > 1/31 at h_min = ½log(1/(2/31·... )) ≈ 1.36 so
that n ≥ 5 is covered (n ≤ 4 exhausted numerically). If the true landscape
minimum decays with n this strategy needs the decay to stay above
1/(N−1) — the n=5,6 probes (running) will calibrate.

Note: Lemma X needs NO further input from the seal beyond h_min — the seal
enters only through Pinsker (h_min) and the Gibbs form. This decouples the
hard combinatorial core from the fixed-point analysis entirely — a much
cleaner surface than DCT/RAC/SPS.

## 2026-07-02 — CORRECTION: Lemma X as stated is FALSE; true mechanism found

Machine-precision verification passed for all five identities (G, Φ, J, B,
DP) at n=3,4,5 (worst error 1.9e-12, zero DP violations). n=5 probe: best
non-delta D ≈ 0.4058 (|M|=9, three-level structure) vs D_δ(32) ≈ 0.03175.
Floor stays ≈ 0.33+ for n = 2..5.

**Lemma X (one-sided version) is FALSE:** the "k dips + perfectly flat bulk"
configuration f = −Σ_j d_j·N·1_{s_j} + const with k=3 equal dips on 3 points
of an affine plane has full spectrum (|F(a)| ∈ {d, 3d} > 0 on the four sign
classes) and Gibbs gap Φ ≈ 3/N — arbitrarily small. The h_min floor alone
cannot kill it. (This config is exactly the shape of the observed n=4
runner-up — but the runner-up's true sealed D is 0.33, NOT 3/N.)

**The true mechanism (two-sided spectral matching):** the seal demands BOTH
  h_a = |ĝ(a)| ≈ (1/N)|Σ_j β_j χ_a(s_j)|   (log-side: β_j = dip log-depths)
  e^{−h_a} = |x̂(a)| ≈ (1/N)|Σ_j μ_j χ_a(s_j) + bulk-tilt|  (x-side:
  μ_j = 1−X(s_j) ∈ (0,1] dip masses).
The exponential link h = log N − log|G| inverts peaking:
- **k=2 exact kill:** matching forces 2β₂ = N·log(|μ₁−μ₂|/(μ₁+μ₂)) < 0 —
  a negative dip depth. Contradiction. No non-delta 2-dip sealed law.
- **Common-sign-class argument (k ≥ 2, dips not affinely spanning):** ∃ mask
  a* ≠ 0 with χ_{a*}(s_j) all equal ⇒ |F(a*)| = Σβ_j is the MAXIMUM of |F|
  (all β_j > 0) so h_{a*} = max h; but |G(a*)| = Σμ_j is the maximum of |G|
  so u_{a*} = max u, i.e. h_{a*} = MIN h. Hence h flat ⇒ (flat-rigidity
  lemma) delta ⇒ contradiction. **Positivity of both weight families + the
  log-link forces flatness, and flatness forces delta.**
- Remaining to make fully rigorous: (i) the quantitative ε-version (bulk is
  only ℓ²-flat to √(2c₀), dips only approximately point-like); endgame via
  z-integrality (z even, Σz = N, Σz² = N² are exact, so "near-delta ⇒ delta"
  has integer rigidity to absorb the ε's); (ii) the affinely-spanning
  large-k case (k up to ~c₀N dips; common-sign class can be {0}).

Empirical confirmation that the fixed point enforces the gap: the n=4
exhaustive scan shows the interval (0.0646, 0.328) contains NO sealed D
value — the landscape has a hard gap above the delta orbit.

Plan: write the full deliverable (`walsh-delta-gibbs-route.md`): rigorous
proofs of the reduction package + k=2 kill + sign-class lemma + flat
rigidity, precise statement of the two remaining quantitative lemmas,
numerics receipts (incl. exhaustive SPS-1/2 for n ≤ 4 — new evidence for
§47), mpmath spot-checks per precision policy, n=6 probe.

## 2026-07-02 — Corrections found during rigorization + final state

Two of my own overclaims caught and fixed before write-up:

1. **Flat-rigidity corrected.** "Flat spectrum ⇒ delta" is FALSE as stated:
   the exact statement (now Theorem 4 of the deliverable) is
   **flat spectrum ⇒ z two-valued ⇒ the upper level set S is a difference
   set in F₂ⁿ**. Admissible families: k=1 (delta, the only small-D one),
   k=N−1 (anti-delta, D→log N, already killed by [WD] §13), and
   Hadamard/Menon-parameter sets = bent configurations, n even (two ≈N/2
   levels ⇒ exponential separation kills half the mass ⇒ D ≥ log2−o(1)).
   Parameter equation k(N−k) = μ²(N−1) verified to admit only trivial +
   Hadamard solutions at N = 16, 32, 64, 256 (μ integrality of the
   discriminant). At n=4 the bent class sits at defect distance 6 with
   D ∈ [0.978, 1.020] in the exhaustive scan — consistent.
2. **k=2 kill superseded by a cleaner argument.** The common-sign-class
   argument now closes ALL non-spanning k ≥ 2 at once (Theorem 5):
   at a common-sign mask a*, |F| is maximal AND |G| is maximal; the
   exponential seal link sends max|F| to min|G|; hence |G| constant;
   constancy + positive weights forces (Σμ)² = Σμ² ⇔ k = 1. Positivity of
   the two weight families + log-link inversion of peaking = the whole
   mechanism. This is the endpoint statement DCT was reaching for.

**Deliverable written:** `walsh-delta-gibbs-route.md` — Theorems 1–5 with
complete proofs (existence/uniqueness via convex G_σ; Gibbs–defect identity
package; exact delta comparison; flat classification by difference sets;
single-dip rigidity), quantitative low-gap structure §6, the two remaining
lemmas L1 (ε-stability of the dip model, integer-rigidity endgame via z)
and L2 (affinely-spanning dips), full numerics receipts, and the mapping to
the [WD] program (§9: why RAC couldn't be one Bregman square — the log-side
alone genuinely admits cheap non-delta configs; both sides of the seal are
needed).

**Final status of the Real Novel Problem after this session:**
- PROVED unconditionally: everything in §§2–6 of the deliverable + finite
  verification n ≤ 4 (exhaustive; margins 0.19–0.46; extremes re-verified
  in mpmath dps 50).
- OPEN: Lemmas L1, L2 — the entire remaining content on this route.
  Conditional Theorem 6: L1 + L2 ⇒ global delta optimality for all
  n ≥ n₀ with equality classification.
- Landscape data: min non-delta D = 0.4599 (n=2), 0.5958 (n=3),
  0.3280 (n=4), 0.4058 (n=5, probed), 0.3356 (n=6, probed); D_δ = 0.2667,
  0.1335, 0.0645, 0.0317, 0.0157. Floor stays ≈ 0.33 across n = 2..6.
- SPS ([WD] §47.6): both halves verified exhaustively n ≤ 4 (first
  systematic evidence); thinnest margin 0.0024408 (SPS-2, n=3, mp-verified),
  two orders sharper than the theorem itself — SPS-2 is strictly harder
  than delta optimality.

## 2026-07-02 — Adversarial audit of the conditional theorem (4 hostile auditors)

Question audited: "L1 + L2 proven ⇒ problem fully solved?" Verdict:
**not as literally stated — two defects found and repaired** (deliverable
§7/§10 rewritten; revision note added).

**Defect 1 (well-posedness):** "the dip set" of a sealed law was never
pinned down — §6 admits ≥3 inequivalent definitions (threshold-d level
sets; the (N/2)h_min deep points, under which L2 is vacuous; dips relative
to an undefined bulk level λ). L1/L2 were statement-schemas; proven for
different definitions they could leave laws covered by neither. Repair:
the open content is now **Lemma L0** (definition-free): ∃(c₀, n₀) s.t.
every sealed law with D ≤ c₀, n ≥ n₀ is a delta sealed law. L1/L2 survive
as the two cases of L0's intended proof, relative to ONE fixed dip set
(pinned: 𝒮 = {s: m_max − m(s) ≥ h_min}).

**Defect 2 (effectivity):** bare existential constants do NOT close the
problem. Covered range: {n ≤ 4} ∪ {n ≥ max(n₀, n_c)}, n_c = min{n: c₀ >
D_δ(2ⁿ)}. The window 5 ≤ n < max(n₀, n_c) must be closed by finite
verification, which is feasible at n=5 (**exactly 176 orbits** of
translations⋊GL(5,2) — computed exactly during audit), heroic at n=6
(≥7.1e6 orbits, transversal generation is research-grade), impossible at
n ≥ 7 (≥8.1e21 orbits). So a proof of L0 must deliver c₀ > D_δ(128) =
0.0078432, n₀ ≤ 7 at minimum; clean target c₀ ≥ 0.031749 & n₀ ≤ 5
(NOTE: 0.0317 fails — D_δ(32) = ln(32/31) − 6.8e-48; 1/31 works).
Observed floor ≈ 0.33 gives ≥10× headroom over the target.

**Also from the audit (positive):** Theorem 5's proof verified
step-by-step (common-sign-mask existence; max/min inversion; the Parseval
counting identity machine-checked); Theorems 1–3 + identity package
re-derived and re-verified; ALL exhaustive-scan numbers replicated on
independent code (agreement ~5e-21 on the 20-digit receipts); at n=4 the
14 group orbits carry constant D to 6e-15 (delta orbit 16 @ 0.0645;
runner-up orbit 560 @ 0.3280; bent orbits 448/240 @ 0.978/1.020). No
circularity in the chain. Silent imports made explicit in §7 "recovery
facts": σ-recovery from the sealed law; translation covariance (equality
orbit); elementary self-contained bound D_δ < 1/(N−1) (removes the
[WD] §13 dependency from the chain).

**Bookkeeping corrections applied:** §10 proved-list tightened (Theorem 4's
Hadamard classification = citation; bent log2-floor = sketch; §6(c),(e)
hedged — all non-load-bearing for Theorem 6, they are proof obligations
inside L0); §1 receipt phrasing fixed (mp re-verification covers extremes +
thinnest margin, not "every marginal quantity"); n ≤ 4 verification labeled
"numerical, certification mechanical but not yet performed" (Newton–
Kantorovich pass with Hessian floor λ_min ≥ min_a u_a from Theorem 1;
~8 orders of slack).

**Net answer to "L1+L2 (now L0) ⇒ solved?":** L0 with effective constants
(c₀ ≥ 0.031749, n₀ ≤ 5) + certified n ≤ 4 verification ⇒ FULLY solved,
equality classification included. With weaker effective constants, also
need orbit-exhaustive n=5 (trivial: 176 orbits) and possibly n=6 (hard);
below c₀ = 0.00785 or above n₀ = 7 the window cannot be closed by any
computation.

## 2026-07-02 — FULL-PROOF CAMPAIGN: plan

User instruction: fix everything, fully prove it. Honest scope statement
up front: items 1–3 below are closable this session; item 4 (Lemma L0,
especially the spanning-dips case) is genuine open mathematics — it gets
a maximal-effort push with exact documentation of the frontier.

1. **Certified n ≤ 4.** Upgrade the float64 exhaustive scans to
   proof-grade: a posteriori Newton–Kantorovich certificates per
   orientation. Basis (rigorous): Hess G_σ = Cov_P(χ) + diag(e^{−σ_aℓ_a})
   ⪰ diag part, so on a ball of radius r around the numeric ℓ̃,
   λ_min ≥ (min_a ũ_a)e^{−r}; monotonicity of ∇G gives
   ‖ℓ̃ − ℓ*‖ ≤ ‖∇G(ℓ̃)‖·e^r/(min_a ũ_a) once self-consistent. Then a
   Lipschitz bound on D(ℓ) converts to a certified D-enclosure. Final
   pass in mpmath (dps 30) per orientation to kill float rounding.
2. **n = 5 unconditional.** BFS orbit enumeration in C over all 2^31
   orientations (256 MB visited bitmap) under the invariance group
   ⟨translations, GL(5,2) generators⟩ — produces the complete orbit
   partition BY CONSTRUCTION (completeness certificate: orbit sizes sum
   to 2^31; cross-check vs audit's Burnside count of 176). Then certified
   mpmath solves of the ≤176 representatives vs D_δ(32) (closed scalar
   form, dps 60). If clean: **theorem extended unconditionally to n = 5**
   and L0's effectivity target relaxes to c₀ > D_δ(64) ≈ 0.0157, n₀ ≤ 6.
3. **New unconditional theorems** (proofs found while re-attacking L0
   today; to be written into the deliverable):
   - T-A (universal abyss): EVERY sealed law has
     min_s X ≤ N·exp(−2‖h‖₂) ≤ N·exp(−2h_min√(N−1)).
     [Bhatia–Davis on w ∈ [0, max w], Ew = log N + D̄, Var w = Σh²,
     then AM–GM.] No smallness assumption — h_min > 0 always.
   - T-B (ℓ¹-saturation reduction): σ is delta iff m₁ := min_s m < 2h_min
     iff w_max > Σ_a h_a + log N + D̄ − 2h_min. So L0 ⇔
     [D ≤ c₀ ⇒ the deepest point exhausts the ℓ¹ spectral budget to
     within 2h_min].
   - T-C (sign-rigidity dominance criterion): if the deepest point
     carries enough of the ℓ² budget — precisely, if
     φ(s₁)·N/(N−1) > √((N−1)·V₂) where φ = w − Ew and
     V₂ = N·Σh² − φ(s₁)²·N/(N−1) is the off-deep-point fluctuation —
     then sgn ĝ(a) = −χ_a(s₁) for ALL a, i.e. σ is the delta at s₁, and
     by Theorem 1 uniqueness the law IS the delta law. (Key simplification:
     no need to identify the law analytically — only the SIGN pattern;
     uniqueness does the rest.) At the delta itself V₂ = O(u⋆²·N²)-small
     and the criterion holds with room.
   L0 thereby sharpens to: D ≤ c₀ ⇒ the T-C dominance holds. Multi-dip
   configs violate T-C's hypothesis and must be killed by the two-sided
   matching (L1/L2 cases) — that remains the open core.
4. **L0 push:** quantitative one-dip stability (dominant-dip regime) via
   T-C; spanning case: the rigidity system
   Ψ(s) := Σ_{a≠0} sgn(G(a))(Λ − log|G(a)|)χ_a(s) must be constant off
   the dip set — a support/uncertainty statement; document partial
   results precisely.
5. Hostile audit of all new material before finalizing (last audit caught
   2 real defects; keep that bar).

Budget note: dips can number up to Θ(c₀N) a priori (each costs ~0.15/N in
D), so the spanning case k ≥ n+1 is NOT exotic — it is the generic
obstruction for small c₀. Any honest L0 proof must handle it.

## 2026-07-02 — Campaign progress 1: certification + orbits + new theorems

**n ≤ 4 CERTIFIED (proof-grade).** cert_scan.py: per-orientation
a-posteriori Kantorovich certificates (mpmath dps 30 evaluation at the
exact float64 point; radius bound ‖ℓ*−ℓ̃‖ ≤ 2e·ρ/λ̃ via convexity +
Hessian floor diag(e^{−σℓ}); D-transfer via ‖∇D‖ ≤ (N−1)‖ℓ‖; delta value
by certified sign-bracketing of the scalar seal polynomial at dps 60).
Results — zero failures across ALL orientations:
  n=2: worst certified margin 0.19324 (max radius 5.8e-14)
  n=3: worst certified margin 0.46224 (max radius 2.7e-14)
  n=4: worst certified margin 0.26351 (max radius 2.3e-11, max D-err 1.6e-9)
Trust base: faithful mpmath arithmetic at dps 30 (not directed-rounding
interval arithmetic — noted as final polish; 8–9 orders of slack).

**Orbit enumeration (orbit_bfs.c).** BFS over all orientations under
⟨translations, GL(n,2)⟩ with completeness checksum (orbit sizes sum to
2^{N−1}): n=2: 2 orbits ✓, n=3: 4 ✓, n=4: 14 ✓ (all matching the audit's
independent Burnside counts; n=4 orbit structure: delta 16, runner-up
560, bent classes 448+240 at D ≈ 0.98/1.02 ✓). n=5 run (2^31 states)
in progress.

**Theorems A/B/C written into the deliverable (§6b), proofs complete:**
- A (universal abyss): min X ≤ N·exp(−2‖h‖₂) for EVERY sealed law.
- B (defect threshold): delta ⇔ min_s m < 2h_min ⇔ w_max > B − 2h_min.
  L0 ⇔ [D ≤ c₀ forces ℓ¹-budget saturation to within 2h_min].
- C (sign-rigidity dominance): φ₁·N/(N−1) > √((N−1)V₂) ⇒ the SIGN
  pattern is delta at the deep point ⇒ (Theorem 1 uniqueness) the law IS
  the delta law. Exact threshold φ₁² > (N−1)³‖h‖₂²/(N²−N+1); the delta
  satisfies it with relative margin ~1/(2N) (exactly calibrated: at delta
  φ₁ = (N−1)α⋆ exactly, V₂ = O(N²u⋆²)). Key insight: only the SIGNS need
  to be identified — uniqueness finishes; no analytic identification of
  the law needed.

Both B and C isolate the same remaining enemy: multi-dip spreading of the
depth/fluctuation budget. That is exactly L0's open core (§5 matching).

## 2026-07-02 — Campaign progress 2: THEOREM D — rigorous dip reduction

Major step: the "idealized dip model" of §5 is now a THEOREM with explicit,
N-uniform constants (deliverable §6c). For D ≤ c₀ ≤ 1/200, with dips
𝒮 = {X ≤ ½} (depths β_s = −log X(s)), spikes {X > 2}, bulk the rest,
F(a) = Σ_𝒮 β_sχ_a(s):

- **(D0)** 𝒮 ≠ ∅ for N ≥ N₀(c₀) (via Theorem A).
- **(D1) full spectrum + sign readout:** |ĝ(a) + F(a)/N| ≤ ε_G = 2.5√(2c₀),
  |F(a)| ≥ N(h_min − ε_G) for ALL a, and **σ_a = −sgn F(a)** — the
  orientation is read off the dip configuration. (Key input: spike-log
  ℓ¹-mass ≤ N√(2c₀)/4·2 via mean-matching E(X−1)₊ = E(1−X)₊, which keeps
  ε_G constant-scale — earlier worry about c₀·log N growth resolved.)
- **(D2) dominant-dip kill:** β_max ≥ Σ_rest β ⇒ sgn F ≡ χ(s₁) ⇒ σ = delta
  at s₁ ⇒ (Theorem 1 uniqueness) the law IS the delta law ⇒ k = 1.
  Corollaries: k = 2 impossible (equal depths kill |F| on half the masks;
  unequal is dominance); non-delta ⇒ k ≥ 3 with NO dominant dip.
- **(D3) depth scale:** Σβ ≥ (N/2)log(1/(Cc₀)) always (bulk-ℓ² budget
  Στ² ≤ 4c₀ forces every u_a ≤ C′√c₀-ish, so the total dip depth is Θ(N)).

**Consequence: L0 ⟺ L2′**, the single irreducible open lemma:
> L2′: no sealed law with D ≤ c₀ has a balanced (no dominant depth) dip
> set of size k ≥ 3 (n ≥ n₀).

**Documented negative finding (important):** for the balanced
3-of-an-affine-plane configuration (the shape of the n=4 runner-up), ALL
budget-level accounting — ℓ¹/ℓ²/counting/Jeffreys, spike bounds, bulk
tilts — is self-consistent at scales β ~ (N/2)log(N/c₀), ū ~ √(c₀/N).
So L2′ CANNOT be proved by budget accounting alone; it requires the exact
fixed-point coupling between the bulk x-tilt τ and bulk log-tilt η (same
bulk values, η ≈ τ, with |η_a| forced to track e^{−|F(a)|/N}). This
explains structurally why the problem has resisted: every relaxation that
forgets the τ–η coupling admits the balanced-k≥3 phantom.

Next: n=5 BFS still running → cert_n5; then hostile audit of §6b/§6c;
then final status.

## 2026-07-02 — Campaign progress 3: THE 1/N LANDSCAPE — constant floor is FALSE

**Correction of the record:** the earlier "min non-delta D ≈ 0.33 floor"
claims (n=5,6 probes) were LOCAL-SEARCH ARTIFACTS. Solving the seal for the
balanced 3-dip family directly (σ_a = +1 iff a ⊇ {bit0,bit1}; = the exact
runner-up orbit at n=3,4) gives:

| n | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| N·D | 4.766 | 5.249 | 5.460 | 5.523 | 5.540 | 5.544 |

**D ~ 5.545/N → 0.** So there is NO absolute constant floor: T2 and the
constant-c₀ form of L0/L2′ are FALSE as stated. The delta wins by a
constant FACTOR, not a constant gap. This explains, structurally, the
resistance of the problem to every slack-based method: the true statement
is a sharp constant-factor race at scale 1/N.

**Exact asymptotics found (and matched to 4 digits):**
- 3-dip family: N·D → κ₂ = 4·log4 = 5.545177. Limit shape: dips {s₁,s₂,s₃}
  (depths β ≈ N·log(N/4)), spike at the 4th plane point with X → 4
  EXACTLY (forced: it zeroes the (+,+)-class x-coefficients and balances
  the plane's mass), bulk → 1 + o(1/N), u-levels {4/N on |F|=β classes,
  64/N³ on the (+,+) class}.
- j-flat generalization (σ = +1 iff a ⊇ bits 0..j−1):
  N·D → κ_j = 2^j·log(2^j/(2^{j−1}−1)): κ₃ = 8log(8/3) = 7.846 ✓ measured
  7.8458. Increasing in j ⇒ the 3-dip family leads.
- Delta: κ₁ = 1.

**THE LIMIT PROBLEM (new; the tractable form of the asymptotic theorem).**
Sequences of sealed laws with N·D bounded converge (to be made rigorous by
compactness) to finite configurations: dead points K₀ (X → 0, depths
β_s = N(logN − log c_s), c_s > 0), finite-value points (s_i, ξ_i ∈
(0,∞)\{1}), bulk → 1. Writing m_a = Σ_{K₀}χ_a(s) ∈ Z and
Φ(a) = Σ_i(ξ_i−1)χ_a(s_i) − Σ_{K₀}χ_a(s), the seal passes to the limit as:
  (i) |m_a| ≥ 1 for every a ≠ 0 (limit full-spectrum condition);
  (ii) Φ(0) = 0 (mass balance) and Φ(a) = 0 on every class with |m_a| ≥ 2;
  (iii) on |m_a| = 1 classes: sgn Φ(a) = −sgn(m_a) and the magnitude
  matching log|Φ(a)| = (signed c-form) — linear in {log c_s};
and the limit cost is **N·D → κ = |K₀| + Σ_i ψ(ξ_i)**, ψ(x) = xlogx−x+1.
Solved cases (all rigorous given the limit formulation):
  - |K₀| = 1: forced to the pure delta, κ = 1 (spikes impossible: a mask
    ⊥ the spike-differences would give Φ = 0 on an |m|=1 class).
  - |K₀| = 2: impossible (m_a = 0 on half the masks).
  - |K₀| = 3: three points always span a 2-flat; Φ ≡ 0 on the |m|=3 class
    forces per-coset balance: the unique completion is ONE spike at the
    4th plane point with ξ = 4: **κ = 3 + ψ(4) = 4log4, uniquely**.
  - |K₀| = 4: impossible (Parseval counting: (2^r−1)·4 + 16 ≤ 2^r·4 fails).
  - |K₀| = 6: Parseval allows it only in dimension ≥ 4; κ ≥ 6 > 4log4.
  - |K₀| = 5: κ ≥ 5; whether spike-costs can be pushed below 0.545 is
    constrained by (iii) (not yet resolved — the γ/c-matching is the
    binding constraint; the j=3 family realizes 8log(8/3) = 7.85).
**Restated open lemma (the true one):**
> **L0-ratio:** ∃κ⁎ > 1, n₀: for all n ≥ n₀, every non-delta orientation
> has N·D ≥ κ⁎. (Conjectured sharp: liminf of min non-delta N·D = 4log4.)
Proof shape now visible: (a) compactness/limit-extraction at scale 1/N
(quantitative version of the above); (b) the finite limit problem: any
admissible limit config with K₀ ≠ delta has κ ≥ κ⁎ (κ ≥ 2 already follows
from |K₀| ≥ 2·-impossible → ≥ 3 once |K₀| ∈ {1,2,4} are settled as above —
i.e. **κ⁎ = 3 is within reach**, pending |K₀| = 5,7,... spike-cost floors
≥ 0 which hold trivially since ψ ≥ 0: κ ≥ |K₀| ≥ 3 for ALL surviving
non-delta configs!). So modulo the compactness step, the limit problem
gives κ⁎ = 3. The remaining analytic work: (a) rigorously; then the finite
window n < n₀ by certified computation.

## 2026-07-02 — Campaign progress 4: n=5 CERTIFIED; theorem now stands for n ≤ 5

- orbit_bfs (C, 2^31 states, ~40 min): **exactly 176 orbits**, checksum
  2147483648 = 2^31 exact (completeness by construction). Matches the
  audit's independent Burnside count. Cross-checks n=2,3,4: 2/4/14 ✓.
- cert_n5.py: certified Kantorovich solves (mpmath dps 40) of all 176
  representatives: **zero failures**. Delta orbit (rep 0, size 32)
  uniquely minimal, D = 0.03174869831458030115699628 (enclosure-matched
  to the certified scalar value). Worst certified non-delta margin
  0.138872685663742 (orbit rep 2040). Certified D-errors ≤ 1e-33.
- Landscape confirmation: the five lowest orbits are delta (0.0317),
  the balanced 3-dip family (rep 2040, size 4960, D = 0.170621384 —
  matches the family computation to 9 digits), 0.234707 (rep 498144),
  the j=3 family (rep 30, 0.243618), and 0.405832 (rep 109268 — the
  config my n=5 local search had found and mistaken for the runner-up).

**STATUS: Global Delta Optimality is now established for all n ≤ 5**
(equality exactly on the delta orbits), by certified computation
(faithful-mpmath trust base; interval arithmetic = final polish).
Remaining open: L0-ratio for n ≥ 6 (κ⁎ > N·D_δ-scale), with the §8b/log
limit problem giving κ⁎ = 3 modulo the compactness step. Awaiting the
hostile-audit workflow on Theorems A–D + certification methodology.

## 2026-07-02 — Campaign progress 5: hostile audit returned — ALL THEOREMS CONFIRMED

Three independent verifiers (fresh solvers, exhaustive n ≤ 4 sweeps,
dps-250 delta calibration, 200k adversarial dominance configs, stress
tests to n = 10): **Theorems A, B, C, D all TRUE — zero falsifications.**
Highlights beyond confirmation:
- Theorem C: V₂ = 0 EXACTLY at the delta (w two-valued ⇒ ψ ≡ 0) — my
  O(N²u⋆²) hedge was an understatement. And C is sharp from the false
  side too: 1-defect laws approach the dominance threshold with deficit
  → 0 (ratio 0.99999974 at n=8): B and C are exactly calibrated on BOTH
  sides — no relaxation possible.
- Theorem B: the 2h_min threshold is ATTAINED by every 1-defect
  orientation (min m = 2h_min exactly, h minimized at the flipped mask):
  strictness is load-bearing with zero margin.
- Theorem D: verified end-to-end incl. Pinsker normalization (sharp to
  0.99999997), the two calculus bounds (with cutoff margins: |log x| ≤
  2|x−1| first fails at x ≈ 0.203; ψ ≥ (x−1)²/4 first fails at x ≈ 5.12),
  and the dominance sign-inequality (200k configs, zeros only in the
  equality case, correctly excluded via D1). (D0) STRENGTHENED: k ≥ 1
  needs no N₀ — k = 0 makes F ≡ 0, so h_a ≤ ε_G < h_min directly.
  (D3)'s absolute constant: C = 9 explicit. One wrong parenthetical
  fixed (2ε_G = 0.50, not 0.36, at c₀ = 1/200; conclusion unaffected).
  (D2)'s k=1 line completed (A⋆ = u⋆^N(1+u⋆) < ½).
- Certification: Kantorovich + Lipschitz transfer independently reproved
  and stress-tested (min slack ratio 5.4). Two trust-base caveats fixed
  in the note: delta-enclosure rounding (~5e-62, absorbed by 60 orders),
  theoretical NaN channel (closed by exhaustive finiteness sweep;
  hardening recommended). n=5 count 176 doubly certified (BFS checksum +
  independent exact Burnside over all of GL(5,2); the match also proves
  the generators generate the full group). The auditor's "orbits_n5.txt
  missing" error was a timing artifact (its snapshot predated BFS
  completion; the run finished checksum-OK and cert_n5 passed with zero
  failures).

All repairs applied to the deliverable (§6b calibration note, §6c D0/D2/
D3 fixes, §8a trust-base notes).

## 2026-07-02 — CANDIDATE COMPLETE PROOF: Theorems E and F written

The compactness step is NOT needed. Realization: only the COUNT of
nearly-dead dips matters, and (D1)+(D2) control it at the moderate
threshold c₀ = 1/60 (where h_min ≥ ½log30 = 1.7006 > 2ε_G = 0.9129, so
Theorem D applies verbatim — its proofs are parameterized by that
hypothesis alone, not by "c₀ ≤ 1/200").

**Theorem E (deep-dip trichotomy):** non-delta sealed law with D ≤ 1/60
⇒ N·D ≥ 3ψ(e⁻⁵) = 2.87871. Proof: split dips at Θ = 5; Σ_shallow <
5k ≤ 0.543148N; (D1) gives |F(a)| ≥ Nh' ≥ 1.24416N ∀a; then
m = #deep ∈ {0,1,2} each force a contradiction (m=0: |F| ≤ Σ_sh too
small; m=1: β₁ ≥ Nh'−Σ_sh = 0.70102N > Σrest ⇒ dominant ⇒ (D2) delta;
m=2: |β₁−β₂| ≥ 0.70102N ⇒ dominance margin Nh'−2Σ_sh = 0.15787N > 0 ⇒
delta), so m ≥ 3 and D = E[ψ(X)] ≥ 3ψ(e⁻⁵)/N.

**Theorem F (Global Delta Optimality, ALL n):** n ≤ 5 certified; n ≥ 6:
either D > 1/60 > 1/63 ≥ 1/(N−1) > D_δ, or D ≤ 1/60 and Theorem E gives
D ≥ 2.87871/N > 1/(N−1) > D_δ. Strict in both branches; equality exactly
on the delta orbit by translation covariance. **The win threshold is
N·D_δ < 64/63 ≈ 1.016, NOT the sharp constant 4log4 = 5.545 — the
photo-finish that defeated all slack-based methods was an artifact of
aiming at the sharp constant. 2.879 clears 1.016 with 2.8× margin.**

Numerical verification BEFORE write-up (log-domain — first attempt hit
float underflow at β ≈ N·log(N/4) ≈ 5700 and falsely flagged the (D1)
floor; log-domain computation confirms all steps): 3-dip family n=9,10,11
and j=3 family n=10,11 (the only known in-regime laws): every inequality
of E verified, sign readout exact, min|F|/N = 4.85–6.24 vs h' = 1.55–2.43.

Status: **submitted to hostile audit (4 independent verifiers) before
any claim of completeness.** Given today's three self-corrections, no
victory declaration until the audit returns.

## 2026-07-02 — AUDIT RETURNED: THE PROOF STANDS. PROBLEM SOLVED.

Four maximally-hostile independent verifiers (instructed to assume the
proof wrong; ~550k tokens, 145 tool calls, independent solvers):
**verdicts: proof-correct (hunt), proof-correct-with-repairs (×3).
ZERO fatal findings. ZERO gaps.** Highlights:

- Every load-bearing step of Theorem E re-proved by hand and machine:
  Pinsker normalization, ε_G = 2.5√(2D) re-derivation, simultaneous
  worst-case-at-D=1/60 monotonicity, the trichotomy including the
  m=2 equality/anti-alignment edge case, ψ facts, branch arithmetic.
- Confirmed: (D1)/(D2) are parameterized ONLY by h_min > 2ε_G (2.1×
  slack at c₀ = 1/60; hypothesis persists to D ≈ 0.035). No hidden
  circularity anywhere in the chain (dependency graph verified).
- Counterexample campaign: ~55,000 solves at n = 4..13 (perturbations,
  adversarial dip-derived sign patterns, direct m=2 attacks, random
  low-defect, greedy descent): ZERO violations; m-census over 4,570+
  non-delta laws: minimum deep count is 3; designed 2-dip patterns
  collapse to the exact delta law (D2's mechanism observed directly);
  the region D ≤ 1/60 at n = 6,7 is empty as Theorem E implies.
- All computational trust-base legs replicated on independent code
  paths (n=4 rescan exact; all 176 n=5 orbits re-solved, worst margin
  0.1388726856637 to 12 digits; Burnside 2/4/14/176 zero remainder;
  D_δ < 1/(N−1) certified at dps 100 for n = 6..14).

**Repairs found (all display/hygiene, zero effect on conclusions),
ALL APPLIED:** four constants safe-rounded (1.70059 / <0.543149N /
>0.701014N / >0.157865N; margins were 4–5 orders above the slips);
recovery fact (ii′) added (GL(n,2)-invariance of D — the one missing
one-paragraph lemma, load-bearing for the n=5 orbit reduction;
audit-verified numerically to 1.8e-15); Theorem F's precise trust-base
sentence adopted; §8b constant fixed (8log(8/3) = 7.84663);
verify_theorem_E.py receipt committed (runs green, all checks);
cert_scan.py NaN-hardened.

**FINAL STATUS: the Walsh Delta Global-Optimality Problem — the Real
Novel Problem of [WD] §4 — is SOLVED for all n ≥ 2, with equality
exactly on the spin-flip orbit of the delta:**
- n ≤ 5: certified computation (exhaustive n ≤ 4; 176-orbit transversal
  n = 5; worst certified margin 0.1389; faithful-mpmath trust base,
  directed rounding = remaining formality with 8–30 orders of slack).
- n ≥ 6: Theorems D(D1,D2) + E + F, fully analytic, all constants
  explicit and N-uniform. Win threshold 64/63; achieved 2.87871.
- Corpus impact: v8 Paper 5's chiral gap law upgrades from
  "[THEOREM at n ≤ 4; all-n modulo (Lμ)]" to THEOREM (the (Lμ) residue
  is discharged by this route — Theorem F implies [L*] directly);
  two-branch physics grounded; prefactor-1 asymptotics proved
  (N·D_δ → 1 with non-delta floor ≥ 2.879 > 1). v8 canon edits left to
  the author.
- The sharp asymptotic constant (min non-delta N·D → 4log4,
  conjectured) remains open as a refinement — the §8b limit problem is
  its natural route; it is no longer needed for the theorem.

`walsh-delta-explained-for-engineers.md` — plain-language, fully correct
walkthrough (hypercube → parity features → distributions → softmax →
seal with worked n=1 example tanh(h) = e^{−h} → score → delta → why hard
(the 1/N photo-finish) → status → SHARD role and literature placement).

## 2026-07-02 — Q&A: can a single finite n close the whole theorem?

Answer recorded for the record: **No** with current knowledge — no upward
transfer exists (products of sealed laws are not sealed: mixed masks get
zero coefficients vs the seal's u_a > 0; quotients not sealed either), so
each n is a separate statement and computation is capped at n=6 forever.
The correct finite object is the §8b LIMIT PROBLEM (n = ∞), not a finite
n. However, the answer flips to YES under one unproven lemma:

> **(M) monotonicity/lifting:** min over non-delta of N·D is
> nondecreasing in n (any version losing ≤ ~5× total also works).

Given (M), the certified n=5 value (32·0.170621 = 5.4599) beats the delta
ceiling N·D_δ < N/(N−1) ≤ 32/31 ≈ 1.033 for ALL n ≥ 5 — theorem done.
Data consistent with (M): certified minima 1.84, 4.77, 5.25, 5.46
(n = 2..5), increasing, all attained by the 3-dip family, → 4log4.
(M) is a uniform-in-n statement, likely as hard as the limit route, but
a restriction-map mechanism (orientation restricted to the bit_n = 0
mask subgroup) is testable numerically — candidate next experiment.


## 2026-07-02 — Standalone journal paper shipped (shard repo)

Per instruction: an independent, publication-grade mathematics paper for
the problem + solution now lives in the SHARD publishable-batch repo
(`/Users/felixrobles/workspace/shard`), fully self-contained (no isp/SHARD
dependencies, no [P] tags; "sealed" renamed to "self-calibrated"):

- `papers/paper-XII-walsh-delta.md` (source of record, ~1030 lines): full
  derivations of everything — existence/uniqueness (convex G_eps with
  coercivity proof), translation + GL covariance, the delta law in closed
  form (symmetry reduction via GL-transitivity + the scalar polynomial),
  D_delta < 1/(N-1), Pinsker bookkeeping, spectral floor + sign readout,
  dominance criterion, the deep-dip trichotomy with safe-rounded
  constants, assembly for n >= 6, the certified n <= 5 computation
  (Kantorovich + entropy-transfer lemmas proved; orbit reduction with
  generator proof; Burnside cross-check), sharpness section (3-dip family,
  conjecture 4log4), code manifest, references.
- `tex/paper-XII-walsh-delta.tex` via the house md2tex (extended
  additively with pipe-table + blockquote-display-math support;
  regression-tested against paper-I: byte-identical output).
- Code `w1`–`w5` + fresh canonical receipts (all green, all reproducible
  per the README protocol): w1 exhaustive certified n<=4; w2 orbit BFS
  (2/4/14/176 + checksums); w3 certified 176-orbit n=5 (path fixed to run
  from repo root); w4 in-regime family verification (now both families at
  n=9,10,11 + Lemma 5.1 checks); w5 NEW independent Burnside count in C
  (exact divisibility, 2/4/14/176).
- README: new "Standalone mathematics paper" section + receipt-map row;
  notes that XII discharges the global-optimality lemma left open by
  paper IX's receipt p9a (their "alternating-by-weight" orientation = the
  delta at the all-minus state).

Referee audit before finalizing (3 hostile journal referees): verdicts
minor-revision x3, ZERO fatal/major math findings; all findings fixed:
the two majors (unshipped cross-checks -> w5 shipped + Section 8.4
reworded to shipped-vs-development; md2tex table/math damage -> converter
patched, tex regenerated clean), the unsafe-rounding chain in Thm 6.1
(1.244163 now cited so 0.701014 derives exactly), h_a > 0 one-liner in
Section 1.1, margin 0.138873 -> 0.138872 (safe direction), entropy-error
global bound 1e-32, Burnside wording (translation-sum inside the GL
loop), j=1 remark, notation dip-transform F -> Phi, receipt-file
documentation. PDF compilation pending (no tectonic on this machine; tex
is ready and clean).
