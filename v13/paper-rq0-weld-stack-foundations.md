# The Weld Stack

## W3 Observability, Quantaloid Supports, and Derived Quantum Overlaps

**Status:** `GREEN-UNREVIEWED`  
**Date:** 2026-07-31  
**Provisional highest result:** `RQ0-L0-WELD-QUANTALOID-CHARTS`  
**Strict non-claim:** no spatial locality, topology, causality, geometry, spacetime, field theory or gravity

---

## Abstract

An exact quantum process theory with finitely many arrows cannot contain an
ordinary contractive closed amplitude. We prove the general obstruction: if a
finite category is represented linearly, every nonzero represented scalar is
a root of unity, and every nonzero eigenvalue of every represented
endomorphism is semisimple and root-of-unity valued. The obstruction concerns
finite arrow sets, not finite presentations or finite-dimensional Hilbert
spaces.

We replace the failed object by a finitely presented, generally infinite,
dagger-linear process sketch equipped with a separately declared grammar of
physically admitted experiments. The complete branch-memory
write/preserve/erase/control experiment is represented exactly over
$\mathbb Q(\sqrt2)$, including its closed amplitude $1/2$.

For each internally certified stable-record diagram $W$, we define the
counterfactual observability algebra

$$
\mathcal A_W(y)
=
C^*\!\left(
\Phi_a^*(P):P\in R_W,
\ a:y\to x_W\text{ admitted}
\right).
$$

It is the least operator algebra carrying every admitted Heisenberg image of
the record algebra. We prove presentation invariance, gauge covariance,
monotonicity in the counterfactual law, handle independence, and exact proper,
global and trivial classifications. A proper observability algebra is called
record-relevant, not local. It becomes an addressable chart only when the
admitted process law contains a completely positive split/comprehension
certificate.

The accessible operator spans form an involutive quantaloid. On it we
construct an exact incidence distributor between canonical process-support
subspaces and internal W3 diagrams. Its Isbell fixed points form a complete
quantaloid-enriched category; the addressable fixed points give a
presentation-invariant W3 chart groupoid. Presentation gauge is quotiented,
while physical symmetry remains a separate action.

This paper does not construct the advertised analytic or derived Weld stack.
It defines a homotopy-cone prestack for overlap and proves its reduction in a
finite commutative corner control, but does not prove general representability.
Interior tensor product of $C^*$-correspondences is retained as composition,
not mislabeled as a pullback. The earned object is therefore a
finite-boundary, finite-dimensional **Weld quantaloid with addressable W3 chart
concepts**. Its hom-lattices are not finite. A genuine Weld stack,
derived overlaps and a manifold shadow remain conditional future layers.

---

## 1. Claim boundary

The target is pre-spatial. A process chart in this paper means an
operator-algebraic part of an admitted quantum process law that is both:

1. relevant to an internally certified stable record; and
2. independently addressable through an admitted physical certificate.

It does not mean a bounded spatial region, a causal domain, a coordinate
patch, or an open set of a manifold.

The construction separates five questions:

$$
\begin{aligned}
&\text{Can the quantum amplitudes be represented coherently?}\\
&\text{Which observables are counterfactually visible to a stable record?}\\
&\text{Can that observable part be independently addressed?}\\
&\text{How are all mutually compatible operation/record concepts retained?}\\
&\text{Do their comparisons possess physical higher overlaps?}
\end{aligned}
$$

Only the first four receive positive finite results here. The fifth receives
a typed prestack and special controls, not a general overlap theorem.

The complete admitted process law remains a provisional nomological input.
This paper does not derive that law from one realized history. It instead
tests which localization statements are invariant consequences of a fixed
law and which change when the counterfactual law changes.

---

## 2. The finite-arrow obstruction

### Definition 2.1 — exact scalar representation

Let $\mathcal C$ be a category with finitely many arrows and a distinguished
object $\mathbf 1$. An exact scalar representation is a functor

$$
\rho:\mathcal C\longrightarrow\mathbf{FinVect}_{\mathbb C}
$$

with $\rho(\mathbf 1)=\mathbb C$. Every
$c\in\operatorname{End}_{\mathcal C}(\mathbf 1)$ is then represented by
multiplication by one complex number $\lambda_c$.

### Theorem 2.2 — finite-arrow scalar obstruction

For every represented scalar $\lambda_c$,

$$
\lambda_c=0
\quad\text{or}\quad
\lambda_c\text{ is a root of unity}.
$$

In particular, no exact nonzero closed amplitude with modulus strictly between
zero and one occurs in such a representation.

*Proof.* The endomorphism monoid of $\mathbf 1$ is finite. Hence the sequence

$$
c,c^2,c^3,\ldots
$$

eventually repeats: there exist positive integers $m<n$ with $c^m=c^n$.
Functoriality gives

$$
\lambda_c^m=\lambda_c^n,
$$

so

$$
\lambda_c^m(1-\lambda_c^{n-m})=0.
$$

Either $\lambda_c=0$ or $\lambda_c^{n-m}=1$. $\square$

### Theorem 2.3 — spectral obstruction

Let $a:x\to x$ be any endomorphism of a finite category, and let
$T=\rho(a)$. Then:

1. every nonzero eigenvalue of $T$ is a root of unity;
2. every nonzero eigenvalue is semisimple;
3. the generalized zero-eigenspace may contain a nilpotent part of finite
   index.

*Proof.* Finiteness gives $a^m=a^n$ for some $m<n$, hence

$$
T^m(T^{n-m}-I)=0.
$$

The minimal polynomial of $T$ divides

$$
p(t)=t^m(t^{n-m}-1).
$$

Its nonzero roots are roots of unity. Over characteristic zero,
$t^{n-m}-1$ is square-free, so every nonzero root occurs with multiplicity
one in $p$ and therefore in the minimal polynomial. Jordan blocks at nonzero
eigenvalues have size one. Only the factor $t^m$ permits a nilpotent block, at
eigenvalue zero. $\square$

### Corollary 2.4 — the branch-memory contradiction

If a purported finite-arrow process category contains a closed process with
represented amplitude $1/2$, it has no exact scalar representation of the
form in Definition 2.1.

This is the precise failed assumption. Finite-dimensional Hilbert spaces are
not excluded. A finite list of generators and relations is not excluded. A
dagger category is not excluded. What fails is a finite set of arrows closed
under unrestricted repeated categorical composition.

---

## 3. Finitely presented Weld process sketches

### Definition 3.1 — amplitude presentation

Fix a conjugation-stable subfield $\mathbb K\subseteq\mathbb C$. A finite
dagger-linear presentation consists of:

1. a finite set $B$ of generating boundary types, including a unit boundary
   $\mathbf 1$;
2. a finite typed graph $G$ of generating amplitude arrows;
3. the formal daggers of all generators;
4. the free $\mathbb K$-linear dagger category
   $\mathbb K\langle B,G\rangle_\dagger$;
5. a finite dagger-stable family $R$ of typed linear equations; and
6. the quotient
   $$
   \mathcal C_D^{\mathrm{amp}}
   =
   \mathbb K\langle B,G\rangle_\dagger/\langle R\rangle,
   $$
   where $\langle R\rangle$ is the two-sided dagger ideal generated by the
   relations.

The category is finitely presented, not finite. Its hom-spaces are
$\mathbb K$-vector spaces and normally contain infinitely many arrows.
Identities, zero arrows, addition, scalar multiplication and dagger are
therefore typed and exact.

### Definition 3.2 — admitted experimental grammar

An admitted grammar $\mathsf{Adm}_D$ is a finitely specified typed language of
experimental diagrams together with an interpretation

$$
\llbracket-\rrbracket:
\mathsf{Adm}_D\longrightarrow\mathcal C_D^{\mathrm{amp}}.
$$

It contains identities and a declared finite set of primitive experiments and
is closed under exactly the sequential pastings and control constructions
specified by its grammar. It need not mark every formal linear combination or
every linear map between represented Hilbert spaces as physically executable.

This distinction is load-bearing:

$$
\text{mathematically representable amplitude}
\ne
\text{admitted intervention}.
$$

The admitted grammar can generate infinitely many finite diagrams from
finitely many productions.

Its interpreted image is denoted

$$
\mathcal C_D^{\mathrm{adm}}
=
\operatorname{im}\llbracket-\rrbracket
\subseteq
\mathcal C_D^{\mathrm{amp}}.
$$

