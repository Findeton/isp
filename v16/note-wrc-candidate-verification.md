# WRC candidate verification

Status: **REPLAY-VERIFIED GREEN-UNREVIEWED**.

Candidate commit: `e5fb6047a84805b5bd260d969099bb229e369441`.

The candidate artifacts verified here are byte-immutable:

| artifact | SHA-256 |
|---|---|
| `v16/code/wrc_output.txt` | `45d386714b600ae3dc78369e3785cd78788333a3d0b6bdd31917289d03c2c34c` |
| `v16/code/wrc_receipt.json` | `017debe87508bd91b64fa413870af47c5969b442240bff2fa998a538b2de4fef` |
| `v16/paper-08-walk-reconstruction.md` | `6934297cc2a79a8d7ebfa4dd7c52a58d601d686adf9d91b15c45fe416291e0f5` |

Frozen constructor hashes also re-match: pin
`956d26e22515471c49ed95a43b2956d8f73e8bcd662eeacc82215d9527c00f99`,
provenance addendum
`a93f648cbdff08fba97054b2b28fe261375bccc52d4ebc3b81c1d9f25bc04a7e`,
core `94c74731179c1302254a3b7424dcb66d1154518bcf936c5531b05a52f42fa6b3`,
core-freeze note
`5220f66b187769e6efb0e6f4b1bbc627f5d71f4ac3968ed057d23cc3d3884993`,
fixture `4ced0a163d645072ded79c51c92cf6f847576f062f35091df67db6d6f8a971c8`,
repaired scorer
`58555958108ea62d28ebb541c5da8f6e9a3ec9ea50ef9a16540ee0df0ce1a128`,
and fixture-freeze note
`f6622aeb0dbd72c7942521a341ce7acfa0fb8340cb9ef1b78fba9c5b5e881fd4`.

## Replay-repair audit

The first replay of candidate #94 refused before physical scoring because that
candidate had performed the pin-authorized post-result Q8 board update, while
the frozen scorer accepted only the pre-result board hash. Repair commit
`3f75079a970b32f95b1740c4bb07bc2bd9fd79f8` changes only the scorer's
provenance predicate: `v16/QUESTIONS.md` may have either the frozen pre-result
hash/tokens or the one exact post-result hash plus three terminal-scope tokens.
No third state is accepted.

Before official regeneration, the repaired scorer reproduced the #94
transcript and Paper 8 byte-for-byte. Regeneration #96 again kept both bytes
unchanged; only the receipt moved, exactly in its scorer hash, Q8 anchor row,
dependent seals, and payload digest. The scientific result object, comparator,
claims, targets, scope, transcript seal, and paper seal are unchanged. The
failure and repair remain explicit evidence for hostile review rather than
being erased from the chronology.

## Replay, payload, and CLI

Two clean worktree invocations to six disjoint temporary result paths
reproduce transcript, receipt, and paper byte-for-byte. The receipt's payload
digest, twelve manifest seals, 31 unique passing gates,
13 claims, 13 qualifiers, 13 scope walls, and twelve runtime anchor bindings
all verify independently.

`--selftest` exits `0` only after its internal anchor mutant is refused;
unknown options exit `2`; an invocation aimed at the existing official targets
exits `1` before evaluation. No failed invocation writes an artifact. The core
and scorer contain zero Python float literals and the fixture contains zero
JSON float values.

## Mutation battery

All `34/34` registered mutants exit `1`, emit no stdout or traceback, begin
with `WRC REFUSAL:`, and write no transcript, receipt, or paper:

