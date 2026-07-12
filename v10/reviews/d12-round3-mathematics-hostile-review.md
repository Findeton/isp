# D12 focused hostile round-3 mathematics closure review

**Date:** 2026-07-11  
**Verdict:** **PASS / MATHEMATICS CLOSED AT THE STATED `A_D12` SCOPE**  
**New fatal or major opening:** none  
**Round-2 residuals:** closed, subject only to one editorial support-domain clarification

## Decision first

The frozen 142-check repair closes the mathematical openings left after round
two.  The quantum packet no longer mislabels atomwise extended log densities as
finite contrast coefficients; it records finite coordinates only on each
law's positive support.  Paper 13 now displays and proves the arbitrary-prefix
`P_r` family.  That process has an explicit finite collar state, its local
exponential races reproduce every cylinder probability, and the construction
gauge is extended from the exact `AB/BA` generator to arbitrary finite
disjoint schedules by the standard adjacent-swap theorem for linear
extensions.  The final theorem remains expressly limited to the shared
finite-packet, unitary-frame principles actually implemented.

No surviving issue changes a probability, defeats projectivity, invalidates
the countermodel pair, or enlarges Theorem 3 beyond its evidence.  D12's
`UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS` verdict is mathematically licensed at
that stated scope.  It is still not a derivation of the process of our universe,
and the paper now says so.

## Frozen artifacts and independent reproduction

