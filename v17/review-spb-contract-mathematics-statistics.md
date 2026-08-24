# SPB contract review — Seat M (mathematics/statistics)

Date: 2026-08-24

Seat: M — mutually blind mathematics/statistics review

Frozen pin: `v17/note-spb-sufficient-physical-boundary-contract-review-pin.md`

## 1. Independence, chronology, and authentication

I performed this review independently. I did not inspect, request, receive, or
communicate with any sibling reviewer or sibling report. I made no repository
edit. The only review output is this report.

### 1.1 Commit and pin authentication

- Repository `HEAD` and the abbreviated pin name `014c820` both resolve to
  `014c82008f736ea8837be6af548cd308f317f3af`.
- Its sole parent is
  `b1ff02806aade184298534f1d285f82b8c32ab89`, exactly the scientific-package
  commit declared by pin §1.
- The pin has 489 LF-terminated lines and 22,169 bytes. Its raw SHA-256 is
  `b5491cd698af90f6603f1597a8724f9614d0d255fef5b0da0c9b54686ac6c75d`.
- I replaced the two six-digit pin counts and the 64 hexadecimal pin self-hash
  by zeroes exactly as its terminal rule directs. The result hashes to
  `1ac5bc365a13e2158386ab6e2a1847cf94cdaa750e79e130ea83b5de2bc5391d`,
  exactly the printed normalized self-SHA-256.
- The pin ends in one LF and has no line with trailing horizontal whitespace.
- The unrelated untracked `v16/note-handoff-prompt-2026-08-22.md` was present
  and was not consumed.

Chronology and pin authentication therefore pass.

### 1.2 Section 2 repository objects

I authenticated every Section 2 object relevant to Seat M against both the
working bytes and the blob at the pin commit. The working copies and committed
blobs were byte-identical.

| object | LF lines | bytes | SHA-256 |
|---|---:|---:|---|
| `v17/note-foundational-assumption-deletion-programme.md` | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` |
| `v17/research-incubator/active/assumptions/v17_assumption_parallel_synthesis_and_next_gates.md` | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` |
| `v17/research-incubator/active/spb/v17_spb_primary_source_receipt_manifest.md` | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` |
| `v17/research-incubator/active/spb/v17_spb_p0_physical_platform_and_source_audit.md` | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` |
| `v17/research-incubator/active/spb/v17_spb_result_neutral_gate_contract.md` | 727 | 28901 | `7212e363cea918e82343eaa0dfe930aa27210c1fbbda4eae3115ccd98174b4d8` |
| `v17/research-incubator/active/spb/v17_spb_root_pre_pin_readiness_and_mutant_audit.md` | 418 | 19438 | `fdb1808a007dce02c4f606889c5632f1d6369542056c3f7664a2f8d63341cd68` |
| `v17/research-incubator/active/spb/README.md` | 77 | 3500 | `04b985f737ca4179c132be03daa1ff169827ff041e407c4921b2dbe532fe933b` |

### 1.3 Primary objects and author repositories

Before inspecting source content, I independently rehashed all six local
primary PDFs named by pin §3. All matched the pinned received-byte identities.

| ID | exact local object | bytes | SHA-256 |
|---|---|---:|---|
| S1 | `/private/tmp/spb_t_pollock.pdf` | 896695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` |
| S2 | `/private/tmp/spb_t_giarmatzi_v3.pdf` | 6601486 | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` |
| S3 | `/private/tmp/spb_t_xiang_v2.pdf` | 1276514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` |
| S4 | `/private/tmp/spb_r_isoscattering.pdf` | 1835223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` |
| S5 | `/private/tmp/spb_r_star_product.pdf` | 307827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` |
| S6 | `/private/tmp/spb_r_isoscattering_equal_oneport.pdf` | 3291194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` |

The local `NMN-tomo` repository resolves to
`154235f8bbf5e70eb71c325370a67b1894490452`; its selected files reproduce the
pinned byte/hash pairs: `README.md` 904 /
`fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593`,
`All codes.ipynb` 1399666 /
`b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1`,
`NMN_lab_rslts.json` 20177 /
`b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43`, and
`NMN_tomog_rerun.json` 176825 /
`450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657`.
The local `qucse` repository resolves to
`81998e861ae43541d03738c15d7c60715be37309`. Both repositories were clean.

I inspected S1, S4, and S5 where their exact mathematical claims were needed.
No later source or substituted version was used.

