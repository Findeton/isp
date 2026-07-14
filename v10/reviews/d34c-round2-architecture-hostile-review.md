# D34c round 2 — independent actor/history/locality architecture hostile review

**Frozen target:** commit `d634f3d` (`v10 d34c repair: sew quantum operations into actor events`).  
**Review stream:** actor/history measure, locality, mailbox factorization, construction-order gauge, and projective-prefix architecture.  
**Verdict:** **REJECT AT THE STATED D34b-COARSE-SUBALGEBRA WIDTH; ACTION-LEVEL CORE SURVIVES.**  
**Count:** **1 BLOCKER / 3 MAJOR / 3 MINOR / 2 NIT.**

## 1. Independent reproduction

I reran `code/d34c_nse_quantum_history_exact.py` under fresh `PYTHONHASHSEED=77` and `31337`. Both runs returned 10/10 and were byte-identical to the committed output:

```text
a7cee72762f4244a57b5a698b3eb7172c8d1826bfa52effe37625b1e4c843720
```

There are no false printed fractions, branch counts, ranks, or hashes in the replacement receipt. Independently reading the enumerator gives exactly the advertised private A-initiated tree: three first-ring paths; after first birth four extensions and otherwise three, hence ten depth-two paths. The changing target weights after birth are `1/8+1/8`; Ulam names `A/1,A/2` are parent-local; the mass-one and `2->1` arithmetic is correct.

Most importantly, the round-1 spectator defect is genuinely repaired **inside this ten-path object**. Birth applies `acry(A,child)`, idle applies identity, and interaction applies the diamond to `A` and the named target. The depth-two branches are rebuilt by composing both event operations. `d_actor2` is not `diag(mu)` tensored with one unchanged diamond.

## 2. BLOCKER — the omitted incoming events are not a coarse graining of D34b

The receipt calls its object the A-local stopping algebra with “incoming remote receptions coarse-grained.” The code does not perform that coarse graining. It deletes every ring initiated by `B` or any other actor before constructing either the classical or quantum histories.

This matters at positive D34b measure. Before A's first or second own ring, B may ring any number of times. In particular, B may interact with A. Such an event:

- writes a passive-reception token into A's mailbox;
- advances the last event on A's wire without advancing A's own clock/ring;
- can supply a distinct target-wire predecessor to A's next event;
- under the proposed symmetric action family, applies a quantum operation to A and can change the class operators for A's later birth or interaction.

None of those alternatives is enumerated or summed. Every first A event in the replacement has empty predecessors and an untouched A mailbox. Every non-A ring counter remains zero. This proves only that **targets of A's outgoing interactions are passive**. It does not model A as a passive receiver, and it does not prove a marginal obtained by forgetting incoming events.

There is a sharp counter-cylinder: `i(B,A)` before A's next own ring has positive probability in D34b. The physical local projection contains the B event in A's mailbox/wire. The replacement has no branch carrying it. If one chooses an observation algebra that forgets the token, the incoming quantum operation must still be integrated; replacing it by no operation is not coarse graining.

Therefore §14's “genuine coarse subalgebra of the D34b exemplar,” C8's “incoming remote receptions coarse-grained,” and §15/LEDGER #168's D34b actor-cylinder reading are not established. The word “remote” is also misleading here: B is an adjacent, causally coupled actor, not a disconnected remote component.

**Disposition:** either build the actual marginal, or narrow the noun to **`A-INITIATED TWO-RING ACTION-SEWING EXHIBIT`**, explicitly conditional on/suppressing all non-A-initiated events. Without one of those changes, C8 is not fail-closed at its printed scope.

## 3. MAJOR findings

### M1 — the finite-prefix induction theorem uses the wrong completeness typing

The exact `108->10` equality is a real state-level restriction result for the chosen initial vector. It does not by itself prove the advertised all-preparation induction.

The theorem in §15.4 writes recorded alternatives `e` with preparation-independent weights `q_e` and isometries `F_e`, then uses

```text
sum_e q_e F_e^dagger F_e = I.
```

