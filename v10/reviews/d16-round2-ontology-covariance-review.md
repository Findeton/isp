# D16 ontology/covariance review — round 2

**Date:** 2026-07-11  
**Review verdict:** **PASS FOR THE NARROWED FINITE POSET-RELABELING THEOREM**  
**Formal D16 verdict retained:** **`INCOMPLETE-INVESTIGATION`**

## Executive finding

The round-1 category and claim-scope blockers are substantially closed.

The executable now represents boundary ports with an element, kind and owner.
It requires nonempty type/owner fields, valid indices, antichain support,
past-minimal/future-maximal polarity and disjoint past/future elements.  Every
relabeling transports the complete boundary metadata, and typed-boundary
automorphisms are counted against that transported object.

Regional gluing is no longer positional.  It matches the entire declared
future/past interface by `(kind, owner)`, identifies those extremal elements,
takes transitive closure, transports the outer boundaries and rejects a type
mismatch.  Independently relabeling both regions leaves the sewn interval,
automorphism and linear-extension counts unchanged.

The repair does not pretend that interval actions factorize.  It demonstrates
the cross interval, rejects naive regional addition and recomputes the action
once on the quotient order.  The theorem explicitly says this is a
whole-composite evaluator; a factorizable sewing law would still need
boundary/corner factors and a measure.

The global-clock wording is also repaired.  Linear extensions are now used
only to show that a supplied whole-order scalar is independent of its chosen
presentation.  No measure on presentation fibers, sequential transition law,
local support rule or diagram-generation algorithm is inferred.

The scientific theorem is therefore supported at this scope:

```text
ON THE FROZEN FINITE TYPED POSET CENSUS,
POSET RELABELING + ORDER-INTRINSIC INTERVAL DEPENDENCE
DO NOT SELECT ONE BINARY COEFFICIENT PACKET.
```

It remains a combinatorial nonselection theorem, not physical
diffeomorphism/general covariance.  The theorem and source docstring now say
so.  Quantum measure, D14 records, join/birth dynamics, BDG provenance,
matter, stable `3+1`, cones, units and `G` remain absent.  V9 remains closed.
Formal D16 therefore correctly remains incomplete.

## Exact reproduction

The repaired standard-library source was copied to an isolated temporary tree.
Normal and optimized Python produced byte-identical stdout and byte-identical
packets.  The regenerated packet matches the primary artifact.

