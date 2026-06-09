# Variable Particle Number in Relativistic ISP

*Exact finite-lattice Fock-space lift for number-preserving quadratic dynamics, plus first local sector-changing examples*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 9 in the relativistic ISP sequence; phase-8 implementation after the one-particle phase-1 through phase-7 stack

## Abstract

Phases 1 through 7 fixed the exact one-particle relativistic ISP stack through the first non-leading regulator comparison. The next honest extension is variable particle number. From the Barandes point of view, that extension should not begin by importing a new continuum ontology or by treating Fock space as more primitive than the underlying transition law. It should begin by enlarging the configuration space and asking what the exact kernel algebra already forces.

This paper does that at the strongest scope currently justified. For number-preserving quadratic dynamics on the fixed finite lattice, the primitive kernels, localized comparison maps, and exchange defects decompose exactly sector by sector, so the bond-centered thin-slab law lifts exactly to the full finite-lattice Fock space by second quantization: the tangential generator is $d\Gamma(K_\parallel[\beta])$, and no new continuum kinematics appear. We then add the first explicit local sector-changing examples—a local source/sink term and a local pair-creation term—and prove the exact leading sector-selection rules for their primitive kernels and comparison maps. On the full finite lattice their first comparison coefficients are explicit local occupancy-toggle kernels, and for disjoint local source/pair couplings those leading coefficients commute exactly, so the corresponding exchange defect has no $\Delta^4$ term. We then compute the first nonzero disjoint local defect coefficient at order $\Delta^6$: it is exact, mass-blind, supported on universal two-, three-, and four-mode blocks, and vanishes unless the two local couplings lie one free-Dirac hop apart. Finally, we classify the genuine exchanged strip channels in those disjoint local $\Delta^6$ classes: one bonded source/source channel, six source/pair channels, and six adjacent pair/pair channels. What still remains open is the broader finite-support sector-changing exchange algebra and its general strip package.

Scope note. The theorem-level exact content of this paper is the full fixed finite-lattice Fock lift for number-preserving quadratic dynamics together with the exact leading and first nonzero disjoint-local sector-changing coefficient package. On the number-preserving side, the common infinite-volume bond-centered one-particle operator and its second-quantized large-volume stabilization can now also be stated exactly. What is still not proved is the genuine infinite-volume / infinite-Fock theorem for the primitive kernels, comparison maps, and exchange defects. The sector-changing terms are not yet carried to a general finite-support strip-level or all-orders exchange-defect theorem.

## Introduction

The phase ordering of the relativistic ISP program matters. Before broadening into variable particle number, the one-particle exchange-defect algebra had to be pushed far enough that the correct local continuum object was no longer in doubt. That is what the earlier phase papers now supply: exact localized comparison kernels, exact support-level leading boundary control, exact higher-order overlap structure, the strip-moment criterion, the first explicit non-leading singleton coefficient, and the first explicit non-leading regulator comparison.

Only after that stack is in place is the Fock-space question well posed. From a Barandes-style perspective, the right first move is conservative. One should not begin by treating creation and annihilation operators as primitive physical data. One should begin from ordinary stochastic conditioning on an enlarged configuration space. In the present setting that means finite fermionic configuration sectors, their exact primitive kernels, and the comparison maps they inherit from localized finite deformations.

This paper therefore separates two burdens. The first is exact and theorem level: number-preserving quadratic dynamics on finite fermionic Fock sectors, and hence on the entire fixed finite lattice once all sectors are summed. There the sectorwise structure is exact, and the one-particle bond-centered thin-slab law lifts without modification of its continuum kinematics. The second burden concerns genuinely sector-changing local dynamics. For that second burden the correct deliverable is now two-layered: first a mathematically clean identification of the local terms and the exact sector blocks in which they first appear, and then the exact first nonzero disjoint-local exchange coefficient where the current stack actually lets it be computed.

**Main results (informal).**

1. *Exact sectorwise kernel decomposition.* For number-preserving quadratic dynamics, primitive kernels, comparison maps, and exchange defects on the fixed finite lattice are exact direct sums of fixed-particle-number objects.
2. *Exact bond-centered lift.* The already-proved one-particle bond-centered thin-slab law lifts sectorwise by second quantization: the full finite-lattice tangential generator is $d\Gamma(K_\parallel[\beta])$.
3. *Exact first local sector-changing coefficients.* A local source/sink term first populates adjacent sector blocks $N\leftrightarrow N\pm1$, while a local pair term first populates $N\leftrightarrow N\pm2$; in both cases the first sector-changing probabilities arise at order $\Delta^2$, and on the full finite lattice the corresponding first comparison coefficients are explicit local occupancy-toggle kernels.
4. *Exact disjoint-local exchange law through first nonzero order.* For disjoint local source/pair couplings on the full finite lattice, the naive $\Delta^4$ term vanishes exactly, and the first nonzero coefficient at order $\Delta^6$ is an exact universal local kernel supported on two-, three-, or four-mode blocks according to the local coupling type.
5. *Exact disjoint-local strip-channel classification.* Those universal $\Delta^6$ kernels close on a finite exact channel basis: one bonded source/source strip, six source/pair strips, and six adjacent pair/pair strips, all supported on the minimal one-hop active strip.

Strategic note. The point is not to overstate phase 8 as a finished variable-particle-number field theory. The point is to close the number-preserving theorem cleanly and to isolate the first genuine sector-changing algebraic data without pretending that their full thin-slab reduction has already been proved.

## Fixed finite-lattice fermionic Fock-space setup

**Definition 1**

(Finite-particle configuration sectors).

Let $\mathcal C_L:=\Lambda_L\times\{\uparrow,\downarrow\}$ denote the one-particle configuration set of the free lattice-Dirac model, and let $\mathcal H_L=\mathbb C^{2L}$ be the corresponding one-particle Hilbert space. For $0\le N\le 2L$, let
$$
\mathcal F_L^{(N)}:=\Lambda^N\mathcal H_L
$$
be the fermionic $N$-particle sector, with antisymmetrized occupation basis indexed by $N$-element subsets of $\mathcal C_L$. For a finite truncation level $N_{\max}\le 2L$, define
$$
\mathcal F_{L,\le N_{\max}}
:=
\bigoplus_{N=0}^{N_{\max}}\mathcal F_L^{(N)}.
$$

Remark.

At this stage the primitive objects are still ordinary transition laws on ordinary configuration spaces. Fock space is a convenient Hilbert-space representation of the finite disjoint union of the configuration sectors, not a replacement for the $\Gamma$-level point of view.

**Definition 2**

(Sectorwise primitive kernels and comparison maps).

Let $h_0$ be the one-particle reference Hamiltonian and $h_R$ a one-particle localized deformation Hamiltonian of the type already studied in the earlier phase papers. For number-preserving quadratic dynamics define
$$
\widehat H_0:=d\Gamma(h_0),
\qquad
\widehat H_R:=d\Gamma(h_R)
$$
on $\mathcal F_{L,\le N_{\max}}$.
Let
$$
\widehat U_0(\Delta):=e^{-i\Delta \widehat H_0},
\qquad
\widehat U_R(\Delta):=e^{-i\Delta \widehat H_R}.
$$
On sector $N$, write
$$
\widehat U_0^{(N)}(\Delta):=\widehat U_0(\Delta)\big|_{\mathcal F_L^{(N)}},
\qquad
\widehat U_R^{(N)}(\Delta):=\widehat U_R(\Delta)\big|_{\mathcal F_L^{(N)}}.
$$
The sectorwise primitive kernels are
$$
\Gamma_0^{(N)}(\Delta):=\Gamma\bigl(\widehat U_0^{(N)}(\Delta)\bigr),
\qquad
\Gamma_R^{(N)}(\Delta):=\Gamma\bigl(\widehat U_R^{(N)}(\Delta)\bigr),
$$
with sectorwise comparison maps
$$
J_R^{(N)}(\Delta):=\Gamma_R^{(N)}(\Delta)\bigl[\Gamma_0^{(N)}(\Delta)\bigr]^{-1}
$$
whenever the inverse exists. For two localized supports $R,S$, define the sectorwise exchange defect
$$
E_{R,S}^{(N)}(\Delta)
:=
J_R^{(N)}(\Delta)J_S^{(N)}(\Delta)\bigl[J_R^{(N)}(\Delta)\bigr]^{-1}\bigl[J_S^{(N)}(\Delta)\bigr]^{-1}.
$$

**Proposition 1**

(Exact sectorwise decomposition of primitive kernels, comparison maps, and exchange defects).

