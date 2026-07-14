# Relativistic ISP v10 paper 22

# The predictive record-DAG boundary of a chosen click law

## Exact distributed sufficiency, unbounded width and a fixed-radius ancestry no-go

**Status:** terminal accepted after independent scientific, narrow-repair and
string/hygiene deltas.
**Date:** 2026-07-13.

## Abstract

Paper 21 left a precise question: the chosen D34b click law is strong Markov on
its complete global configuration and its generator reads only an actor's
incident star, but does the future of one actor admit a record-carried
predictive boundary smaller than the global state?  We answer that question
for two passive local-wire queries and prove a complementary obstruction for
full durable ancestry.

For the coarse future A-wire process, the behavioral state consists of A's
carrier and counters together with the histogram of the current degrees of
A's neighbors.  A physical realization is not a histogram secretly stored in
A.  It is a distributed radius-one typed star: A owns its carrier, counters
and endpoint ports; each incident actor owns its current eligible degree and
birth ordinal; shared edges carry the typed incidence.  We derive the exact
closed generator, implement its record-native updater, prove construction-
order and nominal-name covariance, and prove typed regional composition.  The
same object predicts the role-labeled A-wire query.  It is an all-future,
pointwise sufficient carrier for the chosen passive law at fixed construction
time and A-own/A-wire count stops.

The result is local in actor-graph read/write scope but not bounded in memory.
A births at rate `1/4`, so the incident star has unbounded port and identifier
support at every positive time and grows without bound along an infinite run.
The one-record candidate fails by the exact `1/4 -> 1/8` incoming-rate witness.
Even retaining A's degree and its complete current incoming rate fails: the
reachable neighbor-degree multisets `{2,3,6}` and `{2,4,4}` have the same
current rate `1/4` but different rate derivatives, `61/1344` and `11/240`.

For the enlarged query that retains the complete durable ancestry of future A
records, every complete fixed actor radius fails.  For each finite `r`, two
positive-cylinder pasts have the same complete radius-`r` carrier but differ
in one immutable event at distance `r+1`.  A common inward interaction
subcylinder brings that exact pre-stop event, selected by structural actor role
and own-ring ordinal, into A's future ancestry.  Its conditional probability
is at least

```text
p_r = [1/(8(r+3))]^(r+1) > 0
```

in the idle past and zero in the interaction past.  Later remote events do not
alter the selected ordinal.  The whole connected component is sufficient, but
its necessity and the minimal adaptive ancestry frontier remain open.

The theorem is deliberately narrow.  It does not derive D34b, compute the
canonical weak/timed predictive quotient, prove a bounded boundary, connect
the online state to the v9 profinite stem spectrum, construct the missing
timed controlled D34b-D34c quantum process, or derive spacetime cones,
dimension, proper time, `G` or the universe click law.

## 1. What is proved

Let `mu_D34b` be the chosen static-adjacency D34b history law.  The paper proves
four statements.

1. **Coarse and role-labeled sufficiency.**  A distributed typed star `B3_A`
   screens the declared passive C/L future of A and updates recursively.
2. **Unbounded physical width.**  The constructed `B3_A` has no uniform
   capacity bound, despite graph radius one.
3. **Full-ancestry fixed-radius no-go.**  No complete finite-radius carrier
   `C_r` in the declared class screens Branch F.
4. **Component ceiling.**  A's complete connected-component configuration is
   sufficient for Branch F, while disconnected factors are irrelevant at the
   licensed continuous-time and component-local stopping scopes.

The first statement is a sufficient-carrier theorem, not a minimality theorem.
The behavioral predictive quotient, a physical carrier of that quotient and
the complete history remain distinct objects.  This law/query-relative
predictive-state distinction is the computational-mechanics one [3]; the
record-native carrier theorem is the D34e-specific question.

## 2. Frozen law and query scopes

### 2.1 The chosen D34b law

