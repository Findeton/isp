# Sharp Facts and Unsharp Evidence

## W3 Record Transport under Quantum Channels

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-07-31

**Governing pin:** `e994807`

**Inherited result:** `RQ0-L0-REPRESENTABLE-W3-SKETCH`

**Provisional highest result:** `RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM`

**Strict scope:** finite-dimensional, law-relative quantum record transport;
no intrinsic localization, overlap, topology, causality, spacetime, fields or
gravity

---

## Abstract

A stable quantum record is sharp at its native W3 seam: its alternatives are
represented by a projection-valued measure, occurrence is certified by a
record-writing amplitude process, and availability is tested against declared
continuations. A general quantum channel does not preserve that sharp logic.
It maps the record PVM to a POVM whose effects may be unsharp. We separate the
two physical roles that were previously compressed into one Boolean record
interface.

Every admitted unital completely positive Heisenberg map transports effects,
POVMs, and, when outcome maps are supplied, full quantum instruments. This
defines a total law-relative evidence interface. We introduce the record
multiplicativity defect

$$
\Delta_F^{\mathrm{rec}}(a,b)=F(ab)-F(a)F(b)
$$

and its positive sharpness specialization

$$
\Sigma_F(a)=F(a^2)-F(a)^2.
$$

They obey an exact composition chain law. For a finite record algebra, zero
defect is equivalent to multiplicative-domain membership, homomorphic
transport, and preservation of every record projector. This produces a
partial sharp Boolean interface inside the total effect-valued interface.
Sharp transport remains necessary but not sufficient for identity of the same
physical fact or occurrence token.

The least directly generated observability object is an operator system, not
an automatically physical C*-algebra. To type addressability, we form the
Karoubi completion of the category of *admitted* UCP maps. An admitted UCP
idempotent whose fixed operator system contains the record-observability
system is a law-relative addressability certificate. Abstract conditional
expectations that the physical grammar does not admit are excluded. Exact
unitary, bit-flip, dephasing, random-unitary, amplitude-damping, noisy-chain,
branch-memory, instrument-disturbance, declared-overlap, spectator,
idempotent, symmetry and global controls are derived by hand.

The result repairs the logical and map typing exposed by the rejected Weld
stack, but it does not repair that stack. Selected boundaries, record
projectors, instruments and transport grammars remain inputs. The result is
therefore law-relative record transport and addressability, not intrinsic
quantum localization.

---

## 1. Question, result, and non-claim

The physical question is:

> Given a sharp record produced and tested inside one quantum process, what
> becomes of that record when it is viewed through an arbitrary admitted
> quantum channel?

There are two different answers.

1. The channel always transports **evidence**. A sharp outcome projector
   becomes an effect, and a PVM becomes a POVM.
2. The channel transports the **sharp proposition exactly** only when it is
   multiplicative on the record algebra.

This distinction is the organizing result:

$$
\boxed{
\begin{array}{c}
\text{all admitted UCP maps}
\longrightarrow
\text{effect/POVM-valued evidence},\\[1mm]
\text{record-multiplicative admitted maps}
\longrightarrow
\text{sharp Boolean proposition transport}.
\end{array}}
$$

The paper establishes three cumulative finite-dimensional layers:

$$
\begin{array}{ll}
\texttt{RQ0-L0-W3-EFFECT-TRANSPORT}
&\text{total effect, POVM and instrument-shadow transport};\\
\texttt{RQ0-L0-SHARP-FACT-TRANSPORT}
&\text{zero-defect sharp Boolean transport};\\
\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}
&\text{law-relative addressability by admitted UCP idempotents}.
\end{array}
$$

The word *fact* in the second label is deliberately narrow. It means that a
sharp proposition is transported homomorphically. It does not mean that two
record tokens are the same occurrence, or even that they refer to the same
historical fact. W6 co-reference still requires an independent physical
bridge.

No object in this paper is a spatial region. No causal relation, overlap
topology, Lorentzian structure, field or gravitational response is defined.
The rejected quantaloid, Isbell, quotient-stack and generic-overlap headlines
are not restored.

### 1.1 Claim vocabulary

We use the following grades.

- A **definition** fixes a mathematical type.
- A **declared law input** is physically meaningful data supplied by the
  process theory but not derived here.
- A **theorem** follows at the stated finite-dimensional scope.
- A **construction** exhibits an exact object satisfying a definition.
- A **control** separates two claims on a small exact model.
- An **interpretation** states physical meaning but is not a theorem.
- An **open obligation** marks what would be needed for intrinsic
  localization or later physics.

---

## 2. Finite operational setting and the W3 input

### Definition 2.1 — observable algebras and channel convention

Every boundary $x$ carries a finite-dimensional unital C*-algebra
$\mathfrak B_x$. A physical Schrödinger channel from boundary $x$ to boundary
$y$ is represented in this paper by its Heisenberg adjoint

$$
F:\mathfrak B_y\longrightarrow\mathfrak B_x.
$$

Thus displayed Heisenberg arrows run opposite to physical state evolution.
We write

$$
G:C\to B,
\qquad
F:B\to A,
\qquad
F\circ G:C\to A.
$$

Every such map is linear, unital and completely positive (UCP). Let
$\mathsf{Chan}_D$ be a category whose objects are the declared boundary
algebras and whose arrows are the physically admitted UCP maps. Identities
and composites are admitted. The subscript $D$ emphasizes that admission is
part of one process law. An abstractly existing UCP map is not thereby an
arrow of $\mathsf{Chan}_D$.

### Definition 2.2 — internal finite W3 record

An internal W3 record diagram $W$ supplies, as actual process data:

1. a preparation family;
2. a record-writing process;
3. a record-preserving continuation family;
4. a coherent erasing continuation family;
5. a no-write control;
6. accessible probes; and
7. a finite record PVM at the record boundary $x_W$,

$$
\mathbf P=(P_r)_{r\in\Omega},
\qquad
P_rP_s=\delta_{rs}P_r,
\qquad
\sum_{r\in\Omega}P_r=I.
$$

The W3 amplitude criteria independently establish correlation at writing and
continuation-relative availability. They are not redefined by the channel
logic below. The finite commutative record algebra is

$$
R_W=C^*(P_r:r\in\Omega).
$$

This paper inherits the exact branch-memory W3 construction and reconstructs
it in Section 10. The choice of $W$, its native boundary and its record PVM
are declared law inputs. Deriving them without selected cuts or projector
packages remains open.

### Definition 2.3 — presentation gauge

A unitary presentation change consists of *-automorphisms

$$
\alpha_A=\operatorname{Ad}_{U_A},
\qquad
\alpha_B=\operatorname{Ad}_{U_B}
$$

and replaces $F:B\to A$ by

$$
F'=\alpha_A\circ F\circ\alpha_B^{-1}.
$$

The PVM is replaced by $P'_r=\alpha_B(P_r)$. Record-handle renaming is a
bijection of $\Omega$ and changes no operator. These are presentation
changes, not new physical channels.

---

## 3. Effects and the total evidence interface

### Definition 3.1 — effects

For a finite-dimensional unital C*-algebra $A$, define

$$
\operatorname{Eff}(A)
=
\{a\in A_{\mathrm{sa}}:0\le a\le I_A\}.
$$

Effects have orthocomplement $a^\perp=I-a$. A finite partial sum
$a_1\mathbin{\oplus}\cdots\mathbin{\oplus}a_n$ is defined exactly when
$\sum_i a_i\le I$. With scalar multiplication by $[0,1]$, this is the usual
effect-module structure.

### Theorem 3.2 — UCP effect transport

Every UCP map $F:B\to A$ restricts to an effect-module morphism

$$
\operatorname{Eff}(F):\operatorname{Eff}(B)
\longrightarrow
\operatorname{Eff}(A).
$$

