# ISP v17 — U-Gen C1 pair-history composition candidate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS/ONTOLOGY CANDIDATE / NOT A PIN / NOT REVIEWED

**Date:** 2026-08-23

**Scientific result awarded:** none
**Authority created:** none

---

## 0. Physical correction under investigation

Paper 01 proves that ordinary probabilities on complete physical records can
represent every registered finite quantum process. PC2--PC6 show why this fact
does not yet explain quantum composition: the whole-process evaluator retains
phase-complete information that is absent from isolated positive endpoint
kernels.

The most economical known correction is not to make amplitudes into material
objects. It is to distinguish two levels of law:

1. **actual record probabilities**, which are ordinary and nonnegative on a
   stable record partition; and
2. **relations between alternative fine histories**, encoded by a
   decoherence functional or an equivalent pair-history kernel, which carries
   the information required to compose unresolved alternatives.

The candidate architecture is therefore

$$
\boxed{
\text{one actual history or record}
+\text{ pair-history nomology}
\longrightarrow
\text{ordinary probabilities at decoherent record boundaries}.}
$$

This is a known quantum-measure/history architecture, not a newly invented
theory and not yet an ISP ontology. U-Gen C1 asks exactly what it clarifies,
what it merely rewrites, and whether a Barandes-style $\Gamma$ can be recovered
as its record-level shadow.

---

## 1. Finite history law

Let $\Omega$ be a finite set of fine histories and $\mathcal A=2^\Omega$ its
event algebra. A decoherence functional is a map

$$
D:\mathcal A\times\mathcal A\longrightarrow\mathbb C
$$

that is:

1. Hermitian: $D(A,B)=\overline{D(B,A)}$;
2. additive in each argument over disjoint unions;
3. normalized: $D(\Omega,\Omega)=1$; and
4. weakly positive: $D(A,A)\ge0$.

Its diagonal quantum measure is

$$
\mu(A)=D(A,A)\ge0.
$$

$\mu$ is generally grade-2 additive, not an ordinary probability measure. For
pairwise disjoint $A,B,C$,

$$
\begin{aligned}
\mu(A\cup B\cup C)
={}&\mu(A\cup B)+\mu(A\cup C)+\mu(B\cup C)\\
&-\mu(A)-\mu(B)-\mu(C).
\end{aligned}
$$

$D$ is **strongly positive** when, for every finite family of events
$A_1,\ldots,A_m$, the matrix

$$
\bigl[D(A_i,A_j)\bigr]_{i,j=1}^m
$$

is positive semidefinite.

Strong positivity is stronger than nonnegativity of $\mu$. It makes $D$ a Gram
kernel and permits a history Hilbert-space representation. That representation
does not by itself make Hilbert vectors ontic.

---

## 2. Exact diagonal-noncomposition theorem

### Proposition C1-A

There are two finite strongly positive decoherence functionals with exactly
the same diagonal quantum measure on every event, but whose product composition
with the same fixed strongly positive system gives different quantum measures
for the same composite event.

### Construction

Let $\Omega=\{0,1\}$ and define, on the atomic events,

$$
D_+=
\begin{pmatrix}
\frac12&\frac{i}{4}\\
-\frac{i}{4}&\frac12
\end{pmatrix},
\qquad
D_-=
\begin{pmatrix}
\frac12&-\frac{i}{4}\\
\frac{i}{4}&\frac12
\end{pmatrix}.
$$

Extend both matrices to $2^\Omega\times2^\Omega$ by biadditivity. Their
eigenvalues are $3/4$ and $1/4$, so both are strongly positive. Their entries
sum to one, so both are normalized.

For either sign,

$$
\mu_\pm(\varnothing)=0,
\qquad
\mu_\pm(\{0\})=\mu_\pm(\{1\})=\frac12,
\qquad
\mu_\pm(\Omega)=1.
$$

Thus

$$
\mu_+=\mu_-
$$

on the complete event algebra. In fact this common diagonal is an ordinary
additive fair-bit probability measure.

Now fix a second system with $E=D_+$ and use the standard independent product
rule

