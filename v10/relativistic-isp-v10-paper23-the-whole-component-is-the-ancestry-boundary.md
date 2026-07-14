# Relativistic ISP v10 paper 23

# The whole component is the exact ancestry boundary

## Anchored tomography, predictive identity and unbounded information

**Status:** terminal candidate after three clean independent paper-level
hostile streams; exact status delta pending.
**Date:** 2026-07-14.

## Abstract

Paper 22 proved that no complete fixed actor radius predicts the full durable
ancestry of future records at a distinguished actor A under the chosen passive
D34b click law.  It left open whether an adaptive causal frontier could remain
smaller than A's connected component.  This paper closes that opening for the
exact full-ancestry query.

Every event touching an actor persists in that actor's current wire tip.  On a
finite birth-tree component, one inward interaction per edge in postorder
therefore collects every old component event into a future A record.  Mere
returnability is not yet predictive necessity: two different conditioning
cuts can reproduce the same unmarked-by-cut ancestry in the same number of
future events.  We exhibit that exact counterexample, with leading
coefficients `1/1152` and `1/576`, and reject the initial bare-sweep proof.

The repair is a fresh observable anchor.  A first creates one future A-idle
record, broadcasts it outward once over every rooted tree edge, and echoes it
inward once.  For a component of n actors the construction has

```text
q = 1 + 2(n-1) = 2n-1
```

distinct future events, all containing the fresh anchor.  The prescribed path
is a positive subevent of a measurable Branch-F output-prefix cylinder and
has small-time order `Delta^q`.  A different past either leaves an immutable
extra attachment witness in the prefix, or must spend at least one additional
future event creating missing old structure.  Its cylinder probability is
therefore zero or `O(Delta^(q+1))`.  The complete Branch-F future law separates
every rooted marked component configuration.

Consequently A's component class is sufficient and isomorphic to the minimal
exact predictive quotient.  Every deterministic exact sufficient carrier
must determine that class, although a nonminimal carrier may retain extra
data.  A positive-cylinder family with `2^M` distinguishable component
histories proves an M-bit worst-case lower bound for every M.  Thus the exact
ancestry boundary is component-sized in information and has no uniform finite
capacity over growth.

The result is analytical but model-relative.  It does not say one record
stores the component, that a simulator uses a global commit clock, that the
physical universe follows D34b, or that spacetime geometry is recovered.  It
also does not complete the v9 profinite bridge: only the discrete serialized
event-content skeleton has an immediate finite-prefix inverse tower; elapsed
time requires a separately constructed topology or finite quotients.

## 1. Result and interpretation

Let `K_A(h)` be the complete current configuration of A's connected D34b
component after a finite legal history h, and let `[K_A(h)]_g` denote its
rooted marked isomorphism class after quotienting nominal actor names and
auxiliary serialization order.

### Main theorem — component predictive identity

At every licensed finite stop of the chosen passive D34b law:

1. the conditional Branch-F future law is determined by `[K_A]_g`;
2. two different component gauge classes have different conditional Branch-F
   future laws;
3. the minimal exact predictive quotient is therefore isomorphic to
   `[K_A]_g`;
4. every deterministic exact sufficient carrier determines `[K_A]_g`; and
5. no uniform finite information capacity suffices over unbounded growth.

The theorem is stronger than Paper 22's fixed-radius no-go.  It excludes every
proper exact information quotient, not merely every fixed graph ball.  It is
also narrower than the slogan “the whole component must be stored.”  Cached
counts, degrees, parities and tips can be reconstructed from the legal event
DAG, and a minimal code may compress them.  What cannot be done is identify
two different rooted marked component histories while preserving the exact
full-ancestry future law.

For the connected seed used by D34b, the generated world is one growing
component.  In that chosen model the exact Branch-F boundary is therefore
world-component-sized.  This does not measure the real universe or establish
that nature uses this law.

## 2. Frozen law, records and query

### 2.1 Chosen D34b dynamics

Each active actor has an independent rate-one Poisson ring process.  At a ring
actor y chooses

