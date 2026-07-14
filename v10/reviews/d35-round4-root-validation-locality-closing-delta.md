# D35 round 4 — root-validation and locality closing delta

**Frozen target:** commit
`d414c56de480fd692630c1d7b3b10ada44cb60f7`.

**Lane:** root-input fail-closed behavior, complete rejection-state
preservation, typed actor ownership, generated-birth continuity, serializer
gauge, grown replay and preservation of the A-rooted/shared-joint scope.

**Verdict:** **TERMINAL LOCALITY DELTA ACCEPTED.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

D35d closes the sole round-3 locality minor. The typed-identity replacement
also preserves the actor-ownership and scheduler properties already accepted
for D35c. It does not change the scientific object from a supplied A-rooted
laminar family into a root-free or independently distributed law.

## 1. Exact reproduction

Fresh runs under `PYTHONHASHSEED=104729` and `1299709` exited zero, were
byte-identical to each other and to the committed receipt, and printed `PASS
18/18`.

```text
source SHA-256
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

stdout SHA-256
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574

internal science SHA-256
79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c

D35 note SHA-256
d9f4367c0de815f693f1fe14dd06eb7bae053572a12ea4dd80a6115c3cf08936
```

Both `git diff --check d414c56^ d414c56` and `git diff --check de51b4e
d414c56` are clean.

Per Q1/Q2, the reproduced receipt contains:

```text
first histories/physical atoms                 16/16
FIFO/LIFO/canonical totals                       1/1
ordinary renamed projectivity             16/408/408
typed-collision projectivity               16/408/408
late collision continuation                       6/6
rejections and whole-state snapshots              6/6
rejected envelope retained                         1/1
inherited adversarial regression                    9/9
grown serializer checks                              32
multi-call replay                                      8
root-owned ordinal after replay                        8
```

## 2. Root bit validation precedes model-state mutation — pass

The public D35d `start_root_call` first evaluates membership in the admitted
bit alphabet and raises for a non-bit value. Only after this check succeeds
does it call the inherited constructor. Consequently no assignment to
`current_tx`, `root_payload`, `collector.root_tip`, `call_lowers`, the root
issuance set, the root mailbox or the actor-owned ordinal is reachable for a
rejected value.

I independently tested the values

```text
2, -1, 1/2, "0", None, (0,)
```

against fresh Q1 and Q2 initial states. Every value raised `ValueError`.
Before/after equality held both under D35c's declared state snapshot and under
a complete protocol-5 serialization of the `Network` object. This directly
closes the round-3 case in which payload `2` left an issued root envelope and
advanced the ordinal.

The test is validation of the mathematical value alphabet `{0,1}`. Python
representations equal to those two values have the same admitted value; the
result does not assert a separate runtime-type ontology for bits.

## 3. Six rejection snapshots — pass

I reconstructed the six D35d closing cases without calling the printed
summary assertion:

1. an unissued but structurally plausible child query;
2. a visit to nonexistent port 9;
3. a fork repeating the same port;
4. an idle choice with a probability not in the local menu;
5. the malformed fork through ordinary peek/process/ack service; and
6. a non-bit root request.

All six rejected before any difference in a complete serialized network
object, in both Q cells. The fifth case retained the exact rejected envelope
at the same mailbox index. The independently obtained result is therefore

```text
Q1 complete-object unchanged  6/6
Q2 complete-object unchanged  6/6
rejected service queued        1/1
```

This is stronger than detecting only durable event or tip changes: it also
covers the collector, carrier, mailboxes, issued/used capability sets, open
calls, transfers, root fields and actor ordinal as represented by the
executable.

## 4. Typed actor ownership and generated-birth continuity — pass

Storage identities now have disjoint value domains. Supplied actors and
events cannot equal generated actors and events even when their display text
is identical. Generated identities have the declared coordinates

```text
(component namespace, root causal ordinal, laminar call path),
```

