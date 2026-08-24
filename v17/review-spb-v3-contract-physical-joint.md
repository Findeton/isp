# SPB v3 contract review - Seat P joint physical-source/apparatus disposition

Date: 2026-08-24

Seat: P (joint temporal-regional physical-source and apparatus review)

Review state: independently frozen read-only report; empirical boundary result
awarded: none

## 1. Independence, authentication, and signed subreports

I performed the temporal, regional, and joint physical review read-only after
authenticating the v3 pin. I did not inspect, contact, or receive any current
sibling reviewer or current sibling report. I inspected the terminal v2
dependencies because pin Section 3 makes them review evidence. I made no
repository edit, contract repair, candidate selection, apparatus acquisition,
simulation-as-result, empirical inference, or source substitution. The
unrelated untracked `v16/note-handoff-prompt-2026-08-22.md` was excluded.

`HEAD` and a fresh Git-object hash both resolve the pin commit as
`fed678f4a5986f8025b828c319a6dcc3377ac222`. Its sole parent is
`0a74a362bf6fb3b7e30dc0366c54c89d6d515f07`; its tree is
`bb206ef2005f34f0667785a702e0fc1760a9bc11`, and the parent tree is
`46cdbc04922f2be37c4ff9e479ed93875f9b0f2e`. The only parent-to-pin change is
the addition of the pin file, Git blob
`e517da009d8e4b8a5b874d15b0f6739dee35b34a`.

The pin has 619 LF lines and 30,921 bytes, raw SHA-256
`9d0529b3baa19fd54817609e79bf37ecfed969b83c9b8cd90490885c597d07a5`,
and normalized self-SHA-256
`b155501fd9ed549b3436e145e86b97f6f87a7383322ff8dbe8c57d8864e8c9c4`
under Section 9.1. It ends in one LF and contains no trailing horizontal
whitespace.

The frozen seven-object ledger authenticates as follows:

| Object | LF lines | Bytes | SHA-256 |
|---|---:|---:|---|
| foundational programme | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` |
| parallel synthesis | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` |
| source-receipt manifest | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` |
| P0 platform/source audit | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` |
| terminal v2 adjudication | 705 | 29792 | `8d89e91cf0a3e354989a398d00328c76f7c86d9e22219687cc8d1a45070618f1` |
| v3 gate contract | 1624 | 60659 | `06b5f87ce2de2e31d82622d07f8aba80b47606a1d46224c2fd73545618ba3c54` |
| v3 pre-pin adversarial audit | 575 | 23014 | `80dd14c5be7397e2676771f067279909b740fe62e935f33d8d71b58f9a016ce5` |

Every object ends in LF and has no trailing horizontal whitespace. All 13
entries of `SPB_V3_SHA256.txt` reproduce against the parent commit. The
terminal v2 pin, M, P-T, P-R, P-joint, O, and adjudication dependencies also
reproduce their 560/26284, 613/33833, 323/20571, 343/21484, 282/16602,
467/31734, and 705/29792 line/byte identities and their seven Section 3 raw
SHA-256 values exactly.

I independently retrieved every exact scholarly receipt. The identities and
source-role ceilings are:

| Source | Bytes | SHA-256 | Maximum authenticated role |
|---|---:|---|---|
| Pollock v1 | 896695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | causal-break/memory criterion |
| Giarmatzi v3 | 6601486 | `ce0c1dc116b0394dce9c526e7d230b89b69a27726641c9c4110905fc7ddadc28` | system-side multi-time tomography |
| Xiang v2 | 1276514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` | engineered two-transmon predecessor |
| Lawniczak publisher PDF | 1835223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` | measured conjugate multiport response |
| Kostrykin-Schrader | 307827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` | graph star-product theorem |
| Farooq publisher PDF | 3291194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` | ideal one-port equality and approximate control |

The author repositories authenticate at exact commits
`154235f8bbf5e70eb71c325370a67b1894490452` and
`81998e861ae43541d03738c15d7c60715be37309`. All four consumed `NMN-tomo`
files reproduce their receipt hashes. The `qucse` tree contains fitted/derived
objects and scripts calling an external `DataVaultWrapper`, but no laboratory
DataVault. Authentication passes and supplies no apparatus result.

The separately signed subreports frozen before this joint object are:

| Subreport | LF lines | Bytes | Raw SHA-256 | Normalized self-SHA-256 |
|---|---:|---:|---|---|
| `/tmp/spb-v3-review-seat-p-temporal.md` | 297 | 18105 | `07487f2b03a13d74f757754092755a2fd81c895ed0402cc5bd48d319da48f94e` | `0c8fabde14e6691b804dd72c72240f54ee3763dfbdd62e9e5466d59a6ff6717b` |
| `/tmp/spb-v3-review-seat-p-regional.md` | 300 | 18097 | `bd468f07baf77a07bc9ff4b5daae7d33d7161786f9a0921335087f69d266855e` | `d7b422c4fc487ca5677df67e464f83595534e7075073a365d04d857761ebdadb` |

