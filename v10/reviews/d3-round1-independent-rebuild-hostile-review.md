# D3 hostile review, round 1: independent reconstruction and reproducibility

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION of the receipt, with the core finite theorem independently confirmed**

The substantive finite result is correct. A variable-history maximal extension
can preserve every old relation while adding a new common-future event above a
down-set meeting several old components. The naturally labeled order counts,
deletion fibers, bridge census, rational kernels, cylinder measures,
antichain probabilities, covariance count, stem witness, and Decimal survival
value all reproduce independently.

The production receipt nevertheless overgrades several checks. `A6` is a
tautology over `range` lengths, not a transition audit. `C2` inserts arbitrary
fractions `1/4` and `3/4` without constructing scheduler presentations or a
canonical quotient. `B3` compares next-level ratios to an edge table saved
from the same kernel-generation loop instead of independently reconstructing
the parent and precursor from each child. The last result is mathematically
correct and passes an independent reconstruction, but the production control
is too coupled. Finally, the last `D3` label says “eligibility” although both
registered positive laws have exactly the same eligible extension support;
the check demonstrates weight nonselection only.

These are concrete repair openings, not a refutation of `CONSISTENT-FAMILY`.

## 1. Frozen snapshot and deterministic execution

```text
ba1bc397a85881b2dcfdad5328dd67e58de6e805d873348e22c374a2e1335e6f  v10/note-d3-profinite-variable-history-extension.md
c1d23fe3481e5245724d8625ade897f708e5ae70c788707110995a7b034d00c9  v10/code/d3_profinite_extension_exact.py
ec845c4b326aacb4057a0c5ac4e8e3aac24826348ff1cfc72008ab7ed803f881  v10/relativistic-isp-v10-paper4-profinite-growth-preserves-past-not-law.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d3_profinite_extension_exact.py
```

Two executions exited zero and were byte-identical:

```text
4f6b8a04c0b9db21ab8f4b08359fb6514460ff80ec7c23f9e92eea348958fd40
```

The receipt reports **23/23 checks passed** and payload digest

```text
0f2f0ed7157811ec94bfa218b0487c39b3b58422afca1853f79050abb66538ec
```

The payload digest is not a hash of the complete stdout. It hashes only the
level-count tuple and the two bridge probabilities. The external byte hash
above is the reproducibility receipt for the full output.

## 2. Independent implementation

I wrote a separate Ruby implementation which imports no production code. Its
SHA-256 was

```text
47b2738031031b74d9148db86812259f0bd9ba8089749c1821c7c6cc95c82a9e
```

It independently implemented:

1. direct upper-triangular transitive-order enumeration;
2. growth by down-set precursors;
3. maximal-event extension and end-deletion;
4. old-old immutability and cover/direct-parent reconstruction;
5. comparability components and bridge index;
6. both exact rational kernels;
7. finite measure recursion;
8. independent child-to-parent/precursor recovery from next-level states;
9. cylinder grouping by end-deletion;
10. arbitrary-permutation covariance;
11. canonical unlabeled order signatures; and
12. exact-rank stem enumeration.

Independent output:

```text
COUNTS growth=[1,1,2,7,40,357]
COUNTS direct=[1,1,2,7,40,357]
EXTEND deletion=true immutable=true direct_parents=true
TRANSITION child multiplicity maxima=[1,1,1,1,1]
BRIDGE disconnected parents=203 exists=true reduction=true
MEASURE normalized=true cylinders=true independent_recovery=true
MEASURE same positive support=true unequal measures=true
ANTICHAIN bridge=1/2,5/7 pair=1/8,1/7
COVARIANCE cases=17648 pass=true
STEMS chain-plus-isolate rank-2 types=2
```

This confirms the core finite result without trusting the production helper
functions.

## 3. Natural-order census — pass

The two finite constructions agree exactly:

$$
|Omega_n|=(1,1,2,7,40,357),\qquad 0\le n\le5.
$$

The direct reconstruction enumerates all subsets of upper-triangular pairs and
retains only transitive strict orders. The growth reconstruction starts from
the empty order and adjoins one maximal label above every down-set.

The shared use of a transitivity predicate in production means its two paths
are not maximally independent, but the separate Ruby implementation obtains
the same sequence.

## 4. Extension, deletion, and state identity — pass

For every transition through `n=5`, independent reconstruction verifies:

- deletion of label `n` returns the exact parent;
- no old-old relation changes;
- the selected precursor is a down-set;
- its maximal elements are exactly the covers into the new event; and
- the child is a strict order on `n+1` elements.

### No hidden child collisions

Every next-level child was independently grouped by its relation. The maximum
number of `(parent,precursor)` pairs generating one child is one at every
audited transition level:

```text
n=0,1,2,3,4: maximum multiplicity 1,1,1,1,1
```

This is also structural. The parent is recovered by deleting the distinguished
last label, and the precursor is recovered as the old ancestors of that label.

### Level identity is load-bearing

