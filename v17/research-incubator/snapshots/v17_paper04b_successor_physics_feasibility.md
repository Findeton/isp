# ISP v17 — Paper 04B successor physics feasibility memo

Date: 2026-08-23

Status: **PRIVATE / NONBINDING / NOT A PIN / NO SUCCESSOR AUTHORIZED**

Scientific result awarded: **none**

Parent model selected: **no**

Authority created by this memo: **none**

This memo follows terminal adjudication commit
`8dc2889a27ca60dbd564f6ee7aa2e2fc5996561a` and the frozen adjudication
`v17/note-paper04b-pin-review-adjudication.md`, ordinary SHA-256
`9343d9845f993081ad9c94ab8200ab761edf31676008c69e00de131352f7f953`.
It tests the proposed R1--R4 repair against established physics before any
request to freeze a successor. It does not edit the accepted corpus.

## 1. Main finding

R1--R4 are necessary but not sufficient as currently phrased. The former pin
used one symbol, `lambda`, for three physically different objects:

1. a gauge/orbit label in a constrained representation;
2. a reading of an external physical reference clock or a laboratory duration;
3. an exogenous time-indexed control or endpoint schedule.

These cannot share one removal theorem.

- A gauge label should not affect physical predictions in the first place.
- A physical reference reading should affect clock and system statistics; an
  internal clock can replace it only conditionally or protocol-by-protocol.
- A control schedule is absent only when the controller and its timing resource
  are physical parts of the parent.

The old complete-predictor factorization is therefore the wrong maximum target
for an informative clock. If the complete transcript contains an internal clock
record `R` and external time `tau` is physically operative, then the distribution
of `R` should generally vary with `tau`. Demanding the whole transcript be
independent of `tau` either fails or reduces `tau` to a dummy/gauge label.

The physically meaningful relational target is screening/sufficiency:

$$
Y\;\perp\!\!\!\perp\;\tau\mid(R,E),
$$

on a preregistered operational domain, where `Y` denotes the registered system
and comparator outcomes and `E` retains all supplied non-temporal context. This
can hold exactly or within a frozen complete-law metric. It says that after the
internally generated physical clock record is known, the external reference
reading adds no predictive information for the specified system task. It does
not say the clock record itself is independent of external time.

## 2. Physics-supported object split

Any revised pin should type these separately before model comparison.

| Symbol | Physical role | Correct question |
|---|---|---|
| `gamma` | gauge/orbit coordinate of a constrained representation | are physical observables invariant and are route maps well typed? |
| `tau` | reading of an independent external clock or laboratory duration | does internal record `R` carry time information, and does it screen `Y` from `tau`? |
| `u_tau` | externally scheduled control, switch, stop, or detector-opening action | is it absent after initialization, or physically generated and resource-counted inside `P`? |
| `R` | internally produced retained clock record | is it classical/readable, informative, intervenable, finite-resource, and adequate on held-out tasks? |
| `Y` | complete registered system/comparator transcript excluding `R` | is its conditional law relative to `R` adequate and external-reference invariant? |
| `E` | experiment identity, preparation, passive readout choice, policy, causal slots, and other supplied context | is every retained context explicit and prevented from caching `tau`? |

No future paper should use `external scalar/orbit/runtime parameter` as one
undifferentiated noun phrase.

## 3. Operational clock predicate

The literature supports defining a clock by an information-bearing task, not by
its Hamiltonian, phase label, or name. A model-neutral task packet `K` should
freeze:

1. an independently defined reference variable `tau` supplied by a physical
   comparator clock over a local ordered laboratory domain;
2. a complete internal record `R` and a reader/estimator of `tau` from `R`;
3. a proper loss, delay-function, phase, or discrimination score appropriate to
   the frozen task;
4. a no-clock baseline plus frozen/mistuned controls;
5. a positive held-out improvement threshold with uncertainty, covariance,
   multiplicity, failure, and stopping rules;
6. clock-local rate/phase/resource interventions whose effects cannot be
   reproduced by copying the comparator or supplied slot label;
