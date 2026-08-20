# Paper 14 premetric official-result verification

Date: 2026-08-20

Status: **STAGE C GREEN-UNREVIEWED / HOSTILE REVIEW REQUIRED**

## 1. Frozen authority and chronology

The result-neutral pin is committed at
`9687d59c2faa29efd53993643deb92b3f5c5a025`.

The Stage B source freeze is committed at
`dda7a01e80a17883a039bd0e33a3453b0601af3f`:

```text
source  v16/code/p14_premetric_exact.py
SHA-256 1a1d9a7acc3ef4ba62a9e9b0f6101263dde3b72dd9d407918ea0be653d5d628e

paper   v16/paper-14-stable-happenings-and-premetric-order.md
SHA-256 ffc3dca2863bf9f36c9fe62e8dff80628c59c8837b3d96006e449329dee05ec1

note    v16/note-paper14-premetric-construction.md
SHA-256 e6d59fd49e5af805df96f8b3a4c2db5676dafaa3c552ecadb0779ca690887253
```

No fresh-case content existed before that commit. At
`2026-08-20T17:12:43Z`, one and only one `openssl rand -hex 32` invocation
generated the nonce

```text
f1e235c9c6b8ae75335fbfac95492857d0dd356d880b2231a3ab976f0b2a3439
```

There was no reroll. The resulting fresh file binds the frozen source and
contains six unique cases across all six preregistered generic kinds.

## 2. Official artifacts

The frozen source was invoked once in publication mode. It completed in
9.16 seconds, below the 60-second cap, and wrote the two absent destinations
transactionally.

```text
v16/p14_premetric_fresh_cases.json
SHA-256 4f5d8d21bb66d5e7c41a9c34a35a26ec955b03497d9682564efd23df681126c7
1,535 bytes

v16/p14_premetric_output.json
SHA-256 95a38ebbb6d2e9c85c2a2f66ca3275fd1f4205761dfcc5eae6a1d9ea2b233993
26,103 bytes

v16/p14_premetric_receipt.json
SHA-256 2d320edc0eb152d5fcb6ffdf1444e8071d9466c5773c13be51ad438036c2fa4c
29,695 bytes
```

The official normalized payload SHA-256 is
`292b9c9dad12785cdb0b233a7d56237500fd716e38b740ad3772a1f6969e8ecf`.
The receipt-core SHA-256 is
`0d71fd0eed5a2fe399fc7b6f9321c46c91b06e03c68f878dd626407175937914`.

## 3. Fresh controls

All six unseen cases pass their frozen semantic predicates:

| case | kind | exact result |
|---|---|---|
| `FRESH-FRONTIER-27-57` | frontier profiles | identical projected state carries distinct future profiles `2/7` and `5/7`; frontier incomplete |
| `FRESH-CORRELATED-ANTICHAIN-1234` | correlated antichain | weak path products both equal `1/10`, but strong local-factor descent fails |
| `FRESH-SCREENED-FORK-2535` | screened common cause | eight positive histories normalize and every conditional screening row is exact |
| `FRESH-FIXED-MEMORY-100-4-4` | fixed memory | 256 required histories exceed capacity 100 |
| `FRESH-PRESENTATION-PERMUTATION-3` | presentation permutation | raw order changes while the canonical multiset is identical |
| `FRESH-DEPENDENCY-BUNDLE-UV` | mutual dependence | `u` and `v` form one strongly connected bundle; `w` and `z` remain separate |

The fresh-result aggregate SHA-256 reconstructed independently is
`c47fc41ee44b1434e2e51d2b936863b7091e77eecd81012294f079bcd6e24abd`.

## 4. Independent no-import reconstruction

An independent verifier was written in private scratch after publication. It
does not import or execute the candidate source.

```text
/private/tmp/p14_premetric_independent_verify.py
SHA-256 076dece93991f410bf7a2d184f601b40077e7baaa06e91114bb6fe9fa27b5f6d

/private/tmp/p14_premetric_independent_verify_result.json
SHA-256 6602d819952fbb4a7ec38efb604f835bf2c4afcc627d5d47d77b9722089e75e8
```

It completed with 30 top-level exact assertions. Each assertion reconstructs
a complete object rather than trusting a published boolean. In particular it:

1. reserializes output and receipt into their canonical bytes;
2. recomputes the normalized payload and receipt-core hashes;
3. authenticates all five observed inputs and the output bytes;
4. recomputes all 17 scientific-key seals and all nine receipt-core seals;
5. reconstructs the exact writer maps, projectors, six record-preserving
   futures, orthogonality, completeness, and eraser exclusion;
6. independently enumerates the five-state/seven-word/five-trace minimal
   history and its three-bundle quotient;
7. reconstructs the 16-history reciprocal law, all four direct-versus-cut
   rows, hidden future profiles, and all four stability/frontier combinations;
8. reconstructs the correlated-antichain refusal and the screened-fork
   positive control;
9. independently generates the 12 unlabeled rooted-tree shape census rows and
   all 38 uniform finite-family rows;
10. reconstructs all six fresh controls from their raw parameters; and
11. reconstructs the complete old/new preimages, SHA-256 identities,
    dispositions, and evidence for H1--H26.

The independently reconstructed aggregate hashes are:

```text
measurements 962340352d502c8e5a8056c57dcb7df559543cef5741607b8863beb3c802d2f0
attacks      fd593caf97a61e3ee4572295dccd25e72c15eed13c08f87eed4819bf9c2ad23f
fresh        c47fc41ee44b1434e2e51d2b936863b7091e77eecd81012294f079bcd6e24abd
```

No mismatch or scientific survivor was found.

## 5. Exact scientific disposition

The official artifact reports:

```text
scientific checks:          16 / 16 PASS
registered attacks:         26 / 26 KILLED
fresh controls:              6 /  6 PASS
law provenance:             DECLARED-NEW-LAW-POSTULATE
official status:            ELIGIBLE-GREEN-UNREVIEWED
eligible coordinate:        P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
```

This coordinate is product-valued. It includes presentation-invariant stable
happening bundles, complete-frontier discrimination, an intrinsic locally
finite bundle order, unit interval measure, and unequal weights only where
the strong typed-diamond condition descends. A stable happening is not
silently promoted into a complete probabilistic checkpoint.

## 6. Ontology and successor wall

The result is relative to one declared new finite history law. It does not
select that law or an actuality map. `rho` remains an external actualization
postulate. The result constructs no chronology, causal cones, topology,
dimension, signature, scale, spatial volume, proper time, metric, connection,
curvature, stress-energy, entropy, gravity, GR, continuum, or QFT.

Accordingly this is **GREEN-UNREVIEWED**, not terminal acceptance. The next
authorized event is to freeze the result-neutral hostile-review protocol.
Paper 15 remains closed until a hostile panel and adjudication terminate this
Paper 14 cycle and explicitly open a successor pin.

The ordinary SHA-256 of this verification note is recorded after creation in
the ledger and status board; it is not self-embedded here.
