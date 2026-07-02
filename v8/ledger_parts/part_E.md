# PHASE-0 LEDGER, part E: RECEIPTS INVENTORY

Date: 2026-07-01. Scope: all `*.py` in `/Users/felixrobles/workspace/isp/v7/code/` (273 files) and `/Users/felixrobles/workspace/isp/v6/code/` (1 file). Docstrings/headers read only; receipts NOT run. Citations = literal filename grep over `v7/*.md`, `v6/*.md`, `v6/publishable/*.md` (paper names shortened: `v7-paperN`, `v6-paperN`, `v6-pub-*`; plan/note mds count as citers). ORPHAN = no .md mentions the filename (also checked stem without `.py`). CHECKS column is greppable structure (declared N/N in docstring; `check()` call sites; asserts; else print-report style), not a run result.

NOTE: the corpus was under ACTIVE concurrent edit during this scan (papers 11,12,13,14,16,17,19 have 2026-07-01 mtimes); the inventory reflects the state at generation time -- p19c_swerve_fdr.py was de-orphaned mid-scan by the paper19 update.

| RECEIPT | WHAT IT VERIFIES (<=15 words) | CHECKS (from docstring/greppable) | CITING PAPER(S) | ORPHAN? | NOTES |
|---|---|---|---|---|---|
| _r2_independent_hunt.py | R2-counterexample INDEPENDENT hunt for Paper XVIII (chiral-gap global-optimality lemma). | none found | — | YES | Paper18 R2 adversarial scratch (independent reimplementation); imported by other _r2_* |
| _r2_math_checks.py | Independent verification of the all-n math claims (A,B,D,E,F). | none found | — | YES | Paper18 R2 scratch: all-n math claims A,B,D,E,F |
| _r2_n6_n7.py | R2 n=6 and n=7 adversarial hunt + n=5 witness verification. Independent. | none found | — | YES | Paper18 R2 scratch: n=6,7 hunt + n=5 witness |
| _r2_nearalt.py | R2 near-alternating + structured perturbation probe at n=5,6,7. The non-multiset- | none found | — | YES | Paper18 R2 scratch: near-alternating perturbation probe |
| _r2_specifics.py | Verify specific numeric claims in the paper text. | none found | — | YES | Paper18 R2 scratch: paper-text numeric spot-checks |
| _r2_structured.py | R2 structured-family hunt: the families most likely to produce low-KL_1d multisets. | none found | — | YES | Paper18 R2 scratch: bent/Reed-Muller structured-family hunt |
| c1_lorentz_scalar_seal_mcc.py | MOVE C1 -- "Lorentz-scalar seal -> MCC (microcausality to all orders)". | print-report style (1 OK/PASS strings) | v6-pub-companion-E-covariant-decoherence, v7-paper7 | no |  |
| c2_bhs_collar_nogo.py | v7 C2 deferral probe -- why discharging Paper VII's covariance premise is BLOCKED on discreteness. | 1 asserts | v7-LONG_MARCH_PLAN, v7-note-C2-covariance-premise-deferral | no |  |
| c2_derived_noise_kernel.py | MOVE C2 -- DOES SHARD DERIVE THE LITERATURE'S COLORED LORENTZ-INVARIANT NOISE | 2/2 declared | v6-pub-companion-E-covariant-decoherence, v7-paper7 | no |  |
| c3_covariance_chi_ab_probe.py | R3 -- COVARIANCE PROBE on the free input chi_AB. | 12 checks declared; 15 check() calls; 1 asserts | v7-paper13, v7-paper16 | no |  |
| f1_born_projection_q2.py | Filter 1 (F1-kinematic-form) receipts, part 2. | 1 asserts | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1 | no |  |
| f1_kernel_positive_type.py | Filter 1 (F1-kinematic-form) receipts. | none found | v7-LONG_MARCH_PLAN, v7-paper1 | no |  |
| f3_self_consistency.py | FILTER 3 -- SELF-CONSISTENCY UNDER REFINEMENT. v7 Long March, Paper 1, Tier A. | 2 asserts | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1, v7-paper20, v7-paper21 | no |  |
| f3b_sparse_seal_shape.py | FILTER 3-B -- THE SPARSE-SEAL (GENUINELY-INDIVISIBLE) FORCED SHAPE. | none found | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1, v7-paper20, v7-paper21 | no |  |
| f3c_sequential_odometer.py | F3c -- THE SEQUENTIAL CONTENT-ODOMETER. v7 Long March, Paper 1, Tier A. | 7 asserts | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1, v7-paper20, v7-paper21 | no |  |
| f3d_foundational_supports.py | F3d -- THE TWO FOUNDATIONAL SUPPORTS of Paper 1 v7 s3.2's forcing chain. | 5 asserts | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1, v7-paper20, v7-paper21 | no |  |
| f3e_history_independence.py | v7 Paper 1 — f3e: the two dense-step premises (b1) single channel and (b2) stationarity, | 3 asserts | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1, v7-paper20, v7-paper21 | no |  |
| f4_variational_rate.py | FILTER 4 -- VARIATIONAL RATE. v7 Long March, Paper 1. | 2/2 declared; 4 asserts | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper1 | no |  |
| f5_oi_pi_consistency.py | FILTER 5 -- OI/PI CONSISTENCY WITH THE FORCED MULTIPLICATIVE SEALING SKELETON. | 20 check() calls; 1 asserts | v7-LONG_MARCH_PLAN, v7-paper4 | no |  |
| f6_unistochastic_record_blind_probe.py | F6 (PROBE) -- the transition-MATRIX level question, BEFORE the q=2 screen collapses | 11 check() calls; 1 asserts | v7-paper16 | no |  |
| global_frustration_optimum.py | receipt for Theorem 7.1 of the binding-codes paper. | 1 asserts | v6-pub-companion-F-chiral-matter, v6-pub-paper-C0-binding-codes | no |  |
| m2_mode_canonicalization.py | MOVE M2 (THE LINCHPIN). | 1 asserts | v6-pub-companion-F-chiral-matter, v7-LONG_MARCH_PLAN, v7-paper8 | no |  |
| m3_cm_hierarchy_mechanism.py | MOVE M3 -- does SHARD's record(slow)/substrate(fast)-mode split GENERATE the | 1 asserts | — | YES | Move M3 probe (c_m hierarchy as slow/fast mode split, Sahakian isomorph); unreferenced |
| move_C3_TS_factorization.py | MOVE C3 -- Residue B (interacting-field Tomonaga-Schwinger integrability) factorization. | 4 asserts | — | YES | Move-C3 covariance Residue-B probe; Move C ABORTED per plan, never folded into an md |
| nonadditive_entangling_complement.py | RECEIPT: The non-additive entangling complement (Investigation B). | 15 asserts | v7-LONG_MARCH_PLAN, v7-paper4 | no |  |
| p10_spin2_pricing.py | v7 Paper X, receipt -- the graviton spin-2 three-layer pricing. | 1 asserts | v7-LONG_MARCH_PLAN, v7-paper10 | no |  |
| p15a_routeA_conjugacy.py | p15a -- ROUTE A: the direct unimodular-conjugacy route to Sorkin's everpresent Lambda. | print-report style (3 OK/PASS strings) | v7-paper15 | no |  |
| p15b_routeB_drift_walk.py | ROUTE B (the corpus-NATIVE route to Sorkin everpresent Lambda). | 14 check() calls | v7-paper15 | no |  |
| p15c_weight_classification_nogo.py | SHARD v7 receipt -- the WEIGHT-CLASSIFICATION of the cosmological-constant | 27 check() calls | v7-paper15, v7-paper17 | no |  |
| p15d_desitter_selfconsistency.py | BONUS SELF-CONSISTENCY (NOT a tension, NOT a derivation): | 18 check() calls | v7-paper15 | no |  |
| p15e_numerology.py | CANONICAL receipt: SHARD vs the Sorkin everpresent-Lambda numerology. | 14 check() calls | v7-paper15 | no |  |
| p15f_routeC_action_density.py | ROUTE C -- the UNIMODULAR-FREE route to Sorkin's everpresent Lambda ~ V^{-1/2}. | 23 check() calls | v7-paper15 | no |  |
| p15g_zero_mean_equivalence.py | THE LAST RESIDUAL: does SHARD deliver the ZERO-MEAN sqrt(N) action walk natively? | 19 check() calls | v7-paper15 | no |  |
| p17_classification.py | SHARD v7 Paper XVII. THE CLASSIFICATION THEOREM. | 23 check() calls | v7-paper17, v7-paper20, v7-paper21 | no |  |
| p18_seal_divisibility.py | v7 Paper XVIII -- DOES THE SEAL SKELETON FORCE THE BARANDES / DOUKAS TRANSITION-MATRIX STRUCTURE, | 26 check() calls; 1 asserts | v7-paper16 | no | MISLABEL: docstring says 'Paper XVIII' but is the Move-C probe folded into paper16 (its only citer) |
| p19a_seal_swerve.py | Channel A seal-swerve: unique LI momentum diffusion, seal tie kappa=(1/6)sigma l_step^-3, bound | 23 check() calls; 1 asserts | v7-paper19 | no |  |
| p19b_norevival_blindness.py | Channel B: seal CP-divisible/no-revival, blind vs standard QM decoherence (BLIND_NO_ESCAPE) | 2/2 declared; 22 check() calls; 3 asserts | v7-paper19 | no |  |
| p19c_swerve_fdr.py | Channel A FDR: de Bruijn grounding of the swerve seal-rate tie; posited-status audit | 16 check() calls; 1 asserts | v7-paper19 | no | DE-ORPHANED MID-SCAN: was a known-orphan candidate; paper19.md (edited 2026-07-01 15:43) now cites it 19/19 (de Bruijn grounding, posited-tie audit) |
| p20_deterministic_machines.py | Receipt for v7 Paper XX: deterministic record machines. | 8 check() calls | v7-paper20, v7-paper21 | no |  |
| p21_record_martingale.py | Receipt for v7 Paper XXI: the record martingale principle. | 13 check() calls | v7-paper21 | no |  |
| p22_marked_manifold_audit.py | Receipt for v7 Paper XXII: marked compensators and finite-order | 46 check() calls | v7-paper22 | no |  |
| p23_aggregate_pair_palm_bracket_audit.py | Collapsed Paper 23 receipt: aggregate pair-Palm bracket audit. | 5 check() calls | v7-paper23 | no |  |
| p23_aggregate_pair_palm_source_audit.py | Collapsed Paper 23 receipt: aggregate pair-Palm source audit. | 5 check() calls | v7-paper23 | no |  |
| p23_asymptotic_bracket_identity.py | Collapsed Paper 23 receipt: asymptotic marked bracket identity. | 5 check() calls | v7-paper23 | no |  |
| p23_asymptotic_jittered_cluster_limit_audit.py | Collapsed Paper 23 receipt: asymptotic jittered-cluster limit audit. | 5 check() calls | v7-paper23 | no |  |
| p23_cycle_neutrality_signature_audit.py | Collapsed Paper 23 receipt: overlap-graph cycle-neutrality signature audit. | 5 check() calls | v7-paper23 | no |  |
| p23_degree_covariance_label_residue_audit.py | Collapsed Paper 23 receipt: degree-covariance hidden-label residue audit. | 5 check() calls | v7-paper23 | no |  |
| p23_diagonal_identity_rarity_bound.py | Collapsed Paper 23 receipt: diagonal hidden-identity rarity bound. | 5 check() calls | v7-paper23 | no |  |
| p23_direct_unlabeled_likelihood_ladder.py | Collapsed Paper 23 receipt: direct split unlabeled likelihood ladder. | 7 check() calls | v7-paper23 | no |  |
| p23_endpoint_symmetric_pair_flag_likelihood_audit.py | Collapsed Paper 23 receipt: endpoint-symmetric pair-flag likelihood audit. | 7 check() calls | v7-paper23 | no |  |
| p23_exact_palm_kernel_integral.py | Collapsed Paper 23 receipt: exact local Palm-kernel integral. | 5 check() calls | v7-paper23 | no |  |
| p23_growing_window_washout_bounds.py | Collapsed Paper 23 receipt: growing-window order-only washout bounds. | 5 check() calls | v7-paper23 | no |  |
| p23_hidden_partition_likelihood_audit.py | Collapsed Paper 23 receipt: hidden-partition likelihood/top-tail audit. | 5 check() calls | v7-paper23 | no |  |
| p23_higher_order_label_residue_audit.py | Collapsed Paper 23 receipt: higher-order hidden-label residue audit. | 5 check() calls | v7-paper23 | no |  |
| p23_invariant_aggregate_pair_palm_bracket_audit.py | Collapsed Paper 23 receipt: endpoint-invariant aggregate pair-Palm bracket audit. | 5 check() calls | v7-paper23 | no |  |
| p23_jitter_linear_washout_audit.py | Collapsed Paper 23 receipt: linear/superlinear jitter washout audit. | 7 check() calls | v7-paper23 | no |  |
| p23_jitter_scaling_exponent_audit.py | Collapsed Paper 23 receipt: jitter scaling exponent audit. | 6 check() calls | v7-paper23 | no |  |
| p23_jitter_scaling_phase_diagram.py | Collapsed Paper 23 receipt: jitter scaling phase diagram. | 6 check() calls | v7-paper23 | no |  |
| p23_joint_global_interval_bracket.py | Collapsed Paper 23 receipt: joint global-and-interval bracket calibration. | 5 check() calls | v7-paper23 | no |  |
| p23_linear_critical_kernel_audit.py | Collapsed Paper 23 receipt: linear critical-window kernel audit. | 5 check() calls | v7-paper23 | no |  |
| p23_linear_window_interval_variance_audit.py | Collapsed Paper 23 receipt: linear-window interval variance audit. | 4 check() calls | v7-paper23 | no |  |
| p23_linear_window_load_bracket_audit.py | Collapsed Paper 23 receipt: linear-window load/bracket audit. | 5 check() calls | v7-paper23 | no |  |
| p23_local_factor_inequality_audit.py | Collapsed Paper 23 receipt: local cross-likelihood factor audit. | 5 check() calls | v7-paper23 | no |  |
| p23_mecke_palm_poisson_audit.py | Collapsed Paper 23 receipt: order-only Mecke/Palm compensator audit. | 5 check() calls | v7-paper23 | no |  |
| p23_mesoscopic_rooted_flag_field_audit.py | Collapsed Paper 23 receipt: mesoscopic rooted pair-flag field audit. | 6 check() calls | v7-paper23 | no |  |
| p23_multiscale_interval_pair_covariance.py | Collapsed Paper 23 receipt: multiscale interval-pair covariance audit. | 6 check() calls | v7-paper23 | no |  |
| p23_n12_invariant_screen_selected_count.py | Collapsed Paper 23 receipt: N=12 invariant-screen selected-count audit. | 5 check() calls | v7-paper23 | no |  |
| p23_observable_label_information_audit.py | Collapsed Paper 23 receipt: observable hidden-label information audit. | 5 check() calls | v7-paper23 | no |  |
| p23_observable_law_metric_campaign.py | Collapsed Paper 23 receipt: observable law metric campaign. | 5 check() calls | v7-paper23 | no |  |
| p23_order_visible_bracket_variance_audit.py | Collapsed Paper 23 receipt: order-visible bracket variance audit. | 5 check() calls | v7-paper23 | no |  |
| p23_overlap_component_factorization_audit.py | Collapsed Paper 23 receipt: overlap-component factorization audit. | 5 check() calls | v7-paper23 | no |  |
| p23_overlap_graph_cycle_tax.py | Collapsed Paper 23 receipt: hidden-overlap graph cycle tax. | 5 check() calls | v7-paper23 | no |  |
| p23_overlap_graph_mgf_bound.py | Collapsed Paper 23 receipt: overlap-graph component mgf bound. | 5 check() calls | v7-paper23 | no |  |
| p23_pair_palm_signature_audit.py | Collapsed Paper 23 receipt: pair-rooted Palm-signature audit. | 5 check() calls | v7-paper23 | no |  |
| p23_palm_kernel_projection_audit.py | Collapsed Paper 23 receipt: local Palm-kernel projection audit. | 5 check() calls | v7-paper23 | no |  |
| p23_partition_overlap_poisson_bound.py | Collapsed Paper 23 receipt: hidden-partition overlap Poisson bound. | 2/2 declared; 5 check() calls | v7-paper23 | no |  |
| p23_reconstructed_coordinate_palm_audit.py | Collapsed Paper 23 receipt: reconstructed-coordinate Palm audit. | 5 check() calls | v7-paper23 | no |  |
| p23_recursive_interval_law.py | Receipt for v7 Paper XXIII: recursive interval laws and no hidden staging. | 55 check() calls | v7-paper23 | no |  |
| p23_rooted_palm_bracket_audit.py | Collapsed Paper 23 receipt: rooted/Palm bracket audit. | 7 check() calls | v7-paper23 | no |  |
| p23_selected_class_probability_formula.py | Collapsed Paper 23 receipt: selected-class P_N probability formula. | 4 check() calls | v7-paper23 | no |  |
| p23_selected_rare_class_n10_n12_audit.py | Collapsed Paper 23 receipt: selected rare-class audit at N=10 and N=12. | 5 check() calls | v7-paper23, v7-paper27 | no |  |
| p23_small_unlabeled_likelihood_second_moment.py | Collapsed Paper 23 receipt: small-N unlabeled likelihood second-moment proxy. | 5 check() calls | v7-paper23 | no |  |
| p23_split_sample_diagonal_artifact_audit.py | Collapsed Paper 23 receipt: split-sample diagonal artifact audit. | 8 check() calls | v7-paper23 | no |  |
| p23_sqrt_collision_poisson_law.py | Collapsed Paper 23 receipt: square-root collision Poisson law. | 5 check() calls | v7-paper23 | no |  |
| p23_stability_adversarial_limit_audit.py | Collapsed Paper 23 receipt: stability and adversarial-limit audit. | 8 check() calls | v7-paper23 | no |  |
| p23_transfer_operator_cycle_theorem.py | Collapsed Paper 23 receipt: transfer-operator cycle theorem. | 5 check() calls | v7-paper23 | no |  |
| p23_unlabeled_rare_class_stability_audit.py | Collapsed Paper 23 receipt: unlabeled rare-class stability audit. | 5 check() calls | v7-paper23 | no |  |
| p23_unlabeled_second_moment_ladder.py | Collapsed Paper 23 receipt: unlabeled likelihood second-moment ladder. | 5 check() calls | v7-paper23 | no |  |
| p23_unlabeled_second_moment_n8_stability.py | Collapsed Paper 23 receipt: N=8 unlabeled second-moment stability audit. | 5 check() calls | v7-paper23 | no |  |
| p23_washout_residue_dichotomy_bounds.py | Collapsed Paper 23 receipt: washout/residue dichotomy bounds. | 6 check() calls | v7-paper23 | no |  |
| p23_washout_two_sample_distance_audit.py | Collapsed Paper 23 receipt: two-sample washout distance audit. | 5 check() calls | v7-paper23 | no |  |
| p24_projective_fixed_point_law.py | Receipt for v7 Paper XXIV: projective fixed-point search for the record law. | 8 check() calls | v7-paper23, v7-paper24 | no |  |
| p25_interval_bracket_action.py | Receipt for v7 Paper XXV: calibrated interval-compensator bracket action. | 5 check() calls | v7-paper23, v7-paper25 | no |  |
| p26_quadratic_record_action_audit.py | Paper 26 receipt: quadratic record-action audit. | 5 check() calls | v7-paper26 | no |  |
| p27_cluster_expansion_bound_audit.py | Paper 27 receipt: cluster-expansion bound audit. | 9 check() calls | v7-paper27 | no |  |
| p27_coherent_shell_cancellation.py | Paper 27 receipt: coherent-wave cancellation against shell-local responses. | 5 check() calls | v7-paper27 | no |  |
| p27_continuous_copula_envelope.py | Paper 27 receipt: continuous copula envelope for A_N(c). | 5 check() calls | v7-paper27 | no |  |
| p27_density_matched_rank_kernel_projection.py | Paper 27 receipt: density-matched one-pair rank kernel and unlabeled projection. | 7 check() calls | v7-paper27 | no |  |
| p27_fourier_wave_boundary.py | Paper 27 receipt: Fourier/coherent-wave boundary. | 7 check() calls | v7-paper27 | no |  |
| p27_higher_cycle_residue_scaling.py | Paper 27 receipt: higher-cycle residue scaling. | 5 check() calls | v7-paper27 | no |  |
| p27_integrated_click_law_matrix.py | Paper 27 receipt: integrated candidate click-law matrix. | 8 check() calls | v7-paper27 | no |  |
| p27_intrinsic_local_response_gate.py | Paper 27 receipt: order-intrinsic local response gate. | 6 check() calls | v7-paper27 | no |  |
| p27_lemma_m_one_pair_projection.py | Paper 27 receipt: finite one-pair projection attack on Lemma M. | 5 check() calls | v7-paper27 | no |  |
| p27_linear_window_polymer_budget.py | Paper 27 receipt: linear-window polymer budget. | 6 check() calls | v7-paper27 | no |  |
| p27_linear_window_theorem_fork.py | Paper 27 receipt: linear-window theorem fork. | 7 check() calls | v7-paper27 | no |  |
| p27_local_mark_coupling_gate.py | Paper 27 receipt: local mark-coupling gate. | 6 check() calls | v7-paper27 | no |  |
| p27_mark_anti_laundering.py | Paper 27 receipt: anti-laundering tests for the marked sector. | 8 check() calls | v7-paper27 | no |  |
| p27_matching_free_energy_separator.py | Paper 27 receipt: matching/free-energy separator. | 9 check() calls | v7-paper27 | no |  |
| p27_n12_adaptive_invariant_screen.py | Paper 27 receipt: adaptive N=12 invariant screen for selected denominators. | 9 check() calls | v7-paper27 | no |  |
| p27_nonshared_cycle_neutrality.py | Paper 27 receipt: nonshared-cycle neutrality for density-matched pair factors. | 6 check() calls | v7-paper27 | no |  |
| p27_physical_pressure_asymptotic_adversary.py | Paper 27 receipt: physical matching-pressure scaling and tuned adversaries. | 9 check() calls | v7-paper27 | no |  |
| p27_projective_mark_field_law.py | Paper 27 receipt: projective mark-field admissibility. | 7 check() calls | v7-paper27 | no |  |
| p27_quotient_washout_proof_skeleton.py | Paper 27 receipt: quotient-level washout proof attempt and fallback ledger. | 8 check() calls | v7-paper27 | no |  |
| p27_rank_copula_bound_scaling.py | Paper 27 receipt: rank-copula bound scaling for density-matched Lemma M. | 7 check() calls | v7-paper27 | no |  |
| p27_sectoral_pressure_marks.py | Paper 27 receipt: sectoral pressure law with explicit matter marks. | 8 check() calls | v7-paper27 | no |  |
| p27_shell_projection_bound.py | Paper 27 receipt: shell-local projection bound. | 5 check() calls | v7-paper27 | no |  |
| p27_sqrt_global_witness_attack.py | Paper 27 receipt: square-root/global witness attack. | 4 check() calls | v7-paper27 | no |  |
| p27_unlabeled_second_moment_contiguity.py | Paper 27 receipt: unlabeled second-moment/contiguity campaign. | 6 check() calls | v7-paper27 | no |  |
| p28_2core_activity_bound_audit.py | Paper 28 receipt: 2-core activity bound audit. | 7 check() calls | v7-paper28 | no |  |
| p28_boundary_replacement_identity.py | Paper 28 receipt: boundary replacement cancellation identity. | 3 check() calls | v7-paper28 | no |  |
| p28_canonical_kernel_contraction_lemma.py | Paper 28 receipt: canonical-kernel contraction lemma. | 9 check() calls | v7-paper28 | no |  |
| p28_coefficient_summability_sieve.py | Paper 28 receipt: coefficient-level polymer summability sieve. | 8 check() calls | v7-paper28 | no |  |
| p28_cumulant_spectral_cancellation.py | Paper 28 receipt: cumulant/spectral attack on the stable-cancellation lemma. | 13 check() calls | v7-paper28 | no |  |
| p28_formal_sufficiency_theorem.py | Paper 28 receipt: finite record-sufficiency theorem. | 8 check() calls | v7-paper28 | no |  |
| p28_hybrid_theorem_falsification.py | Paper 28 receipt: prove/falsify the hybrid cancellation theorem route. | 6 check() calls | v7-paper28 | no |  |
| p28_interval_bridge_campaign.py | Paper 28 receipt: interval-to-subset bridge campaign. | 8 check() calls | v7-paper28 | no |  |
| p28_interval_residue_scaling_no_go.py | Paper 28 receipt: proper-interval residue scaling no-go. | 5 check() calls | v7-paper28 | no |  |
| p28_linear_window_second_moment_attack.py | Paper 28 receipt: direct bounded-width linear-window second-moment attack. | 13 check() calls | v7-paper28 | no |  |
| p28_missed_residue_equivalence_no_go.py | Paper 28 receipt: missed-residue equivalence no-go. | 3 check() calls | v7-paper28 | no |  |
| p28_mobius_falling_factor_expansion.py | Paper 28 receipt: exact Möbius/falling-factor 2-core expansion. | 6 check() calls | v7-paper28 | no |  |
| p28_physical_missed_residue_campaign.py | Paper 28 receipt: physical missed-residue cancellation campaign. | 5 check() calls | v7-paper28 | no |  |
| p28_physical_missed_residue_parameter_audit.py | Paper 28 receipt: physical missed-residue parameter audit. | 3 check() calls | v7-paper28 | no |  |
| p28_physical_width_boundary_scan.py | Paper 28 receipt: physical width-boundary scan. | 3 check() calls | v7-paper28 | no |  |
| p28_pressure_density_boundary_audit.py | Paper 28 receipt: pressure-density theorem boundary. | 9 check() calls | v7-paper28 | no |  |
| p28_pressure_to_washout_gap.py | Paper 28 receipt: pressure-density versus washout gap. | 4 check() calls | v7-paper28 | no |  |
| p28_principle_selection_matrix.py | Paper 28 receipt: hostile principle-selection matrix. | 5 check() calls | v7-paper28 | no |  |
| p28_rare_class_divergence_screen.py | Paper 28 receipt: rare-class divergence screen. | 6 check() calls | v7-paper28 | no |  |
| p28_record_sufficiency_principle.py | Paper 28 receipt: record sufficiency principle audit. | 8 check() calls | v7-paper28 | no |  |
| p28_recursive_heredity_campaign.py | Paper 28 receipt: recursive interval heredity campaign. | 6 check() calls | v7-paper28 | no |  |
| p28_sector_promotion_receipt.py | Paper 28 receipt: sector promotion from likelihood residue. | 8 check() calls | v7-paper28 | no |  |
| p28_signed_coefficient_envelope_final_campaign.py | Paper 28 receipt: signed coefficient-root envelope final campaign. | 6 check() calls | v7-paper28 | no |  |
| p28_smooth_local_theorem_campaign.py | Paper 28 receipt: smooth/local theorem campaign. | 8 check() calls | v7-paper28 | no |  |
| p28_subset_heredity_certificate.py | Paper 28 receipt: exact subset-heredity certificate theorem. | 3 check() calls | v7-paper28 | no |  |
| p29_admissibility_candidate_norms.py | Paper 29 receipt: admissibility candidate norms. | 5 check() calls | v7-paper29 | no |  |
| p29_admissibility_norm_audit.py | Paper 29 receipt: admissibility norm audit. | 6 check() calls | v7-paper29 | no |  |
| p29_adversarial_score_family_audit.py | Paper 29 receipt: adversarial score-family audit. | 6 check() calls | v7-paper29 | no |  |
| p29_boundary_cover_transfer.py | Paper 29 receipt: boundary-histogram cover transfer. | 5 check() calls | v7-paper29 | no |  |
| p29_boundary_histogram_minimal_cover.py | Paper 29 receipt: boundary-histogram minimal cover. | 4 check() calls | v7-paper29 | no |  |
| p29_controlled_projection_martingale.py | Paper 29 receipt: controlled projection martingale law. | 5 check() calls | v7-paper29 | no |  |
| p29_cover_transfer_matrix.py | Paper 29 receipt: cover transfer matrix. | 5 check() calls | v7-paper29 | no |  |
| p29_cycle_determinant_surrogate.py | Paper 29 receipt: cycle determinant surrogate. | 4 check() calls | v7-paper29 | no |  |
| p29_deck_ambiguity_certificate.py | Paper 29 receipt: deck-ambiguity certificate. | 4 check() calls | v7-paper29 | no |  |
| p29_deep_defect_peak_boundary.py | Paper 29 receipt: deep near-top defect peak boundary. | 4 check() calls | v7-paper29 | no |  |
| p29_defect_saddle_motion_audit.py | Paper 29 receipt: defect saddle motion audit. | 4 check() calls | v7-paper29 | no |  |
| p29_deletion_flow_conflict_cover.py | Paper 29 receipt: deletion flow of local conflict covers. | 5 check() calls | v7-paper29 | no |  |
| p29_effective_action_projection_identity.py | Paper 29 receipt: effective action projection identity. | 5 check() calls | v7-paper29 | no |  |
| p29_exact_2core_sector_decomposition.py | Paper 29 receipt: exact 2-core sector decomposition. | 4 check() calls | v7-paper29 | no |  |
| p29_external_math_campaigns.py | Paper 29 receipt: external mathematics compatibility campaigns. | 10 check() calls | v7-paper29 | no |  |
| p29_flag_compression_no_go.py | Paper 29 receipt: flag compression no-go. | 4 check() calls | v7-paper29 | no |  |
| p29_flag_deck_reconstruction_audit.py | Paper 29 receipt: flag-deck reconstruction audit. | 5 check() calls | v7-paper29 | no |  |
| p29_flag_deletion_projectivity.py | Paper 29 receipt: flag deletion projectivity. | 4 check() calls | v7-paper29 | no |  |
| p29_flag_interaction_expansion_audit.py | Paper 29 receipt: flag interaction expansion audit. | 5 check() calls | v7-paper29 | no |  |
| p29_flag_operator_family_audit.py | Paper 29 receipt: flag operator-family audit. | 5 check() calls | v7-paper29 | no |  |
| p29_greedy_flag_operator_selection.py | Paper 29 receipt: greedy flag-operator selection. | 4 check() calls | v7-paper29 | no |  |
| p29_greedy_operator_robustness.py | Paper 29 receipt: greedy operator robustness audit. | 3 check() calls | v7-paper29 | no |  |
| p29_hidden_lift_realizability.py | Paper 29 receipt: hidden lift realizability. | 5 check() calls | v7-paper29 | no |  |
| p29_labelled_cycle_index_correction.py | Paper 29 receipt: labelled cycle-index correction. | 4 check() calls | v7-paper29 | no |  |
| p29_lower_order_dominance_audit.py | Paper 29 receipt: lower-order dominance audit. | 4 check() calls | v7-paper29 | no |  |
| p29_matching_generating_identity.py | Paper 29 receipt: exact physical matching generating identity. | 4 check() calls | v7-paper29 | no |  |
| p29_matching_lib.py | Shared mpmath matching/permanent helper functions for the p29 receipt family | none found | — | YES | NOT a receipt: shared helper lib imported by 16 p29_* receipts; orphan-by-citation only |
| p29_matching_root_radius_audit.py | Paper 29 receipt: scaled matching-root radius audit. | 3 check() calls | v7-paper29 | no |  |
| p29_minimal_cover_ladder.py | Paper 29 receipt: minimal conflict-cover ladder. | 5 check() calls | v7-paper29 | no |  |
| p29_multivariate_score_polynomial.py | Paper 29 receipt: multivariate projected score polynomial. | 5 check() calls | v7-paper29 | no |  |
| p29_n8_polynomial_minimal_cover.py | Paper 29 receipt: N=8 polynomial minimal cover. | 5 check() calls | v7-paper29 | no |  |
| p29_n8_transfer_and_nullspace.py | Paper 29 receipt: N=8 transfer and nullspace growth. | 5 check() calls | v7-paper29 | no |  |
| p29_n9_active_flag_scan.py | Paper 29 receipt: N=9 active-flag scan. | 5 check() calls | v7-paper29 | no |  |
| p29_n9_active_minimal_cover.py | Paper 29 receipt: N=9 active-mask minimal cover. | 5 check() calls | v7-paper29 | no |  |
| p29_n9_feasibility_probe.py | Paper 29 receipt: N=9 feasibility probe. | 5 check() calls | v7-paper29 | no |  |
| p29_near_top_defect_profile.py | Paper 29 receipt: near-top defect profile. | 4 check() calls | v7-paper29 | no |  |
| p29_omitted_local_flag_spike_scan.py | Paper 29 receipt: omitted local flag spike scan. | 5 check() calls | v7-paper29 | no |  |
| p29_palm_flag_sufficiency_audit.py | Paper 29 receipt: causal Palm-flag sufficiency audit. | 5 check() calls | v7-paper29 | no |  |
| p29_profile_envelope_implication.py | Paper 29 receipt: factorial-normalized profile envelope implication. | 5 check() calls | v7-paper29 | no |  |
| p29_projected_likelihood_basis_audit.py | Paper 29 receipt: projected likelihood basis audit. | 4 check() calls | v7-paper29 | no |  |
| p29_projection_sufficiency_invariant.py | Paper 29 receipt: projection-sufficiency invariant. | 8 check() calls | v7-paper29 | no |  |
| p29_projection_ward_tower.py | Paper 29 receipt: projection Ward tower. | 5 check() calls | v7-paper29 | no |  |
| p29_rare_spike_amplification.py | Paper 29 receipt: rare-spike amplification. | 4 check() calls | v7-paper29 | no |  |
| p29_rook_hit_expansion_certificate.py | Paper 29 receipt: rook/hit expansion certificate. | 4 check() calls | v7-paper29 | no |  |
| p29_rooted_deletion_score_recurrence.py | Paper 29 receipt: rooted deletion score recurrence. | 8 check() calls | v7-paper29 | no |  |
| p29_score_polynomial_sufficiency.py | Paper 29 receipt: score-polynomial sufficiency theorem. | 5 check() calls | v7-paper29 | no |  |
| p29_sector_cancellation_stability.py | Paper 29 receipt: sector-cancellation stability. | 4 check() calls | v7-paper29 | no |  |
| p29_sector_shape_amplitude_no_go.py | Paper 29 receipt: sector shape without amplitude is not enough. | 4 check() calls | v7-paper29 | no |  |
| p29_sector_signature_audit.py | Paper 29 receipt: sector-signature audit. | 3 check() calls | v7-paper29 | no |  |
| p29_targeted_atom_amplification.py | Paper 29 receipt: targeted rare-atom amplification. | 4 check() calls | v7-paper29 | no |  |
| p29_top_order_beta_boundary.py | Paper 29 receipt: physical top-order beta boundary. | 4 check() calls | v7-paper29 | no |  |
| p29_top_order_lambda_boundary.py | Paper 29 receipt: physical top-order lambda boundary. | 4 check() calls | v7-paper29 | no |  |
| p29_unresolved_nullspace_audit.py | Paper 29 receipt: unresolved nullspace audit. | 5 check() calls | v7-paper29 | no |  |
| p29_washout_sector_promotion_bound.py | Paper 29 receipt: washout versus sector-promotion bound. | 5 check() calls | v7-paper29 | no |  |
| p29_worst_unresolved_atom_attack.py | Paper 29 receipt: worst unresolved atom attack. | 5 check() calls | v7-paper29 | no |  |
| p29_zero_free_radius_no_go.py | Paper 29 receipt: zero-free radius alone is not enough. | 4 check() calls | v7-paper29 | no |  |
| p2a_content_supply.py | Long March v7, PAPER 2 receipt: the content supply. | print-report style (17 OK/PASS strings) | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper2, v7-paper20, v7-paper21 | no |  |
| p2b_event_law_saturation.py | Long March v7, PAPER 2, P2-R2 DECISIVE receipt. | print-report style (18 OK/PASS strings) | v6-pub-companion-A-entropic-clock, v7-LONG_MARCH_PLAN, v7-paper2, v7-paper3 | no |  |
| p2c_vector_ledger_roots.py | Long March v7, PAPER 2, vector-ledger commitment roots. | 1 asserts | v6-pub-companion-A-entropic-clock, v7-paper2, v7-paper3 | no |  |
| p30_admissibility_selection_rule_campaign.py | Paper 30 receipt: admissibility selection rule campaign. | 6 check() calls | v7-paper30 | no |  |
| p30_backward_forward_hole_campaign.py | Paper 30 receipt: backward-then-forward multi-hole campaign. | 12 check() calls | v7-paper30 | no |  |
| p30_boundary_filtration_campaign.py | Paper 30 receipt: record-intrinsic boundary filtration campaign. | 7 check() calls | v7-paper30 | no |  |
| p30_complex_amplitude_campaign.py | Paper 30 receipt: complex amplitude campaign. | 11 check() calls | v7-paper30 | no |  |
| p30_diamond_boundary_center_campaign.py | Paper 30 receipt: diamond-boundary center campaign. | 11 check() calls | v7-paper30 | no |  |
| p30_effective_weight_six_campaigns.py | Paper 30 receipt: six effective-weight campaigns. | 12 check() calls | v7-paper30 | no |  |
| p30_flag912_obstruction_campaign.py | Paper 30 receipt: decode and audit the flag5_912 obstruction. | 5 check() calls | v7-paper30 | no |  |
| p30_forward_extension_law_campaign.py | Paper 30 receipt: forward extension law campaign. | 6 check() calls | v7-paper30 | no |  |
| p30_harmonic_quotient_campaign.py | Paper 30 receipt: harmonic quotient campaign. | 15 check() calls | v7-paper30 | no |  |
| p30_hinge_mechanism_campaign.py | Paper 30 receipt: why the lopsided hinge works. | 12 check() calls | v7-paper30 | no |  |
| p30_hinge_n9_prediction_campaign.py | Paper 30 receipt: next-scale hinge-sector prediction campaign. | 7 check() calls | v7-paper30 | no |  |
| p30_n9_sector_generator_campaign.py | Paper 30 receipt: N=9 sector-generator mechanism campaign. | 6 check() calls | v7-paper30 | no |  |
| p30_quadratic_norm_uniqueness_campaign.py | Paper 30 receipt: quadratic-norm uniqueness campaign. | 11 check() calls | v7-paper30 | no |  |
| p30_reflection_positive_campaign.py | Paper 30 receipt: six reflection-positive positive-shadow campaigns. | 13 check() calls | v7-paper30 | no |  |
| p30_rooted_boundary_flag_cover.py | Paper 30 receipt: rooted boundary flag cover. | 4 check() calls | v7-paper30 | no |  |
| p30_rooted_boundary_transfer.py | Paper 30 receipt: rooted boundary cover transfer. | 5 check() calls | v7-paper30 | no |  |
| p30_rooted_unrooted_equivalence.py | Paper 30 receipt: rooted/unrooted cover equivalence. | 3 check() calls | v7-paper30 | no |  |
| p31_diamond_shadow_closure_receipt.py | Paper 31 receipt: diamond-shadow closure theorem ledger. | 11/11 declared; 7 check() calls | v7-paper31 | no |  |
| p32_v6_v7_diamond_law_bridge.py | Paper 32 receipt: v6-v7 diamond law bridge audit. | 11 check() calls | v7-paper32 | no |  |
| p33_intrinsic_center_shadow_hweight_campaign.py | Paper 33 receipt: intrinsic C_N -> P_N -> h_P_N campaign. | 10 check() calls | v7-paper33 | no |  |
| p34_boundary_work_potential_campaign.py | Paper 34 receipt: boundary-work potential campaign. | 9 check() calls | v7-paper34 | no |  |
| p35_shadow_coalgebra_variational_recurrence.py | Paper 35 receipt: shadow-coalgebra variational recurrence campaign. | 9 check() calls | v7-paper35 | no |  |
| p36_indivisible_history_prediction_campaign.py | Paper 36 receipt: indivisible W-history prediction campaign. | 14 check() calls | v7-paper36 | no |  |
| p36_n9_history_bound_campaign.py | Paper 36 receipt: exact N=9 history-bound follow-up. | 7 check() calls | v7-paper36 | no |  |
| p37_joint_history_spacetime_boundary_work.py | Paper 37 finite receipt. | print-report style (1 OK/PASS strings) | v7-paper37 | no |  |
| p37_spacetime_onset_campaign.py | Paper 37 long campaign: first finite spacetime-onset audit. | 11 check() calls | v7-paper37 | no |  |
| p3_d_nogo.py | v7 Paper 3 — the seal-spacing no-go (d-no-go) receipt. | 1 asserts | v6-pub-companion-G-scale-grading, v7-LONG_MARCH_PLAN, v7-paper20, v7-paper21, v7-paper3 | no |  |
| p4a_joint_clicklaw.py | Long March v7, PAPER 1, Tier A, section 5.2 OPEN. | 24 asserts | v7-LONG_MARCH_PLAN, v7-paper22, v7-paper4 | no |  |
| p4b_connectivity_metric_split.py | v7 Paper 4 — the connectivity/metric weight-split receipt (entanglement -> spacetime). | 1 asserts | v7-LONG_MARCH_PLAN, v7-paper4 | no |  |
| p5_cm_calibration.py | v7 Paper 5 — the c_m free-calibration receipt (the gravitational per-species coupling). | 1 asserts | v6-pub-companion-G-scale-grading, v7-LONG_MARCH_PLAN, v7-paper5 | no |  |
| p6_transverse_nogo.py | THE MAIN TRANSVERSE NO-GO RECEIPT. v7 Long March, Paper 6. | 42 check() calls; 1 asserts | v7-paper12, v7-paper16, v7-paper17, v7-paper20, v7-paper21 | no | Part 5b I3322 swapped to CG-projector form 2026-06-16; 42/42 after fix |
| p6b_holonomy_phase_audit.py | OPEN-PATH 1, THE CRUX. | 21 check() calls; 1 asserts | v7-paper12, v7-paper16 | no |  |
| p6c_alternative_capacity.py | v7 Long March, OPEN-PATH 2. | 5 asserts | v7-paper12 | no |  |
| p6d_sign_magnitude.py | RECEIPT p6d: SIGN/MAGNITUDE RESIDUE on chi_AB -- can the transverse | 20 check() calls; 1 asserts | v7-paper12 | no |  |
| p9a_chiral_gap_closed.py | v7 Paper IX, receipt A -- the CLOSED chiral-gap law (closes Paper VIII's O2 conjecture). | 1 asserts | v6-pub-companion-F-chiral-matter, v7-LONG_MARCH_PLAN, v7-paper18, v7-paper9 | no |  |
| p9b_psg_ingredient_functor.py | v7 Paper IX, receipt B -- the record orientation-class group (the PSG-INGREDIENT functor), | 1 asserts | v6-pub-companion-F-chiral-matter, v7-LONG_MARCH_PLAN, v7-paper9 | no |  |
| p9c_chirality_bridge_nogo.py | v7 Paper IX, receipt C -- the second no-go: NO record-forced chirality bridge. | 1 asserts | v6-pub-companion-F-chiral-matter, v7-LONG_MARCH_PLAN, v7-paper9 | no |  |
| pB_donoho_stark.py | v7 Paper IX, receipt pB (TOOL 1) -- DONOHO-STARK uncertainty + K.T. SMITH equality case, | 1 asserts | v7-paper18 | no |  |
| pB_entropic.py | v7 Paper IX / [L*] residue -- TOOL 2: ENTROPIC UNCERTAINTY adapted to the flat ... | 1 asserts | v7-paper18 | no |  |
| pB_hypercontractive.py | TOOL 3 -- HYPERCONTRACTIVITY / Fourier analysis on the hypercube applied to the open chiral-gap | 3 asserts | v7-paper18 | no |  |
| pB_variational.py | v7 Paper IX, receipt pB -- TOOL 4: a DIRECT VARIATIONAL / Gibbs lower bound ... | 2 asserts | v7-paper18 | no |  |
| pD2_achievability.py | v7 Paper XVIII, receipt pD2 -- ACHIEVABILITY of the chiral-gap T-multisets. | 5 asserts | v7-paper18 | no |  |
| pD2_counterexample_hunt.py | pD2 -- COUNTEREXAMPLE HUNT for the SHARD chiral-gap GLOBAL-OPTIMALITY residue (v7 Paper XVIII). | 1 asserts | v7-paper18 | no |  |
| pD2_minimization_proof.py | v7 Paper XVIII -- the chiral-gap GLOBAL-OPTIMALITY residue, PROOF ATTACK on the 1-D minimization. | 5 asserts | v7-paper18 | no |  |
| pD_chiral_global_optimality.py | v7 Paper IX, receipt D -- the chiral-gap GLOBAL-OPTIMALITY lemma. | 2 asserts | v7-paper18 | no |  |
| pE_phase_causalset.py | v7 Paper E (probe) | 10 check() calls | — | YES | KNOWN orphan confirmed; probe: complex-phase vs real-weight causal-set selection |
| pFDT_seal_influence.py | v7 THREAD FEYNMAN -- ADVERSARIAL-REVIEW VERDICT (2026-06-17): THE FDT FRAMING IS A METAPHOR, NOT A | 21/21 declared; 21 check() calls; 2 asserts | — | YES | KNOWN orphan confirmed; docstring self-marks FDT framing 'METAPHOR, NOT A THEOREM' (math 21/21 sound) |
| pK1_seal_information_rate.py | v7 -- THE kappa = 1 CRUX: does the seal commit at exactly the information ... | 8 check() calls; 1 asserts | — | YES | KNOWN orphan confirmed; kappa=1 saturation crux; superseded by Thread RAMANUJAN |
| pPRIN_seal_record.py | v7 -- THE SEAL-IS-RECORD PRINCIPLE: internal-consistency receipt. | 21 check() calls; 1 asserts | — | YES | KNOWN orphan confirmed; Thread EINSTEIN seal-is-record principle receipt |
| pRUN_kappa_exact.py | v7 THREAD RAMANUJAN -- THE EXACT RUNNING OF THE SEAL/DECOHERENCE PROPORTIONALITY CONSTANT kappa(s). | 2/2 declared; 17 check() calls; 1 asserts | — | YES | KNOWN orphan confirmed; 17/17 PASS per memory; Thread RAMANUJAN result not yet folded into any paper |
| r1_order_to_conformal_direction.py | v7 ROUTE-1 receipt -- the causal ORDER -> the CONFORMAL metric (null cones / DIRECTIONS). | 1 asserts | v6-pub-companion-D-conformal-direction, v7-LONG_MARCH_PLAN, v7-paper11 | no |  |
| r2_number_volume_lstep.py | v7 ROUTE 2 (causal-set "Order + Number = Geometry") -- the NUMBER -> VOLUME half, | 1 asserts | v6-pub-companion-D-conformal-direction, v7-LONG_MARCH_PLAN, v7-paper11 | no |  |
| r3_manifoldlikeness_myrheim_meyer.py | ROUTE 3 -- the MANIFOLDLIKENESS obstruction, made operational via the Myrheim-Meyer dimension. | 1 asserts | v6-pub-companion-D-conformal-direction, v7-LONG_MARCH_PLAN, v7-paper11 | no |  |
| s_chiral_bridge_parity_probe.py | SCOUT PROBE (PRELIMINARY) -- area S-CHIRAL-BRIDGE. | 1 asserts | — | YES | Scout, self-marked PRELIMINARY (paper IX chirality-bridge parity) |
| s_chiral_gap_ratios.py | v7 matter-sector paper, PART (III) "SHARPENING" production receipt. | 1 asserts | v7-paper14 | no |  |
| s_geom_chi_sweep.py | v7 R2 receipt -- the TWO genuinely-new geometric constraints on the free input chi_AB, | 20 check() calls; 1 asserts | v7-paper13, v7-paper16 | no |  |
| s_igw_gross_neveu_probe.py | S-IGW PRELIMINARY PROBE (scout, NOT a finished receipt). | none found | — | YES | Scout, self-marked 'NOT a finished receipt'; precursor of paper14 [CONSTRUCTIVE] leg |
| s_igw_production_gap_flow.py | PRODUCTION receipt (Task A, the CONSTRUCTIVE win). | 1 asserts | v7-paper14 | no |  |
| s_igw_robustness_probe.py | S-IGW robustness probe (scout). Two checks on the dynamical-mass mechanism: | none found | — | YES | Scout (Banks-Casher/zero-mode robustness); precursor of paper14 R1 correction |
| s_matter_chi_probe.py | PRELIMINARY SCOUT PROBE -- S-MATTER sector. | 1 asserts | — | YES | Scout, self-marked PRELIMINARY (matter-mode vs chi_AB link) |
| s_mode_import_wall.py | TASK B (PRODUCTION). The canonical-mode no-go (the third/matter import-fixed wall). | 1 asserts | v7-paper14, v7-paper17 | no |  |
| s_modeh_mode_selecting_hamiltonian.py | SCOUT S-MODEH (PRELIMINARY). -- THE FIFTH-WALL ESCAPE under test (Paper VIII s4, s8(c); m2 caveat). ... | 1 asserts | — | YES | Scout S-MODEH (fifth-wall escape test); feeds paper14 mode-wall leg |
| s_order_feedback_probe.py | R4 -- ORDER-FEEDBACK PROBE (the HIGHEST-risk open path of the v7 downstream no-go). | 18 check() calls; 1 asserts | v7-paper13 | no |  |
| s_probe_qtilde_minus_q.py | R1, THE HEADLINE / SPINE RECEIPT. v7 Long March. | 26 check() calls; 1 asserts | v7-paper13, v7-paper16 | no |  |
| s_ratio_probe.py | PRELIMINARY SCOUT PROBE -- S-RATIO sector (the headline morsel). | 1 asserts | — | YES | Scout S-RATIO (mass-ratio gating); feeds paper14 [SHARPEN] leg |
| scout_everpresent_numerology.py | SCOUT S-NUMEROLOGY: Sorkin everpresent-Lambda numerology vs SHARD record substrate. | none found | — | YES | Scout preceding paper15 numerology section; superseded by p15-series |
| setup_extract_d1d.py | SETUP extraction for the SHARD chiral-gap global-optimality residue (v7 Paper XVIII). | 3 checks declared; 14 asserts | — | YES | Setup/extraction helper for paper18 residue (reuses pD functionals); not independently cited |
| t1_npa_q_vs_qtilde.py | ATTACK MOVE T1. -- Does SHARD's TRANSVERSE SELF-CONSISTENCY cut the joint click-law correlation set to | 8 check() calls; 1 asserts | v6-pub-companion-B-almost-quantum, v7-LONG_MARCH_PLAN, v7-paper6 | no |  |
| t2_purification_uniqueness.py | MOVE T2 -- Does SHARD's record structure admit a CDP-PURIFICATION uniqueness | 2 asserts | v6-pub-companion-B-almost-quantum, v7-LONG_MARCH_PLAN, v7-paper6 | no |  |
| t3_tsirelson_derivation.py | MOVE T3 -- CAN SHARD *DERIVE* THE TSIRELSON BOUND (CHSH <= 2 sqrt 2) FROM ... | 16 check() calls; 1 asserts | v7-LONG_MARCH_PLAN, v7-paper12, v7-paper6 | no |  |
| v7_m1_psg_gap_chiral_receipt.py | MOVE M1 receipt: import PSG / Levin-Wen string-net framing, recast SHARD's | none found | v6-pub-companion-F-chiral-matter, v7-LONG_MARCH_PLAN, v7-paper8 | no |  |
| v6/code/s_conj_everpresent_sorkin.py | S-CONJ scout receipt: does SHARD's unimodular Lambda-V conjugacy + the Poisson | 11 check() calls | — | YES | ONLY v6/code file; scout for the paper15 (XV) Sorkin conjugacy route; superseded by p15a |

## ORPHAN SUMMARY

**23 orphans out of 274 .py files** (no .md in v7/, v6/, v6/publishable/ cites them, checked with and without `.py`).

- Of the 6 KNOWN orphan candidates: 5 confirmed (pE_phase_causalset.py, pFDT_seal_influence.py, pK1_seal_information_rate.py, pPRIN_seal_record.py, pRUN_kappa_exact.py); p19c_swerve_fdr.py NO LONGER an orphan (paper19.md updated 2026-07-01 mid-scan, cites it 19/19)
- NEW orphans found (18): _r2_independent_hunt.py, _r2_math_checks.py, _r2_n6_n7.py, _r2_nearalt.py, _r2_specifics.py, _r2_structured.py, m3_cm_hierarchy_mechanism.py, move_C3_TS_factorization.py, p29_matching_lib.py, s_chiral_bridge_parity_probe.py, s_igw_gross_neveu_probe.py, s_igw_robustness_probe.py, s_matter_chi_probe.py, s_modeh_mode_selecting_hamiltonian.py, s_ratio_probe.py, scout_everpresent_numerology.py, setup_extract_d1d.py, v6/s_conj_everpresent_sorkin.py

New-orphan breakdown: 6 `_r2_*` paper18-R2 adversarial scratch files; 8 `s_*`/`scout_*` self-marked preliminary scouts (paper14/paper15/paperIX/paperVIII areas; 1 of them the sole v6/code file); 2 aborted/unfolded move probes (move_C3_TS_factorization, m3_cm_hierarchy_mechanism); 1 shared lib (p29_matching_lib, imported by 16 p29 receipts); 1 setup helper (setup_extract_d1d). Also note the p18_seal_divisibility.py docstring mislabel ('Paper XVIII' -> actually Move-C probe folded into paper16; NOT an orphan, cited by v7-paper16).