For number-preserving quadratic dynamics on $\mathcal F_{L,\le N_{\max}}$ one has the exact direct-sum decompositions
$$
\widehat U_0(\Delta)
=
\bigoplus_{N=0}^{N_{\max}}\widehat U_0^{(N)}(\Delta),
\qquad
\widehat U_R(\Delta)
=
\bigoplus_{N=0}^{N_{\max}}\widehat U_R^{(N)}(\Delta),
$$
and therefore
$$
\Gamma_0^{\le N_{\max}}(\Delta)
=
\bigoplus_{N=0}^{N_{\max}}\Gamma_0^{(N)}(\Delta),
\qquad
\Gamma_R^{\le N_{\max}}(\Delta)
=
\bigoplus_{N=0}^{N_{\max}}\Gamma_R^{(N)}(\Delta).
$$
Whenever each sectorwise inverse exists,
$$
J_R^{\le N_{\max}}(\Delta)
=
\bigoplus_{N=0}^{N_{\max}}J_R^{(N)}(\Delta),
\qquad
E_{R,S}^{\le N_{\max}}(\Delta)
=
\bigoplus_{N=0}^{N_{\max}}E_{R,S}^{(N)}(\Delta).
$$

Proof.

Because $d\Gamma(h_0)$ and $d\Gamma(h_R)$ preserve particle number exactly, each commutes with every sector projector $\Pi_N$ on $\mathcal F_{L,\le N_{\max}}$. Hence their exponentials are block diagonal in the particle-number decomposition:
$$
\widehat U_0(\Delta)=\bigoplus_N \widehat U_0^{(N)}(\Delta),
\qquad
\widehat U_R(\Delta)=\bigoplus_N \widehat U_R^{(N)}(\Delta).
$$
Taking entrywise squared moduli in the corresponding occupation bases preserves block diagonality and gives the kernel decompositions. A block-diagonal matrix has a block-diagonal inverse whenever each block is invertible, so the same direct-sum form holds for the comparison maps. The exchange defect is built algebraically from those comparison maps, hence it is again block diagonal with the displayed sector blocks.

$ \square $

**Corollary 1**

(Variable particle number without a new primitive probabilistic object).

At finite truncation and for number-preserving quadratic dynamics, the variable-particle-number relativistic ISP problem is an exact direct sum of ordinary finite configuration-space kernel problems. No new primitive probabilistic object is needed beyond the sectorwise transition laws.

Remark.

This is the clean Barandes-style moral. One does not get variable particle number by abandoning ordinary stochastic transition data. One gets it by enlarging the configuration space and then reading off the exact direct-sum structure that the transition law already has.

## Exact bond-centered lift of the one-particle law

The previous phase papers already determined the one-particle bond-centered thin-slab law. The only legitimate phase-8 question is therefore how that exact one-particle result lifts to finite particle number.

**Definition 3**

(Antisymmetrized sampling maps and sectorwise second quantization).

Let
$$
\iota_a:C_c^\infty(\mathbb R,\mathbb C^2)\to \mathcal H_L
$$
denote the one-particle sampling map used in the earlier phase papers. For $N\ge 1$, define the antisymmetrized $N$-particle sampling map on decomposable wedges by
$$
\iota_a^{(N)}(\phi_1\wedge\cdots\wedge\phi_N)
:=
\iota_a\phi_1\wedge\cdots\wedge\iota_a\phi_N,
$$
and extend linearly to smooth compactly supported antisymmetric $N$-particle profiles. On the finite truncation, set
$$
\iota_a^{\le N_{\max}}
:=
\bigoplus_{N=0}^{N_{\max}}\iota_a^{(N)}.
$$
For a one-particle operator $X$, let
$$
d\Gamma_N(X)
:=
\sum_{j=1}^N I^{\wedge(j-1)}\wedge X\wedge I^{\wedge(N-j)}
$$
denote its second quantization on $\mathcal F_L^{(N)}$, and set
$$
d\Gamma_{\le N_{\max}}(X)
:=
\bigoplus_{N=0}^{N_{\max}}d\Gamma_N(X).
$$

**Theorem 1**

(Exact sectorwise bond-centered lift of the one-particle thin-slab law).

Let $\mathcal T_a[\beta]$ and $K_\parallel[\beta]$ denote the already-proved one-particle bond-centered density and tangential operator, so that
$$
\mathcal T_a[\beta]\iota_a\phi
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a)
$$
for every smooth compactly supported one-particle profile $\phi$. Then for every fixed $N\le N_{\max}$ and every smooth compactly supported antisymmetric $N$-particle profile $\Psi$,
$$
d\Gamma_N(\mathcal T_a[\beta])\,\iota_a^{(N)}\Psi
=
\iota_a^{(N)}\bigl(d\Gamma_N(K_\parallel[\beta])\Psi\bigr)+O(a).
$$
Equivalently, on the finite truncation,
$$
d\Gamma_{\le N_{\max}}(\mathcal T_a[\beta])\,\iota_a^{\le N_{\max}}\Psi
=
\iota_a^{\le N_{\max}}\bigl(K_{\parallel,\mathcal F}^{\le N_{\max}}[\beta]\Psi\bigr)+O(a),
$$
where
$$
K_{\parallel,\mathcal F}^{\le N_{\max}}[\beta]
:=
d\Gamma_{\le N_{\max}}(K_\parallel[\beta]).
$$

Proof.

It is enough to prove the statement on decomposable wedges
$$
\Psi=\phi_1\wedge\cdots\wedge\phi_N.
$$
On such a vector,
$$
d\Gamma_N(\mathcal T_a[\beta])
=
\sum_{j=1}^N I^{\wedge(j-1)}\wedge \mathcal T_a[\beta]\wedge I^{\wedge(N-j)}.
$$
Applying the already-proved one-particle estimate in the $j$th slot gives
$$
\mathcal T_a[\beta]\iota_a\phi_j
=
\iota_a(K_\parallel[\beta]\phi_j)+O(a).
$$
Summing over the finitely many slots yields
$$
d\Gamma_N(\mathcal T_a[\beta])\,\iota_a^{(N)}\Psi
=
\iota_a^{(N)}\bigl(d\Gamma_N(K_\parallel[\beta])\Psi\bigr)+O(a),
$$
because $N$ is fixed and finite. Direct-summing over $N\le N_{\max}$ gives the finite-truncation statement.

$ \square $

**Corollary 2**

(No new continuum kinematics in the number-preserving Fock lift).

For finite truncations of number-preserving quadratic dynamics, the variable-particle-number tangential generator is
$$
K_{\parallel,\mathcal F}^{\le N_{\max}}[\beta]
=
\bigoplus_{N=0}^{N_{\max}}d\Gamma_N(K_\parallel[\beta]).
$$
Thus phase 8 introduces no new continuum kinematical operator beyond second quantization of the already-proved one-particle one.

**Corollary 3**

(Exact completion on the full finite-lattice Fock space).

Because the one-particle lattice Hilbert space has dimension $2L$, one may take $N_{\max}=2L$ in Theorem 1. Hence the number-preserving quadratic relativistic ISP lift is exact on the full finite-lattice Fock space
$$
\mathcal F_L
:=
\bigoplus_{N=0}^{2L}\mathcal F_L^{(N)},
$$
with tangential generator
$$
K_{\parallel,\mathcal F_L}[\beta]
:=
\bigoplus_{N=0}^{2L}d\Gamma_N(K_\parallel[\beta]).
$$
Thus, at fixed lattice size $L$, there is no further truncation issue: taking $N_{\max}=2L$ already includes every fermionic sector.

Remark.

This is exactly the conservative outcome one should want. The one-particle exchange algebra has already earned the operator $K_\parallel[\beta]$. Variable particle number does not get to invent a different one before the exact transition law compels it.

**Remark on fixed-$N$ large-volume stabilization.**

The proof of Theorem 1 is local in the one-particle slots. For any fixed particle number $N$ and any smooth compactly supported antisymmetric $N$-particle profile, once the periodic ring is chosen large enough that the support window and its bond-centered two-step collar do not meet the periodic seam, the same slotwise computation goes through unchanged. So the present argument is compatible with an infinite-volume statement on each fixed finite-particle sector separately.

**Remark on why this still falls short of the genuine infinite-Fock limit.**

That fixed-$N$ stabilization is not the theorem deferred here. The proof of Theorem 1 explicitly uses that $N$ is fixed when the slotwise $O(a)$ errors are summed, so it gives no estimate uniform in particle number. To pass from the sectorwise statements to a genuine $L\to\infty$ / infinite one-particle-space Fock theorem one would need, in addition, a controlled infinite-volume construction of the sectorwise primitive kernels, comparison maps, and exchange defects together with bounds compatible across all $N$, plus a domain/closability analysis for the full second-quantized operator
$$
\bigoplus_{N\ge 0} d\Gamma_N(K_\parallel[\beta])
$$
on the infinite Fock space. None of that is supplied by the present stack, so no genuine infinite-volume / infinite-Fock direct-sum theorem is claimed here.

**Proposition 1A**

(Canonical infinite-lattice realization of the bond-centered one-particle operator).

