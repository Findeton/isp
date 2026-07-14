# D34f round 1 — predictive/profinite hostile review

**Frozen target:** commit `4c2498772d48273548420c5e483d519976344f91`

**Primary target:** `note-d34f-component-tomography-and-necessity.md`, especially
sections 11--12, with its exact code/stdout receipt.

**Verdict:** **ANCHORED TOMOGRAPHY CORE ACCEPTED; TWO SCOPE/DEFINITION REPAIRS
REQUIRED — 0 blockers / 0 majors / 2 minors / 0 nits.**

The fresh-anchor replacement survives the hostile probability attack that
killed bare-sweep T4.  I did not find an equal- or lower-order anchored
emulator.  More importantly, the universal `q` versus `q+1` statement has a
short invariant proof that covers arbitrary nonisomorphic legal finite pasts,
not only the receipt's `7,410` continuation probes.  Extra records persist into
the echo and make the target trace impossible; missing target records require
at least one additional future event; and the `q=2n-1` anchor/echo events cannot
be borrowed from before the stop because the anchor is itself a future
A-output and every other target echo node has it in its ancestry.

Two precision repairs remain.  First, the note must define the observable
`U_K^anchor(Delta)` as a structural Branch-F **prefix cylinder** and distinguish
it from the underlying exact-first-`q`-component-ring subevent used for its
lower bound.  Second, the finite-level inverse-limit host is valid only for the
discrete event-content skeleton.  Branch F's real elapsed-time marks make the
full timed prefix levels uncountable and not automatically profinite.

Neither repair changes component predictive injectivity, the information lower
bound, or the finite-stop theorem.

## 1. Frozen artifacts and reproduction

The frozen hashes reproduce as:

```text
note
f29b34b5d4b0ce1b56ec98fcc2caa7954cd106a79110988047d8763d15bbf053

code
906687d7dae9776cb707dd040de8970c2aee72096b2e0a636f97e5bdb1e6182a

stdout
ff2365ad8c5cf85d7e463d42b8a1f039b2a58d987229de3e606026f10c4a5eea
```

A fresh execution under `PYTHONHASHSEED=104729` exits zero, prints `11/11`,
reproduces internal digest

```text
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee,
```

and has stdout SHA-256 exactly

```text
ff2365ad8c5cf85d7e463d42b8a1f039b2a58d987229de3e606026f10c4a5eea.
```

The high-value reproduced rows are:

```text
reachable levels                         1,6,40,304,2576
cumulative states                        2,927
wire incidences                          20,148
sorted/reverse sweeps                     2,927 / 2,927
anchored echoes                           2,927
registered gauge classes/traces           351 / 351
direct continuation attempts              7,410
equal/lower-order emulators               0
bare equal-order coefficients             1/1152 / 1/576
anchored q/q+1 coefficients               1/192 / 1/1536
binary families                           2,4,8,16,32,64
finite gauge counts                       1,6,40,304
```

`git diff --check 4c24987^..4c24987` is clean.  All printed discrete masses are
`Fraction` exact; the 110-digit decimal evaluations agree with the analytic
Erlang/exponential formulas.

## 2. CTMC probability and small-time audit

Let `K` have `n` actors.  Its frozen anchored path contains

```text
one A-idle anchor + (n-1) outward interactions + (n-1) inward interactions,
q = 2n-1.
```

No birth occurs on this path, so the component has constant total ring rate
`n`.  The exact probability that the first `q` component rings are the frozen
path and the `q`th completes by `Delta` is

```text
p_echo(K) * ErlangCDF(q,n,Delta),
```

where

```text
p_echo(K)
 = 1/(2n)
   * product_out 1/[4n degree(parent)]
   * product_in  1/[4n degree(child)].
```

This agrees with the code.  Expanding the ordered-jump integral gives

```text
P(S_K(Delta)|K)
 = [product of continuous path rates]/q! * Delta^q
   + O(Delta^(q+1)).
```

The actor-count factors cancel between the embedded mass and the leading
Erlang term, as they should.  The registered `n=2` target coefficient is

```text
(1/2)(1/4)(1/4)/3! = 1/192.
```

For a catch-up path whose actor count changes because of birth, the constant-
rate Erlang expression is not used.  Its small-time leading term is still the
product of its successive continuous transition rates divided by the path
factorial.  The receipt follows that rule and obtains `1/768` for the printed
three-event birth catch-up specimen.

### Why at least `q+1` rings imply the advertised upper order

