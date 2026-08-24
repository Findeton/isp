# ISP v17 — temporal sufficiency, Markov enlargement, law form, and external-time assumption audit

**Status:** ACTIVE AUTHOR-SIDE FOUNDATIONAL AUDIT / RESULT-NEUTRAL / NOT A PIN / NOT REVIEWED

**Date:** 2026-08-24

**Scientific result awarded:** none

**Unit, construction, review, or successor authority created:** none

---

## 0. Question and disposition

This audit investigates four assumptions from the foundational
assumption-deletion programme:

1. **N1:** physical law is propagation of a sufficient instantaneous state;
2. **N2:** a non-Markovian law is physically a hidden-Markov law on an
   enlarged carrier;
3. **N3:** a fundamental law is an initial condition plus a forward equation;
4. **N4:** time is an external real parameter.

The strongest current conclusion is not that these assumptions are false.
It is that they contain several different claims whose implications run in
only one direction:

$$
\boxed{
\begin{gathered}
\text{physical sufficient state}
\Longrightarrow
\text{Markov representation},\\[2mm]
\text{Markov representation}
\not\Longrightarrow
\text{physical sufficient state};\\[2mm]
\text{source-complete forward law}
\Longrightarrow
\text{forward factorization},\\[2mm]
\text{forward factorization}
\not\Longrightarrow
\text{source-complete forward law};\\[2mm]
\text{operationally adequate physical clock}
\Longrightarrow
\text{relational time coordinate},\\[2mm]
\text{relational time coordinate}
\not\Longrightarrow
\text{operationally adequate physical clock}.
\end{gathered}}
\tag{1}
$$

The reverse implications fail because a mathematical representation can be
built from the complete target law, while a physical carrier must be fixed,
prepared, manipulated, read, and resource-accounted independently of the
answer it is supposed to explain.

The immediate research target is therefore not “eliminate states” or
“eliminate time.” It is:

> Determine whether a candidate temporal boundary carries an independently
> evidenced physical object that screens every licensed past intervention
> from every licensed future response, and determine whether an internal
> record can replace a nontrivially operative external timing input without
> importing that timing through preparation, control, completion, or readout.

The audit constructs no candidate ontology and chooses no answer among an
ordinary-positive boundary state, a noncommutative boundary object, a growing
history, a scale-dependent interface, or a genuinely indivisible whole law.

---

## 1. Scope and objects inspected

The repository objects directly reconstructed for this audit are:

1. `v17/note-foundational-assumption-deletion-programme.md`;
2. `v17/research-incubator/active/qcut/` author-side Q-Cut theorem and
   readiness package;
3. `v17/research-incubator/active/ugen/`
   `v17_ugen_u0_t3_history_markovization_and_physical_closure_theorems.md`;
4. the U0 Barandes source-completion and Markovian-embedding scope audits;
5. the terminal Paper 04 hostile-review adjudication; and
6. the terminal Paper 04B pre-construction pin-review adjudication.

The Q-Cut package is an unreviewed author theorem candidate. It is used here
only as a conditional pressure test. Paper 04 is terminal
`REJECT-WITH-EXACT-SALVAGE`; Paper 04B is terminal
`REVISE-BEFORE-MODEL-SELECTION`. Neither supplies an accepted fundamental
clock.

New literature claims in this file are limited to the primary scholarly
sources listed in Section 15. Their existence demonstrates mathematical or
experimental possibilities inside stated domains. It does not select a
fundamental ontology.

---

## 2. Typed temporal-boundary vocabulary

Let a complete registered experiment be divided at an operational seam
$\Sigma$ into a past laboratory region $E_-$ and a future laboratory region
$E_+$. The seam is identified by physical operations and retained records,
not merely by an integer in a program or by a coordinate value $t$.

Let:

- $H_-$ be the registered past transcript;
- $\Pi_+$ be the licensed set of future adaptive intervention policies;
- $F$ be any event in a measure-determining future reader family; and
- $C_\Sigma$ be a proposed boundary carrier.

### Definition 2.1 — statistical future sufficiency

$C_\Sigma$ is statistically future sufficient on the registered experiment
when

$$
P(F\mid H_-,C_\Sigma,\operatorname{do}(\pi))
=
P(F\mid C_\Sigma,\operatorname{do}(\pi))
\tag{2}
$$

for every licensed $\pi\in\Pi_+$ and every positive-support conditioning
event.

This is an operational conditional-independence statement. It is not yet an
ontology claim.

### Definition 2.2 — source closure

$C_\Sigma$ is source-closed at the tested scope only when every independently
evidenced memory, reference, retained record, environment channel, common
cause, communication port, and controller capable of affecting the future is
included, or its influence is excluded by a registered intervention or
isolation control.

### Definition 2.3 — independently physical boundary carrier

$C_\Sigma$ is independently physical only if its identity and physical type
are fixed without consuming the held-out complete process and if the claimed
carrier has an appropriate combination of:

1. preparation or occurrence conditions;
2. intervention response;
3. a typed reader or stable record;
4. re-preparation or causal-break meaning where division is claimed;
5. stability over the licensed future grammar; and
6. explicit information, precision, energy, space, time, and law-description
   costs at the claimed scope.

### Definition 2.4 — licensed physical temporal division

$\Sigma$ is a licensed physical temporal division only if $C_\Sigma$ is
source-closed, independently physical, future sufficient, and supports the
claimed restart or re-preparation intervention.

These definitions deliberately leave open the carrier's mathematical type.
An ordinary random variable is one possibility, not a default.

