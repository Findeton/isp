# D40c exact closing delta

**Status:** `PASS 4/4`; independent final review open.  
**Date:** 2026-07-15.  
**Source:** `code/d40c_receipt_integrity_delta_exact.py`.  
**Stdout:** `data/d40c_receipt_integrity_delta_exact.out`.

D40c closes only the receipt-integrity findings from D40b round two.

```text
direct locks                    4/4
D40 transitive antecedent locks 12/12
typed level constructors         7/7
exact census       (28,17,44,40,4)
star target mass             23/198
global target mass             5/96
timed/infinite scope claims        0.
```

The scientific theorem and every prior number are unchanged.

```text
source_sha256           = 9ede91edd5f3d4868df00e6b3d6bf30c61160ce9a5dd27734f70e97c244285e4
stdout_body_sha256      = 38755041bcf19dec43dea5078e00901e137c27d492d09f0dcc5600787eafe0ee
internal_science_sha256 = 3f9d2a34a9102295c2fb0f2a24ceb9953ce55e02a580ef8aae7ba01aa31cd3e5
complete_stdout_sha256  = a73a868725f5904535e844cdf9e4144e6499b545cd945b4b782724659635a475
```

The committed stdout is byte-identical to a fresh zero-exit run.
