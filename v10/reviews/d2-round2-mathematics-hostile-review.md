# D2 hostile review round 2 — marked pushout and exact no-bootstrap audit

**Referee:** independent exact-mathematics/category hostile review

**Date:** 2026-07-11

**Verdict:** **PASS WITH MINOR CORRECTIONS**. The round-1 categorical and
marked-ontology defects are repaired. The weak-homomorphism category is
coherent, the quotient construction satisfies the stated universal property,
and all finite no-bootstrap, fill-family, restriction, and stochastic claims
reproduce. Remaining findings concern proof exposition and support-skeleton
wording, not the validity of the scoped results.

## 1. Frozen artifacts and reproduction

Source hashes reviewed:

```text
c1cddaf5bd9785ce73f2fc035852e13c7b2f95c1063a5ec3c3211889f017fc36  v10/note-d2-primitive-carrier-amalgamation.md
3a09225eee20888aea932fab191e4c4f3003654e60bb79ab02585f5b1df37891  v10/code/d2_marked_diamond_amalgamation_exact.py
509ae3821bc90d01bf2a4d378c060d600d5edf700c6af802b07d256b1025df98  v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d2_marked_diamond_amalgamation_exact.py
```

The receipt exited `0` with `RECEIPT: 33/33 exact checks passed`. Two
independent runs produced the same output SHA-256:

```text
6e759b111a5989b1a52953a2062c72a86a527a30d1cbb8f7b59211917eae84ef
```

The AST import audit returns no non-standard-library module. The reproduction
was run with bytecode writing disabled.

## 2. Ambient category audit

The repaired receipt defines the required category explicitly.

An object is a finite support hypergraph whose vertices carry exact typed
provenance marks. A morphism is a total mark-preserving vertex map. For each
source support, an image with at least two distinct vertices must be a target
support; a fully collapsed image may be a singleton. General morphisms may be
noninjective, while supplied interface legs are separately required to be
injective.

These maps form a category:

- the identity preserves every mark and support;
- if a first map collapses a support to one vertex, every composite remains
  collapsed;
- otherwise the first image is a support, so the second morphism either
  collapses it or sends it to a target support.

Thus weak support homomorphisms are closed under composition. Allowing
noninjective general morphisms correctly resolves the round-1 `FinInj`
coproduct counterexample.

## 3. General marked pushout proof

For injective marked legs

$$
A\xleftarrow{f}I\xrightarrow{g}B,
$$

the executable construction takes the tagged disjoint union of `A` and `B`
and identifies `f(i)` with `g(i)`. Injectivity prevents two distinct vertices
on either one side from being collapsed. Mark preservation through the common
interface makes the quotient mark well defined.

Every pushout support is exactly the image of an input support. The canonical
maps are therefore weak homomorphisms and are injective. Given compatible
cocone maps `u:A->X` and `v:B->X`, define

$$
h([a])=u(a),\qquad h([b])=v(b).
$$

Cocone compatibility makes `h` well defined on identified classes. If a
pushout support came from `A`, its image under `h` is the image under `u` of
the corresponding `A` support, and similarly for `B`; hence `h` is a weak
homomorphism. Joint surjectivity of the canonical maps forces uniqueness.

This proves the universal property for every finite target in the frozen
category. The receipt's exhaustive target audit is correctly supplemental,
not the sole proof.

## 4. Exhaustive cocone and empty-coproduct audits

The six-vertex target has two vertices of each of the three relevant mark
classes and every two-vertex support. A compatible cocone is determined by:

- one of two images for the shared collar vertex;
- one of two images for the `A` output;
- one of two images for the `B` output.

Thus there are exactly `2*2*2=8` valid cocones. The receipt exhausts every map
pair and then every candidate mediator; each cocone has exactly one.

For the empty interface, the two singleton inputs have the same mark and the
audit target has one vertex of that mark. Both input maps land on that one
vertex. Their unique mediator collapses the two coproduct vertices, which is a
legal weak homomorphism. This directly closes the round-1 injection-only
objection.

