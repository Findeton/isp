# Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes

Preprint, not peer reviewed, version 2026-05-28.

*Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Focused sequel on explicit free-model deformation rules and exchange-defect structure

## Abstract

The previous relativistic ISP paper isolated Proposition 4G as its central conditional statement: *if* localized finite Dirac deformation maps admit an order-by-distance filtration, *then* the exchange defect cannot appear below the support-separation order. This paper places the two explicit free one-particle rules in one account. The first rule, the bulk-then-collar Lie-Trotter step $e^{-i\Delta B_R}e^{-i\Delta C_R}$, proves filtration and inversion stability but yields the shifted law $E_{R,S}(\Delta)=I+O(\Delta^{2\max(4,d)})$ for singleton supports at graph distance $d$, because the one-region comparison maps start only at order $\Delta^4$. The second rule, collar excision $e^{-i\Delta B_R}$, starts at order $\Delta^2$ and gives $E_{R,S}(\Delta)=I+O(\Delta^{2d})$ for $d\ge 2$, with only a minor $O(\Delta^4)$ floor at $d=1$.

The new conceptual results are meta-theorems about rule dependence and the thin-slab agenda. First, we prove a no-go lemma: the current local-intervention axioms do not uniquely select a localized deformation rule, because they admit continuous families of admissible local Hamiltonian deformations with distinct leading comparison coefficients. Second, we prove a restricted renormalized universality theorem: if an admissible class of rules shares the same normalized thin-slab local generator after rule-dependent onset rescaling, then the renormalized leading exchange bracket is rule-independent and reduces to the same continuum tangential Dirac-Schwinger bracket. For the concrete $ \lambda $-family $U_R^{(\lambda)}(\Delta)=e^{-i\Delta(H_D-\lambda C_R)}$, the first comparison coefficient scales exactly as $A_{R,\lambda}^{(1)}=\lambda(2-\lambda)A_R^{(1)}$, giving an exact finite-lattice test of renormalized universality at the first visible exchange order. If one naively site-smears the singleton collar-excision coefficient, the resulting $\Delta^{-4}$ exchange term diverges entrywise like $a^{-1}$. But the same exact local algebra also identifies the correct free-model tangential density: a bond-centered renormalized operator built from the bond-flip and two-step strip channels has a finite continuum action on smooth sampled one-particle profiles and yields the explicit tangential pseudo-generator
$$
K_\parallel[\beta]=\bigl(\beta\partial_x+\tfrac12\partial_x\beta\bigr)(I-\alpha),
\qquad
\beta=N\partial_xM-M\partial_xN.
$$
After the same onset renormalization, the admissible $ \lambda $-family shares that tangential limit. The collar-excision rule therefore supplies the sharpest explicit free-model realization of Program 1 now available: raw rule uniqueness fails, the naive entrywise thin-slab limit fails, but bond-centered renormalized universality survives.

## Introduction

Program 1 of the previous relativistic ISP paper asked for an explicit free-Dirac localized deformation rule satisfying four properties: (i) normalization preservation, (ii) boundary/tangential localization of the exchange defect, (iii) separation scaling $E_{R,S}(\Delta) = I + O(\Delta^{2\ell(R,S)})$, and (iv) reduction to the normal-normal Dirac-Schwinger bracket in the thin-slab limit.

This paper places the two explicit free one-particle rules in one account. The first explicit benchmark uses the bulk-then-collar Lie-Trotter step $U_R^{\mathrm{LT}}(\Delta)=e^{-i\Delta B_R}e^{-i\Delta C_R}$. It proved quasilocal filtration and inversion stability, but found that the one-region maps begin only at order $\Delta^4$, forcing the shifted law $E_{R,S}(\Delta)=I+O(\Delta^{2\max(4,d)})$ for singleton supports at graph distance $d$. The second rule, collar excision $U_R^{\mathrm{exc}}(\Delta)=e^{-i\Delta B_R}$, starts at order $\Delta^2$ and restores the exact $O(\Delta^{2d})$ law for $d\ge 2$, with only a minor $O(\Delta^4)$ floor at $d=1$.

Those two explicit rules sharpen the physical issue rather than dissolving it. The question is no longer whether localized finite deformations can be made concrete at all; both rules show that they can. The question is whether the relativistic ISP program should expect a unique physically selected rule, or only a weaker rule-independent continuum bracket after appropriate renormalization. The new results of the present paper address exactly that fork.

First, we prove a no-go lemma: the current local-intervention axioms do not uniquely select a localized deformation rule. They admit continuous families of admissible local Hamiltonian modifications with distinct leading comparison coefficients. Second, we prove a restricted renormalized universality theorem: if an admissible class of rules shares the same normalized thin-slab local generator after rule-dependent onset rescaling, then the renormalized leading exchange bracket is rule-independent and reduces to the same continuum tangential Dirac-Schwinger bracket. Raw finite-$\Delta$ universality therefore fails, but onset-renormalized universality remains a live target.

Two further results sharpen that fork. The $ \lambda $-family from the no-go lemma can be analyzed exactly at the finite-lattice level: its first comparison coefficient is globally proportional to the collar-excision coefficient, so the family gives a genuine nontrivial test of restricted renormalized universality. If one insists on an entrywise matrix limit, the thin-slab problem fails: naive site-smearing of the singleton collar-excision coefficients makes the leading exchange commutator diverge like $a^{-1}$ after $\Delta^4$ normalization.

But the exact exchange algebra is not organized by isolated sites. It closes on bond-flip and two-step strip operators, and those operators define a bond-centered renormalized tangential density whose action on smooth sampled one-particle profiles has a finite continuum limit. So the explicit free rule does reach the tangential bracket after the correct spatial renormalization, and the same onset-renormalized limit propagates across the $ \lambda $-family. We stay entirely within the free one-particle $1+1$ dimensional lattice Dirac model on a periodic ring. No gauge fields, variable particle number, detector models, gravity, or continuum control. The point is narrower and cleaner: give the sharpest explicit free-model realization of Program 1, record the first-rule benchmark inside the same paper, and isolate the exact theorem-level sense in which raw rule selection fails, the naive entrywise thin-slab limit fails, but a bond-centered renormalized thin-slab bracket survives.

**Main results (informal).**

There are three theorem-level conclusions:

1. *Lie-Trotter benchmark.* For $U_R^{\mathrm{LT}}(\Delta)=e^{-i\Delta B_R}e^{-i\Delta C_R}$, the one-region comparison maps begin at order $\Delta^4$ and the exchange defect obeys $E_{R,S}^{\mathrm{LT}}(\Delta)=I+O(\Delta^{2\max(4,d)})$ for singleton supports at graph distance $d$.
2. *Collar-excision success.* For $U_R^{\mathrm{exc}}(\Delta)=e^{-i\Delta B_R}$, the one-region comparison maps begin at order $\Delta^2$ and the exchange defect obeys $E_{R,S}^{\mathrm{exc}}(\Delta)=I+O(\Delta^{2d})$ for $d\ge 2$, with explicit leading coefficients at $d=1,2$.
3. *No-go, bond-centered thin-slab reduction, and restricted universality.* The present local-intervention axioms do not uniquely select a localized deformation rule. The naive site-smearing of the collar-excision coefficient has no finite entrywise continuum limit, but a bond-centered renormalized density built from the exact exchange-strip algebra yields an explicit tangential pseudo-generator on smooth sampled profiles. Across the admissible $ \lambda $-family, the onset-renormalized leading tangential bracket is rule-independent.

## Free periodic lattice-Dirac setup

Let $\Lambda_L = \mathbb{Z}/L\mathbb{Z}$ be a periodic spatial lattice of length $L$ with lattice spacing $a > 0$. The single-particle configuration basis is $\{|n,\uparrow\rangle, |n,\downarrow\rangle\}_{n\in\Lambda_L}$, and the Hilbert space is $\H_L = \mathbb{C}^{2L}$. We use the same free Dirac matrices as in the previous papers:
$$
\alpha = \sigma_x, \qquad \beta = \sigma_z.
$$
The free lattice Dirac Hamiltonian is $H_D = K + M$ with
$$
K = -\frac{i}{2a}\,\alpha(T_+ - T_-), \qquad M = m\beta,
$$
where $T_\pm$ are the periodic shift operators. In local form,
$$
H_D = \sum_{n\in\Lambda_L} m\,\beta_n + \sum_{n\in\Lambda_L} k_{n+1/2},
$$
where $k_{n+1/2}$ is the nearest-neighbor kinetic bond between sites $n$ and $n+1$. The ISP kernel for any unitary one-particle propagator $U$ is
$$
\Gamma(U)_{AB} = |U_{AB}|^2, \qquad A,B\in\C_L := \Lambda_L\times\{\uparrow,\downarrow\}.
$$
The reference slab kernel is $\Gamma_0(\Delta) = \Gamma(e^{-i\Delta H_D})$.

**Definition 1**

(Periodic neighborhoods and support).

For a finite interval $R\subset\Lambda_L$ and integer $q\ge 0$, let
$$
\N_q(R) := \{x\in\Lambda_L:\,d(x,R)\le q\}
$$
where $d$ is the periodic graph distance. A matrix $A$ on the configuration basis is

*supported in $\N_q(R)$*

if $A_{AB}=0$ whenever the site component of $A$ or of $B$ lies outside $\N_q(R)$.

Remark.

The support notion is kernel-theoretic throughout. We track which matrix entries are nonzero at a given order in $\Delta$, not strict compact support at fixed $\Delta$.

## Explicit deformation rules

The collar/bulk splitting of the Dirac Hamiltonian relative to a region $R$ is common to both explicit rules and to the previous draft.

**Definition 2**

(Collar and bulk Hamiltonians).

For a finite interval $R\subset\Lambda_L$, define the

*Dirac collar Hamiltonian*

$$
C_R := \sum_{n\in R} m\,\beta_n + \sum_{\substack{n+1/2:\\\{n,n+1\}\cap R\ne\varnothing}} k_{n+1/2}.
$$
Thus $C_R$ contains the on-site mass terms at $R$ and every kinetic bond with at least one endpoint in $R$. The complementary

*bulk Hamiltonian*

