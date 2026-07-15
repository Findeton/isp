# D38 round-one record-closed specification hostile review

**Frozen target:** commit `7a3919b`.
**Receipt:** `PASS 9/9`, complete-output SHA-256
`b0e61b087451f216db1696ece836453f5ba403667fbdb5043a67ce17e070c3f6`.
**Lanes:** probability/projectivity/predictive quotient; causal record
closure/authentication; corpus/D26/NSE/sealing/quantum.
**Verdict:** `2 BLOCKERS / 7 MAJOR / 1 MINOR / 0 NIT`.
**Promotion:** withheld.

Fresh executions under seeds `3`, `65537` and `1000003` reproduce the frozen
output.  The four holding rates, 29 atom/tower arithmetic rows, 258 arity
rows, nine `p_r` values, anchor coefficients, attenuation counts, D26 factors
and finite mass-transport numbers are arithmetically correct.  The failures
are architectural and scope failures in the claimed object.

## Blocker 1 — cached heads admit invalid histories

`Boundary.state` and `Boundary.tips` are authoritative unauthenticated cache.
The selected row payloads are compared with that cache, but the record DAG is
not validated as a unique append-only current history.  Exact hostile
constructions validate after:

- rollback to old tips/state after a valid append, followed by stale replay;
- union of incompatible `ROOT_IDLE` and `ROOT_OUT` forks, selecting either
  branch as current;
- insertion of an authentic disconnected event;
- a retargeted edge whose wires and payload endpoints disagree;
- a fabricated parentless current root row with arbitrary counters;
- a cross-wire/nonadvancing root row parented by a neighbor-owned event; and
- duplicate tip keys, which `dict()` silently collapses.

The 14-case battery mutates only one candidate and calls a pure predicate.
Its `target == before` condition is tautological; the hostile value is never
passed through the durable updater.  C3, C4 and C6 are therefore not earned.

**Required repair.**  Derive unique heads and current state from a validated
typed DAG.  Enforce exact per-kind payload/parent schemas, parent closure,
acyclicity, one comparable chain per wire, no forks or disconnected extras,
event parents equal to all prior touched-wire heads, row-transition
derivation, exact edge endpoints and no duplicate head entries.  Exercise
whole-boundary attacks through the actual updater and require byte-identical
pre/post snapshots on rejection.

## Blocker 2 — no regional restriction or cocycle exists

R1 checks four temporal embedded jump kernels.  Each reported tower is the
identity `p(a) sum_b p(b|a)=p(a)`.  There are no indexed regions, incoming or
lateral boundaries, spatial restrictions, or direct-versus-staged regional
conditionals.  R3 updates two independent Python tuple components in opposite
orders and returns the literal cocycle count `2`.  It defines no
parent-closed `r_(F,E)` and does not test
`r_(F,D)=r_(E,D) o r_(F,E)` or update/restriction naturality.

**Required repair.**  Implement explicit nested typed regions, external
predecessor references, parent-closed record restriction and namespaced
transport.  Compare direct and staged restriction on genuine
`D contained in E contained in F`, then compare update-before-restriction with
restriction-before-induced-update.  Instantiate actual positive-cylinder
regional kernels, including holding-time data, and compare direct and staged
conditionals on hostile boundaries.

## Major 1 — the updater is not the physical typed D34b boundary

`NEIGHBOR_BIRTH` increments a degree summary but emits no fresh Ulam child,
child row, port or edge.  The printed touched child is absent from the actual
event wires.  Neighbor own-birth counts are missing, so the next child cannot
be named.  Root/neighbor counters and explicit ports required by the locked
D34e B3 carrier are incomplete, and impossible hand-built seeds validate.

**Required repair.**  Carry actor-owned birth counts, emit a fresh typed child
and incidence records on every birth, execute only reachable D34b cells, and
compare the record-only projected successor with the chosen D34b row.  If the
object remains only query-projected, say so and do not call it a global
self-generating law.

