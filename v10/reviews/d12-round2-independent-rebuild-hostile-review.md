# D12 hostile review, round 2: independent multi-diamond rebuild

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **PASS at the stated finite-packet, unitary-frame, primitive-process scope**

The replacement implementation genuinely repairs the round-1 one-cell
overclaims. It constructs immutable records and continuing collars, explicit
quantum towers through depth four, adjacent cylinder pushforwards, an
all-depth continuation induction, independently changed unitary endpoint
frames and stored links, canonical disjoint schedule fibers, overlap controls,
local eligibility refusals, two full interaction models, and an all-level
non-Markov classical cylinder family. Quarter- and half-iSWAP pass the same
declared packet gates and still predict `1/2` and `0` for one durable record.

During hostile reconstruction I found that the first repaired threshold test
initially covered only one three-record block. The finalized 137-check source
now uses block-relative conditionals and verifies threshold-product equality
for every cylinder through depth nine for both `r=1/2` and `r=1/3`. The
arbitrary-depth product formula closes the induction. That potential blocker
is therefore closed in the frozen source reviewed here.

The PASS is scoped. Connectedness is declared by the two-owner collar type,
not derived from a graph; the evidence clock and commitment coefficient are
shared primitive packet metadata rather than an executed opportunity process;
and frame integration is unitary. Paper 13 states those limitations and does
not claim empirical selection or a universe-specific law.

## 1. Reproduction and hashes

All four programs use only Python's standard library. I ran each normally and
with `python -O`, setting `PYTHONDONTWRITEBYTECODE=1`. Every pair was
byte-identical and every fixed check-count/semantic-receipt gate passed.

Final source hashes:

```text
6f55ab55476925b7474bc78866646a1bbf26609d8b36c11f8175d75fda39827b  v10/code/d12_restored_diamond_process_exact.py
e5a8a50ffe03459cf62ca5b5168fd48079c6309fb3ae7ac2d7310203c1669b1f  v10/code/d12_diamond_law_nonuniqueness_exact.py
34215f2605f68029e4bce59c9e471d8af5892269d6b4b0ee7ac0193f67fe55dc  v10/code/d12_symmetric_interaction_family_exact.py
228e34053549fcfbeb9cb894004195fe1d558241b470e58b888b6873cd29afe1  v10/code/d12_multidiamond_history_exact.py
db80a8cd1ff48d649eaf83154d7f53b2148f30dadb5ae7b2e1a4538cf934364b  v10/relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
2497f7878cf464bc54f6e505b548fcb09fb5c2abc6f76891f22f212dd96ea2e9  v10/data/d12-round1-repair-receipt.md
```

Complete stdout SHA-256 values under both normal and optimized execution:

```text
one-cell precursor       b3411c5f77498af0a70ba9ea3d3fb21ac80bc80be048863805eca180391f120a
42-check countermodels   ffaf1bb6bb8125ca4f4d08d048d8828f6c48b81eb5e99f14ba6b0b3f8621ff7d
18-check symmetric pair  a2da06a85371f83de4b22047f734747a988254cfce887039563b34161b3ba73f
137-check multidiamond   ef930e21338322c76c3581cbcaab0e6f8f95c370ccc9bb2a0a22e319f5031091
```

The multidiamond semantic receipt is:

```text
b8a0dd95bf1487860d981ae4d41782d155820d9fd5c5309c3167047fea219433
```

The retained 25-check executable now identifies itself as a replaced
one-cell precursor. It is no longer used to support multi-diamond claims.

## 2. Clean-room mathematical reconstruction

For `P_r(x,y,z)=(1+rxyz)/8`, summing over any sign cancels the triple term.
All one/two-record shadows are therefore uniform, while

$$
P_r(z=1\mid x,y)={1+rxy\over2}.
$$

At `x=y=1`, `r=1/2` and `r=1/3` give `3/4` and `2/3`. Dependence on `x` after
conditioning on `y` proves the first-order Markov refusal.

For the exchange interaction,

$$
U_\theta|01\rangle
=\cos\theta|01\rangle+i\sin\theta|10\rangle,
$$

so the later second-leg-1 probability is `cos^2(theta)`: exactly `1/2` at
`pi/4` and `0` at `pi/2`. Both gates are unitary, exchange symmetric,
excitation preserving, entangling on `|++>`, and compatible with the same
declared collars, screens, pointer, evidence tag, and commitment tag. The
nonselection theorem follows independently of implementation detail.

## 3. Explicit records, collars, and local refusal

`DiamondPacket` now contains its interaction, one-diamond history law,
positive reference, complete three-contrast ledger, screens, order unit,
eventless flag, input/output types, evidence tag, and commitment tag.

Every positive firing constructs:

- an immutable `DurableRecord` with owners, input/output collars, endpoint
  frames, transported interaction, output effect, conditional mass, and
  nonterminal status; and
- a normalized `Collar` with state, frame, order unit, transformed screen,
  parent record, emitted `INTERACT` opportunity, and continuing two-leg type.

The next firing consumes that emitted collar. Wrong type, wrong owner arity,
missing opportunity, stale input, and nonnormalized input are refused locally.
Earlier record tuples persist byte-for-byte and their values repeat-read from
every later prefix.

“Connected” here is a declared property of the single owned two-leg collar.
The refusal does not derive physical connectedness from an incidence graph,
and Paper 13 does not generalize it to arbitrary bridge discovery.

