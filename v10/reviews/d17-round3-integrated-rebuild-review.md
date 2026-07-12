# D17 hostile review, round 3: integrated clean-room rebuild

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-11  
**Integrated-packet verdict:** **MAJOR REVISION**  
**Finite fixed-action kernel-nonselection theorem:** **PASS**

The integrated executable is exactly reproducible and its finite arithmetic is
correct.  Normal and optimized Python pass 32/32 with identical stdout and all
receipt hashes.  An independent reconstruction extends the causal node map to
depth 12, verifies every induced edge, reproduces all three projective kernels,
checks the full record-network isometry and reset completeness, and matches all
three normalized D14 record tables to the causal towers through depth three.

The proposed owner-safe integrated grammar does not survive hostile controls.
It rejects a consistently relabeled copy of an admitted edge, accepts forged
children whose owner, memory or carrier disagree with the declaration, and
allows a past-directed two-owner join without entitlement.  The reset also
produces visible history `100`, for which the supposedly complete causal node
map has no node.  These failures expose a remaining conflation between causal
path marks and visible record marks and show that the growth metadata and D14
record process are matched by duplicated labels rather than composed into one
typed transition law.

The narrow result remains secure: one fixed action and one supplied finite
causal tree admit inequivalent positive kernels.  What fails round-three
closure is the stronger claim that the executable now supplies a
gauge-independent, owner-admitted, intervention-stable causal-history record
packet.

## 1. Reproduction and hashes

The following were repeated independently:

```bash
python3 v10/code/d17_integrated_causal_history_exact.py
python3 -O v10/code/d17_integrated_causal_history_exact.py
python3 v10/code/d17_integrated_causal_history_exact.py | shasum -a 256
python3 -O v10/code/d17_integrated_causal_history_exact.py | shasum -a 256
shasum -a 256 v10/code/d17_integrated_causal_history_exact.py
shasum -a 256 v10/data/d17-integrated-causal-history-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 32/32
SEMANTIC SHA256: 61aac50273a1cc01779b6bfea696fa6195f22bb4e0ce7cf8724da90a331e86bc
SOURCE SHA256: 6c12a6bab7edd24a530e294e6efd2f97484b67dc0f959b82f18b68a15695a422
VERDICT: INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION
```

Normal and `-O` stdout hashes are identical:

```text
663d456e8cc05c4137993fba0834084fee94ec46025ceddf23569d357d003b56
```

The packet and dependency hashes also match exactly:

```text
packet     8791db408ace7751a89f4652eff202484aa867f2d54b6cc29beabcc93282e8aa
D14        e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16        861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
first D17  305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
```

There is no Python `assert` or `__debug__` gate in the integrated source.  The
explicit check-count and semantic-hash guards survive `-O`; output is written
only after they pass.

## 2. Independent causal-tree and action rebuild

I regenerated the node map to depth 12, rather than trusting the frozen depth
six.  It contains one root plus two nodes at every positive depth, for 25 nodes
total.  Every mark is unique, every child has exactly one more element, and
restriction to the old leading elements reproduces its parent relation.

The repaired size-four right branch is exact:

```text
V3 relations             (0<2, 1<2)
relabeled diamond4       (0<2, 1<2, 3<0, 3<1, 3<2)
```

Thus its first three elements induce `V3`; the new element is inserted below
all three.  The left branch reaches `chain4`, and later nodes on both branches
add one maximal element.  The unique-child construction remains valid through
depth 12 and gives the advertised finite-depth induction.

An independently instantiated `S=N_0` action gives phases `-1` and `+1` on the
size-four chain and diamond leaves.  It evaluates without ambiguity on every
node.  Equal `(1/2,1/2)`, positive-envelope `(9/25,16/25)` and inverse-orbit
`(2/3,1/3)` kernels remain normalized and projective through depth 12.  Their
one/zero non-Markov conditionals are exact.

This confirms the finite action/tree/kernel compatibility.  As the ceiling
states, action values do not select or generate any transition weight.

## 3. Independent record, orbit and reset reconstruction

