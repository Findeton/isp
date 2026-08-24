# SPB contract review - Seat P-R regional physical-source/apparatus report

Date: 2026-08-24

Seat: P-R (regional preparation, metrology, adapter, and reconnection)

Review state: frozen independent report; scientific result awarded: none

## 1. Independence and authenticated review boundary

I performed this review read-only and did not inspect, contact, or receive a
sibling reviewer or sibling report. I made no repository change and used no
later source as a repair. The unrelated untracked
`v16/note-handoff-prompt-2026-08-22.md` was excluded.

At authentication, the checked-out commit was
`014c82008f736ea8837be6af548cd308f317f3af`, whose sole parent is
`b1ff02806aade184298534f1d285f82b8c32ab89`. The pin is present in that commit,
has 489 LF lines, 22,169 bytes, and raw SHA-256
`b5491cd698af90f6603f1597a8724f9614d0d255fef5b0da0c9b54686ac6c75d`.
Applying the pin's Section 6.1 normalization exactly reproduces
`1ac5bc365a13e2158386ab6e2a1847cf94cdaa750e79e130ea83b5de2bc5391d`.
The worktree bytes of the pin and all seven Section 2 objects are identical to
commit `014c820`.

Authenticated Section 2 objects:

| Object | LF lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `v17/note-foundational-assumption-deletion-programme.md` | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` |
| `v17/research-incubator/active/assumptions/v17_assumption_parallel_synthesis_and_next_gates.md` | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` |
| `v17/research-incubator/active/spb/v17_spb_primary_source_receipt_manifest.md` | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` |
| `v17/research-incubator/active/spb/v17_spb_p0_physical_platform_and_source_audit.md` | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` |
| `v17/research-incubator/active/spb/v17_spb_result_neutral_gate_contract.md` | 727 | 28901 | `7212e363cea918e82343eaa0dfe930aa27210c1fbbda4eae3115ccd98174b4d8` |
| `v17/research-incubator/active/spb/v17_spb_root_pre_pin_readiness_and_mutant_audit.md` | 418 | 19438 | `fdb1808a007dce02c4f606889c5632f1d6369542056c3f7664a2f8d63341cd68` |
| `v17/research-incubator/active/spb/README.md` | 77 | 3500 | `04b985f737ca4179c132be03daa1ff169827ff041e407c4921b2dbe532fe933b` |

Authenticated exact scholarly receipts:

| ID | Bytes | SHA-256 |
|---|---:|---|
| `SPB-S1`, Pollock et al., arXiv:1801.09811v1 | 896695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` |
| `SPB-S2`, Giarmatzi et al., arXiv:2308.00750v3 | 6601486 | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` |
| `SPB-S3`, Xiang et al., arXiv:2105.03333v2 | 1276514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` |
| `SPB-S4`, Lawniczak et al., publisher PDF | 1835223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` |
| `SPB-S5`, Kostrykin and Schrader, arXiv:math-ph/0008022v1 | 307827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` |
| `SPB-S6`, Farooq et al., publisher PDF | 3291194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` |

The `NMN-tomo` repository is clean at
`154235f8bbf5e70eb71c325370a67b1894490452`. Its four listed receipts reproduce
exactly: `README.md`, 904 bytes,
`fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593`;
`All codes.ipynb`, 1,399,666 bytes,
`b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1`;
`NMN_lab_rslts.json`, 20,177 bytes,
`b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43`;
and `NMN_tomog_rerun.json`, 176,825 bytes,
`450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657`.
The `qucse` repository is clean at
`81998e861ae43541d03738c15d7c60715be37309`; its tracked tree contains fitted
matrices and analysis products but no laboratory DataVault. Authentication
therefore passes, including the pinned absence.

## 2. Review standard

I distinguished exact equality of ideal graph functions, approximate equality
of measured records, similarity/conjugacy of matrices, and literal equality at
common labelled physical reference planes. I treated connector, load, adapter,
calibration, source phase, noise, and assembly state as apparatus, not notation.
I also separated a unitary graph theorem from a measured lossy network and an
algebraic bracketing identity from a direct three-module observation.

