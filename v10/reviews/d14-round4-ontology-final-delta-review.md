# D14 final ontology/locality delta review — round 4

**Date:** 2026-07-11  
**Review verdict:** **PASS AT `BRIDGE-CONDITIONAL` SCOPE**  
**Review scope:** sealed-input ownership admission and final wording only

## Result

The clean-room opening found after the round-3 ontology pass is closed.

Primitive ownership admission now examines **every source port**, including
sealed records.  Two protected records owned by different components can no
longer feed one primitive joint output without the declared owner-list
entitlement.  The rule is enforced by `Mor` itself and therefore also by
`Signature.declare`, which delegates to `Mor`.

The three nonblocking wording hardenings requested in round 3 are also
applied.  Paper 15 now says:

- supplied regional amplitudes **and instruments** realize the record picture
  on a fixed local DAG;
- no preferred total order is required to evaluate or accumulate records
  **within the supplied DAG**, while its generative support/weight law remains
  open; and
- the final arrow is `EVALUATION-ORDER-FREE`, not an unqualified
  `CLOCK-FREE` claim.

No new ontology, locality, Barandes, action-scope or V9-holdout opening was
found.  The entitlement remains supplied grammar rather than derived
connected-collar provenance, exactly as required by the
`BRIDGE-CONDITIONAL` ceiling.

## Exact reproduction

The frozen source and reviewed arithmetic dependency were copied to an
isolated temporary tree and executed under normal and optimized Python.

```text
checks                         = 42/42
normal stdout SHA-256          = a7c840c55373bb4fc84530c8cd47f48d4ebbaed545581fb784096ef4b01ce830
-O stdout SHA-256              = a7c840c55373bb4fc84530c8cd47f48d4ebbaed545581fb784096ef4b01ce830
generated JSON SHA-256         = 37f411d53d0b93313bac1066be71fc7450a92a5b90225c4ad14f17a177397663
primary JSON SHA-256           = 37f411d53d0b93313bac1066be71fc7450a92a5b90225c4ad14f17a177397663
semantic SHA-256               = a8b22100a104b04069734bd563a8a3f1411e7772dafa1d0062baf019859658c7
source SHA-256                 = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
dependency SHA-256             = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

The new check 10 states:

```text
primitive admission includes owned sealed inputs in join entitlement.
```

It passes before the previously reviewed protected-symmetry and owner-
reassignment cells.

## Independent sealed-input probes

Two protected two-level records were declared:

```text
R_A: sealed, owner A, record_id RA
R_B: sealed, owner B, record_id RB.
```

A primitive map retained both records and emitted a joint output.  Without an
entitlement, both admission paths give:

```text
Mor_sealed_unentitled=rejected
  multi-component generator lacks a connected join entitlement

Signature_sealed_unentitled=rejected
  multi-component generator lacks a connected join entitlement.
```

With the supplied owner list, the same map gives:

```text
sealed_entitled=accepted
join_entitlement=('A','B')
sealed_map=((0,0),(1,1)).
```

Thus admission and protected-record preservation coexist: the entitlement
licenses the primitive multi-owner input, while both sealed identities and
values remain persistent.

A second control combined one sealed owner-A record with one ownerless live
input.  It gives:

```text
sealed_owned_plus_ownerless=rejected
  primitive generator mixes owned and ownerless inputs.
```

This verifies that the earlier mixed-input loophole did not reappear when
sealed inputs were added to the owner census.

## Code-path audit

For every primitive `Mor`, the repaired admission now performs:

```text
input_ports = every source port;
declared_owners = every non-null source owner;
owned + ownerless mixture -> reject;
more than one distinct owner -> exact entitlement owner set required.
```

The `derived` path remains reserved for identities, composites, tensors and
structural symmetries assembled from admitted primitives.  This is correct:
tensoring two disjoint admitted morphisms does not itself create a joint
interaction, while any primitive consuming both components must pass the
owner gate.

Record correspondence is unchanged from the round-3 pass.  Persistent IDs
still propagate through composition, tensor and symmetry; owner reassignment
and protected-label overwrite still reject.

## Wording closure

### Action and instrument

Section 1 no longer asks whether an action alone generates records.  It asks
whether **supplied regional amplitudes and instruments** realize the record
picture on a fixed DAG.  This matches the theorem antecedent and preserves the
open autonomous-instrument map.

### Global clock

The theorem summary now says:

```text
No preferred total order is required to evaluate or accumulate records
within the supplied DAG; its generative support/weight law remains open.
```

This is precisely evaluation-schedule gauge, not a claim that D14 derived the
local law generating the DAG or eliminated every possible global mechanism
from a generative theory.

### Final arrow

The concluding schematic now says:

```text
EVALUATION-ORDER-FREE PROJECTIVE NON-MARKOV RECORD HISTORIES.
```

The following paragraph repeats that the packet is supplied and that the
action-to-kernel map, autonomous instrument, diagram law and physical action
are unselected.  The formerly detachable `CLOCK-FREE` overread is closed.

## Scope retained

This delta does not alter the round-3 scientific ceiling:

```text
finite admitted FSDiam evaluation                   proved
sequential protected projective records             proved
one finite visible non-Markov memory realization    proved
primitive multi-owner admission                     enforced
join entitlement origin                             supplied/open
D12-U6 connected-collar provenance                  not derived
diagram/birth/support law                            not derived
action-to-kernel and autonomous instrument maps     not derived
action selection                                    open
V9 cone/dimension holdout                            correctly withheld
```

The generic ownerless finite packet remains a generic circuit witness, not a
D12-U6 locality theorem.  A future physical signature must supply or derive
its ownership and entitlement provenance before receiving that stronger
interpretation.

## Final verdict

**PASS AT `BRIDGE-CONDITIONAL` SCOPE.**  The final sealed-input ownership gap
is closed in both constructor paths, the 42/42 frozen receipt reproduces
exactly, and the clock/action wording now matches the theorem's supplied-DAG
and supplied-instrument antecedents.

No further ontology/locality repair is required for D14's narrowed conditional
bridge.  This remains a finite translation theorem, not the selected final
interactive click law.
