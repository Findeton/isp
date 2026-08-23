# ISP v17 — reality identification and selection-accounting contract

Date: 2026-08-23

Status: **PRIVATE / NONBINDING / NOT A PIN / NO NEW UNIT AUTHORIZED**

Scientific result awarded: **none**

Authority created by this document: **none**

Purpose: formalize the difference between an operational representation, an
empirically identified equivalence class, a physical invariant, an explanatory
reduction of inputs, and a selected ontology. This contract is intended to
prevent the v16 error—promoting exact structure inside an unselected fixture—
from recurring in v17.

## 1. Central conclusion

The programme should not ask whether one candidate can be made internally
beautiful. It should ask which parts of a candidate survive every registered
operational comparison and which new observation or independently justified
principle could distinguish the surviving equivalence classes.

The permanent question for every unit is:

> Did this result constrain the physically admissible class, derive an
> independent physical input, expose a representation-invariant structure,
> establish a scalable theorem, or force a new empirical difference—or did it
> only describe one representative of an unchanged empirical fiber?

There is no universal numerical “selection gain.” The admissible class may be
infinite, differently parametrized, or lack a natural measure. Selection is
reported by explicit set inclusion, separating experiments, derived-input
maps, invariants, or no-go witnesses, never by counting model labels.

## 2. The complete operational profile

Let `M` be a frozen class of candidate microscopic or explanatory models. Let
`E_reg` be the frozen typed category of registered preparations,
interventions, adaptive controls, compositions, readers, failures, resource
meters, and complete continuations.

For each model `M`, define its complete operational profile schematically as

$$
\Phi_{\mathcal E}(M):
\mathcal E_{\rm reg}\longrightarrow\mathsf{Instr}_{\rm op}.
$$

The codomain is not merely a set of outcome distributions. It contains the
complete operational boundary appropriate to the domain:

- normalized classical kernels or quantum instruments;
- post-intervention predictive states/boundaries;
- retained records and their types;
- adaptive conditionals on positive-support events;
- null and failure outputs;
- exposed controller, clock, energy, memory, communication, and other physical
  resource records; and
- the composition, tensor, coarse-graining, and complete-reader relations used
  by future tests.

In finite-dimensional quantum domains, complete comparisons may use diamond or
strategy/comb norms. Classical standard-Borel domains use measure-determining
readers or total-variation-type complete-law metrics. AQFT domains require the
frozen normal-state/observable/instrument test family. No narrow metric may
support a broader equivalence claim.

The word “functor” here is a target obligation, not a license to ignore
enrichment, almost-everywhere conditionals, partial domains, or category
typing. If the exact model needs a pseudofunctor, indexed family, measurable
fibration, or paired stochastic/Heisenberg semantics, that structure must be
printed.

## 3. Empirical equivalence is relative to an experiment domain

Define exact registered equivalence by

