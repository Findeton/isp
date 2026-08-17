# JRH hostile delta adjudication — the finite boundary result stands; the history-to-instrument bridge requires repair

**Date:** 2026-08-17  
**Frozen repaired target:** commit `99f2352`  
**Frozen delta protocol:** commit `1c225a2`  
**Panel grades:** OPERATOR `ACCEPT-WITH-FIXES`; GRAVITY
`ACCEPT-WITH-FIXES`; QUANTUM `ACCEPT-WITH-FIXES`.

## 1. Frozen independent evidence

The three reports were written without cross-reading and frozen verbatim in
separate commits before this adjudication:

| seat | report | SHA-256 | grade |
|---|---|---|---|
| operator / exact demolition | `v16/review-jrh-operator-delta.md` | `66c0569c1935e3cab41eed31e2fcc776ab0130d06e6db86c1fd2bf2048ebfc06` | `ACCEPT-WITH-FIXES` |
| gravity / covariance / ontology | `v16/review-jrh-gravity-delta.md` | `cd2822aa823581adf21677b3da9235438803f2700a6cace993d81806d22b2dc7` | `ACCEPT-WITH-FIXES` |
| quantum / EPR / QFT | `v16/review-jrh-quantum-delta.md` | `b99baa273cea7955d65e13b0e161c3d0ba908b8d46c4481b6da96aab8cdb02b4` | `ACCEPT-WITH-FIXES` |

The adjudicator also reran the target three times, exercised every black-box
mutant, checked unknown-CLI and non-writing behavior, independently verified
the total seal, and reproduced the paper, transcript, and receipt byte for byte
from an off-tree copy containing the source and its thirteen frozen inputs but
no `.git` directory.

## 2. Joint ruling

The repaired exact primary verdict is confirmed:

```text
BOUNDARY-INSTRUMENT-CONSISTENT-BUT-FUNDAMENTAL-DYNAMICS-UNSELECTED
```

This verdict has two deliberately unequal halves.

- The finite Z instrument is a proved fixed-factor CP boundary instrument.
  Its preparation blindness, registered no-signalling result, feed-forward
  eliminability, entanglement breaking, interference-placement constraint,
  arity/cycle separation, proper finite holonomy, logarithm ambiguity, and
  weak-surface Z/X nonselection independently reproduce.
- The complex relational-history law is still a candidate.  On common fixed
  boundary spaces its displayed decoherence functional is mathematically
  coherent, but its changing-carrier typing, local weights, record selector,
  gluing, all-input normalization, refinement fixed point, geometry response,
  and continuum phase are unselected.

No reviewer found a false promoted exact result after repair.  The original
dynamic-geometry claim remains rejected.  The candidate may proceed to one
bounded paper repair; it is not terminal before that repair and its post-commit
verification.

## 3. Exact findings confirmed by all three seats

1. The nominal outputs satisfy `G'=g xor z` and `C'=z` on the full delivered
   bit domain.  Retaining `g` and the ordinary record reconstructs every
   declared readout; the input collar is unused and no relation carrier moves.
2. Z and X ensembles both average to `I/2`.  Any fixed linear instrument gives
   the same complete output for every decomposition of one density operator.
   The registered decomposition-reading control is non-affine and changes
   under the steerable decompositions.
3. Z dephasing on one half of the Bell state gives the separable normalized
   Choi state `(1/2)|00><00|+(1/2)|11><11|`, of purity `1/2`; the displayed
   unconditioned channel is entanglement breaking.
4. The rational paths have amplitudes `9/25` and `-16/25`.  Coherent summation
   gives `49/625`; inserting an intermediate record gives `337/625`.  The
   displayed projective map therefore cannot be a universal microscopic
   rewrite while retaining this interference.
5. Cycle ranks are `0,0,1` for the edge, open three-vertex path, and triangle.
   The repaired three-edge transport closes, reverses by adjoint, transforms
   by base-point conjugation, and has invariant trace `0` and determinant `1`.
   This is transport-loop kinematics, not gravitational curvature.
