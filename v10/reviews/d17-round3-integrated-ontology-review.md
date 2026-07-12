# D17 round-3 integrated ontology/locality hostile review

**Date:** 2026-07-11  
**Referee stream:** integrated causal ontology, locality and claim scope  
**Candidate result:** `INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION`  
**Verdict:** **MAJOR REVISION — NARROW NONSELECTION SURVIVES; H8 DOES NOT**

## Decision

The new executable is a substantial integration repair.  Every positive
probability cylinder through depth six is now assigned an actual finite
strict order.  Every displayed edge preserves the parent's induced order and
adds exactly one element.  The formerly missing `V3 -> diamond4` edge exists
after relabeling the diamond.  The fixed interval action is evaluated on every
node.  Three positive projective kernels use the same node set and grammar.
The causal collars and D14 network share the same one-owner binary carrier
type, and both positive boundary packets pass through the same three-record
network.  Sealed records are durable and a local memory reset changes `Z`.

The central nonselection result survives hostile attack:

> A supplied finite causal skeleton, fixed interval action, supplied record
> network and supplied extension grammar remain compatible with inequivalent
> positive kernels.  Therefore the action alone does not select the kernel.

That result is exact.  The candidate should not close in this revision,
because the advertised ownership/join grammar has three executable bypasses:

1. `admit()` checks the caller's `requested_owner`, but never checks the new
   element's owner recorded in `child.element_owners`;
2. the declared-edge key omits owners and collar data, so a declared order
   edge remains admitted after replacing the child with a foreign owner or a
   foreign/wrong-memory collar; and
3. the join test looks only at old elements preceding the new element.  A
   past-inserted element preceding two differently owned old elements has an
   empty precursor set and passes without any entitlement.

I reproduced all three bypasses exactly.  They invalidate the general claims
that nonowner extensions reject and cross-component joins require
entitlement.  The frozen main tree happens to use one owner everywhere, so the
bypasses do not change its probabilities or refute nonselection.  They do
block H8 and the claim that the former grammar/locality construction gap is
closed.

A second scope issue concerns “construction order is gauge.”  The diamond
edge inserts the fourth construction label into the causal past of all three
existing elements.  This is a valid induced-suborder refinement of a whole
history, but it is not forward causal birth.  Moreover the supplied grammar
keys exact labeled relation matrices: a simultaneous relabeling of a declared
parent and child is rejected as undeclared.  Thus construction-label gauge
covariance is asserted in a comment, not implemented.  The present object may
be treated as one fixed representative/gauge choice, but it does not prove
that the construction order is physically irrelevant.

Finally, the causal collar and D14 record network are connected by structural
carrier equality and matching mark tables, not by one composed causal-edge
morphism.  The D14 live collars are never consumed by `GrowthGrammar`, and the
classical `Collar.memory` field is not the state output of the preceding D14
commit.  This is enough for a finite compatibility/nonselection witness after
narrowing, but not yet a locally executable interacting click law.

## Frozen reproduction

I copied D13, D14, D16, the first D17 executable and the integrated D17
executable into a clean `/tmp` tree.  Ordinary and optimized Python both pass
`32/32`, produce byte-identical stdout, and regenerate a packet byte-identical
to the primary packet.

```text
checks                    32/32 normal and -O
source SHA-256             6c12a6bab7edd24a530e294e6efd2f97484b67dc0f959b82f18b68a15695a422
packet SHA-256             8791db408ace7751a89f4652eff202484aa867f2d54b6cc29beabcc93282e8aa
semantic SHA-256           61aac50273a1cc01779b6bfea696fa6195f22bb4e0ce7cf8724da90a331e86bc
normal/-O stdout SHA-256   663d456e8cc05c4137993fba0834084fee94ec46025ceddf23569d357d003b56
D14 dependency             e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16 dependency             861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
first D17 dependency       305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
```

The receipt is accurate about these hashes and about the explicit ceiling
that the grammar, kernel and commit are supplied rather than action-derived.
The check-count and semantic-hash guards survive `-O`.

## Hostile counterexample receipt

I imported the clean copied source and constructed variants of already
declared nodes.  The results were:

```text
foreign_new_element_owner_admitted                 True
foreign_wrong_child_collar_admitted                True
past_join_precursor                                ()
two_owner_past_join_without_entitlement_admitted   True
diamond_past_insertion_precursor                    ()
simultaneously_relabelled_declared_edge             rejected as undeclared
node_carriers_equal_network_source                  True
```

These are deterministic exact API results, not philosophical objections.
They follow from the predicates currently used by `GrowthGrammar.admit()`.

## Finding ledger

```text
I1 MAJOR    New-element ownership is not checked.  A child whose new element
            is recorded as foreign passes a declared edge under a local
            requested_owner.
I2 MAJOR    The edge declaration omits typed ownership/collar state.  A child
            with a foreign owner, wrong memory, or foreign collar can reuse the
            same declared order edge.
I3 MAJOR    Past insertion bypasses join admission because touched owners are
            computed only from old -> new precursors, not new -> old
            successors or the full incident support.
I4 MAJOR    Construction-order gauge is not demonstrated: Ext is keyed by
            labeled matrices and rejects a consistently relabeled copy of a
            declared edge.
I5 MODERATE Causal collars and D14 commits are synchronized by type, marks and
            probabilities but are not one composed transition; D14 live
            collars never license the next causal extension.
I6 MODERATE Collar memory is repeated as node metadata.  Early edges do not
            obtain it as the output of a local transition, so “carried” is
            partly declarative.
I7 MINOR    The all-depth statement is a parameterized finite schema, not one
            frozen infinite grammar.  This is enough for finite-cylinder
            induction if stated that way.
I8 PASS     Every frozen cylinder through depth six is an actual induced
            one-element order refinement.
I9 PASS     The supplied D14 commits are single-owner, isometric on the two
            branches, emit live ports, and preserve all earlier seals.
I10 PASS    Three positive kernels are projective and remain inequivalent with
            the action, nodes, grammar and record network fixed.
I11 PASS    Supplied-vs-derived, clock, geometry, scale and G ceilings are
            stated honestly.
```

## 1. Every frozen cylinder is now a real order refinement

The source constructs thirteen nodes: one root plus two nodes at each visible
depth one through six.  The mapping is explicit:

```text
()          root1
(0)         chain2
(1)         antichain2
(0,0)       chain3
(1,0)       V3
(0,0,0)     chain4
(1,0,1)     relabeled diamond4
later       one maximal element appended to each branch
```

For every nonroot node, the child has one more element and its upper-left old
relation equals the parent's full relation.  Since `CausalOrder` validates
irreflexivity, asymmetry and transitive closure, each displayed edge is a
genuine induced one-element refinement.  This closes the round-2 defect in
which only two transitions had order witnesses.

The second size-four leaf deserves exact wording.  In the standard diamond,
the new labeling permutation sends the old minimal element to label `3`.
Consequently the first three labels form exactly `V3`, and adding label `3`
produces relations

```text
3 < 0, 3 < 1, 3 < 2, 0 < 2, 1 < 2.
```

Thus `V3` is indeed the induced restriction obtained by deleting element 3.
No order-theoretic error remains there.

The later `add_maximal()` rule is also exact.  For an arbitrary requested
finite depth it appends a new maximal element above every old element.  The
projective probabilities persist on the unique child, so the displayed rule
supports an induction over arbitrary finite truncation depth.

Two qualifications are required:

- The receipt freezes and checks depths one through six.  “All finite depth”
  is a schema generated by calling `causal_nodes(max_depth)` with larger
  values, not one stored infinite grammar.
- “Extension” here means induced-set refinement, not necessarily a future
  birth.  The diamond edge is explicitly a past insertion.

These do not defeat the finite nonselection theorem.  They matter for the
claim that this is a locally generative click law.

## 2. Construction-order gauge and past insertion

Lines 103–106 acknowledge that an added construction label may lie in the
causal past of old labels and state that construction order is gauge.  The
first half is implemented; the second is not proved.

A whole-history cylinder can certainly be refined by revealing an element
anywhere in the partial order.  On that interpretation, adding the diamond's
minimal element last is not a physical event appearing backward in time.  It
is merely a bookkeeping refinement of a history that was already whole.

