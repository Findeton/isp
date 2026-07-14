# D34c action-level replacement — independent NSE/seal hostile review

**Target:** frozen replacement commit `d634f3d`.  **Review scope:** the new
action-level D34c object only.  **Verdict:** THE ACTION-LEVEL REPAIR IS REAL,
BUT THE `A`-LOCAL STOPPING-ALGEBRA AND ALL-FINITE-PREFIX WIDTHS REQUIRE MAJOR
NARROWING/REPAIR.  **Count:** 0 BLOCKER / 2 MAJOR / 5 MINOR / 2 NIT.
**False results:** zero false printed quantum numbers, zero hash mismatch, zero
hidden preparation-dependent scheduler weight.  One observation-algebra claim
is too wide: incoming receptions are omitted, not coarse-grained.  The
all-finite-prefix architecture also assumes an unbounded append-only mailbox.

## Reproduction and independent checks

The receipt was rerun under `PYTHONHASHSEED=314159` and `271828`.  Both outputs
were byte-identical to the committed output, with SHA-256
`a7cee72762f4244a57b5a698b3eb7172c8d1826bfa52effe37625b1e4c843720`.
All ten displayed gates pass.

The replacement genuinely removes the round-1 spectator defect.  In
`quantum_branches`, an event label now selects the operation: birth applies
`acry` to the named Ulam child, interaction calls `interaction_branches` on the
named target, and idle copies the carrier vector unchanged.  The first
interaction's off-diagonal path terms produce the printed coherent output; the
birth and idle blocks have no attached spectator diamond.  The exact
`108 -> 10` restriction therefore applies a real second operation, rather than
marginalizing an unused kind symbol.

The preparation-independence audit is also clean at its declared fixed-seed
scope.  `actor_options` reads only the classical neighbor graph and local birth
counter.  It never reads an amplitude, density matrix, `s`, `p`, or `o`.
Quantum outcomes `s,o` naturally have preparation-dependent Born weights, but
they are generated inside the isometric interaction and copied into record
flags; they are not an external state-reading lottery.  The forbidden
state-reading control remains a valid negative witness in C7.

## MAJOR

### M1 — incoming receptions are omitted, not coarse-grained

The new object is described as the `A`-initiated local-ring stopping algebra
with incoming remote receptions coarse-grained.  The executable instead runs
two consecutive `A`-initiated steps.  `depth1_paths` and `depth2_paths` call
only `actor_step(... actor_options(...))`, and every generated event ID is
`A#rj`.  No other actor clock rings between those calls.  The predecessor map
therefore contains only earlier events from this `A`-only skeleton.

That is not the marginal obtained by coarse-graining the full D34b process.
Before `A`'s first ring, and between its first and second rings, `B` and any
born neighbor can ring with positive probability.  In particular an incoming
`i(B,A)` is a physical predecessor on `A`'s wire, writes a durable reception,
and—under the chosen quantum operation family—changes `A`'s carrier state.
Summing over that hidden history is not equivalent to deleting it.  The
classical kind marginal of `A` remains `(1/4,1/4,1/2)`, but the quantum
functional at `A`'s next ring need not remain the one computed from
`actor_initial` with no incoming operation.

**Disposition:** the exact depth-2 receipt earns an action-level result for a
**consecutive `A`-initiated skeleton**, equivalently a conditional/intervention
schedule in which other clocks are paused or no touched-wire incoming event
occurs.  It does not yet earn the name "D34b `A`-local stopping-algebra
marginal."  Either make that conditioning explicit everywhere, or enumerate
and sum the incoming actor histories.  Because their count before a local
stopping time is unbounded, the latter route is already part of the missing
continuous-time/infinite-sum problem, not a cosmetic depth-2 addition.

### M2 — the finite-prefix induction assumes unbounded actor mailboxes

At depth two, the mailbox construction is finite and exact.  The claimed
induction to **every** finite local prefix repeatedly appends a complete event
token—including predecessor data and durable outcomes—to a Python list owned
by each touched actor.  Thus one actor's mailbox dimension and stored evidence
grow without a uniform bound.  The proof silently uses either an
infinite-dimensional append-only record or a different, larger Hilbert space
at every prefix depth.

This matters in SHARD because individual records are supposed to have finite
evidence capacity.  "Every finite depth is finite" is not a single
finite-capacity actor architecture.  The old tokens are durable only because
the model supplies indefinitely many orthogonal mailbox states and never
reuses them.

**Disposition:** depth two survives.  The all-finite-prefix theorem must be
made conditional on an explicitly unbounded local mailbox, or the flags must
be realized as fresh finite-capacity event records linked to the actor, with
future events appending a new record rather than enlarging the old actor
record.  The latter construction must preserve predecessor access and prove
that old flag factors remain support-excluded.  Until one option is explicit,
the induction is algebraically correct as a growing-family schema but is not a
completed SHARD record architecture.

## MINOR

