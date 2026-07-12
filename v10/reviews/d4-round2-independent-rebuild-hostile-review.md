# D4 hostile review, round 2: independent rebuild and reproducibility

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **PASS — all round-1 repairs and the round-2 convex-certificate opening reproduce independently**

All requested round-1 repairs reproduce independently. During round 2, the
review found one further load-bearing gap in the proposed convex-cut
extension: an arbitrary inside/outside comparable pair need not itself be
convex. That opening was investigated before final acceptance. The paper now
uses a saturated chain's first boundary-crossing cover, or an incomparable
pair when available; the receipt now verifies a convex certificate for every
one of the 1,304 audited proper ideals. The independent rebuild reproduces
the split `616` cover-chain and `688` antichain certificates.

The final production receipt is deterministic, self-contained, and
numerically correct at every executed cutoff. The separate rebuild obtains
the same four cut-category ranks, positive stem and interval controls,
independent completion pushforwards, joint relabeling quotient, fixed-law and
pooled class counts, explicit chain messages, capacity escape models, and
factorial error shadow. No independent-rebuild blocker remains.

## 1. Frozen snapshot

```text
fb5d1c2ff71bc58b82a33a3a04140c0016242756ce070d7cfd36d5d4ff4d4c95  v10/note-d4-no-silent-boundary-sufficiency.md
3e6360c71592ca9a46df2914251fdf59976d24440a1f20333cb8754fe117dd4a  v10/code/d4_boundary_sufficiency_exact.py
e216c266f9402cce6a48ebd0d35c94dbcfe630fa5a275c9c7f38bb1bec0d5b93  v10/relativistic-isp-v10-paper5-restriction-naturality-global-shock.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d4_boundary_sufficiency_exact.py
```

Two clean executions exited zero and produced byte-identical stdout:

```text
f370625dc41046242fea6430e4362dddb66fdb54746b43da65d94c484534f2d1
```

The production executable reports **23/23 exact checks passed**.

The separate self-containment audit reports 4/4:

```text
PASS: all v10 investigation executables reside in v10/code
PASS: no duplicate investigation source exists outside v10/code
PASS: every investigation executable imports only the Python standard library
PASS: no .pyc cache artifact exists under v10
```

## 2. Independent implementation

The round-1 Ruby bitset/Rational reconstruction was extended rather than
replaced with calls into revised production code. It imports no production
module. Its final SHA-256 is:

```text
2df4f51941b29be7c5b60671f14237f23f7e6dbc524fdc16ea0b6e3deaad3beb
```

New round-2 reconstruction covers:

1. all induced, convex, ancestor-closed stem, and causal-interval cut sets;
2. a fresh exact linear system and sparse rank for each cut category;
3. the minimal-layer stem law and component-mixture interval law;
4. convex and nonconvex proper-ideal pair certificates;
5. direct full-weight normalization and projection separate from completion
   aggregation;
6. joint canonicalization of retained relation and probability vector;
7. fixed-law as well as pooled labeled/canonical counts;
8. explicit prefix ideals through 64-chain depth;
9. stochastic, distributed, unbounded-value, and approximate controls; and
10. factorial residues, error monotonicity, and the exact terminal identity.

Independent output:

```text
POSETS [1, 1, 3, 19, 219]
LINEAR variables=111 equations=1087 rank=108 augmented=108 affine=3
LINEAR shock_line=true
CUT all=[111,1087,108,108,3]
CUT convex=[111,1069,108,108,3]
CUT stem=[111,939,103,103,8]
CUT interval=[111,985,103,103,8]
PROOF affine_consequences chain=true vee=true,true
PROOF proper_ideals=1304/1304
PROOF pair_types={antichain:652,chain:652}
PROOF convex_proper_ideals=1304/1304
PROOF convex_pair_types={antichain:688,chain:616}
PROOF nonconvex_candidate_contexts=516
SHOCK natural=true cuts=3671
CUT stem_witness natural=true cases=1789 all_failure=true
CUT interval_witness natural=true cases=2210 convex_failure=true
MESSAGE exact=true contexts=7342
MESSAGE pooled_labeled=756/66 pooled_canonical=199/42
MESSAGE perlaw_labeled=[564,601]/[42,45]
MESSAGE perlaw_canonical=[144,168]/[30,36]
MESSAGE witness=1/2,9/14
CAPACITY states=64 bits=6 first=1/2 last=64/65
CAPACITY flag_collision=true values=2/3,3/4
CAPACITY alternatives stochastic=true distributed=true unbounded=true approximate=true
PROFINITE residue=true factorial_diagonal=true errors_decrease=true
PROFINITE identity8=true terminal=1/40321
```

