# Operational Classical Cores of Minimal Quantum Boundaries

## Matrix-Ordered Testers, Nondisturbing Instruments, and Split Process Sectors

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-01

**Frozen analytical pin:** `f00140c`

---

## Abstract

A minimal sufficient quantum process boundary need not be an observable
algebra, so its mathematical center is not defined. This paper gives a
strictly operational replacement at finite one-chart scope.

First, an ancilla-complete family of admitted process testers defines an
Archimedean matrix order on the effect dual of a process boundary. An
admitted deterministic superchannel pulls these effects back by a unital
completely positive map. A minimum process idempotent therefore induces a
UCP idempotent exactly when its idempotence survives the complete operational
kernel. This is automatic under an explicitly declared ancilla-saturation
condition, but it does not follow from scalar positivity alone. The positive
transpose symmetrizer supplies an exact two-level counterexample.

Second, classicality is defined by a complete admitted instrument whose
outcome can be retained, whose forgotten-outcome channel is the identity of
the minimal Karoubi object, and whose branches are exclusive and repeatable.
No multiplication is required. A two-outcome branch is a completely positive
order projection: both it and its complement are CP. We prove that all such
order projections commute. Under the physically explicit closure of admitted
instruments under sequential composition and classical coarse-graining,
they form a finite Boolean algebra. Its nonzero atoms give a unique finest
nondisturbing repeatable instrument, up to outcome permutation. We call this
the operational classical core. It may have only one atom.

For a finite \(C^*\)-algebra with all standard instruments admitted, the
construction recovers the minimal central projections. It therefore recovers
the classical Koashi--Imoto sectors of a finite minimal state experiment.
For a full matrix factor it is trivial. It is also trivial for the hostile
operator system

\[
\operatorname{span}_{\mathbb C}
\{(I,I),(Z,Z),(X,2X+Z)\}
\subset M_2\oplus M_2,
\]

even though its \(C^*\)-envelope has center \(\mathbb C^2\). This separates
a physically readable split from an algebraic envelope center.

The corrected branch-memory minima have cores associated with
\(\mathbb C\), \(\mathbb C^5\), and \(M_4\oplus\mathbb C\). None selects the
familiar memory seam: the last center records only success versus failure,
with the same distribution for every source branch. Thus this cycle derives
a physical classical-core operation for a fixed minimal boundary, but not a
task-independent W3 record, local chart, spatial boundary or causal object.

---

## 1. Question and result

### 1.1 The obstruction

Fix one finite operational chart and one independently declared compatible
future-task family \(\mathfrak F\). Earlier work constructs a minimal
sufficient process boundary

\[
B_{\mathfrak F}=(X,e)
\in\operatorname{Kar}(\mathsf{Proc}_D),
\]

where \(e\) is an admitted stabilizing process idempotent. This object is
unique up to reversible operational equivalence at the declared
compact-convex scope.

The datum \((X,e)\) does not include a multiplication. Consequently,

\[
Z(X,e)
\]

is not a typed expression. Passing to a chosen \(C^*\)-envelope does not
solve the physical problem: the resulting central projections need not be
effects or instruments admitted by the original operational theory.

The question is therefore not how to manufacture a center. It is:

\[
\boxed{
\text{What classical information can actually be read repeatedly while the
entire minimal process boundary remains undisturbed?}
}
\]

### 1.2 Main result

At finite-dimensional, ancilla-saturated, instrument-complete operational
scope, the paper proves:

1. the complete tester dual of the minimal boundary is an operator system;
2. the minimum process idempotent induces a UCP idempotent on that dual;
3. every nondisturbing repeatable classical branch is a CP order projection;
4. all CP order projections commute;
5. the admitted split projections form a finite Boolean algebra; and
6. its atoms define a unique finest physical classical instrument.

The provisional cumulative result is

\[
\boxed{
\begin{array}{c}
\texttt{RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY}
\\[1mm]
\Downarrow
\\[1mm]
\texttt{RQ0-L0-OPERATIONAL-CLASSICAL-CORE}.
\end{array}}
\]

Both outcome names are restricted by the operational assumptions stated in
Sections 2 and 4. A law with no nontrivial admitted split has the trivial
one-outcome core and still satisfies the theorem.

### 1.3 Ontology firewall

The following distinctions are binding:

\[
\begin{array}{c}
\text{minimal future-relevant process information}
\\
\neq
\\
\text{physically readable classical information}
\\
\neq
\\
\text{an actual outcome in one run}
\\
\neq
\\
\text{a fact shared between charts}
\\
\neq
\\
\text{a spatial or causal boundary}.
\end{array}
\]

The operational core is relative to one fixed future task inside one chart.
No atlas-wide tester, global state, global event set or global present is
introduced.

---

## 2. Complete tester duality

### 2.1 Matrix-ordered operational data

Let \(V_B\) be the finite-dimensional real vector space spanned by the
Hermitian process objects of a typed boundary \(B\). Let

\[
K_n(B)\subset M_n(V_B)
\]

be the cone of positive \(n\)-ancilla process objects admitted by the law.
The following complete-admission assumptions are explicit.

**A1 — matrix compatibility.** The cones are closed, pointed and generating,
and are stable under direct sums and scalar conjugation:

\[
K_n(B)\oplus K_m(B)\subseteq K_{n+m}(B),
\]

