# ISP v17 — U0 CRP first construction attempt

## Exact reversible Gibbs parent, secondary quantum process, and actuality split

**Status:** ACTIVE AUTHOR-SIDE CONSTRUCTION / ONE MODEL / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official candidate, pin, review, implementation, apparatus, chronology, spacetime, or gravity model:** none

---

## 0. Executive verdict

The selected cut-local reflection-positive architecture admits an exact,
nontrivial positive construction.

One reversible two-state Gibbs kernel and one positive two-system source
coupling generate:

1. a normalized ordinary-positive two-sided configuration law;
2. exact reflection positivity;
3. a secondary Hilbert space and Hamiltonian;
4. coherent endpoint darkening and stochastic nondivision after analytic
   continuation;
5. a positive source insertion whose secondary state is entangled; and
6. a secondary common-Hilbert CHSH value above the Bell-local bound and below
   Tsirelson's bound.

The same construction fails the native ontology test. Its directly sampled
positive process is reversible, Markov, and dissipative. The coherent controls
and noncommuting readers belong to the analytically continued secondary
Hilbert process, not to measurable record functions of the same positive
configuration sample. Direct local records of the positive process obey the
Bell bound. Context-by-context reflection positivity admits every positive
record law, including PR. Therefore reflection positivity does not select the
physical reader/composition bridge.

The result is:

$$
\boxed{
\begin{gathered}
\text{CRP MATHEMATICAL CONTROL: REACHES L2,}\\
\text{POSITIVE SOURCE OF SECONDARY ENTANGLEMENT: YES,}\\
\text{SAME-LAW POSITIVE ACTUALITY FOR QUANTUM CONTROLS: NOT REALIZED,}\\
\text{NATIVE U0 CANDIDATE: NOT ADMITTED.}
\end{gathered}}
\tag{CRP1-1}
$$

This is a semantic failure, not a software defect. It does not refute every
possible positive whole-boundary ontology. It shows that the strongest known
positive-first reconstruction still needs an additional physical law
identifying interventions, readers, and actuality across the Euclidean and
quantum layers. Adding that law would be a new scientific object, not a repair
of this construction.

---

## 1. Scope and dependency boundary

This attempt instantiates the architecture selected in
`v17_ugen_u0_single_candidate_architecture_selection.md`. It uses the
reflection-positive control, R1/native-gap synthesis, Barandes source audit,
QPB purification audit, QB Bell counterfamily, and WPR reciprocity audit as
hostile dependencies.

The exact model is finite only so every claim can be proved. It is not a
proposal that reality is a two-state lattice, a discrete web, a Markov chain,
or externally timed.

The construction asks one bounded question:

> When an ordinary-positive source law genuinely reconstructs coherent and
> Bell-violating Hilbert predictions, are those predictions also the complete
> physical record law of the same positive actual configurations?

The answer for this model is no.

---

## 2. One universal relational kernel

Let

$$
X=\{0,1\},
\qquad
z_x=(-1)^x.
\tag{CRP1-2}
$$

For a positive relational coupling $\kappa$, define

$$
K_\kappa(x,y)
=
\frac{e^{\kappa z_xz_y}}{2\cosh\kappa}.
\tag{CRP1-3}
$$

The same local rule rewards agreement and suppresses disagreement. No phase,
amplitude, Hamiltonian, wavefunction, or target record probability occurs in
(CRP1-3).

Choose the exact control value

$$
\kappa=\log 3.
\tag{CRP1-4}
$$

Then

$$
K
=
\begin{pmatrix}
9/10&1/10\\
1/10&9/10
\end{pmatrix}.
\tag{CRP1-5}
$$

$K$ is positive, row-stochastic, symmetric, and strictly positive definite.
Its stationary distribution is uniform,

$$
\pi=(1/2,1/2),
\tag{CRP1-6}
$$

and its normalized eigenvectors and eigenvalues are

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2},
\tag{CRP1-7}
$$

