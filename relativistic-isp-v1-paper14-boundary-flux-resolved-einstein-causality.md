# Boundary-Flux-Resolved Einstein Causality in Relativistic ISP

*Exact physical-sector gluing, extended regional configuration spaces, and center-resolved locality on the finite matter-link benchmark*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Proposed interposed bridge-refinement paper after Paper 13 and before the roadmap interacting gauge-matter benchmark

## Abstract

The preceding operational and bridge papers already isolate the exact obstruction to naive locality on the fixed finite matter-link benchmark of relativistic ISP: on the physical Gauss sector, regional data do not generically factor as unconstrained tensor-product data, but are fibered over shared boundary electric-flux labels. The present paper turns that obstruction into the next exact theorem. In the Barandes spirit, the analysis stays at the level of ordinary finite configuration spaces and stochastic maps, rather than importing auxiliary Hilbert-space structure as primary.

For a connected mixed region we define an extended regional configuration space carrying local matter data, interior link-flux data, and the two cut-boundary electric-flux labels. We then prove that the global physical-sector configuration space is canonically a fiber product of the corresponding extended regional spaces over matching boundary-flux data. For the boundary-flux-preserving detector and setting subclasses already isolated in the operational benchmark paper, the induced stochastic maps preserve the relevant boundary-label fibers and descend to exact regional maps on those extended spaces. This yields a finite abelian boundary-flux center, and the correct induced local net on the benchmark is therefore not naively unfibered but center resolved: on each admissible joint boundary-flux block the regional induced algebras commute exactly, and after compression to any fixed admissible joint block one recovers an ordinary finite benchmark local net satisfying Einstein causality outright on that block. In this precise sense the benchmark theory is Einstein-causal relative to the joint boundary-flux center.

The paper therefore strengthens the phase-11 Haag-Kastler bridge at the exact scope already earned by the stack, while making explicit what it still does not claim: no identification of raw comparison maps with observables, no nontrivial exact raw commuting theorem for the active free or gauge comparison-map families, no arbitrary-coupling universality beyond the preserving subclasses, and no compact-rotor, continuum, interacting, or non-Abelian completion. The gain is narrower and firmer: the physical Gauss sector does not fail locality; it fails naive factorization, and the exact boundary data required to repair locality are now made explicit.

Scope note. The theorem-level content of this paper is the exact obstruction to naive physical-sector factorization, the definition of extended regional configuration spaces with boundary flux labels, the exact gluing theorem on the fixed finite benchmark, the induced finite abelian boundary-flux center, the exact regional action of boundary-flux-preserving detector/setting subclasses on the extended spaces, the corresponding center-resolved Einstein-causality theorem for the induced benchmark net, and the blockwise reduction to ordinary finite benchmark local nets on fixed admissible joint boundary-flux sectors. This is the finite ISP analogue of the standard gauge-theory lesson that electric centers, edge/boundary data, and superselection sectors must be handled explicitly before locality is formulated. The paper does not claim a raw observable-identification theorem, a nontrivial exact raw commuting class, arbitrary-coupling universality, compact-rotor or continuum completion, or an interacting gauge-matter extension.

## Introduction

The phase ordering of the relativistic ISP program has become sharper with each paper. The architecture paper identified localized finite deformations and their exchange defect as the right relativistic integrability datum. The exact free-model papers then isolated quasilocal filtration, exact comparison-map coefficients, and the first exchange-defect theorems. The gauge papers enlarged the benchmark from matter alone to matter plus dynamical link variables, and the operational paper inserted localized settings and detectors into the same finite-hypersurface framework. The bridge paper then showed that, once localized maps commute at the appropriate operational or induced level, one obtains a genuine Einstein-causality theorem for an induced local net.

But the same sequence also made a negative fact exact. On the physical Gauss sector of the finite matter-link benchmark, the correct microscopic locality target is not naive tensor-factor locality. The reason is not interpretive looseness. It is a literal recursion theorem: local matter occupation data on a connected region do not fix the interior link-flux profile unless one also supplies cut-boundary electric-flux data. So the physical-sector configuration space is organized into fibers over boundary flux labels rather than as an unconstrained regional product. The operational paper stated this explicitly and proved first preserving-class fiber theorems. The bridge paper then incorporated the point only as a refinement clause.

The purpose of the present paper is to promote that refinement into the main theorem. The correct next question is not whether the active raw comparison-map families secretly commute after all; the present stack already contains explicit nonzero disjoint-support raw exchange in the free and gauge benchmarks. Nor is the next question yet a continuum $C^\ast$-completion or an interacting compact-rotor theory. The right next question is simpler and more structural: what are the correct regional configuration spaces on which locality should be formulated, once Gauss law is imposed exactly?

