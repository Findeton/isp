# D36 round 1 — probability/arbitration hostile review

**Frozen target:** commit
`5f6cd7fccb6e34991bccd10fa1aa7992ebd0a393`
**Lane:** exact K1/K2/K3 arithmetic, stochastic covariance, disjoint
factorization, finite-bit retry, regional restriction, hard-core
conditionals, hypergraph/finite-cover scope, terminal multiplicities and
infinite liveness
**Verdict:** **MAJOR REPAIR — THE NUMERICAL KERNELS AND RECEIPT REPRODUCE,
BUT THE CLAIMED DISJOINT FACTORIZATION FOR PHYSICAL K1 ARBITRATION MARKS IS
ONLY AN ACCEPTED-SET PUSHFORWARD, AND THE FACTORIZATION FIXTURE VIOLATES THE
REGISTERED THREE-PROPOSAL BATCH BOUND.**

**Count:** **0 blockers / 2 majors / 2 minors / 1 nit.**

The D36 candidate contains real and useful exact results.  K1 and K2 differ on
the path exactly as printed; K3 has the stated hard-core weights; all four
finite-bit rows are right; the raw restriction failure and K3 boundary mixture
are right; fail-fast terminal multiplicities are explicitly not probabilities;
and the note does not promote finite cells into an all-cover, starvation or
root-free completion theorem.

The promotion nevertheless fails in this lane for one structural reason with
two consequences.  K1 calls the sampled strict order a **physical arbitration
mark**.  The code then discards that order, compares only the accepted-set
distribution, and reports full disjoint factorization.  On the negative-control
fixture it samples one global order of four proposals across two disconnected
conflict components.  The selected-set marginal factorizes, but the physical
marked-history law has not been defined or checked after quotienting the
cross-component shuffle.  The same four-proposal fixture is omitted from the
capacity census that prints `max_proposals=3`.

The repair is local.  It does not invalidate the P4 safety result, K1/K2
separation on the connected path, K3 arithmetic, deterministic covariance
no-go or born/token matched control.

## 1. Fresh reproduction and hashes

I ran the frozen executable independently under hash seeds `141421356` and
`173205080`.  Both processes exited zero, were byte-identical and printed
`PASS 22/22`.

The reproduced hashes are:

```text
source
f1b2c5010812e08f560876a570fc06693d59633de03421b0fed5ff5e5c3daed0

complete stdout / committed receipt
0bf500873acdc71bb68c5b7d9012b89310941c879f59b013105db1f0e00fccea

stdout body before the hash/gate trailer
c5258f02d8f9763708e9355a304295e6c94a7c85aac39dde22c1d3f0b826c1c7

internal science
872a38acd65f7ebcb122a50f6713da53ae119764c7449387b1b55efe27acf04b

note
5605b76f0053e1527e84dc3f0830362e246f6ff43ab0623cf01a56a073d87e98
```

`git diff --check 8b589e2..5f6cd7f` is clean.

The note correctly distinguishes the full stdout hash in section 16 from the
`stdout_body_sha256` printed inside that stdout.  The earlier hashes in section
15 are explicitly labeled provisional and remain as an audit checkpoint.

## 2. Independent K1/K2/K3 reconstruction — pass

### 2.1 K1 on the path

The conflict graph is

```text
P -- Q -- R.
```

There are six strict orders.  Greedy gives `{Q}` exactly when Q precedes both
endpoints, which occurs in the two orders

```text
QPR, QRP.
```

The other four orders accept both endpoints.  Therefore

```text
K1({Q})   = 2/6 = 1/3;
K1({P,R}) = 4/6 = 2/3.
```

This matches the code and receipt.

### 2.2 K2 on the path

The only maximal independent sets are `{Q}` and `{P,R}`.  Uniform maximal-set
selection therefore gives

```text
K2({Q})   = 1/2;
K2({P,R}) = 1/2.
```

The separating event is exact.  K1 and K2 are normalized, safe, nonempty,
maximal and automorphism-covariant on this finite connected graph.  Their
disagreement is a valid finite regional nonselection witness.  It does not
derive either law physically.

### 2.3 K3 on the path

The path's independent sets are