is $B_R := H_D - C_R$.

### The Lie-Trotter benchmark rule

We first record the main free-model Lie-Trotter benchmark before turning to collar excision.

**Benchmark proposition.**

(Bulk-then-collar Lie-Trotter rule).

Set
$$
U_R^{\mathrm{LT}}(\Delta):=e^{-i\Delta B_R}e^{-i\Delta C_R},
\qquad
\Gamma_R^{\mathrm{LT}}(\Delta):=\Gamma(U_R^{\mathrm{LT}}(\Delta)).
$$
Then the corresponding comparison maps satisfy
$$
J_R^{\mathrm{LT}}(\Delta)=I+\sum_{k\ge 2}\Delta^{2k}A_{R,\mathrm{LT}}^{(k)},
\qquad
\supp A_{R,\mathrm{LT}}^{(k)}\subset\N_k(R),
$$
their perturbative inverses inherit the same filtration, and the exchange defect obeys
$$
E_{R,S}^{\mathrm{LT}}(\Delta)
=
I+O\!\bigl(\Delta^{2\mu_{\mathrm{LT}}(R,S)}\bigr),
\qquad
\mu_{\mathrm{LT}}(R,S):=\min\{p+q:\ p,q\ge 2,\ \N_p(R)\cap\N_q(S)\neq\varnothing\}.
$$
For singleton supports at graph distance $d$,
$$
E_{R,S}^{\mathrm{LT}}(\Delta)=I+O\!\bigl(\Delta^{2\max(4,d)}\bigr).
$$
Localized pseudo-stochasticity appears already in the near-local sector at order $\Delta^4$.

Remark.

This benchmark is included here because any viable rule-selection or universality statement has to explain both facts at once: the free program already works explicitly for one rule, and yet the raw short-distance law depends on which localized rule one chooses.

### The collar-excision rule

The second rule is genuinely different. Instead of evolving both bulk and collar in a locally reordered step, one can excise the collar entirely for one slab.

**Definition 3**

(Collar-excision deformation rule).

The

*collar-excision finite deformation*

supported in $R$ is
$$
U_R(\Delta) := e^{-i\Delta B_R}.
$$
Its kernel is $\Gamma_R(\Delta) := \Gamma(e^{-i\Delta B_R})$. Similarly for a second finite interval $S$, $U_S(\Delta) := e^{-i\Delta B_S}$ with kernel $\Gamma_S(\Delta)$.

Remark.

The physical interpretation is exact. The bulk Hamiltonian $B_R = H_D - C_R$ contains no bonds incident on $R$ and no mass term at sites within $R$. The unitary $e^{-i\Delta B_R}$ therefore leaves sites in the collar of $R$ completely frozen at zeroth order in $\Delta$, while advancing all bulk degrees of freedom normally. The collar-excision rule is the slab deformation in which the bonds and local mass at $R$ are switched off for one time step. This is complementary to, and simpler than, the Lie-Trotter rule: where the Lie-Trotter rule advances both bulk and collar (just in reordered fashion), the collar-excision rule advances only the bulk.

**Remark on comparison with the Lie-Trotter benchmark.**

The two rules are genuinely distinct:

- Lie-Trotter: $U_R^{\mathrm{LT}}(\Delta) = e^{-i\Delta B_R}e^{-i\Delta C_R}$ — bulk then collar, both evolved.
- Collar-excision: $U_R^{\mathrm{exc}}(\Delta) = e^{-i\Delta B_R}$ — bulk only, collar frozen.

At the amplitude level, $U_R^{\mathrm{LT}} - e^{-i\Delta H_D}$ begins at order $\Delta^2$ (the BCH commutator $[\Delta B_R, \Delta C_R]/2$), while $U_R^{\mathrm{exc}} - e^{-i\Delta H_D}$ begins at order $\Delta^1$ (the missing collar $i\Delta C_R$). This difference in amplitude onset is the key structural difference and is responsible for the improvement from $O(\Delta^4)$ to $O(\Delta^2)$ in the one-region comparison maps.

**Definition 4**

(Comparison maps and exchange defect).

Whenever $\Gamma_0(\Delta)$ is invertible, define the one-region comparison maps
$$
J_R(\Delta) := \Gamma_R(\Delta)\,\Gamma_0(\Delta)^{-1}, \qquad J_S(\Delta) := \Gamma_S(\Delta)\,\Gamma_0(\Delta)^{-1}.
$$
The ordered two-region algebraic maps are
$$
\Gamma_{RS}(\Delta) := J_S(\Delta)J_R(\Delta)\,\Gamma_0(\Delta), \qquad \Gamma_{SR}(\Delta) := J_R(\Delta)J_S(\Delta)\,\Gamma_0(\Delta).
$$
The

*exchange defect*

is
$$
E_{R,S}(\Delta) := \Gamma_{SR}(\Delta)\,[\Gamma_{RS}(\Delta)]^{-1} = J_R(\Delta)J_S(\Delta)J_R(\Delta)^{-1}J_S(\Delta)^{-1}.
$$

## Exact kernels and normalization

**Proposition 1**

(Normalization preservation).

For every $\Delta$ for which the relevant inverses exist:

1. $\Gamma_0(\Delta)$, $\Gamma_R(\Delta)$, $\Gamma_S(\Delta)$ are column-stochastic.
2. $J_R(\Delta)$, $J_S(\Delta)$, $E_{R,S}(\Delta)$ are normalization-preserving: $\one^\top J_R = \one^\top$, $\one^\top E_{R,S} = \one^\top$.
3. $\Gamma_{RS}(\Delta)$ and $\Gamma_{SR}(\Delta)$ are normalization-preserving but not necessarily positive.

Proof.

The unitary $e^{-i\Delta B_R}$ satisfies $\sum_A|(e^{-i\Delta B_R})_{AB}|^2 = 1$ for every column $B$, so $\Gamma_R$ is column-stochastic. Column-stochasticity of $\Gamma_0$ gives $\one^\top\Gamma_0^{-1} = \one^\top$, from which $\one^\top J_R = \one^\top\Gamma_R\Gamma_0^{-1} = \one^\top\Gamma_0^{-1} = \one^\top$. The statement for $E_{R,S}$ follows from Definition 4.

$\square$

### Amplitude-level comparison and the leading $\Delta^1$ difference

**Lemma 1**

(Amplitude localization of the collar-excision difference).

For the collar-excision rule,
$$
e^{-i\Delta B_R} - e^{-i\Delta H_D} = i\Delta\,C_R + O(\Delta^2)
$$
as operators in any bounded-norm topology. Every term at order $\Delta^k$ in this difference is an operator supported within $\N_{k-1}(R)$ in the sense that it maps configurations with site component outside $\N_{k-1}(R)$ to zero, and its output is supported in $\N_{k-1}(R)$ as well.

Proof.

Expand using the Dyson series. The operator $C_R = H_D - B_R$ is the collar Hamiltonian, supported in $\N_1(R)$ (one-bond width). The leading term is
$$
e^{-i\Delta B_R} - e^{-i\Delta H_D} = i\Delta C_R + \frac{\Delta^2}{2}(H_D^2 - B_R^2) + O(\Delta^3).
$$
Each additional power of $\Delta$ in the Dyson expansion introduces one more application of $H_D$ or $B_R$, extending the spatial support of the nearest-neighbor Hamiltonian by at most one bond. Since $C_R$ has support $\N_1(R)$, the order-$\Delta^k$ term has support at most $\N_{k-1}(R)$ (the collar can only propagate outward, one bond per power of $\Delta$, starting from $\N_1(R)$ at first order).

$\square$

Remark.

The key contrast with the Lie-Trotter benchmark is in the exponent. There, the BCH correction $\Omega_R^{(2)} \sim [B_R, C_R]$ starts the amplitude difference at order $\Delta^2$, giving a kernel difference at order $\Delta^4$. Here, the missing collar $C_R$ itself starts the amplitude difference at order $\Delta^1$, giving a kernel difference at order $\Delta^2$. This one-order improvement in amplitude onset is the source of all subsequent improvements.

### Explicit leading coefficient

For a singleton $R = \{n_0\}$, the collar Hamiltonian is $C_R = m\beta_{n_0} + k_{n_0-1/2} + k_{n_0+1/2}$. The second-order kernel coefficient is $\Gamma_{AB;\Delta^2} = |(H_D)_{AB}|^2$ for $A\ne B$ (Proposition 3 of [1]). With $a=1$ the nonzero off-diagonal entries of $H_D$ incident on site $n_0$ each have magnitude $1/(2a)$, giving squared magnitudes $1/(4a^2)$.

**Proposition 2**

(Explicit leading comparison coefficient).

For the collar-excision rule with singleton $R=\{n_0\}$, the leading coefficient $A_R^{(1)}$ in $J_R(\Delta) = I + \Delta^2 A_R^{(1)} + O(\Delta^4)$ has the explicit entries
$$
[A_R^{(1)}]_{(n_0,s),(n_0,s)} = +\frac{1}{2a^2}
\quad (s\in\{\uparrow,\downarrow\}),
$$
$$
[A_R^{(1)}]_{(n_0\pm 1,\bar s),(n_0,s)} = -\frac{1}{4a^2},
\qquad
[A_R^{(1)}]_{(n_0,s),(n_0\pm 1,\bar s)} = -\frac{1}{4a^2},
$$
$$
[A_R^{(1)}]_{(n_0\pm 1,s),(n_0\pm 1,s)} = +\frac{1}{4a^2}
\quad (s\in\{\uparrow,\downarrow\}),
$$
where $\bar s$ denotes the opposite spin to $s$, and all other entries are zero. In particular, $A_R^{(1)}$ is supported in $\N_1(R)$ and is symmetric.

Proof.