The answer developed here is configuration-space level and finite. For a connected mixed region one must include not just regional matter and interior link data, but also the cut-boundary electric-flux labels. These form an extended regional configuration space. The first theorem then shows that the global physical-sector configuration space is canonically a fiber product of such extended regional spaces over matching boundary data. Once that is done, the boundary-flux-preserving detector and setting subclasses already isolated in the operational paper become honest regional maps on the extended spaces, and the corresponding induced local algebras commute fiberwise over a finite abelian center generated by the boundary-flux projectors.

This is the precise sense in which the present paper refines the phase-11 bridge. It does not broaden the raw scope. It sharpens the benchmark locality statement. The physical Gauss sector does not fail Einstein causality; it fails the stronger and wrong statement that the relevant local degrees of freedom were already unconstrained tensor-factor data before the boundary information was supplied.

The dependence on earlier exact results is correspondingly narrow. Proposition 1 below is a direct repackaging of the exact boundary-flux recursion of Paper 12, Proposition 3A. The preserving hypotheses used later are exactly the boundary-flux-preserving detector and setting hypotheses of Paper 12, Definition 8A and Theorems 4A and 4C. The final induced-net interpretation is designed to sharpen the physical-sector refinement clause already present in the restricted gauge-benchmark bridge theorem of Paper 13, rather than to replace its benchmark assumptions by new ones.

**Main results (informal).**

1. *Exact obstruction.* Naive unfibered regional factorization fails on the physical Gauss sector because the interior link-flux profile requires boundary-flux seeds.
2. *Extended regional spaces.* The correct regional object is an extended configuration space carrying local matter data, interior link data, and boundary flux labels.
3. *Exact gluing.* The physical-sector configuration space is canonically a fiber product of such regional spaces over matching boundary-flux labels.
4. *Regional action of preserving subclasses.* Boundary-flux-preserving detector and setting maps descend to exact regional stochastic maps on the extended spaces.
5. *Boundary-flux center.* The corresponding boundary-flux projectors generate a finite abelian center over which the induced benchmark net decomposes.
6. *Center-resolved Einstein causality.* On each admissible joint boundary-flux block, the regional induced algebras commute exactly; equivalently, the benchmark net is Einstein-causal relative to the boundary-flux center.
7. *Blockwise ordinary local nets.* Compressing to any fixed admissible joint boundary-flux block yields an ordinary finite benchmark local net satisfying Einstein causality outright on that block.

Strategic note. The paper is strongest exactly where the stack is already strongest: finite benchmark configuration spaces, exact boundary-flux recursion, exact preserving-class block diagonality, and exact induced-net locality at restricted benchmark scope. It is deliberately noncommittal where the present stack remains restricted or open.

## Exact obstruction to naive physical-sector factorization

We begin by isolating the structural point that motivates the whole paper. The operational benchmark already proved that on the physical Gauss sector the regional link-flux profile is determined recursively only after one supplies cut-boundary flux data. The first proposition simply repackages that fact as a no-go theorem for naive unfibered factorization.

**Proposition 1**

(Exact obstruction to naive unfibered regional factorization).

Fix the finite matter-link benchmark of the dynamical Abelian gauge paper, the background charges
$$
(\rho_n^{\mathrm{bg}})_n,
$$
the physical Gauss datum
$$
\mathbf g_{\mathrm{phys}},
$$
and a connected site interval
$$
I=\{n_-,n_-+1,\dots,n_+\}.
$$
Let
$$
\omega=(X,\mathbf m)
$$
be a physical-sector basis configuration, with site occupation numbers
$$
N_n(X):=\sum_s \mathbf 1_{(n,s)\in X}
$$
and link fluxes
$$
\mathbf m=(m_{1/2},m_{3/2},\dots,m_{L-1/2}).
$$
Then the physical Gauss law implies the exact recursion
$$
m_{n+1/2}
=
m_{n-1/2}-N_n(X)+\rho_n^{\mathrm{bg}}-g_n^{\mathrm{phys}}
$$
for every site $n$, hence
$$
m_{n+1/2}
=
m_{n_- -1/2}
-\sum_{j=n_-}^{n}\bigl(N_j(X)-\rho_j^{\mathrm{bg}}+g_j^{\mathrm{phys}}\bigr).
$$
and therefore
$$
m_{n_- -1/2}-m_{n_+ +1/2}
=
\sum_{j=n_-}^{n_+}\bigl(N_j(X)-\rho_j^{\mathrm{bg}}+g_j^{\mathrm{phys}}\bigr).
$$
Consequently the interior link-flux profile on $I$ is determined by the matter data on $I$ only after one supplies a boundary-flux seed. In particular, the physical-sector regional data on $I$ do not canonically factor as unconstrained tensor-product data independent of the surrounding cut-boundary flux.