$$
K|+\rangle=|+\rangle,
\qquad
K|-\rangle=\frac45|-\rangle.
\tag{CRP1-8}
$$

This gives one compact positive member. The parameter $\kappa$ will later be
charged as a source input; no material descent is claimed.

---

## 3. Positive whole law and reflection positivity

Let

$$
\Omega=X^{\mathbb Z}
\tag{CRP1-9}
$$

and let $\mu_K$ be the stationary two-sided Markov law with transition $K$.
Define reflection by

$$
(\vartheta\omega)_n=\omega_{-n}.
\tag{CRP1-10}
$$

Let $\mathcal A_+$ be the bounded cylinder functions of
$\omega_0,\omega_1,\ldots$.

### Theorem CRP1-A — exact reflection positivity

For every $F\in\mathcal A_+$,

$$
\int_\Omega
\overline{F(\vartheta\omega)}F(\omega)
\,d\mu_K(\omega)
\ge0.
\tag{CRP1-11}
$$

### Proof

Condition on $\omega_0=x$. Reversibility makes the conditional past and
future laws identical; the Markov property makes them conditionally
independent. Hence

$$
\mathbb E
[\overline{F\circ\vartheta}F\mid\omega_0=x]
=
|\mathbb E[F\mid\omega_0=x]|^2.
\tag{CRP1-12}
$$

Averaging with $\pi_x\ge0$ proves (CRP1-11). $\square$

The quotient map

$$
J(F)(x)=\mathbb E[F\mid\omega_0=x]
\tag{CRP1-13}
$$

identifies the secondary space as

$$
\mathcal H_{\rm OS}
\cong
L^2(X,\pi;\mathbb C)
\cong\mathbb C^2.
\tag{CRP1-14}
$$

Thus Hilbert space is genuinely downstream of a positive whole law plus the
reflection/cut packet.

---

## 4. Secondary Hamiltonian and coherent endpoint family

Because $K$ is strictly positive, define

$$
H=-\log K.
\tag{CRP1-15}
$$

Writing

$$
\epsilon=\log\frac54,
\tag{CRP1-16}
$$

gives

$$
H
=
\epsilon|-\rangle\langle-|
=
\frac{\epsilon}{2}(I-X).
\tag{CRP1-17}
$$

Positive integer translation reconstructs

$$
K^n=e^{-nH}.
\tag{CRP1-18}
$$

Analytic continuation defines

$$
U(t)=e^{-itH}
=
e^{-i\epsilon t/2}e^{i\epsilon tX/2}.
\tag{CRP1-19}
$$

The secondary endpoint transition law in the configuration basis is

$$
\Gamma(t)
=
|U(t)|^{\odot2}
=
\begin{pmatrix}
\cos^2(\epsilon t/2)&\sin^2(\epsilon t/2)\\
\sin^2(\epsilon t/2)&\cos^2(\epsilon t/2)
\end{pmatrix}.
\tag{CRP1-20}
$$

All entries of $\Gamma(t)$ are ordinary probabilities. The relation among
different $t$ values is carried by $U$, not by stochastic multiplication of
$\Gamma$.

---

## 5. Exact scalar separation

The directly sampled positive Markov process and the secondary coherent
process make sharply different predictions.

For the positive process,

$$
(K^n)_{00}
=
\frac12\left[1+\left(\frac45\right)^n\right]
>\frac12.
\tag{CRP1-21}
$$

It relaxes monotonically and never makes the stay record dark.

For the secondary process, let

$$
t_{\rm dark}=\frac{\pi}{\epsilon}.
\tag{CRP1-22}
$$

Then

$$
\Gamma_{00}(t_{\rm dark})=0,
\qquad
\Gamma_{10}(t_{\rm dark})=1.
\tag{CRP1-23}
$$

At the half interval,

$$
\Gamma(t_{\rm dark}/2)
=
\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{CRP1-24}
$$

Therefore