But that interpretation has two consequences:

1. the extension sequence is not a local proper-time evolution or a physical
   sequence of births; and
2. predictions and admission must be invariant under the arbitrary
   construction labels, or the source must explicitly declare a gauge fixing.

The grammar currently uses

```text
(parent marks, child marks, parent relation matrix, child relation matrix)
```

as its declaration key.  Relation matrices are labeled objects.  I applied a
consistent permutation to the chain2 parent and chain3 child while keeping the
new element last.  The relabeled pair is still an induced one-element edge and
is isomorphic to the declared edge, but `admit()` rejects it because its exact
matrix key is absent from `declared_edges`.

Therefore D16 action covariance does not make the D17 grammar covariant.  The
present grammar can be read as a fixed representative or gauge choice, but no
canonicalization, orbit quotient, Faddeev-like weighting, or independence
test shows that another representative gives the same `Ext`, memory or
probabilities.

Required wording until repaired:

> The finite witness uses one supplied labeled construction representative.
> It allows nonmaximal induced refinements and does not interpret construction
> depth as physical time.

Do not say that construction order **is** gauge as an established result.
Either canonicalize the order/edge key and test simultaneous relabelings, or
state that the executable fixes a construction gauge whose physical
independence remains to be proved.

## 3. Ownership admission has an exact bypass

`GrowthGrammar.admit()` first checks

```text
requested_owner == parent.collar.owner.
```

This proves only that the caller supplied the expected string.  The method
never checks

```text
child.element_owners[new] == requested_owner.
```

I replaced the owner of the new element on the already declared
`chain2 -> chain3` edge with `foreign-cell`, while leaving the requested owner
as `history-cell`.  The edge was admitted.

The same problem occurs at the collar.  The declared-edge key contains marks
and order matrices only.  It omits:

- `parent.element_owners` and `child.element_owners`;
- parent and child collar owners;
- collar carrier kind/dimension/owner; and
- the collar memory transition.

I replaced the declared child with a node having collar owner `foreign-cell`
and the wrong memory bit.  Because its marks and order were unchanged, it
reused the declared edge and was admitted under the parent's owner.

This means the source check “extension by a nonowner rejects” tests only a
foreign **request argument**, not a foreign extension.  It does not establish
the typed ownership property claimed by the ledger and theorem.

At minimum, `GrowthNode` and `admit()` need to enforce:

```text
len(element_owners) == order.n
new element owner == requested owner == parent live-collar owner
child collar owner == the declared output owner
child carrier == the declared D14 boundary type
child memory == the licensed transition output
typed parent/child node data are part of the declaration
```

The negative control must mutate the actual child owner and collar, not merely
the caller's owner argument.

## 4. Past insertion bypasses the join entitlement

Join admission computes

```text
precursor = {old i : old_i < new}
touched = owners(precursor).
```

This is sufficient only when the new element is a future/maximal addition.  A
past insertion can relate to old elements entirely in the opposite direction,
`new < old_i`.  Its precursor set is then empty even though it joins several
old owned components.

The integrated diamond demonstrates the orientation issue: its newly revealed
element is below all three old elements, and `actual_precursor()` returns the
empty tuple.  All those elements happen to share `history-cell`, so the frozen
branch is harmless.

The general H8 claim fails.  I constructed a two-element antichain owned by
`A` and `B`, then inserted a new `A` element below both old elements:

```text
new < old_A
new < old_B.
```

With `declared=False` and no join entitlement, `GrowthGrammar.admit()` returned
`True`.  The source's existing join control tests only the opposite orientation
`old_A < new` and `old_B < new`, so it misses this counterexample.

If nonmaximal refinements remain allowed, touched support must include both
directions—or, better, the exact typed boundary/cover relations used by the
local extension—and the grammar must demand entitlement whenever more than
one owner participates.  Add explicit future-join and past-join negative
controls.

This is not a cosmetic validator defect.  Preventing an unlicensed connection
of previously disconnected record components is one of the central physical
questions that motivated the investigation.

## 5. Collar memory and the D14 connection