Proof.

This is the exact boundary-flux recursion already isolated at benchmark level in Paper 12, Proposition 3A. The displayed one-step relation is just the Gauss-law eigenvalue equation rearranged to solve for the outgoing link flux. Iterating it from the left cut link proves the second formula, and setting $n=n_+$ gives the boundary-difference identity. The last sentence follows immediately: fixing only the matter occupation data on $I$ leaves the interior link profile undetermined whenever multiple admissible boundary seeds are compatible with the finite cutoff. Therefore the regional physical-sector data are fibered over boundary-flux labels rather than canonically unconstrained product data.

$ \square $

Remark.

Proposition 1 is the exact reason the present paper is needed. The benchmark locality problem is not “prove strict product factorization anyway.” The benchmark locality problem is “formulate locality on the correct regional spaces once strict product factorization has already been proved false.”

## Extended regional configuration spaces

The proposition above suggests the correct regional object. One should keep the ordinary configuration-space viewpoint but enlarge each regional configuration by the minimal boundary data needed to reconstruct the interior link profile.

**Definition 1**

(Connected mixed region and cut-boundary labels).

Let $R$ be a gauge-compatible mixed region whose site set is a connected interval
$$
V_R=\{n_-,n_-+1,\dots,n_+\}.
$$
The two cut-boundary links of $R$ are
$$
n_- - \tfrac12,
\qquad
n_+ + \tfrac12.
$$
For a physical-sector configuration
$$
\omega=(X,\mathbf m),
$$
define the boundary-flux label
$$
\partial\Phi_R(\omega)
:=
\bigl(m_{n_- -1/2},\,m_{n_+ +1/2}\bigr).
$$
Let
$$
\Lambda_\partial(R)
$$
denote the set of admissible such labels on the physical sector.

**Definition 2**

(Extended regional configuration space).

Fix the physical Gauss datum
$$
\mathbf g_{\mathrm{phys}}.
$$
The extended regional configuration space of $R$ is
$$
\Omega_R^{\mathrm{ext}}
$$
consisting of tuples
$$
\eta_R=
\bigl(X_R,\mathbf m_R^{\mathrm{int}},\lambda_-,\lambda_+\bigr)
$$
such that:

1. $X_R$ is a matter occupation configuration on the sites of $R$;
2. $\mathbf m_R^{\mathrm{int}}$ is an interior link-flux profile on the links fully contained in $R$;
3. $(\lambda_-,\lambda_+)\in\Lambda_\partial(R)$ is an admissible boundary-flux label;
4. the local data satisfy the physical Gauss recursion on every site of $R$ with incoming seed $\lambda_-$ and outgoing boundary value $\lambda_+$.

For fixed admissible boundary label $\lambda=(\lambda_-,\lambda_+)$, write
$$
\Omega_{R,\lambda}^{\mathrm{ext}}
\subset
\Omega_R^{\mathrm{ext}}
$$
for the corresponding fiber.

Remark.

For a connected interval the interior link profile is already determined recursively by $X_R$ together with one boundary seed. We nevertheless keep both cut labels as part of the regional datum because gluing two regional spaces requires a symmetric interface language rather than an asymmetric seed language.

**Definition 3**

(Complementary extended space and matching boundary data).

For the complementary mixed region $R^c$ on the same periodic ring, define
$$
\Omega_{R^c}^{\mathrm{ext}}
$$
and its admissible boundary-label map analogously. Write
$$
\pi_R:\Omega_R^{\mathrm{ext}}\to\Lambda_\partial(R),
\qquad
\pi_{R^c}:\Omega_{R^c}^{\mathrm{ext}}\to\Lambda_\partial(R)
$$
for the corresponding label maps, where the two cut links are identified in the obvious geometric way. The fiber product of the two extended spaces over matching boundary data is
$$
\Omega_R^{\mathrm{ext}}
\times_{\Lambda_\partial(R)}
\Omega_{R^c}^{\mathrm{ext}}
:=
\bigl\{
(\eta_R,\eta_{R^c}) :
\pi_R(\eta_R)=\pi_{R^c}(\eta_{R^c})
\bigr\}.
$$

## Exact physical-sector gluing theorem

The next theorem states the basic structural replacement for naive product factorization. The global physical-sector configuration space is not a direct product of regional spaces, but it is an exact fiber product of the extended regional spaces just defined.

**Theorem 1**

(Exact gluing of the physical sector by boundary flux).

