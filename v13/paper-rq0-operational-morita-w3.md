# Operational Morita Geometry of W3 Records

## Complete Instruments, Classical Algebra Objects, and Spectator-Stable Quantum Seams

**Version:** v0.1

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-01

**Governing pin:** `35a4878`

**Scope:** finite-dimensional, exact, analytical RQ0-L0

---

## Abstract

The preceding W3 seam-stack construction failed for one common reason: it
formed record candidates in a Hilbert-space presentation and only afterward
tried to remove incomplete probes, redundant grammar, matrix spectators and
ineffective stabilizers. This paper reverses that order.

We define a complete marked operational theory on finite Hilbert modules.
For a right Hilbert $A$-module $M$, the physical observable algebra is
$\mathcal L_A(M)$. Preparations, effects, complete outcome instruments,
channels and counterfactual comparisons form one candidate-independent
marking. A strong Morita equivalence $X:{}_A X_B$ transports $M$ to
$M\otimes_A X$ and induces a canonical *-isomorphism

$$
\mathcal L_A(M)
\cong
\mathcal L_B(M\otimes_A X).
$$

The complete marking is transported through these isomorphisms. W3 seams are
then constructed on the resulting marked Morita object, not on a raw carrier.

A sharp record interface is a finite classical algebra
$C\cong\mathbb C^\Omega$ acting on a boundary module. Equivalently it is a
commutative special dagger-Frobenius classical object with an admitted module
action. Embedded PVMs are concrete representatives. Preservation is tested
against the entire admitted output effect operator system. We prove

$$
\mathcal D_C T(a)=T(a) \forall a
\iff
p_rT(a)p_s=0\ \forall r\ne s,a
\iff
T(\mathcal E_{\rm out})\subseteq C',
$$

and keep this universal block law separate from sharp readable availability.
A complete output instrument supplies the latter; an eraser has an admitted
effect with a nonzero cross-sector block.

The construction is invariant under marked operational Morita equivalence.
Inaccessible matrix amplification is handled by the standard imprimitivity
bimodule rather than the ill-typed rule “tensor every preparation with an
identity.” A physically accessible spectator changes the marking and is not
removed. We construct an explicit finite rigidification by the normal kernel
of automorphisms acting trivially on every marked operational object. We also
construct the full category-valued addressability fibration, retaining all
admitted noninvertible Karoubi/CP arrows.

The complete branch-memory instrument still has nine W3 interfaces at atomic
fine rank. Its marked symmetry group is $U(1)\times S_4$ at the declared
monomial scope; the global phase is ineffective, while the effective $S_4$
action gives two retained symmetry components: six $2+1+1$ seams and three
$2+2$ seams. The familiar memory partition is not selected. The strongest
provisional result is

$$
\boxed{\texttt{RQ0-L0-FULL-ADDRESSABILITY-FIBRATION}}
$$

at the exact finite marked-Morita scope. “Addressability” still means
law-relative repeatable coarse-graining, not autonomous control or space. No
actual outcome, W6 co-reference, physical overlap, spatial localization,
topology, causality, field, or gravity claim is made.

---

## 1. Problem and claim boundary

### 1.1 The failed order

The immutable seam-stack paper started with concrete Hilbert spaces,
candidate projectors and selected experiment packets. Its two hostile reviews
accepted a fixed complete-packet nine-seam theorem but exposed four general
failures:

1. an incomplete probe subfamily can manufacture preserving availability;
2. the promised operational quotient was not the displayed moduli object;
3. the spectator comparison was ill-typed on preparations and effects and
   enlarged retained ineffective isotropy; and
4. the addressability fiber deleted admitted noninvertible Karoubi arrows.

These are not four independent bugs. Each comes from constructing the seam
before fixing the physical operational object.

### 1.2 The corrected order

This paper uses

$$
\boxed{
\text{complete operational marking}
\to
\text{marked Morita semantics}
\to
\text{classical W3 objects}
\to
\text{effective moduli and full fibers}.
}
$$

The construction is **law-relative**. The admitted state, effect,
instrument and counterfactual grammar is physical input. What is removed is
its redundant representation, not its counterfactual content.

### 1.3 Provisional cumulative outcomes

The registered ladder is:

$$
\begin{aligned}
&\texttt{RQ0-L0-COMPLETE-INSTRUMENT-W3},\\
&\texttt{RQ0-L0-MORITA-INVARIANT-W3-SEAMS},\\
&\texttt{RQ0-L0-EFFECTIVE-W3-SEAM-STACK},\\
&\texttt{RQ0-L0-FULL-ADDRESSABILITY-FIBRATION}.
\end{aligned}
$$

All four are provisional until three independent hostile reviews are frozen
and jointly adjudicated.

### 1.4 Terminology ceiling

In this paper:

- **complete** means complete relative to a fixed admitted operational law,
  not automatically all mathematical effects in a matrix algebra;
- **seam** means a W3-stable classical interface in a quantum process;
- **Morita invariant** means invariant under an equivalence preserving the
  full operational marking, not bare algebraic Morita equivalence;
- **stack** means a finite retained-symmetry moduli groupoid after explicit
  rigidification; and
- **addressability** means an admitted repeatable UCP coarse-graining and its
  full Karoubi category.

None of these words means spatial region, causal localization or autonomous
subsystem control.

---

## 2. Complete marked operational semantics

### Definition 2.1 — finite operational boundary chart

A finite operational boundary chart is a pair

$$
\mathsf x=(A_x,M_x),
$$

where $A_x$ is a finite-dimensional unital C*-algebra and $M_x$ is a finite,
full right Hilbert $A_x$-module. Its represented observable algebra is

$$
\mathcal O_x=\mathcal L_{A_x}(M_x),
$$

the C*-algebra of adjointable right-module endomorphisms.

The pair, not a preferred Hilbert-space basis, is the boundary presentation.
The familiar full-matrix representation is recovered from

$$
(A_x,M_x)=(\mathbb C,H_x),
\qquad
\mathcal O_x=B(H_x).
$$

### Definition 2.2 — complete operational marking

A complete marking $\mathcal M_D$ assigns to the boundary charts:

1. every admitted finite preparation instrument and all of its outcome
   branches;
2. every admitted readout instrument and its complete POVM, including all
   declared coarse-grainings;
3. every admitted CP process branch and UCP Heisenberg channel;
4. every admitted sequential and parallel composite used by the law;
5. every matched counterfactual comparison; and
6. every scalar experiment context generated by these data.

For a boundary $x$, let

$$
\mathcal E_D(x)
=
\operatorname{span}_{\mathbb C}
\{I, e_j: e_j\text{ is an outcome effect of an admitted readout at }x\}.
$$

Because every complete POVM is included, $\mathcal E_D(x)$ is a unital
self-adjoint operator system. It need not be all of $\mathcal O_x$.

The marking is fixed before a record candidate is tested. A seam may choose
an admitted complete instrument as a witness; it may not choose a favorable
proper subset of that instrument's outcomes or ignore another effect already
admitted at the same boundary.

### Definition 2.3 — preparation completeness

A preparation instrument is a finite family of CP branches whose classical
outcomes supply normalized postselected states

$$
(\rho_\alpha)_{\alpha\in A}
$$

with their nonzero occurrence weights. A W3 test using this source includes
all $\alpha\in A$. The complete theory may admit several source instruments;
the seam construction ranges over all of them.

This does not assert that every density operator is preparable. When full
state tomography is used, it is stated as a separate operational postulate.

### Definition 2.4 — represented operational image

Begin with any generator-and-relation syntax for $D$. Map every generator to
its actual state, effect, CP map, instrument branch or module intertwiner.
The **represented operational image** $\overline D$ is the image category of
this map, with two syntactic arrows identified exactly when they induce the
same typed operational transformation.

