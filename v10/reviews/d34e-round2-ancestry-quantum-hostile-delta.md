# D34e round 2 — ancestry/quantum hostile delta

**Frozen target:** commit `bd143fb`.

**Comparison base:**
`d34e-round1-ancestry-quantum-hostile-review.md` at `a880e62`.

**Exact verdict:** **ONE CENTRAL MAJOR REMAINS — 0 BLOCKER / 1 MAJOR /
2 MINOR / 0 NIT.**

The replacement is a large, real improvement.  It reproduces exactly; the
complete `C_r` schema, counter/time augmentation, embedded-versus-timed
probability split, component/disconnected scope, finite-unmarked diagram,
D34c dependency pin and executable branch table are substantially repaired.
However the Branch-F predicate does not select the remote endpoint event that
already existed at the conditioning stop.  It selects the immediate remote
predecessor at propagation time.  A positive-probability intervening D-idle
therefore turns the implemented event true in the interaction branch, directly
refuting the asserted immutable zero.  Round-1 M1 remains open and the row-6 F
verdict is not yet earned.

## 1. Independent reproduction

I ran the replacement under fresh hash salts `0`, `271828`, `999983` with
`-O`, and `424242`.  Every execution exited zero and printed `13/13` with
internal summary digest

```text
88ce0efb91521151d098bc8f68a132cf6b4fc3278d9be032785817a2452714c3.
```

The `424242` stdout was byte-identical to the committed output.  Both have
SHA-256

```text
b168723596fde346b227e6e96f9a00d0304740a498f834809d42afbab346f9bc.
```

Frozen artifact hashes independently reproduce as:

```text
note   0c46f181bc5aaf672e572740e7f47d8dd2a69145f3530ea1f1f61dc2cd15d331
code   e3d3daee3297174183b970299df3289a03ce5491349aa1c43acc2a3a14d26533
output b168723596fde346b227e6e96f9a00d0304740a498f834809d42afbab346f9bc
```

The registered receipt values reproduce:

```text
levels                 1,6,40,304,2576
states                 2927
coarse collisions      2816
predictive stress      106,110,110
B3 updates             35898
disjoint swaps         120276
composition checks     159734
radius lower bounds    1/24,1/1024,1/64000,1/5308416
unmarked classes       4,10
quantum                REFUSAL
```

I also called the parameterized Branch-F constructor at unregistered
`r=4,6,9`.  At each radius:

- the complete carriers were equal;
- the forced-path idle query was true and interaction query false;
- the structural relabeling check passed;
- the computed embedded mass equaled the analytic formula.

The extra exact masses were:

```text
r=4: 1/550731776
r=6: 1/10030613004288
r=9: 1/66483263599150104576.
```

Thus the remaining failure is not a finite-radius arithmetic accident.

## 2. Round-1 finding disposition

### M1 — complete carrier plus one common predictive event: NOT CLOSED

The **carrier half** is closed.  `complete_radius_carrier` now contains:

- every full actor row owned in the closed radius ball;
- owned wire tips and wire counts;
- every incident endpoint port, including cut ports;
- every complete event touching an owned wire;
- opaque predecessor identifiers when the predecessor event is outside.

The differing D event is at distance `r+1` and touches only D and its leaf, so
the two current `C_r` values are genuinely equal.  Because `C_r` is maximal for
the frozen no-dereference radius class, equality also excludes every encoder
that is a function of that complete restriction, once a valid future-law
witness is supplied.

The **query half is not closed**.  Details and an exact counter-cylinder are in
M1 below.

### M2 — first-applicable outcome machinery: CLOSED FOR THE REGISTERED BRANCHES

E13 now represents each scientific branch with its frozen
`(mu,A,Q,I,S,C)` scope, calculates an outcome rather than storing only a
verdict string, exercises every Paper-21 outcome row, and checks the six
registered results against a frozen expected table.  It correctly separates:

