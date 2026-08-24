# SPB contract review - Seat P joint physical-source/apparatus report

Date: 2026-08-24

Seat: P joint disposition integrating P-T and P-R without averaging

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

## 2. Non-averaged arm conclusions

### Temporal arm

The temporal contract is physically meaningful at an effective,
independently controlled two-transmon scope. Pollock supplies the causal-break
criterion; Giarmatzi supplies complete system-side three-time tomography at
its registered basis/timing scope and public aggregate counts; Xiang supplies
an engineered system-memory predecessor with restricted system projections.
None supplies the registered direct memory grammar, complete attempt ledger,
or three-segment held-out run. Backaction, reset destinations, crosstalk,
controller records, seed access, residual bath channels, and isolation are
measurable finite-accuracy apparatus duties, not assumptions of erasure.

### Regional arm

The regional contract is physically meaningful at a calibrated linear,
time-stationary, single-mode coherent microwave scope with a frozen stochastic
readout/noise parent. Farooq proves exact equality for an ideal scalar
one-contact graph relation and observes close, not literal, equality in two
separately connected physical networks. Lawniczak proves conjugacy and reports
an approximate four-port realization, not fixed-labelled-port equality.
Kostrykin-Schrader proves a unitary self-adjoint graph composition theorem, not
lossy apparatus gluing. No source supplies a common-plane adapter, immutable
raw matrices, or direct pair/triple reconnection.

These conclusions are separate. Temporal feasibility cannot cure a regional
source/interface gap, and regional feasibility cannot establish a memory
carrier. No averaging, majority rule, or cross-arm transfer is used.

## 3. Joint findings

### P-J-01 - Authentication and chronology pass

- Severity: none.
- Category: procedural.
- Affected claims: review validity and all `C1`-`C12` only as authenticated
  objects.
- Evidence: full commit/parent, pin normalized signature, seven frozen object
  identities, six exact PDF byte identities, two clean author commits, and
  four public data/code file receipts all reproduce as recorded before
  scientific inspection.
- Finding: there is no procedural basis to invalidate the scientific review.
Authentication awards no scientific result.

### P-J-02 - The six sources support complementary predecessor roles, not a collaged result

- Severity: high source-scope boundary.
- Category: physical-source and semantic.
- Affected claims: `C1`-`C3`, `C6`-`C10`, and all six source-role ceilings.
- Evidence: Pollock has no apparatus carrier; Giarmatzi has no direct memory
  battery and exposes unmodeled environment; Xiang has only system-side
  restricted projections and no raw DataVault; Farooq has one theoretical
  scalar equality with approximate separate-network measurements; Lawniczak
  has conjugacy and request-only data; Kostrykin-Schrader has a unitary graph
  theorem and no physical reconnection.
- Finding: no one source and no permissible combination executes either SPB
  arm. The frozen package mostly states this correctly. Two phrases require
  the narrow reading already entailed by P0: Farooq's "literal equality" is
  literal for the ideal scalar response, not exact equality of laboratory
  bytes at one transplanted connector; Lawniczak's "measured conjugate
  response" is approximate and not literal fixed-port equality. With those
  printed ceilings enforced, no false source promotion controls the contract.

### P-J-03 - The apparatus duties divide cleanly into feasible tests and forbidden/impossible substitutes

- Severity: high boundary-control finding.
- Category: apparatus and semantic.
- Affected claims: `C1`, `C2`, `C4`, `C6`-`C11`.
- Evidence: the frozen grammar, anti-controls, source debts, and resource
  ledgers were compared with the exact apparatus reported in all six sources.
- Finding:

| Duty or substitute | Physical classification | Consequence |
|---|---|---|
| Effective two-transmon preparation, typed memory instruments, matched-copy backaction calibration, and direct `ABC` execution | feasible on suitably instrumented custom hardware | exact device packet is still missing |
| Nondisturbing informationally complete pre/post tomography of the same individual scored memory trajectory | impossible | only destructive ensemble/validation copies are admissible, as contract Section 6.3 already entails |
| Perfect logical reset, perfect isolation, or destruction of the old information everywhere | impossible | finite reset/isolation budgets and all destinations remain in the parent |
| Seed-unavailable randomization achieved by deleting a logged column while the future controller retains access | circular | fails `M-RAND-U`; physical access and disposal must be demonstrated |
| Full reconstructed process, whole past, per-program interval map, or target-sized history table used as boundary | target-built | anti-control only; no descent/composition credit |
| Fixed-plane coherent multiport metrology and direct two-/three-module assembly | feasible with calibrated modules, connectors, sources and readers | no cited packet performs it |
| Scalar-normalized `T4` used as a passive lossless four-port | impossible because `T4^dagger T4` is not scalar identity | a real lossy/active/ancillary-port adapter is a larger charged physical object |
| Software conjugation, held-out-tuned adapter, held-out connector de-embedding, or fitted composite matrix | circular/target-built | no fixed-interface or composition credit |
| Microscopic transcript of every bath, defect, photon, and controller degree | impossible | the admissible scope is complete retained attempts plus explicit inaccessible source debt |
| Deterministic `S` matrices alone used to predict noisy complete raw transcripts | incomplete | the already required frozen nuisance/noise parent must supply the stochastic relation |

