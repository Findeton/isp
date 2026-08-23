# Paper 04 pre-construction pin-audit adjudication

## Relational clocks and the operational redundancy of external time

Date: 2026-08-23

Status: **TERMINAL PRE-CONSTRUCTION ADJUDICATION**

Disposition:

```text
ACCEPT-MATHEMATICAL-BOUNDARY-WITH-BINDING-SCOPE
MODEL-SPECIFIC-PREFIT-FREEZE-REQUIRED-BEFORE-CONSTRUCTION
```

First decisive semantic blocker in the frozen experiment: **none**

Paper-04 scientific coordinate awarded: **none**

Clock-neutral parent constructed: **no**

External parameter shown redundant: **no**

Fundamental status of time selected: **no**

Paper 05, spacetime, and gravity: **closed**

## 0. Exact authority and decision rule

This adjudication authenticates and binds the following exact corpus.

| Artifact | Ordinary SHA-256 | Normalized self-SHA-256 | Exact size |
|---|---|---|---:|
| `v17/note-paper04-relational-clock-external-time-pin.md` | `da48bc95bf02c93393697ad6b447605ab89879ff45a1be6896abf6ce6a276b0c` | `6b903e20eb0507ed1f8d1b6fa1a9ca2378b0994ca108b16a9c0ccbd7220493bf` | 1,016 LF / 45,152 bytes |
| `v17/note-paper04-pin-audit-mathematics.md` | `2151bee5c6ac9b93f315047f2164c995a7fdbc6726a431ebd992814071d0d204` | `25d075f1c1e9da4a0c667fc1ed19c218951ac325802907827e7b51768e2227e5` | 837 LF / 41,302 bytes |
| `v17/note-paper04-pin-audit-quantum-clocks.md` | `3440dd49b51ae8245070c23963c7a51fc43fe5c02a5c54d4308b4cefd71ec8f2` | `b5e27c123ab2d9fcae88a55329bbeaec4efa42fe7286b0b1407572ea659b3a18` | 825 LF / 52,916 bytes |
| `v17/note-paper04-pin-audit-ontology-relativity.md` | `76c2a5d412f56b031ff4e0bbce87a22f9c7ea65a4fe24f62289fbcc12be6defd` | `d340016a701be6b1c1353124e7c2445a5c206ade1f492ecba7283b8bc874c198` | 916 LF / 59,146 bytes |

The adjudicator read the complete pin and all three reports. Matching verdicts
are not votes. Every ruling below follows from an independent reconstruction
of the mathematical and physical issue.

No candidate clock, Hamiltonian, state, constraint, parent law, calibration,
numerical result, or implementation was inspected or selected while making
this decision.

## 1. Root decision

The frozen Paper-04 experiment is coherent and worth running. It asks a real
physical question:

> Can complete laboratory predictions currently indexed by an external scalar
> parameter instead be obtained from records of two physical clocks that are
> themselves parts of one common clock-neutral process?

The pin correctly distinguishes five progressively stronger claims:

1. a clock is correlated with an external schedule;
2. clock-conditioned predictions are operationally adequate;
3. two physical clocks define compatible local temporal frames;
4. laboratory and clock-relative descriptions reduce from one parent without
   consuming the external parameter on held-out predictions; and
5. time is absent from fundamental reality.

None of these implications is automatic. In particular, item 4 would not
establish item 5. The supplied Paper-03 causal frontier also remains supplied;
clock records cannot derive its arrows.

The exact pin is therefore accepted as a mathematical boundary, with every
binding condition in Section 3. The acceptance authorizes only the next
pre-fit freeze. It does not authorize choosing a parent and evaluating it in
one inseparable step.

## 2. Independent reconstruction of the decisive issues

### R1 — one joint law does not imply the displayed clock-change mixture

Let $A$ and $B$ be independent fair bits and let the complete reader be
$R=A$. Then

$$
P(R=1\mid A=1)=1,
$$

while, for either value of $B$,

$$
P(R=1\mid B=b)=\frac12.
$$

Consequently,

$$
\sum_b P(R=1\mid B=b)P(B=b\mid A=1)=\frac12,
$$

not $1$. All probabilities belong to one normalized, full-support joint law.
The missing premise is conditional sufficiency, such as

$$
R\mathrel{\perp\!\!\!\perp} A\mid(B,u),
$$

or a stronger complete state-valued reduction theorem. Therefore a common
parent is necessary but not sufficient for a scalar stochastic change of
clock. If sufficiency fails, the honest output is a lossy or clock-dependent
frame map retaining the residual memory.