7. local aliasing, recurrence, degradation, and validity domains; and
8. a retained classical outcome instrument, with coherent clockwork memory kept
   distinct from its classical record.

The minimal nonvacuity condition is that some registered reader of `R` carries
positive decision-theoretic information about `tau` beyond all frozen baselines.
No particular Fisher-information, mutual-information, or mean-square-loss metric
is universally privileged; the task and scoring rule must freeze before family
selection.

This is an operational laboratory clock. It does not define fundamental time or
derive chronology.

## 4. Autonomy and self-timing

Autonomy is a separate coordinate from clock adequacy.

A time-independent generator is necessary in many autonomous-clock models but
is not sufficient for the claim sought here. A valid autonomy certificate must
show:

1. after one exposed preparation, no control inside the registered run is a
   function of an unrepresented external time signal;
2. the clockwork, tick/record register, controller, reference, environment, and
   reset resources needed for the task are represented in `P`;
3. observation of the classical record is nondemolition on the admitted clock
   dynamics to the frozen tolerance;
4. a detector-opening or endpoint-selecting pulse is a physical intervention,
   not passive readout;
5. either a represented internal mechanism writes an available record whose law
   is stable over a nonzero passive-interrogation domain, or a represented second
   clock schedules the endpoint; and
6. finite recurrence and late-reader failures remain explicit.

An open-system or large-environment completion is allowed. A finite closed
unitary carrier must not be advertised as producing an irreversible classical
record forever; recurrence and record-erasure channels must remain visible.

## 5. Correct relational-replacement theorem

Let the one parent produce a joint kernel

$$
K_\tau(dR,dY\mid E)
$$

for an externally referenced validation protocol. A nonvacuous relational clock
claim needs all of the following.

### 5.1 External-reference informativeness

There exist `tau_1 != tau_2` and a preregistered reader of `R` for which the
record laws are separated by a positive frozen margin. Equivalently, `R` is not
ancillary for the registered external-time task.

### 5.2 Relational screening

There exists a kernel `Q(dY|R,E)`, independent of `tau`, such that

$$
K_\tau(dY\mid R,E)=Q(dY\mid R,E)
$$

for all registered interventions and common-support clock records, exactly or
within the frozen tolerance. Continuous records require the accepted regular-
conditional/a.e. semantics; null records remain explicit failures.

### 5.3 Protocol equivalence

The complete instrument for an externally triggered measurement at `tau` must
be compared with the complete instrument for an internally triggered or
clock-conditioned measurement at `R`. Postselection on a record after an
externally timed interaction is not automatically equivalent to an interaction
physically triggered by that record. Finite-clock time-nonlocality and
measurement disturbance are allowed outcomes, not errors to idealize away.

### 5.4 Leakage refusal

`tau` may not remain in experiment metadata, source preparation, slot depth,
controller memory, random seed, cache, lookup table, endpoint pulse, or a prior
that is marginalized only after use.

### 5.5 Exact meaning

Success establishes task-relative relational sufficiency. It does not eliminate
the mathematical evolution parameter from every representation, prove a
timeless universe, select a microscopic ontology, or derive temporal order.

## 6. Gauge invariance is a different theorem

For a constrained parent with gauge/orbit label `gamma`, freeze a group/action,
constraint domain, physical inner product, and complete invariant instrument.
Then test whether the physical joint law and relational observables descend to
the gauge quotient and whether the constrained and autonomous descriptions are
restrictions of one primitive law.

This is an internal consistency/representation theorem. It cannot count as the
empirical replacement of an operative external clock. A dummy `gamma` is not a
clock result, even if it disappears exactly.

## 7. Two clocks should be an independent branch

The former cumulative L5 -> L6 ordering is not a logical necessity.

- One adequate self-timing clock can, in principle, establish relational
  screening for a specified system task.
- Two separately adequate clocks are required for synchronization, cross-clock
  comparison, and clock-switch/frame-covariance claims.