The integration is stronger than round 2.  Every `GrowthNode` collar contains
an `Obj` with one port

```text
Port("causal-boundary-memory", 2, owner="history-cell"),
```

and the D14 record network starts from a structurally equal object.  I checked
that every node's `collar.carrier == net1.source`.  The classical collar memory
also equals the first branch mark on every nonroot frozen node.  Thus the two
constructions no longer use unrelated carrier types.

The D14 network then performs three owner-local commits:

```text
X = boundary memory
Y = supplied constant 0
Z = boundary memory.
```

For the equal amplitudes it produces exactly the causal tower's
`000/101` table.  For the second amplitudes it produces exactly
`(9/25,16/25)`.  The inverse-orbit amplitude ratio also reaches the same
record labels.  This is a valid shared-type, shared-label, shared-weight
compatibility packet.

It is not yet a single composed causal transition system:

- `GrowthNode.collar` is a D17 dataclass, while the emitted D14 live collars
  are separate `Port` objects.
- `GrowthGrammar.admit()` reads the D17 collar and never consumes or verifies
  a live collar emitted by `commit-X`, `commit-Y` or `commit-Z`.
- The integer `collar.memory` is populated manually on the early nodes and
  copied as metadata later; it is not obtained by applying a D14 morphism to
  the parent boundary state.
- `causal_tower()` and `record_table()` are computed independently and then
  compared by expected values.  There is no combined order-plus-boundary
  state or edge morphism whose marginal yields both tables.

So the word “integrated” is defensible as a finite pullback/correspondence
witness, but not yet as an executable local click law.  The next repair should
make an admitted extension consume the actual live D14 collar and return the
child order, child boundary memory and new sealed record in one typed result.

## 6. Commit locality, durability and reset

Within the D14 algebra, the commit construction passes.

All source and target ports have the one explicit owner `history-cell`; no
primitive commit mixes owners.  Each `append_local_record()` copies either the
live memory bit or the fixed local bit into one fresh sealed record and emits a
two-valued live collar.  Its matrix has one unit entry per input basis column,
so the map is an isometry.  The three-record composite maps the two input basis
states to orthogonal outputs.

Durability is stronger than a record-name check.  D14's `Mor` constructor
infers a sealed-port correspondence and rejects any nonzero matrix entry that
changes an existing sealed value.  Composition carries those correspondences
forward.  The final target contains record IDs `X,Y,Z` in order, and all prior
seals are protected.  The exact local finite durability claim passes.

The reset channel changes only the first memory port and preserves the sealed
records.  Summing its two branches and then committing `Z` changes support
from

```text
000 / 101
```

to

```text
000 / 100.
```

Thus the next visible record really depends on the carried boundary memory,
and deleting that memory changes the law.  The exact source calls the reset
“CPTP” but does not recheck Kraus completeness locally; the dependency is
hash-pinned to the reviewed D14 construction, where the corresponding reset
algebra is exact.  This is not a blocker.

“Local” here must retain its finite meaning: one declared owner and one
finite boundary carrier.  No metric, light cone, spacelike-separation theorem
or relativistic microcausality condition has been derived.

## 7. Projectivity and kernel nonselection

The three supplied root kernels are

```text
equal               (1/2, 1/2)
positive envelope   (9/25, 16/25)
inverse orbit       (2/3, 1/3).
```

Every entry is positive and normalized.  Every nonroot frozen node has one
declared child, so each parent mass equals its child sum.  All three towers are
projective through depth six, and the deterministic maximal-extension schema
preserves projectivity at every later finite depth.

The first two kernels pass through the same D14 record network exactly.  The
inverse-orbit raw amplitudes normalize to `(2/3,1/3)` on the same sealed
records.  Uniform labeled mass on the frozen pair of size-four isomorphism
classes descends, conditional on that pair, to the same inverse-automorphism
ratio.  These calculations are correct.

The fixed action is evaluated on every node, and its size-four phases remain
`(-1,+1)`.  The action values are not used by `causal_tower()` to choose the
root weights or continuation.  That is the point of the counterexample: the
same supplied action and skeleton admit multiple kernels.

