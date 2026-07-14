# Relativistic ISP v10 paper 25

# Record birth carries coordination but does not select it

## A clock-free append-only transaction protocol, a finite-horizon eliminability theorem, and the missing arbitration law

**Status:** COORDINATOR-CLOSED CANDIDATE after terminal D36 and one disclosed
self-hostile paper review; independent paper-level review remains open.
**Date:** 2026-07-14.

## Abstract

Can a newly born record coordinate overlapping interactions among persistent
record actors without a global commit clock, a privileged universe root or a
physical global queue?  The answer separates three questions that record
language easily conflates: what carries a proposal, what makes overlapping
applications safe and terminating, and what selects which proposal should
win.

Fresh transaction identity alone does none of the protocol work.  If a born
ticket retains sequential held-resource acquisition, the reachable graph is
isomorphic to the original lock graph and keeps its circular-wait deadlock.
Reusable immutable grants allow incompatible commits.  Independent local
adoption permits partial commits.  Exclusive grants prevent double use but
still split-deadlock when a busy participant waits.  The positive mechanism
is instead a version-bound exclusive promise, an immediate typed rejection
when busy or stale, one authenticated transaction decision, local
apply/release records, acknowledgements and a final transaction close.

Under supplied finite attempts, ideal authentication, honest record-generating
actors, reliable messages, failure-free operation and fair complete servicing,
this protocol closes every attempt commit or abort.  It has no numerical time
field.  Participant and transaction handlers read only the addressed actor and
the carried envelope; a handler-plus-transport macro routes their outputs.
Every durable effect is an immutable record on one owned linear wire.  The
reference transition systems contain up to `34,637` states and `140,028`
edges.  Their actor refinement emits checked append-only record deltas on all
`297,980` BORN-plus-TOKEN representative quotient edges and validates one
complete ledger for each of 56 terminal quotient states.  Maximum record
parent arity is two.

The crucial matched control independently implements two carrier algebras.
BORN creates a transaction carrier.  TOKEN activates a pre-existing dormant
slot.  On four finite fixtures their authenticated actor coordination
quotients are edge-for-edge identical, but their complete record algebras are
not.  Birth therefore supplies real support, persistence, addressability and
causal evidence.  It does not supply the protocol's finite-horizon
coordination power.  That power lies in the exclusive fail-fast reservation
and causal closure structure.

A five-round repair campaign removes three hidden global oracles: exact
evidence must be signed; a continuation must grow one persistent ledger; and
participant per-attempt entries plus transaction routing must be keyed by the
carrier-derived structural attempt rather than a global transaction ordinal.
Participant actor roles themselves remain a supplied finite interface.  The
terminal gate closes a transaction at nominal address two with no address-one
actor or record, completes both competing local prepare orders with typed
responses, and proves that inserting an independent transaction leaves all
exact local record bytes unchanged.

The result remains nonselecting.  A symmetric conflict pair has no nonempty
safe deterministic equivariant winner.  Two exact progressing arbitration
kernels survive—component-local random order plus greedy acceptance and a
uniform law on maximal feasible sets—and disagree on a three-proposal path.  A
broader hard-core regional statistical family also survives but need not make
progress.  Raw regional restriction fails without boundary data, and pairwise
overlap consistency does not guarantee a joint finite-cover law.  Birth
opportunity, batch closure, arbitration, retry fairness, crash recovery,
quantum joining and root-free history completion remain extra physics.

The terminal D36 result is therefore neither “birth is merely notation” nor
“birth solves distributed coordination.”  Its exact statement is:

> A born record can durably carry one clock-free causal coordination diamond,
> but safety and closure come from an exclusive fail-fast protocol, and the
> law choosing the opportunity and winner is still absent.

## 1. The answer in ordinary language

Imagine two proposed interactions both need the same current record of A.  A
new transaction record is useful: it gives the proposal a durable identity,
binds its body and capabilities, receives replies and can close the resulting
history.  But merely creating that record does not answer the hard questions.

If the proposal still takes resources one at a time and waits, the new record
is only a named lock request.  If A can promise its same version to both
proposals, both may commit.  If A and B choose independently, one may apply P
while the other applies Q.  If each grants exclusively but waits when busy,
three proposals can each hold one promise and wait forever for another.

The finite positive protocol changes the local response rule:

```text
free and current       append a typed grant and hold one exclusive promise;
busy or stale          append a typed rejection immediately;
all grants             transaction records commit;
any rejection          transaction records abort after its finite replies;
commit at participant  append Apply and advance the protected version;
abort at participant   append Release without advancing the version;
all acknowledgements   transaction appends Close.
```

No actor waits for another actor before producing its grant or rejection.
Transactions may wait for their fixed finite replies, but a busy participant
does not join a wait-for cycle.  Under reliable fair servicing and no crash,
every reply arrives and every attempt closes.

This explains the paper's title.  Birth **carries** the protocol because the
carrier is a real immutable record and the later causal history descends from
it.  Birth does not **select** the protocol opportunity, the participant set,
the conflict boundary or the winner.  Those are separate laws.

