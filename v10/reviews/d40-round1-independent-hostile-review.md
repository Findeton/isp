# D40 round-one independent hostile review

**Verdict:** `0 BLOCKERS / 1 MAJOR / 3 MINOR / 1 NIT`.  
**Frozen theorem commit:** `d11ba91ec987e4998ad623f6514216f7dfd53039`.  
**Reviewed source:** `code/d40_action_cocycle_level_audit_exact.py`, SHA-256
`3930ae7abd704763767ececcf2b0de8e4ad5926143211e981e90d389cb88b9d5`.  
**Reviewed stdout:** `data/d40_action_cocycle_level_audit_exact.out`, SHA-256
`7f00c92019765086089c2f9a5aa1f22d3a52076c124c77228e1d99466bac464a`.  
**Date:** 2026-07-15.

Paper 29 remains held.  The central level distinction is promising and the
finite Bell/descent results survive, but R5 currently crosses two probability
spaces at the point where the paper's headline would be read.

## 1. Reproduction and clean calculations

The frozen source exits zero and reproduces the committed stdout byte-for-byte
under `PYTHONHASHSEED=7` and `83`.  Both runs have complete-output SHA-256

```text
7f00c92019765086089c2f9a5aa1f22d3a52076c124c77228e1d99466bac464a.
```

I independently re-derived the displayed arithmetic:

```text
projected relevant-event products:
  (1/3)(1/6)  = 1/18,
  (1/6)(4/11) = 2/33,
  1/18 + 2/33 = 23/198;

complete first-two-global-event products:
  (2/8)(1/8)  = 1/32,
  (1/8)(2/12) = 1/48,
  1/32 + 1/48 = 5/96.
```

The source-level event rows confirm that A's idle and B's birth retain the
same two record identities, same parents, same final authenticated store and
same sorted typed causal-DAG atom in either serialization.  The Bell
correlators are `(+r,+r,+r,-r)` with `r=1/sqrt(2)`, hence
`CHSH=4r=2sqrt(2)`.  At `x=1,a=+1`, the two Bob-setting conditionals are
`1/2+sqrt(2)/4` and `1/2-sqrt(2)/4`.

R1's core identity is also correct: for a positive four-atom measure,

```text
P(A=a) P(B=b | A=a) = mu(a,b) = P(B=b) P(A=a | B=b).
```

Finite coarse sufficiency is exactly constancy of the pushed next law on each
coarse fibre.

## 2. MAJOR — R5 substitutes the global-event pushforward for the star-law pushforward

R5 first computes the Paper 28 object: the projected first-relevant-event
star kernel, whose two serial products are `1/18` and `2/33`.  It then switches
to a different object: D39b's complete first-two-global-event embedded jump
chain, whose products are `1/32` and `1/48`.  The printed `5/96` is the typed-
DAG pushforward mass of the second object only.

Those comparisons are both useful, but they are not interchangeable.  The
direct pushforward of the Paper 28 serialized star law assigns the common
unordered projected atom

```text
1/18 + 2/33 = 23/198,
```

not `5/96`.  Silent omitted events explain why the star's first-relevant-event
law and the complete first-two-global-event law have different denominators.
Consequently the frozen receipt has not yet printed the pushforward that
directly adjudicates its own `1/18 != 2/33` headline.

The expected repair is small and likely strengthens the result:

1. type `STAR_RELEVANT_SERIAL`, `STAR_UNORDERED_ACTION_ATOM`,
   `GLOBAL_SERIAL_EVENT` and `GLOBAL_TYPED_DAG_ATOM` separately;
2. gate the star pushforward at `23/198`;
3. retain the global control at `5/96`;
4. state that unequal serialization weights are legitimate in both objects
   because the declared unordered atom receives their sum;
5. keep Paper 28's flat-action-variety nonmembership unchanged.

Until that delta is frozen, `PRIMARY=LEVEL_MISMATCH...` is plausible but not
receipt-complete at the exact probability space that generated the headline.

## 3. MINOR — fixed-depth embedded jump law is not a full Harris/projective theorem

`push_path_law(packet, typed=True)` is the registered depth-two embedded jump
law.  It is normalized and exact.  It is not, by this receipt alone, a timed
Harris-cylinder measure, an arbitrary-down-set projective family or an
infinite typed-DAG completion.  Replace unqualified “the actual typed-DAG law”
with “the registered depth-two embedded-jump typed-DAG pushforward” and carry
the stationary/infinite/timed questions as open.

## 4. MINOR — Bell Gram positivity is constructed but the gate label is under-explained

The Bell branches are explicit vectors and `gram(...)` therefore constructs a
positive semidefinite matrix algebraically.  The numeric `Gram_forms=4/4`
counter, however, checks only `G=G^T`.  The theorem is sound by construction,
but the receipt should print the load-bearing identity

```text
c^T G c = || sum_i c_i v_i ||^2 >= 0
```

and distinguish that algebraic proof from the symmetry counter.  An exact
finite principal-minor or rational-coefficient quadratic-form control would
make the printed gate self-auditing.

## 5. MINOR — R9 is a typed claim ledger, not an independent universality theorem

R9 checks that twelve manually entered rows have unique labels and the
expected class counts.  It does not derive those labels from antecedent
theorems.  That is useful claim-discipline, but Paper 29 must call it a
row-by-row corpus classification and argue each placement in prose.  The
receipt alone proves schema completeness, not universality of any row.

## 6. NIT — exact-number rendering

The second erased-setting conditional prints as
`1/2+-1/4*sqrt2`.  Render it as `1/2-1/4*sqrt2`.  The exact value is correct.

## 7. Surviving theorem surface

The following survive this round unchanged:

- the refined classical cylinder identity and finite fibre-sufficiency iff;
- the D34c disjoint-support operator/functional interchange and shared-
  support negative control;
- the two durable decoherent-record click-square families;
- the interference versus orthogonal path-record discriminator;
- the fact that Paper 28's action-variety nonmembership is not a probability-
  law inconsistency;
- the general positive h-ratio classification of K-flat's shape, with no Born
  uniqueness;
- exact Bell `CHSH=2sqrt(2)`, no-signalling and setting-boundary failure;
- the unresolved D15 state/instrument/grammar/clock dictionary;
- the conditional D26 `4/5` BORN visibility handoff.

The major is an object-typing repair, not a refutation of the proposed paper.
A focused D40b delta can close it before Paper 29 authorship.