Fix the finite matter-link benchmark, the physical Gauss datum
$$
\mathbf g_{\mathrm{phys}},
$$
and a connected mixed region $R$ with complementary region $R^c$. Then the physical-sector configuration space
$$
\Omega_{\mathrm{phys}}
:=
\Omega_{L,S}^{(\mathbf g_{\mathrm{phys}})}
$$
is canonically isomorphic to the fiber product
$$
\Omega_{\mathrm{phys}}
\cong
\Omega_R^{\mathrm{ext}}
\times_{\Lambda_\partial(R)}
\Omega_{R^c}^{\mathrm{ext}}.
$$
Equivalently, a physical-sector configuration is exactly the same thing as a pair of compatible extended regional configurations with matching cut-boundary flux labels.
Moreover, for each admissible label
$$
\lambda\in\Lambda_\partial(R),
$$
the fixed-label block
$$
\Omega_{\mathrm{phys},\lambda}(R)
:=
\{\omega\in\Omega_{\mathrm{phys}}:\partial\Phi_R(\omega)=\lambda\}
$$
is canonically isomorphic to
$$
\Omega_{R,\lambda}^{\mathrm{ext}}
\times
\Omega_{R^c,\lambda}^{\mathrm{ext}}.
$$

Proof.

Define the map
$$
\mathfrak G_R:\Omega_{\mathrm{phys}}
\longrightarrow
\Omega_R^{\mathrm{ext}}
\times_{\Lambda_\partial(R)}
\Omega_{R^c}^{\mathrm{ext}}
$$
by restricting a global configuration
$$
\omega=(X,\mathbf m)
$$
to its regional matter data, regional interior link data, and common cut-boundary label on $R$ and $R^c$. The two resulting extended regional configurations clearly have matching boundary labels, so the map is well defined.

It is injective because the regional matter occupations on $R$ and $R^c$ reconstruct the global occupation configuration $X$, while the regional interior link data together with the shared cut-boundary values reconstruct the global link-flux profile $\mathbf m$.

It is surjective because any compatible pair
$$
(\eta_R,\eta_{R^c})
$$
with matching boundary labels determines a unique global matter configuration by union, and determines a unique global link-flux profile by taking the two regional interior profiles together with the common cut values. Since each regional component already satisfies the physical Gauss recursion on its own sites and the cut values match, the reconstructed global configuration satisfies the physical Gauss law everywhere. Hence the reconstructed configuration lies in $\Omega_{\mathrm{phys}}$.
Thus $\mathfrak G_R$ is a canonical bijection. The fixed-label statement is the restriction of the same bijection to the subspace of pairs carrying the common boundary label $\lambda$.

$ \square $

**Corollary 1**

(Iterated multi-region gluing).

For any finite decomposition of the ring into connected mixed regions, the physical-sector configuration space is canonically an iterated fiber product of the corresponding extended regional configuration spaces over matching boundary-flux labels on the cut links.

Proof.

Apply Theorem 1 successively across each cut in the decomposition. Matching boundary labels at each stage are exactly the compatibility conditions needed to reconstruct the unique global physical-sector configuration.

$ \square $

Remark.

Theorem 1 is the exact replacement for naive tensor-factor locality on the physical sector. The regional spaces are ordinary finite configuration spaces; what changes is the gluing law. The benchmark local structure is therefore not an unconstrained product but a fiber product over a finite classical boundary algebra.

## Boundary-flux center

Once the gluing law is stated correctly, the algebraic refinement becomes straightforward. The cut-boundary flux labels generate a finite abelian center that organizes the induced local net.

**Definition 4**

(Boundary-flux center).

For a connected mixed region $R$ on the physical sector, let
$$
P_{R,\lambda}^{\partial},
\qquad
\lambda\in\Lambda_\partial(R),
$$
denote the exact boundary-flux projectors already defined at operational benchmark level. The

*boundary-flux center*

of $R$ is the finite abelian algebra
$$
\mathfrak Z_\partial(R)
:=
\operatorname{Alg}_1\bigl(\{P_{R,\lambda}^{\partial}\}_{\lambda\in\Lambda_\partial(R)}\bigr).
$$
For a finite family of disjoint regions
$$
R_1,\dots,R_m,
$$
define the corresponding joint boundary-flux center by
$$
\mathfrak Z_\partial(R_1,\dots,R_m)
:=
\operatorname{Alg}_1\Bigl(\bigcup_{j=1}^m \mathfrak Z_\partial(R_j)\Bigr).
$$

Remark.

The point of Definition 4 is not to add a new quantum center by hand. The center is already present in the exact finite configuration-space organization of the physical sector. The present paper merely promotes it from a bookkeeping device to the correct local structural datum.