Every active unsealed actor has an independent rate-one Poisson clock.  At its
ring an actor `y` chooses

```text
birth                              probability 1/4,
interaction with each neighbor x  probability 1/(4 degree(y)),
idle                               probability 1/2.
```

Birth creates a fresh Ulam child joined only to its parent.  Interaction
appends one shared event to the initiator and receiver wires and toggles the
modeled carrier bit on both.  Idle appends one event only to the initiator.
Actor rows, adjacency, wire tips, predecessor references and event records
persist.  This chosen exemplar has no dynamic sealing and never joins two
previously disconnected components.

These coefficients and grammar are inputs.  D34e characterizes their
predictive carriers; it does not derive them from sealed records, diamonds,
No Silent Erasure or the history-action family.

### 2.2 Three passive queries

Branch C retains every future event touching A with

```text
elapsed time from the conditioning stop,
kind/direction,
post-event A carrier,
post-event A-own-ring count,
post-event A-wire-event count.
```

Branch L also retains the incident actor role, modulo nominal relabeling of
the typed star.  Branch F retains the complete event contents and transitive
predecessor ancestry of every future event touching A.

No intervention law is inferred from the passive measure.  The intrinsic
quantum branch therefore requires a separate timed controlled process and
all-instrument kernels.

### 2.3 Stopping and time convention

The licensed scopes are fixed construction time, A-own-ring hitting times and
A-wire-event hitting times.  Future times are elapsed from the conditioning
stop; a common time translation is gauge.  A passive incoming event advances
A's wire count but not A's own-ring count.

Fixed global event depth is used only for finite enumeration.  It is not a
regional stopping rule: adding a disconnected component changes the global
event race without changing A's continuous-time component law.

## 3. Candidate boundaries

The candidates form a strict conceptual ladder.

```text
B0  A's private actor row and tip;
B1  A carrier, A degree and aggregate current incoming rate;
B2  A carrier/counters and histogram of neighbor degrees;
B3  physical distributed typed incident star;
B4  complete current configuration of A's connected component.
```

`B2` is behavioral.  `B3` is physical and distributed.  In `B3`, A owns its
carrier, ring/birth/wire counters and A-side endpoint ports.  Each incident
actor owns its degree and birth ordinal.  One typed edge joins the two endpoint
ports.  Nominal actor names are construction labels; the distinguished root
role and Ulam child relation transport under gauge.

An analyst may read the entire star.  A does not privately store its
neighbors' rows, and the reference Python program is not a simulation by
independent operating-system actors.  The claim concerns the factorization of
the ideal probability law and record ownership, not hardware architecture.

## 4. The exact closed boundary generator

Write A's carrier as `c`, its own and wire counts as `r_A,w_A`, and

```text
h = (n_1,n_2,...),
n_k = number of current A-neighbors having degree k,
d_A = sum_k n_k.
```

The projected continuous-time generator has five row families.

```text
A birth, rate 1/4:
    add one degree-1 neighbor;
    (r_A,w_A) -> (r_A+1,w_A+1);
    emit A-birth.

A idle, rate 1/2:
    histogram unchanged;
    (r_A,w_A) -> (r_A+1,w_A+1);
    emit A-idle.

A outgoing interaction, aggregate rate 1/4:
    c -> 1-c;
    (r_A,w_A) -> (r_A+1,w_A+1);
    emit A-outgoing.

birth of a degree-k neighbor, aggregate rate n_k/4:
    n_k -> n_k-1, n_(k+1) -> n_(k+1)+1;
    counters unchanged;
    emit no A-wire record.

degree-k neighbor interacts into A, aggregate rate n_k/(4k):
    c -> 1-c;
    (r_A,w_A) -> (r_A,w_A+1);
    emit incoming-to-A.
```

Every other law row leaves this state and the C output unchanged.  For Branch
L the same partition retains the initiating/receiving incident role.

### Theorem 1 — all-future B3 sufficiency

