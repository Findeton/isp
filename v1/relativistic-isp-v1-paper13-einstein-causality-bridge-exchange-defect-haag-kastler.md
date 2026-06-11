# Einstein Causality from Exchange Defects: a Haag-Kastler Bridge for Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

*Induced local operational nets, spacelike exchange triviality, and restricted gauge-benchmark microcausality*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 13 in the relativistic ISP sequence; phase-11 bridge after detector/control dynamics

## Abstract

After the exact free-model exchange-defect papers, the dynamical Abelian gauge benchmark, and the operational detector/control paper, the next honest question in the relativistic ISP program is algebraic rather than merely kinematic or operational. The existing stack already proves exact foliation-compatible composition for spacelike-separated operational layers, exact no-signaling for localized control/readout families, and a restricted microscopic benchmark in which localized setting-plus-detector maps reproduce the same operational algebraic structure on the fixed matter-link system. What is still missing is the precise theorem that connects those results to Einstein causality in the Haag-Kastler sense.

This paper develops that bridge at the strongest scope currently justified. It introduces an induced local operational/algebraic net on the dual effect space of the finite-hypersurface state space and proves an abstract bridge theorem: whenever spacelike-supported localized deformations have trivial exchange defect—or, equivalently at the operational layer, the corresponding localized maps commute—the induced local dynamics is foliation-order independent and the induced local algebras commute. The paper then realizes that theorem exactly in the factorized finite-hypersurface control/readout calculus of Paper 12 and, at restricted benchmark level, on the fixed matter-link Gauss-sector family of Papers 11 and 12 using benchmark-commuting setting/detector maps together with commuting-projector local observable families. On the physical Gauss sector it also records the refinement forced by Gauss law: for boundary-flux-preserving subclasses, locality is fiberwise over shared boundary-flux data rather than naive unfibered tensor-factor locality. Under the explicit sufficient-condition package of the Paper 12 Lorentz theorem, the induced benchmark net is also Lorentz-frame independent. The paper also proves the strongest raw-side structural theorem presently supported by the stack: in every benchmark class where raw comparison maps already satisfy exact quasilocal filtration and inverse control, they generate inverse-closed localized relative-dynamics groups on the state side, and their dual image generates a corresponding induced raw net on the effect side. What is not claimed is an automatic identification of raw comparison maps with Haag-Kastler local observables, an equality between this raw-induced net and the operational benchmark net, or an exact spacelike-commutation theorem for the nontrivial free and gauge raw families themselves. A full Haag-Kastler reconstruction, a quasilocal $C^\ast$-completion, additivity or time-slice theorems, a full arbitrary-coupling microscopic bridge, and the interacting compact-rotor / continuum net all remain outside the present claim. The result is therefore exactly what the present stack can honestly support: a theorem-level bridge from ISP exchange-defect commutativity to Einstein causality for an induced local net, together with a strong raw-side regional group theorem and a clean ledger of the algebraic-QFT burden still remaining beyond that bridge.

Scope note. The exact theorem-level content of this paper is an induced-net construction on the dual effect space of the finite-hypersurface formalism, a strong raw-side regional group theorem for benchmark classes with exact raw filtration and inverse control, an abstract exchange-defect-to-Einstein-causality bridge theorem for spacelike-commuting localized generators, an exact factorized finite-hypersurface realization using the Paper 12 operational calculus, a restricted gauge-benchmark induced net on fixed Gauss sectors built from benchmark-commuting setting/detector maps and commuting-projector local observable families, a fiberwise boundary-flux refinement for preserving subclasses on the physical sector, and a conditional Lorentz-covariant induced-net theorem at that benchmark scope. The induced net is a finite Haag-Kastler-type benchmark object, not a continuum AQFT net. The paper does not claim a direct identification of raw $J_R$ or $E_{R,S}$ with local observable algebras, an equality between the raw-induced net and the operational benchmark net, a full arbitrary-coupling gauge benchmark theorem, a quasilocal or continuum completion of the induced net, isotony/additivity or time-slice axioms, spectrum/energy conditions, compact-rotor or interacting-net reconstruction, or a full Haag-Kastler field theory outside the proved benchmark hypotheses.

## Introduction

The operational phase of the relativistic ISP program changed the question in the right way. Once settings and detectors are treated as localized physical operations supported in bounded spacetime regions, the minimal relativistic demand is no longer a slogan about “covariance somehow.” It is a concrete structural statement: exchanging the order in which a foliation crosses spacelike-separated localized layers should not change the induced predictions. Paper 12 proved that statement exactly in the factorized finite-hypersurface setting and then again, at restricted benchmark level, on the fixed matter-plus-link system.

But that success immediately raises the next question. In algebraic quantum field theory, Einstein causality is not stated directly in terms of transition kernels or operational tables. It is stated as commutativity of local algebras attached to spacelike-separated regions. So if the relativistic ISP stack is to make contact with Haag-Kastler language at all, it must explain how one passes from exchange defects and localized stochastic maps to an induced local net, and exactly what theorem that induced net actually satisfies.

That is the purpose of the present paper. The key point is a separation of levels. The raw localized comparison maps

$$
J_R=\Gamma_R\Gamma_0^{-1}
$$

and their exchange defects

$$
E_{R,S}
=
J_{S|R}J_R\bigl(J_{R|S}J_S\bigr)^{-1}
$$

are algebraic comparison objects, not yet local observable algebras. So the bridge to Einstein causality cannot honestly be the claim that the raw comparison-map commutator is already a Haag-Kastler commutator. The honest statement is weaker and sharper: if spacelike-separated localized deformations exchange trivially, then the *induced* local operational/algebraic net built from the corresponding dual effect-space actions is Einstein-causal. That is the bridge theorem proved here.

