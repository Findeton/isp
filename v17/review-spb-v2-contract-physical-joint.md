# SPB v2 contract review - Seat P joint physical-source/apparatus disposition

Date: 2026-08-24

Seat: P (joint temporal-regional physical-source and apparatus review)

Review state: independently frozen read-only report; empirical boundary result awarded: none

## 1. Independence and authenticated review boundary

I performed the temporal, regional, and joint physical review read-only after
authenticating the pin. I did not inspect, contact, or receive any sibling v2
reviewer or sibling v2 report. I made no repository edit, performed no in-pin
repair, and used no source outside the frozen receipts to enlarge a claim. The
unrelated untracked `v16/note-handoff-prompt-2026-08-22.md` was excluded.

The checked-out commit is
`7221d777cc341b9e5f9ee010f44f642d5a45d4ea`; its sole parent is
`915f1c2bad3c97337b0e7b74d1f97e9f8f16cce8`. The 560-LF-line, 26,284-byte
pin has raw SHA-256
`f2f982e55f8b4d9cc26626f830fc2bd5b99dc0fd5067539ac3611183303fa1d7`
and normalized self-SHA-256
`8d46d1a7c499a4f9f11b534142d9ae5815dfcf41e12ce8942d77917278bf2425`.
The pin ends in LF and has no trailing horizontal whitespace. Every frozen
repository object equals HEAD.

The authenticated seven-object v2 ledger is:

| Object | LF lines | Bytes | SHA-256 |
|---|---:|---:|---|
| governing programme | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` |
| synthesis | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` |
| source receipt manifest | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` |
| P0 physical/source audit | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` |
| terminal v1 adjudication | 702 | 27687 | `5f7719af388afedf962282ba9b29924bfa6da6af917219ecdde6cd6f5aeff5ac` |
| v2 gate contract | 1282 | 47642 | `71990429c4c3d8c8ed841298950bf142895a9754f4184532ca31e975c57d9775` |
| v2 root/countermodel audit | 555 | 19752 | `fc5dcfee9dd32572c1cb8cfe059d617a195bedee1883dbd31acb6e67b17fe63b` |

The terminal v1 pin and M, P-T, P-R, P-joint, O, and adjudication objects
authenticate respectively as 489/22169/`b5491cd698af90f6603f1597a8724f9614d0d255fef5b0da0c9b54686ac6c75d`,
443/23617/`1b80d6ef86a3983ec9a9a40da23b4ef8c918010ed1ffcab55d2826628f1ee998`,
278/17034/`631a68aefa628f355fb5ae1616a0e389b7cd98cad9074c9495c3532cf9289fff`,
279/17144/`5ca35981cfef951d0c875c34e1c8d03a8a59627a739f085e7a1828dc7b439d81`,
245/15277/`c986d3359071b8aa5e9f37411b2f5641b594a63756b67af8195fe93ff02e2a74`,
373/19859/`fd29f31e809b64490fce332875c13ec32e11e63c138973b7b595721ec10abaa2`,
and 702/27687/`5f7719af388afedf962282ba9b29924bfa6da6af917219ecdde6cd6f5aeff5ac`.

All six exact PDFs authenticate by bytes/SHA-256: Pollock
896695/`cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc`,
Giarmatzi
6601486/`ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28`,
Xiang
1276514/`cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242`,
Lawniczak
1835223/`597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5`,
Kostrykin-Schrader
307827/`1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e`,
and Farooq
3291194/`dcc126a0910c2c7f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f`.
The clean author repositories authenticate at
`154235f8bbf5e70eb71c325370a67b1894490452` and
`81998e861ae43541d03738c15d7c60715be37309`. Authentication passes but
awards no scientific or empirical result.

## 2. Separate feasibility and packet-closure findings

### P-J-V2-01 - The temporal test is physically feasible, but its exact run packet does not close

