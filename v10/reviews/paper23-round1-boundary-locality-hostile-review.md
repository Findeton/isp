# Paper 23 round 1 — independent boundary/locality hostile review

**Candidate target:** commit
`540ddf164438335a9ce14e849e43168f9af338b3`.

**Terminal source compared:** D34f commit
`398077e`.

**Exact hostile target:** find a Paper 23 theorem step that fails for a legal
finite D34b component, a nonlocal write or global-clock dependency hidden by
the centralized executable, a licensed stop at which the component ceases to
be sufficient, a disconnected factor that changes A's continuous future law,
or a next-step recommendation that silently generalizes beyond the chosen
static birth-tree grammar.

**Exact verdict:** **PASS — TERMINAL D34f IS TRANSFERRED WITHOUT
BOUNDARY/LOCALITY SCOPE DRIFT.**

**Count:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

The synthesis keeps the strongest earned result—whole-component predictive
identity for exact complete durable ancestry—and repeatedly states the inputs
that make it true: persistent wire tips, immutable event references, a static
birth tree, no sealing, no component joining and an unlimited-horizon exact
Branch-F query. It does not promote the diagnostic echo into a global update
algorithm or a component ring count into proper time.

## 1. Candidate and receipt reproduction

The Paper 23 candidate adds only the paper and its ledger entry relative to
terminal D34f. `git diff --check 398077e..540ddf1` is clean.

Frozen artifact hashes are:

```text
Paper 23
bfd3ab67ec12e285b3d5011b07a9b7a6453971f59f7ecad02863ea7f2c3a893e

D34f executable
0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef

committed stdout
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2
```

I reran the terminal executable under fresh `PYTHONHASHSEED=15485863`. It
exited zero, printed `11/11 PASS`, and byte-matched the committed receipt:

```text
fresh stdout SHA-256
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2

internal summary SHA-256
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee
```

The reproduced ledger includes 2,927 reachable states, 20,148 wire
incidences, 2,927 sorted and reversed sweeps, 2,927 anchored echoes, 351 gauge
checks, 7,410 continuation attempts, zero equal-or-lower-order emulators, the
attachment witness `1/1` and the exact `2,4,8,16,32,64` information family.

## 2. Wire persistence and reconstruction

Paper 23's wire lemma uses only the literal event schema. Each new event on
wire v points to v's previous tip and becomes its new tip. Induction gives a
single persistent ancestry chain along every touched wire. No D34b operation
overwrites a tip without retaining its predecessor, mutates an old event or
deletes a predecessor reference.

The reconstruction paragraph also matches the executable and terminal note:

- birth records identify every non-seed actor, parent and immutable tree edge;
- the fixed A--B seed supplies the one edge without a birth event;
- initiator-own identifiers recover contiguous ring ordinals;
- typed interactions recover carrier parity;
- the unique maximal event touching each actor is its current tip.

This determines the legal current component modulo actor-name and
incomparable-serialization gauge. The paper correctly avoids claiming that
cached degree, parity, count and tip fields require separate storage.

I reran the independent 10-actor asymmetric specimen containing 23 old events,
births at several depths, one idle per actor and additional interactions.
Reconstruction was exact and no old event mutation was found.

## 3. Returnability and the attachment boundary

The postorder collection proof is a valid induction specifically because the
current graph is the immutable D34b birth tree. A leaf transfers its current
tip ancestry to its parent. Once every child subtree has returned, an internal
actor's inward interaction transfers their accumulated tips plus its own
history. The last root interaction contains every pre-stop event.

Sorted and reversed sibling sweeps both collected all 23 old events in the
independent branched specimen. This confirms the paper's distinction between
nominal schedule serialization and physical collection.

The first-unmatched-attachment argument is also transferred correctly. If a
source has an extra subtree relative to target K, its first unmatched actor's
birth touched a matched parent. K's target echo necessarily touches every
matched parent. Wire persistence therefore puts the attachment record in the
specified A prefix even when events later confined to the extra subtree stay
hidden.

I repeated the exact extension attack over every actor of every registered
state through level three:

```text
extra-leaf placements                      1096
missing attachment births at A            0
remote internal idles visible at A         0
canonical target-prefix emulators          0
```