6. The full integer phase-lift family `(4m,1+4n)` maps to the same frozen
   transfer.  The five receipt rows are witnesses only.
7. Z and X instruments predict `(1,0)` and `(1/2,1/2)` on the registered input
   while passing the same weak uncalibrated boundary surface.  This proves
   nonselection by that surface, not equivalence of calibrated physical laws.

## 4. New exact blocker: state-relative decoherence is not an instrument theorem

All three seats independently found the same defect.  It is adopted.

For a fixed positive boundary state, the class-operator form

`D(A,B)=Tr(K_A rho K_B^dagger)`

is Hermitian, additive, and strongly positive whenever the operators have a
common domain and codomain.  Strong positivity is a Gram-matrix fact and does
not select the weights.  If one partition decoheres and its diagonal values
sum to one for that particular `rho`, those values are lawful probabilities
for that prepared state.  They do not yet define a reusable quantum
instrument.

The quantum seat's exact counterexample is decisive:

```text
rho = |0><0|,
K0  = diag(3/5,2),
K1  = (4/5)|1><0|.
```

The partition is exactly decoherent for `rho` and has diagonal probabilities
`9/25` and `16/25`, summing to one.  Yet

`K0^dagger K0 + K1^dagger K1 = diag(1,4)`.

The second input basis state is amplified to trace four.  Therefore the paper
must separate:

- state-relative decoherent probabilities; from
- an operational boundary instrument, which additionally requires every
  branch to be trace nonincreasing and the complete CP family to satisfy
  operator/all-input normalization, such as
  `sum_alpha K_alpha^dagger K_alpha=I` in the single-Kraus fixed-space case.

Changing boundary algebras require the correctly typed ancilla-stable analogue.
Objective actualization is an additional postulate even after either
probability condition is met.

## 5. The geometry-sector overlap rule

The gravity and operator seats independently exposed the sharpest new typing
question.  Putting different output geometries in orthogonal direct-sum sectors
makes their cross terms vanish by definition.  Allowing arbitrary nonorthogonal
pairings can manufacture the desired interference.  Neither choice may be
made after inspecting the amplitudes.

The bounded repair adopts the following principled candidate rule.

1. A physical boundary type `B` is defined by its durable interface record and
   continuation algebra, with a declared state space or observable algebra.
2. Fine matter–geometry histories may interfere only when independently frozen
   refinement maps place them at the same unread coarse boundary type.
3. Alternatives that leave distinguishable durable boundary records occupy
   orthogonal output sectors.  Their direct sum is appropriate precisely
   because a division has occurred.
4. Histories with different unrecorded internal geometries but the same coarse
   boundary are summed before probabilities are taken.
5. All boundary embeddings, pairings, gauge quotients, and refinement maps are
   part of the candidate law and must be declared before weights or held-out
   predictions are examined.

This rule types the proposal without selecting the required maps.  The first
successor experiment must still test cylindrical/refinement consistency and a
nontrivial cross-geometry interference witness.

## 6. Merely joint is not back-reacting

The gravity seat's factorization objection is also adopted.  A history may
contain both matter data `h_m` and geometry data `h_g` while its weight still
factorizes as `a_m[h_m]a_g[h_g]`.  Co-presence is not coupling.

A future backreaction claim therefore requires both:

- a nonfactorization discriminator for the complete local class operator,
  invariant under allowed representation changes; and
- a calibrated response test in which changing an independently defined
  matter load changes a relational/transport observable, which in turn changes
  a held-out later matter availability or amplitude, subject to branchwise
  balance.

Until that test passes, the history formula includes geometry as a variable but
does not demonstrate gravitational backreaction.

## 7. Remaining ontological and representational corrections

The panel adopts the following smaller but binding distinctions.

