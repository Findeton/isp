# PRIVATE THEOREM PACKAGE — one parent, two clock derivations

Date: 2026-08-23

Status: **PRIVATE / RESULT-NEUTRAL / SUPERSEDES THE AMBIGUOUS DUAL-PARENT READING**

Scientific result awarded: **none**

This package implements the correction from the private preflight audit. The
physical hypothesis is one frozen parent law P. A constrained clock-neutral route
and an autonomous complete-experiment route are two derivations from P, not two
independently fitted laws. Their agreement tests internal consistency. Physical
evidence comes from held-out interventions and readers against an independently
frozen laboratory comparator.

## 1. One-parent architecture

For every registered experiment e, one parent P supplies the complete physical
model. Two derivation maps produce operational transcript laws:

$$
\mu^{\rm con}_e=F_{\rm con}(P,e),
\qquad
\mu^{\rm aut}_e=F_{\rm aut}(P,e).
$$

The constrained route derives the law using the physical constraint, clock POVM,
physical inner product, and relational observables. The autonomous route derives
the same experiment from the parent carrier, fixed mechanism, record instruments,
and endpoint transcript.

An independently frozen laboratory comparator supplies

$$
\mu^{\rm lab}_e.
$$

The internal-consistency target is

$$
\mu^{\rm con}_e=\mu^{\rm aut}_e.
$$

The empirical target is

$$
\mu^{P}_e\stackrel{?}{=}\mu^{\rm lab}_e
$$

on held-out experiments, where mu^P is the common law only if internal
consistency passes.

## 2. Complete transcript

Let X_e be the standard-Borel complete endpoint transcript space. It contains:

- experiment and preparation identity;
- every supplied intervention-slot and policy label;
- every physical clock record;
- comparator outcomes;
- every later-readable controller/memory value;
- stopped, recurrent, null, leakage, and failure outcomes; and
- resource and disturbance observations.

The causal-slot order is supplied by the registered experiment. It is not removed
or derived in this unit.

### Theorem 2.1 — complete-reader criterion

Two probability measures on finite X_e are equal exactly when all singleton
indicator probabilities agree. On standard-Borel X_e, equality on a frozen
measure-determining pi-system and its monotone-class closure is sufficient.

Therefore selected marginals, means, or clock calibration tables do not establish
complete law equality.

### Theorem 2.2 — adaptive endpoint compilation

When the endpoint transcript retains every earlier record, chosen setting, policy
identity, and final outcome, one endpoint law determines all positive-support
registered adaptive conditionals. This is an operational statement and does not
postulate a path law over unrecorded native configurations.

## 3. Valid clock records

Let Phi be a clock POVM and {I_r} an instrument.

### Theorem 3.1 — record typing

A clock reading is a valid operational classical record only if:

1. the branch maps form a normalized instrument;
2. the output contains an explicit commutative record factor;
3. every registered symmetry/constraint action preserves its center;
4. all later guards consume that retained factor;
5. every future-readable memory is represented; and
6. null and failed writes remain typed outcomes.

A phase effect, conditional state, pointer basis, or classical table alone is not
a record.

### Theorem 3.2 — finite invariant relational record

For a finite joint group action on clock and reference configurations, every
invariant function f defines a complete invariant PVM by summing basis projectors
over its fibers. A neutral pointer controlled by those fiber projectors records f
without destroying coherence inside one f-fiber.

The theorem does not choose f, a physical reference, or a clock transport law.

### Continuous scope

A continuous covariant POVM requires a model-specific normal instrument,
measurable posterior field, null-class convention, and finite-resolution or
integrated record interpretation. Generic point evaluation on a nonatomic
L-infinity factor is refused.

## 4. Constrained derivation F_con

The constrained derivation must prove:

1. physical landing of sources, branches, posteriors, records, guards, and
   readers;
2. normalized conditional comparator laws at positive-support clock readings;
3. equality with physical relational-observable expectations;
4. the exact clock-domain and nonideal POVM hypotheses;
5. retention of clock--system interactions; and
6. complete treatment of stopped, recurrent, and null clock regions.

The route may yield source-dependent, time-nonlocal, or reduced nonunitary
dynamics. Those are outcomes, not reasons to retune the parent.

## 5. Autonomous derivation F_aut

The autonomous derivation must use P's same carrier and law. It must prove:

1. one fixed Hamiltonian or endpoint mechanism after one exposed initialization;
2. physical program/reference/controller degrees of freedom;
3. a complete retained endpoint transcript;
4. nontrivial clock-controlled comparator response;
5. finite accuracy, resolution, recurrence, stopping, leakage, disturbance, and
   backreaction bounds; and
