# ISP v17 — phase-sensitive composition investigation

## From indivisible endpoint laws to one uniform quantum nomology

**Status:** ACTIVE AUTHOR-SIDE / RESULT-NEUTRAL INVESTIGATION / NOT A PIN
**Date:** 2026-08-23
**Scientific result awarded:** none
**Official authority created:** none

This note records the constructive question exposed by E-Comp. It does not
propose a new physical law, identify complex amplitudes as beables, reopen
Paper 04B, or authorize chronology, spacetime, QFT, or gravity.

---

## 1. Empirical fact and exact obstruction

Quantum experiments require phase-sensitive sequential composition. In the
balanced-qubit control, the positive endpoint map

$$
q(U)=|U|^{\odot2}
$$

obeys

$$
q(H)=q(V)=G,
$$

but

$$
q(H^2)=I_2,
\qquad
q(V^2)=X,
\qquad
q(H)^2=q(V)^2=G.
$$

More generally, the family

$$
U_\theta
=
\frac1{\sqrt2}
\begin{pmatrix}
1&e^{i\theta}\\
e^{i\theta}&-e^{2i\theta}
\end{pmatrix}
$$

has one common isolated endpoint $G$ and the two-step family

$$
q(U_\theta^2)
=
\begin{pmatrix}
\cos^2\theta&\sin^2\theta\\
\sin^2\theta&\cos^2\theta
\end{pmatrix}.
$$

Therefore the passage from coherent processes to positive endpoint matrices is
not compositional. In exact algebraic language, the equivalence relation

$$
U\sim V\quad\Longleftrightarrow\quad q(U)=q(V)
$$

is not a congruence for multiplication: $H\sim V$ but
$H^2\not\sim V^2$. Hence no endpoint-only product $\star$ can obey
$q(U_2U_1)=q(U_2)\star q(U_1)$ for all unitaries. The positive quotient
forgets information later revealed by coherent continuation.

This does not show that positive whole-history laws are impossible. It shows
that a whole-history law must carry, generate, or otherwise account for the
forgotten composition information.

---

## 2. The missing object

The target is one uniform law packet $\mathfrak A$ with:

1. a typed assignment to every admitted physical preparation, process,
   intervention, record, and reader;
2. sequential and parallel composition;
3. complete adaptive and post-measurement continuation laws;
4. a positive completed-record projection equal to observed probabilities;
5. gauge covariance across every complete experiment;
6. one finite or otherwise physically charged generator rather than a fresh
   table for every program;
7. scaling under system size and circuit depth; and
8. an explicit statement of which ingredients are law, contingent state,
   physical configuration, record, and representation.

The central diagram is not expected to commute at the positive primitive
level:

$$
\begin{array}{ccc}
\text{phase-sensitive processes}&\xrightarrow{\ \circ\ }&
\text{phase-sensitive processes}\\
\downarrow q&&\downarrow q\\
\text{positive endpoints}&\not\xrightarrow{\ \text{kernel product}\ }&
\text{correct positive whole law}.
\end{array}
$$

A successful theory must replace the crossed lower arrow by a lawfully
generated whole-process assignment.

---

## 3. Composition-lift formulation

The fiber $q^{-1}(G)$ contains many coherent lifts. A pointwise lift is
insufficient because independently choosing representatives need not respect
wiring. The neutral mathematical problem is to classify the extra structure
that makes composition well defined over the typed experiment category. A
gauge-covariant composition connection is one candidate representation of
that structure, not the assumed answer.

This language can be made exact in several nonequivalent ways:

1. a functor into a dagger symmetric monoidal process category followed by a
   completed-record probability functor;
2. a groupoid extension whose cocycle records the obstruction to composing
   positive endpoint representatives;
3. a path-amplitude rule with sum and product laws followed by a Born map;
4. a direct positive whole-program law satisfying equivalent coherence
   identities without treating amplitudes as ontology; or
5. a larger physical carrier whose lawful marginal realizes the required
   connection, with all extra resources charged.

These are research branches, not synonyms. The gate must determine their
operational equivalences, empirical content, and ontology costs rather than
select one by taste.

---

## 4. Existing-physics routes to test

### Route A — process-category reconstruction

Categorical quantum mechanics treats systems and processes through sequential
and tensor composition, with scalars and the Born rule emerging from additional
structure. This is directly relevant because E-Comp is a failure of the
positive endpoint quotient to preserve process composition.

The v17 question is not whether Hilbert spaces form a suitable category. They
do. It is whether the required categorical structure can be stated as an
independently physical law of configurations and interactions, or whether the
full quantum process category must simply be supplied.

Primary route:

- S. Abramsky and B. Coecke, *A categorical semantics of quantum protocols*:
  <https://arxiv.org/abs/quant-ph/0402130>.

### Route B — operational reconstructions

Quantum-reconstruction programmes derive complex quantum theory from packages
such as continuous reversible transformations, purification, compression,
causality, and local distinguishability.

The correct use in ISP is premise auditing:

1. translate each principle into the complete stochastic experiment category;
2. distinguish observed regularity from mathematically convenient axiom;
3. test whether the principle constrains native positive laws or imports the
   quantum process structure under another name; and
4. identify which principle supplies the missing composition information.

Primary routes:

- L. Hardy, *Quantum Theory From Five Reasonable Axioms*:
  <https://arxiv.org/abs/quant-ph/0101012>;
- G. Chiribella, G. M. D'Ariano, and P. Perinotti, *Informational derivation
  of Quantum Theory*: <https://arxiv.org/abs/1011.6451>.

### Route C — sum/product amplitude reconstruction

Feynman-style alternatives use a sum rule for exclusive unresolved paths and a
product rule for sequential composition, followed by modulus square. This is
almost exactly the information E-Comp finds absent from positive endpoint
kernels.

