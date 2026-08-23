# PRIVATE PHYSICS PACKAGE — discriminating record architectures

Date: 2026-08-23

Status: **PRIVATE / RESULT-NEUTRAL / NO OFFICIAL UNIT**

This package asks how reality could distinguish the physical features used in the
honest resolutions of the controlled-record obstruction. It does not select an
ontology by mathematical elegance.

## 1. Resolution features under comparison

### I — invariant commutative output

A joint invariant $f$ is measured by a complete instrument. Its classical output
labels the $f$-fibers; coherence survives inside each fiber and is removed between
distinct recorded values.

### C — classicalized controller/skew product

The controlling sector is superselected or decohered. The joint controller/raw
record spectrum then supports an ordinary classical skew-product permutation.
Controller coherence is no longer part of the state space or is lost into an
explicit environment.

### N — noncommutative memory/groupoid completion

The coherent controller and raw pointer are retained. Relative-permutation orbits
become matrix blocks. Raw labels inside one block are quantum memory coordinates,
not central records. A classical fact appears only after a later commutative
instrument or restriction.

### R — reference-assisted raw record

An additional physical reference system compensates the raw transformation. The
record is relational to that reference, whose state, asymmetry, resolution,
degradation, and backreaction are resources.

### 1.1 These are overlapping coordinates

I/C/N/R are not four mutually exclusive theories. They answer different
questions:

- I describes the algebra and coarse graining of the final output;
- C describes the coherence status of a controller;
- N describes an intermediate or retained noncommutative memory;
- R describes the physical resource used to define a relation.

A single apparatus can therefore be I+R, N+I, C+I, or another conjunction. The
minimal three-qubit design is I+R: the b qubit is the physical reference entering
$y=a\oplus qb$, and the final y pointer is invariant and commutative. Results must
print these feature coordinates separately.

## 2. One instrument does not select a mechanism

For an operational instrument $\{\mathcal I_y\}$, define its classical-output
channel

$$
\Phi(\rho)=\sum_y\mathcal I_y(\rho)\otimes|y\rangle\langle y|.
$$

Every such completely positive channel has Stinespring dilations. A minimal
dilation is unique only up to an environment unitary, and nonminimal dilations can
append arbitrary idle ancillas or refine the environment. Therefore the observed
instrument alone does not select:

- a microscopic pointer carrier;
- an environment decomposition;
- a preferred basis outside the exposed output algebra;
- an invariant-output, hidden-reference, or memory implementation when they
  induce the same complete channel;
- a Barandes configuration space or actual trajectory.

This is not merely philosophical underdetermination. It is a theorem about the
many-to-one map from dilations to operational channels.

To distinguish mechanisms, the experiment category must be enlarged by physically
licensed interventions or readers on the proposed reference, memory, controller,
or environment. If no such access exists and every complete endpoint-experiment
law agrees, the fully specified mechanisms are operationally equivalent in that
domain. This does not imply equality of an optional, separately selected path
realizer.

## 3. Required discriminator suite

### D1 — within-fiber coherence

Prepare coherent alternatives with the same proposed invariant. Measure the
registered record and then a complete interference reader.

- I predicts preservation within the ideal fiber.
- C predicts loss if the coherent controller was classicalized.
- N can preserve the coherence before a final classical read.
- R depends on reference entanglement and residual which-sector information.

### D2 — cross-fiber coherence

Prepare alternatives with different invariant values. A complete sharp I record
must remove their operational coherence in the nonselective output. Failure means
the output was an incomplete premeasurement, not a classical record.

### D3 — incompatible memory readers

Before classical amplification, test two noncommuting memory observables.

- A positive incompatible-reader witness supports N-type quantum memory.
- It is incompatible with treating the same complete output algebra as purely
  classical.
- It does not by itself prove a fundamental groupoid ontology.

### D4 — reversible uncomputation

Reverse the premeasurement before amplification.

- Recovery supports a coherent memory/dilation description.
- Failure after verified inverse control indicates leakage, amplification, or an
  incomplete model.
- Recovery does not show that an already actual macroscopic fact was destroyed.

### D5 — reference intervention

Transform, rotate, replace, or deliberately degrade the proposed reference while
holding the target system preparation fixed.

- R predicts controlled changes of raw-coordinate performance or calibration.
- A truly invariant I output should retain its registered covariance, subject to
  the changed apparatus resources.
- No conclusion is possible if the reference cannot be independently addressed.

### D6 — repeated-use degradation

Reuse the same finite reference or memory across a frozen sequence. Measure
resolution, asymmetry, disturbance, and backreaction after each use.

- Reference degradation is direct evidence of a consumed R resource.
- Absence of degradation over a finite window does not prove catalytic or
  infinite-resource behavior.
- The same source must be used; resetting the reference between trials tests a
  different process.

### D7 — sector classicalization witness

Tomographically test off-diagonal controller operators before and after record
formation.

