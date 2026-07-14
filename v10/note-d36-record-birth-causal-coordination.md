# D36 — record birth as causal coordination

**Status:** ROUND-3 HOSTILE DELTA OPEN; PARTICIPANT-LOCAL ATTEMPT OPENING REQUIRED.
**Date:** 2026-07-14.
**Parent:** terminal D35 / Paper 24 at commit `8b589e2`.

## 1. Question

Can a fresh record help long-lived record actors coordinate overlapping local
interactions without held-resource deadlock, a privileged root, a physical
global queue or numerical time?

The investigation does **not** assume that every actor is replaced at every
interaction, that a transaction ticket is fundamental, or that D24 already
contains arbitration.  Its sharper question is:

> After matching validation, arbitration and commit semantics, does a born
> transaction actor add causal coordination power over immutable proposal and
> grant records, or is birth only a durable representation of a protocol whose
> real work is done by an exclusive multi-tip seal and a selection law?

## 2. Inherited boundary

D36 inherits the full 441-artifact pre-D35 census and terminal supersessions.
The load-bearing record is:

1. V6 sealed/born composition makes complete realized history relevant but
   does not select the underlying process law.
2. V7/V8 click-law claims remain conditional on supplied bridge, stationarity
   and placement data where so marked; nominal construction order is not
   physical time.
3. D24 supplies a selected one-parent conditional content isometry `B_g`; it
   does not select birth opportunity, `g`, partner set, priority or join law.
4. D28 proves one-parent birth alone cannot create common operational futures;
   post-birth interactions are needed, while the opportunity kernel remains
   extra physics.
5. D31 excludes count-only stationary path-covariant interaction at unbounded
   growth under its stated hypotheses; it does not force locality or a unique
   richer selector.
6. D33--D34 show that a complete history measure would answer conditionals,
   but local-clock/race constructions add time/rate data and do not solve NSE
   or predictive-memory questions by themselves.
7. D35 proves a supplied A-rooted nested-call family can define exact next-A
   probabilities without numerical time.  Root freedom, peer overlap, joins
   and the regional specification remain open.
8. D24 G4 already warns that, at fixed finite scope, fresh support birth may be
   observationally equivalent to activation of dormant capacity.

The fresh D36 keyword search finds no accepted earlier theorem that transaction
record birth solves distributed overlap.  Earlier occurrences of transaction,
reservation or arbitration language are not imported as a completed protocol.

## 3. Ontology normalization

The attachment's mutable-record language is repaired before modeling.

```text
actor/wire A       persistent typed identity with successive immutable tips;
A_i                one immutable record on A's wire;
T0                 immutable realized proposal record;
G_A(T0,A_i)        immutable grant referencing A's exact base tip;
J_A(T0,reason)     immutable rejection or stale certificate;
T1                 immutable rebase record referencing T0 and new bases;
C_T                immutable successful commit/upper seal;
U_A(C_T)           A's next adoption/successor record, if separately modeled.
```

No record is appended to or changes status.  Status is derived from later typed
records.  An unresolved proposal is one with no terminal successor yet.

Unselected alternatives in a probability kernel are not realized records and
need no rejection record.  A syntactically invalid envelope may reject before
mutation, as in D35.  Once a valid proposal is sealed, every grant, rejection,
supersession or rebase that affects later physics persists.

The **transaction identity** is not an arbitrary fresh nominal atom.  In the
finite exhibit it is the typed structural identity

```text
tau = (initiator lower-tip identity, bounded local output slot,
       ordered capability roles, stable participant capabilities).
```

Relabeling records relabels `tau`; printable spelling has no priority.  This is
a finite exhibit, not a root-free global freshness theorem.  A transaction may
name only participant records reached through existing capabilities.  Naming a
disconnected participant would already assume the missing bridge/join law.
Exact participant current tips are not in `tau`: authenticated grant records
bind them later into a separate version-bound **attempt identity**.  A rebase
keeps the logical transaction lineage while creating a new attempt identity.

## 4. Capacity pin

The exact campaign uses bounded cells:

```text
transaction arity                    at most 3;
participants in a fixture            at most 4;
proposals in one audited region       at most 4;
incident contenders per participant  at most 2;
priority chunk                        b in {1,2} bits per retry record;
record parents/evidence fields        explicitly enumerated, no hidden list;
retry/rebase history                  one new bounded record per attempt.
```

No digest is treated as an injective compression of arbitrary evidence.  No
single record contains an unbounded queue, participant set or retry history.
These bounds make the finite theorem exact; they are not asserted uniformly
over the universe.  A later scalable law needs either a uniform incidence/arity
bound or a bounded-arity tree of merge records.

## 5. Conflict object

At a supplied finite causal boundary `b`, let `T(b)` be the realized proposals.
Each proposal names a finite participant set and exact base-tip version for
each participant.  Two proposals conflict when they claim the same participant
base version incompatibly.  More generally, minimal forbidden sets form a
conflict hypergraph

```text
H_b = (T(b), E_b).
```

A set of commits is feasible exactly when it contains no forbidden hyperedge.
For the first receipt every conflict is pairwise, so feasibility is an
independent set of the conflict graph.  One three-way-only forbidden hyperedge
is reserved as a generalization gate; it must not be silently reduced to
pairwise conflict.

## 6. Probability-free protocol ladder

The exact state checker compares matched semantics, not a favorable protocol
against an unrelated lock baseline.

