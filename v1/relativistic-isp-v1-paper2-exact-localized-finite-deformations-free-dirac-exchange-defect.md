# Exact Localized Finite Deformations and the Free Dirac Exchange-Defect Theorem

Preprint, not peer reviewed, version 2026-05-28.

*Quasilocal filtration, deleted-bond leading coefficients, and the first exact finite-support exchange package in relativistic ISP*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 2 in the relativistic ISP sequence; exact free one-particle scope only

## Abstract

Program 1 of the relativistic ISP architecture asks for an exact free-model package of localized finite deformations and their exchange defect before the program broadens into higher coefficients, variable particle number, or gauge structure. This paper isolates that theorem-level core at the exact scope currently justified. We work in the one-particle periodic lattice Dirac model with the collar-excision localized deformation rule and treat the exact finite slab kernels, their localized comparison maps, and the resulting exchange defect as the primitive objects.

The results are exact and deliberately limited. First, for every finite interval support $R$, the localized comparison map $J_R(\Delta)=\Gamma_R(\Delta)\Gamma_0(\Delta)^{-1}$ admits a quasilocal $\Delta^2$-onset filtration, and its inverse has the same filtration. Second, the leading coefficient $A_R^{(1)}$ is determined by deleted bond data plus the diagonal normalization required by column sums: its off-diagonal part depends only on the bonds removed by collar excision, not on the deleted mass terms. Third, for disjoint finite intervals we isolate the first exact exchange package. The full defect has the exact order formula
$$E_{R,S}(\Delta)=I+\Delta^{2\mu_1(R,S)}C_{R,S}^{(\mu_1)}+O(\Delta^{2\mu_1(R,S)+2}),$$
while the minimal-strip part of the first support-level commutator $[A_R^{(1)},A_S^{(1)}]$ is controlled exactly by the boundary packets facing the gap. Thus the first nontrivial exchange data are boundary-controlled rather than volume-controlled. We do not here claim a higher-coefficient strip-closure theorem, a general finite-support bond-centered continuum law, a Fock-space lift, or gauge coupling. Those belong to later papers.

## Introduction

The relativistic ISP architecture paper identified the exchange defect for localized finite deformations as the decisive free-model integrability datum. The immediate sequel made that datum explicit for concrete one-particle rules, proved a sharp singleton bond-centered thin-slab reduction, and showed that raw rule uniqueness fails while onset-renormalized universality survives at the singleton level. What remained missing was a clean paper that isolates the exact free one-particle exchange-defect core at the scope one can presently defend without borrowing future higher-coefficient, Fock-space, or gauge results.

That is the sole purpose of the present paper. We keep the collar-excision rule, because it is the sharpest explicit free-model realization of Program 1 currently available, and we extract the exact statements that can already be made for arbitrary finite interval supports. The point is not to broaden the ontology; it is to sharpen theorem-level scope.

**Main results (informal).**

1. *Exact filtration.* For every finite interval support $R$, the comparison map $J_R(\Delta)$ has an exact $\Delta^2$-onset quasilocal filtration, and $(J_R(\Delta))^{-1}$ has the same support growth.
2. *Exact leading finite-support coefficient.* The first coefficient $A_R^{(1)}$ is a sum of local deleted-bond contributions plus the diagonal normalization forced by column sums.
3. *Exact first exchange package.* For disjoint finite intervals $R,S$, the defect order is governed by the exact overlap index $\mu_1(R,S)$, and the minimal-strip part of the first support-level commutator $[A_R^{(1)},A_S^{(1)}]$ is exactly the commutator of the boundary packets facing the gap.

Scope note. This paper closes the exact free one-particle exchange-defect package now at fixed finite-lattice scope and for sufficiently small slab size where the reference kernels are invertible. Constants in the filtration and inverse-control statements may depend on the fixed lattice size, mass, spacing, and support data unless a separate uniform estimate is stated. It does not claim higher-coefficient strip closure, a general support-level bond-centered continuum law, a Fock-space lift, or gauge coupling.

