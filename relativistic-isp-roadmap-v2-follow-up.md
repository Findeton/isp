# Relativistic ISP Roadmap V2: Follow-Up After the Finite Benchmark Stack

Author: Felix Robles Elvira

Date: 2026-05-14

Purpose: state the next non-gravitational steps needed to make relativistic ISP a more viable physics theory after the 17-paper finite benchmark arc. This document does not replace the original roadmap. It starts from its honest conclusion: the current stack is a theorem-level finite benchmark program, not yet a full continuum relativistic ISP.

## Executive Status

After the current sequence, relativistic ISP has exact dynamics in controlled finite settings, but it does not yet have a full relativistic dynamics in the strong physics sense.

What exists:

- finite hypersurface-kernel architecture;
- localized finite deformations and comparison maps;
- exchange defects with exact free-model support and coefficient control;
- leading and first non-leading regulator/stability evidence;
- finite Fock-sector dynamics;
- static and dynamical Abelian gauge benchmarks;
- localized controls, detectors, no-signaling, and finite operational composition;
- induced finite local-net causality results under explicit hypotheses;
- boundary-flux-resolved locality on physical Gauss sectors;
- finite interacting `Z_2` and truncated compact `U(1)` gauge-matter benchmarks;
- a free one-particle V2 stochastic-curvature theorem at the scoped leading/log-smeared level;
- a V2 projective hypersurface-kernel framework draft for exact and asymptotic refinement compatibility.

What does not yet exist:

- a full Lorentz-covariant continuum construction over arbitrary hypersurfaces;
- a general interacting/gauge regulator-stable continuum hypersurface-deformation theorem;
- a full interacting QFT reconstruction;
- a continuum Haag-Kastler net;
- a compact-rotor or `K -> infinity` gauge theorem;
- a non-Abelian gauge theory;
- a Bell local-causality theorem for arbitrary microscopic couplings;
- metric reconstruction, dynamical spacetime, or gravity.

The next phase must therefore be a viability phase. Its job is not to add more finite examples. Its job is to prove that the finite-kernel machinery survives the passage toward continuum relativistic dynamics.

## Central Viability Gate

The core question is:

> Can exact stochastic kernel dynamics reproduce foliation-independent relativistic evolution in a regulator-stable continuum limit?

In the current language, this becomes:

> Do normalized exchange defects converge to the hypersurface-deformation / Dirac-Schwinger tangential action under a controlled refinement limit?

If yes, relativistic ISP becomes a serious candidate framework for probability-first relativistic quantum dynamics. If no, it remains a valuable finite representation and benchmark program, but not yet a viable relativistic physics theory.

## Roadmap V2 Principles

1. **Do not broaden before proving continuity.** More finite benchmarks are useful only if they feed the continuum and covariance problem.
2. **Keep raw, operational, and observable levels separate.** Raw comparison maps are not automatically local observables.
3. **Treat covariance as a theorem, not a slogan.** Finite stochastic isomorphisms with stochastic inverses are only permutations, so nontrivial covariance needs refinement or continuum structure.
4. **Do not import Hilbert-space locality as primitive.** The point is to show which local and algebraic structures are earned by `Gamma`, `J_R`, `E_{R,S}`, and operational instruments.
5. **Make failure sharp.** Every phase should have a pass/fail criterion that can stop the program early if the stochastic data are insufficient.
6. **Keep gravity out until metric data are reconstructed.** Gravity is a later question. The next viability gates are non-gravitational.

## V2 Paper 1: The Free Stochastic-Curvature Theorem

Suggested title:

`The Free Stochastic-Curvature Theorem for Relativistic ISP`

Investigation file:

`free-stochastic-curvature-theorem-investigation.md`

Consolidated paper draft:

`relativistic-isp-v2-paper1-free-stochastic-curvature-theorem.md`

Coefficient-level proof file:

`coefficient-level-free-stochastic-curvature-theorem.md`

Finite-slab proof file:

`finite-slab-free-stochastic-curvature-theorem.md`

Main question:

> Does the free `1+1D` Dirac exchange-defect machinery converge to the tangential hypersurface-deformation generator with explicit regulator control?

Main job:

- consolidate the free one-particle exchange-defect papers into one theorem-level continuum test;
- define the admissible localized-deformation/regulator class;
- define the lattice-spacing and slab-size scaling regime;
- define the sampling maps from smooth compactly supported spinor profiles to lattice profiles;
- prove explicit error bounds for the normalized exchange defect;
- prove that the limiting operator is independent of the allowed regulator class after the stated normalization.

