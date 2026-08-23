# ISP v17 — PC4 positive dilation and the first composition frontier

**Status:** ACTIVE AUTHOR-SIDE THEOREM CANDIDATE / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

This note subjects the PC3 projective-control candidate to its strongest
finite ordinary-positive control. It asks whether the exhaustive PC3 endpoint
law really requires projective coherent composition, or whether a uniform
positive reversible model on a larger carrier produces the same registered
predictions.

The answer is positive: a six-state stochastic-readout model and an
eight-state deterministic-readout model both reproduce the entire PC3
\(4I_2/4X/16G\) law. The six-state carrier is minimal inside the finite
reversible realization class defined below. This closes PC3 as an ontology
discriminator at its present endpoint scope.

The result does **not** refute the PC3 projective classification. It shows that
the classification is conditional on its projective-covariance antecedent and
is operationally nonunique once enlarged positive carriers are admitted.

---

## 1. The exact PC3 target

Let

$$
G=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
$$

and let the control group be

$$
\mathcal O
=
\langle b,r\mid b^2=e,\ r^4=e,\ (br)^3=e\rangle.
$$

The intended group is the orientation-preserving octahedral group of order
\(24\), isomorphic to \(S_4\). PC3's projective lift produces an endpoint law

$$
K_g\in\{I_2,X,G\},
\qquad g\in\mathcal O,
$$

with the exhaustive census

$$
\#I_2=4,
\qquad
\#X=4,
\qquad
\#G=16.
$$

The primitive endpoints are

$$
K_b=G,
\qquad
K_r=I_2.
$$

The target of PC4 is this complete \(24\)-element positive endpoint law, not
the unobserved complex matrices used by one representation of it.

---

## 2. A real octahedral realization

Let \(e_x,e_y,e_z\) be the standard basis of \(\mathbb R^3\). Define

$$
B=
\begin{pmatrix}
0&0&1\\
0&-1&0\\
1&0&0
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
0&-1&0\\
1&0&0\\
0&0&1
\end{pmatrix}.
$$

These are orientation-preserving signed permutation matrices. Direct
multiplication gives

$$
B^2=I_3,
\qquad
R^4=I_3,
\qquad
(BR)^3=I_3.
$$

They generate all \(24\) orientation-preserving signed permutation matrices.
Thus they provide the ordinary real action

$$
\rho:\mathcal O\longrightarrow SO(3)
$$

on classical directions.

For every \(g\in\mathcal O\), the vector \(\rho(g)e_z\) is one of

$$
\{\pm e_x,\pm e_y,\pm e_z\}.
$$

This orbit, rather than a Hilbert lift, is enough to determine the registered
PC3 endpoint.

---

## 3. Six-state positive generator

### 3.1 Carrier and dynamics

Take the finite ontic carrier

$$
\Omega_6=\{\pm e_x,\pm e_y,\pm e_z\}.
$$

Every control \(g\) acts deterministically and reversibly:

$$
T_g(v)=\rho(g)v.
$$

The rule is uniform under composition:

$$
T_{gh}=T_gT_h.
$$

It is therefore a genuine positive group generator, not a \(24\)-entry
response table.

### 3.2 Preparations

For binary input \(j\in\{0,1\}\), prepare

$$
\mu_j=\delta_{(-1)^j e_z}.
$$

### 3.3 Reader

Define the stochastic binary response

$$
\xi_0(v)=\frac{1+v_z}{2},
\qquad
\xi_1(v)=1-\xi_0(v).
$$

Thus the \(Z\)-axis ontic states have deterministic readout and the four
equatorial ontic states give a balanced response.

### 3.4 Derived endpoint law

Write

$$
c_g=e_z^{\mathsf T}\rho(g)e_z\in\{-1,0,1\}.
$$

Then

$$
K_g
=
\frac12
\begin{pmatrix}
1+c_g&1-c_g\\
1-c_g&1+c_g
\end{pmatrix}.
$$

Consequently,

