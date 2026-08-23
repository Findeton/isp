# ISP v17 — U-Gen U0 native indivisible-law search contract

**Status:** ACTIVE AUTHOR-SIDE SEARCH CONTRACT / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Reality-first question

U0 asks one question and refuses to replace it with a representation theorem:

> Does there exist one uniform ordinary-positive, genuinely indivisible law
> on abstract physical configurations that predicts held-out complete quantum
> processes without receiving the target quantum predictive object, or an
> equivalent phase-complete encoding, as input?

Barandes's ontology makes this question physically serious. Existing v17
results make it difficult. U0 is a search contract, not a claim that the
answer is yes.

The candidate slot is intentionally empty. A future candidate must be written
from independently motivated physical primitives before its held-out quantum
targets are evaluated.

---

## 1. Why a new contract is needed

The active controls establish several non-equivalent facts.

1. Paper 01 gives positive representations of complete finite quantum record
   processes when the phase-complete quantum process is supplied.
2. E-Comp and PC2 show that endpoint stochastic equivalence does not descend
   through coherent composition.
3. PC3--PC5 show that finite endpoint and transformation controls can be
   reproduced by enlarged positive carriers, while exact unbounded
   non-Clifford process structure defeats one finite functorial reversible
   class.
4. Pair-history kernels and G1 compile complete processes when phase-complete
   data are supplied, but earn zero native-law credit.
5. N1/N1A show what one prior-art positive trajectory model can and cannot do;
   their continuum, time, diffusion, and phase structures are not inherited.
6. G2 derives one free coherent kernel only inside already quantum Galilei
   premises and separates real-time coherence from Euclidean probability.

None of these constructs the missing native law. U0 therefore freezes the
*type of the search* without freezing a physical candidate.

---

## 2. Form-neutral candidate type

A candidate is a tuple

$$
\mathfrak U=
(\mathsf{Sys},\mathsf{Conf},\mathsf{Prep},\mathsf{Ctrl},
 \mathsf{Read},\mathsf{Div},\mathcal N,\mathsf{Comp},
 \mathsf{Act},\mathsf{Cost}).
$$

Every coordinate is load-bearing.

### 2.1 System and configuration objects

$\mathsf{Sys}$ is a family of physical system types. For each $S$,
$\mathsf{Conf}(S)$ supplies an abstract measurable configuration object

$$
(\mathcal C_S,\Sigma_S).
$$

This is the minimum needed for ordinary probability. It does not imply that
$\mathcal C_S$ is space, phase space, a lattice, a manifold, a graph, a field
space, or a particle-path space.

The candidate must state:

1. what distinguishes two physical configurations;
2. which transformations are presentation/gauge only;
3. which measurable events are physical;
4. whether the domain is fixed across runs or contingent;
5. how domains for composites are formed; and
6. which regularity assumptions are mathematical conveniences rather than
   physical postulates.

A finite or standard-Borel benchmark is permitted as a bounded operational
control. It cannot be promoted to fundamental discreteness or continuity.

### 2.2 Contingent preparation or state

$\mathsf{Prep}(S)$ contains contingent boundary data $\sigma$. When $\sigma$
is a probability measure,

$$
\sigma\in\mathcal P(\mathcal C_S).
$$

It is not the law and is not silently a wavefunction. If more structure than a
measure is required, the candidate must type it, explain its physical
preparation, and charge its information content.

Two runs may differ in $\sigma$ while sharing the same $\mathcal N$. Retuning
$\mathcal N$ for each prepared state is a family of laws, not one law.

### 2.3 Physical interventions

$\mathsf{Ctrl}$ contains typed, independently specifiable interventions. A
control may contain calibrated apparatus settings, fields, couplings, source
records, or boundary operations. It may not contain:

1. a target unitary or process matrix;
2. a wavefunction chosen because it gives the desired answer;
3. the held-out outcome probabilities;
4. an action or phase table equivalent to the target process;
5. per-program latent advice; or
6. future settings that are not physically available at the intervention.

Abstract labels such as `H`, `T`, `CNOT`, or `measure-Z` are not physical
inputs until their source, calibration, implementation equivalence, and reader
interface are typed without importing the target process.

### 2.4 Readers and records