It preserves zero, unit, orthocomplement, scalar multiplication and every
defined finite partial sum. These restrictions preserve identities and
composition exactly.

*Proof.* If $0\le a\le I_B$, positivity gives $F(a)\ge0$ and
$F(I_B-a)\ge0$. Unitality gives $F(I_B-a)=I_A-F(a)$, so
$0\le F(a)\le I_A$. Linearity gives

$$
F(0)=0,
\quad
F(I_B)=I_A,
\quad
F(I_B-a)=I_A-F(a),
\quad
F(ta)=tF(a).
$$

If $\sum_i a_i\le I_B$, positivity and linearity give
$\sum_iF(a_i)=F(\sum_i a_i)\le I_A$. Finally,
$\operatorname{Eff}(\operatorname{id})=\operatorname{id}$ and restriction
commutes with ordinary channel composition. Complete positivity is stronger
than needed for this theorem, but is required by the quantum channel category
and later Schwarz arguments. $\square$

### Definition 3.3 — finite POVMs

For a finite outcome set $\Omega$, let

$$
\operatorname{POVM}_\Omega(A)
=
\left\{(E_r)_{r\in\Omega}:
E_r\in\operatorname{Eff}(A),\ \sum_rE_r=I_A\right\}.
$$

A POVM is a PVM exactly when every $E_r$ is a projection. In that case the
normalization implies pairwise orthogonality.

### Theorem 3.4 — every W3 PVM transports to a POVM

For every UCP $F:B\to A$ and every finite PVM $\mathbf P=(P_r)$ in $B$,

$$
F_\Omega(\mathbf P)=(F(P_r))_{r\in\Omega}
$$

is a POVM in $A$.

*Proof.* Theorem 3.2 makes every $F(P_r)$ an effect, and

$$
\sum_rF(P_r)=F\!\left(\sum_rP_r\right)=F(I_B)=I_A.
\qquad\square
$$

No idempotence follows from this calculation.

### Definition 3.5 — the total POVM functor

For fixed $\Omega$, define

$$
\operatorname{POVM}_\Omega:
\mathsf{Chan}_D\longrightarrow\mathbf{Set}
$$

by

$$
A\longmapsto\operatorname{POVM}_\Omega(A),
\qquad
(F:B\to A)\longmapsto
\left[(E_r)\mapsto(F(E_r))\right].
$$

Theorem 3.4 and exact composition make this a functor in the displayed
Heisenberg direction. Relative to the corresponding Schrödinger process, it
is contravariant.

To retain the varying carrier algebra, let
$\mathsf{POVMIfc}_\Omega(D)$ be the category whose objects are pairs
$(A,\mathbf E)$ with
$\mathbf E\in\operatorname{POVM}_\Omega(A)$, and whose arrows

$$
h:(A,\mathbf E)\longrightarrow(A',\mathbf E')
$$

are admitted UCP maps $h:A\to A'$ satisfying
$h(E_r)=E'_r$ for every outcome. This is the category of elements of the
displayed POVM functor; identity and composition are inherited exactly.

For one W3 record $W$, let $(B_W\downarrow\mathsf{Chan}_D)$ be the
undercategory of admitted transports out of its native algebra. An object is
$F:B_W\to A$; an arrow from $F$ to $F'$ is an admitted $h:A\to A'$ with
$h\circ F=F'$. Define

$$
\operatorname{Rec}_{\mathrm{eff}}^W:
(B_W\downarrow\mathsf{Chan}_D)
\longrightarrow
\mathsf{POVMIfc}_\Omega(D),
$$

$$
\operatorname{Rec}_{\mathrm{eff}}^W(F:B_W\to A)
=
\bigl(A,(F(P_r))_{r\in\Omega}\bigr).
$$

On $h$ it acts by effect transport. The triangle equation gives

$$
h\bigl(\operatorname{Rec}_{\mathrm{eff}}^W(F)\bigr)
=
\operatorname{Rec}_{\mathrm{eff}}^W(F').
$$

Thus `Rec_eff` is a total, handle-independent, law-relative evidence
interface on every admitted transport of the chosen W3 record.

### Proposition 3.6 — gauge covariance and handle invariance

Under Definition 2.3,

$$
F'(P'_r)=\alpha_A(F(P_r)).
$$

Hence gauge-related presentations give unitarily isomorphic POVMs. A
bijection $\sigma:\Omega\to\Omega'$ merely reindexes the same family:
$E'_{\sigma(r)}=E_r$. Neither the functor nor any theorem below reads a record
handle.

### Interpretation 3.7 — evidence is not identity

The numbers

$$
\Pr(r\mid\rho)=\operatorname{Tr}(\rho F(P_r))
$$

are quantitative evidence associated with the native record proposition.
They do not by themselves establish that a new token exists, that the old
record remains currently available, or that two equal outcome laws concern
the same fact. Those are dynamical and co-reference questions.

---

## 4. Instruments above their POVM shadows

### Definition 4.1 — finite quantum instrument

Let $\mathcal T(H)$ denote trace-class operators on a finite-dimensional
Hilbert space. A Schrödinger instrument from input $H_A$ to output $H_B$ with
outcomes $\Omega$ is a family

$$
\mathcal I=(\mathcal I_r)_{r\in\Omega},
\qquad
\mathcal I_r:\mathcal T(H_A)\to\mathcal T(H_B),
$$

of completely positive trace-nonincreasing maps such that
$\sum_r\mathcal I_r$ is trace preserving. Its Heisenberg effects are

$$
E_r=\mathcal I_r^*(I_B)\in\mathfrak B(H_A).
$$

The outcome probability on input state $\rho$ is
$\operatorname{Tr}(\mathcal I_r(\rho))=\operatorname{Tr}(\rho E_r)$.
When nonzero, the normalized state
$\mathcal I_r(\rho)/\operatorname{Tr}(\mathcal I_r(\rho))$ records the
outcome-conditioned disturbance.

### Theorem 4.2 — instrument transport and logical shadow

The effects of every instrument form a POVM. If

$$
\Lambda:\mathcal T(H_C)\to\mathcal T(H_A)
$$

is a CPTP channel, then

$$
(\mathcal I\circ\Lambda)_r=\mathcal I_r\circ\Lambda
$$

is an instrument from $H_C$ to $H_B$, with effects

$$
E_r^{\mathcal I\circ\Lambda}=\Lambda^*(E_r^{\mathcal I}).
$$

Both operations compose exactly.

*Proof.* Complete positivity and trace nonincrease are closed under
composition. The sum is

$$
\sum_r\mathcal I_r\circ\Lambda
=
\left(\sum_r\mathcal I_r\right)\circ\Lambda,
$$

which is CPTP. Moreover,

$$
(\mathcal I_r\circ\Lambda)^*(I_B)
=
\Lambda^*(\mathcal I_r^*(I_B)).
$$

Functoriality follows from associativity. $\square$

### Proposition 4.3 — a POVM does not determine an instrument

Let $P_0=|0\rangle\langle0|$, $P_1=|1\rangle\langle1|$ and
$P_+=|+\rangle\langle+|$. Define

$$
\mathcal L_r(\rho)=P_r\rho P_r,
\qquad
\mathcal J_r(\rho)=\operatorname{Tr}(P_r\rho)P_+.
$$

Both are instruments with effects $P_r$, but they are not the same
instrument. On input $P_0$ and outcome $0$,

$$
\mathcal L_0(P_0)=P_0,
\qquad
\mathcal J_0(P_0)=P_+.
$$

Therefore equal effects and equal outcome probabilities do not determine the
continuation dynamics.

### Interpretation 4.4 — the three-level interface

Whenever the W3 process supplies outcome maps, the primary transported object
is the instrument. Its POVM is the quantitative logical shadow. Only when the
POVM is sharp and the channel is record-multiplicative does a Boolean
interface exist:

