# Truncated Compact U(1) Gauge-Matter Benchmark in Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

*Finite $K$-truncated $U(1)$ matter-link sectors, exact physical-sector elimination, Coulomb-string reduced interaction, and finite-block validation*

Author: Felix Robles Elvira

Draft preprint

Date: April 2026

Paper 16 in the relativistic ISP sequence; first QED-adjacent continuation of the $Z_2$ benchmark of Paper 15

## Abstract

Paper 15 closed the first benchmark in which exact physical-sector elimination produces a genuinely interacting reduced matter Hamiltonian inside a finite $Z_2$ matter-link configuration space. The present paper takes the next conservative step on the same axis: the gauge group is replaced by compact $U(1)$ truncated at integer electric charge $|e|\le K$, with fermionic matter on a one-dimensional open lattice. The matter-link configuration space and all primitive ISP objects remain exact finite matrices on every fixed benchmark size $L$ and truncation $K$, and the gauge content is now quantitatively richer: the reduced diagonal interaction after elimination is a quadratic Coulomb-string functional of the occupation configuration, not merely a parity string.

We prove exact local $U(1)$ gauge symmetry, exact Gauss-sector decomposition, and exact physical-sector elimination on each compatible pair $(\mathbf g,w)$ consisting of a Gauss-sector label and a left-boundary flux seed $w\in\{-K,\dots,K\}$. The transported reduced Hamiltonian contains ordinary nearest-neighbor fermion hopping together with a Coulomb-string electric term
$$
\tfrac{g^{2}}{2}\sum_{n=0}^{L-2}\!\left[w+\sum_{j=0}^{n}\!\bigl(\widehat N_j-q_j^{\mathrm{bg}}\bigr)\right]^{2},
$$
whose dependence on the occupation is quadratic in a running prefix charge. On each fixed reduced block the primitive kernels, comparison maps, and exchange defects remain exact finite objects. On the minimal reduced two-bond strip prototype we record the first exact interaction-sensitive exchange-defect coefficient with Coulomb-string gap data. The benchmark theorem therefore reproduces the structure of Paper 15 with a strictly richer reduced interaction, now keyed to the Coulomb-string data familiar from one-dimensional lattice QED.

A dedicated conventional-physics section states explicitly what this benchmark does and does not claim relative to standard truncated Hamiltonian compact-$U(1)$ lattice gauge theory. The reduction is not a statement of "$U(1)$ broken by truncation" or an exotic nonlocality claim; it is an exact finite-sector rewriting of the truncated compact-$U(1)$ gauge law in charge-prefix variables. A finite-block validation section records direct numerical checks of exact Gauss commutation, exact full-to-reduced matching on every physical sector of a small chain, and the first interacting prototype coefficient at two independent flux seeds.

Scope note. The theorem-level content of this paper is the truncated compact-$U(1)$ matter-link setup, exact local $U(1)$ gauge symmetry, exact Gauss-sector decomposition, exact physical/global-flux elimination under the no-truncation condition, the Coulomb-string reduced Hamiltonian, the reduced finite-kernel primitive/comparison-map/exchange-defect package, the exact two-step support of the one-region reduced order-$\Delta^4$ coefficient, and the first exact interaction-sensitive exchange-defect coefficient on the minimal reduced two-bond strip prototype. Non-goals include a $K\to\infty$ continuum limit, a nonintegrability theorem, and any duality-based continuum claim. Those are deliberately deferred to later phases in the roadmap.

## Introduction

Paper 15 fixed the first benchmark in which Gauss-law elimination produces a genuinely interacting reduced matter Hamiltonian on a finite configuration space. That result was made possible by a conservative choice of gauge group: with $Z_2$ link variables, every primitive ISP object remained an exact finite matrix, and the reduced electric contribution became a parity string that is manifestly not a one-body operator. The question that opens Paper 16 is the next conservative step: can the same benchmark structure be carried across to a compact $U(1)$ gauge group without losing finiteness?

The answer is yes, provided that the link-electric basis is truncated at integer charge $|e|\le K$. In that truncated basis every primitive kernel, localized deformation, comparison map, and exchange defect remains an exact finite matrix, while the gauge-theoretic content is strictly richer than in the $Z_2$ case: electric fields are now integer-valued with a truncation window rather than $\pm 1$, the Wilson link operator is a genuine raising operator within the window, and the electric Hamiltonian is a quadratic functional of the integer flux profile rather than a transverse field. That is the minimal step from the $Z_2$ benchmark toward QED-adjacent content without leaving finite configuration-space scope.

