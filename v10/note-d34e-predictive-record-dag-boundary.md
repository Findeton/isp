# D34e — the predictive record-DAG boundary

**Status:** historical pin through section 14; provisional receipt rejected by
hostile round 1; replacement protocol frozen in section 16; replacement
receipt passes `13/13` in section 17 but was rejected by round 2; the second
repair protocol is section 18, its `13/13` receipt is section 19, and all three
closing deltas accept the declared theorem ceiling in section 20.  Paper-level
round 1 preserved the science but opened an executable-integrity repair;
sections 21--22 freeze that repair and its candidate receipt pending a closing
paper delta.  Sections 23--26 carry the paper-level repair chain and terminal
acceptance.
**Date:** 2026-07-13.

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

## 16. Hostile round 1 and frozen replacement protocol

The three independent reviews reproduced the provisional stdout exactly and
found no counterexample to the histogram generator, the distributed-star
construction, the B0/B1 obstructions, the all-radius ancestry idea, the
component ceiling or the quantum refusal.  They nevertheless reject the
provisional `11/11` and its theorem label:

```text
predictive/profinite: 0 blockers / 2 majors / 1 minor / 1 nit;
boundary/locality:    0 blockers / 2 majors / 4 minors / 1 nit;
ancestry/quantum:     0 blockers / 2 majors / 3 minors / 2 nits.
```

The following repairs are frozen before the replacement executable is edited.

### 16.1 Time and stopping convention

Branch C/L future records retain **elapsed time from the conditioning stop**,
not an absolute construction timestamp.  Histories related by a common time
translation are identified.  This is sufficient for the time-homogeneous
Poisson law and avoids pretending that a continuously precise absolute clock
is a finite record field.  A-own-ring and A-wire-event counts are appended to
the actual projected carrier and updated in its generator rows.  Their hitting
times use the inherited strong-Markov theorem for the complete boundary CTMC;
the simple exponential gate refers only to the next full boundary transition.

### 16.2 Finite predictive partition

The registered finite state domain is the set of distinct coarse boundaries
actually reached through global embedded depth four.  Horizon signatures are
computed coinductively from output labels, exact rates and the **previous-
horizon successor class**, aggregating rows entering the same class.  Raw
successor states are forbidden in a predictive signature.  The separate
synthetic 110-state family may be retained only as a named stress test; it is
not called `D(N=4)`.

### 16.3 Physical B3 schema and updater

The B3 carrier at A is frozen as:

```text
A-owned carrier, own-ring/birth/wire counters and incident endpoint ports;
one external endpoint row per current neighbor carrying its nominal role,
current eligible degree and its locally owned birth ordinal;
one shared edge identifier with two endpoint-port records;
elapsed time from the conditioning stop, supplied as an update increment.
```

Nominal actor names are presentation labels.  Gauge maps fix the distinguished
A role, transport old names and extend functorially to Ulam children.  The
replacement receipt must implement an updater that consumes only the old B3
carrier, elapsed/survival data and one typed local/passive/silent event; it
must compare that update with direct projection of every enumerated full-state
row.  It must also print the maps B3-to-B2 and B3-to-the-role-labeled quotient.

### 16.4 Two covariance gates and typed composition

Relabeling covariance and construction-order covariance are separate.  The
receipt must check both actor/fresh-name transport and both serializations of
every registered pair of disjoint write-support events.  The analytic theorem
is that disjoint touched/created actor and event-record supports commute up to
the same nominal-name transport; finite pairs are a regression.

Composition treats an edge as one shared typed object and its two endpoint
ports as separately owned incidence records.  Typed union must validate every
duplicated edge field and exactly-once port ownership, reject corrupted
duplicates, and agree with direct projection for every registered disjoint
region pair, not one specimen.

### 16.5 Complete fixed-radius carrier and Branch-F event

For the obstruction, `C_r(h)` is the complete physical restriction owned by
actors in the closed graph ball of radius `r`: full actor rows and endpoint
ports; every event on an owned wire, including cross-cut events; complete event
contents; and typed predecessor references, retained as opaque identifiers
when the referenced event is not owned.  The carrier may not recursively
dereference an opaque outside identifier, since that would cease to be a
radius restriction.

