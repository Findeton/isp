# SPB contract review - Seat P-T temporal physical-source/apparatus report

Date: 2026-08-24

Seat: P-T (temporal preparation, carrier, intervention, and reader)

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

I treated a transmon label as an effective, independently controlled apparatus
partition, not a fundamental tensor-factor award. I separated a system-side
process reconstruction from a descended memory carrier, an ensemble
calibration from a non-disturbing single-shot state fact, logical reset from
information destruction, and a retained acquisition transcript from
microscopic environmental completeness.

## 3. Findings

### P-T-01 - Pollock establishes the causal-break criterion, not a carrier

- Severity: none for the frozen source role; high if promoted to apparatus evidence.
- Category: physical-source and semantic.
- Affected claims: `C1`, `C3`, `C6`, `C7`, and the `SPB-S1` role ceiling.
- Evidence: exact `SPB-S1`, pp. 2-3, defines a causal break as an output
  preparation independent of the input and tests whether the later normalized
  system state depends on the prior measurement or controls. Its memory is an
  unspecified external environment. The paper contains no selected transmon,
  memory preparation, memory reader, reset, isolation, or controller ledger.
- Finding: the frozen package attributes exactly the theorem-level role that
  the source supports. Pollock supplies the operational break and an
  all-controls Markov criterion. It cannot identify `M`, prove `S+M`
  sufficiency, or validate any physical memory grammar.

### P-T-02 - Giarmatzi is complete only on the registered system-side three-time grammar

- Severity: high evaluation blocker; no defect in the printed ceiling.
- Category: physical-source and apparatus.
- Affected claims: `C1`, `C4`, `C6`-`C8`, and the `SPB-S2` role ceiling.
- Evidence: exact `SPB-S2`, pp. 3-5, uses sequential system
  measure-prepare operations over 324 protocols and approximately 5.3 million
  shots per process; one UQ and nine IBM process datasets are represented in
  the authenticated JSON files. Page 4 says interactions during tomography
  operations and dynamics shorter than the measurement pulse are not
  captured. Pages 8-10 identify a dominant neighboring transmon only as the
  simplest model, report additional qubits and classical sources, and state
  that the nearest-neighbor model does not account for all measured
  non-Markovianity. IBM frequency and interaction strength were not
  controllable. The JSON objects are aggregate setting/outcome counts, not
  attempt IDs, pulse/controller logs, failures, timestamps, reset records, or
  memory interventions.
- Finding: the work establishes implementable, informationally complete
  system-side multi-time tomography in its stated three-time basis. It does
  not establish a complete physical source, a direct memory grammar, a
  break-on-memory map, or an SPB attempted-run law. Calling its reconstructed
  `W` the boundary would be target-built and is correctly forbidden.

### P-T-03 - Xiang supplies an engineered two-transmon predecessor, but only system interventions and fitted analysis

- Severity: high evaluation blocker; no defect in the printed ceiling.
- Category: physical-source and apparatus.
- Affected claims: `C6`-`C8` and the `SPB-S3` role ceiling.
- Evidence: exact `SPB-S3`, pp. 2-5, prepares neighboring transmons `S` and
  `E`, applies CNOT-CZ and CZ-CNOT interactions, and inserts a nine-element
  basis of projective/POVM operations on `S`; the reported object is explicitly
  a restricted process tensor. The paper characterizes reduced CZ maps for
  selected initial `E` states but does not cross the held-out process with
  read, toggle, randomize, reset, isolate, and reset-isolate instruments on `E`
  at the cut. It also reports postselection and an omitted near-zero-probability
  trajectory. Its conclusion links only analysis code. At the authenticated
  `qucse` commit, `plot_fig_02.py`, `plot_fig_03.py`, `plot_fig04c.py`, and
  `process_tenor_fit.py` import an external `DataVaultWrapper`; no corresponding
  raw DataVault is tracked.
- Finding: the source supports physical plausibility of an engineered
  two-transmon system-memory experiment and restricted system projections. It
  does not supply the complete memory battery or raw apparatus lineage.
  Fitted process matrices cannot substitute for the absent DataVault.