$$
\boxed{
\text{record instrument}
\longrightarrow
\text{effect/POVM interface}
\longrightarrow
\text{sharp Boolean interface when eligible}.}
$$

A bare PVM or POVM does not select a unique instrument.

---

## 5. Record defects and their composition law

### Definition 5.1 — record multiplicativity defect

For UCP $F:B\to A$, define

$$
\Delta_F^{\mathrm{rec}}(a,b)
=
F(ab)-F(a)F(b),
\qquad a,b\in B.
$$

For self-adjoint $a$, define the sharpness defect

$$
\Sigma_F(a)
=
\Delta_F^{\mathrm{rec}}(a,a)
=
F(a^2)-F(a)^2.
$$

For a projector $P$, this becomes

$$
\Sigma_F(P)=F(P)-F(P)^2.
$$

### Theorem 5.2 — positivity and exact sharpness criterion

For self-adjoint $a$, $\Sigma_F(a)\ge0$. For a projection $P$,

$$
\Sigma_F(P)=0
\quad\Longleftrightarrow\quad
F(P)\text{ is a projection}.
$$

*Proof.* Kadison--Schwarz for a UCP map gives
$F(a^*a)\ge F(a)^*F(a)$. For self-adjoint $a$, this is the stated
positivity. If $P=P^*=P^2$, then

$$
\Sigma_F(P)=F(P)-F(P)^2.
$$

The image is already a positive contraction. The defect vanishes exactly
when it is idempotent, hence exactly when it is a projection. $\square$

### Theorem 5.3 — defect chain laws

For UCP maps $G:C\to B$ and $F:B\to A$,

$$
\boxed{
\Delta_{F\circ G}^{\mathrm{rec}}(a,b)
=
F\!\left(\Delta_G^{\mathrm{rec}}(a,b)\right)
+
\Delta_F^{\mathrm{rec}}\!\left(G(a),G(b)\right).}
$$

For self-adjoint $a$,

$$
\boxed{
\Sigma_{F\circ G}(a)
=
F\!\left(\Sigma_G(a)\right)
+
\Sigma_F\!\left(G(a)\right).}
$$

*Proof.* Insert and subtract $F(G(a)G(b))$:

$$
\begin{aligned}
F(G(ab))-F(G(a))F(G(b))
={}&F\bigl(G(ab)-G(a)G(b)\bigr)\\
&+F(G(a)G(b))-F(G(a))F(G(b)).
\end{aligned}
$$

This is the first identity. Put $b=a=a^*$ for the second. $\square$

Both summands in the sharpness law are positive. Consequently, if the
composite sharpness defect vanishes, then

$$
F(\Sigma_G(a))=0,
\qquad
\Sigma_F(G(a))=0.
$$

It does **not** follow that $\Sigma_G(a)=0$ unless $F$ is faithful on that
positive element. This qualification prevents a later channel from hiding an
earlier defect from being mistaken for restored native sharpness.

### Proposition 5.4 — gauge covariance

For $F'=\alpha_A\circ F\circ\alpha_B^{-1}$,