The two pasts put the differing immutable D-tip event wholly outside all owned
wires, so their complete `C_r` values agree.  The common future query `E_r` is
record-only and gauge-invariant:

> at the next A-wire event reached by the structurally selected inward chain,
> the durable ancestry contains that chain and its pre-existing remote
> endpoint event has kind idle.

The exact consecutive embedded path is a subcylinder.  Therefore the receipt
must distinguish

```text
P(E_r | h_idle) >= p_r = [1/(8(r+3))]^(r+1) > 0,
P(E_r | h_interaction) = 0
```

by immutability.  The fractions are embedded-chain lower bounds, not timed
cylinder probabilities.  For a continuous interval `Delta>0`, an optional
positive lower bound is obtained by multiplying `p_r` by the Erlang completion
factor for the first `r+1` component rings; it is not needed as an equality.
The theorem applies to this explicitly frozen complete radius-carrier family,
not to every imaginable bounded encoding.

### 16.6 Component, finite-unmarked and quantum scope

The whole connected component is tested only as a sufficient growing upper
bound.  Its recursive update and covariance follow from the pinned D34b
independent-Poisson/no-joining theorem; disconnected invariance is licensed at
continuous construction time and component-local stops, never fixed global
event depth.  No necessity noun is allowed.

The finite unmarked diagram is named exactly:

```text
(u_3 o r_(4->3))_* mu_4 = (u_3)_* mu_3,
```

where truncation occurs on the labeled committed prefix before marks are
forgotten.  No unmarked `4 -> 3` restriction, completed-history or v9
posterior theorem is inferred.  The intrinsic quantum branch pins the accepted
finite D34c dependency but remains `REFUSAL/UNDEFINED` because the timed
controlled D34b-D34c process and all-instrument kernels do not exist.

### 16.7 Executable first-applicable decision rule

Every branch is represented as `(mu,A,Q,I,S,C)` plus explicit screening,
closure, covariance, composition, bounded-capacity, necessity, universal-
exclusion and finite-domain flags.  The executable evaluates Paper 21's eight
outcomes in their frozen priority order and asserts that the emitted row is the
first applicable row.  Expected repaired dispositions are pinned as:

```text
C/L via B3:              ALL-FUTURE GROWING-CARRIER PASS / POINTWISE,
F complete radius C_r:   NO EXACT REALIZATION IN THE DECLARED CARRIER CLASS,
F whole component B4:    ALL-FUTURE GROWING-CARRIER PASS / POINTWISE
                         (sufficient upper bound; no necessity),
v9 posterior bridge:     REFUSAL/UNDEFINED beyond the finite diagram,
intrinsic quantum:       REFUSAL/UNDEFINED.
```

The F-radius row is permitted only if the repaired `C_r` equality and common
future-event proof quantify over every finite `r` in the frozen family.  The
B4 row is not evidence that the whole component is necessary.  For C/L, the
constructed B3 is unbounded; existence of a different bounded physical carrier
and minimality remain open.

### 16.8 Replacement gates

The replacement receipt must fail closed on: chosen-law normalization;
full-to-coarse and full-to-labeled generator projection including counters;
B0/B1 witnesses; correct coinductive finite partitions; physical B3 recursive
updates; relabeling covariance; disjoint-update covariance; typed composition
and corruption rejection; capacity/identifier ledger; complete `C_r` plus
`E_r`; component ceiling; the finite labeled-truncation/unmarked diagram;
typed quantum refusal; and the executable first-applicable scorecard.

No terminal paper is written until all three hostile streams review the
replacement delta and every major finding is either closed or explicitly
lowers the claim.

## 17. Replacement receipt before hostile delta review

The replacement executable passes `13/13`.  Runs under
`PYTHONHASHSEED=17,65537` are byte-identical.  The frozen artifacts are:

```text
code SHA-256
e3d3daee3297174183b970299df3289a03ce5491349aa1c43acc2a3a14d26533

stdout file SHA-256
b168723596fde346b227e6e96f9a00d0304740a498f834809d42afbab346f9bc

internal summary SHA-256
88ce0efb91521151d098bc8f68a132cf6b4fc3278d9be032785817a2452714c3
```