This is a typed selected process language. It need not be full, linear, or
closed under every formal dagger present in the amplitude completion.

### Definition 3.3 — exact representation and channel envelope

An exact amplitude representation is a \(\mathbb K\)-linear dagger functor

$$
\rho_D:
\mathcal C_D^{\mathrm{amp}}
\longrightarrow
\mathbf{FinHilb}_{\mathbb C}
$$

with \(\rho_D(\mathbf 1)=\mathbb C\), where
\(\mathbb K\hookrightarrow\mathbb C\) is the fixed embedding and every
declared exact matrix coefficient lies in \(\mathbb K\). Thus the Hilbert
spaces and \(C^*\)-algebras have their standard complex meaning while the
load-bearing arithmetic remains exact over \(\mathbb K\).

Operational equivalence at this scope is exact equality of represented typed
maps. Equivalently, replace
\(\mathcal C_D^{\mathrm{amp}}\) by its quotient through the dagger ideal
\(\ker\rho_D\), so that \(\rho_D\) is faithful on represented arrows.
For channel diagrams, equivalence is exact equality of their Choi matrices.
These relations are congruences for typed composition, linear operations and
dagger. Consequently every equation used by W3, observability and projector
pullback is an equation in the same operational quotient, not a separate
handle comparison.

The channel envelope is separately specified. At every represented boundary
$x$, let

$$
\mathfrak B_x=B(\rho_D(x)).
$$

An admitted Schrödinger channel $\Phi_a:\mathfrak B_y{}_*\to
\mathfrak B_x{}_*$ is completely positive and trace preserving. Its
Heisenberg adjoint

$$
\Phi_a^*:\mathfrak B_x\longrightarrow\mathfrak B_y
$$

is unital and completely positive. Unitary amplitude generators produce the
channels $\sigma\mapsto U\sigma U^\dagger$; additional noisy, reset, discard
or conditional-expectation channels are admitted only when explicitly
generated by the channel grammar.

The amplitude and channel layers are related but not identified. This is the
finite-dimensional instance of the familiar distinction between pure process
theories and categories of completely positive classical–quantum channels
[1].

### Definition 3.4 — Weld process sketch

A **Weld process sketch** is

$$
\mathbb P_D
=
(B,G,R,\mathsf{Adm}_D,\dagger,\rho_D,
  \mathsf{Chan}_D,G_D),
$$

where $G_D$ is a declared presentation-gauge group acting by compatible
unitary changes of boundary representation. A gauge element
$g=(J_x)_x$ sends

$$
\rho_D(a)
\longmapsto
J_y\rho_D(a)J_x^\dagger
$$

for $a:x\to y$, and transports channels and distinguished projectors by the
same boundary unitaries.

Physical symmetries are not included in $G_D$ merely because they preserve the
law. Gauge denotes presentation redundancy; physical symmetry is treated
separately in Section 9.

### Proposition 3.5 — why the obstruction is removed

A Weld process sketch may have a finite presentation and a finite-dimensional
exact representation while containing infinitely many distinct powers of a
closed amplitude.

*Proof.* The free linear dagger category and its quotient are not required to
have finitely many arrows. If a represented closed scalar is $1/2$, its powers
are represented by $2^{-k}$. These are distinct, so the corresponding arrows
remain distinct in any quotient through which the representation factors.
No finiteness argument identifies them. $\square$

---

## 4. Exact branch-memory W3 representation

### 4.1 The finite presentation

Work over

$$
\mathbb K=\mathbb Q(\sqrt2).
$$

Use four generating boundaries

$$
\mathbf 1,
\qquad
x_0,
\qquad
x_1,
\qquad
x_2,
$$

represented by \(\mathbb C\) and three copies of

$$
H=\mathbb C^2\otimes\mathbb C^2,
$$

with all displayed matrices in \(\mathbb K\).

The ordered configuration basis is

$$
|00\rangle,
|01\rangle,
|10\rangle,
|11\rangle,
$$

where the first bit is the branch and the second bit is the memory.

The generating preparations and probes are

$$
\eta_{bm}:\mathbf1\to x_0,
\qquad
f_{cn}:x_2\to\mathbf1,
$$

represented by $|bm\rangle$ and $\langle cn|$. The four fine alternatives at
$x_1$ are

$$
Q_{bm}=|bm\rangle\langle bm|.
$$

The record projectors are

$$
P_m=Q_{0m}+Q_{1m},
\qquad
m\in\{0,1\}.
$$

The finite relations include

$$
Q_{bm}Q_{b'm'}
=
\delta_{bb'}\delta_{mm'}Q_{bm},
\qquad
\sum_{b,m}Q_{bm}=I_{x_1},
$$

$$
P_mP_{m'}=\delta_{mm'}P_m,
\qquad
P_0+P_1=I_{x_1},
\qquad
P_m=Q_{0m}+Q_{1m}.
$$

The process generators are

$$
U,N:x_0\to x_1,
\qquad
V,E:x_1\to x_2.
$$

Let

$$
H_2=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
$$

Their exact representations are

$$
\rho(U)=\operatorname{CNOT}_{b\to m}(H_2\otimes I),
\qquad
\rho(N)=H_2\otimes I,
$$

$$
\rho(V)=H_2\otimes I,
\qquad
\rho(E)=(H_2\otimes I)\operatorname{CNOT}_{b\to m}.
$$

The relations declare these generators unitary. The admitted amplitude
grammar contains all displayed preparations, probes, projectors and the
forward process generators \(U,N,V,E\), together with the typed forward
composites used below and arbitrary finite products of completed closed scalar
diagrams at the unit boundary. Formal daggers exist in the amplitude
completion but are not thereby admitted as inverse experiments. The channel
grammar contains the four forward unitary channels and their type-compatible
forward composites. It contains no conditional expectation, subsystem
discard, inverse-time channel or unlisted boundary endomorphism at this stage.

### Definition 4.1 — internal W3 predicates

For a candidate write $A:x_0\to x_1$, perfect record correlation means

$$
Q_{bm}A\eta_j\ne0,
\quad
Q_{b'm'}A\eta_j\ne0,
\quad
(b,m)\ne(b',m')
\quad\Longrightarrow\quad
m\ne m'.
$$

A continuation $T:x_1\to x_2$ preserves availability when

$$
f_iTQ_{bm}\ne0,
\quad
f_iTQ_{b'm'}\ne0
\quad\Longrightarrow\quad
m=m'.
$$

It is a witnessed eraser when availability fails and some cross-sector term

$$
C_{i,j;(b,m),(b',m')}^T
=
(f_iTQ_{bm}U\eta_j)
\overline{(f_iTQ_{b'm'}U\eta_j)}
$$

is nonzero with $m\ne m'$.

The name “no-write” for $N$ is an operational role declaration. The theorem
below proves only that it fails the record-correlation predicate. That failure
alone would not establish a historical claim about what physically happened.

### Theorem 4.2 — W3 sketch representability

The preceding finitely presented Weld process sketch has an exact
finite-dimensional
representation in which:

1. $U$ passes perfect correlation;
2. $V$ preserves availability;
3. $E$ is a witnessed coherent eraser;
4. $N$ fails perfect correlation; and
5. the closed amplitude $f_{00}VQ_{00}U\eta_{00}$ equals $1/2$.

*Proof.* For every basis preparation,

$$
U|b,m\rangle
=
\frac{|0,m\rangle+(-1)^b|1,m\oplus1\rangle}{\sqrt2}.
$$

The two nonzero alternatives have different memory values, proving
correlation.

The continuation $V$ acts only on the branch bit. Therefore
$f_{cn}VQ_{bm}$ can be nonzero only when $n=m$. Any two alternatives visible
to one final basis probe have the same memory value, proving availability.

For $\eta_{00}$ and $f_{00}$,

$$
f_{00}EQ_{00}U\eta_{00}=\frac12,
\qquad
f_{00}EQ_{11}U\eta_{00}=\frac12.
$$

The two alternatives belong to different record sectors and their cross term
is $1/4$, so $E$ is a witnessed eraser.

By contrast,

$$
N|b,m\rangle
=
\frac{|0,m\rangle+(-1)^b|1,m\rangle}{\sqrt2}.
$$

Two distinct nonzero alternatives have the same memory value, so correlation
fails.

Finally,