Let
$$
\mathcal H_\infty:=\ell^2(\mathbb Z,\mathbb C^2),
\qquad
(\iota_{a,\infty}\phi)_n:=\phi(an),
$$
and for each lattice size $L$ identify the periodic ring with the centered interval
$$
I_L:=\{-\lfloor L/2\rfloor,\ldots,\lceil L/2\rceil-1\}\subset\mathbb Z
$$
to obtain an isometric embedding
$$
\jmath_L:\mathcal H_L\hookrightarrow\mathcal H_\infty.
$$
Let $\iota_{a,L}$ denote the finite-ring sampling map already used above, and let $\mathcal T_{a,L}[\beta]$ denote the corresponding finite-ring bond-centered operator.
For $\beta\in C_c^\infty(\mathbb R)$ define the infinite-lattice bond-centered operator by the same local stencil as in the one-particle paper:
$$
\bigl(\mathcal T_{a,\infty}[\beta]\psi\bigr)_n
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
\end{pmatrix},
$$
for $\psi=(u,d)\in\mathcal H_\infty$. Then:

1. for every compactly supported $\beta$, the operator $\mathcal T_{a,\infty}[\beta]$ is bounded and in fact has finite input/output support;
2. there exists $L_0(\beta,a)$ such that for all $L\ge L_0(\beta,a)$,
  $$
  \jmath_L\,\mathcal T_{a,L}[\beta]\,\jmath_L^*
  =
  \mathcal T_{a,\infty}[\beta]
  $$
  as operators on $\mathcal H_\infty$;
3. for every $\phi\in C_c^\infty(\mathbb R,\mathbb C^2)$ there exists $L_1(\beta,a,\phi)$ such that for all $L\ge L_1(\beta,a,\phi)$,
  $$
  \jmath_L\,\mathcal T_{a,L}[\beta]\,\iota_{a,L}\phi
  =
  \mathcal T_{a,\infty}[\beta]\iota_{a,\infty}\phi,
  $$
  and moreover
  $$
  \mathcal T_{a,\infty}[\beta]\iota_{a,\infty}\phi
  =
  \iota_{a,\infty}\bigl(K_\parallel[\beta]\phi\bigr)+O(a^2).
  $$

Proof.

Because $\beta$ is compactly supported, only finitely many midpoint samples $\beta_{n+1/2}$ are nonzero. The displayed formula therefore involves only finitely many lattice sites and only the shifts $\pm1,\pm2$, so $\mathcal T_{a,\infty}[\beta]$ is a finite sum of bounded coordinate-shift maps with bounded coefficients; in particular it is bounded and has finite input/output support.

Let $W_{\beta,a}\subset\mathbb Z$ be a finite window containing every site that appears either as an output index $n$ with some nonzero coefficient in the displayed formula or as one of the corresponding input indices $n\pm1,n\pm2$. If $I_L\supset W_{\beta,a}$, then the finite-ring operator $\mathcal T_{a,L}[\beta]$ uses exactly the same local stencil on that window and no periodic wrap-around can occur. Hence after transport by $\jmath_L$ the finite-ring operator agrees entrywise with the infinite-lattice one, proving the exact operator identity for all sufficiently large $L$.

Now fix $\phi\in C_c^\infty(\mathbb R,\mathbb C^2)$, and let $W_{\phi,a}\subset\mathbb Z$ be the finite set of lattice sites on which the sampled infinite-lattice profile $\iota_{a,\infty}\phi$ is supported. If $I_L$ contains both $W_{\beta,a}$ and $W_{\phi,a}$, then $\jmath_L\,\iota_{a,L}\phi=\iota_{a,\infty}\phi$, so the exact operator identity above gives
$$
\jmath_L\,\mathcal T_{a,L}[\beta]\,\iota_{a,L}\phi
=
\mathcal T_{a,\infty}[\beta]\iota_{a,\infty}\phi.
$$
The final displayed equality is the same midpoint-Taylor expansion already used in the one-particle bond-centered paper, now applied to the identical local stencil on the infinite lattice.

$ \square $

**Corollary 3A**

(The bond-centered large-volume Fock operator is already under exact control).

Let
$$
\jmath_L^{(N)}:=\Lambda^N\jmath_L,
\qquad
P_L:=\jmath_L\jmath_L^*,
\qquad
P_L^{(N)}:=\Lambda^N P_L=\jmath_L^{(N)}\jmath_L^{(N)\,*},
$$
and write
$$
\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]
:=
\begin{cases}
\jmath_L^{(N)}\,d\Gamma_N(\mathcal T_{a,L}[\beta])\,\jmath_L^{(N)\,*}, & N\le 2L,\\
0, & N>2L,
\end{cases}
$$
$$
\widetilde{\mathcal T}^{\mathcal F}_{a,L}[\beta]
:=
\bigoplus_{N\ge 0}\widetilde{\mathcal T}_{a,L}^{(N)}[\beta].
$$
Then:

1. for every fixed sector cutoff $N_{\max}$ there exists $L_1(\beta,a,N_{\max})$ such that for all $L\ge L_1(\beta,a,N_{\max})$ and all $0\le N\le N_{\max}$,
  $$
  \widetilde{\mathcal T}_{a,L}^{(N)}[\beta]
  =
  P_L^{(N)}\,d\Gamma_N(\mathcal T_{a,\infty}[\beta])\,P_L^{(N)};
  $$
  in particular, on the embedded subspace $\Lambda^N(\jmath_L\mathcal H_L)\subset\Lambda^N\mathcal H_\infty$ these operators agree exactly with $d\Gamma_N(\mathcal T_{a,\infty}[\beta])$;
2. the operator $\mathcal T_{a,\infty}[\beta]$ is bounded, so
  $$
  \|d\Gamma_N(\mathcal T_{a,\infty}[\beta])\|
  \le
  N\|\mathcal T_{a,\infty}[\beta]\|,
  $$
  and therefore $d\Gamma(\mathcal T_{a,\infty}[\beta])$ is well defined on the number-operator domain
  $$
  \operatorname{Dom}\mathcal N
  :=
  \Bigl\{\Psi=(\Psi^{(N)}):\sum_{N\ge 0}N^2\|\Psi^{(N)}\|^2 < \infty\Bigr\};
  $$
  in particular, it is closed on this domain and the algebraic finite-particle subspace is a core. Moreover there exists $C_\beta < \infty$ such that for every $L$ and every $N$,
  $$
  \|\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\|
  \le
  C_\beta N;
  $$
3. the zero-extended finite-volume Fock operators $\widetilde{\mathcal T}^{\mathcal F}_{a,L}[\beta]$ converge strongly to $d\Gamma(\mathcal T_{a,\infty}[\beta])$ on $\operatorname{Dom}\mathcal N$ as $L\to\infty$.

Proof.

For item (1), Proposition 1A gives $\jmath_L\,\mathcal T_{a,L}[\beta]\,\jmath_L^*=\mathcal T_{a,\infty}[\beta]$ for all sufficiently large $L$. Functoriality of second quantization therefore yields, on every fixed sector $N\le 2L$,
$$
\jmath_L^{(N)}\,d\Gamma_N(\mathcal T_{a,L}[\beta])\,\jmath_L^{(N)\,*}
=
P_L^{(N)}\,d\Gamma_N(\mathcal T_{a,\infty}[\beta])\,P_L^{(N)},
$$
which is the displayed identity. On $\Lambda^N(\jmath_L\mathcal H_L)$ one has $P_L^{(N)}=I$, so the two operators agree there exactly.

For item (2), if $B$ is bounded on a one-particle Hilbert space then
$$
\|d\Gamma_N(B)\|\le N\|B\|
$$
on the $N$-particle sector, so the displayed bound follows with $B=\mathcal T_{a,\infty}[\beta]$. Hence the direct sum $d\Gamma(\mathcal T_{a,\infty}[\beta])$ is defined on $\operatorname{Dom}\mathcal N$.
For bounded one-particle operators this direct sum is the standard number-operator graph norm closure of its restriction to the algebraic finite-particle subspace, so it is closed and that finite-particle subspace is a core.
Also,
$$
\|\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\|
\le
N\|\mathcal T_{a,L}[\beta]\|
\qquad
(N\le 2L),
$$
while $\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]=0$ for $N>2L$. Proposition 1A gives $\|\mathcal T_{a,L}[\beta]\|=\|\mathcal T_{a,\infty}[\beta]\|$ for all sufficiently large $L$, and only finitely many small $L$ remain, so $\sup_L\|\mathcal T_{a,L}[\beta]\|

<

\infty$. This yields the uniform bound with some finite $C_\beta$.