The bare relation `frozenset()` occurs at several sizes: the empty history,
one point, and larger antichains all have no ordered pairs. Production avoids
collision because:

- each `levels[n]` is a separate dictionary;
- every relation function receives `n` explicitly;
- edge tables are separated by transition level; and
- cross-level positive-support comparisons use `(n,state)`.

Thus no state-size collision was found. A future serialization must continue
to include `n`; a relation set alone is not a complete finite-state key.

## 5. Bridge shadow — pass at the weak stated meaning

There are exactly 203 disconnected naturally labeled parents across the
audited levels `n=2,...,5`. Every one admits a down-set meeting at least two
comparability components. For every such precursor, the number of undirected
components decreases by

$$
k-1,
$$

where `k` is the number of old components met.

The result is unsurprising because the full old vertex set is always a
down-set, but the exhaustive audit also covers selective down-sets.

The paper's “bridge shadow” terminology is appropriately weak. The extension
creates one common-future event. It creates no old-old comparability, no
signaling relation, no metric adjacency, and no sealed interaction outcome.

## 6. Exact rational kernels — pass

For legal precursor `D` in parent `C`, the two registered laws normalize

$$
w_{a,b}(D\mid C)=a^{|D|}b^{\beta_C(D)}
$$

with `(a,b)=(1,1)` and `(1,2)`.

All finite probabilities and level masses are positive `Fraction` values and
each level sums to one exactly.

On the three-element antichain:

$$
P_{1,1}(\beta\ge1)=\frac12,
\qquad
P_{1,2}(\beta\ge1)=\frac57.
$$

For one fixed pair precursor:

$$
K_{1,1}=\frac18,
\qquad
K_{1,2}=\frac17.
$$

These values reproduce independently.

## 7. Actual next-level cylinder masses and kernel recovery — pass independently

The independent control did not use a saved transition-probability table.
Instead, for every actual state in level `n+1`, it:

1. deleted the last event to recover the parent;
2. read all relations `(i,n)` to reconstruct the precursor mask;
3. grouped the actual child mass by recovered parent;
4. checked the group sum against the actual parent mass; and
5. checked `child_mass/parent_mass` against a freshly evaluated closed-form
   kernel.

Every cylinder and ratio passes exactly for both laws through the full cutoff.

Therefore Theorem 3.1 is correctly instantiated in the audited tower. The
production `B3` gate should nevertheless adopt this independent traversal so
that a future precursor-key or state-collision bug cannot be hidden by the
same generator feeding both sides of the check.

## 8. Infinite projective-limit theorem — mathematically sound, not an executable limit

Each level is finite discrete, each deletion map is surjective, and the finite
measures are projectively consistent. The inverse limit is therefore a compact
metrizable space, and the compatible finite distributions determine a unique
Borel probability measure; on this compact metric space it is Radon.

The executable audits only levels through five events. The infinite statement
comes from the stated projective-extension theorem and the explicit all-level
definitions, not from finite extrapolation alone. The paper supplies those
hypotheses and handles zero-mass parents separately.

## 9. Isomorphism covariance — pass

Independent arbitrary-permutation testing reproduces all 17,648 mapped
parent/precursor cases through `n=4` for both laws.

The invariant quantities are precursor size and number of old comparability
components met. Relabeling transports down-sets and leaves both quantities
unchanged, so the normalized kernels agree exactly.

This is one-step kernel covariance. It does not imply equal raw probability
for every natural labeling of one final unlabeled order.

## 10. Major finding 1 — C2 does not test construction-order quotient discipline

Production `C2` sets

```python
raw_ab = Fraction(1,4)
raw_ba = Fraction(3,4)
canonical_pushforward = raw_ab + raw_ba
```

and checks that the unequal fractions sum to one. These numbers are not
obtained from either registered kernel, a scheduler path, a relation, an
isomorphism class, or a quotient map. The check is an arithmetic illustration,
not an executed gauge test.

There is an actual exact control available inside the registered law. Under
the uniform law at `n=3`, the three natural labelings of the unlabeled order
“one two-chain plus one isolate” have raw masses

$$
\frac18,
\quad
\frac18,
\quad
\frac16.
$$

Their canonical unlabeled pushforward mass is

$$
\frac18+\frac18+\frac16=\frac5{12}.
$$

This demonstrates the intended corrected gauge discipline using real history
states: raw presentation weights need not agree, while the physical orbit mass
is their pushforward sum.

**Required repair:** replace `C2` with a canonical-isomorphism grouping of
actual level masses for both laws. Verify:

1. at least one orbit contains unequal raw natural-label masses;
2. orbit sums are exact;
3. all orbit sums together normalize to one; and
4. relabeling or enumeration order does not change the grouped result.

Do not describe arbitrary fractions as scheduler presentations in a theorem
receipt.

## 11. Major finding 2 — A6 is tautological

Production `A6` checks only

```python
len(range(n+1)) == len(range(n)) + 1
```

for each integer `n`. It never examines a parent, child, precursor, or state
key. The label “every transition changes cardinality” therefore overstates the
gate.

