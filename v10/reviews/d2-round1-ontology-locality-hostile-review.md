# D2 hostile review, round 1: ontology, locality, and category scope

**Referee:** independent hostile ontology/locality audit  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**

## Frozen artifacts reviewed

- `v10/note-d2-primitive-carrier-amalgamation.md`
- `v10/code/d2_marked_diamond_amalgamation_exact.py`
- `v10/relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md`

Hashes executed in this review:

```text
33bc4c17a6b91e45e03c71416090231b7fca1f2b78698e733e7c2282259de58f  note-d2-primitive-carrier-amalgamation.md
347458cd9806b015ba278d9f912dd6d459a999285873d44fd513c78a861e2831  d2_marked_diamond_amalgamation_exact.py
3fddcfba28d9dacf6b0038ea3693bdffb2cd128c3d8705648904fe3ada33ff19  relativistic-isp-v10-paper3-diamond-amalgamation-is-composition-not-carrier-birth.md
```

The receipt reproduces **20/20** exact checks. The finite graph and support-set
calculations are internally consistent. The revision is required because the
paper repeatedly interprets those unmarked incidence calculations as a typed
sealed-diamond amalgamation theorem and as a record-carrier no-go. The receipt
does not yet contain the ontology needed for either interpretation.

## Major findings

### M1 — The support hypergraph is not shown to represent a sealed-diamond interface

The executable `SupportSystem` contains only:

```text
vertices : finite set of strings
supports : finite set of vertex subsets
```

A sealed holonomy diamond, as summarized by the paper itself, additionally
contains lower and upper screens, collars, orientation, transports, a
count/reference or whole-history law, sealing data, and holonomy information.
None of these survives in the D2 object. There is no abstraction map from
sealed diamonds to `SupportSystem`, no theorem that compatible diamond gluing
maps to support-union gluing, and no conservativity result saying that an
incidence pushout reflects physical diamond compatibility.

Two physically incompatible diamonds can therefore have the same D2 support
hypergraph. Conversely, two different diamond amalgams can collapse to the
same D2 object. The support calculation may be a useful obstruction in an
incidence shadow, but it is not yet a faithful diamond theorem.

**Mandatory opening:** choose one of two honest repairs.

1. Downgrade D2 throughout to a theorem about a **finite support-incidence
   surrogate** and state explicitly that transfer, law, screen/collar, seal,
   and holonomy compatibility are not tested; or
2. define an abstraction functor from a finite marked sealed-diamond category
   to the support systems and prove the exact preservation/reflection property
   needed to transport the pushout and no-bootstrap claims.

Until then, the title phrase “diamond amalgamation” is stronger than the
receipt.

### M2 — “Typed” and “marked” fixed-span claims are not executable

The note freezes a span

$$
D_A\xleftarrow{f}I\xrightarrow{g}D_B
$$

with injective mark-preserving legs. The receipt defines no interface object
`I`, no leg dataclass, no port direction/type, no vertex or support marks, and
no provenance. `union_amalgam` assumes that the shared labels have already
been identified. `graph_pushout` accepts a list of vertex-pair
identifications, but it neither validates injectivity nor checks any mark or
support compatibility.

Consequently, the executable supports this conditional statement:

> given already identified labels, union the transported unmarked supports.

It does not support “a supplied finite typed overlap span has a canonical
pushout up to marked isomorphism.” Marks and interface legs are not
load-bearing because they do not exist in the model.

**Mandatory opening:** add a genuinely typed span receipt with:

- a finite interface object;
- explicit left and right injective legs;
- input/output port types;
- mark and stable-provenance data;
- compatibility and rejection rules;
- an incompatible-mark negative control;
- canonical marked-isomorphism, leg-swap, relabeling, and serial-composition
  checks.

Alternatively, remove “typed,” “marked,” and “marked isomorphism” from the
theorem.

### M3 — The construction-order result is only associativity of preidentified union

G5 computes

```text
(A union B) union C == A union (B union C)
```

for systems whose shared vertices already use the same labels. This is exact,
but it is set-union associativity. It does not execute two iterated pushout
diagrams with explicit interfaces, transported legs, compatibility marks, or
potentially different intermediate quotient names.

