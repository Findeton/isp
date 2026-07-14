# D36 round 1 — concurrency, locality and liveness hostile review

**Frozen target:** commit
`5f6cd7fccb6e34991bccd10fa1aa7992ebd0a393`.

**Lane:** concurrency safety, actor/causal locality, hidden coordination and
atomicity, partial application, construction-order gauge, finite-attempt
liveness, crash/fairness scope and verdict ceiling.

**Verdict:** **THE FAIL-FAST SAFETY CORE IS SOUND AT THE FROZEN FINITE
REFERENCE-TRANSITION SCOPE, BUT THE EXECUTABLE DOES NOT YET CARRY THE CLAIM
THAT P4 IS A STRICTLY ACTOR-LOCAL RECORD PROTOCOL.**

**Count:** **0 blockers / 1 major / 2 minors / 1 nit.**

The important scientific result survives this lane.  Exclusive version-bound
promises, fail-fast rejection and an immutable transaction decision remove
circular wait without pretending that a final seal updates several participant
wires at once.  All generated P4 traces are stale-safe and conflict-safe in the
four registered fixtures.  Partial applications are present rather than
hidden.  The multiwire oracle is correctly isolated as an oracle, and the
failure-free, fair-service and nonselection ceilings are stated.

The opening is architectural rather than arithmetical.  The positive checker
is one global state vector and one global pending-message multiset.  Its
transition handler directly reads and writes fields that the prose assigns to
different actors.  It neither transports authenticated causal evidence nor
constructs the immutable event histories claimed by the actor description.
Consequently it is an exact centralized reference semantics for P4, not yet an
actor-local refinement of that semantics.

## 1. Exact independent reproduction

I ran the frozen source twice:

```text
PYTHONHASHSEED=104729 \
  python3 v10/code/d36_birth_coordination_exact.py \
  > /tmp/d36.locality.104729.out

PYTHONHASHSEED=1299709 \
  python3 v10/code/d36_birth_coordination_exact.py \
  > /tmp/d36.locality.1299709.out
```

Both runs exited zero, printed `PASS 22/22`, were byte-identical to each
other, and were byte-identical to the committed receipt.  The hashes are:

```text
source
f1b2c5010812e08f560876a570fc06693d59633de03421b0fed5ff5e5c3daed0

fresh stdout, both seeds
0bf500873acdc71bb68c5b7d9012b89310941c879f59b013105db1f0e00fccea

committed stdout
0bf500873acdc71bb68c5b7d9012b89310941c879f59b013105db1f0e00fccea

printed stdout-body hash
c5258f02d8f9763708e9355a304295e6c94a7c85aac39dde22c1d3f0b826c1c7

printed internal-science hash
872a38acd65f7ebcb122a50f6713da53ae119764c7449387b1b55efe27acf04b.
```

`git diff --check 5f6cd7f^ 5f6cd7f` is clean.

The reproduced finite state counts are exactly:

```text
pair       1,113 states /   2,984 edges /  8 terminals /   232 partial
triangle  34,637 states / 140,028 edges / 17 terminals / 9,420 partial
disjoint     289 states /     816 edges /  1 terminal  /   120 partial
partial    1,517 states /   5,162 edges /  2 terminals /   518 partial.
```

Every graph is acyclic, every generated terminal is fully typed, and no graph
has a terminal nonclosed state.

I also independently inspected every state for two incompatible transactions
that had both obtained all-grant commit decisions.  The result was zero in all
four fixtures:

```text
pair       conflicting commit-decision states  0 / 1,113
triangle   conflicting commit-decision states  0 / 34,637
disjoint   conflicting commit-decision states  0 / 289
partial    conflicting commit-decision states  0 / 1,517.
```

Thus the safety criticism below is not that a generated frozen trace double
commits.  It is that the locality/authentication layer named by the theorem is
not the object that was executed.

## 2. Properties that pass this hostile lane

### 2.1 The fail-fast mechanism is genuinely different from held waiting

P4 gives a busy participant an immediate reject transition.  A transaction
then waits only for the finite set of responses already required by its fixed
body; after any rejection it releases every promise it obtained.  Under the
declared reliable fair-service and no-failure assumptions, the transition
graph contains no circular wait.  The exact pair and triangle graphs include
the split-grant schedules rather than excluding them by a favorable order.

This is a real structural result:

```text
exclusive promise + wait       safety but reachable circular wait;
exclusive promise + fail-fast  safety and finite-attempt termination;
retry lineage                  still possibly live-locked or starved.
```

The note preserves the final distinction.

### 2.2 No multiwire atomicity is hidden in P4

The exact graph contains many states in which only part of a committed
transaction has applied.  One independently extracted pair state is:

```text
versions       (1, 0)
promises       (-1, 0)
P applications (1, 0)
P phase         COMMIT.
```

A has appended its application and released its promise; B still holds P's
promise and has not applied.  The close transition is unavailable until the
remaining application and every acknowledgement occur.

This is exactly the right negative control.  P5 alone performs the atomic
multi-tip transition, and the note repeatedly calls P5 an oracle.  D36 has not
smuggled D35's shared-world `sync_tips` operation into the local protocol.