Target theorem:

```math
\lim_{a\to 0} Z_a\bigl(E_{N,M}(a,\Delta)-I\bigr)\iota_a\phi
= K_\parallel[N\partial_xM-M\partial_xN]\phi.
```

Pass condition:

- a real theorem with uniform estimates, not only coefficient matching;
- precise domains, normalization, and order of limits;
- stability across the admissible regulator class.

Fail condition:

- the limit depends on microscopic deformation rule, sampling convention, support discretization, or incompatible order of limits.

Why this comes first:

This is the point at which exchange defects either become stochastic curvature in a physics-relevant sense or remain finite-lattice algebraic data.

## V2 Paper 2: Projective Hypersurface Kernel Dynamics

Suggested title:

`Projective Hypersurface Kernels and Foliation Compatibility in Relativistic ISP`

Investigation file:

`projective-hypersurface-kernel-dynamics-investigation.md`

Consolidated paper draft:

`relativistic-isp-v2-paper2-projective-hypersurface-kernel-dynamics.md`

Main question:

> What replaces finite stochastic isomorphism when hypersurfaces, lattices, and regulators change?

Main job:

- define a directed family of regulated hypersurface configuration spaces `C_{Sigma,a}`;
- define refinement, coarse-graining, or embedding maps between configuration spaces;
- define projective states and cylinder effects;
- define slab kernels compatible with those maps exactly or asymptotically;
- prove naturality of primitive kernels, comparison maps, and exchange defects;
- prove the error-propagation theorem showing how primitive refinement errors are amplified by `Gamma_0^{-1}`, `J_R`, and `J_R^{-1}`;
- define when two hypersurface paths are equivalent at the stochastic level, with curvature-corrected equivalence treated as extra projective tangential data;
- formulate covariance as projective/refinement compatibility rather than finite-set permutation covariance;
- keep gauge-sector projective systems center-resolved where Gauss-law boundary centers are present.

Pass condition:

- a mathematically precise projective/asymptotic framework in which continuum covariance can be stated and in which Paper 3's inverse-control hypotheses are explicit.

Fail condition:

- no nontrivial covariance notion survives beyond fixed finite relabeling, or refinement errors are uncontrollably amplified by reference/comparison inverses.

Why this follows Paper 1:

Once the free curvature limit is known, the theory needs a place for that limit to live across different hypersurface regulators.

## V2 Paper 3: Interacting Comparison-Map Locality and Inverse Control

Suggested title:

`Quasilocality and Inverse Control for Interacting ISP Comparison Maps`

Investigation file:

`interacting-comparison-map-locality-inverse-control-investigation.md`

Consolidated paper draft:

`relativistic-isp-v2-paper3-interacting-comparison-map-locality.md`

Main question:

> Can interacting finite-range Hamiltonian locality control the stochastic comparison maps `J_R = Gamma_R Gamma_0^{-1}` and exchange defects `E_{R,S}`?

Main job:

- prove finite-size estimates for `Gamma_0^{-1}` in controlled interacting benchmark classes;
- identify conditions under which localized deformation maps remain quasilocal after inversion;
- choose a local/anchored topology rather than relying on global matrix norms that scale with volume;
- use the paired-word Born-squared polymer-activity/KP theorem to upgrade fixed-order LC-log to finite-slab anchored locality of the connected logarithmic defect `L_R=log J_R` in the bounded finite-range/common-collar class, then derive locality of `J_R-I`;
- prove or isolate the anchored finite-slab inverse theorem for `J_R` and `J_R^{-1}`;
- prove primitive refinement estimates in the projective framework of Paper 2;
- control the propagation of those refinement errors through `J_R`, `J_R^{-1}`, and `E_{R,S}`;
- test whether Lieb-Robinson-type operator bounds can be transferred to primitive kernels and comparison maps;
- prove or disprove an exchange-defect support/window bound for interacting lattice systems;
- separate raw comparison-map bounds from operational locality theorems.

Pass condition:

- a theorem transferring finite-range or gapped/local Hamiltonian assumptions into controlled `J_R` and `E_{R,S}` locality/refinement estimates.

Fail condition:

- inverses destroy locality generically, making raw comparison-map exchange defects too nonlocal to support continuum relativistic dynamics.

Why this matters:

The finite interacting `Z_2` and truncated `U(1)` papers show that exact interacting benchmark blocks exist. Viability requires estimates that scale beyond prototype matrices.

## V2 Paper 4: Operational Observable Reconstruction

