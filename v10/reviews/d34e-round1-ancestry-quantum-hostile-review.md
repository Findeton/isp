# D34e round 1 — ancestry/quantum hostile review

**Frozen target:** commit `a880e62`.

**Artifacts audited:**

- `note-d34e-predictive-record-dag-boundary.md`;
- `code/d34e_predictive_boundary_exact.py`;
- `data/d34e_predictive_boundary_exact.out`;
- the inherited D34b component-factorization and D34c finite-quantum claim
  boundaries consumed by E8 and E10.

**Exact verdict:** **MAJOR REPAIR, CORE CONSTRUCTIONS SURVIVE — 0 BLOCKER /
2 MAJOR / 3 MINOR / 2 NIT.**

The receipt reproduces and its arithmetic is clean.  The coarse C/L theorem,
the all-`r` ancestry construction, the connected-component upper bound, the
finite unmarked warning and the intrinsic-quantum refusal all have sound cores.
The central Branch-F conclusion is very likely true and the existing
construction contains the ingredients of its proof.  It is not yet an exact
predictive-law obstruction at receipt strength, because the code never defines
one licensed future event and checks its two conditional probabilities.  The
dependent scorecard also does not implement the frozen first-applicable verdict
rule or freeze the carrier class on which its F verdict depends.

## 1. Independent reproduction

I executed the receipt under fresh hash salts `0`, `1`, `8675309` and
`314159`.  Every run exited zero and printed the same:

```text
gates=11/11
levels=1,6,40,304,2576
states=2927
collisions=2898
rate_gap=1/2240
signatures=110,110,110
radius_masses=1/24,1/1024,1/64000,1/5308416
prefix_classes=4,10
quantum=REFUSAL
```

The `314159` stdout was byte-identical to the committed output.  Both have
SHA-256

```text
81dc0a289631f97961a661fda9ce3b3aed36b40e298024173cbc693998eb2586
```

The internal summary digest reproduced as

```text
48d83ba568052d4822278f43efe0c3a268e268e6372e642219b6b400c027d3fd.
```

The source hashes at the frozen target are:

```text
note   5454e16c245c739f72a28f111f121acd0a11eb24119cc337fb2451b3615dcd99
code   53205d8a412b63bc0382f6ee6f7e2c3d2570105ecd54b684c66b1e02afa20f47
output 81dc0a289631f97961a661fda9ce3b3aed36b40e298024173cbc693998eb2586
```

No float enters the discrete Branch-F, component, unmarked-shadow or quantum
gates.  The independently exposed Branch-F past/path masses are:

| `r` | idle-past embedded mass | interaction-past embedded mass | exact inward consecutive-path mass |
|---:|---:|---:|---:|
| 0 | `1/48` | `1/192` | `1/24` |
| 1 | `1/768` | `1/3072` | `1/1024` |
| 2 | `1/15360` | `1/61440` | `1/64000` |
| 3 | `1/368640` | `1/1474560` | `1/5308416` |

All are positive and agree with the code's general construction.

## 2. Findings that survive hostile attack

### 2.1 The all-`r` construction is physically viable

For registered actor radius `r`, the code grows a path

```text
A -- ... -- D -- E
```

with `D` at distance `r+1`.  The two current pasts differ only in D's latest
event:

```text
h_n:  D idle,
h_i:  D interacts with E.
```

Both pasts are reached by positive embedded cylinders.  The differing event
is wholly outside the owned radius-`r` actors.  The same ordered sequence of
`r+1` inward child-to-parent interactions then propagates D's existing tip to
an event on A.  Each step has embedded probability

```text
1 / [8(r+3)],
```

so the displayed path probability

```text
p_r = [1 / (8(r+3))]^(r+1)
```

is exact and positive.  Event records are immutable, so the old D event in the
final A ancestry is idle in one branch and interaction in the other.  No
finite-`r` arithmetic failure was found, and the formula extends analytically
to every finite `r`.

### 2.2 A common Branch-F query can be built—but is not yet the receipt gate

The construction can genuinely distinguish conditional future laws.  A
licensed, record-only event can be chosen as:

> at the next A-wire event, the persistent ancestry contains the structurally
> selected inward predecessor chain and its pre-existing remote endpoint
> record has type `idle`.

Call this event `E_r`.  The exact consecutive global path used by the receipt
is a positive subcylinder of `E_r` from `h_n`, so

```text
P(E_r | h_n) >= p_r > 0.
```

