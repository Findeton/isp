# RFB generic exact core freeze

**Frozen:** 2026-08-18, v16 ledger #131.

**Status:** PUBLIC CORE FROZEN — NO PHYSICAL FIXTURE, SCORER, RESULT, OR
PAPER 10 CANDIDATE EXISTS AT THIS EVENT.

## 1. Frozen objects

| object | SHA-256 |
|---|---|
| `v16/code/rfb_core.py` | `7d0a787d108ac16229dc6819a81f74f7b80203eaefa71d28f30f1f31b27e9ada` |
| `v16/code/rfb_public_output.txt` | `4988daa3ca88f52af279d0491d5dd56ac2724f79f998e75f7a0c91ddceb28b2e` |
| `v16/code/rfb_public_receipt.json` | `7356ae0f309645eaee9e6202e8cc61a4f0e231e087c3c3f6104cb6f6cac6ad11` |

The receipt's internal content digest is
`298fd5631d4e6c2ef433900de056dcc4f6c304a3a584b27e284bd6799388dc38`.
Its source and transcript seals reproduce the first two hashes above.

## 2. Public content and deliberate abstention

The core supplies exact reusable machinery only:

- reversible full-cycle writers and conjugacy to a cyclic shift;
- vertex-phase gauge and the cycle-product exponent;
- additive reader classification and writer/reader relabeling orbits;
- strongly positive two-history port functionals and their exclusive-kernel
  control;
- exact partial tags, predictive partitions, and fixed-factor local channels.

It does not contain an ISP graph, RFB assumption row, expected physical
measurement, verdict word, candidate ontology selection, or Paper 10 prose.
The public calibrations use an order-five algebra where useful and therefore
cannot encode the registered `q=2,3,4` fixture answers by a typed table.

## 3. Verification

The official public invocation passes all nine gates. Eleven targeted mutants
each refuse before producing either artifact:

```text
cycle-classifier
phase-gauge
reader-composition
pair-orbit
history-interference
history-positivity
hybrid-normalization
predictive-partition
locality
exactness
payload-seal
```

`--selftest`, gate and mutant enumeration, unknown-argument refusal,
same-target refusal, and existing-target refusal pass. A byte-for-byte copy of
the core run from `/private/tmp` with no repository and no `.git` produces the
same transcript and a JSON-identical receipt. The transcript's complete gate
rows are compared in both directions with the receipt ledger before promotion;
the receipt content seal is recomputed after all source/transcript keys exist.

## 4. Scope and next immutable event

These calibrations establish only that the instrument can recognize the
registered kinds of algebra. They select no record-feedback law and make no
claim that a stochastic rewrite kernel, an enriched-state kernel, an
indivisible process, or a decoherence functional is fundamental.

The next event may freeze the result-neutral RFB fixture. The core bytes and
their three hashes are then anchors; changing them requires a disclosed new
freeze and invalidates any later scorer hash. The physical scorer may not run
until both fixture and scorer have been separately committed.
