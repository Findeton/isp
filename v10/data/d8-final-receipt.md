# D8 final receipt — complete SCIR rulebook

**Date:** 2026-07-11

## Claim

D8 supplies a complete-compressed interacting rulebook: finite typed port
data, one root package/state, a finite local opportunity/rewrite grammar, and
finite local unitary/Kraus coupling packets.  These generate exponential local
survival, Born outcomes, durable seals, construction-order-gauge histories,
and a projective nonexplosive full-history measure.

It does not claim a parameter-free law, unique grammar/couplings, or completed
empirical identification.

## Exact SCIR receipt

Commands:

```text
python3 v10/code/d8_scir_exact.py
python3 -O v10/code/d8_scir_exact.py
```

Normal and optimized stdout are byte-identical:

```text
D8 SCIR EXACT RECEIPT
checks=101
root_extensions=1
bridge_legs=2
born_B0=1/2
born_B1=1/2
no_signalling_A=True
commuting_order_equal=True
overlap_order_equal=False
survival_I_plus_J=0.48030530108979937160993840455195355843605760592749125555411827428345221024620952684928248913337078463096405970
survival_relative_error=0
nonexplosion_block_lower=1/4
receipt_sha256=b6387d4e6621402b320b41b5513bd13bbdad667acecfa40899b8ad7d3b0dd430
```

Stdout SHA-256:

```text
bbd2e4ca1b2077db06ccdafd497dcf02c42c3c1a1f3c4160a9f2751bca46f134
```

## Exact diffusion-shadow receipt

Commands:

```text
python3 v10/code/d8_scir_diffusion_shadow_exact.py
python3 -O v10/code/d8_scir_diffusion_shadow_exact.py
```

Normal and optimized stdout are byte-identical:

```text
D8 SCIR DIFFUSION SHADOW RECEIPT
checks=19
g=9/50
pair_contraction=16/25
effective_g=2/5
continuous_semigroup_error=0E-110
free_influence_slots=1
coupled_influence_slots=8
receipt_sha256=b9ee5f0b02932a6c091624d988abf82b6bc57a2f55b6b8895b38efa8cf3580ec
```

Stdout SHA-256:

```text
1bd40680161e0eea4931dae47bdfbcca3776a9b5910a0144308a3cc02a7af875
```

## Fresh 24-seed V9 shadow replication

Command:

```text
/Users/felixrobles/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 v10/code/d8_scir_v9_shape_replication.py
```

The wrapper hash-gates the frozen V9 builder and replaces only its seed range:

```text
D8 SCIR / V9 DIFFUSION 24-SEED REPLICATION
source_sha256=aff9525110f6fd209332badccf1a5353c011be9eb8461a4db50063bf0670d81a
fresh_seeds=range(20268000, 20268024)
F_dom=1.206359971971 se=0.014863055872 t=-1.994208
F_m4=1.172542400393 se=0.009990489711 t=-3.949516
strict_shape_bar=-2.33 both_conventions
strict_shape_pass=False
d_pinned_instrument_suspect=4.486459474023
dimension_refusals=24/24
S4_witnesses=24/24
receipt_sha256=e7a143ce4398482d642ab0041c36426c776d5ae58a02af605019aeab1a715b0e
```

Stdout SHA-256:

```text
10d66cd3dfe1265b28345ec7185d6ddd82737625bb1aa44eb1009afe22e9b630
```

The strict two-convention shape conjunction fails.  The `m4` leg passes
strongly; the `dom` leg does not.  The dimension proxy is printed but excluded
from grading because its nonstationarity remains unresolved.

## Frozen source hashes

```text
4d7407fde5bedb580b53262549f4c98c611bd491862fc1ac122584620c7d4682  v10/note-d8-complete-rulebook-selection-gates.md
b8b9aba18803759b41620f2f66444800cf35bfe22420304c9b4d3e87db87947e  v10/note-d8-independent-sealed-causal-instrument-rewrite.md
4f28f7e96278a55a906d6f8c76e2b6bfa8085d3abbab60eea159e191f0ec865b  v10/note-d8-literature-audit-scir.md
67b94b079880354be5cdd987f75bba25b21e5869b9a448b554c9b36774b0e3d5  v10/code/d8_scir_exact.py
3f2f7a750116c78ed442e9e30c2795e305c593e504c3920444ceb08b650d302f  v10/code/d8_scir_diffusion_shadow_exact.py
4327649dbb5f67c0007ca484b17e491961ad6c255df71fa4376785ad5b2d201b  v10/code/d8_scir_v9_shape_replication.py
ea9ebcf2931e8f63d35aea7a38e4163fede2ce879b6cb8e6f36ba8a48cdfe6bb  v10/relativistic-isp-v10-paper9-a-complete-sealed-causal-instrument-rewrite-rulebook.md
```

## Final boundary

```text
COMPLETE-COMPRESSED-RULEBOOK-FOUND
+ ROOT-AND-LOCAL-OPPORTUNITY-CLOSED
+ QUANTUM-INSTRUMENT-SEAL
+ EXPONENTIAL-EVIDENCE-TIME
+ CONSTRUCTION-ORDER-GAUGE
+ PROJECTIVE-FULL-HISTORY-MEASURE
+ LOCAL-BOUNDED-NONEXPLOSIVE
+ C-ABSORBED-IN-INSTRUMENT
+ G-IDENTIFIED-AS-PHYSICAL-COUPLING
+ DIFFUSION-SHADOW-GEOMETRICALLY-PROMISING-NOT-YET-VALIDATED
+ NOT-UNIQUE-OR-PARAMETER-FREE
```