The price of the truncation is one additional sector-level condition. On each fixed Gauss sector with a fixed left-boundary flux seed $w\in\{-K,\dots,K\}$, the link-electric data are reconstructed from matter data by the one-dimensional recursion, exactly as in Paper 15. The recursion closes inside the truncation window only if every reduced link value along the chain satisfies $|E_{n+1/2}(X)|\le K$. We call this the no-truncation condition and make it the precise gating condition of the elimination theorem. On the blocks where the condition holds, the reduced Hamiltonian is a finite matrix with an explicit Coulomb-string electric term. On the blocks where it fails, the reduced block is smaller than its nominal charge-neutral dimension, because certain matter configurations are removed from the sector by the truncation. This is the clean finite-$K$ statement of what "truncation effect" means at the benchmark level.

The phrase *genuinely interacting* therefore continues to refer to the reduced matter description after exact Gauss-sector/global-flux elimination. In the present paper the content of that phrase is strictly richer than in Paper 15. The $Z_2$ benchmark produced a non-bilinear reduced Hamiltonian with a multiplicative parity string. The truncated compact-$U(1)$ benchmark produces a non-bilinear reduced Hamiltonian with a quadratic Coulomb-string kernel whose coefficients depend on $w$, the background charges, and the running prefix of occupations. That is the first benchmark-scale instance of reduced electrostatic interaction in the ISP sequence.

**Main results (informal).**

1. *Exact truncated compact-$U(1)$ benchmark.* The first QED-adjacent interacting gauge-matter phase of the sequence is formulated on an ordinary finite matter-plus-link configuration space with $K$-truncated integer link variables.
2. *Exact local $U(1)$ gauge symmetry.* The combined Hamiltonian and the localized mixed-support deformations commute with the local integer-valued Gauss generators on every fixed truncation $K$.
3. *Exact Gauss-sector decomposition.* Both the full and localized dynamics decompose exactly into common eigenspaces of the local Gauss generators.
4. *Exact physical-sector elimination under the no-truncation condition.* On each compatible Gauss sector and left-boundary flux seed $w\in\{-K,\dots,K\}$, the link-electric data are reconstructed exactly from matter data whenever the one-dimensional recursion closes inside the truncation window.
5. *Coulomb-string reduced Hamiltonian.* On every such block the transported Hamiltonian contains ordinary nearest-neighbor hopping together with a quadratic Coulomb-string electric term in the reduced occupation variables.
6. *Exact reduced finite-kernel setup.* Primitive kernels, comparison maps, and exchange defects remain exact finite objects on every reduced block at every fixed $K$.
7. *Exact two-step reduced support of the one-region $\Delta^4$ coefficient.* The first nontrivial one-region reduced coefficient beyond order $\Delta^2$ already leaves all exterior data outside the two-step neighborhood unchanged.
8. *Exact first interaction-sensitive reduced-strip prototype coefficient.* On the minimal reduced two-bond strip prototype the first disjoint site-block exchange channel is explicit through the first order at which the Coulomb-string gap data appear.
9. *Conventional-physics clarification.* The interaction claim is a reduced-variables statement at fixed finite $K$; no $K\to\infty$, nonintegrability, or continuum local-net claim is made.
10. *Finite-block validation.* Exact Gauss commutation, exact full-to-reduced matching on every physical sector of a small chain, and the first interacting prototype coefficient are directly reproducible by exact finite-matrix evaluation.

## Truncated Compact $U(1)$ Matter-Link Benchmark

**Definition 1**

(Truncated compact-$U(1)$ matter-link configuration space).

