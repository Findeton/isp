# D5 hostile round-1 mathematics / probability / capacity review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**  
**Core finite sum-product theorem:** confirmed  
**Core positive-ray theorem:** confirmed at its arbitrary-positive-test scope  
**Reason for grade:** missing frozen receipt cells, an unenforced probability
type, and several load-bearing scope/quantifier overstatements

## Frozen sources reviewed

- `v10/note-d5-typed-collar-message-algebra.md`  
  SHA-256 `67e4a025d65ec49494703c32d937e5280e46ac0fc3e102e3d1799ef3dcb607f6`
- `v10/code/d5_typed_collar_exact.py`  
  SHA-256 `bdd1a0e17b7246b93d3db36c5bec43f8baf05d70689ffa802d060fd2cc9ed923`
- `v10/relativistic-isp-v10-paper6-typed-collar-composition.md`  
  SHA-256 `9ef00b1887e4a83c6fdc61cb7d3cdc125f8e8f7422264bad44040118ba9416f5`

The production receipt was run twice. Both runs reported 29/29 and had
byte-identical stdout SHA-256
`31811a11dda55188639599240df5acc7c0043d851d15311811f76ab425aaa5e8`.

## Independent reconstruction

I rebuilt the decisive cells without importing the production executable.
The independent exact results were

```text
complete parity ranks n=1,2,3:       1, 3, 7
duplicate ledger rank:                2
two independent translated channels: 2
product rank/trace at n=6:            6 / 9/2
16-channel chi-square upper partial:  1431655765/17179869184
gap to 1/12:                          1/51539607552
direct three-factor boundary table:   29, 25, 31, 35
loop separator table:                 20, 6, 6, 20
same-ray prediction:                  5/12, 7/12
reverse-ray prediction:               7/12, 5/12
two supplied birth tables:            2/5,3/5 and 4/9,5/9
swap-invariant scope families:        4 total / 3 nonempty
width-one chain at step 32:            17167680177565,27777890035288
primitive-ray bit growth:             2 -> 45
distinct primitive rays through 32:   32
Bernoulli p=2/3 and p=3/4 towers:      exactly projective through width 8
```

The numerical receipt is reproducible. The problems below concern what those
numbers prove and what the typed arena actually enforces.

## 1. Exact sum-product and provenance

### Confirmed theorem

For a fixed finite factor multiset, disjoint factor provenance, and a cut
through which the two regions meet only on `S`, the contraction identity is
correct. Expanding

$$
\sum_s M_A(a,s)M_B(s,b)
$$

gives one product of every factor for each full assignment and one finite sum
over every eliminated variable. Finite distributivity proves equality with
direct elimination, order independence, associativity, and covariance under
joint relabeling of the assignment variables and factor tables.

The direct table `(29,25,31,35)` and reverse elimination agree independently.
The provenance union carried by intermediate tables is also sufficient to
detect literal reuse of the same provenance identifier in later
multiplication.

### Opening C1 — “construction-order gauge” is too broad

What is proved is **variable-elimination/composition-order invariance for one
fixed provenanced factor multiset**. It does not compare distinct record-birth
histories that produce different factor multisets, factor values, or
provenance allocations. Paper 6 repeatedly abbreviates the former as
“construction-order gauge,” which can be read as the stronger v9 physical
quotient.

**Required repair:** qualify every such occurrence with “for a fixed
provenanced factor multiset.” State explicitly that D5 does not prove equality
of physical pushforwards for distinct factor-creation histories.

### Opening C2 — frozen branching/associativity cell is absent

The preregistered adversarial list requires a branching tree, and C2 promises
an explicit three-piece associativity check. The executable contains only the
three-factor chain and two variable-elimination orders. It has no branching
tree and no independent left-parenthesized versus right-parenthesized message
composition gate. The general algebraic proof is valid, but the promised
receipt coverage was not executed.

