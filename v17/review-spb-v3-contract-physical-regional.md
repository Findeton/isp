# SPB v3 contract review - Seat P-R regional physical-source/apparatus report

Date: 2026-08-24

Seat: P-R (regional preparation/metrology and reader/nuisance)

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
regional receipts are:

| Source | Bytes | SHA-256 | Authenticated ceiling |
|---|---:|---|---|
| Lawniczak et al., publisher PDF | 1835223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` | measured conjugate multiport response only |
| Kostrykin-Schrader, arXiv:math-ph/0008022 | 307827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` | generalized star-product theorem only |
| Farooq et al., publisher PDF | 3291194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` | ideal one-port equality and approximate laboratory control only |

The two exact author-repository commits were also authenticated:
`NMN-tomo` at `154235f8bbf5e70eb71c325370a67b1894490452` and
`qucse` at `81998e861ae43541d03738c15d7c60715be37309`. Their identities do not add
regional apparatus evidence. Authentication passes and awards no empirical
rung.

## 2. Review standard

I distinguished ideal graph equality, approximate measured agreement,
frequency-independent matrix conjugacy, and literal equality at the same
serial-labelled physical ports. I treated collar volume, modes, reference
planes, sources, receivers, loads, connectors, adapters, calibration epoch,
noise waves, assembly history, and hidden channels as apparatus. I separated
coherent `S` from a complete stochastic law, algebraic bracketing from direct
assembly, and architecture-bounded feasibility from an existing packet.

## 3. Findings

### P-R-V3-01 - Regional source truth and ceilings remain exact

- Severity: none at the printed ceiling; high if ideal equality, conjugacy, or
  a theorem is promoted to fixed-collar complete-law or gluing evidence.
- Category: physical-source and scope-binding.
- Affected claims: `V3-C8`, `V3-C11`, `V3-C14`, `V3-C17`, and
  `SPB-S4`-`SPB-S6`.
- Exact evidence: exact `SPB-S6`, pp. 3-6, proves equality of scalar ideal
  one-contact graph responses through equal M-functions and reports almost
  perfect but finite-accuracy measurements over 0.01-1 GHz; its data are
  request-only. Exact `SPB-S4`, Eqs. (5) and (11), gives
  `S_I=T^-1 S_II T`, not same-labelled-port equality; the four-port matrix is
  reconstructed through six two-port cable/load configurations, and its data
  are request-only. Exact `SPB-S5`, Theorems 3.8-4.1, proves a generalized star
  product and associativity for unitary scattering matrices of self-adjoint
  graph Laplacians under its printed construction.
- Finding: the source roles are not enlarged. Farooq is an ideal scalar
  equality plus approximate separate-network control, Lawniczak is measured
  conjugacy rather than a physical fixed-port adapter or triple, and
  Kostrykin-Schrader is a lossless graph theorem rather than a calibrated
  noisy/lossy apparatus law. None supplies public raw SPB assembly bytes.

### P-R-V3-02 - Preparation and fixed-collar metrology are physically coherent but remain packet duties

- Severity: none for contract coherence; high implementation and calibration
  duty before any physical rung.
- Category: regional preparation and metrology.
- Affected claims: `V3-C2`, `V3-C3`, `V3-C5`, `V3-C11`, `V3-C12`, and
  `V3-C17`.
- Exact evidence: Section 9.1 fixes a collar by serial-labelled port
  cross-sections, finite material region, admitted modes/polarizations,
  impedances, reference planes, cable map, topology, orientation, references,
  and calibration epoch. Sections 7.1-7.3 and 9.6 require a normalized
  target-independent source/preparation law, seam and component kernels,
  connectors, adapters, and shared nuisance/reference parent trained without
  connected targets. Sections 5-6 require independent physical margins,
  anchors, simultaneous coverage, and two-sided power.
- Finding: fixed-plane multiport calibration and controlled source ensembles
  are conventional and feasible. Sequential VNA port-pair measurements are
  admissible only under the registered stationarity and reference model;
  reconnecting a cable, changing a load, shifting a plane, or drifting an
  oscillator is not silently the same collar. Preparation failure, source
  uncertainty, phase/frequency reference state, and common correlations remain
  in `Pi_0`/`Lambda` and the attempted-run schema. No exact collar, preparation
  law, margin, anchor, power calculation, or calibration packet exists here.

### P-R-V3-03 - Interior substitution and reconnection have a real causal ITT route

- Severity: none for the frozen law; decisive causal/packet duty if physical
  exogeneity, positivity, consistency, timing, or carryover cannot be certified.
- Category: physical causal identification and attempted-run typing.
- Affected claims: `V3-C1`-`V3-C3`, `V3-C6`, and `V3-C17`.
- Exact evidence: Sections 2.1-2.4 separate immutable context, assigned
  interior/instrument/exterior policy, literal assembly execution, and physical
  observation. Every issued substitution or reconnection attempt, including
  noncompliance, timeout, missing, inaccessible, failed-calibration, and anomaly
  branches, maps to one common schema and one ITT estimand. `ID-R` requires a
  physical target-independent randomizer, per-cell positivity, source
  exogeneity, consistency without success conditioning, and bounded or blocked
  carryover; a nonrandom schedule needs the full rejectable `ID-T` bridge.
- Finding: interiors, connector/reconnection orders, exterior policies, and
  source settings can be randomized by an independent assignment controller,
  often at block or cluster level because physical exchange is slow. The
  assignment, assembly acknowledgement, serials, operator/controller actions,
  settling, warm-up, and failures remain scored. Hysteresis, connector wear,
  temperature drift, or prior assembly state must be bounded/washout-controlled
  or preassignment-blocked. A balanced schedule or source log alone cannot
  identify substitution.

### P-R-V3-04 - Reader, nuisance, hidden-channel, and failure typing is complete at operational scope

- Severity: none for contract coherence; high apparatus duty for every future
  evaluation packet.
- Category: regional reader and nuisance.
- Affected claims: `V3-C1`, `V3-C2`, `V3-C11`, and `V3-C17`.
- Exact evidence: Section 9.2 distinguishes the coherent coordinate
  `b=S_B a` from a complete kernel containing emitted/thermal/noise waves,
  source/receiver references, drift covariance, nonlinearity, saturation,
  hysteresis, mode conversion, stationarity, missing/invalid/failure outcomes,
  and shared correlations without assuming Gaussianity or independence.
  Sections 9.6 and 11.1 retain collar and wave readers, hidden modes, loads,
  connector state, calibration, readers/backaction, loss, leakage, conversion,
  drift, every attempt, and inaccessible debt.
- Finding: a VNA or equivalent coherent reader physically loads and excites the
  network; it is not an external view from nowhere. Source impedance, receiver
  state, matched-load quality, switch/cable state, dynamic range, thermal
  emission, unadmitted-mode leakage, and failed calibrations remain in the
  response or nuisance law. Complete means the frozen admitted-mode and attempt
  schema with declared debt, not omniscience over every electromagnetic mode.
  Equal coherent `S` with unequal noise, saturation, timeout, or failure laws
  cannot pass the complete-boundary duty.

### P-R-V3-05 - Collars, physical adapters, connectors, and seams are not quotiented away

- Severity: none for contract coherence; high physical-realization and
  conditioning duty.
- Category: regional collars, adapters, and seams.
- Affected claims: `V3-C4`, `V3-C11`, `V3-C13`, `V3-C14`, and `V3-C17`.
- Exact evidence: Section 9.5 makes only a simultaneous coordinate change in
  all sources, responses, readers, records, and likelihoods passive. Cable
  permutation is active. A transplantation/mixing adapter must expose every
  ancillary port, termination, loss, gain, noise, phase, dynamic-range,
  saturation, calibration, and resource charge. The source audit and v3 audit
  reproduce
  `spec(T_4^dagger T_4)={2-sqrt(2),2-sqrt(2),2+sqrt(2),2+sqrt(2)}`, so scalar
  normalization cannot make the printed `T_4` passive unitary. Sections 10.1-
  10.4 separately type seam existence, internal/exterior uniqueness,
  conditioning, a global solve, both sequential pivots, and stochastic
  compatibility.
- Finding: a nonunitary map may be tested only through a real active/lossy
  channel with ancillas, gain/noise, calibration, and loads; software conjugacy
  is not an adapter. The seam equations are realizable for linear network
  feedback, including resonant singular or ill-conditioned cases. A global
  solution can exist while both sequential pivots are singular, and a unique
  coherent mean need not select a noise law. The explicit unresolved/model-
  invalid routes prevent an algebraic singularity or calibration failure from
  being manufactured into physical composition.

### P-R-V3-06 - R-B3 is a material admission type, not a higher-kernel relabeling

- Severity: none for the submitted claim; decisive scope condition for any
  future B3 score, minimality, or necessity statement.
- Category: material-carrier typing and scope-binding.
- Affected claims: `V3-C8`, `V3-C10`, `V3-C15`, and `V3-C16`.
- Exact evidence: Section 9.3 requires `H_R,k` to be an additional material
  interface-memory device, not already part of the collar, with substrate,
  serials, topology, preparation, write/hold/read/reset instruments, retention,
  failure, references, accessible records, costs, and a normalized kernel.
  Volterra, finite higher-response, and nonstationary kernels on the existing
  collar remain coordinate controls. Lines 1017-1022 require a separately
  authorized physical pin either to instantiate exactly one complete member or
  remove `R-B3` from scoring before acquisition; data cannot choose, and an
  uninstantiated row cannot enter the poset, minimality, or necessity.
- Finding: no actual `H_R,k` exists in this packet, so no material-memory
  apparatus or result is inferred. If a device is later inserted, its loading,
  coupling, disturbance, state history, noise, and resource costs change the
  network and remain in the complete law. This review neither instantiates nor
  removes B3.

### P-R-V3-07 - Pair/triple composition is direct, normalized, and target-blind as a contract

- Severity: none for contract coherence; high direct-assembly and model duty.
- Category: regional composition and target-leakage audit.
- Affected claims: `V3-C12`-`V3-C14` and `V3-C17`.
- Exact evidence: Sections 7.1-7.5 require `Pi_0`, normalized component and
  connector kernels, shared-parent `Lambda`, a target-independent global law
  for feedback, and direct pair plus `ABC` targets. Section 9.6 requires at
  least one held-out interior substitution. It bars target-fitted de-embedding,
  planes, adapters, connectors, cross-seam correlations, source state,
  thresholds, and error covariance. Section 10 makes the global triple solve
  primary and both bracketings conformance calculations on one physical
  network.
- Finding: reusable modules and physical seams can be independently
  characterized and then directly assembled. Cross-seam correlations or
  assembly-induced modes that cannot be learned target-independently make the
  stochastic construction invalid, nonunique, or unresolved; they are not fit
  from `ABC`. Pairwise agreement cannot replace the direct triple. I found no
  circular or target-leaking regional requirement.

### P-R-V3-08 - The regional architecture is feasible, but the exact packet is absent

- Severity: high packet-closure blocker; not a defect in the result-neutral
  contract and not a negative boundary result.
- Category: regional feasibility, source closure, and rung boundary.
- Affected claims: `V3-C17`, the Section 14 ladder, and every future regional
  empirical predicate.
- Exact evidence: P0 Sections 3.4, 6.2, and 7 state that no audited source
  combines a common fixed multiport collar, complete stochastic response,
  public raw bytes, registered reconnection, and a direct triple. Contract
  Section 18 and pin Sections 5.7, 11, and 12 state that no regional packet
  exists and that this cycle can award only `SPB-L0`.
- Finding: modular multiport preparation, substitution, reading, and pair/triple
  assembly are feasible in bounded principle. Missing bytes include serial-
  labelled interiors/modules and a literally common collar; complete port,
  mode, plane, impedance, cable, load, connector, adapter, source, receiver,
  oscillator, and epoch identities; a physical assignment source with
  probabilities, exogeneity, timing, and carryover controls; `Pi_0`, complete
  stochastic component/seam kernels, and shared correlations; linearity,
  stationarity, saturation, hysteresis, conversion, and dynamic-range records;
  global and pivot classifier inputs; an actual B3 instantiation or
  preregistered removal; margins, anchors, power, and split objects; direct
  pair/substitution/`ABC` attempts with every assembly and failed-calibration
  record; a distinct transfer regime; raw bytes; code/environment; and immutable
  lineage. Papers, algebra, request-only data, simulation, and feasibility
  supply none of them.

## 4. Regional conclusion

The regional v3 contract is a physically meaningful, causally identifiable,
finite-accuracy test at its printed effective modular-microwave and
licensed-access scope. Preparation/metrology and reader/nuisance duties are
separately typed; the collar, randomizer, common attempted-run schema, initial
source law, adapters, loads, hidden channels, failures, deterministic seam,
stochastic law, and direct triple remain visible. B3 is only a material
admission type until a later separately authorized physical pin makes the
pre-data instantiate-or-remove choice. I found no physically impossible,
circular, target-leaking, source-substituting, or untyped regional requirement
that defeats the submitted claims.

The exact regional packet does not exist. This subreport therefore awards no
empirical rung, no screening/composition result, no minimality/necessity result,
and no ontology or downstream conclusion. The sole Seat P disposition is made
only in the separately signed joint report.

Report LF line count: `000300`

Report byte count: `018097`

Report normalized self-SHA-256:
`d7b422c4fc487ca5677df67e464f83595534e7075073a365d04d857761ebdadb`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