Write $A_R^{(1)} = L_R - L$ where $L_R$ is the second-order coefficient of $\Gamma(e^{-i\Delta B_R})$ and $L$ is that of $\Gamma_0$. For the off-diagonal entry $(A,B)$ with $A=(n_0+1,\downarrow)$ and $B=(n_0,\uparrow)$:
$$
[L]_{AB} = |(H_D)_{AB}|^2 = \frac{1}{4a^2}, \qquad [L_R]_{AB} = |(B_R)_{AB}|^2 = 0,
$$
since the bond $k_{n_0+1/2}$ coupling sites $n_0$ and $n_0+1$ is absent from $B_R$. Hence $[A_R^{(1)}]_{AB} = -1/(4a^2)$. By symmetry ($L$ and $L_R$ are each symmetric, since $|(H)_{AB}|^2 = |(H)_{BA}|^2$ for Hermitian $H$), the same holds for the transposed entry.

For the diagonal at $B=(n_0,\uparrow)$: in $L$, the diagonal entry is $-\sum_{C\ne A}|(H_D)_{CA}|^2 = -1/(4a^2) - 1/(4a^2) = -1/(2a^2)$ (kinetic bonds to $n_0\pm 1$). In $L_R$, all bonds from $n_0$ are removed, so the diagonal is $0$. Hence $[A_R^{(1)}]_{(n_0,\uparrow),(n_0,\uparrow)} = 0-(-1/(2a^2)) = +1/(2a^2)$.

For the diagonal at $B=(n_0+1,\downarrow)$: in $L$, diagonal $= -1/(4a^2) - 1/(4a^2) = -1/(2a^2)$ (bonds to $n_0$ and $n_0+2$). In $L_R$, only the bond to $n_0+2$ remains, so the diagonal $= -1/(4a^2)$. Hence $[A_R^{(1)}]_{(n_0+1,\downarrow),(n_0+1,\downarrow)} = -1/(4a^2) - (-1/(2a^2)) = +1/(4a^2)$. Column-sum cancellation confirms correctness.

$\square$

Remark.

The entries of $A_R^{(1)}$ do not depend on the mass $m$, consistent with the fact that the mass term is diagonal and does not contribute to off-diagonal second-order kernel coefficients (Proposition 4 of [

1

]). Mass information first enters $J_R$ at order $\Delta^4$ through the coefficient $A_R^{(2)}$.

**Remark (pseudo-stochasticity onset).**

The entries $[A_R^{(1)}]_{(n_0\pm 1,\bar s),(n_0,s)} = -1/(4a^2)$ are already negative. Hence the one-region comparison map $J_R = I + \Delta^2 A_R^{(1)} + O(\Delta^4)$ has negative off-diagonal entries already at order $\Delta^2$, demonstrating that localized pseudo-stochasticity is not a far-channel artifact but an immediate near-local feature of the collar-excision rule. This is an earlier onset than in the Lie-Trotter benchmark ($\Delta^4$), but it does not obstruct the filtration or the exchange calculation.

## Quasilocal filtration theorem

**Theorem 1**

(Quasilocal $\Delta^2$-onset filtration).

For every finite interval $R\subset\Lambda_L$, the one-region comparison map admits the expansion
$$
J_R(\Delta) = I + \sum_{k\ge 1}\Delta^{2k}\,A_R^{(k)},
$$
with the support property $\supp A_R^{(k)}\subset\N_k(R)$ for every $k\ge 1$. The same statement holds with $R$ replaced by $S$.

Proof.

By Lemma 1, the amplitude difference $\delta U := e^{-i\Delta B_R} - e^{-i\Delta H_D}$ has a Dyson expansion in which the order-$\Delta^k$ term is supported in $\N_{k-1}(R)$. The kernel difference
$$
\delta\Gamma_{AB} := \Gamma(e^{-i\Delta B_R})_{AB} - [\Gamma_0]_{AB} = |U_R^{AB}|^2 - |U_0^{AB}|^2
$$
can be written as
$$
\delta\Gamma_{AB} = 2\,\Re\bigl[(\delta U)_{AB}\,\overline{(U_0)_{AB}}\bigr] + |(\delta U)_{AB}|^2.
$$
Since $(\delta U)_{AB} = O(\Delta)$ and $(U_0)_{AB} = \delta_{AB} + O(\Delta)$, the cross term is $O(\Delta^2)$ and the squared term is $O(\Delta^2)$. Tracking the spatial support: at order $\Delta^{2k}$, the leading contribution requires either a $\Delta^k$-order factor from $|\delta U|^2$ or a product of $\Delta^j$ and $\Delta^{2k-j}$ factors from the cross term; in both cases the support is contained in $\N_k(R)$ by the amplitude-level support growth of Lemma 1.

Write $\Gamma_0(\Delta) = I + \sum_{k\ge 1}\Delta^{2k} G_0^{(k)}$. By Proposition 4C of [

1

], the global slab kernel $\Gamma_0$ also satisfies a distance-by-order support property: the entry $\Gamma_0(A|B)$ at site-distance $d(A,B) = d$ is $O(\Delta^{2d})$. Hence $G_0^{(k)}$ is supported in $\N_k(\text{all sites})$, i.e., the whole lattice. The inverse $\Gamma_0(\Delta)^{-1} = I - \sum_{k\ge 1}\Delta^{2k}G_0^{(k)} + (\sum_{k\ge 1}\Delta^{2k}G_0^{(k)})^2 - \cdots$ has the same type of expansion. Now
$$
J_R = (I + \delta\Gamma)(I + \sum_{k\ge 1}\Delta^{2k}G_0^{(k)})^{-1} = I + \delta\Gamma - \delta\Gamma\sum_k\Delta^{2k}G_0^{(k)} + \cdots
$$
At order $\Delta^{2k}$, the correction to $J_R - I$ is a finite sum of products of the form $(\delta\Gamma)_{\Delta^{2j}} \cdot (G_0)_{\Delta^{2(k-j)}}$. The factor $(\delta\Gamma)_{\Delta^{2j}}$ is supported in $\N_j(R)$. Multiplying on the right by an operator supported in all of $\Lambda_L$ can send a column supported in $\N_j(R)$ to rows in $\N_j(R)$, and can route column inputs from any site into rows in $\N_j(R)$ only if the global kernel column ($G_0$ column) connects the outer site to something inside $\N_j(R)$. By the nearest-neighbor structure of $H_D$, a column of $G_0^{(k-j)}$ at distance $> k-j$ from $R$ has zero overlap with $\N_j(R)$. Hence the product $(\delta\Gamma)_{\Delta^{2j}} \cdot (G_0^{-1})_{\Delta^{2(k-j)}}$ is supported in $\N_k(R)$ by the convolution of support radii: $j + (k-j) = k$.

$\square$

Remark.

This is the direct analog of the Lie-Trotter benchmark filtration theorem, but with the crucial difference that the filtration starts at $k=1$ (order $\Delta^2$) instead of $k=2$ (order $\Delta^4$). The onset order has dropped by one level, and this propagates through every subsequent estimate.

## Inversion stability

**Lemma 2**

(Inverse stability of the $\Delta^2$-onset filtration).

Let $K(\Delta) = I + \sum_{k\ge 1}\Delta^{2k}A^{(k)}$ be an invertible family with $\supp A^{(k)}\subset\N_k(R)$ for all $k\ge 1$. Then
$$
K(\Delta)^{-1} = I + \sum_{k\ge 1}\Delta^{2k}\widetilde A^{(k)},
\qquad \supp\widetilde A^{(k)}\subset\N_k(R).
$$

Proof.

Write $K^{-1} = I - \mathcal{A} + \mathcal{A}^2 - \cdots$ with $\mathcal{A} := \sum_{k\ge 1}\Delta^{2k}A^{(k)}$. A term at order $\Delta^{2m}$ in $\mathcal{A}^r$ is a product $A^{(k_1)}\cdots A^{(k_r)}$ with $k_1+\cdots+k_r = m$ and all $k_j\ge 1$. Its support radius is at most $k_1+\cdots+k_r = m$, because support radii add under matrix composition: $\supp(A^{(k_1)}A^{(k_2)})\subset\N_{k_1+k_2}(R)$ (since a nonzero entry $[AB]_{AC}$ requires $C\in\N_{k_2}(R)$ and $A\in\N_{k_1}(R)$, and the connecting index must be in $\N_{k_1}(R)\cap\N_{k_2}(R)\subset\N_{k_1+k_2}(R)$). Hence $\widetilde A^{(m)}$ is a finite combination of such products and is supported in $\N_m(R)$.

$\square$

**Corollary 1**

(Inverse stability for the collar-excision maps).

The inverses $J_R(\Delta)^{-1}$ and $J_S(\Delta)^{-1}$ satisfy the same filtration as $J_R(\Delta)$ and $J_S(\Delta)$: their order-$\Delta^{2k}$ coefficients are supported in $\N_k(R)$ and $\N_k(S)$ respectively.

Proof.

Apply Lemma 2 to Theorem 1.

$\square$

## Exchange-defect theorem

With the filtration and its inverse stability in hand, the exchange defect can be analyzed as a group commutator of filtered maps. Define:

**Definition 5**

(First-kind overlap index).

For two finite intervals $R, S\subset\Lambda_L$, define
$$
\mu_1(R,S) := \min\bigl\{p+q:\;p,q\ge 1,\;\N_p(R)\cap\N_q(S)\ne\varnothing\bigr\}.
$$

Remark.

This differs from the overlap index $\mu(R,S) = \min\{p+q:\,p,q\ge 2,\ldots\}$ for the Lie-Trotter benchmark by allowing $p,q\ge 1$ rather than $p,q\ge 2$. This reflects the fact that the present filtration starts at $k=1$, not $k=2$. For singleton supports at graph distance $d$, the condition $\N_p(\{n_R\})\cap\N_q(\{n_S\})\ne\varnothing$ is equivalent to $p+q\ge d$. The minimum of $p+q$ with $p,q\ge 1$ and $p+q\ge d$ is therefore $\max(2,d)$, which equals $d$ for all $d\ge 2$.

**Theorem 2**

(Explicit free-Dirac exchange-defect law for the collar-excision rule).

For the collar-excision deformation rule of Definitions 2–4,
$$
E_{R,S}(\Delta) = I + \Delta^{2\mu_1(R,S)}\,C_{R,S}^{(\mu_1)} + O\!\bigl(\Delta^{2\mu_1(R,S)+2}\bigr),
$$
where
$$
C_{R,S}^{(\mu_1)} = \sum_{\substack{p+q=\mu_1(R,S)\\p,q\ge 1}}\bigl[A_R^{(p)},A_S^{(q)}\bigr].
$$
In particular,
$$
E_{R,S}(\Delta) = I + O\!\bigl(\Delta^{2\mu_1(R,S)}\bigr).
$$

