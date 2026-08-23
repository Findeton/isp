# ISP v17 — U0 short-time probability-jet source gate

**Status:** ACTIVE AUTHOR-SIDE CLASS-BOUNDED THEOREM/CONTROL PACKET
**Date:** 2026-08-23
**Scientific result awarded:** none
**Native U0 candidate constructed:** no
**Official pin/review/U0-T4 opened:** no

---

## 0. Question and claim ceiling

The active U0 problem is not whether a supplied quantum evolution can be
rewritten in probability language. It is:

> Can one uniform ordinary-positive, genuinely indivisible stochastic law on
> abstract physical configurations generate held-out complete quantum
> processes without receiving the target wavefunction, process matrix,
> action, phase, holonomy, or an equivalent answer encoding?

This packet asks a narrower source question:

> What local dynamical form is already excluded by the short-separation
> behavior of coherent quantum transition probabilities, and what positive
> information survives in the higher probability derivatives?

The exact answer is class-bounded.

1. A differentiable amplitude potential whose squared moduli form a
   stochastic kernel has zero first derivative at an identity boundary. This
   is the short-time obstruction already identified by Doukas.
2. Therefore a locally Lipschitz, autonomous, first-order ordinary
   differential equation on the instantaneous stochastic kernel alone cannot
   generate a nonconstant coherent family from the identity.
3. The second probability derivative carries coupling magnitudes.
4. The third probability derivative can carry directed three-step
   interference and distinguish conjugate chiral controls using only positive
   transition probabilities.
5. A positive two-state second-order equation can reproduce one exact coherent
   endpoint family without a complex amplitude, but only after its parameter,
   coupling, boundary jet, and family have been supplied.
6. Every finite time-independent unitary endpoint family has a finite
   probability-coordinate differential representation, but its coefficients
   and initial jets can encode the target generator. This is a compiler
   control, not native source completion.

The packet does **not** prove that reality is finite, differentiable,
trajectory-based, externally timed, unitary, complex, Hamiltonian, Markovian,
or governed by a local differential equation. It does not construct the
native law. Its strongest physical conclusion is that a regular instantaneous
rate law on the visible stochastic kernel is too small, while an
ordinary-positive whole-boundary or memory-bearing law remains open.

---

## 1. Binding routing and ontology firewalls

This packet inherits the v17 scientific scope correction.

1. N1 and N1A are Nelson-mechanics hostile controls only.
2. No continuous path, Euclidean configuration, Brownian noise, Markov
   division, external time, Nelson coefficient, mean-Newton law, phase field,
   U(1) target, bundle, or holonomy is inherited.
3. G1 remains a target-action/holonomy compiler control.
4. G2 remains a fixed-background quantum-kinematics control.
5. Barandes supplies a serious guiding hypothesis, not a predetermined
   ontology.
6. MG0 remains a gravity-discriminator preflight and is not used here.

The finite configuration basis below is an operational quantum control. It is
not proposed as the microscopic configuration domain of U0. The parameter
\(\tau\) is a supplied one-parameter separation coordinate in the control. It
is not thereby external time, proper time, or a clock reading in the native
theory.

---

## 2. Version-bound primary-source boundary

The attribution and interpretation were checked on 2026-08-23 against:

