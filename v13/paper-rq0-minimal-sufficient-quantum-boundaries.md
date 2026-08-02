# Minimal Sufficient Quantum Boundaries

## W3 Records, Process Experiments, and the Classical Center of the Future

**Version:** v0.1

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-01

**Governing pin:** `9344434`

**Scope:** finite-dimensional, exact, analytical RQ0-L0 inside one
operational chart

---

## Abstract

The previous RQ0-L0 construction made W3 operationally complete: writing,
preservation, erasure, and no-write are comparisons of complete quantum
combs under admitted complete testers. That construction did not select one
record interface. Several inequivalent projector families passed the same
nonseparating experiment. This paper tests a stronger selection principle:
a boundary should be the least process interface through which all
future-task-relevant dependence on the operational past factors.

For a typed cut $c$ in one finite operational chart and an independently
fixed future-task family $\mathfrak F$, every complete admitted past
instrument $\theta$ induces a conditional future comb
$F_{c,\mathfrak F,\theta}$. The family

$$
\mathsf E_{c,\mathfrak F}
=
(X_{c,\mathfrak F},\Theta_c,
  (F_{c,\mathfrak F,\theta})_{\theta\in\Theta_c})
$$

is a process statistical experiment. One experiment simulates another only
when one parameter-independent admitted deterministic superchannel maps the
whole first family to the whole second family.

At finite-dimensional compact-convex scope we prove a process-level minimal
sufficiency theorem. In the Karoubi completion of the admitted process
category, every finite experiment has a minimal sufficient process retract,
unique up to reversible operational equivalence. The proof uses a
minimum-rank idempotent in the stabilizer semigroup and a finite-dimensional
mean-ergodic argument. This is not obtained by treating normalized Choi
operators as arbitrary states.

The proposed next step does **not** follow. A minimal process retract is only
an idempotent-split operational object. It need not possess an intrinsic
multiplication, a canonical center, or an admitted central readout. Two exact
counterexamples isolate the obstruction. First, unitary swap of the two
factors of a normalized qubit Choi state is a reversible state operation and
fixes the identity-channel state, but it fails the channel normalization
constraint on a generic replacer channel and therefore is not a
superchannel. Second, an explicit operator system generates
$M_2\oplus M_2$ as its $C^*$-envelope while containing neither of the two
central block projectors as an operational effect. An algebraic center is not
automatically a physical record interface.

There is a second, downstream obstruction. For any desired finite PVM, one
can choose a dephasing future task whose minimal sufficient state algebra has
exactly that PVM algebra as its center. Unless future tasks are fixed
independently, center extraction simply moves the planted answer from the
record input into the task input.

The branch-memory model makes the point sharply. Its frozen preserving
terminal task erases all dependence on the four source labels, so its minimal
experiment is trivial. Its eraser-terminal task perfectly recovers the four
labels, so its minimum is the fine four-point classical experiment. A
tomographically complete retained-quantum task instead has full matrix
algebra and trivial center. None selects the inherited nine coarse seams or
the additional complex seam. Candidate-matched dephasing tasks can select
any of them, but only circularly.

The strongest provisional cumulative result is therefore

$$
\boxed{
\texttt{RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY}
}
$$

through `RQ0-L0-FUTURE-EXPERIMENT`, at finite-dimensional,
tester-quotiented, compact-convex, idempotent-completed one-chart scope. The
first registered obstruction is

$$
\boxed{
\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.
}
$$

No actual outcome, fact co-reference, autonomous subsystem, spatial
locality, overlap, topology, causal order, field, or gravity claim is made.

---

## 1. Question, result, and ontology firewall

### 1.1 The selection problem

The complete-comb W3 criterion answers a conditional question:

> Given a typed cut, a candidate record action, and admitted future
> experiments, does that record behave classically under one continuation
> while recoverable coherence remains under another?

It does not answer:

> Why is this record action the physically relevant interface rather than
> another W3-positive action?

The branch-memory experiment exposed that gap. Nine inherited partition
records survived complete tester analysis, and a hostile review constructed
an additional exact complex rank-two record. A larger catalogue or a better
sheaf would retain the ambiguity but would not select a boundary.

This paper tests a different principle:

$$
\boxed{
\text{the physical boundary is a minimal sufficient experiment for a
declared family of future tasks.}
}
$$

The principle asks what information about the operational past must cross a
typed cut in order to reproduce every future process in the declared task
class. It does not begin with a PVM.

### 1.2 The result in one sentence

A minimal sufficient **process retract** exists and is unique at a precise
finite convex scope, but its classical center is not intrinsically defined
or physically readable in general. Minimal sufficiency solves redundancy;
it does not by itself solve classical-record selection.

### 1.3 One chart only

Every object below belongs to one finite operational chart $D$.

- A cut is a declared laboratory composition boundary in $D$.
- A past instrument closes ports before that cut.
- A future task acts only on the exposed future profile in $D$.
- A tester is complete only relative to the admitted law of $D$.
- A minimum is taken only among process maps admitted in $D$.

There is no atlas-wide tester, global state, global event set, or global
present. “Past” and “future” name the typed order of a laboratory comb. They
do not denote an already derived relativistic causal order.

### 1.4 What is and is not primitive

The primitive one-chart law supplies:

1. typed finite-dimensional process profiles;
2. a complete process tensor or comb at each eligible cut;
3. complete admitted past instruments;
4. independently declared complete future-task families;
5. admitted deterministic superchannels and complete testers; and
6. presentation gauge and physical symmetries.

It does **not** supply a record PVM, a seam label, a desired factor, a center,
or a classification of a task as “preserving” because it preserves a center
found later.

### 1.5 Registered outcome

The paper provisionally earns

$$
\texttt{RQ0-L0-FUTURE-EXPERIMENT}
$$

and

$$
\texttt{RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY}
$$

at the scope stated below. It does not earn
`RQ0-L0-CANONICAL-CLASSICAL-CENTER` or
`RQ0-L0-W3-MARKOV-BOUNDARY`. The first obstruction is
`RQ0-L0-BLOCKED-AT-CENTER-LIFT`.

All status is `GREEN-UNREVIEWED` until the three prescribed mathematical
reviews are frozen and jointly adjudicated.

---

## 2. Process experiments at a typed cut

### 2.1 Operational quotient inherited from complete-comb W3

For a process profile $\tau$, let $K_\tau$ be the compact convex set of
deterministic finite-dimensional combs of that type. Let $V_\tau$ be the
real linear span of their Hermitian Choi representatives. The admitted
complete tester family defines