Nor does the matched TOKEN control erase ontology.  BORN adds a new support
record.  TOKEN has an old dormant slot plus an activation.  An observer allowed
to inspect the complete record algebra can distinguish them.  Only after
forgetting the carrier presentation do their audited coordination graphs
agree.

## 2. What is inherited and what is new

### 2.1 The V10 boundary before D36

The terminal earlier record establishes the following limits.

1. Sealed records and causal diamonds constrain legal evidence and
   composition, but do not derive a variable-support history law.
2. D24 supplies an exact one-parent conditional newborn-content isometry
   `B_g`.  It does not choose whether birth occurs, the value of `g`, a peer
   set or a joining interaction.
3. D28 separates one-parent support birth from later interaction: birth alone
   cannot create a common operational future between disconnected records.
4. D31 excludes a count-only stationary path-covariant interacting selector
   under its stated none-free, birth-positive, unbounded-growth fork.  It does
   not derive a unique richer selector or locality principle.
5. Papers 21--23 show that a complete history law determines next-conditionals
   and that exact durable-ancestry prediction can require component-sized
   information under a chosen law.  Local event generation alone does not
   imply a small predictive memory.
6. Paper 24 constructs a supplied A-rooted nested-call history family in which
   A's next record is the upper seal of a finite causal call diamond.  It does
   not supply root-free peer overlap, a global history law or numerical birth
   weights selected by SHARD.

D36 attacks the first peer-overlap cell after Paper 24: several proposals may
claim intersecting persistent participant tips.  Its contribution is a finite
probability-free protocol and an actor-record realization.  It is not yet the
overlap-consistent regional probability architecture Paper 24 left open.

### 2.2 Three separate layers

For a proposed interaction `T`, distinguish:

```text
opportunity layer      which proposal exists, with which participants;
coordination layer     how a supplied proposal safely commits or aborts;
selection layer        which feasible conflicting proposal receives priority.
```

Record birth occurs at the opportunity/carrier interface.  The P4 protocol is
the coordination layer.  K1, K2 and K3 below are alternative selection or
regional statistical layers.  Proving the middle layer cannot silently derive
either neighboring layer.

### 2.3 No novelty claim about transactions

Exclusive reservations, fail-fast rejection, commit/abort decisions and
acknowledgement closure are familiar distributed-protocol ingredients.  The
claim here is not that these mechanisms are newly invented.  The contribution
is an ontology and locality audit inside the ISP/SHARD record program:

```text
which protocol facts are immutable records;
which actor owns each state transition;
which apparent global indices are only serializer coordinates;
which causal ancestry certifies closure;
what remains after birth presentation is quotiented;
and which probability law is still missing.
```

The closest standard protocol background is transaction commit.  Gray and
Lamport describe traditional Two-Phase Commit, its zero-fault relation to
Paxos Commit and the fault-tolerance distinction between them.  D36 is not a
new fault-tolerant commit algorithm and does not identify P4 with either full
specification.  Its failure-free coordinator/participant decision pattern is
in that background family; its contribution is the record ontology,
carrier-control comparison, actor-local refinement and construction-ordinal
audit.  Paxos-style consensus, replicated coordinators and crash recovery are
not imported.

## 3. Immutable record ontology

### 3.1 Persistent actors and records

A participant actor A is a persistent typed identity with a succession of
immutable records on one owned wire.  A transaction actor T likewise owns one
wire beginning at its carrier.  Mutable simulator fields such as “current
tip,” “promise,” “phase,” sparse application/response tables and locally
registered authorization tuples are caches of state derived from
authenticated carriers, envelopes and emitted durable records; past records
themselves never change.  Local authorization registration has a durable
witness in the verified carrier/prepare and typed participant response—it is
not a separate `AUTHORIZATION` record type.

The principal record types are:

```text
carrier T0 or activation      supplied proposal attempt begins;
Grant_A or Reject_A           A's typed response at its exact base;
ResponseReceipt_T             T durably receives that response;
DecisionCommit/Abort_T        T's unique monotone decision;
Apply_A or Release_A          A durably acts on the decision;
AckReceipt_T                  T durably receives A's acknowledgement;
Close_T                       T's upper closure seal.
```

The same participant wire may contain records from many attempts.  Every
record has at most two parents; bounded merge chains replace hidden unbounded
parent lists.

### 3.2 Logical transaction and structural attempt

The logical transaction lineage contains structural participant roles and
stable route capabilities.  It does not contain exact remote current tips
that its one-parent carrier could not yet know.  Those exact bases arrive in
authenticated participant responses.

A concrete version-bound attempt is identified by

```text
Attempt(carrier, body)
  = SHA256("structural-attempt", exact carrier record ID, body digest).
```

The body digest commits the member set and requested bases.  Changing the
carrier changes the attempt even if body and base are repeated.  Rebase may
retain logical lineage while creating a different structural attempt.

