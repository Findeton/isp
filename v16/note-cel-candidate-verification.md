# CEL candidate verification

Status: **REPLAY-VERIFIED GREEN-UNREVIEWED**.

Candidate commit: `f3c3ef99f1506f01208a670198a91abe27c952d5`.

The candidate artifacts verified here are byte-immutable:

| artifact | SHA-256 |
|---|---|
| `v16/code/cel_output.txt` | `098d6113fb9f3ce0dbf43a28aeec213a5b06235c55556389989e93e1387028f6` |
| `v16/code/cel_receipt.json` | `a2fe34ccbbc8a1049824fd72020da5806e399f7a50a45e9bdf832e7e45a8eeda` |
| `v16/paper-07-creation-event-universality-recoverable-records.md` | `acf2dafb165d5ceb82bf4bc532b194f760095ce355b0b5ee7c5996df13878f90` |

Frozen constructor hashes also re-match: pin
`83762533fa6dad63acbeb3c13b2db9a63b6533b0ce113a61012d959552fa542d`,
core `f08b880095e71ac79082d2672ec849dc9ffd1ab66c702a85f2b24165a02aedac`,
core-freeze note
`01f584c0117a79f61d9dcb2dc352d7ecf291f4176f583882d72c5a13bfd6966c`,
fixture `8a18a70f1e1b7781806d800c54afd5dcbd10dbac1307db4420bafcb4b57854f2`,
scorer `27ee69af161382dfda3de81e1ea4d0edf4d6b4afb8d11d5f30ec7d3e075749c8`,
and fixture-freeze note
`b5bf12b6d8032601ed59a6d8d32d46ea7f4e809c842c3efa7020f3546d4748e7`.

## Replay, payload, and CLI

Two clean worktree invocations to six disjoint temporary result paths
reproduce transcript, receipt, and paper byte-for-byte. The receipt's outer
transcript/paper hashes, all eight internal payload seals, 44 unique gates,
13 paper claims, 11 qualifiers, 15 scope walls, and eleven runtime anchor
hash/token bindings all verify independently.

`--selftest` exits `1` at `CEL-ANCHORS`; unknown options exit `2`; existing
official targets refuse before evaluation. No failed invocation writes an
artifact. The generic core and scorer contain zero Python float literals and
the fixture contains zero JSON float values.

## Mutation battery

All `41/41` registered mutants exit `1`, emit no stdout or traceback, and
write no transcript, receipt, or paper:

```text
anchor-hash / anchor-token -> CEL-ANCHORS
history-typing -> typed CNOT refusal
kernel-entry -> CEL-R1-LOCAL-SURFACE-NONSELECTION
spectator-naturality -> CEL-R3-LICENSED-SPECTATOR-NATURALITY
operational-null -> CEL-R4-OPERATIONAL-NULL-QUOTIENT
exchange-licence -> CEL-R5-EXCHANGE-SYMMETRY-WITHIN-ORBIT
shared-restriction -> CEL-R6-SHARED-TOKEN-GLUING
shared-negative-control -> CEL-R7-GLUING-MISMATCH-REFUSED
universality-dimension -> CEL-R8-UNIVERSALITY-PRICE
universality-postulate -> CEL-R9-TYPE-UNIVERSALITY-IS-A-POSTULATE
reset-kraus / covariance-as-permanence -> CEL-P1-RESET-KILLS-BARE-COVARIANCE-CRITERION
relabeling -> CEL-P2-RELABELING-RECOVERS-WITHOUT-FIXED-PROJECTORS
writer-involution -> CEL-P4-INVOLUTIVE-WRITER-IS-ITS-OWN-FLAG-ERASER
copy-support -> CEL-P5 / CEL-P6
all-word-grammar -> CEL-P6-REDUNDANT-GRAMMAR-ALL-WORD-RECOVERY
catalogue-enlargement -> CEL-P7-CATALOGUE-ENLARGEMENT-DEMOTES-PERMANENCE
branch-label -> CEL-P9 / CEL-P11
recovery-licence -> CEL-P10 / CEL-P11
jcv-coefficient / dilation-isometry -> CEL-D1 / D2 / D4 / D5 and downstream weld gates
post-catalogue / flag-attachment / support-direction -> CEL-D3 or D4 and downstream weld gates
calibrated-statistic -> CEL-D5-CALIBRATED-FLAG-MOVES-AT-FIXED-CHANNEL
anonymous-classification -> CEL-D6-ANONYMOUS-ANCILLA-IS-NOT-A-RELATIONAL-FLAG
dilation-durability -> CEL-D7-SAME-DILATION-DIFFERENT-DURABILITY-GRAMMARS
scalar-obstruction -> CEL-E1-SCALAR-RESOURCE-WITNESS
three-row-witness -> CEL-E2-RANK-TWO-MINIMUM-THREE-ROW-WITNESS
ldl-reconstruction / row-bound -> CEL-E3-GAUSSIAN-RATIONAL-2R-CONSTRUCTION
psd-refusal -> CEL-E4-NONPSD-REFUSAL
some-vs-specified -> CEL-E5-SOME-SPECIFIED-AND-GRAMMAR-REALIZATION-SEPARATED
field-ontology -> CEL-EXACT-SOURCE / CEL-E6
actualization / all-n -> CEL-D8 or CEL-SCOPE-WALLS
exact-arithmetic -> exact-scalar refusal
primary-comparator -> CEL-PRIMARY-COMPARATOR
transcript-binding -> CEL-TRANSCRIPT-BINDING-PRECHECK
prewrite-seal -> CEL-PREWRITE-SEAL
```