The replacement closes the round-1 defects at receipt level:

- the scoped coarse carrier includes A-own and A-wire counts, while time is
  explicitly elapsed from the conditioning stop;
- the finite predictive stress partition is coinductive and gives
  `(106,110,110)`, including the expected horizon-two B1 split;
- an independent physical B3 updater matches direct projection on `35,898`
  full-state rows;
- relabeling/fresh-name covariance and `120,276` disjoint-update swaps pass as
  separate gates;
- typed composition passes `159,734` ordered region pairs and rejects a
  corrupted duplicate shared edge;
- the complete radius carrier `C_r`, the common event `E_r`, its exact
  embedded lower bound and immutable zero are executable;
- the finite unmarked result is the labeled-truncation commuting diagram;
- the accepted finite D34c output is hash-pinned while the intrinsic quantum
  branch still refuses the absent controlled process;
- the decision machine unit-tests all eight Paper-21 rows before scoring the
  six scientific branches.

The provisional replacement dispositions are:

```text
C coarse / physical B3:             ALL-FUTURE GROWING-CARRIER PASS,
L role-labeled / physical B3:       ALL-FUTURE GROWING-CARRIER PASS,
F / complete finite-radius family:  NO EXACT REALIZATION IN THE DECLARED
                                     CARRIER CLASS,
F / whole connected component:      ALL-FUTURE GROWING-CARRIER PASS
                                     as a sufficient ceiling only,
v9 posterior bridge:                REFUSAL/UNDEFINED,
intrinsic timed quantum boundary:    REFUSAL/UNDEFINED.
```

The exact fixed-radius embedded lower bounds remain

```text
r=0: 1/24,
r=1: 1/1024,
r=2: 1/64000,
r=3: 1/5308416,
p_r = [1/(8(r+3))]^(r+1).
```

For `Delta=1`, the optional high-precision timed subcylinder lower bounds are
approximately `3.959221e-2`, `8.871307e-4`, `1.367731e-5` and
`1.598963e-7`.  They multiply the exact embedded mass by the named Erlang
completion factor and are not advertised as total event probabilities.

This section is still provisional.  It does not promote the result beyond the
replacement protocol until all three independent delta streams inspect the
new carrier schema, stopping theorem, ancestry event and decision priority.

## 18. Hostile round 2 and second replacement protocol

The first replacement is not terminal.  All three delta streams reproduced
its bytes and preserved the physical B3 construction, but each found an exact
output-typing or proof-hardening defect:

```text
predictive/profinite: 0 blockers / 1 major / 1 minor / 0 nits;
boundary/locality:    0 blockers / 1 major / 3 minors / 0 nits;
ancestry/quantum:     0 blockers / 1 major / 2 minors / 0 nits.
```

The following second repair is frozen before the executable is edited.

### 18.1 Observable marks versus internal boundary transitions

The live Branch-C/L query keeps post-event A-own and A-wire counters.  Every
non-silent A-wire output mark must therefore contain

```text
(elapsed time, kind/direction, post carrier, post own count, post wire count)
```

and Branch L additionally carries the incident role.  With the absolute
counter values retained, the `111` registered scoped states have exact finite
strong-transition class counts `(111,111,111)`, not `(29,29,29)`.

A neighbor birth is an internal boundary-state transition, not an A-wire
output.  The finite coinduction is therefore renamed a **strong boundary-
transition bisimulation stress test**: internal rows are typed as silent, not
advertised as observable `tau` records.  No claim is made that this strong
refinement is the canonical weak/timed predictive quotient of the observed
A-wire process.  The all-future result needs only an exact sufficient carrier;
minimal predictive quotient remains open.  Computing the weak timed quotient
would require eliminating arbitrarily many hidden neighbor births and is a
separate investigation.

The B1 pair `{2,3,6}` versus `{2,4,4}` is gated directly: equal at one internal
transition horizon and distinct at two, alongside the already exact observable
`Lf` proof.  The synthetic `(106,110,110)` stress family is not said to contain
that pair.

### 18.2 Root/role output covariance

The role-labeled closed generator is parameterized by its distinguished root,
not hard-coded to literal `A`.  Under a nominal map `g`, the receipt must check