### P0 — sequential held mutexes

Transactions acquire participant locks one at a time and hold them across
waits.  The triangle

```text
P: A then B;  Q: B then C;  R: C then A
```

has the circular-wait witness `P holds A, Q holds B, R holds C`.  Adding a
fresh transaction identity without changing lock semantics must leave the
reachable state graph isomorphic.

### P1 — nonexclusive read-only grants

Participants issue immutable grants naming their current version, but may
grant the same version to several proposals.  If commit trusts those grants
without an exclusive version transition, two conflicting proposals can both
commit.  Final atomic validate-and-advance repairs safety only by adding a
bounded multi-participant atomic oracle; the receipt must attribute safety to
that oracle, not to ticket birth.

### P2 — participant-local adoption without an atomic seal

After collecting grants, participants independently adopt proposals.  Two
participants can adopt different conflicting proposals, leaving partial
commits.  This is the exact countermodel to hiding atomicity in “simultaneous
validation.”

### P3 — exclusive grants that wait

Each participant grants at most one proposal per base version and holds that
promise while the transaction waits.  This prevents two overlapping
transactions from collecting complete grant sets, but the triangle admits

```text
A grants P;  B grants Q;  C grants R.
```

If a busy participant merely waits, every transaction holds one promise and
awaits another.  This is the same coordination deadlock in immutable-record
clothing.  Calling the promise “version evidence” does not change its lock
semantics.

### P4 — exclusive fail-fast prepare/abort/apply/close

This is the positive finite reference semantics intended for an independent
actor-local refinement:

1. an initiator locally births `T0` and sends authenticated prepares to its
   fixed finite participants;
2. participant `i` handles the prepare in one local wire event, granting iff
   its exact tip is current, it is authorized and its promise slot is free;
   the grant installs an exclusive promise until T's unique decision;
3. a busy or stale participant replies with an immediate typed rejection—it
   never waits for another transaction;
4. T records one monotone commit decision after all grants or abort after any
   rejection;
5. T sends the decision; each participant locally appends `Apply_i` or
   `Release_i` and acknowledges; and
6. only after every acknowledgement does T append `Close(T)` as the causal
   upper closure seal.

Under authenticated reliable messages, failure-free actors/coordinator and
fair delivery, every finite attempt commits or aborts.  Split grants cause
aborts and releases rather than circular wait.  The protocol is safe because
the exclusive promise survives from grant through apply/release.  It does not
prove retry success or starvation freedom, and the promise is a reservation
even though no mutex object is stored.

The closure seal advances only T's wire.  Participant wires advance through
their own local apply/release records.  The closed diamond is macro-atomic as a
completed history; no single local click is claimed to mutate several wires.

### P5 — atomic multiwire oracle control

As a comparison, admit one primitive operation that simultaneously validates
and advances every participant tip.  It is safe by definition and resembles
D35's shared-world `sync_tips` transition.  The receipt must label it an
atomic regional oracle, not a derivation from local tickets.  Comparing P4 and
P5 exposes the intermediate partial-application states that the oracle hides.

### P6 — closed batch plus component-local strict arbitration orders

A supplied finite boundary seal declares the contender batch closed.  Every
connected conflict component carries one physically readable strict proposal
order.  Proposals in disconnected components are incomparable; a global
presentation shuffle between them is construction gauge.  Process each
component from greatest to least mark, accepting a proposal iff its complete
participant set remains unused.  This returns a maximal independent set and
provides a finite arbitration **specification** for P4 attempts.

The batch-close record solves the unknown-future-contender problem and each
component-local strict mark supplies symmetry breaking.  Neither comes from
freshness.
The accepted set may be realized through P4's local commit/abort/apply/close
diamonds; no multiwire mutation is implied.

### P7 — online priority without a close

If a participant decides after seeing the currently greatest proposal, a later
higher contender can invalidate the claim; if it waits for every possible
higher contender, it cannot know none will arrive.  The safe P4 alternative is
weaker: a successful exclusive prepare closes the cited participant tip and
makes unseen proposals stale.  Priority biases observed conflicts; it is not a
census of all concurrent/future contenders.

## 7. Exact structural theorems and no-gos

### N1 — nominal freshness obstruction

No deterministic equivariant function can choose one unused atom from a
homogeneous infinite nominal namespace.  A permutation fixing the used set but
moving the alleged fresh atom is a contradiction.  Structural typed identity
is therefore required; fresh spelling is not physics.

### N2 — birth-alone deadlock no-go

If born tickets retain held-resource acquisition, the projection that forgets
ticket nodes is a transition-system isomorphism to P0.  Ticket creation alone
cannot remove the circular wait.

### N3 — read-only ticket insufficiency

If two conflicting proposals can collect reusable grants on one participant
version and commit does not perform an exclusive transition visible to that
participant, some service order commits both.

### N4 — deterministic covariance obstruction

For two structurally symmetric conflicting proposals `P,Q`, the boundary has
an automorphism swapping them.  A deterministic equivariant selected set must
be invariant.  The invariant choices are `{}` and `{P,Q}`; liveness forbids the
first and safety forbids the second.  A physical asymmetry or stochastic law is
necessary.

The same argument applies to a transitive symmetric conflict orbit whenever
no nonempty feasible subset is automorphism-invariant.

### N5 — exclusive waiting grants do not imply progress

