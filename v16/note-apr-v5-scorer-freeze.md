# APR Paper 12 — v5 scorer source freeze

**Date:** 2026-08-19

**Status:** FINAL SCORER BYTES FROZEN BEFORE ANY V5 FIXTURE EVALUATION

**Binding pin:** `v16/note-apr-v5-executable-law-weld-pin.md`

**Pin commit:** `f15d96e8f35d896292c6e2cf9f2912d63ded7db7`

**Pin SHA-256:**
`c20217d263bbbac9d6f2dc94ad1f51938ef3b283c6401c01c6c17e5ed6ccc5e6`

## 1. Frozen scorer bytes

The only scientific-program source changed after the pin commit is:

```text
v16/code/apr_score.py
SHA-256 c2a9f467d5f2403021634c4b056b63769b5a0e8003fff8e472d5f2a1236ec205
19,368 lines
757,632 bytes
diff against #177: +5,377 / -7
```

`v16/code/apr_core.py` remains
`cd51fd36bc26701fdc649ee81f4b048dadde03e645860a7b885c501e2e180ca9`.
`v16/code/apr_fixtures.py` remains
`0698d5d413384e43108241a15eb7134fda82deec8bffdc4413edb2c5ea2742bc`.
No fixture, protocol, law, outcome vocabulary, precedence, ontology ceiling,
or prior artifact changed.

The final source is now immutable. Any later scorer-byte change invalidates
this freeze. After this source and note commit, a confirmed semantic
counterexample terminalizes APR under the v5 pin; no v5b/v6 scorer repair is
authorized.

## 2. Disclosed development testing

Fixture-free development self-tests ran while the scorer was being written.
They were advisory, were never pre-truth, and did not import or evaluate the
APR fixture. No `--run`, `--mutant`, `--mutants-all`, `load_frozen_fixture`,
official artifact path, or scientific receipt path was invoked.

The permanent inherited disclosure remains:

```text
RESULT-KNOWN-BEFORE-V5-IMPLEMENTATION
```

V5 is a final verifier-plumbing repair. Its synthetic executable laws are not
APR physics and cannot enter the scientific output or receipt.

## 3. Final-byte repository and off-tree replay

After the scorer SHA above was declared and edits stopped, the exact final
bytes were run in both the repository and a true off-tree/no-`.git` directory
containing only authenticated `apr_score.py` and `apr_core.py`.

Both runs returned zero and emitted byte-identical canonical stdout:

```text
schema                         apr-generic-selftest-v5
status                         PASS
check_count                    47
registered_attack_count        24
scientific_fixture_evaluated   false
fixture_import_attempts         []
fixture_import_denial_active    true
scorer_source_sha256            c2a9f467d5f2403021634c4b056b63769b5a0e8003fff8e472d5f2a1236ec205
semantic_witness_sha256         4256f6db060acc7fa2aec4b10cf8674029ab4f92fb9cb08d0345f978d336f1de
stdout bytes                    14,791,639
stdout SHA-256                  17c636328cf25de41a1abb3444bab26755fdbfb287f5470d7df40d5599dd1cec
```

The machine-reconstructible payload includes complete primitive bundles,
typed occurrence and backward-slice DAGs, carrier traces, `P_i` and `r_i`,
global-to-regional restrictions, the post-rewrite reader path, exact
Gaussian-rational quantum witnesses, every residual, and every attack object.
The parity-global same-shadow family remains an explicit scientific non-kill.

The registered attacks are:

```text
RESET-ONE
NONINVOLUTIVE
STALE-CACHE
CLONE-ID
SEVER-OCCURRENCE
ZERO-SLICE
CANCELLED-LOOP
CARRIER-ONLY
RESTRICTION-CACHE
REMOVE-BRIDGE
LABEL-ONLY-JOINT
ALIEN-CARRIER
ISOMORPHIC-DISCONNECT
DUPLICATE-ID
BRANCH-SUM-ONLY
ONE-COLUMN-TENSOR
SINGLE-INPUT-READER
HIDDEN-ERASER
CALIBRATION-BYPASS
CONTACT-IDENTITY
MOVE-DOWNSTREAM
CONJUGATION-SOURCE
HISTORY-TRANSPOSE
Z-TRANSPOSE
```

## 4. Real changed-source attacks

Three private off-tree copies changed exactly one marked final-source
operation. Each changed copy returned nonzero and refused the synthetic
positive at `gate:quantum`; neither candidate could earn
`HORIZONTAL-QUANTUM` or the joint primary.

```text
attack                changed-source SHA-256
CONJUGATION-SOURCE    94607cbcdd2e69033137ae7862ab1a3a19e4fa340a73e3869202c548545ae8fb
HISTORY-TRANSPOSE     4de9dd6f5b0917a1f0e7467da7495a2710d3628d53607197a9b0f2038ddba96d
Z-TRANSPOSE           39602662ff0612e5640dbfcb62d3c8273801bdd5704f0a51aa63a677afef6c38
```

The original source remained byte-identical throughout. The changed copies
are private test objects, not repository inputs or scientific evidence.

## 5. Static and publication boundary

- Python AST parsing passes.
- `git diff --check` passes.
- one public `classify_primitive_law` and one `ExecutableLaw` definition exist;
- the only added `apr_fixtures` reference is the deliberate self-test denial
  guard;
- no v5 artifact path is embedded in the scorer;
- `v16/apr_output_v5.txt` and `v16/apr_receipt_v5.json` were absent at freeze;
- the frozen v4 output and receipt remain respectively
  `68374ea18576466ccc40553f8b221360fdfce3fc43d5b555a6eeb0d2827a2f56`
  and
  `ab9ea941fceebf5b57c7955d483730f3a5f0b317bb5a21da9cc0820331919a61`.

The next authorized event, only after this source and freeze note are
committed, is one transactional official run to the two absent v5 paths. Its
scientific output and receipt content must be byte-identical to v4. New v5
provenance remains in this note and independent verifier reports, never in the
scientific receipt. Candidate drafting and the scientific panel remain blocked
until two independent post-freeze reconstructions are green.

## 6. Ontology and law-type wall

This freeze certifies no physical law. The immediate v4 defects were ordinary
one-law typing/dataflow failures. The deeper ISP debt remains one indivisible
stochastic law of transition probabilities between complete relational
configurations, conditioned at admissible division events/times, from which
regional shadows, instruments, records, comparisons, and relational rewrites
are derived. V5 supplies only synthetic verifier controls and cannot promote
its finite `ExecutableLaw` into that missing `Gamma`.
