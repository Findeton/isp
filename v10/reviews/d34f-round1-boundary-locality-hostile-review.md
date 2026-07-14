# D34f round 1 — independent boundary/locality hostile review

**Frozen target:** commit
`4c2498772d48273548420c5e483d519976344f91`.

**Exact hostile target:** find either

1. a legal pre-stop event in A's finite component that is absent from the
   final A-touching ancestry after the prescribed rooted echo; or
2. a component configuration not rooted-marked-isomorphic to target `K` that
   produces `K`'s exact anchored Branch-F trace in at most
   `q(K)=2|K|-1` post-stop component rings.

**Exact verdict:** **PASS — NO BOUNDARY, LOCALITY OR CLOCK COUNTEREXAMPLE AT
THE FROZEN CLAIM CEILING.**

**Count:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

This stream independently accepts the provisional first decision row,
`COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED`, for the chosen passive D34b law,
the exact durable-ancestry Branch-F query and the licensed stopping scopes.
The result is an identity of finite predictive gauge classes, not a derivation
of that law, a local finite-capacity ontology, a proper-time construction or a
spacetime/quantum theorem.

## 1. Frozen-target reproduction

I reran the exact program with fresh `PYTHONHASHSEED=104729`. It exited zero,
printed `11/11 PASS`, and was byte-identical to the committed receipt.

```text
source SHA-256
906687d7dae9776cb707dd040de8970c2aee72096b2e0a636f97e5bdb1e6182a

committed stdout SHA-256
ff2365ad8c5cf85d7e463d42b8a1f039b2a58d987229de3e606026f10c4a5eea

fresh stdout SHA-256
ff2365ad8c5cf85d7e463d42b8a1f039b2a58d987229de3e606026f10c4a5eea

note SHA-256
f29b34b5d4b0ce1b56ec98fcc2caa7954cd106a79110988047d8763d15bbf053

receipt digest
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee
```

The frozen ledger reproduced exactly:

```text
reachable labeled levels                 1, 6, 40, 304, 2576
cumulative legal states                  2927
wire incidences checked                   20148
sorted/reverse bare sweeps                2927 / 2927
anchored echoes                           2927
renaming/gauge checks                     351
registered gauge classes/traces           351 / 351
direct continuation emulator attempts    7410
equal-or-lower-order emulators            0
bare equal-order coefficients             1/1152, 1/576
anchored target/catch-up coefficients     1/192, 1/1536
binary-family class sizes                 2, 4, 8, 16, 32, 64
finite gauge-class counts                 1, 6, 40, 304
finite worst-case bit ceilings            0, 3, 6, 9
```

The fractions are exact. Decimal exponential/Erlang rows are evaluations of
the printed analytic formulas at the declared precision; no inference in this
review depends on decimal rounding.

## 2. Wire persistence and reconstruction

The persistence argument survives direct inspection. An event touching wire
`v` stores the previous tip of `v`. Thus the new event contains the previous
tip's whole transitive ancestry. Induction over later touches proves both:

```text
every old event on v is in v's current-tip ancestry;
every later event touching v retains that ancestry.
```

There is no overwrite operation, destructive seal or edge deletion in the
frozen D34b grammar that could defeat the induction.

The reconstruction claim also stays inside that grammar. From the persistent
typed event DAG and the fixed A--B seed one recovers:

- actors and birth edges from typed births;
- adjacency from the immutable birth tree;
- each initiator's own ring ordinal from event identifiers;
- interaction parity and therefore the modeled carrier;
- current wire tips as the maximal touching events.

Cached degree, count, parity and tip fields need not be stored twice. This is
why the theorem is correctly stated for `[K_A]_g` up to lossless recoding,
rather than as a claim that every database column is separately irreducible.

I added an independent legal specimen with 10 actors, an asymmetric branched
birth tree and 23 old events. Reconstruction matched the generated state
exactly. This test included births at several depths, an idle on every actor
and additional interactions at alternating depths.