$\mathsf{Read}$ specifies physical reader interactions and complete retained
records. A reader cannot be merely a target POVM table handed to the law.

For each registered experiment $e$, the candidate must output a normalized
joint record law

$$
p_{\mathcal N,e}(dr\mid\sigma,c)
$$

for the full transcript, including adaptive settings, earlier retained
records, erasures, and null outcomes.

If the reader is modeled as a measurable function, partition, or stochastic
kernel on configurations, its physical calibration and its coupling to the
system must be stated. If the apparatus is part of a larger configuration,
the same $\mathcal N$ must govern the composite.

### 2.5 Divisions and nondivisions

$\mathsf{Div}$ identifies genuine physical restart boundaries. A formal
intermediate label is not automatically a division.

A division requires, relative to the licensed future grammar:

1. a retained physical record;
2. exact or declared-scope future sufficiency;
3. a typed conditional restart law; and
4. stability under every licensed record-preserving future.

At a genuine division $d$, ordinary conditioning/composition must be valid.
Schematically,

$$
\Gamma_{q\circ_d p}
=
\int \Gamma_q(\,cdot\mid z,r)\,
      \Gamma_p(dz,dr\mid\cdot).
$$

At an unrecorded seam $u$, the law is not required to factor. A candidate is
genuinely indivisible only if at least one operationally relevant member has

$$
\Gamma_{q\circ_u p}
\ne
\int \Gamma_q(\,cdot\mid z)\Gamma_p(dz\mid\cdot)
$$

for every *licensed* positive restart through the claimed intermediate
configuration. The witness must not be manufactured by omitting state that
the candidate elsewhere declares physically available.

This is a carrier- and interface-relative claim. It is not a claim of
non-Markovizability under arbitrary mathematical dilation: every finite
complete transcript law can be made Markov by taking its whole past as a
state. Such a target-built history state, or the minimal predictive quotient
computed from the complete target law, is a charged representation and not an
independently physical counterexample. Conversely, an independently
evidenced reference or memory that carries future-relevant information must
be included before a nondivision witness can receive native credit. Source
closure, predictive sufficiency, and ultimate ontic completeness remain
distinct.

### 2.6 One native law

$\mathcal N$ is a single mathematical rule assigning ordinary-positive laws
to admissible complete experiments:

$$
\mathcal N:
(S,\sigma,b,c,\mathsf{Read})
\longmapsto
\Gamma^{\mathcal N}_{S,b,c}
\quad\text{and}\quad
p^{\mathcal N}_{S,b,c}(r\mid\sigma).
$$

The notation allows whole-program dependence; it does not assume Markov
factorization. But $\mathcal N$ must be specified independently of the target
answer and uniformly over the declared family.

The candidate must print:

1. its invariant law parameters;
2. which inputs are contingent state;
3. which inputs are physical controls;
4. the exact rule for every allowed program length;
5. normalization and measurability;
6. response to interventions;
7. genuine-division composition;
8. composite-system formation; and
9. the source of any contextual or whole-program dependence.

### 2.7 Composite systems and interaction

$\mathsf{Comp}$ is not allowed to be an imported Hilbert tensor product. The
candidate must say how two independently preparable systems form a combined
configuration object and how an interaction changes the joint law.

For independently prepared, noninteracting controls it must recover the
registered product law at the declared accuracy. For interacting controls it
must predict correlations from the same rule and fixed couplings. Entanglement
and Bell-process predictions must not be inserted as composite answer tables.

### 2.8 Actuality

$\mathsf{Act}$ states what the theory says happens.

At least one of the following must be chosen explicitly.

1. **Division-boundary actuality:** configurations and records are actual only
   at typed physical divisions; no unrecorded fine path is asserted.
2. **Complete-history actuality:** one complete history is actual and
   $\mathcal N$ supplies its probability law on a stated event algebra.
3. **Realizer-class actuality:** a class of fine realizers is empirically
   equivalent; the theory states whether choosing one is physical, gauge, or
   deliberately underdetermined.
4. **Record-only actuality:** only registered records are claimed as beables;
   the broader configuration language is predictive bookkeeping.

Calling configurations ontic while leaving every possible chronology or
realizer compatible is not automatically inconsistent, but the exact level of
actuality must be stated. Record probabilities alone do not create a hidden
fine-history measure.