```text
T_g Rows_root = Rows_(g root) T_g
```

on output marks, successor carriers and fresh Ulam children.  The semantic
output role remains “the distinguished root”; participant handles and a fresh
child `root/n` are transported.  Counter-bearing marks and silent internal
rows are included in the same conjugacy regression.

### 18.3 Endpoint-pinned full-ancestry event

The common Branch-F selector is frozen at the conditioning stop as

```text
(structural remote actor role D, D-own-ring ordinal k, immutable event D#rk).
```

The licensed future event is:

> the future A record contains the selected inward interaction chain and its
> ancestry contains that exact pre-stop event, whose kind is idle.

It must not follow D's moving tip.  The interaction branch is zero because the
selected ordinal already names an immutable interaction record.  The idle
branch contains the earlier exact positive subcylinder.  In addition to the
registered radii and relabeling transport, the receipt must insert later D
idles, later D interactions, unrelated events and several consecutive D events
before propagation; none may change the selected pre-stop kind or the zero.

### 18.4 Full B4 history composition

Regional physical messages are extended from actors/ports/edges to:

- exactly-once owned event records, owned by their initiator;
- validated crossing/shared event references;
- owned wire tips;
- predecessor identifiers, opaque only when their owner is outside the region.

Typed union must compose these fields to the direct full-region restriction.
The validator runs before union and rejects missing owned ports, phantom
owners, edges without required endpoint ports, inconsistent external rows,
corrupt shared edges/events and duplicate event ownership.  Only then may B4
consume the composition flag for its sufficient growing-carrier row.

### 18.5 Complete capacity and verdict typing

The B3 ledger adds neighbor birth-ordinal bits, the root carrier bit, explicit
port/edge/identifier counts and a declared reference encoding cost.  It prints
the representative values rather than only the number of ledger rows.  The
physics claim remains encoding-independent: the constructed B3 is unbounded
because its incident actor/port count has unbounded support.

Capacity status is three-way:

```text
BOUNDED_PROVED / UNBOUNDED_PROVED / UNKNOWN.
```

Paper-21 row 2 requires the first, row 3 the second.  `UNKNOWN` cannot inherit
row 3 from a default Boolean.  Each outcome predicate is calculated
independently; the first true row is selected.  Unit tests include overlapping
later predicates, so priority is tested rather than assumed.  Impossible flag
combinations may instead fail explicitly, but may not silently suppress an
earlier row.

### 18.6 Second-delta claim ceiling

The physical result remains eligible for the same ceiling only after these
gates pass:

```text
C/L B3: all-future sufficient growing carrier, POINTWISE;
        no minimal/weak predictive quotient claimed;
F C_r:  no exact realization in the declared complete finite-radius family;
F B4:   sufficient all-future growing ceiling, not necessary;
v9 and intrinsic quantum: REFUSAL/UNDEFINED at their declared widths.
```

No source claim is terminal until the repaired endpoint selector survives a
fresh interloper attack, the counter-bearing/root-covariant output kernel is
reproduced, and the full-history composition and capacity/verdict hardening
receive independent hostile deltas.

## 19. Second replacement receipt before closing review

The second replacement passes `13/13`; salts `17` and `65537` byte-match the
committed stdout.  Artifact hashes are:

```text
code SHA-256
e66490560f7c38af746b6fea144a4356dfdb3630205eab9f46723ed8c830bff8

stdout file SHA-256
3d12f6191883ee3790c78498bae4bb1971144765341a354df587d33188f54498

internal summary SHA-256
a53fa0c18a5905f282cea4c283ec3061c049ad7378a00f624906c1d68091d701
```

The exact replacement ledger is:

```text
registered strong boundary-transition classes: 111,111,111;
synthetic internal stress classes:              106,110,110;
explicit B1 stress:                             H1 equal, H2 split;
physical B3 updates:                            35,898;
root/role output-conjugacy states:               2,927;
disjoint construction swaps:                    120,276;
full typed regional compositions:               159,734;
malformed message attacks rejected:             6/6;
moving-tip ancestry interlopers:                 16/16;
finite unmarked classes at depth 3/4:            4/10.
```

