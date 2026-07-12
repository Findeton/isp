# D21 final receipt

**Frozen:** 2026-07-12 after protocol, exact construction, literature audit,
round-1 hostile openings, repairs and round-2 integrated audit.

## Executable result

```text
CHECKS PASSED: 40/40
SEMANTIC SHA256: 46f9e4ff8a6627f289a4786d2d5fd43c21e936c6a05f22c3e7a8a58be0c07533
SOURCE SHA256: 93dd24b415adfc59272df484dadeb73cf0d8f5abe0cc0ad65c9708b0b597eeb4
VERDICT: FINITE-COMPLETE-RULEBOOK-DISCRIMINATOR
```

Normal and optimized Python both exit zero with the same 40 checks, semantic
hash and source hash.

## Frozen file hashes

```text
93dd24b415adfc59272df484dadeb73cf0d8f5abe0cc0ad65c9708b0b597eeb4  code/d21_two_rulebook_discriminator_exact.py
255fceb6f4e57731f448433599aa1c5a0bce106a86a7a1e9b445142534bbe9fb  data/d21-two-rulebook-discriminator-exact.json
38730db47669cf94f484e864f00bd47ca6fcfbddde5f699619c85c761fdfb44b  note-d21-two-rulebook-comparison-protocol.md
e1de6147edde6fc832c562a25061378d26d97adce0e2abd48ae33a078eac4b19  note-d21-two-rulebook-investigation.md
a141bfe9658d775093930ff7e6fc150e0a7c391484ebf37365ca217eac50a612  note-d21-literature-audit-two-rulebook-discriminator.md
40e034aba9626130e71fed53481085495b89a91163ac677ef22f542eea935d4e  relativistic-isp-v10-paper17-two-complete-history-laws-one-record-interface.md
2e5c7f9905f008adbec57e2e06379fc993bb9e8bd9a46e560a8caeb0face1b12  reviews/d21-round1-mathematics-hostile-review.md
39cd47a4ac43ac35ba6bfefb09780a016ef93c762d92c41b8d9da0414e318982  reviews/d21-round1-ontology-locality-hostile-review.md
f23a6287d859d58d0d27fafc6a5a64e6300a301c259d0d1e5e1d2f21aaf68cdf  reviews/d21-round1-opening-ledger.md
317906861e81632156b36a617788b72ac3fa60eb785ae615289c1785b42e7d4b  reviews/d21-round1-physics-identifiability-hostile-review.md
b2c656ea1e1001ff4c2ccb781547c44d1509546ec8c375ece7afda1520c0b95a  reviews/d21-round1-rebuild-hostile-review.md
3271376737da34ffde02e91bc7da7f557d48440372ebd71024c606aa9ee73d6a  reviews/d21-round2-integrated-hostile-review.md
```

The receipt's own hash and index-file hashes are intentionally not included
inside this self-referential manifest.

## Regression and containment

- D19 empirical-identifiability regression: `20/20`, exit zero.
- V10 self-containment audit: `4/4`, exit zero under Python 3.9 after a
  compatibility repair; all current V10 executables are included in the
  census, with numpy/sympy dependencies explicitly declared.
- All D21 source lives under `v10/`; no D21 source or runtime dependency was
  placed in `.env`, `.venv` or an external code directory.

## Claim ceiling

```text
PROVED: two inequivalent complete fixed-carrier finite instrument laws share
all proper record shadows and differ at complete-support Mermin/XXX order.

NOT PROVED: two complete cosmological generators, arbitrary record-record
birth/join dynamics, relativistic collapse ontology, physical eta scale,
untouched empirical selection, round cones, 3+1 emergence, gravity or G.
```