```text
anchor-hash / anchor-token -> WRC-ANCHORS
receipt-binding -> WRC-PATH-VALUES
carrier-catalogue / cell-dictionary -> WRC-PACKET-REFERENT
coin-entry -> WRC-TRANSPORT-UNITARY
phase-power / record-increment -> WRC-SOURCE-REGRESSION
shift-orientation / initial-state -> WRC-SOURCE-DECLARATIONS
cut-order / clock-boundary -> WRC-CLOCK-CUTS
born-normalization -> WALK-BORN-NORMALIZATION
branch-state -> WRC-ONTIC-PSI-CONTROL
beable-histogram -> WRC-BEABLE-MAP
mixture-affinity -> WRC-NONAFFINITY
cp-completeness -> WRC-CP-COMPLETENESS
cp-state / continuation -> WRC-CP-REPAIR-DISCRIMINATOR
translation-action / record-translation / absolute-anchor -> WRC-TRANSLATION-COVARIANCE
gauge-phase -> WRC-GAUGE-SELFTEST
recurrence-signature -> WRC-RECURRENCE-CENSUS
hidden-coin -> WRC-COUPLING-FIBER
coupling-typing -> WRC-COUPLING-TYPING
arena-scope -> WRC-SCOPE-WALLS
cell-hit-type -> WRC-TERM-BINDING
primary-comparator -> WRC-PRIMARY-COMPARATOR
q8-retirement -> WRC-QUALIFIERS
exact-arithmetic -> WRC-FIXTURE-NEUTRAL
transcript-binding -> WRC-TRANSCRIPT-BINDING
paper-claim -> WRC-PAPER-CLAIMS
prewrite-seal -> WRC-PREWRITE-SEAL
```

The record-translation mutant is important: translating the quantum vector
while holding the deliberately nonuniform record fixed fails covariance. The
mixture mutant is also theorem-sensitive: a zero displayed witness cannot pass
while the independently checked non-scalar-effect criterion says the rule is
all-input nonaffine.

## Independent exact reconstruction

An implementation importing neither `wrc_core.py` nor `wrc_score.py` uses
only integers, rational numbers, and explicit pairs for
`Q(w)`, `w^2+w+1=0`. It independently confirms:

- all three artifact hashes, the outer payload digest, twelve manifest seals,
  twelve current anchor hashes, 31 unique passing gates, and every paper claim;
- the 27-cell co-division-pair carrier, 81-entry transport support, and six
  cells moved between the post-coin and post-shift labelled screens;
- the exact five-tick branch ladder `3, 27, 486, 10527, 284078`, unit mass at
  every tick, and all nine registered observable families, including exit
  `927415552/847288609443` and inverse participation
  `35971074413334039128803/239299329230617529590083`;
- four recurring local record signatures across distinct sites, the complete
  two-tick 27-history count-field map with zero violations, and the admitted
  alternate-coin inverse participation `51246599/129140163` versus Grover
  `33596579/129140163`; and
- source/CP probability `9/25`, all-input projective completeness, exactly six
  conditioned future probabilities moved, with the first `64/225 -> 0`, plus
  the independent non-scalar-effect proof of nonaffinity.

The exact pure-state branch recoding therefore survives as mathematics, while
the affine-instrument target fails at the registered held-out continuation.

## True off-tree/no-git execution

A `git archive` at candidate commit `e5fb604` containing only the frozen
scorer, core, fixture, and twelve runtime-read anchors was extracted under
`/private/tmp` with no `.git` directory. Executed from alien CWD
`/private/tmp`, it reproduces transcript, receipt, and paper byte-for-byte at
the immutable hashes above.

## Scope and disposition

WRC is **REPLAY-VERIFIED GREEN-UNREVIEWED**, not terminal. It reconstructs the
committed finite fixed-carrier walk packet and exposes the source CELL-HIT
instrument defect. It does not construct carrier growth, a relation-generated
history family, relational graph backreaction, a selected law, or a
family-level geometry-irreducibility result.

In particular, the later methodological proposal is not silently counted as
evidence here. A meaningful eliminability test must predeclare a constrained
geometry-blind adversary class and compare one uniform rule on a family with
held-out carriers. DISC's third-tick result is evidence for memory dependence
against its registered memoryless classes; it is not by itself evidence that
the memory is dynamical geometry rather than a generic record. That distinction
is mandatory in hostile review and in any successor unit.

A separately frozen hostile protocol, three isolated reports, joint
adjudication, any ordered bounded repair, and terminal replay remain mandatory
before Paper 8 can be cited as terminal.
