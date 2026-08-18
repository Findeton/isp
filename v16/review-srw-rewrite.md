# SRW hostile review — relational rewrite, composition, identity, and catalogue

Seat: **R — relational rewrite, category, identity, and catalogue**  
Target: repaired Paper 4 candidate commit
`cd3ad8f61c244ef8703a736bc68cdcbcdb397e30`  
Protocol: `v16/note-srw-hostile-protocol.md`  
Review mode: repository read-only except this assigned report; independent
exact reconstruction in `/private/tmp`; no candidate implementation imported
into the counterfixture  
Grade: **REJECT**

Normalized self-SHA-256:
`44aa1f7bab09cf4d4df30a2737b4a929119978e232180e6329b1037fd17d5f2d`.
This is the SHA-256 of the complete UTF-8 report after replacing only the
64 hexadecimal characters in this field by 64 ASCII zeroes. This convention
allows the report to carry a non-self-referential integrity value in its own
bytes.

## 1. Bottom line

The repaired computation is exact, sealed, reproducible, and useful. I
independently recover the 12-to-2 dictionary census, the distinction between
kinematic support and actual nonzero support, the two different ancestry spans
carried by one anonymous matrix, all four declared fiber dimensions, the
future-sensitive dictionary screens, and the conditional left-inverse result.
The first two registered findings therefore survive, with the finite
declared-future qualification required by the protocol.

The object advertised as the **successor rewrite bundle** does not yet have
the compositional structure needed for that name. `RewriteSpan` is a labelled
source graph, a labelled target graph, a partial vertex-persistence relation,
a set of created internal vertices, and an allowed matrix-entry relation. It
has no interface graph, edge/port persistence morphisms, match into a context,
pushout complement, dangling/gluing conditions, or composition operation. The
paper says that bundle arrows compose, but the source contains no such method
and the battery never compares two decompositions of an overlapping rewrite.

The mandatory new arena exposes the omission exactly. Two locally lawful,
isometric, relabel-covariant creation steps reach the same final graph by two
orders. Every individual step passes the local support/dimension/isometry
surface, including after adding a created two-valued internal degree, but the
two composites disagree: an input at `a` arrives at `c` in one decomposition
and at `b` in the other. A final projector has exact probabilities `1` and
`0`. No declared associator, order record, fusion rule, or overlap law says
which composite is the law. This is the protocol's material failure of overlap
composition, so the third registered finding must be killed rather than
word-repaired. The fourth registered “reciprocal weld” depends on the same
unbuilt bundle and must be demoted to a conditional matrix lemma.

Paper 4 has constructed the kinematic signature of a possible joint successor
law, not the law. It contributes the right type separation—rewrite, ancestry,
fiber choice, and transport cannot be recovered from an anonymous matrix—but
it supplies neither compositional rewrite semantics nor a rule selecting and
coherently composing the typed arrows.

## 2. Frozen-target, chronology, and replay audit

The chronology is unusually important because the first generated candidate
passed symbolic checks while leaking inexact runtime scalar types. I read the
pin, both initial freezes, first refusal, repair freeze, failed verification,
repaired-artifact note, full source, fixture, transcript, receipt, and paper.
The bounded repair added Gaussian-rational runtime enforcement and provenance;
it did not change the scientific fixture, registered outcome vector, or paper.

I recomputed the repaired artifact hashes directly:

| artifact | SHA-256 | result |
|---|---|---|
| `srw_core.py` | `dd902c37375f87185f693f8b1e4b22ba3ddeaf9de5641e5d7d951cbba1d3c585` | PASS |
| `srw_score.py` | `73dfb580b056b4ed2cee511542684bdbe9943633bd2c9888fd4934cd521742f9` | PASS |
| `srw_fixture.json` | `e40650f04c60635e68fd91938dbba201afec6e426c2e1cfaa0b4f4d8dcefd2e3` | PASS |
| transcript | `e52c5573c0c784a83419de368286152302bbbfe02cf0c12fb132bd568f0c8695` | PASS |
| receipt | `c9b036c9d6382bfd8f1402fe5eee39d3a362842b82b1690e28e5a0130a4d5675` | PASS |
| Paper 4 | `f61dde79e5fc0e10db1e5dbe13dec25dceaff9842d5e0c5c06ba2ae90eb4bcae` | PASS |
| repaired-artifact verification | `bb270d86ddb79b9f2dae1f4275f6ce2e5025a32f11b899efb4d18df6046a7eb1` | PASS |