For item (3), let $\Psi=(\Psi^{(N)})\in\operatorname{Dom}\mathcal N$. For each fixed $N$, the projections $P_L^{(N)}$ converge strongly to the identity on $\Lambda^N\mathcal H_\infty$. Once $L$ is large enough that item (1) applies on that sector,
$$
\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]
=
P_L^{(N)}\,d\Gamma_N(\mathcal T_{a,\infty}[\beta])\,P_L^{(N)},
$$
so
$$
\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\Psi^{(N)}
\longrightarrow
d\Gamma_N(\mathcal T_{a,\infty}[\beta])\Psi^{(N)}.
$$
Moreover, by item (2),
$$
\bigl\|
\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\Psi^{(N)}
-
d\Gamma_N(\mathcal T_{a,\infty}[\beta])\Psi^{(N)}
\bigr\|
\le
\bigl(C_\beta+\|\mathcal T_{a,\infty}[\beta]\|\bigr)N\|\Psi^{(N)}\|.
$$
The square of the right-hand side is summable over $N$ because $\Psi\in\operatorname{Dom}\mathcal N$. Dominated convergence over the particle-number direct sum therefore gives
$$
\widetilde{\mathcal T}^{\mathcal F}_{a,L}[\beta]\Psi
\longrightarrow
d\Gamma(\mathcal T_{a,\infty}[\beta])\Psi,
$$
as claimed.

$ \square $

**Sufficient hypothesis package for a future genuine infinite-volume / infinite-Fock theorem.**

Write
$$
\mathcal F(\mathcal H_\infty):=\bigoplus_{N\ge 0}\Lambda^N\mathcal H_\infty
$$
for an infinite one-particle Hilbert space $\mathcal H_\infty$, and let $\mathcal F_{\mathrm{fin}}(\mathcal D_\infty)$ denote the algebraic finite-particle subspace generated by finite wedges of vectors from a dense one-particle core $\mathcal D_\infty\subset\mathcal H_\infty$. Assume that for each lattice size $L$ there are isometric embeddings
$$
\jmath_L:\mathcal H_L\hookrightarrow\mathcal H_\infty,
\qquad
\jmath_L^{(N)}:\Lambda^N\mathcal H_L\hookrightarrow\Lambda^N\mathcal H_\infty,
$$
and that $\mathcal D_\infty$ has the eventual-inclusion property that every $\psi\in\mathcal D_\infty$ lies in $\jmath_L\mathcal H_L$ for all sufficiently large $L$. Suppose furthermore that the following hold.

1. *Sectorwise infinite-volume limits.* For every fixed $N$, slab thickness $\Delta$, and localized supports $R,S$, the transported operators
  $$
  \widetilde X_{L}^{(N)}
  :=
  \begin{cases}
  \jmath_L^{(N)}X_L^{(N)}\jmath_L^{(N)\,*}, & N\le 2L,\\
  0, & N>2L,
  \end{cases}
  $$
  attached to
  $X_L^{(N)}\in\{\Gamma_{0,L}^{(N)}(\Delta),\Gamma_{R,L}^{(N)}(\Delta),J_{R,L}^{(N)}(\Delta),E_{R,S,L}^{(N)}(\Delta)\}$
  converge strongly on $\Lambda^N\mathcal H_\infty$ as $L\to\infty$ to bounded limits
  $\Gamma_{0,\infty}^{(N)}(\Delta)$,
  $\Gamma_{R,\infty}^{(N)}(\Delta)$,
  $J_{R,\infty}^{(N)}(\Delta)$,
  $E_{R,S,\infty}^{(N)}(\Delta)$.
2. *Particle-number-uniform kernel bounds.* For each fixed $\Delta$ and support data,
  $$
  \sup_{L,N}\Bigl(
  \|\widetilde\Gamma_{0,L}^{(N)}(\Delta)\|
  +\|\widetilde\Gamma_{R,L}^{(N)}(\Delta)\|
  +\|\widetilde J_{R,L}^{(N)}(\Delta)\|
  +\|\widetilde E_{R,S,L}^{(N)}(\Delta)\|
  \Bigr) < \infty.
  $$
3. *Infinite-volume one-particle bond-centered limit.* The transported one-particle bond-centered operators
  $$
  \widetilde{\mathcal T}_{a,L}[\beta]:=\jmath_L\,\mathcal T_{a,L}[\beta]\,\jmath_L^*
  $$
  converge on $\mathcal D_\infty$ to a closed one-particle operator $\mathcal T_{a,\infty}[\beta]$, i.e.
  $$
  \widetilde{\mathcal T}_{a,L}[\beta]\psi \longrightarrow \mathcal T_{a,\infty}[\beta]\psi
  \qquad
  (\psi\in\mathcal D_\infty).
  $$
4. *Finite-volume particle-number-uniform second-quantized bound.* If
  $$
  \widetilde{\mathcal T}_{a,L}^{(N)}[\beta]
  :=
  \begin{cases}
  \jmath_L^{(N)}\,d\Gamma_N(\mathcal T_{a,L}[\beta])\,\jmath_L^{(N)\,*}, & N\le 2L,\\
  0, & N>2L,
  \end{cases}
  $$
  then there exists $C_\beta < \infty$ such that for every $L$ and every $N$,
  $$
  \|\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\|
  \le
  C_\beta N.
  $$
5. *Full-Fock operator construction.* The direct sum
  $$
  d\Gamma\!\bigl(\mathcal T_{a,\infty}[\beta]\bigr)
  :=
  \bigoplus_{N\ge 0}d\Gamma_N\!\bigl(\mathcal T_{a,\infty}[\beta]\bigr)
  $$
  is well defined as a closed operator on $\mathcal F(\mathcal H_\infty)$ with core $\mathcal F_{\mathrm{fin}}(\mathcal D_\infty)$.

Remark.

Proposition 1A and Corollary 3A now supply items (3) through (5) of this package. So the genuinely unproved part of the future infinite-volume theorem is concentrated in the primitive kernels, comparison maps, and exchange defects together with the particle-number-uniform control needed to sum their sectorwise limits.

**Conditional proposition.**

(What the sufficient package yields).

Under the package above, the finite-volume number-preserving relativistic ISP data admit a genuine infinite-volume / infinite one-particle-space Fock lift. More precisely:

1. the bounded operators
  $$
  \Gamma_{0,\infty}(\Delta):=\bigoplus_{N\ge 0}\Gamma_{0,\infty}^{(N)}(\Delta),
  \qquad
  \Gamma_{R,\infty}(\Delta):=\bigoplus_{N\ge 0}\Gamma_{R,\infty}^{(N)}(\Delta),
  $$
  $$
  J_{R,\infty}(\Delta):=\bigoplus_{N\ge 0}J_{R,\infty}^{(N)}(\Delta),
  \qquad
  E_{R,S,\infty}(\Delta):=\bigoplus_{N\ge 0}E_{R,S,\infty}^{(N)}(\Delta)
  $$
  are well defined on $\mathcal F(\mathcal H_\infty)$, and the zero-extended transported finite-volume Fock operators converge strongly to them as $L\to\infty$;
2. writing
  $$
  \widetilde{\mathcal T}_{a,L}^{\mathcal F}[\beta]
  :=
  \bigoplus_{N\ge 0}\widetilde{\mathcal T}_{a,L}^{(N)}[\beta],
  $$
  one has
  $$
  \widetilde{\mathcal T}_{a,L}^{\mathcal F}[\beta]\Psi
  \longrightarrow
  d\Gamma\!\bigl(\mathcal T_{a,\infty}[\beta]\bigr)\Psi
  \qquad
  (\Psi\in\mathcal F_{\mathrm{fin}}(\mathcal D_\infty));
  $$
3. if, for each fixed $N$, the corresponding sectorwise convergence extends from $\Lambda^N\mathcal D_\infty$ to $\operatorname{Dom}\!\bigl(d\Gamma_N(\mathcal T_{a,\infty}[\beta])\bigr)$, then the same convergence holds on
  $$
  \operatorname{Dom}\mathcal N
  \cap
  \operatorname{Dom}\!\bigl(d\Gamma(\mathcal T_{a,\infty}[\beta])\bigr)
  $$
  by dominated convergence over particle number.

Hence the genuine infinite-volume number-preserving tangential generator would be
$$
K_{\parallel,\mathcal F_\infty}[\beta]
=
d\Gamma\!\bigl(\mathcal T_{a,\infty}[\beta]\bigr).
$$

Proof.

For the primitive kernels, comparison maps, and exchange defects, assumption (2) makes each displayed direct sum uniformly bounded on the Hilbert direct sum $\mathcal F(\mathcal H_\infty)$. For any
$$
\Psi=(\Psi^{(N)})_{N\ge 0}\in\mathcal F(\mathcal H_\infty),
$$
the difference between a zero-extended transported finite-volume operator and its limiting direct sum has squared norm equal to the sum of the sectorwise squared norms. For each fixed $N$ those terms go to zero by assumption (1), and they are dominated by a constant multiple of $\|\Psi^{(N)}\|^2$ by assumption (2). Dominated convergence over $N$ therefore gives strong convergence on the whole Fock space.

