# D13 hostile review, round 2: independent rebuild and corpus closure

**Referee:** independent clean-room reproducibility/corpus audit  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE NARROWED FINITE-KERNEL THEOREM AND DECLARED `INCOMPLETE-INVESTIGATION` STATUS**

The round-1 blocking defects are repaired.  The authoritative D13 exact
witness now runs under the default Python with no external dependency, passes
21 exact checks, gates its count and semantic hash, prints its source hash,
and produces byte-identical normal/optimized output.  The corpus inventory now
excludes D13 artifacts, freezes the V1--V10-D12 antecedent boundary at 524
Markdown files, retains untruncated headings/scope guards, and fails on count
or corpus-hash drift.  Its normal and optimized outputs are also identical.

Paper 14 and the repaired notes correctly narrow the result.  They no longer
claim equal positive support, a universal diamond category, general Lorentz/
diffeomorphism covariance, a derived record instrument, or D13 priority for
the iSWAP family.  The human ledger now adjudicates V7 Papers 47--51, the
literature note cites the direct process-tensor reconstruction paper and
primary Lovelock/Jaynes sources, and the candidate-class note retains live
asymptotic-safety, causal-set-phase, and empirical-selector openings.

No overlooked earlier action selector defeats the conclusion.  A further
search found one major-looking item worth adding explicitly to the human
ledger—V4 Paper 39's standalone Yang--Mills construction—but its own status
is a conditional reduction with the fixed-scale infrared bridge and the 4D
construction/mass gap still open.  It therefore reinforces, rather than
changes, D13's architecture-versus-physical-input boundary.

Three nonblocking hardenings remain: the visible-memory "circuit" check stores
the circuit's two history atoms rather than executing reversible copy gates;
the repeat-read check duplicates the persistence marginal equality; and the
old SymPy predecessor remains in `v10/code` without an in-file replacement
banner.  These should be cleaned before a final archive, but none affects the
proved two-kernel nonselection theorem or the honest provisional verdict.

## 1. Authoritative exact receipt

### 1.1 Source and generated packet

Direct filesystem hashes are:

```text
b11f8ffce91d803d991afe294be95e156a79461094edb833c8cf723743d8cb39  v10/code/d13_finite_kernel_no_go_exact.py
e03cea4a1940a3a274e7dc5499b39c4932a8e334ff09945265480836f7dc3fe4  v10/data/d13-finite-kernel-no-go-exact.json
```

The generated JSON contains the same source hash and the frozen semantic
receipt:

```text
checks_passed=21
semantic_sha256=4eb19b0eb34bdc9cd910029cb3d4c22bb47d8d847e0fe12353a7b5eac69f2852
source_sha256=b11f8ffce91d803d991afe294be95e156a79461094edb833c8cf723743d8cb39
verdict=FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
```

### 1.2 Default-Python reproduction

With `PYTHONDONTWRITEBYTECODE=1`, both

```text
python3 v10/code/d13_finite_kernel_no_go_exact.py
python3 -O v10/code/d13_finite_kernel_no_go_exact.py
```

complete successfully.  Their full stdout hashes are identical:

```text
587f768d8f5b7c59b3858c4275b17273a41c7fbd9a28e80dd6c5e14add369fca
```

Both end with:

```text
CHECKS PASSED: 21/21
SEMANTIC SHA256: 4eb19b0eb34bdc9cd910029cb3d4c22bb47d8d847e0fe12353a7b5eac69f2852
SOURCE SHA256: b11f8ffce91d803d991afe294be95e156a79461094edb833c8cf723743d8cb39
VERDICT: FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
```

The implementation uses only `dataclasses`, `fractions`, `hashlib`, `json`,
and `pathlib`.  All theorem-critical arithmetic is exact in
`Q(sqrt(2),i)`.

### 1.3 Check-count and semantic gates

The source fixes:

```text
EXPECTED_CHECKS=21
EXPECTED_SEMANTIC_SHA256=4eb19b0e...
```

and raises if either differs.  The final check is itself counted, after which
the exact count is compared again.  Unlike the old SymPy witness, the new file
is independently reproducible in the declared workspace runtime.

## 2. Independent mathematical reconstruction

The finite no-go remains sound.  On the fixed operational interval,

```math
U_\theta=e^{i\theta X_{ex}},
\qquad X_{ex}=|01\rangle\langle10|+|10\rangle\langle01|.
```

