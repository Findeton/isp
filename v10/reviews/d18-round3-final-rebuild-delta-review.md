# D18 round-3 final clean-room delta review

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-12  
**Verdict:** **PASS — FINAL AT THE FINITE/CYLINDER SUFFICIENCY SCOPE**

Round three changes no executable mathematics.  The only source edit is the
module docstring, which now states the operational/generator/interpretation
separation correctly.  All 30 checks, semantic fields, constants, functions
and dependency bytes are unchanged.  Normal and optimized execution reproduce
the new frozen receipt exactly.

The theorem also incorporates the round-two operational-equivalence ceiling
accurately: distinct complex decoherence matrices can agree on every subset
quantum measure and every licensed decoherent-partition probability, so D18
proves finite sufficiency rather than literal minimality or uniqueness of the
`(E,D)` representation.

## 1. Exact source-delta proof

The current docstring says, in substance:

```text
typed E plus normalized strongly-positive D is sufficient;
record semantics and units form an interpretation layer;
action/state/measure/instrument data form an explanatory generator;
physical interventions must be distinguished from factorization gauge.
```

I replaced only that docstring in memory with the round-two wording.  The
resulting byte digest is:

```text
99e0b696bb1c39374a4b366a4c07fc72f3b9dffae38850d70292c9e64947032f
```

which is exactly the reviewed round-two source hash.  Therefore every byte
after the docstring is unchanged.  The new source hash is:

```text
010c68757d259badab81667f1ff04c549e87aa32448027d884679ad864bc61b4
```

The edit is scientifically appropriate.  It removes the former implication
that coarse maps and units are additional inputs to dimensionless operational
probabilities after `D` is supplied, and it no longer calls factorization
redundancy physical generator nonuniqueness.

## 2. Reproduction and hashes

The following were repeated:

```bash
python3 v10/code/d18_minimal_history_rulebook_exact.py
python3 -O v10/code/d18_minimal_history_rulebook_exact.py
python3 v10/code/d18_minimal_history_rulebook_exact.py | shasum -a 256
python3 -O v10/code/d18_minimal_history_rulebook_exact.py | shasum -a 256
shasum -a 256 v10/code/d18_minimal_history_rulebook_exact.py
shasum -a 256 v10/data/d18-minimal-history-rulebook-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 30/30
SEMANTIC SHA256: e92b39b7308e6e51887ef073430e86608e96de863874fcf46b217f1d5d5dc779
SOURCE SHA256: 010c68757d259badab81667f1ff04c549e87aa32448027d884679ad864bc61b4
VERDICT: FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY
```

Normal and `-O` stdout hashes are identical:

```text
8010279a8bc98f18ce5e5457d409d553b9c7874763797c8ce982b2f8adb1b1b6
```

The remaining frozen hashes match:

```text
packet          fb0e70c1d2701c69dd17b20b9b40237de756e6393289b63dfbe9e3db93c3cf3a
integrated D17  5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57
semantic        e92b39b7308e6e51887ef073430e86608e96de863874fcf46b217f1d5d5dc779
```

The packet changed only because its receipt-bearing `source_sha256` field
changed.  The semantic digest is identical to round two.

As a second delta control, I replaced only the newly printed source hash in
the current stdout with the old source hash.  The reconstructed stdout digest
is:

```text
04ffee18f1ea2c99599e99b47faef1ee1ce24c0e6cf371a7606cdad0e37aa455
```

exactly the round-two stdout hash.  Thus no PASS label, check order, numerical
result, semantic value or verdict line changed.

## 3. Operational-equivalence ceiling

The theorem now explicitly states that `(E,D)` is not proved minimal modulo
every operational equivalence.  This matches the clean-room counterexample:

```text
D+ = [[1/2, +i/4],[-i/4,1/2]],
D- = [[1/2, -i/4],[+i/4,1/2]].
```

Both matrices are:

- Hermitian;
- normalized by `D(Omega,Omega)=1`;
- strongly positive, with eigenvalues `1/4` and `3/4`;
- distinct as complex matrices.

Yet on the two-history Boolean event algebra both give:

```text
mu(empty)=0,
mu({0})=mu({1})=1/2,
mu({0,1})=1.
```

They also have the same exact decoherence classification: the one-block
partition decoheres, while the singleton partition does not.  Therefore every
licensed classical partition probability agrees.

The added prose draws the correct conclusion: either quotient decoherence
functionals by the declared operational equivalence or enlarge the experiment
class with phase-sensitive composition/interventions.  It does not use this
ceiling to weaken the finite sufficiency theorem.

## 4. Final scope

The accepted D18 statement remains:

> On a finite typed event algebra, a normalized strongly-positive
> decoherence functional, together with a supplied decoherent event question,
> determines every licensed probability and conditional without a second
> click lottery.

The following remain outside the result:

- literal minimality or uniqueness of the operational representation;
- selection of the physical generator, state, measure or record instrument;
- extension of a quantum cylinder functional to the full sigma algebra;
- alternate-filtration equivalence, continuum geometry, units or `G`;
- the final action-derived interacting click law.

The manuscript and semantic ceiling preserve all of these exclusions.

## 5. Editorial metadata

The theorem status line still says “awaiting round-2 review,” and the receipt
status likewise names round two.  Those are stale workflow labels only; they
do not affect source, packet or theorem content.  They should be updated when
the review bundle is finalized.

## 6. Decision

**PASS `FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY` at finite/cylinder scope.**
The executable delta is docstring-only, all new hashes reproduce, and the
operational-equivalence ceiling is incorporated exactly at the strength
supported by the `D+ / D-` counterexample.
