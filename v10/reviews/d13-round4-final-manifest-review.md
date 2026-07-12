# D13 hostile review, round 4: final manifest and boundary audit

**Referee:** independent clean-room final-manifest audit  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE DECLARED FINITE-KERNEL / `INCOMPLETE-INVESTIGATION` BOUNDARY**

The final receipt agrees with the current bytes.  Both authoritative programs
reproduce under ordinary and optimized Python with byte-identical stdout.  The
antecedent inventory has the refined non-self-referential boundary of 522
Markdown files, 499 action-relevant files, and excludes all D13 self-files as
well as mutable V10 `PLAN.md` and `LOG.md`.  Every primary-artifact and prior
hostile-review digest printed in the receipt matches the corresponding current
file.

Paper 14, `PLAN.md`, `LOG.md`, and the final receipt agree on the scientific
claim boundary: D13 proves finite local-unitary kernel nonuniqueness but does
not select the complete action, license a V9 geometry holdout, derive a
universal sealed-diamond category, or close the requested investigation.

One nonblocking editorial residue remains in Paper 14: the second column of
the section 11 gate table is headed `status after round 1`, although the table
itself includes the final three-round A12 disposition and the paper header and
verdict sections correctly say three hostile rounds.  This stale column label
does not alter any gate status, theorem, receipt, or manifest hash.  It is not
a mathematical or scope blocker.

## 1. Authoritative inventory reproduction

I ran, from the repository root,

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d13_corpus_action_inventory.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d13_corpus_action_inventory.py
```

Both executions completed successfully and printed the same substantive
receipt:

```text
MARKDOWN FILES SCANNED: 522
ACTION-RELEVANT FILES: 499
CORPUS STREAM SHA256: bc95bed456aca8d8e65af121ac2f4f5069bcd70b4bd6685e5d02a32b242d0c91
INVENTORY SHA256: 6f5337cec925b61e41931cf8fbf6ffc6411ad0954b14d50a4ee435b4162b613a
CHECKS PASSED: 5/5
```

Hashing the entire stdout of each run gives the same value:

```text
normal  97108300f07af7e6874342fd1b95ca9ffce2b30726e31da9dd7254bf88dee1bb
-O      97108300f07af7e6874342fd1b95ca9ffce2b30726e31da9dd7254bf88dee1bb
```

The current source and generated JSON hashes are:

```text
efca2f21c22609d6e48231b7b0e4aec3ef797b7d4183095f22f80c13c8d9681a  v10/code/d13_corpus_action_inventory.py
6f5337cec925b61e41931cf8fbf6ffc6411ad0954b14d50a4ee435b4162b613a  v10/data/d13-corpus-action-inventory.json
```

These are exactly the values frozen in `d13-final-receipt.md`.

### Boundary check

The source excludes, inside V10:

1. `v10/PLAN.md` and `v10/LOG.md` explicitly;
2. every filename containing `d13`, case-insensitively;
3. Paper 14 through `paper14-the-action-behind`.

The JSON identifies its boundary as

```text
V1 through V10 D12; D13 self-files and mutable V10 PLAN/LOG excluded
```

and independently reports 522 scanned files and 499 relevant files.  Its
499-file ledger has 499 distinct paths.  Filtering those stored paths for
`v10/PLAN.md`, `v10/LOG.md`, `d13`, or `paper14-the-action-behind` returns no
path.  Thus writing this review cannot perturb the antecedent inventory.

## 2. Exact finite-kernel reproduction

I independently ran

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d13_finite_kernel_no_go_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d13_finite_kernel_no_go_exact.py
```

Both executions completed with exactly 21 labeled passes and printed:

```text
CHECKS PASSED: 21/21
SEMANTIC SHA256: 4eb19b0eb34bdc9cd910029cb3d4c22bb47d8d847e0fe12353a7b5eac69f2852
SOURCE SHA256: 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
VERDICT: FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
```

The entire stdout hashes agree byte for byte:

```text
normal  883e68627002aa33de6a8c3946c5d21f5d8771c257e3d0e1c1184110f26859c2
-O      883e68627002aa33de6a8c3946c5d21f5d8771c257e3d0e1c1184110f26859c2
```

Current authoritative bytes give:

```text
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  v10/code/d13_finite_kernel_no_go_exact.py
60cbfe88baa4da37ab6a323cc3f73198caf614222a91c1158290f877e576efda  v10/data/d13-finite-kernel-no-go-exact.json
```

The JSON contains the same 21-check count, semantic and source hashes, exact
verdict, interaction predictions `1/2` and `0`, and visible-memory
conditionals `1` and `0`.  All kernel entries in the final receipt therefore
match both execution and stored data.

## 3. Primary-artifact manifest

I hashed every primary file named in the receipt.  All seven entries match:

| Artifact | Current SHA-256 | Receipt |
|---|---|---|
| Paper 14 | `595716796938d7f19e45faf8ca5a4a91a34a9157770146c7de276be50018463d` | match |
| action-selection protocol | `c34f7212681007199e73f55ab6a2b7d9861d8e3e38bf3bf248024010c462d6be` | match |
| V1-V10 action ledger | `9e7c04c0a6dd294862169efef688a55b8c7fe1d13d864aca9e624cbed7bccb7a` | match |
| literature audit | `efe8792fd2c4fdcd78901b7de93e07fa77e4ef5bf7f652e630525ac8790f4173` | match |
| candidate adjudication | `0100f2f9e28e3c5e51193ebba44957a62f5d6877deaffc4cb502b0240358a262` | match |
| withdrawn maximal-action note | `836f2138945e7d210b93c3deafaaaaadea5ba80fbd1dffc848056b833176d7eb` | match |
| round-1 opening repairs | `6bfe606b6e68f4610d8d85edadef7875ec296fa5a6aa0875d9acbb4d0b7e79b9` | match |

