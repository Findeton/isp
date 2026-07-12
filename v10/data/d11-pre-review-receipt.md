# D11 pre-review receipt

**Date:** 2026-07-11  
**Status:** **SUPERSEDED BY ROUND-1 REPAIRS.** This file preserves the exact
pre-review state for audit only. Do not use its hashes, influence counts, or
verdict as the final D11 result; see `d11-final-receipt.md` once review closes.

## Reproduction

Exact engine:

```text
python3 v10/code/d11_complete_bloch_lorentz_exact.py
python3 -O v10/code/d11_complete_bloch_lorentz_exact.py
```

Both outputs are byte-identical:

```text
stdout sha256 be58dff995e1103e08236d735370bf996e9cbd81de071d0d8e3bbd2e31b807be
checks 65
cutoff3_histories 117
depth12_orbit 113
depth12_support 0.914143429015
receipt_sha256 64cbb0bd2691713145f8679211d01dda023b78f9f5b32d64e146c08ad3ff9de8
```

Numerical campaign:

```text
/Users/felixrobles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  v10/code/d11_generated_history_geometry.py
```

Deterministic stdout SHA-256:

```text
3107fb0719a3de929fee1de3fdc086ebf535a56bf9e11d84e3cf49143a8295a7
```

## Exact gates

```text
dual_sl2c_born_gauge PASS
split_join_seal_instruments PASS
typed_complete_next_history_kernel PASS
construction_order_gauge PASS_AT_ENUMERATED_SCOPE
ancestry_subset_positive_cone PASS
naive_join_negative_control FIRED
pairwise_positivity_equals_influence FALSE
cone_containment_is_construction_theorem YES
equal_activity_population A_S_EXTINCTION_THEOREM
```

## Frozen numerical result

```text
cutoff  reached  terminal  median_clicks  max_clicks  join_influence  rank4
512     0/24     24/24     1              49          3/24            3/24
1024    0/24     24/24     3              171         9/24            5/24
2048    0/24     24/24     1              47          5/24            4/24

ancestry edge violations 0
influence cone violations 0
median support -1.0000, -0.8515625, -1.0000
valid generated F_dom 1,3,1
valid generated F_m4 1,0,0
M4 controls under m4 axis 24/24 at each rung
M4 mean 1.085537373230, 1.079347373771, 1.078453579417
M4 controls under dom axis 0/24 at each rung
numerical verdict INTERACTION-INERT
receipt_sha256 f073ed07f712c0d578dcd360ccf312be49129428beac20cf9c6bab8e142888e0
```

All 72 histories terminate before their nominal cutoff. No survivor
conditioning or parameter sweep is used.

## Artifact hashes

```text
728775ae57c90f6737ee1655933ec43ff29cf1f11003f521e5f087bc42b8fd08  code/d11_complete_bloch_lorentz_exact.py
04d529f3ae790bf8bb39ad52d4c653fa450cb5841bd408524f853da8d116ccd0  code/d11_generated_history_geometry.py
3679e66ef46eb554c7723b19cf5e1e81fc24798be4a8567b473d728c11f99940  note-d11-complete-bloch-lorentz-scir-protocol.md
af87777d63cb929e744bbee4ce04c60e36facf4b84c2ee4af92014d59fc12634  note-d11-complete-bloch-lorentz-scir-investigation.md
8e32c4d226ba4b5bd4675f852c0e5b829a0f558a6a5431a6d7096d084058d599  note-d11-literature-audit-complete-packet-and-extinction.md
ff7bd46237eb0a4e58365c264219c49ac7a230c8a6ff5824a042eb38d0915ff5  relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md
```

## Pre-review verdict

```text
COMPLETE-KINEMATICS/INFLUENCE-ENVELOPE-OPEN
```

The numerical protocol's label is `INTERACTION-INERT`; the more precise
mechanism is local-interaction-capable but population-extinct. The proposed
`SEAL -> COMMIT` successor-carrier repair is a next-investigation hypothesis,
not part of this result.
