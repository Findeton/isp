# D9 final receipt — minimal Bell packet and one-coupling refutation

**Date:** 2026-07-11

## Frozen claim

```text
MINIMAL-NUMERIC-SCIR-BELL-PACKET-FOUND
+ EXACT-BORN-TSIRELSON-NOSIGNALLING
+ GAUGE-RELATIVE-TOMOGRAPHY
+ THETA-PI/4-WITHIN-PARTIAL-ISWAP-FAMILY
+ G-SHADOW-1/2-FROZEN-BEFORE-GEOMETRY
+ DRIFT-MATCHED-DIMENSION-CONTROL-PASS
+ FULL-INFLUENCE-COUPLING
+ SHAPE-DIMENSION-SCALE-HOLDOUT-FAIL
= REFUTED-ONE-COUPLING
+ SCIR-NOT-REFUTED
```

## Exact Bell packet

Commands:

```text
python3 v10/code/d9_minimal_bell_packet_exact.py
python3 -O v10/code/d9_minimal_bell_packet_exact.py
```

Normal and optimized stdout are byte-identical.  Key output:

```text
D9 MINIMAL BELL PACKET EXACT RECEIPT
checks=126
theta=pi/4
g_shadow=(1/2)+(0)sqrt2
CHSH=(0)+(2)sqrt2 decimal=2.8284271247461900976033774484193961571393437507538961463533594759814649569242140777007750686552831454700276924
B0_recovered=((0)+(1/2)sqrt2,(0)+(1/2)sqrt2)
B1_recovered=((0)+(1/2)sqrt2,(0)+(-1/2)sqrt2)
context_attack_norm2=(3/4)+(0)sqrt2
finite_E00=0.709570000000
finite_E01=0.707540000000
finite_E10=0.706930000000
finite_E11=-0.706930000000
receipt_sha256=754c87826fb1b5b3a61efdf6c0ee203357aba8c49de6c130df41124b3c8e1ab7
```

Stdout SHA-256:

```text
5a7c3a90c1b8ff2c2f6bebd219ab44545cc7198f912b127d123eed476b013e45
```

## Drift-matched dimension validation

Command:

```text
/Users/felixrobles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 v10/code/d9_drift_matched_dimension.py
```

The receipt passes 21/21 gates.  Load-bearing `d=4` controls:

| injected scale drift | legacy reading | matched reading |
|---:|---:|---:|
| `1.00` | `4.139749` | `4.008057` |
| `1.55` | `6.000000` | `4.013223` |
| `1.94` | `6.000000` | `4.138438` |

All synthetic latent dimensions `2..6` pass the frozen matched-recovery
tolerance at drift ratios `1`, `1.55`, and `1.94`.

Stdout SHA-256:

```text
6a1270fb33e1f16a869e227a40970d44c7cd91760abc338fc9551f58f8076889
```

## Bell-frozen geometry holdout

Command:

```text
/Users/felixrobles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 v10/code/d9_frozen_packet_geometry.py
```

Output:

```text
D9 BELL-FROZEN PACKET GEOMETRY HOLDOUT
v9_source_sha256=aff9525110f6fd209332badccf1a5353c011be9eb8461a4db50063bf0670d81a
frozen_theta=pi/4
frozen_g=1/2
primary_seeds=20269900..20269923
F_dom=1.334800679172 se=0.031342050192 t=+3.152336
F_m4=1.239304422452 se=0.018978025767 t=+1.438739
strict_shape_pass=False
corrected_relation_fraction=0.160520218176
corrected_dimension=2.708730221728
observed_scale_drift=1.774124617186
dimension_refusals=24/24
S4_witnesses=24/24
influence_slots=32,32,32
scale_N=2048 F_dom=1.371094694907 se_dom=0.086637900084 F_m4=1.253627196450 se_m4=0.028783394938 corrected_d=2.733840027518 drift=1.755899324194
scale_N=4096 F_dom=1.558498631392 se_dom=0.067905160201 F_m4=1.391889063124 se_m4=0.039072051271 corrected_d=2.199734084775 drift=2.584227994204
scale_N=8192 F_dom=1.678201609803 se_dom=0.084111228397 F_m4=1.487290513097 se_m4=0.047943898988 corrected_d=2.189838334127 drift=2.565805181576
dom_worsening_z=+2.543306
m4_worsening_z=+4.178492
scale_reversal=True
verdict=REFUTED-ONE-COUPLING
receipt_sha256=c10442d1b20cedd7fff737a087f78f481e2f0e07c9740615b76105c0ab0a1bc6
```

Stdout SHA-256:

```text
55c93d5d330838d5b8a3800cef5ea85410ecfceb3ea63437f7dee189b9705d85
```

## Frozen source hashes

```text
eaf86c63b68c2279cecb633c30cb6e88ee5f838b3b004d1cb8a9ae0b2bb3e8b4  v10/note-d9-minimal-packet-and-anti-tuning.md
f0d00767a1b349c447bd92f8b2c7c11307c0aab4c7ae34fd38dc41484b0e692c  v10/note-d9-literature-and-hostile-self-audit.md
2362a2562bdaff5a0add7004bae700ed97dcc737e052dcdfafc556a66a216c03  v10/code/d9_minimal_bell_packet_exact.py
f4c456e54a89e3c34b95c801d642aafffea49a996a90e9a082d19e0a57b8a31f  v10/code/d9_drift_matched_dimension.py
eee2c76916e82cd3ac781ef3eedbc79de23afe16cc1c52a259d88fb8cfb8dd58  v10/code/d9_frozen_packet_geometry.py
ce7d309fd25a8fae2e8e23618ee6ec71f28c1ca4bab7a25fc32b5dc9cf4a7e32  v10/relativistic-isp-v10-paper10-bell-identifies-but-does-not-set-geometric-coupling.md
```

## Scope

The Bell packet identifies the state/measurements up to the declared gauge and
fixes `theta` only inside the one-partial-iSWAP family.  It does not
device-independently identify a unique source circuit.  The corrected
dimension remains a validated volume proxy, not a manifold-dimension theorem.
The holdout refutes the one-coupling identification, not the SCIR architecture.

