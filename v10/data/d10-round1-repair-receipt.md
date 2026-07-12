# D10 round-1 repair receipt

**Frozen for round-2 review:** 2026-07-11.

## Review verdicts repaired

All round-1 streams returned `MAJOR REVISION` while preserving the central
qubit/Lorentz theorem and primary `KINEMATICS-ONLY` ceiling.

```text
9f494342cde8dd803282e0ffb4551699fe29aaa34a619a0752880b94eb517301  d10-round1-mathematics-hostile-review.md
74eb63c65c609213db3d3a858b470b42999d6d70c7d083f2425445fc0fcc90dd  d10-round1-ontology-locality-hostile-review.md
35dc1d09c06f94ab87a69863c7c29dbda0d9843f79d7de6f9e45998bdd26de8a  d10-round1-independent-rebuild-hostile-review.md
ed9340af3900c32110084d76e34719923fcafb8cdae8e9693bcd922366b70d1e  d10-pre-review-receipt.md
```

Every disposition is listed in
`v10/note-d10-round1-opening-repairs.md`.

## Repaired reproducibility audit

```text
D10 REPRODUCIBILITY AUDIT
scripts=3
normal_optimized=BYTE_IDENTICAL
frozen_stdout_hashes=PASS
d10_bloch_lorentz_exact.py bytes=4750 stdout_sha256=a05b84aa0a94a4a3086c190045fc56e96eb0fde6a00c179073a23944bbebcd5f
d10_finite_clock_convergence.py bytes=7470 stdout_sha256=f2e8c45e1a224e4f84ebfdd5a11e9973266879723443508d9f04539fdaa3be27
d10_relational_scir_packet.py bytes=3294 stdout_sha256=b5827de1d703ab492563fb1b981a41da477a1627943215ffe4ce660d0feb65eb
audit_sha256=f8c409191f05ee830a6422428517860e1961311b98c6f3b6be1dc5c505e6b596
```

The repaired scripts freeze `EXPECTED_CHECKS` at `109`, `99`, and `43` and
fail if either count or stdout hash moves.

## Repaired artifact hashes

```text
fe91dfeb1e95d04b813f59b59c47443df246b8e74ad579ef263796df511ff494  v10/note-d10-round1-opening-repairs.md
0b9040cc8e6d6608b169ed5ff11c290b32768ebbce1fb964c0fb694956a36c88  v10/code/d10_bloch_lorentz_exact.py
595ca56dce92052f0db0ecc3fe28252e2b467dd1eb28b55aead26aa0848650d3  v10/code/d10_finite_clock_convergence.py
09e68cb09301a1706b65f2742f3eb0fb5e4f5a5468bd69b1893374a5d1c1d856  v10/code/d10_relational_scir_packet.py
ed9cf8089f61dc777be4dc436f5df41a30cd4f764e0617a975a0d2e667439d90  v10/code/d10_reproducibility_audit.py
bccb87ca0b05c8882052a388e85974c40ae6dd89fc9a056bc93208686e908942  v10/note-d10-bloch-celestial-investigation.md
1a41f3848095ea524c06035af74c08450108f5d822aa9e73093af290150824ba  v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
743b8d93c3baad99981db20e3133cdf36b4fe58486584161205609b4ec5381db  v10/code/v10_self_containment_audit.py
```

## Repaired scope submitted to round 2

```text
CONDITIONAL-COMPLEX-QUBIT/LORENTZ-CONE-ISOMORPHISM
+ FOUR-FACTOR-DIRECTIONAL-POSITIVE-EVALUATIONS
+ FINITE-OUTER-CONE-APPROXIMATIONS
+ FINITE-ALPHABET/FINITE-DEPTH-PROJECTOR-REFINEMENT
+ CHOSEN-PACKET-SEAL/SCHEDULE/FOREST-INTERVENTION-TESTS
+ SUPPLIED-SU2-CONNECTION-GAUGE-COVARIANCE
- COMPLEX/LOCAL-TOMOGRAPHY-SELECTION-NOT-DERIVED
- NORMALIZED-QUBIT-TIME/SCALE-MAP-NOT-DERIVED
- PHYSICAL-LINK/SEAL/CAPACITY-NOT-DERIVED
- FULL-SL2C-BORN-GAUGE-OPEN
- JOINING/ORDER/SPACETIME-INFLUENCE-LINK-OPEN
= KINEMATICS-ONLY
```
