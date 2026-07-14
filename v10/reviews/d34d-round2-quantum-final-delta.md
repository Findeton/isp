# D34d round 2 — quantum/process final delta

**Target:** commit `44a54d4`, audited only against the two nits remaining in
the round-1 quantum/process delta.

**Verdict:** **NOT YET TEXTUALLY DELTA-CLEAN — 0B / 0M / 0m / 1n**.

The receipt and all scientific claims remain clean.  The rank-certificate nit
is fully closed.  The Q3 terminology nit is almost, but not completely,
closed: one stale source comment still calls the cross-context comparison
“lumpable.”

## 1. Fresh reproduction

I ran

```text
PYTHONHASHSEED=130363 python3 -O v10/code/d34d_quantum_predictive_exact.py
```

It exits zero, prints 10/10 and reproduces the unchanged summary hash

```text
cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0
```

No output, probability, matrix, scope statement or claim ceiling changed.

## 2. Nit disposition

### n1 — rank certificate naming: CLOSED

The former generic `rank` accumulator is now consistently named
`rank_from_block_proof` at initialization, increment, gate, detail output and
summary construction.  That name accurately states the logic: each of four
disjoint blocks has zero determinant and positive trace, hence rank one and
total rank four.  No false independent row-rank calculation is implied.

### n2 — stale Q3 lumpability terminology: ONE COMMENT REMAINS

The section heading is repaired to
`cross-context durable-record insufficiency`, the Boolean is correctly named
`record_projection_operationally_insufficient`, and the printed Q3 statement
continues to say explicitly that this is not non-Markovianity of one fixed
process.

However, source line 248 still reads:

```text
# next visible output instruments, so this projection is not lumpable.
```

That is the exact cross-context-to-lumpability terminology the repair was
intended to remove.  Replace it with, for example:

```text
# future output laws, so retaining only s is operationally insufficient
# across these two declared past-instrument contexts.
```

This is a source-comment nit only.  It does not affect execution, the receipt,
the fixed-process causal-break witness, or any paper-level conclusion.

## 3. Final scope

The accepted quantum result remains:

> **FINITE FIXED-PROCESS QUANTUM MEMORY + REBIT BOUNDARY-STATE
> CHARACTERIZATION.**

After deleting the single stale word in the Q3 comment, this stream can be
recorded as `0B/0M/0m/0n DELTA-CLEAN`; no receipt rerun or conceptual review
is otherwise required.