The two chosen members are exact matrices in `Q(sqrt(2),i)`.  Independently:

- `U_(pi/4)` and `U_(pi/2)` are unitary;
- the generator commutes with excitation number and leg exchange;
- `U_(pi/4)^2=U_(pi/2)`, so the displayed shared-screen composition is exact;
- disjoint tensor-factor operations commute;
- an overlapping first-leg `Z` operation does not commute with the quarter
  interaction;
- input/output unitary basis changes cancel in the tested instrument
  probability;
- the seal map `|j> -> |j>_S |j>_R |live>` is an isometry and gives
  orthogonal record labels;
- both members have a normalized maximal-entanglement witness; and
- for preparation `|10>` and effect `|10><10|`, the two probabilities are
  exactly `1/2` and `0`.

The two kernels are therefore physically inequivalent under the stated
instrument-probability equivalence.  The shared finite premises cannot select
the interaction angle, hence cannot select the corresponding fixed-interval
coupling.

The added cells are correctly scoped as examples, not universal theorems:

- `H H` versus an inserted dephasing record distinguishes coherent amplitude
  addition from probability addition;
- a local Hadamard on one half of a Bell state preserves the other reduced
  state in one exact no-signalling cell;
- projective Kraus operators implement an exact normalized dephasing limit;
- a sealed record marginal is invariant under the declared later
  system-only unitary algebra; and
- one visible history law has the same current `Y=0` but different next `Z`
  conditionals depending on the earlier `X`.

These checks do not prove arbitrary QFT sewing, general no-signalling,
nonunitary Lorentz transport, or a universal record ontology.  Paper 14 and
the theorem note now explicitly say so.

## 3. Corpus inventory reproduction and stability

### 3.1 Frozen source and output

Direct hashes are:

```text
06226a2bd93a3314fe74aaefe1d2a26b2869197dad77f2fa4c1177673e9e753d  v10/code/d13_corpus_action_inventory.py
31e0ddbf3d32f066ec657327c0b0824352cf80b2f92953ae176bd0ec87429ab9  v10/data/d13-corpus-action-inventory.json
```

Default normal and optimized runs are byte-identical:

```text
stdout_sha256=34a498085240c2504d5e780e95f66a63548bf3edb49af3ae3d57c01ef41505f7
```

Both print:

```text
MARKDOWN FILES SCANNED: 524
ACTION-RELEVANT FILES: 501
CORPUS STREAM SHA256: 51d19c00e979ecfb796aba2c34e810cfbe3bd00586e8703c1ce54c7826877c6e
INVENTORY SHA256: 31e0ddbf3d32f066ec657327c0b0824352cf80b2f92953ae176bd0ec87429ab9
CHECKS PASSED: 5/5
```

The JSON repeats the correct boundary, counts, corpus hash, and inventory
source hash.

### 3.2 The self-inclusion defect is closed

The inventory includes all V1--V9 Markdown and only antecedent V10 Markdown.
Within V10 it excludes filenames containing `d13` and Paper 14's filename.
The frozen count and corpus hash are asserted before output.

I independently inspected the generated file list:

```text
self-included D13/Paper14 paths = []
unique relevant paths          = 501
listed relevant paths          = 501
```

Adding this round-2 review therefore does not change the census.  A
misnamed future D13 file could enter the path set, but the frozen count/hash
would cause a hard failure rather than silent receipt drift.

### 3.3 Truncation and fake-check defects are closed

The source no longer applies `[:24]` to headings or scope guards.  In the
current JSON, long cumulative papers retain hundreds or more than a thousand
headings/guards; the first-round late-section blindness is gone.

The three theorem-relevant corpus quantities—file count, relevant count, and
stream hash—are actual expected-value assertions.  Every relevant file must
also have a nonempty hit ledger.  The `5/5` label is therefore materially
stronger than the old four unguarded print statements.

The fourth printed PASS (untruncated extraction) is primarily a source-
structure assertion rather than mutation-sensitive runtime validation, but
the frozen source and inventory stdout hashes make this a nonblocking receipt
hardening issue, not renewed corpus drift.

## 4. Repaired V1--V10 action ledger

### 4.1 V7 Papers 47--51 are now present

The human ledger explicitly adds the late selector sequence and gives the
correct disposition:

- Paper 47's Einstein residual assumes a selected carrier, scale anchors,
  typed sources, stationarity, residual separation, and projective stability;