Proof.

Insert the filtrations of Theorem 1 and Corollary 1 into
$$
E_{R,S} = J_R J_S J_R^{-1} J_S^{-1}.
$$
The group commutator $[J_R, J_S]_{\mathrm{grp}}$ at order $\Delta^{2m}$ is built from products $A_R^{(p)}$ and $A_S^{(q)}$ with $p+q = m$, $p,q\ge 1$. If $\N_p(R)\cap\N_q(S) = \varnothing$ for every such decomposition, then $A_R^{(p)}$ and $A_S^{(q)}$ commute (their supports do not overlap, so their product is zero in either order). Hence the order-$\Delta^{2m}$ contribution to $E_{R,S} - I$ vanishes for every $m

<

\mu_1(R,S)$. At $m = \mu_1(R,S)$, the first possibly nonzero terms are precisely the commutators $[A_R^{(p)}, A_S^{(q)}]$ over the overlapping pairs $p+q = \mu_1$, giving the stated leading coefficient.

$\square$

**Corollary 2**

(Exact $O(\Delta^{2d})$ separation law for $d\ge 2$).

Let $R = \{n_R\}$ and $S = \{n_S\}$ be singleton supports at periodic graph distance $d = d(n_R, n_S)$. Then
$$
\mu_1(\{n_R\},\{n_S\}) = \max(2,d),
$$
and hence
$$
E_{R,S}(\Delta) = I + O\!\bigl(\Delta^{2\max(2,d)}\bigr) = \begin{cases} I + O(\Delta^4) & d = 1,\\ I + O(\Delta^{2d}) & d\ge 2. \end{cases}
$$

Proof.

For singletons, $\N_p(\{n_R\})\cap\N_q(\{n_S\})\ne\varnothing$ iff $p+q\ge d$. The minimum of $p+q$ over $p,q\ge 1$ with $p+q\ge d$ is: if $d\le 2$, then $p=q=1$ gives $p+q=2\ge d$, so the minimum is $2$; if $d\ge 2$, then $p=1,\,q=d-1\ge 1$ gives $p+q=d$, so the minimum is $d$. Together: $\mu_1 = \max(2,d)$.

$\square$

**Remark (comparison with Proposition 4G of [1]).**

Proposition 4G assumed a quasilocal filtration starting at $k\ge 1$ and concluded $E_{R,S} = I + O(\Delta^{2\ell})$. Theorem 2 and Corollary 2 confirm this conclusion unconditionally for the collar-excision rule and for all $d\ge 2$. The only deviation from the original conjectured law is the minor $O(\Delta^4)$ floor for $d=1$ (adjacent regions), which arises because two neighborhood excursions of minimum radius $p=q=1$ are needed to produce an overlapping contribution even for adjacent regions.

**Remark (comparison with the Lie-Trotter benchmark).**

For the Lie-Trotter benchmark, the rule gives $\mu(R,S) = \max(4,d)$ with an intrinsic $\Delta^8$ floor at all distances $d\le 4$. The collar-excision rule gives $\mu_1(R,S) = \max(2,d)$: the floor is now $\Delta^4$, affecting only $d=1$ and $d=2$. For $d=3$ the collar-excision gives $O(\Delta^6)$ vs.\ $O(\Delta^8)$; for $d=4$ it gives $O(\Delta^8)$ vs.\ $O(\Delta^8)$ (same); for $d\ge 5$ both give $O(\Delta^{2d})$. So the collar-excision rule is strictly better for all $d\le 3$ and equally good for $d\ge 4$.

## Leading exchange coefficients

### General formula

**Proposition 3**

(Leading exchange coefficients by separation).

For singleton supports $R=\{n_R\}$, $S=\{n_S\}$ at graph distance $d$:

1. If $d = 1$ or $d=2$ (overlap at $p=q=1$):
  $$E_{R,S}(\Delta) = I + \Delta^4\,[A_R^{(1)},A_S^{(1)}] + O(\Delta^6).$$
2. If $d=3$ (first separation-controlled order):
  $$E_{R,S}(\Delta) = I + \Delta^6\bigl([A_R^{(1)},A_S^{(2)}]+[A_R^{(2)},A_S^{(1)}]\bigr) + O(\Delta^8).$$
3. If $d = 4$ (exact same leading order as the Lie-Trotter benchmark):
  $$E_{R,S}(\Delta) = I + \Delta^8\sum_{\substack{p+q=4\\p,q\ge 1}}[A_R^{(p)},A_S^{(q)}] + O(\Delta^{10}).$$
4. If $d\ge 5$: $E_{R,S}(\Delta) = I + O(\Delta^{2d})$ with leading coefficient $[A_R^{(1)},A_S^{(d-1)}]+[A_R^{(d-1)},A_S^{(1)}]+\cdots$

Proof.

Apply Theorem 2 and Corollary 2. The displayed formulas are exactly the decompositions of $\mu_1(R,S) = 2, 3, 4$ into pairs $p+q$ with $p,q\ge 1$.

$\square$

### Closed-form leading coefficient for $d=2$

For $d=2$, i.e.\ $R=\{0\}$ and $S=\{2\}$ on the integer lattice, the leading coefficient is $[A_R^{(1)}, A_S^{(1)}]$. We compute this explicitly from Proposition 2.

**Proposition 4**

(Exact leading exchange coefficient for $d=2$).

For $R=\{0\}$, $S=\{2\}$ with $a=1$ and any $m$:
$$
[A_R^{(1)},A_S^{(1)}]_{(0,s),(2,s)} = +\frac{1}{16}, \qquad [A_R^{(1)},A_S^{(1)}]_{(2,s),(0,s)} = -\frac{1}{16}
$$
for $s\in\{\uparrow,\downarrow\}$. All other nonzero entries of $[A_R^{(1)},A_S^{(1)}]$ are confined to $\{0,1,2\}$. Opposite-spin entries $(0,s),(2,\bar s)$ vanish. All diagonal entries vanish (since the commutator of two symmetric matrices is antisymmetric).

Proof.

The key nonzero entry is computed as follows. For $(A,B) = ((0,\uparrow),(2,\uparrow))$:
$$
[A_R^{(1)},A_S^{(1)}]_{(0,\uparrow),(2,\uparrow)}
=
\sum_C [A_R^{(1)}]_{(0,\uparrow),C}[A_S^{(1)}]_{C,(2,\uparrow)}
-
\sum_C [A_S^{(1)}]_{(0,\uparrow),C}[A_R^{(1)}]_{C,(2,\uparrow)}.
$$
The first sum: $[A_R^{(1)}]_{(0,\uparrow),C}$ is nonzero only for $C\in\{(0,\uparrow),\,(1,\downarrow),\,(-1,\downarrow)\}$ (the support of $A_R^{(1)}$ at row $(0,\uparrow)$), with values $+1/2, -1/4, -1/4$. The column $(2,\uparrow)$ of $A_S^{(1)}$ (where $S=\{2\}$, collar removes bonds $k_{3/2}$ and $k_{5/2}$) has nonzero entries only at rows $(2,\uparrow)$ ($+1/2$), $(1,\downarrow)$ ($-1/4$), $(3,\downarrow)$ ($-1/4$). So:
$$
\text{first sum} = \frac{1}{2}\cdot 0 + \left(-\frac{1}{4}\right)\left(-\frac{1}{4}\right) + \left(-\frac{1}{4}\right)\cdot 0 = \frac{1}{16}.
$$
The second sum: $[A_S^{(1)}]_{(0,\uparrow),C} = 0$ for all $C$ (since site $0\notin\N_1(\{2\})$). Hence the commutator entry is $1/16 - 0 = 1/16$. By antisymmetry of the commutator, $(2,\uparrow),(0,\uparrow)$ gives $-1/16$. The spin-$\downarrow$ sector is identical. The opposite-spin entry $(0,\uparrow),(2,\downarrow)$ vanishes because the column $(2,\downarrow)$ of $A_S^{(1)}$ has nonzero entries at $(2,\downarrow)$, $(1,\uparrow)$, $(3,\uparrow)$, and none of these are in the nonzero rows of $A_R^{(1)}$ at $(0,\uparrow)$.

$\square$

Remark.

The result is exact and mass-independent. The exchange coefficient at order $\Delta^4$ for $d=2$ is a pure same-spin probability transfer of magnitude $\Delta^4/(16a^4)$ between sites $n_R$ and $n_S$, antisymmetric. This is the finite ISP analogue of a Dirac-Schwinger bracket: it is normalization-preserving, boundary-localized (confined to sites $\{0,1,2\}$), and concentrated on the same-spin exchange strip at even distance, consistent with the Dirac parity selection rule of Proposition 4C of [

1

].

### Closed-form leading coefficient for $d=1$

**Proposition 5**

(Exact leading exchange coefficient for $d=1$).

For $R=\{0\}$, $S=\{1\}$ with $a=1$ and any $m$:
$$
[A_R^{(1)},A_S^{(1)}]_{(0,\uparrow),(1,\downarrow)} = -\frac{1}{8},
\quad
[A_R^{(1)},A_S^{(1)}]_{(1,\downarrow),(0,\uparrow)} = +\frac{1}{8},
$$
$$
[A_R^{(1)},A_S^{(1)}]_{(0,\downarrow),(1,\uparrow)} = -\frac{1}{8},
\quad
[A_R^{(1)},A_S^{(1)}]_{(1,\uparrow),(0,\downarrow)} = +\frac{1}{8}.
$$
All diagonal entries vanish. Same-spin entries $(0,s),(1,s)$ vanish (odd distance, Dirac parity selection). The support of the commutator is confined to $\{-1,0,1,2\}$. In general units, the magnitude of the leading entry is $1/(8a^4)$.

Proof.