Fix a finite source state `K'` with `n'` actors.  Before its first `j` rings it
has at most `n'+j` actors because one ring creates at most one child.  Hence all
total rates through any fixed `q+1`-ring prefix are bounded by constants
depending on `K',q`, and

```text
P(number of component rings by Delta >= q+1 | K') = O(Delta^(q+1)).
```

This supplies the CTMC step implicit in section 12.1.  Nonexplosion alone would
not be a sufficient small-time estimate for an arbitrary jump process, but the
linear D34b birth/ring bound is sufficient here.

## 3. Universal emulator attack

The receipt's finite search is deliberately not the proof: its continuation
battery uses two small targets and sources through depth one.  I therefore
attacked arbitrary legal finite `K,K'` by decomposing a putative matching
Branch-F trace around its observed future anchor.

### 3.1 Target trace anatomy

In the target trace:

1. the anchor is the first specified future A-output;
2. all `q-1` broadcast/echo operations are distinct descendants of that
   anchor;
3. every one of those `q` nodes is in a future A record or in the final A
   record's transitive ancestry;
4. every pre-stop event of `K` is also in the final ancestry; and
5. no pre-stop event can contain the future anchor.

Thus the target trace contains `q` distinct anchor-cone nodes that no source
past can pre-supply.  Any realization from any `K'` must generate all `q` of
them after its stop.

### 3.2 Proper extensions and extra unobserved rings

If `K'` contains an extra pre-stop event on an actor used by the matching echo,
wire persistence carries that event into the final ancestry, so the exact
target trace is impossible.  If `K'` contains an extra actor/subtree, its root
birth event touches the first retained actor at the boundary of that subtree;
that persistent event likewise contaminates the matching echo.  This covers
different actor counts, extra idles/interactions and extra birth branches.

An unobserved post-stop ring scheduled after an actor's final inward transfer
can be absent from the A trace, but it cannot help emulate a missing target
record: precisely because it is absent, it supplies no missing trace node.  If
it occurs early enough to supply such a node, it is one additional actual ring.

### 3.3 Strict prefixes and incomparable marked DAGs

If `K'` lacks a target actor, edge or event, a future birth or other event can
create the missing old-complement node before the anchor reaches that wire.
The lack of a pre/post mark on old ancestry allows this catch-up, just as the
note recognizes.  But it does not make the catch-up free.  The target still
contains all `q` distinct anchor-cone nodes, so the missing node is an
additional `(q+1)`st event.

A birth cannot double as the target outward interaction: the exact trace
contains both the old birth record and the new interaction record, with
different kinds and anchor ancestry.  The same argument prevents an old
interaction or idle from being folded into an echo operation.  If the two
pasts have incomparable/altered marked DAGs, the source has both a missing
target node and a persistent incompatible extra node; the latter makes exact
emulation impossible rather than cheaper.

### 3.4 Different cuts and coefficient-only emulators

The bare-sweep counterexample succeeds because a remote event can move across
the unmarked stop while a different sweep event moves to the other side.  It
uses the same number of future rings and only the coefficient distinguishes
the laws.  The executable correctly reproduces `1/1152` versus `1/576` and
rejects bare T4.

The anchor blocks the same exchange.  It is itself a future A-output, and all
target echo nodes contain it.  A pre-stop source event cannot stand in for one
of those nodes; a post-stop catch-up node lacking the not-yet-broadcast anchor
can stand only for an old target node and is additional to the `q` echo nodes.
Therefore a same-order anchored emulator would force the old complement of the
matching trace to be isomorphic to `K`, which makes `K'` gauge-isomorphic to
`K`.  No distinct coefficient-only `q` emulator remains.

This proves the required result pairwise in `K'`.  The big-O constant and the
threshold in `Delta` need not be uniform over all finite source components, and
the note does not claim uniformity.

## 4. Predictive-law injectivity — pass

Once `U_K^anchor` is made a precise Branch-F cylinder, the inference to T5 is
valid.  For every `K'` outside `K`'s rooted marked gauge class,

```text
P_K(U_K^anchor(Delta)) has positive order Delta^q,
P_K'(U_K^anchor(Delta)) is zero or order at least Delta^(q+1).
```

The conditional future laws therefore differ for sufficiently small positive
`Delta`.  Conversely, D34b's exponential future generator is a function of
the reconstructed current component class, so that class is sufficient at the
declared fixed-time and local stopping scopes.  Equality of exact Branch-F
future laws is consequently equivalent to equality of `[K_A]_g`.

