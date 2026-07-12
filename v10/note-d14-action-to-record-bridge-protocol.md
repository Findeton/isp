# D14 protocol — construct the action-to-record bridge exactly

**Status:** frozen before D14 theorem, executable outcomes, and new geometry
tests, 2026-07-11.

## 1. Question

D13 proved that current record principles do not select one interaction
kernel.  It left the most natural upstream architecture—regional amplitudes
sewn across diamond boundaries—as a proposal.  D14 asks:

> Can a nontrivial class of finite sealed diamonds be defined as a clock-free
> boundary-amplitude category whose local kernels generate coherent histories,
> protected durable records, a compatible whole-history measure, and visible
> non-Markov dynamics, without inserting a universe-wide commit order?

D14 does **not** claim to select the physical field content or coefficients.
It must either prove this bridge on a sharply defined class or exhibit the
obstruction.

## 2. Frozen finite class

The source class is the finite typed causal circuit class `FSDiam`:

```text
objects    finite ordered tuples of typed finite-dimensional boundary ports;
generators finite local diamond maps with declared input/output tuples;
morphisms  finite acyclic typed circuit expressions modulo the strict
           symmetric-monoidal presentation relations;
tensor     disjoint union/tuple concatenation;
compose    typed boundary gluing;
identity   eventless typed wire;
symmetry   explicit typed wire permutation.
```

Protected sealed-record ports are read-only outputs: later licensed generators
may copy/read them but may not target or erase them.  Live output-collar ports
remain ordinary typed outputs and may feed later diamonds.

This is a nontrivial exact subclass of possible SHARD diamonds.  D14 may not
rename it the category of all physical diamonds.

## 3. Candidate amplitude assignment

Each type `t` has a finite Hilbert carrier `H_t`.  Each generator `g:A->B`
has one supplied linear amplitude `K_g:H_A->H_B`.  Evaluation sends:

```math
Z(id_A)=I_A,
\qquad Z(g\circ f)=Z(g)Z(f),
\qquad Z(f\otimes g)=Z(f)\otimes Z(g),
```

and sends symmetries to permutation matrices.  The resulting `Z` is the
candidate strict symmetric-monoidal amplitude functor.

For fixed basis labels, internal boundaries are summed exactly:

```math
Z_N(b_{out},a_{in})
=\sum_{internal\ labels}\prod_{v\in N}K_v(b_v,a_v).
```

This is the finite action/path-amplitude form.  An `exp(iS)` representation is
licensed only when the local kernels, support, measure and branch choices are
separately supplied.

## 4. Frozen gates

### B0 — typed category

Objects, identities, composition, tensor, symmetry and protected-record rules
are explicit.  Ill-typed gluing and attempts to overwrite sealed records must
be rejected.

### B1 — category/coherence laws

Associativity, units, tensor associativity, interchange and symmetry
naturality must hold exactly.  At least one nontrivial three-diamond and one
disjoint two-diamond diagram are required.

### B2 — construction-order gauge

All topological contraction schedules of the same finite acyclic diagram give
the same amplitude.  The proof must identify adjacent swaps of incomparable
contractions and may not assume a global physical clock.

### B3 — coherent gluing

Internal unsealed alternatives are summed at amplitude level.  A control that
inserts a record or row-normalizes alternatives must change an interference
observable, demonstrating that classical local normalization is not the law.

### B4 — local frame/gauge covariance

Independent unitary boundary frames must cancel on internal edges and preserve
closed probabilities.  A separate rank-two positive-cone cell must test the
dual `SL(2,C)` state/effect pairing; this does not by itself prove emergent
Lorentz covariance of the network.

### B5 — records and birth

At least one generator must emit:

```text
system output + orthogonal sealed record + live typed output collar.
```

The map is isometric, the record is repeat-readable, later licensed dynamics
cannot alter its distribution, and an overwrite control is rejected.

### B6 — whole-history decoherence functional

For class operators `C_alpha`, compute

```math
D(alpha,beta)=Tr(C_alpha rho C_beta^dagger).
```

The recorded partition is positive, normalized and exactly decoherent in the
finite witness.  Born weights appear once.

### B7 — projective history law

Extending the circuit by a complete future instrument and summing its outcomes
preserves every past cylinder probability.  At least depths 1–3 and a general
finite induction argument are required.

### B8 — visible non-Markov memory

An executed reversible memory circuit must give the same current visible
record with different past-conditioned next probabilities.  The enlarged
carrier may remain Markov/unitary; the visible history must not.

### B9 — locality/no-signalling

Disjoint local operations satisfy interchange and at least one entangled
no-signalling marginal test.  D14 must not infer continuum microcausality from
this finite cell.

### B10 — action scope

The bridge must list every primitive input: types, grammar, kernels, boundary
state, record instrument, protected algebra, frames and unit bridge.  It may
not claim that functoriality selects their values.

### B11 — downstream handoff

State exactly what extra map is required before a causal-set, EFT or
asymptotic-safety action can generate V9 record webs.  No cone/dimension
holdout is allowed merely because the bridge works.

### B12 — hostile closure

Independent mathematics, ontology/locality and clean-room reviews must attack
the source category, functor, record protection, projectivity, memory and
claim scope.  Openings are repaired before the next round.

## 5. Countercontrols

D14 must include or prove the following failures:

1. ill-typed boundary gluing;
2. sealed-record overwrite;
3. insertion of an intermediate record changes interference;
4. local row normalization changes the composite amplitude;
5. omitting a live collar prevents continuation;
6. tracing hidden memory can make visible histories non-Markov, while deleting
   it changes the process;
7. a global schedule label is observationally absent from the evaluated map.

## 6. Verdicts

```text
FINITE-ACTION-TO-RECORD-BRIDGE-PROVED
  B0–B10 and B12 pass on the frozen FSDiam class; B11 is explicit;

BRIDGE-CONDITIONAL
  the algebra works only after an unproved structural premise or supplied
  quotient is added;

BRIDGE-REFUTED
  a frozen category, sewing, record, projectivity or locality gate fails;

INCOMPLETE-INVESTIGATION
  a promised gate, control, receipt or review is missing.
```

Even the positive verdict does not complete the thread goal.  It proves the
carrier from action amplitudes to records; action selection, physical fields,
couplings, scales and empirical spacetime holdouts remain separate gates.

## 7. Final adjudication

After two hostile rounds and focused closure, the executable core passes
42/42 exact checks.  The final formal verdict is

```text
BRIDGE-CONDITIONAL.
```

The narrower theorem is supplied regional amplitudes + state + record
instruments -> durable projective recorded histories on finite `FSDiam`
networks, with evaluation-schedule gauge.  Physical action-to-kernel,
autonomous record-instrument, diagram-generation and join-entitlement-origin
maps remain supplied or open.  No V9 geometry holdout is licensed.