```text
{}, {P}, {Q}, {R}, {P,R}.
```

For `lambda=1`, every weight is one and every probability is `1/5`.  For
`lambda=2`, the weights are `1,2,2,2,4`, with partition function eleven:

```text
{}:1/11, {P}:2/11, {Q}:2/11, {R}:2/11, {P,R}:4/11.
```

The printed K3 laws and supplied-`lambda` nonselection are correct.  K3 may
select the empty or a nonmaximal set, and the note correctly refuses to call it
a progress protocol.

## 3. Covariance and deterministic symmetry — pass at the selected-set scope

Uniform strict orders, uniform maximal independent sets and hard-core weights
are all equivariant under complete relabeling of the marked graph.  The path
alpha gate is therefore supported by the formulas, not merely its one tested
renaming.

The deterministic pair no-go is also exact.  The safe feasible sets are

```text
{}, {P}, {Q}.
```

Under the automorphism swapping P and Q, only the empty safe set is invariant.
The other invariant subset `{P,Q}` is unsafe.  Thus no deterministic
equivariant selector can be both safe and nonempty on that genuinely symmetric
boundary.  Structural asymmetry could evade the theorem; nominal spelling
cannot.  The note states that premise correctly.

The covariance of K1's **physical mark history**, rather than its selected-set
pushforward, remains part of M1 below.

## 4. MAJOR M1 — selected-set factorization is not full physical-mark factorization

Sections 8 and 9 jointly require more than the executable proves:

```text
K1: the strict order is a physical arbitration mark;
regional gate: test full joint distributions, not only local marginals;
quantum/record scope: a priority that changes dynamics must be recorded.
```

But `random_greedy_kernel` enumerates strict orders and immediately collapses
them to an `Outcome = FrozenSet[str]`.  `disjoint_factorization_gate` then
compares only

```text
law(accepted set on union)
```

with the product of the two component accepted-set laws.  It does not retain
or compare:

- the physical priority/order mark;
- cross-component order comparisons;
- retry/tie records;
- the P4 apply/reject/close histories conditioned on selection; or
- a construction-order quotient of those marked histories.

The omission is visible exactly on the gate's two disconnected conflicts:

```text
component 1: P -- Q
component 2: R -- S.
```

A global uniform order has `4! = 24` physical order atoms.  The product of
independent component orders has only

```text
2! * 2! = 4
```

atoms.  Each pair of component orders has six global interleavings.  After
forgetting those six shuffles, the four accepted sets do indeed have
probability `1/4`; this is exactly why the committed gate passes.  If the
global strict order itself is physical, however, those 24 histories have not
factored into the four product histories.  If the cross-component shuffle is
gauge, the note must say so and the executable must quotient it before calling
the physical law factorized.

This does not refute the mathematical identity that restrictions of a uniform
global permutation to disjoint subsets are independent.  It refutes the
stronger receipt narration that the tested `Distribution` is the full joint
physical distribution.

**Required repair:** choose and implement one consistent ontology:

1. sample and record independent strict orders separately on each connected
   conflict component; or
2. retain a global presentation order but prove that cross-component shuffles
   are construction gauge and define the canonical component-order quotient.

In either case, compare the complete marked arbitration law—not merely the
accepted set—under disjoint union, alpha renaming and the shared-randomness
negative control.  Then compose the selected marks with the typed P4 terminal
histories or explicitly limit G11 to the arbitration selected-set
pushforward.  Until then, “full joint distributions” and physical K1
factorization are unearned.

## 5. MAJOR M2 — the factorization fixture violates the frozen capacity pin

The note pins

```text
proposals in one closed batch at most 3.
```

The receipt prints `max_proposals=3`.  But `disjoint_union_fixture()` contains
four proposals:

```text
P, Q, R, S.
```

It is passed as one fixture to all four kernels, and K1 enumerates all 24
strict orders on that four-proposal union.  `capacity_gate` obtains the value
three only because it scans `FIXTURES.values()` and does not scan
`disjoint_union_fixture()`.

The campaign therefore has a four-proposal probability cell that is absent
from its capacity census.  Calling it two separate batches would not describe
the present K1 implementation, which samples one global four-proposal order.