This is the sharp behavior claimed by the paper. It neither requires nor
asserts that every internal event of an unmatched subtree is collected by K's
shorter target echo.

## 4. Anchored tomography and observable scope

The paper preserves the essential self-correction: the bare sweep does not
give a universal `m` versus `m+1` discriminator. Its stated equal-order pair
and exact leading coefficients `1/1152` and `1/576` match the receipt.

The fresh A idle repairs the location-of-cut ambiguity. The one anchor,
`n-1` outward broadcasts and `n-1` inward echoes create `q=2n-1` distinct
future records, each descended from the post-stop anchor. A source cannot
borrow one of those records from before the stop.

Paper 23 also keeps the repaired measurability distinction:

```text
S_K = exact first-q component-ring path subevent;
U_K = observable initial Branch-F A-output prefix cylinder.
```

S need not be observed; it only supplies a positive probability lower bound
inside U. The Branch-F cylinder uses no global ring count or hidden remote
time. It is determined by the ordered A records, their typed finite ancestry
and the last specified A event's elapsed time.

The independent hidden-event attack still passes. In a three-actor branch the
five-ring target echo

```text
A idle; A->B; B->C; C->B; B->A
```

and a six-ring path with a C idle inserted after `C->B` have the same initial
A-output prefix. The C idle is absent from final A ancestry. Thus `S subset U`
is genuinely strict, and the hidden path first contributes at order
`Delta^(q+1)`, exactly as Paper 23 says.

## 5. Local execution versus global proof objects

The centralized Python enumerator does not by itself prove physical locality,
so I audited every reachable transition row independently. For each D34b step
I checked that:

- only the initiator row changes for idle;
- only initiator and adjacent target rows/tips change for interaction;
- only the parent and its fresh child change adjacency for birth;
- all unrelated actors, tips and adjacency rows remain identical; and
- every old event record is byte-for-byte unchanged.

Results:

```text
legal transition rows checked             35898
nonlocal actor/edge/tip mutations          0
old-event mutations                       0
```

Each transition rate consults only the initiating actor and its incident
eligible-neighbor list. New identities are parent-relative Ulam names. The
model can therefore be specified by independent actor clocks and atomic
edge-local interactions. Continuous independent clocks make simultaneous
finite-component rings a probability-zero event; a global chronological
serialization exists almost surely but is not a primitive universal commit
clock.

The anchored broadcast/echo is different: it is a globally described
positive-probability continuation chosen by the proof to distinguish two
conditional laws. Nothing requires a physical actor or simulator to discover
the whole tree and deliberately run that protocol. Paper 23 makes this
distinction explicitly in Sections 8 and 12.

“The whole component is the predictive state” therefore means the entire
class is required to specify the exact future distribution. It does not mean
each click reads that class, A privately owns it, or a serial machine scans it
before advancing.

## 6. Licensed stops and clocks

The three stopping scopes remain correctly separated:

1. fixed construction time is a deterministic mathematical conditioning
   scope;
2. an A-own-ring hitting time is determined by A's initiated records; and
3. an A-wire-event hitting time is determined by records touching A,
   including passive neighbor interactions.

The latter two are stopping times of the joint finite-component filtration.
The inherited nonexplosion and strong-Markov property make the current legal
configuration sufficient at each. Poisson memorylessness means no unrecorded
clock age must be appended to `K_A`.

“Absolute construction time is gauge” means the time origin is not a physical
record label. Future elapsed event times are nevertheless part of Branch F.
Paper 23 does not identify construction time, the A-own count, the A-wire
count or the superposed component-ring counter with relativistic proper time.

For the prescribed echo no birth occurs, so the A-component population and
total component rate remain n. Its embedded path mass times
`ErlangCDF(q,n,Delta)` is therefore exact. A catch-up path may change n by
birth, but the proof uses only its finite-prefix positivity and small-time
event-count order, not a constant-rate Erlang formula for that path.

Fixed global event depth is used only for finite enumeration. It is explicitly
excluded as a regional physical clock and as a licensed physical stop.

## 7. Disconnected factorization

I added a disconnected P--Q seed to each of the 351 registered component
states and compared every continuous transition row whose initiator lies in
A's component:

```text
registered A-component states              351
local continuous-rate rows compared        3682
rate mismatches                            0
```