A clean off-artifact replay into a fresh `/private/tmp` directory reproduced
the transcript, receipt, and paper byte-for-byte. The receipt has 37 gates,
27 registered mutants, nine sealed payload components, independent outcome
indices `(2,3,5,6)`, and the four registered findings expected by the pin. The
fixture's result vocabulary gate reports no forbidden result keys. Runtime
provenance reports 213 exact Gaussian-rational values and zero floating
literals in the scorer surface. The repaired verification is off-tree in the
limited artifact-replay sense recorded by the unit; it is not evidence for the
categorical claims attacked below.

I reran nine rewrite-relevant mutants. Each refused before producing result
artifacts:

| mutant | first refusal |
|---|---|
| `dictionary-drop` | `SRW-DICTIONARY-CENSUS` |
| `persistence-spelling` | `SRW-PERSISTENCE-NATURALITY` |
| `graph-probe-row` | `SRW-GRAPH-FUTURE` |
| `support-equality` | `SRW-ACTUAL-SUPPORT` |
| `forbidden-support` | `SRW-FORBIDDEN-SUPPORT` |
| `functor-dimension-type` | `SRW-FIBER-DIMENSIONS` |
| `relabel-break` | `SRW-BUNDLE-NATURALITY` |
| `recurrence-site-drift` | `SRW-RECURRING-LOCALITY` |
| `seal-after-write` | `SRW-PREWRITE-SEALS` |

These checks secure the delivered claims against the mutations the author
registered. They do not cover composition, because no overlap object or
composition gate exists in the battery.

## 3. Type audit: six objects that the word “support” must not merge

| layer | delivered object | status |
|---|---|---|
| source/target relational configuration | `RelGraph(internal, ports, edges)` | declared finite labelled graph; exact object |
| boundary ports | a separate tuple inside each `RelGraph` | typed, but not included in persistence or matrix-entry grammar |
| rewrite span | before/after graphs plus `persists`, `created`, `allowed_entries` | declared labelled before/after datum; not a compositional graph rewrite |
| persistence/ancestry | injective pairs between source and target **internal vertices** | declared semantic relation, not recovered from transport |
| kinematic entry grammar | allowed source-internal/target-internal pairs | possibility relation; an allowed coupling may be zero |
| actual support | nonzero entries of a chosen matrix in chosen bases | dynamical fact at one parameter value; subset of grammar |
| carrier/fiber | `FiberSpec.dimension(graph)` plus separately constructed matrices | conditional on a declared sector/multiplicity/port choice; no global functor object |
| transport | exact rectangular isometry assigned to a typed example | entries are law data; no general assignment on all rewrites |
| history weights | separate circle variables for durable successors | probability-layer data; not part of `RewriteSpan` or `FiberSpec` |

Most importantly, a nonzero matrix entry `(source vertex, target vertex)` is a
transition possibility **across time**. An edge of the target `RelGraph` is a
spatial/relational adjacency **within one configuration**. The fact that a
chosen dictionary lets the same names appear in both does not make these
relations identical.

The concrete source has internal vertices `a,b`, boundary port `p`, and edges
`a-b,b-p`; the target has internal vertices `a',b',c`, port `p`, and edges
`a'-c,c-p`. Yet the persistence relation contains only internal-vertex pairs.
It says nothing about whether the port persists and carries no edge map for
the deletion of `a-b,b-p` or creation of `a'-c,c-p`. Those omissions are
exactly the data a genuine rewrite interface normally controls.