---

## 3. The central distinction: history Markovization is not physical state discovery

For a finite prefix-causal controlled transcript law,

$$
P_{c_{0:T-1}}(r_{0:T}),
$$

define the full observed prefix

$$
H_t=(c_{0:t-1},r_{0:t}).
\tag{3}
$$

On positive-support histories, the conditional ratios

$$
K_t(r_{t+1}\mid H_t,c_t)
=
\frac{
P(r_{0:t+1}\mid c_{0:t})
}{
P(r_{0:t}\mid c_{0:t-1})
}
\tag{4}
$$

give an exact Markov representation on the ever-growing history state. The
product telescopes to the supplied complete law. A predictive equivalence
relation can then quotient histories that have identical continuations under
every licensed future policy.

These are exact mathematical facts. Their dependency direction is

$$
\boxed{
\text{complete target process}
\longrightarrow
\text{history state or predictive quotient}.}
\tag{5}
$$

They do not reverse to

$$
\text{independently specified physical state}
\longrightarrow
\text{held-out complete process}.
\tag{6}
$$

Three reasons are decisive.

1. Equation (4) consumes the complete process that the representation is
   supposed to explain.
2. The full-history state grows with the transcript and is not thereby an
   object stored at the cut by nature.
3. The predictive quotient depends on the complete future policy class and
   target conditionals. Minimality as a predictor does not make it ontic.

Appending an unobserved independent process $J_t$ gives another equally good
realizer $(H_t,J_t)$. Thus even exact prediction does not select one enlarged
carrier as reality.

The same distinction governs the Barandes-facing question. Barandes's
indivisible-law programme gives a serious reason not to identify an
ordinary-positive stochastic description with a divisible instantaneous-state
law. Its Hilbert lift is downstream of supplied configuration, time, contingent
state, and transition data. A Hilbert or Markovian embedding does not select
the underlying law, complete its intervention fiber, or make its auxiliary
coordinates physical.

---

## 4. Exact control C1: identical one-step dynamics, different complete process

Let $R_0,R_1,R_2\in\{0,1\}$.

### Process I — independent bits

$$
P_{\rm iid}(r_0,r_1,r_2)=\frac18
\tag{7}
$$

for all eight triples.

### Process P — even parity

$$
P_{\rm par}(r_0,r_1,r_2)=
\begin{cases}
\frac14,&r_0\oplus r_1\oplus r_2=0,\\
0,&\text{otherwise}.
\end{cases}
\tag{8}
$$

Both processes have

$$
P(R_0=0)=P(R_0=1)=\frac12,
\tag{9}
$$

and the same adjacent one-step kernels,

$$
P(R_1=b\mid R_0=a)=\frac12,
\qquad
P(R_2=c\mid R_1=b)=\frac12.
\tag{10}
$$

Yet in the parity process,

$$
R_2=R_0\oplus R_1
\tag{11}
$$

with certainty, whereas in the independent process every triple occurs.

This one control proves three scoped statements.

1. Initial distribution plus adjacent one-step transition matrices does not
   determine the complete process.
2. The latest observed variable $R_1$ is not sufficient for the parity
   future, while $(R_0,R_1)$ is.
3. A full-history forward factorization of the parity law remains possible,
   but its later kernel was built from the complete parity answer.

The control does not prove that nature lacks a deeper instantaneous state.
It proves that the observed endpoint and its first-order transition law do not
identify one.

---

## 5. Exact control C2: independently evidenced memory versus formal memory

Let a physical memory bit $M$ be fair. Define

$$
R_0=M.
\tag{12}
$$

At the middle cut perform a complete system causal break and reprepare

$$
\operatorname{do}(R_1=0).
\tag{13}
$$

Let the final device read the memory,

$$
R_2=M.
\tag{14}
$$

Then

$$
P(R_2=R_0\mid\operatorname{do}(R_1=0))=1.
\tag{15}
$$

The system-only carrier fails the operational Markov condition. The joint
carrier $(R,M)$ is an ordinary-positive sufficient state.

This enlargement is physically warranted only if $M$ is independently
identified. A decisive control grammar is:

1. **read:** a reader reports $M$ at the cut with calibrated error;
2. **toggle:** $\operatorname{do}(M\mapsto1-M)$ changes the final relation to

   $$
   P(R_2=1-R_0)=1;
   \tag{16}
   $$

3. **erase/randomize:** a licensed eraser replaces $M$ by an independent fair
   bit, yielding

   $$
   P(R_2=R_0)=\frac12;
   \tag{17}
   $$

4. **isolate:** blocking the memory channel removes the residual dependence.

When these consequences occur, the hidden-Markov enlargement has physical
content. When no $M$ is independently evidenced, adding the full transcript
as “memory” only renames the mathematical history representation.

The correct outcome in that second case is **interface nondivision**, not
“no hidden dilation exists.”

---

## 6. Exact control C3: a physical cut is an information and intervention claim

The active Q-Cut package studies an ordinary-positive cut variable $\Lambda$
that screens preparation $X$ from all later readers in a scalable partial
matching task. Conditional on its unreviewed theorem candidate and fixed
hard input ensemble, any admitted standard-Borel positive cut obeys

$$
I(X:\Lambda\mid S)
=
\Omega(\sqrt n),
\tag{18}
$$

while the registered quantum comparator has $O(\log n)$ log-dimension and
preparation information.

The important assumption-level meaning is:

