# APR Paper 12 scorer protocol — semantic reconstruction before measurement

**Date:** 2026-08-18

**Status:** FROZEN SCORER PROTOCOL. This document freezes the APR scoring
rules, mutant transformations, evidence schema, and integrity contract before
`v16/code/apr_score.py`, any APR result, receipt, candidate paper, hostile
protocol, or hostile report exists.

This protocol contains no fixture result, preferred verdict, expected primary,
or expected numerical screen. Every metric is to be reconstructed from the
frozen primitive objects. The scorer is forbidden to contain a table of
expected fixture answers.

## 1. Immutable basis

The scorer is bound to commit
`2dfd8ba357e37b6d486b3ce1ba0d0bfd6113fb62` and the following bytes.

| path | role | SHA-256 |
|---|---|---|
| `v16/note-apr-pin.md` | parent question, principles, gates, outcomes, and scope | `f2b952182b9356e8ebb0aa07e1a6a022a5f892585a20d118f5ea75aabccbec52` |
| `v16/note-apr-pin-addendum.md` | contextual regional congruence and canonical boundary correction | `d018d0129f6ae7c312599e3fe0ab66cb8689a78ded9969d74c1c3e5d97e67fe5` |
| `v16/note-apr-pin-addendum-2.md` | process, locality, contact, probe, and atomic-control correction | `54573094f1ebb872f5daa907888bd4ee264ec9fe337562c62e30e3e9dfd865da` |
| `v16/code/apr_core.py` | generic exact mechanics; never fixture truth | `cd51fd36bc26701fdc649ee81f4b048dadde03e645860a7b885c501e2e180ca9` |
| `v16/code/apr_fixtures.py` | frozen primitive declarations | `0698d5d413384e43108241a15eb7134fda82deec8bffdc4413edb2c5ea2742bc` |

The fixture's canonical payload SHA-256 is
`1f55bb4a495fb7d5a76f93c83e39cc72337fbff0f1a31e67b8bda5ccd45816d0`.
The fixture validator reports schema `apr-primitive-fixtures-v1`; its counts
are integrity metadata, not scientific evidence.

No later file, untracked scratchpad, candidate prose, or review may alter the
meaning of these inputs. Any repair to a frozen input requires a new explicit
authorization and a newly frozen protocol.

## 2. Governing rule: reconstruct semantics, never score declarations

The scorer may import exact data types and algebraic mechanics from
`apr_core.py`. It may import only primitive declarations from
`apr_fixtures.py`. It must not accept any of the following as a measured fact:

- a fixture identifier or human-readable operation string;
- a field saying that a map is a process, comparison, refinement, extension,
  record, contact, causal arrow, support, boundary, probe, or law;
- a supplied profile, support subspace, comparison class, or boundary
  partition without independently rebuilding the relevant semantic object;
- an empty issue list from `validate_gluing` as evidence that a pushout,
  composite filling, or process composite exists;
- equality of ranks or dimensions as equality of calibrated subobjects;
- a finite split census as atomlessness;
- a branch label as a readable or durable record;
- a target value, expected screen, expected outcome, or expected gate boolean.

The scorer must construct a provenance DAG. Each positive scientific metric
names the primitive roots and scorer-owned transformations from which it was
computed. A byte-identical table with a disconnected provenance root is not
the same scientific object.

### 2.1 Expected-outcome prohibition

`apr_score.py` and its tests may contain:

- exact definitions and identities from the pin and this protocol;
- generic zero/nonzero, equality, inclusion, factorization, normalization,
  congruence, reachability, and covariance predicates;
- the registered outcome vocabulary and its precedence rules;
- the primitive mutant transformations in section 17.

They may not contain:

- a dictionary from fixture IDs to measured numbers or pass/fail values;
- copied profile columns, screens, ranks, class counts, residuals, or primary
  outcomes;
- conditionals whose scientific branch is selected by a fixture ID;
- a stored SHARE/SPLIT answer;
- a fallback that treats a missing construction as a pass;
- a preferred or anticipated primary.

Every reported number must be reproducible from the primitive object after
changing its neutral identifier. Identifier swaps and relabelings are
mandatory controls.

## 3. Scorer-owned exact representations

The scorer must implement the following semantic normal forms independently
of fixture measurement code.

### 3.1 Regions and Bernoulli valuations

Regions are canonical `PrefixRegion` values. For rational `0 < p < 1`, define

```text
mu_p(A) = sum over w in canonical_antichain(A)
          p^(number of 0 symbols in w)
          (1-p)^(number of 1 symbols in w).
```

This is exact `Fraction` arithmetic. The parameter rows are law inputs. The
scorer must not hard-code a value for any registered row.

### 3.2 Full-cone regional questions

For the full cone of positive finitely additive valuations, reconstruct

```text
Q_C^1(nu)(A) = nu(A meet C)
Q_C^0(nu)(A) = nu(A meet complement(C)).
```

