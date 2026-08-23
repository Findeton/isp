# ISP v17 — U-Gen C2 relational-kernel decomposition candidate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Question and scope

C1 established that a complete isolated diagonal event law can fail to
determine composite event probabilities. This note identifies, without an
ontological interpretation, the exact finite datum that a strongly positive
pair-history law adds to its diagonal weights.

The result is elementary but load bearing. It prevents three mistakes:

1. calling the diagonal entries probabilities when interference prevents
   their normalization;
2. identifying every strongly positive kernel with one scalar wave
   amplitude; and
3. treating a local phase convention as a physical absolute phase.

Nothing here selects a history space, a dynamical member, an action,
Planck's constant, an actual history, a time variable, a spacetime, or a
gravitational law.

---

## 1. Finite atomic setup

Let

$$
\Omega=\{h_1,\ldots,h_N\}
$$

be a finite fine-history set. A biadditive decoherence functional is fixed by
its atomic matrix

$$
D_{jk}=D(\{h_j\},\{h_k\}).
$$

For the present theorem, **strong positivity** means that $D$ is Hermitian
positive semidefinite. Normalization, when imposed, is

$$
D(\Omega,\Omega)
=\sum_{j,k=1}^{N}D_{jk}=1.
$$

This is not the same as $\operatorname{tr}D=1$.

Define the atomic diagonal weights

$$
w_j=D_{jj}\ge 0
$$

and their support

$$
S=\{j:w_j>0\}.
$$

The weights $w_j$ are called **weights**, not probabilities. In general,

$$
\sum_j w_j=\operatorname{tr}D
$$

need not equal one, and the event propensity

$$
\mu(A)=D(A,A)
$$

need not be additive on fine-history events.

---

## 2. Proposition C2-A — positive weights plus a correlation kernel

### Statement

For every finite Hermitian positive-semidefinite matrix $D$:

1. if $w_j=0$, then $D_{jk}=D_{kj}=0$ for every $k$;
2. on $S$ there is a unique Hermitian positive-semidefinite matrix $C$ with
   unit diagonal such that

   $$
   D_{jk}=\sqrt{w_jw_k}\,C_{jk};
   $$

3. conversely, every nonnegative weight vector $w$ and every Hermitian
   positive-semidefinite unit-diagonal matrix $C$ on its positive support
   define a Hermitian positive-semidefinite $D$ by that equation; and
4. the least Gram dimension of $C$ is $\operatorname{rank}D$.

Thus a finite strongly positive pair-history law is exactly

$$
\boxed{
\text{nonnegative atomic weights}
+
\text{a complex correlation matrix}
}
$$

on its nonzero support.

### Proof

For any two indices, positivity of the corresponding $2\times2$ principal
minor gives

$$
|D_{jk}|^2\le D_{jj}D_{kk}=w_jw_k.
$$

If $w_j=0$, the entire $j$th row and column therefore vanish.

On $S$, let

$$
W=\operatorname{diag}(\sqrt{w_j})_{j\in S}
$$

and define

$$
C=W^{-1}D_SW^{-1}.
$$

Congruence by the invertible positive matrix $W^{-1}$ preserves positive
semidefiniteness. Hermiticity is preserved and

$$
C_{jj}=\frac{D_{jj}}{w_j}=1.
$$

The formula also proves uniqueness.

Conversely, if $C\succeq0$ and has unit diagonal, then

$$
D_S=WCW\succeq0.
$$

Adding zero rows and columns off $S$ preserves positivity. Since $W$ is
invertible on $S$,

$$
\operatorname{rank}D=\operatorname{rank}C.
$$

Every positive-semidefinite $C$ is a Gram matrix,

$$
C_{jk}=\langle u_j,u_k\rangle,
$$

and its unit diagonal makes every $u_j$ a unit vector. The minimal dimension
of such a Gram representation is its rank. QED.

### Corollary C2-A.1 — coherence bound

For all supported histories,

$$
|C_{jk}|\le1.
$$

Equality means that $u_j$ and $u_k$ are collinear; zero means that they are
orthogonal in a minimal Gram representation. This is a relational statement.
It does not make the auxiliary Gram vectors ontic.

### Corollary C2-A.2 — normalized law constraint

If $D$ is normalized, then