$$
\Gamma(t_{\rm dark})
\ne
\Gamma(t_{\rm dark}/2)^2.
\tag{CRP1-25}
$$

This is an exact indivisibility witness for the secondary endpoint family.
It is not an indivisibility witness for $\mu_K$, which is Markov and divisible.

### Physical consequence

The model has not derived coherent darkening as a record of the positive
Markov sample. It has reconstructed a second process by inserting the
analytic-continuation rule $e^{-H}\mapsto e^{-itH}$ and then applying a
norm-square endpoint reader.

Calling both objects “the process” would erase the central ontology question.

---

## 6. Positive source coupling and a secondary entangled state

Take two independent copies $A$ and $B$ of the positive law. At the reflection
plane introduce the same relational rule with a source coupling $J$:

$$
F_J(a,b)
=
\frac{e^{(J/2)z_az_b}}{\sqrt{\cosh J}}.
\tag{CRP1-26}
$$

$F_J$ is real and strictly positive. It defines a normalized OS vector because

$$
\frac14\sum_{a,b}F_J(a,b)^2=1.
\tag{CRP1-27}
$$

Choose

$$
J=\log 3.
\tag{CRP1-28}
$$

Under the canonical isometry from $L^2(X^2,\pi\otimes\pi)$ to standard
$\mathbb C^2\otimes\mathbb C^2$, the source vector is

$$
|\psi_J\rangle
=
\frac{
3|00\rangle+|01\rangle+|10\rangle+3|11\rangle
}{2\sqrt5}.
\tag{CRP1-29}
$$

No complex source amplitude was inserted; all four coefficients descend from
one positive Gibbs relation. The concurrence is

$$
C_J
=
2|c_{00}c_{11}-c_{01}c_{10}|
=
\frac45.
\tag{CRP1-30}
$$

The directly tilted positive whole law is also legitimate:

$$
d\mu_{K,J}
=
F_J(\omega_0^A,\omega_0^B)^2
\,d(\mu_K^A\otimes\mu_K^B).
\tag{CRP1-31}
$$

Its time-zero bit distribution equals the squared coefficients of
(CRP1-29). Thus one commuting reader is common to both descriptions.

The tilted law remains reflection positive. Conditioning on the two time-zero
bits still makes past and future independent with identical reversible
conditional laws; $F_J^2$ only replaces the nonnegative cut distribution.
The proof of CRP1-A therefore applies with that new cut weight.

The decisive issue is whether all required noncommuting readers are also
physical coarse-grainings of (CRP1-31).

---

## 7. Secondary local controls and CHSH prediction

Let $Z$ be the multiplication reader in the configuration basis. The local
secondary control $U(t)$ generates the rotated reader

$$
M(\theta)
=
U(t)^\dagger ZU(t)
=
Z\cos\theta-Y\sin\theta,
\qquad
\theta=\epsilon t.
\tag{CRP1-32}
$$

For the state (CRP1-29),

$$
\langle Z\otimes Z\rangle=\frac45,
\qquad
\langle Y\otimes Y\rangle=-\frac45,
\qquad
\langle Z\otimes Y\rangle
=
\langle Y\otimes Z\rangle=0.
\tag{CRP1-33}
$$

Choose

$$
A_0=Z,
\qquad
A_1=Y,
\tag{CRP1-34}
$$

$$
B_0=\frac{Z-Y}{\sqrt2},
\qquad
B_1=\frac{Z+Y}{\sqrt2}.
\tag{CRP1-35}
$$

The secondary CHSH value is

$$
S_{\rm OS}
=
\langle A_0B_0\rangle
+\langle A_0B_1\rangle
+\langle A_1B_0\rangle
-\langle A_1B_1\rangle
=
\frac{8\sqrt2}{5}.
\tag{CRP1-36}
$$

Hence

$$
2
<
\frac{8\sqrt2}{5}
<
2\sqrt2.
\tag{CRP1-37}
$$