$$
\Delta_{F'}^{\mathrm{rec}}(\alpha_B(a),\alpha_B(b))
=
\alpha_A\bigl(\Delta_F^{\mathrm{rec}}(a,b)\bigr),
$$

and for self-adjoint $a$,

$$
\Sigma_{F'}(\alpha_B(a))=\alpha_A(\Sigma_F(a)).
$$

Thus zero defect, positivity, spectrum and norm are presentation invariant.

### Separation 5.5 — this is not the Born composition defect

The record defect and the ISP Born defect have different types and physical
questions:

$$
\boxed{\Delta^B\ne\Delta^{\mathrm{rec}}.}
$$

- $\Delta^B$ compares a stochastic shadow of a composed amplitude process
  with the composition of stochastic shadows.
- $\Delta^{\mathrm{rec}}$ compares a UCP image of an operator product with
  the product of the two UCP images.

One may vanish while the other does not. No inference between them is made in
this paper.

---

## 6. The multiplicative domain and sharp fact transport

### Definition 6.1 — multiplicative domain

For UCP $F:B\to A$, define

$$
\operatorname{MD}(F)
=
\left\{x\in B:
\begin{array}{l}
F(x^*x)=F(x)^*F(x),\\
F(xx^*)=F(x)F(x)^*
\end{array}
\right\}.
$$

The standard multiplicative-domain theorem states that this is a unital
C*-subalgebra and that, for $x\in\operatorname{MD}(F)$ and $y\in B$,

$$
F(xy)=F(x)F(y),
\qquad
F(yx)=F(y)F(x).
$$

For completeness, the mixed identities follow from the equality case of the
operator Schwarz inequality, applied to the $2\times2$ positive matrix
obtained from $(x,y)$; closure under the C*-operations then gives the stated
subalgebra. In finite dimension no topological qualification is needed.

### Theorem 6.2 — equivalent sharp-record criteria

Let $\mathbf P=(P_r)_{r\in\Omega}$ be a finite PVM in $B$, and let

$$
R=C^*(P_r:r\in\Omega).
$$

For a UCP map $F:B\to A$, the following are equivalent:

1. $R\subseteq\operatorname{MD}(F)$;
2. $F|_R:R\to A$ is a unital *-homomorphism;
3. $F(P_r)$ is a projection for every $r$;
4. $\Sigma_F(P_r)=0$ for every $r$;
5. $\Delta_F^{\mathrm{rec}}(a,b)=0$ for all $a,b\in R$.

When they hold, $(F(P_r))_r$ is a PVM and $F$ induces a Boolean-algebra
homomorphism on the projections of $R$.

*Proof.*

`1 => 2.` The mixed multiplicative-domain identities show that $F$ preserves
every product inside $R$; positivity gives *-preservation and unitality is
given.

`2 => 3.` A *-homomorphism sends a projection to a projection.

`3 <=> 4.` This is Theorem 5.2.

`4 => 1.` For a self-adjoint projection $P_r$, the two defining Schwarz
equalities coincide and equal $F(P_r)=F(P_r)^2$. Hence every $P_r$ lies in
$\operatorname{MD}(F)$. The multiplicative domain is a C*-subalgebra, so it
contains the algebra they generate.

`2 => 5.` Multiplicativity makes the defect zero on $R$.

`5 => 4.` Put $a=b=P_r$. $\square$

The implication from all sharp generator images to multiplicativity is not a
mere set-level assertion: it passes through the multiplicative-domain
theorem. That is the load-bearing step.

### Definition 6.3 — the sharp record category

Define $\mathsf{SharpRec}_D$ as follows.

- An object is a pair $(A,R_A)$, where $A$ is a boundary algebra and
  $R_A\subseteq A$ is a finite commutative C*-algebra generated by a declared
  sharp record PVM.
- A displayed Heisenberg arrow
  $$
  F:(B,R_B)\longrightarrow(A,R_A)
  $$
  is an admitted UCP map $F:B\to A$ satisfying
  $$
  R_B\subseteq\operatorname{MD}(F),
  \qquad
  F(R_B)\subseteq R_A.
  $$

The second condition is genuine target-interface typing. Multiplicativity on
$R_B$ alone does not select which target record interface receives the image.

### Theorem 6.4 — closure of sharp transport

$\mathsf{SharpRec}_D$ is a category. If

$$
G:(C,R_C)\to(B,R_B),
\qquad
F:(B,R_B)\to(A,R_A),
$$

are sharp record arrows, then

$$
R_C\subseteq\operatorname{MD}(F\circ G),
\qquad
(F\circ G)(R_C)\subseteq R_A.
$$

*Proof.* Identities are unital *-homomorphisms on all of their algebras. For
$a,b\in R_C$, first use $R_C\subseteq\operatorname{MD}(G)$ and then
$G(R_C)\subseteq R_B\subseteq\operatorname{MD}(F)$:

$$
\begin{aligned}
(F\circ G)(ab)
&=F(G(a)G(b))\\
&=F(G(a))F(G(b)).
\end{aligned}
$$

The same calculation with adjoints establishes the multiplicative-domain
criterion for the composite. Image containment follows from the two given
containments. Associativity is inherited from $\mathsf{Chan}_D$. $\square$

### Definition 6.5 — the partial Boolean interface

Let $\operatorname{Proj}(R)$ denote the finite Boolean algebra of projections
of a finite commutative C*-algebra $R$. Define

$$
\operatorname{Rec}_{\mathrm{sharp}}:
\mathsf{SharpRec}_D\longrightarrow\mathbf{BoolAlg}
$$

by

$$
(A,R_A)\longmapsto\operatorname{Proj}(R_A),
\qquad
F\longmapsto F|_{\operatorname{Proj}(R_B)}.
$$

Theorem 6.2 makes every arrow a Boolean homomorphism, and Theorem 6.4 gives
identity and composition exactly. The functor is covariant along displayed
Heisenberg arrows and contravariant relative to physical Schrödinger
evolution. Relative to all admitted channels it is partial: a generic channel
lies only in `Rec_eff`, not in $\mathsf{SharpRec}_D$.

### Proposition 6.6 — sharpness is necessary, not sufficient, for fact identity

There exist two sharp record PVMs with the same Boolean map and the same
outcome law but no supplied common process, copying lineage, common witness or
overlap morphism. The construction above then certifies only a Boolean
homomorphism. It does not certify W6 co-reference.

*Proof.* Take two separately prepared qubits, each measured in its
computational basis with the same fair state, and identify their two-element
outcome sets abstractly. Identity on the Boolean outcome algebra is sharp and
probability preserving. No physical arrow between the preparations has been
specified. The same mathematics also applies to an accidental agreement
control. Hence proposition transport does not construct fact identity.
$\square$

---

## 7. The law-relative record-observability operator system

### Definition 7.1 — admitted transports

Fix an internal W3 diagram $W$ at boundary $x_W$. For another boundary $y$,
let $\mathsf{Tr}_D(y,W)$ be the declared family of physically admitted
Heisenberg channel diagrams

$$
\Phi_a^*:\mathfrak B_{x_W}\longrightarrow\mathfrak B_y.
$$

The family is closed under presentation equivalence and contains exactly the
transports admitted by the law. It is not inferred from a single realized
history.

### Definition 7.2 — minimal observability operator system

Define

$$
\mathcal S_W(y)
=
\operatorname{span}_{\mathbb C}
\left(
\{I_y\}
\cup
\{\Phi_a^*(P_r):a\in\mathsf{Tr}_D(y,W),\ r\in\Omega\}
\cup
\{\Phi_a^*(P_r)^*\}_{a,r}
\right).
$$

Every displayed generator is an effect and therefore self-adjoint; the last
set is redundant in this finite record case but records the operator-system
typing explicitly.

### Theorem 7.3 — operator-system observability

At each eligible boundary $y$, $\mathcal S_W(y)$:

1. is a unital self-adjoint linear subspace of $\mathfrak B_y$;
2. is the least operator system containing every admitted transported record
   effect;
3. grows monotonically when the admitted transport family grows;
4. is covariant under unitary presentation changes;
5. is invariant under record- and arrow-handle renaming; and
6. obeys the clean inaccessible-spectator law of Proposition 7.5.

*Proof.* The displayed span contains $I_y$, is linear by construction, and is
closed under adjoint, proving the first claim. Every operator system
containing the generators contains their complex span, proving minimality.
Generator inclusion proves monotonicity. A presentation change conjugates
every generator by the same boundary unitary, so it conjugates the span.
Handles do not occur in the operator formula. The last claim is proved below.
$\square$

### Definition 7.4 — four distinct closures

The following objects must not be compressed:

$$
\mathcal S_W(y),
\qquad
C^*(\mathcal S_W(y)),
\qquad
\operatorname{Eff}(\mathcal S_W(y)),
\qquad
\operatorname{Sharp}(\mathcal S_W(y)).
$$

Here

$$
\operatorname{Eff}(\mathcal S)
=
\mathcal S\cap\operatorname{Eff}(\mathfrak B_y),
$$

and $\operatorname{Sharp}(\mathcal S)$ is the set of those effects in
$\mathcal S$ that are projections in the ambient algebra. The generated
C*-algebra additionally closes under multiplication. Those products are
algebraic consequences, not automatically jointly implementable experiments.

### Proposition 7.5 — clean inaccessible-spectator law

Let the boundary algebra be $A\otimes C$, let the native record projectors be
$P_r\otimes I_C$, and suppose every relevant admitted transport is exactly
$\Phi_a^*\otimes\operatorname{id}_C$. Then

$$
\mathcal S_{W\otimes C}(y\otimes C)
=
\mathcal S_W(y)\otimes\mathbb C I_C.
$$

*Proof.* Unitality gives

$$
(\Phi_a^*\otimes\operatorname{id}_C)(P_r\otimes I_C)
=
\Phi_a^*(P_r)\otimes I_C.
$$

Taking the unital self-adjoint span gives exactly the right-hand side.
$\square$

An accessible spectator with its own admitted effects can enlarge the system.
The proposition concerns a genuinely inaccessible spectator and therefore
prevents its matrix dimension from being mislabeled as record support.

### Proposition 7.6 — law-relative, not intrinsic

Two admitted transport grammars with the same native W3 experiment can yield
different operator systems.

*Proof.* One grammar may contain only the identity transport, while a second
also contains a unitary that rotates the record PVM to a noncommuting PVM.
The native W3 amplitudes and record law agree, but the second generator span
is strictly larger. $\square$

Thus $\mathcal S_W$ is a theorem of a declared counterfactual law, not an
intrinsic support derived from realized amplitudes alone.

---

## 8. Admitted idempotents and type-correct addressability

### Definition 8.1 — admitted Karoubi completion

Let $\mathsf{Chan}_D$ be fixed before subobjects are discussed. Its Karoubi
completion $\operatorname{Kar}(\mathsf{Chan}_D)$ has:

- objects $(B,e)$, where $e:B\to B$ is an **admitted** UCP map with
  $e\circ e=e$;
- arrows
  $$
  f:(B,e)\longrightarrow(C,d)
  $$
  given by admitted UCP maps $f:B\to C$ satisfying
  $$
  f=d\circ f\circ e.
  $$

The identity on $(B,e)$ is $e$. Composition is inherited from
$\mathsf{Chan}_D$.

### Theorem 8.2 — Karoubi typing

Definition 8.1 gives a category.

*Proof.* The proposed identity satisfies $e=e\circ e\circ e$. If
$f=dfe$ and $g=kgd$, then

$$
g f
=
k g d\, d f e
=
k(gf)e,
$$

so the composite has the required type. Moreover,
$f\circ e=dfe=f$ and $d\circ f=d(dfe)=dfe=f$. Associativity follows from
the ambient category. $\square$

### Proposition 8.3 — fixed ranges are operator systems

For an admitted UCP idempotent $e:B\to B$,

$$
\operatorname{Fix}(e)=\{b\in B:e(b)=b\}=\operatorname{Ran}(e)
$$

is a unital self-adjoint linear subspace, hence an operator system.

*Proof.* Linearity and idempotence identify fixed points with the range.
Unitality puts $I$ in the range, and positivity implies *-preservation, so the
range is self-adjoint. $\square$

The range need not be a C*-subalgebra under the ambient multiplication. The
Choi--Effros theorem supplies a C*-product

$$
x\circ_e y=e(xy)
$$

on the range of a completely positive contractive projection. At the UCP
finite-dimensional scope used here, this applies. If $e$ is a conditional
expectation onto an ambient C*-subalgebra $N$—equivalently in this finite
setting, an idempotent UCP projection with the appropriate $N$-bimodule
property—then its range is $N$ with the ordinary ambient product. These are
different claims.

### Definition 8.4 — addressability candidate

For an observability operator system $\mathcal S_W(y)\subseteq B$, an
**effect-addressability candidate** is an admitted Karoubi object $(B,e)$
with

$$
\mathcal S_W(y)\subseteq\operatorname{Fix}(e).
$$

If the transported interface at $y$ is a PVM with record algebra $R_W(y)$, a
**sharp-addressability candidate** additionally requires

$$
R_W(y)\subseteq\operatorname{MD}(e).
$$

Because a fixed projection $P=e(P)$ satisfies
$e(P)=e(P)^2$, this extra condition follows from Theorem 6.2 whenever all the
record projectors themselves lie in $\mathcal S_W(y)\subseteq\operatorname{Fix}(e)$.
It is retained explicitly to expose the typing when a sharp record algebra is
supplied separately from the effect span.

### Definition 8.5 — order and classification

For admitted UCP idempotents on the same algebra, set

$$
e\preceq f
\quad\Longleftrightarrow\quad
e f=f e=e.
$$

This is a partial order. Moreover, $e\preceq f$ implies
$\operatorname{Fix}(e)\subseteq\operatorname{Fix}(f)$.

*Proof.* Reflexivity and transitivity follow by associativity. If
$e\preceq f$ and $f\preceq e$, the defining equations give $e=f$.
For $x=e(y)$, $f(x)=fe(y)=e(y)=x$. $\square$

The law-relative classifications are:

1. a unique minimal proper containing idempotent;
2. several incomparable minimal proper containing idempotents;
3. one physical-symmetry orbit or groupoid of such minima; or
4. identity only, so the record-observability system is global at this
   admitted-law scope.

There is an important correction to the frozen pin. Every category contains
$\operatorname{id}_B$, and it always fixes $\mathcal S_W(y)$. Therefore a
literal “no containing idempotent” case is impossible under Definition 8.4.
The honest negative is:

$$
\boxed{\text{no proper admitted containing idempotent; identity only}.}
$$

If a future definition excludes the identity by requiring a proper chart,
that same case may be called no proper addressability. The theorem is not
altered to manufacture a logically impossible control.

### Proposition 8.6 — abstract existence is not physical admission

Let $B=M_2(\mathbb C)$ and

$$
\mathcal S=\operatorname{span}\{I,Z\}.
$$

The dephasing map

$$
E_Z(a)=P_0aP_0+P_1aP_1
$$

is a UCP idempotent with $\operatorname{Fix}(E_Z)=\mathcal S$. In a grammar
that admits $E_Z$, it is a proper addressability certificate. In a grammar
that admits only identities and a declared unitary group not containing an
idempotent with this range, the same abstract $E_Z$ is not an arrow and the
classification is identity-only.

The algebra, states and record can be identical in the two theories. Physical
addressability depends on counterfactual operations, not abstract algebraic
availability.

---

## 9. Exact qubit transport controls

All matrices in this section are exact. Put

$$
P_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\quad
P_1=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\quad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad
Z=P_0-P_1.
$$

### Control 9.1 — unitary transport

For a unitary $U$, let $F_U(a)=U^*aU$. Then

$$
F_U(ab)=F_U(a)F_U(b)
$$

on the entire algebra. Hence

$$
\operatorname{MD}(F_U)=M_2(\mathbb C),
\qquad
\Delta_{F_U}^{\mathrm{rec}}=0,
\qquad
\Sigma_{F_U}(P_r)=0.
$$

The PVM is unitarily conjugated and remains sharp. This is the positive gauge
and presentation control.

### Control 9.2 — deterministic bit flip

For $F_X(a)=XaX$,

$$
F_X(P_0)=P_1,
\qquad
F_X(P_1)=P_0.
$$

The induced Boolean map is the nontrivial automorphism exchanging the two
atoms. Exact sharp transport need not fix record values pointwise.

### Control 9.3 — dephasing

Define

$$
D_Z(a)=P_0aP_0+P_1aP_1.
$$

This is UCP, unital and idempotent. It fixes the diagonal record algebra

$$
R_Z=\operatorname{span}\{I,Z\}
$$

pointwise. Therefore $R_Z\subseteq\operatorname{MD}(D_Z)$ and the record
PVM remains sharp, although $D_Z$ is not multiplicative on all of
$M_2(\mathbb C)$.

### Control 9.4 — random-unitary unsharp evidence

Define

$$
F_{1/4}(a)=\frac34a+\frac14XaX.
$$

Then

$$
F_{1/4}(P_0)
=
\begin{pmatrix}3/4&0\\0&1/4\end{pmatrix},
\qquad
F_{1/4}(P_1)
=
\begin{pmatrix}1/4&0\\0&3/4\end{pmatrix}.
$$

The effects commute and sum to $I$, but neither is a projection. Exactly,

$$
\Sigma_{F_{1/4}}(P_0)
=
\Sigma_{F_{1/4}}(P_1)
=
\frac3{16}I.
$$

Thus `Rec_eff` is defined and `Rec_sharp` is not. Commutativity does not turn
an unsharp effect algebra into Boolean logic.

### Control 9.5 — amplitude damping

Take damping parameter $\gamma=1/2$ and Schrödinger Kraus operators

$$
K_0=\begin{pmatrix}1&0\\0&1/\sqrt2\end{pmatrix},
\qquad
K_1=\begin{pmatrix}0&1/\sqrt2\\0&0\end{pmatrix}.
$$

The Heisenberg channel is

$$
A_{1/2}^*(a)=K_0^*aK_0+K_1^*aK_1.
$$

For the excited-state record proposition,

$$
A_{1/2}^*(P_1)=\frac12P_1,
\qquad
\Sigma_{A_{1/2}^*}(P_1)=\frac14P_1.
$$

Evidence transport exists exactly; the proposition is not sharp upstream.

### Control 9.6 — two noisy channels and the chain law

For

$$
F_p(a)=(1-p)a+pXaX,
$$

composition gives

$$
F_p\circ F_q=F_{p\star q},
\qquad
p\star q=p+q-2pq.
$$

At $p=q=1/4$, $p\star q=3/8$, so

$$
\Sigma_{F_{3/8}}(P_0)=\frac{15}{64}I.
$$

The two chain-law terms are

$$
F_{1/4}\!\left(\Sigma_{F_{1/4}}(P_0)\right)
=
\frac3{16}I
=
\frac{12}{64}I,
$$

and, because
$F_{1/4}(P_0)=\tfrac12I+\tfrac14Z$,

$$
\Sigma_{F_{1/4}}\!\left(F_{1/4}(P_0)\right)
=
\frac3{64}I.
$$

Their sum is $15I/64$, exactly the composite defect. The calculation tests
the chain law rather than merely restating it.

### Control 9.7 — sharp evidence still does not prove co-reference

Controls 9.1--9.3 transport projections exactly. If the source and target
records belong to separately declared experiments with no physical bridge,
this sharpness does not make them the same fact. Conversely, when a declared
channel genuinely is the physical bridge, zero defect verifies the logical
part of that bridge but not event-token identity. This separates
multiplicative transport from W6 descent.

### Control 9.8 — record-handle renaming

Replace labels $0,1$ by $\mathtt{red},\mathtt{blue}$ while retaining
$P_{\mathtt{red}}=P_0$ and $P_{\mathtt{blue}}=P_1$. Every effect, defect,
multiplicative-domain decision, operator system and idempotent classification
is unchanged. Only the external outcome-indexing bijection changes.

---

## 10. The branch-memory W3 seed inside the same quantum process

### 10.1 Exact process

Let

$$
H=\mathbb C^2_b\otimes\mathbb C^2_m
$$

with basis $|b,m\rangle$. The branch is $b$ and the memory degree is $m$;
these names describe this declared control and are not inferred spatial
coordinates. Put

$$
H_2=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$

The write, no-write, preserve and erase arrows are

$$
U=\operatorname{CNOT}_{b\to m}(H_2\otimes I),
\qquad
N=H_2\otimes I,
$$

$$
V=H_2\otimes I,
\qquad
E=(H_2\otimes I)\operatorname{CNOT}_{b\to m}.
$$

The memory record PVM is

$$
P_m=\sum_{b=0}^1|b,m\rangle\langle b,m|,
\qquad
R_W=\operatorname{span}\{I,Z_m\}.
$$

For fine alternatives write
$Q_{bm}=|b,m\rangle\langle b,m|$.

### Theorem 10.1 — internal W3 seam

The same exact amplitude process has all four required behaviors:

1. $U$ writes a perfectly correlated record;
2. $V$ preserves record availability;
3. $E$ coherently erases it and restores a nonzero cross-sector term;
4. $N$ fails the writing-correlation test.

Moreover,

$$
\langle00|VQ_{00}U|00\rangle=\frac12.
$$

*Proof.* For every basis preparation,

$$
U|b,m\rangle
=
\frac{|0,m\rangle+(-1)^b|1,m\oplus1\rangle}{\sqrt2}.
$$

The nonzero alternatives have different memory values, establishing perfect
record correlation. Since $V$ changes only the branch, a final basis probe
can receive alternatives only from one memory sector. Thus availability is
preserved.

For preparation $|00\rangle$ and final probe $\langle00|$,

$$
\langle00|EQ_{00}U|00\rangle=\frac12,
\qquad
\langle00|EQ_{11}U|00\rangle=\frac12.
$$

The alternatives come from different record sectors and have cross term
$1/4$, so the eraser fails availability and exposes recoherence. In contrast,

$$
N|b,m\rangle
=
\frac{|0,m\rangle+(-1)^b|1,m\rangle}{\sqrt2},
$$

whose two alternatives have the same memory value; the write-correlation
criterion fails. Finally, $Q_{00}U|00\rangle=|00\rangle/\sqrt2$ and
$\langle00|V|00\rangle=1/\sqrt2$, giving $1/2$. $\square$

Historical occurrence and present availability remain distinct. The write
certifies occurrence; $V$ retains availability; $E$ removes availability but
does not make the earlier writing event never have occurred.

### Proposition 10.2 — native and transported record logic

At the native record boundary, $(P_0,P_1)$ is a PVM and $R_W$ is Boolean.
The preserving and erasing dynamics are part of the same amplitude family;
the record is not an attached classical spectator.

Consider Heisenberg transport of $Z_m$. The no-write unitary gives

$$
N^*Z_mN=Z_m,
$$

while the write unitary gives

$$
U^*Z_mU=X_bZ_m.
$$

Both channels are unitary and therefore sharp. If both transports are
admitted at the preparation boundary, the minimal operator system generated
by the two transported record PVMs is

$$
\mathcal S_W(x_0)
=
\operatorname{span}\{I,Z_m,X_bZ_m\}.
$$

It has dimension three. Its generated C*-algebra additionally contains

$$
Z_m(X_bZ_m)=X_b
$$

and equals

$$
C^*(\mathcal S_W(x_0))
=
\operatorname{span}\{I,Z_m,X_bZ_m,X_b\}.
$$

Thus the operator system and its multiplicative closure are strictly
different even in the seed.

If the law instead admits the random mixture

$$
\tfrac34\operatorname{Ad}_N+\tfrac14\operatorname{Ad}_U,
$$

then a native sharp memory proposition can become an unsharp effect at the
preparation boundary. The W3 occurrence theorem is unchanged; only the
transported evidence interface differs.

### Construction 10.3 — an admitted addressability map for the seed

Let $P_s^X=(I+sX)/2$ on the branch qubit and let $P_m^Z$ be the
computational projector on the memory qubit. Put

$$
Q_{s,m}=P_s^X\otimes P_m^Z,
\qquad s\in\{+,-\},\quad m\in\{0,1\},
$$

be the four joint spectral projections of the commuting observables $X_b$
and $Z_m$. Define

$$
e_{XZ}(a)=\sum_{s,m}Q_{s,m}aQ_{s,m}.
$$

This is a UCP idempotent conditional expectation with

$$
\operatorname{Fix}(e_{XZ})
=
\operatorname{span}\{I,Z_m,X_bZ_m,X_b\}
=
C^*(\mathcal S_W(x_0)).
$$

Therefore, in a process grammar that physically admits $e_{XZ}$, the Karoubi
object $(M_4(\mathbb C),e_{XZ})$ is a proper addressability candidate
containing the three-dimensional W3 observability operator system. If the
grammar does not admit this or another proper containing idempotent, the same
operator system is classified identity-only. The matrix formula alone does
not decide which law is physically present.

### Interpretation 10.4 — what the seed demonstrates

The W3 seam is an internally quantum source of a sharp record. The present
paper does not replace it by a POVM. It says that a later or earlier noisy
view of that seam may carry only unsharp evidence. Sharpness belongs to a
typed boundary and transport, not to a label detached from the process.

---

## 11. The terminal RQ0-A declared-map control

Terminal RQ0-A constructed finite amplitude instruments, a common amplitude
subinstrument and declared signed-permutation/isometric process morphisms.
For each relevant record projector $P_r$ and declared isometry $J$, it checked
an exact pullback of the form

$$
J^*P_r^{\mathrm{target}}J=P_r^{\mathrm{source}}.
$$

### Proposition 11.1 — RQ0-A is a sharp-map control

At that inherited finite declared-map scope, the record projector pullbacks
are zero-sharpness transports on the selected record algebra. Therefore the
induced Boolean maps are instances of Theorem 6.2.

*Proof.* The selected pullback is a projector. Hence its sharpness defect on
each record atom vanishes. Theorem 6.2 places the generated finite record
algebra in the multiplicative domain of the selected UCP pullback map.
$\square$

Compression $a\mapsto J^*aJ$ need not be multiplicative on the full ambient
algebra. The proposition concerns only the exactly checked record algebra.
RQ0-A remains a declared-region, declared-morphism fact-descent result. It is
not converted into intrinsic overlap discovery by the present theorem.

---

## 12. Addressability controls and ambiguity

### Control 12.1 — unique proper candidate

Let $B=M_2(\mathbb C)$, let
$\mathcal S=\operatorname{span}\{I,Z\}$, and let the admitted endomorphism
grammar be generated under composition by $\operatorname{id}$ and $D_Z$.
The only idempotents are $\operatorname{id}$ and $D_Z$. Thus $D_Z$ is the
unique minimal proper addressability candidate. Its fixed operator system is
the diagonal algebra, and it is sharp on the computational record PVM.

### Control 12.2 — admitted versus merely abstract expectation

Keep the same $B$ and $\mathcal S$ but remove $D_Z$ from the admitted grammar.
If the remaining admitted endomorphisms are identities and a group of unitary
automorphisms, their only idempotent is the identity: an invertible idempotent
must equal the identity. Although the formula for $D_Z$ still exists in
operator theory, it supplies no physical certificate. The classification is
identity-only/global.

### Control 12.3 — identity-only because the record is global

Let $\mathcal S=B=M_2(\mathbb C)$. If $e$ fixes every element of
$\mathcal S$, then $e=\operatorname{id}_B$. Thus no proper idempotent can
contain the system, independently of which additional maps are admitted. This
is the exact global control.

### Control 12.4 — symmetry-related minimal candidates

Let

$$
B=\mathbb C^2\otimes M_2(\mathbb C),
\qquad
\mathcal S=\mathbb C^2\otimes\mathbb C I_2.
$$

Choose the exact unit Bloch vectors

$$
n=(0,0,1),
\qquad
m=(\sqrt3/2,0,1/2),
\qquad
c=n\cdot m=\frac12,
$$

and let

$$
D_u(a)=\frac12\bigl(a+\sigma_u a\sigma_u\bigr),
\qquad
\sigma_u=u_xX+u_yY+u_zZ,
$$

be the exact qubit dephasing channel along axis $u$. Define

$$
e_n=\operatorname{id}_{\mathbb C^2}\otimes D_n,
\qquad
e_m=\operatorname{id}_{\mathbb C^2}\otimes D_m.
$$

Both are proper UCP idempotents and both fix $\mathcal S$. Let $U$ implement
the angle-$\pi$ Bloch rotation about the unit bisector of $n$ and $m$; this
rotation exchanges the two axes and has exact algebraic entries. Admit the
grammar generated under composition by $e_n,e_m$ and
$\alpha=\operatorname{id}\otimes\operatorname{Ad}_U$.

After deleting adjacent repetitions, every nontrivial alternating word in
$D_n,D_m$ has, on Bloch vectors, the form

$$
c^k u v^{\mathsf T},
\qquad
u,v\in\{n,m\},
$$

for some $k\ge0$. Its only possible nonzero eigenvalue is
$c^k(v\cdot u)$. It equals one only for the unrepeated single-axis maps
$nn^{\mathsf T}$ and $mm^{\mathsf T}$; every other nonzero reduced word has
a positive power of $c$ strictly between zero and one. A nonzero rank-one
map is idempotent exactly when its nonzero eigenvalue is one. The words with
no dephasing are $I$ and the involutive Bloch rotation $R$ induced by
$\alpha$; $R\ne I$ and $R^2=I$, so $R$ is not idempotent. Using
$\alpha D_n\alpha=D_m$ and $\alpha^2=I$ reduces every word containing
$\alpha$ to these cases. Hence the proper idempotents of the declared grammar
that contain $\mathcal S$ are exactly $e_n$ and $e_m$.

They are incomparable: neither fixed operator system contains the other.
The physical symmetry $\alpha$ exchanges them. The correct result is the
two-object action groupoid, not a lexical choice of one Bloch axis.

If the full depolarizing expectation onto
$\mathbb C^2\otimes\mathbb C I$ were admitted, it would lie below both and
remove the ambiguity. It is deliberately not admitted in this control. Its
abstract existence does not affect the declared category.

### Control 12.5 — inaccessible spectator

Tensor Control 12.1 with an algebra $C$ on which no independent preparations,
effects or controls are admitted, and extend all record transports by
$\operatorname{id}_C$. Proposition 7.5 returns
$\mathcal S\otimes I_C$, not the full $B\otimes C$. The spectator changes
carrier size but not record relevance. If a separate admitted idempotent or
probe makes $C$ operationally accessible, the premise fails and the
classification may change honestly.

### Control 12.6 — the literal no-containing branch is empty

For every $\mathcal S\subseteq B$,

$$
\mathcal S\subseteq\operatorname{Fix}(\operatorname{id}_B).
$$

Thus an implementation or proof returning “no containing idempotent” while
identities remain admitted is incorrect. The measurable negative is “no
proper containing idempotent.” This control catches a category-definition
error rather than a physical phenomenon.

---

## 13. Ontology: sharp fact, unsharp evidence, and law-relative access

The mathematical layers have different referents.

### 13.1 Native sharp record

At its W3 seam, a record proposition is sharp because the actual write and
continuation tests certify a finite PVM and its classical availability. This
is not a claim that the entire process is classical. The eraser control shows
that coherent amplitude structure remains outside the seam and can be made
operational again.

### 13.2 Transported evidence

An upstream or downstream channel can blur a sharp proposition into an
effect. The effect answers a quantitative question:

> With this transformed preparation or access path, how strongly does the
> native record outcome bear on the present experiment?

It need not itself name a currently available Boolean fact. Unsharpness is
ordinary quantum behavior, not a failure of the channel description.

### 13.3 Exact sharp transport

Zero record defect means the channel behaves as a *-homomorphism on the
record algebra. It preserves the proposition logic exactly. This makes it
eligible for `Rec_sharp`. It still does not supply a historical copying
lineage, common witness, physical overlap or token identity. Those are
additional referents.

### 13.4 Law-relative addressability

An admitted idempotent says that the process law contains an executable,
repeatable projection of operational access onto a fixed operator system.
That is stronger than mere observability but weaker than spatial locality.
The addressability answer can change when the admitted counterfactual grammar
changes even though realized amplitudes and record statistics do not.

This dependence is not an implementation defect. It is a theorem about what
localization claims require: realized history underdetermines the space of
possible interventions.

### 13.5 What remains ungrounded

The construction still begins with selected:

- process boundaries;
- a W3 diagram;
- a native record PVM;
- a family of admitted transports;
- and, for addressability, admitted idempotent operations.

No theorem here shows that operationally equivalent choices always yield the
same family, or discovers physical overlaps among independently presented
systems. The result must therefore be called law-relative W3 transport and
addressability, never intrinsic support or quantum locality.

---

## 14. Four-gate audit

| Object | Referent | Necessity | No-smuggling boundary | Exact discriminator |
|---|---|---|---|---|
| effect | yes/no propensity for an admitted outcome | generic channels do not preserve projectors | effect value does not establish fact identity | unitary versus random-unitary transport |
| POVM | complete outcome-probability interface | every transported PVM remains normalized | no state update is invented | same POVM, different instruments |
| instrument | outcome together with conditional process update | W3 is dynamical | supplied branches, not inferred from effects | Lüders versus reprepare |
| record defect | failure of a channel to preserve record multiplication | separates sharp logic from noisy evidence | kept distinct from $\Delta^B$ | zero unitary/dephasing versus noisy controls |
| multiplicative domain | maximal algebra on which one UCP map is homomorphic | types the sharp subcategory | no W6 co-reference inferred | sharp PVM versus unsharp POVM |
| operator system | least unital self-adjoint span directly generated by transported record effects | avoids silently adjoining products | transport grammar remains declared | three-dimensional seed system versus four-dimensional C*-closure |
| admitted idempotent | executable repeatable access projection | turns an abstract range into a typed process object | abstract expectation excluded | admitted versus unadmitted dephasing |
| Karoubi object | fixed operator system of an admitted idempotent | repairs the prior codomain mismatch | not every subalgebra is promoted | proper, ambiguous and identity-only controls |

All objects pass referent, necessity and finite exact discriminator gates at
their declared law-relative scope. The operator system and idempotent layers
do **not** pass the stronger no-smuggling gate required for intrinsic support,
because their selected record and admitted grammar remain inputs. This blocks
every localization or spatial interpretation while leaving the transport
theorems intact.

---

## 15. Theorem and control register

| Item | Grade | Scope | Result |
|---|---|---|---|
| UCP effect transport | theorem | finite-dimensional unital C*-algebras | effects and partial sums preserved |
| PVM-to-POVM transport | theorem | finite outcome set | total and functorial |
| instrument precomposition | theorem | finite-dimensional Schrödinger CP maps | instrument and effect shadow compose |
| equal POVM/different disturbance | construction | one qubit | exact separation |
| record-defect positivity | theorem | UCP, self-adjoint input | $\Sigma_F\ge0$ |
| defect chain law | theorem | composable UCP maps | exact two-term identity |
| record sharpness equivalence | theorem | finite PVM algebra | MD, homomorphism, sharpness and zero defect equivalent |
| sharp record category | construction/theorem | admitted UCP maps with image typing | closed under identity and composition |
| `Rec_sharp` | construction | sharp record category | Boolean functor; partial among all channels |
| operator-system observability | theorem | fixed W3 diagram and admitted transport law | minimal, monotone, covariant, handle invariant |
| spectator law | theorem | exact product transports with unital spectator identity | no inaccessible factor inflation |
| Karoubi completion | construction/theorem | admitted UCP channel category | type-correct idempotent objects |
| fixed range | theorem | admitted UCP idempotent | operator system; Choi--Effros product available |
| addressability | definition/constructions | fixed admitted law | proper, ambiguous and identity-only cases |
| branch-memory seam | inherited theorem, rederived | exact $\mathbb Q(\sqrt2)$ amplitudes | write/preserve/erase/no-write and $1/2$ loop |
| terminal RQ0-A | inherited control | finite declared-map scope | exact sharp projector pullback only |
| intrinsic localization | open obligation | representation-independent operational theory | not established |

---

## 16. Outcome audit

### 16.1 Effect-transport rung

The following requirements are proved:

- every admitted UCP map carries effects to effects;
- every finite W3 PVM carries to a normalized POVM;
- fixed-outcome POVM transport is functorial;
- full outcome instruments compose whenever their branches are supplied;
- effects are a functorial shadow, not a replacement, of instruments;
- the record defect is positive on self-adjoint inputs and obeys the exact
  chain law;
- unitary covariance and handle invariance are exact.

Therefore the paper provisionally earns

$$
\boxed{\texttt{RQ0-L0-W3-EFFECT-TRANSPORT}.}
$$

### 16.2 Sharp-fact-transport rung

The finite record algebra lies in the multiplicative domain exactly when all
record atoms remain sharp, exactly when the restricted map is a unital
*-homomorphism, and exactly when the record defect vanishes throughout that
algebra. The typed sharp category and Boolean functor close under
composition. No co-reference or token identity is inferred.

Therefore the paper provisionally earns

$$
\boxed{\texttt{RQ0-L0-SHARP-FACT-TRANSPORT}.}
$$

### 16.3 Addressable-operator-system rung

The least law-relative observability object is constructed as an operator
system. Admitted UCP idempotents form typed Karoubi objects, and exact controls
separate proper addressability, abstract-but-unadmitted expectations,
symmetry-related ambiguity and identity-only/global cases. The pin's literal
no-containing case is corrected to the only category-consistent negative:
no proper candidate.

Therefore the provisional highest cumulative result is

$$
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM}.}
$$