- Severity: none for feasibility; high evaluation-packet blocker.
- Category: temporal apparatus and source closure.
- Affected claims: `V2-C1`-`V2-C8`, `V2-C12`, `V2-C14`, and `V2-C15`.
- Exact evidence: Pollock provides the all-controls causal-break criterion but
  no carrier. Giarmatzi supplies full registered system-side three-time
  tomography while expressly leaving sub-pulse system-environment dynamics
  and broader environmental contributions outside that reconstruction. Xiang
  supplies a restricted two-transmon system-ancilla process tensor, system-side
  projections, postselection, and code, but its scripts call an absent
  DataVault and it does not execute the v2 memory grammar. The contract types
  break backaction, `M-ID`, `M-READ`, `M-X`, both randomizations, reset,
  isolation, reset-isolation, controller/reference traces, leakage, reservoirs,
  failures, direct `ABC`, and a disjoint second regime.
- Finding: a sufficiently instrumented two-transmon apparatus can execute
  these finite-accuracy operations. The operations need not reveal a single
  trajectory nondestructively, erase information globally, or isolate
  perfectly. Their measured backaction, destinations, access graph, residuals,
  retries, heat, latency, and failures remain in the attempted-run law. No
  exact serial-labelled device, full crossed run ledger, direct interval
  composite, or second-regime packet is frozen, so feasibility supplies no
  packet bytes.

### P-J-V2-02 - The regional test is physically feasible, but its exact run packet does not close

- Severity: none for feasibility; high evaluation-packet blocker.
- Category: regional apparatus and source closure.
- Affected claims: `V2-C9`-`V2-C12`, `V2-C14`, and `V2-C15`.
- Exact evidence: Farooq proves ideal scalar one-contact equality but reports
  only almost-perfect measurements of separate networks through distinct
  leads. Lawniczak establishes `S^(I)=T4^-1 S^(II) T4`, measures a four-port
  system through six two-port reconnections with 50-ohm loads, and publishes
  trace/transformed-component evidence, not fixed-labelled-port equality.
  The printed `T4` has `T4^dagger T4` eigenvalues `2-sqrt(2)` and
  `2+sqrt(2)`, each twice, so no scalar normalization makes it a passive
  lossless adapter. Kostrykin-Schrader proves generalized star-product results
  for unitary scattering of self-adjoint finite graph Laplacians, not noisy,
  lossy, calibrated laboratory modules.
- Finding: fixed-plane complete multiport characterization, independently
  calibrated adapters, stochastic noise/reference kernels, global seam
  solving, and direct pair/triple reconnection are physically realizable. The
  collar is the actual ports, finite region, modes, reference planes, sources,
  readers, connectors, loads, adapters, epoch, and hidden-channel audit, not
  merely `S`. No exact common-collar raw packet, joint stochastic law, or
  direct target-blind assembly exists in the frozen sources.

### P-J-V2-03 - Physical feasibility does not substitute for source bytes

- Severity: decisive rung boundary.
- Category: joint apparatus, source closure, and procedure.
- Affected claims: `V2-C14`, `V2-C15`, pin Sections 7 and 10, and the stopping
  rule.
- Exact evidence: both arms have implementable effective carriers and finite
  registered outcome spaces, but every frozen source predates an exact v2
  apparatus/run pin. The microwave raw matrices are request-only; the Xiang
  DataVault is absent; no source has the crossed memory battery or target-blind
  direct triple.
- Finding: the contract asks an empirical question without defining its
  answer. Neither exact arm packet presently closes. No screening,
  composition, transfer, boundary, or necessity result follows in this cycle.

## 3. Independent reconstruction of the 16 binding hostile countermodels

Each routing check below is physical or source-facing; synthetic success
tests the contract only and earns no apparatus rung.

1. **Literal history in score.** Let histories be `h=0,1` and all physical
   future records have law `R`. Scoring `(h,R)` gives total variation one even
   though the carrier laws agree. The v2 common execution map sends both
   correctly executed labels to `COMPLIANT`; it does not copy `h`. Result:
   the label-cloning mutant is rejected.