Equivalently, when the marking is separating, two arrows are equal in
$\overline D$ exactly when every complete marked scalar context evaluates
them equally.

### Proposition 2.5 — the operational quotient is a congruence

Equality in $\overline D$ is compatible with source, target, composition,
adjoint where declared, convex combination, outcome coarse-graining and
instrument summation.

*Proof.* Every constructor in the claim is a well-defined operation on the
represented state, effect, CP-map or module-intertwiner objects. Replacing one
representative by the same typed represented transformation leaves the result
unchanged. For the contextual formulation, placing equal arrows inside any
larger admitted context gives another admitted scalar context, hence equal
evaluation. Thus the quotient is taken before any seam object is formed.
$\square$

### Remark 2.6 — why this fixes the packet defect

The previous object ranged over arbitrary finite preparation and probe
subfamilies. Definition 2.2 instead fixes the complete admitted marking, and
Definition 2.3 requires all branches of a selected source instrument. A
candidate can no longer hide an admitted leakage witness by omitting its
effect handle.

---

## 3. The marked operational Morita bicategory

### Definition 3.1 — the correspondence bicategory

Let $\mathbf{Corr}_{\mathrm{fd}}$ be the bicategory whose:

- objects are finite-dimensional unital C*-algebras;
- 1-morphisms $A\to B$ are finite C*-correspondences, namely right Hilbert
  $B$-modules with a nondegenerate *-representation of $A$ by adjointable
  operators;
- 2-morphisms are adjointable bimodule intertwiners; and
- horizontal composition is the interior tensor product.

An invertible 1-morphism is an $A$--$B$ imprimitivity bimodule. This is the
bicategorical form of strong Morita equivalence [1,2].

### Lemma 3.2 — transport of boundary modules

Let ${}_A X_B$ be an imprimitivity bimodule. The functor

$$
F_X:\mathbf{Hilb}_A^{\mathrm{fin}}
\longrightarrow
\mathbf{Hilb}_B^{\mathrm{fin}},
\qquad
M\longmapsto M\otimes_A X,
$$

is an equivalence. For finite Hilbert modules $M,N$, the map

$$
\Theta_X^{M,N}:
\mathcal L_A(M,N)
\longrightarrow
\mathcal L_B(M\otimes_A X,N\otimes_A X),
\qquad
T\longmapsto T\otimes I_X,
$$

is a linear adjoint-preserving bijection. In particular,

$$
\Theta_X^M:
\mathcal L_A(M)
\overset{\cong}{\longrightarrow}
\mathcal L_B(M\otimes_A X)
$$

is a unital *-isomorphism.

*Proof.* Let ${}_B\overline X_A$ be the conjugate imprimitivity bimodule.
There are unitary correspondence isomorphisms

$$
X\otimes_B\overline X\cong A,
\qquad
\overline X\otimes_A X\cong B.
$$

Tensoring by $\overline X$ is therefore a quasi-inverse to $F_X$. Full
faithfulness gives the Hom-space bijection. Tensoring respects composition
and adjoint, so the endomorphism bijection is a unital *-isomorphism.
$\square$

This is the finite module theorem behind the operator-module formulation of
strong Morita equivalence [1].

### Definition 3.3 — transport of the operational marking

Through $\Theta_X$, transport:

- an effect $e$ to $\Theta_X(e)$;
- a state $\rho$ to $\rho\circ\Theta_X^{-1}$;
- a CP map $\Phi:\mathcal O_y\to\mathcal O_x$ to

$$
\Phi^X
=
\Theta_X^x\circ\Phi\circ(\Theta_X^y)^{-1};
$$

- every outcome branch separately; and
- every counterfactual comparison and scalar context by the same coherent
  conjugation.

Because a *-isomorphism and its inverse are completely positive, CP, UCP,
positivity, instrument sums and all scalar probabilities are preserved.

### Definition 3.4 — marked operational Morita equivalence

Two represented complete theories $D,D'$ are **marked operationally Morita
equivalent** when there are:

1. a bijection of boundary roles;
2. an imprimitivity bimodule $X_x:A_x\to A'_{x'}$ at every boundary;
3. the induced module equivalences $F_{X_x}$;
4. a bijection of the complete admitted preparations, effects, channels,
   outcome instruments and comparisons under Definition 3.3; and
5. coherent preservation of identities, composition, outcome sums,
   classical handles and every scalar experiment value.

The coherence diagrams are the ordinary associativity and unit diagrams for
interior tensor product together with

$$
(\Psi\circ\Phi)^X=\Psi^X\circ\Phi^X,
\qquad
(\operatorname{id})^X=\operatorname{id},
$$

for every typed operational composite.

The definition does not mention the seam set. Hence seam invariance, if
proved, is not built into the equivalence.

### Warning 3.5 — bare Morita equivalence is too coarse

$\mathbb C$ and $M_n(\mathbb C)$ are strongly Morita equivalent as unmarked
algebras. A system with a fully accessible $n$-level degree of freedom is not
therefore physically equivalent to a scalar system. The equivalence counts
only when their **marked** module semantics correspond. Different admitted
controls or effects break it.

### Definition 3.6 — the operational Morita localization

Let $\mathbf{Pres}_D$ be the bicategory of complete represented presentations
of one operational law, marked correspondences and coherent 2-cells. Let
$\mathcal W_{\mathrm{Mor}}$ be its marked operational Morita equivalences.
Define

$$
\mathbf{OpMor}(D)
=
\mathbf{Pres}_D[\mathcal W_{\mathrm{Mor}}^{-1}].
$$

At finite scope the elements of $\mathcal W_{\mathrm{Mor}}$ are already
adjoint equivalences in the correspondence bicategory; the localization
records their unit, counit and stabilizers instead of reducing them to an
orbit set. All seam objects below are defined as categorical constructions on
$\mathbf{OpMor}(D)$.

---

## 4. Classical record interfaces

### Definition 4.1 — finite classical object

For a finite outcome set $\Omega$, let

$$
C_\Omega=\mathbb C^\Omega
$$

with minimal idempotents $(\delta_r)_{r\in\Omega}$. In finite-dimensional
categorical quantum mechanics this carries the canonical commutative special
symmetric dagger-Frobenius structure

$$
\delta_r\longmapsto\delta_r\otimes\delta_r,
\qquad
\delta_r\longmapsto1,
$$

and is a classical object in the completely positive setting [3,4].

### Definition 4.2 — classical action on a boundary module

A sharp classical interface on $(A,M)$ is a unital *-homomorphism

$$
\lambda:C_\Omega\longrightarrow\mathcal L_A(M).
$$

Put

$$
p_r=\lambda(\delta_r).
$$

Then $(p_r)$ is a PVM of adjointable module projections. The invariant datum
is the classical object and its module action $\lambda$, not the coordinates
of the $p_r$ in one Hilbert-space representation.

### Proposition 4.3 — PVM/action equivalence

Unital *-homomorphisms
$\lambda:\mathbb C^\Omega\to\mathcal L_A(M)$ are in bijection with finite
PVMs $(p_r)_{r\in\Omega}$ in $\mathcal L_A(M)$.

*Proof.* A *-homomorphism carries the mutually orthogonal minimal idempotents
of $\mathbb C^\Omega$ to mutually orthogonal projections summing to the
identity. Conversely a PVM defines

$$
\lambda((c_r)_r)=\sum_r c_rp_r,
$$

which is a unital *-homomorphism. $\square$

Thus the concrete PVM is recovered without making it the primary type.

### Definition 4.4 — fine and coarse classical objects

Let $K$ be a finite fine-outcome set and let

$$
q:K\twoheadrightarrow\Omega
$$

