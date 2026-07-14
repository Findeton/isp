# D34c round 2 — independent quantum-mathematics hostile review

**Frozen target:** commit `d634f3d`, especially `v10/code/d34c_nse_quantum_history_exact.py` and note-d33 §§14–15.  This review does not re-score the superseded spectator-product receipt.

**Verdict:** **MAJOR REVISION** — the action-level finite quantum construction is real and the old product-witness blocker is closed, but two advertised scope/gate claims are wider than the object actually built.

**Counts:** **0 BLOCKER / 2 MAJOR / 4 MINOR / 2 NIT**.

## 1. Independent reproduction

I ran the frozen receipt twice without changing the tree:

- `PYTHONHASHSEED=424242 python3 v10/code/d34c_nse_quantum_history_exact.py`
- `PYTHONHASHSEED=919191 python3 -O v10/code/d34c_nse_quantum_history_exact.py`

Both executions exit zero, print 10/10, and hash to

```text
a7cee72762f4244a57b5a698b3eb7172c8d1826bfa52effe37625b1e4c843720
```

This equals the committed output and §15.  The implementation uses exact `Fraction`/`Q(sqrt(2))` arithmetic throughout the quantum calculation.  I found no float, tolerance, numerical eigensolver, stochastic gate, or hash-order dependence.

## 2. Independent mathematical rebuild

### 2.1 Diamond, Gram functional and explicit path record — confirmed

For the first interaction, the initial source and path each contribute `1/sqrt(2)`, while the final path Hadamard contributes the third `1/sqrt(2)`.  The branch amplitude is therefore magnitude `1/(2 sqrt(2))` with sign

```text
(-1)^[p(1+s+o)].
```

Hence

```text
D((s,p,o),(s',p',o'))
 = 1/8 delta_ss' delta_oo'
   (-1)^[p(1+s+o)+p'(1+s'+o')].
```

Each fixed `(s,o)` block is `1/8 [[1,eta],[eta,1]]`, so its eigenvalues are exactly `(1/4,0)`.  The full matrix is a normalized rank-four Gram matrix.  Coherent path summation gives `(P00,P01,P10,P11)=(0,1/2,1/2,0)`; diagonal path reading gives four `1/4`s.  The exact row reduction now genuinely returns rank four.

The replacement no longer masks the path functional by assignment.  Appending the orthogonal `|p>` receiver to each already resolved branch constructs a Gram matrix equal to the masked functional.  That construction is algebraically equivalent to copying `P` to a fresh receiver at the path cut and then excluding that receiver from later support.

### 2.2 Actor history census and conditional factors — confirmed

The exact A-initiated history masses are:

```text
depth 1:  b=1/4, i(A,B)=1/4, n=1/2.

after b:  bb=1/16, bi(A,B)=1/32,
          bi(A,A/1)=1/32, bn=1/8;
after i:  ib=1/16, ii(A,B)=1/16, in=1/8;
after n:  nb=1/8, ni(A,B)=1/8, nn=1/4.
```

These are ten distinct depth-two histories, sum to one, and restrict to the three depth-one masses.  In particular, the post-birth interaction total `1/4` is correctly split into two target-conditional masses `1/8+1/8`; I found no conditional/unconditional factor confusion.

The quantum row census is also correct: `1+8+1=10` at depth one and `18+80+10=108` at depth two.  Every depth-two row maps to exactly one independently constructed depth-one fine branch through its first event, first mailbox state and first internal `(s,p,o)` alternative.  The exact incidence calculation really does return the independently built `10 x 10` functional; this is not the former `diag(mu) tensor D` identity.

### 2.3 Action operations, D24 birth and interaction interference — confirmed

The classical event label now selects an operation on the actor carrier:

- idle leaves the carrier vector unchanged;
- birth applies the D24 controlled rotation `(c,s)=(4/5,3/5)` to the named fresh Ulam slot;
- interaction applies `CNOT(A,target)`, the path resolution, `CZ(A,path)`, `H(path)`, and output copy on the actual target.

All three carrier operations are isometries/unitaries on the preallocated finite carrier.  For initial `A=|+>` and fresh child `|0>`, D24 gives

