# D35 — timeless local next-click law

**Status:** PIN before corpus receipt, derivation, simulation or result.
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

The realized relation is binary.  The pre-click probability is the cylinder
ratio

```text
P(e reaches A2 | H0)
 = mu({completed H extending H0: e in NewPast_A(A1,A2(H))})
   / mu({completed H extending H0}).
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
`data/d35_corpus_causal_inventory.out`.  It content-hashes all 437 primary
paper/note artifacts in V1--V10 existing before D35; 423 hit at least one
registered causal/birth/time category.  The frozen corpus stream hash is

```text
84d6fb20bf780d268ba825c38120e4754abdfce30e448a6df6ad66993fc27485
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