For an interaction there are three different indices:

- `x`: the classical D34b option `(kind,target)`, with fixed weight `q_x`;
- `r=(s,o)`: the durable quantum result, whose probability depends on the preparation;
- `p`: the unrecorded alternative, which must be summed coherently.

The durable-result class operators are not individually isometries. The required object is

```text
K_(x,r) = sum_p C_(x,r,p),
W_x = sum_r |mailbox(x,r)> tensor K_(x,r),
sum_r K_(x,r)^dagger K_(x,r) = I,
sum_x q_x W_x^dagger W_x = I.
```

That is the correct local closure/isometry and restriction lemma. It also supplies the missing bridge from the abstract Busch result to the **actual** birth/interaction/idle family. C6 currently proves Busch form only for the separate `I,X,Z` test maps. The actor receipt checks one reachable state tree, not the operator identities above.

The theorem is likely repairable—the interaction circuit is unitary and its exhaustive projectors have the needed identity—but the stated proof does not carry it. Until the operator-level identity is written and gated, the “algebraic finite-local-prefix induction” and actual-family NSE conjunct are unearned.

### M2 — no actor-level construction-order gauge or remote actor factor is tested

All actual C8 events are initiated by A, so every pair is comparable on A's wire. The only disjoint-commutation test uses the abstract two-dimensional `I,X,Z` controls from C6. The “remote quantum factorization” is likewise a deliberately constructed product of those abstract flagged channels on one product input.

It does not test:

- two actual D24 birth/diamond actor operations on disjoint Ulam carriers;
- their actor-local mailbox writes in both serializations;
- equality after forgetting serialization;
- a D34b disconnected source-family measure;
- remote marginal invariance for the actual actor channel (or on an arbitrary entangled input).

Thus the exact internal-circuit `a/b` commutation survives, but the actor-history construction-order gauge and remote actor-factorization clauses of repair gate 9 remain open.

### M3 — predecessors never exercise the shared-wire merge they are claimed to represent

The predecessor routine is syntactically correct, but the enumerated tree never presents it with two distinct incoming wire tips. On a second A event, A's prior tip and the target's tip are either absent or the same earlier A-initiated interaction. Consequently every nonempty predecessor tuple is just `("A#r1",)`.

No branch has the physically decisive form

```text
last(A) = A#r1, last(B) = B#r1,
i(A,B) predecessors = {A#r1, B#r1}.
```

That is the mailbox/causal-diamond case which distinguishes a real shared event from a one-thread sequence. The current receipt proves token duplication to a passive target, not merging of independently evolved actor histories. This gap is related to the blocker but survives even as a minimum finite architecture gate: one independently initiated B event followed by `i(A,B)` would exercise it exactly.

## 4. MINOR findings

1. **“Complete” needs its full qualifier everywhere.** The `3/10` tree is complete for A's **private initiated mark stream through two A rings**, given the graph updates caused by A itself. It is not complete for A's local physical wire, A's stopped causal past, or the full D34b local-ring marginal.

2. **“Passive reception” is one-sided at receipt width.** The code exactly shows that B or a child does not advance its ring counter when A initiates an interaction and that the shared token is written to the target. That narrow result should be called “outgoing-target passive reception.” Incoming passive reception by A is absent.

3. **The mailbox tensor product is a sound finite Gram representation, but its coherent writer is implicit.** Multiplying actor-mailbox Kronecker deltas is equivalent to orthogonal local flag bases at this finite width, and the injectivity test correctly leaves `p` unrecorded. For the NSE/induction theorem, however, the controlled isometry that coherently copies the orthogonal `(event,s,o)` token into both blank mailboxes should be included in `W_x`, rather than inferred only from the inner-product rule.

## 5. NIT findings

1. `all_m_identity` evaluates `m=1..64`; the prose calls it an algebraic all-`m` result. The identity is trivial for every positive integer `m`, but the one-line symbolic proof should carry that wording rather than a finite loop.

