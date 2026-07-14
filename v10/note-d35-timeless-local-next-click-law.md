# D35 — timeless local next-click law

**Status:** TERMINAL ACCEPTED at the rooted nested-call scope after three clean
independent typed-identity closing deltas.
**Date:** 2026-07-14.

**Parent:** terminal D34f / Paper 23 at commit `de51b4e`.

## 1. Question

Can SHARD define the probability law of A's next record update without a
global time, a numerical proper time on each record, or a supplied Poisson
clock, while retaining:

- a strong local causal principle for which evidence may enter A's next
  record;
- the already constructed D24 birth-content kernel and D25/D27 reception
  constraints;
- construction-order gauge for incomparable events;
- projectively consistent finite-stem probabilities;
- genuine record birth and variable actor support; and
- an executable actor-local sampler whose physical law is independent of its
  machine serialization?

The target is not another D34b clock model.  It is a time-free marked-history
law or a proof that the inherited structures do not select one.

## 2. Corpus boundary

Before derivation, a deterministic census must cover every primary paper and
note in V1--V10 existing before D35.  Reviews are routed through their parent
artifacts and may be read where they changed a terminal claim.  The census
must hash each file and classify at least:

```text
causal order and locality;
next-click and record-wire semantics;
birth/support/opportunity kernels;
diamonds, collars and holonomy;
whole-history/path measures and actions;
construction-order gauge/projectivity/profinite stems;
proper/local/global clock claims;
Markov and non-Markov predictive-state claims;
simulation/generative algorithms;
scope guards and retractions.
```

The accepted D13 522-file action census is inherited as an independent
antecedent control, not substituted for the fresh D35 causal/birth/time audit.

## 3. Primitive time-free object

A finite marked record stem is

```text
H = (events, directed ancestry, record wires, active tips,
     typed marks, parentage, sealed evidence references).
```

There is no numerical event time.  The ancestry relation is acyclic and
locally finite.  Every record wire is linearly ordered by its own successive
updates; unrelated events may remain incomparable.

A completed history is a compatible infinite or terminal extension of finite
stems.  A candidate primitive law is a normalized measure `mu` on completed
marked histories, specified by consistent finite cylinder probabilities.
Sequential growth is a sampling representation only.  Its integer step and
linear extension are construction gauge.

## 4. Strong causal acquisition principle

Let A1 be a current A-wire event and let A2(H) be the next A-wire successor in
a completed history H.  Define

```text
NewPast_A(A1,A2) = Anc(A2) minus Anc(A1).
```

The structural principle under test is:

> **CAP.** Evidence record e is newly acquired by A at A2 if and only if e is
> in `NewPast_A(A1,A2)`, connected to A2 by a finite chain of locally licensed
> record transfers.  Construction order, nominal adjacency and correlation
> through a common older cause do not by themselves constitute acquisition.

The realized relation is binary.  Let `[H0]` be the cylinder of completions of
the present finite history and assume `mu([H0]) > 0`.  Assign `A2 = bottom` to
completions in which A has no strict successor and declare reach false there.
The pre-click probability is the cylinder ratio

```text
P(e reaches A2 | H0)
 = mu({H in [H0]: A2 != bottom and
                   e in NewPast_A(A1,A2(H)) by a licensed path})
   / mu([H0]).
```

No elapsed time occurs.  “Before the next A click” is the local stopping
condition that A2 is A1's first wire successor.

An operational influence strengthening must be typed separately: when an
intervention family exists, changing e's locally allowed content must change
the A2 law.  CAP ancestry alone may carry correlation and is not silently
promoted to interventionist causation.

## 5. Existing birth result and missing layer

D24 is not reopened as absent.  Its one-parent tree birth family supplies:

```text
fresh child initialized in |0>;
controlled-Ry parent/child coupling g_e;
isometric/distinguishability-preserving closure;
collar locality and exact ledger balance;
construction-order gauge on rooted trees;
click-identifiability of tree and interior couplings.
```

Its own scope guard leaves free which collar attaches next and `g_e`.  D1
shows that no-silent centers do not select support or firing probability; D2
shows that diamond amalgamation composes a supplied interface but does not
create the first carrier; D28 names the opportunity kernel.

Accordingly distinguish:

```text
q(o | H)          opportunity/extension selection on a finite stem;
B_o(dr | H)       D24-type conditional newborn record-content kernel.
```

The time-free law must combine them without pretending that B already selects
q.  Paper 19's completeness remains at its declared experimental interface,
not a unique cosmological history measure.

## 6. Mathematical obligations

Any positive result must establish:

### O1 — legal grammar and local finiteness

Continuation, one-parent birth, interaction and any admitted join have typed
parents and finite local ancestry.  Every finite causal interval is finite.
The root/seed rule is explicit.

### O2 — cylinder normalization and projectivity

Finite stem probabilities are nonnegative, normalized and compatible under
restriction.  If amplitudes rather than probabilities are used, strong
positivity and the probability extraction are separately proved.

### O3 — construction-order gauge

For independent extensions x,y,

```text
p(x | H) p(y | Hx) = p(y | H) p(x | Hy),
```

or the equivalent cylinder identity.  Two linear extensions of one marked
causal history have one physical weight.

### O4 — strong locality

An event's extension weight and content kernel consult only its declared
causal collar plus inherited sufficient marks.  Any normalization depending
on an entire spacelike antichain is disclosed as global and cannot earn the
local row.

### O5 — CAP next-A law

The next A-wire successor and its complete ancestry are well typed on the
completed-history cylinders.  CAP acquisition probabilities are exactly
recoverable and unaffected by disjoint components.

### O6 — D24/D25/D27 compatibility

Birth uses the admitted D24 isometric family at the frozen tree scope;
reception obeys the distinguishability-isometry/NSE ceiling.  Any selector of
opportunity or `g_e` is proved, clearly posited, or returned as a family.

### O7 — real simulation

One self-contained implementation under `v10/code/` must provide:

1. an exact finite-stem enumerator;
2. at least two incompatible machine schedulers/linear-extension policies;
3. an actor/tip-local message implementation rather than only a global-state
   transition table;
4. exact agreement of gauge-quotiented history and next-A distributions;
5. live birth, interaction, ancestry transfer and A stopping;
6. deterministic replay and independent hash-seed equality; and
7. explicit rejection of malformed nonlocal or ancestry-forging messages.

A central priority queue may be an implementation aid only if changing it
does not change the physical measure.  No computer step is called time.

### O8 — infinite ceiling

The finite law must identify what is proved about completed histories.  A
finite discrete inverse system is not identified with the v9 stem spectrum
without the construction-order quotient and bonding maps.  Existence,
uniqueness and continuity are separately scored.

## 7. Exact receipt requirements

Discrete probabilities and amplitudes use exact rational/algebraic arithmetic
where available.  Decimal evaluations use at least 100-digit working
precision.  The receipt must print:

```text
corpus file count and stream hash;
primary-artifact category counts;
finite-stem normalization/projectivity checks;
independent-extension covariance checks;
disconnected-component invariance;
birth/reception compatibility checks;
next-A outcome and ancestry distributions;
scheduler and actor-message equivalence counts;
malformed-message rejection counts;
finite/infinite/profinite ceiling;
source, stdout and internal hashes.
```

Finite enumeration is a regression/counterexample search.  Any all-size claim
requires a separate proof.

## 8. Decision rows

Apply the first supported row.

1. **TIMELESS LOCAL NEXT-CLICK LAW / SELECTED:** O1--O8 hold and inherited
   principles uniquely select the extension/opportunity and D24 parameter
   data at the declared scope.
2. **TIMELESS LOCAL NEXT-CLICK FAMILY / EXECUTABLE:** a covariant projective
   actor-local family exists and is executable, but opportunity weights,
   couplings or root data remain extra physics.
3. **TIMELESS MEASURE / NONLOCAL NORMALIZATION:** a projective history measure
   exists but exact next-click probabilities require spacelike-global state.
4. **FINITE TRACE LAW ONLY:** finite scheduler-covariant stems exist, but no
   completed-history measure or consistent projective family is proved.
5. **NO TIME-FREE LIFT:** D24/reception/locality constraints are inconsistent
   with every registered time-free extension family.
6. **REFUSAL/UNDEFINED:** a required grammar, opportunity law, root, instrument
   or completed-history object remains absent.

No row may claim physical proper time, Lorentzian distance, cone roundness,
dimension, G, the actual universe law or a v9 posterior factorization.

## 9. Review protocol

After the corpus audit and frozen candidate are executable, three independent
hostile streams must attack:

1. probability/projectivity/profinite completion;
2. causal locality/construction gauge/actor simulation; and
3. D24 birth/reception/quantum and ontology scope.

Every major opening is frozen before repair.  A synthesis paper is written
only after the D35 theorem ceiling survives exact deltas.

## 10. Corpus-audit result (frozen before the candidate executable)

The deterministic antecedent inventory is
`code/d35_corpus_causal_inventory.py` with receipt
`data/d35_corpus_causal_inventory.out`.  It content-hashes all 441 primary
paper/note artifacts in V1--V10 existing before D35; 427 hit at least one
registered causal/birth/time category.  The frozen corpus stream hash is

```text
b0e4c7e0be1c8587b5f3b35e36a834fa8f485cf4bd7cfbb61331017bcd1541b7
```

The fresh audit is routed through the accepted D13 522-file action ledger and
the later terminal supersessions.  The load-bearing inheritance is:

| corpus layer | retained result | restriction carried into D35 |
|---|---|---|
| V1--V5 | finite supplied kernels, record thermodynamics and non-Markov whole-history admissibility | no selected variable-support extension law |
| V6 | sealed holonomy coordinates can identify a supplied positive law | coordinates do not select support or weights |
| V7 | evidence survival, projective cylinders, history dependence, diamonds and boundary shadows | early universal/forced click-law language is superseded where placement, content increment or finite-window extrapolation remained free |
| V8 | record-native configurations and candidate growth grammars | placement/root/branching and interaction weights remained model data |
| V9 | stem spectrum, construction-order quotient and an exact recurrent marked-support template | support hypergraph, shared allocation, transfer, root and bridge sectors remained free; V9 geometry is closed |
| V10 D1--D23 | rulebook characterization, nonselection, finite regional sewing, whole-history sufficiency, D24 birth, D25/D27 reception, D28 opportunity and D31 covariance restrictions | a supplied history functional answers conditionals but does not construct the missing local opportunity law |
| V10 D33--D34f | finite typed-DAG actor/quantum compatibility and exact predictive-boundary theorems for chosen D34b | the timed D34b rates are supplied; exact full-ancestry prediction can require the whole component because records never seal/attenuate |

Five distinctions are therefore non-negotiable:

1. causal ancestry is not construction order;
2. a local generator may induce a globally correlated history law without a
   central updater;
3. D24 newborn content is not the opportunity selector;
4. a record projection may be non-Markov although a larger history state is
   Markov by construction; and
5. profinite completion preserves compatible finite laws but neither selects
   them nor automatically extends an arbitrary quantum functional.

The inventory is a completeness/forgetting control, not evidence that a
keyword classifier semantically proved these conclusions.  The conclusions
come from the cited terminal papers and notes; the per-file hashes make the
antecedent boundary reproducible.

## 11. Candidate architecture: locally completed causal call diamonds

This section freezes the first candidate before its executable exists.

### 11.1 Record component and ownership scope

The positive construction begins on a finite rooted actor tree.  Every actor
owns a current wire tip, finite typed child ports and a finite-dimensional
carrier.  The root is boundary data.  Parentage is physical ownership, not a
metric direction.  The first construction deliberately excludes cycles,
peer joins and initially disconnected-component joins; those are extension
fronts, not silently simulated by global lookup.

For an actor A with current tip A1, a **causal call diamond** is generated by a
locally carried query rooted at A1.  A queried actor v makes one normalized
local choice:

```text
idle:    seal one v event and return it;
birth:   seal one D24 parent/new-child event and return it;
visit:   query one existing child, then seal a joint return event;
fork:    query two distinct existing children, then seal one joint return event.
```

Unavailable `visit` or `fork` mass is assigned to `idle`, not normalized over
the universe.  Child selection is uniform over v's own eligible typed ports
in the frozen exhibit.  A later law may replace that local selector but must
remain a declared collar field.

Queries descend only along owned child ports.  Independent child calls may be
processed in either machine order.  A joint return event consumes the querying
actor's held lower tip and the returned child tips; it is created only after
all of its declared inputs exist.  The root return is A2.  Hence A2 is A1's
first A-wire successor even when arbitrarily many causally relevant remote
events occur inside the diamond.

### 11.2 Strong causal-local principle

The candidate strengthens CAP to the **Local Diamond Acquisition Principle
(LDAP)**:

> A2 may acquire only immutable records already present on an owned input
> collar of its completed call diamond or created by a finite chain of
> licensed query/return/birth cells inside that diamond.  Every acquired
> record has a directed carried path into A2, and every record with such a
> path appears in A2's ancestry.  A disconnected record, an uncarried machine
> ordering or a common cause without a return path cannot enter the A2 law.

The realized acquisition set is still exactly
`Anc(A2) minus Anc(A1)`.  LDAP adds a local constructor of those ancestry
edges.  There is no probability that an already realized message “half
arrived”: reachability is binary.  Probability applies before completion to
which locally normalized call tree and marks are realized.

### 11.3 Time-free probabilities

Let the local action probabilities be exact rationals

```text
q = (q_idle, q_birth, q_visit, q_fork),   sum q = 1.
```