P3's triangle split vote is terminal when busy participants wait.  Exclusive
evidence is a reservation; removing a mutex data type has not removed the
wait-for cycle.  P4 escapes only by fail-fast rejection and abort/release.

### N6 — one-seal multiwire locality obstruction

If a local transition may append only its addressed actor's wire, no T-local
event can also be the successor on several participant wires.  A joint
successor is an additional bounded regional instrument.  Otherwise participant
apply records and their intermediate states are physical.

### T1 — closed-attempt reservation-safety theorem

For a supplied fixed finite batch of base-version-zero attempts, authenticated
reliable messages, local
atomic wire appends, exclusive version-bound promises held until one monotone
T decision, immediate reject when busy, failure-free actors/coordinator and
fair delivery, every attempt terminates commit or abort.  No stale or double
consumption is possible, no wait-for cycle exists, and disjoint attempts
commute when identities, randomness and supports are disjoint.  No numerical
clock enters.  Retry termination and starvation freedom do not follow.

### T2 — causal closure decomposition

Every successful P4 macro-transaction has the append-only diamond

```text
participant lower tips -> proposal/prepares -> grants -> commit decision
 -> participant apply records -> acknowledgements -> T closure seal.
```

Participant actors remain active and every immutable past record remains.
`Close(T)` is locally generable from T's causal past and summarizes the closed
diamond; it is not an atomic multiwire mutation.  The construction lies outside
D24's one-parent content theorem at the join/application layer.

### T3 — closed ordered-batch theorem

On every finite closed conflict graph with a strict proposal order on each
connected component, the
greedy accepted set is feasible, maximal and nonempty when proposals exist.
The result depends only on the marked graph, not the machine serializer.
Disjoint components factor at the full physical-mark level because their
orders are sampled separately.  A global permutation is only a presentation:
on two two-proposal components its 24 orders quotient to four component-order
atoms, with six gauge shuffles per atom.  Each selected attempt may then be
realized by P4.

### T4 — finite-horizon eliminability test

Compare two protocols with identical validation, priority and atomic-seal
semantics:

```text
BORN       create a fresh transaction actor/record;
TOKEN      activate a pre-supplied dormant transaction slot or carry tau in
           immutable participant-local proposal/grant records.
```

After forgetting inactive-slot and born/token presentation fields, their
independently generated authenticated actor **coordination quotients** and
declared participant/commit observables should be bisimilar.  Their full record
algebras are expected to differ: BORN contains a new support record while
TOKEN contains a pre-existing dormant slot and an activation record.  Passing
proves only that fresh support is not required for this protocol's bounded
coordination behavior.  It does not make birth representational in every
observable or ontologically absent at all scales.

## 8. Time-free probabilistic arbitration

Probability is placed on arbitration marks or feasible commit sets, not on a
race in seconds.

### K1 — uniform random strict order plus greedy acceptance

On a finite closed batch, sample every strict proposal order with probability
`1/n!` within each connected conflict component, then apply P6/T3's greedy
rule.  Each component order is a physical arbitration mark, not machine
service order.  The induced kernel is automorphism-covariant and factors on
disconnected conflict components at both marked-history and accepted-set
levels.

### K2 — uniform maximal-independent-set law

Assign equal probability to every maximal feasible commit set.  This is safe,
progressing, covariant and disjoint-factorizing on finite graphs, but differs
from K1 on the three-proposal path.  If both survive, the present principles do
not select arbitration.

### K3 — hard-core regional family

For rational activity `lambda > 0`,

```text
kappa_b(W) proportional to 1[W feasible] * lambda^|W|.
```

This family is exactly normalized, covariant and factorizes on disjoint
components.  Its single-site conditional is local on the conflict graph for
every admissible positive-mass outside configuration:

```text
P(T accepted | all neighbors rejected) = lambda/(1+lambda);
P(T accepted | some neighbor accepted) = 0.
```

It can choose the empty or nonmaximal set, so it is a regional statistical
specification, not by itself a progress protocol.  `lambda` is supplied.

### Finite-bit retry

For a fixed finite **single-winner** contest of `k` symmetric contenders
drawing one `b`-bit mark from `M=2^b` values, the probability of a unique
greatest mark is

```text
U(k,M) = k/M^k * sum_{s=0}^{M-1} s^(k-1).
```

Ties create an explicit unresolved/retry record.  Conditional on the law
actually supplying a continued iid retry opportunity after every tie,
unresolved probability after `n` attempts is `(1-U)^n`, so resolution is
almost sure and expected attempts equal `1/U`.  The worst-case number of retry
records is unbounded even though every record has bounded capacity.  This is
not a complete strict-order sampler: the one-chunk probability that all marks
are distinct is `(M)_k/M^k`, which the receipt prints separately.

More generally, almost-sure lineage success requires a declared conditional
lower bound or product criterion; it is not implied by deadlock freedom.

## 9. Regional restriction and overlap tests

D36 does not claim Paper 24's undefined all-region architecture.  It tests the
first finite conflict-region cells.

1. **Raw restriction attack.**  On the path `P-Q-R`, restricting a larger K1
   or K3 law to `P-Q` must be compared with running the same law directly on
   the induced edge.  They are expected to differ because external `R` changes
   Q's boundary condition.
2. **Boundary repair.**  Retain an explicit external-blocker/boundary field and
   verify the conditional mixture identity for K3 exactly.
