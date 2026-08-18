# SRW physical fixture and scorer freeze

Status: **FROZEN BEFORE FIRST PHYSICAL EXECUTION**.

Immutable generic-core commit: `caaf9f7`.

| artifact | SHA-256 |
|---|---|
| `v16/code/srw_fixture.json` | `e40650f04c60635e68fd91938dbba201afec6e426c2e1cfaa0b4f4d8dcefd2e3` |
| `v16/code/srw_score.py` | `475aee9509b02c5c77d6d9535605c440ef0ff513627fbbadb3bcdee1f43bf20f` |
| frozen generic core | `783f71589b2c1d9cee3b20ccf864ae372b480affcf6df4a4181befd5b55f0137` |

The JSON fixture is data-only. A recursive key scan finds no key containing
`expected`, `result`, `verdict`, or `outcome`. The physical output, receipt,
and Paper 4 result paths are absent. The scorer has not been invoked on this
fixture.

The fixture declares:

- the inherited anonymous `Vgrow`, `Ualpha`, `Ubeta`, `R`, and `J` matrices;
- an independently named source graph, target graph, boundary port, rewrite
  span, persistence map, created vertex, alternate ancestry span, and allowed
  entry grammar;
- all anonymous source and target labels required for the exhaustive
  dictionary census;
- a five-row rational circle family including both zero-coupling endpoints;
- four fiber specifications: vertex one-excitation, an internal-bit lift,
  port stabilization, and edge excitation;
- separately typed growth, eraser/recombiner, and recorded-successor
  occurrences for the coupling census; and
- the fourth-root phase group and a directed three-cycle.

The scorer imports but cannot edit the frozen generic core. It anchors the
fixture, pin, core, Paper 3 fixture, and Paper 3 receipt; reconstructs the
registered inherited identities; separates support filtering from future
discrimination; computes the carrier dimensions; solves the independent-angle
grid and reciprocity locus; exhausts the phase gauge; and renders the
transcript, receipt, and candidate paper from one in-memory object.

Static compilation with warnings promoted to errors passes. AST scans find no
floating-point literal. The CLI lists 26 registered mutants and rejects an
unknown flag with exit 2. No selftest, mutant, or ordinary physical solve has
run. The next and only event is the first official ordinary invocation. A
failure must be frozen before any repair; a success must be committed as-is
before replay or interpretation changes.
