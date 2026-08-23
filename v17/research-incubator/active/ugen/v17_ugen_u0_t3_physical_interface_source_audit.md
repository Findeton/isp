# ISP v17 — U-Gen U0-T3 physical-interface source audit

**Status:** ACTIVE AUTHOR-SIDE PRIMARY-SOURCE AUDIT / NO FIXTURE RESULT
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review opened:** no

This audit reconstructs the source constraints for a configuration-neutral
complete-process fixture. Its purpose is to prevent U0-T3 from replacing bare
gate names with equally circular apparatus labels.

The fixture must describe what experimenters prepare, change, connect, and
record, while leaving open what microscopic configurations exist and which law
generates the records.

This audit inherits the binding Nelson-control correction. N1/N1A contribute
only hostile prior-art lessons. No trajectory, Euclidean configuration,
Brownian noise, Markov division, external time, diffusion scale, mean-Newton
law, phase target, bundle, or holonomy is a U0-T3 premise. G1 remains an
action/holonomy compiler control, and MG0 remains a gravity-discriminator
preflight only.

---

## 1. Primary sources fixed for this audit

The claims below are limited to these sources and versions or published
identifiers, accessed on 2026-08-23.

1. Robert W. Spekkens,
   [“Contextuality for preparations, transformations, and unsharp
   measurements”](https://arxiv.org/abs/quant-ph/0406166),
   published as
   [Phys. Rev. A 71, 052108](https://doi.org/10.1103/PhysRevA.71.052108).
2. Matthew F. Pusey, Lídia del Rio, and Bettina Meyer,
   [“Contextuality without access to a tomographically complete
   set”](https://arxiv.org/abs/1904.08699).
3. Felix A. Pollock, César Rodríguez-Rosario, Thomas Frauenheim,
   Mauro Paternostro, and Kavan Modi,
   [“Non-Markovian quantum processes: complete framework and efficient
   characterisation”](https://arxiv.org/abs/1512.00589),
   published as
   [Phys. Rev. A 97, 012127](https://doi.org/10.1103/PhysRevA.97.012127).
4. Gregory A. L. White, Felix A. Pollock, Lloyd C. L. Hollenberg,
   Kavan Modi, and Charles D. Hill,
   [“Non-Markovian Quantum Process
   Tomography”](https://arxiv.org/abs/2106.11722).
5. Gregory A. L. White and collaborators,
   [“Demonstration of non-Markovian process characterisation and control on
   a quantum processor”](https://doi.org/10.1038/s41467-020-20113-3),
   *Nature Communications* **11**, 6301 (2020).
6. Paul G. Kwiat, Aephraim M. Steinberg, and Raymond Y. Chiao,
   [“Observation of a quantum eraser: A revival of coherence in a two-photon
   interference experiment”](https://doi.org/10.1103/PhysRevA.45.7729),
   *Phys. Rev. A* **45**, 7729 (1992).
7. Thomas J. Herzog, Paul G. Kwiat, Harald Weinfurter, and Anton Zeilinger,
   [“Complementarity and the Quantum
   Eraser”](https://doi.org/10.1103/PhysRevLett.75.3034),
   *Phys. Rev. Lett.* **75**, 3034 (1995).
8. Lynden K. Shalm and collaborators,
   [“Strong Loophole-Free Test of Local
   Realism”](https://doi.org/10.1103/PhysRevLett.115.250402),
   *Phys. Rev. Lett.* **115**, 250402 (2015), with the
   [NIST software and raw-data
   repository](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data)
   and archived data DOI
   [10.5060/D2JW8BTT](https://doi.org/10.5060/D2JW8BTT).
9. Pascal Cerfontaine, René Otten, and Hendrik Bluhm,
   [“Self-Consistent Calibration of Quantum Gate
   Sets”](https://arxiv.org/abs/1906.00950).
10. The version-bound Barandes and information-equivalence sources audited in
    v17_ugen_u0_barandes_source_completion_audit.md and
    v17_ugen_u0_t2_information_equivalence_source_audit.md.

This is a scope reconstruction, not an independent replication or acceptance
of every source result.

---

## 2. Procedures first, ontology later

Spekkens's operational framework treats preparations, transformations, and
measurements as laboratory procedures and defines equivalence through their
observable statistics. This supports a fixture whose primitive public
language is procedural:

$$
\text{prepare}\;+\;\text{intervene}\;+\;\text{connect}
\;+\;\text{read}
\longmapsto
\text{record transcript}.
$$

It does not imply that procedures are the ultimate ontology. A candidate may
later propose finite, continuous, field-like, relational, contextual, or
whole-process configurations, provided that the proposal generates the same
registered physical interface without importing its target.

The source also blocks one shortcut: two laboratory implementations are not
fully equivalent merely because one preferred measurement cannot distinguish
them. Full operational equivalence quantifies over the admitted continuation
and reader grammar.

### U0-T3 terminology correction

Let $\mathfrak T_{\rm cal}$ be the finite or otherwise bounded tester family
used before target opening. U0-T3 may assert only

$$
x\simeq_{\rm cal}y
\quad\Longleftrightarrow\quad
\text{all testers in }\mathfrak T_{\rm cal}
\text{ agree within registered uncertainty}.
\tag{1}
$$

It must not silently replace $\simeq_{\rm cal}$ by complete operational
equivalence.

Pusey, del Rio, and Meyer show why the distinction matters: an assumed
tomographically complete set can miss extra degrees of freedom that break a
putative operational equivalence. Their result is about contextuality tests,
but the methodological lesson is general. Unknown continuations remain part
of the calibration fiber rather than being declared absent.

**Fixture consequence:** use calibration-equivalence classes as typed public
inputs and place their untested refinements in the held-out surface.

---

## 3. Complete processes require interventions, not passive trajectories

The process-tensor framework maps sequences of inserted operations to later
states or record probabilities and includes correlations that endpoint
dynamics can miss. White and collaborators experimentally demonstrate why
this matters: a Markovian gate-set description can be predictively inadequate
when the device carries temporal correlations.

For U0-T3 the empirical object is therefore not a passive time series. It is
a family

$$
\mathbf P:
a\longmapsto P(\,\cdot\mid a),
\tag{2}
$$

where $a$ is a physically executable intervention program and the output is
the complete raw-record law.

The experimental process-tensor literature also supplies two honesty walls.

1. A tomographically complete control basis plus all corresponding outcomes
   reconstructs a complete quantum process at the stated scope. Supplying it
   to a candidate is target import under U0-T2.
2. Real experiments often access only a restricted span of controls. White
   and collaborators explicitly distinguish restricted process tensors from a
   fully complete control basis. A restricted reconstruction must not be
   advertised as complete.

The 2020 superconducting-device experiment used thousands of sequences and
standard quantum pulse parameterizations to characterize a restricted
multi-time process. It is a useful empirical comparator, not a native U0 input
packet: the control basis, gate interpretation, tomography, and reconstructed
process are already quantum-model-laden.

**Fixture consequence:** calibration may use physical actuator waveforms,
source diagnostics, detector response, and deliberately incomplete local
response tests. It may not contain an informationally complete process
reconstruction.

---

## 4. Physical controls are not gate names

Self-consistent calibration and gate-set tomography show that pulse sequences
can identify many coherent error coordinates and jointly characterize a gate
set despite preparation-and-measurement uncertainty. This is experimentally
valuable, but information-equivalence matters more than the word
“calibration.”

U0-T3 distinguishes:

### Admissible apparatus calibration

1. actuator voltage, current, displacement, pulse envelope, timing record, or
   material setting;
2. source rate, spectrum, stability, and blocked-channel diagnostics;
3. detector dark counts, dead time, saturation, efficiency, and raw record
   encoding;
4. classical feed-forward truth table and latency;
5. connectivity and independently measured loss; and
6. environmental monitor records and uncertainty.

### Target-complete calibration

1. a gate or process matrix reconstructed for every control;
2. a tomographically complete gate set fixing all registered circuits;
3. a process tensor or comb;
4. an action, phase, Jones matrix, unitary, Hamiltonian, or holonomy response
   sufficient to compile the target; and
5. a pulse model fitted against the held-out process and then presented as
   physical source data.

The distinction is operational, not lexical. A physical waveform is not
automatically clean, and a long apparatus description is not automatically
answer import.

An apparatus serial number or version label is likewise not a physical
explanation. It may key provenance and custody, but if a candidate branches on
an otherwise opaque identity token, that token is charged as experiment-
specific advice. A native test therefore needs descriptor-based transfer to a
separately built or independently recalibrated implementation whose held-out
composition records were unavailable at candidate freeze.

**Fixture consequence:** every control field receives a provenance node and a
T2 decoder-closure audit.

---

## 5. A reversible marker is not an erased stable record

Quantum-eraser experiments demonstrate that interference can be lost when
alternatives become distinguishable through another physical degree of
freedom and can reappear in an appropriate conditional or recombined
measurement context. Kwiat, Steinberg, and Chiao used polarization to mark
alternatives and polarizers before detection to remove that distinguishability
for the registered coincidence records. Herzog and collaborators used
entangled partners to control which-alternative information.

These experiments do not license the statement

$$
\text{delete an amplified classical record}
\Longrightarrow
\text{restore the earlier coherent process}.
\tag{3}
$$

At least four operations must be separately typed.

1. **Unamplified marker:** a degree of freedom becomes correlated with an
   alternative but no stable complete record is yet formed.
2. **Coherent unmarking:** a licensed reversible operation removes the
   distinguishability before amplification.
3. **Conditional eraser reader:** a later reader groups or conditions records
   in a basis that reveals complementary interference subensembles.
4. **Stable-record overwrite:** an amplified record is physically erased or
   overwritten after formation; this does not by itself reverse the larger
   record-forming interaction.

Unconditional and conditional distributions must both be reported. A
postselected fringe in two complementary subensembles is not an unconditional
retrocausal restoration.

**Fixture consequence:** U0-T3 must include unmarked, marked-unread,
coherently-unmarked, conditionally read, stably recorded, and
record-overwritten programs as distinct physical types.

---

## 6. Composite records must include settings, failures, and every trial

The Shalm and collaborators Bell experiment combined random setting choices,
spacelike-separated measurement events, high-efficiency detectors, raw time
records, and a hypothesis test that did not require fair sampling. NIST
published raw data and analysis software.

U0-T3 does not use this experiment to assume a fundamental spacetime, photon
ontology, or quantum state. It uses it to specify what a serious composite
record packet looks like:

$$
(x,y,a,b,\tau_A,\tau_B,
 \text{source trigger},\text{failure flags},\text{monitor data}).
\tag{4}
$$

Here $x,y$ are recorded physical settings and $a,b$ include no-click and other
registered outcomes. Geometry and timing are apparatus records with
uncertainties. They can test signalling or locality claims only at their
declared experimental scope.

Local marginals do not determine the joint law. Uniform settings and local
records can be shared by independent, quantum, local-hidden, nonsignalling,
and whole-program positive completions.

**Fixture consequence:** the composite held-out surface includes complete
joint transcripts, null/product controls, setting randomization, losses, and
no-signalling marginals. Postselected coincidence tables alone are
insufficient.

---

## 7. Target custody has three evidential levels

A fixture must distinguish data secrecy from scientific novelty.

### Level R — public retrospective replay

Published or public raw data may test parsers, likelihoods, resource ledgers,
and known controls. Because candidate designers can know the answer, success
earns no prospective prediction claim.

### Level B — administratively blind archive

An existing data partition may be hidden from the construction team by a
custodian. This blocks direct tuning within the protocol but does not erase
the broader community's prior knowledge of standard quantum behavior.

### Level P — prospective prediction

A candidate and analysis freeze before a new apparatus setting, later run, or
independent replication is opened. Only this level can support a genuinely
new empirical-wedge claim.

U0-T3 creates no Level-P experiment and acquires no data. It merely requires
the distinction in any future evaluation.

---

## 8. Configuration neutrality is not apparatus vagueness

The public packet may contain a finite wiring diagram, spatial metrology,
clock readings, pulse samples, detector labels, or continuous knob values.
These describe the laboratory procedure. They do not force the candidate's
microscopic configuration object to be:

1. the vertices of the wiring diagram;
2. positions in the laboratory;
3. particle trajectories;
4. a continuous field;
5. a Hilbert vector;
6. a hidden-state automaton; or
7. a spacetime history.

The candidate must declare its own configuration type and the source map from
the public packet. The fixture judges only the resulting complete record law
and charged resources.

Conversely, configuration neutrality does not permit an untyped symbol such
as $H$, $T$, “beam splitter,” or “measurement.” Each physical module must
include its actuator, connectable ports, calibration procedure, uncertainty,
raw record interface, and provenance.

---

## 9. Source-conditioned fixture coordinates

The sources support the following public interface:

$$
\mathcal X_E=
(\mathsf{Sys},\mathsf{Bnd},\mathsf{Proc},\mathsf{Port},\mathsf{Set},\mathsf{Wire},
 \mathsf{Cal},\mathsf{Read},\mathsf{Rec},\mathsf{Prov},
 \mathsf{Cost}).
\tag{5}
$$

1. $\mathsf{Sys}$ identifies the physical apparatus/system family through
   independently measured descriptors, not a microscopic ontology.
2. $\mathsf{Bnd}$ separates the preparation procedure and contingent
   pre-program records from invariant nomological data.
3. $\mathsf{Proc}$ contains concrete preparation, control, connection, and
   reader procedures.
4. $\mathsf{Port}$ types physical connectability without naming a microscopic
   carrier.
5. $\mathsf{Set}$ contains actuator and setting records with units and
   uncertainty.
6. $\mathsf{Wire}$ contains executable laboratory composition and classical
   feed-forward.
7. $\mathsf{Cal}$ contains only the frozen incomplete calibration split.
8. $\mathsf{Read}$ specifies physical record formation.
9. $\mathsf{Rec}$ specifies complete raw transcripts, including failures.
10. $\mathsf{Prov}$ is the T2 provenance graph.
11. $\mathsf{Cost}$ charges information, precision, memory, communication, and
   external computation.

$\mathsf{Bnd}$ may contain source triggers, temperatures, material loads,
reset outcomes, or other actually available preparation records. It may not
be a target wavefunction or process object supplied under the name “state.”

Program order is an experimenter-supplied executable dependency. It is not an
emergent chronology or a fundamental global clock.

---

## 10. What U0-T3 must demonstrate mathematically

Before it can be called a usable fixture, U0-T3 must show:

1. the physical system family, contingent boundary data, every public
   procedure, and every record are typed and kept distinct from the law;
2. calibration equivalence is not promoted to full operational equivalence;
3. no target-complete quantum/action/tomography object enters the candidate
   packet;
4. the calibration fiber contains at least two complete positive laws that
   satisfy all frozen public constraints and differ on a held-out program;
5. the difference survives the complete-record quotient rather than a label
   convention;
6. causal prefix records do not depend on later randomized settings in the
   comparator family;
7. stable records, unamplified markers, coherent unmarking, conditional
   eraser readers, and overwrite are distinct;
8. composite targets include all settings, outcomes, losses, and failures;
9. finite, continuous, contextual, whole-program, quantum-compiler, and
   supplied-parent controls can all enter without selecting the ontology; and
10. retrospective, blind-archive, and prospective evidence are never merged.

None of these conditions constructs the missing source-completion map.

---

## 11. Present source verdict

$$
\begin{array}{ll}
\text{PROCEDURE-FIRST PUBLIC LANGUAGE} & \text{SOURCE-SUPPORTED}\\
\text{FULL OPERATIONAL EQUIVALENCE FROM FINITE CALIBRATION}
& \text{NOT LICENSED}\\
\text{INTERVENTION-COMPLETE TARGET} & \text{REQUIRED}\\
\text{COMPLETE PROCESS TOMOGRAPHY AS CANDIDATE INPUT}
& \text{FORBIDDEN / COMPILER}\\
\text{RESTRICTED CALIBRATION} & \text{ALLOWED IF FIBER REMAINS}\\
\text{REVERSIBLE MARKER / STABLE RECORD} & \text{DISTINCT}\\
\text{COMPLETE COMPOSITE TRANSCRIPT} & \text{REQUIRED}\\
\text{MICROSCOPIC CONFIGURATION FORM} & \text{UNSELECTED}\\
\text{NATIVE LAW} & \text{ABSENT}\\
\text{OFFICIAL PIN / REVIEW / RESULT} & \text{NONE}
\end{array}
$$

---

## 12. Maximum legitimate claim

> Primary sources support a configuration-neutral fixture built from typed
> physical procedures, incomplete calibration-equivalence classes, inserted
> interventions, and complete raw records. They also show why complete
> tomography would import the target, why an unamplified reversible marker is
> not an erased stable record, and why composite evaluation must retain
> settings, losses, timing, and failures. These constraints define an honest
> experimental interface; they neither construct nor refute a native
> indivisible stochastic law.
