# D17 round-4 integrated ontology/locality hostile review

**Date:** 2026-07-12  
**Referee stream:** focused typed-admission, gauge and record-path audit  
**Candidate:** `INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION`  
**Verdict:** **MAJOR REVISION OF H8/GAUGE CLAIMS; NONSELECTION PASSES AT FIXED-FILTRATION SCOPE**

## Decision

The round-3 exploits against the new element owner, child collar owner,
carried memory, D14 carrier, and past-directed join are repaired.  I reran
those attacks and added a future-directed two-owner join.  All four forged
D17 node fields reject.  Both join orientations reject without the exact
two-owner set and pass with it.  A consistently relabeled version of the
declared `chain2 -> chain3` edge now admits.  Every causal node through depth
six has exactly the D14 boundary type appropriate to its depth.  The reset
changes record support while leaving the causal path support unchanged.

The finite fixed-action kernel-nonselection theorem is therefore sound at a
clear narrowed scope:

> One supplied finite **labeled filtration**, its supplied D17 collar grammar,
> one fixed action, and one supplied local D14 record network admit at least
> three inequivalent positive projective kernels.

Two exact openings prevent an unconditional H8/gauge closure.

First, `canonical_typed_key()` canonicalizes the relation and
`element_owners`, but silently discards the D16 `past_boundary` and
`future_boundary` fields that are part of `CausalOrder`.  I added a
foreign-owned typed future boundary to an otherwise declared `chain3` child.
The declared edge still admitted.  Thus the repaired key protects every D17
collar field but not every typed field of the imported causal-order object.
The source must either include those boundaries in the canonical key or reject
nonempty D16 boundaries as outside D17's grammar.

Second, relabel covariance is not construction-order gauge.  The canonical
key correctly identifies isomorphic copies of the **same parent-child edge**.
It does not identify different filtrations of the same completed order.  The
frozen diamond is reached by revealing its minimal element after a `V3`
parent.  The same diamond can be reached by revealing its maximal element
after a `Lambda3` parent.  That second induced edge is valid and ends at the
same unlabeled diamond, but the supplied grammar rejects it.  This is allowed
for a supplied filtration; it disproves the stronger wording that
construction order has been shown to be gauge.

These openings do not alter any frozen probability or undermine the logical
nonselection counterexample.  They do mean that the round-3 ledger's phrase
“owner-safe and gauge-covariant” remains too broad.  D17 is owner-safe for its
explicit D17 node/collar fields and invariant under compatible element
relabeling of a declared edge.  It is not yet complete for D16 boundary types
or invariant under alternative construction filtrations.

## Frozen reproduction

I copied D13, D14, D16, the first D17 witness and the integrated D17 witness to
a clean `/tmp` tree.  Normal and optimized Python both pass `38/38`; their
stdout hashes agree, and the regenerated packet is byte-identical to the
primary packet.

```text
checks                    38/38 normal and -O
source SHA-256             1e934d2630aaae6ece9670b10132ab4f1c3f87d92c17c148ac699fd2209c0640
packet SHA-256             397f35deafa549731b43c01886ecade5f8981651d13aca222b3a6430dcd84624
semantic SHA-256           addbfd1a0324b9ca26906361e42be731dbe0531660628a7db3ebe33cd614e7b2
normal/-O stdout SHA-256   1c520ddbfe0822a62c7e86ae7e80dc3305952bfb3a3aca66a5f28783242f18f4
D14 dependency             e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16 dependency             861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
first D17 dependency       305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
```

The receipt's bytes and numerical claims reproduce exactly.  Explicit
`check()` calls, count guard and semantic hash guard remain active under
`-O`.

## Focused hostile matrix

The following results come from a clean import of the copied source:

```text
forged new-element owner rejects                    True
forged child collar owner rejects                   True
forged carried memory rejects                       True
forged D14 carrier rejects                          True
forged D16 future-boundary metadata admits          True   <-- opening

past two-owner join without entitlement             rejects
past two-owner join with {A,B}                      admits
future two-owner join without entitlement           rejects
future two-owner join with {A,B}                    admits

consistently relabeled declared edge                admits
Lambda3 -> same diamond alternative filtration      rejects <-- scope/gauge

all node carriers match D14 boundaries              True
causal paths before reset                           000,101
causal paths after reset                            000,101
reset visible-record support                        000,100
```

## Finding ledger