\[
\alpha^*K_n(B)\alpha\subseteq K_m(B)
\]

for every scalar matrix \(\alpha\in M_{n,m}(\mathbb C)\).

**A2 — deterministic effect.** There is a distinguished normalization
functional \(u_B\) that is an Archimedean matrix order unit for the admitted
effect span.

**A3 — ancillary tester separation.** Equality in the complete operational
quotient means equality of every probability generated by every admitted
finite ancillary tester at every matrix level.

**A4 — pullback closure.** Precomposing an admitted tester with an admitted
process map gives an admitted tester of the source type.

These are law-relative operational assumptions. They do not imply that every
mathematically conceivable ancilla or tester exists.

### 2.2 The effect operator system

Let \(E_B^0\) be the complex linear span of admitted scalar tester effects.
Two effects are identified if they agree on every admitted process object at
every matrix level. Let \(E_B\) denote this quotient.

For \(F=[f_{ij}]\in M_k(E_B)_{\mathrm{sa}}\), define

\[
F\in M_k(E_B)_+
\]

exactly when the map

\[
x=[x_{ab}]
\longmapsto
[f_{ij}(x_{ab})]_{(i,a),(j,b)}
\]

is positive for every \(n\) and every \(x\in K_n(B)\).

The class of \(u_B\) is denoted by \(1_B\).

### Theorem 2.1 — complete tester dual

Under A1--A3,

\[
\mathcal E(B):=(E_B,\{M_n(E_B)_+\}_{n\geq1},1_B)
\]

is a finite-dimensional abstract operator system.

**Proof.** Self-adjointness is inherited from complex conjugation of tester
effects. Direct sums and scalar compression of positive effect matrices
follow from A1. Pointedness follows after quotienting by effects null on all
matrix process cones. The deterministic effect is a matrix order unit by A2;
Archimedeanization removes any residual infinitesimal order-null directions.
The Choi--Effros abstract characterization then represents this
Archimedean matrix-order-unit space completely order isomorphically as a
unital self-adjoint subspace of some \(B(H)\) [1,2]. No multiplication is
part of the conclusion. \(\square\)

### 2.3 Process maps act contravariantly

Let \(F:B\to C\) be an admitted process transformation. Define tester
pullback by

\[
F^\sharp(a)=a\circ F.
\]

### Proposition 2.2 — UCP pullback

If \(F\) is an admitted deterministic completely positive process map and
A4 holds, then

\[
F^\sharp:\mathcal E(C)\longrightarrow\mathcal E(B)
\]

is UCP. Composition and identities satisfy

\[
(GF)^\sharp=F^\sharp G^\sharp,
\qquad
1_B^\sharp=1_{\mathcal E(B)}.
\]

**Proof.** Determinism gives \(F^\sharp(1_C)=1_B\). For every positive effect
matrix \([a_{ij}]\), every admitted ancillary process \(x\), and every matrix
level, evaluation of \([F^\sharp(a_{ij})]\) on \(x\) is evaluation of
\([a_{ij}]\) on the completely positive image of \(x\). It is therefore
positive. Null effects remain null by tester pullback, so the map descends to
the quotient. The variance equations follow from associativity. \(\square\)

This is the finite-dimensional contravariant process/effect duality needed
below. General matrix-ordered duality for finite operator systems is an
established antecedent [1,2]; the contribution here is the operational
tester construction and its exact admission scope.

---

## 3. Lifting the minimal process idempotent

### 3.1 Scalar and complete kernels

Let \(N_1(B,C)\) be the space of process maps invisible to all admitted
scalar testers and let

\[
N_\infty(B,C)
=
\bigcap_{n\geq1}N_n(B,C)
\]

be the space invisible to every admitted ancillary tester. In general,

\[
N_\infty(B,C)\subseteq N_1(B,C).
\]

Let \(\widetilde e:X\to X\) be an admitted deterministic-superchannel
representative of the scalar Karoubi idempotent. Scalar idempotence says

\[
\widetilde e^2-\widetilde e\in N_1(X,X).
\]

### Proposition 3.1 — complete lift criterion

The scalar idempotent defines an idempotent on the complete operational
quotient if and only if

\[
\widetilde e^2-\widetilde e\in N_\infty(X,X).
\]

When this holds, its tester pullback is a UCP idempotent:

\[
(e^\sharp)^2=e^\sharp.
\]

**Proof.** Equality of two maps in the complete quotient is equality modulo
\(N_\infty\). The first statement is therefore the definition of complete
idempotence. Proposition 2.2 makes the pullback UCP, while contravariance
gives

\[
(e^\sharp)^2=(e^2)^\sharp=e^\sharp.
\]

\(\square\)

### 3.2 Ancilla saturation

Call the admitted tester doctrine ancilla-saturated at \(X\) when every
admitted ancillary distinction can already be closed into a scalar complete
tester of the same process type. Equivalently,

\[
N_1(X,X)=N_\infty(X,X).
\]

This is satisfied by the standard finite comb model when arbitrary admitted
finite references, memory-assisted controls and separating final
measurements are already included among the scalar closed experiments. It is
not a theorem about an arbitrary restricted laboratory grammar.

### Corollary 3.2 — matrix-ordered minimal boundary

At finite ancilla-saturated comb scope, the earned scalar minimum
\((X,e)\) has a matrix-ordered lift. Its effect system is

