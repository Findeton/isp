# D35 round 3 — causal-locality and fail-closed final review

**Frozen target:** commit
`8a9bb98da2a37d61f5887fa69d397792ed0f4807`.

**Lane:** issued-call ownership, local transition preconditions, mailbox
peek/ack semantics, adjacent carried evidence, local menus versus shared joint
audit representation, actor-owned succession, serializer gauge and A-rooted
scope.

**Verdict:** **SCIENTIFIC LOCALITY DELTA ACCEPTED WITH ONE NARROW FAIL-CLOSED
MINOR.**

**Count:** **0 blockers / 0 majors / 1 minor / 0 nits.**

D35c closes the load-bearing round-2 findings at its newly narrowed scope. It
does not construct independent quantum-state storage or a root-free universe
law. It does construct an executable supplied A-rooted laminar call family in
which structural action menus are actor-local, incoming calls must have been
issued to the target, return evidence is carried across each selected edge,
machine mailbox order is gauge, and A owns the causal ordinal of its calls.

## 1. Exact reproduction

Fresh runs under `PYTHONHASHSEED=11235813` and `23571113` exited zero, were
byte-identical to each other and the committed stdout, and printed `PASS
16/16`.

```text
source SHA-256
50f1e710cc04de3576b24bd5e7414764f1dea1ebb86f0b0b5747d2b18109c765

stdout SHA-256
d8f0ef0c4320ff58badcff6ce6916fe7a3f4adb94b58de8afd95c4aa09bb6f42

internal science SHA-256
da82ce3ca611fd2e51f0d0e4fd3a36ec74edb895c279e9f6bcd48ac8ceb5aebf
```

The reproduced receipt contains, per Q1/Q2:

```text
serializer branches/atoms        16/16 under FIFO, LIFO and canonical
actor+event alpha quotient       16 atoms, exact equality
second-call refinements          408
event/payload persistence        408/408
closing rejections               5/5 unchanged
inherited rejections             9/9 unchanged
rejected envelope retained       1/1
D-source queried/unqueried       6/10 histories
grown scheduler checks           32
root-owned ordinal after replay  8.
```

## 2. Issued incoming ownership — pass at the declared protocol scope

Every logical actor now owns `issued_incoming`. `enqueue_query` adds the exact
capability identifier before placing the query in that actor's mailbox;
`validate_query` refuses any identifier absent from the set; successful
processing removes it and records it as used.

The round-2 unissued A-to-B construction, including the model-derived edge
token and a locally adjacent route, now rejects before state mutation. This is
the correct scientific distinction:

```text
owned edge       an interaction could be locally legal;
issued incoming  this particular call belongs to the sampled call diamond.
```

In trusted generation, the requester first stores its `OwnedCall`, then issues
the exact child capabilities into the targets' incoming sets. The target-side
set is therefore sufficient for the supplied single-process protocol.

This is not a general theorem for untrusted or independently administered
networks. `enqueue_query` is part of the model's call constructor, and the
family remains a supplied rooted protocol. The manuscript does not claim a
broader distributed-authentication result, so no scientific overreach remains
in this lane.

## 3. Full option validation and peek/ack — pass

`prevalidate_event_and_option` now runs before capability consumption,
transfer recording, event creation or tip mutation. It checks:

- exact membership in the actor's local probability menu;
- kind-specific arity and owned ports;
- newborn address/name freshness; and
- generated-event identity freshness.

The previous malformed visit to port 9, duplicate fork leg and altered idle
probability all reject with the complete state snapshot unchanged.

Mailbox service now peeks without removal, processes the envelope, and
acknowledges only after successful completion. A rejected envelope remains in
the mailbox. This closes the previous discrepancy between direct-handler and
ordinary service paths.

## 4. Adjacent carried D-origin evidence — pass

D35c adds a connected source seal at D and gives actors local evidence bits
and source sets. Every return envelope carries:

```text
result event;
evidence digest;
output bit; and
output source set.
```

When D is queried, its event returns those fields to B; B's merge consumes the
carried child values and returns the merged values to A. When D is not queried,
neither its bit nor its source identity appears at A2. Changing an inert
disconnected source also leaves the A observable unchanged.