3. **Disjoint product.**  Test full joint distributions, not only local
   marginals, on two disconnected conflicts.  Shared arbitration randomness is
   a deliberate negative control.
4. **Three-way-only hyperedge.**  Verify a triple may be forbidden even when
   every pair is allowed; pairwise conflict data are not generally complete.
5. **Finite-cover feasibility.**  Formulate exact rational joint-extension
   constraints for a three-region cover, including the pairwise-anticorrelated
   binary counterexample.  Passing cells remain finite examples, not an
   all-cover theorem.

The intended nested law has the schematic form already isolated by Paper 24:

```text
(r_E,D)_* gamma_E(. | b_E)
  = sum_bD gamma_D(. | b_D) nu_E->D(b_D | b_E).
```

## 10. Liveness vocabulary without clocks

All liveness is about causal extensions or retry succession:

```text
deadlock freedom       every reachable nonterminal finite state has an action;
system progress        a fair maximal extension terminals some proposal;
proposal resolution   a named attempt commits or receives a terminal failure;
lineage success        some descendant rebase/retry commits;
starvation freedom     the lineage is not postponed forever.
```

Weak/strong fairness or probabilistic conditional bounds must be declared.
No computer loop counter is physical time.  No finite-horizon absence of
starvation is promoted to an infinite theorem.

## 11. Quantum and D24 scope

A one-parent transaction actor birth may use D24's exact `B_g` after that birth
alternative is selected.  It may initially carry only initiator-derived
quantum content plus deterministic structural incidence.  Independent content
from other participants must arrive through licensed later records.

The final multi-parent commit is not a D24 birth.  A physical quantum version
needs a D25/D27-admissible variable-support instrument with orthogonal durable
outcome sectors for commit/reject/retry and a declared join map.  A priority
that changes dynamics cannot be free metadata; it must be boundary evidence or
a normalized recorded physical outcome.  D36's first receipt is classical and
structural.  It tests only D24's one-parent **graph shape**; no `B_g`/NSE
operator gate is executed here, and no quantum join is claimed.

## 12. Exact receipt gates

The first executable under `v10/code/` must use exact integers/Fractions and
print at least:

```text
G0  ontology/type and immutable-history checks;
G1  structural identity alpha covariance and nominal-freshness no-go;
G2  P0 circular-deadlock witness and born-ticket isomorphism;
G3  P1 reusable-grant double-commit witness;
G4  atomic-oracle attribution and P2 split-adoption witness;
G5  P3 exclusive-wait split-vote/deadlock witness;
G6  P4 fail-fast attempt safety and termination under fair delivery;
G7  P4 partial-application states and causal closure ancestry;
G8  P5 atomic-oracle comparison and attribution;
G9  T3 safety, maximality, progress and all serializer permutations;
G10 stale evidence rejection and explicit typed loser records;
G11 disjoint commutation and full product factorization;
G12 deterministic automorphism no-go;
G13 exact K1/K2 laws and their separating event;
G14 K3 normalization, DLR conditionals and supplied-lambda separation;
G15 finite-bit tie/retry arithmetic and almost-sure scope;
G16 raw restriction failure plus boundary-mixture repair;
G17 three-way hyperedge and triple-cover consistency counterexample;
G18 reference-presentation equality, with independent actor bisimulation in a
    separately hash-locked companion;
G19 bounded-capacity census, with every nonuniform bound disclosed;
G20 crash/no-fair-delivery blocking counterexample;
G21 nonvacuous gate-census/integrity check, source/stdout/internal hashes;
    two-process replay and committed-receipt equality run externally.
```

## 13. Decision rows

Apply the first earned row:

1. **BIRTH SELECTS ROOT-FREE COORDINATION:** birth plus inherited principles
   uniquely supplies safe/live arbitration, atomic overlap and a completed
   root-free law.
2. **BIRTH-CARRIED REGIONAL COORDINATION / FAMILY:** a finite root-free-in-
   initiator protocol exists using born transaction/grant/seal records, but a
   close boundary, arbitration law, atomic join or parameters remain supplied.
3. **COORDINATION CARRIER / REPRESENTATIONALLY ELIMINABLE:** records make the
   evidence ledger causal and durable, but matched token/dormant protocols have
   the same finite observable law; safety/liveness comes from other primitives.
4. **DEADLOCK-FREE BUT UNSAFE/UNLIVE:** held waits disappear but double commits,
   split votes, livelock or starvation remain.
5. **BIRTH DOES NOT HELP:** every admitted born protocol has the same obstruction
   as the control even after allowed extra principles are matched.
6. **UNDEFINED:** an atomic join, eligibility boundary or observable algebra is
   still too vague to score.

Expected honest result before execution: rows 2 and 3 may both apply at
different meanings.  Birth is likely a useful record-native coordination
carrier, yet finite-horizon computationally eliminable.  The missing physical
structure is expected to sharpen to exclusive version-bound causal promises,
a local apply/ack/closure grammar and a covariant overlap-selection law.  A
single multiwire seal is an alternative regional oracle, not something tickets
derive—not a clock and not a ticket alone.

## 14. Review protocol

After the exact receipt, independent hostile lanes attack:

1. concurrency/safety/liveness and hidden atomicity;
2. probability/covariance/restriction and infinite-liveness scope;
3. record ontology/capacity/D24/NSE and eliminability.

Every blocker/major is frozen before repair.  The synthesis paper is written
only after the D36 result survives focused deltas.  Paper-level hostile review
then runs separately.