$$
\boxed{
\begin{aligned}
&\text{large ordinary-positive cut information}\
&\quad\lor\ \text{failure of positive cut sufficiency}\
&\quad\lor\ \text{future dependence, input correlation, or another charged
premise}.
\end{aligned}}
\tag{19}
$$

This closes the “one exact real is a small state” rhetorical escape at the
mutual-information coordinate. It does not show that a physical memory device
requires the same number of bits, the same energy, or the same volume. It does
not apply to a noncommutative cut or a genuinely indivisible whole law.

Q-Cut is therefore a high-value pressure test on N1, not an answer to N1.
It requires independent review before use as an ISP result.

---

## 7. Necessity record N1 — sufficient instantaneous state

### N1 record

| Field | Frozen author-side content |
|---|---|
| $S$ — statement | Every complete physical experiment admits, at each relevant temporal cut, an independently physical carrier $C_\Sigma$ such that all future intervention-conditioned records are screened from the registered past by the present value of $C_\Sigma$. |
| $D$ — domain | Complete controlled processes with a declared past/future seam, measure-determining readers, explicit adaptive intervention grammar, positive-support conditionals, and source-closure accounting. “Instantaneous” has no meaning outside a supplied or operationally constructed cut. |
| $T$ — status | Ontology postulate when asserted universally; empirical regularity when asserted for a bounded apparatus; theorem only after a specific carrier and screening relation are proved. |
| $R$ — referent | The material information-bearing object at the seam, including every reference, memory, record, environment channel, and controller that can affect future observations. |
| $\Delta$ — deletion | Retain normalized complete laws and prefix causality, but do not assume any proper ordinary-positive carrier screens past from future. Permit growing-history, noncommutative, scale-dependent, regional, or whole-process interfaces. |
| $K$ — recovery | Complete adaptive record laws; causal-break behavior; stable records; quantum interference and contextual composition; source-to-record fixed-background baseline; no-signalling at its correct operational scope; eventually QFT and reciprocal gravity limits. |
| $C$ — costs | Full-history growth, target-built sufficient statistic, inaccessible precision, noncommutative boundary algebra, future-program dependence, preferred cut, missing memory/reference, law-description size, reader compilation, energy and stability. |
| $O$ — outcomes | `COMPACT-PHYSICAL-STATE-SUPPORTED`; `GROWING/RESOURCE-HEAVY-STATE`; `NONCOMMUTATIVE-BOUNDARY`; `SCALE-DEPENDENT-SUFFICIENCY`; `INTERFACE-NONDIVISION`; `WHOLE-PROCESS-LIVE`; `UNDERDETERMINED`. |

### What is already known

1. Full-history Markovization and a minimal predictive quotient exist for
   every finite prefix-causal controlled transcript law.
2. Those constructions consume the complete process and therefore do not
   discover a physical state.
3. The latest observed endpoint need not be sufficient, as C1 proves.
4. Process-tensor theory supplies a complete operational multi-time object
   relative to interventions; a sequence of state-to-state maps is not in
   general complete.
5. Quantum Markov order can depend on the instrument sequence. Taranto *et
   al.* prove that a non-Markovian quantum process cannot have finite Markov
   order with respect to all possible instruments.
6. Q-Cut conditionally lower-bounds the retained information of one class of
   ordinary-positive sufficient boundaries.

### What remains open

1. Whether realistic closed experiments possess a compact independently
   physical temporal boundary object.
2. Whether that object is ordinary-positive, noncommutative, or only
   effective.
3. Whether source-closed causal breaks exist at the required precision.
4. Whether a boundary remains sufficient across a held-out intervention
   family rather than only the performed program.
5. Whether the resource cost scales like a compact law or a hidden answer
   table.

### Smallest honest deletion test

Fix one experimentally identified cut and one candidate carrier. Preserve the
same source, apparatus, reader family, and laboratory order. Add only:

1. a complete causal break on the proposed system state;
2. independently addressable interventions on each evidenced memory/reference;
3. erasure and isolation controls;
4. future policies withheld from carrier calibration; and
5. complete null/failure records.

Test Equation (2). Failure earns interface nondivision at this scope. Success
earns a scoped physical sufficient boundary, not a universal ontology.

---

## 8. Necessity record N2 — physical hidden-Markov enlargement

### N2 record

| Field | Frozen author-side content |
|---|---|
| $S$ — statement | Whenever observed dynamics is non-Markovian, there exists an enlarged, physically real state $Z_t=(X_t,M_t)$ whose present value is sufficient and whose transition law is Markovian. |
| $D$ — domain | A declared observed system, licensed interventions and readers, a candidate memory/environment boundary, and an exact or tolerance-bounded operational Markov criterion. The horizon and allowed carrier class must be printed. |
| $T$ — status | Mathematical representation theorem when $M_t$ is the full past; ontology postulate when $M_t$ is asserted physical; empirical hypothesis when $M_t$ is independently manipulated and read. |
| $R$ — referent | A material memory, environment, reference, field, conserved sector, or other carrier that survives the system causal break and influences future records. |
| $\Delta$ — deletion | Permit non-Markovian complete laws without asserting that any target-independent, source-closed physical enlargement exists. Retain formal Markovization as representation only. |
| $K$ — recovery | Same complete intervention-conditioned records; correct response to memory toggles, erasers, isolation, and re-preparation; transfer to held-out programs; no answer import into the enlarged state. |
| $C$ — costs | Memory dimension and growth, preparation, precision, access, intervention energy, environment expansion, idle-variable ambiguity, hidden future setting, target-built transition table, and nonunique realizer choice. |
| $O$ — outcomes | `EVIDENCED-HIDDEN-MARKOV-CARRIER`; `PARTIAL-MEMORY-ENLARGEMENT`; `TARGET-BUILT-MARKOVIZATION-ONLY`; `INTERFACE-NONDIVISION`; `NO-IN-CLASS-ENLARGEMENT`; `UNDERDETERMINED`. |

