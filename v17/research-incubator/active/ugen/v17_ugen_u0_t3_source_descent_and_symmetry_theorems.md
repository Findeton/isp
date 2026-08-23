# ISP v17 — U-Gen U0-T3 source-descent and symmetry theorems

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Candidate, implementation, or target data bound:** no

This file extracts the exact mathematical content of representation-neutral
source completion. It proves necessary conditions on any future U0 candidate.
It does not construct a native stochastic law, select an ontology, or open
U0-T4.

No configuration form is assumed. The finite bare-carrier theorem below is a
bounded diagnostic control, not a claim of fundamental discreteness.

---

## 0. Physical question

> If the same apparatus can be described with different labels, coordinates,
> units, gauges, or lossless encodings, what must a physical source-completion
> law do—and what can it never infer from those presentation choices?

The answer must preserve two facts:

1. labels and gauge cannot create dynamics;
2. genuine physical context cannot be erased merely because current
   calibration declares two procedures operationally similar.

---

## 1. Typed source-packet groupoid

Let $\mathsf P$ be a **verified neutral groupoid**.

An object $x\in\operatorname{Ob}(\mathsf P)$ is a target-blind physical source
packet:

$$
x=(X^0,A,\mathsf{Proc},\mathsf{Read},\mathsf{Prov}).
\tag{1}
$$

A morphism

$$
g:x\longrightarrow y
\tag{2}
$$

is admitted only when independent evidence establishes that it changes
presentation but no physical system, preparation, control, reader,
composition interface, or record event.

Each object has a measurable complete-record space

$$
(\mathcal R_x,\Sigma_x),
$$

and each $g:x\to y$ induces a measurable record isomorphism

$$
\rho_g:\mathcal R_x\longrightarrow\mathcal R_y
\tag{3}
$$

with

$$
\rho_{h\circ g}=\rho_h\circ\rho_g,
\qquad
\rho_{\mathrm{id}_x}=\mathrm{id}_{\mathcal R_x}.
\tag{4}
$$

The candidate nomology $\mathcal N$ assigns a complete ordinary-positive law

$$
F_{\mathcal N}(x)\in\mathcal P(\mathcal R_x).
\tag{5}
$$

Whole-program dependence is allowed. Equations (1)--(5) impose no Markov
factorization through intermediate configurations.

---

## 2. Definition of source descent

### Definition SD.1 — neutral equivariance

$F_{\mathcal N}$ **descends through verified presentation** when, for every
$g:x\to y$,

$$
F_{\mathcal N}(y)
=
(\rho_g)_*F_{\mathcal N}(x).
\tag{6}
$$

Equivalently, after undoing the record relabeling, the two predictions are the
same physical law:

$$
(\rho_{g^{-1}})_*F_{\mathcal N}(y)
=
F_{\mathcal N}(x).
\tag{7}
$$

This is representation covariance. It is not the stronger assertion that all
operationally equivalent physical procedures have the same ontic
representation.

### Definition SD.2 — aligned target distance

Let $Q_x$ and $Q_y$ be complete target laws and let $d$ be a metric on
probability laws invariant under measurable record isomorphisms. Define

$$
\Delta_g(Q_x,Q_y)
=
d\!\left(
Q_x,
(\rho_{g^{-1}})_*Q_y
\right).
\tag{8}
$$

Total variation is one admissible bounded-fixture choice. The theorem does
not require that choice.

---

## 3. The orbit-mismatch theorem

### Theorem SD.A — neutral-equivalent packets cannot support unequal aligned predictions

Let $g:x\to y$ be a verified neutral morphism and let $F_{\mathcal N}$ satisfy
(6). If

$$
\Delta_g(Q_x,Q_y)=\Delta>0,
\tag{9}
$$

then

$$
\max\!\left\{
d(F_{\mathcal N}(x),Q_x),
d(F_{\mathcal N}(y),Q_y)
\right\}
\ge \frac{\Delta}{2}.
\tag{10}
$$

### Proof

By equivariance and metric invariance,