For the tangential operator, write
$$
\widetilde{\mathcal T}_{a,L}^{\mathcal F}[\beta]
:=
\bigoplus_{N\ge 0}\widetilde{\mathcal T}_{a,L}^{(N)}[\beta].
$$
Let
$$
\Phi=\psi_1\wedge\cdots\wedge\psi_N\in\Lambda^N\mathcal D_\infty.
$$
By the eventual-inclusion property of $\mathcal D_\infty$, all $\psi_j$ lie in $\jmath_L\mathcal H_L$ once $L$ is large enough. On $\Lambda^N(\jmath_L\mathcal H_L)$ one therefore has
$$
\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]
=
d\Gamma_N(\widetilde{\mathcal T}_{a,L}[\beta]).
$$
Applying the same slotwise argument used in Theorem 1 and assumption (3) now gives
$$
\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\Phi
\longrightarrow
d\Gamma_N\!\bigl(\mathcal T_{a,\infty}[\beta]\bigr)\Phi.
$$
By linearity the same holds for every $\Phi\in\Lambda^N\mathcal D_\infty$. Summing over the finitely many occupied sectors yields the displayed convergence on $\mathcal F_{\mathrm{fin}}(\mathcal D_\infty)$. If, for each fixed $N$, this sectorwise convergence extends to $\operatorname{Dom}\!\bigl(d\Gamma_N(\mathcal T_{a,\infty}[\beta])\bigr)$, then for every
$$
\Psi\in \operatorname{Dom}\mathcal N\cap \operatorname{Dom}\!\bigl(d\Gamma(\mathcal T_{a,\infty}[\beta])\bigr)
$$
the sectorwise squared difference norms are dominated by a constant multiple of
$$
N^2\|\Psi^{(N)}\|^2+\bigl\|d\Gamma_N(\mathcal T_{a,\infty}[\beta])\Psi^{(N)}\bigr\|^2,
$$
because assumption (4) gives
$$
\|\widetilde{\mathcal T}_{a,L}^{(N)}[\beta]\Psi^{(N)}\|
\le
C_\beta N\|\Psi^{(N)}\|.
$$
The sum of these dominators is finite by the two domain assumptions. Dominated convergence over $N$ therefore gives the extension to that domain.

$ \square $

Remark.

The proposition is intentionally conditional. It is not an additional theorem extracted from the present stack. Its purpose is to isolate the exact future hypothesis package that would have to be proved in order to upgrade the present fixed-$N$ stabilization to a genuine infinite-volume / infinite-Fock theorem.

## First local sector-changing examples

The exact number-preserving lift does not yet by itself address genuine sector-changing dynamics. The next honest step is therefore to isolate the first exact local examples showing where off-diagonal sector blocks enter, and then to determine how far the disjoint local exchange-defect algebra can already be pushed without inventing a general finite-support theorem.

**Definition 4**

(Local source/sink term).

Fix a single mode $A\in\mathcal C_L$ and a coupling $\eta\in\mathbb R$. On the finite truncation $\mathcal F_{L,\le N_{\max}}$, define the local source/sink perturbation
$$
\widehat S_A
:=
\eta\bigl(c_A^\dagger+c_A\bigr),
$$
and the perturbed Hamiltonian
$$
\widehat H_{\mathrm{src}}
:=
d\Gamma(h_0)+\widehat S_A.
$$

**Proposition 2**

(Exact leading sector selection for a local source/sink term).

Let $\Pi_N$ denote the projector onto $\mathcal F_L^{(N)}$, and let
$$
\widehat U_{\mathrm{src}}(\Delta):=e^{-i\Delta\widehat H_{\mathrm{src}}}.
$$
Then for every $N$ with $0\le N\le N_{\max}$ one has
$$
\Pi_{N\pm1}\widehat U_{\mathrm{src}}(\Delta)\Pi_N
=
-\,i\Delta\,\Pi_{N\pm1}\widehat S_A\Pi_N+O(\Delta^2),
$$
while
$$
\Pi_M\widehat U_{\mathrm{src}}(\Delta)\Pi_N
=
O(\Delta^2)
\qquad\text{for }|M-N|>1.
$$
Consequently the primitive kernel of $\widehat U_{\mathrm{src}}(\Delta)$ has first nonzero sector-changing probabilities only in the adjacent sector blocks $N\leftrightarrow N\pm1$, and those probabilities are $O(\Delta^2)$.

Proof.

Expand
$$
\widehat U_{\mathrm{src}}(\Delta)
=
I-i\Delta\widehat H_{\mathrm{src}}+O(\Delta^2).
$$
The number-preserving quadratic part $d\Gamma(h_0)$ commutes with every $\Pi_N$, whereas $c_A^\dagger$ raises particle number by one and $c_A$ lowers it by one. Therefore the only first-order off-diagonal sector blocks are the $N\to N\pm1$ blocks displayed above. Any transition to sectors with $|M-N|>1$ requires at least two applications of the source/sink term and therefore begins at order $O(\Delta^2)$ in amplitude. Squaring moduli gives the $O(\Delta^2)$ onset for the adjacent sector probabilities.

$ \square $

Remark.

This is the simplest exact local sector-changing example. It breaks fermion parity and creates the first off-diagonal comparison blocks between neighboring particle-number sectors.

**Definition 5**

(Local pair-creation / pair-annihilation term).

Fix a lattice site $n$ and define
$$
\widehat P_n
:=
g\bigl(c_{n,\uparrow}^\dagger c_{n,\downarrow}^\dagger + c_{n,\downarrow}c_{n,\uparrow}\bigr)
$$
with coupling $g\in\mathbb R$. Let
$$
\widehat H_{\mathrm{pair}}
:=
d\Gamma(h_0)+\widehat P_n.
$$

**Proposition 3**

(Exact leading sector selection for a local pair term).

With
$$
\widehat U_{\mathrm{pair}}(\Delta):=e^{-i\Delta\widehat H_{\mathrm{pair}}},
$$
one has
$$
\Pi_{N\pm2}\widehat U_{\mathrm{pair}}(\Delta)\Pi_N
=
-\,i\Delta\,\Pi_{N\pm2}\widehat P_n\Pi_N+O(\Delta^2),
$$
while
$$
\Pi_M\widehat U_{\mathrm{pair}}(\Delta)\Pi_N
=
O(\Delta^2)
\qquad\text{for }|M-N|\neq 2
$$
among the sector-changing blocks. Consequently the first nonzero sector-changing probabilities occur only in the $N\leftrightarrow N\pm2$ blocks and begin at order $O(\Delta^2)$.

Proof.

Again expand the unitary to first order in $\Delta$. The quadratic number-preserving part remains sector diagonal. The operator $c_{n,\uparrow}^\dagger c_{n,\downarrow}^\dagger$ raises particle number by two, while $c_{n,\downarrow}c_{n,\uparrow}$ lowers it by two. Hence the only first-order off-diagonal sector blocks are the $N\to N\pm2$ blocks shown above. Larger sector jumps require at least two insertions of the pair term and therefore begin at order $O(\Delta^2)$ in amplitude. Squaring moduli gives the $O(\Delta^2)$ onset for the corresponding sector-changing probabilities.

$ \square $

Remark.

Unlike the source/sink term, the pair term preserves fermion parity. So the two examples isolate two different kinds of local sector-changing comparison map one may want later exact exchange-defect theorems to treat.

**Boundary remark.**

Because the number-preserving reference kernel is block diagonal, multiplying a sector-changing primitive kernel by its inverse on the right does not erase sector selection. So the comparison maps inherit the same first nontrivial off-diagonal sector blocks as the primitive kernels in the two examples above.

**Definition 6**

(Full-Fock local toggle kernels).

Work now on the full finite-lattice Fock space $\mathcal F_L$ with occupation basis $\{|X\rangle\}_{X\subset\mathcal C_L}$. For a mode $A\in\mathcal C_L$, define the source-toggle kernel
$$
[\mathsf T_A]_{XY}:=
\begin{cases}
1, & X=Y\triangle\{A\},\\
0, & \text{otherwise},
\end{cases}
$$
where $\triangle$ denotes symmetric difference of occupation sets. For a lattice site $n$, define the pair-toggle kernel $\mathsf P_n$ by
$$
[\mathsf P_n]_{XY}:=
\begin{cases}
1, & X \text{ and } Y \text{ agree outside } \{(n,\uparrow),(n,\downarrow)\}\\
&\text{and the local occupation toggles }00\leftrightarrow 11,\\
0, & \text{otherwise}.
\end{cases}
$$
Let $\mathsf Q_n$ be the diagonal projector onto configurations with even local pair occupancy at site $n$, i.e.
$$
[\mathsf Q_n]_{XX}=
\begin{cases}
1, & \text{if the local occupation at }n\text{ is }00\text{ or }11,\\
0, & \text{if it is }01\text{ or }10.
\end{cases}
$$

**Proposition 4**

(Exact first comparison coefficients on the full finite lattice).

