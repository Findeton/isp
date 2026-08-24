# SPB v3 contract review — Seat O foundations, ontology, and gravity firewall

Date: 2026-08-24

Seat: `O` — mutually blind foundations/ontology/gravity-firewall review

Frozen pin: `v17/note-spb-v3-sufficient-physical-boundary-contract-review-pin.md`

Frozen commit: `fed678f4a5986f8025b828c319a6dcc3377ac222`

Frozen parent: `0a74a362bf6fb3b7e30dc0366c54c89d6d515f07`

Review mode: independent, read-only, no sibling v3 report inspected or contacted

Scientific result awarded: none

## 1. Independence, chronology, and authentication

I performed this review independently. I did not inspect, request, receive, or
communicate with any sibling v3 reviewer or sibling v3 report. I made no
repository edit. The only report object I created is this file in `/tmp`. The
unrelated untracked `v16/note-handoff-prompt-2026-08-22.md` remained outside the
review boundary.

### 1.1 Commit and pin authentication

Authentication preceded scientific inspection of the frozen v3 objects.

- Repository `HEAD` resolved exactly to
  `fed678f4a5986f8025b828c319a6dcc3377ac222`.
- The commit is a Git commit with the sole parent
  `0a74a362bf6fb3b7e30dc0366c54c89d6d515f07`, tree
  `bb206ef2005f34f0667785a702e0fc1760a9bc11`, and subject
  `Freeze SPB v3 contract review pin`.
- Its only tree change from the parent is addition of the named v3 pin.
- The pin has 619 LF lines, 30,921 raw bytes, and raw SHA-256
  `9d0529b3baa19fd54817609e79bf37ecfed969b83c9b8cd90490885c597d07a5`.
- Applying the pin's exact normalization rule reproduced normalized
  self-SHA-256
  `b155501fd9ed549b3436e145e86b97f6f87a7383322ff8dbe8c57d8864e8c9c4`.
- The pin contains no CR byte or trailing horizontal whitespace and ends in
  exactly one LF.
- An explicit tracked-path comparison found no working-tree difference from
  the frozen commit for the pin, the seven Section 2 objects, or the Section 3
  terminal dependencies.

Chronology, pin identity, and repository-byte authentication pass.

### 1.2 Seven frozen v3 scientific objects

I authenticated every pin Section 2 object before inspecting its scientific
content. Counts are LF lines and raw bytes.

| object | lines | bytes | observed SHA-256 | result |
|---|---:|---:|---|---|
| `v17/note-foundational-assumption-deletion-programme.md` | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` | match |
| `v17/research-incubator/active/assumptions/v17_assumption_parallel_synthesis_and_next_gates.md` | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` | match |
| `v17/research-incubator/active/spb/v17_spb_primary_source_receipt_manifest.md` | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` | match |
| `v17/research-incubator/active/spb/v17_spb_p0_physical_platform_and_source_audit.md` | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` | match |
| `v17/note-spb-v2-sufficient-physical-boundary-contract-review-adjudication.md` | 705 | 29792 | `8d89e91cf0a3e354989a398d00328c76f7c86d9e22219687cc8d1a45070618f1` | match |
| `v17/research-incubator/active/spb/v17_spb_v3_result_neutral_gate_contract.md` | 1624 | 60659 | `06b5f87ce2de2e31d82622d07f8aba80b47606a1d46224c2fd73545618ba3c54` | match |
| `v17/research-incubator/active/spb/v17_spb_v3_root_pre_pin_adversarial_audit.md` | 575 | 23014 | `80dd14c5be7397e2676771f067279909b740fe62e935f33d8d71b58f9a016ce5` | match |

I read the seven frozen scientific objects in full. I treated the v3 root audit
as an author-side attack record, not as independent evidence that a claim
survives.

### 1.3 Terminal v2 review dependencies

I authenticated all pin Section 3 dependencies. The repeated adjudication is
the same byte object already listed above.