$$
(D\otimes E)(A_1\times A_2,B_1\times B_2)
=D(A_1,B_1)E(A_2,B_2),
$$

extended by biadditivity. Let

$$
F=\{(0,0),(1,1)\}.
$$

Then

$$
\begin{aligned}
\mu_{D_+\otimes E}(F)
&=\frac14+\frac14-\frac1{16}-\frac1{16}
=\frac38,\\
\mu_{D_-\otimes E}(F)
&=\frac14+\frac14+\frac1{16}+\frac1{16}
=\frac58.
\end{aligned}
$$

Kronecker products of positive-semidefinite matrices are positive
semidefinite, so both composite systems remain strongly positive.

Therefore the common diagonal law does not determine the composite diagonal
law. QED.

### Corollary C1-A.1

Neither positivity, normalization, complete knowledge of the single-system
quantum measure, nor strong positivity selects the missing relational
orientation. A composition law needs the pair-history datum $D$, or another
object carrying equivalent information.

### Corollary C1-A.2

Even an ordinary additive law on all events of an isolated history space can
hide compositionally active information. “Every local history has an ordinary
probability” is therefore weaker than “the theory is classically complete
under composition.”

### Gauge qualification

$D_+$ and $D_-$ are complex conjugates. If every system, apparatus, boundary
condition, and reader is conjugated together, the change may be a presentation
symmetry. Proposition C1-A fixes the second system $E$ and the composite event
$F$. It detects a *relative* orientation. The result is relational
nonselection, not an assertion that an isolated absolute phase is physical.

---

## 3. Why a pair-history kernel reconstructs Hilbert structure

For a finite strongly positive $D$, quotient the free complex vector space on
events by the null vectors of the sesquilinear form

$$
\langle A,B\rangle_D=D(A,B).
$$

Completion gives a history Hilbert space $\mathcal H_D$. Equivalently, there is
a spanning vector-valued measure $\mathcal E$ such that

$$
D(A,B)=\langle\mathcal E(A),\mathcal E(B)\rangle,
\qquad
\mu(A)=\|\mathcal E(A)\|^2.
$$

For finite systems the minimal spanning representation is unique up to a
unitary isomorphism. In standard pure-state nonrelativistic quantum mechanics,
the history Hilbert space is naturally isomorphic, under the source
hypotheses, to the usual Hilbert space.

This cuts in both directions:

1. Hilbert space need not be assumed as the ontology; it can be a
   representation of pair-history relations.
2. Replacing Hilbert vectors by a strongly positive $D$ does not remove the
   quantum structure. It reconstructs it.

The explanatory question moves from “why a wavefunction?” to

> Why this event algebra, this decoherence functional, this composition law,
> and this actualization rule?

---

## 4. Composition selects a positivity class, not a dynamical member

Under the standard product rule for independent systems:

1. strong positivity is closed under tensor composition;
2. weak positivity alone is not closed;
3. the strongly positive class cannot be enlarged while remaining closed and
   containing all standard quantum decoherence functionals, in the finite
   theorem of Boes--Navascués; and
4. in the broader Dowker--Wilkes theorem, the strongly positive class is the
   unique tensor-closed Galois-self-dual class within their complex
   decoherence-functional landscape.

The qualifications are load bearing:

1. the product rule is assumed;
2. noninteracting, uncorrelated composition is the registered operation;
3. Galois self-duality is stronger than closure alone;
4. positive-entry functionals supply another tensor-closed class before the
   maximality condition;
5. the uniqueness theorem changes in a real-only landscape; and
6. none of these results selects the actual $D$, action, coupling constants,
   boundary state, or physical history space.

Composition therefore gives genuine framework evidence for strong
positivity. It is not a derivation of quantum dynamics.

---

## 5. Complete finite-circuit pair-history compiler

### 5.1 Reversible programme

Take any finite programme with externally supplied laboratory order in the
Paper 01 scope and compile its preparations, instruments, adaptive controls,
environment, and records
into one reversible dilation $U_p$. Choose a presentation basis only for the
calculation. Purify the initial state, or diagonalize its density operator and
carry its eigenlabel as the source label $s$. Insert basis resolutions at
declared unrecorded internal cuts.

