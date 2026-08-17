# JRH — GRAVITY / COVARIANCE / ONTOLOGY HOSTILE REVIEW

**Seat:** G, frozen three-seat JRH panel.  
**Target:** commit `2f117f2`; candidate paper, source, transcript, and receipt.  
**Integrity at open:** all four SHA-256 values match the frozen protocol exactly.  
**Independence:** I did not read either other JRH review.  I did not import or
execute the candidate implementation.  The finite spot checks below were
rebuilt directly from the displayed objects.  
**Status:** candidate report until the panel is frozen and adjudicated.

## Grade and ruling

**GRADE: REJECT.**

The rejection is of the candidate **as a dynamic-spacetime seed**, not of its
ordinary quantum-instrument algebra.  The latter can remain a useful container.
The former is not instantiated by these artifacts.

The decisive defect is exact.  For fixed incoming geometry bit `g`, every
published output obeys

`(G', C', record) = (g xor z, z, z)`.

Consequently the incoming `g` and retained ordinary record determine every
declared geometry and collar value.  The only “later geometry probe” is the
identity function on that copied bit.  Erasing `G',C'` while retaining `g` and
the record changes none of the declared predictions: one reconstructs both on
demand.  Moreover, the input `collar` argument is unused, and the collar gate
does not compare two collar values through one successor law; it compares two
manually swapped Kraus families.  The alleged geometry/collar therefore fails
the pin's Necessity, No-smuggling, and Discriminator tests.

This is not repaired by saying that geometry may be a derived reading of the
record.  It may.  But then the construction must show that this reading governs
future adjacency, causal separation, transport, or a constraint in a way fixed
by a geometric rule.  It does none of those.  At present the highest honest
description is **a branch-resolved projective instrument with redundant binary
memory**.  “Geometry-labelled branch” is tolerable if explicitly nominal;
“dynamic geometry,” “backreacting spacetime,” and “actual carrier changes” are
not measured.

This triggers the pin's geometry kill condition and semantically fails G-C2 and
G-C4.  Therefore my highest licensed primary verdict for the object as pinned is
`JRH-INCONSISTENT`.  If the object is demoted to a non-geometric
record-conditioned instrument, `JRH-CONSISTENT-BUT-UNDERDETERMINED` survives—but
that is a different, weaker object.

## Independent finite spot checks

I independently obtained the following exact facts.

- For the declared connected simple graphs, `b1 = E - V + 1` gives `0,0,1`
  for `K2`, the three-vertex path, and the triangle.
- From the matrices printed in the implementation, `q_j q_i = diag(i,-i)`.
  This is nonidentity.
- For both `g=0` and `g=1`, the two outcome rows satisfy
  `G'=g xor record` and `C'=record`.  The reconstruction is bijective on the
  published rows.
- The balanced mean is `1/2`, which is not one of the toy's binary labels.
  That is a fact about the chosen alphabet, not an obstruction to a continuous
  expectation-sourced geometry.

The first two checks license a graph-cycle statement.  They do not license a
spacetime-curvature statement.  In particular, the code multiplies two
transports, not three oriented edge transports around a declared closed loop.
It supplies neither a gauge action nor a conjugacy-class/trace observable.  A
third identity edge could be supplied by convention, but it is not part of the
measured boundary object.  The matrix is thus an open-path product in the
delivered fixture, not an audited gauge-covariant holonomy.

## G1 — Does geometry do physical work?

### G-MAJOR-1 — the geometry and collar are predictively eliminable

**Exact object.**  In `successor`, the relation is merely copied into an output
key, `G'` is `g xor z`, and both `C'` and `record` are `z`.  There is no incoming
relation state `R`, no before/after adjacency comparison, and no carrier
rewrite.  Both output blocks remain `2 x 2`.  G-A2 checks the spelling of a
dictionary key and the matrix shape; it does not establish distinct geometric
operator algebras or a changed carrier.