## 3. Findings

### P-R-01 - Farooq gives ideal scalar equality and approximate one-port laboratory agreement, not a common-interface gluing result

- Severity: moderate source-scope correction; high if promoted to a passed SPB-R arm.
- Category: physical-source and apparatus.
- Affected claims: `C9`, `C10`, the `SPB-S6` role ceiling, and P0 Sections 3.1
  and 3.4.
- Evidence: exact `SPB-S6`, Eq. (6), states general isoscattering as
  conjugacy. For its single contact the matrix is scalar, so Eqs. (9)-(11)
  prove `M_Gamma1(k)=M_Gamma2(k)=2k tan(3kl)` and hence exact ideal-graph
  equality. The experiment uses two different microwave networks connected to
  the VNA by leads `L1` and `L2`, not one physically transplanted common
  connector. Its text says the measured amplitudes and phases are in "almost
  perfect agreement" over 0.01-1 GHz, not literally identical, and models
  absorption by a complex wave number. The data are available only on request.
  It reports no reconnection or triple assembly.
- Finding: the source is a valid positive control for scalar one-contact
  indistinguishability of different ideal interiors and close physical
  realization. "Literal equality" is exact at the theoretical one-channel
  response level; the laboratory evidence is finite-accuracy agreement across
  separately connected networks. It does not establish literal common-hardware
  reference planes, multiport completeness, or composition. The contract's
  later demand for those objects is necessary.

### P-R-02 - Lawniczak establishes transplantation conjugacy, not fixed-port equality

- Severity: high source-scope boundary for fixed-interface screening.
- Category: physical-source, apparatus, and semantic.
- Affected claims: `C9`, `C10`, the `SPB-S4` role ceiling, and P0 Sections 3.2
  and 3.4.
- Evidence: exact `SPB-S4`, Eqs. (4), (5), (11), and (15), gives
  `S^(I)=T4^-1 S^(II) T4` for an explicitly printed frequency-independent
  `T4`. For the four-lead experiment, a two-port Agilent E8364B was reconnected
  in six port-pair configurations while the other two ports were terminated
  with 50-ohm loads. The paper says full matrices are required for the
  transplantation calculation, but its published trace plots use diagonal
  elements and its direct transplantation figure displays only the modulus of
  transformed `S11`. It reports small discrepancies above 0.55 GHz for that
  comparison and trace discrepancies over 1-1.3 GHz. Raw matrices are
  request-only. No direct adapter or triple gluing is built.
- Finding: the exact mathematical relation is conjugacy, and the physical
  evidence is approximate. Trace, determinant, spectra, and the displayed
  transformed component do not imply equality for every common labelled port
  excitation and phase-sensitive reader. The source is correctly useful as a
  transplantation control, but cannot itself pass fixed-interface screening.

### P-R-03 - The printed `T4` is not unitary up to any scalar

- Severity: high apparatus restriction; decisive against a passive lossless
  four-port-adapter reading.
- Category: apparatus and physical-source.
- Affected claims: `C9`, contract Section 7.3, and the adapter branch of P0
  Sections 3.2 and 6.2.
- Evidence: from exact `SPB-S4`, Eq. (15),
  `T4=[[1,-1,0,0],[1,0,-1,0],[0,1,0,-1],[0,0,1,1]]`. Direct multiplication
  gives
  `T4^dagger T4=[[2,-1,-1,0],[-1,2,0,-1],[-1,0,2,1],[0,-1,1,2]]`, whose
  eigenvalues are `2-sqrt(2)` twice and `2+sqrt(2)` twice. Its off-diagonal
  entries remain nonzero under multiplication by any nonzero scalar.
