# D10 hostile review, round 3: final narrow ontology/locality/gauge closure

**Referee:** independent hostile ontology/locality/gauge audit  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE REPAIRED FINITE CONDITIONAL `KINEMATICS-ONLY` SCOPE**

## Closure artifacts

- `v10/data/d10-round2-textual-closure-receipt.md`
- `v10/note-d10-bloch-celestial-investigation.md`
- `v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md`
- `v10/code/d10_relational_scir_packet.py`
- `v10/reviews/d10-round2-ontology-locality-hostile-review.md`

Hashes independently reproduced:

```text
a93d1f461087e908c9adc242900e5d5ed500a05a18a86c09b37f0c65cb8d316d  d10-round2-textual-closure-receipt.md
9e8bb52ebc7d4732eb4d88b82e2cbca958ce649b1b006b4442e7c7218560afe6  note-d10-bloch-celestial-investigation.md
b8af6242554f321ad6c6a6b8d4596377b94dc3401acb300ab15c972ca871c6c6  relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
435cea33e9d6f57dca114567828544bc04c0add597d8a87534f6301bda481b5f  d10_relational_scir_packet.py
```

## Narrow closure table

| Round-2 blocker/correction | Status | Evidence |
|---|---|---|
| `SL(2,C)` versus `PSL(2,C)` covering language | **CLOSED** | Paper now states that `SL(2,C)` maps two-to-one onto `SO^+(1,3)` with kernel `{+I,-I}`, while `PSL(2,C)` is isomorphic to `SO^+(1,3)`. |
| Finite Hilbert dimension promoted to finite record capacity | **CLOSED** | Investigation now claims only finitely many algebra coordinates versus infinitely many independent classical clock registers; exact description, provenance, evidence/KL, and per-record capacity remain open. |
| External sphere absent without generator/diagnostic qualifier | **CLOSED** | Executable docstring now says no external generation oracle and explicitly identifies the Fibonacci sphere as a coverage diagnostic. |

## 1. Group-theory closure

The corrected sentence is exact:

```text
SL(2,C) -> SO^+(1,3)
```

is a two-to-one covering homomorphism with kernel `{+I,-I}`, and

```text
PSL(2,C)=SL(2,C)/{+I,-I} ~= SO^+(1,3).
```

The repair introduces no new gauge promotion. The same section continues to
state that a generic `SL(2,C)` congruence is nonunitary on normalized qubit
states, changes trace/branch weight, and cannot be treated as harmless gauge
until a dual event/effect and Born-weight law is supplied.

`FULL-SL2C-BORN-GAUGE-OPEN` therefore remains the correct verdict component.

## 2. Finite-information closure

The rejected sentence has been removed. The investigation now says:

- finitely many qubit algebra coordinates can answer many correlated
  projective questions;
- this avoids storing infinitely many **independent classical clock
  registers**;
- it does not bound exact state-description length;
- it does not bound accumulated provenance;
- it does not bound evidence/KL content;
- and the remaining per-record capacity notions stay open.

This agrees with the paper, executable receipt, and repaired verdict:

```text
FINITE-ALPHABET/FINITE-DEPTH-PROJECTOR-REFINEMENT
PER-RECORD-EVIDENCE-CAPACITY=NOT_ESTABLISHED
```

No inference from finite Hilbert dimension to a fixed exact record alphabet
or evidential capacity remains.

## 3. Generator/diagnostic sampler closure

The executable docstring now matches its implementation:

```text
no external S2 generation oracle;
external Fibonacci sphere used only for coverage diagnosis.
```

The output remains equally explicit:

```text
generation_external_sphere_sampler=ABSENT
coverage_diagnostic_external_fibonacci_sampler=50000
```

Independent execution reproduces **43/43** checks, 113 depth-12 projectors,
sampled support `0.914143429015`, and receipt hash

```text
95aac16b99d4948e6f96494452ea29fb212d92f3cb3167c8c3f077aa2b6ae215
```

The docstring-only correction changes no executable result. The external
round sphere remains a benchmark for angular coverage, not an input to the
`H/T` rewrite generator and not evidence that SCIR selected physical space.

## Scope regression check

No corrected sentence introduces a new ontology or locality claim. The live
package still states that:

- the complex qubit/Lorentz result is a conditional ordered-space
  isomorphism;
- directional projectors are positive functionals/clock shadows, not derived
  operational clocks;
- the Bloch-to-displacement and time/scale maps are declared;
- complex structure and local tomography are imported;
- the `SU(2)` connection is supplied, with link birth, ownership,
  calibration, and physical holonomy sealing open;
- the chosen SEAL/schedule/forest controls are finite packet tests only;
- joining-sector and spacetime influence are open;
- positivity, declared coordinate cone, ancestry, and interventional
  influence remain nonidentified;
- profinite history, projective state space, and metric refinement remain
  distinct;
- and no Einstein dynamics, absolute units, `G`, or physical `3+1` selection
  follows.

## Accepted final ledger

```text
CONDITIONAL-COMPLEX-QUBIT/LORENTZ-CONE-ISOMORPHISM
+ FOUR-FACTOR-DIRECTIONAL-POSITIVE-EVALUATIONS
+ FINITE-OUTER-CONE-APPROXIMATIONS
+ FINITE-ALPHABET/FINITE-DEPTH-PROJECTOR-REFINEMENT
+ CHOSEN-PACKET-SEAL/SCHEDULE/FOREST-INTERVENTION-TESTS
+ SUPPLIED-SU2-CONNECTION-GAUGE-COVARIANCE
- COMPLEX/LOCAL-TOMOGRAPHY-SELECTION-NOT-DERIVED
- NORMALIZED-QUBIT-TIME/SCALE-MAP-NOT-DERIVED
- PHYSICAL-LINK/SEAL/CAPACITY-NOT-DERIVED
- FULL-SL2C-BORN-GAUGE-OPEN
- JOINING/ORDER/SPACETIME-INFLUENCE-LINK-OPEN
= KINEMATICS-ONLY
```

## Verdict

**PASS AT THE REPAIRED FINITE CONDITIONAL `KINEMATICS-ONLY` SCOPE.** Both
round-2 blockers are closed, the sampler documentation is accurate, and no
new blocker was caused by the corrections.

This pass accepts the conditional qubit/Lorentz algebraic bridge and the
finite chosen-packet tests. It does not accept a derivation of physical space,
time, complex structure, link dynamics, record capacity, boost gauge, or an
order/influence spacetime law.

