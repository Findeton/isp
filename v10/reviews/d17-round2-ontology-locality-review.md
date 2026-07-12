# D17 round-2 ontology/locality hostile review

**Date:** 2026-07-11  
**Referee stream:** ontology, locality, causal-extension scope  
**Formal D17 verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Narrow fixed-action nonselection subresult:** **ACCEPTED WITH A STRICT SCOPE CEILING**

## Decision

The round-1 repairs are real.  The executable now keeps a supplied boundary
envelope, an orbit square-root factor and the fixed action phase as distinct
arguments; uses a positive-support second packet; propagates an
inverse-automorphism factor through the D14 seal; checks normalized projective
mark cylinders through depth six; and imports the reviewed D14 carried-memory
and CPTP-reset construction.  Normal and optimized execution reproduce all
26 checks and every frozen hash.

The strongest defensible result is therefore:

> On a frozen two-alternative finite carrier, a fixed phase function and a
> fixed supplied record isometry are compatible with more than one positive
> boundary/orbit probability packet and more than one supplied projective
> mark-cylinder family.  Consequently the phase action alone does not select
> those additional data.

That is a sound nonselection theorem.  It is not yet the requested interacting
click law.  The repaired source contains three mathematically valid but
unconnected witnesses:

1. a size-four `chain4/diamond4` phase-and-record cell;
2. a root/chain/antichain/chain3/V3 collection of one-element order
   extensions; and
3. an `X,M,Y,Z` finite circuit that transports and resets one memory bit.

No typed construction identifies the D14 live carrier or memory with a
boundary/collar of the causal orders, maps the mark cylinders to order nodes,
or makes the fixed action weight their extensions.  Thus the code proves
compatibility and nonselection of supplied data, not a causal-history record
measure generated locally from the action.

The theorem and receipt mostly respect this ceiling.  Their explicit formal
status `INCOMPLETE-INVESTIGATION`, and their statements that the commit,
extension weights and continuation are supplied, must remain.  They should be
tightened further: a typed extension **grammar** is currently absent rather
than supplied, and the executable label “complete recorded history laws” is
too broad.

## Reproduction

I copied only D13, D14, D16 and D17 into a clean `/tmp` tree and ran D17 in
ordinary and optimized Python modes.  Both modes pass `26/26`, produce
byte-identical stdout, and regenerate a packet byte-identical to the primary
packet.

```text
checks                    26/26 normal and -O
source SHA-256             305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
packet SHA-256             15cfd44534c4b7de4d66e834a318a00eb666cfaffe7dccb86bc45c2891563cfe
semantic SHA-256           a5d2cb4dd4b7b065430bcb4aedc7c88daddf1df1ad84c970f1ae3b78cd7ee525
normal/-O stdout SHA-256   bf5a54311daf639d612857c36cd40acc637f9a4246bd1cdecb816fa74b80b306
D14 dependency             e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16 dependency             861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
```

The explicit `check` function, final count guard and semantic-hash guard are
not removed by `-O`.  The packet is written only after those gates.  The
receipt hashes and its `26/26` statement are exact.

## Finding ledger

```text
O1 MAJOR    The action/record cell, causal-extension examples and local-memory
            circuit remain separate witnesses; no integrated causal-history
            record packet exists.
O2 MAJOR    Check 18 does not realize the depth-1-to-3 tower as causal orders.
            It checks only two induced-order extension steps and supplies no
            history-to-order map or truncation map.
O3 MAJOR    Ext(C), typed collars, ownership and join admission are absent.
            No forbidden extension or unowned join is rejected in D17.
O4 MODERATE The record map is local only at D14's abstract single-owner cell:
            its input is a predeclared global two-order alternative.  The
            physical local interaction that makes that alternative readable
            remains supplied.
O5 MODERATE Orbit factors reach one finite D14 record, but not either
            projective tower or the local-memory continuation.
O6 MODERATE The source still calls a supplied mark-cylinder family a
            “complete recorded history law”; the all-depth rule is complete
            only for those marks, not for causal-order growth.
O7 MINOR    The before/after erasure numbers are correct on the sealed image,
            but “the same effect” is not represented as one typed operator and
            its lifted operator; it is implemented by two specialized helper
            formulas.
O8 PASS     The positive second packet closes the null-conditioning opening.
O9 PASS     The local D14 memory/reset witness no longer reads a universe
            ledger and the reset changes the later visible law exactly.
O10 PASS    Commit, weights and continuation are not claimed action-derived;
            no clock, geometry, scale, G or V9 holdout conclusion is claimed.
```

## 1. Action, state and orbit data

### Factor separation is repaired

`amplitudes(boundary_envelope, orbit_sqrt, phases)` explicitly multiplies
three separately passed factors.  The equal packet uses

