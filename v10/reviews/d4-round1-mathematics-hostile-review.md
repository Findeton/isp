# D4 hostile round-1 mathematics / probability / profinite review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**  
**Core global-collapse theorem:** confirmed  
**Load-bearing repair:** completion-message minimality and its pooled-law census

## Frozen sources reviewed

- `v10/note-d4-no-silent-boundary-sufficiency.md`  
  SHA-256 `ff785c56b8c95dd9843e77b548951aedc9f8496f7938272de2ac73006ac8fdf9`
- `v10/relativistic-isp-v10-paper5-restriction-naturality-global-shock.md`  
  SHA-256 `5dde07f57a6b8098d6f464ee686457981448e0d0dd26f3c31ccaac770b181c6b`
- `v10/code/d4_boundary_sufficiency_exact.py`  
  SHA-256 `7c87e81f333d75814ec508023c7a21a01b0a25142415819288da3aaac1137481`

The receipt was run twice. Both runs reported 17/17 and had byte-identical
stdout SHA-256
`3a7ee070b7fc6a359cd33512cda4329055b4aaeab8ec2343121db2c4dcc7af8d`.

## Independent exact reconstruction

I rebuilt the finite system without importing the production executable. The
independent enumerator used ternary choices on each unordered pair rather
than the production code's directed-edge power set. It obtained

```text
labeled strict posets by level:       1, 1, 3, 19
down-set variables by level:          1, 2, 10, 98
total variables:                      111
normalization equations:              24
relabeling covariance equations:      611
induced-cut equations:                452
total equations:                      1087
coefficient rank:                     108
augmented rank:                       108
signed affine dimension:              3
proper-ideal pair certificates n<=4: 1304 / 1304
```

Thus the 111/1,087/rank-108/dimension-three report is not an artifact of the
production enumeration or elimination order.

## Theorem 3.1: confirmed

### The two-chain step

For `a<b`, restriction to the bottom point gives

$$
\kappa(\{a\})+\kappa(\{a,b\})=p,
$$

while restriction to the top gives

$$
\kappa(\{a,b\})=p.
$$

The bottom-only ideal is therefore zero by equality alone.

### The V-order transfer

For `a<c` and `b<c`, the fiber of the bottom-only ideal on the retained chain
`{a,c}` is exactly the pair of V-ideals `{a}` and `{a,b}`. The analogous
fiber on `{b,c}` is `{b}` and `{a,b}`. Naturality and the two-chain result give

$$
\kappa(\{a\})+\kappa(\{a,b\})=0,
\qquad
\kappa(\{b\})+\kappa(\{a,b\})=0.
$$

Signed charges can solve these by cancellation. Probabilities cannot:
nonnegativity forces all three terms to zero. Restricting the V to its two
minimal points then kills both singleton probabilities of the two-antichain.
This transfer is valid and positivity is genuinely load-bearing.

### The arbitrary proper-ideal step

Let `D` be proper and nonempty, choose `x in D` and `y notin D`. Downward
closure excludes `y<x`. Therefore the induced pair is either `x<y`, on which
`D` is the forbidden bottom singleton, or an antichain, on which it is a
forbidden singleton. The zero pair marginal is a sum of nonnegative full
probabilities and contains `kappa_P(D)`, so that term is zero. This applies to
every proper ideal; the independent 1,304-case census confirms the structural
step through four vertices.

Only empty and full remain. Their weights are `1-p_P,p_P`, and restriction to
one point makes `p_P` the same `p` for every nonempty `P`. The empty poset is
the harmless degenerate case where empty and full coincide.

The theorem therefore proves that the **positive** solution set is the
one-dimensional empty/full line segment even though the signed affine
relaxation has dimension three. The manuscript's correction of the failed
preregistered dimension-one expectation is mathematically honest.

## Major finding: predictive minimality is underspecified and the census pools laws

Proposition 5.1 says that two contexts may share a deterministic exact mark
exactly when their `q` vectors agree. That statement is true only after the
decoder's side information has been fixed. In the physical setup the decoder
already sees the retained unmarked structure `S=P|K`; and the proposition is
introduced **for a supplied law**, so the decoder normally also knows which
law is being used.

Formally, if an exact decoder has the form

$$
F_L(S,m(c))=q_c,
$$

then the forced equivalence is conditional: for fixed `L` and fixed `S`, two
contexts can share a message only if their `q` values agree. Message symbols
may be reused across different visible structures because `F_L` also receives
`S`. They may also be reused across different supplied laws if each law has
its own decoder. Conversely, if the intended decoder receives neither `S`
nor `L`, that stronger and physically different contract must be stated.

The executable confirms the ambiguity because it pools both D3 laws before
printing its class census. My independent reconstruction obtained