$$
\|x\|_{\mathsf{Test}_D,\tau}
=
\sup_{T\in\mathsf{Test}_D(\tau)}
\|p_T(x)\|_1.
$$

Its kernel consists of process differences invisible to every admitted
closed experiment of that type. We work from the outset in

$$
\overline V_\tau
=
V_\tau/\ker\|\cdot\|_{\mathsf{Test}_D,\tau}.
$$

An admitted superchannel must preserve operational kernels and therefore
descend to a linear map between these quotients. Dormant Choi coefficients
have no role in the construction.

### 2.2 Complete past parameters

Fix an eligible cut $c$ with exposed cut type $\tau_c$. A parameter
$\theta\in\Theta_c$ is normally a **complete past instrument setting**, not
a normalized postselected state. If that setting has CP branches
$\{\mathcal P_{\theta,a}\}_a$, the branch weights, outcome flag $a$, and
conditional quantum output are retained together as the deterministic
flagged channel

$$
\widehat{\mathcal P}_\theta(\rho)
=
\sum_a
|a\rangle\langle a|_{A_\theta}
\otimes
\mathcal P_{\theta,a}(\rho).
$$

The sum over $a$ is trace preserving. The displayed flag is the physical
outcome of that instrument, not a free copy of the externally chosen setting
label $\theta$. Linking
$\widehat{\mathcal P}_\theta$ into the prefix of the chart gives one
deterministic cut process $s_{c,\theta}\in K_{\tau_c}$. Consequently two
source instruments having the same normalized conditional states but
different branch weights remain different whenever the flag is accessible.

When individual subnormalized branches are used as parameters, write a
branch as $x_\theta=p_\theta\bar x_\theta$ and embed it in one common
deterministic type by

$$
\widehat x_\theta
=
p_\theta|1\rangle\langle1|\otimes\bar x_\theta
+
(1-p_\theta)|0\rangle\langle0|\otimes\omega_{\mathrm{sink}},
$$

with the same declared sink process for every $\theta$. This flag records
success versus complement; it does not reveal the external parameter label.
It retains $p_\theta$ without dividing it away. Future maps act on the
success branch, and any admitted feed-forward from the success flag must be
declared explicitly.

### 2.3 Bundled future tasks

A future-task family $\mathfrak F$ is a finite complete family of admitted
instruments and adaptive tails that acts after $c$. When its members have
different output profiles, attach a classical task flag and use the typed
direct sum of the output systems. This produces one deterministic controlled
superchannel

$$
L_{c,\mathfrak F}:\tau_c\longrightarrow\tau_{c,\mathfrak F}.
$$

The conditional future process is

$$
F_{c,\mathfrak F,\theta}
=
L_{c,\mathfrak F}(s_{c,\theta}).
$$

All members therefore have one displayed type and remain deterministic
flagged combs. The process experiment at $(c,\mathfrak F)$ is

$$
\boxed{
\mathsf E_{c,\mathfrak F}
=
\left(
X_{c,\mathfrak F},
\Theta_c,
(F_{c,\mathfrak F,\theta})_{\theta\in\Theta_c}
\right),
}
$$

where $X_{c,\mathfrak F}$ denotes the operational process object of the
common output type.

### Proposition 2.1 — typed future-experiment construction

For every declared cut and future-task family satisfying the preceding
completeness and common-output conditions,
$\mathsf E_{c,\mathfrak F}$ is a finite operational statistical experiment
in the quotient process theory. It retains all source weights, instrument
outcomes, disturbances, output types, and tester-visible process data.

**Proof.** Every complete past setting is a deterministic flagged comb.
Linking deterministic combs is deterministic. The controlled task family is
a deterministic superchannel into a tagged common codomain. Its action
therefore gives one deterministic process of that codomain for every
$\theta$. Quotienting by the tester kernel identifies exactly the differences
that no admitted complete experiment can detect. No normalization or branch
information is discarded. $\square$

### 2.4 Presentation covariance

Let $U:X\to X'$ be a reversible admitted presentation superchannel, with
inverse $U^{-1}$. It may implement a typed basis change, Choi-convention
change, complete Kraus re-presentation, or outcome-handle permutation. It
transports the whole family by

$$
(x_\theta)_\theta
\longmapsto
(Ux_\theta)_\theta.
$$

Every construction below is expressed through composition, equality in the
operational quotient, compact convex hom-sets, and reversible conjugation.
It is therefore covariant under this transport. A physical symmetry need not
be quotiented: it acts on the resulting equivalence class and its
automorphism group remains visible.

### 2.5 First rung

Proposition 2.1 supplies the exact referent required for

$$
\boxed{\texttt{RQ0-L0-FUTURE-EXPERIMENT}.}
$$

It is a task-relative process experiment, not a local region.

---

## 3. Simulation, sufficiency, and operational deficiency

### 3.1 The process category

For the central theorem, fix a finite-dimensional category
$\mathsf{Proc}_D$ with the following hypotheses.

1. Each object $X$ is represented by a compact convex deterministic base
   $K_X$ spanning a finite-dimensional real vector space $V_X$.
2. A morphism $\Gamma:X\to Y$ is an admitted deterministic superchannel,
   represented by a linear map $V_X\to V_Y$ taking $K_X$ into $K_Y$.
3. Every hom-set is nonempty when required, compact, and convex; classical
   randomization of admitted controls is admitted.
4. Identities and compositions are admitted, and composition is continuous
   and bilinear on the linear representatives.
5. Morphisms contract the declared tester norms.
6. Operational kernels have already been quotiented, as in Section 2.1.

The standard finite-dimensional category of all deterministic combs of
specified profiles and all deterministic superchannels between them obeys
these hypotheses. A restricted laboratory theory obeys them only if its
admitted control sets are closed and convex. The theorem below is not claimed
for a nonclosed or nonconvex grammar.

### 3.2 Exact simulation

Let

$$
\mathsf E=(X,\Theta,(x_\theta)_\theta),
\qquad
\mathsf G=(Y,\Theta,(y_\theta)_\theta)
$$

have the same finite parameter set. Define

$$
\mathsf E\succeq_D\mathsf G
$$

when there is one admitted morphism $\Gamma:X\to Y$ such that

$$
\Gamma x_\theta=y_\theta
\qquad\text{for every }\theta\in\Theta.
$$

The map may not depend on $\theta$. Reflexivity follows from the identity;
transitivity follows from composition. Exact equivalence
$\mathsf E\simeq_D\mathsf G$ is mutual simulation.

An admitted decision map $Q:Y\to Z$ preserves the preorder:

$$
\mathsf E\succeq_D\mathsf G
\quad\Longrightarrow\quad
Q\mathsf E\succeq_DQ\mathsf G,
$$

because $Q\Gamma$ is admitted. Reversible presentation maps give equivalence.

### 3.3 Sufficiency

A coarse-graining $\Gamma:X\to Y$ is sufficient for $\mathsf E$ when an
admitted recovery $R:Y\to X$ obeys

$$
R\Gamma x_\theta=x_\theta
\qquad\forall\theta.
$$

Thus $\Gamma\mathsf E$ and $\mathsf E$ are operationally equivalent. The
entire conditional future processes are recovered; agreement of one terminal
probability table is not enough.

### 3.4 Deficiency

For compatible experiment types define

$$
\delta_D(\mathsf E\Vert\mathsf G)
=
\min_{\Gamma\in\mathsf{Proc}_D(X,Y)}
\max_{\theta\in\Theta}
\|\Gamma x_\theta-y_\theta\|_{\mathsf{Test}_D}.
$$

The minimum is attained because the hom-set is compact and the objective is
continuous. Exact simulation implies zero deficiency. Conversely, zero
deficiency gives an exact simulator because the minimum is attained.

### Proposition 3.1 — finite convex randomization formula

Let $V_Y^*$ carry the dual tester norm and define the compact convex
$\ell^1$-sum ball

$$
\mathcal B_1
=
\left\{
(g_\theta)_{\theta\in\Theta}:
g_\theta\in V_Y^*,\quad
\sum_\theta\|g_\theta\|_*
\le 1
\right\}.
$$

Then

$$
\begin{aligned}
\delta_D(\mathsf E\Vert\mathsf G)
=
\max_{(g_\theta)\in\mathcal B_1}
\left[
\sum_\theta g_\theta(y_\theta)
-
\max_{\Gamma\in\mathsf{Proc}_D(X,Y)}
\sum_\theta g_\theta(\Gamma x_\theta)
\right].
\end{aligned}
$$

In particular, positive deficiency has a finite operationally separated
decision-functional witness.

**Proof.** For $z_\theta=y_\theta-\Gamma x_\theta$,

$$
\max_\theta\|z_\theta\|
=
\max_{(g_\theta)\in\mathcal B_1}
\sum_\theta g_\theta(z_\theta).
$$

The domains are compact convex and the displayed expression is affine and
continuous in each variable. Finite-dimensional minimax interchanges the
minimum over $\Gamma$ with the maximum over $g$. Taking the minimum of the
negative $\Gamma$ term gives the stated formula. Equivalently, every
nonzero $g_\theta$ may be written
$g_\theta=\lambda_\theta f_\theta$ with
$\lambda_\theta=\|g_\theta\|_*$ and $\|f_\theta\|_*=1$; unused $\ell^1$
weight may be assigned to a zero functional. $\square$

When the tester norm is generated by the balanced convex hull of admitted
complete outcome evaluations, the $g_\theta$ are weighted signed,
classically flagged
decision tests. In the unrestricted channel/comb categories, stronger
complete randomization criteria are established in channel comparison
theory. Proposition 3.1 is the exact convex statement needed here; it does
not enlarge the admitted tester law.

---

## 4. A minimal sufficient process boundary

### 4.1 Why the Karoubi completion is required

An idempotent deterministic superchannel

$$
e:X\longrightarrow X,
\qquad e^2=e,
$$

need not have a range that is already one of the declared ordinary comb
types. The Karoubi completion $\operatorname{Kar}(\mathsf{Proc}_D)$ has
objects $(X,e)$ and morphisms

$$
f:(X,e)\longrightarrow(Y,d)
\quad\text{such that}\quad
f=dfe.
$$

The identity on $(X,e)$ is $e$. This object is a repeatable operational
coarse-graining. It is not automatically an algebra, tensor factor,
autonomous subsystem, or spatial region.

### 4.2 Stabilizer semigroup

For a finite experiment $\mathsf E=(X,\Theta,(x_\theta))$, define

$$
\mathsf{Stab}(\mathsf E)
=
\{a\in\mathsf{Proc}_D(X,X):a x_\theta=x_\theta\ \forall\theta\}.
$$

It is a compact convex subsemigroup containing $1_X$. Hence it contains
idempotents. Choose an idempotent $e\in\mathsf{Stab}(\mathsf E)$ of minimum
linear rank on $V_X$.

The experiment points lie in $\operatorname{ran}e$, so they define an
experiment

$$
\mathsf M_e
=
((X,e),\Theta,(x_\theta)_\theta)
$$

in the Karoubi completion.

### Lemma 4.1 — rigidity of a minimum-rank stabilizer retract

Every endomorphism $f:(X,e)\to(X,e)$ satisfying
$f x_\theta=x_\theta$ for all $\theta$ equals the identity $e$.

**Proof.** The morphism relation gives $f=efe$. Every power $f^n$ is an
admitted endomorphism of $(X,e)$ and fixes all $x_\theta$. The compactness of
the hom-set, or equivalently tester-norm contraction in finite dimension,
makes $(f^n)$ power bounded. Therefore the Cesàro averages

$$
A_N=\frac1N\sum_{n=1}^N f^n
$$

converge to the mean-ergodic projection $p$ onto the fixed space of $f$ in
$\operatorname{ran}e$. Closedness and convexity of the hom-set imply that
$p$ is admitted. It obeys

$$
p^2=p,
\qquad
p= epe,
\qquad
p x_\theta=x_\theta.
$$

Thus $p$ is a stabilizing idempotent. If $f\ne e$, then $f$ is not the
identity on $\operatorname{ran}e$, so its fixed space is a proper subspace of
$\operatorname{ran}e$. Hence $\operatorname{rank}p<\operatorname{rank}e$,
contradicting the choice of $e$. Therefore $f=e$. $\square$

### Theorem 4.2 — finite minimal sufficient process boundary

Under the hypotheses of Section 3.1, every finite process experiment
$\mathsf E$ has a minimal sufficient representative $\mathsf M_e$ in
$\operatorname{Kar}(\mathsf{Proc}_D)$. It has the following properties.

1. $\mathsf M_e\simeq_D\mathsf E$.
2. $\mathsf M_e$ is a retract of every sufficient representative of
   $\mathsf E$.
3. Every endomorphism of $\mathsf M_e$ fixing the parameter processes is its
   identity.
4. Any two representatives with these properties are reversibly
   operationally equivalent.

**Proof.** The maps $e:X\to(X,e)$ and $e:(X,e)\to X$ show that
$\mathsf M_e$ and $\mathsf E$ simulate one another and recover every
$x_\theta$.