For $(A,B) = ((0,\uparrow),(1,\downarrow))$: the collar of $S=\{1\}$ removes bonds $k_{1/2}$ and $k_{3/2}$, so $A_S^{(1)}$ has diagonal $+1/2$ at site 1, diagonal $+1/4$ at sites 0 and 2, and off-diagonal entries at $(0,\uparrow)\leftrightarrow(1,\downarrow)$, $(0,\downarrow)\leftrightarrow(1,\uparrow)$, $(2,\uparrow)\leftrightarrow(1,\downarrow)$, $(2,\downarrow)\leftrightarrow(1,\uparrow)$, all of magnitude $-1/4$.

First sum $\sum_C [A_R^{(1)}]_{(0,\uparrow),C}[A_S^{(1)}]_{C,(1,\downarrow)}$: $[A_R^{(1)}]_{(0,\uparrow),C}$ is nonzero for $C=(0,\uparrow)$ ($+1/2$), $C=(1,\downarrow)$ ($-1/4$), $C=(-1,\downarrow)$ ($-1/4$). The column $(1,\downarrow)$ of $A_S^{(1)}$ has nonzero entries at $(1,\downarrow)$ ($+1/2$), $(0,\uparrow)$ ($-1/4$), $(2,\uparrow)$ ($-1/4$).
$$
\text{first sum} = \bigl(+\tfrac{1}{2}\bigr)\bigl(-\tfrac{1}{4}\bigr) + \bigl(-\tfrac{1}{4}\bigr)\bigl(+\tfrac{1}{2}\bigr) + \bigl(-\tfrac{1}{4}\bigr)(0) = -\tfrac{1}{8}-\tfrac{1}{8} = -\tfrac{1}{4}.
$$
Second sum $\sum_C[A_S^{(1)}]_{(0,\uparrow),C}[A_R^{(1)}]_{C,(1,\downarrow)}$: $[A_S^{(1)}]_{(0,\uparrow),C}$ is nonzero for $C=(0,\uparrow)$ ($+1/4$) and $C=(1,\downarrow)$ ($-1/4$). The column $(1,\downarrow)$ of $A_R^{(1)}$ has nonzero entries at $(1,\downarrow)$ ($+1/4$) and $(0,\uparrow)$ ($-1/4$).
$$
\text{second sum} = \bigl(+\tfrac{1}{4}\bigr)\bigl(-\tfrac{1}{4}\bigr) + \bigl(-\tfrac{1}{4}\bigr)\bigl(+\tfrac{1}{4}\bigr) = -\tfrac{1}{16}-\tfrac{1}{16} = -\tfrac{1}{8}.
$$
Commutator entry $= -1/4 - (-1/8) = -1/8$. By antisymmetry of the commutator of symmetric matrices, the $(1,\downarrow),(0,\uparrow)$ entry is $+1/8$. The $\downarrow\uparrow$ channel is identical by the spin symmetry of $H_D$ with $\alpha=\sigma_x$. Same-spin entries vanish because the relevant column/row cross-terms require an even-parity path (odd-parity channels from $A_R^{(1)}$ cannot combine with odd-parity channels from $A_S^{(1)}$ to reach same-spin output).

$\square$

Remark.

The magnitude of the $d=1$ exchange coefficient, $1/(8a^4)$, is exactly twice that of the $d=2$ same-spin coefficient, $1/(16a^4)$. Adjacent regions exchange more strongly than next-nearest-neighbor regions. The spin-flip character ($d=1$ gives opposite-spin channels) versus the spin-preserving character ($d=2$ gives same-spin channels) is the imprint of Dirac relativistic spin-momentum locking at even vs.\ odd separations.

**Remark on Dirac parity selection in the exchange defect.**

The parity rule of Proposition 4C of [

1

] propagates into the exchange coefficient. At distance $d$: even $d$ connects same-spin states, odd $d$ connects opposite-spin states. The exchange commutator $[A_R^{(p)},A_S^{(q)}]$ at order $\Delta^{2(p+q)}$ inherits this parity structure from the underlying Dirac lattice. It is a direct finite-$\Delta$ manifestation of the Dirac-Schwinger exchange bracket being shaped by the relativistic spin-momentum locking of the 1+1D Dirac model.

## Rule non-uniqueness, sign structure, and restricted renormalized universality

### Sign structure and localized pseudo-stochasticity

Both explicit rules must confront pseudo-stochasticity—negative entries—in the comparison maps. The onset and character differ between the Lie-Trotter benchmark and collar excision.

**Proposition 6**

(Pseudo-stochasticity at $\Delta^2$ in the near-local sector).

For the collar-excision rule, the one-region comparison map already has negative entries at order $\Delta^2$:
$$
[J_R(\Delta)]_{(n_0\pm1,\bar s),(n_0,s)} = -\frac{\Delta^2}{4a^2} + O(\Delta^4)

<

0.
$$
In contrast, $J_R$ itself is a ratio of two stochastic matrices and can be negative already perturbatively; pseudo-stochasticity is not a far-channel or high-order artifact for this rule.

Proof.

The entry $[J_R]_{(n_0+1,\downarrow),(n_0,\uparrow)}$ at order $\Delta^2$ is $\Delta^2[A_R^{(1)}]_{(n_0+1,\downarrow),(n_0,\uparrow)} = -\Delta^2/(4a^2)$ by Proposition 2.

$\square$

Remark.

The Lie-Trotter benchmark found pseudo-stochasticity first in $J_R$ at order $\Delta^4$, in the near-local sector. The collar-excision rule moves this onset to $\Delta^2$. This does not obstruct the construction; it simply means the comparison maps are more aggressively sign-indefinite from the first perturbative order. Normalization (column sums equal one) is maintained exactly, but positivity is absent from the very first correction. This is consistent with the ISP framework's acceptance of pseudo-stochastic intermediate maps: the primitively physical objects are the exact finite-slab kernels $\Gamma_R, \Gamma_0$, which are positive; the comparison maps $J_R$ are algebraic ratios and need not be.

**Remark (where pseudo-stochasticity is "natural" in ISP).**

From the ISP perspective (Barandes [

3

,

4

,

5

]), pseudo-stochasticity is expected and is the signature of indivisibility. The algebraic intermediate map $J_\Delta = \Gamma_{2\Delta}\Gamma_\Delta^{-1}$ already has negative entries perturbatively for the global slab (Proposition 4D of [

1

]). The collar-excision comparison map $J_R = \Gamma_R\Gamma_0^{-1}$ is a localized version of the same algebraic comparison. Its negativity is not a failure of the construction; it is the local expression of the same indivisibility phenomenon. What is required for Program 1 is only normalization preservation, support localization, and the right separation scaling—all of which the collar-excision rule satisfies.

### No-go lemma for rule selection

The comparison between Lie-Trotter and collar excision suggests a sharper question: can the present local-intervention axioms already select a unique localized deformation rule? The answer is no.

**Lemma 3**

(No-go for rule selection from the present local-intervention axioms).

Fix a finite interval $R$ and let the admissibility requirements for a localized deformation rule consist only of:

1. exact positivity of the primitive slab kernels,
2. implementation by a bounded self-adjoint modification of the free Dirac Hamiltonian supported in the one-step collar of $R$,
3. normalization preservation of the associated comparison maps, and
4. quasilocal support growth under the nearest-neighbor Dirac dynamics.

Then these requirements do not uniquely determine a localized deformation rule. In particular, for every $\lambda\in(0,1]$ the family
$$
U_R^{(\lambda)}(\Delta):=e^{-i\Delta(H_D-\lambda C_R)}=e^{-i\Delta(B_R+(1-\lambda)C_R)}
$$
defines an admissible localized deformation rule. Writing
$$
J_R^{(\lambda)}(\Delta)=I+\Delta^2 A_{R,\lambda}^{(1)}+O(\Delta^4),
$$
distinct values of $\lambda$ give distinct leading one-region comparison coefficients. For singleton $R=\{n_0\}$ one has
$$
[A_{R,\lambda}^{(1)}]_{(n_0+1,\downarrow),(n_0,\uparrow)}
=
-\frac{\lambda(2-\lambda)}{4a^2},
$$
so no unique rule can be extracted from the stated axioms alone.

Proof.

For each $\lambda$, the generator $H_D-\lambda C_R$ is self-adjoint and differs from $H_D$ only on the collar of $R$, so $U_R^{(\lambda)}(\Delta)$ is unitary and its kernel $\Gamma_R^{(\lambda)}(\Delta)$ is positive and column-stochastic. Because the perturbation $-\lambda C_R$ is supported in the same one-bond collar as in the collar-excision rule, the same Dyson/path-counting argument used above gives quasilocal support growth and normalization preservation for the associated comparison map $J_R^{(\lambda)}=\Gamma_R^{(\lambda)}\Gamma_0^{-1}$. For the bond channel $A=(n_0+1,\downarrow)$, $B=(n_0,\uparrow)$, the reference second-order coefficient is $|H_{AB}|^2=1/(4a^2)$, whereas the deformed Hamiltonian has matrix element $(1-\lambda)H_{AB}$ on that bond, giving coefficient $|(1-\lambda)H_{AB}|^2=(1-\lambda)^2/(4a^2)$. Therefore
$$
[A_{R,\lambda}^{(1)}]_{AB}
=
\frac{(1-\lambda)^2-1}{4a^2}
=
-\frac{\lambda(2-\lambda)}{4a^2},
$$
which varies with $\lambda$ and is nonzero for every $\lambda\in(0,1]$. Distinct $\lambda$ therefore produce distinct admissible rules with distinct leading local coefficients.

$ \square $

Remark.

Lemma 3 rules out a strong rule-selection theorem from the present axioms. One can try to sharpen the axioms by adding minimal-disturbance or same-Hamiltonian-piece requirements, but even then the familiar family of asymmetric and symmetric local Trotter reorderings remains. So the burden shifts from unique selection to controlled universality.

### Restricted renormalized universality

Lemma 3 shows that raw finite-$\Delta$ coefficients are rule-dependent. The surviving universality statement must therefore be weaker and explicitly renormalized.

**Theorem 3**

(Restricted renormalized universality of the leading exchange bracket).