with separate actor and event domain tags. The disconnected control has its
own actor/event domains.

For a birth, D35d creates the generated actor and generated event with equal
structural coordinates but unequal types. It then installs the child in all
of the following mutually consistent locations:

- the parent's owned port table;
- the child's local parent address and parent port;
- the shared world's parent/child actor relation;
- the actor-name/address bijection;
- reciprocal parent/child edge-key tables; and
- the birth event and synchronized actor tips.

I checked these relations independently for every actor in all 16 first-call
states and all 408 second-call refinements in each Q cell. Across those state
families, the first laws contained 12 generated-actor state-occurrences and
the refinements contained 752. Every occurrence had:

```text
name -> address -> actor round trip          exact
local parent port -> child address           exact
shared-world parent/child relation           exact
reciprocal edge key                          exact
local tip = shared-world tip                 exact
matching generated birth event               present
actor/event structural coordinates           equal
actor/event typed domains                     disjoint.
```

The eight-call deterministic replay contained four generated actors under
each of FIFO, LIFO and canonical service, with all the same continuity checks
passing. Thus typed freshness is not only a dictionary-collision repair at
the first event; newborns remain usable owned actors in later calls.

The registered collision probes pass immediate `16/408/408` projectivity,
six-call late continuation and the future-newborn actor case. I additionally
used the actual `str(TypedId(...))` form of a future generated event and actor
as supplied display strings. The event case again passed `16/408/408`, and
the actor case retained all 16 normalized branches in both Q cells. Domain
separation, rather than a reserved display-string convention, supplies the
freshness property.

## 5. Serializer and grown replay — pass at the physical quotient

FIFO, LIFO and canonical mailbox service independently produce the same
16-atom exact distribution with total mass one in each Q cell. Every one of
the 16 completed first states admits a second call: comparison of FIFO and
LIFO with the canonical reference gives 32 exact grown-law equalities per
cell.

Eight successive deterministic root calls also give the same
`physical_key` under all three serializers, with the root actor's causal
ordinal equal to eight. The generated typed identities depend on causal call
ordinal and call path, not on mailbox delivery order, so the collision repair
does not introduce a serializer channel.

Here “exact equality” is equality of the registered physical quotient,
including actor structure, generated event provenance, carrier amplitudes,
evidence and transfers. It is not an assertion that two Python executions
must have the same incidental dictionary insertion order.

## 6. A-rooted and shared-joint scope — unchanged

D35d replaces identity allocation and adds an early public-boundary check; it
does not replace D35c's architecture. The executable still has logical actors
with actor-indexed tips, port tables, mailboxes, issued and used capabilities,
outstanding calls, evidence fields and the root causal ordinal. It also still
has one shared `Network.collector` containing the persistent event DAG and one
exact joint carrier state used to evaluate the composed quantum maps.

Accordingly, the accepted locality statement remains:

> local action menus and licensed message transfers in a supplied A-rooted
> laminar protocol, represented and audited through a shared exact joint
> history/carrier object.

It is not a theorem that the carrier factors into actor-owned quantum states,
that Python actors are independent processes, or that the complete physical
state is stored distributively. The terminal receipt continues to state
“supplied A-rooted laminar nested-call family” and leaves overlapping/root-free
diamond specification, peer/cycle/join sectors, Q, g, the root, coherent graph
support, the v9 bridge, spacetime and nature's law open.

## 7. Findings and allowed noun

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final count:** **0B / 0M / 0m / 0n.**

This locality delta permits the existing decision noun:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

with the mandatory expansion:

> a typed, alpha-safe, supplied A-rooted laminar classical actor protocol with
> logical mailboxes, structural CAP and one carried D-origin bounded datum,
> evaluated using a shared exact event-DAG/joint-carrier representation.

It does **not** permit “root-free universe law,” “independently initiating
actor law,” “distributed quantum state,” “selected Q or g,” “complete
interactive click law,” or any spacetime, dimension, cone or gravitational
claim.