$$
K_g=
\begin{cases}
I_2,&\rho(g)e_z=+e_z,\\[1mm]
X,&\rho(g)e_z=-e_z,\\[1mm]
G,&\rho(g)e_z\perp e_z.
\end{cases}
$$

In particular,

$$
K_b=G,
\qquad
K_r=I_2.
$$

The stabilizer of \(+e_z\) has order \(4\), four rotations send \(+e_z\) to
\(-e_z\), and the remaining \(16\) send it to an equatorial direction. Hence
the complete census is exactly

$$
4I_2+4X+16G.
$$

---

## 4. Eight-state outcome-deterministic dilation

The response randomness in the six-state model can be moved into an enlarged
ontic carrier without changing the operational law.

### 4.1 Cube carrier

Take

$$
\Omega_8=\{(x,y,z):x,y,z\in\{-1,+1\}\},
$$

the eight vertices of a cube. The same signed permutation matrices act by

$$
T_g(\lambda)=\rho(g)\lambda.
$$

### 4.2 Face preparations

Prepare input \(j\) uniformly on the face

$$
F_j=\{(x,y,z)\in\Omega_8:z=(-1)^j\}.
$$

Each preparation therefore has four ontic possibilities.

### 4.3 Deterministic reader

Set

$$
o(\lambda)=
\begin{cases}
0,&z=+1,\\
1,&z=-1.
\end{cases}
$$

If \(\rho(g)e_z=+e_z\), the two prepared faces are preserved. If it is
\(-e_z\), they are exchanged. If it is equatorial, each transformed face has
two vertices above and two below the readout plane. The resulting binary law
is therefore again \(I_2\), \(X\), or \(G\), with the same \(4/4/16\) census.

This model is ordinary-positive, Markovian, reversible at the ontic level,
outcome deterministic, and uniform under all PC3 control words.

---

## 5. Carrier-minimum theorem

The following lower bound is deliberately restricted to the class that the
six-state construction inhabits.

### Definition 1 — finite reversible positive realization

A finite reversible positive realization of the PC3 endpoint law consists of:

1. a finite set \(\Omega\);
2. a group homomorphism
   \(\tau:\mathcal O\to\operatorname{Sym}(\Omega)\);
3. two preparation distributions \(\mu_0,\mu_1\) on \(\Omega\); and
4. a response function \(\xi_0:\Omega\to[0,1]\), with
   \(\xi_1=1-\xi_0\),

such that

$$
K_g(o\mid j)
=
\sum_{\lambda\in\Omega}
\xi_o(\tau(g)\lambda)\mu_j(\lambda)
$$

equals the complete PC3 target for every \(g\in\mathcal O\).

No preparation noncontextuality, outcome determinism, or minimal-support
assumption is added.

### Proposition A — every exact action is faithful

If \(n\in\ker\tau\), then

$$
K_{gn}=K_g
$$

for every \(g\in\mathcal O\). In particular, \(K_n=I_2\), so \(n\) fixes the
oriented axis \(+e_z\) in the PC3 target action.

Because \(\ker\tau\) is normal, every conjugate \(gng^{-1}\) also lies in the
kernel and therefore fixes \(+e_z\). Equivalently, \(n\) fixes every member of
the octahedral orbit

$$
\{\pm e_x,\pm e_y,\pm e_z\}.
$$

Only the identity rotation does so. Hence

$$
\ker\tau=\{e\}.
$$

### Proposition B — four states are impossible

Every faithful action of \(S_4\) on four points is its natural transitive
action. The order-four element \(r\) acts as a four-cycle.

The target has

$$
K_{r^k}=I_2,
\qquad k=0,1,2,3.
$$

Since \(0\le\xi_0\le1\), the equality

$$
K_{r^k}(0\mid0)=1
$$

forces \(\xi_0=1\) on every point reached from the support of \(\mu_0\) by
\(r^k\). Transitivity of the four-cycle forces \(\xi_0=1\) on all four
points. This contradicts

$$
K_e(0\mid1)=0.
$$

### Proposition C — five states are impossible

