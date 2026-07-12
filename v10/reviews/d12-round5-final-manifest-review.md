# D12 round 5: final archive-manifest review

**Referee:** independent archive-only audit  
**Date:** 2026-07-11  
**Verdict:** **PASS — FINAL MANIFEST AND SELF-CONTAINMENT CLOSED**

The new `v10/data/d12-final-receipt.md` exists and every filesystem hash,
path, executable output, review reference, regression count, and containment
claim checked in this audit agrees with the workspace.  The formerly mixed
round-1 repair manifest now records the current 145-check executable, stdout,
source, and final Paper 13 hash.  No remaining mismatch was found.

This is an archive audit only.  It does not reopen or enlarge the scientific
scope adjudicated in hostile round 4.

## 1. Final authoritative files

Direct SHA-256 recomputation gives:

```text
179c885ea74b6523f3ff9ae4ea93dec161a35c3dd6d678db297b97d9fc21a860  v10/data/d12-final-receipt.md
e203453d4138a565f87dcc162a1faea13e434fcdade137254e2e5e9ae2216b37  v10/data/d12-round1-repair-receipt.md
54c2c6e1f193658924e3ac35e52ca897f95a07dbd4412bf86b4b0f0e0fb2b74b  v10/code/d12_multidiamond_history_exact.py
f9f9c11b8598a6c8d45dd32fdbed0ed22706d61f697f969899f0bdb14b392ad9  v10/relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

The final receipt and the historical round-1 repair receipt both now name the
same current executable facts:

```text
checks=145
semantic_receipt=d48f9a161dd3e7f850726225d9ea3faad8433fe35ede0c3957cbbb0963e691c6
stdout normal/-O=466cbfc9dbdfb4432428779b1f4054921a98f3869c3aa665ba723e7e0a623521
source=54c2c6e1f193658924e3ac35e52ca897f95a07dbd4412bf86b4b0f0e0fb2b74b
Paper 13=f9f9c11b8598a6c8d45dd32fdbed0ed22706d61f697f969899f0bdb14b392ad9
```

The source was not changed by the administrative repair.  Its normal and
optimized outputs had already been independently reproduced byte-for-byte at
the stated stdout hash, with the stated check count and semantic receipt.

## 2. Supporting executable receipts

All three files exist at the manifest paths and have the listed source hashes:

```text
e5a8a50ffe03459cf62ca5b5168fd48079c6309fb3ae7ac2d7310203c1669b1f  v10/code/d12_diamond_law_nonuniqueness_exact.py
34215f2605f68029e4bce59c9e471d8af5892269d6b4b0ee7ac0193f67fe55dc  v10/code/d12_symmetric_interaction_family_exact.py
6f55ab55476925b7474bc78866646a1bbf26609d8b36c11f8175d75fda39827b  v10/code/d12_restored_diamond_process_exact.py
```

Normal and optimized executions are byte-identical and match the final
manifest:

```text
42-check countermodel stdout  ffaf1bb6bb8125ca4f4d08d048d8828f6c48b81eb5e99f14ba6b0b3f8621ff7d
18-check symmetric stdout     a2da06a85371f83de4b22047f734747a988254cfce887039563b34161b3ba73f
25-check precursor stdout     b3411c5f77498af0a70ba9ea3d3fb21ac80bc80be048863805eca180391f120a
```

Their printed semantic receipts also match exactly:

```text
1f9472d6ed613ad96fe875d68cf0a773062c077e9a44fc357f65ccfd93bd4b97
7da912f8deb705aaa1467d3428aacf7cc626b249bf16c324c5c365f376b89db9
bf05e72d6f806f674c6d2a9b7621f3e78bb37c905987b83f62f3a3180209f172
```

The 25-check program still labels itself
`ONE_CELL_PRECURSOR_REPLACED_BY_MULTIDIAMOND_EXECUTABLE`, as the manifest
states.

## 3. Manuscript and note paths

Every manuscript/note path in section 3 of the final receipt exists, and each
hash recomputes exactly:

```text
f9f9c11b8598a6c8d45dd32fdbed0ed22706d61f697f969899f0bdb14b392ad9  Paper 13
430b13c9bb46a4d3d6a7d7bf411e91cecd7a9ed67ea129aba121d57f6750d084  D11 postscript
88142db43046b729bb88b4d5fd2fe345384d2431a6c239e91419a02b748de5b8  restoration protocol
a2f4feca2e2b689979c7794e2547c041890dac1f50d6dfaf73da79dc900aa8a5  V6--V10 ledger
a367cf1bc613fb68db39c872579da4dc7d9e0f85ed9df1aa0614d118c8219c74  extension characterization
2670a2ea7644963e0e517b6ab7511e6ea031f767beba0251bd3b357dc6501de6  selection audit
357f8d2e9320e91a5847dfd3c7a3036c9c724ffc5d3de15e2016cb9d4e04e399  geometry gate
12604d2edb5438ec35719b710cc797cf84371eb84e8a8c45994b5d10c2c38796  round-1 repairs
d5bd82c8ad58409518bce14fbc02715dcb8a6173dd1e35593340e0233c9662f6  round-2 repairs
fe344a86a80047fb8ae29c93b8a98f1013b910316c17110b9635e13dcdc2df2a  round-3 repairs
```

The round-3 note's reference to `v10/data/d12-final-receipt.md` now resolves.

## 4. Hostile-review trail

All twelve hashes in the four-round hostile trail resolve to the expected
review files and match byte-for-byte:

```text
round 1  4d002941...  03ce60f1...  0cfe4660...
round 2  f3d13ffa...  49382d3d...  ac05d917...
round 3  21cd49ec...  15e0cc4a...  6e992649...
round 4  d045417b...  2bf55af9...  07cbd8ce...
```

The files preserve the actual progression from major revision, through
focused residuals, to the narrowed final PASS.  The round-4 independent
review's sole administrative condition is precisely the manifest repair now
being audited.

## 5. Regression and self-containment

The regression programs reproduce the counts listed in the final receipt:

```text
v10_self_containment_audit.py             4/4 PASS
d7_rulebook_nonselection_exact.py        68/68 PASS
d8_scir_exact.py                         101/101 PASS
d10_bloch_lorentz_exact.py               109/109 PASS
d11_complete_bloch_lorentz_exact.py       73/73 PASS
```

The containment claim was also checked directly rather than inferred only
from the audit label:

- an exhaustive workspace search finds exactly four `d12*.py` files;
- all four reside under `v10/code/`;
- no D12 source exists under `.env`, `.venv`, or elsewhere;
- no `.pyc` file exists anywhere below `v10/`; and
- the D12 exact executables use only Python's standard library.

The self-containment audit's static source list predates D11/D12, but that does
not create a manifest mismatch: its reported 4/4 checks genuinely pass, and
the D12-specific location/cache claims were independently verified by the
exhaustive scans above.

## 6. Final determination

| Archive gate | Result |
|---|---|
| final receipt exists | pass |
| authoritative source/check/semantic/stdout tuple | pass |
| final Paper 13 hash | pass |
| repaired historical manifest | pass |
| three supporting executable source hashes | pass |
| three supporting normal/-O stdout hashes | pass |
| manuscript and note hashes/paths | pass |
| twelve hostile-review hashes/paths | pass |
| regression counts | pass |
| D12 source containment | pass |
| absence of `v10` bytecode artifacts | pass |

No stale hash, missing path, ambiguous current artifact, or containment
failure remains in the D12 final archive.

**Round-5 final-manifest verdict: PASS.  D12 is archive-ready at the exact
narrowed scope stated in the final receipt.**