## 5. Marks, leg validation, and interface ambiguity

All quotient vertices carry a mark. Valid interface legs must preserve both
components of the mark and must be injective. The receipt verifies:

- matching ancestry provenance is admitted and conflicting ancestry is
  rejected;
- indistinguishable interface marks permit aligned and crossed embeddings
  with nonisomorphic marked pushouts;
- distinct red/blue interface marks make the aligned matching admissible and
  reject the crossed matching;
- the legacy graph helper rejects noninjective identification lists.

The marked pushout therefore composes a supplied diagram without selecting
that diagram. The map-selection boundary remains real.

## 6. Iterated typed pushouts

The repaired construction performs actual pushouts of the zigzag

$$
A\xleftarrow{}I\xrightarrow{}B\xleftarrow{}J\xrightarrow{}C
$$

in both bracketings. Each intermediate interface leg is a validated marked
map into the preceding pushout. Both results have the same exhaustive marked
signature: the path supports `A-I`, `I-J`, `J-C` with the same ordered mark
multiset. The executed example passes.

More generally, both bracketings are colimits of the same finite zigzag in the
frozen category, so the universal property gives their unique marked
isomorphism. The construction-order-gauge statement is valid for compatible
iterated spans.

## 7. Independent closure and restriction reconstruction

I independently reconstructed the deterministic censuses in Ruby.

### Pair closures

There are

$$
\prod_{m\subseteq E(K_3)}2^{3-|m|}=4096
$$

extensive deterministic maps. Idempotence, all six permutations, and all
two-vertex restrictions leave one rule:

```text
[0,1,2,3,4,5,6,7]
```

The structural all-finite proof from round 1 remains valid.

### Intersection/shadow triple fills

The full `2^8=256` predicate census returns exactly

```text
(0,0,0,0,0,0,0,0)
(0,0,0,0,0,0,0,1)
```

so the receipt now asserts the actual truth tables, not only their counts.

### Contained-event triple fills

Independent enumeration of covariance, monotonicity, and refusal at mask
`000` gives exactly four rules:

```text
00000000
00000001
00010111  # paths and triangle, in mask order 0,...,7
01111111  # every nonempty pair graph
```

Requiring the pair graph to connect all three vertices removes the last rule
and leaves exactly three. Contained naturality is automatic here because the
new triple disappears on every proper restriction. The reported `4` and `3`
counts are correct.

The connected fill is contained-natural and fails intersection naturality on
a two-edge path. The root-shadow versus contained-root control also passes.

## 8. Deterministic and stochastic symmetry

The only pair families fixed by all of `S_3` are the empty family and all
three pairs. Therefore no deterministic covariant selector chooses exactly
one pair.

For a probability law supported on exactly one pair, transitivity forces
equal probabilities and exact normalization gives

$$
P(AB)=P(AC)=P(BC)=\frac13.
$$

Restricting the output law to `AB` leaves the `AB` edge with probability
`1/3`; applying the two-record law after restricting the edgeless input gives
probability zero by factorized refusal. Hence the uniform kernel is covariant
but not strongly projective. The paper correctly treats it as additional
stochastic input and scopes the obstruction to the frozen strong restriction
gate.

## 9. Round-1 disposition

Every mathematical round-1 opening was addressed:

1. weak general morphisms and injective interface legs are separated;
2. typed provenance marks and compatibility are executable;
3. the quotient, canonical maps, and general mediator proof are present;
4. the finite cocone target and empty coproduct are exhausted;
5. true iterated marked pushouts replace shared-label union as the positive
   gauge test;
6. ancestry provenance is load-bearing;
7. exact fill predicates, contained-family counts, and the stochastic kernel
   are executed;
8. the full-diamond claim is downgraded to a marked support-skeleton theorem.

## 10. Minor findings

### [Minor 1] State the category axioms explicitly in the paper

