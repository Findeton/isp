# Paper 13 Stage-B independent receipt verification

**Status:** VERIFIED. Stage B is independently green under the frozen Paper 13
construction pin. This is a construction-stage verification, not terminal
scientific adjudication.

**Verdict:** `ACCEPT-STAGE-B`

**Strict primary:**
`P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED`

## Frozen bytes

- HEAD: `389cfcf496272cfc37d13a1eca60b22bb9addbfd`
- evaluator source SHA-256:
  `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e`
- fresh-case file SHA-256:
  `2ac664c94a6b29c5b73fd8047e97a2e086ac45defc9c3431bc1ded66f011dd29`
- output SHA-256:
  `7f544c79f60d91c84e5805541313ec9d7ac068cdf0ee4f6184947cf44f43886f`
- receipt SHA-256:
  `83bd33028c81e9dd555a44e9e7721d5ace298d522e0c069409118bdbf51c6c48`
- fresh normalized-payload SHA-256:
  `5d0a3ee2ac368307064ed769bc3d3f514121662a6de759bf6776ec6189a6c1b7`
- receipt normalized-payload SHA-256:
  `622b21b914ab5056713fe61916b672f25c95cd9de33d045713619f581c1c00e8`

The three repository JSON artifacts (fresh, output, and receipt) parsed under
duplicate-key and no-float refusal, were byte-exact canonical JSON followed by
one newline, and their normalized self-hashes recomputed exactly. The private
verifier-result JSON is separately hash-authenticated and does not claim a
normalized self-hash. The evaluator was never imported or called by the
independent verifier, and neither `--generate-fresh` nor an official mode was
run.

## Independent verifier

- verifier:
  `/private/tmp/p13_stageB_receipt_verifier.py`
- verifier SHA-256:
  `779ea735ee226947b3159637f821e9494cf64021594aecb8d7c65538cd629385`
- result:
  `/private/tmp/p13_stageB_receipt_verifier_result.json`
- result SHA-256:
  `f954266a68b37c666678504b603b993f5f254dace9e1364bd5399555d062f1d3`
- independent checks: `346`
- first discrepancy: `null`

The verifier used its own exact `Fraction` arithmetic, SHAKE256 derivation,
matching-law construction, canonical serializer, matrix algebra, and seal
builder. It parsed the evaluator only as source text/AST to authenticate the
registered vocabulary and the single direct matching-call structure.

## Fresh derivation

Starting from the one externally supplied 32-byte nonce and the frozen source
digest, the verifier independently recomputed

```text
SHAKE256("P13-FRESH-v1" || raw_source_sha256 || raw_nonce).
```

It recovered exactly:

- seed SHA-256:
  `51b21dafdb978d85df48d34f2a8bccd70ce3cb872241f2d2225d93c3c7d6e65f`
- selected-block SHA-256:
  `cc07ecce3a2e9e7013867c30a45cd49d088edab390d96e78c750ffda3b365416`
- rerolls: `0`
- rejections: `0`
- size: `12`
- queries: `[1, 8, 9, 10]`
- challenge fixed pattern: `[false, false, false, true]`
- case SHA-256:
  `536fe43eb88137934cc76e12209db297ee5945554f411a49ff5f341a9ba31d61`
- blind-token SHA-256:
  `c107be3bf53d0ce31d44c3efe9c133ba0a03189a416069f3e6a0680291662751`
- peak cells: `37`
- peak target states: `1296`

The fresh payload, including its anchor-manifest hash, case hash, blind
projection, resource counts, permutation, exposure class, and normalized hash,
was byte-identical to the unique independent derivation. The nonce was not
rerolled, and the generator contains no fresh outputs.

## Full global matching-law reconstruction

The verifier independently enumerated every one of the `1296` complete target
coordinates for both size-12 members. It did not use the receipt's endpoint
table as its evaluator.

- COMMON: 16 nonzero endpoints; every queried marginal is `16/25`; endpoint
  SHA-256
  `cf790b31142cadd4f62d0133dd8f67d1f4fd45c25ad4397c2c9d3a9044f5eb65`.
- CHALLENGE: 2 nonzero endpoints; marginals are zero at queries `1`, `8`, and
  `9`, and `16/25` at query `10`; endpoint SHA-256
  `39df953f0a1818488a9bac3b2d710961fa5b494598151fbef786b98d4ef54d1d`.

Both laws normalize exactly. Their independently constructed physical
catalogues have identical blind projections: `37` cells, `48` incidences,
`24` roles, four ports and coins, identical schedules, support and degree
multisets, and blank prior-record laws. The source AST contains one direct
`gamma_evaluate` call in `measure_matching_case`; the receipt records one call
per member and two total.

## Exact scientific controls

The independent matrix reconstruction reproduced `R`, `B`, coherent `C`,
recorded `B^2`, and the unique native factor `K = C B^{-1}` exactly. The two
off-diagonal entries of `K` are `-176/175`, excluding a positive
source-independent restart kernel on the registered native cut. The interval
calculation independently gives `t(1/3)=7/25`, `t(1/2)=-7/25`, and

```text
|2t - 1/t| >= 527/175.
```

The positive history-conditioned joint remains normalized and nonnegative, so
the negative is correctly configuration- and cut-relative.

For the registered division, the verifier reconstructed all writer branches,
all 16 alternate-cut rows (including the spectator probe bit), `B^2`, the
36-state complete target catalogue, 32 retained zero coordinates, and the
three record projectors. Every registered continuation generator preserves the
record projector; the printed composition lemma extends this to every finite
licensed word. Active reuse exposes the exact inverse toggle.

The reciprocal chain independently gives

```text
00 -> 9/25
01 -> 0
10 -> 144/625
11 -> 256/625
```

with normalization one and the opposite-incidence counterfactual probe-one
probability zero.

## Receipt and outcome integrity

The verifier recomputed:

- the complete 14-row read set and every actual anchor hash;
- the source/fresh/output and canonical input-bundle bindings;
- all 12 claim rows, their gate hashes, falsifier links, and consumed
  arithmetic/type-DAG hashes;
- all 15 scope walls and all 8 orthogonal coordinates by exact two-way
  equality;
- all 92 source-registered mutation rows, with every row changed and killed,
  every evidence hash exact, and every supplied old/new primitive byte hash
  independently authenticated;
- all 178 seal entries and every coverage predicate.

The recomputed seal-manifest SHA-256 is
`63e4c0a5e63fa7d8923b972001a66dcb243e7199888706403f7c131556d157b5`.
The output is the exact canonical projection of the sealed receipt. All 12
eligible gates are true, the pre-registered earliest-outcome comparator selects
index 12, and the cap prevents either future law-selection rung from being
awarded.

The construction therefore passes Stage B exactly at its registered ceiling.
It remains `REPAIR-GREEN-UNREVIEWED`: the coupling, event grammar, division
doctrine, and actualization are still priced, typed-candidate, or postulated;
valuation, metric, curvature, continuum, GR, and QFT remain unconstructed.
Under the frozen pin, Stage C may now begin, but no terminal scientific claim is
citable before the later hostile panel and adjudication.
