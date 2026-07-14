# D34e hostile delta review — predictive probability and profinite stream

**Frozen target:** commit `bd143fb1d757cb46af17d2b471ebed53efad6d82`  
**Reviewed artifacts:** `code/d34e_predictive_boundary_exact.py`, its committed
stdout, and `note-d34e-predictive-record-dag-boundary.md`  
**Independence:** fresh hash salts, an extension through global depth five, and
separate predictive-signature probes not used by the receipt  
**Verdict:** **DELTA REJECTED — 0 blockers / 1 major / 1 minor / 0 nits.**

The replacement genuinely closes the absolute-time/stopping major and the
finite labeled-prefix/profinite wording defect.  It also repairs the raw-
successor recursion and the registered-domain mismatch from the first review.
The remaining major is narrower but exact: E4 still does not compute the
predictive partition of the query frozen in section 3.  It hides the durable
A-own/A-wire count values in successor state instead of emitting them in the
output alphabet, and it exposes silent neighbor births as a literal `tau`
symbol.  The first defect makes histories with observably different next
records merge.  Thus the analytic B3 sufficiency result survives, but the E4
`29,29,29` finite predictive-class claim and dependent `13/13` receipt do not.

## 1. Artifact and deterministic reproduction audit

The frozen hashes reproduce:

```text
code   e3d3daee3297174183b970299df3289a03ce5491349aa1c43acc2a3a14d26533
stdout b168723596fde346b227e6e96f9a00d0304740a498f834809d42afbab346f9bc
note   0c46f181bc5aaf672e572740e7f47d8dd2a69145f3530ea1f1f61dc2cd15d331
```

Fresh runs under `PYTHONHASHSEED=83,104729,271828` exit zero, agree byte for
byte with each other, and the last agrees byte for byte with the committed
stdout.  The printed internal digest is

```text
88ce0efb91521151d098bc8f68a132cf6b4fc3278d9be032785817a2452714c3.
```

All receipt numbers reproduce, including:

```text
reachable levels                 1,6,40,304,2576
cumulative states                2927
coarse-boundary collisions       2816
synthetic signature classes      106,110,110
registered states/classes        111 / (29,29,29)
B3 row updates                    35898
disjoint swaps                   120276
composition pairs                159734
path counts depth 3/4             400/4440
unmarked classes depth 3/4        4/10
```

As an out-of-receipt extension, I regenerated every state through global depth
five.  The level counts are

```text
(1,6,40,304,2576,23800), cumulative 26727.
```

Both the full-to-coarse and full-to-role-labeled generator formulas agree on
all `26,727` cumulative states.  No new counterexample to the analytic row
partition appears just beyond the frozen depth.

## 2. Round-1 finding dispositions

### Round-1 M1 — closed

The replacement makes a definite and physically coherent choice: future C/L
times are elapsed from the conditioning stop and histories related by a common
time translation are identified.  The scoped boundary is now

```text
(carrier, degree histogram, A-own count, A-wire count),
```

and the generator rows update both monotone counters correctly.  The simple
`exp(-q Delta)` calculation is now explicitly limited to the next full boundary
transition.  A-own and A-wire stops are hitting times of the corresponding
projected CTMC counters.  D34b already proves a nonexplosive time-homogeneous
strong-Markov pure-jump process; the arbitrary-state row partition gives its
closed boundary projection, so the standard stopped-process argument applies.

The older section-3 phrase `construction time` is inside the status-declared
historical pin.  Section 16.1 explicitly supersedes it by elapsed time, so I do
not count that preserved history as a live ambiguity.

This closes the old absolute-time major.  It does **not** license omission of
the two durable count values from the future output alphabet; that separate
issue is the major below.

### Round-1 M2 — only partially closed; one major remains

The recursion is now genuinely coinductive in one important sense: it
aggregates exact rates by `(label, previous-horizon successor class)` and no
longer inserts raw successor state.  The registered domain is also correctly
the `111` distinct scoped boundaries reached through global depth four; the
separate `110`-state family is honestly called synthetic.  Those two repairs
are real.

