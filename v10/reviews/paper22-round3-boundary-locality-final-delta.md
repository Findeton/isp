# Paper 22 round 3 — boundary/locality narrow final delta

**Frozen target:** commit
`a074608ebbc012ac6bd564d51757c6e009688124`.

**Comparison base:** repaired paper candidate `8e820cc` and
`paper22-round2-boundary-locality-closing-delta.md`.

**Exact verdict:** **NARROW DELTA CLEAN — 0 BLOCKER / 0 MAJOR / 0 MINOR /
0 NIT.**

This review checks only the exact repaired manuscript, the explicit validator
ceiling, the genuine-projection composition scope and preservation of the
already accepted boundary/locality claims.  No scientific rerun was required.

## 1. Exact paper artifact

The frozen manuscript hash is exactly:

```text
e33c0ad9294ff1411f49e7d32dc640c9047d3a7603e954219703f23031bf8576
```

This matches the candidate hash pinned in the commit ledger and terminal note.
`git diff --check` is clean.

The underlying executable and output are unchanged from the accepted closing
delta and retain hashes:

```text
code    1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5
stdout  158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7
```

No code or data file differs between `8e820cc` and `a074608`.

## 2. Validator ceiling is now explicit

The repaired paper states:

> The validator certifies these declared invariants on the composition
> interface; it is not a complete recognizer for whether an arbitrary
> fabricated history is reachable under D34b.

That is the exact ceiling established by the prior hostile campaign.  The
validator checks ownership, canonical event IDs/ordinals, internal predecessor
visibility, visible acyclicity, actor counters, carrier parity, degree/ports
and maximal tips.  It does not replay the click law, authenticate a message or
decide arbitrary generative reachability.  The manuscript no longer permits
the stronger reading.

## 3. Typed-union theorem retains the correct input class

The following sentence immediately fixes the theorem domain:

> The composition theorem is the typed-union identity on genuine regional
> projections.

Thus the theorem remains

```text
compose(M_R(h), M_S(h)) = M_(R union S)(h)
```

for messages projected from one legal D34b configuration `h`.  It does not
assert that every dictionary accepted by the defensive validator is a
reachable history.  This exactly incorporates the four beyond-scope fabricated
histories documented in the round-2 boundary review without weakening the
`159,734/159,734` genuine composition result or B4 sufficiency.

## 4. Bibliography-only repair leaves the science unchanged

Relative to `8e820cc`, the manuscript changes only:

1. its status line;
2. the explicit validator/composition scope paragraph; and
3. the two frozen bibliography metadata substitutions.

The corrected entries now carry:

```text
Shalizi--Crutchfield DOI  10.1023/A:1010388907793
Geiger--Temmel            Journal of Applied Probability 51(4), 1114--1132
```

Neither reference is a proof dependency.  No theorem statement, boundary
generator, probability, capacity ledger, stopping scope, outcome row or claim
ceiling changed.

In particular, the already accepted physical wording remains intact:

- “local” means actor-graph read/write scope, not bounded memory;
- B3 is distributed and has unbounded width;
- the Python receipt is not a hardware-actor implementation;
- construction time and elapsed stopping time are not Einstein proper time;
- construction-order covariance is not Lorentz covariance;
- fixed global event depth is not a regional stopping rule;
- B4 is a sufficient growing component ceiling, not necessary; and
- no light cone, dimension, `G` or universe click law is inferred.

## 5. Final disposition

The bibliography repair and explicit validator ceiling introduce no new
boundary/locality issue.  The defensible endpoint remains:

> For the chosen passive D34b law, the distributed unbounded B3 star is an
> exact all-future sufficient C/L carrier at the licensed stops; every complete
> fixed actor radius fails the declared F query; and the complete component is
> a sufficient growing F ceiling.  Typed composition is proved on genuine
> regional projections, while the validator is only a checker of the declared
> interface/history invariants.

**Final count: 0B / 0M / 0m / 0n.  Boundary/locality final delta terminal.**
