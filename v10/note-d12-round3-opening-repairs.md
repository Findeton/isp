# D12 hostile round-3 focused repairs

**Date:** 2026-07-11  
**Round-3 mathematics:** PASS  
**Round-3 ontology/rebuild:** two constructor/receipt blockers  
**Status:** repaired and frozen for final focused closure.

## 1. Upper-frame domain validation

Round 3 showed that lower-collar eligibility rejected a nonunitary stored
frame but `fire(history,...,upper_frame,...)` accepted a newly supplied
nonunitary upper frame.  `fire` now validates `A^dagger A=I` before constructing
the link, screen, record, or born collar.  A direct hostile-style probe calls
`fire` with the diagonal nonunitary frame and must receive `ValueError`.

Both ends of every generated link are therefore inside the explicitly claimed
unitary-frame domain.  Nonunitary Lorentz gauge remains openly outside this
packet theorem.

## 2. Exact RN reconstruction and mutation refusal

Round 3 correctly observed that manually correct RN fields were not derived by
the receipt.  The packet no longer stores unverified log-coordinate values.
It stores exact support-relative RN **contrast ratios**.  The executable now:

1. reconstructs positive support from nonzero history masses;
2. conditions both the law and positive reference on that support;
3. computes exact RN values;
4. divides each nonbaseline RN value by the baseline RN value;
5. compares the resulting ratios with the packet field.

Two mutation controls must fail: quarter-iSWAP ratio `(7)` in place of `(1)`,
and false support `(0,3)` in place of `(1,2)`.  The corresponding log-RN
coordinates are the logarithms of these exact ratios; no `-infinity` string is
used as a finite coefficient.

Paper 13 now states explicitly that `h_D` is support-relative when ambient
Born probabilities contain zeros.

## 3. Frozen closure receipt

```text
checks=145
semantic_receipt=d48f9a161dd3e7f850726225d9ea3faad8433fe35ede0c3957cbbb0963e691c6
```

Normal/optimized stdout and source hashes are frozen after the final direct
run and recorded in `data/d12-final-receipt.md`.
