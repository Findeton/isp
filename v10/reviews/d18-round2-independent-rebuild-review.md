# D18 hostile review, round 2: independent clean-room rebuild

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-12  
**Candidate-subresult verdict:** **PASS — `FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY`**  
**Minimal/unique rulebook verdict:** **NOT ESTABLISHED**

The repaired 30-check executable reproduces exactly in normal and optimized
Python.  An independent rational reconstruction confirms both interferometer
decoherence functionals, every one of the fifteen coarse partitions, the
state/instrument interventions, the factorization gauge, and the causal
diagonal `D_n` family and conditionals.  Direct continuation remains
projective through depth 100.

The repaired layer split is correct: a typed event domain and a normalized
strongly-positive decoherence functional are sufficient to answer every
declared decoherent probability question; record semantics, queries and units
interpret that core; a richer action/state/measure/instrument packet explains
how the core might arise.

“Sufficient” must not be strengthened to “minimal” without an operational
equivalence theorem.  I constructed two distinct normalized strongly-positive
complex functionals on the same event algebra that have identical quantum
measures, identical decoherent partitions and identical licensed classical
probabilities.  Thus the full matrix `D` can contain representation data that
the declared Boolean event questions do not distinguish.  The manuscript
already withholds `MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK`, so this is a scope
boundary rather than a rejection of its exact candidate subresult.

## 1. Reproduction and hashes

The following were repeated:

```bash
python3 v10/code/d18_minimal_history_rulebook_exact.py
python3 -O v10/code/d18_minimal_history_rulebook_exact.py
python3 v10/code/d18_minimal_history_rulebook_exact.py | shasum -a 256
python3 -O v10/code/d18_minimal_history_rulebook_exact.py | shasum -a 256
shasum -a 256 v10/code/d18_minimal_history_rulebook_exact.py
shasum -a 256 v10/data/d18-minimal-history-rulebook-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 30/30
SEMANTIC SHA256: e92b39b7308e6e51887ef073430e86608e96de863874fcf46b217f1d5d5dc779
SOURCE SHA256: 99e0b696bb1c39374a4b366a4c07fc72f3b9dffae38850d70292c9e64947032f
VERDICT: FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY
```

Normal and `-O` stdout hashes are identical:

```text
04ffee18f1ea2c99599e99b47faef1ee1ce24c0e6cf371a7606cdad0e37aa455
```

The packet and dependency hashes match the receipt:

```text
packet          d5d318373b140df932d8051f90eb1f6a9afb599d45c042c34412b850ee2346b5
integrated D17  5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57
```

No `assert` or `__debug__` gate occurs.  The explicit checks and final count
and semantic-hash guards survive `-O`; the packet is written afterward.

## 2. Explicit interferometer reconstruction

With fine histories ordered as

```text
(path,output) = 00,10,01,11,
```

the independently reconstructed unrecorded functional is

```text
       [ 1  1  0  0 ]
D0=1/4 [ 1  1  0  0 ]
       [ 0  0  1 -1 ]
       [ 0  0 -1  1 ].
```

The path-record commit makes the four branch vectors orthogonal:

```text
DR = diag(1/4,1/4,1/4,1/4).
```

Both are Hermitian and satisfy `D(Omega,Omega)=1`.  `D0` is the Gram matrix of
two output-space branch pairs; `DR` is the Gram matrix after tensoring an
orthogonal path record.  Hence for arbitrary complex coefficients—not merely
the executable grid—

```math
c^dagger D c = ||sum_i c_i b_i||^2 >= 0.
```

The output coarse grainings are exactly:

```text
without record  [[1,0],[0,0]]     -> (1,0)
with record     [[1/2,0],[0,1/2]] -> (1/2,1/2).
```

All four fine diagonals remain `1/4`.  The change therefore resides in
off-diagonal interference data; a classical fine-path distribution cannot
replace `D`.

