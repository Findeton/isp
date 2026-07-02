# PHASE-0 LEDGER — PART B (v7 papers 10–19)

Source: `/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper10-*.md` … `paper19-*.md`. Graded by the papers' fine print (scope/non-claims/precision sections), not abstracts. Receipts live in `/Users/felixrobles/workspace/isp/v7/code/`.

## Paper X (paper10-spin2-carried-helicity2-modeblind)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| Record stress carries spin-2 tensor structure: dipole forbidden, traceless quadrupole radiating at 2ω (period π), pure l≥2; sympy-exact on binary source. | DERIVED | X (SHARD-owned) | p10_spin2_pricing.py | — | 4 |
| Record stress is conserved symmetric rank-2 current (massless on-shell, sympy-exact) = exactly Weinberg's soft-graviton source; universal helicity-2 coupling follows. | CONDITIONAL(Weinberg soft-graviton uniqueness, imported) | X + Weinberg (ext lever) | p10_spin2_pricing.py | — | 4 |
| Weinberg–Witten no-go evaded: record stress is an emergent internal modular current, not the fundamental Poincaré charge — standard emergent-gravity evasion. | POSITED | X (argument, ext no-go) | — (argued, unreceipted) | — | 4 |
| Graviton's two physical polarizations record-blind: TT projection (5→2 dof) needs propagation direction (metric continuum) + canonical +/× mode frame (fifth wall). | NO-GO | X | p10_spin2_pricing.py (counting only; wall attribution argued, unreceipted) | Direction leg RECLASSIFIED by XI (r1): order-owned, scale-free, manifoldlikeness-gated — no longer "premature/unbuilt" | 3 |
| Earlier corpus attributions of the missing propagating content (3+1-dimensionality, lattice shape, holography — v6 p52 lineage) replaced by metric+mode wall attribution. | RETIRED | X (vs v6 p52/p55 guesses) | — | Superseded by X §4 re-attribution; direction half further moved by XI | L |

## Paper XI (paper11-order-owns-direction-manifoldlikeness-gate)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| Order → conformal: dimension, null cones, scale-free directions recovered from pure record causal order (Malament–HKMM + Myrheim–Meyer; d_MM 2.01/3.01, link slope→1, boost/dilation-invariant). | CONDITIONAL(manifoldlikeness; Malament/MM theorems imported) | XI + ext theorems | r1_order_to_conformal_direction.py (9/9) | — | 4 |
| Paper X's propagation direction reclassified: order-determined and scale-free (bit-identical under dilation), gated only by manifoldlikeness — NOT the l_step wall. | CONDITIONAL(manifoldlikeness) | XI | r1_order_to_conformal_direction.py | Supersedes X's "premature/unbuilt" grading of the direction input | 4 |
| Seal count is an unbiased Poisson volume counter E[N]=V/l_step^d (bias 0.5%, Var/E 0.97); volume ratios weight-0 owned to 1.5%. | DEMONSTRATED | XI | r2_number_volume_lstep.py (6/6) | — | 4 |
| Absolute physical volume is weight +d and walled — the l_step no-go recurring on the volume/conformal-factor axis; closed only by INPUTTING G. | NO-GO | XI (recurrence of III/57 wall) | r2_number_volume_lstep.py | — | 4 |
| Manifoldlikeness named as the field-shared gate under tiers I–II: KR orders dominate 2^{n²/4}; single MM estimator fooled (d_MM 2.38; unmasked by height 3 vs 46). | OPEN (field-shared gate, not a SHARD wall) | XI + Kleitman–Rothschild (ext) | r3_manifoldlikeness_myrheim_meyer.py (17/17) | r3 check-count corrected to 17 (fix already in paper) | 4 |
| Click-law offers no proven lever on manifoldlikeness; v6 paper1's "non-discriminating finite-sprinkling drift" read as the first symptom. Hauptvermutung leg also open. | OPEN | XI (reading of v6 p1) | — (argued from r3 + external dominance theorem) | — | 4 |
| Headline conditional: the emergent metric continuum is buildable up to the single scale l_step, GIVEN manifoldlikeness (order→conformal, number→volume). | CONDITIONAL(manifoldlikeness; G input closes volume normalization) | XI | r1+r2+r3 | — | 4 |