A faithful \(S_4\)-action on five points cannot be transitive because \(5\)
does not divide \(24\). The only faithful orbit structure is the natural
four-point orbit plus one globally fixed point. Other partitions of five
points have a nontrivial common kernel.

The same \(r^k\) argument shows that \(\mu_0\) and \(\mu_1\) cannot both place
weight on the four-cycle. At least one preparation must therefore be
supported entirely on the globally fixed point. Its readout probability is
then unchanged under every \(g\in\mathcal O\), contradicting the balanced
column required by

$$
K_b=G.
$$

### Theorem 1 — exact finite minimum

Every finite reversible positive realization in Definition 1 satisfies

$$
|\Omega|\ge6.
$$

The six-state construction attains the bound. Therefore

$$
\boxed{|\Omega|_{\min}=6}
$$

inside this declared realization class.

This theorem permits a stochastic response. The outcome-deterministic model
above gives

$$
6\le |\Omega|_{\min}^{\rm det}\le8,
$$

but PC4 does not claim the exact deterministic minimum.

---

## 6. What physical information the positive model uses

The model does not receive a \(24\)-entry endpoint table. It receives:

1. the classical octahedral control group;
2. its ordinary action on a direction or cube vertex;
3. the identification of the preparation/readout axis \(e_z\); and
4. a positive preparation and reader.

The word law then follows by group multiplication.

This is a real compression relative to an arbitrary table, but it is not a
derivation of the control representation from no structure. The ordinary
\(SO(3)\) covariance bridge is a physical input just as PC3's projective
\(PU(2)\) bridge was a physical input. At this finite operational scope, the
two bridges lie in the same empirical fiber.

The comparison is therefore:

| Coordinate | PC3 coherent model | PC4 positive model |
|---|---|---|
| primitive endpoint carrier | two configurations | two registered configurations |
| internal carrier | complex two-vector representation | 6 directions or 8 cube vertices |
| control action | projective \(PU(2)\) | ordinary permutation/\(SO(3)\) |
| composition | matrix multiplication | group action composition |
| completed endpoints | \(4I_2/4X/16G\) | \(4I_2/4X/16G\) |
| intermediate positive division | not supplied by PC3 lift | present on enlarged carrier |
| selected by current experiment | no | no |

The extra positive carrier is not automatically a literal apparatus memory
cost. It is an ontological and predictive-capacity input that must be charged
until an experiment or independent principle gives it physical meaning.

---

## 7. Primary-source relation

PC4 is not presented as discovery of a new classical simulation of the
single-qubit Clifford sector.

1. Spekkens' toy theory demonstrates that an epistemic restriction over
   ordinary ontic states can reproduce many quantum-like effects while
   failing at Bell and Kochen--Specker phenomena:
   <https://arxiv.org/abs/quant-ph/0401052v2>.
2. Wallman and Bartlett construct nonnegative qubit subtheories on finite
   ontic spaces and show that single-qubit Clifford generators can supervene
   on permutations in the relevant stabilizer case:
   <https://arxiv.org/abs/1203.2652v2>.
3. Lillystone, Wallman, and Emerson show that the complete single-qubit
   stabilizer subtheory is generalized-contextual once operationally
   equivalent transformation implementations are included, although the
   contextuality can be confined to transformations:
   <https://arxiv.org/abs/1802.06121v2>.
4. Kocia and Love give another positive, state-independent description of
   Clifford propagation and identify the non-Clifford \(T\) gate as requiring
   additional structure in their formalism:
   <https://arxiv.org/abs/1705.08869v2>.

The exact PC4 contribution is narrower: it binds an explicit positive
dilation and a six-state minimum theorem to the already frozen author-side
PC3 endpoint battery, then states exactly why that battery is not an ontology
discriminator.

---

## 8. Why PC3 did not see transformation contextuality

PC3 registers pure reversible group elements and one final binary reader. It
does not register all convex mixtures of controls or identify distinct
implementations of the same operational channel.

The transformation-contextuality obstruction in the full single-qubit
stabilizer subtheory uses precisely such operational equivalences. Two
different random implementations of the completely depolarizing channel can
induce different hidden transitions even though their registered quantum
channel is the same.

