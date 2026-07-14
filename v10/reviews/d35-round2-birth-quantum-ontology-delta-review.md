# D35 round 2 — birth/quantum/ontology delta review

**Frozen repair target:** commit
`592e1028b75cb3052b734bf4d28aac0b8284936c`.

**Round-1 lane:**
`reviews/d35-round1-birth-quantum-ontology-hostile-review.md`.

**Verdict:** **DELTA NOT CLEAN — THE CLASSICAL CAPABILITY-ACTOR REPAIR
SURVIVES, BUT THE BUSCH INSTRUMENT AND CARRIED-PAYLOAD INFLUENCE CLAIMS DO
NOT.**

**Count:** **0 blockers / 2 majors / 1 minor / 0 nits.**

The replacement genuinely repairs actor ownership, authenticated routes,
local identities, full classical projectivity and most event typing. It also
preserves the correct D24 newborn-content result. Two central round-1 claims
remain over-promoted. The receipt never constructs the flagged operators on a
common input space, and its intervention changes a bit already supplied by A
to A rather than evidence originating remotely and returning through a query.

## 1. Independent reproduction — pass

I ran

```text
v10/code/d35b_capability_actor_exact.py
```

under fresh hash seeds `123457` and `765431`. Both executions exited zero,
were byte-identical to each other and to the committed receipt, and reproduced:

```text
source SHA-256
fa6d69e6d6b85620d19da8e80899dba4a3a5f976fb6e0b3fcfb7b1224a253c4d

stdout SHA-256
8afc279b5ace76a2c7e043dc043d4b450f14536e262d353333d86c08899e304a

internal science SHA-256
3d6703f6ef4fcc84588bf8927d32621052733b6652c27225553fa97772ed3679

verdict
PASS 18/18
```

Both `git diff --check b08249c..592e102` and the narrow repair-range check
`git diff --check 2bb4fa2..592e102` are clean. The findings below are semantic
and mathematical gate failures, not nondeterminism, arithmetic drift or
whitespace defects.

## 2. Round-1 issue map

| Round-1 issue | Delta disposition |
|---|---|
| Classical metadata was called an orthogonal flag | **not closed at operator grade** |
| No arbitrary-input flagged completeness | **not closed; separate incompatible-size operators are checked** |
| Structural ancestry lacked a persistent route | **closed structurally by capabilities and TransferRecords** |
| No physical payload intervention | **not closed; root self-copy is tested** |
| Multi-leg roles and arity implicit | substantially closed on generated paths |
| Malformed paths fail before mutation | **new reachable API counterexample; minor** |
| D24 marginal instant | remains correct |
| Stale status | closed |
| “birth cells” wording | closed as branch-cell incidences |

## 3. D24 birth and reception wording

### 3.1 Newborn-content instant — pass

The replacement hash-locks the reviewed base source and calls its
`create_birth` unchanged. For each birth, the parent marginal is read
immediately before a genuinely fresh child is represented in `|0>`, and the
child marginal is read immediately after the controlled rotation. Independent
enumeration reproduces the same 12 branch-cell incidences per parameter cell:

```text
Q1, g=9/25:
16/25       -> 144/625
144/625     -> 1296/15625
1296/15625  -> 11664/390625

Q2, g=16/25:
16/25       -> 256/625
256/625     -> 4096/15625
4096/15625  -> 65536/390625
```

Every row obeys `P(child=1)=g P(parent=1)` exactly and every completed carrier
has norm one. The standalone `4x2` birth matrix also satisfies `V^T V=I_2`
exactly. No D24 timing or branchwise-isometry repair is requested.

### 3.2 “The right birth kernel” — adequately scoped

The note still distinguishes:

```text
D24: one valid inherited one-parent newborn-content family;
q_birth, g, root, ownership and omitted sectors: unselected;
D25/D27 Busch class: broader than D24.
```

Section 15 additionally says the replacement does not select D24 over the
wider reception class and that Q1/Q2 disagree. “Right” is restricted to the
frozen exhibit or appears as an explicitly unsolved selection question. I find
no new uniqueness overclaim.

## 4. Major findings

### M1 — `sum q V^dag V=I` and orthogonal flag ranges are asserted, not constructed

The receipt prints:

```text
operator_isometries=4/4
orthogonal_local_flags=5
sum_q_VdagV=I
```

But `flagged_operator_gate` constructs only these unflagged elementary
matrices:

```text
idle    2x2
birth   4x2
visit   4x4
fork    8x8
```

