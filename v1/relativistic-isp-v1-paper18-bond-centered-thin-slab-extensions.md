# Beyond the Leading Singleton Sector in Relativistic Indivisible Stochastic Processes

Preprint, not peer reviewed, version 2026-05-28.

*Bridge draft on general supports, higher coefficients, Fock-space lift, and a minimal $U(1)$ gauge benchmark for the bond-centered thin-slab law*

Author: Felix Robles Elvira

Bridge draft / roadmap preprint

Date: March 2026

Direct sequel to “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes”

## Abstract

The companion free-model sequel established the first explicit bond-centered thin-slab reduction for relativistic indivisible stochastic processes (ISPs): for the collar-excision rule in the one-particle lattice Dirac model, the leading singleton exchange coefficient has no finite entrywise continuum limit, but after bond-centered spatial renormalization its action on smooth sampled profiles converges to the tangential pseudo-generator
$K_\parallel[\beta] = (\beta\partial_x + \tfrac12\partial_x\beta)(I-\alpha)$.
That result solved only the first case in the agenda stated there. The present document is not a further exact theorem paper. Its role is to separate what is already proved from the next layer of finite-support, higher-coefficient, Fock-space, and gauge-benchmark scaffolding.

The sections below keep the intended order of the program, but they now mark their status explicitly. At leading order we state the finite-support boundary picture as a conjectural extension of the singleton result. For higher coefficients and larger support types we record a conditional theorem under an exact strip-closure hypothesis. For variable particle number we give a formal Fock-space lift conditional on a proved one-particle bond-centered law. For gauge coupling we separate the exact $\Gamma$-level invariance of the primitive slab data from the still-conditional bond-centered continuum action. The point is not to blur roadmap material into theorem-level claims, but to preserve the next targets in the sharpest form currently justified:
$K_\parallel^A[\beta] = (\beta D_x + \tfrac12\partial_x\beta)(I-\alpha)$
with $D_x = \partial_x - iqA_x$. The outcome is a sharper near-term sequence: exact free one-particle exchange-defect results first, then higher coefficients and larger supports, then a genuinely exact Fock-space lift, and only after that the minimal gauge benchmark and broader field-theoretic questions.

Status note. The present file is a bridge draft. Whenever a statement below depends on unproved strip-closure, exact-kernel, or support-level assumptions beyond the established singleton free-model results, it is labeled as a Program, Conjecture, or Conditional Theorem rather than as an unconditional theorem claim.

Update note. The theorem-level completion of phases 2 through 7 now lives in the dedicated phase papers on the leading support-level boundary law, the leading-order restricted universality statement, the higher-order overlap / strip-moment criterion, the broader regulator-stability criterion, the explicit singleton higher-coefficient calculation, and the first non-leading singleton regulator comparison. The remaining material still visible in this bridge draft should therefore be read primarily as scaffolding for later Fock-space and gauge phases rather than as already-completed theorem papers.

## Introduction

The previous relativistic ISP sequel ended with an unusually concrete conclusion. After comparing the Lie-Trotter and collar-excision localized deformation rules in the free one-particle lattice Dirac model, it identified the exact leading singleton exchange algebra, proved that naive site-smearing diverges entrywise in the thin-slab limit, and then showed that the same exchange algebra admits a *bond-centered* renormalization whose action on smooth sampled profiles converges to the tangential pseudo-generator required by Program 1. The final paragraph then named the next agenda in a specific order: extend the bond-centered identification beyond the leading singleton sector, treat general supports and higher coefficients, move to variable particle number, and only after that test gauge coupling.

This paper follows that order exactly. Its role is intermediate rather than final. We do not claim a complete relativistic ISP field theory, and we do not claim a unique physical rule-selection theorem beyond the restricted universality already established in the free-model sequel. What we do claim is that the bond-centered thin-slab law can be organized in a substantially more stable way than the singleton calculation alone might suggest.

There are four intended points. First, for the collar-excision rule the natural leading-order conjecture is that the coefficient $A_R^{(1)}$ for a finite support $R$ is already boundary-driven: at order $\Delta^2$ the mass terms remain invisible and the coefficient should decompose into local deleted-bond contributions together with the diagonal normalization required by column sums. If so, the first nontrivial exchange between disjoint supports is controlled by the bond packets facing the gap rather than by the whole support volume. Second, once one abstracts the exact singleton calculation into a strip-channel language, the higher-coefficient and larger-support problem has a clean conditional form. The right hypothesis is not an entrywise matrix limit but closure of the exact exchange algebra on finitely many strip channels with finite first moments. Under that hypothesis the same bond-centered renormalization produces a first-order tangential operator on smooth sampled profiles.