### What is already known

1. Every finite controlled transcript law is mathematically Markovian on its
   full history.
2. The minimal exact predictive quotient is also derived from the complete
   law and policy set.
3. A physically evidenced memory can make an apparently non-Markovian
   subsystem Markovian; C2 is the exact control.
4. An omitted physical memory and quantum interference nondivision are
   different mechanisms and must not be conflated.
5. In quantum process theory, memory length is generally instrument-relative,
   so “the physical memory state” cannot be inferred from passive correlation
   alone.

### What remains open

1. Whether one target-independent physical enlargement closes the complete
   process across incompatible interventions.
2. Whether the enlargement is finite, stationary, local, or accessible.
3. Whether the same enlargement works under system composition.
4. Whether an alleged memory is a physical referent or merely a state-space
   encoding of already known probabilities.

### Smallest honest deletion test

Use C2's grammar on an actual source-closed apparatus. A putative memory earns
physical status only when independently calibrated interventions on it change
future statistics as predicted and when its erasure removes the residual past
dependence. If no such variable is found, do not conclude that none can exist;
record interface nondivision and the searched carrier class.

---

## 9. Necessity record N3 — initial condition plus forward equation

### N3 record

| Field | Frozen author-side content |
|---|---|
| $S$ — statement | The fundamental nomology consists of an initial physical state and a forward evolution equation that uniquely generates every later complete process. |
| $D$ — domain | A supplied temporal orientation and foliation or slot order; a well-posed state space; boundary/constraint data; licensed interventions; and a criterion for uniqueness and physical admissibility. |
| $T$ — status | Successful law form in broad physical domains; modelling convention or representation when obtained by chain factorization; ontology postulate when asserted necessary for all reality. |
| $R$ — referent | The physically prepared initial condition, the lawfully generated later process, and the empirical arrow connecting interventions to future records. |
| $\Delta$ — deletion | Retain normalized complete predictions and operational prefix causality, but permit regional gluing, constraints, two-boundary ensembles, or whole-process laws without privileging an initial slice as fundamental. |
| $K$ — recovery | Ordinary laboratory prediction without future-setting access; adaptive interventions; no-backwards-signalling/prefix independence at the observed scope; conservation; standard initial-value limits where empirically valid; QFT and GR limits. |
| $C$ — costs | Final-boundary postselection, global normalization, future input, preferred foliation, boundary state, action or amplitude supplied by hand, nonlocal constraint solving, solution multiplicity, and hidden target law in full-history kernels. |
| $O$ — outcomes | `FORWARD-SOURCE-LAW-SUPPORTED`; `FORWARD-REPRESENTATION-ONLY`; `REGIONAL/CONSTRAINT-LAW-EQUIVALENT`; `WHOLE-PROCESS-PREDICTIVELY-DISTINCT`; `FUTURE-INPUT/POSTSELECTION`; `UNDERDETERMINED`. |

### What is already known

1. C1 proves that an initial marginal plus adjacent one-step transitions does
   not determine a complete three-time process.
2. Every finite ordered joint law can nevertheless be written as an initial
   distribution times full-history conditionals. This factorization is a
   representation theorem built from the target law.
3. A complete process tensor can encode all licensed intervention statistics
   without reducing them to a sequence of state-to-state maps. Its circuit
   slots and causal order remain supplied.
4. The general-boundary formulation associates state spaces to boundaries
   and amplitudes to arbitrary regions; standard temporal quantum mechanics
   is recovered as a special case. This proves formal room beyond a privileged
   initial/final pair, not that nature selects that formulation.
5. Aharonov, Bergmann, and Lebowitz construct time-symmetric ensembles using
   both initial and final selections. That is a valid conditional ensemble,
   not evidence that future postselection is a fundamental source law.

### What remains open

1. Whether a source-complete regional, constraint, or whole-process law can
   predict held-out complete experiments from less supplied structure than a
   source-complete forward law.
2. Whether any such alternative makes a physical prediction that cannot be
   removed by refactorizing the same joint law.
3. Whether operational prefix causality follows from an independently
   motivated whole-process principle rather than being imposed as a
   constraint.
4. Whether a temporal orientation is selected by boundary conditions,
   thermodynamic records, interventions, gravity, or another physical
   asymmetry rather than by the direction in which equations are written.
5. Whether regional gluing remains well defined for the complete interacting
   QFT and gravity experiment rather than only for a supplied formal model.

### The chain-rule trap

For every finite ordered positive law,

$$
P(r_{0:T}\mid c_{0:T-1})
=
P(r_0)
\prod_{t=0}^{T-1}
P(r_{t+1}\mid r_{0:t},c_{0:t}).
\tag{20}
$$

Equation (20) makes a forward description available after the complete joint
law is known. It does not show that a compact forward nomology generated the
joint law from weaker physical inputs. Conversely, writing a regional or
whole-process law does not by itself explain it; an imported action,
wavefunction, process matrix, or amplitude remains an imported answer.

### Operational prefix causality is not forward ontology

A whole-process law may obey