This digest is an exact finite-model identifier under the declared ideal
collision-free authentication assumption.  It is not a proof that finite
digests inject arbitrary infinite histories or that a homogeneous universe
can equivariantly choose a fresh nominal atom.

### 3.3 Sparse actor-local state

Participant state is keyed by structural attempt:

```text
promise_attempt       one attempt ID or empty;
application_entries   finite attempt -> pending/apply/release map;
response_entries      finite attempt -> exact response record map;
authorizations        finite attempt-first authenticated entries.
```

Transaction actors also inhabit a tuple representation of a finite sparse
keyed registry.  Lookup is by structural attempt; canonical tuple order is only
deterministic serialization, not a constant-time data-structure claim.  The
integer transaction address remains a typed nominal coordinate in records and
in the frozen finite reference adapter, but it neither admits a participant
entry nor locates a live transaction actor.

Participant actor identity is narrower.  D36 supplies a fixed finite
participant interface, and participant transport addresses those supplied
roles by index and capability.  The theorem does not prove participant
discovery or covariance under inserting and renumbering participant actors.
The construction-order repair concerns participant **per-attempt entries**,
global transaction ordinals and transaction-actor routing.

The sparse maps are finite because the theorem supplies a finite attempt
family.  They are not uniformly bounded over unbounded growth.

### 3.4 Exact authentication boundary

Every protocol envelope authenticates:

```text
sender and recipient roles;
transaction and participant address;
body digest and protected base;
stable capability;
structural attempt ID;
exact carried record ID;
participant response-record binding where required;
application code.
```

The record ID commits the complete record kind, payload and parents.  A reduced
header is used only to quotient the finite coordination-state graph; it is not
the physical signed statement.  Forgery, wrong-base substitution, replay,
parent deletion, omitted-field substitution, disconnected lookalikes and
cross-carrier same-base messages all reject before durable mutation.

## 4. Why birth alone fails

### 4.1 Held-resource control

Consider the triangle

```text
P needs A then B;
Q needs B then C;
R needs C then A.
```

Sequential held acquisition reaches the state

```text
P holds A; Q holds B; R holds C.
```

Every proposal waits for its second participant.  The exact graph has 45
states, 69 edges and one circular-wait deadlock.  Adding one inert born ticket
per proposal, while leaving acquisition and waiting unchanged, yields a graph
isomorphic to this one after forgetting ticket decorations.

**Birth-alone no-go.**  A new proposal identity cannot remove a deadlock when
the wait-for transition relation is unchanged.

### 4.2 Reusable grant control

Suppose A emits immutable statements that its current version is zero, but
does not reserve that version for one attempt.  P and Q can each collect a
valid statement about the same base and both commit.  A later atomic
validate-and-advance oracle repairs the double commit only by adding precisely
the regional atomicity that the protocol was meant to explain.

**Read-only insufficiency.**  Evidence that a version once existed is not an
exclusive right to consume it.

### 4.3 Independent adoption control

Suppose each participant decides locally after receiving proposal evidence,
without a unique transaction decision.  A can adopt P while B adopts Q.
Immutable records make this split visible; they do not prevent it.

**Decision insufficiency.**  A safe multi-participant attempt requires one
decision to which every local application is bound, or an explicit primitive
regional operation.

### 4.4 Exclusive waiting control

Now let every participant grant at most one attempt on its version but wait
silently when busy.  The triangle admits two split-vote deadlocks, including

```text
A grants P; B grants Q; C grants R.
```

No transaction has every grant, and each waits for a busy participant.  The
exclusive promise repairs safety but not progress.

**Exclusive-wait no-go.**  Renaming a held reservation as a version grant does
not remove the wait-for cycle.

## 5. The positive protocol

### 5.1 Supplied finite boundary

The theorem fixes a finite set of attempts.  Each has a fixed finite member
set, requested base for each member, authenticated capabilities, exact body
and structural carrier.  The audited capacity cells use:

```text
transaction arity                    at most 3;
participants in a fixture            at most 4;
proposals in an audited region        at most 4;
incident contenders per participant  at most 2;
priority chunk                        at most 2 bits per retry record;
record parent arity                   at most 2.
```

These are exact campaign bounds, not universal constants.

### 5.2 Prepare

T sends one authenticated prepare to every fixed participant.  A participant
checks the exact carrier/body attempt, capability, requested base, signature
and one-use message identity using only its local state and the envelope.

If its base is current and its promise empty, it appends `Grant`, records the
exact response and holds `promise_attempt = T`.  If it is stale or already
promised, it appends `Reject`.  Either way it responds in that local event.

Carrier birth may create T and route prepares.  It may not preinstall
participant application slots, response slots or attempt authorizations.
Those are allocated by each participant's own prepare event after it verifies
the structural attempt.

### 5.3 Decision

T accepts only exact authenticated responses for its own attempt and fixed
participant role.  Each accepted response produces a T-owned receipt.  Once
the fixed finite response set is complete, T appends one decision:

```text
commit   iff every response is Grant;
abort    iff at least one response is Reject.
```

