# SPB v3 contract review - Seat P-T temporal physical-source/apparatus report

Date: 2026-08-24

Seat: P-T (temporal preparation/metrology and reader/nuisance)

Review state: independently frozen read-only subreport; scientific result
awarded: none

## 1. Independence and authenticated review boundary

I performed this review read-only after the v3 pin commit existed. I did not
inspect, contact, or receive any current sibling reviewer or current sibling
report. I inspected the terminal v2 dependencies because pin Section 3 makes
them review evidence. I made no repository edit, repair, candidate choice,
apparatus acquisition, simulation-as-result, empirical inference, or source
substitution. The unrelated untracked
`v16/note-handoff-prompt-2026-08-22.md` was excluded.

`HEAD` and a fresh Git-object hash both resolve the pin commit as
`fed678f4a5986f8025b828c319a6dcc3377ac222`. Its sole parent is
`0a74a362bf6fb3b7e30dc0366c54c89d6d515f07`; its tree is
`bb206ef2005f34f0667785a702e0fc1760a9bc11`, and the parent tree is
`46cdbc04922f2be37c4ff9e479ed93875f9b0f2e`. The only parent-to-pin change is
the addition of
`v17/note-spb-v3-sufficient-physical-boundary-contract-review-pin.md`, whose
Git blob is `e517da009d8e4b8a5b874d15b0f6739dee35b34a`.

The pin has 619 LF lines and 30,921 bytes. Its raw SHA-256 is
`9d0529b3baa19fd54817609e79bf37ecfed969b83c9b8cd90490885c597d07a5`.
Applying pin Section 9.1 exactly reproduces normalized self-SHA-256
`b155501fd9ed549b3436e145e86b97f6f87a7383322ff8dbe8c57d8864e8c9c4`.
It ends in one LF and contains no trailing horizontal whitespace.

The seven frozen scientific repository objects authenticate from the parent
and pin trees as follows:

| Object | LF lines | Bytes | SHA-256 |
|---|---:|---:|---|
| foundational programme | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` |
| parallel synthesis | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` |
| source-receipt manifest | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` |
| P0 platform/source audit | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` |
| terminal v2 adjudication | 705 | 29792 | `8d89e91cf0a3e354989a398d00328c76f7c86d9e22219687cc8d1a45070618f1` |
| v3 gate contract | 1624 | 60659 | `06b5f87ce2de2e31d82622d07f8aba80b47606a1d46224c2fd73545618ba3c54` |
| v3 pre-pin adversarial audit | 575 | 23014 | `80dd14c5be7397e2676771f067279909b740fe62e935f33d8d71b58f9a016ce5` |

Every object ends in LF and has no trailing horizontal whitespace. The
13-entry `SPB_V3_SHA256.txt` convenience manifest also reproduces every entry
against the parent commit. The terminal v2 pin, M, P-T, P-R, P-joint, O, and
adjudication objects authenticate respectively as
560/26284/`f2f982e55f8b4d9cc26626f830fc2bd5b99dc0fd5067539ac3611183303fa1d7`,
613/33833/`e9fa22d3776c74b90301bcec46731784d2f475a5fac4ed69ee32415cdf3b4152`,
323/20571/`8c7e662703dce98fd9bfa6c6f8e7e12c707ee8db5a191508994f4b792f0de5be`,
343/21484/`776b0a8b0513cf4f56b0bca8d32c3f108cc5fc85cdcef58ea8fe6f29305dd89a`,
282/16602/`74839181f605f74fd5df3d5c11bb58943d77682f437cd3b630c0d7cf6dc8a3ad`,
467/31734/`0c20b0a59f10e6f3338fa38e5ef715d4faa7a3f13b7303970e858a83259d4736`,
and
705/29792/`8d89e91cf0a3e354989a398d00328c76f7c86d9e22219687cc8d1a45070618f1`.

I independently retrieved all six exact scholarly objects before source
inspection; all reproduce the pin's byte counts and SHA-256 identities. The
temporal receipts are:

| Source | Bytes | SHA-256 | Authenticated ceiling |
|---|---:|---|---|
| Pollock et al., arXiv:1801.09811v1 | 896695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | causal-break/memory criterion only |
| Giarmatzi et al., arXiv:2308.00750v3 | 6601486 | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` | system-side multi-time tomography only |
| Xiang et al., arXiv:2105.03333v2 | 1276514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` | engineered system-memory predecessor only |