```text
birth                              probability 1/4;
interaction with each neighbor x  probability 1/[4 degree(y)];
idle                               probability 1/2.
```

Birth creates one fresh Ulam child connected only to y.  Interaction appends
one shared event to the initiator and receiver wires.  Idle appends one event
to the initiator wire.  Every event contains its immutable kind, initiator-own
ring identifier, target, touched actors and previous tip of each touched wire.
Events and predecessor references persist.  Edges are never deleted.  This
chosen law has no dynamic sealing and does not join disconnected components.

The seed is the connected edge `A--B`.  Every component reached at a finite
stop is finite almost surely by the accepted D34b nonexplosion result.

These operations and coefficients are inputs.  This paper identifies the
predictive state of their exact ancestry query; it does not derive them from
SHARD's foundational principles.

### 2.2 Branch F

Branch F retains the ordered future process of every event touching A,
including each event's complete typed contents, persistent transitive
predecessor ancestry and elapsed occurrence time from the conditioning stop.
Nominal names are quotiented by rooted marked isomorphism.

Licensed stops are fixed construction time, A-own-ring hitting times and
A-wire-event hitting times.  Absolute construction time is gauge.  Fixed
global event depth is used only to enumerate finite regression domains; it is
not a regional physical clock or stopping rule.

### 2.3 Component state and gauge

`K_A` contains:

```text
actor rows and current wire tips;
the current birth tree and endpoint incidence;
all persistent typed event records;
all predecessor links.
```

The distinguished A role, actor parentage, event kinds, targets, initiator
ordinals, touched wires and predecessor DAG are physical marks.  Raw actor
names and serial orders of incomparable operations are presentation gauge.

The persistent legal event DAG plus the fixed seed reconstructs the rest:
birth events recover actors and adjacency; initiator identifiers recover ring
ordinals; interactions recover carrier parity; maximal touching events recover
wire tips.  The theorem concerns this gauge class, not duplicate storage of
every cached field.

## 3. Persistence and returnability

### Lemma 1 — wire persistence

Every event touching actor v is an ancestor of v's current wire tip.  Every
later event touching v retains that ancestry.

### Proof

The first touch becomes v's tip.  Every subsequent touch names the previous
tip as a predecessor and becomes the new tip.  Induction preserves the entire
old tip ancestry.  D34b has no overwrite, edge deletion or destructive seal
that could break the induction.  ∎

Root the current birth tree at A.  For every `v != A`, let `parent_A(v)` be the
neighbor one edge closer to A.

### Lemma 2 — postorder component collection

List every `v != A` in postorder and require the interaction

```text
v -> parent_A(v).
```

After the final A-touching interaction, every pre-stop event in the component
is in A's ancestry.

### Proof

A leaf transfers its whole persistent wire ancestry to its parent.  For an
internal actor, collect every child subtree first.  Those histories persist in
the actor's current tip; its subsequent interaction with its parent transfers
all child histories together with its own.  Induction through the rooted tree
collects the whole component at A.  Sibling order changes the path
serialization but not collection.  ∎

For n actors and one fixed postorder, the exact embedded component-clock mass
is

```text
p_sweep(K) = product_(v != A) 1/[4 n degree(v)] > 0.
```

If `m=n-1` and `Delta>0`, the event that these are the first m component rings
and complete by Delta has exact mass

```text
p_sweep(K) * ErlangCDF(m,n,Delta) > 0.
```

Thus every component record is capable of returning to A.  This fact alone
does not yet prove that every old history has a distinct future law.

## 4. Why the first tomography proof was false

The initial proposal used the bare postorder sweep itself as a fingerprint and
claimed that a different past would require one extra future event.  The stop
is not a mark inside old ancestry, so that claim is false.

Start with A--B and let B birth children C and D.  Compare:

```text
K:   D idles before the stop;
     after the stop run C->B, D->B, B->A.

K':  C->B occurs before the stop;
     after the stop run D-idle, D->B, B->A.
```