### P-T-04 - The two-transmon architecture is physically meaningful without a fundamental factorization premise

- Severity: moderate scope condition, not a contract rejection.
- Category: apparatus and semantic.
- Affected claims: `C1`, `C6`, `C7`, and contract Sections 6.1-6.3.
- Evidence: `SPB-S2` describes separate XY/flux control, dedicated readout
  resonators, a measured coupling, and a dominant neighboring transmon;
  `SPB-S3` directly controls two neighboring transmons. The contract explicitly
  retains `E_perp`, controllers, readout, and leakage and calls Hilbert/operator
  language a benchmark rather than ontology.
- Finding: separate ports, pulse calibrations, response matrices, and reader
  records are enough to define an effective operational `S` and `M`. The test
  need not assume fundamental tensor factors. It does require the evaluation
  packet to show independent addressability over the full registered pulse,
  leakage, and readout regimes. Addressability cannot be inferred merely from
  two qubit names.

### P-T-05 - Break and read backaction are measurable maps, not harmless observations

- Severity: high apparatus duty for an evaluation pin.
- Category: apparatus.
- Affected claims: `C4`, `C7`, and contract Sections 6.3-6.7.
- Evidence: the UQ sequence in exact `SPB-S2`, p. 4, uses a roughly 2 microsecond
  mid-circuit measurement interval while `S` and its environment may interact;
  the source expressly says this interaction is not captured by its
  tomography. The frozen readiness audit identifies measurement photons,
  residual coupling, Stark shifts, crosstalk, shared resonators, and feedback
  latency as break-on-`M` channels. An informationally complete `M-READ`
  necessarily has a classical outcome and a post-read state.
- Finding: causal-break and `M-READ` branches are feasible only as calibrated
  instruments including their action on `M`, leakage, resonators, and
  controller. Informationally complete tomography immediately before and
  after the break cannot noninvasively reveal the same individual scored
  trajectory. The only physically valid reading already entailed by contract
  Section 6.3 is ensemble/matched-copy calibration, with destructive validation
  copies excluded from scored continuations. A same-shot nondisturbing reading
  would be an impossible duty and receives no credit.

### P-T-06 - Toggle, randomization, reset, and isolation are feasible only with retained destinations and quantitative budgets

- Severity: high apparatus duty for an evaluation pin.
- Category: apparatus and physical-source.
- Affected claims: `C4`, `C7`, `C11`, and contract Sections 6.5-6.7, 8, and 11.
- Evidence: neither `SPB-S2` nor `SPB-S3` executes the registered battery at a
  cut. Both platforms nevertheless exhibit the ingredients for microwave
  toggles, measurement, preparation, and frequency control on a custom device.
  The sources also expose residual qubits, dissipation, material/electronic
  noise, readout infidelity, and finite `T1/T2`. The contract keeps seed,
  disposal, reset, controller, reservoir, residual coupling, leakage, failure,
  energy, and latency records.
- Finding: `M-X`, `M-RAND-R`, `M-RESET`, and approximate `M-ISO` are technically
  feasible on a suitably instrumented custom two-transmon device. Perfect
  decoupling and metaphysical erasure are not. `M-RAND-U` is meaningful only if
  the seed is causally unavailable to the licensed continuation, not merely
  hidden from the analyst; its physical register and disposal path remain in
  the parent. Active reset must retain measurement records, resonator ringdown,
  heat/bath destination, retries, leakage, thermal repopulation, and recovery
  time. Isolation needs measured residual `ZZ`, exchange, bus, drive, readout,
  and leakage bounds over every held-out duration. `M-RESET-ISO` removes only
  the named logical carrier within those bounds.

### P-T-07 - Instrument-level complete attempts are obtainable; microscopic closure is not