The receipt's six queried and ten unqueried histories reproduce in both cells,
with 18 hop checks. Thus the result is stronger than structural ancestry alone:
it supplies one explicit bounded classical datum whose effect reaches A2 if
and only if the D route is selected.

The exact joint event DAG and output tables still audit the carried data. This
does not invalidate the carried construction, but it fixes its noun: one
shared mathematical representation verifies the whole protocol. D35c does not
prove physically distributed storage of the full history or entangled state.

## 5. Local actor menus versus shared joint representation — correctly scoped

An actor's stochastic menu depends only on its owned port table and the
supplied Q1/Q2 parameter cell. No universe-wide opportunity normalization is
used. Mailboxes, issued incoming calls, used calls, open calls, evidence bit,
source set and root ordinal are actor-indexed.

The collector continues to hold one persistent event DAG and one exact joint
carrier vector. This shared object is used to evaluate the composed quantum
maps and audit ancestry. The final note/output explicitly calls it a shared
joint representation and refuses both OS-process and distributed-quantum-state
storage claims.

That separation is scientifically acceptable: the classical causal actor
specification is local at its rooted laminar scope, while its exact quantum
evaluation is represented jointly. The result must not be paraphrased as a
local hidden-variable factorization of the entangled carrier.

## 6. Actor/event gauge, actor-owned succession and serializers — pass

Seed events are now canonically represented by kind, structural actor roles,
flags and recursively canonical predecessors. A simultaneous nontrivial actor
and complete seed-event renaming gives the identical 16-atom physical
distribution and retains 408/408 projective/persistence checks.

The root actor owns `call_ordinal`. `start_root_call` reads that ordinal as the
transaction's causal successor label and increments it. Eight-call replays end
at ordinal eight under every serializer. The label is local A-wire succession,
not elapsed duration, a rate, proper time or a global event counter.

FIFO, LIFO and canonical mailbox selections produce identical complete
distributions on initial calls, all registered second calls, and the
eight-call deterministic replay. Construction service order is therefore
gauge inside the strict rooted nested-call grammar.

## 7. MINOR m1 — root payload domain is checked after root-call mutation

The declared root request payload is a bit, but `start_root_call` does not
check `request_payload in {0,1}` before it:

1. writes `Network.current_tx` and `Network.root_payload`;
2. records `call_lowers[tx]`;
3. enqueues the root capability; and
4. increments A's `call_ordinal`.

With `request_payload=2`, the later query validation correctly raises
`ValueError: malformed evidence payload`, but the before/after state is not
equal: A's ordinal is one and the root envelope remains queued.

This does not affect any admitted Q1/Q2 history because all registered calls
use bit payloads. It is nevertheless a real fail-closed gap in the public root
call constructor.

**Required repair:** validate the payload alphabet at the start of
`start_root_call`, before writing transaction state, enqueueing or incrementing
the ordinal. Add this case to the unchanged-state battery.

## 8. A-conditioned and root-free scope — honest

D35c is a sampler conditional on:

- distinguished A and A1;
- a supplied finite rooted ownership tree;
- laminar outward nested calls;
- a supplied request payload;
- Q1 or Q2; and
- supplied coupling/root/capability grammar.

It does not define which actor initiates next in a root-free collection, nor
overlapping peer calls, cycles, joins or simultaneous competing diamonds. The
note and receipt state those openings explicitly. The correct interpretation
is therefore an A-conditioned family, not the complete interactive click law
of all records.

## 9. Findings and allowed noun

```text
B  blockers  0
M  majors    0
m  minors    1   root payload validated after root-call mutation
n  nits      0
```

**Final count:** **0B / 0M / 1m / 0n.**

Subject to the one-line fail-closed payload repair, this lane allows:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

with the mandatory expansion:

> a supplied A-rooted laminar classical actor protocol with logical mailboxes,
> structural CAP and one carried D-origin classical datum, evaluated with a
> shared exact event-DAG/joint-carrier representation.

It does **not** allow “root-free universe law,” “independently initiating actor
law,” “distributed quantum state,” “derived opportunity weights/coupling,” or
“the complete interactive click law.”