This status is `GREEN-UNREVIEWED`. It is subject to the two independent
reviews required by the governing pin.

### 16.4 Explicit non-results

The paper does not establish:

- a record-independent choice of boundary or projector package;
- invariance under every operationally equivalent transport grammar;
- a unique intrinsic chart;
- a physical overlap or pullback among generic instruments;
- W6 fact descent beyond the inherited declared-map control;
- a quantaloid, Isbell completion, quotient groupoid or Weld stack;
- a spatial region, topology, influence relation or causal order;
- a manifold, Lorentzian geometry, quantum field or gravitational dynamics.

---

## 17. Open mathematical and physical obligations

### 17.1 Instrument-native W3 transport

The total logical transport is presently formulated for a selected native
PVM, with full instruments retained when supplied. A stronger theory would
derive a canonical outcome instrument from the internal W3 diagram—or prove
that no such canonical choice exists—without adding a measurement collapse
to a unitary record-writing process.

### 17.2 Grammar equivalence

The operator system is invariant under presentation isomorphism of one fixed
admitted category. It is not yet proved invariant under different syntactic
grammars presenting the same operational channel theory. A future
no-smuggling theorem must quotient by operational equivalence without
discarding physically distinct counterfactuals.

### 17.3 Naimark and Kraus presentation controls

