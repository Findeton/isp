# ISP v17 — U-Gen U0 Barandes Markovian-embedding and complex-structure scope audit

**Status:** ACTIVE AUTHOR-SIDE SOURCE/MATHEMATICS AUDIT / NO CANDIDATE
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review/successor opened:** no

This companion to the U0 source-completion audit examines a newly relevant
Barandes argument: the proposal that the Hilbert-space formulation of quantum
theory is a Markovian embedding of an underlying indivisible stochastic
process, and that complex numbers are needed for that embedding.

The audit is deliberately charitable and strict. It preserves the important
ontological lesson that a wavefunction need not be material furniture, while
separating four claims that do not follow from one another:

1. a supplied stochastic matrix has a Hilbert/Born representation;
2. a supplied family of first-order transition matrices has a divisible
   state-space representation;
3. that representation predicts a complete controlled process;
4. one physical nomology generates the correct process for held-out systems,
   interventions, readers, and compositions.

The first claim is mathematically broad. The second requires compatibility
across a family, not just one matrix. The third requires intervention-complete
statistics. The fourth is U0's source-completion problem. None may be promoted
by changing the meaning of “embedding.”

This file inherits the binding Nelson-control correction. It assumes no
particle path, Euclidean configuration space, Brownian noise, Markov
divisibility, external time, Nelson coefficient, mean-Newton equation,
fundamental phase field, $U(1)$ target, bundle, or holonomy. It also does not
inherit a discrete carrier, trajectory ontology, or supplied time parameter
from the Barandes examples.

---

## 1. Version-bound primary sources