That observation does not by itself refute a process ontology. A
history-sensitive theory may treat two implementations as physically
different if complete records or future interventions can distinguish them.
The v17 reality-identification rule therefore requires a future unit to print:

1. the complete experiment class under which the implementations are
   operationally equivalent;
2. whether implementation records are retained or erased;
3. whether future continuations can distinguish the implementations; and
4. whether noncontextuality is a derived invariance, an empirical fact, or a
   new postulate.

Without that typing, “contextual” would again be used as an ontology verdict
instead of a statement relative to an operational quotient.

---

## 9. The first real frontier beyond PC3

### 9.1 A non-Clifford gate is necessary but not sufficient

Adding a calibrated non-Clifford transformation such as \(T\) defeats the
finite cube permutation model. It does not defeat positivity in general. A
positive ontological model can carry a complete continuous Bloch direction,
the quantum state itself, or an equivalent response law. Such a model has
merely chosen the first branch of the v17 trilemma:

$$
\text{phase-complete predictive state}.
$$

The scientific question is therefore not whether one more gate breaks eight
states. It is where the missing predictive information goes and how it scales.

### 9.2 The next author-side target

The next U-Gen construction should extend the same calibrated interface in
two stages:

1. **implementation-equivalence control:** add registered mixtures and
   retained/erased records to locate transformation contextuality relative to
   a complete experiment class;
2. **Clifford-plus-resource displacement:** add one non-Clifford resource and
   classify whether each successful positive model pays through a
   phase-complete carrier, context, nonuniform advice, enlarged dynamics, or
   indivisible whole-program law.

The scalable version, not the finite witness alone, is the promotion-bearing
target. Montina's Markovian ontological-dimension theorem is a relevant
external comparator, but its assumptions must be reconstructed before use:
<https://arxiv.org/abs/0711.4770v2>.

### 9.3 Relation to Q-Cut

Q-Cut and PC4 address different branches:

$$
\begin{array}{ll}
\text{Q-Cut:}&
\text{charge a positive future-sufficient cut;}\\[1mm]
\text{PC4/U-Gen:}&
\text{test the enlarged-carrier or indivisible whole-law escape.}
\end{array}
$$

The PC4 positive model is exactly why Q-Cut cannot be replaced by a finite
composition example, and why Q-Cut cannot replace U-Gen.

---

## 10. Scope ceiling

The strongest current author-side claim is:

> The complete \(24\)-element PC3 endpoint law has an exact uniform
> ordinary-positive reversible realization on six ontic states, and an exact
> outcome-deterministic realization on eight cube vertices. Six states are
> minimal among finite reversible positive realizations with arbitrary
> stochastic binary response. Therefore the present PC3 endpoint experiment
> does not distinguish its projective coherent realization from enlarged
> positive dynamics.

No claim is earned about:

1. a selected ontology;
2. the full single-qubit stabilizer process theory;
3. arbitrary qubit quantum mechanics;
4. interacting or many-body systems;
5. the impossibility of positive histories;
6. Barandes' complete indivisible stochastic framework;
7. QFT;
8. internal time;
9. spacetime; or
10. gravity.

---

## 11. Disposition

    PC3 ENDPOINT POSITIVE DILATION:       CONSTRUCTED EXACTLY AUTHOR-SIDE
    SIX-STATE STOCHASTIC MODEL:           PASS
    EIGHT-STATE DETERMINISTIC MODEL:      PASS
    FINITE REVERSIBLE MINIMUM:            SIX / AUTHOR-SIDE PROOF
    PROJECTIVE MODEL UNIQUENESS:          ONLY INSIDE ITS DECLARED BRIDGE CLASS
    ONTOLOGY DISCRIMINATION AT PC3:       FAILS
    FULL STABILIZER PROCESS PROFILE:      NOT TESTED
    NON-CLIFFORD RESOURCE DISPLACEMENT:   OPEN
    INDEPENDENT REVIEW:                   NOT AUTHORIZED / NOT RUN
    OFFICIAL UNIT:                        NOT OPENED
