# D43a (N1) — the Lie-Trotter rule-independence test of the free core

**Status:** CAMPAIGN PIN (strict; the receipt runs only against this
text), 2026-07-19. Parent: D43 #327 (audit verdict A2 — the orphan
open since v1 paper 1's closing remark: "whether both rules, after
the appropriate onset renormalization and continuum identification,
land on the same tangential bracket"; re-declared v2 paper 1 §11
burden 4, never executed). Receipt:
`v10/code/d43a_lie_trotter_exact.py` (mpmath dps 80).

## 1. What is at stake

The click-law lineage's coefficient anchor exists only under the
collar-excision rule. If the onset-renormalized exchange bracket is
rule-relative, part of the identified law's foundation is a
regularization artifact. v1 paper 8 settled the WITHIN-class
question (the λ-family: raw A⁽²⁾ differs interior-shell-only;
normalized strip moments coincide) and explicitly deferred the
CROSS-class one: "The Lie-Trotter benchmark remains a different
onset class and is therefore an explicit contrast, not a same-order
comparator, at this stage." This receipt is that deferred
comparison.

## 2. The fixture and rules [ported verbatim from v1 p1 / v2 p1 /
## the root validator — no reconstruction]

1+1D periodic lattice, L sites, 2-component spinors (α = σx,
β = σz), a = 1, one free parameter m. H_D = Σ m·β_n + Σ k_{n+1/2}
with K = −(i/2)·α(T₊ − T₋). For a region R: C_R = Σ_{n∈R} m·β_n +
Σ_{bonds meeting R} k; B_R = H_D − C_R. Rules:
- **EXC:** U_R = exp(−iΔ·B_R).
- **LT:** U_R = exp(−iΔ·B_R)·exp(−iΔ·C_R) (bulk-then-collar).
Γ(U) = entrywise |U|² (Born-squared; the validator's convention);
comparison map J_R(Δ) = Γ(U_R)·Γ(exp(−iΔ·H_D))⁻¹; exchange defect
E_{R,S} = J_R·J_S·J_R⁻¹·J_S⁻¹. Singletons R = {n0}, S = {n0+d}.

## 3. Committed anchors (must reproduce before the new content runs)

- **AN1:** EXC singleton J_n = I + Δ²·A_n⁽¹⁾ + O(Δ⁴) with the v2 p1
  exact entries (diagonal (n,s),(n,s) = 1/2 at a = 1; the
  off-diagonal (n±1, s̄),(n,s) structure per v2 p1 lines 142-146,
  read at run-build time and hard-coded as Fractions).
- **AN2:** the v1 p1 documented exchange-commutator entries at the
  documented case (the ±1/8 ↑↓-channel values, v1 p1 line ~532).
- **AN3:** the LT onset law: E^LT − I = O(Δ^{2·max(4,d)}) — the
  sub-onset fitted coefficients vanish at 1e-40.
- **AN4 (λ-family self-check, one value):** the EXC c_λ = λ(2−λ)
  scaling at λ = 1/2 (normalized coefficients c-invariant).

## 4. The pinned test (the new content)

For d ∈ {2, 3} at L = 12, m ∈ {1/2, 1} (two mass points — the
bracket is mass-carrying via β):
- **T1 (onset extraction):** fit each rule's E − I on its own even-
  power ladder; extract the leading coefficient MATRIX B^rule_d at
  the rule's own onset order (EXC: Δ^{2d}; LT: Δ^{2max(4,d)}).
- **T2 (THE RULE-INDEPENDENCE TEST):** does there exist a single
  scalar κ_d (per d, allowed to depend on d and m only through the
  documented onset-constant structure) with B^LT_d = κ_d·B^exc_d
  entrywise at 1e-40? Report the verdict per (d, m):
  - PROPORTIONAL (all entries, one κ) → the tangential bracket is
    rule-independent at this order — the POSITIVE certificate.
  - STRUCTURED (proportional on the boundary-facing/strip-moment
    entries — the p8 decomposition, ported: entries with site
    components at graph distance ≥ d−1 from both interiors — while
    interior-shell entries differ) → the p8-class refinement: raw
    nonuniversality, normalized-strip universality. Report both
    parts exactly.
  - DIVERGENT (strip entries not proportional) → THE ALARM: the
    foundation is rule-relative; every downstream coefficient claim
    needs re-scoping. (Pre-registered outcome; the receipt exits 0
    on any of the three verdicts delivered exactly — the FAILURE
    mode is only extraction/anchor breakage.)
- **T3 (mass dependence):** κ_d(m) printed for both masses; whether
  κ is m-independent (a pure onset constant) or m-carrying is part
  of the verdict.

## 5. Scope

One fixture (the v1 free core), singletons, d ≤ 3, L = 12, two mass
points — the ORPHANED question at its original grain, not a general
regulator theorem. Interacting (p15-fixture) cross-check is the
named successor if T2 returns PROPORTIONAL/STRUCTURED. Precision:
mp.dps = 80; fits on Δ ∈ {3,4,5,6,7}×10⁻² (Vandermonde exact-solve
pattern); thresholds 1e-40 (Δ⁸ coefficients at these Δ are ≥ 1e-13
— 27 digits of margin).

## 6. First-run amendment (2026-07-19, pre-round; the E-level verdict
## stands, the bracket-level test added)

**A1 (the E/bracket distinction, found at first exact run).** T2 as
pinned compared the full defect coefficients B^rule at each rule's
onset. Delivered exactly (series arithmetic, all anchors 1e-30):
DIVERGENT at all four (m, d) cells with EXACT RATIONAL mass-dependent
ratios (kappa = -137/2304, -13/48, -7/288, -11/24) and O(1) strip
deviations — the raw defects are genuinely non-proportional. BUT the
LT defect at Delta^8 is NOT the pure exchange bracket: it mixes
[A^LT_R, A^LT_S] with second-order one-region cross terms. The
orphan's actual question ("the same tangential bracket after onset
renormalization and continuum identification") lives at the
ONE-REGION-COEFFICIENT COMMUTATOR level — v2 p1's own object.
**T4 (added):** extract A^rule_R = the leading one-region J
coefficient (EXC at Delta^2, LT at Delta^4); compute the direct
commutators C^rule_d = [A^rule_R, A^rule_S] for d in {1, 2, 3}; test
C^LT_d proportional to C^exc_d (one constant per (m, d); the same
three-way verdict). T4, not T2, decides the orphan; T2's raw-defect
divergence stands as its own delivered finding.

## 7. Round-1 amendments (2026-07-19; round frozen at #336)

**B1 (F1 — the T4/T2 distinction was empty).** §6's cross-terms
rationale was FALSE: E^LT[Δ⁸] = [A^LT_R, A^LT_S] EXACTLY (the J^LT
ladder is even-only; only (4,4) contributes) — referee-proved at
d = 1, 2, 3, both masses, both L. T4 is T2 extended to d = 1 plus
the d = 3 support corollary; nothing more.

**B2 (F2 — kappas are orbit representatives).** The per-cell d = 2
"kappa" was an argmax tie-break artifact: the max-magnitude orbit
carries THREE exact ratios ({−137/2304, −5/256, +79/2304} at
m = 1/2; {−7/288, −3/128, +13/576} at m = 1). DIVERGENT is
unaffected; kappa reporting is replaced by the full spectrum + the
orbit-free channel-moment ratios. LOG #332's kappa list is
non-canonical (forward-noted).

**B3 (F3 — STRUCTURED restated).** §4's strip clause was vacuous as
worded (empty EXC strips). Restated p8-faithfully: STRUCTURED =
proportional CHANNEL MOMENTS in the p7 strip basis (F/S/T) with
zero residual outside the basis. Under the repaired clause the
verdict is STILL DIVERGENT (six distinct channel ratios; 12 LT
residual entries — referee-verified), so the delivered outcome
stands with the clause corrected.

**B4 (F4 — THE SMEARED ANSWER; the alarm re-aimed).** The round
computed the corpus's own v2 p1 §5 continuum identification for
both rules: the lattice channel data genuinely differ (LT carries
δ = ±3, ±4 channels), but everything collapses to the SAME
tangential operator ray K_par[β] = (β∂x + ½∂xβ)(I − α) at leading
order, with ONE per-mass constant across both derivative layers:
κ(1/2) = 13/2304, κ(1) = −1/72. THE SIGN FLIP is a new no-go: no
shared-generator Theorem-3 class (c² > 0) can underlie both rules —
bracket-ray universality holds WITHOUT that mechanism. RE-SCOPE:
rule-relativity is real at lattice-entrywise scope (normalization
and sign of the constant); the bracket's OPERATOR CONTENT is
rule-independent at this order. The blanket downstream re-scoping
obligation of #332 is WITHDRAWN and replaced by: (i) constants are
rule-class data, operators are not; (ii) named successors — the
LT-side log-smeared finite-slab theorem; κ(m) as an exact function
(locate the zero crossing); the interacting p15-fixture cross-check.

**B5 (F6-F9 — process/precision).** §5's precision is corrected to
the as-run dps 50 / 1e-30 / exact-series (the pinned 80/1e-40 was
the fit-era spec). "Pre-registered" scopes to T2; §6's T4 entered
with the green commit, not before it (the retro-fit owned —
the #304 precedent class). Dead code removed; the completeness
checks (odd E^LT orders vanish; AN1 off-support vanishing) added;
"seed-independent" replaced by "deterministic, rerun byte-identical".

**B6 (delta findings).** §5's precision text is superseded by B5
(as-run dps 50 / 1e-30 / exact series — this pointer is D6's fix).
The delta's reconciliation: the tau tables are the SAME OBJECT in
the SAME convention (delta-odd in every channel); the receipt's
four (-2/-4, same) reference signs were transcription errors, fixed;
the gate upgraded to signed equality with no extra keys. chi0 is
delta-re-verified bidirectionally (same kappa on both layers); the
in-receipt chi0 gate is a successor nicety. Terminal statement
endorsed as phrased by the round.