\[
\mathcal E(B_{\mathfrak F})
=
\operatorname{ran}e^\sharp
\]

with the inherited matrix cones and order unit. On this range,
\(e^\sharp\) is the identity.

This earns

\[
\boxed{\texttt{RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY}}
\]

only at the stated ancilla-saturated physical scope.

### 3.3 Why scalar positivity is insufficient

Let \(\tau:M_2\to M_2\) be matrix transposition and set

\[
P=\frac12(\operatorname{id}+\tau).
\]

Then \(P\) is positive, unital and idempotent:

\[
P^2=P.
\]

It is not completely positive. With the unnormalized maximally entangled
vector \(\Omega=|00\rangle+|11\rangle\), its Choi matrix is

\[
J(P)=\frac12\left(|\Omega\rangle\langle\Omega|+\mathsf F\right),
\]

where \(\mathsf F\) is the swap. On the antisymmetric vector

\[
|\psi^-\rangle
=
\frac{|01\rangle-|10\rangle}{\sqrt2},
\]

one has

\[
\langle\psi^-|J(P)|\psi^-\rangle=-\frac12.
\]

Thus a scalar ordered idempotent need not define a quantum operation. The
complete-admission gate is load bearing rather than terminological.

---

## 4. Nondisturbing repeatable instruments

For the rest of the paper, write

\[
S=\mathcal E(B_{\mathfrak F})
\]

for the matrix-ordered minimal effect boundary. Its identity process map is
denoted by \(I_S\).

### Definition 4.1 — complete classical instrument

A finite operational classical instrument on \(S\) is a family

\[
\mathcal M=\{m_r:S\to S\}_{r\in\Omega}
\]

such that:

1. every \(m_r\) is an admitted CP branch;
2. the flagged family is an admitted complete instrument;
3. forgetting the flag is nondisturbing:
   \[
   \sum_rm_r=I_S;
   \]
4. the branches are repeatable and exclusive:
   \[
   m_sm_r=\delta_{sr}m_r.
   \]

The outcome effect is

\[
q_r=m_r(1_S).
\]

It obeys

\[
q_r\geq0,
\qquad
\sum_rq_r=1_S.
\]

The associated state branch sends a state \(\rho\) to the subnormalized
state

\[
\rho_r=\rho\circ m_r.
\]

The retained outcome flag carries the finite Boolean algebra
\(\mathbb C^\Omega\). No product among the effects \(q_r\) is assumed.

### Proposition 4.2 — operational repeatability

For every state \(\rho\), performing the instrument twice gives

\[
\Pr(s\text{ second},r\text{ first}\mid\rho)
=
\delta_{sr}\rho(q_r).
\]

Forgetting either flag leaves the state of every admitted effect in \(S\)
unchanged.

**Proof.** The joint branch functional is

\[
\rho\circ m_rm_s.
\]

The branch equation gives the displayed probability. Summing either branch
index uses \(\sum_rm_r=I_S\). \(\square\)

### Definition 4.3 — operational split projection

An admitted map \(P:S\to S\) is an operational split projection when

\[
P^2=P,
\qquad
P\ \text{is CP},
\qquad
I_S-P\ \text{is CP},
\]

and \(\{P,I_S-P\}\) is an admitted flagged instrument.

Every branch of Definition 4.1 is an operational split projection, because
its complement is the sum of the other branches.

---

## 5. The split-projection theorem

The key result requires no associative multiplication.

### Lemma 5.1 — ranges are order ideals

Let \(V\) be a finite-dimensional real ordered vector space with a pointed
generating cone \(V_+\). If \(P^2=P\), \(P\geq0\), and \(I-P\geq0\), then
\(\operatorname{ran}P\) and \(\operatorname{ran}(I-P)\) are order ideals.

**Proof.** Let \(0\leq y\leq x\) with \(x\in\operatorname{ran}P\). Positivity
and order preservation give

\[
0\leq(I-P)y\leq(I-P)x=0.
\]

Hence \((I-P)y=0\), so \(y\in\operatorname{ran}P\). The complementary case
is identical. The positive cone in \(\operatorname{ran}P\) generates that
range because any \(v\in\operatorname{ran}P\) can be written

\[
v=P(a)-P(b)
\]

for positive \(a,b\in V_+\). \(\square\)

This is the finite elementary form of the general relation between order
projections and band projections [3].

### Theorem 5.2 — all operational split projections commute

Let \(P,Q:S\to S\) be operational split projections. Then

\[
PQ=QP.
\]

**Proof.** Work first on \(S_{\mathrm{sa}}\). If
\(x\in\operatorname{ran}P\) is positive, then

\[
0\leq Qx\leq x
\]

because both \(Q\) and \(I-Q\) are positive. Lemma 5.1 therefore gives

\[
Qx\in\operatorname{ran}P.
\]

Since the positive cone generates \(\operatorname{ran}P\), \(Q\) preserves
the entire range. The same argument shows that \(Q\) preserves
\(\operatorname{ran}(I-P)\). Hence \(Q\) is block diagonal with respect to

\[
S_{\mathrm{sa}}
=
\operatorname{ran}P
\oplus
\operatorname{ran}(I-P),
\]

which is equivalent to \(PQ=QP\). Complex linearity extends the equality to
\(S\). \(\square\)

### Proposition 5.3 — Boolean operations