- C/L B3 growing passes;
- the F finite-radius class;
- the F whole-component carrier;
- v9 posterior refusal;
- intrinsic quantum refusal.

B4 is never called `WHOLE-COMPONENT ONLY`; that necessity flag is false.  The
decision machinery itself therefore closes the substance of round-1 M2 for
the actual registered flags.  The F row-6 output remains scientifically false
because its `universal_exclusion` input is supplied by the defective E9 gate,
not because E13 chooses the wrong row from that input.

Minor m2 below records one generic priority-hardening defect outside the six
registered flag combinations.

### m1 — embedded versus timed cylinders: CLOSED

The exact fractions are now explicitly embedded-chain lower bounds, not total
Branch-F event probabilities.  The optional continuous-time number is

```text
p_r * F_Erlang(r+1, rate=r+3; Delta=1).
```

This is correct for the exact component subcylinder: during the selected
`r+1` interactions the component has `r+3` active rate-one clocks and no birth,
so the first `r+1` component-ring waiting times sum to the stated Erlang law.
The reproduced values are

```text
3.959221E-2, 8.871307E-4, 1.367731E-5, 1.598963E-7.
```

They are correctly described as positive lower bounds on the broader event,
not equalities for its full probability.

### m2 — whole component and disconnected dependency: CLOSED IN SUBSTANCE

E10 now states and checks the no-joining hypotheses, adds a multi-step
component-local embedded cylinder, retains the parent independent-Poisson
product theorem as the analytic proof, and scopes disconnected invariance to
continuous construction time and component-local stops.  It does not use fixed
global event depth.  B4 is a sufficient growing upper bound and its necessity
flag is explicitly false.

The remaining full-history composition precision is the fresh minor m1 below;
it does not undermine the strong-Markov sufficiency ceiling.

### m3 — C/L counters and time: CLOSED

A-own-ring and A-wire-event counts are now actual coordinates in the projected
carrier and generator.  Passive reception advances `(0,1)` and root-initiated
events advance `(1,1)` in exhaustive finite row comparisons.  Time is an
elapsed increment from the conditioning stop, not a continuously precise
absolute timestamp silently treated as finite record content.

### n1 — finite past-finite pseudo-gate: CLOSED

E11 now states the exact finite diagram as labeled source-prefix truncation
before mark forgetting.  It neither invents an intrinsic unmarked `4 -> 3`
restriction nor claims a completed-history/v9 posterior theorem.

### n2 — declarative quantum status: CLOSED

E12 verifies the accepted D34c output bytes against

```text
9ce73a693b41f765eff163749ef769ca0cb4ce856ead66d690a63a20331a731a
```

and separately records that the timed controlled D34b-D34c process and
all-instrument kernels are absent.  The finite D34c theorem and auxiliary
`P,E` negative control remain acknowledged, while no intrinsic SHARD
`d_carrier`, `d_op` or `chi_cut` is assigned.  `REFUSAL/UNDEFINED` is still the
correct first outcome for that intrinsic branch; no existing process result is
overlooked.

## 3. MAJOR finding

### M1 — `branch_f_event` follows a later tip, so the advertised immutable zero is false

The frozen prose intends `E_r` to inspect the **pre-existing remote endpoint
event at the conditioning stop**.  That can be a valid single common future
cylinder if the event is fixed by:

```text
the structurally selected remote actor D
+ D's wire ordinal k at the conditioning stop
+ the corresponding immutable event identity D#rk.
```

The two paired pasts deliberately use the same actor role and wire ordinal;
only the event kind differs.  Branch F's future A ancestry carries that exact
event record once propagation reaches A.  Consequently the properly frozen
query

```text
E_r^stop = final ancestry contains the selected pre-stop event D#rk
           and that event has kind idle
```

is one gauge-covariant licensed event with

```text
P(E_r^stop | h_idle) >= p_r > 0,
P(E_r^stop | h_interaction) = 0
```