6. no externally switched gate sequence inside the claimed mechanism.

This earns a finite autonomous realization inside P. It does not select that
realization as the unique ontology.

## 6. Internal-consistency theorem

### Theorem 6.1

Assume both derivations land on the same complete transcript interface. The
following are equivalent for a registered experiment family:

1. mu_con,e equals mu_aut,e for every e;
2. every measure-determining complete reader has equal expectation under both
   derivations; and
3. all positive-support adaptive conditionals obtained from the endpoint
   transcripts agree.

If the equality is approximate, the normalization and error metric must be frozen
before calculation. For total variation defined as half the L1 distance, bounded
readers with sup norm at most one differ in expectation by at most twice the total
variation.

### Meaning

This is an internal consistency theorem for P. It is not independent empirical
support and does not select P over operationally equivalent parents.

## 7. Empirical adequacy

### Definition 7.1 — promotion-bearing held-out evidence

P has held-out operational adequacy only if, on a preregistered test set:

1. its common transcript law agrees with laboratory observations within a frozen
   equivalence region;
2. no-clock, mistuned-clock, frozen-clock, stopped-clock, and interaction-deletion
   controls separate in the predicted directions;
3. finite-resource effects are predicted before test data;
4. one adaptive continuation is predicted completely;
5. a coherent reader tests more than scalar clock statistics; and
6. calibration parameters are fewer than independent held-out constraints.

Standard quantum agreement validates this operational architecture. It does not
confirm a native stochastic ontology.

### Definition 7.2 — new-physics evidence

A new-physics coordinate requires a preregistered prediction that differs from
standard quantum theory, QFT on the supplied background, or GR as appropriate.
No such prediction is presently supplied.

## 8. Universal scheduled-simulator no-go

### Theorem 8.1

For every finite family of conditional transcript laws mu(dx|e), there exists one
externally scheduled parent simulator with physical input e that reproduces the
entire family.

### Proof

Let e be supplied as an input register and u be one uniform random seed. For each
e, choose a measurable inverse-CDF map Q_e such that Q_e(u) has law mu(dx|e). One
fixed simulator law reads e and u, writes Q_e(u) to the endpoint memory, and
therefore reproduces every complete reader for every experiment. QED.

### Corollary 8.2

No finite operational transcript family can exclude every hidden-schedule
completion. A positive result may establish that P contains a finite autonomous
realization and that an external scalar parameter is unnecessary for the task. It
cannot prove fundamental timelessness.

## 9. Dilation nonselection

### Theorem 9.1

Every finite quantum instrument has a unitary dilation on a larger space. Finite
gate sequences also admit enlarged clock/program representations. Consequently
unitary or time-independent representation existence is not a physical clock
selection theorem.

### Evidential requirement

The mechanism must be independently restricted by interaction form, locality or
coupling graph, resources, preparation, reuse across tasks, and held-out
interventions. A bespoke dilation constructed from the target instrument earns
only a representation coordinate.

## 10. Route-provenance certificate

Route provenance is a construction certificate, not a physical theorem. It must
bind:

1. immutable parent P;
2. separate derivation artifacts;
3. absence of held-out output-table imports;
4. shared parameters and their calibration sources;
5. a dependency graph from P to every transcript field;
6. more held-out constraints than fitted degrees of freedom; and
7. refusal of outcome-dependent transcript-map repair.

The two derivations may share P because they must describe one law. Their
mathematical steps should nevertheless be independently checkable.

## 11. Finite nonideal-measurement discriminator

For one finite coherence-versus-diagonal instrument schema, define

