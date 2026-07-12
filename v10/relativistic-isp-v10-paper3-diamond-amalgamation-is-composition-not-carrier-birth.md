# Relativistic ISP v10 Paper 3: Marked-Support Amalgamation Is Composition, Not Carrier Birth

## Conditional pushout theorem, projective no-bootstrap, and interface-selection boundary

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** revised after two independent hostile-review rounds, 2026-07-11.
All production source is under `v10/code/` and uses only the Python standard
library.

**Receipt:** `v10/code/d2_marked_diamond_amalgamation_exact.py` — 33/33 exact
checks after hostile-round-1 repairs.

## Abstract

D1 showed that no-silent boundary closure can filter an already supplied
record cut but cannot derive the cut's participating support. D2 asks whether
the sealed-diamond ontology contains a more primitive construction: glue
bounded marked diamonds along their common screens or collars and read the new
direct carrier from the amalgam.

The answer separates composition from birth. Given a finite typed overlap
span

$$
D_A\xleftarrow{f}I\xrightarrow{g}D_B,
$$

the marked-support pushout exists in an explicit weak-homomorphism category,
is covariant, is symmetric up to isomorphism, and is independent of compatible
serial construction order. An exhaustive finite cocone audit verifies unique
factorization. This is a finite support-incidence analogue of the v6
overlap/sheaf and artificial-seam cancellation principles; it does not model
their probability, collar, source, or holonomy data. The pushout contains
exactly the transported input supports. Empty-interface gluing is a disjoint
coproduct; nonempty
overlap does not create a support connecting the exclusive records. Moreover,
two different legal embeddings of the same bare interface can yield
nonisomorphic pushouts. The universal property determines the amalgam only
after the interface and its legs have been supplied.

An exhaustive finite closure census sharpens the no-go. Across all 4,096
extensive deterministic pair-edge closures on three labeled records,
permutation covariance, idempotence, commutation with every induced
restriction, and refusal to join two isolated records leave exactly one rule:
the identity. A first pair carrier cannot be bootstrapped under these axioms.
Higher supports remain underdetermined: under intersection/shadow restriction,
exactly two three-record fill laws survive—leave a complete triangular
boundary unfilled or fill it. Under contained-event restriction, a connected
two-edge path may also be filled without leaving pair shadows. Thus even the
answer depends on what physical restriction means.

Finally, on three symmetric output ports no deterministic covariant rule can
select exactly one pair. A uniform stochastic kernel can select one pair with
probability `1/3` each and remain covariant, but it fails strong restriction
naturality against the edgeless two-record refusal axiom. It is an additional
stochastic law, not a construction-order derivation.

The D2 verdict is

$$
\boxed{
\text{typed marked-support amalgamation gives canonical conditional composition,}
\quad
\text{not primitive carrier birth.}
}
$$

Under the frozen support-skeleton axioms, a first carrier requires an
additional root/bridge-sector law, typed boundary seed, or explicit
symmetry-breaking record. No-silent closure remains a downstream admissibility
test.

## 1. Why D2 is upstream of the click rate

A complete interacting click law must determine at least:

1. which existing record ports may participate;
2. whether the event is private, pairwise, or higher-arity;
3. the new event/diamond and its parent incidence;
4. the event rate;
5. the event outcome and transport response.

The v7 click law addresses item 4 after a channel is supplied. D1 addresses
one admissibility condition after items 1–3 are supplied. D2 asks whether
the marked support skeleton of sealed-diamond composition determines items 1–3
before any rate is assigned.

No emergent metric appears in D2. “Local” means local to a supplied finite
record interface, not spatially nearby.

## 2. What the earlier diamond corpus actually supplies

### 2.1 Sealed record diamonds

V6 defines a sealed diamond by a finite record atom set, count/reference law,
lower and upper screens, collar data, internal transports, and a whole-history
law. The object is bounded and internally readable; it is not an Alexandrov
reference region or a construction-order square.

### 2.2 Collar and source gluing

V6's source-gluing law has the coboundary form

$$
\rho_i=h_{i+1}-h_i.
$$

Artificial internal seams cancel:

$$
\sum_{i=a}^{b-1}\rho_i=h_b-h_a.
$$

This is a strong composition law once the complete interface cochain `h` is
known. External boundary totals do not reconstruct the internal interfaces.