For operational split projections \(P,Q\), define

\[
P\wedge Q=PQ,
\]

\[
P^\perp=I_S-P,
\]

and

\[
P\vee Q=P+Q-PQ.
\]

If admitted instruments are closed under sequential composition and
classical coarse-graining, all three maps are operational split projections.

**Proof.** Commutativity makes \(PQ\) idempotent. It is CP as a composition,
and

\[
I_S-PQ=(I_S-P)+P(I_S-Q)
\]

is a coarse-grained sum of CP sequential branches. Similarly,

\[
P\vee Q=P+(I_S-P)Q
\]

is CP, while

\[
I_S-(P\vee Q)=(I_S-P)(I_S-Q)
\]

is CP. The displayed decompositions also construct the retained sequential
flags required for admission. \(\square\)

### Theorem 5.4 — finite atomic operational core

Assume the admitted process law is closed under identity, sequential
composition and finite classical coarse-graining of retained instrument
outcomes. Then the set

\[
\mathfrak B_{\mathrm{op}}(S)
=
\{P:P\text{ is an operational split projection}\}
\]

is a finite Boolean algebra. Its nonzero atoms

\[
A_1,\ldots,A_N
\]

satisfy

\[
\sum_{i=1}^NA_i=I_S,
\qquad
A_iA_j=\delta_{ij}A_i.
\]

The instrument

\[
\boxed{
\operatorname{Cl}_{\mathrm{op}}(B_{\mathfrak F})
=
\{A_1,\ldots,A_N\}
}
\]

is the unique finest admitted nondisturbing repeatable classical instrument,
up to permutation of outcomes.

**Proof.** Theorem 5.2 and Proposition 5.3 give a Boolean algebra of
commuting idempotents. Every commuting family of idempotents on a
finite-dimensional vector space is simultaneously diagonalizable because
each minimal polynomial divides \(t(t-1)\). In a common eigenbasis, each
idempotent has only zero and one on the diagonal. Hence there are finitely
many such maps and the Boolean algebra is atomic.

Its atoms are pairwise disjoint and sum to the identity. They are admitted
CP branches by the closure used in Proposition 5.3, so they form a complete
flagged instrument.

For any other complete instrument \(\{m_r\}\), every branch \(m_r\) belongs
to \(\mathfrak B_{\mathrm{op}}(S)\), and therefore is the sum of precisely the
atoms below it. The instrument is consequently a unique deterministic
coarse-graining of \(\{A_i\}\). \(\square\)

### Corollary 5.5 — stochastic postprocessing adds no sharper objects

Suppose

\[
n_s=\sum_i\kappa(s\mid i)A_i
\]

for a stochastic matrix \(\kappa\), and suppose \(\{n_s\}\) is itself
exclusive and repeatable. Then every coefficient \(\kappa(s\mid i)\) is
zero or one, and each atom \(i\) is assigned to exactly one outcome \(s\).

**Proof.** From \(n_s^2=n_s\) and atomic orthogonality,

\[
\kappa(s\mid i)^2=\kappa(s\mid i)
\]

for every nonzero atom. Normalization assigns exactly one unit coefficient
per atom. \(\square\)

Thus deterministic partition is the correct refinement order for sharp
repeatable cores.

### Corollary 5.6 — symmetry covariance

Every admitted reversible complete-order automorphism \(g:S\to S\) acts by

\[
P\longmapsto gPg^{-1}
\]

on \(\mathfrak B_{\mathrm{op}}(S)\) and therefore permutes its atoms.

The core is invariant, but no atom label is selected. Physical symmetry is
retained rather than quotiented into a preferred outcome.

---

## 6. Finite \(C^*\)-algebra classification

The abstract theorem should reproduce the ordinary algebraic center only
when the corresponding physical branches are actually admitted.

### 6.1 A full matrix factor

Let \(A=M_d\) with the standard complete positive map cone. Suppose
\(P:A\to A\) and \(I-P\) are CP. In Choi form,

\[
0\leq J(P)\leq J(I).
\]

The Choi matrix of the identity channel is the rank-one operator

\[
J(I)=|\Omega_d\rangle\langle\Omega_d|,
\qquad
|\Omega_d\rangle=\sum_{j=1}^d|jj\rangle.
\]

Every positive operator dominated by a rank-one positive operator is a
scalar multiple of it. Hence

\[
J(P)=\lambda J(I),
\qquad
0\leq\lambda\leq1,
\]

so

\[
P=\lambda I.
\]

If \(P^2=P\), then \(\lambda\in\{0,1\}\).

### Proposition 6.1 — factors have trivial operational core

When every standard CP branch is admitted on \(M_d\),

\[
\operatorname{Cl}_{\mathrm{op}}(M_d)
=
\{I\}.
\]

No nontrivial classical value can be extracted repeatedly without
disturbing the full matrix factor.

### 6.2 Finite direct sums

Let

\[
A=\bigoplus_{k=1}^NM_{d_k}.
\]

Write \(z_k\) for the unit of the \(k\)-th simple summand. The standard
central branch maps are

\[
P_k(a)=z_ka.
\]

They are CP, pairwise exclusive, repeatable, and sum to the identity.

### Theorem 6.2 — recovery of the finite algebraic center

If the standard central-sector branches are admitted, then every
operational split projection on \(A\) is