## Exact regional action of boundary-flux-preserving benchmark maps

The operational benchmark already identified boundary-flux-preserving detector and setting subclasses. The next theorem reformulates those block-diagonality results as exact regionality statements on the extended spaces.

**Definition 5**

(Boundary-flux-preserving benchmark maps).

Let $R$ be a connected mixed region on the physical sector. A benchmark stochastic map
$$
M_R
$$
supported in $R$ will be called

*boundary-flux preserving*

if it is one of the following exact benchmark maps and preserves every boundary-flux projector:

1. a detector instrument component
  $$
  \mathcal J_{R,\mathbf g_{\mathrm{phys}}}^{a,(S)}(\tau)
  $$
  from the operational benchmark paper satisfying the preserving hypothesis of the detector locality theorem; or
2. a localized setting map
  $$
  \mathcal S_{R,\mathbf g_{\mathrm{phys}}}^{x,(S)}(\tau_{\mathrm{set}})
  $$
  satisfying the analogous preserving hypothesis for setting pulses.

Equivalently,
$$
[M_R,P_{R,\lambda}^{\partial}]=0
$$
for every admissible boundary label $\lambda$; by Paper 12, Theorems 4A and 4C, this is exactly the block-diagonality condition satisfied by the benchmark preserving subclasses.

**Theorem 2**

(Exact regional action on the extended configuration spaces).

Let $R$ be a connected mixed region on the physical sector, and let
$$
M_R
$$
be a boundary-flux-preserving benchmark map in the sense of Definition 5. Then:

1. *Fiber preservation.* The global map $M_R$ preserves each boundary-flux block
  $$
  P_{R,\lambda}^{\partial}\Omega_{\mathrm{phys}}.
  $$
2. *Extended regional descent.* For each admissible label $\lambda$, under the fixed-label gluing identification of Theorem 1,
  $$
  \Omega_{\mathrm{phys},\lambda}(R)
  \cong
  \Omega_{R,\lambda}^{\mathrm{ext}}
  \times
  \Omega_{R^c,\lambda}^{\mathrm{ext}},
  $$
  there exists a stochastic map
  $$
  M_{R,\lambda}^{\mathrm{ext}}:
  \Omega_{R,\lambda}^{\mathrm{ext}}\to\Omega_{R,\lambda}^{\mathrm{ext}}
  $$
  such that the restriction of $M_R$ to $\Omega_{\mathrm{phys},\lambda}(R)$ acts only on the $R$ factor and leaves the complementary extended factor fixed.
3. *Exact regionality.* In this sense the preserving benchmark maps are exact regional stochastic maps on the extended spaces.

Proof.

Item 1 is exactly the preserving-class block-diagonality already proved at benchmark level for detector and setting maps in Paper 12, Theorems 4A and 4C. Because
$$
[M_R,P_{R,\lambda}^{\partial}]=0
$$
for every $\lambda$, the map $M_R$ preserves each boundary-flux block.

For item 2, fix an admissible label $\lambda$. By the fixed-label part of Theorem 1, every state in $\Omega_{\mathrm{phys},\lambda}(R)$ is represented uniquely by a compatible pair
$$
(\eta_R,\eta_{R^c})
\in
\Omega_{R,\lambda}^{\mathrm{ext}}
\times
\Omega_{R^c,\lambda}^{\mathrm{ext}}.
$$
Transport the restricted stochastic map
$$
M_R\big|_{\Omega_{\mathrm{phys},\lambda}(R)}
$$
across that canonical identification. Since the underlying detector or setting Hamiltonian is supported in $R$, the transported stochastic map can change only the matter and interior-link variables belonging to the $R$ component. Because the map is boundary-flux preserving, it cannot alter the common boundary label $\lambda$, and because its support is confined to $R$, it does not alter the complementary extended variables. Hence on the $\lambda$ block there is a unique regional stochastic map
$$
M_{R,\lambda}^{\mathrm{ext}}
$$
on $\Omega_{R,\lambda}^{\mathrm{ext}}$ such that the transported action is the identity on the complementary extended factor.

Item 3 is merely the interpretation of item 2.

$ \square $

Remark.

Theorem 2 is the paper’s key dynamical reformulation. The earlier operational benchmark proved block diagonality. The present paper upgrades that statement to exact regionality on the correct regional spaces.

## Center-resolved induced local algebras and Einstein causality

Once the preserving benchmark maps are recognized as exact regional maps on the extended spaces, Einstein causality becomes a direct local statement over the boundary-flux center.

**Definition 6**

(Boundary-resolved induced local algebra).