### 2.3 Overlap/sheaf composition

V6 also requires overlapping local diamonds to be restrictions of one
coherent whole-history law. The finite audit found arbitrary overlap-compatible
local coefficients and hidden higher-body holonomies. Sheaf consistency is
necessary but does not choose the glued process.

### 2.4 V7 primitive interfaces

V7 later classified boundary, order interval, perturbation, and overlap as the
four primitive interfaces of a bounded record diamond. Its least no-silent
response class is conditional on that primitive-interface seed and on supplied
overlap transport maps.

### 2.5 The remaining gap

All these constructions begin with one of the following already present:

- a shared screen or collar;
- a global interface cochain;
- a common ancestor;
- an overlap diagram and transport map;
- a supplied candidate extension.

They explain how shared structure composes. They do not explain how the first
shared structure arises between previously unjoined records.

## 3. Finite marked support skeletons

D2 applies a forgetful abstraction to the carrier incidence of a sealed
diamond. The resulting marked support skeleton is

$$
D=(V,E),
$$

where `V` is a finite record/port set, `E` is a finite family of direct
supports, and

$$
m(v)=(\text{port/interface type},\text{stable provenance/ancestry}).
$$

This skeleton does not contain the complete probability law, screens, collar
response, transports, or holonomy of a sealed diamond. Positive results in D2
are theorems about marked support incidence. A carrier-birth law on full
diamonds would have to descend to this skeleton to inherit the negative
closure theorems.

### 3.1 Morphisms

The ambient category uses mark-preserving weak support homomorphisms. A vertex
map `f:V->W` is a morphism when marks are preserved and, for every source
support `e`, its image `f(e)` is a target support whenever at least two distinct
vertices remain. A collapsed support may become a singleton.

General morphisms are allowed to be noninjective. Supplied interface legs are
required to be injective. This distinction matters: a category containing
only injective maps would not give the claimed empty coproduct for arbitrary
cocones.

**Lemma 3.1 (category).** Identity maps are weak marked-support
homomorphisms, and the composite of two such homomorphisms is again one.

**Proof.** Marks are preserved by identity and transitively by composition.
For a source support, its first image either collapses to a singleton or is a
support. A singleton cannot expand under a function. If it remains a support,
the second map again either collapses it or carries it to a target support.
Thus identities and composition close. ∎

Two support restrictions are kept distinct.

### 3.2 Intersection/shadow restriction

For retained vertices `K`,

$$
r_K(E)=\{e\cap K:e\in E,\ |e\cap K|\ge2\}.
$$

A higher support leaves lower-arity shadows when participants are removed.
This is the support projection used in D1B.

### 3.3 Contained-event restriction

Alternatively,

$$
q_K(E)=\{e\in E:e\subseteq K\}.
$$

An irreducible event disappears if any participant is removed. This is a
different ontology, not a notation change.

## 4. Conditional marked-support pushout

Let a typed interface diagram be

$$
D_A\xleftarrow{f}I\xrightarrow{g}D_B,
$$

with injective mark-preserving legs. The finite pushout identifies `f(i)` with
`g(i)` for every interface record, transports the input supports into the
quotient, and carries the common mark to every identified vertex. No
additional support is inserted.

**Proposition 4.1 (fixed-span amalgamation).** For a supplied finite typed
span in the finite marked-support category, the pushout exists and is unique
up to marked isomorphism. It is covariant under relabeling, symmetric under
exchange of the two legs, and associative up to marked isomorphism for
compatible iterated spans.

**Proof.** Form the disjoint union of the two vertex sets and quotient by the
relations `f(i)~g(i)`. Injective mark-preserving legs make the quotient mark
well defined. Transport every input support to the quotient. Given a compatible
cocone into any marked support system `X`, assign each quotient class the
common cocone image of any representative. Compatibility makes this map well
defined; support preservation follows because every pushout support came from
one input. The canonical input maps are jointly surjective, so the mediator is
unique. ∎

The exact receipt additionally:

- exhausts all eight valid cocones into a six-vertex marked audit target and
  finds exactly one mediator for each;
- verifies the empty-interface coproduct against a noninjective mediator;
- verifies relabeling covariance and exchange symmetry;
- constructs both true iterated typed pushouts of a three-object chain and
  compares their canonical marked signatures.