### 2.9 Resource ledger

$\mathsf{Cost}$ reports, separately:

1. configuration capacity/dimension;
2. predictive state information;
3. online memory;
4. implementation context;
5. inter-system communication or shared advice;
6. whole-program description length;
7. parameter precision;
8. calibration data;
9. composition data; and
10. uniformity across system size and program depth.

The ledger must be representation-resistant. Moving a wavefunction into a
real vector, probability simplex, hidden context, or infinite-precision real
number does not erase its cost.

---

## 3. Native-law criterion

A candidate is **native at scope $\mathcal E$** only if all of the following
hold.

1. **Independent primitives:** its configurations, controls, and invariant
   parameters are specified without target quantum process data.
2. **Uniformity:** one rule covers the preregistered system-size and
   program-depth family; there is no per-program response table.
3. **Complete processes:** it predicts complete retained/erased,
   sequential/adaptive, transformation, and composite record laws.
4. **Held-out prediction:** target processes are hidden until the law,
   calibration split, parameters, and evaluation map freeze.
5. **No equivalent import:** no input is information-equivalent to the target
   wavefunction, process matrix, action, phase, holonomy, or answer table.
6. **Typed intervention:** settings change predictions through a physical
   intervention interface rather than an evaluator branch.
7. **Typed actuality:** the object said to occur has a law, or the theory
   explicitly limits actuality to records/divisions.
8. **Honest indivisibility:** nonfactorization occurs at an unrecorded seam and
   disappears only when a genuine physical division is inserted.
9. **Composite closure:** product controls and at least one entangling process
   use the same construction rule.
10. **Cost accounting:** hidden memory, context, advice, precision, and
    calibration scale are reported against matched quantum and positive
    controls.
11. **Secondary Hilbert representation:** any Hilbert object is reconstructed
    from the frozen positive law after construction; it is not consulted by
    the generator.
12. **Failure visibility:** every unsupported target produces a registered
    failure rather than a post-hoc domain or parameter change.

Passing a finite benchmark establishes only the printed finite scope. It does
not establish the ontology of nature.

---

## 4. What “Hilbert space is secondary” must mean operationally

The phrase earns content only through a one-way construction order:

```text
physical primitives + contingent preparation + controls
                         |
                         v
             native positive law Gamma
                         |
               freeze and evaluate
                         |
                         v
       optional Hilbert dilation / representation
```

The following reverse order fails:

```text
target Hilbert process U or process matrix W
                         |
                         v
                 Gamma = |U|^2
                         |
                         v
             call Gamma fundamental
```

A later Hilbert dilation may be useful and gauge-nonunique. Its existence
proves representability, not physical primacy. Conversely, failure to find a
native positive law does not prove Hilbert ontology.

---

## 5. Complete-process target surface

The first bounded candidate must predict more than endpoint transition
probabilities. Before construction, freeze at least:

1. continuously variable one-system interference;
2. two noncommuting calibrated transformations;
3. an unbounded or depth-scaling non-Clifford word family;
4. retained versus coherently erased intermediate records;
5. a sequential adaptive instrument whose later setting depends on an earlier
   record;
6. two-system product preparations;
7. one entangling interaction and Bell-sensitive readout;
8. preparation and measurement context controls;
9. a null/no-interaction product control;
10. at least one composite process not used in calibration; and
11. complete transcript probabilities, not selected marginals.

The bounded C1 Clifford-plus-$T$ packet may supply one operational stress test,
but its gate labels are not the native physical source contract. A future
candidate must bind those labels to independently calibrated interventions or
use a different physically grounded family.

---

## 6. Calibration and hold-out discipline

Split all information into four ledgers before evaluating a candidate.

### 6.1 Universal law data

These are invariant parameters or structural rules of $\mathcal N$. They are
fixed once for the declared family.

### 6.2 Contingent preparation data

These describe the run's prepared boundary condition. Their complexity is
charged separately and cannot contain future answer tables.

### 6.3 Independently calibrated control data

These come from physical source/apparatus calibration and must be obtainable
without reconstructing the held-out complete process.

### 6.4 Held-out operational targets

These are inaccessible during construction and parameter selection. The
candidate predicts them once. Choosing among candidate variants after opening
them is model selection and requires a new preregistered split.