The construction therefore gets a real Bell-violating quantum prediction from
a positive source coupling and a common secondary Hilbert representation.

That is a meaningful positive-first representation result. It is not yet the
record law of the positive actual configurations.

---

## 8. The reader/actuality obstruction

$Z$ is a measurable function of the time-zero configuration. $Y$ is not.
In the two-point configuration algebra, every direct stable reader is a
commuting multiplication operator. The rotated projectors built from $Y$
belong to the secondary operator algebra obtained only after analytic
continuation.

Suppose the positive configuration sample $\lambda$ is complete at the Bell
source cut, source-independent of the later settings, and each separated
reader is a local stochastic response:

$$
P(a,b\mid x,y)
=
\int
\rho(d\lambda)
A(a\mid x,\lambda)
B(b\mid y,\lambda).
\tag{CRP1-38}
$$

Then the standard pointwise CHSH argument gives

$$
|S|\le2.
\tag{CRP1-39}
$$

The positive Markov/Gibbs law with directly readable local pointers belongs to
this class. It cannot yield (CRP1-36).

To retain (CRP1-36), at least one of the following must change:

1. the positive configuration at the source cut is not complete;
2. the law is not divisible through that cut;
3. reader responses are not local functions/kernels of that carrier;
4. the source law depends on the complete measurement context;
5. source and settings are statistically dependent;
6. there is a retrodependent/two-boundary relation;
7. the secondary noncommutative operator law, rather than the positive sample,
   is predictively fundamental; or
8. the theory departs from the quantum prediction.

CRP-1 supplies none of these as an independently justified physical law. It
simply changes from the positive Markov process to the secondary Hilbert
process at the point where they matter.

---

## 9. Theorem CRP1-B — reflection positivity alone admits PR

The Bell failure cannot be repaired by citing reflection positivity without a
common physical source/composition rule.

Let $c$ denote any complete experiment context and let $P_c(r)$ be any
positive normalized finite record law. Define

$$
\Omega_c=\mathcal R_c^-\times\mathcal R_c^+,
\qquad
\vartheta(r^-,r^+)=(r^+,r^-),
\tag{CRP1-40}
$$

and

$$
\mu_c(r^-,r^+)
=
P_c(r^+)\,\mathbf1[r^-=r^+].
\tag{CRP1-41}
$$

For a function $F$ of the plus coordinate,

$$
\int
\overline{F\circ\vartheta}F
\,d\mu_c
=
\sum_rP_c(r)|F(r)|^2
\ge0.
\tag{CRP1-42}
$$

Thus every finite positive record law has a diagonal reflection-positive
completion.

Apply this construction to

$$
P_v(a,b\mid x,y)
=
\frac14
\left[1+v(-1)^{a\oplus b\oplus xy}\right].
\tag{CRP1-43}
$$

The family is reflection positive context by context for every
$0\le v\le1$. Its CHSH value is

$$
S=4v.
\tag{CRP1-44}
$$

Hence the same reflection-positivity syntax admits the local boundary, the
quantum value, and PR:

$$
v=\frac12,
\qquad
v=\frac1{\sqrt2},
\qquad
v=1.
\tag{CRP1-45}
$$

### Scope

The diagonal completion is a representation, not a source-complete model. Its
purpose is exact: reflection positivity by itself does not select quantum
composition. The selecting work in (CRP1-36) came from one common tensor-
product Hilbert representation and its noncommuting local readers.

CRP would earn native credit only by generating that common structure and the
actual record bridge from the positive source law. CRP-1 does not.

---

## 10. Sequential controls and division

The same split appears in sequential experiments.

In the positive process,

$$
K^{m+n}=K^mK^n
\tag{CRP1-46}
$$

at every intermediate configuration cut. An actual complete read of the
intermediate bit changes no mathematical composition rule because the process
was already Markov on that carrier.

In the secondary process,

$$
U(t_2+t_1)=U(t_2)U(t_1),
\tag{CRP1-47}
$$