For the seed A idle remains rate `1/2` with or without P--Q. Only an artificial
merged embedded-depth probability changes from `1/4` to `1/8`. The paper uses
the continuous/component law and rejects the merged-depth clock.

At fixed construction time, disconnected processes are independent. A-own
and A-wire stops are measurable from A's component alone, so a remote
component neither triggers the stop nor changes A's post-stop generator. The
component class is sufficient at all three licensed scopes.

This factorization depends on the frozen no-joining grammar. Paper 23 does not
generalize it to a model in which disconnected components can later couple.

## 8. Explicit scope-breaking countermodels

I deliberately applied two operations outside D34b:

```text
delete a current child-parent edge          inward sweep becomes illegal;
dynamically seal the child                 child has zero initiator rows.
```

Both destroy the universal returnability construction. Component joining
would likewise destroy disconnected factorization, and destructive ancestry
erasure would destroy wire persistence.

These are not counterexamples to Paper 23. Sections 2, 3, 12, 14 and 15 state
that D34b has immutable edges and predecessors, no dynamic sealing and no
component joining, and that a changed law must establish its own boundary.
The explicit failures confirm that those hypotheses are doing physical work;
the synthesis does not hide them.

The theorem also remains restricted to complete exact ancestry over an
unlimited future. Finite horizons, coarse observations and approximation may
have smaller predictive carriers without contradicting it.

## 9. Information lower bound

The `2^M` family is carried over without inflation. All histories first grow
the same rooted chain. At each structurally distinguished depth, idle versus
inward interaction is a typed binary choice. The choices add no actors, so all
words can be embedded at one fixed finite-time scope by requiring the finite
path before T and silence afterward. Every such cylinder has positive
probability.

Rooted depths prevent nominal permutations from merging different words, and
the echo returns all choices. Thus at least `2^M` predictive classes and M
worst-case bits are required for each M. This establishes unbounded exact
capacity over growth, not a universal bit density, one-record capacity or
cosmological size estimate.

The illustrative expectations are also exact within D34b:

```text
E[N_T] = 2 exp(T/4);
E[R_T] = integral E[N_s] ds = 8(exp(T/4)-1).
```

Paper 23 labels them construction-time model quantities, not metres, seconds
or real cosmology.

## 10. Claimed next fork

The paper correctly closes one narrow search: under unchanged passive D34b
and exact unlimited-horizon Branch F, no proper predictive quotient of the
component can work. Repeating a search for a smaller exact collar would
contradict the proved injectivity theorem.

Its proposed fork is not presented as a deduction that nature must seal. It
offers two ways to change the boundary problem:

- weaken the observational demand through finite horizon, coarse graining or
  controlled approximation; or
- change the law so a genuine mechanism—horizon, attenuation, sealing,
  disconnection or causal-speed structure—limits returnability.

The paper also retains the independent opens: timed/gauge profinite bridge,
controlled quantum lift, law selection and a geometry rerun only after a law
survives. It explicitly allows the other logical possibility that nature
uses rather than avoids a large exact boundary.

The recommendation is therefore a sound boundary-specific fork, not a proof
that any listed mechanism is physically correct and not a substitute for
deriving the interactive click law.

## 11. Final disposition

The hostile audit found:

```text
wire-persistence counterexamples in D34b       0
reconstruction mismatches                      0
uncollected events in legal branched sweeps    0
extra-subtree prefix emulators                 0
support-nonlocal D34b transition rows          0 / 35898
disconnected continuous-rate mismatches        0 / 3682
licensed-stop or proper-time overclaims         0
static-birth-tree scope drift                   0
next-fork scope drift                           0
```

The accepted statement is exactly model-relative:

> For the chosen passive, persistent, static-birth-tree D34b law and exact
> unlimited-horizon Branch F, the minimal predictive state is A's whole finite
> connected-component history modulo rooted marked gauge, and no uniform
> finite exact capacity suffices over unbounded growth.

It does not derive D34b, define nature's click law, impose a global ledger,
prove quantum dynamics, recover a light cone or dimension, construct proper
time, set physical units or determine G.

**Final count:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

**Final verdict:** **PASS — PAPER 23 TRANSFERS TERMINAL D34f CLEANLY AT THE
BOUNDARY/LOCALITY CLAIM CEILING.**