1. **The all-state NSE lemma and the actor construction are not yet joined by
   one operator-level gate.**  C6 proves the Busch direct-sum identity for an
   abstract three-branch qubit channel.  C8 evaluates the actor functional on
   the single `actor_initial` state.  The intended general proof is sound if
   one defines, for each classical ring option, a coherent isometry that
   includes the `s,o` mailbox-copy operation and then proves orthogonality of
   the scheduler-history ranges.  State that isometry explicitly—or gate
   `W_h^dag W_h=I`, `W_h^dag W_h'=0` on the depth-1/2 actor maps—before calling
   NSE action-level rather than abstract compatibility.  The fixed graph-sector
   scope is correctly disclosed; graph-sector superposition remains open.

2. **The remote quantum gate is abstract, not the actor channel just built.**
   `product_flagged_channel` tensors the C6 `I/X/Z` test channel.  It does not
   tensor the D24-birth/target-diamond/mailbox actor instrument.  The claimed
   conclusion is mathematically expected—disjoint tensor-factor isometries
   commute and a trace-one remote channel leaves the local marginal—but the
   receipt should either instantiate the actual actor maps once or label this
   line as the dimension-free analytic tensor lemma.  It also does not address
   the connected incoming-reception issue in M1.

3. **The explicit path receiver is branch-level rather than time-ordered.**
   `append_path_receiver(v,p)` is exactly the isometric embedding
   `v_p -> v_p tensor |p>` and its Gram matrix independently reproduces the
   masked functional.  That is adequate mathematically.  The prose should say
   it is the class-branch representation of a CNOT inserted at the `p` cut;
   the code appends the receiver after constructing the final four-qubit
   branch and does not literally evolve a fifth qubit through the later gates.

4. **Instrument completeness is proof-carried more than receipt-carried.**
   Row weights and the degree-two split are exact, and all event operations are
   visibly unitary/isometric.  But `all_m_identity` checks only `m=1..64`, and
   no actor-map matrix identity is printed.  The one-line rational identity
   holds for every positive integer `m`; record it as the analytic proof and
   call the loop a finite regression.  Likewise distinguish scheduler
   alternatives `e` from the durable quantum outcomes `s,o`: the full coherent
   flag-writing map for one `e` is the isometry used in the Busch argument.

5. **Mailbox durability is represented by inner products, not future-support
   checks.**  `factorized_flag_inner` is a valid product of actor-mailbox
   Kronecker deltas, and the tokens omit `p` while including `s,o`.  At depth
   two, appending preserves the earlier list prefix.  For the induction,
   however, explicitly state that each new token occupies a fresh tensor
   factor and every future operation is identity on old factors; otherwise a
   whole-list basis update is only an encoding of durability, not its
   operator-level proof.

## NIT

- The helper name/comment "all-m identity" is too wide for a loop ending at
  64, even though the analytic equation is elementary and true.
- Global sorting in `mailbox_key` and global dictionaries are acceptable
  verifier/serializer conveniences, but the note should say so explicitly.
  The physical tokens themselves use the initiator-local ID `A#rj`, named
  target, and touched-wire predecessor data; no universe-wide event number or
  live-record census was found.

## What survives at reviewed strength

- C1--C4's exact non-diagonal diamond, explicit receiver equivalence, strong
  positivity, and finite restriction survive.
- C5 now says exactly what it proves: every later modeled operation fixes the
  local `R` algebra because `R` is support-excluded, while a relational
  `R--S` observable changes.  It does **not** claim sealed holonomy.  This is
  clean.
- The Busch/NSE block-norm theorem is correct for preparation-independent
  weights and orthogonal isometry ranges, at a fixed classical seed/graph
  sector.  Forgetting the flag and nonlinear state-reading remain sound
  negative controls.
- The event kind and target genuinely select touched-carrier operations.
  Birth is the D24 rotation on the named fresh child, interaction is the
  diamond on `A` and the named target, and idle is identity.
- The mailbox inner product is actor-factorized.  `p` is excluded and remains
  capable of interference; `s,o` are included and decohere.  No hidden global
  history atom, global serialization number, or universe census appears in the
  flag rule at the tested depth.
- Every printed depth-1/depth-2 classical shadow, interaction signature,
  degree-two target weight, and `108 -> 10` quantum restriction reproduces.
- No scope leakage to the full timed law, untimed inverse system, graph-sector
  superposition, or nature's unique law was found in §15/C9.  Those exclusions
  are explicit and should remain.

## Required terminal wording after repair

Without addressing M1, the strongest defensible noun is:

> **CONSECUTIVE-A-INITIATED DEPTH-2 ACTOR/QUANTUM SEWING PASS** — on a
> conditioned skeleton with no intervening incoming touched-wire events,
> birth/interact/idle select the declared local quantum operations; distributed
> finite-depth flags retain the quantum path interference and the second
> instrument restricts exactly.

The finite-prefix statement may be carried only as:

> **Conditional algebraic induction:** given preparation-independent local
> weights, isometric event maps, fresh mutually orthogonal durable flag factors,
> and sufficient fresh carrier/mailbox capacity, the Gram functional is strongly
> positive and exhaustive extension restricts by induction.

To restore the proposed `A`-local D34b stopping-algebra noun, integrate the
positive-probability incoming receptions and their quantum actions.  To restore
the unconditional all-finite-prefix architecture, supply the fresh bounded
event-record construction or explicitly adopt an unbounded mailbox ontology.