\[
P_J(a)=\left(\sum_{k\in J}z_k\right)a
\]

for a unique subset \(J\subseteq\{1,\ldots,N\}\). Consequently,

\[
\operatorname{Cl}_{\mathrm{op}}(A)
=
\{P_1,\ldots,P_N\},
\]

and its flagged Boolean outcome algebra is canonically isomorphic to

\[
Z(A)=\bigoplus_{k=1}^N\mathbb Cz_k.
\]

**Proof.** The completely positive Radon--Nikodym theorem applied to
\(0\leq_{\mathrm{CP}}P\leq_{\mathrm{CP}}I\) represents \(P\) by a positive
contraction in the commutant of a minimal Stinespring representation of the
identity map. For the multiplicity-free standard representation of a finite
direct sum of factors, that commutant consists of the block scalars:

\[
P(a)=\sum_k\lambda_kz_ka,
\qquad
0\leq\lambda_k\leq1.
\]

Idempotence gives \(\lambda_k^2=\lambda_k\), so each coefficient is zero or
one. Equivalently, the same conclusion follows blockwise from the rank-one
Choi argument of Section 6.1 and positivity of the complementary map. The
atoms are the singleton blocks. \(\square\)

The theorem does not say that an abstract finite algebra center is always
physical. It assumes the corresponding central-sector instruments are
admitted.

### 6.3 The mixed control

For

\[
A=M_2\oplus\mathbb C,
\]

the operational core has two atoms when both central-sector branches are
admitted. The qubit block remains irreducibly quantum; only the block label is
classical.

---

## 7. Koashi--Imoto and nondisturbing accessibility

### 7.1 Finite minimal state experiments

For a finite family of density operators, restrict first to their joint
support. Its minimal sufficient Koashi--Imoto form is

\[
H
\simeq
\bigoplus_r H_r^Q\otimes H_r^N,
\]

\[
\rho_\theta
\simeq
\bigoplus_r
p(r\mid\theta)\,
\rho_{\theta,r}^Q\otimes\omega_r^N.
\]

The minimal sufficient observable algebra is

\[
M_{\min}
\simeq
\bigoplus_rB(H_r^Q)\otimes I_{H_r^N}.
\]

Its central block label \(r\) carries the classical information, the
\(H_r^Q\) factors carry irreducibly quantum parameter dependence, and the
\(H_r^N\) factors are parameter-independent redundant structure [4,5].

### Theorem 7.1 — state-experiment recovery

In the standard finite quantum channel category, where every central-sector
nondemolition instrument of \(M_{\min}\) is admitted,

\[
\operatorname{Cl}_{\mathrm{op}}(M_{\min})
\]

is exactly the finite classical experiment

\[
\theta\longmapsto(p(r\mid\theta))_r.
\]

**Proof.** Theorem 6.2 identifies the atomic operational branches with the
minimal central projections of \(M_{\min}\). Evaluating those branches in
\(\rho_\theta\) gives \(p(r\mid\theta)\). No branch resolves the quantum
state inside \(H_r^Q\), and the redundant factor has already disappeared
from the minimal algebra. \(\square\)

Kuramochi proves in the von Neumann-algebraic state setting that information
accessible without disturbing a minimal sufficient experiment is bounded by
this classical part [5]. The present theorem agrees with that result where
the process boundary is already an observable algebra. Our new statement is
different in scope: before any algebra is known, the operational split
instrument itself defines the classical core.

### 7.2 The classical, mixed and quantum controls

For \(\mathbb C^n\), the core has \(n\) atoms and retains the whole
classical sample space.

For \(M_2\oplus\mathbb C\), the core has two atoms but retains the full
qubit process inside the first sector.

For two distinct nonorthogonal pure qubit states whose minimum is \(M_2\),
the core is trivial even though the minimal boundary is nontrivial. Minimal
future information need not contain classical information.

---

## 8. The hostile operator-system discriminator

Let

\[
S
=
\operatorname{span}_{\mathbb C}
\{s_0,s_1,s_2\}
\subset M_2\oplus M_2,
\]

where

\[
s_0=(I,I),
\qquad
s_1=(Z,Z),
\qquad
s_2=(X,2X+Z).
\]

### 8.1 Its algebraic envelope

One has

\[
s_2^2=(I,5I).
\]

Therefore the generated algebra contains

\[
z_1=\frac{5s_0-s_2^2}{4}=(I,0),
\qquad
z_2=\frac{s_2^2-s_0}{4}=(0,I).
\]

Multiplying by these central projections separates the Pauli generators in
the two blocks, so

\[
C^*(S)=M_2\oplus M_2.
\]

Neither simple summand can be removed by a boundary quotient. Deleting the
second block lowers

\[
\|s_2\|=\sqrt5
\]

to \(1\). Deleting the first block lowers the norm of

\[
-3s_1+s_2=(X-3Z,2X-2Z)
\]

from \(\sqrt{10}\) to \(\sqrt8\). Hence

\[
C_e^*(S)=M_2\oplus M_2.
\]

But

\[
S\cap Z(M_2\oplus M_2)=\mathbb C(I,I).
\]

Indeed, a general element

\[
\alpha s_0+\beta s_1+\gamma s_2
\]

is scalar in both blocks only when \(\beta=\gamma=0\).

### 8.2 Complete-order decompositions force an internal central effect