The exact `NMN-tomo` commit
`154235f8bbf5e70eb71c325370a67b1894490452` exists and its four consumed files
reproduce the manifest: `README.md`, 904 bytes,
`fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593`;
`All codes.ipynb`, 1,399,666 bytes,
`b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1`;
`NMN_lab_rslts.json`, 20,177 bytes,
`b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43`;
and `NMN_tomog_rerun.json`, 176,825 bytes,
`450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657`.
The exact `qucse` commit
`81998e861ae43541d03738c15d7c60715be37309` exists. Its tree contains fitted
matrices and analysis products, while four analysis scripts call an external
`DataVaultWrapper`; no corresponding laboratory DataVault is present.
Authentication passes and awards no empirical rung.

## 2. Review standard

I treated `S`, `M`, controllers, resonators, baths, and record media as
effective serial-labelled apparatus roles, not fundamental tensor factors. I
distinguished a randomized assignment from a logged schedule; ensemble
metrology from nondisturbing single-shot state revelation; reset from universal
erasure; bounded isolation from perfect decoupling; an operational coordinate
from matter; and architecture-bounded feasibility from an existing packet.

## 3. Findings

### P-T-V3-01 - Temporal source truth and ceilings remain exact

- Severity: none at the printed ceiling; high if any source is promoted to a
  carrier, complete apparatus, or SPB run packet.
- Category: physical-source and scope-binding.
- Affected claims: `V3-C8`-`V3-C10`, `V3-C17`, and `SPB-S1`-`SPB-S3`.
- Exact evidence: exact `SPB-S1`, pp. 2-3, defines a causal break by measurement
  and independent repreparation and attributes surviving dependence to an
  external environment; it names no physical memory device. Exact `SPB-S2`
  reports system-side multi-time tomography and public count files, but states
  that interaction during the measurement pulse is not captured, identifies
  only a dominant memory transmon, and discusses electronics, defects, other
  qubits, and fluctuations. Exact `SPB-S3` uses neighboring `S` and `E`
  transmons with CNOT/CZ orders and a restricted projection process tensor; it
  also reports dissipation to a larger environment. The authenticated `qucse`
  tree lacks its referenced laboratory DataVault.
- Finding: the pin uses each source only for its demonstrated criterion or
  predecessor architecture. No paper, count file, process matrix, fitted
  matrix, or simulation is treated as direct memory intervention, source
  closure, or a complete run packet. The source-scope firewall survives.

### P-T-V3-02 - Preparation and metrology are physically coherent but remain packet duties

- Severity: none for contract coherence; high implementation and calibration
  duty before any physical rung.
- Category: temporal preparation and metrology.
- Affected claims: `V3-C2`, `V3-C3`, `V3-C5`, `V3-C12`, and `V3-C17`.
- Exact evidence: contract Sections 7.1-7.3 require normalized,
  target-independent `Pi_0(dx_0,dy_0|u_0,lambda)`, preparation-failure states,
  `Lambda`, and normalized downstream kernels. Sections 8.1, 8.4, and 8.6
  require independently addressable `S` and `M`, validation-copy boundary
  matching, history separation, candidate-specific carrier coordinates, and
  disjoint component/direct-target data. Sections 5-6 require independent
  physical-resolution/loss margins, an above-margin anchor, simultaneous
  coverage, and two-sided power.
- Finding: independent calibration of finite S/M preparations, ensemble
  informationally complete readers, leakage, crosstalk, preparation failure,
  and shared-reference distributions is feasible on a two-transmon platform.
  The scored continuation is not destructively measured to certify its own
  input. Unknown S/M/bath correlations do not get assumed away: they must be
  represented in the frozen preparation/joint law, invalidate its model, or
  cause screening/composition failure. No numerical margin, anchor, `Pi_0`,
  calibration, or power calculation exists in the current packet.

### P-T-V3-03 - The randomizer and complete attempted-run law identify a real ITT experiment

- Severity: none for the frozen law; decisive causal/packet duty if physical
  exogeneity, positivity, consistency, timing, or carryover cannot be certified.
