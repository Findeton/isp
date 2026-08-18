# Relational sufficiency and the finite eliminability game

**Date:** 2026-08-18

**Status:** frozen successor methodology. This note is not a WRC result and
does not retrofit a geometry claim into Paper 8.

## 1. The corrected question

On a finite horizon, unrestricted eliminability is vacuous: a lookup table or
an enlarged state can reproduce any finite input-output table. Conversely,
excluding one memoryless class proves only that memory matters.

The next investigation must therefore ask a layered question:

> Does a relational state provide a sufficient, compressed, compositional,
> and interventionally load-bearing statistic of the past for one uniform law
> across a held-out family, relative to a frozen adversary/resource class?

“Geometry is a sufficient statistic” is necessary but not sufficient for an
ontological conclusion. An invertible renaming of the same statistic as
“memory” predicts identically. Minimality, locality, composition, intervention,
and scaling must be tested separately.

## 2. Predictive sufficiency

Let `h` denote a complete past, `Z(h)=(R(h),G(h),S(h))` the proposed present
record/geometry/process state, `i` an allowed future intervention, and `F` a
future calibrated record-and-geometry observation. The screening condition is

```text
P(F | h, i) = P(F | Z(h), i)
```

for every registered past, intervention, future horizon, and observable.
Equivalently, histories with the same `Z` must have the same complete future
law. Failure means the proposed state is incomplete.

This is exactly the predictive-equivalence construction already frozen in
v15 JS Pin v2, S1a. The successor must absorb that instrument rather than
invent a looser substitute: refine the history partition on two axes (past
window and future horizon), predeclare stabilization, and report only
`NO-STABILIZATION-WITHIN-<range>` when it does not stabilize. JS S1b's
state-law fixed point remains the deeper candidate; compression alone does not
select truth.

## 3. Minimality and representation equivalence

If a graph-blind memory state `M(h)` is in bijection with `G(h)` on all reached
states and the bijection preserves successor probabilities, calibrated
observables, locality, composition, and interventions, then the two are
representations of one predictive state. Calling one “geometry” and the other
“memory” creates no empirical fork.

The relevant comparison is therefore the predictive quotient of histories,
not the variable name. A geometry claim gains force only if:

1. `(R,G,S)` screens off the deeper past;
2. no admissible strictly coarser local statistic does so;
3. the quotient and its update are natural under relabeling and composition;
4. the relational coordinates have calibrated intervention semantics; and
5. a claimed rival is not merely an isomorphic recoding of those coordinates.

Even all five establish a privileged law-native state description, not an
absolute metaphysical theorem. Ontology still requires the program's separate
beable/actualization commitments.

## 4. Frozen family-level game

Before seeing target screens, freeze

```text
Game = (Family, Train, Holdout, Interventions, Tau,
        BlindInterface, Resources, Gauge, Metric, Tolerance).
```

- `Family` contains genuinely nonisomorphic relational carriers and
  carrier-changing successors.
- `Train` and `Holdout` are disjoint graph-isomorphism classes and preparation
  sets.
- `Interventions` includes relabelings, record-only changes at fixed graph,
  graph-only changes at calibrated-equal nongeometric state, and at least one
  law-generated rewrite followed by a probe computed from the output graph.
- `Tau` is one rule and one parameter dictionary across every member; no
  per-graph recompilation or retuning.
- `BlindInterface` states exactly what labels, state, clock, memory, and graph
  features a rival receives. Raw names may not secretly encode adjacency.
- `Resources` fixes locality radius, state/memory dimension, ancillas, circuit
  depth, parameter count, description length, and numerical field/precision
  for both sides.
- `Gauge` fixes permitted relabelings/calibration transport.
- `Metric` and `Tolerance` compare the complete registered outcome instrument,
  not one planted screen.

The graph-fed rule must pass every training and held-out row. A class-relative
load-bearing result additionally requires every rival in the frozen class to
fail a held-out invariant row and positive controls to show the rival class is
nonempty and capable on easier cases.

## 5. Adversary ladder

The minimum nested ladder is:

| class | resources | meaning of exclusion |
|---|---|---|
| `B0` | fixed-carrier, memoryless process | the registered memoryless class cannot reproduce the feedback |
| `B1` | bounded equivariant memory, no graph input or graph-coded raw labels | explicit relational input adds predictive information beyond that bounded memory class |
| `B2` | budgeted graph-labelled/compiled circuits and lookups | one uniform relational rule generalizes or compresses the family better under the frozen budget |

DISC reaches only a registered `B0` exclusion. Unbounded `B2` always wins on a
finite family. A `B1` or budgeted-`B2` win is necessarily class-relative; the
resource bound must be reported as part of the result, not hidden as a
technicality.

## 6. Causal/load-bearing control

The decisive fixture is a matched intervention. Two cases have the same
allowed nongeometric input to the blind class but different relational state.
One uniform law must predict different later distributions through a probe
computed from the changed output graph. Erasing or changing only that graph
must erase or change the effect, and reconstructing the graph must restore it.

To test dynamic rather than background geometry, the same `Tau` must first
produce `G'` from the incoming state and then use `G'` in the later transport.
A duplicated flag, port label, or separately compiled circuit fails the
erasure/reconstruction control.

## 7. Scaling criterion

Held-out accuracy alone can still hide a large simulator. Record, for an
increasing graph family, the description length and state/memory growth of:

1. the uniform relational rule;
2. the best admitted graph-blind memory law; and
3. the best admitted compiled lookup/circuit.

Constant-size or law-governed relational growth against unavoidable rival
growth is evidence of compression and family generalization. It is not an
absolute proof of ontology, but it is stronger than per-fixture eliminability
and makes the declaration price explicit.

## 8. Frozen outcomes for a successor

At minimum:

```text
RELATIONAL-STATE-INSUFFICIENT-WITHIN-RANGE
RELATIONAL-STATE-SUFFICIENT-NOT-MINIMAL
RELATIONAL-STATE-ISOMORPHIC-TO-MEMORY-REPRESENTATION
RELATIONAL-STATE-CLASS-RELATIVE-LOAD-BEARING
RELATIONAL-STATE-ELIMINABLE-WITHIN-REGISTERED-CLASS
NO-STABILIZATION-WITHIN-RANGE
METHOD-INCONCLUSIVE
```

No outcome may be paraphrased as absolute non-eliminability.

## 9. Current debt disposition

- WRC remains a fixed-carrier reconstruction with non-inert state-record
  feedback and a CELL-HIT instrument obstruction. It does not run this game.
- DISC supplies `B0` evidence only.
- SCOUT-T remains procedurally unsealed in the tracked v15 ledger and is not
  cited as a result here; its untracked worktree files remain untouched.
- JS Pin v2 is frozen but unexecuted. Its S1a/S1b predictive-equivalence
  machinery is the governing ancestor for the successor and must be absorbed
  or explicitly dispositioned before a new geometry-irreducibility unit.
- A generative engine—not a JSON packet of named matrices—must construct the
  graph family, histories, uniform `Tau`, held-out split, probes, and adversary
  census from frozen grammar rules.

This resolves the conceptual criterion. It does not pre-answer the experiment.
