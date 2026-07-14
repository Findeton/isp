# Paper 22 round 2 — boundary/locality closing hostile delta

**Frozen target:** commit
`8e820cc2464eeefeabafe49ed64246e98d51ce4a`.

**Comparison base:** Paper 22 at `a34b36e` and
`paper22-round1-boundary-locality-hostile-review.md`.

**Exact verdict:** **DELTA CLEAN AND TERMINAL FOR THE BOUNDARY/LOCALITY
STREAM — 0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

The strengthened validator closes the round-1 full-history interface opening.
It independently rejects the internally owned opaque predecessor, self-cycle
and stale-tip witnesses, while all `159,734` genuine regional compositions
remain exact.  A broader coordinated campaign rejects every violation of an
invariant that the repaired manuscript actually claims.  The validator is not
a complete D34b reachability or exact transition-law recognizer; four
deliberately fabricated but acyclic/counter-consistent histories demonstrate
that ceiling.  This is not a remaining finding because the manuscript now
enumerates the checked integrity invariants and bases its composition theorem
on genuine regional projections.

The other round-1 findings are also closed.  The conclusion no longer claims a
smallest boundary, and the ancestry event is called persistent/immutable and
selected by its own-ring ordinal.  The actor-graph locality, unbounded-memory,
hardware, construction-time, Lorentz/proper-time and B4 scopes remain exact.

## 1. Frozen artifacts and fresh reproduction

The candidate artifacts independently hash as:

```text
paper   1718dce460c5d1711fa3b02fe8424c9a5b4819abb8b9facd0d64abbff14b92ee
note    af3c9b6fdf7590c6a28db93f0e473691b30c00ae921440156a7e48e8cb19a98c
code    1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5
stdout  158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7
```

Fresh runs under `PYTHONHASHSEED=271828` and `104729` exit zero and produce
stdout with the committed hash.  Both reproduce the internal summary digest

```text
9f9cea1886db0c889677fdb735b8cb9fc76ae4d2ba18b501242f58331795e017.
```

The exact candidate ledger remains:

```text
gates                                  13/13
reachable levels                      1,6,40,304,2576
registered states                     2927
registered strong classes             111,111,111
physical B3 row updates               35898
root/role conjugacy states            2927
disjoint construction swaps           120276
genuine regional compositions         159734
frozen malformed messages             9/9 rejected
ancestry interlopers                   16/16
```

The changed validator does not alter any boundary generator, B3 updater,
capacity result, fixed-radius witness, component product theorem or outcome
row.

## 2. Round-1 finding disposition

### m1 — full-history validator was only interface-consistent: CLOSED AT THE NEW DECLARED INVARIANTS

The repaired validator now checks:

1. canonical `initiator#r(own-ring ordinal)` event identifiers;
2. agreement between event-ID owner and event initiator;
3. visibility of every predecessor owned inside the region;
4. strict same-initiator predecessor ordinals;
5. acyclicity of the visible predecessor graph;
6. complete initiated ordinals `1..ring` for each owned actor;
7. birth, wire and carrier-parity agreement with visible history;
8. degree agreement with owned endpoint ports;
9. event kind/target/touched tuple schema;
10. maximal owned wire tips whose visible ancestry contains every event on that
    wire; and
11. the earlier edge, port, external-row, crossing-reference and shared-content
    interface invariants.

The paper names these checks rather than using the unqualified phrase “a fully
valid history.”

#### The three exact round-1 witnesses

All three now fail closed:

```text
internally owned opaque B#r99
    -> ValueError: internally owned predecessor is opaque

self predecessor B#r1 -> B#r1
    -> ValueError: same-initiator predecessor is not earlier

older visible A#r1 substituted for current A#r2 tip
    -> ValueError: stored wire tip is not maximal on owned wire
```

The repairs are semantic.  They do not merely add the three specimens to a
deny-list.

#### Expanded coordinated corruption campaign

I ran 24 fabricated message/composition probes.  Twenty violated a named
invariant and were rejected; four were deliberately constructed beyond the
claimed verifier scope and are discussed separately below.