## Exact free one-particle setup

Let $\Lambda_L=\mathbb Z/L\mathbb Z$ be a periodic lattice of length $L$ and spacing $a>0$. The one-particle configuration basis is
$$\C_L=\Lambda_L\times\{\uparrow,\downarrow\},$$
and the Hilbert space is $\H_L=\mathbb C^{2L}$. We use the free lattice Dirac Hamiltonian
$$H_D=K+M,\qquad
K=-\frac{i}{2a}\alpha(T_+-T_-),\qquad
M=m\beta,$$
with $\alpha=\sigma_x$ and $\beta=\sigma_z$.

**Definition 1**

(Localized collar-excision data).

For a finite interval $R\subset\Lambda_L$, let
$$C_R:=\sum_{n\in R}m\,\beta_n+\sum_{\substack{n+1/2:\\ \{n,n+1\}\cap R\neq\varnothing}}k_{n+1/2},\qquad
B_R:=H_D-C_R.$$
Define the reference and localized slab kernels by
$$\Gamma_0(\Delta):=\Gamma(e^{-i\Delta H_D}),\qquad
\Gamma_R(\Delta):=\Gamma(e^{-i\Delta B_R}),$$
where $\Gamma(U)_{AB}:=|U_{AB}|^2$ in the configuration basis. The localized comparison map is
$$J_R(\Delta):=\Gamma_R(\Delta)\Gamma_0(\Delta)^{-1}.$$
For two supports $R,S$, define the exchange defect
$$E_{R,S}(\Delta):=J_R(\Delta)J_S(\Delta)J_R(\Delta)^{-1}J_S(\Delta)^{-1}.$$

Remark.

The exact positive kernels $\Gamma_0$ and $\Gamma_R$ are the primitively physical objects here. The maps $J_R$ and $E_{R,S}$ are algebraic comparison objects, so pseudo-stochasticity is not a bug but part of the ISP structure.

## Exact quasilocal filtration from the kernels

**Theorem 1**

(Exact quasilocal $\Delta^2$-onset filtration).

For every finite interval $R\subset\Lambda_L$, the comparison map admits an expansion
$$J_R(\Delta)=I+\sum_{k\ge 1}\Delta^{2k}A_R^{(k)}$$
with
$$\supp A_R^{(k)}\subset\N_k(R)\qquad (k\ge 1).$$
The same statement holds for every finite interval $S$.

Proof sketch.

At the amplitude level, $e^{-i\Delta B_R}-e^{-i\Delta H_D}$ has a Dyson expansion whose order-$\Delta^k$ term is supported in the $k\!-\!1$ step neighborhood of $R$. Passing to kernels replaces amplitudes by modulus-squared expressions, so the first nontrivial comparison term begins at order $\Delta^2$. The nearest-neighbor structure of $H_D$ then gives order-by-distance support growth, and convolution with the global inverse kernel preserves the same support radius order by order.

$ \square $

**Corollary 1**

(Inverse stability).

If
$$J_R(\Delta)=I+\sum_{k\ge 1}\Delta^{2k}A_R^{(k)},\qquad \supp A_R^{(k)}\subset\N_k(R),$$
then
$$J_R(\Delta)^{-1}=I+\sum_{k\ge 1}\Delta^{2k}\widetilde A_R^{(k)},\qquad \supp \widetilde A_R^{(k)}\subset\N_k(R).$$

Proof.

Expand $J_R^{-1}$ as a Neumann series in $\sum_{k\ge 1}\Delta^{2k}A_R^{(k)}$. Support radii add under matrix multiplication, so a product contributing to order $\Delta^{2m}$ is supported in $\N_m(R)$.

$ \square $

Remark.

This is the exact kernel-level part of Program 1: no strip-closure hypothesis and no continuum identification have been invoked yet.

## Exact leading finite-support coefficient

**Definition 2**

