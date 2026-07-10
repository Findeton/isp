# 3p1-lorentz2 — Lorentz II: the footprint instrument (the cross-section shape of the causal indicator)

**Status:** design note, 2026-07-10 (v9 round 40; LEDGER #96's named redesign). Receipt: `v9/code/dimwall_footprint.py` (pinned here, committed strictly before running). Reviews ON.

## 1. Why this instrument (the round-36 diagnosis, addressed at the root)

Round 36's exponent-fit discriminator voided at certification for three diagnosed reasons: chain lengths are tiny integers at this scale; both clocks share the causal-axis component; and the cone-shape signal lives at the EDGE of the cone, which pooled fits wash out. The footprint drops chains and fits entirely and measures the edge directly: for related pairs, the scale-free transverse position v = w/s (w = displacement transverse to the causal axis, s = the axial component) lies inside the cone's cross-section — a **ball** for the round (Lorentz) cone, a **regular simplex** for the orthant/dominance cone. The simplex has corners: its directional support from the centroid along a corner direction is 3× the support along a face direction (regular tetrahedron, the C = 3 case). The round ball's ratio is 1. Every related pair contributes; no fits; the anchors differ maximally by construction.

## 2. The instrument (pinned)

Per instance (relation + coordinates): standardize coordinates per component (the round-36 pinned diagonal affine). Causal axis d-hat: dominance families = the diagonal/sqrt(k); M4 = the t-axis. For every related pair (i ≺ j): d = X_j − X_i; s = d·d-hat; keep pairs with s ≥ s_min = 0.3 (pinned floor; v = w/s is unstable below it; disclosed); w = d − s·d-hat; v = w/s.

**Directions.** Dominance/web families (native frame, corners known by construction): corner directions c_a = normalize(P_perp e_a), a = 1..4, the transverse projections of the four coordinate axes — the tetrahedron's vertices; face directions = −c_a. M4 (round anchor, direction-blind by symmetry — the choice cannot matter, which is the fairness property): a pinned regular tetrahedron in the (x,y,z) transverse space: t1 = (1,1,1)/√3, t2 = (1,−1,−1)/√3, t3 = (−1,1,−1)/√3, t4 = (−1,−1,1)/√3, faces = negatives.

**The statistic.** Directional support h(u-hat) = the q = 0.9 quantile of {v·u-hat : pairs with v·u-hat > 0}. F = mean_a h(corner_a) / mean_a h(face_a). Round cone: F ≈ 1. Orthant cone: F substantially > 1 (the tetrahedral 3:1 support asymmetry, attenuated by the sprinkling measure — no magic constant pinned; the gate is separation, not a band).

## 3. Pinned gates (windows and builders verbatim from round 36: web_window Δ = 1024 central, NW = 256, corner mode C = 3 (M, L, α) = (32, 16, 0.75), kdir = per-slot Dirichlet mixing; anchors m4diamond and orthant4 at N = 256; seeds 20262000+; 5 per family)

- **Gf0 (certification — strict separation, no magic numbers):** min over 5 orthant-iid seeds of F  >  max over 5 M4-own-coordinates seeds of F. REFUSED ⇒ VOID-INSTRUMENT-V (named), stop before any web is read.
- **Gf1 (the baseline; registered [directional]: polyhedral):** F(corner C = 3 webs) printed with seed band; expected on the orthant side of the M4 band (min corner F > max M4 F would be the clean read; the printed classification is the deliverable either way).
- **Gf2 (THE MIXING QUESTION; [directional]):** mean F(kdir) < mean F(corner) — channel mixing rounds the cone. Either outcome decisive: movement toward the M4 band ⇒ Lorentzization-by-mixing lives; no movement ⇒ the finite-C polyhedral anisotropy stands as the framework's falsifiable prediction and the Lorentz fork is squarely posed.
- **INFO (ungated):** per-family per-seed F; pair counts after the s-floor; the full directional support tables h(±c_a); the corner/face profile for each family; the M4-frame-choice robustness probe (a second, rotated tetrad — must not move F beyond seed noise; if it does, the fairness disclosure fires).
- Exit 1 by design on any gate refusal.

## 4. Scope and kill-risks (registered)

The statistic reads the OCCUPIED cross-section under the sprinkling/growth measure, not the geometric cone boundary; density attenuation of the corner signal is expected and folded into the separation-gate design (no pinned constants). The per-component standardization is applied identically to all families (anchors included). Windowed webs carry their window relation verbatim from the round-36 builder. Named kills: (K1) the s-floor + quantile choice could under-power the separation — Gf0 catches it (that is what certification is for); (K2) web χ-coordinates are non-negative accumulations with resets — their standardized clouds may sit asymmetrically in the transverse space; the INFO tables expose this before interpretation; (K3) kdir's Dirichlet weights change per-slot scales — the standardization is per-component within-instance, absorbing global scale but not shape, which is the point.

## References

LEDGER #96 (the redesign, named); note-3p1-lorentz1 (the voided instrument + the builders and window conventions, reused verbatim); the round-35 scoped forms (paper 6 §6(i)); paper 14 Thm 2.1 (the direction-resolved shelf).