From `h_i`, the selected pre-existing record is already an immutable
interaction record, so

```text
P(E_r | h_i) = 0.
```

This avoids treating the absence of unrelated global events as part of the
Branch-F readout: the exact consecutive sequence supplies a lower bound, while
`E_r` itself is measurable from the next A record and its durable ancestry.
The event can be defined by typed structural position rather than literal Ulam
names, so relabeling gauge is not an obstruction.

Thus the intended obstruction is not refuted.  Finding M1 below concerns the
missing formal carrier/query/probability gate, not a counterexample to the
mathematics.

### 2.3 Whole component is sufficient; necessity remains open

B4 retains the complete current D34b configuration of A's connected component,
including actors, adjacency/eligibility, carrier/counter rows, wire tips and
persistent events.  The parent D34b strong-Markov/product theorem makes that
component an all-future sufficient upper bound at continuous construction time
and the licensed component-local stopping scopes.  Since the chosen law never
joins disconnected components, no future A ancestry can acquire a record from
a disconnected component.

The text does **not** claim that B4 is minimal or necessary.  That restraint is
correct.  The fixed-radius obstruction does not exclude a compressed growing
frontier, cut message or other non-radius encoding smaller than the literal
component.

### 2.4 Disconnected negative control is correct at its licensed clocks

Adding the independent `P--Q` component leaves A's continuous-time component
generator and every A-component future law unchanged.  Hence the literal
global configuration is unnecessary for the passive C/L/F queries.  This
statement would be false at fixed **global event depth**, where additional
remote actors change the next-global-event denominator, but the pin explicitly
labels that depth an auxiliary locality-negative control and does not use it
to certify screening.

### 2.5 The finite unmarked shadow claim stays finite

E9 correctly proves only that:

- the finite marked path law pushes forward to finite unmarked orders at the
  tested source prefixes;
- depth-four source-prefix mass restricts to depth three;
- the same one-point unmarked order can arise from an idle or interaction
  history while the retained A carrier, and therefore a later marked output,
  differs.

It explicitly refuses a v9 posterior-sufficiency, completed-history or
profinite theorem.  No stronger stem claim is consumed by E11.

### 2.6 Intrinsic quantum REFUSAL/UNDEFINED is the correct first verdict

The corpus supplies two relevant but insufficient finite objects:

1. the D34c strongly positive finite typed-DAG operation family and its
   conditional finite-down-set sewing theorem;
2. the auxiliary `P,E` causal-break negative control.

Neither is a timed controlled D34b-D34c process family on the D34e histories.
No supplied object gives `P(r|I,h)` for every licensed future instrument from
each D34e past.  Therefore assigning SHARD `d_carrier`, `d_op` or `chi_cut`
would be an overclaim.  E10 correctly assigns none and emits
`REFUSAL/UNDEFINED`.

This refusal does not erase the accepted finite D34c result.  A separately
frozen finite-D34c operational-boundary branch could earn a `FINITE-DOMAIN`
answer; it would not answer the intrinsic timed branch audited here.

## 3. MAJOR findings

### M1 — E7 does not yet gate predictive-law inequivalence or a complete carrier class

The executable currently establishes:

```text
radius_projection(h_n) == radius_projection(h_i),
the selected inward path has positive mass,
the two forcibly evolved final ancestries are different.
```

Its final Boolean is only `ancestry_idle != ancestry_interact`, together with
the two record kinds.  It never constructs one query `E_r`, verifies that it
belongs to the frozen Branch-F readout, or checks

```text
P(E_r | h_n) > 0 and P(E_r | h_i) = 0.
```

Different outputs under one coupled future realization are not, in general,
enough to prove different marginal future laws.  Immutability makes the desired
zero-probability event available here, but that argument is presently in the
reviewer's reconstruction rather than a fail-closed receipt gate.

The carrier side is also under-typed.  `radius_projection` stores owned actor
rows and tip identifiers, degree-only external references, and only events
whose entire touched set is inside the radius.  It does not encode the full
record-native restriction promised by “every fixed actor radius”: complete
inside event contents, cross-cut events touching an inside wire, typed
predecessor references and the permitted treatment of ancestry references are
not frozen.  The paired histories appear equal even under the natural stronger
restriction because their sole differing event is wholly outside, but the code
does not prove that equality.

**Required repair:**

1. define a covariant complete radius carrier `C_r(h)` with exact actor/event/
   cross-cut fields and ownership;