## 15. First exploratory receipt and self-audit

The first implementation executes `PASS 22/22` over exact integers/Fractions.
It prints:

```text
held-lock graph                 45 states, 69 edges, 1 circular deadlock;
exclusive-wait triangle        2 split-vote deadlocks / 8 assignments;
fail-fast pair                 1,113 states, 2,984 edges, 8 terminals;
fail-fast triangle             34,637 states, 140,028 edges, 17 terminals;
fail-fast disjoint             289 states, 816 edges, 1 terminal;
fail-fast partial overlap      1,517 states, 5,162 edges, 2 terminals;
closed priority serializers    8,976 exact checks;
K1 path law                    {Q}:1/3, {P,R}:2/3;
K2 path law                    {Q}:1/2, {P,R}:1/2;
finite-bit unique rows         1/2, 3/4, 3/8, 21/32;
raw K1 restriction             2/3 vs direct 1/2;
hard-core boundary repair      exact;
```

Provisional source/stdout/science hashes are

```text
407a11c13505c79d2db10d12438c2d9a212e06bd349ee5a63fab8ff16bd57673
c4483a3151f9e8352c37915747b5e4fb09bd24150c3cf637c614a02f025b8d51
0a81851fb746811d745856a07a68308ec94577ebfa1e2b1640ae122f0cb86a94.
```

This is **not** the review candidate.  The coordinator's pre-hostile self-audit
freezes four repairs:

1. G10's terminal typing expression contains a vacuous empty-state quantifier;
   replace it with explicit response/application/ack checks on every terminal.
2. The born/token result currently duplicates core state indices by a
   presentation tag; rebuild the two labeled transition graphs and exhibit the
   explicit projection/bisimulation on every node and edge.
3. Add the three-participant cyclic local-order witness
   `R<P<Q<R`; independent participant queues do not define an acyclic global
   serialization.
4. Reconcile the prose's “21 gates” with labels G0--G21 (`22` gates), and make
   clear that fail-fast terminal-state multiplicities are state counts, not a
   probability distribution over service orders.

The first source and receipt remain as an auditable provisional checkpoint.
No scientific noun is promoted until a strengthened rerun and hostile review.

## 16. Strengthened exact review candidate

All four self-audit repairs were made without changing the frozen fixtures,
protocol or 22 verdict gates.  Two clean reruns are byte-identical and give:

```text
all fail-fast terminal states explicitly typed       28 / 28;
fail-fast transition graphs directed acyclic         4 / 4;
cyclic local order R<P<Q<R global serializations     0;
born/token projected nodes                           1,113 / 1,113;
born/token projected edges                           2,984 / 2,984;
born/token terminal observable classes               3 / 3;
verdict                                               PASS 22/22.
```

The fail-fast terminal multiplicities (`8,17,1,2`) count distinct canonical
terminal *states*.  No probability measure over asynchronous delivery orders
has been supplied, so those counts are not probabilities.  The actual
probability results remain K1--K3 and the finite-bit rows, all computed with
exact `Fraction` arithmetic.

The born/token statement is also deliberately narrow.  The checker constructs
two labeled transition graphs: one whose transaction carriers are immutable
structural proposal records, and one whose carriers are activated pre-existing
bounded slots.  Erasing only that carrier presentation maps every node and
every edge in both graphs to the same coordination graph, and preserves the
three terminal commit-observable classes.  Thus record birth adds persistence,
addressability and causal evidence, but it has not yet added finite-horizon
coordination power.  This is a matched-control bisimulation, not a theorem that
birth is eliminable in an unbounded universe.

Hashes are:

```text
source  f1b2c5010812e08f560876a570fc06693d59633de03421b0fed5ff5e5c3daed0
stdout  0bf500873acdc71bb68c5b7d9012b89310941c879f59b013105db1f0e00fccea
science 872a38acd65f7ebcb122a50f6713da53ae119764c7449387b1b55efe27acf04b
```

The unchanged candidate verdict is:

> **CLOCK-FREE LOCAL TRANSACTION COORDINATION / SAFE, NONSELECTING,
> FAILURE-FREE.**

It means the local record grammar can represent safe completed attempts and
exactly exposes partial application, but only under failure-free fair delivery.
It does not select arbitration, define the closed eligibility boundary, prove
starvation freedom, derive the opportunity/birth law, or generate the quantum
instrument.  Independent hostile review now attacks those exact boundaries.

## 17. Round-one hostile opening ledger

Three independent lanes reproduced the strengthened receipt byte-for-byte
under six fresh hash seeds.  They agree that the fail-fast safety core and all
printed arithmetic survive, but reject promotion of the record-native and
actor-local headline.  The frozen count is:

```text
blockers 0; majors 7; minors 6; nits 2.
```

The seven major openings are:

1. **Decorated-identity control.**  G18 wraps one already-built pair graph in
   constant BORN/TOKEN labels and erases them.  It needs independent pre-
   proposal state types, birth/activation transitions, forward/backward
   matching and all four fixtures plus a continuation horizon.
2. **No executed immutable record history.**  `FFState` is a global mutable
   summary.  The static upper-seal dictionary is not generated by P4, so
   persistence, rejection/release ancestry and T2 closure are not yet checked.