## 2. Independent reconstruction

### 2.1 Complete attempts and the causal estimand

The frozen attempted-run tuple is

`omega = (j,p,c,b,f,r,n,q)`.

For a screening comparison, the design/assignment variables and the scored
outcome variables must live in different types. In particular, a coherent
reconstruction has the form

`A = (j,h,i,f, assigned commands/seeds)`

and a common measurable outcome

`Y = (boundary outcomes, future reader record, nuisance/environment record,
quality/failure state)`.

The causal quantity is then the law of `Y` under the implemented assignments,
not the observational conditional obtained by selecting rows after the fact.
The governing synthesis prints this distinction explicitly as
`P(F_+ | do c_+, x)` at lines 187–200 and gives the fair-common-cause
counterexample at lines 323–334. S1 likewise makes a causal break a physical
measurement followed by independently randomized re-preparation (PDF p. 2),
not a passive conditional.

At registered scope, the intended population statement is therefore:

`for each candidate fixed before held-out opening, for every predeclared
nontrivial (h,h') certified close at the boundary, every implemented i, and
every held-out f, d(Q^{do}_{h,i,f}, Q^{do}_{h',i,f}) <= epsilon_{h,h',i,f}`.

The candidate, presentation quotient, comparison family, assignment mechanism,
margin, record projection, and nuisance standardization all precede the
held-out records in that quantifier order.

### 2.2 One-sided equivalence

For a nonnegative distance `d` and a scientific margin `epsilon`, a
simultaneous upper confidence bound `U <= epsilon` is a valid positive
equivalence rule. It is not a failure-to-reject rule. A complete three-way
decision also distinguishes evidence that `d > epsilon` from an interval that
straddles `epsilon`; low power belongs to the indeterminate branch. The family
for simultaneous coverage includes the candidate lattice, boundary-matching
validation, all pairs/instruments/policies, composition targets, frequency
bins, and both bracketings selected for a common claim.

Total variation is mathematically suitable on a common finite outcome space.
Its empirical plug-in is finite-sample biased, and its sample complexity can be
large in a complete transcript alphabet; the frozen text correctly delegates
bias, coverage, missing-attempt treatment, drift, and power to an exact
evaluation pin. Continuous timestamps, phases, temperatures, and nuisance
records need the same frozen measurable treatment as waveforms if they remain
in the primary TV outcome.

### 2.3 Temporal composition and the pairwise/triple mutant

Typed quantum instruments, augmented with their classical outcomes and failure
states, can compose to a normalized joint record law. Independently fitted
segment maps cannot be allocated one per held-out control word without turning
the construction into a response table. The pin's C8, contract lines 322–337
and 624–626, and author audit lines 197–208 collectively block that leakage.

The pairwise-good/triple-bad attack is exact. Let `P_iid` be three independent
fair bits and `P_even` the uniform law on the four even-parity triples. Their
three pairwise marginals are identical, while

`TV(P_iid,P_even) = 1/2`.

Thus adjacent/paired maps cannot establish three-time composition. The direct
`ABC` run and the registered triple mutant catch this counterexample.

### 2.4 Regional seam equations

Combine all module exterior and seam ports and write

`b_e = S_ee a_e + S_es a_s`,

`b_s = S_se a_e + S_ss a_s`,

with connector convention `a_s = V b_s`. Then

`K a_s = V S_se a_e`, where `K = I - V S_ss`,

and, when `K` is invertible,

`S_eff = S_ee + S_es K^{-1} V S_se`.

For all exterior inputs, existence requires
`Range(V S_se) subseteq Range(K)`. Internal seam amplitudes are unique exactly
when `Ker(K) = {0}`. Even if the seam solution is nonunique, the exterior
relation is unique when the ambiguity is annihilated by `S_es`, i.e.
`S_es Ker(K) = {0}`. These are distinct singular cases.

For three modules, both bracketings are Schur-elimination orders of one global
seam system. If all relevant pivots exist, they agree algebraically. A global
system can be invertible while a particular intermediate pivot is singular, so
the phrase “where defined” is necessary. Calibration uncertainty is amplified
through

`delta(K^{-1}) = -K^{-1} (delta K) K^{-1}`,

and near-singular bins require joint, non-linear propagation rather than an
unqualified entrywise error bar.

### 2.5 Printed transplantation matrix

S4 PDF p. 3, eqs. (2)–(4), gives for `n=2`

