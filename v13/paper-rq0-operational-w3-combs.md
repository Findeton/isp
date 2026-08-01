# Operational W3 Combs

## Complete Instruments, Tester-Visible Coherence, and Contextual Quantum Seams

**Version:** v0.1

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-01

**Governing pin:** `3c958da`

**Scope:** finite-dimensional, exact, analytical RQ0-L0

---

## Abstract

A stable quantum record is not determined by a state, a projector, a channel,
or an isolated complex amplitude. It is a multi-stage experiment. Its source
has outcome-conditioned completely positive branches; its writing operation
creates a candidate classical interface; its continuation may preserve or
recover coherence; and its final readout has both probabilities and
disturbance semantics. This paper represents that entire experiment as a
finite quantum comb with a continuation slot.

For each comb type, a candidate-independent admitted family of complete
testers defines the seminorm

$$
\|X\|_{\mathsf{Test}_D}
=
\sup_{\mathbf T\in\mathsf{Test}_D}
\sum_t|\operatorname{Tr}(T_tX)|.
$$

The physical operational quotient is taken before any record criterion.
Record preservation means that inserting record dephasing changes no
admitted complete-tester probability. Coherent recovery means that some
admitted complete tester sees a positive probability contrast. The resulting
recoverable process coherence is

$$
\mathcal C_R(W;E)
=
\|E\star(W-\mathcal D_R\star W)\|_{\mathsf{Test}_D}.
$$

This rule rejects an exact four-level false eraser whose individual complex
cross term is nonzero but whose entire admitted probability law is unchanged.
It accepts a phase-aligned eraser with exact tester distance $1/2$. It also
separates instruments with the same POVM but different disturbance and source
instruments with the same normalized branch states but different weights.

At a fixed terminal readout law, all nine previously identified
branch-memory candidates remain operational W3 candidates. Their recovered
coherences are not equal: the six $2+1+1$ candidates have value $5/4$, while
the three $2+2$ candidates have value $1$. No preferred candidate is selected.

The assignment “W3-valid seams in a tester context” is not a presheaf:
preservation restricts, but an existential eraser witness can disappear.
Instead we construct a finite tester-context site, a sheaf of complete
tester-evaluation data, and its retained-symmetry quotient stack. W3 seams are
a chart-complete locus of physically realized sections over one chart's
tester site. A favorable singleton test is only partial evidence and cannot
become a chart-complete seam without extension to that chart's jointly
separating master context.

The strongest provisional result is

$$
\boxed{\texttt{RQ0-L0-W3-TEST-SHEAF}}
$$

at a finite, definite-order, law-relative tester scope. This result constructs
neither an actual outcome nor fact co-reference, spatial localization,
topology, causality, fields, or gravity.

---

## 1. Question and claim boundary

### 1.1 The physical question

Consider a declared sequence of laboratory ports

$$
\text{source instrument}
\longrightarrow
\text{write operation}
\longrightarrow
\text{continuation slot}
\longrightarrow
\text{output instrument and tail tester}.
$$

The question is:

> When does this complete interactive quantum process contain a stable record
> interface that is operationally classical under a preserving continuation
> but whose coherence can be recovered by another admitted continuation?

The answer must use complete closed-experiment probabilities. A selected
matrix entry is not a physical witness unless an admitted tester converts it
into an outcome-probability difference.

### 1.2 What is primitive in this paper

The declared process law supplies:

1. finite-dimensional typed input and output wires;
2. complete source, continuation, and output CP instruments;
3. the write and no-write operations;
4. a candidate sharp record action at one declared laboratory cut;
5. a candidate-independent admitted family of complete testers; and
6. presentation gauge and physical-symmetry actions.

The paper derives operational equivalence, preservation, recovered coherence,
the exact candidate classification in its benchmarks, and tester-context
descent from those data.

It does **not** derive the cut, the tester law, or the candidate record action
from a bare Hamiltonian. It therefore constructs a complete operational W3
object, not yet an intrinsic localization theorem.

### 1.3 One-chart locality firewall

Every object in this paper belongs to one finite operational chart $D$.
$\mathsf{Test}_D$, its master context $A_D$, and every probability table close
only the ports of that chart. “Complete” means complete relative to the
admitted experimental law of $D$. It never means one tester family spanning
an atlas of charts.

Likewise, the sheaf-theoretic phrase “global section” below means a section
over the terminal tester context $A_D$ **inside this one chart's tester
site**. It does not mean a global event set, an atlas-wide state, or a
simultaneous readout of several regions. Cross-chart fact comparison still
requires separately supplied physical maps and the independent co-reference
discipline. No such map is constructed here.

### 1.4 Definite laboratory order is not spacetime causality

The wire order of a comb is the declared order in which laboratory devices
are connected. It supplies the typing needed to compose experiments. It is
not an emergent causal order, a global time, a metric, or a foliation.
Indefinite-order process matrices lie outside the present first scope.

### 1.5 Registered cumulative outcomes

The only provisional positive outcomes used here are

$$
\begin{aligned}
&\texttt{RQ0-L0-COMB-COMPLETE-W3},\\
&\texttt{RQ0-L0-TESTER-SEPARATED-W3},\\
&\texttt{RQ0-L0-W3-TEST-SHEAF}.
\end{aligned}
$$

They are cumulative and remain unreviewed until the prescribed independent
hostile rounds are frozen and jointly adjudicated.

---

## 2. Finite comb convention

### 2.1 Choi operators

For a linear map

$$
\Phi:\mathcal L(H_X)\longrightarrow\mathcal L(H_Y),
$$

fix an orthonormal basis of $H_X$ and define

$$
J(\Phi)
=
\sum_{m,n}|m\rangle\langle n|_X
\otimes
\Phi(|m\rangle\langle n|)_Y.
$$

Thus the input factor precedes the output factor. The map is CP precisely
when $J(\Phi)\geq0$, and it is trace preserving precisely when

$$
\operatorname{Tr}_YJ(\Phi)=I_X.
$$

All basis changes below transform process operators and testers together.
The resulting closed probabilities are basis independent.

### 2.2 Deterministic and probabilistic combs

Let an $N$-comb type be the ordered wire profile

$$
\tau=(H_0,H_1,\ldots,H_{2N-2},H_{2N-1}),
$$

where $H_{2j}$ is the input and $H_{2j+1}$ the output of the $j$th slot.
A deterministic $N$-comb is a positive operator $C^{(N)}$ on
$\bigotimes_{j=0}^{2N-1}H_j$ for which there are positive operators
$C^{(n)}$ satisfying

$$
\operatorname{Tr}_{2n-1}C^{(n)}
=
I_{2n-2}\otimes C^{(n-1)},
\qquad 2\leq n\leq N,
$$

and