The morphism definition is correct, and composition closure follows by the
two-case argument in Section 2 of this review. The paper immediately calls
the resulting structure a category without stating identity/composition
closure. Add that one-line lemma so the universal-property theorem is fully
self-contained.

### [Minor 2] Make the general associativity argument explicit

Proposition 4.1 claims associativity up to marked isomorphism for compatible
iterated spans. The receipt checks one nontrivial chain, and the claim follows
generally because both bracketings are colimits of the same zigzag. Add this
sentence to the proof rather than leaving the general claim to be inferred
from the example.

### [Minor 3] Keep “diamond” shorthand subordinate to the support-skeleton scope

Sections 3--4 and the nonclaims correctly say the theorem concerns only a
forgetful marked support skeleton, not probability, collar, transport, or
holonomy data. The verdict box and conclusion still say “typed diamond
amalgamation” and “their composition can be canonical.” For claim precision,
say “typed marked-support-skeleton amalgamation” and “their support
skeletons compose canonically.”

## 11. Verdict and claim ceiling

**Round-2 grade: PASS WITH MINOR CORRECTIONS.** No major mathematical or
categorical defect remains.

Accepted claim ceiling:

1. a general finite pushout theorem for supplied injective spans in the frozen
   category of typed marked support skeletons and weak homomorphisms;
2. support conservation, relabeling covariance, exchange symmetry, and
   compatible iterated-span construction-order gauge at that skeleton level;
3. finite unmarked pair no-bootstrap under strong induced restriction;
4. exact intersection and contained-event triple-fill families in the frozen
   three-vertex class;
5. deterministic one-pair symmetry obstruction and failure of the uniform
   stochastic kernel under the frozen strong projectivity/refusal gate;
6. interface-selection, restriction-ontology, and initial-root boundaries.

Not accepted:

- a pushout theorem for full sealed-diamond probability, screen, collar,
  transport, or holonomy data;
- derivation of an interface, new carrier, initial root, bridge sector, or
  event domain;
- a click rate, outcome law, transfer kernel, relativistic locality,
  no-signaling, quantum dynamics, geometry, continuum, or profinite theorem.

## 12. Final correction addendum

The authors applied all three round-2 minor corrections and the requested
ontology-scope clarifications. I verified the live artifacts.

1. Paper 3 now states and proves closure of identities and composition for the
   weak marked-support homomorphisms before invoking the category.
2. The general iterated-pushout statement now explicitly observes that both
   bracketings are colimits of the same zigzag and invokes colimit uniqueness;
   the executable chain is correctly described as an implementation witness.
3. The abstract, verdict, claims, and conclusion now consistently say
   marked-support or support-skeleton amalgamation. The final conclusion uses
   the precise phrase that the diamonds' **support incidence** composes
   canonically, while extension to full probability/collar/transport laws is a
   separate theorem.
4. “Factorized refusal” has been replaced where needed by the actual frozen
   axiom: an edgeless two-record support skeleton remains edgeless.
5. The no-bootstrap consequence is explicitly qualified as holding under the
   frozen support-skeleton axioms.
6. The note and paper now state the path-measure fork: if a full variable
   marked-history measure is primitive, it already supplies the candidate
   event domain and conditional next-event law; D2 is a derivation question
   only for the stronger SHARD program.

Final source hashes:

```text
edd7c62e5424ed4143f219432758489f2c1bf40f9310fd9b82d88f6cd82975a1  v10/note-d2-primitive-carrier-amalgamation.md
bf8e9a749dc961978263fb787ac059567467890f204d5a9b1e39bf94235300e8  v10/code/d2_marked_diamond_amalgamation_exact.py
ee6a4c4bb4b24dfcb84f0bc6da0b43fae4643db6e861559d7441b4e435eeb490  v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

The final receipt remains `33/33`. Two executions have identical output
SHA-256:

```text
4163c3be7450c2510d62ebe241011c8c96e098b3be7f9e083d561c2c1fa27559
```

**Final verdict after correction: PASS at the claim ceiling in Section 11.**
There are no outstanding mathematical or categorical corrections from this
referee.
