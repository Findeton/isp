# Paper 23c review — Seat P (probability/instrument)

Date: 2026-08-22

Disposition: **ACCEPT-WITH-FIXES** (one MAJOR, one MODERATE)

Blind delta review of the #325/#326 construction
(`7e90aba64c4abf5585d409f8d9696c76e0308007da3f81607e8e187cf709f126`,
235 LF) against frozen pin `d50dc41c…` and 13D `3b91766f…`. Seat lens:
probability kernels, seed law, exactness of every quantitative claim.

## Findings

**F-P1 (MAJOR). Lemma C's "independent reversal" claim overreaches for
the bond field at unequal colors.** The lemma asserts invariance under
"independent reversal of the two hypothetical ranks". The bond kernel
$\ell_{ij}$ depends on $v_{ij}$ and on color *equality* only, so
rank-permutation invariance holds — but "independent reversal" as a
statement about joint laws of hypothetical rank variables is vacuous:
the ranks are not $\Gamma_D$ variables at all. As phrased, the lemma
proves invariance of a law that has no referent in the construction.
*Required repair:* restate Lemma C as invariance of the complete
physical-field law (packets, colors, records, bonds) under all carrier
relabelings — dropping "or independent reversal of the two hypothetical
ranks" — and carry the coupling argument in Proposition D where it
belongs; there the two couplings are genuinely different laws *of a
decoration*, and their common pushforward onto $\Gamma_D$ fields is
exactly Lemma C's content.

**F-P2 (MODERATE). The §2/§6 exactness claims are asserted as verified
but the verification is not part of the artifact.** The exhaustive
transposition check ($n=2,\dots,5$) and the $0$ vs $1/6$ densities are
correct (recomputed independently with `fractions.Fraction` under
`python3.13`: P(all-flat cell, n=3) $=\frac{2}{125}$
$=2^{1-3}(10/25)^{\binom32}$ confirmed), but the paper cites them as
bare assertions. Since harnesses are audit scaffolding only, either
mark these two claims as "verified by audit computation, not part of
the constructed object", or replace the exhaustive claim by the
two-line general argument (a transposition-fixed total order is
impossible since it would contain both $x<y$ and $y<x$ — already given
in Prop A's proof, making the finite checks redundant). Prefer the
latter; keep the finite checks as scaffolding.

## What survived

All arithmetic that appears is exact and correct: the bond threshold
table $(16,9)$ matches 13D §6.3; marginal bond fairness
$\frac12\cdot\frac9{25}+\frac12\cdot\frac{16}{25}=\frac12$;
$\frac16$ from uniform-rank pattern counting; the grand-experiment
cardinality law untouched. The no-go does not depend on any
approximation or asymptotic argument — every obstruction is finite,
exact, and fixture-scoped. Control rows 1–10 PASS (control 3's
representative-independence verified through orbit-cell masses).
Outcome `P23C-ORIENTED-PAIR-NOT-DERIVABLE` earned modulo F-P1/F-P2;
neither is structural.
