# PRIVATE PHYSICS SUPPLEMENT — native stochastic lift of operational records

Status: PRIVATE / OFF-TREE / NON-AUTHORITATIVE

This supplement develops an interface only. It does not construct, select, or
validate a native ontology. It does not reopen terminal Paper 04 and it does not
authorize a successor cycle.

## 1. The correction forced by Paper 04

Paper 04 established an operational typing failure. A controller-dependent
pointer permutation did not preserve the declared classical output algebra on an
admitted coherent input. That conclusion is exact, but its ontological meaning is
limited.

The correct inference is:

> The proposed pointer is not a classical operational record at that boundary.

The following inference is invalid:

> Therefore the corresponding quantity cannot be physically definite.

In a Barandes-style stochastic ontology, a native beable is a measurable function
of a definite configuration. Its Hilbert-space representative need not be central
in every operational subalgebra, and a noncommutative operational observable need
not itself be a native beable. The dictionary between these levels must be supplied
and tested. Algebraic noncentrality is neither an actuality theorem nor an
unreality theorem.

This yields four distinct questions:

1. Is there a definite native value in each actual history?
2. Is that native value a stable record under a declared native future grammar?
3. Is a corresponding value readable through a valid commutative operational
   output instrument?
4. Is that operational output redundantly and nondisturbingly available to
   multiple readers?

None of these questions answers another by definition.

## 2. Four layers and two orthogonal boundary properties

### 2.1 Native actual variable

Let $\mathcal C$ be a declared native configuration space and let $h_*$ be the
actual history in one run. A native variable is a measurable map

$$
b:\mathcal C\longrightarrow B
$$

or, when the value is irreducibly history-dependent,

$$
b:\mathsf{Hist}\longrightarrow B.
$$

Its actual value is $b(c_*)$ in the first case and $b(h_*)$ in the second.
Definiteness does not imply that the value is readable, stable, local, classical
in an operational algebra, or dynamically autonomous.

### 2.2 Native stable record

At a declared native boundary $D$, a native record is a measurable function

$$
r_D:\mathcal C_D\longrightarrow Y.
$$

It is stable relative to a licensed native future category
$\mathsf{Fut}_{\mathrm{stable}}$ only if every supported future arrow preserves
its value. In an exact discrete model this is the pointwise condition