The decision commits the attempt body and the exact response-record
commitment.  Later messages cannot change it.

### 5.4 Local application

T sends the decision to every participant.  A participant accepts it only
when its stored attempt authorization and exact response binding match.

For commit, A additionally requires that the same promise is still held and
the protected version is still current.  It appends `Apply`, advances one
version and clears the promise.  For abort, it appends `Release`, leaves the
version unchanged and clears that attempt's promise if held.  It then sends an
acknowledgement carrying the exact application record.

### 5.5 Closure

T records every acknowledgement.  Only after all fixed acknowledgements are
present does T append `Close`.  Participant records remain on participant
wires; Close does not retroactively mutate them or become their common wire
successor.  It is T's causally justified summary of the completed protocol
diamond.

The implementation is therefore macro-atomic only as a completed history.
Intermediate partial-application records are physical and appear in the
reference state graphs.  A primitive one-step multiwire oracle would hide
those states and is a distinct model.

## 6. Reservation safety and closure theorem

### 6.1 Assumptions

The theorem assumes:

```text
a supplied finite attempt family and fixed bodies;
ideal authentication and collision-free exact record identity;
honest record-generating participant and transaction actors;
reliable message delivery;
failure-free actors and transaction coordinators;
fair complete servicing of every addressed finite mailbox;
local atomic append on one owned actor wire.
```

There is no elapsed-time, rate, timeout or lease assumption.

### 6.2 Exclusive-base lemma

At one participant version, at most one attempt holds the participant's
promise.  A commit application succeeds only for that exact promised attempt
and exact version.  Therefore two incompatible attempts cannot both consume
the same protected participant base.

### 6.3 Unique-decision lemma

The transaction phase is monotone.  It accepts at most one response per fixed
participant, binds their exact records, and creates one commit or abort
decision after the finite response set is complete.  Every accepted local
application cites that decision and the participant's stored response.  Split
participant decisions are excluded.

### 6.4 Fail-fast progress lemma

A participant never waits for another transaction before replying to a valid
prepare.  A free current participant grants; a busy or stale participant
rejects.  Thus the circular wait of the exclusive-wait protocol is absent.

With reliable delivery, failure-free handlers and fair servicing, every fixed
participant response reaches T.  T decides, every decision reaches its fixed
participants, every valid participant applies or releases and acknowledges,
and every acknowledgement reaches T.  Hence the attempt closes.

This is causal-extension liveness, not a statement about seconds.  It says
every supplied failure-free attempt terminates under fair complete servicing.
It does not bound the number of serializer steps, choose an interleaving or
guarantee that a later retry opportunity exists.

### 6.5 Closure-ancestry lemma

Every response record is an ancestor of the decision through T's response
receipts.  Every apply/release record is an ancestor of a T acknowledgement
receipt.  The T receipts form one linear owner wire ending at Close.  Therefore
the complete set of transaction-relevant carrier, response, decision,
application and acknowledgement records lies below Close.

### 6.6 Theorem

**Closed-attempt actor-record theorem.**  Under the assumptions of section
6.1, every supplied finite attempt closes commit or abort.  No incompatible
closed commits consume the same protected base; no admitted application uses
a stale or unpromised base; every durable effect lies on one authenticated
append-only owner wire; and no numerical clock or held-wait cycle is required.

The theorem does not establish linearizable all-wire visibility at one event.
It establishes a typed closed causal diamond with visible intermediate local
records.

## 7. Exact finite evidence

### 7.1 Reference transition systems

The probability-free reference enumerates all asynchronous message services
for four fixtures:

```text
fixture          states      edges    terminal states
pair              1,113      2,984          8
triangle         34,637    140,028         17
disjoint            289        816          1
partial overlap   1,517      5,162          2
```

Every terminal is typed and every graph is acyclic.  The terminal
multiplicities count canonical states, not probabilities of service orders.
The graphs contain 232, 9,420, 120 and 518 partial-application states,
respectively, showing exactly what the atomic regional oracle would hide.

### 7.2 Authenticated actor refinement

Independent participant and transaction actors refine those four reference
graphs in both BORN and TOKEN modes.  The forgetful projection is exact on
every state and edge.  Across both modes:

```text
representative coordination-quotient edges with checked record deltas 297,980
complete terminal-ledger path lifts                                      56
maximum terminal ledger records                                           39
maximum parent arity                                                        2
```

The 297,980 edge checks are one authenticated causal representative per
coordination-quotient edge.  The 56 ledgers are one complete path lift per
terminal quotient state.  They are not a census of every exact record history;
different same-actor service orders may produce distinct valid record IDs.

### 7.3 Negative authentication battery

Fourteen attacks reject before durable mutation or output creation.  They
include forged response, wrong-base grant, forged decision, forged ack,
prepare replay, duplicate application, unissued capability, disconnected
recipient lookalike, parent deletion under an old signature, substitution of
a payload field omitted from the quotient header, a nonexistent decision
parent, two same-base cross-attempt replays and a side-authorized attempt not
derived from its carrier.