- Paper 48 calibrates finite constraint penalties while physical tolerances,
  large-panel satisfaction, numerical couplings, and a unique amplitude remain
  conditional/open;
- Papers 49 and 51 turn manifoldlikeness into calibrated response/coercivity
  and entropy-versus-action conditions whose proto-metrological seed still
  has to be physically generated; and
- Paper 50 proposes record-sensitive anomaly experiments but supplies no
  observed action selector.

None chooses the microscopic grammar, amplitude, field content, boundary
state, record instrument, or absolute units.  Their inclusion closes the
specific round-1 omission without changing the no-go.

### 4.2 Targeted older candidates remain correctly adjudicated

Clean-room reinspection confirms the earlier findings:

- V4 Paper 25 is a conditional effective-GR normal-form/Ward theorem with a
  supplied action/reference/alphabet/source dictionary and strong EU/Cartan
  assumptions.
- V6 Paper 4's commitment fixed point is a genuine unique coefficient
  selector on a fixed primitive quotient ledger, reference, orientation, and
  log-partition functional; it does not select that arena or complex action.
- V7 Paper 29 uniquely projects a supplied likelihood onto a committed
  filtration; it does not select the likelihood or physical filtration.
- V7 Paper 40 gives a unique convex minimizer after the boundary-work terms,
  channels, masses, scales, coercivity, and projective hypotheses are supplied.
- V8 growth actions retain placement/victim/committer freedom and measured
  sparse/dense failure modes.
- V9's mode-Hamiltonian sign selection is void at exact completion because
  omitted cumulant/Legendre terms reverse or split the coefficient.

### 4.3 Additional search: V4 Paper 39

The most serious candidate not individually named in the human ledger is:

```text
v4/relativistic-isp-v4-paper39-standalone-ontology-free-yang-mills-proof.md
```

Its title and internal theorem chain make it look like a possible action-
selection exception.  Its own front matter and final frontier map are clear,
however:

- it fixes the pure `SU(N)` field/gauge sector and regulator class;
- the theorem is a conditional standard Yang--Mills confinement/gap
  reduction;
- the fixed-physical-scale infrared bridge IR1--IR6 remains required;
- uniform 4D continuum bounds, Euclidean restoration, zero-flow local fields,
  non-Gaussian nontriviality, and the mass gap are listed as open in the
  established literature; and
- its Wilson/heat-kernel equivalence is within the already chosen pure-gauge
  action sector.

It therefore does not choose the universe's gauge group, matter content,
renormalized coupling, vacuum/boundary state, record instrument, or complete
action.  It does not overturn D13.  Because it is the corpus's strongest
standalone internal field-action claim, the next ledger edit should add an
explicit V4 Paper 39 row rather than leaving it implicit in the generic V4
normal-form entry.

No other newly searched `unique action`, `selected action`, Hamiltonian, or
variational candidate escaped the existing version-level dispositions.

## 5. Literature, candidates, and originality

The round-1 literature repairs are correct:

- process-tensor completeness/reconstruction now cites Pollock et al.
  `arXiv:1512.00589`, the direct source, rather than only the later operational
  Markov-condition paper;
- Lovelock's metric uniqueness theorem is linked to its primary publication;
- maximum entropy/caliber is anchored to Jaynes's original formulation;
- general-boundary amplitudes, strong decoherence, Deser consistency,
  EFT/Warsaw operators, causal-set actions/growth, asymptotic safety, and
  causal-set phase suppression retain their accurate conditional scopes.

The candidate-class note no longer claims an exhaustive universal action
taxonomy.  It says B--E are the strongest candidate envelope found, keeps the
architecture census unproved, and grades the empirically known low-energy
packet only `EFFECTIVE-ACTION-ONLY`.  Live selector programs are explicitly
open rather than declared refuted.

The originality boundary is now accurate.  It credits D12 with the core
iSWAP-family counterexample and reserves D13's contribution for the fixed-
interval action reading, the corpus/literature audit, repaired quantum/record
cells, and the proposed action-to-record boundary-amplitude bridge.  It also
states that bridge universality is unproved.

## 6. Paper 14 receipt paths and status

Paper 14's status and claims match the reviewed artifacts:

```text
Status: repaired after D13 hostile round 1
formal verdict: INCOMPLETE-INVESTIGATION
proved result: FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
```

Every receipt path listed at the end of the paper exists:

```text
code/d13_corpus_action_inventory.py
data/d13-corpus-action-inventory.json
code/d13_finite_kernel_no_go_exact.py
data/d13-finite-kernel-no-go-exact.json
note-d13-v1-v10-action-ledger.md
note-d13-literature-audit-action-selection.md
note-d13-candidate-class-adjudication.md
note-d13-maximal-action-theorem.md
reviews/d13-round1-mathematics-hostile-review.md
reviews/d13-round1-ontology-locality-hostile-review.md
reviews/d13-round1-independent-rebuild-hostile-review.md
```

Paper hash reviewed:

```text
77309f48136b8036365157509e9d27f1032e2a602398a70d9598544b3592f77e
```

The paper does not cite the old SymPy script as authoritative and does not
claim that A0--A12 are closed.  It correctly withholds V9 geometry holdouts.

## 7. Nonblocking residual hardening

### 7.1 The reversible memory circuit is described, not executed

Check 20 defines the history law directly:

```python
histories={(0,0,0): 1/2, (1,0,1): 1/2}
```

and computes the two conditionals.  This is an exact visible non-first-order-
Markov witness.  It is also realizable by the described reversible circuit:
copy `X` to hidden memory, keep visible `Y=0`, then copy memory to `Z`.
However, the executable never constructs the memory registers or copy-gate
matrices.  The check label and Paper 14 call it an executed circuit.

For final closure, either implement the reversible permutation/CNOT circuit
and derive the history table from it, or rename the check to "visible history
law with a reversible-copy realization."  The finite kernel nonselection
theorem does not depend on this cell.

### 7.2 Persistence and repeat-read checks are algebraically duplicate

Checks 17 and 18 respectively compare:

```text
record_dist(later) == record_dist(before)
record_dist(later) == record_dist(sealed)
```

where `record_dist` was already defined as `record_dist(sealed)`.  They certify
the same marginal equality twice.  Since later operations act only on the
system register, record observables are structurally untouched, but no
separate repeat-read operation is executed.

For a final 21-cell receipt, make check 18 an actual idempotent record read or
a branch-conditioned repeat-read correlation rather than a duplicate marginal
test.  Again, this does not alter check 11's inequivalent predictions.

### 7.3 The SymPy predecessor should identify itself as replaced

`v10/code/d13_local_action_family_exact.py` remains discoverable and still
fails under default Python.  Paper 14's authoritative receipt list omits it,
and the repair note says the SymPy witness was replaced, so there is no current
scientific ambiguity.  For archive hygiene, make the old program print or
document `PRECURSOR_REPLACED_BY_D13_FINITE_KERNEL_NO_GO_EXACT` in-file, as D12
did for its one-cell predecessor.

## 8. Final gate ledger

| Round-2 item | Independent result | Status |
|---|---|---|
| dependency-free source | default Python, standard library only | pass |
| exact checks | 21/21 | pass |
| normal/-O stdout | byte-identical `587f768d...` | pass |
| source/semantic hashes | exact `b11f8ffc...` / `4eb19b0e...` | pass |
| inventory checks | 5/5 | pass |
| inventory normal/-O | byte-identical `34a49808...` | pass |
| antecedent corpus | 524 files / 501 broad-relevant / `51d19c00...` | pass |
| D13 self-exclusion | no D13/Paper14 file in inventory | pass |
| full headings/guards | untruncated | pass |
| V7 P47--P51 ledger | explicitly included and correctly scoped | pass |
| V4 P39 | conditional YM reduction; not individually ledgered | nonblocking addition |
| literature repairs | primary/process-tensor citations corrected | pass |
| candidate status | live selectors retained; universality unclaimed | pass |
| originality | D12 credited | pass |
| Paper receipts/status | all paths exist; `INCOMPLETE-INVESTIGATION` | pass |
| visible-memory circuit execution | history table exact; circuit not constructed | nonblocking hardening |
| repeat-read cell | duplicates persistence marginal | nonblocking hardening |
| old SymPy predecessor | non-authoritative but not bannered | archive hardening |

The independently supported result is exactly the one Paper 14 now claims:

```text
On one fixed operational diamond interval, the tested finite local-unitary
principles admit two physically inequivalent kernels.  Therefore they do not
select a unique interaction angle.  General action architecture, physical
fields, grammar, state, record instrument, covariance, units, and empirical
selection remain open.
```

**Round-2 independent-rebuild verdict: PASS at the narrowed theorem and
declared `INCOMPLETE-INVESTIGATION` scope.  Apply the three receipt/ledger
hardenings before final archival closure.**
