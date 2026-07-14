# D34f round 1 — ancestry/quantum hostile review

**Frozen target:** commit `4c24987`.

**Reviewed artifacts:** sections 11--12 of
`note-d34f-component-tomography-and-necessity.md`,
`code/d34f_component_tomography_exact.py`, and
`data/d34f_component_tomography_exact.out`.

**Exact verdict:** **ANCHORED COMPONENT-IDENTITY CORE SURVIVES; TWO SOURCE
REPAIRS REQUIRED — 0 BLOCKER / 0 MAJOR / 2 MINOR / 0 NIT.**

The fresh A-idle is genuinely a Branch-F observable rather than a hidden
pre/post mark.  Keeping the complete future A-touching trace, rather than only
the final ancestry, defeats later-cut emulators.  Initiator ordinals and
immutable records defeat event reuse.  Explicit extra-record attacks also
fail, including one where a remote old idle really does remain outside the
final A ancestry: the extra branch's attachment-birth record is nevertheless
forced into the echo and changes the observable trace.

The core predictive-injectivity result therefore survives this review.  The
two minors concern what must be written to own that result precisely.  First,
the all-finite proof currently asserts rather than proves why every unmatched
extra branch leaves an unavoidable attachment witness.  Second, an arbitrary
exact sufficient carrier need not be *only* a lossless recoding; it may be a
strictly finer representation.  Minimal exact carriers are the objects
bijective to the component gauge class.

## 1. Independent reproduction

The frozen artifacts independently hash as:

```text
note   f29b34b5d4b0ce1b56ec98fcc2caa7954cd106a79110988047d8763d15bbf053
code   906687d7dae9776cb707dd040de8970c2aee72096b2e0a636f97e5bdb1e6182a
stdout ff2365ad8c5cf85d7e463d42b8a1f039b2a58d987229de3e606026f10c4a5eea
```

The historical pin and anchored replacement pin exist at `7a5f2fb` and
`eea9474`, both before the executable.

I reran the exact program under fresh hash salt `999961`.  It exited zero with
`11/11`, produced stdout byte-identical to the committed file, and reproduced
internal digest

```text
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee.
```

The exact receipt ledger is:

```text
reachable levels                 1,6,40,304,2576
cumulative states                2927
wire incidences                  20148
sorted/reverse sweeps            2927/2927
anchored echoes                  2927
gauge checks                     351
gauge classes/traces             351/351
continuation emulator attempts   7410
equal/lower-order emulators      0
bare equal-order coefficients    1/1152 versus 1/576
anchored q/q+1 coefficients      1/192 versus 1/1536
binary family sizes              2,4,8,16,32,64
finite gauge classes             1,6,40,304
```

All discrete values are `Fraction` exact.  Exponential/Erlang evaluations use
110-decimal working precision and are evaluations of named analytic formulas.
The commit range is also clean under `git diff --check`.

## 2. Is the fresh anchor actually observable? — yes

Branch F is a future process, not merely one final DAG.  It supplies, in
sequence, every future event touching A, each event's complete persistent
ancestry, and that future A event's elapsed time from the conditioning stop.

The anchor is the prescribed first A-idle event

```text
a_* = A#r(current A own-ring count + 1).
```

It is directly one of the future A-touching outputs.  Its “after the stop”
status therefore comes from membership in the future output sequence, not from
an invented mark inside old ancestry.

The preorder broadcast starts with A's current anchored tip.  Each subsequent
parent-to-child interaction inherits the parent's anchored tip.  The
postorder return then inherits the child's anchored tip.  Inductively every
one of the `2n-1` target events contains `a_*` in its predecessor ancestry.
Their post-anchor status is consequently visible from the same predecessor DAG
that Branch F already returns.

The fingerprint needs no remote timestamp.  Its measurable cylinder is:

- the specified finite prefix of future A-touching record/ancestry outputs;
- with the final echo A-event occurring by elapsed time `Delta`.

The internal echo-event times are not observed or consumed.  The structural
receipt omits exact timestamps consistently; the timed test uses only the
final future A-event's licensed elapsed time and the exact Erlang subcylinder.

Thus the replacement does not smuggle in a pre-stop/future bit on an old
record, a remote clock, or an intervention not present in passive Branch F.

## 3. Alternative conditioning-cut attacks

### 3.1 Earlier cut: catch-up can imitate the trace, but costs one event

Let the target past contain one old B-idle.  Its anchored echo uses three
target events:

```text
A idle anchor; A -> B; B -> A.
```