**Required repair:** either:

- adopt the component-local/quotient repair in M1 so the two factors are
  genuinely separate two-proposal regions and no four-proposal closed batch is
  constructed; or
- change the registered bound to four, include every auxiliary fixture in one
  authoritative capacity census, and rerun the source/receipt/science hashes.

Add a gate that recursively inventories every fixture passed to every kernel,
not only the named `FIXTURES` dictionary.  The present printed capacity theorem
is false even though every probability is numerically finite.

## 6. MINOR m1 — finite-bit “resolution” needs the exact fixed-contest and retry-opportunity scope

The unique-greatest formula is correct:

```text
U(k,M) = k/M^k * sum_(s=0)^(M-1) s^(k-1).
```

It gives exactly:

```text
(k,M)=(2,2): 1/2, expected attempts 2;
(2,4):       3/4, expected attempts 4/3;
(3,2):       3/8, expected attempts 8/3;
(3,4):       21/32, expected attempts 32/21.
```

The one-bit pair unresolved mass after five independent attempts is
`(1/2)^5=1/32`.

Two scope clauses are nevertheless implicit:

1. `(1-U)^n` and `1/U` assume the same finite contender contest is actually
   retried with fresh independent marks after every tie; D36 has not supplied
   the opportunity/fairness law that guarantees those retry records occur.
2. `U(k,M)` is the probability of a unique **greatest** mark, not a complete
   strict order.  If one chunk must instantiate K1's whole order, the relevant
   probability is

   ```text
   (M)_k / M^k.
   ```

   For three contenders this is zero at `M=2` and `3/8` at `M=4`, rather than
   `3/8` and `21/32`.  A unique greatest can settle a single-winner clique, but
   a general residual conflict graph needs a recursive tie/refinement rule.

The note's final verdict does leave retry fairness and arbitration open, so
this is a scope repair, not a failed arithmetic result.

**Required repair:** call the printed rows “unique-greatest resolution of a
fixed finite single-winner contest, conditional on an iid retry sequence that
continues after every tie.”  If they are intended to realize K1 on arbitrary
graphs, add a bounded-record recursive tie-refinement construction and check
the induced complete strict-order law.  Change the receipt's
`eventual_resolution` wording to expose that conditioning.

## 7. MINOR m2 — the DLR formula silently excludes zero-mass boundaries

For each lambda, the path has twelve target/boundary assignments in the raw
single-site loop.  The code checks ten and silently skips two when

```text
mass0 + mass1 = 0.
```

They are the inadmissible outside assignments `{Q,R}` when the target is P and
`{P,Q}` when the target is R.  Across `lambda=1,2`, the receipt therefore
prints 20 conditionals while four zero-mass assignments were skipped.

The displayed DLR formula is correct on admissible positive-mass boundary
conditions.  It is not an ordinary conditional probability on a zero-mass
boundary without a separately chosen specification value.

**Required repair:** qualify the two conditional equations by “for every
admissible positive-mass outside configuration,” and print both

```text
tested_positive_mass=20
skipped_zero_mass=4.
```

Alternatively define the kernel on all formal boundary states and test that
chosen extension separately.  No K3 weight changes.

## 8. NIT n1 — K1 points to the wrong deterministic theorem

Section 8 says to sample a strict order and “then apply T1.”  T1 is the
fail-fast causal-attempt theorem.  The deterministic accepted-set map is P6,
proved by T3.

**Required repair:** replace “apply T1” with “apply P6/T3's greedy rule.”

## 9. Restriction and boundary mixture — exact finite cell, properly scoped

The raw K1 restriction is right:

```text
path K1 restricted to {P,Q}: {P}:2/3, {Q}:1/3;
direct edge K1:               {P}:1/2, {Q}:1/2.
```

For K3 at `lambda=1`, the path law is uniform over its five independent sets.
Restriction to `{P,Q}` gives

```text
{}:2/5, {P}:2/5, {Q}:1/5.
```

The external boundary variable has

```text
P(R=0)=3/5,  P(R=1)=2/5.
```

