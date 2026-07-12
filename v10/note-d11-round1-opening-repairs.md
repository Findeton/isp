# D11 round-1 hostile openings and repairs

**Date:** 2026-07-11  
**Round-1 verdicts:** three independent `MAJOR REVISION`.

The reviewers unanimously reproduced the extinction theorem, the 72-history
termination result, and the original executable hashes. They also agreed that
the pre-review headline overreached. This note records every opening and its
disposition before round 2.

## Implemented repairs

1. **Silent packet globals.** `Token.packet` now stores the actual exact
   instrument matrices rather than strings. The root gate compares the stored
   packets to `(K_H,K_T)` and `(P0,P1)` exactly.
2. **Outcome logging versus durable records.** A frozen `DurableOutcome` type
   now stores identifier, record, owner ports, rule, value, effect, and
   terminal/continuing semantics. Terminal seals consume their recorded owner;
   SPLIT, terminal seal, and sibling-merge outcomes are distinctly typed.
3. **Multi-parent provenance.** A live port now stores a tuple of parent ports.
   Sibling-merge outputs retain both parents explicitly and inherit the
   order-unit/frame fields from the recorded shared anchor, not silently from
   the left input.
4. **Unbounded ancestry word.** The redundant growing ancestry string was
   removed from live ports. Provenance stays distributed over immutable
   records. Identifier/capacity and coordinate-shadow compression remain
   open and are no longer claimed closed.
5. **Numerical influence proxy.** `join_transfers` now counts a changed
   downstream `P0/P1` seal probability after merge. A state or coordinate
   difference alone no longer qualifies. The prevalence changes from
   `3,9,5` histories to `1,4,5` across the three rungs; the failure is
   stronger.
6. **Owned exact intervention.** A new exact cell starts from the frozen
   `P0` versus `P+` root intervention, executes the same owned H-SPLIT with a
   fresh `P0` sibling, and verifies that sibling-merge changes the downstream
   seal law.
7. **Algebraic sign certificate.** Positivity ordering in `Q(sqrt(2))` now
   uses rational square comparisons exactly. Decimal arithmetic remains only
   in the external finite-sphere diagnostic.
8. **Selected construction probability.** The two disjoint SPLIT schedules
   now have both canonical-state equality and exact presentation probability
   `1/140`. This closes that cell only.
9. **Hash gates.** Exact and numerical receipts are asserted internally. The
   repaired exact engine has 73 checks and normal/optimized byte-identical
   output.
10. **Terminology.** JOIN is qualified as `sibling-MERGE`; `projective mass`
    is replaced by `finite-prefix mass normalization`; the registered
    `INTERACTION-INERT` label is accompanied by the mechanism diagnosis
    `POPULATION-EXTINCT / INTERACTION-SPARSE`.

## Accepted scope downgrades

1. **Global race remains global.** D11 is a globally normalized sequential
   kernel with incidence-scoped instruments. A decentralized local-clock
   construction and its quotient by auxiliary earliest-event order are not
   proved.
2. **Gauge remains a template.** Dual `SL(2,C)` covariance is exact, but the
   generated history remains in one root frame. No multi-frame generated
   history is compared under vertex-local gauge changes.
3. **Canonical projective pushforward remains open.** One schedule cell and
   per-prefix normalization do not establish the full deletion/pushforward
   theorem over canonical physical histories.
4. **General joining remains open.** Sibling-MERGE cannot connect independent
   components or records that lack a common SPLIT anchor.
5. **Physical spacetime remains open.** Ancestry lies in a declared imported
   positive-coordinate cone by construction. No physical scale, proper time,
   Einstein dynamics, or equality of ancestry/positivity/influence is derived.
6. **ISP implementation remains open.** D11 is Markov on augmented typed
   history. Barandes allows more general indivisible non-Markovian measures
   but does not select this kernel.
7. **COMMIT is not forced.** `SEAL -> COMMIT` is one new primitive candidate.
   Terminal observations, separate birth opportunities, and other
   continuation ontologies remain possible.

## Adjudicated verdict

The pre-review `COMPLETE-KINEMATICS/INFLUENCE-ENVELOPE-OPEN` verdict is
withdrawn. Under the frozen gate definitions, missing integrated history
gauge and canonical projective construction force

```text
INCOMPLETE-PACKET
+ COMPLETE GLOBALLY RACED FINITE-PREFIX KERNEL
+ INCIDENCE-SCOPED EXACT INSTRUMENTS
+ SEPARATE DUAL SL(2,C) COVARIANCE TEMPLATE
+ ALGEBRAIC POSITIVE-CONE CONTAINMENT
+ OWNED SIBLING-INTERACTION WITNESS
+ ALMOST-SURE TERMINAL-SEAL EXTINCTION
- DECENTRALIZED LOCAL CLICK LAW
- GENERATED MULTI-FRAME GAUGE
- CANONICAL PROJECTIVE PUSHFORWARD
- GENERAL BRIDGE/JOIN BIRTH
- PHYSICAL SPACETIME INFLUENCE ENVELOPE
```

The extinction theorem remains D11's strongest result. It falsifies this
global packet as a cosmology without pretending that the final interacting
local record law has been found.