The conclusion is about lossless information, not literal duplicate fields.
The event DAG reconstructs ring/birth counts, adjacency, carrier parity and
tips, so a compressed serialization of that same gauge class is allowed.

## 5. Yule and information checks — pass

Every actor births at rate `1/4`, so the component population is a Yule process
started at two actors:

```text
E[N_T] = 2 exp(T/4).
```

Every actor rings at total rate one and each ring creates one event record.
Therefore, for records created after the seed,

```text
E[R_T] = integral_0^T E[N_s] ds
       = 8(exp(T/4)-1).
```

At `T=1`, independent 110-digit evaluation gives exactly the printed prefixes

```text
E[N_1] = 2.56805083337548296814684113612487...
E[R_1] = 2.27220333350193187258736454449949...
```

The `2^M` chain family is also a valid worst-case information lower bound.  Its
structurally placed idle/interaction choices are positive cylinders, are
gauge-distinct, and are recovered by collection.  This proves unbounded
worst-case capacity over finite legal stops; it does not say that one finite
stop already contains infinitely many records.

## 6. MINOR findings

### m1 — pin the observable cylinder separately from the path subevent

Section 11.3 calls `U_K^anchor(Delta)` the “exact gauge-invariant Branch-F trace
... by elapsed time Delta,” while section 11.2 gives an exact probability for
the event that the **first `q` component rings** follow one chosen echo path.
Those are not literally the same event.  Branch F does not report every silent
component ring, and the first-`q` condition is an underlying path subevent used
to lower-bound an observable trace cylinder.

There are two possible readings of “by Delta”:

- an initial structural Branch-F prefix whose final specified A event occurs no
  later than `Delta`, with no restriction after that final echo; or
- the complete A observation up to `Delta`, which additionally requires no
  later A event before `Delta` and therefore carries a survival factor.

Both have the same leading order, but only the first makes the printed
embedded-times-Erlang event an immediate subevent without an after-echo silence
condition.

The notation

```text
P(U|K) >= c Delta^q + O(Delta^(q+1))
```

is also not a well-formed asymptotic inequality because the sign of an
unspecified `O` term is not fixed.

**Required repair:** define

```text
U_K^anchor(Delta)
 = {the initial Branch-F A-output prefix has the canonical finite structural
    echo trace, and its final specified A event occurs by Delta},
```

where intermediate real times are integrated over and nominal names are
quotiented.  Define `S_K(Delta)` separately as the exact first-`q` component-
ring path.  Then state

```text
S_K(Delta) subset U_K^anchor(Delta),
P_K(S_K(Delta)) = c_K Delta^q + O(Delta^(q+1)),
liminf_(Delta->0) P_K(U_K^anchor(Delta))/Delta^q >= c_K > 0,
P_K'(U_K^anchor(Delta)) = O(Delta^(q+1)) or 0.
```

This makes measurability and the lower-bound logic exact without changing T4
or T5.

### m2 — the finite-level inverse-limit host excludes continuous time unless constructed

Section 8 says the “serialized marked-prefix tree has finite levels” and
section 12.3 says its inverse-limit host is available.  That is correct for the
discrete event-content skeleton: at fixed event depth the chosen grammar has
only finitely many labeled structural histories.  It is not correct for the
full Branch-F marked process as currently described, because each future A
record also carries a real elapsed time.  A fixed-depth timed level is already
uncountable, not finite discrete, and is not automatically a profinite level.

The surrounding refusals are otherwise correct: no construction-order-gauge
bonding maps, v9 stem-spectrum identification, predictive continuity or finite
physical completed-history record is claimed.

**Required repair:** say explicitly that the available finite inverse tower is
the **discrete serialized event-content skeleton after forgetting elapsed-time
marks**.  A timed marked completion requires explicit finite observable time
partitions or another declared topology; if it is called profinite, that
topology must itself arise from finite discrete quotients.  Keep continuity of
the timed Branch-F predictive map and the v9 bridge `OPEN`.

## 7. Exact verdict

No blocker or major opening survives.  After the two local precision repairs,
the first decision row is supported at the following ceiling:

> At every legal finite stop of the chosen D34b law, the complete Branch-F
> future law identifies A's entire finite connected-component configuration
> modulo rooted marked gauge and lossless recoding.  The exact carrier has no
> uniform finite information bound over unbounded growth.  This proves neither
> a completed timed profinite bridge nor a v9 posterior, quantum boundary,
> spacetime consequence or law of nature.

**Final count: 0B / 0M / 2m / 0n.**