Third, the fixed-particle-number assumption can be relaxed without changing the essential architecture, but here only at the level of a formal or conditional Fock-space lift. In a fermionic Fock-space lift of the lattice Dirac model, number-preserving quadratic dynamics suggests that the localized deformation maps should decompose sectorwise and that the bond-centered thin-slab operator should simply second quantize. Thus the natural variable-particle-number extension is not a new continuum object but the Fock lift $d\Gamma(K_\parallel)$ of the one-particle tangential generator. Fourth, a minimal-coupling lattice $U(1)$ test can already be posed sharply. At the exact $\Gamma$ level the primitive slab kernels and the resulting exchange defect remain gauge invariant, while the continuum bond-centered action is recorded below only as the benchmark one would want later exact kernel calculations to recover. That is the right first gauge benchmark because it tests genuine gauge structure without yet diffusing the discussion into full field-theoretic constraints.

The paper is organized as follows. Section II recalls only the minimal one-particle background needed from the previous sequel. Section III records the leading-order boundary picture for general finite supports in conjectural form. Section IV states the general strip-closure result as a conditional theorem for higher coefficients and larger support types. Section V gives the corresponding formal Fock-space lift. Section VI introduces the minimal lattice $U(1)$ coupling, keeping the exact primitive-kernel invariance separate from the conditional continuum action. Section VII closes with the sharpened near-term program.

## Minimal background from the one-particle free-model sequel

We work on the same periodic one-dimensional lattice Dirac model as in the preceding sequel. The one-particle Hilbert space is $\H_L=\mathbb{C}^{2L}$ with configuration basis $\{|n,\uparrow\rangle,|n,\downarrow\rangle\}_{n\in\Lambda_L}$, lattice spacing $a$, and free Hamiltonian $H_D = K + M$ with $\alpha=\sigma_x$ and $\beta=\sigma_z$. For a finite support region $R\subset\Lambda_L$, the collar-excision rule uses the bulk Hamiltonian

$$
B_R := H_D - C_R,
$$

where $C_R$ contains the on-site mass terms in $R$ and every kinetic bond incident on $R$. The primitive positive slab kernels are

$$
\Gamma_0(\Delta) := \Gamma(e^{-i\Delta H_D}),
\qquad
\Gamma_R(\Delta) := \Gamma(e^{-i\Delta B_R}),
$$

and the localized algebraic deformation map is

$$
J_R(\Delta) := \Gamma_R(\Delta)\Gamma_0(\Delta)^{-1}.
$$

Whenever the relevant inverses exist one has an expansion

$$
J_R(\Delta)=I+\sum_{k\ge 1}\Delta^{2k}A_R^{(k)}.
$$

For singleton supports $R=\{n\}$, the preceding sequel computed $A_R^{(1)}$ exactly and showed that the leading exchange commutators close on two kinds of strip operators: the bond-flip operators $F_{n+1/2}$ and the two-step strip operators $S_{n,n+2}$. The naive site-smeared density

$$
\mathcal K_a[N] := a\sum_n N_nA_{\{n\}}^{(1)}
$$

does *not* have a finite entrywise continuum commutator. But the bond-centered density

$$
\tau_{n+1/2}^{(a)}
:=
\frac{1}{2a}F_{n+1/2}
+\frac{1}{8a}\bigl(S_{n-1,n+1}+S_{n,n+2}\bigr)
$$

does, in the sense that for
$\beta = N\partial_xM - M\partial_xN$
and smooth compactly supported profiles $\phi=(u,d)$,

$$
[\mathcal K_a[N],\mathcal K_a[M]]\,\iota_a\phi
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a),
\qquad
K_\parallel[\beta]
:=
\Bigl(\beta\partial_x+\frac12\partial_x\beta\Bigr)(I-\alpha).
$$

The rest of the present paper should be read as the systematic extension of that statement.

## General finite supports at leading order: boundary reduction

The first extension is the next exact target at the free-model level. Before discussing higher coefficients, one should understand what the leading collar-excision coefficient $A_R^{(1)}$ ought to look like for a genuine finite support $R$, not just a singleton.

**Definition 1**

(Deleted-bond set).

For a finite region $R\subset\Lambda_L$, let
$$
\partial_1R
:=
\Bigl\{n+\tfrac12:\ \{n,n+1\}\cap R\neq\varnothing\Bigr\}
$$
denote the set of kinetic bonds deleted by collar excision. For each bond $b=n+\tfrac12$, write $Q_b$ for the second-order local kernel coefficient obtained by deleting only that bond from the free Dirac Hamiltonian and comparing with the reference free slab. Thus $Q_b$ is supported on the two adjacent sites and carries the same spin-parity structure as the singleton coefficient.

**Conjecture 1**

(Deleted-bond boundary decomposition for finite supports).