Now let $\Gamma:X\to Y$ be any sufficient coarse-graining and let
$R:Y\to X$ be an admitted recovery. Put

$$
a=\Gamma e:(X,e)\longrightarrow(Y,1_Y),
\qquad
b=eR:(Y,1_Y)\longrightarrow(X,e).
$$

Then $ba=eR\Gamma e$ fixes every $x_\theta$. Lemma 4.1 gives $ba=e$.
Thus $(X,e)$ is a retract of $Y$. The same calculation works when $Y$ is
already a Karoubi object.

For uniqueness, let $M$ and $N$ be two rigid minimal representatives.
Operational equivalence supplies maps $u:M\to N$ and $v:N\to M$ that fix the
corresponding experiment points under composition. Rigidity gives
$vu=1_M$ and $uv=1_N$. Thus $u$ is an admitted reversible isomorphism.
$\square$

### Corollary 4.3 — presentation invariance and retained symmetry

A reversible presentation superchannel conjugates stabilizer semigroups and
minimum-rank idempotents. It therefore transports the minimal boundary to an
isomorphic minimal boundary. The isomorphism class is intrinsic to the
declared operational experiment. Stabilizers and physical automorphisms are
retained; the theorem does not choose a preferred matrix representative.

### 4.3 What the theorem actually earns

The theorem is a process theorem, not a normalized-Choi-state theorem. Its
morphisms are admitted superchannels, and its object is an idempotent-split
process type. It establishes

$$
\boxed{\texttt{RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY}}
$$

at the finite-dimensional compact-convex Karoubi scope.

It does **not** prove that the minimum is an ordinary wire boundary. It does
not provide independent preparation, independent control, a complementary
subsystem, or a multiplication of observables. “Boundary” here means the
least recoverable process interface for a task-indexed experiment.

---

## 5. State-level minimal sufficiency and the Koashi--Imoto center

### 5.1 The inherited theorem

For comparison, let $\{\rho_\theta\}$ be a finite family of states on a
matrix algebra. Finite quantum statistical sufficiency gives a canonical
decomposition, up to the appropriate unitary and block equivalences,

$$
H
\simeq
\bigoplus_r H_r^Q\otimes H_r^N,
$$

$$
\rho_\theta
\simeq
\bigoplus_r
p(r\mid\theta)\,
\rho^Q_{\theta,r}\otimes\omega_r^N.
$$

The $N$ factors are independent of $\theta$ and statistically redundant for
this family. The minimal sufficient algebra is

$$
M_{\min}
\simeq
\bigoplus_r B(H_r^Q)\otimes I_{H_r^N},
$$

with center

$$
Z(M_{\min})
\simeq
\bigoplus_r\mathbb C I_r.
$$

The label $r$ is the classical part; $H_r^Q$ carries irreducibly quantum
parameter information; $H_r^N$ carries none. Minimal sufficient experiments
on von Neumann algebras exist and are unique up to normal isomorphism under
the established CP/Schwarz comparison hypotheses.

### Proposition 5.1 — center-only sufficiency is exceptional

For a minimal sufficient finite state experiment on $M_{\min}$, restriction
to $Z(M_{\min})$ is sufficient for the entire experiment if and only if
$M_{\min}$ is abelian.

**Proof.** If $M_{\min}$ is abelian, it equals its center. Conversely, if the
center restriction were sufficient, the experiment would be CP-equivalent to
an abelian experiment. Minimal sufficient representatives are unique up to
normal $*$-isomorphism. Hence $M_{\min}$ would be isomorphic to an abelian
algebra and therefore abelian. $\square$

Thus a nontrivial center does not mean the center contains everything the
future needs. Quantum information may remain inside each central sector.

### 5.2 Hand-checkable Koashi--Imoto control

Let

$$
H=(\mathbb C_Q^2\otimes\mathbb C_N^2)\oplus\mathbb C_c,
\qquad
\tau_N=I_N/2,
$$

and define

$$
\rho_0
=
\frac34|0\rangle\langle0|_Q\otimes\tau_N
\oplus\frac14,
$$

$$
\rho_1
=
\frac14|+\rangle\langle+|_Q\otimes\tau_N
\oplus\frac34.
$$

The classical block label has two values, the first block retains genuinely
quantum dependence on $\theta$, and the $N$ qubit is redundant. The minimal
sufficient algebra is

$$
M_2\oplus\mathbb C,
$$

its center is $\mathbb C^2$, and the spectator $N$ factor disappears from
the statistical minimum. It disappears from a physical process only when
the corresponding compression and recovery are admitted superchannels.

### 5.3 Classical and purely quantum controls

For the classical experiment on $\{a,b,c,d\}$

$$
p_0=(1/3,1/3,1/6,1/6),
\qquad
p_1=(1/6,1/6,1/3,1/3),
$$

the likelihood vectors identify $a\sim b$ and $c\sim d$. The ordinary
minimal sufficient statistic is the two-block partition
$\{\{a,b\},\{c,d\}\}$, and its algebra and center are both $\mathbb C^2$.

For two nonorthogonal, nonidentical pure qubit states, the
Koashi--Imoto quantum block is irreducible. The minimal algebra is $M_2$ and
its center is only $\mathbb C I$. A minimal boundary can therefore exist
while carrying no nontrivial canonical classical variable.

---

## 6. Why the classical center does not lift automatically

The state theorem in Section 5 does not supply the third registered rung.
There are two independent failures: a state compression need not be a
physical superchannel, and a process operator system need not contain the
center of its algebraic envelope as an admitted effect.

### 6.1 Choi-state equivalence need not be process equivalence

Use the convention

$$
J(\Phi)\in B(H_A\otimes H_B),
\qquad
\operatorname{Tr}_B J(\Phi)=I_A
$$

for a channel $\Phi:A\to B$. Take $A$ and $B$ to be qubits and let $W$ swap
the two Choi tensor factors. The map

$$
\mathcal S(J)=WJW
$$

is a reversible CPTP map on normalized Choi **states**. It fixes the
normalized Bell Choi state of the identity channel.

But for the replacer channel $\Phi_\rho(X)=\operatorname{Tr}(X)\rho$,

$$
J(\Phi_\rho)=I_A\otimes\rho_B.
$$

After swap,

$$
\mathcal S(J(\Phi_\rho))=\rho_A\otimes I_B,
$$

and therefore

$$
\operatorname{Tr}_B\mathcal S(J(\Phi_\rho))
=2\rho_A,
$$

