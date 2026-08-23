# Paper 03 v2 pin audit

## Causal-frontier category feasibility

Date: 2026-08-22

Status: **RESULT-NEUTRAL AUTHOR AUDIT**

Disposition: **FIT-FOR-CONSTRUCTION**

This audit awards no Paper 03 v2 coordinate. It tests only whether the frozen
repair pin defines a coherent finite mathematical construction and whether its
scope can be respected without introducing new physics.

## 0. Authentication

| Artifact | SHA-256 | Size | Binding commit |
|---|---|---:|---|
| `v17/note-paper03v2-causal-frontier-repair-pin.md` | `d9df65a0bfb39576663396f75476db9c3be9413ebbd281853162411e9376ce73` | 628 LF / 25,109 bytes | `1967d7b` |
| `v17/note-paper03-hostile-review-adjudication.md` | `165fa3690dda1613152bfa94c2188823a296063678a5ebdea8be5dcd34e796b7` | 339 LF / 16,311 bytes | `dab4a9c` |

The pin was read completely. The v1 adjudication supplies exactly the two
semantic repairs frozen in the pin. No construction or review truth is
presumed here.

## 1. Exact finite category model

For a fixed admitted packet $\Xi$, the lower sets of the finite slot poset are
ordinary boundary indices. Let $G_\Xi$ have one object for each fully typed
boundary $B_{\Xi,D}$ and one directed edge for each admitted mechanism filling
one enabled slot. The free path category exists without further assumptions:

$$
\mathcal P_\Xi=\operatorname{Path}(G_\Xi).
$$

Identity is the empty path; composition is concatenation; associativity is
literal associativity of finite lists modulo the standard path convention.
Every exactly matching codomain/domain pair composes. All physical
admissibility work occurs when primitive edges are admitted, before category
composition.

This is the minimal exact repair of the v1 defect.

## 2. Three decisive finite controls

### 2.1 Timelike chain

Let

$$
V=\{-,+\},\qquad -\prec+.
$$

The lower sets are

$$
\varnothing,\quad\{-\},\quad\{-,+\}.
$$

The early generator has type

$$
B_\varnothing\longrightarrow B_{\{-\}},
$$

and the later generator has type

$$
B_{\{-\}}\longrightarrow B_{\{-,+\}}.
$$

There is no lower set $\{+\}$ and therefore no later-first generator. The v1
counterexample cannot be formed. No partial composition rule is required.

### 2.2 Spacelike/incomparable pair

Let $V=\{a,b\}$ with no order relation. The lower sets are

$$
\varnothing,\quad\{a\},\quad\{b\},\quad\{a,b\}.
$$

There are two paths from $B_\varnothing$ to $B_{\{a,b\}}$. They are different
free-category arrows before physics. If the full registered mechanism maps
causally factorize, their equality is added as a congruence generator. Thus
schedule independence is a theorem about the evaluation, not a hidden axiom of
path composition.

### 2.3 Procedure alternatives at one slot

Let $m$ and $m'$ be two physical mechanisms with the same exact interface at
one enabled slot $v$. Then

