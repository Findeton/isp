# Paper 18 version-3 mathematical adjudication

Date: 2026-08-21

Disposition: **REVISE / SUPERSEDED ONLY BY A NEW VERSIONED AMENDMENT**

No version-3 candidate byte is repaired in place. No implementation or
downstream Paper 17 evaluation is authorized by this adjudication.

## 1. Authenticated candidate

The reviewed version-3 mathematical object was the binding composite of:

| role | ordinary SHA-256 |
|---|---|
| complete version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` |
| binding version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` |
| version-3 construction note | `71d3bef893d772aff8c102915a570ffee76d4bbab15e48a47219bbef3de7876b` |
| version-3 hostile-review protocol | `cece6b5e44c1d3f5bdebe650d1723a03f828e5a107610bbacf9a24416852f910` |

The amendment correctly repaired version 2's target-only definition of
branching. It separated resolved physical channels from their target-sector
pushforward and admitted inequivalent positive-measure channels with a
common target.

## 2. Independent reviews

| seat | verdict | report SHA-256 |
|---|---|---|
| category and measure | `REVISE` | `3d74b3722db56a7ea4f60ea6b3393f2e997c9ef2e52660f1f51e4826d723f289` |
| probability and identifiability | `REVISE` | `0eea76ef1094f10eb8c18cf94c1fc8be30358ef47d29c6cc7be951e619316344` |
| physics and ontology | `ACCEPT` | `688c7a6cb7bbad92744f129c3f126ccf58c3f085b08c0b00d88e79e79c3178ea` |

All three reports were mutually blind and frozen before adjudication.

## 3. Decisive common defect

Version 3 declared a finite invariant measure \(\mu_{a,b}\) separately on
each resolved-channel fiber. It did not declare:

1. one measurable total resolved-channel bundle over
   \(\mathsf S\times\mathsf S\);
2. one jointly measurable target map on that total bundle; or
3. an input-measurable finite kernel \((a,b)\mapsto\mu_{a,b}\).

Fiberwise measurability does not imply measurable dependence on the input
pair. A non-Borel choice between two inequivalent same-target channels can
therefore satisfy every pointwise version-3 condition and have a perfectly
measurable associative target pushforward while failing to define a
resolved conditional Markov kernel.

The normalization and target-pushforward identities are correct for each
fixed input pair. The failed claim is the general measurable-kernel theorem.
This is a mathematical typing defect, not a physical counterexample and not
an implementation issue.

## 4. Surviving result

The following version-3 conclusions survive unchanged:

- resolved channel identity need not equal target-sector identity;
- two inequivalent channels may have the same target;
- structural plurality does not supply occurrence odds;
- target-sector probabilities do not determine resolved-channel
  probabilities;
- Paper 13D's fixed simultaneous-fusion family has one resolved generator
  class, with fresh bonds in its indexed history fiber;
- Paper 13D supplies no autonomous measure over primitive, staged, fused,
  and disconnected whole-complex alternatives; and
- no selector, actualization, chronology, dimension, signature, metric,
  curvature, or gravity result follows.

## 5. Required forward repair

A successor may retain the entire version-3 physical distinction, but it
must replace the pointwise family by a measurable dependent sum

\[
 \mathcal C=\coprod_{(a,b)}|\mathsf{Ch}(a,b)|
\]

with a declared total sigma algebra, measurable projection and target map,
and a finite nonzero kernel on its fibers. For every total measurable
resolved event \(E\), the function

\[
 (a,b)\longmapsto\mu_{a,b}(E_{a,b})
\]

must be measurable. Positive-measure branching must use such total
measurable events. This condition must reject the reviewers' non-Borel
same-target split while preserving discrete, continuous, hybrid, and
non-standard measurable branches.

## 6. Adjudicated vector

The conservative product vector remains:

    P18-SECTOR-REFERENT-CONTRACT-CONSTRUCTED
    P18-BOUNDED-SECTOR-CENSUS-UNCONSTRUCTED
    P18-GLOBAL-SECTOR-COMPLETION-UNCONSTRUCTED
    P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED
    P18-NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED
    P18-PHYSICAL-CHANNEL-MEASURE-UNCONSTRUCTED
    P18-COMPOSITION-CLOSURE-UNPROVEN
    P18-POSITIVE-CHARACTER-UNTESTED-NO-PHYSICAL-CHANNEL-MEASURE
    P18-RESOLVED-CHANNEL-LAW-UNCONSTRUCTED
    P18-TARGET-SECTOR-LAW-UNCONSTRUCTED
    P18-WHOLE-SELECTOR-UNCONSTRUCTED
    P18-ACTUALIZATION-UNCONSTRUCTED
    P18-CHRONOLOGY-NOT-EVALUATED
    P18-DIMENSION-NOT-EVALUATED
    P18-SIGNATURE-NOT-EVALUATED
    P18-METRIC-NOT-EVALUATED
    P18-CURVATURE-NOT-EVALUATED
    P18-GRAVITY-NOT-EVALUATED
