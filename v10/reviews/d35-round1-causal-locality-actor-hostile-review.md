# D35 round 1 — causal locality, construction gauge and actor-simulation hostile review

**Frozen candidate:** commit
`b08249c71ab42b839d43ec240aa8d0d8f7cfc902`.

**Lane:** causal acquisition and message provenance; A-wire succession;
construction-order gauge; disconnected-component invariance; actor versus
global simulation architecture; malformed-message rejection; rooted ownership
and omitted cyclic/overlapping sectors.

**Verdict:** **REJECT THE PROVISIONAL ROW-2 PROMOTION.  THE TRUSTED RECURSIVE
ROOTED-TREE KERNEL SURVIVES, BUT THE REQUIRED ACTOR-LOCAL EXECUTABLE AND CAUSAL
MESSAGE GATES DO NOT.**

**Findings:** **1 blocker / 2 majors / 1 minor / 0 nits.**

The central mathematical object is not destroyed.  Exact local menu
normalization, finite termination, A1-to-A2 succession and scheduler invariance
survive both the registered specimen and my deeper adversarial tree.  The
failure is at the architecture/provenance boundary that D35 itself made
load-bearing: the second implementation is one central mutable `World`, one
central pending-task list and one central continuation dictionary.  Worse,
the message handlers accept unissued but locally plausible queries and returns
that create immutable ancestry before their missing route is discovered.  The
printed `malformed_rejected=5/5` battery does not test these cases.

Consequently the current code is an exact centralized interpreter of a local
recursive grammar, not yet the promised actor/tip-local sampler.  D35 can be
repaired without abandoning the timeless call-family idea, but row 2 and the
`18/18` actor/rejection reading are not available at the frozen target.

## 1. Reproduction and frozen artifacts

The candidate artifacts hash as:

```text
D35 note
f0ae99fa7c2c484b8a71774bbc9faad2f49d3b2f88d2871df3bbd087565c688b

exact source
06c997a195294991293fdedc9edce005a3f8ad1d23bfd8f73a5a08490163fa26

committed stdout
24a5cdfe35e1a85b25929217def4bede01e57169a14789392e7e5a7947a11656

corpus source
9347035205c9210ce6cbbbefab7242f3de687624c45098c0f6feb278850c80e6

corpus stdout
49a4bd6a1adc1be8ba247e55cb254b9084bcf03c2ff180e57a1073895d41203f
```

I reran the main receipt under independent hash seeds `24681357` and
`975318642`.  Both runs exited zero, were byte-identical to each other and to
the committed stdout, printed `PASS 18/18`, and retained internal science hash

```text
1f7b39ddaea634c1444695e5e536d528be45785e8c9997eba1388ed22cfe8aa6.
```

I also reran the antecedent corpus inventory under seed `13579`.  It was
byte-identical to the committed receipt and reproduced:

```text
primary files              437
category-relevant files    423
corpus stream SHA-256
84d6fb20bf780d268ba825c38120e4754abdfce30e448a6df6ad66993fc27485
gates                      5/5.
```

The failures below are therefore logical coverage failures, not flaky
execution, arithmetic drift or hash instability.

## 2. BLOCKER B1 — causal call-route provenance is not enforced

The candidate's strong locality claim is not merely “all predecessor names
exist.”  LDAP requires every acquired record to enter through a **licensed**
query/return/birth chain, and O7 requires explicit rejection of malformed
nonlocal or ancestry-forging messages.  The actor handler does not retain or
validate the capability that would establish that license.

### 2.1 What the code checks

`validate_query` checks:

- the target actor exists;
- for a nested query, target is a child of the named requester;
- the requester still has the claimed lower tip; and
- `root_cause` is the current global `world.root_tip`.

It does **not** check that:

- a requester actually issued this query;
- `continuation` exists and owns the declared slot;
- actor, path and slot match that continuation's outstanding child call;
- a requester-free query is the distinguished A-root query; or
- a returned event was created by the outstanding query it purports to close.

`process_return` likewise checks only a continuation/slot/actor tuple and that
the supplied event is the actor's current tip.  There is no outstanding-query
token and no requirement that the event descend from the carried query route.

### 2.2 Exact counterexample A — an unissued child query mutates history

Starting from the registered Q1 or Q2 world, I sent:

```text
Query(actor=B,
      path=(0,),
      root_cause=A1,
      requester_actor=A,
      requester_lower=A1,
      continuation=K-missing,
      slot=0)
```

There is no `K-missing` continuation and A issued no such call.  The query
passes `validate_query`.  Selecting the ordinary idle arm creates immutable
event

```text
E91:0 actors=(B) predecessors=(BD,A1)
```

and only then queues a return to the nonexistent continuation.  The later
return would be rejected, but the supposedly immutable record has already
been created and B's tip has already moved.  Rejection after mutation is not
the promised malformed-message gate.

The result is identical in Q1 and Q2.

### 2.3 Exact counterexample B — a non-A query is accepted as the root call

I submitted a requester-free root-shaped query to B with B's valid tip `BD`
and the global root cause `A1`:

```text
Query(actor=B,
      path=(),
      root_cause=A1,
      requester_actor=None,
      requester_lower=BD,
      continuation=None,
      slot=None).
```

It passes validation.  The idle arm sets

```text
machine.root_result = E92:r,
actors(E92:r) = (B),
A.tip = A1.
```

Thus the generic actor handler can declare a completed “root result” that is
not an A event and is not A2.  The trusted constructor never sends this query,
so the registered E1 test passes; the claimed malformed actor interface does
not enforce the theorem it is said to realize.

### 2.4 Exact counterexample C — an old tip can impersonate a query return

With a root continuation waiting for B, I supplied B's pre-call current tip
`BD` as the return event without executing any B query cell.  `process_return`
accepts it and creates:

```text
root_result               E93:r
transaction events        (E93:r) only
BD in NewPast_A(A1,E93:r) yes
pending work              empty
continuations             empty.
```

The grammar says a queried B must first seal an idle, birth, visit or fork
event.  Here the root acquires B's old `BD` record through a manufactured
merge with no B transaction event.  The existing validator has no datum with
which to distinguish this from a real return.

This counterexample was constructed using the same style of manually seeded
continuation that `run_malformed_tests` itself uses.  It therefore attacks the
declared validation boundary, not an unrelated private helper.

### 2.5 Why the printed 5/5 does not close this

The frozen battery tests:

```text
forged root tip;
unauthorized A--D ownership edge;
foreign root cause;
duplicate return;
foreign return event.
```

Those five cases do reject.  They do not test an authorized edge with no
issued continuation, a requester-free non-A root, a path/slot not owned by an
outstanding call, or a current but pre-query actor tip used as a return.  The
gate therefore proves five examples, not route provenance.

### 2.6 Consequence and required repair

This is a blocker because O7.7 and actor-local LDAP are prerequisites of the
provisional row-2 verdict.  The trusted recursive enumerator still defines a
law, but the message implementation does not enforce that law against the
malformed traffic it advertises rejecting.

At minimum the repair needs:

1. a fresh call capability created by the requester and stored as an
   outstanding child call at the owning actor;
2. query validation against capability, exact owner, actor, slot, path,
   requester lower tip and root transaction;
3. a return capability tied to the issued query and a proof/reference that the
   returned event is the result of that query, not merely the actor's current
   tip;
4. an explicit rule that only the distinguished A-root actor can emit the
   top-level result in this model;
5. validation before any immutable event/tip mutation, with transactional
   rollback on failure; and
6. exact adversarial gates for all three counterexamples above, negative slots,
   missing continuations and cross-continuation replay.

Until that exists, `malformed_rejected=5/5` must not feed the general O7/LDAP
row.

## 3. MAJOR M1 — the “actor mailbox rebuild” is a global interpreter

The second implementation is algorithmically independent of
`resolve_recursive`, which is useful.  It is not, however, the actor/tip-local
message implementation required by O7.3.

The actual state is:

```text
Machine.world          one World containing every actor, event and amplitude;
Machine.pending        one universe-wide task list;
Machine.continuations  one universe-wide continuation dictionary;
frontier               one global exact branch list.
```

`Actor` has no mailbox, no local outstanding-call table and no local random
source.  `enumerate_actor_machine` centrally:

1. chooses the next message from the global queue;
2. calls `local_options` through the global `World`;
3. clones the whole world once for each option;
4. multiplies global branch probabilities; and
5. mutates a global amplitude dictionary and global actor tips.

