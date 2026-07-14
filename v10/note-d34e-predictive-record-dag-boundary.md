# D34e — the predictive record-DAG boundary

**Status:** preregistration before D34e receipt code.  **Date:** 2026-07-13.

**Parent:** Paper 21 section 10 at terminal commit `70e0b4d`.

## 1. Question

D34d proved that the chosen D34b law is strong Markov on its complete global
configuration and that A's own record is not sufficient: B gaining a child
changes the incoming B-to-A rate from `1/4` to `1/8` while A is unchanged.
D34e asks the positive question:

> For a frozen passive D34b query, what distributed record-DAG boundary screens
> A's future, can it update without consulting hidden global history, and is
> its physical width bounded?

The investigation also asks how the answer changes when the licensed query is
enlarged from a coarse A-wire process to the complete durable ancestry of A's
future records.  The query classes are frozen separately because the canonical
predictive quotient is query-relative.

This note is a pin, not a result.  The executable, receipts and reviews do not
exist at the time of this commit.

## 2. Frozen law and ontology

The classical law is exactly the terminal chosen D34b exemplar.

- Every active unsealed actor has an independent rate-one Poisson ring.
- At its ring it births with probability `1/4`, interacts with each eligible
  neighbor with probability `1/(4d)`, and idles with probability `1/2`.
- Birth creates a fresh Ulam child joined only to its parent.
- Interaction appends one shared event to the two actor wires and toggles the
  modeled classical carrier bit on both actors.
- Idle appends one event only to the initiator wire.
- The event records, wire predecessors, actor counters and adjacency persist.
- There is no joining of previously disconnected components and no dynamic
  sealing in this chosen law.

The initial connected specimen is the edge `A--B`; disconnected product
controls may be added.  The ideal probability source, not the deterministic
reference PRF, owns the theorem.

No D34b coefficient, adjacency rule, carrier operation or initial condition is
derived here.  D34e characterizes the predictive representations of this
chosen law.

## 3. Frozen passive branches

No interventional law is supplied by D34b.  D34e therefore runs passive
classical branches only.  The operational quantum branch is separately gated
in section 12.

### 3.1 Branch C — coarse local A-wire process

The durable readout at every event touching A retains:

```text
construction time,
direction/kind in {A-birth, A-idle, A-outgoing, incoming-to-A},
A's carrier bit after the event,
A-own-ring count,
A-wire-event count.
```

It deliberately forgets actor names beyond the role at the event, the remote
wire predecessor and the transitive event ancestry.  This is a covariant coarse
record query, not the complete SHARD record.

### 3.2 Branch L — role-labeled local A-wire process

This branch additionally retains which incident boundary actor sourced or
received an interaction, modulo a declared relabeling of the typed star.  It is
used to test the record-native labeled-star carrier and typed composition.

### 3.3 Branch F — full durable A-record ancestry

This branch retains the complete typed record of every future event touching
A, including its two wire predecessors where present and the persistent
transitive ancestor sub-DAG reachable through those predecessors.

Branch F is not allowed to inherit a positive result from C or L.  A carrier
that predicts event kind but loses a remote predecessor fails F.

## 4. Stopping scopes

Every result is tagged with one of:

1. fixed construction time `T`;
2. the next or `m`th A-own ring;
3. the next or `m`th A-wire event, including passive incoming receptions.

Fixed global event depth is an auxiliary enumeration truncation and a named
locality-negative control only.  It cannot certify regional screening.

The theorem branch is `POINTWISE` on every legal finite D34b configuration,
using the explicit ideal generator.  Finite enumeration uses reachable
positive-cylinder histories.  No arbitrary regular-conditional value on a
null history is consumed.

## 5. Candidate carriers

### B0 — one record

A's carrier, counters and tip only.  D34d already supplies the exact
`1/4 -> 1/8` obstruction.

### B1 — instantaneous-rate summary

```text
(A carrier, A degree, aggregate incoming rate)
aggregate incoming rate = sum_(x neighbor A) 1/(4 degree(x)).
```