For every legal finite D34b configuration, the conditional law of the
declared passive Branch C or L future depends on the complete past only
through `B3_A`.  `B3_A` has a recursive event/time update, is covariant under
nominal relabeling and swaps of disjoint incomparable record-DAG updates, and
composes by validated typed union.  The theorem is pointwise on the declared
generator domain.

### Proof sketch

The five row families above exhaust every transition capable of changing the
carrier or licensed output.  Their rates and successor fields are functions
of `B3_A`.  Births, interactions and idles outside the star either leave B3
unchanged or flow elapsed time only.  Thus the complete generator factors
through B3.

The relevant jump intensity obeys

```text
q(c,h) = 1 + d_A/4 + sum_k n_k/(4k) <= 1 + d_A/2.
```

A's incident count grows through its rate-`1/4` birth process.  The parent
D34b nonexplosion theorem therefore gives a unique nonexplosive projected
pure-jump process.  The monotone own/wire counters define hitting times of
that process, so the strong-Markov result extends from fixed time to the two
local count stops.

The use of a closed strong boundary refinement rather than an automatically
minimal observed process follows the standard distinction between Markov
lumpability and weaker law-relative aggregations [4].

The physical updater consumes only old B3, an elapsed increment and one typed
root/passive/silent event.  Nominal transport conjugates output marks,
successor fields and fresh children.  Disjoint write supports commute.
Regional messages give every actor row, endpoint port, event record and wire
tip exactly one owner.  The validator checks both shared interface content and
intrinsic owned-history integrity: event ownership/ordinals, internal
predecessor visibility, acyclicity, counter/history agreement and maximal wire
tips.  Shared edges, crossing events and genuinely external opaque predecessor
references are validated before union.  These facts establish recursive
closure, covariance and composition rather than merely one-step rate fitting.

## 5. Why smaller summaries fail

### Proposition 1 — one actor record is insufficient

Initially B has only A as a neighbor, so

```text
rate(B -> A) = 1/4.
```

After B births a child, A's private row and tip are unchanged while B has
degree two, giving

```text
rate(B -> A) = 1/8.
```

Thus B0 does not screen even A's next wire event.

### Proposition 2 — the current rate is not a recursive state

Consider reachable degree multisets

```text
H  = {2,3,6},
H' = {2,4,4}.
```

Both have three neighbors and

```text
sum_(k in H) 1/k = sum_(k in H') 1/k = 1,
```

so both give aggregate incoming rate `f=1/4`.  But

```text
L f = 1/16 - sum_k n_k/[16 k(k+1)]
```

gives

```text
L f(H)  = 61/1344,
L f(H') = 11/240,
gap      = 1/2240.
```

The expected incoming count differs at order `t^2` by coefficient `1/4480`.
The exact internal-transition stress test likewise places the pair together at
one horizon and separates it at two.  B1 knows the current hazard but not how
that hazard will change.

## 6. Radius one is not bounded memory

### Theorem 2 — B3 has unbounded width

A's birth rings are a rate-`1/4` thinning of its rate-one Poisson clock.  Hence
at every `T>0`, A's incident count has unbounded support, and over an infinite
realization it diverges almost surely.  B3 therefore has unbounded actor-row,
port, edge, identifier and integer support.

The exact capacity ledger separately reports graph radius, row/port/edge
counts, carrier and integer bits, nominal identifier cost, handle cost and one
ideal relative-time coordinate.  This proves that the constructed B3 is
growing.  It does not exclude a different bounded physical realization of the
same behavioral quotient.

This distinction matters: “local” here means radius-one read scope and bounded
touched/write support per event.  It does not mean bounded degree, finite
memory, Lorentz locality or a spacetime light cone.

## 7. Full ancestry defeats every complete fixed radius

Branch F asks more than the event kind and post-carrier.  It inspects all
durable predecessor records that a future A event inherits.

For radius `r`, define `C_r` as the complete record-native restriction owned by
actors in the closed graph ball of radius `r` around A:

- full actor rows, tips, wire counts and endpoint ports;
- every complete event touching an owned wire, including crossing events;
- complete predecessor identifiers, opaque when the referenced event is
  outside the ball.

An opaque outside identifier may not be recursively dereferenced; otherwise
the object is no longer a radius-`r` carrier.

### Theorem 3 — no exact Branch-F realization in `{C_r:r<infinity}`

For every finite `r`, there are two reachable positive-cylinder pasts with
identical `C_r` and different conditional Branch-F future laws.

### Construction and proof

Grow a chain from A to an actor D at distance `r+1`, and give D a leaf E.  The
two pasts differ only in D's next event:

```text
h_idle:        D idles,
h_interaction: D interacts with E.
```

The differing event touches only D or D/E, outside the owned radius ball, so
the complete `C_r` values agree.  The two events have the same structural D
role and the same D-own-ring ordinal `k`; only their immutable kind differs.

Now require the `r+1` child-to-parent interactions that propagate D's wire
ancestry inward to A.  There are `r+3` active component actors and each
selected initiator has degree two, so the exact embedded subcylinder mass is

```text
p_r = [1/(8(r+3))]^(r+1).
```

Define one common future event `E_r`:

> A's future record contains the selected inward chain, and its ancestry
> contains the exact pre-stop D event at ordinal `k`, whose kind is idle.

Then

```text
P(E_r | h_idle)        >= p_r > 0,
P(E_r | h_interaction)  = 0.
```

The zero is not a moving-tip assertion.  Later D idles, interactions or births
can change D's current tip, but cannot change the persistent immutable event at
ordinal `k`.  The executable attacks later idles, later interactions,
unrelated events and several later D events; independent review extends those
attacks to fresh radii and longer interloper sequences.

For `Delta=1`, multiplying by the Erlang completion factor for the first
`r+1` component rings gives positive timed subcylinder lower bounds.  These are
not asserted to be total `E_r` probabilities.

The theorem excludes every member of the declared complete fixed-radius
family.  It does not exclude an adaptive, non-radius frontier.

## 8. The whole component is sufficient, not necessary

### Theorem 4 — component ceiling

The complete current D34b configuration of A's connected component is an
all-future sufficient growing carrier for C, L and F at continuous
construction time and component-local stops.

Every law event remains inside its current connected component: birth attaches
inside, interaction follows an existing edge and idle touches one actor.  The
independent Poisson construction therefore factors over disconnected
components.  Adding a disconnected `P--Q` component does not change A's
component law, although it does change fixed-global-depth race shares.

The typed regional algebra composes actor rows, ports, edges, persistent event
records, crossing references, predecessor references and tips into the direct
component restriction.  This certifies B4 as a physical sufficient carrier.
No theorem proves that all of B4 is necessary.

The principal open between Theorems 3 and 4 is an adaptive growing causal
frontier: perhaps live wire tips plus exactly the immutable records still able
to return to A.  Such a frontier could be smaller than the component while
escaping every fixed actor radius.

## 9. Exact receipt and hostile review

The terminal executable is
`v10/code/d34e_predictive_boundary_exact.py`.  Its standard-library receipt
passes `13/13` with:

```text
reachable levels through global depth four  1,6,40,304,2576;
cumulative reachable states                 2,927;
registered strong classes                   111,111,111;
physical B3 row updates                      35,898;
root/role output conjugacy states            2,927;
disjoint construction swaps                 120,276;
full typed regional compositions             159,734;
malformed messages rejected                  9/9;
moving-tip interloper attacks                16/16;
unmarked classes at depth three/four         4/10.
```

The artifact hashes are:

```text
code
1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5

stdout
158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7

internal summary
9f9cea1886db0c889677fdb735b8cb9fc76ae4d2ba18b501242f58331795e017
```