Represent each branch map symbolically as `Restriction(E)`, meaning
`nu -> [A -> nu(A meet E)]`. A zero restriction remains a typed zero branch.
No branch is deleted or renormalized because its current weight is zero.

The scorer proves all-input positivity from restriction to a Boolean event and
proves all-input normalization from

```text
C join complement(C) = one
C meet complement(C) = zero
Q_C^1 + Q_C^0 = identity
```

on an arbitrary finitely additive valuation. Checking only the two Bernoulli
preparation rows is insufficient.

### 3.3 Decision-tree normal form

For a finite decision tree and record path `b`, derive the branch cell

```text
E_b = meet_i C_i^(b_i),
C_i^1 = C_i,
C_i^0 = complement(C_i).
```

For nonzero preparation support `S`, a registered Bernoulli row gives

```text
weight_p(b | S) = mu_p(S meet E_b) / mu_p(S).
```

The scorer retains the subnormalized branch law as the primary process
object. Conditional posterior supports are secondary readings on nonzero
branches.

Composition must be reduced by

```text
Restriction(F) after Restriction(E) = Restriction(E meet F).
```

Coarse-graining a set of pairwise disjoint branch cells is

```text
sum_b Restriction(E_b) = Restriction(join_b E_b).
```

It is never an average and never a fresh normalization.

### 3.4 Record-port normal form

The depth-`k` boundary has all bit words of length `k`. The depth-zero port is
the empty word. A question appends exactly one bit to every live input port.
The scorer derives the input/output port relation and branch cells from the
tree; it does not trust the textual `record_port_rule`.

### 3.5 Exact finite maps

Primitive matrices are parsed into `QMatrix` only by the scorer. Matrix
identities, ranks, kernels, quotient actions, fixed-effect spaces, marginals,
and subspace residuals are recomputed. A supplied matrix may be an input or a
negative control, never its own interpretation.

## 4. Branch normalization, composition, and coarse-graining gates

For every registered question tree, every nonzero preparation support, and
every registered valuation row, report:

```text
branch_cells
pairwise_overlap_cells
join_of_branch_cells
zero_branch_count
negative_weight_count
normalization_residual
posterior_supports
```

The all-input gate is analytical: branch cells must be a Boolean partition of
the incoming support. Numerical rows are exact controls only.

For every factorization, independently build:

1. the whole-tree branch normal form;
2. the branch normal form obtained by sequential grafting at each cut;
3. every registered alternate cut;
4. every registered coarse-graining of the fine record ports.

Compare canonical branch cells, record-port maps, and restriction operators.
The comparison is not a comparison of fixture strings or of final scalar
probabilities alone.

The empty tree must act as the identity at every compatible boundary.

## 5. Typed cospans, the law functor, tensor, and naturality

A joint horizontal-process gate requires one typed object containing all of
the following:

1. boundary objects with predictive state or operator spaces;
2. vertical passive maps between presentations of the same boundary fact;
3. horizontal fillings;
4. an assignment `M -> T_M` from each horizontal filling to the process map
   reconstructed in section 3;
5. identity;
6. horizontal composition;
7. disjoint monoidal composition;
8. vertical naturality;
9. generated output readers/effects;
10. generated exterior replacements when locality is claimed.

### 5.1 Cospan composition

For each factorization, the scorer must form the finite pushout-shaped
composite rather than call `validate_gluing` and stop. It must:

- make disjoint tagged copies of the two apices;
- impose exactly the shared-boundary identifications induced by the legs and
  any lawful boundary comparison;
- transport and union the apex relations;
- canonicalize the quotient presentation;
- compare it with the declared whole filling by a boundary-fixing
  isomorphism;
- compare the corresponding process assignments under the same isomorphism.

Compatible endpoint names without the constructed quotient do not pass.

### 5.2 Functoriality

The scorer verifies exactly

```text
T_(N compose M) = T_N compose T_M
```

on all full-cone branch restrictions and record ports, not only on registered
Bernoulli states.

### 5.3 Disjoint tensor

The scorer distinguishes Boolean disjointness inside one event algebra from
independent monoidal carriers. A spectator declaration passes only if the
fixture law constructs the independent carrier, tensor boundary, tensor
filling, and tensor process map and verifies

```text
T_(M tensor N) = T_M tensor T_N.
```

Sequentially commuting questions are not a tensor product.

### 5.4 Vertical naturality

For every passive vertical map and every filling square, reconstruct the
transported filling and verify

```text
J_out T_M = T_M' J_in.
```

Many-to-one maps, record erasures, and record retypings are not passive merely
because they are listed in the vertical section. A passive isomorphism must
have its inverse and both composites must act as identity on complete future
profiles.

## 6. Generated probes and complete future profiles

The scorer must build profiles from the law. The fixture may supply regions,
preparations, tree grammar, continuation grammar, and reader schedules; it
may not supply final profile values.