$$
d(F_{\mathcal N}(y),Q_y)
=
d\!\left(
F_{\mathcal N}(x),
(\rho_{g^{-1}})_*Q_y
\right).
\tag{11}
$$

The triangle inequality gives

$$
\Delta
\le
d(Q_x,F_{\mathcal N}(x))
+
d\!\left(
F_{\mathcal N}(x),
(\rho_{g^{-1}})_*Q_y
\right).
\tag{12}
$$

At least one term is at least $\Delta/2$. $\square$

### Physical meaning

A failed pair does not immediately refute the nomology. It proves that at
least one of the following is true:

1. the declared transformation was not physically neutral;
2. a target-relevant physical descriptor was omitted;
3. the target or record alignment is wrong;
4. the implementation drifted;
5. the candidate violates representation descent; or
6. the target evidence is inconsistent at the printed tolerance.

Changing a label-dependent branch cannot repair the physics.

---

## 4. The automorphism fixed-point theorem

### Theorem SD.B — self-symmetries constrain the complete law

For an object $x$, let

$$
G_x=\operatorname{Aut}_{\mathsf P}(x).
\tag{13}
$$

If $F_{\mathcal N}$ descends, then

$$
F_{\mathcal N}(x)
\in
\operatorname{Fix}(G_x)
\equiv
\left\{
Q\in\mathcal P(\mathcal R_x):
(\rho_g)_*Q=Q\ \forall g\in G_x
\right\}.
\tag{14}
$$

### Proof

Apply (6) to each $g:x\to x$. $\square$

This is the exact sense in which verified symmetry constrains a source law.
It does not say that the fixed-point set is a singleton.

---

## 5. Covariance nonselection

### Theorem SD.C — symmetry selects only when its admissible fixed set is unique

Let $\mathcal A_x\subseteq\mathcal P(\mathcal R_x)$ be the laws satisfying all
other printed conditions: normalization, state, complete-record, division,
composition, resource, and provenance constraints. If

$$
\left|
\mathcal A_x\cap\operatorname{Fix}(G_x)
\right|
\ge 2,
\tag{15}
$$

then neutral covariance alone does not select a unique complete-process law.

### Proof

Every member of the intersection satisfies all stated constraints, including
covariance. A condition shared by at least two distinct members cannot choose
one of them without an additional rule. $\square$

### Consequence

“Derived from symmetry” is incomplete unless the uniqueness proof prints:

1. the exact symmetry group;
2. the full admissible class;
3. every additional regularity/composition premise;
4. the contingent state;
5. the uniqueness argument; and
6. the physical origin of every premise.

Framework covariance must not be reported as dynamical selection.

---

## 6. Exact finite bare-carrier classification

This section asks what an anonymous finite carrier can support before any
physical relation, control action, reader structure, or geometry is supplied.

Let

$$
\mathcal C_n=\{1,\ldots,n\},
\qquad n\ge 2,
\tag{16}
$$

and declare every permutation $\pi\in S_n$ neutral. Let $\Gamma$ be a
column-stochastic one-step law satisfying simultaneous relabeling covariance:

$$
\Gamma_{\pi(i)\pi(j)}=\Gamma_{ij}
\qquad
\forall i,j,\ \forall\pi\in S_n.
\tag{17}
$$

### Theorem SD.D — bare finite covariance leaves one free persistence parameter

Every $\Gamma$ satisfying (17) has the form

$$
\Gamma_{ij}
=
\begin{cases}
a, & i=j,\\[2mm]
b, & i\ne j,
\end{cases}
\qquad
a+(n-1)b=1,
\tag{18}
$$

where

$$
0\le a\le 1,
\qquad
b=\frac{1-a}{n-1}.
\tag{19}
$$

Conversely, every matrix (18)--(19) is column-stochastic and
$S_n$-covariant.

### Proof

The diagonal action of $S_n$ on ordered pairs $(i,j)$ has exactly two orbits:
the diagonal $i=j$ and the off-diagonal $i\ne j$. Equation (17) therefore
forces one value $a$ on the first orbit and one value $b$ on the second.
Column normalization gives $a+(n-1)b=1$. Nonnegativity gives (19). The
converse is immediate. $\square$

