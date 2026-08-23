# ISP v17 — U-Gen U0-T3 reference-bearing relational theorems

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Candidate, implementation, or target data bound:** no

This file proves the exact positive complement to the U0-T3 bare-carrier
theorem. A physical reference can make relational distinctions available
without introducing an absolute label or breaking covariance of the complete
law. The result is kinematic and source-theoretic. It neither selects the
reference structure nor constructs the native indivisible stochastic law.

The general result uses only measurable spaces and ordinary-positive kernels.
Finite and compact group controls are included for exactness. They do not
assert fundamental discreteness, continuity, group structure, spacetime,
external time, $U(1)$, complex amplitude, action, bundle, or holonomy.

---

## 0. Why this theorem is needed

The preceding bare-carrier theorem shows that an anonymous finite carrier
with full relabeling covariance supports only equality-pattern distinctions.
That is not enough to model a structured laboratory.

There are two bad reactions:

1. install a preferred coordinate, lattice, order, or phase convention as an
   absolute background; or
2. demand complete permutation invariance after erasing every physical
   standard, thereby making nontrivial prediction impossible by construction.

The correct middle is a **physical reference**: another transformable,
readable, contingent, resource-bounded constituent. Absolute descriptions
remain gauge or presentation; relative configurations can remain physical.

---

## 1. Measurable reference-bearing source object

Let $G$ be a group acting bimeasurably on two measurable spaces

$$
(X,\Sigma_X),
\qquad
(R,\Sigma_R).
\tag{1}
$$

$X$ is a bounded control for system configurations and $R$ for reference
configurations. The same $g\in G$ acts diagonally by

$$
g\cdot(x,r)=(g\cdot x,g\cdot r).
\tag{2}
$$

The orbit map is

$$
q:X\times R\longrightarrow Q\equiv(X\times R)/G,
\qquad
q(x,r)=[x,r].
\tag{3}
$$

Equip $Q$ with the quotient sigma-algebra

$$
\Sigma_Q=
\{A\subseteq Q:q^{-1}(A)\in\Sigma_X\otimes\Sigma_R\}.
\tag{4}
$$

Let $(Y,\Sigma_Y)$ be a registered relative-record space. A complete-record
kernel

$$
K:X\times R\rightsquigarrow Y
\tag{5}
$$

is **diagonally invariant** when

$$
K(g\cdot x,g\cdot r;B)=K(x,r;B)
\quad
\forall g\in G,\ x\in X,\ r\in R,\ B\in\Sigma_Y.
\tag{6}
$$

This treats $Y$ as already written in invariant record language. If records
also transform, (6) is replaced by the source-descent pushforward equation;
the same argument applies after record alignment.

---

## 2. Diagonal-orbit factorization

### Theorem RB.A — invariant predictions are functions of relative orbits

A kernel $K$ satisfies (6) if and only if there exists a unique kernel

$$
\bar K:Q\rightsquigarrow Y
\tag{7}
$$

such that

$$
K(x,r;B)=\bar K(q(x,r);B)
\quad
\forall x,r,B.
\tag{8}
$$

### Proof

If $K$ is invariant, define

$$
\bar K([x,r];B)=K(x,r;B).
\tag{9}
$$

This is well defined because two representatives of one orbit differ by the
diagonal action and therefore give the same value by (6). For fixed $B$, the
map $(x,r)\mapsto K(x,r;B)$ is measurable and invariant. By the definition of
the quotient sigma-algebra, its factor through $q$ is measurable. For fixed
$[x,r]$, normalization and countable additivity follow from those of
$K(x,r;\cdot)$. Uniqueness follows because $q$ is surjective.

Conversely, any kernel of the form (8) is constant on diagonal orbits and
therefore satisfies (6). $\square$

### Meaning

Covariance does not require the prediction to be structureless. It requires
the prediction to depend on the **joint orbit**, not on an absolute
representative. If $Q$ has nontrivial measurable distinctions, relational
response is possible.

The theorem does not say that every physically meaningful relation is a group
orbit. Groupoids, partial transformations, operational comparisons, and
noninvertible controls remain possible. Equation (8) is an exact control, not
a universal ontology.

---

## 3. Exact regular-action control

Let $G$ now be a finite group and let

$$
X=R=G
\tag{10}
$$

with the regular left action. Define

$$
z(x,r)=r^{-1}x.
\tag{11}
$$

### Theorem RB.B — the relative element classifies diagonal orbits