## 4. What an algebraic graph rewrite would require

In double-pushout graph rewriting a production is normally a span
`L <- K -> R` of graph morphisms. Applying it to a match of `L` in a context
requires a pushout complement and a second pushout; the interface `K` records
what is preserved, and gluing/dangling conditions control lawful deletion.
Sequential composition along overlaps is then a theorem only in a category
with the required adhesive structure and only after the overlap/matches are
typed. This comparison supplies a standard of completeness, not imported
dynamics.

`RewriteSpan.validate()` performs only these checks:

1. persistence endpoints belong to the source/target internal vertex sets;
2. the persistence pairs are injective on both sides;
3. created vertices belong to the target and do not overlap persistent
   targets; and
4. allowed matrix entries join declared internal vertices.

It does not construct `K`, represent edge or port morphisms, state deleted
material, validate a context match, enforce a dangling condition, compute a
pushout complement, or define composition. Thus the delivered span is a
labelled before/after pair with an internal-vertex correspondence. It is not
wrong as a finite data structure. It is insufficient for the paper's global
sentence “composition composes both.”

The `SRW-BUNDLE-WELD` gate checks a typed referent, five individually
isometric matrices, and one passive relabelling screen. None of these asserts
that two rewrite decompositions produce one common composite morphism. The
primary word `CONSTRUCTED` therefore overstates what was built.

## 5. Independent map-only reconstruction

At the inherited growth point the anonymous map is

```text
V = [[3/5, 0],
     [0,   1],
     [4/5, 0]].
```

Its actual support is `{(row0,col0),(row1,col1),(row2,col0)}`. Exhausting the
`2! * 3! = 12` basis dictionaries against the declared allowed relation

```text
a -> a',  a -> c,  b -> b'
```

leaves exactly two:

```text
columns (a,b), rows (a',b',c)
columns (a,b), rows (c,b',a').
```

The input dictionary is forced. The sole ambiguity exchanges which of the two
`a`-fed target directions is named persistent `a'` and which is named created
`c`. Every present contraction ignores those semantic names, so the two
current signatures coincide.

No admissible invariant of the anonymous matrix repairs this. Singular values,
row/column norms, ranks, kernel, image, Gram matrix, and support automorphisms
can distinguish two numerical row directions, but cannot say which one is the
ancestral continuation of `a`. More decisively, the exact same `V` accepts the
two typed persistence spans

```text
{a->a', b->b'}
{a->c,  b->b'}.
```

An anonymous coordinate invariant is identical in those two models while the
declared ancestry differs. Recovering ancestry would require a physical
observable or an independent relational record that already individuates the
target directions. That extra object is the very dictionary/span the map-only
proposal tried to remove.

The support argument is also robust under the endpoint rows. On the registered
rational circle, the kinematic grammar always has three allowed arrows, while
at zero-coupling endpoints the map has only two nonzero entries. Therefore the
lawful relation is

```text
actual support subset-of kinematic grammar,
```

not equality. A zero amplitude cannot by itself be promoted to the ontological
statement that an interaction is forbidden.

Classification: map-only non-recovery is a **finite countermodel/theorem by
non-injectivity**, not merely failure of one reconstruction algorithm.

## 6. The two dictionaries and a new lawful future

The candidate's two futures are correctly computed. A graph-local probe that
reads the unique internal neighbor of the typed boundary port gives exact
probabilities

```text
primary dictionary: 16/25
swapped dictionary:   9/25.
```

A persistence-sensitive future reverses the pair to `9/25,16/25`. These
screens show that the distinction can become physical once a continuation is
declared in relational language rather than by row number.

I added a third lawful future absent from the scorer: create a flag vertex
attached to whichever target vertex is typed as **created**, then measure the
flag excitation after an isometric copy of that direction. It is graph/span
local and gives `16/25` versus `9/25`; the analogous flag attached to the
persistent target gives the complementary pair. This is an exact independent
reactivation of the same ambiguity.

