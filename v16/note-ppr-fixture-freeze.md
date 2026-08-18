# PPR physical fixture and scorer freeze

Status: **FROZEN BEFORE FIRST PHYSICAL EXECUTION**.

The separately frozen physical inputs are:

| artifact | SHA-256 |
|---|---|
| `v16/code/ppr_fixture.json` | `cecc3b0d3c7bf46503481fa7b422e915ba0ff6aac42e3cec5f61c395e565b389` |
| `v16/code/ppr_score.py` | `f3589042829650c081068342ad5c9b398db6691ade21b1b4c48deb5d6c6d7e73` |
| inherited `v16/code/ppr_core.py` | `490668340b08022ac5d11c8fdc07c392739153b609a72b9bda5bfcf112f472ea` |
| pin `v16/note-ppr-pin.md` | `cce2e194f1f1c557e2cb1745c0f15b9feaa98b48b2300126970098da0fadd48f` |

The actual pin commit is
`828b510a3229ae6330a55520b676a33e031c77a8`; the immutable JCV-terminal
base is `7e95322c589a42211e3a10cab7655492014bd0ae`.

No official execution has occurred. The output, receipt, and Paper 3 paths are
absent. Static source compilation passes. A source scan finds no floating-point
or tolerance mechanism and no typed PPR verdict literal in the scorer. The
data-only fixture contains no `expected`, `result`, `verdict`, or `outcome`
field. The scorer parses the ten ordered outcome labels from the frozen pin and
selects only a numeric index from measured predicates; a separately coded
comparator reconstructs that index from a serialized raw-measurement view.

## Frozen physical content

The fixture and scorer jointly instantiate, without executing:

1. graph-individuated relational events, a vertex relabelling, exact history
   split/merge, and same-channel/different-instrument Kraus controls;
2. a three-boundary continuation grammar with both delayed reactivation and a
   permanently dark direction;
3. a two-dimensional/three-dimensional heterogeneous fork and common-future
   Gram pullback with a reached-subspace tamper;
4. reconvergent, dangling-record, partial-overlap, and one-outcome
   interference controls;
5. an append-only record, a physical eraser, exhaustive finite partition
   censuses with unique nontrivial, unique trivial, and multiple-maximal cases;
6. a three-route same-fact comparison diagram and a separately typed physical
   transport loop;
7. an actual relation rewrite whose output graph computes the later probe,
   plus relabelling, graph-erasure, feed-forward, spectator, and disjoint
   controls;
8. two complete nonfactorizing rival laws and a held-out screen;
9. fixed-Bob unconditional no-signalling under two finite carrier-growth
   instruments plus an incomplete amplifier; and
10. all twenty pin-registered mutants, total payload sealing, pre-write
    renderer recomputation, and refusal to overwrite official paths.

## Forward-only corrections to ledger #34

The frozen `v16/note-ppr-core-freeze.md` printed the pin commit as
`828b51077ed85d1158135244fb6ea010b6d26350`. That string is wrong. The pin
was actually committed at
`828b510a3229ae6330a55520b676a33e031c77a8`, as `git log`, the fixture
anchor, and this freeze record state. The historical note is not edited.

The public core's two-coordinate row called a rational rotation an `eraser`.
That calibration proves only failure of one fixed-coordinate block partition;
a reversible basis rotation does not by itself destroy the availability of a
record. The physical scorer therefore does not import that interpretation. It
implements the stronger v12 co-live/co-merge support criterion: a record
survives exactly when every pair simultaneously live after the first leg is
kept in different future co-merge blocks. It also includes an explicit
tag-removal operation whose later interference is restored. The core bytes
remain frozen; this is a scope correction in the first downstream unit able to
make the physical distinction.

## Next authorized event

Commit this freeze as ledger #35. Then invoke the physical scorer once. Any
failure in that first execution must be frozen as the next ledger event before
repair; success may render the transcript, receipt, and Paper 3 from the one
sealed result object and commit those artifacts as-is before replay.