This battery supports the exact physical signature boundary.  It does not
prove Byzantine agreement or remote predecessor-wire validity against a
malicious record-generating actor; the theorem assumes honest record
generation.

### 7.4 Persistent continuation

In both carrier modes, one world begins at participant version one with a
stale version-zero attempt.  That attempt receives typed rejections and closes
abort.  A new version-one attempt is then opened from the actual terminal
actors and ledger.  Old heads, capabilities, used messages and record bytes
persist; the new attempt has a new carrier-derived identity and descends from
the old close.  It commits and advances both participants to version two.

Both combined ledgers validate, preserve the old prefix, place the old close
below the new close and reject an old envelope after rebase.  The two histories
contain 50 records in total.

## 8. Birth versus dormant activation

### 8.1 Matched carriers

The eliminability test holds validation, participant roles, attempts,
exclusive promises, decisions, application and closure fixed.  It varies only
the carrier presentation:

```text
BORN    append a new transaction carrier descended from its supplied parent;
TOKEN   activate a bounded dormant transaction slot already in the record algebra.
```

These are independently constructed actor worlds, not one graph decorated by
two constant labels.

### 8.2 Coordination-quotient equivalence

For pair, triangle, disjoint and partial overlap, erasing only birth/token
presentation yields the same authenticated coordination graph in both
directions.  Every projected state, edge and terminal commit-observable class
matches.  The persistent stale/rebase continuation succeeds in both modes.

**Finite-horizon eliminability theorem.**  At the supplied audited horizon,
fresh support is not required for the exclusive fail-fast protocol's
coordination behavior.  BORN and TOKEN are equivalent after projection to the
declared coordination observables.

### 8.3 Why this is not ontological equivalence

The full record supports differ.  BORN contains a fresh support record.  TOKEN
contains a pre-existing dormant slot and activation.  Their exact record
identities and ancestry are observably distinct.  No isomorphism of complete
record algebras is claimed.

The conclusion is therefore asymmetric:

```text
birth is useful physical carrier structure             yes;
birth is the source of P4's audited coordination power no;
birth is eliminable from every record observable       no;
birth is eliminable in an unbounded universe           not proved.
```

## 9. Construction order is not a hidden address

### 9.1 Participant-local admission

Earlier candidate implementations admitted a participant attempt only when
its global transaction index equaled the length of a dense participant array.
That made an unrelated transaction elsewhere decide whether A could respond.

The terminal law instead allocates one sparse entry after A verifies the
carrier-derived attempt in A's own prepare event.  Carrier birth changes only
T's carrier and transport mailboxes; it does not prewrite participant
predictive state.

### 9.2 Structural transaction routing

The surrounding transaction registry is also sparse.  Responses are routed by
the attempt ID carried in the authenticated envelope.  Transaction service and
replacement use that same key.  A nominal address is never used as a live
tuple subscript.

The terminal gapped run starts with a closed address-zero attempt, opens only
address two and runs ordinary prepare, response, decision, application,
acknowledgement and close services.  It has no address-one actor or record:

```text
gapped tx2 closed                    1 / 1
no tx1 actor or record               1 / 1
combined ledger records                 24
maximum parent arity                     2
```

### 9.3 Both local prepare orders

Two attempts at nominal addresses one and two are opened from the same closed
base.  Each local order is serviced at both participants and the complete
world then runs to quiescence.  The locally first attempt receives grants and
closes commit.  The other receives busy rejections and closes abort.

```text
complete local-order histories       2 / 2
typed response records               8 / 8
missing or padded local slots             0
```

The two histories show that the probability-free protocol can realize either
winner under different supplied delivery histories.  They do not assign a
probability to those histories.

### 9.4 Disjoint insertion

In the disjoint fixture, one run contains only local `P(A,B)` plus four
participant seeds.  Another also contains and closes `Q(C,D)`.  Restriction to
the A, B and P owner wires yields exactly the same 13 complete records,
including IDs, payloads, parents and signatures.

The absent-Q branch removes Q's actor, carrier, prepares and Q-specific
application, response, capability and authorization entries on C/D.  It is
therefore a pure absent remote-transaction control, not merely a dormant remote
mailbox comparison.

Thus a serializer may interleave the remote component, but no remote insertion
changes local physics.  This is full-ledger covariance, not merely equality of
a reduced state label.

## 10. Arbitration remains unselected

### 10.1 Deterministic covariance obstruction

Take two structurally symmetric conflicting proposals P and Q.  The boundary
automorphism swaps them.  A deterministic equivariant selected set must be
swap-invariant.  Among safe feasible sets, only the empty set is invariant:
`{P,Q}` is unsafe and each singleton breaks the symmetry.  Progress excludes
the empty set.

Therefore a nonempty safe deterministic winner requires physical asymmetry,
or the law must be stochastic.  A fresh nominal spelling is not acceptable
asymmetry because relabeling can move it.

### 10.2 K1 — component-local random order