(Deleted-bond coefficients).

For a bond midpoint $b=n+\tfrac12$, let $Q_b$ denote the order-$\Delta^2$ local kernel coefficient obtained by deleting only that kinetic bond from the free Dirac Hamiltonian and comparing with the free reference slab. Each $Q_b$ is supported on the two adjacent sites of the bond.

**Theorem 2**

(Exact leading finite-support coefficient).

For every finite interval $R\subset\Lambda_L$,
$$A_R^{(1)}=\sum_{b\in\partial_1R}Q_b+D_R,$$
where
$$\partial_1R:=\Bigl\{n+\tfrac12:\ \{n,n+1\}\cap R\neq\varnothing\Bigr\}$$
is the deleted-bond set and $D_R$ is diagonal, uniquely determined by the column-normalization condition $\one^\top A_R^{(1)}=0$. In particular:

1. the off-diagonal part of $A_R^{(1)}$ depends only on the deleted kinetic bonds;
2. the deleted mass terms contribute only through the diagonal normalization bookkeeping;
3. $\supp A_R^{(1)}\subset\N_1(R)$.

Proof.

For $A\neq B$, the order-$\Delta^2$ coefficient of $\Gamma(e^{-i\Delta H})$ is $|H_{AB}|^2$. Replacing $H_D$ by $B_R$ removes precisely the off-diagonal matrix elements associated with the bonds incident on $R$; the on-site mass terms are diagonal and therefore contribute no off-diagonal second-order weight. Hence the off-diagonal part of $A_R^{(1)}$ is the sum of the deleted-bond differences $Q_b$. The diagonal entries are then uniquely fixed by the exact normalization condition on $J_R(\Delta)$, and support in $\N_1(R)$ is immediate from the support of each $Q_b$.

$ \square $

Remark.

At leading order, finite-support localized deformations are already boundary-organized. The first coefficient is not a support-volume blob; it is a finite sum of local deleted-bond pieces plus diagonal normalization.

## The first exact exchange package for disjoint finite supports

**Definition 3**

(Exact overlap index).

For two finite intervals $R,S\subset\Lambda_L$, define
$$\mu_1(R,S):=\min\bigl\{p+q:\ p,q\ge 1,\ \N_p(R)\cap\N_q(S)\neq\varnothing\bigr\}.$$

**Proposition 3**

(Exact defect order formula).

For disjoint finite intervals $R,S$,
$$E_{R,S}(\Delta)=I+\Delta^{2\mu_1(R,S)}C_{R,S}^{(\mu_1)}+O(\Delta^{2\mu_1(R,S)+2}),$$
where
$$C_{R,S}^{(\mu_1)}:=\sum_{\substack{p+q=\mu_1(R,S)\\ p,q\ge 1}}[A_R^{(p)},A_S^{(q)}].$$

Proof.

Insert the filtrations of Theorem 1 and Corollary 1 into the group commutator definition of $E_{R,S}$. Terms of order below $2\mu_1(R,S)$ vanish because the corresponding support neighborhoods do not yet meet. At the first nonzero order, the surviving contribution is exactly the sum of commutators with $p+q=\mu_1(R,S)$.

$ \square $

Remark.

Proposition 3 gives the exact order of the defect for every disjoint finite-support pair. What it does

*not*

do by itself is make the leading coefficient explicit when $\mu_1(R,S)>2$, because then higher coefficients $A_R^{(p)}$ enter. That is precisely where the next paper begins.

**Definition 4**

(Minimal exchange strip and boundary packets).

Fix a nonwrapping pair of disjoint finite intervals on the periodic ring and choose the branch on which
$$
R=[r_-,r_+],\qquad S=[s_-,s_+],\qquad r_+<s_-.
$$

$$
\Xi_{R,S}:=[r_+-1,\ s_-+1].
$$

**Theorem 3**

(Exact minimal-strip boundary-packet reduction).

