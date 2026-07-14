# D34d round 1 — independent locality/clock architecture hostile review

**Target:** baseline commit `0119f4e`. **Verdict:** REJECT AT STATED
LOCAL/D34b WIDTH; THE GENERIC PREDICTIVE-STATE AND CLOCK WITNESSES SURVIVE.
**Count:** 1 BLOCKER / 5 MAJOR / 4 MINOR / 2 NIT.

## Reproduction and audit scope

The classical D34d receipt reproduced byte-for-byte under fresh
`PYTHONHASHSEED=541,9001`; both outputs have SHA-256
`1b75e1628cc5ab09f29592036d0f29a4032ec4cde3dcb3300efa9dbca615f386`
and the internal summary hash remains
`31e924d568af3bc59f7cd08fbaefe2e6bb1e7c357d1e7951e0312ab94810cbc3`.
All seven printed gates are true of the objects actually coded.

The terminal D34b receipts were also rerun rather than inferred from D34d.
Under fresh salts they reproduce the committed output hashes
`47993cbcaf3d3a719ef868fd6a4d122b9b2d46e23555133d886185f79358740c`
(exact Harris receipt, 7/7) and
`59d28bc5db03cca5e30a81eaed09c1c42d7e51541f6ea7c3d078c9d59a75c2a3`
(actor reference, 8/8). I inspected the repaired D34b three-object split, the
actual actor state and stopping rules, passive reception, the D34c bounded
event-record repair, and the remaining timed-quantum/incoming-marginal opens.

No printed D34d fraction is false. The rejection is about which mathematical
object those fractions establish.

## BLOCKER

### B1 — the claimed *local* predictive state is not constructed

The note's earned statement uses “the full current distributed actor
configuration” (`live graph/tips, carrier state and ... mark law`). That is a
perfectly good **global configuration of a locally generated interacting
process**. It is not yet an “appropriately enlarged local state” for one
record, one collar, or one operational boundary. Calling the data distributed
does not prove that any bounded/local subset of it screens a record's future.

P4 proves only the elementary tensor identity for two arbitrary independent
`2x2` chains. It therefore establishes independence of a truly disconnected
factor, already earned more strongly and pathwise by D34b A4. It says nothing
about causally connected state outside a proposed collar. The actual D34b
partner law supplies an exact counterpressure: if B's only eligible neighbor
is A, B sends an incoming interaction to A at rate

```text
1 * (interaction mass 1/4) * (target share 1) = 1/4.
```

After B births an unsealed child C, while A's own tip and private clock state
are unchanged, B's eligible degree is two and the incoming B-to-A rate is

```text
1 * (1/4) * (1/2) = 1/8.
```

Thus A's current tip/record alone is not predictive. A one-step boundary must
at least retain B's eligible degree; arbitrary-horizon prediction may require
a growing connected boundary or a belief/process state over it. D34d neither
constructs that boundary state nor proves it finite, record-carried, or closed.
At an A-local stopping time the unobserved neighbor configuration can remain
random, so its conditional belief—not just the visible A tip—can be the needed
predictive memory.

This is not repaired by complete-history Markovization: the full global Harris
configuration is the current-state version of the same trivial escape. The
central desired reconciliation can be stated only after distinguishing:

1. a global configuration on which the Harris process is Markov;
2. a generator whose individual updates are actor/edge local; and
3. a local observer's sufficient boundary state, which is not yet shown to be
   finite or smaller than the connected component.

Until item 3 is proved or explicitly withdrawn, the combined D34b–D34c
`PREDICTIVE-STATE ... CHARACTERIZATION` noun exceeds the receipt.

## MAJOR findings

### M1 — P4/P5 are analogies, not gates on the repaired D34b actor object

P4 introduces fresh matrices `LOCAL_TRANS` and `REMOTE_TRANS`, then separately
hardcodes `own_ring_birth=1/4` and the census shares `1/2,1/4`. P5 checks one
exponential survival ratio, uniform `1/k` race rows through `k=8`, and the
three-number mark vector. It never constructs a D34b actor, Ulam child,
birth-tree adjacency, passive reception, receiver clock that is not reset,
wire predecessor, sealed/ineligible state, local stopping filtration, or typed
wire-DAG. Nevertheless its PASS line concludes that the chosen D34b actor
process closes.