## 2. Source truth

### P-J-V3-01 - The six exact sources support the printed architectures and no more

- Severity: none at the frozen ceilings; decisive scope violation if any
  source is promoted to a complete run, carrier, adapter, or composition law.
- Category: joint physical-source and scope-binding.
- Affected claims: `V3-C8`-`V3-C11`, `V3-C14`, and `V3-C17`.
- Exact evidence: Pollock identifies an operational causal-break criterion but
  no memory carrier. Giarmatzi supplies system-side multi-time tomography and
  public counts but not the crossed named-memory grammar. Xiang supplies an
  engineered system-ancilla predecessor and restricted process tensor but no
  public laboratory DataVault or full memory battery. Farooq supplies exact
  ideal scalar equality and approximate separate-network measurements.
  Lawniczak supplies multiport conjugacy under a nonunitary-up-to-scalar
  transplantation map and request-only data. Kostrykin-Schrader supplies a
  unitary self-adjoint graph theorem, not a noisy lossy apparatus law.
- Finding: the receipt manifest, P0 audit, v3 contract, and pin agree exactly.
  No abstract, later version, branch, fitted matrix, paper result, algebra, or
  simulation has been substituted for a receipt or physical packet.

## 3. Physical coherence

### P-J-V3-02 - Both arms define complete causal experiments rather than observational comparisons

- Severity: none for the frozen contract; decisive packet duty.
- Category: joint causal identification and attempted-run apparatus.
- Affected claims: `V3-C1`-`V3-C3`, `V3-C6`, `V3-C9`, `V3-C11`-`V3-C14`,
  and `V3-C17`.
- Exact evidence: contract Sections 2 and 7 separate context, assignment,
  execution, and observation; require a physical randomizer or complete
  rejectable transport bridge; preserve positivity, consistency, staged-policy
  timing, carryover, ITT failures, one common schema, `Pi_0`, shared-parent
  correlations, and normalized composition. Sections 8-10 type temporal
  backaction/destinations and regional collars/adapters/seams. Section 11
  inventories readers, nuisance, references, debt, failures, and resources.
- Finding: the temporal arm can randomize histories, causal breaks, memory
  instruments, and futures without postselecting reset/readout failure. The
  regional arm can randomize or validly transport interior substitution,
  reconnection, and exterior policies while retaining assembly failure and
  carryover. Future-accessible matter cannot be deleted through the comparison
  or nuisance projections. Initial preparation and direct connected targets
  share the registered instrument/schema, but targets train nothing. Failure
  of exogeneity, positivity, model validity, existence, uniqueness,
  stationarity, or conditioning routes invalid/underdetermined/fail rather than
  manufacturing a pass.

### P-J-V3-03 - The physical readers and intervention grammars do not demand impossible idealizations

- Severity: none; scope-binding.
- Category: joint apparatus coherence.
- Affected claims: `V3-C8`-`V3-C14` and `V3-C17`.
- Exact evidence: temporal `M-READ` is an ensemble instrument on validation
  copies or randomized branches; reset retains reservoirs, old records, heat,
  retries, latency, and recovery; isolation is finite and retains residual
  coupling. Regional readers include source/load backaction, references, noise,
  hidden modes, saturation, hysteresis, conversion, and failures. Active cable
  changes and nonunitary adapters are physical channels, not presentation.
  Deterministic and stochastic seam statuses remain separate.
- Finding: the contract asks for finite-accuracy calibrated instruments, not
  nondisturbing single-shot state revelation, perfect isolation, universal
  erasure, passive implementation of an arbitrary nonunitary map, or
  microscopic omniscience. I reconstructed treatment-log leakage, correlated
  randomizer, positivity, carryover, postselection, omitted seed/heat, equal-S
  unequal-law, active-as-passive, singular-pivot/global-solve, pair-good/triple-
  bad, and target-sized-table mutants. Each is retained, rejected, or routed
  without changing the physical question.

### P-J-V3-04 - B3 admission is physically typed and presently supplies no candidate apparatus

- Severity: none for `V3-C10`; decisive scope condition for any later B3,
  poset, minimality, or necessity claim.
- Category: joint material-carrier and scope-binding.
- Affected claims: `V3-C8`, `V3-C10`, `V3-C15`, and `V3-C16`.
- Exact evidence: Sections 8.2 and 9.3 require any `H_T,k` or `H_R,k` member to
  have material substrate, serials, topology, preparation, write/hold/read/reset
  grammar, retention/failure law, access, references, costs, and a complete
  kernel. Abstract histories and higher kernels remain coordinate controls.
  Before acquisition, a separately authorized physical pin must instantiate
  exactly one complete member or remove the row; data cannot choose, and an
  uninstantiated row cannot enter scoring, order, minimality, or necessity.
