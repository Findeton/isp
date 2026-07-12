# D5 hostile review, round 1: independent rebuild and reproducibility

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION of the executable/type boundary, with the finite factor algebra independently confirmed**

Every registered numeric result reproduces in a clean-room implementation.
The exact parity ranks, weak-channel budgets, separator contractions,
elimination orders, loop message, predictions, component counts, separator
growth, bit lengths, structural zeros, scope-family count, and projective
towers are correct. Production stdout is deterministic and the v10
self-containment audit passes.

The central finite theorem is standard and sound: supplied finite factors
with disjoint provenance compose by exact sum-product contraction, and their
effective boundary positive ray is predictively sufficient in the stated
arena.

The production type boundary does not enforce that arena. `Table` validates
only variable uniqueness and table length. It accepts negative entries, while
`normalized()` checks only that the **sum** is positive. A table such as
`(-1,2)` is therefore accepted and normalized to `(-1,2)`, which is not a
probability distribution. `predict_new_state` inherits the same defect. This
contradicts the manuscript's strictly positive base-factor premise and its
claim that structural zeros form a separately tested support category.

The receipt also does not explicitly execute the preregistered right-nested
three-piece associativity cell or a branching-tree composition cell, and its
numeric-storage diagnostic measures an unnormalized representative without
certifying that the positive ray is primitive. These are repairable receipt
openings. The independent reconstruction supplies the missing right nesting
and confirms that the registered chain ray happens to be primitive, so none
refutes the mathematics.

## 1. Frozen snapshot and reproducibility

```text
67e4a025d65ec49494703c32d937e5280e46ac0fc3e102e3d1799ef3dcb607f6  v10/note-d5-typed-collar-message-algebra.md
bdd1a0e17b7246b93d3db36c5bec43f8baf05d70689ffa802d060fd2cc9ed923  v10/code/d5_typed_collar_exact.py
9ef00b1887e4a83c6fdc61cb7d3cdc125f8e8f7422264bad44040118ba9416f5  v10/relativistic-isp-v10-paper6-typed-collar-composition.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d5_typed_collar_exact.py
```

Two sequential executions exited zero and produced byte-identical stdout:

```text
31811a11dda55188639599240df5acc7c0043d851d15311811f76ab425aaa5e8
```

The executable reports **29/29 exact checks passed** and internal payload
digest:

```text
33f00dab6d86991576d87bd4e008cdb9715ac8bebb3f55cbf4e56bd272716b42
```

The internal digest covers the registered numeric payload rather than all
stdout; the external hash above is the full-output reproducibility receipt.

The self-containment audit reports 4/4:

```text
PASS: all v10 investigation executables reside in v10/code
PASS: no duplicate investigation source exists outside v10/code
PASS: every investigation executable imports only the Python standard library
PASS: no .pyc cache artifact exists under v10
```

## 2. Clean-room implementation

I wrote a separate Ruby implementation using semantic assignment hashes and
exact `Rational` arithmetic. It imports no production code. Its SHA-256 is:

```text
7614738b1b45f21de404b25a4fdadaa1bae21a81065df15e7a3baff422002575
```

The reconstruction independently implements:

1. binary assignment generation and explicit semantic table lookup;
2. variable reorder, multiplication, marginalization, and elimination;
3. provenance-set union and duplicate refusal;
4. direct, left-associated, right-associated, and reverse-order contraction;
5. arbitrary rational matrix rank and parity covariance;
6. local prediction and positive-ray comparison;
7. factor-hypergraph components and direct-scope tests;
8. exact chain-message recursion and primitive-ray diagnostics;
9. Bernoulli projective towers;
10. structural-zero and impossible-support controls; and
11. swap-invariant scope-family enumeration.

Independent output:

```text
R ranks=[1,3,7] duplicate=2 collective=(1,1),(10,1)
R product=[(1,3/4),(2,3/2),(3,9/4),(4,3),(5,15/4),(6,9/2)]
R weak_tv=[1/6,1/10,1/18,1/34,1/66,1/130,1/258,1/514]
R weak_kl_partial_16=1431655765/17179869184 < 1/12
C chain=[29,25,31,35]
C reverse=true left=true right=true relabel=true duplicate_refused=true
C loop=[20,6,6,20]
C loop_normalized=[5/13,3/26,3/26,5/13]
C one_site_product=[1/4,1/4,1/4,1/4]
S messages=[2,4],[2,4],[4,2]
S predictions=[5/12,7/12],[5/12,7/12],[7/12,5/12]
S unmarked=[1/2,1/2] ray_control=true
B components base/local/joined=2/2/1
B parent subsets local/spanning=6/9
B connected_growth_components=1
B ancestry_message=[10,6,6,10] direct_AB_factor=false
K separator_8=[8,256,255]
K distinct_width_one_predictions=32
K bit_lengths=2->45 strictly_increasing=true
K final_ray_gcd=1 normalized_denominator_bits=46
K projective_towers=true
Z message=[1,0,0,1] normalized=[1/2,0,0,1/2] refusal=true
L candidates=[2/5,3/5],[4/9,5/9]
L invariant_scope_families=4 nonempty=3
```