For a connected mixed region $R$ on the physical sector, define the boundary-resolved induced local algebra
$$
\mathfrak A_\partial^{\mathrm{ind}}(R)
$$
to be the unital algebra generated by:

1. the dual effect-space actions of the boundary-flux-preserving benchmark detector and setting maps supported in $R$; and
2. the boundary-flux center
  $$
  \mathfrak Z_\partial(R).
  $$

Equivalently, one may view
$$
\mathfrak A_\partial^{\mathrm{ind}}(R)
$$
as the direct sum over admissible boundary labels of the induced local algebras on the fibers
$$
\Omega_{R,\lambda}^{\mathrm{ext}}.
$$

**Theorem 3**

(Boundary-flux-resolved Einstein causality on the benchmark).

Let
$$
R_A\perp R_B
$$
be disjoint connected mixed regions on the physical sector, and consider the boundary-resolved induced local algebras
$$
\mathfrak A_\partial^{\mathrm{ind}}(R_A),
\qquad
\mathfrak A_\partial^{\mathrm{ind}}(R_B)
$$
generated by the boundary-flux-preserving detector and setting benchmark subclasses. Then:

1. *Joint central decomposition.* Both algebras are block diagonal with respect to the joint boundary-flux center
  $$
  \mathfrak Z_\partial(R_A,R_B).
  $$
2. *Fiberwise commutation.* On every admissible joint boundary-flux block, the two regional algebras commute exactly.
3. *Center-resolved Einstein causality.* Equivalently, the induced benchmark net is Einstein-causal relative to the finite abelian boundary-flux center.

Proof.

By Theorem 2, every preserving benchmark map supported in $R_A$ acts, on each admissible joint boundary-label block, only on the extended $R_A$ component of the corresponding glued configuration, while every preserving benchmark map supported in $R_B$ acts only on the extended $R_B$ component. The boundary projectors generating
$$
\mathfrak Z_\partial(R_A,R_B)
$$
are diagonal on the same block decomposition, so item 1 is immediate.

Fix a joint admissible boundary-label block. Under the iterated gluing decomposition of Corollary 1, the $R_A$ generators act only on the $R_A$ factor and the $R_B$ generators act only on the $R_B$ factor. Therefore every generator from the first family commutes with every generator from the second family. By closure under products and linear combinations, the generated algebras commute on that block. This proves item 2.

Item 3 is exactly the interpretation of item 2: the benchmark net is not naively unfibered, but once resolved over the finite classical boundary-flux center it satisfies Einstein causality exactly.

$ \square $

**Corollary 2**

(Blockwise ordinary Einstein-causal benchmark net).

Let
$$
Q_{\boldsymbol\lambda}^{\partial}
$$
be a minimal nonzero projector in the joint boundary-flux center corresponding to a fixed admissible joint label
$$
\boldsymbol\lambda
$$
of the pair
$$
R_A,R_B.
$$
For each of the two regions under consideration, define the compressed block algebra
$$
\mathfrak A_{\boldsymbol\lambda}^{\mathrm{ind}}(R)
:=
Q_{\boldsymbol\lambda}^{\partial}\,
\mathfrak A_\partial^{\mathrm{ind}}(R)\,
Q_{\boldsymbol\lambda}^{\partial},
\qquad
R\in\{R_A,R_B\}.
$$
Then the fixed-block assignment
$$
R\longmapsto \mathfrak A_{\boldsymbol\lambda}^{\mathrm{ind}}(R)
$$
on the two-region benchmark subassignment generated by $R_A$ and $R_B$ is an ordinary finite benchmark local net on that block, and for the preserving subclasses it satisfies Einstein causality exactly on the chosen block.

Proof.

By Theorem 3, the regional algebras are block diagonal over the joint boundary-flux center and commute on every admissible joint block. Compressing by the chosen minimal projector
$$
Q_{\boldsymbol\lambda}^{\partial}
$$
therefore freezes the central label and removes the need to keep the center explicit inside the local algebra. What remains is precisely the pair of compressed regional algebras acting on a fixed block of the extended configuration-space decomposition, and Theorem 3 gives their exact Einstein-causality relation.

$ \square $

**Corollary 3**

(Structural reinterpretation of the phase-11 restricted bridge).

The restricted gauge-benchmark induced-net microcausality theorem of the phase-11 bridge paper is precisely the center-resolved Einstein-causality theorem of Theorem 3 written in the older fiberwise language. In particular, the phase-11 “fiberwise refinement” is not an auxiliary caveat but the correct local structure of the physical Gauss sector at the presently justified benchmark scope.

Proof.