Starting instead from the seed, one can produce the same Branch-F trace by

```text
B idle catch-up; A idle anchor; A -> B; B -> A.
```

The first event is not A-touching and is indistinguishable inside the final
ancestry from the target's old B-idle.  This is the correct hostile emulator,
and the executable explicitly observes

```text
target trace == catch-up trace,
target order 3,
catch-up order 4,
leading coefficients 1/192 and 1/1536.
```

So the anchor does not falsely make old-versus-new ancestry directly visible.
It does exactly what the repaired proof needs: it prevents any prescribed echo
operation from being borrowed before the stop, leaving catch-up at order
`q+1`.

### 3.2 Later cut: final ancestry alone would fail, complete future trace does not

I conditioned the same target immediately after its A-idle anchor and then ran
only `A -> B; B -> A`.  The final ancestry still contains the anchor, but the
complete future traces differ:

```text
target future A-touching outputs     3
later-cut future A-touching outputs  2
complete traces equal                False
```

At the later cut the anchor is an ancestor of a future output, but it is no
longer itself a future A-touching output.  This is why section 11.2's use of
the complete future A-touching trace is load-bearing.  No hidden cut mark is
needed.

### 3.3 Own-ring ordinal attack

The target anchor and echo operations carry initiator-own-ring IDs.  If an
alternative past is missing an old initiated event, its next event receives
the missing ordinal, while the target anchor/echo event has the subsequent
ordinal.  One event cannot fill both roles.  If the alternative already
contains the target ordinal with a different immutable kind or ancestry, it
cannot overwrite that record.  These ordinal/persistence facts close the
obvious duplicate-ID and moving-tip emulators.

## 4. Extra old records and actors

I attacked the case left implicit by section 11.3 in three ways.

### 4.1 Extra old record on a target actor

Adding an old idle to an actor in K and then running K's same `q` target
operations does not reproduce K's trace.  The first later touch of that actor
inherits its complete current tip, and T1 forces the extra idle into the echo.

### 4.2 Extra old idle on a target leaf

Take K to contain the three-actor tree `A--B--C`, and let K' add one old C-idle.
Running K's same five anchored operations on both gives:

```text
same-q Branch-F traces equal       False
extra C-idle in final A ancestry   True
```

The broadcast/return touches C, so its old wire is collected.

### 4.3 Extra branch whose remote idle stays outside ancestry

The sharpest attack starts from target K=`A--B`.  Let K' contain an extra
B-born leaf C and then an old C-idle.  Run only K's three target operations on
K', deliberately never touching C.  The exact observations are:

```text
extra C-idle outside final A ancestry       True
attachment birth B#r1 inside A ancestry     True
same-q Branch-F traces equal                 False
source final A ancestry IDs                  A#r1,A#r2,B#r1,B#r2
```

This defeats the naive statement that *every* extra record itself must return.
The remote idle need not.  But C can belong to A's connected component only
because of its persistent birth event, and that event touched B.  K's echo
touches B, so wire persistence inevitably carries the attachment witness into
A.  The event ID also shifts B's later ordinal.

More generally, after matching the target trace's actors/old records inside
K', choose the first extra actor on any path out of that matched rooted tree.
Its birth record touched a matched parent.  The target echo touches every
matched actor, hence that birth record enters the observable trace.  If there
is no extra actor, every extra record touches a matched actor directly and is
collected by the same argument.

This closes the extra-record counterexample in substance.  Minor m1 records
that the analytical proof must actually state this argument.

## 5. Emulator-search and finite-evidence scope

E8 proves two different finite facts and narrates them separately:

1. all 351 registered depth-at-most-three gauge classes have distinct traces
   under their own canonical echoes; and
2. 7410 direct continuation attempts find no nonisomorphic emulator for the
   two small target states within three events.

The second search is intentionally small: its sources are the seed and
depth-one states, and its targets are the seed and one B-idle state.  It does
not computationally exhaust arbitrary components or arbitrary conditioning
cuts.  The code says “no tested” emulator, and the note says finite enumeration
is only a regression.  There is therefore no finite-to-infinite overclaim at
the executable level.  The all-finite theorem stands or falls on the anchored
catch-up and extra-witness lemmas, not on `7410`.

The canonical trace uses only future A-output events and their ancestor
records.  Although its implementation minimizes labels over the actors in the
post-continuation state, unused labels cannot improve the minimum ahead of
labels appearing in the trace; and any connected extra actor relevant to an
echo emulator exposes at least its attachment birth.  I found no hidden-state
distinction consumed by the registered equality test.

