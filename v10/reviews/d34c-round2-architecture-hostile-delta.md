# D34c round 2 architecture — hostile delta review

**Frozen target:** commit `cf33fe2` (`v10 d34c repair: bounded event records and typed DAG sewing`).  
**Compared against:** `d34c-round2-architecture-hostile-review.md`.  
**Verdict:** **CORE DELTA-CLEAN / PASS WITH SMALL REPRESENTATION CORRECTIONS.**  
**Count:** **0 BLOCKER / 0 MAJOR / 3 MINOR / 3 NIT.**

The maximum scientific noun is accepted at its new conditional width:

> **FINITE TYPED-DAG ACTOR/QUANTUM SEWING WITH BOUNDED EVENT-OUTCOME FACTORS**, plus the conditional finite-down-set theorem for the chosen operation family.

It is not, and is nowhere newly narrated as, the timed operator-valued D34b measure or the infinite incoming-event marginal.

## 1. Independent reproduction

Fresh runs under `PYTHONHASHSEED=991` and `424242` returned 14/14 and reproduced the committed output byte-for-byte:

```text
8349459eb2ff077578f8a9d08a761b12b98997430d9e1fd2134af83a49270cd0
```

I found no false exact fraction, branch count, matrix size, rank, closure identity, carrier probability, predecessor set, or hash.

## 2. Delta disposition of the round-2 findings

### The incoming-event blocker is closed by honest scope plus an explicit specimen

The old `3/10`, `10/108` tree is now called exactly what it is: a **consecutive-A-initiated conditioned specimen with non-A events suppressed**. C8 and §§16–17 no longer call it a marginal or claim that incoming events were coarse-grained.

Separately, C10 constructs `i(B,A)` with positive actor semantics:

- B's ring advances and A's does not;
- both wire tips become `B#r1`;
- the next A event inherits `B#r1` as predecessor;
- the actual B-to-A interaction changes A's carrier from the declared zero baseline to probability `1/2` of value one;
- one fresh record factor is allocated.

This does not sum the unbounded incoming marginal, and the note explicitly says so. That is the correct disposition of the former blocker.

### Two independent tips and physical merging are now real

C10 builds independent `A#r1` and `B#r1` tips followed by `i(A,B)`. The merged event has the exact direct-predecessor set `{A#r1,B#r1}`. Swapping the two incomparable idles leaves the actor state, locally named typed DAG, fresh records and class branches identical after auxiliary list order is erased.

The actor IDs are lineage/local-ring IDs (`initiator#local-ring`), not a universe event counter. Sorting those IDs in `canonical_graph` is a read-only canonical representation; it is not consulted by `actor_step` to choose or advance an event. I find no hidden global scheduler or global normalization in this construction.

### The actual-family instrument theorem is repaired

C9 now carries the correct types:

```text
C_(x,r,p),
K_(x,r) = sum_p C_(x,r,p),
W_x = orthogonal-record sum over r,
W_x^dag W_x = sum_r K_(x,r)^dag K_(x,r) = I.
```

The exact operator closures are verified on an arbitrary four-carrier input sector, so entanglement with the other declared input carriers is included. Birth, idle, and interaction with either existing target close to `16x16` identity. The degree-one and degree-two scheduler rows close exactly, and the all-positive-degree step is the algebraic identity `m*(1/(4m))=1/4`.

This supplies the operator-level premise that the prior state-specific `108->10` calculation lacked. The individual durable-result maps are explicitly shown not to be isometries, so the review's typing correction is genuinely load-bearing.

### The actor-level gauge and disconnected factor are repaired

C11 uses the actual operation family: an A-to-B diamond interaction on one component and a P-to-P/1 D24 birth on a disconnected component. The full maps commute on all 64 carrier basis states; all eight interaction class branches agree in both orders; typed actor/record states agree; and the remote unitary leaves the complete local diamond functional equal to `D_diamond`.

This is no longer the rejected `I/X/Z` surrogate.

### The finite-down-set theorem is conditional, not extrapolated from four examples

The four specimens do not by themselves prove “every finite DAG.” The proof does not rely on that inference. Its actual premises are:

1. a supplied finite typed wire-DAG/classical sector;
2. preparation-independent normalized scheduler weights;
3. one fresh orthogonal bounded event-outcome factor per event;
4. the operator identity `sum_x q_x W_x^dag W_x=I`;
5. commuting maps for incomparable disjoint touched-carrier supports.

