# Investigation: V2 Paper 2 - Projective Hypersurface Kernel Dynamics

Author: Felix Robles Elvira

Date: 2026-05-13

Purpose: investigate the next viability gate after the free stochastic-curvature theorem. Paper 1 showed that, in the free one-particle benchmark, a normalized exchange defect can converge to the tangential hypersurface-deformation generator. Paper 2 asks where such limits live when hypersurfaces, lattice regulators, support discretizations, and configuration spaces change.

Suggested paper title: `Projective Hypersurface Kernels and Foliation Compatibility in Relativistic ISP`.

Consolidated draft now created:

`relativistic-isp-v2-paper2-projective-hypersurface-kernel-dynamics.md`

## Executive Verdict

V2 Paper 2 is necessary before moving to interacting inverse-control or gauge-continuum claims. The pre-Paper-2 corpus had exact finite hypersurface kernels, exact finite comparison maps, finite exchange defects, operational locality, induced finite nets, gauge-sector block decompositions, and the V2 Paper 1 free stochastic-curvature theorem. What it lacked was a projective/refinement framework that says what continuum covariance means for a family of changing finite stochastic configuration spaces. The consolidated Paper 2 draft now supplies that framework at theorem-framework level.

The right conceptual move is not finite-set isomorphism. A fixed finite lattice can only support covariance under relabelings that preserve that lattice. A continuum relativistic ISP needs a weaker and more natural object: a projective family of finite stochastic kernels over regulated hypersurface configuration spaces, with coarse-graining maps that make kernels, comparison maps, exchange defects, states, and effects compatible across refinements.

The strongest safe Paper 2 target is therefore a framework theorem plus an error-propagation theorem:

> If regulated hypersurface kernels are projectively compatible and the reference kernels are invertible in a common refinement regime, then the induced comparison maps and exchange defects are also projectively compatible. If compatibility is only asymptotic, the comparison-map and exchange-defect errors are controlled by explicit primitive-kernel errors multiplied by reference-inverse and comparison-map inverse bounds. Foliation compatibility can then be stated as equality in the projective effect/state system, or equality modulo a separately specified projective tangential correction, rather than equality of finite matrices on one regulator.

This would not yet construct a full Lorentz-covariant ISP. It would define the mathematical arena in which such a construction can be tested.

## Why Paper 2 Follows Paper 1

Paper 1 proves a free stochastic-curvature theorem in a controlled regulator setting. But that result still lives in a particular regulated representation: a one-particle lattice, a chosen sampling map, and a chosen finite-slab lift. To become part of a relativistic theory, the result must survive comparison across regulators.

Paper 2 should answer:

- what is a regulated hypersurface configuration space `C_{Sigma,a}`;
- how does a finer configuration project to a coarser one;
- when are two finite kernels at different regulators the same continuum stochastic process;
- how do localized deformation maps `J_R` and exchange defects `E_{R,S}` transform under refinement;
- how should foliation compatibility be stated without imposing Markov divisibility.

Without this, later papers risk proving facts on unrelated finite lattices rather than a single continuum-directed ISP.

## Existing Inputs From The Corpus

### Input 1: hypersurface kernels are already formulated

The relativistic architecture paper defines hypersurface transition kernels between Cauchy hypersurfaces and motivates localized finite deformations. It also records the ISP Dirac-Schwinger condition as an infinitesimal target.

Important limitation: that paper is architectural. It does not build a directed projective system of regulated hypersurface configuration spaces.

### Input 2: exact finite relative dynamics exist at fixed benchmark scope

The free and gauge papers define exact finite primitive kernels, localized comparison maps, and exchange defects on fixed finite configuration spaces. In the free one-particle benchmark,

```math
J_R(\Delta)=\Gamma_R(\Delta)\Gamma_0(\Delta)^{-1},
\qquad
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}.
```

The induced-locality bridge also identifies regional raw relative-dynamics groups at fixed benchmark scope.

