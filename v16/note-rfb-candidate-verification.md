# RFB Paper 10 post-commit candidate verification

**Frozen:** 2026-08-18, v16 ledger #135.

**Status:** VERIFIED GREEN-UNREVIEWED CANDIDATE — HOSTILE PANEL,
ADJUDICATION, AND TERMINAL PROMOTION REMAIN OUTSTANDING.

## 1. Committed target

Commit `a2cceab` freezes the candidate chain:

| object | SHA-256 |
|---|---|
| `v16/code/rfb_core.py` | `7d0a787d108ac16229dc6819a81f74f7b80203eaefa71d28f30f1f31b27e9ada` |
| `v16/code/rfb_fixture.json` | `f3557b3400584d01984c6a4f38d40744c9e2cf2f0e36c7c4aa225b045e5bd362` |
| `v16/code/rfb_score.py` | `4a2c9590e1d64f9e40c6e5828d132b9b746aa8938e18aee95a484caabc8c87ff` |
| `v16/code/rfb_output.txt` | `a7ebef77a507bac62c64fa594ed539902ed7a333fe5c77a677a4aad1f124aace` |
| `v16/code/rfb_receipt.json` | `e8cefe5b28d343fe76fdad89283a02c8c2f477243bbc7455b83324a0fe7a4659` |
| `v16/paper-10-record-feedback-boundary.md` | `360b4e861add1a5eac0b09296fe0e52438787697aa22097801f0e43cc2c2a5f4` |

No committed candidate byte moved during this verification event.

## 2. Fresh generation and integrity

A fresh post-commit invocation writes to an isolated temporary directory and
reproduces transcript, receipt, and paper byte-for-byte. The scorer passes all
forty-nine ordered gates. Its receipt content seal, transcript gate multiset,
paper claim tables, positive scope sentences, exactness registry, source
digests, and live read set all reproduce.

All thirty-nine registered mutants were rerun after the commit. Each refuses
at its preassigned named gate, and no mutant produces an output, receipt, or
paper. Self-test and unknown-argument behavior pass. A separately copied tree
with no `.git`, executed from `/private/tmp`, reproduces all three official
artifacts. Deleting the pin anchor from another isolated copy causes refusal
before artifact creation.

## 3. Independent exact reconstruction

A separate rational/combinatorial implementation importing neither scorer nor
core reconstructs:

- writer triples `(q, all reversible, full cycles)` as `(2,2,1)`, `(3,6,2)`,
  and `(4,24,6)`;
- reader triples `(q, general, additive)` as `(2,2,2)`, `(3,9,3)`, and
  `(4,64,4)`;
- constructive/destructive coherent port pairs as `(1,0)` and `(0,1)`, while
  their exclusive diagonal control remains equal;
- the mode plus probabilities `1/2`, `4/5`, and `1`; and
- predictive quotient sizes `1` for zero charge and `3` for unit charge
  through the held-out horizon.

Those independently computed values agree exactly with the sealed receipt.

## 4. Scientific status

The verification supports the candidate's scoped primary
**RFB-FORCING-BOUNDARY-MAPPED** and its simultaneous microscopic and
representational `METHOD-INCONCLUSIVE` coordinates. It does not independently
establish the continuous-phase extension, long-time hybrid dynamics, absolute
record permanence, changing-factorization no-signalling, a graph-generated
law, geometry, QFT, or GR.

The next authorized procedural object is a result-neutral three-lens hostile
protocol. This note assigns no reviewers and licenses no adjudication or
repair.