```text
T4 = [[1,-1, 0, 0],
      [1, 0,-1, 0],
      [0, 1, 0,-1],
      [0, 0, 1, 1]].
```

Direct multiplication gives

```text
T4^dagger T4 = [[ 2,-1,-1, 0],
                 [-1, 2, 0,-1],
                 [-1, 0, 2, 1],
                 [ 0,-1, 1, 2]],
det(T4) = 2.
```

If `lambda T4` were unitary, then
`|lambda|^2 T4^dagger T4 = I`; the nonzero off-diagonal entries make this
impossible. C9's nonunitarity-up-to-scalar statement is correct.

## 3. Numbered findings

### M-1 — The screening law has no frozen common outcome projection or explicit intervention arrow

- Severity: **BLOCKING**
- Category: **mathematical; statistical; semantic**
- Affected claims: **C2, C4, C5, C7**
- Exact evidence: contract lines 66–92 define `Omega` using fields that include
  the differing history/interior preparation `p`, all commands/seeds `c`, and
  policy `f`; lines 130–156 introduce a new, undefined `omega_F` and then call
  TV on the “complete finite transcript” primary. The synthesis lines 187–200
  prints a `do`-law, whereas the binding contract only writes `P_{h,i,f}`.
  Contract lines 253–255 refer to destructive validation copies but never
  define which boundary outcomes, pre-cut records, nuisance coordinates, and
  quality states survive in `omega_F`.
- Decisive attack: if “complete transcript” means the full `Omega`, take
  distinct registered histories `h != h'` and the event `A = {p=h}`. Then
  `P_{h,i,f}(A)=1` and `P_{h',i,f}(A)=0`, so TV is exactly one independently of
  all future behavior. Every nontrivial same-boundary pair fails by typing. If
  `omega_F` instead means a projection, its map and sigma-algebra are not
  frozen. Omitting boundary outcome `b` gives the opposite error: histories
  with different instrument-outcome laws but identical post-boundary reader
  laws falsely screen.
- Causal attack: the fair-common-cause example frozen in the synthesis has
  `P(Y=y|X=x)=delta_{yx}` but `P(Y=y|do(X=x))=1/2`. Merely recording controller
  commands and seeds does not mathematically identify the first law with the
  second; assignment, noncompliance, drift standardization, and postselection
  must be part of the estimand.
- Consequence: the current bytes admit both a trivially impossible reading and
  an incompletely normalized reading of SPB-S. This is more than a notation
  preference because the two readings produce opposite decisions on explicit
  mutants.

### M-2 — The positive equivalence rule is sound, but negative versus indeterminate classification is not a decision rule

- Severity: **BLOCKING**
- Category: **statistical; semantic**
- Affected claims: **C5, C11**
- Exact evidence: contract lines 138–159 print only the positive condition
  `U <= epsilon`; temporal lines 304–320 repeatedly route “if no” toward larger
  candidates or no-boundary outcomes; regional outcomes at lines 510–523
  distinguish failure from underdetermination; lines 580–597 delegate coverage,
  bias, missingness, and power but print no negative threshold. Author audit
  lines 71–73 and 338–359 correctly name indeterminacy and wide-margin theater,
  but do not bind a mathematical routing rule into the contract.
- Decisive attack: let a simultaneous interval for a distance be
  `[L,U]=[0.02,0.20]` with `epsilon=0.10`. The positive criterion does not pass,
  but the data also do not establish non-equivalence. Routing every nonpass to
  T7/R8 forces a negative; routing it to pass would be failure-to-reject
  promotion. The frozen outcomes contain T8/R9, but no printed rule sends this
  interval there.
- Margin attack: line 147 derives `epsilon` from preparation, reader, and drift
  validation budgets, while the upper bound is also required to propagate
  those uncertainties. A poor reader can therefore enlarge both uncertainty
  and the allowed effect. The author audit's downstream-relevance warning is
  scientifically right, but the binding equation does not separate a maximum
  scientifically negligible effect from uncertainty in estimating that effect.
- Multiplicity attack: “all registered screening pairs” does not explicitly
  include selection of same-boundary pairs on validation data, sequential
  choice across T-B0…T-B3, composition targets, frequency bins, and bracketing
  comparisons in one claimed family. Without that quantifier, nominal
  simultaneous coverage can be lost before SPB-S is evaluated.