```text
P(child=1 | birth) = (1/2)(3/5)^2 = 9/50,
P(birth and child=1) = (1/4)(9/50) = 9/200,
```

matching the receipt.  For the first interaction, multiplying the conditional diamond by actor mass `1/4` gives coherent durable cells `(0,1/8,1/8,0)` and diagonal-only cells `1/16` after summing the two path diagonals.  The old common spectator diamond is gone: birth and idle have one class row, while interaction alone creates the eight quantum alternatives.

### 2.4 Distributed flags, positivity and finite-prefix algebra — confirmed with scope qualifications below

`factorized_flag_inner` is the product-basis Kronecker inner product over actor mailbox strings.  Birth and interaction copy the same event token to the two touched actor factors; idle writes only A.  Because the unrecorded `p` value is excluded from the token, the two path rows inside a fixed durable `(s,o)` event can interfere.  Different kinds, targets, predecessors, or durable `(s,o)` values are orthogonal.  Multiplying the carrier Gram matrix by this block-equivalence kernel is exactly the Gram matrix obtained by tensoring the carrier vectors with the corresponding mailbox basis vectors, so strong positivity is sound.

The finite-prefix induction is also algebraically valid under its stated hypotheses if `F_e` means the **full flagged event isometry**: preparation-independent `q_e`, `F_e^dag F_e=I`, mutually orthogonal recorded-event ranges, exhaustive internal class operators, and `sum_e q_e=1`.  Then exhaustive extension gives `sum_e q_e F_e^dag F_e=I`, and iteration proves finite-prefix restriction.  It does not supply the missing timed/direct-integral law, as §15 correctly states.

## 3. Major findings

### M1 — “Incoming remote receptions are coarse-grained” is not implemented

The code enumerates only rings initiated by A.  It does not enumerate, integrate, or sum any event initiated by B (or a later child) that passively touches A before A's first or second ring.  Such events are not harmless hidden labels: the declared interaction operation for an incoming `i(B,A)` acts on A's quantum carrier, and the reception also changes the predecessor structure of A's next visible event.

Therefore the implemented object is not yet the pushforward of the D34b actor process onto A's first-two-own-rings subalgebra.  It is the **A-initiator skeleton conditioned on/constructed with no interleaved incoming receptions**.  Calling the missing events “coarse-grained” does not perform that coarse graining.

This affects the receipt docstring, C8's headline, §14.1, §15.1 and the maximum noun wherever they call the object a genuine coarse subalgebra of the D34b actor law.  It does not invalidate the finite quantum circuit or the abstract induction theorem.

**Required repair — choose one honestly:**

1. narrow the noun to an `A-INITIATED, NO-INCOMING-RECEPTION DEPTH-2 SEWING WITNESS`, explicitly conditional rather than a D34b marginal; or
2. construct the actual marginal by including the possible incoming receptions and their quantum operations/predecessors and summing them.  Because an unbounded number can interleave before two A rings, this second route needs an analytic clock marginal or a declared finite-time/finite-incoming cutoff; it cannot be repaired by adding one extra branch.

An acceptable intermediate theorem could instead prove the action-level restriction for an arbitrary input state at each A ring and state that incoming receptions are absorbed into that input, but that would still not be the claimed full cylinder pushforward.

### M2 — The pinned remote **actor** factor gate is still an abstract-channel surrogate

The action-level branches repair the local sewing, but the remote part of C8 does not construct a second D34c actor.  `product_flagged_channel` reuses C6's unrelated one-qubit `(I,X,Z)` test channel, and `disjoint_commute` checks only tensor placements of those same test unitaries.  It never composes two D24/interaction/idle actor instruments, never uses the distributed mailbox tokens, and never compares the two serializations of actual disjoint actor events.

Thus the general tensor identity is correctly demonstrated, but §14 gate 9 — “construct a disjoint quantum actor factor” — and C8's action-level remote wording are not earned by the receipt.  This is not a hidden product defect in the local 108→10 object; it is an unfulfilled locality/order-gauge gate attached to that object.

**Required repair:** either construct a small disjoint `P,Q` actor pair with the same event operations and factorized mailboxes, then gate both event orders, the joint functional and the A marginal; or re-label the present row as the abstract tensor-factor lemma and leave action-level remote sewing open.