### Lemma 8.1 — a split operator system decomposes its envelope

If \(P:S\to S\) and \(I-P\) are CP projections, then

\[
\Phi:S\longrightarrow
\operatorname{ran}P\oplus\operatorname{ran}(I-P),
\qquad
\Phi(s)=(P(s),(I-P)(s)),
\]

is a unital complete order isomorphism, where the summand order units are
\(P(1)\) and \((I-P)(1)\).

**Proof.** Both coordinate maps are CP. The inverse is addition, which is CP
at every matrix level on the direct-sum cone. The two composites are the
identities. \(\square\)

The \(C^*\)-envelope preserves this direct sum. Consequently, a nontrivial
split makes \(P(1)\) a nontrivial central projection of \(C_e^*(S)\) that is
already an element of \(S\).

### Theorem 8.2 — the envelope-center false positive is rejected

For the displayed hostile operator system,

\[
\operatorname{Cl}_{\mathrm{op}}(S)=\{I_S\}.
\]

**Proof.** If a nontrivial split \(P\) existed, Lemma 8.1 would make
\(P(1)\) a nontrivial element of

\[
S\cap Z(C_e^*(S)).
\]

That intersection contains only scalar multiples of the unit. Write
\(P(1)=\lambda1\). Idempotence gives

\[
P(P(1))=P(1)
\quad\Longrightarrow\quad
\lambda^2=\lambda.
\]

If \(\lambda=0\), positivity and the order-unit property force \(P=0\). If
\(\lambda=1\), the same argument forces \(I-P=0\). Thus the split is
trivial. \(\square\)

The algebraic projections \((I,0)\) and \((0,I)\) exist only after
multiplicative closure. They are not effects in \(S\), and no complete
instrument on \(S\) reads them. The operational core therefore gives the
required answer without pretending that the envelope center is physical.

### 8.3 Direct state witness

Let \(\operatorname{tr}_2\) be normalized trace and define

\[
\varphi_\lambda(a,b)
=
\lambda\operatorname{tr}_2(a)
+(1-\lambda)\operatorname{tr}_2(b).
\]

Every \(\varphi_\lambda\) restricts to the same state on \(S\):

\[
\varphi_\lambda(s_0)=1,
\qquad
\varphi_\lambda(s_1)=0,
\qquad
\varphi_\lambda(s_2)=0.
\]

Yet

\[
\varphi_\lambda(z_1)=\lambda.
\]

This makes the operational point transparent: the envelope block weight is
not determined by any effect of \(S\).

---

## 9. Physical admission and symmetry controls

### 9.1 Algebraically available but physically unavailable

Take the abstract algebra \(A=\mathbb C^2\), but let the admitted process
law contain only the identity deterministic map, its zero branch, and the
trivial one-outcome flag. Suppose the two coordinate filters are not admitted
operations.

Mathematically, \(A\) has two central projections. Operationally,

\[
\mathfrak B_{\mathrm{op}}(A)=\{0,I\},
\]

so the physical core is trivial.

If the law is enlarged by admitting the two coordinate branches, the core
becomes the two-atom instrument. Thus admission is measured rather than
inferred from algebraic existence.

### 9.2 Closure is physically load bearing

Suppose a laboratory advertises two complete split instruments but refuses
every sequential composition of their branches. The mathematical order
projections still commute, but their common refinement need not belong to the
advertised grammar. Two incomparable maximal instruments may then remain.

Theorem 5.4 therefore requires operational-category closure under sequential
composition and retained classical coarse-graining. This is not a technical
convenience: it is the physical experiment that constructs the common
refinement.

### 9.3 Symmetric sectors

For \(\mathbb C\oplus\mathbb C\) with the full standard law, let
\(g\) swap the two summands. The core has two atoms \(A_0,A_1\) and

\[
gA_0g^{-1}=A_1.
\]

The unordered two-outcome instrument is canonical. Neither outcome is
preferred. If one later needs token identity, the symmetry must remain as a
groupoid action rather than being broken by a lexical label.

---

## 10. Corrected branch-memory controls

This section uses only the immutable corrected task minima. It does not
recompute or modify the predecessor process law.

### 10.1 Complete weighted branches

Each source branch \(j\in\{0,1,2,3\}\) has success weight \(1/4\) and a
common failure sink of weight \(3/4\). The deterministic representation is

\[
\widehat x_j
=
\frac14|1\rangle\langle1|\otimes\bar x_j
+
\frac34|0\rangle\langle0|\otimes\omega_{\mathrm{sink}}.
\]

The sink is retained throughout. Conditioning on success is forbidden.

### 10.2 Preserving future

The preserving future gives the same complete distribution for every
source branch. Its minimum is

\[
M_{\mathrm{pres}}=\mathbb C.
\]

Therefore

\[
\operatorname{Cl}_{\mathrm{op}}(M_{\mathrm{pres}})
\]

is the trivial one-atom instrument. No record of \(j\) is present in this
task minimum.

### 10.3 Eraser future

The complete eraser distributions are

\[
q_j(\bot)=\frac34,
\qquad
q_j(k)=\frac14\delta_{jk}
\]

on the five-point alphabet

\[
\{\bot,0,1,2,3\}.
\]

Their minimum is

\[
M_{\mathrm{erase}}=\mathbb C^5.
\]