## 3. Returnability on an arbitrary finite rooted birth tree

The postorder proof is a valid tree induction.

For a leaf `v`, `v -> parent_A(v)` transfers every old event on `v` into the
parent wire. For an internal vertex, first collect every child subtree. Wire
persistence leaves their accumulated histories in `v`'s current tip. The one
subsequent `v -> parent_A(v)` interaction transfers all of them, together with
`v`'s own old history, toward A. Applying the step through the root makes the
last A-touching interaction contain every pre-stop component event.

Sibling order is irrelevant to collection: whichever child is collected
first remains in the parent's wire ancestry when later children arrive. My
10-actor specimen was swept in both sorted and reversed sibling orders; both
orders collected all 23 old events. No legal component event outside the
final A ancestry was found.

The proof uses precisely the static connected birth-tree property of D34b.
It would need revision for edge deletion, destructive sealing, component
joining or a non-tree opportunity graph; D34f does not claim those extensions.

## 4. Why the fresh anchor repairs the bare-sweep failure

The note correctly rejects its original bare-sweep T4. In its printed K/K'
pair, moving `C->B` across the unobservable stop and moving `D`'s idle the
other way gives the same final ancestry in three future rings. The unequal
coefficients `1/1152` and `1/576` distinguish the laws but refute the proposed
universal `m` versus `m+1` support argument.

The anchored echo removes exactly that cut ambiguity:

1. A creates a fresh future idle event `a_*`.
2. Preorder interactions carry it once over every outward tree edge.
3. Postorder interactions carry every subtree back to A.

There are exactly

```text
1 + (n-1) + (n-1) = 2n-1 = q
```

target events. Every one contains `a_*` in its ancestry. Hence none is an old
event merely reclassified by a different position of the conditioning cut.
The final echo also contains all pre-stop target history by the returnability
induction.

I attacked the two vulnerable scheduling cases explicitly:

- arbitrary raw child ordering rather than the program's preferred order;
- one new idle on every actor after outward broadcast but before inward
  collection.

The 10-actor echo used 9 outward and 9 inward interactions. Every target event
contained the anchor, all 23 old events arrived at A, and all 10 interleaved
extra events were collected.

## 5. The `q` versus `q+1` lower bound

The repaired catch-up argument is combinatorial, not a conclusion from the
finite search.

To emit the exact target trace, any source must create all `q` target event
records after the stop: each contains the new anchor, and persistent event
records cannot be forged by relabeling an old record across the stop. Those
`q` records already require at least `q` component rings.

If a candidate source is missing any target record, actor or birth edge, it
must first create it. That creation is not one of the target anchored records,
so it costs at least one additional component ring. It cannot be hidden by
performing it before the anchor: it is still post-stop and contributes to the
small-time event order. It also cannot replace one of the `q` target events,
because the target record's kind, initiator ordinal, touched wires and
predecessors are part of the exact trace.

If a source has an extra or altered old record on a target wire, persistence
makes it visible when that wire is collected. An extra actor or branch cannot
be silently used as a target actor: its immutable birth record and the
parent's initiator ordinal expose the change. Ignoring the branch does not
create a shortcut to a missing target record, and a pure extra history shifts
the first later initiated target ordinal or enters a collected predecessor
ancestry. Balancing an extra with a missing target record returns to the
additional-ring case.

Consequently a nonisomorphic source has either zero support for the exact
trace or needs at least `q+1` post-stop component rings. This is sufficient for

```text
target:       positive leading term at Delta^q;
non-target:   zero or O(Delta^(q+1)).
```

As an independent finite attack, I expanded the direct emulator search from
the committed registered battery to every depth-one target in the frozen
enumeration, comparing level-zero and level-one sources through the target's
`q`-ring bound. It performed 17,390 canonical trace comparisons and found
zero equal-or-lower-order emulators. This is a regression check on the proof,
not its replacement.

## 6. Gauge and canonical schedules