Define
$$
J_A^{\mathrm{src}}(\Delta)
:=
\Gamma\!\bigl(e^{-i\Delta(d\Gamma(h_0)+\widehat S_A)}\bigr)\,
\Gamma\!\bigl(e^{-i\Delta d\Gamma(h_0)}\bigr)^{-1},
$$
and
$$
J_n^{\mathrm{pair}}(\Delta)
:=
\Gamma\!\bigl(e^{-i\Delta(d\Gamma(h_0)+\widehat P_n)}\bigr)\,
\Gamma\!\bigl(e^{-i\Delta d\Gamma(h_0)}\bigr)^{-1}.
$$
Then
$$
J_A^{\mathrm{src}}(\Delta)
=
I+\Delta^2\eta^2(\mathsf T_A-I)+O(\Delta^4),
$$
and
$$
J_n^{\mathrm{pair}}(\Delta)
=
I+\Delta^2g^2(\mathsf P_n-\mathsf Q_n)+O(\Delta^4).
$$

Proof.

For an off-diagonal kernel entry between configurations $X\neq Y$, the order-$\Delta^2$ coefficient of the primitive slab kernel is $|\widehat H_{XY}|^2$. Since the number-preserving reference Hamiltonian $d\Gamma(h_0)$ is sector diagonal, it has no off-diagonal matrix elements between different particle-number sectors. So for the source/sink perturbation the order-$\Delta^2$ sector-changing coefficient is
$$
|\langle X|\widehat S_A|Y\rangle|^2
=
\eta^2
$$
exactly when $X=Y\triangle\{A\}$, and otherwise it is zero. This gives the off-diagonal part $\eta^2\mathsf T_A$. On the full finite lattice each configuration has exactly one allowed $A$-toggle, so column normalization forces the diagonal correction to be $-\eta^2 I$. The pair term is identical in structure: its only nonzero off-diagonal matrix elements connect local occupations $00$ and $11$ at site $n$, each with squared magnitude $g^2$, giving the off-diagonal kernel $g^2\mathsf P_n$. The diagonal correction is then the negative column-sum projector $-g^2\mathsf Q_n$. Since, for either local perturbation,
$$
J(\Delta)=\Gamma_{\mathrm{loc}}(\Delta)\Gamma_0(\Delta)^{-1}
=
I+\Delta^2(\text{kernel-coefficient difference})+O(\Delta^4),
$$
the displayed formulas follow.

$ \square $

**Corollary 4**

(Vanishing of the naive $\Delta^4$ disjoint local sector-changing defect on the full finite lattice).

Let $R$ and $S$ be disjoint local sector-changing supports on $\mathcal F_L$, of source/source, pair/pair, or source/pair type. Then their first comparison coefficients commute:
$$
[A_R^{(1)},A_S^{(1)}]=0.
$$
Consequently the corresponding exchange defect satisfies
$$
E_{R,S}(\Delta)=I+O(\Delta^6).
$$

Proof.

For disjoint supports, the toggle kernels of Definition 6 act on disjoint local occupation bits. So symmetric-difference toggles commute:
$$
\mathsf T_A\mathsf T_B=\mathsf T_B\mathsf T_A,
\qquad
\mathsf P_m\mathsf P_n=\mathsf P_n\mathsf P_m
\qquad (m\neq n),
$$
and the same is true for disjoint source/pair combinations. The diagonal factors $I$ and $\mathsf Q_n$ commute with everything supported away from their own local support. Hence the first comparison coefficients from Proposition 4 commute pairwise when the supports are disjoint. For any two $\Delta^2$-onset comparison maps one has the group-commutator expansion
$$
E_{R,S}(\Delta)
=
I+\Delta^4[A_R^{(1)},A_S^{(1)}]+O(\Delta^6),
$$
so the vanishing of the commutator removes the entire $\Delta^4$ term.

$ \square $

Remark.

Corollary 4 removes the naive order and isolates the first remaining candidate:
$$
C_{R,S}^{(3)}=[A_R^{(1)},A_S^{(2)}]+[A_R^{(2)},A_S^{(1)}],
$$
The next subsection resolves that coefficient exactly in the disjoint local source/source, source/pair, and pair/pair classes.

### Exact first nonzero disjoint local exchange coefficient

For the free-Dirac reference on the fixed finite lattice, the answer is yes at the disjoint local level. Once the $\Delta^4$ term has been removed, the order-$\Delta^6$ coefficient reduces exactly to minimal local bond blocks: two modes for bonded source/source pairs, three modes for source/pair adjacency, and four modes for adjacent pair sites.

**Definition 7**

(Universal local $\Delta^6$ exchange kernels).

For two modes $A,B\in\mathcal C_L$, let $\mathsf Z_{AB}$ be the diagonal parity-sign kernel
$$
[\mathsf Z_{AB}]_{XX}:=(-1)^{n_A(X)+n_B(X)},
$$
where $n_A(X),n_B(X)\in\{0,1\}$ are the occupation bits of configuration $X$ at $A,B$. Define the two-mode source/source kernel
$$
\Omega_{A,B}^{\mathrm{ss}}
:=
\frac23\,(\mathsf T_A-\mathsf T_B)\mathsf Z_{AB}.
$$
In the local basis $00,10,01,11$ on the $(A,B)$ bits, this is
$$
\Omega_{A,B}^{\mathrm{ss}}
=
\frac23
\begin{pmatrix}
0 & -1 & 1 & 0\\
1 & 0 & 0 & -1\\
-1 & 0 & 0 & 1\\
0 & 1 & -1 & 0
\end{pmatrix}.
$$
For the three-mode source/pair block $(a,b,c)$ with source mode $a$, pair block $(b,c)$, and active number-preserving bond $a\leftrightarrow c$, define $\Omega_{a|bc}^{\mathrm{sp}}$ in the local basis
$$
|0;00\rangle,\ |1;00\rangle,\ |0;10\rangle,\ |1;10\rangle,\ |0;01\rangle,\ |1;01\rangle,\ |0;11\rangle,\ |1;11\rangle
$$
with source bit on $a$ and pair bits on $(b,c)$, by
$$
\Omega_{a|bc}^{\mathrm{sp}}
=
\begin{pmatrix}
0 & -\frac{5}{12} & \frac12 & -\frac13 & -\frac1{12} & 0 & \frac13 & 0\\
\frac{5}{12} & 0 & 0 & 0 & \frac13 & -\frac{5}{12} & 0 & -\frac13\\
-\frac12 & 0 & 0 & \frac1{12} & 0 & 0 & \frac{5}{12} & 0\\
\frac13 & 0 & -\frac1{12} & 0 & 0 & 0 & -\frac13 & \frac1{12}\\
\frac1{12} & -\frac13 & 0 & 0 & 0 & -\frac1{12} & 0 & \frac13\\
0 & \frac{5}{12} & 0 & 0 & \frac1{12} & 0 & 0 & -\frac12\\
-\frac13 & 0 & -\frac{5}{12} & \frac13 & 0 & 0 & 0 & \frac{5}{12}\\
0 & \frac13 & 0 & -\frac1{12} & -\frac13 & \frac12 & -\frac{5}{12} & 0
\end{pmatrix}.
$$
For the four-mode pair/pair block $(a,b,c,d)$ with pair blocks $(a,b)$ and $(c,d)$ and crossed number-preserving bonds $a\leftrightarrow d$ and $b\leftrightarrow c$, define $\Omega_{ab|cd}^{\mathrm{pp}}$ on the natural pair-site basis
$$
|xy;zw\rangle,
\qquad
xy,zw\in\{00,10,01,11\},
$$
with each local pair ordered as $00,10,01,11$, by
$$
\Omega_{ab|cd}^{\mathrm{pp}}|00;00\rangle
=
\frac56\bigl(|11;00\rangle-|00;11\rangle\bigr),
$$
$$
\Omega_{ab|cd}^{\mathrm{pp}}|10;00\rangle
=
\frac56\bigl(-|00;01\rangle+|11;01\rangle\bigr),
\qquad
\Omega_{ab|cd}^{\mathrm{pp}}|01;00\rangle
=
\frac56\bigl(-|00;10\rangle+|11;10\rangle\bigr),
$$
$$
\Omega_{ab|cd}^{\mathrm{pp}}|11;00\rangle
=
\frac56\bigl(-|00;00\rangle+|11;11\rangle\bigr),
$$
$$
\Omega_{ab|cd}^{\mathrm{pp}}|00;10\rangle
=
\frac56\bigl(|01;00\rangle-|01;11\rangle\bigr),
\qquad
\Omega_{ab|cd}^{\mathrm{pp}}|11;10\rangle
=
\frac56\bigl(-|01;00\rangle+|01;11\rangle\bigr),
$$
$$
\Omega_{ab|cd}^{\mathrm{pp}}|00;01\rangle
=
\frac56\bigl(|10;00\rangle-|10;11\rangle\bigr),
\qquad
\Omega_{ab|cd}^{\mathrm{pp}}|11;01\rangle
=
\frac56\bigl(-|10;00\rangle+|10;11\rangle\bigr),
$$
$$
\Omega_{ab|cd}^{\mathrm{pp}}|00;11\rangle
=
\frac56\bigl(|00;00\rangle-|11;11\rangle\bigr),
\qquad
\Omega_{ab|cd}^{\mathrm{pp}}|11;11\rangle
=
\frac56\bigl(-|11;00\rangle+|00;11\rangle\bigr),
$$
$$
\Omega_{ab|cd}^{\mathrm{pp}}|10;11\rangle
=
\frac56\bigl(|00;01\rangle-|11;01\rangle\bigr),
\qquad
\Omega_{ab|cd}^{\mathrm{pp}}|01;11\rangle
=
\frac56\bigl(|00;10\rangle-|11;10\rangle\bigr),
$$
and
$$
\Omega_{ab|cd}^{\mathrm{pp}}|10;10\rangle
=
\Omega_{ab|cd}^{\mathrm{pp}}|01;10\rangle
=
\Omega_{ab|cd}^{\mathrm{pp}}|10;01\rangle
=
\Omega_{ab|cd}^{\mathrm{pp}}|01;01\rangle
=0.
$$
In the full finite lattice, these kernels are embedded by tensoring with the identity outside the indicated local modes.