Important limitation: all of this is fixed-regulator mathematics. It does not say how `J_R` or `E_{R,S}` behave when the regulator changes.

### Input 3: finite induced nets are available, but not continuum Haag-Kastler nets

The induced-locality papers show that, under explicit commutation or preserving-class hypotheses, finite effect-space algebras satisfy Einstein-causality statements. This is a useful dual/effect-side precedent.

Important limitation: finite induced Einstein causality is not a continuum algebraic-QFT net. Paper 2 should not claim Haag-Kastler reconstruction.

### Input 4: gauge-sector block decompositions show why projective structure matters

The finite gauge papers already distinguish full configuration spaces, physical Gauss sectors, boundary-flux centers, and preserving subclasses. They show that naive tensor factorization fails in constrained sectors.

Important limitation: these are finite and fixed-cutoff results. Projective compatibility across link cutoff, lattice refinement, and hypersurface regulator is still missing.

### Input 5: ISP transition matrices are indivisible

Barandes-style ISP dynamics does not generally compose through intermediate stochastic kernels. Therefore Paper 2 must not impose Markov composition

```math
\Gamma_{\Sigma_2\leftarrow\Sigma_0}
=
\Gamma_{\Sigma_2\leftarrow\Sigma_1}
\Gamma_{\Sigma_1\leftarrow\Sigma_0}
```

as a general axiom. Projective compatibility concerns refinement of the same endpoint kernel, not divisibility through intermediate hypersurfaces.

### Input 6: finite stochastic isomorphisms are too small

On a finite configuration space, an invertible stochastic map whose inverse is also stochastic is a permutation. This means finite stochastic covariance cannot carry nontrivial boosts, regulator changes, or continuum comparison maps by itself. Paper 2 should make this a lemma near the beginning, because it is the clean mathematical reason projective/refinement structure is not optional.

## Core Definitions To Build

### Regulated hypersurface configuration system

For each hypersurface `Sigma`, define a directed regulator set `I_Sigma`. An element `a in I_Sigma` labels a finite configuration space

```math
C_{\Sigma,a}.
```

For a refinement `a' >= a`, choose a deterministic or stochastic coarse-graining map

```math
P_{\Sigma,a\leftarrow a'}:
\mathbb R^{C_{\Sigma,a'}}\to\mathbb R^{C_{\Sigma,a}}.
```

The maps should be column-stochastic and satisfy

```math
P_{\Sigma,a\leftarrow a}=I,
\qquad
P_{\Sigma,a\leftarrow a''}
=
P_{\Sigma,a\leftarrow a'}P_{\Sigma,a'\leftarrow a''}
```

for `a'' >= a' >= a`.

If refinement is deterministic, there is a restriction map of configurations

```math
r_{\Sigma,a\leftarrow a'}:C_{\Sigma,a'}\to C_{\Sigma,a},
```

and

```math
[P_{\Sigma,a\leftarrow a'}]_{c,c'}=1
\quad\text{iff}\quad
c=r_{\Sigma,a\leftarrow a'}(c').
```

### Projective states

A projective state on `Sigma` is a compatible family

```math
p_\Sigma=(p_{\Sigma,a})_{a\in I_\Sigma},
```

with

```math
P_{\Sigma,a\leftarrow a'}p_{\Sigma,a'}=p_{\Sigma,a}
```

for all refinements `a' >= a`.

This is the probability-side analog of cylinder-measure consistency. Paper 2 should avoid assuming that every such projective family comes from a countably additive continuum measure unless separate compactness or standard-Borel hypotheses are added.

### Cylinder effects

The dual map

```math
P_{\Sigma,a\leftarrow a'}^*:
(\mathbb R^{C_{\Sigma,a}})^*\to(\mathbb R^{C_{\Sigma,a'}})^*
```

pulls coarse effects back to fine cylinder effects. Two effects at different regulators are equivalent if they agree after pullback to a common refinement. Operational covariance should be stated on these projective/cylinder effect classes.

