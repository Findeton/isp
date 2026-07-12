# D21 round-1 mathematics hostile review

**Reviewer stance:** internal adversarial audit; no claim of external
independence.  **Verdict before repairs:** MINOR REVISION.

## Rebuild

The Gaussian-rational executable was read from definitions rather than from
the manuscript conclusions.  The density operators have the claimed
two-dimensional nonzero block

```math
{1\over2}\begin{pmatrix}1&eta\\eta&1\end{pmatrix}
```

with eigenvalues `(1+eta)/2` and `(1-eta)/2`.  The proper-reduction theorem is
correct: tracing any factor annihilates both off-diagonal terms.  The Pauli
word count is `4^3-3^3=37`.  Direct Pauli multiplication gives `XXX=eta`,
`XYY=YXY=YYX=-eta` and hence `M=4 eta`.

## Openings

1. The initial source was stated as a state but not as an interacting finite
   generator.  A source circuit is needed to support the “different rules”
   language.
2. A dephased density operator alone does not print Candidate C's objective
   selection variable or conditional branch states.
3. “Third record” can be misread as physical time although the three regions
   are spacelike and serial order is gauge.
4. Positivity is proved only for `0<=eta<=1`; no claim should be made outside
   this interval.
5. Complete finite conditioning does not imply a quantum sigma-algebra
   extension or a variable-carrier process.

## Disposition

Openings 1–3 were repaired in the executable and text: Q is reconstructed by
the Hadamard-plus-two-CNOT source circuit; C now prints both `1/2` source
weights and normalized branches; and the discriminator is described as joint
conditioning rather than causal temporal influence.  Openings 4–5 are stated
as scope boundaries.  The repaired exact count is `40/40`.

**Final round-1 mathematics verdict:** PASS at the fixed three-factor finite
instrument scope.