2. The explicit Q receiver is mathematically equivalent to copying `p` immediately after its projector because later operators exclude Q. The code implements the equivalent branch embedding at the end. Calling it an explicit receiver is defensible, but the narration should say “branchwise equivalent copy isometry” unless the five-qubit intermediate circuit is literally built.

## 6. Claim-by-claim disposition

| Claim | Disposition | Evidence |
|---|---|---|
| Spectator product removed | **PASS** | Event labels select and compose distinct carrier operations; birth/idle contain no diamond alternatives. |
| A-private depth-one/two mark tree | **PASS** | Exact `3/10` enumeration, mass one, degree update, Ulam children and `1/8+1/8`. |
| Full D34b A-local stopped/coarse algebra | **FAIL / BLOCKER** | Positive-measure incoming rings/receptions are omitted, not marginalized. |
| Outgoing target is passive | **PASS, narrow** | Target mailbox changes while every non-A ring counter stays zero. |
| General passive reception | **NOT TESTED** | A is never a passive receiver. |
| Physical predecessor/diamond merge | **NOT TESTED** | No target has a distinct independently generated prior tip. |
| Factorized mailbox inner product/injectivity | **PASS at enumerated width** | Product of actor deltas; same mailbox implies same durable history; `p` remains unflagged. |
| Classical shadow | **PASS for the ten-path tree** | Every block sums to the exact private-stream mass. |
| Genuine sequential `2->1` restriction | **PASS for the chosen initial state/tree** | Second operation is composed; exact `108->10`. |
| All-preparation finite-prefix induction | **MAJOR REPAIR** | Durable quantum outcomes and coherent internal paths are not correctly typed in the theorem; actor operator completeness ungated. |
| Actor construction-order gauge | **NOT TESTED** | Actual C8 events all share A; surrogate `I,X,Z` test only. |
| Actual remote actor factorization | **NOT TESTED** | Surrogate product channel, not D34b actor events/mailboxes. |
| Full timed/direct-integral, profinite, graph-superposition ceiling | **PASS** | These remain explicitly open. |

## 7. Minimum repair

### Exact repair route

1. Add at least one independently initiated B event and the reception cylinder `i(B,A)`; verify that A's ring counter is unchanged while its mailbox, last-wire tip and quantum carrier are updated.
2. Add the two-tip merge `A#r1`, `B#r1` followed by `i(A,B)` and require both predecessors, the shared token on both mailboxes, and identical results under the two allowed serializations of the incomparable first events.
3. If retaining “coarse-grained incoming receptions,” actually sum the connected actors' intervening histories and their quantum maps. A bounded exact observation functor or a declared conditional cylinder is acceptable; deletion is not.
4. Replace the induction paragraph by the `C_(x,r,p) -> K_(x,r) -> W_x` theorem above. Gate `W_x^dagger W_x=I` as an operator identity for idle, birth, and interaction on arbitrary inputs and both degree-one/two targets.
5. Build a genuinely disjoint second actor component using the same birth/interaction/idle family. Apply one actual event in both orders, compare carrier state plus factorized mailboxes after serialization is erased, and gate the actual tensor channel/marginal identity.

### Honest narrowing route

Without those additions, retain the exact receipt but rename its maximum result:

> **A-INITIATED TWO-RING ACTION-SEWING EXHIBIT PASS — on the private initiated mark tree with non-A events suppressed; state-level sequential restriction exact.**

Do not call it the D34b local stopping-algebra marginal, do not say incoming receptions were coarse-grained, and defer the finite-prefix/NSE theorem until the operator instrument is written correctly.

## 8. Bottom line

The replacement is scientifically substantive: **the actor labels now do the quantum work, and the old independent spectator subsystem is gone.** The exact ten-path action-level object, its mailbox Gram law, classical shadow, and state-level sequential restriction survive hostile inspection.

What does not yet survive is the bridge from that object to the D34b local actor process. The missing piece is precisely the one the actor architecture makes unavoidable: other actors can touch A between A's own rings. Until those receptions are either included or genuinely integrated, the result is a controlled initiated-stream exhibit rather than a coarse local history law.