But the labels passed to that recursion are only

```text
A-birth:c0, A-idle:c0, A-outgoing:c1, incoming-to-A:c1, tau, ...
```

They do not contain the post-event A-own and A-wire count values frozen into
every durable Branch-C record.  Putting those values in hidden `after` state is
not enough: coinduction deliberately quotients successor states, while
predictive equivalence is equality of the **observable** future-record law.

### Round-1 m1 — closed

E11 now states exactly the finite diagram it computes:

```text
(u3 o r4->3)_* mu4 = (u3)_* mu3,
```

where labeled-prefix restriction happens before marks are forgotten.  It
explicitly refuses an unmarked `4 -> 3` restriction, a completed v9 posterior,
and a profinite sufficiency theorem.  This is the correct finite ceiling.

### Round-1 n1 — closed

The top status now labels sections 1--14 as a historical pin, records the
rejected first receipt, and identifies sections 16--17 as the replacement.

## 3. MAJOR — E4's output alphabet is not the frozen durable-record query

Section 3 freezes each Branch-C output record as

```text
(time, kind/direction, post-event carrier,
 post-event A-own-ring count, post-event A-wire-event count).
```

The elapsed-time repair changes only the first coordinate.  It does not gauge
away the two counts.  Nevertheless `row_output()` and
`boundary_formula_rows()` emit kind plus carrier only.  The counts occur solely
inside the successor boundary.  Therefore E4 can identify current histories
whose very next durable records have different count values.

An exact reachable witness among the `111` registered states is

```text
left  = (0, ((1,1),(2,1)), own=1, wire=1)
right = (0, ((1,1),(2,1)), own=1, wire=3).
```

E4 assigns the same horizon-one signature to both.  Yet their positive-rate
observable rows include

```text
left  A-idle -> (carrier=0, own=2, wire=2) at rate 1/2
right A-idle -> (carrier=0, own=2, wire=4) at rate 1/2,
```

and similarly every next A event emits wire count `2` versus `4`.  They are not
predictively equivalent for the declared query.

I reran the same coinductive recursion after adding the declared post-event
own/wire values to every non-silent output label.  On the registered domain the
exact class counts become

```text
H=1,2,3: (111,111,111),
```

not `(29,29,29)`.  This is not a numerical tolerance or a minimality debate;
it is a direct output-law distinction.

There is a second query mismatch in the same gate.  A neighbor birth is frozen
as **no A-wire output**, but E4 makes it a literal `tau` output symbol.  The
resulting recursion is a strong transition-system refinement in which hidden
boundary changes are exposed.  It is useful as a sufficient-state diagnostic,
but it is not the canonical predictive partition of the observed C process.
For that noun the silent transitions must be eliminated/aggregated in the
timed hidden-CTMC law (or the audited query must be renamed to the fully
observed boundary-jump process).  Branch L needs the analogous role-labeled
observable construction; E4 currently computes only the coarse recursion.

**Scope of damage.** This finding does not refute B3's all-future screening or
recursive update.  B3 really retains the counters, and its state plus a typed
event deterministically produces the missing output values.  The arbitrary-
state generator partition, inherited nonexplosion, covariance and composition
therefore still support an all-future growing B3 realization after the output
map is stated correctly.  What fails is the claim that E4 has computed the
frozen finite predictive quotient, so E4 cannot pass as written and E13's
dependent `13/13` cannot be terminal.

**Required repair.** Freeze the observable mark first.  It should contain
elapsed output time, event kind/direction, post carrier and post own/wire counts
(plus the licensed incident role for L).  Then either:

1. compute the finite timed/marked output law with silent neighbor-birth
   transitions weakly aggregated, and quotient by equality of that law; or
2. rename the present object as a fully observed boundary-transition
   bisimulation, include the counters in its emitted marks, and do not call its
   class counts the predictive partition of Branch C/L.

Regenerate the code/output hashes and dependent scorecard either way.