which equals $I_A$ only for $\rho=I/2$. Thus $\mathcal S$ does not preserve
the affine channel-normalization slice and cannot be a deterministic
superchannel on all qubit channels.

### Proposition 6.1 — nonliftable Choi shadow

Exact CP equivalence of a family of normalized Choi states does not imply
exact process equivalence by one admitted deterministic superchannel.

The swap construction proves the proposition even for a reversible state
map. The process normalization constraints are physical data, not a
presentation detail.

### 6.2 An algebraic center need not be an operational effect

Let

$$
A=M_2\oplus M_2
$$

and write $X,Z$ for Pauli matrices. Consider the operator system

$$
S=\operatorname{span}_{\mathbb C}\{s_0,s_1,s_2\}\subset A,
$$

where

$$
s_0=(I,I),
\qquad
s_1=(Z,Z),
\qquad
s_2=(X,2X+Z).
$$

Since

$$
s_2^2=(I,5I),
$$

the generated $C^*$-algebra contains

$$
z_1=\frac{5s_0-s_2^2}{4}=(I,0),
\qquad
z_2=\frac{s_2^2-s_0}{4}=(0,I).
$$

Multiplying by $z_1,z_2$ then recovers $X$ and $Z$ in each block, so

$$
C^*(S)=M_2\oplus M_2.
$$

Neither central projector lies in $S$. Indeed, if
$\alpha s_0+\beta s_1+\gamma s_2=(I,0)$, comparison in the first block
forces $(\alpha,\beta,\gamma)=(1,0,0)$, leaving $I$ rather than $0$ in the
second block.

This is not cured by replacing the generated algebra with the
$C^*$-envelope. Every ideal of $A$ removes a full block. Quotienting to the
first block lowers the norm of $s_2$ from $\sqrt5$ to $1$. Quotienting to the
second lowers the norm of

$$
-3s_1+s_2=(X-3Z,\,2X-2Z)
$$

from $\sqrt{10}$ to $\sqrt8$. No nonzero block ideal is a boundary ideal,
so

$$
C_e^*(S)=A.
$$

### Proposition 6.2 — center/readout separation

There is no general construction that takes an operational operator system
$S$ to the center of $C_e^*(S)$ while guaranteeing that the central
projections are effects or readouts already admitted in $S$.

The displayed $S$ is an exact finite counterexample. The multiplication
that creates $z_1,z_2$ is algebraically legitimate in the envelope but is
not part of the original linear operational interface.

### 6.3 The type-theoretic obstruction

The minimum of Theorem 4.2 is a Karoubi object $(X,e)$. Its primitive data
are a process type and an idempotent superchannel. A center requires a
multiplication; a record requires an admitted instrument reading the central
effects. Neither is contained in the definition of $(X,e)$.

One may choose a Choi realization, a generated $C^*$-algebra, or an operator
system envelope, but Propositions 6.1 and 6.2 show that these choices do not
automatically define physical process maps or readouts. Therefore the paper
cannot pass the liftability gate for

$$
\texttt{RQ0-L0-CANONICAL-CLASSICAL-CENTER}.
$$

The first registered obstruction is

$$
\boxed{\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.}
$$

---

## 7. A separate no-smuggling theorem for future tasks

Even if the center-lift problem were solved, the future task can encode the
desired record.

### Theorem 7.1 — task-smuggling theorem

Let $\{P_r\}_{r=1}^m$ be any finite PVM on $H$, and define the dephasing
channel

$$
\mathcal D_P(\rho)=\sum_rP_r\rho P_r.
$$

Let

$$
A_P=\bigoplus_r P_rB(H)P_r.
$$

There exists a finite, faithful state experiment $\{\rho_\theta\}$ such that
the output family $\{\mathcal D_P(\rho_\theta)\}$ has minimal sufficient
algebra $A_P$ and hence center

$$
Z(A_P)=C^*(P_1,\ldots,P_m).
$$

**Proof.** Choose a finite family of faithful density matrices whose affine
span is the self-adjoint state space of $A_P$. Regard them as outputs of
$\mathcal D_P$; each has a preimage under $\mathcal D_P$, namely itself. Any
normal CP endomorphism fixing the entire family fixes the affine span and
therefore all of $A_P$. The experiment is minimal on $A_P$. Its center is
the algebra generated by the block identities $P_r$. $\square$

### Corollary 7.2 — no center without an independently fixed task

Any desired finite sharp record algebra can be made the center of a minimal
sufficient future experiment by first choosing its matching dephasing task.
Therefore “derive the record as the center” is circular unless the future
task family is specified independently of the candidate record.

This is not an argument against task relativity. It is a discriminator
between genuine task-relative physics and choosing a task after inspecting
the desired answer.

### 7.1 Within-sector quantum dependence

Let $M=M_2\oplus M_2$ and consider two pure states supported in the first
block:

$$
\rho_0=|0\rangle\langle0|\oplus0,
\qquad
\rho_1=|+\rangle\langle+|\oplus0.
$$

Their center distributions are identical: both give $(1,0)$. Their trace
distance is

$$
\|\rho_0-\rho_1\|_1=\sqrt2.
$$

Any recovery map from the center receives the same input for both parameters
and hence returns one common state $\sigma$. The triangle inequality gives

$$
\max_i\|\rho_i-\sigma\|_1
\ge\frac{\sqrt2}{2}.
$$

The center can be a nontrivial classical interface while failing badly to be
sufficient for the full future experiment.

---

## 8. W3 as task-relative sufficiency: a nonempty finite control

The generic center rung is blocked, but the proposed W3 criterion can still
be tested in a small scope where the classical output algebra is itself an
admitted process object.

### 8.1 Exact qubit control

Let the source experiment admit two deterministic preparation settings with
conditional cut states

$$
|\psi_0\rangle
=
\frac{\sqrt3|0\rangle+|1\rangle}{2},
\qquad
|\psi_1\rangle
=
\frac{|0\rangle+\sqrt3|1\rangle}{2}.
$$

The settings may be sampled with equal prior weights, but their external
setting label is not delivered to the future as a side channel. Take write
to be the identity at the displayed cut. Freeze the preserving
future task to be $Z$-dephasing followed by a complete classical readout.
It gives

$$
p_0=(3/4,1/4),
\qquad
p_1=(1/4,3/4).
$$

This two-point classical experiment is minimal and has center $\mathbb C^2$.
The center is sufficient for every task in the frozen preserving class by
construction of that class as a classical output profile.

Take the matched no-write process to reset both source branches to
$|+\rangle$. Its center statistics are $(1/2,1/2)$ for both labels, so it
fails the write-correlation discriminator.