The observable/internal distinction is now explicit.  Counter-bearing
non-silent marks are part of the durable C/L output.  Neighbor births are
internal `None` transitions in a strong CTMC bisimulation stress test.  The
`111` counts are not called the canonical weak/timed predictive quotient; B3
is a proved sufficient carrier and minimality remains open.

The role-labeled generator now accepts the distinguished root as an argument.
Nominal transport checks output marks, successor carriers and fresh children
on every registered state, including `A -> R` and `A/1 -> R/1`.

The Branch-F selector is now
`(remote structural role, pre-stop own-ring ordinal)`.
The event searches the future A ancestry for that exact immutable event and
the inward chain.  Four interloper families per registered radius—later remote
idle, later remote interaction, unrelated A event, and several later remote
events—leave the idle branch true and the interaction branch false.  Thus the
zero no longer follows the moving tip.

Regional composition now owns persistent events by initiator, carries crossing
event references, predecessor references and wire tips, and validates them
alongside actors, ports and shared edges.  Six malformed-message attacks cover
missing ports, phantom ownership, inconsistent external rows, corrupt shared
edges, corrupt shared event contents and duplicate event ownership.

The capacity receipt now includes root carrier, neighbor degree and birth-
ordinal integers, counters, identifier bytes and port/edge handle costs.  Its
representative values are

```text
d/root-bit/degree-bits/neighbor-birth-bits/counter-bits/id-bits/handle-bits
= 5/1/5/5/9/112/60.
```

The verdict engine uses `BOUNDED_PROVED`, `UNBOUNDED_PROVED` and `UNKNOWN`.
All eight outcome rows and six overlapping-predicate cases are exercised.  The
scientific dispositions remain those pinned in section 18.6, but this section
is not terminal until the three independent closing deltas reproduce and
accept the exact output, endpoint and full-history gates.

## 20. Terminal D34e note disposition

The three independent closing streams are unqualified clean:

```text
predictive/profinite: 0 blockers / 0 majors / 0 minors / 0 nits;
boundary/locality:    0 blockers / 0 majors / 0 minors / 0 nits;
ancestry/quantum:     0 blockers / 0 majors / 0 minors / 0 nits.
```

They independently reproduced the code/output hashes, the `13/13` gate set
and the internal summary digest.  Additional attacks extended the generator
projection through global depth five (`26,727` cumulative states), tested
fresh roots and multi-event B3 paths, checked three-region associativity,
expanded malformed messages, and ran fresh radii with later births, seven
remote idles, alternating remote interactions and unrelated inner events.  No
counterexample remained at the declared scope.

The terminal D34e result is therefore:

> **QUERY-RELATIVE ALL-FUTURE GROWING RECORD-DAG BOUNDARY FOR THE CHOSEN
> PASSIVE D34b C/L QUERIES, PLUS A COMPLETE FINITE-RADIUS NO-GO FOR FULL
> DURABLE ANCESTRY.**  The physical B3 star is a pointwise sufficient,
> recursively closed, covariant and composable carrier, but its width is
> unbounded.  The complete radius family `{C_r:r<infinity}` cannot screen full
> A-record ancestry.  The whole connected component is a sufficient growing
> ceiling; its necessity and the minimal full-ancestry frontier remain open.

This terminal noun does **not** identify B3 with the minimal predictive
quotient, compute the weak/timed quotient, find a bounded alternative, derive
the chosen D34b rulebook, prove a v9 stem-posterior factorization, construct the
timed controlled D34b-D34c process, define intrinsic quantum boundary widths,
or derive a Lorentzian light cone, proper time, spacetime dimension, `G` or the
universe click law.

The next load-bearing theoretical opening is no longer “local record or global
history.”  It is:

> Does Branch F admit an adaptive growing causal frontier—smaller than the
> literal component and not confined to any fixed actor radius—that carries
> exactly the immutable records still capable of returning to A?

A second independent opening is the canonical weak/timed predictive quotient
of the observed C/L process after internal neighbor births are eliminated.
Neither opening changes the terminal sufficient-carrier and fixed-radius
theorems proved here.

## 21. Paper-level integrity opening and frozen repair

