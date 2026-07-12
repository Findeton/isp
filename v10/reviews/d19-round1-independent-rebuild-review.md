# D19 hostile review, round 1: independent clean-room rebuild

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-12  
**Finite history-law theorem:** **PASS**  
**`EMPIRICAL-GENERATOR-NONSELECTION` verdict:** **MAJOR SCOPE REVISION**

The 20-check executable reproduces exactly in normal and optimized Python.
An independent Walsh-basis reconstruction confirms rank seven, the complete
one-dimensional nullspace, the normalization and scaling of `P_r`, every
one- and two-record marginal, the full positivity interval, both holdout
values, and the non-Markov conditionals.  I found no arithmetic, rank or
factor-of-eight error.

The exact theorem proved is narrower than the executable verdict.  It gives
two inequivalent positive **complete history laws** that agree on a frozen
low-order observation map and differ on the omitted triple interaction.  It
does not construct two physical generator packets
`(domain,measure,action,state,instruments,units)`, establish that both laws lie
in a frozen physical generator class, or quotient generator gauge/field
redefinitions.  The manuscript admits this ceiling, but the semantic verdict
still says `EMPIRICAL-GENERATOR-NONSELECTION`, whose protocol definition
requires explicit inequivalent positive generators.

Accept the result as `FINITE-HISTORY-LAW-NONIDENTIFIABILITY` or provide two
fully specified generator realizations before promoting the generator-level
verdict.

## 1. Reproduction and frozen hashes

The following were repeated:

```bash
python3 v10/code/d19_empirical_identifiability_exact.py
python3 -O v10/code/d19_empirical_identifiability_exact.py
python3 v10/code/d19_empirical_identifiability_exact.py | shasum -a 256
python3 -O v10/code/d19_empirical_identifiability_exact.py | shasum -a 256
shasum -a 256 v10/code/d19_empirical_identifiability_exact.py
shasum -a 256 v10/data/d19-empirical-identifiability-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 20/20
SEMANTIC SHA256: 6e102423970bff5e8732c29cf7fcc8d8a51e5d04136e1cce62ac155bc9314df5
SOURCE SHA256: 9f2f9c7b8a9a27ed145fcc8e13524054db28c69251d70cc4fe173437ebf29bf6
VERDICT: EMPIRICAL-GENERATOR-NONSELECTION
```

Normal and `-O` stdout hashes are identical:

```text
4504da4feb37e3556d6d3fd856894954b8a915cb53e184ea422c21082900e75f
```

The packet hash matches the receipt:

```text
f137019ca9cb7aaa8f98eb81c4ef887a29a851959b8a2918134d7a0fa7dd7507
```

There is no Python `assert` or `__debug__` gate.  Explicit checks, the final
count guard and semantic digest survive optimization; output is written only
after they pass.

## 2. Independent rank and nullspace reconstruction

Order the eight histories lexicographically over `(-1,+1)^3` and let `A` have
rows

```text
1, x, y, z, xy, xz, yz.
```

These are seven distinct Walsh characters.  Direct exact multiplication gives

```math
A A^T = 8 I_7.
```

The rows are therefore independent and `rank(A)=7`, without depending on a
particular elimination pivot order.  The eighth Walsh character is

```text
u(x,y,z)=xyz.
```

Orthogonality gives `A u=0`.  Since the nullity is one, the complete kernel is

```math
ker A = span{u}=span{u/8}.
```

The executable's direction is exactly

```text
xyz/8 = (-1,+1,+1,-1,+1,-1,-1,+1)/8,
```

so its normalization is correct.  Using `xyz` instead would describe the same
kernel but change the family parameter scale by eight; the source does not
make that mistake.

## 3. The full `P_r` family and positivity interval

The law is

```math
P_r(x,y,z)=1/8+r xyz/8.
```

Its eight atoms take only two values:

```text
(1-r)/8 when xyz=-1,
(1+r)/8 when xyz=+1.
```

Consequently:

```text
normalized for every r;
valid nonnegative law exactly for -1 <= r <= 1;
strictly positive exactly for -1 < r < 1.
```

At the endpoints four atoms vanish; outside the closed interval at least one
atom is negative.  The theorem's open strict-positivity interval is exact.
The source's samples `-9/10,0,9/10` are regression points inside that interval,
not the analytic proof.

For the two frozen survivors:

```text
r=1/2: atoms are 1/16 or 3/16;
r=1/3: atoms are 1/12 or 1/6.
```

Both are normalized, strictly positive, and unequal.

## 4. Training moments and every low-order marginal

For any character of degree at most two, multiplying by `xyz` produces a
nonconstant Walsh character.  Its uniform sum vanishes.  Therefore every
training expectation is independent of `r`:

```text
E[1]=1,
E[x]=E[y]=E[z]=0,
E[xy]=E[xz]=E[yz]=0.
```

For binary `+/-1` variables, those moments determine every one- and two-variable
marginal.  Direct summation independently gives:

```text
P(x)=P(y)=P(z)=1/2 for each sign;
P(x,y)=P(x,z)=P(y,z)=1/4 for every sign pair.
```