3. **Forged remote-tip knowledge.**  `tau` contains exact remote current tips
   although one-parent `T0` has no causal path from them.  Stable participant
   capabilities belong in `T0`; exact versions must arrive in authenticated
   grants, with logical transaction and version-bound attempt IDs separated.
4. **Capacity mismatch at arity three.**  The two-party closure DAG has parent
   arity three, but naively extending it to a three-party transaction requires
   arity four.  A bounded merge tree or a raised honest bound is required.
5. **No actor-local refinement.**  The positive executable has one global
   response matrix/pending multiset and cross-owner reads.  Bare triples accept
   forged responses.  Separate owned mailboxes, authenticated typed envelopes,
   rejection-before-mutation attacks and a projection to the reference graph
   are required.
6. **Physical K1 mark not factorized.**  The four-proposal global order has 24
   marked atoms; the product of two component orders has four.  The accepted-
   set pushforward factors only after discarding six cross-component shuffles.
   Arbitration must be component-local or those shuffles explicitly gauged.
7. **Capacity census omits an auxiliary fixture.**  The registered maximum is
   three proposals while the factorization control actually uses four.

The six minor repairs require: a stronger structural-freshness/collision
battery; an explicit statement that D24 compatibility is only one-parent
graph shape until `B_g`/NSE is supplied; fixed-batch/version-zero scope or a
two-epoch stale/rebase continuation; the verdict qualifier “closed-attempt
reservation-safe, failure-free”; unique-greatest retry separated from complete
strict-order sampling; and disclosure of 20 positive-mass DLR checks plus four
zero-mass skips.  The nits correct P6/T3 attribution and the stale status/gate
provenance labels.

The coordinator freezes two additional receipt gaps before repair: G2 prints
ticket-graph isomorphism without constructing it, and G21 is assigned `True`
instead of executing the promised replay/integrity check.  Both must become
nonvacuous exact gates.

No opening changes the central negative/positive core:

```text
held waiting can deadlock;
reusable grants can double commit;
exclusive waiting can split-deadlock;
exclusive fail-fast reservation closes every supplied finite attempt under
failure-free complete delivery in the reference semantics;
arbitration remains unselected.
```

Repairs proceed only from this ledger.  Paper 25 remains unwritten.

## 18. Reference-semantics repair checkpoint

The numerical/reference executable is repaired first and deliberately
downgraded while the actor companion remains open.  It now prints:

```text
PASS 22/22
CLOCK-FREE FINITE REFERENCE TRANSITION SYSTEM /
CLOSED-ATTEMPT RESERVATION-SAFE
```

This checkpoint closes the reference-side findings:

- G2 constructs and projects the complete 45-state/69-edge inert-ticket graph;
- `tau` contains stable carried capabilities, while exact remote tips appear
  only in the later version-bound attempt identity;
- the arity-three success closure uses a 25-node bounded merge chain with all
  24 prior nodes below `CloseT` and maximum parent arity two;
- every named and auxiliary fixture is inventoried, honestly raising the
  audited proposal maximum from three to four;
- K1's physical mark is a product of connected-component orders; the old
  four-name presentation has 24 shuffles quotienting to four physical atoms,
  six shuffles each;
- K3 prints 20 positive-mass DLR checks and four zero-mass exclusions;
- unique-greatest single-winner retry and complete strict-order probability
  are separate exact rows; and
- G21 checks the entire preceding gate census instead of assigning `True`.

Two fresh runs are byte-identical.  The repaired reference identifiers are:

```text
source  dad183c2e303b0315fa7f452ab1c197569d6983332696421d70f04ba5b3d0743
stdout  3478d1447ee54a33599d9d1e3b00b63cfa323ed7df1a44e3915b13da62545093
science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314
```

G18 is no longer narrated as an earned bisimulation.  It is labeled a
definition-level **reference-presentation control**, and explicitly prints
`independent_actor_bisimulation=0`.  The actor/mailbox/append-only-history
companion must now earn the stronger noun on all four fixtures plus a
continuation horizon before D36 can return to hostile review.

## 19. Authenticated actor-record repair result

The companion `code/d36b_actor_record_refinement_exact.py` independently
rebuilds P4 from participant actors and transaction actors.  Each actor owns
its local version/promise or response/decision/ack slots, authenticated
capabilities, used-envelope set and mailbox.  The simulator's only global
operation is choosing one addressed nonempty mailbox to service; no handler
reads another actor's live state.  This is logical actor locality, not a claim
that Python launched independent operating-system processes.

Every prepare, grant/reject, decision and acknowledgement envelope carries a
typed sender, recipient, transaction/body digest, protected base, issued
capability and signed predecessor record.  All eight hostile cases reject
before durable mutation:

```text
forged response; wrong-base grant; forged decision; forged ack;
prepare replay; duplicate application; unissued capability;
disconnected lookalike.                                  8 / 8
```

The actor graph is explicitly quotiented by the authenticated envelope header,
not by complete record bytes.  This prevents causal-record presentation from
being mistaken for the coordination state.  The stronger record checks run in
parallel:

- all `297,980` BORN+TOKEN actor edges emit a valid typed record delta with
  parent arity at most two;
- one complete immutable ledger is replayed for every one of the `56` terminal
  coordination-quotient states;
- every parent exists before use, all earlier record bytes remain identical,
  all grant/reject/apply/release records survive, and every `Close(T)` contains
  its transaction records in its ancestry;
