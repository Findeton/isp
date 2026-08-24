# ISP v17 — SPB-P0 physical platform and source audit

**Status:** COMPLETE AUTHOR-SIDE SOURCE/PLATFORM AUDIT / SPB OPEN / NO EVALUATION PIN
**Date:** 2026-08-24
**Scientific result awarded:** none
**Maximum claim:** two physically serious architectures identified; neither
current public packet executes the complete SPB experiment

---

## 0. Executive verdict

The Sufficient Physical Boundary Gate cannot honestly be run by taking a
tomographically reconstructed process matrix for SPB-T and an on-shell
scattering matrix for SPB-R and declaring them to be physical boundaries.
Those objects are excellent predictive interfaces. The question of SPB is
whether an independently identified carrier and a complete physical grammar
make them sufficient.

The primary-source audit reaches four conclusions.

1. The strongest temporal starting architecture is a two-transmon
   system--memory experiment. Existing work separately supplies complete
   system-side multi-time tomography with public count data and an engineered
   two-qubit memory process with direct system projections. Neither published
   experiment performs the full registered memory read/toggle/randomize/
   erase/isolate battery on the same held-out process family.
2. The strongest regional starting architecture is a modular multiport
   microwave network. A 2025 one-port experiment physically realizes
   different interiors with the same scalar scattering response at a fixed
   contact, while an earlier four-port experiment realizes a richer response
   related by transplantation. A rigorous theorem composes graph scattering
   matrices by a generalized star product. No one experiment combines fixed-
   interface equality, multiport completeness, public raw scattering bytes,
   registered interior reconnection, and a three-region direct-measurement
   test.
3. These gaps are not clerical. Without intervention on the proposed memory,
   SPB-T cannot tell whether it has found the memory or merely fitted its
   effects. Without a common fixed port interface and direct gluing, SPB-R
   cannot tell whether it has found a sufficient boundary or only an invariant
   of two closed presentations.
4. Therefore P0 selects the two architectures for a result-neutral SPB
   contract, but it does not select existing results as an SPB evaluation.

```text
SPB-T PHYSICAL ARCHITECTURE:       TWO-TRANSMON SYSTEM + MEMORY
SPB-T COMPLETE PUBLIC RUN PACKET:  ABSENT
SPB-R PHYSICAL ARCHITECTURE:       MODULAR MULTIPORT MICROWAVE NETWORK
SPB-R COMPLETE PUBLIC RUN PACKET:  ABSENT
SPB EVALUATION PIN:                NOT YET POSSIBLE
SPB SCIENTIFIC OUTCOME:            NONE
```

The absence of a complete packet is an apparatus/source-closure result about
the audited literature. It is not a no-go theorem for sufficient physical
boundaries.

---

## 1. Question and five non-equivalent duties

For either arm, let `I` denote an alleged physical interface, `P` an earlier or
interior preparation, `F` a held-out future or exterior policy, and `R_F` the
complete retained record. A serious boundary claim must earn all five duties.

### D1 — independent descent

`I` must be located, prepared, transformed, and read by source-closed physical
operations chosen without the held-out answer. A predictive quotient computed
from the complete target law is not independent descent.

### D2 — screening

After conditioning or intervening on `I` in the registered way, every admitted
past/interior alternative must give the same complete future/exterior record
law within a predeclared uncertainty and equivalence region.

### D3 — composition

The same interface description must predict a physically reconnected held-out
experiment. Fitting the already connected whole is not composition.

### D4 — physical intervention and readout

Every operation used in D1--D3 must be an implemented instrument with null,
failure, old-record, drift, and invalid outcomes retained. An operator label,
tomography basis, or mathematical marginal is not automatically a physical
operation.

### D5 — no-refit transfer

The law, interface rule, reader map, and nuisance family are frozen before the
held-out future, exterior, frequency band, or gluing is opened. Transfer after
retuning is calibration, not evidence of sufficiency.

Screening without composition is admissible. Composition without independent
descent is a compiler. A physically descended interface that fails screening
is still a useful discovered carrier, but not a sufficient boundary.

---

## 2. Temporal primary-source reconstruction

### 2.1 Operational causal break

Pollock et al. define a causal break by measuring/discarding the system input
and preparing a known output independent of it. After such a break, dependence
of a later system state on the prior controls or measurement outcome witnesses
memory outside the freshly prepared system. This is the correct theoretical
control for SPB-T because it distinguishes an observational conditional from
an intervention.

The theorem does not identify the physical memory. A process tensor can encode
the effect of an unobserved environment even when the environment carrier is
unknown. SPB-T therefore adds direct operations on every claimed memory.

Exact retrieved object:

| object | bytes | SHA-256 | role |
|---|---:|---|---|
| Pollock et al., *Operational Markov condition for quantum processes*, arXiv:1801.09811v1 retrieved 2026-08-24 | 896,695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | causal-break and operational-memory theorem |