regardless of later D events.  The ordinal is preserved under nominal actor
relabeling, so this repair does not require a preferred Ulam spelling.

The executable does something else.  `structural_inward_endpoint` follows the
immediate D-wire predecessor of the first inward interaction.  It does not
accept or compare the endpoint event ID saved at the conditioning stop.
`branch_f_event` therefore asks whether **whatever D event is immediate at
propagation time** is idle.

I constructed the following positive counter-cylinder from each interaction
past:

1. D performs one additional idle after the conditioning stop;
2. the registered inward interaction chain then occurs exactly;
3. evaluate the current `branch_f_event`.

The predicate becomes true at every registered radius.  Exact results are:

| `r` | pre-stop interaction event | later idle selected by code | `branch_f_event` | positive added-idle-plus-path mass |
|---:|---|---|---:|---:|
| 0 | `B#r2` | `B#r3` | `True` | `1/144` |
| 1 | `B/1#r2` | `B/1#r3` | `True` | `1/8192` |
| 2 | `B/1/1#r2` | `B/1/1#r3` | `True` | `1/640000` |
| 3 | `B/1/1/1#r2` | `B/1/1/1#r3` | `True` | `1/63700992` |

All masses are conditional embedded probabilities after the interaction past
and are strictly positive.  Hence, for the implemented event,

```text
P(branch_f_event | h_interaction) > 0,
```

not zero.  The Boolean called `immutable_zero` checks only that the old
interaction record remains kind `i` along the **forced no-intervening path**;
it never checks that the query continues to select that old record under other
futures.  The finite E9 specimens and the gauge regression therefore do not
gate the advertised statement.

**Required repair:**

1. save the common pre-stop endpoint selector `(D role, wire ordinal k,
   event ID)` in the witness specification;
2. define the licensed event by membership and kind of that exact immutable
   event in the future A ancestry, not by the immediate predecessor at
   propagation time;
3. transport both D's structural role and ordinal under the gauge map;
4. test the positive idle subcylinder and immutable interaction zero;
5. add hostile interlopers before propagation: D-idle, D-interaction, unrelated
   actor events and arbitrarily many D events;
6. show all interlopers can change the immediate tip but cannot change the
   selected pre-stop event kind;
7. only then set `universal_exclusion=True` for every finite `C_r` and emit
   Paper-21 row 6.

The complete-carrier equality and all-`r` path construction do not need to be
discarded.  The defect is exactly the endpoint selector and the false zero.

## 4. Fresh MINOR findings

### m1 — B4's declared composition gate omits B4's event-history fields

The B4 carrier includes wire tips and persistent event records.  E7's
`region_message` and `compose_messages` cover actor rows, boundary references,
endpoint ports and shared graph edges, but not event contents, event ownership,
wire tips or predecessor references.  E10 sets B4 composition to

```text
e7_ok and unique_event_ownership,
```

where `unique_event_ownership` only checks unique IDs and that the initiator is
touched.  It does not construct and compare the composed full-history carrier.

The whole-component Markov state remains an obvious sufficient upper bound;
this is not a necessity or screening counterexample.  But Paper 21's
all-future pass consumes a typed composition flag.  Either:

- extend regional messages to owned event records, shared-event references,
  wire tips and predecessor links and compare their union with direct B4
  projection; or
- declare composition not applicable for an intentionally indivisible B4
  carrier and make that scope explicit in the outcome rule.

Until then the B4 **sufficiency ceiling** survives, while its fully flagged
Paper-21 row-3 certification has this minor proof gap.

### m2 — the decision unit tests do not exercise conflicting true predicates

The registered branch table has sensible, nonconflicting flags, so round-1 M2
is closed for those branches.  The generic decision function nevertheless
does not exactly implement priority under inconsistent or overlapping raw
predicates.  Rows 2 and 3 are defined with

```text
not whole_necessary and not global_necessary,
```

