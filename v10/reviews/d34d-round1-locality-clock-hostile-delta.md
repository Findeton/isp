# D34d round 1 — locality/clock hostile delta review

**Target:** repaired commit `b92b82b`, audited strictly against
`d34d-round1-locality-clock-hostile-review.md`.

**Verdict:** **CORE DELTA-CLEAN — 0 BLOCKER / 0 MAJOR / 2 MINOR / 2 NIT.**
The round-1 locality blocker and all five majors are closed. The remaining
items are scope/evidence cleanup; none changes a printed fraction, the repaired
theorem, or the withdrawal of a bounded local predictive state.

## Reproduction

Fresh-salt reruns were byte-identical to the committed data:

- D34d classical, `PYTHONHASHSEED=424242,8675309`:
  `43aa03a459bd05509998e0f770a97ed726982ab28fdcdbaf0735aadae3c4891c`,
  13/13, internal summary hash
  `9f9e59954bd1710e70c27d1fa6c5b285c50eec096dae21d433c04201092ac282`;
- D34d quantum, the same two salts:
  `e1990fe3a4dfbc44c83b4b49216df44ad9462dcb410c9c24c19dc4144c3884d1`,
  10/10, internal summary hash
  `cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0`;
- terminal D34b exact parent:
  `47993cbcaf3d3a719ef868fd6a4d122b9b2d46e23555133d886185f79358740c`,
  7/7;
- terminal D34b actor parent:
  `59d28bc5db03cca5e30a81eaed09c1c42d7e51541f6ea7c3d078c9d59a75c2a3`,
  8/8.

The parent A3 gate still independently confirms that passive reception leaves
the receiver's private ring, next deadline and next keyed mark unchanged. A4
still confirms pathwise disconnected-component invariance at fixed
construction time and fixed A-own-ring count, while rejecting fixed global
event depth as a locality criterion.

## Round-1 disposition

### Blocker B1 — CLOSED

The repaired work no longer equates the complete distributed configuration
with a finite local record state. It defines `Z_t` as the **complete global
Harris configuration**, proves/instantiates the generator as a sum of actor
terms, and explicitly states that a bounded all-future collar remains open.

The counterexample is now carried on the actual D34b grammar. B's incoming
interaction rate to A changes exactly

```text
deg(B)=1: 1 * 1/4 * 1   = 1/4,
deg(B)=2: 1 * 1/4 * 1/2 = 1/8,
```

after B births a child while A's tip and private actor row remain unchanged.
This establishes precisely what round 1 required: A's tip is insufficient,
and no bounded connected boundary is inferred from global Markov closure.

### Major M1 — CLOSED

P8–P9 replace the generic product/race analogy with an independently coded
D34b generator, Ulam birth, degree-split partner rates, wire tips,
predecessors, incoming reception, carrier update, disconnected component and
separate own-ring/wire/global counts. The analytic strong-Markov statement is
attached to the ideal Poisson/mark source, not to Decimal/BLAKE2. The terminal
D34b parent supplies the stronger pathwise fixed-time/fixed-local-ring checks.

### Major M2 — CLOSED

P11 and §9.2 now state the rate/time scopes correctly:

```text
embedded winner/order law under common scaling: invariant,
fixed numeric T:                              not invariant,
compensated horizon: Law_(c lambda,T)=Law_(lambda,cT),
nonlinear time relabeling: order preserved, homogeneous law changed.
```

The old unqualified fixed-time gauge reading is withdrawn. Construction time,
causal order and emergent proper time remain separate; proper time is not
claimed derived.

### Major M3 — CLOSED

P11 constructs actual D34b idle/birth/interact states and canonicalizes their
typed event/predecessor data. Disjoint A-idle/P-birth serializations agree in
both typed-DAG and complete state keys; shared-wire interaction/birth orders do
not. The relative-rate calculation is explicitly a **heterogeneous D34b
variant**, outside the chosen unit-rate law, and the marked masses are the
requested exact values `(1/48,1/24)` and `(1/32,1/32)`.

### Major M4 — CLOSED