- Finding: neither B3 row is an existing apparatus object. The rule repairs the
  terminal v2 referent defect without silently deleting an inconvenient result.
  An added record bank or interface-memory device changes the experiment and
  retains its write/loading disturbance and resources. This review performs
  neither instantiation nor removal.

## 4. Architecture-bounded feasibility

### P-J-V3-05 - Both selected architectures are feasible in bounded principle

- Severity: none for feasibility; feasibility awards no packet or empirical
  claim.
- Category: joint physical feasibility.
- Affected claims: `V3-C7`-`V3-C14` and `V3-C17`.
- Exact evidence: the exact temporal sources separately demonstrate
  system-side multi-time tomography and an engineered two-transmon
  system-memory process. The exact regional sources separately demonstrate
  one-port different-interior control, multiport conjugate response, and graph
  scattering composition. P0 Sections 4 and 6 specify finite two-transmon and
  three-module microwave architectures and their missing operations.
- Finding: a sufficiently instrumented two-transmon platform can execute
  preparation, causal break, direct memory interventions, and interval
  pair/triple circuits. A modular microwave platform can implement a fixed
  collar, independently calibrated source/readout, real connectors/adapters,
  interior substitution, and pair/triple assemblies. Expense, sample size,
  calibration burden, finite accuracy, and possible underdetermination do not
  make either experiment impossible in principle. This is architecture-bounded
  feasibility only; it neither predicts an outcome nor establishes existence
  of a sufficient boundary.

## 5. Exact-packet closure

### P-J-V3-06 - Neither exact physical packet exists

- Severity: decisive blocker for `SPB-L1+` and every empirical SPB claim; not a
  contract defect and not a negative physical result.
- Category: joint apparatus/source closure and rung boundary.
- Affected claims: `V3-C17`, the cumulative ladder, and all future temporal or
  regional empirical predicates.
- Exact evidence: P0's temporal and regional admission matrices and minimum
  packet lists identify missing direct intervention, complete-attempt, raw,
  and composition objects. The exact source PDFs and repositories contain no
  crossed temporal memory battery and no fixed-collar complete stochastic
  pair/triple packet. Contract Section 18 and pin Sections 5.7, 11, and 12 state
  the absence explicitly.
- Finding: the temporal arm lacks the serial device, randomizer/exogeneity,
  preparation, full memory-operation/backaction, complete issuance/failure,
  direct `AB`/`BC`/`ABC`, transfer, B3 decision, calibration, code, and lineage
  bytes enumerated in the temporal subreport. The regional arm lacks the common
  collar, module/interior, source/reader/reference, randomizer, complete
  stochastic/seam, adapter/connector, direct pair/triple, transfer, B3
  decision, calibration, raw, code, and lineage bytes enumerated in the
  regional subreport. Feasibility, request-only data, fitted products, algebra,
  and simulation cannot fill any missing byte.

## 6. Final contract audit and disposition

### P-J-V3-07 - The final v3 law repairs the terminal v2 physical-contract defects

- Severity: none; no load-bearing physical/source semantic defect found.
- Category: joint contract semantics and physical apparatus.
- Affected claims: `V3-C1`-`V3-C18`.
- Exact evidence: compared with the terminal v2 adjudication Sections 2 and 6,
  v3 adds a physically identified randomization route and complete transport
  alternative, strict nonvacuity/power duties, explicit normalized `Pi_0`,
  disjoint feedback/seam/bracketing routes, material B3 admission grammars,
  physical embeddings, antichain/necessity quantifiers, duty-specific outcomes,
  complete source/resource ledgers, and the no-packet/no-ontology ceiling.
- Finding: I found no physically impossible, circular, target-leaking,
  untyped-carrier, source-scope, collar/adapter/seam, attempted-run,
  preparation, reader, nuisance, failure, or packet-presence assertion that
  defeats a submitted claim. The printed effective apparatus, finite candidate
  family, licensed-access graph, task/regime, margin/power, and no-result
  restrictions already bind the scope; no additional narrowing is required.

Recommended disposition: **SPB-D4 — ACCEPT**.

Recommended maximum rung: **SPB-L0 — RESULT-NEUTRAL CONTRACT INDEPENDENTLY
ACCEPTED**, subject to root authentication and adjudication.

No apparatus packet, boundary existence, empirical screening or composition,
minimality, necessity, ontology, actuality, chronology, spacetime, gravity, or
unification result is awarded. No physical acquisition or further packet work
is authorized by this report.

Report LF line count: `000253`

Report byte count: `015003`

Report normalized self-SHA-256:
`92f99f693987cd8b5cad4f18262ccb311d859844fd3b78379dc0c423d1f3e19d`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