This can faithfully **simulate** a semantically local grammar, just as a
single-threaded event simulator can simulate a distributed protocol.  It does
not independently demonstrate that the protocol can be hosted by autonomous
actors with only local state and carried messages.  In particular, the hidden
central continuation table is precisely what the route-provenance blocker
needs but never types as an actor-owned capability.

The global amplitude vector alone is not automatically a physical nonlocality:
a classical simulator may need global storage to calculate an entangled state
while applying only local operations.  The overclaim is narrower and clearer:
the code calls a central exact-state interpreter an actor-mailbox rebuild even
though no mailbox process exists.

**Required resolution:** either implement a genuinely distributed reference
in which each actor owns its tip, ports, mailbox and outstanding capabilities,
and the central scheduler sees only deliverable envelopes; or rename E2/O7 as
an independent **message-shaped global interpreter** and withdraw the
actor-local-executable clause from row 2.  A central collector may assemble a
history afterward for comparison, but it may not authorize calls or make
local choices for the actors.

## 4. MAJOR M2 — disconnected invariance misses the global identifier channel

The registered P--Q control passes because its names are chosen not to collide
with the root transaction's deterministic names.  The generator creates
events and newborn actors from only `(tx,path)`:

```text
E0:r, E0:0, ...
N0:r, N0:0, ...
```

Those names are allocated in the single global `World` dictionary.  No local
freshness capability or component namespace is present.

I added a valid disconnected one-actor component X carrying preexisting event
`E0:r`.  It has no path to A and changes no A collar.  Calling the frozen
kernel at `tx=0` fails immediately with:

```text
ValueError: duplicate event
```

in both Q1 and Q2.  The A law is therefore not invariant under arbitrary
disconnected marked factors in the executable representation.  A remote
nominal identifier changes whether A's next law is even defined.

This does not refute the abstract local product kernel; event names are gauge
and the collision can be repaired.  It does show that E5's single P--Q fixture
is too weak and that the current implementation relies on a hidden global name
reservation.  The completed-history discussion similarly supplies `tx`
externally rather than deriving collision-free local event capabilities.

**Required repair:** use actor/component-scoped or content-addressed fresh
identities, prove alpha-renaming covariance, and rerun disconnected controls
under adversarial remote names, arbitrary remote event content and at least
two independently advancing root namespaces.  The physical distribution
must be compared after the nominal-name quotient.

## 5. MINOR m1 — scheduler equality needs an explicit physical quotient gate

The registered scheduler comparison is not false.  FIFO, LIFO, canonical,
forward/reverse child evaluation and shared-control gate reversal all agree
exactly on the specimen.  The local weights are normalized physical branch
weights, so the strong equal-path diamond is a valid sufficient construction
gauge inside the frozen strict-tree grammar; this is consistent with the v9
correction that quotient pushforward, not arbitrary raw race density, is the
general requirement.

However, `local_history_key` retains nominal actor names, deterministic
`E{tx}:{path}` event identifiers and path slots assigned after sorting child
names.  The deterministic replay tape is also keyed by actor name and path.
There is no alpha-relabeled canonical marked-history comparison of the kind
already required in the v9 gauge work and D34e/f.

This matters because construction serialization and nominal identity are two
different gauges.  Equality on one fixed labeled address system is stronger
than one scheduler check but does not by itself demonstrate a well-defined
measure on unlabeled physical stems.

**Required repair:** add independent actor/event relabelings, transport owned
ports and action choices with the permutation, canonicalize the resulting
marked DAG without using construction paths as physical labels, and compare
the full pushforward distribution.  Deterministic replay may remain
address-keyed as an implementation coupling, but it must not be evidence for
physical relabeling covariance.

## 6. Independent deeper-tree attack — positive result

To distinguish a shallow-fixture failure from the architectural failures
above, I enlarged the owned tree from

```text
A->{B,C}, B->{D}
```

to

```text
A->{B,C}, B->{D,F}, C->{E,G}.
```

This exercises nested forks in both root branches and permits deeper
interleavings.  For both Q1 and Q2 I obtained exactly:

```text
completed branches                         122
distinct labeled history atoms             122
forward/canonical vs reverse/reverse        exact equal
recursive vs actor FIFO/LIFO/canonical      exact equal
branches with A touched only at root return 122/122.
```