The two pasts are not gauge-isomorphic, yet the final B-to-A ancestry is the
same and both branches use three future rings.  Their exact leading
coefficients are

```text
K     1/1152;
K'    1/576.
```

The unequal coefficients still distinguish these two conditional laws, but
the claimed universal event-count separation is wrong.  D34f found and froze
this counterexample before the first receipt.  The bare sweep remains a valid
returnability construction; it is not a universal tomographic discriminator.

## 5. Fresh-anchor broadcast and echo

For a finite component K with n actors, prescribe:

1. one fresh A-idle future event `a_*`;
2. one parent-to-child interaction over every rooted edge in preorder;
3. one child-to-parent interaction over every rooted edge in postorder.

There are

```text
q = 1 + (n-1) + (n-1) = 2n-1
```

target events.  The first outward interaction inherits A's anchored tip.
Preorder induction puts `a_*` into every outward event.  Postorder induction
puts it into every inward event.  Every target operation therefore contains a
future event that did not exist before the conditioning stop.

The final inward event also contains every pre-stop component event by Lemma
2.  The construction simultaneously labels its own future cone and collects
the old component history.

For one frozen covariant preorder/postorder pair, the exact embedded mass is

```text
p_echo(K)
 = 1/(2n)
   * product_(parent->child outward) 1/[4n degree(parent)]
   * product_(child->parent inward)  1/[4n degree(child)]
 > 0.
```

No birth occurs on this path, so the total component ring rate remains n.  If
`S_K(Delta)` is the event that the first q component rings follow this path and
the qth completes by Delta, then

```text
P_K(S_K(Delta))
 = p_echo(K) * ErlangCDF(q,n,Delta)
 = c_K Delta^q + O(Delta^(q+1)),
```

where `c_K>0` is the product of the selected continuous transition rates
divided by `q!`.

## 6. The observable cylinder

The exact first-q-component-ring event is not itself a Branch-F observation:
Branch F need not report silent remote rings.  Define instead

```text
U^anchor_K(Delta)
 = {the initial future A-output prefix has K's canonical finite structural
    anchored-echo trace, and its final specified A event occurs by Delta}.
```

This is measurable from the ordered future A records, their typed ancestry and
the final specified event's elapsed time.  It says nothing about later A
outputs.  Intermediate real times and nominal names are integrated or
quotiented.

The prescribed path necessarily emits that prefix, so

```text
S_K(Delta) subset U^anchor_K(Delta)
```

and therefore

```text
liminf_(Delta->0)
  P_K(U^anchor_K(Delta))/Delta^q >= c_K > 0.
```

The distinction is real.  A remote actor may ring after its final inward
transfer while the remaining echo completes.  That hidden event adds a
component ring without changing the initial A-output prefix.  Independent
review constructs exactly such a q+1-ring path.  Thus `S` is generally a
strict subevent of `U`.

## 7. Anchored tomography

### Lemma 3 — first-unmatched-attachment

Let K' be a legal finite source that contains K's matched rooted actor/event
substructure plus extra old structure.

- An extra event touching a matched actor persists into that actor's target
  echo touch.
- If K' has an extra actor or subtree, choose the first unmatched actor along
  a birth-tree path out of the matched structure.  Its attachment birth event
  touched a matched parent.  That parent is touched by K's target echo, so the
  attachment record enters the output prefix.
- An altered event on a matched wire is immutable and likewise contaminates
  the prefix.

Therefore a proper extension or incompatible marked DAG has zero support for
K's exact anchored prefix.

The lemma does not claim every record inside an extra subtree returns under
K's shorter target echo.  A remote leaf idle can remain hidden.  Its attachment
birth cannot.

### Lemma 4 — anchored catch-up

If K' lacks a target record, actor or birth edge, any realization of K's
anchored prefix from K' needs at least q+1 post-stop component rings.

### Proof