The rejected campaign covered:

| Attack | Independent result |
|---|---|
| internally owned opaque predecessor | rejected |
| self predecessor | rejected |
| stale visible tip | rejected |
| event-ID owner differs from initiator | rejected |
| noncanonical leading-zero ordinal | rejected |
| gap in owned initiator ordinals | rejected |
| incorrect ring counter | rejected |
| incorrect birth counter | rejected |
| incorrect wire counter | rejected |
| incorrect carrier parity | rejected |
| degree/owned-port mismatch | rejected |
| port peer/edge disagreement | rejected |
| reference no longer crossing the region | rejected |
| crossing-event ID owner mismatch | rejected |
| mutually well-typed but inconsistent shared-event copies | rejected on union |
| two-actor visible predecessor cycle | rejected |
| two incomparable local-wire maxima | rejected |
| idle event with a target | rejected |
| reversed interaction touched tuple | rejected |
| unknown event kind | rejected |

Several attacks coordinated multiple fields so that a single redundant check
could not catch them.  In particular, the shared-event mismatch changed event
kind and the affected actor carrier together, allowing the regional copy to
pass its own counter/parity checks; composition still rejected its disagreement
with the initiator-owned copy.

#### Genuine projection and associativity regression

The frozen receipt reconstructs every valid message from a legal enumerated
D34b state and verifies

```text
compose(M_R, M_S) = M_(R union S)
```

in both orders on all `159,734` registered disjoint region pairs.  The stronger
validator accepts all of them.

I additionally selected event-bearing states with at least three actors and
tested

```text
(M_A union M_B) union M_C
    = M_A union (M_B union M_C)
    = M_(A union B union C)
```

on `53` fresh singleton triples.  Every parenthesization and direct projection
agrees exactly, including event promotion from crossing reference to initiator
ownership and recomputation of opaque predecessor references.

**Disposition:** **CLOSED.**

### m2 — “smallest causal boundary” asserted unproved minimality: CLOSED

The concluding statement now says:

> prediction can live on a sufficient query-relative causal boundary carrying
> the history still capable of changing the licensed future.

The program table likewise says “exact all-future screening,” not “exactly
sufficient” in a way that could suggest minimality.  B3 remains sufficient but
not proved minimal; the weak/timed C/L quotient, a bounded alternative and the
minimal adaptive F frontier remain open.

**Disposition:** **CLOSED.**

### n1 — “sealed event” in a no-dynamic-sealing model: CLOSED

The ancestry proof now says “persistent immutable event.”  The selector is
also correctly described everywhere as the remote actor's **own-ring ordinal**,
not its wire position.  Passive incoming events can distinguish those two
counts, so this terminology repair is substantive and correct.

**Disposition:** **CLOSED.**

## 3. Validator ceiling — independently demonstrated and not overclaimed

The strengthened function recognizes the listed interface and owned-history
invariants.  It does not replay the chosen click law or decide whether an
arbitrary serialized message is reachable from the seed.  Four coordinated
messages demonstrate the distinction:

```text
an A-wire fork that later rejoins at one maximal tip;
an acyclic predecessor imported from an event's untouched wire;
an interaction with a target absent from graph/ports/references;
a birth whose target is absent from the Ulam graph/interface.
```

Each message was adjusted so that event-ID ownership, ordinals, counters,
carrier parity, visible acyclicity and unique tip maximality all agree.  Each is
accepted.  None is generated by `d34b_step`:

- exact D34b wire semantics requires each new event to inherit the immediately
  previous tip of every touched wire;
- an interaction target must be an existing eligible neighbor; and
- a birth target must be the fresh Ulam child with its new actor row and edge.

These pass-throughs would be findings if the paper claimed authentication,
generative reachability, exact predecessor reconstruction or a complete D34b
history decision procedure.  It does not.  The revised proof paragraph lists
the enforced invariants, while the arbitrary-region theorem continues to take
messages produced by `region_message` from a **legal finite D34b
configuration**.  Typed set union on those genuine projections is exact.

This ceiling should remain attached to any future reuse of the validator:

> it is an interface/intrinsic-invariant checker used as defense in depth, not
> the source of the click-law theorem and not a replacement for lawful message
> construction.

No additional repair is required for Paper 22's present wording.

## 4. Actor-graph locality, memory and hardware scope

The repaired manuscript remains disciplined about “local.”  It means:

- graph radius one for B3 reads;
- bounded touched/write support for each event; and
- distributed ownership of root rows, neighbor rows, endpoint ports and shared
  edges.

It does not mean bounded fan-in or bounded memory.  A's rate-`1/4` births give
its incident count unbounded support at every positive construction time and
almost-sure divergence over an infinite run.  Paper 22 therefore retains the
correct result:

```text
constructed B3 = ALL-FUTURE GROWING-CARRIER PASS,
bounded alternative/minimality = OPEN.
```

Nor is B3 an extra centralized subsystem carried alongside A.  A owns only its
row and endpoint ports; neighbor degree/birth rows remain neighbor-owned.  A
silent neighbor birth changes that neighbor-owned portion without writing A.
An analyst can read the star, but A does not privately maintain the histogram.

The Python receipt is explicitly not an operating-system actor simulation or a
hardware-architecture proof.  Its serial schedule represents an ideal law in
which disjoint writes commute.  The text also avoids the converse overclaim:
it does not infer that an actual simulator must inspect the whole universe.

## 5. Construction time, local stops and relativity ceiling

The time vocabulary is unchanged and exact:

- D34b uses a common ideal construction parameter for independent rate-one
  Poisson clocks;
- future query times are elapsed from the conditioning stop;
- common time translation is gauge;
- A-own and A-wire counts are distinct monotone stopping coordinates; and
- fixed global event depth is only an enumeration/locality-negative control.

The inherited nonexplosive strong-Markov theorem licenses fixed finite time and
the two local count-hitting stops.  Adding a disconnected component changes the
global event-depth race but not A's continuous component law.

The manuscript never calls construction time Einstein proper time, never
claims Lorentz covariance from construction-order covariance, and never turns
actor-graph radius into a spacetime light cone.  It explicitly refuses proper
time, Lorentz locality, cone roundness, 3+1 dimension, `G` and the universe
click law.  No correction is needed.

## 6. Full-history B4 and outcome-table scope

B4 means the complete current connected-component configuration, including
actors/counters/carriers, adjacency, persistent events, predecessor IDs and
wire tips.  It is recursively sufficient because the chosen law never joins
components and independent component Poisson sources factor at continuous
construction time and component/A-local stops.

The strengthened history checks improve defensive validation but do not supply
the B4 theorem: lawful D34b generation plus the product theorem do.  Thus the
accepted pass-throughs in section 3 do not alter B4 sufficiency.

The outcome table remains exactly scoped:

```text
C/L physical B3             ALL-FUTURE GROWING-CARRIER PASS / POINTWISE
F complete finite radii     NO EXACT REALIZATION IN DECLARED CARRIER CLASS
F whole component B4        ALL-FUTURE GROWING-CARRIER PASS, sufficient only
v9 posterior bridge         REFUSAL/UNDEFINED beyond finite diagram
intrinsic timed quantum     REFUSAL/UNDEFINED
```

Nothing says that B4 is necessary, that every bounded F carrier fails, that a
classical B3 is a quantum boundary, or that the chosen D34b law is derived.

## 7. Closing disposition

This stream accepts the following paper-level endpoint:

> For the chosen passive D34b law, the distributed unbounded B3 star is an
> exact all-future sufficient carrier for C/L at fixed-time and local count
> stops.  Every complete fixed actor radius fails the declared full-ancestry
> query, while the complete component is a sufficient growing ceiling.  The
> strengthened regional validator enforces the listed interface and
> owned-history invariants on composable messages; it is not a complete
> click-law reachability recognizer.  None of these actor-graph probability-law
> results establishes bounded hardware, Lorentz locality, proper time or a
> universe law.

**Final count: 0B / 0M / 0m / 0n.  Boundary/locality stream terminal at the
repaired Paper 22 ceiling.**
