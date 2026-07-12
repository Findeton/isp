# D2 hostile review round 1 — exact mathematics and category audit

**Referee:** independent exact-mathematics/category hostile review

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION**. The finite closure censuses, restriction
counterexamples, map-ambiguity witness, and symmetry theorem reproduce. The
negative carrier-birth conclusions are sound at their stated finite scope.
The positive “typed/marked pushout” theorem is not yet established because the
receipt defines neither marked objects nor the ambient morphism category and
never checks the pushout universal property.

## 1. Frozen artifacts and reproduction

Source hashes reviewed:

```text
33bc4c17a6b91e45e03c71416090231b7fca1f2b78698e733e7c2282259de58f  v10/note-d2-primitive-carrier-amalgamation.md
347458cd9806b015ba278d9f912dd6d459a999285873d44fd513c78a861e2831  v10/code/d2_marked_diamond_amalgamation_exact.py
3fddcfba28d9dacf6b0038ea3693bdffb2cd128c3d8705648904fe3ada33ff19  v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d2_marked_diamond_amalgamation_exact.py
```

The receipt exited `0` with `RECEIPT: 20/20 exact checks passed`. Two
independent runs produced identical SHA-256 output:

```text
8fe0f7e389b429e509770df14f47218334cdd512fafb845daa2587206fb96c1a
```

Inspection confirms that the production file imports only the Python standard
library.

## 2. Independent census reconstruction

I rebuilt both exhaustive searches in Ruby without importing the production
functions.

### 2.1 Pair closures

For each of the eight labeled graphs on three vertices, an extensive output
may be any supergraph. Hence the number of deterministic extensive maps is

$$
\prod_{m\subseteq E(K_3)}2^{3-|m|}
=2^{24-12}
=4096.
$$

The independent enumeration applied idempotence, all six vertex
permutations, and equality of every input/output two-vertex restriction under
the fixed two-vertex identity law. It returned

```text
total   = 4096
passing = 1
rule    = [0,1,2,3,4,5,6,7]
```

Thus the sole survivor is the identity closure.

The paper's structural proof is stronger than the census and is correct. If a
finite closure adds a missing pair `{u,v}`, restricting to `{u,v}` makes that
edge an output of the edgeless two-vertex input. Extensivity and factorized
refusal fix the two-vertex law to identity, giving a contradiction. This
extends the first-pair no-bootstrap statement to any finite vertex set for a
restriction-compatible family of closures.

### 2.2 Three-support predicates

With the pair law fixed, a deterministic extensive rule for an absent triple
has one Boolean decision for each of eight pair masks, hence `2^8=256`
predicates. Independent enumeration of permutation covariance and
intersection/shadow naturality returned exactly

```text
00000000
00000001  # one only at mask 111
```

in mask order `0,...,7`: never fill, or fill only the complete triangle. The
counts and addition totals reproduce exactly:

```text
total=256, passing=2, additions=(0,1)
```

Idempotence is automatic in this parameterization because filling does not
change the pair mask and an already present triple is retained by extensivity.

### 2.3 Symmetric pair families

Independent enumeration found that the only pair masks fixed by all of `S_3`
are `000` and `111`. Therefore a deterministic covariant rule cannot select
exactly one pair from a fully symmetric three-port input. This theorem is
correctly limited to deterministic selection.

## 3. Pushout/isomorphism examples

The fixed shared-label union example is exact:

$$
\{a,i\}\cup_{\{i\}}\{i,b\}
$$

has transported supports `{a,i}` and `{i,b}` only. It contains neither
`{a,b}` nor `{a,i,b}`. The empty-overlap union contains no support.

The interface-map ambiguity example also reproduces independently. For the
aligned matching, the four-vertex output has degree multiset
`(0,1,1,2)`; for the crossed matching it has `(1,1,1,1)`. They are therefore
nonisomorphic. An independent exhaustive canonical labeling gives the paper's
signatures:

```text
aligned = (4, 000011)
crossed = (4, 001100)
```

Swapping the two legs of the fixed aligned diagram yields the same unlabeled
signature. The example validly proves that specifying only the bare interface
cardinality does not select its embeddings.

## 4. Restriction-semantics audit

The two restriction operations are mathematically distinct and correctly
implemented.

- Intersection/shadow restriction sends each support to its retained
  intersection when at least two vertices remain.
- Contained-event restriction keeps only supports wholly contained in the
  retained set.

For a triple added above a two-edge path, intersection restriction casts the
missing pair shadow and violates pair naturality. Contained-event restriction
drops the triple on every proper pair, so the same fill is invisible there.

The connected masks on three vertices are exactly `011`, `101`, `110`, and
`111`. “Fill iff connected” is permutation-covariant, monotone, idempotent,
and refuses mask `000`. It is contained-natural and not
intersection-natural. “Always fill” is also covariant, monotone, and
contained-natural but fails factorized refusal. All these claims pass.

The inherited-root control is also exact: a supplied `{r,a,b}` support casts
`{a,b}` under intersection restriction and disappears under contained-event
restriction. Neither behavior creates the root.

## 5. Major findings

### [Major 1] The ambient category and universal property are undefined

The paper and note call the construction a pushout, but no morphism class is
defined for `SupportSystem`. Without morphisms there is no categorical
universal property to state. The receipt performs two different concrete
operations:

1. `union_amalgam`, which unions supports after shared vertex labels have
   already been identified;
2. `graph_pushout`, which quotients two simple graphs by a supplied list of
   vertex identifications.

It does not construct interface objects and legs as morphisms, return the two
canonical structure maps, enumerate compatible cocones, or verify existence
and uniqueness of a mediating morphism.

The missing category matters. If all morphisms are required to be injections,
even the claimed empty-interface coproduct generally fails. In the category
of finite sets and injections, take singleton objects `A={a}`, `B={b}`, and
the empty span. The two injective maps `A -> {x}` and `B -> {x}` form a cocone,
but no injective map `{a,b} -> {x}` mediates it. Thus the disjoint union is not
a coproduct in that category.

The support-union quotient can be a pushout in a category with suitable
support-preserving homomorphisms, but that category must be frozen. Required
repair:

1. define objects and morphisms, including whether morphisms may identify
   vertices and how images of supports are treated;
2. define monic/injective interface legs within that ambient category;
3. construct the quotient and its two structure maps;
4. prove that every compatible cocone factors uniquely;
5. specify how degenerate support images, duplicated supports, and marks are
   handled.

Alternatively, replace “pushout” and “universal property” throughout with the
strictly proved phrase “shared-label support-union amalgam.” The current
receipt supports the latter unconditionally.

### [Major 2] The typed/marked theorem exceeds the executable ontology

The note freezes an object `D=(V,E,m)` and requires mark-preserving interface
maps. Proposition 4.1 and Claim 1 speak of a typed span and uniqueness up to
marked isomorphism. The executable `SupportSystem` contains only `vertices`
and `supports`; no marks, types, provenance, interface object, or mark
compatibility appears. `graph_pushout` likewise accepts untyped vertex and
edge lists plus raw identifications.

The paper itself acknowledges that marks “can be added,” which confirms that
they have not been tested. Required repair: either implement compatible marks
and demonstrate that quotient marks are well defined, or scope the positive
result to **unmarked finite support skeletons**. No statement about full sealed
holonomy diamonds follows from the current support skeleton.

These two major findings affect only the positive categorical formulation.
They do not weaken the pair no-bootstrap theorem, the higher-support family,
the restriction-semantic dependence, or the automorphism obstruction.

## 6. Minor findings

### [Minor 1] G0 does not execute the full gate stated in the note

G0 checks only that the source path lies under `v10/code`. It does not inspect
imports or verify the environment variable. Manual inspection confirms that
all imports are standard-library modules, and the reproduction command used
`PYTHONDONTWRITEBYTECODE=1`, so no substantive result fails. The executable
gate label or test should match the preregistered claim.

### [Minor 2] The higher-fill receipt should assert the surviving predicates themselves

`hyperedge_fill_census_intersection` returns only the number of passing laws
and their addition counts. G11 checks `(passing=2, additions=(0,1))`, not the
actual truth tables stated in the paper. Code inspection and independent
enumeration verify that the survivors are exactly “never” and “mask 111
only,” but the production receipt should return and assert those predicates
directly.

### [Minor 3] `graph_pushout` does not validate its claimed legal interface maps

The helper does not check that identification vertices exist, that each leg is
injective, or that types/marks are preserved. The frozen examples themselves
are legal and their conclusions pass. Validation is required before the
routine can witness the general typed-span claim.

## 7. Claims that pass now

The following results are accepted without waiting for the categorical repair:

1. shared-label support union is commutative, relabeling-covariant, and
   associative for the executed compatible presentations;
2. that union contains exactly the transported input supports and creates no
   exclusive cross-support;
3. two supplied legal untyped matchings can produce nonisomorphic graph
   quotients;
4. strong induced-restriction naturality plus two-record factorized refusal
   forbids a first pair edge;
5. exactly two intersection-projective triple-fill predicates survive in the
   frozen unmarked three-vertex class;
6. contained-event and intersection/shadow semantics admit different fill
   families;
7. deterministic covariance forbids selecting one pair from a transitive
   three-port orbit;
8. common-root support is inherited boundary data, not derived birth.

## 8. Verdict and claim ceiling

**Round-1 grade: MAJOR REVISION.** The paper's central negative conclusion—
amalgamation does not derive primitive carrier birth—is supported. The
positive result must be restated or completed categorically.

Claim ceiling before repair:

- exact finite unmarked shared-label support-union composition;
- exact unmarked graph-quotient map ambiguity in the displayed examples;
- the finite pair no-bootstrap theorem;
- the frozen higher-support family and restriction-semantic counterexamples;
- the deterministic three-port symmetry obstruction.

Not yet accepted:

- a pushout theorem in any specified category;
- a typed or marked universal construction;
- uniqueness up to marked isomorphism;
- a theorem for full sealed holonomy diamonds;
- a universal finite amalgamation theorem beyond the displayed support-union
  presentations;
- any carrier-birth, click-rate, outcome, transport, profinite, continuum,
  relativistic, or quantum law.

## 9. Required openings before round 2

1. Freeze the ambient category and prove or retract the universal property.
2. Implement marks/types and compatibility, or explicitly downgrade to
   unmarked support skeletons.
3. Validate the interface legs used by the general quotient helper.
4. Make G11 assert the actual two surviving fill predicates.
5. Align G0's executable check with its stated scope.

