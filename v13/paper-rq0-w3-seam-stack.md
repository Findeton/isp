# The W3 Seam Stack

## Intrinsic Record Interfaces and Law-Relative Addressability

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-01

**Governing pin:** `21d28d1c80a3a9518887c9b257475694fc5843e8`

**Scope:** exact finite-dimensional boundary Hilbert spaces; generally
infinite represented process laws; law-relative reconstruction; no outcome
actualization, physical overlap, spatial localization, topology, causality,
field theory, or gravity

---

## Abstract

A stable quantum record is usually analyzed after a boundary and a record
projector-valued measure have already been selected. That order hides the
question of whether the process law itself distinguishes the record seam. We
reverse it. At every eligible finite-dimensional boundary we vary a nested
pair of commutative algebras

$$
R\subseteq F\subseteq B(H),
$$

whose minimal projections are the coarse record sectors and fine
alternatives, and impose exact write-correlation, matched no-write failure,
preserving-availability, and coherent-erasure equations using only admitted
process arrows, preparations, and probes. For each fixed rank type and finite
experiment packet, the solution is a real semialgebraic locus.
Its passive unitary presentation action defines an explicit action groupoid;
stabilizers and active physical-symmetry orbits are retained.

We prove that strong equivalences of represented operational theories induce
equivalences of these seam groupoids. The result covers basis and handle
changes, redundant grammars with the same represented completion, Kraus
changes at the channel/instrument layer, minimal instrument-preserving
dilations, formal inaccessible spectators, and explicitly equivalent
idempotent-split boundary presentations. The qualifications are load-bearing:
equal POVMs with different instruments and different counterfactual
completions need not have the same seam family.

The four-dimensional branch-memory process can be solved completely without
inserting the memory PVM. At atomic fine rank, its fixed experiment packet has
exactly nine unlabelled seams: six record partitions of type $2+1+1$ and
three of type $2+2$. The familiar memory record is only one of them. Every
partition containing a block of size three fails write correlation, while the
fully fine partition fails the no-write discriminator. This is a positive
reconstruction result and a negative uniqueness result.

For every reconstructed seam we then reuse the total effect transport,
zero-defect sharp-proposition transport, and minimal operator-system
construction. Minimal physically admitted UCP idempotents containing that
operator system assemble into a Grothendieck fibration over the seam
groupoid. Its meaning remains repeatable coarse-graining, not autonomous
subsystem control. The strongest provisional outcome is
`RQ0-L0-ADDRESSABILITY-FIBRATION` at this law-relative scope.

---

## 1. Question and claim boundary

The question is:

$$
\boxed{
\text{Which W3 record seams exist when neither the cut nor the record PVM is
supplied as the answer?}
}
$$

Three distinctions govern the answer.

First, the complete counterfactual process law is physical input. A realized
state vector or one history does not determine which write, preserve, erase,
and no-write experiments are possible.

Second, a projector that exists abstractly in $B(H)$ is not automatically an
admitted operational alternative. The process theory must contain the
projector as a typed idempotent/effect arrow, or contain an operationally
equivalent representative.

Third, a reconstructed sharp record proposition is not a selected true
outcome. The construction below produces candidate Boolean record questions.
It does not supply an ultrafilter, occurrence flag, W6 co-reference
certificate, or event-token identity.

The word *stack* has one narrow meaning here: an action groupoid retaining the
stabilizers of a moduli problem. No site, overlap descent, or spatial atlas is
constructed.

### 1.1 Provisional result ladder

The paper tests three cumulative outcomes:

$$
\begin{aligned}
&\texttt{RQ0-L0-W3-SEAM-MODULI},\\
&\texttt{RQ0-L0-PRESENTATION-INVARIANT-W3-SEAMS},\\
&\texttt{RQ0-L0-ADDRESSABILITY-FIBRATION}.
\end{aligned}
$$

All claims are finite-dimensional and law-relative. The final audit states
which conditions are actually met.

---

## 2. Represented operational theories

The instrument language follows the operational separation between outcome
probabilities and outcome-conditioned state changes [1,2]. Completely
positive maps, their operator-sum presentations, and their dilations are used
in the standard finite-dimensional sense [3--5].

### Definition 2.1 — amplitude-and-instrument theory

A represented operational theory $D$ consists of:

1. a class $X_D$ of typed boundaries;
2. a finite-dimensional complex Hilbert space $H_x$ for each $x\in X_D$;
3. a typed dagger-linear amplitude category $\mathsf{Amp}_D$ represented by
   linear maps between the $H_x$;
4. admitted preparations $\eta:\mathbb C\to H_x$ and probes
   $f:H_x\to\mathbb C$;
5. admitted outcome-indexed CP instruments and UCP Heisenberg channels where
   those are part of the experiment;
6. a set of matched-control declarations $\mathsf{Cmp}_D$ between process
   arrows with common types;
7. exact relations and composition; and
8. a passive presentation groupoid $G_{\mathrm{pres}}(D)$.

The presentation may have finitely many generators. Its represented arrow
category is generally infinite. In particular, a nonzero scalar such as
$1/2$ can have distinct positive powers without contradiction.

An arrow or effect is **admitted** only if it lies in the represented closure
of the declared operational grammar. Mathematical existence in the ambient
matrix algebra is insufficient.

### Definition 2.2 — eligible W3 packet

An eligible packet at a candidate boundary $x_1$ is a typed tuple

$$
\omega=(x_0,x_1,x_2;\mathsf P,U,N,\mathsf V,\mathsf E,\mathsf F),
$$

where:

- $\mathsf P$ is a nonempty admitted preparation family at $x_0$;
- $U,N:H_{x_0}\to H_{x_1}$ are a matched write/control pair in
  $\mathsf{Cmp}_D$;
- $\mathsf V$ is a nonempty family of admitted candidate preserving
  continuations $H_{x_1}\to H_{x_2}$;
- $\mathsf E$ is a nonempty family of admitted candidate erasing
  continuations of the same type; and
- $\mathsf F$ is a nonempty admitted probe family at $x_2$.

The words *write*, *preserving*, and *erasing* name roles to be tested. They
are not constructor truth values. The packet is eligible before any record
algebra is chosen. Its matched-control relation may refer to a controllable
laboratory setting but may not mention the candidate record sectors.

Let $\mathsf{Pkt}(D)$ be the complete admitted family of such packets.
The family $\mathsf{Pkt}(D)$ is part of the represented operational theory and
is fixed before any pair $(R,F)$ is tested. One may not manufacture a
candidate preserve/erase subfamily after inspecting a proposed record
decomposition. In a finitely generated worked control, *complete* means that
every finite typed choice allowed by the frozen comparison grammar is
included; the names of the two continuation roles carry no record-sector or
support label.

### Definition 2.3 — admitted projective resolution

An admitted projective resolution at $x$ is a finite family

$$
\mathbf Q=(Q_k)_{k\in K}
$$

of actual typed dagger-idempotent effects in the represented law satisfying

$$
Q_k^*=Q_k,
\qquad
Q_kQ_\ell=\delta_{k\ell}Q_k,
\qquad
\sum_{k\in K}Q_k=I_{H_x}.
$$

Outcome handles $k$ have no mathematical identity beyond indexing. A handle
bijection is presentation change.

This definition is deliberately stricter than “choose any projector in
$B(H_x)$.” In a full-matrix laboratory law all projectors may be admitted; in
a restricted law only a smaller family may be operational.