The path partition of `D0` is `diag(1/2,1/2)`, independently confirming that
the same functional answers a distinct declared question.  A matrix with
nonzero coarse off-diagonals correctly rejects before its diagonal is called a
classical probability.

## 3. All fifteen coarse partitions

I regenerated the Bell-number `B_4=15` set partitions independently and formed
each coarse matrix by exact block summation.  Every coarse functional is
Hermitian, normalized and strongly positive because it is `M D M^dagger`.

The complete decoherence classification provides a stronger audit than the
source's positivity regression:

```text
unrecorded D0: 4 of 15 partitions decohere
recorded DR:  15 of 15 partitions decohere.
```

The four decoherent unrecorded partitions and their probabilities are:

```text
{0123}             -> (1)
{01}|{23}          -> (1,0)       output
{02}|{13}          -> (1/2,1/2)   path
{03}|{12}          -> (1/2,1/2)   crossed cancellation
```

For `DR`, every partition is decoherent and a block containing `k` fine
histories has probability `k/4`.

The source checks all fifteen partitions only for `D0` and tests strong
positivity on a finite real coefficient grid.  That grid is regression
coverage, not the proof.  The proof is valid because `decoherence(branches)`
constructs a Gram matrix and coarse graining is an incidence congruence.  The
theorem states this analytic division correctly, although source check 7's
label is stronger than its one-vector predicate.

## 4. State and instrument interventions

Changing the initial state from `0` to `1` while keeping the two-Hadamard
interferometer fixed gives

```text
       [ 1 -1  0  0 ]
D1=1/4 [-1  1  0  0 ]
       [ 0  0  1  1 ]
       [ 0  0  1  1 ],
```

and the output law flips from `(1,0)` to `(0,1)`.  This is a clean physical
boundary-state intervention.

The normalized positive path amplitudes `(3/5,4/5)` give output amplitudes
proportional to `7` and `-1`, hence probabilities:

```text
(49/50,1/50).
```

The path-record intervention changes `D0` to `DR` and changes the output law
while the four typed histories and their fine diagonal weights remain fixed.
It therefore demonstrates that physical record generation can be
operationally visible in the functional.

The positive-path example varies the combined path amplitude supplied to the
interferometer.  It does not by itself distinguish whether that amplitude came
from boundary state, orbit/reference measure or another generator factor.
Accordingly it supports generator nonselection only at the combined-envelope
level.  A separate necessity claim for `nu` versus `rho_boundary` would need an
intervention holding the other factor fixed under a declared normalization
convention.

## 5. Factorization gauge

The two source factorizations are exact:

```text
(+1/sqrt2,+1/sqrt2) * (+1,+1)
(+1/sqrt2,-1/sqrt2) * (+1,-1)
```

and both products equal `(+1/sqrt2,+1/sqrt2)`.  Every branch amplitude and
observable is therefore unchanged.  This is representation gauge, not two
physical generators.  The repaired theorem classifies it correctly.

This example also explains why generator fields cannot be inferred separately
from `D` without conventions or independent interventions: `D` determines the
combined amplitudes only up to factorization redundancies and, more generally,
up to branch-space unitary representations.

## 6. Causal diagonal `D_n` family

The integrated D17 equal tower has two positive cylinders at every depth:

```text
depth 1: 0,1
depth 2: 00,10
depth 3: 000,101
later:  append one deterministic 0.
```

At each depth D18 constructs the diagonal functional

```text
D_n = diag(1/2,1/2)
```

in that depth's ordered cylinder basis.  It is Hermitian, normalized and
strongly positive for all complex coefficient vectors.  Prefix restriction is
block coarse graining; each parent has one child of equal mass, so

```math
D_n = M D_(n+1) M^dagger.
```

I independently iterated and restricted this family through depth 100.  Every
identity held.  The two positive-past conditionals are:

```text
P(101)/P(10) = 1,
P(000)/P(00) = 1.
```

