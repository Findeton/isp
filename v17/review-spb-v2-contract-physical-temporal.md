# SPB v2 contract review - Seat P-T temporal physical-source/apparatus report

Date: 2026-08-24

Seat: P-T (temporal preparation, carrier, instrument, and reader)

Review state: independently frozen read-only subreport; scientific result awarded: none

## 1. Independence and authenticated review boundary

I performed this review read-only. I did not inspect, contact, or receive any
sibling v2 reviewer or sibling v2 report. I made no repository edit and used
no later source to repair the pin. The unrelated untracked
`v16/note-handoff-prompt-2026-08-22.md` was excluded.

The checked-out commit is
`7221d777cc341b9e5f9ee010f44f642d5a45d4ea`; its sole parent is
`915f1c2bad3c97337b0e7b74d1f97e9f8f16cce8`. The pin is present in HEAD,
has 560 LF lines, 26,284 bytes, and raw SHA-256
`f2f982e55f8b4d9cc26626f830fc2bd5b99dc0fd5067539ac3611183303fa1d7`.
Applying pin Section 8.1 exactly reproduces normalized self-SHA-256
`8d46d1a7c499a4f9f11b534142d9ae5815dfcf41e12ce8942d77917278bf2425`.
It ends in one LF and has no trailing horizontal whitespace. Worktree bytes
for the pin and every frozen repository dependency equal HEAD.

Authenticated seven-object v2 bundle:

| Object | LF lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `v17/note-foundational-assumption-deletion-programme.md` | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` |
| `v17/research-incubator/active/assumptions/v17_assumption_parallel_synthesis_and_next_gates.md` | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` |
| `v17/research-incubator/active/spb/v17_spb_primary_source_receipt_manifest.md` | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` |
| `v17/research-incubator/active/spb/v17_spb_p0_physical_platform_and_source_audit.md` | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` |
| `v17/note-spb-sufficient-physical-boundary-contract-review-adjudication.md` | 702 | 27687 | `5f7719af388afedf962282ba9b29924bfa6da6af917219ecdde6cd6f5aeff5ac` |
| `v17/research-incubator/active/spb/v17_spb_v2_result_neutral_gate_contract.md` | 1282 | 47642 | `71990429c4c3d8c8ed841298950bf142895a9754f4184532ca31e975c57d9775` |
| `v17/research-incubator/active/spb/v17_spb_v2_root_readiness_and_countermodel_audit.md` | 555 | 19752 | `fc5dcfee9dd32572c1cb8cfe059d617a195bedee1883dbd31acb6e67b17fe63b` |

Authenticated terminal v1 dependencies:

| Object | LF lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `v17/note-spb-sufficient-physical-boundary-contract-review-pin.md` | 489 | 22169 | `b5491cd698af90f6603f1597a8724f9614d0d255fef5b0da0c9b54686ac6c75d` |
| `v17/review-spb-contract-mathematics-statistics.md` | 443 | 23617 | `1b80d6ef86a3983ec9a9a40da23b4ef8c918010ed1ffcab55d2826628f1ee998` |
| `v17/review-spb-contract-physical-temporal.md` | 278 | 17034 | `631a68aefa628f355fb5ae1616a0e389b7cd98cad9074c9495c3532cf9289fff` |
| `v17/review-spb-contract-physical-regional.md` | 279 | 17144 | `5ca35981cfef951d0c875c34e1c8d03a8a59627a739f085e7a1828dc7b439d81` |
| `v17/review-spb-contract-physical-joint.md` | 245 | 15277 | `c986d3359071b8aa5e9f37411b2f5641b594a63756b67af8195fe93ff02e2a74` |
| `v17/review-spb-contract-foundations-ontology.md` | 373 | 19859 | `fd29f31e809b64490fce332875c13ec32e11e63c138973b7b595721ec10abaa2` |
| `v17/note-spb-sufficient-physical-boundary-contract-review-adjudication.md` | 702 | 27687 | `5f7719af388afedf962282ba9b29924bfa6da6af917219ecdde6cd6f5aeff5ac` |

