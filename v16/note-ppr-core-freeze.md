# PPR generic exact core freeze

Status: **FROZEN BEFORE PHYSICAL FIXTURE AND SCORER**.

Pin commit: `828b51077ed85d1158135244fb6ea010b6d26350`.

The generic source and its public calibration artifacts are frozen together:

| artifact | SHA-256 |
|---|---|
| `v16/code/ppr_core.py` | `490668340b08022ac5d11c8fdc07c392739153b609a72b9bda5bfcf112f472ea` |
| `v16/code/ppr_public_output.txt` | `f8198dd124c0f7aaa6c3459e43ff4c14e08aa9283e1286549ac0693fd5bf78fc` |
| `v16/code/ppr_public_receipt.json` | `1acf2d48c5ddf0ca5283f655dfda9fbe29952ca3ec18c47679d7215831992926` |

No `ppr_fixture.json`, `ppr_score.py`, official output, official receipt, or
Paper 3 file exists at this freeze. The module contains no PPR primary verdict
literal and no physical-fixture constructor.

## Public exact checks

The public CLI returns 9/9 gates:

1. calibration anchor;
2. multi-boundary continuation-stable null descent;
3. continuation congruence;
4. induced quotient map;
5. common-future pullback identity;
6. exhaustive two-element partition census separating durable, erasable, and
   coherent cases;
7. same unconditioned channel versus different record instrument;
8. history split/merge equality; and
9. graph relabelling.

The delayed-activation public control starts with constraint ranks
`cut=1,future=1`, stabilizes after one strict round at `cut=2,future=1`, leaves
only the third cut direction permanently null, and induces quotient map
`[[0,1]]`. The public pullback is exactly
`[[0,1,0],[-1,0,0]]`. The two-element partition census contains two
partitions: the identity continuation admits the two singleton record sectors,
whereas the rational eraser and coherent Gram control admit only the trivial
one-block partition.

The exact rational Kraus rotation preserves one unconditioned channel and
changes the outcome-resolved instrument. The public result therefore verifies
the term split without treating a Kraus rotation as a relational-history
automorphism.

## Robustness checks

- Two clean artifact-generating runs are byte-identical.
- `--selftest` confirms an anchor corruption dies before artifact construction.
- An unknown flag exits 2.
- Each public mutant exits 1:
  `anchor-corrupt`, `stable-drop-edge`, `pullback-transpose`,
  `partition-preplant`, `channel-shadow`, and `split-weight`.
- The receipt's seal manifest is total over every payload key existing before
  the manifest itself.
- Source compilation succeeds under `/opt/homebrew/bin/python3.13`.
- The substantive source contains no float literal, `float`, `numpy`,
  tolerance, or `isclose` path.

These are public calibration facts, not PPR physics results. The next permitted
event is the separate data-only physical fixture and verdict-neutral scorer
freeze. The generic source is byte-immutable for that first official fixture.
