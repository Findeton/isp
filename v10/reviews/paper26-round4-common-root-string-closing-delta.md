# Paper 26 round 4 — common-root string closing delta

**Frozen target:** `a1ba7c9` (`Align D37 note with common-root receipt`).
**Review mode:** two independent targeted lanes; audit only; no reviewer edits.
**Verdict:** `0B/0M/0m/0n` in both lanes.
**Promotion:** recommended at Paper 26's stated scope.

The delta was limited to the two findings frozen in
`paper26-round3-common-root-closing-delta.md`.

1. The D37 note now reports 158, not 140, K1 typed events.
2. The deleted same-line chain/comparability account is replaced by the
   implemented canonical common-root sibling structure and the commuting-child
   coherence product without a transaction order.

No live Paper 26, D37 or README text retains the superseded account.  Remaining
mentions occur only in frozen reviews or dated ledger entries describing prior
commits and are historically scoped.

The executable and stored receipt are unchanged.  Fresh deterministic and
random-hash replays remain byte-identical and return `PASS 9/9`:

```text
source    b15e577bfdf03e1bc78628d9d934bab1e604da9f4b62f7c6372fa61dca7fcbd9
stdout    df5aa182d432206642ed3440d8d0b7f4cc9e971bd2d014811b9fea9e47391c16
science   82a2dac6a1f9c5352ea05309b1ae24f38098924c5be595f5b6dfb49960fdf126
complete  20d4b2f6add6db3296f221c184be539dd62c66ada81f32418b9288bebf778ed8
D36b      57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b
```

The independent Paper 26 stream therefore closes cleanly.  This review does
not broaden the result beyond a supplied typed opportunity carrier, finite K3/
K2/joint specification, countable locally finite pairwise-conflict completion,
finite D36b append adapter, unselected couplings and no quantum join.