| object | lines | bytes | observed SHA-256 | result |
|---|---:|---:|---|---|
| `v17/note-spb-v2-sufficient-physical-boundary-contract-review-pin.md` | 560 | 26284 | `f2f982e55f8b4d9cc26626f830fc2bd5b99dc0fd5067539ac3611183303fa1d7` | match |
| `v17/review-spb-v2-contract-mathematics-statistics.md` | 613 | 33833 | `e9fa22d3776c74b90301bcec46731784d2f475a5fac4ed69ee32415cdf3b4152` | match |
| `v17/review-spb-v2-contract-physical-temporal.md` | 323 | 20571 | `8c7e662703dce98fd9bfa6c6f8e7e12c707ee8db5a191508994f4b792f0de5be` | match |
| `v17/review-spb-v2-contract-physical-regional.md` | 343 | 21484 | `776b0a8b0513cf4f56b0bca8d32c3f108cc5fc85cdcef58ea8fe6f29305dd89a` | match |
| `v17/review-spb-v2-contract-physical-joint.md` | 282 | 16602 | `74839181f605f74fd5df3d5c11bb58943d77682f437cd3b630c0d7cf6dc8a3ad` | match |
| `v17/review-spb-v2-contract-foundations-ontology.md` | 467 | 31734 | `0c20b0a59f10e6f3338fa38e5ef715d4faa7a3f13b7303970e858a83259d4736` | match |
| `v17/note-spb-v2-sufficient-physical-boundary-contract-review-adjudication.md` | 705 | 29792 | `8d89e91cf0a3e354989a398d00328c76f7c86d9e22219687cc8d1a45070618f1` | match |

I used the terminal v2 adjudication and the independently frozen v2 Seat M and
Seat O findings as hostile evidence, then retested the successor duties against
the v3 bytes. I did not accept any author-side statement merely because it said
that a v2 defect was closed.

### 1.4 Exact scholarly and author-repository identities

Before any source-content use, I independently rehashed the six received local
PDFs. I consumed no later version, abstract, HTML replacement, author copy, or
derived object.

