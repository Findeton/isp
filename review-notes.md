# Physics Corpus Review Notes

Author: Felix Robles Elvira

Reviewer stance: expert physics/mathematical-physics review of the papers in this folder, with emphasis on errors, overclaims, missing hypotheses, and refinements that would improve publishability. This is not a full independent rederivation of every displayed coefficient, but it does check the structure, examples, scope claims, and validation layer across the corpus.

## Implementation Status

Applied follow-up fixes on 2026-05-12:

- Corrected the qubit generator derivation and the three-site tight-binding frequency mismatch in `entropy-indivisible.html`.
- Restored Python 3.8 compatibility for both validation scripts and verified both scripts run successfully in the configured environment.
- Added Schur-Hadamard lift-scope caveats to the entropy and entanglement papers.
- Rephrased the isolated ZZ-gate discussion around terminal-kernel invisibility rather than treating the phrase "phantom entanglement" as an unqualified physical claim.
- Added finite stochastic-isomorphism, fixed-benchmark, nonwrapping-support, regulator-selection, conditional higher-order closure, finite-ring holonomy, AQFT, gauge-center, and Bell-local-causality scope refinements across the relevant relativistic ISP papers.

## Original High-Priority Findings

1. `entropy-indivisible.html` has two concrete worked-example errors.
   - In the qubit generator discussion, the text identifies `Gamma_00(t)` with the evolved probability `p_0(t)`, which depends on the initial mixture. The transition entry is instead `cos^2(omega t/2)` for the Rabi transition matrix. The final `K_01 = (omega/2) tan(omega t)` result can still be obtained from the transition matrix, but the derivation should be corrected.
   - In the three-site chain, the Hamiltonian is written as adjacency divided by `sqrt(2)`, whose eigenvalues are `-1,0,+1`. The probabilities should involve `cos t` and `sin t`, not `cos(sqrt(2) t)` and `sin(sqrt(2) t)`. If the intended frequency is `sqrt(2)`, remove the `/sqrt(2)` normalization from the Hamiltonian.

2. The validation scripts do not run in the configured Python environment.
   - `validate_minimal_interacting_gauge_matter_benchmark.py` and `validate_truncated_u1_benchmark.py` use `list[list[complex]]`, which requires Python 3.9+. The configured environment is Python 3.8.20, so both fail before any benchmark check runs. Either require Python >=3.9 or replace these annotations with `typing.List` / quoted annotations compatible with 3.8.

3. The Schur-Hadamard gauge discussion needs a sharper physical qualifier across `entropy-indivisible.html`, `entanglement-indivisible.html`, and the relativistic papers.
   - Arbitrary entrywise rephasing preserves `Gamma = |Theta|^2`, but it does not generally preserve unitarity of `Theta`. The resulting `rho = Theta diag(p) Theta^dagger` can still be a positive trace-one matrix if the columns remain normalized, but it is not automatically a closed-system unitary quantum state. Claims about von Neumann entropy being gauge-dependent should specify whether the allowed lifts are arbitrary Gamma-lifts, unistochastic/unitary lifts, or circuit-realizable lifts.

4. The relativistic program repeatedly uses finite stochastic isomorphisms for covariance. On a finite set, an invertible stochastic map whose inverse is also stochastic is a permutation. If the Lorentz maps are meant to be nontrivial boosts rather than relabelings between discretizations, the papers need a different notion: embeddings, coarse-graining/refinement maps, projective limits, or continuum configuration functoriality.

5. The phrase "Einstein causality" should remain explicitly benchmark-relative. The later papers often do this well, but abstracts still risk sounding stronger than the theorem: the proved locality is for induced operational/effect-space nets, preserving subclasses, fixed finite benchmarks, or boundary-flux-resolved blocks, not for a full Haag-Kastler QFT with additivity, time-slice, isotony in the continuum, and type-III local algebras.

## Cross-cutting refinements

- Separate three levels everywhere: raw comparison maps `J_R`, operational stochastic instruments, and observables/effects. Several papers correctly warn that raw maps are not observables; that warning should be repeated whenever a bridge theorem is invoked.
- Replace phase-roadmap language in theorem statements with mathematical hypotheses. Phrases such as "phase X closes" are fine for the roadmap, but abstracts and theorems should foreground exact assumptions and conclusions.
- Add dependency diagrams or theorem ledgers. Many papers depend on exact results from earlier papers; readers need a one-page map of which claims are unconditional, conditional, numerical, or deferred.
- Treat continuum limits as separate theorems. Fixed finite-lattice exactness is valuable, but it does not imply volume-uniform inverse control, cutoff-uniform estimates, Lorentz covariance, or continuum QFT locality.
- For every coefficient paper, include a machine-checkable symbolic or numerical notebook/script, and state the Python version. Right now the validation layer is a good idea but not executable in the selected environment.