Suggested title:

`Operational Observable Reconstruction from Relativistic ISP Kernels`

Investigation file:

`relativistic-isp-v2-paper4-operational-observable-reconstruction-investigation.md`

Consolidated paper draft:

`relativistic-isp-v2-paper4-operational-observable-reconstruction.md`

Main question:

> Which local operational algebras are selected by the stochastic dynamics rather than chosen by hand?

Measurement-problem question:

> Can ISP make definite detector records, selective update, and outcome
> probabilities primitive stochastic facts, so that no additional collapse law
> is needed, while still recovering quantum interference?

Main job:

- state the precise finite operational sense in which ISP addresses the
  measurement problem;
- formalize detector record sectors and conditioning-as-update;
- formalize the map from raw kernel data to operational instruments;
- characterize when operational instruments are realizable by finite localized dynamics;
- compare raw-induced effect algebras with operationally generated algebras;
- state conditions under which the two agree, differ, or cannot be compared;
- extend boundary-flux center methods from fixed preserving subclasses toward broader classes.

Pass condition:

- a theorem saying under what finite benchmark hypotheses localized detector
  instruments write definite stable records, selective update is conditioning
  rather than collapse, and the induced local net is not merely an abstract
  construction but the operationally relevant local net.

Fail condition:

- the raw stochastic dynamics underdetermines local observable structure so strongly that additional Hilbert/circuit data must be taken as primitive.
- detector records or interference phenomena cannot be recovered without
  adding measurement/phase structure as primitive.

Why this matters:

A physics theory needs observables and experiments, not only transition kernels and algebraic comparison maps.

## V2 Paper 5: Continuum Gauge Benchmark

Suggested title:

`Toward a Continuum Gauge Benchmark for Relativistic ISP`

Initial paper draft:

`relativistic-isp-v2-paper5-continuum-gauge-benchmark.md`

Current status as of 2026-05-14:

- the first theorem package is now fixed to an open-chain `1+1D` compact `U(1)`
  gauge-matter benchmark;
- the concrete finite Hamiltonian/lift is stated, with exact Gauss-sector and
  boundary-center preservation;
- the no-truncation theorem is specialized to reachable finite Hamiltonian
  hulls and local bond-gate strings;
- a finite-energy cutoff-tail estimate bounds local cutoff leakage;
- center-resolved locality is formalized through a local boundary-flux center
  and an explicit `epsilon_cent` oscillation bound;
- the first representative center-resolved exchange coefficient is computed on
  the minimal two-bond open-chain strip.
- a locally admissible cutoff scaling regime is now stated: under only a local
  finite-electric-energy bound, `a(K-r)^2 -> infinity`, so power laws require
  `K >> a^{-1/2}`;
- using Gauss-law bounded-slope plus tight local centers, the sufficient cutoff
  scaling improves to `a(K-r-B)^3 -> infinity`, so power laws `K >> a^{-1/3}`
  suffice for that class; bounded profile classes need only eventual cutoff
  dominance;
- the clipped local electric-energy statistic is the first concrete
  continuum-facing gauge statistic, and it now has a proved continuum limit on
  deterministic center-profile preparations and finite profile mixtures;
- a center-cutoff-Gauss detector record family is defined, with an explicit
  deterministic readout protocol and a classical confusion-channel residual;
- finite-depth inverse control is proved by a Neumann bound; unconditional
  full Hamiltonian slab inverse control is now ruled out across arbitrary
  refinements by an exact two-state hopping resonance obstruction;
- the first exchange coefficient is extended to a mixed-corridor onset,
  small-slab tail estimate, and renormalized contact-channel law;
- fixed-volume `K -> infinity` compact-rotor local stability is proved, and a
  growing-volume compact-rotor cutoff-transfer theorem is proved for local
  statistics assuming the rotor local thermodynamic limit exists; growing-volume
  compact-rotor inverse control remains open.
- Paper 5 now includes a claim audit, dependency graph, and Main Theorem M,
  making explicit which statements are proved finite facts, proved model-limit
  statements, conditional transfers, obstructions, or open inputs.
- Paper 5 now has a dedicated remaining-gaps section covering physical flux
  tails, replacement inverse control, fluctuating continuum preparations,
  contact-channel interpretation, concrete rotor thermodynamic limits, detector
  hardware, and periodic/non-Abelian extensions.

Main question:

> Can the finite gauge benchmarks survive cutoff and volume limits in at least one controlled continuum gauge theory?

Main job:

- choose a conservative target, such as a Schwinger-model-like `1+1D` compact `U(1)` benchmark;
- prove cutoff-uniform or `K`-stability estimates for truncated compact `U(1)` blocks;
- control the no-truncation condition under refinement;
- track boundary-flux centers through the limit;
- identify which reduced Coulomb-string structures survive;
- keep the compact-rotor obstruction explicit.

Pass condition:

- a controlled limit from finite truncated gauge blocks to a continuum or infinite-cutoff gauge benchmark.

Fail condition:

- inverse control, no-truncation stability, or boundary-center locality fails irreparably under cutoff/volume growth.

Why this matters:

Gauge theory is the first serious test of whether relativistic ISP can handle constrained local field theory rather than only free or finite reduced examples.

## V2 Paper 6: Relativistic QFT Reconstruction or No-Go

Suggested title:

`Relativistic QFT Reconstruction and No-Go Tests for ISP`

Initial investigation draft:

`relativistic-isp-v2-paper6-qft-reconstruction-no-go-investigation.md`

Main question:

> Are the stochastic-kernel axioms restrictive enough to select ordinary local QFT universality classes?

Main job:

- state a reconstruction theorem target from stochastic kernels to Hilbert/algebraic QFT representations;
- identify which data are `Gamma`-level and which require lift/circuit choices;
- look for counterexamples: identical stochastic exchange-curvature data with inequivalent local QFT physics;
- prove a narrow reconstruction theorem for a free or gauge benchmark, or prove a no-go theorem showing what extra data are unavoidable;
- explicitly separate representation existence from physical locality/covariance.

Pass condition:

- a nontrivial recovery theorem for a known relativistic QFT class, or a precise no-go theorem locating the missing data.

Fail condition:

- stochastic transition data are too underdetermined to recover local QFT without reintroducing Hilbert-space field structure as primitive.

Why this matters:

This is where relativistic ISP either becomes a reconstruction program for QFT or becomes a useful representation layer sitting beneath standard QFT rather than replacing it.

Current investigation status, 2026-05-16:

- The first clean result is now drafted as a no-go theorem against Markovized
  Gamma-only reconstruction: component-level stochastic shadows composed as if
  the process were divisible cannot reconstruct QFT, because they do not
  determine coherent phase-sensitive composition.
- The minimal example is a Mach-Zehnder/two-path obstruction. The component
  shadows `Gamma(H)` and `Gamma(D_phi)` are independent of the phase `phi`,
  while the coherent composition `H D_phi H` gives output probabilities
  `cos^2(phi/2)` and `sin^2(phi/2)`.
- This is a Barandes-style indivisibility warning, not a claim that ISP itself
  predicts the Markov product. A genuine ISP treatment may use a whole-process
  kernel or explicitly declared division events.
- Paper 6 now contains a Barandes alignment section: whole-process kernels are
  primary, division/record events are physical structure, and Hilbert lifts are
  representational rather than ontological.
- The Mach-Zehnder section now includes the whole-process correction
  `Gamma_whole^phi=Gamma(H D_phi H)`, showing that ISP can encode the correct
  phase-dependent circuit law when the coherent circuit is not falsely divided.
- This does not refute ISP. It shows that Paper 6 must distinguish stochastic
  kernels, detector records, coherent lift data, and local algebraic QFT data.
- A component-kernel-derived strengthening is also drafted: any `J_R`,
  `E_{R,S}`, or projective comparison object built only as a function of the
  same component shadows inherits the same phase blindness. Whole-process
  kernels are a different input.
- The local-net/factorization no-go is now formalized by a four-state example:
  the same deterministic kernel is a one-region reset in one factorization and
  non-product in another.
- A two-qubit version is also drafted: the same global unitary is a local
  one-qubit phase gate in one tensor factorization and an entangling `ZZ` phase
  gate in another.
- The locality obstruction is generalized by dimension count: product-local and
  one-region-local kernels are lower-dimensional families relative to a chosen
  factorization, so locality is a property of `(kernel + factorization)`.
- The positive route is conditional: enrich ISP with tomographically complete
  instruments, whole-process kernels or declared division events, projective
  locality, and sector/center resolution. The finite operational reconstruction
  theorem is now proved in finite epsilon-stable form with explicit
  span/separation assumptions.
- Paper 6 now adds an explicit epsilon-division criterion: partial-kernel
  composition is allowed only with an intermediate configuration space,
  whole-process comparison, record/boundary data, outcome floor when selective,
  reset/coarse-graining rule, and stability tolerance.