The phase-11 theorem already proved exact commuting induced algebras on fixed compatible boundary-flux blocks for the relevant preserving subclasses. Theorem 3 repackages the same commuting statement as a theorem about a net resolved over the finite abelian boundary-flux center generated by the exact projectors
$$
P_{R,\lambda}^{\partial}.
$$
This is a structural strengthening, not a change of benchmark scope.

$ \square $

## Raw-side status and explicit non-claims

The center-resolved locality theorem should not be confused with stronger claims that the current stack does not support. The point of this section is to say that plainly.

**Raw-side status.**

The present paper does not prove that the primitive raw comparison maps
$$
J_R=\Gamma_R\Gamma_0^{-1}
$$
or the raw exchange defects
$$
E_{R,S}
$$
are themselves local observables in the Haag-Kastler sense. Nor does it produce a nontrivial exact raw commuting class for the active free, static-$U(1)$, or dynamical-gauge raw families. The phase-11 bridge paper already records explicit nonzero disjoint-support raw exchange in those benchmark families. The present paper therefore sharpens the operational and induced local structure without erasing the raw-side obstruction by vocabulary.

**Scope boundary.**

Theorem 3 applies only to the preserving detector and setting subclasses already isolated at benchmark level. It does not yet give arbitrary-coupling universality, a full boundary-flux-resolved theorem for all gauge-compatible couplings, a compact-rotor extension, a continuum quasilocal completion, a time-slice theorem, a non-Abelian extension, or an interacting gauge-matter closure theorem.

## Exact closure at the presently justified scope

With the structural issue now isolated correctly, the theorem-level deliverable of the paper can be stated cleanly.

**Theorem 4**

(Exact closure of the boundary-flux-resolved bridge refinement at the presently justified scope).

At the presently justified benchmark scope, the following are established exactly:

1. *Exact no-go for naive unfibered physical-sector factorization.* The physical Gauss sector is fibered over cut-boundary flux labels and is not canonically an unconstrained regional product space.
2. *Exact extended regional spaces.* The correct regional objects are finite configuration spaces carrying local matter data, interior link data, and boundary flux labels.
3. *Exact physical-sector gluing.* The global physical-sector configuration space is canonically the fiber product of the corresponding extended regional spaces over matching boundary labels.
4. *Exact boundary-flux center.* The boundary-flux projectors generate a finite abelian center organizing the benchmark locality structure.
5. *Exact regional action of preserving benchmark maps.* Boundary-flux-preserving detector and setting benchmark maps descend to exact regional stochastic maps on the extended spaces.
6. *Exact center-resolved Einstein causality.* The induced benchmark local algebras commute on each admissible joint boundary-flux block, hence define an Einstein-causal benchmark net relative to the boundary-flux center.
7. *Exact blockwise local-net reduction.* After compression to a fixed admissible joint boundary-flux block, one recovers an ordinary finite benchmark local net satisfying Einstein causality outright on that block.
8. *Exact reinterpretation of the phase-11 fiberwise bridge.* The older fiberwise gauge-benchmark refinement is now identified as the correct center-resolved local structure rather than as a secondary qualification.

Proof.

Item 1 is Proposition 1. Items 2 and 3 are Definitions 1–3 together with Theorem 1 and Corollary 1. Item 4 is Definition 4. Item 5 is Definition 5 together with Theorem 2. Item 6 is Definition 6 together with Theorem 3. Item 7 is Corollary 2. Item 8 is Corollary 3.

$ \square $

What remains outside the present claim is equally important:

1. *No raw observable-identification theorem yet.* The paper does not prove that raw comparison maps or raw exchange defects are themselves local observables.
2. *No nontrivial exact raw commuting theorem yet.* The active free and gauge raw benchmarks still exhibit explicit disjoint-support raw exchange.
3. *No arbitrary-coupling boundary-flux-resolved locality theorem yet.* The present theorem applies to the preserving detector and setting subclasses already isolated in the operational paper.
4. *No compact-rotor, continuum, or quasilocal completion yet.* The finite cutoff benchmark remains the exact scope of the present theorem package.
5. *No interacting, non-Abelian, or full Haag-Kastler reconstruction yet.* Those remain later burdens.

**Strategic remark.**

The gain of the present paper is conceptual and exact. It does not broaden the benchmark. It repairs the benchmark locality statement by putting the correct regional variables in place.

## Discussion: center, edge data, and the next exact burdens

The central conceptual gain of the paper is easy to misstate if one speaks too quickly in algebraic-QFT language. Nothing here changes the Barandes ontology. The primary objects remain ordinary finite configuration spaces and stochastic maps on those spaces. The boundary-flux center is not imported as an additional quantum structure in order to save locality after the fact. It is the finite classical interface datum that the exact Gauss recursion already forces on the physical sector. In that sense the paper is conservative about ontology while being revisionary about local bookkeeping.