## Paper-by-paper notes

### `The Stochastic-Quantum Correspondence.mhtml`

The correspondence is best read as a representation/dilation theorem, not by itself as physical equivalence to ordinary quantum theory. The main refinement is to distinguish arbitrary stochastic processes from unistochastic processes and from processes generated by local Hamiltonians. The paper's own "category problem" is essential: locality, tensor product structure, energy, symmetries, and measurements are extra data, not automatic consequences of a transition matrix.

### `The Stochastic-Quantum Theorem.mhtml`

The theorem's breadth is mathematically interesting, but the phrase "any indivisible stochastic process corresponds to a unitarily evolving quantum system" needs careful reading. If the Hilbert space/dilation is freely enlarged, the result risks being physically underconstrained. For later relativistic work, the missing issue is not existence of some unitary dilation but existence of a local, covariant, physically natural one.

### `Quantum Systems as Indivisible Stochastic Processes.mhtml`

Useful conceptual foundation, but the Schur-Hadamard gauge material should be carried forward with the unitarity/circuit-realizability caveat above. Dynamical symmetries at the Gamma level may be much weaker than symmetries of a Hamiltonian or local field theory.

### `entropy-indivisible.html`

Correct the qubit and three-site example errors described above. Also refine the entropy-gap identity: `S[p] - S_vN[rho] = C(rho)` holds when `p` is the diagonal of `rho` in the chosen configuration basis. It is not a Gamma-only identity unless a lift has been chosen.

### `entanglement-indivisible.html`

The process-entanglement measure is a sensible Gamma-level correlation measure, but calling ZZ-gate entanglement a "terminal-basis phantom" is rhetorically risky. The safer statement is: the isolated Z-basis transition kernel cannot witness phase entangling power; the full circuit or a richer operational context can. Also, LOCC monotonicity and entanglement-capacity equality are major open burdens and should not be implied by examples.

### `relativity-indivisible-rewrite.html`

The programmatic move from event-local dynamics to finite hypersurface kernels is coherent. Main refinements: define Lorentz covariance in a way that is not just finite-set relabeling; separate pseudo-generators from physical stochastic kernels; and avoid presenting disjoint product-factor control commutativity as a nontrivial relativistic locality theorem. It is a sanity check, not yet a QFT locality result.

### `light-cones-vs-relativistic-isp.html`

Good explanatory artifact, but it risks caricaturing light-cone physics as merely event-by-event. In relativistic QFT, causal propagation is also formulated via algebras on regions and Cauchy-surface evolution. Refine the comparison to say ISP changes the primitive probabilistic object, not that standard relativity lacks hypersurface/global formulations.

### `collar-excision-exchange-defect.html`

Strongest early technical paper in the stack. The no-go for rule uniqueness and the bond-centered renormalized limit are valuable. Needed refinements: be explicit that the result is 1+1D, one-particle, fixed lattice, free Dirac; the tangential pseudo-generator is not yet the Dirac-Schwinger algebra in a full field theory.

### `exact-localized-finite-deformations-free-dirac-exchange-defect.html`

The finite-support theorem is well scoped. The main risk is hidden dependence on invertibility of `Gamma_0(Delta)` and uniformity in Delta/lattice size. State the allowed Delta neighborhood and whether constants depend on support size, mass, lattice spacing, and ring length.

### `general-supports-higher-coefficients-bond-centered-thin-slab-law.html`

Appropriately narrowed to leading support order. Add a clear nonwrapping versus wrapping distinction for intervals on the periodic ring, since support prototypes near the periodic seam may have different minimal-strip data.

### `universality-regulator-stability-bond-centered-thin-slab-law.html`

The onset-renormalized universality statement is the right weaker replacement for rule uniqueness. Keep emphasizing that it is not raw microscopic universality. A useful refinement would be to state whether the admissible regulator class is physically motivated or merely mathematically admissible.

### `higher-coefficients-strip-moment-closure-bond-centered-thin-slab-law.html`

The overlap-window factorization is plausible and useful. The strip-moment theorem is conditional; the paper should make the conditionality visible in the title/abstract and avoid letting readers infer that general higher-order closure has been proved.

### `broader-regulator-stability-across-support-prototypes.html`

Good negative result: raw prototype-level universality fails. The positive criterion is still mostly a theorem schema. Add examples beyond the lambda family before using it as evidence of broad regulator stability.

