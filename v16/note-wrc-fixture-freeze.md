# WRC Paper 8 — physical fixture and scorer freeze

Date: 2026-08-18  
Status: **FROZEN BEFORE OFFICIAL INVOCATION**  
Base commit: `ec26502d2266c7fad0e2c1b2d6277e03955886c5`

## Frozen bytes

| path | SHA-256 |
|---|---|
| `v16/code/wrc_fixture.json` | `4ced0a163d645072ded79c51c92cf6f847576f062f35091df67db6d6f8a971c8` |
| `v16/code/wrc_score.py` | `ff250da02a04c2cb98edc5fcdf5cf86da61072f0e014e6a2f67e9c8ae62772ad` |

The fixture is exact data. It contains no target, expected verdict, primary,
outcome, solution, or pass-count key. The scorer contains the complete frozen
outcome vocabulary and derives a primary from independent packet coordinates;
the fixture contains no comparator table.

## What the scorer measures

The scorer independently rebuilds the fixed 27-cell walk and binds the source
at full packet grain. In particular it:

- binds twelve antecedents by bytes and tokens, including both the original
  WRC pin and its provenance-only hash addendum;
- reconstructs the carrier, coin, record phase, shift, three cuts, Born tree,
  count-field beable map, and all nine committed observable families;
- tests translation covariance with a nonuniform record that is actually
  moved with the state and labels, plus a failing absolute-anchor control;
- separates the literal non-collapse operation, a complete affine CP
  comparison instrument, and the ontic-pure-state recoding;
- checks the exact mixture witness against an independent all-input theorem:
  the literal map is affine exactly when its effect is scalar on the trace-one
  domain;
- scores `TRANSPORT`, `AFFINE-CP`, and `ONTIC-PURE-STATE` in a separately
  sealed target table;
- extracts recurring local signatures and the admitted coin fiber without
  promoting a Born probability or coin entry to a selected constant; and
- carries all thirteen scope walls. Its rendered paper additionally states
  that fixed-fixture record dependence is not a family-level proof of
  irreducible geometry.

## Prefreeze validation and full disclosure

No official WRC target existed or was written during construction. Temporary
targets under `/private/tmp` were used to debug and harden the instrument.
The first physical dry run refused before scientific scoring on the pin's
mistyped `QUESTIONS.md` digest; ledger #83 froze that provenance-only repair.

Later temporary successful runs necessarily exposed the derived branch before
this freeze. After that exposure, the comparator and frozen outcome vocabulary
were not changed. The subsequent edits were all strengthening or neutrality
repairs and are disclosed here: inherited branch/max values were read from the
committed receipt rather than typed; all nine observable families were bound;
the translation record became nonuniform; the affinity witness was required
to agree with an all-input theorem; the CP continuation and hidden-coin gates
were split into assay validity versus measured movement; the three target
packets were separated; result-dependent prose was made conditional; and the
family-level eliminability refusal was added after the user's methodological
feedback. A hostile panel may price this prefreeze exposure, but no result word
or target literal moved because of it.

Two final clean temporary runs and one alien-CWD run are byte-identical in all
three rendered artifacts. All 34 named mutants refuse before writing any
target; the refusal directory is empty. The suite includes the new
`record-translation` mutant, the theorem-disagreeing affinity witness, CP-port
implementation, continuation quality, comparator, qualifier, claim,
transcript, exactness, and prewrite-seal controls. Selftest succeeds; unknown
CLI options, colliding targets, and existing targets refuse; the fixture and
both substantive Python paths contain no float literal or runtime float.

## Locked next action

There is now exactly one authorized official invocation, with no source edit
between this freeze and execution. It may write only:

```text
v16/code/wrc_output.txt
v16/code/wrc_receipt.json
v16/paper-08-walk-reconstruction.md
```

The unrelated v15 SCOUT-T files and every Paper 3–7 review remain outside the
WRC runtime and staging sets.