```text
R4-1 MAJOR    D16 typed past/future boundary ports are omitted from the
              canonical declaration key.  A foreign boundary can reuse a
              declared edge.
R4-2 MAJOR    Compatible element relabeling now passes, but alternative
              construction filtrations of the same final order need not.
              “Construction order is gauge” remains unproved.
R4-3 MODERATE The D17 collar and D14 carrier types now coincide exactly, but
              causal extension and record evolution remain parallel typed
              calculations rather than one state-carrying morphism.
R4-4 MINOR    The built-in path/reset separation check contains a tautological
              order equality; independent reconstruction confirms the intended
              separation anyway.
R4-5 PASS     The prior new-owner, collar-owner, memory and carrier forgeries
              all reject.
R4-6 PASS     Both past and future multiowner joins reject without and pass
              with the exact touched-owner set.
R4-7 PASS     All thirteen frozen node carriers equal the corresponding D14
              source/target boundary types, including both branches and later
              continuations.
R4-8 PASS     The full three-commit network is isometric, the reset is exactly
              CPTP complete, and sealed records are durable.
R4-9 PASS     Causal paths and intervention-dependent visible record labels are
              distinct maps; reset does not rewrite causal order.
R4-10 PASS    Grammar, kernel, commit and continuation remain explicitly
              supplied; no action-derived universe law or geometry is claimed.
```

## 1. Prior D17 node-field forgeries are closed

The repaired admission predicate checks the complete D17 node transition in
the following order:

```text
requested owner == parent live-collar owner
child collar owner == requested owner
child is an induced one-element extension
owner tuple arities match order sizes
all old element owners are unchanged
new element owner == requested owner
boundary memory is installed once and then preserved
child D14 carrier == the exact depth-dependent expected carrier
multiowner touched support has exact entitlement
canonical typed parent/collar/child/collar edge is declared
```

This closes the previous mismatch between a caller-provided owner string and
the actual owner recorded on the child.  Changing only the new element's owner
now fails at the explicit new-owner equality.  Changing only the child collar
owner fails before declaration lookup.  Changing memory from zero to one on
the declared chain branch fails the carried-memory transition.  Replacing the
first D14 memory port with a different kind while retaining all other ports
fails exact carrier equality.

The declaration key also now includes:

- the canonical relation-plus-element-owner key for the parent and child;
- collar owner and memory; and
- every D14 carrier port's kind, dimension, seal flag, owner and record ID.

Consequently the earlier strategy of preserving marks and relation while
spoofing D17 owner/collar/carrier data no longer reuses a declared edge.  This
is a substantive locality repair, not merely an extra negative test.

`GrowthNode` itself still has no `__post_init__`, but malformed owner arities
are rejected by `admit()` and by `canonical_typed_key()`.  Since admission is
the protected boundary in the frozen construction, that is sufficient for
the displayed packet.

## 2. One typed causal-order field remains outside the key

D17 imports D16's `CausalOrder`.  That dataclass contains three physical data
fields:

```text
relation
past_boundary: tuple[BoundaryPort,...]
future_boundary: tuple[BoundaryPort,...].
```

`canonical_typed_key()` calls `order.permute()`, which correctly permutes the
boundary ports, but then records only the flattened relation and the
`element_owners` tuple.  The permuted past/future boundary data are discarded.
`is_one_element_extension()` likewise compares only the old relation block.

I cloned the declared `chain3` child relation and added

```text
future_boundary = BoundaryPort(
    element=2,
    kind="forged-boundary-kind",
    owner="foreign-cell",
).
```

The order is valid under D16: element 2 is maximal.  I left the D17 element
owners, D17 collar, memory and D14 carrier unchanged.  `GrowthGrammar.admit()`
returned `True` for the declared edge.

This is precisely the class of typed-data substitution the new declaration
key is meant to prevent.  There are two clean repairs:

1. extend `canonical_typed_key()` with canonicalized past/future boundary
   triples `(element,kind,owner)`; or
2. state that D17 uses only boundary-free D16 orders and reject any node whose
   `order.past_boundary` or `order.future_boundary` is nonempty.

The second option is compatible with the current D17 collar design.  Leaving
the fields silently ignored is not.

This opening does not affect the frozen thirteen nodes, whose D16 boundary
tuples are all empty.  It blocks the general claim that the present admission
key covers the complete typed causal node.

## 3. Past and future join controls now work

The touched support now includes every old element comparable with the new
element in either direction:

```text
old < new  or  new < old.
```

This is the necessary repair for a grammar that permits past insertion.  I
used the same two-owner antichain parent for both attacks.

For a past join,

```text
new_A < old_A
new_A < old_B,
```