**Required repair:** add a branching factor tree; compare direct elimination
with leaf-to-root messages; and explicitly compare both three-piece
parenthesizations with disjoint provenance. Report the exact tables.

### Opening C3 — provenance scope

Opaque unique IDs prevent literal double use; they do not solve ownership of
a factor shared by overlapping collars, semantic duplication under fresh IDs,
or typed orientation of a separator. The theorem already assumes disjoint
provenance, so it remains true.

**Required repair:** state that provenance is a no-double-count guard under a
supplied unique-identity/ownership convention, not a derivation of that
convention. Add a nested-message reuse test showing that provenance union
survives elimination and refuses reintroduction of an interior factor.

## 2. Positive-ray sufficiency and minimality

### Confirmed at the stated mathematical scope

If `M'=cM`, every candidate weight is multiplied by `c`, which cancels on
normalization. Conversely, for distinct normalized positive messages `p,q`,
choose a cell `b0` on which they differ and

$$
g(b)=1+\mathbf 1[b=b_0].
$$

The strictly positive binary birth test with the `z=-1` leg equal to one and
the `z=+1` leg equal to `g` produces a probability strictly monotone in
`E[g]`, so it distinguishes `p` and `q`. Thus the positive ray is exactly the
coarsest predictive quotient **when the external test class contains every
strictly positive table on the full finite collar**.

### Opening S1 — physical minimality must retain the test-class quantifier

The separating `g` is generally a full-collar, high-arity factor. If the
eventual physical birth law permits only bounded-arity, symmetry-restricted,
or otherwise factorized tests, the predictive quotient may be strictly
coarser than the full positive ray. The theorem title states “arbitrary
positive external tests,” but the abstract, verdict diagram, and note
occasionally shorten this to unqualified “minimality” or “positive-ray
sufficiency.”

**Required repair:** attach the arbitrary-full-collar-positive-test quantifier
to every minimality headline. Call the ray a universal diagnostic target, not
the proved minimal state for the still-unknown restricted physical birth
class.

The two same-ray histories and the reversed-ray witness are otherwise exact.
They establish conditional augmented-state sufficiency without making the
primitive unmarked process Markovian.

## 3. Probability typing and structural zeros

### Opening Z1 — the executable accepts signed “probabilities”

The frozen theorem arena requires positive rational factors, and the zero
extension requires nonnegative factors. `Table.__post_init__` checks only
shape. `Table.normalized()` checks only that the total is positive. Therefore

```text
Table(("X",), (2,-1), {"bad"}).normalized() = (2,-1)
```

is accepted, and `predict_new_state` can likewise return signed normalized
weights. The 29 passing examples happen to be nonnegative, but the executable
does not enforce the premise it claims to type.

**Required repair:** reject every negative entry before multiplication or
normalization. Distinguish strict-positive factor construction from the
explicit nonnegative structural-zero sector. Require nonempty provenance for
primitive factors while permitting the provenance-free multiplicative
identity only as an internal message object.

### Structural-zero ceiling

The equality-factor example `(1,0,0,1)` is correct and the all-zero table has
no normalized conditional law. It proves only that one compatible
nonnegative support composes. It does not classify support compatibility,
zero-probability boundary fibers, or conditional versions.

**Required repair:** keep Z1/Z2 labeled as controls, not a general
structural-zero theorem. Add at least one incompatible-support gluing and one
boundary assignment with zero marginal, then state the required refusal or
conditional-version rule.

## 4. Covariance and birth-scope census

Within the explicitly frozen candidate list

```text
{Z,A}, {Z,B}, {Z,A,B}
```

the `A<->B` action has exactly four invariant subsets: the empty family, both
one-leg scopes, the joint scope, and all three. Hence exactly three nonempty
eligibility families survive. The independent census confirms it.

This is not a classification of covariant numerical proposal laws. Even after
an invariant eligibility family is chosen, equivariant weights and factor
tables remain free.