2. **Future-readable log omitted.** If the `h=1` controller retains `L=1` and
   the `h=0` controller retains `L=0`, then `L` is a physical future-accessible
   trace. Projecting it away would falsify the estimand. V2 puts it in the
   boundary/nuisance record, restoring total variation one. Result: syntax is
   removed, physical memory is not.
3. **Interval straddles the margin.** With scientific margin 0.10, an interval
   `[0.02,0.20]` proves neither equivalence nor material difference. Reader or
   calibration uncertainty cannot enlarge the margin. Result:
   `UNDERDETERMINED`, not a forced apparatus pass or fail.
4. **Threshold closeness is nontransitive.** For `0`, `0.75 delta`, and
   `1.5 delta`, consecutive points are within `delta` but endpoints are not.
   Result: validation matching is not a presentation equivalence and cannot
   create a quotient carrier.
5. **Equal coherent response, unequal complete laws.** Two modules with
   `S=0` differ when one is noiseless and the other emits `+sigma/-sigma` or
   times out with positive probability. Result: deterministic equality earns
   only the coherent control; complete kernels retain noise and failure.
6. **Incompatible cyclic kernels.** Binary conditions `X=Y` and `Y=1-X`
   are each normalized locally but have no joint realization. Result: the
   composition routes to no compatible stochastic law, never post-hoc
   renormalization.
7. **Nonunique cyclic kernels.** Conditions `X=Y` and `Y=X` admit both point
   masses `(0,0)`, `(1,1)`, and their mixtures. Result: local kernels do not
   select a joint; target data may not select it after assembly.
8. **Nonunique interior, unique exterior.** In
   `K a_s=V S_se a_e`, take `K=0`, `S_se=0`, and `S_es=0`. Every internal
   amplitude solves the seam but the exterior response is unique. Result: v2
   separates existence, interior uniqueness, and exterior uniqueness.
9. **Regular global solve, singular sequential pivot.** A three-module block
   system may be invertible while one selected Schur pivot is singular.
   Result: the direct global prediction remains physical; the failed
   bracketing is an algorithmic status, not empirical nonassociativity.
10. **Pairwise-good, triple-bad.** The iid uniform law on three bits and the
    uniform even-parity law have identical one- and two-bit marginals but
    total variation one-half. Result: direct target-blind `ABC` is mandatory.
11. **Primary composition passes, composition transfer fails.** A frozen rule
    can predict direct `ABC` in `rho_0` and fail in `rho_1`. Result: primary
    `C` passes while `X_C` fails; the subjects are not collapsed.
12. **Screening transfer passes, composition transfer fails.** The candidate
    can preserve the screening relation in `rho_1` while its triple rule
    fails. Result: `X_S` passes and `X_C` fails; no scalar transfer verdict
    hides the distinction.
13. **Larger pass, predecessor unknown.** If `T-B1` passes but `T-B0` has a
    screening interval straddling its margin, the larger carrier is not shown
    required. Result: necessity remains underdetermined until every applicable
    strict predecessor is actually refuted.
14. **Active cable permutation.** A software relabelling that leaves the
    serial-labelled cable map fixed can be passive; physically swapping cables
    changes connector histories and loads. Result: the latter is an
    intervention, with calibration, noise, and resource charges.
15. **Exporting memory operations.** Reset displaces records and entropy to
    controller/reservoir/heat; readable randomization retains a seed;
    unavailable randomization needs a physical access barrier and disposal;
    isolation leaves calibrated residual coupling and pulse history. Result:
    every accessible destination and failure remains scored or declared debt.
16. **Target-sized predictive table.** A table indexed by every direct-target
    control word can reproduce target outcomes while encoding the target
    itself. Result: prediction alone is insufficient; it fails independent
    descent, reusable-component, and sub-target resource criteria.

These reconstructions leave no load-bearing physical counterexample against
the printed v2 contract. They do block every attempt to substitute coherent
matrices, fitted target tables, hidden logs, or pairwise marginals for the
registered complete test.