On each connected conflict component, sample a strict proposal order uniformly
and greedily accept proposals when their participants remain unused.  This is
safe, maximal, covariant and factors on disjoint components when the physical
mark is one order per component.  Cross-component shuffles of a global
presentation order are gauge.

On the three-proposal path `P-Q-R`, K1 gives

```text
{Q}       1/3
{P,R}     2/3.
```

### 10.3 K2 — uniform maximal feasible set

Choose uniformly among maximal feasible sets.  This is also safe, progressing,
covariant and disjoint-factorizing.  On the same path it gives

```text
{Q}       1/2
{P,R}     1/2.
```

K1 and K2 therefore disagree while satisfying the declared finite symmetry
and progress conditions.

### 10.4 K3 — hard-core regional family

For supplied rational activity `lambda > 0`, assign

```text
kappa(W) proportional to 1[W feasible] lambda^|W|.
```

The family is normalized, covariant, disjoint-factorizing and has the exact
single-site conditional

```text
P(T accepted | every neighbor rejected) = lambda/(1+lambda);
P(T accepted | some neighbor accepted)   = 0.
```

It can select the empty or a nonmaximal feasible set, so it is a regional
statistical specification rather than a progress protocol.  `lambda` is not
derived.

### 10.5 Nonselection theorem

**Arbitration nonselection.**  The inherited record, covariance, finite
feasibility and disjoint-factorization requirements do not uniquely select an
arbitration law.  K1 and K2 already separate on the path; K3 supplies a wider
unselected activity family.  P4 safely realizes a supplied selected attempt
set or supplied delivery history but does not choose its distribution.

## 11. Batch closure, restriction and overlap

### 11.1 The closed-boundary assumption

K1 and K2 require a supplied finite contender batch.  A batch-close mark says
no additional contender belongs to that arbitration cell.  Without it, a
locally greatest currently visible proposal need not remain greatest when a
later contender appears.

P4 can still safely close online attempts without knowing all future
contenders: an exclusive successful prepare makes later proposals on the old
base stale.  But P4 does not claim that the resulting winner is distributed by
K1 or K2, nor that every losing logical transaction gets a future retry.

### 11.2 Raw restriction failure

On the conflict path `P-Q-R`, restrict the larger K1 law to the edge `P-Q`.
The result is

```text
larger path restricted   P: 2/3, Q: 1/3;
direct edge law          P: 1/2, Q: 1/2.
```

External R changes Q's boundary condition.  Therefore “run on a larger region
and forget” is not generally the same as “run directly on the subregion.”

For K3, retaining an explicit external-blocker boundary field repairs the
conditional mixture identity.  This confirms Paper 24's warning: an oriented
regional law needs incoming and lateral boundary data, not bare overlap sets.

### 11.3 Pairwise agreement is insufficient

Three binary region variables can be pairwise anticorrelated while admitting
no joint support.  Pairwise marginal agreement is therefore not a global
finite-cover theorem.  A root-free regional history architecture still needs:

1. a category of oriented finite causal regions and embeddings;
2. incoming conditioning interfaces, generated upper/outgoing records and
   lateral collars;
3. extraction, restriction and boundary-transport maps;
4. conditional kernel-composition identities;
5. positive joint extensions on every finite overlapping cover; and
6. a measurable global history space plus an existence theorem.

D36 supplies finite conflict cells and negative controls for that program.  It
does not complete the program.

## 12. Retry, crashes and scaling

### 12.1 Bounded marks do not imply bounded resolution

For `k` symmetric contenders drawing a `b`-bit priority mark from `M=2^b`
values, the probability of a unique greatest mark is

```text
U(k,M) = k/M^k * sum_(s=0)^(M-1) s^(k-1).
```

For two one-bit contenders, `U=1/2`; conditional on a fresh independent retry
after every tie, unresolved mass after five attempts is `1/32`.  Almost-sure
resolution and expected attempts follow only after the continued retry
opportunity is supplied.  The worst-case number of bounded retry records is
unbounded.

### 12.2 Failure-free is load-bearing

If a transaction coordinator disappears after participants grant, their
exclusive promises may remain held.  Safe unilateral expiry requires a clock,
lease, failure detector or additional recovery protocol.  D36 supplies none.
It therefore makes no crash-tolerance claim.

Reliable messages and fair complete servicing are likewise theorem
assumptions, not derived physical laws.  The implementation tests no loss,
duplication beyond replay rejection, partition or Byzantine remote ancestry.

### 12.3 Finite is not uniformly bounded

Every audited record is bounded and every finite supplied world has finite
sparse tables.  Nevertheless, indefinite interaction can create arbitrarily
many attempt entries and retry records.  No uniform finite-memory,
nonexplosion, infinite-ledger projectivity or starvation theorem follows from
the finite receipts.

## 13. Relation to record birth and quantum content

### 13.1 D24 and D36 answer different questions

D24's `B_g` says what one admitted newborn receives on one one-parent content
family.  D36 says how a supplied classical transaction attempt can collect
authenticated participant responses and close a multiwire causal protocol.