### R2 — two calibration points make affine agreement tautological

Any two distinct ordered reading pairs determine one affine map
$\tau_B=a\tau_A+b$. Exact agreement on only those two pairs tests neither
affine form nor predictive stability. A positive coordinate therefore needs
at least one separated held-out reading region, or another explicitly
overidentifying statistic, after $a,b$ are frozen.

### R3 — an empty temporal task makes every clock look adequate

If all registered system readers are constant and every system operation is
the identity, predictions are independent of the external parameter even for
an unrelated random clock. Paper 04 must include a predeclared reader whose
law differs across at least two comparator values and a sequential or adaptive
context not fixed by one-time marginals.

### R4 — a nonzero coupling need not be physical backreaction

For $V=cI$, or for an admitted source class entirely inside one eigenspace of
$V$, removing $V$ changes at most a global phase and changes no registered
reader. Operator norm and a nonzero coefficient do not establish interaction.
Backreaction is earned only when removing the frozen coupling changes
predeclared system responses under clock interventions and clock responses
under system interventions, with no retuning.

### R5 — identity-only covariance is vacuous

Every model is covariant under the singleton registry $\{\mathrm{id}\}$,
including a model that hard-codes one numerical clock coordinate. Coordinate
16 requires at least one nonidentity orientation-preserving Borel reading
isomorphism, preferably including a nonlinear monotone map on the good-clock
window, with the entire physical interface pushed forward.

### R6 — equal POVMs do not determine equal clock processes

A Lüders readout and a measure-and-reset readout can have the same clock POVM
effects and different posterior states. Their first-reading probabilities
agree, while repeated readings and clock-controlled continuations differ.
Calibration must bind the complete instrument, retained record, disturbance,
posterior, and future contexts—not only the effects.

### R7 — one-time equality does not determine a temporal process

Two binary two-step histories can have identical fair marginals at both steps
while obeying respectively $t_2=t_1$ and $t_2=1-t_1$. A retained equality
reader distinguishes them. The construction must test complete sequential and
adaptive histories and may not Markovize equal current readings.

### R8 — a periodic phase plus an appended orbit index is not a clock theorem

Appending a mathematical winding number to a recurrent phase makes the pair
injective only by importing path position. A valid cycle record must be made
by a physical subsystem inside the parent, remain gauge valid, and pay its
resource and disturbance costs. It then defines a larger reference system,
not a repaired version of the original phase alone.

### R9 — a history-state wrapper can reproduce without explain

Given a complete target family $U(s)$, one can form a history state whose
clock-conditioned components are $U(s)|\psi\rangle$ and construct a constraint
that annihilates it. Exact recovery then follows because the target dynamics
was inserted before the test. This earns a formal parametrization theorem,
not an independently motivated clock-neutral law or elimination of physical
time.

### R10 — removing a runtime argument does not remove hidden time

An allegedly autonomous source may encode the external schedule in its state
preparation, controller phase, factorization, lookup table, winding record,
or generator bytes. The held-out predictor must be audited by physical
dependency, not variable names. A bound gauge-integration parameter is not an
external input; a value supplied to switch a physical coupling is.

### R11 — record, division, occurrence, and causal arrow remain distinct

A durable clock record can omit future-relevant apparatus memory and therefore
fail to be a complete division. A complete reset may yield a future-sufficient
division without producing any clock record. Neither fact selects an actual
history. Increasing readings may track but cannot derive the supplied causal
frontier. All four record/division combinations must survive.

### R12 — operational redundancy cannot select a timeless ontology

Tensoring a successful parent with an operationally idle temporal sector
leaves every registered reduction and reader unchanged. Thus even complete
operational redundancy on the declared domain would not prove uniqueness of
the parent or absence of fundamental time. It would prove only that the
external scalar is unnecessary for those predictions.

## 3. Binding construction conditions

The following conditions are mandatory and noncompensatory.

### B1 — physical clock packets

Each clock must have a distinct physical subsystem lineage, preparation,
total dynamics, coupling, normalized instrument, posterior, retained record,
calibration window, resource ledger, and complete readers. Two displays of
one hidden oscillator count as one clock unless independent clock dynamics is
proved.

### B2 — one experiment and one parent

Both clocks, the system, controllers, interactions, memories, and records must
belong to one normalized joint law or one physical-inner-product-complete
parent. Separate fitted tables or clock-indexed system laws fail.

### B3 — complete sequential semantics

Every positive claim quantifies over the registered finite sequential and
adaptive contexts, including readout disturbance, retained memory, guards,
ancillas, and complete future readers. One-time conditional states are
insufficient.