the touched owner set is `{A,B}`.  Admission rejects with no entitlement and
passes with exactly `{A,B}`.  For the time-reversed future join,

```text
old_A < new_A
old_B < new_A,
```

the result is identical.  Extra or missing owner sets fail the equality.

This closes the round-3 directional bypass.  At the ontology level,
`join_entitlement=("A","B")` remains supplied authorization data rather than
something derived from the interval action.  Moreover it is a declared owner
set, not a cryptographically authenticated capability.  That is consistent
with D17's finite symbolic scope, provided “entitlement” retains that meaning.

For a future extension the use of all transitive comparables can be stricter
than a cover-boundary locality rule, but over-rejection is not a nonlocal join
bypass.  Selection of the physically correct local support remains part of the
supplied grammar.

## 4. Relabel covariance passes; construction-order gauge does not

The new canonical key minimizes the relation-plus-owner representation over
all element permutations.  A simultaneous relabeling of the declared
`chain2` parent and `chain3` child, with the old/new embedding retained, now
has the same canonical key and admits.  This repairs dependence on arbitrary
names of the elements in one edge.

That property is **element-relabel covariance**.  Construction-order gauge is
stronger.  It asks whether different reveal/birth filtrations that reach the
same unlabeled completed order are physically equivalent.

The diamond makes the distinction exact:

```text
delete the minimal diamond element -> V3 parent
delete the maximal diamond element -> Lambda3 parent
```

The frozen grammar declares the first filtration.  I constructed the second
as a valid induced one-element edge

```text
Lambda3 -> standard diamond4.
```

It ends at an order canonically identical to the frozen diamond and uses the
same owner, collar, memory and D14 carrier types.  It rejects because the
`Lambda3` parent has a different unlabeled order key from `V3` and that edge is
not in supplied `Ext(C)`.

There is nothing inconsistent about rejecting it: `Ext(C)` is explicitly a
supplied, selective grammar.  What follows is that construction filtration is
part of the supplied kernel data, not a proved gauge redundancy.

The source comment “Construction order is gauge, so past insertions are
allowed” conflates two claims.  The executable proves only that nonmaximal
induced refinements are permitted when declared.  The round-3 ledger's
“gauge-covariant” should be replaced by:

> declared edges are invariant under compatible element relabeling; the
> filtration/extension grammar remains supplied, and independence from a
> different construction order is open.

If true construction-order gauge is desired, D17 needs a path-independence or
discrete-general-covariance condition comparing all admitted filtrations that
reach the same unlabeled order, including their amplitudes, records and
cylinder weights.

## 5. Node-to-D14 carrier identity

The repair establishes exact structural identity at every frozen depth.
Starting from the root's one-port memory carrier, the causal grammar expects:

```text
depth 0   boundary memory
depth 1   memory + sealed X + live-X collar
depth 2   previous carrier + sealed Y + live-Y collar
depth 3   previous carrier + sealed Z + live-Z collar
depth >3  preserve the complete depth-3 carrier.
```

These are exactly `net1.source`, `net1.target`, `net2.target`, and
`net3.target`.  I checked all thirteen nodes, not only the zero branch sampled
by the built-in equality.  Both branches at each depth and every later
maximal continuation match.

The carrier key includes the full ordered port signature, so changing kind,
dimension, seal, owner or record ID rejects.  This closes the prior
type-level gap between a generic D17 collar and a separate D14 network.

One ceiling remains.  Carrier equality is equality of immutable boundary
**types**, not an application of a state-carrying causal-extension morphism.
`causal_tower()` advances nodes and probabilities; `record_table()` separately
applies the D14 matrices to supplied amplitudes.  Their labels and weights are
then shown equal.  No single operator returns both the child causal order and
the child boundary state.

That is adequate for the theorem's word “compatible.”  It is still not the
final locally executable interacting click law.  The theorem's last paragraph
correctly keeps the commit and grammar supplied.

## 6. Commit locality, durability and reset separation

The three-commit D14 network passes full, not merely branchwise, isometry:

```math
V^\dagger V=I_2.
```

Every port has owner `history-cell`.  Each commit appends a sealed record and a
live collar.  D14's `Mor` admission preserves every prior sealed value, and
the final carrier contains `X,Y,Z` with their identities intact.  This is a
valid exact finite durability result.

The reset family now explicitly satisfies Kraus completeness on the complete
depth-two carrier:

```math
K_0^\dagger K_0+K_1^\dagger K_1=I.
```