Fix an open chain of $L$ sites labeled $\Lambda_L=\{0,1,\dots,L-1\}$ and $L-1$ links labeled by $n+\tfrac12$ for $n=0,\dots,L-2$. Fix an integer truncation level $K\ge 1$. Let
$$
\Omega_L^{\mathrm{matt}}:=\{X\subseteq \Lambda_L\}
$$
be the spinless fermion occupation space, with occupation numbers $N_n(X)\in\{0,1\}$, and let each link carry a $K$-truncated integer electric variable
$$
e_{n+1/2}\in\mathbb Z_K:=\{-K,-K+1,\dots,K-1,K\}.
$$
The full finite matter-link configuration space is
$$
\Omega_{L,K}^{U(1)}:=\Omega_L^{\mathrm{matt}}\times\mathbb Z_K^{\,L-1},
$$
whose elements are written $\omega=(X,\boldsymbol e)$ with $\boldsymbol e=(e_{1/2},e_{3/2},\dots,e_{L-3/2})$.

Remark.

At fixed $L$ and $K$ the matter space has $2^{L}$ states and the link space has $(2K+1)^{L-1}$ states, so every primitive object below is an exact finite matrix of finite dimension $2^{L}(2K+1)^{L-1}$.

**Definition 2**

(Truncated link and matter operators).

On each link introduce the electric number operator $\widehat e_{n+1/2}$ diagonal in the $\mathbb Z_K$ basis, together with the Wilson raising operator $\widehat U_{n+1/2}$ acting by
$$
\widehat U_{n+1/2}|e\rangle
=
\begin{cases} |e+1\rangle, & e

-K,\\[2pt] 0, & e=-K,\end{cases}
$$
so that $\widehat U$ is a partial isometry on the truncated link space satisfying $[\widehat e_{n+1/2},\widehat U_{n+1/2}]=\widehat U_{n+1/2}$ in the interior of the window. On the matter sector let $c_n,c_n^{\dagger},\widehat N_n=c_n^{\dagger}c_n$ be the usual fermionic operators, and fix integer background charges $q_n^{\mathrm{bg}}\in\mathbb Z$.

**Definition 3**

(Gauge generators and the combined benchmark Hamiltonian).

Define the local integer-valued $U(1)$ Gauss generators on interior sites $1\le n\le L-2$ by
$$
\widehat G_n
:=\widehat e_{n+1/2}-\widehat e_{n-1/2}-\bigl(\widehat N_n-q_n^{\mathrm{bg}}\bigr),
$$
and the gauge-invariant matter-link Hamiltonian by
$$
\widehat H_{L,K}^{U(1)}
:=
m\sum_{n=0}^{L-1}(-1)^n\widehat N_n
+\tfrac{g^{2}}{2}\sum_{n=0}^{L-2}\widehat e_{n+1/2}^{\,2}
-t\sum_{n=0}^{L-2}\bigl(c_{n+1}^{\dagger}\,\widehat U_{n+1/2}^{\dagger}\,c_n+c_n^{\dagger}\,\widehat U_{n+1/2}\,c_{n+1}\bigr).
$$

Remark.

The operator $\widehat U_{n+1/2}^{\dagger}$ in the rightward-hopping term is the correct direction for $U(1)$ gauge invariance: moving a unit positive charge from site $n$ to site $n+1$ must lower the link-$n+1/2$ electric field by one to keep $\widehat G_n$ and $\widehat G_{n+1}$ unchanged, and the truncation endpoints automatically kill any hop that would otherwise move outside the window.

**Proposition 1**

(Exact local gauge symmetry and Gauss-sector decomposition).

For every interior site $n\in\{1,\dots,L-2\}$,
$$
[\widehat G_n,\widehat H_{L,K}^{U(1)}]=0.
$$
Hence every polynomial in the Hamiltonian and every finite-time propagator decompose exactly into common eigenspaces of the commuting family $\{\widehat G_n\}_{n=1}^{L-2}$.

Proof sketch.

The mass term commutes with every $\widehat G_n$ because it depends only on occupations. The electric term is diagonal in the same $\widehat e$ variables that appear in the Gauss generators and therefore commutes. For a rightward hopping term $c_{n+1}^{\dagger}\widehat U_{n+1/2}^{\dagger}c_n$, the fermion operators change $\widehat N_n$ by $-1$ and $\widehat N_{n+1}$ by $+1$, while $\widehat U_{n+1/2}^{\dagger}$ lowers $\widehat e_{n+1/2}$ by $1$. The combined change of $\widehat G_n=\widehat e_{n+1/2}-\widehat e_{n-1/2}-(\widehat N_n-q_n^{\mathrm{bg}})$ is $-1-0-(-1)=0$, and the combined change of $\widehat G_{n+1}$ is $0-(-1)-(+1)=0$. All other Gauss generators receive no change. Truncation does not affect the commutation because $\widehat U^{\dagger}$ is defined to annihilate the boundary state and therefore commutes trivially with every Gauss generator on that boundary state. Hermitian conjugation gives the leftward term, which is handled identically.