It separately checks each `V^T V=I`, checks that the five root probabilities
sum to one, and checks that five Python tuples `(action,target_ports)` are
distinct. It then infers the advertised direct-sum identity in a comment.

Those matrices do not even have a common input dimension, so their closures
cannot be summed. At the registered root, the actual pre-event carrier is the
joint A/B/C sector. Idle must be extended by identity on B/C, each visit must
be embedded on its named target while acting identically on the spectator,
fork acts on all three, and birth maps that same full input into a sector with
one additional child. Only after those embeddings can the output sectors be
placed in an explicit direct sum and tested.

The claimed physical flags are likewise still stored as
`Provenance.flag_factor` tuples. They never enter `collector.amplitudes`, no
flagged matrix `W_o` is built, and no exact `W_o^dag W_o'` calculation is
performed. Distinct tuple values can *index* an orthogonal basis in a future
definition, but set cardinality is not an operator-range proof. The
`completed_flag_histories=16` gate proves distinct classical labels, not
orthogonal persistent quantum factors.

The support-changing birth alternative makes the missing step especially
important. A legitimate construction may use

```text
H_out = direct_sum_o H_out,o,
W_o   = J_o V_o,
```

where all `V_o` share the same full `H_in`, birth's `H_out,o` includes the
newborn factor, and `J_o` are mutually orthogonal injections. But that object
is not in this executable. Busch's theorem applies only after a common channel
and its orthogonal ranges exist; branchwise isometries plus classical labels
do not constitute the printed proof.

There is a second typing issue hidden in the tuples. Their alleged factor label
contains namespace, transaction, path and structural addresses. D34c separated
the bounded local outcome alphabet from unbounded structural incidence. D35b
must make the same separation if “bounded event factor” is restored; otherwise
the tuple should be called an unbounded provenance label, not a bounded-rank
local record state.

**Required repair:** for each reachable local degree in the declared grammar:

1. choose the common full pre-event carrier;
2. extend idle/visit/fork by spectator identities and define birth on that
   same input;
3. construct explicit flagged injections into one direct-sum output;
4. check `W_o^dag W_o=I`, `W_o^dag W_o'=0` for `o!=o'`, and
   `sum_o q_o W_o^dag W_o=I` exactly;
5. keep local outcome rank separate from structural event identity; and
6. compose two calls or prove finite-prefix induction with old factors
   support-excluded.

Until then the allowed quantum statement is **branchwise D24/unitary carrier
compatibility with a proposed classical flag schema**. The nouns `flagged
direct-sum Busch instrument compatibility`, `NSE closure`, and `physical
orthogonal event factors` are not earned.

### M2 — the payload intervention is A-to-A self-copy, not acquired remote evidence

The replacement now retains authenticated capabilities and complete adjacent
routes. That closes the structural half of round-1 M2. The intervention gate,
however, sets `network.root_payload` and places the same bit in the top-level A
capability. Every A2 event records it directly.

An exact probe of Q1 with payload one gives:

```text
root idle:
  output payload = 1
  route = (root,)
  transaction transfers = [(requester=None, target=root, route=(root,), payload=1)]

root birth:
  output payload = 1
  route = (root,)
  transaction transfers = [(requester=None, target=root, route=(root,), payload=1)]
```

Thus `do_source_0_to_A2=0 / do_source_1_to_A2=1` passes even on branches with
no child query or return. It proves that A can copy a supplied A-local bit into
A's next record. It does not prove that evidence at B, C or D reaches A only
through a queried route.

The two printed `unqueried_route_controls` test whether the old structural
event `BD` is absent when A visits C. They do not intervene on a payload held
at B/D. The disconnected test changes a remote metadata string and verifies
factorization; it likewise supplies no connected remote source whose bit can
return or be blocked.

Consequently section 15's sentence

> “Intervening on the declared source payload ... changes A2 ...; an unqueried
> or disconnected route does not”

is only true if “source” means A itself, in which case the route qualifier is
vacuous. It does not discharge the frozen requirement that a source bit reach
A2 *through a queried route and fail on an unqueried route*.

**Required repair:** give one non-A actor a source payload while A's own input
and all other data are fixed. Compare exact interventions `do(e=0)` and
`do(e=1)` under:

1. a completed query/return route from that actor to A;
2. the same connected state with that route unqueried; and
3. an isomorphic disconnected source.