A fine path $h$ contains:

1. the source basis label;
2. the internal basis label at every inserted resolution;
3. all physical setting and outcome records; and
4. a final system/environment/record basis label $f(h)$.

Let $A_p(h\mid s)$ be the product of the corresponding matrix elements of the
compiled programme for source label $s$, and let $\omega(s)$ be the source
mixture.

### 5.2 Pair kernel

On atomic fine histories define

$$
D_p(h,h')
=\sum_s\omega(s)
A_p(h\mid s)\overline{A_p(h'\mid s)}
\,\delta_{f(h),f(h')}.
$$

Extend by biadditivity to events. Normalization follows from unitarity:

$$
D_p(\Omega_p,\Omega_p)
=\sum_{s,f}\omega(s)
\left|\sum_{h:f(h)=f}A_p(h\mid s)\right|^2
=1.
$$

Strong positivity follows because every event matrix is a Gram matrix of the
vectors whose components are the coherent endpoint sums for $(s,f)$.

### 5.3 Physical record probabilities

Let $R_a$ be the event that the final physical record has value $a$. Orthogonal
record sectors imply

$$
D_p(R_a,R_b)=0
\qquad(a\ne b).
$$

Hence the record partition is decoherent and

$$
p(a\mid p)=D_p(R_a,R_a)
$$

is an ordinary normalized probability distribution. Coarse-graining records,
conditioning on a retained outcome, and adaptive substitution agree with the
Paper 01 operational law.

At an unrecorded internal cut, however, the fine alternatives need not
decohere. Their individual diagonals cannot be composed as stochastic restart
probabilities. Cross terms in $D_p$ are what restore $H^2=I$ instead of the
idempotent Markov endpoint law $|H|^{\odot2}$.

### 5.4 Sequential and parallel composition

Sequential programme composition glues the amplitude indices at the common
boundary before the diagonal record law is taken. Parallel independent
composition tensors the decoherence functionals. Entangled sources and
interacting gates are described by one parent $D_p$, not by factorizing an
interacting law.

This compiler is exact and uniform for the registered finite programmes. It is
also a direct reformulation of the quantum dilation and therefore receives no
explanatory-reduction credit by itself.

---

## 6. Relationship to Paper 01

Paper 01 evaluates the whole reversible programme and pushes the squared
amplitude to physical records:

$$
p_{\rm rec}(a)=
\sum_f
\left|\sum_{h:f(h)=f,\,r(h)=a}A_p(h)\right|^2.
$$

The pair-history compiler makes the suppressed dependency explicit:

$$
p_{\rm rec}(a)=
\sum_{h,h'\in R_a}D_p(h,h').
$$

Thus Paper 01's ordinary positive record law and U-Gen C1's pair-history law are
not competitors. They are two levels of the same known construction:

$$
D_p
\longrightarrow
\mu_p\text{ on fine-history events}
\longrightarrow
p_{\rm rec}\text{ on a decoherent record partition}.
$$

Paper 01 proves operational sufficiency of the last arrow. Proposition C1-A
proves that the diagonal object alone does not generally determine composition.

---

## 7. Candidate D-over-$\Gamma$ architecture

### 7.1 Derived division boundaries

Let $\mathcal B\subseteq\mathcal A$ be a Boolean record algebra on which

$$
D(A,B)=0
$$

for every pair of distinct atoms $A,B$ of the same registered partition. Then
$\mu|_{\mathcal B}$ is an ordinary probability measure.

For a positive-probability earlier record atom $B_j$ and a later compatible
record atom $A_i$, define, only when the joint record algebra is decoherent,

$$
\Gamma_{ij}
=\frac{\mu(A_i\cap B_j)}{\mu(B_j)}.
$$

The classical law of total probability then holds on that record algebra.
Such a boundary is a candidate **division boundary**.

At a cut whose alternatives still interfere, this conditionalization is not
licensed as a complete future-sufficient stochastic restart. That is the
candidate **nondivision** case.

### 7.2 Interpretation

On this architecture:

1. $D$ is the compositional nomological object;
2. a Barandes-style $\Gamma$ is a derived conditional law on decoherent record
   sectors;
3. stable records have ordinary probabilities;
4. unresolved alternatives are related by $D$ rather than assigned a joint
   Kolmogorov distribution; and
5. Hilbert space is a representation of the history kernel, not automatically
   a beable.

This would explain why $\Gamma$ can be indivisible and why its isolated
endpoint values do not compose: it is the diagonal shadow of a richer law.

### 7.3 Source wall

This hierarchy is a v17 candidate synthesis. The audited Barandes sources take
first-order $\Gamma$ laws as the native dynamical axiom and use nonunique
potential/Hilbert lifts. They do not state that a decoherence functional is the
fundamental law or that division is exactly decoherence of a history event
algebra.

U-Gen C1 must therefore test this bridge; it may not attribute it to Barandes.

---

## 8. Actuality remains open

A quantum measure is nonnegative but is not an ordinary probability measure on
fine histories. It therefore does not by itself sample one fine history.

Sorkin's quantum-measure programme proposes one real history and interprets
zero-measure events through preclusion. The published programme explicitly
leaves aspects of conditional preclusion and the interpretation unfinished;
later coevent schemes are additional physical postulates, not consequences of
strong positivity alone.

For U-Gen C1 the alternatives are printed separately:

1. one actual **record** is sampled only after a decoherent record partition is
   formed;
2. one actual **fine history** is postulated with an additional preclusion or
   coevent rule;
3. actuality is not specified and $D$ remains only a predictive law; or
4. an empirically distinct actualization dynamics is proposed.

No option is silently selected.

---

## 9. Action-generated law and explanatory accounting

In known quantum mechanics and field theory a pair-history law can be generated
schematically from an action and boundary data:

$$
D(A,B)
\sim
\int_A\mathcal D\phi
\int_B\mathcal D\phi'
\exp\left(\frac{i}{\hbar}
[S[\phi]-S[\phi']]
\right)
\,\rho_{\rm bdry}(\phi,\phi').
$$

This forward/backward structure is the natural histories analogue of the Born
rule. It is uniform and can be far smaller than a table of complete-process
answers. But it receives explanatory credit only for inputs it truly derives.
The action still supplies:

1. field content;
2. couplings and masses;
3. interaction structure;
4. background or dynamical geometry;
5. boundary/cosmological data; and
6. the complex phase and $\hbar$.

Writing these inputs as $D$ does not explain why nature chose them. A genuine
advance would derive some of them from independently motivated principles or
predict a held-out deviation.

---

## 10. Gravity relevance and ceiling

History/event-algebra language is compatible with covariant formulations and
does not require a preferred Hamiltonian foliation. The history space could in
principle contain matter fields and geometries rather than circuit states.
This makes the architecture relevant to the eventual unification problem.

Nothing in U-Gen C1 yet supplies:

1. a history space of physical geometries;
2. diffeomorphism gauge and observables;
3. a well-defined gravitational path-integral measure;
4. causal orientation or Lorentzian signature;
5. Einstein dynamics or a semiclassical limit;
6. matter backreaction;
7. scale, clocks, or empirical quantum-gravity predictions; or
8. an actualization rule for fluctuating geometry.

No lattice, causal set, discrete web, or continuum is assumed by this
candidate.

---

## 11. Candidate result coordinates

If independently accepted later, the exact new mathematical coordinate could
be no stronger than:

```text
P17-UGEN-C1-DIAGONAL-HISTORY-LAW-NONCOMPOSITION
```

with the statement:

> Complete single-system diagonal history propensities, even when ordinary
> additive and arising from strongly positive systems, do not determine the
> diagonal law of a composite system under the standard product rule.

The pair-history compiler coordinate would be:

```text
P17-UGEN-C1-PAIR-HISTORY-QUANTUM-COMPLETION
```

with the ceiling:

> A strongly positive pair-history kernel uniformly reconstructs the complete
> finite circuit record law, but is representation-equivalent to the supplied
> quantum process and does not select dynamics, ontology, actuality, time, or
> gravity.

No scientific result is awarded by this author-side candidate.
