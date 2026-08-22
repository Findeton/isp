# Paper 18 version-2 mathematical review adjudication

Date: 2026-08-21

Status: **REVISE / ONE BOUNDED SEMANTIC DEFECT / NO IMPLEMENTATION**

## Authenticated reports

| seat | verdict | ordinary SHA-256 |
|---|---|---|
| category, measure, restriction | `ACCEPT-WITH-SCOPE` | `e5dae6f16844dd2981cedb12c522277781cb59c229f69cb6086bb1d4e397341f` |
| probability, projectivity, identifiability | `REVISE` | `e351250b9a59b64c7707cac9de41fc909f309c8602cfeec4de9c7c39206e85c5` |
| physics, ontology, firewalls | `ACCEPT` | `653df431aa647ca11006a15814fdc85d3efa35ce830a48c2a7e67e8e6884f9ee` |

The reviewed version-2 candidate remains fixed at
`b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614`.

## First and only decisive defect

Version 2 Definition 12 requires two inequivalent target sectors for
selector-level branching. That is too strong. There can be two inequivalent
resolved physical channels

\[
 \kappa_0,\kappa_1:a\boxtimes a\to a
\]

with one common target. Resolved counting gives

\[
 \mathsf M_{a,a}=2\delta_a,
 \qquad d(a)=2,
\]

so each resolved slot has probability one half even though the pushed-forward
target-sector law is deterministic.

This does not refute the accepted Paper 13D branching fork. Paper 13D has one
resolved simultaneous-fusion generator for a fixed component family; its
random cross-bond values are histories, not additional resolved channel
objects.

## Required version-3 correction

1. Define nontrivial structural branching on resolved channel objects or
   positive-measure invariant channel families, not only on target sectors.
2. Introduce an independently physical resolved channel measure
   \(\mu_{a,b}(d\kappa)\).
3. Define the target convolution as its pushforward
   \(\mathsf M_{a,b}=(\tau_{a,b})_*\mu_{a,b}\).
4. Define the resolved conditional law
   \[
    \mathsf P^{\rm res}_{a,b}(d\kappa)
    =\frac{d(\tau\kappa)}{d(a)d(b)}\mu_{a,b}(d\kappa),
   \]
   whose target pushforward is the earlier \(\mathsf P_{a,b}\).
5. Report resolved-channel and target-sector laws on separate product
   coordinates.

## Accepted notation scopes to make literal

The category seat accepted version 2 with three harmless readings that
version 3 should state explicitly:

- the groupoid-valued inverse limit is the pseudo-limit or descent groupoid;
- “history fibration” means an equivariant indexed family unless cartesian
  lifting is separately proved; and
- cardinality counts point-free isomorphism classes, while measurable labels
  are hierarchical descriptors rather than exclusive bins.

## Preserved product

All conservative version-2 physical coordinates survive. No sector census,
channel measure, channel law, whole selector, chronology, dimension,
signature, metric, curvature, gravity, or actualization is promoted.

Version 3 is a mathematical typing amendment only. It may not select a
measure, multiplicity, character, coupling, sector type, or downstream
output.