For boundary state `(support S, record R)`, precontext `P`, future tree `W`,
spectator `X`, regional effect `E`, and record effect `Z`, derive

```text
Pred(P,W,X,E,Z | S,R)
```

by composing the scorer-owned branch restrictions and summing precisely the
fine record ports accepted by `Z`.

Profile coordinates are ordered canonically by the canonical serialization
of the generated context, never by fixture insertion order.

The probe coordinate is assigned exactly as in addendum 2:

```text
INCOMPLETE | COMPLETE-POSTULATED | COMPLETE-GENERATED.
```

`COMPLETE-GENERATED` requires all of the following:

- the question constructor accepts a fresh scorer-created `PrefixRegion`
  outside the registered finite list;
- the same uniform constructor produces its branch law and reader;
- the continuation grammar is closed at the claimed scope;
- the symbolic separating-probe proof uses only that predeclared grammar;
- a finite-depth or serialization oracle fails the registered mutants.

The finite catalogue and appended-probe rows must be used to show that a
finite receipt does not by itself establish completeness.

## 7. Three quotient types

The receipt must expose three separate constructions.

### 7.1 `linear_null`

For a linear future map, compute `V / kernel(Phi)` and the largest
continuation-stable null with `compute_stable_null`. The scorer generates the
continuation closure from the generator maps. It does not trust a bounded list
of words as complete.

### 7.2 `contextual_process`

Two process arguments are equivalent only when every licensed precontext,
future, reader, branch coarse-graining, and monoidal spectator gives the same
generated prediction. Future-only equality is merely a right congruence.

A positive contextual-process closure requires descent under every operation
claimed by the process gate. If tensor is unconstructed, monoidal contextual
closure is unconstructed as well.

### 7.3 `regional_congruence`

For candidate regions, equality must survive every licensed regional and
process context:

- meet, join, complement or relative complement;
- contact and causal predicates, or an explicit pricing of them;
- passive refinements;
- boundary gluing;
- horizontal pre- and post-composition;
- disjoint tensor when constructed.

Use `regional_profile_equivalence` for the finite Boolean part, then add the
process and gluing contexts independently. Missing closures do not count as
agreement.

The only registered regional quotient coordinate is

```text
PROFILE-EQUIVALENCE-ONLY | CONGRUENCE | INCONSISTENT.
```

No physical-region rung is reachable unless `contextual_process` is closed at
the declared scope and `regional_quotient=CONGRUENCE`.

## 8. Post-quotient atomlessness

Raw syntax atomlessness is proved symbolically with
`PrefixRegion.atomless_bipartition`. It is not the physical gate.

For the process quotient, the scorer must show for every nonzero quotient
class `[A]` that its generated split `L,R` satisfies

```text
[L] != [0]
[R] != [0]
[L] < [A]
[R] < [A]
[L] meet [R] = [0]
[L] join [R] = [A].
```

For the full generated question grammar, any claimed separator must be
constructed as a lawful preparation, question, continuation, and delayed
record reader. A bare call to `mu(A meet B)` is a static response, not a
process separator.

For an ideal `I`, independently use the exact criterion from addendum 2:

```text
for every A not in I, there exists B <= A such that
B not in I and A difference B not in I.
```

The ultrafilter-character mutant must give the atomic control. The constant,
finite-depth, zero-image, and volume-only controls remain separate.

The atomlessness coordinate remains exactly

```text
SYNTAX-ONLY | LOST-IN-QUOTIENT | PHYSICAL-IMAGE-ATOMLESS.
```

No finite support rank, finite leaf count, or absence of sampled atoms may
select `PHYSICAL-IMAGE-ATOMLESS`.

## 9. Stable records and recovery

Record evidence has three independent parts:

1. the branch process writes distinct record ports;
2. a generated delayed reader distinguishes them;
3. every word in the declared continuation grammar preserves a recoverable
   copy, up to registered relabeling.

For append-only trees, derive the prefix relation between input and reachable
output record words. A record is stable at this scope only if all reachable
outputs retain enough information for an exact recovery map and the delayed
reader is part of the same process law.

The scorer must also evaluate the finite record-recovery operations directly
on every source bit. Present orthogonality, a field name, an invariant
diagonal algebra, or a declared append operation is insufficient.

Reset, last-token erasure, copied-record, double-erasure, and delayed-reader
controls are all mandatory. Coarse-graining an effect that ignores a record
is not itself physical erasure of the underlying record port.

Every permanence statement is explicitly relative to the scored continuation
catalogue. No APR receipt may state absolute record permanence.

## 10. Regional-support locality and replacement grammars

`Kin(A)` and `SuppDyn(A)` must be generated independently in one calibrated
ambient effect space.

### 10.1 Kinematic construction

Construct `Kin(A)` from effects/actions of law-generated fillings whose
support is contained in `A`. Do not import `REGIONAL_SUPPORT_PRIMITIVES`
subspaces as the answer. Those matrices are controls against the independently
generated result.