```text
12ca4f04b65351158bdcb9eda3e455baa73340c077cbb604cf1c9582a555e0a6  code/d12_multidiamond_history_exact.py
39b42a4af1ab48a2059c18096fb616094583cce4ea26cde2c2e1664a1a741f9f  relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

The replacement executable was run under normal and optimized Python.  The
outputs were byte-identical and matched the frozen receipt:

```text
checks                  = 142
stdout SHA-256 normal   = 96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
stdout SHA-256 -O       = 96df7ed44360c980f9bafbf5e86a792241d774a8995c2303bc3bbf47c8ed6e78
semantic receipt        = 47b5aecd660370264c2e5c377493b70a9e7371880168f2b3f9f04fed936af5ba
```

All audited probability and matrix calculations remain exact in rational
arithmetic or `Q(sqrt(2),i)`.

## 1. Positive-support RN coordinates

**Verdict: closed.**

The previous field of extended atomwise values has been replaced by

```text
positive_history_support
log_rn_coordinates_on_support
```

For quarter-iSWAP the positive support is `{1,2}`.  Restricted to that support,
both the Born law and the normalized restriction of the ambient uniform
reference are `(1/2,1/2)`.  The log-RN function is therefore constant, so its
coordinate modulo constants is the single value `0`, exactly as stored.

For half-iSWAP the positive support is the singleton `{2}`.  Its probability
simplex modulo normalization has dimension zero, so the correct coordinate
tuple is empty.  The check

```text
len(h_support) = |support| - 1
```

is therefore correct for both packets.  The supports differ because the
physical interactions give different zero-probability outcomes; the ambient
pointer atoms, reference, ledger, screens, types, grammar, evidence data, and
commitment data remain shared.  This is exactly the intended nonselection
witness.

The finite V6 log-RN reconstruction applies on the positive support, not across
ambient Born-zero atoms.  One editorial sentence should say explicitly that
`h_D` in the restored tuple is support-relative whenever the ambient history
law has zeros.  The code is now correct; this is only a domain clarification in
Paper 13 sections 3–4.

## 2. Arbitrary-`n` `P_r` process

**Verdict: closed.**

Paper 13 now defines, for `n=3q+s`, `s in {0,1,2}`,

$$
P_r^{(n)}(x_1,\ldots,x_n)=
\left[\prod_{j=0}^{q-1}
\frac{1+r x_{3j+1}x_{3j+2}x_{3j+3}}8\right]2^{-s}.
$$

For rational `|r|<1` every cylinder atom is strictly positive.  Normalization
factorizes blockwise.  The last-coordinate pushforward has only three cases:

1. at block phase 0, summing a new fair sign removes a factor `1/2`;
2. at phase 1, the same operation removes the second fair factor;
3. at phase 2, summing the third sign cancels the triple term and leaves the
   uniform two-sign marginal `1/4`.

Hence

$$
(\pi_{n+1,n})_*P_r^{(n+1)}=P_r^{(n)}
$$

for every `n`, not merely through the nine executable levels.  The compatible
finite discrete cylinders therefore define the intended infinite history
measure.  Its one- and two-coordinate marginals are uniform, while every third
conditional depends on the previous two signs when `r != 0`; the process is
not first-order Markov.  The `r=1/2` and `r=1/3` measures are genuinely
different.

The executable's depth-9 enumeration covers all three phase cases repeatedly
for both parameters.  The formula and case proof carry the result to arbitrary
depth.

## 3. Finite-memory collar realization

**Verdict: closed.**

The classical collar stores only

```text
block_phase in {0,1,2}
block_memory of length 0, 1, or 2
```

and advances by

```text
phase 0: remember the new sign
phase 1: remember the second sign
phase 2: clear memory and return to phase 0
```

There are only `1 + 2 + 4 = 7` phase/memory states.  At phases 0 and 1 the
next-sign law is fair; at phase 2, stored signs `x,y` give

$$
p(z\mid x,y)=\frac{1+rxyz}{2}.
$$

Thus the live interface does not copy the unbounded sealed past.  Immutable
records retain that past, while the continuing process needs only two signs of
current-block memory.  The recursive `classical_tower` actually advances this
collar; the finite state is not reconstructed from full history during normal
generation.  `finite_collar_from_prefix` is used only as an exhaustive audit
oracle.

The code verifies through depth 9 that the finite-collar conditional equals the
closed-form block conditional for every prefix.  The three-state cycle proves
the equality for all depths.

## 4. All-level exponential-threshold representation

**Verdict: closed.**

For every positive prefix, the two race rates are set equal to its supplied
conditional masses.  Since the rates sum to one and are strictly positive for
`|r|<1`, independent exponential clocks choose outcome `e` with

$$
\frac{\lambda_e}{\lambda_{-1}+\lambda_{+1}}=p(e\mid H).
$$

Multiplying the winner probabilities along a prefix gives the chain-rule
product.  The executable compares that product with `P_r^(n)` for every atom at
every level through depth 9, for both `r=1/2` and `r=1/3`.  The finite-collar
phase rule and arbitrary-`n` factorization prove the equality beyond the
enumerated levels.

Architecture E is therefore an implementation of the already supplied class-C
measure.  It does not add or select a different law.  The earlier first-block
only bug is absent.

## 5. Finite-poset construction gauge

**Verdict: closed at the declared disjoint-schedule scope.**

The exact program supplies the generating calculation:

```text
AB law = BA law
canonical marked-outcome fibers have equal weight
one canonical pushforward normalizes without double counting
same-collar overlap does not commute and can change a record probability
```

Paper 13 now supplies the general lemma.  Any two linear extensions of a finite
partial order are connected by a sequence of adjacent swaps of incomparable
elements.  Under `A_D12`, incomparable operations admitted to the construction
quotient are disjoint, so their instrument maps commute and one adjacent swap
preserves the marked canonical history and its weight.  Induction along the
swap sequence proves presentation independence for every finite disjoint
schedule.  Operations sharing a collar are excluded from this equivalence and
retain physical order, as the overlap control demonstrates.

The hypothesis matters: incomparability alone would not imply tensor
disjointness in an arbitrary model.  Here disjoint ownership is part of the
packet rule and the theorem's stated scope.  The paper does not export the
lemma to arbitrary process networks without that hypothesis.

## 6. Final Theorem 3 scope

**Verdict: closed and logically valid.**

The theorem quantifies over `A_D12`, not all conceivable SHARD models.  Its
premises are enumerated: common finite ambient atoms and contrasts, positive
reference, fixed evidence/commitment data, connected two-owner collar,
typed eligibility, complete Born pointer, immutable record/output birth,
projective prefix continuation, the disjoint construction quotient with
overlap retained, and independent unitary vertex-frame transport.

Quarter- and half-iSWAP are separately constructed under the same carrier,
grammar, pointer, and audit functions.  Both continue at arbitrary depth and
pass the stated unitary-frame/projective gates.  They assign the same durable
record probability `1/2` and `0`, respectively.  Therefore `A_D12` cannot entail
a unique interaction coupling or induced history measure.  This is the direct
two-model criterion and contains no statistical inference.

The theorem correctly delegates extension-grammar nonselection to D7, does not
claim nonunitary Lorentz-frame integration, and does not claim a
universe-specific field theory.  The independent all-level classical twins
show separately that projective non-Markov completeness does not choose a
measure.  These two counterexample layers support, rather than conflate, the
final conclusion.

## Closure ledger

```text
R2-1 arbitrary-n P_r formula/proof                 CLOSED
R2-2 positive-support finite RN coordinates         CLOSED
R2-3 finite-poset adjacent-swap construction lemma  CLOSED AT DISJOINT SCOPE
R2-4 packet-specific continuation scope             CLOSED BY EXPLICIT SCOPE
R2-5 stale collar as constructor invariant          CLOSED IN PAPER/API

new fatal opening                                    NONE
new major mathematical opening                      NONE
editorial clarification                              h_D IS SUPPORT-RELATIVE WHEN AMBIENT BORN ZEROS OCCUR
```

## Final assessment

The result that survives is precise and worthwhile:

> Given a typed finite packet architecture and a supplied compatible
> whole-history process, next-record probabilities are its positive-cylinder
> conditionals.  The audited structural, projective, construction-gauge,
> unitary-frame, evidence, and record principles do not uniquely select the
> interaction or process measure.

That statement is now supported by exact countermodels and an all-level
classical construction.  It does not recover the physical click law, metres,
seconds, gravity, bridge grammar, or the universe's couplings.  Paper 13 keeps
those objects primitive or empirical and refuses downstream geometry.

**Final verdict: PASS.**  Archive the mathematics as closed at the explicit
`A_D12` scope, with the single support-domain sentence added when convenient.