| ID | exact local receipt | bytes | observed SHA-256 | result |
|---|---|---:|---|---|
| `SPB-S1` | `/private/tmp/spb_t_pollock.pdf` | 896695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | match |
| `SPB-S2` | `/private/tmp/spb_t_giarmatzi_v3.pdf` | 6601486 | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` | match |
| `SPB-S3` | `/private/tmp/spb_t_xiang_v2.pdf` | 1276514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` | match |
| `SPB-S4` | `/private/tmp/spb_r_isoscattering.pdf` | 1835223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` | match |
| `SPB-S5` | `/private/tmp/spb_r_star_product.pdf` | 307827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` | match |
| `SPB-S6` | `/private/tmp/spb_r_isoscattering_equal_oneport.pdf` | 3291194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` | match |

Read-only remote verification returned `HEAD` exactly at
`154235f8bbf5e70eb71c325370a67b1894490452` for `NMN-tomo` and exactly at
`81998e861ae43541d03738c15d7c60715be37309` for `qucse`. Direct byte streams
from the immutable `NMN-tomo` commit reproduced all four selected receipts:

| path | bytes | observed SHA-256 | result |
|---|---:|---|---|
| `README.md` | 904 | `fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593` | match |
| `All codes.ipynb` | 1399666 | `b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1` | match |
| `NMN_lab_rslts.json` | 20177 | `b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43` | match |
| `NMN_tomog_rerun.json` | 176825 | `450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657` | match |

The source roles remain ceilings: Pollock supplies a causal-break/memory
criterion, Giarmatzi system-side multi-time reconstruction, Xiang an engineered
system-memory predecessor, Lawniczak measured multiport conjugacy, Kostrykin--
Schrader a theorem under its hypotheses, and Farooq ideal one-port equality
plus an approximate laboratory control. None supplies the complete v3
apparatus, selects a material ontology, or constitutes an SPB run.

## 2. Independent answer to the circularity question

The frozen v3 test does not define its preferred answer into the candidates,
margins, readers, or access graph. It defines a finite, task-relative empirical
predicate whose positive, negative, unknown, and invalid outcomes remain
separately reachable.

The key reasons are:

1. Candidate identity does not confer sufficiency. A candidate must separately
   earn target-independent material descent, implemented instruments, held-out
   screening, and direct composition (contract lines 350--421 and 762--776).
2. Boundary matching is performed on independent validation copies, is
   explicitly nontransitive, requires genuinely separated histories/interiors,
   and can return underdetermined when no pair both separates and matches
   (lines 456--490).
3. Matching and screening margins lie strictly inside total variation's
   diameter, have nonempty inside and outside regions, carry two-sided power,
   and require independently justified physical resolution/loss before held-out
   acquisition (lines 492--528 and 552--597). A blind reader or unavailable
   power returns underdetermined rather than a pass.
4. The complete connected target may score but may not train, normalize,
   de-embed, select a joint law, choose a threshold, or choose a candidate
   (lines 632--639 and 762--776).
5. The licensed access graph is a declared operational scope, not a claim about
   everything in the universe. Every licensed-future-accessible material trace
   remains scored; claims outside the frozen future family are not made
   (lines 169--198 and 86--90).
6. A larger candidate can fail, pass, remain unknown, or be ineligible. An
   uninstantiated B3 type cannot enter scoring, order, minimality, or necessity
   (lines 807--846 and 993--1027).
7. Unknown, invalid, infeasible, or unrun proper candidates block minimality,
   registered necessity, and universal/exclusion headlines (lines 1293--1323
   and 1359--1371).

The apparatus, system/port decomposition, clocks, policies, loss, resolution,
reader family, candidate roster, and access graph remain supplied experimental
inputs. The output is therefore apparatus-, task-, policy-, regime-, margin-,
resolution-, and roster-relative. The contract repeatedly prints that scope
and never promotes it into fundamental necessity or universal sufficiency.

## 3. Terminal v2 defect-to-v3 reconstruction

I independently checked whether the v2 defects survive under new notation.

| terminal v2 defect | v3 reconstruction | Seat O result |
|---|---|---|
| source closure used as causal identification | `ID-R` requires a physical randomizer, exogeneity, positivity, consistency, and carryover control; `ID-T` requires a complete rejectable causal/transport bridge; source closure is separately only an inventory (lines 223--346 and 1213--1233) | repaired |
| maximal margins manufacture equivalence | strict interior margins, positive two-sided gaps, two-sided power, physical resolution/loss, and the matching anchor exclude the diameter endpoints (lines 492--528 and 552--597) | repaired |
| composition lacks an initial law | normalized target-independent `Pi_0`, preparation sentinels, shared-parent law, and explicit iterated composition are supplied (lines 643--711) | repaired |
| feedback/seam/bracketing classifiers overlap or omit finite-resolution cases | ordered priority, global quantifiers, unresolved routes, and ordered `(G,L,R)` bracketing are explicit (lines 713--758 and 1092--1207) | repaired |
| histories or higher kernels are called material B3 carriers | abstract history/higher kernels are coordinate controls only; B3 requires additional material substrate and complete instruments and is an ineligible admission type until separately instantiated (lines 807--846 and 993--1027) | repaired |
| a suggestive order and minimal antichain become individual necessity | order requires a physical embedding and commensurate duties; minimal antichains and registered necessity have different quantifiers (lines 1271--1323) | repaired |
| aggregate transfer, unguarded “only,” and physical-refutation headlines | every transfer predicate names `X_g`; “only” requires all proper candidates to validly run and fail; duty failure is scope-specific and not physical nonexistence (lines 1327--1394) | repaired |

No terminal v2 defect survives on this review axis.

## 4. Independent hostile and fresh semantic attacks

I searched for a decisive semantic counterexample rather than relying on the
author's 37 controls. The following constructions were evaluated against the
literal frozen routes.

### A1 — scheduled common-cause assignment

Let a logged schedule be `A=U`, let the later outcome be `Y=U`, and give `A` no
causal arrow to `Y`. Source inventory and perfect balance do not identify the
do-law. The v3 bytes require either assignment-source exogeneity under `ID-R`
or a complete `ID-T` bridge; otherwise the comparison is unidentified or the
assignment is invalid (lines 237--329). Scheduling cannot become intervention.

### A2 — encoded material treatment trace

Let execution projection map both branches to `COMPLIANT`, but let the
controller leave an encrypted analog tag `L=f(h)` that a licensed future can
decode. Calling `L` something other than a treatment label does not evade the
law: every controller log, pulse residue, cable state, heat load, or other
accessible trace belongs in `b` or `n`, and deleting a column is not physical
inaccessibility (lines 169--198). The mutant fails screening if the tag changes
the complete law; it cannot create a false pass.

### A3 — serial-labelled but nonfunctional B3 prop

Give a box a serial number and call it `H_T,k`, but omit a validated write,
hold, read, reset, retention, failure, and normalized response law. Material
appearance alone does not satisfy the B3 admission fields or the `D` and `I`
certificates (lines 807--841 and 417--434). The row is ineligible or
underdetermined, not a material-history pass.

### A4 — experimenter-added perfect history bank

Attach a target-independent bank that records every admitted history in the
finite task. Even if the augmented candidate later passes, lines 843--846 and
1024--1027 restrict the claim to the augmented apparatus and retain the write
channel, disturbance, and costs. The result cannot be read as evidence that
the unaugmented process already possessed that bank or that reality is
fundamentally history-valued.

### A5 — candidate-dependent access graph

Let a larger candidate license a future operation on an added register while a
smaller candidate silently forbids it, then try to call the larger candidate
necessary. Such candidates do not answer a commensurate duty: order and
necessity require the same external outcome, licensed interventions/policies,
loss, margin, power, regime, and resolution, and the carrier embedding must
preserve the smaller access grammar (lines 1273--1291). With a common augmented
apparatus and common access graph, the smaller candidate must retain the added
register as an exterior trace or declared debt. Access selection cannot prove
necessity by changing the question.

### A6 — physical cable swap disguised as basis choice

For a nonsymmetric port response, swap two physical cables while conjugating
only the reported matrix. Exact presentation requires transforming every
source, carrier, reader, record, and likelihood while leaving the serial port-
to-cable experiment fixed. A physical swap is an intervention, and a mixer is
a charged channel with loss, noise, ancillary ports, and calibration (lines
445--454 and 1045--1067). The active apparatus cannot be quotiented away.

### A7 — blind reader and permissive task

Choose a reader that cannot resolve the predeclared outside region, or choose a
screening margin without an independently justified physical loss and
resolution. The matching anchor then fails or the required two-sided power is
physically unavailable, routing the comparison to invalid or underdetermined
status (lines 509--528 and 580--597). If a genuinely narrow declared task is
insensitive to a physical difference, any pass is explicitly task-relative;
it is not a universal equality claim.

### A8 — incomparable passes plus an unknown competitor

Let `p` validly fail, let incomparable `x` and `y` pass, and leave another
proper competitor `z` unrun. The contract can print a minimal antichain only
for candidates whose applicable predecessors validly fail; it cannot call `x`
or `y` individually necessary, and `z` blocks registered necessity and every
universal exclusion (lines 1293--1323 and 1359--1371).

### A9 — reset exports the old record

Copy the memory into a reservoir/controller bit and then reset the named
memory. The local memory can reach its reference distribution while the old
record persists. V3 retains retries, old record, reservoir, resonator, heat,
latency, recovery, source carrier, access proof, and disposal route, and states
that no instrument destroys information from the universe (lines 899--913).
The mutant defeats a screening claim if licensed access remains; it does not
support an erasure theorem.

### A10 — finite success promoted to universe-wide sufficiency

Let one candidate pass every registered arm, policy, regime, reader, and
margin. The strongest local conclusion remains the named finite task result.
The supplied-structure declaration, registered-necessity scope, ladder, and
claim ceiling bar inference to a universal state, fundamental Markovianity,
indivisibility, ontology, chronology, spacetime, gravity, or unification
(lines 68--94, 1320--1323, and 1398--1421).

### A11 — laboratory ordering promoted to physical chronology

Let both sequential pivots be singular while the global three-module solve is
defined, then read the preferred algebraic bracketing as an order of physical
becoming. The contract types the result as an ordered solver-status triple on
one physical network and explicitly denies any associativity or chronology
inference (lines 1178--1200). Laboratory clocks and schedules were supplied at
the outset (lines 68--84), not derived.

### A12 — operational Hilbert/process success promoted to actuality

Let a density operator or process tensor predict every held-out record. It is
still an operational coordinate on an independently identified apparatus, not
the material carrier, a one-run selector, or a fundamental Hilbert ontology
(lines 350--386 and 796--805). Conversely, failure of that coordinate does not
select Barandes indivisibility or any rival ontology.

None of these constructions yields a reproduced semantic failure. Each either
produces a permitted failure/unknown/invalid outcome or is confined to the
explicit finite effective scope. I found no decisive counterexample that makes
the preferred answer true by definition.

## 5. Numbered foundations/ontology findings

### O3-01 — INFORMATIONAL / survives — intervention is not conditioning, scheduling, or inventory

- Affected claims: `V3-C1`, `V3-C2`, `V3-C3`, and `V3-C17`.
- Category: causal-semantic and ontological firewall.
- Exact evidence: contract lines 98--167 distinguish context, assignment,
  execution, and observation; lines 223--346 require `ID-R` or `ID-T`; lines
  1213--1233 define source closure as an inventory and expressly deny that it
  identifies a causal law.
- Finding: a command, observational conditional, known schedule, or complete
  source ledger never becomes a do-law without the separately printed physical
  identification premises. Adaptive scheduling remains a predeclared policy on
  supplied laboratory chronology.

### O3-02 — INFORMATIONAL / survives — syntax removal does not erase matter

- Affected claims: `V3-C1`, `V3-C2`, and `V3-C9`.
- Category: semantic, physical-record, and access-scope firewall.
- Exact evidence: contract lines 169--221 retain the complete archive, map only
  literal syntax to a common execution coordinate, and require every licensed-
  future-accessible material trace in `b` or `n` absent a physical
  inaccessibility certificate.
- Finding: the projection prevents treatment-label leakage from defining TV
  one while preserving logs, seed carriers, residue, heat, cable state,
  failures, and other physical traces. Inaccessibility is relative to the
  frozen access graph, never absence from the universe.

### O3-03 — INFORMATIONAL / survives — carrier, coordinate, kernel, instrument, and reader remain different types

- Affected claims: `V3-C8`, `V3-C10`, `V3-C11`, and `V3-C17`.
- Category: representation/referent and ontology firewall.
- Exact evidence: contract lines 350--386 type `Sigma_B`, `X_B`, physical
  instruments, presentation, matching, kernel, and costs separately; lines
  968--991 distinguish deterministic coherent response from the complete
  stochastic instrument law.
- Finding: predictive success of a density operator, process tensor, `S`
  matrix, finite-history vector, higher kernel, conjugacy, or lookup table does
  not instantiate a material carrier or select an ontology.

### O3-04 — INFORMATIONAL / survives — B3 is a material admission type, not an abstract history or invented apparatus

- Affected claims: `V3-C8`, `V3-C10`, `V3-C15`, and `V3-C16`.
- Category: carrier semantics and outcome eligibility.
- Exact evidence: temporal contract lines 807--841 and regional lines
  993--1022 require physical substrate, serials, topology, preparation,
  write/hold/read/reset, retention/failure, access, costs, and a normalized
  kernel; uninstantiated rows are barred from scoring, order, minimality, and
  necessity.
- Finding: v3 repairs the decisive v2 B3 collapse. Coordinate-only history and
  higher-response models remain legitimate controls on an existing carrier but
  earn no material enlargement. A symbolic admission type supplies no device.

### O3-05 — INFORMATIONAL / survives — added memory is not preexisting ontology

- Affected claims: `V3-C9`, `V3-C10`, `V3-C15`, and `V3-C18`.
- Category: experimental-intervention and ontology firewall.
- Exact evidence: contract lines 843--846 and 1024--1027 say that actively
  adding or writing a memory changes the experiment, retains its disturbance
  and costs, and cannot establish that the unaugmented process contained it.
- Finding: a B3 pass could establish only sufficiency of the frozen augmented
  apparatus. It cannot prove a history ontology, hidden preexisting record
  bank, fundamental discreteness, or universal Markov enlargement.

### O3-06 — INFORMATIONAL / survives — subsystem and port decompositions are supplied effective structure

- Affected claims: `V3-C7`, `V3-C8`, `V3-C11`, and `V3-C18`.
- Category: effective/fundamental and decomposition firewall.
- Exact evidence: contract lines 68--94 declare clocks, apparatus,
  system/port decomposition, comparators, regimes, candidates, order, and access
  graph to be supplied with no fundamental ontological status; lines 782--805
  and 939--991 type the bounded transmon and microwave apparatuses.
- Finding: passing cannot derive a tensor factorization, fundamental entity,
  field carrier, spatial boundary, time, or locality. The apparatus split is an
  input to a fixed-background laboratory discriminator.

### O3-07 — INFORMATIONAL / survives — passive presentation is not active transformation

- Affected claims: `V3-C4`, `V3-C8`, `V3-C11`, and `V3-C17`.
- Category: presentation/action and physical-resource firewall.
- Exact evidence: contract lines 443--454 require exact pushforward of every
  description while preserving the serial-labelled experiment; lines
  1045--1067 classify cable permutations and adapters as physical instruments
  with complete loss/noise/resource laws.
- Finding: names, bases, and reference coordinates may change passively only
  together. Rewiring, mixing, transplantation, reset, pulses, and randomization
  remain active apparatus. Software conjugacy never becomes a physical adapter.

### O3-08 — INFORMATIONAL / survives — registered completeness is not microscopic omniscience

- Affected claims: `V3-C1`, `V3-C2`, `V3-C11`, `V3-C12`, and `V3-C17`.
- Category: scope-binding and epistemic completeness.
- Exact evidence: contract lines 86--90 define completeness on one frozen
  attempted-run schema and deny microscopic omniscience; lines 200--221 require
  one sentinel-completed normalized parent; lines 1213--1233 retain residual
  environment and inaccessible debt.
- Finding: every issued attempt and declared failure route remains in the
  operational law. Unmeasured microscopic facts are neither claimed known nor
  silently declared absent. The scope is complete enough to prevent
  postselection, not complete enough to support an ontology theorem.

### O3-09 — INFORMATIONAL / survives — physical order, minimal antichain, registered necessity, and fundamental necessity remain distinct

- Affected claims: `V3-C15` and `V3-C16`.
- Category: order theory, quantifier semantics, and ontology firewall.
- Exact evidence: contract lines 1271--1323 require a carrier embedding,
  grammar preservation, monotone cost, and commensurate duties; unknown
  predecessors block minimality; incomparable minima form an antichain;
  registered necessity requires a passing proper candidate and failed proper
  competitors without the augmentation.
- Finding: the rules establish, at most, minimality or necessity inside the
  frozen apparatus, roster, policies, regime, margin, power, and resolution.
  They cannot establish individual or fundamental necessity.

### O3-10 — INFORMATIONAL / survives — finite success is not universal sufficiency

- Affected claims: `V3-C5`, `V3-C14`, `V3-C15`, `V3-C16`, and `V3-C18`.
- Category: quantifier and effective/fundamental firewall.
- Exact evidence: contract lines 29--42 and 68--90 bind finite experiments and
  candidate families; lines 1327--1371 parameterize every headline and block
  universal exclusions on unknown candidates; lines 1414--1421 bar universal
  promotion.
- Finding: a pass speaks only about the registered carrier, duties, histories/
  interiors, futures/exteriors, regimes, readers, loss, margin, resolution, and
  access graph. It is not a theorem about every process, scale, or the universe.

### O3-11 — INFORMATIONAL / survives — reset, randomization, disposal, and marginalization do not destroy information

- Affected claims: `V3-C1`, `V3-C9`, `V3-C17`, and `V3-C18`.
- Category: information and thermodynamic-resource firewall.
- Exact evidence: contract lines 899--913 retain randomizer source/seed,
  access proof, disposal/destination, reset retries, old records, reservoirs,
  heat, latency, recovery, and isolation residuals and explicitly deny universal
  information destruction; lines 1250--1267 charge those resources.
- Finding: operational unavailability is relative to a licensed access graph.
  Statistical integration over `z` changes a predictive law, not the physical
  universe. No erasure, reversibility, or actuality theorem is inferred.

### O3-12 — INFORMATIONAL / survives — schedule and bracketing do not derive chronology

- Affected claims: `V3-C3`, `V3-C13`, `V3-C14`, and `V3-C18`.
- Category: syntax/physics and chronology firewall.
- Exact evidence: contract lines 68--84 supply clocks and schedules; lines
  139--145 type adaptive futures as predeclared policies; lines 1178--1200 type
  global and sequential solves and deny a chronology result.
- Finding: “past,” “future,” interval, and reconnection order are registered
  laboratory roles. Algebraic parenthesization is a conformance calculation on
  one network. Neither yields an emergent physical time or global causal order.

### O3-13 — INFORMATIONAL / survives — Barandes, Hilbert, actuality, spacetime, gravity, and unification ceilings are complete

- Affected claims: `V3-C8`, `V3-C10`, `V3-C11`, and `V3-C18`.
- Category: ontology, actuality, spacetime, gravity, and unification firewall.
- Exact evidence: contract lines 44--64 forbid state/process/response promotion;
  lines 1398--1421 cap the ladder; lines 1485--1528 submit no existence theorem
  and explicitly deny every listed downstream promotion. The governing premise
  lines 19--23 and 75--91 separates mathematical Markovization from a physical
  memory, while the synthesis lines 398--479 leaves ontology, actuality,
  chronology, spacetime, and gravity open.
- Finding: neither a compact pass nor a history/target-built result selects
  Barandes indivisibility, Hilbert ontology, an actual trajectory, a field or
  subsystem ontology, spacetime, a gravitational source/coupling law, or a
  unified theory. Failure of one representation selects no rival.

### O3-14 — INFORMATIONAL / survives — the result vocabulary is neutral and noncircular

- Affected claims: `V3-C4`, `V3-C5`, `V3-C6`, `V3-C7`, `V3-C14`, `V3-C15`,
  and `V3-C16`.
- Category: semantic routing and result-neutrality.
- Exact evidence: contract lines 599--639 separate pass, fail, unknown, and
  invalid; lines 762--776 require direct target-blind composition; lines
  1327--1394 parameterize local and headline outcomes.
- Finding: compact pass, enlarged pass, antichain, duty-specific failure,
  direct-triple failure, transfer failure, no registered proper pass,
  target-built-only performance, ineligibility, invalidity, and
  underdetermination are all reachable without rewriting the law. The preferred
  answer is not encoded in the candidate name, threshold, reader, or roster.

No blocking, major, moderate, minor, or scope-narrowing Seat O finding remains.

## 6. Claim-level Seat O audit

| frozen claim | Seat O result | controlling reason |
|---|---|---|
| `V3-C1` | survives | typed context/assignment/execution/observation and syntax/trace firewall; O3-01--O3-02 |
| `V3-C2` | survives | one sentinel-completed ITT schema without postselection; O3-01, O3-08 |
| `V3-C3` | survives | explicit `ID-R`/`ID-T`; inventory and scheduling give no shortcut; O3-01 |
| `V3-C4` | survives | exact passive presentation, statistical matching, and screening are distinct; O3-07, O3-14 |
| `V3-C5` | survives at its printed task-relative scope | strict nonvacuity, independent physical justification, and two-sided power prevent a defined pass; Section 2 and A7 |
| `V3-C6` | survives on this axis | ignorance and invalidity are not converted into pass/fail or ontology; O3-08, O3-14 |
| `V3-C7` | survives | each duty and transfer coordinate retains its subject and regime; O3-14 |
| `V3-C8` | survives | material carrier, coordinate, kernel, instrument, and reader remain different types; O3-03 |
| `V3-C9` | survives as a contract duty | backaction, records, destinations, residuals, and failures remain visible; O3-02, O3-11 |
| `V3-C10` | survives | B3 requires material grammar and predata eligibility; coordinate controls earn no enlargement; O3-04--O3-05 |
| `V3-C11` | survives | coherent response is nested and cannot fill the stochastic attempt law; O3-03, O3-07 |
| `V3-C12` | survives on this axis | explicit preparation and failures preserve the physical complete-attempt referent; O3-08 |
| `V3-C13` | survives on this axis | statuses do not become ontology or chronology claims; O3-12 |
| `V3-C14` | survives | direct pair/triple targets remain empirical tests and never training payload; O3-10, O3-14 |
| `V3-C15` | survives | physical embeddings, antichains, and registered necessity have distinct scopes; O3-09 |
| `V3-C16` | survives | every headline is parameterized and ignorance blocks exclusion; O3-09--O3-10 |
| `V3-C17` | survives | source, preparation, resources, access, and debt remain physical; simulation supplies no apparatus; O3-01, O3-07--O3-11 |
| `V3-C18` | survives | ladder and stopping wall award no ontology or downstream foundational result; O3-05--O3-13 |

All submitted claims survive on the Seat O axis as printed. No narrower scope
needs to be invented: effective apparatus scope, finite registered quantifiers,
task/loss/margin/resolution dependence, licensed-access relativity, and the
absence of any ontology or downstream promotion are already literal frozen
conditions.

## 7. Recommendation, award ceiling, and no-claim statement

Recommended disposition: **`SPB-D4 — ACCEPT`**.

Authentication passes. The central test is an empirical, causally typed,
nonvacuous discriminator rather than a definition of a preferred answer. I
found no foundations, ontology, carrier, source-scope, quantifier, information,
chronology, gravity, or result-vocabulary defect in the frozen law, and no
unprinted narrowing is required.

This recommendation can support only `SPB-L0`, conditional on root
authentication and adjudication. It authorizes no apparatus work and awards no
physical boundary result. It does not establish a sufficient boundary in
nature, a necessary carrier, a fundamental Markov state, indivisibility,
Barandes or Hilbert ontology, a unique actuality, chronology, spacetime,
gravity, or unification.

Signed: Seat O, independent foundations/ontology/gravity-firewall reviewer

Report LF line count: `000538`

Report byte count: `033134`

Report normalized self-SHA-256:
`17b6caac6d6696057d06a894e1bd338fe5f234c91a8018f622480449cca7bdef`

Normalization rule: replace the six decimal digits on both report count lines
and the 64 hexadecimal characters on the normalized-self line by ASCII zeroes,
preserve every other byte, and compute SHA-256. The file uses LF, ends in one
LF, and contains no trailing horizontal whitespace.