This may determine current coarse rates without being recursively closed.

### B2 — covariant degree histogram

```text
(A carrier, optional stopping counters,
 n_k = number of A-neighbors currently having degree k for every k>=1).
```

This is a behavioral quotient.  It is not presumed to be stored centrally in
A.

### B3 — distributed typed star

The physical collar consists of:

- A's own locally stored carrier/counters;
- every currently incident neighbor record;
- that neighbor's locally stored degree/eligibility row;
- the typed incident ports and their actor identities modulo relabeling.

The star is distributed: a neighbor birth updates the neighbor's own degree
without sending a new event to A.  An analyst can read the collar; A alone need
not store the histogram.

### B4 — whole connected component

The complete current D34b configuration restricted to A's connected component,
including persistent event records and wire tips.  Disconnected factors are
excluded.  This is an obvious sufficient upper bound but is not presumed
minimal.

### B5 — D5-style factor message

This candidate is refused unless a complete physical factor cover, scopes,
values, interface embeddings and exactly-once ownership are supplied.  D5
contraction alone cannot create those data.

## 6. Proposed coarse boundary generator

For Branch C, write the histogram as `h=(n_1,n_2,...)`, let
`d=sum_k n_k`, and let `c` be A's carrier.  The proposed relevant generator is:

```text
A birth:
    rate 1/4,
    h -> h + one degree-1 neighbor,
    output A-birth;

A idle:
    rate 1/2,
    h unchanged,
    output A-idle;

A outgoing interaction:
    aggregate rate 1/4,
    c -> 1-c,
    output A-outgoing;

degree-k neighbor birth:
    aggregate rate n_k/4,
    n_k -> n_k-1, n_(k+1) -> n_(k+1)+1,
    no A-wire output;

degree-k neighbor interaction into A:
    aggregate rate n_k/(4k),
    c -> 1-c,
    output incoming-to-A.
```

All other actors/events leave this carrier and Branch-C output unchanged.  The
receipt must derive this row partition from the full D34b generator and compare
it with exhaustive reachable finite states.  It may not infer the theorem from
the finite comparison alone.

For consecutive continuous-time updates the boundary kernel includes elapsed
time and no-relevant-event survival.  Exponential memorylessness removes a
renewal-age coordinate but does not remove the current degree histogram.

## 7. Exact obstructions frozen in advance

### O1 — one record

Reuse only the terminal D34d witness: B's degree changes from one to two while
A's private state and tip do not, changing B-to-A intensity `1/4 -> 1/8`.

### O2 — current rates do not imply recursive sufficiency

Compare two reachable degree multisets:

```text
H = {2,3,6},        H' = {2,4,4}.
```

Both have three neighbors and

```text
sum_(k in H) 1/k = sum_(k in H') 1/k = 1,
```

so B1 gives the same current A degree and incoming rate.  But if
`f(h)=sum_k n_k/(4k)`, the boundary generator gives

```text
L f = 1/16 - sum_k n_k/[16 k(k+1)].
```

The two exact values must differ.  This distinguishes their future incoming
laws at the next nontrivial time order and refutes B1 as an all-future state.

### O3 — every fixed radius can lose durable ancestry

For every registered radius `r`, grow a reachable actor chain with an actor D
outside radius `r` of A and a leaf E.  Construct two positive-cylinder pasts
with the same radius-`r` restriction but different durable D-tip records
(D-idle versus D-to-E interaction).  Then use the same positive-probability
sequence of inward interactions to propagate D's tip ancestry along the chain
to a future event on A.

The future cylinder asks for that exact inward sequence and inspects the
persistent ancestor sub-DAG of A's final record.  It has positive probability
in one branch and zero in the other because the old D record is immutable.
This refutes fixed-radius carriers for Branch F.  It does not prove that the
literal whole component is the unique possible encoding.

## 8. Composition and covariance gates

The role-labeled star B3 must be represented as typed actor rows, crossing
ports and boundary references.  For disjoint adjacent regions R and S:

1. duplicate references must agree on the referenced actor degree;
2. internal actor rows have exactly one owner;
3. composition is typed union plus validation, never positional concatenation;
4. the result must equal the directly constructed star of `R union S`;
5. relabeling the global actor graph before or after construction must commute
   with the carrier up to the same relabeling.

The histogram B2 may be a smaller Branch-C quotient while failing this typed
composition requirement.  The distributed B3 carrier, not a fictitious
central histogram stored in A, owns any record-native composition claim.

## 9. Capacity ledger

Every candidate prints:

```text
graph radius,
actor/record count,
open-port count,
number of occupied degree bins,
largest degree and integer bit cost,
A counter bit costs,
continuous coordinates/precision (none for the embedded state),
explicit unbounded fields.
```

For the chosen exponential law, A births form a rate-`1/4` thinned Poisson
process.  Hence at every `T>0`, A's degree has unbounded support, and along an
infinite realization it grows without bound almost surely.  A fixed radius-one
star is therefore not a bounded-width carrier.

## 10. Finite audit domain

The first receipt freezes

```text
D(N=4 global embedded events,
  H=3 relevant boundary transitions,
  Q={C,L,F as separately tagged},
  I=passive only,
  S={fixed T, A-own-ring, A-wire-event};
  global depth auxiliary only).
```

It must:

1. enumerate every reachable D34b embedded state through global depth four;
2. compare the projected full-generator rows with the proposed B2/B3 rows;
3. run the exact O1 and O2 witnesses;
4. run O3 for radii `r=0,1,2,3` and print each positive path mass;
5. test B3 composition and relabeling on nontrivial adjacent regions;
6. report finite predictive signatures only as `D(N,H,...)` evidence.

The analytic row partition, nonexplosion and standard pure-jump uniqueness may
promote B2/B3 screening beyond the finite domain if every hypothesis is carried
explicitly.  Finite enumeration alone may not.

## 11. Profinite/stem-spectrum branch

The candidate map is

```text
u: completed marked D34b histories -> unmarked completed causal orders.
```

Before use, D34e must gate:

1. finite-time nonexplosion implies every D34b event has finite past;
2. forgetting actor/event marks gives a past-finite causal order;
3. `u` is invariant under the declared event/Ulam relabeling gauge;
4. `u` is Borel on the cylinder coding;
5. the supplied completion law has the required conditional pushforward.

At an online past `h`, the candidate v9 datum is the adapted posterior measure

```text
nu_tau(h) = (phi o u)_* mu(completion in . | F_tau)(h),
```

not one completed stem-spectrum point.  D34e does not claim that `nu_tau`
screens C, L or F.  An unmarked stem shadow also cannot carry arbitrary marked
carrier/quantum outputs without a separate marked-factor theorem.  A marked
profinite bridge requires explicit finite discrete quotients; general
compactness is insufficient.

## 12. Quantum branch

The terminal corpus supplies:

- finite D34c strongly-positive typed-DAG functionals;
- one auxiliary finite `P,E` causal-break negative control;
- no timed controlled D34b-D34c process family on which to define
  `P(r|I,h)` for every licensed instrument sequence.

Therefore the intrinsic operational quantum D34e branch is preregistered to
return `REFUSAL/UNDEFINED` unless that missing controlled process object is
constructed as an additional input.  The classical receipt may type the gates
but may not assign `d_carrier`, `d_op` or `chi_cut` to SHARD from the auxiliary
example.

## 13. Frozen verdict rules

Each branch emits one Paper-21 section-10 outcome and separate flags for
screening, recursive closure, covariance, composition, capacity, NSE and
profinite/quantum applicability.

- Branch C can earn `ALL-FUTURE GROWING-CARRIER PASS` only from the analytic
  generator-factor theorem plus physical B3 realization and composition.
- Branch F can earn only what its ancestry theorem proves.  O3 by itself earns
  `CANDIDATE-CLASS OBSTRUCTION` for fixed-radius carriers, not universal
  whole-component necessity.
