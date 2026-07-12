# D11 hostile review, round 1: ontology, locality, record semantics, and physics scope

**Referee:** independent hostile ontology/locality/physics audit  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**

## Frozen artifacts audited

- `v10/note-d11-complete-bloch-lorentz-scir-protocol.md`
- `v10/code/d11_complete_bloch_lorentz_exact.py`
- `v10/code/d11_generated_history_geometry.py`
- `v10/note-d11-complete-bloch-lorentz-scir-investigation.md`
- `v10/note-d11-literature-audit-complete-packet-and-extinction.md`
- `v10/relativistic-isp-v10-paper12-complete-lorentz-rulebook-that-cannot-grow-a-universe.md`
- `v10/data/d11-pre-review-receipt.md`

The exact engine independently reproduces **65/65** checks and receipt hash

```text
64cbb0bd2691713145f8679211d01dda023b78f9f5b32d64e146c08ad3ff9de8
```

The instrument identities, finite kernel normalization, common-future
placement, bounded-history census, and population drift arithmetic survive.
The blockers concern what the packet is allowed to mean.

## Blockers

### B1 — The local rules are incidence-scoped, but the next-event law still uses a global race

**Severity:** critical

Each SPLIT, JOIN, and SEAL token names only owned ports. That is genuine
support locality. But `enabled(history)` enumerates every open port and JOIN
in the complete universe, and `next_kernel` divides each activity by the sum
over that global list. The generated-history simulator likewise chooses one
global next token.

This is not yet a decentralized local click implementation. Independent
exponential clocks can define the same continuous-time process without a
central machine, but D11 must then specify the local clock ontology, causal
availability of clocks, and why taking the global earliest firing is an
auxiliary presentation rather than a physical universal commit order.

**Repair:** distinguish `local generator terms` from `global next-event
normalization`. Either construct commuting local Poisson clocks and quotient
the auxiliary ordering, or call the result a globally normalized sequential
path law with incidence-local transition kernels. Remove “no hidden
all-universe scheduler” until that realization is proved.

### B2 — The generated history is not the gauge-covariant relational object proved in G0

**Severity:** critical

G0 proves correct dual `SL(2,C)` covariance for separately supplied matrices.
The actual `History`, however, is generated entirely in one root gauge. Ports
store absolute `event_position` matrices; children inherit the same
`frame_link`; JOIN copies the left order unit and frame link; and no generated
rewrite transports states/effects through nontrivial incident links.

Thus algebraic gauge covariance and path generation are parallel tests, not
one integrated gauge-covariant history law. The claim “complete
Lorentz-covariant record rulebook” is stronger than the executable packet.

**Repair:** execute the same generated history in independently changed local
frames, including order units, states, effects, links, instruments, JOIN
anchors, positions, outcome probabilities, and canonical history comparison.
Until then use `root-gauge packet with a separately verified dual-covariance
template`.

### B3 — Terminal SEAL does not create the durable record object its name implies

**Severity:** critical

`seal_outcomes` consumes the only port and appends `(pid,"SEAL",outcome)` to a
tuple. It creates no record node, position, owner, post-measurement state,
ancestry edge, or successor. Repeat durability is checked algebraically on an
unnormalized branch, but repetition is impossible in the actual grammar after
the carrier is deleted.

SPLIT and JOIN outcomes are also appended to the same `seals` tuple even
though they have different continuation semantics. The packet therefore
conflates outcome logging, a durable record, terminal observation, and
carrier destruction.

**Repair:** type at least `OUTCOME`, `DURABLE_RECORD`, `TERMINAL_SEAL`, and
`CONTINUING_COMMIT` separately. A terminal seal must create an immutable
record object even if it emits no open carrier. Durability must be tested on
the generated record semantics, not only by reapplying a projector outside
the history grammar.

### B4 — JOIN is a sibling recombination, not a general joining or bridge law

**Severity:** major

The ownership gate is honest: JOIN can act only on the two direct children of
one SPLIT and uses their stored common anchor. It never joins unrelated roots,
components, or independently arising records. Consequently it does not solve
the corpus's first-cross-component carrier problem.

Partial-iSWAP does provide a real two-input statistical interaction in the
chosen qubit packet, and a witness changes a later projector probability.
That supports `sibling interaction`. It does not support an unrestricted
`JOIN`, bridge birth, or general influence mechanism.

**Repair:** rename the rule `SIBLING-MERGE` or qualify every JOIN claim.
Preserve that unrelated-component joining is absent. A broader JOIN needs a
local proposal/eligibility law for previously independent records and typed
cross-component ownership.

### B5 — Construction-order gauge is under-tested and probability pushforward is absent

**Severity:** major

The receipt executes two deterministic disjoint SPLIT schedules and compares
their sorted final histories. It does not compare their path probabilities,
sum all presentation orders into a canonical physical fiber, or test general
disjoint SPLIT/SEAL/JOIN combinations.

Final-state commutation is not yet the v9 construction-order gauge theorem.
The global race changes its enabled-token denominator after each firing, so
probability equality must be demonstrated rather than inferred from matrix
commutation.

**Repair:** push the complete bounded path measure to canonical marked
histories and compare fiber masses under alternative disjoint presentations.
Until then retain only `DISJOINT-SPLIT STATE COMMUTATION AT ENUMERATED SCOPE`.

### B6 — Per-record state is not finitely bounded and carries hidden history/global coordinates

**Severity:** major

Each port stores an ever-growing `ancestry_word`, an expanding string-based
record identifier, and an exact absolute position whose rational/algebraic
description can grow. The generative rule does not need the full ancestry word
for its local instrument, yet the claimed primitive record tuple includes it.

This conflicts with the program's finite-record discipline and reintroduces
history into each current carrier rather than distributing it over immutable
records.

