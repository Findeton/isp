# ISP v17 — U-Gen U0 Barandes source-completion audit

**Status:** ACTIVE AUTHOR-SIDE SOURCE AUDIT / NO CANDIDATE
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review opened:** no

This audit answers U0-T1 from the native indivisible-law search contract. It
separates three questions that are easy to conflate:

1. can a supplied ordinary-positive stochastic law be represented in Hilbert
   space;
2. can a supplied quantum model be represented by a suitable stochastic law;
3. what physical principle selects the stochastic law for a previously unseen
   system, control, and complete experiment?

The cited Barandes work gives important positive answers to the first two
questions. The third is the live source-completion problem. Calling it open is
not a refutation of Barandes's ontology, and a representation theorem is not a
solution to it.

This file implements the binding Nelson-control scope correction. It inherits
no particle trajectory, Euclidean configuration space, Brownian noise,
Markov divisibility, external time, Nelson coefficient, phase field, bundle,
or holonomy from N1/N1A.

---

## 1. Version-bound primary sources

The source claims below are limited to these versions, accessed on
2026-08-23:

1. Jacob A. Barandes, [*Quantum Systems as Indivisible Stochastic
   Processes*](https://arxiv.org/html/2507.21192v1),
   arXiv:2507.21192v1.
2. Jacob A. Barandes, [*The Stochastic--Quantum
   Theorem*](https://arxiv.org/html/2309.03085v2),
   arXiv:2309.03085v2.
3. Jacob A. Barandes, Matthew Hasan, and David Kagan,
   [*The CHSH Game, Tsirelson's Bound, and Causal
   Locality*](https://arxiv.org/html/2512.18105v1),
   arXiv:2512.18105v1.
4. Jacob A. Barandes, [*The Born Representation Theorem and the
   Unistochastic Theorem*](https://arxiv.org/html/2608.04354v1),
   arXiv:2608.04354v1.

The papers are moving research sources. Manuscript dates printed inside their
HTML need not coincide with arXiv deposit dates. The identifiers above, not an
internal date, bind this audit.

This is a source-scope reconstruction, not an independent certification of
every theorem in the papers.

---

## 2. The central distinction

For an experimental specification $e$, write

\[
e=(S,b,c,R),
\]

where $S$ is the physical system specification, $b$ is contingent boundary
or preparation information, $c$ is an admitted control program, and $R$
is a typed family of physical readers. A source-complete native theory would
contain one uniform rule

\[
\boxed{
\mathcal S_{\mathcal N}:
(S,b,c,R)\longmapsto
\Gamma^{\mathcal N}_{S,b,c,R}
}
\tag{SC}
\]

derived from fixed nomological data $\mathcal N$. The output must be an
ordinary-positive complete-process law, not merely an endpoint table.

The rule must work on held-out experiments without receiving any object that
is information-equivalent to the target answer. In particular, its allowed
input cannot contain the target wavefunction, density operator, process
matrix, quantum channel, unitary, action, phase, holonomy, or a lookup table of
the requested probabilities.

Four maps must remain separate:

| map | input | output | status in this audit |
|---|---|---|---|
| source completion | physical system, state, controls, readers | stochastic law $\Gamma$ | live missing physics |
| stochastic propagation | $\Gamma$ and contingent state | later distributions | supplied by stochastic dynamics |
| Hilbert representation | supplied $\Gamma$ | Hilbert-space ingredients | established at the cited theorem scope |
| empirical readout | law plus typed physical reader | records | only partially specified across the cited sources |

The stochastic--quantum dictionary acts downstream of $\Gamma$. It cannot be
silently read backwards as the physical map (SC).

---

## 3. Primitive/generated ledger for the cited framework

### 3.1 Printed as primitive or model-supplied

At the scope located in the cited sources, the construction begins with:

1. a configuration space $\mathcal C$ selected for a model;
2. real-valued time labels and at least one conditioning or division time;
3. a contingent standalone probability distribution $p(i,t_0)$;
4. first-order conditional probabilities

   \[
   \Gamma_{ij}(t\leftarrow t_0)
   =p(i,t\mid j,t_0);
   \]

5. admitted division events and the distinction between divisible and
   indivisible intervals;
6. for the CHSH composite treatment, Cartesian-product configuration
   kinematics and a parent conditional law

   \[
   p(q_t,r_t\mid q_0,r_0);
   \]

7. physical premises used by a particular application, including spatial
   localization and light-cone relations in the causal-locality analysis.

"Primitive" here means supplied to the displayed construction. It does not
mean that Barandes asserts every item must remain fundamental in a future
theory.

### 3.2 Generated once those data are supplied

The framework then supports, at its stated scope:

1. propagation of the contingent distribution,

   \[
   p(t)=\Gamma(t\leftarrow t_0)p(t_0);
   \]

2. ordinary-positive descriptions with transition probabilities that need
   not divide through arbitrary intermediate times;
3. a nonunique potential $\Theta$ satisfying

   \[
   \Gamma_{ij}=|\Theta_{ij}|^2;
   \]

4. a Hilbert-space representation, including dilation when required;
5. Born-style representations and, for finite stochastic matrices, bounded
   unistochastic dilation at the scope of the 2026 theorem;
6. quantum-like empirical structures once a suitable stochastic law and the
   rest of the experimental model are supplied;
7. parent-to-subsystem marginals and a factorization test for noninteraction
   once a composite parent law is supplied.

This is substantial. It shows that complex Hilbert machinery can be secondary
to an ordinary-positive law at the level of representation. It does not yet
show where the correct law of a new physical experiment comes from.

### 3.3 Not located as a uniform derivation in these sources

The cited versions do not establish one universal rule that derives:

1. which configuration object is physically correct for every system;
2. which first-order stochastic law belongs to a specified interaction;
3. an interacting parent law from subsystem laws plus independently typed
   control primitives;
4. the full probabilities of arbitrary adaptive intervention/readout
   programs from one fixed non-quantum nomology;
5. the admissible reader map without encoding the desired quantum observable;
6. the division structure of every composite experiment from an independent
   physical criterion;
7. an internal clock, chronology, metric, or gravitational coupling;
8. a unique fine-grained non-Markovian realizer;
9. one scalable configuration-and-composition rule that predicts held-out
   complete processes across changing systems and program depth.

"Not located" means absent from the source scope audited here. It does not
mean impossible, and it does not rule out later or unpublished work.

---

## 4. What indivisibility does and does not provide

The cited framework's important move is to keep fixed first-order conditional
laws while declining to require a Kolmogorov tower or divisibility through
every intermediate time. That blocks the automatic inference

```text
ordinary positive law => Markov chain or classical hidden trajectory model.
```

It also means that "the stochastic process" cannot be treated casually as one
fully specified probability measure over all fine histories. The 2025/2026
paper states that generically many complete Kolmogorov towers can realize the
same minimalist indivisible law. Their equivalence class is empirical at the
specified level, while the specific realizer may be unknowable or physically
meaningless.

U0 must therefore distinguish three actuality claims:

1. **division-boundary actuality:** a configuration is actual only at typed
   division/readout boundaries;
2. **fine-history actuality:** one detailed configuration history is actual
   between boundaries;
3. **law-level actuality:** only the equivalence class encoded by the
   indivisible law carries warranted physical content.

The sources motivate realist language and mention one trajectory as what
ultimately happens. They do not, at the audited scope, select one unique
probability law over those fine trajectories. A U0 candidate must state which
claim it makes and what observations could distinguish it. It may not import a
Kolmogorov tower merely to make the ontology look familiar.

---

## 5. The representation achievement and its exact boundary

The stochastic--quantum theorem states a broad correspondence from an
indivisible stochastic process to a unitarily evolving quantum representation.
The later Born and Unistochastic theorems broaden finite endpoint
representability: any finite stochastic matrix admits a Born-style
representation, and a bounded dilation can embed it into a larger
unistochastic matrix.

For v17 this yields two opposite lessons.

### Positive lesson

If a native positive law is found first, complex Hilbert space, unitary
evolution, and Born-style expressions may be reconstructed as secondary
mathematics. U0 therefore must not assume Hilbert ontology merely because
standard quantum predictions are normally written that way.

### Selection lesson

Broader representability makes it easier to represent a supplied stochastic
matrix. It does not tell nature which matrix to use. Indeed, the more universal
the representation, the less it can by itself select a member of the
represented class.

Therefore neither of these implications is valid:

```text
HAS A HILBERT DILATION => PHYSICAL LAW DERIVED
ALL STOCHASTIC MATRICES ARE REPRESENTABLE => ALL ARE EQUALLY PHYSICAL
```

The native burden remains (SC).

---

## 6. Gauge and phase discipline

The potential $\Theta$ satisfying $\Gamma=|\Theta|^2$ is nonunique. The cited
work explicitly treats entrywise phase changes, accompanied by corresponding
changes in downstream Hilbert ingredients, as Schur--Hadamard gauge
transformations with no empirical effect.

Consequently, this is not by itself a physical counterexample:

```text
same isolated Gamma + different arbitrary lift phases.
```

A valid held-out complete-process test must instead:

1. fix the physical meanings of preparations, interventions, composition, and
   readers;
2. hold all gauge-invariant input data fixed;
3. exhibit distinct continuation statistics that the native positive law
   either predicts or fails to predict;
4. prevent a compensating redefinition of the rest of the experiment from
   being counted as new physics.

This is why G1 remains a compiler/control. Supplying an action or holonomy can
produce a positive record law, but the supplied global object carries the
missing interference information. It does not solve (SC).

---

## 7. Composite systems and complete experiments

The CHSH paper provides genuine structural guidance:

\[
\mathcal C_{QR}=\mathcal C_Q\times\mathcal C_R,
\]

and subsystem laws arise by marginalizing a parent conditional law. A parent
law factorizes when the subsystems do not interact. This supports the idea
that an entire laboratory, including agents and apparatus, may be treated as
one physical stochastic system rather than as an external observer acting on
a wavefunction.

But the displayed interacting parent law is supplied. The audited source does
not give a general generator

\[
(\Gamma_Q,\Gamma_R,\text{typed interaction})
\longmapsto
\Gamma_{QR}^{\rm int}
\]

that predicts every held-out interacting parent. Nor does Cartesian-product
kinematics follow from ontology-neutral premises; it is one explicit composite
choice.

The same paper describes a possible quantum-comb/process-tensor relation as a
conjecture. U0 may use that as a comparison target, not as an already derived
positive complete-process functor.

Thus two propositions must not be conflated:

1. a fixed complete experiment can be represented as one parent indivisible
   stochastic system;
2. one uniform physical law generates the parent for every new experiment
   from independently specified local systems and controls.

The cited work strongly motivates the first. U0 is asking for the second.

---

## 8. Time, locality, and gravity boundary

The primary indivisible laws are indexed by supplied times. The CHSH
causal-locality analysis additionally uses spatial localization, elapsed time,
light cones, and the speed of light. These are legitimate fixed-background
premises for that analysis.

They do not derive:

1. operational chronology from the positive law;
2. spacetime dimension or metric;
3. Lorentzian causal structure from configuration relations;
4. reciprocal matter--geometry dynamics.

U0 therefore cannot inherit external time or a spatial configuration space
from the current correspondence. MG0 remains a discriminator preflight only.
Gravity may compare two genuinely different, complete matter laws after they
make distinct gravity-sensitive predictions; it may not select U0's ontology
in advance.

---

## 9. Source-faithful base embedding

For a future finite fixture, define a base embedding

\[
\iota_0(e)
\]

that may contain only independently calibrated physical information. Depending
on the experiment, admissible fields may include:

1. system identity and composition interfaces;
2. possible configuration/readout labels, without choosing discrete or
   continuous form globally;
3. preparation equivalence classes;
4. control equivalence classes and their physically charged parameters;
5. reader equivalence classes and stable records;
6. isolated component laws already belonging to calibration rather than the
   hidden target;
7. explicit division and nondivision controls;
8. honest resource bounds and precision.

The following are forbidden in $\iota_0(e)$:

1. the target complete-process table or any invertible encoding of it;
2. a target wavefunction, unitary, channel, process matrix, or Hamiltonian;
3. target action, phase, connection, holonomy, or path-integral weight;
4. interaction-specific parent probabilities learned from the target;
5. per-program advice or exponentially large lookup memory;
6. a reader definition whose labels encode the desired answer;
7. a post-hoc choice of configuration domain after opening the target.

Source completion then requires one frozen nomology $\mathcal N$ such that

\[
\Gamma_e^{\mathcal N}
=
\mathcal S_{\mathcal N}(\iota_0(e))
\tag{SC2}
\]

for calibration and held-out experiments under the same rule.

---

## 10. Minimal completeness criteria for (SC)

A purported source-completion rule is not complete unless it prints:

1. **domain:** the typed category of systems and experimental programs on
   which it acts;
2. **state:** the contingent information that varies between otherwise equal
   runs;
3. **nomology:** the fixed data that do not vary per target;
4. **controls:** how physical interventions alter the admitted program;
5. **readers:** how actual records are formed without answer import;
6. **composition:** how systems and controls generate interacting parents;
7. **division:** when conditional recomposition is physically valid;
8. **actuality:** what occurs in one run;
9. **resources:** memory, precision, time, and description length;
10. **generalization:** preregistered held-out complete-process predictions.

Endpoint agreement alone is insufficient. A table that reproduces isolated
transition probabilities but cannot predict sequential, adaptive, composite,
or retained/erased-seam experiments has not supplied the complete physics.

---

## 11. The first exact theorem target

U0-T1 earns a precise problem statement, not a no-go:

### Definition U0-SC1 — source-complete positive nomology

A positive nomology $\mathcal N$ is source-complete on an experiment class
$\mathfrak E$ if one fixed measurable rule $\mathcal S_{\mathcal N}$:

1. is defined before target opening;
2. maps every admissible $\iota_0(e)$, $e\in\mathfrak E$, to a normalized
   complete-process law;
3. is functorial under declared relabelings and physical composition;
4. distinguishes contingent state from law;
5. exposes typed interventions, readers, and division seams;
6. uses no target-equivalent quantum or answer data;
7. has bounded, declared resource scaling;
8. predicts the frozen held-out records of $e$.

### Theorem question U0-SC-Q

Does there exist a nontrivial source-complete ordinary-positive nomology on a
configuration-form-neutral experiment class containing:

1. incompatible sequential controls;
2. interference-sensitive continuations;
3. composite entangling controls;
4. adaptive readers; and
5. retained versus erased operational seams?

No existence or impossibility answer is presently awarded.

---

## 12. What this audit says about the Barandes programme

The source-completion gap is a constructive burden, not a semantic dismissal.
The audited papers support the serious hypothesis that:

1. ordinary probability can be fundamental;
2. indivisibility can replace automatic Markov composition;
3. configurations can carry realist content;
4. Hilbert-space machinery can be representationally secondary;
5. measurement can be treated as physical interaction.

They do not yet establish, at the audited scope, that one fixed non-quantum
nomology generates the correct complete stochastic law for arbitrary new
physical systems and controls without being given equivalent quantum data.

This leaves three logically open possibilities:

1. a source-complete native positive law exists and remains to be found;
2. extra global or whole-process positive structure is required but can be
   generated from deeper non-quantum physics;
3. the desired positive ontology fails at some exact gate, without thereby
   proving that Hilbert space is ontic.

U0 must discriminate among these possibilities rather than assume one.

---

## 13. Routing consequence

U0-T1 is complete only as an author-side source reconstruction. Its output is:

```text
BARENDES REPRESENTATION ACHIEVEMENT:  SUBSTANTIAL
HILBERT-SECONDARY POSSIBILITY:        SOURCE-SUPPORTED
INDIVISIBILITY AS NON-MARKOV LAW:      SOURCE-SUPPORTED
UNIFORM SOURCE-COMPLETION MAP:         NOT LOCATED / OPEN
COMPOSITE PARENT GENERATOR:            NOT LOCATED / OPEN
COMPLETE INTERVENTION FUNCTOR:         NOT ESTABLISHED IN AUDITED SOURCES
CONFIGURATION FORM FOR U0:             UNSELECTED
EXTERNAL TIME INHERITANCE:             FORBIDDEN
N1/N1A ONTOLOGY INHERITANCE:           NONE
G1 ACTION/HOLONOMY STATUS:             COMPILER/CONTROL
MG0 STATUS:                            GRAVITY PREFLIGHT ONLY
NATIVE U0 CANDIDATE:                   ABSENT
OFFICIAL PIN / REVIEW / RESULT:        NONE
```

The next author-side task is U0-T2: define a representation-resistant
no-equivalent-input criterion, then construct a configuration-neutral
complete-process fixture. That task does not authorize a candidate, pin,
review cycle, paper, or automatic successor.

---

## 14. Maximum legitimate claim

> The cited Barandes results make it mathematically credible that a supplied
> ordinary-positive indivisible stochastic law can carry quantum empirical
> structure while Hilbert space remains secondary. At the audited source
> scope, they do not yet provide the uniform physical source-completion rule
> that maps independently specified systems, contingent states, controls, and
> readers to held-out complete-process laws without target-equivalent quantum
> input. This is an open constructive gate, not an impossibility theorem and
> not a refutation of the indivisible-stochastic ontology.