## Paper XII (paper12-transverse-nogo-envelope-forced)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| Transverse no-go: no record-internal self-consistency forces χ_AB — M1 capacity blindness (faithful Fisher marginal-only, λ-spread 1.3e-141) + M2 field blindness (qubit→rebit moment-algebra invariance). | NO-GO | XII (settles IV's named open question) | p6_transverse_nogo.py (42/42), p6c_alternative_capacity.py (5) | — | 3 |
| Mechanism classification: an invariance/capacity-degeneracy obstruction at weight-0 — structurally DISTINCT from the weight-(+1) grading-homomorphism scale/Newton-G no-go (Paper 57). | DERIVED | XII | p6_transverse_nogo.py PARTs 0–4 | Consistent with the corpus-wide scale-wall-weight-(+1) fix (cf. paper14 correction) | 3 |
| Holonomy escape closed: composite seal-loop invariant is the degree-≤3 moment polynomial or pure local gauge; only complex value needs an unhostable out-of-plane Y-seal. | NO-GO | XII | p6b_holonomy_phase_audit.py (21) | Resolves the corpus's flagged "retained-holonomy phase" | 3 |
| Neither sign nor magnitude of χ_AB is forceable: outcome-relabel involution blinds every magnitude functional; E_cl a free continuum 0→ln 2; balances drift with marginals. | NO-GO | XII | p6d_sign_magnitude.py (20) | — | 3 |
| Almost-quantum envelope forced FROM INSIDE: Γ⪰0 (Gram of own observables) entails no-signaling, Tsirelson 2√2, PR exclusion, I3322 strict outer nesting, monogamy facet CHSH²+CHSH²≤8. | CONDITIONAL(level-(1+AB) single-joint-outcome substrate premise; SDP digits solver-tol ~1e-9, PSD logic exact) | XII (upgrades IV's respected / VI's located envelope) | p6_transverse_nogo.py PART 5 | I3322 nesting per corpus-wide correction: 0.2514709 > 0.2509397 (FULL level-2) > 0.2508754 (Pál–Vértesi); paper carries corrected values | 2 |
| χ_AB remains a free Tier-A input up to Q̃; gap Q̃∖Q strict (NGHA 2015 + own I3322 receipt), level-independent (Slofstra); records force the fence, never the filling. | OPEN (residue; strictness IMPORTed from NGHA/Pál–Vértesi/Slofstra) | XII + ext | p6_transverse_nogo.py PART 5 | XIII thrice-proves the freedom; "experiment-fixed" tensor-product bit later regraded CONTESTED-CONVENTION (Renou reopening, XVI correction) | 3 |