The result is conditional, not a selector. Paper 4 has a finite list of
declared futures, not a law-generated continuation closure. It has not proved
that nature licenses the graph-neighbor future, the persistence future, my
flag future, all three, or some different family. Therefore the strongest
surviving sentence is:

> The two support-compatible dictionaries are indistinguishable by the
> registered present observables and distinguishable by some finite declared
> typed futures; which future family and which dictionary are physical remain
> unselected.

The swap is not stable gauge relative to those declared futures, but neither
is it established as an absolute physical identity fact.

## 7. Fiber dimensions and the absent global carrier functor

`FiberSpec.dimension` computes exactly:

| declared sector recipe | source | target |
|---|---:|---:|
| one vertex excitation | 2 | 3 |
| one vertex excitation with multiplicity 2 | 4 | 6 |
| vertex/port stabilized recipe | 3 | 4 |
| one edge excitation | 2 | 2 |

Only the first recipe has the inherited anonymous `3 x 2` shape. The values
are derived **after** choosing the sector, internal multiplicity, and whether
ports contribute. They do not follow from the graph alone.

There is no implemented functor from a category of configurations and
rewrites to carrier spaces and transports. `FiberSpec` provides an objectwise
dimension formula. It has no action on a general relabelling, no action on a
rewrite, no identity/composition laws, and no common catalogue of all complete
configurations. The fixture contains two finite graphs and four recipes, not
the paper's global direct sum over a meta-catalogue.

Internal multiplicity makes the gap concrete. `V tensor I_2` is a lawful
`6 x 4` isometry, but so is `V tensor X`, with the internal bit flipped during
growth. Both have the same coarse graph rewrite. The original allowed-entry
relation on vertex pairs cannot distinguish them unless it is enlarged to
include internal states and their transport rule. Once enlarged, the support
grammar is not “the same rewrite” without an additional fiber-level
compatibility axiom. The port and edge recipes pose the same issue: their
basis elements are not in the internal-vertex persistence relation.

Thus the candidate establishes several **possible fiber constructions**. It
does not derive a configuration basis, catalogue, or carrier functor.

## 8. Relabelling naturality and recurring locality

For passive bijections of the finite vertex names, covariance is easy: relabel
the graph/span and conjugate the coordinate matrix by the corresponding
permutation representations. This holds for the full name groupoid by direct
substitution, not just the registered swap. But the candidate gate checks one
renamed screen and does not implement that groupoid action as a functor. More
importantly, passive-name covariance does not imply coherence of **different
rewrite decompositions**. The mandatory counterfixture below separates those
claims.

`SRW-RECURRING-LOCALITY` sets the second growth pair equal to the first and
checks that a mutant with a different pair moves a screen. That proves the
consequence of a type-universality axiom. It does not derive that the two sites
have the same full local type, nor does locality force numerical equality
across otherwise disconnected contexts. The equality is law data. The honest
classification is:

- recurrence under a previously declared equality of local event type:
  **conditional theorem**;
- equality of the two local event types and their couplings:
  **declared universality**, not selected by the fixture; and
- the repeated numerals `3/5,4/5`:
  **not yet a measured physical constant**.

## 9. Mandatory overlap counterfixture

I built the counterfixture independently over exact rationals. Let the initial
graph have vertices `a,b,c` and edges `a-b,b-c`. Event `A` creates `x` attached
at the shared actor `b` while its transport swaps the `a,b` directions. Event
`B` creates `y` at the same shared actor while its transport swaps `b,c`.
Both orders reach the same labelled final graph with vertices `a,b,c,x,y` and
both created attachments.

Each event is represented by a rectangular permutation embedding: it maps the
old orthonormal basis into the new carrier, performs its local swap, preserves
the other event's already-created direction, and leaves its own new row
initially unfed. Therefore every individual map satisfies
`Theta^dagger Theta = I`, actual support is a subset of its allowed grammar,
and carrier dimension equals the declared one-excitation vertex count.

The exact checks are:

```text
four local isometries:                 True True True True
AB composite isometry:                 True
BA composite isometry:                 True
AB == BA:                              False
AB |a>:                                |c>
BA |a>:                                |b>
probability of final projector |c><c|: 1 versus 0
```

I then tensor every leg with an idle two-valued internal degree. The local
dimensions are `6 -> 8 -> 10`; all four legs and both composites remain exact
isometries, while the composites still disagree. This supplies the protocol's
required created internal degree and shows that spectator/internal
stabilization does not cure the overlap.

The arena does not show that lawful physics must make `A` and `B` commute. It
shows something more basic: the local SRW surface does not decide among at
least four possible completions:

1. declare one causal order;
2. record the order as relational data;
3. supply a nontrivial associator/order-holonomy rule; or
4. replace the overlap by an independently specified joint event.

Any of those may be viable. None is in Paper 4. Hence two typed local bundle
arrows do not yet determine one typed composite successor. The counterfixture
is a **kill** of the universal bundle-composition reading, not a kill of the
individual finite isometries.

## 10. Reciprocity: exact lemma, invalid weld promotion

For unit growth vectors `(x,z)` and a unit reconvergence row `(u,v)`, requiring
exact erasure on the reached image gives

```text
xu + zv = 1.
```

Since both vectors have norm one,

```text
(x-u)^2 + (z-v)^2 = 2 - 2(xu+zv) = 0,
```

so `(u,v)=(x,z)` over the registered real slice. This is an exact conditional
left-inverse theorem. Extensions on an orthogonal direction remain free until
a future reads them, and probabilities of different durable successors are
not selected. The five reciprocal rows in the 25-point grid are correctly
reported.

What fails is the noun “weld.” A left inverse for one matrix on its reached
image neither creates a compositional relational rewrite nor selects a
continuation grammar. The fourth registered finding should therefore be
replaced by a lemma, not retained as a primary architectural result.

## 11. Contribution to the missing joint successor law

The candidate contributes these real advances:

1. a sharp type correction: geometry/rewrite, persistence, carrier choice,
   and transport entries are distinct law components;
2. an exact counterexample to recovering allowed grammar or ancestry from an
   anonymous transition matrix;
3. a finite method for testing whether a basis dictionary becomes physical
   under specified relational futures;
4. objectwise carrier recipes for several selected sectors; and
5. a conditional creation/erasure left-inverse constraint.

It does **not** yet supply the missing map

```text
(relations, geometry, process state)
    -> (new relations, new geometry, new process state)
```

as one law, because it lacks:

- a generative catalogue of admissible configurations and rewrites;
- an event-selection/weight rule;
- a carrier functor with identities and composition;
- an overlap, order, associator, or fusion law;
- coherence across multiple cuts/decompositions;
- a continuation-closed definition of durable records; and
- an actualization postulate tied to that same composed law.

For unbounded growth and a genuine two-to-`n` construction, the next object
must at minimum be a category (or higher rewrite structure) of typed local
events with interfaces, a monoidal/disjoint product, explicit overlaps, and a
coherence rule for alternative decompositions. A law must then assign
transports and probabilities functorially or state exactly how the failure of
functoriality is recorded as physical order/curvature. Paper 4 stops before
that step.

## 12. Numbered findings

1. **PASS — theorem/countermodel.** The anonymous map does not determine the
   kinematic grammar or ancestry. The same `V` supports two distinct typed
   persistence spans, and allowed zero-coupling arrows disappear from actual
   support.

2. **PASS WITH QUANTIFIER FIX — finite-fixture fact.** Twelve dictionaries
   reduce to two; registered present observables are blind; specified typed
   futures distinguish them. No law-generated closure proves this difference
   physical under all licensed continuations.

3. **KILL — categorical/architectural claim.** `SRW-BUNDLE-WELD-CONSTRUCTED-`
   `BUT-CATALOGUE-AND-COUPLINGS-UNSELECTED` is false as a claim of a constructed
   successor rewrite bundle. Only single-arrow typed pairs are constructed;
   overlap composition fails the standing surface in an exact counterfixture.