### Definition 2.4 — strong represented equivalence

A strong represented equivalence $T:D\simeq D'$ consists of:

- a bijection of boundary types;
- unitaries $T_x:H_x\to H_{T x}$;
- bijections of admitted amplitude arrows, preparations, probes, CP
  instruments, and UCP channels;
- preservation of source, target, composition, dagger, sums, scalar
  amplitudes, and outcome branches;
- preservation of matched-control declarations; and
- an equivalence of passive presentation groupoids.

On represented amplitude arrows,

$$
T(a)=T_y aT_x^*
$$

for $a:H_x\to H_y$. On effects and channels it acts by the corresponding
conjugations.

This is stronger than equality of outcome probabilities. It preserves the
counterfactual experiment law and its coherent composites.

---

## 3. Nested commutative alternatives

Finite commutative C*-subalgebras encode compatible Boolean families of
projections; their order-theoretic role in a general C*-algebra is reviewed in
[10]. Only the elementary finite-dimensional classification is needed here,
and it is proved below.

### Definition 3.1 — algebraic seam candidate

At a boundary $x$, an algebraic seam candidate is a pair

$$
R\subseteq F\subseteq B(H_x)
$$

of finite-dimensional commutative unital C*-algebras such that every minimal
projection of $F$ is an admitted projective alternative.

Write

$$
F=C^*(Q_k:k\in K).
$$

Because $R\subseteq F$ is a unital commutative subalgebra, there is a unique
partition

$$
K=\coprod_{r\in\Omega}K_r
$$

such that

$$
R=C^*(P_r:r\in\Omega),
\qquad
P_r=\sum_{k\in K_r}Q_k.
$$

The fine-to-coarse refinement is therefore derived from the algebra
inclusion. It is not a second supplied field.

We require $|\Omega|\ge2$. At least one $K_r$ must contain more than one fine
atom, because otherwise the matched no-write discriminator below cannot fire.

### Proposition 3.2 — classification by rank and partition type

Let $\dim H_x=d$. Every nested pair $R\subseteq F$ is unitarily equivalent to
a canonical pair determined by:

1. a positive rank vector

$$
\mathbf q=(q_1,\ldots,q_n),
\qquad
\sum_{k=1}^n q_k=d;
$$

2. a set partition $\pi$ of $\{1,\ldots,n\}$.

For fixed type $\tau=(\mathbf q,\pi)$, the unlabelled candidate space is a
compact homogeneous orbit

$$
\mathcal F_\tau
\simeq
U(d)/N_\tau,
$$

where $N_\tau$ is the normalizer of the canonical nested pair, including
block unitaries and only those permutations preserving ranks and the coarse
partition.

*Proof.* The minimal projections of $F$ are pairwise orthogonal and sum to the
identity, so their ranges give an orthogonal decomposition of $\mathbb C^d$
with dimensions $q_k$. A unitary carries it to the canonical coordinate
decomposition. A unital subalgebra of $\mathbb C^n$ consists exactly of
functions constant on the blocks of a unique set partition, giving $R$.
Two unitaries determine the same unlabelled nested pair precisely when they
differ by the stated normalizer. $\square$

### Corollary 3.3 — finite type inventory

For fixed $d$, only finitely many rank vectors and set partitions occur. The
space of every type is finite-dimensional. This does not imply that the full
seam space over an arbitrary admitted arrow law is a finite union: the packet
family may itself be infinite.

### Definition 3.4 — operationally reduced candidate

For a packet $\omega$ and a nested pair, call a fine atom $Q_k$ **used** when
both conditions hold:

1. $Q_kU\eta\ne0$ or $Q_kN\eta\ne0$ for some admitted preparation; and
2. $fCQ_kA\eta\ne0$ for some typed admitted composite built from the packet,
   where $A\in\{U,N\}$ and $C\in\mathsf V\cup\mathsf E$.

A coarse sector is used when one of its fine atoms is used. A candidate is
operationally reduced when every fine atom and every coarse sector is used.

This is a nonvacuity condition, not spatial support. It removes extensions on
which the packet has no preparation-and-probe discriminator. It does not
identify two genuinely different admitted counterfactual completions.

### Definition 3.5 — contextual operational reduction

For two admitted arrows $a,b:x\to y$ in one typed process layer, write

$$
a\equiv_D b
$$

when every admitted, well-typed one-hole scalar context $C[-]$ built from the
preparations, probes, compositions, daggers, instruments, and comparison
experiments of $D$ gives

$$
C[a]=C[b].
$$

The quantification is over the complete represented grammar, not merely the
packet currently being tested. Let $\overline D$ be the typed quotient by
this relation. A seam is counted only up to the induced equivalence of its
packet arrows and projector algebras in $\overline D$; every retained fine
atom and coarse sector must also satisfy Definition 3.4.

### Proposition 3.6 — existence and covariance of the reduction