- Finding: no scalar `a` makes `(a T4)^dagger(a T4)=I`; therefore `T4` cannot
  be a passive lossless four-channel mixer in the same normalization. A
  broader linear implementation could realize suitably scaled contractions
  using attenuation, ancillary dump ports, and separate input/output networks,
  or could use active gain, but then the inverse transformation, common-plane
  calibration, extra channels, loss, gain, noise, dynamic range, and matching
  attenuation on the comparator are physical boundary data. Such an adapter
  must be built and calibrated before held-out opening. Matrix conjugation in
  software is not an adapter.

### P-R-04 - Fixed reference planes and coherent multiport readers are feasible but absent from the predecessors

- Severity: high apparatus duty for an evaluation pin.
- Category: apparatus.
- Affected claims: `C4`, `C9`, `C10`, and contract Sections 7.1-7.4 and 8.
- Evidence: `SPB-S4` uses RG402 coax and states a TE11 onset near 33 GHz, so its
  0.01-1.3 GHz cable propagation is safely in the TEM range; it nevertheless
  reconfigures a two-port VNA and changes terminations. `SPB-S6` likewise uses
  a VNA and distinct leads. Neither exact source publishes calibration
  standard records, de-embedded common reference planes, multi-source relative
  phase trials, connector torque/orientation histories, load characterization,
  or complete replugging attempts.
- Finding: full coherent multiport characterization at fixed planes is
  conventional and feasible with a calibrated multiport VNA/test set or
  synchronized sources, stable reference clocks, and appropriate SOLT/TRL or
  equivalent calibration. One-port-at-a-time data predict coherent
  superpositions only after linearity and shared-phase stability have been
  validated. Cable single-mode propagation does not rule out junction,
  connector, adapter, evanescent, common-mode, radiation, or hidden-load
  channels. Reference planes must be outside noncomposable near fields or the
  collar/mode data must enter the boundary.

### P-R-05 - A frequencywise `S` relation is sufficient only for the validated deterministic coherent-response scope

- Severity: moderate scope condition and high evaluation duty.
- Category: apparatus and semantic.
- Affected claims: `C4`, `C9`-`C11`, and contract Sections 5, 7.2, 7.4, 7.5,
  8, and 10.
- Evidence: both microwave papers study passive coaxial networks with
  absorption. `SPB-S6` inserts an empirical dissipation coefficient;
  `SPB-S4` discusses absorption but does not publish power sweeps, additive
  noise-wave statistics, intermodulation tests, or time-stationarity blocks.
  Kostrykin-Schrader assumes unitary scattering. A measured complex matrix
  fixes coherent mean outputs of a linear time-stationary mode, but by itself
  does not fix receiver noise, thermal/emission noise of a lossy module,
  correlated internal fluctuations, dropped acquisitions, or drift.
- Finding: the printed contract is physically coherent at the explicitly
  frozen linear, time-stationary, single-mode scope only if the Section 8
  nuisance parent supplies a separately calibrated stochastic readout/noise
  relation and the complete attempt law. The phrase in Section 7.5 that module
  matrices and connector calibration are the "only prediction inputs" can
  apply to the deterministic seam response; it cannot erase the already
  required noise, loss, load, drift, calibration covariance, and failure
  inputs needed to predict complete transcripts. Detection of conversion,
  hysteresis, internal-state memory, or extra propagating modes is the printed
  `R7`/underdetermination outcome, not permission to enlarge `S` after opening.

### P-R-06 - The generalized star-product theorem has a lossless self-adjoint graph domain

- Severity: high source-scope boundary; no defect in the contract's operational seam definition.
- Category: physical-source and apparatus.
- Affected claims: `C10`, the `SPB-S5` role ceiling, and contract Sections 7.5
  and 7.6.
- Evidence: exact `SPB-S5` analyzes finite graphs with self-adjoint Laplacians
  and unitary on-shell scattering matrices. Definition 3.1 and Eqs. (3.2)-(3.4)
  give the generalized product; Theorems 3.8 and 3.9 establish unitarity and
  continuity, and the text gives associativity with its port-dimension
  conditions. Theorem 4.1 gives the glued graph scattering matrix for all
  positive energies, including the non-compatible cases handled by the
  generalized definition. The theorem contains no lossy coax, additive noise,
  VNA calibration, replugging, or empirical composite.