### B4 — informative frozen comparator

Before model evaluation, freeze at least one time-sensitive complete reader,
one nontrivial sequential/adaptive task, an informative error metric and
tolerance, a mistuned/no-clock baseline, and disjoint calibration and
held-out contexts.

### B5 — overidentified same-path calibration

Fit units and origin on one supplied path and one predeclared good-clock
window. Test on at least one further positive-support region not used to fit
$a,b$. Different-path proper-time effects remain physical comparator input.

### B6 — sufficiency or full parent transport

The scalar clock-change mixture is awarded only after a complete-reader
conditional-sufficiency or Blackwell-garbling theorem. Otherwise transform
the full parent state, residual memory, records, instruments, observables, and
readers, and print exact loss or clock-choice dependence.

### B7 — physical normalization

A constrained route must construct its solution space, rigging or
group-averaging map where needed, physical null quotient, physical inner
product, clock POVMs, and reduction maps. A kinematic norm or formal
$\delta(\widehat C)$ is not a probability model.

### B8 — nonvacuous reparameterization

Freeze and execute at least one nonidentity orientation-preserving Borel
reading-coordinate bijection on positive support. Push forward the instrument,
record, marginal/reference measure and null class, calibration, conditionals,
and every dependent reader. A noninjective map is physical coarse-graining,
not gauge.

### B9 — deep hidden-time exclusion

Trace held-out probabilities to state preparation, parent law, constraint,
factorization, controller, clock records, and reduction maps. No external
schedule, slot rank, source order, run counter, target label, hidden winding,
or schedule-derived model bytes may enter. Bound integration variables over
gauge orbits are permitted when no value is supplied to the predictor.

### B10 — finite resources and recurrent domains

Print dimension, energy bandwidth and origin, coherence, resolution,
recurrence window, runtime, success/failure probability, preparation/readout
cost, physical cycle memory, and stopped-clock domains at the theorem level
used. Scaling a Hamiltonian without paying energy is not improvement.

### B11 — operationally detectable bidirectional interaction

At least one frozen interaction or readout disturbance must change
predeclared clock and system readers in both intervention directions. Global
phase, $cI$, restricted inert sectors, manual reset, and post-hoc retuning do
not pass.

### B12 — multiple-choice honesty

If two admissible physical clocks yield inequivalent complete reduced
dynamics, report that dependence. No clock-indexed law change or incomplete
reader family may convert it into equivalence.

### B13 — periodic and stopped-clock honesty

Recurring readings support only local or mixture-valued descriptions unless
a physical enlarged reference stores cycle information. Clock stoppage ends
the clock's certified domain, not physical change.

### B14 — formal-wrapper classification

A parent, factorization, constraint, or controller selected after the complete
target dynamics is known is capped at
`P04-FORMAL-PARAMETRIZATION-REPRESENTATION`, even if its reductions are exact
and its final notation contains no external parameter.

### B15 — pre-fit lineage freeze

The concrete parent state/law, factorization, clocks, interactions,
controllers, clock instruments, reduction maps, resource conventions,
calibration regions, fitting variables, held-out contexts, error functional,
tolerance, and allowed reparameterizations must freeze before any derivation,
fit, or evaluation of their Paper-04 performance.

### B16 — supplied-order and geometry firewall

Paper-03 causal order, time orientation, worldlines, same-path labels,
Lorentzian metric, AQFT net, and comparator proper times remain supplied. A
clock result cannot derive chronology, dimension, geometry, or gravity.

### B17 — ontology and actuality firewall

No stationary state, positive history law, constrained parent, clock frame,
or parameter-free predictor selects a unique microontology, one actual
history, a fundamental clock, or the fundamental presence/absence of time.

### B18 — no implementation substitution

Symbolic or numerical tools may verify a frozen construction. Runtime,
serialization, or code architecture cannot define a clock, select a parent,
repair a failed theorem, or retune any physical object.

## 4. Target, control, attack, and product ruling

All 25 targets are coherent under B1--B18. All 42 paired controls have two
typed and scientifically distinct arms. All 68 mandatory attacks change a
named physical or mathematical object and have an exact earliest affected
coordinate. The audits add 58 fresh countermodels; their substantive content
is covered by R1--R12 and B1--B18 without deleting their independent evidence.

The 28-coordinate product remains noncompensatory. Coordinates 1--22 are open
until a candidate is frozen, audited, reviewed, and terminally adjudicated.
Coordinates 23--28 remain binding refusals in every possible result:

```text
23 P04-CAUSAL-ORDER-STILL-SUPPLIED
24 P04-ONTOLOGY-SELECTION-UNCONSTRUCTED
25 P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED
26 P04-GRAVITY-UNCONSTRUCTED
27 P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED
28 P04-ACTUALIZATION-UNCONSTRUCTED
```

The earliest failed rung controls. Exact recovery of one-time marginals cannot
compensate for failed sequential semantics; a common parent cannot compensate
for hidden external time; and reparameterization covariance cannot compensate
for target-fitted parent selection.

## 5. Ruling on construction chronology

The generic pin deliberately froze the question before selecting a clock or
parent. The audits establish that those choices are physical and semantic,
not mere implementation details. B15 cannot be evidenced if model selection,
derivation, calibration, and evaluation are all first exposed in one completed
candidate.

The next authorized artifact is therefore exactly one model-specific,
result-neutral pre-fit construction pin. It must name:

1. the two clock algebras/subsystems and their physical independence witness;
2. their states, generators, interactions, instruments, and records;
3. the system and the one common clock-neutral parent;
4. the physical normalization and all reduction maps;
5. every controller and complete sequential/adaptive context;
6. the time-sensitive target readers and no-clock/mistuned controls;
7. training, calibration, and held-out regions;
8. the loss/error functional, threshold, and resource conventions;
9. the nonidentity reparameterization family;
10. all support, recurrence, stoppage, cycle, and sector domains;
11. the exact dependency graph and hidden-time mutant; and
12. which claims are formal controls versus promotion-bearing tests.

The model-specific pin must contain no fitted value, derived result, candidate
verdict, or evaluation output. Because it fixes the semantic objects omitted
from the generic experiment pin, it must receive independent constrained-
dynamics, quantum-clock, and ontology/relativity pre-construction audits.
Those audits are not an automatic repair cycle: they judge the first and only
model selection before the sole Paper-04 scientific construction.

Only if all three accept and root independently adjudicates that exact model
pin may one construction be frozen. Any later change to a clock, parent,
constraint, interaction, instrument, support, calibration, held-out test,
threshold, reparameterization family, or interpretation requires new user
authorization; no automatic v2/v3 repair chain exists.

## 6. Outcome and downstream walls

This adjudication awards no Paper-04 scientific rung. Its exact product is:

```text
P04-MATHEMATICAL-EXPERIMENT-BOUNDARY:
  ACCEPTED-WITH-BINDING-SCOPE

P04-MODEL-SPECIFIC-PARENT:
  UNCONSTRUCTED — ONE PREFIT PIN AUTHORIZED

P04-PHYSICAL-CLOCKS:
  UNCONSTRUCTED

P04-CLOCK-NEUTRAL-PARENT:
  UNCONSTRUCTED

P04-EXTERNAL-PARAMETER-STATUS:
  UNTESTED

P04-CAUSAL-ORDER:
  SUPPLIED

P04-ONTOLOGY-SELECTION:
  UNCONSTRUCTED

P04-SPACETIME-CHRONOLOGY:
  UNCONSTRUCTED

P04-GRAVITY:
  UNCONSTRUCTED

P04-FUNDAMENTAL-TIME-STATUS:
  UNSELECTED

P04-ACTUALIZATION:
  UNCONSTRUCTED
```

Paper 05 remains closed. A later terminal Paper-04 success would permit only
a separately frozen Paper-05 question; it would not authorize chronology,
spacetime, or gravity by itself.

## 7. Final disposition

The frozen experiment asks a physically meaningful, nontrivial question and
contains honest failure outcomes. The three audits found no semantic
contradiction. Root independently confirms the decisive probability,
calibration, instrument, resource, hidden-time, ontology, and relativity
boundaries.

Final disposition:

```text
ACCEPT-MATHEMATICAL-BOUNDARY-WITH-BINDING-SCOPE
MODEL-SPECIFIC-PREFIT-FREEZE-REQUIRED-BEFORE-CONSTRUCTION
```

First decisive semantic blocker: **none**.

Scientific result awarded: **none**.

## 8. Authentication

Adjudication LF line count: `000465`

Adjudication byte count: `019476`

Adjudication ordinary SHA-256: reported externally after final bytes freeze;
embedding an ordinary self-hash would be circular.

Adjudication normalized self-SHA-256:
`88b74315e541694ddc8361939aa9320186503b9f32a2b72709ca51f097f3015b`

Normalization rule: replace the six decimal digits on each count line and the
64 hexadecimal characters on the normalized-self line by ASCII zeroes,
preserve every other byte, and compute SHA-256. The file must use LF endings,
end in one LF, and contain no trailing horizontal whitespace.
