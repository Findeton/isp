# ISP v17 — U-Gen U0 dynamical complex-structure gate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS/SOURCE GATE / NO CANDIDATE
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review/U0-T4 opened:** no

The reflection-positive control proves that a positive whole-law packet can
place Hilbert space downstream. The Barandes Markovian-embedding audit proves
that isolated endpoint positivity does not force a complex carrier. This file
asks the next exact question:

> If a native positive law first reconstructs a real predictive Hilbert space
> and one coherent reversible physical flow, does that flow select a complex
> structure rather than merely permit one?

At finite scope the answer is conditionally yes for one oriented flow. On the
nonstationary sector, the polar factor of a real skew generator is a unique
orthogonal complex structure once that generator is required to have a
positive-frequency factorization. For a family of interventions, however,
the correct question is whether their generators have a common complex
structure in their joint commutant. It is not whether every intervention has
the same polar factor.

That result is not yet quantum physics. A classical measure-preserving flow
has the same Koopman property. Stationary sectors remain unselected, time
reversal sends $J$ to $-J$, a family may admit many common complex structures
or none, and a reflection-positive semigroup does not produce the required
real reversible flow without a complexification or doubling step. The source
law and complete operational interface remain the load-bearing missing
objects.

No Hilbert, time, continuum, deterministic, reversible, Poincaré, field,
trajectory, lattice, or complex ontology is inherited by U0. This is a gate
for a future native proposal, not that proposal.

---

## 1. Version-bound source boundary

The physical interpretation is checked against these sources, accessed on
2026-08-23:

1. Valter Moretti and Marco Oppio,
   [*Quantum Theory in Real Hilbert Space: How the Complex Hilbert Space
   Structure Emerges from Poincaré Symmetry*](https://arxiv.org/abs/1611.09029),
   *Reviews in Mathematical Physics* **29**, 1750021 (2017).
2. B. O. Koopman,
   [*Hamiltonian Systems and Transformation in Hilbert
   Space*](https://www.pnas.org/doi/pdf/10.1073/pnas.17.5.315),
   *Proceedings of the National Academy of Sciences* **17**, 315--318
   (1931).
3. Maxim Kontsevich and Graeme Segal,
   [*Wick Rotation and the Positivity of Energy in Quantum Field
   Theory*](https://arxiv.org/abs/2105.10161),
   arXiv:2105.10161.
4. Jacob A. Barandes,
   [*A Deflationary Account of Quantum Theory and its Implications for the
   Complex Numbers*](https://arxiv.org/html/2602.01043v1),
   arXiv:2602.01043v1.
5. Jacob A. Barandes,
   [*Quantum Systems as Indivisible Stochastic
   Processes*](https://arxiv.org/html/2507.21192v1),
   arXiv:2507.21192v1.
6. Konrad Osterwalder and Robert Schrader,
   [*Axioms for Euclidean Green's Functions*](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/Axioms-for-Euclidean-Greens-functions/cmp/1103858969.pdf),
   *Communications in Mathematical Physics* **31**, 83--112 (1973).

The exact finite-dimensional theorems below are proved directly. The sources
support the following surrounding distinctions:

1. real Hilbert-space quantum theories can acquire a symmetry-invariant
   complex structure under strong Poincaré, irreducibility, and spectral
   premises;
2. measure-preserving classical dynamics already induce Hilbert-space
   isometries through Koopman representation;
3. positive energy and analytic continuation are substantial physical and
   analytic restrictions;
4. Barandes treats complex Hilbert ingredients as secondary gauge-dependent
   appurtenances to a supplied stochastic law; and
5. reflection positivity reconstructs Hilbert structure conditionally but
   does not generate its Euclidean measure or physical time reflection.

Moretti--Oppio begin with a real-Hilbert quantum system, a Poincaré
representation, an observable algebra, and elementary-system premises. Their
result is a major positive control for complex-structure emergence; it is not
a source-completion theorem for U0 and does not derive Poincaré spacetime.

---

## 2. Definition — real coherent physical flow

Let $(V,g)$ be a finite-dimensional real Hilbert space. A **real coherent
flow** is a differentiable homomorphism

$$
O:\mathbb R\longrightarrow O(V,g),
\qquad
O(t+s)=O(t)O(s),
\qquad
O(0)=I.
$$

Its generator is

$$
A=\left.\frac{d}{dt}O(t)\right|_{t=0},
$$

so

$$
A^*=-A,
\qquad
O(t)=e^{tA}.
$$

Here $t$ is only the supplied one-parameter group coordinate. The mathematics
does not establish that it is an external time, an internal clock reading, or
any other physical parameter. Its operational meaning and orientation must be
generated or calibrated by a candidate law.

The word *physical* is not earned by these equations. A U0 candidate must
additionally show that $V$, $g$, and $O(t)$ descend from its target-blind
positive source law and licensed interventions. A target-built feature space
or independently selected lift remains a representation.

Decompose

$$
V=V_0\oplus V_{\rm mov},
\qquad
V_0=\ker A,
\qquad
V_{\rm mov}=V_0^\perp.
$$

On $V_{\rm mov}$, $A$ is invertible.

---

## 3. Theorem DCS-A — polar dynamics selects a complex structure on the moving sector

Define on $V_{\rm mov}$ the nonnegative frequency operator

$$
\Omega=|A|=(A^*A)^{1/2}=(-A^2)^{1/2}
$$

and

$$
J=A|A|^{-1}.
$$

Then:

$$
J^2=-I,
\qquad
J^*=-J,
\qquad
J^*J=I,
$$

$$
[J,\Omega]=0,
\qquad
A=J\Omega,
\qquad
O(t)|_{V_{\rm mov}}=e^{tJ\Omega}.
$$

Thus $J$ is an orthogonal complex structure on the moving real space.

### Proof

Because $A$ is skew-adjoint,

$$
A^*A=-A^2.
$$

The positive operator $\Omega=(-A^2)^{1/2}$ is a function of $A^2$ and
therefore commutes with $A$. It is invertible on $V_{\rm mov}$. Hence

$$
J^2
=
A^2\Omega^{-2}
=
A^2(-A^2)^{-1}
=
-I.
$$

Also,

$$
J^*
=
\Omega^{-1}A^*
=
-\Omega^{-1}A
=
-A\Omega^{-1}
=
-J.
$$

Therefore

$$
J^*J=-J^2=I.
$$

Commutation and $A=J\Omega$ follow directly from the definition. $\square$

### Secondary complex Hilbert space

Declare multiplication by $i$ to be

$$
iv=Jv
$$

and define, with the convention linear in the second argument,

$$
\langle u,v\rangle_J
=
g(u,v)-i\,g(u,Jv).
$$

Then $V_{\rm mov}$ becomes a complex Hilbert space and $\Omega$ is
complex-linear
and self-adjoint. The same real flow becomes

$$
O(t)=e^{it\Omega}
$$

under this sign convention. Reversing the convention or time orientation
gives the familiar $e^{-it\Omega}$ form.

This is a representation theorem. It is not yet a Born rule, an observable
algebra, a complete process law, or an actuality statement.

Only after $t$ is physically identified as time and an action scale is
independently supplied may one define a Hamiltonian such as
$H_{\rm phys}=\hbar\Omega$. Neither that identification nor $\hbar$ follows
from the polar decomposition.

### Infinite-dimensional scope note

For a strongly continuous orthogonal one-parameter group on a real Hilbert
space, the skew-adjoint generator has a polar decomposition whose partial
isometry restricts to an orthogonal complex structure on
$(\ker A)^\perp$. The same zero-mode and orientation qualifications remain,
but unbounded domains and spectral questions enter. The finite theorem above
is the exact result used by this packet; no QFT or continuum conclusion is
claimed from the extension.

---

## 4. Theorem DCS-B — uniqueness under positive-frequency factorization

Suppose another pair $(K,B)$ on $V_{\rm mov}$ satisfies

$$
K^2=-I,
\qquad
K^*=-K,
$$

$$
B=B^*>0,
\qquad
[K,B]=0,
$$

and

$$
A=KB.
$$

Then

$$
\boxed{K=J,\qquad B=\Omega}.
$$

### Proof

Using $K^*K=I$ and $[K,B]=0$,

$$
A^*A
=(KB)^*(KB)
=B^2.
$$

The positive square root is unique, so

$$
B=(A^*A)^{1/2}=\Omega.
$$

Then

$$
K=A\Omega^{-1}=J.
\qquad\square
$$

### Meaning

The dynamics does not merely admit an arbitrary imaginary unit. Given the
oriented generator and the requirement that the residual generator be
positive, its moving sector selects one $J$. Here that residual operator is
$\Omega=|A|$; writing it as a physical Hamiltonian requires the extra time
and action-scale identifications stated above.

The phrase “positive frequency” is mathematical relative to the oriented
group parameter. Calling it “positive energy” adds physical interpretation.
The theorem does not prove that $|A|$ is nature's energy, supply its units,
select the direction called future, or show that the flow is fundamental.

---

## 5. Theorem DCS-C — stationary sectors remain unselected

On

$$
V_0=\ker A,
$$

the polar factor is undefined. The flow supplies no orientation because

$$
O(t)v=v
$$

for all $v\in V_0$.

In finite dimensions:

1. if $\dim V_0$ is odd, no complex structure exists on all of $V_0$;
2. if $\dim V_0=2m>0$, many orthogonal complex structures exist; and
3. no one of them is selected by $A=0$.

Therefore a dynamical complex structure is complete only if stationary/null
sectors are absent, gauge, physically real with separately generated
structure, or coupled to additional source-generated controls that resolve
them.

This is not a technical corner. Vacuum, conserved, superselection, gauge, and
zero-frequency sectors can be physically important.

---

## 6. Theorem DCS-D — reversing the flow complex-conjugates the structure

For the reversed flow

$$
O_{\rm rev}(t)=O(-t),
$$

the generator is

$$
A_{\rm rev}=-A.
$$

Its positive factor remains

$$
|A_{\rm rev}|=|A|=\Omega,
$$

while its polar complex structure is

$$
J_{\rm rev}=-J.
$$

The complex Hilbert structures defined by $J$ and $-J$ are conjugate. Thus
the unoriented flow determines at most the pair

$$
\{J,-J\}.
$$

A fundamental sign requires a physical time orientation, positive-frequency
condition, asymmetric contingent state, or equivalent operational input. The
direction in which a program, category, or proof is written cannot supply it.

---

## 7. Exact frequency-origin and phase-gauge control

Let

$$
J_0=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$

and on $V=\mathbb R^4$ take

$$
J=J_0\oplus J_0,
$$

$$
A
=
\omega_1J_0\oplus\omega_2J_0,
\qquad
0<\omega_1<\omega_2.
$$

Then

$$
\Omega=\omega_1I_2\oplus\omega_2I_2,
\qquad
A=J\Omega.
$$

For a real number $c$, define

$$
A_c=A+cJ=J(\Omega+cI).
$$

Once $J$ is used to identify complex rays,

$$
e^{tA_c}=e^{ctJ}e^{tA}
$$

differs by a common complex phase and gives identical ray-transition
probabilities. Yet for

$$
-\omega_2<c<-\omega_1,
$$

the polar factor of $A_c$ flips on exactly one real rotation plane. At either
threshold $A_c$ acquires a kernel.

The control establishes two distinct statements.

1. **Positive-frequency branch:** if $\Omega+cI>0$ is imposed, the polar
   structure remains $J$.
2. **Ray-data insufficiency:** transition probabilities alone do not determine
   an absolute energy origin or the representative generator before the
   positive-frequency/gauge convention is fixed.

If the parameter and action scale are later identified with physical time and
action, this becomes the familiar additive-energy control. In
nongravitational quantum physics a common additive energy constant is normally
operationally irrelevant. Whether absolute energy gravitates is a later MG0
question and is not used here to select $J$.

---

## 8. Theorem DCS-E — the family gate is a joint-commutant problem

For a family of coherent generators

$$
\mathcal A=\{A_c:c\in\mathcal C\},
$$

define its compatible complex structures by

$$
\mathfrak J(\mathcal A)
=
\left\{
K:K^*=-K,\ K^2=-I,\ [K,A_c]=0\text{ for every }c
\right\}.
$$

A member $K\in\mathfrak J(\mathcal A)$ makes every admitted coherent flow
complex-linear on the same carrier. This does **not** require $K$ to equal the
polar factor $A_c|A_c|^{-1}$ of every generator. General quantum Hamiltonians
need not be positive before a physically consistent energy-origin convention
is fixed.

### DCS-E1 — different polar factors can coexist with many common complex structures

Use the quaternion basis $(1,i,j,k)$ on $\mathbb R^4$. Define left
multiplication by $i$ and $j$:

$$
J_1=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix},
$$

$$
J_2=
\begin{pmatrix}
0&0&-1&0\\
0&0&0&1\\
1&0&0&0\\
0&-1&0&0
\end{pmatrix}.
$$

They satisfy

$$
J_1^2=J_2^2=-I,
\qquad
J_1^*=-J_1,
\qquad
J_2^*=-J_2,
$$

and

$$
J_1J_2=-J_2J_1.
$$

Let two licensed control flows have generators

$$
A_1=J_1,
\qquad
A_2=J_2.
$$

Each separately has positive polar factor $\Omega_a=I$ and a unique dynamical
complex structure $J_a$.

There is no single complex structure $J$ for which both admit factorizations

$$
A_a=J\Omega_a,
\qquad
\Omega_a>0,
$$

because Theorem DCS-B would force simultaneously

$$
J=J_1
\qquad\text{and}\qquad
J=J_2.
$$

Nevertheless, right multiplication by $i$ is represented by

$$
K=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
$$

It is an orthogonal complex structure and

$$
[K,J_1]=[K,J_2]=0.
$$

Right multiplication by every unit pure-imaginary quaternion gives another
such $K$. Hence $\mathfrak J(\{A_1,A_2\})$ is nonempty and nonunique even
though the two positive polar structures disagree.

This proves a correction that matters physically:

> Objectwise complex-structure extraction is not family-level quantum
> reconstruction.

### DCS-E2 — an exact family with no common complex structure

Let

$$
A_1=J_0\oplus 2J_0,
\qquad
C=\begin{pmatrix}1&0\\0&2\end{pmatrix},
$$

and

$$
A_2=
\begin{pmatrix}
0_2&C\\
-C&0_2
\end{pmatrix}.
$$

Both are real skew-adjoint generators. Since

$$
A_1^2=(-I_2)\oplus(-4I_2),
$$

any operator commuting with $A_1$ preserves the two displayed real planes.
An orthogonal complex structure on a real two-plane is $J_0$ or $-J_0$.
Consequently every candidate in $\mathfrak J(\{A_1\})$ has the form

$$
K_{\epsilon_1,\epsilon_2}
=
(\epsilon_1J_0)\oplus(\epsilon_2J_0),
\qquad
\epsilon_1,\epsilon_2\in\{-1,+1\}.
$$

Commutation with $A_2$ would require

$$
\epsilon_1J_0C=\epsilon_2CJ_0.
$$

But

$$
J_0C=
\begin{pmatrix}0&-2\\1&0\end{pmatrix}
\neq
\pm
\begin{pmatrix}0&-1\\2&0\end{pmatrix}
=\pm CJ_0.
$$

Therefore

$$
\boxed{\mathfrak J(\{A_1,A_2\})=\varnothing}.
$$

### Correct family-level requirement

A native law must generate a physically justified coherent family for which:

1. $\mathfrak J(\mathcal A)$ is nonempty;
2. source symmetries and composition reduce it to one conjugate pair
   $\{J,-J\}$, or the residual multiplicity is physically typed;
3. one independently oriented distinguished flow has its polar factor in that
   pair and selects the sign if the sign is operationally meaningful; and
4. every held-out coherent control and composite is compatible with that same
   $J$.

Discrete time-reversing symmetries may instead satisfy
$RJR^{-1}=-J$. They must be typed as anti-complex symmetries rather than
silently counted as incompatible continuous dynamics. Nonunitary instruments
also require a later positive-map/process reconstruction; orthogonal-flow
compatibility alone does not supply them.

---

## 9. Koopman control — complex structure is not sufficient for quantum physics

Let the ordinary classical configuration be a point

$$
\theta\in S^1
$$

with uniform probability and deterministic measure-preserving flow

$$
\theta\longmapsto\theta+\omega t.
$$

The Koopman action on real square-integrable observables is orthogonal. On

$$
V_1=\operatorname{span}_{\mathbb R}\{\cos\theta,\sin\theta\},
$$

its generator is, up to the convention for pullback direction,

$$
A_1=\omega J_0.
$$

Theorem DCS-A yields

$$
J=\operatorname{sgn}(\omega)J_0,
\qquad
\Omega=|\omega|I_2,
$$

and the complex mode $e^{i\theta}$ packages the two real modes naturally.

Nothing quantum has followed. The underlying event algebra remains
commutative, the configuration follows a deterministic divisible flow, and
ordinary conditioning remains valid. Koopman already teaches that Hilbert
space, unitary/orthogonal evolution, Fourier phase, and a dynamically natural
complex structure can all occur in classical physics.

The quantum burden therefore includes at least:

1. the nonclassical complete intervention algebra;
2. phase-sensitive composition across unrecorded seams;
3. contextual/Bell-complete composite predictions;
4. stable record and eraser behavior; and
5. source-generated member selection.

Complex structure is an important coordinate. It is not an ontology or a
quantum criterion by itself.

---

## 10. Reflection-positive control — avoid a circular derivation

Reflection positivity can reconstruct a real Hilbert quotient and a positive
Euclidean contraction semigroup

$$
e^{-tH}.
$$

But a real orthogonal Lorentzian flow of the form

$$
e^{tJH}
$$

still requires an oriented complex structure $J$, an equivalent real
doubling, or an independently physical reversible flow from which $J$ can be
extracted.

Consequently this argument is circular:

```text
complexify the OS Hilbert space
-> analytically continue to a unitary flow
-> forget the complex structure
-> recover that same complex structure from the real polar factor.
```

The polar theorem earns origin credit only when the real reversible flow is
generated independently of the target complex quantum description.

Conversely, if a positive law supplies a classical Koopman flow, the theorem
is noncircular but the result may remain classical. U0 needs both independent
origin and quantum-complete operational discrimination.

---

## 11. Barandes-facing interpretation

Barandes's deflationary claim is compatible with DCS-A:

1. a complex structure can be a secondary organization of real predictive
   dynamics;
2. $J$ need not be a material field or configuration variable;
3. reversing temporal orientation conjugates the representation; and
4. a fixed coherent family can make the complex choice less arbitrary than
   separate endpoint square-root lifts.

But the audited Barandes laws begin with the stochastic transition law and a
time parameter supplied. Sparse endpoint $\Gamma$ does not determine the real
orthogonal generator, its phase orientation, or a common control-family lift.
The Foldy--Wouthuysen freedom described by Barandes further warns that a
Hamiltonian representative is gauge dependent.

The theorem therefore sharpens rather than fills the source-completion map:

$$
(S,\sigma,c,R)
\xrightarrow{\text{native positive law}}
(V,g,O_c)
\xrightarrow{\text{polar compatibility}}
(\mathcal H_J,\Omega_c).
$$

The second arrow is now understood at finite scope. The first remains absent.

---

## 12. U0 admission ledger

Any proposal using dynamical complex-structure emergence must print:

| coordinate | required evidence |
|---|---|
| real predictive space | generated from physical positive law, not target feature engineering |
| inner product | operational/source origin and quotient/null interpretation |
| flow | one target-blind rule for all admitted settings and depths |
| reversibility | physical scope, approximation, and excluded irreversible operations |
| orientation | what distinguishes $J$ from $-J$ physically |
| stationary sector | exact treatment of $\ker A$ |
| frequency/energy | what the flow parameter means; whether $|A|$ is physical frequency; origin and action-scale evidence before calling it energy |
| family compatibility | compute $\mathfrak J(\mathcal A)$; distinguish common complex-linearity from equality of per-flow polar factors |
| reversing symmetries | type $RJR^{-1}=-J$ separately from coherent complex-linear dynamics |
| readers | how physical records descend from the real/complex representation |
| division | which seams admit ordinary restart and which retain coherence |
| actuality | which positive-law object happens; $J$ is not automatically a beable |
| resources | real dimension, doubling, memory, precision, context, and advice |

Passing DCS-A alone earns none of the later coordinates.

---

## 13. Hostile controls

A future candidate must survive at least:

1. **endpoint-lift mutant:** select $A$ after inspecting target endpoint
   probabilities;
2. **OS circularity:** complexify first and claim the recovered polar $J$ was
   derived from positivity alone;
3. **Koopman promotion:** infer quantum ontology from Hilbert/orthogonal
   classical dynamics;
4. **stationary-sector omission:** define $J=A|A|^{-1}$ on $\ker A$;
5. **time-sign laundering:** choose $J$ rather than $-J$ from notation order;
6. **positive-energy naming:** call $|A|$ physical energy without calibration
   or symmetry evidence;
7. **energy-zero omission:** ignore central phase/energy-shift equivalence;
8. **one-flow overreach:** extract $J$ from one calibration flow but never
   test held-out controls;
9. **per-flow-polar overconstraint:** demand the same positive polar factor
   from every Hamiltonian instead of testing their joint commutant;
10. **real-doubling laundering:** hide a supplied complex process in twice as
    many real coordinates;
11. **observable omission:** treat every real self-adjoint operator as a
    physical observable without a compatibility rule;
12. **Born-rule import:** append modulus square after constructing $J$ without
    deriving the reader law;
13. **Poincaré inheritance:** use fixed relativistic symmetry to claim emergent
    spacetime or gravity;
14. **irreducibility laundering:** invoke a symmetry-selection theorem without
    proving the physical sector is elementary/irreducible;
15. **reversibility promotion:** infer fundamental reversible ontology from a
    representation of one coherent sector;
16. **classical-event erasure:** ignore that the Koopman multiplication algebra
    remains commutative;
17. **source omission:** solve complex packaging while never generating the
    complete positive law;
18. **QFT/gravity overreach:** extrapolate finite polar mathematics to fields,
    gauge constraints, continuum control, or reciprocal geometry.
19. **commutant nonselection:** exhibit one common $J$ while ignoring a
    continuous family of equally compatible choices;
20. **antiunitary misclassification:** reject a typed reversing symmetry
    because it conjugates $J$ rather than commuting with it;
21. **parameter laundering:** call the supplied group coordinate physical
    time without an operational clock or source argument;
22. **family incompatibility:** enlarge or retune the carrier after finding
    $\mathfrak J(\mathcal A)=\varnothing$ without charging the new resource.
23. **controlwise complex patching:** assign unrelated $J_c$ to different
    controls and call the resulting collection one complex quantum theory.

---

## 14. Outcome ladder

```text
DCS-L0  polar or uniqueness theorem fails
DCS-L1  one real coherent flow selects J on its moving sector
DCS-L2  stationary, reversal, origin, joint-commutant, and Koopman controls survive
DCS-L3  one source-generated family has J-space {+J,-J} and a typed sign rule
DCS-L4  complete adaptive/composite quantum processes use that same J
DCS-L5  J is stable under QFT limits, gauge structure, and physical clocks
DCS-L6  an empirical or explanatory discriminator favors the construction
DCS-L7  reciprocal matter--geometry dynamics generates the required orientation
```

This packet reaches DCS-L2 author-side. It does not construct DCS-L3.

---

## 15. Routing consequence

The complex-number question is now more sharply located.

Complex structure need not be fundamental material ontology. It can be the
unique positive-frequency polar orientation of one real coherent flow, while
the whole coherent family fixes—or fails to fix—the common commutant in which
that orientation must live. But that statement becomes physically explanatory
only after one positive source law
independently generates:

1. the real predictive quotient;
2. the oriented coherent flow;
3. the common control-family compatibility;
4. the nonclassical intervention/composition behavior; and
5. the physical reader and actuality map.

The next native construction should therefore not postulate $U(1)$, $J$, a
wavefunction, or a target unitary. It should attempt to generate a real
source-closed complete-process family and test whether its compatible set
reduces to $\{J,-J\}$ across held-out controls, with any sign selector stated
physically. An empty or persistently nonunique common-$J$ set is a semantic
outcome, not a code defect.

This creates no candidate, official pin, review cycle, U0-T4, implementation,
clock, spacetime, QFT, or gravity result.

---

## 16. Present disposition

```text
ONE REAL ORTHOGONAL FLOW:           CANONICAL J ON MOVING SECTOR
POSITIVE-FACTOR UNIQUENESS:         EXACT FINITE THEOREM
STATIONARY SECTOR:                  UNSELECTED / MAY LACK J
TIME REVERSAL:                      J -> -J
FLOW PARAMETER / ENERGY:            ADDITIONAL PHYSICAL IDENTIFICATION
PER-FLOW POLAR EQUALITY:            NOT THE FAMILY CRITERION
JOINT-COMMUTANT J-SET:              MAY BE MANY OR EMPTY
ANTI-COMPLEX SYMMETRIES:            MUST BE TYPED SEPARATELY
CLASSICAL KOOPMAN CONTROL:          PASSES POLAR THEOREM / REMAINS CLASSICAL
REFLECTION-POSITIVE SEMIGROUP:      DOES NOT NONCIRCULARLY SUPPLY J ALONE
BARENDES COMPLEX APPURTENANCE:      COMPATIBLE IN PRINCIPLE / SOURCE ABSENT
SOURCE-GENERATED REAL FLOW FAMILY:  ABSENT
COMPLETE QUANTUM PROCESS:           ABSENT
CONFIGURATION FORM:                 UNSELECTED
MG0 / GRAVITY RESULT:               NONE
OFFICIAL PIN / REVIEW / U0-T4:      NONE
```

---

## 17. Maximum legitimate claim

> On the nonstationary sector of a finite-dimensional real orthogonal flow,
> the skew generator has a unique factorization $A=J|A|$ with $J$ an
> orthogonal complex structure and $|A|>0$. Reversing the supplied flow
> conjugates $J$, while stationary sectors remain unresolved. A control
> family must instead be tested through
> the common complex structures in its joint commutant: exact finite families
> can have many such structures or none, and equality of individual polar
> factors is not the correct criterion.
> Classical Koopman dynamics already satisfy the one-flow theorem, so this is
> neither a quantum criterion nor an ontology selection. It identifies a
> precise secondary-complexity route for U0: a target-blind positive law must
> first generate one real source-closed coherent family whose held-out
> controls and composites reduce the compatible set to a physically typed
> conjugate pair and exhibit the complete nonclassical process interface.
