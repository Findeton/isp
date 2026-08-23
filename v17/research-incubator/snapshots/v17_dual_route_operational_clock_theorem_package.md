# PRIVATE THEOREM PACKAGE — dual-route operational clocks

Date: 2026-08-23

Status: **PRIVATE / RESULT-NEUTRAL / NO MODEL OR UNIT OPENED**

Scientific result awarded: **none**

This package develops the generic mathematics required before choosing a clock
model. It is deliberately representation-aware: finite probability laws always
admit scheduled simulators and unitary dilations, so existence of a second
representation is not evidence that time has emerged. A positive clock result
requires typed records, physical phase transport, constrained resources,
independent provenance, and held-out operational agreement.

## 1. Typed setting

Let e range over a frozen finite or standard-Borel family of complete clock
experiments. Each experiment has a complete transcript space X_e containing:

- preparation and setting provenance;
- every retained clock record;
- every comparator outcome;
- controller memory used by later guards;
- stopped, recurrent, leakage, and failure flags; and
- every later complete-reader output.

The constrained route assigns a probability law

$$
\mu^{\rm con}_e\in\mathcal P(X_e),
$$

and the autonomous route assigns

$$
\mu^{\rm aut}_e\in\mathcal P(X_e).
$$

An ordinary laboratory comparator, when present, assigns

$$
\mu^{\rm lab}_e\in\mathcal P(X_e).
$$

The maps into X_e are part of the physical interface. Relabeling an internal
state after the calculation does not change the transcript map.

## 2. Complete-reader equivalence

### Theorem 2.1 — finite transcript criterion

For a finite transcript space X, two laws mu and nu are equal if and only if

$$
\sum_{x\in X}f(x)\mu(x)
=
\sum_{x\in X}f(x)\nu(x)
$$

for every bounded reader f:X to R. It is enough to test the indicator readers of
all singletons, or any frozen linear basis spanning all real functions on X.

### Consequence

Equality of clock marginals, means, calibration tables, or selected conditionals
does not imply complete route equivalence. The complete transcript law is the
minimal exact object.

### Theorem 2.2 — standard-Borel criterion

For standard-Borel X, equality on a pi-system generating its sigma-algebra and
closed under the required monotone-class extension implies equality of measures.
The registered reader family must therefore be measure determining. A finite
tomographic approximation earns only its declared tolerance and model class.

### Theorem 2.3 — adaptive transcript criterion

Let a physical policy choose later settings from earlier retained records. If the
complete transcript includes the policy identity, every setting, every record, and
the final output, equality of the endpoint transcript laws implies equality of all
positive-support registered adaptive conditionals. The converse holds when the
initial law and all conditional kernels are included consistently.

This theorem does not introduce stochastic kernels at unobserved intermediate
native boundaries. It is an operational endpoint statement.

## 3. Record and phase are separate objects

Let C be a clock carrier, Phi={E_tau} a finite phase POVM, and R a record carrier.
A measurement channel has the form

$$
\mathcal I(\rho)
=
\sum_\tau \mathcal I_\tau(\rho)\otimes|\tau\rangle\langle\tau|_R,
\qquad
\sum_\tau\mathcal I_\tau\ \text{trace preserving}.
$$

### Theorem 3.1 — valid classical clock record

The phase output is an operational classical record exactly when:

1. the branch maps form a normalized instrument;
2. the complete output algebra contains the commutative R factor;
3. every registered symmetry maps its center into itself;
4. every later guard consumes the retained R factor rather than an unrecorded
   phase label; and
5. every future-readable memory is represented in the typed boundary.

The existence of Phi alone proves none of these items.

### Theorem 3.2 — finite invariant relational record

Let a finite group G act jointly on a clock configuration X_C and reference
configuration X_F. Let

$$
f:X_C\times X_F\longrightarrow Y
$$

be invariant under the diagonal action. Then the fiber projections

$$
E_y=\sum_{f(c,r)=y}|c,r\rangle\langle c,r|
$$

form a G-invariant PVM. A neutral pointer controlled by these projections defines
a G-invariant premeasurement, and dephasing or broadcasting only the pointer
produces a classical relational record while preserving system coherence inside
each f-fiber.

This is a record theorem, not a clock theorem. Clock status additionally requires
transport of C and comparator response.

### Continuous qualification

For a continuous covariant POVM, Naimark dilation and covariant-instrument
existence must be proved on the selected measurable/null-class domain. A raw
point value in a nonatomic L-infinity record algebra is not a normal state.
Continuous outputs are integrated ensemble records or finite-resolution bins
unless a sharper physical construction is provided.

