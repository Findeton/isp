# WRC generic exact core freeze

Status: **GENERIC CORE FROZEN BEFORE PHYSICAL FIXTURE**.

Ledger event: v16 #79. Immutable Paper 8 pin commit: `97b02b3`.

The following public artifacts are frozen before any WRC physical fixture,
scorer, official result, receipt, or Paper 8 candidate exists:

| artifact | SHA-256 |
|---|---|
| `v16/code/wrc_core.py` | `94c74731179c1302254a3b7424dcb66d1154518bcf936c5531b05a52f42fa6b3` |
| `v16/code/wrc_public_output.txt` | `6e0932a22f44ee3163f5d17444fc367887962d852c081ba3132a8dbcd1359018` |
| `v16/code/wrc_public_receipt.json` | `32852f6ca29e4e6a4988e3bd5b3fac543c6fae8f389fb8262d1c042ca590ad2b` |

The self-contained core contains no WRC site, carrier dimension, link set,
Grover entry, committed record, horizon, observable, coupling target, outcome
word, comparator, or Paper 8 prose. It implements:

- exact rational Eisenstein arithmetic `Q(w)` with `w^2+w+1=0`;
- exact vectors, density matrices, adjoints, products, traces, effects,
  projectors, permutations, unitary conjugation, and Born probabilities;
- Kraus operations, all-input instrument completeness, the literal
  `Tr(E rho) U rho U^dagger` outcome operation, affine mixtures, and exact
  matrix comparison;
- finite event histograms and generic covariance actions; and
- deterministic canonical JSON, gate-time component seals, atomic writes,
  strict CLI, existing-target refusal, selftest, and public mutants.

Eight constructor-stated public gates pass. They verify the cyclotomic
relation, three exact unitaries, a complete two-port projective instrument,
the exact `9/25,16/25` Born control, a nonzero mixture-affinity defect
`diag(-1/4,1/4)`, an equal-trace CP comparison with a different conditioned
matrix, simultaneous state/effect covariance under a swap, and the computed
histogram `(1,1,2)`. These are generic calibrations, not WRC's walk fixture or
registered result.

Two fresh executions reproduce both public artifacts byte-for-byte. An
execution from alien CWD `/private/tmp` does the same. `--selftest` and all six
public mutants exit nonzero without writing artifacts or emitting tracebacks;
an unknown option exits `2`; existing official targets refuse before
evaluation. Static AST inspection finds zero Python float literals.

At this freeze the following later paths are absent:

```text
v16/code/wrc_fixture.json
v16/code/wrc_score.py
v16/note-wrc-fixture-freeze.md
v16/code/wrc_output.txt
v16/code/wrc_receipt.json
v16/paper-08-walk-reconstruction.md
v16/note-wrc-candidate-verification.md
v16/note-wrc-hostile-protocol.md
```

The next authorized stage is a data-only physical fixture and verdict-neutral
scorer, both frozen before first official execution. This generic core may not
change after the core-freeze commit. In-flight review reports and the unrelated
untracked v15 SCOUT-T files remain outside WRC's runtime and staging sets.