The A2 record law or its retained evidence factor must differ only in case 1,
and the payload must be authenticated at every hop and included in the final
physical record—not merely in an audit digest. Until then the allowed noun is
**structural CAP ancestry plus authenticated root-payload propagation**. A
general physical carried-evidence or operational acquisition theorem remains
open.

## 5. Minor finding

### m1 — malformed typed options can still mutate actor state before rejection

`process_query` validates the capability, then immediately adds its identifier
to `used_capabilities` and inserts its `TransferRecord`. Only afterward does it
validate visit/fork legs. The comment “Validation is complete before any
immutable mutation” is therefore false for the action option.

Using a genuine issued root capability and the malformed internal option

```text
LocalOption("fork", (0,0), 1)
```

produces the exact result:

```text
rejected = duplicate event leg
state_unchanged = False
used_capabilities = 1
transfers = 1
provenance events = 0
```

The registered `9/9 pre_mutation_unchanged` battery misses this by calling
`validate_typed_event` directly for malformed merge rows rather than sending a
malformed option through the real query handler. The law's own enumerator only
generates legal options, so this is not a bad branch in the normalized family.
It is nevertheless a fail-closed actor/API gap and a denial-of-service path
against the claimed capability discipline.

**Required repair:** verify that the entire selected option is a member of the
current actor's exact `local_options` menu—including action, legs and assigned
probability—before consuming the capability or recording a transfer. Add this
probe to the pre-mutation battery.

## 6. What the repair does establish

The following advances survive independent attack:

- actors now own mailboxes, tips, port tables, used capabilities and open
  calls at the declared rooted-tree scope;
- authenticated one-use capabilities bind component, transaction, caller,
  target, slot, held tip, route and payload;
- returns bind the issued child capability to a provenance-bearing result;
- disconnected display-name collisions do not alter A's distribution;
- actor relabeling leaves the port-addressed classical quotient fixed;
- all 16 full first-call cylinders marginalize exactly over 408 second-call
  refinements, with old provenance and root-wire ancestry persistent;
- generated idle/birth/visit/fork events have explicit initiator, typed legs,
  operation and coupling provenance;
- the classical rooted nested-call law remains normalized and serializer
  invariant on first calls, every first-call output's second call, and the
  deterministic eight-call runs;
- D24 birth is evaluated at the correct instant and is branchwise isometric;
  and
- Q1/Q2 continue to prove nonselection of opportunity weights and `g`.

None of the new findings requests a change to those exact probabilities.

## 7. Allowed nouns and prohibited promotions

### Allowed now

```text
TIMELESS ROOTED NESTED-CALL CLASSICAL FAMILY / EXECUTABLE

CAPABILITY-AUTHENTICATED ACTOR REBUILD
at the declared finite rooted ownership scope

STRUCTURAL CAP ANCESTRY + AUTHENTICATED ROOT-PAYLOAD PROPAGATION

BRANCHWISE D24 BIRTH / UNITARY RETURN CARRIER COMPATIBILITY
```

### Not yet allowed

```text
FLAGGED DIRECT-SUM BUSCH INSTRUMENT COMPATIBILITY
PHYSICAL ORTHOGONAL EVENT-FACTOR CONSTRUCTION
NSE CLOSURE OF THE TIMELESS q-MIXTURE
REMOTE CARRIED-PAYLOAD INFLUENCE / PHYSICAL EVIDENCE ACQUISITION
THE RIGHT OR UNIQUE BIRTH OR OPPORTUNITY LAW
```

The note already refuses the last uniqueness noun; that refusal must remain.

## 8. Final disposition

| Audit target | Disposition |
|---|---|
| Exact receipt and hash-seed replay | pass |
| D24 marginal instant | pass |
| Elementary branch isometries | pass |
| Common-input option operators | **absent** |
| Explicit direct-sum flagged operators | **absent** |
| Orthogonal range calculation | **absent** |
| Busch/NSE mixture claim | **not earned** |
| Persistent structural routes | pass |
| A-local payload copy | pass |
| Remote payload acquired through query | **not tested** |
| Unqueried/disconnected payload exclusion | **not tested** |
| Generated event typing | pass at registered scope |
| Fail-closed malformed option handling | **fails new probe** |
| D24 uniqueness scope | honest |

**Final count:** **0B / 2M / 1m / 0n.**

**Final verdict:** retain the capability-authenticated timeless classical
family and its exact branchwise D24 carrier maps. The round-2 delta is not
clean at the frozen O6/physical-acquisition width. Repair M1/M2 or narrow the
note and receipt to the allowed nouns above before terminal promotion.
