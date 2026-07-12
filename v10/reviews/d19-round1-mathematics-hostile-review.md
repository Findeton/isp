# D19 hostile round-1 mathematics review

**Date:** 2026-07-12  
**Verdict:** **MAJOR REVISION — VERDICT LABEL OUTRUNS THE THEOREM**

## Decision

The finite identifiability theorem is exact and correct. On eight binary
histories, normalization plus all degree-one and degree-two Walsh moments has
rank seven. Its null space is the one-dimensional `xyz/8` direction. The laws

```math
P_r(x,y,z)=(1+rxyz)/8
```

are normalized and strictly positive for `-1<r<1`. The choices `r=1/2` and
`r=1/3` agree on every one/two-record marginal but differ on triple correlation
and future conditional holdouts.

What is not proved is `EMPIRICAL-GENERATOR-NONSELECTION`. The executable
constructs two classical history laws, not two physical generators, and no
candidate generator class or map `G -> D_G` is implemented. A restricted
generator family could map injectively into either law, or might realize only
one. History-law nonidentifiability from the frozen observations is necessary
evidence against generator identification, but is not itself a generator
nonselection theorem.

## Reproduction

```text
source    9f2f9c7b8a9a27ed145fcc8e13524054db28c69251d70cc4fe173437ebf29bf6
packet    f137019ca9cb7aaa8f98eb81c4ef887a29a851959b8a2918134d7a0fa7dd7507
receipt   2f7f5f350f5e7f11488e497331cd5811b6370492c888a54be8f6aef2d97464ea
semantic  6e102423970bff5e8732c29cf7fcc8d8a51e5d04136e1cce62ac155bc9314df5
stdout    4504da4feb37e3556d6d3fd856894954b8a915cb53e184ea422c21082900e75f
checks    20/20 normal and optimized
```

Normal and optimized output are byte-identical.

## Exact rank and null space

The observation rows are the seven independent Walsh characters

```text
1, x, y, z, xy, xz, yz.
```

Orthogonality of the eight Walsh characters already proves rank seven and
identifies the missing character `xyz`. The exact Gaussian elimination and
matrix-vector multiplication reproduce this. Since the kernel dimension is
`8-7=1`, the displayed nonzero direction spans the full null space.

For binary variables, these moments determine all one- and two-variable
marginals, and the executable additionally compares those marginals directly.
Every pair table is uniform `1/4` for both survivors.

## Positivity and holdouts

For each history, `P_r` is either `(1+r)/8` or `(1-r)/8`; therefore strict
positivity holds exactly for `|r|<1`. Normalization follows because the `xyz`
character sums to zero. The chosen survivors and the sampled perturbations
are correctly inside this interval.

The difference between `r=1/2` and `r=1/3` is exactly one-sixth of the null
direction. Their untouched toy holdouts are correctly computed:

```text
E[xyz]                         1/2 versus 1/3
P(z=1 | x=1,y=1)              3/4 versus 2/3.
```

Both laws are visibly non-Markov relative to current visible record `y`,
because fixing `y` while changing earlier `x` changes the next-`z`
conditional. Denominators are positive by strict positivity.

These are legitimate holdouts for the frozen toy observation map, not new
measurements of nature. The theorem draft says this correctly.

## History-law versus generator identification

The proved map is

```text
history law P -> seven training moments.
```

The protocol's target map is

```text
physical generator G -> history functional D_G -> observed data.
```

Noninjectivity of the second arrow does not by itself establish two points in
the image of the first arrow from a frozen physical generator class. To claim
generator nonselection, D19 must exhibit two physically inequivalent complete
generators `G_1,G_2` that realize the two laws, survive the equivalence quotient,
and agree on all training evidence while differing on the holdout.

Conversely, no finite marginal fit can identify the unrestricted whole-history
law. This blocks any generator-identification argument that relies on those
marginals alone unless the independently frozen generator class is proved to
remove the null direction. That is the correct consequence.

## Required repair

1. Rename the executable and semantic verdict to something like
   `FINITE-HISTORY-LAW-NONIDENTIFIABILITY`.
2. State that it refutes unrestricted history-law identification from the
   frozen low-order observations.
3. Reserve `EMPIRICAL-GENERATOR-NONSELECTION` for two realized, inequivalent
   generator packets or a theorem that the generator image contains the null
   family.
4. Keep the physical evidence ledger and V9 refusal as motivation/scope, not
   as an exact consequence of the eight-history calculation.

## Gate disposition

```text
I0 OPEN for physical generators; finite law class is frozen.
I1 OPEN for generator equivalence; distinct laws are operationally inequivalent.
I2 PASS exactly for the finite history-law observation map.
I3-I7 evidence/scope ledgers only, not proved by this executable.
I8 PASS for the toy holdout discipline; no physical holdout opened.
I9 PASS as a refusal.
I10 OPEN; this review finds a verdict-scope blocker.
```

## Final verdict

**MAJOR REVISION.** Rank, null space, positivity, marginals, conditionals and
hashes all pass. Freeze the exact subresult as finite history-law
nonidentifiability. Do not label it generator nonselection until the two laws
are realized by a frozen inequivalent generator class.
