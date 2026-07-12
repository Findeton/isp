# D1 final canonical receipt

**Frozen:** 2026-07-11  
**Verdict:** `CENTER-NONSELECTION + SUPPORT-OVERELIGIBILITY +
PROJECTIVITY-REFUSAL` for the naive universal record-support birth rule.  
**Accepted scope:** exact finite boundary accounting and marked-history models.

## Source hashes (SHA-256)

```text
ccd80151270a10c2f16996012096db3f3242a2d640404f90a82afa01a7768215  v10/code/d1_no_silent_center_exact.py
276e7919d88878ae9447dbb9a6619f4914b906d4816c8addc8f71b41c3883703  v10/code/d1b_marked_support_restriction_exact.py
c72ed14601fe474c177d6aee97e1a0b94d2290c46b723c9b4332a0792189131c  v10/note-d1-no-silent-support-birth.md
c8802b0aecde37755ec1099419de0c5dba6ed68166252879e12b1dd871841747  v10/relativistic-isp-v10-paper2-no-silent-centers-do-not-select-support-birth.md
```

## Execution

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 \
  v10/code/d1_no_silent_center_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 \
  v10/code/d1b_marked_support_restriction_exact.py
```

Results:

```text
D1A: ALL CHECKS PASS (45/45)
D1B: RECEIPT: 28/28 exact checks passed
```

Each receipt was executed twice after the final repair. Output was
byte-identical across repeats.

```text
25e5d0eefd35f8cdac40b5cc42683f189d7d8caeeee697425377b0f7772fad21  D1A stdout
e589cfb7b5690a246cb8cf3adba68f374c9c2ce61525e7f9448fbb82ce22e799  D1B stdout
```

D1A uses integer cross-products for every verdict and Python standard-library
`Decimal` at precision 120 for CMI reports. D1B uses integer arithmetic
throughout. All investigation source is inside `v10/`; neither receipt needs a
virtual environment or third-party package.

## Final theorem boundary

1. A supplied finite cut may have a unique minimal marked nonlookup center.
2. Strict positivity, equal center-cell count, and equal cell-mass entropy do
   not guarantee center uniqueness.
3. Unique closure on every pair and triple cut does not select one support from
   a supplied common-root candidate family.
4. A supplied direct-carrier/output-port axiom blocks structurally unlicensed
   joins and does not transitively complete an `AB-BC` chain.
5. Marked history data restrict path-independently on both executed subset
   lattices.
6. Under intersection support projection, the derived eligible-support family
   fails naturality on an exact pairwise-independent, jointly dependent
   parity/synergy history.
7. No-silent closure does not derive the direct carrier, event rate, transfer
   kernel, initial root, continuum/profinite limit, or spacetime dynamics.

## Independent hostile closure

- `reviews/d1-round3-mathematics-hostile-review.md` — final PASS;
- `reviews/d1-round3-independent-rebuild-hostile-review.md` — final PASS;
- `reviews/d1-round3-ontology-locality-hostile-review.md` — final PASS.

Round-2 major reviews and the round-1 disposition ledger remain preserved in
`v10/reviews/`.