### Projective hypersurface kernels

For two hypersurfaces `Sigma_0, Sigma_1`, a projective kernel family is a collection of finite stochastic kernels

```math
\Gamma_{\Sigma_1\leftarrow\Sigma_0}^{a}
:
\mathbb R^{C_{\Sigma_0,a}}
\to
\mathbb R^{C_{\Sigma_1,a}}
```

or, more generally, kernels indexed by compatible regulator pairs. In the equal-index case, projective compatibility is

```math
P_{\Sigma_1,a\leftarrow a'}
\Gamma_{\Sigma_1\leftarrow\Sigma_0}^{a'}
=
\Gamma_{\Sigma_1\leftarrow\Sigma_0}^{a}
P_{\Sigma_0,a\leftarrow a'}.
```

This is the central naturality square of Paper 2.

### Projective localized kernels

For a regulated support system `R_a subset L_{Sigma,a}`, where `L_{Sigma,a}` is the regulated cell/link/mode set rather than the full configuration set, define localized kernels

```math
\Gamma_{R_a}^{a},
```

compatible with refinement if

```math
P_{\Sigma_1,a\leftarrow a'}\Gamma_{R_{a'}}^{a'}
=
\Gamma_{R_a}^{a}P_{\Sigma_0,a\leftarrow a'}.
```

The support system must itself be compatible: the coarse region should be the image or thickened image of the fine region under coarse-graining.

## Main Theorems Paper 2 Should Prove

### Theorem A: projective kernel action on states and effects

If `Gamma^a` is a projectively compatible hypersurface kernel family, then it maps projective states on `Sigma_0` to projective states on `Sigma_1`, and its dual maps cylinder effects on `Sigma_1` to cylinder effects on `Sigma_0`.

Proof idea: apply the naturality square to the state compatibility equation. The effect statement is the dual square.

This theorem is elementary but foundational. It says the continuum object is not a single finite matrix but an equivalence class/family of compatible finite kernels.

### Theorem B: comparison-map naturality

Assume both the reference kernels and localized kernels are projectively compatible:

```math
P_1A^{a'}=A^aP_0,
\qquad
P_1B_R^{a'}=B_R^aP_0.
```

Here `A^a=Gamma_0^a`, `B_R^a=Gamma_R^a`, and

```math
P_i=P_{\Sigma_i,a\leftarrow a'}.
```

Assume the reference kernels are invertible in the slab/regulator range under discussion. Then

```math
P_1J_R^{a'}=J_R^aP_1,
```

with the domain/codomain indices adjusted to the slab. In the equal-slice comparison-map case this is simply

```math
P_aJ_R^{a'}=J_R^aP_a.
```

Proof idea: from `P_1A^{a'}=A^aP_0` and invertibility,

```math
(A^a)^{-1}P_1=P_0(A^{a'})^{-1}.
```

Then

```math
P_1J_R^{a'}
=P_1B_R^{a'}(A^{a'})^{-1}
=B_R^aP_0(A^{a'})^{-1}
=B_R^a(A^a)^{-1}P_1
=J_R^aP_1.
```

This theorem is central because it proves that algebraic comparison maps inherit projective consistency from primitive kernels.

### Theorem C: exchange-defect naturality

Under the hypotheses of Theorem B for `R` and `S`, and assuming the comparison-map inverses exist in a common small-slab regime,

```math
P_1E_{R,S}^{a'}=E_{R,S}^aP_1.
```

Proof idea: use comparison-map naturality for `J_R`, `J_S`, and their inverses, then multiply the intertwinings through

```math
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}.
```

This is the exact projective statement needed after Paper 1: stochastic curvature should be a projective family of exchange defects, not one finite matrix.

### Theorem D: asymptotic naturality and inverse-control bookkeeping