**Repair:** remove redundant full ancestry from the live port; retain parent
IDs/provenance in the record graph and audit per-record description/evidence
capacity separately. Treat absolute root-frame position as a downstream
coordinate shadow, not primitive local storage.

### B7 — The built-in construction cone is not physical spacetime

**Severity:** major

Every SPLIT edge is positive because D11 declares `Delta Y=2 rho`. Every JOIN
edge is positive because it declares `Y_c=Y_a+Y_b-Y_o`. The cone containment
is therefore a wiring theorem in an imported `Herm_2(C)` coordinate space.
The receipt correctly says so.

Nevertheless the investigation and paper repeatedly call the packet “exact
relativistic kinematics,” “Lorentz-covariant causal construction,” and a
successful local Bloch–Lorentz construction. No physical time scale, metric
calibration, order/influence equality, propagation front, or Einstein
dynamics is derived.

**Repair:** consistently call this `algebraic positive-cone containment in a
declared coordinate shadow`. Keep rewrite ancestry, positivity, coordinates,
and intervention as four distinct relations. The primary verdict must not
suggest an emergent influence envelope has been obtained.

### B8 — Barandes/ISP is a boundary comparison, not a property implemented by D11

**Severity:** major

D11 is a Markov kernel on the complete current `History` data structure. It
factorizes into a global enabled-token race followed by local instruments.
It has memory only insofar as the current state stores the accumulated record
graph and strings. The code does not construct an indivisible or genuinely
non-Markovian full-history measure in the Barandes sense.

The literature note mostly respects this, but phrases such as “Barandes
supplies ... an indivisible, generally non-Markovian full-history dynamics”
can make the packet sound like an implementation of that dynamics.

**Repair:** state explicitly that D11 is an ordinary Markov growth law on an
augmented typed-history state. Barandes permits more general full-history
laws and does not select or validate this factorization, filtration, grammar,
or activity race.

### B9 — `SEAL -> COMMIT` is an invented successor rule, not an ontological consequence

**Severity:** major

Replacing terminal SEAL by a zero-population-change COMMIT makes extinction
impossible from one root by construction and produces positive drift. The
arithmetic is correct. But a durable record does not logically require that
the same carrier continue, and a post-measurement quantum output does not by
itself constitute birth of a new record.

Other coherent ontologies include terminal observations, a separate local
birth opportunity after sealing, branching commits, finite lifetimes, or a
primitive path measure. The proposed repair is motivated by the failure but
not forced by SHARD, the click law, or Barandes.

**Repair:** label `COMMIT` a new primitive candidate packet. Derive or
preregister its proposal opportunity, successor identity/ownership,
position/link, evidence/seal semantics, and activity. Do not call terminal
SEAL a proven “type error.”

### B10 — `INTERACTION-INERT` is false as a mechanism label

**Severity:** major

The exact engine proves that JOIN depends on both inputs and can change a
later seal probability. The numerical campaign observes transmitted influence
in some histories. The packet is therefore not interaction-inert; it is
population-extinct and rarely realizes interactions before extinction.

**Repair:** replace the numerical verdict by `POPULATION-EXTINCT /
INTERACTION-SPARSE` or the paper's own `interaction-capable but
population-extinct`. A failed 20/24 prevalence gate cannot be renamed absence
of the mechanism.

## Minor findings

1. **Projectivity terminology.** Summing each next kernel to one constructs a
   consistent path tree, but the receipt does not explicitly push child
   histories through a deletion map and sum canonical fibers. Use `prefix
   mass consistency` unless the deletion map is executed.
2. **Root locality.** A unique root is primitive global initial data, not
   generated by the local grammar. The paper acknowledges this; keep it
   explicit.
3. **Influence scope.** Exact influence witnesses compare selected projector
   probabilities in hand-built cells. They do not classify the full generated
   influence envelope.
4. **Nonexplosion.** Linear total opportunity rate supports the standard
   comparison, but this is a global continuous-time construction; it does not
   supply physical proper times for records.

## Accepted results

Hostile review accepts the following narrower statements:

- the frozen matrices define normalized SPLIT, sibling-MERGE, and terminal
  measurement instruments;
- the finite sequential kernel is fully specified once the global race,
  root, packet constants, and history state are supplied;
- declared ancestry edges lie in the imported positive cone;
- selected local interventions can propagate through sibling partial-iSWAP;
- equal activities make the terminal-SEAL open-port population extinct almost
  surely;
- the failure is conditional on this packet and does not refute ISP or a
  broader SCIR architecture.

## Verdict

**MAJOR REVISION.** The extinction theorem is valuable and the packet is more
complete than earlier builders, but it is not yet a fully incidence-local,
relational, finite-record physical law. It is a globally raced sequential
kernel with incidence-scoped instruments, root-gauge absolute coordinates,
terminal outcome logging, and sibling-only interactions.

The strongest defensible verdict is:

```text
COMPLETE-GLOBALLY-RACED CONDITIONAL PACKET
+ LOCAL SUPPORT INSTRUMENTS
+ ALGEBRAIC POSITIVE-CONE CONTAINMENT
+ SIBLING INTERACTION WITNESS
+ TERMINAL-SEAL POPULATION EXTINCTION
- DECENTRALIZED LOCAL CLICK LAW NOT PROVED
- PHYSICAL RECORD/SEAL SEMANTICS INCOMPLETE
- GENERAL JOIN/BRIDGE LAW ABSENT
- CONSTRUCTION-GAUGE PUSHFORWARD OPEN
- SPACETIME INFLUENCE ENVELOPE OPEN
= COMMIT SUCCESSOR IS A NEW CANDIDATE, NOT DERIVED
```