With all standard classical filters admitted, its operational core has five
atoms. It is the fine eraser outcome plus failure, not one of the inherited
coarse memory seams.

The common sink cannot be removed by Blackwell recovery. On a failure event,
no parameter-independent map can reconstruct the unknown label \(j\).

### 10.4 Retained tomographic future

For a tomographically separating success family with the same retained sink,
the corrected minimum is

\[
M_{\mathrm{tomo}}=M_4\oplus\mathbb C.
\]

Its standard operational core has two atoms:

\[
\text{success},
\qquad
\text{failure}.
\]

For every source label \(j\), their distribution is

\[
\left(\frac14,\frac34\right).
\]

Hence this classical core is not correlated with \(j\). The full success
sector contains the branch dependence quantum mechanically, while the only
nondisturbing classical label says whether the preparation succeeded.

### Proposition 10.1 — no branch-memory seam selection

Under the three independently fixed corrected future tasks, the operational
cores are respectively:

\[
\boxed{
\mathbb C,
\qquad
\mathbb C^5,
\qquad
Z(M_4\oplus\mathbb C)\simeq\mathbb C^2.
}
\]

None selects the familiar memory PVM, any of the nine inherited partition
seams, or the additional complex seam.

**Proof.** The first is trivial. The second resolves the complete five-point
classical task rather than a chosen coarse partition. The third distinguishes
only success from failure, and that distribution is independent of the
source label. \(\square\)

This is not a failure of the operational-core theorem. It confirms the
separate task-selection obstruction: different future experiments can have
different physically readable classical cores without one being the
task-independent W3 boundary.

---

## 11. Relation to existing nondisturbance theorems

Koashi and Imoto classify finite-dimensional degrees of freedom into
classical, quantum and redundant sectors for a specified family of states
[4]. Kuramochi constructs a minimal sufficient experiment on a von Neumann
algebra and defines its classical part by restriction to the center [5,6]. He
proves that no more information than this classical part can be extracted by
the relevant nondisturbing CP or Schwarz channels.

Those results presuppose an operator algebra. The present construction does
not. Its starting point is the matrix-ordered effect system of a process
boundary, and its primary classical object is a flagged family of admitted
CP maps.

When the effect system is a finite \(C^*\)-algebra and all standard sector
instruments are admitted, Theorem 6.2 makes the two notions coincide. When
the effect system lacks an internally readable algebraic center, Theorem 8.2
returns the trivial core rather than importing the center of an envelope.

Effect-theoretic reconstruction results show that stronger operational
axioms involving filters, compressions, purity, dagger structure and
monoidal composition can recover Jordan or \(C^*\)-algebraic models [7]. No
such reconstruction is assumed here. The split-instrument theorem isolates
the classical direct-sum content available before those stronger axioms.

---

## 12. Four-gate audit

| Object | Referent | Necessity | No-smuggling | Discriminator |
|---|---|---|---|---|
| ancillary matrix tester | admitted coherent reference-assisted closed experiment | scalar positivity is weaker than CP | tester doctrine fixed before inspecting a core | transpose symmetrizer passes scalar positivity and fails level two |
| matrix-ordered effect dual | complete tester-visible effects of the minimum | CP instruments require matrix cones | no multiplication or PVM is inserted | reversible presentations give complete-order isomorphisms |
| split projection | one complete two-outcome admitted process instrument | physical classical information must be readable and repeatable | both branches and retained flag are operational data | factor versus direct-sum controls |
| operational core | atoms of all admitted split projections | removes arbitrary choice among readable instruments | built without a candidate record algebra | hostile operator system is trivial while a readable direct sum is not |

The complete-admission and sequential-instrument closures are explicit
operational postulates. They are candidate-independent and have direct
negative controls. The theorems derive their consequences rather than
conceal them.

---

## 13. Classification of statements

### 13.1 Definitions

- complete ancillary tester kernel;
- matrix-ordered operational effect dual;
- complete lift of a process idempotent;
- nondisturbing repeatable classical instrument;
- operational split projection;
- refinement by retained classical postprocessing; and
- operational classical core.

### 13.2 New theorems proved here

1. complete admitted tester effects form an operator system at finite
   Archimedean scope;
2. deterministic process maps pull effects back by UCP maps;
3. the exact complete-kernel criterion characterizes lift of the scalar
   Karoubi idempotent;
4. ranges of complementary positive projections are order ideals;
5. every pair of operational split projections commutes;
6. instrument closure makes the split projections a finite Boolean algebra;
7. the Boolean atoms form the unique finest nondisturbing repeatable
   instrument;
8. sharp repeatable stochastic postprocessings reduce to deterministic
   partitions;
9. finite \(C^*\)-algebras recover precisely their admitted central-sector
   instruments;
10. standard finite minimal state experiments recover their
    Koashi--Imoto classical part;
11. the hostile operator system has a trivial operational core; and
12. the corrected branch-memory tasks select no inherited seam.

### 13.3 Inherited theorems

- finite-dimensional abstract operator-system representation [1];
- matrix-ordered duality for finite operator systems [1,2];
- order projections as bands in generating ordered spaces [3];
- Koashi--Imoto state decomposition [4];
- minimal sufficient operator-algebraic experiments [5]; and
- nondisturbingly accessible information is bounded by the classical part
  in the von Neumann-algebraic state setting [6].

### 13.4 Postulates