### `explicit-higher-coefficients-first-nontrivial-singleton-strip-moments.html`

Narrow, useful coefficient paper. It needs an independent reproducibility artifact for the boundary-active `A_n^(2)` block. Also clarify whether mass-independence of the boundary-facing shell depends on the specific lattice Dirac discretization.

### `explicit-regulator-comparison-first-non-leading-singleton-order.html`

The distinction between raw nonuniversality and normalized strip-moment universality is strong. Main caveat: this is still a singleton, distance-three, common-onset result; do not let it stand in for broad non-leading universality.

### `bond-centered-thin-slab-extensions.html`

This file now reads correctly as bridge/scaffold. It should not be cited as a theorem paper except for definitions or roadmap context. Consider splitting remaining Fock/gauge scaffold into short appendices or deleting superseded sections to avoid accidental overcitation.

### `variable-particle-number-relativistic-isp-fock-space-lift-sector-changing-dynamics.html`

The number-preserving lift by second quantization is natural. The sector-changing part is promising but very finite/local. Add CAR sign-convention details and clarify which sector-changing kernels remain honest stochastic Gamma kernels versus algebraic comparison objects.

### `minimal-u1-gauge-coupling-holonomy-relativistic-isp.html`

The static U(1) holonomy classification is conventional and solid at finite ring level. Main cautions: the gauge-dressed continuum operator is a target/action result, not a full gauge-coupled exchange-algebra theorem; the first holonomy-sensitive order `Delta^(L+2)` is finite-ring/wrapped physics and may disappear or become nonuniform in large-volume limits.

### `dynamical-abelian-gauge-field-gauss-law-relativistic-isp.html`

The finite link-space benchmark is well motivated. The rotor discussion correctly identifies an infinite global-flux tower; that is a major obstruction, not a side note. Do not advertise compact U(1) completion until cutoff-uniform inverse control and kernel existence are proved.

### `localized-controls-detectors-operational-relativity-isp.html`

The operational finite-instrument calculus is useful. The largest conceptual risk is Bell language: a setting-dependent full-circuit account can reproduce quantum joint laws, but Bell's local causality issue is not solved merely by making settings active operations. The paper does flag this; keep the restricted Bell-1976 theorem visibly restricted.

### `einstein-causality-bridge-exchange-defect-haag-kastler-relativistic-isp.html`

Good bridge theorem if read as induced finite effect-space locality. It should not be marketed as Haag-Kastler reconstruction. Missing AQFT axioms include continuum isotony/additivity, time-slice, covariance, spectrum/energy, quasilocal C*-completion, and type-III local structure.

### `boundary-flux-resolved-einstein-causality-relativistic-isp.html`

This is a strong refinement: Gauss-law constraints obstruct naive tensor factorization but can be handled by boundary centers/flux sectors. The main improvement is to connect explicitly to standard algebraic gauge-theory language: centers, edge modes, electric center choices, and superselection sectors.

### `minimal-interacting-gauge-matter-benchmark-relativistic-isp.html`

The reduced Z2 benchmark is honestly scoped. The phrase "genuinely interacting" should always be tied to the reduced matter Hamiltonian, because one-dimensional Z2 gauge theories can have dual/free descriptions. The current conventional-physics section is important and should stay.

### `reduced-strip-overlap-companion-z2-benchmark-relativistic-isp.html`

Good as a companion calculation, but it is highly specialized. Add a table mapping each coefficient/order to the exact state-space prototype used, and separate exact symbolic statements from numerical extrapolation.

### `truncated-u1-matter-link-benchmark-relativistic-isp.html`

The open-chain truncated compact U(1) benchmark is a reasonable next step. The no-truncation condition is not a technicality; it defines the physical sector on which elimination is valid. State very clearly how conclusions change when matter configurations hit the truncation boundary.

### `boundary-flux-resolved-einstein-causality-relativistic-isp.html`, `minimal-interacting-gauge-matter-benchmark-relativistic-isp.html`, and `truncated-u1-matter-link-benchmark-relativistic-isp.html` together

These papers form the most physically convincing gauge-theory arc. The refinement to add is a unified comparison to standard lattice gauge theory: unreduced local gauge theory versus reduced nonlocal matter variables; electric-center locality; and which statements survive as cutoff/volume limits.

### Validation scripts

`validate_minimal_interacting_gauge_matter_benchmark.py` and `validate_truncated_u1_benchmark.py` are valuable, but currently fail under Python 3.8.20 because of PEP 585 generics. After fixing the version issue, add command-line output that summarizes pass/fail tolerances and run them in CI or at least document the expected Python version.