2. place D strictly outside every record owned by `C_r` and assert
   `C_r(h_n)=C_r(h_i)`;
3. define the structural Branch-F event `E_r` on the next A-wire record;
4. print the two positive past masses;
5. assert an exact positive lower bound `P(E_r|h_n)>=p_r` and the immutable
   zero `P(E_r|h_i)=0`;
6. distinguish `p_r`, the exact consecutive-path subcylinder mass, from the
   generally larger total probability of `E_r`;
7. repeat finite specimens and carry the all-`r` proof symbolically.

This is major because E7 carries the only full-ancestry lower bound, but it is
a repairable proof/typing defect: the frozen construction already supplies the
needed witness.

### M2 — E11 does not implement the frozen first-applicable verdict hierarchy

Paper 21 freezes a branch as `(mu,A,Q,I,S,C)` and requires the first applicable
outcome row.  E11 instead fills a dictionary of verdict strings and checks only
its length, one prefix and one literal string.  It does not evaluate the
outcome predicates, the priority order or most flag values.

The ambiguity matters for Branch F:

- If `C` is the fully defined class of **all fixed-radius record-native
  carriers** and the repaired M1 theorem excludes every member, the applicable
  row is `NO EXACT REALIZATION IN THE DECLARED CARRIER CLASS`, not the weaker
  `CANDIDATE-CLASS OBSTRUCTION`.
- If only the particular `radius_projection` family has been tested, then
  `CANDIDATE-CLASS OBSTRUCTION` is correct, but “every fixed actor radius” must
  not be narrated as exclusion of the wider carrier class.
- B4 sufficiency is an upper-bound fact, not `WHOLE-COMPONENT ONLY`; that row
  requires necessity.  If B4's screening, recursive update, covariance,
  composition and capacity gates are all supplied, its branch should emit the
  earlier `ALL-FUTURE GROWING-CARRIER PASS`.  If they are not, it must remain a
  separately labeled sufficient ceiling with the missing flags printed, not a
  non-schema verdict.

The C/L growing verdicts and intrinsic-quantum refusal have the right apparent
priority, but `e11_ok` would still pass if several other dictionary values or
flags were corrupted.

**Required repair:** represent every branch with the frozen tuple including
`C`; calculate mutually exclusive outcome predicates; choose the first true
row; fail on two true emitted rows or a skipped earlier row; and gate every
covariance/composition/capacity/NSE flag actually consumed by that branch.

## 4. MINOR findings

### m1 — embedded masses are not timed-cylinder probabilities

The past masses and `p_r` divide event intensities by the current active-actor
count.  They are exact probabilities in the embedded global jump chain.  They
are sufficient to prove reachability and a positive future subcylinder, but
they are not the probabilities of histories with exact continuous event
times.  For the timed branch, use open time intervals and integrate the
exponential waiting factors, or label the printed fractions explicitly as
embedded-chain masses and consume them only for positivity.  The total
Branch-F event probability is bounded below by `p_r`; it is not shown equal to
`p_r`.

### m2 — E8's executable control is much narrower than its theorem label

The executable checks the A-local generator rows only on the initial `A--B`
state with and without one remote `P--Q` edge.  The all-future component claim
is valid only because it imports the parent ideal-Harris product theorem.  Pin
that dependency by exact theorem/commit and carry a fail-closed statement of
its hypotheses: independent product sources, no component joining, continuous
construction time or component-local stops, and product rather than initially
cross-correlated components.  A small paired multi-step regression should be
added, while remaining explicitly a regression rather than the analytic
proof.

### m3 — C/L scope counters are narrated but not part of the tested generator state

Branches C and L output A-own-ring and A-wire-event counts, and B3 includes A's
counters.  `boundary_dyn` and `labeled_star_boundary` omit those two counters;
E4 supplies only a hand-written update table.  This is readily repaired by
augmenting the boundary state with the scoped counters and checking the full
projected rows, including passive incoming reception `(0,1)`.  Absolute
continuous construction time should likewise be typed as the supplied stop
coordinate, with future times represented as `t+Delta t`.  The histogram/star
partition itself is unaffected.

## 5. NIT findings

### n1 — E9's `past_finite_specimens` gate is tautological at finite size

The test `|relations| <= |events|^2` cannot fail for a finite relation and does
not validate a completed-history map.  Retain E9 as a finite source-prefix
pushforward regression, remove that pseudo-gate, and keep the existing refusal
of any intrinsic v9 restriction/posterior theorem.

