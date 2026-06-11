# Localized Controls, Detectors, and Operational Relativity in Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

*Finite-hypersurface stochastic instruments, foliation-compatible composition, and no-signaling with Bell-compatible full-circuit families*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 12 in the relativistic ISP sequence; phase-10 operational continuation after the dynamical Abelian gauge benchmark

## Abstract

After the exact free-model, Fock-space, and gauge benchmarks, the next honest phase in the relativistic ISP program is operational rather than merely kinematic. From the Barandes point of view, settings and detectors should not enter as verbal labels attached afterward to a terminal kernel. They should enter as localized physical operations supported in bounded spacetime regions between finite hypersurfaces.

This paper develops that operational phase at the strongest scope currently justified. It works on factorized finite hypersurface configuration spaces, defines localized stochastic controls and localized detector instruments, proves an abstract finite-dimensional realization theorem for every such localized instrument by a wing-supported ancilla, unitary evolution, and pointer partition, proves that disjoint operational layers commute and therefore compose foliation-compatibly across spacelike-separated regions, and proves a no-signaling theorem for local marginals under arbitrary localized control/readout families. At the same fixed finite-benchmark level it adjoins a neutral finite pointer ancilla to the Paper 11 matter-plus-link system and proves that gauge-invariant detector couplings supported on gauge-compatible mixed regions induce exact sector-preserving stochastic instruments after pointer readout. It also derives localized gauge-compatible setting-Hamiltonian pulses on the same finite matter-link benchmark and proves that they induce exact sector-preserving stochastic setting maps. It also proves an exact boundary-flux recursion on the fixed physical Gauss sector, showing that naive strict factorwise locality is not the correct generic microscopic target once Gauss law is imposed, and proves first partial boundary-flux-resolved locality theorems for boundary-flux-preserving detector and setting subclasses. It further proves a restricted microscopic Bell bridge theorem: for a concrete commuting benchmark family of those localized setting-plus-detector maps, the induced joint law already reproduces the same operational algebraic structure, foliation-order independence, and no-signaling form isolated earlier in the paper. It also proves a restricted universality theorem on a nontrivial commuting-projector subclass, including boundary-flux-preserving variants, at exact benchmark level, a restricted Bell-1976 screening-off theorem with explicit temporal-memory beables on that benchmark subclass, and a conditional Lorentz-covariant detector/control theorem at benchmark scope under an explicit sufficient-condition package extending Criterion A. It also gives a nonempty explicit benchmark class, a compact constructed two-setting/two-outcome worked law, and a restricted embedding theorem placing this benchmark class into a simple setting-dependent full-circuit family reproducing the same joint laws. It also identifies an equally important negative fact: if one tries to encode a Bell experiment as a single common source distribution followed only by local stochastic post-processing on a fixed product factorization, then the resulting setting family lies inside the local polytope, and the CHSH family already rules out any setting-independent Bell-factorizable reduced model of that kind. So Bell compatibility in ISP cannot live in that reduced operational model alone. Instead it must live, exactly as the companion process-entanglement paper already shows, in a family of setting-dependent full circuits in which the settings are active local Hamiltonians rather than passive basis labels. At that scope, phase 10 now closes the operational bookkeeping and first microscopic detector/setting benchmarks: localized controls and abstract detector instruments can be organized relativistically, local marginals are preserved, nontrivial gauge-compatible detector and setting Hamiltonian classes are available on the finite matter-link benchmark, restricted benchmark Bell bridge / universality / Bell-1976 / Lorentz-covariant detector-control theorems already hold with explicit nonemptiness, worked realization, and restricted full-circuit embedding, Bell-compatible nonfactorizable full-circuit families are allowed, and the precise boundary between those statements and the still-open full universality / full locality / full bridge burdens is made explicit. What is not yet claimed is full microscopic universality realizing every abstract localized instrument by such gauge-compatible region-supported couplings, a full boundary-flux/edge-mode-resolved locality theorem for arbitrary couplings, a full microscopic bridge from those couplings to Bell-setting full circuits, a full Bell-local-causality theorem in Bell's stronger 1976 sense for arbitrary couplings, or a constructive fully integrable Lorentz-covariant detector field theory beyond the present conditional benchmark theorem.

Scope note. The exact theorem-level content of this paper is the finite-hypersurface operational factorization, the localized control/readout instrument calculus, the abstract finite-dimensional realization theorem for localized instruments, the commutativity and foliation-compatible composition of spacelike-separated operational layers, the no-signaling theorem for local marginals, the theorem that any Bell family built only from a fixed common source plus local stochastic post-processing is Bell-local, first finite-benchmark detector and localized-setting Hamiltonian theorems on the Paper 11 matter-plus-link benchmark, an exact boundary-flux recursion on the physical Gauss sector showing why naive strict factorwise locality is not the correct generic microscopic target, partial boundary-flux-resolved locality theorems for boundary-flux-preserving detector and setting subclasses, a restricted microscopic Bell bridge theorem on a concrete commuting benchmark family, a restricted universality theorem on a commuting-projector benchmark subclass (including boundary-flux-preserving variants), a restricted Bell-1976 screening-off theorem with temporal-memory beables on that subclass, a conditional Lorentz-covariant detector/control theorem at benchmark scope under an explicit sufficient-condition package extending Criterion A, a nonempty explicit benchmark class with a constructed two-setting/two-outcome worked law, and a restricted embedding theorem from this benchmark class into a simple setting-dependent full-circuit family reproducing the same joint law. Bell-compatible nonfactorizable joint laws then enter through the already-established setting-dependent full-circuit family of the companion entanglement paper, whose CHSH value already excludes any setting-independent Bell-factorizable reduced model. Full microscopic universality for arbitrary abstract localized instruments, a full boundary-flux/edge-mode-resolved locality theorem, a full microscopic Bell-family bridge, a full Bell-1976 local-causality theorem for arbitrary couplings, and a constructive fully integrable Lorentz-covariant detector field theory remain open and are not overclaimed here.

## Introduction

The earlier relativistic ISP papers were deliberately structural. They first fixed the right primitive objects: exact finite-hypersurface kernels, localized deformation maps, exchange defects, and then the number-preserving, sector-changing, and gauge benchmarks that survive at the $ \Gamma $ level. But a relativistic theory is not operationally complete until settings and detectors are inserted into that same finite-hypersurface language.

There is a familiar temptation here, and from the present point of view it is the wrong one. One is tempted to treat a detector setting as a basis label and a detector outcome as an informal projection postulate attached to the end of the story. That is not good enough. In Barandes' framework, changing a basis is not a verbal redescription. It is a physical operation, implemented by a Hamiltonian or circuit. So phase 10 has to start from localized operational maps supported in bounded spacetime regions and ask what exact relativistic bookkeeping they satisfy.

At the same time, phase 10 has to avoid a second mistake: collapsing Bell experiments into a single pre-existing common source law followed only by local stochastic post-processing on a fixed product factorization. That reduced model is too weak. It preserves no-signaling, but it also lands inside the local polytope, and the CHSH family discussed below already rules out any setting-independent Bell-factorizable reduced model. So it cannot be where Bell-compatible nonfactorizable laws live. The right Bell lesson is instead the one already visible in the companion entanglement paper: the relevant objects are setting-dependent full circuits, with the settings implemented as active local operations. This reproduces the operational Bell laws at the stated circuit level; it is not by itself a proof of Bell's stronger local-causality condition for arbitrary microscopic couplings. The remaining Bell-1976 burden is therefore not a one-shot source-factorization problem; it is a local-beables-with-temporal-memory problem.

**Main results (informal).**

1. *Exact operational factorization.* Localized controls and detectors can be formulated as stochastic maps and stochastic instruments on factors of a finite hypersurface configuration space.
2. *Exact abstract finite realization theorem.* Every finite localized detector instrument already admits an ancilla / unitary / pointer realization on an enlarged finite factor space.
3. *Exact foliation-compatible composition.* Spacelike-separated operational layers commute, so any two foliations differing only by their order produce the same conditioned and unconditioned global law.
4. *Exact no-signaling theorem.* Local marginals are independent of remote settings and remote outcomes under arbitrary localized control/readout families.
5. *Exact Bell-locality of the reduced post-processing model.* A single common source distribution followed only by local stochastic post-processing yields a Bell-local family and therefore cannot by itself reproduce CHSH violation.
6. *Bell-compatible nonfactorizable full-circuit families remain allowed.* The companion entanglement paper's Bell-test circuits fit the operational perspective precisely because the settings are active local operations in the full circuit rather than mere post-processing labels.
7. *Exact finite-benchmark detector-Hamiltonian theorem.* Inside the finite matter-plus-link benchmark of Paper 11, gauge-compatible neutral pointer couplings already yield exact sector-preserving stochastic instruments after pointer readout.
8. *Exact finite-benchmark localized setting-Hamiltonian theorem.* On the same fixed matter-plus-link benchmark, gauge-compatible localized setting pulses on mixed regions already yield exact sector-preserving stochastic setting-control maps.
9. *Exact boundary-flux structure and partial fiberwise locality.* In the Paper 11 benchmark, Gauss law determines regional link fluxes recursively from local matter data only after boundary-flux data are supplied, and boundary-flux-preserving detector and setting couplings induce maps that decompose exactly fiberwise over those boundary-flux sectors.
10. *Exact restricted microscopic Bell bridge theorem.* A concrete commuting benchmark family of localized setting-plus-detector maps already reproduces the operational joint-law structure, foliation-order independence, and no-signaling algebra.
11. *Exact restricted universality theorem on a commuting-projector subclass.* A meaningful subclass of localized benchmark instruments—commuting-projector, optionally boundary-flux-preserving, and diagonal in natural commuting local charge/flux data—admits exact microscopic realization by gauge-compatible neutral-pointer couplings on the same finite matter-link benchmark.
12. *Exact restricted Bell-1976 screening-off theorem.* On the memory-labeled benchmark subclass, local-beables-with-temporal-memory screening-off holds exactly in Bell’s stronger 1976 sense.
13. *Conditional Lorentz-covariant detector/control theorem at benchmark scope.* Under an explicit sufficient-condition package (covariant layer transformation, spacelike-commuting layers, and adjacent-exchange foliation relation), benchmark detector-control experiments are foliation compatible and Lorentz-frame independent.
14. *Explicit nonempty benchmark class and worked realization.* The restricted assumptions are nonvacuous: Proposition 4H constructs a nonempty class, and Example 1 gives an explicit two-setting/two-outcome finite law computed end-to-end with no-signaling, screening-off, and Bell-local CHSH bound.
15. *Restricted embedding into a setting-dependent full-circuit family.* The memory-labeled benchmark class admits a simple setting-indexed full-circuit embedding whose observed outcome law matches the benchmark law exactly.

Strategic note. This paper is exact where the current stack already has exact operational algebra, an abstract finite realization theorem, first finite-benchmark detector and localized setting constructions, an exact boundary-flux obstruction to naive strict factorization, first partial boundary-flux-resolved locality theorems for preserving subclasses, restricted benchmark theorems for Bell bridge / universality / Bell-1976 screening-off, a conditional Lorentz-covariant detector/control benchmark theorem, and an explicit nonempty worked benchmark class together with a restricted full-circuit embedding theorem. It is deliberately noncommittal where full microscopic universality, full boundary-flux-resolved locality, full Bell-bridge/Bell-1976 theorems, or a constructive fully integrable Lorentz-covariant detector/control theory do not yet exist.

## Finite-hypersurface operational architecture

**Definition 1**

(Operational hypersurface factorization and source slab).

Let $ \Sigma_{\mathrm{src}} \prec \Sigma_{\mathrm{op}} $ be two finite hypersurfaces. Assume that on $ \Sigma_{\mathrm{op}} $ the relevant configuration space factorizes as
$$
\mathcal C_{\Sigma_{\mathrm{op}}}
\cong
\mathcal C_A \times \mathcal C_B \times \mathcal C_R,
$$
where $A$ and $B$ are the two operational wings and $R$ denotes the remaining degrees of freedom. Let
$$
\Gamma_{\mathrm{src}} : \mathbb R^{\mathcal C_{\Sigma_{\mathrm{src}}}} \to \mathbb R^{\mathcal C_{\Sigma_{\mathrm{op}}}}
$$
be the source slab kernel, and for an initial distribution $p_0$ define
$$
q_{ABR}:=\Gamma_{\mathrm{src}}\,p_0.
$$
We call $q_{ABR}$ the

*pre-setting source law*

on the operational hypersurface.

Remark.

The distribution $q_{ABR}$ is allowed to contain arbitrary correlations. At this stage it is just the output of a prior slab. The exact question is what later localized operations can and cannot do with it.

**Definition 2**

(Localized stochastic control).

For a setting value $x$, a localized control on wing $A$ is a column-stochastic map
$$
\Lambda_A^x : \mathbb R^{\mathcal C_A}\to \mathbb R^{\mathcal C_A}.
$$
Its global extension is
$$
\widehat\Lambda_A^x:=\Lambda_A^x\otimes I_B\otimes I_R.
$$
Similarly, a localized control on wing $B$ is a column-stochastic map
$$
\Lambda_B^y : \mathbb R^{\mathcal C_B}\to \mathbb R^{\mathcal C_B}
$$
with global extension
$$
\widehat\Lambda_B^y:=I_A\otimes \Lambda_B^y\otimes I_R.
$$

**Definition 3**

(Localized detector instrument).