$$
r_{D'}(F(c))=r_D(c)
$$

for every legal $c$ and every $F:D\to D'$ in
$\mathsf{Fut}_{\mathrm{stable}}$. In a measure-theoretic model the null-set
convention must be frozen and stability stated almost surely with respect to the
declared family of contingent initial laws. Identity-only closure is vacuous.

### 2.3 Operational classical record

An operational classical record is an exposed outcome algebra or sigma-algebra
with a normalized instrument, complete readers, and a state-independent action of
the registered presentation symmetries. In the finite sharp domain it is a
commutative output factor whose sector projectors are central in the complete
operational boundary algebra.

This is a statement about usable laboratory outputs. It is not a statement that
only central operators can represent physically definite native variables.

### 2.4 Operational objective broadcast

An operational record is objectively broadcast only when at least two disjoint,
independently addressable fragments carry the same distinguishable label, their
registered reads commute or satisfy the frozen nondisturbance bound, and the
joint state has the required broadcast structure. A mutual-information plateau by
itself is insufficient.

Operational objectivity does not select one actual history. Native actuality does
not imply operational objectivity.

### 2.5 Two division notions

A **Barandes division event** is a boundary that is licensed as a conditioning
time for the first-order endpoint transition law. It does not require
the theory to specify a probability distribution over all intermediate
trajectories.

A **strong screening division** is a property of a separately supplied
non-Markovian realizer or path law. It requires

$$
\mathbb P(H_+\in A\mid H_-,C_D)
=
\mathbb P(H_+\in A\mid C_D)
$$

for every registered future event $A$. The expression is meaningful only after
the joint history law, conditioning domain, and null-set convention have been
declared.

These notions may coincide in a completed model, but neither is definitionally
the other. Decoherence, a stable pointer, reader agreement, or operational
broadcasting alone establishes neither.

## 3. Minimal native packet and optional realizer

The minimal Barandes-compatible packet is

$$
\mathfrak B
=
(\mathcal C,\mathcal G,\mathsf E,\Omega,
 \Gamma,\mathsf{Obs},\mathsf{Div},
 \mathsf{Fut}_{\mathrm{stable}},\mathsf{Exec}).
$$

The fields have the following meanings.

1. $\mathcal C$ is the fixed native configuration object, including every
   apparatus, controller, reference, environment, and record degree of freedom
   invoked by the experiment.
2. $\mathcal G$ is the presentation or gauge groupoid. A gauge arrow changes a
   description, not the physical configuration.
3. $\mathsf E$ is the typed experiment category. Settings, interventions, and
   readers are physical slots, not silent changes to the law.
4. $\Omega$ is the explicitly contingent initial distribution or preparation
   family. It is not absorbed into the nomological law.
5. $\Gamma_e(t\leftarrow D)$ is the fixed family of first-order stochastic
   endpoint laws from licensed division boundaries $D$ to registered target
   boundaries $t$, all inherited from one parent dynamics.
6. $\mathsf{Obs}_{e,t}$ maps target configurations to registered operational
   transcripts.
7. $\mathsf{Div}$ declares the boundaries allowed as conditioning times.
8. $\mathsf{Fut}_{\mathrm{stable}}$ is the typed record-preserving future
   subcategory.
9. $\mathsf{Exec}$ is the broader executable experiment category and includes
   typed erasers and destructive controls.

This packet does **not** contain a unique probability law over complete
intermediate trajectories. Barandes's indivisible process retains an equivalence
class of compatible non-Markovian realizers. If a theory adds a particular
realizer, it must freeze the additional object

$$
\mathfrak R=(\mathsf{Hist},\mathbb P_{\rm path})
$$

or an equivalent complete Kolmogorov tower and state what selects it. The realizer
is a new physical or nomological postulate, not part of the minimal correspondence.
One actual trajectory may be ontically asserted without assigning a unique
probability measure to all possible trajectories; statistical claims involving
several intermediate times then require either an enlarged endpoint experiment or
the optional realizer.

The packet must distinguish physical symmetry from gauge redundancy. A physical
reference state may break a physical symmetry and consume asymmetry. It may not be
used to break a pure descriptive redundancy.

## 4. One parent law, not one law per arm

The invariant-record, raw-record, eraser, redundant-reader, and reference-control
arms must be restrictions of one common parent experiment. The setting choice is
a physical variable or preparation inside the parent packet. It is not permission
to replace $\Gamma$.

Let $s$ be the setting variable and let $c_0,c_f$ be initial and final composite
configurations. The endpoint law is

$$
\mu^{\Omega}(ds,dc_0,dc_f)
=
\Omega(ds,dc_0)\,\Gamma(dc_f\mid s,c_0).
$$

Each experimental arm is then a conditional or typed restriction of this same
law. Postselection on a null setting is refused. If changing a setting changes the
microscopic law rather than a physical input configuration, the comparison is not
an experiment within one theory.

For an indivisible interval, the endpoint law relates the complete configuration
at the admitted division directly to the complete configuration at the target.
No stochastic intermediate kernel may be inserted merely to imitate a circuit
diagram. A Barandes division licenses a new endpoint conditional; factorization
of an optional path realizer requires the separately stronger screening property.

## 5. The native-to-operational commuting requirement

For every registered endpoint experiment $e$ with target $t$, let

$$
O_{e,t}:\mathcal C_t\longrightarrow\mathsf{Trans}_e
$$

be the gauge-invariant observation map into the complete operational transcript.
Given a contingent initial law $\Omega_e$, define

$$
\mu_{e,t}^{\Omega}(dc_0,dc_t)
=
\Omega_e(dc_0)\,\Gamma_e(t,dc_t\mid D,c_0).
$$

The native lift reproduces the operational theory only if

$$
(O_{e,t})_*\mu_{e,t}^{\Omega}=P_{e,t}^{\mathrm{op}}
$$

for every admitted preparation, adaptive policy, reader, coarse graining, and
held-out experiment in the registered domain.

Equivalently, for every bounded measurable operational reader $f$,

$$
\int f(O_{e,t}(c_t))\,d\mu_{e,t}^{\Omega}(c_0,c_t)
=
\int f(x)\,dP_{e,t}^{\mathrm{op}}(x).
$$

This equality must be derived from the frozen native packet. It may not be made
true by defining $\Gamma$ from the desired operational probabilities after those
probabilities are opened.

If an optional realizer $\mathfrak R$ is supplied, its $(D,t)$ endpoint marginal
must equal $\mu_{e,t}^{\Omega}$. This consistency condition does not select a
realizer and does not make the realizer part of the minimal lift.

The observation maps must satisfy:

- gauge descent: $O_{e,t}(c)=O_{e,t}(g\cdot c)$ for every descriptive gauge
  arrow $g$;
- typed naturality under experiment wiring;
- compatible coarse graining of records;
- exact retention of setting and reader provenance;
- explicit treatment of null events;
- no hidden future memory omitted from an allegedly sufficient boundary.

## 6. Adaptive endpoint experiments and empirical equivalence

Matching one instrument is not enough. A candidate lift must match every complete
registered endpoint experiment under interventions.

An adaptive policy chooses a later physical setting from an earlier readable
record. In the minimal endpoint formulation, the controller, its memory, every
setting write, and the final transcript are components of one enlarged physical
experiment. Its target configuration contains the complete registered transcript.
For each policy $\pi$, the endpoint pushforward must equal the operational law:

$$
(O_{e,\pi,t})_*\mu_{e,\pi,t}^{\Omega}=P_{e,\pi,t}^{\mathrm{op}}.
$$

This construction does not assign a joint probability to unrecorded intermediate
configurations. A physical controller may respond to an intermediate apparatus
record without turning that boundary into a stochastic restart; the controller
and carried record remain parts of the indivisible endpoint experiment. A
Barandes division is required only if the theory claims a new endpoint conditional
with that boundary as its conditioning input. Claims about correlations among
unrecorded intermediate configurations require the optional realizer.

Two native lifts are empirically equivalent on a registered domain only if the
endpoint identity holds for every licensed policy and complete reader in that
domain. Equality for one prepared state, one POVM, or one nonselective channel is
insufficient.

They are ontologically equivalent only if there is a groupoid isomorphism between
their complete native configuration/experiment packets that preserves endpoint
laws, beables, interventions, observation maps, and division structure. If both
theories additionally assert path realizers, the isomorphism must also preserve
their realized history objects and path measures. Operational equivalence does
not imply ontological equivalence.

## 7. Actuality and the measurement record

In one run the actual target configuration is $c_t^*$ and, if the ontology makes
the stronger claim, one actual trajectory $h_*$ connects the boundaries. The
observed endpoint record is

$$
y_*=O_{e,t}(c_t^*)_Y.
$$

For a Barandes-style lift, a measuring device's final outcome must be a function
of the final composite native configuration. It need not be a pre-existing value
of the measured emergeable. Thus the interface must identify:

1. the final apparatus configuration map;
2. the record coarse graining of that configuration;
3. the contingent distribution over initial configurations;
4. the fixed endpoint law producing the final correlation;
5. the operational instrument reproduced by pushforward.

If a claim uses a probability for an unrecorded intermediate configuration, it
must also identify the selected realizer and show its endpoint consistency.

A diagonal density matrix or broadcast state is an ensemble description, not the
actual configuration or trajectory. Conversely, the claim that one native
trajectory is actual does not by itself establish the operational instrument,
robustness, or objectivity of its record.

## 8. Beables, emergeables, and noncentral operators

The interface adopts the following firewall.

> Noncentral in an operational representation does not mean unreal in the native
> ontology. Definite in the native ontology does not mean central, readable, or
> classical in every operational representation.

A native beable requires a declared measurable function on configurations or
histories. Its Hilbert representative is fixed only by a specified dictionary.
An operational noncommutative observable may instead be an emergeable: a pattern
in the complete measurement interaction, not a pre-existing system value.

Therefore the center-preservation theorem classifies classical operational
outputs. It does not classify all possible native beables. The noncommutative
record-completion theorem classifies one represented observable closure. It does
not declare that closure fundamental.

## 9. Record stability, erasure, and hidden traces

The native and operational erasure questions must be tested separately.

1. **Visible reset:** the exposed operational label is set to a standard value.
2. **Operational erasure:** no registered operational reader distinguishes the
   prior value.
3. **Recoverable hidden trace:** an enlarged licensed reader recovers the value
   from a memory, reference, controller, or environment.
4. **Native destruction:** no complete native future variable retains the value.

Endpoint-law stability at a Barandes division $D$ is the support condition

$$
\Gamma_F\!\left(\{c':r_{D'}(c')=r_D(c)\}\mid c\right)=1
$$

for every licensed stable future $F:D\to D'$ and every admitted $c$ (with the
declared almost-sure convention in continuous models). Only a complete native
packet plus a separating family of future variables can decide native destruction
at its registered target boundaries. A claim that no trace existed at any
intermediate point additionally requires a realizer. Unitary uncomputation
generally establishes neither native destruction nor a division. If an
operational eraser restores interference, the endpoint law must reproduce that
target statistic without inserting a classical stochastic alternative at a
nondivision.

## 10. Stable record versus decoherence and broadcasting

Decoherence is reduced operational coherence caused by correlations with an
environment. It is not identical to native actualization, record stability, an
admitted Barandes division, or strong screening under a selected realizer.

Spectrum broadcasting is an operational structural criterion for independently
available classical information. It is stronger than an entropic redundancy
plateau, but it still does not select a native ontology or prove that a boundary is
an admitted conditioning division or a strong screening boundary.

A native lift must therefore print six independent coordinates:

```text
NATIVE-ACTUAL-VALUE
NATIVE-STABLE-RECORD
OPERATIONAL-CLASSICAL-OUTPUT
OPERATIONAL-OBJECTIVE-BROADCAST
BARANDES-DIVISION
STRONG-SCREENING-DIVISION
```

Each coordinate is `CONSTRUCTED`, `REFUTED`, `UNTESTED`, or `ILL-TYPED` with an
explicit witness or blocker.

## 11. Physical reference resources

If a raw coordinate becomes measurable only relative to a physical reference,
the reference must be inside $\mathcal C$ and $\Gamma$. Its preparation,
finite dimension, asymmetry, localization, energy, disturbance, reuse, and
backreaction are part of the physical claim.

The reference may not be:

- a label transformation treated as a costless system;
- a preferred basis selected after the desired output is known;
- an inaccessible spectator whose only purpose is to make a dilation work;
- changed between experimental arms without a physical intervention;
- declared classical while its relevant coherences are used elsewhere.

Exact deterministic programming of a finite orbit of distinct sharp measurements
requires perfectly distinguishable program states and a reference dimension at
least the orbit size. An uncountable exact orbit cannot be supplied by a finite
reference. These are necessary resource bounds, not an ontology theorem.

## 12. Class-relative native nonselection

An idle extension illustrates but does not universally prove native
underdetermination. Given a lift $\mathfrak B$, one may form a declared class of
extensions $\mathfrak B\times Z$ in which $Z$ is unread and dynamically idle for
every registered endpoint experiment. These extensions have the same operational
pushforwards but need not be ontologically isomorphic. If a path realizer is also
asserted, its extension is a separate comparison and cannot be inferred from
endpoint equivalence.

The result is only:

> The present operational experiment does not select a unique native lift within
> the registered class containing unread idle extensions.

It is not:

> No structural or empirical principle can ever select a native ontology.

The idle extension is excluded as physical if a separately justified parsimony,
completeness, dynamical coupling, locality, or intervention principle rules it out.
Such a principle must be frozen independently rather than chosen because it
selects a desired ontology.

## 13. Anti-circularity chronology

A prospective native model must be frozen in the following order:

1. configuration space, with a history space only if a realizer is claimed;
2. gauge/presentation groupoid;
3. contingent preparation family;
4. one parent endpoint law, plus any separately claimed realizer;
5. physical experiment slots and intervention semantics;
6. native-to-operational observation maps;
7. division and stable-future categories;
8. native record and reference variables;
9. training/calibration experiments;
10. held-out operational experiments and their outcomes.

The model may then be rejected, calibrated within a preregistered family, or
compared with alternatives. No element in steps 1--8 may be selected from the
held-out outcomes. Parameters fitted in step 9 remain declared inputs and must be
tested out of sample.

## 14. Exact constraints from the invariant/raw/eraser experiment

A native lift of the minimal invariant-record experiment must use one fixed
configuration object and one fixed parent law across all arms. It must reproduce:

1. preservation of within-invariant-fiber coherence under the invariant record;
2. loss of the registered interference contrast under the raw-coordinate record;
3. recovery under the coherent eraser;
4. fragment agreement in the redundant invariant arm;
5. the reference-resource dependence of the invariant label;
6. the resource and disturbance accounting of the reference and controller.

This implies the following native constraints.

- The raw arm cannot insert an actual classical intermediate value at a boundary
  whose later eraser statistics require indivisibility.
- Any hidden native trace claimed to survive the eraser must be included in the
  complete reader domain and tested by a separating intervention.
- The reference degree of freedom must be physical if the invariant is relational
  to it.
- A definite final apparatus record may coexist with an earlier indivisible
  interval; definiteness at the final boundary does not Markovize the interval.
- A broadcast operational record may be a coarse graining of a finer native
  configuration, but the map and its stability must be explicit.

## 15. Falsifiers and discriminators

A native lift earns evidential weight only through predictions not already built
into its reconstruction. The minimum discriminator suite includes:

1. unseen adaptive policies;
2. repeated use of the same reference;
3. interventions directly on the proposed native memory/reference;
4. eraser and delayed-choice arms;
5. finite-resource deviations from ideal covariance;
6. environment-fragment reads outside the calibration family;
7. tests of stable-record persistence under nonidentity futures;
8. separate tests of Barandes conditioning admissibility and, where a realizer is
   claimed, strong future screening;
9. held-out source states with the same operational coarse record;
10. competing lifts with equal training predictions but differing test
    predictions.

If two lifts induce the same complete endpoint-experiment law for every licensed
policy and reader, the current domain cannot select between them. Elegance,
Hilbert dilation, or a preferred basis is not evidence.

## 16. Relation to Barandes

The interface is compatible with the following core Barandes distinctions:

- a fixed configuration space supplies ontological content;
- a contingent standalone probability distribution is not the dynamical law;
- the stochastic law is nomological;
- a system follows one definite trajectory;
- its first-order endpoint laws need not select a unique Kolmogorov tower or
  non-Markovian realizer;
- Hilbert-space states and noncommutative operators are secondary
  representational tools;
- measurements are ordinary interactions ending in definite apparatus
  configurations;
- interference and decoherence can reflect indivisible dynamics and leaked
  correlations rather than literal simultaneous configurations.

The interface does not inherit several things that Barandes's current framework
does not by itself settle for this programme:

- which universal configuration space nature uses;
- which indivisible law is physically correct;
- which compatible non-Markovian realizer, if any, should carry nomological path
  probabilities;
- a relativistic local-QFT native model reproducing the supplied AQFT comparator;
- background-free chronology;
- dynamical spacetime geometry or gravity.

Thus Barandes supplies a promising ontological form, not the missing universal
microphysics.

## 17. Relation to QFT

Paper 03 established an operational representation over a supplied locally
covariant AQFT setting. That result concerns algebras, instruments, causal
factorization, and probabilities on an already supplied spacetime. It does not
construct native beables.

A native lift of QFT must additionally address:

- the absence of simple local tensor-factor decompositions for type-III local
  algebras;
- normal localized instruments and their preparation costs;
- gauge constraints and relational observables;
- relativistic covariance without a preferred foliation;
- compatibility of actual configurations with Bell correlations and no
  signalling;
- one parent endpoint law for fields, apparatuses, references, and environments;
- empirical equivalence for complete local intervention networks.

Finite pointer models are calibrations, not evidence that field ontology is
finite, discrete, or lattice-like.

## 18. Distance to gravity

The native lift interface is necessary for the ontology question but is still far
from gravity. A gravity-bearing theory would additionally need:

1. no fixed comparator metric in the native law;
2. relational localization and causal structure derived rather than supplied;
3. gravitational and matter degrees of freedom in one common configuration and
   law;
4. a dynamical rule for geometry--matter reciprocity;
5. diffeomorphism/gauge descent;
6. operational clocks and rods with resource and backreaction accounting;
7. a controlled limit recovering local QFT on curved spacetime;
8. a controlled classical limit recovering Einstein dynamics or a clearly
   falsifiable alternative;
9. empirical predictions not used to choose the ontology or law.

The present operational clock work has not supplied these objects. In particular,
a quantum-reference-frame coordinate map is not automatically a physical clock,
and a physical clock record is not automatically spacetime geometry.

### 18.1 Primary-source routing

- [Barandes, Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/html/2507.21192v1): fixed configuration spaces, contingent standalone
  distributions, nomological transition laws, definite configurations, secondary
  Hilbert representations, system-relative division events, and the absence of a
  fundamental time-reversal requirement. It does not select the universal
  configuration or supply background-independent gravity.
- [Barandes, The Stochastic--Quantum Correspondence](https://arxiv.org/html/2302.10778v3): interference, decoherence, entanglement, emergeables,
  ordinary measurement interactions, and definite apparatus configurations in a
  stochastic reconstruction. It does not make an arbitrary operational pointer a
  native stable record.
- [Korbicz--Horodecki--Horodecki, Objectivity Through State Broadcasting](https://arxiv.org/abs/1305.3247): spectrum broadcasting as a structural
  operational criterion for objective information. It does not select an actual
  native trajectory, admit a Barandes conditioning division, or prove strong
  screening under a realizer.
- [Marvian--Spekkens, Information-theoretic WAY theorem](https://arxiv.org/abs/1212.3378): exact asymmetric measurements require a perfectly
  asymmetric resource under the theorem's programming hypotheses. It does not
  construct the reference device or a native ontology.
- [Barnum et al., Noncommuting mixed states cannot be broadcast](https://arxiv.org/abs/quant-ph/9511010): no-broadcasting boundary for general
  quantum information. It does not prohibit copying distinguishable classical
  labels.
- [Brown--Kuchař, Dust as a standard of space and time](https://arxiv.org/abs/gr-qc/9409001): physical reference matter in canonical gravity. It does
  not make reference fields costless or derive them from quantum-record algebra.
- [Dittrich, Partial and Complete Observables for Hamiltonian Constrained Systems](https://arxiv.org/abs/gr-qc/0507106): relational observables under
  canonical constraint hypotheses. It does not provide the missing quantum-gravity
  law.

## 19. Proposed theorem and control additions

Any future authorized pin should add the following theorem targets.

### NL1 — native/operational layer-separation theorem

Prove formally that operational centrality classifies the registered classical
output, not all native beables. Print the four layers and division coordinate.

### NL2 — complete endpoint-experiment pushforward theorem

For the declared native packet, derive the operational law for every registered
adaptive endpoint experiment and complete reader. Represent each transcript in
the final apparatus/controller configuration; do not assume a path measure.

### NL3 — one-parent-law theorem

Show that all comparison arms arise by physical settings and preparations inside
one fixed parent law.

### NL4 — realizer noninheritance theorem

Prove that the endpoint laws do not, by themselves, select a unique joint law over
intermediate configurations. If a realizer is added, print its selector and prove
all registered endpoint marginals agree. Keep an ontically actual trajectory
distinct from a probability distribution over possible trajectories.

### NL5 — native record transport theorem

Construct the native record function, future category, eraser category, and exact
stability/erasure witnesses.

### NL6 — class-relative nonselection theorem

Construct operationally equivalent, ontologically inequivalent lifts only within
an explicitly registered class, and print the interventions that would distinguish
them if licensed.

### NL7 — QFT/gravity nonpromotion theorem

Trace every spacetime, locality, time, and gravitational input to its source and
prove that no output coordinate silently promotes it.

Required hostile controls:

- treat a noncentral operator as automatically unreal;
- treat a native definite variable as automatically readable;
- derive a native law separately for each arm;
- absorb the contingent preparation into the law;
- define the native law by inverting opened quantum outcomes;
- insert a Markov kernel at a nondivision;
- silently add a unique path law or Kolmogorov tower;
- conflate a Barandes division with strong conditional screening;
- infer actualization from decoherence or broadcasting;
- infer a division from record stability;
- omit the physical reference from the native configuration;
- allow a hidden reference to change without backreaction;
- match one instrument but fail an adaptive policy;
- declare idle-extension underdetermination universal;
- identify empirical with ontological equivalence;
- promote the supplied AQFT metric to emergent geometry;
- treat a finite clock calibration as a lattice ontology.

## 20. Present disposition

The strongest honest conclusion is:

> The operational record architecture can be classified without choosing a native
> ontology. A Barandes-style ontology remains compatible in principle because
> native definiteness is not operational centrality. To become physics rather than
> an inverse representation, a native lift must freeze one configuration object,
> one parent indivisible endpoint law, one contingent preparation family, and one
> gauge-invariant endpoint-observation family, then reproduce every registered
> endpoint experiment out of sample. A unique multi-time realizer is an additional
> unselected input, not part of this minimum.

No such lift is constructed here. Therefore the live native coordinates remain:

```text
NATIVE-CONFIGURATION-UNSELECTED
NATIVE-ENDPOINT-LAW-UNSELECTED
NON-MARKOVIAN-REALIZER-UNSELECTED
PATH-PROBABILITIES-UNSPECIFIED
NATIVE-ACTUALITY-UNTESTED
NATIVE-STABLE-RECORD-UNTESTED
NATIVE-DIVISION-UNTESTED
RELATIVISTIC-QFT-NATIVE-LIFT-UNCONSTRUCTED
GRAVITY-UNCONSTRUCTED
```