$$
Q_{00}U\eta_{00}=\frac{|00\rangle}{\sqrt2},
$$

and the $|00\rangle$ component of $V|00\rangle$ is $1/\sqrt2$. Hence

$$
f_{00}VQ_{00}U\eta_{00}=\frac12.
$$

Every factor is a typed generator or declared composite in the amplitude
category. Repeated powers remain distinct, so no finite-arrow contradiction
arises. $\square$

### Definition 4.3 — the stable-record algebra

The W3 record algebra at $x_1$ is

$$
R_W=C^*(P_0,P_1)
=
\operatorname{span}\{I,Z_m\},
$$

where $Z_m=I_b\otimes Z$. Historical occurrence is certified by the write
test. Availability remains continuation-relative: $V$ preserves it and $E$
does not.

Theorem 4.2 earns the first rung

$$
\boxed{\texttt{RQ0-L0-REPRESENTABLE-W3-SKETCH}}.
$$

It makes no support or localization claim.

---

## 5. Counterfactual observability of a stable record

### 5.1 Eligible transports are part of the process law

Fix an internal W3-positive diagram \(W\). It contains its typed write,
preserving and erasing continuations, preparations, probes, fine alternatives
and coarse record projectors. Write \(x_W\) for its record boundary and

$$
R_W=C^*(P_r:r\in\mathsf{Val}(W))
\subseteq \mathfrak B_{x_W}.
$$

For another boundary \(y\), let
\(\mathsf{Tr}_D(y,W)\) be the family of channel diagrams in the admitted
grammar whose Schrödinger direction is \(y\to x_W\). The family is not a
support annotation. Its members are executable counterfactual experiments in
the nomological process law. A boundary is eligible when this family is
nonempty.

The dependence on \(W\), \(y\), and the admitted transport grammar is
deliberate. No unique record or boundary is selected. The construction is
applied to every internally W3-positive diagram and every eligible boundary,
and exact symmetries are retained.

### Definition 5.1 — counterfactual observability algebra

For an eligible pair \((W,y)\), define

$$
\mathcal A_W(y)
=
C^*\!\left(
\Phi_a^*(P):
a\in\mathsf{Tr}_D(y,W),\ P\in R_W
\right)
\subseteq \mathfrak B_y.
$$

All maps in this formula are channel maps. Thus
\(\Phi_a^*\) is unital completely positive and
\(\Phi_a^*(I)=I\). The definition does not replace a channel by
\(a^\dagger(-)a\) when \(a\) is a nonunital amplitude. For a unitary
amplitude arrow the two expressions agree.

We use the following exact classifications:

$$
\begin{array}{c|c}
\mathcal A_W(y)=\mathbb C I_y & \text{trivial observability}\\
\mathbb C I_y\subsetneq\mathcal A_W(y)\subsetneq\mathfrak B_y
 & \text{proper record relevance}\\
\mathcal A_W(y)=\mathfrak B_y & \text{global observability}.
\end{array}
$$

The middle line says only that a proper part of the admitted operator law is
relevant to the record. It does not yet say that this part can be independently
prepared, controlled, discarded or read as a region.

### Theorem 5.2 — observability theorem

At finite-dimensional channel scope, \(\mathcal A_W(y)\) has the following
properties.

1. It is the least unital \(C^*\)-subalgebra of \(\mathfrak B_y\) containing
   every admitted Heisenberg image of \(R_W\).