```text
boundary envelope  (1/sqrt(2), 1/sqrt(2))
orbit factor       (1, 1)
action phases      (-1, +1)
final amplitude    (-1/sqrt(2), +1/sqrt(2)).
```

The second packet changes only the envelope to `(3/5,4/5)`, yielding final
amplitudes `(-3/5,+4/5)` and recorded probabilities `(9/25,16/25)`.  Both
components are positive in probability, so the two past-conditioned events
used by the non-Markov comparison remain non-null in both towers.  This is the
right repair to round 1.

The variables `equal_boundary_state` and `second_boundary_state` are still
misnamed: they contain the action phases and are final amplitudes, not merely
`Psi_boundary`.  That naming defect no longer conflates the computation,
because the factors are independently present at the call site.

### Orbit propagation is finite but genuine

The exact automorphism counts are one for the chain and two for the diamond.
The two candidate normalized orbit conventions are therefore

```text
uniform unlabeled              (1/2, 1/2)
normalized inverse-|Aut|       (2/3, 1/3).
```

The source implements the inverse-automorphism ratio with raw square-root
factors `(1,1/sqrt(2))`, sends the resulting amplitudes through the same D14
seal, and normalizes the record probabilities to `(2/3,1/3)`.  Using raw
rather than normalized square roots is harmless here because the common total
is divided out after the seal.  The orbit ratio really does reach the record;
it is no longer only a paper comparison.

Two ceilings remain:

- H1 asks for labeled and unlabeled sums to agree under one explicit groupoid
  convention.  D17 compares two candidate unlabeled conventions but does not
  construct that labeled/unlabeled equality.
- The orbit-weighted packet stops at the finite record.  Neither
  `tower_equal` nor `tower_second` is built from `inverse_aut`; the local
  memory circuit is also fixed at half-half.  Orbit **record** nonselection is
  demonstrated, not end-to-end orbit-weighted causal-history continuation.

These limitations do not damage the logical point that the phase action does
not choose an orbit convention.  They prevent an H0-H6-complete orbit packet.

## 2. Local record and interference/erasure observable

The repaired `record_seal()` has one abstract owner, `history-cell`, on its
source system, sealed record and collar.  Its isometry maps

```text
|0> -> |system=0, record=0, collar=1>
|1> -> |system=1, record=1, collar=1>.
```

Thus it neither mixes disconnected owners nor reads a universe ledger.  The
record labels are orthogonal, every branch emits a live collar, and the
reviewed D14 protected-future rule preserves the record.  At the abstract
finite-cell level, locality, sealing and durability pass.

For the equal unrecorded state, the `+`/erasure effect has probability

```math
|(-1/\sqrt 2+1/\sqrt 2)/\sqrt 2|^2=0.
```

After the record has made the alternatives orthogonal, the corresponding
system effect with the record ignored has probability

```math
\tfrac12\left(\tfrac12+\tfrac12\right)=\tfrac12.
```

The source returns exactly `0` and `1/2`, so the old scalar-cancellation-only
opening is closed.  On the image of this seal,
`recorded_erasure_probability()` is exactly the expectation of the system
`|+><+|` effect tensored with identities on record and collar.

The helper does not construct those two operators and prove the tensor lift;
it uses a two-component sum before the seal and selected-coordinate norms
after it.  Therefore “same effect” is verified by source inspection on the
frozen image rather than frozen as a general operator identity.  This is a
minor receipt weakness, not a numerical failure.

The more important ontology ceiling is the seal's input.  The basis label
`causal-alternative` is declared to mean the completed global alternatives
`chain4` and `diamond4`.  No local collar observable or interaction derives
that bit from subregional order data.  The map is local **conditional on the
two-valued carrier having already been supplied at the history cell**.  It is
not a derivation of how a local environment learns which completed universe
order occurred.  The theorem's language that the D14 isometry “copies the
alternative” is acceptable only with that conditional reading.

## 3. The causal-extension claim does not yet match the tower

`is_one_element_extension(parent,child)` correctly checks two facts:

1. the child has exactly one additional element; and
2. the old labeled relation is the child's upper-left induced suborder.

Because `CausalOrder` separately validates strict transitive closure, the four
individual extension statements tested in check 18 are genuine labeled
one-element order extensions:

```text
root1  -> chain2
root1  -> anti2
chain2 -> chain3
anti2  -> vee3.
```

This is useful evidence that causal-order growth can carry a binary branch.
It does **not** realize `projective_tower()` as a causal-order tower.

The mismatch is exact.  If depth one is the first extension from the root,
then

```text
P1: (0),(1)        can map to chain2,anti2
P2: (0,0),(1,0)    can map to chain3,vee3
P3: (0,0,0),(1,0,1) has no supplied size-four children.
```

