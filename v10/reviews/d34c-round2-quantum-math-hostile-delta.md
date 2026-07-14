# D34c round-2 quantum-mathematics hostile delta

**Frozen delta target:** commit `cf33fe2` against `d34c-round2-quantum-math-hostile-review.md`.

**Verdict:** **DELTA-CLEAN**.

**Findings:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT**.

The finite typed-DAG noun is accepted at its stated conditional width.  This delta does not approve, and the target does not claim, the timed operator-valued D34b measure or the unbounded incoming-reception marginal.

## 1. Independent reproduction

I ran the frozen receipt twice:

- `PYTHONHASHSEED=555123 python3 v10/code/d34c_nse_quantum_history_exact.py`
- `PYTHONHASHSEED=888321 python3 -O v10/code/d34c_nse_quantum_history_exact.py`

Both executions exit zero, print 14/14, and independently produce

```text
8349459eb2ff077578f8a9d08a761b12b98997430d9e1fd2134af83a49270cd0
```

This is byte-identical to the committed output and §17.  The new gates remain exact `Fraction`/`Q(sqrt(2))` calculations; no float, tolerance, random sample, hash-order assumption or numerical eigensolver enters.

## 2. Prior finding disposition

| Prior finding | Delta disposition |
|---|---|
| M1: incoming receptions were suppressed while called coarse-grained | **CLOSED.** C8 is explicitly a conditioned consecutive-A specimen. C13 excludes the timed/infinite marginal. C10 separately constructs a real incoming `i(B,A)` and does not pretend that one specimen performs the missing marginal. |
| M2: remote actor gate used abstract `I/X/Z` surrogate | **CLOSED.** C11 uses the actual A→B diamond interaction and a disjoint P→P/1 D24 birth, on the same 64-dimensional carrier, in both orders. |
| m1: no arbitrary-input actual-family closure | **CLOSED.** C9 constructs the operator tower `C_(x,r,p) -> K_(x,r) -> W_x` and exact 16×16 closures for degree one and two. |
| m2: receiver was an embedding, not literally a time-ordered five-qubit circuit | **CLOSED BY HONEST TYPING.** §16 explicitly distinguishes a branchwise orthogonal receiver embedding from a literal circuit. No stronger circuit claim is consumed by §17. |
| m3: mailbox/flag injectivity checked one way | **CLOSED.** The replacement removes growing mailboxes and compares equality of the durable-signature and fresh-event-record partitions in both directions. |
| m4: census/incidence numbers only printed | **CLOSED.** `(3,10,10,108)`, one incidence entry per depth-two column and nonempty coverage of every depth-one row are fail-closed Booleans. |
| n1: “idle is identity” blurred carrier and total ontology | **CLOSED.** Idle closure is carrier identity while C9 separately appends a fresh event record in the total flagged map. |
| n2: “no spectator diamond” wording | **CLOSED BY SUPERSESSION.** The terminal candidate is the finite typed-DAG/event-instrument statement; it does not use the old phrase as a theorem premise. |

## 3. Independent rebuild of the repaired mathematics

### 3.1 Correct class-operator typing and arbitrary-input closure

The common input sector has four actor slots `(A,B,C,D)`, dimension 16.  At degree two, B and C are distinct existing interaction targets and D is a separate birth slot.  An interaction appends `P=|+>` and `O=|0>`, so every fine class operator

```text
C_(x,s,o,p): H_16 -> H_64
```

has the correct common input width.  The code sums the unrecorded path **before** Gram squaring,

```text
K_(x,s,o) = C_(x,s,o,0) + C_(x,s,o,1),
```

and only then uses the durable `(s,o)` record ranges.  Independent algebra gives

```text
sum_(s,o) K_(x,s,o)^dag K_(x,s,o) = I_16
```

for x targeting B and for x targeting C.  D24 birth on `(A,D)` and carrier-idle separately obey `U^dag U=I_16`.  Consequently

```text
degree 1:  1/4 I_birth + 1/4 I_iB + 1/2 I_idle = I_16,
degree 2:  1/4 I_birth + 1/8 I_iB + 1/8 I_iC + 1/2 I_idle = I_16.
```

This is an operator identity for arbitrary inputs, not a regression on `|+>` alone.  The fresh birth slot is index D, not either target.  The separately retained D24 `9/200` initial-state witness remains correct but no longer carries the general theorem.

The receipt's `durable_result_not_isometry` test is also correctly typed: an individual `K_(x,s,o)` need not be an isometry; the orthogonally flagged sum `W_x` is.  The theorem consumes the exact closure, not an individual durable outcome.

### 3.2 Fresh bounded record Gram semantics

