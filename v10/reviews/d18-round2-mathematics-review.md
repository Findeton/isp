# D18 focused round-2 mathematics review

**Date:** 2026-07-12  
**Verdict:** **PASS AT THE FINITE/CYLINDER OPERATIONAL SCOPE**

## Decision

The round-one mathematical blockers are closed. The theorem now separates:

```text
operational probability core: typed event algebra E plus decoherence functional D;
query/record/unit interpretation;
physical explanatory generator: domain, measure, action, state and instruments.
```

All 15 partitions of the four-history algebra preserve Hermiticity,
normalization and strong positivity. General positivity and coarse-graining
closure are proved analytically by Gram/incidence identities; the finite grid
is correctly labeled regression coverage.

The D17 causal tower is now lifted to diagonal functionals `D_n`, with exact
block restriction through depths one to six. Factorization sign moves are
classified as representation gauge, and the theorem explicitly refuses a
full sigma-algebra extension.

## Reproduction

```text
source    99e0b696bb1c39374a4b366a4c07fc72f3b9dffae38850d70292c9e64947032f
packet    d5d318373b140df932d8051f90eb1f6a9afb599d45c042c34412b850ee2346b5
theorem   c6ff937539e35f5269d698cfb88889be262896ac15a76772445954c71fdd69de
receipt   b92a8c71014862d88479908d10e7dd9879efe26a748c4e198ccb82a0ea0d101b
ledger    06f8332241189950a51ecbd2e0b64ed74370b4b5bdde58af91a2cc58cf6b4a0a
stdout    04ffee18f1ea2c99599e99b47faef1ee1ce24c0e6cf371a7606cdad0e37aa455
checks    30/30 normal and optimized
```

Normal and optimized output are byte-identical.

## Operational core

On a finite typed event algebra, `(E,D)` is sufficient to evaluate quantum
weights, test decoherence, assign probabilities to decoherent partitions and
form conditionals on positive events. Instruments and units are no longer
called additional mathematical inputs once their operational effects are
encoded in `D`.

The richer generator packet remains necessary for explaining how the physical
functional, records and dimensional interpretation arise. This resolves the
previous minimality contradiction: “minimal” applies to the operational core,
not to the explanatory action packet or unit dictionary.

## Positivity and all coarse grainings

Both fine functionals are Gram matrices, so for arbitrary complex `c`,

```math
c^dagger D c = ||sum_i c_i branch_i||^2 >= 0.
```

For a partition incidence matrix `M`, coarse graining gives

```math
D' = M D M^dagger,
```

which preserves Hermiticity and strong positivity and satisfies
`D'(Omega,Omega)=1`. The code enumerates all Bell-number `B_4=15` partitions
as regression coverage. This is the correct analytic/executable division.

Nondecoherent partitions still reject before diagonal entries are interpreted
classically. Recorded versus unrecorded functionals retain identical fine
diagonals but different off-diagonals and different output laws, correctly
showing that a classical fine-history measure is insufficient.

## Integrated causal functionals

Each projective D17 cylinder table becomes one diagonal strongly-positive
functional `D_n`. The restriction incidence map satisfies

```math
D_n = M D_(n+1) M^dagger
```

at every adjacent depth from one through six. Its diagonal probabilities are
therefore one coherent projective family, and the next-record conditional is
ordinary disintegration of that same family. The interferometer and causal
tower are no longer presented as one unconnected sufficiency witness.

The result remains a cylinder-algebra theorem. For the durable classical
record subalgebra, ordinary projective extension may apply under its stated
hypotheses; an arbitrary quantum decoherence functional need not extend to the
full generated sigma algebra. The theorem states this ceiling explicitly.

## Necessity and factorization scope

Changing physical boundary state or record generation changes `D` and
operational predictions. Changing the query changes the requested observable,
not the core law. Changing units leaves dimensionless probabilities fixed but
changes dimensional reports. These roles are now distinguished rather than
all being called irreducible probability inputs.

The envelope/phase sign-moving example leaves their product and every
observable unchanged. It is correctly classified as representation gauge,
not physical nonselection. Only interventions that change the operational
functional support physical generator nonuniqueness.

## Gate disposition

```text
Q0 PASS: operational, interpretation and generator layers separated.
Q1 PASS at finite/cylinder witness scope.
Q2 PASS for the stated role/necessity ledger, not unique physical selection.
Q3-Q4 inherited finite covariance/local-generation scope.
Q5 PASS: normalized strongly-positive D and all finite partitions.
Q6 PASS through depth six at cylinder scope; full sigma extension withheld.
Q7-Q10 remain recovery/empirical ledgers, not new selection theorems.
Q11 OPEN beyond this review stream.
```

## Final verdict

**PASS AT THE FINITE/CYLINDER OPERATIONAL SCOPE.** The `(E,D)` core split,
all-partition closure, integrated causal restriction law, positivity proof,
factorization-gauge wording and cylinder ceiling are mathematically sound.
This does not select the physical generator packet or prove a full quantum
sigma-algebra measure.
