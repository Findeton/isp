# D17 round-5 integrated ontology/locality review

**Date:** 2026-07-12  
**Referee stream:** joint-embedding, D16 boundary and filtration-scope audit  
**Candidate:** `INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION`  
**Verdict:** **PASS AT THE FINITE SUPPLIED-FILTRATION NONSELECTION SCOPE**

## Decision

The two exact round-4 keying defects are repaired.

The declaration no longer canonicalizes the parent and child separately.  It
canonicalizes one **marked extension edge**, permuting the old elements in the
parent and child together while keeping the newly inserted child element
distinguished.  A compatible relabeling of a declared edge therefore admits,
while an abstractly isomorphic child with a different undeclared embedding of
the parent rejects.

The marked-edge presentation now includes every D16 boundary tuple in both
the parent and child.  Forged future-boundary, past-boundary and parent-
boundary metadata all reject.  I also constructed a grammar with a genuine
typed past boundary and verified that a compatible relabeling of that typed
edge still admits.  Thus boundary inclusion did not break the intended label
covariance.

The claim scope is now correct.  The source comment, theorem and opening
ledger say only that compatible element relabelings are quotiented **within
one supplied filtration**.  They explicitly deny that this proves gauge
equivalence among all construction filtrations.  An alternative
`Lambda3 -> diamond4` filtration still rejects, as it should under the supplied
`Ext(C)` and as the prose now acknowledges.

No new ontology/locality blocker was found for the candidate finite theorem:

> Holding one supplied finite filtration, its typed owner-safe extension
> grammar, one record network and one interval action fixed, at least three
> inequivalent positive projective kernels remain possible.  The action alone
> therefore does not select the kernel.

This closes the focused D17 ontology review at that conditional scope.  It
does not solve the full interacting-click-law problem: the filtration,
grammar, kernel, record commit and deterministic continuation remain supplied,
and equivalence or sewing among different construction filtrations remains
open.

## Frozen reproduction

I copied D13, D14, D16, the first D17 executable and the integrated D17
executable into a clean `/tmp` tree.  Normal and optimized Python both pass
`40/40`, produce identical stdout hashes, and regenerate a packet byte-
identical to the primary packet.

```text
checks                    40/40 normal and -O
source SHA-256             5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57
packet SHA-256             a9c08c3b5702dce8726f2b2b355b98398f227085ced61eedda98207d3018fa00
semantic SHA-256           bf465b07380b96350afb929ba661fe4309b002cfcb5142b9a495876b22a92987
normal/-O stdout SHA-256   b8593b3aa3f012243455904f407a2822b3e866b4ddf9a8554b6a0dc752df8398
D14 dependency             e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16 dependency             861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
first D17 dependency       305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
```

The receipt reproduces exactly.  Its check count, source, packet, semantic,
stdout and dependency hashes are correct.  The explicit count and semantic
guards remain active under `-O`.

## Focused hostile results

```text
compatible relabel of declared marked edge admits           True
joint keys for original/relabelled edge equal               True

isomorphic chain child with new-minimum embedding admits    False
joint keys for maximal/new-minimum embeddings equal         False

forged child future BoundaryPort admits                     False
forged child past BoundaryPort admits                       False
forged parent BoundaryPort admits                           False
typed-boundary compatible relabel admits                    True

alternate Lambda3 -> same diamond filtration admits         False
```

These results independently reproduce the two new built-in controls and add
past-boundary, parent-boundary and typed-boundary covariance attacks.

## Finding ledger

```text
R5-1 PASS  Joint canonicalization preserves the marked parent embedding.
R5-2 PASS  Compatible old-element relabelings of a declared embedding admit.
R5-3 PASS  An isomorphic endpoint reached by an undeclared new-element
           embedding rejects.
R5-4 PASS  Parent and child D16 past/future boundary metadata are included in
           the declaration key; forged metadata rejects.
R5-5 PASS  Boundary-aware joint keys remain covariant under a compatible
           relabeling of the marked edge.
R5-6 PASS  The prose distinguishes label covariance within a supplied
           filtration from construction-filtration gauge equivalence.
R5-7 PASS  The alternative Lambda3-to-diamond filtration remains outside the
           supplied grammar and is described as an open quotient/sewing issue.
R5-8 PASS  Prior owner, collar, memory, carrier and bidirectional-join repairs
           remain present and load-bearing.
R5-9 PASS  Supplied-versus-derived and absent geometry/time ceilings remain
           explicit.
R5-10 NOTE The theorem status line still mentions round 3; this is editorial
           and does not affect the result.
```