For every finite $R\subset\Lambda_L$, the leading collar-excision coefficient admits the decomposition
$$
A_R^{(1)}
=
\sum_{b\in\partial_1R}Q_b + D_R,
$$
where $D_R$ is diagonal and uniquely determined by column normalization. In particular:

1. the off-diagonal part of $A_R^{(1)}$ depends only on deleted kinetic bonds, not on the deleted mass terms;
2. $A_R^{(1)}$ is supported in the one-step neighborhood $\N_1(R)$;
3. the support-volume dependence of $A_R^{(1)}$ enters through a sum of local bond contributions.

**Motivation.**

Exactly as in the singleton calculation, the second-order off-diagonal coefficient of a kernel $\Gamma(e^{-i\Delta H})$ is $|(H)_{AB}|^2$ for $A\neq B$. Replacing $H_D$ by $B_R$ removes precisely the off-diagonal matrix elements belonging to kinetic bonds incident on $R$; the diagonal mass terms contribute no off-diagonal second-order weight. Hence the off-diagonal part of $A_R^{(1)}$ is the sum over deleted bonds of their local differences, which is precisely $\sum_{b\in\partial_1R}Q_b$. The diagonal part is then fixed by the condition $\one^\top A_R^{(1)}=0$, since $J_R(\Delta)$ is normalization preserving order by order. Support in $\N_1(R)$ is immediate because each $Q_b$ is supported on the two sites adjacent to $b$.

$ \square $

Conjecture 1 captures how one should try to think about finite supports. If it is correct, then the leading coefficient is not an indivisible “blob” attached to $R$; it is a finite sum of boundary-local deleted-bond pieces plus the diagonal bookkeeping needed for normalization.

**Definition 2**

(Boundary-facing bond packet).

Let $R,S\subset\Lambda_L$ be disjoint finite intervals. A deleted bond $b\in\partial_1R$ is

*facing $S$*

if its midpoint lies on a shortest lattice path from $R$ to $S$. Denote by
$$
\mathcal B_{R\to S}
\subset
\partial_1R
$$
the set of deleted bonds in $R$ facing $S$, and define the associated packet
$$
\mathcal Q_{R\to S}
:=
\sum_{b\in\mathcal B_{R\to S}}Q_b.
$$
Similarly define $\mathcal Q_{S\to R}$.

**Conjecture 2**

(Boundary reduction at the first exchange order).

Let $R,S\subset\Lambda_L$ be disjoint finite intervals. Then
$$
[A_R^{(1)},A_S^{(1)}]
=
[\mathcal Q_{R\to S},\mathcal Q_{S\to R}] + \mathcal R_{R,S},
$$
where every term in the remainder $\mathcal R_{R,S}$ is supported on strips whose minimal distance from the gap between $R$ and $S$ is strictly larger than the first meeting strip of the two supports. Equivalently, the first nontrivial exchange channel is completely determined by the boundary-facing bond packets.

**Heuristic reduction.**

Expand both leading coefficients using Conjecture 1:
$$
[A_R^{(1)},A_S^{(1)}]
=
\sum_{b\in\partial_1R}\sum_{c\in\partial_1S}[Q_b,Q_c]
+\sum_{b\in\partial_1R}[Q_b,D_S]
+\sum_{c\in\partial_1S}[D_R,Q_c].
$$
The diagonal terms may shift local coefficients but cannot create a new overlap strip before a bond term does. Each bond commutator $[Q_b,Q_c]$ vanishes unless the one-step neighborhoods of $b$ and $c$ intersect or are connected by the minimal strip carrying the first exchange channel. Interior deleted bonds of $R$ lie farther from $S$ than the boundary-facing bonds, so any commutator involving them contributes only on a thicker strip. Therefore the first strip on which the exchange can appear is produced entirely by the bond packets facing the gap, which is the claimed reduction.

$ \square $

**Program 1**

(Leading-order finite-support bond-centered law).

Fix prototype finite intervals $R_\ast,S_\ast\subset\mathbb Z$ and write their translates on the lattice as $R_n:=n+R_\ast$, $S_n:=n+S_\ast$. Define
$$
\mathcal K_{a,R_\ast}[N]
:=
a\sum_n N_n A_{R_n}^{(1)},
\qquad
\mathcal K_{a,S_\ast}[M]
:=
a\sum_n M_n A_{S_n}^{(1)}.
$$
Then there exists a bond-centered density $\mathcal T_{a;R_\ast,S_\ast}[\beta]$, built from the translated commutators of the boundary-facing packets, such that for every smooth compactly supported two-component profile $\phi$,
$$
[\mathcal K_{a,R_\ast}[N],\mathcal K_{a,S_\ast}[M]]\,\iota_a\phi
=
\mathcal T_{a;R_\ast,S_\ast}[\beta]\iota_a\phi + O(a),
$$
where $\beta=N\partial_xM-M\partial_xN$. Moreover
$$
\mathcal T_{a;R_\ast,S_\ast}[\beta]\iota_a\phi
=
\iota_a\bigl(K_{\parallel;R_\ast,S_\ast}[\beta]\phi\bigr)+O(a),
$$
for a first-order tangential operator of the form
$$
K_{\parallel;R_\ast,S_\ast}[\beta]
=
\Bigl(\beta\partial_x+\frac12\partial_x\beta\Bigr)\Xi_{R_\ast,S_\ast},
$$
with $\Xi_{R_\ast,S_\ast}$ determined by the strip moments of the boundary packets. For singleton prototypes, $\Xi_{R_\ast,S_\ast}=I-\alpha$, recovering the earlier theorem.