### 2.3 The cyclic-order counterexample is correct

The local comparisons

```text
A: R < P
B: P < Q
C: Q < R
```

induce `R < P < Q < R`, and the exact checker finds zero compatible global
serializations.  This correctly proves that independent local queue orders do
not by themselves define an acyclic transaction history.  It is the relevant
three-region overlap obstruction, not merely a deadlock example.

### 2.4 A transaction coordinator is not automatically a cosmic coordinator

Analytically, one transaction actor T may own its finite participant body,
response slots, decision and acknowledgement slots.  That is coordination
over one finite causal region, not a universe-wide next-event selector.  D36
also labels the complete closed-batch greedy evaluator a supplied
**specification**, leaves the eligibility/batch seal open and refuses to call
its common priority derived.  I find no hidden global *opportunity
normalizer* in the stated P4 theorem.

The major below is narrower: the current executable has not realized the
claimed per-actor ownership and evidence transport.

### 2.5 Construction-order scope is mostly honest

For two prepares contending at the same participant, the first processed
prepare changes the physical promise:

```text
deliver P-at-A first -> owner 0 (P)
deliver Q-at-A first -> owner 1 (Q).
```

Those transitions are not incomparable gauge swaps; they are alternative
local conflict events.  D36 does not convert the terminal-state multiplicities
into probabilities and explicitly marks arbitration as unselected.  Disjoint
closed outcomes converge, while the K1--K3 laws are separately normalized.
The current wording therefore avoids the worst construction-order error.

## 3. MAJOR M1 — “strictly actor-local” is not receipt-carried

Section 6 calls P4 “the positive strictly actor-local protocol.”  The executed
object does not yet establish that adjective.

The complete P4 state is one `FFState` containing:

```text
all participant versions and promises;
all transaction responses and phases;
all participant applications and acknowledgements;
one global sorted pending-message tuple.
```

`ff_deliver` then performs every logical role.  More importantly, its handler
preconditions cross the ownership boundary described in the paper:

- a participant-side `PREPARE` reads T's global `phase` and T's response slot;
- a participant-side `COMMIT_DECISION` reads T's global phase directly;
- a T-side `ACK` reads the participant's global application slot directly;
- all messages are bare triples `(kind, tx_index, participant_index)` with no
  sender, target mailbox, base-tip identity, capability, decision event,
  application event, digest or one-use provenance; and
- the fixed fixture supplies direct participant incidence but no admitted
  route or disconnected-address rejection.

These reads are harmless in a reference transition table, but they are the
facts a local implementation must receive as carried causal evidence.  The
table currently obtains them from shared memory.

The omission is operationally visible.  I inserted two response triples into
the otherwise frozen pair initial state, without delivering either participant
prepare:

```text
(REJECT_RESPONSE, P, A)
(REJECT_RESPONSE, P, B).
```

Both were accepted.  The coordinator moved P to `ABORT` and generated both
abort-decision messages:

```text
forged_rejects_accepted       1
P responses                  (2, 2)
P phase                       ABORT
decision messages             ((ABORT,P,A), (ABORT,P,B)).
```

The still-pending real `PREPARE(P,A)` then raises `AssertionError: malformed
prepare` because the forged response already occupied the shared response
slot.

This is not a counterexample inside the paper's *assumption* of authenticated
messages.  It is exact evidence that the executable does not implement or test
that assumption.  It also shows why the remote reads matter: a real T actor
must validate a carried grant/reject record issued by the named participant;
it cannot inspect the participant or a global response matrix.

The closure receipt has the same evidentiary gap.  `upper_seal_gate` builds one
hard-coded two-participant parent dictionary.  It is internally correct, but
the 28 fail-fast terminal states do not generate immutable proposal, grant,
decision, application, acknowledgement and close records, and no projection
connects their state transitions to that dictionary.  Consequently T2 is a
plausible analytical construction, not yet an executed record-history theorem
for every P4 success.

### Required repair gate for M1

Either narrow the earned noun to

```text
CLOCK-FREE FINITE REFERENCE TRANSITION SYSTEM / RESERVATION-SAFE,
NONSELECTING, FAILURE-FREE
```

or add an independent actor refinement with all of the following:

1. participant actors own only their tip/version, promise, used-message set
   and mailbox;
2. each transaction actor owns only its immutable body, response slots,
   monotone decision, acknowledgement slots and mailbox;
3. `Prepare`, `Grant/Reject`, `Decision` and `Ack` envelopes carry typed sender,
   recipient, transaction/body digest, protected base tip, issued capability
   and the predecessor record needed by the receiver;
4. every handler consults only its addressed actor's state and the carried
   envelope; there is no remote phase/application lookup;
5. proposal birth is one-parent and every participant is reached through an
   admitted route; a disconnected or unissued lookalike rejects unchanged;
6. forged response, wrong-base grant, forged decision, forged ack, replay and
   duplicate-application cases all reject before any durable state mutation;
7. the actor rebuild generates immutable event DAGs, including partial states,
   and a close record only after all carried apply acknowledgements;
8. the actor transition graph projects exactly to the current P4 reference
   graph on the four frozen fixtures, with identical terminal classes; and