```text
                              classes (S,q)   max q's for one S
fixed law b=1                       564                  42
fixed law b=2                       601                  45
pooled union of both laws           756                  66
```

The reported `756` and `66` are therefore union diagnostics, not the minimal
message-state counts for either supplied law. Pooling is useful for showing
law relativity, but it cannot simultaneously certify fixed-law minimality
without saying that law identity is hidden from the decoder.

This affects a named proposition, the abstract's “coarsest” claim, and the
interpretation of two headline receipt numbers. It is why the review is
MAJOR REVISION even though the global-collapse and capacity results survive.

### Required repair M1

1. Specify the decoder signature and its free side information.
2. State minimality conditionally: for each fixed supplied law and fixed
   retained structure/outcome alphabet, the equivalence classes of equal `q`
   are the coarsest exact deterministic predictive partition.
3. Call the vector `q` a canonical representative of that partition, not a
   unique ontological or bit-minimal encoding.
4. Print and gate the per-law counts `564/42` and `601/45`; retain `756/66`
   only if explicitly labeled as the pooled union across both laws.
5. Amend the note, abstract, Proposition 5.1, and result discussion to use the
   same contract.

The exact-sufficiency identity itself is fine: normalized completion weights
are algebraically the direct pushforward. The fixed-cut law-relative witness
is also correct: the three-antichain inclusion probabilities are `1/2` and
`9/14`.

## Chain capacity: correct, with one contract sentence owed

On an `n`-chain, the `n+1` ideals are its prefixes. Retaining the minimal point
gives one omitting ideal and `n` including ideals, hence

$$
q_n(\mathrm{included})=\frac{n}{n+1}.
$$

These values are strictly increasing. All examples have the same retained
one-point structure and use the same fixed law, so the side-information issue
above cannot merge them. An exact deterministic message through depth `N`
needs at least `N` states, hence at least `ceil(log2 N)` fixed-length binary
bits. The 64-state/six-bit and nine-versus-eight checks are correct.

### Required repair C1

Add explicitly that the local decoder receives the retained state and the
fixed law but **not** construction depth, a global clock, or any other full
context except through the boundary mark. If depth is separately supplied,
the claimed lower bound on the *additional* mark is false. This is already the
intended retained-subsystem reading, but it must be part of the theorem's
formal premises.

The manuscript correctly limits the result to exact, deterministic,
uniformly bounded alphabets and does not overextend it to stochastic marks,
unbounded finite values, expanding boundaries, approximation, or other laws.

## Profinite claim: theorem correct; executable gate is weaker than its label

For every fixed positive integer `m`, `j!` is divisible by `m` once `j>=m`.
Thus `j! -> 0` in the standard profinite integers. Meanwhile

$$
\frac{j!}{j!+1}=1-\frac1{j!+1}\longrightarrow1,
$$

whereas the depth-zero value is `0`. Any continuous real-valued extension
would have to send the convergent sequence `j! -> 0` to a sequence converging
to its value at zero, which is impossible. The no-continuous-extension claim
is valid. The refusal to generalize this to every compact topology is also
correct; the one-point compactification is a legitimate counter-control.

However, PASS 16 checks only divisibility for `2<=j<=8`, `m<=j`, and that the
single value at `8!` is nonzero. It does not executable-check the printed
phrase “approaches 1.”

### Required repair P2

Either relabel PASS 16 as a finite residue shadow whose infinite conclusion
is supplied by the displayed analytic proof, or add exact checks of
`1-f(j!)=1/(j!+1)`, strict decrease over the audited sequence, and a printed
terminal error bound. Do not describe the present condition alone as an
executable convergence certificate.

## Other executable observations

- The duplicated declaration of `structural_to_messages` is harmless but
  should be removed.
- The 1,304-case “certificate” checks the structural pair-exposure step; the
  infinite zero-probability conclusion still rests on the analytic
  nonnegative-fiber argument. The paper currently supplies that argument, so
  no theorem gap results.
- The global-shock mixture is exactly restriction-natural and retains a free
  `p`. Calling it universe-global rather than local is correct.

## Adjudication

The following claim survives without qualification:

```text
All-induced-subset naturality collapses a nonnegative unmarked precursor
family to a free empty/full global-shock mixture. The D3 positive kernels lie
outside that class. For the fixed uniform chain law, exact deterministic
boundary sufficiency requires unboundedly many states when no depth side
channel is available. The standard profinite-integer topology does not make
n/(n+1) a continuous readout.
```

What does **not** yet survive is the manuscript's unconditional coarsest-mark
statement and the presentation of pooled `756/66` counts as support for a
fixed supplied-law minimality proposition. Land repairs M1, C1, and P2 before
round 2.