$$
\mathcal J_{\rm coh}(X)
=
\sum_{t,t'}G_{tt'}V_tXV_{t'}^*\otimes|t\rangle\langle t'|
$$

and

$$
\mathcal J_{\rm diag}(X)
=
\sum_tG_{tt}V_tXV_t^*\otimes|t\rangle\langle t|.
$$

### Theorem 11.1

On frozen input system S and complete-reader system R, these two finite
instruments are operationally equivalent exactly when every reader in R
annihilates their off-diagonal difference for every input in S.

This is a finite discriminator schema. It is not a general theorem identifying
the full twirled-observable and purified-measurement frameworks. Any application
to those frameworks requires a model-specific derivation of their actual
instruments.

## 12. Two-clock structural certificate

Two clocks are structurally distinct only after printing:

1. separate faithful carrier embeddings;
2. separately addressable intervention families;
3. nonaliasing complete response signatures;
4. common-controller/reference degrees of freedom;
5. interactions and cross-disturbance; and
6. proof neither output is a relabel or deterministic copy of the other.

No joint probability table alone can prove this factorization.

## 13. Local clock validity

### Theorem 13.1 — periodic ceiling

Without a physical winding record, a cyclic clock has no injective phase lift on
any supported segment containing a repeated phase. Its exact validity window ends
before recurrence or at an explicit ambiguity outcome.

### Theorem 13.2 — stopped-sector rule

Every positive-support sector with no comparator-sensitive phase transport is a
stopped sector. It remains in the endpoint law with full weight. Postselection
cannot turn a local clock into a global one.

## 14. External scalar-parameter redundancy

Let lambda be the external scalar/orbit/runtime parameter used in an ordinary
derivation. The experiment identity, policy, and causal-slot order are separate
supplied context variables and remain inputs.

### Definition 14.1

Lambda is task-redundant on a frozen domain when:

1. it is absent from P's complete predictor and caches;
2. predictions depend on physical clock records plus supplied experiment context;
3. clock interventions produce P's preregistered response;
4. no-clock and mistuned controls fail the target;
5. one predictor handles every held-out source and policy without retuning; and
6. both derivations of P agree internally.

### Theorem 14.2

Passing Definition 14.1 establishes operational redundancy of lambda for that
task. It does not remove supplied causal-slot order and, by Theorem 8.1, cannot
exclude every hidden-time completion.

## 15. Native endpoint-law lift

For a future native packet B, one fixed endpoint law supplies

$$
\mu^{\Omega}_e(dc_0,dc_f)
=
\Omega_e(dc_0)\Gamma_e(dc_f\mid c_0).
$$

If O_e maps final native configurations to the complete transcript, the lift
condition is

$$
(O_e)_*\mu^{\Omega}_e=\mu^P_e
$$

for every registered experiment and preparation.

This condition requires no probability measure over unrecorded intermediate
paths. It does not derive the target/conditioning time labels already present in
the endpoint law. Native clock status additionally requires a physical phase
subsystem and record map inside the configuration ontology.

## 16. Chronology, metric, and gravity walls

Clock phase transport is not intervention-derived precedence. An operational
chronology requires signed response, independent no-backwards/prefix invariance,
mediation/common-cause controls, co-onset bundling, cycle classification, and
local-finiteness/continuum tests.

Clock agreement is not a metric. Proper time and geometry require independently
calibrated multiple clocks, signal/radar structure, locality, dimension,
signature, scale, and dynamical agreement.

Gravity requires one common matter--geometry law, universal coupling, constraint
closure, conservation, equivalence-principle controls, and held-out GR limits.

## 17. Hostile controls

- G1. Two unrelated fitted parents called two derivations.
- G2. Generic dilation called independent physics.
- G3. Internal route equality called empirical evidence.
- G4. Experiment slot order claimed removed with scalar lambda.
- G5. E-specific simulator laws instead of one simulator with input e.
- G6. Provenance certificate called a physical theorem.
- G7. Finite discriminator called the general twirled/purified theorem.
- G8. Public literature evidence forbidden during architecture selection.
- G9. Candidate held-out outputs inspected during model choice.
- G10. Phase POVM called a retained record.
- G11. Stopped/recurrent outcomes discarded.
- G12. Standard-QM agreement called native-ontology confirmation.
- G13. Physical autonomous realization called unique ontology.
- G14. Clock phase called chronology.
- G15. Two clocks called metric.
- G16. Clock--matter response called gravity.

## 18. Product ceiling

```text
ONE-PARENT-LAW:                         REQUIRED / UNSELECTED
VALID-INVARIANT-CLOCK-RECORD:           UNCONSTRUCTED
CONSTRAINED-DERIVATION:                 UNCONSTRUCTED
FINITE-AUTONOMOUS-REALIZATION:          UNCONSTRUCTED
INTERNAL-ROUTE-CONSISTENCY:             UNTESTED
HELD-OUT-OPERATIONAL-ADEQUACY:          UNTESTED
NEW-PHYSICS-DEVIATION:                  NONE REGISTERED
SECOND-CLOCK-INDEPENDENCE:              UNCONSTRUCTED
EXTERNAL-SCALAR-TASK-REDUNDANCY:        UNTESTED
NATIVE-ENDPOINT-LIFT:                   UNCONSTRUCTED
OPERATIONAL-CHRONOLOGY:                 UNCONSTRUCTED
PROPER-TIME/METRIC:                     UNCONSTRUCTED
GRAVITY/ACTUALITY:                      UNCONSTRUCTED
```

## 19. Present disposition

The corrected theorem package is ready for private pin integration. It does not
authorize model selection or construction.

No repository file was edited.
