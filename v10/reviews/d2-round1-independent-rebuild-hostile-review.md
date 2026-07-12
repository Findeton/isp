# D2 hostile review, round 1: independent reconstruction and adversary search

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION**

The finite unmarked incidence mathematics is correct and independently
reproducible. The 4,096-map pair census, 256-predicate intersection census,
map-ambiguity example, restriction-semantic split, and deterministic
automorphism obstruction all survive reconstruction.

The positive theorem is presently stated above its executable ontology. The
receipt contains no marks, provenance, typed interface object, mark-preserving
legs, or general marked-span pushout. Its positive gates establish shared-label
support union and one bare simple-graph quotient. They do not yet establish the
paper's “typed/marked pushout up to marked isomorphism.”

A second opening matters directly to the click-law program: deterministic
symmetry obstruction does not exclude a covariant stochastic selector. The
uniform rational kernel on the three pair orbit selects exactly one pair with
probability one while remaining permutation-covariant. It fails the paper's
strong restriction naturality, so the projective pair no-bootstrap theorem
survives and can likely be strengthened to stochastic kernels. But the
symmetry discussion must not present its deterministic alternatives as
exhaustive for a stochastic record law.

## 1. Snapshot and production reproduction

The reviewed artifacts were:

```text
33bc4c17a6b91e45e03c71416090231b7fca1f2b78698e733e7c2282259de58f  v10/note-d2-primitive-carrier-amalgamation.md
347458cd9806b015ba278d9f912dd6d459a999285873d44fd513c78a861e2831  v10/code/d2_marked_diamond_amalgamation_exact.py
3fddcfba28d9dacf6b0038ea3693bdffb2cd128c3d8705648904fe3ada33ff19  v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d2_marked_diamond_amalgamation_exact.py
```

Two runs exited zero and produced byte-identical output:

```text
8fe0f7e389b429e509770df14f47218334cdd512fafb845daa2587206fb96c1a
```

The receipt reports **20/20 exact checks**.

## 2. Independent rebuild

I wrote a separate Ruby implementation importing no production helper. The
final scratch implementation used in this review had SHA-256

```text
599a2390b4636c196073e4eb75a68ff87bc39ad961b4e5aa393899938b430d4e
```

It independently implemented:

1. the three-edge permutation action;
2. all 4,096 extensive deterministic pair closures;
3. exact idempotence, covariance, and pair-restriction gates;
4. all 256 absent-triple fill predicates;
5. intersection/shadow naturality;
6. connected-mask and contained-event audits;
7. invariant pair-family enumeration;
8. the two interface-map pushouts;
9. fixed-label support union;
10. intersection versus contained restriction; and
11. a rational stochastic orbit selector.

Independent exact output:

```text
PAIR total=4096 passing=1 identity=true
INTERSECTION fill_total=256 passing=2 addition_sizes=[0,1]
CONNECTED masks=[3,5,6,7]
CONNECTED covariance=true monotone=true contained_natural=true
CONNECTED intersection_failure=true
AUTOMORPHISM invariant_pair_masks=[0,7]
AUTOMORPHISM invariant singleton exists=false
PUSHOUT aligned degrees=[0,1,1,2]
PUSHOUT crossed degrees=[1,1,1,1]
FIXED supports=[{a,i},{i,b}]
FIXED has {a,b}=false; has {a,i,b}=false
RESTRICT intersection(root,ab)={ab}
RESTRICT contained(root,ab)=empty
```

This independently confirms the production arithmetic and finite
combinatorics.

## 3. Fixed-span support union — passes at unmarked scope

For already identified shared label `i`, the two systems

$$
E_A=\{\{a,i\}\},
\qquad
E_B=\{\{i,b\}\}
$$

have transported-support union

$$
E=\{\{a,i\},\{i,b\}\}.
$$

It contains neither `{a,b}` nor `{a,i,b}`. Empty-interface union is a
coproduct with no cross-support. Set union is relabeling-covariant and
associative for compatible shared-label presentations.

These are exact positive results. They show that an already supplied incidence
diagram composes without inventing a new direct hyperedge.

They do not by themselves implement a general typed span.

## 4. Interface-map ambiguity — passes

The aligned matching gives a four-vertex path of length two plus an isolated
vertex, with degree multiset

$$
(0,1,1,2).
$$

The crossed matching gives two disjoint edges, with degree multiset

$$
(1,1,1,1).
$$

Degree multisets already prove the pushouts nonisomorphic, independently of
the production canonical-signature routine. Thus a bare interface together
with the universal pushout property does not select its own embeddings.

The example is deliberately untyped. A port type could forbid one matching,
but that type is additional input rather than output of the pushout.

## 5. Pair-closure census — passes