- Consequence: the package specifies a valid sufficient condition for a
  positive result, but it is not yet a statistically decidable three-way
  contract and can force a negative classification under low power.

### M-3 — The regional star-product predictor has the wrong codomain for the required complete-attempt law

- Severity: **BLOCKING**
- Category: **mathematical; statistical; semantic**
- Affected claims: **C4, C8, C10, C11**
- Exact evidence: common composition at contract lines 163–185 requires a
  normalized predicted probability `P_hat_ABC` on the complete attempt space.
  The regional candidate at lines 378–398 is only the complex multiport
  relation `S_B(nu)`. Regional composition at lines 448–466 solves for an
  exterior input–output relation and says the module matrices and connector
  calibration are the only prediction inputs. Yet the attempted-run law also
  contains reader randomness, nuisance/environment records, aborts, dropped
  attempts, invalid states, and hardware failures (lines 66–92), and Section 8
  requires a joint nuisance parent.
- Decisive counterexample: two linear, time-stationary, single-mode modules can
  have the same coherent matrix `S=0` while obeying `b=Sa+eta` with different
  noise-wave laws, for example `eta=0` in one and `eta=+sigma/-sigma` with equal
  probabilities in the other. They have identical `S`, and their star-product
  coherent predictions are identical, but their complete reader laws have
  positive TV distance. The same construction uses identical `S` and different
  registered timeout probabilities in `q`. Neither distribution follows from
  `S_A,S_B,S_C,V`.
- The architecture's symbol `N` does not close the typing issue as printed. If
  interior-emitted noise, failure kernels, or their seam correlations enter the
  predictor through `N`, the matrices and connector are not the only prediction
  inputs. If they do not enter, no normalized `P_hat_ABC` exists for the scored
  transcript. Treating all such differences as nuisance also risks removing a
  real interface channel from the boundary question.
- Consequence: direct S-matrix gluing can validly predict coherent mean
  response, but the frozen contract demands a stronger probability-valued
  composition. The two types are not connected by the current bytes.

### M-4 — “Singular seam” does not determine existence or uniqueness of the exterior response

- Severity: **MAJOR**
- Category: **mathematical**
- Affected claim: **C10**
- Exact evidence: contract lines 448–462 define the composite by a unique
  exterior relation but classify frequencies where the seam system is singular
  or nonunique as anomaly outputs without an exterior-uniqueness test. The
  final checklist at lines 685–700 delegates the actual seam equations and
  singular policy. S5 PDF pp. 14–20, especially Theorem 4.1, proves composition
  for all positive energies in its unitary graph domain, including the set
  where the internal matching kernel is nontrivial; the generalized product
  uses the noncompatible case rather than simply dropping it.
- Decisive counterexample: set `K=0`, `S_se=0`, and `S_es=0`. The internal seam
  amplitude is arbitrary, but `b_e=S_ee a_e` is unique. This is the algebraic
  trapped-mode case: singular/nonunique internally, determinate externally.
  Conversely, a singular `K` can make the inhomogeneous equation inconsistent,
  and a merely near-singular invertible `K` can make uncertainty unbounded for
  practical purposes. These cases need different mathematical outcomes.
- Bracketing consequence: a singular intermediate Schur pivot can make one
  sequential bracketing undefined even when the global three-module seam
  matrix is invertible. The contract's “where defined” clause is correct, but
  no printed rule says whether the global solve, the singular tag, or the
  sequential calculation controls the scored prediction.
- Consequence: registering rather than deleting difficult bins is correct, but
  “singular” alone is not a sufficient decision predicate for C10.

### M-5 — Exact presentation equivalence and empirical boundary closeness are conflated

- Severity: **MAJOR**
- Category: **mathematical; statistical; semantic**
- Affected claims: **C5, C6, C9**
- Exact evidence: contract lines 96–108 call `sim_B` a predeclared
  presentation/equivalence relation; lines 130–150 quantify only over pairs
  satisfying it; lines 253–255 say equivalence is empirically certified on
  validation copies. Regional lines 389–392 use a true presentation quotient
  for label/phase conventions, while lines 400–432 separately ask approximate
  physical response equality. Author audit lines 183–195 adds a nontrivial
  separation certificate, but no joint matching-and-screening coverage rule is
  printed.
- Mathematical attack: threshold closeness is generally not an equivalence
  relation. Boundary values `0`, `0.75 delta`, and `1.5 delta` make the first
  close to the second and the second close to the third while the first is not
  close to the third. Treating this as a quotient changes which pairs are
  universally quantified. Treating `sim_B` as exact identity instead can make
  generic §4 vacuous unless the mandatory history-different pairs are actually
  certified.