All six exact PDFs in `/private/tmp` reproduce the pin's byte counts and
SHA-256 identities. For the temporal sources these are Pollock v1, 896,695
bytes, `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc`;
Giarmatzi v3, 6,601,486 bytes,
`ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28`;
and Xiang v2, 1,276,514 bytes,
`cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242`.
The three regional PDF identities were also authenticated before inspection.

The `NMN-tomo` repository is clean at
`154235f8bbf5e70eb71c325370a67b1894490452`. Its four consumed receipts
reproduce exactly: `README.md`, 904 bytes,
`fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593`;
`All codes.ipynb`, 1,399,666 bytes,
`b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1`;
`NMN_lab_rslts.json`, 20,177 bytes,
`b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43`;
and `NMN_tomog_rerun.json`, 176,825 bytes,
`450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657`.
The `qucse` repository is clean at
`81998e861ae43541d03738c15d7c60715be37309`; its tracked tree contains
fitted matrices and analysis products but no laboratory DataVault.

Authentication passes. It awards no scientific or empirical rung.

## 2. Review standard

I treated `S` and `M` as effective, independently addressable apparatus
roles, not fundamental tensor factors. I distinguished ensemble-calibrated
instruments from nondisturbing single-shot state revelation, logical reset
from information destruction, a seed hidden from an analyst from a carrier
physically inaccessible to the licensed continuation, and a complete retained
attempt ledger from microscopic environmental omniscience.

## 3. Findings

### P-T-V2-01 - Pollock supplies an all-controls causal-break criterion, not a memory carrier

- Severity: none for the frozen role; high if promoted to apparatus evidence.
- Category: physical-source and semantic.
- Affected claims: `V2-C7`, `V2-C8`, and the `SPB-S1` ceiling.
- Exact evidence: exact `SPB-S1`, pp. 2-3 and Fig. 1, defines a causal break
  by an output preparation independent of its input and declares a process
  Markovian only when every later normalized system state depends on the
  freshly prepared state, not on the prior measurement outcome or controls.
  The paper represents memory as an unspecified external environment. It
  selects no transmon, memory port, reader, reset, isolation operation,
  controller, reservoir, or source packet.
- Finding: the v2 source role is exact. Pollock justifies the operational
  break and memory witness but cannot identify `M`, close `S+M`, or validate
  any physical memory operation.

### P-T-V2-02 - Giarmatzi is complete only for its registered system-side three-time grammar

- Severity: high evaluation-packet blocker; no source-scope defect.
- Category: physical-source and apparatus.
- Affected claims: `V2-C7`, `V2-C8`, and the `SPB-S2` ceiling.
- Exact evidence: exact `SPB-S2`, pp. 2-5, implements sequential
  measure-reprepare operations on the system over 324 protocols and about
  5.3 million shots per process. Page 4 and Fig. 2 state that the system can
  interact with its environment during tomography and that dynamics shorter
  than the measurement pulse are not captured. Pages 7-11 state that a
  nearest-neighbour qubit is only a simple model, that other qubits,
  electronics, material defects, and classical fluctuations also contribute,
  and that this model does not account for all observed non-Markovianity.
  Table 3 says `ibm_perth` offered no frequency or interaction-strength
  control. The authenticated JSON objects are aggregate setting/outcome
  counts, not per-attempt controller, failure, reset, or memory-operation logs.
- Finding: the source supports full system-side process reconstruction at its
  basis and timing scope. It does not supply direct `M` instruments, the
  break-on-`M` map, a complete attempt law, or source closure around the named
  neighbouring qubit. V2 states all four limits.

### P-T-V2-03 - Xiang supplies a two-transmon system-memory predecessor, not the SPB memory battery

