# CSF candidate verification

Status: **REPLAY-VERIFIED GREEN-UNREVIEWED**.

Candidate commit: `61c32d884d688f49f29d3863fe5959d1053d382e`.

The candidate artifacts verified here are byte-immutable:

| artifact | SHA-256 |
|---|---|
| `v16/code/csf_output.txt` | `59077d8ad0f9e9ba4cf5afc0a44fea242d7a6032f1d998e088b3433cf4541785` |
| `v16/code/csf_receipt.json` | `7ae9b4a17fd38883bbff39b212f0edf819e2edf17942c9d54f8cf9f772414fdc` |
| `v16/paper-06-completeness-spectrahedra-record-fibers.md` | `543a2c927ecc7bd184fc758e4d72ebd4d4974327ae5ae2bb279d1fe33086c5d9` |

Frozen constructors and bindings also re-hash exactly: pin
`c953618c66685b20705bef7436ebfa29d4b0370b076493bc1997aea898e1bcba`,
core-freeze note
`60fc2c5b2174631f33bdb946e6b6c051cac533d9dbbe9fcbbde885d578d4068a`,
fixture-freeze/refusal/repair note
`b2a140a123cab91fe1aba19a87aa2ee9d9c09c97992260338123b3bd7be1ddf1`,
core `93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4`,
fixture `8c10210b6fee0a5477f3f70593cca080c26a4c91d678ad60bf691f6d853fbd37`,
and repaired scorer
`d3adf994e1c89fca5b53a0969cf0eed256488790b361477116b7cd1a76da84ba`.

## Replay and CLI

Two clean worktree invocations to six disjoint temporary result paths
reproduce the transcript, receipt, and paper byte-for-byte. `--selftest` dies
only at `CSF-ANCHORS`, exits `1`, writes no file, and emits no traceback.
Unknown options exit `2`. An ordinary invocation aimed at the existing
official paths refuses before evaluation, so candidate bytes cannot be
silently overwritten.

The scorer and generic core contain zero Python float literals; the physical
fixture contains zero JSON float values.

## Mutation battery

All 36 frozen mutants exit `1`, write only a refusal to stderr, emit no stdout
or traceback, and write no transcript, receipt, or paper:

```text
anchor-corrupt -> CSF-ANCHORS
history-event-mix -> CSF-HISTORY-INDIVIDUATION
gram-index-transpose -> CSF-ALL-INPUT-COMPLETENESS, CSF-CHANNEL-INDEX-ORIENTATION
completeness-cross-drop -> CSF-ALL-INPUT-COMPLETENESS
channel-cross-drop -> CSF-ALL-INPUT-COMPLETENESS
state-only-normalize -> CSF-ALL-INPUT-COMPLETENESS
psd-skip -> CSF-ALL-INPUT-COMPLETENESS
same-m-different-channel -> CSF-CALIBRATED-RECORD-FIBER
same-m-call-same-instrument -> CSF-CALIBRATED-RECORD-FIBER
calibrated-port-call-gauge -> CSF-CALIBRATED-RECORD-FIBER
jcv-first-move -> CSF-M-FACTORIZATION, CSF-JCV-BASE-FIBER
jcv-third-same -> CSF-JCV-BASE-FIBER
rich-spectrum-cross-keep -> CSF-RICH-SPECTRUM
rich-spectrum-call-record -> CSF-ERASER-PERMANENCE, CSF-SCOPE-WALLS
nonnormal-spectral-shortcut -> CSF-NONNORMAL-DIRECT
flag-overlap-ignore -> CSF-FLAG-SPECTRAL
orthogonal-call-durable -> CSF-ERASER-PERMANENCE, CSF-SCOPE-WALLS
eraser-drop -> CSF-ERASER-PERMANENCE
recurrence-dictionary-postselect -> CSF-RECURRENCE-DICTIONARY
recurrence-rephase-break -> CSF-RECURRENCE-DICTIONARY
recurrence-swap-break -> CSF-RECURRENCE-DICTIONARY
asymmetric-swap-impose -> CSF-EXCHANGE-LICENCE
context-drop -> CSF-RECURRENCE-INTERSECTION
heldout-use-in-fit -> CSF-RECURRENCE-INTERSECTION, CSF-HELDOUT-CONTEXT, CSF-PRIMARY-EQUALITY
intersection-dimension-type -> CSF-RICH-SPECTRUM, CSF-RECURRENCE-INTERSECTION
singleton-no-certificate -> CSF-SELECTED-KERNEL, CSF-PRIMARY-EQUALITY
extreme-equals-rankone -> CSF-EXTREME-TANGENT
extreme-stability-assume -> CSF-EXTREME-STABILITY
port-refinement-move-m -> CSF-PORT-REFINEMENT
steering-promote -> CSF-SCOPE-WALLS
all-n-promote -> CSF-SCOPE-WALLS
float-leak -> CSF-EXACT-ARITHMETIC
typed-count -> CSF-EXACT-ARITHMETIC
verdict-flip -> CSF-PRIMARY-EQUALITY
transcript-forge -> CSF-PROMOTION transcript binding
seal-after-write -> CSF-PROMOTION payload seal
```

The mutant name set is total and unique. No mutation exemption or post-write
failure is observed.

## Independent payload and mathematics audit

An independent exact implementation using only integer and rational-pair
arithmetic, and importing neither `csf_core.py` nor `csf_score.py`, confirms:

- all eight payload seals, both outer artifact hashes, all runtime-read hashes,
  30 unique passing gates, and 12 claims appearing exactly once in the paper;
- affine context dimensions
  `phase-sign=2, quarter-sign=2, rich-three=1, held-rich=1,
  left-calibrated=2`;
- independent training dimension `5`, recurring intersection dimension `1`,
  exchange-fixed dimension `0`, and the unique kernel
  `M=diag(1/2,1/2)`;
- completeness of that kernel in both the held-out rich context and the
  asymmetric calibration control;
- the JCV pair's common kernel `diag(16/25,9/25)`, calibrated first-port
  probabilities `0` and `49/625`, and the third kernel's changed channel;
- two calibrated factorizations of the selected kernel with retained-port
  probabilities `1` and `9/25`;
- the nonnormal `C^2 -> C^3` control, its relative map
  `[[0,3/5],[0,4/5]]`, and full real-linear affine dimension `1`;
- flag overlaps `1,3/5,0`, phase-compatible partial tagging, the real-weight
  and rich-spectrum failures, and reconvergence restoring overlap `1`;
- tangent nullities endpoint/selected/rich-restriction `0/0/1`, including a
  rank-2 selected kernel; and
- fixed-Bob marginal `I/2` before and after the complete unconditioned law,
  while the incomplete amplifier gives `2I`.

The audit thereby confirms the candidate's exact results and also its stated
limits: recurrence and exchange are input doctrine, calibrated port law is not
selected, orthogonality is not permanence, and fixed-factor unconditioned
no-signalling is not a conditional steering theorem.

## True off-tree/no-git execution

A `git archive` of every runtime-read path at candidate commit `61c32d8` was
extracted under `/private/tmp` without a `.git` directory. From alien CWD
`/private/tmp`, the archived scorer produces the transcript, receipt, and
paper byte-for-byte with the committed hashes above.

## Disposition

CSF is **REPLAY-VERIFIED GREEN-UNREVIEWED**, not terminal. The exact finite
candidate and all negative scope walls survive verification. A separately
committed three-lens hostile protocol, three mutually isolated reports,
adjudication, any authorized repair, and terminal replay remain mandatory
before citation as a terminal result.