### 10.2 Dynamic/support construction

For a common finite boundary with a full effect basis, reconstruct every
licensed complement-supported replacement map from its Boolean action. If a
replacement acts on valuations by `T_g`, the fixed-effect space is

```text
Fix(G_A) = intersection over g in G(complement(A))
           kernel(T_g^T - identity).
```

Rational mixtures are checked for positivity, unit-mass preservation, and
support in the relative complement. Automorphisms are checked as Boolean
automorphisms before their matrices are used.

Then compare `Kin(A)` and `Fix(G_A)` in the same calibrated effect space by
both subspace-inclusion residuals. Equal dimensions or an abstract
isomorphism do not pass.

### 10.3 Questions are not exterior replacements

The nonselective question satisfies

```text
Q_C^0 + Q_C^1 = identity.
```

It cannot supply nontrivial exterior replacement dynamics. Branch
conditioning is not silently retyped as a physical exterior replacement.
Only the independently generated replacement grammar may contribute to
`SuppDyn`.

### 10.4 Restricted child-swap control

For target `A=[00]`, use a common refined leaf basis and reconstruct the
semigroup generated by the registered child swaps in the complement
`[01] join [1]`. Compute its exterior orbits and full fixed-effect space.

If the restricted grammar leaves `m` independently invariant exterior
blocks, while `Kin(A)` contains only the single common exterior scalar, the
scorer reports the exact excess residual `m-1`. It must neither delete those
directions nor call them gauge.

The depth-two regrouping that exchanges `[01]` and `[10]` is the covariance
kill. Conjugate every relevant generator by the regrouping. If the conjugate
is not generated by the same replacement grammar at the transported region,
presentation covariance fails.

### 10.5 Intrinsic relative-complement grammar

The intrinsic grammar is scored independently. A positive regional-support
result requires:

- every generator fixes the target region and acts only in its relative
  complement;
- positivity and mass preservation;
- closure under word composition;
- transitivity on every declared finite exterior partition, rather than one
  selected presentation;
- closure under vertical conjugation/refinement;
- equality of the independently constructed fixed-effect and kinematic
  subspaces;
- recurrence under held-out refinements.

The scorer may not accept the textual words `all`, `transitive`, or
`vertical_closure` as proofs. It must generate the finite actions at each
registered boundary and verify the properties. An infinite all-partition
claim beyond the symbolic grammar remains scoped to the theorem actually
proved.

The locality coordinate remains exactly

```text
FAIL | VACUOUS-CONSTANT | REGIONAL-SUPPORT | CAUSAL-DYNAMIC.
```

`CAUSAL-DYNAMIC` is unavailable until an operational causal relation has
separately been derived or priced and used to define the exterior.

## 11. Comparisons

### 11.1 Process comparisons

For each candidate vertical map, compute:

- typing and invertibility where passive isomorphism is claimed;
- action on the linear stable quotient;
- action in every generated future, precontext, and spectator;
- vertical naturality with every compatible horizontal filling;
- whether rival lifts differ only in the complete stable null.

The scorer classifies only with the registered words

```text
DERIVED | NULL-QUOTIENT | PRICED | INCONSISTENT.
```

### 11.2 Mandatory RHL discriminator

Independently rebuild the common-boundary span, standard pairing, coherent
reference, local-isometry checks, future profiles, and null quotient from the
primitive matrices. The coherent screen is calculated, not stored.

The full-profile, null-profile, invalid-map, and phase-blind variants are
separate controls. Standalone Born weights do not complete the comparison
profile.

If no lawful regional-process continuation and stable record realizes the
coherent reference, the receipt distinguishes a mathematical cross-term
difference from an operational `PRICED` comparison. A separate comparator
namespace cannot silently supply the missing joint-law provenance.

## 12. Canonical predictive boundaries

For each boundary label, generate the complete future-profile column. Build
`PredictiveBoundary.from_profiles` inside the scorer.

A proposed configuration partition is:

- insufficient when a block mixes canonical profile classes;
- redundant when separate blocks lie in one canonical profile class;
- minimal at the catalogue only when it equals the canonical classes up to a
  natural relabeling.

For linear boundary spaces, independently check kernel equality and canonical
rank factorization. Do not use linear rank to count discrete configuration
classes unless operational linear mixtures have been declared.

The scorer must verify the universal property: every sufficient boundary
presentation factors through the canonical quotient, uniquely up to the
registered natural isomorphism and null directions. Literal
deletion-minimality is insufficient.

Appending a legal future effect must either factor through the same quotient
or explicitly demote the previous completeness/minimality scope.

The boundary coordinate remains exactly

```text
DECLARED | SUFFICIENT | MINIMAL-AT-CATALOGUE.
```

## 13. Contact, influence, and causal cycles

The scorer constructs both elementary contact candidates from the Boolean
data:

```text
C_min(A,B) iff meet(A,B) is nonzero
C_max(A,B) iff A and B are both nonzero.
```

It then generates every permitted joint filling and calibrated effect under
each relation. If deleting non-overlap contact changes no generated object,
non-overlap contact is not derived.

The contact coordinate remains exactly

```text
DERIVED | OVERLAP-ONLY | PRICED | NULL.
```

Causal influence is computed from interventions, not arrows, correlation, or
record order. Hold common past and boundary data fixed, apply each registered
intervention, generate the delayed stable reader, and compare its exact
distribution.

Common-cause correlation without an interventional change is a negative
control. Since a nonselective regional question is identity, conditional
question correlations do not by themselves derive regional causal
precedence.

If both directions are operationally supported, the scorer uses the
registered cyclic/fused/higher-order branch and never silently forces a
partial order.

The causality coordinate remains exactly

```text
DERIVED | UPPER-BOUND-ONLY | PRICED | CYCLIC-BLOCK.
```

Absence is absolute only at a proved complete intervention/reader scope.

## 14. E-37 family-level game

The scorer reconstructs the game before evaluating any family member:

```text
Family, Train, Holdout, Interventions, Tau,
BlindInterface, Resources, Gauge, Metric.
```

### 14.1 Family integrity

Independently canonicalize every regional member and compute:

- region-incidence structure;
- component and interface counts;
- topology/isomorphism signature;
- preparation and continuation resources;
- train/holdout separation;
- matched-pair blind projection.

For each matched pair, the blind inputs must be byte-identical after
canonicalization. Raw names, prefix words, insertion order, and relation-mode
strings may not leak through the blind interface.

### 14.2 Generated physical prediction

The regional rule must use one callable law and one parameter row across all
training and held-out members. The scorer constructs preparations, fillings,
questions, replacements, continuations, and delayed readers from the member's
regional structure. It then derives the entire registered outcome instrument.

A direct overlap lookup, stored response matrix, member-ID branch, canonical
serialization oracle, or per-member compiled circuit fails provenance even if
its final numbers agree.

### 14.3 Blind classes and resources

For every B0/B1/B2 row, enforce exactly the frozen available fields, memory
interface, state dimension, history depth, calibration slots, parameter
slots, number field, and precision. A rule factoring through a byte-identical
blind projection must return the same instrument on that matched pair.

Positive controls must show that each blind class is nonempty and can solve
registered easier rows. Adding memory or parameters changes the resource
class and cannot be counted as failure of the original class.

The E-37 conclusion is always relative to the frozen family and resource
classes. No output may say absolute non-eliminability.

## 15. One-law provenance and ontology role

The scorer computes a root hash from the actual primitive components used by
the construction, including:

```text
valuation parameter
question grammar and transition
decision-tree grammar
boundary and filling factory
horizontal composition
tensor constructor
vertical comparison system
reader/effect grammar
replacement grammar
contact/influence operations actually consumed
```

Every positive gate lists its ancestors. External comparator matrices,
fixture-supplied support matrices, hand boundary tables, and separately
declared influence arrows are controls until a typed composition proves that
they are representations of the same law.

The ontology section is a mandatory diagnostic, not a new primary-outcome
vocabulary. It states which role the process actually constructs:

```text
STATIC-RESPONSE
FIXED-ALGEBRA-CONDITIONING
RECORD-WRITING-ON-FIXED-ALGEBRA
REGION-REWRITING
```

This is derived from the generated output regional algebra. If every output
support is only `S meet C` or `S difference C` inside the predeclared algebra,
the process has not created or rewritten a region. Appending a recoverable
record may earn `RECORD-WRITING-ON-FIXED-ALGEBRA`; it does not by itself earn
`REGION-REWRITING`.

The scorer also states explicitly:

- finite words, matrices, and tree depth are representations;
- a finitely additive valuation is a law/state representation whose ontic
  status is not selected by the scorer;
- `p` is law data unless independently selected;
- a classical regional process does not select a quantum microscopic law;
- actualization remains a postulate;
- no metric, geometry, gravity, continuum, GR, QFT, particle, or Hamiltonian
  claim is entered.

## 16. Registered outcome classification

The scorer may emit only the primary words frozen by the parent pin and
addenda, with the addendum's inserted congruence block:

```text
APR-INCONSISTENT
APR-BLOCKED-AT-ATOMLESS-REGION-ALGEBRA
APR-BLOCKED-AT-BOUNDARY-GLUING
APR-BLOCKED-AT-TWO-ARROW-TYPING
APR-BLOCKED-AT-FUTURE-PROFILE-COMPLETENESS
APR-BLOCKED-AT-REGIONAL-CONGRUENCE
APR-ATOMLESS-KINEMATICS-CONSTRUCTED-COMPARISON-PRICED
APR-COMPARISON-QUOTIENT-CONSTRUCTED-BUT-DYNAMICAL-LOCALITY-FAILS
APR-DYNAMIC-REGIONAL-REFERENT-CONSTRUCTED-BUT-CAUSAL-ORDER-PRICED
APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED
APR-JOINT-POINT-FREE-REGIONAL-LAW-CONSTRUCTED
```