The provenance qualification on `note-d13-maximal-action-theorem.md` is
accurate: the filename survives while its title and body withdraw the
maximal/universal theorem.

## 4. Prior hostile-review manifest

Every one of the nine prior review hashes also matches current bytes:

| Round and stream | Current SHA-256 | Disposition |
|---|---|---|
| R1 mathematics | `6fc74788de9c8c82e136094afb98bf8acac301d11182dfe046654361760a3614` | MAJOR REVISION |
| R1 ontology/locality | `ea7424ab604b54653d96f9dc2e4455967a84c20375fe221fb6b96563342e5d18` | MAJOR REVISION |
| R1 independent rebuild | `29203bd6ebbd0fdb2b619cb470f9dd9b1e1371dc20023a99ffaa2474e939c5a4` | MAJOR REVISION |
| R2 mathematics | `a683cccc7f6274fdc58512936f765e3f8495bb3589bd63a1c7884d065995511a` | PASS narrowed |
| R2 ontology/locality | `56727935ea5807e5be6d6324540aaee069db05f62ce6e61f4780a4bd01710fa3` | PASS narrowed |
| R2 independent rebuild | `cbed6355982ec9fa97cacac678e048107200fbc897605bd919fa06e0c6e13cdf` | PASS narrowed |
| R3 mathematics focused | `b7d9e19f9eeb4839d947a0691adf749a4d32c4fec177d9b440adf32b6510b623` | PASS |
| R3 ontology focused | `1be896d16cffa7f8a32a42d22f82a65cd10c3fe1d3d9f960b04b0d893aaeacf4` | PASS |
| R3 independent focused | `e1e35cb35c14bec117e03e79d4e869fcc55798786977e5a2dfad4abe59fc2c29` | PASS |

The manifest preserves the adverse round-1 history instead of rewriting it
as retrospective agreement.

## 5. Paper 14 claim-boundary audit

Paper 14's current SHA-256 is the manifest value
`595716796938d7f19e45faf8ca5a4a91a34a9157770146c7de276be50018463d`.
Its header says it is final after three hostile rounds at narrowed scope.  Its
abstract and verdict section distinguish:

```text
formal protocol verdict: INCOMPLETE-INVESTIGATION
proved result: FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
```

The paper does not turn the finite witness into a universal action theorem.
It explicitly leaves open the universal diamond category and sewing law,
Lorentz/diffeomorphism-covariant action, fields, state and record instrument,
couplings, units and `G`, and independent action selection.  It also withholds
all V9 geometry holdouts.  D9 is correctly limited to conditional parameter
identification inside a supplied partial-iSWAP family, followed by rejection
of the proposed one-coupling geometry map.

The final receipt's closed/open lists are faithful summaries of those paper
claims.

### Nonblocking table-label residue

At Paper 14 section 11, the column heading still reads

```text
status after round 1
```

but A12 in that same table reads `three hostile rounds pass the narrowed
theorem and receipt`, and the paper header, abstract, and section 12 all carry
the correct final disposition.  This is a stale editorial label, not a false
gate value or scope expansion.  Because this audit was instructed not to edit
primary artifacts, I leave it recorded rather than changing the frozen paper
and cascading every manifest hash.

## 6. `PLAN.md` and `LOG.md` consistency

The D13 plan section and final log entry agree with each other, Paper 14, and
the final receipt on all load-bearing points:

- three hostile rounds pass only the narrowed finite theorem;
- the formal protocol verdict remains `INCOMPLETE-INVESTIGATION`;
- the antecedent inventory is frozen at 522/499 and the plan prints the same
  `bc95bed4...` corpus digest;
- the exact kernel receipt passes 21/21;
- D9 is a within-family partial selector whose geometry mapping failed;
- no complete UV action, field content, state, record ontology, coupling set,
  physical scale, or V9 geometry result has been selected.

I found no plan/log contradiction and no claim licensed in one document but
withheld in the others.

## 7. Repository integrity

After both normal and optimized reruns, and after creating this review:

```text
git diff --check
```

returns successfully with no whitespace error.  The investigation scripts
were run with `PYTHONDONTWRITEBYTECODE=1`; the authoritative D13 data bytes
remain exactly those recorded above.  Unrelated pre-existing workspace
changes were neither modified nor adjudicated by this review.

## 8. Final determination

| Final-manifest gate | Result |
|---|---|
| antecedent count | 522/499, exact |
| corpus stream | `bc95bed456ac...`, exact |
| inventory normal/-O | byte-identical `97108300f07a...` |
| inventory source/JSON | `efca2f21c226...` / `6f5337cec925...` |
| kernel normal/-O | 21/21, byte-identical `883e68627002...` |
| kernel source/JSON | `1ea9969cb3e6...` / `60cbfe88baa4...` |
| kernel semantic receipt | `4eb19b0eb34b...`, exact |
| seven primary hashes | all match |
| nine prior-review hashes | all match |
| Paper 14 scope | narrowed theorem / incomplete investigation |
| PLAN/LOG | consistent |
| post-write antecedent stability | guaranteed by boundary and rechecked |
| `git diff --check` | pass |

**Round-4 final-manifest verdict: PASS at the finite local-unitary kernel
nonuniqueness theorem and explicit `INCOMPLETE-INVESTIGATION` boundary.**