This is the support-skeleton construction-order-gauge result D2 was looking
for. It is conditional on the diagram and is not yet a gluing theorem for the
full stochastic/holonomy laws.

The general associativity statement is not inferred from the one chain
receipt. Both parenthesized iterated pushouts are colimits of the same finite
zigzag `A <- I -> B <- J -> C`; colimit uniqueness gives their unique marked
isomorphism. The executable chain is an implementation witness for that
argument.

## 5. Pushout support conservation

Take

$$
A=\{a,i\},\quad E_A=\{\{a,i\}\},
$$

and

$$
B=\{i,b\},\quad E_B=\{\{i,b\}\}.
$$

Their shared-interface pushout has supports

$$
E_{A\cup_I B}=\{\{a,i\},\{i,b\}\}.
$$

It contains neither `{a,b}` nor `{a,i,b}`.

**Proposition 5.1 (no novel support in ordinary amalgamation).** The finite
support-union pushout contains exactly the transported supports of its inputs.
It does not create a carrier across the exclusive parts of the two diamonds.

For the empty interface, the same construction is the disjoint coproduct and
contains no cross-component carrier. Thus ordinary pushout gluing obeys the
no-bootstrap rule rather than solving it.

## 6. The interface-map selector remains open

The universal property also cannot select its own legs. Consider a bare
two-record interface and two three-vertex graphs:

- `A` has edge `x-i1` and an additional interface vertex `i2`;
- `B` has edge `y-j1` and an additional interface vertex `j2`.

Two legal embeddings are:

$$
i_1\sim j_1,\quad i_2\sim j_2,
$$

and

$$
i_1\sim j_2,\quad i_2\sim j_1.
$$

The first pushout has degree multiset `(0,1,1,2)`; the second has
`(1,1,1,1)`. Their exact canonical graph signatures are respectively

```text
(4, 000011)
(4, 001100)
```

and are nonisomorphic.

**Proposition 6.1 (diagram-selection boundary).** The pushout universal
property does not determine an interface matching. Distinct legal untyped
embeddings can yield physically different amalgams. Unique port types could
force a matching, but those types would be additional record structure.

The repaired typed receipt makes this conditional explicit. When both
interface vertices carry the same bare collar mark, the aligned and crossed
maps are legal and their pushouts remain nonisomorphic. When the two vertices
carry distinct red/blue provenance marks, the aligned map is legal and the
crossed map is rejected as non-mark-preserving. Likewise, an ancestry
interface marked `root:R1` maps into two `R1` ports but not into an `R2` port.
Marks can therefore select a span only when the distinguishing record is
already present; the pushout does not create that mark.

## 7. Exact first-pair no-bootstrap theorem

Now ask whether a closure operator `F` on finite pair-support graphs can create
the first direct carrier. Freeze the following requirements:

1. `F` is extensive: existing edges remain;
2. `F` is deterministic;
3. `F` is permutation-covariant;
4. `F` is idempotent;
5. `F` commutes with every induced vertex restriction;
6. two isolated retained records remain unjoined.

On three labeled records there are eight input graphs. For each graph, every
supergraph is a possible extensive output. The total number of deterministic
extensive maps is

$$
\prod_{G\subseteq K_3}2^{3-|E(G)|}=2^{12}=4096.
$$

The receipt enumerates all 4,096 maps and applies the gates exactly. Exactly
one survives: `F(G)=G`.

**Theorem 7.1 (finite projective pair no-bootstrap).** On graphs through three
vertices, extensivity, deterministic covariance, idempotence, all-restriction
naturality, and edgeless two-record refusal force the identity closure.

There is also a structural proof independent of the census. If `F(G)` added a
missing pair `{u,v}`, restrict to `{u,v}`. Naturality says this edge must equal
the output of `F` on the restricted input, which is two isolated vertices.
The edgeless two-record axiom says that output is empty, a contradiction.

The proof extends to any finite number of vertices for first pair edges.

## 8. Higher support is not uniquely forced

Pair no-bootstrap does not imply that higher support is unique once all lower
faces exist. Add one possible three-record support `ABC` above the three pair
faces. An extensive rule is determined by eight yes/no decisions—whether to
add the triple for each pair graph—so there are 256 predicates.