For a finite completed call diamond D,

```text
P(D | H,A1) = product over queried actors v of
              q(action_v) / number of v-local selected port sets.
```

Invalid-action mass folded into idle is included in the idle factor.  No
factor compares v with spacelike opportunities elsewhere.  The sum is one by
recursive local normalization.  Independent subtree factors commute, so all
linear extensions of one call DAG have one weight.

Because the pre-call actor tree is finite, queries move strictly outward and
each actor is queried at most once, every call diamond is finite without a
duration or subcritical-rate assumption.  One call adds at most one child per
queried actor.  Repeating the discrete local kernel along record wires gives
finite prefixes by induction; standard countable product-extension then gives
a classical completed-history measure for the frozen rooted-tree grammar.
This is an order/history theorem, not physical proper time.

### 11.4 Birth and quantum/reception layer

At `birth`, structural opportunity and content remain separately visible:

```text
q_birth                  probability of the local birth action;
B_g                      D24 fresh-|0>, controlled-Ry content map.
```

The exhibit uses rational rotation legs so all carrier calculations are exact.
Every birth is an isometry.  Visit/fork returns use controlled rotations on
the locally touched carriers; disjoint branches commute, and two return gates
sharing only the same control commute.  Every event also receives one fresh
orthogonal bounded-rank durable type flag, as required by D33.  This is a
classical mixture of finite typed quantum instruments, not a claim that the
fundamental support alternatives have already been coherently summed.

D25/D27 permit the broader Busch trace-norm-isometric CP class.  D24 is
therefore an exact admitted and identifiable one-parent birth family, not a
uniqueness theorem over every quantum receiver or every value of g.

### 11.5 Frozen parameter cells and nonselection control

The executable must compare at least these two complete local cells:

```text
Q1 = (3/8, 2/8, 2/8, 1/8),  birth g = 9/25;
Q2 = (4/10,2/10,3/10,1/10), birth g = 16/25.
```

Both use interaction rotation probability `16/25`.  If both satisfy every
structural gate and produce different next-A/birth predictions, inherited
principles do not select a unique law.  This is a mandatory negative control,
not optional parameter exploration.

## 12. Candidate receipt protocol

The no-third-party-dependency executable is frozen as
`code/d35_timeless_causal_actor_exact.py`.  It must use exact `Fraction`
arithmetic for probabilities and rational-amplitude carrier states; decimal
reports use at least 100 digits.  The initial connected specimen is the owned
tree `A->{B,C}, B->{D}` with a persistent seed event DAG in which D's newest
record is not yet in A1's ancestry.  A disconnected marked component is the
locality control.

The gates are:

1. **E1 recursive exact law:** enumerate every completed A1-to-A2 call
   diamond; total probability one; every event typed and ancestrally closed.
2. **E2 actor-message rebuild:** independently enumerate the same law using
   actor mailboxes, query/return messages and waiting continuations.
3. **E3 scheduler gauge:** FIFO, LIFO and canonical pending-message policies
   give identical canonical history, next-A and carrier distributions; fork
   AB/BA quantum evaluations agree exactly.
4. **E4 LDAP:** every acquired record has a licensed carried path; every
   carried input occurs in `Anc(A2) minus Anc(A1)`; a nominally near but
   unqueried branch is absent.
5. **E5 disconnected invariance:** changing a disconnected component changes
   no A distribution or local access trace.
6. **E6 birth/reception:** every newborn is fresh, one-parent and D24-isometric;
   `P(child=1)=g P(parent=1)` at the birth instant; exact norms and the local
   controlled-rotation identities hold.
7. **E7 projectivity:** the first-call cylinder is exactly the marginal of the
   two-call law; local refinement of every open actor choice sums to its parent
   cylinder.
8. **E8 replay and rejection:** independent hash seeds give byte-identical
   receipt output; deterministic actor runs agree across schedulers; forged
   tips, unauthorized edges, duplicate returns and foreign ancestry reject.
9. **E9 nonselection:** Q1 and Q2 both pass but disagree on at least one birth
   and one next-A observable.
10. **E10 ceiling:** the receipt prints rooted-tree, classical-support and
    finite-typed-quantum scopes; cycles, peer joins, disconnected joins,
    coherent graph-sector sums, Lorentzian geometry and a nature-selected law
    remain open.

An exact positive result earns row 2 only if the actor-message implementation
uses no whole-component probability normalization and the completed rooted-tree
extension proof survives hostile review.  A computer work queue is a serializer
of pending incomparable messages, never a physical time coordinate.

## 13. Provisional exact result before hostile review

The candidate executable at commit `674fb46` passes `18/18` under hash seeds
17 and 65537 with byte-identical output.  Candidate hashes are:

```text
source  06c997a195294991293fdedc9edce005a3f8ad1d23bfd8f73a5a08490163fa26
stdout  24a5cdfe35e1a85b25929217def4bede01e57169a14789392e7e5a7947a11656
science 1f7b39ddaea634c1444695e5e536d528be45785e8c9997eba1388ed22cfe8aa6
```

The two independently implemented paths agree exactly:

```text
recursive call-tree enumerator
actor mailboxes + query/return messages + waiting continuations
```

Each has 16 completed branches on the registered specimen.  FIFO, LIFO and
canonical pending-message policies have the same 16-atom canonical history
distribution in Q1 and Q2.  Reverse child evaluation and reverse
shared-control quantum-gate evaluation also agree exactly.  The serializer
therefore changes neither causal history, probability nor carrier state in
the audited domain.

### 13.1 Finite-call theorem

Let `T` be a finite rooted actor tree and let queries move strictly from a
vertex to zero, one or two distinct children.  Then every query terminates
after finitely many cells.

**Proof.** Induct on subtree height.  A leaf can only idle or birth because
unavailable visit/fork mass is folded into idle; both close immediately, and
the newborn is not queried inside the same call.  At a nonleaf, idle/birth
close immediately.  Visit/fork invoke one/two strict child subtrees, which
terminate by induction, after which one local merge closes.  ∎

Every actor is queried at most once in one call, so at most `|T|` events and
`|T|` newborn actors are added.  No rate, duration, compact time interval or
subcriticality assumption is used.

### 13.2 Normalization and construction-gauge theorem

At each queried actor the exact local menu sums to one.  Applying the preceding
height induction, the sum over every completed call tree is therefore one.
Its weight is the product of the local menu and local port-selection factors.
Two incomparable child subtrees have disjoint actors, event identifiers and
carrier targets; swapping their evaluation order permutes scalar factors and
commuting tensor operations only.  Fork return rotations share the control and
have disjoint targets, so the D24 shared-control commutation lemma applies.
Thus every machine linear extension of one call DAG has the same physical
weight and state.

This is stronger than the receipt's finite enumeration within the frozen
rooted-tree grammar.  It is not extended to cycles, overlapping peer calls or
unowned joins, where the independence premise can fail.

