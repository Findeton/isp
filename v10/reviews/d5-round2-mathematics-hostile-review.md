# D5 hostile round-2 mathematics / probability / capacity review

**Date:** 2026-07-11  
**Verdict:** **PASS at the repaired claim ceiling**  
**Blocking findings:** none  
**New openings:** none

## Frozen sources reviewed

- `v10/note-d5-typed-collar-message-algebra.md`  
  SHA-256 `883f27535ab82e60a49f896b82a3910113291661f1706b5fe1bde652ba48f147`
- `v10/code/d5_typed_collar_exact.py`  
  SHA-256 `efbe43a452784ccf8e78db6404826adcfe1d554cc5dfe875689b2a1cf7340c85`
- `v10/relativistic-isp-v10-paper6-typed-collar-composition.md`  
  SHA-256 `f2d31845a97379f36f8c01acc065d36a73c1336d7843954a06cb6658e7626005`
- `v10/reviews/d5-hostile-round1-opening-ledger.md`  
  SHA-256 `f44e1e01cd6fed6d12d9877c3a4d4c5b5316c5802d1c4f3e674ab2b0a9374aea`

The repaired executable was run twice. Both runs reported **34/34** and had
byte-identical stdout SHA-256
`e7e8e345314e852552c63bc61a8fbecfb5f2af3d85140507dd22db42277118a8`.

## Independent reconstruction

I reran the original clean-room arithmetic and independently rebuilt the new
round-2 cells without importing the production implementation. The decisive
values are

```text
complete parity ranks:                    1, 3, 7
product Fisher rank/trace at n=6:         6 / 9/2
16-channel chi-square upper partial:      1431655765/17179869184
gap from the analytic 1/12 ceiling:       1/51539607552
three-factor chain table:                 29,25,31,35
branching-tree entries/endpoints:         16 / 319,319
branching-tree full table:                319,205,215,269,205,151,149,215,
                                           215,149,151,205,269,215,205,319
exactly-once ownership table:             15,12,13,20
loop separator table:                     20,6,6,20
dummy/separable/irreducible determinants: 0 / 0 / 3
derived shared-ancestor message:          10,6,6,10
same/reverse-ray predictions:             (5/12,7/12) / (7/12,5/12)
primitive width-one ray at step 32:       17167680177565,27777890035288
primitive bit growth:                     2 -> 45
incompatible support product:             0,0,0,0
swap-invariant scope families:            4 total / 3 nonempty
```

The two Bernoulli families `p=2/3` and `p=3/4` also marginalize exactly
through width eight and remain distinct.

## Probability and table types

The executable now has four explicit kinds: strict-positive primitive factor,
nonnegative support-control factor, derived message, and the provenance-free
scalar identity. Primitive factors require nonempty scope and exactly one ID;
negative entries are rejected globally; positive factors reject zeros;
support factors require nonempty support; and the identity is uniquely typed.

Adversarial runtime checks independently confirmed refusal of:

- the signed message `(-1,2)`;
- an all-zero primitive support factor;
- a provenance-bearing object labeled as identity.

The final hardening also ensures that a one-factor region with no eliminated
variable returns kind `message`, not the original primitive-factor kind, while
retaining its provenance. Primitive and derived objects therefore no longer
masquerade as one another at this boundary.

The structural-zero ceiling is exact. Compatible equality supports produce
`(1,0,0,1)` and normalize on their surviving fibers. Equality and inequality
supports multiply to the all-zero impossible message, which refuses
normalization. The paper labels these as controls and leaves general
fiberwise support calculus and conditional versions open.

## Exact factor-partition composition

The sum-product theorem is correct for a supplied complete finite factor
partition with unique IDs allocated exactly once. Direct elimination, both
three-piece parenthesizations, reverse variable schedule, and the branching
tree agree exactly. The clean-room branch table reproduces every one of the
16 production entries.

The ownership repair is also real. A unary separator factor allocated once to
the left or once to the right gives the same `(15,12,13,20)` result as direct
elimination. Derived-message provenance is the union of its constituents, so
attempting to reintroduce that separator factor is refused.

The paper now states the correct ceiling:

- IDs and ownership are supplied, not derived;
- fresh-ID semantic duplication is not detected;
- no physical interface type or direction is constructed;
- invariance concerns elimination schedules for one fixed identified factor
  multiset, not physical record-birth construction-order gauge.

The missing parenthesization, branch, and nested-reuse receipt cells from round
1 have all been executed.

## Positive-ray sufficiency and minimality

The mathematical theorem remains sound. Proportional positive separator
messages multiply every candidate-state weight by one common scalar, which
cancels under normalization. For distinct normalized messages `p,q`, the
strictly positive test