The physical target is not a raw actor-name serialization. A is fixed; other
actor names are quotiented by rooted marked isomorphism. Canonical preorder
and postorder schedules select one representative construction of an
observable gauge class.

Automorphism ties among indistinguishable sibling subtrees do not create a
physical distinction. Exchanging tied subtrees transports the whole event
trace by the same rooted isomorphism, and the exact probability mass is
unchanged because the corresponding degrees and interaction rows are
transported together.

I independently renamed a fresh 6-actor asymmetric specimen, reconstructed
both copies and transported the anchored trace. Their canonical component,
canonical trace and exact embedded mass agreed. The mass in that deliberately
nonuniform example was

```text
1/194775186325635072.
```

No nominal-name or sibling-order discriminator survived the quotient.

## 7. Exact mass and lawful clocks

With `n` actors fixed during an echo, component rings occur at total rate
`n`. At an embedded ring:

```text
A idle                                  1/(2n)
fixed initiator v interacts with x     1/[4 n degree(v)]
```

Multiplying the first factor, all outward factors and all inward factors gives
the note's exact `p_echo(K)`. Requiring the `q`th component ring by elapsed
time `Delta` multiplies the fixed embedded sequence by
`ErlangCDF(q,n,Delta)`. Equivalently, its leading continuous-time coefficient
is the product of the selected continuous event rates divided by `q!`.

This use of time does not install a universal ledger clock. The law begins
with independent actor Poisson processes; their superposition within A's
current finite component is a calculational component clock. A disconnected
component does not change these continuous rates or this component-relative
sequence probability.

I added a disconnected `P--Q` component. The selected A-component continuous
factor remained `1/2`, while the same row's artificial global-depth share
changed from `1/4` to `1/8`. This is the intended distinction: fixed global
embedded depth is not a regional physical stopping rule.

The licensed fixed-construction-time, A-own-ring and A-wire-event stops are
compatible with the inherited nonexplosion and strong-Markov arguments. None
of them turns an actor's event counter or the superposed component clock into
relativistic proper time. D34f makes no Lorentz, cone or metric claim, and I
found no concealed such promotion.

## 8. Predictive identity, factorization and unboundedness

The anchored discriminator separates every distinct finite component gauge
class in the complete Branch-F future law. Conversely, the frozen generator
consults only the component configuration, so that class is sufficient. The
predictive quotient is therefore isomorphic to `[K_A]_g` up to lossless
recoding.

Disconnected controls factor because D34b has neither component joining nor
cross-component rates. This is component locality, not bounded-radius
locality: within A's connected component, complete durable ancestry makes
arbitrarily remote finite history returnable to A with positive probability.

The rooted-chain family supplies the required information lower bound. Its M
structurally located binary idle/interaction choices are physical marked-DAG
choices, not nominal permutations. The echo recovers them, producing `2^M`
distinguishable positive-cylinder classes and at least M worst-case bits. This
establishes no uniform finite exact capacity as the component grows.

## 9. Claim ceiling and final disposition

At the exact frozen scope I found:

```text
uncollected legal component events                  0
branched/reversed-sibling collection failures       0
fresh-anchor containment failures                   0
nonisomorphic <=q-ring emulators                     0
nominal-gauge/transport failures                     0
disconnected continuous-rate locality failures      0
clock or geometry overclaims                         0
```

The accepted statement is narrow but strong:

> For every legal finite stop of the chosen passive D34b model, exact
> prediction of complete future A-touching ancestry distinguishes the entire
> rooted marked component configuration. The exact predictive state is that
> gauge class up to lossless recoding, and its information requirement is
> unbounded over growth.

It does **not** establish that D34b is nature's history law; derive its
coefficients or event grammar; provide a quantum operation rule; connect the
actor clock to proper time; produce light cones or dimension; identify `G`;
or prove the v9/profinite bridges. Those remain outside D34f.

**Final count:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

**Final verdict:** **PASS — COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED
SURVIVES THIS INDEPENDENT BOUNDARY/LOCALITY HOSTILE STREAM.**
