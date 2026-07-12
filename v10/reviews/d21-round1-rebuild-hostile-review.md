# D21 round-1 clean-room-style rebuild audit

**Status:** internal reconstruction audit, not an external independent review.

## Procedure

1. Read the protocol before the manuscript conclusion.
2. Reconstructed the two nonzero density-matrix blocks and the Pauli
   predictions by hand.
3. Ran the standard-library executable under normal and optimized Python.
4. Checked that source and generated receipt remain under `v10/`.
5. Compared the reported scope with the actual executable carrier.

## Result

Both runtimes pass the same `40/40` exact checks and print the same semantic
hash after final freezing.  The executable has no third-party imports.  The
carrier is exactly three qubits with `X/Y/Z` PVMs; it does not contain a hidden
graph builder, V9 geometry input or external data file.

## Hostile boundary

The executable establishes complete probabilities and conditionals only for
the printed finite intervention alphabet.  It does not establish experimental
error models, relativistic flashes, a continuum limit or cosmological
completeness.

**Verdict:** REBUILD PASS at declared scope.