$\square$

## Exact Physical-Sector Elimination on Fixed Global-Flux Blocks

**Definition 4**

(Compatible Gauss sector, left-boundary flux seed, and the no-truncation condition).

Fix a Gauss-sector label
$$
\mathbf g=(g_1,\dots,g_{L-2}),\qquad g_n\in\mathbb Z,
$$
and a left-boundary flux seed $w\in\mathbb Z_K$. For a matter configuration $X\in\Omega_L^{\mathrm{matt}}$ define the cumulative charge prefix
$$
\sigma_{n+1/2}(X;\mathbf g,w):=w+\sum_{j=0}^{n}\bigl(N_j(X)-q_j^{\mathrm{bg}}\bigr)+\sum_{j=1}^{n}g_j,\qquad n=0,1,\dots,L-2.
$$
Write $\Omega_{L,K,\mathbf g,w}^{\mathrm{red}}$ for the set of matter configurations satisfying the no-truncation condition
$$
|\sigma_{n+1/2}(X;\mathbf g,w)|\le K,\qquad n=0,1,\dots,L-2.
$$

**Theorem 1**

(Exact recursion and physical-sector elimination on fixed $(\mathbf g,w)$).

Fix a Gauss-sector label $\mathbf g$ and a left-boundary flux seed $w\in\mathbb Z_K$. Then:

1. *Exact recursion.* Every basis state in the corresponding sector satisfies
  $$
  e_{n+1/2}=e_{n-1/2}+\bigl(N_n(X)-q_n^{\mathrm{bg}}\bigr)+g_n,\qquad n=1,\dots,L-2,
  $$
  with the left-boundary condition $e_{1/2}=w+\bigl(N_0(X)-q_0^{\mathrm{bg}}\bigr)$. Consequently,
  $$
  e_{n+1/2}=\sigma_{n+1/2}(X;\mathbf g,w).
  $$
2. *Exact elimination.* The map
  $$
  \iota_{\mathbf g,w}:\Omega_{L,K,\mathbf g,w}^{\mathrm{red}}\to \Omega_{L,K}^{U(1)},\qquad X\mapsto\bigl(X,\boldsymbol\sigma(X;\mathbf g,w)\bigr)
  $$
  is a bijection onto the fixed $(\mathbf g,w)$ block of the full benchmark.
3. *Reduced Hamiltonian.* Transporting the fixed-block Hamiltonian through $\iota_{\mathbf g,w}$ yields a reduced matter Hamiltonian $\widehat H_{\mathbf g,w}^{\mathrm{red}}$ acting on the reduced matter space alone, with matter hops forbidden whenever the image link variable would exceed the truncation window.

Proof sketch.

Items (i) and (ii) are the deterministic recursion $e_{n+1/2}=e_{n-1/2}+(N_n-q_n^{\mathrm{bg}})+g_n$ unrolled from the left boundary. Item (iii) follows from the fact that every Hamiltonian term either commutes with $\widehat e$ (mass and electric terms) or moves $\widehat e$ by $\pm 1$ on a single link together with $\widehat N$ by $\mp 1$ on the two adjacent sites (hopping terms), so the image of the block under every term is again inside the same fixed $(\mathbf g,w)$ sector, with the sole restriction that hops terminating outside $\mathbb Z_K$ are forbidden by the partial-isometry truncation. The result is a well-defined finite matrix on the reduced matter space.

$\square$

**Corollary 1**

(Explicit Coulomb-string reduced Hamiltonian).

On the reduced matter space of a fixed compatible pair $(\mathbf g,w)$, the transported Hamiltonian takes the form
$$
\widehat H_{\mathbf g,w}^{\mathrm{red}}
=
m\sum_{n=0}^{L-1}(-1)^n\widehat N_n
+\frac{g^{2}}{2}\sum_{n=0}^{L-2}\!\left[w+\sum_{j=0}^{n}\bigl(\widehat N_j-q_j^{\mathrm{bg}}\bigr)+\sum_{j=1}^{n}g_j\right]^{2}
-t\sum_{n=0}^{L-2}\Pi_{n+1/2}^{(\mathbf g,w)}\bigl(c_{n+1}^{\dagger}c_n+c_n^{\dagger}c_{n+1}\bigr),
$$
where $\Pi_{n+1/2}^{(\mathbf g,w)}$ is the diagonal indicator that the image link value under the hop remains inside $\mathbb Z_K$.