Exact projective compatibility is not established for the actual lattice-continuum problem. Paper 1 proves convergence on sampled smooth profiles, not exact block-spin compatibility of every finite kernel. Paper 2 should therefore include an asymptotic theorem.

Let

```math
R_0=P_1A^{a'}-A^aP_0,
\qquad
R_R=P_1B_R^{a'}-B_R^aP_0.
```

Then

```math
P_1J_R^{a'}-J_R^aP_1
=
(R_R-J_R^aR_0)(A^{a'})^{-1}.
```

Thus primitive-kernel refinement errors propagate to comparison-map errors only if the reference inverse and comparison map are controlled. A corresponding telescoping estimate propagates comparison-map and inverse-comparison-map errors to `E_{R,S}`.

This is the theorem-level bridge into Paper 3: interacting locality must control `Gamma_0^{-1}`, `J_R`, and `J_R^{-1}` after Born-squared projection, not only Hamiltonian commutators.

### Theorem E: projective foliation equivalence

Let `P` and `Q` be two regulated hypersurface paths with the same endpoints. Let each path define a projective family of endpoint kernels

```math
\Gamma_P^a,
\qquad
\Gamma_Q^a.
```

The paths are projectively equivalent if, for every coarse regulator `a`, there is a refinement `a' >= a` such that their pushdowns agree on cylinder effects/states:

```math
P_{a\leftarrow a'}\Gamma_P^{a'}
=
P_{a\leftarrow a'}\Gamma_Q^{a'}
```

In the curved/exchange setting, they may instead differ by a declared projective tangential correction. To make that a true equivalence relation rather than notation, the tangential corrections must form a compatible projective group or groupoid, at least to the perturbative order being claimed.

This theorem may initially be a definition plus basic equivalence-relation lemma. The hard physics enters later when proving nontrivial path equivalence for actual kernel families.

## The Most Important Choice: Projective, Not Markovian

Paper 2 must sharply distinguish two ideas.

Wrong axiom for ISP:

```math
\Gamma_{\Sigma_2\leftarrow\Sigma_0}
=
\Gamma_{\Sigma_2\leftarrow\Sigma_1}
\Gamma_{\Sigma_1\leftarrow\Sigma_0}.
```

This would impose divisible Markov dynamics and erase the ISP content.

Correct axiom:

```math
P\Gamma^{\text{fine}}_{\Sigma_1\leftarrow\Sigma_0}
=
\Gamma^{\text{coarse}}_{\Sigma_1\leftarrow\Sigma_0}P.
```

This says the same endpoint stochastic law is represented consistently across regulators. It does not say the law factors through intermediate hypersurfaces.

Localized comparison maps and exchange defects then express finite-deformation path dependence inside this projective framework.

## How Paper 1 Feeds Paper 2

Paper 1 gives the first nontrivial continuum object to place in the projective framework:

```math
\frac{1}{c_\lambda^2\Delta(a)^4}
(\mathbb E_{a,\Delta(a)}^{(\lambda)}[N,M]-I)\iota_a\phi
\to
\iota_aK_\parallel[N\partial_xM-M\partial_xN]\phi.
```

Paper 2 should reinterpret this as a projective statement:

- `E_a` is one representative of a refinement-compatible exchange-defect family;
- the limiting tangential operator is the action on projective/cylinder test profiles;
- regulator changes are controlled by naturality squares, not by finite permutation covariance.

Important correction: Paper 1 does not prove exact projective compatibility of the full finite free-Dirac kernels across lattice spacings. It proves a normalized strong limit on sampled smooth profiles. Paper 2 should therefore phrase the connection through asymptotic projective compatibility and test-profile/cylinder-effect convergence unless a separate block-spin theorem is added.

This allows Paper 1's curvature theorem to become a statement about continuum-directed ISP dynamics rather than about one chosen lattice.

## Failure Modes

Paper 2 should be allowed to fail. The important failure modes are:

1. **No useful coarse-graining maps.** If physically meaningful coarse-graining destroys the kernel information needed for comparison maps, the projective route may be too weak.
2. **Inverses do not descend.** If reference-kernel inverse control is not stable under refinement, `J_R` may fail to be projective even when primitive kernels are.
3. **Support systems are regulator-dependent in an uncontrolled way.** If `R_a` cannot be chosen compatibly, exchange defects will not define a projective family.
4. **Gauge constraints break naive projection.** Physical-sector projections may require center-resolved or boundary-flux-labeled projective systems rather than one unfibered system.
5. **Foliation compatibility collapses into Markov divisibility.** If the only clean path-equivalence notion forces kernel composition through intermediate slices, it is not an ISP-compatible covariance notion.
6. **Asymptotic errors are amplified by inverses.** Even small primitive-kernel refinement errors may become useless if `Gamma_0^{-1}`, `J_R`, or `J_R^{-1}` grow too fast.

## Minimal Publishable Paper 2

A minimal successful Paper 2 should prove the following without constructing a full continuum model:

1. define regulated hypersurface configuration systems;
2. define projective states and cylinder effects;
3. define projectively compatible hypersurface kernels;
4. prove projective kernel action on states/effects;
5. prove comparison-map naturality;
6. prove exchange-defect naturality;
7. prove the asymptotic/error-propagation version with explicit inverse-control hypotheses;
8. define projective foliation equivalence;
9. explain why this avoids Markov-divisibility assumptions;
10. show how the Paper 1 free stochastic-curvature theorem fits into the framework without claiming exact block-spin compatibility.

This would be a real structural advance: it would tell later papers what it means for their finite kernels to approximate the same relativistic ISP.

## Stronger Version

A stronger Paper 2 would add at least one worked nontrivial projective family.

Candidate examples:

1. **Free one-particle lattice refinement.** Compare a lattice of spacing `a` to one of spacing `a/2` using block-spin or interpolation coarse-graining.
2. **Finite Fock sector refinement.** Define occupation coarse-graining compatible with number-preserving kernels.
3. **Finite Abelian gauge cutoff refinement.** Compare link cutoffs `S` and `S'` using flux truncation or flux binning, with boundary-center labels retained.

The safest worked example is the free one-particle case, because Paper 1 already controls the continuum tangential operator there. Gauge cutoff refinement is more interesting but riskier because of Gauss-sector centers and compact-rotor towers.

## Relationship To Later V2 Papers

Paper 3 on interacting comparison-map locality will need Paper 2's naturality theorem to say what inverse control means under refinement. Paper 4 on gauge-matter continuum benchmarks will need center-resolved projective systems. Paper 5 on operational covariance will need the cylinder-effect version of projective equivalence. Paper 6 on reconstruction will need projective state/effect systems before asking about continuum observables.

Thus Paper 2 is not optional infrastructure. It is the bridge from finite benchmark proofs to a possible continuum relativistic ISP.

## Recommended Immediate Work

Write Paper 2 as a theorem-framework paper, not as a physics-result paper. Its central deliverable should be the naturality of `Gamma`, `J`, and `E` under refinement, the asymptotic error-propagation theorem, and a clean distinction between projective covariance and Markov divisibility.

Recommended title:

`Projective Hypersurface Kernels and Foliation Compatibility in Relativistic ISP`

Consolidated draft:

`relativistic-isp-v2-paper2-projective-hypersurface-kernel-dynamics.md`

## Bottom Line

Paper 2 should define the continuum arena for relativistic ISP. Paper 1 proved a free curvature datum. Paper 2 must say what it means for that datum, and future interacting/gauge data, to be the same object across changing hypersurface regulators. The correct answer is exact or asymptotic projective compatibility of finite stochastic kernels, states, effects, comparison maps, and exchange defects, with explicit inverse-control bookkeeping. If that structure cannot be made nontrivial, then relativistic ISP has no clear continuum covariance language beyond fixed finite benchmarks.
