# D4 hostile review, round 1: ontology, locality, no-silent boundaries, Barandes, diamonds, and profinite scope

**Referee:** independent hostile ontology/locality audit  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**

## Frozen artifacts reviewed

- `v10/note-d4-no-silent-boundary-sufficiency.md`
- `v10/code/d4_boundary_sufficiency_exact.py`
- `v10/relativistic-isp-v10-paper5-restriction-naturality-global-shock.md`
- v10 Papers 1–4 and the D1–D3 hostile-review foundations

Hashes executed in this review:

```text
ff785c56b8c95dd9843e77b548951aedc9f8496f7938272de2ac73006ac8fdf9  note-d4-no-silent-boundary-sufficiency.md
7c87e81f333d75814ec508023c7a21a01b0a25142415819288da3aaac1137481  d4_boundary_sufficiency_exact.py
5dde07f57a6b8098d6f464ee686457981448e0d0dd26f3c31ccaac770b181c6b  relativistic-isp-v10-paper5-restriction-naturality-global-shock.md
```

The executable reproduces **17/17** exact checks using integers and
`Fraction` arithmetic. The finite classification, positivity certificate,
completion-message marginals, chain-capacity witness, and standard
profinite-integer discontinuity example are internally correct.

Major revision is nevertheless required. D4 has proved a sharp conditional
theorem about **unmarked autonomy under every induced-subset cut**. It has not
shown that this is the restriction principle physically licensed by SHARD,
nor that its canonical predictive quotient is a physically constructible
record. Those are the two load-bearing openings.

## Executive finding

D4 establishes three useful negative results, each with a strict boundary:

1. If every finite subset is required to evolve autonomously with the same
   unmarked down-set kernel after its environment is discarded, positivity
   collapses the law to an empty/full universal-precursor mixture.
2. For a supplied law and one chosen marginal-prediction task, the exact
   completion marginal is the coarsest deterministic predictive quotient;
   the number of its distinguishable values is unbounded on the chain family.
3. The particular readout `n -> n/(n+1)` has no continuous extension from
   natural depths to the standard profinite integers.

None of these statements yet yields a final interacting record click law.
The first begins from a physically unproved autonomy axiom, the second
packages the desired answer rather than deriving a carrier that computes it,
and the third depends on a particular compactification and a continuity
requirement.

## Major findings

### M1 — All-subset autonomy is a proposed physical axiom, not the default meaning of locality

D4's naturality square quantifies over **every** retained subset `K` and then
requires the pushed-forward kernel to equal the kernel of the bare induced
subposet `P|K`. This means that, after discarding the environment, no boundary
residue, ancestry flag, carrier state, collar, law parameter, or conditional
context may remain.

That is much stronger than causal locality. In fact it is the autonomy
principle that D1's no-silent analysis warns against using silently. The
structural proof makes the issue especially clear: its first decisive cut
restricts a two-chain to its **top point alone**, erasing that point's causal
ancestor and demanding that it behave exactly like a primitive isolated
point. Such a cut is an induced-subset cut, but it is not ancestor closed and
has not been shown to be an admissible physical screen, sealed-diamond
restriction, or complete local laboratory.

The theorem is valid as stated. What is not justified is promoting its
hypothesis to “the” SHARD locality principle. Restriction of mathematical
incidence and autonomous re-use of an unchanged physical kernel are distinct
requirements.

**Mandatory opening:** define and compare at least the following restriction
categories before drawing a physical no-go conclusion:

1. arbitrary induced subsets, as in D4;
2. ancestor-closed stems/down-sets;
3. causal intervals or convex retained regions;
4. screen/collar-complete cuts that retain the D1 boundary residue;
5. typed direct-carrier restrictions inherited from D1/D2.

For each category, rerun the exact finite classification and state whether
the empty/full collapse survives. If it survives only for arbitrary silent
cuts, then it is a theorem against silent all-subset autonomy, not against
local interaction.

### M2 — The survivor is global incidence, but “shock” still adds unproved physical content

The paper does **not** mislabel its survivor as local. It repeatedly says that
the empty/full mixture is all-universe and fails to provide a bounded
record-local interaction. That is correct and should be preserved.