## 4. Constrained route

Let the clock-neutral theory have physical state space H_phys, constraint C-hat,
physical inner product, clock POVM Phi, comparator algebra A_S, and relational
instrument J_con.

### Gate C1 — physical landing

Every preparation, instrument branch, retained record, and complete reader must
land in the physical state/algebra domain. Bare kinematic clock effects are not
physical merely because they have phase labels.

### Gate C2 — conditional dynamics

For every positive-support clock record tau, the conditional comparator state or
law is defined and normalized. Null clock events carry an explicit refusal or
version convention.

### Gate C3 — complete relational observable

The conditional probabilities agree with physical-inner-product expectations of
gauge-invariant complete observables for every registered reader. State-level
agreement alone is insufficient.

### Gate C4 — nonideal clock domain

The clock POVM, nonorthogonality, recurrence, and invalid regions are explicit.
No ideal time operator is silently imported.

### Gate C5 — interaction retention

Clock--system interactions remain in C-hat. If the conditional law becomes
time-nonlocal, source dependent, or nonunitary on a reduced description, that is
reported rather than repaired away.

## 5. Autonomous route

Let the autonomous route have a fixed physical carrier, one initial preparation,
and a single time-independent Hamiltonian H_aut or one fixed native endpoint law.
It includes clock, comparator, reference, controller, memory, and failure degrees
of freedom.

### Gate A1 — one fixed mechanism

After initialization, no external switch chooses which interaction acts. Every
later control is generated by physical state in the carrier.

### Gate A2 — explicit program and reference

The initial program wavepacket, reference asymmetry, energy, dimension, and
reset/preparation cost are in the resource ledger. They are not free constants.

### Gate A3 — record-complete endpoint

The target endpoint contains the full registered transcript. A history-state
clock register that is never physically read does not satisfy this gate.

### Gate A4 — comparator nontriviality

The comparator response differs from no-clock, mistuned-clock, frozen-clock, and
interaction-deletion controls on preregistered held-out readers.

### Gate A5 — finite validity

Accuracy, resolution, recurrence, stopping, leakage, disturbance, and
backreaction are bounded on one declared window.

## 6. Dual-route theorem

### Theorem 6.1 — operational dual-route equivalence

Assume both routes satisfy their respective gates and share the same complete
transcript interface. Then the following are equivalent:

1. mu_con,e = mu_aut,e for every registered e;
2. every measure-determining complete reader has equal expectation under the two
   routes for every registered preparation and policy; and
3. every positive-support adaptive conditional derived from the complete
   transcript agrees.

When the equality holds only within epsilon in total variation, every bounded
reader f with norm at most one differs by at most 2 epsilon under the conventional
total-variation normalization. The precise normalization must be frozen.

### Scope

This theorem establishes operational equivalence between two typed physical
descriptions. It does not establish:

- that the routes are microscopically identical;
- that the autonomous mechanism is unique;
- that external time is absent from reality;
- that the constraint is fundamental;
- that either route is a native ontology; or
- that chronology is derived.

## 7. Representation-as-autonomy no-go

### Theorem 7.1 — scheduled-simulator completion

For every finite family of transcript laws {mu_e}, there exists an externally
scheduled classical simulator that samples x from mu_e and writes the complete
transcript x into a memory register. Therefore no finite collection of transcript
probabilities alone can prove that the underlying mechanism is autonomous or
timeless.

### Proof

For each experiment e, take an external random seed u uniformly distributed on
[0,1]. Partition the interval into measurable cells of lengths mu_e(x), and let a
scheduled controller write the corresponding x. All registered readers reproduce
mu_e exactly. The mechanism uses an external scheduler by construction. QED.

### Theorem 7.2 — unitary-dilation nonselection

Every finite quantum instrument admits a Stinespring/Naimark dilation. A clocked
program Hamiltonian can encode a finite gate sequence in an enlarged carrier.
Consequently the existence of a unitary or time-independent dilation does not by
itself prove that a physical clock, autonomous mechanism, or fundamental time has
been found.

### Required escape

A positive autonomy result must constrain the mechanism independently of the
target transcript through locality, interaction form, resource bounds,
preparation independence, reuse across multiple tasks, and held-out predictions.
The autonomous route may not be a bespoke dilation built after the constrained
route's complete law is known.

## 8. Provenance independence

