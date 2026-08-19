# Paper 13 Stage-A independent post-freeze audit — first blocker

Verdict: **REJECT FOR STAGE B / FRESH TAUTOLOGICAL-CHILD ATTACK SURVIVES**

## Authentication

- Frozen commit: `e203f72939ba1589c8c684f96d8d41777af209e3`
- Evaluator SHA-256:
  `c699fc0316295e230c2cd0ef50601f631b195ad2237bebc2c42a75a2163f1aaf`
- Freeze-note SHA-256:
  `d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5`
- Pin SHA-256:
  `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35`
- Canonical self-test independently replayed: 26,134,100 stdout bytes, SHA-256
  `a217f96d3d8bb92c214a4235ed7ac3e7a9c5a954557a01820176f489c778c6a2`,
  status `PASS`.

No evaluator function was imported.  No official fresh case was generated.

## Changed object

Off-tree mutant:
`/private/tmp/p13_mut_tautological.py`, SHA-256
`a6cd95e0eb5c917fa3ad2f93441a2f56d9ec69e4f3801ec551dacdfdef4c5668`.

The only scientific edit is in `context_extend`.  The frozen source performs
a genuine split:

```python
for cell in context.cells:
    cells.append(cell)
    if formula_evaluate(parent, cell):
        cells.append(tuple(sorted(cell + (child.name,))))
```

The mutant instead adds a child that is perfectly correlated with the parent:

```python
for cell in context.cells:
    if formula_evaluate(parent, cell):
        cells.append(tuple(sorted(cell + (child.name,))))
    else:
        cells.append(cell)
```

For the minimal base context with nonzero cells `()` and `(A)`, a lawful split
must produce three nonzero cells `()`, `(A)`, `(A,N)`.  The mutant produces
only `()` and `(A,N)`.  On every nonzero cell, `A=N`; extensionally they are
the same Boolean element.  The number of Boolean atoms remains two.  This is a
new role name, not new point-free support.

## Surviving false promotion

The mutant self-test returns all 36 checks `PASS` and strict primary
`P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED`.
Its deterministic stdout SHA-256 is, on two independent runs,
`c5dbfe91701e5dd6f5e73a63c818448fa28d01c386f4a2ecc2dfdb0f5b8c28bc`.

The emitted measurements disclose the defect while promoting it:

```text
source_role_count = 1
target_role_count = 2
source_cell_count = 2
target_cell_count = 2
all_inverse_merge = true
all_support_changed = true
coherent.support.created_cells = 2
```

The gate defines `configuration_nonisomorphic` only by inequality of
`(role_count,cell_count)`.  Therefore the new raw role name is sufficient to
pass even though no atom was split.  Neither the essential-support quotient,
source-groupoid gate, support gate, registered support mutants, nor outcome
classifier checks extensional distinctness of the new Boolean role or the
required increase in nonzero cells.

## Scientific consequence

This is exactly the pin's point-free no-smuggling boundary.  A context in which
the child equals its parent is presentation enlargement, not physical support
change.  The frozen verifier therefore cannot distinguish the advertised
horizontal relational rewrite from a duplicate Boolean name and can award the
relational-Gamma ceiling to a presentation-only construction.

The earliest affected scientific rung is no later than
`P13-SUPPORT-CHANGE-UNPROVEN`; because the claimed physical source quotient
also fails to identify coextensive roles, `P13-REFERENT-PRESENTATION-ONLY` is
the conservative ontology reading.  In either reading Stage B cannot proceed
under this frozen source.

This is the first fresh attack in the post-freeze sequence that produced a
reproducible semantic survivor.  Per the stopping rule, later attacks were not
used to dilute or repair it, and no patch is proposed under the same freeze.