### What the theorem does not say

1. it does not force $a$ to a unique value;
2. it does not make the process quantum;
3. it does not forbid whole-history indivisibility;
4. it does not imply that nature is finite; and
5. it does not show that every structured carrier reduces to (18); and
6. if an independently physical invariant $lambda$ is supplied, it does not
   forbid $a=a(\lambda)$—but covariance still does not select that function.

It shows exactly why an anonymous set is not yet a physical interaction law.

---

## 7. Whole-history bare-carrier corollary

Let a length-$k$ configuration history be

$$
h=(i_1,\ldots,i_k)\in\mathcal C_n^k
\tag{20}
$$

and let a whole-process law satisfy

$$
P(\pi i_1,\ldots,\pi i_k)=P(i_1,\ldots,i_k)
\qquad
\forall\pi\in S_n.
\tag{21}
$$

### Corollary SD.D.1 — only equality patterns survive anonymous relabeling

$P(h)$ can depend only on the orbit of $h$, equivalently on which positions
$r,s$ satisfy $i_r=i_s$, subject to the carrier-size bound.

### Proof

Two tuples lie in the same diagonal $S_n$ orbit exactly when their entries
have the same equality pattern, provided the required distinct values fit in
$\mathcal C_n$. Equation (21) makes $P$ constant on each such orbit.
$\square$

Thus even a genuinely indivisible anonymous-carrier law may contain
non-Markov correlations among complete histories, but it cannot acquire
label-specific physical meaning from the names $1,\ldots,n$.

Controls, readers, relations, or boundary data can break this orbit structure
only when they are physically typed rather than inserted as target advice.

---

## 8. Symmetry-resolution ledger

### Theorem SD.E — a non-invariant ensemble needs a printed physical asymmetry

Let $g\in G_x$ and suppose the target law obeys

$$
(\rho_g)_*Q_x\ne Q_x.
\tag{22}
$$

No descending predictor on the unchanged packet $x$ can equal $Q_x$.

### Proof

Theorem SD.B requires every descending prediction on $x$ to be fixed by $g$,
contradicting (22). $\square$

A legitimate resolution must occupy at least one of these ledger rows:

| resolution | exact change |
|---|---|
| physical apparatus asymmetry | $g$ is not an automorphism of the fully described packet |
| contingent boundary or sector | the extended state $(x,b)$ transforms and is not fixed |
| nomological asymmetry | $g$ was never a symmetry of the fixed law |
| invariant mixture | the ensemble remains symmetric although individual histories need not |
| classification correction | the purportedly neutral transformation was unresolved or physical |

An arbitrary gauge fixing, label order, memory address, or code iteration
order occupies none of these rows.

---

## 9. Spontaneous asymmetry is not law selection

### Proposition SD.F — asymmetric actual histories can coexist with an invariant law

Let $Q\in\operatorname{Fix}(G_x)$. For an event $A\subseteq\mathcal R_x$,

$$
Q(A)=Q(\rho_g A)
\qquad
\forall g\in G_x.
\tag{23}
$$

Individual histories in $A$ need not be fixed by $g$.

### Proof

Equation (23) is exactly the pushforward invariance of $Q$. A measure can be
invariant while its individual sample points form nontrivial group orbits.
$\square$

Observing one asymmetric record therefore does not prove that the nomology
breaks the symmetry. Predicting unequal sector frequencies requires a
contingent sector distribution, a law-level asymmetry, or a physical
selection mechanism.

---

## 10. Marginals do not generate an interacting parent

The source-completion problem also appears at composition.

### Theorem SD.G — component laws generically underdetermine the joint law

Let $X,Y\in\{0,1\}$ have fixed marginal probabilities

$$
P(X=1)=p,
\qquad
P(Y=1)=q.
\tag{24}
$$

The joint probability

$$
r=P(X=1,Y=1)
\tag{25}
$$

may take any value in the Fréchet interval

$$
\max(0,p+q-1)
\le r\le
\min(p,q).
\tag{26}
$$

