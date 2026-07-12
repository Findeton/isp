# D10 pre-review receipt — Bloch–celestial selection investigation

**Frozen:** 2026-07-11, before independent hostile review.

## Primary verdict submitted for review

```text
EXACT-QUBIT-LORENTZ-BRIDGE
+ MANY-CLOCKS-FOUR-FACTORS
+ FINITE-RECORD-DIRECTION-REFINEMENT
+ RELATIONAL-SU2-DIAMOND-GAUGE
- COMPLEX-SELECTION-NOT-DERIVED
- NORMALIZED-QUBIT-HAS-NO-TIME-SCALE
- FULL-SL2C-GAUGE-OPEN
- ORDER-INFLUENCE-LINK-OPEN
= KINEMATICS-ONLY
```

## Reproduction

```bash
python3 v10/code/d10_bloch_lorentz_exact.py
python3 -O v10/code/d10_bloch_lorentz_exact.py
python3 v10/code/d10_finite_clock_convergence.py
python3 -O v10/code/d10_finite_clock_convergence.py
python3 v10/code/d10_relational_scir_packet.py
python3 -O v10/code/d10_relational_scir_packet.py
python3 v10/code/d10_reproducibility_audit.py
```

The reproducibility audit reports:

```text
D10 REPRODUCIBILITY AUDIT
scripts=3
normal_optimized=BYTE_IDENTICAL
d10_bloch_lorentz_exact.py bytes=4229 stdout_sha256=aec13fa5e950590a26f318a7f5b3ee13aa4768375ff0aee9cb466c49ca4af484
d10_finite_clock_convergence.py bytes=7227 stdout_sha256=1aa359956a10b01390ef7150c4db6de841d1ad3c26f004673cf05cf02ad0406b
d10_relational_scir_packet.py bytes=2327 stdout_sha256=11e38ec6a630ef503ed48bb91ab43eb673b3a150d3d2fed341f78aaa9fcc587c
audit_sha256=379b43354f8bb7137ca98b2d776abac73e5a579d947b167f969c22b9aa190e1a
```

## Receipt summaries

```text
D10 BLOCH-LORENTZ EXACT RECEIPT
checks=101
exact_bridge=PASS
alternative_spin_factors=EXHIBITED
complex_selection=NOT_IMPLIED_BY_CONE
local_gauge_diamond=PASS
full_lorentz_gauge=REQUIRES_NONUNITARY_SL2C_EXTENSION
provisional_scope=KINEMATIC_AND_CONDITIONAL
receipt_sha256=52c02c70358655913a5bf54614b5834cecaeb5979a9d96e5c56d459d4490973e

D10 FINITE CLOCK CONVERGENCE RECEIPT
checks=97
precision_decimal_digits=90
load_bearing_method=spherical_voronoi_triple_enumeration
independent_probe=fibonacci_120000
finite_cones=OUTER_POLYHEDRAL_APPROXIMATIONS
receipt_sha256=0cf75d4511b9fb20965f70d33fd8cd6a21f755a160492f423a076c67f14818d5

D10 RELATIONAL SCIR PACKET RECEIPT
checks=32
depth12_projectors=113
depth12_sampled_support=0.914143429015
external_sphere_sampler=ABSENT
finite_local_grammar=H,T,SEAL
local_influence=PASS
bloch_increment_map=DECLARED_NOT_DERIVED
order_influence_cone_equivalence=OPEN
receipt_sha256=b28f286f59879420ed7f320200a95e54a39381ec3451959b012dc5c913fad0f0
```

## Frozen artifact hashes

```text
26e61c146b328b5eae14994594f79bb70421a275a35de464b4245e482dc42a46  v10/note-d10-bloch-celestial-selection-protocol.md
8d9d05f6ea95d4c522f8cf7bde9d05d88e1bb712bf65c3eaf5da21cc8fc155b8  v10/code/d10_bloch_lorentz_exact.py
32b5be41cb73c41d9804c2576c3297aa5ba3d9d044fa6a4283e7a003c708f7ed  v10/code/d10_finite_clock_convergence.py
5417d17efcbfed942701f9cf9512327aaa665bf3ba489d6aec72f4456225290b  v10/code/d10_relational_scir_packet.py
527fd9bbd4cc19f0741b33bfb4812be424fb83f32bcad6a620f1a4e54149bde4  v10/code/d10_reproducibility_audit.py
435a4c183d908a7e2191de455946a78d20287421020adfff5b80c6de4b2feee7  v10/note-d10-literature-audit-bloch-celestial.md
cd3e7109078daa3e7688fa3c5e639ef5094e414a752c7b338cbdf5fdf33ac06e  v10/note-d10-bloch-celestial-investigation.md
500e5e92cb11b6941486350c716a21705d3a2a9f9e3d506fb8d0567756d7fba7  v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
```

## Claim boundary

D10 claims an exact algebraic bridge and a finite local candidate. It does not
claim unique complex selection, physical Bloch/celestial identity, full boost
gauge, order/influence equivalence, Einstein dynamics, absolute units, or `G`.