The two layers are:

```text
birth opportunity and content    q_birth plus B_g;
post-birth coordination          prepare/grant/decision/apply/ack/close.
```

D36 does not derive `q_birth` or `g`.  Conversely, `B_g` does not provide
exclusive promises, conflict arbitration or the multi-participant join.

### 13.2 Graph-shape compatibility is not a quantum realization

The proposal carrier can have one causal parent, matching D24's bounded birth
shape.  Later grant collection, decision and participant application have
multi-parent causal content represented by bounded merge chains.  No common
Hilbert-space isometry, instrument normalization, NSE distinguishability
proof or entangled joining map is supplied for that protocol.

Therefore `proposal_birth_one_parent=1` and `quantum_join_derived=0` must remain
together.  A quantum realization is a separate investigation.

### 13.3 Birth remains physical

The eliminability theorem is about one coordination quotient.  In the full
record ontology, a born support can participate in other future observables,
carry quantum content, change capacity and seed new causal descendants.  None
of those observables is erased by the finite matched control.

The correct interpretation is not “birth is fake.”  It is:

> birth is not a substitute for the interaction and selection laws that act
> on the born support.

## 14. Relation to Paper 24's clock-free next click

Paper 24 proves that, in a supplied A-rooted nested-call family, A's next wire
successor can be the upper seal of a finite call diamond without a numerical
clock race.  D36 proves an analogous probability-free coordination fact for a
supplied finite peer-overlap attempt: its close is the upper seal of a typed
prepare/response/decision/application diamond.

The common lesson is that local causal succession does not require seconds.
The important distinction is selection:

```text
Paper 24 supplies Q1 or Q2, so it has a complete rooted probability family;
D36 supplies attempts and services but no probability on interleavings or winners.
```

D36 also does not remove Paper 24's root-free opening.  Participants are
reached through supplied capabilities, attempt bodies and finite fixtures.
There is no law discovering an arbitrary peer, joining disconnected
components, deciding which actor initiates next or completing consistent
overlapping regions into one universe history measure.

## 15. What the executable is and is not

### 15.1 Logical actors

Participant and transaction objects own separate state and mailboxes.
`handle_participant` and `handle_transaction` read only the addressed actor and
the carried envelope.  The surrounding Python process enumerates which
nonempty mailbox to service and then transports outgoing messages.

`service_world` is therefore a **handler-plus-transport macro**.  One handler
changes its addressed durable state; the driver then inserts emitted envelopes
into recipient mailboxes.  It is not claimed to be a literal transition of
one operating-system process or to mutate only one Python object.

### 15.2 No physical global scheduler

The finite checker sees all mailboxes to enumerate the state graph and to run
deterministic replay.  Its loop index, sorting key and chosen linear extension
are proof machinery.  No theorem identifies them with universal time,
simultaneity, energy, rate or a physical global queue.

Disjoint service diamonds commute, and the exact disjoint-insertion gate
preserves local record bytes.  Alternative services at one participant can be
physically different histories because they decide which attempt receives the
exclusive grant.  A probability law over those alternatives is not supplied.

### 15.3 Reference adapter

The dense frozen reference model is retained as a finite analysis coordinate
system.  `project_reference()` explicitly requires all nominal fixture
indices, orders actors by those declared indices and forgets exact record
bytes.  Sparse full-ledger gates bypass that adapter and validate the physical
actor registry directly.

The reference is a theorem oracle for the declared finite cells, not the
ontology of the actor implementation.

## 16. Reproducibility

The terminal D36 artifacts are:

```text
note-d36-record-birth-causal-coordination.md
code/d36_birth_coordination_exact.py
data/d36_birth_coordination_exact.out
code/d36b_actor_record_refinement_exact.py
data/d36b_actor_record_refinement_exact.out
code/d36_replay_integrity_exact.py
data/d36_replay_integrity_exact.out
reviews/d36-round1-* through reviews/d36-round6-*
```

The committed results are:

```text
reference model                 PASS 22/22
actor-record refinement         PASS 14/14
external deterministic replay  PASS 8/8
```

Deterministic identifiers:

```text
reference source  2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683
reference stdout  868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17
reference science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source      57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b
actor stdout      eaf2e535b475b9f3fafe080175a5399e2748c0a554ed768f470869cfdf291b48
actor science     7bee23d9ebf22b2a0112ec0677f3b584990ef9a09a4e4ef34b77e75e7bca53d0

replay source     af3d773e11095bd125126a01028ffc83c7c91129fc6c921faa52dd173287ce98
replay stdout     9324aec40ad8f184058d75ea2870ed9628823971ee7ca0e591e28b5af0b06110
```

The terminal D36 review stream ends with a focused structural-routing delta at
`0B/0M/0m/0n`.  Paper-level review may challenge this synthesis without
silently rewriting those terminal artifacts.

## 17. Decision table