- Finding: `SPB-S5` is a correct mathematical conformance control where its
  self-adjoint/unitary hypotheses hold. It does not establish laboratory
  reconnection or complete-law composition for dissipative apparatus. For
  measured lossy linear modules, solving the actual seam equations is valid
  when a unique stable solution exists; ill-conditioned/nonunique cases and
  their uncertainty are experimental outcomes. The directly measured
  composite remains indispensable.

### P-R-07 - Direct pair and triple gluing are physically feasible and not supplied by any cited run

- Severity: high apparatus and no-refit duty.
- Category: apparatus, physical-source, and semantic.
- Affected claims: `C2`, `C9`-`C11`, and contract Sections 5, 7.5-7.7, 9, and
  11.
- Evidence: none of `SPB-S4`-`SPB-S6` measures independently characterized
  modules and connectors, predicts a newly assembled two- or three-module
  network, and compares both algebraic bracketings with one direct complete
  record. The frozen contract requires exactly that and holds out an interior
  substitution in one assembly.
- Finding: modular coaxial two- and three-network assembly is feasible. Each
  isolated module must be measured with the same port impedances and reference
  conventions later used at seams; connector `V` must include electrical
  length, mismatch, orientation, repeatability, and covariance. One final
  physical `ABC` network is sufficient: the two bracketings are two calculations
  on the same frozen inputs, not two physical ontologies. A composite matrix
  fitted after assembly, a connector de-embedded using the held-out composite,
  or an adapter tuned on held-out residuals is circular/target-built and earns
  no composition credit.

### P-R-08 - Exact regional packet remains absent and is fully identifiable

- Severity: high; blocks `SPB-L1` and every empirical regional conclusion.
- Category: physical-source, apparatus, and procedural.
- Affected claims: `C4`, `C9`-`C12`, and the ladder ceiling.
- Evidence: both microwave data statements are request-only; no source has an
  immutable raw multiport matrix packet, common-interface adapter calibration,
  direct reconnection, triple assembly, complete attempt log, or SPB held-out
  split.
- Finding: the exact missing regional packet is: immutable module, interior,
  cable, connector, adapter, load, calibration-standard, source and reader
  identities; physical topology, dimensions, impedances, orientations,
  reference planes, environmental state, firmware and VNA settings; raw
  complex waves or S records with timestamps and covariance; literal common-
  plane different-interior preparations; independently characterized adapters
  including all ancillary ports, insertion loss/gain/noise and realizability;
  linearity, superposition, power, intermodulation, stationarity, mode and
  noise-wave validation; connector and load relations; frozen frequency,
  waveform, power and time blocks; independently measured `A/B/C` modules;
  direct two-module and one three-module composite with one held-out interior
  substitution; both bracketings and singular/conditioning policy; complete
  assembly, calibration, replugging, anomaly, abort and failure attempts;
  immutable split/randomization objects, nuisance covariance and analysis
  environment; and public raw bytes. No present source supplies that packet,
  and this review performs no repair or acquisition.

## 4. P-R conclusion

The regional contract is a physically meaningful and nonvacuous experiment at
the printed calibrated coherent multiport scope, provided complete transcript
prediction includes the already required stochastic nuisance/noise parent.
The predecessor claims need strict scope: ideal scalar equality is not exact
laboratory equality, and transplantation conjugacy is not common-port
screening. A scalar-normalized `T4` passive lossless four-port is impossible;
the contract correctly makes a real adapter with all extra resources a new
physical object. Direct two- and three-module gluing is feasible, but no cited
source has done it and the exact run packet is absent. This report awards no
empirical rung and makes no separate joint disposition recommendation.

Report LF line count: `000279`

Report byte count: `017144`

Report normalized self-SHA-256:
`88bf9924d75dce41296c4902605af2cb93875493b5870562e58c7332afbda19f`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