It acts on the memory port while D14's protected correspondence preserves
sealed `X,Y`.  The final `Z` commit then produces visible support
`000/100`.

The causal tower remains supported on paths `000/101`.  I recorded the causal
path keys before and after the reset calculation; they are byte-for-byte the
same.  Thus the intervention changes the record map, not the order path.  The
new explicit maps correctly represent

```text
normal: causal path 101 -> visible record 101
reset:  causal path 101 -> visible record 100.
```

The built-in check's order clause compares
`by_marks[(1,0,1)].order` with itself and is therefore tautological.  This is a
minor receipt weakness, not a semantic conflation: the reset functions receive
only D14 states/morphisms and have no reference by which to mutate the frozen
causal nodes.  The independent before/after support test confirms the intended
separation.

The post-reset record family is used only as a depth-three deletion
countercontrol.  D17 does not claim it is a second all-depth causal path tower,
and it should not: `100` is a visible record label, not a replacement causal
node.

## 7. Supplied-versus-derived audit

The source, JSON and receipt consistently preserve the crucial ceiling:

| Object | Frozen D17 status |
|---|---|
| Interval action | supplied and evaluated on every node |
| Extension filtration/grammar | supplied |
| Root branch kernel | supplied |
| Deterministic continuation | supplied |
| D14 record commit | supplied |
| Boundary amplitudes/orbit convention | supplied |
| Proper-time sampler | absent |
| Action-derived universe law | not claimed |
| Geometry, scale, `G`, V9 holdout | absent |

The exact result is nonselection: holding the action, node set, supplied
grammar and supplied record network fixed still permits the equal,
positive-envelope and inverse-orbit kernels.  Repairing the typed-boundary key
or narrowing the gauge language will not change that proof.

The theorem says the packet “closes the former causal-tower/grammar/local-
memory construction gap at finite scope.”  After the D16 boundary omission is
fixed, that is defensible as a finite conditional compatibility statement.
It must not be paraphrased as selecting a physical grammar or producing the
final dynamic click law.

The theorem status line is stale—it still says “awaiting focused round-3
closure”—but the substantive final paragraph is correctly scoped.  This is an
editorial update, not a scientific finding.

## Gate disposition

```text
H0  PASS          action, state and orbit factors remain separate.
H1  PASS/PARTIAL  finite groupoid ratio passes on the frozen pair; no complete
                  path-groupoid quotient.
H2  PASS          exact finite local record network and interference witness.
H3  PASS          Born weights applied once.
H4  PASS          positive normalized recorded partitions.
H5  PASS          actual induced nodes through depth six plus supplied finite-
                  depth continuation schema.
H6  PASS/PARTIAL  exact shared D14 carrier types, two positive packets and
                  reset; no combined order-plus-state transition operator.
H7  PASS          one fixed action/grammar/network admits inequivalent kernels.
H8  PARTIAL/FAIL  D17 owner/collar/memory/carrier and bidirectional join checks
                  pass; D16 boundary metadata omission remains.
H9  PARTIAL       element relabel covariance passes; construction-order gauge
                  and filtration independence are not proved.
H10 OPEN/HONEST   no geometry, units, scale, G or V9 claim.
H11 OPEN          one focused typed-boundary/gauge-scope repair remains before
                  ontology closure.
```

## Required repair

1. Include canonical D16 past/future `BoundaryPort` data in the typed order key,
   or reject all nonempty D16 boundaries in D17 nodes.
2. Replace “construction order is gauge” with “one supplied construction
   filtration; compatible element relabelings are quotiented,” unless a real
   path-independence theorem is added.
3. Change the ledger's “owner-safe and gauge-covariant” to the exact narrower
   claims proved by the API.
4. Replace the tautological order equality in the reset check with a frozen
   before/after causal-key comparison.
5. Preserve the existing supplied-data ceiling.  A future composed
   order-plus-boundary transition would strengthen integration but is not
   needed for the finite nonselection theorem.

## Final verdict

**MAJOR REVISION of H8 and construction-gauge wording.**  The round-3 D17
owner, collar, memory, carrier and past-join bypasses are genuinely closed;
future joins also behave correctly.  Carrier identity, isometry, CPTP reset,
durability, projectivity, path/record separation and fixed-action kernel
nonselection all pass at finite scope.

Do not claim complete typed admission while D16 boundary ports can be forged,
and do not equate compatible element relabeling with construction-order gauge.
With those two scope repairs, the candidate nonselection theorem can close as
a finite conditional result.  It still does not derive the grammar, commit,
kernel, continuation, proper time or geometry from the action.