The same POVM has many Naimark dilations, and the same channel has many Kraus
representations. The present constructions depend only on the represented
UCP map and effects, so they are formally Kraus invariant. A complete
operational no-smuggling round must additionally compare minimal
Naimark-equivalent instruments and their admitted disturbances.

### 17.4 Physical minimality of idempotents

The order $\preceq$ is exact, but the admitted idempotent category can be
infinite and can contain several incomparable candidates. No theorem here
says nature supplies a proper minimum. Identity-only and groupoid-valued
answers are legitimate.

### 17.5 From addressability to charts

An addressable operator system is not yet a chart. A chart claim would need
an intrinsic selection or complete groupoid of such systems, physically typed
maps between them, and executable pullbacks representing overlaps. These are
deliberately outside the cycle.

---

## 18. Conclusion

A W3 record can be sharp where it is written while appearing only as unsharp
evidence through another quantum channel. This is not a contradiction and
does not require abandoning the record. It requires separating two logical
interfaces:

$$
\boxed{
\text{sharp fact at the native W3 seam}
\longrightarrow
\text{possibly unsharp evidence under quantum transport}.}
$$

The positive operator

$$
\Sigma_F(P)=F(P)-F(P)^2
$$

measures that loss of sharpness, and its exact chain law makes the loss
compositional. The zero-defect maps are precisely those whose multiplicative
domain contains the record algebra; only there does Boolean proposition
transport exist. An admitted idempotent can then type a law-relative
addressability object for the directly generated record-observability
operator system.