For all $g,x,r\in G$,

$$
z(gx,gr)=z(x,r).
\tag{12}
$$

Moreover,

$$
z(x,r)=z(y,s)
$$

if and only if $(x,r)$ and $(y,s)$ lie on the same diagonal orbit. Hence every
invariant kernel has the exact form

$$
K(x,r;B)=\kappa(r^{-1}x;B)
\tag{13}
$$

for a unique kernel $\kappa:G\rightsquigarrow Y$.

### Proof

Equation (12) follows from

$$
(gr)^{-1}(gx)=r^{-1}x.
$$

If $r^{-1}x=s^{-1}y$, choose $g=sr^{-1}$. Then $gr=s$ and
$gx=sr^{-1}x=y$. The converse follows from (12). The kernel statement follows
from Theorem RB.A. $\square$

### Cyclic illustration only

For $G=\mathbb Z_n$, the invariant is $x-r\pmod n$. This shows, on a finite
control, how a nontrivial relative orientation can exist with no preferred
absolute label. It does not imply a cyclic microscopic world, a lattice, a
clock, or discreteness.

---

## 4. Symmetric law with asymmetric relative state

Let $\nu$ be any probability distribution on a finite group $G$. Define a
joint ordinary-positive law

$$
P_\nu(x,r)
=
\frac{1}{|G|}\nu(r^{-1}x).
\tag{14}
$$

### Theorem RB.C — full covariance permits arbitrary relative distributions

$P_\nu$ is normalized and invariant under the diagonal left action. Both
absolute marginals are uniform,

$$
P_\nu(X=x)=P_\nu(R=r)=\frac1{|G|},
\tag{15}
$$

while the relative variable $Z=R^{-1}X$ has exactly the law

$$
P_\nu(Z=z)=\nu(z).
\tag{16}
$$

### Proof

For every fixed $r$, the map $x\mapsto r^{-1}x$ is a bijection, so (14) sums
to one over $x,r$. Diagonal invariance follows from (12). The $R$ marginal is
$1/|G|$ by summing $\nu$ over $x$. For fixed $x$, the map
$r\mapsto r^{-1}x$ is a bijection, giving the same $X$ marginal. Finally,
$X=RZ$, so summing (14) over the $|G|$ possible values of $R$ gives (16).
$\square$

### Physical meaning

An ensemble can contain a sharp or biased **relative** condition without a
preferred absolute orientation. Thus:

$$
\text{covariant nomology}
\not\Rightarrow
\text{relationally symmetric contingent state}.
$$

The reference state or system--reference correlation must still be prepared
and costed. Equation (14) does not explain where $\nu$ comes from.

---

## 5. Reference nonselection

### Theorem RB.D — a reference exposes variables but does not select dynamics

If $|G|\ge2$, the family

$$
\{P_\nu:\nu\in\mathcal P(G)\}
\tag{17}
$$

contains multiple distinct normalized, diagonally invariant joint laws with
the same uniform absolute marginals. Therefore covariance, normalization, the
carrier, and the presence of the reference do not uniquely select the
relative law $\nu$.

### Proof

Choose $\nu_1\ne\nu_2$. Equations (14)--(16) show that $P_{\nu_1}$ and
$P_{\nu_2}$ satisfy all stated common conditions but have different relative
predictions. $\square$

### U0 consequence

The reference-bearing construction defeats the false inference

$$
\text{covariance}\Rightarrow\text{structureless law},
$$

but proves no converse selection principle. The native U0 burden becomes:

> Which independently motivated physical rule, if any, fixes the complete
> response on relational source objects across held-out experiments?

Supplying $\nu$, $\kappa$, a quantum action, or a process matrix is not an
answer.

---

## 6. Reference removal and ordinary twirling

Let $G$ be finite or compact with normalized Haar probability $\lambda$, let
$X$ carry a measurable $G$-action, and take $R=G$ with the regular left
action. Let $K:X\times G\rightsquigarrow Y$ satisfy (6). If the reference is
unobserved and distributed according to $\lambda$, define

$$
K_{\rm lost}(x;B)
=
\int_G K(x,r;B)\,\lambda(dr).
\tag{18}
$$

### Theorem RB.E — losing an invariantly distributed reference erases orbit position

For every $g\in G$,

$$
K_{\rm lost}(g\cdot x;B)=K_{\rm lost}(x;B).
\tag{19}
$$

If the action on $X$ is transitive, $K_{\rm lost}$ is independent of $x$.