## 4. MINOR — the claimed executable B1 horizon split is not gated

Section 17 says the `(106,110,110)` stress counts include the expected B1 split.
They do not establish that assertion.  The synthetic family uses neighbor
degrees only in `1..5`, while the registered B1 left witness is `{2,3,6}`;
therefore the pair is not even contained in that family.  Moreover `e4_ok`
checks only the three total class counts and never compares the named pair.

An independent direct probe confirms the desired mathematics:

```text
sig({2,3,6}, H=1) == sig({2,4,4}, H=1),
sig({2,3,6}, H=2) != sig({2,4,4}, H=2).
```

So this is a missing receipt assertion, not a counterexample.  Add the explicit
pairwise equality/inequality gate and print it separately from the synthetic
class counts.

## 5. Remaining requested audits

### Analytic all-future promotion and count stopping — pass

The analytic row partition is structural: only A's own rows, births of current
A-neighbors, and interactions from current A-neighbors can change the boundary
or its licensed output.  Their aggregate rates depend only on the distributed
star/histogram fields.  D34b's Yule proof gives finite global activity on every
bounded time interval, hence also finite projected activity; standard
pure-jump uniqueness supplies the all-future projection.  Monotone A-own and
A-wire counters are in the projected state, so their hitting times inherit
strong Markov.  The receipt now correctly avoids treating one exponential
survival value as the complete A-wire stopping law.

### Finite labeled-truncation diagram — pass

The path masses at depths three and four each sum to one.  Truncating each
labeled four-event path to its committed first three events and only then
forgetting marks reproduces the depth-three pushforward exactly.  No canonical
unmarked restriction map is smuggled in.

### First-applicable verdict priority — pass as a decision machine

The eight Paper-21 outcomes occur in the frozen order.  The six scientific rows
select the expected first true predicate, including the important overlap in
the v9 row where missing inputs beats `FINITE-DOMAIN ONLY`.  The complete-radius
F row is universal over the declared class `{C_r:r finite}`, whereas B4 is
reported only as a sufficient growing upper bound.  The decision logic itself
passes.  Its C/L scientific inputs must be recomputed after the E4 correction,
but the all-future B3 result is not presently contradicted.

## 6. Opening ledger after adversarial probes

| Opening | Delta disposition |
|---|---|
| Projection beyond frozen `N=4` | Survives on all `23,800` depth-five states; both formulas pass on `26,727` cumulative states. |
| Absolute versus elapsed time | Closed by an explicit time-translation gauge and relative-time stopping convention. |
| A-own/A-wire count stops | Closed analytically by the projected nonexplosive CTMC and strong-Markov hitting times. |
| Durable count values in E4 output | **Fails:** exact reachable same-signature/different-next-record witness; declared-label counts are `111,111,111`. |
| Silent `tau` handling | Present recursion is a strong boundary-transition refinement, not yet the canonical observed-C predictive quotient. |
| B1 horizon split | True independently, but absent from the executable gate and absent from the synthetic-count domain. |
| Finite profinite/stem claim | Correctly capped at the labeled-prefix/unmarked pushforward; completed posterior remains open. |
| B2 minimality / bounded replacement for B3 | Still open and still honestly unclaimed. |

## 7. Exact revised ceiling

The delta supports the following statement now:

> For the chosen static D34b law, the scoped histogram boundary and physical
> distributed star retain the fields needed to generate the coarse/role-
> labeled relative-time A-wire law at fixed-time and local count stops.  The
> arbitrary-state row partition, nonexplosion, recursive B3 updater,
> covariance and composition support an all-future growing-carrier
> realization.  B0 and the B1 instantaneous-rate summary fail exactly; full
> ancestry defeats every complete finite actor radius; and the whole component
> is a sufficient, not necessary, ceiling.  The present E4 `29,29,29` values
> are not predictive-class counts for the frozen durable output, and no v9
> posterior or intrinsic timed quantum boundary has been constructed.

**Final count: 0B / 1M / 1m / 0n.**