- Nonvacuity result: the temporal pair types at lines 233–255, the regional
  changed-interior requirement at lines 486–488, and the author audit's
  duplicate-label mutant do block the simplest same-program vacuity if enforced.
  What remains unresolved is whether `sim_B` is an exact presentation quotient
  or a statistical closeness event, and how uncertainty/selection in the latter
  is propagated into the simultaneous SPB-S claim.
- Consequence: the broad nonvacuity design survives, but the boundary relation
  and quantifier order are not yet sufficiently typed for a frozen statistical
  decision.

## 4. Attacks that survived

1. **Predictive-object leakage (C1): survives.** Full process tensors, complete
   histories, target quotients, and scattering similarities are consistently
   denied physical-descent credit.
2. **Five duties and arm separation (C2–C3): survives semantically.** The five
   coordinates are separately reported and temporal/regional scores cannot be
   averaged. M-1 affects their mathematical implementation, not this separation.
3. **Attempt completeness principle (C4): survives in intent.** Failure,
   leakage, old-record, missing, and nuisance branches are explicitly retained;
   successful postselection is not the principal law. M-1 and M-3 prevent the
   intent from becoming a common scored law as printed.
4. **Temporal lattice and grammar (C6–C7): survives the named mutants.** The
   candidates are frozen, enlargement after residual opening is forbidden, and
   read/reset/randomize/isolate operations retain outcomes, backaction, seeds,
   disposal carriers, and failures.
5. **Temporal no-refit composition (C8): survives.** Direct ABC records are
   held out, both bracketings are computed from the same maps, a seam
   intervention is required, per-program tables are charged, and the parity
   mutant is detected.
6. **Fixed-interface regional equality and T4 (C9): survives.** Similarity,
   trace, spectrum, and determinant are not literal fixed-port equality. The
   exact printed T4 cannot be made unitary by scalar normalization.
7. **Direct triple comparison (part of C10): survives.** Both algebraic
   bracketings must predict one directly assembled network, and the hostile
   pairwise-good/triple-bad mutant is registered. M-3 and M-4 still block the
   complete-law and singular-case portions.
8. **Resource visibility and result neutrality (C11): substantially survives.**
   Calibration, precision, memory, reset, adapters, discarded records, and
   target-sized tables are charged; larger, no-boundary, and underdetermined
   outcomes remain named. M-2 prevents exhaustive statistical routing.
9. **Ceiling (C12): survives.** No contract or future bounded result is promoted
   to universal state, Markovianity, ontology, chronology, spacetime, gravity,
   or unification.

## 5. Claim-level result

| claim | Seat M result |
|---|---|
| C1 | survives |
| C2 | conceptual separation survives; formal scoring affected by M-1 |
| C3 | survives |
| C4 | blocked by M-1 and M-3 |
| C5 | blocked by M-1, M-2, and M-5 |
| C6 | candidate lattice/nonvacuity design survives; matching type affected by M-5 |
| C7 | physical grammar survives; causal estimand affected by M-1 |
| C8 | survives the parity and target-table attacks |
| C9 | survives, including the exact T4 calculation |
| C10 | blocked by M-3; singular policy affected by M-4 |
| C11 | resource/outcome visibility survives; decision exhaustiveness affected by M-2 |
| C12 | survives |

## 6. Disposition and award

**Recommended disposition: SPB-D2 — REVISE BEFORE PHYSICAL PIN.**

The central SPB question is nonvacuous, the physical interventions and direct
triple comparisons test real distinctions, the source ceilings are honest, and
the main adversarial representations are blocked. Authentication also passed.
However, the current contract cannot govern acquisition or adjudication while
its complete-record screening law has two incompatible sample-space readings,
its statistical outcomes lack a frozen negative/indeterminate rule, and its
regional composition produces a matrix where the common contract requires a
normalized complete-attempt probability law. These are semantic/mathematical
contract defects, not empirical results.

Scientific boundary result: none.

Award: none; `SPB-L0` is not earned by this review.

LF line count: `000443`

Byte count: `023617`

Normalized self-SHA-256:
`447d4c60ef8c036070c261b877c6bb8246c5ef217d5a28b25a723a46b7d510fa`

The normalization rule replaces decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