That distinction also identifies the strongest raw-side theorem one can honestly try to prove now. It is not a raw observable-identification theorem. The natural raw-side object is the inverse-closed family generated by the localized comparison maps and their inverses, all relative to a common reference slab. Because all such maps act on one fixed finite state space, the right raw-side structure is actually stronger than a merely suggestive pseudogroup slogan: it is a regional subgroup of the invertible linear maps, equipped with the same benchmark quasilocal filtration already proved for the primitive generators. The dual image of that regional group then generates a corresponding induced raw net on the effect space. This formulation is much closer to the actual state of the stack, because inverse control and quasilocal support-growth statements are already proved for the raw maps in the free and fixed-sector gauge benchmarks, whereas Haag-Kastler observable reconstruction is not.

This is exactly the point at which the gauge benchmark matters. In the factorized operational setting, locality is a literal tensor-factor statement. On the physical Gauss sector of the matter-link benchmark, it is not. Paper 12 already proved that the exact physical-sector organization is fiberwise over shared boundary flux. So the correct Paper 13 theorem must recover ordinary induced-net microcausality on the factorized operational hypersurface, but only a boundary-flux-refined version on the gauge benchmark. Anything stronger would ignore the exact obstruction that the previous phase has already isolated.

**Main results (informal).**

1. *Induced-net formulation.* Localized ISP operations admit a natural dual effect-space representation, and support-respecting families of such dual maps generate finite-dimensional local operational/algebraic nets.
2. *Abstract exchange-defect bridge theorem.* If spacelike-supported localized deformations are exchange-trivial—or equivalently the relevant localized maps commute—then induced local dynamics is foliation-order independent and the induced local algebras commute.
3. *Exact factorized realization.* The Paper 12 factorized finite-hypersurface calculus already realizes this bridge exactly: disjoint localized controls/instruments induce commuting local algebras and foliation-independent local dynamics.
4. *Restricted gauge-benchmark realization.* On the fixed matter-link benchmark, a restricted induced net can already be built from benchmark-commuting setting/detector maps and commuting-projector local observable families on each fixed Gauss sector.
5. *Boundary-flux refinement on the physical sector.* For preserving subclasses, the induced gauge-benchmark net is not naively factorwise local but fiberwise Einstein-causal over the admissible shared boundary-flux labels.
6. *Conditional covariance at induced-net level.* Under the explicit sufficient-condition package of the Paper 12 Lorentz theorem, the induced benchmark net transforms covariantly and its Einstein-causality statement is frame independent.
7. *Strong raw-side structural theorem.* At every benchmark scope where raw comparison maps already satisfy exact quasilocal filtration and inverse control, they generate inverse-closed localized relative-dynamics groups, and the dual-generated algebras define a corresponding induced raw net.
8. *Explicit raw-side bridge interpretation.* The bridge to Haag-Kastler Einstein causality applies to that raw-induced net only after dualization and only under a spacelike-commutation hypothesis; it is not an identification of raw comparison maps with local observables, nor a theorem that the nontrivial free/gauge raw families already commute exactly.
9. *Explicit non-claims.* No full quasilocal completion, no time-slice theorem, no arbitrary-coupling gauge bridge, no compact-rotor or interacting continuum net, and no full Haag-Kastler reconstruction are claimed here.

Strategic note. Paper 13 is strongest precisely where the current stack is already strongest: exact finite-hypersurface local commutation, exact foliation compatibility, restricted gauge-benchmark local observable families, conditional Lorentz covariance at benchmark scope, and exact quasilocal/inverse-control structure for raw comparison maps on the benchmarks where those theorems already exist. It is deliberately modest where the stack is still conditional or restricted: raw comparison maps are not yet observables, the raw-induced net is not yet identified with the operational benchmark net, Gauss-law locality is fiberwise rather than naive tensor-factor locality, and full algebraic-QFT reconstruction remains later work.

## Induced local nets on the dual effect space

**Definition 1**

(Finite-hypersurface state space, effect space, and dual localized maps).

For a finite hypersurface configuration space $ \mathcal C_\Sigma $, let
$$
\mathscr S_\Sigma:=\mathbb R^{\mathcal C_\Sigma}
$$
denote the real state space of column vectors, with probability laws as the nonnegative normalized cone inside $ \mathscr S_\Sigma $. Let
$$
\mathscr E_\Sigma:=\operatorname{Hom}(\mathscr S_\Sigma,\mathbb R)\cong\mathbb R^{\mathcal C_\Sigma}
$$
denote the dual effect space of row vectors. For any linear map
$$
T:\mathscr S_{\Sigma_-}\to\mathscr S_{\Sigma_+},
$$
define the dual effect transport
$$
T^\dagger:\mathscr E_{\Sigma_+}\to\mathscr E_{\Sigma_-},
\qquad
T^\dagger e:=e\circ T.
$$
In matrix form relative to the canonical configuration bases,
$$
T^\dagger=T^\top.
$$

Remark.

If $e\in\mathscr E_{\Sigma_+}$ is an outcome effect and $p\in\mathscr S_{\Sigma_-}$ an incoming state, then
$$
e^\top(Tp)=\bigl((T^\dagger e)^\top p\bigr).
$$
So the dual picture is the natural finite-hypersurface Heisenberg picture for the present stochastic setting.

**Definition 2**

(Support-respecting generator assignment and induced Haag-Kastler-type net).