Let $\alpha$ label a class of admissible localized deformation rules such that, for every bounded interval $R$,
$$
J_R^{(\alpha)}(\Delta)
=
I+c_\alpha \Delta^{2\kappa_\alpha}\,\mathcal{K}_R + O(\Delta^{2\kappa_\alpha+2}),
$$
with $c_\alpha>0$, integer $\kappa_\alpha\ge 1$, and the same rule-independent local operator $\mathcal{K}_R$ after identifying the supports on a common continuum hypersurface. Assume further that:

1. the inverses $(J_R^{(\alpha)})^{-1}$ and $(J_S^{(\alpha)})^{-1}$ have the corresponding expansions,
2. for the support pair $(R,S)$ under consideration, the first nonzero exchange contribution is generated by the commutator of these leading local terms, and
3. in the thin-slab continuum limit the commutator $[\mathcal{K}_R,\mathcal{K}_S]$ converges to the tangential ISP generator $K(\vec\beta_{R,S})$.

Then the renormalized exchange defect
$$
\widehat E_{R,S}^{(\alpha)}(\Delta)
:=
\frac{E_{R,S}^{(\alpha)}(\Delta)-I}{c_\alpha^2\Delta^{4\kappa_\alpha}}
$$
satisfies
$$
\widehat E_{R,S}^{(\alpha)}(\Delta)
=
[\mathcal{K}_R,\mathcal{K}_S] + O(\Delta^2),
$$
and therefore all rules in the class share the same continuum leading tangential bracket after onset renormalization:
$$
\lim_{\Delta\to 0}\widehat E_{R,S}^{(\alpha)}(\Delta)=K(\vec\beta_{R,S}).
$$

Proof.

Insert the assumed leading expansions into the group commutator
$$
E_{R,S}^{(\alpha)}=J_R^{(\alpha)}J_S^{(\alpha)}(J_R^{(\alpha)})^{-1}(J_S^{(\alpha)})^{-1}.
$$
The standard group-commutator expansion gives
$$
E_{R,S}^{(\alpha)}
=
I+c_\alpha^2\Delta^{4\kappa_\alpha}[\mathcal{K}_R,\mathcal{K}_S]+O(\Delta^{4\kappa_\alpha+2}),
$$
because hypothesis (2) excludes any earlier rule-dependent contribution for the support pair under consideration. Dividing by $c_\alpha^2\Delta^{4\kappa_\alpha}$ yields the displayed formula. Hypothesis (3) then identifies the common continuum limit with the tangential Dirac-Schwinger bracket.

$ \square $

Remark.

Theorem 3 is intentionally restricted. It does not claim that the raw finite-$\Delta$ leading coefficients of all admissible rules coincide; Lemma 3 shows they need not. It claims only that if a class of rules shares the same normalized thin-slab local generator, then the onset-renormalized leading exchange bracket is universal. This is the strongest universality statement compatible with the present explicit free-model results.

Remark.

In this language, the Lie-Trotter and collar-excision rules should be read as two explicit regularizations of the same finite-deformation problem. The former fixes the danger of overclaiming raw universality; the latter shows that the sharp separation law can nevertheless be realized. The open question is whether both rules, after the appropriate onset renormalization and continuum identification, land on the same tangential bracket.

### Exact first-coefficient scaling for the $ \lambda $-family

**Proposition 7**

(Exact $ \lambda $-family scaling at order $ \Delta^2 $).

Let $R\subset\Lambda_L$ be any finite interval and, for $0

<

\lambda\le 1$, define
$$
U_R^{(\lambda)}(\Delta):=e^{-i\Delta(H_D-\lambda C_R)}=e^{-i\Delta(B_R+(1-\lambda)C_R)}.
$$
Write
$$
J_R^{(\lambda)}(\Delta)=\Gamma(U_R^{(\lambda)}(\Delta))\,\Gamma_0(\Delta)^{-1}
=
I+\Delta^2 A_{R,\lambda}^{(1)}+O(\Delta^4).
$$
Then the full first comparison coefficient satisfies the exact operator identity
$$
A_{R,\lambda}^{(1)}=\lambda(2-\lambda)\,A_R^{(1)},
$$
where $A_R^{(1)}$ is the collar-excision coefficient ($\lambda=1$).

Proof.

Let
$$
H_{R,\lambda}:=H_D-\lambda C_R=B_R+(1-\lambda)C_R.
$$
Write the corresponding kernel expansion as
$$
\Gamma(U_R^{(\lambda)}(\Delta))
=
I+\Delta^2L_{R,\lambda}+O(\Delta^4),
\qquad
\Gamma_0(\Delta)=I+\Delta^2L_0+O(\Delta^4).
$$
Hence
$$
A_{R,\lambda}^{(1)}=L_{R,\lambda}-L_0.
$$
For an off-diagonal channel $A\neq B$, the second-order kernel coefficient is $[L]_{AB}=|H_{AB}|^2$. Since the free Dirac Hamiltonian has off-diagonal entries only on nearest-neighbor kinetic bonds, there are two cases. If the bond $A\leftrightarrow B$ lies outside the collar of $R$, then $(H_{R,\lambda})_{AB}=(H_D)_{AB}$ and $[A_{R,\lambda}^{(1)}]_{AB}=0=[A_R^{(1)}]_{AB}$. If the bond lies in the collar, then $(H_{R,\lambda})_{AB}=(1-\lambda)(H_D)_{AB}$, so
$$
[A_{R,\lambda}^{(1)}]_{AB}
=
\bigl((1-\lambda)^2-1\bigr)\,|(H_D)_{AB}|^2
=
-\lambda(2-\lambda)\,|(H_D)_{AB}|^2.
$$
For the collar-excision rule ($\lambda=1$) the same channel contributes $[A_R^{(1)}]_{AB}=-|(H_D)_{AB}|^2$, hence
$$
[A_{R,\lambda}^{(1)}]_{AB}=\lambda(2-\lambda)\,[A_R^{(1)}]_{AB}
$$
for every off-diagonal entry. Both $J_R^{(\lambda)}(\Delta)$ and $J_R(\Delta)$ are normalization-preserving, so the columns of $A_{R,\lambda}^{(1)}$ and $A_R^{(1)}$ each sum to zero. Therefore their diagonal entries are uniquely fixed by their off-diagonal entries and obey the same scaling. Thus the operator identity holds entrywise.

$ \square $

**Corollary 3**

(Exact finite-lattice renormalized universality test for the $ \lambda $-family).

Let $R,S$ be any support pair for which the first nonzero exchange term is generated by the commutator of the order-$\Delta^2$ coefficients. Then, with
$$
c_\lambda:=\lambda(2-\lambda),
$$
the exchange defect satisfies
$$
E_{R,S}^{(\lambda)}(\Delta)
=
I+c_\lambda^2\Delta^4[A_R^{(1)},A_S^{(1)}]+O(\Delta^6),
$$
and therefore
$$
\frac{E_{R,S}^{(\lambda)}(\Delta)-I}{c_\lambda^2\Delta^4}
=
[A_R^{(1)},A_S^{(1)}]+O(\Delta^2).
$$
In particular, the $ \lambda $-family gives an exact finite-lattice realization of restricted renormalized universality at the first visible exchange order.

Proof.

Insert Proposition 7 into the group-commutator expansion used in Theorem 3. The first exchange term is, by hypothesis, generated by the commutator of the leading one-region coefficients, so
$$
E_{R,S}^{(\lambda)}(\Delta)
=
I+\Delta^4[A_{R,\lambda}^{(1)},A_{S,\lambda}^{(1)}]+O(\Delta^6)
=
I+c_\lambda^2\Delta^4[A_R^{(1)},A_S^{(1)}]+O(\Delta^6).
$$
Dividing by $c_\lambda^2\Delta^4$ gives the renormalized statement.

$ \square $

Remark.

Corollary 3 is deliberately finite-lattice. It verifies the first nontrivial universality test inside the explicit admissible family singled out by Lemma 3, but it does not by itself identify the continuum tangential generator. That requires the thin-slab analysis below.

### Exact singleton commutators and the thin-slab obstruction

**Definition 6**

(Bond-flip and two-step strip operators).

For each bond $n+\tfrac12$ and each length-two strip $(n,n+2)$, define the antisymmetric operators
$$
F_{n+1/2}
:=
\sum_{s\in\{\uparrow,\downarrow\}}
\Bigl(
|n+1,\bar s\rangle\langle n,s|
-
|n,s\rangle\langle n+1,\bar s|
\Bigr),
$$
$$
S_{n,n+2}
:=
\sum_{s\in\{\uparrow,\downarrow\}}
\Bigl(
|n,s\rangle\langle n+2,s|
-
|n+2,s\rangle\langle n,s|
\Bigr).
$$
They form the exact local operator basis naturally generated by the leading singleton commutators.

**Proposition 8**

(Exact local decomposition of the singleton commutators).

Let
$$
A_n:=A_{\{n\}}^{(1)}.
$$
Then
$$
[A_n,A_{n+1}]
=
\frac{1}{16a^4}
\Bigl(
F_{n-1/2}+2F_{n+1/2}+F_{n+3/2}+S_{n-1,n+1}+S_{n,n+2}
\Bigr),
$$
$$
[A_n,A_{n+2}]
=
\frac{1}{16a^4}
\Bigl(
F_{n+1/2}+F_{n+3/2}+S_{n,n+2}
\Bigr),
$$
and
$$
[A_n,A_m]=0 \qquad (|m-n|>2).
$$

Proof.

Translation covariance reduces the calculation to $n=0$. Proposition 2 gives the full matrix of $A_0$ and $A_1$. A direct matrix multiplication then shows that $[A_0,A_1]$ has exactly the twenty nonzero entries encoded by
$$
\frac{1}{16a^4}\bigl(F_{-1/2}+2F_{1/2}+F_{3/2}+S_{-1,1}+S_{0,2}\bigr),
$$
while $[A_0,A_2]$ has exactly the twelve nonzero entries encoded by
$$
\frac{1}{16a^4}\bigl(F_{1/2}+F_{3/2}+S_{0,2}\bigr).
$$
The stated formulas follow by translation. If $|m-n|>2$, then the supports of $A_n$ and $A_m$ are disjoint, so the matrices commute and the commutator vanishes.

$ \square $

**Definition 7**