## 4. Exact missing apparatus/run facts

### 4.1 Temporal packet

The temporal arm still requires immutable bytes for one named serial-labelled
chip/device stack; `S`, `M`, controller, resonator/feedline, refrigerator,
clock/reference, cable and acquisition identities; topology, coupling/control
range, firmware/compiler/FPGA/AWG/RNG versions; pulse and program hashes;
timing, routing, retry, and raw destinations. It needs one calibration epoch
with independent preparations and informationally complete ensemble
instruments for `S` and `M`, confusion/leakage/backaction/covariance objects,
and a material-change rule.

It further needs the measured causal-break action on `M`, matched idle,
sham-readout and break-on-memory controls; actual executions and failures for
all eight memory branches; readable-seed lineage, unavailable-seed physical
access proof and disposal; reset retries, old records, resonator/reservoir,
heat, latency and recovery; finite isolation budgets for exchange, `ZZ`, bus,
drive, readout and leakage; controller/reference and residual-mode inventory;
future-accessible logs; inaccessible debt; frozen history-pair batteries;
common outcome map; access certificates; assignment law; margins, power,
multiplicity and stopping; target-independent interval kernels and nuisance
law; direct `ABC`; disjoint `rho_1`; every issued-attempt sentinel; immutable
raw attempts, calibration lineage, code, dependency locks and reproducible
environment. None is supplied as a complete exact packet.

### 4.2 Regional packet

The regional arm still requires immutable module, interior, collar, port,
cable, connector, adapter, ancillary-port, load, calibration-standard,
source, receiver/VNA, clock/reference, environment and acquisition identities,
with topology, dimensions, impedances, orientation, torque/replug state,
firmware, settings and epoch. It needs literal cross-sections, finite collar,
admitted modes/polarizations, common physical reference planes, impedance and
phase/frequency conventions, serial port-to-cable maps, and hidden,
evanescent, common-mode and radiative-channel validation.

It further needs two distinct interiors at one carrier; independently
characterized adapters with forward/inverse maps, ancillas, terminations,
loss/gain, noise, phase, dynamic range, saturation and costs; raw complex
incident/reflected records; every calibration/replug/failure attempt;
linearity, power/intermodulation, stationarity, hysteresis, saturation,
mode-conversion, drift and noise-wave validation; independently measured
module/connector/load/adapter kernels; one target-independent shared
reference/nuisance/noise law with cross-port and cross-seam correlations;
joint-law existence/uniqueness/normalization evidence; global range/kernel,
exterior-uniqueness and conditioning checks; frozen sequential pivots; direct
two-module targets and one direct `ABC` with held-out substitution; no-refit
splits and `rho_1`; all issued-attempt sentinels; immutable raw bytes,
calibration lineage, code, locks and reproducible environment. None is
supplied as a complete exact packet.

## 5. Joint disposition and rung

All frozen physical-source and apparatus claims survive as printed. The
contract is noncircular at apparatus level, selects feasible effective
carriers, preserves physical traces rather than treatment syntax, keeps
complete failure and stochastic laws, distinguishes algebra from direct
assembly, and prints the correct primary-source ceilings. Its feasibility is
not an empirical result, and the absent packets cannot be inferred from
papers, fitted products, simulation, or this review.

Joint disposition recommendation: SPB-D4 — ACCEPT.

Maximum rung awarded by this report: SPB-L0 — RESULT-NEUTRAL CONTRACT
INDEPENDENTLY ACCEPTED.

No boundary exists-by-result claim, empirical screening or composition claim,
minimality/necessity claim, ontology claim, chronology claim, or spacetime,
gravity, or unification claim is awarded.

Report LF line count: `000282`

Report byte count: `016602`

Report normalized self-SHA-256:
`f13be91419f3d44c4c59614ee57b2b325100e26fd4e823410d7409e6da79a598`

Normalization rule: replace decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