be a surjection. It induces a unital *-homomorphism

$$
q^*:C_\Omega\longrightarrow C_K,
\qquad
(q^*f)(k)=f(q(k)).
$$

A fine/coarse action is a classical action
$\lambda_F:C_K\to\mathcal L_A(M)$ together with

$$
\lambda_R=\lambda_F\circ q^*.
$$

Writing $q_k=\lambda_F(\delta_k)$ gives

$$
p_r=\sum_{k:q(k)=r}q_k.
$$

The refinement is therefore the classical-object morphism $q^*$; no separate
support label is supplied.

### Proposition 4.5 — Morita transport of classical actions

For an imprimitivity bimodule ${}_A X_B$, define

$$
\lambda^X=\Theta_X^M\circ\lambda:
C_\Omega\longrightarrow
\mathcal L_B(M\otimes_A X).
$$

Then $\lambda^X$ is a sharp classical action with the same Frobenius object,
and fine/coarse maps transport functorially.

*Proof.* $\Theta_X^M$ is a unital *-isomorphism, so it preserves products,
adjoints, sums and identity. Hence it carries the PVM and the relation
$\lambda_R=\lambda_Fq^*$ exactly. The Frobenius equations live in the fixed
finite classical object and are unchanged. Functoriality follows from the
associativity coherence of interior tensor product. $\square$

### Scope 4.6

Proposition 4.5 does **not** say that a chosen commutative subalgebra of $A$
canonically becomes a chosen commutative subalgebra of $B$. It transports a
classical action on a module to a classical action on the equivalent module.
This is precisely why the module/action type is used.

---

## 5. Complete-instrument W3 structures

Fix boundary charts $x_0,x_1,x_2$ in a complete marked theory. Write
$\mathcal O_i=\mathcal L_{A_i}(M_i)$.

### Definition 5.1 — eligible complete experiment

An eligible complete W3 experiment is

$$
\omega=(S,U,N,\mathsf V,\mathsf E),
$$

where:

- $S=(\rho_\alpha)_{\alpha\in A}$ is one complete admitted preparation
  instrument at $x_0$;
- $U^*,N^*:\mathcal O_1\to\mathcal O_0$ are a matched write/control pair;
- $\mathsf V$ is a nonempty complete declared family of preserving-candidate
  UCP maps $V^*:\mathcal O_2\to\mathcal O_1$;
- $\mathsf E$ is a nonempty admitted eraser-candidate family of the same
  types; and
- all readout instruments and effects admitted at $x_2$ remain in the fixed
  operator system $\mathcal E_D(x_2)$.

The words “write,” “preserving” and “eraser” are roles to be tested. The
families are fixed by the comparison grammar before a classical action is
chosen.

### Definition 5.2 — write correlation

For a fine/coarse action $C_\Omega\xrightarrow{q^*}C_K\xrightarrow{\lambda_F}
\mathcal O_1$, define

$$
w_{\alpha k}=\rho_\alpha(U^*(q_k))\ge0.
$$

The write process correlates fine alternatives with coarse record sectors
when

$$
w_{\alpha k}w_{\alpha\ell}=0
$$

for every source outcome $\alpha$, every $r$, and distinct
$k,\ell\in q^{-1}(r)$.

Every branch of the complete source instrument is quantified.

### Definition 5.3 — matched no-write failure

Put

$$
n_{\alpha k}=\rho_\alpha(N^*(q_k)).
$$

The matched control fails correlation when there exist
$\alpha,r$ and distinct $k,\ell\in q^{-1}(r)$ with

$$
n_{\alpha k}n_{\alpha\ell}>0.
$$

### Definition 5.4 — universal block preservation

For the coarse action $(p_r)$, define

$$
\mathcal D_R(a)=\sum_r p_rap_r.
$$

A continuation $V^*$ is universally block preserving at the admitted scope
when

$$
\mathcal D_RV^*(a)=V^*(a)
\qquad
\forall a\in\mathcal E_D(x_2).
$$

### Definition 5.5 — sharp readable availability

A universally block-preserving $V^*$ has sharp readable availability when
there is a complete admitted output instrument with POVM
$(e_j)_{j\in J}$ and a surjection

$$
\ell:J\twoheadrightarrow\Omega
$$

such that, for every $r$,

$$
V^*\left(\sum_{j:\ell(j)=r}e_j\right)=p_r.
$$

Thus the Boolean record algebra is the exact Heisenberg pullback of a complete
coarse output question. No claim is made that each arbitrary effect in
$\mathcal E_D(x_2)$ lies in one record sector; the identity effect would make
that demand impossible.

### Definition 5.6 — coherent erasure

An eraser candidate $E^*$ exposes written cross-sector coherence when there
exist a complete-source outcome $\alpha$, an admitted output effect
$a\in\mathcal E_D(x_2)$ belonging to a complete readout instrument, and fine
atoms $k,\ell$ with $q(k)\ne q(\ell)$ such that

$$
\boxed{
\rho_\alpha\!\left(
U^*(q_kE^*(a)q_\ell)
\right)\ne0.
}
$$

The individual scalar is used; a sum of cross terms could vanish by phase
cancellation.

### Definition 5.7 — complete-instrument W3 object

A complete-instrument W3 object is a tuple

$$
s=(\omega,C_\Omega\xrightarrow{q^*}C_K,\lambda_F)
$$

satisfying:

1. write correlation;
2. matched no-write failure;
3. universal block preservation and sharp readable availability for every
   declared preserving continuation; and
4. coherent erasure for at least one declared eraser.

All actions, channels, states, effects and instruments are objects of the
complete represented operational theory.

---

## 6. Universal preservation theorem

### Theorem 6.1 — four equivalent block conditions

Let $(p_r)$ be a finite PVM in a unital C*-algebra $B$ and let
$\mathcal E\subseteq B$ be a unital self-adjoint operator system. For a
linear map $T:\mathcal E\to B$, the following are equivalent:

1. $\mathcal D_R(T(a))=T(a)$ for every $a\in\mathcal E$;
2. $p_rT(a)p_s=0$ for every $a\in\mathcal E$ and $r\ne s$;
3. $T(\mathcal E)\subseteq\operatorname{Fix}(\mathcal D_R)$;
4. $T(\mathcal E)\subseteq C_R'$, where
   $C_R=C^*(p_r:r\in\Omega)$.

*Proof.* Expanding the identity
$I=\sum_rp_r$ gives

$$
T(a)=\sum_{r,s}p_rT(a)p_s.
$$

The dephasing retains exactly the $r=s$ terms, proving (1)$\Leftrightarrow$(2)
and (1)$\Leftrightarrow$(3). If the cross blocks vanish, then
$p_rT(a)=p_rT(a)p_r=T(a)p_r$ for every $r$, so $T(a)$ commutes with $C_R$.
Conversely, if $T(a)$ commutes with every $p_r$, then for $r\ne s$,

$$
p_rT(a)p_s=T(a)p_rp_s=0.
$$

Thus (2)$\Leftrightarrow$(4). $\square$

### Corollary 6.2 — intrinsic factorization

Universal block preservation is precisely factorization of the admitted
effect map through the fixed operator system

$$
\operatorname{Fix}(\mathcal D_R)=C_R'.
$$

This is the internal block/module condition required here. It is independent
of a scalar-probe basis.

### Proposition 6.3 — sharp readability is additional structure

Universal block preservation neither implies nor is implied by the existence
of a supplied single favorable scalar effect. Definition 5.5 adds a complete
POVM and a Boolean coarse-graining whose pullback is exactly $(p_r)$.

*Proof.* A block-preserving channel can erase the distinction among sectors
by mapping every output effect to a scalar multiple of identity, so no sharp
readout need pull back to $p_r$. Conversely one favorable effect can be block
diagonal while another admitted effect has a nonzero cross block. The latter
is the hostile singleton-probe mechanism proved explicitly in Control 12.1.
$\square$