$$
\operatorname{Tr}_{1}C^{(1)}=I_0,
\qquad C^{(0)}=1.
$$

A probabilistic comb is a positive process operator that is a summand of a
deterministic comb. A finite comb instrument

$$
\boldsymbol{\mathcal I}=(C_i)_{i\in\Omega}
$$

is a finite family of probabilistic combs whose sum is deterministic. Both
the classical outcome $i$ and the output quantum wire remain part of the
instrument. Replacing the family by its sum, normalized conditional states,
or outcome effects is a shadow operation.

### 2.3 Link product

When an output wire $Y$ of an operator $A$ is connected to an input wire $Y$
of an operator $B$, define the link product in the fixed Choi convention by

$$
B\star_Y A
=
\operatorname{Tr}_Y
\left[
\left(A^{T_Y}\otimes I\right)
\left(I\otimes B\right)
\right],
$$

with untouched tensor factors ordered by their labels. For Choi operators of
channels this is the Choi operator of ordinary channel composition. Link
products on disjoint wires associate; every expression below is required to
match input and output types before it is formed.

### 2.4 Complete testers and generalized Born probabilities

A complete tester for type $\tau$ is a finite family

$$
\mathbf T=(T_t)_{t\in\Lambda}
$$

of positive dual process operators obtained by closing every open wire of a
$\tau$-comb with an admitted source, memory, adaptive control, and terminal
readout network. Its normalization is defined operationally by

$$
\sum_t\operatorname{Tr}(T_tC)=1
$$

for every deterministic $\tau$-comb $C$. Equivalently, its sum obeys the
dual comb-normalization recursion. For a deterministic comb $C$,

$$
p_{\mathbf T}(C)_t=\operatorname{Tr}(T_tC)
$$

is the generalized Born probability vector.

This definition includes testers with retained classical outcomes, ancillas,
quantum memory, and adaptive tail operations whenever the declared law admits
them. It also includes a trivial deterministic tester.

The comb, tester, link-product, and generalized-instrument formalism used in
this section is the finite-dimensional quantum-network formalism of
Chiribella, D'Ariano, and Perinotti [1]. Interactive strategy norms and their
tester interpretation are developed independently in [2,3].

---

## 3. The admitted tester quotient

### Definition 3.1 — law-relative tester family

For each process type $\tau$, fix before inspecting a record candidate a
family

$$
\mathsf{Test}_D(\tau)
$$

of complete admitted testers. It is closed under the classical
postprocessings and refinements used below. Whenever an admitted deterministic
supermap $S:\tau\to\tau'$ is used, the family also obeys the pullback rule

