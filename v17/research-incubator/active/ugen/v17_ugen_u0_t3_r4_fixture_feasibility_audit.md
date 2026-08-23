# ISP v17 — U-Gen U0-T3 R4 physical-fixture feasibility audit

**Status:** ACTIVE AUTHOR-SIDE FEASIBILITY AUDIT / NO IMPLEMENTATION BOUND
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Target data downloaded or evaluated:** no
**Hardware run or external contact:** none

This audit asks which real experimental architecture could eventually test a
native indivisible positive law under the U0-T3 fixture. It compares public
source descriptions only. It does not select vendors, acquire data, contact a
laboratory, freeze a source packet, or authorize a run.

The audit inherits the binding Nelson-control correction and the descriptor-
sufficiency gate. No experimental platform is promoted to microscopic
ontology.

---

## 0. Author-side verdict

No inspected historical data set is by itself an adequate T3-R4 native-law
fixture.

The strongest prospective architecture located in this bounded audit is a
**modular heralded-photon parent** in which one physical source and one raw
time-tagging/readout stack support both:

1. a single-system interference/marker/unmarker/adaptation cell; and
2. a common-source composite/Bell cell.

This is an author-side feasibility ranking among the inspected platforms, not
a scientific selection. The architecture would still require a prospective
or independently replicated target, two implementation members, a clean
augmentation window, and separately authorized source freeze and review.

Public historical resources remain useful as hostile controls and pipeline
rehearsals:

1. the NIST Bell archive for raw settings/outcomes/timing/failure handling;
2. the Bath photon-source data for source-diagnostic formats;
3. detailed entangled-photon construction literature for reproducible module
   manifests;
4. modern RFSoC/QICK work for waveform and raw-readout architecture;
5. the open classical-laser eraser kit for a classical apparatus mutant; and
6. process-tensor experiments for a target-complete quantum/tomography control.

None earns prospective native-law evidence.

---

## 1. Primary and institutional sources

The source claims in this audit are limited to the following records, accessed
2026-08-23.