## 1. Why a joint edge key was necessary

Separately canonicalizing parent and child orders loses which child elements
are the image of the parent.  Two extension edges may have isomorphic parent
orders and isomorphic child orders while differing in the distinguished new
element.  They are not the same marked extension.

The chain example makes this exact.  The declared edge is

```text
chain2 -> chain3 by adding a new maximal element.
```

An alternative child has the same unlabeled `chain3` order but obtains it by
adding a new minimal element:

```text
new < old_0 < old_1.
```

The parent and child endpoint isomorphism classes are identical in the two
cases.  The parent embeddings are not.

`canonical_typed_edge_key(parent,child)` now treats child index `n` as the
marked new element.  It enumerates permutations of only the old `n` elements,
applies the same permutation to their copies in the child, and fixes the new
element at index `n`.  Each candidate contains:

```text
typed parent presentation
parent collar key
typed child presentation with marked new element fixed
child collar key.
```

Taking the minimum therefore removes arbitrary labels on the old embedded
elements without forgetting which element was added.

The hostile results are decisive:

```text
key(declared edge) == key(compatibly relabeled edge)
key(declared edge) != key(new-minimum embedding).
```

The first edge admits and the second rejects.  This closes the endpoint-only
canonicalization bypass.

## 2. Compatible label covariance is implemented at the right scope

The built-in relabel control swaps the two old elements in both the chain2
parent and chain3 child while leaving the new child element distinguished.
The resulting relation presentations differ at the matrix level, but the
joint canonical edge keys are equal and admission succeeds.

This is the appropriate covariance for one marked extension in the supplied
filtration.  It says that names attached to the already embedded elements do
not change whether the declared edge exists.

It does not identify every possible choice of which completed-order element
was revealed last.  The theorem now says exactly this:

> Joint canonical marked-edge keys quotient compatible element relabelings
> while preserving the parent embedding and D16 boundary metadata.  This is
> label covariance within the supplied filtration, not yet a quotient over
> every construction filtration of the same completed order.

The source comment likewise says that explicit past insertions are permitted
by this supplied filtration and are not proof of gauge equivalence among
filtrations.  The round-4 opening ledger calls alternate filtrations an open
quotient/sewing problem.  I found no remaining statement in the audited
source, theorem, receipt or ledger claiming that construction order itself
has been proved gauge.

The alternative diamond control confirms the distinction.  Deleting the
diamond's minimal element gives the declared `V3` precursor; deleting its
maximal element gives a valid `Lambda3` precursor.  Both lead to the same
unlabeled completed diamond, but `Lambda3 -> diamond4` rejects because it is a
different supplied filtration edge.  This is no longer an inconsistency or an
overclaim.

## 3. D16 boundary metadata is now load-bearing

A D16 `CausalOrder` contains its relation plus typed `past_boundary` and
`future_boundary` port tuples.  The repaired `typed_presentation_key()`
contains all of them:

```text
flattened relation
(element,kind,owner) for every past boundary port
(element,kind,owner) for every future boundary port
element-owner tuple.
```

Because that presentation is used inside the joint parent-child key, a change
to boundary kind, owner, polarity or endpoint changes the declared edge key.

I repeated the round-4 exploit by adding a foreign-owned future port to the
declared chain3 child.  It now rejects.  A foreign-owned past port on the
minimal chain3 element also rejects.  Adding a foreign past port to the
chain2 parent rejects as well.  These controls show that neither side of the
edge can smuggle unkeyed D16 boundary metadata.

Boundary inclusion also preserves covariance.  I declared a custom
`chain2 -> chain3` edge with a typed past `leg` on the minimal element in both
orders, then consistently relabeled the old elements.  The D16 permutation
moved the boundary element with the relation, the joint canonical key stayed
equal, and the relabeled typed edge admitted.

Thus the repair is not merely a hard rejection of all boundaryful orders.  It
correctly incorporates boundary metadata into the marked-edge isomorphism
class.

## 4. Ownership, joins and collar state remain protected

The round-5 key changes do not weaken the prior admission checks.

Before declaration lookup, `admit()` still requires:

- requested owner, parent collar owner and child collar owner to agree;
- old element owners to be unchanged;
- the new element's actual owner to equal the requested owner;
- the first memory bit to be installed from the first mark and then preserved;
- the child D14 boundary carrier to be the exact next carrier type; and
- all owners touched in either causal direction to have the exact supplied
  join entitlement when more than one component participates.

The joint key then includes the complete parent and child collar keys, which
contain owner, memory and every D14 port's kind, dimension, sealed flag, owner
and record ID.