The owner-local record network has source dimension two and successive target
dimensions `8`, `32` and `128`.  Direct matrix multiplication gives

```text
V_record* V_record = I_2.
```

For each supplied amplitude packet, I normalized the independently generated
record table and compared every entry at depths one, two and three with the
causal tower:

```text
equal packet       000:1/2,  101:1/2
positive packet    000:9/25, 101:16/25
inverse orbit      000:2/3,  101:1/3
```

All comparisons pass.  Exhaustive automorphism counts are `1` for `chain4`
and `2` for the diamond; labeled orbit sizes `24` and `12` therefore give the
same normalized `(2/3,1/3)` ratio.  Orbit arithmetic is no longer a detached
number table.

For the two reset morphisms, the independent Kraus sum is exactly

```text
K_0* K_0 + K_1* K_1 = I_32.
```

The equal packet changes from support `000/101` to `000/100`, with one-half on
each.  Prior sealed records remain unchanged.  Thus the finite record and
memory-deletion mathematics is correct.

## 4. Relabeling covariance fails in `Ext(C)`

Declared edges are keyed by:

```text
(parent marks, child marks, raw parent relation, raw child relation).
```

This is a labeled matrix key, not an isomorphism-class or equivariant edge
key.  I took the admitted `chain2 -> chain3` edge and consistently permuted its
old two elements:

```text
parent old->new = (1,0)
child  old->new = (1,0,2).
```

The permuted child still has the permuted parent as an induced leading
suborder.  Nevertheless:

```text
original edge  -> admitted
relabeled edge -> ValueError: absent from supplied Ext(C)
```

The action is relabeling-invariant, but the supplied growth grammar is not.
This is incompatible with reading the nodes as unlabeled causal histories or
construction labels as gauge.  A choice of one representative could be a
computational gauge, but then admission must canonicalize both orders and
transport boundaries/owners, or prove that every relabeling gives the same
quotient law.  The current leaf-level automorphism count does not repair
edge-level noncovariance.

## 5. Owner and collar declarations can be forged

The declaration key omits every typed field of `GrowthNode`: element owners,
collar owner, carried memory value and carrier object.  `admit()` checks that
the caller-supplied `requested_owner` equals the **parent** collar owner, but it
does not validate the child metadata against that owner or against the
declared child.

Starting from the honest admitted `(0,) -> (0,0)` edge, I retained the exact
marks and causal order but changed one child field at a time.  All of the
following were accepted:

```text
child element owners and collar owner = foreign
child carried memory                  = wrong branch bit
child carrier                         = unrelated dimension/type
```

Because the raw marks/order key still matches the declaration, the grammar
cannot distinguish these forged typed children from the declared one.
`GrowthNode` itself also has no constructor invariant requiring
`len(element_owners)==order.n`, matching collar ownership, a binary memory
value, or the declared carrier.

This invalidates the general label “owned extension grammar.”  The particular
frozen nodes are well formed, but the admission layer does not enforce the
properties attributed to it.

## 6. Past-directed joins bypass entitlement

The join check defines touched components only through

```text
old < new,
```

using `actual_precursor`.  The source explicitly permits past insertions
`new < old`, and the relabeled diamond uses exactly such an insertion.  For a
two-owner antichain parent I tested both orientations:

```text
old A,B < new   without entitlement -> rejected
new < old A,B   without entitlement -> accepted
```

The second extension joins the same two owned components but has an empty
precursor set, so the entitlement guard never runs.  Supplying entitlement or
not supplying it produces the same acceptance.

The current production tree has only one owner, so this bug does not alter its
probabilities.  It does defeat the claimed cross-component admission control
and is directly relevant to the past-insertion convention used on the diamond
branch.  Compute touched owners from the full comparable neighborhood of the
new element, or split future and past insertion rules explicitly.

## 7. Reset exits the causal node map

At depth three the causal grammar declares exactly two nodes:

```text
000 -> chain4
101 -> diamond4.
```

The memory reset produces:

```text
000 -> 1/2
100 -> 1/2.
```