The former append-only actor mailbox has been removed.  Each graph node allocates one immutable event-record factor with local alphabet

```text
birth, idle, interaction x (s,o),  s,o in {0,1},
```

six values total.  Initiator, target and predecessor references live in the typed incidence sector; the local quantum outcome rank does not grow with actor age.  `p` is absent from the record.

The functional's inner product is exactly the product-basis construction represented sparsely:

- different canonical typed graphs are orthogonal;
- on one graph, differing event-record contents are orthogonal;
- rows differing only in unrecorded `p` retain their carrier inner product.

The code now proves that the fresh-record partition and the durable physical-signature partition coincide in both directions modulo `p`, requires one record per event, enforces the six-value alphabet and indegree at most two, and verifies prefix factors persist unchanged.  This is a valid Gram/direct-sum semantics and therefore strongly positive.

### 3.3 Conditioned 108→10 object and hardened incidence

The original tree is now accurately named: non-A events are suppressed.  Its exact masses, action operations, shadows, interference and `108 x 108 -> 10 x 10` restriction are unchanged.  The repair now fail-closes on:

- 3/10 classical histories;
- 10/108 quantum branches;
- exactly one incidence target for every depth-two branch;
- nonempty coverage of every depth-one branch.

The incidence map remains physical: it preserves the first canonical event graph, first record prefix and first fine internal alternative.  Exact matrix pushdown still equals the independently reconstructed depth-one functional.

### 3.4 Incoming reception and two-tip merge

For the incoming specimen, B starts in `|+>` and A in `|0>`.  `i(B,A)` applies the actual interaction with B as control and A as target.  Summing the exhaustive class operators reconstructs the unitary, giving norm one and `P(A=1)=1/2`.  Actor bookkeeping independently confirms:

- B's private ring advances to one;
- A's private ring remains zero;
- both wire tips become `B#r1`;
- A's later idle has predecessor `B#r1`;
- both events have fresh records.

For the merge specimen, independent A and B idles create tips `A#r1` and `B#r1`; `i(A,B)` has exactly both predecessors.  Sorting by event identity erases only auxiliary serialization.  The two idle orders yield equal actor state, canonical typed DAG, fresh-record product and every interaction class vector.  No shared-wire order is incorrectly gauged away.

This closes the finite reception/merge existence requirement without claiming the probability sum over arbitrarily many timed incoming events.

### 3.5 Actual remote interaction × birth factor

C11 is no longer the abstract C6 channel.  On the 64-dimensional carrier it uses:

- actual diamond interaction on `(A,B,P_path,O)`;
- actual D24 birth on disjoint `(P,P/1)`.

The maps commute on all 64 basis vectors.  All eight interaction class vectors agree in both orders, as do the canonical actor graph and fresh records.  Since the remote birth is one common isometry applied to every local class vector, its inner products cancel exactly and the local functional remains `D_diamond`.  The claimed remote marginal statement is therefore sound at this finite actor width.

## 4. C12 theorem audit

C12 follows without importing the missing timed marginal.  Its hypotheses are conditional:

1. a finite typed wire-DAG/prefix sector;
2. preparation-independent normalized local scheduler weights `q_x`;
3. one full flagged event isometry `W_x` per alternative, supported on the touched carriers plus a fresh bounded event factor;
4. exhaustive internal class operators;
5. tensor-support commutation for record-disjoint incomparable events.

For one exhaustive extension,

```text
sum_x q_x W_x^dag W_x = I.
```

Thus incidence coarse-graining of that extension returns the parent functional.  Repeating the same identity removes maximal events one at a time and proves finite down-set restriction.  Gram vectors supply strong positivity at every stage.  Disjoint maps may be swapped; shared-wire events retain their predecessor order, and the merge specimen demonstrates the two-tip case.

This proof is independent of the continuous exponential placement law.  It is a conditional quantum sewing theorem on finite typed sectors, not a measure assigning probabilities to all such sectors.  C13, §17 and LEDGER #170 preserve exactly that boundary: the operator-valued timed D34b measure, unbounded incoming marginal, untimed inverse system and infinite extension remain open.

## 5. Final delta disposition

No prior finding survives at the repaired claim width, and I found no new false formula, normalization, rank, branch factor, closure, incidence map, record Gram, reception/merge identity, remote factorization or theorem overclaim.

The quantum-mathematics stream stamps the following wording:

> **FINITE TYPED-DAG ACTOR/QUANTUM SEWING PASS WITH BOUNDED EVENT RECORDS**, plus the conditional finite-down-set induction theorem for the chosen operation family.  This does not establish the timed operator-valued D34b measure or the infinite incoming-reception marginal.