The source reconstruction below is limited to these versions, accessed on
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
4. Jacob A. Barandes, [*The Stochastic--Quantum
   Theorem*](https://arxiv.org/html/2309.03085v2),
   arXiv:2309.03085v2.
5. Felix A. Pollock, César Rodríguez-Rosario, Thomas Frauenheim, Mauro
   Paternostro, and Kavan Modi, [*Non-Markovian quantum processes: complete
   framework and efficient characterisation*](https://arxiv.org/abs/1512.00589),
   arXiv:1512.00589v3.
6. Felix A. Pollock, César Rodríguez-Rosario, Thomas Frauenheim, Mauro
   Paternostro, and Kavan Modi, [*Operational Markov condition for quantum
   processes*](https://arxiv.org/abs/1801.09811), arXiv:1801.09811v1.

The Barandes papers are active research manuscripts. This audit reconstructs
their printed claims and supplies elementary independent controls. It is not
an official peer review or a certification of the papers as wholes.

---

## 2. Executive verdict

The 2026 Markovian-embedding picture strengthens one central v17 intuition:

> Hilbert states and complex amplitudes can be secondary predictive
> coordinates rather than the material configuration of the world.

It does **not** fill U0's native-law slot. The construction begins after a
configuration space, time indexing, contingent distribution, and first-order
transition laws have been supplied. It neither chooses those laws for a new
physical system nor generates the complete controlled process across new
apparatus and intervention programs.

The complex-number claim also requires a scope correction:

1. some $N\times N$ unistochastic matrices have no same-size real orthogonal
   lift, so complex structure can be necessary under a fixed-size lift
   requirement;
2. every finite stochastic matrix nevertheless has a bounded **real
   orthogonal dilation** whose squared entries reproduce it after
   marginalization;
3. therefore a single endpoint stochastic matrix does not force complex
   structure;
4. a globally coherent, economical representation of smooth evolution,
   composition, counterfactual controls, and tensor structure may still force
   or strongly favor a compatible complex structure, but that is a different
   theorem and is not established by endpoint dilation alone.

The physically important open question is consequently not

```text
Can one take square roots of a stochastic table?
```

but

```text
Can one fixed ordinary-positive nomology generate a coherent family of
complete laws for all licensed interventions and compositions, such that a
Hilbert/complex description is reconstructed as their economical predictive
representation rather than supplied per experiment?
```

That is the Barandes-facing U0 question in its sharpest present form.

---

## 3. What the 2026 paper calls a Markovian embedding

The paper begins from a familiar nomology--ontology trade-off. A higher-order
law on configurations $x$ can be rewritten as a first-order law on an enlarged
state such as $(x,y)$. The enlarged variables store whatever past information
the first-order dynamics needs. Complex coordinates can package pairs of real
variables compactly.

For the quantum application, the printed indivisible model supplies fixed:

1. a configuration space $\mathcal C$;
2. target times $\mathcal T$ and conditioning times
   $\mathcal T_0\subseteq\mathcal T$;
3. first-order transition matrices

   $$
   \Gamma(t\leftarrow t_0):\mathcal C\times\mathcal C\to[0,1];
   $$

and supplies contingently:

4. standalone distributions $p(t)$.

The sparse law generally leaves many complete Kolmogorov towers compatible
with the same first-order transitions. Barandes calls these towers
non-Markovian realizers and treats the indivisible law as their equivalence
class at the first-order empirical scope.

For a finite $N$-configuration member, the Hilbert reconstruction starts from
the already supplied matrix $\Gamma$ and introduces a nonunique potential
$\Theta$ such that

$$
\Gamma_{ij}=|\Theta_{ij}|^2.
$$

If a same-size unitary lift is unavailable, Kraus and Stinespring/Naimark
dilation constructions enlarge the representation. With a sufficiently
regular unitary path $U(t\leftarrow0)$, the familiar Hamiltonian and
Schrödinger equation can be defined downstream.

This is a representation achievement. It does not derive $\Gamma$ from a
target-blind physical description.

---

## 4. Four distinct enlargement operations

The word “embedding” covers four mathematically and physically different
operations in the present programme.

| operation | input consumed | enlarged state | what it preserves | physical status |
|---|---|---|---|---|
| full-history Markovization | complete controlled law $Q$ | full observed prefix $h$ | all continuations of $Q$ | exact representation built from target |
| minimal predictive quotient | $Q$ plus licensed policy class | future-equivalence class $[h]_Q$ | all licensed future laws | smallest exact target-built predictor |
| Barandes/Hilbert lift | supplied sparse $\Gamma$ plus lift/dilation choices | density/state vector on enlarged linear space | represented $\Gamma$-level probabilities | secondary analytical mechanics |
| physical carrier enlargement | independently evidenced memory/reference degrees | enlarged physical configuration | whatever one nomology predicts | possible ontology; must pass source and intervention tests |

The first three can always be useful without being ontological. The fourth is
the only operation that can add physical explanatory content, and only when
the extra carrier is justified independently of the held-out answer.

The Barandes lift is not identical to full-history Markovization. It is built
from the sparse first-order law and therefore cannot recover distinctions
between complete realizers that the sparse law has quotiented away.

---

## 5. Proposition ME-A — a sparse-law representation cannot complete its own fiber

Let $\mathfrak Q$ be a class of complete controlled stochastic laws and let

$$
\pi:\mathfrak Q\to\mathfrak G
$$

forget all information except the sparse first-order indivisible law
$\Gamma=\pi(Q)$. Let a representation be any map

$$
R:\mathfrak G\to\mathfrak H.
$$

Suppose there exist $Q_1,Q_2\in\mathfrak Q$ such that

$$
Q_1\neq Q_2,
\qquad
\pi(Q_1)=\pi(Q_2)=\Gamma,
$$

and some licensed intervention/readout policy $\alpha$ distinguishes them:

$$
P_{Q_1}(\cdot\mid\alpha)
\neq
P_{Q_2}(\cdot\mid\alpha).
$$

Then no decoder $D$ acting only on $R(\Gamma)$ can return the correct complete
law for both $Q_1$ and $Q_2$.

### Proof

Because $\pi(Q_1)=\pi(Q_2)$,

$$
R(\pi(Q_1))=R(\Gamma)=R(\pi(Q_2)).
$$

Any fixed decoder receives the same input in the two cases, so it returns the
same output. That output cannot equal two distinct $\alpha$-conditioned laws.
$\square$

### Consequence

A Hilbert lift of the sparse first-order law may represent every statistic
that the declared sparse empirical quotient retains. It cannot, merely by
being a Hilbert lift, choose or reconstruct a complete realizer inside a
nontrivial fiber.

This is not a refutation of Barandes's declared scope. The 2025 paper openly
allows many realizers and suggests that the distinction may be physically
meaningless. U0 imposes a stronger empirical task: predict complete controlled
records for held-out interventions. Under that task, either:

1. all licensed interventions are proved constant on the realizer fiber; or
2. the native law must supply additional whole-process structure.

The first option is a theorem burden, not a verbal appeal to apparatus.

---

## 6. Apparatus inclusion and the moving-parent problem

Barandes's response to apparently missing phase information is physically
serious: include the measuring device and environment in the overall system,
choose configurations that include pointer records, and let the parent
stochastic law deliver the correct record probabilities.

For one fixed parent experiment, this can make isolated lift phases gauge.
It does not by itself supply the parent law for a *different* intervention.
If experiment $e$ and experiment $e'$ differ by inserting, removing, delaying,
or coherently controlling an apparatus operation, then the framework needs

$$
e\longmapsto\Gamma_e,
\qquad
e'\longmapsto\Gamma_{e'}
$$

under one fixed source rule. Supplying $\Gamma_e$ and $\Gamma_{e'}$
separately is a family of answers, not a source-complete nomology.

Thus “include the apparatus” has two readings:

1. **ontological closure:** apparatus and records are physical, not external
   classical primitives;
2. **nomological closure:** one law generates the changed parent whenever the
   apparatus program changes.

The sources strongly motivate the first. The second remains U0's open gate.

---

## 7. Proposition ME-B — a same-size complex lift can be genuinely stronger

Consider the $3\times3$ stochastic matrix

$$
\Gamma_3=\frac13
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix}.
$$

Let $F_3$ be the normalized complex Fourier matrix,

$$
(F_3)_{jk}=\frac{1}{\sqrt3}
\exp\!\left(\frac{2\pi i jk}{3}\right).
$$

Then $F_3$ is unitary and

$$
(\Gamma_3)_{jk}=|(F_3)_{jk}|^2,
$$

so $\Gamma_3$ is unistochastic.

There is no real $3\times3$ orthogonal matrix $O$ with

$$
(\Gamma_3)_{jk}=O_{jk}^2.
$$

### Proof

Such an $O$ would have every entry equal to $\pm1/\sqrt3$. The inner product
of any two distinct columns would therefore be one third of a sum of three
numbers, each equal to $+1$ or $-1$. A sum of three such numbers is odd and
cannot vanish. The columns cannot be orthogonal. $\square$

### Exact scope

This proves a genuine same-dimension distinction:

```text
same-size unitary lift:       exists
same-size real orthogonal lift: does not exist
```

It does not prove that every Markovian embedding, at every enlarged
dimension and under every allowed marginalization, requires complex numbers.

---

## 8. Proposition ME-C — every finite stochastic matrix has a real orthogonal dilation

Let $\Gamma$ be an $M\times L$ column-stochastic matrix. Put

$$
N=\max(M,L)
$$

and pad $\Gamma$ to an $N\times N$ column-stochastic matrix
$\widetilde\Gamma$ using the same harmless row/column extension as the 2026
Unistochastic Theorem.

For each $j=1,\dots,N$, define a vector $v_j\in\mathbb R^{N^2}$ with
coordinates indexed by $(i,k)$:

$$
(v_j)_{(i,k)}
=
\sqrt{\widetilde\Gamma_{ij}}\,\delta_{kj}.
$$

Then the $N$ vectors $v_1,\dots,v_N$ are orthonormal.

### Proof

For each $j$,

$$
\|v_j\|^2
=
\sum_{i,k}\widetilde\Gamma_{ij}\delta_{kj}
=
\sum_i\widetilde\Gamma_{ij}
=1.
$$

For $j\neq j'$, the supports lie in disjoint $k$ sectors, so
$\langle v_j,v_{j'}\rangle=0$. $\square$

Complete these real orthonormal vectors to a real orthonormal basis of
$\mathbb R^{N^2}$. Let $O\in O(N^2)$ be the orthogonal matrix whose columns
include

$$
O_{(i,k),(j,1)}=(v_j)_{(i,k)}.
$$

Then

$$
\boxed{
\Gamma_{ij}
=
\sum_{k=1}^{N}
O_{(i,k),(j,1)}^2
}
$$

for the original $i\le M$, $j\le L$.

Therefore every finite stochastic matrix is the stated marginal of an
orthostochastic matrix of dimension at most $N^2$.

### Relation to the cited theorem

This is already latent in the constructive proof of the 2026 Unistochastic
Theorem:

1. choose the potential $\Theta_{ij}=\sqrt{\widetilde\Gamma_{ij}}$ real;
2. its displayed Kraus columns are real;
3. complete those columns using Gram--Schmidt over the reals;
4. the resulting “unitary” matrix is in fact real orthogonal.

The result is not a criticism of the unistochastic theorem. Orthogonal
matrices are unitary, so it strengthens the endpoint representation claim.
It does, however, restrict what can be inferred about the necessity of complex
numbers from that endpoint theorem.

---

## 9. What Proposition ME-C does not show

The real dilation is deliberately narrow. It does not automatically provide:

1. a canonical choice of orthogonal completion;
2. a single fixed dilation space for an unbounded class of systems;
3. a smooth $O(t)$ for every supplied time-indexed family;
4. compatible composition for sequential controls;
5. local tensor composition for independent systems;
6. a reader calculus for arbitrary counterfactual measurements;
7. the full process statistics distinguished by inserted interventions;
8. a physical interpretation of the auxiliary coordinates;
9. a source rule for $\Gamma$.

Those missing compatibility requirements are precisely where complex
structure may re-enter as an economical, globally coherent predictive
language. They are also where merely dilating each endpoint matrix separately
becomes a compiler rather than a physical theory.

The correct conclusion is not “complex numbers are unnecessary.” It is:

> Endpoint representability alone does not decide the physical or even the
> globally predictive status of complex structure.

---

## 10. Three possible statuses of complex structure

U0 must keep three claims distinct.

### C1 — material complex ontology

The world is fundamentally made of complex amplitudes or a complex field.
Neither the stochastic--quantum correspondence nor the same-size obstruction
establishes this.

### C2 — algebraic structure of a chosen representation

A same-size Hilbert representation of some transition laws requires a linear
complex structure $J$ with $J^2=-I$. Proposition ME-B supports this at a
specific representation scope. A real $2N$ notation preserving such a fixed
$J$ is still algebraically complex; changing symbols does not remove the
structure.

### C3 — coherent predictive structure across counterfactuals

One compatible complex structure may be the minimal or natural way to encode
smooth evolution, reversible transformations, composition, and the outcomes
of many alternative interventions under one reusable law. This would make
complex Hilbert structure secondary but physically non-arbitrary, much as
Hamiltonian phase space can be secondary yet structurally powerful.

C3 is the most promising interpretation for v17, but it is presently a
theorem target, not a result. It must be earned from the family of complete
positive laws, not inserted as a wavefunction, action, phase, or holonomy.

---

## 11. The complete-process mismatch

The Barandes indivisible law deliberately records a sparse set of first-order
conditionals and leaves a fiber of compatible higher-order realizers. A
process tensor or equivalent complete operational law instead maps every
licensed sequence of interventions to its output statistics.

These objects answer different questions:

| object | answers | does not automatically answer |
|---|---|---|
| sparse $\Gamma(t\leftarrow t_0)$ | endpoint conditional distribution at licensed divisions | inserted multi-time interventions |
| complete realizer | one full Kolmogorov tower | which tower is physical |
| process tensor/comb | operational statistics for a licensed intervention class | ontology or source of the process |
| U0 native law | must generate the complete operational family from physical inputs | not yet constructed |

The absence of the word “intervention” from the main 2025/2026 indivisible
construction is not a semantic defect by itself; it marks the source scope.
U0 may not silently upgrade first-order endpoint completeness into controlled
process completeness.

If all apparatus is included, every intervention program can be represented
as a different enlarged parent experiment. The remaining physical burden is
to generate those parents coherently from one nomology.

---

## 12. Fixed nomology versus target answer

The Markovian-embedding audit does not strengthen U0's ban into a ban on
universal dynamics. A physical theory may contain fixed masses, couplings,
symmetry principles, constitutive constants, and one universal law. It must
also accept contingent state and licensed controls.

The forbidden move is per-target completion before the proposed law acts:

$$
\text{target }\Gamma_e, U_e, H_e, \Psi_e,
\text{ action}_e, \text{phase}_e,
\text{ or process}_e
\longrightarrow
\text{claimed derivation of the same target}.
$$

A fixed nomology receives credit only when the same frozen rule maps
independently specified physical descriptors to calibration and held-out
processes without refitting.

This boundary was already fixed by U0-T2. The 2026 paper adds no reason to
relax it.

---

## 13. Configuration, time, and actuality scope

The finite correspondence examples use an $N$-element configuration space,
real-valued external time labels, conditioning times, and language of a
trajectory in an old-fashioned configuration space. The broader 2025 paper
notes both discrete and continuous examples.

None of this selects U0's carrier. In particular:

1. finite $N$ is a theorem scope, not evidence that nature is a lattice;
2. continuous examples do not select a continuum ontology;
3. external time is supplied, not derived;
4. one actual trajectory is an actuality claim whose complete probability
   law remains underdetermined by sparse $\Gamma$;
5. a Hilbert dilation coordinate is not automatically a physical degree of
   freedom;
6. a full-history state is not automatically an ontic configuration.

U0 remains configuration-form neutral and must type actuality explicitly.

---

## 14. The coherent-family requirement

The source-completion map should be sharpened from an object-by-object rule to
a coherent rule on physical experiments. Let $\mathfrak E$ be a typed category
whose objects are independently specified systems, boundaries, controls, and
readers, and whose arrows include verified presentation changes, physical
control insertion, composition, coarse-graining, and record retention or
erasure where defined.

A native nomology $\mathcal N$ must generate

$$
\mathcal S_{\mathcal N}:\mathfrak E\longrightarrow\mathfrak P,
$$

where $\mathfrak P$ is a category of normalized complete ordinary-positive
process laws. The rule must satisfy the appropriate typed covariance and
composition equations rather than choose each $\Gamma_e$ independently.

Only after $\mathcal S_{\mathcal N}$ freezes may one ask whether a secondary
representation

$$
\mathcal H:\mathfrak P\longrightarrow\mathfrak{Hilb}
$$

is economical, coherent, and perhaps forced up to representation equivalence.

This order matters:

```text
physical descriptors -> native positive complete law -> optional Hilbert lift
```

is an explanatory architecture, whereas

```text
target Hilbert process -> modulus squares -> positive records
```

is a compiler/control.

---

## 15. Hostile controls for any future native proposal

Any future U0 proposal must survive at least these attacks.

1. **Endpoint-only lift:** reproduce $\Gamma(t\leftarrow0)$ but fail an
   inserted intermediate control.
2. **Per-program re-lift:** choose new dilation phases or auxiliary states
   after each target program is revealed.
3. **Apparatus migration:** answer every objection by enlarging the parent
   while supplying the enlarged parent's law by hand.
4. **Realizer ambiguity:** two complete positive laws share all supplied
   first-order transitions but differ under one licensed policy.
5. **Hidden external time:** call a time-indexed embedding relational without
   constructing a physical clock/readout relation.
6. **Discrete-carrier promotion:** infer microscopic discreteness from a
   finite theorem fixture.
7. **Continuum promotion:** infer fundamental continuity from a continuous
   example.
8. **Complex-necessity overclaim:** use Proposition ME-B while ignoring the
   real dilation in Proposition ME-C.
9. **Realification overclaim:** replace $i$ by a real matrix $J$ and claim the
   algebraic complex structure disappeared.
10. **Auxiliary ontology:** reify a nonunique dilation coordinate without an
    independent reader or intervention.
11. **Resource hiding:** allow dilation dimension, precision, or memory to
    scale like a target lookup table.
12. **Composition failure:** fit isolated systems while failing a held-out
    interacting parent.
13. **Counterfactual failure:** fit the performed experiment while failing a
    preregistered alternative control on the same source.
14. **Sparse/complete equivocation:** call an equivalence class of realizers a
    complete controlled process without proving policy invariance.
15. **Hilbert-by-renaming:** store the wavefunction or process tensor as a
    “positive configuration” or “reference state.”

---

## 16. Consequence for the v17 research front

The 2026 source changes the interpretation of the latest U0 result, not its
authority level.

### Strengthened

1. Hilbert ontology is not forced by the practical success of first-order
   state evolution.
2. Markovian state variables can be bookkeeping for non-Markovian predictive
   dependence.
3. Complex structure can be a representation-level resource rather than
   material substance.
4. The distinction between physical carrier enlargement and target-built
   predictive enlargement is load-bearing.

### Still missing

1. the physical configuration/referent domain;
2. the fixed source rule for the stochastic law;
3. complete intervention statistics;
4. interacting-parent generation;
5. coherent lift choices across programs and systems;
6. internal chronology;
7. a gravity-sensitive pair of fully specified matter laws.

### Explicitly not opened

1. U0-T4 or any official pin;
2. an N1B or Nelson repair;
3. a complex, real-plane, phase, bundle, or holonomy ontology;
4. a hardware programme;
5. a clock, spacetime, or gravity model;
6. an assertion that the Barandes ontology succeeds or fails globally.

---

## 17. Outcome ladder

```text
ME-L0  source reconstruction or elementary propositions fail
ME-L1  sparse-law/Hilbert representation boundary survives
ME-L2  same-size complex-vs-real distinction survives
ME-L3  bounded real orthogonal endpoint dilation survives
ME-L4  one coherent target-blind positive law spans held-out interventions
ME-L5  Hilbert/complex structure is reconstructed naturally from that family
ME-L6  scalable QFT processes and a novel empirical wedge survive
ME-L7  internal chronology and reciprocal matter-geometry dynamics survive
```

This author-side audit reaches ME-L3 as mathematics and source scope only.
ME-L4 and above remain open. No rung is a scientific result without an
authorized freeze and independent review.

---

## 18. Routing statement

```text
BARENDES HILBERT-SECONDARY THESIS:      STRENGTHENED AS A LIVE HYPOTHESIS
SPARSE INDIVISIBLE LAW:                 REPRESENTATION INPUT / NOT SOURCE LAW
COMPLETE REALIZER FROM SPARSE GAMMA:    NOT DETERMINED IN GENERAL
SAME-SIZE COMPLEX ADVANTAGE:            EXACT 3x3 WITNESS
FINITE ENDPOINT COMPLEX NECESSITY:      REFUTED UNDER BOUNDED DILATION
REAL ORTHOGONAL DILATION:               EXACT AT <= N^2
GLOBAL COHERENT COMPLEX STRUCTURE:      OPEN / MAY BE REPRESENTATION-NATURAL
UNIFORM COMPLETE-PROCESS GENERATOR:     ABSENT
CONFIGURATION FORM:                     UNSELECTED
EXTERNAL TIME INHERITANCE:              FORBIDDEN
N1/N1A ONTOLOGY INHERITANCE:            NONE
G1 STATUS:                              COMPILER/CONTROL
MG0 STATUS:                             GRAVITY PREFLIGHT ONLY
OFFICIAL PIN / REVIEW / SUCCESSOR:      NONE
```

---

## 19. Maximum legitimate claim

> Barandes's 2026 Markovian-embedding account gives a serious and physically
> illuminating reason not to identify Hilbert states with material ontology:
> a first-order Hilbert description can function as analytical mechanics for
> sparse indivisible stochastic laws. The cited construction still begins
> from supplied configuration, time, contingent state, and first-order
> transition data, and it does not generate held-out complete controlled
> processes. Moreover, although some stochastic matrices require complex
> amplitudes for a same-size unitary lift, every finite stochastic matrix has
> a bounded real orthogonal dilation after marginalization. Complex structure
> is therefore not forced by endpoint positivity alone. The live physical
> possibility is that one coherent complex structure is reconstructed as the
> economical predictive representation of a single target-blind family of
> complete positive laws across interventions and composition. Constructing
> that native family remains U0's open problem.