### Definition 8.1

The constrained and autonomous routes have independent provenance relative to a
test family if:

1. their dynamical forms are frozen before held-out outputs are calculated;
2. neither route imports the other's output table or fitted latent states;
3. shared parameters are fixed by common training data or independently measured
   resources;
4. the held-out readers outnumber the shared fitted degrees of freedom;
5. at least one intervention changes a physical resource in one route and has a
   predeclared image in the other; and
6. failure of equality cannot be repaired by outcome-dependent redefinition of
   transcript maps.

This is stronger than source-code independence and weaker than ontological
independence. It is an evidential condition.

### Proposition 8.2

If P_aut is obtained solely by applying a generic dilation theorem to the already
fixed J_con, route agreement is a representation theorem, not independent physical
evidence. It may still be mathematically valuable but cannot earn the strongest
external-time-redundancy rung.

## 9. Nonideal-measurement fork

For a finite phase family, write an idealized purified route schematically as

$$
\mathcal J_{\rm PM}(\rho)
=
\sum_{t,t'}G_{tt'}V_t\rho V_{t'}^*\otimes|t\rangle\langle t'|_M,
$$

where G is the clock-state Gram matrix. A diagonal/twirled route discards or never
creates the t-not-equal-t-prime terms:

$$
\mathcal J_{\rm TO}(\rho)
=
\sum_tG_{tt}V_t\rho V_t^*\otimes|t\rangle\langle t|_M.
$$

### Theorem 9.1 — exact operational fork criterion

On a declared input operator system S and complete reader system R, the routes are
operationally equivalent if and only if

$$
\operatorname{tr}\!\left[
F\sum_{t\ne t'}G_{tt'}V_t X V_{t'}^*\otimes|t\rangle\langle t'|
\right]=0
$$

for every X in S and F in R.

Orthogonal clock states, explicit record dephasing, or readers blind to the
off-diagonal memory are sufficient special cases. None is automatic for a finite
nonideal clock. Dephasing is changed physics when later coherent readers are
admitted.

### Consequence

The twirled and purified routes must be treated as different physical
implementations unless this condition is proved on the complete operational
domain. Their disagreement is a discriminator, not a defect to average away.

## 10. Two-clock independence

### Definition 10.1 — structural independence

Two candidate clocks A and B are structurally distinct when the parent contains
faithful, separately addressable carrier embeddings and local intervention
families U_A and U_B such that:

1. neither carrier algebra is a relabeling or deterministic record copy of the
   other;
2. at least one A-local and one B-local intervention have distinct complete
   response signatures;
3. the interventions are physical operations inside one law, not law changes;
4. common-controller and common-reference degrees of freedom are explicit; and
5. interactions between A and B are retained and measured.

Statistical independence is neither required nor sufficient. Perfectly correlated
physical clocks can be distinct, while independent random number generators need
not be clocks.

### Proposition 10.2 — transcript nonselection

No joint reading distribution alone proves structural independence: an enlarged
single carrier can simulate any finite joint law. Structural factorization and
separate interventions are therefore mandatory declared-and-tested inputs.

## 11. Local clock validity

Let the phase outcome space be cyclic with period n. A local clock chart is a
subset W and lift ell:W to R such that ell is injective on every supported
trajectory segment within the declared window.

### Theorem 11.1 — recurrence ceiling

Without a physical winding record, no supported segment containing two visits to
the same phase can admit an injective lift. Hence the maximum exact validity
window ends before the first supported recurrence or at an exposed ambiguity flag.

### Theorem 11.2 — stopped-sector rule

If a positive-support sector has phase law independent of the proposed transport
parameter or comparator change, the clock is stopped there. It must appear as an
ordinary outcome with its full weight. Postselection cannot recover a global
clock claim.

### Approximate clock report

An approximate finite clock must report, on the same held-out window:

- phase-estimation error;
- missed/double tick probability;
- calibration residuals;
- comparator prediction error;
- disturbance of clock and comparator;
- recurrence/wrap probability;
- stop/failure probability; and
- resource cost.

## 12. Hidden-time dependency theorem

### Definition 12.1

Let D_pred be the minimal declared dependency graph of the complete predictor.
A laboratory schedule variable s is operationally redundant on a frozen domain
if:

1. s is absent from every predictor input and cached object;
2. all predictions are functions of physical clock records and declared physical
   context;
3. interventions on the clock alter predictions as the parent law specifies;
4. no-clock and mistuned-clock controls fail the target law; and
5. the same predictor handles every held-out source and policy without retuning.

### Theorem 12.2 — bounded conclusion

Passing Definition 12.1 proves operational redundancy of s for the registered
prediction task. It does not prove that no observationally equivalent hidden-time
completion exists, by Theorem 7.1. The correct result is task-relative
redundancy, not fundamental timelessness.

## 13. Native endpoint-law commuting square

For a future native packet B and each complete experiment e, let

$$
\mu^{\Omega}_{e}(dc_0,dc_f)
=
\Omega_e(dc_0)\Gamma_e(dc_f\mid c_0),
$$

where the conditioning boundary is an admitted Barandes division and c_f retains
the complete transcript. Let O_e map final configurations to X_e.

The native lift condition is

$$
(O_e)_*\mu^{\Omega}_e
=
\mu^{\rm con}_e
=
\mu^{\rm aut}_e
$$

for every registered e, preparation, and complete reader.

This equation needs no probability law over unrecorded intermediate
configurations. A path realizer is an additional coordinate. The equation also
does not derive the target/conditioning time labels used by the native law; a
physical clock subsystem must still be identified inside C.

## 14. Hostile theorem controls

- H1. Compare only clock marginals.
- H2. Omit policy/settings from the transcript.
- H3. Treat a POVM as an instrument.
- H4. Treat a raw pointer label as invariant.
- H5. Use a nonatomic point state on L-infinity.
- H6. Let a kinematic branch leave the physical subspace.
- H7. Delete clock--system interactions.
- H8. Exclude null and stopped outcomes.
- H9. Build P_aut by copying P_con's output table.
- H10. Use a generic Stinespring dilation as physical evidence.
- H11. Use a Feynman program counter as a clock.
- H12. Hide external switching in a potential selected after the target.
- H13. Compare two routes only on training readers.
- H14. Refit the transcript map after disagreement.
- H15. Assume twirled/purified equivalence for nonideal clocks.
- H16. Dephase the memory while retaining a coherent-reader claim.
- H17. Call copied records independent clocks.
- H18. Infer structural independence from statistical independence.
- H19. Omit a positive-support recurrence.
- H20. Append a free winding counter.
- H21. Infer fundamental timelessness from task-relative redundancy.
- H22. Infer chronology from phase transport.
- H23. Infer native ontology from dual-route agreement.
- H24. Insert a path measure into an indivisible endpoint law.
- H25. Identify Barandes division with operational record stability.
- H26. Promote finite clock agreement to proper time or metric.

## 15. Theorem status

```text
T2.1--T2.3 COMPLETE-READER MEASURE CRITERIA:        DERIVED
T3.1 VALID CLASSICAL RECORD CRITERION:              DERIVED FROM ACCEPTED TYPING
T3.2 FINITE INVARIANT RECORD:                       DERIVED IN PRIVATE PACKAGE
C1--C5 CONSTRAINED-ROUTE GATES:                     SPECIFIED
A1--A5 AUTONOMOUS-ROUTE GATES:                      SPECIFIED
T6.1 DUAL-ROUTE OPERATIONAL EQUIVALENCE:            DERIVED
T7.1 SCHEDULED-SIMULATOR NO-GO:                     DERIVED
T7.2 UNITARY-DILATION NONSELECTION:                 DERIVED
PROVENANCE-INDEPENDENCE CRITERION:                  SPECIFIED
T9.1 NONIDEAL-MEASUREMENT FORK:                     DERIVED ON FINITE SCHEMA
TWO-CLOCK STRUCTURAL INDEPENDENCE:                  SPECIFIED / NOT SELECTED
T11.1--T11.2 LOCAL VALIDITY RULES:                  DERIVED
T12.2 TASK-RELATIVE REDUNDANCY CEILING:             DERIVED
NATIVE COMMUTING SQUARE:                            SPECIFIED / LIFT UNCONSTRUCTED
MODEL/PARAMETERS/HARDWARE:                          UNSELECTED
```

## 16. Decision

The generic theorem package reveals the actual live scientific burden:

> The next model must do more than possess a stationary constraint or an
> autonomous dilation. It must realize the same complete finite clock experiment
> through independently constrained relational and autonomous routes, with valid
> invariant records, finite-resource failures, interactions, and held-out
> predictions. Even success earns only operational external-parameter redundancy.

This is the narrowest next gate that advances Phase T without pretending to solve
chronology, ontology, spacetime, or gravity.

No repository file was edited.