### 13.3 Completed classical history measure

After a completed root call, use A2 as the lower tip for the next call.  The
finite-call theorem maps every finite rooted state to a normalized countable
discrete kernel on finite rooted states.  Starting from the supplied root law,
Ionescu--Tulcea therefore gives a probability measure on the infinite sequence
of completed root-call states.  Every finite prefix contains finitely many
actors/events by induction.  Pushing each sequence to its persistent event DAG
gives the corresponding classical history law.

This earns a completed-history measure for this **rooted nested-call grammar**.
It does not prove a measure for arbitrary mutually initiating actor calls,
cycles, joins or coherent superpositions of graph sectors.  The root-wire
index is an intrinsic succession order of A records, not seconds or a global
event counter; nevertheless the rooted ownership architecture is substantive
extra physics and may be too restrictive for nature.

### 13.4 LDAP and the probability of “reaching A”

All transaction events in all 32 registered Q1/Q2 branches occur in
`Anc(A2) minus Anc(A1)`.  The negative control in which A visits only C never
acquires B's newer `BD` record.  Changing a disconnected P--Q component leaves
the A law exactly fixed and produces zero P/Q local reads.

Thus the model resolves the earlier ambiguity:

```text
realized statement: e either is or is not in A2's new causal past;
probabilistic statement: before the diamond is sampled, sum the weights of
                         completed diamonds in which e is in that set.
```

No arrival probability is assigned after a particular history has already
been realized.

### 13.5 Birth result

Every live newborn is created by a fresh one-parent D24 controlled rotation.
Across the 24 enumerated birth branch-cell incidences, exact normalization and

```text
P(child=1 at birth) = g P(parent=1 before birth)
```

hold.  The controlled maps are isometries and the return maps are unitary, so
the executable lies inside the D25/D27 admitted reception class.  Classical
event identities supply fresh immutable bounded-alphabet flags; the code does
not claim a coherent sum over alternative support graphs.

The answer to “the right birth kernel” is consequently two-layered:

1. D24 is a valid exact one-parent **newborn-content** family and is the right
   inherited kernel for this frozen tree exhibit;
2. neither `q_birth`, `g`, the root, nor the omitted bridge/peer sectors are
   selected, and the Busch class is broader than D24.

There is not yet one uniquely derived universal birth kernel.

### 13.6 Exact nonselection

Both Q1 and Q2 pass every positive gate, while

```text
P_Q1(A2 is birth) = 1/4,   P_Q2(A2 is birth) = 1/5;
P_Q1(A2 is visit) = 1/4,   P_Q2(A2 is visit) = 3/10.
```

Their expected transaction-birth counts are `25/64` and `63/200`, and their
expected summed newborn-one masses are `106929/1562500` and
`1080576/9765625`.  The coarse probability that old `BD` reaches A happens to
equal `1/4` in both cells; that collision is printed rather than used to hide
the other discriminators.

The provisional decision is therefore row 2:

```text
TIMELESS LOCAL NEXT-CLICK FAMILY / EXECUTABLE
```

This is not terminal until the three hostile streams decide whether the actor
implementation is genuinely local at its declared scope, the projective/
completion proof is sound, and the D24/quantum wording stays within what the
executable actually represents.

## 14. Hostile round 1 and frozen replacement protocol

**Round-1 verdict:** promotion rejected.  The three independent lanes report:

```text
probability/projectivity       0B / 0M / 1m / 1n
causal locality/actor          1B / 2M / 1m / 0n
birth/quantum/ontology         0B / 2M / 1m / 2n
```

Reports:

- `reviews/d35-round1-probability-projectivity-hostile-review.md`;
- `reviews/d35-round1-causal-locality-actor-hostile-review.md`;
- `reviews/d35-round1-birth-quantum-ontology-hostile-review.md`.

All three reproduce the frozen receipts byte-for-byte under fresh salts.  The
finite rooted recursive kernel, all exact probabilities, finite-call theorem,
strict-tree scheduler theorem, D24 marginal instant and Ionescu--Tulcea
completion argument survive.  Row 2 nevertheless fails at the pinned O7/O6
width because the actor and physical-evidence/flag implementations do not.

### 14.1 Frozen openings

1. **Capability blocker:** an unissued but syntactically local query can mutate
   B before its missing continuation is rejected; a requester-free B query can
   be declared the root result while A remains at A1; an old B tip can be
   accepted as a completed return with no B call.
2. **Not actor-owned:** the alleged mailbox rebuild uses one global `World`,
   pending list and continuation table; actors own neither mailboxes nor
   outstanding calls.
3. **Identifier channel:** a disconnected event named `E0:r` makes the A kernel
   fail by collision.  Local fresh identity is absent.
4. **No physical quotient gate:** scheduler equality retains nominal names and
   construction paths; alpha-relabeling covariance is not tested.
5. **Coarse E7:** the advertised full first cylinder is checked only after a
   16-to-14 next-A projection, although the review independently confirms the
   complete 16-atom/408-refinement equality.
6. **Flag/NSE overclaim:** `Event.flag` is a classical string outside the
   carrier.  No orthogonal output ranges, arbitrary-input completeness or
   Busch trace-isometric mixture are implemented.
7. **Structural not physical LDAP:** nested D events directly cite A1 while
   the A-to-B-to-D query route is ephemeral.  The receipt proves constructed
   ancestry, not a carried evidence channel.
8. **Multi-leg typing:** initiator, ordered target legs, operation/coupling and
   kind-specific arity/ownership are constructor assumptions, not fail-closed
   history fields.
9. **Corpus omission/self-opening:** the antecedent selector's broad
   `"paper24"` exclusion accidentally omits V3, V4, V6 and V7 Paper 24.  Its
   title truncation also creates the review's three trailing spaces.  The
   437-file count is withdrawn pending a corrected rerun.

### 14.2 Replacement architecture (frozen before code)

The replacement is a separate companion executable
`code/d35b_capability_actor_exact.py`; the rejected candidate remains in the
record.  It may import the exact recursive/quantum primitives only after
hash-locking source `06c997a1...3fa26`.  It must implement:

1. **actor ownership:** every logical actor owns its tip, typed port table,
   mailbox, used-capability set and outstanding-call table; the serializer may
   choose only which nonempty mailbox to service;
2. **authenticated capabilities:** every query is a one-use capability signed
   by the shared owned-edge key (the root by its root key), naming component,
   transaction, root, requester/target, port, path, slot, held lower tip,
   payload and parent call; validation occurs before mutation;
3. **return binding:** a return names the issued child capability and a result
   event that records that capability; the parent accepts only the exact open
   actor-owned slot and consumes it once;
4. **root typing:** only the distinguished root actor can issue a top-level
   call/result;