This reproduces every theorem-critical production cell without trusting its
table, rank, component, or elimination helpers.

## 3. Table ordering and state identity — pass

Production enumerates each variable in the order `(-1,+1)` and interprets
`-1` as binary bit zero, `+1` as bit one. Thus a two-variable table with
variables `(X,Y)` is ordered:

```text
(X,Y)=(-1,-1),(-1,+1),(+1,-1),(+1,+1).
```

The clean-room implementation uses semantic assignment hashes and only
converts to this order when printing. It independently recovers:

```text
chain boundary (A,B) = (29,25,31,35)
loop boundary  (A,B) = (20,6,6,20)
zero boundary  (A,B) = (1,0,0,1).
```

Therefore the agreement is not an accidental raw-array comparison under a
shared index convention.

Variable names remain part of assignment identity and table variable order
remains explicit. Reordering reconstructs values semantically. No collision
between, for example, `(-,+)` on `(A,B)` and the same bit tuple on `(B,A)` was
found. Joint relabeling transports factor scopes and boundary names together
and reproduces the same ordered physical prediction.

The elimination-order validator compares sets and therefore accepts an order
containing duplicate variable names if its set equals the interior set. Such
duplicates are operationally harmless—eliminating an already eliminated
variable is a no-op—but the validator should also require unique order entries
and exact length so that “contains exactly” is true literally.

## 4. Rank and weak-channel controls — pass

### Complete and redundant parity ledgers

At the uniform screen, the nonconstant parity characters are orthonormal. The
independent covariance matrices therefore have ranks:

$$
1,3,7
$$

for one, two, and three variables. Repeating masks `(1,2,1)` gives rank two,
not three. A single full-support parity character has variance one and rank
one at every reconstructed arity through ten. Participant count, listed
channel count, and rank are therefore separated correctly.

### Independent biased channels

For independent `P(+)=3/4` coordinates, each mean is `1/2` and each variance
is `3/4`; cross covariances vanish. Independent reconstruction gives

$$
\operatorname{rank}J_n=n,
\qquad
\operatorname{tr}J_n=\frac{3n}{4}
$$

through six channels. The manuscript correctly scopes the Fisher reading to
an exponential-family character parameterization instead of equating every
scalar content with this matrix.

### No positive weak-channel floor

The total-variation sequence reproduces exactly and ends at `1/514`. For

$$
\delta_i=2^{-(i+3)},
$$

the independent exact partial upper sums increase while remaining below
`1/12`; at width 16 the sum is

$$
\frac{1431655765}{17179869184}.
$$

The analytic result is valid:

$$
D(P_i\Vert U)\le\chi^2(P_i\Vert U)=4\delta_i^2,
\qquad
\sum_{i=0}^{\infty}4\delta_i^2=\frac1{12}.
$$

Thus this additive KL control permits arbitrarily many nonzero independent
channels under one finite upper budget. It does not prove a statement about
every imaginable resource functional, and the paper appropriately frames the
conclusion as refusal to infer an arity bound without a separate irreducible
per-carrier cost and allocation theorem.

Production inserts the TV and chi-square formulas rather than constructing
the corresponding distributions. The paper supplies the elementary proof,
so the result is sound; a stronger receipt should instantiate each binary
pair and recompute TV and chi-square directly to remove formula coupling.

## 5. Separator contraction and elimination order — pass

For factors `A-S`, `S-T`, and `T-B`, independent direct elimination gives:

$$
M_{AB}=(29,25,31,35).
$$

The following all agree semantically:

- eliminate `S` then `T` directly;
- eliminate `T` then `S` directly;
- first contract the left two factors, then attach the right factor; and
- first contract the right two factors, then attach the left factor.

Production executes the first three comparisons except that the explicit
right-associated contraction is absent. The theorem's finite-sum proof covers
it, and the clean-room right nesting passes, but the preregistered
“three-piece associativity” gate should include both parenthesizations.

The preregistration also requested a branching-tree adversarial composition
cell. Production contains the branch `H-A,H-B` and correctly derives its
correlated boundary message `(10,6,6,10)`, but uses it only to distinguish
ancestry correlation from a direct `A-B` carrier. It does not compare direct
and nested elimination on a branching tree. Add that explicit gate or record
the preregistered deviation.