so a specimen with a proved carrier and a later necessity flag skips the
earlier carrier row instead of selecting the first true row or rejecting the
inconsistent flags.  The eight unit cases activate one row at a time and never
test collisions.  The subsequent “no earlier raw row” check is tautological
after `selected_index` has already been chosen as the first true raw index.

Repair by defining each Paper-21 row predicate independently, selecting the
first true row, and adding pairwise-collision tests.  Logically impossible flag
combinations may instead fail explicitly.  This does not alter the registered
verdicts once E9 supplies a valid universal-exclusion input.

## 5. Required claim disposition at `bd143fb`

| Claim | Delta disposition |
|---|---|
| Complete `C_r` carrier equality | **PASS** |
| All-finite-`r` inward construction and exact `p_r` | **PASS** |
| Optional Erlang timed lower bound | **PASS** |
| Gauge-covariant forced-path specimen | **PASS** |
| Implemented common-event immutable zero | **FAIL — M1** |
| Row-6 universal finite-radius exclusion | **NOT EARNED until M1 closes** |
| B4 whole-component sufficiency | **PASS** |
| B4 necessity/minimality | **OPEN and correctly not claimed** |
| Disconnected invariance at continuous/local stops | **PASS** |
| Fixed-global-depth locality | **not claimed; correctly negative/control** |
| Finite unmarked diagram | **PASS at finite source-prefix width** |
| Intrinsic quantum branch | **REFUSAL/UNDEFINED — PASS** |
| Registered verdict ordering machinery | **PASS, contingent on truthful inputs** |
| Generic verdict collision hardening | **m2 repair required** |

The maximum defensible Branch-F statement is currently:

> **COMPLETE FINITE-RADIUS CARRIER PAIRS AND POSITIVE ALL-`r` INWARD
> PROPAGATION CONSTRUCTED; THE COMMON IMMUTABLE-EVENT LAW OBSTRUCTION AWAITS
> ENDPOINT-ORDINAL REPAIR.**

C/L retain their query-relative all-future growing B3 results.  B4 remains a
sufficient growing ceiling, not a necessity theorem.  The intrinsic quantum
branch remains correctly refused.

## 6. Openings investigated and next moves

### O1 — endpoint-pinned ancestry cylinder

This is the immediate repair.  The query must follow a **fixed event identity
through ancestry**, not follow the actor's moving tip.  Once implemented, the
intervening-idle attack becomes a positive regression for immutability rather
than a counterexample.

### O2 — adaptive frontier between `C_r` and B4

After O1 closes, the substantive open remains whether full ancestry can be
screened by a growing, non-radius frontier smaller than the literal component:
live wire tips plus the exact immutable records that can still return.  The
finite-radius row-6 theorem will not exclude that carrier family.

### O3 — B4 event-record union

Extend the typed regional algebra from graph ports/edges to event ownership,
wire tips and predecessor references.  This both closes m1 and supplies useful
machinery for the adaptive-frontier investigation.

### O4 — finite quantum branch versus intrinsic lift

The D34c hash pin confirms that the finite operation family remains available.
A separate finite operational-boundary study can measure its finite-domain
widths.  The intrinsic D34e branch still requires the timed controlled
D34b-D34c process and all-instrument kernels before any SHARD quantum width is
defined.

## 7. Next hostile delta gate

The next delta should refuse to close M1 unless it independently observes all
of the following:

1. the two current `C_r` values are equal;
2. the selected endpoint event identity and wire ordinal are identical across
   the paired pasts;
3. the idle past gives a positive exact subcylinder;
4. the interaction past gives zero for the **same pinned event**;
5. later D idles/interactions do not change that zero;
6. relabeling transports the endpoint role and preserves the ordinal;
7. the proof is parameterized for arbitrary finite `r`;
8. E13 receives row-6 truth only from that repaired gate.

No source artifact is terminal at this delta.  Round-1 M1 remains open;
round-1 M2 closes for the registered branches.