$$
P(r_{0:t}\mid c_{0:T-1})
=
P(r_{0:t}\mid c_{0:t-1})
\tag{21}
$$

without being fundamentally generated one slot at a time. Equation (21)
excludes dependence of registered prefixes on later freely chosen controls at
the tested interface. It does not select a metaphysical direction of
generation.

### Smallest honest deletion test

Do not compare verbal “forward” and “timeless” pictures. Require two fully
specified laws on the same complete experiment, with identical public inputs,
controls, readers, and resource ledger. Freeze them before held-out records.
If they induce identical complete laws, their law-form difference is
representational at that scope. If they differ, the held-out record selects
between them. A boundary-conditioned model that consumes the observed future
record is postselection, not prediction.

---

## 10. Necessity record N4 — external real time

### N4 record

| Field | Frozen author-side content |
|---|---|
| $S$ — statement | A real parameter $t$ external to the physical system is a fundamental independent variable of every physical law and supplies the order, duration, and rate used by all predictions. |
| $D$ — domain | Fixed-background dynamics or a constrained relational model with explicit clock/system split, constraint, clock observable or POVM, preparation, completion, readout, and comparison grammar. |
| $T$ — status | Exceedingly successful modelling structure in laboratory and field theory; external reference standard operationally; ontology postulate when claimed fundamental; gauge/coordinate label in some constrained formulations. |
| $R$ — referent | Physical clock readings, duration comparisons, ordering records, rates, recurrence, proper-time comparisons, and the controllers that prepare and interrogate them. |
| $\Delta$ — deletion | Replace one nontrivially operative external scalar in a frozen predictor family by records generated inside one physical parent, while retaining preparation, intervention, failure, resource, and complete-reader semantics. |
| $K$ — recovery | Held-out clock-task performance; nonvacuous duration/rate/phase/order inference; two-clock comparison; finite resolution and recurrence; interactions and backreaction; passive readout or represented completion; reparameterization maps; ordinary laboratory limit. |
| $C$ — costs | Supplied Hamiltonian/constraint, clock-system factorization, clock POVM, global state, ideal clock, recurrence, interaction, externally timed initialization or readout, scheduler, second clock, common reference, hidden slot index, and calibration. |
| $O$ — outcomes | `TASK-RELATIVE-DEPARAMETRIZATION`; `VALID-PHYSICAL-CLOCK-WITH-EXTERNAL-CONTEXT`; `HIDDEN-EXTERNAL-TIME`; `CONTROLLER-NOT-CLOCK`; `CLOCK-CHOICE/DOMAIN-DEPENDENT`; `NO-ADEQUATE-CLOCK`; `UNDERDETERMINED`. |

### What is already known: what Page--Wootters actually establishes

Page and Wootters show that a closed stationary quantum system can exhibit
relational subsystem dynamics through correlations with an internal clock.
Modern constrained-system work by Höhn, Smith, and Lock proves an equivalence
between relational Dirac observables, the Page--Wootters conditional-state
picture, and quantum deparametrization within its stated domain, including
nonideal clocks through covariant POVMs.

This is a substantial result. It blocks the claim that a globally evolving
Schrödinger state with an observable external time is the only way to express
quantum dynamics.

It does not begin without structure. A standard Page--Wootters construction
receives or chooses:

1. a physical Hilbert space and clock/rest decomposition;
2. a total constraint or Hamiltonian;
3. a physical state satisfying that constraint;
4. clock states or a covariant clock POVM;
5. a clock Hamiltonian or group action that orders those states;
6. a conditioning and normalization rule;
7. a physical reader and record interpretation; and
8. an experimental preparation, completion, and interrogation protocol.

Schematically,

$$
\rho_S(t)
=
\frac{
\operatorname{Tr}_C[(E_t\otimes I_S)\rho_{CS}]
}{
\operatorname{Tr}[(E_t\otimes I_S)\rho_{CS}]
}.
\tag{22}
$$

If the global constraint and clock covariance are chosen appropriately, the
conditional family obeys the desired relational dynamics. Equation (22)
shows how time dependence is encoded in correlations. It does not derive the
clock split, constraint, state, clock POVM, or physical source of the desired
dynamics.

### Interactions make relocation visible

Smith and Ahmadi show that when clock and system interact in the constraint,
the conditional state generally obeys a time-nonlocal Schrödinger equation
rather than the ordinary noninteracting form. This is evidence that clock
backreaction and the clock/system split matter physically. It is not a defect
of relational time; it prevents the ideal clock from being treated as a free
coordinate with no resource cost.

### Relational time can relocate supplied structure

A relational formalism merely relocates external time when any of the
following remains true:

1. the clock states are indexed by the same real parameter whose physical
   meaning is at issue, without an independent clock-task calibration;
2. the desired system Hamiltonian is supplied in the global constraint;
3. the clock/rest split is chosen after the target dynamics is known;
4. the clock record is created by an externally timed pulse;
5. a supplied laboratory slot number predicts the answer;
6. the readout time selects which conditional state is observed;
7. a second omitted clock schedules completion;
8. the “clock” is an arbitrary controller that predicts outputs but performs
   no timekeeping task.

None of these points refutes Page--Wootters. They identify the difference
between a relational representation of supplied quantum dynamics and the
physical derivation of a clock and its law.

### What remains open

1. Whether one physical parent can generate an operationally adequate clock
   record and the compared dynamics without an externally timed completion or
   readout channel.
2. Whether an informative external scalar can be removed nonvacuously across
   held-out tasks rather than merely relabeled by a clock-state index.