**Why this should follow.**

By Conjecture 2, the leading translated commutator can be replaced up to thicker-strip errors by the commutator of the boundary-facing packets. Translation covariance makes that commutator depend only on relative displacement. Antisymmetrizing the smeared sum gives
$$
[\mathcal K_{a,R_\ast}[N],\mathcal K_{a,S_\ast}[M]]
=
a^2\sum_{n,r}\bigl(N_nM_{n+r}-N_{n+r}M_n\bigr)\,\mathcal X_r + O(a),
$$
for finitely many translated strip operators $\mathcal X_r$. Smoothness gives
$$
N_nM_{n+r}-N_{n+r}M_n
=
ar\,\beta(x_{n+r/2})+O(a^2).
$$
The finite first moments of the active strip coefficients therefore produce a bond-centered density depending on $\beta$ at strip midpoints, and the same midpoint-Taylor argument as in the singleton case turns that density into a first-order tangential operator acting on smooth sampled profiles. The singleton result is the special case in which only the bond-flip and two-step strip channels are active.

$ \square $

Remark.

Program 1 is the conceptual extension of the singleton result. What matters is not the support volume of $R$ and $S$ but the strip moments of the boundary data that survive after antisymmetrization. The natural finite-support generalization of the bond-centered law should therefore still be a boundary law.

## Higher coefficients and larger support types: the strip-closure theorem

Beyond leading order the right framework is slightly more abstract. The previous sequel explicitly computed the first singleton coefficient and its exchange algebra. For higher coefficients or more general support shapes, the decisive question is whether the exact coefficient algebra closes on finitely many strip channels with controllable moments.

**Definition 3**

(Translated coefficient families).

Let $\sigma$ label a support type (for example a singleton, an interval of fixed width, or a finite union of local cells). For each order $p\ge 1$, let $A_{\sigma,n}^{(p)}$ denote the order-$\Delta^{2p}$ coefficient appearing in the localized comparison map attached to the translate of type $\sigma$ centered at lattice site $n$. Define the corresponding smeared operator by
$$
\mathcal K_{\sigma,a}^{(p)}[N]
:=
a\sum_n N_nA_{\sigma,n}^{(p)}.
$$

**Definition 4**

(Bond-centered admissible strip channels).

Suppose that for each active channel label $(\ell,\chi)$ there is a translated antisymmetric strip operator family $X_{n+1/2}^{(\ell,\chi)}$ and a corresponding smeared bond-centered density $\mathcal T_a^{(\ell,\chi)}[\beta]$ such that for every smooth compactly supported profile $\phi$,
$$
\mathcal T_a^{(\ell,\chi)}[\beta]\iota_a\phi
=
\iota_a\bigl(K_{\ell,\chi}[\beta]\phi\bigr)+O(a),
$$
with $K_{\ell,\chi}[\beta]$ first-order in derivatives and local in $\beta$. Call such a family

*bond-centered admissible*

.

**Hypothesis 1**

(Exact strip closure with finite first moments).

Fix support types $\sigma,\tau$ and orders $p,q$. Assume:

1. *strip closure:* $$
  [A_{\sigma,n}^{(p)},A_{\tau,m}^{(q)}]
  =
  \sum_{(\ell,\chi)} c_{\sigma,\tau}^{(p,q;\ell,\chi)}(m-n)\,
  X_{n+1/2}^{(\ell,\chi)},
  $$
  for finitely many strip channels $(\ell,\chi)$ and finitely supported coefficient functions $c_{\sigma,\tau}^{(p,q;\ell,\chi)}$;
2. *antisymmetry:* $c_{\sigma,\tau}^{(p,q;\ell,\chi)}(r) = -c_{\tau,\sigma}^{(q,p;\ell,\chi)}(-r)$;
3. *finite first moments:* $$
  C_{\sigma,\tau}^{(p,q;\ell,\chi)}
  :=
  \sum_r r\,c_{\sigma,\tau}^{(p,q;\ell,\chi)}(r)
  $$
  exist for all active channels.

