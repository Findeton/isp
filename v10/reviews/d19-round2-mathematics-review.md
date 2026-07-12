# D19 focused round-2 mathematics review

**Date:** 2026-07-12  
**Verdict:** **PASS**

## Decision

The round-one scope blocker is repaired. The executable, packet, receipt and
theorem now identify the exact result as

```text
FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY.
```

They explicitly deny generator nonselection, physical ultraviolet realization,
and any new empirical measurement of nature. The triple-correlation and future
conditional are diagnostic coordinates constructed from the known null
direction, not independently untouched physical holdouts.

## Reproduction

```text
source    fdf804f29144513dcfe2398262213551e1c462c222118939d5587a5173331bdb
packet    5a53f79470f22d9b517b440b7c6752b39719da01696f0e2cd56fecaa33a5dc68
theorem   78702090ef1d9db42fcc417eaa567f09e31afb88ba2a7e1f30cc61e500bdffcb
receipt   592539e13d77a8066f329cbc96ba0d56305f2698ecc6ca8d5a86eb151aaee4ec
stdout    5d1f0f22ea566082279990e92a04e5483ef3acb64e11cbcc72d36ac9f311f3a8
checks    20/20 normal and optimized
```

Normal and optimized output are byte-identical.

## Mathematical regression audit

The substantive theorem is unchanged and exact:

```text
carrier dimension                         8
training-map rank                         7
null direction                            xyz/8
shared one/two-record marginals           uniform
survivor parameters                       r=1/2 and r=1/3
triple correlations                       1/2 and 1/3
P(z=1|x=1,y=1)                            3/4 and 2/3
```

Both laws remain strictly positive and normalized, their difference lies
exactly in the null direction, and both visible conditionals retain genuine
dependence on earlier `x` at fixed current `y`.

## Claim boundary

The theorem correctly states the implication:

> Frozen one/two-record evidence does not identify an unrestricted complete
> history law because the observation map has a physical positive null
> direction.

It also correctly states what does not follow. To prove generator
nonselection, D19 would still need two inequivalent frozen generators whose
images realize the two laws, after quotienting gauge/field-redefinition
equivalence. A restricted independently justified generator class could remove
the history-law null direction.

The physical evidence ledger is now contextual motivation rather than an exact
consequence of the eight-history calculation. V9 remains unopened.

## Final verdict

**PASS.** The exact mathematics and hashes reproduce with no regression, and
the repaired semantic/prose ceiling matches the theorem actually proved.