**Required repair:** consistently call the result “three nonempty
swap-invariant eligibility families in the three-candidate arena.” Do not call
them the complete covariant birth laws.

## 5. Character, Gram, covariance, and Fisher ranks

At the uniform screen the nonconstant parity characters form an orthonormal
basis, so their covariance/Gram rank is `2^n-1`. For independent coordinate
observables with plus probability `3/4`, the natural-parameter Fisher matrix
is diagonal with entry `3/4`, hence rank `n` and trace `3n/4`. These exact
claims and the `1/3/7` receipt are correct.

The paper also correctly says that Fisher trace is only one coordinate- and
parameterization-dependent scalarization; it is not a derived universal
content measure.

### Opening R1 — relabeling statement is false as written

Note gate R2 says “Copying or relabeling an existing channel does not increase
rank.” Copying a duplicate does not. Jointly relabeling the entire ledger and
distribution preserves rank. But **adding** a symmetry-translated channel can
increase it: under the uniform two-bit screen, `x1` alone has rank one, while
`x1,x2`—where `x2` is the swap image—have rank two. The executable tests only
a literal duplicate.

**Required repair:** replace R2 by the two true statements: duplicate or
linearly dependent channels do not increase rank; joint bijective relabeling
of the whole model preserves rank. Explicitly refuse the claim for adding a
translated observable.

### Opening R2 — keep the rank nouns separate

The complete-ledger number is a covariance/Gram rank at a declared screen.
It equals a Fisher rank only after choosing the corresponding exponential
family and natural parameterization. Participant count and factor arity are
neither. Preserve these qualifiers in the verdict; “channel rank” alone is
not an invariant physical capacity without the model and quotient.

## 6. Weak-channel KL construction and arity

For

$$
P_i(\pm)=\frac12\pm\delta_i,
\qquad \delta_i=2^{-(i+3)},
$$

all channels are strictly positive and nontrivial. The exact identities are

$$
\chi^2(P_i\Vert U)=4\delta_i^2,
\qquad
D(P_i\Vert U)\le\chi^2(P_i\Vert U),
$$

and independence makes KL additive. The geometric sum is

$$
\sum_{i=0}^{\infty}4\delta_i^2=\frac1{12}.
$$

The clean-room 16-channel upper partial is
`1431655765/17179869184`, exactly `1/51539607552` below `1/12`.
The construction is correct and proves that an additive KL-to-uniform budget
with no positive per-channel floor does not bound channel count.

### Opening A1 — “finite content” is broader than the witness

The construction does not bound the exact description length of the scopes,
the rational biases, provenance, carrier identities, or factor tables. It
does not address a content functional that assigns a fixed positive metadata
or carrier cost. Thus it cannot by itself show that every notion of finite
record content fails to bound arity.

**Required repair:** replace generic “finite content alone” conclusions with
“bounded additive KL/evidence divergence from the chosen null, absent an
irreducible carrier/metadata cost.” State that the example rules out an arity
inference from that scalar alone; it does not prove arbitrarily high arity
fits a fixed exact record encoding.

The single high-arity parity/rank-one example separately proves only that
participant count and infinitesimal channel rank are not the same quantity.

## 7. Separator width and exact state growth

An arbitrary binary width-`b` table has `2^b` entries and its positive ray has
`2^b-1` degrees of freedom. This is a worst-case table-coordinate count, not
an encoding lower bound under every structured or algorithmic representation.
The loop `(20,6,6,20)` correctly proves that one-site marginals can erase a
load-bearing correlation; it does not prove that every loop requires a full
exponential table. Paper 6 mostly preserves this distinction.

For the width-one chain, the primitive ray obeys

$$
(a_{n+1},b_{n+1})=(a_n+b_n,a_n+2b_n),
\qquad(a_0,b_0)=(1,1).
$$

Moreover