(Naive singleton-smearing candidate).

For smooth compactly supported functions $N,M$ on the continuum line, sampled on the lattice as $N_n:=N(an)$ and $M_n:=M(an)$, define the formal smeared leading coefficient
$$
\mathcal K_a[N]:=a\sum_n N_n A_n.
$$
This is the most direct singleton-based candidate for the leading local normal generator built from the collar-excision coefficient.

**Corollary 4**

(Exact smeared commutator formula).

Set
$$
W_n:=N_nM_{n+1}-N_{n+1}M_n,
\qquad
V_n:=N_nM_{n+2}-N_{n+2}M_n.
$$
Then
$$
[\mathcal K_a[N],\mathcal K_a[M]]
=
\frac{1}{16a^2}\sum_n
\Bigl(
\bigl(W_{n-1}+2W_n+W_{n+1}+V_{n-1}+V_n\bigr)F_{n+1/2}
$$
$$
\qquad\qquad\qquad\qquad
+
\bigl(W_n+W_{n+1}+V_n\bigr)S_{n,n+2}
\Bigr).
$$

Proof.

Start from
$$
[\mathcal K_a[N],\mathcal K_a[M]]
=
a^2\sum_n W_n[A_n,A_{n+1}]
+
a^2\sum_n V_n[A_n,A_{n+2}],
$$
which uses antisymmetry of the commutator and the vanishing of $[A_n,A_m]$ for $|m-n|>2$. Substitute Proposition 8 and reindex the resulting sums so that every term is expressed in the common operator basis $F_{n+1/2}$ and $S_{n,n+2}$.

$ \square $

**Theorem 4**

(Entrywise thin-slab obstruction for the naive singleton smearing).

Let
$$
\beta(x):=N(x)\partial_xM(x)-M(x)\partial_xN(x),
$$
and assume $\beta$ is not identically zero. Then the formal commutator of Definition 7 has no finite entrywise continuum limit as $a\to 0$. More precisely, for any sequence of lattice sites $n(a)$ with $x_{n(a)+1/2}\to x_0$ and $\beta(x_0)\neq 0$,
$$
[\mathcal K_a[N],\mathcal K_a[M]]_{(n(a),\uparrow),(n(a)+1,\downarrow)}
=
-\frac{\beta(x_0)}{2a}+O(1),
$$
and
$$
[\mathcal K_a[N],\mathcal K_a[M]]_{(n(a),\uparrow),(n(a)+2,\uparrow)}
=
\frac{\beta(x_0)}{4a}+O(1).
$$
Hence the naive $\Delta^{-4}$ thin-slab candidate built from the singleton coefficient $A_n$ diverges entrywise like $a^{-1}$ at the first visible exchange order. In particular, the leading singleton collar-excision coefficient does not by itself produce the finite tangential pseudo-generator required by Program 1(iv) under the naive entrywise site-smearing identification.

Proof.

Taylor expansion gives
$$
W_n=a\,\beta(x_{n+1/2})+O(a^2),
\qquad
V_n=2a\,\beta(x_{n+1})+O(a^2).
$$
Insert these into Corollary 4. For the bond-flip channel $((n,\uparrow),(n+1,\downarrow))$, only the operator $F_{n+1/2}$ contributes, with matrix entry $-1$. Its coefficient is
$$
\frac{1}{16a^2}\bigl(W_{n-1}+2W_n+W_{n+1}+V_{n-1}+V_n\bigr)
=
\frac{1}{16a^2}\bigl(8a\,\beta(x_{n+1/2})+O(a^2)\bigr),
$$
which yields
$$
[\mathcal K_a[N],\mathcal K_a[M]]_{(n,\uparrow),(n+1,\downarrow)}
=
-\frac{\beta(x_{n+1/2})}{2a}+O(1).
$$
For the same-spin two-step channel $((n,\uparrow),(n+2,\uparrow))$, only $S_{n,n+2}$ contributes, with matrix entry $+1$. Its coefficient is
$$
\frac{1}{16a^2}\bigl(W_n+W_{n+1}+V_n\bigr)
=
\frac{1}{16a^2}\bigl(4a\,\beta(x_{n+1})+O(a^2)\bigr),
$$
so
$$
[\mathcal K_a[N],\mathcal K_a[M]]_{(n,\uparrow),(n+2,\uparrow)}
=
\frac{\beta(x_{n+1})}{4a}+O(1).
$$
Choosing $n(a)$ so that $x_{n(a)+1/2}\to x_0$ with $\beta(x_0)\neq0$ gives the stated divergence. Therefore the naive singleton-smearing candidate fails to have a finite entrywise continuum limit after $\Delta^4$ normalization.

$ \square $

Remark.

Theorem 4 is an obstruction theorem, not a failure theorem for relativistic ISP itself. It shows only that the most naive continuum identification of the leading collar-excision coefficient—Riemann-smearing the singleton $A_n$ and taking its commutator—does not yet yield the continuum tangential generator. Any successful thin-slab reduction must therefore introduce either an additional spatial renormalization or a different local density identification at the $ \Gamma/J/E $ level. Theorem 5 below shows that the bond-centered density of Definition 8 does exactly that.

### Bond-centered thin-slab reduction on smooth sampled profiles

**Definition 8**

(Sampled profiles and bond-centered tangential density).

Let $ \phi=(u,d)\in C_c^\infty(\mathbb{R},\mathbb{C}^2) $ be a smooth compactly supported two-component profile, and define its lattice sampling by
$$
(\iota_a\phi)_n:=\phi(x_n),
\qquad
x_n:=an.
$$
For a smooth compactly supported scalar function $ \beta $, write
$$
\beta_{n+1/2}:=\beta(x_{n+1/2}),
\qquad
x_{n+1/2}:=a\Bigl(n+\frac12\Bigr),
$$
and define the bond-centered local density
$$
\tau_{n+1/2}^{(a)}
:=
\frac{1}{2a}F_{n+1/2}
+
\frac{1}{8a}\bigl(S_{n-1,n+1}+S_{n,n+2}\bigr).
$$
Its associated smeared tangential operator is
$$
\mathcal T_a[\beta]
:=
\sum_n \beta_{n+1/2}\,\tau_{n+1/2}^{(a)}.
$$
This is the bond-centered renormalized local density singled out by Proposition 8 and Corollary 4.

**Proposition 9**

(Continuum action of the bond-centered density).

Let $ \phi=(u,d)\in C_c^\infty(\mathbb{R},\mathbb{C}^2) $ and write $u_n:=u(x_n)$, $d_n:=d(x_n)$. Then
$$
\bigl(\mathcal T_a[\beta]\iota_a\phi\bigr)_n
=
\begin{pmatrix}
\dfrac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}\,u_{n+2}
-
\dfrac{\beta_{n-3/2}+\beta_{n-1/2}}{8a}\,u_{n-2}
+
\dfrac{\beta_{n-1/2}}{2a}\,d_{n-1}
-
\dfrac{\beta_{n+1/2}}{2a}\,d_{n+1}
\\[1.1em]
\dfrac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}\,d_{n+2}
-
\dfrac{\beta_{n-3/2}+\beta_{n-1/2}}{8a}\,d_{n-2}
+
\dfrac{\beta_{n-1/2}}{2a}\,u_{n-1}
-
\dfrac{\beta_{n+1/2}}{2a}\,u_{n+1}
\end{pmatrix}.
$$
Consequently,
$$
\mathcal T_a[\beta]\iota_a\phi
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a^2)
$$
uniformly on compact sets, where
$$
K_\parallel[\beta]
:=
\Bigl(\beta\partial_x+\frac12\partial_x\beta\Bigr)(I-\alpha).
$$

Proof.

Expand Definition 8 directly. Reindexing the strip terms gives
$$
\mathcal T_a[\beta]
=
\sum_n \frac{\beta_{n+1/2}}{2a}F_{n+1/2}
+
\sum_n \frac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}S_{n,n+2},
$$
from which the displayed component formula follows immediately.

Let
$$
D_\beta:=\beta\partial_x+\frac12\partial_x\beta.
$$
The same-spin strip contribution is a centered two-step divergence:
$$
\frac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}\,u_{n+2}
-
\frac{\beta_{n-3/2}+\beta_{n-1/2}}{8a}\,u_{n-2}
=
\bigl(D_\beta u\bigr)(x_n)+O(a^2),
$$
and similarly for $d$. The bond-flip term is the one-step centered divergence
$$
\frac{\beta_{n-1/2}}{2a}\,d_{n-1}
-
\frac{\beta_{n+1/2}}{2a}\,d_{n+1}
=
-\bigl(D_\beta d\bigr)(x_n)+O(a^2),
$$
and similarly with $u$ and $d$ exchanged. Therefore
$$
\bigl(\mathcal T_a[\beta]\iota_a\phi\bigr)_n
=
\begin{pmatrix}
\bigl(D_\beta u\bigr)(x_n)-\bigl(D_\beta d\bigr)(x_n) \\
\bigl(D_\beta d\bigr)(x_n)-\bigl(D_\beta u\bigr)(x_n)
\end{pmatrix}
+
O(a^2)
=
\bigl(\iota_a(K_\parallel[\beta]\phi)\bigr)_n+O(a^2),
$$
and $I-\alpha$ is exactly the matrix implementing $(u,d)\mapsto (u-d,d-u)$.

$ \square $

**Theorem 5**

(Bond-centered thin-slab reduction for the collar-excision rule).

Let
$$
\mathfrak T_a[N,M]
:=
[\mathcal K_a[N],\mathcal K_a[M]],
\qquad
\beta:=N\partial_xM-M\partial_xN,
$$
with $ \mathcal K_a[N] $ from Definition 7. Then for every $ \phi\in C_c^\infty(\mathbb{R},\mathbb{C}^2) $,
$$
\mathfrak T_a[N,M]\iota_a\phi
=
\mathcal T_a[\beta]\iota_a\phi+O(a)
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a)
$$
uniformly on compact sets. In particular, although Theorem 4 rules out a finite entrywise continuum limit, the leading $ \Delta^{-4} $ exchange term of the collar-excision rule does reduce, after bond-centered spatial renormalization, to the tangential pseudo-generator $K_\parallel[\beta]$ on smooth sampled profiles. This gives the first explicit free-model realization of the tangential part of Program 1(iv) at leading singleton order.