1. Jason Doukas,
   [On the emergence of quantum mechanics from stochastic processes](https://arxiv.org/abs/2602.22095),
   arXiv:2602.22095v2 (2026).
2. Jacob A. Barandes,
   [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192),
   arXiv:2507.21192 (2025; current HTML dated 2026-03-22).
3. Jacob A. Barandes,
   [The Stochastic--Quantum Correspondence](https://arxiv.org/abs/2302.10778),
   arXiv:2302.10778v3.
4. B. Misra and E. C. G. Sudarshan,
   [The Zeno's paradox in quantum theory](https://doi.org/10.1063/1.523304),
   Journal of Mathematical Physics **18**, 756--763 (1977).
5. Zoltán Zimborás, Mauro Faccin, Zoltán Kádár, James D. Whitfield,
   Ben P. Lanyon, and Jacob Biamonte,
   [Quantum Transport Enhancement by Time-Reversal Symmetry Breaking](https://arxiv.org/abs/1208.4049),
   Scientific Reports **3**, 2361 (2013).
6. Jacob Biamonte and Jacob Turner,
   [Topological classification of time-asymmetry in unitary quantum processes](https://arxiv.org/abs/1703.02542),
   arXiv:1703.02542.

### 2.1 Attribution ledger

Doukas proves the differentiable short-time zero-rate obstruction for
\(\theta\)-processes and shows that the only Markovian member of that class is
trivial. That fact is prior art, not a v17 discovery.

Misra--Sudarshan supply the broader quantum-Zeno context in which regular
unitary survival probabilities have quadratic rather than exponential
short-time departure. The theorem below is not presented as a rediscovery of
the quantum Zeno effect.

Zimborás et al. and Biamonte--Turner establish that complex edge transport on
loops can produce directional asymmetry in observable transition
probabilities. The exact third-jet triangle calculation below is an elementary
v17 reconstruction used to locate that information in the probability jet.

Barandes supplies the stochastic--quantum dictionary and the indivisible-law
motivation. The cited papers do not by themselves provide the target-blind
source-completion map demanded by U0.

### 2.2 What remains original to this packet

Subject to later independent priority review, the packet's author-side
contribution is the combined source gate:

1. the autonomous first-order stall corollary stated as a U0 source-law
   exclusion;
2. the exact second/third probability-jet information ledger;
3. the conjugate triangle as a minimal no-magnitude/no-spectrum selection
   witness;
4. the positive second-order escape control;
5. the finite spectral-ODE compiler control; and
6. the resulting distinction between local rate generation, enlarged
   memory/jet generation, and whole-boundary indivisible generation.

No novelty or result is awarded author-side.

---

## 3. Operational control notation

Let \(H=H^\dagger\) be an \(n\times n\) Hermitian matrix and define

\[
U(\tau)=e^{-i\tau H}.
\]

Relative to one supplied finite reader/preparation basis, define the
column-stochastic endpoint family

\[
\Gamma_{ij}(\tau)=|U_{ij}(\tau)|^2.
\]

Thus \(j\) labels the prepared basis record and \(i\) labels the later reader
record. For every \(\tau\),

\[
\Gamma_{ij}(\tau)\geq 0,
\qquad
\sum_i\Gamma_{ij}(\tau)=1,
\qquad
\Gamma(0)=I.
\]

This is a standard-quantum comparator. The U0 source problem is precisely to
avoid receiving \(H\), \(U\), or their information-equivalent encoding as the
native law's answer input.

For a smooth stochastic family, its boundary probability jet is

\[
\mathcal J_k(\Gamma;0)
=
\bigl(\Gamma(0),\dot\Gamma(0),\ldots,\Gamma^{(k)}(0)\bigr).
\]

A jet is observable only relative to a physically calibrated family of
preparations, readers, and separation settings. Mathematical derivatives are
not self-authenticating physical observables.

---

## 4. Theorem PJ-A — differentiable squared-modulus laws have zero rate

Let

\[
\theta(\epsilon)=I+\epsilon A+O(\epsilon^2)
\]

be a differentiable complex matrix family at \(\epsilon=0\). Suppose

\[
\Gamma_{ij}(\epsilon)=|\theta_{ij}(\epsilon)|^2
\]

is column stochastic for sufficiently small nonnegative \(\epsilon\). Then

\[
\dot\Gamma(0)=0.
\]

### Proof

For \(i\neq j\),

\[
\theta_{ij}(\epsilon)=\epsilon A_{ij}+O(\epsilon^2),
\]

so

\[
\Gamma_{ij}(\epsilon)
=
\epsilon^2|A_{ij}|^2+O(\epsilon^3).
\]

Hence every off-diagonal first derivative vanishes. For \(i=j\),

\[
\Gamma_{jj}(\epsilon)
=
|1+\epsilon A_{jj}+O(\epsilon^2)|^2
=
1+2\epsilon\operatorname{Re}A_{jj}+O(\epsilon^2).
\]

Column stochasticity gives

\[
\sum_i\dot\Gamma_{ij}(0)=0.
\]

All off-diagonal terms in this sum vanish, so

\[
2\operatorname{Re}A_{jj}=0.
\]

Thus the diagonal first derivative also vanishes. \(\square\)

### Scope

This is Doukas's short-time obstruction in the present notation. It excludes
ordinary continuous-time Markov leakage with a nonzero rate matrix from the
differentiable squared-modulus class. It does not exclude:

1. a general stochastic kernel not of squared-modulus form;
2. a nondifferentiable or singular boundary;
3. a law on a larger state than \(\Gamma\);
4. a nonautonomous law with a supplied schedule;
5. a higher-order law;
6. a whole-boundary indivisible law; or
7. a law whose physically meaningful parameter has no identity boundary.

---

## 5. Theorem PJ-B — autonomous first-order probability dynamics stalls

Let \(\mathcal X\) be a finite-dimensional normed space containing the
stochastic matrices, and let \(F:\mathcal X\to\mathcal X\) be locally
Lipschitz near \(I\). Suppose a differentiable stochastic family obeys

\[
\dot\Gamma(\tau)=F(\Gamma(\tau)),
\qquad
\Gamma(0)=I.
\]

If

\[
\dot\Gamma(0)=0,
\]

then the unique local solution is

\[
\Gamma(\tau)=I.
\]

### Proof

The initial derivative gives

\[
F(I)=0.
\]

The constant curve \(\Gamma(\tau)=I\) therefore solves the initial-value
problem. Local Lipschitz continuity gives uniqueness, so no different local
solution can leave \(I\). \(\square\)

### Corollary PJ-B1

No nonconstant differentiable coherent family of Theorem PJ-A can be generated
from its instantaneous transition matrix by one regular autonomous
first-order equation

\[
\dot\Gamma=F(\Gamma)
\]

starting at the identity.

### Exact meaning

The obstruction is not positivity by itself. It is the conjunction:

1. instantaneous visible state \(=\Gamma\);
2. first-order local evolution;
3. autonomy;
4. local uniqueness/regularity; and
5. an identity boundary with coherent quadratic departure.

A native positive proposal may escape honestly by supplying independently
physical memory, a boundary velocity or higher jet, explicit relational
context, a singular selection rule, or one irreducible whole-boundary law.
Each escape changes the physical state or law type and must be charged.

### Non-Lipschitz warning

Dropping uniqueness can allow curves to wait at the identity and then depart,
as in scalar equations of the form \(\dot x=\sqrt{|x|}\). But the equation
alone then fails to select which departure occurs or when. Nonuniqueness is
not free source completion; it transfers the selection burden to an
additional rule.

---

## 6. Theorem PJ-C — exact unitary probability jets

For the finite comparator of Section 3:

\[
\Gamma(0)=I,
\qquad
\dot\Gamma(0)=0.
\]

For \(i\neq j\),

\[
\Gamma_{ij}(\tau)
=
|H_{ij}|^2\tau^2
+
\operatorname{Im}
\left[
H_{ij}^*(H^2)_{ij}
\right]\tau^3
+
O(\tau^4).
\]

Therefore

\[
\ddot\Gamma_{ij}(0)=2|H_{ij}|^2
\]

and

\[
\Gamma^{(3)}_{ij}(0)
=
6\operatorname{Im}
\left[
H_{ij}^*(H^2)_{ij}
\right].
\]

For \(i=j\),

\[
\Gamma_{ii}(\tau)
=
1-
\left(
\sum_{k\neq i}|H_{ki}|^2
\right)\tau^2
+
O(\tau^4),
\]

and every odd derivative of \(\Gamma_{ii}\) at zero vanishes.

### Proof

The exponential expansion gives

\[
U_{ij}(\tau)
=
\delta_{ij}
-i\tau H_{ij}
-\frac{\tau^2}{2}(H^2)_{ij}
+\frac{i\tau^3}{6}(H^3)_{ij}
+O(\tau^4).
\]

For \(i\neq j\), set

\[
a=-iH_{ij},
\qquad
b=-\frac12(H^2)_{ij}.
\]

Then

\[
|a\tau+b\tau^2+O(\tau^3)|^2
=
|a|^2\tau^2
+2\operatorname{Re}(a^*b)\tau^3
+O(\tau^4).
\]

Since

\[
2\operatorname{Re}(a^*b)
=
\operatorname{Im}
\left[
H_{ij}^*(H^2)_{ij}
\right],
\]

the off-diagonal formula follows.

For \(i=j\), Hermiticity makes \(H_{ii}\) real and

\[
(H^2)_{ii}=\sum_k|H_{ki}|^2.
\]

Expanding the squared modulus gives the printed quadratic coefficient.
Finally,

\[
U_{ii}(-\tau)=U_{ii}(\tau)^*,
\]

so \(|U_{ii}(\tau)|^2\) is even. \(\square\)

### Information ledger

At this bounded comparator scope:

| jet coordinate | information visible in positive endpoint data |
|---|---|
| order 0 | identity of prepared/read records |
| order 1 | zero; no regular instantaneous leakage rate |
| order 2 | edge-coupling magnitudes \(|H_{ij}|\) |
| order 3 | directed interference among a direct edge and two-step routes |
| higher orders | longer spectral/path interference combinations |

This ledger does not state that \(H\) is fundamental. It states which
standard-quantum distinctions are visible in the positive response family a
native law would have to predict.

---

## 7. Corollary PJ-C1 — the first directed response is a loop effect

For \(i\neq j\),

\[
(H^2)_{ij}
=
\sum_k H_{ik}H_{kj}.
\]

Hence the cubic coefficient is

\[
\operatorname{Im}
\left[
H_{ij}^*
\sum_k H_{ik}H_{kj}
\right].
\]

Diagonal \(k=i,j\) terms are real after multiplication by \(H_{ij}^*\).
The imaginary part therefore comes from alternative two-step routes through
other configurations. A two-state comparator has no such third-vertex route
and no cubic directional asymmetry of this form.

Thus the first local probability signature of chirality in this class is not
an isolated edge property. It is relational interference around a loop.

This is physically important for U0: a presentation-covariant source rule
whose only input is independent edge magnitudes cannot distinguish conjugate
members that share those magnitudes. If both members belong to the target
family, additional law-level relational structure must determine how
alternative routes cohere, or the chiral response remains underselected.

### Corollary PJ-C2 — gauge and energy-origin invariance

Let

\[
H'=DHD^\dagger+cI,
\]

where \(D\) is diagonal unitary and \(c\in\mathbb R\). For \(i\neq j\),

\[
|H'_{ij}|=|H_{ij}|
\]

and

\[
\operatorname{Im}
\left[
(H'_{ij})^*(H'^2)_{ij}
\right]
=
\operatorname{Im}
\left[
H_{ij}^*(H^2)_{ij}
\right].
\]

The diagonal rephasing factors cancel between the direct edge and the
two-step route. The energy shift contributes \(2c|H_{ij}|^2\), which is real.
Thus the second- and third-jet quantities above do not depend on basis-vector
phases or the chosen energy origin. Complex conjugation, by contrast, reverses
the cubic imaginary part.

This establishes a representation-invariant comparator quantity at the
printed operational basis scope. It does not make that basis fundamental or
provide the physical reference that orients the experiment.

---

## 8. Exact control PJ-D — conjugate triangle chirality

Let \(g>0\) and

\[
H_\phi
=
g
\begin{pmatrix}
0&1&e^{-i\phi}\\
1&0&1\\
e^{i\phi}&1&0
\end{pmatrix}.
\]

Then \(H_\phi\) and \(H_{-\phi}\):

1. are Hermitian;
2. have identical entry magnitudes;
3. have identical diagonal data;
4. have identical characteristic polynomial

\[
\lambda^3-3g^2\lambda-2g^3\cos\phi;
\]

5. are related by complex conjugation; and
6. have opposite directed cubic probability response.

Indeed,

\[
(H_\phi^2)_{12}=g^2e^{-i\phi},
\]

so

\[
\Gamma^{(\phi)}_{12}(\tau)
=
g^2\tau^2-g^3\sin\phi\,\tau^3+O(\tau^4),
\]

whereas

\[
\Gamma^{(\phi)}_{21}(\tau)
=
g^2\tau^2+g^3\sin\phi\,\tau^3+O(\tau^4).
\]

Therefore

\[
\Gamma^{(\phi)}_{12}(\tau)
-
\Gamma^{(\phi)}_{21}(\tau)
=
-2g^3\sin\phi\,\tau^3+O(\tau^4).
\]

Conjugating \(\phi\mapsto-\phi\) reverses the sign.

### What the control proves

Neither edge magnitudes nor spectrum selects the directed response. The
observable positive transition family can nevertheless distinguish the two
responses once preparation/read direction and the orientation of the
separation protocol are physically fixed.

The missing datum need not be called a fundamental phase or holonomy.
Operationally it is the law's rule for directed relational response around a
three-way alternative. A native positive theory must generate that rule from
its own physical inputs.

### Reference and gauge firewall

If all preparation/read labels and protocol orientation are quotiented away,
the conjugate pair may become operationally indistinguishable. U0 may claim a
chiral distinction only when physical references, interventions, and readers
make the comparison meaningful. Absolute label asymmetry is not a substitute
for a physical relational reference.

---

## 9. Exact control PJ-E — a positive second-order two-state endpoint equation

Let

\[
\Gamma(\tau)
=
\begin{pmatrix}
1-p(\tau)&p(\tau)\\
p(\tau)&1-p(\tau)
\end{pmatrix}
\]

and impose

\[
p''(\tau)=2g^2\bigl(1-2p(\tau)\bigr),
\qquad
p(0)=0,
\qquad
p'(0)=0.
\]

The unique solution is

\[
p(\tau)=\sin^2(g\tau).
\]

Therefore

\[
\Gamma(\tau)
=
\begin{pmatrix}
\cos^2(g\tau)&\sin^2(g\tau)\\
\sin^2(g\tau)&\cos^2(g\tau)
\end{pmatrix},
\]

which is exactly the endpoint transition family generated by
\(H=g\sigma_x\).

### Why this matters

This exact control blocks an invalid inference:

> Zero first-order rate does not force a fundamental complex amplitude.

An ordinary real equation on a positive probability coordinate can reproduce
this endpoint family.

### Why it is not U0

The control receives:

1. the two-state carrier;
2. the supplied separation parameter \(\tau\);
3. the coupling \(g\);
4. the second-order equation selected for the target;
5. both initial jet values; and
6. no intervention, tensor-product, adaptive, reader, or actuality law.

It is a target-specific endpoint representation. It neither generates its own
physical coupling nor predicts a held-out complete process. Its stochastic
matrices also fail the ordinary Chapman--Kolmogorov semigroup law at generic
unrecorded seams, which is compatible with indivisibility but does not by
itself establish a native indivisible ontology.

---

## 10. Theorem PJ-F — finite spectral probability-coordinate ODE

Let

\[
H=\sum_a E_aP_a
\]

be the spectral resolution of a finite time-independent Hermitian matrix.
Then

\[
U_{ij}(\tau)
=
\sum_a e^{-iE_a\tau}(P_a)_{ij}
\]

and

\[
\Gamma_{ij}(\tau)
=
\sum_{a,b}
e^{-i(E_a-E_b)\tau}
(P_a)_{ij}(P_b)_{ij}^*.
\]

Hence every real function \(\Gamma_{ij}\) is a finite real trigonometric
polynomial in the distinct energy gaps. If \(\Delta_+\) is the set of
distinct positive gap magnitudes that occur, then

\[
\mathcal L_H
=
D\prod_{\omega\in\Delta_+}(D^2+\omega^2),
\qquad
D=\frac{d}{d\tau},
\]

annihilates every entry:

\[
\mathcal L_H\Gamma_{ij}=0.
\]

### Proof

The spectral expansion shows that each entry is a finite sum of a constant
and terms proportional to \(\cos(\omega\tau)\) and
\(\sin(\omega\tau)\). The factor \(D\) kills the constant, and
\(D^2+\omega^2\) kills the terms at frequency \(\omega\). \(\square\)

### Compiler classification

This theorem shows that a finite coherent endpoint family always has a
finite-order real probability-coordinate differential representation.
It does **not** show that the representation is a native positive law.

1. The gap set is computed from the target \(H\).
2. Enough initial jets contain the spectral mixing data.
3. Generic solutions of the scalar ODE need not remain stochastic or
   nonnegative.
4. A separate equation is not yet a uniform composite/intervention law.
5. Degeneracies and operational gauges leave inverse nonuniqueness.

Supplying \(\mathcal L_H\) and the target-complete initial jet can be
information-equivalent to supplying the target quantum process. PJ-F is
therefore a strict compiler/control under the U0 no-equivalent-input gate.

---

## 11. Complete-process wall

Even the exact full endpoint family

\[
\{\Gamma(\tau):\tau\in I\}
\]

is not automatically a complete controlled process.

A complete process must predict, under one unchanged law:

1. different preparations;
2. inserted physical interventions;
3. adaptive controls conditioned on retained records;
4. alternative readers;
5. composites and separated subsystems;
6. genuine recorded divisions;
7. unrecorded nondivisions;
8. erasure and memory export;
9. held-out program lengths; and
10. the joint distribution of the full retained transcript.

Endpoint probability jets may identify some coupling invariants in a
calibrated comparator while leaving coherent composition underdetermined.
E-Comp and the active U0 complete-process controls already show why a
collection of endpoint kernels cannot silently be promoted to a process
matrix or universal intervention law.

The U0 source rule must generate the control-indexed family

\[
\mathcal N:
(S,\sigma,b,c,\mathsf{Read})
\longmapsto
p^{\mathcal N}_{S,b,c}(dr\mid\sigma)
\]

without first reconstructing the held-out answer and placing it in a
coefficient, memory, action, or boundary jet.

---

## 12. Source-law classification after the jet gate

The exact gate separates five classes.

### Class S1 — instantaneous Markov rate on the visible kernel

\[
\dot\Gamma=R\Gamma
\quad\hbox{or}\quad
\dot\Gamma=F(\Gamma).
\]

For regular autonomous dynamics at an identity boundary, this class cannot
generate nontrivial coherent quadratic departure. **Excluded at the printed
scope.**

### Class S2 — nonautonomous visible-kernel dynamics

\[
\dot\Gamma=F(\tau,\Gamma).
\]

This can leave the identity even when the initial derivative vanishes, but
the supplied schedule can encode the target response. **Open only with a
source/provenance and no-equivalent-input audit.**

### Class S3 — enlarged local state or probability jet

\[
\dot\Gamma=V,
\qquad
\dot V=G(\Gamma,V,\ldots).
\]

This accommodates quadratic departure. The extra state must be physically
identified, positively interpreted where claimed, accessible to the licensed
interventions, and charged as memory/context. A signed formal velocity is not
automatically an ordinary-positive configuration variable. **Open.**

### Class S4 — singular or nonunique local law

This can evade the Lipschitz theorem but needs an additional physical branch
and departure selector. **Mathematically open; source incomplete without the
selector.**

### Class S5 — irreducible whole-boundary or whole-program law

The law assigns a normalized complete record distribution directly to the
typed experiment and need not arise from a local rate or intermediate
restart. This is the most Barandes-facing escape and is not touched by PJ-B.
It must still satisfy U0 uniformity, intervention, genuine-division,
actuality, and resource gates. **Open and primary.**

No class is selected merely by surviving this gate.

---

## 13. Barandes-facing interpretation

The probability-jet result strengthens rather than weakens the reason to take
indivisible stochastic laws seriously.

1. A differentiable squared-modulus coherent endpoint family is tangent to
   the identity at first order.
2. A time-homogeneous visible-kernel Markov rate law either has nonzero
   first-order leakage or, under the printed uniqueness premises, remains at
   the identity.
3. The physically relevant information begins in correlations among boundary
   alternatives at second and higher order.
4. At third order, directed loop response already depends on how alternative
   routes combine.

This suggests that the missing physics may live in a law for complete
boundaries, interventions, or relational histories rather than in an
instantaneous jump rate on visible configurations.

But this is only a constraint, not Barandes completion. The stochastic--
quantum dictionary can represent a supplied process. U0 still needs the
physical source map that chooses one law for each typed system and control
without receiving the target quantum answer.

The correct live question becomes:

> Can an ordinary-positive indivisible source rule generate the entire
> hierarchy of control-dependent probability jets—or the corresponding
> complete boundary laws—from independently physical relational inputs?

Calling those higher jets “hidden phase” does not answer the question.
Calling them “memory” is explanatory only after the memory has a
target-independent physical carrier, source rule, intervention response, and
resource account.

---

## 14. Physical intuition

The zero first derivative has a clean operational meaning. At an identity
boundary, a differentiable coherent alternative first develops a small
*possibility amplitude* proportional to separation; its observable
probability is therefore quadratic. A positive theory need not regard that
amplitude as matter. But it must reproduce the delayed probability departure.

The second jet says how strongly each alternative initially opens. The third
jet says whether a direct route and a two-step route reinforce differently
when the experiment is directionally reversed. The triangle shows that this
orientation information is visible in positive statistics even though it is
not present in isolated edge magnitudes or the spectrum.

The promising native object is consequently not “a classical jump process
with unusual rates.” It is a law that assigns mutually constrained positive
responses to whole relational experiments. Its indivisibility would mean
that an unrecorded intermediate cut is not a lawful restart, while genuine
records still license conditioning.

That picture is compatible with the Barandes programme, but it does not yet
establish that the configurations are particles, fields, events, histories,
or anything else.

---

## 15. Hostile controls and forbidden inferences

Any use of this packet must survive the following attacks.

1. **Doukas priority erasure:** claiming the zero-rate theorem as new.
2. **Zeno relabeling:** treating a known short-time effect as a native law.
3. **Complex-ontology promotion:** inferring that quadratic departure makes
   complex amplitudes material.
4. **Second-order promotion:** calling PJ-E a complete stochastic ontology.
5. **Coefficient smuggling:** computing the ODE from the target Hamiltonian
   and calling it prediction.
6. **Initial-jet smuggling:** supplying enough derivatives to reconstruct the
   target.
7. **External-parameter laundering:** calling \(\tau\) emergent time without
   a clock or operational construction.
8. **Basis laundering:** treating the finite reader basis as fundamental
   discrete configuration space.
9. **Chirality without reference:** using label order as a physical
   orientation.
10. **Magnitude sufficiency:** assuming \(|H_{ij}|\) and the spectrum select
    the directed response.
11. **Endpoint/process conflation:** treating all pairwise kernels as the
    adaptive complete process.
12. **Memory by renaming:** calling phase-complete target advice a physical
    stochastic memory.
13. **Non-Lipschitz free choice:** using mathematical nonuniqueness without a
    physical selector.
14. **Markov no-go inflation:** extending PJ-B to every positive stochastic
    law.
15. **Indivisibility by omission:** hiding an independently evidenced carrier
    variable to manufacture noncomposition.
16. **Gravity rescue:** asking MG0 to select the missing matter law.
17. **Nelson graft:** importing diffusion or trajectories as the higher-jet
    carrier.
18. **Hilbert fallback:** promoting Hilbert ontology because this one local
    positive class fails.

---

## 16. Falsifiers for a future native proposal

A future source proposal that invokes this gate must fail if any of the
following occurs.

1. Its visible state is only \(\Gamma\), its law is regular autonomous
   first-order, and it claims nontrivial coherent identity-boundary response.
2. Its extra jet/memory state is fitted separately for each held-out target.
3. Its triangle response depends only on edge magnitudes and spectrum but
   purports to choose between \(\phi\) and \(-\phi\).
4. Its physical reader cannot distinguish the directed comparison that
   carries the claimed chirality.
5. Its local equations reproduce unperturbed endpoints but fail inserted
   interventions or adaptive complete records.
6. Its enlarged state is merely the target wavefunction, process tensor, or
   action under a new name.
7. Its whole-boundary rule changes with program length rather than following
   one uniform composition grammar.
8. Its nondivision disappears when independently evidenced memory/reference
   variables are restored.

---

## 17. Outcome ladder and present adjudicative status

### PJ-L0 — algebra or attribution fails

The packet is withdrawn.

### PJ-L1 — known short-time control only

The zero-rate fact is retained solely as Doukas/Zeno prior art.

### PJ-L2 — bounded source-class obstruction

PJ-A through PJ-F survive: regular autonomous first-order dynamics on
\(\Gamma\) alone is excluded; higher probability jets carry magnitude and
directed-loop information; real positive higher-order and finite spectral
representations remain compiler controls.

### PJ-L3 — native positive source law

One target-blind ordinary-positive law generates the control-dependent jet
hierarchy and held-out complete processes. **Not reached.**

### PJ-L4 — scalable quantum matter

The same law passes arbitrary composition, adaptive intervention, Bell,
contextuality, identical-particle, QFT, and continuum controls. **Not
reached.**

### PJ-L5 — gravity-relevant complete matter law

The complete law enters MG0 against a genuinely different rival. **Not
reached.**

Author-side present status:

\[
\boxed{\mathrm{PJ\!-\!L2\ author\ packet\ only;\ no\ scientific\ award}}
\]

No official review has tested the attribution, formulas, claim scope, or
novelty.

---

## 18. Next author-side question

This packet points to one physically sharper source question without opening
U0-T4:

> What target-independent positive relational datum can generate the
> second-and-higher control-response hierarchy while remaining genuinely
> indivisible at unrecorded cuts and conditionable at physical records?

The admissible answer is not required to be a local differential law. It may
be a normalized whole-boundary consistency rule, a source-closed relational
memory law, or another form-neutral positive construction. It must still
explain:

1. how couplings and directional loop response arise from physical controls;
2. why one complete response family rather than its conjugate is actual;
3. how readers and interventions couple under the same law;
4. which records create genuine divisions;
5. how composites are formed;
6. how actuality is sampled;
7. what information and memory the law carries; and
8. why the construction is not an encoding of the target quantum process.

That is the surviving U0 source-completion problem. It is a physics problem,
not an invitation to tune another representation.

---

## 19. Authority ledger

\[
\begin{array}{ll}
\text{N1/N1A status} & \text{Nelson controls only}\\
\text{G1/G2 status} & \text{compiler/source-origin controls}\\
\text{PJ-A zero rate} & \text{prior art reconstructed}\\
\text{PJ-B first-order stall} & \text{author-side bounded theorem}\\
\text{PJ-C probability jets} & \text{author-side exact reconstruction}\\
\text{PJ-D triangle chirality} & \text{author-side exact control}\\
\text{PJ-E positive second order} & \text{compiler control}\\
\text{PJ-F spectral ODE} & \text{compiler control}\\
\text{native positive source law} & \text{absent}\\
\text{configuration ontology} & \text{unselected}\\
\text{fundamental complex structure} & \text{not inferred}\\
\text{external or emergent time} & \text{not inferred}\\
\text{U0-T4 / official pin / review} & \text{closed / not authorized}\\
\text{MG0 / gravity result} & \text{none}
\end{array}
\]
