# D14 focused round-3 mathematics/category review

**Date:** 2026-07-11  
**Reviewer:** independent mathematics/category referee  
**Verdict:** **PASS**  
**Scope:** round-2 blocker C1, with final 42-check artifact reproduction  
**Honest action-level ceiling:** `BRIDGE-CONDITIONAL`

## Decision

The round-2 protected-category blocker is closed.  Protected record identity
is now explicit morphism data rather than occurrence-order convention.  The
correspondence is validated at construction, composed under sequential
gluing, shifted by the correct source and target offsets under tensor, and
transported by the declared wire permutation under symmetry.

I reran the exact counterexamples that failed round 2.  The tensor of an
admitted record-appending morphism with an admitted protected identity now
admits with the correct old-record destinations.  A symmetry exchanging two
distinct protected records admits, and composing it with its inverse restores
both the identity matrix and the identity protected correspondence.  Stronger
probes of tensor associativity and protected symmetry naturality also agree in
their objects, matrices and correspondence maps.

No mathematical blocker remains in C1.  The final concurrent hardening that
includes sealed owned inputs in primitive join admission does not disturb
these results and closes the separate direct-constructor bypass found by the
clean-room stream.

This PASS establishes the protected symmetric-monoidal finite bridge at the
paper's stated supplied-signature scope.  It does not derive the source
category, physical kernels, join-entitlement origin, record instrument or
action-to-record dictionary.  `BRIDGE-CONDITIONAL` remains the maximal honest
action-level grade.

## Frozen final artifacts and reproduction

```text
e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425  code/d14_action_record_bridge_exact.py
37f411d53d0b93313bac1066be71fc7450a92a5b90225c4ad14f17a177397663  data/d14-action-record-bridge-exact.json
fcc213372bb0589150c75a4f3b1eedf3df03413012b776faa3b8dafe5bd94d45  note-d14-finite-action-record-bridge-theorem.md
dc4373773c79c931f06c6f7b518aeb0776e3b38587b00058f45940a7e6da40f1  relativistic-isp-v10-paper15-from-action-to-records-without-a-global-clock.md
f30ecff3a217ed02b7e7bb687f2b5750c3bf7898566ac4b78bb716f0b11c5518  reviews/d14-round2-mathematics-hostile-review.md
```

Independent normal and optimized execution produced:

```text
checks                         = 42/42
stdout SHA-256 normal          = a7c840c55373bb4fc84530c8cd47f48d4ebbaed545581fb784096ef4b01ce830
stdout SHA-256 optimized       = a7c840c55373bb4fc84530c8cd47f48d4ebbaed545581fb784096ef4b01ce830
semantic SHA-256               = a8b22100a104b04069734bd563a8a3f1411e7772dafa1d0062baf019859658c7
reported source SHA-256        = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D13 dependency SHA-256         = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
generated packet SHA-256       = 37f411d53d0b93313bac1066be71fc7450a92a5b90225c4ad14f17a177397663
```

Normal and optimized stdout are byte-identical.  The generated packet agrees
with the frozen packet.  No Python `assert` supplies a gate.

## 1. Constructor invariant

Each `Mor` carries

```text
sealed_map : source protected-port position -> target protected-port position.
```

Construction requires that:

1. every protected source position occurs exactly once;
2. no protected target position is reused;
3. every mapped target is protected;
4. mapped source and target `Port` values agree, including type, dimension,
   owner and persistent `record_id`; and
5. every nonzero matrix entry gives equal pointer labels at the two mapped
   positions.

Thus `sealed_map` is an injective protected-wire continuation, while protected
target ports outside its image are genuinely fresh records.  Owner or record
identity reassignment fails before a morphism is admitted.

Automatic inference is only a convenience for primitives whose continuing
ports are already unambiguous by exact `Port` equality.  The category
operations that move wires supply the map explicitly, so their validity no
longer depends on inference order.

## 2. Closure proof

Write the protected correspondence of `f:S -> T` as `mu_f` and that of
`g:T -> U` as `mu_g`.

### Identity

`ident(S)` assigns `(i,i)` to every protected position.  Its matrix is the
identity, so the protected labels are unchanged.

### Composition

The implementation assigns

```text
mu_(g o f)(i) = mu_g(mu_f(i)).
```