but the endpoint probabilities do not compose stochastically across an
unread seam. Inserting a complete $Z$ record replaces coherent operator
composition with an instrument sum and destroys the cross-term.

This reproduces the correct quantum distinction conditionally. It does not
make the positive base process indivisible. The division grammar belongs to
the secondary quantum intervention law.

---

## 11. Purification and local tomography audit

The positive source function $F_J$ is a useful physical clue: correlations in
a positive parent can become entanglement in the secondary Hilbert space.
But neither load-bearing reconstruction principle is natively earned.

### 11.1 Purification

Finite-dimensional Hilbert theory permits purification of the secondary mixed
states. That conclusion uses the secondary tensor product and reversible
operator group. It does not prove that the purifying coordinates are actual
positive configurations.

If they are declared complete, readable, and restartable configurations, the
positive parent divides through them. If they are merely predictive Hilbert
coordinates, purification says nothing about positive actuality. If they are
actual but incomplete, another whole law is required. The QPB trilemma remains
unchanged.

### 11.2 Local tomography

$\mathbb C^2\otimes\mathbb C^2$ is locally tomographic under the complete
secondary quantum reader set. The directly measurable cylinder algebra of
$X^2$, however, contains only commuting configuration functions and is not
that reader set.

Thus local tomography is true of the reconstructed predictive theory and
false as a claim that all those readers have descended from the positive
configuration ontology.

---

## 12. Source-completion and resource audit

The construction uses only two real couplings, $\kappa=J=\log3$, and a fixed
Gibbs relation. Its mathematical description is compact. That does not yet
earn physical source completion.

### 12.1 Transfer input

At exact finite scope,

$$
K=e^{-H},
\qquad
H=-\log K.
\tag{CRP1-48}
$$

Therefore the complete transfer kernel and the secondary Hamiltonian are
mutually computable. If $\kappa$ is chosen because it yields the desired
quantum frequency, the target has been reparameterized.

Native credit would require $\kappa$ and $J$ to descend from independently
measured non-target physical relations and then predict a held-out coherent
and Bell-sensitive response. No such material transfer is constructed.

### 12.2 Analytic-continuation input

The map

$$
e^{-nH}\longmapsto e^{-itH}
\tag{CRP1-49}
$$

supplies the imaginary unit, the Lorentzian parameter, and the rule connecting
the two. Reflection positivity makes the reconstruction mathematically
consistent; it does not prove that this continuation is the physical control
law experienced by the positive configurations.

### 12.3 Reader input

The $Z$ pointer is sourced. The $Y$ reader and its continuous rotations are
secondary. Adding apparatus variables that implement them through an
ordinary-positive local Markov interaction restores the Bell bound unless a
new nonlocal, contextual, indivisible, measurement-dependent, or two-boundary
law is printed.

### 12.4 Scaling

The finite control has constant resources. A scalable family would still have
to generate:

1. the carrier and reference measure;
2. all cut involutions;
3. reflection-positive interaction measures;
4. physical noncommuting readers;
5. products and interacting parents;
6. gauge/fermion sectors;
7. a continuum or other scale limit; and
8. an actuality bridge.

No target-process compression theorem follows from the two-state model.

---

## 13. QFT and gravity preflight

The construction confirms why reflection positivity remains relevant to QFT:
one positive law can organize a common Hilbert representation rather than a
separate lift for every endpoint table.

It also confirms why gravity cannot yet promote it.

1. the reflection cut is supplied;
2. the two-sided index is external structure;
3. no local operational chronology is generated;
4. no metric, dimension, continuum, gauge constraint, or stress-energy source
   is derived;
5. the actual object sourcing gravity is ambiguous between the positive
   configuration, secondary quantum state, and stable records;
6. no reciprocal matter--geometry law exists; and
7. no fixed-background interacting QFT family has been source-generated.

MG0 therefore records a failed-entry preflight, not a gravity model.

---

## 14. Hostile controls survived and failed