5. **physical route/payload:** every event retains the complete locally
   adjacent capability route, initiator, ordered typed legs, operation,
   coupling and an immutable evidence payload.  Consecutive route hops must be
   owned parent/child edges.  A declared source-bit intervention must reach A2
   through a queried route and fail on an unqueried/disconnected route;
6. **local identities:** event/newborn identities carry an unforgeable supplied
   component namespace plus actor-local structural address; disconnected
   nominal strings cannot collide.  The namespace is root data, not derived;
7. **port covariance:** owned edges carry transported local port identities.
   A nontrivial actor/event alpha-renaming must give the same quotient history
   distribution with no nominal name in the quotient key;
8. **full projectivity:** E7 compares all 16 complete first-call cylinders over
   all 408 second-call refinements, separately printing the 14-atom coarse
   projection and immutable-event/root-wire persistence;
9. **flagged CQ instrument:** every event has one fresh physical orthogonal
   record-factor label including action and typed legs.  Exact operator gates
   must establish idle, D24 birth, visit and fork isometries on arbitrary
   inputs, local `sum q V^dag V=I`, mutually orthogonal flag ranges and durable
   factor persistence.  The earned quantum noun is a classical-output/direct-
   sum Busch mixture with conditional carrier isometries, not coherent
   superposition over graph sectors;
10. **adversarial battery:** the three hostile capability forgeries, negative
    and cross-continuation slots, replay, malformed direct merges, disconnected
    colliding display names, arbitrary remote content and independent root
    namespaces all reject or factor before mutation;
11. **grown execution:** all first-call output states receive a second exact
    actor rebuild under FIFO/LIFO/canonical policies, and a deterministic
    multi-call growth run agrees across serializers; and
12. **current status/hygiene:** correct the stale top status, branch-cell
    wording, corpus selector and truncation whitespace; rerun independent hash
    seeds and both relevant diff checks.

The replacement still does not seek cycles, peers, mutually initiating calls,
disconnected joins or a root-free law.  If the protocol passes, the maximum
noun remains

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

with Q, g, root/ownership, capability/evidence grammar and missing sectors
supplied.  A favorable replacement cannot be called the universe's complete
interactive click law.

## 15. Capability-actor replacement result before delta review

The frozen companion now executes at registered source hash

```text
fa6d69e6d6b85620d19da8e80899dba4a3a5f976fb6e0b3fcfb7b1224a253c4d
```

Hash seeds 17 and 65537 produce byte-identical receipts.  The stdout and
internal-science hashes are:

```text
stdout   8afc279b5ace76a2c7e043dc043d4b450f14536e262d353333d86c08899e304a
science  3d6703f6ef4fcc84588bf8927d32621052733b6652c27225553fa97772ed3679
```

The replacement passes `18/18`.  For each of Q1 and Q2, three serializers
produce the same 16 exact physical atoms with total mass one.  The complete
16-cylinder first-call law is the exact marginal of all 408 second-call
refinements; the separately printed coarse shadow has 7 atoms.  Every one of
the 408 retained-event/root-wire checks passes.

This is now an actor-owned implementation at the declared scope.  Each actor
owns its mailbox, current tip, port table, used capabilities and open calls.
The sampler's only global operation is choosing one nonempty mailbox to
service; FIFO, LIFO and canonical choices have the same quotient law.  Queries
and returns carry authenticated, one-use, call-bound capabilities.  Nine
forgery or malformed-event classes reject before mutation.  A disconnected
component with a colliding display name and arbitrary content does not change
the A law or get read.  Nontrivial actor-name relabeling leaves the
port-addressed physical quotient exactly unchanged.

Every accepted transaction event retains the full adjacent capability route,
typed legs, action, coupling, evidence digest and source payload.  The Q1 and
Q2 receipts each check 44 authenticated route incidences and two unqueried
controls.  Intervening on the declared source payload from 0 to 1 changes A2's
retained payload from 0 to 1; an unqueried or disconnected route does not.
This earns both structural CAP ancestry and a declared classical carried-
payload influence claim.  It does not derive the payload alphabet or promote
all ancestry to interventionist causation.

The quantum layer now uses fresh orthogonal action/leg output flags rather
than metadata strings alone.  Idle, D24 birth, visit and fork pass exact
arbitrary-input isometry gates; the five local alternatives have orthogonal
flag ranges and satisfy `sum q V^dag V = I`.  All 16 complete histories have
distinct persistent flag histories.  The earned description is a classical-
output/direct-sum Busch instrument with conditional carrier isometries.  It is
not a coherent sum over changing graph sectors and does not select D24 over
the wider D25/D27 class.

All 16 first-call output states in each cell receive a second actor-local call
under FIFO and LIFO and match canonical exactly, giving 32 grown scheduler
checks per cell.  Eight-call deterministic replays agree across serializers.
This is a real executable growth sampler for a supplied rooted ownership tree;
the computer service order is construction gauge and no duration, rate,
proper-time variable or global opportunity normalization is present.

The corrected corpus audit now includes the four historical Paper 24 files
wrongly omitted by the first selector.  Its manifest is frozen at pre-D35 git
commit `fc074b9ec4f2c9ecdef28b61c623d89d08e76432`, so later papers cannot enter
the antecedent census.  It reports 441 primary artifacts, 427 category-
relevant artifacts, corpus stream hash `b0e4c7e0...41b7`, source hash
`44568721...0a21` and receipt hash `7f998dea...4182`; independent hash seeds
agree, the truncation whitespace defect is absent, and the sixth gate confirms
that later papers/notes are excluded by the pinned tree.

The result remains deliberately narrower than the generic D35 row-2 label:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

It is not a root-free peer law.  Cycles, simultaneous/mutually initiating
calls, joins of previously disconnected components, coherent support-sector
sums, the capability/ownership ontology, opportunity weights, coupling, v9
stem-spectrum bridge, cones, dimension and nature's law remain open.  Q1 and
Q2 still pass while disagreeing, so inherited SHARD/ISP principles have not
selected the right opportunity or birth-parameter law.  This section is a
candidate terminal result until the independent hostile delta round closes
the exact repair claims.

## 16. Hostile round 2 and frozen closing protocol

**Round-2 verdict:** delta not clean.  The independent lanes report:

```text
probability/projectivity       0B / 1M / 0m / 0n
causal locality/actor          1B / 3M / 1m / 1 scope note
birth/quantum/ontology         0B / 2M / 1m / 0n
```

Reports:

- `reviews/d35-round2-probability-projectivity-delta-review.md`;
- `reviews/d35-round2-causal-locality-actor-delta-review.md`;
- `reviews/d35-round2-birth-quantum-ontology-delta-review.md`.

The probability lane independently confirms all 16 complete cylinders, all
408 second-call refinements, 3,180 old-event equality checks per cell,
root-wire persistence and Ionescu--Tulcea completion on the labeled rooted
state space.  Fresh seeds reproduce both repaired receipts and the corrected
441-file corpus audit.  D24's newborn instant and exact isometry also survive.
The normal generated actor runs remain scheduler invariant.