## 6. Predictive identity and lossless coding

The correct implication of anchored tomography is:

```text
B(h)=B(h')  =>  [K_A(h)]_g=[K_A(h')]_g
```

for every deterministic exact sufficient Branch-F carrier B.  Therefore B
must determine the component gauge class.  Conversely the component class is
sufficient, so the **minimal predictive quotient** is isomorphic to
`[K_A]_g`.

This does not require duplicate cached fields.  Ring/birth counts, carrier
parity, degree and tips may be reconstructed from the persistent legal event
DAG and seed.  A minimal code can remove those redundancies while remaining a
lossless code of the gauge class.

It also does not prohibit a nonminimal sufficient carrier from storing extra
information.  That distinction is minor m2 below.

## 7. Quantum, profinite and geometry ceilings

The provisional result stays entirely classical and chosen-law-relative.

- No D34b coefficient, grammar, seed or record operation is derived.
- No timed controlled quantum process, quantum operation law or intrinsic
  quantum boundary is constructed.
- The serialized marked-prefix inverse-limit host is not identified with the
  v9 unmarked stem spectrum.
- No construction-order-gauge bonding maps or continuity of the predictive
  map on a completion are proved.
- No causal speed, Lorentz cone, dimension, proper-time conversion or value of
  `G` follows.

The executable's E11 ceiling flags all of these stronger statements `OPEN`.
I found no D34c, profinite or geometry theorem smuggled into the component-
identity row.

## 8. MINOR findings

### m1 — the all-finite extra-record case needs the attachment-witness lemma

Sections 11.3 and 12.1 currently say only:

> an altered or extra immutable record makes the exact fingerprint impossible.

That sentence is not self-evident.  The explicit extra-leaf attack shows why:
an extra old record on an unvisited extra leaf can remain outside final A
ancestry.  What saves the theorem is the different, unavoidable record by
which the extra branch was attached.

The finite emulator campaign does not cover this statement at arbitrary size,
so the analytical proof must carry it.

**Required repair:** add the first-unmatched-attachment argument from section
4.3, explicitly using the connected birth-tree grammar and T1.  Separate:

- extra records on matched actors, which are collected directly; and
- extra actors/subtrees, whose first attachment birth touches a matched actor
  and is collected even if later records inside the extra subtree remain
  hidden.

Then state that an altered record is likewise immutable and collected once its
matched wire is touched.  This closes the `zero` branch of the all-finite
catch-up dichotomy without claiming every extra record individually returns
under the target K echo.

### m2 — arbitrary sufficient carriers need only determine K; only minimal ones are recodings

Pinned T5 concludes:

> every exact alternative is a lossless recoding of its gauge class.

The displayed implication proves that an exact sufficient carrier cannot merge
two different component classes.  It does not forbid a carrier from being
strictly finer, for example `[K_A]_g` together with an irrelevant auxiliary
bit or a retained gauge serialization.

**Required repair:** replace the universal sentence by:

> every exact sufficient carrier determines `[K_A]_g`; every minimal exact
> carrier is a lossless recoding of the component predictive quotient, while a
> nonminimal carrier may retain additional information.

Section 12.1's sentence about the **minimal exact predictive state** is already
correct.  This repair changes no injectivity theorem, information lower bound
or decision row.

## 9. Final disposition

| Audit target | Disposition |
|---|---|
| Fresh exact receipt | `11/11`, byte-identical, hashes exact |
| Fresh anchor as Branch-F output | observable |
| Hidden old/future ancestor mark | not used |
| Complete future A-touching trace | load-bearing and correctly used |
| Earlier conditioning cut | same trace only at order `q+1` |
| Later conditioning cut | loses anchor as future output |
| Event IDs/own ordinals | close reuse/double-duty attacks |
| Extra old target-actor record | collected |
| Extra remote leaf record | may remain hidden, but attachment witness is visible |
| All-finite attachment proof | **m1 repair required** |
| Component predictive quotient | survives |
| “Every alternative is a recoding” | **m2 wording repair required** |
| Quantum/profinite/geometry ceilings | clean |

**Closing count:** **0B / 0M / 2m / 0n.**

**Recommendation:** retain the provisional
`COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED` result, but do not promote D34f to
terminal until m1's all-finite attachment lemma and m2's minimal-versus-
nonminimal carrier distinction are committed and independently checked.  No
new probability campaign or quantum/geometry branch is required for these
repairs.