The analytic conclusion is plausible for the **ideal complete Harris
configuration**, but the executable does not gate it. Reuse or independently
rebuild the D34b generator and state inventory. Gate conditionals at fixed
construction time, A's own-ring stopping time, and A-wire event stopping time
(which includes passive receptions), with fixed global depth retained only as
the negative control. The theorem should be a strong-Markov/independent-Poisson
increments argument, with the finite PRF/Decimal actor program kept as a
reference rather than as the memorylessness object.

### M2 — the common-rate “gauge” claim lacks the indispensable stopping scope

Common multiplication of all rates leaves the **embedded winner/order law at
fixed event depth** unchanged. It does not leave the D34b fixed-time law
unchanged. Even one clock has

```text
P(no ring by T) = exp(-lambda T),
```

and the D34b Yule population obeys

```text
E[N(T)] = N0 exp(lambda T/4).
```

Both change under `lambda -> c lambda` with `T` fixed. The correct equivalence
is a simultaneous unit conversion, schematically
`Law_(c lambda) at T = Law_lambda at cT`, or the fixed embedded/local-count
pushforward after time is erased. Section 3's unqualified “changes only units”
and P6's “untimed causal-DAG probabilities unchanged” are therefore false for
the actual D34b `G_T` object unless the horizon transformation is stated.

Likewise, a nonlinear monotone relabeling of an already realized set of times
preserves its order but transforms homogeneous exponential clocks into a
time-inhomogeneous hazard law. It is an order-coordinate fact, not invariance
of the stationary D34b measure. Freeze and gate an invariant table separating
fixed `T`, rescaled `T`, fixed local count, fixed global count, and the all-time
order skeleton.

### M3 — P6's serializer gate is tautological, and its relative-rate specimen
is outside the chosen family

`canonical_disjoint` simply assigns the same literal string to the two input
orders. No actor events or typed-DAG canonicalizer are executed, no predecessor
closure is rebuilt, and no orbit pushforward is independently checked. D34b
E4 and D34c's merge/disconnected-actor gates contain the actual structures;
D34d should call or independently reconstruct those objects rather than
replace them with a dictionary assertion.

The relative-rate lesson is mathematically correct, but D34b's chosen family
has unit rate on every live actor and explicitly left heterogeneous rates
untested. An actual heterogeneous D34b extension would give, for A's marked
interaction and B's marked birth sharing B's wire,

```text
(lambda_A,lambda_B)=(1,2): masses 1/48 and 1/24,
(lambda_A,lambda_B)=(2,2): masses 1/32 and 1/32,
```

because each marked pair contributes `1/16` times the relative-order race
probability. That would prove relative rates change physical shared-wire
histories. The current abstract `A-first` numbers do not instantiate the
chosen D34b grammar, and heterogeneous rates cannot simultaneously be called
part of the chosen family and a previously untested variant.

### M4 — the renewal control proves age necessity only, not actor-process
sufficiency

The uniform `[0,2]` calculation correctly shows that the next-half-unit ring
probability is `1/4` at age zero and `1/2` at age one. This proves that the
age-free state is insufficient for that single renewal clock. It does not
prove the pinned sufficiency direction for an interacting renewal actor
process. With births, each new actor needs an age/birth epoch; after its own
ring its renewal clock resets; after passive reception it does not; and local
conditioning may leave a distribution over unobserved neighbor ages. Depending
on how waiting times are sampled, the closing state is an age vector plus the
known renewal law, or the actual residual/deadline variables. Gate the full
transition kernel and both reception/reset cases. Narrow the present result to
`single-clock age-necessity witness` until that is done.

### M5 — “record-carried” has no capacity/storage audit

D34c established one fresh event factor per click with bounded local outcome
rank and bounded incidence arity; it explicitly did **not** bound Ulam
identifier bit length. The D34b actor implementation additionally stores an
incident `neighbors` set whose size is unbounded because a parent can birth
arbitrarily many children. P5's “live graph/tips” state therefore cannot be
silently identified with one finite-capacity record.