- Severity: high evaluation-packet blocker; no source-scope defect.
- Category: physical-source and apparatus.
- Affected claims: `V2-C7`, `V2-C8`, and the `SPB-S3` ceiling.
- Exact evidence: exact `SPB-S3`, pp. 2-5 and Figs. 1-3, uses two neighbouring
  transmons as `S` and ancilla environment `E`, applies CNOT-CZ and CZ-CNOT
  sequences, and inserts a nine-element complete POVM basis on `S`. The paper
  repeatedly calls the reconstructed object a restricted process tensor,
  postselects projection outcomes, and omits one near-zero-probability
  trajectory in Fig. 3. Figure 2(d) changes initial `E` states only for reduced
  gate characterization. Page 7 says `E` simulates an environment and the
  method applies when microscopic noise is beyond measurement or control.
  The exact `qucse` scripts `plot_fig_02.py`, `plot_fig_03.py`,
  `plot_fig04c.py`, and `process_tenor_fit.py` instantiate an external
  `DataVaultWrapper`; the corresponding DataVault is absent from the commit.
- Finding: Xiang establishes physical plausibility of an engineered
  two-transmon memory and system-side intervening projections. It does not
  cross a held-out family with `M-ID`, `M-READ`, `M-X`, both randomizations,
  reset, isolation, and reset-isolation, and fitted CSV matrices cannot replace
  the missing raw attempts.

### P-T-V2-04 - The named two-transmon architecture is physically feasible at effective apparatus scope

- Severity: none for feasibility; high identity/calibration duty for an
  evaluation packet.
- Category: apparatus and scope.
- Affected claims: `V2-C7`, `V2-C14`, and contract Sections 8.1-8.3.
- Exact evidence: exact `SPB-S2`, pp. 3 and 8-9, reports separate XY/flux
  controls, dedicated readout resonators, a dominant coupled transmon, and
  measured device parameters. Exact `SPB-S3`, pp. 3-4, directly controls two
  neighbouring transmons. V2 names `S`, `M`, `E_perp`, controller, readout,
  and leakage, and calls density operators/instruments operational coordinates.
- Finding: independently calibrated ports, pulse families, leakage levels,
  readout instruments, and coupling maps are enough to define operational
  `S` and `M`; no fundamental factorization premise is needed. Addressability
  must be demonstrated throughout the registered pulse, readout, reset, and
  isolation regimes, not inferred from two qubit labels. The selected
  architecture is feasible but no exact serial-labelled implementation is
  presently pinned.

### P-T-V2-05 - Causal-break backaction is a measured instrument map, and the common score keeps its traces

- Severity: high apparatus duty; no v2 semantic defect.
- Category: apparatus, causal typing, and record scope.
- Affected claims: `V2-C1`-`V2-C3`, `V2-C8`, and contract Sections 2.1,
  6, 8.4, and 8.6.
- Exact evidence: exact `SPB-S2`, p. 4, uses a roughly two-microsecond
  mid-circuit measurement interval while system-environment interaction may
  continue and expressly says that interaction is not captured. On the
  selected hardware, measurement photons, Stark shifts, shared-feedline
  effects, residual exchange/`ZZ`, crosstalk, reset pulses, and feedback
  latency are credible `S`-break-to-`M` channels. V2 Section 8.4 requires the
  calibrated action of the break on `M`, input outcome, reset attempts,
  prepared setting, acknowledgements, latency, leakage, failure, matched idle,
  sham-readout, and break-on-memory controls.
- Finding: the break is feasible only as a finite-accuracy instrument whose
  action on `M` is calibrated on matched copies. Informationally complete
  pre/post measurement cannot reveal the same individual memory trajectory
  nondestructively. V2 does not require that impossibility: destructive
  validation copies are separated from scored continuations, and any
  future-accessible log, pulse residue, or heat load must remain in `b` or
  `n_star`. If such a trace were projected out, the pin's future-readable-log
  mutant would invalidate the estimand rather than manufacture screening.

### P-T-V2-06 - Every typed memory operation is feasible only with its physical destinations and failures retained

- Severity: high apparatus and source-closure duty; no impossible idealization
  remains in the contract.