The theorem itself is true by construction and independently verified. Repair
the executable by counting actual transition records and asserting that every
child is typed at level `n+1`, every parent at level `n`, and no child belongs
to the same fixed-level state space. Alternatively, move the statement out of
the receipt and present it as a definitional corollary.

## 12. Major finding 3 — production kernel recovery is too coupled

Production stores

```python
edges[(parent, precursor)] = probability
```

while building the measure, then later iterates the same parents and
precursors and compares `child_mass/parent_mass` to that saved value. The ratio
does use actual next-level masses, so the test is not empty. But parent,
precursor, and expected probability are all supplied by the forward generator.

A defect that consistently miskeys both the generator and recovery loop could
pass. The independent child traversal in Section 7 removes that coupling and
passes exactly.

**Required repair:** recover parent and precursor exclusively from each actual
next-level child, independently recompute the kernel, and assert one-to-one
fiber multiplicity.

## 13. Major finding 4 — “eligibility” is not varied by the witness

Both registered kernels are strictly positive on every legal down-set. Their
extension supports are identical. The final production label

```text
D3 bridge eligibility remains an additional law
```

is therefore not what the check establishes. It compares `1/8` to `1/7` for
the same legal pair precursor.

The receipt proves that **bridge weighting** remains additional. It does not
show that one law permits a bridge which another forbids.

Rename the check and corresponding claims to weighting nonselection. If
eligibility nonselection is desired, add a separately registered covariant
kernel family with controlled zeros and audit normalization, support, and
projective consistency explicitly.

## 14. Covtree/stem witness — pass

For the three-event order containing relation `0<1` and isolated event `2`,
the exact two-element down-stems include:

- `{0,1}`, a two-chain;
- `{0,2}`, a two-antichain.

Their canonical signatures differ. Thus the rank-two stem datum contains two
nonisomorphic types, whereas a sequential two-event prefix is one order.

This exact witness supports the paper's distinction between the labeled
prefix inverse limit and covtree observable refinement. It does not itself
construct a marked lift between them.

## 15. Decimal precision and survival value — pass

Production evaluates `exp(-1.1)` in a local Decimal context of precision 140
and prints 125 significant fractional digits:

```text
0.33287108369807955328884690643131552161247952156921249179333138675074708541284431161261707270054785196654212528402885007445958
```

An independent 200-digit `mpmath` evaluation begins with exactly those digits;
the next omitted digit is `2`, so the printed rounding is correct.

The equality `survival_a == survival_b` in production is tautological because
the identical expression is evaluated twice. That is acceptable as an
illustration of holding the clock fixed, but it is not an independent numerical
cross-check. The independent high-precision comparison supplies that control.

## 16. Self-containment and output discipline

Manual import inspection finds only Python standard-library modules. The file
is under `v10/code/`, uses no network or external data, and writes no files.

Unlike D2, D3 has no executable AST/path self-containment gate. Add one if the
receipt intends to grade that claim rather than leave it to review.

The `CANONICAL PAYLOAD SHA256` is deterministic but intentionally narrow. It
does not cover source code, every check result, the survival string, covariance
case count, or final prose. Preserve the external full-output SHA-256 in the
review/log if bitwise reproducibility is claimed.

## 17. Other remaining openings, correctly disclosed

1. The witness kernel uses a global component statistic and is not a local
   physical law.
2. A common-future bridge shadow is not yet a sealed joint interaction.
3. The unmarked poset contains no ports, screens, evidence block, outcome,
   transport, or holonomy.
4. The marked profinite completion remains open.
5. The physical filtration linking covtree refinement to record birth remains
   open.
6. No D3 result determines cone shape, dimension, stationarity, or scale.

The paper states these limitations honestly.

## 18. Required disposition and passing claim ceiling

Before a passing hostile review:

1. replace `C2` with an actual canonical orbit pushforward;
2. replace or demote tautological `A6`;
3. make `B3` recovery child-driven and collision-sensitive;
4. rename bridge eligibility to bridge weighting;
5. add explicit state-level typing and self-containment controls; and
6. record a full-output digest separately from the narrow canonical payload.

After those repairs, the supported theorem is:

> Naturally labeled finite orders admit coherent one-maximal-event extensions
> by down-set precursors. Such growth preserves every old relation while a new
> event may have ancestry in several old comparability components. Positive
> covariant rational kernels induce consistent measures on the labeled prefix
> inverse limit, and at least two inequivalent kernels exist on the same full
> extension arena. The prefix tower and covtree stem-observable tower have
> different transition meanings.

It does not establish:

- a local or uniquely selected bridge kernel;
- bridge eligibility variation in the positive witness family;
- a construction-order-gauge descended measure on canonical histories;
- a marked sealed-diamond birth law;
- a marked profinite extension;
- a physical identification of covtree rank with click time; or
- any geometric/cone/dimension prediction.

The exact finite mathematics earns `CONSISTENT-FAMILY`. The current production
receipt requires major revision because several of its 23 labels claim tests
that were not actually executed.