- Exact loss with an exposed environment supports C at the registered boundary.
- Retention rules out a complete classicalized-controller description.
- Apparent loss due to averaging over an uncontrolled phase requires a phase
  reference/control before being called decoherence.

### D8 — centrality and repeatability

Test whether record projectors commute with the complete output reader algebra and
whether repeated reads agree without changing later registered statistics.

- Passing supports a classical output factor.
- A preferred pointer basis alone is insufficient.
- Centrality is boundary-relative; later enlarged algebras may reclassify the
  memory.

### D9 — redundant fragment access

Read two or more physically disjoint, independently addressable fragments.
Demonstrate agreement, nondisturbance, and absence of a single aliased hidden
store. This tests operational objectivity, not actuality.

### D10 — full endpoint-experiment discrimination

Compare every registered preparation, reference intervention, memory reversal,
fragment read, adaptive controller, and final transcript reader. Operational
process tensors may organize these laboratory interventions, but each tested
protocol must be realized as a complete endpoint experiment; this does not assign
probabilities to unrecorded native intermediate configurations. A difference on
one preregistered experiment makes the specified mechanisms operationally
distinct. Equality only on a smaller measurement list proves nothing about the
unmeasured extensions.

## 4. Outcome classification

Every pair of fully specified mechanism models receives one of:

```text
DISTINCT-ON-REGISTERED-EXPERIMENT
EQUIVALENT-ON-COMPLETE-REGISTERED-PROCESS
INCOMPLETE-READER-OR-INTERVENTION-ACCESS
MODEL-ILL-TYPED
```

`EQUIVALENT-ON-COMPLETE-REGISTERED-PROCESS` forbids ontological selection within
that domain. It does not prove global equivalence under future experiments. The
generic I/C/N/R feature coordinates themselves are not assigned pairwise verdicts
as though they were exclusive models.

## 5. Exact finite-reference resource theorem

Let a group $G$ act on a target sharp measurement $M$, producing a set of distinct
measurements

$$
\mathcal O_M=\{g\cdot M:g\in G\}.
$$

Suppose one fixed symmetric programmable device is intended to realize each member
of $\mathcal O_M$ using a corresponding reference state $\rho_g$.

The task is deterministic and exact on every admitted target input, uses no
postselection, begins with a program/reference uncorrelated with the unknown target
state, and quotients measurements differing only by a frozen operationally free
outcome relabeling. Without these hypotheses the following bound is not licensed.

### Theorem 5.1 — perfect-reference necessity

If the programmed sharp measurements are exactly distinct and exactly simulated,
then the resource states for distinct programs must be perfectly distinguishable.
For pure reference states,

$$
\langle r_g|r_h\rangle=0
$$

whenever $g\cdot M\ne h\cdot M$. Consequently

$$
\dim\mathcal H_R\ge|\mathcal O_M|
$$

for a finite orbit.

### Proof route

Exact symmetric simulation makes the group orbit of the reference state a program
for the corresponding orbit of sharp measurements. The no-programming theorem for
distinct projective measurements requires perfectly distinguishable program
states. The dimension bound follows. This is the information-theoretic WAY
mechanism.

### Continuous consequence

If a compact continuous group generates uncountably many distinct sharp target
measurements, no finite-dimensional reference can provide an orthogonal program
orbit. Exact simulation therefore requires an idealized infinite resource or a
different, explicitly scoped construction. Finite references can only approximate
the task, with performance controlled by the distinguishability/asymmetry of their
orbit states.

This is a necessity theorem. A dimension bound alone does not construct the
measurement device, establish sufficiency under every conservation law, or make
the reference fundamental.

## 6. Approximate and repeated reference use

For nonorthogonal orbit states, the reference cannot encode the transformation
perfectly. The exact error depends on the registered measurement task and device.
An honest finite-resource result must print:

1. the group and target-measurement stabilizer;
2. the reference representation and state;
3. orbit-state distinguishability or asymmetry monotone;
4. simulation error in a frozen operational norm;
5. target disturbance and reference backreaction;
6. degradation under repeated use;
7. whether a reset or fresh reference is consumed;
8. energy, dimension, entropy, and localization costs.

No universal equality may be inferred from the pure two-state record formula.

## 7. Mechanism-specific falsifiers

| Feature claim | Required positive evidence | Direct falsifier in registered domain |
|---|---|---|
| I invariant output | complete invariant instrument; within-fiber coherence; central repeatable output | leakage of distinguished sector into pointer or failure of invariant covariance |
| C classicalized controller | controller off-diagonals absent with exposed mechanism; classical skew-product closure | verified retained controller coherence after complete record formation |
| N noncommutative memory | incompatible memory readers or reversible coherent processing; orbit-block algebra | complete central broadcast already present at the claimed earlier boundary |
| R physical reference | independently controllable reference; reference-dependent performance; resource/backreaction ledger | identical complete endpoint-experiment laws under separating reference changes when model predicts dependence |

These falsifiers concern an implementation. They do not decide which feature
combination, if any, is fundamental throughout nature.