$$
\sum_{j,k\in S}\sqrt{w_jw_k}\,C_{jk}=1.
$$

This global constraint does not force $\sum_jw_j=1$. If the diagonal event
function happens to be ordinary additive, the real cross-term sum vanishes
on every relevant disjoint pair, but C1 shows that compositionally active
correlations can still remain.

---

## 3. Proposition C2-B — rank one is positive magnitude plus $U(1)$ phase

### Statement

For the supported correlation matrix $C$, the following are equivalent:

1. $\operatorname{rank}C=1$;
2. there are phases $z_j\in U(1)$ such that

   $$
   C_{jk}=z_j\overline{z_k};
   $$

3. there is one complex atomic amplitude

   $$
   a_j=\sqrt{w_j}\,z_j
   $$

   such that

   $$
   D_{jk}=a_j\overline{a_k}.
   $$

The phase list is unique only up to one common multiplier
$z_j\mapsto e^{i\alpha}z_j$.

### Proof

A rank-one positive-semidefinite unit-diagonal matrix has the form
$C=zz^\dagger$. Its diagonal gives $|z_j|=1$. The remaining implications are
immediate. If $zz^\dagger=z'z'^\dagger$ on a nonempty support, then one
component fixes a common phase relating $z'$ to $z$. QED.

### Scope wall

General strongly positive kernels need not have rank one. They require unit
Gram vectors $u_j$, or equivalently several amplitude components. A mixed
boundary condition, environment, unresolved endpoint, or source label can
produce that higher rank. Calling every $D$ “one complex phase per history”
is false.

---

## 4. Proposition C2-C — tensor composition transports both layers

Let

$$
D=W C W,
\qquad
E=V K V
$$

be two supported decompositions. Under the standard independent product,

$$
D^{AB}=D\otimes E,
$$

the composite decomposition is

$$
W^{AB}=W\otimes V,
\qquad
C^{AB}=C\otimes K.
$$

Consequently,

$$
w^{AB}_{(j,r)}=w^A_jw^B_r,
$$

and

$$
\operatorname{rank}C^{AB}
=\operatorname{rank}C\,\operatorname{rank}K.
$$

This proves that the positive weights and relational kernel are both
composition data. Tensor closure does not select which $C$ or $K$ nature
uses.

---

## 5. Proposition C2-D — multiplicative scalar laws carry a $U(1)$ functor

Let $\mathcal P$ be a category of typed process segments. Suppose a possibly
vanishing scalar amplitude law, not identically zero,

$$
a:\operatorname{Mor}(\mathcal P)\longrightarrow\mathbb C
$$

satisfies

$$
a(q\circ p)=a(q)a(p),
\qquad
a(1_x)=1.
$$

On the subcategory of nonzero morphisms define

$$
r(p)=|a(p)|>0,
\qquad
z(p)=\frac{a(p)}{|a(p)|}\in U(1).
$$

Then

$$
r(q\circ p)=r(q)r(p)
$$

and

$$
z(q\circ p)=z(q)z(p).
$$

Thus $r$ is a positive multiplicative functor and $z$ is a $U(1)$-valued
functor. This conclusion follows only after scalar amplitude multiplicativity
has been assumed. It does not derive scalar amplitudes from ordinary
probabilities.

### Object-gauge covariance

For phases $\eta_x\in U(1)$ attached to boundary objects, define

$$
z^\eta(p:x\to y)
=\eta_y z(p)\overline{\eta_x}.
$$

This remains a functor. For two alternatives $p,q:x\to y$, the relative
phase

$$
z(p)\overline{z(q)}
$$

is invariant. The phase of a closed loop is invariant as well. Hence a
boundary phase convention is gauge, while relative transport and holonomy
can remain physical.

### Modular action

Writing

$$
z(p)=\exp\!\left(\frac{i}{\hbar}S(p)\right)
$$

gives

$$
S(q\circ p)
\equiv S(q)+S(p)
\pmod{2\pi\hbar}.
$$

A globally defined real additive lift $S$ is additional structure and is not
guaranteed by the $U(1)$ functor. Even when such a lift exists, it is not
unique, and it need not be an endpoint difference. Nontrivial closed-loop
holonomy can survive. This is why topology and gauge transport cannot be
replaced silently by one global scalar phase coordinate.