**Theorem 2**

(Exact first nonzero disjoint local sector-changing defect coefficient on the full finite lattice).

For the free-Dirac reference Hamiltonian on the full finite lattice, let $C_{R,S}^{(3)}$ be the order-$\Delta^6$ coefficient defined by
$$
E_{R,S}(\Delta)=I+\Delta^6 C_{R,S}^{(3)}+O(\Delta^8)
$$
after Corollary 4. Then $C_{R,S}^{(3)}$ is exact, mass-blind, and completely local in the following sense.

1. *Source/source.* Let $A,B\in\mathcal C_L$ be disjoint source modes. If $A$ and $B$ are not joined by a free-Dirac one-particle bond, then
  $$
  C_{A,B}^{(3)}=0.
  $$
  If they are joined by such a bond, then
  $$
  C_{A,B}^{(3)}
  =
  \frac{\eta_A^2\eta_B^2}{4a^2}\,\Omega_{A,B}^{\mathrm{ss}}.
  $$
  Equivalently, the disjoint local source/source defect is already $I+O(\Delta^8)$ unless the two source modes are opposite-spin nearest neighbors.
2. *Source/pair.* Let $A$ be a source mode and $n$ a disjoint pair site. If no free-Dirac bond joins $A$ to either mode at site $n$, then
  $$
  C_{A,n}^{(3)}=0.
  $$
  If $A$ lies one free-Dirac hop from $n$, let $c_n(A)\in\{(n,\uparrow),(n,\downarrow)\}$ be the unique mode at site $n$ directly coupled to $A$, and let $b_n(A)$ be the other mode at site $n$. Then
  $$
  C_{A,n}^{(3)}
  =
  \frac{\eta_A^2 g_n^2}{4a^2}\,\Omega_{A|\,b_n(A)c_n(A)}^{\mathrm{sp}}.
  $$
  So the disjoint local source/pair defect is $I+O(\Delta^8)$ unless the source mode lies one free-Dirac hop from the pair site.
3. *Pair/pair.* Let $m\neq n$ be disjoint pair sites. If the sites are not adjacent, then
  $$
  C_{m,n}^{(3)}=0.
  $$
  If $m$ and $n$ are adjacent, then
  $$
  C_{m,n}^{(3)}
  =
  \frac{g_m^2 g_n^2}{4a^2}\,\Omega_{(m,\uparrow)(m,\downarrow)\,|\,(n,\uparrow)(n,\downarrow)}^{\mathrm{pp}}.
  $$
  Hence the disjoint local pair/pair defect is $I+O(\Delta^8)$ for nonadjacent sites and has a universal adjacent-site $\Delta^6$ coefficient otherwise.

In particular, the first nonzero disjoint local sector-changing defect coefficient is already fixed exactly by universal two-, three-, and four-mode kernels, with no mass dependence and no contribution from supports beyond one free-Dirac hop.

Proof sketch.

By the exact higher-order exchange package, once Corollary 4 kills the order-$\Delta^4$ term, the first remaining coefficient is
$$
C_{R,S}^{(3)}=[A_R^{(1)},A_S^{(2)}]+[A_R^{(2)},A_S^{(1)}].
$$
For a local source or pair perturbation $V$, the off-diagonal order-$\Delta^4$ primitive-kernel coefficient depends only on the sector-changing words
$$
H_0V+VH_0,
\qquad
H_0^2V+H_0VH_0+VH_0^2+V^3,
$$
because the remaining quadratic and cubic words preserve particle number and therefore do not contribute to the relevant sector-changing comparison block. Since $H_0=d\Gamma(h_0)$ is the nearest-neighbor free-Dirac lift, the only part of $A^{(2)}$ that can fail to commute with a disjoint local first coefficient is the part carried by free-Dirac bonds incident on the local support. Every other contribution acts on occupation bits disjoint from the other local first coefficient and commutes with it.

This reduces the full-lattice calculation exactly to minimal local bond blocks: a two-mode block when two source modes share one free-Dirac bond, a three-mode block when a source mode lies one free-Dirac hop from a pair site, and a four-mode block when two pair sites are adjacent. Direct finite local calculation of those blocks gives the universal kernels of Definition 7. The diagonal mass terms enter only through local one-particle phases and cancel from the kernel commutator coefficient, so the result is mass-blind; bond phases survive only through the common free-Dirac bond factor $|\lambda|^2=1/(4a^2)$ of the relevant local block. Embedding the local block coefficients back into $\mathcal F_L$ gives the displayed formulas. If no active one-hop block exists, every term in the commutator coefficient acts on bits disjoint from the other local first coefficient, so $C_{R,S}^{(3)}=0$.

$ \square $

**Definition 8**

(Exact disjoint-local $\Delta^6$ strip-channel basis).

For a finite local mode set $U$, define the symmetric-difference toggle kernel
$$
[\mathsf S_E]_{XY}
:=
\begin{cases}
1, & X=Y\triangle E,\\
0, & \text{otherwise},
\end{cases}
$$
for every nonempty subset $E\subset U$. For singletons, $\mathsf S_{\{A\}}=\mathsf T_A$. For two-mode subsets this is

*not*

the same as the one-region pair-toggle kernel $\mathsf P_n$: the kernel $\mathsf S_{\{i,j\}}$ toggles all four local occupations by symmetric difference, including $01\leftrightarrow10$, whereas $\mathsf P_n$ only toggles $00\leftrightarrow11$.
For any two modes $i,j$ in the same local block, write $\mathsf Z_{ij}$ for the two-mode diagonal parity-sign kernel of Definition 7 formed from the occupation bits at $i$ and $j$.

For the bonded source/source block $(A,B)$, define the exchanged strip channel
$$
X_{A|B}^{\mathrm{ss}}
:=
\frac23(\mathsf T_A-\mathsf T_B)\mathsf Z_{AB}.
$$
For the source/pair block $(a,b,c)$, define
$$
X_{a|bc}^{\mathrm{sp};a}
:=
\mathsf S_{\{a\}}\Bigl(\frac14\mathsf Z_{ab}+\frac16\mathsf Z_{ac}\Bigr),
\qquad
X_{a|bc}^{\mathrm{sp};b}
:=
-\mathsf S_{\{b\}}\Bigl(\frac14\mathsf Z_{ab}+\frac14\mathsf Z_{bc}\Bigr),
$$
$$
X_{a|bc}^{\mathrm{sp};ab}
:=
\mathsf S_{\{a,b\}}\Bigl(\frac16\mathsf Z_{ac}+\frac16\mathsf Z_{bc}\Bigr),
\qquad
X_{a|bc}^{\mathrm{sp};c}
:=
\mathsf S_{\{c\}}\Bigl(-\frac16\mathsf Z_{ac}+\frac14\mathsf Z_{bc}\Bigr),
$$
$$
X_{a|bc}^{\mathrm{sp};ac}
:=
\mathsf S_{\{a,c\}}\Bigl(\frac16\mathsf Z_{ab}-\frac16\mathsf Z_{bc}\Bigr),
\qquad
X_{a|bc}^{\mathrm{sp};bc}
:=
-\mathsf S_{\{b,c\}}\Bigl(\frac16\mathsf Z_{ab}+\frac16\mathsf Z_{ac}\Bigr).
$$
For the adjacent pair/pair block $(a,b,c,d)$, define
$$
X_{ab|cd}^{\mathrm{pp};ab}
:=
\frac{5}{24}\mathsf S_{\{a,b\}}\bigl(\mathsf Z_{ac}+\mathsf Z_{bc}+\mathsf Z_{ad}+\mathsf Z_{bd}\bigr),
$$
$$
X_{ab|cd}^{\mathrm{pp};ac}
:=
\frac{5}{24}\mathsf S_{\{a,c\}}\bigl(-\mathsf Z_{ab}-\mathsf Z_{bc}+\mathsf Z_{ad}+\mathsf Z_{cd}\bigr),
\qquad
X_{ab|cd}^{\mathrm{pp};bc}
:=
\frac{5}{24}\mathsf S_{\{b,c\}}\bigl(\mathsf Z_{ab}-\mathsf Z_{ac}+\mathsf Z_{bd}-\mathsf Z_{cd}\bigr),
$$
$$
X_{ab|cd}^{\mathrm{pp};ad}
:=
\frac{5}{24}\mathsf S_{\{a,d\}}\bigl(\mathsf Z_{ab}+\mathsf Z_{ac}-\mathsf Z_{bd}-\mathsf Z_{cd}\bigr),
\qquad
X_{ab|cd}^{\mathrm{pp};bd}
:=
\frac{5}{24}\mathsf S_{\{b,d\}}\bigl(-\mathsf Z_{ab}+\mathsf Z_{bc}-\mathsf Z_{ad}+\mathsf Z_{cd}\bigr),
$$
$$
X_{ab|cd}^{\mathrm{pp};cd}
:=
-\frac{5}{24}\mathsf S_{\{c,d\}}\bigl(\mathsf Z_{ac}+\mathsf Z_{bc}+\mathsf Z_{ad}+\mathsf Z_{bd}\bigr).
$$