Now enlarge the future class by also retaining the quantum output before
dephasing. The two nonorthogonal pure states form an irreducible qubit
experiment. No classical-bit recovery can reconstruct both states exactly:
a nontrivial convex mixture cannot equal a pure state unless every
positive-weight component equals that pure state, which would force the two
different pure outputs to coincide. Compactness therefore gives strictly
positive deficiency from the preserving center to the enlarged experiment.

The tester-visible coherence removed by $Z$-dephasing is exact. For either
source state,

$$
\left\|
|\psi_i\rangle\langle\psi_i|
-
\mathcal D_Z(|\psi_i\rangle\langle\psi_i|)
\right\|_1
=
\frac{\sqrt3}{2}.
$$

### Proposition 8.1 — nonemptiness of the Markov-boundary criterion

At the displayed one-step state-process scope, an independently fixed
classical preserving task and a richer retained-quantum task satisfy

$$
\delta_{\mathrm{pres}}=0,
\qquad
\delta_{\mathrm{full}}>0,
$$

with a nontrivial write statistic and a matched no-write failure.

This proposition proves that the proposed discriminator is mathematically
nonempty. It does not establish a generic center-lift theorem and therefore
does not earn `RQ0-L0-W3-MARKOV-BOUNDARY` for process combs.

### 8.2 Interpretation

The screening statement is

$$
\text{operational past}
\longrightarrow
\text{classical statistic}
\longrightarrow
\text{declared preserving task}.
$$

It is a one-chart, instrument-relative Markov statement. It is not a causal
Markov condition in spacetime.

---

## 9. Exact branch-memory reclassification

### 9.1 Frozen process law

Let

$$
H=\mathbb C_b^2\otimes\mathbb C_m^2,
\qquad
H_2=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
$$

and use source labels $j$ in the order
$(|00\rangle,|10\rangle,|01\rangle,|11\rangle)$. The write, no-write,
preserve, and erase unitaries are

$$
U=\operatorname{CNOT}_{b\to m}(H_2\otimes I),
\qquad
N=H_2\otimes I,
$$

$$
V=H_2\otimes I,
\qquad
E=U^*.
$$

Put

$$
\psi_j=U|j\rangle
$$

with source-branch weight $1/4$ retained through the common success/sink
embedding of Section 2.2. Because that weight is the same for all four
parameters, the success flag carries no information about $j$. Define also

$$
v_0=|+,0\rangle,
\quad v_1=|-,0\rangle,
\quad v_2=|+,1\rangle,
\quad v_3=|-,1\rangle.
$$

The exact transition matrix obeys

$$
2\langle v_i|\psi_j\rangle
=
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix}_{ij}.
$$

Thus every terminal probability $|\langle v_i|\psi_j\rangle|^2$ is $1/4$.

### 9.2 Preserving terminal task: the minimum is trivial

Freeze the preserving future to “apply $V$, then measure the computational
basis.” Its pulled-back effects at the cut are
$|v_i\rangle\langle v_i|$. For every written source $\psi_j$, the output
law is

$$
(1/4,1/4,1/4,1/4).
$$

All four parameters therefore define the same future process. The minimal
sufficient experiment has one point and algebra $\mathbb C$. It contains no
nontrivial classical center. In particular, it selects neither the six
$2+1+1$ seams, the three $2+2$ seams, nor the additional complex rank-two
seam.

The matched no-write states are $N|j\rangle\in\{v_i\}$. Under the same task
their terminal distributions are delta functions. The no-write process
carries strictly **more** source-label information than the write process.
Hence this frozen task also fails the proposed write/no-write ordering.

### 9.3 Eraser terminal task: the minimum is the fine classical label

Freeze instead “apply $E=U^*$, then measure the computational basis.” Since

$$
E\psi_j=|j\rangle,
$$

the output distribution is deterministic at $j$. The minimal sufficient
experiment is the fine four-point classical experiment $\mathbb C^4$. If the
preserving and eraser terminal tasks are tagged and bundled, the eraser
component already separates every $j$, so the bundle remains at least this
informative.

This task does not select any one inherited coarse seam. Its classical
center is the entire fine four-label algebra, and it is sufficient for the
purely classical bundled output. There is no positive center deficiency at
that terminal-only scope.

### 9.4 Retained quantum output and separating pasts

With only the four written states $\{\psi_j\}$, retaining the cut state gives
four orthogonal pure states and again a fine classical four-point minimal
experiment. If the admitted past family is enlarged **before inspection**
to a tomographically separating set of cut preparations, retaining the full
quantum output yields the full matrix experiment $M_4$, whose center is
scalar.

Thus natural task enrichments display the sequence

$$
\mathbb C
\quad\longrightarrow\quad
\mathbb C^4
\quad\text{or}\quad
M_4,
$$

not a canonical one of the proposed coarse record algebras.

### 9.5 Candidate-matched tasks are circular

For a candidate record PVM $R$, inserting its dephasing $\mathcal D_R$ as a
future task can make the corresponding block algebra and its center appear.
With a separating past extension, a $2+1+1$ PVM gives the block algebra

$$
M_2\oplus\mathbb C\oplus\mathbb C
$$

with center $\mathbb C^3$, while a $2+2$ PVM gives

$$
M_2\oplus M_2
$$

with center $\mathbb C^2$. The exact complex rank-two candidate also gives
an abstract $M_2\oplus M_2$ block algebra, but with a different embedding in
$M_4$.

Theorem 7.1 shows that this is not selection. Rotating the candidate PVM and
rotating the dephasing task generates continuous families of equally
manufactured centers.

### Theorem 9.1 — no canonical branch-memory center under the frozen tasks

For the original complete four-branch source and the independently frozen
preserving and eraser terminal tasks:

1. the preserving minimum is trivial;
2. the eraser minimum is the fine four-point classical experiment;
3. their tagged bundle is separated by the fine label;
4. none of the nine partition seams or the additional complex seam is the
   unique minimal sufficient center; and
5. candidate-specific dephasing can recover those centers only by violating
   the task-independence gate.

Minimal sufficiency therefore reclassifies the old seam multiplicity rather
than resolving it in favor of the familiar memory PVM.

---

## 10. Task-indexed boundaries, not tester descent

### 10.1 Information monotonicity

Suppose $\mathfrak F_1\subseteq\mathfrak F_2$ are independently declared
future-task families and the rich tagged output has an admitted forgetful
superchannel

$$
q:X_{c,\mathfrak F_2}\longrightarrow X_{c,\mathfrak F_1}.
$$