For a three-edge graph mask `m`, extensivity permits

$$
2^{3-|m|}
$$

outputs. Multiplying over all eight masks gives

$$
2^{12}=4096.
$$

Independent exhaustive enumeration leaves exactly the identity map.

The structural proof is stronger than the census. If a missing edge `{u,v}`
were added, restrict to `{u,v}`. Naturality would require that edge to be
produced by the two-vertex rule on two isolated vertices, contradicting the
frozen refusal. This proof extends to any finite unmarked graph on a fixed
vertex set.

The theorem is conditional on strong shadow-preserving restriction
naturality. It is not an unconditional impossibility of carrier birth.

## 6. Higher-support and restriction censuses — pass

For an absent triple above a three-edge mask there are `2^8=256` deterministic
fill predicates. Under permutation covariance and intersection/shadow
naturality, a triple can be added only when all three pair faces are present.
Exactly two predicates survive:

1. never fill;
2. fill only the complete triangle.

Extensivity and idempotence on the full state space are automatic here: an
already present triple is retained, and filling does not alter the pair mask
on which the predicate depends.

Under contained-event restriction, the triple disappears on every proper
restriction. The connected rule fills exactly masks

```text
3, 5, 6, 7
```

and is covariant, monotone, idempotent, empty-input-refusing, and
contained-natural. It fails intersection naturality on the three two-edge
paths because the filled triple casts the missing pair shadow.

I also exhausted the contained-natural predicates under the paper's stated
covariance, monotonicity, and refusal only at the empty three-record graph.
There are four, with numbers of filled masks

```text
0, 1, 4, 7
```

corresponding to never fill, triangle-only, at-least-two-edges, and
at-least-one-edge thresholds. The paper does not claim an exhaustive contained
count, so this is a strengthening rather than a contradiction. It makes the
contained-family underdetermination sharper.

If “factorized refusal” is strengthened to reject every disconnected pair
graph, the at-least-one-edge rule is removed, while the other three remain.

## 7. Automorphism obstruction — deterministic result passes

The three pair edges form one orbit under `S3`. The only invariant subsets are

$$
\varnothing
\quad\text{and}\quad
\{AB,AC,BC\}.
$$

Therefore no deterministic equivariant output family contains exactly one
pair. This is exact.

It does not cover stochastic kernels; see Major finding 2.

## 8. Major finding 1 — the positive marked theorem is not implemented

The source calls its objects “marked diamonds” and its positive result a
“typed overlap span,” but the executable ontology contains only:

```text
SupportSystem(vertices, supports)
```

There is no:

- mark or provenance field;
- typed interface object;
- explicit left and right interface maps for support systems;
- mark-preservation predicate;
- compatibility rule for marks on identified records;
- marked quotient object;
- marked isomorphism test; or
- general iterated nontrivial-span pushout.

`union_amalgam` is set union for objects whose overlap has already been encoded
by equal vertex labels. `graph_pushout` accepts a list of bare vertex
identifications for simple graphs. It does not validate that the supplied legs
are injective or mark-preserving. The associativity gate is associativity of
shared-label set union, not an executed comparison of two iterated typed
pushout diagrams.

Accordingly, Proposition 4.1 and Claim 1 are presently above the receipt.

**Required repair, option A:** downgrade the positive result everywhere to:

> A supplied finite unmarked support-incidence span, represented by compatible
> shared labels or valid bare vertex identifications, has a canonical
> support-union amalgam at the tested finite scope.

**Required repair, option B:** implement a genuine marked span:

1. typed interface object `I`;
2. explicit injective legs `f,g`;
3. typed vertices/supports and stable provenance;
4. validation of mark compatibility;
5. quotient transport of arbitrary hyperedges and marks;
6. marked canonicalization/isomorphism;
7. leg exchange and relabeling covariance; and
8. a nontrivial iterated-span associativity/path comparison.

The elementary categorical theorem is plausible once the category is defined,
but it is not yet the executed theorem.

## 9. Major finding 2 — covariance permits stochastic one-pair selection

On three indistinguishable ports define the exact rational kernel

$$
K(AB)=K(AC)=K(BC)=\frac13.
$$

It selects exactly one pair with total probability one and is invariant under
every permutation of the ports. It uses neither a serial construction order
nor a distinguishing record mark.

Thus symmetry alone does not force a physical law to return the whole orbit,
return none, choose a higher support, or wait for a mark. Those are the
deterministic alternatives. A covariant stochastic orbit measure is another.

This does **not** defeat Theorem 7.1. Restrict the stochastic output to a fixed
pair such as `AB`. The retained edge has probability `1/3`, whereas the
two-vertex factorized-refusal rule assigns it probability zero. The uniform
kernel therefore fails strong restriction naturality exactly:

$$
\frac13\ne0.
$$

Indeed the structural no-bootstrap proof extends to natural Markov kernels:
if an absent edge had positive output probability, its two-vertex restriction
would have the same positive probability, contradicting the two-record
refusal.

**Required repair:** distinguish the statements explicitly:

1. deterministic covariance alone forbids one-pair selection;
2. stochastic covariance alone allows a uniform orbit selector;
3. strong projectivity plus two-record refusal forbids first-pair birth even
   for a stochastic kernel that casts pair shadows.

This distinction is essential because the desired click law is stochastic.

## 10. Major finding 3 — the receipt is a support-incidence shadow, not a sealed-diamond theorem

The finite support system omits the structures that make a v6 object a sealed
diamond:

- lower and upper screens;
- collars and interface cochains;
- transport maps and holonomy;
- whole-history probability laws;
- seals/outcomes; and
- typed record provenance.

The paper acknowledges that not every sealed diamond is fully represented by
a support hypergraph. Nevertheless its title, abstract, and positive theorem
frequently promote the support-union result as “typed diamond amalgamation.”

The safe statement is that D2 proves an obstruction in the **support-incidence
shadow** of a possible diamond category. Extra record-visible diamond data may
select an interface or bridge sector; if it does, that is precisely the
additional structure D2 concludes is missing.

This scope correction does not weaken the useful no-go. It prevents a finite
bare-hypergraph theorem from being mistaken for a theorem about the full
sealed-holonomy ontology.

## 11. Minor findings

### m1 — injection and span validity are assumed, not checked

`graph_pushout` accepts arbitrary identification pairs. It neither checks that
vertices exist nor that the two interface legs are injective. Invalid input can
collapse same-side vertices even though the paper's theorem excludes such
spans. The static examples are valid, but the executable theorem should enforce
its own hypotheses.

### m2 — the G13 factorized-refusal predicate is tautological

The code computes

```python
all(not is_connected_pair_mask(mask) or mask != 0 for mask in range(8))
```

which is automatically true: a connected three-vertex mask cannot be zero.
The intended check is simply `not is_connected_pair_mask(0)`, preferably with
explicit refusals for the disconnected one-edge masks if component
factorization is intended.

The mathematical result is correct; the gate should state what it actually
tests.

### m3 — idempotence is analytic rather than executable in the fill audit

The triple predicates are automatically idempotent because adding a triple
does not change the pair mask. State this explicitly or add the full
triple-present states to the census. No reported count changes.

### m4 — G0 does not prove the import claim

G0 checks only that the source path lies under `v10/code`. Inspection confirms
the current imports are standard-library modules, but the executable condition
does not enforce that claim.

## 12. Findings that survive unchanged

The following results pass independent hostile reconstruction:

1. shared-label support union is exactly covariant and associative;
2. ordinary union gluing invents no direct exclusive cross-support;
3. the two bare interface matchings yield nonisomorphic graph pushouts;
4. the universal property cannot select its own bare interface legs;
5. all 4,096 deterministic extensive pair closures reduce to identity under
   the frozen strong gates;
6. exactly two intersection-natural triple fill predicates survive;
7. contained-event restriction admits a strictly larger fill family;
8. intersection and contained restriction give different common-root shadows;
9. deterministic covariance forbids selecting one pair from the symmetric
   three-pair orbit; and
10. no-silent closure remains downstream of a supplied carrier proposal.

## 13. Required disposition and claim ceiling

Before a passing review:

1. implement typed marked spans or downgrade the positive theorem to unmarked
   support incidence;
2. separate deterministic symmetry obstruction from stochastic covariance and
   stochastic projectivity;
3. scope every “diamond” conclusion to the support-incidence abstraction;
4. repair or clarify the minor executable gates.

At the current evidence level, the defensible theorem is:

> Given a supplied finite unmarked support-incidence diagram, transported
> support union composes canonically and creates no new direct hyperedge. In
> the unmarked fixed-vertex graph sector, strong restriction naturality plus
> two-record refusal forbids first pair-edge birth. Higher-support filling is
> nonunique and depends on restriction semantics. A deterministic covariant
> rule cannot select one edge from a transitive three-edge orbit.

The evidence does not yet establish:

- a marked or typed diamond pushout theorem;
- an interface proposal law;
- a stochastic carrier-birth kernel;
- a physical choice of restriction ontology;
- a root/bridge-sector nucleation law;
- full sealed-holonomy composition;
- relativistic locality;
- a marked profinite extension; or
- the final interacting click law.

At that claim ceiling the mathematics is strong. The present Paper 3 requires
major revision because its positive ontology and deterministic physical
discussion exceed that ceiling.