If instead `root1` is called level one, then the probability table already
has two level-one nodes while the causal construction has only one root.  No
indexing convention makes all three displayed probability levels coincide
with the supplied causal orders.

The code supplies no function

```text
history marks -> CausalOrder,
pi(child) -> parent,
Ext(C) -> admitted typed children,
```

and evaluates the fixed action on none of the extension nodes.  Check 18's
label, “projective branches are realized by actual one-element causal-order
extensions,” therefore overstates its predicate.  The defensible statement is
that **the first two transitions of a possible two-branch causal growth tree
have example one-element extensions**.

At depths four through six, and in the claimed all-depth continuation, the
probability helper simply appends mark `0`.  It constructs no further causal
order at all.  The induction proves projectivity of the sparse mark strings,
not existence or admissibility of an all-depth causal extension.

## 4. Extension grammar, ownership and joins remain open

The D17 protocol requires `Ext(C)` with typed collars, ownership and join
entitlements, plus a rejecting unowned-extension control.  None appears in
the repaired D17 source.

The four causal examples have empty D16 boundary lists.  The permissive
predicate accepts any valid one-element induced-order extension and does not
ask:

- which future collar owns the new element;
- what local data may determine its relations;
- whether two components may be joined;
- whether the new element is born locally or attached across disconnected
  support;
- which alternatives are forbidden; or
- which weights belong to the admitted alternatives.

D14 contains an owner/join-entitlement admission layer and D16 contains typed
boundary gluing, but D17 invokes neither for its extension examples.  No
forbidden extension or unowned join is attempted and rejected.

Accordingly, the final theorem paragraph should not imply that a complete
extension grammar has merely been supplied.  What is present is:

```text
four hard-coded extension examples              supplied
two branch weights                              supplied
one mark-level deterministic continuation       supplied
typed Ext(C)/ownership/join grammar              absent
action-derived choice among extensions           absent
```

This is the central remaining construction-law opening.

## 5. Local carried memory and reset

The imported D14 packet is a real repair of the universe-ledger defect.  It
uses four finite carriers ordered as `X,M,Y,Z`:

1. a local CNOT copies `X` into memory `M`;
2. visible records of `X` and then fixed `Y=0` are sealed;
3. a later local CNOT copies `M` into `Z`; and
4. `Z` is sealed.

With the supplied mixture of `X=0` and `X=1`, the exact record support is

```text
000 with probability 1/2,
101 with probability 1/2.
```

The next visible record therefore differs for two positive pasts having the
same current visible record `Y=0`.  The code does not inspect a history tuple
to decide `Z`; the needed bit is physically carried in `M` through the finite
circuit.

The two reset Kraus operators erase only `M`, preserve `X,Y,Z`, and are known
from the hash-pinned reviewed D14 source to satisfy exact CPTP completeness.
Applying the reset before the final copy makes both branches end at `Z=0`.
D17 checks the final exact density matrix.  The dependence is therefore
caused by the carried memory, not merely correlated with a ledger key.

This passes the finite **local-memory compatibility witness** and deletion
countercontrol.  D17 does not, however, connect `M` to a D16 causal boundary,
an extension collar, or the `chain4/diamond4` action.  The D14 ports used by
`integrated_memory_history_tables()` have no owner labels, and the packet is
called independently of the causal-order objects.  Therefore H6's phrase
“one integrated causal-history/record packet” remains only partial in D17,
even though the memory circuit itself is valid and local in the finite-circuit
sense.

## 6. Positive projective packets and nonselection

For arbitrary positive weights `w0+w1=1`, `projective_tower()` supplies

```text
P1: 0 -> w0,       1 -> w1
P2: 00 -> w0,      10 -> w1
P3: 000 -> w0,     101 -> w1
Pn+1: append 0 uniquely for every n >= 3.
```

Every stored level is normalized.  Every parent's unique child has the same
mass, so the parent-cylinder equation holds.  The source tests depths one
through six; the displayed unique-child rule gives an immediate all-finite-
depth induction for this mark alphabet.  The independently normalized control
correctly fails projectivity.

The equal tower uses `(w0,w1)=(1/2,1/2)` and the second uses
`(9/25,16/25)`.  Both weights are positive.  Consequently both have the same
well-defined non-Markov conditionals

```text
P(z=1 | x=1,y=0)=1,
P(z=1 | x=0,y=0)=0,
```

while assigning different probabilities to the recorded complete marks.
This closes the round-1 H7 null-event opening.

The logical nonselection conclusion is sound even though these are supplied
mark laws: the same fixed phase action does not mathematically determine which
positive envelope or which compatible projective cylinder weights must be
used.  Indeed, the construction deliberately demonstrates that additional
data can vary while the action stays fixed.