| control | verdict |
|---|---|
| ordinary positivity and normalization | pass |
| exact reflection positivity | pass |
| Hilbert secondary to positive law | pass |
| positive correlated source insertion | pass |
| scalar coherent darkening in secondary law | pass |
| stochastic nondivision in secondary endpoints | pass |
| actual positive base is itself indivisible | fail; base is Markov |
| quantum controls are physical positive-law interventions | fail |
| all Bell readers are measurable configuration records | fail |
| direct local positive actuality violates CHSH | fail by Bell bound |
| reflection positivity excludes PR | fail by CRP1-B |
| purification physically descends | fail / trilemma unchanged |
| local tomography physically descends | fail; secondary only |
| target-independent material source map | absent |
| internal time or chronology | absent |
| QFT or gravity closure | absent |

The passes are genuine mathematics. The failures are physical and semantic.

---

## 15. Outcome adjudication

Relative to the architecture ladder:

```text
CRP-L1  POSITIVE SOURCE MEMBER:              MATHEMATICALLY YES
CRP-L2  REFLECTION/HILBERT RECONSTRUCTION:   EXACT YES
CRP-L3  SAME-LAW SCALAR/SEQUENTIAL PROCESS:  NO
CRP-L4  NATIVE PRODUCT/INTERACTION PARENT:   NO
CRP-L5  PHYSICAL PURIFICATION/TOMOGRAPHY:    NO
CRP-L6  SOURCE/RESOURCE TRANSFER:            NO
CRP-L7  INTERACTING QFT FAMILY:              NO
CRP-L8  EMPIRICAL DISCRIMINATOR:             NO
CRP-L9  CHRONOLOGY/GRAVITY:                  NO
```

The correct split verdict is

$$
\boxed{
\begin{aligned}
\text{representation/control ceiling}
&=\text{CRP-L2},\\
\text{native U0 admission}
&=\text{REJECTED FOR THIS MODEL}.
\end{aligned}}
\tag{CRP1-50}
$$

No automatic second CRP model, alternative architecture, pin, review, or
repair chain follows.

---

## 16. What this changes in the ontology ranking

The attempt strengthens three conclusions without selecting an ontology.

1. **Positive-first reconstruction is real.** A positive Gibbs relation can
   generate a secondary entangled state and coherent quantum predictions.
2. **Representation is not actuality.** The sampled positive process and the
   quantum process reconstructed from it are not the same typed dynamics.
3. **The reader/composition bridge is the irreducible burden.** Reflection
   positivity organizes the quantum predictive carrier but does not make its
   noncommuting readers into records of the positive configurations.

This weakens the claim that ordinary-positive configurations already explain
quantum theory. It does not establish Hilbert ontology. The live ontology fork
is now:

1. a different source-complete positive whole-process law with a genuinely
   physical contextual reader bridge;
2. a primitive pair-history/quantum relational predictive law plus positive
   record actuality; or
3. standard QFT composition plus an objective actualization modification.

Only option 1 was attempted here, and only through CRP-1.

---

## 17. Maximum legitimate claim

> A single exact positive reversible Gibbs kernel reconstructs a qubit Hilbert
> space and Hamiltonian. A positive two-system Gibbs source insertion
> reconstructs the entangled state
> $(3|00\rangle+|01\rangle+|10\rangle+3|11\rangle)/(2\sqrt5)$,
> and secondary local controls predict CHSH $8\sqrt2/5$. The directly sampled
> positive process is instead Markov and dissipative; its local measurable
> records obey CHSH at most two. Every finite record table, including PR, also
> has a contextwise diagonal reflection-positive completion. Reflection
> positivity therefore makes positive-first quantum representation possible
> but does not source the physical noncommuting readers, common composition,
> or actuality bridge. This model is rejected as a native U0 candidate while
> remaining a valid mathematical control. No conclusion about fundamental
> Hilbert ontology, QFT origin, spacetime, gravity, or unification follows.