Under permutation covariance and intersection/shadow projectivity, exact
enumeration leaves two:

1. never add the triple;
2. add the triple exactly when all three pair faces exist.

**Theorem 8.1 (higher-support family).** Even with all pair faces present,
covariance, idempotence, extensivity, and intersection projectivity do not
choose whether the triangular boundary is an unfilled family of pair
relations or one filled three-record support.

This is the carrier analogue of D1's support over-eligibility.

## 9. Restriction ontology changes the family

Under contained-event restriction, a triple vanishes on every proper
two-record restriction. Consequently, the rule

> add `ABC` whenever its pair graph is connected

is permutation-covariant, monotone, idempotent, refuses a completely
fully disconnected three-record support skeleton, and commutes with
contained-event restrictions.
It fills the three two-edge paths as well as the complete triangle.

The same rule fails intersection/shadow projectivity: filling a two-edge path
creates the missing pair as a projected shadow.

Contained-event projectivity by itself is weaker still: “always add the
triple” is covariant, monotone, and contained-natural, although the edgeless
refusal axiom correctly rejects it.

The repaired receipt exhausts all 256 fill predicates. Permutation covariance,
monotonicity, contained-event naturality, and refusal on the empty graph leave
four rules. Strengthening refusal so that a triple may not join an isolated
component still leaves three. Thus the displayed connected-fill rule is not a
hand-picked lone survivor.

**Proposition 9.1 (restriction-semantic dependence).** Projectivity cannot be
claimed without specifying whether higher events cast lower-support shadows.
The two restriction ontologies admit different carrier families.

The corpus does not yet derive which support restriction is physical.

## 10. Automorphism obstruction and construction order

Consider three output ports with no distinguishing mark. The permutation group
acts transitively on their three possible pairs. Exhausting all pair families
shows that only two are invariant under every permutation:

$$
\varnothing,
\qquad
\{AB,AC,BC\}.
$$

No invariant family contains exactly one pair.

**Theorem 10.1 (deterministic symmetric-pair selector obstruction).** A
deterministic covariant rule cannot select exactly one pair from three
structurally indistinguishable ports.

The deterministic qualifier is essential. There is an exact covariant
stochastic kernel:

$$
P(AB)=P(AC)=P(BC)=\frac13.
$$

It chooses one pair almost surely without using construction order. But after
restriction to, say, `AB`, the probability of an inherited `AB` edge is
`1/3`, whereas the edgeless two-record refusal axiom requires zero. Hence this
kernel fails strong restriction naturality.

**Proposition 10.2 (stochastic projective no-bootstrap).** The unique
covariant probability law supported on exactly one of the three symmetric
pairs is uniform. It is not compatible with strong pair restriction and
edgeless two-record refusal.

A serial builder can choose “the first eligible pair,” but then its commit
order is a physical symmetry-breaking input rather than gauge. A stochastic
kernel avoids that deterministic problem but is itself extra dynamical input
and fails the frozen projectivity gate. A deterministic invariant rule must
return the whole orbit, return none, use an invariant higher support, or wait
for a distinguishing record mark. None is selected by covariance alone.

## 11. Supplied common-root carriers are inherited, not born

Suppose the ontology is supplied with a root event carrying support
`{r,a,b}` and ancestry provenance `root:R`. Under intersection
restriction to `{a,b}`, the descendants inherit the pair shadow `{a,b}`.
Under contained-event restriction, the irreducible root event disappears.

Both statements are conditional on that supplied root/support mark and are
consistent with their respective restriction ontologies. Neither derives the
root event. Common ancestry moves the carrier question to the root/branch law.

## 12. What D2 establishes

The correct architecture is now:

$$
\text{committed marked history}
\longrightarrow
\boxed{\text{still-missing span/carrier proposal}}
\longrightarrow
\text{canonical marked-support amalgam}
\longrightarrow
\text{D1 no-silent filter}
\longrightarrow
\text{still-missing rate/outcome law}.
$$

D2 supplies:

1. a finite fixed-span amalgamation construction on marked support skeletons;
2. relabeling covariance;
3. construction-order gauge for compatible diagrams;
4. support conservation under ordinary pushout;
5. an exact first-pair no-bootstrap theorem;
6. exact higher-support and symmetry obstructions;
7. an explicit separation of restriction ontologies.