- Severity: moderate scope condition and high source-closure duty.
- Category: apparatus and procedural.
- Affected claims: `C4`, `C7`, `C11`, and contract Sections 2 and 8.
- Evidence: the existing public JSON records contain aggregate successful
  counts only. The contract, by contrast, requires attempt identity, commands,
  seeds, boundary outcomes, reader and nuisance transcripts, and abort,
  timeout, leakage, stale, overwritten, and hardware-failure states. It also
  expressly permits unmonitored residual environment as printed debt leading
  to `T8`.
- Finding: a custom acquisition stack can log every issued program, compiler
  artifact, FPGA/AWG command, RNG seed, acknowledgement, classifier output,
  timeout, dropped record, calibration epoch, and accessible monitor. It cannot
  measure every material defect, bath mode, emitted photon, or microscopic
  controller degree without changing the experiment. The contract remains
  physical because it asks for complete retained attempts plus explicit
  inaccessible debt, not omniscience. Any claim of microscopic source closure
  would be impossible and is outside the printed award.

### P-T-08 - Temporal composition is feasible and noncircular only with frozen reusable interval instruments

- Severity: high anti-target-leakage duty.
- Category: apparatus and semantic.
- Affected claims: `C1`, `C2`, `C8`, `C11`, and contract Sections 5, 6.8, 9,
  and 11.
- Evidence: neither temporal experiment reports a direct three-segment SPB
  run. Contract Section 6.8 freezes interval maps before the direct `ABC`
  circuit, forbids an `ABC` process tensor, repeats with a seam intervention,
  and charges map dimension and calibration. Section 6.2 explicitly marks a
  full process and full history as anti-controls.
- Finding: separate interval characterization followed by a direct `ABC` run
  is physically feasible. It tests, rather than assumes, whether `S`, `S+M`,
  or a larger printed candidate carries the needed correlations. A distinct
  map for each held-out control word, a process tensor fitted to `ABC`, or a
  history table growing with the target is target-built and earns no
  composition/descent credit. Algebraic equality of the two bracketings is a
  conformance check; the direct complete-record run supplies the empirical
  comparison.

### P-T-09 - Exact temporal packet remains absent and is fully identifiable

- Severity: high; blocks `SPB-L1` and every empirical temporal conclusion.
- Category: physical-source, apparatus, and procedural.
- Affected claims: `C4`, `C6`-`C8`, `C11`, `C12`, and the ladder ceiling.
- Evidence: the exact sources and repositories contain no run crossing the
  full memory grammar, no raw Xiang DataVault, and no complete attempt or
  three-segment packet.
- Finding: the exact missing temporal packet is: immutable device and qubit
  identities; topology, Hamiltonian-control range, firmware/compiler and pulse
  bytes; calibration epoch; independently calibrated `S` and `M` preparations
  and informationally complete instruments including leakage; the measured
  causal-break-on-`M` map and sham/idle controls; all eight `M` branches with
  seed access proofs, reset destinations, resonator recovery, and isolation
  budgets; crosstalk, residual-mode, bath and controller inventory; nontrivial
  history separation and boundary-equivalence validation copies; frozen
  incompatible futures and adaptive-record scope; reusable `A/B/C` interval
  instruments and direct three-segment runs; every attempted-run row including
  failure and data-loss states; split/randomization objects; calibration and
  nuisance covariance; and immutable raw bytes plus analysis environment.
  No present source supplies that packet, and this review performs no repair or
  acquisition.

## 4. P-T conclusion

The temporal contract is a physically meaningful, nonvacuous test at the
printed effective two-transmon and accessible-record scope. The cited sources
correctly function as complementary predecessors, not a completed SPB run.
No registered temporal operation is impossible when interpreted as a finite-
accuracy instrument on ensemble-calibrated hardware. Perfect nondisturbing
pre/post state revelation, perfect isolation, literal information destruction,
and microscopic environmental completeness would be impossible, but the
frozen contract does not require them. The complete temporal evaluation packet
is absent, so this report awards no empirical rung and makes no separate joint
disposition recommendation.

Report LF line count: `000278`

Report byte count: `017034`

Report normalized self-SHA-256:
`be2addc42b10255f65732728e03de3b32a75b338d3a32b888dfa65c26bcdfac1`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
