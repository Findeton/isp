# Paper 18 mathematical hostile-review adjudication

Date: 2026-08-21

Status: **REJECT-AS-FROZEN / FORWARD REVISION REQUIRED / NO IMPLEMENTATION**

## 1. Authenticated corpus

| role | path | ordinary SHA-256 |
|---|---|---|
| candidate | `v16/paper-18-operational-structural-sectors.md` | `7f8c15b7205b044b06c63d44e4619e3749d6226f99af0c3b7015679cd01b6004` |
| construction note | `v16/note-paper18-operational-structural-sectors-construction.md` | `3a25bfb175624696685fcbd1db04fb5ff95572328bb345d9f97adda1dd46ae77` |
| frozen review protocol | `v16/note-paper18-operational-structural-sectors-review-protocol.md` | `7611586515f10c73a1c99c064254130407aa758a243fa496dc31faab662f25c6` |
| category/measure report | `v16/review-paper18-operational-structural-sectors-category-measure.md` | `972c647defffaccdfbc0d6f8e891e2386833478b411578981509a7df5421299f` |
| probability report | `v16/review-paper18-operational-structural-sectors-probability.md` | `cf12145ca420a55633c8e678e4ef3877e0964fbd1cc9118262b7305569453306` |
| physics/ontology report | `v16/review-paper18-operational-structural-sectors-physics.md` | `d67f61269640f6cda85772cf98988e6fb99fe2d6206791e6d8dc6ae4019a4fdc` |

All hashes match. The three reports were constructed mutually blind and
remained unstaged and uncommitted.

## 2. Combined verdict

The frozen candidate is rejected as a completed mathematical contract.

- Seat M: `REJECT`.
- Seat P: `REVISE`.
- Seat O: `REVISE`.

The rejection is not caused by Python, Rust, serialization, runtime, or an
implementation. It is a semantic typing failure in the candidate's first
sector construction.

No review refuted the accepted-law branching fork:

> Paper 13D simultaneous fusion has one unmarked target; random cross-bond
> values are histories inside that target, and retaining any invariant of
> them inherits its probability by Gamma pushforward.

No review derived a physical channel measure, positive character, channel
law, whole selector, chronology, dimension, geometry, or actualization.

## 3. First decisive blocker

Definition 2 says that two response profiles are behaviorally
indistinguishable when there is a typed correspondence matching all response
probabilities. It does not define the correspondence objects or require:

- identity arrows;
- totality on the complete experiment catalogue;
- invertibility;
- type preservation;
- measurable or natural dependence on contexts;
- closure under composition; or
- compatibility with the accepted presentation groupoid.

Therefore the stated relation need not be transitive. The Seat-M
counterexample has profiles

    S = {s0}, T = {t0,t1}, U = {u1}

with response values `0`, `(0,1)`, and `1`. One partial correspondence pairs
`s0` with `t0`; another pairs `t1` with `u1`. Both preserve their paired
responses, but their composite is empty and no response-preserving
correspondence relates `S` to `U`.

Consequently the notation

    [Prof_Gamma(s)]

does not denote a defined equivalence class. The current coordinate
`P18-SECTOR-REFERENT-CONTRACT-CONSTRUCTED` is demoted.

## 4. Additional exact blockers and scope corrections

### 4.1 Restrictions are not a functor

The candidate supplies maps `r_(B,B')` but does not require

    r_(B,B) = id
    r_(B',B'') r_(B,B') = r_(B,B'')

or prove descent through presentation-groupoid orbits. An unrooted
two-occurrence interface immediately defeats a rule that retains “the first”
occurrence.

Paper 13D uniform deletion is a stochastic covariant operation, not
automatically a deterministic restriction map. A valid successor must
separate exact restriction along a declared marked inclusion from stochastic
uniform deletion.

### 4.2 The global-classification branches are not exhaustive or orthogonal

An inverse system over all finite subsets of an uncountable index set has
finite levels and a closed autonomous inverse limit with a non-countably
generated cylinder sigma algebra. It is neither standard Borel nor
contextual/nonclosed.

Moreover cardinality, measurable type, measure type, and closure are
different coordinates. A system may be both contextual and finite, or
standard Borel with atomic, nonatomic, or mixed measures. `HYBRID` also
overlaps standard-Borel disjoint unions.

### 4.3 Pairwise-finite kernels need not be closed under composition

Definition 10 requires each channel measure to be finite but permits an
iterated convolution whose two bracketings are both infinite. Equality
`infinity = infinity` does not define a finite positive convolution object.
Finite-word closure, or an equivalent convolution-boundedness condition, is
missing.

### 4.4 Deletion transfer lacks a base convention

The symbol `D` in Section 7.2 does not say whether it is raw deletion
multiplicity, a normalized class-level Markov kernel, a labeled coefficient,
or a stabilizer-weighted coefficient.

With one class at every size, raw multiplicity is `n+1` while uniform
deletion probability is `1`. The displayed transfer equation gives
different answers under those two conventions.

The invariant primary statement must be projectivity of probability
measures through an explicitly constructed deletion Markov kernel. Any
weight-ratio formula must then declare its orbit, labeled, or groupoid base
and all automorphism factors.

### 4.5 Three bounded probability qualifications

1. The countable and continuous additive examples have many characters but
   every character produces the same deterministic conditional kernel. They
   prove raw-character nonuniqueness, not distinct physical channel laws.
2. Theorem 7 should compare strictly positive occurrence propensities. At
   `q=0`, conditioning on composition is conditioning on a null event and is
   not determined by the whole probability measure.