### Proof

By left invariance of Haar measure, substitute $r=g\cdot s$ in (18):

$$
\begin{aligned}
K_{\rm lost}(g\cdot x;B)
&=\int_G K(g\cdot x,r;B)\,\lambda(dr)\\
&=\int_G K(g\cdot x,g\cdot s;B)\,\lambda(ds)\\
&=\int_G K(x,s;B)\,\lambda(ds).
\end{aligned}
$$

The last equality uses diagonal invariance. Transitivity then equates every
pair of $x$ values. $\square$

### Scope

This is an ordinary-probability statement. It is the representation-neutral
core of the reference-averaging control often called twirling in quantum
information. It does not derive quantum decoherence, a superselection rule,
or a Hilbert representation.

A nonuniform, retained, or correlated reference need not obey (19). Therefore
one must not average away a real reference and then call the lost information
gauge.

---

## 7. Shared-reference correlation control

Let $R$ be a physical reference with law $\mu$. Suppose systems $A$ and $B$
are conditionally independent given $R$:

$$
P(a,b,r)=\mu(r)K_A(a\mid r)K_B(b\mid r).
\tag{20}
$$

### Theorem RB.F — marginal correlation does not prove interaction

The marginal

$$
P(a,b)=\int K_A(a\mid r)K_B(b\mid r)\,\mu(dr)
\tag{21}
$$

need not factor as $P(a)P(b)$.

### Proof by exact binary control

Let $R$ be a fair bit and set $A=R$, $B=R$ deterministically. Then $A$ and
$B$ are conditionally independent given $R$, but

$$
P(A=B)=1,
\qquad
P(A=0)=P(B=0)=\frac12.
$$

Thus the marginal is perfectly correlated and not a product. $\square$

### Consequence

Common-reference, common-source, interaction, communication, and genuinely
indivisible joint dynamics require separate fixture members. Shared-reference
correlation must not be renamed entanglement or nonlocality. Conversely, a
candidate may not discard a real shared reference and then claim unexplained
correlation.

---

## 8. Advice-embedding control

Physical embodiment alone does not prevent target smuggling.

### Lemma RB.G — a distinguishable reference token can carry a target index

Let $\{Q_1,\ldots,Q_M\}$ be a finite target family. If a reference packet has
$M$ perfectly distinguishable prepared cells $R_1,\ldots,R_M$, then the rule

$$
r\in R_j\longmapsto Q_j
\tag{22}
$$

encodes the complete target index in the reference.

### Proof

The cell reader recovers $j$ with certainty, after which the lookup returns
$Q_j$. $\square$

### Consequence

A laser, clock, crystal, field setting, calibration file, or material token is
not automatically an explanatory primitive merely because it is physical.
U0-T2 still requires a nontrivial calibration fiber: the joint source packet
must leave multiple held-out complete processes possible before the proposed
nomological rule acts.

---

## 9. Reference-bearing complete-process contract

A future native candidate may use reference structure only by extending its
complete source map to

$$
\mathcal N:
(S,R,\sigma_{SR},b,c,\mathsf{Compare},\mathsf{Read})
\longmapsto
\Gamma^{\mathcal N}_{SR,b,c},
\tag{23}
$$

with all of the following frozen before target opening:

1. the joint measurable configuration object;
2. neutral presentation transformations;
3. active system and reference interventions;
4. preparation and provenance of $\sigma_{SR}$;
5. comparison and reader operations;
6. complete retained records;
7. independent, shared-reference, and interacting composition;
8. genuine divisions and nondivisions;
9. reference removal, drift, degradation, and replacement;
10. no-refit transfer; and
11. reference precision, capacity, communication, and refresh cost.

Equation (23) allows whole-program indivisibility. No reference reading is
automatically a future-sufficient cut, and no sequence of apparatus commands
is promoted to fundamental time.

---

## 10. Primitive-admission firewall

A relational primitive $\rho$ is admissible only if it passes:

$$
\begin{array}{ll}
\text{P1} & \text{target-blind physical preparation or comparison};\\
\text{P2} & \text{verified joint presentation descent};\\
\text{P3} & \text{typed active transformation law};\\
\text{P4} & \text{reader and retained-record meaning};\\
\text{P5} & \text{non-equivalent-input / calibration-fiber test};\\
\text{P6} & \text{provenance and no-refit transfer};\\
\text{P7} & \text{finite precision and resource accounting};\\
\text{P8} & \text{reference removal and common-source controls};\\
\text{P9} & \text{no ontology promotion from the fixture};\\
\text{P10}& \text{no clock, spacetime, or gravity inference}.
\end{array}
\tag{24}
$$