4. **DEMOTE — conditional matrix theorem.** The reciprocal left inverse on a
   reached unrecorded image is exact, while null extensions and durable-branch
   weights remain free. Calling it a reciprocal *weld* inherits finding 3's
   missing composition and should be removed.

5. **FIX — declared functor scope.** The four dimensions are derived from four
   selected `FiberSpec` recipes. A global complete-configuration catalogue and
   functor are not built.

6. **FIX — locality wording.** Reusing a coupling at two sites is enforced by
   the declared equality of event type; it is not selected by locality alone.

7. **NEW BLOCKER — exact overlap counterfixture.** Locally isometric,
   support-compatible, internally stabilized creation events can yield
   different composites on the same final graph. The law needs an explicit
   overlap/coherence completion.

## 13. Smallest repair/kill set

1. Kill the third registered primary finding and replace every statement that
   a compositional bundle has been constructed by “a finite family of typed
   single-step `(rewrite, transport)` examples has been constructed.”

2. Demote the fourth primary to the conditional left-inverse lemma stated in
   section 10, with no bundle/weld promotion.

3. Bind the second finding to the finite declared continuation family. Do not
   call the dictionary selected, absolute, or continuation-stable.

4. Replace “carrier functor/global meta-catalogue” by “four objectwise sector
   recipes” until an action on rewrite morphisms, identities, and compositions
   is implemented and gated.

5. Add a successor unit—not an in-place unregistered repair—with interfaces,
   edge/port persistence, overlapping matches, and an explicit coherence
   outcome. The mandatory arena above must either commute by theorem, acquire
   a recorded order, or be assigned a typed nontrivial associator/joint event.

6. Extend allowed support to internal/port/edge basis elements before claiming
   that catalogue enlargements use the same rewrite grammar.

These are not prose-only fixes to the present paper: items 1 and 2 change two
of four registered outcomes. That is why the grade is `REJECT`, despite a
clean replay and two substantial surviving results.

## 14. Proposed adjudicated finding list

I propose exactly two primary findings:

1. **`SRW-MAP-ONLY-WELD-REFUTED`**, with “weld” understood only as the rejected
   map-only identification: actual transition support does not recover the
   allowed entry grammar or persistence/ancestry span.

2. **`SRW-DICTIONARY-CURRENT-BLIND-BUT-DECLARED-FUTURE-PHYSICAL`**: the frozen
   current observables leave two support dictionaries; some finite declared
   typed futures distinguish them; neither the continuation family nor the
   dictionary is law-selected.

Retain outside the primary list:

> **Conditional reciprocal-image lemma.** If an unrecorded growth is required
> to reconverge exactly through a unit-norm real leg, the later row equals the
> adjoint growth row on the reached image. This selects neither its orthogonal
> extension nor durable-successor weights.

Do not retain either registered `...BUNDLE-WELD-CONSTRUCTED...` or
`...RECIPROCAL-WELD-CONSTRUCTED...` finding. The exact mandatory counterfixture
satisfies the protocol's material composition-failure condition.

## 15. Scope labels

- **Theorem:** anonymous-map non-injectivity for the registered discriminator;
  actual support need only be a subset of allowed grammar; conditional
  reciprocal-image left inverse.
- **Exact finite-fixture fact:** 12 dictionaries, 2 survivors; screens
  `16/25,9/25`; four dimension pairs; 25 angle rows; four finite phase orbits.
- **Declared grammar/type:** the two graphs, ports, persistence pairs, created
  vertices, allowed entry relation, sector recipes, recurrence identity.
- **Conditional result:** future-physical dictionary, carrier dimensions,
  reciprocal erasure, phase holonomy screens.
- **Interpretation:** global meta-catalogue, one successor bundle, recurring
  physical constant.
- **Refusal:** no event-selection law, overlap law, unbounded two-to-`n`
  composition, global record permanence, particle/species ontology, QFT/GR,
  Hamiltonian reconstruction, or actualization follows from this unit.