### Proposition 6.4 — full-matrix unitary negative

Let $T:B(H_2)\to B(H_1)$ be a *-isomorphism and let
$\mathcal E=B(H_2)$. If $(p_r)$ has at least two nonzero sectors, then $T$
does not satisfy universal block preservation.

*Proof.* $T(B(H_2))=B(H_1)$. For two nonzero sectors choose unit vectors
$u\in p_rH_1$, $v\in p_sH_1$ and the rank-one operator
$|u\rangle\langle v|$. It lies in $B(H_1)$ and has a nonzero $r,s$ block, so
$B(H_1)\not\subseteq C_R'$. Apply Theorem 6.1. $\square$

This is why “complete admitted” cannot be silently replaced by “all matrix
effects,” nor can a full-control law be shrunk after the candidate is known.

### Proposition 6.5 — erasure is an operational failure of block preservation

If Definition 5.6 holds, then $E^*$ fails the universal block law on the
admitted effect $a$.

*Proof.* If every cross block $p_rE^*(a)p_s$ vanished, then so would
$q_kE^*(a)q_\ell$ whenever $q(k)\ne q(\ell)$, because
$q_k\le p_{q(k)}$ and $q_\ell\le p_{q(\ell)}$. The displayed eraser scalar
would therefore be zero, a contradiction. $\square$

---

## 7. Marked Morita transport of W3 structures

### Theorem 7.1 — complete W3 transport

Let $D,D'$ be marked operationally Morita equivalent complete theories. Then
the boundary module equivalences and marking bijections induce an equivalence