Failure of P1--P8 makes the primitive either an ungrounded background or an
advice channel. Passing all ten makes it an admissible source coordinate, not
a selected law.

---

## 11. Hostile controls

1. preferred coordinate disguised as a reference;
2. target process table stored in a physical token;
3. uncosted infinite-precision reference;
4. reference condition selected after target opening;
5. active transformation confused with passive relabeling;
6. physical reference averaged away as gauge;
7. gauge label treated as a physical standard;
8. asymmetric state reported as an asymmetric law;
9. covariant law reported as unique;
10. shared-reference correlation reported as interaction;
11. interaction reported as mere shared reference;
12. reader coupling omitted from the parent configuration;
13. reference measurement declared a division without sufficiency;
14. apparatus sequence declared fundamental time;
15. finite group control promoted to discreteness;
16. group quotient promoted to spacetime geometry;
17. relative group element promoted to $U(1)$ phase;
18. quantum twirling theorem promoted to native positive dynamics;
19. a no-refit implementation allowed a new calibration convention;
20. reference capacity omitted from the resource ledger; and
21. gravity used to choose the unfinished matter law.

---

## 12. Present theorem verdict

```text
BARE CARRIER:                         DYNAMICALLY UNDERDETERMINED
PHYSICAL REFERENCE:                   LEGITIMATE RELATIONAL SOURCE CLASS
JOINT PRESENTATION COVARIANCE:        COMPATIBLE WITH NONTRIVIAL RELATION
ABSOLUTE ORIENTATION:                 NOT REQUIRED
RELATIVE-ORBIT FACTORIZATION:         PROVED
FINITE REGULAR-ACTION CLASSIFIER:     PROVED / CONTROL ONLY
RELATIVE ASYMMETRY WITH UNIFORM
  ABSOLUTE MARGINALS:                 PROVED / CONTROL ONLY
REFERENCE REMOVAL INVARIANCE:         PROVED AT FINITE/COMPACT SCOPE
SHARED-REFERENCE CORRELATION:         PROVED / NOT INTERACTION
REFERENCE AS UNIQUE LAW SELECTOR:     REFUTED IN EXACT FINITE CONTROL
REFERENCE AS ADVICE CHANNEL:          EXACT RISK / T2 REQUIRED
QUANTUM COMPLETE-PROCESS GENERATION:  NOT CONSTRUCTED
CONFIGURATION ONTOLOGY:               UNSELECTED
IMPLEMENTATION / TARGET:              UNBOUND
PIN / REVIEW / RESULT:                NONE
```

---

## 13. What this changes in U0

The bare-carrier theorem did not imply that configuration ontology must be
structureless. This theorem now shows exactly how one class of structure can
enter honestly:

$$
\text{physical system}
+
\text{physical reference}
\longrightarrow
\text{relative source object},
$$

while

$$
\text{simultaneous presentation change}
\longrightarrow
\text{same complete prediction}.
$$

This is progress in the source contract, not in the quantum prediction. The
central missing object remains one uniform rule that maps independently
specified relational source objects to held-out complete quantum processes
without receiving those processes in the source packet.

---

## 14. Authority wall

This theorem does not authorize:

1. choosing a group, reference system, configuration space, or native law;
2. binding an apparatus or target data set;
3. importing $U(1)$, phase, action, bundle, holonomy, trajectories, Brownian
   noise, Markov divisibility, external time, or Hilbert ontology;
4. U0-T4, an official pin, independent review, or scientific result;
5. an N1B, G1 successor, clock, QFT, spacetime, or gravity model; or
6. a successor paper or repair chain.

---

## 15. Maximum legitimate claim

> Ordinary-positive relational response and exact presentation covariance are
> mathematically compatible when a reference is included as a physical,
> contingent, and costed constituent. Invariant predictions factor through
> joint system--reference orbits, not through absolute labels. Exact finite
> controls show both that relative asymmetry can survive with uniform absolute
> marginals and that the reference does not select the relative law. Losing a
> uniformly unknown reference erases orbit position, while sharing one can
> create ordinary common-source correlations. These results identify an
> admissible source architecture and its anti-smuggling tests; they do not
> generate or select the native indivisible quantum law.