The evaluation must test whether the calibration packet is already
informationally equivalent to the held-out quantum process. If so, predictive
success is compilation, not derivation.

---

## 7. Mandatory hostile controls

Any U0 candidate must be compared with at least the following failures or
zero-gain controls.

### U0-H1 — supplied-unitary modulus square

Construct $\Gamma=|U|^{\odot2}$ from the target unitary. This is a valid
Barandes-style representation control and zero native gain.

### U0-H2 — supplied-process record compiler

Use Paper 01's positive record-history representation with the complete
quantum process supplied. Exact adequacy, zero member selection.

### U0-H3 — action/holonomy compiler

Use G1 with target-equivalent action or holonomy data. Positive and
indivisible at bounded scope, not native.

### U0-H4 — pair-history compiler

Use a strongly positive decoherence kernel reconstructed from target
amplitudes. Complete process adequacy, phase-complete input retained.

### U0-H5 — quantum-driven trajectory law

Use Bohm/Bell/collapse rates or currents computed from the target quantum
state. This may add actuality but does not generate quantum prediction
structure natively.

### U0-H6 — Nelson graft

Import Euclidean space, external time, Brownian noise, $\hbar/(2m)$, and
mean-Newton dynamics. This is the bounded N1 control and is not an admissible
default repair.

### U0-H7 — endpoint-only stochastic family

Match every calibrated one-step endpoint matrix while failing held-out
composition, adaptive, or eraser processes.

### U0-H8 — finite hidden-state dilation

Add latent states until the finite calibration set fits. Test held-out depth,
context, and tensor scaling; charge carrier growth and precision.

### U0-H9 — continuous projective-state model

Use a Bloch/projective state space with deterministic unitary motion. This is
a positive control but imports the quantum state geometry under another
ontic label.

### U0-H10 — whole-program lookup

Store one stochastic response table for each program. This is indivisible by
construction and predictively vacuous; its advice cost scales with the target.

### U0-H11 — infinite-precision encoding

Encode all held-out answers in a real parameter or initial condition. Count
recoverable precision/information, not parameter count.

### U0-H12 — Markovization by hidden memory

Enlarge the state until every seam factors. This may be mathematically valid;
the new future-sufficient memory is physical structure and its scaling is
charged.

### U0-H13 — post-hoc configuration domain

Choose finite, continuum, graph, trajectory, or field configurations after
seeing which target must be reproduced. This is model selection, not
emergence.

### U0-H14 — reader import

Supply the target POVM/instrument as a reader table while claiming the law
predicted the experiment. Require physical apparatus calibration or a common
composite-system law.

### U0-H15 — fake division

Factor through an unrecorded formal seam, or refuse to factor at a retained
future-sufficient record. Both violate the physical division grammar.

### U0-H16 — disappearing resource

Relabel wavefunction information as context, memory, gauge, an oracle, source
metadata, or a compact program without accounting for its scaling and
precision.

### U0-H17 — discrete-ontology promotion

Pass a finite operational fixture and infer a microscopic lattice or finite
world. The conclusion does not follow.

### U0-H18 — stochastic failure implies Hilbert ontology

Reject one candidate and declare the Hilbert representation fundamental. The
control is logically invalid.

---

## 8. Candidate-family search without ontology preselection

U0 may investigate multiple families in parallel author-side, but none gains
priority merely because it resembles known quantum notation.

### Family A — whole-experiment positive functionals

One invariant functional maps physical controls and boundary data directly to
complete stochastic laws, with factorization only at physical divisions.
The central risks are lookup-table freedom, future-setting dependence, and
unbounded description cost.

### Family B — compositional stochastic primitives

A small set of physical stochastic primitives and a non-Markov composition
rule generate complete programs. The central risk is importing phase-complete
composition data or an abstract gate presentation with no physical source.

### Family C — contextual predictive-state dynamics

An abstract predictive state carries just enough relational memory to produce
held-out processes. The central risks are renaming the wavefunction and
resource explosion.

### Family D — symmetry- or invariance-selected positive laws

Independently observed physical symmetries constrain $\mathcal N$. The central
risk is that framework symmetry leaves the dynamical member free or silently
assumes spacetime, action, or Hilbert structure.

### Family E — operational quotient with native stochastic lift