- **Actualization.**  Decoherence supplies compatible probabilities, not the
  fact that one outcome happens.  A preferred stable record algebra, compatible
  nested partitions, refinement/future-extension consistency, and a statement
  of what is actual between divisions remain required.  The paper may postulate
  objective stochastic actualization but must not say it emerges.
- **Hamiltonian.**  A strongly continuous unitary group has a Hamiltonian
  generator.  A generic CPTP semigroup has a Lindblad/GKSL generator, and a
  non-Markovian process may have neither time-homogeneous form.  A selected
  unitary dilation can carry a larger-space Hamiltonian but adds environment,
  clock, and embedding choices.
- **EPR/ontic branch.**  Inaccessibility of decomposition data is only a safety
  condition.  Any surviving ontic-pure-state theory must also reproduce
  conditional steering and Bell correlations while proving parameter
  independence for its complete composite law.
- **Arity.**  The L2 projective occurrence refutes a minimum-three claim only
  at its typed boundary-instrument scope.  A future selected fundamental law
  could still impose a minimum support.  All-`n` extension remains open.
- **Gravity noise.**  Orthogonal durable geometry records imply loss of their
  interference.  Stochastic metric noise additionally requires nontrivial
  branching, a selected actualization rate, a metric readout, and a scale; it
  is not automatic in deterministic or zero-response sectors.

## 8. Consequence ruling

The existing conservative consequence ledger survives, with three rows to be
made explicit: all-`n` extension `OPEN`, objective actualization `OPEN`, and
Lorentz violation `OPEN`.  “Open” means neither predicted nor excluded.

No particle/species inventory, affine-coset value, channel translation,
cosmological value, absolute scale, matter–gravity coupling, GR/QFT limit, or
observable deviation is derived.  The Hamiltonian is proved nonunique from one
transfer but is not proved absent as an effective representation.  Two-actor
gravitational backreaction remains open.  The existing ISP walk is not
reconstructed.

## 9. Binding bounded repair

Before terminalization of paper 01 at its negative/candidate scope:

1. replace automatic instrument/actualization “emergence” with the
   state-relative versus all-input/operator distinction;
2. add common-boundary/direct-sum typing and the geometry-sector overlap rule;
3. require nonfactorization plus calibrated response before naming
   backreaction;
4. add compatible stable record partitions and actualization consistency;
5. split unitary Hamiltonian, Lindbladian, dilation, and non-Markovian cases;
6. narrow the arity and gravitational-noise wording;
7. add all-`n`, objective-actualization, and Lorentz rows to the exact
   consequence object;
8. add dedicated measurement-moving mutants for entanglement breaking,
   interference placement, and the complete nominal diamond;
9. remove the duplicate arity assignment and record the independent off-tree
   no-git reproduction; and
10. bind load-bearing generated numerals to explicit receipt sources rather
    than merely categorizing every numeral by line.

The actual overlapping `R -> R'` matter–geometry successor is not smuggled into
this bounded prose/instrument repair.  It remains the separately pinned next
scientific obstruction.

## 10. Status and halt

```text
EXACT FIXED-BOUNDARY INSTRUMENT AND NEGATIVE RESULTS: CONFIRMED
ORIGINAL DYNAMIC-GEOMETRY TOY: REJECTED
FIXED-BOUNDARY DECOHERENCE-FUNCTIONAL FORM: COHERENT BUT NONSELECTING
CHANGING-CARRIER HISTORY LAW: CANDIDATE, UNTYPED/UNSELECTED
HISTORY-TO-INSTRUMENT BRIDGE: REQUIRES OPERATOR COMPLETENESS
OBJECTIVE ACTUALIZATION: POSTULATED, UNSELECTED
QFT/GR/PARTICLES/CONSTANTS/DEVIATIONS: OPEN
```

One bounded repair and one post-commit verifier are authorized for paper 01.
No overlapping-successor, continuum, particle, or phenomenology unit is
authorized by this adjudication.  After the repaired paper reaches its scoped
terminal or refused status, halt and return to the user.
