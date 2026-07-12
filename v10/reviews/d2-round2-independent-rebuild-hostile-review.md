# D2 hostile review, round 2: independent marked-pushout reconstruction

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **PASS at the stated finite marked-support scope**

The round-1 categorical and stochastic openings are repaired. I independently
implemented the marked weak-homomorphism category and quotient pushout without
importing production code. The fixed-span object, injective legs, universal
mediator, empty coproduct with a noninjective mediator, iterated pushouts,
typed interface ambiguity, provenance selection, all closure censuses, and the
uniform stochastic obstruction reproduce exactly.

I found no executable counterexample to the finite marked-support theorem.
The live paper now states its claim at the correct level: a marked support
skeleton, not the probability/collar/holonomy content of a sealed diamond. It
also names the two-record axiom as edgeless-pair refusal and qualifies
carrier-birth refusal by that axiom plus strong restriction naturality.

## 1. Frozen round-2 snapshot

```text
edd7c62e5424ed4143f219432758489f2c1bf40f9310fd9b82d88f6cd82975a1  v10/note-d2-primitive-carrier-amalgamation.md
bf8e9a749dc961978263fb787ac059567467890f204d5a9b1e39bf94235300e8  v10/code/d2_marked_diamond_amalgamation_exact.py
98fc7d8d58f13b43a65cc02b04f8e988feb8305093ed24ab8dfec2f822971b23  v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d2_marked_diamond_amalgamation_exact.py
```

Two executions exited zero and produced byte-identical output:

```text
4163c3be7450c2510d62ebe241011c8c96e098b3be7f9e083d561c2c1fa27559
```

The receipt reports **33/33 exact checks**.

## 2. Independent implementations

Two separate Ruby reconstructions imported no production helper.

The marked-category reconstruction had SHA-256:

```text
5271fb96215b69be2fb2c4342704a4bd2465fe11df9c25441c4bfabf65fffc27
```

The closure/restriction/stochastic reconstruction had SHA-256:

```text
599a2390b4636c196073e4eb75a68ff87bc39ad961b4e5aa393899938b430d4e
```

Independent marked output:

```text
TYPED vertices=3 supports=2 canonical legs valid=true
UNIVERSAL valid cocones=8 unique mediator for each=true
COPRODUCT vertices=2 mediator count=1 mediator noninjective=true
ITERATED left/right marked signatures equal=true
AMBIGUITY equal bare marks permit nonisomorphic pushouts=true
MARK_SELECT red/blue aligned valid=true crossed valid=false
```

Independent closure output:

```text
PAIR extensive maps=4096 passing=1 identity=true
INTERSECTION predicates=256 passing=2 addition sizes=[0,1]
CONTAINED covariant monotone empty-refusing=4 sizes=[0,1,4,7]
CONTAINED additionally component-refusing=3
CONNECTED masks=[3,5,6,7]
AUTOMORPHISM invariant pair masks=[0,7]
STOCHASTIC exact weights=[1/3,1/3,1/3]
STOCHASTIC covariant=true strong-projective=false
ROOT intersection shadow={ab}; contained event=empty
```

## 3. The marked-support category is now explicit

The repaired object is a finite colored support hypergraph

$$
(V,E,m),
$$

with one typed provenance mark per vertex. A weak morphism is a total
mark-preserving vertex map whose image of every source support is a target
support whenever at least two distinct image vertices remain. Collapse to a
singleton is allowed. Interface legs are separately required to be injective.

This category choice is load-bearing. Allowing noninjective general morphisms
permits the empty-interface coproduct to mediate arbitrary compatible cocones;
requiring interface legs to be injective prevents one input object from being
collapsed by the gluing diagram.

The definitions are internally consistent and the production validators agree
with the independent implementation.

## 4. Fixed-span marked pushout — pass

For injective mark-preserving legs

$$
A\xleftarrow{f}I\xrightarrow{g}B,
$$

the construction takes the disjoint vertex union, identifies `f(i)` with
`g(i)`, transports every input support, and assigns the common mark to each
quotient class.

The canonical input maps are injective marked homomorphisms. No support is
created except an image of an input support.

The universal proof is correct:

1. a compatible cocone has one common target value for every identified
   quotient class;