**Conditional Theorem 2**

(General bond-centered thin-slab reduction under strip closure).

Assume Hypothesis 1, and assume moreover that each active strip channel is bond-centered admissible in the sense of Definition 4. Then for every smooth compactly supported two-component profile $\phi$ one has
$$
[\mathcal K_{\sigma,a}^{(p)}[N],\mathcal K_{\tau,a}^{(q)}[M]]\,\iota_a\phi
=
\sum_{(\ell,\chi)}
C_{\sigma,\tau}^{(p,q;\ell,\chi)}
\mathcal T_a^{(\ell,\chi)}[\beta]\iota_a\phi
+O(a),
$$
with $\beta=N\partial_xM-M\partial_xN$. Consequently,
$$
[\mathcal K_{\sigma,a}^{(p)}[N],\mathcal K_{\tau,a}^{(q)}[M]]\,\iota_a\phi
=
\iota_a\bigl(K_{\parallel;\sigma,\tau}^{(p,q)}[\beta]\phi\bigr)+O(a),
$$
where
$$
K_{\parallel;\sigma,\tau}^{(p,q)}[\beta]
:=
\sum_{(\ell,\chi)}
C_{\sigma,\tau}^{(p,q;\ell,\chi)}K_{\ell,\chi}[\beta].
$$
Thus every coefficient pair with strip closure and finite first moments has the same bond-centered continuum form: an antisymmetrized first-order tangential operator controlled by strip moments.

Proof.

Start from
$$
[\mathcal K_{\sigma,a}^{(p)}[N],\mathcal K_{\tau,a}^{(q)}[M]]
=
a^2\sum_{n,m}N_nM_m[A_{\sigma,n}^{(p)},A_{\tau,m}^{(q)}].
$$
Insert the strip-closure expansion from Hypothesis 1 and set $r=m-n$:
$$
=
a^2\sum_{n,r}
N_nM_{n+r}
\sum_{(\ell,\chi)}
c_{\sigma,\tau}^{(p,q;\ell,\chi)}(r)\,X_{n+1/2}^{(\ell,\chi)}.
$$
Antisymmetrizing under $(n,\sigma,p)\leftrightarrow(n+r,\tau,q)$ replaces $N_nM_{n+r}$ by
$N_nM_{n+r}-N_{n+r}M_n$.
Smoothness gives
$$
N_nM_{n+r}-N_{n+r}M_n
=
ar\,\beta(x_{n+r/2})+O(a^2),
$$
uniformly on the finite set of active displacements. Summing over $r$ therefore produces precisely the first moments $C_{\sigma,\tau}^{(p,q;\ell,\chi)}$ multiplying the bond-centered admissible strip densities. The assumed profile-action limit of each strip density then yields the final continuum operator.

$ \square $

**Conditional Corollary 1**

(Singleton theorem as the first strip-closure case).

The leading singleton collar-excision theorem of the previous sequel is the special case of Theorem 2 in which

1. $\sigma=\tau=$ singleton,
2. $p=q=1$,
3. the only active strip channels are the bond-flip and two-step strip families, and
4. their bond-centered admissible combination yields $K_\parallel[\beta] = (\beta\partial_x+\tfrac12\partial_x\beta)(I-\alpha)$.

Remark.

Conditional Theorem 2 is deliberately formulated at the coefficient algebra level rather than the kernel-entry level. This is exactly the lesson of the previous sequel: the naive entrywise continuum limit is too rigid. The object with a stable continuum meaning is the bond-centered action of the exchange algebra on smooth sampled profiles.

## Variable particle number: Fock-space lift of the bond-centered law

The next requested extension is variable particle number. The clean first step is the fermionic Fock lift of the one-particle lattice Dirac model.

**Definition 5**

(Fermionic Fock-space ISP lift).

Let
$$
\F_L
:=
\bigoplus_{N=0}^{2L}\Lambda^N\H_L
$$
be the finite-lattice fermionic Fock space. For a number-preserving quadratic Hamiltonian
$$
\widehat H = \sum_{A,B\in\C_L} h_{AB}\,c_A^\dagger c_B,
$$
write $\widehat U(\Delta)=e^{-i\Delta\widehat H}$ and denote its restriction to the $N$-particle sector by $\widehat U^{(N)}(\Delta)$. The corresponding primitive kernels are
$$
\Gamma_0^{(N)}(\Delta)
:=
\Gamma(\widehat U^{(N)}(\Delta)),
\qquad
\Gamma_R^{(N)}(\Delta)
:=
\Gamma(\widehat U_R^{(N)}(\Delta)),
$$
with comparison maps
$$
J_R^{(N)}(\Delta)
:=
\Gamma_R^{(N)}(\Delta)\bigl[\Gamma_0^{(N)}(\Delta)\bigr]^{-1}.
$$

