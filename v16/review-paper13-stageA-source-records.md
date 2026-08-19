# Paper 13 Stage-A independent terminal audit

Verdict: **NO-GO FOR STAGE B**  
Earliest corrected scientific rung: **`P13-SUPPORT-CHANGE-UNPROVEN`**

## Authentication

- Frozen source commit:
  `e203f72939ba1589c8c684f96d8d41777af209e3`
- Frozen evaluator SHA-256:
  `c699fc0316295e230c2cd0ef50601f631b195ad2237bebc2c42a75a2163f1aaf`
- Freeze-note SHA-256:
  `d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5`
- Construction-pin SHA-256:
  `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35`
- Mutant source:
  `/private/tmp/p13_stageA_audit_e203f729/context_replace_mutant.py`
- Mutant source SHA-256:
  `a6cd95e0eb5c917fa3ad2f93441a2f56d9ec69e4f3801ec551dacdfdef4c5668`

The mutant was made from the authenticated frozen source. No evaluator
function was imported and no other verifier or report was read.

## Exact changed source

The only semantic change is inside `context_extend`. The frozen source retains
every parent cell and additionally creates the child-labelled part:

```python
for cell in context.cells:
    cells.append(cell)
    if formula_evaluate(parent, cell):
        cells.append(tuple(sorted(cell + (child.name,))))
```

The mutant instead replaces every satisfying cell by its child-labelled cell:

```python
for cell in context.cells:
    if formula_evaluate(parent, cell):
        cells.append(tuple(sorted(cell + (child.name,))))
    else:
        cells.append(cell)
```

Thus forgetting the child still recovers the old context, and a role is added,
but no parent cell is split: the satisfying parent cell is not retained.

## Exact replay

- Command mode: permitted Stage-A `--selftest`
- Exit code: `0`
- Stdout:
  `/private/tmp/p13_stageA_audit_e203f729/context_replace_mutant_selftest.json`
- Stdout size: `17,098,516` bytes
- Stdout SHA-256:
  `c5dbfe91701e5dd6f5e73a63c818448fa28d01c386f4a2ecc2dfdb0f5b8c28bc`
- Normalized payload SHA-256, observed and independently recomputed:
  `279bb73a94beca773a998cbf4bb4e6e52cebf3effec89e51d467d414157b7046`
- Self-test checks: `36/36 PASS`
- Registered mutations: `81/81 KILLED`
- Mutation-registry SHA-256:
  `1607b2888b2d25eacedf0fa1f0f1e6ce927937abd6aca915165a6de697a3c077`
- All check evidence hashes independently recompute: `true`
- All mutation evidence hashes independently recompute and every registered
  old/new object differs: `true`

The two reported support branches both have:

```text
source_role_count = 1
target_role_count = 2
source_cell_count = 2
target_cell_count = 2
inverse_merge_exact = true
configuration_nonisomorphic = true
```

Nevertheless the evaluator reports:

```text
all_inverse_merge = true
all_support_changed = true
gates.variable_carrier = true
gates.support_change = true
strict_primary = P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED
```

## Disposition

This is a genuine hard-kill survivor. The pin defines horizontal extension as
a split of every parent-satisfying nonzero cell. The mutant performs replacement,
not splitting, but survives because the current discriminator asks only that
`(role_count, cell_count)` change as a pair and that forgetting the child recover
the source. Adding a role makes that pair unequal even when the number of cells
does not increase and the parent cell disappears.

The result does not force `P13-FIXED-CARRIER-ONLY`: a new role is present. What
it defeats is the proof that the new role realizes the registered lawful split.
The earliest substantive outcome is therefore
`P13-SUPPORT-CHANGE-UNPROVEN`.

Under the frozen stopping rule, the source cannot be repaired in this cycle.
Stage B must not proceed from these bytes.