Thus the candidate's scheduler theorem is not merely a 16-branch coincidence.
Inside a trusted finite rooted tree, sibling subcalls are disjoint, their
probability factors commute, their local carrier operations commute, and the
root merge is held until both return.  The analytic height/commutation proof is
credible at that scope.

This positive attack also isolates the review verdict: I do **not** request a
change to the strict-tree construction-gauge theorem merely because its actor
host is currently centralized.

## 7. A2 and query-created ancestry — trusted path versus public handler

For every registered branch and all 122 deeper-tree branches, the only new
transaction event touching A is the final root return.  Descendant events may
have A1 as a carried causal predecessor, but they do not touch A's wire.  Hence
the trusted constructor really does make A2 the first A-wire successor of A1.

Likewise, direct ancestry edges from `root_cause` and `requester_lower` into a
child event are not automatically forgeries.  They are a compact
representation of a query message carrying those immutable references.  In
the trusted recursion, every such edge follows an owned parent-to-child route.

The blocker is that the actor handler cannot distinguish that trusted carried
query from an invented message containing the same public identifiers.  The
repair should preserve query-carried ancestry while making its route
capability explicit; it need not insert a fictitious numerical time or global
query event.

## 8. Root ownership, barrier structure and honest exclusions

The model is not a universe of independently initiating actors.  A is the sole
root caller; descendant activity occurs only inside A's synchronous nested
transaction; the next root call begins only after every selected descendant
has returned.  In distributed-systems language this is a rooted recursive RPC
barrier, not an asynchronous peer network.

That architecture is substantive extra physics and can act as a
component-spanning logical barrier when the call visits a large subtree.  It
does not require an elapsed time, but “no time variable” should not be confused
with “no privileged transaction nesting.”

The candidate is honest about this at its important loci:

- the root is boundary data;
- only outward owned-child calls are proved;
- completed history iterates root calls;
- cyclic, peer, mutually initiating, overlapping and disconnected joins are
  excluded; and
- the rooted ownership architecture may be too restrictive for nature.

I therefore record this as the principal forward opening rather than an
additional severity finding.  After B1/M1 are repaired, the accepted noun
should still say **rooted nested-call family** until simultaneous peer calls
and overlaps are defined.  The frozen result must not be narrated as the full
interactive click law for all records.

## 9. Corpus consistency

The attack is consistent with the inherited boundaries:

- v9 construction-order work separates locality from gauge and requires the
  physical pushforward on covariant marked histories, not a hidden global
  scheduler distinction;
- D14 permits finite local diamond sewing but does not call every possible
  physical diamond constructed;
- D28 distinguishes representable local operations from a locality theorem
  and leaves opportunity support as extra law;
- D31 warns that covariance can force consultation of richer state without
  proving that such state is local;
- D33/D34 separate an ideal local law from the implementation architecture and
  explicitly refuse to equate a central reference evaluator with OS actors;
  and
- D34e/f make nominal actor names and incomparable serialization gauge while
  keeping typed wires, parentage and ancestry physical.

D35's local recursive grammar fits those results.  Calling its current global
dictionary evaluator an actor-mailbox implementation does not.

## 10. Findings ledger and disposition

```text
B1  BLOCKER  query/return route provenance absent; malformed messages can
             create ancestry and even non-A root results before rejection

M1  MAJOR    the purported actor rebuild is one global World, queue,
             continuation table and branch frontier, not independent actors

M2  MAJOR    disconnected invariance misses a global identifier channel;
             a remote E0:r makes the A kernel fail with duplicate event

m1  MINOR    scheduler equality lacks an alpha-relabeled physical quotient
             gate, although strict-tree order invariance itself survives

n   NITS     none
```

**Final count:** **1B / 2M / 1m / 0n.**

**Decision:** the first-applicable safe row at this frozen target is not row 2.
The exact recursive finite rooted-call law, nonselection exhibit and trusted
strict-tree scheduler theorem survive, but O7's actor-local and malformed-
rejection conjuncts fail.  Freeze these openings before modifying code.

After a capability-authenticated per-actor rebuild, adversarial remote-name
and alpha-gauge gates, and a fresh exact delta, the candidate may again seek:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE.
```

Cycles, peer joins, overlapping calls, independently advancing roots,
coherent graph-sector sums, v9 stem-spectrum identification, Lorentzian
geometry, proper time and nature's selected law remain open even after such a
repair.