There is no `GrowthNode` with marks `(1,0,0)`.  Therefore the reset control is
a valid D14 record intervention but not a history in the declared causal
grammar.  This exposes a semantic collision: the same tuple is being used as
both the identity of a causal-order path and the string of visible record
outcomes.  Resetting a record carrier should not erase or replace the
underlying diamond causal order.

Separate causal node/path identifiers from visible record strings and provide
an observation map.  Under reset, the causal path can remain the diamond while
its visible `Z` record changes.  Projectivity and the deletion control must
then be checked on the appropriate joint or marginal cylinders.

## 8. The growth and D14 state are still only partially composed

Every `GrowthNode` collar contains an `Obj` structurally equal to the record
network's initial memory port; I verified that equality for all nodes.  That is
a real improvement.  But the collar's Python `memory` integer is never read by
the grammar transition or D14 network.  It is copied forward as metadata and
checked against `marks[0]`; the record circuit independently receives a
two-component amplitude vector.

Likewise, a growth node stores only the dimension-two memory carrier.  It does
not contain the sealed records or live collars emitted by the D14 morphisms:

```text
GrowthNode collar dimension          2
record targets after X,Y,Z commits   8,32,128
```

The D14 network internally preserves its records, but no growth edge has that
network state as source and the child node state as target.  Beyond depth
three the causal tower continues through depths four to six, while no further
record commit realizes the appended marks.  The code demonstrates an exact
probability-table isomorphism through depth three, not yet one composed typed
growth/record morphism at every edge.

This also explains why the reset can leave the node map: causal and record
marks are joined by equality of table keys rather than by an explicit
observation morphism.

## 9. Validator disposition

The round-two probability-validator defects are repaired:

```text
depth below three in causal_nodes  -> rejects
empty tower                        -> False
non-unit start                     -> False
nonbinary marks                    -> False
negative/unnormalized/projectively inconsistent tables -> False
```

The generated families remain projective at depths beyond the frozen receipt.
The remaining validator failures are in the grammar layer, not
`is_projective_binary`: typed child identity is under-specified, join touching
is orientation-dependent, and declared edges are not relabeling-covariant.

## 10. Finding ledger

```text
I1 MAJOR    Ext(C) rejects a consistently relabeled admitted edge; the
            extension law does not descend to unlabeled histories.
I2 MAJOR    Declared-edge identity omits child owner, collar, memory and
            carrier fields, so forged typed children are admitted.
I3 MAJOR    Past-directed cross-owner joins bypass entitlement because only
            old<new precursors count as touched.
I4 MAJOR    Reset support includes 100, which has no causal node; causal path
            marks and visible record marks are incorrectly identified.
I5 MODERATE Growth collars and D14 record state are not composed edge by edge;
            metadata and amplitudes remain parallel representations.
I6 MODERATE Causal continuation reaches depth six/all finite depths, but D14
            record commits stop at depth three.
I7 MINOR    Network isometry, reset completeness and full packet/tower equality
            are true but stronger than the predicates frozen in several source
            check labels.
```

## 11. Required repair and decision

Preserve the exact candidate subresult that one fixed finite action does not
select a supplied positive kernel.  Its arithmetic and counterexample are
independently confirmed.

Before accepting `INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION` at the stated
owned/unlabeled record scope:

1. canonicalize or equivariantly quotient declared causal edges, including
   transported owner/collar data;
2. make the full typed child packet part of the declaration identity and
   validate every `GrowthNode` invariant;
3. include both predecessors and successors when enforcing join entitlement;
4. distinguish causal path identifiers from visible records so reset remains
   inside a well-defined joint packet;
5. define one edge morphism carrying prior seals and the live collar into each
   child rather than matching separate tables; and
6. either realize later marks by record commits or call them causal path marks,
   not recorded-history cylinders.

**Final verdict: MAJOR REVISION for the integrated packet; PASS for narrow
finite fixed-action kernel nonselection.**  The explicit ceiling—grammar,
kernel and commit supplied rather than action-derived—remains necessary but is
not sufficient to excuse the failed grammar invariants above.