Terminal promotion is nevertheless rejected.  The following openings are
frozen before any closing code:

1. **Issued-capability blocker.**  A child query reconstructed from the
   model's deterministic public edge-key formula, but absent from the
   requester's open call, is accepted.  Each target must own an exact incoming
   issuance set; knowledge of structural addresses cannot manufacture one.
2. **Event-alpha major.**  `physical_event_id` retains raw seed names.  A
   consistent five-event seed-DAG renaming changes the purported quotient law.
3. **Prevalidation major.**  A genuine query paired with an invalid option
   consumes the capability and writes a transfer before typed-leg rejection.
4. **Flagged-instrument major.**  The printed gate checks unflagged operators
   of incompatible dimensions plus distinct Python labels.  It constructs no
   common input, spectator extensions, support-changing output direct sum,
   flagged injections or cross-range zeros.  Provenance labels are not by
   themselves orthogonal quantum factors.
5. **Remote-evidence major.**  The source intervention is A's own bit copied
   to A2, including idle/birth branches with route `(root,)`.  It does not
   show evidence originating at B/C/D returning only on a queried route.
6. **Shared-state/ordinal major.**  The statement that mailbox selection is
   the only global operation is false: the executable uses a shared exact
   event/carrier collector and an externally supplied transaction ordinal.
   The former may be an honest joint-state audit representation; the latter
   must be derived from root-owned causal succession.  Neither is metric time.
7. **Rejection-state minor.**  Normal service dequeues before validation, so a
   rejected envelope changes volatile mailbox state.  The repair must either
   peek/ack or narrow the unchanged claim explicitly to durable record state.
8. **Scope opening.**  Repeated root calls condition on A initiating.  The
   model answers the causal contents of A's next rooted update; it does not
   select a next initiator for a root-free universe or sew overlapping
   peer-initiated diamonds.

The closing executable is frozen as a new companion, not an in-place erasure
of D35b.  It must:

```text
maintain actor-owned issued-incoming capability sets;
validate the whole LocalOption before any durable mutation;
derive call/event ordinals from root-owned wire succession;
canonicalize the complete supplied seed event DAG and rerun 16/408 alpha tests;
construct exact common-input flagged direct-sum operators for all five root options;
separate bounded local outcome rank from unbounded structural provenance;
place a source bit at non-A actor D and compare queried, unqueried and disconnected interventions;
make volatile rejection semantics explicit and test them honestly;
rerun every inherited D35b gate under two independent hash seeds.
```

The direct-sum construction may use exact rational Gram identities rather
than floating square roots: for common-input isometries `V_o` and orthogonal
injections `J_o`, verify

```text
V_o^dag V_o = I;
(J_o V_o)^dag (J_p V_p) = 0 for o != p;
sum_o q_o (J_o V_o)^dag (J_o V_o) = I.
```

The non-A intervention must not merely change a digest.  The returned payload
must be an explicit durable A2 field, must bind every accepted adjacent return,
and must differ under `do(D=0)`/`do(D=1)` only on histories whose completed
query tree reaches D.  The paired history probabilities themselves may remain
equal; an interventionist acquisition claim requires the conditional A2
record content to change, not necessarily the action weights.

Even a clean close can earn only the supplied rooted nested-call family.  The
root-free object suggested by the review is a compatible local specification
on finite causal diamonds: each boundary-conditioned diamond kernel must agree
with restrictions and overlaps of larger diamonds.  Such a DLR/projective
family could define a global history measure without selecting a global next
event or assigning proper times.  D35 does not silently claim that missing
overlap theorem.

## 17. D35c closing result before independent review

The separate closing companion is
`code/d35c_local_specification_exact.py`, with receipt
`data/d35c_local_specification_exact.out`.  It hash-locks D35b at
`fa6d69e6...253c4d` and leaves both rejected predecessors unchanged.  Hash
seeds 17 and 65537 are byte-identical.  Candidate hashes are:

```text
source   50f1e710cc04de3576b24bd5e7414764f1dea1ebb86f0b0b5747d2b18109c765
stdout   d8f0ef0c4320ff58badcff6ce6916fe7a3f4adb94b58de8afd95c4aa09bb6f42
science  da82ce3ca611fd2e51f0d0e4fd3a36ec74edb895c279e9f6bcd48ac8ceb5aebf
```

The candidate passes `16/16` at exact rational grade.

### 17.1 Local causal probability result

The physically meaningful statement is now:

> Given A1 and the supplied A-rooted local call grammar, A2 is the upper seal
> of the finite completed call diamond.  An evidence bit is in A2 exactly when
> its adjacent query/return chain is part of that diamond.  Before completion,
> the probability is the sum of the exact local-menu products of precisely
> those completed diamonds.

This contains no duration.  The integer on A's calls is derived from A's own
successor count and used only for fresh structural identity; it is causal
ordinal data, not seconds, a rate or a proper-time variable.  FIFO, LIFO and
canonical machine service orders give the same 16-atom law in each parameter
cell.  Thus no global commit order is physical within the laminar grammar.

A new D-only source seal makes the transport test nonvacuous.  In each Q cell,
six of the 16 complete histories query D through `A -> B -> D`; ten do not.
Under paired `do(D=0)` and `do(D=1)` interventions, structural support and
every branch probability remain identical.  The durable A2 bit and D-source
identity change in exactly the six queried histories and in none of the ten
unqueried histories.  Each child return carries the bit and source set inside
the return envelope, bound by the evidence digest/signature; the parent does
not infer it merely from the machine service order.  Changing an isomorphic
disconnected source leaves the A2 projected law fixed.  This earns a concrete
operational acquisition theorem for one bounded classical evidence channel,
not for arbitrary quantum information or every ancestral correlation.

### 17.2 Fail-closed actor result

Each actor now owns the exact set of incoming capabilities actually issued to
it.  A structural lookalike absent from that set rejects.  The full local menu,
typed legs, event identity and newborn identity validate before the issued
token is consumed or a transfer is recorded.  Five closing cases—including a
genuine token paired with invalid choices—leave the complete logical state
unchanged.  Service peeks first and acknowledges only after success, so a
rejected envelope stays queued for explicit policy rather than disappearing
silently.  The inherited nine D35b cases still pass `9/9`.

This is logical actor locality, not a claim that Python created independent OS
processes.  The exact simulator deliberately maintains one shared persistent
event-DAG audit and one exact joint carrier vector, because entangled quantum
states need not factor into actor-owned wavefunctions.  The stochastic action
menu and admissible ports are actor local; the shared objects record the joint
physical history/state.  A separate distributed tensor-network implementation
would be an engineering/theorem target, not an earned D35 result.

### 17.3 Complete event alpha quotient and projectivity