Paper 22 round 1 preserves all four scientific theorems.  Its three hostile
streams report:

```text
predictive/profinite: 0 blockers / 0 majors / 2 minors / 1 nit;
boundary/locality:    0 blockers / 0 majors / 2 minors / 1 nit;
ancestry/quantum:     0 blockers / 0 majors / 0 minors / 0 nits.
```

One review opened a deeper validator attack that the terminal note reviews had
not tried.  The composition identity remains exact for genuine regional
projections, but the validator accepted three coordinated malformed histories:
an opaque predecessor whose encoded owner was already inside the region, a
self-cycle, and a stale visible wire tip.  Before Paper 22 is terminal, the
executable will strengthen intrinsic regional-history validation rather than
merely narrow the manuscript.

The repair is frozen as follows.

1. Parse every event identifier as `initiator#r(own-ring ordinal)` and require
   agreement with the event initiator.
2. Require an opaque predecessor's encoded initiator to lie outside the owned
   region; an internally owned predecessor must be visible.
3. Reject visible predecessor cycles and non-increasing same-initiator ring
   ordinals.
4. For every owned actor, require initiated event ordinals `1..ring`, birth
   count equal to the actor birth ordinal, visible touching-event count equal
   to its wire count, interaction parity equal to its carrier bit, and the
   stored tip to be the unique local-wire maximum whose ancestry contains
   every earlier visible event on that wire.
5. Add the three coordinated corruptions to the existing six-field battery and
   regenerate the receipt hashes.

The ancestry selector terminology is also corrected everywhere.  The event ID
`D#rk` uses D's **own-ring ordinal**, not its position on D's wire; passive
incoming events can make those ordinals differ.  The proof is unchanged
because the paired pasts share the same structural D role and own-ring ordinal.

Paper prose will then:

- remove the unproved “smallest boundary” slogan and use “a sufficient query-
  relative boundary”;
- replace “already sealed” with “persistent immutable” because the chosen law
  has no dynamic sealing;
- distinguish exact screening from minimality;
- cite the predictive-state, lumpability and operational-memory references at
  the claims they contextualize, with DOI/provenance metadata;
- state the terminal note/review commit chain explicitly.

This is an integrity and provenance hardening pass.  It does not change the
D34e theorem or outcome table.  A closing paper delta must reproduce the new
hashes and independently reject all nine malformed messages before terminal
publication status.

## 22. Paper-level integrity repair receipt

The strengthened executable remains `13/13`; the malformed-message battery is
now `9/9`.  The new frozen-candidate hashes are:

```text
code SHA-256
1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5

stdout file SHA-256
158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7

internal summary SHA-256
9f9cea1886db0c889677fdb735b8cb9fc76ae4d2ba18b501242f58331795e017
```

The extra gates reject an internally owned opaque predecessor, a self-cycle
and a stale visible tip, in addition to the six prior interface/ownership
corruptions.  Genuine regional composition remains `159,734/159,734`.
Terminology now follows the actual event identifier: Branch F pins the remote
actor's own-ring ordinal, not its wire position.  Paper 22 also removes every
minimality/sealing overstatement and adds claim-local literature/provenance.
Closing paper deltas remain required.

## 23. Paper 22 closing round and narrow repair

The closing round against exact commit `8e820cc` preserves every scientific
claim and independently reproduces the `13/13` receipt, `9/9` registered
corruption rejections, artifact hashes and typed-union identity:

```text
predictive/profinite: 0 blockers / 0 majors / 1 minor / 0 nits;
boundary/locality:    0 blockers / 0 majors / 0 minors / 0 nits;
ancestry/quantum:     0 blockers / 0 majors / 1 minor / 0 nits.
```

The two one-minor reports identify the same prose-only defect: Paper 22 copied
the wrong DOI for Shalizi--Crutchfield and the wrong issue/pages for
Geiger--Temmel.  The repaired metadata are respectively
`10.1023/A:1010388907793` and *Journal of Applied Probability* `51(4),
1114--1132 (2014)`.  Neither source is a proof dependency.