The physics question is whether those rules follow from registered composition
and symmetry requirements, and whether their scalar field is forced, rather
than whether complex numbers are useful.

Primary route:

- P. Goyal, K. H. Knuth, and J. Skilling, *Origin of Complex Quantum
  Amplitudes and Feynman's Rules*: <https://arxiv.org/abs/0907.0909>.

### Route D — Barandes-native whole-law generation

Barandes supplies native first-order transition matrices from division events
to arbitrary targets and permits nondivision at intermediate targets. A fixed
model may therefore contain the correct whole transition directly.

The open question is uniform nomology: what one principle generates the
correct family for arbitrary interacting, adaptive, composite experiments?
The answer might be stated directly in positive stochastic language even if a
Hilbert lift is the shortest representation.

Primary routes:

- J. A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*:
  <https://arxiv.org/html/2507.21192v1>;
- J. A. Barandes, *The Born Representation Theorem and the Unistochastic
  Theorem*: <https://arxiv.org/html/2608.04354>.

### Route E — action and holonomy

In established quantum physics, relative phases are generated dynamically by
Hamiltonians or actions, and gauge fields appear through phase transport. This
makes an action/holonomy rule an important later comparator for a composition
connection.

It cannot be inserted now as the answer. An action presupposes variables,
locality, integration structure, and often spacetime. A reality-first route
would have to show which of those are empirical inputs, which are emergent, and
why one common law also governs matter and geometry.

---

## 5. Exact theorem programme

### PC1 — endpoint-quotient obstruction

Prove and review the E-Comp theorem, including the quotient no-congruence
coordinate, coherent $U_\theta$ fiber, carrier-relative rank obstruction,
actual measurement control, full-calibration counterfactual, and gauge wall.

### PC2 — lift classification on a finite separating grammar

For a frozen finite gate/instrument grammar, classify all uniform
phase-sensitive lifts or direct whole-law extensions of the positive primitive
packet, modulo natural complete-experiment gauge.

Required outputs:

1. existence;
2. uniqueness or moduli;
3. minimal additional data;
4. sequential/tensor/adaptive coherence;
5. empirical separators; and
6. exact representation-versus-ontology status.

### PC3 — principle tournament

Test candidate principle packages from Routes A--D against one identical
complete process interface. No package receives credit merely for restating
the Hilbert control.

Possible outcomes:

```text
UNIQUE-LIFT-FROM-INDEPENDENT-PRINCIPLES
MULTIPLE-EMPIRICALLY-EQUIVALENT-LIFTS
QUANTUM-LIFT-EXISTS-BUT-IS-DECLARED-INPUT
POSITIVE-NATIVE-GENERATOR-WITH-EXPLICIT-COST
NO-GENERATOR-IN-THE-FROZEN-CLASS
```

### PC4 — scalable information and resource accounting

Combine the lift result with Q-Cut and later uniform-law bounds. Determine
whether positive intermediate sufficiency, global whole-history dependence,
context access, law description, or physical apparatus resources carry the
phase-sensitive burden.

### PC5 — relativistic and field-theoretic extension

Only after PC1--PC4, test locality, covariance, indefinite causal structures,
QFT composition, and continuum scaling. Supplied AQFT spacetime is a comparator,
not an emergent result.

---

## 6. Hostile controls

Any future composition-lift gate must include:

1. global phase changed with no prediction change;
2. entrywise lift phases changed at one endpoint only;
3. a complete gauge transformation of states, processes, and readers;
4. the $H/V/U_\theta$ repeated-balanced family;
5. an actual middle measurement/division;
6. a cached middle mixture without a physical record;
7. target-process injection;
8. one answer table per program;
9. an infinite real encoding the table;
10. a larger hidden carrier or dilation;
11. real and quaternionic representations;
12. exact realification of complex quantum theory;
13. a PR-box/GPT control that satisfies positivity but not quantum composition;
14. a fixed-system Barandes law that supplies all target transitions;
15. a Markov law with the same primitive endpoints;
16. a process tensor imported as state;
17. a supplied laboratory clock or causal order;
18. a fitted action or Hamiltonian;
19. a per-system rule with no common generator; and
20. an alleged gravity connection inferred from notation alone.

---

## 7. Reality and gravity wall

The additional composition structure, if identified, would answer only how a
quantum law maintains phase-sensitive predictive structure under composition.
It would not
yet answer:

1. why one actual outcome occurs;
2. whether configurations are unique ontology;
3. what physical processes occur cosmologically;
4. how operational clocks arise;
5. how causal structure becomes dynamical;
6. why spacetime is Lorentzian and four-dimensional;
7. how stress-energy and geometry reciprocally respond; or
8. whether the connection is related to gravity.

The possible formal resemblance between phase transport, gauge connections,
and gravitational connections is motivation for a later comparison, not
evidence of identity. No gravity inference is licensed by the word
“connection.”

---

## 8. Present recommendation

The programme should proceed in this order:

1. Q-Cut review, because it is already a scalable quantitative theorem
   candidate;
2. E-Comp review, because it exactly locates the missing phase-composition
   datum;
3. PC2 lift classification, if E-Comp survives;
4. U-Gen source-completion classification, informed by PC2 and Q-Cut; and
5. only then reconsider the repaired clock gate.

This order attacks whether the proposed ontology explains quantum law before
using that ontology to remove time or approach geometry.

```text
ACTIVE AUTHOR-SIDE INVESTIGATION UPDATED
NO COMPOSITION CONNECTION CONSTRUCTED
NO PHYSICAL LAW SELECTED
NO EMPIRICAL DEVIATION DERIVED
NO OFFICIAL UNIT OPENED
```