At `R=0`, the edge law is uniform on `{}, {P}, {Q}`.  At `R=1`, Q is blocked
and P is a one-site hard-core variable, giving `{}, {P}` with probabilities
`1/2,1/2`.  The mixture reproduces `2/5,2/5,1/5` exactly.

This is one valid numerical boundary-disintegration cell.  The note correctly
does not call it a defined region category, an all-region overlap theorem or a
global completion.  The executable hand-constructs the `R=1` boundary law; a
future architecture must type that boundary and its transport map rather than
infer a theorem from this example.

## 10. Hypergraph and finite-cover claims — pass only at the stated obstruction scope

The three-way gate proves the elementary but important obstruction that one
triple can be forbidden while every pair is allowed.  The executable's actual
arbitration functions remain pairwise graph functions; they do not implement
K1--K3 on general conflict hypergraphs.  Section 5 explicitly says the first
receipt is pairwise, so no hypergraph protocol theorem is currently being
claimed.

Likewise, three pair laws supported on unequal binary pairs have matching
uniform singleton marginals but no joint triple: no binary assignment can
satisfy all three inequalities.  Support emptiness is already an exact proof
that the corresponding rational marginal system is infeasible.  This is a
negative finite-cover counterexample, not a positive cover-consistency gate.
The note preserves that ceiling and disclaims an all-cover theorem.

Any next round should avoid renaming G17 as “hypergraph support” or “finite
cover consistency.”  It establishes **pairwise insufficiency** in both rows.

## 11. Terminal multiplicities, liveness and nonselection — scope pass

The fail-fast terminal rows

```text
pair       8 terminals: 2 empty, 3 P, 3 Q;
triangle  17 terminals: 2 empty, 5 each singleton;
disjoint   1 terminal:  both proposals;
partial    2 terminals: one for each singleton
```

are counts of distinct canonical terminal states in a nondeterministic
delivery graph.  They are not equiprobable service orders or a probability
law.  Both note and receipt now say this explicitly.  No probability should be
inferred from ratios such as `3/8` in the pair row.

The positive P4 theorem is also correctly conditional on a finite attempt,
authenticated reliable messages, failure-free actors/coordinator and fair
delivery.  The exact graphs have no nonterminal leaves and are directed
acyclic on the four registered fixtures.  Coordinator loss can strand a
promise, and safe unilateral expiry without a failure detector is rejected.

The note does not derive retry opportunity, lineage success, starvation
freedom or an infinite root-free history measure.  K1/K2 and the two supplied
K3 activities demonstrate numerical nonselection at finite regional scope;
they do not prove that nature uses any of those laws.  Subject to m1's
conditional wording, the infinite-liveness ceiling is honest.

## 12. Repair gates and final disposition

Required closing gates are:

1. **marked-law factorization:** retain component-local arbitration marks or
   quotient global cross-component shuffles, then compare exact full marked
   laws under disjoint union and alpha renaming;
2. **authoritative capacity census:** include every fixture passed to every
   kernel, or eliminate the four-proposal global batch by the componentwise
   construction;
3. **finite-bit scope:** distinguish unique-greatest contest resolution from
   complete strict-order generation and condition iid formulas on continuing
   retries;
4. **DLR support:** print positive-mass checks and zero-mass skips separately;
5. **cross-reference repair:** point K1 to P6/T3; and
6. rerun exact source/stdout/internal hashes and one focused probability delta.

The following results need no numerical repair:

```text
K1 path                         {Q}:1/3, {P,R}:2/3
K2 path                         {Q}:1/2, {P,R}:1/2
K3 lambda 1 and 2               exact as printed
finite-bit U rows               1/2, 3/4, 3/8, 21/32
K1 raw restriction              2/3 versus 1/2
K3 boundary mixture             exact
deterministic pair no-go        exact
terminal multiplicity warning  correct
all-cover/infinite scope        still open
```

Final tally:

```text
B  blockers  0
M  majors    2
m  minors    2
n  nits      1
```

**Recommendation:** retain the candidate noun provisionally but withhold
terminal promotion.  The finite safe fail-fast grammar and numerical
arbitration examples survive.  D36 must close the physical-mark/product and
capacity contradictions before it can claim disjoint-factorizing local
probabilistic arbitration.