Then

$$
qF_{c,\mathfrak F_2,\theta}
=F_{c,\mathfrak F_1,\theta}
$$

for every $\theta$, and hence

$$
\mathsf E_{c,\mathfrak F_2}
\succeq_D
\mathsf E_{c,\mathfrak F_1}.
$$

The minimal total boundary for the richer task is therefore at least as
informative in the process-simulation preorder.

### 10.2 Centers are not monotone

Classical centers do not inherit this direction. In the qubit control of
Section 8, the preserving task has minimal algebra $\mathbb C^2$, while the
richer retained-quantum task has minimal algebra $M_2$ and center
$\mathbb C$. The total sufficient object becomes richer while its center
becomes smaller.

Therefore there is no monotone assignment

$$
\mathfrak F\longmapsto Z(\mathsf M_{c,\mathfrak F})
$$

without additional structure and variance choices. The physically honest
object is the task-indexed family of total minimal boundaries. It is not a
sheaf, and unrelated process profiles are not required to glue.

### 10.3 Symmetry and no selection

Theorem 4.2 determines a minimal boundary only up to reversible operational
equivalence. If a physical symmetry maps one realization to another, that
symmetry is an automorphism or an arrow in the retained equivalence groupoid.
No basis, block order, or lexical representative is selected. A symmetry
orbit is a positive classification, not a reason to invent a preferred
chart.

---

## 11. Mandatory controls and gate audit

### 11.1 Control table

| Control | Exact result | Consequence |
|---|---|---|
| Classical statistic | $\{a,b\}$ and $\{c,d\}$ are the minimal blocks | ordinary sufficiency recovered |
| KI family | $M_2\oplus\mathbb C$ with center $\mathbb C^2$ and redundant $N$ factor | classical, quantum, and redundant data separate |
| Purely quantum family | two nonorthogonal pure qubit states give $M_2$ | minimal boundary can have trivial center |
| Redundant spectator | parameter-independent $\tau_N$ drops from the state minimum | physical deletion still needs admitted maps |
| Nonliftable Choi shadow | Choi-factor swap violates channel normalization | CP state equivalence is not process equivalence |
| Operator-system center | $C_e^*(S)=M_2\oplus M_2$ but $z_1,z_2\notin S$ | algebraic center need not be readable |
| Task relativity | preserving $\mathbb C^2$, richer task $M_2$ | minimum depends on future role |
| Within-sector quantum data | center inputs identical while state distance is $\sqrt2$ | center-only sufficiency fails |
| Complete weights | flagged $p\rho$ and $q\rho$ differ for $p\ne q$ | normalized branches may not replace instruments |
| Branch-memory | preserving minimum $\mathbb C$; eraser minimum $\mathbb C^4$ | no inherited coarse seam selected |
| Continuous rotated candidates | matching rotated dephasings manufacture matching centers | task-smuggling detector fires |
| Tomographic past extension | retained quantum task reaches $M_4$ | center becomes scalar rather than preferred coarse record |
| Symmetry | reversible realizations remain a groupoid | no arbitrary representative |
| Terminal RQ0-A | supplied regional maps still pull back sharp projectors | declared-overlap control survives but is not rederived |

### 11.2 Same normalized branches, different weights

If two source branches are $p\rho$ and $q\rho$ with $p\ne q$, normalization
maps both to $\rho$ and erases the distinction. In the complete flagged
instrument, the flag probability is respectively $p$ and $q$, so an admitted
flag tester distinguishes them by $|p-q|$. This is why $\Theta_c$ contains
complete instruments rather than normalized conditional states.

### 11.3 Terminal RQ0-A control

The terminal factual-base construction supplied amplitude-instrument
morphisms and literal record-projector pullbacks among declared regions. In
the present language those maps furnish a sharp, zero-defect process
interface at their stated finite scope. This is a positive control for what a
physical lift looks like. Minimal sufficiency does not reconstruct those
regions or maps and cannot turn equality of centers into W6 fact identity.

### 11.4 Four gates

| Object | Referent | Necessity | No-smuggling condition | Discriminator |
|---|---|---|---|---|
| future experiment | complete conditional future comb family | records should summarize dependence of future tasks on past controls | no record PVM or factor enters | weights, flags, presentation covariance |
| simulation | one admitted parameter-independent superchannel | familywise information comparison | no map chosen separately for each $\theta$ | exact positive/negative deficiency |
| minimal boundary | least recoverable process retract | remove operational redundancy | no arbitrary Choi-state CP map | minimum-rank idempotent and retract theorem |
| state center | classical part of a specified state experiment | separates classical/quantum/redundant information | not promoted to process readout | KI controls and trivial-center family |
| physical center | admitted classical readout of a process minimum | needed for a record interface | multiplication and readout must be constructed | Choi and operator-system counterexamples |
| W3 task boundary | center sufficient for preserving but not richer tasks | formalizes the classical seam/recoverable quantum split | tasks frozen independently | qubit positive control and branch-memory negative |

---

## 12. Classification of statements

### 12.1 Definitions

- typed future process experiment;
- exact process simulation and equivalence;
- process sufficiency and recovery;
- tester-norm deficiency;
- Karoubi minimal process boundary;
- task-relative W3 sufficiency criterion.

### 12.2 New theorems proved here

1. typed complete future experiments exist for every declared compatible
   cut/task package (Proposition 2.1);
2. the finite convex deficiency has the displayed decision-functional
   minimax form (Proposition 3.1);
3. every finite experiment in the declared compact-convex process category
   has a minimal sufficient Karoubi representative, unique up to reversible
   operational equivalence (Theorem 4.2);
4. center-only sufficiency of a minimal state experiment is equivalent to
   abelianness of its minimal algebra (Proposition 5.1);
5. normalized-Choi CP equivalence need not lift to a deterministic
   superchannel (Proposition 6.1);
6. the center of an operator-system envelope need not be an admitted effect
   (Proposition 6.2);
7. any desired finite PVM center can be planted through its matching
   dephasing future task (Theorem 7.1);
8. the proposed W3 task criterion is nonempty at a one-step state-process
   scope (Proposition 8.1); and
9. the independently frozen branch-memory tasks do not select any inherited
   coarse record seam (Theorem 9.1).

### 12.3 Inherited theorems

- finite-dimensional comb/tester representation and tester-separated
  operational equivalence;
- CP/Schwarz sufficiency and uniqueness of minimal sufficient state
  experiments;
- Koashi--Imoto classical/quantum/redundant decomposition;
- comparison of channel families by one superchannel;
- finite-dimensional randomization criteria for channel/process decision
  problems; and