- Category: physical causal identification and attempted-run typing.
- Affected claims: `V3-C1`-`V3-C3`, `V3-C6`, and `V3-C17`.
- Exact evidence: contract Sections 2.1-2.3 separate `Xi`, assigned `A`, literal
  `E`, and physical `Y`; retain acknowledgement, timing, deviations, retries,
  nuisance, and `q`; and map every issued attempt, including noncompliance,
  timeout, missing, inaccessible, and failed branches, into one common
  measurable schema. Section 2.4 requires a physically identified,
  target-independent randomizer, per-cell positivity, source exogeneity,
  consistency without success conditioning, and bounded or blocked carryover.
  Staged choices are pre-fixed policies with sequential exogeneity and
  positivity. Section 8.5 requires `ID-R` for compared break/future assignments
  unless a complete rejectable `ID-T` bridge is separately pinned.
- Finding: a hardware randomizer can issue interleaved history, break, memory,
  and future assignments before their outcomes while an independent attempt
  ledger preserves source, seed lineage, acknowledgements, and failure. This is
  physically meaningful at bounded laboratory scope. Balance or a known
  schedule is not promoted to exogeneity. A common-cause channel, missing
  within-cell arm, descendant adjustment, unbounded reservoir carryover, or
  lost issuance record routes invalid or unidentified rather than passing.

### P-T-V3-04 - Reader, nuisance, backaction, destination, and failure typing is complete at operational scope

- Severity: none for contract coherence; high apparatus duty for every future
  evaluation packet.
- Category: temporal reader and nuisance.
- Affected claims: `V3-C1`, `V3-C2`, `V3-C9`, and `V3-C17`.
- Exact evidence: Sections 2.2 and 11.1 require every future-accessible
  controller log, seed carrier, pulse residue, reservoir change, heat load, and
  other material trace to remain in `b` or `n`, with omission allowed only by a
  predeclared physical inaccessibility certificate. Section 8.5 retains break
  outcome and backaction and defines `M-ID`, `M-READ`, `M-X`, accessible- and
  inaccessible-seed randomization, active reset, finite isolation, and
  reset-isolation with records and failures. The complete temporal score in
  Section 8.6 retains `E_star,b_M,r_S,r_M,r_H,n_T_star,q_T` with typed sentinels.
- Finding: no operation requests nondisturbing revelation of an unknown
  single-run state, global information destruction, exact bath isolation, or
  failure-free reset. `M-READ` is an ensemble instrument on validation copies
  or randomized scored branches. Reset exports old records, entropy, heat,
  resonator state, latency, and retries; randomization exports or sequesters a
  seed; finite isolation retains residual exchange, `ZZ`, bus, drive, readout,
  and leakage bounds. The phrase “nuisance projection” cannot license deletion
  of accessible matter: Sections 2.2 and 15 control 2 make such deletion
  procedural invalidity. Complete means the registered instrument schema and
  declared inaccessible debt, not microscopic omniscience.

### P-T-V3-05 - T-B3 is a material admission type, not an invented apparatus

- Severity: none for the submitted claim; decisive scope condition for any
  future B3 score, minimality, or necessity statement.
- Category: material-carrier typing and scope-binding.
- Affected claims: `V3-C8`, `V3-C10`, `V3-C15`, and `V3-C16`.
- Exact evidence: contract Section 8.2 types `H_T,k` by substrate, serials,
  topology, clocks, record alphabet, write/read/hold/reset instruments,
  retention, overwrite, crosstalk, leakage, failures, blank law, outcome-to-cell
  map, access graph, costs, and a normalized kernel. It expressly rejects an
  abstract response vector, process tensor, or untyped software cache as B3.
  Lines 836-841 require a separately authorized physical pin either to
  instantiate exactly one member by every field or remove `T-B3` from the
  scored roster before acquisition; data cannot choose. An uninstantiated row
  cannot enter scoring, the poset, minimality, or necessity.
- Finding: no actual `H_T,k` exists in this packet, so no B3 apparatus or result
  is inferred. The admission/removal rule closes the v2 referent defect without
  hiding a candidate: an actively written record bank changes the apparatus,
  and its write disturbance, records, reservoirs, and costs remain in the law.
  This review neither instantiates nor removes B3.

### P-T-V3-06 - Direct temporal composition is normalized and target-blind as a contract