Because the dynamics is quadratic and number preserving, the sectors decouple exactly. Variable particle number therefore appears as a direct sum of fixed-$N$ problems rather than as a new algebraic obstruction.

**Conditional Theorem 3**

(Formal sectorwise bond-centered thin-slab lift to Fock space).

Assume the one-particle bond-centered density $\mathcal T_a[\beta]$ satisfies
$$
\mathcal T_a[\beta]\iota_a\phi
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a)
$$
for smooth compactly supported one-particle profiles. Define its fermionic second quantization on $\F_L$ by
$$
d\Gamma(\mathcal T_a[\beta])\big|_{\Lambda^N\H_L}
:=
\sum_{j=1}^N
I^{\wedge(j-1)}\wedge\mathcal T_a[\beta]\wedge I^{\wedge(N-j)},
$$
and similarly for $d\Gamma(K_\parallel[\beta])$. Then for every finite-particle smooth antisymmetrized sampled profile $\Psi$,
$$
d\Gamma(\mathcal T_a[\beta])\,\iota_a^\F\Psi
=
\iota_a^\F\bigl(d\Gamma(K_\parallel[\beta])\Psi\bigr)+O(a),
$$
uniformly on finite particle-number truncations. In particular, the variable-particle-number tangential generator for number-preserving quadratic dynamics is
$$
K_{\parallel,\F}[\beta]
=
d\Gamma(K_\parallel[\beta]).
$$

Proof.

Fix an $N$-particle sector. On antisymmetrized tensors of smooth one-particle profiles, $d\Gamma(\mathcal T_a[\beta])$ is the sum of $N$ copies of the one-particle operator acting in each slot. The one-particle convergence assumption therefore gives the same $O(a)$ estimate in each slot, and finite $N$ preserves the order of the error. Antisymmetrization commutes with applying the same one-body operator in each slot, so the resulting limit on $\Lambda^N\H_L$ is $d\Gamma(K_\parallel[\beta])$. Direct-summing over sectors gives the Fock-space statement for finite-particle states.

$ \square $

**Conditional Corollary 2**

(Variable particle number without new continuum kinematics).

For any state in a finite superposition of particle-number sectors, the bond-centered thin-slab law is obtained by applying the same one-particle tangential generator in each occupied slot and summing over sectors. Thus the first variable-particle-number extension is kinematically conservative: no new continuum operator is required beyond second quantization.

**Remark on genuine number-changing dynamics.**

If one adds localized source, sink, detector, or pair-creation terms, the Fock-space comparison map acquires off-diagonal blocks
$A_R^{(p;N\to N\pm1)}$ or
$A_R^{(p;N\to N\pm2)}$.
Conditional Theorem 3 then no longer applies literally, but Conditional Theorem 2 still gives the right template on any finite Fock truncation: if those off-diagonal blocks satisfy the same strip-closure and finite-moment hypotheses, the exchange algebra again reduces to a bond-centered tangential law, now with local creation/annihilation insertions on the exchange strip. Deriving those exact coefficients is the natural next step beyond the present conservative Fock lift.

## Minimal $U(1)$ gauge coupling test

Only after the support and Fock-space extensions are in place is it sensible to test gauge coupling. The minimal benchmark is static lattice $U(1)$ coupling through Peierls phases on the Dirac kinetic bonds.

**Definition 6**

(Lattice minimal coupling).

Let $A_{n+1/2}$ be a real link field and $q$ a charge. Define the link variable
$$
U_{n+1/2}:=e^{-iqaA_{n+1/2}}.
$$
The minimally coupled lattice Dirac Hamiltonian is
$$
H_D[A]
=
m\sum_n\beta_n
-\frac{i}{2a}\sum_{n,s}
\Bigl(
U_{n+1/2}\,|n+1,\bar s\rangle\langle n,s|
-U_{n+1/2}^{-1}\,|n,s\rangle\langle n+1,\bar s|
\Bigr).
$$
For a support region $R$, define the coupled collar Hamiltonian $C_R[A]$ by replacing each free kinetic bond in $C_R$ with its minimally coupled version, and set $B_R[A]:=H_D[A]-C_R[A]$.

**Definition 7**

(Local lattice gauge transformation).

For a site phase function $\chi_n$, let
$$
G_\chi|n,s\rangle := e^{iq\chi_n}|n,s\rangle,
$$
and transform the link field by
$$
A_{n+1/2}\longmapsto A_{n+1/2}^\chi
:=
A_{n+1/2}+\frac{\chi_{n+1}-\chi_n}{a}.
$$
Equivalently, $U_{n+1/2}\mapsto U_{n+1/2}^\chi=e^{-iq\chi_{n+1}}U_{n+1/2}e^{iq\chi_n}$.