```text
checks                         = 26/26
normal stdout SHA-256          = bbc674b8052e7e1a7ca9aca438f82eb2cd644b1ee82cb8c0ada392b43fc6e037
-O stdout SHA-256              = bbc674b8052e7e1a7ca9aca438f82eb2cd644b1ee82cb8c0ada392b43fc6e037
generated JSON SHA-256         = 8882ce9ff680336ef747fefe500f9d9927d6b273081017faa09fb932c2423640
primary JSON SHA-256           = 8882ce9ff680336ef747fefe500f9d9927d6b273081017faa09fb932c2423640
semantic SHA-256               = a3931af2f999a7381b86792f03750420c3be411d83c7a0598cb6dfe6eb9e10a6
source SHA-256                 = 861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

All normalization and automorphism weights now use exact
`fractions.Fraction`; the round-1 binary-float weakness is closed.

## Round-1 closure ledger

| Round-1 opening | Round-2 adjudication |
|---|---|
| “general covariance” used for label invariance | **CLOSED in theorem/docstring.** Principal claim is finite poset relabeling; continuum diffeomorphism covariance denied.  Two receipt labels still merit wording cleanup. |
| typed boundary/ownership absent | **CLOSED for the frozen finite class.** Type, owner, polarity, extremality and transport execute. |
| positional gluing | **CLOSED.** Full declared interface is matched by type/owner and tested under independent relabeling. |
| gluing obstruction lacked replacement | **CLOSED at quotient-evaluator scope.** Composite action is recomputed once; factorized local sewing remains open. |
| linear extension promoted toward no-global-clock law | **CLOSED by narrowing.** Presentation independence only; no growth/measure claim. |
| interval dependence called physical locality | **SUBSTANTIALLY CLOSED.** The theorem says order-intrinsic and denies microcausality; one explicit quasilocal/nonlocal sentence is still useful. |
| `1/Aut` arithmetic inexact | **CLOSED.** Exact rationals. |
| automorphism factor treated as selected measure | **CLOSED in prose by supplied-convention warning; receipt label could be sharper.** |
| weak common-phase test | **CLOSED.** Action-difference and phase-ratio vectors are both nonconstant over expanded census. |
| coefficient census under-resolved | **CLOSED.** Sewn chain exposes odd `N_1`; all 16 packets have 16 signatures. |
| quantum measure/records/geometry absent | **OPEN, HONESTLY.** No promotion occurs. |

## Typed boundary ontology

**PASS for the finite implemented class.**

`BoundaryPort` now carries:

```text
element;
kind;
owner.
```

`CausalOrder` validates:

- strict irreflexive, asymmetric, transitively closed order;
- no element simultaneously on past and future boundaries;
- unique, in-range boundary elements;
- nonempty type and owner;
- antichain boundary support;
- minimal past ports; and
- maximal future ports.

The frozen V and Lambda witnesses use two same-kind legs with distinct owners;
the diamond uses a screen owned by `cell-D`.  Exhaustive relabeling transports
kind and owner while changing only the element address.  The automorphism
counts consequently shrink when boundary metadata breaks otherwise available
symmetries, exactly as expected.

This closes the false round-1 “boundary ownership” label, which previously
checked only integer validity.

### Finite-class limitation

`glue_typed` keys an interface by `(kind, owner)` and requires those keys to be
unique.  Thus the current class cannot glue two distinct same-kind ports owned
by the same component without adding a collar/port identity.  The executed
single shared interface is valid, and the theorem is explicitly frozen and
finite.  A general multiport D14/SHARD interface should later add `collar_id`
or another persistent port identity.  This is nonblocking for the present
witness.

## Typed extremal sewing

**PASS as quotient construction and obstruction.**

The two chain regions declare:

```text
left.future  = (shared, cell-C)
right.past   = (shared, cell-C)
```

with separate typed outer past/future ports.  Sewing:

1. matches the whole interface key set;
2. identifies each right shared element with its matching left element;
3. assigns fresh indices to all other right elements;
4. transports relation edges;
5. takes transitive closure; and
6. returns the left outer past and mapped right outer future.

The result is the three-chain with interval counts `(2,1,0)`.  A mismatched
type rejects.  Permuting both regional presentations before sewing leaves the
sewn combinatorial invariants unchanged.

For `S=N_1`, the regional values sum to zero while the quotient value is one.
The code therefore computes the composite action **once on the quotient** and
does not count the shared point or cross interval twice.

This is not a local/factorizable sewing theorem.  Recomputing all intervals on
the complete quotient can require whole-composite information.  The theorem
states that a factorized regional amplitude would still need explicit
boundary/corner/cross factors.  No locality or online-growth inference is
made.

## Relabeling covariance versus physical covariance

**PASS after narrowing.**

The theorem title and main result now say “poset relabeling.”  They also state:

```text
This is not a theorem of continuum diffeomorphism covariance or physical
microcausality.
```

That is the correct interpretation.  The executable proves invariance of the
relation, typed boundary metadata, interval counts and scalar action under
finite isomorphism.  It does not provide a state, measure, matter fields,
observables, continuum limit or physical gauge quotient.

Two executable labels still use broader shorthand:

```text
exactly generally covariant under relabeling;
covariance plus interval locality does not select one action.
```

They should become:

```text
exactly invariant under finite typed-poset relabeling;
relabeling covariance plus interval dependence does not select one action.
```

The source docstring, theorem and packet ceiling already enforce the narrow
meaning, so this is a nonblocking receipt-wording repair.

## Linear extensions and no global clock

**PASS at presentation-independence scope.**

The exact scalar receives a completed `CausalOrder`, not a construction
schedule.  Repeating it over every linear extension therefore confirms that
the scalar factors through the completed order.  The repaired theorem no
longer calls this a whole-history measure result.

It explicitly denies:

```text
a measure over presentations;
a locally computable sequential growth rule;
a support law choosing which orders occur.
```

This is the correct resolution.  A labeled growth process could still weight
orders by path multiplicity or transition products unless a quotient/pushforward
theorem removes that dependence.  D16 has not supplied such a process and does
not claim to have removed its clock.

## Automorphisms and measure

**PASS as an obstruction, not a selected convention.**

Typed-boundary automorphism counts and exact rational values are now
reproducible.  The chain and antichain give `1` and `1/24` under the displayed
`1/|Aut|` groupoid convention.

Relabeling covariance does not select that convention.  Unit weight per
isomorphism class, a labeled sum, a labeled sum divided by `n!`, or a groupoid
measure have different bookkeeping unless the full state/measure construction
specifies them.  The theorem correctly says an explicit orbit convention is
required.

The check label “unlabeled orbit measure” would be safer as “one candidate
groupoid orbit weight.”  No physical measure conclusion depends on it.

## Interval dependence and coefficient nonselection

**PASS at algebraic action-family scope.**

The expanded census contains the original five orders plus the sewn
three-chain.  That extra object exposes `N_1`, producing 16 distinct phase
signatures for the 16 binary packets.  `N_0` and `N_2` have nonconstant action
difference and phase-ratio vectors, so neither one additive constant nor one
global phase relates them across the census.

This proves coefficient nonselection inside the frozen scalar family.  It
does not require a quantum measure because the objects being distinguished
are action functionals.  It also does not yet prove different observed
probabilities; that requires common-boundary alternatives, state/measure and
interference/decoherence data.

`N_k` scans comparable pairs and their open intervals.  This is intrinsic to
the order but can be quasilocal/nonlocal in causal-set terminology.  It is not
nearest-neighbor locality or continuum microcausality.  The theorem's explicit
denial of microcausality is adequate; adding the words “quasilocal/nonlocal”
would close C2 textually.

## Missing physical packet

**Open and honestly retained.**

Pure phases still do not define a normalized quantum measure.  D16 supplies no
alternative-order domain beyond illustrative pairs, boundary state,
decoherence functional, orbit convention, regulator/limit or convergence
law.

It also supplies no:

```text
D14 pointer environment or record instrument;
commit/protected future/live collar;
multi-component join entitlement;
matter sector;
published BDG coefficient packet and scale provenance;
stable manifoldlike 3+1 phase;
influence/dispersion observable;
cone anisotropy prediction;
proper-unit bridge or G.
```

The theorem and receipt list these absences.  No physical general covariance,
growth law, record law or geometry result is inferred from the combinatorial
cells.

## V9 adjudication

**CORRECTLY WITHHELD.**

C9/C10 remain unfired.  There is no complete coefficient/state/measure/record
packet, no fixed prediction for dimension or cone scale dependence, no unit
bridge and no pair of complete candidates with differing non-tunable
predictions.

A dimension-tagged illustrative packet or future BDG coefficients matched in
a chosen dimension would not make dimension emergent.  A sprinkling into a
continuum Lorentzian manifold would likewise input the cone context.  D16 runs
no V9 test and claims none.

## Gate adjudication

| Gate | Round-2 result |
|---|---|
| C0 exact partial orders | **PASS for the finite typed/owned extremal-boundary class.** |
| C1 label gauge | **PASS as finite typed-poset relabeling covariance only.** |
| C2 locality meaning | **PASS in substance; add explicit quasilocal/nonlocal word.** |
| C3 coefficient nonselection | **PASS for the expanded finite scalar family.** |
| C4 dimension provenance | **OPEN; illustrative tags only, honestly.** |
| C5 regional gluing | **PASS as typed quotient gluing plus nonadditivity obstruction; factorized local sewing remains open.** |
| C6 quantum measure | **OPEN; missing-data obstruction retained.** |
| C7 records and birth | **OPEN; no D14 packet.** |
| C8 no global clock | **PASS only as presentation independence; physical growth law open.** |
| C9 geometry predictions | **OPEN; no dimension/cone/unit/`G` packet.** |
| C10 empirical discriminator | **OPEN; V9 correctly withheld.** |
| C11 hostile closure | **Round-2 ontology review passes the narrowed theorem; full D16 remains incomplete.** |

## Verdict

**PASS FOR THE NARROWED FINITE POSET-RELABELING THEOREM.**  Typed owner metadata,
extremal boundary validation, relabeling transport and quotient gluing are now
real.  The action is recomputed once on the sewn order, and the code no longer
pretends this gives a factorized local law.  Linear extensions establish only
presentation independence.

The accepted exact result is:

```text
FINITE TYPED-POSET RELABELING COVARIANCE             PASSED
TYPED EXTREMAL QUOTIENT GLUING                       PASSED
NAIVE LOCAL ACTION ADDITIVITY                        REFUTED
16-PACKET INTERVAL COEFFICIENT SELECTION             REFUTED
PHYSICAL GENERAL COVARIANCE/LOCAL GROWTH             NOT DERIVED
QUANTUM MEASURE/RECORDS/BDG/GEOMETRY/SCALES          OPEN
V9                                                     WITHHELD
```

Formal D16 correctly remains:

```text
INCOMPLETE-INVESTIGATION.
```

Only minor receipt wording and future multiport identity hardening remain for
the finite theorem; neither reopens its exact nonselection result.