1. BIPM/JCGM, [VIM 3 definition 2.48: measurement
   model](https://jcgm.bipm.org/vim/en/2.48.html) and
   [definition 2.50: input quantity](https://jcgm.bipm.org/vim/en/2.50.html).
2. NIST, [Metrological Traceability: Frequently Asked Questions and NIST
   Policy](https://www.nist.gov/metrology/metrological-traceability).
3. Dietrich Dehlinger and M. W. Mitchell,
   [“Entangled photon apparatus for the undergraduate
   laboratory”](https://arxiv.org/abs/quant-ph/0205172), published in
   *American Journal of Physics* 70, 898 (2002),
   [DOI 10.1119/1.1498859](https://doi.org/10.1119/1.1498859).
4. Si Xie and collaborators,
   [“Entangled Photon Pair Source Demonstrator using the Quantum
   Instrumentation Control Kit System”](https://arxiv.org/abs/2304.01190).
5. Robert Francis-Jones and Peter Mosley,
   [Dataset for All-fiber multiplexed source of high-purity single
   photons](https://researchdata.bath.ac.uk/312),
   [DOI 10.15125/BATH-00312](https://doi.org/10.15125/BATH-00312).
6. Lynden Shalm and collaborators,
   [“Strong Loophole-Free Test of Local
   Realism”](https://doi.org/10.1103/PhysRevLett.115.250402), with the
   [NIST Bell Test Research Software and Data
   archive](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data).
7. Gregory White and collaborators,
   [“Demonstration of non-Markovian process characterisation and control on a
   quantum processor”](https://doi.org/10.1038/s41467-020-20113-3).
8. Graham Gibson and collaborators,
   [CAD, PCB, results, and assembly files for a 3D-printable open-source
   quantum-eraser demonstration](https://doi.org/10.5281/zenodo.18001274),
   described by the University of Strathclyde
   [data record](https://pureportal.strath.ac.uk/en/datasets/cad-and-pcb-files-results-and-assembly-instructions-for-a-3d-prin/).
9. The U0-T1, T2, T3 fixture, fiber, and descriptor-sufficiency files in this
   repository.

This is source and feasibility reconstruction, not replication or acceptance
of any experimental result.

---

## 2. What “physically described” must mean

The BIPM definition of a measurement model is deliberately modest: it is a
mathematical relation among quantities known to be involved in a measurement.
NIST likewise requires traceability for significant input quantities in the
declared model and stresses that calibration of an instrument does not
automatically establish traceability for every later result produced with it.

For U0 this yields three ledgers, not one.

### M — measurement ledger

1. measurand;
2. measurement procedure;
3. input and influence quantities;
4. calibration chain;
5. uncertainty and covariance;
6. instrument/software version; and
7. disturbance and failure records.

### S — source-map ledger

1. which M quantities the candidate consumes;
2. how they define its system and contingent state;
3. unresolved physical coordinates and their marginalization;
4. invariant versus implementation-specific parameters;
5. source-identifiability diameter; and
6. candidate-declared augmentations.

### Q — sealed target ledger

1. raw settings and outcomes;
2. all time tags and failure categories;
3. calibration/held-out membership;
4. frozen trial and record maps;
5. conventional quantum comparator; and
6. hashes, uncertainty, and access log.

M supports measurement. S makes a candidate evaluable. Q tests it. Combining
the ledgers before freeze destroys the experiment.

---

## 3. Admission criteria for an R4 architecture

A real architecture must satisfy all of the following before source binding.

1. **One physical parent:** interference, marker, adaptive, product, and
   common-source programs arise by typed reconfiguration of one declared
   apparatus family rather than unrelated response tables.
2. **Raw event access:** source triggers, settings, clicks/no-clicks,
   multi-clicks, time tags, actuator monitors, invalid records, and drift
   monitors are retained.
3. **Physical controls:** voltage, displacement, pulse, orientation, geometry,
   or material settings replace ideal gates.
4. **Incomplete calibration:** detector/source/local calibration leaves a
   certified held-out process fiber.
5. **No target state:** no wavefunction, density matrix, process tensor,
   Jones/unitary table, action/phase response, or fitted visibility enters the
   candidate packet when jointly target-complete.
6. **Marker grammar:** unread marker, coherent unmarking, stable readout,
   conditional eraser, and later overwrite are physically distinct programs.
7. **Composite closure:** the same source and law support independent-product
   and common-source joint experiments.
8. **Adaptation:** a stable record can control a later actuator, with the full
   record retained.
9. **Depth:** at least two held-out composition depths exceed calibration.
10. **Transfer:** a second implementation is described by measured physical
    coordinates, not an identity lookup.
11. **Custody:** prospective or independent-replication target access occurs
    only after law and analysis freeze.
12. **Feasible resources:** build, acquisition, metrology, custody, and
    replication costs are explicit.

Failure of one criterion makes an architecture a control or partial fixture,
not a complete R4 member.

---

## 4. Anchor A — NIST loophole-free Bell archive

### What it genuinely provides

The NIST page exposes raw server data, processed data, acquisition programs,
and analysis programs for the published Bell experiment. It is unusually
strong for testing:

1. complete trial parsing;
2. setting and outcome retention;
3. timing and coincidence rules;
4. no-click/failure handling;
5. reproducible likelihood or Bell-function evaluation; and
6. the retrospective evidence label.

### Why it is not R4

1. the target and its qualitative quantum behavior have been public since
   2015;
2. no candidate can make a genuinely blind prediction of that historical
   outcome;
3. NIST explicitly warns that metadata may be missing and that the repository
   is a best-effort living collection;
4. the archive was assembled to reproduce a Bell analysis, not to provide a
   target-incomplete microscopic source packet for an ontology-neutral law;
5. an apparatus identity plus public paper knowledge can act as advice; and
6. there is no separately built transfer member under U0 custody.

### Verdict

```text
EVIDENCE LEVEL:          R — PUBLIC RETROSPECTIVE
PIPELINE VALUE:          VERY HIGH
NATIVE PREDICTION VALUE: NONE
R4 STATUS:               CONTROL ONLY
```

No NIST data are downloaded or evaluated here.

---

## 5. Anchor B — Bath all-fiber photon-source data

### What it provides

The Bath archive documents raw coincidence-count, heralded second-order
coherence, marginal-bandwidth, and related source-characterization data,
stored in MATLAB workspaces and linked to a published all-fiber multiplexed
source.

This is useful for typing:

1. source-rate and coincidence calibration;
2. heralding and accidental records;
3. marginal spectral diagnostics;
4. raw-versus-analysis-file provenance; and
5. source-only calibration that is not yet a complete process.

### Why it is not R4

1. it is a historical source-characterization data set, not a complete
   intervention family;
2. it lacks the T3 interference/marker/adaptive/composite grammar;
3. MATLAB aggregate workspaces are not guaranteed event-complete time-tag
   transcripts;
4. it carries no prospective target custody; and
5. it does not establish descriptor transfer to a second source.

### Verdict

```text
EVIDENCE LEVEL:          R — PUBLIC RETROSPECTIVE
SOURCE-CALIBRATION VALUE: HIGH
COMPLETE-PROCESS VALUE:   LOW
R4 STATUS:                SOURCE CONTROL ONLY
```

No Bath data are downloaded or evaluated here.

---

## 6. Anchor C — detailed entangled-photon laboratory construction

Dehlinger and Mitchell give detailed instructions for a two-crystal type-I
spontaneous-parametric-downconversion source, coincidence detection, strong
polarization correlations, and a Bell test executable on undergraduate-lab
timescales. This establishes that a modular source/readout architecture is not
purely hypothetical.

### Strengths

1. physical construction and operation are central;
2. the source and detectors can be described without calling them abstract
   gates;
3. coincidence events support both heralded single-system and common-source
   composite programs;
4. analyzer orientations are physical continuous controls; and
5. a separately rebuilt apparatus is conceivable.

### Deficits against T3

1. the published apparatus is not under current target custody;
2. its original acquisition path was not designed to retain every modern
   failure and timing field;
3. no marker/unmarker/stable-record grammar is supplied as one parent;
4. no descriptor-sufficiency or target-import audit exists; and
5. the construction article is not an immutable R4 hardware manifest.

### Verdict

```text
ARCHITECTURE VALUE:      HIGH
RETROSPECTIVE DATA VALUE: LIMITED
TRANSFER POTENTIAL:      PLAUSIBLE / UNTESTED
R4 STATUS:               DESIGN PRECEDENT ONLY
```

---

## 7. Anchor D — modern RFSoC/QICK source and readout

Xie and collaborators demonstrate an entangled-photon-pair source driven and
read out with RFSoC-FPGA hardware. Their reported controls include explicit
waveform generation, source driving, detector waveform digitization,
coincidence construction, and cross-channel timing characterization.

### Strengths

1. raw actuator waveforms can be versioned;
2. detector pulse shapes and time records can be retained below the final
   coincidence map;
3. feed-forward and randomized settings are programmable;
4. the same electronics can support source, interference, and composite
   cells; and
5. hardware/firmware identity and resource costs can be printed.

### Deficits against T3

1. the paper reports a feasibility demonstration, not a U0 custody protocol;
2. its time-bin state, visibility, and interferometer phase are interpreted
   through standard quantum optics;
3. no target-blind augmentation or non-equivalent-input audit exists;
4. no public complete prospective target is bound; and
5. cost and specialist infrastructure remain substantial despite the claimed
   reduction relative to commercial timing equipment.

### Verdict

```text
INSTRUMENTATION VALUE:   VERY HIGH
NATIVE INPUT STATUS:     UNRESOLVED
PROSPECTIVE POTENTIAL:   HIGH
R4 STATUS:               DESIGN PRECEDENT ONLY
```

---

## 8. Anchor E — open classical-laser eraser demonstrator

The 2025 Strathclyde/Glasgow data record provides build files for a
3D-printable educational apparatus. Its own description says that it uses
linear polarizers and **classical laser light** in a Young double-slit setup.

That makes it valuable, but in a different role.

### Correct role

1. apparatus-manifest rehearsal;
2. continuous actuator and image/readout calibration;
3. marker/unmarker terminology testing;
4. Maxwell/classical-wave comparator;
5. implementation-transfer rehearsal through reproducible build files; and
6. proof that “quantum eraser” in a title does not type a single-event quantum
   process.

### Incorrect role

It cannot establish native quantum-process generation, single-photon
indivisibility, Bell correlation, or record-level quantum actuality.

### Verdict

```text
APPARATUS REHEARSAL:     HIGH
CLASSICAL CONTROL VALUE: HIGH
QUANTUM TARGET VALUE:    NONE
R4 STATUS:               HOSTILE CLASSICAL CONTROL
```

No build archive or results are downloaded here.

---

## 9. Anchor F — White process-tensor experiments

The White experiments are exceptionally valuable demonstrations that
multi-time interventions and non-Markovian correlations matter. The 2020
paper reports data and code as available from the authors on reasonable
request and uses standard quantum operations, state/process tomography, and
process-tensor reconstruction.

### Correct role

1. complete-process grammar benchmark;
2. endpoint-Markov failure control;
3. adaptive/memory target design;
4. quantum process-tensor comparator; and
5. warning that local gate characterization can miss temporal correlations.

### Why it is not the first R4 implementation

1. the public interpretation is already quantum-process-laden;
2. reconstructed controls and process tensors can become target-complete
   inputs;
3. the hardware is accessed through an IBM quantum-device abstraction;
4. data are not an already frozen public raw U0 archive; and
5. implementation identity, pulse compilation, and device calibration create
   a large advice/leakage surface.

### Verdict

```text
PROCESS-GRAMMAR VALUE:   VERY HIGH
TARGET-IMPORT RISK:      VERY HIGH
FIRST-R4 SUITABILITY:    LOW
R4 STATUS:               QUANTUM/TOMOGRAPHY CONTROL
```

No data or code are requested.

---

## 10. Proposed prospective architecture — modular heralded-photon parent

The minimum credible common parent uses one versioned optical source family
and one raw acquisition stack.

### 10.1 Source and boundary layer

1. pump source with raw power, spectrum, timing, and stability monitors;
2. nonlinear pair-generation module with material, geometry, temperature,
   alignment, and failure records;
3. herald channel with raw detector waveform/time tag;
4. signal/idler connection grammar; and
5. source-only rate, accidental, spectrum, and second-order diagnostics.

No entangled state vector or density matrix is public candidate input.

### 10.2 Cell I branch

1. heralded signal enters a Mach--Zehnder or equivalent two-alternative
   interferometric module;
2. a voltage/displacement/orientation actuator supplies a continuous setting;
3. polarization or another reversible physical degree supplies an unamplified
   marker;
4. an inverse module supplies coherent unmarking before amplification;
5. a distinct reader amplifies the marker into a stable record;
6. later electronics can overwrite the stored bit without being called
   uncomputation;
7. a stable herald/marker record can drive a later Pockels cell or equivalent
   actuator; and
8. every detector pulse, time tag, setting, failure, and monitor is retained.

### 10.3 Cell C branch

1. route both source outputs to independently randomized analyzer modules;
2. retain complete local and joint raw events, including no-click and invalid
   categories;
3. include independent-source/product and no-source controls;
4. randomize settings through recorded physical electronics;
5. measure timing and geometry only for declared operational locality tests;
   and
6. score the full joint law before Bell functionals.

### 10.4 Depth and order branch

Use two physically distinct waveplate/retarder/actuator families in both
orders and at preregistered repeated depths. Their measured mechanical and
electrical settings are public; their ideal Jones or unitary matrices are not.

### 10.5 Transfer member

At least one of the following must be frozen before target opening:

1. independently built second interferometer;
2. replacement actuator from a different fabrication lot;
3. independently assembled second source; or
4. independent-laboratory replication using the same public type.

The same law must consume its measured descriptors without a new invariant
parameter or serial-number branch.

---

## 11. Public versus sealed coordinates for that architecture

### Public core

1. physical bill of materials and assembly graph;
2. material and geometric measurements with uncertainty;
3. source preparation and contingent monitor records;
4. raw voltage/current/pulse/displacement/orientation settings;
5. detector and time-tagger calibration, including failures;
6. blocked-arm, no-source, independent-source, and local reference runs;
7. classical feed-forward truth table and latency;
8. environmental and drift monitors;
9. measurement models and provenance; and
10. closed augmentation budget.

### Sealed

1. recombined single-event fringe records;
2. marker/unmarker/reader/overwrite complete laws;
3. order-sensitive sequences and held-out depths;
4. adaptive joint records;
5. common-source composite tables;
6. Bell-sensitive functionals derived from the complete law;
7. transfer-member held-outs;
8. standard quantum comparator; and
9. target hashes and access log.

### Forbidden public completion

1. fitted source state;
2. calibrated Jones/unitary matrices sufficient for the target;
3. phase-response or visibility curve;
4. process or detector-instrument tomography sufficient for held-outs;
5. target-trained optical simulation;
6. per-depth response table; and
7. serial-number advice.

---

## 12. Evidence ladder for eventual execution

### F0 — documentation rehearsal

Populate manifests from published papers and open hardware descriptions. No
target claim.

### F1 — classical apparatus mutant

Use a classical laser through the same or matched optics to validate
actuators, marker vocabulary, raw acquisition, drift, and Maxwell controls.
No quantum claim.

### F2 — retrospective event-pipeline rehearsal

Use public NIST/Bath-style records only to test parsers, complete-record maps,
uncertainty, and target custody software. No blindness or discovery claim.

### F3 — implementation-bound author packet

Bind actual hardware manifests, measurement models, costs, target custodian,
and prospective split. This is future T3-R4 and needs separate authority.

### F4 — independent leakage/source review

Review the T2 joint packet, descriptor sufficiency, marker semantics, transfer,
and evidence level. This is future T3-R5 and needs a separately authorized
pin.

### F5 — native candidate contest

Only after F4 may a candidate freeze and predict prospective targets. This is
U0-T4, not authorized here.

---

## 13. Why the architecture does not select photon ontology

The words pump, crystal, optical path, photon detector, and time tag describe
the laboratory at the resolution of its construction and records. U0 does not
thereby assume:

1. a photon follows one ontic path;
2. a Hilbert factor is fundamental;
3. a wavefunction is a material field;
4. laboratory space is emergent microscopic space;
5. a detector click reveals a pre-existing particle property;
6. program order is a global time; or
7. the configuration domain is discrete or continuous.

A candidate must supply and pay for its own referent while predicting the same
complete records.

---

## 14. Feasibility risks that remain open

1. a target-incomplete raw apparatus packet may still be insufficient for all
   proposed source maps;
2. source microstructure may drift faster than it can be characterized;
3. marker readout may disturb more modules than the grammar records;
4. an apparent coherent inverse may be only a fitted quantum label;
5. detector calibration may become target-complete jointly with source data;
6. no-click completeness and long time-tag streams may dominate storage;
7. implementation transfer may change several uncontrolled coordinates at
   once;
8. a second laboratory may be required for credible transfer;
9. a positive law may need physical descriptors that cannot be measured
   without opening or destroying the apparatus;
10. classical-wave and quantum single-event layers may be confounded;
11. prospective custody may be administratively difficult; and
12. the native candidate may remain absent after the fixture is ready.

These are scientific/protocol risks, not reasons to fill gaps with a quantum
state or Nelson mechanics.

---

## 15. Present disposition

```text
DESCRIPTOR-SUFFICIENCY GATE:      CONSTRUCTED AUTHOR-SIDE / NOT REVIEWED
EXISTING COMPLETE R4 DATA SET:    NOT LOCATED
NIST BELL ARCHIVE:                RETROSPECTIVE PIPELINE CONTROL
BATH SOURCE DATA:                 RETROSPECTIVE SOURCE CONTROL
OPEN CLASSICAL ERASER:            CLASSICAL APPARATUS MUTANT
WHITE PROCESS EXPERIMENTS:        QUANTUM/TOMOGRAPHY CONTROL
MODULAR HERALDED-PHOTON PARENT:   STRONGEST INSPECTED PROSPECTIVE ARCHITECTURE / UNBOUND
IMPLEMENTATION TRANSFER:          REQUIRED / NOT AVAILABLE
TARGET CUSTODY:                   REQUIRED / NOT ESTABLISHED
NATIVE CANDIDATE:                 ABSENT
DATA ACQUISITION OR HARDWARE:     NOT AUTHORIZED / NOT PERFORMED
OFFICIAL PIN / REVIEW / RESULT:   NONE
```

---

## 16. Authority wall

This audit does not authorize:

1. downloading or interpreting target data;
2. downloading build archives;
3. purchasing, assembling, or controlling hardware;
4. contacting authors, laboratories, or vendors;
5. binding an apparatus or custodian;
6. candidate construction or evaluation;
7. a source freeze, pin, or review panel;
8. a scientific result or publication;
9. a new paper or successor; or
10. QFT, clock, spacetime, or gravity work.

---

## 17. Maximum legitimate claim

> Existing public resources are sufficient to design and rehearse parts of a
> rigorous native-law fixture, but no inspected historical data set supplies
> the combination of target-blind physical descriptors, complete intervention
> records, prospective custody, marker semantics, composite closure, and
> implementation transfer required for T3-R4. A modular heralded-photon parent
> is the strongest prospective architecture found at author side. It is an
> unbound experimental design, not evidence for photon, stochastic, or Hilbert
> ontology and not a test result.