2. Enlarging \(\mathsf{Tr}_D(y,W)\) can only enlarge the algebra.
3. An exact isomorphism of Weld process sketches preserving the admitted
   grammar and carrying \(W\) to \(W'\) carries
   \(\mathcal A_W(y)\) isomorphically to
   \(\mathcal A_{W'}(y')\).
4. A presentation gauge \(J_y\) sends
   \(\mathcal A_W(y)\) to
   \(J_y\mathcal A_W(y)J_y^\dagger\).
5. Renaming arrow handles, record handles or configuration labels while
   preserving the represented channels, projectors and typing does not change
   the algebra except by the corresponding presentation isomorphism.
6. An external field purporting to name the support of \(W\) is invisible to
   the construction.

*Proof.* The intersection of all unital \(C^*\)-subalgebras containing the
displayed generator family is itself a unital \(C^*\)-subalgebra and is
precisely the generated algebra. This proves existence and minimality.
Generator inclusion proves monotonicity.

An isomorphism or gauge transports each generator by conjugation:

$$
\Phi_a^*(P)
\longmapsto
J_y\Phi_a^*(P)J_y^\dagger.
$$

Conjugation commutes with sums, products, adjoints and norm closure, proving
the covariance statements. Handle and label renamings do not occur in the
formula. An external support field also does not occur. \(\square\)

The last clause is a no-smuggling theorem of limited but useful scope. It
does not prove that the admitted counterfactual law is uniquely forced by a
realized history. It proves that, once the law is fixed, no independently
attached support list participates in the answer.

### Proposition 5.3 — clean-product law

Let the ambient boundary factor as \(H_A\otimes H_B\), let the record
algebra be \(R_A\otimes I_B\), and suppose every admitted transport relevant
to this calculation is a product channel

$$
\Phi_\alpha^A\otimes\Psi_\alpha^B
$$

with \((\Psi_\alpha^B)^*(I_B)=I_B\). Then

$$
\mathcal A_W
=
C^*\!\left((\Phi_\alpha^A)^*(R_A)\right)\otimes I_B.
$$

*Proof.* For every \(P\in R_A\),

$$
(\Phi_\alpha^A\otimes\Psi_\alpha^B)^*(P\otimes I_B)
=
(\Phi_\alpha^A)^*(P)\otimes I_B.
$$

Taking the generated algebra proves the result. \(\square\)

In particular, if the \(A\)-side counterfactual orbit generates
\(B(H_A)\), the product observability algebra is exactly
\(B(H_A)\otimes I_B\). The result is not weakened by the existence of
independent \(B\)-controls, provided their Heisenberg maps remain unital.

The unitality condition is load-bearing. For a bare amplitude product
\(a_A\otimes b_B\),

$$
(a_A\otimes b_B)^\dagger(P\otimes I_B)(a_A\otimes b_B)
=
a_A^\dagger Pa_A\otimes b_B^\dagger b_B,
$$

so a nonisometric spectator can be imported into the alleged support. The
channel definition prevents this silent switch.

### 5.2 Exact calculation for the branch-memory seed

At the record boundary \(x_1\), the identity transport gives

$$
\mathcal A_W(x_1)=R_W=\operatorname{span}\{I,Z_m\}.
$$

At \(x_0\), include the two admitted counterfactual write transports \(U\)
and \(N\). Their unitary Heisenberg actions give

$$
N^\dagger Z_m N=Z_m,
\qquad
U^\dagger Z_m U=X_bZ_m.
$$

The two generators commute and are independent. Hence

$$
\mathcal A_W(x_0)
=
C^*(Z_m,X_bZ_m)
=
\operatorname{span}
\{I,Z_m,X_b,X_bZ_m\}.
$$

This is a four-dimensional maximal abelian algebra inside
\(M_4(\mathbb C)\). It is proper and nontrivial. The branch-memory record is
therefore record-relevant at \(x_0\); no tensor-factor name was read by the
definition.

The base grammar contains only unitary channels. A unitary-conjugation
channel is invertible, and an invertible idempotent channel is the identity.
Consequently the base grammar contains no idempotent channel with this proper
algebra as its range. The seed is a first exact instance of

$$
\boxed{\text{proper record relevance}
\ne\text{independent addressability}.}
$$

Theorem 5.2 and this nontrivial control earn

$$
\boxed{\texttt{RQ0-L0-W3-OBSERVABILITY-SUPPORT}}.
$$

The word support here means counterfactual operator support, not spatial
support.

---

## 6. Independent addressability

### Definition 6.1 — admitted UCP split

Let \(\mathcal A\subseteq\mathfrak B_y\) be a unital \(C^*\)-subalgebra and
let \(i:\mathcal A\hookrightarrow\mathfrak B_y\) be its inclusion. An
addressability certificate in this paper is an admitted Heisenberg channel

$$
E:\mathfrak B_y\longrightarrow\mathcal A
$$

such that

$$
E\text{ is unital and completely positive},
\qquad
E i=\operatorname{id}_{\mathcal A}.
$$

Equivalently, \(e=iE\) is an admitted UCP idempotent on
\(\mathfrak B_y\), has range \(i(\mathcal A)\), and fixes that range
pointwise. Because the range is already a \(C^*\)-subalgebra, this strict
certificate is a conditional expectation at the finite scope used here.
The certificate must occur in the admitted channel grammar; its abstract
existence in the category of all linear maps is insufficient.

Indeed, every \(a\in\mathcal A\) lies in the multiplicative domain of \(e\):
\(e(a^\dagger a)=a^\dagger a=e(a^\dagger)e(a)\), and similarly for
\(aa^\dagger\). Hence
\(e(aXb)=ae(X)b\) for \(a,b\in\mathcal A\), the conditional-expectation
bimodule identity.

This choice is intentionally narrower than all possible notions of a quantum
subsystem:

- a multiplicative retract requires a \(*\)-homomorphic \(E\);
- the present conditional expectation is UCP but need not be multiplicative;
- a general CP split may be nonunital or have a Choi--Effros range product;
- a reversible dilation requires an explicitly admitted ancilla and unitary
  comprehension;
- a noiseless factor is defined by a represented algebra and its commutant.

These notions can disagree. This paper proves results only for the admitted
UCP split above.

Categorical comprehension and splitting constructions for general
finite-dimensional von Neumann subsystems provide a broader comparison class
[8]. No result from that broader setting is used to infer that the strict
split above is admitted.

### Definition 6.2 — chart status

For every eligible \((W,y)\), return exactly one of:

$$
\begin{array}{ll}
\texttt{TRIVIAL-RECORD-ORBIT}
 & \mathcal A_W(y)=\mathbb CI_y,\\
\texttt{GLOBAL-RECORD}
 & \mathcal A_W(y)=\mathfrak B_y,\\
\texttt{RECORD-RELEVANT-NOT-ADDRESSABLE}
 & \mathcal A_W(y)\text{ is nontrivial proper but no admitted split is present},\\
\texttt{ADDRESSABLE-W3-CHART}
 & \mathcal A_W(y)\text{ is nontrivial proper and has an admitted split},\\
\texttt{UNDERDETERMINED-UP-TO-SYMMETRY}
 & \text{several exact symmetry-related addressable candidates remain}.
\end{array}
$$

The last status is not an algorithmic failure. It prohibits an ungrounded
choice of representative.

### Proposition 6.3 — exact heterogeneous product chart

Take the branch-memory seed on \(H_A=\mathbb C^4\) and an independently
controlled qutrit spectator \(H_B=\mathbb C^3\). Admit only unital product
transports in the observability calculation. Then

$$
\mathcal A_W(x_0)
=
\mathcal A_0\otimes I_3,
\qquad
\mathcal A_0=C^*(X_b,Z_m).
$$

Let

$$
e_A(X)
=
\frac14\sum_{g\in\{I,X_b,Z_m,X_bZ_m\}}gXg^\dagger.
$$

This is the group average onto the commutant of the displayed abelian Pauli
group. That commutant is exactly \(\mathcal A_0\). With normalized qutrit
trace \(\tau_3\), define

$$
e_{A|B}(X)
=
e_A\!\left((\operatorname{id}\otimes\tau_3)(X)\right)\otimes I_3.
$$

It is UCP, idempotent, fixes \(\mathcal A_0\otimes I_3\), and has precisely
that range. If and only if this channel is in the admitted grammar, the
record-relevant algebra has the certificate used here and is an addressable
W3 chart.

*Proof.* Proposition 5.3 gives the observability algebra. Finite group
averaging is UCP and projects onto the fixed-point algebra. Partial normalized
trace is UCP. Their composite has the asserted range and fixes it
pointwise. \(\square\)

The tensor factorization is verification data for this hand control. It is
not an input field to Definition 5.1.

### Theorem 6.4 — counterfactual-completion separation

Identical realized W3 amplitudes and record laws do not determine either
addressability or record relevance from realized data alone.

*Construction and proof.* Keep the exact branch-memory W3 diagram of
Section 4 fixed in three Weld sketches.

1. In \(\mathbb P_{\mathrm{base}}\), retain only the displayed unitary channel
   grammar. The algebra at \(x_0\) is the proper \(\mathcal A_0\), but it has
   no admitted split.
2. In \(\mathbb P_{\mathrm{split}}\), add the exact channel \(e_A\) above as
   an admitted counterfactual operation. The realized W3 diagram is
   unchanged, while \(\mathcal A_0\) becomes addressable. Closing the grammar
   under composites with \(e_A\) does not enlarge observability because
   \(e_A\) fixes \(\mathcal A_0\) pointwise.
3. In \(\mathbb P_{\mathrm{mix}}\), instead add typed alternative unitary
   transports \(a_k:x_0\to x_1\) represented by
   $$
   J_0,\quad
   I_b\otimes H_m,\quad
   \operatorname{CNOT}_{b\to m},\quad
   \operatorname{CNOT}_{b\to m}(H_b\otimes I_m).
   $$
   Here \(J_0:x_0\to x_1\) is a typed generator whose matrix is the
   \(4\times4\) identity; it is not the categorical identity because its
   source and target differ.
   Their images of \(Z_m\) include
   $$
   Z_m,\quad X_m,\quad Z_bZ_m,\quad X_bZ_m.
   $$
   Products with \(Z_m\) give \(Z_b\) and \(X_b\). Thus the generated
   algebra contains \(X_b,Z_b,X_m,Z_m\) and equals \(M_4(\mathbb C)\).

The write, preserve, erase, no-write, preparation and probe amplitudes of the
realized W3 experiment are identical in all three sketches. Only the admitted
counterfactual completion differs. The respective statuses are
record-relevant-not-addressable, addressable, and global. \(\square\)

This theorem is not a defect in the construction. It locates the ontological
input: localization claims depend on the physically admitted nomological
law, not on one realized record history. A theory that refuses to specify
counterfactual interventions must return underdetermination.

---

## 7. The Weld quantaloid

### 7.1 Accessible operator supports

Extend the exact represented matrices from \(\mathbb K\) to complex
finite-dimensional Hilbert spaces. For each admitted CP channel choose no
preferred Kraus list. Instead use its canonical Kraus support: the linear span
of any minimal Kraus family. Two minimal Kraus families differ by a unitary
mixing and therefore have the same span.

Let \(\mathscr S_D\) be the smallest represented complex linear dagger
subcategory of \(\mathbf{FinHilb}\) that contains:

1. every represented admitted amplitude generator;
2. every distinguished admitted preparation, effect and projector;
3. the Kraus support of every admitted channel; and
4. all identities,

and is closed under typed composition, adjoint and linear span. Write
\(\mathscr S_D(x,y)\subseteq B(H_x,H_y)\) for its hom-space.

This completion does not assert that every vector in a span is separately
executable. It records accessible operator support. A permanently inaccessible
matrix that belongs to no admitted amplitude, effect or channel support is
not added.

For an admitted channel with Kraus operators \(K_i:H_y\to H_x\),

$$
\Phi^*(P)=\sum_iK_i^\dagger P K_i
\in\mathscr S_D(y,y).
$$

Hence every observability algebra in Section 5 is contained in the
corresponding endomorphism support.

### Definition 7.1 — operator-support quantaloid

The objects of \(\mathcal Q_D\) are the represented boundary types. Define

$$
\mathcal Q_D(x,y)
=
\operatorname{Sub}_{\mathbb C}\bigl(\mathscr S_D(x,y)\bigr),
$$

ordered by inclusion. For \(U:x\to y\) and \(V:y\to z\), set

$$
V\odot U
=
\operatorname{span}\{vu:v\in V,\ u\in U\},
$$

$$
1_x=\operatorname{span}\{I_x\},
\qquad
U^\dagger=\operatorname{span}\{u^\dagger:u\in U\}.
$$

The join of an arbitrary family is the linear span of its union; the bottom
arrow is the zero subspace.

### Theorem 7.2 — quantaloid theorem

\(\mathcal Q_D\) is a small involutive quantaloid at the declared finite
representation scope.

*Proof.* Each hom is the complete lattice of subspaces of a fixed
finite-dimensional vector space. Matrix multiplication is bilinear, so
composition is well typed, associative, and preserves arbitrary linear-span
joins in each variable. The spans of identities are two-sided identities.
Adjoint reverses composition, preserves joins, is involutive, and sends
identities to identities:

$$
(V\odot U)^\dagger=U^\dagger\odot V^\dagger,
\qquad
(U^\dagger)^\dagger=U.
$$

There are finitely many boundary objects and set-sized hom-lattices, so the
quantaloid is small relative to the fixed universe. \(\square\)

### Proposition 7.3 — covariance and dormant exclusion

An exact presentation isomorphism or boundary gauge induces an involutive
quantaloid isomorphism

$$
U\longmapsto J_yUJ_x^\dagger.
$$

If a raw matrix is permanently absent from the amplitude generators, effects,
projectors and Kraus supports and is not generated from them by the declared
closures, it does not occur in \(\mathscr S_D\) or \(\mathcal Q_D\).

*Proof.* Conjugation is linear, bijective, composition preserving and
adjoint preserving. The second statement is immediate from the least-closure
definition. \(\square\)

This theorem does not make \(\mathcal Q_D\) an inverse quantal frame, a
locale, or a localic groupoid. Those structures require additional
distributivity, support and inverse-semigroup axioms. Operator-subspace
quantaloids and weakly closed operator bimodules have close precedents in the
theory of quantum relations [2], but the finite construction above is proved
directly.

---

## 8. W3 Isbell concepts

### 8.1 Residuation in the Weld quantaloid

Because composition in a quantaloid preserves joins, it has right adjoints in
each variable. In the present concrete quantaloid, for
\(U:x\to y\), \(V:y\to z\), and \(H:x\to z\), define

$$
H\swarrow U
=
\{v\in\mathscr S_D(y,z):vU\subseteq H\},
$$

$$
V\searrow H
=
\{u\in\mathscr S_D(x,y):Vu\subseteq H\}.
$$

These are linear subspaces and are the largest arrows satisfying

$$
V\odot U\subseteq H
\quad\Longleftrightarrow\quad
V\subseteq H\swarrow U
\quad\Longleftrightarrow\quad
U\subseteq V\searrow H.
$$

### Definition 8.1 — process-probe and W3 categories

Define a discrete \(\mathcal Q_D\)-category
\(\mathsf{Proc}_D\). Its objects are pairs

$$
p=(y,U),
$$

where \(U\in\mathcal Q_D(y,y)\) is canonically generated by a finite
family of represented admitted endomorphism/effect/Kraus supports, or is one
of the derived algebras \(\mathcal A_W(y)\). Equal represented subspaces are
identified regardless of their generating handles. These are mathematical
support probes extracted from admitted process data; they are not thereby
separately executable interventions. Their extent is \(|p|=y\). The hom is
\(1_y\) on an object and the bottom arrow otherwise.

Define a second discrete \(\mathcal Q_D\)-category
\(\mathsf{W3}_D\). Its objects are pairs

$$
w=(W,y)
$$

where \(W\) is an internal W3-positive diagram and \(y\) is an eligible
source boundary for \(W\). Again \(|w|=y\), with identity hom on an object
and bottom otherwise.

No support label enters either object class. \(\mathsf{W3}_D\) is the full
declared collection of internally positive diagrams, not one diagram selected
after seeing the desired chart.

### Definition 8.2 — observability distributor

Use the convention that a distributor
\(\Phi_D:\mathsf{Proc}_D\nrightarrow\mathsf{W3}_D\) has components

$$
\Phi_D(w,p):|p|\longrightarrow|w|.
$$

For equal extent \(y\), put

$$
\Phi_D\bigl((W,y),(y,U)\bigr)
=
\mathcal A_W(y)\swarrow U.
$$

For unequal extents, put the bottom arrow. The component is an exact
operator subspace, not a Boolean fact-law label. It detects ordinary
incidence through

$$
1_y\subseteq\Phi_D\bigl((W,y),(y,U)\bigr)
\quad\Longleftrightarrow\quad
U\subseteq\mathcal A_W(y).
$$

### Proposition 8.3 — distributor typing

\(\Phi_D\) is a \(\mathcal Q_D\)-distributor.

*Proof.* With the convention above, the distributor inequality is

$$
\mathsf{W3}_D(w,w')
\odot\Phi_D(w,p)
\odot\mathsf{Proc}_D(p',p)
\subseteq
\Phi_D(w',p').
$$

For discrete enriched categories, a nonbottom left side requires
\(w=w'\) and \(p=p'\). The inequality then reduces to multiplication by
identity arrows on both sides. In every other case it is the bottom
inclusion. Typing follows from the equal-extent clause. \(\square\)

The use of discrete source and target categories is a declared first rung. It
does not assert a nontrivial order among probes or among W3 diagrams. The
nontrivial information is in the exact residual-valued incidence.

### 8.2 Isbell fixed points

Let \(\mathcal P\mathsf{Proc}_D\) and
\(\mathcal P^\dagger\mathsf{W3}_D\) be the contravariant and covariant
presheaf \(\mathcal Q_D\)-categories. For the distributor above, define

$$
(\Phi_D)_\uparrow(\mu)
=
\Phi_D\swarrow\mu,
\qquad
\Phi_D^\downarrow(\lambda)
=
\lambda\searrow\Phi_D.
$$

The residual identities give the Isbell adjunction

$$
(\Phi_D)_\uparrow
\dashv
\Phi_D^\downarrow.
$$

Thus

$$
C_D=\Phi_D^\downarrow(\Phi_D)_\uparrow
$$

is a closure monad on \(\mathcal P\mathsf{Proc}_D\). Define

$$
\mathsf{Con}_{W3}(D)
=
\operatorname{Fix}(C_D).
$$

Equivalently, an Isbell concept is a pair \((\mu,\lambda)\) satisfying

$$
\lambda=(\Phi_D)_\uparrow\mu,
\qquad
\mu=\Phi_D^\downarrow\lambda.
$$

The general theorem for a distributor over a small quantaloid states that
these fixed points form a skeletal complete \(\mathcal Q_D\)-category [3].
Its hypotheses hold here by Theorem 7.2 and Proposition 8.3. We import only
that enriched completeness theorem; the new observability distributor and
its physical filtering are the constructions of this paper.

For intuition, the identity test above has the ordinary formal-concept
shadow

$$
O=R^\downarrow,
\qquad
R=O^\uparrow,
$$

where \(O\) is a family of process supports, \(R\) is a family of W3
diagrams, and incidence means \(U\subseteq\mathcal A_W(y)\). This Boolean
shadow is not substituted for the residual-valued construction.

### Definition 8.4 — the observable algebra of a concept

For a fixed point \(c=(\mu,\lambda)\) of extent \(y\), let

$$
\mathsf{Rel}(c)
=
\{(W,y):
1_y\subseteq\lambda(W,y)\}.
$$

When this family is nonempty, define

$$
\mathcal A_c
=
\bigcap_{(W,y)\in\mathsf{Rel}(c)}\mathcal A_W(y).
$$

It is a unital \(C^*\)-subalgebra. The concept is **addressable** when
\(\mathcal A_c\) is proper and the admitted channel grammar contains a UCP
split onto it.

This intersection is derived after the Isbell fixed point. It is not a
planted intersection of operation handles. If the record family is empty, no
W3 chart is declared.

### Proposition 8.5 — principal addressable concepts exist

Let \(W\) be an internal W3 diagram at eligible boundary \(y\), and suppose
\(\mathcal A_W(y)\) is proper with an admitted split. Then
\(\mathsf{Con}_{W3}(D)\) contains an addressable concept whose observable
algebra is exactly \(\mathcal A_W(y)\).

*Proof.* Take the process-probe object

$$
p_W=(y,\mathcal A_W(y))
$$

and its Yoneda presheaf \(Yp_W\). Apply the closure monad and pair
\(C_DYp_W\) with

$$
\lambda_W=(\Phi_D)_\uparrow Yp_W.
$$

The triangular identities of the adjunction imply that this is a fixed-point
pair. By residuation,

$$
1_y\subseteq\lambda_W(W',y)
\quad\Longleftrightarrow\quad
\mathcal A_W(y)\subseteq\mathcal A_{W'}(y).
$$

The family contains \(W\) itself, and every member's algebra contains
\(\mathcal A_W(y)\). Therefore its intersection is exactly
\(\mathcal A_W(y)\). The admitted split supplies the certificate.
\(\square\)

The heterogeneous product in Proposition 6.3 therefore gives a nonempty
addressable Isbell concept. Isbell closure alone still does not make any
concept physical: the split is an independent gate.

### Theorem 8.6 — incidence no-smuggling and covariance

Suppose two presentations have the same represented admitted amplitude and
channel law, the same internally derived W3 decisions, the same projectors
and the same transport maps, up to exact process isomorphism. Then their
quantaloids, distributors, Isbell fixed-point categories and addressable
principal concepts are isomorphic.

In particular, changing only operation handles, record handles, tensor-factor
names, external access lists or proposed region identifiers cannot change the
construction.

*Proof.* The process isomorphism induces the quantaloid isomorphism of
Proposition 7.3 and carries every \(\mathcal A_W(y)\) by Theorem 5.2.
Residuals are characterized by a universal order property and are therefore
preserved. Hence the distributor is transported componentwise. Isbell
adjunctions and their fixed points are functorial under the induced
infomorphism, and admitted split maps transport by conjugation. The listed
metadata occur in none of these operations. \(\square\)

This earns typed, addressable W3 concepts. It does not discover a spatial
cover.

---

## 9. Chart groupoid, record interface and symmetry

### Definition 9.1 — raw W3 chart groupoid

An object of \(\mathfrak{Chart}^{\mathrm{raw}}_{W3}(D)\) is a tuple

$$
c=(\mu,\lambda,y,\mathcal A_c,E_c,\mathsf P_c)
$$

where:

1. \((\mu,\lambda)\) is an addressable Isbell fixed point of extent \(y\);
2. \(E_c\) is an admitted UCP split onto \(\mathcal A_c\); and
3. \(\mathsf P_c\) is the family of transported W3 projector resolutions in
   \(\mathsf{Rel}(c)\).

An arrow is an exact process-sketch isomorphism carrying boundaries,
admitted amplitude and channel grammar, the fixed-point presheaves,
\(\mathcal A_c\), the split, and every projector resolution to the
corresponding target data. Only isomorphisms are retained, so this is a
groupoid.

### Definition 9.2 — partial record interface

A chart is record-compatible when all projectors in \(\mathsf P_c\), after
their declared transports to \(y\), commute. Only then define

$$
\operatorname{Rec}(c)
=
\operatorname{Bool}\langle\mathsf P_c\rangle
\hookrightarrow
\operatorname{Proj}(\mathcal A_c).
$$

For a chart isomorphism \(F:c\to c'\) whose Heisenberg map pulls target
projectors back to source projectors, define

$$
\operatorname{Rec}(F):
\operatorname{Rec}(c')
\longrightarrow
\operatorname{Rec}(c)
$$

by exact projector pullback. Identities and composite process isomorphisms
give identity and composite Boolean maps. Thus

$$
\operatorname{Rec}:
\mathfrak{Chart}^{\mathrm{rec}}_{W3}(D)^{op}
\longrightarrow
\mathsf{BoolAlg}
$$

is a contravariant functor on the record-compatible subgroupoid.

Record handles play no role: replacing every name while preserving projector
operators and dynamics gives a naturally isomorphic functor. The functor is
partial because noncommuting record families are not silently forced into one
Boolean algebra.

### Definition 9.3 — presentation quotient

The declared presentation gauge \(G_D\) acts on every datum in Definition
9.1 by boundary conjugation and the induced quantaloid, presheaf, split and
projector maps. Define the presentation quotient groupoid

$$
\mathfrak{Chart}_{W3}(D)
=
\bigl[
\mathfrak{Chart}^{\mathrm{raw}}_{W3}(D)/G_D
\bigr].
$$

This quotient removes presentation redundancy only. The physical symmetry
group \(\operatorname{Aut}_{\mathrm{phys}}(D)\) acts on the quotient as a
separate group. It is not divided out merely because it preserves the law.

The same gauge acts on the correspondence data of Section 10. Conjugation
\(\operatorname{Ad}_{J_y}\) is a \(*\)-isomorphism of each represented
algebra; transport of left actions and the boundary unitary give an
equivalence of Hilbert correspondences. Interior tensor products and unitary
2-cells are preserved up to their canonical unitary identifications.
Therefore gauge-related cospans have equivalent overlap cone prestacks.
This verifies gauge covariance of the higher comparison datum without
quotienting a genuine physical symmetry.

### Theorem 9.4 — automorphism no-selection

Let a physical automorphism group \(G\) act transitively on a set of at least
two addressable chart objects. If every available discriminator is
\(G\)-invariant, no \(G\)-invariant rule selects one chart.

*Proof.* If a selected chart \(c\) were invariant, then
\(g c=c\) for all \(g\in G\). Transitivity would make every chart equal to
\(c\), contrary to the existence of at least two distinct objects.
\(\square\)

The forced conclusion is nonselection. This paper represents that conclusion
by retaining all candidates and all physical symmetry arrows. It does not
claim that a groupoid is the unique possible ontology in every theory.

### 9.1 Symmetric-copy control

Take two identical copies of the addressable heterogeneous product of
Proposition 6.3 and admit the swap as a physical automorphism, not as
presentation gauge. The two copied internal W3 diagrams have isomorphic
observability algebras and transported UCP splits. Swap exchanges the two
principal Isbell concepts.

With no asymmetric admitted preparation, probe or control, Theorem 9.4
forbids a preferred copy. Both chart objects and the swap remain. Nothing in
this result says that the copies are spatially separated.

Theorems 7.2, 8.3, 8.5, 8.6 and the construction above jointly establish the
provisional rung

$$
\boxed{\texttt{RQ0-L0-WELD-QUANTALOID-CHARTS}}.
$$

Its terminal status is subject to the two external reviews required by the
pin.

---

## 10. Higher physical overlap: definition, one theorem, and a limit

### 10.1 The independently fixed map bicategory

Let \(\mathbf{Corr}_{fd}\) be the bicategory whose objects are
finite-dimensional \(C^*\)-algebras, including the zero algebra; whose
1-morphisms \(A\to B\) are finite right Hilbert \(B\)-modules equipped with
a nondegenerate left \(*\)-representation of \(A\); and whose 2-morphisms are
unitary bimodule intertwiners. Horizontal composition is the interior relative
tensor product, and the identity on \(A\) is the standard
\({}_AA_A\) correspondence. This standard composition is associative up to
the canonical unitary associator [4].

An inclusion \(i_A:A\hookrightarrow D\) of a unital chart algebra determines
the correspondence \({}_AD_D\). Thus addressable chart comparisons have a
typed image in \(\mathbf{Corr}_{fd}\). The bicategory is fixed before any
particular pair of charts is compared.

### Definition 10.1 — overlap cone prestack

For a cospan of chart correspondences

$$
A\xrightarrow{i_A}D\xleftarrow{i_B}B,
$$

define, for every test algebra \(X\), the groupoid

$$
\mathsf{Ov}_{A,B;D}(X)
=
\mathbf{Corr}_{fd}(X,A)
\times^h_{\mathbf{Corr}_{fd}(X,D)}
\mathbf{Corr}_{fd}(X,B).
$$

Its objects are triples \((u,v,\alpha)\), where

$$
u:X\to A,
\qquad
v:X\to B,
\qquad
\alpha:i_A\circ u\Rightarrow i_B\circ v
$$

and \(\alpha\) is a unitary 2-cell. Its arrows are pairs of unitary
intertwiners compatible with \(\alpha\). Precomposition makes
\(\mathsf{Ov}_{A,B;D}\) a pseudofunctor
\(\mathbf{Corr}_{fd}^{op}\to\mathbf{Grpd}\).

### Definition 10.2 — physical bicategorical overlap

A physical overlap for the cospan is an object \(P\), correspondences
\(P\to A\) and \(P\to B\), and a comparison 2-cell that represent the cone
prestack:

$$
\mathbf{Corr}_{fd}(X,P)
\simeq
\mathsf{Ov}_{A,B;D}(X)
$$

pseudonaturally in \(X\).

This is the explicit higher universal property. The definition does not
assert that such a \(P\) exists.

### Warning 10.3 — tensor product is composition, not pullback

For correspondences \(E:A\to D\) and \(F:D\to B\), the relative tensor
product

$$
E\otimes_DF
$$

is their composite \(A\to B\). It is not, merely by being a balanced tensor
product, a representing object for Definition 10.2. No such identification
is made here.

### Theorem 10.4 — finite commutative central-corner control

Let \(D=\mathbb C^n\) and let \(p,q\) be central projections. Put

$$
A=pD,
\qquad
B=qD,
\qquad
P=pqD.
$$

Use the corner correspondences \(pD:A\to D\) and \(qD:B\to D\). Then
\(P\), with the evident corner correspondences to \(A\) and \(B\),
represents \(\mathsf{Ov}_{A,B;D}\).

*Proof.* A finite Hilbert \(D\)-module decomposes canonically into its
\(n\) coordinate Hilbert spaces. A correspondence into \(pD\) has zero
coordinate fibers outside the support of \(p\); extension along
\(pD:A\to D\) preserves its remaining fibers and inserts zeros elsewhere.
The analogous statement holds for \(q\).

If the two extensions to \(D\) are unitarily isomorphic, their coordinate
modules agree and vanish outside both supports. Hence they are supported on
the intersection, the support of \(pq\), and factor through a unique
\(X\)-\(pqD\) correspondence up to its unitary intertwiner. Conversely, any
correspondence into \(pqD\) extends to such a compatible pair. This
equivalence respects unitary arrows and precomposition in \(X\), giving the
required pseudonatural groupoid equivalence. \(\square\)

When \(pq=0\), the representing object is the zero algebra: the overlap is
empty at this scope. When \(pq\ne0\) but no compatible W3 projector survives
on it, the overlap is process-only. It is record-bearing only when exact
projector pullbacks define a nontrivial Boolean interface there.

The groupoid-valued cone retains automorphisms of mediating
correspondences. Thus a symmetry control does not become a falsely unique
set-valued intersection.

### 10.2 What is and is not recovered

The terminal RQ0-A construction supplies declared amplitude instruments and
declared maps

$$
O\longrightarrow D_a\longrightarrow\mathsf E
$$

with exact projector pullbacks. In its own finite thin cover category, the
tested pair and triple diagrams descend. This remains a positive control for
a declared physical overlap and for contravariant record maps.

It is not promoted to a theorem that \(O\) represents Definition 10.2 in
\(\mathbf{Corr}_{fd}\). Nor does this paper prove that arbitrary pairs of
addressable Isbell charts possess bicategorical pullbacks. General
representability of \(\mathsf{Ov}\), and the agreement of direct and
composite \(\operatorname{Rec}\) maps on those general overlaps, remain open.

The result of this section is therefore:

$$
\boxed{
\text{a typed higher overlap test}
+
\text{one commutative representability theorem},
}
$$

not a general derived quantum overlap construction.

---

## 11. Weld datum versus a conjectural Weld stack

### Definition 11.1 — the earned finite-dimensional Weld datum

At one fixed represented process sketch \(D\), define

$$
\mathbb X_D
=
\left(
\mathcal Q_D,\,
\mathfrak{Chart}_{W3}(D),\,
\operatorname{Rec}_{\mathrm{partial}}
\right).
$$

The first component is the involutive operator-support quantaloid. The second
is the presentation-gauge quotient groupoid of addressable Isbell concepts,
with physical automorphisms retained separately. The third is the
contravariant Boolean interface on record-compatible chart isomorphisms.

This is a finite-representation Weld datum. It is not a stack.

### Definition 11.2 — obligations for a genuine Weld stack

A future Weld stack would require, at minimum:

1. an independently specified test category of process sketches and maps;
2. a Grothendieck topology or another exact covering doctrine;
3. a category or higher groupoid of Weld data over every test object;
4. restriction pseudofunctors and coherent 2-morphisms;
5. effective descent for objects and arrows;
6. a proved treatment of presentation gauge and stabilizers;
7. representable or otherwise controlled higher physical overlaps; and
8. a precise declaration of whether the moduli object is ordinary, analytic,
   real-analytic, derived, or some combination.

None of these obligations follows from one quotient groupoid. Derived moduli
of objects in dg-categories supply an important algebraic precedent [5], but
they do not automatically provide a \(C^*\), unitary, dagger-compatible
analytic stack for the present process sketches. That comparison is a
research direction, not a proof.

Accordingly,

$$
\boxed{\texttt{CONJECTURAL-WELD-STACK}}
$$

is only a design label. The pre-registered rung
\(\texttt{RQ0-L0-WELD-STACK}\) is not earned.

Condensed mathematics may eventually provide a useful substrate for
topological and analytic passage to continua [6]. It neither defines the
finite counterfactual support nor supplies the missing descent theorem, so it
does no work in the positive results above.

---

## 12. Conditional classical shadow

This section gives sufficient gates, not a derivation.

Suppose a coarse endomorphism part of a future Weld datum satisfies all of the
following.

1. Its relevant quantale is a unital inverse quantal frame, rather than an
   arbitrary noncommutative operator-subspace quantale.
2. The chart moduli satisfy effective descent and have controlled or trivial
   stabilizers at the desired classical truncation.
3. Physical overlaps are representable and become underived/transverse at
   the coarse scale.
4. The resulting locale is spatial.
5. Its space of points is Hausdorff, second countable at the declared limit,
   and locally Euclidean of a stable dimension.

Under the first condition, the inverse-quantal-frame/localic-groupoid
correspondence produces an étale localic groupoid at the appropriate scope
[7]. Conditions 2 and 3 allow a set- or locale-valued coarse atlas rather
than an unresolved higher groupoid. Condition 4 yields an ordinary topological
space. Condition 5 makes that space a topological manifold candidate.

None of the hand controls in this paper satisfies this complete chain. In
particular:

$$
\text{operator-support quantaloid}
\not\Rightarrow
\text{inverse quantal frame}
\not\Rightarrow
\text{manifold}.
$$

No causal order, Lorentzian signature or spacetime interpretation follows
from the conditional chain. Agreement with an independently reconstructed
causal structure belongs to a later, unauthorized weld unit.

---

## 13. Mandatory hand-worked controls

The controls below separate the formal layers. Constructor knowledge is used
only to verify each answer after applying the definitions.

### C1 — branch-memory W3 seed

**Assumptions.** The exact sketch and grammar of Sections 3 and 4.  
**Calculation.** Theorem 4.2 gives write correlation, preserve availability,
eraser recoherence, failed control correlation and closed amplitude \(1/2\).
Section 5 gives
\(\mathcal A_W(x_0)=C^*(X_b,Z_m)\subsetneq M_4\).  
**Deduction.** The seed is representable and properly record-relevant, but
the unitary-only grammar supplies no proper idempotent split.  
**Non-claim.** It is not a region or a spatial support.

### C2 — clean heterogeneous product

**Assumptions.** The seed is tensored with a qutrit; spectator transports are
unital; the exact expectation \(e_{A|B}\) is admitted.  
**Calculation.** Proposition 5.3 removes the spectator from observability,
and Proposition 6.3 proves the UCP split.  
**Deduction.** An exact proper addressable W3 concept exists.  
**Non-claim.** Generic processes need not factor, and the visible tensor
presentation is not a localization algorithm.

### C3 — mixed interaction

**Assumptions.** Keep the W3 diagram but admit the four alternative transports
listed in Theorem 6.4.  
**Calculation.** Their record orbit generates
\(X_b,Z_b,X_m,Z_m\), hence \(M_4\).  
**Deduction.** A genuine interaction/counterfactual completion can turn the
same realized record into a global one.  
**Non-claim.** This algebraic globality is not causal nonlocality.

### C4 — symmetric identical copies

**Assumptions.** Two identical independently addressable copies and an exact
physical swap, with no asymmetric discriminator.  
**Calculation.** Swap exchanges the two principal Isbell concepts and their
splits.  
**Deduction.** No invariant representative exists; both candidates and the
physical symmetry action remain.  
**Non-claim.** Presentation gauge and physical exchange symmetry are not
identified.

### C5 — universal-control full matrix algebra

**Assumptions.** At a \(d\)-dimensional boundary, admit every unitary channel
and a nontrivial record projector \(0\ne P\ne I\).  
**Calculation.** The commutant of all conjugates \(U^\dagger P U\) is only
\(\mathbb CI\): an operator commuting with every projector of the fixed rank
must be scalar. The finite-dimensional bicommutant theorem then gives

$$
C^*(U^\dagger P U:U\in U(d))=M_d(\mathbb C).
$$

**Deduction.** Definition 5.1 returns \(\texttt{GLOBAL-RECORD}\), not a
proper chart.  
**Non-claim.** A globally observable record is not spatially ubiquitous.

### C6 — public quaternion object

**Assumptions.** Use the immutable public \(Q_8\) calibration exactly as
opened in the preceding architecture cycle.  
**Calculation.** Its three cyclic order-four subgroups and common central
order-two subgroup are genuine; \(Q_8\) has no proper normal direct-product
decomposition. Its W3 packages, however, are separate matrix witnesses
attached to subgroup lists through the external
\(\mathsf{access\_operations}\) field.  
**Deduction.** The group facts survive, but the object supplies no internal
\(W\), no derived \(\mathcal A_W\), and no addressable Isbell chart under the
definitions here.  
**Non-claim.** This is not a no-go theorem against an internally rebuilt
quaternion process.

### C7 — terminal RQ0-A

**Assumptions.** Use its declared amplitude instruments, signed-permutation
maps and projector pullbacks at the terminal finite scope.  
**Calculation.** The regional record restrictions agree through the declared
common subinstrument and compose in the finite cover category.  
**Deduction.** Once regions and maps are supplied, typed physical fact descent
is coherent and law matching is unnecessary.  
**Non-claim.** RQ0-A did not intrinsically discover those regions, and its
overlap is not silently promoted to a pullback in
\(\mathbf{Corr}_{fd}\).

---

## 14. Four-gate audit

| Primitive | Referent | Necessity | No-smuggling rule | Discriminator |
|---|---|---|---|---|
| admitted grammar | executable counterfactual experiments | realized amplitudes do not fix nomological possibilities | no support or region label occurs | three completions in Theorem 6.4 |
| internal W3 diagram | typed write, continuations, preparations, probes and projectors | record relevance needs an independently certified fact | all W3-positive diagrams are retained; no chosen support | write/preserve/erase/no-write controls |
| eligible boundary and transports | physical channels from a possible source to the record cut | Heisenberg observability needs a typed source | eligibility is composability in the grammar, not a coordinate | product versus mixed transport |
| observability algebra | least algebra visible through record counterfactuals | replaces external support lists | constructed only from channels and projectors | proper/global/trivial cases |
| admitted UCP split | physically executable discard/comprehension of a proper algebra | relevance alone gives no independent control | abstract linear retractions do not count | base seed versus split completion |
| accessible support category | amplitudes, effects and Kraus supports generated by admitted law | provides typed operator supports | dormant matrices are excluded by least closure | gauge copy and inaccessible completion |
| residual distributor | exact relation between a support subspace and W3 observability | retains all mutually determined concepts | values contain no region or fact-law label | identity test \(U\subseteq\mathcal A_W\) |
| presentation gauge | boundary-basis redundancy | presentation independence | physical automorphisms are excluded from the quotient | gauge conjugation versus physical swap |
| correspondence bicategory | physical higher maps between finite algebras | overlap requires an independent universal-property category | literal common handles do not enter | central-corner theorem versus open generic case |

Every primitive is nomological or operational, not spatial. The table does
not claim that nature has selected the admitted grammar.

---

## 15. Claim register and outcome

| Item | Status | Exact scope |
|---|---|---|
| finite-arrow scalar and spectral obstruction | theorem | finite categories with exact finite-dimensional complex representations |
| finitely presented Weld process sketch | definition and construction | finite dagger-linear presentation, generally infinite arrow set |
| branch-memory W3 representation | theorem | exact \(\mathbb Q(\sqrt2)\) matrices and declared grammar |
| counterfactual observability | definition and theorem | finite-dimensional admitted channel grammar |
| clean-product law | theorem | unital spectator channels |
| addressability certificate | definition | admitted UCP split onto a unital \(C^*\)-subalgebra |
| completion separation | constructive theorem | three exact grammars sharing one realized W3 diagram |
| Weld quantaloid | theorem | all subspaces of the least accessible operator-support category |
| observability distributor | construction and theorem | discrete probe/W3 \(\mathcal Q_D\)-categories |
| Isbell completeness | imported theorem, specialized here | small quantaloid and exact distributor |
| addressable principal concepts | theorem | proper observability algebra with admitted split |
| chart groupoid and partial \(\operatorname{Rec}\) | construction | record-compatible isomorphism subgroupoid |
| automorphism nonselection | theorem | transitive invariant physical symmetry |
| higher overlap prestack | definition | \(\mathbf{Corr}_{fd}\) |
| central-corner overlap | theorem | finite commutative central ideals |
| generic derived quantum overlap | open | representability not proved |
| Weld stack | conjectural design | site and effective descent absent |
| classical manifold shadow | conditional criterion | none of the examples passes the chain |

The highest provisional rung is

$$
\boxed{\texttt{RQ0-L0-WELD-QUANTALOID-CHARTS}}.
$$

It is supported by:

1. an exact replacement for the inconsistent finite-arrow language;
2. an internally represented W3 seed;
3. a handle-independent observability theorem;
4. an admitted physical addressability discriminator;
5. an involutive operator-support quantaloid;
6. a typed residual-valued Isbell construction with a positive addressable
   concept; and
7. a presentation-invariant chart groupoid retaining physical symmetry.

It does not include a general overlap theorem or a stack. A negative review
at either layer does not erase the earlier rungs.

---

## 16. Ontological result and first obstruction

The paper's positive ontology is modest but sharper than a support list.

> A candidate quantum chart is a mutually closed operation/record concept
> whose record relevance is generated by the admitted counterfactual process
> law and whose independent handling is witnessed by an admitted physical
> channel. It is retained up to presentation gauge and without selecting
> among physically symmetric alternatives.

This says what a chart is at pre-spatial L0. It does not say that the chart is
somewhere. Stable records provide the factual discriminator; the surrounding
quantum amplitudes remain part of the chart and can recohere under other
admitted continuations.

The first real unresolved obstruction is twofold.

1. The admitted counterfactual grammar remains a provisional nomological
   input. Theorem 6.4 proves that realized W3 data cannot determine it.
2. Even for addressable charts, the higher cone prestack need not be
   representable. Without general physical overlaps and effective descent,
   there is no Weld stack or atlas.

Those are constructive obligations, not no-go theorems. Spatial topology,
operational influence, causality, Lorentzian geometry, fields and gravity
remain outside this cycle.

---

## References

[1] B. Coecke, C. Heunen and A. Kissinger,
“Categories of quantum and classical channels,”
*Electronic Proceedings in Theoretical Computer Science* **158** (2014),
1–14, [arXiv:1408.0049](https://arxiv.org/abs/1408.0049).

[2] N. Weaver, “Quantum relations,”
*Memoirs of the American Mathematical Society* **215** (2012), no. 1010,
[arXiv:1005.0354](https://arxiv.org/abs/1005.0354).

[3] L. Shen and D. Zhang,
“Categories enriched over a quantaloid: Isbell adjunctions and Kan
adjunctions,” *Theory and Applications of Categories* **28** (2013),
577–615, [arXiv:1307.5625](https://arxiv.org/abs/1307.5625).

[4] A. Pander Maat, “Hilbert modules over \(C^*\)-categories,”
[arXiv:2305.10859](https://arxiv.org/abs/2305.10859), 2023.

[5] B. Toën and M. Vaquié, “Moduli of objects in dg-categories,”
*Annales scientifiques de l'École Normale Supérieure* **40** (2007),
387–444, [arXiv:math/0503269](https://arxiv.org/abs/math/0503269).

[6] D. Clausen and P. Scholze,
“Condensed Mathematics and Complex Geometry,”
[arXiv:2605.11731](https://arxiv.org/abs/2605.11731), 2026.

[7] P. Resende, “Étale groupoids and their quantales,”
*Advances in Mathematics* **208** (2007), 147–209,
[arXiv:math/0412478](https://arxiv.org/abs/math/0412478).

[8] S. Mestoudjian, M. Wilson, A. Vanrietvelde and P. Arrighi,
“Picturing general quantum subsystems,”
[arXiv:2511.09494](https://arxiv.org/abs/2511.09494), version 2, 2026.

[9] For conceptual comparison only, observable-induced tensor structures are
studied by P. Zanardi, D. A. Lidar and S. Lloyd,
“Quantum tensor product structures are observable-induced,”
*Physical Review Letters* **92** (2004), 060402,
[arXiv:quant-ph/0308043](https://arxiv.org/abs/quant-ph/0308043).
That work is not used as a proof of the addressability or overlap results
above.