**Proposition 2**

(Genuinely interacting Coulomb-string reduced dynamics).

Assume $L\ge 3$ and $g\ne 0$. Then the electric part of $\widehat H_{\mathbf g,w}^{\mathrm{red}}$ cannot be written as a constant plus a one-body occupation operator $a_0+\sum_n a_n\widehat N_n$. More strongly, it contains strict two-body and higher-body terms in the reduced occupation variables whose coefficients are fixed by $g,w,\mathbf g$, and the background charges.

Proof sketch.

Expanding the quadratic Coulomb-string sum yields terms of the form $g^{2}\sum_{j\le k}\widehat N_j\widehat N_k$ with $j\ne k$, whose coefficients are strictly nonzero because each interior link gets a contribution from every pair of occupations whose running prefix passes through that link. No reshuffle of constants or one-body occupation operators can absorb these pair terms, which completes the proof.

$\square$

Remark.

Proposition 2 is strictly stronger than its $Z_2$ analogue. The $Z_2$ benchmark produced a reduced electric term that was multiplicative in a prefix parity string. The truncated compact-$U(1)$ benchmark produces a reduced electric term that is quadratic in a prefix cumulative charge and therefore carries explicit two-body occupation structure by direct expansion.

## Reduced Primitive Kernels, Comparison Maps, and Exchange Defects

Once a fixed compatible pair $(\mathbf g,w)$ has been chosen, the reduced truncated compact-$U(1)$ benchmark is again an ordinary finite stochastic problem. The reduced configuration space, the reduced full and localized propagators, and all primitive ISP kernels remain exact finite matrices at every fixed truncation $K$. That is the continuation of the methodology of Papers 1-15 into the first QED-adjacent phase.

**Definition 5**

(Reduced primitive kernel package on a fixed $(\mathbf g,w)$ block).

Fix a reference slab and a gauge-compatible mixed region $R$. Let $\widehat H_{\mathbf g,w}^{\mathrm{red}}$ be the reduced Hamiltonian of Corollary 1 and let $\widehat H_{R,\mathbf g,w}^{\mathrm{red}}$ denote the corresponding reduced localized Hamiltonian obtained by transporting the mixed-support localized deformation of the full truncated $U(1)$ benchmark through the elimination map $\iota_{\mathbf g,w}$. Define the reduced primitive kernels, comparison maps, and exchange defects exactly as in Papers 4-15, but now on the finite reduced configuration space $\Omega_{L,K,\mathbf g,w}^{\mathrm{red}}$.

**Theorem 2**

(Exact finite-kernel interacting benchmark package on fixed reduced blocks).

For every fixed compatible pair $(\mathbf g,w)$ at fixed $L,K$:

1. the reduced configuration space is finite;
2. the reduced full and localized propagators are finite matrices;
3. the corresponding primitive kernels, comparison maps, and exchange defects are exact finite objects on the reduced interacting benchmark.

**Definition 5A**

(Reduced bond-transfer kernels on a fixed $(\mathbf g,w)$ block).