That point is also why the present paper should not be read as a merely verbal “edge-mode” gloss. The benchmark obstruction is exact and finite. If one suppresses the cut-boundary electric-flux data, the physical sector appears not to factor regionally and localized benchmark maps appear to have a residual nonlocal dependence. Once the boundary data are restored explicitly, the same benchmark dynamics reorganizes into exact regional actions on extended configuration spaces and into commuting induced local algebras on each admissible joint block. The gain is therefore not a change of interpretation attached to the old theorem package; it is a sharper theorem package stated on the correct regional objects.

This also clarifies the status of the phase-11 bridge. Paper 13 already had the right local content at restricted benchmark scope, but it expressed that content as a fiberwise refinement clause attached to a broader bridge theorem. The present paper reverses the emphasis. On the physical Gauss sector, the center-resolved statement is not a secondary caveat; it is the benchmark locality theorem itself. Put differently: the phase-11 bridge did not overreach on the preserved subclasses, but it did not yet isolate the correct local variables as the main object of study.

The new phase ordering follows directly from this diagnosis. A genuinely interacting benchmark is scientifically more useful once the exact noninteracting local structure has been put in its correct form. Otherwise one risks mixing two different burdens: the pre-existing failure of naive physical-sector factorization and the genuinely new burden of interaction-induced exchange structure. By inserting the present paper before the interacting benchmark, the roadmap cleanly separates those issues. The later interacting paper can then ask a sharper question: does the center-resolved locality structure survive, widen, or break when genuine physical-sector interactions are turned on?

The next exact burdens are therefore more focused than they were before. First, one would like to enlarge the preserving subclasses toward broader gauge-compatible detector and setting couplings, ideally identifying the precise maximal class on which the extended-space regional-action theorem still holds. Second, one would like to compare the operational induced net and any raw-induced net on the overlap of their justified benchmark domains, rather than continuing to treat them as merely parallel constructions. Third, one would like to understand whether the boundary-flux center survives in a compact-rotor or larger-cutoff setting without losing exact control of the physical-sector gluing map. Only after those structural questions are settled does the interacting benchmark become maximally diagnostic rather than merely exploratory.

**Discussion remark.**

At this phase of the program, the right slogan is not “locality fails until interaction is added” and not “locality was already obvious on the physical sector.” The exact statement earned by the current stack is narrower: naive factorization fails, center-resolved locality survives, and the finite benchmark already knows the difference.

## Conclusion

The correct moral of the present benchmark is now simple. The physical Gauss sector does not generically factor into independent regional tensor factors, and the program should stop speaking as if it did. But that failure is not a failure of locality. It is a failure to include the exact cut-boundary data that the Gauss recursion already shows are necessary.

Once the regional spaces are enlarged by those boundary-flux labels, the benchmark preserving subclasses become exact regional stochastic maps, and the corresponding induced local net becomes Einstein-causal in the right finite sense: not as an unfibered tensor-factor net, but as a net resolved over a finite abelian boundary-flux center. This is the strongest honest refinement of the phase-11 bridge that the present stack can support, and it clarifies the next true burdens rather than obscuring them.

The immediate consequence for the roadmap is also sharp. If the roadmap is updated to reflect the exact structural burden now visible, this paper sits naturally before the first genuinely interacting gauge-matter benchmark. Only after the exact boundary-data organization of locality is closed does it become maximally informative to ask which interacting benchmark best tests whether the center-resolved locality structure survives beyond the present preserving subclasses and fixed finite cutoff. In that sense, the present paper is best understood as the last exact bridge-refinement paper before the interacting benchmark, not as an optional side note.

## References

1. [1] Anonymous, “Toward Lorentz-Covariant Indivisible Stochastic Processes,” architecture draft (2026).
2. [2] Anonymous, “Dynamical Abelian Gauge Field and Gauss-Law Sectors in Relativistic ISP,” preprint (2026).
3. [3] Anonymous, “Localized Controls, Detectors, and Operational Relativity in Relativistic ISP,” preprint (2026).
4. [4] Anonymous, “Einstein Causality from Exchange Defects: a Haag-Kastler Bridge for Relativistic ISP,” preprint (2026).
5. [5] R. Haag and D. Kastler, “An Algebraic Approach to Quantum Field Theory,” *Journal of Mathematical Physics* **5**, 848–861 (1964).
6. [6] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* (accepted version, 2025).
7. [7] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” preprint (2025).
8. [8] J. A. Barandes, “The Stochastic-Quantum Theorem,” preprint (2026).