9. swapping genuinely incomparable mailbox services preserves the complete
   canonical event history, while same-participant contention remains an
   explicitly marked physical branch rather than machine gauge.

Passing that gate would show that the global table is only a verification
representation.  At the frozen commit that equivalence is not proved.

## 4. MINOR m1 — the exact P4 campaign is a supplied one-batch, one-version
model

`initial_failfast` places every registered transaction's prepares in the
single initial pending tuple.  Every proposal body is therefore supplied
before any delivery.  Participant versions are hard-coded to `0` initially
and are allowed only in `{0,1}`.  No transition births a new proposal after an
application, rebases it onto version 1, or adds a previously unknown
contender.

Delaying a preloaded base-0 prepare correctly models a late *message* for an
already supplied attempt.  It does not model a newly born version-1 attempt or
an indefinite online population.  The separate stale gate is only the true
comparison

```text
{"A":0,"B":1} != {"A":0,"B":0};
```

it is not a path through the P4 state machine.

The note already says that the eligibility boundary, opportunity law, retries
and starvation are open, so this is a scope repair rather than a failure of the
finite checker.

### Required repair gate for m1

State T1 and the verdict explicitly as a theorem for a **supplied fixed finite
batch of base-version-0 attempts**, or add a two-epoch continuation in which:

- a transaction is born after another transaction has partially or fully
  applied;
- every participant validates the exact carried current tip rather than the
  literal integer zero;
- an old-base proposal is rejected as stale through the normal actor path;
- a correctly rebased proposal can later commit; and
- identities and event ancestry remain construction-order covariant.

No unbounded online/root-free history theorem follows even from that repair.

## 5. MINOR m2 — “safe” needs its exact failure and visibility qualifier in
the verdict

D36 is admirably explicit that partial application is physical and that P4 is
failure-free.  The short verdict nevertheless leaves “safe” broader than the
proved predicate.

The generated safety property is:

```text
no two incompatible closed commits consume one frozen base version;
no admitted commit application uses a stale or unpromised frozen base;
every failure-free fully serviced attempt eventually closes commit or abort.
```

It is not linearizable all-or-nothing visibility.  It is not nonblocking
atomic commit.  It is not crash-safe completion.

The distinction is exact.  Removing future progress after one grant produces:

```text
P phase      OPEN
A promise    P
pending      empty
terminal?    no.
```

Removing future progress after the extracted first application produces:

```text
versions       (1, 0)
promises       (-1, P)
P applications (1, 0)
pending         empty.
```

The second history is permanently partly applied.  A cannot safely undo its
sealed successor, and B has not adopted.  This is outside the declared fair,
failure-free model, but it fixes the meaning of the noun.

### Required repair gate for m2

Expand the terminal noun to **closed-attempt reservation-safe under reliable
fair service and no failures; partial visibility and blocking otherwise**.
Add executable negative controls for:

1. coordinator/message loss after one grant; and
2. participant/message loss after the first commit application.

They must print the live promise and partial-application witnesses and remain
explicit failures of liveness/failure atomicity, not failed P4 safety gates.
“Fair delivery” should also be defined to include eventual handler service of
each continuously pending envelope; network arrival alone is insufficient.

## 6. NIT n1 — gate provenance and note status should distinguish receipt
from pins

The note header still says `PRE-RECEIPT PROTOCOL PIN` although section 16 and
the committed data are the strengthened review candidate.  In addition, the
`PASS 22/22` display gives exhaustive graph checks, one-line finite witnesses
and pinned assertions the same visual status.  For example the crash gate
returns literal `(1,0)`, and G21 is assigned `True` before hashes are printed.

Nothing numerical is wrong, but the receipt should classify gates as

```text
exhaustive state enumeration;
exact finite arithmetic;
symbolic/static counterexample;
or scope assertion.
```

The status line should name the frozen review-candidate state.

## 7. Final disposition

```text
B  blockers  0
M  majors    1   actor-local/authenticated record refinement not executed
m  minors    2   fixed one-batch/one-version scope; safety noun too broad
n  nits      1   status and gate-provenance presentation
```

**Final count:** **0B / 1M / 2m / 1n.**

The following findings are accepted at reviewed strength now:

```text
birth alone does not remove held-wait deadlock;
read-only version photographs do not ensure safe commit;
exclusive fail-fast promises give conflict-safe finite attempts;
partial application is real and a close seal is not a multiwire successor;
local pairwise orders can form a global causal cycle;
crash tolerance, starvation freedom and arbitration remain open;
born and dormant-token carriers are presentation-equivalent in the matched
finite reference graph.
```

The promoted noun must wait on M1.  Until an actor-local refinement or a scope
downgrade is supplied, the strongest executable interpretation is:

```text
CLOCK-FREE FINITE COORDINATION REFERENCE SYSTEM /
RESERVATION-SAFE ON GENERATED FAILURE-FREE TRACES, NONSELECTING.
```

That is already a useful and honest result.  It identifies the indispensable
physical content as the exclusive causal promise plus explicit
apply/ack/closure records, while proving that fresh ticket birth itself does
not supply the missing arbitration or atomic joint click.