The paper mostly says “compatible shared-label presentations,” which is the
correct scope. Calling this a general construction-order-gauge theorem for
typed diamond composition overstates the receipt.

**Mandatory opening:** either retain the shared-label union scope explicitly
in every claim or execute a true three-object typed diagram and compare both
iterated pushouts by canonical marked isomorphism.

### M4 — The first-pair theorem is a bare-incidence theorem, not yet a factorized-record theorem

The pair census contains only an edge mask. Its two-vertex boundary law is
fixed to identity: an edgeless pair always remains edgeless. No probability
law, boundary evidence, parent mark, common cause, output port, or factorization
test is represented.

Thus “factorized refusal” in G9 actually means:

> the unique bare two-vertex edgeless state is fixed.

An edgeless pair of record ports need not be physically factorized. It could
retain a boundary likelihood, common-cause mark, unresolved holonomy, or other
record data not represented by the graph. A birth rule depending on data that
survive restriction is outside the census.

The structural proof is valid and useful at its true scope: if all induced
pair restrictions forget every contextual mark and the empty pair is fixed,
strong naturality forbids adding a pair elsewhere. It is not a universal
record-carrier no-bootstrap theorem.

This scope matters especially because D1 already produced a typed example in
which derived eligibility is not natural under restriction. Strong naturality
is an axiom under investigation, not an established physical law.

**Mandatory opening:** rename the gate to `edgeless two-vertex refusal` and
make the theorem explicitly conditional on the bare-graph state space and
strong induced-restriction naturality. If a record-level theorem is desired,
repeat the census with load-bearing boundary/parent/field marks and state which
marks survive restriction.

### M5 — Deterministic covariance does not exhaust symmetric carrier birth

The automorphism result is correct for deterministic set-valued selectors. It
does not rule out a covariant stochastic kernel. On three symmetric ports,

$$
K(\varnothing,\{AB\})
=K(\varnothing,\{AC\})
=K(\varnothing,\{BC\})
=\frac13
$$

is permutation-covariant in law and produces exactly one pair in each
realization without using construction order.

This kernel fails the paper's strong induced-pair naturality if the isolated
two-port law has zero birth probability: its `AB` restriction has edge
probability `1/3`, not zero. That is an informative conflict, not a reason to
omit the stochastic possibility. SHARD's click dynamics is probabilistic, so
law covariance and realization-level symmetry breaking must be distinguished.

**Mandatory opening:** add a stochastic symmetry section. At minimum:

1. exhibit the uniform one-pair kernel as a counterexample to any unqualified
   covariance obstruction;
2. test it against the two restriction ontologies;
3. decide whether stochastic naturality plus isolated-pair refusal extends the
   pair no-go;
4. state whether non-natural but covariant stochastic bridge birth remains a
   live physical route.

Theorem 10.1 may remain, but only with “deterministic” prominent in every
summary.

### M6 — The common-root control has no root or ancestry ontology

G18 begins with one unmarked support `{r,a,b}` and intersects it with `{a,b}`.
The resulting pair is an exact hyperedge shadow. Nothing in `SupportSystem`
states that `r` is a root event, that `a,b` are descendants, or that the
support represents ancestry rather than a simultaneous three-port event.

Section 11's statement that descendants “inherit” the pair is therefore an
interpretation attached to a vertex name. This repeats the annotation problem
found in D1 round 1.

**Mandatory opening:** either rename G18/G19 as a neutral
`three-support restriction control`, or add typed root/parent/descendant marks
and make them survive the appropriate restriction. Do not use the control as
evidence for a root law; it only shows the consequences of two supplied
support projections.

## Minor findings

### m1 — Support conservation is definitional for this chosen amalgam

`union_amalgam` is defined as vertex union plus support union. Proposition 5.1
therefore follows immediately. It proves that this **ordinary support-union
amalgam** creates no exclusive support; it does not prove that every physically
admissible diamond composition must use this amalgam or forbid a generated
composite support.

The paper usually includes “ordinary,” but the distinction should remain in
the abstract and conclusion.

### m2 — The higher-fill family is scoped to a narrow predicate class