Fix a class of bounded spacetime regions $O$ between chosen hypersurfaces. A

*support-respecting generator assignment*

$$
O\longmapsto \mathcal G(O)\subset \operatorname{End}(\mathscr E_\Sigma)
$$
is a family of effect-space endomorphisms such that:

1. every element of $ \mathcal G(O) $ is induced by a localized map or local effect operator supported in $O$;
2. if $O_1\subset O_2$, then $ \mathcal G(O_1)\subset \mathcal G(O_2) $.

The

*induced local operational/algebraic net*

is the assignment
$$
\mathfrak A^{\mathrm{ind}}(O)
:=
\operatorname{Alg}_1\bigl(\mathcal G(O)\bigr)
\subset
\operatorname{End}(\mathscr E_\Sigma),
$$
the unital real matrix algebra generated by $ \mathcal G(O) $. We say that this induced net satisfies

*Einstein causality*

if for every spacelike-separated pair $O\perp O'$,
$$
[A,B]=0
\qquad
\forall A\in \mathfrak A^{\mathrm{ind}}(O),\;
\forall B\in \mathfrak A^{\mathrm{ind}}(O').
$$

Remark.

This is deliberately a

*Haag-Kastler-type*

finite-scope net, not yet a full quasilocal $C^\ast$-net. At fixed finite benchmark, the natural objects are ordinary finite-dimensional matrix algebras. If one wants a $^\ast$-structure, transpose already supplies the finite-dimensional involution, and one may complexify later. None of the bridge theorems below depend on that later completion.

**Definition 3**

(Spacelike exchange triviality and spacelike commutation).

Let $O\perp O'$ be spacelike-separated localized regions. If the localized family is represented at finite-slab level by comparison maps
$$
J_O,\qquad J_{O'},
$$
relative to a common reference slab, we call the pair

*spacelike exchange trivial*

if the corresponding exchange defect satisfies
$$
E_{O,O'}=I,
$$
equivalently if the two ordered localized deformations induce the same global map. At the operational layer, where one is given localized stochastic maps directly rather than comparison maps, the corresponding condition is exact commutativity of the localized maps. In either language, a support-respecting generator assignment is called

*spacelike commuting*

if for every spacelike-separated pair $O\perp O'$ and every generators
$$
X\in\mathcal G(O),\qquad Y\in\mathcal G(O'),
$$
one has
$$
XY=YX.
$$

Remark.

Definition 3 is the formal point at which the paper separates raw comparison objects from induced local algebras. Exchange-triviality is checked on the deformation side; Einstein causality is concluded only on the induced-net side. The bridge theorem is precisely the implication from the first statement to the second.

**Definition 3A**

(Localized relative-dynamics family generated by raw comparison maps).

Suppose a chosen benchmark or model provides, relative to a common reference slab and in a regime where all relevant inverses exist, a family of invertible localized comparison maps
$$
J_R
$$
on the state side for bounded support regions $R$. For a bounded region $O$, define the

*raw localized relative-dynamics family*

$$
\mathcal P_{\mathrm{rel}}(O)
:=
\{I\}\cup
\Bigl\{
J_{R_1}^{\varepsilon_1}\cdots J_{R_n}^{\varepsilon_n}:
n\ge 1,\;
R_k\subset O,\;
\varepsilon_k\in\{+1,-1\}
\Bigr\}
\subset
\operatorname{GL}(\mathscr S_\Sigma).
$$
Its dual image is
$$
\mathcal G_{\mathrm{rel}}^\dagger(O)
:=
\{W^\dagger: W\in\mathcal P_{\mathrm{rel}}(O)\}
\subset
\operatorname{End}(\mathscr E_\Sigma),
$$
and the corresponding dual-generated induced algebra is
$$
\mathfrak A_{\mathrm{rel}}^{\mathrm{ind}}(O)
:=
\operatorname{Alg}_1\bigl(\mathcal G_{\mathrm{rel}}^\dagger(O)\bigr).
$$

Remark.

Definition 3A states the raw-side structure that can now be turned into a theorem. The raw comparison maps are not themselves local observables; the natural raw-side object is the inverse-closed family they generate under composition. Since all those maps act on one fixed state space, each regional family is in fact a subgroup of the corresponding general linear group. One may still use the looser phrase localized relative-dynamics algebra or pseudogroup for intuition, but the exact finite-scope structure is stronger. The exchange defect measures the failure of a naive commutative regional closure law, while the dual family
$$
\mathcal G_{\mathrm{rel}}^\dagger(O)
$$
lands directly in the induced-net framework of Definition 2. The next theorem isolates exactly how much of that raw-side structure the current stack already proves.

**Theorem A**

(Strong raw relative-dynamics regional group theorem at fixed benchmark scope).

Assume a benchmark class of raw comparison maps on a fixed finite state space $ \mathscr S_\Sigma $ with the following exact properties:

1. for every allowed bounded support region $R$, the comparison map
  $$
  J_R(\Delta)
  $$
  is invertible in a common small-$\Delta$ regime;
2. both
  $$
  J_R(\Delta)=I+\sum_{m\ge 2}\Delta^mA_R^{[m]},
  \qquad
  J_R(\Delta)^{-1}=I+\sum_{m\ge 2}\Delta^m\widetilde A_R^{[m]}
  $$
  admit benchmark-local coefficient filtrations
  $$
  \supp A_R^{[m]}\subset N_m(R),
  \qquad
  \supp \widetilde A_R^{[m]}\subset N_m(R).
  $$
  Here
  $$
  N_m(R)
  $$
  denotes the appropriate $m$-step neighborhood in the chosen benchmark class.

These hypotheses are exactly the free one-particle raw benchmark of Paper 2 and the fixed-sector dynamical Abelian raw benchmark of Paper 11.

Then for every allowed bounded region $O$:

1. *Regional group structure.* The set
  $$
  \mathcal P_{\mathrm{rel}}(O)
  $$
  is an inverse-closed subgroup of
  $$
  \operatorname{GL}(\mathscr S_\Sigma),
  $$
  and the assignment is isotonic:
  $$
  O_1\subset O_2
  \quad\Longrightarrow\quad
  \mathcal P_{\mathrm{rel}}(O_1)\subset\mathcal P_{\mathrm{rel}}(O_2).
  $$
2. *Inherited quasilocal filtration.* Every element
  $$
  W\in\mathcal P_{\mathrm{rel}}(O)
  $$
  admits an expansion
  $$
  W(\Delta)=I+\sum_{m\ge 2}\Delta^mW_O^{[m]}
  $$
  with
  $$
  \supp W_O^{[m]}\subset N_m(O).
  $$
3. *Exact dual-generation of the raw-induced algebra.* The dual family
  $$
  \mathcal G_{\mathrm{rel}}^\dagger(O)
  $$
  is inverse closed, and
  $$
  \mathfrak A_{\mathrm{rel}}^{\mathrm{ind}}(O)
  =
  \operatorname{Alg}_1\bigl(\mathcal G_{\mathrm{rel}}^\dagger(O)\bigr)
  =
  \operatorname{Alg}_1\Bigl(\{J_R^\dagger:\ R\subset O\}\Bigr).
  $$
4. *Conditional Einstein-causal raw-induced net.* If for every spacelike-separated pair
  $$
  O\perp O'
  $$
  the two regional raw families commute pairwise on the state side, then
  $$
  O\longmapsto\mathfrak A_{\mathrm{rel}}^{\mathrm{ind}}(O)
  $$
  is a Haag-Kastler-type induced net satisfying Einstein causality.

Proof.

Item 1 is immediate from Definition 3A: the family is built from finite words in invertible generators and their inverses, so it is a subgroup, and isotony follows from inclusion of allowed regional generators.

For item 2, let
$$
W=K_1\cdots K_n,
$$
where each factor is one of the generators
$$
J_{R_j}^{\pm1}
$$
with
$$
R_j\subset O.
$$
By hypothesis each factor has an expansion with coefficients supported in
$$
N_m(R_j)\subset N_m(O).
$$
The order-$\Delta^m$ coefficient of the product is a finite sum of products of coefficient matrices whose orders add to $m$. The same support-growth argument used in the inverse-stability proofs of Papers 2 and 11 shows that support radii add under matrix composition, so every such product is supported in
$$
N_m(O).
$$
Summing those products gives the claimed filtration for
$$
W.
$$

For item 3, dualization reverses order:
$$
(K_1\cdots K_n)^\dagger=K_n^\dagger\cdots K_1^\dagger,
$$
and takes inverses to inverses. Hence the dual image of the regional group is again inverse closed. Because every dual of a word already lies in the unital algebra generated by the primitive duals
$$
\{J_R^\dagger:\ R\subset O\},
$$
one inclusion is immediate; the reverse inclusion holds because those primitive duals themselves belong to
$$
\mathcal G_{\mathrm{rel}}^\dagger(O).
$$

For item 4, the generator assignment
$$
O\mapsto\mathcal G_{\mathrm{rel}}^\dagger(O)
$$
is isotonic by item 1 and support-respecting in the same benchmark-local sense as item 2. If the regional raw families commute pairwise for spacelike-separated regions, then so do their duals. Theorem 1 below therefore applies to the dualized raw family and yields Einstein causality for the raw-induced net.

$ \square $

## Abstract bridge theorem: from exchange defects to Einstein causality

**Theorem 1**

(Abstract exchange-defect-to-Einstein-causality bridge theorem).

Let
$$
O\longmapsto \mathcal G(O)
$$
be a support-respecting generator assignment on a fixed effect space $ \mathscr E_\Sigma $, and let
$$
O\longmapsto \mathfrak A^{\mathrm{ind}}(O)
$$
be the induced local net of Definition 2. Assume the assignment is spacelike commuting in the sense of Definition 3. Then:

1. *Foliation-order independence for localized dynamics.* For every finite family of pairwise spacelike-separated regions
  $$
  O_1,\dots,O_m
  $$
  and every choice of generators
  $$
  X_k\in\mathcal G(O_k),
  $$
  the ordered product
  $$
  X_{\pi(1)}\cdots X_{\pi(m)}
  $$
  is independent of the permutation $ \pi $. Hence any two foliations related by finitely many adjacent exchanges of such spacelike-separated layers induce the same local dynamics on the effect space.
2. *Isotony.* The induced net is isotonic:
  $$
  O_1\subset O_2
  \quad\Longrightarrow\quad
  \mathfrak A^{\mathrm{ind}}(O_1)\subset \mathfrak A^{\mathrm{ind}}(O_2).
  $$
3. *Einstein causality / induced-net microcausality.* For every spacelike-separated pair $O\perp O'$,
  $$
  [A,B]=0
  \qquad
  \forall A\in\mathfrak A^{\mathrm{ind}}(O),\;
  \forall B\in\mathfrak A^{\mathrm{ind}}(O').
  $$
4. *Bridge interpretation.* If the spacelike commutation hypothesis is verified through exact exchange triviality
  $$
  E_{O,O'}=I
  $$
  of localized comparison maps, then the theorem gives a bridge from ISP exchange-defect commutativity to Einstein causality in the Haag-Kastler sense for the induced local net.

Proof.

Item 1 is immediate from adjacent transpositions. If two neighboring factors in an ordered product come from spacelike-separated regions, they commute by hypothesis. Any permutation is a product of adjacent transpositions, so the ordered product is permutation independent. This is exactly the finite-hypersurface foliation-order statement.

Item 2 follows from the support-respecting hypothesis: if $O_1\subset O_2$, then every generator of $ \mathfrak A^{\mathrm{ind}}(O_1) $ already belongs to $ \mathcal G(O_2) $, hence the algebra it generates is a subalgebra of $ \mathfrak A^{\mathrm{ind}}(O_2) $.

For item 3, choose
$$
A\in\mathfrak A^{\mathrm{ind}}(O),\qquad
B\in\mathfrak A^{\mathrm{ind}}(O').
$$
Each is a finite linear combination of finite words in generators from $ \mathcal G(O) $ and $ \mathcal G(O') $, respectively. Every generator from $ \mathcal G(O) $ commutes with every generator from $ \mathcal G(O') $, so by repeated reordering every such word in $A$ commutes with every such word in $B$. Bilinearity then gives $[A,B]=0$.

Item 4 is just the interpretation of item 3: the deformation-side statement is exchange triviality, while the algebra-side statement is Einstein causality for the induced net. The bridge is the implication between them, not an identification of the two notions.

$ \square $

Remark.

Theorem 1 is the precise bridge statement that the roadmap needs. Theorem A above is the strongest raw-side structural theorem presently earned, and Theorem 1 is what turns that raw-side structure into Einstein causality once a spacelike-commutation hypothesis is available. Neither theorem says that raw comparison maps

*are*

Haag-Kastler local observables.

**Corollary 1**

(Dualization preserves the spacelike commutation hypothesis).

If a spacelike-separated localized family is given on the state side by commuting maps
$$
T_O T_{O'}=T_{O'} T_O,
$$
then the corresponding dual generators also commute:
$$
T_O^\dagger T_{O'}^\dagger
=
T_{O'}^\dagger T_O^\dagger.
$$

Proof.

Take transposes:
$$
T_O^\dagger T_{O'}^\dagger
=
(T_O T_{O'})^\top
=
(T_{O'} T_O)^\top
=
T_{O'}^\dagger T_O^\dagger.
$$
So the same spacelike commutation statement holds in the induced Heisenberg picture.

$ \square $

## Exact factorized operational realization

The abstract bridge theorem becomes exact immediately on the factorized finite-hypersurface operational calculus of Paper 12. There the localized setting and detector maps are literally tensor-factor maps on

$$
\mathbb R^{\mathcal C_A}\otimes
\mathbb R^{\mathcal C_B}\otimes
\mathbb R^{\mathcal C_R},
$$

so the support-level commutation hypothesis is already a proved theorem rather than a heuristic expectation.

**Definition 4**

(Factorized operational generator family).

In the factorized setting of Paper 12, let $O$ be one of the localized operational wings or, more generally, one of the disjoint factors crossed by a localized operational layer. Let
$$
\mathcal G_{\mathrm{fac}}(O)
$$
be the family of dual endomorphisms generated by the transposes of the localized control maps and localized detector-instrument maps supported in $O$:
$$
\widehat\Lambda_O^{x\,\dagger},
\qquad
\widehat{\mathcal J}_O^{a|x\,\dagger},
$$
optionally enlarged by any local event projectors or local readout multipliers supported in the same factor. Define
$$
\mathfrak A_{\mathrm{fac}}^{\mathrm{ind}}(O)
:=
\operatorname{Alg}_1\bigl(\mathcal G_{\mathrm{fac}}(O)\bigr).
$$

**Theorem 2**

(Exact factorized finite-hypersurface Einstein-causality bridge).

In the setting of Definition 4:

1. the family
  $$
  O\longmapsto \mathfrak A_{\mathrm{fac}}^{\mathrm{ind}}(O)
  $$
  is an isotonic induced local net;
2. for spacelike-separated operational factors $O\perp O'$,
  $$
  [A,B]=0
  \qquad
  \forall A\in\mathfrak A_{\mathrm{fac}}^{\mathrm{ind}}(O),\;
  \forall B\in\mathfrak A_{\mathrm{fac}}^{\mathrm{ind}}(O');
  $$
3. any two foliations differing only by the order in which they cross those spacelike-separated localized operational regions induce the same conditioned and unconditioned local dynamics;
4. the induced local marginals obey no-signaling.

Proof.

Paper 12, Proposition 1 proves exact commutativity of disjoint localized instruments and controls on distinct factors. By Corollary 1 above, the same commutation holds for their dual effect-space actions. Therefore the generator assignment of Definition 4 is spacelike commuting. Theorem 1 then gives items 1–3.

For item 4, Theorem 2 of Paper 12 already proves no-signaling for the localized operational joint law. Rewriting that law in the dual picture does not change the scalar probabilities, so the same no-signaling statement holds for the induced local dynamics.

$ \square $

Remark.

Theorem 2 is the cleanest exact realization of the bridge. It is already a finite-scope Haag-Kastler-type result: isotony, Einstein causality, and foliation-order independence all hold exactly. What it is

*not*

yet is a field-theoretic reconstruction theorem, because the factorized operational setting was never intended to solve the Gauss-law and continuum burdens by itself.

## Restricted gauge-benchmark induced net and boundary-flux refinement

The fixed matter-link benchmark is the real test of whether the bridge can survive beyond naive tensor-factor locality. Paper 11 and Paper 12 together already isolate the correct answer. Exact gauge-compatible localized setting and detector maps exist on each fixed finite Gauss sector, but on the physical sector naive strict factorwise locality is replaced by a fiber decomposition over shared boundary electric flux. So the correct Paper 13 bridge theorem on the gauge benchmark must be restricted and fiberwise where necessary.

**Definition 5**

(Restricted benchmark local generator family on a fixed Gauss sector).

Fix $L$, $S$, a compatible Gauss sector $ \mathbf g $, and a gauge-compatible mixed region $R$. Let
$$
\mathscr E_{L,S}^{(\mathbf g)}
:=
\bigl(\mathbb R^{\Omega_{L,S}^{(\mathbf g)}}\bigr)^\ast
$$
be the sector effect space. Define the

*restricted benchmark generator family*

$$
\mathcal G_{\mathbf g}^{\mathrm{bench}}(R)
\subset
\operatorname{End}\bigl(\mathscr E_{L,S}^{(\mathbf g)}\bigr)
$$
to be generated by the following operators whenever they are present in the chosen restricted benchmark class:

1. the dual benchmark setting/detector maps
  $$
  \bigl(\mathcal I_{R,\mathbf g}^{a|x,(S)}\bigr)^\dagger
  =
  \bigl(\mathcal I_{R,\mathbf g}^{a|x,(S)}\bigr)^\top;
  $$
2. the spectral projectors
  $$
  \Pi_\zeta^{(R,\mathbf g)}
  $$
  from a commuting gauge-invariant local observable family of Definition 11 in Paper 12;
3. on the physical sector and for preserving subclasses, the boundary-flux projectors
  $$
  P_{R,\lambda}^{\partial}.
  $$

Set
$$
\mathfrak A_{\mathbf g}^{\mathrm{bench}}(R)
:=
\operatorname{Alg}_1\bigl(\mathcal G_{\mathbf g}^{\mathrm{bench}}(R)\bigr).
$$

Remark.

Definition 5 deliberately mirrors the exact restricted theorems of Paper 12. The setting/detector maps come from the benchmark Bell family of Definition 10, the local projectors come from the commuting-projector subclass of Definition 11, and the fiberwise refinement comes from the boundary-flux projectors of Definition 8A together with the preserving theorems 4A and 4C there.

**Theorem 3**

(Restricted gauge-benchmark Einstein-causality bridge theorem).

Fix two disjoint gauge-compatible mixed regions
$$
R_A\perp R_B
$$
on a chosen compatible Gauss sector $ \mathbf g $. Assume:

1. the benchmark-commuting hypothesis of Definition 10 in Paper 12 holds for the included setting/detector maps on $R_A$ and $R_B$;
2. the included local observable families on $R_A$ and $R_B$ belong to the commuting-projector class of Definition 11 in Paper 12 and are chosen so that the cross-wing projector generators commute;
3. if the physical-sector fiberwise refinement is claimed, then the chosen setting/detector subclass is boundary-flux preserving in the sense of Theorems 4A and 4C of Paper 12.

Then:

1. the restricted benchmark induced algebras commute:
  $$
  [A,B]=0
  \qquad
  \forall A\in\mathfrak A_{\mathbf g}^{\mathrm{bench}}(R_A),\;
  \forall B\in\mathfrak A_{\mathbf g}^{\mathrm{bench}}(R_B);
  $$
2. the induced benchmark local dynamics is foliation-order independent under exchanges of the spacelike-separated layer regions $R_A$ and $R_B$;
3. the corresponding joint laws retain the no-signaling property proved in Paper 12;
4. if $ \mathbf g=\mathbf g_{\mathrm{phys}} $ and the preserving hypotheses of item 3 hold, then each induced algebra is block diagonal over the admissible boundary-flux fibers and the Einstein-causality statement holds fiberwise on every common boundary-flux block.

Proof sketch.

Item 1 is a generator-by-generator statement. For the benchmark setting/detector maps, Theorem 4D of Paper 12 gives exact cross-wing commutation. For the commuting-projector observable families, the cross-wing generators commute by the explicit hypothesis of the present theorem. On the physical sector, the boundary-flux projectors are diagonal projectors on the sector basis and hence commute with one another; by Theorems 4A and 4C of Paper 12, the preserving subclasses are block diagonal with respect to those projectors. Therefore every generator in
$$
\mathcal G_{\mathbf g}^{\mathrm{bench}}(R_A)
$$
commutes with every generator in
$$
\mathcal G_{\mathbf g}^{\mathrm{bench}}(R_B),
$$
and the generated algebras commute.

Item 2 follows exactly as in Theorem 1: adjacent exchanges of commuting benchmark layers do not change the ordered product. Item 3 is already part of Theorem 4D in Paper 12 and is unchanged by passing to the induced effect-space picture.

For item 4, Theorems 4A and 4C give fiberwise block diagonality for the relevant detector and setting subclasses on the physical sector, while Definition 8A provides the projectors $P_{R,\lambda}^{\partial}$. Therefore the induced algebra decomposes over those admissible blocks, and the same commuting-generator argument applies on each block separately.

$ \square $

Remark.

Theorem 3 is already enough to justify the roadmap language “bridge to Haag-Kastler” at the benchmark level. What it does

*not*

justify is a claim that the full physical Gauss sector factorizes into independent regional tensor factors. The benchmark microcausality theorem is fiberwise where Gauss law says it must be fiberwise.

**Corollary 2**

(Restricted induced-net microcausality on the commuting-projector benchmark subclass).

On the restricted benchmark class generated by benchmark-commuting setting/detector maps and commuting-projector local observable families, the fixed-sector assignment
$$
R\longmapsto \mathfrak A_{\mathbf g}^{\mathrm{bench}}(R)
$$
is an induced Haag-Kastler-type local net satisfying Einstein causality at the exact finite benchmark scope proved here.

Proof.

Isotony is inherited from the support-respecting choice of local generator families, and Theorem 3 supplies Einstein causality. That is exactly the claimed restricted induced-net statement.

$ \square $

## Conditional Lorentz covariance at induced-net level

Einstein causality in the Haag-Kastler sense is usually discussed together with covariance. The present stack does not yet have a constructive full covariance theorem for arbitrary couplings, but Paper 12 does provide an explicit sufficient-condition package at benchmark scope. The induced-net version is immediate once the generators are transported to the dual side.

**Definition 6**

(Dual Lorentz transport and induced-net covariance at benchmark scope).

Assume the Lorentz-covariant transport maps
$$
U_\Lambda^\Sigma
$$
of Definition 3 in the architecture paper exist on the state side. Define the dual transport on the effect space by
$$
U_\Lambda^{\Sigma\,\dagger}
:=
\bigl(U_\Lambda^\Sigma\bigr)^\top.
$$
An induced benchmark net is called

*covariant at benchmark scope*

if for every localized region $O$ in the allowed benchmark class,
$$
U_\Lambda^{\Sigma\,\dagger}
\mathfrak A^{\mathrm{ind}}(O)
\bigl(U_\Lambda^{\Sigma\,\dagger}\bigr)^{-1}
=
\mathfrak A^{\mathrm{ind}}(\Lambda O).
$$

**Theorem 4**

(Conditional Lorentz-covariant induced-net theorem at benchmark scope).

Assume the four explicit hypotheses of Theorem 4G in Paper 12:

1. Lorentz-covariant transport on the state side;
2. covariant transformation of the benchmark detector/control generators;
3. spacelike commutation of the benchmark layer maps;
4. foliations related by finitely many adjacent exchanges of spacelike-separated neighboring layers.

Then for the induced benchmark net generated by those covariantly transforming local generators:

1. the induced benchmark net is covariant in the sense of Definition 6;
2. its Einstein-causality statement is Lorentz-frame independent on the benchmark class considered;
3. the corresponding benchmark probabilities are foliation compatible in every frame related by the allowed Lorentz transformations.

Proof sketch.

Theorem 4G of Paper 12 already proves foliation compatibility and Lorentz-frame independence of the benchmark experiment law under the stated explicit sufficient-condition package. Hypothesis (2) there says precisely that the benchmark localized generators transform covariantly. Taking duals preserves those conjugation relations, so the corresponding induced generator families are mapped to one another by
$$
U_\Lambda^{\Sigma\,\dagger}(\cdot)\bigl(U_\Lambda^{\Sigma\,\dagger}\bigr)^{-1}.
$$
Therefore the generated local algebras transform covariantly as well, giving item 1. Item 2 follows because commuting algebras are carried to commuting algebras under conjugation, and item 3 is just the probability statement of Theorem 4G restated in the induced-net picture.

$ \square $

Remark.

Theorem 4 is conditional for exactly the same reason Theorem 4G is conditional. It is not a constructive full Lorentz-covariant field-theory theorem, and it certainly does not yet prove the time-slice or primitive-causality package of a fully developed Haag-Kastler net.

## Exact phase-11 closure and the remaining Haag-Kastler burden

With the bridge formulated this way, Paper 13 can now be stated cleanly at the strongest honest scope presently justified.

**Theorem 5**

(Exact phase-11 closure at the presently justified bridge scope).

At the presently justified bridge scope, phase 11 is closed in the following exact sense.

1. *Induced-net formulation.* Localized ISP maps admit a natural dual effect-space picture and support-respecting families of such generators define induced local operational/algebraic nets.
2. *Strong raw-side regional group theorem.* On every benchmark class where raw comparison maps already satisfy exact quasilocal filtration and inverse control, they generate inverse-closed localized relative-dynamics groups whose dual image defines a raw-induced net.
3. *Abstract bridge theorem.* Spacelike exchange triviality / commuting localized maps imply foliation-order independence of the induced local dynamics and Einstein causality for the induced local net.
4. *Exact factorized realization.* The Paper 12 factorized finite-hypersurface control/readout calculus realizes the bridge theorem exactly.
5. *Restricted fixed-sector gauge realization.* On each fixed compatible Gauss sector of the Paper 11 benchmark, benchmark-commuting setting/detector maps plus commuting-projector local observable families generate a restricted induced local net satisfying Einstein causality.
6. *Physical-sector fiberwise refinement.* For boundary-flux-preserving subclasses on the physical sector, the induced gauge-benchmark net is Einstein-causal fiberwise over the admissible shared boundary-flux blocks.
7. *Conditional induced-net covariance.* Under the explicit sufficient-condition package of Paper 12, the induced benchmark net is Lorentz covariant and its Einstein-causality statement is frame independent.

Proof.

Item 1 is Definitions 1 and 2. Item 2 is Theorem A. Item 3 is Theorem 1 together with Corollary 1. Item 4 is Theorem 2. Item 5 is Theorem 3 together with Corollary 2. Item 6 is item 4 of Theorem 3. Item 7 is Theorem 4.

$ \square $

What remains outside the present claim is equally important.

1. *No raw-comparison-map identification theorem yet.* The paper does not prove that the primitive comparison maps $J_R$ or exchange defects $E_{R,S}$ are themselves Haag-Kastler local observables.
2. *No theorem that the raw-induced net equals the operational benchmark net yet.* The strong raw-side theorem constructs a corresponding dual-generated raw net. It does not identify that raw net with the operational induced net generated later from localized setting/detector maps and commuting-projector observable families.
3. *No exact raw spacelike-commutation theorem for the nontrivial free/gauge benchmarks yet, and no genuine nontrivial raw exception class is supported by the present stack.* The strong raw-side theorem proves regional group structure and inherited filtration, but the active free, static-$U(1)$, and fixed-sector dynamical-gauge comparison families already contain explicit disjoint-support nonzero raw exchange at benchmark level. So the only exact raw commuting classes presently supported are the ideal factorized/local case and degenerate support-frozen or otherwise trivial cases; the commuting-projector subclasses of Paper 12 are operational benchmark families rather than raw comparison-map exceptions.
4. *No full arbitrary-coupling microscopic bridge yet.* The gauge-benchmark theorem still depends on the restricted benchmark-commuting and commuting-projector families of Paper 12. Full arbitrary-coupling universality and full microscopic bridge theorems remain open.
5. *No unfibered physical-sector locality theorem yet.* On the physical Gauss sector, the exact locality statement remains boundary-flux refined for the preserving subclasses. The paper does not erase that obstruction by vocabulary.
6. *No full Haag-Kastler reconstruction yet.* The paper does not provide additivity, primitive causality, time-slice, quasilocal completion, or a full interacting local net on the continuum side.
7. *No compact-rotor or interacting continuum net yet.* The compact-rotor tower, larger-benchmark inverse-control burden, and later genuinely interacting gauge-matter benchmark remain future work.
8. *No non-Abelian extension yet.* The bridge is built only at the current Abelian operational/gauge scope already established in Papers 11 and 12.

**Strategic remark.**

This is the strongest honest Paper 13 that the present stack can support. It upgrades exact spacelike commutation from an operational bookkeeping fact to an induced-net Einstein-causality theorem, but it does so without pretending that the full Haag-Kastler machine has already been reconstructed from the stochastic side.

## Conclusion

The right conceptual gain of Paper 13 is narrow but real. The earlier papers already showed that localized ISP dynamics can be organized on finite hypersurfaces, that disjoint operational layers commute, and that the fixed matter-link benchmark admits nontrivial local setting and detector maps with restricted benchmark commutation. What they did not yet say is how those results should be read in algebraic-QFT language. The present paper supplies that reading.

The bridge is not a slogan and not an identity claim. It is an induced-net theorem. Exchange-defect triviality or, operationally, exact commutation of localized spacelike-separated layers implies that the dual local dynamics is foliation-order independent and that the induced local algebras commute. In the factorized operational calculus this statement is exact outright. On the gauge benchmark it survives in the restricted form already earned by the previous papers: fixed Gauss sectors, benchmark-commuting setting/detector maps, commuting-projector local observable families, and fiberwise boundary-flux refinement where Gauss law requires it.

That is the right Barandes-style phase-11 outcome. The paper now closes the first Einstein-causality bridge theorem that the stack can honestly support, and it also closes the strongest raw-side structural theorem that the current stack can really earn: at the benchmarks where exact raw filtration and inverse control already exist, the localized comparison maps generate inverse-closed regional relative-dynamics groups, and their dual image generates a corresponding raw-induced net. What remains is now sharper rather than vaguer. The present evidence does not support a hidden nontrivial exact raw commuting subclass: outside the ideal factorized/local case and degenerate support-frozen trivialities, the active free and gauge raw benchmarks already exhibit explicit disjoint-support nonzero raw exchange. So the next burden is not to guess a raw structure or to relabel an operational commuting subclass as a raw exception, but to determine whether a deeper no-go theorem can be proved, whether the raw-induced net coincides with the operational benchmark net on the classes already controlled, and how much of the full time-slice / covariance / quasilocal-completion package the ISP side can actually earn rather than borrow by analogy.

## References

1. [1] Anonymous, “Relativity and Indivisible Stochastic Processes,” architecture draft (2026).
2. [2] Anonymous, “Exact Localized Finite Deformations and the Free Dirac Exchange-Defect Theorem,” preprint (2026).
3. [3] Anonymous, “Dynamical Abelian Gauge Field and Gauss-Law Sectors in Relativistic ISP,” preprint (2026).
4. [4] Anonymous, “Localized Controls, Detectors, and Operational Relativity in Relativistic ISP,” preprint (2026).
5. [5] R. Haag and D. Kastler, “An Algebraic Approach to Quantum Field Theory,” *Journal of Mathematical Physics* **5**, 848–861 (1964).
6. [6] R. Brunetti, K. Fredenhagen, and R. Verch, “The Generally Covariant Locality Principle—A New Paradigm for Local Quantum Physics,” *Communications in Mathematical Physics* **237**, 31–68 (2003).
7. [7] J. Schwinger, “The Theory of Quantized Fields. I,” *Physical Review* **82**, 914–927 (1951).
8. [8] P. A. M. Dirac, “The Hamiltonian Form of Field Dynamics,” *Canadian Journal of Mathematics* **3**, 1–23 (1951).
9. [9] S. G. Brown, “Dirac-Schwinger Covariance Condition in Canonical Theories,” *Physical Review* **158**, 1608–1626 (1967).
10. [10] S. Fedida, “Einstein Causality of Quantum Measurements in the Tomonaga-Schwinger Picture,” *Annals of Physics* **485**, 170314 (2026).