$$
M\sim_{\mathcal E}M'
\quad\Longleftrightarrow\quad
\Phi_{\mathcal E}(M)\simeq\Phi_{\mathcal E}(M')
$$

naturally over every registered complete procedure. The isomorphism must
preserve physical ports, record meanings, supplied interventions, and resource
outputs. A bare relabeling of model-internal variables may be gauge; relabeling
a physical control or output is not.

For approximate empirical models, freeze

$$
D_{\mathcal E}(M,M')
=\sup_{e\in\mathcal E_{\rm reg}}
d_e\!\left(\Phi_M(e),\Phi_{M'}(e)\right),
$$

where each `d_e` is the correct complete-process metric and the supremum also
ranges over every registered compatible continuation. An equivalence claim is

$$
D_{\mathcal E}(M,M')\le\epsilon_{\rm phys},
$$

with the tolerance, systematic error, and confidence rule frozen before
evaluation.

Equivalence is always indexed by `E_reg`. If

$$
\mathcal E\subseteq\mathcal E',
$$

then

$$
M\sim_{\mathcal E'}M'\Longrightarrow M\sim_{\mathcal E}M',
$$

but not conversely. “Empirically equivalent” therefore means “not separated by
the printed experiment class,” never “identical in every possible future
experiment.”

## 4. The empirically identified object

The data identify at most the quotient

$$
\mathcal M/\!\sim_{\mathcal E}.
$$

The fiber

$$
[M]_{\mathcal E}
=\{M':M'\sim_{\mathcal E}M\}
$$

contains operationally unresolved representations or ontologies. A model-
internal field, trajectory, scalar algebra, hidden fiber, or history label is
not selected merely because it is coherent, economical, or visually natural.

A property `X` has different statuses:

1. **representative property:** true of one chosen `M`;
2. **gauge-invariant property:** stable under declared presentation changes of
   that `M`;
3. **fiber invariant:** true of every member of `[M]_E` under the admitted
   equivalences;
4. **class invariant:** true of every empirically adequate class remaining
   after all frozen constraints;
5. **empirically selected property:** absence of `X` is separated by a
   registered observation;
6. **postulated property:** imposed by a new physical principle not derived
   from current evidence.

Status 3 supports a representation-invariance theorem only inside the declared
candidate universe; that universe may itself have been restricted so that `X`
is common. Status 4 can support a necessity claim only with the adequate-class
premises printed. Status 5 supplies direct empirical selection on the
registered domain. Status 6 is allowed only when labeled as a new postulate
with an independent motivation and immediate empirical-wedge audit.

## 5. Five legitimate forms of progress

Every promotion-bearing unit should identify at least one of these. A pure QA
or repair unit may enable one but does not itself claim it.

### 5.1 Empirical partition refinement

There exist previously equivalent candidates `M,M'` and a newly registered
experiment `e_*` such that

$$
d_{e_*}\!\left(\Phi_M(e_*),\Phi_{M'}(e_*)\right)
>\epsilon_{e_*}.
$$

The experiment, metric, calibration, and decision rule must precede the result.

### 5.2 Derived-input gain

A physical input previously declared independently is derived from older
inputs without introducing an equally strong surrogate. Track a dependency
graph rather than a slogan. If

$$
I_{\rm old}=F(I_1,\ldots,I_k)
$$

is proved, the derivation is a gain only if none of `I_1,...,I_k` encodes
`I_old` through a lookup table, boundary condition, controller, fitted kernel,
or hidden schedule.

Examples include nonvacuously replacing an external clock schedule with a
physical internal record, deriving a response coefficient from a frozen law,
or deriving a continuum prediction from a scalable family. Gauge removal of a
dummy coordinate is not derived-input gain.

### 5.3 Invariant-structure gain

A theorem proves that `X` descends to the empirical quotient or is required by
every member of the admitted adequate class. Phase-complete future predictive
structure may be forced even when complex scalars are not ontologically
selected. A record event may be operationally invariant while the microscopic
trajectory remains idle.

### 5.4 Broad no-go or classification gain

A theorem eliminates a well-defined class under printed premises or classifies
all possible realizers. A counterexample to one finite fixture is not a class
no-go. After repeated failures of the same semantic type, the next scientific
move should be a general theorem or a stop, not another patched fixture.

### 5.5 Scaling or controlled-limit gain

A family indexed by physical size, precision, energy, distance, or scale has a
proved composition law, approximation bound, and stable limit. A handful of
finite examples, however exact, cannot earn continuum, locality, dimension, or
geometry.

## 6. Empirical-wedge ledger

For a candidate `M` and the domain-appropriate accepted comparator `M_0`, define

$$
\Delta_e(M;M_0)
=d_e\!\left(\Phi_M(e),\Phi_{M_0}(e)\right).
$$

The comparator is standard quantum theory for finite quantum experiments,
QFT on a supplied metric for the present relativistic laboratory domain, and
QM+GR only where the experiment genuinely enters their common domain.

Every new physical postulate receives one row:

| Wedge status | Meaning |
|---|---|
| `IDENTICALLY-ZERO-THEOREM` | exact empirical equivalence on the registered domain |
| `ZERO-WITHIN-FROZEN-TOLERANCE` | no resolved difference; finite-data scope printed |
| `UNCOMPUTED` | proposed principle has no derived operational prediction yet |
| `TUNABLE` | a free parameter can make the wedge vanish; no prediction without independent calibration |
| `CALIBRATED` | parameters fixed on training/calibration data; held-out wedge remains testable |
| `FORCED-NONZERO` | parameter-free or independently fixed difference follows from the frozen postulate |
| `REFUTED` | held-out observation excludes the frozen candidate on its printed domain |

A “potential experimental signature” is not a wedge until it is derived from
the frozen law. Adding a term because it would be interesting is model
invention, not discovery.

Resource differences belong in `Delta_e` only when they are physical outputs
or required interventions of the complete experiment. The source-code length
of two descriptions is not an empirical wedge.

## 7. A simulation preorder for explanatory cost

The feedback correctly identifies explanatory cost as a live question, but a
raw ontic-state count or description length is not representation invariant.
Continuous variables can hide arbitrary tables in exact real numbers; idle
fibers can inflate any carrier; different universal languages change code
length; and unrestricted contextual models can reify the complete predictor.

Define cost only relative to:

1. a frozen scalable target family `Q_n`;
2. a frozen candidate class `C_n`;
3. allowed encoders, decoders, interventions, and free simulations;
4. an approximation tolerance and robustness domain;
5. a uniformity/computability requirement across `n`;
6. a composition and locality interface; and
7. a physical or operational resource vector.

Write

$$
M\preceq_{\mathcal F,\epsilon,\mathbf r}N
$$

when one fixed family of admitted simulations in `F` uses resource vector
`r(n)` to reproduce the complete profile of `M` from `N` to error `epsilon`,
naturally under registered composition. The simulator may not receive the
entire target process as a per-experiment oracle unless that context bandwidth
is explicitly costed.

Useful cost coordinates can include:

- accessible classical memory capacity across a registered causal cut;
- dimension or entropy of a minimal sufficient predictive boundary;
- quantum memory dimension where the comparator uses it;
- bandwidth of preparation, transformation, or measurement context supplied
  to the simulator;
- communication across a declared multipartite separation;
- number and range of physical couplings in a uniform family;
- energy, entropy production, record, reset, and clock resources;
- process-tensor or comb bond/memory dimension;
- approximation error and robustness; and
- uniform circuit/kernel-generation complexity under a fixed computational
  model.

Raw carrier cardinality is not a universal cost. Idle inflation makes it
arbitrarily large, while one continuous coordinate can encode infinite formal
information unless accessible precision and dynamics are bounded.

## 8. The positive-history cost trilemma

Paper 01 proves that positive probabilities on actual laboratory records can
represent finite-dimensional, definite-order quantum processes when the
complete quantum predictor and whole-program context are retained. It does not
prove that a compact autonomous microscopic positive law exists.

The high-leverage next theorem target should be a trilemma rather than a demand
for one scalar “complexity.” For a scalable family of quantum processes, prove
or refute:

> Every ordinary-positive history realizer satisfying the frozen complete
> process contract must pay at least one of the following costs:

1. **predictive-state cost:** it retains a boundary with essentially the
   phase-complete quantum process capacity;
2. **context/coordination cost:** it receives growing whole-program context,
   nonlocal communication, or a global coordination variable; or
3. **composition cost:** it abandons a uniform local/compositional update law,
   using task-specific kernels, unbounded memory, or nonuniform lookup data.

A positive result would instead exhibit one uniform, compositionally stable,
ordinary-probability law whose costs remain below the relevant quantum
predictive benchmark without moving information into another coordinate.

A detailed private feasibility analysis, including candidate classes, free
simulations, a resource vector, staged target families, and anti-laundering
controls, is recorded at
`/private/tmp/v17_positive_history_cost_theorem_feasibility.md`.

One exact branch has now been isolated privately. For the
\(\alpha\)-Partial Matching prepare--measure family, any finite
ordinary-positive boundary satisfying a past/future screening factorization
induces a classical randomized one-way protocol and therefore requires
\(\Omega(\sqrt n)\) classical bits for fixed \(\alpha\), while the quantum
carrier uses \(O(\log n)\) qubits. The reduction, premises, and escape ledger
are recorded at
`/private/tmp/v17_operational_cut_nondivision_theorem_candidate.md`. This is a
private scoped theorem candidate, not an adjudicated result or universal
ontology no-go.

A second private candidate removes the finite-carrier assumption. Under the
explicit natural hard ensemble used in the source proof, a standard-Borel
positive screening variable
must carry

$$
I(X:\Lambda\mid S)=\Omega(\sqrt{n/\alpha})
$$

whenever the total prediction and approximate-factorization error retains a
constant success margin. The response-quantization proof is recorded at
`/private/tmp/v17_continuous_cut_information_theorem_candidate.md`. The result
is invariant under one-real encodings and idle-fiber inflation, but remains
cut-, ensemble-, and screening-relative. Indivisible whole-history laws remain
unclassified.

This target is deliberately compatible with indivisible, non-Markovian
dynamics. A theorem restricted to Markovian hidden variables cannot decide the
Barandes question.

The trilemma is conditional on the frozen exact/approximate quantum process
contract, intervention freedom, context interface, and composition rules. A
candidate can escape by rejecting one of those premises—through a preferred
structure, measurement dependence, retrocausal/global boundary data,
indefinite-order physics, or a genuine empirical deviation—but the escaped
premise and its wedge then become the result. It may not disappear into an
uncosted variable.

## 9. A workable theorem domain

To make the trilemma falsifiable, freeze a nested family such as:

$$
\mathsf Q(n,d,L,\epsilon),
$$

the causally ordered `L`-slot process family on `n` subsystems of local
dimension `d`, evaluated to operational precision `epsilon` under a
tomographically complete intervention set.

Candidate positive-history realizers must provide:

1. a standard-Borel or finite configuration boundary;
2. one uniform root-law and update-law generator across `n`;
3. normalized complete instruments for every registered adaptive program;
4. tensor and sequential composition under a fixed interface;
5. explicit context ports and communication;
6. explicit memory carried across each cut;
7. an actual-record map distinct from any microscopic actuality postulate;
8. no oracle containing the complete target comb unless its size/bandwidth is
   counted; and
9. exact or frozen-approximate operational adequacy.

Test subfamilies should be staged:

- stabilizer/Clifford processes, where efficient contextual models exist and
  prevent a false universal exponential claim;
- sequential state-independent contextuality, which has proven classical
  memory costs;
- arbitrary pure-state unitary families, where Markovian ontological models
  have known dimension lower bounds;
- finite-memory non-Markovian process families;
- Bell-separated tasks, where communication or measurement-dependence costs
  must be exposed; and
- universal multi-time combs, the actual Paper 01 ceiling.

The theorem must permit different answers in these subfamilies. Contextuality
does not imply exponential cost in every model, and efficient stabilizer
simulation does not extend automatically to universal quantum processes.

## 10. What existing theorems do and do not establish

### 10.1 Markovian ontological dimension

Montina proves that, for the class of Markovian ontological theories in the
paper, representing an `N`-dimensional quantum system requires at least
`2N-2` continuous variables. For `n` qubits this grows exponentially in `n`.
This is a powerful branch result, not a theorem about unrestricted
indivisible, contextual, or whole-program history laws.

Primary source:
https://doi.org/10.1103/PhysRevA.77.022104

### 10.2 Contextuality and memory

Kleinmann et al. show that sequential state-independent contextuality can
require classical simulator memory exceeding the information capacity of the
measured system in their scenarios. Karanjai, Wallman, and Bartlett derive
contextuality-based lower bounds and quadratic classical-memory scaling for
the qubit stabilizer subtheory under their simulation framework. These support
a context/memory coordinate, not a universal ontology lower bound.

Primary sources:
https://arxiv.org/abs/1007.3650
https://arxiv.org/abs/1802.07744

### 10.3 Efficient contextual controls

Efficient contextual ontological models exist for important restricted
subtheories, including `n`-qubit stabilizer quantum mechanics with quadratic
memory/computation in a published construction. This is an essential hostile
control against equating contextuality with exponential inefficiency.

Primary source:
https://doi.org/10.1103/PhysRevLett.129.130401

### 10.4 Statistical comparison and recovery

Quantum versions of Le Cam/Blackwell comparison relate channel simulation by
post-processing to operational decision performance and diamond-norm
deficiency. This supplies a rigorous language for “one record/channel is
sufficient for another” in the clock gate, but it does not select an ontology.

Primary source:
https://arxiv.org/abs/1512.07016

### 10.5 Signaling dimension

Doolittle and Chitambar quantify the minimum classical communication needed to
simulate a channel's input-output correlations when shared randomness is free,
and provide device-independent bounds. This gives an operationally meaningful
communication coordinate for matched regional or prepare-transform-measure
cuts. It is not automatically an ontological-memory or locality theorem.

Primary source:
https://arxiv.org/abs/2102.12543

### 10.6 Process-tensor memory

Purified process-tensor constructions provide cut-sensitive quantum memory
complexity and a possible comparator for non-Markovian processes. A bridge
theorem is still required before a tensor-network bond parameter can be called
physical ontic memory.

Primary source:
https://arxiv.org/abs/2203.01492

## 11. Hostile controls for the cost theorem

1. idle-bit or idle-continuum inflation changes raw carrier size;
2. arbitrary target table encoded in one exact real number;
3. whole program supplied as free context;
4. nonuniform kernel family with one hand-written law per `n`;
5. exponential preprocessing omitted from online memory;
6. shared random seed stores the target process;
7. global coordinator omitted from local communication cost;
8. measurement dependence renamed contingent state;
9. final output record counted while predictive memory is ignored;
10. postselection success probability omitted;
11. approximate simulation reported without uniform error over continuations;
12. stabilizer efficiency extrapolated to universal quantum theory;
13. Markov lower bound extrapolated to indivisible histories;
14. Hilbert dimension compared with raw classical cardinality at unequal
    precision;
15. context-dependent decoder selected after seeing the process;
16. code length or elegance used as a physical selector;
17. minimality proved only inside a family chosen because the result works;
18. physical energy/entropy cost confused with algorithmic simulation cost;
19. operationally equivalent models called empirically distinguished because
    their internal variables differ; and
20. a resource lower bound promoted to ontological truth.

Operational or computational cost theorems diagnose what a representation
must carry under declared interfaces. They do not prove that nature performs a
classical simulation of quantum theory, nor do they select the lower-cost
representative without an independently physical selection principle.

## 12. Integration with the relational-clock gate

The repaired clock target can earn derived-input gain even if it predicts no
deviation from standard quantum theory. The input being tested is an
independently operative external timing resource. A positive result must show:

1. the reference clock changes registered predictions before replacement;
2. the internal record is independently adequate on a timekeeping task;
3. the clock-system core exists when the validation clock is disconnected;
4. the record statistically and instrumentally screens the target from the
   reference over a frozen domain;
5. an internally triggered experiment reproduces the externally triggered
   experiment to a predicted finite-resource tolerance; and
6. no schedule, timestamp, sample count, or controller carries the removed
   input covertly.

Then one independent physical input has become derivable from a represented
subsystem and law. This is explanatory/physical progress even if

$$
\Delta_e=0
$$

relative to ordinary quantum mechanics on the same laboratory domain. It is
not ontology selection. A constrained/autonomous representation equality by
itself earns no derived-input gain because universal parametrization can make
it tautological.

The private clock blueprint at
`/private/tmp/v17_paper04b_successor_blueprint.md` already implements these
distinctions. No official successor is opened.

## 13. Integration with later v17 gates

### 13.1 Operational chronology

A future influence relation derived from interventions is an operational
signalling structure relative to supplied opportunities. It earns endogenous
chronology only if it is not reducible to laboratory slot order, survives
common-cause/cancellation/cycle attacks, and supplies additional oriented
structure without reading the procedure syntax. Paper 05 remains closed until
an accepted clock-relative law exists.

### 13.2 Geometry and continuum

No geometry gate reopens without a scalable family, controlled coarse
graining, convergence/error bounds, emergent local operational algebra, and
separation of universal behavior from regulator artifacts. Finite posets and
graphs remain regression tests.

### 13.3 Matter and gravity

A candidate common law must generate, from the same immutable dynamics and
different contingent states,

$$
\text{matter change}
\longrightarrow
\text{operational geometry change}
\longrightarrow
\text{later matter-response change}.
$$

Both arrows require independent readers, multiple matter/clock probes, and
held-out low-energy tests. A decoder, supplied metric, fitted feed-forward
table, or copied Einstein equation earns no derived-input gain.

## 14. Workflow corrections

1. **Classify every manuscript:** representation theorem, identifiability/no-go
   theorem, proposed physical law, or empirical comparison. Mixed products
   report each coordinate separately.
2. **After repeated semantic failures, generalize or stop:** do not maintain an
   automatic repair chain.
3. **Record selection accounting:** print the before/after admissible class,
   separating witness, derived-input map, invariant, wedge status, and scaling
   status.
4. **Treat automated panels as adversarial QA:** they are not external
   replication. Human domain review is required before a new-physics claim.
5. **Compare equivalence classes, not attractive representatives:** a
   multi-family tournament is meaningful only after the common profile,
   metrics, free simulations, and physical resource outputs freeze.
6. **Do not force novelty:** `Delta=0` plus a genuine equivalence or
   nonselection theorem is an honest result; inventing a deviation is not.

## 15. Present research-front decision

The v17 evidence currently supports:

```text
FINITE DEFINITE-ORDER QUANTUM RECORD REPRESENTATION:  ACCEPTED WITH SCOPE
OPERATIONAL QUOTIENT / IDLE-FIBER NONSELECTION:       ACCEPTED WITH SCOPE
RELATIVISTIC OPERATIONAL REPRESENTATION:              ACCEPTED ON SUPPLIED SPACETIME
SELECTED MICROSCOPIC ONTOLOGY:                        NO
EMPIRICAL ISP/QM DISCRIMINATOR:                       NO
ACCEPTED INTERNAL RELATIONAL CLOCK:                   NO
FINITE POSITIVE CUT-CAPACITY THEOREM:                 PRIVATE / UNREVIEWED CANDIDATE
CONTINUOUS POSITIVE CUT-INFORMATION THEOREM:          PRIVATE / UNREVIEWED CANDIDATE
UNIFORM INDIVISIBLE-LAW CLASSIFICATION GATE:          PRIVATE / SPLIT-BEFORE-PIN
UNIVERSAL POSITIVE-HISTORY COST THEOREM:              OPEN / UNCONSTRUCTED
PAPER 05 CHRONOLOGY:                                  CLOSED
GEOMETRY / GRAVITY:                                   CLOSED
```

The next official scientific move remains subject to fresh authority because
the exact Paper 04B pin is terminal `REVISE-BEFORE-MODEL-SELECTION`. Safe
private work may continue on the model-neutral clock repair, operational
identification contract, cost-theorem scope, and uniform indivisible-law
classification. It may not select a parent, run a tournament, open Paper 05,
or construct gravity.