- The profinite branch remains `REFUSAL/UNDEFINED` or `FINITE-DOMAIN ONLY`
  unless the candidate-map and posterior-factor gates pass.
- The intrinsic quantum branch remains `REFUSAL/UNDEFINED` without the timed
  controlled process family.

No branch may average partial flags into a bounded-collar headline.

## 14. Claim ceiling before execution

Maximum possible result of this pin:

> For the chosen D34b law and the explicitly coarse passive A-wire query, a
> distributed record-DAG star is an exact recursively closed all-future
> predictive carrier, but its width is unbounded.  Enlarging the query to full
> durable ancestry defeats every fixed-radius carrier by an exact positive-
> cylinder witness.  No minimal full-record carrier, v9 profinite
> factorization, intrinsic quantum boundary, relativistic light cone, proper
> time or universe law follows.

The receipt and hostile reviews may force a lower ceiling.

## 15. Provisional receipt before hostile review

`v10/code/d34e_predictive_boundary_exact.py` currently passes `11/11` and its
stdout byte-matches under `PYTHONHASHSEED=17,65537` with file SHA-256
`81dc0a289631f97961a661fda9ce3b3aed36b40e298024173cbc693998eb2586`.
The internal summary digest is
`48d83ba568052d4822278f43efe0c3a268e268e6372e642219b6b400c027d3fd`.

The provisional result is query-relative.

### 15.1 Coarse and role-labeled local wire branches

The full generator projects exactly to both:

- the covariant state `(A carrier, multiset of neighbor degrees)`; and
- the role-labeled distributed star carrying each incident actor and its
  degree.

All `2,927` reachable states through global embedded depth four agree with the
closed formulas, with `2,898` repeated coarse-boundary comparisons.  The
analytic row partition is not depth-limited: only A's own rows and births or
incoming interactions of its current neighbors can change the projected state
or output.  The inherited D34b nonexplosion theorem then supplies the unique
all-future marked pure-jump projection.

The state is local in graph radius but not bounded in physical width.  A's
births form a rate-`1/4` Poisson process, so the number of incident ports has
unbounded support at every positive construction time and grows without bound
along an infinite realization.  Provisional Branch C/L verdict:

```text
ALL-FUTURE GROWING-CARRIER PASS / POINTWISE.
```

### 15.2 Exact compression failures

The D34d one-record obstruction survives.  A stronger D34e witness shows that
even the complete current rate summary is not recursively sufficient:

```text
{2,3,6} and {2,4,4}
```

both give current aggregate incoming rate `1/4`, but their infinitesimal
incoming-rate derivatives are `61/1344` and `11/240`, differing by `1/2240`.
Both pasts are reachable with positive exact cylinder mass.

### 15.3 Full durable ancestry

For radii `0,1,2,3`, exact outside-radius record pairs and inward interaction
paths give future cylinder masses

```text
1/24, 1/1024, 1/64000, 1/5308416.
```

The general radius-`r` mass is `[1/(8(r+3))]^(r+1)>0`.  Thus every fixed
actor-graph radius loses some full durable A-record ancestry.  The whole
connected component is a sufficient growing upper bound and disconnected
components factor, but no theorem yet identifies the minimal full-record
encoding.  Provisional Branch-F disposition is fixed-radius
`CANDIDATE-CLASS OBSTRUCTION`, not whole-component necessity.

### 15.4 Stem/profinite and quantum ceilings

Finite mark-forgetting produces `4` unmarked order classes at depth three and
`10` at depth four; depth-four prefix restriction exactly recovers the
depth-three pushforward.  This checks only the finite candidate map.  It does
not construct the adapted posterior on the v9 completed-history stem spectrum
or prove that the posterior screens any D34e branch.

The intrinsic quantum branch returns `REFUSAL/UNDEFINED`: D34c's finite
functionals and the auxiliary `P,E` witness do not supply the missing timed,
controlled D34b-D34c process family.

Three independent hostile streams are required before any provisional noun is
promoted: predictive/probability/profinite; locality/record/capacity; and
full-ancestry/quantum/process scope.