- each participant and transaction owner's records form one linear wire;
- the largest terminal ledger has 39 records; and
- four exact two-service diamonds show that swapping genuinely incomparable
  disjoint actor services changes neither actor world nor full ledger.  This
  does not gauge alternative services at one actor.

The edgewise forgetful projection is exact for both carrier presentations:

```text
fixture    reference states/edges/terminals    BORN             TOKEN
pair              1,113 /   2,984 /  8         identical         identical
triangle         34,637 / 140,028 / 17         identical         identical
disjoint            289 /     816 /  1         identical         identical
partial overlap    1,517 /   5,162 /  2         identical         identical
```

BORN and TOKEN have separate pre-proposal types and separate opening
transitions.  The coordination projection agrees in every fixture, but the
full support-record observable deliberately disagrees.  Thus the earned result
is:

> **At this supplied finite horizon, fresh support is not what supplies P4's
> coordination power.  Birth and dormant activation implement the same
> coordination quotient, while remaining ontologically distinguishable record
> processes.**

The requested continuation is also executed in both modes.  Starting from
participant version one, an old-base attempt rejects through the normal actor
path; a version-one rebase then commits and advances both participants to
version two.  A bounded two-parent `REBASE_LINK` retains the old closure and
new carrier, while logical lineage stays fixed and attempt identity changes.

The companion passes `12/12`.  Two fresh hash-seed runs are byte-identical:

```text
source  5813304446d267dc3d08f520f4db991bf6bdb94ae45b1f96a5e0cc2a094996ba
stdout  8e2e9b9ad6de8ad7ebef4554c2eef32f20b1ffead33a7af6f89f6251e0d8b41d
science ab275cc69ef529bceba96c7cb484232a5c4b661e9cd1a902c695067bd04193a4
```

The separate two-process replay checker runs the reference and companion under
seeds 17 and 104729, compares all four outputs to committed receipts and passes
`8/8`.  Its source SHA-256 is
`878f0a1daa08db30974bf06e7075a9952faa18d569d74286eea2ed51011f2ec6`.

The repaired candidate verdict is:

> **CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION REFINEMENT /
> FAILURE-FREE CLOSED ATTEMPTS.**

“Safe” remains the longer predicate: no incompatible closed commits consume
one protected base, no admitted application uses a stale/unpromised base, and
every fully serviced failure-free attempt closes commit or abort.  It is not
linearizable multiwire visibility, crash recovery, starvation freedom or an
unbounded online theorem.  Ideal authentication, capabilities, fixed attempt
bodies and mailbox service are supplied.  The birth opportunity law,
arbitration selector, crash/failure detector, root-free infinite completion,
`B_g`/NSE quantum realization and spacetime consequences remain open.

## 20. Round-two hostile opening ledger

Three independent closing lanes froze the candidate at commit `63314a2` and
reproduced the reference, actor and external-replay receipts.  The
probability/capacity lane closes with no finding.  The ancestry lane returns
`0B/2M/2m/0n`; the locality lane returns `1B/1M/1m/1n`.  Before deduplication
the round therefore records:

```text
blockers 1; majors 3; minors 3; nits 1.
```

Two failures are load-bearing and overlap across the hostile lanes.

1. **Exact evidence and attempt identity are not authenticated.**  The
   signature binds the reduced coordination header, not the exact carried
   record ID, parents or omitted payload field.  A same-header record with a
   different ancestry remains authentic and mutates the receiver.  Moreover,
   the body/capability/authorization tuple omits the carrier attempt: a valid
   same-base epoch-zero decision is accepted by an epoch-one participant.
   The reduced header may remain a graph-quotient key, but the physical
   signature must commit the complete record and a structural attempt ID.
2. **The claimed continuation is two fresh histories joined afterward.**
   `continuation_gate()` initializes the stale and rebased attempts
   independently, unions their ledgers and appends `REBASE_LINK`.  In both
   BORN and TOKEN modes the combined object fails `validate_owned_wires`;
   participant seeds branch, the transaction owner has multiple roots and
   same-owner parents, and the old close is not below the new close.  The next
   attempt must be opened from the actual terminal actors and ledger, preserve
   used-envelope/capability state and old bytes, and pass the complete ledger
   validators.

The surviving scope repairs are also frozen rather than inflated.  The 56
terminal ledgers and 297,980 edge checks are one causal lift per coordination-
quotient terminal/edge, not a census of every full record history.  Opposite
same-transaction response orders can share the declared `ActorWorld` quotient
while producing different valid ledgers and decision IDs.  Capabilities,
fixed attempt bodies, finite structural slots and cryptographic collision
resistance remain supplied finite-fixture assumptions, not a root-free
freshness theorem.  Finally, G20 is still a static failure-scope assertion,
not an executed crash trace.

No finding changes the probability-free reference core or the honest
single-attempt projection.  It does prevent the candidate actor-record verdict
and Paper 25.  Repairs begin only from this frozen ledger: exact evidence and
attempt authentication first, then one genuinely persistent stale/rebase
history, then a new hostile closing delta.

## 21. Exact-evidence and persistent-continuation repair

The round-two blocker and major are now repaired in the executables, but not
yet promoted past candidate strength.

The actor companion separates two algebras that the rejected version had
conflated.  `public_fields()` remains the reduced finite-state coordination
label.  The physical signature instead commits:

```text
sender and recipient;
transaction and participant address;
body and protected base;
stable route capability;
carrier-derived structural attempt ID;
participant response-record binding where applicable;
exact carried record ID, which commits complete payload and parents.
```

