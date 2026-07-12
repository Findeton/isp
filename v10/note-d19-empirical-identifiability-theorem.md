# D19 theorem draft — finite evidence selects shadows, not necessarily the law

**Status:** final after two hostile rounds at frozen finite history-law scope,
2026-07-12.

## Exact theorem

Take the eight complete binary histories `(x,y,z)` and train only on
normalization, the three one-record moments and the three two-record moments.
The resulting exact observation matrix is the seven-row Walsh-character
matrix

```text
1, x, y, z, xy, xz, yz.
```

It has rank seven.  Its one-dimensional null direction is `xyz/8`.  The
strictly positive normalized family

```math
P_r(x,y,z)=(1+r xyz)/8,qquad -1<r<1,
```

moves exactly along that invisible direction.  In particular, `r=1/2` and
`r=1/3` agree on every frozen one- and two-record marginal, but

```math
E[xyz]=1/2 versus 1/3,
```

and

```math
P(z=1|x=1,y=1)=3/4 versus 2/3.
```

Both survivors are visibly non-Markov in the current record `y`.

**Finite empirical non-identifiability.**  A rank-deficient observation map on
complete histories can leave a nonzero operational history-law direction through the
interior of the positive normalized law space.  Training evidence then cannot
select the whole-history law; a higher-order holdout can.

This is an exact history-law theorem, not yet a proof that two fully specified
Standard-Model-plus-gravity ultraviolet generators realize these particular
eight probabilities.

## Consequence for the rulebook search

The theorem blocks a common shortcut:

```text
all measured local marginals fit
therefore
the full non-Markov universe law has been identified.
```

That implication is false.  It also explains why Barandes-style full-history
data are substantive: instantaneous or low-order probability shadows need not
determine the probability on trajectories.

Independent evidence can still identify a **restricted candidate family** if
the observation map is injective on that family.  The restriction itself must
be justified independently; otherwise it hides the missing null directions.

## Physical evidence ledger inherited from D15-D18

| generator field | strongest current status in this corpus |
|---|---|
| effective 3+1 field content | Standard Model plus Lorentzian metric selected by extensive low-energy evidence; not derived from records |
| low-energy action form | Einstein-Hilbert plus the Standard Model is the leading extensively tested baseline at declared scope; allowed higher operators/extensions remain |
| coefficients, masses, mixings, `G`, `Lambda` | measured/fitted inputs, with scale-dependent conventions |
| higher EFT operators | bounded incompletely; infinitely many coefficients are not all identified |
| ultraviolet completion/causal-order action | open; D16 coefficient family and D17 kernel nonselection survive |
| cosmological boundary state | constrained by cosmological data, not uniquely derived |
| gauge measure/contour | theory- and observable-dependent; no unique quantum-gravity construction selected |
| durable-record variables | conditionally generated in D14/D17 finite packets; universal emergence not proved |
| metres/seconds dictionary | operationally calibrated; dimensionless records do not set it |
| round cone and 3+1 geometry | V9 phenomenology remains downstream; in EFT4 they are inputs, not emergent holdouts |

## Holdout discipline

The exact `xyz`/future-conditional cells are **designed discriminators**, chosen
from the null direction used to construct the survivors.  They are not
untouched predictions, are algebraically the same `r` coordinate, and are not
empirical measurements of our universe.  No V9 cone or dimension dataset is
opened here because no surviving fundamental generator fixes a cross-candidate
value without fitted nuisance parameters.

## Candidate exact verdict

```text
FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY
```

is proved for the frozen finite history-law class.  It is not
`EMPIRICAL-GENERATOR-NONSELECTION`: that stronger result requires two complete
inequivalent local covariant generators whose images realize the surviving
laws.  The broader D19 physical verdict remains `INCOMPLETE-INVESTIGATION`
until such a candidate census, complete evidence ledger and real untouched
discriminator exist and are hostile-reviewed.