## 4. Quantum projective tower and continuation

The quarter-iSWAP tower has `1,2,4,8,16` positive histories at depths zero
through four. Each level normalizes. For every adjacent pair, deleting the
last record and summing fine masses reproduces the exact coarse cylinder law.
Every positive prefix through depth three has the nontrivial next law
`(1/2,1/2)`.

The all-depth induction uses three facts: the interaction is unitary, the
four pointer effects sum to identity, and each branch emits the same normalized
two-leg type. For these two packet matrices, pointer projection also preserves
the branch-mass/state class accepted by the exact normalizer. Thus the finite
tower is a carrier for a valid arbitrary-depth repeated-diamond process, not
the old integer-only continuation check.

Quarter- and half-iSWAP are independently passed through the same model audit.
They agree on all declared structure while their depth-one durable probability
differs by `1/2` versus `0`.

## 5. Vertex frames and transported history

The generated endpoint sequence is

```text
I, H⊗I, I⊗H, H⊗H, SWAP.
```

At step `n`, the stored link is

$$
F_{n+1}U F_n^\dagger.
$$

States and pointer screens are transported at each endpoint. At every depth,
the complete framed cylinder law equals the root-frame law, final collar states
equal transported baseline states, and durable records contain the expected
lower/upper frame names and links.

This is a genuine multi-endpoint unitary gauge test. Full nonunitary
`SL(2,C)` history integration remains open and is explicitly excluded in the
paper.

## 6. Construction fibers and overlap

For two disjoint diamonds, `AB` and `BA` schedules produce the same complete
16-outcome law. Canonical keys retain labeled outcomes but omit auxiliary
order. Duplicate presentations have equal mass and are stored only once; the
canonical physical law sums to one rather than two.

For overlapping same-collar operations, the executable verifies
noncommutation and finds an input/pointer outcome whose probability changes
with order for both packets. This repairs the prior bare-commutator receipt and
correctly keeps physical overlap order.

## 7. All-level classical process and threshold equivalence

The arbitrary-depth cylinder family is a product of independent three-record
blocks:

$$
P_r^{(n)}
=\prod_k {1+r x_{3k+1}x_{3k+2}x_{3k+3}\over8}
\times 2^{-(n\bmod3)}.
$$

Production verifies normalization, all adjacent prefix maps, and conditional
disintegration through depth nine for both `r=1/2` and `r=1/3`. The formula
proves the same at arbitrary depth.

The finalized threshold representation uses the same block-relative
conditionals as rates. It tests a block-boundary prefix `(1,1,-1)` and verifies
for every cylinder through depth nine that the product of threshold winner
probabilities equals `P_r^(n)`, for both `r` values. Independent exponential
races choose an outcome with `lambda_e/sum(lambda)`, so this is an exact
representation of class C rather than a new law.

## 8. Opening ledger after hostile rebuild

| Potential opening | Finding | Status |
|---|---|---|
| old one-cell continuation | replaced by explicit depth-four histories and all-depth induction | closed |
| one pointer deletion called projectivity | every adjacent quantum pushforward through depth four plus induction | closed |
| one global frame | five independently assigned unitary endpoints with stored transported links/screens/states | closed at unitary scope |
| bare disjoint commutator | canonical AB/BA fibers, invariant weights, normalization, and overlap probability control | closed |
| seal/birth metadata only | immutable records and continuing collars are constructed and consumed | closed |
| detached non-Markov API | explicit classical records/collars plus all-level block cylinders | closed |
| deterministic disintegration | every positive quantum prefix has `(1/2,1/2)` | closed |
| architecture E only first block | all-level block-relative rates checked through depth nine and proved by product formula | closed in finalized source |
| owner connectivity | primitive two-owner collar typing, not a derived connectivity theorem | scope limitation disclosed |
| evidence/commitment strings | shared supplied metadata; separate scalar receipts, not integrated opportunity selection | scope limitation disclosed |
| both packet models | same constructor/audit, different durable prediction | closed |
| full nonunitary frame gauge | explicitly open | not claimed |

No remaining issue invalidates the stated underdetermination result or the
finite-packet universal-form witness.

## 9. Paper and receipt audit

The final repaired numbers match production:

```text
checks=137
depth=4
depth4_histories=16
quarter/half durable probability=1/2 versus 0
semantic receipt=b8a0dd95...
```

Paper 13 now says the implementation works at the stated unitary-frame scope,
keeps full nonunitary integration and local computability as additional gates,
separates grammar support from measure support, distinguishes decoherent
histories from process-tensor tomography, refuses geometry before selection,
and reserves empirical claims about nature.

The architecture census is now supported: A remains D11's dying negative
control; B is the previously supplied conditional SCIR packet; C is the
all-level `P_r` process; D is represented by the explicit repeated projector-
history quantum towers; and E is equivalent to C under the repaired threshold
construction. The census does not select one class as physical.

## 10. Final determination

The independently supported theorem is:

$$
\boxed{
\text{the repaired shared diamond/record constraints admit at least two}
\text{ continuing exact process models with different durable predictions.}
}
$$

Consequently those constraints do not uniquely derive the primitive process,
interaction angle, grammar, or universe-specific measure. D12 supplies a
working conditional universal form and a nonuniqueness theorem, not the real
law of nature.

**Round-2 independent-rebuild verdict: PASS.**