The unmarked order proves only this transition:

- choose no precursor; or
- choose every old event as precursor, so the new maximal event is above the
  whole finite parent.

Calling the second branch a “global shock” suggests a physical disturbance,
joint interaction, or change propagated through all old records. None of that
is in the order. It is an **empty/full universal-precursor mixture** or a
**global-incidence branch**. It may later be interpreted as a shock only after
outcomes, transport, and a joint carrier make that interpretation testable.

This is the same ontology discipline imposed on D3's common-future shadow: a
universal future is incidence, not automatically an interaction.

**Required revision:** retain “global” and “nonlocal,” but use
`empty/full universal-precursor mixture` in theorem statements and receipts.
If `shock` remains as an intuition, label it explicitly as a metaphor.

### M3 — The completion vector is a canonical predictive quotient, not yet a physical boundary record

For fixed `P`, `K`, and supplied weights `w_P`, D4 defines

$$
q_{P,K}(A)
=
\frac{\sum_{D\cap K=A}w_P(D)}{\sum_D w_P(D)}.
$$

This is exactly the target visible precursor distribution. Consequently it is
predictively sufficient by construction, and equality of these vectors is
the coarsest equivalence relation for **that one prediction task**. The proof
and the exact audit are sound.

But this construction can encode the answer. It requires the whole parent
`P`, the retained set `K`, the global law `w_P`, and a sum over discarded
completions. No executable step shows that a finite sealed boundary can
produce the vector from its own incoming carriers. Calling `q` a boundary
message before supplying that production rule would turn “no silent
restriction” into an oracle for the missing marginal.

There are four additional scope limits:

- minimality is relative to one supplied law;
- it is relative to one selected marginal-prediction task;
- the normalized vector need not retain the total weight needed by a later
  rate, evidence, or normalization update;
- minimality as an abstract statistic does not imply minimal physical memory,
  composability, locality, or reusability across successive cuts.

D4 already admits most of this. The abstract and conclusion must make it
load-bearing, not parenthetical.

**Mandatory opening:** before treating a completion statistic as a record,
require all of the following:

1. a typed carrier and provenance rule saying where each component is stored;
2. a pre-sampling update rule computable from admissible child/boundary data;
3. a gluing/composition law for nested or adjacent cuts;
4. sufficiency for a declared family of future queries, not only the marginal
   used to define the quotient;
5. a test that two globally different parents with the same physically
   available boundary state cannot demand different updates.

Until then `q` is the canonical law-relative decoder target, not the missing
dynamic click law.

### M4 — Finite evidence does not imply a fixed deterministic alphabet

The chain argument is exact. Under the uniform down-set law, retaining the
minimum of an `n`-chain produces inclusion probability `n/(n+1)`. Hence the
first `N` depths require `N` distinguishable deterministic exact message
states when the retained unmarked structure and decoder are fixed. The
receipt correctly obtains 64 states, at least 6 bits, and failure of a
three-bit alphabet at depth nine.

This does not follow from the single-record evidence ceiling alone. A finite
evidence or likelihood budget does not by itself imply:

- finite support;
- a finite deterministic alphabet;
- a uniform worst-case number of distinguishable states;
- or a bound on the number of boundary records available jointly.

A real- or rational-valued record can carry an unbounded exact label while
each realized label is finite; an expanding collar can distribute an
unbounded message across individually bounded records; and finite Shannon or
KL information is not the same resource as exact zero-error state capacity.

The paper correctly labels fixed bounded deterministic capacity as an extra
assumption. That qualification must be attached to every physical summary of
the chain no-go.

**Mandatory opening:** state an operational capacity axiom with answers to:

1. Is the budget per primitive record, per screen, or per complete boundary?
2. Is capacity worst-case zero-error, expected code length, Shannon entropy,
   or evidence/KL weight?
3. May the number of carrier records grow with the parent?
4. Are approximate predictions allowed, and in which metric?
5. Must one decoder work across all parents and laws?

Only after that axiom is derived or adopted can the chain theorem constrain
physical record capacity.

### M5 — Stochastic, distributed, and unbounded marks remain genuine loopholes, not footnotes