D2 does not supply:

1. the overlap interface;
2. the embeddings of that interface into the two diamonds;
3. a first pair carrier;
4. a unique higher-support fill rule;
5. a root/bridge nucleation law;
6. an event rate or outcome kernel.

## 13. Consequence for the interacting click-law search

The failure is not that category theory is useless. The pushout gives exactly
what construction-order gauge requires after physical incidence is known. The
mistake would be to ask a universal property to generate the diagram to which
it applies.

There is an important foundational fork. Let `\Omega` be a finite or standard
measurable space of variable marked histories, `\mu` a path measure, and
`\mathcal F_n` the sigma-algebra of the committed history through click `n`.
If `\mu` is taken as primitive and the relevant regular conditional law
exists, then for every positive-mass committed history `H` it already defines

$$
\mu(dH_{n+1}\mid\mathcal F_n)(H),
$$

whose support defines `Ext_\mu(H)` and whose marks include the carrier
marginal. In that formulation D2 is not needed to derive the law; the measure
is the law. D2 concerns the stronger SHARD program of deriving `\mu` and its
extension support from sealed record structure. “Depend on the full history”
specifies the conditioning sigma-algebra and argument `H`; it does not by
itself specify `\mu`.

Three honest routes remain:

1. **Initial connected seed:** carry a primitive relational root as
   cosmological boundary data. Later carriers are inherited or refined.
2. **Bridge-sector birth:** introduce a genuinely new event sector whose
   proposition includes its participating ports and whose rate must be derived
   from record-intrinsic boundary work.
3. **Typed symmetry breaking:** wait until a recorded difference between ports
   selects an interface orbit; this cannot explain the first completely
   symmetric bridge.

The first is an initial-condition answer. The second is new physics. The third
is conditional dynamics after asymmetry already exists.

## 14. Reproducibility

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d2_marked_diamond_amalgamation_exact.py
```

The receipt uses only standard-library exact finite combinatorics and prints
33/33 checks.

## 15. Claims and nonclaims

### Claims

1. A supplied finite typed overlap span has a canonical support-conserving
   pushout in the marked support-skeleton category, up to marked isomorphism.
2. Compatible fixed diagrams admit construction-order-gauge composition.
3. The pushout universal property does not select its own interface legs.
4. Strong restriction naturality plus the edgeless two-record refusal axiom
   forbids first pair birth in the support skeleton.
5. Higher-support completion remains a family.
6. That family depends on support-restriction semantics.
7. Exact symmetry forbids deterministic selection of one pair from a
   transitive three-port orbit.
8. Uniform stochastic one-pair selection is covariant but fails the frozen
   strong restriction/edgeless-refusal gate.

### Nonclaims

This paper does not claim:

- that every sealed holonomy diamond is fully represented by a support
  hypergraph;
- a pushout theorem for full probability, collar, transport, or holonomy data;
- a final carrier, click-rate, outcome, or transport law;
- that an initial connected seed has been selected;
- relativistic locality or no-signaling;
- quantum joint-diamond dynamics;
- a continuum or marked profinite theorem;
- any geometry, dimension, or cone-shape result.

## 16. Conclusion

Marked-support amalgamation solves a real problem: once two sealed record
diamonds come with a typed common interface, their support incidence can be
composed canonically and independently of serial presentation. Extending this
to their full probability/collar/transport laws remains a separate gluing
theorem.

It does not solve the prior problem: why those diamonds have that common
interface, or why previously unjoined records acquire a first direct carrier.

Under the frozen support-skeleton axioms, the projective pair theorem shows
that this is not merely a missing clever closure definition. If every
restriction must see the same carrier shadow and an edgeless two-record
skeleton remains edgeless, no first pair edge can appear. Weakening the
restriction ontology admits more higher events but does not select among them.
Covariance prevents construction order from quietly making the deterministic
choice; stochastic choice remains additional law.

The next investigation must therefore be explicit about its new input:

$$
\boxed{
\text{derive or posit a root/bridge-sector nucleation law that supplies the
typed carrier diagram itself.}
}
$$

Only after that diagram exists do D2 amalgamation, D1 boundary accounting, and
the v7 evidence clock become applicable in sequence.