For a setting value $x$, a localized detector instrument on wing $A$ is a finite family of nonnegative matrices
$$
\{\mathcal J_A^{a|x}\}_a,
$$
acting on $ \mathbb R^{\mathcal C_A} $, such that
$$
\sum_a \mathcal J_A^{a|x}=\Lambda_A^x
$$
is column-stochastic. Its global extension is
$$
\widehat{\mathcal J}_A^{a|x}:=\mathcal J_A^{a|x}\otimes I_B\otimes I_R.
$$
Likewise, for wing $B$ one has
$$
\{\mathcal J_B^{b|y}\}_b,
\qquad
\sum_b\mathcal J_B^{b|y}=\Lambda_B^y,
$$
with global extension
$$
\widehat{\mathcal J}_B^{b|y}:=I_A\otimes \mathcal J_B^{b|y}\otimes I_R.
$$

**Theorem A**

(Abstract finite realization of a localized stochastic instrument).

Fix a setting value $x$ and a localized detector instrument
$$
\{\mathcal J_A^{a|x}\}_a
$$
of Definition 3 on the finite factor $ \mathbb R^{\mathcal C_A} $. Then there exist:

1. a finite ancilla space
  $$
  \mathcal D_A^x
  \cong
  \mathbb C^{\Xi_A^{\mathrm{abs},x}},
  \qquad
  \Xi_A^{\mathrm{abs},x}
  =
  \bigsqcup_a \Xi_{A,a}^{\mathrm{abs},x},
  $$
  with each $ \Xi_{A,a}^{\mathrm{abs},x} $ in bijection with $ \mathcal C_A $;
