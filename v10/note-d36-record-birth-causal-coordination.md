# D36 — record birth as causal coordination

**Status:** PRE-RECEIPT PROTOCOL PIN.
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
       ordered capability roles, referenced participant base tips).
```

Relabeling records relabels `tau`; printable spelling has no priority.  This is
a finite exhibit, not a root-free global freshness theorem.  A transaction may
name only participant records reached through existing capabilities.  Naming a
disconnected participant would already assume the missing bridge/join law.

## 4. Capacity pin

The exact campaign uses bounded cells:

```text
transaction arity                    at most 3;
participants in a fixture            at most 4;
proposals in one closed batch         at most 3;
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

This is the positive strictly actor-local protocol at the first finite scope:

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

### P6 — closed batch plus a common strict arbitration order

A supplied finite boundary seal declares the contender batch closed.  Every
proposal carries a common, physically readable strict priority mark.  Process
proposals from greatest to least mark, accepting a proposal iff its complete
participant set remains unused.  This returns a maximal independent set and
provides a finite arbitration **specification** for P4 attempts.

The batch-close record solves the unknown-future-contender problem and the
common strict mark supplies symmetry breaking.  Neither comes from freshness.
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

### T1 — safe fail-fast causal-attempt theorem

For a fixed finite participant set, authenticated reliable messages, local
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

On every finite closed conflict graph with a strict common proposal order, the
greedy accepted set is feasible, maximal and nonempty when proposals exist.
The result depends only on the marked graph, not the machine serializer.
Disjoint components factor because their relative internal orders determine
their outputs independently.  Each selected attempt may then be realized by
P4.

### T4 — finite-horizon eliminability test

Compare two protocols with identical validation, priority and atomic-seal
semantics:

```text
BORN       create a fresh transaction actor/record;
TOKEN      activate a pre-supplied dormant transaction slot or carry tau in
           immutable participant-local proposal/grant records.
```

After forgetting inactive-slot and born/token presentation fields, their full
finite state graphs and declared participant/commit observables should be
bisimilar.  Passing proves birth is representational at this bounded scope,
not ontologically absent at all scales.  A failure must print the first support
observable that distinguishes them.

## 8. Time-free probabilistic arbitration

Probability is placed on arbitration marks or feasible commit sets, not on a
race in seconds.

### K1 — uniform random strict order plus greedy acceptance

On a finite closed batch, sample every strict proposal order with probability
`1/n!`, then apply T1.  The order is a physical arbitration mark, not machine
service order.  The induced kernel is automorphism-covariant and factors on
disconnected conflict components because relative orders on disjoint subsets
are independent.

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
components.  Its single-site conditional is local on the conflict graph:

```text
P(T accepted | all neighbors rejected) = lambda/(1+lambda);
P(T accepted | some neighbor accepted) = 0.
```

It can choose the empty or nonmaximal set, so it is a regional statistical
specification, not by itself a progress protocol.  `lambda` is supplied.

### Finite-bit retry

For `k` symmetric contenders drawing one `b`-bit mark from `M=2^b` values, the
probability of a unique greatest mark is

```text
U(k,M) = k/M^k * sum_{s=0}^{M-1} s^(k-1).
```

Ties create an explicit unresolved/retry record.  With independent retries,
unresolved probability after `n` attempts is `(1-U)^n`, so resolution is
almost sure and expected attempts equal `1/U`.  The worst-case number of retry
records is unbounded even though every record has bounded capacity.

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
structural.  It tests D24 compatibility but does not claim the quantum join.

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
G18 born/token finite-horizon bisimulation;
G19 bounded-capacity census, with every nonuniform bound disclosed;
G20 crash/no-fair-delivery blocking counterexample;
G21 deterministic replay, source/stdout/internal hashes.
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