D4 responsibly lists these escape routes. They need formal treatment because
they divide two very different conclusions.

#### Stochastic marks

A finite random mark can reproduce arbitrarily many visible probabilities if
its context-dependent mixing weights are allowed to depend on the discarded
environment. This evades deterministic state counting, but it has not made
the law local: the missing information has moved into the mark-generation
channel. If the realized mark is observed, predictions conditional on that
mark may also differ from the desired unconditioned `q`.

Therefore a stochastic mark is neither an automatic solution nor excluded by
the current theorem. It needs an explicit operational diagram specifying what
is sampled, what the local observer conditions on, where the mixing weights
are computed, and which equality is required.

#### Distributed or expanding boundaries

If each record has fixed capacity but a boundary may contain more records as
the history grows, the total exact capacity can grow like `log n` or faster.
The single-alphabet lower bound does not exclude this. A SHARD-compatible
construction might naturally place the missing context in a collar rather
than one center token.

#### Unbounded integer, rational, or structured marks

An unbounded mark is finite on every finite history while lacking a uniform
alphabet bound over all histories. That is fully compatible with the chain
receipt unless an independent uniform-capacity principle is supplied.

**Mandatory opening:** formalize all three models and prove one of two honest
outcomes for each: either it admits a local compositional realization, or the
global dependence reappears in a precisely identified encoder, carrier, or
normalization law.

### M6 — The profinite obstruction is correct for the standard profinite integers and should not be generalized

The analytic example is sound. In the usual profinite topology,
`j! -> 0` because every fixed modulus eventually divides `j!`, whereas

$$
\frac{j!}{j!+1}\longrightarrow 1
$$

in the real topology, conflicting with the depth-zero value `0`. Thus the
chain readout has no continuous extension to the standard profinite integer
completion with its ordinary embedding of finite depths.

The executable's finite residue checks are an illustration of that proof, not
the proof of convergence for all moduli; the paper's analytic argument closes
the gap.

The result does **not** establish that:

- all profinite or Stone boundary spaces fail;
- an exact measurable but discontinuous readout is impossible;
- all compact record topologies fail;
- or the v9 stem spectrum has the topology of `\widehat{\mathbb Z}`.

Indeed D4 explicitly notes a one-point compactification adapted to the limit
of `n/(n+1)`. Continuity itself is an additional physical regularity
principle, not a consequence of exact prediction.

**Required revision:** always say `standard profinite-integer completion` and
`continuous real readout`. Keep the counterexample to all-compact
overgeneralization in the main conclusion. Any application to the v9 Stone
spectrum must identify a concrete embedding and topology and then test the
readout there.

### M7 — No-silent restriction demands retained residue or refusal; it does not manufacture D4's statistic

D1 established a fork: either retain sufficient typed boundary residue, or
refuse the restriction as physically inadmissible. It did not prove that the
residue is a unique finite center, nor that it must equal a probability
vector.

D4 supplies one canonical statistic after a law and target query are already
given. This is a valuable diagnostic of how much a silent restriction lost.
It is not a derivation from sealed holonomy, and it does not resolve D1's
nonuniqueness of centers or eligible-support naturality failure.

The possibility of **refusal** is especially important for M1. Some arbitrary
subsets may simply fail to define a complete local experiment. Forcing them
to receive an autonomous kernel and then interpreting the collapse as a
locality theorem bypasses the no-silent fork.

**Mandatory opening:** type each allowed restriction as either:

- autonomous with a proved sufficient retained state;
- conditional on an explicit boundary/collar state; or
- inadmissible/refused.

Then formulate naturality separately in those three sectors.

## Barandes audit

D4 handles Barandes with appropriate restraint.

- A primitive full-history measure can make a completion conditional
  well-defined by disintegration.
- This supports law-relative memory inherited from discarded degrees of
  freedom.
- It does not select the primitive measure.
- Indivisibility does not imply all-subset autonomy, a fixed bounded
  statistic, or a Markov next-click law.

One phrase should remain interpretive: conditioning on discarded history
produces a mathematical conditional, not automatically a physically located
boundary memory. The carrier and production requirements in M3 are still
needed.