$$
\mathbf T\in\mathsf{Test}_D(\tau')
\quad\Longrightarrow\quad
S^*\mathbf T\in\mathsf{Test}_D(\tau).
$$

This is a physical closure postulate about the available experiments. “All
testers” below means this family, not every mathematically possible tester
unless complete tomography is explicitly declared.

### Definition 3.2 — tester seminorm and operational quotient

For a Hermitian operator $X$ in the real linear span of same-type combs,
define

$$
\boxed{
\|X\|_{\mathsf{Test}_D}
=
\sup_{\mathbf T\in\mathsf{Test}_D(\tau)}
\sum_{t\in\Lambda_{\mathbf T}}
|\operatorname{Tr}(T_tX)|.
}
$$

For deterministic combs $C,C'$ of type $\tau$, write

$$
C\simeq_{\mathrm{op}}C'
\quad\Longleftrightarrow\quad
\|C-C'\|_{\mathsf{Test}_D}=0.
$$

The conventional factor $1/2$ used when quoting discrimination advantage is
not included here.

### Proposition 3.3 — seminorm and separation

The displayed function is a seminorm. Moreover,

$$
\|C-C'\|_{\mathsf{Test}_D}=0
\quad\Longleftrightarrow\quad
p_{\mathbf T}(C)=p_{\mathbf T}(C')
\quad\forall\mathbf T\in\mathsf{Test}_D.
$$

*Proof.* For each fixed tester, the sum of absolute values of real linear
functionals is a seminorm. A supremum of seminorms is a seminorm, giving
nonnegativity, absolute homogeneity, symmetry, and the triangle inequality.
The value is zero precisely when each summand is zero for every admitted
tester outcome. $\square$

### Proposition 3.4 — congruence and contraction

Let $S:\tau\to\tau'$ be an admitted deterministic supermap satisfying the
tester pullback rule. Then

$$
\|S(X)\|_{\mathsf{Test}_D(\tau')}
\leq
\|X\|_{\mathsf{Test}_D(\tau)}.
$$

Consequently $\simeq_{\mathrm{op}}$ is a congruence for every admitted link
composition used in this paper.

*Proof.* For every downstream tester $\mathbf T$,

$$
p_{\mathbf T}(S(X))=p_{S^*\mathbf T}(X).
$$

The pullback is admitted, so its $\ell^1$ value is bounded by the supremum on
the right. Taking the downstream supremum proves the claim. Plugging a fixed
deterministic comb into an open slot is such a supermap. $\square$

### Proposition 3.5 — presentation invariance

Simultaneous typed basis changes, Choi-convention changes, and permutations
of classical outcome handles leave the tester seminorm invariant.

*Proof.* A typed basis change conjugates process and dual tester operators so
that $\operatorname{Tr}(T_tX)$ is unchanged. A consistent Choi-convention
change is the same coordinate change written with the corresponding partial
transposes. An outcome permutation only permutes terms in the $\ell^1$ sum.
$\square$

### Remark 3.6 — unrestricted scope

When $\mathsf{Test}_D(\tau)$ contains every mathematically admissible
generalized tester, Definition 3.2 is the standard tester/comb or interactive
strategy distinguishability norm in the $\ell^1$ convention. With the common
$1/2$ normalization it is the optimal single-use discrimination bias. The
restricted version is only a seminorm because experimentally inaccessible
process differences may lie in its kernel [1--3].

The operational quotient is therefore

$$
\overline{\mathsf{Comb}}_D(\tau)
=
\operatorname{span}_{\mathbb R}\mathsf{Comb}(\tau)
/\ker\|\cdot\|_{\mathsf{Test}_D}.
$$

No dormant coefficient survives this quotient merely because it is nonzero.

---

## 4. A complete operational W3 package

### 4.1 Typed wires

Use the following laboratory types:

$$
\begin{array}{ccl}
\mathcal P_\alpha&:&I\longrightarrow H_0,\\
\mathcal U,\mathcal N&:&H_0\longrightarrow H_1,\\
\mathcal R_r,\mathcal Q_k&:&H_1\longrightarrow H_1,\\
\mathcal V_v,\mathcal E_e&:&H_1\longrightarrow H_2,\\
\mathcal M_j&:&H_2\longrightarrow K_j.
\end{array}
$$

Here $I\cong\mathbb C$ is the trivial source system. Classical outcome
registers $\alpha,r,k,v,e,j$ are retained. A later tail tester may act on
$K_j$ and on any retained classical or quantum memory admitted by the law.

### Definition 4.1 — complete marked W3 comb

A complete marked W3 candidate is

$$
\mathbf W
=
\left(
\boldsymbol{\mathcal P},
\boldsymbol{\mathcal U},
\boldsymbol{\mathcal N},
\mathbf R\subseteq\mathbf F,
\mathsf{Slot},
\boldsymbol{\mathcal V},
\boldsymbol{\mathcal E},
\boldsymbol{\mathcal M},
\mathsf{Test}_D
\right),
$$

where:

- $\boldsymbol{\mathcal P}=(\mathcal P_\alpha)_\alpha$ is a complete source
  CP instrument;
- $\boldsymbol{\mathcal U}$ is the write channel or complete write
  instrument;
- $\boldsymbol{\mathcal N}$ is a same-type no-write control;
- $\mathbf F=(\mathcal Q_k)_k$ is a finite sharp fine interrogation and
  $\mathbf R=(\mathcal R_r)_r$ its coarse record action;
- $\mathsf{Slot}$ is the typed continuation port;
- $\boldsymbol{\mathcal V}$ and $\boldsymbol{\mathcal E}$ are complete
  preserving- and erasing-candidate instrument families;
- $\boldsymbol{\mathcal M}$ is the complete output-instrument family; and
- $\mathsf{Test}_D$ is the frozen admitted complete-tester family.

Every field is part of the process object. None is replaced by a normalized
state or POVM shadow.

### Proposition 4.2 — instrument families and flagged combs

For every finite CP instrument $(\mathcal I_i)_{i\in\Omega}$, define the
flagged channel

$$
\widehat{\mathcal I}(\rho)
=
\sum_{i\in\Omega}|i\rangle\langle i|_C
\otimes\mathcal I_i(\rho).
$$

Then $\widehat{\mathcal I}$ is CPTP, and its Choi operator is

$$
J(\widehat{\mathcal I})
=
\sum_i|i\rangle\langle i|_C\otimes J(\mathcal I_i).
$$

Conversely, projecting a channel that is diagonal on the declared classical
flag $C$ recovers a unique CP-instrument family. These two constructions are
inverse.

*Proof.* Complete positivity follows termwise. Trace preservation follows
from $\sum_i\mathcal I_i$ being trace preserving. Orthogonal projection onto
$|i\rangle\langle i|_C$ recovers $J(\mathcal I_i)$ uniquely. $\square$

Applying this construction to source, continuation, and output outcomes turns
Definition 4.1 into one typed deterministic open comb with classical wires
and a continuation slot. Applying the inverse recovers every original CP
branch, including its weight and quantum output. The family and flagged-comb
representations are therefore equivalent at this finite scope.

### 4.2 Sharp record action

At the cut, let $(Q_k)_{k\in K}$ be mutually orthogonal projections summing
to $I_{H_1}$. Let $K=\bigsqcup_{r\in\Omega}K_r$ and

$$
P_r=\sum_{k\in K_r}Q_k.
$$

The complete nondemolition branches are

$$
\mathcal Q_k(\rho)=Q_k\rho Q_k,
\qquad
\mathcal R_r(\rho)=P_r\rho P_r.
$$

Their deterministic sums are the fine and coarse dephasings. In particular,

$$
\boxed{
\mathcal D_R(\rho)=\sum_rP_r\rho P_r.
}
$$

The Lüders form is a declared first finite representative of a sharp
nondemolition classical action. The outcome instruments, not only their
effects $(P_r)$, are retained.

### 4.3 Source branches

Because the source input is trivial, each source branch is equivalently a
subnormalized state

$$
\sigma_\alpha=\mathcal P_\alpha(1),
\qquad
w_\alpha=\operatorname{Tr}\sigma_\alpha,
\qquad
\sum_\alpha w_\alpha=1.
$$

This equivalence does not discard branch information: the complete list
$(\sigma_\alpha)_\alpha$, including every weight and outcome handle, is the
CP source instrument. General nontrivial source inputs require the CP maps
themselves and are covered by the comb definition.

Write

$$
W_\alpha=\mathcal U(\sigma_\alpha),
\qquad
W=\bigoplus_\alpha W_\alpha,
$$

where the direct sum denotes the retained classical source flag. Record
dephasing acts as the identity on that flag.

---

## 5. Operational W3 conditions

### Definition 5.1 — complete write correlation

Let $r(k)$ denote the unique coarse sector containing fine alternative $k$.
The complete support-correlation condition is

$$
\operatorname{Tr}(Q_kW_\alpha)>0,
\quad
\operatorname{Tr}(Q_\ell W_\alpha)>0,
\quad k\ne\ell
\quad\Longrightarrow\quad
r(k)\ne r(\ell)
$$

for every nonzero source branch $\alpha$. Equivalently, each written branch
has support on at most one live fine alternative inside each coarse record
sector. For positive $W_\alpha$, a zero fine probability removes the
corresponding support block, so the probability and support formulations
agree. All probabilities use the subnormalized branch $W_\alpha$; no branch
is normalized and then stripped of its weight.

### Definition 5.2 — complete no-write failure

Let

$$
N_\alpha=\mathcal N(\sigma_\alpha).
$$

The no-write control fails correlation when at least one retained nonzero
source branch has positive probability on two distinct fine alternatives in
one coarse record sector. The control is a complete same-type comb, not one
selected matrix column.

### Definition 5.3 — preservation

Encode the complete continuation instrument
$(\mathcal V_v)_v$ as one channel to a direct-sum output carrying the
classical outcome $v$. It preserves the record at the admitted tester scope
when

$$
\boxed{
\|\boldsymbol{\mathcal V}\star W
-
\boldsymbol{\mathcal V}\star\mathcal D_R\star W
\|_{\mathsf{Test}_D}=0.
}
$$

Because the continuation outcome remains available to every compatible
tester, this equality compares every CP branch and all admitted tail
experiments, not only the unconditional channel or a POVM shadow.

### Definition 5.4 — coherent recovery

The complete continuation instrument
$(\mathcal E_e)_e$ is a coherent eraser or recovery operation when

$$
\boxed{
\|\boldsymbol{\mathcal E}\star W
-
\boldsymbol{\mathcal E}\star\mathcal D_R\star W
\|_{\mathsf{Test}_D}>0.
}
$$

Equivalently, there exist an admitted complete tester $\mathbf T$ and outcome
$t$ for which

$$
\operatorname{Tr}
\left[
T_t\bigl(\boldsymbol{\mathcal E}\star W\bigr)
\right]
\ne
\operatorname{Tr}
\left[
T_t\bigl(\boldsymbol{\mathcal E}\star\mathcal D_R\star W\bigr)
\right].
$$

### Definition 5.5 — complete operational W3

A marked candidate is W3 at the declared tester scope precisely when:

1. every field in Definition 4.1 is a correctly typed complete instrument or
   deterministic comb;
2. complete write correlation holds;
3. the matched complete no-write control fails correlation;
4. at least one declared preserving continuation satisfies Definition 5.3;
5. at least one declared eraser satisfies Definition 5.4; and
6. all comparisons are made after the operational quotient of Section 3.

This definition identifies a possible stable record seam. It does not select
which record outcome actually occurs.

### Definition 5.6 — recoverable process coherence

For a same-type deterministic or complete-instrument continuation $E$, set

$$
\boxed{
\mathcal C_R(W;E)
=
\|E\star(W-\mathcal D_R\star W)\|_{\mathsf{Test}_D}.
}
$$

### Proposition 5.7 — elementary properties

At the declared finite scope:

1. $0\leq\mathcal C_R(W;E)\leq2$ for deterministic normalized compared
   processes;
2. it is invariant under typed presentation changes and outcome renaming;
3. if $\mathsf T_1\subseteq\mathsf T_2$, then
   $\mathcal C_R^{\mathsf T_1}\leq\mathcal C_R^{\mathsf T_2}$; and
4. for an admitted downstream supermap $S$ whose tester pullbacks are
   admitted,

   $$
   \mathcal C_R(W;S\circ E)
   \leq
   \mathcal C_R(W;E).
   $$

*Proof.* The first bound is the $\ell^1$ distance between probability
distributions. The second is Proposition 3.5. The third follows because a
supremum over a subset cannot increase. The fourth is Proposition 3.4.
$\square$

### Remark 5.8 — three distinct defects

Recoverable process coherence is not the Born composition defect
$\Delta^B$, which compares composition of stochastic shadows. It is also not
the record multiplicativity defect

$$
\Delta_F^{\mathrm{rec}}(a,b)=F(ab)-F(a)F(b),
$$

which tests whether a UCP map transports a record algebra homomorphically.
$\mathcal C_R$ instead compares two complete interactive processes under all
admitted testers.

---

## 6. Relation to terminal effect tests

The complete tester definition contains the earlier effect-level block
criterion as a special case, but the two are not interchangeable.

### Theorem 6.1 — terminal one-step equivalence

Let $V:H_1\to H_2$ be a channel, let $\mathcal E\subseteq\mathcal L(H_2)$
be the admitted terminal effect operator system, and let the admitted source
states span the Hermitian operators on $H_1$. Let terminal testers consist of
the binary readouts $(a,I-a)$ for every $a\in\mathcal E$. Then

$$
\|V\star W-V\star\mathcal D_R\star W\|_{\mathsf{Test}_D}=0
$$

for every retained source branch if and only if

$$
\boxed{
\mathcal D_RV^*(a)=V^*(a)
\quad\forall a\in\mathcal E.
}
$$

Equivalently,

$$
P_rV^*(a)P_s=0
\quad(r\ne s)
$$

for every admitted terminal effect.

*Proof.* The probability contrast on source state $\rho$ and effect $a$ is

$$
\operatorname{Tr}\rho
\left(V^*(a)-\mathcal D_RV^*(a)\right).
$$

If the block identity holds, every contrast vanishes. Conversely, vanishing
on a Hermitian-spanning source family forces the Hermitian operator in
parentheses to be zero. The block form is the definition of the fixed points
of $\mathcal D_R$. $\square$

### Corollary 6.2 — nonseparating sources

For a fixed non-tomographic source family, the block identity remains
sufficient but need not be necessary. A nonzero off-diagonal block may lie in
the annihilator of every admitted source state. Operational preservation is
always the tester equality; the operator identity is equivalent only under
the stated separation hypothesis.

### Proposition 6.3 — tail testers retain disturbance

Suppose two output instruments have the same POVM effects but different CP
branches. Terminal outcome probabilities cannot separate them, but an
admitted tail tester may. Therefore a terminal complete-effect block theorem
is not by itself equivalent to equality of arbitrary interactive instrument
combs. It is not sufficient when tail testers resolve disturbance; without a
separating source family it also need not be necessary.

*Proof.* The explicit Lüders/reprepare construction in Section 8.2 has equal
outcome effects and disjoint tail probabilities, proving the first claim.
Corollary 6.2 proves the second. $\square$

### Proposition 6.4 — sharp transport is the zero-defect special case

Let $F:B\to A$ be UCP and let

$$
R=C^*(P_r:r\in\Omega)\subseteq B
$$

be a finite sharp record algebra. The following are equivalent:

$$
\begin{aligned}
&R\subseteq\operatorname{MD}(F),\\
&F|_R\text{ is a unital *-homomorphism},\\
&F(P_r)\text{ is a projection for every }r,\\
&F(P_r)-F(P_r)^2=0\text{ for every }r.
\end{aligned}
$$

*Proof.* Schwarz positivity gives
$F(P_r)-F(P_r)^2\geq0$. Equality for a projection is exactly the two-sided
multiplicative-domain condition. If it holds for every minimal generator,
linearity and the bimodule property make $F$ multiplicative on $R$.
Conversely a *-homomorphism preserves every projector and has zero defect.
$\square$

This proposition characterizes homomorphic transport of sharp propositions.
It does not by itself say that complete Schrödinger instrument branches,
their disturbances, or arbitrary tail testers are equal. Theorem 6.1 instead
characterizes when the **particular coherent/dephased process pair** is
indistinguishable under a separating terminal effect law. The two criteria
coincide only when additional typing identifies the transported record
algebra with the complete process comparison; neither is substituted for the
other here.

---

## 7. Exact cross-term controls

### 7.1 Four-level process

Let $H=\mathbb C^4$, $q_j=|j\rangle\langle j|$, and

$$
P_A=q_0+q_1,
\qquad
P_B=q_2+q_3.
$$

The complete source instrument has four equally weighted branches

$$
\sigma_j=\frac14q_j.
$$

Define unitary write and no-write controls by

$$
\begin{aligned}
U|0\rangle&=(|0\rangle+|2\rangle)/\sqrt2,
&U|1\rangle&=(|1\rangle+|3\rangle)/\sqrt2,\\
U|2\rangle&=(|0\rangle-|2\rangle)/\sqrt2,
&U|3\rangle&=(|1\rangle-|3\rangle)/\sqrt2,
\end{aligned}
$$

and

$$
\begin{aligned}
N|0\rangle&=(|0\rangle+|1\rangle)/\sqrt2,
&N|1\rangle&=(|0\rangle-|1\rangle)/\sqrt2,\\
N|2\rangle&=(|2\rangle+|3\rangle)/\sqrt2,
&N|3\rangle&=(|2\rangle-|3\rangle)/\sqrt2.
\end{aligned}
$$

Every $U|j\rangle$ has one fine component in each coarse sector. The matched
$N|0\rangle$ has two fine components in sector $A$, so the complete write and
no-write conditions hold. Let the preserving continuation be
$V=\mathcal D_R$ and the candidate eraser be $E=\operatorname{id}$.

### 7.2 Imaginary-cross-term false eraser

Admit the complete readouts $(P_A,P_B)$ and $(a_i,I-a_i)$, where

$$
|\chi_i\rangle=(|0\rangle+i|2\rangle)/\sqrt2,
\qquad
a_i=|\chi_i\rangle\langle\chi_i|.
$$

Each displayed effect pair denotes the full terminal instrument

$$
\mathcal M_x(\rho)
=
\operatorname{Tr}(e_x\rho)|x_c\rangle\langle x_c|,
$$

with $(e_x)_x$ equal to the displayed pair. Thus the output target and the
disturbance—destruction into a classical register—are fixed, rather than
silently replaced by the POVM alone.

For source branch $0$, put

$$
|\psi\rangle=U|0\rangle=(|0\rangle+|2\rangle)/\sqrt2.
$$

The individual algebraic term is

$$
\langle\psi|q_0a_iq_2|\psi\rangle=-\frac{i}{4}\ne0.
$$

It is not a probability. Its conjugate cancels it, and exactly

$$
\langle\psi|a_i|\psi\rangle
=
\langle\psi|\mathcal D_R(a_i)|\psi\rangle
=
\frac12.
$$

The same equality holds for all four source branches and both admitted
readouts. Hence

$$
\boxed{
\|E\star W-E\star\mathcal D_R\star W\|_{\mathsf{Test}_D}=0.
}
$$

The algebraic cross term is nonzero, but the eraser is rejected.

### 7.3 Probability-visible eraser

Replace $a_i$ by

$$
a_+=|\chi_+\rangle\langle\chi_+|,
\qquad
|\chi_+\rangle=(|0\rangle+|2\rangle)/\sqrt2.
$$

Freeze the admitted family here to the coarse record readout, this binary
readout, and their classical postprocessings.

For source branch $0$, the coherent binary distribution is $(1,0)$ and the
dephased distribution is $(1/2,1/2)$. For branch $2$ the distributions are
$(0,1)$ and $(1/2,1/2)$. Branches $1$ and $3$ give no contrast for this
readout. Retaining the source label and its weight $1/4$ gives

$$
\boxed{
\mathcal C_R(W;E)
=
\frac14(1)+\frac14(1)
=
\frac12.
}
$$

Classical postprocessing cannot increase $\ell^1$ distance, so the displayed
lower bound is also the exact supremum for this frozen family. This is a
probability-visible coherent recovery and passes.

---

## 8. Complete-instrument controls

### 8.1 Same normalized branches, different weights

Let two complete source instruments prepare the same normalized states
$(\rho_\alpha)_\alpha$ but with weights $p_\alpha$ and $q_\alpha$. A tester
that reads the retained source outcome obtains distributions $p$ and $q$, so

$$
\|\boldsymbol{\mathcal P}^{p}
-\boldsymbol{\mathcal P}^{q}\|_{\mathsf{Test}_D}
\geq
\sum_\alpha|p_\alpha-q_\alpha|.
$$

Equality holds when no later branch-dependent difference is present. The
normalized-state shadow would identify these sources incorrectly.

### 8.2 Same POVM, different instrument

On $H=\mathbb C^3$, let

$$
P_A=q_0+q_1,
\qquad
P_B=q_2.
$$

Compare the Lüders instrument

$$
\mathcal L_r(\rho)=P_r\rho P_r
$$

with the measure/reprepare instrument

$$
\mathcal J_A(\rho)=\operatorname{Tr}(P_A\rho)q_0,
\qquad
\mathcal J_B(\rho)=\operatorname{Tr}(P_B\rho)q_2.
$$

Both are complete and have the same effects:

$$
\mathcal L_r^*(I)=P_r=\mathcal J_r^*(I).
$$

On input $q_1$, outcome $A$ is certain, but

$$
\mathcal L_A(q_1)=q_1,
\qquad
\mathcal J_A(q_1)=q_0.
$$

A subsequent computational readout has disjoint outcome distributions, so
their tester distance is $2$. The instrument combs are operationally
different even though their POVM shadows agree.

### 8.3 An interactive tester beyond one-shot output labels

The preceding discriminator is a two-stage tester: it first retains outcome
$r$ and then, conditional on $r=A$, applies a second quantum readout to the
surviving output. A one-shot tester that keeps only the label $r$ cannot
distinguish $\boldsymbol{\mathcal L}$ from $\boldsymbol{\mathcal J}$; the
adaptive tail does so perfectly. No quantum memory ancilla is required in
this smallest example, although the complete comb formalism admits one.

This is the exact finite control required to show that complete effects do
not exhaust complete instruments. More general memory-assisted advantages in
channel discrimination are established in [4].

### 8.4 Inaccessible spectator

Let $C'=C\otimes\sigma_A$ for a fixed spectator state. Suppose the admitted
tester law on $C'$ is exactly the image of the tester law on $C$ under

$$
T\longmapsto T\otimes I_A,
$$

with the spectator discarded at closure. Then

$$
p_{T\otimes I_A}(C')=p_T(C)
$$

for every admitted tester, so their probability functors are naturally
identical and the spectator is operationally inaccessible. If a
spectator-resolving tester is admitted, the premise fails and no quotient is
licensed. The criterion is the tester functor, not a bare tensor formula.

### 8.5 Nonfaithful tester family

In Section 7.2, the coherent and dephased processes are distinct positive
operators but equal in the quotient generated by the two frozen readouts.
Adding the real-phase tester of Section 7.3 separates them. Thus

$$
C\simeq_{\mathrm{op}}C'
$$

is deliberately law relative. A restricted admitted family can be
non-tomographic without being inconsistent.

### 8.6 Declared regional fact descent as a special case

In the finite RQ0-A control, typed amplitude-instrument morphisms and exact
projector pullbacks are supplied between a master instrument, three declared
regions, and a common overlap. Regard each supplied instrument as a comb and
each declared sharp pullback as a zero-defect classical interface map. The
same commuting diagrams remain valid under the tester functor, so the prior
record descent is recovered as a declared sharp special case.

Nothing here reconstructs those regions or overlap maps. Equal tester laws
without the supplied structural maps would still not establish fact identity.

---

## 9. Exact nine-candidate branch-memory classification

### 9.1 Complete law

Let

$$
H=\mathbb C_b^2\otimes\mathbb C_m^2,
\qquad
H_2=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

The complete source instrument has four outcomes

$$
\sigma_j=\frac14|j\rangle\langle j|
$$

in the order $(|00\rangle,|10\rangle,|01\rangle,|11\rangle)$. The complete
terminal output instrument is

$$
\mathcal M_i(\rho)
=
\operatorname{Tr}(|i\rangle\langle i|\rho)
|i_c\rangle\langle i_c|.
$$

The frozen tester law retains the source label and every classical
postprocessing of this terminal four-outcome instrument. It admits no
quantum tail after the classical target.

Use

$$
U=\operatorname{CNOT}_{b\to m}(H_2\otimes I),
\qquad
N=H_2\otimes I,
$$

$$
V=H_2\otimes I,
\qquad
E=(H_2\otimes I)\operatorname{CNOT}_{b\to m}=U^*.
$$

Define

$$
v_0=|+,0\rangle,
\quad v_1=|-,0\rangle,
\quad v_2=|+,1\rangle,
\quad v_3=|-,1\rangle.
$$

In the displayed source order,

$$
A_{ij}=2\langle v_i|U|j\rangle
$$

is

$$
A=
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix},
\qquad A^*A=4I.
$$

### 9.2 Candidate partitions

Universal preservation under the declared terminal tester law requires the
coarse record projectors to be spans of blocks in a set partition of
$\{v_0,v_1,v_2,v_3\}$. For a block of size one, the restricted write columns
have one fine ray. For a block of size two, they lie on the two orthogonal
rays $(1,1)$ and $(1,-1)$, and both occur. A block of size three fails the
fine correlation test because distinct restricted columns have nonzero inner
product. The all-singleton partition has no within-sector pair on which the
matched no-write control can fail. A one-block partition is not a nontrivial
record.

Therefore the complete write and no-write controls leave exactly

$$
6\text{ partitions of type }2+1+1
\quad\sqcup\quad
3\text{ partitions of type }2+2.
$$

The source weights and output disturbances are retained in this statement;
the output branches end in a classical system.

### 9.3 Preservation distance

For every such partition $\pi$, the pulled-back terminal effects under $V$
are diagonal in the $v_i$ basis and hence fixed by $\mathcal D_{R_\pi}$.
The sufficient direction of Theorem 6.1 applies at the declared terminal
tester scope, giving

$$
\epsilon_{\mathrm{pres}}(R_\pi,V)=0
$$

for all nine candidates.

### 9.4 Exact recovery distance

Coherent evolution through $E=U^*$ returns every written source state to its
original computational output with probability one. After dephasing into
partition blocks $B\in\pi$, the probability of returning to the original
source label is

$$
p_{\mathrm{return}}(\pi)
=
\sum_{B\in\pi}
\left(\frac{|B|}{4}\right)^2
=
\frac1{16}\sum_{B\in\pi}|B|^2.
$$

The remaining probability is distributed among other output labels. Hence
the $\ell^1$ distance from the deterministic coherent distribution is

$$
\mathcal C_{R_\pi}(W;E)
=
2\left(1-\frac1{16}\sum_{B\in\pi}|B|^2\right).
$$

Consequently

$$
\boxed{
\begin{array}{c|c|c}
\text{partition type}&\sum_B|B|^2&\mathcal C_R\\ \hline
2+1+1&6&5/4\\
2+2&8&1
\end{array}
}
$$

for every source branch and therefore for the retained equally weighted
source instrument.

### Theorem 9.1 — operational classification

At this exact complete terminal-instrument law, all nine candidates satisfy
the complete comb W3 conditions. They form two tester-distinguished numerical
classes, six with recovered coherence $5/4$ and three with recovered
coherence $1$.

No preferred seam is selected. A larger admitted tester family may refine or
eliminate this law-relative classification; it may not be added after seeing
which candidate one wants.

---

## 10. Tester contexts and the variance obstruction

### 10.1 Context category

First define $\mathsf{Tester}_D(\tau)$. Its objects are complete admitted
testers of type $\tau$. A morphism $f:\mathbf T\to\mathbf T'$ is an admitted
deterministic conversion of complete experiments—classical
postprocessing/coarse-graining, outcome refinement with its declared
forgetful map, or insertion of a fixed admitted control—together with its
affine probability map

$$
p_{\mathbf T'}(C)=K_f p_{\mathbf T}(C).
$$

Identity conversions and composition of the affine maps make this a small
category. No arrow is introduced merely because two testers happen to have
the same probability on one candidate.

Fix a finite candidate-independent master object set $A=A_D$ in this tester
category, closed under every conversion used in the paper. It is jointly
separating for the declared operational quotient: equality of all tables
indexed by $A$ is exactly $\simeq_{\mathrm{op}}$ at this finite scope. The
conversion maps $K_f$ are stored as compatibility equations on physically
realized tables; the raw evaluation sheaf below stores the typed coordinates
before that chart-complete image condition is imposed.

Define $\mathsf{TestCtx}_D$ to be the poset category whose objects are subsets
$U\subseteq A$ and whose arrows $V\to U$ are inclusions $V\subseteq U$.
The empty context is allowed for gluing but certifies no physical predicate.
Each $U$ represents a family of **complete** testers; “incomplete context”
means only that the family is not jointly separating, not that its individual
testers are unnormalized fragments.

For each $U$, let

$$
\mathsf{Comb}_U
=
\mathsf{Comb}/\ker\|\cdot\|_U.
$$

A family $\{U_i\to U\}$ covers $U$ exactly when

$$
\bigcup_iU_i=U.
$$

It is jointly separating for the $U$-observable quotient
$\mathsf{Comb}_U$. In particular, every cover of the master context $A$ is
jointly separating for the declared physical quotient.

The sheaf and stack terminology below uses the standard site and descent
conventions of [8].

### Proposition 10.1 — Grothendieck topology

The displayed coverage is a Grothendieck topology on
$\mathsf{TestCtx}_D$.

*Proof.* The identity family covers. If $\{U_i\}$ covers $U$ and $V\subseteq
U$, then $\{U_i\cap V\}$ covers $V$, proving pullback stability. If each
$U_i$ is covered by $\{U_{ij}\}$, then the union of all $U_{ij}$ is $U$,
proving transitivity. $\square$

### 10.2 Why valid seams are not a presheaf

For a candidate $s$, define informally

$$
\operatorname{Valid}_s(U)
$$

to mean that every preserving comparison is zero on $U$ and at least one
eraser comparison is positive on $U$. If $V\subseteq U$, the universal zero
condition restricts from $U$ to $V$. The existential positive witness need
not.

Take $U=\{T_+,T_i\}$ from Sections 7.2--7.3 and
$V=\{T_i\}$. The real tester $T_+$ witnesses erasure on $U$, but the
imaginary tester $T_i$ sees zero contrast. Thus $s$ is valid on $U$ and not
on $V$. There is no restriction arrow

$$
\operatorname{Valid}_s(U)\longrightarrow\operatorname{Valid}_s(V).
$$

Therefore contextwise W3-valid seams do **not** form a presheaf. No notation
or sheafification can repair a missing restriction map.

---

## 11. The tester-evaluation sheaf

### 11.1 Probability-table fibers

Let $\mathfrak S$ be the finite groupoid of typed candidate W3 presentations
declared independently of the tester context. Its arrows are presentation
gauge isomorphisms; physical symmetries may be retained as a separate action.

For every candidate $s$, tester $a\in A$, and named comparison

$$
\Xi\in
\{W,N,V\star W,V\star\mathcal D_RW,
E\star W,E\star\mathcal D_RW\},
$$

let $X_{s,a,\Xi}$ be the finite simplex containing the complete outcome
probability vector. Source, continuation, output, and tail outcomes remain
jointly indexed.

For each candidate define

$$
\mathcal E_s(U)
=
\prod_{a\in U}
\prod_\Xi X_{s,a,\Xi}.
$$

The simultaneous candidate census is

$$
\mathcal E(U)
=
\prod_{s\in\operatorname{Ob}\mathfrak S}\mathcal E_s(U).
$$

For $V\subseteq U$, restriction deletes the coordinates indexed by
$U\setminus V$. The candidate groupoid acts equivariantly by relabeling its
object index and the associated typed outcome coordinates.

### Theorem 11.1 — exact descent of tester data

$\mathcal E$ is a sheaf on $\mathsf{TestCtx}_D$.

*Proof.* Let $\{U_i\to U\}$ cover. A matching family consists of probability
tables $e_i\in\mathcal E(U_i)$ whose coordinates agree on every
$U_i\cap U_j$. Since $\bigcup_iU_i=U$, each coordinate in $U$ occurs in at
least one member, and overlap agreement makes its value independent of the
choice. These values define a unique $e\in\mathcal E(U)$ restricting to every
$e_i$. $\square$

The theorem glues complete probability data. It does not assert that every
abstract compatible table is generated by a physical comb.

### Definition 11.2 — physically realized chart-complete sections

For each candidate $s$, let

$$
\operatorname{Real}_{D,s}(A)\subseteq\mathcal E_s(A)
$$

be the image of the declared typed comb packages carrying $s$ under the
generalized Born evaluation map, and put

$$
\operatorname{Real}_D(A)
=
\coprod_s\operatorname{Real}_{D,s}(A).
$$

Presentation arrows in $\mathfrak S$ transport these fibers. Physical
realizability is an image condition at the terminal context $A_D$ of this
one-chart site; it is not manufactured by sheafification.

For $e\in\operatorname{Real}_D(A)$ and candidate $s$, define the
chart-complete W3 predicate using:

1. the complete write and no-write tables;
2. zero preservation contrast for every tester in $A$; and
3. positive erasure contrast for at least one tester in $A$.

The **chart-complete W3 locus** is the full subgroupoid

$$
\mathfrak{Seam}_{W3}(D)
\subseteq
\operatorname{Real}_D(A)//\mathfrak S
$$

on objects satisfying that predicate. Physical-symmetry arrows are retained;
no lexical representative is chosen.

### Definition 11.3 — tester stack

The candidate-presentation action groupoid on the family
$\coprod_s\mathcal E_s$ defines a groupoid-valued prestack. Its stackification
is denoted

$$
\boxed{
\mathfrak{Eval}_{W3}
=
[\coprod_s\mathcal E_s/\mathfrak S]^{\#}.
}
$$

Concretely, descent data are local complete probability tables together with
candidate-presentation isomorphisms on overlaps satisfying the cocycle law.
Theorem 11.1 glues the tables; stackification glues the isomorphism descent
data and retains stabilizers. It does not create a physical realization or
an eraser witness. Objects added by stackification over disconnected tester
subcontexts are contextual candidate families; they count as one physical
seam of chart $D$ only if represented by an object of the realized
chart-complete W3 locus.

The notation “W3” here records the suite of comparisons carried by the
evaluation object. W3 validity itself is the chart-complete locus of Definition
11.2, not a contextwise object predicate.

### Corollary 11.4 — singleton discipline

A singleton tester context can carry partial evidence for or against one
comparison inside chart $D$. It cannot certify a chart-complete W3 seam
unless its table extends to a physically realized section over $D$'s jointly
separating master context $A_D$ and that section lies in
$\mathfrak{Seam}_{W3}(D)$.

### 11.2 Preservation-versus-erasure variance

Let $Z_V(s)\subseteq A$ be the testers giving zero preserving contrast, and
let

$$
W_E(s)=\{a\in A:\text{$a$ gives a positive eraser contrast}\}.
$$

Preservation on $U$ is the inclusion $U\subseteq Z_V(s)$; it is downward
closed under restriction. Erasure on $U$ is $U\cap W_E(s)\ne\varnothing$;
it is upward closed under extension. The evaluation sheaf stores both sets'
underlying probability data without pretending that their conjunction has
one variance.

This is the precise resolution of the tester-descent obstruction.

---

## 12. Context and ontology controls

### 12.1 Favorable singleton versus separating family

Let a continuation rotate $\operatorname{span}\{|1\rangle,|2\rangle\}$
across two record sectors while fixing $|0\rangle$. A singleton terminal test
of $q_0$ sees zero coherence contrast. The admitted test of $q_1$ has a
nonzero cross-sector pullback and hence a positive probability contrast on a
separating source. The singleton is locally favorable; the covering family
rejects chart-complete preservation.

### 12.2 Context variance

The real/imaginary pair of Sections 7.2--7.3, used in Section 10.2, exhibits
eraser-witness loss under restriction. The rotated $q_0/q_1$ pair above
exhibits a preservation false
positive under a nonseparating singleton. Together they show why both
universal and existential parts must be evaluated on the frozen master
context.

### 12.3 Instrument-relative memory

The master tester family is physical law input. Enlarging it can expose
previously invisible coherence or disturbance; restricting it can identify
distinct process tensors. This instrument relativity is consistent with the
operational process-tensor framework and with results showing that quantum
Markov order can depend on the intervention instrument [5--7].

It follows that this paper does not produce one context-free metaphysical
cut. It produces W3 validity relative to a declared complete experimental
law, with compatibility across its tester contexts.

### 12.4 No actualization and no co-reference

A comb and its tester functor determine outcome probabilities and
outcome-conditioned CP transformations. They do not select which outcome is
actual in one run. Moreover, two record interfaces with equal probability
functors need not denote the same fact or the same occurrence token.
Therefore

$$
\boxed{
\text{W3 seam}
\ne
\text{actual outcome}
\ne
\text{fact co-reference}
\ne
\text{event-token identity}.
}
$$

---

## 13. Four-gate audit

| Object | Referent | Necessity | No-smuggling rule | Discriminator |
|---|---|---|---|---|
| complete W3 comb | whole multi-stage laboratory network with every CP branch | states and POVMs discard weights and disturbance | no branch may be replaced by its normalized/effect shadow | Lüders versus reprepare; unequal source weights |
| admitted tester quotient | equality under every experiment the declared law can perform | dormant matrix coefficients produced false erasers | tester family is frozen independently of the candidate | imaginary cross term fails; real contrast passes |
| recoverable process coherence | maximum admitted closed-experiment contrast after dephasing | algebraic coherence need not be observable | only generalized Born probabilities enter | exact values $0$, $1/2$, $1$, $5/4$ |
| tester-context site | compatible families of complete experimental contexts | W3's universal and existential clauses have opposite variance | covers are actual unions and separate the stated quotient | singleton/cover and witness-loss controls |
| evaluation sheaf | complete probability tables of every named comparison | contextwise valid seams have no restriction maps | sheafification cannot create physical realizability or a witness | explicit coordinate gluing theorem |
| chart-complete W3 locus | realized one-chart full-context data satisfying all W3 clauses | partial favorable tests can be misleading | only realized $A_D$ sections qualify; no atlas-wide tester is allowed | rotated singleton and real/imaginary cover |

Every construction is law relative. The cut, record action, and admitted
tester grammar remain selected inputs in this cycle; the paper does not
rename them intrinsic.

---

## 14. Theorems and limitations

### 14.1 Provisional earned ladder

The finite construction establishes, prior to hostile review:

#### `RQ0-L0-COMB-COMPLETE-W3`

The source, write, no-write, record, continuation, and output CP branches are
fields of one typed open-comb package. Complete write and control conditions
use subnormalized source branches, and every continuation is composed by a
typed link product.

#### `RQ0-L0-TESTER-SEPARATED-W3`

Operational equivalence is equality under all frozen admitted complete
testers. Preservation is zero tester distance and recovery is positive tester
distance. The imaginary-cross false eraser is rejected and an exact
probability-visible eraser passes.

#### `RQ0-L0-W3-TEST-SHEAF`

The finite context category and Grothendieck topology are explicit. Complete
tester-evaluation data form a sheaf; the candidate-presentation quotient has
a typed stackification; W3 seams form a realized chart-complete locus; and the
universal/existential variance obstruction is resolved without inventing a
restriction map for contextwise-valid seams.

### 14.2 Exact scope of the third rung

The third result is a **tester-evaluation** sheaf and chart-complete W3 locus.
Its “global sections” are internal to one chart's finite tester site. It is
not a theorem that arbitrary partially realized process tables glue to a
chart-complete comb, nor is it a spatial or atlas sheaf. It depends on a fixed
finite master tester universe for $D$ and a fixed candidate groupoid. These
restrictions are part of the theorem.

### 14.3 First unresolved obstruction

The first remaining question is intrinsic selection of the process cut,
candidate sharp action, and tester grammar from operational theory without
planting them. The present work tells us what a complete W3 claim means once
those objects are supplied and how to compare it experimentally. It does not
derive quantum charts or their physical overlaps.

### 14.4 Prohibited conclusions

No result in this paper establishes:

- a selected actual record atom;
- W6 fact or event-token co-reference;
- autonomous subsystem control;
- a generic physical overlap;
- intrinsic spatial localization;
- topology or a manifold shadow;
- influence or causal order;
- dimension, volume, Lorentzian geometry, or special relativity;
- quantum fields; or
- gravity.

---

## 15. Conclusion

The physically meaningful W3 primitive is not an off-diagonal amplitude and
not a PVM with loose dynamical annotations. It is a complete interactive
quantum process identified through every complete experiment admitted by its
law.

At that level, the two central W3 statements become operationally exact:

$$
\text{preservation}
\iff
\text{record dephasing changes no admitted tester probability},
$$

and

$$
\text{coherent recovery}
\iff
\text{an admitted tester sees a positive probability contrast}.
$$

The tester quotient removes invisible coefficients automatically. Complete
instruments retain branch weights and disturbance. The tester-evaluation
sheaf keeps partial-context experimental evidence compatible without falsely treating
an existential witness as restriction stable. The result is a finite,
law-relative operational foundation for recognizing quantum seams inside one
finite operational chart—not yet cross-chart locality or spacetime.

---

## References

1. G. Chiribella, G. M. D'Ariano, and P. Perinotti, “Theoretical framework
   for quantum networks,” *Physical Review A* **80**, 022339 (2009),
   [arXiv:0904.4483](https://arxiv.org/abs/0904.4483).
2. G. Gutoski and J. Watrous, “Toward a general theory of quantum games,”
   in *Proceedings of STOC 2007*, pp. 565–574,
   [arXiv:quant-ph/0611234](https://arxiv.org/abs/quant-ph/0611234).
3. G. Gutoski, “On a measure of distance for quantum strategies,”
   *Journal of Mathematical Physics* **53**, 032202 (2012),
   [arXiv:1008.4636](https://arxiv.org/abs/1008.4636).
4. G. Chiribella, G. M. D'Ariano, and P. Perinotti, “Memory effects in
   quantum channel discrimination,” *Physical Review Letters* **101**,
   180501 (2008),
   [journal](https://doi.org/10.1103/PhysRevLett.101.180501).
5. F. A. Pollock, C. Rodriguez-Rosario, T. Frauenheim, M. Paternostro, and
   K. Modi, “Operational Markov condition for quantum processes,”
   *Physical Review Letters* **120**, 040405 (2018),
   [arXiv:1801.09811](https://arxiv.org/abs/1801.09811).
6. F. A. Pollock, C. Rodriguez-Rosario, T. Frauenheim, M. Paternostro, and
   K. Modi, “Non-Markovian quantum processes: Complete framework and
   efficient characterization,” *Physical Review A* **97**, 012127 (2018),
   [arXiv:1512.00589](https://arxiv.org/abs/1512.00589).
7. P. Taranto, F. A. Pollock, S. Milz, M. Tomamichel, and K. Modi, “Quantum
   Markov order,” *Physical Review Letters* **122**, 140401 (2019),
   [arXiv:1805.11341](https://arxiv.org/abs/1805.11341).
8. S. Mac Lane and I. Moerdijk, *Sheaves in Geometry and Logic: A First
   Introduction to Topos Theory*, Springer (1992).