$$
g_{v,m,D},g_{v,m',D}:B_D\longrightarrow B_{D\cup\{v\}}
$$

are parallel arrows. They may be operationally equivalent while remaining
distinct procedures, exactly as required by Paper 02 v2 contextuality typing.
The frontier repair therefore does not erase the prequotient physical
procedure distinction.

## 3. Identity versus explicit skip

The empty path at $B_D$ leaves the slot $v$ available. An explicit skip moves
to $B_{D\cup\{v\}}$ and removes that opportunity from every compatible future.
They have different target objects and different continuation sets. Hence the
pin is correct to distinguish them even if all immediate system observables
are unchanged.

This is laboratory protocol provenance, not a claim that “nothing happening”
creates a microscopic spacetime atom.

## 4. No hidden global clock

A lower set records which causal opportunities have been completed, not the
order in which incomparable slots were serialized. For an incomparable pair,
both serializations end at the same $D=\{a,b\}$. No integer rank or loop index
is part of the object.

The construction therefore uses a finite partial order already declared by
the experimental comparator. It neither derives nor assumes a universal
foliation. A candidate that stores the topological-sort index in a boundary,
kernel, or reader fails C5/C20 and attacks 7/32.

## 5. Adaptive control feasibility

Finite classical adaptation can be represented by a record register already
present at the source boundary and a controlled mechanism at the next slot.
All branch mechanisms share one frontier target. A false guard uses the typed
skip mechanism. Because guards may read only predecessor records, no branch
can enable a causal predecessor after a successor.

The construction must define the controlled operation as one complete
instrument/channel with a classical input register. It must not create a
different category object by conditioning on a zero-support value.

## 6. Evaluation functor obligation

The path category alone is syntax. The construction must define a typed
evaluation functor

$$
\operatorname{Ev}_\Xi:\mathcal P_\Xi
\longrightarrow\mathcal K_\Xi,
$$

where $\mathcal K_\Xi$ is the admitted category of algebraic operations,
instruments, classical controls, and standard-Borel kernels for the packet.
It must prove:

1. empty paths evaluate to identities;
2. concatenation evaluates to chronological composition;
3. every branch/output interface matches its target boundary;
4. trusted randomization is affine with exposed source lineage;
5. every map preserves the admitted state/predictive-object class; and
6. certified exchange generators lie in the kernel congruence of
   $\operatorname{Ev}_\Xi$.

This obligation is already implicit in V2-T5 through V2-T16 and in the
scientific question. Printing it explicitly in the candidate is mandatory.

## 7. State and measurable closure

The state closure condition is well typed. Algebraic statehood after a CP
update is not enough: the posterior and nonselective state must remain in the
packet's declared class whenever that class is used as a boundary type.

For finite outcomes the existing normalization proof applies. For a
nonatomic standard-Borel outcome, a CP-valued measure and a measure kernel are
the correct objects. The pin correctly forbids a canonical posterior on every
zero-mass singleton.

No impossibility appears, but preservation of a narrow Hadamard/microlocal
class is model-specific and must remain conditional.

## 8. Packet covariance feasibility

The pin correctly separates three maps:

1. covariant observable transport along a `Loc` arrow;
2. contravariant state pullback; and
3. full experiment transport only along an explicitly supplied packet
   isomorphism/intertwiner.

The full packet tuple can be transported along a comparator isomorphism when
the system/probe/coupled theories, scattering map, supports, source state,
effects, slot structure, records, and readers all intertwine. A proper
embedding still supplies no canonical forward state extension.

This restriction is coherent and avoids the v1 full-packet covariance gap.

## 9. Operational quotient feasibility

Within one registered packet/skeleton, all procedures under comparison have
objects in one small path category. Complete one-hole contexts are paths and
registered constructors before and after a tested arrow. If the context family
is explicitly closed, equality under every complete tester is stable under
precomposition, postcomposition, controlled composition, and trusted mixing.
It is then a congruence.

The quotient is deliberately packet/reachable-interface scoped. The pin does
not require comparison of arbitrary unrelated slot skeletons. A construction
must not silently claim a universal quotient across packets without a typed
common refinement or packet morphism.

## 10. Rest-frame scope

The narrowed statement is physically correct. A law can be locally covariant
while a material state breaks Lorentz symmetry. A KMS state may select an
inertial rest frame; that state-selected frame is physical packet data.

What is excluded is an undeclared dependence on how incomparable laboratory
operations were listed. This is exactly the map-level schedule theorem. It
does not exclude idle microscopic preferred structure.

## 11. Ontology audit

The slot poset is a finite laboratory control object. It is not:

- a set of fundamental happenings;
- a lattice of spacetime points;
- a causal-set ontology;
- a physical clock;
- a volume or duration measure;
- the actual history of the universe; or
- a selector of one outcome.

The construction remains comparator mathematics. No v16 happening, order,
metric, FLRW, selector, fusion, or gravity object is imported.

## 12. Feasibility of the target/control/attack package

The 20 targets are finite and mutually typed. The 28 controls cover both
directions of the category, covariance, probability, frame, and ontology
claims. The 40 hostile attacks include the v1 counterexample, hidden-clock and
occurrence-collapse failures, update/measurability defects, source correlation,
Bell/model collage, type-III/tensor traps, and all downstream promotions.

No target demands a computation over an unbounded family. General finite-slot
claims are proved structurally; named Bell/split/KMS examples remain
existential or conditional controls.

## 13. Construction obligations

The candidate must make the following explicit rather than rely on this audit:

1. the evaluation functor and its target operation/kernel category;
2. exact boundary-interface update for every primitive mechanism;
3. adaptive control as a complete classical-register morphism;
4. independent product-probe source in every factorization theorem that uses
   it;
5. the exact localization/Haag substitute;
6. state-class closure and normality;
7. complete packet-isomorphism intertwiners;
8. context-family closure before quotient congruence;
9. the KMS/state-rest-frame positive control; and
10. the slot-poset no-ontology wall in every product/outcome statement.

Failure of any item is scientific/type failure, not a prose fix.

## 14. Disposition

**FIT-FOR-CONSTRUCTION.**

The pin has a coherent finite model, closes the exact v1 category
counterexample without a partial composition rule, retains procedure
contextuality, and introduces no new physical postulate. The remaining duties
are theorem construction and independent review, not implementation.

No Paper 03 v2 coordinate is awarded. One mathematics-only construction may
begin at a new path. Paper 04, internal clocks, spacetime emergence,
matter--geometry dynamics, and gravity remain closed.