3. Whether two independently adequate finite clocks admit complete
   state/instrument/record transformations on their common domain.
4. Whether clock choice, interaction, finite resolution, and recurrence can
   be reconciled without importing a preferred clock or foliation.
5. Whether operational clock comparisons generate chronology or only measure
   relations inside an already ordered experiment.
6. How any surviving clock structure couples to a reciprocal dynamical metric
   without presupposing proper time or the gravitational source law.

### Smallest honest deletion test

Keep the same fixed-background reference predictor and delete only one
operative scalar input. Require one physical parent to produce an internal
record that replaces that scalar over preregistered held-out tasks. Preserve
the laboratory preparation and reader interface, expose every completion and
scheduling device, and refuse any claim when the scalar was dummy or when an
external pulse creates the record. Section 12 states the exact positive
criterion. Success is task-relative deparametrization, not a theorem that
fundamental time is absent.

---

## 11. What Paper 04 and Paper 04B already settled

### 11.1 Paper 04

Paper 04 constructed a genuine finite constrained quantum parent and an exact
B-relative finite clock packet. It failed as a complete two-clock result
because the proposed A transformation did not act on the accepted classical
record algebra while preserving the coherence used by the model. Keeping the
coherence required a quantum pointer; classicalizing it destroyed the same
coherence.

The physical lesson is:

> A quantum reference-frame coordinate map is not automatically a physical
> clock transformation with a retained outcome.

The accepted salvage retains a finite parent, B-relative packet, restricted A
state-coordinate map, and finite recurrence/rank controls. It does not derive
fundamental time, chronology, spacetime, or gravity.

### 11.2 Paper 04B

Paper 04B did not reach model construction. Its pre-construction gate was
revised because it lacked four model-independent predicates:

1. a controller could be called a clock without outperforming no-clock
   controls on a preregistered timekeeping task;
2. a dummy external scalar could be “removed” even when it never affected
   the reference predictor;
3. one adequate clock plus one independent time-insensitive device could be
   called two clocks; and
4. an externally timed pulse could create or stabilize the readout while the
   mechanism was called autonomous.

The exact repair obligations remain sound author-side guidance:

- **R1:** a positive operational clock-task predicate;
- **R2:** nonvacuous external-scalar replacement;
- **R3:** separate adequacy and joint independence for two clocks;
- **R4:** explicit autonomous completion versus passive readout.

No repaired pin or parent model is authorized by this audit.

---

## 12. Nonvacuous relational-time test

Let a reference predictor use a scalar $\tau$:

$$
P_{\rm ref}(y\mid x,\tau).
\tag{23}
$$

Removing the symbol $\tau$ is physically meaningful only if the reference
family depends nontrivially on it. Before seeing a candidate, freeze two
values and a measure-determining reader with

$$
\left\|
P_{\rm ref}(\cdot\mid x,\tau_1)
-
P_{\rm ref}(\cdot\mid x,\tau_2)
\right\|_{\rm TV}
\ge\epsilon_*>0.
\tag{24}
$$

A one-parent relational model must then produce an internal record $C$ without
receiving $\tau$ through a hidden channel and must predict the held-out family
through that record:

$$
P_{\rm parent}(y,C\mid x),
\qquad
P_{\rm parent}(y\mid x,C)
\simeq
P_{\rm ref}(y\mid x,\tau(C)).
\tag{25}
$$

At minimum, it must pass:

1. no-clock, frozen-clock, and mistuned-rate controls;
2. a clock-local intervention that changes the task response;
3. complete null, recurrence, aliasing, stoppage, and failure outputs;
4. a represented completion event or a nonzero passive-readout window over
   which the record law is stable;
5. an audit excluding slot number, cached schedule, source label, and hidden
   controller metadata;
6. finite held-out values not used to choose the clock map; and
7. eventually, a separately adequate second clock with independently
   addressable interventions.

Passing this test earns only:

```text
TASK-RELATIVE OPERATIONAL DEPARAMETRIZATION
```

It does not establish that fundamental time is absent, that chronology has
emerged, or that the universe is globally timeless.

---

## 13. Cross-assumption theorem ledger

| Claim | Current status | Legitimate inference | Illegitimate promotion |
|---|---|---|---|
| Full history is Markov | Exact for finite prefix-causal laws | a Markov representation exists | nature stores the full past as present state |
| Minimal predictive quotient exists | Exact relative to complete law and policy set | target law admits a smallest deterministic predictor | predictor is ontic or source-generated |
| Physical memory closes a cut | Exact when independently evidenced and sufficient | subsystem non-Markovity came from omitted memory | every nondivision has such a memory |
| Process tensor is complete for licensed controls | Established operational framework | state-to-state maps can be insufficient | process tensor is fundamental ontology |
| Instrument-specific quantum Markov order | Established in source domain | memory classification depends on probing grammar | no physical memory exists |
| Q-Cut information burden | Author theorem candidate only | positive sufficient cuts face scalable retained-information pressure | all positive histories or ontologies fail |
| General-boundary formulation exists | Established formal framework | initial/final slicing is not mathematically compulsory | nature uses a general-boundary ontology |
| Page--Wootters relational dynamics | Established in constrained domains | dynamics can be encoded in internal correlations | clock, constraint, and law were derived from no input |
| Clock interaction modifies conditional evolution | Established model result | clock is a physical participant, not a free label | one interaction model settles fundamental time |
| Paper 04 B-clock salvage | Terminal exact finite salvage | one finite relational clock packet can be constructed | complete two-clock law or external-time redundancy |
| Paper 04B repair map | Terminal pre-construction finding | clock adequacy needs R1--R4 | a parent clock model is selected or authorized |