- Category: apparatus and physical-source.
- Affected claims: `V2-C2`, `V2-C8`, `V2-C14`, and contract Sections 8.5,
  8.6, 11.1, and 11.3.
- Exact evidence and finding:

| Branch | Physical reading required by v2 | Apparatus assessment |
|---|---|---|
| `M-ID` | drift and residual coupling | feasible as a matched-duration control, not literal absence of action |
| `M-READ` | outcome plus post-read backaction | feasible as an informationally complete ensemble instrument on validation copies or randomized scored branches; impossible as nondisturbing single-shot state revelation, which v2 does not request |
| `M-X` | pulse execution, leakage, crosstalk | feasible with independent calibration and common-space failure outcomes |
| `M-RAND-R` | seed/controller future-accessible | feasible; the seed carrier is part of the candidate/nuisance record and cannot be removed by scoring |
| `M-RAND-U` | seed unavailable to the licensed continuation, with access proof and disposal route | feasible only by a physical access separation; hiding a database column while a controller retains the seed fails |
| `M-RESET` | retries, old record, reservoir, resonator, heat, latency, recovery | feasible finite active reset; it is not erasure of information from the universe |
| `M-ISO` | residual exchange, `ZZ`, bus, drive, readout, leakage bounds | feasible as bounded detuning/echo/decoupling; perfect isolation is neither feasible nor claimed |
| `M-RESET-ISO` | all reset and isolation records | feasible only as the serial composition of the two calibrated instruments, with both failure routes retained |

The two temporal sources demonstrate the control ingredients but neither
executes this battery at a candidate cut. Reset exports a record and entropy;
randomization exports or sequesters a seed; isolation leaves a measured
residual. V2 keeps all three facts and therefore survives the physical-export
countermodel.

### P-T-V2-07 - Controller/reference memory, leakage, reservoirs, and inaccessible debt remain part of the test

- Severity: moderate scope condition and high evaluation duty.
- Category: apparatus, records, and source closure.
- Affected claims: `V2-C2`, `V2-C7`, `V2-C8`, `V2-C14`, and contract
  Sections 2.1, 8.1-8.6, and 11.
- Exact evidence: `SPB-S2` reports extra qubits, a common feedline, dedicated
  resonators, control electronics, material defects, classical fluctuations,
  and model mismatch. `SPB-S3` reports dissipation of both qubits to a larger
  lossy environment, measurement-induced transitions, neighbouring-qubit
  crosstalk, clock phase noise, and photon-number fluctuations. V2 freezes an
  access graph and inventories controllers, references, clocks, reservoirs,
  residual environments, leakage, drift, every issued attempt, every data-loss
  route, and inaccessible debt.
- Finding: instrument-level complete attempts are obtainable; microscopic
  closure of every bath mode is not. A custom stack can retain commands,
  programs, RNG lineage, FPGA/AWG acknowledgement, pulse timing, classifier
  output, timeout, retry, dropped record, calibration epoch, reset destination,
  and accessible monitor. Unmeasured material/bath degrees remain declared
  debt and can force failure or underdetermination. They cannot be regressed
  away as drift or appended as an answer-selected memory after held-out data.

### P-T-V2-08 - Direct three-interval composition and a distinct second regime are feasible and target-blind as typed

- Severity: high no-target-leakage and transfer duty; no contract defect.
- Category: apparatus, composition, and transfer.
- Affected claims: `V2-C6`-`V2-C8`, `V2-C12`, `V2-C14`, and contract
  Sections 4, 7, 8.7, 8.8, and 11.
- Exact evidence: neither temporal source reports an SPB direct three-interval
  target. V2 requires reusable `K_A`, `K_B`, and `K_C` characterized without
  the direct `ABC` run, seam instruments including all memory records, one
  independently calibrated shared nuisance law, a normalized complete-attempt
  prediction, and a direct circuit. A fitted `ABC` process tensor is an
  anti-control. `rho_1` is disjoint and must materially change duration,
  coupling, pulse family, preparation family, or device while naming allowed
  standard recalibrations.