- physical admission of the chosen ancillary tester levels;
- ancilla saturation where the positive first rung is claimed;
- closure of admitted instruments under sequential composition; and
- closure under retained finite classical coarse-graining.

### 13.5 Open obligations

- deriving rather than declaring the physically admissible future task;
- finding a task--record fixed point resistant to the task-smuggling theorem;
- upgrading a nontrivial core to an independently controllable autonomous
  process chart;
- deriving physical overlaps between independently recovered charts; and
- every topological, causal, field-theoretic and gravitational successor.

---

## 14. Outcome audit

### `RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY`

**Provisionally earned at finite ancilla-saturated scope.** Complete tester
effects define an operator system, and an admitted completely idempotent
minimum induces a UCP idempotent on the dual. Proposition 3.1 states the
exact compatibility gate; the transpose symmetrizer proves that scalar
positivity alone is insufficient.

### `RQ0-L0-OPERATIONAL-CLASSICAL-CORE`

**Provisionally earned at finite instrument-complete scope.** Theorem 5.4
constructs the unique finest admitted nondisturbing repeatable instrument up
to permutation. Its outcome effects and postmeasurement branches are
physical. The core may be trivial.

### `RQ0-L0-BLOCKED-AT-OPERATIONAL-CENTER`

**Not selected at the declared positive scope.** It remains the required
outcome for any law lacking complete-kernel compatibility, admitted
instrument closure, or the physical branches needed by the construction.

No W3 rung is registered.

---

## 15. Physical meaning and limits

The result can be said without operator-algebra terminology:

> Once a future experiment has been compressed to its smallest repeatable
> quantum-process interface, collect every physical yes/no reading that can
> be performed repeatedly while leaving that whole interface unchanged.
> These readings are automatically compatible. Performing all of them gives
> one finest classical label—the operational classical core.

The theorem explains why a full quantum factor has no such nontrivial label
and why a genuine direct sum does. It also explains why an abstract center
outside the admitted effect system is physically irrelevant.

It does not explain why the future-task family was chosen. The inherited
task-smuggling theorem remains untouched. Therefore the core is not yet a
W3 record boundary, and certainly not a local region.

The current logical chain is only

\[
\boxed{
\text{fixed future task}
\longrightarrow
\text{minimal sufficient process boundary}
\longrightarrow
\text{maximal nondisturbing classical instrument}.
}
\]

The missing next arrow would have to determine the task and record together,
without feeding either one in as the answer. That successor is not attempted
here.

---

## 16. Claim ceiling

This paper makes no claim of:

- actual outcome selection;
- W6 fact co-reference or event-token identity;
- task-independent W3 stability;
- autonomous subsystem control;
- an intrinsic quantum chart;
- a physical overlap or atlas;
- topology or manifold structure;
- influence or causal order;
- Lorentzian spacetime;
- quantum field theory, QCD or gravity.

The term “boundary” means a one-chart task-relative process interface. The
term “classical” means a retained outcome of a complete nondisturbing
repeatable instrument.

---

## 17. Conclusion

The center-lift obstruction can be resolved without inventing a product.
Ancilla-complete testers give the minimum process boundary an operational
matrix order. Within that order, physically nondisturbing repeatable
instruments are exactly finite partitions by CP order projections. Those
projections commute and form a finite Boolean algebra; its atoms define a
canonical finest physical classical instrument.

The construction agrees with ordinary central decomposition where central
instruments are physically available, and it refuses an unreadable center
where they are not. Its most important negative result is equally clear:
the corrected branch-memory future tasks still do not select a W3 seam.

Thus the finite result is

\[
\boxed{
\begin{array}{c}
\text{a matrix-ordered minimal quantum boundary exists at complete scope},
\\[1mm]
\text{and its maximal physically nondisturbing classical instrument is
canonical},
\\[1mm]
\text{but it remains relative to the chosen future task and is not locality.}
\end{array}}
\]

---

## References

1. M.-D. Choi and E. G. Effros, “Injectivity and operator spaces,” *Journal
   of Functional Analysis* **24** (1977), 156–209.
   https://doi.org/10.1016/0022-1236(77)90052-0
2. W. H. Ng, “Matrix-ordered duals of separable operator systems and
   projective limits,” arXiv:1803.01758 (2018).
   https://arxiv.org/abs/1803.01758
3. J. Glück, “A short note on band projections in partially ordered vector
   spaces,” arXiv:1807.01003 (2018).
   https://arxiv.org/abs/1807.01003
4. M. Koashi and N. Imoto, “Operations that do not disturb partially known
   quantum states,” *Physical Review A* **66** (2002), 022318.
   https://arxiv.org/abs/quant-ph/0101144
5. Y. Kuramochi, “Minimal sufficient statistical experiments on von Neumann
   algebras,” *Journal of Mathematical Physics* **58** (2017), 062203.
   https://doi.org/10.1063/1.4986247
6. Y. Kuramochi, “Accessible information without disturbing partially known
   quantum states on a von Neumann algebra,” *International Journal of
   Theoretical Physics* **57** (2018), 2249–2266.
   https://doi.org/10.1007/s10773-018-3749-8
7. J. van de Wetering, “An effect-theoretic reconstruction of quantum
   theory,” *Compositionality* **1** (2019), 1.
   https://arxiv.org/abs/1801.05798
