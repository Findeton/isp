# PPR candidate verification

Status: **GREEN-UNREVIEWED; CANDIDATE REPLAY VERIFIED**.

Verified candidate commit:
`0f7a4b9bfc55be224143b2bc56bd4a5f5f51e5ee`.

The committed artifacts remain:

| artifact | SHA-256 |
|---|---|
| `v16/code/ppr_score.py` | `c7f1cfb63b179746d0a66f28c1a6ec79975f8489a025d1196a2531d9fee069d6` |
| `v16/code/ppr_fixture.json` | `cecc3b0d3c7bf46503481fa7b422e915ba0ff6aac42e3cec5f61c395e565b389` |
| `v16/code/ppr_output.txt` | `0c85efb4186e0faf6afc55f06184e9351bd6df621297ab2155745d7106e45b05` |
| `v16/code/ppr_receipt.json` | `dc88d6a2fbcf350785cc5f12cdcb8ea0805c4df6deaacac9ceffd34b1699c630` |
| `v16/paper-03-contextual-pullbacks-permanent-records.md` | `ca7b06e9e5540d81afb4a401beb66cb2834e3e74033fd742ac5257108a19654f` |

## Deterministic replay

Two clean worktree invocations using distinct empty output paths are mutually
byte-identical and byte-identical to the three committed result artifacts.
The canonical existing-artifact invocation refuses with exit 2 and changes no
file.

A `git archive` of only the committed runtime/read set at candidate commit
`0f7a4b9` was extracted without `.git` metadata. From alien working directory
`/private/tmp`, the archived scorer wrote to fresh explicit paths. Its paper,
transcript, and receipt are byte-identical to the committed artifacts. No git
command or mutable worktree path is used by the scorer.

## Independent integrity audit

An external receipt reader, sharing no scorer renderer, confirms:

- all 8 payload keys are present in the seal manifest and all 8 hashes
  recompute;
- all 25 gate rows pass and the summary is exactly 25/25;
- all 10 generated exact-claim sentences occur exactly once in Paper 3;
- the builder and independent comparator both return numeric outcome 9;
- the source and fixture hashes match receipt provenance;
- the fixture has zero keys named `expected`, `result`, `verdict`, or
  `outcome` at any nesting depth;
- the source abstract syntax tree contains zero floating-point constants, and
  no `isclose`, tolerance, or scientific-notation comparison path exists;
- all 20 registered mutant names are distinct and sealed; and
- the paper and transcript hashes recompute from committed bytes.

Source compilation passes for both the generic core and physical scorer.
`--selftest` passes without an artifact, and an unknown CLI flag exits 2.

## Mutation battery

Every mutant exits 1 and writes none of its three requested artifacts:

| mutant | first rejecting gate |
|---|---|
| `anchor-corrupt` | `PPR-ANCHORS` |
| `event-mix` | `PPR-EVENT-ALGEBRA` |
| `split-weight` | `PPR-HISTORY-REFINEMENT` |
| `kraus-promote` | `PPR-CHANNEL-INSTRUMENT-QUOTIENT` |
| `pullback-half` | `PPR-HETEROGENEOUS-PULLBACK` |
| `dark-reactivate-drop` | `PPR-STABLE-NULL-DESCENT` |
| `null-promote` | `PPR-STABLE-NULL-DESCENT` |
| `eraser-ignore` | `PPR-RECORD-AVAILABILITY` |
| `record-preplant` | `PPR-PARTITION-CENSUS` |
| `comparison-phase` | `PPR-COMPARISON-COCYCLE` |
| `transport-flatten` | `PPR-COMPARISON-DYNAMICS-TYPE` |
| `loop-conflate` | `PPR-COMPARISON-DYNAMICS-TYPE` |
| `graph-copy` | `PPR-EVENT-ALGEBRA` |
| `graph-erase` | `PPR-RELATIONAL-REWRITE` |
| `probe-feedforward` | `PPR-RELATIONAL-REWRITE` |
| `spectator-couple` | `PPR-LOCAL-COMPOSITION` |
| `completeness-amplify` | `PPR-ALL-INPUT-COMPLETENESS` |
| `result-count-type` | `PPR-PARTITION-CENSUS` |
| `verdict-flip` | `PPR-INDEPENDENT-PRIMARY` |
| `seal-after-write` | `PPR-POST-SEAL-IMMUTABILITY` |

## Status and remaining gate

This verifies implementation integrity, not physical truth or theorem scope.
The candidate remains
`PPR-CONTEXTUAL-PULLBACK-CONSTRUCTED-BUT-LAW-UNSELECTED` and
**GREEN-UNREVIEWED**. It is not a record-generated fixed point, unique law,
gravity theory, continuum limit, QFT reconstruction, particle theory, or
actualization result.

The next process step is a frozen hostile protocol followed by three mutually
independent read-only reviews: operator/representation,
histories/category/congruence, and relational geometry/gravity. Under the
active collaboration rule, assigning those independent reviewers requires an
explicit user instruction to delegate; this verification does not supply that
authorization.