The prefix contains q distinct target event records descended from the fresh
future anchor.  None can be supplied by K' before the stop.  A missing old
record or actor must be created by another future ring before the relevant
anchored target operations occur.  It cannot double as an echo operation: the
target trace contains both the unanchored old record and the anchored future
operation, with distinct kind, initiator ordinal or predecessor ancestry.
Thus all q anchor-cone nodes plus at least one catch-up node are required.  ∎

Starting from any fixed finite K', actor count grows by at most one per ring.
Total rates through a fixed q+1-ring prefix are therefore bounded.  The jump-
count tail obeys

```text
P_K'(at least q+1 component rings by Delta) = O(Delta^(q+1)).
```

Lemmas 3 and 4 give, for every `K'` not gauge-isomorphic to K,

```text
P_K'(U^anchor_K(Delta)) = 0 or O(Delta^(q+1)).
```

The target has positive liminf at order q, while every different source has
zero or higher order.  Their conditional Branch-F laws differ for all
sufficiently small positive Delta.

### Theorem 1 — finite component tomography

The map from a legal finite component gauge class to its complete conditional
Branch-F future law is injective.

### Proof

For each target class K use its measurable anchored cylinder.  The target and
every nonisomorphic source have different small-time behavior by the preceding
comparison.  ∎

## 8. Predictive quotient and exact carriers

The complete component class is sufficient: D34b is Markov on its current
legal configuration, its generator is equivariant under the declared gauge,
and disconnected components factor at the licensed stops.

Tomographic injectivity supplies the reverse direction.  If `B(h)` is any
deterministic exact sufficient carrier for Branch F, then

```text
B(h)=B(h')  implies  [K_A(h)]_g=[K_A(h')]_g.
```

Hence every exact carrier determines the component quotient.  The minimal
exact predictive quotient is isomorphic to `[K_A]_g`.  A minimal carrier is a
lossless code of it; a nonminimal carrier may retain additional information.

This is an information-necessity theorem.  It neither chooses a preferred
serialization nor says that A privately owns the data.  The state may be
distributed across record wires and reconstructed analytically.

## 9. Unbounded information

### Theorem 2 — M-bit lower bound

For every positive integer M, there are `2^M` reachable positive-cylinder
component histories at a common finite-time scope whose complete Branch-F
future laws are pairwise distinct.

### Construction

Grow a rooted chain with M structurally distinguished actor positions.  At
each position choose one of two legal typed events: idle or interaction toward
the parent.  All words of length M have positive probability.  They contain
the same number of construction events, so at any fixed `T>0` each can be
realized by requiring its finite sequence before T and no further component
ring before T.  The structural depths prevent nominal relabeling from
identifying different words.

The postorder sweep, or the anchored echo, returns all M choices to A.
Tomography makes the `2^M` classes predictively distinct.  Any exact carrier
therefore has at least `2^M` states on this family and needs at least M bits in
the worst case.  Since M is arbitrary, no uniform finite exact capacity
exists.  ∎

The chosen population process also illustrates the growth scale.  Every actor
births at rate `1/4`, so from two seed actors

```text
E[N_T] = 2 exp(T/4).
```

Every actor rings at rate one and every ring creates one event record, giving

```text
E[R_T] = integral_0^T E[N_s] ds = 8(exp(T/4)-1).
```

These are construction-time expectations inside D34b, not real cosmological
units or a prediction of the size of the physical universe.

## 10. Exact receipt

The terminal standard-library executable is
`v10/code/d34f_component_tomography_exact.py`; its committed stdout is
`v10/data/d34f_component_tomography_exact.out`.  It passes `11/11`:

```text
reachable labeled levels                  1,6,40,304,2576;
cumulative states                         2,927;
wire incidences                           20,148;
sorted/reverse bare sweeps                2,927 / 2,927;
anchored echoes                           2,927;
renaming/gauge checks                     351;
registered gauge classes/traces           351 / 351;
direct continuation emulator attempts     7,410;
equal-or-lower-order emulators             0;
bare equal-order coefficients             1/1152 / 1/576;
anchored q/q+1 coefficients               1/192 / 1/1536;
first-unmatched-attachment witness         1/1;
binary family sizes                       2,4,8,16,32,64;
finite gauge-class counts                 1,6,40,304.
```

