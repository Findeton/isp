# QSF generic public-core freeze

**Frozen:** 2026-08-18, v16 ledger #113.

This event freezes the generic exact assay before it may read the WRC fixture,
carrier, targets, or verdict. It is calibration evidence only; no QSF physical
outcome exists here.

## Frozen artifacts

| artifact | SHA-256 |
|---|---|
| `v16/code/qsf_core.py` | `6dd6b4999c0474a362f56bb70271845fb5f322c6676a4de90c79b64ce753736f` |
| `v16/code/qsf_public_output.txt` | `a16b7d6026dc4d19c7659d17732890eea005e608b7389b0e8c064aef83fe77cf` |
| `v16/code/qsf_public_receipt.json` | `4252153f56b6ad12102eaba218aa8a4e29fe956c83d923796c9d3814f3dffac4` |

Arithmetic is exact in `Q(omega)`, with `omega^2 + omega + 1 = 0`.
The receipt seals payload, source, and transcript hashes.

## Public gates

Eight of eight public calibrations pass:

1. the exact Eisenstein field relation;
2. complete rank-one measure-and-prepare instruments;
3. an exact HJW Z/X ensemble pair with one density operator;
4. nonaffinity of probability-times-input-state versus affinity of a fixed
   output completion;
5. decomposition sensitivity of sequential nondemolition readout versus the
   affine projective control;
6. the history-grain split: discard can be affine while retained records and
   record-controlled continuation are nonaffine;
7. a finite predictive-partition positive and negative control; and
8. runtime exactness plus the artifact payload seal.

All eight independently targeted mutants refuse before artifact write:
`field-relation`, `instrument-drop`, `hjw-state`, `nonlinear-flag`,
`history-feedback`, `partition-merge`, `exactness`, and `payload-seal`.
`--selftest`, syntax compilation, no-overwrite behavior, and unknown-argument
refusal pass.

## What this freezes—and what it does not

The core establishes only that the registered assay can distinguish:

```text
AFFINE INSTRUMENT / LITERAL NONDEMOLITION RULE / INTERNAL-LABEL DISCARD /
DURABLE-LABEL RETENTION / LABEL-CONTROLLED FUTURE / PREDICTIVE QUOTIENT.
```

It contains no WRC dimension, walk matrix, record map, observable target,
expected verdict, or physical fixture. In particular, it does not yet show
that WRC signals, admits an affine packet-preserving completion, or has a
lawful indivisible history boundary. Those are separately frozen physical
assays after this commit.