Seed-event identity is now the recursively marked rooted causal structure,
not the raw strings `A0`, `AB`, `AC`, `BD`, `A1` or `D-source-seal`.  A joint
renaming of all actor display names, all six seed events, every predecessor
reference and every tip reproduces the same 16 physical atoms in Q1 and Q2.
On that renamed presentation the full 16 first cylinders again equal the
exact marginal of 408 second-call refinements, with 408 persistence checks.
The unrenamed 16/408/408 gate separately passes.

This is a canonicalization theorem only for the declared finite supplied seed
class.  It is not a general efficient graph-isomorphism algorithm for every
possible root-free history.

### 17.4 Common-input variable-support instrument

At the initial degree-two root, all five alternatives are now maps from the
same eight-dimensional `A tensor B tensor C` input.  Idle is extended over the
two spectators; the two visits act on their named target and as identity on
the other; fork acts on all three; birth maps the same input to a
16-dimensional sector with one fresh child.  Their five output sectors form
one explicit 48-dimensional direct sum.

Exact matrices establish:

```text
five self-Gram identities on the common 8-dimensional input;
10/10 cross-alternative Gram matrices equal zero;
sum_o q_o W_o^dag W_o = I_8 exactly.
```

The bounded local outcome alphabet has rank four—idle, birth, visit, fork.
The five degree-two alternatives additionally contain structural port
incidence.  Unbounded transaction/path/address provenance is retained
separately and is not called a bounded local flag.  The earned noun is a
classical-output common-input direct-sum quantum instrument at the registered
local sector, with branchwise D24/unitary carrier maps.  A coherent amplitude
sum over alternative support graphs remains open.

### 17.5 Birth answer

The closing does not turn D24 into a uniqueness theorem.  It sharpens the
factorization:

```text
local opportunity instrument: q_idle, q_birth, q_visit, q_fork and port choice;
conditional newborn content:  D24 B_g on the selected birth alternative.
```

Q1 and Q2 satisfy the same causal, projective, actor, quantum and transport
gates but retain

```text
P_Q1(A2 birth)=1/4, P_Q2(A2 birth)=1/5;
P_Q1(A2 visit)=1/4, P_Q2(A2 visit)=3/10.
```

Therefore neither strong causal locality, no proper time, construction gauge,
D24/D25/D27 reception, sealed records, diamonds nor the existing profinite
work selects the numerical birth opportunity or coupling.  The “right birth
kernel” known here is a valid family plus explicit unselected parameters, not
one derived universal law.

### 17.6 What a real time-free universe simulation still needs

D35c is a real executable sampler of its supplied A-rooted family, but it is
not yet a real root-free universe simulation.  It repeatedly asks A to open a
call.  It never decides, from the physical law, whether A, B or another actor
initiates an overlapping transaction.

The corpus suggests a candidate time-free replacement for a global next-event
race.  It is not yet a defined SHARD architecture.  For every oriented finite
causal region D and admissible boundary record b, one would seek a normalized
local kernel

```text
gamma_D(interior marked history | boundary b).
```

The region category, incoming/generated/lateral interfaces, boundary
extraction, restriction transport and conditional kernel-composition law must
first be defined.  Pairwise agreement on overlaps is not sufficient: every
finite cover needs a coherent positive joint extension.  Only after a global
history space and an existence theorem are supplied would “A's next click” be
a marginal of regions whose upper seal is A2, without selecting a global next
actor or adding a proper-time race.

The current nested calls are laminar and their internal rooted consistency is
easy.  They motivate the candidate architecture but are not yet a proved
special case, because no embedding into the missing region category has been
defined.  The next foundational problem is the overlap theorem for peer-
initiated regions with births and shared quantum instruments.  That is where
locality, diamonds, whole histories and the profinite finite-stem idea could
meet.  Profinite completion could preserve a compatible family; as Papers 4/8
and D3 already proved, it cannot choose the family or repair an incompatible
one.

### 17.7 Candidate decision

Subject to independent closing review, D35c earns:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

It does not earn a selected history law, the right universal birth numbers, a
root-free local universe simulation, proper time, Lorentzian geometry, v9
cone/dimension implications, G or nature's interactive click law.

## 18. Hostile round 3 and frozen typed-identity close

**Round-3 verdict:** the quantum and locality repairs substantially pass, but
terminal covariance is again withheld:

```text
probability/covariance          0B / 1M / 0m / 0n
causal locality/fail-closed     0B / 0M / 1m / 0n
quantum/birth/ontology          0B / 0M / 1m / 0n
```

Reports:

- `reviews/d35-round3-probability-covariance-final-review.md`;
- `reviews/d35-round3-causal-locality-final-review.md`;
- `reviews/d35-round3-quantum-birth-final-review.md`.

The quantum lane independently reconstructs the five common-input maps with
output dimensions `16,8,8,8,8`, their 48-by-8 flagged injections, all five
self Grams, all ten cross zeros, spectator placement and exact weighted
identity.  It also confirms the D24 instant and the six queried/ten unqueried
D-origin paired histories.  The locality lane confirms issued ownership,
prevalidation, peek/ack, carried return fields, local menus, shared-joint-state
scope and actor-owned causal ordinal.  Fresh independent seeds reproduce the
candidate receipt.

Three openings are frozen before the terminal companion:

1. **Typed-freshness major.**  The structural `physical_key` is name-free, but
   the generator allocates future event/newborn storage with raw strings.  A
   complete seed rename `A0 -> EROOT-CAP-0::T1:r` leaves the first 16-atom law
   equal and makes the second call reject.  Renaming to the call-five string
   makes calls zero through four pass and the sixth reject.  Renaming actor D
   to `NROOT-CAP-0::T0:r` makes the root-birth branch reject.  Hence the kernel,
   unlike its reporting key, does not descend to the full alpha quotient.
2. **Root-input minor.**  `start_root_call(request_payload=2)` writes the
   transaction state, enqueues and advances A's ordinal before later rejection.
   The bit alphabet must validate at the public boundary before mutation.
3. **Disconnected-control wording minor.**  The remote fixture proves
   disconnection invariance but is not isomorphic to the connected D source
   seal.  Either remove “isomorphic” or build a typed disconnected copy of the
   source-seal component.  The terminal protocol chooses the stronger latter
   control.

The final companion must put identities in disjoint structural types:

```text
supplied actor identity;
generated actor identity = (component, root causal ordinal, call path);
supplied event identity;
generated event identity = (component, root causal ordinal, call path);
disconnected-control identity.
```

Display strings may be alpha-renamed to any text, including the printable form
of a future generated identity, without storage collision.  The companion
must repeat the next-call, late-call and newborn collision probes in Q1/Q2,
the original and renamed 16/408 projectivity gates and multi-call replay.
It must validate the root bit before all writes and compare two genuinely
isomorphic source-seal components under disconnected `do(0/1)`.