Inventory every predictive-state field and label it: bounded event outcome,
bounded incidence endpoint, unbounded identifier, unbounded incident-edge
census, actor tip, quantum carrier, clock age/deadline, or observer belief.
Either represent adjacency as a distributed web of bounded edge/event records
and prove that the update/query rule is support-local, or retract any inference
that the full configuration is a bounded record-carried Markov state. Total
web finiteness at finite `T` is not a uniform per-record capacity bound.

## MINOR findings

1. **Two local counters are conflated.** A's private own-ring index does not
   equal the number of events on A's causal wire because incoming receptions
   append wire events without advancing A's clock. Define both filtrations and
   stopping times wherever “local actor count” is used.
2. **Ideal and reference states need separate wording.** Memorylessness belongs
   to the ideal exponential source. The finite PRF/Decimal actor reference
   stores absolute `next_ring` deadlines and is neither exactly exponential nor
   memoryless. It can close trivially if those deadlines are included.
3. **The “minimal predictive state” gate partitions ontic hidden states, not
   observed-history posterior states.** For the visible HMM, the operational
   predictive state is the posterior belief modulo future equivalence; the
   reachable belief set need not be the three hidden labels or finite. This
   reinforces rather than falsifies D34d's warning, but P2's label is too broad.
4. **Construction time remains a common external parameter.** Erasing
   incomparable serialization does not establish relativistic locality,
   foliation independence, or proper time. The note correctly says proper time
   is not derived; add that no local-clock synchronization/gauge theorem has
   been proved either.

## NIT

- The file header still says `Status: INVESTIGATION PIN (pre-receipt)` after
  adding provisional receipts and conclusions.
- `SINDEX` is unused; remove it or use it in the independently reconstructed
  transition checks.

## Exact repair prescription

1. **Freeze the state/filtration dictionary.** Name the global Harris state
   `Z_t`, its local update supports, the observer-A filtration (including
   passive receptions), the A-own-ring and A-wire-event stopping times, and a
   candidate collar/boundary predictive state. Do not call `Z_t` local.
2. **Prove the global theorem honestly.** From independent Poisson increments
   and fresh marks, prove that the ideal complete D34b configuration is strong
   Markov and that its generator is a sum of support-local actor terms.
3. **Decide the actual local theorem.** Gate the exact B-degree witness
   `1/4 -> 1/8`; then either construct a boundary/belief state that screens all
   licensed A futures, with its size/access scope printed, or state that only
   full connected-component/global configuration closure is currently known.
4. **Replace P4/P5 with D34b objects.** Include Ulam birth, partner selection,
   passive reception/no-reset, typed predecessor merge, disconnected coupling,
   and the four declared stopping scopes. Carry the analytic theorem; use exact
   finite enumeration/reference runs only as regression.
5. **Complete the renewal comparison.** Build at least a two-actor birth plus
   passive-reception renewal specimen and prove that graph+tip+age/residual
   variables close its future kernel. Print a same-visible-state/different-age
   necessity witness and an equal-full-age-state/all-future sufficiency gate.
6. **Replace P6 by a real typed-DAG orbit gate and a transformation table.**
   State and test: serializer orbit invariance; common affine unit conversion
   with transformed horizon; failure at fixed `T`; pathwise order preservation
   but law change under nonlinear time maps; and an explicitly named
   heterogeneous-rate D34b variant for the shared-wire split.
7. **Carry the capacity ledger.** Separate bounded event rank/arity from
   unbounded graph degree, identifier length, boundary width, and posterior
   memory. This determines whether “record-carried” is literal or only
   distributed-system notation.

After these repairs, the strongest possible positive classical result would be
valuable: **the chosen D34b universe is a Markov process on its complete
distributed Harris configuration with support-local generator terms, while a
declared record projection is non-Markov exactly when it fails to retain the
needed boundary/belief state.** What is not yet earned is that this boundary is
finite, bounded-capacity, or attached to each record independently.

## Surviving verdict

`GENERIC FINITE-HMM LUMPABILITY/NON-MARKOV WITNESS + SINGLE-CLOCK
EXPONENTIAL/RENEWAL AGE WITNESS + ORDER/RATE TOY WITNESS`.

The D34b terminal classical measure and D34c finite typed-DAG compatibility
results are not damaged. D34d's new conceptual target is good, but the local
actor theorem and clock-gauge characterization remain open at baseline
`0119f4e`.