- A second clock does not by itself strengthen the single-clock screening
  theorem if both are driven by the same hidden external schedule.

The successor should use a dependency product rather than one linear ladder:

```text
VALID CLASSICAL RECORD
        |
        +--> CLOCK-TASK INFORMATIVENESS --> HELD-OUT CLOCK ADEQUACY
        |
        +--> SELF-TIMING/AUTONOMY --> COMPLETION/READOUT CERTIFICATE

ONE PARENT + CLOCK ADEQUACY + AUTONOMY
        --> RELATIONAL SCREENING / PROTOCOL EQUIVALENCE

TWO SEPARATELY ADEQUATE CLOCKS + STRUCTURAL MANIPULABILITY
        --> JOINT CLOCK COMPARISON
        --> COMPLETE CLOCK-SWITCH MAPS
```

A headline may report a meet of independently earned coordinates, but no
coordinate should be made prerequisite merely to create a prettier ladder.

Common environments or references need not be forbidden; they must be
represented and subjected to interventions that distinguish shared drive from
separate clock response.

## 8. One-parent intersection problem

Established physics supplies the ingredients separately, but does not obviously
supply their exact conjunction in one finite operational packet:

1. constrained/Page--Wootters/relational-observable families provide
   clock-neutral and conditional descriptions, covariant clock POVMs, and
   temporal-frame changes under stated hypotheses;
2. autonomous ticking-clock families provide self-timing classical tick
   registers, time-independent generators, accuracy measures, and explicit
   resource costs;
3. finite autonomous-control/quasi-ideal-clock families provide fixed physical
   controllers with quantified energy, dimension, accuracy, and backreaction;
4. complete operational instruments provide the retained classical boundary
   needed to avoid Paper 04's pointer-type failure.

The future model comparison must score candidate **intersections**, not score
these ingredients separately and then graft the winners together. A legitimate
Stage-B outcome is:

```text
NO ESTABLISHED FAMILY INSTANTIATES THE FROZEN INTERSECTION
```

That outcome should stop the branch rather than invite a bespoke Hamiltonian.

## 9. Empirical feasibility before model choice

The no-hardware boundary remains consequential. Before selecting a parent, a
future unit must determine whether qualifying held-out laboratory data exist.

- Public results used to compare families are training/model-selection evidence.
- A plot or dataset already inspected while choosing a model cannot later become
  promotion-bearing holdout.
- Simulation can test mathematics and power but cannot earn operational adequacy.
- If no pre-existing sequestered data with an auditable access boundary exist,
  the maximum outcome is an internally consistent theoretical clock packet below
  empirical L4, unless a hardware/data programme is separately authorized.

This check should happen before, not after, one parent is frozen.

## 10. Recommended model-neutral gate set

A future authorized pin should replace the old L0--L7 scalar ladder with at
least these independent coordinates:

1. `ONE-PARENT-PRIMITIVE-LAW`
2. `COMPLETE-CLASSICAL-CLOCK-RECORD`
3. `OPERATIONAL-CLOCK-INFORMATIVENESS`
4. `HELDOUT-CLOCK-ADEQUACY`
5. `SELF-TIMING-AUTONOMY`
6. `COMPLETION-PASSIVE-READOUT`
7. `CONSTRAINED-AUTONOMOUS-ROUTE-CONSISTENCY`
8. `GAUGE-ORBIT-DESCENT`
9. `RELATIONAL-SCREENING`
10. `EXTERNAL-TRIGGER/INTERNAL-TRIGGER-EQUIVALENCE`
11. `RESOURCE-AND-RECIPROCAL-DISTURBANCE`
12. `SECOND-CLOCK-SEPARATE-ADEQUACY`
13. `JOINT-CLOCK-COMPARISON`
14. `COMPLETE-CLOCK-SWITCH-MAPS`
15. `REPRESENTATION-NONSELECTION`

Native Barandes endpoint lift, native actuality, chronology, proper time,
spacetime, metric, gravity, discreteness, and new physics remain separate closed
coordinates.

## 11. Honest maximum claim after a future successful construction