The previous forged-owner, forged-collar, forged-memory and forged-carrier
attacks therefore remain closed.  The past-insertion join repair also remains:
the touched support uses both `old < new` and `new < old`, so the diamond's
nonmaximal insertion cannot evade ownership inspection merely by having an
empty precursor set.

As before, a join entitlement is supplied symbolic grammar data, not something
selected by the action.  The finite theorem needs only that this data are
explicit and held fixed across the kernel comparison.

## 5. Integrated record/locality status is unchanged

The repair concerns identity of causal extension edges.  The exact D14 facts
from rounds 3 and 4 remain intact:

- all thirteen frozen causal nodes carry the depth-appropriate D14 boundary
  type;
- both branches share that type at each depth;
- the complete three-commit map satisfies `V^dagger V = I`;
- every commit is one-owner, appends a sealed record and emits a live collar;
- D14 composition preserves earlier records exactly;
- the reset Kraus family is complete and changes `Z` while preserving `X,Y`;
  and
- causal path labels remain distinct from intervention-dependent visible
  record labels.

This proves a finite typed compatibility packet.  The causal extension and
D14 state evolution are still coordinated structures rather than one
order-plus-state transition operator.  That ceiling was already accepted for
the nonselection theorem and remains relevant to the larger interacting-click
law investigation.

## 6. Nonselection and supplied-versus-derived scope

Nothing in the marked-edge repair makes the interval action choose a
probability kernel.  With the same action, nodes, typed grammar and record
network fixed, D17 still has the exact positive root weights

```text
equal               (1/2, 1/2)
positive envelope   (9/25, 16/25)
inverse orbit       (2/3, 1/3).
```

All three towers are projective.  The first two pass through the same local
record network, and the inverse-orbit ratio reaches the same records and
causal tower.  The fixed action gives the opposite size-four phases but is not
used to choose among the kernels.

The source, theorem, JSON and receipt continue to state the correct ontology:

| Datum | Status |
|---|---|
| Finite filtration and `Ext(C)` | supplied |
| Element-label quotient within each marked edge | implemented |
| Quotient/sewing across different filtrations | open |
| Branch kernel | supplied |
| Record commit and memory architecture | supplied |
| Deterministic continuation | supplied |
| Interval action | fixed, but nonselecting |
| Action-derived universe law | absent |
| Proper-time sampler | absent |
| Geometry, units, scale, `G`, V9 holdout | absent |

Therefore the candidate result is neither circular nor overclaimed.  It is an
exact counterexample to uniqueness of the measure given the action, at one
explicit finite conditional domain.

## Gate disposition

```text
H0  PASS          state, orbit and action factors remain explicit.
H1  PASS/PARTIAL  finite orbit/groupoid ratio passes on the frozen pair.
H2  PASS          finite one-owner D14 records and interference witness.
H3  PASS          Born weights applied once.
H4  PASS          positive normalized finite record partitions.
H5  PASS          actual induced causal cylinders and supplied finite-depth
                  continuation schema.
H6  PASS/PARTIAL  shared D14 carrier, two positive record packets and reset;
                  no universal local order-plus-state dynamics.
H7  PASS          fixed action/domain/grammar/network admit distinct kernels.
H8  PASS          at finite supplied-grammar scope: embedding, owner, D16
                  boundary, collar, memory, carrier and join controls pass.
H9  PASS/HONEST   label covariance within the filtration passes; alternative
                  filtration quotient and proper time remain open.
H10 OPEN/HONEST   no geometry, scale, G or V9 prediction.
H11 PASS          focused ontology openings are closed at candidate scope.
```

## Minor editorial note

The theorem status line still reads “awaiting focused round-3 closure.”  The
substance is current and correctly narrowed, but the status should be updated
when the review ledger is closed.

The dead helper `canonical_typed_key()` independently canonicalizes a single
node and is no longer used by admission.  Removing or clearly labeling it as a
node-only utility would reduce the chance of a future regression to separate
endpoint keying.  It is not load-bearing in this revision.

## Final verdict

**PASS AT THE FINITE SUPPLIED-FILTRATION NONSELECTION SCOPE.**  The joint
marked-edge key closes the embedding bypass; D16 past/future boundary metadata
are now protected; and compatible typed relabelings still admit.  The prose
accurately distinguishes label covariance from construction-order gauge and
keeps alternate filtrations open.

The result that closes is conditional nonselection, not a final universe law:
the action does not uniquely determine the kernel even after a finite typed
filtration and local record network are supplied.  Selection of the
filtration, grammar, commit, kernel, continuation, proper time and geometry
remains outside D17.