- Finding: this is physically executable on a sufficiently instrumented
  two-transmon device. Residual `E_perp` memory may make the local kernels fail
  or their composition underdetermined; that is an empirical outcome, not an
  infeasibility. A per-control-word map, full-history table, or `ABC`-fitted
  nuisance parent is target-built and fails descent/composition. Primary `C`
  and each `X_g` retain distinct subjects, so a transferred screening law
  cannot be reported as transferred composition.

### P-T-V2-09 - The exact temporal evaluation packet is absent, with no ambiguous missing object

- Severity: high; blocks temporal `SPB-L1` and every empirical temporal claim.
- Category: physical-source, apparatus, and procedural.
- Affected claims: `V2-C7`, `V2-C8`, `V2-C12`, `V2-C14`, `V2-C15`, and the
  ladder ceiling.
- Exact evidence: the authenticated PDFs and repositories contain no run that
  crosses the full memory grammar, no Xiang laboratory DataVault, no per-attempt
  causal-break source lineage, no reusable interval packet, and no direct
  three-interval or second-regime SPB run.
- Exact missing facts and bytes:

1. immutable device, chip, qubit, resonator, feedline, cable, controller,
   clock, refrigerator, and acquisition identities; topology, control range,
   coupling model, firmware/compiler/FPGA/AWG/RNG versions, pulse/program
   bytes and hashes, timing, retry, routing, and raw destinations;
2. one calibration epoch with independent `S` and `M` preparations,
   informationally complete instruments/readers, readout-confusion and
   leakage models, their backaction and covariance, and material-change rule;
3. the measured causal-break action on `M`, including matched idle,
   sham-readout, and break-on-memory controls, preparation independence,
   latency, leakage, noncompliance, and failure;
4. executed bytes and calibration records for all eight `M` branches, including
   seed-retention/access graphs, physical inaccessibility proof and disposal,
   reset retries/old record/reservoir/resonator/heat/recovery, and duration-wise
   residual exchange/`ZZ`/bus/drive/readout/leakage isolation budgets;
5. the controller/reference register, residual-mode and `E_perp` inventory,
   crosstalk, thermal and dissipation paths, inaccessible debt, and all
   future-accessible log/pulse/heat destinations;
6. frozen memory-different, `S+M`-matched, controller-different, depth-mutant,
   and duplicate-label history pairs; validation-copy boundary matching,
   history separation, incompatible futures, and common finite outcome schema;
7. the exact `kappa`/`E_star` map, nuisance projection, access certificates,
   assignment and seed law, randomization/interleaving, split objects,
   scientific margins, power, simultaneous multiplicity, and stopping rule;
8. target-independent `K_A/K_B/K_C`, seam operations, parameter sharing,
   shared nuisance law, resource/sub-target certificate, direct `ABC` attempts,
   and a separately frozen `rho_1` plus permitted recalibrations; and
9. every issued-attempt row, including compiler substitution, noncompliance,
   abort, timeout, missing, invalid, leakage, stale/overwritten, recovery, and
   hardware failure, with immutable raw bytes, calibrations, analysis code,
   dependency lockfiles, and reproducible environment.

No present source supplies these facts or bytes. Simulation cannot supply
them, and this report performs no repair or acquisition.

## 4. Temporal conclusion

The temporal arm is a physically meaningful, nonvacuous, finite-accuracy test
at the printed effective two-transmon and licensed-access scope. Causal-break
backaction, memory readout, both randomization branches, reset destinations,
finite isolation, controller/reference memory, leakage, reservoirs, heat,
latency, recovery, and all failures are retained as apparatus rather than
assumed away. Direct three-interval composition and a materially distinct
second regime are feasible. The exact temporal run packet does not close, so
this subreport awards no empirical rung and makes no separate disposition
recommendation.

Report LF line count: `000323`

Report byte count: `020571`

Report normalized self-SHA-256:
`e82b8ae526b0dcaab87c7fed86354d1af6fd98aaf7e02ec423d6701f353d4f62`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