Every finite theorem check uses integers or exact rationals.

## 3. Four cut categories — finite classifications pass

The independently rebuilt signed systems through three vertices give:

| cut category | variables | equations | rank | augmented rank | affine dimension |
|---|---:|---:|---:|---:|---:|
| all induced subsets | 111 | 1,087 | 108 | 108 | 3 |
| convex subsets | 111 | 1,069 | 108 | 108 | 3 |
| ancestor-closed stems | 111 | 939 | 103 | 103 | 8 |
| causal intervals | 111 | 985 | 103 | 103 | 8 |

Thus every reported finite rank is correct. The signed dimensions are not
mistaken for probability-face dimensions.

### Stem witness — pass

For every ancestor-closed retained set `K`, independently reconstructed
minimal layers satisfy

$$
Min(P)\cap K=Min(P|K).
$$

The deterministic law selecting `Min(P)` passes all 1,789 audited stem cuts
through four vertices. It fails the top-only cut of the two-chain, which is
not ancestor closed. This is a valid positive witness that stem-only
naturality does not force the all-subset collapse.

### Interval witness — pass

Independently selecting each comparability component with Bernoulli parameter
`2/5` passes all 2,210 registered interval cuts. Empty, full, singleton, and
closed comparable-endpoint intervals match the recomputed component law.

The law fails the convex cut retaining the two minima of a `V`: the parent
puts them in one perfectly correlated component, while the retained
antichain recomputation gives two independent components. This correctly
separates interval from convex naturality.

### Collar-complete and typed-carrier cuts — correctly refused

The revised paper does not pretend that an unmarked vertex subset contains
collars, screens, or typed carriers. Those categories remain conditional on a
future marked construction. No executable result silently classifies them.

## 4. Convex all-size promotion — opening repaired and passed

The initial round-2 draft checked only the small point/chain/`V` cells. The
hostile opening was that an arbitrary comparable inside/outside pair can omit
intermediate vertices and therefore fail convexity. The final paper now adds
the missing all-size lemma.

For a proper ideal `D`, an incomparable inside/outside pair is convex
vacuously. If `x in D`, `y outside D`, and `x<y`, follow a saturated chain
from `x` to `y` and take its first relation `u` in `D`, `v` outside `D`.
Because `u` covers `v`, the two-element subset is convex. In both cases `D`
projects to a forbidden singleton.

The final production certificate requires every selected pair to be either
incomparable or a cover and gates the full proper-ideal count in `R4`.
Independent reconstruction gives:

```text
proper ideals checked                         1,304
contexts with a nonconvex comparable candidate 516
proper ideals with some convex certificate   1,304
convex certificates: cover-chain / antichain  616 / 688
```

Thus the signed dimension `3` at cutoff three is now backed by an all-size
proof rather than used as an extrapolation. The convex-collapse claim passes.

## 5. Positivity and global-shock controls — pass

The independent row-span reconstruction again verifies:

- the two-chain proper singleton is forced to zero;
- both `V` zero sums are affine consequences; and
- positivity kills all terms in those sums.

The revised proper-ideal receipt records actual induced pair type, projected
singleton, and convex boundary status. Independent selection reproduces
`616` cover-chain and `688` antichain certificates. This closes both the
round-1 tautology and the round-2 convex opening.

The empty/full family with `p=2/5` remains natural on all 3,671 audited cuts.
Its all-size naturality is immediate by direct projection, and the paper
correctly calls its full branch universal-precursor incidence rather than an
outcome or transport shock.