- instrument-relative quantum Markov order.

### 12.4 Measurements and exact finite calculations

- the classical four-point statistic;
- the KI block example;
- Choi swap normalization failure;
- the $M_2\oplus M_2$ operator-system center exclusion;
- trace distances $\sqrt2$ and $\sqrt3/2$;
- branch-memory uniform preserving law and deterministic eraser law.

### 12.5 Conjectures and open obligations

- a physically natural class of process minima may carry additional
  operator-system or algebra structure;
- an admitted nondemolition instrument may select a readable center;
- independently motivated future roles may produce stable, nontrivial
  centers in less symmetric laws;
- autonomous process charts and their physical pullbacks remain open.

None of these conjectures is used to upgrade the outcome.

---

## 13. Outcome audit and first unresolved obstruction

### `RQ0-L0-FUTURE-EXPERIMENT`

**Provisionally earned.** Complete past instruments induce correctly typed,
flagged conditional future combs under independently fixed task
superchannels. Weights, outcomes, disturbances, tester quotient, and
presentation covariance are retained.

### `RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY`

**Provisionally earned at Karoubi scope.** Theorem 4.2 constructs a minimal
sufficient process retract using admitted deterministic superchannels and
proves its retract property and uniqueness up to reversible operational
equivalence.

### `RQ0-L0-CANONICAL-CLASSICAL-CENTER`

**Not earned.** A Karoubi process retract has no intrinsic multiplication;
a normalized-Choi statistical compression may not be a superchannel; and a
center of an algebraic operator-system envelope may not be an admitted
effect. No general physical central readout has been constructed.

### `RQ0-L0-W3-MARKOV-BOUNDARY`

**Not reached.** The criterion has a small positive state-process control,
but the generic physical center prerequisite fails. The branch-memory law
does not select its familiar record under independently frozen task classes.

### Disposition

The first registered obstruction is

$$
\boxed{
\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.
}
$$

`RQ0-L0-BLOCKED-AT-TASK-SELECTION` is a real downstream obstruction proved
by Theorem 7.1, but it is not selected as the first block because center lift
already fails.

---

## 14. Physical meaning

The paper establishes a useful but narrower fact than the motivating
proposal.

> A finite operational quantum experiment has a least recoverable process
> interface, once the chart, cut, admitted past instruments, future tasks,
> and superchannel class are fixed.

That interface is ontologically meaningful as a repeatable coarse-graining
of future-relevant process information. It removes redundancy without
choosing a coordinate presentation.

But:

> The least process interface is not automatically classical, and the
> center of an algebra chosen to represent it is not automatically a
> physical record.

This failure matters. Quantum information can remain irreducible within
central sectors. A physical law may not admit the compression or readout
suggested by a state-level algebra. And a future experiment chosen to match a
PVM can manufacture the desired center.

The next conceptual obligation, if separately authorized, would be to state
physical conditions under which an idempotent-split process boundary carries
an admitted nondemolition classical instrument and to derive those
conditions without selecting the task from the desired record. That is still
one-chart record physics. It is not yet localization.

---

## 15. Claim ceiling

Nothing in this paper establishes:

- an actual selected outcome;
- W6 fact co-reference or event-token identity;
- an autonomous quantum subsystem;
- a physical overlap between independently reconstructed charts;
- intrinsic spatial localization;
- a topology or manifold shadow;
- operational influence or causal order;
- dimension, volume, a Lorentzian metric, or special relativity;
- a quantum field; or
- gravity.

The typed direction of a comb is laboratory composition order only.
`RQ0-T1`, `RQ0-C1`, and every later programme remain closed.

---

## 16. Conclusion

Minimal sufficiency is a better selection principle than enumerating every
W3-positive projector family. It yields a genuine new theorem: one finite
operational chart and one future-task class determine a minimal sufficient
process retract, unique up to reversible operational equivalence.

The theorem also shows exactly where the stronger proposal breaks. A process
retract is not yet an observable algebra. Its representation-dependent
algebraic center may fail to be an admitted readout, and an arbitrary desired
center can be planted by choosing a matching future task. The branch-memory
model consequently moves between a trivial minimum, a fine classical
minimum, and a full quantum minimum as independently declared tasks change;
it does not reveal one canonical coarse seam.

The honest result is therefore:

$$
\boxed{
\begin{array}{c}
\text{minimal sufficient process boundaries exist at finite Karoubi scope},\\[1mm]
\text{but a physical canonical classical center does not follow generically.}
\end{array}
}
$$

That is progress in quantum boundary theory, not yet locality or spacetime.

---

## References

1. A. Jenčová and D. Petz, “Sufficiency in quantum statistical inference,”
   *Communications in Mathematical Physics* **263**, 259–276 (2006),
   [arXiv:math-ph/0412093](https://arxiv.org/abs/math-ph/0412093).
2. M. Koashi and N. Imoto, “What is Possible Without Disturbing Partially
   Known Quantum States?”, *Physical Review A* **66**, 022318 (2002),
   [arXiv:quant-ph/0101144](https://arxiv.org/abs/quant-ph/0101144).
3. Y. Kuramochi, “Minimal sufficient statistical experiments on von Neumann
   algebras,” *Journal of Mathematical Physics* **58**, 062203 (2017),
   [arXiv:1701.03394](https://arxiv.org/abs/1701.03394).
4. Y. Kuramochi, “Accessible information without disturbing partially known
   quantum states on a von Neumann algebra,” *International Journal of
   Theoretical Physics* **57**, 2249–2266 (2018),
   [arXiv:1710.01599](https://arxiv.org/abs/1710.01599).
5. G. Gour, “Comparison of Quantum Channels by Superchannels,” *IEEE
   Transactions on Information Theory* **65**, 5880–5904 (2019),
   [arXiv:1808.02607](https://arxiv.org/abs/1808.02607).
6. A. Jenčová, “A general theory of comparison of quantum channels (and
   beyond),” [arXiv:2002.04240](https://arxiv.org/abs/2002.04240).
7. G. Chiribella, G. M. D’Ariano, and P. Perinotti, “Theoretical framework
   for quantum networks,” *Physical Review A* **80**, 022339 (2009),
   [arXiv:0904.4483](https://arxiv.org/abs/0904.4483).
8. P. Taranto, F. A. Pollock, S. Milz, M. Tomamichel, and K. Modi, “Quantum
   Markov Order,” *Physical Review Letters* **122**, 140401 (2019),
   [arXiv:1805.11341](https://arxiv.org/abs/1805.11341).