The strongest physically supportable operational claim would be:

> On one frozen laboratory domain, one parent physical packet produces a typed
> retained clock record that carries independently validated information about
> a physical reference time, operates without unrepresented time-indexed
> control over its registered run, predicts held-out clock and system
> transcripts, and renders the registered system predictions conditionally
> independent of the external reference reading once its internal record is
> known. Any separately earned second-clock and clock-switch results are
> reported as additional coordinates.

This would be meaningful progress toward relational time. It would not yet be a
theory of time, chronology, spacetime, or gravity.

## 12. Primary-source anchors and scope

- Woods, Silva, Putz, Stupar, Renner,
  *Quantum clocks are more precise than classical ones*,
  https://arxiv.org/abs/1806.00491 — information-bearing clock task and finite
  accuracy/resource scaling; not relational-time emergence.
- Silva, Nurgalieva, Wilming, *Ticking clocks in quantum theory*,
  https://arxiv.org/abs/2306.01829 — independence principle, classical tick
  degree of freedom, self-timing, clockwork independence, and multi-clock tick
  sequences; not a clock-neutral constrained parent.
- Woods, *Autonomous Ticking Clocks from Axiomatic Principles*,
  https://arxiv.org/abs/2005.04628 — autonomous ticking-clock channels,
  time-independent local dilation with environment, and external-timing
  distinction; not external-time elimination.
- Woods, Silva, Oppenheim,
  *Autonomous quantum machines and the finite sized Quasi-Ideal clock*,
  https://arxiv.org/abs/1607.04591 — fixed autonomous control with finite
  energy/dimension/backreaction; not passive-readout or ontology selection.
- Erker et al.,
  *Autonomous quantum clocks: does thermodynamics limit our ability to measure
  time?*, https://arxiv.org/abs/1609.06704 — autonomous ticking and
  accuracy-resolution-entropy costs; not clock-neutral relational dynamics.
- Hoehn, Smith, Lock, *The Trinity of Relational Quantum Dynamics*,
  https://arxiv.org/abs/1912.00033, and the relativistic extension
  https://arxiv.org/abs/2007.00580 — equivalence of constrained relational,
  Page--Wootters, and deparametrized descriptions under hypotheses; not
  empirical clock adequacy or unique ontology.
- Hoehn, Vanrietvelde, *How to switch between relational quantum clocks*,
  https://arxiv.org/abs/1810.04153 — multiple-clock switching through a
  clock-neutral theory and multiple-choice limitations; not a reason to make
  two-clock comparison prerequisite to every single-clock claim.
- Chataignier et al., *Relational Dynamics with Periodic Clocks*,
  https://arxiv.org/abs/2409.06479 — local-cycle validity and the failure of a
  winding counter to manufacture global invariance.
- Hausmann, Schmidhuber, Castro-Ruiz,
  *Measurement events relative to temporal quantum reference frames*,
  https://arxiv.org/abs/2308.10967 — operational inequivalence of measurement
  constructions for finite nonideal clocks and possible time-nonlocality; a
  warning against identifying postselection with physical triggering.
- Głowacki, *Operational Quantum Frames*,
  https://arxiv.org/abs/2304.07021 — operational frame as physical system plus
  covariant POVM and complete operational equivalence; not a time ontology.
- Rankovic, Liang, Renner,
  *Quantum clocks and their synchronisation — the Alternate Ticks Game*,
  https://arxiv.org/abs/1506.01373 — two-clock synchronization as an independent
  operational task.
- Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
  https://arxiv.org/abs/2507.21192 — Hilbert representation may be secondary to
  a configuration-space stochastic ontology; it does not provide this unit's
  native clock, chronology, or gravity law.

## 13. Authorization boundary

No corrected pin should be frozen from this memo automatically. A future user
authorization would need to name one bounded successor pin incorporating the
object split, product outcome, and exact gate set above; authorize fresh
pre-construction review; and state whether existing sequestered data may be
used. Model selection must remain barred until that revised pin passes.