## 6. Completion path and joint quotient — pass

The independent rebuild normalizes the full law first and projects actual
full ideal probabilities. This agrees in all 7,342 contexts with separately
aggregating raw completion weights and normalizing the visible totals.

All revised counts reproduce:

| law scope | labeled classes / max | canonical classes / max |
|---|---:|---:|
| `b=1` | 564 / 42 | 144 / 30 |
| `b=2` | 601 / 45 | 168 / 36 |
| pooled union | 756 / 66 | 199 / 42 |

The canonical operation transports the retained relation and every visible
precursor probability together under the same permutation before choosing an
orbit representative. The manuscript now correctly calls `756/66`
labeled-cover pooled diagnostics and `199/42` the pooled canonical unmarked
quotient. It also correctly refuses to interpret pooled values as fixed-law
minimal token counts.

The law-relative antichain witness remains exactly `1/2` versus `9/14`.

The conceptual downgrade is appropriate: the normalized vector is a decoder
target for a supplied law and visible alphabet. It is not yet a physical
carrier, encoder, nested-cut update, or diamond gluing law.

## 7. Explicit chain and capacity controls — pass

The independent reconstruction uses the actual prefix ideals

$$
0,(2^1-1),(2^2-1),\ldots,(2^n-1)
$$

for every chain depth `1,...,64`. It recovers `n/(n+1)`, not merely an
inserted formula. All 64 messages are distinct, giving the six-bit lower
bound, and nine depths exceed a three-bit alphabet.

The renamed context flag is now typed honestly:
`discarded-chain-context-present` is true at depths two and three, while the
required messages are `2/3` and `3/4`. The flag is not described as a parent
of the retained minimal record.

Each explicit escape control also reproduces:

1. **stochastic:** a binary token with mixing weight `q_n` reproduces the
   marginal, while placing the depth dependence in its encoder;
2. **distributed:** six binary records encode depths 1–64, while unbounded
   depth needs growing total carrier count;
3. **unbounded value:** integer `n` decodes the exact message with no uniform
   alphabet; and
4. **approximate:** the one-valued tail decoder has error at most `1/100` for
   every `n>=99`.

The paper explicitly says these models evade the fixed-token theorem by
changing a premise and do not provide a derived local encoder. The stochastic
control does not smuggle in a claimed solution: it names the global mixing
probability as the relocated missing information.

## 8. Profinite residue and factorial controls — pass

The residue example `5` and `12` modulo `7` reproduces and is correctly
presented as one fixed-stage witness. The general `n` versus `n+m` argument is
analytic.

The repaired factorial gate is honestly labeled a finite shadow. Independent
calculation through `8!` verifies:

- `j!` is zero modulo every `m<=j` in the audited triangle;
- the errors `1/(j!+1)` decrease strictly;
- `j!/(j!+1)=1-1/(j!+1)` exactly; and
- the terminal error is `1/40321`.

The paper supplies the universal argument separately: for every fixed `m`,
the residues are eventually zero, while the real predictions converge to one
and the depth-zero prediction is zero. Its ceiling is explicitly limited to
the standard profinite-integer topology and continuous real readouts, not the
v9 stem spectrum, every Stone space, or measurable discontinuous decoders.

## 9. Reproducibility and state identity — pass

Production state keys retain cardinality wherever the bare empty relation or
mask could collide across levels. Message quotient keys include retained
size, and relabeling canonicalizes relation and probabilities jointly. No
cross-level or label-orbit collision remains.

The source writes no files and imports only the standard library. Two stdout
hashes agree byte for byte, and the final cache-free self-containment audit
passes 4/4.

## 10. Final determination

The revised executable's numerical outputs and the boxed all-subset verdict
are independently reproducible. Round-1 openings concerning coupled message
paths, quotient discipline, explicit chain construction, typed flags,
capacity alternatives, and finite profinite labeling are closed. The
round-2 convex opening is also closed by the cover-or-incomparable lemma and
the independently reproduced `1,304/1,304` certificate gate.

No independent-rebuild blocker remains.

**Round-2 independent-rebuild verdict: PASS.**