P10 upgrades the single-clock necessity witness to a global age-vector PDMP
specimen. It gates `S(a+s)/S(a)`, the two-actor residual race `(1/4,3/4)`,
initiator reset, newborn age zero, passive receiver advance without reset and
joint survival. The narration correctly limits sufficiency to the complete
graph-plus-age state and leaves a local observer's hidden-age posterior open.

### Major M5 — CLOSED

P12 carries the requested ownership/capacity ledger. Only event-outcome rank
six and event incidence arity two are uniformly bounded. Ulam bit length,
actor degree, total configuration, connected-boundary width, renewal-age-vector
width and posterior complexity are explicitly nonbounded/unproved. The score
states that the global configuration is not one finite-capacity record.

### Round-1 minors/nits — CLOSED

- A-own-ring count and A-wire-event count are distinguished; the reception
  specimen prints `0/1/1` for own/wire/global counts.
- Ideal exponential memorylessness and the finite stored-deadline reference
  are separated.
- P2 now quotients observed histories/posterior beliefs rather than only pure
  hidden states and prints `2,3,...,13` reachable predictive classes.
- Construction time remains an external model parameter; relativistic
  synchronization, foliation independence and proper time are not claimed.
- The note status is updated and unused `SINDEX` is removed.

## Remaining MINOR findings

### m1 — eligibility/sealing scope in the reconstructed generator is broader
in prose than in code

The reachable reconstructed seed contains only active unsealed actors, matching
the active-only D34b exact oracle, while the terminal actor reference separately
contains and suppresses the event-inert sealed root `R`. However P8 inventories
“active/sealed Ulam actors,” and `d34b_rates` skips sealed **initiators** but
does not filter sealed interaction **targets** from `neighbors[y]`.

If the actual actor-reference seed `R--A--B` were inserted literally, the
current code would assign A-to-B and A-to-R rates `1/8,1/8` instead of the
eligible-only A-to-B rate `1/4`. This does not affect any reachable P8–P11
specimen and does not falsify the no-sealing exemplar theorem, but the declared
state inventory is too broad.

**Repair:** either (a) call P8 the active-only quotient with inert sealed `R`
removed and delete `sealed` from its claimed state domain, or (b) define
`eligible(y)={x in neighbors[y]: not sealed(x)}`, use it in both rates and
steps, include the actual sealed-root seed, and gate A-to-B=`1/4`, no A-to-R
option.

### m2 — the full rate–horizon law identity is correct but the executable gate
checks only one cylinder

P11's numerical evidence for
`Law_(c lambda,T)=Law_(lambda,cT)` is the zero-ring survival probability of two
actors. The full branching D34b identity is true, but it needs the pathwise
source coupling as its proof: divide every preassigned exponential wait by
`c`, retain every mark/Ulam address, and induct over births; the event/DAG path
through `T` in the scaled law then equals the original path through `cT`.

**Repair:** carry that induction explicitly in the note/P11 label and gate a
nontrivial birth-plus-reception path under paired rescaled clock coordinates.
Do not present the two-clock no-ring regression alone as a full-law gate.

## Remaining NIT

1. P8 still says “physical stopping times.” D34d's own terminology has
   correctly demoted this parameter to **construction time**. Use
   “stopping times of the complete construction-time filtration” to prevent
   accidental proper-time import.
2. `age_kernel_1` and `age_kernel_2` are constructed by the identical function
   call, so their equality is not an independent kernel reconstruction. The
   analytic PDMP argument and other exact subgates suffice; either remove the
   duplicate or compute the second row by direct integration/symbolic survival
   algebra.

## Delta verdict

The substantive repaired noun is accepted:

> **D34d GLOBAL-MARKOV / LOCAL-GENERATOR / OBSERVABLE-MEMORY
> CHARACTERIZATION:** the chosen active, static-adjacency classical D34b law is
> strong Markov on its complete global configuration and is generated by
> actor-local terms; record projections require law-scoped
> sufficiency/lumpability tests; a bounded local predictive collar remains
> open.

This does **not** establish a bounded per-record Markov state, relativistic
locality, a timed D34b–D34c operator-valued measure, physical proper time, or a
derived universe law. Those withdrawals are now explicit and load-bearing.

Apply the two minor scope/evidence repairs and two nits, rerun the classical
receipt, and this locality/clock stream can stamp unqualified `DELTA-CLEAN`.