2. this defines a mediator on all quotient vertices;
3. every quotient support came from one input, so the mediator preserves it;
4. the two canonical maps are jointly surjective, so the mediator is unique.

Independent exhaustion reproduces all eight valid cocones into the production
six-vertex target and finds one mediator for each. The target is only an
executable sample, but the preceding representative-class proof is general.

## 5. Empty coproduct and noninjective mediator — pass

With empty interface, two one-vertex systems of the same mark produce a
two-vertex coproduct with no cross-support. A one-vertex target of that mark
admits cocone maps from both inputs. The unique mediator collapses both
coproduct vertices to the target vertex.

This exact control confirms why general morphisms cannot all be required to be
injective. It also confirms that empty-interface gluing itself creates no
direct carrier.

## 6. Iterated typed pushouts — pass

The repaired receipt executes both presentations of the marked chain

$$
A\leftarrow I\rightarrow B\leftarrow J\rightarrow C.
$$

The `I` and `J` marks are distinct and the external output marks remain
visible. The two final marked-support objects have equal exhaustive canonical
signatures. Independent construction gives the same result.

This is a genuine quotient-pushout comparison rather than associativity of
already-shared-label set union. It supports construction-order gauge for the
executed compatible diagram. General compatible finite diagrams follow from
the same colimit construction, but the paper correctly keeps the physical
input diagram supplied.

## 7. Typed interface ambiguity and mark selection — pass

When both interface vertices have the same bare collar mark, aligned and
crossed injective legs are legal. Their quotient graphs have different degree
multisets and nonisomorphic marked signatures.

When the vertices carry distinct red/blue marks, the aligned legs preserve
marks and the crossed right leg does not. The validator rejects the crossed
span. Likewise, ancestry mark `root:R1` maps into `R1` ports and not an `R2`
port.

Thus marks can select among spans only when the distinguishing record mark is
already supplied. The pushout does not generate the type or provenance that
makes the selection.

I also attacked the marked helper with a noninjective two-vertex interface
leg; it raises `ValueError` as required.

## 8. Pair closure and higher-support censuses — pass

Independent exhaustive enumeration confirms:

- 4,096 extensive deterministic pair closures;
- exactly one survivor under covariance, idempotence, all pair restrictions,
  and edgeless two-vertex refusal;
- that survivor is identity;
- 256 absent-triple predicates;
- exactly two intersection-natural predicates: never fill and triangle-only;
- four covariant monotone contained-natural predicates refusing the empty
  graph;
- three of those remain when filling is forbidden on every disconnected
  three-vertex pair graph.

The four contained rules have addition counts `0,1,4,7`; the three
component-refusing rules have counts `0,1,4`.

The restriction-ontology conclusion is therefore stronger after repair:
intersection and contained semantics do not merely differ on one hand-picked
rule; their exhaustively admitted finite families differ.

## 9. Deterministic and stochastic symmetry — pass

The deterministic invariant pair families on three indistinguishable ports
are exactly empty and the complete three-pair orbit.

The repaired receipt also represents the unique probability law supported on
exactly one symmetric pair:

$$
P(AB)=P(AC)=P(BC)=\frac13.
$$

This law is exactly covariant and normalized. On restriction to `AB`, it casts
an inherited `AB` edge with probability `1/3`, while the frozen two-vertex
edgeless-refusal law assigns probability zero. It therefore fails strong
restriction naturality.

The distinction is now honest:

- deterministic covariance forbids a one-pair output;
- stochastic covariance permits the uniform orbit measure;
- strong shadow projectivity plus edgeless-pair refusal blocks that stochastic
  first edge.

## 10. Search for remaining executable counterexamples

I attacked:

1. missing and noninjective interface legs;
2. mark-incompatible legs;
3. ancestry-provenance mismatch;
4. support images collapsed to singleton by a mediator;
5. empty-interface cocones with a noninjective mediator;
6. both iterated quotient orders;
7. indistinguishable and distinguishable two-port interfaces;
8. every deterministic pair closure;
9. every intersection fill predicate;
10. every contained fill predicate under the stated finite gates;
11. common-root restriction under both support ontologies; and
12. deterministic and uniform stochastic symmetric pair selection.

No exact counterexample invalidates the implemented finite marked-support
claims.

## 11. Support-skeleton scope — repaired and passed