- Severity: none for contract coherence; high direct-execution and model duty.
- Category: temporal composition and target-leakage audit.
- Affected claims: `V3-C12`-`V3-C14` and `V3-C17`.
- Exact evidence: Sections 7.1-7.5 supply `Pi_0`, failure-domain closure, piece
  and seam kernels, shared-parent `Lambda`, a normalized iterated law, and
  disjoint feedback statuses. Section 8.6 uses three interval kernels on the
  same carrier and bars separately fitted `ABC` process tensors. Direct `AB`,
  `BC`, and `ABC` circuits are disjoint from component training. Section 7.5
  bars target tomography, de-embedding, residual fitting, normalization,
  correlations, and threshold selection from the prediction.
- Finding: the apparatus can execute reusable interval instruments and direct
  pair/triple circuits on randomized copies. If residual bath correlations make
  the component kernels invalid or a feedback joint nonexistent, nonunique, or
  unresolved, `C` cannot pass. The connected target tests exactly one frozen
  prediction and cannot select a joint or repair it. I found no circular or
  target-leaking physical requirement.

### P-T-V3-07 - No temporal operation is impossible in principle at the printed scope

- Severity: none; scope-binding.
- Category: physical feasibility and hostile-control reconstruction.
- Affected claims: `V3-C7`-`V3-C10`, `V3-C12`, and `V3-C17`.
- Exact evidence: contract Sections 1, 4, 8, 11, and 13 restrict claims to one
  finite effective apparatus, separate duty outcomes, finite-accuracy
  instruments, registered resources, and explicit invalid/underdetermined
  routes. P0 Sections 2 and 4 identify existing system-side tomography and an
  engineered two-transmon predecessor while preserving the missing battery.
- Finding: I attacked the law with treatment-label leakage, future-readable
  logs, correlated pseudo-random seeds, positivity holes, postselected reset
  failures, reservoir carryover, destructive-read assumptions, perfect-reset
  assumptions, latent-bath promotion, target-sized history tables, and
  pairwise-good/triple-bad behavior. The frozen routes reject or retain each
  mutant. The two-transmon architecture is feasible in bounded principle, but
  feasibility neither establishes a carrier's sufficiency nor supplies data.

### P-T-V3-08 - The exact temporal apparatus/run packet is absent

- Severity: high packet-closure blocker; not a defect in the result-neutral
  contract and not a negative boundary result.
- Category: temporal source closure and rung boundary.
- Affected claims: `V3-C17`, the Section 14 ladder, and every future temporal
  empirical predicate.
- Exact evidence: P0 Sections 2.4, 6.1, and 7 state that neither predecessor
  supplies the crossed memory battery or a complete public packet. The v3
  contract Section 18 and pin Sections 5.7, 11, and 12 state that no temporal
  packet exists and that this cycle can award only `SPB-L0`.
- Finding: missing bytes include a serial-labelled S/M device and calibration
  epoch; immutable firmware/pulse/compiler and clock/reference identities;
  physical randomizer source, probabilities, exogeneity audit, seed/access and
  disposal routes; normalized `Pi_0` and shared-parent law; crossed history,
  causal-break, sham/idle, `M-ID`, `M-READ`, `M-X`, both randomizations, reset,
  isolation, and reset-isolation records; complete issuance, failure, leakage,
  reservoir, heat, latency, recovery, and inaccessible-debt schemas; an actual
  B3 instantiation or preregistered removal; margins, anchors, power, and split
  objects; component kernels; direct `AB`, `BC`, and `ABC` raw records; a
  distinct transfer regime; analysis code/environment; and immutable lineage.
  None may be inferred from the exact papers, repositories, feasibility, or
  this report.

## 4. Temporal conclusion

The temporal v3 contract is a physically meaningful, causally identifiable,
finite-accuracy test at its printed effective two-transmon and licensed-access
scope. Preparation/metrology and reader/nuisance duties are separately typed;
the physical randomizer, complete attempted-run schema, initial law, memory
backaction, destinations, failures, and direct triple remain visible. B3 is
only a material admission type until a later separately authorized physical
pin makes the pre-data instantiate-or-remove choice. I found no physically
impossible, circular, target-leaking, source-substituting, or untyped temporal
requirement that defeats the submitted claims.

The exact temporal packet does not exist. This subreport therefore awards no
empirical rung, no screening/composition result, no minimality/necessity result,
and no ontology or downstream conclusion. The sole Seat P disposition is made
only in the separately signed joint report.

Report LF line count: `000297`

Report byte count: `018105`

Report normalized self-SHA-256:
`0c8fabde14e6691b804dd72c72240f54ee3763dfbdd62e9e5466d59a6ff6717b`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
