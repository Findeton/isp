# V17 Paper 04B empirical-feasibility census

Date: 2026-08-23

Status: **PRIVATE / NONBINDING / NOT A PIN / NO SUCCESSOR AUTHORIZED**

Purpose: determine whether an existing laboratory result could support a repaired
Paper 04B test without pretending that ordinary clock calibration is relational
time, that relational reparametrization is an autonomous clock, or that public
results already used for model selection are fresh held-out evidence.

No raw experimental dataset was downloaded or opened during this census. Public
articles, abstracts, repository metadata, and file manifests were inspected.

## 1. The empirical target after the pre-construction failure

The failed pin conflated three different objects:

1. `gamma`: a redundant coordinate or gauge/orbit label;
2. `tau`: a physically informative reading or duration supplied by an external
   reference clock; and
3. `u_tau`: an externally timed control, stop, acquisition, or readout schedule.

An empirical clock record `R` should not be independent of `tau`; a clock is
useful precisely because `R` is informative about `tau`. The physically relevant
screening question for registered system/comparator outputs `Y` and context `E`
is instead

$$
Y \perp\!\!\!\perp \tau \mid (R,E),
$$

within a frozen local validity domain and against no-clock, mistuned, record-
scrambled, metadata-only, and externally scheduled controls. This means that,
after conditioning on the physical record and legitimate context, the external
reference reading adds no predictive information for the registered outputs.
It does **not** mean that the complete experiment is independent of physical
duration.

The stronger one-parent requirement is additional: the same fixed physical
parent must yield both a clock-neutral/constrained description and a finite
autonomous realization with identical complete transcript laws. A laboratory
clock alone does not establish this.

## 2. Evidence tiers

| Tier | Meaning | Permitted claim |
|---|---|---|
| E0 | simulation or internally generated pseudo-data | mathematics/conformance only |
| E1 | retrospective reproduction of published data/results | calibration and feasibility only |
| E2 | analysis frozen before first access to sequestered pre-existing raw values, with all publication-level contamination disclosed | limited quasi-held-out evidence, not clean prospective confirmation |
| E3 | prospective independent acquisition after model, task, readers, controls, and decision rule freeze | promotion-bearing empirical evidence |

Once a public result is used to select the family, estimator, parent, or target,
the same result cannot later be relabeled E3. Merely refraining from opening its
raw file does not erase knowledge of the publication.

## 3. Candidate census

| Candidate | What reality supplies | Persistent internal record? | Fixed/autonomous after initialization? | Relational replacement test? | One parent / two routes? | Open data | Honest role |
|---|---|---:|---:|---:|---:|---:|---|
| Moreva et al. 2014, two-photon Page--Wootters illustration | static entangled polarization correlations; one photon labels the other's conditional state | no retained multi-tick record in one run | no; externally prepared and measured ensemble | illustrates conditional time but not record sufficiency or external-schedule removal | no | no raw-data repository found | conceptual/quantum-correlation control, E1 |
| Moreva et al. 2017, multitime correlations | photon position as clock plus polarization memories; Page--Wootters two-time correlations and Leggett--Garg test | measurement memories exist, but not a self-running retained clock stream | no; engineered optical ensemble | tests multitime conditional correlations, not autonomous relational screening | no | no raw-data repository found | multitime/coherent-reader control, E1 |
| Pearson et al. 2021, driven nanomechanical clock | membrane oscillations, RF readout, measured entropy--accuracy relation | yes at readout level | not in Paper-04B sense; stochastic external drive and laboratory acquisition remain | estimates ordinary lab duration; no constrained clock-neutral route | no | no suitable raw-data manifest established here | classical autonomous-clock/resource benchmark, E1 |
| He et al. 2023, superconducting quantum clock | continuously monitored driven transmon/resonator; coherent-oscillation and jump regimes; kinetic uncertainty test | continuous measurement trace | dynamics require coherent drives and monitored output; external laboratory clock/schedule remains | estimates lab time/precision, not a time-free parent | no | no suitable open raw-data repository established here | quantum finite-clock/backaction benchmark, E1 |
| Wadhia et al. 2025, double-quantum-dot clock | stochastic charge jumps, full classical sequence record, equilibrium and biased regimes, DC/RF resource accounting | **yes**: jump sequence `s=(s0,...,sm)` | after gate tuning, no external AC drive and settings are fixed during 30-minute acquisitions; however the recorder/acquisition interval and lab calibration are external physical resources | **partial and strongest clock-task match**: record estimates lab duration after calibration; paper does not show system-output screening or removal of endpoint/acquisition timing | no constrained/global-parent derivation | **yes**: measurement traces and analysis code on GitHub | primary operational-clock, record, resource, and readout-cost benchmark; E1 now, possible E2 only for genuinely unreported frozen statistics |
| Barontini 2026, cold-atom relational time | nearly closed BEC under a time-independent Hamiltonian; bright/dark partition; internal entropic ordering and effective Schrödinger equation | no nondestructive retained record in one realization; data are reconstructed from repeated absorption images at externally selected lab times | evolution is fixed and nearly closed between preparation and imaging, but acquisition is externally scheduled and ensemble-based | **yes at analog/reparametrization level**: internal entropy orders measured sector variables; not conditional screening with a retained clock record | structural WDW/minisuperspace analogy, not an accepted literal constraint plus autonomous route of one parent | **yes**: figure-level `.dat` files and numerics on Zenodo | primary relational-ordering benchmark; E1 now, not a Paper-04B passing parent |