Three hostile rounds were required.  Round 1 exposed missing time/counter
scope, a non-predictive raw-successor signature, absent physical B3 updates,
conflated covariance, under-typed radius carriers and a hard-coded scorecard.
Round 2 found omitted counter outputs, root-name dependence and a moving-tip
error in the ancestry event.  The second replacement pins the pre-stop
ordinal, carries counter-bearing marks, parameterizes root transport, composes
full event history, validates malformed messages and types capacity as
bounded-proved, unbounded-proved or unknown.  All three closing streams return
`0 blockers / 0 majors / 0 minors / 0 nits` at the declared ceiling.

The terminal D34e note and three clean closing reviews are frozen at commit
`d10ca52`; the second repaired executable/output were frozen at `6e6676b`.
Paper-level review then opened three additional record-DAG corruptions.  The
validator now also rejects internally owned opaque predecessors, predecessor
cycles and stale wire tips while cross-checking actor ring/birth/wire counters,
carrier parity and local-wire maximality.  The closing scientific delta
reproduced all nine attacks and the revised hashes.  The validator certifies
these declared invariants on the composition interface; it is not a complete
recognizer for whether an arbitrary fabricated history is reachable under
D34b.  The composition theorem is the typed-union identity on genuine
regional projections.

## 10. Strong boundary refinement is not the minimal predictive quotient

The finite class census uses a strong boundary-transition bisimulation.  Every
non-silent mark contains the declared post-event carrier and counters.  A
neighbor birth is represented as an internal transition, not an observable
A-wire record.

This strong state is sufficient but may retain more information than the
observed A-wire process requires.  Eliminating arbitrarily many hidden
neighbor births to compute the canonical weak/timed predictive quotient is a
different problem.  The class counts `111,111,111` are therefore not presented
as a minimal causal-state count.

## 11. Profinite and quantum ceilings

### 11.1 Finite mark forgetting

At finite depth the marked law pushes forward to unmarked causal orders and
obeys the exact diagram

```text
(u_3 o r_(4->3))_* mu_4 = (u_3)_* mu_3,
```

where the committed labeled prefix is truncated before marks are forgotten.
There is no canonical unmarked `4 -> 3` map inferred from this receipt.

A current online past also does not select one completed v9 stem-spectrum
point.  The candidate datum would be a posterior measure over completed
points.  D34e constructs neither that completed-history pushforward nor a
proof that its posterior screens C, L or F.  Profinite structure hosts
compatible finite data; it does not select the growth law or boundary.

### 11.2 Intrinsic quantum branch

The accepted finite D34c strongly-positive typed-DAG functional remains a
valid finite result and is hash-pinned by the receipt.  It is not a timed
controlled D34b-D34c process.  Without intervention-indexed kernels
`P(r|I,h)`, D34e cannot define the intrinsic operational predictive boundary
or assign SHARD `d_carrier`, `d_op` or `chi_cut`.  The correct verdict is
`REFUSAL/UNDEFINED`, not a classical approximation to a missing quantum law.
The operational criterion being reserved here is the intervention-indexed
quantum Markov condition of the process-tensor framework [5].

## 12. Outcome table

| Branch | Terminal result |
|---|---|
| C coarse A-wire / physical B3 | `ALL-FUTURE GROWING-CARRIER PASS / POINTWISE` |
| L role-labeled A-wire / physical B3 | `ALL-FUTURE GROWING-CARRIER PASS / POINTWISE` |
| F full ancestry / complete finite-radius family | `NO EXACT REALIZATION IN THE DECLARED CARRIER CLASS` |
| F full ancestry / whole component | `ALL-FUTURE GROWING-CARRIER PASS / POINTWISE`, sufficient only |
| v9 completed-stem posterior factor | `REFUSAL/UNDEFINED` beyond the finite diagram |
| intrinsic timed quantum boundary | `REFUSAL/UNDEFINED` |

Predictive omission deletes nothing physically, so No Silent Erasure is not
the gate being tested.  The persistent records remain in the global history.

