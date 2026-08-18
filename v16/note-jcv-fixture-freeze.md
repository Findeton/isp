# JCV physical fixture and scorer freeze

Status: **FIXTURE-AND-SCORER-FROZEN-BEFORE-FIRST-EXECUTION**.

Prefixture commit:
`999a5311e599fb223ac9192991d20386b3ce6ab4`.

Frozen paths:

- `v16/code/jcv_fixture.json`, SHA-256
  `ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b`;
- `v16/code/jcv_score.py`, SHA-256
  `768c4bbc6b0e39436a6d6b7dcf026149f95c2e8bb931d080052262638827f692`.

The scorer has not been imported or executed.  Static parsing found valid JSON,
valid Python syntax, zero floating-point literals, and zero top-level call
expressions.  Both model `expected` fields are empty.  The physical output,
receipt, and paper paths are absent.

## Frozen content

The fixture contains the shared-law model from the PIN and one
independently-weighted-triangle control.  The scorer eliminates raw chart-sign
gauge to the four holonomy variables, then sends the quotient polynomial
systems to the already frozen generic solver.  It separately checks the raw
intertwiners over `Q(sqrt(2))`, raw-to-quotient defect identities, chart-gauge
orbits, exact rational real witnesses, all-input trace preservation, the
homogeneity control, classifier reachability, claim walls, read closure,
transcript equality, and total seals.

The scorer contains all seven registered outcome words and their decision
table, but no expected physical sector count, dimension, witness value, or
verdict.  Fifteen named mutants are frozen.  Normal execution is single-shot:
it refuses if any result artifact already exists; `--replay` is the separately
typed no-write reproduction mode.

The only authorized next action is one official execution from the committed
bytes, followed by commit-as-is.  No source or fixture repair is authorized
after truth is visible and before those result bytes are committed.