`mu_g` covers every protected source port of `g`, including records freshly
created in `f` and present at the glued boundary.  Hence the displayed
composition is defined for every old protected source of `f`.  Injectivity is
preserved by composition, exact `Port` equality is transitive, and nonzero
matrix paths preserve the label at both stages.  A record created by `f` but
absent from the external source correctly does not appear in the composite's
source correspondence; it remains a fresh protected target.

### Tensor

For `f tensor g`, the implementation takes the disjoint union

```text
mu_f
union
(source_offset + domain(mu_g), target_offset + image(mu_g)).
```

The source offset is the number of source ports of `f`; the independently
required target offset is the number of target ports of `f`.  Consequently a
fresh target record created by `f` cannot steal an old record belonging to the
right tensor factor.  The two images occupy disjoint target blocks, so
injectivity and label preservation survive tensoring.

### Symmetry

`swap_mor(A,B)` sends protected ports of `A` to the right block and protected
ports of `B` to the left block, using the same permutation as its matrix.
This is a bijective transport of protected wires.  The inverse swap restores
the identity correspondence; the hostile naturality probe below also verifies
compatibility with nontrivial record creation.

These definitions close identities, composition, tensor and symmetry on the
admitted protected morphisms.  They repair the exact failure proved in round
2.

## 3. Re-executed round-2 counterexample

I repeated the old construction:

```text
f : q tensor A_record -> q tensor A_record tensor fresh_record
g : B_record -> B_record
```

Both factors admit.  The repaired tensor gives

```text
f.sealed_map              = ((1,1),)
g.sealed_map              = ((0,0),)
(f tensor g).sealed_map   = ((1,1),(2,3))
```

The old `B_record` therefore lands at target position 3, after the fresh
record at position 2.  The occurrence-order implementation had incorrectly
paired it with that fresh record and rejected the tensor.

For two distinct protected records, the repaired symmetry gives

```text
swap(A,B).sealed_map                      = ((0,1),(1,0))
(swap(B,A) o swap(A,B)).sealed_map        = ((0,0),(1,1))
(swap(B,A) o swap(A,B)).amp               = I_4
```

Both formerly failing cases now pass in normal and optimized Python.

## 4. Stronger hostile probes

The built-in exact gate checks protected swap inversion and admission of a
fresh-record tensor.  I additionally inspected the maps themselves and tested
coherence beyond mere admission.

### Tensor associativity with fresh and old records

Using the record-appending `f` above and protected identities `g` and `h`:

```text
((f tensor g) tensor h).sealed_map = ((1,1),(2,3),(3,4))
(f tensor (g tensor h)).sealed_map = ((1,1),(2,3),(3,4))
```

Their source objects, target objects and exact matrices also agree.

### Protected symmetry naturality

For the same nontrivial `f` and `g`, I compared

```text
swap(f.target,g.target) o (f tensor g)
(g tensor f) o swap(f.source,g.source).
```

Both sides have correspondence

```text
((1,2),(2,0))
```

and identical source, target and exact matrix.  This directly exercises a
symmetry in the presence of a newly created protected record.

### Identity reassignment control

An explicitly mapped morphism preserving `record_id="ra"` but changing owner
from `alice` to `bob` is rejected with

```text
ValueError: protected record identity/type mismatch
```

The final executable also rejects a primitive generator joining two differently
owned sealed inputs without entitlement.  Primitive admission now considers
all source ports, sealed as well as live.

## 5. Scope and residual nonblockers

The pure `Mor` protected rule enforces pointer-label permanence.  Physical
unconditional future dynamics still additionally requires the theorem's
branchwise isometry/CPTP completeness hypothesis.  That distinction is stated
correctly in the theorem and paper and is not a C1 defect.

The exact built-in fresh-tensor check currently asserts the length of its
correspondence rather than the expected index pair.  The independent hostile
probe above checked the full map and all stronger coherence equations exactly.
Freezing those full-map equalities in a future executable would improve
regression localization, but their present truth makes this nonblocking.

Likewise, persistent correspondence makes supplied protected morphisms
compose correctly; it does not explain why nature selects a seal, a join
entitlement, a graph-extension grammar or a particular amplitude.  Those are
the already-declared selection problems behind the `BRIDGE-CONDITIONAL`
ceiling.

## Final verdict

**PASS.**  C1 is repaired on the final frozen bytes.  The protected morphisms
now form the claimed symmetric-monoidal finite class under identity,
composition, tensor and declared symmetry, including fresh-record creation.
The old counterexamples reverse from rejection to exact coherent admission,
and no replacement mathematics blocker was found.
