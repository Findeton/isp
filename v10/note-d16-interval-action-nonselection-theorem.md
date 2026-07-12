# D16 theorem draft — poset relabeling does not select the causal action

**Status:** final finite theorem after hostile closure, 2026-07-11.

## Result

On a frozen finite class of strict causal orders, every scalar action

```math
S_{alpha,beta}(C)=alpha |C|+sum_k beta_k N_k(C)
```

is exactly invariant under poset relabeling, where `N_k` counts comparable pairs
whose open order interval contains `k` elements.  Relabeling covariance and
intrinsic interval dependence therefore constrain the form of the action but
do not select its coefficients.

The exact receipt checks the antichain, chain, `V`, `Lambda`, diamond and sewn
three-chain orders.  It exhausts every relabeling, computes typed-boundary
automorphism groups and linear extensions, rejects nontransitive relations,
non-antichain/nonextremal boundaries, ownership overlap and typed sewing
mismatch, and
enumerates all sixteen binary coefficient packets with
`alpha,beta_0,beta_1,beta_2 in {0,1}`.

All sixteen packets have distinct phase signatures on the expanded census.  In particular,

```math
S_A=N_0,
qquad S_B=N_2
```

are both label invariant, yet on the four-element diamond

```math
exp(i pi S_A)=+1,
qquad exp(i pi S_B)=-1.
```

The action-difference and phase-ratio vectors are nonconstant, so the packets
are not related by one common additive or multiplicative phase on the frozen
class.  Thus exact finite poset-relabeling covariance plus intrinsic interval
dependence is nonselecting.  This is not a theorem of continuum
diffeomorphism covariance or physical microcausality.

## Evaluation order and physical law

A causal order can have many linear extensions.  The action depends only on
the completed order, so all its birth-label presentations receive the same
phase.  This proves only that the supplied whole-order scalar ignores the
chosen linear-extension presentation.  It supplies no measure over
presentations, locally computable sequential growth rule, or support law
choosing which orders occur.

## Gluing obstruction

Gluing two two-element chains at one matching typed/owned extremal boundary
port and taking quotient transitive closure produces a three-element chain.
Independent regional relabelings preserve its interval, automorphism and
linear-extension counts, while a type mismatch rejects.  The closure creates a cross-boundary
interval with one interior element.  Therefore an action containing `N_1`
obeys

```math
S(C_left union_boundary C_right)
!= S(C_left)+S(C_right).
```

A quotient evaluator can own the cross interval by recomputing the action once
on the sewn order.  A factorizable regional sewing law would still need
explicit boundary/corner factors; it cannot blindly multiply
`exp(iS_left)` and `exp(iS_right)`.  This is the finite
causal-order analogue of the boundary/corner warning in D14/D15.

## Measure obstruction

Pure phases have unit modulus.  For two alternative orders the raw Born mass
in the receipt is `2`, not `1`.  A normalized quantum/history law additionally
requires:

```text
the alternative-history domain;
orbit/automorphism measure;
state or boundary amplitude;
normalization/decoherence rule;
possibly a regulator/limit.
```

All displayed normalization/orbit values are exact rationals.  Automorphism factors differ already between a four-element chain (`1`) and
antichain (`24`).  Summing labeled orders without an explicit orbit convention
would insert gauge multiplicity into physics.

## Dimension and BDG scope

Dimension-specific interval coefficients can be justified by matching a
causal-set operator/action to a continuum limit in a declared dimension.  In
that construction the dimension and nonlocality/discreteness scale enter the
coefficient packet.  Recovering the chosen continuum dimension is then a
calibration result unless a separate dynamical phase-selection theorem shows
that other dimensions are suppressed.

The exact D16 code does not claim to implement published BDG coefficients.  It
proves the upstream nonselection theorem that makes their continuum-matching
provenance necessary.

## Verdict and ceiling

```text
INTERVAL-ACTION-FAMILY-NONSELECTING
```

is proved on the frozen finite coefficient class.  The theorem does not yet supply a quantum measure, action-to-D14
record instrument, generally covariant matter sector, stable `3+1` phase,
round-cone prediction, proper units or `G`.  Formal D16 remains
`INCOMPLETE-INVESTIGATION` until those protocol gates are adjudicated.