$$
\mathsf{W3}_{\rm ci}(D)
\simeq
\mathsf{W3}_{\rm ci}(D')
$$

between their categories of complete-instrument W3 objects and marked
intertwiners.

*Proof.* Let $\Theta_i$ be the boundary endomorphism *-isomorphisms of
Lemma 3.2. Transport the classical actions by Proposition 4.5 and every
operational map by Definition 3.3.

For write correlation,

$$
(\rho_\alpha\circ\Theta_0^{-1})
\bigl(
\Theta_0U^*(q_k)
\bigr)
=
\rho_\alpha(U^*(q_k)).
$$

Thus every zero and positive probability is unchanged. The same identity
handles the matched control.

For preservation,

$$
\Theta_1\!\left(\sum_rp_rap_r\right)
=
\sum_r\Theta_1(p_r)\Theta_1(a)\Theta_1(p_r),
$$

so the dephasing equation is preserved on the bijectively transported complete
effect system. The complete output instrument and its coarse-graining are
transported outcome by outcome, giving the same sharp pullback equation.

For erasure, the transported scalar is exactly the original scalar because
states are pulled back by $\Theta^{-1}$ and maps/effects are conjugated by
$\Theta$. Hence nonzero cross-sector coherence is preserved.

The inverse imprimitivity bimodules give the inverse functor. Coherence under
composition follows from the interior-tensor associators and the equations in
Definition 3.4. $\square$

### Corollary 7.2 — redundant grammar invariance

Two syntactic grammars with the same complete represented operational image
give equivalent W3 categories.

*Proof.* They define the same object $\overline D$ before the Morita
localization. Apply Theorem 7.1 to the identity marked equivalence. $\square$

### Proposition 7.3 — different markings remain different

Two theories with the same boundary C*-algebras but different admitted
effect or counterfactual instrument families need not have equivalent W3
categories.

*Proof.* The identity algebra bimodule is not a marked operational Morita
equivalence unless it also gives a bijection of the complete markings.
Adding an effect with a nonzero cross-sector block can turn a preserving
candidate into an eraser. Hence bare algebra identity does not identify the
theories. $\square$

### Definition 7.4 — the Morita W3 category

Let

$$
\mathfrak{W3Mor}(D)
$$

be the Grothendieck category of the pseudofunctor assigning to an object of
$\mathbf{OpMor}(D)$ its category of complete-instrument W3 classical actions.
Theorem 7.1 supplies transport along every marked Morita equivalence.

Equivalently, it is the total category of W3 objects **after** the base has
been localized at marked Morita equivalences. No raw matrix seam list is
formed and then quotiented.

---

## 8. Spectator stability

### 8.1 The standard finite matrix amplification

Let $A=\mathbb C$ and $B=M_n(\mathbb C)$. Let

$$
X=\mathbb C^{1\times n}
$$

with its standard left scalar and right matrix actions. It is a
$\mathbb C$--$M_n$ imprimitivity bimodule. For a Hilbert space $H$ viewed as
a right $\mathbb C$-module,

$$
H^X=H\otimes_{\mathbb C}X
$$

is a right $M_n$-module and

$$
\mathcal L_{M_n}(H^X)\cong B(H).
$$

Although a concrete realization of $H^X$ has vector-space dimension
$n\dim H$, its adjointable module observables are exactly the original
$B(H)$, not all of $B(H\otimes\mathbb C^n)$.

### Theorem 8.1 — inaccessible spectator stability

Let $D^{(n)}$ be obtained from $D$ by transporting every boundary module and
the complete operational marking through the standard matrix-amplification
imprimitivity bimodule. Admit no extra spectator-resolving state, effect or
instrument. Then

$$
\boxed{
\mathfrak{W3Mor}(D)
\simeq
\mathfrak{W3Mor}(D^{(n)}).
}
$$

*Proof.* The standard bimodule is an operational Morita equivalence. The
endomorphism *-isomorphisms transport the full marking, including scalar
preparations and readout effects, by Definition 3.3. No formula of the form
$\eta\mapsto\eta\otimes I_n$ is used. Theorem 7.1 gives the equivalence of W3
categories. $\square$

### Proposition 8.2 — physical spectator discriminator

Suppose instead that the amplified presentation admits an effect or control
whose represented operator is not in the image of
$\Theta_X:\mathcal L_A(M)\to\mathcal L_B(M\otimes_A X)$. Then the standard
imprimitivity bimodule does not implement a marked operational Morita
equivalence of the two theories.

*Proof.* Definition 3.4 requires a bijection of complete markings. The new
operation has no preimage, so that requirement fails. It can distinguish
scalar contexts that the original theory cannot form. $\square$

### Ontological reading 8.3

An inaccessible spectator is not a hidden physical system that is later
ignored. It is a matrix presentation of the same operational module. A
spectator becomes physical precisely when additional preparation, effect or
control structure enters the marking.

---

## 9. Effective W3 moduli and rigidification

### Definition 9.1 — marked W3 equivalence groupoid

Let $\mathfrak S(D)$ be the maximal groupoid of
$\mathfrak{W3Mor}(D)$: objects are complete-instrument W3 structures and
arrows are invertible marked Morita intertwiners. Active physical
automorphisms are retained as arrows. Passive syntactic equality has already
been removed in $\overline D$.

### Definition 9.2 — ineffective isotropy

For $s\in\mathfrak S(D)$ let $K_s$ consist of automorphisms $g:s\to s$ whose
induced action is identity on:

- every complete marked state and effect;
- every channel and every instrument branch;
- every counterfactual comparison and scalar context;
- the fine and coarse classical actions; and
- every object and morphism of the addressability category defined below.

Equality means equality in the represented operational image, not merely
equality of marginal probabilities.

### Lemma 9.3 — the ineffective system is normal

For every arrow $f:s\to t$ in $\mathfrak S(D)$,

$$
fK_sf^{-1}=K_t.
$$

*Proof.* Let $k\in K_s$. For any marked operational datum $a$ at $t$, pull it
back along $f^{-1}$. The element $k$ acts trivially on that pullback. Pushing
forward along $f$ shows that $fkf^{-1}$ acts trivially on $a$. Thus
$fK_sf^{-1}\subseteq K_t$. Apply the same argument to $f^{-1}$ for the
reverse inclusion. $\square$

### Definition 9.4 — explicit finite rigidification

Define an equivalence relation on each hom-set by

$$
f\sim k_t f\sim f k_s
$$

for $k_s\in K_s$ and $k_t\in K_t$. Let

$$
\mathfrak S_{\rm eff}(D)=\mathfrak S(D)/\!/K
$$

have the same objects and these equivalence classes as arrows.

### Theorem 9.5 — finite rigidification is a groupoid

Composition

$$
[g]\circ[f]=[gf]
$$

is well defined. The quotient is a groupoid, and an automorphism survives
nontrivially exactly when it has a nontrivial action on some complete marked
operational datum.

*Proof.* Suppose $f'=k_tf k_s$ and $g'=k_ugk_t'$ are equivalent
representatives. Then

$$
g'f'
=
k_u g(k_t'k_t)f k_s.
$$

By Lemma 9.3,
$g(k_t'k_t)g^{-1}\in K_u$, so $g'f'$ differs from $gf$ by ineffective
elements at source and target. Identities and inverses descend similarly.
The final statement is Definition 9.2. $\square$

This is a direct finite-groupoid construction. It does not invoke the general
algebraic-stack rigidification theorem, although the mechanism is analogous
to removing a normal subgroup of inertia [7,8].

### Corollary 9.6 — spectator phases are removed, physical swaps remain

Inner matrix-spectator transformations naturally isomorphic to identity on
the induced marking lie in $K_s$. A swap that permutes two record actions or
changes any admitted effect or control does not lie in $K_s$ and remains.

---

## 10. Full category-valued addressability

### Definition 10.1 — seam observability operator system

For a seam $s$ with coarse effects $(p_r)$ at $x$, define at every marked
boundary $y$

$$
\mathcal S_s(y)
=
\operatorname{span}_{\mathbb C}
\{I,\Phi^*(p_r),\Phi^*(p_r)^*:
\Phi^*\text{ is an admitted typed transport}\}.
$$

This is constructed only after $s$ exists. It is the inherited
record-observability operator system of the terminal transport paper.

### Definition 10.2 — full addressability category

For a seam $s$, define $\mathsf{Addr}(s)$ as follows.

An object is a pair $(y,e)$ where

$$
e:\mathcal O_y\to\mathcal O_y
$$

is an admitted UCP idempotent with

$$
\mathcal S_s(y)\subseteq\operatorname{Fix}(e).
$$

A morphism

$$
h:(y,e)\longrightarrow(z,f)
$$

is an admitted CP map $h:\mathcal O_y\to\mathcal O_z$ satisfying

$$
h=fhe
$$

and carrying the typed seam observability maps at $y$ to those at $z$.
Identity on $(y,e)$ is $e$, and composition is CP-map composition.

No minimality or invertibility requirement is imposed.

### Proposition 10.3 — category typing

$\mathsf{Addr}(s)$ is a category.

*Proof.* For an object $(y,e)$, idempotence gives $e=e e e$, so $e$ is a
Karoubi identity. If $h=fhe$ and $k=gkf$, then

$$
kh=gkfh e=g(kh)e.
$$

The composite is admitted by closure of the process grammar and is CP.
Record-interface compatibility composes. $\square$

### Theorem 10.4 — Morita transport of full fibers

Every marked Morita seam equivalence $u:s\to t$ induces an equivalence of
categories

$$
u_*:\mathsf{Addr}(s)\simeq\mathsf{Addr}(t)
$$

by conjugating $e$ and $h$ through the boundary endomorphism
*-isomorphisms. These assignments form a pseudofunctor

$$
\mathsf{Addr}:
\mathfrak S_{\rm eff}(D)^{\rm op}\longrightarrow\mathbf{Cat},
$$

where $u^*=(u^{-1})_*$. Equivalently, the covariant transports $u_*$ form
an opindexed pseudofunctor. Because the base is a groupoid, the two
descriptions determine one another.

*Proof.* Conjugation by *-isomorphisms preserves CP, unitality,
idempotence, fixed operator systems, the corner equation and composition.
The inverse marked Morita equivalence gives a quasi-inverse. Interior-tensor
associators supply the pseudofunctor coherence. Put $u^*=(u^{-1})_*$ to obtain
the displayed contravariant assignment. Ineffective automorphisms act as
identity on addressability data by Definition 9.2, so the assignment descends
to the rigidified groupoid. $\square$

### Theorem 10.5 — full addressability fibration

The Grothendieck construction

$$
\boxed{
\pi:\int_{\mathfrak S_{\rm eff}(D)}\mathsf{Addr}
\longrightarrow
\mathfrak S_{\rm eff}(D)
}
$$

is a category-valued fibration. Using the covariant form $u_*$ it is also an
opfibration. Its maximal subgroupoid is the earlier invertible-core
bifibration, but the total category also contains every admitted
noninvertible Karoubi arrow.

*Proof.* For the contravariant pseudofunctor, an object of the Grothendieck
construction is $(s,a)$ and an arrow over $u:s\to t$ is a fiber arrow
$a\to u^*b$. The arrow represented by
$\operatorname{id}_{u^*b}$ is cartesian, and the usual factorization proves
the lifting property. The covariant presentation supplies cocartesian lifts.
No invertibility of fiber arrows is used. $\square$

### Scope 10.6

The word addressability retains its adjudicated weak meaning: an admitted
repeatable coarse-graining and its process maps. The construction does not
give independently selectable preparations, arbitrary internal control,
nondemolition readout, a disposable complement or a spatial boundary.

---

## 11. The two-dephasing fiber

Let $B=M_2\otimes M_2$, and let the record observability system be

$$
\mathcal S=\operatorname{span}\{I,Z\otimes I\}.
$$

On the auxiliary factor let $D_n,D_m$ be dephasing channels about distinct
nonorthogonal Bloch axes, and put

$$
e_n=\operatorname{id}\otimes D_n,
\qquad
e_m=\operatorname{id}\otimes D_m.
$$

Both are admitted UCP idempotents fixing $\mathcal S$. Define

$$
h=e_me_n.
$$

### Proposition 11.1 — the omitted noninvertible arrow exists

$h$ is an admitted Karoubi arrow

$$
h:(B,e_n)\longrightarrow(B,e_m).
$$

For nonparallel, nonorthogonal axes it is not invertible.

*Proof.* Closure under composition makes $h$ admitted and CP. Moreover,

$$
e_mhe_n=e_m(e_me_n)e_n=e_me_n=h.
$$

On the auxiliary Bloch space, $D_n$ and $D_m$ act as the rank-one real
projections $nn^{\mathsf T}$ and $mm^{\mathsf T}$. Their product has singular
value $|m\cdot n|$ strictly between zero and one, so it is neither an
isomorphism nor an idempotent equivalence. $\square$

The reverse composite $e_ne_m$ is another noninvertible arrow. If an admitted
unitary swaps the axes, it gives an invertible arrow between the two objects;
the full fiber contains both the swap and the irreversible composites.

---

## 12. Exact hostile and discriminator controls

### Control 12.1 — singleton-probe false preservation

First rebuild the hostile four-level example. Let the cut and output carrier
be $\mathbb C^4$, with fine atoms $Q_0,\ldots,Q_3$ and coarse sectors

$$
P_A=Q_0+Q_1,
\qquad
P_B=Q_2+Q_3.
$$

Use the complete two-outcome source instrument with

$$
U\eta_0=\frac{|0\rangle+|2\rangle}{\sqrt2},
\qquad
U\eta_1=\frac{|1\rangle+|3\rangle}{\sqrt2},
$$

and matched control

$$
N\eta_0=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
N\eta_1=\frac{|2\rangle+|3\rangle}{\sqrt2}.
$$

Correlation and matched-control failure hold. Let $V$ fix $|0\rangle$ and
rotate the span of $|1\rangle,|2\rangle$ through a nonzero angle strictly
between $0$ and $\pi/2$. The selected effect

$$
e_0=|0\rangle\langle0|
$$

has $V^*(e_0)=P_AV^*(e_0)P_A$ and would pass the old singleton test. But the
also-admitted effect $e_1=|1\rangle\langle1|$ obeys

$$
P_AV^*(e_1)P_B\ne0.
$$

The complete output effect system therefore rejects $V$ at Definition 5.4.
Adding the normalized four-dimensional Walsh eraser still gives the old
nonzero cross-sector witness, but it cannot rescue the failed preserving
gate. This is the exact hostile mechanism, now failed by construction.

A two-level compression makes the same point. Let $\mathcal O=M_2$ and take
the candidate record

$$
p_0=|0\rangle\langle0|,
\qquad
p_1=|1\rangle\langle1|.
$$

Let the continuation be identity. Suppose the marked output law admits the
complete $Z$-readout and complete $X$-readout, so

$$
\mathcal E
=
\operatorname{span}\{I,p_0,p_1,p_+,p_-\},
\qquad
p_+=|+\rangle\langle+|.
$$

The favorable singleton $p_0$ is block diagonal. A packet using only that
effect would pass. But

$$
p_0p_+p_1=\frac12|0\rangle\langle1|\ne0.
$$

The complete effect system therefore fails Theorem 6.1. The false seam is
rejected without selecting a new probe.

If the physical law admits only the complete $Z$-readout, the block statement
is genuinely true at that restricted operational scope. The result is
law-relative, not a claim about inaccessible mathematical measurements.

### Control 12.2 — inaccessible spectator

Use Theorem 8.1 with $A=\mathbb C$, $B=M_n$ and the standard row
imprimitivity module. Every endomorphism, state, effect, channel and
instrument has a unique transported representative. The W3 category and all
addressability fibers are equivalent.

The raw amplified presentation admits inner $U(n)$ changes of spectator
coordinates. They act trivially on the induced marked endomorphism algebra
and enter the ineffective kernel of Definition 9.2.

### Control 12.3 — physical spectator

Replace the transported right $M_n$-module boundary by the ordinary Hilbert
space $H\otimes\mathbb C^n$ over $\mathbb C$, and admit an effect
$I_H\otimes|0\rangle\langle0|$. Its observable algebra is
$B(H)\otimes M_n$, and the new effect is absent from the image of the
transported $B(H)$ marking. Proposition 8.2 blocks the equivalence.

### Control 12.4 — equivalent grammar

Add a generator $c$ with the exact relation $c=ba$ to a represented process
grammar. The represented image $\overline D$ is unchanged, so Corollary 7.2
returns the same W3 category. Add instead a new continuation with no relation
and a cross-record effect. The complete marking changes and Proposition 7.3
allows the seam category to change.

### Control 12.5 — same algebra, different marked law

Let both theories use $M_2$. In $D_Z$, admit only the complete $Z$ readout at
the continuation output. In $D_{ZX}$, also admit the complete $X$ readout.
The identity continuation is block preserving for the $Z$ record in $D_Z$
and fails in $D_{ZX}$ by Control 12.1. Algebra identity and bare Morita
equivalence do not erase the physical counterfactual difference.

### Control 12.6 — quaternion support smuggling

Let $D_{Q8}$ be the represented quaternion process grammar with no internal
complete W3 write/preserve/erase/control experiment. Adjoin, in a separate
factor, a two-level branch-memory witness. The product law contains a W3
object in the witness marking, but the projection to the quaternion marking
does not contain its source instrument, classical action or eraser scalar.

If the two-level factor is declared inaccessible, marked Morita reduction
removes its matrix presentation and creates no quaternion seam. If it is
declared accessible, it is a physical spectator and the seam belongs to the
enlarged marked law. In neither case does a supplied `access_operations`
handle create an internal seam of $D_{Q8}$.

### Control 12.7 — full matrix effect system

Apply Proposition 6.4 to any nontrivial PVM and unitary continuation. The
candidate fails. This control prevents the branch-memory calculation below
from disguising its declared classical output-readout scope as full quantum
tomography.

### Control 12.8 — same abstract classical object, different action

Two actions

$$
\lambda,\lambda':\mathbb C^2\to M_2
$$

related by a marked Morita intertwiner represent the same classical interface
in different coordinates. If the conjugating unitary is not an admitted
marked symmetry and changes an accessible control scalar, the abstract
algebra $\mathbb C^2$ remains isomorphic but the marked actions are not
identified. Classical-algebra isomorphism alone is therefore not the seam
criterion.

---

## 13. Complete branch-memory classification

### 13.1 Frozen complete operational law

Let

$$
H=\mathbb C_b^2\otimes\mathbb C_m^2,
\qquad
H_2=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

The complete source instrument has four outcomes and prepares all four
computational states. The complete output readout is the four-outcome
computational PVM; its effect operator system is the diagonal algebra
$\mathcal D_4$. This is a declared classical readout law, not full matrix
effect access. The readout is terminal: its outcome branches target a
classical result object, and the law does not admit the corresponding
nondemolition pinching as an endomorphism of the cut boundary.

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

The law admits every atomic fine classical action at the cut. This
full-projective-access assumption is specific to the benchmark.

Define

$$
v_0=|+,0\rangle,
\quad v_1=|-,0\rangle,
\quad v_2=|+,1\rangle,
\quad v_3=|-,1\rangle.
$$

In the input order $(|00\rangle,|10\rangle,|01\rangle,|11\rangle)$,

$$
A_{ij}=2\langle v_i|U|j\rangle
$$

gives

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

### Lemma 13.1 — universal preservation discretizes the coarse action

A coarse record action is universally block preserving under $V$ precisely
when each $p_r$ is the span projector of a block in a set partition of
$\{v_0,v_1,v_2,v_3\}$.

*Proof.* Since the output effect system is $\mathcal D_4$,

$$
V^*(\mathcal D_4)
=
\operatorname{span}\{|v_i\rangle\langle v_i|:0\le i<4\}.
$$

By Theorem 6.1, every one of these four minimal effects must commute with the
coarse action. Therefore each $v_i$ lies wholly in one coarse sector, and the
sectors are spans of blocks of a set partition. Conversely all such block
projectors commute with the displayed diagonal algebra. $\square$

This is the universal operator-system version of the earlier four-probe
argument.

### Lemma 13.2 — sharp readable availability

Every partition from Lemma 13.1 has a sharp complete readout under $V$.

*Proof.* For a block $B$, let

$$
e_B=\sum_{i\in B}|i\rangle\langle i|
$$

be the corresponding coarse-graining of the complete output PVM. Then

$$
V^*(e_B)
=
\sum_{i\in B}|v_i\rangle\langle v_i|
=p_B.
$$

The family $(e_B)$ is a complete PVM. $\square$

### Lemma 13.3 — fine correlation, control and erasure

For one- and two-element coarse blocks, the fine action is uniquely forced by
the restricted Hadamard rays. Three-element blocks fail write correlation.
Every partition with blocks of size at most two and at least one two-element
block passes the matched-control and eraser tests.

*Proof.* For a block $B$, the projections of the four write states are the
restricted columns $A_{B,j}$. For $|B|=1$ there is one ray. For $|B|=2$ the
restricted sign columns lie on the two orthogonal rays $(1,1)$ and $(1,-1)$,
both used. For $|B|=3$, any two different restricted columns have inner
product $\pm1$, so four distinct rays cannot fit into a three-vector
orthogonal basis.

The no-write states are the $v_i$ up to signs and order. Inside a two-element
block, a $v_i$ overlaps both sum/difference fine rays, giving two positive
fine probabilities in one coarse sector. For erasure $E=U^*$; for a write
state and the fine ray selected in block $B$, the corresponding diagonal
output effect gives amplitude weight $|B|/4$. Distinct blocks therefore give
a nonzero cross-sector scalar $|B||C|/16$. $\square$

### Theorem 13.4 — nine complete-instrument W3 objects

At atomic fine rank, the complete branch-memory law has exactly

$$
\boxed{
6\text{ seams of type }2+1+1
\quad\sqcup\quad
3\text{ seams of type }2+2.
}
$$

*Proof.* The fifteen partitions of four elements have types
$4$, $3+1$, $2+2$, $2+1+1$ and $1+1+1+1$. The one-block case has no
nontrivial record. Every $3+1$ case fails Lemma 13.3. The all-singleton case
has no within-sector pair on which the matched no-write control can fail.
The three $2+2$ and six $2+1+1$ cases pass Lemmas 13.1--13.3. $\square$

Thus complete-instrument semantics neither destroys the exact prior theorem
nor selects the familiar memory PVM.

### 13.2 Marked Morita and effective symmetry classification

Declare active symmetries of this benchmark to be all unitary boundary
transformations preserving the complete source PVM, complete output PVM and
the four named process roles $U,N,V,E$. The input and output transformations
are therefore monomial. The intertwining equations determine the cut
transformation.

### Lemma 13.5 — active symmetry group

At the declared complete monomial scope, every permutation of the four
availability rays has one symmetry lift up to a common phase. Hence

$$
G_{\rm raw}\cong U(1)\times S_4.
$$

The $U(1)$ factor acts trivially on every state, effect, CP map and classical
action, so it is ineffective. The effective group is $S_4$.

*Proof.* The Hadamard matrix $A$ has exactly one minus sign in every row and
column. More explicitly, for a permutation matrix $P$ on the output basis set

$$
T_2=P,
\qquad
T_1=V^*PV,
\qquad
T_0=U^*T_1U.
$$

Direct substitution in the displayed $4\times4$ matrices shows that $T_0$ is
a signed monomial matrix and

$$
T_1U=UT_0,
\qquad
T_1N=NT_0,
\qquad
T_2V=VT_1,
\qquad
T_2E=ET_1.
$$

The assignment $P\mapsto(T_0,T_1,T_2)$ respects multiplication because each
$T_i$ is obtained by conjugation. Hence it gives an $S_4$ subgroup. Conversely
preservation of the complete source and output PVMs makes $T_0,T_2$
monomial. The first two intertwining equations, read entrywise in the
Hadamard matrix, force their relative phases; one common phase remains. The
last two equations determine $T_1$ and impose no additional permutation.
Thus every symmetry is a common phase times the displayed $S_4$ lift. A
common phase cancels from every operational conjugation and belongs to
$K_s$. $\square$

### Theorem 13.6 — two effective symmetry components

The effective W3 action groupoid has nine objects and two connected
components:

$$
\boxed{
S_4\ltimes\mathsf{Seam}_{\rm BM}
\simeq
\bigl(6\text{-object }2+1+1\text{ component}\bigr)
\sqcup
\bigl(3\text{-object }2+2\text{ component}\bigr).
}
$$

The components are not Morita equivalent as marked classical interfaces.

*Proof.* $S_4$ acts transitively on partitions of each fixed block-size type.
It cannot connect the two types because the coarse classical objects are
$\mathbb C^3$ and $\mathbb C^2$. Strong Morita equivalence of finite
commutative unital C*-algebras preserves the number of points of their spectra,
so these classical interfaces are inequivalent. Rigidification removes the
common phase but retains the $S_4$ arrows because they permute fine and coarse
alternatives nontrivially. $\square$

The action groupoid, not its two-element orbit set, is the physical output.

### 13.3 Addressability classification

For this benchmark's W3 classification, freeze the admitted idempotent
grammar to identity only. This avoids planting a preferred memory pinching.
Then every one of the nine seams has an identity-only addressability category.
The full fibration is still nonempty and typed, but no seam gains a proper
repeatable coarse-graining from this benchmark law.

The independent two-dephasing control of Section 11 tests nontrivial full
fibers. Adding one memory-specific dephasing to the branch benchmark would be
a new marked law and could distinguish one seam, but that distinction would
come from the admitted control, not from W3 alone.

### Corollary 13.7 — no selected memory seam

After complete-instrument testing, marked Morita localization, effective
rigidification and full addressability classification, the benchmark retains
two nontrivial physical symmetry components and no invariantly selected
object. The familiar memory partition remains one of the three $2+2$ seams.

---

## 14. Theorem and construction register

### 14.1 New definitions

1. finite operational boundary chart $(A,M)$;
2. complete candidate-independent operational marking;
3. represented operational image;
4. marked operational Morita equivalence;
5. operational Morita localization;
6. classical Frobenius object with module action;
7. complete-instrument W3 experiment and object;
8. universal block preservation;
9. sharp readable availability;
10. marked Morita W3 category;
11. ineffective isotropy and finite rigidification; and
12. full category-valued addressability.

### 14.2 Proved results

1. operational equality is a constructor congruence;
2. imprimitivity transport gives endomorphism *-isomorphisms;
3. PVMs are equivalent to finite classical actions;
4. classical actions and refinement maps transport under Morita equivalence;
5. four equivalent universal block conditions;
6. sharp readability is additional to block preservation;
7. full-matrix unitary no-record theorem;
8. coherent erasure implies block-law failure;
9. complete W3 objects transport under marked Morita equivalence;
10. redundant grammar invariance and marked-law sensitivity;
11. inaccessible matrix-spectator stability;
12. physical spectator discrimination;
13. normality of ineffective isotropy and finite quotient-groupoid theorem;
14. full addressability category and its Morita transport;
15. category-valued Grothendieck fibration;
16. explicit noninvertible two-dephasing arrow;
17. exact nine-object complete branch-memory classification;
18. $U(1)\times S_4$ raw and $S_4$ effective benchmark symmetry at the
    declared monomial scope; and
19. two retained branch-memory symmetry components.

### 14.3 Inherited results used

1. W3 write/preserve/erase/no-write interpretation from Paper 1;
2. effect/POVM transport and sharpness defect;
3. multiplicative-domain characterization of sharp proposition transport;
4. law-relative record observability operator systems;
5. admitted UCP-idempotent Karoubi typing; and
6. W6's separation of record proposition, fact co-reference and event token.

---

## 15. Four-gate audit

| object | referent | necessity | no-smuggling rule | discriminator |
|---|---|---|---|---|
| complete marking | every operation the declared law actually admits | incomplete packets manufactured seams | fixed before candidate; all outcomes retained | singleton versus complete effect control |
| boundary module $(A,M)$ | operational observables $\mathcal L_A(M)$ | raw carrier size changed under spectators | no planted tensor-factor label | inaccessible versus physical spectator |
| marked Morita equivalence | equivalence of full operational module semantics | bare Morita can erase accessible physics | all states/effects/instruments/counterfactuals coherent | same algebra/different marking |
| classical action | internal finite record question | raw embedded PVM is representation-dependent | transported action, not coordinate projector list | same object/different action |
| universal block law | absence of accessible cross-sector coherence | singleton probes hide leakage | quantifies whole admitted effect system | $Z$ singleton versus admitted $X$ effect |
| sharp readout | complete outcome instrument recovering record PVM | block law alone can be unreadable | full POVM and Boolean coarse map | depolarizing block map versus sharp pullback |
| Morita W3 category | W3 objects of localized operational law | quotient-after-seams failed | equivalence does not mention seam list | grammar and spectator controls |
| ineffective kernel | transformations invisible to all marked semantics | spectator stabilizers enlarged raw groupoid | kernel defined by action, not desirability | global phase versus record swap |
| full addressability fiber | admitted repeatable coarse-grainings and process maps | core deleted irreversible arrows | every admitted corner map retained | $e_me_n$ control |

All referents are operational or categorical. None is called a spatial
support.

---

## 16. Outcome audit

### 16.1 `RQ0-L0-COMPLETE-INSTRUMENT-W3`

Provisionally earned. The complete state/effect/instrument marking is fixed
candidate-independently. Preservation is universal over its output operator
system; sharp readable availability is separately typed. The exact hostile
singleton case fails while the complete branch-memory instrument passes.

### 16.2 `RQ0-L0-MORITA-INVARIANT-W3-SEAMS`

Provisionally earned. Classical interfaces are module actions of finite
classical Frobenius objects. The operational quotient and marked Morita
localization precede seam construction. Imprimitivity transport preserves all
W3 scalars and diagrams. Matrix amplification with induced marking is stable;
a physical spectator is not erased.

### 16.3 `RQ0-L0-EFFECTIVE-W3-SEAM-STACK`

Provisionally earned at the finite groupoid scope. Ineffective isotropy is a
conjugation-stable normal system and the quotient groupoid is explicitly
constructed. The branch benchmark removes a global phase while retaining the
effective $S_4$ action and its two physical components.

### 16.4 `RQ0-L0-FULL-ADDRESSABILITY-FIBRATION`

Provisionally earned. The fiber is a category of all containing admitted UCP
idempotents and all admitted CP corner maps. Morita transport is
category-valued, its Grothendieck construction is a fibration, and the
noninvertible $e_me_n$ arrow is retained.

### 16.5 Strongest provisional statement

$$
\boxed{
\texttt{RQ0-L0-FULL-ADDRESSABILITY-FIBRATION}
\quad
\text{at finite complete-marked operational Morita scope.}
}
$$

This result awaits hostile review. A later review can retain an earlier rung
while blocking a cumulative later one.

---

## 17. Ontology

### 17.1 What the object says exists

The primitive physical description at this rung is a complete marked quantum
process law. Its carrier presentation can change by a marked Morita
equivalence without changing the operational object. A stable record question
is an internal finite classical interface of that quantum law. The interface
can remain exact under some continuations and become coherently erasable under
others.

An inaccessible matrix multiplicity is not an additional piece of reality.
It is a different module presentation. A degree of freedom becomes physical
when the marking contains operations that address it.

### 17.2 What remains ambiguous

One operational law may contain several W3 classical interfaces. The branch
benchmark retains nine objects in two effective symmetry components. The
theory therefore reconstructs a **groupoid of admissible record questions**,
not one preferred record basis.

No law-only rule may select one object from a nontrivial effective symmetry
orbit without an additional invariant discriminator.

### 17.3 What is not actualized

A sharp classical object supplies propositions. It does not supply a truth
valuation choosing one atom in one run. Nothing here proves that one outcome
actually occurs, identifies facts across independent regions, or identifies
event tokens.

### 17.4 Why this is not locality

Morita equivalence says when two operational presentations carry the same
module semantics. Addressability says when an admitted repeatable
coarse-graining contains the record observability system. Neither says that
the object occupies a place, has a boundary, can be independently controlled,
or overlaps another object physically.

The result is infrastructure for a later chart theory, not a chart theory.

---

## 18. Explicit exclusions and first unresolved obstruction

This paper does not construct:

- selected actual outcomes;
- W6 fact co-reference or token descent;
- autonomous quantum subtheories;
- generic categorical pullbacks of independent physical regions;
- spatial localization or a cover;
- topology or a manifold shadow;
- operational influence or causal order;
- dimension, volume or Lorentzian geometry;
- scalar, Dirac or gauge fields; or
- gravity and backreaction.

The first unresolved obstruction is now sharper:

> When does a marked-Morita-invariant W3 interface with an admitted
> coarse-graining become an autonomous quantum chart with independently
> selectable preparations, separating readouts, nontrivial internal controls
> and physical pullbacks against other charts?

That question is not authorized in this cycle.

Condensed mathematics may later organize continuous families and analytic
completions of these operational Morita objects. KK-theoretic localization
may later provide a comparison. Neither is used to prove the finite results
above, because either could erase exact record dynamics if applied too early.

---

## 19. Conclusion

The seam-stack failure did not require a larger projector search. It required
a different physical object.

Complete admitted instruments eliminate candidate-selected probe packets.
Hilbert modules and marked imprimitivity equivalences make the operational
quotient prior to the seam. Finite classical Frobenius objects replace a
preferred PVM coordinate while retaining exact sharp logic. Matrix
amplification becomes spectator-stable without an ill-typed tensor rule.
Explicit rigidification removes only operationally ineffective isotropy.
The complete Karoubi/CP fiber retains irreversible maps.

At the exact finite scope, these layers form a coherent cumulative object:

$$
\boxed{
\text{complete quantum law}
\longmapsto
\text{marked-Morita W3 interfaces}
\longmapsto
\text{effective symmetry groupoid}
\longmapsto
\text{full addressability fibration}.
}
$$

The branch-memory law still refuses to choose one privileged record question.
That is now a result about the complete operational Morita object rather than
an artifact of one scalar-probe packet. It is quantum-record structure, not
space. Three independent hostile reviews must now determine which rung, if
any, survives.

---

## References

1. D. P. Blecher, “On Morita's Fundamental Theorem for C*-algebras,”
   arXiv:math/9906082. Strong Morita equivalence and equivalence of operator
   module categories.
2. R. Brouwer, “A bicategorical approach to Morita equivalence for rings and
   von Neumann algebras,” arXiv:math/0301353. Correspondence bicategories and
   Morita equivalence.
3. B. Coecke, C. Heunen, and A. Kissinger, “Categories of Quantum and
   Classical Channels,” arXiv:1305.3821. The CP* construction and typed
   classical/quantum channels.
4. S. Gogioso, “Finite-dimensional Quantum Observables are the Special
   Symmetric Dagger-Frobenius Algebras of CP Maps,” arXiv:2110.07074.
5. K. Kodaka, “Strong Morita equivalence for completely positive linear maps
   on C*-algebras,” arXiv:2102.13317. CP-map Morita equivalence and matrix
   amplification examples.
6. M.-D. Choi and E. G. Effros, “Injectivity and operator spaces,” Journal of
   Functional Analysis 24 (1977), 156--209. Ranges of CP projections and the
   Choi--Effros product.
7. D. Abramovich, A. Corti, and A. Vistoli, “Twisted bundles and admissible
   covers,” arXiv:math/0106211. Rigidification by a subgroup of inertia.
8. A. Henriques and D. Metzler, “Presentations of noneffective orbifolds,”
   arXiv:math/0302182. Ineffective isotropy and effective presentations.
9. `v12/paper1-composition-defect.md`. Exact finite W3 record
   criteria, boundary gauge and preserve/erase mechanism.
10. `v12/paper2-record-coreference.md`. Fact versus token
    co-reference and effective descent discipline.
11. `v13/paper-rq0-sharp-facts-unsharp-evidence.md`. Effect transport,
    record defects, sharp proposition transport and admitted-idempotent
    operator-system addressability.
12. `v13/paper-rq0-w3-seam-stack.md` and its two hostile reviews. Fixed
    nine-seam theorem and the failures corrected here.
