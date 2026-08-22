# Paper 18 version-4 construction note

Date: 2026-08-21

Status: **MATHEMATICAL CANDIDATE FROZEN / RESULT UNKNOWN**

## 1. Immutable composite

| role | ordinary SHA-256 |
|---|---|
| complete version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` |
| binding version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` |
| binding version-4 amendment | `33f1e9a05bdc16b7aa96831fe1e8bc4c3bd4ca5095d2f79cbbe0c6d32abe8137` |
| version-3 adjudication | `f35e91d9dd5b68aefcd75a55612f64ba15e9f1d6a30f856eb12f43ff914ec45c` |

The precedence rules in the version-4 amendment define the sole version-4
object. No component may be edited during review.

## 2. Reason for the amendment

Version 3 correctly separated resolved channels from target sectors, but it
declared only a finite measure on each channel fiber. Two independent blind
reviews constructed the same counterexample: a non-Borel input-dependent
split between two same-target channels can obey every fiberwise condition
and have a measurable associative target pushforward while failing to be a
resolved Markov kernel.

Version 4 makes the missing object explicit:

\[
 \mathcal C=\coprod_{(a,b)}|\mathsf{Ch}(a,b)|
\]

with one total sigma algebra, measurable projection, jointly measurable
target map, and one finite input-measurable kernel on the varying fibers.
Measurability is tested on every total resolved event, not inferred from
pointwise measures.

## 3. Result-neutral scope

The amendment does not choose:

- the sector catalogue or global completion;
- a resolved channel or target measure;
- a provenance branch;
- a character, coupling, size law, or selector;
- a discrete, continuous, hybrid, or non-standard measurable branch;
- an actual history;
- chronology, dimension, signature, metric, curvature, or gravity; or
- an implementation language or algorithm.

It preserves the version-3 fact that same-target channels can branch at the
resolved level. It also preserves the distinction between structural
plurality and a physical probability law.

## 4. Exact controls frozen before review

Reviewers must verify all four controls independently.

1. A non-Borel same-target split on a product-Borel channel bundle is
   refused because the channel-index event has a nonmeasurable probability
   as a function of the input.
2. The finite two-channel based ring is accepted and gives resolved
   probabilities \(1/2,1/2\) with deterministic target probability.
3. A nonatomic \([0,1]\) same-target channel family is accepted through two
   positive-measure half-intervals even though every point has zero mass.
4. A non-standard measurable branch is neither accepted nor rejected by
   name: it must directly construct the total event kernel, because no
   regular disintegration is assumed.

## 5. Present result

The current result remains a contract plus a no-go/fork statement. Paper 13D
has one resolved simultaneous-fusion generator class for each fixed
component family; fresh bonds are history values. Its other whole-process
complexes have no accepted autonomous structural kernel. Consequently every
selector-law coordinate remains unconstructed.

No implementation or Paper 17 scientific evaluation is authorized before a
terminal mathematical adjudication accepts the complete version-4
composite.