Except when this interval collapses, the component laws do not determine the
parent.

### Proof

The four joint probabilities are

$$
r,\quad p-r,\quad q-r,\quad 1-p-q+r.
\tag{27}
$$

Their nonnegativity is equivalent to (26), and every allowed $r$ defines a
normalized joint law with the required marginals. $\square$

### Physical consequence

The product member $r=pq$ is licensed only by an independently verified
noninteraction premise. An interacting parent needs:

1. a physically described composition interface;
2. target-blind coupling data;
3. one invariant parent-generation rule; and
4. held-out joint records.

Cartesian-product kinematics, subsystem marginals, covariance, and ordinary
probability do not by themselves generate entangling or interacting
statistics.

---

## 11. Neutral refinement consistency

Suppose

$$
r:x'\longrightarrow x
\tag{28}
$$

is declared a neutral refinement or alternative description and induces a
record coarse-graining

$$
c_r:\mathcal R_{x'}\longrightarrow\mathcal R_x.
\tag{29}
$$

A consistent predictor must satisfy

$$
(c_r)_*F_{\mathcal N}(x')
=
F_{\mathcal N}(x).
\tag{30}
$$

Equation (30) is required only when the refinement is proved physically
neutral. Adding a sensor, resolving a previously hidden material coordinate,
or changing the apparatus is not automatically a neutral refinement.

This prevents discretization, mesh choice, database schema, and hidden-state
resolution from changing predictions solely through representation.

---

## 12. Independent-composition square

For independently prepared systems with a certified no-interaction program,
let $\boxtimes$ denote the physical packet composition and $\otimes_{\rm prob}$
the product of record laws. Source completion must satisfy

$$
F_{\mathcal N}(x\boxtimes y)
=
F_{\mathcal N}(x)\otimes_{\rm prob}F_{\mathcal N}(y)
\tag{31}
$$

at the registered accuracy.

For an interacting packet $x\boxtimes_\kappa y$, equation (31) is not imposed.
Instead the same nomology must use the independently described coupling
$\kappa$ to generate the parent. Supplying a separate parent table is target
import.

This square is operational. It does not assert that microscopic
configurations form Cartesian products or Hilbert tensor products.

---

## 13. Candidate entry contract implied by the theorems

Any eventual U0-T4 candidate must provide:

1. a typed packet category and verified neutral subgroupoid;
2. record transports $\rho_g$;
3. proof of (6) or a preregistered counterexample status;
4. the fixed-point sets relevant to each claimed symmetry;
5. every physical symmetry breaker and its ledger class;
6. a contextuality firewall separating presentation from physical procedure;
7. contingent state and nomology as distinct objects;
8. the independent-composition square and interacting-parent rule;
9. neutral-refinement consistency;
10. a target-blind source-identifiability calculation;
11. a no-refit transfer implementation; and
12. complete resource and provenance accounting.

This contract does not authorize candidate construction.

---

## 14. Hostile battery

1. hidden-label permutation changes the prediction;
2. record relabeling is not transported;
3. units change a dimensionless probability;
4. gauge fixing supplies a preferred orientation;
5. serial number selects a law branch;
6. code iteration order becomes chronology;
7. mesh refinement changes a supposedly continuum prediction;
8. coarse-graining is declared neutral despite adding or deleting a reader;
9. every calibration equivalence is forced to be ontic equivalence;
10. a physical contextual difference is left unmeasured;
11. symmetry is cited without a fixed-set calculation;
12. two symmetric members survive but one is called derived;
13. an asymmetric sample is called asymmetric dynamics;
14. a contingent sector is moved into the nomology;
15. a nomological asymmetry is hidden in a label convention;
16. a bare carrier receives arbitrary transition weights;
17. finite-carrier equality patterns are promoted to fundamental atoms;
18. component marginals are said to determine interaction;
19. product composition is used despite a common source;
20. an interacting parent table is inserted by hand;
21. Cartesian product or Hilbert tensor product is imported as ontology;
22. Markov composition is imposed at an unrecorded seam;
23. candidate changes the neutral group after target opening;
24. transfer implementation receives a new invariant parameter;
25. a contextual identifier carries target advice;
26. an unresolved transformation is scored as a passed symmetry test;
27. covariance under laboratory presentation is called general covariance;
28. the locally covariant QFT analogy is used to import spacetime;
29. a reconstruction axiom is called empirical derivation; and
30. failure of source descent is called proof of Hilbert ontology.

---

## 15. Outcome ladder

| outcome | meaning |
|---|---|
| SD-R0 ILL-TYPED | packet, record transport, or transformation class is undefined |
| SD-R1 NON-DESCENDING | a verified neutral change alters the aligned prediction |
| SD-R2 OVERQUOTIENTED | a physically unresolved/contextual difference was declared neutral |
| SD-R3 BARE-CARRIER UNDERDETERMINED | only anonymous-carrier invariants are supplied and multiple laws remain |
| SD-R4 SYMMETRY-UNDERSELECTED | multiple admissible fixed-point laws survive |
| SD-R5 SOURCE-STRUCTURED | target-blind physical relations support an evaluable descending source map |
| SD-R6 TRANSFER-READY | SD-R5 plus no-refit descent on an unknown second implementation |

SD-R5/R6 are candidate-entry conditions, not evidence that the predicted law
is correct.

---

## 16. Physical conclusion

The exact lesson is neither “relations are enough” nor “relations fail.”

An anonymous carrier plus permutation invariance yields only orbit data. In
the finite one-step control it leaves the free parameter $a$ in (18); in a
whole-history law it leaves arbitrary weights on equality-pattern orbits.
Indivisibility does not remove that selection debt.

A viable ontology must therefore say what the physical relations are, how
preparations and interventions transform them, how readers form records, and
which parts are contingent. Those structures may be discrete, continuous, or
neither. What is forbidden is obtaining them from labels or from the held-out
quantum answer.

---

## 17. Present disposition

~~~text
SOURCE DESCENT:                       EXACT NECESSARY CONDITION / AUTHOR-SIDE
ORBIT-MISMATCH BOUND:                PROVED
AUTOMORPHISM FIXED-POINT CONDITION:  PROVED
COVARIANCE AS UNIQUE SELECTOR:       REFUTED IN GENERAL
FINITE BARE-CARRIER CLASSIFICATION:  PROVED / BOUNDED CONTROL
WHOLE-HISTORY EQUALITY PATTERNS:     PROVED / NO MARKOV ASSUMPTION
SPONTANEOUS ASYMMETRY:               COMPATIBLE WITH INVARIANT ENSEMBLE
MARGINAL-TO-PARENT SELECTION:        UNDERDETERMINED IN GENERAL
CONFIGURATION FORM:                  UNSELECTED
PHYSICAL RELATIONAL STRUCTURE:       REQUIRED / NOT YET CHOSEN
NATIVE LAW:                          ABSENT
U0-T4:                               CLOSED / NOT AUTHORIZED
IMPLEMENTATION / TARGET:             UNBOUND
PIN / REVIEW / SCIENTIFIC RESULT:    NONE
~~~

---

## 18. Authority wall

These theorems do not authorize:

1. a native candidate or U0-T4 contest;
2. an apparatus, target acquisition, or hardware programme;
3. a configuration ontology;
4. an official pin or independent review;
5. a successor paper;
6. a spacetime, QFT, clock, or gravity construction;
7. empirical or ontological selection; or
8. an automatic repair chain.

---

## 19. Maximum legitimate claim

> Any native source-completion law must descend through verified neutral
> presentations. This yields an exact orbit-mismatch bound, automorphism
> fixed-point condition, and covariance nonselection theorem. A bare finite
> carrier supports only a one-parameter relabeling-covariant one-step family,
> while an indivisible whole-history law can depend only on equality-pattern
> orbits until physical structure is added. Component laws likewise do not
> generate an interacting parent. Therefore configuration neutrality cannot
> mean structurelessness: a successful law needs independently physical,
> target-blind relational structure. No such native law is constructed or
> ruled out here.