The reset mutation specifically confirms that the quantum Kraus action and
the classical record transition must agree; merely leaving the classical
table unchanged cannot preserve the gate. The anonymous-control mutation
confirms that partial metadata is not enough: the negative control must lack
both a named attachment and relational rewrite.

## Independent exact reconstruction

An implementation importing neither `cel_core.py` nor `cel_score.py` uses
only integers, rational numbers, and explicit Gaussian-rational pairs. It
confirms:

- the eight seals, three outer artifact hashes, eleven anchor bindings, 44
  unique passing gates, and all 13 claims in the paper;
- overlapping-CNOT endpoints `111` and `110`, lawful biased/balanced screen
  probabilities `16/25` and `1/2`, the identical-history operational null,
  exchange selection inside its orbit, both joint restrictions, and the
  universality dimensions `2 -> 1`;
- the reset/relabel distinction, the involutive one-flag eraser, two-copy
  state `111 -> 101`, restricted grammar size `2`, enlarged grammar size `4`,
  and retained-versus-discarded identity/flip recovery;
- the two JCV Gram factorizations' common kernel `diag(16/25,9/25)`, flag
  vectors `(0,1)/(24/25,7/25)` and `(7/25,24/25)/(1,0)`, unit norms,
  calibrated movement `0 -> 49/625`, support equality, catalogue dimensions
  `2 -> 4`, and matter–flag attachment; and
- the scalar `7/5` two-row decomposition, determinant obstruction for the
  square rank-two factor, exact registered three-row factor, independent
  Hermitian `LDL^dagger`/four-square reconstruction of all four PSD controls
  with ranks `2,2,1,2` and rows `2,2,1,2`, and non-PSD refusal.

This independently confirms the primary word and all eleven qualifiers. It
also confirms the negative reading: recurrence universality remains a
postulate, durability remains catalogue/grammar-relative, the calibrated
coupling remains free, and the exact number field is not ontology.

## True off-tree/no-git execution

A `git archive` at candidate commit `f3c3ef9` containing only the frozen
scorer, core, fixture, and eleven runtime-read anchors was extracted under
`/private/tmp` with no `.git` directory. Executed from alien CWD
`/private/tmp`, it reproduces transcript, receipt, and paper byte-for-byte at
the immutable hashes above.

## Disposition

CEL is **REPLAY-VERIFIED GREEN-UNREVIEWED**, not terminal. The finite
creation-event-layer construction and every scope wall survive candidate
verification. A separately frozen hostile protocol, three isolated reports,
adjudication, any ordered bounded repair, and terminal replay remain mandatory
before the result can be cited as terminal.