Primary link: <https://arxiv.org/abs/1801.09811>.

### 2.2 Complete system-side multi-time tomography

Giarmatzi et al. implement full three-time process tomography on an in-house
five-transmon chip and `ibm_perth`. The experiment uses sequential
measure--prepare operations, approximately `5.3e6` shots per process on the
reported UQ run, and publishes raw count JSON plus reconstruction code.

This is a major improvement over unitary-only or projection-only restricted
tomography. It establishes that a complete system-side operational process can
be reconstructed on current superconducting hardware.

It does not close SPB-T:

1. the UQ process is modeled with a dominant nearby transmon called the memory,
   but the reported held-out grammar acts on the system, not through the full
   memory intervention battery;
2. the paper explicitly allows additional qubits, material defects,
   electronics, and classical fluctuations in the environment;
3. the simple one-memory-qubit model does not account for all observed
   non-Markovianity;
4. the tomography does not capture interaction during the measurement pulse;
5. `ibm_perth` supplied no frequency or interaction-strength control; and
6. reconstructing `W` tells us what system records do, not which microscopic
   carrier is actual or sufficient.

The public repository is nevertheless valuable because it closes exact bytes
for the ten reported process datasets and their post-processing.

| object | bytes/commit | SHA-256 or commit | role |
|---|---:|---|---|
| Giarmatzi et al., arXiv:2308.00750v3 | 6,601,486 bytes | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` | complete system-side multi-time experiment |
| authors' `NMN-tomo` repository | commit | `154235f8bbf5e70eb71c325370a67b1894490452` | public reconstruction/data package |
| `NMN_lab_rslts.json` | 20,177 bytes | `b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43` | UQ count data |
| `NMN_tomog_rerun.json` | 176,825 bytes | `450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657` | nine IBM count datasets |

Primary links:

- <https://arxiv.org/abs/2308.00750>
- <https://github.com/Christina-Giar/NMN-tomo>

These file hashes and the repository hash are evidence only for the retrieved commit. A future pin
must vendor or otherwise bind every consumed file, environment, and source
receipt; a moving GitHub branch is not an immutable scientific source.

### 2.3 Engineered explicit memory qubit

Xiang et al. use two neighboring transmons as system `S` and environment `E`,
with a CNOT--CZ or CZ--CNOT interaction sequence. They implement a complete
basis of intervening projective operations on `S`, characterize reduced gates
for `E` prepared in `|0>`, `|1>`, and a superposition, and show that the
restricted process tensor predicts held-out system states much better than a
memoryless reduced-map construction for the deliberately non-Markovian order.

This is the strongest direct predecessor for a physically named memory. It
also exposes the remaining gap. The process tensor is reconstructed from
system operations and system final tomography. The paper states that the
ancilla simulates the environment and that the method can be applied when the
real environment is beyond measurement or control. It resets `E` initially
and uses different initial `E` preparations for gate characterization, but
does not execute read, toggle, randomize, erase, and isolate operations on `E`
at the candidate cut across the held-out family.

The linked QUCSE repository contains fitted matrices and analysis code. The
figure scripts refer to an external laboratory DataVault; the raw laboratory
datasets are not contained in the retrieved repository.

| object | bytes/commit | SHA-256 or commit | role |
|---|---:|---|---|
| Xiang et al., arXiv:2105.03333v2 | 1,276,514 bytes | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` | explicit engineered system--memory predecessor |
| authors' QUCSE repository | commit | `81998e861ae43541d03738c15d7c60715be37309` | analysis/fitted-matrix package; raw DataVault absent |

Primary links:

- <https://arxiv.org/abs/2105.03333>
- <https://github.com/xlelephant/qucse>

### 2.4 Temporal admission matrix

| required coordinate | Giarmatzi et al. | Xiang et al. | SPB-T disposition |
|---|---|---|---|
| exact system-side causal break | yes, measure--prepare | projective system break | retained |
| complete system intervention basis | yes at registered three times | restricted projection span | Giarmatzi control preferred |
| independently named memory | dominant nearby qubit plus unclosed environment | explicit ancilla transmon | Xiang architecture preferred |
| memory read at cut | no held-out battery | no held-out battery | missing |
| memory toggle | no | no at cut | missing |
| memory randomize | no | no at cut | missing |
| memory erase/reset at cut | initial reset only | initial reset only | missing |
| memory isolate/decouple | not in run | not in run | missing |
| incompatible held-out futures | time grid/process datasets | two gate orders and projections | partial |
| complete null/failure/old-record law | counts and error model, not full apparatus transcript | partial/postselected | missing |
| public raw data | yes for system tomography | no laboratory DataVault | partial |
| source closure beyond named memory | explicitly false/underdetermined | dissipation to larger environment | missing |