Contextual operational equivalence is a dagger-compatible composition
congruence. Hence $\overline D$ exists as a typed quotient of the represented
process theory. Every strong represented equivalence $T:D\simeq D'$ descends
to an equivalence $\overline T:\overline D\simeq\overline {D'}$.

*Proof.* Reflexivity, symmetry, and transitivity are inherited from equality
of all scalar evaluations. If $a\equiv_D b$, inserting either arrow into a
larger admitted composition or dagger context still gives a one-hole admitted
context, so the equality is stable under every typed constructor. This is
precisely the congruence property needed for the quotient. A strong
represented equivalence bijects the complete families of scalar contexts and
preserves their values, so it carries congruence classes bijectively and
respects every quotient operation. $\square$

This quotient is the exact finite-scope answer to dormant presentation
structure. It does not identify laws that differ in any admitted
counterfactual context, even if the actually executed history is the same.

---

## 4. Exact W3 seam equations

Fix an eligible packet $\omega$ and an operationally reduced nested pair
$R\subseteq F$ at $x_1$.

### Definition 4.1 — write correlation

The write arrow $U$ satisfies exact fine-to-record correlation when, for all
$\eta\in\mathsf P$, all $r\in\Omega$, and all distinct
$k,\ell\in K_r$,

$$
\|Q_kU\eta\|^2\,\|Q_\ell U\eta\|^2=0.
$$

Thus every prepared state has at most one live fine alternative inside each
coarse record sector.

### Definition 4.2 — matched no-write failure

The matched control $N$ fails correlation when there exist
$\eta\in\mathsf P$, $r\in\Omega$, and distinct $k,\ell\in K_r$ with

$$
\|Q_kN\eta\|^2\,\|Q_\ell N\eta\|^2>0.
$$

This is an operational discriminator between $U$ and its matched control. It
does not prove that the control realizes metaphysical nonoccurrence.

### Definition 4.3 — preserving availability

A continuation $V\in\mathsf V$ preserves availability when, for every
$f\in\mathsf F$, there is a coarse sector $r=r(V,f)$ such that

$$
fV=fVP_r.
$$

Equivalently,

$$
fVP_s=0
\qquad
\text{for every }s\ne r.
$$

In fine notation, two nonzero rows $fVQ_k$ and $fVQ_\ell$ must belong to one
coarse sector. Every continuation declared preserving in the packet must pass
this equation.

### Definition 4.4 — coherent erasure

An erasing continuation $E\in\mathsf E$ exposes cross-record coherence when
there exist $\eta\in\mathsf P$, $f\in\mathsf F$, and fine atoms
$k\in K_r$, $\ell\in K_s$ with $r\ne s$ such that

$$
c_k=fEQ_kU\eta,
\qquad
c_\ell=fEQ_\ell U\eta,
$$

obey

$$
c_k\overline{c_\ell}\ne0.
$$

At least one erasing continuation must pass this condition. The individual
cross term is primary: a summed Born defect can vanish by cancellation while
cross-sector coherence survives.

### Definition 4.5 — W3 seam

A W3 seam is a pair

$$
s=(\omega,R\subseteq F)
$$

that is fully typed, operationally reduced, and satisfies Definitions
4.1--4.4.

The set of all such seams is

$$
\operatorname{Seam}^{\mathrm{raw}}_{W3}(D).
$$

### Proposition 4.6 — support form and the classical seam

For rank-one configuration alternatives and configuration preparations and
probes, Definitions 4.1 and 4.3 are exactly the support-level correlation and
availability criteria. If both hold, every cross term between distinct fine
alternatives in a preserve composite vanishes separately.

*Proof.* If a cross term through $Q_k,Q_\ell$ is nonzero, the two alternatives
are live after $U$ and both reach one final probe through $V$. Availability
places them in one coarse sector; correlation forbids two distinct live fine
atoms in that sector. Hence $k=\ell$. $\square$

This proposition recovers the classical stochastic seam under preserving
continuations while Definition 4.4 requires the same process law to retain a
coherent erasing alternative.

---

## 5. The seam locus

### Theorem 5.1 — semialgebraic structure

Fix:

- finite boundary dimensions;
- one finite packet $\omega$;
- one rank/partition type $\tau$; and
- a semialgebraic admitted projector family.

Then the W3 seam solutions of type $\tau$ form a real semialgebraic subset

$$
\mathcal Z_{\omega,\tau}\subseteq\mathcal F_\tau.
$$

For a passive presentation change $g$,

$$
g\mathcal Z_{\omega,\tau}
=
\mathcal Z_{g\omega,\tau}.
$$

In particular, the locus is invariant under the passive stabilizer of the
represented packet.

*Proof.* Write every complex matrix entry as two real coordinates. Hermiticity,
idempotence, orthogonality, fixed rank, and resolution of the identity are
polynomial equations. The write and availability conditions are finite sums
and products of squared norms set equal to zero. The no-write and erasure
conditions are strict positivity of squared absolute values. Operational
reduction is a finite conjunction of nonvanishing conditions. Intersection
with the admitted projector family is semialgebraic by hypothesis. Therefore
the solution is semialgebraic. Simultaneous unitary conjugation preserves
every equation and nonvanishing condition and carries the represented packet
to $g\omega$, proving covariance. $\square$

### Scope 5.2 — why this is not automatically a manifold

A semialgebraic seam locus may have singularities, components of different
dimensions, and changing stabilizers. The full union over an infinite packet
law need not be finite-dimensional globally. We therefore claim a
componentwise finite-dimensional semialgebraic moduli problem, not a smooth
manifold theorem.

### Definition 5.3 — passive presentation action groupoid

Let $\mathcal P(D)$ be the orbit of represented presentations of $D$ under
families of boundary unitaries. Its seam-presentation object space is

$$
\mathcal O_D
=
\{(D',s):D'\in\mathcal P(D),\ s\in
\operatorname{Seam}^{\mathrm{raw}}_{W3}(D')\}.
$$

An arrow

$$
(D,s)\longrightarrow(D',s')
$$

is a passive unitary presentation change $g$ carrying every boundary,
amplitude, preparation, probe, instrument, comparison declaration, $Q_k$, and
$P_r$ to the primed data. Composition is unitary composition.

The **W3 seam stack** is the action groupoid

$$
\boxed{
\mathfrak{Seam}_{W3}(D)
=
[\mathcal O_D/G_{\mathrm{pres}}(D)].
}
$$

The brackets denote this explicit groupoid. They do not denote a coarse orbit
set. In particular, the automorphism group of an object is retained.

This retained-stabilizer language is the elementary action-groupoid fragment
of the groupoid presentation of differentiable stacks [11]. No differentiable
stack theorem is imported.

### Proposition 5.4 — handle invariance

Relabelling the fine or coarse outcome handles induces an isomorphism in
$\mathfrak{Seam}_{W3}(D)$ and changes no nested algebra, W3 equation, or
stabilizer up to conjugacy.

*Proof.* The equations quantify over atoms and sectors and depend only on the
projectors and their inclusion. A handle bijection merely permutes a finite
resolution. $\square$

---

## 6. Passive gauge, active symmetry, and no selection

### Definition 6.1 — active physical automorphism

An active physical automorphism of $D$ is an invertible automorphism of the
represented operational law: it preserves the admitted arrow and instrument
families, comparison relations, and all operational pairings, while acting on
the physical candidates inside one fixed theory.

Passive presentation change maps one coordinate presentation of the whole law
to another. Active symmetry maps an operational alternative to another
alternative of the same fixed law. These roles are not quotiented together.

### Proposition 6.2 — physical action on seam moduli

Every active physical automorphism maps W3 seams to W3 seams and therefore
acts on $\mathfrak{Seam}_{W3}(D)$ after passive presentation quotienting.

*Proof.* It preserves every admitted packet, composite, norm, zero relation,
and nonzero relation. Since it acts on the fixed law rather than only on its
coordinates, its orbit remains as physical multiplicity. $\square$

The corresponding physical action groupoid is

$$
\mathfrak{Seam}^{\mathrm{phys}}_{W3}(D)
=
\operatorname{Aut}_{\mathrm{phys}}(D)
\ltimes
\mathfrak{Seam}_{W3}(D).
$$

Passive presentation arrows have already been quotiented groupoid-wise in the
second factor. Active automorphisms appear as additional arrows here; taking a
coarse orbit set is forbidden.

### Theorem 6.3 — automorphism no-selection

Let a physical symmetry group act transitively on a set of at least two seam
objects. No equivariant rule depending only on the invariant represented law
can select one object.

*Proof.* If $s$ were selected, equivariance would require $g s=s$ for every
symmetry $g$. Transitivity supplies a $g$ with $g s\ne s$, a contradiction.
$\square$

The honest output is the symmetry orbit/action groupoid unless an additional
invariant discriminator exists.

---

## 7. Presentation-invariance theorem

### Theorem 7.1 — strong operational equivalence

A strong represented equivalence $T:D\simeq D'$ induces an equivalence

$$
T_*:
\mathfrak{Seam}_{W3}(D)
\simeq
\mathfrak{Seam}_{W3}(D').
$$

*Proof.* Apply $T$ to every boundary and arrow of a packet and put

$$
Q'_k=T_{x_1}Q_kT_{x_1}^*,
\qquad
P'_r=T_{x_1}P_rT_{x_1}^*.
$$

Unitary conjugation preserves projector equations, ranks, algebra inclusion,
all norms, and every composite scalar. Hence it preserves write correlation,
no-write failure, availability, erasure, and operational reduction. The
inverse equivalence supplies an inverse on objects. Naturality with passive
presentation arrows gives a functor between action groupoids, and the unit and
counit of the represented equivalence give the groupoid equivalence.
$\square$

The theorem is substantive only after the equivalence notion is fixed. It
does not say that equal marginal laws imply equivalent process theories.

### Corollary 7.2 — redundant grammar

If two syntactic presentations have the same represented completed theory,
including the same instrument branches and matched-control relation, their
seam groupoids are canonically equivalent.

Adding a redundant generator with a relation identifying it to an existing
composite therefore changes no seam. Adding a genuinely new counterfactual
continuation can change the seam family and is not redundant grammar.

### Proposition 7.3 — Kraus invariance at the channel layer

Suppose two Kraus families represent the same CP branch or UCP channel. Every
subsequent effect-transport, sharpness-defect, operator-system, and
idempotent-fiber construction in this paper is identical for the two
families.

*Proof.* Those constructions use the CP linear map itself. Equal Kraus sums
define the same map on every operator, so every image, composite, defect, and
fixed system agrees. $\square$

This proposition does not replace a coherent amplitude arrow by an arbitrary
Kraus decomposition. Native amplitude interference is evaluated on the
represented amplitude arrow. Nor does equality of POVMs identify two
instruments with different outcome-conditioned CP branches.

The operator-sum representation used here is the representation of the CP map,
not extra physical outcome data [4].

### Theorem 7.4 — minimal instrument-preserving dilation invariance

Let one admitted finite-outcome instrument have two minimal Stinespring/
pointer representations that preserve its complete outcome CP maps. Then the
two dilation presentations are related by a unitary intertwiner preserving the
system embedding and pointer sectors. Any seam construction performed on the
formal dilation presentation and descended through that equivalence is
presentation-equivalent.

*Proof.* Regard the instrument as one CP map into the direct-sum
classical-quantum output algebra. Minimal Stinespring representations of the
same CP map are unitarily equivalent. Explicitly, on the algebraic span of
vectors generated by the represented map, send the first dilation vector to
the corresponding second vector. Equality of the CP map makes this assignment
inner-product preserving; minimality makes the span dense and hence the
isometry unitary. Outcome direct-sum central projections are intertwined, so
the pointer sectors and disturbance branches are preserved. $\square$

This is the instrument-preserving version of the standard minimal-dilation
uniqueness mechanism [3,5]. Minimal Naimark dilations are also useful in
finite POVM compatibility analysis [13], but that POVM-level use is weaker
than the instrument hypothesis imposed here.

### Warning 7.5 — POVM-only Naimark equivalence is insufficient

Two instruments may have the same POVM and different disturbance. A minimal
Naimark dilation of the POVM alone therefore does not establish equivalence of
W3 preserve/erase packets. Moreover, a formal dilation ancilla is not a new
physical boundary unless the operational theory admits it as one. This paper
does not turn a formal pointer PVM into a native system seam.

### Proposition 7.6 — formal inaccessible spectator invariance

Let $D\boxtimes K$ be a presentation refinement in which every admitted
boundary algebra, amplitude, preparation, probe, projector, instrument, and
comparison is exactly the image of $D$ under

$$
a\longmapsto a\otimes I_K,
$$

with no spectator-resolving operation admitted. Then

$$
\mathfrak{Seam}_{W3}(D)
\simeq
\mathfrak{Seam}_{W3}(D\boxtimes K).
$$

*Proof.* Tensoring maps every nested pair to
$R\otimes I_K\subseteq F\otimes I_K$ and preserves every zero and nonzero
W3 composite up to the fixed nonzero spectator factor. By hypothesis, every
admitted projector and packet in the refinement lies in this image. The
tensor functor is therefore full and essentially surjective on seam data, with
the evident inverse that forgets the formal multiplicity. $\square$

If spectator-resolving projectors or controls are admitted, the hypothesis
fails: the spectator has become operational content and new seams are not
forbidden.

### Proposition 7.7 — scoped idempotent-split refinement

An idempotent-split or Karoubi boundary presentation preserves the seam
groupoid only when its inclusion and retraction extend to a strong represented
equivalence preserving packets, projectors, instruments, and comparison
relations. Abstract Cauchy completion alone is not sufficient.

*Proof.* Under the stated extension, apply Theorem 7.1. Without it, the new
boundary may contain new admitted packets or projectors and there is no inverse
functor on seam data. $\square$

### Corollary 7.8 — exact scope of intrinsicness

The seam groupoid is intrinsic to the represented operational theory up to
the strong equivalences above. It is not intrinsic to one realized history,
to a probability table, or to an unspecified class of operationally similar
models.

---

## 8. Counterfactual completion remains physical

### Proposition 8.1 — same realized amplitudes, different seam families

Two operational theories can agree on every actually executed amplitude and
record law while admitting different future continuation families. Their W3
seam groupoids can differ.

*Proof.* Begin with a write arrow and a candidate nested pair satisfying
correlation. In $D_+$ admit a preserving continuation and a coherent eraser;
in $D_-$ replace the preserving continuation by one that mixes every coarse
sector into one accessible probe. The realized write experiment is identical,
but the candidate satisfies availability in $D_+$ and fails it in $D_-$. The
two theories are not strongly equivalent because their admitted continuation
laws differ. $\square$

Thus seam reconstruction is nomological at this scope. This is not a defect:
the W3 concept itself is counterfactual, because availability and erasure ask
what admitted continuations would do.

---

## 9. Complete branch-memory seam classification

This section solves one finite moduli problem rather than inserting its known
record PVM.

### 9.1 The represented packet

Let

$$
H=\mathbb C_b^2\otimes\mathbb C_m^2
$$

and let

$$
H_2=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
$$

The packet contains all four computational preparations and probes and the
arrows

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

No record PVM is supplied. The control law admits every atomic rank-one fine
resolution at the intermediate boundary. We solve over all atomic nested
pairs: $F$ has four rank-one atoms and $R$ is any nontrivial proper
coarsening with at least one nonsingleton block.

Admission of every atomic rank-one resolution is an explicit full-projective-
access postulate of this control law, not a conclusion of W3. What is derived
is which of those admitted questions satisfy all four W3 equations. A more
restricted operational theory would generally have a smaller seam locus.

Define the availability basis

$$
v_0=|+,0\rangle,
\quad
v_1=|-,0\rangle,
\quad
v_2=|+,1\rangle,
\quad
v_3=|-,1\rangle.
$$

These vectors satisfy

$$
v_i=V^*|i\rangle
$$

after the corresponding ordering of computational probes. In the preparation
order $(|00\rangle,|10\rangle,|01\rangle,|11\rangle)$, put

$$
A_{ij}=2\langle v_i|U|j\rangle.
$$

Then

$$
A=
\begin{pmatrix}
1&1&1&-1\\
1&1&-1&1\\
1&-1&1&1\\
-1&1&1&1
\end{pmatrix},
\qquad
A^*A=4I.
$$

Thus the write states are the four normalized columns of a real Hadamard
matrix in the availability basis.

### Lemma 9.1 — availability discretizes the coarse algebra

Every rank-type seam in this packet has coarse projectors

$$
P_B=\sum_{i\in B}|v_i\rangle\langle v_i|
$$

for the blocks $B$ of a set partition of $\{0,1,2,3\}$.

*Proof.* Availability says that each row $\langle i|V$ has support in one
coarse sector. Equivalently, each $v_i=V^*|i\rangle$ lies in the range of one
$P_B$. The $v_i$ form an orthonormal basis, and the coarse projectors are
orthogonal and complete. Each coarse range is therefore the span of a subset
of this basis. $\square$

No continuity remains in $R$: the preserving continuation and probe family
reduce it to a finite partition problem.

### Lemma 9.2 — fine algebra inside one coarse block

Let $B$ be a coarse block. Write $A_{B,j}$ for column $j$ restricted to rows
in $B$. Write correlation is possible with an atomic refinement of $P_B$ if
and only if the nonzero rays

$$
[A_{B,j}],
\qquad j=0,1,2,3,
$$

are contained in an orthogonal basis of $\mathbb C^{|B|}$. Operational
reduction requires them to use that basis.

For the displayed Hadamard matrix:

- if $|B|=1$, there is one ray and the fine atom is $|v_i\rangle\langle v_i|$;
- if $|B|=2$, there are exactly two orthogonal rays, represented by

$$
\frac{v_i+\epsilon v_j}{\sqrt2},
\qquad
\frac{v_i-\epsilon v_j}{\sqrt2}
$$

for a sign $\epsilon$ fixed by the two selected rows; and
- if $|B|=3$, the four restricted columns are distinct and no two are
  orthogonal.

*Proof.* A write state has at most one live fine atom in $B$ exactly when its
projection $P_BU|j\rangle$ lies on one fine-projector ray. For two selected
rows, every restricted sign column is proportional to one of two vectors
$(1,1)$ and $(1,-1)$ after a fixed row sign; these rays are orthogonal and
both occur. For three selected rows, omit row $t$. Orthogonality of full
Hadamard columns $j\ne k$ gives

$$
\langle A_{B,j},A_{B,k}\rangle
=
-A_{tj}A_{tk}
\in\{+1,-1\}.
$$

The restricted rays are also distinct, so four nonorthogonal rays cannot lie
in a three-vector orthogonal basis. $\square$

### Lemma 9.3 — no-write and eraser tests

For every partition all of whose blocks have size at most two and with at
least one size-two block, the uniquely determined fine algebra from Lemma 9.2
passes both remaining tests.

*Proof.* The no-write states $N|j\rangle$ are, up to signs and ordering, the
$v_i$. If $v_i$ belongs to a two-element block, it has nonzero overlap with
both sum/difference fine rays in that block. Thus the matched control has two
live fine alternatives in one coarse sector.

For erasure, $E=U^*$. For a write state $\psi_j=U|j\rangle$, its projection
onto a block $B$ lies on the unique fine ray selected by the restricted
Hadamard column. If $Q_{B,j}$ is that fine atom, then

$$
\langle j|EQ_{B,j}U|j\rangle
=
\langle\psi_j|Q_{B,j}|\psi_j\rangle
=
\frac{|B|}{4}.
$$

Every block contributes positively. Because there are at least two blocks,
choosing $B\ne C$ gives the nonzero cross-sector product

$$
\frac{|B|\,|C|}{16}>0.
$$

$\square$

### Theorem 9.4 — exactly nine atomic seams

For the fixed branch-memory packet and atomic rank type above, the unlabelled
W3 seam set has exactly nine objects before active physical-symmetry
identifications:

$$
\boxed{
6\text{ partitions of type }2+1+1
\quad\sqcup\quad
3\text{ partitions of type }2+2.
}
$$

For each coarse partition, the fine algebra is unique as an unlabelled
projector algebra.

*Proof.* There are fifteen set partitions of a four-element set. The one-block
partition is excluded because a record has at least two coarse values. The
all-singleton partition makes $R=F$; each no-write state is one fine atom, so
the matched no-write failure does not occur. Every partition containing a
block of size three fails Lemma 9.2. The remaining partitions are precisely
the six choices of one pair plus two singletons and the three perfect
matchings. Lemmas 9.1--9.3 prove that each is a seam. Uniqueness of $F$ follows
from the complete list of restricted rays in every block. $\square$

| coarse partition type | number | write correlation | no-write failure | preserving availability | eraser cross term | result |
|---|---:|---|---|---|---|---|
| $4$ | 1 | possible | possible | yes | possible | excluded: one record value |
| $3+1$ | 4 | fails | not reached | yes | not reached | reject |
| $2+2$ | 3 | passes | passes | passes | $1/4$ | accept |
| $2+1+1$ | 6 | passes | passes | passes | at least $1/16$ | accept |
| $1+1+1+1$ | 1 | passes | fails | passes | not a W3 eraser test | reject |

The table is a classification, not a sampled census: all fifteen set
partitions appear exactly once.

### Corollary 9.5 — the familiar memory seam is not uniquely selected

The memory record corresponds to

$$
\{v_0,v_1\}\mid\{v_2,v_3\}.
$$

Its derived fine rays are the four computational basis states. It is one of
the three $2+2$ seams, not the unique W3 solution.

The exact process law therefore reconstructs a finite seam moduli family but
does not by itself distinguish “memory” from every other W3-positive coarse
record question. Any unique-memory claim requires an additional invariant
operational discriminator.

### Scope 9.6 — what was solved

The count nine is exhaustive for:

- the displayed four-dimensional packet;
- all four computational preparations and probes;
- one declared preserving and one erasing continuation;
- atomic fine rank $(1,1,1,1)$; and
- every permitted coarse partition.

It is not a classification of all higher-rank fine algebras or every possible
branch-memory experiment grammar. In particular, it does not derive the
full-projective-access postulate used by this benchmark.

---

## 10. Selection and no-smuggling controls

### Control 10.1 — rotated fine resolutions fail

Take any accepted two-element block $B=\{i,j\}$ with its derived orthogonal
fine rays $q_+,q_-$. Replace them by

$$
q'_+=\cos\theta\,q_++\sin\theta\,q_-,
\qquad
q'_-=-\sin\theta\,q_++\cos\theta\,q_-
$$

with $0<\theta<\pi/2$ and $\theta\ne\pi/2$ modulo a permutation. A write
projection that lies on $q_+$ has nonzero components on both rotated fine
atoms, so write correlation fails inside one coarse sector.

Thus the equations select discrete fine rays rather than accepting every
rotated PVM.

### Control 10.2 — rotated coarse sectors fail availability

Start from two coarse blocks and rotate one $v_i$ from the first with one
$v_j$ from the second through a nontrivial angle, leaving the remaining basis
vectors fixed. The transported final probe $v_i$ then has nonzero components
in two rotated coarse sectors. Hence no $r$ satisfies

$$
\langle i|V=\langle i|VP_r,
$$

and availability fails.

### Control 10.3 — inaccessible spectator

Apply Proposition 7.6 to the branch-memory packet. The admitted fine atoms are
$Q_k\otimes I_K$, not arbitrary rank-one projectors resolving the formal
spectator. The nine-object seam groupoid is carried bijectively to the
spectator presentation. If spectator-resolving projectors are added, the
model has changed and the control no longer applies.

### Control 10.4 — quaternion support smuggling

The public quaternion process has three genuine cyclic order-four subgroups
with a common central order-two subgroup. Its attached two-level W3 witness is
a separate amplitude packet. The packet's boundary types, write, control,
continuations, probes, and candidate projectors do not lie in the quaternion
amplitude subtheory.

Under Definition 4.5 it can therefore produce a seam only in the attached
two-level packet. It produces no quaternion seam. Reassigning that seam to one
of the cyclic subgroups through a support list is not an arrow of the seam
groupoid and has no effect on the result.

This preserves the quaternion subgroup arithmetic while rejecting the
record-to-subgroup attachment.

### Control 10.5 — equivalent grammars

Add a generator $W$ to the branch-memory presentation together with the exact
relation $W=VU$, or remove it and use the composite. Both presentations have
the same represented completion, packet family, and matched-control
relations. Corollary 7.2 gives identical nine-object seam groupoids.

If instead a new continuation is admitted without an equality relation, the
completion changes. Invariance is neither expected nor claimed.

### Control 10.6 — symmetric copies

Let a theory contain two separately typed copies of the same W3 packet and an
active physical swap exchanging them. Passive coordinate changes preserve the
two boundary roles; the active swap is not declared gauge. The two copied seam
objects therefore survive in one physical symmetry orbit with a swap arrow in
$\mathfrak{Seam}^{\mathrm{phys}}_{W3}(D)$.
Theorem 6.3 forbids an invariant selection of “the first” copy.

### Proposition 10.7 — universal-control no-seam theorem

Suppose a finite-dimensional packet admits, as preserving candidates to be
passed simultaneously, every unitary continuation and a separating rank-one
probe family. Then no proper coarse record algebra with at least two nonzero
sectors satisfies availability.

*Proof.* Let $P_r,P_s$ be two nonzero coarse sectors. Choose unit vectors
$u\in\operatorname{Ran}P_r$ and $v\in\operatorname{Ran}P_s$. For one
rank-one final probe $f$, choose a unitary $V$ for which

$$
V^*f^*=\frac{u+v}{\sqrt2}.
$$

Then $fVP_r\ne0$ and $fVP_s\ne0$, contradicting availability. $\square$

This control returns an empty proper seam locus rather than manufacturing a
preferred basis. It also shows why the admitted continuation law is
load-bearing.

---

## 11. Transport derived after seam reconstruction

Let $s=(\omega,R_s\subseteq F_s)$ be a reconstructed seam at native boundary
$x_s$, with

$$
R_s=C^*(P_r:r\in\Omega_s).
$$

### Definition 11.1 — seam-relative observability system

For a boundary $y$ and all admitted Heisenberg transports

$$
\Phi_a^*:B(H_{x_s})\longrightarrow B(H_y),
$$

define

$$
\mathcal S_s(y)
=
\operatorname{span}_{\mathbb C}
\left\{
I,\Phi_a^*(P_r),\Phi_a^*(P_r)^*
\right\}.
$$

This definition is applied after $s$ is known. It does not participate in the
W3 seam equations.

### Proposition 11.2 — inherited transport layers

For every admitted UCP transport:

1. $(\Phi_a^*(P_r))_r$ is a POVM;
2. the record sharpness defect

$$
\Sigma_{\Phi_a^*}(P_r)
=
\Phi_a^*(P_r)-\Phi_a^*(P_r)^2
$$

is positive;
3. exact Boolean proposition transport occurs precisely when

$$
R_s\subseteq\operatorname{MD}(\Phi_a^*);
$$

and
4. supplied outcome instruments remain above the POVM shadow.

These are seam-indexed instances of the earlier finite-dimensional transport
theorems. None selects a true record atom or proves co-reference.

The Schwarz and multiplicative-domain facts used by this inherited layer are
the standard UCP results [6,7].

### Proposition 11.3 — presentation covariance

An isomorphism $g:s\to s'$ in the seam groupoid carries
$\mathcal S_s(y)$ to $\mathcal S_{s'}(g y)$ by conjugation. Record handles do
not enter the operator-system identity.

*Proof.* The seam isomorphism carries each $P_r$, admitted transport, and
composite to its conjugate. Linear spans commute with this bijection. $\square$

---

## 12. The addressability fibration

Completely positive idempotents and their fixed operator systems require the
Choi--Effros range product in general [8]. Treating admitted idempotent splits
as typed process objects follows the categorical splitting construction in
[9].

### Definition 12.1 — containing admitted idempotents

For a seam $s$ and observation boundary $y$, let

$$
\mathsf{Idem}_s(y)
$$

be the physically admitted UCP maps $e:B(H_y)\to B(H_y)$ satisfying

$$
e^2=e,
\qquad
\mathcal S_s(y)\subseteq\operatorname{Fix}(e).
$$

Order them by

$$
e\preceq f
\quad\Longleftrightarrow\quad
ef=fe=e.
$$

The identity is always admitted and always contains the operator system.

### Lemma 12.2 — minimal candidates exist in finite dimension

Every nonempty $\mathsf{Idem}_s(y)$ has a minimal element.

*Proof.* If $e\preceq f$, then

$$
\operatorname{Ran}(e)\subseteq\operatorname{Ran}(f).
$$

If the ranges are equal, then $ef=f$ because $e$ is the identity on the range
of $f$, while the order gives $ef=e$; hence $e=f$. Every strict descent thus
strictly lowers the finite vector-space dimension of the range. Starting from
identity, a descending chain terminates. $\square$

### Definition 12.3 — addressability fiber

Let $\mathfrak{Addr}_s(D)$ have as objects triples $(y,e)$ with $e$ minimal in
$\mathsf{Idem}_s(y)$. Its arrows are invertible admitted Karoubi intertwiners
that preserve the seam-relative operator system. Physical automorphisms are
retained.

The fiber records:

- whether a proper minimum exists;
- whether it is unique;
- whether several minima are incomparable; and
- their physical symmetry groupoid.

### Theorem 12.4 — equivariant fiber assignment

The assignment

$$
s\longmapsto\mathfrak{Addr}_s(D)
$$

is a pseudofunctor from the seam groupoid to groupoids of minimal admitted
idempotents. Because all fiber arrows in Definition 12.3 are invertible, this
codomain is well typed. Because the base is a groupoid, its
Grothendieck construction

$$
\boxed{
\pi:\mathfrak{AddrW3}(D)
\longrightarrow
\mathfrak{Seam}_{W3}(D)
}
$$

is both a fibration and an opfibration.

*Proof.* A seam isomorphism implemented by $g$ sends

$$
e\longmapsto geg^{-1}.
$$

It preserves UCP, idempotence, admission, fixed-range containment, the order
$\preceq$, minimality, and Karoubi intertwiners. Conjugation respects identity
and composition exactly. The standard Grothendieck category has objects
$(s,y,e)$ and arrows consisting of a base seam isomorphism together with the
induced fiber arrow. Cartesian and cocartesian lifts exist because every base
arrow is invertible. $\square$

The pseudofunctor/fibration correspondence used in this last step is the
ordinary Grothendieck construction [12].

The same conjugation construction is equivariant for the separately declared
active physical-symmetry action. It therefore extends to the physical
symmetry action groupoid $\mathfrak{Seam}^{\mathrm{phys}}_{W3}(D)$ without
turning active symmetries into passive gauge identifications.

### Proposition 12.5 — presentation invariance of the fibration

A strong represented equivalence $D\simeq D'$ induces an equivalence of total
categories over the base equivalence of Theorem 7.1.

*Proof.* The equivalence conjugates admitted UCP idempotents and operator
systems, hence gives fiberwise equivalences compatible with base arrows.
$\square$

### 12.1 Exact fiber controls

The following controls are finite-dimensional and use physically declared
admission sets.

#### Unique proper minimum

Let $B=M_2(\mathbb C)$,

$$
\mathcal S=\operatorname{span}\{I,Z\},
$$

and admit only identity and the $Z$-pinching

$$
D_Z(a)=P_+^ZaP_+^Z+P_-^ZaP_-^Z.
$$

Then $D_Z$ is the unique proper minimum.

#### Admitted versus abstract

With the same $\mathcal S$, remove $D_Z$ from the admitted law. The matrix
formula still exists abstractly, but the fiber becomes no-proper/identity-only.
Physical admission, not algebraic imagination, determines the result.

#### Incomparable symmetry-related minima

Take a W3 seam whose record observability is carried by the first qubit and
whose admitted transports do not probe an auxiliary second qubit. Let
$B=M_2\otimes M_2$ and

$$
\mathcal S=\operatorname{span}\{I,Z\otimes I\}.
$$

On the auxiliary qubit choose Bloch axes $n,m$ with

$$
0<|n\cdot m|<1
$$

and a unitary involution $A$ whose Bloch action swaps $n$ and $m$. Admit the
channel category generated by

$$
e_n=\operatorname{id}\otimes D_n,
\qquad
e_m=\operatorname{id}\otimes D_m,
\qquad
\alpha=\operatorname{id}\otimes\operatorname{Ad}_A.
$$

Both $e_n$ and $e_m$ fix $\mathcal S$. Their ranges are incomparable. No
mixed finite word is another idempotent: on the auxiliary Bloch space every
word reduces to an alternating product of the rank-one projections
$nn^{\mathsf T}$ and $mm^{\mathsf T}$, optionally followed by the involution
swapping them. A mixed word has its only possible nonzero eigenvalue with
absolute value a positive power of $|n\cdot m|$, strictly between zero and
one; a nontrivial trailing involution is not idempotent. Thus the only
idempotents in the generated grammar are identity, $e_n$, and $e_m$.

The active symmetry $\alpha$ swaps the two minima while fixing $\mathcal S$,
giving a two-object symmetry groupoid rather than a selected representative.

#### Global/identity forced

If $\mathcal S=B(H)$, any containing idempotent fixes every operator and is
therefore identity. This differs from a proper $\mathcal S$ in a grammar that
simply admits no proper idempotent.

### Interpretation 12.6 — the ceiling

The fibration classifies repeatable coarse-grainings of every reconstructed
seam-relative observability system. It does not provide independent
preparations, arbitrary internal control, selective nondemolition readout, a
disposable complement, a tensor factor, a spatial boundary, or a physical
overlap.

---

## 13. Four-gate audit

### 13.1 Nested commutative pair

- **Referent.** Actual admitted projective alternatives at one typed quantum
  boundary.
- **Necessity.** Earlier transport results began with one selected record PVM
  and fine/coarse refinement.
- **No-smuggling.** The construction ranges over every admitted nested pair of
  the declared rank types; the inclusion derives the refinement map.
- **Discriminator.** The branch-memory equations accept nine pairs and reject
  rotated pairs, size-three coarse blocks, and the all-fine partition for
  different measured reasons.

### 13.2 W3 seam moduli groupoid

- **Referent.** The complete family of exact W3-positive packets and nested
  pairs in the represented process law.
- **Necessity.** Exact symmetry and the branch-memory ninefold result defeat a
  unique preferred seam.
- **No-smuggling.** Passive gauge acts on the whole represented presentation;
  active physical symmetries and stabilizers remain.
- **Discriminator.** Empty, finite-multiple, continuous-component, and
  symmetry-related solution families remain distinct.

### 13.3 Strong operational equivalence

- **Referent.** An equivalence of complete represented process and instrument
  laws, not an equality of probabilities.
- **Necessity.** Basis, handles, Kraus lists, redundant generators, formal
  dilations, and inaccessible spectators should not create physical seams.
- **No-smuggling.** The equivalence is defined without mentioning a target
  seam or preferred projector.
- **Discriminator.** Redundant presentations agree; genuinely different
  continuation completions can disagree.

### 13.4 Addressability fibration

- **Referent.** Minimal physically admitted repeatable UCP coarse-grainings
  containing the observability system of each reconstructed seam.
- **Necessity.** Different seams and different admitted laws can have
  different coarse-grainability classifications.
- **No-smuggling.** Abstract but unadmitted expectations are excluded and the
  operator system is derived only after the seam.
- **Discriminator.** Unique, no-proper, incomparable, symmetry-related, and
  mathematically global fibers are separated.

---

## 14. Theorem and control register

### Definitions

1. amplitude-and-instrument theory;
2. eligible W3 packet;
3. admitted projective resolution;
4. strong represented equivalence;
5. nested commutative seam candidate;
6. packet nonvacuity and contextual operational reduction;
7. four exact W3 predicates;
8. raw seam locus and action groupoid;
9. active physical automorphism;
10. seam-relative observability operator system;
11. containing admitted idempotents; and
12. addressability fiber and total category.

### Proved finite-scope results

1. rank/partition classification of nested commutative pairs;
2. existence and covariance of the contextual operational quotient;
3. semialgebraic W3 loci for fixed finite packets and types;
4. handle and passive-presentation invariance;
5. active-symmetry action and no-selection;
6. seam-groupoid equivalence under strong represented equivalence;
7. redundant-grammar, Kraus, minimal instrument-dilation, formal spectator,
   and scoped idempotent-refinement consequences;
8. exact counterfactual-completion dependence;
9. complete nine-seam branch-memory classification at atomic fine rank;
10. rotated-PVM and universal-control negative results;
11. inherited seam-indexed effect and sharp-proposition transport;
12. finite-dimensional existence of minimal containing idempotents; and
13. the addressability Grothendieck fibration and its presentation
    invariance.

### Exact controls

1. branch-memory write/preserve/erase/no-write packet;
2. rotated fine resolutions;
3. rotated coarse sectors;
4. formal inaccessible spectator;
5. quaternion support-smuggling negative;
6. redundant composite grammar;
7. two physical-symmetry-related copies;
8. universal-control no-seam world; and
9. unique, unadmitted, incomparable-symmetry, no-proper, and global
   addressability fibers.

### Conditional inputs

The semialgebraic theorem assumes a semialgebraic admitted projector family.
The Naimark statement assumes minimal instrument-preserving, not merely
POVM-preserving, dilations. The spectator theorem assumes no
spectator-resolving operation is admitted. The Karoubi statement assumes an
actual strong represented equivalence. Removing any of these hypotheses
removes the corresponding invariance claim.

---

## 15. Outcome audit

### 15.1 `RQ0-L0-W3-SEAM-MODULI`

**Provisional disposition: earned at declared scope.**

The cut, packet, fine algebra, and coarse algebra are reconstruction variables.
The full W3-positive locus is defined across every eligible admitted packet.
For fixed finite packet and rank type it is an invariant semialgebraic locus,
and its passive presentation quotient is an explicit
action groupoid retaining stabilizers. The branch-memory control reconstructs
all nine atomic seams and supplies independent false-seam controls.

The result is law-relative and componentwise. It is not a global smooth
manifold theorem.

### 15.2 `RQ0-L0-PRESENTATION-INVARIANT-W3-SEAMS`

**Provisional disposition: earned for the strong equivalences explicitly
defined here.**

Theorem 7.1 proves equivalence of seam groupoids. The listed grammar, Kraus,
instrument-preserving dilation, inaccessible-spectator, and scoped Karoubi
cases are consequences or explicit specializations. Equal POVMs with
different instruments and different counterfactual process completions are
correctly excluded.

This is not invariance under every imaginable empirical equivalence relation.

### 15.3 `RQ0-L0-ADDRESSABILITY-FIBRATION`

**Provisional disposition: earned at admitted-idempotent coarse-graining
scope.**

Every seam has a derived operator-system family. Minimal admitted containing
idempotents exist in finite dimension, transform equivariantly, and assemble
through the Grothendieck construction. All ambiguity is retained.

The word *addressability* has only the adjudicated meaning of repeatable
coarse-graining. Autonomous subsystem control is not claimed.

### 15.4 No blocked verdict

No explicit typing or invariance counterexample defeats the registered finite
scope. The result therefore does not return one of the three registered
blocked outcomes. The two independent hostile reviews remain required before
any terminal status.

---

## 16. Ontological result

The construction changes the ontology in one precise way. A W3 seam is no
longer one record PVM attached to a process by declaration. It is an object of
a law-relative solution groupoid:

$$
\boxed{
\text{represented quantum process law}
\longmapsto
\text{complete groupoid of W3-positive record questions}.
}
$$

The record question remains genuinely quantum. The same packet contains a
preserving continuation whose stochastic shadow composes classically and an
erasing continuation with a nonzero cross-record coherence term. Passing to
the seam moduli does not replace those amplitudes by a Boolean stochastic
model.

The branch-memory theorem is ontologically instructive. The process does not
select one unique “memory location.” It supports nine exact atomic seams under
the declared experiment grammar. The familiar memory decomposition is one
member. The correct object is therefore a family with symmetry and
stabilizers, not a hidden classical partition waiting to be read off.

This result still does not say that any seam is *where* something is in space.
It reconstructs stable record interfaces. Spatial locality would require a
stronger autonomous-process referent and physical overlap maps, neither of
which appears here.

---

## 17. Limits and first unresolved obstruction

### 17.1 Actuality remains separate

For the branch-memory preparation $|00\rangle$, the written state is

$$
\frac{|00\rangle+|11\rangle}{\sqrt2}.
$$

The seam equations identify sharp record propositions and their possible
preservation. They do not select one projector atom as true. Any actuality
claim requires a separate ontological postulate or theorem.

### 17.2 Law-relative admission remains input

The represented theory decides which projectors, controls, continuations, and
instruments are admitted. This paper proves invariance under strong
equivalence of that complete law. It does not derive the operational law from
one realized trajectory.

### 17.3 Coarse-graining is not autonomy

A UCP idempotent can be executable and repeatable without enabling arbitrary
preparation, control, or readout of its fixed operator system. The next
possible analytical strengthening would require autonomous W3 subtheories
with separating preparations and effects, nontrivial internal controls, and
encoding/decoding maps. It is not attempted here.

### 17.4 Physical overlap remains absent

No pair or triple intersection of independently reconstructed seam-supported
subtheories is constructed. Commuting idempotents may later supply one narrow
overlap control, but noncommuting maps cannot be forced into set intersection.

The first unresolved obstruction is therefore:

> Can a reconstructed W3 seam be promoted from a repeatably
> coarse-grainable record interface to an autonomous quantum process chart,
> with physical maps and pullbacks derived independently of support labels?

This question is not authorized in the present cycle.

---

## 18. Explicit nonclaims

This paper does not establish:

- a selected actual outcome;
- historical occurrence or present availability as an interpretation-
  independent truth assignment;
- W6 fact co-reference or event-token identity;
- autonomous subsystem control;
- a tensor factor or spatial boundary;
- generic physical overlap or a process cover;
- an intrinsic spatial localization;
- a topological space or manifold;
- operational influence or causal order;
- dimension, volume, or Lorentzian geometry;
- scalar, Dirac, Maxwell, or other quantum fields; or
- gravity or backreaction.

The rejected quantaloid/Isbell/Weld-stack headline is not restored.

---

## 19. Conclusion

The selected-PVM problem has a finite, exact answer at the declared scope:
make the fine and coarse commutative algebras variables, impose W3 directly on
the represented process law, and retain the entire solution groupoid.

For one branch-memory packet, this does more than recover the expected record.
It proves that the expected record is not unique: nine atomic seams satisfy
the same exact W3 mechanism. Presentation changes do not alter that family,
while genuinely different counterfactual continuation laws may.

Every reconstructed seam inherits a total unsharp-evidence interface, a
zero-defect sharp-proposition interface, and a category of admitted repeatable
coarse-grainings. Those categories form a fibration over the seam moduli.

The result is a stronger quantum factual foundation, not a space. It makes the
remaining task sharper: before topology or causality, stable record interfaces
must become autonomous quantum process charts with physically derived
overlaps.

---

## References

1. E. B. Davies and J. T. Lewis, “An operational approach to quantum
   probability,” *Communications in Mathematical Physics* **17** (1970),
   239--260. Outcome probabilities together with state transformations.
2. M. Ozawa, “Quantum measuring processes of continuous observables,”
   *Journal of Mathematical Physics* **25** (1984), 79--87. Quantum
   instruments and measurement disturbance.
3. W. F. Stinespring, “Positive functions on C*-algebras,” *Proceedings of
   the American Mathematical Society* **6** (1955), 211--216. Dilations of
   completely positive maps.
4. K. Kraus, “General state changes in quantum theory,” *Annals of Physics*
   **64** (1971), 311--335. Operator-sum representations of quantum
   operations.
5. M. A. Naimark, “On a representation of additive operator set functions,”
   *Doklady Akademii Nauk SSSR* **41** (1943), 359--361. Projection-valued
   dilation of positive operator measures.
6. M.-D. Choi, “A Schwarz inequality for positive linear maps on
   C*-algebras,” *Illinois Journal of Mathematics* **18** (1974), 565--574.
   Schwarz inequality and multiplicative behavior of completely positive
   maps.
7. M.-D. Choi, N. Johnston and D. W. Kribs, “The multiplicative domain in
   quantum error correction,” *Journal of Physics A: Mathematical and
   Theoretical* **42** (2009), 245303; arXiv:0811.0947.
8. M.-D. Choi and E. G. Effros, “Injectivity and operator spaces,” *Journal
   of Functional Analysis* **24** (1977), 156--209. Completely positive
   projections and their range product.
9. C. Heunen, A. Kissinger and P. Selinger, “Completely positive projections
   and biproducts,” *Electronic Proceedings in Theoretical Computer Science*
   **171** (2014), 71--83; arXiv:1308.4557. Splitting completely positive
   idempotents.
10. C. Heunen and B. Lindenhovius, “Domains of commutative C*-subalgebras,”
    *Mathematical Structures in Computer Science* **29** (2019), 972--1006;
    arXiv:1504.02730. Commutative subalgebras and Boolean projection
    structure.
11. K. Behrend and P. Xu, “Differentiable stacks and gerbes,”
    arXiv:math/0605694. Lie groupoids and retained-stabilizer stack
    presentations; used here only as comparison language.
12. F. Loregian and E. Riehl, “Categorical notions of fibration,”
    *Expositiones Mathematicae* **38** (2020), 496--514;
    arXiv:1806.06129. Grothendieck fibrations and pseudofunctors.
13. J.-P. Pellonpää, S. Designolle and R. Uola, “Naimark dilations of qubit
    POVMs and joint measurements,” *Journal of Physics A: Mathematical and
    Theoretical* **56** (2023), 155303; arXiv:2208.13588. Minimal Naimark
    dilation as a finite measurement-analysis tool.