What it cannot establish is that either tower is a causal-order measure
generated by that action.  The fixed phases are computed only on the separate
size-four pair.  No action phase, transfer amplitude, normalization or local
extension kernel appears inside `projective_tower()`.  “Compatible with the
action” here means “not contradicted by anything in the supplied action,” not
“obtained from an action-governed causal growth process.”

Source check 20 says the fixed action supports “distinct complete recorded
history laws.”  The semantic packet is more careful: its scope is “two finite
unlabeled causal alternatives; supplied D14 record/towers,” and its ceiling is
“record instrument and projective towers supplied, not action-derived.”  The
check label should be narrowed to “distinct supplied projective mark-cylinder
families.”

## 7. Commit, weights, continuation and claim scope

The following data are not selected by the action and must remain visibly on
the supplied side of every theorem statement:

| Datum | What D17 contains | Status |
|---|---|---|
| Boundary/preparation envelope | equal and `(3/5,4/5)` examples | supplied |
| Orbit convention | uniform and inverse-automorphism candidates | supplied |
| Record commit | one D14 copy isometry | supplied |
| Extension examples | four one-element labeled-order relations | supplied |
| Extension weights | two persistent branch weights | supplied |
| Continuation | append-zero mark rule | supplied |
| Typed extension grammar | no `Ext(C)` object or rejection control | absent |
| Join rule | no owner/entitlement test in D17 extension path | absent |
| Local action-governed sampler | none | absent |
| Proper-time/clock law | none | absent |
| Geometry, dimension, scale, `G` | none | absent |

The theorem's final paragraph correctly labels formal D17
`INCOMPLETE-INVESTIGATION` and explicitly says no BDG quantum packet,
geometry, scale, `G` or empirical holdout is present.  The protocol also says
whole-history consistency is not a sequential sampler or physical proper
time, and keeps the V9 holdout closed.  I found no hidden geometry claim in the
code, JSON or receipt.

The source semantic verdict `CAUSAL-ACTION-TO-MEASURE-NONSELECTION` is
acceptable only as the candidate finite subresult described above.  It must
not be read as `CAUSAL-ACTION-TO-PROJECTIVE-RECORD-MEASURE-DERIVED` or as the
final dynamic interacting click law.

## Gate disposition

```text
H0  PASS/PARTIAL  factors are separate at construction; final amplitude names
                  remain imprecise.
H1  PARTIAL       orbit ratio propagates through one seal; no labeled/unlabeled
                  groupoid equality or orbit-weighted tower.
H2  PASS          for one supplied single-owner D14 record cell and frozen
                  erasure effect; physical origin of the alternative carrier
                  remains supplied.
H3  PASS          Born weights are taken once from the sealed amplitudes.
H4  PASS/PARTIAL  exact recorded partition is positive and normalized; full D
                  is still implicit rather than a receipt field.
H5  PASS           for supplied mark cylinders and their unique-child
                  induction; FAIL as a causal-order extension tower.
H6  PASS           for the finite local D14 memory/reset witness; PARTIAL as an
                  integrated causal-order/action/record packet.
H7  PASS           narrow positive-support boundary-state nonselection; orbit
                  nonselection reaches a record but not an H0-H6 tower.
H8  FAIL           typed Ext(C), ownership, collars, joins and rejection are
                  absent.
H9  PASS           no sampler, global clock or proper-time derivation claimed.
H10 OPEN/HONEST    no geometry, scale, G or V9 holdout claim.
H11 OPEN           the formal thread cannot close while H5-causal/H8 and the
                  integration map remain absent.
```

## Required next repair

Do not add more disconnected examples.  The next executable must define one
shared typed object in which:

1. each probability-cylinder node is an actual causal order with a declared
   boundary/collar;
2. `pi` and `Ext(C)` are executable and every admitted child has an owner;
3. a forbidden extension and an unentitled cross-component join reject;
4. the D14 memory carrier is part of that parent's local boundary, not a
   separate four-bit circuit;
5. the commit is a local morphism on that boundary and emits the child's live
   collar;
6. extension weights and continuation are explicit supplied kernel data;
7. two positive kernels remain possible for the same action, preserving the
   nonselection theorem; and
8. no geometry or proper-time conclusion is drawn until a further selection
   principle fixes one kernel independently.

That construction would convert the present compatibility witnesses into one
locally generative causal-history packet.  It would still prove
nonselection—not an action-derived law—unless an additional theorem or
independent physical principle uniquely fixes the supplied kernel.

## Final verdict

**MAJOR REVISION — `INCOMPLETE-INVESTIGATION`.**  Accept the exact narrow
subresult that a fixed finite action does not select the boundary/orbit packet
or supplied projective mark law.  Accept the local finite record,
interference-change, carried-memory and reset witnesses at their conditional
scope.  Do not accept the present tower as an actual causal-extension history
measure, an extension grammar, a locally generated universe law, a proper-time
law or a geometry bridge.
