# D35 round 2 — causal-locality/actor delta review

**Frozen target:** commit
`592e1028b75cb3052b734bf4d28aac0b8284936c`.

**Lane:** actor ownership, local transition preconditions, causal transport,
identity covariance, construction labels and the claimed simulator scope.

**Verdict:** **REJECT TERMINAL PROMOTION — THE NORMAL GENERATED RUNS ARE
SCHEDULER-COVARIANT, BUT THE ACTOR BOUNDARY IS NOT YET FAIL-CLOSED AND THE
IMPLEMENTATION DESCRIPTION OVERSTATES WHAT IS LOCAL.**

**Count:** **1 blocker / 3 majors / 1 minor / 1 scope note.**

This record preserves the independent review lane's communicated exact probes.
The lane's report-writing turn was interrupted after the findings were sent;
the main investigation transcribed those findings here without changing their
substance.  No repair below was made before this opening record was frozen.

## 1. What passes

The committed receipt reproduces under independent hash seeds.  On generated
legal traffic, each logical actor owns a mailbox, tip, child-port table,
used-capability set and outstanding-call table.  FIFO, LIFO and canonical
mailbox servicing yield the same 16 physical atoms in Q1 and Q2.  Second-call
growth and eight-call deterministic replay also agree.  Actor-display-name
renaming passes.  Those are real improvements over round 1's single global
pending/continuation table.

## 2. Blocker

### B1 — a locally reconstructible but unissued child query is accepted

The replacement signs an edge query using

```text
edge_key(namespace,parent_address,port,child_address)
```

but that key is a deterministic digest of public structural data.  A child
capability constructed with the model's own formula, while absent from the
requester's `outstanding` call and `child_caps` table, passes
`validate_query`.  The exact probe created transaction event
`...T91:7.7` at the child.

The reason is structural, not cryptographic: the target verifies the token's
shape/signature and owned edge, but never verifies that this exact capability
was issued into its actor-owned incoming set.  The test therefore reopens the
round-1 unissued-query failure at a narrower layer.

**Required repair:** a target actor must own a set of capabilities actually
issued to it over an adjacent port.  Validation must require exact membership
and consume it once only after every query and action precondition passes.
Knowing the public graph must not be sufficient to manufacture issuance.

## 3. Major findings

### M1 — action validation still occurs after durable actor mutation

With a genuine root capability, an invalid local choice such as

```text
LocalOption("visit", (9,), 1)
```

or a duplicate-leg fork is rejected only after the capability has been added
to `used_capabilities` and a `TransferRecord` inserted.  Hence the comment
that validation is complete before mutation is false.  The registered 9/9
battery calls `validate_typed_event` directly for malformed choices and does
not exercise this reachable `process_query` path.

**Required repair:** require the exact option to belong to the actor's current
normalized local menu and validate its typed ports before consuming the
capability, recording a transfer or changing any durable record state.

### M2 — the physical quotient retains nominal seed-event identities

Consistently renaming `A0, AB, AC, BD, A1`, their dictionary keys, predecessor
references and actor tips yields the same rooted marked seed DAG, 16 branches
and total mass one, but a different `physical_key` distribution in Q1 and Q2.
`physical_event_id` returns `("seed", raw_name)` for every unprovenanced event.
The committed alpha gate renames actors only.

**Required repair:** canonically identify seed events by their rooted marked
causal structure at this declared seed scope, extend the gate to the whole
seed event DAG, and rerun both the 16-atom and 408-refinement laws.

### M3 — the implementation has more shared state than mailbox selection

Section 15 says the sampler's only global operation is choosing a nonempty
mailbox.  In fact `Network.current_tx`, `Network.root_payload`, the shared
event collector, provenance/transfer dictionaries and the joint carrier
amplitudes are also read or mutated.  The local stochastic menu itself uses
the addressed actor's owned ports, so this does not create a whole-component
probability normalizer.  But the stronger implementation sentence is false.

In particular, a second A call with reused `tx=0` collides with an old event;
a fresh external transaction integer is required by the current API.  This
integer is a structural root-wire/call ordinal rather than elapsed proper
time, but it is supplied by `Network`, not generated from root-owned causal
succession.

**Required repair:** derive fresh event identity/call ordinal from the root
actor's owned successor state, and describe the shared collector honestly as
an exact joint quantum/event-DAG audit representation.  If a fully distributed
quantum-state implementation is claimed, it requires a separate construction;
logical actor locality alone does not provide one.

## 4. Minor finding

### m1 — dequeue-before-validation changes the mailbox on rejection

The 9/9 unchanged-state gate invokes handlers without first using
`pop_envelope`.  Normal service removes an envelope from the mailbox before
handler validation.  A rejected message therefore changes volatile mailbox
state even when durable records do not change.

Either service must peek and acknowledge only after success, or the claimed
invariant must be narrowed explicitly to durable physical record state while
permitting rejection/discard of a bad volatile envelope.  It cannot continue
to call the direct-handler snapshot a whole-actor-state test.

## 5. Scope note — this is A-conditioned, not a root-free universe

`start_root_call` injects an A-root capability, and repeated completion always
starts the next call at A.  The model therefore samples the causal content of
A's next rooted update conditional on an externally chosen A initiation.  It
does not select which actor in a universe initiates a transaction, nor prove
compatibility of overlapping peer-initiated diamonds.

That limitation is not a proper-time failure.  A numerical clock is absent,
and A2 is selected by causal succession.  It is instead an open extension-law
problem.  A root-free physical law would need compatible local conditional
kernels on overlapping causal diamonds, or an equivalent confluent peer
protocol, whose outcome is independent of machine service order.

## 6. Decision ceiling

The exact normalized classical rooted-call kernel survives.  It is not yet a
terminal actor-local result under the frozen fail-closed and alpha-covariance
requirements.  Before repair the maximum safe noun is:

```text
time-free rooted nested-call classical kernel with logical actor mailboxes
```

After the blocker and majors close, the intended ceiling can again be

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

Neither noun is a root-free universe history law, a fully distributed quantum
simulation, a v9 profinite identification, spacetime or nature's law.