```text
Question                                              Answer
----------------------------------------------------  ------------------------
Can born proposal records be useful causal carriers?   yes
Does nominal ticket birth remove held-wait deadlock?   no
Can immutable read-only grants ensure exclusive use?   no
Can exclusive waiting grants ensure progress?          no
Can exclusive fail-fast attempts close without time?   yes, at stated scope
Are participant per-attempt entries structurally keyed? yes
Is transaction routing structurally attempt keyed?     yes
Are participant roles discovered/insertion-covariant?  no; supplied fixed roles
Does a skipped global transaction address work?        yes, through full close
Do disjoint insertions change exact local records?      no, in the audited cell
Are BORN and TOKEN full record algebras identical?      no
Are their audited coordination quotients equivalent?   yes
Is arbitration selected?                               no
Is retry fairness derived?                             no
Are crashes handled?                                   no
Is the quantum join derived?                           no
Is a root-free global history law completed?           no
```

## 18. Candidate paper-level conclusion

The finite transaction cell answers one part of the post-Paper-24 overlap
problem.  Persistent record actors can safely coordinate a supplied
overlapping attempt without a numerical clock, a held-wait cycle or an atomic
multiwire mutation.  Every local effect is durably recorded and every closed
attempt has complete causal ancestry.

The repair history matters to the theorem.  Exact record ancestry must be
authenticated, continuations must grow one real ledger, participant
registration must occur in the addressed event, and participant per-attempt
tables plus the transaction registry must be keyed by structural attempt
rather than global transaction construction ordinal.  Once those conditions
hold, skipped nominal transaction addresses and disjoint transaction
insertions are physically harmless at the audited cells.

But birth is not the missing law.  BORN and TOKEN differ as record ontologies
while agreeing in the audited coordination quotient.  The protocol's work is
performed by exclusive version-bound promises, fail-fast typed rejection, a
unique decision, local application and acknowledgement closure.  Even that
protocol does not tell nature which opportunity appears or which contender
wins.

The strongest candidate noun is therefore:

```text
CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION /
SUPPLIED FINITE FAILURE-FREE ATTEMPTS / NONSELECTING.
```

Paper-level hostile review must preserve all qualifiers.  In particular, this
paper is not evidence for a universal transaction coordinator, global
scheduler, chosen probability law, Byzantine or crash tolerance, bounded
infinite memory, quantum joining instrument, Lorentzian spacetime, cone
geometry, dimension, units or gravitational coupling.

The next constructive target is the one D36 deliberately leaves exposed: an
oriented overlap-consistent regional history specification that supplies
opportunities and arbitration, agrees on every finite cover, admits a global
completion and can then be tested for a genuine quantum realization.  Only
after that architecture exists can record birth be assessed as part of a
root-free universe law rather than as the carrier of one supplied finite
coordination diamond.

## 19. Paper-level hostile review and repair

The candidate draft was frozen at `64f0bf9` and subjected to one disclosed
coordinator self-hostile review:

```text
blockers  0
majors    2
minors    3
nits      1
```

The report is
`reviews/paper25-round1-coordinator-hostile-review.md`.  It is not represented
as an independent lane.

The two majors were paper-scope failures, not failures of D36's safety core.
First, the decision table conflated sparse participant per-attempt state and
structural transaction routing with participant actor identity.  The repaired
paper now states that participant roles are a fixed supplied interface
addressed by role index and capability; participant discovery and insertion
covariance are unproved.  Second, the disjoint comparator removed Q's actor,
carrier and mailboxes but retained Q-specific predictive entries on remote C/D
actors.  The strengthened committed gate removes those entries too.  A13's
exact tuple, 13-record restriction and family hash remain unchanged; actor and
replay receipts remain `PASS 14/14` and `PASS 8/8`.

The minor repairs position D36 against Gray--Lamport transaction-commit
background without importing fault tolerance, distinguish K1/K2 progressing
arbitration from nonprogressing K3, and identify authorization tables as
derived caches rather than an unimplemented record kind.  The nit now calls
the transaction collection a tuple representation of a finite keyed registry.

The strongest paper status after these repairs is **coordinator-closed
candidate**, not independently terminal.  The theorem and receipts are frozen;
an independent paper-level hostile stream may still challenge the synthesis.

## References

1. Relativistic ISP v10 Paper 19, *The complete interactive record law at the
   declared interface*.
2. Relativistic ISP v10 Paper 21, *Local generators do not imply local
   memory*.
3. Relativistic ISP v10 Paper 22, *The predictive record-DAG boundary*.
4. Relativistic ISP v10 Paper 23, *The whole component is the exact ancestry
   boundary*.
5. Relativistic ISP v10 Paper 24, *A's next click is the upper seal of a causal
   call diamond, not the winner of a clock race*.
6. D36 terminal note, `note-d36-record-birth-causal-coordination.md`.
7. J. Gray and L. Lamport, *Consensus on Transaction Commit*, ACM Transactions
   on Database Systems 31(1), 133--160 (2006), MSR-TR-2003-96;
   [Microsoft Research publication page](https://www.microsoft.com/en-us/research/publication/consensus-on-transaction-commit/).