Therefore the nonselection inference does not depend on the ownership bugs.
Even if those validators are repaired, the three frozen positive kernels will
remain possible unless another principle chooses one.  What fails is the
stronger assertion that the current API already supplies a secure typed
locality/join grammar.

## 8. Supplied-versus-derived scope and overclaims

The packet is unusually clear about its ceiling:

```text
extension grammar   supplied
branch kernel       supplied
record commit       supplied
continuation        supplied
action-derived law  not claimed
```

The JSON scope says “owned finite causal extensions and local records;
supplied kernels.”  The theorem says explicitly that no universe law, BDG
packet, continuum geometry, scale, `G` or empirical holdout is present.  No
preferred proper-time sampler is claimed.  These statements pass and must not
be broadened.

Three phrases need correction before closure:

1. “construction order is gauge” is an unproved interpretation; the grammar
   is label-sensitive;
2. “cross-component join rejects without entitlement” holds only for the
   tested future-join orientation and is false for past insertion; and
3. “the integrated packet closes the former causal-tower/grammar/local-memory
   construction gap” is too strong while ownership can be spoofed and the D14
   live collar is not the grammar's consumed collar.

The safe result is:

> One fixed labeled finite representative, one supplied order skeleton and
> one structurally matched finite D14 record network admit several positive
> projective kernels.  This establishes conditional finite kernel
> nonselection, not a derived or relativistically local universe dynamics.

## Gate disposition

```text
H0  PASS          action/state/orbit factors remain separately supplied.
H1  PASS/PARTIAL  labeled conditional ratio and orbit record ratio agree on
                  the frozen pair; no full causal-tree groupoid quotient.
H2  PASS          owner-local finite records and interference witness survive.
H3  PASS          Born weights are taken once from amplitudes.
H4  PASS          displayed recorded partitions are positive and normalized.
H5  PASS          every frozen cylinder through depth six is a real induced
                  order refinement; arbitrary-finite-depth schema supplied.
H6  PASS/PARTIAL  shared boundary type, two positive local record packets and
                  reset pass; no one-step combined causal/D14 morphism.
H7  PASS          fixed action/skeleton/network admit inequivalent kernels.
H8  FAIL          child ownership/collar spoofing and past-join bypass;
                  construction-label gauge covariance absent.
H9  PASS          construction depth is not claimed as proper time, but the
                  past-insertion/gauge wording must be narrowed.
H10 OPEN/HONEST   no geometry, scale, G or V9 prediction.
H11 OPEN          focused ontology closure requires the H8 repairs and a new
                  hostile round.
```

## Required repair

1. Make a typed node declaration include order, element owners, collar owner,
   carrier type and memory transition—not only marks and relation matrices.
2. Validate `GrowthNode` invariants and require the new element's actual owner
   to equal both the requested owner and the live-collar owner.
3. For nonmaximal insertion, compute touched ownership from the complete local
   incident boundary in both causal directions.  Add an exact two-owner
   **past-join** rejection control.
4. Either quotient/canonicalize simultaneous relabelings and test gauge
   covariance, or explicitly call the node labels a fixed construction-gauge
   representative and leave gauge independence open.
5. Replace the parallel D17 `Collar`/D14 live-collar bookkeeping with one typed
   transition that consumes the parent's actual D14 collar and returns the
   child carrier, seal and causal node.
6. Preserve the present ceiling: even after those repairs, the grammar,
   kernel, commit and continuation remain supplied, so the result is
   nonselection rather than an action-derived interacting law.

## Final verdict

**MAJOR REVISION.**  The new packet closes the missing-order-node defect and
secures a meaningful integrated finite **compatibility** witness.  Every
frozen cylinder is an actual induced causal-order refinement; the local D14
records and reset are exact; and fixed-action kernel nonselection is sound.

Do not close D17 yet.  The current grammar admits a foreign-owned declared
child, accepts a foreign/wrong collar, and permits an unentitled two-owner past
join.  Construction-order gauge covariance is also absent, and the D14 live
collar is not yet the collar consumed by causal extension.  These are direct
openings in the locality question, not failures of the nonselection theorem.