**Proposition 3**

($\Gamma$-level gauge invariance of the primitive slab data).

Under the gauge transformation of Definition 7 one has
$$
H_D[A^\chi]=G_\chi H_D[A]G_\chi^{-1},
\qquad
B_R[A^\chi]=G_\chi B_R[A]G_\chi^{-1}.
$$
Consequently,
$$
\Gamma_0[A^\chi](\Delta)=\Gamma_0[A](\Delta),
\qquad
\Gamma_R[A^\chi](\Delta)=\Gamma_R[A](\Delta),
$$
and therefore
$$
J_R[A^\chi](\Delta)=J_R[A](\Delta),
\qquad
E_{R,S}[A^\chi](\Delta)=E_{R,S}[A](\Delta).
$$

Proof.

The first identities are the standard Peierls-covariance statements. Exponentiating gives
$$
e^{-i\Delta H_D[A^\chi]}
=
G_\chi e^{-i\Delta H_D[A]}G_\chi^{-1},
\qquad
e^{-i\Delta B_R[A^\chi]}
=
G_\chi e^{-i\Delta B_R[A]}G_\chi^{-1}.
$$
In the configuration basis,
$$
\bigl(G_\chi U G_\chi^{-1}\bigr)_{AB}
=
e^{iq(\chi_A-\chi_B)}U_{AB},
$$
so the entrywise moduli are unchanged:
$|(G_\chi U G_\chi^{-1})_{AB}|^2=|U_{AB}|^2$.
Hence the primitive kernels are invariant. Since $J_R$ and $E_{R,S}$ are built algebraically from those kernels, they are invariant as well.

$ \square $

So the gauge test passes at the exact $\Gamma$ level before any continuum limit is taken. The remaining question is what bond-centered continuum operator the gauge-coupled exchange algebra selects.

**Definition 8**

(Gauge-coupled strip operators and bond-centered density).

Define the gauge-coupled bond-flip and two-step strip operators by
$$
F_{n+1/2}^A
:=
\sum_{s}
\Bigl(
U_{n+1/2}|n+1,\bar s\rangle\langle n,s|
-U_{n+1/2}^{-1}|n,s\rangle\langle n+1,\bar s|
\Bigr),
$$
$$
S_{n,n+2}^A
:=
\sum_s
\Bigl(
U_{n+1/2}U_{n+3/2}|n+2,s\rangle\langle n,s|
-U_{n+1/2}^{-1}U_{n+3/2}^{-1}|n,s\rangle\langle n+2,s|
\Bigr).
$$
The gauge-coupled bond-centered density is
$$
\tau_{n+1/2}^{A,(a)}
:=
\frac{1}{2a}F_{n+1/2}^A
+\frac{1}{8a}\bigl(S_{n-1,n+1}^A+S_{n,n+2}^A\bigr),
$$
and its smeared operator is
$$
\mathcal T_a^A[\beta]
:=
\sum_n \beta_{n+1/2}\tau_{n+1/2}^{A,(a)}.
$$

**Conditional Proposition 4**

(Gauge-covariant bond-centered continuum action).

Assume that the gauge-coupled leading exchange algebra is generated, at the same strip level as in the free case, by the operators of Definition 8. Let $\phi=(u,d)\in C_c^\infty(\mathbb R,\mathbb C^2)$ and sample it on the lattice as before. If the continuum gauge potential $A_x$ is sampled at bond midpoints, then
$$
\mathcal T_a^A[\beta]\iota_a\phi
=
\iota_a\bigl(K_\parallel^A[\beta]\phi\bigr)+O(a^2)
$$
uniformly on compact sets, where
$$
K_\parallel^A[\beta]
:=
\Bigl(\beta D_x+\frac12\partial_x\beta\Bigr)(I-\alpha),
\qquad
D_x:=\partial_x-iqA_x.
$$

**Formal derivation.**

Expand the link phases at bond midpoints:
$$
U_{n+1/2}=e^{-iqaA_{n+1/2}}=1-iqaA_{n+1/2}+O(a^2).
$$
The bond-flip part of $\mathcal T_a^A[\beta]$ therefore contains one-step covariant differences such as
$$
\frac{\beta_{n-1/2}}{2a}U_{n-1/2}^{-1}d_{n-1}
\,-\,
\frac{\beta_{n+1/2}}{2a}U_{n+1/2}d_{n+1},
$$
which are precisely the midpoint discretization of
$-(\beta D_x+\tfrac12\partial_x\beta)d(x_n)$
up to $O(a^2)$. The two-step strip terms supply the corresponding same-spin covariant centered difference:
$$
\frac{\beta_{n+1/2}+\beta_{n+3/2}}{8a}\,U_{n+1/2}U_{n+3/2}\,u_{n+2}
\,-\,
\frac{\beta_{n-3/2}+\beta_{n-1/2}}{8a}\,U_{n-3/2}^{-1}U_{n-1/2}^{-1}\,u_{n-2},
$$
which is the midpoint discretization of
$(\beta D_x+\tfrac12\partial_x\beta)u(x_n)$
up to $O(a^2)$. Combining the same-spin and opposite-spin pieces gives exactly the matrix action of $(I-\alpha)$, as in the free case, now with $\partial_x$ replaced by the gauge-covariant derivative $D_x$.