## 4. Decisive primary-source facts

### 4.1 Page--Wootters optical demonstrations

The 2014 experiment explicitly calls itself an illustration of a static,
entangled Page--Wootters state: an internal observer conditions on one photon,
while an external observer verifies the global two-photon state is static. This
is strong evidence that conditional dynamics can be operationally illustrated,
but it does not provide one physical device that autonomously accumulates a
durable sequence of ticks.

Primary source:
https://doi.org/10.1103/PhysRevA.89.052122

The 2017 extension experimentally addresses multitime correlations and uses a
memory degree of freedom. It is therefore a valuable coherent/sequential reader
control. The optical apparatus still implements selected correlations in an
externally arranged ensemble rather than a fixed autonomous record-producing
parent.

Primary source:
https://doi.org/10.1103/PhysRevD.96.102005

### 4.2 Thermodynamic and quantum-clock demonstrations

The 2021 membrane experiment stochastically drives a nanomechanical resonator,
reads it through an RF cavity, and measures the entropy--accuracy relation. It
is direct evidence that a clock is a resource-consuming physical device rather
than a bare coordinate. It does not claim a constrained relational derivation.

Primary source:
https://doi.org/10.1103/PhysRevX.11.021029

The 2023 superconducting experiment continuously monitors a driven transmon
coupled to an open resonator, observing both coherent-oscillation and jump-clock
regimes and testing a kinetic uncertainty relation. It is an important quantum
and backaction benchmark, but its coherent drives, monitoring chain, and
laboratory acquisition remain explicit resources.

Primary source:
https://doi.org/10.1103/PhysRevApplied.20.034038

The 2025 DQD experiment is the strongest existing match to the repaired
operational-clock predicate. Charge states `0,L,R` generate stochastic jumps;
the full state sequence is retained; the paper constructs duration estimators
from that record; and the thermodynamic cost of the classical record is measured
separately from the clockwork. The experiment explicitly notes that the analyzer
uses lab timestamps for calibration, while the clock task uses only the state
sequence afterward. It also exposes the decisive physical fact that record
formation is not free: readout dissipation dominates clockwork dissipation in
the tested setup.

But this is not yet Paper 04B. It compares the record to laboratory time; it does
not derive the same complete experiment from one constrained parent and one fixed
autonomous route, and it does not test whether an external reference becomes
conditionally irrelevant for a separately registered system output. Thirty-
minute acquisitions and readout electronics also remain physical boundary
resources that must be represented, not waved away.

Primary sources:
https://doi.org/10.1103/5rtj-djfk
https://github.com/aspects-quantum/equilibrium-clock-public

### 4.3 Cold-atom relational-time demonstration

The 2026 BEC experiment is the strongest existing match to relational
reparametrization. The condensate evolves for about 120 ms under an effectively
closed, time-independent Hamiltonian. A bright/dark partition supplies entropy
exchange, an internal entropic parameter orders measured center-of-mass and
width data, and an effective Schrödinger equation in this internal parameter is
compared with experiment.