Start from physically calibrated procedure equivalence and seek a positive
lift whose extra structure is selected by uniformity and held-out prediction.
The central risks are contextual answer import and nonunique fibers.

### Family F — primitive relational response law

Configurations are defined only by their responses under interventions, with
no spatial or trajectory interpretation. The central risks are operational
circularity and inability to distinguish law from complete future-profile
state.

These are search coordinates, not theories. A new family is admissible if it
passes the same no-answer and complete-process gates.

---

## 9. First author-side research tasks

The next work should be theorem-led rather than a broad model catalogue.

### Task U0-T1 — source-completion theorem

Reconstruct exactly which data Barandes's published correspondence takes as
primitive and which it generates. Identify the minimal missing map

$$
(\text{physical controls, contingent state})
\longmapsto
\Gamma
$$

without interpreting a Hilbert dilation as that map.

**Author-side status:** completed as a source reconstruction in
`v17_ugen_u0_barandes_source_completion_audit.md`. It locates the open map but
awards neither an existence theorem nor a no-go.

### Task U0-T2 — no-equivalent-input criterion

Give a representation-resistant definition of when a calibration packet is
information-equivalent to a target complete process. Q-Cut is a possible
bounded theorem input only if separately authorized and accepted.

**Author-side status:** completed as a source reconstruction and mathematical
gate in v17_ugen_u0_t2_information_equivalence_source_audit.md and
v17_ugen_u0_t2_no_equivalent_input_criterion.md. The criterion freezes the
complete-process operational quotient, neutral/quantum/tomography/advice
decoder classes, calibration fibers, provenance, resource accounting, and the
opaque-program undecidability boundary. It constructs no law and awards no
scientific result.

### Task U0-T3 — configuration-neutral complete-process fixture

Replace bare gate names by typed physical intervention equivalence classes,
while keeping the target process hidden. The fixture must admit finite,
continuous, contextual, and whole-program positive controls without selecting
one ontology by type.

**Author-side status:** schema outcome T3-R3 is constructed in the physical
interface audit, configuration-neutral fixture, and calibration-fiber theorem
files. The descriptor/transfer and source-descent gates now prove that
configuration neutrality cannot mean structurelessness: predictions must
descend through verified presentation changes, while physically meaningful
context cannot be quotiented away. The finite anonymous-carrier control leaves
one free one-step persistence parameter and only equality-pattern whole-history
invariants; covariance therefore constrains but does not generally select a
law. No microscopic configuration form is selected. A real
implementation-bound R4 packet and independently reviewed R5 admission remain
absent. No candidate, official pin, review cycle, or result is opened.

### Task U0-T4 — native candidate contest

T4 is staged so that formula construction does not require premature apparatus
custody, while target access never precedes a freeze.

1. **T4-P, author-side preconstruction.** Exact formulas may be prototyped
   from target-blind primitives and tested against theorem, synthetic, public,
   and retrospective controls. This creates no official candidate, pin,
   empirical claim, or target access. The first formula must predict, rather
   than receive, its executable division-response hierarchy; raw `qCor`, a
   target decoherence functional, or a completed interference table earns no
   source-completion credit. Vanishing third-order interference, strong
   positivity, PR, and almost-quantum behavior are held-out Q-layer controls.
2. **T4-E, candidate-entry readiness.** Before requesting a freeze, one exact
   formula must print its source map, actuality rule, composition rule,
   falsifier, resource bound, and deliberately different positive control,
   and must survive the cheap controls.
3. **R4, implementation and custody.** Only after a separately authorized
   formula freeze may a prospective or otherwise information-safe fixture be
   bound and independently audited for source lineage and leakage.
4. **T4-O, official evaluation.** Only a separately authorized official cycle
   may open held-out targets and award a scientific result.

Do not select a formula or a winner after opening targets. None of T4-E, R4,
T4-O, a formula freeze, or an official contest is opened by this sequencing
clarification.

### Task U0-T5 — scaling and actuality audit

For any surviving finite candidate, test unbounded depth, composite-system
growth, adaptive records, resource scaling, and the exact object claimed to be
actual.

---

## 10. Outcome ladder

No rung is currently awarded.

### U0-L0 — TYPE OR SOURCE FAILURE