All discrete probabilities are `Fraction` exact.  Erlang and exponential
values evaluate named analytic formulas at 110-decimal working precision.
The hashes are:

```text
code
0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef

stdout
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2

internal summary
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee
```

Finite enumeration is a regression and counterexample search, not the
all-size proof.  The persistence, rooted-tree, attachment and catch-up lemmas
carry the theorem analytically.

## 11. Hostile review

The investigation used a pin-before-receipt protocol.  Its own pre-receipt
attack rejected the first bare-sweep theorem and froze the anchored
replacement before code was accepted.

Three independent round-1 streams reproduced the receipt and attacked
probability, graph locality, query measurability, alternative cuts, nominal
gauge, extra branches, carrier minimality and profinite/quantum scope.  Counts
were:

```text
predictive/profinite  0 blockers / 0 majors / 2 minors / 0 nits;
boundary/locality     0 blockers / 0 majors / 0 minors / 0 nits;
ancestry/quantum      0 blockers / 0 majors / 2 minors / 0 nits.
```

Repairs separated the measurable cylinder U from the exact path subevent S,
proved the first-unmatched-attachment case, restricted lossless recoding to
minimal carriers and narrowed the inverse tower to the discrete event-content
skeleton.

All three exact closing deltas returned `0/0/0/0`.  Added attacks include:

- 1,096 extra-subtree placements over every actor in the registered small
  domain, with zero prefix emulators;
- a two-level extra branch whose internal records remain hidden while its
  first attachment birth is forced visible;
- a q+1 hidden-event path with the same A-output prefix, confirming
  `S subset U` is generally strict;
- shifted conditioning cuts and later-cut anchor loss;
- disconnected component-clock controls; and
- 17,390 expanded canonical comparisons with zero equal-or-lower-order
  emulator.

The terminal D34f note and closing reviews are frozen at commit `398077e`.

The candidate synthesis itself was then reviewed independently at commit
`540ddf1`.  Predictive/profinite, boundary/locality and ancestry/quantum
streams each returned `0 blockers / 0 majors / 0 minors / 0 nits`.  Their new
attacks include all 35,898 reachable transition rows for nonlocal writes or
old-record mutation, 351 disconnected controls covering 3,682 A-component
rate rows, attachment directly at A, deeper alternative cuts and the fixed-
time `2^M` construction.  No source repair was requested.  Only the terminal-
status and review-accounting strings differ from that accepted candidate.

## 12. What “the boundary is huge” means

The conclusion concerns an exact, unlimited-horizon question:

> What is the complete typed ancestry of every future record that will touch
> A?

Under a law with perfect persistence and no horizon or sealing, remote old
information always has a positive-probability route back to A.  Asking for its
exact future behavior therefore prevents the predictor from forgetting any
distinguishable component history.  As the component grows, the exact
information boundary grows with it.

This does not imply a physical record contains an enormous literal database.
The history is distributed over many records.  Nor does it imply a machine
must scan the component before every click.  D34b updates by local actor rings;
the component state is the mathematical sufficient state of the whole future
law, not a global execution algorithm.

A smaller boundary can become possible only by changing the problem or the
law, for example:

- predict only a finite future horizon;
- coarse-grain the ancestry readout;
- accept controlled approximation;
- introduce genuine horizons, attenuation or irreversible sealing; or
- use a different interaction grammar with an intrinsic causal-speed
  structure.

These are physical alternatives, not loopholes in the exact theorem.

## 13. Profinite ceiling

After forgetting real elapsed-time marks, the discrete serialized
event-content grammar has finite levels at each fixed event depth and an
ordinary inverse-limit end space.  This is the immediate profinite-adjacent
host earned by D34f.

The full timed prefix levels are uncountable.  A timed completion requires an
explicit topology or finite observable time partitions.  D34f does not prove:

- canonical bonding maps after construction-order gauge;
- identification with the v9 unmarked stem spectrum;
- continuity of the Branch-F predictive map on either completion; or
- a finite physical record carrying one completed infinite-history point.

Profinite organization can host compatible finite records.  It does not by
itself shrink the exact predictive quotient or select the history law.

## 14. Quantum and spacetime ceiling

The theorem is classical and passive.  It constructs no intervention-indexed
controlled process and no intrinsic quantum operation law.  It therefore does
not determine a quantum carrier width, process-tensor Markov order or the way
local actor events generate the D34c quantum functional.

It also supplies no causal speed, Lorentz cone, dimension, proper-time ruler,
metres, seconds or value of G.  The anchored broadcast is a possible event
sequence on the D34b actor graph, not a signal trajectory in an already
derived spacetime.

Any future candidate interactive click law must establish its own predictive
boundary and then rerun the v9 cone, scale and dimension diagnostics.  The
current theorem says how demanding complete durable ancestry is under D34b;
it does not show that D34b grows round cones or 3+1 spacetime.

## 15. What is closed and what remains open

### Closed for the chosen law and exact query

- every component event is returnable to A;
- the bare-sweep universal order proof is false;
- the fresh anchored echo is a valid measurable discriminator;
- the complete Branch-F future law identifies the whole finite component
  gauge class;
- that class is the minimal exact predictive quotient; and
- its worst-case information requirement is unbounded over growth.

### Open beyond this theorem

1. **Finite-horizon and approximate frontiers.**  Quantify how much of the
   component is needed at finite Delta or fixed error tolerance.
2. **Sealing and horizons.**  Determine which record-native erasure or causal
   horizon principle makes old component information permanently
   nonreturnable.
3. **Timed profinite bridge.**  Construct finite time quotients or another
   topology, construction-order-gauge bonding maps and the v9 posterior
   factorization.
4. **Controlled quantum lift.**  Derive how actor events generate the timed
   D34c quantum process rather than carrying an independent subsystem beside
   the record graph.
5. **Law selection.**  Derive or empirically identify the actual interactive
   click law.  D34b remains a chosen exemplar.
6. **Geometry rerun.**  Only for a surviving law, retest causal cones,
   dimension, the many-clocks/few-factors structure, physical-unit recovery
   and gravitational scaling.

The direct next theoretical move is no longer to search for an exact small
full-ancestry frontier under D34b; that possibility is closed.  The productive
fork is either to weaken exact unlimited-horizon ancestry or to add a physical
principle—sealing, attenuation or causal speed—that genuinely limits what can
return.

## 16. Conclusion

The full durable-ancestry query turns persistent history into a severe memory
test.  Local generation does not make that test locally predictable.  Under
D34b every old component record can flow back to A, and a fresh anchored echo
lets the future law reveal which whole component past it came from.

The endpoint is exact:

> the minimal predictor of complete future A ancestry is the rooted marked
> component history itself, up to gauge and lossless coding.

This confirms the motivating expectation that the analytical boundary may be
huge.  It also identifies why: not because a simulator requires a universal
ledger, but because the chosen law never makes component information
irretrievable while the query insists on exact ancestry forever.

The next physics must explain how nature avoids or uses that conclusion.
Either the relevant observations are finite and approximate, or the real law
contains a causal mechanism that limits returnability.  Finding that mechanism
is now sharper than looking for a smaller exact collar inside D34b.

## References

1. Relativistic ISP v10 Paper 21, *Local generators do not imply local
   memory*.
2. Relativistic ISP v10 Paper 22, *The predictive record-DAG boundary of a
   chosen click law*.
3. D34f terminal note, `note-d34f-component-tomography-and-necessity.md`.
4. C. R. Shalizi and J. P. Crutchfield, *Computational Mechanics: Pattern and
   Prediction, Structure and Simplicity*, Journal of Statistical Physics 104,
   817--879 (2001), DOI `10.1023/A:1010388907793`.  Background for minimal
   predictive equivalence; no SHARD component theorem is attributed to it.