3. The whole-selector residue is currently a set or moduli problem, not a
   defined vector space or manifold. Its “dimension” must remain undefined
   until its carrier, operations, topology, and quotient are constructed.

### 4.6 Product emission is incomplete

The current product vector omits two walls already present in its own ladder:

    P18-SIGNATURE-NOT-EVALUATED
    P18-CURVATURE-NOT-EVALUATED

This is a bounded reporting correction and changes no physics.

## 5. Surviving mathematical results

The following results survive, at their stated conditional scope.

1. Finite bounded spaces do not imply a finite or countable global sector
   space.
2. The accepted Paper 13D simultaneous fusion realizes the
   structural/history branching fork and supplies no new whole-complex odds.
3. Given an independently physical finite positive associative measurable
   kernel and a positive character, the displayed transformed kernel is
   normalized.
4. Associativity of the supplied measure kernel gives equality of final
   probability marginals for arbitrary measurable sets.
5. Subject to finiteness, the displayed `h` transformation leaves the
   conditional channel kernel invariant.
6. Every associative Markov convolution has the representation `M=P, d=1`,
   so representability discovered after fitting is not selection.
7. A unique channel law conditional on composition does not determine a
   strictly positive composition-occurrence propensity.
8. Orbit weight and inverse-automorphism groupoid weight are physically
   different base choices unless an additional theorem selects one.
9. Exact projectivity constrains selector families but need not make them
   unique.
10. Stable records, normalization, decoherence, formal complex phases, and
    desired downstream geometry do not supply the missing selector.

These are preserved results, not sufficient grounds for implementation.

## 6. One coherent forward mathematical revision

This section records the smallest architecture that addresses all three
reports together. It is not applied to the rejected candidate by this
adjudication.

### 6.1 Replace pairwise profile correspondences by a profile groupoid

For every bounded exterior, define a groupoid whose objects are complete
typed experiment-profile functors and whose arrows are total invertible
typed measurable natural isomorphisms preserving every admitted context,
intervention, reader, and response kernel. Identities, inverses, and
composition are literal groupoid operations.

Behavioral indistinguishability is then isomorphism in this groupoid. The
physical sector retains both the kinematic structure orbit and the complete
profile object; behavioral isomorphism does not erase nonisomorphic physical
structure.

### 6.2 Split exact restriction from physical deletion

Define an index category of bounded marked exteriors. Exact restriction along
a typed marked inclusion is a contravariant functor or stack with identity,
composition, and presentation-equivariant descent.

Unmarked uniform deletion is separately a Markov kernel between point-free
class spaces. It is used for projectivity of measures, not as a deterministic
pointwise restriction.

### 6.3 Report global type as a product, not one exclusive label

Use separate coordinates for:

- cardinality: finite, countable, uncountable, or unknown;
- measurable type: standard Borel, nonstandard cylinder measurable, other,
  or unconstructed;
- measure type: atomic, nonatomic, mixed, or unconstructed;
- autonomous closure: closed or contextual/nonclosed; and
- topology: none, derived topology class, or unconstructed.

This admits finite, countable, continuous, hybrid, and nonstandard systems
without forcing them into overlapping bins.

### 6.4 Strengthen positive convolution closure

Require every finite iterated channel convolution used by the law to be a
finite measure and require associativity as equality of finite measures.
If only transformed probability kernels are finite, state that weaker object
instead and do not call the raw channel measure a finite convolution monoid.

### 6.5 Make projectivity primary

Construct an exact point-free deletion kernel `K_(n+1,n)` and require

    P_(n+1) K_(n+1,n) = P_n.

Only after choosing a declared orbit, labeled, or groupoid base may this be
rewritten as a transfer equation for unnormalized weights. Raw multiplicity
then appears with the uniform `1/(n+1)` factor and the appropriate
automorphism ratios.

### 6.6 Keep the remaining corrections literal

- Compare `q1,q2` in `(0,1]` in the occurrence-propensity theorem.
- State explicitly that the additive controls vary characters while leaving
  their deterministic conditional kernels unchanged.
- Treat the selector residue as an untyped moduli object until a separate
  theorem supplies algebraic or manifold structure.
- Emit every permanent wall coordinate.

## 7. Adjudicated current product vector

    P18-SECTOR-REFERENT-CONTRACT-UNCONSTRUCTED
    P18-BOUNDED-SECTOR-CENSUS-UNCONSTRUCTED
    P18-GLOBAL-SECTOR-COMPLETION-UNCONSTRUCTED
    P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED
    P18-NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED
    P18-PHYSICAL-CHANNEL-MEASURE-UNCONSTRUCTED
    P18-COMPOSITION-CLOSURE-UNPROVEN
    P18-POSITIVE-CHARACTER-UNTESTED-NO-PHYSICAL-CHANNEL-MEASURE
    P18-CHANNEL-LAW-UNCONSTRUCTED
    P18-WHOLE-SELECTOR-UNCONSTRUCTED
    P18-ACTUALIZATION-UNCONSTRUCTED
    P18-CHRONOLOGY-NOT-EVALUATED
    P18-DIMENSION-NOT-EVALUATED
    P18-SIGNATURE-NOT-EVALUATED
    P18-METRIC-NOT-EVALUATED
    P18-CURVATURE-NOT-EVALUATED
    P18-GRAVITY-NOT-EVALUATED

## 8. Authorization boundary

The rejected candidate remains frozen at its authenticated hash. This
adjudication does not alter it.

A revised mathematical candidate incorporating Section 6 requires explicit
user authorization. It must be frozen as new bytes and independently
reviewed before any bounded sector census or implementation. There is no
automatic repair chain, and no physical parameter, sector type, measure,
dimension, geometry, or state may be selected during revision.