For a bond $b=n+\tfrac12$ and reduced configurations $X,X'\in\Omega_{L,K,\mathbf g,w}^{\mathrm{red}}$, define the reduced bond-transfer kernel by
$$
\bigl[\mathsf T_b^{(\mathbf g,w)}\bigr]_{X',X}
:=
\begin{cases}
1, & X' \text{ is obtained from }X\text{ by moving one fermion across }b,\ \text{and}\ \Pi_b^{(\mathbf g,w)}(X)=1,\\
0, & \text{otherwise}.
\end{cases}
$$
Let $\mathsf D_b^{(\mathbf g,w)}$ be the corresponding diagonal degree kernel and set $\mathsf Q_b^{(\mathbf g,w)}:=\mathsf D_b^{(\mathbf g,w)}-\mathsf T_b^{(\mathbf g,w)}$.

**Proposition 3**

(Exact first one-region coefficient on reduced site blocks).

On every fixed compatible pair $(\mathbf g,w)$,
$$
J_{R_n^{\mathrm{red}},\mathbf g,w}(\Delta)=I+\Delta^2 A_{n,\mathbf g,w}^{[2],\mathrm{red}}+O(\Delta^4),
$$
with
$$
A_{n,\mathbf g,w}^{[2],\mathrm{red}}=t^2\Bigl(\mathsf Q_{n-1/2}^{(\mathbf g,w)}+\mathsf Q_{n+1/2}^{(\mathbf g,w)}\Bigr).
$$

**Proposition 3A**

(Exact two-step reduced support of the one-region $\Delta^4$ coefficient).

For every fixed compatible pair $(\mathbf g,w)$ and reduced site block $R_n^{\mathrm{red}}$, there exists an exact coefficient $A_{n,\mathbf g,w}^{[4],\mathrm{red}}$ such that
$$
J_{R_n^{\mathrm{red}},\mathbf g,w}(\Delta)=I+\Delta^2 A_{n,\mathbf g,w}^{[2],\mathrm{red}}+\Delta^4 A_{n,\mathbf g,w}^{[4],\mathrm{red}}+O(\Delta^6),
$$
and if $\bigl[A_{n,\mathbf g,w}^{[4],\mathrm{red}}\bigr]_{X',X}\ne 0$, then $X$ and $X'$ agree outside the two-step neighborhood $\{n-2,n-1,n,n+1,n+2\}$.

## First Exact Interacting Coefficient on the Minimal Reduced Strip Prototype

**Definition 6**

(Minimal reduced two-bond strip prototype and Coulomb-string gaps).

Fix $L\ge 4$ and background charges $q^{\mathrm{bg}}=(1,0,0,\dots,0)$, so that the reduced one-particle sector at seed $w$ supports the three local configurations
$$
X:=(0,0,0,1,0,\dots,0),\quad Y:=(0,0,1,0,0,\dots,0),\quad Z:=(0,1,0,0,0,\dots,0),
$$
located at sites $n+2$, $n+1$, and $n$ respectively for some choice of $n$. Compute the reduced diagonal energy of a one-particle configuration from Corollary 1 as
$$
\mathcal E_{\mathbf g,w}(X)
=
m\sum_{r=0}^{L-1}(-1)^r N_r(X)+\frac{g^2}{2}\sum_{r=0}^{L-2}\sigma_{r+1/2}(X;\mathbf g,w)^{2},
$$
and define the associated reduced diagonal energy gaps
$$
\delta_{n+3/2}(X):=\mathcal E_{\mathbf g,w}(X)-\mathcal E_{\mathbf g,w}(Y),
\qquad
\delta_{n+1/2}(Y):=\mathcal E_{\mathbf g,w}(Z)-\mathcal E_{\mathbf g,w}(Y).
$$

**Theorem 3**

(First exact interaction-sensitive coefficient on the minimal reduced two-bond strip prototype).

Fix a compatible pair $(\mathbf g,w)$ such that the prototype configurations $X,Y,Z$ all lie in $\Omega_{L,K,\mathbf g,w}^{\mathrm{red}}$ and both prototype hops remain inside the truncation window. Let $J_{n,\mathbf g,w}^{\mathrm{proto}}(\Delta)$ and $J_{n+2,\mathbf g,w}^{\mathrm{proto}}(\Delta)$ denote the site-block comparison maps compressed to the prototype basis $\{X,Y,Z\}$, and define the corresponding exchange defect
$$
E_{n,n+2;\mathbf g,w}^{\mathrm{proto}}(\Delta)
:=
J_{n,\mathbf g,w}^{\mathrm{proto}}(\Delta)J_{n+2,\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigl[J_{n,\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigr]^{-1}\bigl[J_{n+2,\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigr]^{-1}.
$$
Then
$$
\bigl[E_{n,n+2;\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigr]_{Z,X}
=
t^4\Delta^4
+
t^4\left[\frac{13}{6}t^2-\frac{1}{12}\Bigl(\delta_{n+3/2}(X)^2+\delta_{n+1/2}(Y)^2\Bigr)\right]\Delta^6
+O(\Delta^8),
$$
with the gaps now populated by the quadratic Coulomb-string functional of Definition 6.

Remark.

The coefficient formula coincides with its $Z_2$ analogue of Paper 15 Theorem 3 as a universal three-state prototype identity. What changes in the truncated compact-$U(1)$ benchmark is the data feeding it: the gaps $\delta_{n+3/2}(X)$ and $\delta_{n+1/2}(Y)$ are now finite differences of the Coulomb-string functional and therefore depend quadratically on $w$, on the background charges, and on the running prefix of occupations. The physical content of the benchmark is therefore carried by the gap data, not by a deformation of the coefficient formula.

## Conventional Physics Interpretation

It is useful to state explicitly how this benchmark sits relative to standard truncated Hamiltonian compact-$U(1)$ lattice gauge theory. The unreduced model of Definition 3 is the textbook Kogut-Susskind Hamiltonian on a finite open chain with fermionic matter, with the one-body addition that the link electric basis is truncated at $|e|\le K$. That is a well-studied finite-volume construction that converges rapidly in $K$ for weak coupling and low-lying states, and that is used in essentially every modern numerical study of Schwinger-model-like systems. It is the correct microscopic setting for a benchmark that wants to be both QED-adjacent and honestly finite.

The reduction of Theorem 1 is the one-dimensional finite-volume analogue of solving the Kogut-Susskind Gauss law by integrating out the link variables against the charge-prefix string. The resulting Coulomb-string reduced Hamiltonian is exactly the Hamiltonian one obtains after solving $\partial_x E=\rho$ on an open chain with a left-boundary flux seed $w$, exactly as in the one-dimensional Schwinger-model literature. The appearance of explicit two-body terms after this elimination is a familiar feature of one-dimensional gauge theory: electric charges in one spatial dimension interact linearly in distance, and the string term exposes that interaction explicitly.

The phrase *genuinely interacting* here is therefore meant in exactly the sense used in the Schwinger-model and Hamiltonian lattice QED literature: after the link variables have been eliminated on a fixed sector, the resulting matter Hamiltonian contains a genuine Coulomb-string two-body term and all higher-body terms that follow from expanding the square of the prefix charge. As in Paper 15, this does not yet claim anything about nonintegrability, chaos, absence of a simpler dual formulation, or a continuum local-net theorem; in the truncated Hamiltonian case those claims are precisely the ones that require a controlled $K\to\infty$ limit and a continuum analysis that sits beyond the scope of the present benchmark.

**Physics boundary.**

The invariant claim of the present paper is modest but real: exact Gauss-law elimination on the minimal truncated compact-$U(1)$ benchmark produces a reduced matter Hamiltonian whose electric contribution is a quadratic Coulomb-string functional of the reduced occupation variables, and the first reduced exchange-defect correction already depends on the resulting Coulomb-string gap data. Whether a larger $K$, a continuum limit, or an alternative gauge-invariant variable choice would simplify the same physics is intentionally left open here.

## Finite-Block Validation

The benchmark formulas can be checked directly because all matrices involved are finite and small at reasonable $L$ and $K$. A companion validation script, *validate_truncated_u1_benchmark.py*, evaluates the full truncated matter-link Hamiltonian, its Gauss generators, its restricted physical-sector blocks, and the prototype comparison maps and exchange defects by direct matrix computation in pure stdlib Python.

Three validations are especially useful. First, on an $L=3$, $K=2$ open chain with $q^{\mathrm{bg}}=(1,0,1)$, direct evaluation of the full Hamiltonian against every interior Gauss generator reproduces exact local $U(1)$ gauge symmetry at machine precision. Second, on the same chain the full Hamiltonian restricted to each physical sector $(\mathbf g=\mathbf 0,w)$ with $w\in\{-2,-1,0,1,2\}$ agrees exactly with the reduced Coulomb-string Hamiltonian built directly from the explicit prefix formula of Corollary 1 on the corresponding reduced matter block; across all five physical sectors the maximum deviation is machine-precision zero. Third, on the minimal reduced three-state prototype extracted from an $L=4$ one-particle sector at background $q^{\mathrm{bg}}=(1,0,0,0)$, direct evaluation of the order-$\Delta^4$ and order-$\Delta^6$ coefficients of the end-to-end exchange-defect entry recovers the values $t^4$ and $t^4\bigl[(13/6)t^2-(\delta_{n+3/2}(X)^2+\delta_{n+1/2}(Y)^2)/12\bigr]$ with the Coulomb-string gaps computed from Definition 6 at two independent flux seeds $w=0$ and $w=1$.

For the current validation script, the Gauss commutation residual on the $L=3$, $K=2$ chain is $0$ at machine precision. The full-to-reduced elimination residual across all five physical sectors at the same $L,K$ is $0$ at machine precision. On the prototype at $w=0$, the extracted order-$\Delta^4$ coefficient matches $t^4=1$ at relative error $4.0\times 10^{-14}$ and the extracted order-$\Delta^6$ coefficient matches the Coulomb-string gap prediction at relative error $4.2\times 10^{-10}$ with gaps $\delta_{n+3/2}(X)=-0.455$ and $\delta_{n+1/2}(Y)=-0.945$ at $(m,g^2,t)=(0.35,0.49,1.0)$. On the same prototype at $w=1$, the extracted coefficients match at relative errors $3.3\times 10^{-14}$ and $3.4\times 10^{-10}$ with gaps $\delta_{n+3/2}(X)=-0.945$ and $\delta_{n+1/2}(Y)=-0.455$, exhibiting the predicted dependence of the reduced gap data on the left-boundary flux seed. At benchmark stage, that is the right kind of independent check: exact local $U(1)$ gauge symmetry, exact finite-$K$ elimination, and the first interacting prototype coefficient are not only derivable on paper but directly recoverable from the underlying finite matrices.

## Conclusion

The relativistic ISP stack now reaches the first QED-adjacent benchmark that still fits exactly inside finite configuration-space scope. The truncated compact-$U(1)$ matter-link benchmark preserves the exact finite-kernel methodology of the $Z_2$ benchmark while strengthening its reduced-Hamiltonian content: the electric contribution after exact Gauss-law elimination is a genuine quadratic Coulomb-string functional of the reduced occupation variables, keyed to the same left-boundary flux seed that appears in the Kogut-Susskind treatment of one-dimensional Hamiltonian lattice QED.

The benchmark is deliberately conservative in its claims. The interacting reduced Hamiltonian is a theorem at fixed finite $K$; the $K\to\infty$ limit, the continuum limit, and any nonintegrability or duality-resistance claim are explicitly deferred. The companion validation script records the exact finite-block checks that make the benchmark formulas independently checkable by direct matrix evaluation. The next step in the roadmap is no longer to enlarge the prose around a $Z_2$ benchmark, but to decide which of the remaining structural continuations — a $K$-stability theorem, a first two-particle Coulomb-string coefficient, or a first boundary-flux-resolved exchange coefficient in the $U(1)$ setting — deserves the next theorem paper.

## References

1. [1] Anonymous, "Minimal Genuinely Interacting Gauge-Matter Benchmark in Relativistic ISP," preprint (2026).
2. [2] Anonymous, "Reduced-Strip and Overlap Coefficients for the Minimal Interacting $Z_2$ Gauge-Matter Benchmark in Relativistic ISP," companion preprint (2026).
3. [3] Anonymous, "Dynamical Abelian Gauge Field and Gauss-Law Sectors in Relativistic ISP," preprint (2026).
4. [4] Anonymous, "Boundary-Flux-Resolved Einstein Causality in Relativistic ISP," preprint (2026).
5. [5] J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**, 8 (2025).
6. [6] J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes," preprint (2025).
7. [7] J. B. Kogut and L. Susskind, "Hamiltonian Formulation of Wilson's Lattice Gauge Theories," *Phys. Rev. D* **11**, 395 (1975).
8. [8] S. Chandrasekharan and U.-J. Wiese, "Quantum Link Models: A Discrete Approach to Gauge Theories," *Nucl. Phys. B* **492**, 455 (1997).
9. [9] T. Byrnes, P. Sriganesh, R. J. Bursill, and C. J. Hamer, "Density Matrix Renormalisation Group Approach to the Massive Schwinger Model," *Phys. Rev. D* **66**, 013002 (2002).
10. [10] M. C. Bañuls, K. Cichy, K. Jansen, and J. I. Cirac, "The Mass Spectrum of the Schwinger Model with Matrix Product States," *J. High Energy Phys.* **11**, 158 (2013).