No existing experiment passes D1--D5. The selected architecture is therefore
not an old dataset renamed as a result. It is a new two-transmon experiment
whose memory interventions are specified in the SPB contract.

---

## 3. Regional primary-source reconstruction

### 3.1 Fixed-interface one-port substitution

Farooq et al. construct two non-isospectral quantum graphs with different
topologies but the same scalar scattering matrix at one contact and validate
the construction with microwave networks. Because the boundary has one
channel, the isoscattering condition is literal equality,

$$
S_{\Gamma_1}(k)=S_{\Gamma_2}(k),
$$

not merely similarity under a channel transformation. The reported complex
amplitudes and phases agree closely over `0.01--1 GHz`. Perturbing the
interiors reveals resonances that were invisible at the original boundary.
This is the cleanest audited physical demonstration that different interiors
can be indistinguishable to a fixed bounded exterior reader.

Its scope is too small for the whole SPB-R gate. One scalar port does not test
multiport coherent superpositions or a nontrivial seam algebra; no physical
reconnection or three-module gluing is reported; and raw data remain available
only on request.

| object | bytes | SHA-256 | role |
|---|---:|---|---|
| Farooq et al., *Isoscattering non-isospectral quantum graphs* | 3,291,194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` | literal fixed-one-port different-interior substitution control |

Primary link: <https://www.nature.com/articles/s41598-025-23400-5>.

### 3.2 Multiport transplantation control

Ławniczak et al. construct two families of open quantum graphs with different
interiors and prove that their `2n x 2n` scattering matrices are related by a
frequency-independent transplantation matrix. They physically realize the
`n=2`, four-lead case with coaxial microwave networks and measure full complex
scattering matrices using a vector network analyzer.

This is unusually close to an SPB-R substitution control: the interiors have
different vertex and bond structures while the boundary responses lie in one
registered equivalence class.

It is not equal-boundary substitution at a fixed physical interface.
The relation is

$$
S^{(I)}(\nu)=T_4^{-1}S^{(II)}(\nu)T_4.
$$

Conjugacy is not equality for the same labelled port excitations and readers.
For the printed `T_4`, direct multiplication gives
`T_4^\dagger T_4` not proportional to the identity, so multiplying `T_4` by a
scalar does not turn it into a passive lossless port mixer. The transplantation
is a mathematical channel-basis isomorphism, not automatically an executable
boundary adapter. Unless that change is declared gauge and justified
operationally, or implemented by independently calibrated physically allowed
input/output adapters, the two interiors remain distinguishable at fixed
ports. Equality of traces or spectra alone is much weaker than screening for
all exterior readers.

The paper reports excellent agreement below roughly `1 GHz` and small higher
frequency discrepancies attributed to cable-length and vertex-boundary
differences. Its raw data are available only from the authors on request, not
as immutable public bytes. It tests `n=2`, not the registered three-region
gluing.

| object | bytes | SHA-256 | role |
|---|---:|---|---|
| Ławniczak et al., *Isoscattering strings of concatenating graphs and networks* | 1,835,223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` | physical different-interior/conjugate-boundary predecessor |

Primary link: <https://www.nature.com/articles/s41598-020-80950-6>.

### 3.3 Composition theorem

Kostrykin and Schrader prove that, under the printed compatibility conditions,
the scattering matrix of a graph obtained by gluing subgraphs is the
generalized star product of the subgraph scattering matrices. The product is
nonlinear and noncommutative but associative where the relevant products are
defined. This supplies the correct mathematical comparator for physical
reconnection and triple gluing.

The theorem is not an empirical sufficiency result. Real coaxial connectors,
loss, imperfect loads, calibration planes, port-reference phases, evanescent
modes, and frequency drift must be included in the physical interface. A
directly measured composite remains the held-out target.

