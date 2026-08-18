# QSF law-type regeneration — repaired candidate bytes

**Date:** 2026-08-18

**Source commit:** `92e9dca` (v16 ledger #127).

Two clean invocations of the #127 scorer pass `20/20` gates and produce
byte-identical artifacts. The primary and every exact scientific witness are
unchanged. The result typing and paper ontology now explicitly refuse a
microscopic one-step-kernel selection.

| artifact | SHA-256 |
|---|---|
| `v16/code/qsf_score.py` | `0fa04e8d4d9385edc64df8b2e7763753aed2ec5bfc063a716aa8f46515d86489` |
| `v16/code/qsf_output.txt` | `a110d5d6c21a3d5cc27109216bb299c08c5b77ee60c547ce7e63da53c9a27ed9` |
| `v16/code/qsf_receipt.json` | `70c4b63712aba053177ded4d2fabfe865371d16e42e2e6865f9cace4961a2d45` |
| `v16/paper-09-quantum-seam.md` | `f11fe9e124ed70181dc86422b6db528265599dc4dc9f5d56c31f295654677b71` |

The clean runtimes are `232.88` and `234.63` seconds, below the frozen
`360`-second ceiling. Terminal status is still withheld pending post-commit
clean replay, the complete 28-mutant no-write battery, and true off-tree/
no-`.git` execution.