---

## 14. Ranked genuinely physical next tests

These rankings are scientific recommendations only. They create no authority.

### Rank 1 — source-closed causal-break and memory-erasure experiment

**Assumptions tested:** N1 and N2.

Choose a platform with independently addressable system, memory/reference, and
reader degrees of freedom. Freeze a complete intervention set before data:

1. system causal break and re-preparation;
2. memory read, toggle, randomization, erasure, and isolation;
3. incompatible future policies;
4. retained null/failure records; and
5. held-out program sequences.

The decisive output is not a fitted memory model. It is whether one
independently physical carrier screens all registered past influence after the
break. This is the cleanest experimental separator between omitted memory and
interface nondivision.

### Rank 2 — nonvacuous one-parent relational-clock experiment

**Assumption tested:** N4.

Use the R1--R4 criteria of Section 12. The external scalar must affect a frozen
reference prediction; the internal record must replace it over held-out values;
completion/readout timing must be physically represented; and no controller
may be promoted to a clock without task advantage. A second clock is valuable
only after each device separately passes the clock predicate.

This test can establish task-relative deparametrization. It cannot by itself
establish emergent chronology.

### Rank 3 — independently review Q-Cut, then bind it to a physical apparatus

**Assumption tested:** N1.

First review the mathematical candidate without ontology promotion. If it
survives, construct a platform-level source-closure and resource bridge.
Measure not only abstract mutual information but preparation precision,
stability, control complexity, readout error, energy, and apparatus size.

The purpose is to distinguish a genuinely compact physical state from one
real number carrying a hidden response table.

### Rank 4 — forward-law versus regional/whole-law held-out comparison

**Assumption tested:** N3.

This becomes physical only when at least two fully specified laws accept the
same public inputs and predict different complete records without future-data
access or postselection. Comparing two factorizations of the same supplied
joint law has no selection value.

### Rank 5 — clock/gravity coupling only after the preceding gates

Clock redshift, proper time, and gravitational backreaction are important, but
they should not be used to select an ontology before the matter law, clock
record, source, intervention grammar, and complete prediction are independently
specified. MG0 remains a discriminator preflight.

---

## 15. Primary scholarly anchors and exact use

Only primary scholarly sources support new literature claims in this audit.