Relabeling `A,S,T,B` jointly to `Q,R,U,V` preserves the chain message.
Multiplying a relabeled copy of the same sealed factor is refused because its
provenance still overlaps.

## 6. Loop and predictive-message controls — pass

The loop contraction is:

$$
(20,6,6,20),
$$

with normalized distribution

$$
(5/13,3/26,3/26,5/13).
$$

Both one-site marginals are uniform, so their product is `(1/4,1/4,1/4,1/4)`
and loses the correlation. The paper draws only the warranted conclusion:
one-site products are not generally sufficient. It does not infer an
exponential lower bound from this one loop.

The hidden-variable and unary histories independently contract to the same
message `(2,4)` and, against the common `B-Z` birth factor, both predict

$$
(5/12,7/12).
$$

The reverse message `(4,2)` predicts `(7/12,5/12)`, while an unmarked uniform
boundary predicts `(1/2,1/2)`. Scaling `(2,4)` to `(1,2)` leaves the prediction
unchanged. These cells correctly establish the sufficiency of the positive
ray for the audited continuation and the insufficiency of the unmarked
boundary.

The manuscript's universal sufficiency and minimality statements do not rest
on these examples alone. Proportionality cancels for every common external
factor, and its positive test construction distinguishes every pair of
different normalized positive messages. That proof is sound within the
allowed arbitrary positive boundary-factor class.

## 7. Major finding — positivity is claimed but not enforced

The paper defines the base factor arena with strictly positive rational
tables and treats structural zeros in a separate extension. Production
`Table.__post_init__` checks only:

1. that variables are unique; and
2. that the number of values is `2^|scope|`.

It does not check `value>0` or even `value>=0`. `make_table`, `multiply`, and
`relabel` therefore all permit negative factor entries.

`normalized()` checks only

```python
total = sum(values)
if total <= 0: refuse
```

and returns every `value/total`. Hence a table `(-1,2)` has positive total one
and is returned unchanged as a purported normalized distribution with a
negative entry. `predict_new_state` uses this normalization and can expose
the same invalid result as click weights.

This is not merely defensive programming. Strict positivity is used by:

- the probability interpretation;
- positive-ray sufficiency and minimality;
- support-independent conditionalization; and
- the claimed separation between the base theorem and structural-zero
  controls.

**Required repair:** introduce explicit table categories or constructors:

- positive factor tables: every entry strictly positive;
- structural-zero/nonnegative factors: every entry nonnegative, plus explicit
  support compatibility; and
- derived messages: nonnegative, with positive total before normalization.

Negative entries must always be refused. Add exact negative-entry controls
for direct normalization and `predict_new_state`.

Until this is repaired, the executable does not mechanically instantiate the
typed arena described by the paper, even though every registered factor is
itself positive or deliberately zero-valued.

## 8. Provenance behavior — finite check passes; nested ownership remains open

Provenance unions survive multiplication and marginalization, so a derived
message remembers every factor already included. The registered duplicate
test correctly rejects reuse of `f_as` even after its variables are renamed.
Sequential chain composition uses disjoint sets and includes each factor once.

This is sufficient for the finite theorem's explicit premise: two regions
with disjoint factor provenance. It is not yet a complete overlapping-collar
protocol. If a factor touches a separator shared by nested regions, the
physical construction must specify which region owns it, how restrictions of
provenance are represented, and when a previously summarized factor may be
reused without being multiplied twice. A set of opaque strings detects exact
duplication but does not derive those ownership maps.

The paper lists this as a hostile opening and does not claim it solved.
Round 2 should either provide a nested ownership/gluing cell or retain the
theorem explicitly at disjoint-provenance scope.

## 9. Connected components and birth domain — arithmetic passes

The clean-room factor hypergraph gives:

```text
base components                  2
after local Z-A birth            2
after explicit Z-A and Z-C legs  1
within-component parent subsets  6
cross-component parent subsets   9
connected sparse growth          1 component through R0,...,R7.
```

Old factors remain unchanged. Shared ancestor factors `H-A,H-B` generate the
correlated message `(10,6,6,10)` without any factor whose scope contains both
`A` and `B`. Direct carrier, path connectivity, and correlation are therefore
distinguished correctly.

The “refusal” in `B3` is a classification count, not an implemented birth
gate: the code increments a refusal counter for subsets spanning components
and manually constructs a connected chain. The paper honestly calls
connected-collar-only birth a domain choice and does not claim it is derived.
A future executable local law should make this classifier an actual typed
proposal validator.

## 10. Separator growth and exact numeric storage — values pass

An arbitrary binary width-eight table has 256 entries and 255 normalized
degrees. This is a worst-case coordinate count, not an exponential lower
bound for every physical history; the paper says so.