G-C2 then defines `later_probe = {g: g}` and passes because two different labels
read as two different labels.  This is a declared readout, not independent
evidence of a lawful continuation.  A temperature, metric, or causal order may
be derived rather than independently ontic, but its geometric role must then be
demonstrated by nontrivial structural consequences.  The identity lookup does
not do that.

**Consequence.**  The direct-sum label has no predictive content beyond the
record already kept.  The toy cannot distinguish dynamic spacetime from a
laboratory measurement apparatus that writes an outcome bit into a second
classical register.  The paper's claims that the “actual spacetime carrier”
back-reacts and that later possibilities change are unsupported.

**Minimal repair.**  Choose one of two honest branches.

1. Declare `G=F(R,record)` a derived reading, remove it from the independent
   state inventory, and give a predeclared geometric rule that changes the
   *type or availability* of at least one later regional instrument (for
   example, causal reachability computed from `R`, not an arbitrary lookup).
2. Keep `G` as independent predictive state and exhibit two histories with the
   same complete retained record and relation data but different `G` that a
   fixed later experiment distinguishes.  The experiment and geometry-to-probe
   map must be frozen before constructing the two rows.

Until one is done, the dynamic-geometry headline is killed, not merely narrowed.

### G-MAJOR-2 — the collar gate does not test a collar

The `collar` input to `successor` is unused.  G-C4 constructs one Z-resolving
instrument and a separately swapped instrument and observes that they predict
different results on `|0>`.  Neither is obtained by evaluating one registered
law at `C=0` and `C=1`.  The receipt sentence “same relation and geometry with
distinct collar data” is therefore false as a description of its measured
object.

This matters ontologically.  In GR, an intrinsic spatial metric alone is not
enough initial data; extrinsic-curvature/canonical data and constraints are
needed.  But an arbitrary bit that selects between two laws demonstrates only
generic hidden memory.  It does not demonstrate conjugacy, a normal derivative,
a boundary collar, or geometric continuation.

**Repair:** define one function `J[R,G,C,S]` that actually reads `C`; give `C` a
transformation law and an independent geometric referent; impose a constraint
relating it to `G`; and show that quotienting `C` destroys prediction while no
smaller record statistic can restore it.  Merely wiring `C` into a branch switch
would still prove memory, not a gravitational collar.

### Fixed possibility space versus fixed physical stage

The paper is conceptually right that a fixed mathematical configuration space
does not imply a fixed realized spacetime.  Dynamic metrics are routinely
represented in a fixed state space.  The physical discriminator is whether the
realized geometry changes causal/metric relations and thereby changes lawful
future composition.