None of the impossible items is needed for the contract's bounded award. Each
is either expressly rejected, converted into a finite operational budget, or
reported as inaccessible debt/underdetermination. The target-built and circular
routes are expressly anti-controls.

### P-J-04 - Complete-record acquisition is possible only at declared instrument scope

- Severity: moderate scope condition and high evaluation duty.
- Category: apparatus and procedural.
- Affected claims: `C4`, `C5`, `C7`, `C9`-`C11`.
- Evidence: existing temporal JSON files are aggregate counts; Xiang raw data
  and both microwave raw packets are absent/request-only. The contract includes
  every attempted program and failure state while expressly permitting
  inaccessible source debt.
- Finding: a complete command/acquisition/assembly ledger is obtainable and
  statistically scoreable. It must include issued attempts that never produce
  a normal science record. It is not microscopic completeness. For SPB-R,
  complete-law prediction requires module/readout noise and drift relations in
  addition to deterministic seam matrices; for SPB-T it requires the joint
  instrument outcomes and controller/reset records, not only final qubit
  states. Unmeasured material/bath modes limit closure and can force the
  printed underdetermination outcomes.

### P-J-05 - Both composition tests are direct and feasible; their algebraic bracketings are not empirical duplicates

- Severity: high no-refit duty.
- Category: apparatus and semantic.
- Affected claims: `C2`, `C8`, `C10`, `C11`.
- Evidence: contract Sections 5, 6.8, 7.5, and 7.6 freeze reusable pieces,
  hold out one direct composite, and treat bracket agreement as conformance.
  No exact predecessor source performs the required direct composite.
- Finding: temporal interval instruments and regional scattering modules can
  be independently characterized and physically composed. The two
  parenthesizations are calculations from the same frozen inputs. Scientific
  evidence comes from their agreement with one direct `ABC` circuit/network,
  including failure/anomaly records and an intervention/substitution at a
  seam. Reconstructing or de-embedding from that final target would make the
  test circular.

### P-J-06 - Exact physical packets are absent in both arms

- Severity: high; absolute ceiling at contract review only.
- Category: physical-source, apparatus, and procedural.
- Affected claims: `C4`, `C6`-`C12`, evaluation readiness, and the ladder.
- Evidence: P-T finding 09 and P-R finding 08 enumerate the absent immutable
  objects; no exact source closes either list.
- Finding: the temporal arm still needs immutable hardware/control identities,
  direct typed `S/M` instruments, break-on-memory and crosstalk maps, all memory
  branches, seed/reset/isolation evidence, residual-bath/controller inventory,
  nontrivial boundary-matching copies, frozen futures/segments, complete
  attempts, nuisance/covariance/split objects, and raw bytes. The regional arm
  still needs immutable modules/interiors/connectors/adapters/loads/reference
  planes, raw complex records, adapter realizability, mode/linearity/power/
  stationarity/noise validation, independently measured modules/connectors,
  direct two-/three-module assemblies, singular policy, complete assembly and
  failure attempts, nuisance/covariance/split objects, and raw bytes. The
  absences are not repairable by simulation or old fitted matrices.

### P-J-07 - Scope-qualified contract acceptance is supported, with no empirical boundary result

- Severity: controlling joint finding.
- Category: physical-source, apparatus, semantic, and procedural.
- Affected claims: `C1`-`C12`, the allowed maximum claim, and the rung ceiling.
- Evidence: every load-bearing physical operation has either a feasible
  finite-accuracy implementation path or a printed fail/underdetermined
  outcome; source promotions, impossible idealizations, target-built objects,
  and circular composition routes are blocked when the explicit source and
  regime ceilings above are applied.
- Finding: the contract defines nonvacuous interventions and direct held-out
  comparisons. Acceptance is restricted to (i) an effective engineered
  two-transmon partition with accessible-record rather than microscopic
  closure, and (ii) calibrated coherent linear time-stationary single-mode
  microwave response with an explicit stochastic nuisance/noise parent.
  Farooq supplies ideal scalar equality plus approximate physical agreement;
  Lawniczak supplies conjugacy; and a physical `T4` adapter, if attempted, is
  a charged enlarged apparatus rather than a gauge. These restrictions are
  already entailed by the frozen bytes and do not edit the contract.

## 4. Joint disposition and ceiling

Joint disposition recommendation: `SPB-D3 — ACCEPT-WITH-SCOPE`.

Maximum ladder recommendation: `SPB-L0` only. No apparatus/source packet closes
for either arm, so no higher rung, empirical screening result, composition
result, physical boundary, ontology, chronology, spacetime, gravity, or
unification claim is awarded. This report authorizes no repair, successor,
simulation-as-result, acquisition, or repository change.

Report LF line count: `000245`

Report byte count: `015277`

Report normalized self-SHA-256:
`e7cd463d711b614f74d023a28cea794509ccaa66edb966349a65691d7d570248`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
