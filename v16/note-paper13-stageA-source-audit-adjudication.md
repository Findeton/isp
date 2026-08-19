# Paper 13 Stage-A source-audit adjudication

Status: **ADJUDICATED REJECT FOR STAGE B / FORWARD REPAIR PIN ONLY**

## 1. Immutable record

This adjudication concerns the committed Stage-A source at commit
`e203f72939ba1589c8c684f96d8d41777af209e3`:

- evaluator SHA-256
  `c699fc0316295e230c2cd0ef50601f631b195ad2237bebc2c42a75a2163f1aaf`;
- source-freeze note SHA-256
  `d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5`;
- construction-pin SHA-256
  `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35`.

Those bytes remain immutable.  They are not silently repaired or rescored.
No fresh case, official output, receipt, verification note, or Paper 13
candidate exists.

Two mutually blind reports are frozen:

1. `v16/review-paper13-stageA-source-physics.md`, SHA-256
   `20a054cd6542fd02f556b461408f48d75ead0c69ec06abd76c9eed3ce3c3d352`;
2. `v16/review-paper13-stageA-source-records.md`, SHA-256
   `7c5b14a04f938de05b64750f6c8ae454eb4bbe8d0824e9eaaa0016532ab52ed4`.

The adjudicator independently reconstructed the same changed source without
importing the evaluator.  All three reconstructions have mutant source
SHA-256
`a6cd95e0eb5c917fa3ad2f93441a2f56d9ec69e4f3801ec551dacdfdef4c5668`
and deterministic stdout SHA-256
`c5dbfe91701e5dd6f5e73a63c818448fa28d01c386f4a2ecc2dfdb0f5b8c28bc`.

## 2. Accepted finding

The pin defines horizontal extension by retaining each source cell and adding
a child-labelled partner for every cell satisfying the parent formula.  The
changed source instead replaces every satisfying parent cell by the
child-labelled cell.  On the minimal base

```text
source cells: (), (A)
lawful split: (), (A), (A,N)
mutant target: (), (A,N)
```

the mutant child is extensionally equal to its parent and the nonzero
Boolean-cell count remains two.  Forgetting the child still recovers the
source, but no cell was split and no new atom/support was created.

The frozen evaluator nevertheless reports roles `1 -> 2`, cells `2 -> 2`,
`all_support_changed:true`, `variable_carrier:true`, and
`support_change:true`.  All 36 checks and all 81 registered mutations pass,
and the capped primary is still rendered.  The discriminator therefore uses
raw role-count change as a substitute for the pinned point-free split.

This is a reproducible semantic hard-kill survivor.  Stage B is refused.

## 3. Outcome and scope

The directly forced earliest rung is

```text
P13-SUPPORT-CHANGE-UNPROVEN
```

The first report also identifies a possible
`P13-REFERENT-PRESENTATION-ONLY` reading.  That stronger demotion is not
adopted here: the counterexample directly proves that the support-change
discriminator is insufficient, while it does not by itself refute the entire
typed zero-pattern presentation arena or every source-groupoid transport.
The forward repair must nevertheless ensure that coextensive child syntax
cannot acquire a distinct physical support identity.

Nothing in this attack refutes the exact Cayley arithmetic, the native
negative-`K` nondivision certificate, the history-conditioned scope control,
the finite continuation-grammar algebra, the reciprocal joint, or the
matching-family calculations.  Those rows remain provisional and uncitable:
the authoritative construction has not passed its source audit.

This is an ordinary semantic-verifier failure.  It is not evidence against
Barandes-style indivisibility, does not imply configuration incompleteness,
and authorizes no metric, curvature, gravity, GR, or other successor work.

## 4. Forward-only authorization

A repair is authorized only after a separate result-neutral repair pin is
committed.  That pin must require, before any source edit:

1. an exact split-fiber certificate: every parent-satisfying source cell has
   exactly two target preimages under child forgetting, differing only in the
   child bit; every nonsatisfying cell has exactly one;
2. the exact cell-count identity
   `|cells(target)| = |cells(source)| + |cells(source satisfying P)|`;
3. properness of the new child inside the parent, so both `P and N` and
   `P and not N` are nonzero whenever `P` is nonzero;
4. recomputation of those facts from literal source/target contexts in the
   referent census, support gate, groupoid transport, and classifier-consumed
   lineage—never from role count, labels, or supplied booleans;
5. a registered `TAUTOLOGICAL-CHILD` changed-source attack with the exact
   survivor above, plus a native coextensive-child changed-object attack;
6. failure or demotion at `P13-SUPPORT-CHANGE-UNPROVEN` when the split-fiber
   certificate is absent, even if forgetting recovers the source and a role
   was added;
7. no change to the law family, exposed arithmetic, outcome vocabulary,
   eligible ceiling, ontology walls, fresh protocol, or scientific scope.

The repair gets a new source hash and source-freeze note.  It may not rewrite
the #192 freeze note or either audit.  No `--generate-fresh` or official
`--run` mode may execute until the repaired source is committed, independently
reconstructed, and the exact survivor is killed for the registered reason.

The sole next authorized event is the forward repair pin.  Stage B, Paper 13
drafting, hostile scientific review, and all metric-or-later work remain
closed.
