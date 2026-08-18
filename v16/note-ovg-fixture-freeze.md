# OVG physical fixture and verdict-neutral scorer freeze

Status: **FROZEN BEFORE FIRST PHYSICAL EXECUTION**.

Pin commit: `d36b9e5`.

Generic-core commit: `ea71160`.

The data-only physical fixture and verdict-neutral scorer are now byte-frozen:

```text
OVG_FIXTURE_SHA256 = `7b7658492a49c77f6c9ee3e0a2031d5121c627aad5ae6630e21940a68c92b133`
OVG_SCORER_SHA256 = `012171c27b766030b9b8ef02f5cc6a71e86c367af40faeec240d2d5552447e74`
OVG_CORE_SHA256 = `7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf`
```

At this freeze the following reserved result paths do not exist:

```text
v16/code/ovg_output.txt
v16/code/ovg_receipt.json
v16/paper-05-overlap-gram-instrument-variety.md
```

No ordinary scorer invocation, selftest, physical mutant, result build,
classifier build, or paper render has occurred. Only JSON parsing, Python
compilation/AST parsing, fixture-vocabulary inspection, unknown-argument
refusal, path-absence checks, and source hashing were run.

The fixture contains no `expected`, `result`, `verdict`, `outcome`,
`pass_count`, `solution_dimension`, or `target_coefficient` key, and none of
the first four words appears anywhere in its bytes. It declares only:

- actors and typed elementary map descriptors;
- five unitary common-boundary cases with independently checkable spectral
  certificates;
- one dimension-changing isometry pair;
- one three-history carrier family and one delayed-reactivation family;
- four rewrite critical pairs;
- a bounded exact complex-coefficient census grammar;
- a frozen binary factorization grammar, Toffoli sensitivity control, and
  ancilla policy;
- local flag catalogue types and an idle spectator.

The scorer imports the generic core only at its frozen hash. It computes Gram
operators, coefficient solutions, all-input residuals, phase ranks,
dimension-changing operator equations, port channel signatures, critical-pair
types, factorization words, `F_2` linearity, flag dilations, and spectator
marginals. It carries all 30 pin-registered mutants and maps each to a named
gate. Source AST inspection finds zero float literals; unknown arguments exit
`2` without loading the physical fixture.

The first ordinary execution is now authorized. It must either refuse and
freeze the failure as-is, or produce exactly three artifacts and commit them
as-is before replay or mutation testing.

## First invocation refusal

The first ordinary invocation of the frozen scorer exits `1` at
`OVG-ANCHORS` and writes none of the three reserved result paths. The fixture,
scorer, and core hashes remain exactly those frozen above.

Read-only diagnosis finds one failing consumed token. Paper 4 contains the
true sentence “Those are different types of ordered pair,” but a Markdown
line break falls between `of` and `ordered`. The scorer searches for the
literal one-line substring `different types of ordered pair`. Every file hash,
all other consumed anchor tokens, and both fixture/scorer freeze hashes match.

No physical Gram operator, coefficient census, classifier, claim, transcript,
receipt, or paper was returned by this refusal. A bounded source-only repair
may normalize whitespace in consumed prose before token comparison. It may not
change the fixture, anchor hash checks, equations, gates, mutants, outcome
words, renderer, or any physical predicate.