$$
g(b)=1+\mathbf 1[b=b_0]
$$

distinguishes them whenever `p(b0) != q(b0)`. Thus the ray is the coarsest
predictive partition against the full class of arbitrary strictly positive
full-separator tests.

The repaired note and paper keep that test-class quantifier everywhere
load-bearing. They explicitly allow a restricted future physical proposal
class to have a coarser quotient and call the ray a universal diagnostic
target rather than a derived minimal physical record. Candidate-state
prediction is also correctly separated from proposal, no-birth, eligibility,
evidence, and seal laws.

## Scope, incidence, and covariance

The added controls correctly distinguish:

1. listed table scope;
2. essential-variable dependence;
3. separable versus irreducible pair interaction;
4. primitive factor-hyperedge incidence;
5. derived correlation after elimination;
6. directed physical transport, which is not implemented.

The determinant controls `0,0,3` and the derived `(10,6,6,10)` message verify
the first five distinctions. The paper claims no sixth.

Within the explicitly frozen candidate list `{ZA,ZB,ZAB}`, the `A<->B` action
has exactly three nonempty invariant eligibility families. The paper now calls
them swap-invariant eligibility families in that candidate arena, not a
classification of covariant numerical proposal laws.

## Screen-relative ranks and bounded KL

The repaired rank statements are exact:

- duplicate or linearly dependent channels do not raise rank;
- jointly relabeling the complete ledger and screen preserves rank;
- adding a symmetry-translated observable can raise rank;
- covariance/Gram rank is screen-relative;
- Fisher rank additionally assumes the declared exponential family and
  natural parameterization;
- Fisher trace is an illustrative scalarization, not intrinsic content.

The parity `1/3/7`, collective rank-one, and product `rank=n`,
`trace=3n/4` calculations all reproduce independently.

The weak-channel construction now builds the rational distributions
explicitly and recomputes TV and chi-square. For

$$
\delta_i=2^{-(i+3)},
\qquad
D(P_i\Vert U)\le\chi^2(P_i\Vert U)=4\delta_i^2,
$$

the infinite upper sum is exactly `1/12`. The repaired conclusion is limited
to bounded additive KL/evidence divergence from the chosen null in the
absence of a positive carrier/metadata floor. It makes no claim about exact
description length or every possible content functional.

The combined arity conclusion is therefore defensible: participant count,
listed channels, screen-relative rank, additive KL, and exact encoding cost
are distinct resources, and none may be silently substituted for another.

## Separator-state growth

The width count is a worst-case coordinate statement: an arbitrary binary
width-`b` table has `2^b` entries and positive-ray dimension `2^b-1`.
The loop proves one-site marginals can be insufficient, not that every loop
needs a full exponential table.

For the width-one recurrence

$$
(a_{n+1},b_{n+1})=(a_n+b_n,a_n+2b_n),
$$

`gcd(a+b,a+2b)=gcd(a,b)`, so the ray remains primitive, and `b_n` grows
strictly. This proves that positive-ray rescaling cannot erase the exact table
growth. The receipt gates distinct primitive rays, `2->45` primitive bits,
and `3->46` normalized-rational bits through 32 steps. Paper 6 correctly calls
this table-description growth, not an optimal algorithmic lower bound or
physical information capacity.

The verdict has accordingly been renamed `EXACT-SEPARATOR-STATE-GROWTH`; no
distributed physical encoding is claimed.

## Connected-domain and projective ceilings

The component invariant is correct and explicitly conditional: a supplied
candidate with primitive legs only into one component cannot merge components;
a declared one-component proposal domain stays connected given a supplied
connected seed. A multileg proposal token can merge components, but the
factor algebra does not create that token, its direction, or the seed.

The two Bernoulli towers are valid numerical projective nonselection
witnesses, and their product formula extends analytically beyond the finite
receipt. The paper does not promote them to a typed provenance tower, physical
encoder/update system, selector, or new general profinite theorem.

## Final adjudication

**PASS.** The exact supported result is:

```text
supplied complete finite factor partition with exactly-once IDs
  -> exact separator contraction and fixed-multiset schedule invariance;
positive separator ray
  -> universal predictive quotient for arbitrary positive full-separator tests;
bounded additive KL without a carrier floor
  -/-> rank or arity bound;
exact separator state
  -> width and canonical rational-table growth;
composition and covariance
  -/-> proposal, scope, value, evidence, seal, or first joining token.
```

No physical record birth, interacting click law, distributed carrier encoding,
construction-order quotient, speed, cone, dimension, horizon, quantum, or
absolute-scale theorem is claimed.