The same paper also prints why it is not a Paper-04B held-out parent. Absorption
images are taken every 2 ms in laboratory time; the construction uses repeated
images and derives the internal parameter from those measurements; model inputs
including `alpha` and the entropy-dependent pump are inferred from experimental
data; and the system is described as structurally analogous to minisuperspace,
not as a literal accepted Hamiltonian constraint with a second, autonomous
derivation of the identical complete transcript. It is a controlled analog
benchmark, not evidence that fundamental external time has been removed.

Primary sources:
https://doi.org/10.1103/1h9j-df4k
https://doi.org/10.5281/zenodo.19651064

## 5. The empirical complementarity result

Existing demonstrations presently divide into two complementary classes:

$$
\begin{array}{c|c|c}
& \text{retained operational tick record} & \text{relational/time-free description}\\
\hline
\text{DQD / superconducting / membrane clocks} & \checkmark & \text{not established}\\
\text{Page--Wootters / cold-atom analogs} & \text{not autonomous in one run} & \checkmark\ \text{(conditional/analog scope)}
\end{array}
$$

No identified public experiment currently occupies the upper-right cell while
also supplying one frozen parent and two independently derivable complete
routes. This is an empirical ceiling, not an impossibility theorem.

## 6. What a repaired Paper 04B experiment would actually require

The cleanest feasible construction would combine the two classes without
pretending that one published apparatus already does both:

1. **Physical clock branch.** A DQD-like or superconducting jump process produces
   a retained record `R`, with clockwork, amplifier, memory, reset, and readout
   costs included in the parent.
2. **Comparator/system branch.** A separately addressable finite system produces
   held-out outputs `Y` under registered tasks whose ordinary reference predictor
   depends nontrivially on external duration `tau`.
3. **Fixed parent.** Initialization is followed by a fixed interaction/mechanism;
   no time-indexed gate table or externally timed stop pulse is hidden in
   context. A passive readout domain or represented physical completion event is
   frozen.
4. **Clock adequacy.** On held-out runs, `R` beats no-clock, frozen, mistuned,
   scrambled-record, jump-count-only, and metadata-only controls for estimating
   duration or predicting `Y`.
5. **Relational screening.** Test whether `tau` adds predictive information after
   `(R,E)` is known. Reject if success comes from a supplied acquisition length,
   sample count, timestamp, programmed slot number, or controller memory.
6. **One-parent duality.** Independently derive the complete transcript law from
   a constrained/clock-neutral representation and from the fixed autonomous
   realization. This is mathematics about the chosen parent, not an extra fit to
   the same table.
7. **Reciprocity and finite effects.** Clock interventions must change comparator
   responses and comparator interventions must perturb clock statistics within a
   preregistered domain. Resolution, recurrence, disturbance, record cost, nulls,
   and failures remain visible.
8. **Prospective evidence.** Promotion requires E3 data generated after all of
   the above is frozen, or an explicitly weaker E2 result with no claim of clean
   prospective confirmation.

## 7. Feasibility verdict

```text
EXISTING PUBLIC CLOCK DATA FOR STAGE-B CALIBRATION:       YES
EXISTING PUBLIC RELATIONAL-TIME DATA FOR CALIBRATION:     YES
EXISTING DATASET THAT ALREADY PASSES REPAIRED PAPER 04B:  NO IDENTIFIED
ONE-PARENT / TWO-ROUTE LAB DEMONSTRATION:                 NO IDENTIFIED
CLEAN PROMOTION-BEARING HELD-OUT EVIDENCE:                REQUIRES NEW DATA
HARDWARE PROGRAM CURRENTLY AUTHORIZED:                    NO
PAPER 04B V2 CURRENTLY AUTHORIZED:                        NO
```

The empirical programme is feasible in principle, but the exact authorized pin
was correctly stopped before model selection. The next scientific action would
be a separately authorized model-neutral repaired pin that freezes the
`gamma/tau/u_tau` split, clock-task adequacy, relational screening, and passive-
readout/physical-completion rule. It should use the DQD and cold-atom results as
Stage-B controls, not recycle them as fresh promotion evidence.

