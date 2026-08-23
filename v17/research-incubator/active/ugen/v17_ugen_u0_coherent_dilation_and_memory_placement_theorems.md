# ISP v17 — U-Gen U0 coherent dilation and memory-placement theorems

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS/SOURCE AUDIT / NO CANDIDATE
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review/U0-T4 opened:** no

The Barandes Markovian-embedding audit proves that every finite stochastic
matrix has an objectwise real orthogonal dilation. Physics, however, does not
ask only whether each endpoint table can be embedded separately. It asks
whether one law composes across actual procedures without silently receiving
a fresh environment, a new lift, or the target continuation at every step.

This file isolates that difference with exact elementary theorems. Its central
conclusion is:

> Reversible dilation can relocate stochastic irreversibility into memory,
> correlation, discarded environment, or an unlicensed seam. It cannot make
> that information disappear. Complex Hilbert structure does not evade this
> fact; it supplies a different composition calculus whose extra seam data
> are not determined by endpoint probabilities.

The result supports rather than refutes Barandes-style indivisibility. It
shows why the division structure and physical carrier must be typed before a
Markovian embedding is treated as ontology. It does not generate the native
whole-process law.

This packet inherits no Nelson trajectory, Euclidean space, Brownian noise,
external time, phase field, action, holonomy, discrete lattice, continuum, or
Hilbert ontology. It does not infer thermodynamic heat from logical
information loss without separately stated thermodynamic premises.

---

## 1. Version-bound source boundary

The physical interpretation is checked against these sources, accessed on
2026-08-23:

1. Jacob A. Barandes, [*A Deflationary Account of Quantum Theory and its
   Implications for the Complex Numbers*](https://arxiv.org/html/2602.01043v1),
   arXiv:2602.01043v1.
2. Jacob A. Barandes, [*Quantum Systems as Indivisible Stochastic
   Processes*](https://arxiv.org/html/2507.21192v1),
   arXiv:2507.21192v1.
3. Jacob A. Barandes, [*The Born Representation Theorem and the
   Unistochastic Theorem*](https://arxiv.org/html/2608.04354v1),
   arXiv:2608.04354v1.
4. Charles H. Bennett, [*Logical Reversibility of
   Computation*](https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/bennett73.html),
   *IBM Journal of Research and Development* **17**, 525--532 (1973),
   DOI 10.1147/rd.176.0525.
5. Rolf Landauer, [*Irreversibility and Heat Generation in the Computing
   Process*](https://www.cpt.univ-mrs.fr/~verga/pdfs/Landauer-1961uq.pdf),
   *IBM Journal of Research and Development* **5**, 183--191 (1961),
   DOI 10.1147/rd.53.0183.
6. Felix A. Pollock et al., [*Operational Markov condition for quantum
   processes*](https://arxiv.org/abs/1801.09811), arXiv:1801.09811v1.

Bennett gives the relevant constructive lesson: reversible simulation saves
intermediate information and later uncomputes it. Landauer gives a
thermodynamic lesson about physical erasure under stated conditions. The
logical theorems below are self-contained and do not depend on Landauer's
thermodynamic conclusion.

---

## 2. Three composition questions

Let $\mathsf{Stoch}_N$ denote the monoid of $N\times N$ column-stochastic
matrices under ordinary multiplication. Three questions must remain distinct.

### Q1 — endpoint dilation

For a given $\Gamma\in\mathsf{Stoch}_N$, does there exist a reversible matrix
$V_\Gamma$ on a larger space whose readout marginal equals $\Gamma$?

The preceding audit answers yes at finite scope, over either the reals or the
complex numbers.

### Q2 — composition-preserving section

Can the choices $\Gamma\mapsto V_\Gamma$ be made once and for all so that

$$
V_{\Gamma_2\Gamma_1}
=
V_{\Gamma_2}V_{\Gamma_1}
$$

while the identity lifts to the reversible identity and readout recovers each
$\Gamma$?

Theorem CD-A answers no on any stochastic monoid containing a nontrivial
idempotent.

### Q3 — physical sequential reuse

Can one physical environment be prepared once, reused through a sequence, and
returned clean after each irreversible system operation without retaining the
lost information?

Theorems CD-B--CD-D answer no for exact reversible realizations. The missing
information must be retained, correlated, exported, reset, or made irrelevant
by restricting the operation class.

None of these questions asks whether a target complete process can be written
in Hilbert space. They ask where its composition information resides.

---

## 3. Definition — reversible section of stochastic composition

Let $\mathsf S\subseteq\mathsf{Stoch}_N$ be a submonoid containing $I_N$.
Let $\mathsf G$ be a group of reversible transformations, with identity
$e_{\mathsf G}$. Let

$$
q:\mathsf G\longrightarrow\mathsf S
$$

be a declared readout map satisfying

$$
q(e_{\mathsf G})=I_N.
$$

A **composition-preserving reversible section** is a map

$$
s:\mathsf S\longrightarrow\mathsf G
$$

such that, for all $A,B\in\mathsf S$,

$$
q(s(A))=A,
\qquad
s(AB)=s(A)s(B),
\qquad
s(I_N)=e_{\mathsf G}.
$$

The group may be unitary, orthogonal, symplectic, permutation-valued, or an
abstract reversible group. No modulus-square form is required for the
theorem.

---

## 4. Theorem CD-A — nontrivial stochastic idempotents forbid a reversible section

Suppose $\mathsf S$ contains an idempotent $E$ with

$$
E^2=E,
\qquad
E\neq I_N.
$$

Then no composition-preserving reversible section exists.

### Proof

If a section existed, then

$$
s(E)=s(E^2)=s(E)^2.
$$

Because $s(E)$ lies in a group, multiply by $s(E)^{-1}$ to obtain

$$
s(E)=e_{\mathsf G}.
$$

Applying the readout map gives

$$
E=q(s(E))=q(e_{\mathsf G})=I_N,
$$

contradicting $E\neq I_N$. $\square$

### Exact witnesses

For $N>1$, both of the following are nontrivial stochastic idempotents:

1. complete mixing,

   $$
   G_N=\frac1N\mathbf 1\mathbf 1^{\mathsf T},
   \qquad
   G_N^2=G_N;
   $$

2. deterministic erasure to configuration $1$,

   $$
   (E_1)_{ij}=\delta_{i1},
   \qquad
   E_1^2=E_1.
   $$

Thus no group-valued lift can simultaneously be a section of the endpoint
readout and a homomorphism for ordinary stochastic multiplication on a class
containing either operation.

### Scope

The theorem does not say that a reversible dilation of $E$ is impossible.
It says that the dilation cannot be both:

1. a group element selected only by the reduced endpoint map; and
2. composition-preserving under the reduced stochastic product.

Extra environment state, correlations, history, context, or a different
composition law can evade the theorem, but each is new structure that must be
typed and charged.

---

## 5. Corollary CD-A1 — complex amplitudes do not repair the section

Theorem CD-A applies when $\mathsf G$ is a unitary group over $\mathbb C$ and
$q$ is any readout with $q(I)=I_N$. Therefore allowing complex amplitudes does
not create a composition-preserving section of ordinary stochastic
multiplication.

Quantum composition avoids the contradiction in a different way:

$$
q(U_2U_1)
\neq
q(U_2)q(U_1)
$$

in general. The left-hand side retains interference through the unobserved
seam; the right-hand side inserts an ordinary stochastic restart there.

This inequality is not a defect. It is the exact distinction between a
coherent unrecorded seam and a division boundary. But it also means that the
endpoint matrices $q(U_1)$ and $q(U_2)$ do not determine the coherent product.
The lift carries additional relational composition data.

Complex structure can organize that data. It does not derive the data from
the endpoint probabilities.

---

## 6. Corollary CD-A2 — the only free reduced reversible case is the permutation sector

If every $A\in\mathsf S$ has a stochastic inverse in $\mathsf S$, then every
$A$ is a permutation matrix. This is the finite positive-inverse theorem
already used by PC5 and the U0 history-state packet.

Consequently:

1. a functorial reversible-positive representation is straightforward on a
   permutation group;
2. nontrivial mixing, erasure, and probabilistic coarse-graining lie outside
   that free sector;
3. representing them reversibly requires an environment or a non-reduced
   whole-process description.

This locates the burden without asserting that fundamental dynamics must be
reversible.

---

## 7. Definition — clean reusable environment

Let $X$ be a finite system carrier and $M$ a finite memory/environment
carrier. Fix a clean memory state $m_0\in M$. Let

$$
R:X\times M\longrightarrow X\times M
$$

be a bijection.

For a deterministic system map $f:X\to X$, say that $R$ implements $f$ with
an **exactly clean reusable environment** when

$$
R(x,m_0)=(f(x),m_0)
$$

for every $x\in X$.

The requirement is intentionally strong: the same microscopic environment is
ready for immediate exact reuse, is uncorrelated with the system, and carries
no input-dependent record.

---

## 8. Theorem CD-B — clean reusable reversible implementation implies injectivity

If a bijection $R$ implements $f$ with an exactly clean reusable environment,
then $f$ is injective. For finite $X$, $f$ is therefore a permutation.

### Proof

Suppose $f(x)=f(x')$. Then

$$
R(x,m_0)
=
(f(x),m_0)
=
(f(x'),m_0)
=
R(x',m_0).
$$

Injectivity of $R$ implies $x=x'$. Hence $f$ is injective. $\square$

### Meaning

An exactly reversible implementation of a many-to-one operation cannot return
all of its auxiliary degrees of freedom to one input-independent clean
microstate. Something must retain which preimage occurred.

This is a logical information statement. It does not by itself assign heat,
energy, entropy production, or a spacetime volume.

---

## 9. Theorem CD-C — exact memory cardinality lower bound

Relax the clean-return condition and suppose instead that

$$
R(x,m_0)=(f(x),\mu(x))
$$

for a memory record $\mu:X\to M$, while $R$ remains injective.

Then, for every $y\in f(X)$, the restriction

$$
\mu|_{f^{-1}(y)}
$$

is injective. Therefore

$$
\boxed{
|M|
\ge
\max_{y\in f(X)}|f^{-1}(y)|
}.
$$

### Proof

If $x,x'\in f^{-1}(y)$ and $\mu(x)=\mu(x')$, then

$$
R(x,m_0)=(y,\mu(x))=(y,\mu(x'))=R(x',m_0).
$$

Injectivity of $R$ gives $x=x'$. Thus the memory records distinguish every
preimage in each fiber. $\square$

### Erasure witness

If $f$ erases $k$ independent bits to one fixed output, then one fiber has
size $2^k$. Any exact reversible implementation needs at least $2^k$
distinguishable memory states, or at least $k$ bits of logical capacity.

The information has moved; it has not vanished.

---

## 10. Corollary CD-C1 — repeated irreversible operations require growth, reset, or uncomputation

Consider $r$ independent uses that erase inputs with maximal fiber sizes
$d_1,\dots,d_r$, while preserving all produced outputs and never resetting or
uncomputing the memory. The combined preimage fiber has size at least

$$
\prod_{a=1}^{r}d_a.
$$

Hence the retained environment requires at least

$$
\sum_{a=1}^{r}\log_2 d_a
$$

bits of distinguishability.

Within this exact finite reversible, independent-use setup, four generic
exits exhaust the stated information-placement alternatives:

1. supply fresh memory;
2. reset/export the old memory;
3. reversibly uncompute it using retained inputs and outputs; or
4. restrict the operations so the combined map is injective.

A fundamentally irreversible parent, an approximate implementation, or a
different physical carrier lies outside the theorem's premises rather than
constituting a fifth reversible exit.

Bennett's reversible simulation uses the third route: save history, copy the
desired output, then retrace the computation to clean the work tapes. It does
not erase history for free.

---

## 11. Proposition CD-D — stochastic dilation retains seed or correlation

A stochastic map can be realized by adjoining a random seed $r$ and a
deterministic map

$$
y=F(x,r).
$$

If the joint implementation is reversible, then the final joint state must
retain enough information to distinguish every admitted pair $(x,r)$. Even
when the environment marginal distribution returns to its original form, it
may retain:

1. the seed value;
2. a correlation with the system output;
3. a record of the input fiber; or
4. a dependence on earlier uses.

Therefore equality of the environment's marginal distribution before and
after a step is weaker than clean reusable independence. A catalytic-looking
marginal can hide correlation and memory.

This proposition prevents the mutant inference

```text
same environment marginal => no information left the system.
```

No thermodynamic cost is inferred until a physical reset protocol,
temperature, bath, and accuracy regime are supplied.

---

## 12. Linear/Hilbert analogue

Let $V:\mathcal H_S\to\mathcal H_S\otimes\mathcal H_M$ be an isometry. If
there is one fixed unit vector $|m_0\rangle$ and a linear map $W$ such that

$$
V|\psi\rangle
=
W|\psi\rangle\otimes|m_0\rangle
$$

for every $|\psi\rangle$, then preservation of inner products by $V$ implies
that $W$ is an isometry. When input and output system dimensions agree, $W$ is
unitary.

Thus a nonunitary reduced channel cannot arise from a dilation whose
environment returns to the same uncorrelated pure state for every input. Its
Stinespring environment must retain input-dependent information or
correlation, or else the channel was already isometric.

Again, real versus complex scalars do not change this conclusion.

---

## 13. Objectwise dilation versus one physical history

The real orthogonal endpoint construction in the preceding audit chooses, for
each $\Gamma$:

1. square-root columns;
2. an enlarged carrier;
3. an orthogonal completion; and
4. a selected clean input sector.

Those choices prove existence for one table. They do not state what happens
to the auxiliary coordinates after use or how the completion for
$\Gamma_2\Gamma_1$ relates to those for $\Gamma_1$ and $\Gamma_2$.

If each experimental step receives a fresh clean auxiliary state, that supply
is a physical resource. If the auxiliary state is carried forward, it becomes
memory and the reduced system dynamics is generally non-Markovian. If it is
discarded or reset, the environment interface must be included in the
complete parent. If a new completion is chosen after the target program is
known, the construction is a compiler.

Objectwise dilation is therefore a representation theorem, not a composition
law.

---

## 14. The Barandes-facing interpretation

Barandes's central move is to deny that every intermediate target time is a
valid conditioning or division time. Theorems CD-A--CD-D explain why this is
physically coherent:

1. marginalizing a reversible parent can hide environment memory;
2. inserting an ordinary stochastic restart at that seam discards the hidden
   correlation;
3. the product of reduced transition matrices then need not equal the
   unbroken whole-process transition;
4. a genuine division event requires a physical condition under which the
   admitted boundary state is future sufficient for the tested interface.

The theorems do **not** prove that the accepted Barandes ontology is complete.
They leave open:

1. which physical carrier is source closed;
2. which seams are divisions;
3. what one native law generates the whole process;
4. whether fine trajectories, division-boundary configurations, or only the
   law-level equivalence class are actual;
5. how interventions and readers change the parent law;
6. how the construction scales to QFT and gravity.

Indivisibility correctly diagnoses a possible composition failure. It does
not select the process member.

---

## 15. Recorded seam, unrecorded seam, and erasure

The following physical distinctions must not be replaced by algebraic
shorthand.

### Recorded division

A stable intermediate record may provide a future-sufficient boundary after
all evidenced memories are included. Ordinary conditional recomposition can
then be tested.

### Unrecorded coherent seam

No physical restart is inserted. The whole parent law determines the final
record, and reduced endpoint matrices need not multiply.

### Physical erasure

A record carrier is reset or its distinguishability is exported. In a closed
parent description the information moves into other degrees of freedom; it is
not removed from bijective microdynamics.

### Reversible uncomputation

The record-making interaction is coherently undone, allowing alternatives to
recombine. This is different from thermodynamic erasure and can restore an
interference-sensitive continuation.

A future U0 fixture must distinguish all four experimentally.

---

## 16. Why this does not select deterministic reversible ontology

The information-retention theorems are conditional:

```text
IF the parent implementation is exact and reversible,
THEN lost reduced information appears elsewhere.
```

They do not prove that fundamental reality is deterministic, reversible, or
unitary. A genuinely stochastic whole law may be fundamental. Objective
collapse may be real. A non-Kolmogorov history law may be fundamental. The
universe may have no exact microscopic inverse.

The theorem packet merely prevents a reversible dilation from being counted
as a free explanation of irreversibility or stochasticity.

---

## 17. Why this does not select complex ontology

Both orthogonal and unitary groups are groups, so Theorem CD-A applies to
both. Both real and complex isometries obey the clean-environment result.

Complex Hilbert structure earns a more modest role:

1. it can encode coherent seam data compactly;
2. it supports smooth reversible composition and the standard quantum
   predictive calculus;
3. it can be secondary to an underlying positive law;
4. its specific lift member is not determined by endpoint probabilities;
5. its ontological status is not fixed by representation efficiency.

The live theorem target remains whether a single positive source law produces
a family whose minimal coherent predictive representation has one compatible
complex structure. That cannot be answered by choosing a unitary separately
for each $\Gamma$.

---

## 18. Resource ledger

Any claimed coherent dilation must print at least:

| coordinate | required question |
|---|---|
| carrier | what system and environment variables exist? |
| preparation | who supplies the clean or random auxiliary state? |
| memory | what input/seed/history distinguishability remains after use? |
| correlation | is the environment merely marginally restored or product-clean? |
| composition | does the same joint law act on the next step? |
| reset | what physical map restores reusable conditions? |
| uncomputation | which outputs/inputs are retained to reverse the interaction? |
| context | does the dilation depend on the target program or implementation? |
| precision | what exactness and continuous parameter resolution are required? |
| scaling | how do carrier size and retained information grow with depth? |
| reader | which joint variables are physically accessible? |
| actuality | which joint configuration or law-level object is claimed real? |

Dimension, bits, entropy, heat, energy, time, and spacetime volume remain
separate resource coordinates unless an explicit physical bridge is proved.

---

## 19. Hostile controls

At minimum, a future coherent-family proposal must survive:

1. **idempotent section mutant:** claim a group-valued multiplicative section
   on a class containing mixing or erasure;
2. **fresh-ancilla laundering:** silently prepare a new auxiliary state for
   every step;
3. **marginal-reset mutant:** equate restored environment marginal with a
   clean uncorrelated environment;
4. **hidden-seed mutant:** leave the random seed in the environment but charge
   no memory;
5. **history-tape mutant:** store every prior result while calling the reduced
   system Markovian and resource free;
6. **thermodynamic overclaim:** infer $kT\ln2$ without a bath, temperature,
   reset, error, and asymptotic protocol;
7. **uncomputation/erasure conflation:** call coherent reversal physical
   destruction of a record;
8. **complex cure mutant:** claim complex scalars make ordinary stochastic
   multiplication functorial;
9. **real cure mutant:** claim orthogonal dilation supplies canonical
   composition;
10. **per-target completion:** choose a different orthogonal/unitary completion
    after each program is revealed;
11. **environment omission:** test future sufficiency on a subsystem while an
    evidenced memory remains coupled;
12. **arbitrary-hidden-state escape:** add a target-built history variable
    with no independent physical source;
13. **permutation overreach:** extend a theorem about finite positive inverses
    to continuous or genuinely stochastic whole laws;
14. **reversibility promotion:** infer reversible fundamental ontology from a
    conditional dilation theorem;
15. **record-free composition:** multiply reduced endpoint tables across an
    unrecorded seam;
16. **apparatus migration:** enlarge the parent for every objection while
    supplying each enlarged law independently;
17. **resource-name substitution:** report Hilbert dimension as physical bits,
    heat, or volume without a bridge;
18. **source omission:** solve where information can live while never
    generating the process law.

---

## 20. Outcome ladder

```text
CD-L0  an elementary section or memory theorem fails
CD-L1  objectwise dilation is separated from coherent composition
CD-L2  idempotent no-section and clean-memory bounds survive
CD-L3  one target-blind physical carrier and reset/uncompute grammar is found
CD-L4  one fixed positive law predicts held-out recorded/unrecorded/erased seams
CD-L5  scalable adaptive and composite quantum processes survive
CD-L6  the secondary Hilbert/complex representation is reconstructed naturally
CD-L7  QFT transfer and a novel empirical wedge survive
CD-L8  internal chronology and reciprocal matter--geometry dynamics survive
```

This packet reaches CD-L2 author-side only. It does not construct CD-L3.

---

## 21. Routing consequence

The exact result narrows the next physical construction target. It is not
“find another dilation.” It is:

> Identify an independently physical carrier and a single source law whose
> complete parent dynamics predicts when memory is retained, recorded,
> erased, or uncomputed, and whose held-out whole-process laws compose only at
> physically licensed divisions.

The construction must not receive the target complete process or target lift.
It may use fixed universal nomology and independently calibrated contingent
state and controls under U0-T2.

This is a sharpening of the existing U0 source-completion gate, not U0-T4 and
not authorization for an implementation programme.

---

## 22. Present disposition

```text
OBJECTWISE FINITE REVERSIBLE DILATION:  EXISTS / REPRESENTATION ONLY
COMPOSITION-PRESERVING GROUP SECTION:   IMPOSSIBLE WITH NONTRIVIAL IDEMPOTENT
CLEAN REUSABLE EXACT ENVIRONMENT:       ONLY FOR INJECTIVE SYSTEM MAPS
MEMORY FOR MANY-TO-ONE MAP:             >= MAX PREIMAGE FIBER
REPEATED LOSS WITHOUT RESET:            LOGICAL CAPACITY GROWS ADDITIVELY
SAME ENVIRONMENT MARGINAL:              DOES NOT PROVE MEMORY ABSENCE
THERMODYNAMIC HEAT CLAIM:               NOT EARNED WITHOUT PHYSICAL PREMISES
COMPLEX STRUCTURE:                      DOES NOT REPAIR STOCHASTIC FUNCTORIALITY
BARENDES INDIVISIBILITY:                PHYSICALLY MOTIVATED / LAW UNSELECTED
NATIVE COMPLETE-PROCESS SOURCE LAW:     ABSENT
CONFIGURATION FORM:                     UNSELECTED
OFFICIAL PIN / REVIEW / U0-T4:          NONE
```

---

## 23. Maximum legitimate claim

> A reversible dilation of one stochastic endpoint table does not provide a
> coherent physical composition law for free. Any submonoid containing a
> nonidentity stochastic idempotent admits no group-valued
> composition-preserving section. At the implementation level, an exact
> reversible realization of a many-to-one operation must retain enough
> environment information to distinguish the collapsed input fiber; repeated
> uses require fresh capacity, reset/export, or reversible uncomputation.
> These facts hold over both real and complex representations. They explain
> why an unrecorded seam can be indivisible and why Hilbert amplitudes may
> carry extra coherent composition data, but they neither select those data
> nor generate the native positive whole-process law. The next physical
> burden is a target-blind source law on an independently warranted carrier
> with a typed record, memory, erasure, and division grammar.
