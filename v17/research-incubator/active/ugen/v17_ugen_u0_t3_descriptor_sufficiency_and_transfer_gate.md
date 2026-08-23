# ISP v17 — U-Gen U0-T3 descriptor-sufficiency and transfer gate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Implementation or target data bound:** no
**Native candidate constructed:** no

This gate repairs a possible unfairness in the U0-T3 fixture. A public packet
can fail in two opposite ways:

1. it can contain too little physical information for any candidate to make a
   defined prediction; or
2. it can contain so much calibrated response information that the held-out
   quantum process is already encoded.

Neither failure tests a native law. The purpose of this document is to type the
narrow middle: enough independently measured physical information to evaluate
a candidate's source map, but no target-equivalent predictive object.

The gate inherits the Nelson-control correction. It assumes no particle path,
Euclidean configuration, Brownian noise, Markov division, external time,
phase field, bundle, holonomy, Hilbert carrier, spatial lattice, continuum, or
microscopic geometry.

---

## 0. Exact physical question

> What must an experiment tell a proposed fundamental law about the apparatus
> and its contingent preparation so that a held-out prediction is well
> defined, without telling the law the held-out answer?

The answer cannot be “nothing.” A physical law needs a system and boundary
condition to act on. It also cannot be “the calibrated quantum process.” That
would be a compiler.

---

## 1. Typed objects

For experiment member $e$, let

$$
X_e^0
=
(X_{\mathrm{sys}},X_{\mathrm{bnd}},X_{\mathrm{proc}},X_{\mathrm{set}},
 X_{\mathrm{wire}},X_{\mathrm{read}},X_{\mathrm{met}},X_{\mathrm{prov}})
\tag{1}
$$

be the **common raw physical packet**. Its entries are measurement results,
procedures, apparatus descriptions, settings, records, uncertainties, and
provenance available before the target opens.

Let

$$
A_e^{\mathcal N}
\tag{2}
$$

be a **candidate-declared augmentation**: additional physical measurements or
derived coordinates that candidate $\mathcal N$ says its source map needs.
The augmentation must be requested, measured, provenance-typed, and frozen
without access to the held-out records.

The candidate supplies a source map

$$
\mathcal S_{\mathcal N}:
(X_e^0,A_e^{\mathcal N})
\longmapsto
Z_e^{\mathcal N},
\tag{3}
$$

where $Z_e^{\mathcal N}$ contains the candidate's declared system object,
configuration domain, contingent state, controls, readers, nuisance
parameters, and uncertainty set. Its invariant nomological rule then returns

$$
\widehat Q_e^{\mathcal N}
=
\mathcal N(Z_e^{\mathcal N}).
\tag{4}
$$

The held-out target $Q_e$ is not an argument of (3) or (4).

---

## 2. Four sufficiency notions that must not be conflated

### Definition DS.1 — metrological sufficiency

A measurement packet is metrologically sufficient for a declared measurand
when its measurement model, input quantities, calibration chain, uncertainty,
and influence quantities support that measurement result at the printed
scope.

This is the sense formalized by the BIPM vocabulary: a measurement model is a
relation among quantities known to be involved in the measurement. It is not
automatically a microscopic dynamics or a predictor of an unmeasured process.

### Definition DS.2 — source-map evaluability

The packet is evaluable for $\mathcal N$ when (3) is a total, measurable,
representation-stable rule on every admitted uncertainty realization and (4)
returns a normalized complete record law or a preregistered failure.

Evaluability asks whether the theory has been fully stated. It does not ask
whether the prediction is correct.

### Definition DS.3 — source identifiability

The source map is identifiable at tolerance $\eta$ when all
$Z,Z'\in\mathcal S_{\mathcal N}(X_e^0,A_e^{\mathcal N};\eta)$ give held-out
predictions within the registered internal diameter:

$$
\sup_{Z,Z'}
d_{\rm hold}
\bigl(\mathcal N(Z),\mathcal N(Z')\bigr)
\le \delta_{\rm src}.
\tag{5}
$$

If (5) fails, the candidate must return a prediction set or admit source-map
underdetermination. It may not pick the latent value that best fits $Q_e$.

### Definition DS.4 — predictive adequacy

After the target opens, the candidate is adequate only if its frozen
prediction or prediction set meets the preregistered complete-process score.

Adequacy is empirical. It cannot be awarded by metrological traceability,
evaluability, identifiability, elegance, or agreement on calibration alone.

---

## 3. Descriptor no-free-lunch theorem

### Theorem DS.A — a nontrivial fiber defeats packet-only guaranteed prediction

Let $B$ be one frozen public packet and suppose its admissible held-out fiber
contains $Q_0,Q_1$ with

$$
d_{\rm hold}(Q_0,Q_1)=\Delta>0.
\tag{6}
$$

For any packet-only prediction $\widehat Q=A(B)$,

$$
\max\!\left\{
d_{\rm hold}(\widehat Q,Q_0),
d_{\rm hold}(\widehat Q,Q_1)
\right\}
\ge \frac{\Delta}{2}.
\tag{7}
$$

### Proof

The triangle inequality gives

$$
\Delta
\le
d_{\rm hold}(Q_0,\widehat Q)
+d_{\rm hold}(\widehat Q,Q_1).
\tag{8}
$$

At least one summand is at least $\Delta/2$. $\square$

### Meaning

The theorem is not a no-go for prediction. It identifies where scientific
content must enter. A successful $\mathcal N$ must use a fixed law and a
physical source map that rule out the wrong fiber members. Merely restating
$B$, assigning one response by convention, or learning the target after
opening cannot do that.

---

## 4. Target-import theorem

### Theorem DS.B — source augmentation cannot contain the answer

Let

$$
B_e^{\mathcal N}=(X_e^0,A_e^{\mathcal N}).
$$

If a frozen T2 decoder, without invoking the proposed new rule $\mathcal N$,
recovers $Q_e$ from $B_e^{\mathcal N}$ within the target tolerance, then the
augmentation is target-equivalent and cannot support native-law credit.

### Proof

This is Definition T2.15 applied to the joint packet. Splitting a sufficient
payload between a common packet and a candidate augmentation does not alter
its decoder closure. $\square$

### Corollary DS.B.1

The following names create no exemption:

1. effective state;
2. apparatus response;
3. learned material coordinate;
4. calibrated phase;
5. digital twin;
6. latent context;
7. source fingerprint; or
8. physical metadata.

The verdict depends on what the joint object predicts, not its label.

---

## 5. Identifier-table theorem

### Proposition DS.C — opaque identities can encode every finite target family

For a finite experiment family $e_1,\ldots,e_n$ with unique opaque identity
tokens $\iota_1,\ldots,\iota_n$ and arbitrary target laws
$Q_1,\ldots,Q_n$, the table

$$
T(\iota_j)=Q_j
\tag{9}
$$

is a perfect predictor on that family.

It earns zero source-completion credit because the identity token has become
an address into the target table. Renaming the tokens changes nothing.

### Transfer consequence

A candidate that reads identity must also predict a separately built or
independently recalibrated implementation using its printed physical
descriptors, with no new invariant-law parameter and no newly fitted response
entry. Passing only known serial numbers is not uniformity.

---

## 6. Why one universal descriptor list cannot be asserted in advance

Configuration neutrality has a price. A field ontology may need material and
boundary fields; a relational ontology may need preparation and connection
relations; a finite carrier may need calibrated source categories; a
whole-process ontology may need a complete physical program description.

U0-T3 may freeze a common empirical core, but it cannot honestly declare that
the core is source-sufficient for every not-yet-written ontology. Doing so
would select a representation by fixture design.

The correct rule is candidate-relative but target-blind:

1. every candidate sees the same common raw packet;
2. every additional requested measurand must have an executable physical
   procedure;
3. the request and its scientific rationale freeze before target access;
4. the resulting raw measurement becomes available to all admitted
   candidates;
5. candidate-specific derived features must be reproducible from those common
   raw measurements;
6. T2 audits the joint packet, not each field in isolation; and
7. precision, experimental burden, and external theory are charged.

This does not permit an unlimited measurement oracle. The augmentation window,
measurement budget, and eligible apparatus state freeze before construction.

---

## 7. Two-envelope source protocol

### Envelope P — public physical evidence

The custodian freezes:

1. bill of materials and versioned physical assembly;
2. geometric, timing, thermal, electrical, optical, and material measurements
   relevant to registered procedures;
3. preparation and contingent boundary records;
4. raw actuator waveforms and setting records;
5. reader transfer, failure, saturation, and timing calibrations;
6. deliberately incomplete operational calibration;
7. measurement models, influence quantities, uncertainties, and traceability;
8. provenance and all training dependencies; and
9. the augmentation budget.

Envelope P contains neither the held-out record laws nor a quantum process
reconstruction sufficient to compute them.

### Envelope A — pretarget augmentation requests

Each request must print:

1. the proposed measurand;
2. why the source map needs it;
3. the physical measurement procedure;
4. expected units, range, resolution, and uncertainty;
5. whether an established external theory enters its inference;
6. the candidate coordinates that consume it;
7. the maximum allowed repeats and apparatus disturbance;
8. the T2 decoder and advice audit; and
9. the rule for failure or unavailable measurement.

The custodian adjudicates only admissibility and execution. It does not reveal
the target or optimize the measurement to help the candidate pass.

### Development-member freeze order

$$
\text{fixture grammar}
\prec
\text{Envelope P}
\prec
\text{augmentation requests}
\prec
\text{augmentation measurements}
\prec
\text{source map and law freeze}
\prec
\text{held-out run/opening}.
\tag{10}
$$

This order can test extrapolation from incomplete calibration to held-out
processes on one development implementation. It does **not** by itself show
that the nomological rule is uniform: the rule may have been specialized to
that implementation's public descriptors.

If an augmentation is requested after target access, the target split is
burned and must be replaced.

### Transfer-member freeze order

Uniform-law credit requires a second order:

$$
\text{law and source-map functional form}
\prec
\text{transfer-member identity and packet}
\prec
\text{predeclared augmentation measurements}
\prec
\text{source-state instantiation}
\prec
\text{held-out run/opening}.
\tag{11}
$$

The invariant law, descriptor types, measurement rules, uncertainty
treatment, and failure conditions are fixed before the transfer member is
known. Only contingent measured values may change. This distinction prevents
ordinary apparatus-specific model construction from being reported as a
uniform physical law, while still allowing the initial candidate to learn
from target-blind calibration evidence.

---

## 8. Parameter-origin ledger

Every number consumed by (3) or (4) receives exactly one primary class.

| class | meaning | admissibility |
|---|---|---|
| N | invariant nomological constant fixed across members | admissible if independently sourced and charged |
| S | system/material parameter measured before target | admissible through Envelope P/A |
| B | contingent boundary or preparation record | admissible; never merged with N |
| C | control/reader calibration parameter | admissible if T2-incomplete |
| U | nuisance or uncertainty coordinate marginalized prospectively | admissible if rule freezes |
| Q | target-derived effective parameter | forbidden for native credit |
| I | opaque identity/advice coordinate | forbidden unless reduced to physical descriptors and transfer-tested |

Changing a Q or I label to N, S, B, C, or U is a semantic defect.

---

## 9. Unobserved microscopic configurations

A realist candidate need not measure the actual microscopic configuration on
every run. It must state how unavailable configurations are handled.

Admissible options include:

1. a preparation-induced probability measure generated from Envelope P/A;
2. a symmetry or equilibrium measure derived by the fixed law;
3. a measured coarse boundary with the remaining variables marginalized; or
4. an explicit prediction set over unresolved source states.

Forbidden options include:

1. selecting the latent state after seeing the outcome;
2. inserting the target wavefunction as the preparation distribution;
3. assuming a maximum-entropy state because it gives the desired process;
4. assigning a separate hidden distribution to each held-out program; and
5. calling an unobservable target-fitted variable a contingent fact.

---

## 10. Descriptor transfer test

Let $e$ and $e'$ be two implementation members with different identity tokens
and independently measured packets. They share only the registered physical
type and the same invariant $\mathcal N$.

The transfer test requires

$$
\widehat Q_{e'}^{\mathcal N}
=
\mathcal N\!\left(
\mathcal S_{\mathcal N}(X_{e'}^0,A_{e'}^{\mathcal N})
\right)
\tag{12}
$$

with:

1. no target access for $e'$;
2. no new invariant parameter;
3. no identity-indexed branch;
4. the same measurement and uncertainty rules;
5. a preregistered failure outcome if $e'$ lies outside the claimed domain;
6. complete raw-record scoring; and
7. separate reporting of source-map and dynamical errors.

A second run of the same serial number tests stability. It does not by itself
test descriptor descent.

---

## 11. Hostile controls

1. exact target table keyed by serial number;
2. standard quantum process reconstructed from calibration;
3. target wavefunction renamed source state;
4. action/holonomy compiler renamed apparatus model;
5. material simulator trained on held-out data;
6. unrestricted augmentation oracle;
7. physically irrelevant high-precision real carrying advice;
8. candidate-specific raw data unavailable to rivals;
9. nuisance parameter fitted after target opening;
10. latent source state selected per outcome;
11. transfer member chosen after seeing predictions;
12. same-device repeat called implementation transfer;
13. missing descriptor treated as candidate falsification;
14. source-map failure hidden inside dynamical error;
15. metrological traceability called predictive adequacy;
16. agreement on one statistic substituted for complete records;
17. quantum comparator used to design the augmentation;
18. apparatus disturbance from augmentation left unrecorded;
19. unbounded measurement cost ignored; and
20. candidate-relative descriptors promoted to fundamental ontology.

---

## 12. Outcome ladder

| outcome | exact meaning |
|---|---|
| DS-R0 ILL-TYPED | a consumed descriptor or measurand lacks a physical procedure, uncertainty, or provenance |
| DS-R1 NON-EVALUABLE | the candidate cannot map the frozen packet to a unique prediction or registered prediction set |
| DS-R2 SOURCE-UNIDENTIFIED | allowed source-map uncertainty exceeds $\delta_{\rm src}$ and no honest set prediction is supplied |
| DS-R3 TARGET-IMPORTED | the joint packet is target-equivalent under T2 |
| DS-R4 IDENTITY-BOUND | prediction depends on an opaque implementation token and fails transfer typing |
| DS-R5 CLEANLY EVALUABLE | source map, augmentation, uncertainty, and complete prediction are frozen without target import |
| DS-R6 TRANSFER-READY | DS-R5 plus a separately built implementation and no-refit transfer protocol |

DS-R5 or DS-R6 is an admission state, not a physical success. Only later
held-out evaluation can test adequacy.

---

## 13. Consequence for U0-T3-R4

An implementation-bound R4 packet is not ready merely because apparatus files
exist. It must contain:

1. a common raw descriptor packet and measurement models;
2. a closed augmentation window and budget;
3. a parameter-origin ledger;
4. a T2 audit of every joint candidate packet;
5. at least one source-identifiability calculation;
6. a descriptor-transfer member;
7. target custody and evidence level;
8. complete failure and disturbance records; and
9. a separation between source-map failure and law failure.

No such implementation is bound by this document.

---

## 14. Authority wall

This gate does not authorize:

1. target data download or acquisition;
2. candidate-specific measurement execution;
3. a hardware programme;
4. a native candidate;
5. an official source freeze, pin, or review;
6. a scientific result;
7. a new paper or successor;
8. ontology selection;
9. N1B or another compiler repair; or
10. QFT, clock, spacetime, or gravity construction.

---

## 15. Primary-source boundary

The metrological distinctions above use the following institutional sources,
accessed 2026-08-23:

1. BIPM/JCGM, [VIM 3 definition 2.48: measurement
   model](https://jcgm.bipm.org/vim/en/2.48.html) and [definition 2.50: input
   quantity](https://jcgm.bipm.org/vim/en/2.50.html);
2. NIST, [Metrological Traceability: Frequently Asked Questions and NIST
   Policy](https://www.nist.gov/metrology/metrological-traceability).

These sources support the distinction between a declared measurement model,
its significant measured inputs, and the traceability of a measurement
result. They do not claim that calibration data determine an unmeasured
microscopic dynamics or held-out quantum process. The no-free-lunch,
target-import, and identifier-table statements in this file are internal
mathematical consequences of the printed U0-T2/T3 definitions, not claims
attributed to BIPM or NIST.

---

## 16. Maximum legitimate claim

> A nontrivial calibration fiber guarantees that no packet-only prediction is
> uniformly correct across all admissible completions. The missing selection
> must come from a fixed physical law and source map. A fair fixture therefore
> needs a common metrological core, a bounded target-blind augmentation
> protocol, explicit source identifiability, and implementation transfer.
> Conversely, any augmentation from which the target is already recoverable
> remains a compiler input. This gate makes a future native-law test fairer; it
> neither supplies nor refutes the law.