Thus the source's moment statement and its stronger marginal statement are
both exact.  The training map is rank-deficient even with noiseless, infinitely
precise low-order data; finite sampling uncertainty is not responsible.

## 5. Holdouts and scaling

The omitted character is itself the first holdout:

```math
E_r[xyz]=r.
```

Hence the survivors give `1/2` and `1/3` exactly.

The complete conditional formula is:

```math
P_r(z=1|x,y)=(1+rxy)/2.
```

At `y=1`:

```text
                 x=+1   x=-1
r=1/2             3/4    1/4
r=1/3             2/3    1/3.
```

Since the pair marginal gives `P(z=1|y)=1/2`, dependence on the earlier `x`
at fixed current `y` is a genuine visible violation of the first-order Markov
condition for every nonzero `r`.

The two advertised holdout cells are not independent empirical directions:
the triple expectation and future conditional both identify the same scalar
`r`.  They are two operational presentations of the one missing Walsh
coefficient.  This does not weaken their separating power, but it should not
be counted as two independent validations.

Finally,

```math
P_{1/2}-P_{1/3}=(1/6)(xyz/8),
```

exactly as source check 19 states.  There is no missing factor of eight or six.

## 6. What the rank theorem proves

On the full eight-history probability simplex, the seven-row map fixes an
affine one-parameter survivor family.  The uniform law is an interior point,
and the null direction crosses the interior for `-1<r<1`.  Distinct survivors
make different predictions for an observation excluded from training.

Therefore the following inference is rigorously invalid:

```text
all exact one- and two-record marginals are known
therefore
the complete three-record law is known.
```

This is a valid finite empirical non-identifiability theorem for history laws.
The two laws are not gauge-equivalent on the frozen observable algebra because
the `xyz` holdout distinguishes them.

The toy holdout is “untouched” only relative to the frozen toy training map.
It is not new data about nature, and the theorem/receipt correctly say so.

## 7. Generator-level claim ceiling

The D19 protocol defines the generator map as

```text
G -> D_G -> y_train
```

and its `EMPIRICAL-GENERATOR-NONSELECTION` verdict requires explicit
inequivalent positive generators that agree on training evidence and differ on
a holdout.  The executable begins at the middle/output layer: it supplies two
classical laws `P_r`.  It does not specify for either survivor:

- a typed regional history/domain and fields;
- a gauge/reference measure or contour;
- a local action and coefficients;
- a normalized boundary/cosmological state;
- physical record instruments and future algebra;
- a unit/scale dictionary;
- the equivalence quotient on those generator fields.

Nor does it prove that a frozen physical candidate class contains realizations
of both `P_{1/2}` and `P_{1/3}`.  History-law nonidentifiability strongly warns
against generator identification, but the logical lift requires a realization
map or an independently justified primitive-law generator class.

The theorem draft says exactly this in prose and marks broader D19
`INCOMPLETE-INVESTIGATION`.  The source semantic verdict should match that
discipline.  Recommended exact label:

```text
FINITE-HISTORY-LAW-NONIDENTIFIABILITY
```

with `EMPIRICAL-GENERATOR-NONSELECTION` retained as an open target.

## 8. Evidence and holdout scope

The inherited evidence ledger is appropriately cautious:

- low-energy Standard Model plus Einstein-Hilbert structure is empirically
  successful but supplied, not record-derived;
- coefficients, masses, mixings, `G` and `Lambda` are measured inputs;
- higher EFT operators and ultraviolet completion remain underidentified;
- cosmological state, gauge contour and universal record emergence remain
  open;
- metres and seconds are calibrated;
- V9 cone/dimension results are downstream training evidence, not untouched
  generator-discriminating holdouts.

No real geometry dataset is opened, so the exact toy result creates no data
leakage.  It also supplies no physical evidence that the particular `P_r`
family is realized by our universe.

## 9. Finding ledger

```text
D19-1 PASS   A is 7x8, AA^T=8I, rank=7, and ker A=span{xyz/8}.
D19-2 PASS   P_r is normalized; strict positivity is exactly -1<r<1.
D19-3 PASS   Every one/two-record moment and marginal agrees for all r.
D19-4 PASS   E[xyz]=r and P(z=1|x,y)=(1+rxy)/2 separate the survivors.
D19-5 PASS   P_1/2-P_1/3=(1/6)(xyz/8); no scaling error exists.
D19-6 MINOR  Triple and conditional holdouts test the same one-dimensional
             null parameter, not independent missing directions.
D19-7 MAJOR  The executable proves history-law nonidentifiability, not the
             protocol's generator-level verdict. The prose ceiling is honest,
             but the semantic verdict overstates it.
```

## 10. Decision

**PASS the exact finite history-law theorem.**  The rank, null direction,
probability family, low-order marginals, positivity interval, holdouts and
non-Markov conditionals survive independent reconstruction.

**MAJOR SCOPE REVISION for `EMPIRICAL-GENERATOR-NONSELECTION`.**  Rename the
current subresult or supply two explicit inequivalent generator packets and
their common training map.  Preserve the existing ceiling: this is not a
census or empirical selection result for physical ultraviolet theories, and
it licenses no V9 geometry holdout.