| object | bytes | SHA-256 | role |
|---|---:|---|---|
| Kostrykin and Schrader, arXiv:math-ph/0008022 | 307,827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` | generalized star-product and associativity control |

Primary link: <https://arxiv.org/abs/math-ph/0008022>.

### 3.4 Regional admission matrix

| required coordinate | audited isoscattering packets | SPB-R disposition |
|---|---|---|
| two physically different interiors | yes in both | retained |
| common fixed port interface | literal equality in one-port 2025 packet; conjugate only in four-port 2021 packet | fixed-interface multiport packet still missing |
| all complex exterior responses | scalar complex response in 2025; full matrix in 2021 | neither alone closes the gate |
| independent interface calibration | ordinary VNA calibration described | expand to adapter/connector planes |
| physical interior substitution | two separate networks | retained |
| registered reconnection | no | missing |
| direct composite versus star-product prediction | no | missing |
| three-region/two-bracketing test | theorem only; experiment `n=2` | missing |
| gauge/port-phase mutants | transplantation only | expand |
| hidden edge/stub/dressing mutants | no | missing |
| complete null/anomaly/failure records | no public attempt transcript | missing |
| immutable public raw data | no; available on request | missing |
| no-refit held-out band/waveform | no SPB split | missing |

The architecture is selected because it makes the substitution and gluing
questions physical. The two experiments are retained as complementary
positive controls, not collaged into a passed SPB-R arm.

---

## 4. Selected physical architectures

### 4.1 SPB-T-Q2

The temporal architecture is one addressable superconducting system transmon
`S`, one addressable dominant memory transmon `M`, their independently
calibrated coupling, the residual bath `E_perp`, controllers, readout
resonators, classical memory, and complete attempt records.

`S+M` is a candidate boundary, not a conclusion. `E_perp` remains in the
source-closure ledger. A residual dependence after resetting and isolating
`M` is not fitted away by adding an unevidenced latent memory after the fact.

### 4.2 SPB-R-MW3

The regional architecture is three independently characterized passive linear
multiport microwave modules, interchangeable different-interior modules,
calibrated boundary-basis adapters, physical connectors, matched loads, a VNA
or equivalent coherent source/reader, and complete assembly records.

The boundary candidate is the calibrated complex multiport response over a
frozen frequency band and power regime, including reference-plane and loss
metadata. It is an effective physical boundary in classical wave physics, not
a proposed fundamental ontology.

---

## 5. Why numerical completion would be scientifically wrong

A simulation can verify the causal-break algebra, calculate expected response
families, exercise the generalized star product, and test the scoring code. It
cannot establish:

1. that the named memory is the actual carrier of all future-relevant
   information;
2. that reset or isolation works on the physical residual bath;
3. that two microwave interiors are equivalent at one fixed laboratory
   interface;
4. that connector and calibration-plane data compose target-blindly; or
5. that the held-out physical records obey the frozen nuisance model.

Accordingly, synthetic fixtures are hostile controls only. They may make an
analysis pipeline fail closed; they cannot award D1--D5.

---

## 6. Minimum new physical packet

### 6.1 Temporal packet

An admissible SPB-T run must add, on the same device and same process family:

1. independently calibrated `S` and `M` preparation and informationally
   complete readout;
2. a system causal break;
3. registered `M` identity, read, toggle, Pauli-randomize, active reset, and
   dynamical-isolation branches;
4. at least two past policies that agree on the proposed boundary but differ
   in prior history;
5. incompatible held-out future policies;
6. direct three-segment composition runs;
7. all measurement, reset, leakage, timeout, invalid, drift, old-record, and
   controller records; and
8. an immutable open raw-data and calibration packet.

### 6.2 Regional packet

An admissible SPB-R run must add:

1. two different interiors connected to a literally common labelled boundary,
   using independently measured physical transplantation adapters if needed;
2. all complex multiport responses in frozen training and held-out bands;
3. at least one exterior module physically reconnected to each interior;
4. three independently measured modules and one directly measured final
   composite;
5. both algebraic parenthesizations computed without refitting;
6. port permutation, phase-reference, adapter-loss, mismatched-load, hidden
   stub, and connector-drift mutants;
7. complete assembly and failed-calibration records; and
8. immutable public raw bytes.

---

## 7. P0 outcome and ceiling

```text
SPB-P0-T: ARCHITECTURE IDENTIFIED / COMPLETE PUBLIC PACKET ABSENT
SPB-P0-R: ARCHITECTURE IDENTIFIED / COMPLETE PUBLIC PACKET ABSENT
SPB-P0:   PROCEED TO RESULT-NEUTRAL CONTRACT AND PIN READINESS
```

This P0 audit permits the result-neutral contract to be written and reviewed.
It does not permit a positive or negative boundary verdict from the old data.
It reaches no more than author-side `FAD-L1`: the physical candidates, missing
interventions, source debts, and exact next experiment are identified.

No chronology, spacetime, gravity, quantum ontology, Barandes confirmation or
refutation, Hilbert demotion, or universal boundary principle follows.

---

## 8. Differential source rule

Before any independent review or empirical scoring:

1. retrieve and hash the then-current exact scholarly objects, supplements,
   code, raw data, calibration files, apparatus inventory, and analysis
   environment;
2. bind immutable repository commits rather than moving branches;
3. fail closed on missing or substituted raw records;
4. record every source that is request-only or inaccessible;
5. rerun this audit if the platform, intervention grammar, reader, nuisance
   family, held-out split, or boundary candidate changes; and
6. never repair a physical failure by editing the boundary after held-out data
   are opened.

The next file freezes the result-neutral scientific contract. It does not
pretend that the minimum new physical packet already exists.
