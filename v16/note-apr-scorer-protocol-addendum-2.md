# APR scorer-protocol addendum 2 — malformed recovery and grammar rows

**Date:** 2026-08-18

**Status:** BINDING FORWARD CORRECTION TO
`v16/note-apr-scorer-protocol.md` AND
`v16/note-apr-scorer-protocol-addendum.md`. This correction freezes while
`v16/code/apr_score.py` is absent and before any APR fixture truth is
computed. It does not change a registered outcome word.

## 1. Ill-typed sequential recovery row

`rw_002` lists `ro_004` followed by `ro_005` as one sequential operation
word. The composition is ill-typed: `ro_004` returns a one-field reader
output, while `ro_005` requires the original three-field carrier.

The scorer must therefore refuse `rw_002` as a sequential recovery word. It
may independently form the two well-typed diagnostic prefixes

```text
ro_003 then ro_004
ro_003 then ro_005
```

from the common three-field post-writer state. Those are separate reader
controls, not a frozen parallel-effect operation and not a joint double-read
result. The scorer may not repair `rw_002` by guessing parallel semantics,
reordering operations, retaining a hidden copy of the input, or treating a
reader as an identity-on-carrier channel.

This refusal does not kill the independently typed single-reader controls.
It does kill any positive recovery, redundancy, or process-provenance claim
whose only support is the malformed word.

## 2. Undeclared mixed-tree constructor

The public mixed-tree grammar `qg_003` declares productions containing
`replace(...)`. Rows `mx_007` and `mx_008` instead use
`intrinsic_replace(...)`, which is not a declared production of that grammar.
The separate intrinsic replacement grammar `qg_004` does not, by its mere
existence, extend `qg_003` or establish an alias.

The scorer must refuse those mixed-tree rows as unparseable under the frozen
public grammar. It may continue to evaluate the intrinsic replacement rows
inside their separately typed `qg_004` scope. It may not invent an alias,
splice grammars, call a private helper, or count the malformed mixed rows as
evidence for question/replacement process closure.

## 3. Boundary identity scope

The frozen empty-tree cospan assignment exists only at the depth-zero
boundary (`qw_000 -> hf_015`). Categorical identities at the B1/B2/B3
boundaries can be defined in a future total forest construction, but they are
not frozen as process assignments here.

The scorer may report the registered B0 identity control. It must report
all-boundary identity and total-functor identity as `UNCONSTRUCTED`, not infer
them from category vocabulary or fabricate empty cospans at unregistered
boundaries. This is one concrete reason the finite record-tree presentation
cannot yet pass the horizontal regional process rung.

## 4. Ontology consequence

Malformed syntax and missing identity assignments are not physical
discoveries. Refusing them preserves the distinction between a list of
record-tree diagrams and one compositional law. No point-free regional
referent, causal structure, matter-geometry backreaction, metric, or gravity
claim may rely on any of these rows.