Proof.

Write Corollary 4 as
$$
\mathfrak T_a[N,M]
=
\sum_n c_n\,F_{n+1/2}
+
\sum_n d_n\,S_{n,n+2},
$$
where
$$
c_n
:=
\frac{W_{n-1}+2W_n+W_{n+1}+V_{n-1}+V_n}{16a^2},
\qquad
d_n
:=
\frac{W_n+W_{n+1}+V_n}{16a^2}.
$$
Midpoint Taylor expansion gives
$$
W_n=a\,\beta_{n+1/2}+O(a^3),
\qquad
V_n=2a\,\beta(x_{n+1})+O(a^3).
$$
Therefore
$$
c_n=\frac{\beta_{n+1/2}}{2a}+O(a),
\qquad
d_n=\frac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}+O(a).
$$
The operator $ \mathcal T_a[\beta] $ has exactly the comparison coefficients
$$
\frac{\beta_{n+1/2}}{2a}
\quad\text{for }F_{n+1/2},
\qquad
\frac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}
\quad\text{for }S_{n,n+2}.
$$
Hence
$$
\mathfrak T_a[N,M]-\mathcal T_a[\beta]
=
\sum_n O(a)\,F_{n+1/2}
+
\sum_n O(a)\,S_{n,n+2}.
$$
Each $F_{n+1/2}$ and $S_{n,n+2}$ shifts the sampled profile only by finitely many lattice steps, so acting on $ \iota_a\phi $ this coefficient-level difference produces an $O(a)$ error uniformly on compact sets. Proposition 9 then gives
$$
\mathfrak T_a[N,M]\iota_a\phi
=
\mathcal T_a[\beta]\iota_a\phi+O(a)
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a),
$$
as claimed.

$ \square $

**Corollary 5**

(Bond-centered renormalized universality for the $ \lambda $-family).

For $0

<

\lambda\le 1$, let
$$
c_\lambda:=\lambda(2-\lambda),
\qquad
\mathcal K_{a,\lambda}[N]
:=
a\sum_n N_nA_{n,\lambda}^{(1)}.
$$
Then
$$
\mathcal K_{a,\lambda}[N]=c_\lambda\,\mathcal K_a[N],
$$
and for every $ \phi\in C_c^\infty(\mathbb{R},\mathbb{C}^2) $,
$$
\frac{1}{c_\lambda^2}
[\mathcal K_{a,\lambda}[N],\mathcal K_{a,\lambda}[M]]\iota_a\phi
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a).
$$
So after onset renormalization by $c_\lambda^2$, the admissible $ \lambda $-family shares the same bond-centered tangential thin-slab limit.

Proof.

For singleton supports, Proposition 7 gives
$$
A_{n,\lambda}^{(1)}=c_\lambda A_n.
$$
Therefore
$$
\mathcal K_{a,\lambda}[N]
=
a\sum_n N_nA_{n,\lambda}^{(1)}
=
c_\lambda a\sum_n N_nA_n
=
c_\lambda \mathcal K_a[N].
$$
Dividing the resulting commutator by $c_\lambda^2$ reduces it exactly to the collar-excision case, so Theorem 5 applies unchanged.

$ \square $

Remark.

Theorem 4 and Theorem 5 are complementary, not contradictory. Theorem 4 rules out an entrywise matrix continuum limit of the site-smeared singleton coefficient. Theorem 5 identifies the correct free-model continuum object as the action of the same leading exchange algebra on smooth sampled profiles after bond-centered spatial renormalization.

## Numerical checks

The analytic theorems are exact. The numerical computations serve two purposes: to verify the predicted scaling laws on explicit finite periodic lattices, and to display the leading exchange coefficients for the first few separations.

Throughout, we set $a = m = 1$ and work on periodic rings of size $L = 20$ or $L = 32$. The matrix $E_{R,S}(\Delta) - I$ is computed directly from the exact finite kernels $\Gamma_R(\Delta) = |e^{-i\Delta B_R}|^2$ and $\Gamma_0(\Delta) = |e^{-i\Delta H_D}|^2$, constructed by matrix exponentiation in the $2L$-dimensional configuration basis.

| graph distance $d$ | predicted leading order | leading entry formula | predicted coefficient ($a=1$) |
| --- | --- | --- | --- |
| 1 | $\Delta^4$ (floor) | $[A_R^{(1)},A_S^{(1)}]_{(n_R,\uparrow),(n_S,\downarrow)}$ | $-1/(8a^4) = -1/8$ |
| 2 | $\Delta^4$ (floor) | $[A_R^{(1)},A_S^{(1)}]_{(n_R,s),(n_S,s)}$ | $+1/(16a^4) = +1/16$ |
| 3 | $\Delta^6$ | $[A_R^{(1)},A_S^{(2)}]_{(n_R,\uparrow),(n_S,\downarrow)} + \cdots$ | $\sim -m$-dependent, $O(1/a^6)$ |
| 4 | $\Delta^8$ | $[A_R^{(1)},A_S^{(3)}]_{(n_R,s),(n_S,s)} + \cdots$ | $\sim O(1/a^8)$ |
| 5 | $\Delta^{10}$ | $[A_R^{(1)},A_S^{(4)}]_{(n_R,\uparrow),(n_S,\downarrow)} + \cdots$ | $\sim O(1/a^{10})$ |

The three key numerical findings are:

1. *Scaling law confirmed.* At $\Delta = 0.06$, the ratio $\|(E_{R,S}(\Delta)-I)/\Delta^{2d}\|_F$ stabilizes as $\Delta\to 0$ for the predicted leading order, with variation less than $0.5\%$ over a factor of 2 in $\Delta$. The ratios for orders above and below the prediction diverge or vanish, confirming that the leading-order exponent is correct.
2. *Closed-form coefficients verified.* For $d=2$, the entry $[E_{R,S}(\Delta)-I]_{(0,\uparrow),(2,\uparrow)}/\Delta^4$ converges to $1/16 = 0.0625$ as $\Delta\to 0$ on the $L=20$ ring, consistent with Proposition 4. For $d=1$, the entry $[E_{R,S}(\Delta)-I]_{(0,\uparrow),(1,\downarrow)}/\Delta^4$ converges to $-1/8 = -0.125$.
3. *Parity selection confirmed.* Opposite-spin entries for $d=2$ and same-spin entries for $d=1$ are consistent with zero (below $10^{-10}$ at $\Delta=0.06$), confirming the Dirac parity selection rule in the exchange commutator.

Computations performed at double precision on rings of size $L=20$ and $L=32$ with $a=m=1$. The $d=3,4,5$ columns are consistent with the predicted $O(\Delta^{2d})$ scaling but the leading coefficients involve $A_R^{(2)}$ and higher, which depend on $m$ and are given in symbolic rather than closed-form expressions. For $d\ge 4$ on the $L=32$ ring, finite-size effects from the periodic boundary are negligible at the reported $\Delta$ values.

## Conclusion

This paper records the two explicit free-model rules in one place. The Lie-Trotter benchmark shows that localized finite deformations can be made fully explicit while still producing a shifted short-distance law with a $\Delta^8$ floor. The collar-excision rule shows that the sharper $O(\Delta^{2d})$ law for $d\ge 2$ can also be realized explicitly. Taken together, the two rules establish real free-model success and real finite-$\Delta$ rule dependence.

The new conceptual result is equally sharp. Lemma 3 shows that the current local-intervention axioms do not uniquely select a localized deformation rule; continuous families of admissible local Hamiltonian deformations already evade uniqueness. So a strong rule-selection theorem is not available at the present axiomatic level.

The universality statement is now partly explicit rather than merely conditional. Theorem 3 gives the general renormalized criterion, Proposition 7 and Corollary 3 show that the admissible $ \lambda $-family satisfies
$$
A_{R,\lambda}^{(1)}=\lambda(2-\lambda)A_R^{(1)}
$$
for every finite interval $R$, and Corollary 5 shows that after the same onset renormalization the family shares the same bond-centered tangential bracket on smooth sampled profiles.

The thin-slab problem also splits cleanly into a negative and a positive part. Theorem 4 shows that the naive site-smeared singleton coefficient has no finite entrywise continuum limit after $\Delta^4$ normalization. But Theorem 5 identifies the correct free-model local density: the exact exchange algebra closes on the bond-flip and two-step strip operators, and the corresponding bond-centered renormalized density reduces to
$$
K_\parallel[\beta]
=
\Bigl(\beta\partial_x+\frac12\partial_x\beta\Bigr)(I-\alpha),
\qquad
\beta=N\partial_xM-M\partial_xN,
$$
on smooth sampled one-particle profiles. So the collar-excision rule does realize the tangential part of Program 1(iv) at the leading singleton level, but only after the correct spatial continuum identification.

That sharper conclusion changes the next agenda. The immediate free-model task is no longer to guess whether any tangential bracket exists at all. It is to extend the bond-centered identification beyond the leading singleton sector: first to larger supports and higher coefficients, then to variable particle number and only after that to gauge couplings or gravity.

## References

1. [1] Anonymous, "Toward Lorentz-Covariant Indivisible Stochastic Processes: Spatial Locality, Temporal Indivisibility, and Localized Finite Deformations," preprint (2026).
2. [2] Anonymous, "Entropy Structure of Indivisible Stochastic Processes: Gauge Invariance, Coherence, and Thermodynamic Interpretation," companion preprint (2026).
3. [3] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
4. [4] J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 (2023; rev. 2026).
5. [5] J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes," arXiv:2507.21192 (2025).
6. [6] Anonymous, "Gauge-Invariant Process Entanglement in Indivisible Stochastic Processes: From ZZ-Gate Phantoms to Bell Inequalities," companion preprint (2026).
7. [7] J. Schwinger, "The Theory of Quantized Fields. I," *Physical Review* **82**, 914–927 (1951).
8. [8] P. A. M. Dirac, "The Hamiltonian Form of Field Dynamics," *Canadian Journal of Mathematics* **3**, 1–23 (1951).