## 13. What this changes in the SHARD program

The result replaces a false dichotomy.

```text
one record                         too small;
fixed-radius full-ancestry collar  too small;
global universe state              unnecessarily large for C/L and for
                                   disconnected factors;
distributed active star            exact all-future screening for the chosen
                                   C/L law;
whole component                     sufficient ceiling for F;
minimal adaptive F frontier         open.
```

It also clarifies the sense in which observable non-Markovianity can coexist
with local generation.  The complete law is Markov on its current
configuration.  A distributed boundary can Markovize a selected regional
query.  A smaller record projection displays memory because it omits boundary
variables.  None of these statements implies that a single record is a CPU
thread or that the universe has a global physical commit clock.

The theorem is relevant to later cone and dimension work only as a gate.  Any
future interactive law used to grow causal webs must first establish its own
predictive carrier and then re-run the v9 cone, scale and dimension diagnostics.
D34e does not show that the chosen D34b law produces round cones or 3+1
spacetime.

## 14. Open problems

The next investigations are sharply separated.

1. **Adaptive full-ancestry frontier.**  Construct or exclude a recursively
   closed growing frontier between every `C_r` and B4.
2. **Weak/timed predictive quotient.**  Eliminate internal neighbor births and
   characterize the minimal observed C/L causal state.
3. **Bounded alternative.**  Determine whether a different record-native
   physical realization compresses B3 to uniform capacity.
4. **Profinite bridge.**  Construct the completed marked-to-causet map,
   adapted posterior and an actual screening factorization.
5. **Controlled quantum lift.**  Build the timed D34b-D34c intervention family
   before asking for quantum memory widths.
6. **Law selection and geometry.**  Derive or empirically identify the real
   interactive history law, then test its cones, dimension, clock conversion
   and gravitational scale.

The first is the direct successor to D34e.  It asks what information can still
cross the causal boundary, not what one actor privately remembers.

## 15. Conclusion

For the chosen passive D34b law, locality and memory meet in a precise middle
object.  The future of A's coarse or role-labeled wire is screened by a
distributed incident record-DAG star.  That star updates locally, respects the
construction gauge and composes, but it grows without a uniform bound.  Full
durable ancestry is stricter: every complete fixed actor radius misses an
immutable record that can later return, while the connected component remains
a sufficient ceiling.

The correct endpoint is therefore neither “one record is Markov” nor “the
machine must know the whole universe.”  It is query-relative:

> prediction can live on a sufficient query-relative causal boundary carrying
> the history still capable of changing the licensed future.

D34e constructs one such boundary for C/L and proves that no fixed-radius
version can do the same for F.  Finding the minimal adaptive full-ancestry
frontier is the next problem.

## References

1. Relativistic ISP v10 Paper 21, *Local generators do not imply local
   memory*.
2. D34e terminal note, `note-d34e-predictive-record-dag-boundary.md`.
3. C. R. Shalizi and J. P. Crutchfield, *Computational Mechanics: Pattern and
   Prediction, Structure and Simplicity*, Journal of Statistical Physics 104,
   817–879 (2001), DOI `10.1023/A:1010388907793`.  Background for predictive
   equivalence/minimal causal states; no SHARD record-locality result is
   attributed to it.
4. B. Geiger and C. Temmel, *Lumpings of Markov Chains, Entropy Rate
   Preservation, and Higher-Order Lumpability*, Journal of Applied Probability
   51(4), 1114–1132 (2014), DOI `10.1239/jap/1421763331`.  Background for
   strong versus weaker/law-relative lumpability.
5. F. A. Pollock et al., *Operational Markov Condition for Quantum Processes*,
   Physical Review Letters 120, 040405 (2018), DOI
   `10.1103/PhysRevLett.120.040405`.  Background for the intervention-indexed
   operational quantum-memory criterion; no timed D34b-D34c lift is attributed
   to it.