Given those premises, Gram positivity and extension/restriction by induction are standard finite algebra. The exact specimens validate the nontrivial premises for the chosen birth/idle/interaction family, including reception, merging and a disjoint pair. The theorem is therefore accepted as a **conditional finite theorem**, not as the missing timed measure.

## 3. Remaining MINOR corrections

### m1 — bind unrecorded internal labels to event IDs before canonical comparison

The physical records are correctly keyed by local event ID, but `branch_vector_map` and `durable_signature` still carry `row["internals"]` as a tuple in execution order. The tested merge evades this because its incomparable alternatives are both `None`; C11 has only one interaction alternative and binds it manually.

For two incomparable interactions, auxiliary serializations would produce `(h_A,h_P)` versus `(h_P,h_A)` even though the physical class history is the same up to event-keyed permutation. This does not alter the computed Gram law, but it leaves an auxiliary order in the class-label helper.

**Repair:** store/canonicalize internal alternatives as `tuple(sorted((event_id, internal), ...))`. Keep `p` absent from durable records but event-key it in the fine class-history label.

### m2 — “bounded links” needs bounded-arity precision

The code exactly gates a six-symbol outcome alphabet and at most two direct predecessors. The grammar also implies at most two immediate successor wire links because each event touches at most two wires, but that direction is not gated or stated in the receipt.

Moreover, Ulam addresses and local ring ordinals grow in description length. They are structural node/edge identities, not members of the six-symbol evidence factor.

**Repair:** say **bounded local outcome rank and bounded incidence arity**, not bounded total identifier bit length. Add the one-line wire lemma `in-degree <= 2` and `immediate out-degree <= 2` for this grammar, or gate it on the specimens and carry the general proof.

### m3 — state the support lemma behind “incomparable maps commute”

Fresh records being distinct is not alone sufficient for two operations to commute; their touched quantum carriers must be disjoint. In a valid wire-DAG, two events sharing an actor/carrier lie on the same wire and are therefore comparable, so incomparability implies disjoint touched-carrier support for this chosen grammar.

**Repair:** put that wire-support lemma explicitly into §17.6/C12. Then use “carrier-disjoint incomparable maps commute” rather than the potentially weaker “record-disjoint” phrase.

## 4. NIT corrections

1. The code comment at C8 still calls the old object an “A-local D34b actor cylinder/stopping algebra.” The executable output and note correctly call it conditioned; update the stale comment.
2. The module docstring still points only to the original §11/f861328 pin. Add the repair pin `§16`, commit `9cd9ac4`, so provenance matches the replacement.
3. C10 prints `P(A=1) 0->1/2`; the after-value is explicitly gated while the zero baseline is implicit in `basis(ADIM,0)`. Gate/store the baseline too, or narrate only the checked after-value.

## 5. Hidden-ledger and capacity audit

**No global commit ledger found.** The generator uses only initiator-local counters, local neighbor sets, current wire tips and fresh child ordinals. `canonical_graph` globally sorts a completed finite specimen only to compare representations; it neither chooses the next actor nor supplies a denominator.

**No growing record payload found at the earned scope.** Each click creates a new immutable six-state outcome factor. The total web grows by acquiring more records, while no old record's evidence alphabet grows. Typed incidence and Ulam identity remain outside that outcome factor. The minor precision above is necessary so “bounded record” is not misread as a uniform bound on the serialized address of every node in an unbounded web.

## 6. Timed/infinite claim audit

The following remain explicitly open in §17, LOG #170, LEDGER #170 and C13:

- timed operator-valued D34b measure;
- unbounded incoming-event marginal before an actor stopping time;
- direct-integral/infinite quantum extension;
- intrinsic untimed/profinite restriction;
- graph-sector superposition;
- derived weights, operations, basis or NSE;
- sealing, joining, geometry and nature's law.

I found no surviving current-tense claim that the complete timed D34b quantum law has been constructed.

## 7. Terminal recommendation

After applying the three representation/scope corrections above, I would stamp:

> **D34c FINITE TYPED-DAG COMPATIBILITY PASS — for the chosen birth/idle/interaction family, finite typed actor DAGs admit strongly positive, down-set-consistent quantum history functionals with fresh bounded-rank event outcomes; incoming reception, two-tip merging and actor-level construction gauge are explicitly realized. The timed D34b quantum measure remains open.**

The old spectator and false-marginal blockers are closed. No further architectural rebuild is required at the finite conditional width.
