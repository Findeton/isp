# D12 pre-hostile-review receipt

**Date:** 2026-07-11  
**Status:** frozen for independent hostile review  
**Provisional verdict:** `UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS`

## Exact executables

```text
d12_diamond_law_nonuniqueness_exact.py
  checks=42
  semantic_receipt=1f9472d6ed613ad96fe875d68cf0a773062c077e9a44fc357f65ccfd93bd4b97
  stdout_sha256 normal/-O=ffaf1bb6bb8125ca4f4d08d048d8828f6c48b81eb5e99f14ba6b0b3f8621ff7d

d12_symmetric_interaction_family_exact.py
  checks=18
  semantic_receipt=7da912f8deb705aaa1467d3428aacf7cc626b249bf16c324c5c365f376b89db9
  stdout_sha256 normal/-O=a2da06a85371f83de4b22047f734747a988254cfce887039563b34161b3ba73f

d12_restored_diamond_process_exact.py
  checks=25
  semantic_receipt=c31174cbc695de30169e5acf1492998990609ea68e2b20e09b98d6370e039391
  stdout_sha256 normal/-O=7d97f74d547ca13aab6d4978a69732afe27caf0568a2394b512da2e000237586
```

All three use Python's standard library only.  Theorem-critical probability,
matrix, gauge, and history calculations are exact in `Fraction` or
`Q(sqrt(2),i)`.  Decimal at 120 digits occurs only in the first executable's
exponential survival and transcendental fixed-point diagnostic.

## Artifact hashes

```text
e5a8a50ffe03459cf62ca5b5168fd48079c6309fb3ae7ac2d7310203c1669b1f  code/d12_diamond_law_nonuniqueness_exact.py
34215f2605f68029e4bce59c9e471d8af5892269d6b4b0ee7ac0193f67fe55dc  code/d12_symmetric_interaction_family_exact.py
0cfd533c70d29b3f82107927cb7d96b9333af185de57d3161e36800cdb4118fa  code/d12_restored_diamond_process_exact.py
88142db43046b729bb88b4d5fd2fe345384d2431a6c239e91419a02b748de5b8  note-d12-diamond-restoration-uniqueness-protocol.md
a2f4feca2e2b689979c7794e2547c041890dac1f50d6dfaf73da79dc900aa8a5  note-d12-v6-v10-compatibility-ledger.md
a367cf1bc613fb68db39c872579da4dc7d9e0f85ed9df1aa0614d118c8219c74  note-d12-extension-law-characterization.md
f902092529a458c46e04cc0fb1249f9b3eb17b2f612a7444063fb59266d9b567  note-d12-selection-principle-audit.md
357f8d2e9320e91a5847dfd3c7a3036c9c724ffc5d3de15e2016cb9d4e04e399  note-d12-geometry-consequence-gate.md
430b13c9bb46a4d3d6a7d7bf411e91cecd7a9ed67ea129aba121d57f6750d084  note-d11-postscript-diamond-omission.md
ed40587879c7cdbd6259bb65a84cf63e77aed382021ad1530655aea601c8980d  relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

## Regression and containment

```text
v10_self_containment_audit.py: 4/4 PASS
d7_rulebook_nonselection_exact.py: 68/68 PASS
d8_scir_exact.py: 101/101 PASS
d10_bloch_lorentz_exact.py: 109/109 PASS
d11_complete_bloch_lorentz_exact.py: 73/73 PASS
```

## Frozen claims sent to review

```text
complete holonomy identifies but does not generate a law;
the commitment fixed point is conditional on supplied physical presentation;
projective non-Markov whole-history laws remain inequivalent;
standard structural and symmetry gates leave a continuous interaction angle;
the next-click law is disintegration of a primitive/empirically selected process;
the restored universal diamond process works exactly;
the universe-specific process/action/couplings remain additional physics;
geometry is not licensed before process selection.
```