2. a distinguished unit ready state $|0_A^x\rangle\in\mathcal D_A^x$; and
3. a unitary operator
  $$
  U_A^x
  \text{ on }
  \mathbb C^{\mathcal C_A}\otimes\mathcal D_A^x
  $$
  such that for every output configuration $ \alpha'\in\mathcal C_A $, input configuration $ \alpha\in\mathcal C_A $, and outcome label $a$,
  $$
  [\mathcal J_A^{a|x}]_{\alpha',\alpha}
  =
  \sum_{\xi\in\Xi_{A,a}^{\mathrm{abs},x}}
  \Bigl|
  \langle \alpha',\xi|U_A^x|\alpha,0_A^x\rangle
  \Bigr|^2.
  $$

Consequently the unconditioned map
$$
\Lambda_A^x=\sum_a \mathcal J_A^{a|x}
$$
is obtained by reading the ancilla with the coarse-grained outcome partition
$$
\Xi_A^{\mathrm{abs},x}
=
\bigsqcup_a \Xi_{A,a}^{\mathrm{abs},x}.
$$
Equivalently, every finite localized detector instrument on wing $A$ admits an abstract ancilla / unitary / pointer realization after adjoining a finite detector space to that wing alone. The same statement holds for wing $B$ and setting $y$.

Proof.

For each outcome $a$, choose a copy $ \Xi_{A,a}^{\mathrm{abs},x}\cong\mathcal C_A $ and write its orthonormal basis vectors as
$$
|a,\alpha\rangle,
\qquad
\alpha\in\mathcal C_A.
$$
Define a linear map
$$
V_A^x:\mathbb C^{\mathcal C_A}\to \mathbb C^{\mathcal C_A}\otimes\mathcal D_A^x
$$
on the configuration basis by
$$
V_A^x|\alpha\rangle
:=
\sum_{a,\alpha'}
\sqrt{[\mathcal J_A^{a|x}]_{\alpha',\alpha}}\,
|\alpha'\rangle\otimes|a,\alpha\rangle.
$$
Then for any $ \alpha,\beta\in\mathcal C_A $,
$$
\langle \beta| (V_A^x)^\dagger V_A^x |\alpha\rangle
=
\delta_{\alpha\beta}
\sum_{a,\alpha'}
[\mathcal J_A^{a|x}]_{\alpha',\alpha}
=
\delta_{\alpha\beta}
\sum_{\alpha'}
[\Lambda_A^x]_{\alpha',\alpha}
=
\delta_{\alpha\beta},
$$
because $ \Lambda_A^x $ is column-stochastic. Hence $V_A^x$ is an isometry.

Identify $ \mathbb C^{\mathcal C_A} $ with the ready-state subspace
$$
\mathbb C^{\mathcal C_A}\otimes |0_A^x\rangle
\subset
\mathbb C^{\mathcal C_A}\otimes\mathcal D_A^x.
$$
Since all spaces are finite dimensional, the isometry
$$
|\alpha\rangle\otimes|0_A^x\rangle\longmapsto V_A^x|\alpha\rangle
$$
extends to a unitary $U_A^x$ on the full tensor-product space. On the ready-state subspace one then has
$$
\langle \alpha',a,\beta|U_A^x|\alpha,0_A^x\rangle
=
\sqrt{[\mathcal J_A^{a|x}]_{\alpha',\alpha}}\,
\delta_{\beta,\alpha}.
$$
Summing over the copy label $ \beta $ inside the outcome block $ \Xi_{A,a}^{\mathrm{abs},x} $ yields exactly
$$
[\mathcal J_A^{a|x}]_{\alpha',\alpha}
=
\sum_{\xi\in\Xi_{A,a}^{\mathrm{abs},x}}
\Bigl|
\langle \alpha',\xi|U_A^x|\alpha,0_A^x\rangle
\Bigr|^2.
$$
The unconditioned map follows by summing over $a$. Finally, every finite-dimensional unitary has a self-adjoint logarithm, so for any fixed interaction time $ \tau>0 $ one may also write
$$
U_A^x=e^{-i\tau H_A^x}
$$
for some self-adjoint $H_A^x$. The statement for wing $B$ is identical.

$ \square $

Remark.

Theorem A is intentionally abstract. The ancilla may depend on the chosen setting and instrument, and no claim is made here about gauge compatibility, mixed-region support inside the matter-link benchmark, or reduction to a strict physical-sector tensor factorization after Gauss law is imposed. Section VI addresses a different and stronger question: realization by gauge-compatible detector Hamiltonians inside the explicit Paper 11 benchmark.

**Definition 4**

(Operational joint law).

Given the pre-setting source law $q_{ABR}$ and localized instruments as above, define
$$
p(a,b|x,y)
:=
\mathbf 1^\top
\widehat{\mathcal J}_A^{a|x}
\widehat{\mathcal J}_B^{b|y}
\,q_{ABR},
$$
where $ \mathbf 1^\top=\mathbf 1_A^\top\otimes \mathbf 1_B^\top\otimes \mathbf 1_R^\top $. By Proposition 1 below, the order of the two instrument factors does not matter.

## Exact operational locality on finite hypersurfaces

**Proposition 1**

(Commutativity of disjoint localized instruments).

For every outcomes $a,b$ and settings $x,y$,
$$
\widehat{\mathcal J}_A^{a|x}\widehat{\mathcal J}_B^{b|y}
=
\mathcal J_A^{a|x}\otimes \mathcal J_B^{b|y}\otimes I_R
=
\widehat{\mathcal J}_B^{b|y}\widehat{\mathcal J}_A^{a|x}.
$$
The same statement holds for the unconditioned controls $ \widehat\Lambda_A^x $ and $ \widehat\Lambda_B^y $.

Proof.

The two maps act on distinct tensor factors of
$$
\mathbb R^{\mathcal C_A}\otimes\mathbb R^{\mathcal C_B}\otimes\mathbb R^{\mathcal C_R}.
$$
Hence their tensor-product expressions multiply independently and commute.

$ \square $

**Theorem 1**

(Foliation-compatible composition for spacelike-separated operational layers).

Let
$$
\{\widehat{\mathcal J}_{O_k}^{\alpha_k}\}_{k=1}^m
$$
be localized operational maps supported on pairwise disjoint hypersurface factors. Then for every permutation $ \pi $ of $ \{1,\dots,m\} $,
$$
\widehat{\mathcal J}_{O_{\pi(1)}}^{\alpha_{\pi(1)}}\cdots
\widehat{\mathcal J}_{O_{\pi(m)}}^{\alpha_{\pi(m)}}

=
\bigotimes_{k=1}^m \mathcal J_{O_k}^{\alpha_k}\otimes I_{\mathrm{rest}}.
$$
Consequently any two foliations that differ only by the order in which they cross these spacelike-separated operational regions induce the same conditioned and unconditioned global law.

Proof.

By Proposition 1, any adjacent pair of disjoint localized operational maps commute. Any permutation can be reached by a sequence of adjacent transpositions. Hence the ordered product is permutation independent and equals the common tensor-product expression. The foliation statement is exactly the spacetime reading of this algebraic fact.

$ \square $

Remark.

This is the right minimal relativistic statement at the present operational level. It is not a full Lorentz-covariant field-theory theorem. It is the exact finite-hypersurface statement that foliation order across spacelike-separated localized operations is operationally irrelevant. A complete Lorentz-covariant detector theorem would have to extend Criterion A of the architecture paper from abstract localized controls/readouts to honest detector-supported operations in the matter-link benchmark, while also importing the still-open Paper 11 operator-theoretic burdens rather than bypassing them.

**Theorem 2**

(No-signaling for localized stochastic instruments).

For the operational joint law of Definition 4 one has
$$
p_A(a|x,y):=\sum_b p(a,b|x,y)=p_A(a|x),
$$
independent of $y$, and symmetrically
$$
p_B(b|x,y):=\sum_a p(a,b|x,y)=p_B(b|y),
$$
independent of $x$.

Proof.

Using Proposition 1,
$$
\sum_b p(a,b|x,y)
=
\mathbf 1^\top
\widehat{\mathcal J}_A^{a|x}
\Bigl(\sum_b \widehat{\mathcal J}_B^{b|y}\Bigr)
q_{ABR}
=
\mathbf 1^\top
(\mathcal J_A^{a|x}\otimes \Lambda_B^y\otimes I_R)\,q_{ABR}.
$$
Now
$$
\mathbf 1^\top
(\mathcal J_A^{a|x}\otimes \Lambda_B^y\otimes I_R)
=
(\mathbf 1_A^\top \mathcal J_A^{a|x})\otimes(\mathbf 1_B^\top \Lambda_B^y)\otimes \mathbf 1_R^\top.
$$
Because $ \Lambda_B^y $ is column-stochastic,
$$
\mathbf 1_B^\top \Lambda_B^y=\mathbf 1_B^\top.
$$
Therefore
$$
\sum_b p(a,b|x,y)
=
\mathbf 1^\top
(\mathcal J_A^{a|x}\otimes I_B\otimes I_R)\,q_{ABR},
$$
which is independent of $y$. The statement for Bob is identical by symmetry.

$ \square $

**Corollary 1**

(Local post-processing preserves no-signaling).

Any further local stochastic map applied to Alice's detector outcomes after Theorem 2 cannot introduce dependence on Bob's setting, and vice versa.

Proof.

Post-composition with a local stochastic map is a linear averaging of the already setting-independent local marginal. Linearity cannot reintroduce dependence on a remote setting.

$ \square $

## The fixed-source local-postprocessing model is Bell-local

Theorems 1 and 2 are exact and useful, but by themselves they do not yet identify where Bell-compatible joint laws live. In fact, a second exact theorem shows that if one insists on encoding the entire Bell experiment as a single common source distribution followed only by local stochastic post-processing on a fixed product factorization, then one has already reduced oneself to the local polytope.

**Proposition 2**

(Bell-locality of the fixed-source local-postprocessing model).

Let $q_{ABR}$ be a fixed source distribution on
$$
\mathcal C_A\times \mathcal C_B\times \mathcal C_R.
$$
Let
$$
\{\mathcal J_A^{a|x}\}_{a,x},
\qquad
\{\mathcal J_B^{b|y}\}_{b,y}
$$
be localized detector instruments in the sense of Definition 3. Then the family
$$
p(a,b|x,y)
=
\mathbf 1^\top
\widehat{\mathcal J}_A^{a|x}
\widehat{\mathcal J}_B^{b|y}
q_{ABR}
$$
admits the Bell-local decomposition
$$
p(a,b|x,y)
=
\sum_{\lambda}\mu(\lambda)\,
A(a|x,\lambda)\,
B(b|y,\lambda),
$$
with $ \mu(\lambda)\ge 0 $, $ \sum_\lambda \mu(\lambda)=1 $, and local response functions stochastic in $a$ and $b$. Hence this family lies inside the local polytope and obeys every Bell inequality.

Proof.

Write
$$
\lambda:=(\alpha,\beta,\rho)\in \mathcal C_A\times \mathcal C_B\times \mathcal C_R
$$
and set
$$
\mu(\lambda):=q_{ABR}(\alpha,\beta,\rho).
$$
Define the local response functions by
$$
A(a|x,\alpha)
:=
\sum_{\alpha'}[\mathcal J_A^{a|x}]_{\alpha',\alpha},
\qquad
B(b|y,\beta)
:=
\sum_{\beta'}[\mathcal J_B^{b|y}]_{\beta',\beta}.
$$
Since the instrument sums are column-stochastic,
$$
\sum_a A(a|x,\alpha)=1,
\qquad
\sum_b B(b|y,\beta)=1.
$$
Expanding the global expression for $p(a,b|x,y)$ and summing over final local states gives
$$
p(a,b|x,y)
=
\sum_{\alpha,\beta,\rho}
q_{ABR}(\alpha,\beta,\rho)\,
A(a|x,\alpha)\,
B(b|y,\beta),
$$
which is exactly the displayed Bell-local form.

$ \square $

Remark.

This is the precise operational warning. No-signaling is cheap: the fixed-source local-postprocessing model satisfies it automatically. Bell compatibility is harder: this reduced model cannot supply it. Section V sharpens the point further, because the CHSH family already rules out any setting-independent Bell-factorizable reduced model.

## Bell-compatible nonfactorizable full-circuit families

The correct Bell lesson in ISP is therefore not that localized operations fail. It is that the wrong reduced model fails. In the ISP framework, settings are active local Hamiltonians, so the relevant operational objects are setting-dependent *full circuits*, not one common source distribution followed only by local stochastic post-processing on a fixed product factorization.

**Definition 5**

(Setting-dependent full-circuit family).

An operational Bell family in ISP is a setting-indexed collection of full-circuit time-evolution operators
$$
\Theta_{\mathrm{tot}}^{(xy)}
$$
with corresponding observable transition matrices
$$
\Gamma_{\mathrm{tot}}^{(xy)}:=\bigl|\Theta_{\mathrm{tot}}^{(xy)}\bigr|^2,
$$
where the setting dependence enters through localized active operations supported in the two wings. The observable joint outcome law is then
$$
p(a,b|x,y)=\Gamma_{\mathrm{tot}}^{(xy)}(ab|j_0)
$$
for the chosen initial configuration $j_0$.

**Theorem 3**

(Bell-compatible nonfactorizable joint laws are operationally allowed in ISP).

There exists a setting-dependent full-circuit family in the sense of Definition 5 for which
$$
|S_{\mathrm{CHSH}}|=2\sqrt{2},
$$
while the local marginals remain independent of the remote setting. One explicit example is the Bell-test family of the companion process-entanglement paper:
$$
\Theta^{(xy)}
=
\bigl(R_A^{(x)}\otimes R_B^{(y)}\bigr)\cdot U_{\mathrm{Bell}},
\qquad
\Gamma^{(xy)}=\bigl|\Theta^{(xy)}\bigr|^2,
$$
with
$$
U_{\mathrm{Bell}}=\mathrm{CNOT}\cdot(H\otimes I),
$$
and the four local settings
$$
R_A^{(0)}=I,\quad
R_A^{(1)}=R_y(-\tfrac{\pi}{2}),\quad
R_B^{(0)}=R_y(-\tfrac{\pi}{4}),\quad
R_B^{(1)}=R_y(\tfrac{\pi}{4}).
$$

Proof.

The companion process-entanglement paper proves exactly that this family satisfies
$$
|S_{\mathrm{CHSH}}|=2\sqrt{2}
$$
and that each fixed setting has nonfactorizable process structure. Its explicit probability table also shows that the single-wing marginals are
$$
p_A(0|x,y)=p_B(0|x,y)=\frac12
$$
for all $x,y$, hence independent of the remote setting. Therefore ISP permits Bell-compatible nonfactorizable joint laws at the full-circuit level.

$ \square $

**Corollary 2**

(Why Proposition 2 and Theorem 3 are compatible).

The Bell family of Theorem 3 cannot be reduced to the fixed-source local-postprocessing form of Proposition 2. More generally, its CHSH value rules out every setting-independent Bell-factorizable reduced model. Therefore Bell compatibility in ISP requires the setting dependence to live in the full circuit itself rather than only in a local stochastic post-processing layer appended to a single common source distribution.

Proof.

If the Bell family of Theorem 3 admitted the reduced form of Proposition 2, it would lie inside the local polytope and obey every Bell inequality. But Theorem 3 gives
$$
|S_{\mathrm{CHSH}}|=2\sqrt{2}>2.
$$
So no such reduction exists. The same CHSH contradiction excludes any setting-independent Bell-factorizable model of the usual Bell-local form
$$
p(a,b|x,y)=\sum_{\lambda}\mu(\lambda)\,A(a|x,\lambda)\,B(b|y,\lambda)
$$
with $\mu$ independent of $(x,y)$.

$ \square $

Remark.

This is exactly the Barandes-style operational moral. One should not talk as if a measurement setting were merely a basis label attached to a terminal kernel. The setting is part of the physical circuit. Once that is respected, Bell compatibility and no-signaling no longer pull in opposite directions. But Bell's stronger 1976 question does not disappear; it changes form. The remaining burden is to say what the local beables are along the setting-dependent circuit, what temporally propagated memory they carry between the relevant spacetime regions, and whether Bell's stronger screening-off condition can hold at that beable level.

## Microscopic detector Hamiltonians on the finite matter-plus-link benchmark

The operational calculus above was intentionally abstract. Theorem A already shows that every finite localized instrument on the factorized operational spaces admits an abstract ancilla / unitary / pointer realization. Paper 11 now supplies a finite gauge-compatible microscopic benchmark. So the next honest question is not yet whether every abstract instrument admits a local detector-Hamiltonian realization on that benchmark. That would be too strong. The right first question is narrower: can one already write a nontrivial exact detector Hamiltonian inside the finite matter-plus-link benchmark and read off a stochastic instrument from it without leaving the proved scope? The answer is yes.

**Definition 6**

(Neutral finite pointer ancilla and outcome partition).

Fix a gauge-compatible mixed region $R$ of Paper 11 and a compatible Gauss sector $ \mathbf g $. Let
$$
\mathcal D_R\cong \mathbb C^{d_R}
$$
be a finite detector pointer space with orthonormal basis
$$
\{|\xi\rangle:\xi\in \Xi_R^{\mathrm{det}}\},
$$
a distinguished ready state $|0_R\rangle$, and an outcome partition
$$
\Xi_R^{\mathrm{det}}
=
\bigsqcup_{a\in \mathcal A_R}\Xi_{R,a}^{\mathrm{det}}.
$$
Set
$$
\mathcal K_{L,S;R}^{(\mathbf g,\mathrm{det})}
:=
\mathcal K_{L,S}^{(\mathbf g)}\otimes \mathcal D_R.
$$
The detector is called

*neutral*

if the extended Gauss generators are
$$
\widehat G_n^{\mathrm{det}}
:=
\widehat G_n\otimes I_{\mathcal D_R}.
$$

**Definition 7**

(Gauge-compatible detector Hamiltonian supported in a mixed region).

A detector Hamiltonian supported in $R$ is a self-adjoint operator of the form
$$
\widehat H_{R,\mathrm{det}}^{(S)}
:=
\widehat H_{\mathrm{dyn}}^{(S)}\otimes I_{\mathcal D_R}
+
I\otimes \widehat H_{\mathcal D_R}
+
\widehat W_R^{(S)},
$$
where
$$
\widehat W_R^{(S)}
=
\sum_{\alpha=1}^{M_R}
\widehat O_{R,\alpha}^{(S)}\otimes \widehat M_\alpha,
$$
each $ \widehat M_\alpha $ is self-adjoint on $ \mathcal D_R $, and each
$$
\widehat O_{R,\alpha}^{(S)}
$$
is a gauge-invariant matter-link operator generated by the gauge-compatible local mixed cells of Paper 11 contained in $R$. Equivalently, the additional detector coupling acts only through the mixed site-link degrees of freedom of $R$ and commutes with every $ \widehat G_n $.

Remark.

Simple admissible couplings already include local charge, electric-flux, and mixed hopping-density readouts such as
$$
\widehat N_n\otimes \widehat P,
\qquad
\widehat E_{n+1/2}\otimes \widehat P,
\qquad
\sum_s
\Bigl(
c_{n+1,\bar s}^\dagger \widehat U_{n+1/2} c_{n,s}
+
c_{n,s}^\dagger \widehat U_{n+1/2}^\dagger c_{n+1,\bar s}
\Bigr)\otimes \widehat P,
$$
with $ \widehat P $ any self-adjoint pointer generator. These are already gauge invariant and supported on the appropriate mixed cells.

**Proposition 3**

(Exact Gauss-sector preservation of the detector coupling).

For every site $n$,
$$
[\widehat G_n^{\mathrm{det}},\widehat H_{R,\mathrm{det}}^{(S)}]=0.
$$
Consequently the detector-coupled evolution preserves each compatible Gauss sector.

Proof.

By Paper 11, $ \widehat H_{\mathrm{dyn}}^{(S)} $ commutes with every $ \widehat G_n $. The detector Hamiltonian $ \widehat H_{\mathcal D_R} $ acts only on the neutral pointer factor and therefore also commutes with every $ \widehat G_n^{\mathrm{det}} $. Finally, each $ \widehat O_{R,\alpha}^{(S)} $ is gauge invariant by Definition 7, so every term in $ \widehat W_R^{(S)} $ commutes with every $ \widehat G_n^{\mathrm{det}} $. Summing the terms yields the claim.

$ \square $

**Proposition 3A**

(Exact boundary-flux recursion on the physical Gauss sector).

Fix the background charges
$$
(\rho_n^{\mathrm{bg}})_n
$$
and the distinguished physical Gauss datum
$$
\mathbf g_{\mathrm{phys}}=(g_n^{\mathrm{phys}})_n
$$
of the Paper 11 benchmark, and let
$$
\omega=(X,\mathbf m)
$$
be a matter-link basis configuration in the corresponding physical sector. Write
$$
N_n(X):=\sum_s \mathbf 1_{(n,s)\in X}
$$
for the site occupation number and
$$
\mathbf m=(m_{1/2},m_{3/2},\dots,m_{L-1/2})
$$
for the link-flux data. Then for every site $n$,
$$
m_{n+1/2}
=
m_{n-1/2}-N_n(X)+\rho_n^{\mathrm{bg}}-g_n^{\mathrm{phys}}.
$$
Hence for any connected site interval
$$
I=\{n_-,n_-+1,\dots,n_+\}
$$
and any $n\in I$,
$$
m_{n+1/2}
=
m_{n_- -1/2}
-\sum_{j=n_-}^{n}\bigl(N_j(X)-\rho_j^{\mathrm{bg}}+g_j^{\mathrm{phys}}\bigr),
$$
and therefore
$$
m_{n_- -1/2}-m_{n_+ +1/2}
=
\sum_{j=n_-}^{n_+}\bigl(N_j(X)-\rho_j^{\mathrm{bg}}+g_j^{\mathrm{phys}}\bigr).
$$
Consequently the interior link-flux profile on $I$ is determined by the matter occupation data on $I$ only after one supplies one boundary-flux seed. In particular, the physical-sector configuration space is naturally fibered over shared boundary electric-flux data rather than generically factorizing as an unconstrained product of independent regional configuration spaces.

Proof.

Because $\omega$ lies in the physical Gauss sector, the Gauss-law eigenvalue equation of Paper 11 holds at every site:
$$
m_{n-1/2}-m_{n+1/2}-N_n(X)+\rho_n^{\mathrm{bg}}
=
g_n^{\mathrm{phys}}.
$$
Rearranging gives the one-step recursion
$$
m_{n+1/2}
=
m_{n-1/2}-N_n(X)+\rho_n^{\mathrm{bg}}-g_n^{\mathrm{phys}}.
$$
Iterating from the left boundary link of $I$ proves the second displayed formula, and setting $n=n_+$ yields the boundary-difference relation.

The final sentence is then immediate. Once the matter occupation data on $I$ and one boundary flux seed, say $m_{n_- -1/2}$, are fixed, every interior link flux is fixed recursively. Conversely, whenever two different seed values are both admissible under the finite link cutoff, the resulting recursive link profiles differ while the site occupations remain the same. So the regional physical data are not generically independent product data; they are organized into fibers labeled by shared boundary flux.

$ \square $

Remark.

Proposition 3A is the exact structural reason the microscopic locality problem differs from the abstract factorized locality of Sections II and III. On the physical Gauss sector, the right target is not a naive strict factorwise-locality theorem on an unconstrained product space. It is, at best, a boundary-flux/edge-mode-resolved locality theorem formulated fiberwise after conditioning on the shared interface flux data.

**Definition 8**

(Detector instrument induced by pointer readout).

Fix a compatible Gauss sector $ \mathbf g $ and an interaction time $ \tau $. Let
$$
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)
:=
e^{-i\tau \widehat H_{R,\mathrm{det}}^{(S,\mathbf g)}}.
$$
For each detector outcome $a\in \mathcal A_R$, define the matrix on the matter-link sector basis $ \Omega_{L,S}^{(\mathbf g)} $ by
$$
\bigl[\mathcal J_{R,\mathbf g}^{a,(S)}(\tau)\bigr]_{\omega',\omega}
:=
\sum_{\xi\in \Xi_{R,a}^{\mathrm{det}}}
\Bigl|
\langle \omega',\xi |
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)
|
\omega,0_R\rangle
\Bigr|^2.
$$
Set
$$
\Lambda_{R,\mathbf g}^{(S)}(\tau)
:=
\sum_a \mathcal J_{R,\mathbf g}^{a,(S)}(\tau).
$$

**Definition 8A**

(Boundary-flux fibers for a connected detector region).

Assume that the site set of the gauge-compatible mixed detector region is a connected interval
$$
V_R=\{n_-,n_-+1,\dots,n_+\}.
$$
On the physical-sector basis
$$
\Omega_{L,S}^{(\mathbf g_{\mathrm{phys}})},
$$
define the boundary-flux label map
$$
\partial\Phi_R(\omega)
:=
\bigl(m_{n_- -1/2},m_{n_+ +1/2}\bigr),
\qquad
\omega=(X,\mathbf m).
$$
For a boundary-flux label
$$
\lambda=(\lambda_-,\lambda_+)\in\{-S,-S+1,\dots,S\}^2,
$$
set
$$
\Omega_{R,\lambda}^{(\mathbf g_{\mathrm{phys}})}
:=
\{\omega\in\Omega_{L,S}^{(\mathbf g_{\mathrm{phys}})}:\partial\Phi_R(\omega)=\lambda\},
$$
and call $\lambda$

*admissible*

if this fiber is nonempty. Let
$$
P_{R,\lambda}^{\partial}
:=
\sum_{\omega\in\Omega_{R,\lambda}^{(\mathbf g_{\mathrm{phys}})}}|\omega\rangle\langle\omega|
$$
be the corresponding projector on the physical-sector matter-link space. On the detector-extended space set
$$
\widehat P_{R,\lambda}^{\partial}
:=
P_{R,\lambda}^{\partial}\otimes I_{\mathcal D_R}.
$$
The detector Hamiltonian is called

*boundary-flux preserving*

on the physical sector if
$$
[\widehat P_{R,\lambda}^{\partial},\widehat H_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}]=0
$$
for every admissible label $\lambda$.

**Theorem 4**

(Exact finite-benchmark detector instrument from gauge-compatible pointer coupling).

Fix $L$, $S$, a gauge-compatible mixed region $R$, a compatible Gauss sector $ \mathbf g $, and an interaction time $ \tau $. Then the family
$$
\{\mathcal J_{R,\mathbf g}^{a,(S)}(\tau)\}_{a\in \mathcal A_R}
$$
is an exact finite stochastic instrument on the chosen Gauss sector. More precisely:

1. every matrix entry of every $ \mathcal J_{R,\mathbf g}^{a,(S)}(\tau) $ is nonnegative;
2. $ \Lambda_{R,\mathbf g}^{(S)}(\tau)=\sum_a \mathcal J_{R,\mathbf g}^{a,(S)}(\tau) $ is column-stochastic;
3. no off-sector transitions appear, because the detector-coupled evolution is block diagonal in the Gauss decomposition; and
4. the instrument is produced by a genuinely gauge-compatible additional Hamiltonian term $ \widehat W_R^{(S)} $ supported in the mixed region $R$.

Proof.

Nonnegativity is immediate from the absolute-square definition. By Proposition 3, the unitary $ \widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau) $ is the sector block of a Gauss-sector-preserving evolution, so the construction never leaves the chosen sector. For each incoming configuration $ \omega\in\Omega_{L,S}^{(\mathbf g)} $,
$$
\sum_a \sum_{\omega'}
\bigl[\mathcal J_{R,\mathbf g}^{a,(S)}(\tau)\bigr]_{\omega',\omega}
=
\sum_{\omega'}\sum_{\xi\in \Xi_R^{\mathrm{det}}}
\Bigl|
\langle \omega',\xi |
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)
|
\omega,0_R\rangle
\Bigr|^2.
$$
The set
$$
\{|\omega',\xi\rangle\}_{\omega',\xi}
$$
is an orthonormal basis of the sector-plus-pointer space, so by unitarity the last expression equals
$$
\langle \omega,0_R|
\bigl(\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)\bigr)^\dagger
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)
|\omega,0_R\rangle
=
1.
$$
Hence $ \Lambda_{R,\mathbf g}^{(S)}(\tau) $ is column-stochastic. The final item is exactly Definition 7.

$ \square $

**Theorem 4A**

(Partial boundary-flux-resolved locality for boundary-flux-preserving detector couplings).

Assume that the detector region $R$ has connected site set
$$
V_R=\{n_-,n_-+1,\dots,n_+\}
$$
and fix the physical Gauss sector $ \mathbf g_{\mathrm{phys}} $. If the detector Hamiltonian is boundary-flux preserving in the sense of Definition 8A, then:

1. the detector-coupled unitary
  $$
  \widehat U_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}(\tau)
  $$
  preserves each boundary-flux fiber;
2. for every detector outcome $a\in\mathcal A_R$, the matrix
  $$
  \mathcal J_{R,\mathbf g_{\mathrm{phys}}}^{a,(S)}(\tau)
  $$
  is block diagonal with respect to the decomposition
  $$
  \Omega_{L,S}^{(\mathbf g_{\mathrm{phys}})}
  =
  \bigsqcup_{\lambda\ \mathrm{admissible}}
  \Omega_{R,\lambda}^{(\mathbf g_{\mathrm{phys}})},
  $$
  and the same holds for
  $$
  \Lambda_{R,\mathbf g_{\mathrm{phys}}}^{(S)}(\tau).
  $$
  Equivalently, no instrument entry connects two configurations with different boundary-flux labels; and
3. by Proposition 3A, the remaining microscopic locality problem for this class of detector couplings is therefore reduced fiberwise to the fixed-$\lambda$ sectors.

In this exact sense, boundary-flux-preserving detector couplings already satisfy a partial boundary-flux-resolved locality theorem on the physical sector.

Proof.

If
$$
[\widehat P_{R,\lambda}^{\partial},\widehat H_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}]=0
$$
for every admissible $\lambda$, then by functional calculus the same projectors commute with
$$
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}(\tau)
=
e^{-i\tau \widehat H_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}}.
$$
Hence for two different admissible labels $\lambda\neq\lambda'$ one has
$$
\widehat P_{R,\lambda'}^{\partial}
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}(\tau)
\widehat P_{R,\lambda}^{\partial}
=
0.
$$
Therefore, if
$$
\partial\Phi_R(\omega)=\lambda,
\qquad
\partial\Phi_R(\omega')=\lambda',
\qquad
\lambda\neq\lambda',
$$
then for every pointer basis state $|\xi\rangle$,
$$
\langle \omega',\xi |
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}(\tau)
|
\omega,0_R\rangle
=
0.
$$
Summing absolute squares over the outcome partition in Definition 8 therefore gives
$$
\bigl[\mathcal J_{R,\mathbf g_{\mathrm{phys}}}^{a,(S)}(\tau)\bigr]_{\omega',\omega}=0
$$
whenever $\partial\Phi_R(\omega')\neq\partial\Phi_R(\omega)$. This proves the stated block diagonality for each conditioned instrument and for the unconditioned map. The final clause is the structural interpretation of Proposition 3A: once the shared boundary-flux label is fixed, the remaining locality question is a fiberwise one rather than a naive unconstrained product one.

$ \square $

**Corollary 3**

(Concrete cut-flux-diagonal preserving subclass).

In the setting of Theorem 4A, assume in addition that the physical-sector matter-link block and every detector-coupling term are diagonal with respect to the two cut-boundary electric-flux operators, in the sense that
$$
[\widehat H_{\mathrm{dyn}}^{(S,\mathbf g_{\mathrm{phys}})},\widehat E_{n_- -1/2}]
=
[\widehat H_{\mathrm{dyn}}^{(S,\mathbf g_{\mathrm{phys}})},\widehat E_{n_+ +1/2}]
=
0
$$
and
$$
[\widehat O_{R,\alpha}^{(S)},\widehat E_{n_- -1/2}]
=
[\widehat O_{R,\alpha}^{(S)},\widehat E_{n_+ +1/2}]
=
0
$$
for every $ \alpha $. Then
$$
\widehat H_{R,\mathrm{det}}^{(S,\mathbf g_{\mathrm{phys}})}
$$
is boundary-flux preserving, so the conclusion of Theorem 4A applies.

In particular, this covers the explicit syntactic subclass in which every term touching the two cut links is a function only of the corresponding electric-flux operators, while the remaining detector couplings are built from gauge-invariant terms of the following types:

1. site-occupation readouts
  $$
  \widehat N_n\otimes\widehat P,
  \qquad
  n\in V_R;
  $$
2. interior electric-flux readouts
  $$
  \widehat E_{j+1/2}\otimes\widehat P,
  \qquad
  n_-\le j\le n_+-1;
  $$
3. mixed hopping-density readouts
  $$
  \sum_s
  \Bigl(
  c_{j+1,\bar s}^\dagger \widehat U_{j+1/2} c_{j,s}
  +
  c_{j,s}^\dagger \widehat U_{j+1/2}^\dagger c_{j+1,\bar s}
  \Bigr)\otimes\widehat P
  $$
  supported only on links
  $$
  j+\tfrac12\neq n_- -\tfrac12,\ n_+ +\tfrac12.
  $$

Proof.

By Definition 8A, the projectors
$$
\widehat P_{R,\lambda}^{\partial}
$$
are the joint spectral projectors of the two commuting cut-boundary electric-flux operators
$$
\widehat E_{n_- -1/2}\otimes I_{\mathcal D_R},
\qquad
\widehat E_{n_+ +1/2}\otimes I_{\mathcal D_R}
$$
restricted to the physical sector. Hence commutation with both cut-boundary electric-flux operators implies commutation with every
$$
\widehat P_{R,\lambda}^{\partial}.
$$
The detector pointer Hamiltonian acts only on $\mathcal D_R$ and therefore also commutes with these projectors. So the full detector Hamiltonian is boundary-flux preserving, and Theorem 4A applies.

For the explicit subclass, site-occupation terms act only on matter sites, interior electric-flux terms act on links different from the two cut links, and the displayed mixed hopping-density terms act only on interior hopping cells. Therefore each such term commutes manifestly with both cut-boundary electric-flux operators.

$ \square $

Remark.

Corollary 3 is the first concrete benchmark subclass underlying Theorem 4A. The excluded local terms are exactly the hopping cells on the two cut links
$$
n_- -\tfrac12,
\qquad
n_+ +\tfrac12,
$$
because those are the first gauge-invariant terms that can change the shared boundary-flux label seen by the physical-sector fibers.

**Contrast remark.**

Outside that cut-flux-diagonal subclass, boundary-flux preservation is not automatic. In particular, whenever the full detector Hamiltonian contains gauge-invariant mixed hopping terms involving
$$
\widehat U_{n_- -1/2}
\qquad\text{or}\qquad
\widehat U_{n_+ +1/2}
$$
and their adjoints, those terms generally raise or lower the corresponding cut-boundary electric flux and therefore need not commute with the projectors
$$
\widehat P_{R,\lambda}^{\partial}.
$$
So boundary-adjacent mixed hopping couplings must be checked separately; Theorem 4A does not apply to them automatically.

Remark.

Theorem 4 and Theorem 4A together give the strongest exact microscopic detector statement presently justified. Theorem 4 is the general stochastic-instrument theorem for gauge-compatible pointer couplings on the fixed benchmark. Theorem 4A is narrower but more local: for the subclass of boundary-flux-preserving detector couplings, the induced physical-sector instrument already decomposes exactly fiberwise over the boundary-flux sectors. What remains open is the full bridge from arbitrary gauge-compatible region-supported detector Hamiltonians to a general boundary-flux/edge-mode-resolved locality theorem, and beyond that the still-stronger universality statement for arbitrary abstract localized instruments of Sections II and III.

### Localized setting Hamiltonians on the same finite matter-plus-link benchmark

The detector benchmark above is not by itself the full phase-10 microscopic story. The next matching step is to put settings on the same microscopic footing: region-supported gauge-compatible Hamiltonian pulses on the same Paper 11 matter-link benchmark, with exact induced stochastic setting maps at the same fixed finite scope.

**Definition 9**

(Gauge-compatible localized setting-Hamiltonian family on a mixed region).

Fix a gauge-compatible mixed region $R$ of Paper 11, a compatible Gauss sector $ \mathbf g $, a finite setting set $ \mathcal X_R $, and a pulse window $[0,\tau_{\mathrm{set}}]$. A localized setting-Hamiltonian family supported in $R$ is a collection of bounded self-adjoint time-dependent Hamiltonians
$$
\widehat H_{R,\mathrm{set}}^{(S)}(x,t)
:=
\widehat H_{\mathrm{dyn}}^{(S)}
+
\sum_{\alpha=1}^{M_R}u_\alpha^x(t)\,\widehat O_{R,\alpha}^{(S)},
\qquad
x\in\mathcal X_R,\ t\in[0,\tau_{\mathrm{set}}],
$$
where each control profile $u_\alpha^x$ is real-valued and each $ \widehat O_{R,\alpha}^{(S)} $ is gauge invariant and generated by gauge-compatible mixed local cells contained in $R$. For each compatible sector, define
$$
\widehat H_{R,\mathrm{set}}^{(S,\mathbf g)}(x,t)
:=
P_{\mathbf g}\widehat H_{R,\mathrm{set}}^{(S)}(x,t)P_{\mathbf g},
$$
and the corresponding setting propagator
$$
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g)}(x;\tau_{\mathrm{set}})
:=
\mathcal T\exp\!\left(
-i\int_0^{\tau_{\mathrm{set}}}
\widehat H_{R,\mathrm{set}}^{(S,\mathbf g)}(x,t)\,dt
\right).
$$

**Proposition 4**

(Exact Gauss-sector preservation of localized setting pulses).

For every site $n$, setting value $x$, and pulse time $t$,
$$
[\widehat G_n,\widehat H_{R,\mathrm{set}}^{(S)}(x,t)]=0.
$$
Consequently
$$
\widehat U_{R,\mathrm{set}}^{(S)}(x;\tau_{\mathrm{set}})
=
\bigoplus_{\mathbf g}
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g)}(x;\tau_{\mathrm{set}}),
$$
so no transitions occur between distinct compatible Gauss sectors.

Proof.

By Paper 11, $ \widehat H_{\mathrm{dyn}}^{(S)} $ commutes with every $ \widehat G_n $. By Definition 9, each added local setting generator $ \widehat O_{R,\alpha}^{(S)} $ is gauge invariant and therefore commutes with every $ \widehat G_n $. The commutator vanishes termwise for each $x,t$, so the full time-dependent Hamiltonian commutes with all Gauss generators at all times. Standard propagation then gives block-diagonal evolution in the Gauss-sector decomposition.

$ \square $

**Theorem 4B**

(Exact finite-benchmark stochastic setting map from a localized setting pulse).

Fix $L$, $S$, a gauge-compatible mixed region $R$, a compatible Gauss sector $ \mathbf g $, a setting value $x\in\mathcal X_R$, and pulse duration $ \tau_{\mathrm{set}} $. Define the matrix on $ \Omega_{L,S}^{(\mathbf g)} $ by
$$
\bigl[\mathcal S_{R,\mathbf g}^{x,(S)}(\tau_{\mathrm{set}})\bigr]_{\omega',\omega}
:=
\Bigl|
\langle \omega'|
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g)}(x;\tau_{\mathrm{set}})
|\omega\rangle
\Bigr|^2.
$$
Then:

1. every entry of $ \mathcal S_{R,\mathbf g}^{x,(S)}(\tau_{\mathrm{set}}) $ is nonnegative;
2. $ \mathcal S_{R,\mathbf g}^{x,(S)}(\tau_{\mathrm{set}}) $ is column-stochastic;
3. the construction is exactly sector preserving in the sense of Proposition 4; and
4. the stochastic setting map is generated by a genuinely gauge-compatible mixed-region Hamiltonian pulse on the same finite matter-plus-link benchmark as the detector theorem.

Proof.

Nonnegativity is immediate from the absolute-square definition. For each incoming $ \omega\in\Omega_{L,S}^{(\mathbf g)} $,
$$
\sum_{\omega'}
\bigl[\mathcal S_{R,\mathbf g}^{x,(S)}(\tau_{\mathrm{set}})\bigr]_{\omega',\omega}
=
\sum_{\omega'}
\Bigl|
\langle \omega'|
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g)}(x;\tau_{\mathrm{set}})
|\omega\rangle
\Bigr|^2
=1
$$
by unitarity on the finite sector block. Sector preservation is Proposition 4. The final item is exactly Definition 9.

$ \square $

**Theorem 4C**

(Partial boundary-flux-resolved locality for boundary-flux-preserving setting pulses).

Assume $V_R=\{n_-,n_-+1,\dots,n_+\}$ is connected and fix the physical Gauss sector $ \mathbf g_{\mathrm{phys}} $. Suppose that for every admissible boundary-flux label $ \lambda $, setting value $x$, and pulse time $t$,
$$
[P_{R,\lambda}^{\partial},\widehat H_{R,\mathrm{set}}^{(S,\mathbf g_{\mathrm{phys}})}(x,t)]=0.
$$
Then:

1. the setting propagator
  $$
  \widehat U_{R,\mathrm{set}}^{(S,\mathbf g_{\mathrm{phys}})}(x;\tau_{\mathrm{set}})
  $$
  preserves each boundary-flux fiber;
2. the stochastic setting map
  $$
  \mathcal S_{R,\mathbf g_{\mathrm{phys}}}^{x,(S)}(\tau_{\mathrm{set}})
  $$
  is block diagonal with respect to
  $$
  \Omega_{L,S}^{(\mathbf g_{\mathrm{phys}})}
  =
  \bigsqcup_{\lambda\ \mathrm{admissible}}
  \Omega_{R,\lambda}^{(\mathbf g_{\mathrm{phys}})};
  $$
  equivalently, no entry connects configurations with different boundary-flux labels; and
3. the remaining microscopic locality question for this setting class is reduced fiberwise to fixed-$\lambda$ sectors.

Proof.

If each $P_{R,\lambda}^{\partial}$ commutes with the time-dependent generator at all times, then each $P_{R,\lambda}^{\partial}$ commutes with the Dyson expansion of the time-ordered propagator and hence with
$$
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g_{\mathrm{phys}})}(x;\tau_{\mathrm{set}}).
$$
Therefore, for distinct admissible labels $\lambda\neq\lambda'$,
$$
P_{R,\lambda'}^{\partial}
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g_{\mathrm{phys}})}(x;\tau_{\mathrm{set}})
P_{R,\lambda}^{\partial}
=0.
$$
So if $\partial\Phi_R(\omega)=\lambda$ and $\partial\Phi_R(\omega')=\lambda'$ with $\lambda\neq\lambda'$, then
$$
\langle \omega'|
\widehat U_{R,\mathrm{set}}^{(S,\mathbf g_{\mathrm{phys}})}(x;\tau_{\mathrm{set}})
|\omega\rangle
=0,
$$
and therefore
$$
\bigl[\mathcal S_{R,\mathbf g_{\mathrm{phys}}}^{x,(S)}(\tau_{\mathrm{set}})\bigr]_{\omega',\omega}=0.
$$
This gives the claimed block diagonality and the fiberwise reduction statement.

$ \square $

Remark.

Theorems 4, 4A, 4B, and 4C now put settings and detectors on the same finite microscopic footing at the first exact benchmark level: both are generated by gauge-compatible mixed-region Hamiltonians, both preserve Gauss sectors, and both admit partial boundary-flux-resolved locality theorems for boundary-flux-preserving subclasses. The remaining stronger burden is full universality for arbitrary abstract localized controls/instruments, full boundary-flux/edge-mode-resolved locality for arbitrary gauge-compatible couplings, full Bell-bridge and Bell-1976 local-causality theorems in generality, and a constructive fully integrable Lorentz-covariant detector/control theory; Sections VI.2–VI.7 address restricted or conditional benchmark versions only.

### Restricted Bell bridge on a commuting benchmark family

The microscopic setting and detector theorems above do not by themselves yield the full Bell bridge. The next exact step, still strictly restricted, is to show that a benchmark family of such localized maps already reproduces the same operational joint-law structure used in Sections II and III, provided one imposes a concrete commuting-family hypothesis.

**Definition 10**

(Restricted two-wing microscopic benchmark Bell family).

Fix a compatible Gauss sector $ \mathbf g $, two gauge-compatible mixed regions $R_A,R_B$, setting sets $ \mathcal X_A,\mathcal X_B $, and outcome sets $ \mathcal A_A,\mathcal A_B $. For each $x\in\mathcal X_A$, let
$$
\mathcal S_{A,\mathbf g}^{x,(S)}
:=
\mathcal S_{R_A,\mathbf g}^{x,(S)}(\tau_{A,\mathrm{set}})
$$
be the setting map from Theorem 4B, and for each $a\in\mathcal A_A$ let
$$
\mathcal J_{A,\mathbf g}^{a,(S)}
:=
\mathcal J_{R_A,\mathbf g}^{a,(S)}(\tau_{A,\mathrm{det}})
$$
be the detector instrument map from Theorem 4. Define
$$
\mathcal I_{A,\mathbf g}^{a|x,(S)}
:=
\mathcal J_{A,\mathbf g}^{a,(S)}\,
\mathcal S_{A,\mathbf g}^{x,(S)},
\qquad
\Lambda_{A,\mathbf g}^{x,(S)}
:=
\sum_a \mathcal I_{A,\mathbf g}^{a|x,(S)}.
$$
Define $ \mathcal I_{B,\mathbf g}^{b|y,(S)} $ and $ \Lambda_{B,\mathbf g}^{y,(S)} $ analogously from $R_B$.

Call this family

*benchmark commuting*

if for all outcomes and settings,
$$
\mathcal I_{A,\mathbf g}^{a|x,(S)}\mathcal I_{B,\mathbf g}^{b|y,(S)}
=
\mathcal I_{B,\mathbf g}^{b|y,(S)}\mathcal I_{A,\mathbf g}^{a|x,(S)}.
$$
Given a source law $q_{\mathbf g}$ on $ \Omega_{L,S}^{(\mathbf g)} $, define
$$
\kappa_{A,\mathbf g}^{a|x}(\zeta_A(\omega)).
$$
Therefore
$$
p_{\mathbf g}(a,b|x,y)
:=
\mathbf 1^\top
\mathcal I_{A,\mathbf g}^{a|x,(S)}
\mathcal I_{B,\mathbf g}^{b|y,(S)}
q_{\mathbf g}.
$$

**Theorem 4D**

(Restricted microscopic Bell bridge theorem on the fixed benchmark).

In the setting of Definition 10, assume the benchmark-commuting hypothesis and that $q_{\mathbf g}$ is normalized. Then:

1. for every $x,y$, $p_{\mathbf g}(a,b|x,y)\ge 0$ and
  $$
  \sum_{a,b}p_{\mathbf g}(a,b|x,y)=1;
  $$
2. the joint law is foliation-order independent at this benchmark level:
  $$
  \mathbf 1^\top
  \mathcal I_{A,\mathbf g}^{a|x,(S)}
  \mathcal I_{B,\mathbf g}^{b|y,(S)}
  q_{\mathbf g}
  =
  \mathbf 1^\top
  \mathcal I_{B,\mathbf g}^{b|y,(S)}
  \mathcal I_{A,\mathbf g}^{a|x,(S)}
  q_{\mathbf g};
  $$
3. the local marginals obey no-signaling:
  $$
  \sum_b p_{\mathbf g}(a,b|x,y)\ \text{is independent of }y,
  \qquad
  \sum_a p_{\mathbf g}(a,b|x,y)\ \text{is independent of }x;
  $$
  and
4. the family
  $$
  p_{\mathbf g}(a,b|x,y)
  =
  \mathbf 1^\top
  \mathcal I_{A,\mathbf g}^{a|x,(S)}
  \mathcal I_{B,\mathbf g}^{b|y,(S)}
  q_{\mathbf g}
  $$
  has exactly the same operational algebraic form as Definition 4, now realized by explicit localized setting-plus-detector benchmark maps inside the finite matter-link system.

Proof.

By Theorem 4 and Theorem 4B, each factor $ \mathcal J_{A,\mathbf g}^{a,(S)} $ is nonnegative and each $ \mathcal S_{A,\mathbf g}^{x,(S)} $ is column-stochastic with nonnegative entries, so every
$$
\mathcal I_{A,\mathbf g}^{a|x,(S)}
=
\mathcal J_{A,\mathbf g}^{a,(S)}\mathcal S_{A,\mathbf g}^{x,(S)}
$$
is nonnegative. The same holds on wing $B$. Hence $p_{\mathbf g}(a,b|x,y)\ge 0$.

Also
$$
\Lambda_{A,\mathbf g}^{x,(S)}
=
\Bigl(\sum_a \mathcal J_{A,\mathbf g}^{a,(S)}\Bigr)\mathcal S_{A,\mathbf g}^{x,(S)}
$$
is column-stochastic because both factors are column-stochastic; similarly for
$$
\Lambda_{B,\mathbf g}^{y,(S)}.
$$
Therefore
$$
\sum_{a,b}p_{\mathbf g}(a,b|x,y)
=
\mathbf 1^\top
\Lambda_{A,\mathbf g}^{x,(S)}
\Lambda_{B,\mathbf g}^{y,(S)}
q_{\mathbf g}
=
\mathbf 1^\top q_{\mathbf g}
=
1.
$$

Item 2 is exactly the benchmark-commuting hypothesis.

For no-signaling, sum over Bob's outcomes:
$$
\sum_b p_{\mathbf g}(a,b|x,y)
=
\mathbf 1^\top
\mathcal I_{A,\mathbf g}^{a|x,(S)}
\Lambda_{B,\mathbf g}^{y,(S)}
q_{\mathbf g}.
$$
By summing the commuting identities over $b$,
$$
\mathcal I_{A,\mathbf g}^{a|x,(S)}\Lambda_{B,\mathbf g}^{y,(S)}
=
\Lambda_{B,\mathbf g}^{y,(S)}\mathcal I_{A,\mathbf g}^{a|x,(S)}.
$$
Hence
$$
\sum_b p_{\mathbf g}(a,b|x,y)
=
\mathbf 1^\top
\Lambda_{B,\mathbf g}^{y,(S)}
\mathcal I_{A,\mathbf g}^{a|x,(S)}
q_{\mathbf g}
=
\mathbf 1^\top
\mathcal I_{A,\mathbf g}^{a|x,(S)}
q_{\mathbf g},
$$
independent of $y$ because $ \mathbf 1^\top\Lambda_{B,\mathbf g}^{y,(S)}=\mathbf 1^\top $. The Bob statement is symmetric. Item 4 is the displayed formula itself: it is the same bilinear operational form as Definition 4, now with explicit microscopic benchmark maps.

$ \square $

**Scope remark.**

Theorem 4D is intentionally restricted. It does not prove the full microscopic Bell bridge for arbitrary gauge-compatible couplings; it proves that a concrete commuting benchmark family of localized setting pulses plus localized detector couplings already reproduces the operational law structure isolated earlier in this paper.

### Restricted universality on a commuting-projector subclass

The remaining universality burden is still too large in full generality. But one meaningful subclass is already tractable at exact benchmark level: instruments whose outcome dependence is carried by a finite commuting gauge-invariant local observable family, with the benchmark reference propagation retained exactly.

**Definition 11**

(Commuting-projector restricted-universality subclass).

Fix $L,S$, a gauge-compatible mixed region $R$, a compatible Gauss sector $ \mathbf g $, and a time step $ \tau $. Let
$$
\Gamma_0^{(S,\mathbf g)}(\tau)
$$
denote the sector primitive kernel of the benchmark dynamics. Let
$$
\{\widehat Z_{R,\alpha}^{(S,\mathbf g)}\}_{\alpha=1}^m
$$
be a finite commuting gauge-invariant observable family generated by mixed local cells contained in $R$, with finite joint spectrum $ \mathfrak Z_R $ and joint spectral projectors
$$
\{\Pi_\zeta^{(R,\mathbf g)}\}_{\zeta\in\mathfrak Z_R}.
$$
Assume
$$
[\Pi_\zeta^{(R,\mathbf g)},\widehat H_{\mathrm{dyn}}^{(S,\mathbf g)}]=0
$$
for all $ \zeta $.

A localized instrument
$$
\{\mathcal K_{R,\mathbf g}^{a,(S)}(\tau)\}_{a\in\mathcal A_R}
$$
on $ \Omega_{L,S}^{(\mathbf g)} $ belongs to the commuting-projector subclass if there are stochastic weights
$$
q_a:\mathfrak Z_R\to[0,1],
\qquad
\sum_a q_a(\zeta)=1\ \forall\zeta,
$$
such that
$$
\bigl[\mathcal K_{R,\mathbf g}^{a,(S)}(\tau)\bigr]_{\omega',\omega}
=
q_a(\zeta(\omega))\,
\bigl[\Gamma_0^{(S,\mathbf g)}(\tau)\bigr]_{\omega',\omega},
$$
where $ \zeta(\omega) $ is the joint-eigenvalue label of $ \omega $ for the chosen commuting family. Equivalently,
$$
\mathcal K_{R,\mathbf g}^{a,(S)}(\tau)
=
\Gamma_0^{(S,\mathbf g)}(\tau)\,Q_{R,\mathbf g}^{a,(S)},
$$
with $Q_{R,\mathbf g}^{a,(S)}$ diagonal in the sector basis and constant on joint-eigenspace columns.

**Theorem 4E**

(Restricted universality for the commuting-projector subclass).

Every instrument in Definition 11 admits an exact microscopic realization on the same finite matter-link benchmark by a gauge-compatible neutral-pointer detector Hamiltonian supported in $R$.

More precisely, there exist a finite pointer ancilla
$$
\mathcal D_R,
$$
a ready state $|0_R\rangle$, an outcome partition
$$
\Xi_R^{\mathrm{det}}=\bigsqcup_a \Xi_{R,a}^{\mathrm{det}},
$$
and a gauge-compatible detector coupling of controlled form
$$
\widehat W_{R,\mathrm{cp}}^{(S,\mathbf g)}
:=
\sum_{\zeta\in\mathfrak Z_R}
\Pi_\zeta^{(R,\mathbf g)}\otimes \widehat K_\zeta
$$
such that the induced detector instrument of Definition 8 satisfies
$$
\mathcal J_{R,\mathbf g}^{a,(S)}(\tau)
=
\mathcal K_{R,\mathbf g}^{a,(S)}(\tau)
\quad
\forall a.
$$

If, in addition, $ \mathbf g=\mathbf g_{\mathrm{phys}} $ and each $ \Pi_\zeta^{(R,\mathbf g_{\mathrm{phys}})} $ commutes with every boundary-flux projector $P_{R,\lambda}^{\partial}$ of Definition 8A, then the realizing Hamiltonian is boundary-flux preserving and the realized instrument is automatically fiberwise block diagonal as in Theorem 4A.

Proof.

For each $ \zeta\in\mathfrak Z_R $, choose a finite-dimensional pointer unitary $U_\zeta$ such that
$$
\sum_{\xi\in\Xi_{R,a}^{\mathrm{det}}}
\bigl|
\langle \xi|U_\zeta|0_R\rangle
\bigr|^2
=
q_a(\zeta)
\quad
\forall a.
$$
This is always possible in finite dimension by completing
$$
U_\zeta|0_R\rangle
=
\sum_{a,\nu}
\sqrt{q_a(\zeta)}\,c_{a,\nu}^{(\zeta)}|a,\nu\rangle
$$
to a unitary basis extension.

Define the controlled pointer unitary
$$
\widehat U_{\mathrm{cp}}
:=
\sum_{\zeta\in\mathfrak Z_R}
\Pi_\zeta^{(R,\mathbf g)}\otimes U_\zeta.
$$
Because each projector commutes with $ \widehat H_{\mathrm{dyn}}^{(S,\mathbf g)} $, the benchmark-plus-pointer unitary
$$
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)
:=
e^{-i\tau(\widehat H_{\mathrm{dyn}}^{(S,\mathbf g)}\otimes I)}
\widehat U_{\mathrm{cp}}
$$
is generated by a self-adjoint Hamiltonian of the stated controlled form (choose $ \widehat K_\zeta $ with $U_\zeta=e^{-i\tau \widehat K_\zeta}$).

For basis states $|\omega\rangle,|\omega'\rangle$,
$$
\langle \omega',\xi|
\widehat U_{R,\mathrm{det}}^{(S,\mathbf g)}(\tau)
|\omega,0_R\rangle
=
\langle \omega'|e^{-i\tau \widehat H_{\mathrm{dyn}}^{(S,\mathbf g)}}|\omega\rangle\,
\langle \xi|U_{\zeta(\omega)}|0_R\rangle.
$$
Summing $|\cdot|^2$ over $\xi\in\Xi_{R,a}^{\mathrm{det}}$ gives
$$
\bigl[\mathcal J_{R,\mathbf g}^{a,(S)}(\tau)\bigr]_{\omega',\omega}
=
q_a(\zeta(\omega))\,
\bigl[\Gamma_0^{(S,\mathbf g)}(\tau)\bigr]_{\omega',\omega},
$$
which is exactly the target form of Definition 11. Hence
$$
\mathcal J_{R,\mathbf g}^{a,(S)}(\tau)
=
\mathcal K_{R,\mathbf g}^{a,(S)}(\tau).
$$

The boundary-flux clause is immediate: if every $ \Pi_\zeta^{(R,\mathbf g_{\mathrm{phys}})} $ commutes with every $P_{R,\lambda}^{\partial}$, then so does the controlled coupling, hence the realized instrument inherits Theorem 4A block diagonality.

$ \square $

Remark.

Theorem 4E is a genuine restricted-universality statement: it covers a nontrivial benchmark subclass (commuting-projector, optionally boundary-flux-preserving instruments) without claiming universality for arbitrary abstract localized instruments. It includes, in particular, readout families diagonal in natural commuting local charge/flux data generated inside the mixed region.

### Assumption ledger for Theorems 4D–4I

To prevent hidden assumption creep, this subsection records the exact dependency package for the restricted theorem cluster.

**Assumption ledger.**

For Sections VI.2–VI.7, the theorem-level dependencies are exactly:

1. *Theorem 4D.* Definition 10, the benchmark-commuting hypothesis, and normalized source law $q_{\mathbf g}$; plus nonnegativity/column-stochasticity inherited from Theorems 4 and 4B.
2. *Theorem 4E.* Definition 11 (commuting-projector subclass), including $[\Pi_\zeta^{(R,\mathbf g)},\widehat H_{\mathrm{dyn}}^{(S,\mathbf g)}]=0$; the boundary-flux refinement additionally requires $ \mathbf g=\mathbf g_{\mathrm{phys}} $ and $[\Pi_\zeta^{(R,\mathbf g_{\mathrm{phys}})},P_{R,\lambda}^{\partial}]=0$.
3. *Theorem 4F.* Definition 12 in full: label-local response kernels, remote-label preservation, and source label-memory factorization with stochastic memory law and stochastic label channels.
4. *Theorem 4G.* Exactly assumptions (1)–(4) in Theorem 4G (Lorentz-covariant transport, covariant layer transformation, spacelike commutation of benchmark layer maps, and adjacent-exchange foliation relation).
5. *Theorem 4I.* Definition 14 together with Definition 12, Lemma 4F0, and Theorem 4F (for positivity/normalization and equality of embedded and benchmark observed laws).
6. *Scope boundary shared by 4D–4I.* No claim here is full arbitrary-coupling universality, full boundary-flux-resolved locality, full microscopic Bell bridge, full Bell-1976 theorem, or constructive full Lorentz integrability.

### Restricted Bell-1976 local causality with temporal memory

The Bell-1976 burden is stronger than Bell-inequality compatibility: it asks for a local-beables screening-off structure. Full generality is still open, but on a meaningful benchmark subclass one can already construct the memory beable explicitly from benchmark data and prove restricted screening-off directly.

**Definition 12**

(Constructive Bell-1976 benchmark subclass with explicit memory variable).

Fix a sector family
$$
p_{\mathbf g}(a,b|x,y)
$$
from Definition 10 with wing maps in the commuting-projector class of Definition 11. Let
$$
\zeta_A:\Omega_{L,S}^{(\mathbf g)}\to\mathfrak Z_A,
\qquad
\zeta_B:\Omega_{L,S}^{(\mathbf g)}\to\mathfrak Z_B
$$
be the wing label maps induced by the chosen commuting-projector families.
Assume:

1. *label-local response kernels* exist:
  $$
  \kappa_{A,\mathbf g}^{a|x}(\zeta_A)
  :=
  \sum_{\omega'}[\mathcal I_{A,\mathbf g}^{a|x,(S)}]_{\omega',\omega},
  \qquad
  \kappa_{B,\mathbf g}^{b|y}(\zeta_B)
  :=
  \sum_{\omega'}[\mathcal I_{B,\mathbf g}^{b|y,(S)}]_{\omega',\omega},
  $$
  where each right-hand side is constant on the corresponding label fiber;
2. *remote-label preservation* :
  if
  $$
  [\mathcal I_{B,\mathbf g}^{b|y,(S)}]_{\omega',\omega}\neq 0
  $$
  then $\zeta_A(\omega')=\zeta_A(\omega)$, and symmetrically with $A/B$ exchanged;
3. *source label-memory factorization* :
  with
  $$
  \pi_{\mathbf g}(\zeta_A,\zeta_B)
  :=
  \sum_{\omega:\,\zeta_A(\omega)=\zeta_A,\ \zeta_B(\omega)=\zeta_B}
  q_{\mathbf g}(\omega),
  $$
  there exist a finite memory space $\mathcal R_{\mathbf g}$, a law
  $$
  \mu_{\mathbf g}(\rho),\qquad \mu_{\mathbf g}(\rho)\ge 0,\qquad \sum_\rho \mu_{\mathbf g}(\rho)=1,
  $$
  and label channels
  $$
  \nu_{A,\mathbf g}(\zeta_A|\rho),\qquad
  \nu_{B,\mathbf g}(\zeta_B|\rho)
  $$
  with
  $$
  \nu_{A,\mathbf g}(\zeta_A|\rho)\ge 0,\qquad
  \sum_{\zeta_A}\nu_{A,\mathbf g}(\zeta_A|\rho)=1,
  $$
  $$
  \nu_{B,\mathbf g}(\zeta_B|\rho)\ge 0,\qquad
  \sum_{\zeta_B}\nu_{B,\mathbf g}(\zeta_B|\rho)=1,
  $$
  such that
  $$
  \pi_{\mathbf g}(\zeta_A,\zeta_B)
  =
  \sum_{\rho\in\mathcal R_{\mathbf g}}
  \mu_{\mathbf g}(\rho)\,
  \nu_{A,\mathbf g}(\zeta_A|\rho)\,
  \nu_{B,\mathbf g}(\zeta_B|\rho).
  $$

The memory beable is then explicitly
$$
\lambda:=\rho\in\mathcal R_{\mathbf g}.
$$
Define local responses
$$
A_{\mathbf g}(a|x,\rho)
:=
\sum_{\zeta_A}
\kappa_{A,\mathbf g}^{a|x}(\zeta_A)\,
\nu_{A,\mathbf g}(\zeta_A|\rho),
$$
$$
B_{\mathbf g}(b|y,\rho)
:=
\sum_{\zeta_B}
\kappa_{B,\mathbf g}^{b|y}(\zeta_B)\,
\nu_{B,\mathbf g}(\zeta_B|\rho).
$$

**Lemma 4F0**

(Probabilistic regularity of the constructed memory model).

Under Definition 12:

1. $\mu_{\mathbf g}$ is a probability law on $\mathcal R_{\mathbf g}$;
2. for each $x,\rho$, $A_{\mathbf g}(a|x,\rho)\ge 0$ and $\sum_a A_{\mathbf g}(a|x,\rho)=1$;
3. for each $y,\rho$, $B_{\mathbf g}(b|y,\rho)\ge 0$ and $\sum_b B_{\mathbf g}(b|y,\rho)=1$.

Hence $A_{\mathbf g}$ and $B_{\mathbf g}$ are bona fide conditional probability kernels.

Proof.

Item 1 is part of Definition 12.

For item 2, each entry of $ \mathcal I_{A,\mathbf g}^{a|x,(S)} $ is nonnegative, so every
$$
\kappa_{A,\mathbf g}^{a|x}(\zeta_A)
=
\sum_{\omega'}[\mathcal I_{A,\mathbf g}^{a|x,(S)}]_{\omega',\omega}
$$
is nonnegative (for any $ \omega $ with $ \zeta_A(\omega)=\zeta_A $; well-defined by label-locality). Also,
$$
\sum_a \kappa_{A,\mathbf g}^{a|x}(\zeta_A)
=
\sum_{\omega'}[\Lambda_{A,\mathbf g}^{x,(S)}]_{\omega',\omega}
=
1
$$
because $ \Lambda_{A,\mathbf g}^{x,(S)}=\sum_a \mathcal I_{A,\mathbf g}^{a|x,(S)} $ is column-stochastic by the Definition 10 construction. With $ \nu_{A,\mathbf g}(\cdot|\rho) $ a stochastic channel, convexity gives
$$
A_{\mathbf g}(a|x,\rho)\ge 0,\qquad
\sum_a A_{\mathbf g}(a|x,\rho)
=
\sum_{\zeta_A}\nu_{A,\mathbf g}(\zeta_A|\rho)\sum_a\kappa_{A,\mathbf g}^{a|x}(\zeta_A)
=
\sum_{\zeta_A}\nu_{A,\mathbf g}(\zeta_A|\rho)
=
1.
$$
Item 3 is identical with $A/B$ exchanged.

$ \square $

**Theorem 4F**

(Constructive restricted Bell-1976 screening-off theorem).

Under Definition 12,
$$
p_{\mathbf g}(a,b|x,y)
=
\sum_{\rho\in\mathcal R_{\mathbf g}}
\mu_{\mathbf g}(\rho)\,
A_{\mathbf g}(a|x,\rho)\,
B_{\mathbf g}(b|y,\rho).
$$
Hence, defining
$$
p_{\mathbf g}(a|x,\rho):=A_{\mathbf g}(a|x,\rho),
\qquad
p_{\mathbf g}(b|y,\rho):=B_{\mathbf g}(b|y,\rho),
$$
By Lemma 4F0 these are normalized nonnegative conditional kernels. Therefore one has Bell-1976 screening-off on this benchmark subclass:
$$
p_{\mathbf g}(a,b|x,y,\rho)
=
p_{\mathbf g}(a|x,\rho)\,p_{\mathbf g}(b|y,\rho).
$$
This is an explicit local-beables-with-temporal-memory realization with
$$
\lambda=\rho,
$$
without claiming the full Bell-1976 theorem for arbitrary couplings.

Proof.

From Definition 10 and the commuting-family hypothesis,
$$
p_{\mathbf g}(a,b|x,y)
=
\sum_{\omega}
q_{\mathbf g}(\omega)\,
\sum_{\omega'}
[\mathcal I_{B,\mathbf g}^{b|y,(S)}]_{\omega',\omega}\,
\sum_{\omega''}
[\mathcal I_{A,\mathbf g}^{a|x,(S)}]_{\omega'',\omega'}.
$$
By remote-label preservation for the $B$ wing, every nonzero transition
$$
\omega\to\omega'
$$
in the middle sum keeps $\zeta_A$ fixed, so label-locality gives
$$
p_{\mathbf g}(a,b|x,y)
=
\sum_{\omega}
q_{\mathbf g}(\omega)\,
\kappa_{A,\mathbf g}^{a|x}(\zeta_A(\omega))\,
\kappa_{B,\mathbf g}^{b|y}(\zeta_B(\omega)).
$$
Grouping by label pairs gives
$$
p_{\mathbf g}(a,b|x,y)
=
\sum_{\zeta_A,\zeta_B}
\pi_{\mathbf g}(\zeta_A,\zeta_B)\,
\kappa_{A,\mathbf g}^{a|x}(\zeta_A)\,
\kappa_{B,\mathbf g}^{b|y}(\zeta_B).
$$
Insert the source label-memory factorization from Definition 12 and rearrange sums:
$$
p_{\mathbf g}(a,b|x,y)
=
\sum_{\rho}
\mu_{\mathbf g}(\rho)\,
A_{\mathbf g}(a|x,\rho)\,
B_{\mathbf g}(b|y,\rho).
$$
By Lemma 4F0, the weights and local response kernels are bona fide probabilities. This is exactly the claimed screening-off decomposition with memory beable
$$
\lambda=\rho.
$$

$ \square $

### Conditional Lorentz-covariant detector/control theorem at benchmark scope

The architecture paper’s Criterion A isolates the missing Lorentz-covariant integrability burden in conditional form. Here the detector/control extension is stated with an explicit sufficient-condition package rather than an opaque path-independence assumption.

**Definition 13**

(Benchmark detector/control layer experiment).

Let
$$
\Sigma_0 \prec \Sigma_f
$$
be initial and final hypersurfaces. Fix localized regions
$$
O_1,\dots,O_m
$$
between them, with localized benchmark maps
$$
\mathcal I_{O_k}^{\alpha_k}
$$
(each $\alpha_k$ may include local setting and local detector outcome labels), a final local readout map $M_{O_f}$, and an initial law $q_{\Sigma_0}$. For a foliation ordering $\mathcal F$, set
$$
p_{\mathcal F}(\alpha_1,\dots,\alpha_m)
:=
\mathbf 1^\top
M_{O_f}\,
\mathcal T_{\mathcal F}\!\left[
\prod_{k=1}^{m}\mathcal I_{O_k}^{\alpha_k}
\right]
q_{\Sigma_0}.
$$

**Theorem 4G**

(Lorentz-covariant detector/control theorem under explicit sufficient conditions).

Assume:

1. the underlying hypersurface ISP is Lorentz-covariant (Definition 3 of the architecture paper), with stochastic transport maps $U_\Lambda^\Sigma$;
2. benchmark detector/control maps transform covariantly:
  $$
  U_\Lambda^{\Sigma_+}\mathcal I_O^{\alpha}
  =
  \mathcal I_{\Lambda O}^{\alpha}U_\Lambda^{\Sigma_-},
  \qquad
  M_{\Lambda O_f}U_\Lambda^{\Sigma_f}=M_{O_f};
  $$
3. every pair of spacelike-separated benchmark layer maps commutes:
  $$
  \mathcal I_O^{\alpha}\mathcal I_{O'}^{\beta}
  =
  \mathcal I_{O'}^{\beta}\mathcal I_O^{\alpha}
  \quad
  \text{for spacelike }O\perp O';
  $$
4. any two foliations considered are related by finitely many adjacent exchanges of spacelike-separated neighboring layer regions.

Then:

1. the experiment law is foliation compatible:
  $$
  p_{\mathcal F}(\alpha_1,\dots,\alpha_m)
  =
  p_{\mathcal F'}(\alpha_1,\dots,\alpha_m)
  $$
  for any such pair $\mathcal F,\mathcal F'$; and
2. the Lorentz-transformed experiment has identical probabilities:
  $$
  p_{\Lambda\mathcal F}(\alpha_1,\dots,\alpha_m)
  =
  p_{\mathcal F}(\alpha_1,\dots,\alpha_m).
  $$

So, under these explicit assumptions, the detector/control extension of Criterion A holds at restricted benchmark scope.

Proof.

By assumptions (3) and (4), the ordered layer products for $\mathcal F$ and $\mathcal F'$ are connected by a finite sequence of swaps of commuting adjacent spacelike-separated factors, so they are equal. This proves foliation compatibility.

For Lorentz covariance, compute the transformed experiment probability by conjugating each segment of the layer string with the corresponding $U_\Lambda^\Sigma$. Assumption (2) replaces each transformed layer by the conjugate benchmark layer in the original frame, while the initial/final conjugations cancel between preparation and readout. Assumption (1) provides covariance of inter-layer propagation. Therefore the full transformed operator string yields the same scalar probability as the original one.

This is still not a full constructive field-theory theorem, but it gives a transparent sufficient-condition package for benchmark Lorentz and foliation compatibility.

$ \square $

### Existence and worked benchmark family

**Proposition 4H**

(Nonempty explicit class satisfying the restricted benchmark hypotheses).

There exists a nonempty class of benchmark families with the following properties:

1. wing regions $R_A$ and $R_B$ are disjoint and connected;
2. wing setting pulses and detector couplings are built from commuting gauge-invariant local charge/flux observables on each wing and are boundary-flux preserving;
3. the induced detector instruments lie in the commuting-projector subclass of Definition 11;
4. the two-wing benchmark family satisfies Definition 12 (explicit memory-label factorization on the source labels); and
5. therefore Theorems 4D, 4E, and 4F apply; if the sufficient-condition package of Theorem 4G also holds, then Theorem 4G applies as well.

Proof sketch.

Take finite label sets on each wing generated by commuting local charge/flux projectors and choose nontrivial pointer unitaries $U_\zeta$ as in Theorem 4E, giving nontrivial outcome kernels $q_a(\zeta)$. Choose nonconstant localized setting pulses diagonal in the same commuting label algebra. Choose a finite memory variable $\rho$ and source label channels
$$
\nu_A(\zeta_A|\rho),\qquad \nu_B(\zeta_B|\rho)
$$
with a nondegenerate memory prior $\mu(\rho)$, then define
$$
\pi(\zeta_A,\zeta_B)
=
\sum_\rho \mu(\rho)\nu_A(\zeta_A|\rho)\nu_B(\zeta_B|\rho).
$$
This realizes Definition 12 by construction and is manifestly nonempty (e.g. two memory values and two wing labels with nontrivial stochastic channels). Disjoint-support locality gives the commuting-family condition of Theorem 4D at this benchmark level, and Theorem 4E supplies microscopic realizability. If, in addition, assumptions (1)–(4) of Theorem 4G are imposed, the Lorentz/foliation conclusion follows.

$ \square $

**Example 1**

(Constructed two-setting/two-outcome benchmark computed end-to-end).

Fix
$$
\mathcal X_A=\mathcal X_B=\mathcal A_A=\mathcal A_B=\{0,1\},
\qquad
\mathcal R_{\mathbf g}=\{0,1\},
\qquad
\mathfrak Z_A=\mathfrak Z_B=\{0,1\},
\qquad
\mu_{\mathbf g}(0)=\mu_{\mathbf g}(1)=\tfrac12,
$$
with channels
$$
\nu_{A,\mathbf g}(\zeta_A|\rho)=\delta_{\zeta_A,\rho},
\qquad
\nu_{B,\mathbf g}(\zeta_B|\rho)=\delta_{\zeta_B,\rho}.
$$
Define explicit label-local response kernels
$$
\kappa_{A,\mathbf g}^{0|x}(\zeta_A)
:=
\begin{cases}
\tfrac34,& \zeta_A=x,\\[1mm]
\tfrac14,& \zeta_A\neq x,
\end{cases}
\qquad
\kappa_{A,\mathbf g}^{1|x}(\zeta_A):=1-\kappa_{A,\mathbf g}^{0|x}(\zeta_A),
$$
$$
\kappa_{B,\mathbf g}^{0|y}(\zeta_B)
:=
\begin{cases}
\tfrac23,& \zeta_B=y,\\[1mm]
\tfrac13,& \zeta_B\neq y,
\end{cases}
\qquad
\kappa_{B,\mathbf g}^{1|y}(\zeta_B):=1-\kappa_{B,\mathbf g}^{0|y}(\zeta_B).
$$
By Definition 12,
$$
A_{\mathbf g}(a|x,\rho)=\kappa_{A,\mathbf g}^{a|x}(\rho),
\qquad
B_{\mathbf g}(b|y,\rho)=\kappa_{B,\mathbf g}^{b|y}(\rho).
$$
Hence the Theorem 4F decomposition is explicitly
$$
p_{\mathbf g}(a,b|x,y)
=
\tfrac12\,\kappa_{A,\mathbf g}^{a|x}(0)\kappa_{B,\mathbf g}^{b|y}(0)
\;+\;
\tfrac12\,\kappa_{A,\mathbf g}^{a|x}(1)\kappa_{B,\mathbf g}^{b|y}(1)
=
\frac{5+2\,\mathbf 1_{\{a\oplus b=x\oplus y\}}}{24}.
$$
So
$$
\sum_{a,b}p_{\mathbf g}(a,b|x,y)=1,\qquad
\sum_b p_{\mathbf g}(a,b|x,y)=\tfrac12,\qquad
\sum_a p_{\mathbf g}(a,b|x,y)=\tfrac12,
$$
and no-signaling plus screening-off are explicit on this finite benchmark.

Define
$$
E_{xy}:=\sum_{a,b}(-1)^{a+b}\,p_{\mathbf g}(a,b|x,y)
=\frac{(-1)^{x\oplus y}}{6}.
$$
Then, for the standard CHSH combination,
$$
S_{\mathrm{CHSH}}:=E_{00}+E_{01}+E_{10}-E_{11}
=-\frac13,
$$
hence
$$
|S_{\mathrm{CHSH}}|\le 2.
$$
Thus this is a fully checkable constructed restricted Bell-local benchmark, and any CHSH-violating full-circuit family of Theorem 3 lies outside this class.

### Restricted embedding into a simple setting-dependent full-circuit family

The previous results isolate a restricted benchmark class and compute its Bell family exactly. The next restricted step is to embed that class into a simple setting-dependent full-circuit family in the sense of Definition 5, without claiming a full microscopic bridge theorem.

**Definition 14**

(Simple benchmark-to-full-circuit embedding family).

Fix a benchmark family in Definition 12 and the derived kernels of Theorem 4F. Let
$$
\mathcal Y_{\mathbf g}:=\mathcal A_A\times\mathcal A_B\times\mathcal R_{\mathbf g}
$$
and fix an initial configuration label $j_0$. For each setting pair $(x,y)$ define
$$
\Theta_{\mathrm{emb}}^{(xy)}((a,b,\rho)\mid j_0)
:=
\sqrt{\mu_{\mathbf g}(\rho)\,A_{\mathbf g}(a|x,\rho)\,B_{\mathbf g}(b|y,\rho)},
$$
with associated observable transition kernel
$$
\Gamma_{\mathrm{emb}}^{(xy)}
:=
\bigl|\Theta_{\mathrm{emb}}^{(xy)}\bigr|^2.
$$
Define the observed outcome law by marginalizing the memory register:
$$
p_{\mathrm{emb}}(a,b|x,y)
:=
\sum_{\rho\in\mathcal R_{\mathbf g}}
\Gamma_{\mathrm{emb}}^{(xy)}((a,b,\rho)\mid j_0).
$$

**Theorem 4I**

(Restricted embedding theorem into a setting-dependent full-circuit family).

Under Definition 12 and Lemma 4F0:

1. the family
  $$
  \{\Theta_{\mathrm{emb}}^{(xy)}\}_{x,y}
  $$
  is a setting-dependent full-circuit family in the sense of Definition 5 (with
  $$
  \Gamma_{\mathrm{emb}}^{(xy)}=\bigl|\Theta_{\mathrm{emb}}^{(xy)}\bigr|^2
  $$); and
2. its observed law reproduces the benchmark Bell family exactly:
  $$
  p_{\mathrm{emb}}(a,b|x,y)
  =
  p_{\mathbf g}(a,b|x,y)
  $$
  for all outcomes and settings.

Hence every family in this restricted benchmark class admits an explicit simple setting-dependent full-circuit embedding, while the full arbitrary-coupling bridge remains open.

Proof.

By Lemma 4F0,
$$
\mu_{\mathbf g}(\rho)\ge 0,\qquad
A_{\mathbf g}(a|x,\rho)\ge 0,\qquad
B_{\mathbf g}(b|y,\rho)\ge 0,
$$
so
$$
\Gamma_{\mathrm{emb}}^{(xy)}((a,b,\rho)\mid j_0)
=
\mu_{\mathbf g}(\rho)\,A_{\mathbf g}(a|x,\rho)\,B_{\mathbf g}(b|y,\rho)\ge 0.
$$
Also
$$
\sum_{a,b,\rho}\Gamma_{\mathrm{emb}}^{(xy)}((a,b,\rho)\mid j_0)
=
\sum_{\rho}\mu_{\mathbf g}(\rho)\sum_a A_{\mathbf g}(a|x,\rho)\sum_b B_{\mathbf g}(b|y,\rho)
=
1.
$$
So each $ \Gamma_{\mathrm{emb}}^{(xy)} $ is a normalized stochastic outcome kernel, and the family is setting-indexed through $A_{\mathbf g}(a|x,\rho)$ and $B_{\mathbf g}(b|y,\rho)$.

Finally,
$$
p_{\mathrm{emb}}(a,b|x,y)
=
\sum_{\rho}\mu_{\mathbf g}(\rho)\,A_{\mathbf g}(a|x,\rho)\,B_{\mathbf g}(b|y,\rho)
=
p_{\mathbf g}(a,b|x,y)
$$
by Theorem 4F.

$ \square $

**Corollary 3**

(Operational equivalence on observed statistics for the restricted embedding).

Under the hypotheses of Theorem 4I, every linear functional of the observed outcome table is identical for the benchmark family and the embedded full-circuit family. In particular:

1. no-signaling properties are identical for $p_{\mathbf g}$ and $p_{\mathrm{emb}}$;
2. all Bell-functional values coincide, including
  $$
  S_{\mathrm{CHSH}}[p_{\mathrm{emb}}]=S_{\mathrm{CHSH}}[p_{\mathbf g}].
  $$

Proof.

Theorem 4I gives pointwise equality
$$
p_{\mathrm{emb}}(a,b|x,y)=p_{\mathbf g}(a,b|x,y)
$$
for all outcomes and settings. Any linear statistic of the table therefore agrees term by term.

$ \square $

**Scope remark.**

Theorem 4I is intentionally restricted and effective: it embeds the already-constructed benchmark Bell family into a simple setting-dependent full-circuit family at the stochastic transition level. It is not yet a full microscopic derivation of arbitrary setting-dependent circuits from arbitrary gauge-compatible couplings.

## What phase 10 now closes and what it defers

With the scope fixed this way, phase 10 is complete at the strongest honest operational scope currently justified.

**Theorem 5**

(Exact phase-10 closure at the presently justified scope).

At the presently justified operational scope, phase 10 is closed in the following exact sense.

1. *Exact localized control/readout calculus.* Settings and detectors are represented by localized stochastic controls and localized detector instruments on factorized finite hypersurface configuration spaces.
2. *Exact abstract finite realization theorem.* Every finite localized detector instrument admits an abstract ancilla / unitary / pointer realization on an enlarged finite factor space.
3. *Exact foliation-compatible composition.* Spacelike-separated operational layers commute and therefore compose independently of foliation order.
4. *Exact no-signaling.* Local marginals are invariant under remote setting changes for arbitrary localized instrument families.
5. *Exact boundary on reduced operational models.* A single common source distribution plus only local stochastic post-processing yields a Bell-local family and cannot by itself realize Bell violation.
6. *Exact Bell compatibility at the full-circuit level.* Setting-dependent full-circuit families already present elsewhere in the stack provide explicit Bell-compatible nonfactorizable joint laws with setting-independent local marginals.
7. *Exact finite-benchmark detector-Hamiltonian realization.* Gauge-compatible neutral pointer couplings inside the fixed finite matter-plus-link benchmark of Paper 11 induce exact sector-preserving stochastic instruments after pointer readout.
8. *Exact finite-benchmark localized setting-Hamiltonian realization.* Gauge-compatible localized setting pulses on mixed regions of the same fixed benchmark induce exact sector-preserving stochastic setting-control maps.
9. *Exact boundary-flux structure and partial boundary-flux-resolved detector locality.* On the physical Gauss sector, regional link fluxes satisfy an exact boundary-flux recursion, and for boundary-flux-preserving detector couplings the induced instruments decompose fiberwise over the corresponding boundary-flux sectors.
10. *Exact partial boundary-flux-resolved setting locality for preserving subclasses.* For boundary-flux-preserving localized setting pulses, the induced stochastic setting maps are likewise fiberwise block diagonal on the physical sector.
11. *Exact restricted microscopic Bell bridge on a commuting benchmark family.* For a concrete commuting family of localized setting-plus-detector benchmark maps, the induced joint law already reproduces the operational algebraic structure of Definition 4 together with foliation-order independence and no-signaling.
12. *Exact restricted universality on a commuting-projector benchmark subclass.* Instruments of Definition 11 admit exact microscopic realization by gauge-compatible neutral-pointer benchmark couplings, including boundary-flux-preserving variants.
13. *Exact restricted Bell-1976 screening-off realization.* On the memory-labeled benchmark subclass of Definition 12, local-beables-with-temporal-memory screening-off holds exactly.
14. *Conditional Lorentz-covariant detector/control benchmark theorem.* Under the explicit sufficient-condition package of Theorem 4G, benchmark detector-control layer experiments are foliation compatible and Lorentz-frame independent.
15. *Explicit nonempty restricted benchmark class with worked realization.* The restricted hypotheses are nonvacuous: Proposition 4H gives a nonempty class, and Example 1 exhibits an explicit two-setting/two-outcome finite law computed end-to-end, with no-signaling, screening-off, and Bell-local CHSH bound.
16. *Exact restricted embedding into a setting-dependent full-circuit family.* Theorem 4I gives an explicit setting-indexed full-circuit embedding of the memory-labeled benchmark class whose observed outcome law equals the benchmark law exactly.

Proof.

Item 1 is Definitions 1–4. Item 2 is Theorem A. Item 3 is Proposition 1 and Theorem 1. Item 4 is Theorem 2 together with Corollary 1. Item 5 is Proposition 2. Item 6 is Theorem 3 together with Corollary 2. Item 7 is Proposition 3 together with Theorem 4. Item 8 is Proposition 4 together with Theorem 4B. Item 9 is Proposition 3A together with Theorem 4A. Item 10 is Theorem 4C. Item 11 is Theorem 4D. Item 12 is Theorem 4E. Item 13 is Theorem 4F. Item 14 is Theorem 4G. Item 15 is Proposition 4H together with Example 1. Item 16 is Theorem 4I together with Corollary 3.

$ \square $

What remains outside the present claim is equally important.

1. *No full detector/setting-Hamiltonian universality or full boundary-flux-resolved locality theorem yet.* Theorem 4E gives a restricted universality theorem on a commuting-projector benchmark subclass (including boundary-flux-preserving variants). What remains open is full universality for arbitrary abstract localized controls/instruments of Sections II and III, and full boundary-flux/edge-mode-resolved locality for arbitrary gauge-compatible detector/setting couplings.
2. *No full microscopic bridge theorem yet.* Theorems 4D and 4I give restricted bridge/embedding results for concrete benchmark families. What is still open is the general theorem carrying arbitrary gauge-compatible localized matter-link setting regions and detector couplings all the way to setting-dependent full-circuit Bell families.
3. *No full Bell local-causality theorem in Bell's stronger 1976 sense yet.* Theorem 4F proves screening-off on a restricted memory-labeled benchmark subclass. What remains open is a general local-beables-with-temporal-memory theorem for arbitrary gauge-compatible setting/detector couplings and setting-dependent full-circuit families.
4. *No constructive fully integrable Lorentz-covariant detector field theory yet.* Theorem 4G proves a conditional benchmark theorem under an explicit sufficient-condition package (covariant transformation, spacelike-commuting layers, and adjacent-exchange foliation relation). What remains open is to construct and verify that full integrability package from microscopic detector/control dynamics beyond the restricted benchmark hypothesis, while also resolving the still-open Paper 11 operator-theoretic burdens (compact-rotor theory, larger-benchmark/weighted inverse control, and exact coefficient-derived mixed bond-centered continuum law).

**Strategic remark.**

This is the strongest honest phase-10 paper that the current stack can support. It closes the operational calculus, adds the abstract finite realization theorem together with first exact detector and localized-setting Hamiltonian benchmarks on the fixed matter-link system, identifies the exact boundary-flux obstruction to naive strict factorization, proves first partial boundary-flux-resolved locality theorems for preserving subclasses, proves restricted benchmark theorems for Bell bridge, universality, Bell-1976 screening-off, conditional Lorentz-covariant detector/control compatibility, and restricted full-circuit embedding, together with an explicit nonempty worked benchmark class, and then isolates the remaining full universality / full locality / full bridge / full integrability burdens instead of pretending that they have already been solved.

## Conclusion

Phase 10 should not be read as a generic measurement appendix. It is the point at which the relativistic ISP program becomes operational in the right sense. Controls and detectors are localized bounded-region operations on finite hypersurfaces; disjoint layers compose foliation-compatibly; local marginals obey no-signaling; and the operational model now cleanly distinguishes three different levels that are often blurred together.

The first is the reduced model of a single common source law followed only by local stochastic post-processing. That model is exact, useful, and Bell-local. The second is the setting-dependent full-circuit model in which the settings are themselves active local physical operations. That is where Bell-compatible nonfactorizable laws live in ISP, exactly as the companion entanglement paper already demonstrates, and its CHSH family already rules out any setting-independent Bell-factorizable reduced model. From the Barandes point of view, that distinction is essential. It is the difference between treating settings as real localized dynamics and treating them as terminal labels pasted on afterward. The present paper now adds a third exact layer between those two perspectives: finite microscopic detector and localized-setting benchmarks in which neutral pointer ancillas and gauge-compatible setting pulses are coupled directly to mixed-region operators in the same matter-plus-link system and induce honest stochastic maps at the benchmark level.

So phase 10 now closes the operational bookkeeping and first microscopic detector/setting benchmarks, and adds restricted benchmark theorems for Bell bridge, restricted universality, Bell-1976 screening-off, conditional Lorentz-covariant detector/control compatibility, restricted full-circuit embedding, plus a nonempty explicit benchmark class and worked realization, without overclaiming the full bridge or full integrability theorems. The next remaining burden is sharper than before: upgrade the exact boundary-flux recursion and partial preserving-class fiber theorems to full universality and full boundary-flux-resolved locality for arbitrary gauge-compatible couplings, prove a general Bell-1976 local-beables-with-temporal-memory theorem for the setting-dependent full circuits, and establish a constructive fully integrable Lorentz-covariant detector/control dynamics rather than assuming the Criterion A hypothesis package. On the operator-theoretic side, this still requires the Paper 11 completions deferred so far.

## References

1. [1] Anonymous, “Relativity and Indivisible Stochastic Processes,” architecture draft (2026).
2. [2] Anonymous, “Gauge-Invariant Process Entanglement in Indivisible Stochastic Processes: From ZZ-Gate Phantoms to Bell Inequalities,” companion preprint (2026).
3. [3] Anonymous, “Dynamical Abelian Gauge Field and Gauss-Law Sectors in Relativistic ISP,” preprint (2026).
4. [4] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
5. [5] J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085 (2023; rev. 2026).
6. [6] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192 (2025).
7. [7] J. S. Bell, “On the Einstein Podolsky Rosen Paradox,” *Physics Physique Fizika* **1**, 195–200 (1964).
8. [8] J. S. Bell, “The Theory of Local Beables,” *Epistemological Letters* **9**, 11–23 (1976).