## Paper XIII (paper13-feynman-map-chi-ab-bottoms-at-qtilde)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| Downstream ("Feynman") no-go: genuine super-quantum witness P*∈Q̃∖Q (CG-projector I3322, 0.2514709) pushed through geometry/correlation/covariance/matter/tripartite/order — breaks NOTHING; map bottoms out at Q̃. | NO-GO | XIII | s_probe_qtilde_minus_q.py (26/26), s_geom_chi_sweep.py (20/20), c3_covariance_chi_ab_probe.py (15/15), s_order_feedback_probe.py (18/18) | Round-1 witness was WRONG NPA level (bare-Q¹ ±1-correlator 8.748, gap-free encoding) — repaired to genuine CG-projector witness; I3322 nesting per corpus-wide correction | 3 |
| Spine: every downstream sector is a functional of the field-blind moment algebra M; the complex-over-real selecting bit (deficit +1/0, sympy-exact) lies in ker(M). Numeric sector identity true by construction. | DERIVED (structural claim load-bearing, numbers illustrative) | XIII | s_probe_qtilde_minus_q.py | — | 3 |
| Covariance recovers Q̃, not Q: microcausality = on-state commutation (witnessed tensor-free, prime-dim-3 space); P* sub-Tsirelson, passes all covariance gates. | CONDITIONAL(Paper VII Tier-B gates: emergent-Lorentz action, point-locality) | XIII | c3_covariance_chi_ab_probe.py (15/15) | — | 3 |
| Order-feedback path CLOSED: σ=D(P_AB‖P_BA) variable set sympy-exactly disjoint from χ_AB's; 200 re-wirings permute nothing; adversarial surrogate proves non-vacuity. | NO-GO (for the built generator; re-opens only under an unbuilt redefinition Paper I excludes) | XIII | s_order_feedback_probe.py (18/18) | — | 3 |
| Connectivity floor (new): connected emergent geometry REQUIRES χ_AB≠0 — only a globally-product node pinches off (Van Raamsdonk); carves the measure-zero face, not the Q/Q̃ gap. | DERIVED | XIII | s_geom_chi_sweep.py | — | 4 |
| Manifoldlikeness obligation (new): multi-record χ_AB magnitude pattern must be manifold-like; KR dominance makes this an unmet dynamical-selection rule, orthogonal to the complex/real bit. | OPEN (obligation stated; selection unproven — field-shared gate of XI) | XIII | s_geom_chi_sweep.py (R-invariance structural, non-vacuous) | — | 4 |
| Tripartite closure: interaction information and triangle invariant factor through M at degree-(1,1) — more NODES do not open the gap; higher cross-party WORDS untested. | NO-GO (premise-scoped to level-(1+AB) commitment) | XIII | s_geom_chi_sweep.py part iv | — | 3 |
| Residual = one bit = Tsirelson's problem (tensor product/local tomography/complex-over-real); whether even experiment fixes it now CONTESTED (Renou 2021 vs Hoffreumon–Woods/Maioli 2026) — plausibly an unfixable composition-rule convention, vindicating the un-forceable-import verdict. | OPEN (+ ext literature) | XIII + ext | — (literature; localisation via receipts above) | Supersedes retired "Renou ruled out real QM ⟹ experiment-fixed like G"; three-status meta-result (scale MEASURED / mode IMPORT-FIXED / tensor CONTESTED-CONVENTION) | 3 |