The width-one transition recursion produces 32 distinct exact positive rays.
The final unnormalized pair is:

$$
(17167680177565,27777890035288),
$$

with greatest common divisor one. Thus the observed `2 -> 45` numerator-bit
growth is not caused by a removable common scale. The normalized common
denominator requires 46 bits.

Production measures only the raw unnormalized numerator bit length and does
not check the gcd or normalized representation. In this registered cell the
claim is true, as the independent primitive-ray control shows. Add a
canonical-ray reduction or normalized numerator/denominator gate so future
factor normalizations cannot manufacture artificial storage growth.

The verdict phrase `DISTRIBUTED-BOUNDARY-GROWTH` remains stronger than the
implemented object. Production stores each separator as one centralized
table; it does not construct a distribution of that table over bounded finite
carrier records. The note and paper admit this and call the phrase
provisional. A defensible current label is `SEPARATOR-STATE-GROWTH` until an
actual distributed encoding and update law are supplied.

## 11. Projective towers and structural zeros — pass at stated scope

Independent Bernoulli towers with `p=2/3` and `p=3/4` marginalize exactly
through width eight and remain different already at width one. The all-width
formula is immediate, while the executable is honestly a finite shadow.
Projective compatibility hosts both laws and selects neither.

The deterministic equality chain gives:

$$
(1,0,0,1)
$$

and normalizes to `(1/2,0,0,1/2)`. An all-zero table is refused because it has
no conditional law. These controls are correct but do not themselves supply
the support-category typing required by the major finding above.

## 12. Value and scope nonselection — pass

Against the same message `(2,4)`, birth factors with equal/different weights
`(4,1)` and `(2,1)` give:

$$
(2/5,3/5)
\quad\text{and}\quad
(4/9,5/9).
$$

Both are positive and normalized. Composition selects neither value.

Under the swap `A<->B`, the three candidate scopes form two orbits:

```text
{{Z,A},{Z,B}}   and   {{Z,A,B}}.
```

Choosing either orbit, neither, or both gives four invariant families, three
nonempty. A single-`A` family is not invariant. Covariance therefore refuses
asymmetric selection but does not choose among the three nonempty physical
families.

## 13. Scope and claim audit

The paper preserves the main limitations:

- factor scope, value, provenance, and collar assignment are supplied data;
- the universal encoder composes them but does not derive an interacting law;
- connected-collar-only birth and the initial connected seed are choices;
- one high-arity parity channel can remain rank one;
- no scalarization of the multichannel Fisher matrix is declared canonical;
- one-site loop failure is not promoted to a universal exponential bound;
- finite projective towers are not a physical encoder or parameter selector;
- state augmentation does not make the primitive full-history process
  Markovian; and
- no cone, dimension, speed, horizon, quantum, or absolute-scale claim is
  made.

The core verdict `CONDITIONAL-LOCAL-COMPOSITION + CONNECTED-SEED-ONLY +
CHANNEL-RANK-NONBOUND + SCOPE/VALUE-NONSELECTION` is supported. The distributed
memory label should be downgraded as noted until its carrier construction is
real.

## 14. Required openings before round 2

1. **Enforce the factor/support type boundary.** Reject negative entries;
   distinguish positive base factors, nonnegative structural-zero factors,
   and derived messages; add negative normalization and prediction controls.
2. **Complete the composition cells.** Execute both three-piece
   parenthesizations and a direct-versus-nested branching-tree contraction.
3. **Specify nested provenance ownership.** Test overlapping collars or state
   clearly that only a partition into disjoint factor-provenance regions is
   implemented.
4. **Canonicalize numeric storage.** Reduce positive rays to primitive form or
   count normalized numerator and denominator bits before claiming exact
   storage growth.
5. **Rename the provisional distributed verdict.** Use
   `SEPARATOR-STATE-GROWTH` unless a bounded-per-carrier distributed encoding
   is actually constructed.
6. **Instantiate the weak-channel formulas.** Recompute exact TV and
   chi-square from explicit binary distributions so the executable does not
   validate a closed-form expression against itself.
7. **Tighten state validators.** Require elimination orders to be duplicate
   free and give primitive factor constructors nonempty scopes and nonempty
   unique provenance.

## 15. Final determination

The finite algebra and every registered number survive clean-room
reconstruction. The scientific boundary is also essentially correct:
supplied typed factors can screen and compose local history, but covariance
and composition do not select their carrier scopes or numerical values.

Acceptance is withheld because the executable does not enforce the positive
factor arena it claims to instantiate and because several preregistered
composition/type controls remain illustrative rather than executable.

**Round-1 independent-rebuild verdict: MAJOR REVISION.**
