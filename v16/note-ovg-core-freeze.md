# OVG generic exact core freeze

Status: **GENERIC CORE FROZEN BEFORE PHYSICAL FIXTURE**.

Pin commit: `d36b9e5`.

The following generic artifacts are frozen before any OVG physical fixture,
scorer, official result, verdict, output, receipt, or Paper 5 path exists:

| artifact | SHA-256 |
|---|---|
| `v16/code/ovg_core.py` | `7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf` |
| `v16/code/ovg_public_output.txt` | `07f031203ff500af8974cd15c40f8bd752154a3a10ca319951dcbf961f7fff97` |
| `v16/code/ovg_public_receipt.json` | `3cb4153c3685a929b3748aa9862f35bf70e915dba898ec427f6aae9d143b100e` |

The generic engine contains exact `Q(i)` matrix arithmetic with runtime
`Fraction` coercion, typed common-boundary Gram construction, multiport class
operators, all-input completeness residuals, canonical flag dilations,
real-linear rank/nullspace certificates, rewrite critical-pair typing, and a
finite lower-arity factorization enumerator. It contains no OVG physical
fixture, CNOT overlap, AB/BC actor arena, physical coefficient witness, result
word, or Paper 5 classifier.

Nine public calibration gates pass:

- Gaussian-rational multiplication and inversion remain exact at runtime;
- two public isometries produce the full typed Gram family;
- the two parity ports are complete and their stacked flag map is an isometry;
- one, two, and three distinct fourth-root phase rows have exact real-linear
  ranks `1,2,3` and nullities `2,1,0`;
- two unrelated public `C^2 -> C^4` isometries have nonnormal overlap
  `[[0,5/13],[0,0]]`, whose full operator constraint has rank `3`;
- disjoint commuting, joinable overlapping, and one-sided dependency rewrite
  pairs are distinguished before amplitudes; and
- a public target has exactly the reported length-two binary factorization.

These values are constructor-stated calibration answers, not Paper 5 physical
findings.

Two clean temporary-path runs and a copied-source run from `/private/tmp` are
byte-identical. The source compiles and its AST contains zero floating-point
literals. Unknown arguments exit `2`. `--selftest` and each of the public
mutants `public-gram`, `public-parity`, and `public-rank` exit `1` before
writing any artifact.

The core is now byte-immutable. The next lawful event is a separately frozen
data-only physical fixture and verdict-neutral scorer. They may import the
core only at this hash, and must not edit it.