For every nonwrapping disjoint pair of finite intervals $R,S$,
$$\Pi_{R,S}^{\min}[A_R^{(1)},A_S^{(1)}]=[\mathcal Q_{R\to S},\mathcal Q_{S\to R}].$$
In particular, the minimal-strip part of the first support-level commutator is controlled exactly by the boundary packets facing the gap.

Proof.

Write
$$A_R^{(1)}=\sum_{b\in\partial_1R}Q_b+D_R,\qquad
A_S^{(1)}=\sum_{c\in\partial_1S}Q_c+D_S$$
using Theorem 2. Any deleted bond whose support lies farther inside $R$ or $S$ than the boundary sites nearest the gap has matrix support outside $\Xi_{R,S}$ after taking the commutator, so it is annihilated by $\Pi_{R,S}^{\min}$. The same is true for diagonal terms except at the boundary sites already captured by the projected packets. Therefore the projection of the full commutator equals the commutator of the projected boundary pieces.

$ \square $

**Corollary 2**

(Exact nearby-support leading coefficient).

If $\mu_1(R,S)=2$—equivalently, if the first exchange order is already generated by the leading coefficients—then
$$E_{R,S}(\Delta)=I+\Delta^4[A_R^{(1)},A_S^{(1)}]+O(\Delta^6),$$
and therefore
$$\Pi_{R,S}^{\min}\!\bigl(E_{R,S}(\Delta)-I\bigr)
=\Delta^4[\mathcal Q_{R\to S},\mathcal Q_{S\to R}]+O(\Delta^6).$$

Proof.

The first statement is the case $\mu_1(R,S)=2$ of Proposition 3. Apply Theorem 3 to the leading coefficient.

$ \square $

Remark.

Corollary 2 is the exact finite-support analogue of the singleton leading exchange calculation. It is already enough to show that the first nearby-support exchange data are boundary-controlled rather than support-volume controlled.

## Exact scope and what remains

The exact theorem-level core now in hand is the following:

1. the exact localized collar-excision kernels for arbitrary finite interval supports,
2. their exact quasilocal filtration and inverse stability,
3. the exact leading finite-support coefficient $A_R^{(1)}$, and
4. the exact first exchange package consisting of Proposition 3 together with the boundary-packet reduction of Theorem 3.

What remains outside the present claim is equally important:

1. *Higher coefficients.* The paper does not compute $A_R^{(2)}$ or beyond for general supports, nor does it classify the active strip channels at those orders.
2. *General support-level continuum law.* The paper does not derive a bond-centered thin-slab theorem for general finite supports from exact strip moments. It isolates the exact boundary-controlled coefficient package that should feed that later derivation.
3. *Variable particle number.* No Fock-space lift is claimed here.
4. *Gauge coupling.* No minimal-coupling or holonomy theorem is claimed here.

**Strategic remark.**

This exact scope is already enough to justify a stricter phase ordering. The program should next finish the support-level and higher-coefficient exchange algebra before broadening into Fock-space or gauge structure.

## Conclusion

The relativistic ISP program now has a cleaner exact free-model center than before. The exact kernel construction, quasilocal filtration, and leading finite-support coefficient package can be stated without borrowing future hypotheses. The exchange defect for disjoint finite supports has an exact order formula, and the first support-level exchange commutator is boundary-controlled on the minimal exchange strip.

That is the precise sense in which this paper closes Program 1 at the free one-particle theorem level. It does not solve the higher-coefficient problem, the general support-level bond-centered continuum law, variable particle number, or gauge coupling. But it removes the ambiguity about what the presently proved free-model core actually is, and therefore sharpens the next paper’s task rather than broadening it prematurely.

## References

1. [1] Anonymous, “Toward Lorentz-Covariant Indivisible Stochastic Processes: Spatial Locality, Temporal Indivisibility, and Localized Finite Deformations,” preprint (2026).
2. [2] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
3. [3] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
4. [4] J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085 (2023; rev. 2026).
5. [5] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192 (2025).
