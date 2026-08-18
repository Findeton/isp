# SRW generic exact core freeze

Status: **GENERIC CORE FROZEN BEFORE PHYSICAL FIXTURE**.

Pin commit: `96ba84e`.

The following generic artifacts are frozen before any SRW physical fixture,
scorer, result, verdict, output, receipt, or Paper 4 result path exists:

| artifact | SHA-256 |
|---|---|
| `v16/code/srw_core.py` | `783f71589b2c1d9cee3b20ccf864ae372b480affcf6df4a4181befd5b55f0137` |
| `v16/code/srw_public_output.txt` | `824bfca1b5ae9007fc1cdccc100c0219a6a2759e14173750ea758b773500668f` |
| `v16/code/srw_public_receipt.json` | `e11c38f812e004d8bdc9056ed80bf7ca8d51cdb27cc0d2c8cd6571e8e8a74be7` |

The public calibration uses unrelated labels and the rational circle point
`(5/13,12/13)`. It contains no Paper 3 matrix, graph name, physical outcome,
expected dictionary, result classifier, or SRW verdict.

Twelve exact public gates pass. They calibrate:

- rational and Gaussian-rational matrix arithmetic;
- an isometric two-to-three growth map;
- kinematically allowed support versus a proper actual-support subset at a
  zero-coupling endpoint;
- exhaustive anonymous dictionary enumeration and a separately applied
  graph-local future probe;
- computed dimensions for one-excitation, internal-multiplicity,
  port-stabilized, and edge-sector fibers;
- internal-degree blindness followed by explicit reactivation;
- independent-angle normalization and reciprocal reconvergence; and
- the complete fourth-root phase census: 64 connections form four gauge
  orbits of size 16, classified by holonomy, with screen values
  `1,1/2,0,1/2`.

The counts above are generated from the declared finite objects. They are
public instrument calibrations, not SRW physical findings.

Two generated runs, including a copied-source alien-directory run, are byte-
identical. The source compiles, its AST contains zero floating-point literals,
unknown arguments exit 2, and `--selftest` corrupts the circle anchor and
refuses without writes. The three public mutants `public-circle`,
`public-support-equality`, and `public-dictionary-drop` each exit 1 before
writing.

The core is now byte-immutable. The next event is one separately frozen,
data-only physical fixture and verdict-neutral scorer. The physical fixture
must contain no expected, result, verdict, or outcome field, and the scorer
must not edit this generic source.