The carrier-derived attempt ID is stored in the participant authorization,
active promise, every envelope and every post-carrier record.  Each
participant retains the exact response record for its attempt; a decision is
accepted only when its attempt and participant-response binding match.  The
coordination graph may still quotient those exact bytes, but authentication no
longer does.

The hostile battery expands from eight to thirteen cases.  In addition to the
original forged, stale, replay and capability attacks, it now changes a
record's parents under an unchanged signature, changes the payload field that
the quotient deliberately omits, splices a decision onto a nonexistent
parent, and replays same-body/same-base decisions across two different carrier
attempts in both BORN and TOKEN modes.  All `13/13` reject before actor
mutation or output-record creation.

The stale/rebase exhibit is rebuilt as one world and one ledger per carrier
mode.  A stale version-zero attempt begins on version-one participant actors,
rejects and closes.  The version-one attempt is then opened on those exact
terminal actors: participant heads, used-envelope sets, capability state and
old record bytes persist.  The rebased attempt uses a distinct transaction
owner and a new carrier descending from the old close.  In TOKEN mode its
carrier additionally activates a dormant slot that existed before the first
attempt.  Both complete ledgers pass parent-before-use, immutable-prefix,
owned-wire and closure-ancestry validation:

```text
old-base abort                         2 / 2;
rebased commit                         2 / 2;
unchanged old prefix                   2 / 2;
complete combined ledger valid         2 / 2;
old close below new close              2 / 2;
old envelope rejected after rebase     2 / 2;
final participant version              2;
combined records across both modes    50.
```

The reference checker now labels G20 honestly as a static failure-scope
assertion.  The actor receipt likewise renames its `297,980` checks as
**representative coordination-quotient edges**.  The 56 complete ledgers
remain one path lift per terminal quotient state, not all full causal
histories.  Same-transaction service-order histories are retained as
potentially distinct physical histories; no new gauge claim is made.

Fresh deterministic identifiers are:

```text
reference source  2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683
reference stdout  868c57325101f683c8cea58be1226a04ede361212c76e93471529e993e515c17
reference science a373d10d90a6f3063aff02f06dcd92e62a6225981fef291272fbf38cd1e71314

actor source      748128631ff32268a9d0f5c8f74306189a9d371752569e06f87f2a0c2ca0214a
actor stdout      8ee46d53a1f392222b4e60e10ead369a831661f272120e090a2166985edfcf43
actor science     c9fb8f5e75fb635f6dade6c2e176959d96a2451465d2813d4afe72ceb757f19d

replay source     3cbf013bbb1766fbc8e304be33ebcec3d3783f8f5fedc6fc6b7f3a62e7c8ef95
replay stdout     c69b25e39df2f7ac478643ec2a9716c02ff924c02636fcce6211d0c4d1dee94e
```

The reference returns `PASS 22/22`, the actor companion `PASS 12/12`, and the
external checker `PASS 8/8` under hash seeds 17 and 104729.  The surviving
scope is unchanged: this is a supplied finite, failure-free coordination
family.  It does not select birth opportunity, participant discovery,
arbitration, retry fairness, crashes, an unbounded history law, the quantum
join or spacetime geometry.  Independent closing review must now attack only
this delta; Paper 25 remains withheld.

## 22. Round-three hostile opening ledger

The three closing lanes reproduce commit `e80ca6a`.  Probability/capacity and
external replay close at `0B/0M/0m/0n`.  Ancestry returns `0B/1M/1m/0n`, and
locality returns `0B/1M/1m/0n`.  The raw count is therefore
`0B/2M/2m/0n`; after merging the shared opening, it is one major and two
minors.

The reviews close the round-two blocker and continuation defect.  Exact record
substitution now changes the authenticated statement; same-body/base messages
cannot cross carrier attempts; and both 24-record BORN and 26-record TOKEN
histories preserve their old prefixes, linear wires and old-close ancestry.
The representative-quotient wording and static G20 labeling also survive.

The remaining major is earlier in the opening relation.  The rebase helper
directly extends every participant's `applications`, `response_records` and
`authorizations` tuples before any participant event, while the only appended
record is the T-owned carrier.  That side installation is operational: remove
only the injected authorization and the same carried prepare rejects.  Supply
an arbitrary attempt string together with a matching side authorization and
it can close.  Therefore carrier derivation is presently a constructor
convention, not a participant-checked local invariant.

The repair is forced: the already carried stable route capability and exact
carrier must let each participant validate the attempt label, allocate its
bounded slots and register the attempt **inside its own prepare-handling
event**.  The opening helper may create the T carrier and route envelopes, but
it may not change participant predictive fields.  The attempt label must be
locally recomputable from the exact carrier and the body the participant sees.

Two narrower ceilings are frozen.  First, `service_world` is a handler-plus-
transport macro: one handler changes durable addressed state, then the driver
inserts its outgoing envelopes into recipient mailboxes.  Either split network
delivery into its own transitions or name this granularity honestly.  Second,
the receiver checks the exact signed response record but not an independently
carried proof that its other parent belongs to the claimed remote owner wire;
the present theorem must stay within honest record-generating actors unless a
bounded local ancestry proof is added.

No Paper 25 is permitted.  The participant-local registration gate and an
honest transport-macro scope repair must execute, then receive another focused
closing delta.