- The Barandes stochastic-quantum theorem is now treated as a finite
  representation-existence input, not as uniqueness or QFT reconstruction.
- Paper 5 is now repackaged as a regulated input package
  `D_gauge^{K,L}` with regions, boundary centers, operational state/effect
  spaces, detector instruments, kernels, exchange bounds, refinement maps, and
  residual budgets.
- The first positive reconstruction target is a finite center-resolved
  operational ISP-net theorem. It now has an epsilon-stable proof with explicit
  preparation/effect frame constants and residual propagation. It reconstructs
  regulated operational structure from whole-process/record data, not continuum
  QFT.
- The Paper 5 regulated gauge package is conditionally instantiated as a
  fixed-cutoff input to Theorem 8, with reconstruction error controlled by
  `\kappa_{K,L}\eta_{K,L}+\epsilon_{\mathrm{gauge}}^{K,L}`. The canonical
  microscopic center-resolved record frame has `\kappa=1`; coarse/noisy
  detector frames must pay their explicit response condition number.
- The coarse-detector analysis is now explicit: a detector response gives full
  reconstruction when it has a bounded lower separation constant, quotient
  reconstruction when it separates only coarse operational classes, and no
  stable reconstruction when its condition number diverges.
- The open-chain gauge reconstruction theorem is now assigned to Paper 6
  proper as the main positive fixed-cutoff example. Continuum compact-rotor QFT
  remains a promotion gate, not a Paper 6 output.
- The simplest free benchmark promotion gate is now explicit: Paper 1's
  one-particle stochastic-curvature datum must still be supplemented by
  sampling convergence, translation/hypersurface covariance, a spectrum
  condition, vacuum/sector selection, local algebra data, and continuum
  stability before it becomes a free QFT reconstruction claim.
- Papers 1-5 have been audited against Barandes-style indivisibility. Paper 2
  and Paper 4 were already clean; Paper 3 and Paper 5 now include explicit
  caveats clarifying that circuit/gate products are representation-level or
  declared-operation constructions, not silent Markov divisibility through
  unrecorded stochastic stages.
- Paper 6's scope is fixed: it should become a no-go plus finite operational
  reconstruction paper, not a continuum QFT reconstruction paper. Its next edit
  should convert the investigation notes into the publication spine now listed
  in the draft.
- Free-QFT promotion is deferred to a dedicated later paper: it must add
  sampling convergence, covariance, spectrum, vacuum/Fock sector, local algebra,
  and continuum stability rather than hiding those obligations inside Paper 6.
- Schur-Hadamard lift gauge is now separated from physical lattice gauge and
  from operational phase statements; Mach-Zehnder phase dependence is treated as
  whole-process kernel data.
- Existence and uniqueness are now separated: finite Hilbert/unistochastic
  representations may exist broadly, while uniqueness of lift, factorization,
  local algebra, covariance, and continuum limit remains extra.
- A claim audit and the QFT promotion gates are drafted: covariance, spectrum,
  vacuum/sector selection, continuum stability, local `*`-algebra convergence,
  gauge-center control, and lift-gauge discipline.
- Full continuum QFT reconstruction should not be claimed here unless
  covariance, spectrum, vacuum/sector selection, and continuum-limit
  hypotheses are explicitly added.

## V2 Paper 7: Free-QFT Promotion From ISP Stochastic Curvature

Suggested title:

`Free-QFT Promotion From ISP Stochastic Curvature`

Initial investigation draft:

`relativistic-isp-v2-paper7-free-qft-promotion-from-stochastic-curvature-investigation.md`

Main question:

> Can the Paper 1 free one-particle stochastic-curvature theorem be promoted into a standard free relativistic QFT representation, and exactly which lift, spectrum, vacuum/Fock, covariance, and local-algebra data must be added beyond `Gamma`?

Main job:

- prove or state a no-go theorem showing that Gamma-only stochastic curvature does not determine a unique free QFT;
- define the one-particle Hilbert lift and sampling convergence needed beyond Paper 1;
- add covariance gates for translations, time evolution, and the tested hypersurface/tangential action;
- define the positive-energy or complex-structure input;
- build the CAR/Fock local-net promotion for the Dirac benchmark;
- state a conditional free-fermion promotion theorem, clearly marking which data are extra representation inputs.

Pass condition:

- a precise Gamma-only no-go plus a conditional free-QFT promotion theorem for the free Dirac benchmark.

Fail condition:

- the required QFT structure has to be inserted so completely by hand that ISP contributes only transition probabilities and not a nontrivial stochastic-curvature substrate.