## 4. Minor findings

### m1 — Actual actor Kraus completeness is inferred, not gated at operator level

The repair pin asks for local-degree Kraus completeness at `m=1,2`.  The code gates the scalar identity

```text
1/4 + m(1/(4m)) + 1/2 = 1
```

and checks restriction on the chosen branch vectors.  It does not directly verify the actual D24/target-interaction/idle operator identity on the carrier basis.  The theorem makes the inference sound because each operation is unitary, but the advertised exact operator gate is absent.  Add an operator/basis-action certificate for `m=1,2`, or state that this row is analytic rather than receipt-computed.

### m2 — The explicit path receiver is equivalent but not literally the promised circuit gate

`append_path_receiver` tags each finished branch by its history label `p`; it does not build a five-qubit state, apply `CNOT(P,Q)` at the intermediate cut, and separately check that every later operator excludes Q.  The result is mathematically equivalent and the Gram matrix is correct, so no numerical claim falls.  For the exact wording “explicit receiver/copy isometry and later support exclusion,” construct the five-qubit circuit or narrow the description to an exact orthogonal receiver embedding.

### m3 — Mailbox injectivity is checked in only one direction

`flag_factor_ok` proves that one mailbox key cannot represent two durable physical signatures.  It does not explicitly prove that all rows with the same durable signature produce the same mailbox key, nor does it gate the product-basis vectors themselves.  Both facts follow from `write_event_flag` in this small census, but the promised “injectivity modulo p” gate should compare the two partitions for equality.

### m4 — Expected census/cardinality and incidence structure are printed, not fail-closed

`actor_counts=(3,10,10,108)` is included only in the detail string.  C8 does not require equality to that tuple, and it does not explicitly gate one unit entry per incidence column and nonempty coverage of every depth-one row.  The current object has the right counts and map, but these are load-bearing pre-registered numbers and should be Boolean gates.

## 5. Nits

1. “Idle is identity” should consistently mean identity on the **carrier**; the total event isometry also appends an idle flag and therefore is not the identity on the declared total ontology.
2. “Birth and idle contain no spectator diamond” is best phrased as “birth and idle create no diamond class alternatives.”  The universal finite carrier still contains untouched preallocated path/output ancillas, which are benign spectators.

## 6. Claim-by-claim disposition

| Claim | Disposition |
|---|---|
| Exact `Q(sqrt(2))` implementation and reproducibility | **PASS** |
| Diamond amplitudes/formula, normalization, rank and strong positivity | **PASS** |
| Explicit orthogonal path-record functional | **PASS**, wording repair m2 |
| Exact A-initiated depth-1/depth-2 census and weights | **PASS** |
| D24 birth probability `9/200` unconditioned | **PASS** |
| Interaction coherent/diagonal signature | **PASS** |
| Classical shadows equal actor-skeleton masses | **PASS** |
| Distributed mailbox Gram/orthogonality | **PASS**, gate hardening m3 |
| `108->10` exact restriction | **PASS** for the implemented no-incoming actor skeleton |
| Old spectator-product defect removed | **PASS** |
| Actual D34b A-local marginal with incoming receptions coarse-grained | **FAIL / M1** |
| Actual disjoint actor factor and order-gauge gate | **FAIL / M2** |
| Algebraic finite-local-prefix induction under stated isometry hypotheses | **PASS** |
| Full timed D34b quantum law, graph-sector superposition, infinite extension | Correctly **NOT CLAIMED** |

## 7. Adjudicated maximum wording

At the frozen commit, the strongest fully supported wording is:

> **A-INITIATED, NO-INCOMING-RECEPTION DEPTH-2 ACTOR/QUANTUM SEWING WITNESS:** the selected birth/interact/idle actor operations form an exact, non-product, strongly positive finite history functional; its classical shadow, interaction interference and `108->10` prefix restriction are correct.  The finite-local-prefix induction holds for the chosen flagged-isometry family.  The actual D34b marginal over incoming receptions and an action-level disjoint-actor factor remain open.

If M1 is repaired by honest re-scoping and M2 by either construction or explicit deferral, the quantum-mathematics stream can move to delta review without reopening C1–C7 or the local 108→10 computation.