The terminal receipt should additionally print the exact causal reach
probability, not only the number of histories.  Direct summation already gives

```text
P_Q1(D reaches A2) = 1/16;
P_Q2(D reaches A2) = 3/40.
```

These unequal values are a sharper nonselection observable: causal locality
defines which completed diamonds count, while the supplied Q cell determines
their total probability.

## 19. D35d typed-identity terminal candidate

The terminal companion is
`code/d35d_typed_identity_terminal_exact.py`, with receipt
`data/d35d_typed_identity_terminal_exact.out`.  It hash-locks D35c at
`50f1e710...9c765`.  Seeds 17 and 65537 are byte-identical.  Candidate hashes:

```text
source   9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28
stdout   2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574
science  79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c
```

The exact receipt passes `18/18` in Q1 and Q2.  Supplied actors, generated
actors, supplied events, generated events and disconnected-control identities
are distinct value types.  Display text is no longer storage identity.  Three
previously fatal alpha cases now pass:

```text
seed display equals the call-one generated-event print form: 16/408/408;
seed display equals the call-five print form: six calls complete;
actor D display equals the root-newborn print form: all 16 branches normalize.
```

Ordinary joint actor/event renaming separately passes 16/408/408.  The
registered unrenamed law passes 16/408/408, all first states receive second
calls under all serializers, and eight-call replays agree.

The public root constructor now rejects non-bit payloads before writing a call
ordinal, root field, issuance set or mailbox.  The closing battery is `6/6`
whole-state unchanged plus the inherited `9/9`; rejected service still retains
the envelope for an explicit policy.

The disconnected control is now an exact marked copy of D's ancestral source
gadget: one seed actor event, two successive one-parent seed births and one
terminal source seal.  Only its disconnection and typed control domain differ.
Changing its bit leaves the A2 projection exactly fixed.  The connected
intervention retains six queried and ten unqueried histories, with 18 carried
return-hop checks.  Exact reach probabilities are printed as `1/16` and
`3/40`.

The common-input instrument and D24 results are unchanged: input dimension 8,
direct-sum output dimension 48, five alternatives, bounded operation rank 4,
ten zero cross Grams and exact weighted identity.  Typed storage affects no
carrier amplitude or local probability.

The candidate terminal decision remains:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

It is now alpha-safe at the supplied and generated identity boundary, but it
is still rooted, laminar and conditional on A initiating.  It does not close
overlapping diamond specifications, choose Q or g, generate coherent support
sectors, derive a global history law from SHARD alone, recover spacetime or
identify nature's law.  A narrow independent delta must accept typed freshness,
early root validation and the isomorphic disconnected fixture before this
section becomes terminal.

## 20. Terminal hostile close

All three round-4 deltas are clean:

```text
typed covariance/completion      0B / 0M / 0m / 0n
root validation/locality         0B / 0M / 0m / 0n
evidence/quantum/birth            0B / 0M / 0m / 0n
```

Reports:

- `reviews/d35-round4-typed-covariance-closing-delta.md`;
- `reviews/d35-round4-root-validation-locality-closing-delta.md`;
- `reviews/d35-round4-evidence-quantum-closing-delta.md`.

The covariance lane independently verifies disjoint supplied/generated
identity value types, ordinary 16/408/408 alpha projectivity, immediate and
late display collisions, all 16 newborn-collision branches, eight-call
serializer equality and the countable completed rooted-history measure.

The locality lane probes six non-bit root inputs in both Q cells and finds the
complete serialized object unchanged on every rejection.  It rebuilds all six
closing cases, every generated actor over all 16 first histories and 408
refinements, reciprocal ownership keys, current tips and eight-call typed
birth continuity.  The shared-joint-state/rooted scope remains explicit.

The evidence/quantum lane proves an exact marked graph isomorphism between the
connected `A -> B -> D` source ancestry and disconnected `u -> v -> w` control
at bits zero and one, with no cross-component incidence.  The disconnected
intervention preserves both the A projection and the complete connected
16-atom distribution.  It re-derives reach masses `1/16` and `3/40`, all
8-to-48 operator identities and every D24 marginal row.

The terminal D35 decision is therefore:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

### 20.1 What is closed

1. A's next click needs no numerical time: it is A1's first causal wire
   successor and the upper seal of a completed finite local call diamond.
2. Realized evidence reach is binary.  Its pre-click probability is the exact
   measure of completed diamonds containing the licensed adjacent return path.
3. A logical actor/mailbox simulator can implement the supplied laminar law;
   its service order is gauge, not a physical global commit sequence.
4. One D-origin bounded datum reaches A2 exactly on queried paths, with
   disconnected and unqueried nonleakage.
5. D24 is compatible as the conditional newborn-content isometry inside one
   common-input classical-output variable-support instrument.
6. The finite rooted kernels are normalized, fully projective and extend to a
   completed classical rooted-history measure.
7. Typed freshness makes the supplied/generated kernel alpha safe at the
   declared grammar.

### 20.2 What is not closed

1. Q1 and Q2 both pass but disagree on birth, visit and causal reach; no
   inherited principle selects `q` or `g`.
2. The root A, ownership orientation, laminar request protocol and capability
   grammar are supplied physics.
3. No overlap-consistency theorem exists for peer-initiated causal diamonds,
   cycles, joins or disconnected-component birth.
4. The exact quantum state is evaluated jointly; independent actor-owned
   storage of an entangled state and coherent superposition of support graphs
   are not proved.
5. Profinite completion, v9 cones/dimension, units, G and proper time are not
   derived.  Profinite machinery may preserve a future overlap-consistent
   family but cannot select it.

The most pressing next theory target is consequently not another clock.  It
is the **causal-diamond specification problem**: characterize and, if possible,
select normalized local birth/interaction instruments whose kernels agree on
every restriction and overlap.  Only after that root-free history law exists
should its grown causal webs be returned to the D28--D32 cone, dimension and
“many clocks, few factors” tests.

### 20.3 Paper-level scope corrections

Paper 24's independent hostile round does not reopen the terminal executable,
but it narrows two interpretations of this note.  First, a completed call is a
finite realized acquisition/stopping region; the D35 kernel still conditions
on the complete typed rooted state, so predictive-boundary sufficiency and
minimality are not proved.  Second, an overlap-consistent regional law is only
a candidate architecture until its oriented region category, interfaces,
boundary extraction, restriction/transport kernels, coherent finite-cover
extensions and global completion are defined.  The laminar D35 family
motivates that architecture but is not yet a proved special case of it.

The corpus audit is also frozen at the pre-D35 tree
`fc074b9ec4f2c9ecdef28b61c623d89d08e76432`, preventing later papers from
entering the antecedent stream.  The terminal census remains 441/427 with
unchanged stream `b0e4c7e0...41b7`, source `44568721...0a21`, receipt
`7f998dea...4182` and `PASS 6/6` under independent hash seeds.
