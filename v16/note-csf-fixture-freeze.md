# CSF physical fixture and scorer freeze

Status: **FROZEN BEFORE FIRST PHYSICAL EXECUTION**.

Ledger event: v16 #62. Generic-core commit: `22818f9`.

fixture SHA-256: `8c10210b6fee0a5477f3f70593cca080c26a4c91d678ad60bf691f6d853fbd37`

scorer SHA-256: `cedb423ccd201ebd1b0e49a2264c87f6f9e44b70b6f9fc30cba4cb800245aab4`

core SHA-256: `93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4`

The data-only fixture declares:

- two ordered history coordinates bound to one neighboring binary-event
  grammar;
- two incompatible two-phase training contexts, one rich-spectrum training
  context, one rich-spectrum held-out context, and one source-calibrated
  asymmetric control;
- identity, rephase, exchange, and calibration-moving recurrence dictionaries;
- one calibrated port rotation, identical/partial/orthogonal flag vectors and
  branch-specific reconvergence legs;
- one exact `C^2 -> C^3` nonnormal isometry pair;
- restriction, port-refinement, idle-spectator, and catalogue-embedding maps;
- one fixed-factor Bell spectator and an incomplete amplifier control.

The fixture contains no expected result, verdict, outcome, selected kernel,
solution dimension, target witness, or pass count. Its JSON has no float.

The scorer imports the frozen generic core by hash, consumes every declared
anchor, computes Hermitian affine systems and intersections, solves the
exchange-fixed packet, tests the held-out and asymmetric contexts, reconstructs
the JCV base/fiber witnesses, compares calibrated factorizations, evaluates
flags and reconvergence, applies the tangent-support extreme criterion, and
checks fixed-Bob unconditioned no-signalling. It derives the primary from the
pre-registered vocabulary and reconstructs it through a separate comparator.

Thirty-six named mutants are implemented. They attack every load-bearing
object, including history individuation, kernel/channel index orientation,
all-input completeness, PSD, calibrated fibers, JCV embedding, rich-spectrum
cross moments, nonnormal typing, flags, erasure, recurrence dictionaries,
exchange licensing, held-out separation, affine dimensions, uniqueness,
extremality, port refinement, scope walls, exactness, verdict equality, and
gate-to-disk seals.

Static checks only have run: both files parse, the scorer compiles, unknown
arguments exit `2`, scorer and frozen core contain zero float literals, the
fixture contains no float, every declared anchor token exists, and all three
official result paths remain absent. No ordinary solve, selftest, mutant,
classifier, paper render, receipt render, or physical gate has executed.

The next and only ordinary event is the first official scorer invocation. It
must either refuse without artifacts or generate transcript, receipt, and
Paper 6 from one sealed result object. Any refusal is frozen before a bounded
repair is considered.

## First invocation refusal

The first ordinary invocation of the #62 frozen scorer exits `1` at
`CSF-ANCHORS` and writes none of the three reserved result paths. No physical
context equation, affine intersection, classifier, claim, transcript, receipt,
or paper is returned.

Read-only diagnosis finds one failing consumed token. The scorer requests
`erasable` from `v16/paper-03-contextual-pullbacks-permanent-records.md`; the
frozen paper uses the section heading “Records, erasers, and interference” and
the noun `eraser`, but not the adjective `erasable`. Every anchor file hash,
all other consumed tokens, the fixture/scorer freeze hashes, and the core hash
match.

A bounded scorer-only repair may replace that one requested token with the
existing word `eraser`. It may not change the fixture, anchor paths or hashes,
matrix/index conventions, context family, recurrence dictionaries, equations,
gates, mutants, primary vocabulary, claims, renderer, scope walls, or CLI.
The repair must be hash-frozen before another ordinary invocation.
