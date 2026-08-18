# SRW bounded first-run repair freeze

Status: **REPAIRED SCORER FROZEN BEFORE SECOND INVOCATION**.

The repaired `v16/code/srw_score.py` is frozen at SHA-256
`18f0e4f1af224f7f2c6753951621eb3d42dd5e4ce22ee9fd6068ac3e7d62e0ed`.
The physical fixture remains byte-identical at
`e40650f04c60635e68fd91938dbba201afec6e426c2e1cfaa0b4f4d8dcefd2e3`.

The complete source delta from frozen scorer commit `e5bfabd` is one bounded
text-comparator repair at `SRW-SCOPE-WALLS`:

- the rendered paper is whitespace-normalized with split/join;
- the three predeclared needles are normalized by the same operation; and
- containment and the reported count use those normalized values.

No fixture byte, matrix, graph, rewrite span, dictionary, future generator,
support rule, fiber functor, coupling row, reciprocity equation, phase row,
outcome vocabulary, classifier, paper template, numerical claim, mutant,
artifact path, or promotion rule moves. Static compilation with warnings as
errors passes. The result paths remain absent.

The next invocation is the second physical run, not a replay of a successful
result. A success may generate the candidate artifacts as-is; another failure
must be frozen before further action.