The ontological gain is modest but real. A record is no longer forced to be
Boolean at every boundary, and noisy evidence is no longer mislabeled as a
new sharp fact. The remaining limitation is equally clear: the law still
selects the cuts, records, transports and idempotents. Intrinsic localization
has not been derived.

---

## References

1. K. Cho, B. Jacobs, B. Westerbaan and A. Westerbaan, “An Introduction to
   Effectus Theory,” *Electronic Notes in Theoretical Computer Science* 319
   (2015), 19--65; arXiv:1512.05813. Effects, effect algebras and Heisenberg
   predicate transformers.
2. M.-D. Choi, N. Johnston and D. W. Kribs, “The multiplicative domain in
   quantum error correction,” *Journal of Physics A: Mathematical and
   Theoretical* 42 (2009), 245303; arXiv:0811.0947. Multiplicative domains of
   UCP maps and their homomorphic restriction.
3. E. B. Davies and J. T. Lewis, “An operational approach to quantum
   probability,” *Communications in Mathematical Physics* 17 (1970),
   239--260. Quantum instruments as outcome probabilities together with
   transformations.
4. M. Ozawa, “Quantum measuring processes of continuous observables,”
   *Journal of Mathematical Physics* 25 (1984), 79--87. Measurement
   instruments and state change.
5. B. Jacobs, “New Directions in Categorical Logic, for Classical,
   Probabilistic and Quantum Logic,” *Logical Methods in Computer Science*
   11(3:24) (2015); arXiv:1205.3940. Categorical instruments, predicates and
   side effects.
6. M.-D. Choi and E. G. Effros, “Injectivity and operator spaces,”
   *Journal of Functional Analysis* 24 (1977), 156--209. Completely positive
   projections and the induced range product.
7. C. Heunen, A. Kissinger and P. Selinger, “Completely positive projections
   and biproducts,” *Electronic Proceedings in Theoretical Computer Science*
   171 (2014), 71--83; arXiv:1308.4557. Splitting completely positive
   idempotents in categorical quantum mechanics.
8. N. Tomiyama, “On the projection of norm one in $W^*$-algebras,”
   *Proceedings of the Japan Academy* 33 (1957), 608--612. Conditional
   expectations and bimodule structure.
9. A. Mestoudjian, M. Wilson, N. Vanrietvelde and P. Arrighi, “Picturing
   general quantum subsystems,” arXiv:2511.09494v2 (2026). Splitting-map
   comparison language for finite-dimensional von Neumann subsystems; used
   here only as a recent comparison, not as a premise of any theorem.