### n2 — E10 is a declared status table, not an executable quantum audit

`quantum_inputs` consists of four hard-coded Booleans, so E10 cannot detect a
missing or later-superseded D34c artifact.  The present values are correct.
Print the exact accepted D34c theorem/status dependency and assert only the
logical refusal from those pinned inputs; do not make the Boolean table look
like an independent reconstruction of the process literature.

## 6. Branch-by-branch disposition

| Branch/claim | Hostile disposition |
|---|---|
| C coarse A-wire histogram/star | **SURVIVES**, with m3 scope-coordinate repair |
| L role-labeled star | **SURVIVES**, with m3 scope-coordinate repair |
| F every fixed radius | **MATHEMATICALLY SUPPORTED; RECEIPT NOT YET ACCEPTED** under M1 |
| F whole component | **SUFFICIENT UPPER BOUND SURVIVES; NECESSITY/MINIMALITY OPEN** |
| disconnected global factor | **IRRELEVANT at licensed continuous/local scopes** |
| finite unmarked source prefix | **PASS AT FINITE WARNING WIDTH ONLY** |
| v9 posterior/profinite factor | **UNPROVED/REFUSED** |
| intrinsic timed quantum boundary | **REFUSAL/UNDEFINED — CORRECT** |
| E11 first-applicable scorecard | **NOT ACCEPTED** under M2 |

The maximum defensible noun before repair is:

> **QUERY-RELATIVE C/L GROWING-BOUNDARY THEOREM + PROVISIONAL ALL-`r`
> FULL-ANCESTRY CONSTRUCTION + WHOLE-COMPONENT SUFFICIENCY CEILING.**

After M1 and M2, the intended stronger noun can be restored if the exact gates
pass.

## 7. Openings exposed by this round

### O1 — close the exact Branch-F predictive witness

Implement `C_r`, the common structural query `E_r`, its positive lower bound
and immutable zero.  This is the cheapest and highest-priority repair because
it converts a persuasive coupling picture into the precise predictive-law
obstruction D34e was designed to test.

### O2 — decide the actual fixed-radius carrier class

Freeze what a radius carrier may read: complete records owned by actors within
the radius, cross-cut incidence, dangling predecessor references, boundary
degrees, identifiers and permitted ancestry traversal.  Then decide whether
the theorem excludes every member of that class (outcome row 6) or only named
candidate encoders (row 7).

### O3 — search between fixed radius and the literal component

The substantive open is no longer “local or global.”  It is whether Branch F
has a recursively updating **growing causal frontier** smaller than the whole
component—for example, an antichain of live wire tips plus exactly the sealed
ancestor summaries that can still return.  Test sufficiency, minimality and
width growth of that frontier.  The all-`r` result rules out a uniform actor
radius, not such adaptive non-radius carriers.

### O4 — promote B4 only after its own carrier gates

Audit the whole-component encoder/update, construction covariance, typed union
or not-applicable composition scope, capacity ledger and NSE flag.  If all
pass, emit `ALL-FUTURE GROWING-CARRIER PASS`; never emit
`WHOLE-COMPONENT ONLY` without a necessity theorem.

### O5 — separate finite quantum progress from the intrinsic refusal

A finite D34c operational branch can ask for its finite predictive quotient and
report finite-domain `d_carrier`, `d_op` and `chi_cut` under a frozen instrument
family.  In parallel, the intrinsic branch must first construct the timed
controlled D34b-D34c process and its intervention kernels.  The finite exercise
must not be advertised as that missing lift.

### O6 — retain the unmarked shadow as a bridge diagnostic

The one-point collision is a useful negative control for any proposed
mark-forgetting posterior factor.  The next real bridge question is whether a
posterior measure on completed unmarked stems screens any declared marked
query—not whether a finite source prefix has a consistent pushforward.

## 8. Required next review

After repair, the delta review should independently verify:

1. exact equality of the complete frozen `C_r` carriers;
2. one common, gauge-invariant Branch-F event `E_r`;
3. positive-cylinder pasts and `P(E_r|h_n)>0=P(E_r|h_i)` at every specimen and
   symbolically for all `r`;
4. the embedded/timed probability distinction;
5. first-applicable verdict selection for every frozen branch tuple;
6. B4 sufficiency without necessity language;
7. disconnected invariance only at licensed stopping scopes;
8. finite-unmarked and quantum refusals at exactly their present widths.

No source artifact should be promoted to terminal D34e status until M1 and M2
close.