$ \square $

**Conditional Corollary 3**

(Continuum gauge covariance).

Under the continuum gauge transformation
$$
\phi\longmapsto e^{iq\chi}\phi,
\qquad
A_x\longmapsto A_x+\partial_x\chi,
$$
one has
$$
K_\parallel^{A+\partial_x\chi}[\beta](e^{iq\chi}\phi)
=
e^{iq\chi}K_\parallel^A[\beta]\phi.
$$
Hence the bond-centered tangential operator obtained from the lattice exchange law passes the minimal gauge-coupling covariance test.

**Immediate consequence.**

This is the standard covariance of $D_x=\partial_x-iqA_x$ under local phase rotations. Since $\beta$ is a scalar profile built from the deformation smearing functions rather than the charged matter field, the prefactor $\beta\partial_x+\tfrac12\partial_x\beta$ transforms exactly as claimed.

$ \square $

**Remark (Aharonov–Bohm benchmark).**

On a periodic ring the local gauge field can be gauged away on any contractible patch, so the local profile action of $K_\parallel^A[\beta]$ is gauge-equivalent to the free one there. The nontrivial global datum is the holonomy
$$
e^{-iq\Phi},
\qquad
\Phi:=\oint A_x\,dx.
$$
That makes the static ring with nonzero flux the right first numerical gauge benchmark for the finite-slab exchange law: locally the bond-centered algebra should look free, while globally the flux should survive through holonomy-dependent boundary phases.

## Conclusion

The previous sequel fixed the singleton free-model core, and the dedicated phase papers have now carried that exact program through the first non-leading singleton higher-order calculation and the first non-leading regulator comparison. The present bridge draft should therefore no longer be read as a repository of unresolved higher-coefficient or broader regulator-comparison burdens. Its real remaining role is to organize what comes after phase 7 without silently promoting later ontology-expanding steps to theorem status.

The variable-particle-number and gauge sections are therefore the central live scaffold here. The Fock-space section records the formal consequence of a proved one-particle bond-centered law for number-preserving quadratic dynamics. The gauge section separates one exact point—the $\Gamma$-level gauge invariance of the primitive slab data—from the still-conditional bond-centered continuum action.

Read this file, then, as a sharpened program document for the later phases beyond the now-completed phase-7 scope: it preserves the Fock-space and gauge questions in the form in which they should be attacked, while leaving the exact higher-coefficient and regulator-comparison results to the dedicated phase papers.

The resulting near-term program is now sharper than before.

**Program 2**

(Near-term sequence).

1. *Variable particle number.* Extend the present Fock lift from number-preserving quadratic dynamics to localized sector-changing couplings.
2. *Gauge benchmark.* Test the ring-holonomy/Aharonov–Bohm case directly at the finite-slab kernel level.
3. *Operational completion.* Add localized controls and detectors only after the preceding algebraic sectors are under control.
4. *Only then full field-theoretic generalization.* The next serious relativistic questions about non-Abelian gauge fields or gravity should come only after the preceding three items are under control.

So the bond-centered thin-slab law no longer looks like a singleton curiosity. Its exact theorem-level scope now includes the leading support-level law, the leading-order universality theorem, the higher-order structural criterion, the broader regulator-stability criterion, the first explicit singleton higher-order coefficient, and the first explicit non-leading singleton regulator comparison. The remaining Fock-space and gauge sections are benchmarks for later exact papers rather than finished endpoints.

## References

1. [1] Anonymous, “Toward Lorentz-Covariant Indivisible Stochastic Processes: Spatial Locality, Temporal Indivisibility, and Localized Finite Deformations,” preprint (2026).
2. [2] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
3. [3] Anonymous, “Entropy Structure of Indivisible Stochastic Processes: Gauge Invariance, Coherence, and Thermodynamic Interpretation,” companion preprint (2026).
4. [4] Anonymous, “Gauge-Invariant Process Entanglement in Indivisible Stochastic Processes: From ZZ-Gate Phantoms to Bell Inequalities,” companion preprint (2026).
5. [5] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
6. [6] J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085 (2023; rev. 2026).
7. [7] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192 (2025).