The addendum-authorized qualifier

```text
APR-STATIC-ATOMLESS-RESPONSE-CONSTRUCTED-PROCESS-UNBUILT
```

may be printed only when a static response is the highest honest
construction. It never supersedes an earlier registered block.

The strict primary is the earliest supported rung. Missing/unconstructed is
not pass. An exact numerical result cannot override an earlier ontology,
typing, congruence, gluing, completeness, or provenance block.

The process coordinate is exactly

```text
SYNTAX-ONLY | STATIC-RESPONSE-ONLY |
HORIZONTAL-CLASSICAL | HORIZONTAL-QUANTUM | INCONSISTENT.
```

Any claim of `HORIZONTAL-QUANTUM` additionally requires a nonzero generated
interference witness and all-input complete stable record division in the same
law. The separate coherent comparator cannot supply this coordinate.

## 17. Frozen primitive mutant transformations

Mutants are transformations of primitive objects or scorer algorithms. They
are not booleans that directly request failure, and they contain no stored
scientific answer. Each run must recompute the full relevant metric.

### M01–M08: algebra, probes, nulls, and arrow types

**M01 — finite-depth algebra/probe constructor.** Retain the unbounded raw
prefix grammar but replace the generic question/probe constructor by a
constructor accepting only words through a fixed finite depth.

**M02 — atomic character quotient.** Replace the complete regional profile by
the ultrafilter character generated by the frozen repeated-symbol branch.

**M03 — volume-only quotient.** Replace the contextual all-probe profile by
the scalar profile `A -> mu_p(A)` while leaving Boolean contexts available.

**M04 — incomplete probe list.** Retain the generic region algebra but expose
only the finite base probe catalogue; separately remove the appended
separator from the extended catalogue.

**M05 — one-step null shortcut.** Delete the registered length-two and
length-three words while retaining the continuation generator. A correct
closure algorithm still constructs all generator words; an algorithm that
uses only listed words changes its null diagnosis.

**M06 — null reactivation.** Add a typed continuation whose operator maps a
previously null basis direction into a direction read by the immediate
profile. Recompute the stable fixed point.

**M07 — refinement retyped as extension.** Present a profile-invariant passive
map as a horizontal growth candidate without changing its actual future
behavior.

**M08 — writer retyped as refinement.** Present a record-writing horizontal
filling as a vertical comparison without changing its generated record
behavior.

### M09–M16: comparisons, composition, locality, and provenance inputs

**M09 — fed comparison move.** Replace one marked comparison image by the
alternative fed image while retaining local typing and independently compute
the coherent reference.

**M10 — stable-null comparison move.** Apply the same raw comparison move
under the profile whose quotient identifies the two target directions.

**M11 — invalid local map.** Replace a comparison by the frozen non-isometric
or unit-nonpreserving map. It is not promoted to a priced lawful rival.

**M12 — composition mismatch.** Change one relation/branch cell in a declared
whole filling while leaving its factorization steps and endpoint boundary
types unchanged; run the reciprocal change on one factorization step while
leaving the whole fixed.

**M13 — constant laws.** Two submutants replace every generated calibrated
profile by, respectively, the zero law and a constant nonzero normalized law.
The operational quotient is recomputed before locality or faithfulness.

**M14 — equal-rank locality impostor.** Replace one kinematic calibrated basis
direction by a different direction while retaining its rank, and separately
replace generated exterior maps by hand-supplied matrices of the desired
rank.

**M15 — copy oracles.** Two submutants replace the uniform transition by a
canonical-serialization oracle and by a neutral-ID/label-hash oracle.

**M16 — relation erasure.** Remove the regional incidence/overlap relation
while retaining the registered blind interface, resources, labels, and
history length.

### M17–M24: boundaries, causality, and records

**M17 — lossy boundary.** Merge labels with distinct generated future-profile
columns or use the frozen lossy boundary presentation.

**M18 — redundant boundary.** Split one canonical profile class into multiple
presented labels or add a predictively duplicate coordinate.

**M19 — invertible boundary basis change.** Apply the frozen invertible basis
change to a minimal linear boundary without changing its generated future
behavior.

**M20 — future extension.** Append the frozen legal future row/effect and
recompute profile classes, nulls, and minimal boundaries.

**M21 — correlation without influence.** Use the common-cause arena and
compare interventions under common past/boundary data with the generated
delayed reader.

**M22 — causal cycle.** Use the bidirectional arena and reconstruct both
intervention-to-record directions.

**M23 — record reset.** Apply last-token erasure and complete reset after a
writer, then run the delayed reader.

