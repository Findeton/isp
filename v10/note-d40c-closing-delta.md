# D40c — transitive-lock and exact-census closing delta

**Status:** PINNED BEFORE EXECUTION.  No D40c executable or stdout exists at
this commit.  
**Date:** 2026-07-15.  
**Mandate:** `reviews/d40b-round2-independent-review.md`.

D40c is a receipt-integrity delta only.  It may not change any D40/D40b
scientific number or theorem.

## Gates

```text
C0  lock this pin, D40b source, D40b complete stdout and round-two review;

C1  execute D40's own transitive lock/type gate and require exactly
    12/12 antecedent hashes plus 7/7 level constructors;

C2  rerun D40b's two-space census and require exactly
    star serial paths       28,
    star unordered atoms    17,
    global serial paths     44,
    global typed DAG atoms  40,
    global merges            4;

C3  require again the two target masses 23/198 and 5/96, both exact serial
    sums, both normalized, and preserve the three scope zeros.
```

The delta closes only if every gate passes and a fresh run is byte-identical
to committed stdout.  Independent final review must then reproduce D40c under
a fresh seed before Paper 29 begins.