## Paper XIV (paper14-matter-sector-gap-mechanism-mode-wall)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| Interacting record Ginsparg–Wilson flow BUILT: large-N Gross–Neveu four-fermi gap equation on the record overlap operator — closes v6 paper14's named O8 remainder; novelty over quenched paper22. | DERIVED (constructive; scope: large-N, 2d, quenched, L≤10) | XIV | s_igw_production_gap_flow.py (9/9) | — | 5 |
| Exact Lüscher chiral symmetry survives the interaction: GW + Lüscher residuals <1e-90 (dps 120) in Q=0,1,2; breaking strictly O(M), soft; no hard doubler. | DERIVED | XIV | s_igw_production_gap_flow.py | — | 5 |
| Dynamical mass from chiral-SB (mass-WITHOUT-Higgs, record-natively): M=0 below g_c, monotone above; M(g²=4)=0.762/0.886/0.787 (Q=0/1/2); g_c² decreases 3.63→2.35 with L. | DEMONSTRATED (gap-equation traces lattice-numeric float64-flagged; root dps≥110) | XIV | s_igw_production_gap_flow.py | — | 5 |
| Record topology in the order parameter: M·V·Σ→n_zero (total COUNT n₊+n₋=2/1/2); topological INDEX n₋−n₊=Q the signed part; count=|index| only in mono-chiral sectors (Q=0 vector-like pair). | DERIVED | XIV | s_igw_production_gap_flow.py | R1 caught author's count-vs-index conflation (Banks–Casher); corrected + sharpened with explicit γ₅-chirality split, re-proved 3 ways | 5 |
| Canonical MODE is the third (matter) import-fixed wall: rank a superselection invariant; NO cross-sector common energy zero (shift (n′−n)ln2 state-independent, sympy-exact); selector Hamiltonian RELOCATES the choice (argmin switches for every monotone reward; no crossing equals a forced constant). | NO-GO | XIV (proves VIII's wall genuine) | s_mode_import_wall.py (16/16) | Epistemic status per revised meta-result: scale weight-(+1) MEASURED / χ_AB CONTESTED-CONVENTION / mode weight-0 IMPORT-FIXED by measured spectra | 3 |
| Chiral-gap VALUES are forced pure numbers: m_min(n)=−ln(1−2⁻ⁿ)−δ_n to 100+ digits, free of all three gated inputs; prefactor m·2ⁿ→1, adjacent ratios→2. | DERIVED | XIV (law from IX) | s_chiral_gap_ratios.py (14/14, dps 140) | δ_n>0 strict positivity verified only n≤6 (n≥7 underflow ~1e-130 flagged) | 5 |
| Between-species mass ratios SINGLY gated by the rank assignment alone — sharpens VIII's doubly→singly (chirality bridge and Wen-PSG cohomology collapse into the assignment; only limits assignment-free). | DERIVED | XIV | s_chiral_gap_ratios.py | Supersedes VIII's "doubly gated" grading | 5 |

## Paper XV (paper15-everpresent-lambda-scaling-weight-classification)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| SHARD reproduces Sorkin's everpresent-Λ SCALING δΛ~±V^{−1/2} (exponent exactly −1/2) as CLT on native Poisson seals; route A (conjugacy) ≡ route B (corpus's own drift ∇Λ=8πGη) sympy-exactly. | DERIVED (spine Sorkin/ADGS, cited; conjugacy bracket an import in route A; MC slopes flagged with exact targets) | XV + Sorkin/ADGS (ext) | p15a_routeA_conjugacy.py (13), p15b_routeB_drift_walk.py (13) | — | 4 |
| Weight classification (value-add over Sorkin): variance handle δΛ·l_step²=N^{−1/2} weight-0 record-ELIGIBLE; mean Λ₀ weight-(−2) walled; mean-sector weights disjoint from 0 ⇒ paper57 no-go AND paper42 drift both SILENT on the variance — a third category. | DERIVED | XV | p15c_weight_classification_nogo.py (27, sympy-exact) | — | 4 |
| De Sitter self-consistency: paper57's own mean obeys Λ₀~V_dS^{−1/2} — same −1/2 exponent as the fluctuation, ratio O(1); exponents match, absolute values stay weight-(−2) imports. | DERIVED | XV | p15d_desitter_selfconsistency.py (18) | — | 4 |
| Intensive SIGN native: universal −ΛV coupling makes Λ a degree-0 density (shrinks: V^{−1/2} not V^{+1/2}); ℏ literally absent from the exponent; unimodular gravity NOT load-bearing for sign or structure. | DERIVED | XV | p15f_routeC_action_density.py (23) | — | 4 |
| Zero-mean CENTERING of the Λ-kick is an irreducible IMPORT: residual collapses (three-way equivalence, residuals 0) to per-seal kick zero-mean + O(1)-variance = Sorkin's input (iv); unimodular gravity one packaging of exactly this posit. | IMPORT | XV | p15g_zero_mean_equivalence.py (19) | — | 4 |
| CURL-FREE OBSTRUCTION (the discovery): {sign-balanced} and {Λ-eligible} land on DIFFERENT objects — δη not curl-free → routed to decoherence; only one-signed heating mean w>0 sources Λ; seal one-signed (dχ=σ≥0) — mutually exclusive in SHARD's own construction; flip route named, OPEN, not no-go-barred. | DERIVED (structural reason, not merely unbuilt gap) | XV | p15g + v5 paper3 loci | §7's cited "[TARGET] decoherence-rate=seal-rate=σ" (paper56) since DISSOLVED into FDT proportionality D_B=κ·D_KL, κ→1/4 quarter law with exact running (pK1/pRUN_kappa_exact.py) | 4 |
| Numerology: physical δΛ~H² is l_p-FREE (needs only cosmic size R_H); 10^{−120} = (R_H/l_p)^{−2} tautology — the only place l_step=G enters; importing G adds no prediction, orthogonal to the centering obstruction. | IMPORT (Sorkin's numerology reproduced, not improved; d=4 forced by the match) | XV | p15e_numerology.py (14, dps 120) | — | 6 |
| Premise under the exponent: Poisson Var[N]=E[N] kinematics assumes manifold-like sprinkling — the field-shared manifoldlikeness gate (XI) sits under the −1/2. | OPEN | XV | — (disclosed premise) | — | 4 |

## Papers 16-18 (appended by the main-loop assembler, 2026-07-01; from the six-pass review of this date)

| RESULT (<=25 words) | STATUS | OWNER | RECEIPT(S) | SUPERSEDED/CORRECTED-BY | V8-DEST |
|---|---|---|---|---|---|
| Seal = physical mechanism candidate for Barandes division events (kin-in-spirit, not a claim on the correspondence) | POSITED | v7 paper16 | p18_seal_divisibility.py 26/26, f6 | seal forces scalar survival only, never the matrix kernel (Move-C abort) | 2 |
| Gamma>=0 (Gram of own seal observables) entails the almost-quantum envelope: no-signaling structure, Tsirelson 2sqrt2, PR-exclusion, I3322 strict-outer, monogamy facet | CONDITIONAL(records-as-operator-algebra committing level-(1+AB) words) | v7 paper16 (derivation in paper12) | p6_transverse_nogo.py 42/42 | I3322 level-2 corrected to full 0.2509397 (2026-07-01); no-signaling encoded in M-structure, not positivity per se | 2 |
| CG-projector I3322 strict-outer nesting 0.2514709 > 0.2509397 (full level-2) > 0.2508754 (Q, Pal-Vertesi PRA 82 022116) | DEMONSTRATED(SDP solver-tol) | v7 paper16/12/13 | p6, s_probe 26/26, c3 | corrected 2026-07-01 (was partial-level-2 0.2513864; third NPA-label incident) | 2 |
| Meta-result revision: three last inputs have THREE different epistemic statuses (scale MEASURED / mode IMPORT-FIXED / tensor CONTESTED-CONVENTION) | DERIVED(classification) | v7 paper16 | p17_classification.py 23/23 | supersedes "three experiment-fixed inputs" corpus-wide | 3 |
| Renou-2021 "real QM ruled out" retired -> contested composition-rule convention (Hoffreumon-Woods 2603.19208, Maioli 2604.19482, Renou 2604.07425) | RETIRED(correction) | v7 paper16 | - | the 2026 reopening; vindicates (not proves) un-forceability | 2,3 |
| Three-walls classification: SCALE+TENSOR genuine quotient-by-symmetry no-gos; MODE [STRUCTURAL]/[ANALOGY]; G-leg CONDITIONAL(Jacobson-Clausius) | THEOREM(2 of 3)+CONDITIONAL | v7 paper17 | p17_classification.py 23/23 | "carry exactly invariants" corrected to only-invariants/at-least-residual (2026-07-01) | 3 |
| Chiral-gap global optimality: PARTIAL_REDUCTION -- structural core all-n, [L*] reduced to seal-mean MARGIN lemma (Lmu): mT(eps)>=mT(mu*)+c, c>=0.5 verified n<=6; no counterexample to n=9 | OPEN(reduction in hand) | v7 paper18 | pD 17/17, pD2 10/10+6/6, pB_variational 9/9, hunt-to-9 | surrogate ratios 6.1/7.3/21.8 relabeled (true n=4 ~5.1); two-level closed modulo n<=20 step; multiset parenthetical corrected (2026-07-01) | 5 |
| Chiral-gap law m_min(n) = -ln(1-2^-n) - delta_n stands as Paper IX stated | THEOREM(n<=4 exhaustive; all-n modulo [L*]) | v7 paper9/18 | p9a reproduced | - | 5 |