The candidate cannot distinguish law, state, control, reader, record, or
actuality; or it imports a target-equivalent object.

### U0-L1 — NATIVE BOUNDED STOCHASTIC MEMBER

One independently specified positive law predicts a preregistered bounded
complete-process family without target-equivalent input.

### U0-L2 — GENUINE OPERATIONAL INDIVISIBILITY

L1 survives and physical retained/erased seam controls show correct division
and nondivision behavior.

### U0-L3 — COMPOSITE AND ADAPTIVE CLOSURE

L2 survives product, interaction, entangling, Bell-sensitive, and adaptive
complete-process tests under one composition rule.

### U0-L4 — SCALABLE UNIFORM FAMILY

L3 survives preregistered system-size and program-depth scaling with honest
resource accounting and no per-program advice.

### U0-L5 — SECONDARY HILBERT RECONSTRUCTION WITH ONTOLOGY CONTENT

L4 survives and a Hilbert representation is reconstructed after the positive
law freezes, while the candidate's configuration/actuality claims remain
physically distinct and testable or independently motivated.

### U0-L6 — RELATIVISTIC / COMMON-NOMOLOGY READINESS

L5 supplies the fixed-background complete matter law needed before MG0 may
compare gravity-sensitive extensions. U0 itself awards no gravity result.

Failure at any rung is a legitimate scientific output. No lower rung implies
a higher one.

---

## 11. Stop conditions

Stop and classify rather than repair automatically if:

1. the candidate needs a target wavefunction, process matrix, action, phase,
   holonomy, or equivalent predictive state;
2. its configuration domain is chosen after target inspection;
3. it reproduces endpoints but fails complete processes;
4. its whole-program law is an uncharged lookup table;
5. the only successful repair is Nelson, Bohm/Bell, collapse, or Hilbert
   dynamics supplied from the target;
6. composite systems require separate answer tables;
7. hidden resource or precision scales as the target process;
8. actual configurations are claimed but no actuality semantics are stated;
9. a finite control is promoted to fundamental discreteness; or
10. gravity is invoked before two complete matter laws make distinct
    gravity-sensitive predictions.

There is no automatic U0 v2, N1B, G3, official pin, or paper.

---

## 12. Present verdict

```text
BARENDES GUIDING HYPOTHESIS:          SERIOUS / NOT PRESELECTED
ABSTRACT CONFIGURATION DOMAIN:        REQUIRED / FORM UNSELECTED
ORDINARY-POSITIVE LAW:                REQUIRED FOR THIS SEARCH BRANCH
GENUINE INDIVISIBILITY:               REQUIRED OPERATIONALLY
COMPLETE-PROCESS PREDICTION:          REQUIRED
TARGET QUANTUM INPUTS:                FORBIDDEN
HILBERT REPRESENTATION:               SECONDARY ONLY / IF RECONSTRUCTED
CONTINGENT STATE / CONTROL / READER:  MUST BE TYPED SEPARATELY
ACTUALITY CLAIM:                       MUST BE EXPLICIT
RESOURCE LEDGER:                       REQUIRED
N1/N1A:                               HOSTILE PRIOR-ART CONTROLS ONLY
G1/G2:                                COMPILER / SOURCE-ORIGIN CONTROLS
MG0:                                  GRAVITY PREFLIGHT ONLY
NATIVE CANDIDATE:                      ABSENT
SOURCE DESCENT:                        EXACT AUTHOR-SIDE NECESSARY CONDITION
BARE-CARRIER DYNAMICS:                 UNDERDETERMINED / BOUNDED CONTROL
PHYSICAL RELATIONAL STRUCTURE:         REQUIRED / NOT YET CHOSEN
OFFICIAL PIN / REVIEW / RESULT:        NONE
```

---

## 13. Maximum legitimate claim

U0 presently establishes only a search boundary:

> A native Barandes-facing success must begin with an independently specified
> ordinary-positive law on an ontology-neutral configuration domain and must
> generate held-out complete process statistics through typed interventions,
> records, divisions, composition, and actuality semantics. Supplying a
> wavefunction, process matrix, action, phase, holonomy, quantum current,
> Nelson kinematics, or per-program stochastic table converts the construction
> into a compiler or prior-art control. No such native law has yet been found,
> and its absence has not been proved.