## Diamond and support-skeleton audit

D4 correctly refuses to identify the completion vector with a sealed-diamond
center. This is essential.

D2 composes supplied finite typed support incidence. It does not compose the
probability vector, prove its provenance, transport it through a collar, or
show that adjacent marginalizations agree as one holonomy law. D4 therefore
cannot outsource the missing construction to “diamond composition.”

The next diamond-level test should start only after a typed stochastic carrier
has been proposed. It must then check source/screen/collar provenance,
composition under gluing, and whether the statistic survives admissible
restriction without silent recomputation from the global parent.

## Geometry and quantum-promotion audit

**PASS.** D4 does not derive metric distance, elapsed time, cone roundness,
dimension, gravity, amplitudes, Born weights, or a Hilbert-space model. It
keeps geometry downstream and treats the probability kernel as a classical
candidate record-birth law. No quantum or geometric promotion was found.

This separation must remain explicit. A boundary probability vector is not a
quantum state merely because it is normalized, and a universal-precursor
event is not a spacetime cone.

## Exact executable audit

The independent execution returned:

```text
PASS 01-17
RECEIPT: 17/17 exact checks passed
VERDICT: UNMARKED-GLOBAL-COLLAPSE + LAW-RELATIVE-UNBOUNDED-DETERMINISTIC-MESSAGE
BOUNDARY: no bounded record-local interacting extension law is selected
```

The exact claims checked include:

- 111 variables, 1,087 linear equations, rank 108, and signed affine
  dimension 3 through labeled strict-poset size 3;
- positivity killing 1,304 audited proper ideals through size 4;
- exact empty/full naturality through 3,671 cuts;
- 7,342 completion-message contexts and 756 predictive classes;
- up to 66 messages for one retained unmarked structure;
- the law-relative `1/2` versus `9/14` witness;
- 64 distinct chain-depth predictions and the exact 6-bit lower bound;
- failure of a one-bit external-parent flag (`2/3` versus `3/4`);
- and the standard finite-residue/profinite sequence checks.

No arithmetic defect was found. The gaps are assumptions, ontology, and
operational interpretation.

## Mandatory openings before round 2

Round 2 should not begin until the production artifacts do all of the
following:

1. **Restriction-category classification.** Separate arbitrary induced,
   ancestor-closed, convex/interval, collar-complete, and typed-carrier cuts;
   rerun finite exact ranks/positivity classifications for each.
2. **No-silent trichotomy.** Mark each cut autonomous, boundary-conditional,
   or refused, and state a different naturality square for each case.
3. **Physical statistic test.** Replace the abstract `q` oracle by a proposed
   carrier/provenance/update/gluing construction, or explicitly retain `q`
   only as a diagnostic target.
4. **Operational capacity axiom.** Define the resource being bounded and
   distinguish per-record, per-boundary, deterministic, stochastic,
   zero-error, expected, and approximate capacity.
5. **Loophole models.** Give exact stochastic-encoder, expanding-collar, and
   unbounded-mark formulations and locate any remaining global dependence.
6. **Terminology repair.** State T1 as an empty/full universal-precursor
   collapse under strong unmarked all-subset autonomy; do not promote it to a
   no-go for locality in general.
7. **Profinite ceiling.** Restrict P2 to the standard profinite-integer
   topology and continuous real readouts; do not infer a result about all
   Stone/profinite boundary spaces.
8. **Receipt boundary.** Preserve the explicit conclusion that no final
   bounded record-local interacting extension law has been selected.

## Verdict

**MAJOR REVISION.** The core mathematics survives hostile review and is worth
keeping. The strongest defensible headline is:

> Strong unmarked autonomy under every induced-subset restriction collapses
> positive down-set growth to an empty/full universal-precursor mixture. For
> supplied nontrivial laws, exact silent restriction can require an unbounded
> family of law-relative deterministic predictive quotients, and one standard
> profinite-integer completion does not make the chain readout continuous.

That is a sharp boundary theorem. It is not yet a theorem that SHARD locality
forces global shock, that finite evidence forces a fixed alphabet, that a
completion vector is a born record, or that profinite record spaces fail.