The live paper now places the finite theorem in the marked support-skeleton
category and explicitly identifies the abstraction from a sealed diamond.

The executed object omits:

- probability/count laws;
- lower and upper screens;
- collar response;
- transport and holonomy;
- seals and outcomes; and
- compatibility of full stochastic histories.

The passing claim is:

> a supplied finite typed span has a canonical pushout in the marked
> support-skeleton category.

It is not a pushout theorem for complete sealed holonomy diamonds. The live
nonclaims and Section 3 state that boundary correctly. Residual uses of
“diamond” are programmatic motivation, not promotion of the receipt.

## 12. Edgeless-pair axiom — repaired and passed

The pair census contains no probabilities. Its two-record axiom is:

> an edgeless two-vertex support skeleton remains edgeless.

Calling this “factorized refusal” would import an unexecuted statistical
interpretation. The current note, theorem, stochastic discussion, claims, and
conclusion instead use `edgeless-pair refusal`. If a probabilistic
factorization bridge is later desired, it still needs a separate theorem
linking the full law to this skeleton.

## 13. Frozen-axiom qualification — repaired and passed

The no-bootstrap result assumes both:

1. strong restriction naturality that preserves pair shadows; and
2. edgeless-pair refusal.

Contained higher-event semantics deliberately weaken the first condition, and
a bridge sector may enlarge the state/event category. The theorem therefore
does not say that carrier birth is impossible in SHARD. It says that first
pair-edge birth is impossible inside the frozen fixed-vertex support-skeleton
closure class.

The live verdict and conclusion retain that qualification. They do not claim
that carrier birth is impossible in SHARD generally.

## 14. Primitive path-measure fork — repaired and passed

The note and paper correctly identify a foundational fork: if a full measure
on variable marked histories is primitive, D2 is no longer deriving the law.

The live paper now introduces a finite or standard measurable history space,
a path measure, the committed-history sigma-algebras, and the existence of a
regular conditional law. Those are the structures needed to interpret
`next`. In general one needs:

- a measurable history/extension space;
- the committed-history filtration or prefix map;
- a candidate extension domain; and
- regular conditional probabilities, up to the usual null-history ambiguity.

At the finite/countable scope intended here these can be supplied without
difficulty. The current formulation also restricts its pointwise statement to
positive-mass committed histories and does not promote a new measure-theoretic
theorem.

## 15. Minor executable observations

1. `contained_connected_fill_audit` still encodes its empty-input refusal as
   `all(not connected(mask) or mask != 0)`. The result is correct but the test
   is tautological for a connected-mask predicate. The exhaustive four/three
   rule censuses now provide the meaningful refusal gates.
2. The universal cocone receipt exhausts one rich finite target, not all
   targets. This is appropriate as an implementation guard because the paper
   gives the general representative-class proof.
3. Typed relabeling covariance and leg-exchange symmetry follow directly from
   the quotient proof; the executable signature tests emphasize iteration and
   ambiguity rather than separately enumerating every typed relabeling.
4. Common-root shadows remain conditional on a supplied ancestry mark. They
   are inherited incidence, not evidence for root creation.

None changes a receipt count or theorem after the scope corrections above.

## 16. Passing claim ceiling

The evidence now establishes:

> In the finite marked support-skeleton category with mark-preserving weak
> homomorphisms and injective interface legs, every supplied compatible span
> has a support-conserving pushout unique up to marked isomorphism. Compatible
> iterated spans compose independently of presentation. The universal property
> does not select its own span. In the unmarked fixed-vertex graph sector,
> strong shadow restriction plus edgeless-pair refusal forbids a first pair
> edge; higher-support fillings remain nonunique and depend on restriction
> semantics. Deterministic symmetry forbids one-pair output, while the uniform
> stochastic selector is covariant but violates the frozen strong restriction
> gate.

It does not establish:

- a pushout of complete sealed-diamond probability/holonomy data;
- a law proposing the interface or carrier;
- a physical selection of intersection versus contained restriction;
- a root/bridge nucleation law;
- an event rate, outcome, or transfer kernel;
- relativistic locality or no-signaling;
- a marked profinite extension; or
- the final interacting click law.

At this ceiling, D2 round 2 passes. The live note and paper now incorporate
the required scope and terminology corrections.