Equivalently, with current visible bit `y=0`, the next `z` is one on the
`x=1` past and zero on the `x=0` past.  Both follow from the same projective
family; no second click probability is multiplied.

Source check 18 verifies normalization and Hermiticity but not strong
positivity explicitly.  Positivity nevertheless follows immediately from the
nonnegative diagonal entries.  Freezing that predicate would improve receipt
precision without changing the result.

## 7. Operational sufficiency versus minimality

For a finite typed event algebra, `(E,D)` is sufficient to:

- evaluate `D(A,B)` by finite additivity;
- decide exact decoherence of a declared partition;
- read probabilities once on a decoherent partition;
- condition on positive-probability events.

Record instruments and units are not additional probability inputs after
their effects are encoded in `D`.  They remain necessary in the explanatory
generator and interpretation layers.  This layer separation repairs the
round-one contradiction.

It does not prove that the literal matrix `D` is a unique minimal operational
representation.  On a two-history algebra, consider

```text
D+ = [[1/2, +i/4],[-i/4,1/2]],
D- = [[1/2, -i/4],[+i/4,1/2]].
```

Both are Hermitian, normalized and strongly positive, with eigenvalues
`1/4,3/4`.  They are distinct, but every subset quantum measure is identical:

```text
mu(empty)=0, mu({0})=1/2, mu({1})=1/2, mu({0,1})=1.
```

Their exact decoherent partitions are also identical: the trivial one-block
partition decoheres, while the singleton partition does not.  Consequently
all licensed classical probabilities on this Boolean algebra agree.

Therefore a genuine minimality theorem needs either:

1. an operational equivalence quotient on decoherence functionals; or
2. an enlarged class of phase-sensitive interventions/questions that
   distinguishes such imaginary coherences.

Even `E` is partly definitional: it is the domain/type of `D`, not a field that
can be deleted while leaving the same function well formed.  The source check
24 establishes typing necessity, not an intervention-based irreducibility
theorem.

The manuscript is safe because it claims finite **sufficiency** and explicitly
withholds `MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK`.  Continue to avoid using
“minimal” for more than the proposed layer decomposition.

## 8. Units and dimensional interpretation

The exact unit controls correctly show:

```text
dimensionless record probability unchanged,
reported length changes from 3 to 6 metres,
reported numerical G changes under the supplied scale convention.
```

This establishes that a units/scale dictionary is not part of the
dimensionless probability core but is required to report metres, seconds and
dimensional couplings.  It does not recover nature's metre, second or `G` from
the history functional.

## 9. Finding ledger

```text
R2-1 PASS     D0, DR, D1 and the tilted functional reproduce exactly.
R2-2 PASS     All 15 coarse partitions preserve the functional axioms; exact
              decoherence classification is 4/15 for D0 and 15/15 for DR.
R2-3 PASS     The causal diagonal D_n family restricts projectively and gives
              both conditionals without a second lottery.
R2-4 PASS     State and record-instrument interventions change predictions;
              sign-moving factorization is correctly treated as gauge.
R2-5 MODERATE The full generator's state versus reference-measure necessity is
              not separately identified by the tilted combined envelope.
R2-6 MAJOR    No literal minimality/uniqueness theorem for `(E,D)` follows;
              distinct D can be operationally equivalent on the declared
              Boolean event questions. The manuscript correctly withholds it.
R2-7 MINOR    General Gram positivity and diagonal D_n positivity are true by
              construction but stronger than their frozen executable
              predicates.
```

## 10. Decision and scope

**PASS `FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY` at finite/cylinder scope.**
The operational/generator/interpretation split, interferometer functional,
all-partition closure, causal restrictions, conditionals, interventions and
factorization-gauge classification survive independent reconstruction.

Do not promote this to `MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK` or unique
physical selection.  The generator, record interpretation, units, alternate
construction filtrations and quantum sigma-algebra extension remain supplied
or open.  No cone, dimension, scale or gravity holdout is licensed.