1. Jacob A. Barandes,
   [*Quantum Systems as Indivisible Stochastic Processes*,
   `arXiv:2507.21192v1`](https://arxiv.org/abs/2507.21192v1): indivisible
   stochastic-law proposal and Hilbert-secondary ontology hypothesis.
2. Jacob A. Barandes,
   [*The Stochastic--Quantum Theorem*,
   `arXiv:2309.03085v2`](https://arxiv.org/abs/2309.03085v2): representation
   from supplied stochastic structure, not source selection.
3. Felix A. Pollock *et al.*,
   [*Non-Markovian quantum processes: complete framework and efficient
   characterisation*, `arXiv:1512.00589v3`](https://arxiv.org/abs/1512.00589v3):
   complete intervention-relative multi-time process framework.
4. Philip Taranto *et al.*,
   [*Quantum Markov Order*,
   `arXiv:1805.11341v3`](https://arxiv.org/abs/1805.11341v3): instrument-specific
   quantum Markov order and the no-finite-order-for-all-instruments theorem for
   non-Markovian processes.
5. Don N. Page and William K. Wootters,
   [*Evolution without evolution: Dynamics described by stationary
   observables*](https://doi.org/10.1103/PhysRevD.27.2885), *Physical Review D*
   **27**, 2885 (1983): relational dynamics through internal clock readings in
   a stationary closed system.
6. Philipp A. Höhn, Alexander R. H. Smith, and Maximilian P. E. Lock,
   [*The Trinity of Relational Quantum Dynamics*,
   `arXiv:1912.00033v3`](https://arxiv.org/abs/1912.00033v3): equivalence of
   relational Dirac observables, Page--Wootters dynamics, and quantum
   deparametrization within a constrained-system domain; covariant POVMs for
   nonideal clocks.
7. Alexander R. H. Smith and Mehdi Ahmadi,
   [*Quantizing time: Interacting clocks and systems*,
   `arXiv:1712.00081v3`](https://arxiv.org/abs/1712.00081v3): interacting
   clock/system constraint and time-nonlocal conditional evolution.
8. Robert Oeckl,
   [*General boundary quantum field theory: Foundations and probability
   interpretation*, `arXiv:hep-th/0509122`](https://arxiv.org/abs/hep-th/0509122):
   amplitudes for general regions and states on general hypersurfaces, with
   ordinary temporal quantum mechanics as a special case.
9. Yakir Aharonov, Peter G. Bergmann, and Joel L. Lebowitz,
   [*Time Symmetry in the Quantum Process of
   Measurement*](https://doi.org/10.1103/PhysRev.134.B1410), *Physical Review*
   **134**, B1410 (1964): time-symmetric ensembles defined with initial and
   final selection.
10. Ekaterina Moreva *et al.*,
    [*Time from quantum entanglement: an experimental illustration*,
    `arXiv:1310.4691`](https://arxiv.org/abs/1310.4691): laboratory
    illustration of Page--Wootters correlations, not a derivation of the
    clock, Hamiltonian, or fundamental absence of external time.

These sources establish theorem domains and working constructions. None by
itself determines which temporal ontology nature uses.

---

## 16. Hostile controls

Any later audit or candidate on N1--N4 must attack at least the following.

1. Rename the complete past as the “present state.”
2. Construct a predictive quotient from the target process and claim source
   derivation.
3. Append an unread idle variable and claim the enlarged ontology is selected.
4. Omit an independently readable environment or memory.
5. Add an unevidenced memory only after observing residual correlations.
6. Fit the memory intervention response on the held-out sequence.
7. Use passive conditioning where a causal break is required.
8. Call CP divisibility, stochastic divisibility, operational Markovity, and
   Barandes indivisibility the same property.
9. Infer a finite physical memory from a finite mathematical horizon.
10. Encode the complete process in one exact real and count one state
    coordinate.
11. Hide future settings in the preparation or shared seed.
12. Infer a fundamental initial-value law from chain factorization.
13. Use full-history kernels calculated from the target and call them the
    physical equation of motion.
14. Use a final boundary record as an input and advertise postdiction as
    prediction.
15. Infer backward causation merely from a two-boundary mathematical
    representation.
16. Infer a forward ontology merely from operational prefix causality.
17. Supply an action, Hamiltonian, wavefunction, process tensor, or region
    amplitude and call its reformulation a derivation.
18. Infer timelessness from a stationary constrained state.
19. Choose the clock/rest split after seeing the desired dynamics.
20. Supply the target system Hamiltonian inside the total clock constraint.
21. Call any monotone controller output a clock without a held-out clock task.
22. Remove a dummy scalar and claim physical deparametrization.
23. Let an external pulse create, select, or stabilize the clock record.
24. Omit the scheduler or second clock that chooses the endpoint.
25. Treat a quantum reference-frame coordinate map as a complete physical
    record transformation.
26. Ignore recurrence, aliasing, finite resolution, or clock backreaction.
27. Use two structurally distinct devices when only one is time-sensitive.
28. Infer chronology, proper time, metric, or gravity from supplied slot order.
29. Reject Barandes because one positive cut fails.
30. Promote Barandes because a Hilbert lift exists.
31. Promote Hilbert ontology because one positive carrier fails.
32. Treat an experimental Page--Wootters illustration as a test that the
    universe has no fundamental time.

---

## 17. Result ladder for this assumption family

```text
AT-L0  STATEMENTS AND THEOREM DOMAINS SEPARATED
AT-L1  EXACT REPRESENTATION/REFERENT COUNTERCONTROLS SURVIVE
AT-L2  ONE SOURCE-CLOSED PHYSICAL CUT IS OPERATIONALLY TESTED
AT-L3  ONE INDEPENDENT MEMORY ENLARGEMENT OR INTERFACE NONDIVISION IS EARNED
AT-L4  ONE NONVACUOUS INTERNAL CLOCK REPLACES AN OPERATIVE SCALAR AT TASK SCOPE
AT-L5  TWO ADEQUATE CLOCKS AND COMPLETE FRAME MAPS SURVIVE
AT-L6  ONE LAW-FORM ALTERNATIVE MAKES A HELD-OUT COMPLETE-PROCESS DIFFERENCE
AT-L7  THE SURVIVING STRUCTURE TRANSFERS TO RELATIVISTIC QFT WITHOUT REFIT
AT-L8  RECIPROCAL MATTER--GEOMETRY DYNAMICS SELECTS OR FURTHER CONSTRAINS IT
```

This audit reaches only `AT-L1` as author-side analysis. No rung is a
scientific award without a separately authorized freeze, independent review,
and root adjudication.

---

## 18. Maximum legitimate claim

> Every finite controlled process can be represented as Markovian on its full
> history, and can be compressed to a minimal predictor relative to a supplied
> policy class. Those constructions consume the complete process and do not
> establish that nature carries the resulting state. An observed
> non-Markovian process can sometimes be closed by an independently evidenced
> memory, but formal history enlargement does not imply physical hidden-Markov
> ontology. Likewise, any ordered finite joint law can be written as an
> initial distribution followed by full-history conditionals, so forward form
> alone does not establish a fundamental forward source law. Page--Wootters
> and modern relational quantum dynamics show that valid subsystem evolution
> can be encoded in correlations of a constrained stationary parent, but they
> receive the clock split, constraint, state, clock observable, and reader
> structure. The first reality-bearing tests are therefore source-closed
> causal breaks with independently manipulated memories and nonvacuous
> one-parent clock tasks that exclude hidden scheduling and readout time.

---

## 19. No-authority firewall

This file:

1. does not open or name an official paper, unit, pin, or review;
2. does not authorize a Q-Cut review or promote its theorem candidate;
3. does not repair or reopen Paper 04 or Paper 04B;
4. does not construct a memory model, relational clock, whole-process law,
   Barandes source law, process-matrix ontology, or general-boundary theory;
5. does not select discrete, continuous, trajectory, Hilbert, stochastic,
   timeless, retrocausal, or block-universe ontology;
6. does not alter the B0-T source-byte failure or authorize reviewers;
7. does not authorize chronology, spacetime, gravity, implementation, or an
   empirical programme; and
8. does not modify `PLAN.md`, `README.md`, `LOG.md`, or the semantic index.

Any promotion-bearing successor requires separate user authority and must
freeze one exact assumption record, one physical interface, one smallest
deletion, one recovery packet, one resource ledger, and one outcome ladder
before construction or data inspection.