## Major 2 — capacity disclosure is incomplete

The receipt reports touched arity, one width specimen, total records and
parent arity.  It does not separately report actor, record and port counts,
identifier encoding cost, continuous elapsed marks or total width, even
though C7 promises that ledger and the prose invokes unbounded port width.

**Required repair.**  Print a separate empirical/theoretical capacity ledger
with finite specimen values and explicit `UNBOUNDED`, `CONTINUOUS` or `OPEN`
ceilings.

## Major 3 — the generic obstruction criterion is underhypothesized

P,G,R,A,Q,S only requires an observable fresh anchor.  That does not imply
D34f's first-unmatched-attachment lemma, prefix injectivity, reconstruction,
component autonomy, or the `q` versus `q+1` timed catch-up separation for
every nonisomorphic past.

**Required repair.**  Restrict the theorem to chosen D34b, or require for each
finite legal `K` and every `K'` not rooted-marked-isomorphic a Branch-F
measurable anchored prefix `U_K(Delta)` and exponent `q(K)` with positive
order `q` under K and zero or order at least `q+1` under K'.  State the
altered-record and missing-record cases, elapsed-time query, marked-DAG
reconstruction and future-law factorization explicitly.

## Major 4 — the inverse-limit claim exceeds D34f

D38 prints `inverse_limit_boundary=rooted_marked_component_class`.  Locked
D34f proves the finite current component quotient at every legal finite stop
and unbounded worst-case width over growth; it explicitly leaves stronger
timed inverse-limit/profinite identification open.

**Required repair.**  Print the finite-stop quotient and leave the timed or
infinite predictive inverse limit open.

## Major 5 — the escape controls are not load-bearing models

The horizon, seal and attenuation functions are toy projections, not
record-closed laws that retain every other theorem hypothesis.  V6 sealing is
not an exact D34b future read prohibition, and Paper 23 leaves such a physical
seal open.  A bounded actor population also does not bound append-only
unlimited-horizon record information; two actors can accumulate unbounded
history.

**Required repair.**  Label the projections as abstract countermodels, not
existing V6/D34b physics.  Cap the total marked-history state space, record
count or horizon for the bounded-capacity control.  A true
assumption-minimality theorem would need one otherwise-admissible model per
removed premise; leave that theorem open until supplied.

## Major 6 — D26 upkeep is only a conditional interface

D26 prices repeated controlled BORN carriers on one specified coherent
parent line.  The classical D38 updater supplies no coherent line, BORN
carrier, coupling assignment or record-to-system dictionary and does not
identify its update count with physical births.  Generic boundary maintenance
therefore does not automatically inherit `(4/5)^N`.

**Required repair.**  Retain the D26 parameter table only as a conditional
falsifier interface: if a later bridge identifies N same-line D38 maintenance
records with D26 births at `g=9/25`, then the factor follows.  No rate or
generic price follows now.

## Major 7 — inherited anchor data are mislabeled as reproduction

R5 hash-locks and searches D34f output, then hardcodes the four coefficients,
attachment witness and emulator count.  It does not recompute the anchor
construction.  R4's all-size theorem is likewise inherited; its finite rows
are regression specimens.

**Required repair.**  Relabel R5 a hash-locked inherited theorem regression,
or call the antecedent constructors.  Do not count it as new hostile anchor
evidence.

## Minor 1 — parent review status

The D38 note calls both Papers 25 and 26 independently reviewed.  Paper 25 is
coordinator-lineage reviewed with the separate independent stream open;
Paper 26 is independently reviewed.

## Retained result

The chosen local rate arithmetic, bounded touched support, positive fixed
radius witnesses, D34f finite-stop quotient and M-bit lower bound, nonzero
exact attenuation caveat, finite mass-transport example, D34b nonselection
and classical/quantum ceilings survive.  They do not establish the central
record-closed regional noun until both blockers are repaired and independently
re-audited.