**M24 — redundant copied record.** Copy the source record into both flags,
erase only one copy, and read the other; separately erase both copies.

### M25–M35: oracle, family, resource, quantum-scope, and jointness controls

**M25 — expected-value injection.** Inject a field carrying a final profile or
screen into a primitive object. Schema/provenance must refuse it or the scorer
must prove it is never read. Changing only that injected value may not change
any generated metric.

**M26 — identifier/relation-mode swap.** Exchange member IDs and textual
relation-mode labels while preserving the actual regional incidence objects.

**M27 — presentation relabeling.** Apply a nontrivial Boolean/prefix
automorphism and compatible token permutation to every input and transport
all generated outputs back before comparison.

**M28 — blind projection substitution.** Feed the canonical blind projection
to a rule in place of the regional member while keeping all declared blind
resources fixed.

**M29 — unseen held-out member.** Generate a new registered nonisomorphic
family member from the frozen family grammar without adding parameters or a
compiled row to the law.

**M30 — regional-rule blinding.** Force the purported regional rule itself to
factor through the blind projection and regenerate the entire outcome
instrument.

**M31 — resource-class extension.** Add a memory bit or parameter slot to a
blind rule. This is a sensitivity/control transformation, not a required
failure: the scorer must report that the adversary class changed.

**M32 — interference deletion.** Replace a claimed quantum coherent law by
its diagonal/incoherent version while retaining the same classical branch
weights. This mutant is mandatory whenever `HORIZONTAL-QUANTUM` is attempted
and otherwise remains a scope control.

**M33 — branch-law violations.** Run separate submutants that delete one
branch, duplicate one branch, normalize each nonzero branch separately,
insert a negative branch coefficient, and change one posterior restriction
cell.

**M34 — contact deletion/change.** Exchange `C_min` and `C_max` or delete
non-overlap contact while retaining overlap, regions, interventions, and all
other inputs.

**M35 — disconnected provenance.** Replace one law-generated object by a
byte-identical separately declared table/root and recompute one-law ancestry.

### P1–P8: process-algorithm mutants

**P1 — average coarse-graining.** Replace branch summation by an arithmetic
average.

**P2 — drop zero ports.** Remove typed zero branches and their boundary ports
before later composition.

**P3 — overwrite records.** Replace record append by last-bit replacement.

**P4 — freeze the valuation parameter.** Use one parameter row's branch
formula for every registered `p`.

**P5 — whitelist questions.** Reject a fresh scorer-created region while
continuing to answer every registered question ID.

**P6 — questions as exterior dynamics.** Use the nonselective identity
question as the entire exterior replacement semigroup.

**P7 — typing as composition.** Return a positive cospan verdict immediately
after `validate_gluing` without constructing the quotient apex or process
composite.

**P8 — sequential tensor.** Replace independent monoidal composition by one
of the two sequential orders.

### Replacement/locality mutants

**L1 — restricted child swaps only.** Remove the intrinsic
relative-complement grammar and compute the full fixed-effect algebra at each
target, including `[00]`.

**L2 — delete one child swap.** Remove a restricted generator while retaining
the claimed support/locality metadata.

**L3 — regrouping covariance.** Conjugate the restricted grammar by the
depth-two `[01]`/`[10]` regrouping and test generator/semigroup membership.

**L4 — intrinsic transitivity deletion.** Restrict the intrinsic grammar to
two or more exterior orbits while leaving its textual transitivity claim
unchanged.

**L5 — intrinsic conjugation deletion.** Omit one transported conjugate at a
refined presentation.

**L6 — supplied-subspace shortcut.** Return the frozen regional-support
matrices directly instead of deriving effects and replacement fixed spaces
from the law.

### Cospan/functor/gluing mutants

**G1 — apex-relation deletion.** Delete one internal relation from the whole
filling but not its steps, and reciprocally from a step but not the whole.

**G2 — wrong boundary identification.** Retain compatible boundary names but
alter one leg image used by the pushout.

**G3 — no pushout.** Stop at the core gluing-validation receipt.

**G4 — process assignment mismatch.** Keep cospan composites isomorphic while
changing one whole-filling restriction operator or record-port map.

**G5 — alternate-cut mismatch.** Change one direct depth-two/depth-three tree
cell while retaining each one-step question.

**G6 — overlap marginal mismatch.** Alter one global candidate so one local
marginal remains correct and the other moves.

**G7 — no global overlap extension.** Remove every compatible global
candidate while retaining the two agreeing local boundary tables.

Every mutant is run on a fresh in-memory copy. Mutant mode must not modify the
frozen fixture module or official artifacts.

## 18. Mutant evaluation rule

The scorer must not contain expected measured numbers for mutants. Instead,
each mutant is judged by a generic semantic or metamorphic predicate:

- exact identity or nonidentity of reconstructed objects;
- zero/nonzero residual;
- preservation or movement of a baseline generated profile;
- quotient-class refinement/coarsening;
- provenance-root continuity;
- scope or resource-class change;
- type-validity/refusal.

Controls intended to preserve physics under gauge, relabeling, invertible
basis change, redundant copies, or held-out generation are evaluated by
transported equality. Controls that alter a physical primitive are evaluated
by independently regenerated observables. The protocol does not pre-store
their numerical values.

All M01–M30 and M33–M35, P1–P8, L1–L6, and G1–G7 are mandatory executable
transformations. M31 is a mandatory resource-sensitivity transformation. M32
is mandatory for any quantum promotion and otherwise runs as a scope control.

## 19. Receipt schema

The receipt must contain at least the following canonical sections.

```text
schema
immutable_inputs
integrity
primitive_fixture_hash
law_roots
exact_arithmetic

regional_algebra
  canonicalization
  Boolean identities
  symbolic syntax split

process
  full_cone_question_maps
  branch_partition
  all_input_normalization
  identity
  composition
  alternate_cuts
  coarse_graining
  cospan_pushouts
  functorial_assignment
  tensor
  vertical_naturality
  process_coordinate

probes
  finite_catalogue
  appended_probe
  fresh_generated_probe
  completeness_scope

quotients
  linear_null
  stable_null_rank_history
  contextual_process
  regional_congruence

atomlessness
  syntax
  atomic_character_control
  physical_quotient_split_certificate
  atomless_coordinate

records
  port_write
  delayed_reader
  continuation_reachability
  recovery
  eraser_and_copy_controls

locality
  kin_provenance
  replacement_provenance
  replacement_positivity_mass_support
  restricted_fixed_effects
  intrinsic_fixed_effects
  inclusion_residuals
  refinement_conjugation
  locality_coordinate

comparisons
  process_comparisons
  RHL_mathematical_control
  operational_realization
  comparison_coordinate

boundaries
  generated_profiles
  canonical_classes
  lossy_control
  redundant_control
  invertible_change_control
  appended_future_control
  boundary_coordinate

contact
causality
overlap_gluing

E37
  family_signatures
  train_holdout_split
  matched_blind_hashes
  resource_ledger
  physical_generated_instruments
  blind_class_instruments
  relabel_and_erasure_controls
  class_relative_scope

one_law_provenance
ontology_role
law_selection
scope_walls
mutants
strict_primary
payload_sha256
```

Every section records exact evidence and the source-object hashes from which
the scorer derived it. `NOT-CONSTRUCTED`, missing, and out-of-scope states are
represented explicitly and never coerced to pass.

## 20. Integrity and replay contract

`apr_score.py` must:

1. authenticate every immutable input hash before scientific work;
2. authenticate the canonical fixture payload hash;
3. use exact rational/symbolic arithmetic for every load-bearing result;
4. reject decimals, floating tolerances, randomized scientific evidence,
   NumPy approximations, and implicit coercions;
5. accept explicit output and receipt paths only;
6. preflight both destinations before writing either;
7. refuse if either destination exists, leaving both byte-identical and
   creating no other artifact;
8. stage and publish the output/receipt pair so a failed second write cannot
   leave a partial first artifact;
9. refuse unknown arguments with return code 2 and no artifacts;
10. run from the repository tree, an alien working directory, and a true
    off-tree copy containing no `.git` directory;
11. make no runtime request to Git, repository history, the network, current
    working directory, or untracked scratchpads;
12. produce byte-identical official artifacts on two clean runs;
13. expose deterministic self-tests and every frozen mutant;
14. keep mutant artifacts separate from official artifacts;
15. preserve the frozen core and fixture bytes throughout.

Mandatory overwrite-order tests include:

- output exists, receipt absent;
- receipt exists, output absent;
- both exist;
- neither exists;
- an error after staging but before publication.

Refused runs leave no newly published artifact. Mutant runs operate on
in-memory transformed data or fresh temporary copies and never rewrite the
frozen fixture.

## 21. Candidate-generation and review handoff

The official transcript and receipt freeze before candidate prose. The paper
may quote only receipt evidence and independently proved analytical claims.
The candidate must state the ontology role, process coordinate, all quotient
coordinates, locality scope, contact/causality scope, law-selection status,
and every wall even if a higher numerical gate passes.

Hostile reviewers must independently rebuild the load-bearing semantic
objects without calling scorer measurement functions. They must attack:

- full-cone rather than preparation-row normalization;
- pushout/functor/tensor/naturality rather than cospan typing;
- generated probe completeness;
- contextual and regional congruence;
- post-quotient atomlessness;
- delayed record recovery;
- restricted versus intrinsic replacement fixed spaces and covariance;
- comparison operationality;
- boundary universal property;
- intervention rather than correlation;
- E-37 oracle leakage and resource parity;
- one-law provenance and the fixed-algebra-conditioning ontology boundary.

No review majority may override the strict earliest construction rung.