**Proposition 5**

(Exact disjoint-local $\Delta^6$ strip-channel classification).

The universal kernels of Definition 7 decompose exactly as
$$
\Omega_{A,B}^{\mathrm{ss}}=X_{A|B}^{\mathrm{ss}},
$$
$$
\Omega_{a|bc}^{\mathrm{sp}}
=
X_{a|bc}^{\mathrm{sp};a}
+X_{a|bc}^{\mathrm{sp};b}
+X_{a|bc}^{\mathrm{sp};ab}
+X_{a|bc}^{\mathrm{sp};c}
+X_{a|bc}^{\mathrm{sp};ac}
+X_{a|bc}^{\mathrm{sp};bc},
$$
and
$$
\Omega_{ab|cd}^{\mathrm{pp}}
=
X_{ab|cd}^{\mathrm{pp};ab}
+X_{ab|cd}^{\mathrm{pp};ac}
+X_{ab|cd}^{\mathrm{pp};bc}
+X_{ab|cd}^{\mathrm{pp};ad}
+X_{ab|cd}^{\mathrm{pp};bd}
+X_{ab|cd}^{\mathrm{pp};cd}.
$$
Hence the genuine exchanged strip channels of the disjoint-local $\Delta^6$ sector-changing problem are exactly:

1. one bonded source/source channel;
2. six source/pair channels on the three-mode active strip; and
3. six adjacent pair/pair channels on the four-mode active strip.

Under translation along the lattice, the corresponding channel coefficients are supported only at the single one-hop displacement $r=1$.

Proof.

For the source/source class, the claim is immediate from Definitions 7 and 8. For the source/pair and pair/pair classes, insert the explicit matrix and basis-action formulas of Definition 7 and compare entry by entry with the channel operators of Definition 8. The identities hold exactly. In the source/pair and pair/pair classes each displayed summand is antisymmetric because the accompanying diagonal parity factor flips sign under the corresponding symmetric-difference toggle. Finally, the translated local classes occur only when the two supports are one free-Dirac hop apart, so the channel coefficient functions are supported only at $r=1$.

$ \square $

**Remark on strip channels.**

The kernels $\mathsf T_A$ and $\mathsf P_n$ are one-region local toggle channels. Proposition 5 now shows that the first genuine two-region sector-changing exchange channels are already classified exactly in the disjoint local $\Delta^6$ classes. What remains open is the broader finite-support strip classification beyond these local classes and its bond-centered continuum reduction.

## What phase 8 now closes and what it defers

With the scope fixed this way, phase 8 is complete in the following exact sense.

1. *Exact full finite-lattice Fock lift.* The primitive kernels, comparison maps, and exchange defects for number-preserving quadratic dynamics decompose exactly into fixed-particle-number sectors, and the sectorwise second-quantized thin-slab law extends to the entire fixed finite-lattice Fock space.
2. *Exact bond-centered sectorwise law.* The one-particle bond-centered thin-slab theorem lifts exactly by second quantization on every finite sector and therefore on the whole fixed finite lattice.
3. *Exact first local sector-changing coefficients.* The source/sink and pair terms identify the first adjacent and next-adjacent sector blocks, and on the full finite lattice their first comparison coefficients are explicit local toggle kernels.
4. *Exact disjoint-local sector-changing exchange law through first nonzero order.* On the full finite lattice, the naive $\Delta^4$ exchange-defect coefficient vanishes for disjoint source/source, pair/pair, and source/pair supports, and the exact first nonzero $\Delta^6$ coefficient is a universal mass-blind local kernel supported on two-, three-, or four-mode blocks.
5. *Exact disjoint-local strip-channel classification.* Those $\Delta^6$ kernels close on one bonded source/source channel, six source/pair channels, and six adjacent pair/pair channels, all supported on the minimal one-hop active strip.

What remains outside the present claim is equally important.

1. *No general finite-support sector-changing exchange-defect theorem yet.* The paper now closes the disjoint local source/source, source/pair, and adjacent pair/pair coefficient at order $\Delta^6$, but it does not yet extend that theorem to broader finite-support sector-changing deformations.
2. *No general finite-support sector-changing strip-channel classification yet.* The disjoint-local $\Delta^6$ classes are now classified exactly, but the broader support-level strip classification and bond-centered continuum package are still open.
3. *No genuine infinite-volume / infinite one-particle-space / unbounded-particle primitive-kernel Fock limit.* The common infinite-volume bond-centered one-particle operator and its second-quantized large-volume lift are now under exact control, but the paper still does not supply the sectorwise infinite-volume limits and particle-number-uniform kernel / inverse bounds needed to pass from the finite-volume primitive kernels, comparison maps, and exchange defects to a genuine $L\to\infty$ infinite-Fock theorem.
4. *No detector/control dynamics yet.* Localized operational devices remain a later phase rather than an implicit assumption here.

**Strategic remark.**

This is the strongest honest phase-8 paper now supported by the stack. It closes the exact number-preserving Fock lift on the full fixed finite lattice, adds an exact common infinite-volume realization of the bond-centered one-particle operator and its second-quantized large-volume lift, sharpens the first local sector-changing coefficient package into an exact disjoint-local $\Delta^6$ exchange and strip-channel theorem, and cleanly separates those results from the still-open general finite-support sector-changing problem and the still-unjustified primitive-kernel infinite-volume Fock theorem. It also isolates the exact future hypothesis package that would be sufficient for that later kernel-level theorem, without claiming that the present stack has yet proved it.

## Conclusion

Phase 8 extends relativistic ISP to variable particle number at the first exact level that the current document stack can genuinely support. For number-preserving quadratic dynamics, variable particle number is not a new stochastic principle. It is the exact direct sum of fixed-particle-number transition laws, together with the sectorwise second-quantized lift of the already-proved bond-centered thin-slab operator on the full fixed finite lattice.

That is exactly the right Barandes-style outcome. The transition law is enlarged, not replaced. The continuum operator is lifted, not reinvented. And the first sector-changing examples are no longer only one-region data: their leading comparison coefficients are exact, their naive $\Delta^4$ two-region defect vanishes on the full finite lattice, their first nonzero disjoint-local $\Delta^6$ coefficient is fixed by universal local exchange kernels, and those kernels now close on an exact finite strip basis in the local classes. On the number-preserving side the large-volume bond-centered operator itself is now already under exact control on a common infinite one-particle space, and its second-quantized lift converges strongly on the natural number-operator domain. The remaining proof burden is therefore sharper rather than vaguer—extend the local sector-changing theorem to general finite supports and prove the genuinely missing primitive-kernel / comparison-map / exchange-defect large-volume limits with the particle-number-uniform control needed for a true infinite-Fock theorem.

## References

1. [1] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
2. [2] Anonymous, “Exact Localized Finite Deformations and the Free Dirac Exchange-Defect Theorem,” preprint (2026).
3. [3] Anonymous, “Exact Leading Support-Level Boundary Law for the Bond-Centered Thin-Slab Program,” preprint (2026).
4. [4] Anonymous, “Restricted Renormalized Universality of the Leading Bond-Centered Thin-Slab Law,” preprint (2026).
5. [5] Anonymous, “Higher Coefficients and Strip-Moment Closure in the Bond-Centered Thin-Slab Law,” preprint (2026).
6. [6] Anonymous, “Broader Regulator Stability Across Support Prototypes,” preprint (2026).
7. [7] Anonymous, “Explicit Higher Coefficients and First Nontrivial Singleton Strip Moments,” preprint (2026).
8. [8] Anonymous, “Explicit Regulator Comparison at the First Non-Leading Singleton Order,” preprint (2026).
9. [9] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
10. [10] J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085 (2023; rev. 2026).
11. [11] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192 (2025).