On that discriminator, the toy does not yet depart from Barandes's fixed-stage
setting.  It is exactly representable as a dilation onto a fixed direct sum with
a classical pointer bit.  Barandes explicitly treats Hilbert spaces and
dilations as secondary representations of stochastic processes
([Barandes, 2025](https://arxiv.org/abs/2507.21192)); that fact neither supplies
nor forbids dynamic geometry.  Likewise, quantum causal histories already use
CP maps between event algebras on a discrete causal pre-spacetime
([Hawkins–Markopoulou–Sahlmann](https://arxiv.org/abs/hep-th/0302111)).  JRH's
novel burden is the dynamical causal structure.  It is precisely the part not
implemented.

## G2 — Backreaction

### What survives

The paper makes one useful and correct structural point: an outcome-resolved
classical-quantum instrument can correlate a retained branch with another
register while remaining affine on density operators.  One need not use
preparation-decomposition metadata.  That is a valid way to avoid the specific
v15 nonlinear-mixture defect.

### What does not survive

Calling `z` “flux” or “realized transfer” is unlicensed.  It is a projective
measurement outcome.  There is no energy, momentum, stress tensor, current,
orientation, source, balance equation, or before/after conserved charge.  The
geometry response is a hard-coded XOR, not a response law derived from a
constraint.  Nothing tests whether every matter sector gravitates, whether the
response is universal, or whether two overlapping responses are consistent.

The mean-driven control is also a straw control for semiclassical gravity.  It
shows only that `1/2` is outside a binary label alphabet and that one chosen
threshold rule is nonlinear.  Semiclassical gravity sources a continuous
classical field with a stress-energy expectation; it does not require the
expectation value to be one of a microscopic binary outcome alphabet.  The
control may reject that particular binary threshold construction.  It does not
reject expectation-valued semiclassical backreaction as a class.

Before `z` can be called flux and `G'` backreaction, the next object needs at
least:

- an independently defined local charge/current on input and output boundaries;
- a branchwise balance or Ward identity, including what is stored in geometry;
- geometry validity constraints on every branch;
- a discrete Bianchi/closure relation across adjacent curvature carriers;
- equality under alternative unphysical cuts/refinements; and
- overlap gluing, not only commuting tensor factors on disjoint systems.

The continuum contracted Bianchi identity is what makes the Einstein equation
compatible with stress-energy conservation.  Discrete gravity does not make
this obligation disappear: exact Regge Bianchi identities relate rotations and
deficit angles on neighboring hinges
([Hamber–Kagel](https://arxiv.org/abs/gr-qc/0107031)).  One isolated binary flip
and one nonidentity matrix product supply no analogue.

### Covariance actually measured

The delivered covariance content is one cyclic actor relabelling of a literal
event record plus commutation of two tensor-factor projective instruments.
There is no alternative cut, overlapping move, refinement, foliation,
geometry-dependent causal separation, or deformation algebra.  The paper does
list these as future requirements, which is good.  But the abstract's phrase
“ontology plus jointness, locality, affinity, and covariance” must be narrowed
to **finite relabelling plus one disjoint tensor-product diamond**.

## G3 — Route to GR

The literature comparison makes the underdetermination worse, not better.

| route | primary literature supplies | missing from JRH | ruling |
|---|---|---|---|
| Regge calculus | Piecewise-flat simplicial geometry, edge-length data, deficit angles at codimension-two hinges, and a discrete Einstein action ([Regge, 1961](https://cds.cern.ch/record/472394)). | Dimension, signature, simplex inequalities, lengths/areas, dual loops, deficit angles, action variation, constraints, and continuum control. | An ordinary graph triangle is not Regge curvature. In four dimensions the triangle is a hinge; curvature is measured by transport around a dual loop through surrounding four-simplices, not merely around its three graph edges. |
| Causal-set action | A locally finite causal partial order, interval-count operators, manifoldlike sprinkling assumptions, and discreteness/nonlocality scales whose mean approximates `Box - R/2` ([Benincasa–Dowker](https://arxiv.org/abs/1001.2725)). | Partial order, interval census, dimension estimator, density/scale, manifoldlikeness, and a curvature limit. | JRH cannot borrow the causal-set action from generic pair records. Supplying these ingredients would be a substantive new theory. |
| General boundary | States on region boundaries, region amplitudes, orientation and gluing axioms; ordinary temporal evolution is a special case ([Oeckl](https://arxiv.org/abs/hep-th/0509122)). | A family over regions, a genuine boundary category, gluing equality, and amplitudes selected by a physical theory. | This supports JRH's **container shape**, not its weights or geometry. |
| Spin-foam/refinement route | Amplitudes on refined combinatorial histories and nontrivial cylindrical/refinement consistency; even “summing is refining” needs explicit consistency and combinatorial assumptions ([Rovelli–Smerlak](https://arxiv.org/abs/1010.5437)). | A two-complex, boundary representations/intertwiners, simplicity/geometry constraints, face/edge/vertex amplitudes, and a controlled limit. | “Resembles a spin foam” is analogy only. Exact invariance under every refinement would also risk selecting a topological theory rather than four-dimensional propagating gravity, so the intended coarse-graining notion must be specified. |
| Lovelock | In four dimensions, under smooth metric, locality, symmetry, divergence freedom, and at-most-second-derivative assumptions, the metric and Einstein tensors exhaust the relevant rank-two concomitants ([Lovelock, 1971](https://doi.org/10.1063/1.1665613)). | Every hypothesis: smooth metric, dimension, derivative order, divergence law, and continuum map. | It can constrain an assumed low-energy metric limit up to constants. It cannot select the microscopic JRH law. Treating it as selection before deriving those hypotheses imports GR. |
| Hojman–Kuchar–Teitelboim | Canonical geometrodynamics constrained by path/refoliation independence and the hypersurface-deformation structure ([HKT, 1976](https://doi.org/10.1016/0003-4916(76)90112-3)). | Spatial metric phase space, normal/tangential deformations, local constraints, structure functions, and a continuum limit. | A discrete closure test is a strong target. Copying the continuum algebra and its canonical variables would be target fitting, not microscopic derivation. |

Rideout and Sorkin are an especially relevant warning: causality plus a discrete
form of general covariance yields a **family** of sequential-growth laws, not a
unique dynamics
([Rideout–Sorkin](https://arxiv.org/abs/gr-qc/9904062)).  Thus even a successful
discrete-covariance gate should be expected to narrow a family, not magically
select one kernel.

### The smallest decisive next test

The smallest useful test is not a larger mode census.  It is a **three-actor
overlap/refinement square**:

1. Freeze one boundary with overlapping local supports `AB` and `BC`, actual
   input relation/transport data, and two alternative cuts/orderings.
2. Construct the unsplit regional instrument independently of the two
   factorizations.
3. Sum only over unobserved internal outcomes and require the three boundary
   instruments to agree up to one **predeclared** boundary transport computed
   from the input geometry—not a comparator built from the outputs.
4. Require the commutator of the two local deformations to close into that
   independently defined tangential transport, on every registered state and
   geometry label.
5. Include a downstream locality probe whose availability follows from the
   output relation/order grammar, plus a mutant that preserves outcome labels
   while breaking the geometric closure.

This is the minimum arena in which two moves overlap.  A subsequent
four-actor/tetrahedral-shell test should impose a product/closure relation among
neighboring face holonomies; that is the first credible Bianchi-style check.
Passing only the disjoint AB/CD diamond cannot discriminate covariance from
ordinary tensor-factor commutativity.

### “One local weight for transport and geometric deficit”

This is an untested ansatz, not a consequence of jointness.  GR plus matter is
described by one total action but with distinct gravitational and matter terms,
independent field content, and dimensionful/dimensionless coefficients.
Diffeomorphism invariance relates equations through Noether/Bianchi identities;
it does not say that the same numerical local weight must control matter
transport and deficit geometry.  JRH must define what “same” means—one amplitude
factor, one coupling, one representation label, or one conservation law—and
then compare against a two-weight rival.  Without that discriminator the ansatz
can hide exactly the coupling it hopes to derive.

## G4 — Constants and scale

The paper is right to split the names, but two gates overstate what was tested.

- **Affine-line coset/event choice:** untouched and unselected.  Nothing in JRH
  derives the old three-actor coset grammar.
- **Channel affine translation:** the exact unital and reset channels prove that
  CP/TP alone does not select the Bloch translation.  The reset channel is not
  marched through the entire A-E architecture, so the stronger phrase “both
  survive the architecture” is unmeasured.  Narrow the result accordingly or
  rerun every structural gate.
- **Cosmological constant:** presently untyped.  In a *separately assumed*
  unimodular effective theory it can occur as an integration/boundary datum;
  this depends on the field equations and their conservation/Bianchi structure,
  none of which v16 builds.  The status is therefore inherited conditional
  context, not a v16 consequence.  The boundary-data reading is discussed
  explicitly in the unimodular literature
  ([Buchmuller–Dragon](https://arxiv.org/abs/2203.15714)).
- **Newton/area scale:** the code sets `dimensionful_inputs = []` and gates that
  the list is empty.  This confirms by declaration that the toy contains no
  dimensionful datum.  It neither regenerates nor challenges the v6
  weight-counting no-go.  The licensed sentence is “JRH adds no input that
  breaches the existing scale wall,” not “JRH proves the wall.”
- **Dimensionless matter-gravity coupling:** still eligible in principle.
  Outcome probabilities can fix dimensionless numbers even when an absolute
  unit remains free.  What is missing is an independent matter-load observable
  and an independent geometric-response observable.  A minimal target would be
  an exact susceptibility such as a curvature/holonomy response divided by a
  standardized dimensionless boundary-energy change, measured at at least two
  loads and invariant under refinement.  The current `G'=g xor z` hard-codes a
  unit bit flip while `z` simultaneously names the record, so it cannot measure
  such a coupling.

## G5 — Consequences and deviations

The consequence table needs a full reclassification.

| topic | hostile classification | reason |
|---|---|---|
| joint dynamic-geometry instrument | **REFUSED** | Only an outcome-labelled CP instrument with predictively redundant `G,C` is constructed. |
| two-actor occurrence | **FORCED AS AN INSTRUMENT; OPEN AS GRAVITY** | A two-actor projective record update exists. No relation-state or causal geometry update is measured. |
| three actors | **FORCED AS FIRST CYCLE IN THE DECLARED SIMPLE-GRAPH FAMILY ONLY** | `b1=1` first occurs on the triangle. Curvature, gauge covariance, and the exclusion of multiedges are extra assumptions. |
| EPR/no-signalling | **SCOPED FINITE ADMISSIBILITY RESULT** | The registered CP comparison is compatible with no signalling; it says nothing about changing subsystem factorization or geometric causal cones. |
| global Hamiltonian | **NOT DERIVED** | The toy supplies no canonical generator; this does not establish a theorem that no global representation can exist. |
| affine-coset event rule | **OPEN/UNSELECTED** | Untouched. |
| channel affine term | **UNSELECTED BY CP/TP** | Full-architecture survival of the reset rival is not shown. |
| cosmological integration constant | **UNTYPED HERE** | No continuum metric equations, Bianchi identity, or unimodular constraint. |
| Newton/area scale | **NOT DERIVED** | No weight-nonzero datum is present; prior wall is not newly proved. |
| dimensionless gravitational coupling | **OPEN** | Matter load and geometric response are not independently defined. |
| GR limit | **OPEN, NOT YET CONDITIONAL** | The row lists missing requirements but supplies no named sufficient completion or map. |
| macroscopic geometry noise | **REFUSED/UNTYPED** | A binary pointer label is not a metric and there is no coarse-graining or scale. |
| geometry-induced decoherence | **PERMITTED ONLY AS ORDINARY RECORD-FORGETTING** | Tracing the duplicated branch register gives standard dephasing; no independent geometric degree of freedom causes it. |
| higher-curvature corrections | **OPEN/UNTYPED** | One graph cycle permits a matrix product; it does not instantiate a curvature action or coefficient. |
| modified dispersion | **REFUSED/UNTYPED** | There is no momentum, energy, propagation cone, continuum clock, or dispersion relation. |
| Lorentz violation | **REFUSED/UNTYPED** | Discreteness alone does not force it; Poisson causal-set discreteness can avoid selecting a frame ([Bombelli–Henson–Sorkin](https://arxiv.org/abs/gr-qc/0605006)). |
| forced QFT/GR deviation | **NO DEVIATION IS LICENSED; FAMILY-INVARIANT THEOREM NOT PROVED** | No QFT/GR comparison observable is defined. |

G-F4 is logically invalid as an exact deviation theorem.  Its whole predicate
is `no_forced_deviation = rival_diff`.  Two laws having different microscopic
record statistics does **not** imply that they lack some common dimensionless
deviation from QFT or GR; both could share one.  Nor were all surviving laws or
any QFT/GR comparator enumerated.  What *is* warranted is the epistemic wall:
this unit licenses no deviation.  That is not evidence for empirical
equivalence, and it should not be presented as a family-invariant computation.

Likewise, “finite loops allow higher-curvature terms” is too strong.  A loop
allows one to define a transport product after the missing orientation/gauge
data are supplied.  Higher-curvature **gravitational** terms require a typed
curvature observable and an action.  “Outcome-correlated metric noise” makes the
same leap from a pointer bit to a metric.  “Species-dependent dispersion” is
two leaps further: no species and no dispersion are constructed.

## New indirect consequence: a feed-forward equivalence no-go

The artifact implies a negative result not stated in the paper:

> **Within every experiment declared in this fixture, the alleged
> backreacting-geometry model is prediction-equivalent to a standard projective
> instrument followed by classical feed-forward from its retained record.**

Proof: retain the input `g` and outcome record `z`; reconstruct `G'=g xor z` and
`C'=z`; answer the only later probe by returning reconstructed `G'`.  This
reproduces every published geometry/collar row exactly.  No geometric state is
required.

Two consequences follow.

1. The purity loss after “ignoring geometry” cannot be attributed to gravity;
   it is exactly the loss obtained by forgetting an ordinary measurement
   record.
2. No observation in the current arena can decide whether spacetime
   back-reacted or an engineer copied a detector bit into a controller.  A
   successor must break this equivalence with an independently constrained
   locality/transport response.

This no-go does not say outcome-resolved backreaction is impossible.  It says
the present toy has not instantiated it.

## Required repairs before a successor can promote

1. Replace the copied relation label with an actual `R -> R'` carrier update.
2. Either derive geometry from `R` and measure a rule-governed future causal
   consequence, or give `G` independent predictive content.
3. Replace G-C4 with one collar-dependent successor law; give the collar a
   geometric transformation and constraint.
4. Define branch flux independently of the outcome name and impose exact
   conservation plus a geometry response law.
5. Run the overlapping three-actor refinement/deformation square and then a
   neighboring-loop Bianchi closure test.
6. Demote the two-matrix product from curvature/holonomy until orientation,
   the closing edge, gauge covariance, and a gauge-invariant observable exist.
7. Replace G-F4 by an actual observable/family comparison or by a prose scope
   refusal; do not infer it from `rival_diff`.
8. Reclassify metric noise, higher curvature, dispersion, Lorentz violation,
   and the GR limit as untyped/open until their referents exist.

## Highest licensed verdicts

- **Primary, for the pinned dynamic-spacetime object:** `JRH-INCONSISTENT`.
- **Primary after an explicit non-geometric demotion:**
  `JRH-CONSISTENT-BUT-UNDERDETERMINED` for a branch-resolved record instrument.
- **Arity:** `L2-REFUSED` as a demonstrated geometry-changing occurrence; an L2
  CP record instrument exists.
- **Loop:** `TRIANGLE-FIRST-LOOP-NOT-FIRST-EVENT`, scoped to the registered
  connected simple graphs; no curvature claim attaches.
- **Scale:** no Newton/area scale and no cosmological value are derived.
- **Deviation:** the registered
  `NO-FORCED-QFT-GR-DEVIATION-IN-REGISTERED-FAMILY` is **not** machine-licensed
  by G-F4.  The highest honest sentence is: **no QFT/GR deviation is typed or
  licensed by this unit.**

The joint-history instrument remains a plausible language in which to ask the
right question.  The current finite object answers only the easier question:
can a quantum outcome be copied into labels called relation, geometry, collar,
and record?  Yes.  The missing physics is the non-copyable law that makes those
labels geometry.