Current investigation status, 2026-05-16:

- Paper 7 has been started as the direct QFT follow-up to Paper 6.
- The draft separates four layers: stochastic kernels, Hilbert lift,
  one-particle continuum dynamics, and field-theoretic Fock/local algebra.
- It states QFT promotion gates: one-particle convergence, covariance,
  spectrum/complex structure, CAR/Fock promotion, local algebra, and continuum
  stability.
- The Gamma-only no-go is now formalized as a non-injectivity theorem: the same
  one-particle endpoint kernels and stochastic-curvature coefficients do not
  determine field statistics or a local algebra net.
- A minimal counterexample laboratory has been added: identical `Gamma(t)=I`
  data admit inequivalent phase-Hamiltonian lifts; the same one-particle lift
  admits different CAR/CCR field promotions; and identical four-state endpoint
  data admit different local algebra splits.
- The positive benchmark is now fixed as massive `1+1D` free Dirac/CAR, tied to
  Paper 1's sampled lattice Dirac theorem.
- The positive theorem ladder has been hardened: sampled one-particle
  convergence, explicit doubler policy, sampled spectral projection convergence,
  CAR vacuum correlation convergence, finite-polynomial stochastic-curvature
  response, and a final conditional free-Dirac/CAR promotion theorem.
- The positive result is explicitly a sampled-sector theorem; a full finite
  lattice Fock theorem over all regulator modes still needs Wilson/admissible
  doubler control or a proved low-energy sector projection.
- It frames the expected result as mixed: Gamma-only data do not determine a
  unique free QFT, but enriched ISP plus compatible lift/sector/local-net data
  may conditionally promote to a free fermion QFT candidate.
- QFT matching is assigned to Paper 8; Lorentz-covariant free-QFT completion is
  assigned to Paper 9; metric reconstruction is deferred to Paper 10.

## V2 Paper 8: Free-QFT Matching And Equivalence Benchmarks

Suggested title:

`Free-QFT Matching And Equivalence Benchmarks`

Initial investigation draft:

`relativistic-isp-v2-paper8-free-qft-matching-equivalence-benchmarks-investigation.md`

Main question:

> Does the enriched free Dirac/CAR candidate promoted in Paper 7 actually match standard massive `1+1D` free QFT at the level of local algebras, vacuum correlations, time evolution, spectrum, and tested covariance?

Main job:

- prove local vacuum correlation matching for compactly supported sampled test fields;
- prove equal-time CAR local-net matching;
- prove time-evolution and positive-energy spectrum matching on the sampled sector;
- match the stochastic-curvature response to the standard free-QFT field-polynomial action;
- audit exactly which standard QFT properties are matched and which remain outside scope.

Pass condition:

- enriched ISP reproduces standard massive `1+1D` free Dirac/CAR QFT predictions on sampled local field-polynomial observables.

Fail condition:

- the Paper 7 candidate remains QFT-shaped but fails to match standard free Dirac/CAR local correlations, dynamics, spectrum, or local-net structure.

Why this comes before metric reconstruction:

Metric reconstruction should not precede the audit that the promoted free object really matches standard free QFT on controlled observables.

Current investigation status, 2026-05-16:

- Paper 8 has been started as the QFT-matching bridge between Paper 7 and the
  later Lorentz-covariant QFT completion.
- The draft targets standard massive `1+1D` free Dirac/CAR QFT.
- The draft now states conditional theorems for local correlation matching,
  equal-time local-net matching, dynamics/spectrum matching, and tested
  curvature-response matching.
- It bundles those into Theorem 8.5: sampled-sector standard free-QFT matching.
- The theorem package has now been proof-hardened with an explicit weak
  local-polynomial convergence topology, CAR/GNS local-net matching convention,
  compact-time sampled dynamics, and finite-polynomial curvature-response
  domain.
- A Barandes compliance audit has been added: whole-process stochastic data
  remain primary, unrecorded partial-kernel Markov composition is avoided,
  Hilbert/CAR/Fock structures are declared enriched representation data, and
  Gamma-only QFT reconstruction is explicitly denied.
- It explicitly defers boost/full Lorentz covariance and includes an axiom audit
  distinguishing matched facts from deferred facts:
  full Lorentz covariance, Wightman/Haag-Kastler completeness, stress-energy,
  metric extraction, and dynamical geometry are not claimed.

## V2 Paper 9: Lorentz-Covariant Free-QFT Completion

Suggested title:

`Lorentz-Covariant Free-QFT Completion`

Initial investigation draft:

`relativistic-isp-v2-paper9-lorentz-covariant-free-qft-completion-investigation.md`

Main question:

> Does the enriched free Dirac/CAR candidate matched in Paper 8 also match standard massive `1+1D` free Dirac/CAR QFT as a Lorentz-covariant spacetime local theory?

Main job:

- construct finite-regulator boost generators `K_a=1/2(X_aH_a+H_aX_a)`;
- prove sampled boost-generator convergence to the standard free Dirac boost;
- prove sampled Poincare commutator convergence, including the finite lattice
  correction `C_a=(T_++T_-)/2`;
- prove finite-rapidity boost convergence on compact rapidity intervals;
- lift boost convergence to CAR/Fock local field-polynomial predictions;
- extend the equal-time CAR net to a spacetime local net through the free Dirac
  causal propagator;
- prove spacelike graded locality and detector order-independence for even local
  observables;
- audit Wightman/Haag-Kastler properties honestly;
- match the tested stochastic-curvature tangential response to the standard
  local-net tangential action;
- keep stress-energy and metric extraction outside scope.

Pass condition:

- enriched ISP, with the Paper 7/8 representation data, matches standard
  massive `1+1D` free Dirac/CAR QFT as a spacetime-covariant local theory on the
  declared sampled/finite-polynomial sector.

Fail condition:

- the Paper 8 equal-time match cannot be upgraded to a Lorentz-covariant
  spacetime local-net match without adding uncontrolled or ontology-confusing
  structure.

Why this comes before metric reconstruction:

Metric reconstruction should not be attempted before the promoted object has
been checked against relativistic QFT itself: boosts, spacetime locality,
microcausality, and Poincare covariance.

Current investigation status, 2026-05-16:

- Paper 9 has been created as the missing bridge between Paper 8 and metric
  data.
- It now chooses Route B as the primary target: finite-regulator boost
  approximants are constructed and shown, conditionally, to converge to the
  standard Dirac boost on sampled smooth sectors.
- The theorem package defines `K_a=1/2(X_aH_a+H_aX_a)`, proves sampled
  boost-generator convergence, proves sampled Poincare commutator convergence
  with the lattice correction `C_a`, proves finite-rapidity convergence, lifts
  boosts to CAR/Fock local field-polynomial predictions, and then adds the
  spacetime local-net/microcausality completion.
- The Route-B core has been proof-hardened: Paper 9 now states the lattice
  shift convention, weighted Schwartz/Sobolev domains, nonwrapping/growing-ring
  seam policy, exact infinite-lattice commutator derivation, and an explicit
  `a^2 Lambda(a)^3 -> 0` cutoff condition for the sampled boost-generator
  estimate.
- The Lorentz spine has also been hardened after the generator theorem:
  compact-rapidity boost orbits are controlled in weighted Sobolev norms,
  finite positive-energy polarization is shown to intertwine with boosts
  asymptotically, finite vacuum invariance is explicitly asymptotic, and the
  CAR/Fock boost theorem is restricted to fixed finite field polynomials.
- The local-net layer now separates boosted equal-time Cauchy data from compact
  spacetime support: boosts are controlled on Schwartz/weighted Cauchy data,
  while compact spacetime locality is defined by spacetime smearings and the
  Dirac causal propagator. The microcausality proof has been expanded through
  the causal CAR pairing, and the failure appendix now covers seam terms,
  doubler leakage, narrow domains, polarization failure, detector
  incompleteness, and curvature/tangential-action mismatch.
- It preserves Barandes discipline: boosts, CAR/Fock, and spacetime nets are
  enriched representation data, not consequences of `Gamma` alone.

## V2 Paper 10: Metric Data Gate, Not Gravity Yet

Suggested title:

`Metric Data from Stochastic Exchange Curvature`

Initial investigation draft:

`relativistic-isp-v2-paper10-metric-data-from-stochastic-exchange-curvature-investigation.md`

Main question:

> In more than one spatial dimension, can the coefficient of stochastic exchange curvature be identified with inverse spatial metric data?

Main job:

- extend the free stochastic-curvature theorem to at least `2+1D`;
- extract the coefficient of `N partial_j M - M partial_j N`;
- test whether that coefficient transforms as `h^{ij}` or an inverse metric density;
- prove symmetry, positivity, locality, and coordinate behavior where applicable;
- keep geometry fixed and nondynamical at this stage.

Pass condition:

- stochastic exchange curvature can reconstruct fixed-background spatial metric data from the hypersurface-deformation bracket.

Fail condition:

- the coefficient is regulator-dependent, non-tensorial, nonlocal, or only visible after adding non-`Gamma` lift data.

Why this is last in the v2 non-gravitational roadmap:

Metric reconstruction is the first gate toward gravity, but it should only be attempted after the non-gravitational continuum, QFT matching, and Lorentz-covariant QFT structure are under control.

Current investigation status, 2026-05-16:

- Paper 10 has been moved from the former Paper 9 metric-data slot after the
  Lorentz-covariant free-QFT completion was inserted as Paper 9.
- The draft defines a metric-candidate coefficient `C^{ij}` through the
  continuum form
  `K_i[C^{ij}(N partial_j M - M partial_j N)]`.
- It states the required identification gates: locality/first-derivative form,
  coordinate behavior, symmetry, positivity, regulator stability, and no hidden
  lift dependence.
- It explains why `1+1D` is insufficient for metric reconstruction: one spatial
  dimension can recover a tangential scalar, but cannot test tensor structure,
  cross terms, or positivity of an inverse metric.
- The first model target is a flat `2+1D` free benchmark, followed by an
  anisotropic or rotated constant-metric test to expose `C^{12}=C^{21}` cross
  terms.
- Fixed curved backgrounds, stress-energy response, and dynamical geometry are
  explicitly deferred until the flat multi-dimensional metric-coefficient test
  passes.

## Decision Tree

1. If V2 Paper 1 fails, the stochastic-curvature interpretation should be downgraded to finite-model analogy.
2. If V2 Paper 2 fails, relativistic ISP remains a fixed-regulator theory without real covariance.
3. If V2 Paper 3 fails, interacting ISP may be too nonlocal at the raw comparison-map level.
4. If V2 Paper 4 fails, local observables require extra primitive structure beyond stochastic kernels.
5. If V2 Paper 5 fails, gauge theory remains finite-benchmark-only.
6. If V2 Paper 6 fails constructively, the result may still be valuable if it states exactly which data ISP lacks.
7. If V2 Paper 7 fails, free QFT promotion requires more representation structure than the current ISP stack controls.
8. If V2 Paper 8 fails, the promoted object is not yet matched to standard free QFT and metric reconstruction is premature.
9. If V2 Paper 9 fails, the program has an equal-time free-QFT match but not yet a Lorentz-covariant spacetime QFT match.
10. Only if Papers 1 through 9 substantially succeed should metric reconstruction become the next central target.

## What Not To Do Next

Do not make the next paper about gravity.

Do not add another finite benchmark unless it directly tests one of the v2 gates.

Do not claim Lorentz covariance from finite stochastic isomorphisms.

Do not identify raw comparison maps with local observables.

Do not treat Bell-compatible setting-dependent full circuits as a general Bell local-causality theorem.

Do not treat compact `U(1)` truncation as a continuum compact-rotor theorem.

Do not use the conceptual stochastic-curvature leap as a substitute for the free continuum theorem.

## Recommended Immediate Work

With V2 Papers 7 and 8 now establishing conditional free-QFT promotion and
sampled free-QFT matching, the next concrete work is Paper 9:

`Lorentz-Covariant Free-QFT Completion`

Minimum deliverables:

1. decide whether any Paper 9 claims should be promoted from theorem-framework
   to final-paper theorem statements or left as conditional hypotheses;
2. check whether the spacetime-local test-function class should be
   `C_c^\infty` only or an explicitly completed test-function topology;
3. export only the sampled Route-B Lorentz-covariant free-QFT facts to Paper 10.

## Bottom Line

Relativistic ISP becomes viable when exchange defects stop being finite benchmark artifacts and become a regulator-stable hypersurface-deformation law.

The v2 roadmap is therefore:

```text
finite exchange defects
-> free stochastic curvature theorem
-> projective hypersurface dynamics
-> interacting comparison-map locality
-> operational observable reconstruction
-> continuum gauge benchmark
-> QFT reconstruction or no-go
-> free-QFT promotion
-> free-QFT matching and equivalence benchmarks
-> Lorentz-covariant free-QFT completion
-> metric data gate
```

Only after this chain should the program seriously return to gravity.

## V3 Roadmap

The follow-up roadmap for pushing toward full Lorentz-covariant interacting ISP, continuum QFT reconstruction, and non-Abelian gauge theory is:

`relativistic-isp-roadmap-v3-toward-interacting-qft-nonabelian.md`