## 8. Barandes boundary

A Barandes-style ontology requires one fixed configuration space, one indivisible
endpoint law, a contingent distribution/state, and an actual trajectory. It does
not thereby select one non-Markovian realizer or whole-trajectory probability law.
Operational discrimination among fully specified I/C/N/R feature combinations can
constrain candidate lifts only if those mechanisms make different predictions for
complete licensed endpoint experiments.

When all complete operational processes agree, Stinespring or hidden-state
differences do not select a Barandes ontology. Native discrimination would require
additional configuration-level interventions/readers or a new empirical
prediction frozen before data.

## 9. AQFT boundary

The finite center and orbit-block theorems do not automatically extend to local
type-III field algebras. In AQFT, invariant/crossed-product constructions can
organize relational observables on a supplied spacetime, but a crossed product is
not thereby a classical outcome algebra. A physical record still requires a
localized instrument, an apparatus/output algebra, causal factorization, and
complete readers.

Any QFT extension must separately establish:

- normal localized instruments;
- state and domain closure;
- spacelike factorization/no-signalling;
- reference localization and energy cost;
- a classical output factor or an explicit refusal;
- absence of a hidden preferred frame only on the tested operations.

### 9.1 Native-lift discriminator boundary

The I/C/N/R signature is operational. It does not exhaust the possible native
beables. A candidate native lift must use one fixed configuration object and one
parent indivisible endpoint law across every comparison arm, retain the contingent
preparation separately, and push forward to every complete adaptive endpoint
experiment. A noncentral represented coordinate may still be a definite hidden
native variable; a definite native variable may still fail every operational
record criterion. Any asserted path realizer is an additional object with a
separate endpoint-consistency burden.

Consequently a native mechanism is discriminated only by a licensed intervention
or held-out prediction. Empirical equivalence of all registered processes is not
ontological isomorphism, and an unread idle-extension example proves only
class-relative nonselection.

## 10. Gravitational reference systems

General relativity supplies an important analogy, not an inherited result.
Coordinate labels are gauge-dependent; relational observables can be defined using
physical matter or geometric reference fields. Such references are physical:
Brown--Kuchař dust, for example, adds a dynamical matter system and a privileged
reference frame/foliation to the model. Complete-observable constructions likewise
require declared clock/reference fields and constraint control.

Therefore a quantum reference record should not be called a gravitational clock
without proving, in one common matter--geometry law:

1. the reference is part of the dynamical configuration;
2. its stress energy and backreaction are included;
3. different matter clocks couple to one operational geometry;
4. diffeomorphism constraints and observable algebra close;
5. the low-energy predictions satisfy equivalence-principle and GR tests.

None of those conditions is met by the present finite record package.

## 11. Primary-source routing

- [Stinespring, positive functions on C*-algebras](https://doi.org/10.1090/S0002-9939-1955-0069403-4): CP-map dilation existence; not microscopic ontology
  selection.
- [Marvian--Spekkens, information-theoretic WAY theorem](https://arxiv.org/abs/1212.3378): perfect asymmetry, programming, and exact-measurement resource
  necessity; not a universal finite-error formula.
- [Bartlett--Rudolph--Spekkens, reference frames and superselection](https://arxiv.org/abs/quant-ph/0610030): reference resources and relational descriptions;
  not ontology selection.
- [Głowacki, Operational Quantum Frames](https://arxiv.org/abs/2304.07021):
  covariant POVMs and operational relative observables; not classical outcome
  formation.
- [Korbicz--Horodecki--Horodecki, spectrum broadcasting](https://arxiv.org/abs/1305.3247): redundant nondisturbing objective records under its
  hypotheses; not actualization.
- [Brown--Kuchař, dust as space/time reference](https://arxiv.org/abs/gr-qc/9409001): physical reference matter and deparametrization; not a derived
  universal clock.
- [Dittrich, partial and complete observables](https://arxiv.org/abs/gr-qc/0507106): relational Dirac observables under canonical-GR hypotheses; not a
  quantum-gravity completion.

## 12. Present disposition

```text
ARCHITECTURE-SIGNATURES:          CONSTRUCTED-PRIVATELY
COMPLETE-DISCRIMINATOR-SUITE:     SPECIFIED-PRIVATELY
FINITE-REFERENCE-LOWER-BOUND:     PROVED-PRIVATELY
ONE-INSTRUMENT-SELECTS-MECHANISM: REFUTED
EMPIRICAL-PLATFORM:               UNSELECTED
EMPIRICAL-DATA:                   NONE
BARANDES-ONTOLOGY:                UNSELECTED
NATIVE-ENDPOINT-EXPERIMENT-LIFT:  UNCONSTRUCTED
AQFT-EXTENSION:                   UNCONSTRUCTED
GRAVITATIONAL-REFERENCE:          UNCONSTRUCTED
GRAVITY:                          UNCONSTRUCTED
OFFICIAL-UNIT:                    NOT-AUTHORIZED
```