The 256-rule census assigns one yes/no triple-addition decision to each bare
pair graph with no input triple. It does not enumerate arbitrary marked
history operators or full closures on states where the triple already exists.
Extensivity and idempotence are implicit in the fill-only ansatz rather than
independently tested on a complete state space.

The two-rule intersection result is exact for this frozen fill-predicate
class. It should not be described as the complete family of higher-support
dynamics.

### m3 — Restriction-semantics separation is a strength

The paper correctly distinguishes intersection/shadow from contained-event
restriction and does not silently switch between them. The connected-path
fill is a valid exact witness that the admitted family changes. What remains
open is which semantics, if either, is induced by sealed-record restriction.

### m4 — Interface-map ambiguity is established only in the bare graph subcase

G6 is a good exact adversary: two embeddings of the same bare two-vertex
interface yield nonisomorphic graphs. It proves that an untyped universal
property does not select its own legs. Typed marks may remove this particular
ambiguity, but then the origin of those marks remains extra input. The paper
states that qualification correctly.

## Findings that pass now

The following incidence-level results are reproducible and defensible:

1. already-identified support systems compose by relabeling-covariant,
   commutative, associative support union;
2. that chosen union adds no support absent from its inputs;
3. empty-interface union is a disjoint coproduct;
4. two bare legal interface matchings can yield nonisomorphic graph quotients;
5. among 4,096 extensive deterministic bare-graph closures through three
   vertices, strong induced-restriction naturality and fixed empty pairs force
   identity;
6. the structural missing-edge restriction proof extends that bare-graph
   result to finite vertex sets;
7. the frozen triple-fill predicate family is nonunique and depends on the
   chosen support restriction;
8. no deterministic invariant family on one transitive three-port orbit
   contains exactly one pair.

## Precise claim ceiling

The strongest current theorem is:

> In the category-like incidence model of finite unmarked support systems,
> supplied shared-label identifications admit a canonical support-union
> amalgam. It is relabeling-covariant and associative as union, and it creates
> no supports beyond transported input supports. Bare interface embeddings are
> not selected by this construction. On bare pair graphs, a deterministic
> extensive closure that is natural under every induced vertex restriction
> and fixes the edgeless two-vertex state is the identity. A restricted class
> of triple-fill predicates remains nonunique and depends on whether supports
> cast intersection shadows.

It is not yet defensible to promote this to:

- a typed or marked sealed-diamond pushout theorem;
- faithful composition of screens, collars, transports, laws, seals, or
  holonomies;
- a universal record-carrier no-bootstrap theorem;
- a stochastic symmetry obstruction;
- an ancestry/root inheritance theorem;
- relativistic locality or no-signaling;
- a continuum or marked-profinite result;
- or a final carrier-birth/click law.

## Mandatory opening ledger before round 2

1. **D2-O1 — marked span:** make interface objects, injective legs, port types,
   marks, provenance, and incompatibility rejection executable, or downgrade
   every typed/marked claim.
2. **D2-O2 — diamond abstraction:** define the relationship between the
   support-incidence surrogate and sealed diamonds; state exactly which
   physical structures are forgotten and which conclusions survive.
3. **D2-O3 — true iterated span:** execute both parenthesizations of one typed
   three-object diagram rather than relying only on preidentified set union.
4. **D2-O4 — bare-state scope:** replace “factorized refusal” by the actual
   edgeless-pair axiom, or enrich the closure census with physical marks/laws.
5. **D2-O5 — stochastic selector:** classify the uniform random one-pair rule
   under covariance and both restriction semantics; distinguish covariance of
   the kernel from invariance of each realized output.
6. **D2-O6 — typed ancestry:** make root/parent/descendant data load-bearing or
   rename the common-root control as neutral hyperedge restriction.

## Final recommendation

The negative research direction is promising, and the paper's central warning
is correct: a universal construction cannot choose unspecified input legs.
But Paper 3 should not yet be frozen as a sealed-diamond theorem.

After the mandatory openings, one of two outcomes will be publishable:

- a stronger typed marked-span theorem with an explicit, honestly lossy
  diamond abstraction; or
- a clean incidence-level no-go paper whose conclusion is that this surrogate
  cannot derive carrier birth.

Either outcome preserves the important upstream lesson. The current draft
mixes those two levels and therefore requires major revision.
