# D13 hostile review, round 3: independent focused closure

**Referee:** independent clean-room focused rebuild  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE NARROWED FINITE-KERNEL / `INCOMPLETE-INVESTIGATION` SCOPE**

All three round-2 hardenings are materially closed.  The dependency-free
receipt now executes an exact reversible memory circuit rather than inserting
its visible histories, performs a distinct controlled repeat-read into a fresh
record register, and binds the Born-once cell directly to the sealed branch
mass.  It still passes exactly 21 checks under default normal and optimized
Python with byte-identical output.  The semantic result remains unchanged,
while the source and stdout hashes correctly change.

The antecedent corpus inventory remains byte-stable after the additional D13
notes and reviews.  The human ledger and Paper 14 now explicitly adjudicate V4
Paper 39 and D9's conditional Bell selection.  The retained SymPy source begins
with an unambiguous superseded/replacement banner.  I found no remaining
focused mismatch.

## 1. Reproduction and frozen hashes

### Authoritative 21-check source

Direct hashes:

```text
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  v10/code/d13_finite_kernel_no_go_exact.py
60cbfe88baa4da37ab6a323cc3f73198caf614222a91c1158290f877e576efda  v10/data/d13-finite-kernel-no-go-exact.json
```

Normal and optimized execution both complete at 21/21.  Their complete stdout
hash is identical:

```text
883e68627002aa33de6a8c3946c5d21f5d8771c257e3d0e1c1184110f26859c2
```

Both print:

```text
CHECKS PASSED: 21/21
SEMANTIC SHA256: 4eb19b0eb34bdc9cd910029cb3d4c22bb47d8d847e0fe12353a7b5eac69f2852
SOURCE SHA256: 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
VERDICT: FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
```

The generated JSON repeats the correct check count, semantic hash, source
hash, fixed-interval scope, unequal predictions, memory conditionals, and
verdict.

The semantic hash properly remains the round-2 value: the theorem-level facts
did not change.  The new source hash and stdout hash capture the strengthened
implementations.

### Antecedent corpus inventory

Direct hashes remain:

```text
06226a2bd93a3314fe74aaefe1d2a26b2869197dad77f2fa4c1177673e9e753d  v10/code/d13_corpus_action_inventory.py
31e0ddbf3d32f066ec657327c0b0824352cf80b2f92953ae176bd0ec87429ab9  v10/data/d13-corpus-action-inventory.json
```

Normal and optimized full stdout remain byte-identical at:

```text
34a498085240c2504d5e780e95f66a63548bf3edb49af3ae3d57c01ef41505f7
```

The frozen boundary remains:

```text
antecedent Markdown files=524
broad action-relevant files=501
corpus stream=51d19c00e979ecfb796aba2c34e810cfbe3bd00586e8703c1ce54c7826877c6e
checks=5/5
```

No D13 or Paper 14 path occurs in the generated file ledger.  Additional D13
review files therefore do not enter the semantic census.

## 2. Executed memory circuit

The previous receipt only wrote down

```text
(X,Y,Z)=(0,0,0) or (1,0,1)
```

and observed the different conditionals.  The repaired source now constructs
a 16-dimensional permutation matrix on four bits ordered `X,M,Y,Z`.

For every computational-basis state it applies:

```text
M <- M xor X
Z <- Z xor M
```

which is exactly `CNOT X->M` followed by `CNOT M->Z`.  Each source basis vector
maps to one distinct target basis vector, and the executable checks

```math
U_{mem}^\dagger U_{mem}=I_{16}.
```

The input density is the equal mixture of `|0000>` and `|1000>`.  Conjugating
it by the executed permutation gives the two branches:

```text
|0000>  -> |0000>
|1000>  -> |1101>
```

Tracing/summing over hidden memory `M` produces the visible history law:

```text
P(0,0,0)=1/2
P(1,0,1)=1/2
```

and hence exactly:

```math
P(Z=1\mid Y=0,X=1)=1,
\qquad
P(Z=1\mid Y=0,X=0)=0.
```

This is now an executed reversible memory realization, not a hard-coded
history table.  The enlarged four-bit dynamics is reversible, while the
visible `X,Y,Z` process is not first-order Markov in `Y`.  Paper 14 correctly
uses it only as a compatibility witness, not a claim that every amplitude
process has memory.

## 3. Distinct repeat-read and Born-once gates

The receipt's record register has four values.  After a licensed later
system-only unitary, the repaired repeat-read operation appends a fresh
four-level register initialized at zero and applies controlled modular
addition:

```math
|r\rangle_R|0\rangle_Q\longmapsto |r\rangle_R|r\rangle_Q.
```

The resulting joint distribution is checked entry by entry:

```text
P(R=r,Q=q)=P(R=r) if r=q, and 0 otherwise.
```

This is distinct from check 17's earlier marginal-persistence comparison and
establishes perfect repeat-read agreement within the declared future algebra.

The Born-once gate is also sharper.  It verifies that the instrument trace
`p=1/2` equals the corresponding sealed record branch mass and that replacing
it by `p^2` would change the value.  The check now ties the no-double-weight
statement to two independently constructed representations of the same
branch probability.

These are finite instrument cells.  They still do not derive the physical
record instrument or persistence under arbitrary operations on the record
register, and Paper 14 retains that limitation.

## 4. V4 Paper 39 ledger entry

The human ledger and Paper 14 now name V4 Paper 39 explicitly.  Their
disposition matches the source:

- Paper 39 fixes a pure `SU(N)` gauge sector and Wilson/heat-kernel regulator
  architecture;
- its front matter calls the 4D result a conditional confinement/gap
  reduction;
- its fixed-physical-scale infrared bridge IR1--IR6 remains required;
- its own frontier map lists full 4D continuum construction, fixed-scale
  nontriviality, and the mass gap as open in established literature; and
- it does not choose the gauge group, matter content, renormalized coupling,
  vacuum/boundary state, record ontology, or universe action.

It is therefore a strong conditional sector construction, not an overlooked
complete action selector.  The explicit row closes the round-2 human-ledger
omission.

## 5. D9 conditional empirical selector

The new D9 row correctly qualifies the otherwise overly broad phrase "no
selector."  D9/Paper 10 establishes:

```text
maximal Bell records -> theta=pi/4
```

only inside a frozen one-partial-iSWAP preparation family.  This identifies a
parameter conditional on that model; it does not select the preparation
family or the complete action.

D9 then makes the additional cross-sector identification

```math
g_{geometry}=\sin^2\theta=1/2
```

and tests it on 24 fresh geometry seeds.  The holdout refutes that
one-coupling map, not the SCIR architecture.  The repaired D13 ledger and
Paper 14 state exactly this distinction: partial empirical parameter
identification succeeded, complete matter-plus-geometry action selection did
not.

## 6. Superseded SymPy predecessor

The retained file

```text
v10/code/d13_local_action_family_exact.py
```

now begins:

```text
SUPERSEDED ROUND-1 D13 WITNESS (retained for review provenance).
Replacement: d13_finite_kernel_no_go_exact.py ...
```

Its changed source hash is:

```text
b2370e270086ceec6a53e1cdd9f4a4d861ef00ab8ef642549ca16fdff4086f65
```

The banner is visible before the external SymPy import, so even a default-
Python failure cannot be confused with the authoritative receipt.  Paper 14
continues to list only the dependency-free replacement.

## 7. Paper and repair-note consistency

The repair note records the current hashes exactly:

```text
21-check source  1ea9969c...
21-check stdout  883e6862...
semantic         4eb19b0e...
inventory source 06226a2b...
inventory stdout 34a49808...
antecedent corpus 51d19c00...
```

Paper 14 now includes both the V4 Paper 39 and D9 qualifications and describes
the executed memory circuit and repeat-read at their actual finite scope.  Its
current hash is:

```text
575fdbb1c06933ed5da877030739e7ded421e197d3647ac17013cadfaf271f1f
```

The formal paper verdict remains `INCOMPLETE-INVESTIGATION`; the proved result
remains only `FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED`.  No geometry
holdout is newly licensed.

## 8. Final determination

| Focused item | Independent result | Status |
|---|---|---|
| dependency-free normal/-O runs | byte-identical | pass |
| exact check count | 21/21 | pass |
| source hash | `1ea9969c...` | pass |
| stdout hash | `883e6862...` | pass |
| semantic hash | `4eb19b0e...` | pass |
| memory realization | explicit unitary permutation/CNOT circuit | pass |
| visible non-Markov conditionals | derived exactly from circuit output | pass |
| record persistence | later system-only marginal invariant | pass |
| repeat read | fresh controlled register, perfect diagonal agreement | pass |
| Born once | instrument trace equals sealed branch mass | pass |
| inventory normal/-O | byte-identical `34a49808...` | pass |
| inventory self-exclusion | stable 524/501 antecedent boundary | pass |
| V4 Paper 39 | explicit, correctly conditional | pass |
| D9 | partial conditional selector plus failed cross-sector map | pass |
| old SymPy source | explicit superseded banner | pass |
| Paper/repair receipt consistency | current and scoped | pass |

No focused opening remains that weakens the exact finite nonselection theorem
or creates an uncredited earlier complete action selector.

**Round-3 independent-focused verdict: PASS at the narrowed finite-kernel
theorem and declared `INCOMPLETE-INVESTIGATION` scope.**
