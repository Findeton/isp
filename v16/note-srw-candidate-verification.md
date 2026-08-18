# SRW candidate verification — exactness defect found

Status: **VERIFICATION FAILED; CANDIDATE PRESERVED; FORWARD REPAIR REQUIRED**.

Frozen candidate commit: `4f465d0`.

Frozen candidate hashes:

| artifact | SHA-256 |
|---|---|
| scorer | `18f0e4f1af224f7f2c6753951621eb3d42dd5e4ce22ee9fd6068ac3e7d62e0ed` |
| fixture | `e40650f04c60635e68fd91938dbba201afec6e426c2e1cfaa0b4f4d8dcefd2e3` |
| output | `efec1a36cc27863f1107d3e79dbf1cfcdca62f40e182eebeb5d6269288a032fc` |
| receipt | `9c6098dd5f9ac2dc0d05f39692c3d08e2733941778fc48be96b6d3f43ffaf6e8` |
| paper | `f61dde79e5fc0e10db1e5dbe13dec25dceaff9842d5e0c5c06ba2ae90eb4bcae` |

Two clean temporary-path runs were byte-identical to all three committed
candidate artifacts and to one another. The anchor-corruption selftest refused
without writes. Mutants from `anchor-corrupt` through `reciprocity-remove`
passed their registered death checks: 19 mutants refused at their named gates
and wrote no artifact.

Verification stopped at `phase-frame-break`. Instead of a controlled refusal
at `SRW-PHASE-GAUGE`, it raised:

```text
AttributeError: 'float' object has no attribute 'denominator'
```

The root cause is in frozen generic core `srw_core.py`. The `GQ` dataclass
annotates `re` and `im` as `Fraction` but does not coerce constructor inputs.
The constants `ONE = GQ(1)` and `I = GQ(0,1)` therefore store Python integers.
`GQ.inverse()` divides those integers with `/`, producing floats along the
phase-frame path. The AST's zero-float-literal gate cannot detect this runtime
type leak.

The finite group rows happen to retain the displayed values—64 connections,
four size-16 orbits, and screens `1,1/2,0,1/2`—but that numerical agreement
does not license the receipt's exact-`Q(i)` claim. Candidate verification is
therefore failed, not partially passed, and mutants 20 through 26 are not yet
credited.

The forward repair is bounded but substantive:

1. add `GQ.__post_init__` coercing both components through `Fraction`;
2. add a runtime scalar-type gate that checks every phase and transformed
   component is a `Fraction`, rather than relying on AST literals;
3. anchor the repaired core explicitly without altering the opened physical
   fixture's equations or data;
4. add one direct runtime-leak mutant or a machine-checked forcing;
5. regenerate the three candidate artifacts from the repaired, precommitted
   source; and
6. rerun all clean, mutant, off-tree, seal, and paper checks.

No matrix identity, graph, rewrite span, dictionary count, future probability,
support count, fiber dimension, angle screen, reciprocity equation, outcome
index, paper claim, or scientific interpretation is repaired by assertion.
All frozen candidate bytes remain available at commit `4f465d0`.