---

## 6. Proposition C2-E — framework principles do not select the phase member

Fix the standard real mixer $H$ and, for every $\theta\in\mathbb R/2\pi
\mathbb Z$, define

$$
T_\theta=
\begin{pmatrix}
1&0\\
0&e^{i\theta}
\end{pmatrix}.
$$

Every $T_\theta$ has the same computational endpoint kernel,

$$
|T_\theta|^{\odot2}=I_2.
$$

For every $\theta$, standard unitary composition supplies:

1. strong positivity of its pair-history compiler;
2. sequential functoriality;
3. tensor composition;
4. reversible complete processes; and
5. ordinary probabilities on decoherent record algebras.

Prepare $|+\rangle=H|0\rangle$, apply $T_\theta$, then apply the fixed
reference operation

$$
R_\phi=\operatorname{diag}(1,e^{-i\phi}),
$$

followed by $H$ and a computational readout. This phase-sensitive
continuation gives

$$
p_0(\theta\mid\phi)
=\frac{1+\cos(\theta-\phi)}2.
$$

Different $\theta$ therefore yield different held-out predictions while
sharing the endpoint packet and all five framework properties.

Even granting algebraic periodicity merely restricts the family. For example,
$T_\theta^8=I$ leaves

$$
\theta=\frac{k\pi}{4},
\qquad k\in\{0,\ldots,7\}.
$$

### Consequence

Strong positivity, reversible composition, tensoriality, and ordinary final
records can select a framework class without selecting the physical phase
member. A phase calibration, action, symmetry representation, coupling, or
other dynamical principle must enter. If it is inserted separately for every
programme, it is an answer table rather than a native generator.

---

## 7. C1 witness in normalized-correlation coordinates

For

$$
D_\pm=
\begin{pmatrix}
\frac12&\pm\frac{i}{4}\\
\mp\frac{i}{4}&\frac12
\end{pmatrix},
$$

the common weight vector is

$$
w=\left(\frac12,\frac12\right),
$$

while

$$
C_\pm=
\begin{pmatrix}
1&\pm\frac{i}{2}\\
\mp\frac{i}{2}&1
\end{pmatrix}.
$$

Both correlation matrices have eigenvalues $3/2$ and $1/2$, hence rank two.
The C1 example is therefore not merely one omitted scalar phase. It is an
omitted rank-two relational correlation orientation. A fixed second system
detects that relative orientation under tensor composition.

---

## 8. Hostile controls

Any future use of this theorem must survive the following controls.

1. **Probability laundering:** call $w_j$ probabilities although they do not
   sum to one.
2. **Rank-one laundering:** write $D=aa^\dagger$ when $D$ has rank greater
   than one.
3. **Gauge laundering:** call an arbitrary rephasing physical without fixing
   the complete relative reference.
4. **Topology erasure:** assume one global endpoint phase when loop holonomy
   is present.
5. **Action lookup:** choose $S_p$ separately after seeing each target
   programme.
6. **Framework/member collapse:** infer $\theta=\pi/4$ from properties shared
   by every $T_\theta$.
7. **Complex-ontology promotion:** infer that complex numbers are material
   beables from a complex representation.
8. **Product-rule circularity:** use tensor closure to justify the same tensor
   rule that was assumed to define composition.
9. **Boundary hiding:** place the target process in an uncharged initial or
   final boundary kernel.
10. **Actuality promotion:** infer one sampled fine history from strong
    positivity alone.

---

## 9. Exact candidate ceiling

If independently reviewed later, this note could earn no more than:

```text
P17-UGEN-C2-FINITE-STRONGLY-POSITIVE-KERNEL-DECOMPOSITION
```

with the statement:

> A finite strongly positive pair-history kernel is uniquely a nonnegative
> atomic weight vector plus a unit-diagonal positive-semidefinite relational
> correlation matrix on its support. Rank one reduces to relative $U(1)$
> phases; general kernels do not. Tensor composition carries both layers, and
> framework-level composition principles do not select a dynamical phase
> member.

It cannot earn:

1. a native quantum generator;
2. an amplitude or history ontology;
3. the Born rule from nonquantum premises;
4. an actuality rule;
5. an internal clock or chronology;
6. QFT, spacetime, or gravity; or
7. an empirical prediction.