$$
\gcd(a_{n+1},b_{n+1})=\gcd(a_n,b_n)=1,
$$

and `b_{n+1}>b_n`. Therefore the **canonical primitive integer ray** has
unbounded numerator size and all normalized rays are distinct. The reported
step-32 endpoint and `2 -> 45` bits are exact.

### Opening K1 — the receipt gives samples but the paper omits the lemma

Without the gcd/recurrence argument, 32 samples do not establish an
unbounded exact alphabet requirement, and unnormalized numerator growth could
otherwise be positive-ray gauge. The conclusion happens to be true here
because the displayed rays are already primitive.

**Required repair:** add the recurrence, gcd preservation, and monotone-growth
proof to Paper 6; gate primitive-ray reduction in the executable. Keep
“numerator bits” distinct from optimal algorithmic description length—a depth
index plus a recurrence is another exact encoding with different resource
tradeoffs.

### Opening K2 — verdict noun overstates the construction

`DISTRIBUTED-BOUNDARY-GROWTH` sounds like a physical distributed carrier
scheme was built. The receipt proves finite table composition, exponential
worst-case separator coordinates, and one exact numeric-growth family. It does
not construct a uniformly bounded per-carrier distributed encoding. The paper
calls the phrase provisional, which concedes the mismatch.

**Required repair:** rename the verdict to `EXACT-BOUNDARY-STATE-GROWTH` or
`SEPARATOR-STATE-GROWTH`. Reserve “distributed” for an explicit carrier
allocation/update theorem.

## 8. Projective-tower ceiling

The two Bernoulli product families with `p=2/3` and `p=3/4` marginalize
exactly under deletion of the last coordinate and remain distinct. This is a
valid finite numerical projective nonselection witness.

It does not construct a projective system of typed provenance, collar
ownership, physical encoders, or local update maps, and it does not prove a
general profinite message theorem. Paper 6 explicitly says continuity,
finite-level readability, provenance, and update remain to be supplied.
Maintain that ceiling.

## 9. Connectedness and carrier scope

The component invariant is exact. Adding a new variable with factor legs only
into one old component cannot merge two old components. A proposal with legs
into two components does merge them, and the factor algebra composes but does
not invent that proposal. The `6/9` subset census is correct.

This is a theorem conditional on the connected-collar-only birth domain, not
a derivation of that domain or of the initial connected seed. The paper
largely states this correctly. Keep `CONNECTED-SEED-ONLY` explicitly
conditional.

## 10. Required round-2 checklist

1. Enforce nonnegative table entries and strict-positive base factors.
2. Add the missing branching-tree, explicit parenthesization, and nested
   provenance-reuse cells.
3. Narrow construction-order gauge to a fixed provenanced factor multiset.
4. Attach the arbitrary positive full-collar test class to every ray
   minimality claim.
5. Correct the false relabeling/rank statement.
6. Scope the `1/12` conclusion to additive KL/evidence content without a
   carrier or description-cost floor.
7. Add the primitive-ray recurrence/gcd proof and separate numeric table size
   from optimal encoding length.
8. Rename `DISTRIBUTED-BOUNDARY-GROWTH` until a distributed carrier scheme is
   actually built.
9. Keep the three-family result scoped to swap-invariant eligibility subsets
   of the frozen three-scope arena.
10. Keep structural-zero and projective results explicitly at their control
    and finite numerical ceilings.

## Final adjudication

The paper owns a useful conditional theorem:

```text
supplied finite nonnegative factors with unique allocated provenance
  -> exact finite variable elimination and separator contraction;
positive boundary messages modulo scale
  -> universal sufficiency/minimality against arbitrary positive tests;
covariance and composition
  -/-> scope, eligibility weight, factor value, or first joining carrier.
```

The exact arithmetic supporting that theorem is sound. The present manuscript
and receipt nevertheless exceed their executed/type-safe ceiling in enough
places to require **MAJOR REVISION** before final acceptance.