The extended locality attack also fixes the exact validator ceiling.  It
rejected the three registered openings and every additional violation of a
claimed invariant, while fresh associativity checks passed.  But coordinated
fork/rejoin histories, untouched-wire predecessors and phantom/non-neighbor
targets can satisfy those interface invariants without being generated by
the D34b transition law.  Therefore:

> the validator checks the declared ownership, interface, DAG, counter and tip
> invariants used by typed composition of genuine regional projections; it is
> not a complete D34b reachability recognizer.

This ceiling changes no D34e theorem.  A narrow final delta must now verify the
two bibliography substitutions, the validator-scope sentence and candidate
Paper 22 SHA-256
`e33c0ad9294ff1411f49e7d32dc640c9047d3a7603e954219703f23031bf8576`
before the paper status becomes terminal.

## 24. Narrow delta and final hygiene repair

The narrow delta against `a074608` verifies the candidate Paper 22 SHA, both
bibliography corrections and the validator-ceiling sentence.  Its dispositions
are:

```text
predictive/profinite: 0 blockers / 0 majors / 0 minors / 1 nit;
boundary/locality:    0 blockers / 0 majors / 0 minors / 0 nits;
ancestry/quantum:     0 blockers / 0 majors / 0 minors / 0 nits.
```

The sole nit is outside the paper: two Markdown hard-break spaces in the
committed round-2 predictive review made the commit-range `git diff --check`
fail.  They are removed without changing the review's words or verdict.  Paper
22 remains byte-identical at SHA-256
`e33c0ad9294ff1411f49e7d32dc640c9047d3a7603e954219703f23031bf8576`.
A final string/hygiene delta is required before terminal status.

## 25. String/hygiene closure and terminal-status candidate

The three final string streams against `4a764f9` are all clean:

```text
predictive/profinite: 0 blockers / 0 majors / 0 minors / 0 nits;
boundary/locality:    0 blockers / 0 majors / 0 minors / 0 nits;
ancestry/quantum:     0 blockers / 0 majors / 0 minors / 0 nits.
```

They verify a clean commit-range whitespace audit and unchanged scientific
Paper 22 SHA `e33c0ad9...8576`.  The only remaining publication mutation sets
the paper status to terminal and replaces “candidate terminal executable” by
“terminal executable.”  The resulting candidate terminal Paper 22 SHA-256 is

```text
ed0d4646748901044b4d0e2f2849986372ec2bcab2c14bccf10fc184629cf6c4
```

No theorem, receipt, citation, scope or executable changed.  One exact
status-string delta must reproduce this hash before terminal archival.

## 26. Terminal Paper 22 archival

The three independent status-only deltas against `aee572f` are unqualified
clean:

```text
predictive/profinite: 0 blockers / 0 majors / 0 minors / 0 nits;
boundary/locality:    0 blockers / 0 majors / 0 minors / 0 nits;
ancestry/quantum:     0 blockers / 0 majors / 0 minors / 0 nits.
```

They reproduce final Paper 22 SHA-256
`ed0d4646748901044b4d0e2f2849986372ec2bcab2c14bccf10fc184629cf6c4`,
verify the exact two-string publication delta and find no scientific or
artifact drift.  A fresh salt-`999983` execution independently remains
byte-identical to the committed output:

```text
code SHA-256
1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5

stdout SHA-256
158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7

internal summary SHA-256
9f9cea1886db0c889677fdb735b8cb9fc76ae4d2ba18b501242f58331795e017
```

The terminal D34e/Paper 22 result is therefore unchanged from section 20:

> For the chosen passive D34b law, a distributed radius-one typed star is an
> exact all-future growing carrier for the declared coarse and role-labeled A
> futures.  It is unbounded in width.  No complete fixed actor radius carries
> full durable A ancestry.  The complete connected component is sufficient,
> but neither necessary nor minimal by any proved theorem.

The validator checks the enumerated composition invariants of genuine
regional projections; it is not a generative-reachability recognizer.  The
chosen D34b law remains an input, and the v9 posterior, controlled quantum and
spacetime branches remain open/refused at their declared scopes.

The direct next investigation is the adaptive full-ancestry causal frontier:
construct or exclude a recursively updated carrier smaller than the complete
component but not confined to any fixed actor radius.  The canonical
weak/timed predictive quotient is a separate second target.
