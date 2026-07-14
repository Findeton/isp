# D34f round 2 — predictive/profinite closing delta

**Frozen repaired target:** commit
`04ddda89d6be95823c3c430ac6df2278a8bcdcc0`

**Compared against:** frozen round-1 repair protocol at `d6e852f` and original
provisional receipt at `4c24987`.

**Verdict:** **CLOSING DELTA CLEAN — 0 blockers / 0 majors / 0 minors / 0
nits.**

Both predictive/profinite round-1 minors are exactly repaired.  The note now
separates the Branch-F-measurable structural prefix cylinder `U_K` from the
exact first-`q`-component-ring path subevent `S_K`, uses a positive liminf
rather than an ill-formed inequality with an unsigned big-O term, and keeps the
source upper bound at zero or `O(Delta^(q+1))`.  The inverse-limit host is now
explicitly only the discrete event-content skeleton after elapsed-time marks
are forgotten; timed completion, predictive continuity, the gauge quotient and
the v9 bridge remain open.

The additional first-unmatched-attachment witness is exact and correctly
narrow: it demonstrates that a remote extra idle may remain outside the A
ancestry while the extra subtree's attachment birth is forced into it.  The
carrier wording also improves rather than regresses: every deterministic exact
sufficient carrier determines the component quotient, while only a minimal
carrier is a lossless recoding of it.

## 1. Artifact and receipt reproduction

The frozen repaired artifacts have SHA-256:

```text
note
a78311c8fb188813373f2c75141fcd34051e44455f81fd89b94ec713e53d4083

code
0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef

stdout
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2
```

A fresh run under `PYTHONHASHSEED=999983` has stdout SHA-256 exactly

```text
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2.
```

A second fresh run under `PYTHONHASHSEED=424243` exits zero, prints `11/11`,
reproduces the registered attachment witness `1/1`, and preserves internal
digest

```text
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee.
```

The internal digest is unchanged because the mathematical summary fields are
unchanged.  The source/stdout hashes change only because the executable and
narration now carry the repair and attachment regression.  Both
`git diff --check d6e852f..04ddda8` and
`git diff --check 4c24987..04ddda8` are clean.

The repaired delta is confined to the note, code, stdout and ledger.  The
exact numerical engine, reachable levels, `2,927` states, `7,410` emulator
attempts, zero emulators, path coefficients, information family and verdict
remain unchanged.

## 2. Round-1 m1 — observable prefix cylinder closed

The repaired definition is now explicit:

```text
U_K^anchor(Delta)
 = {the initial future A-output prefix has K's exact gauge-invariant structural
    anchored-echo trace, and its final specified A event occurs by Delta}.
```

It places no condition on later A outputs.  This is measurable from Branch F:
the query supplies the ordered future A records, each record's finite typed
ancestry and the elapsed time of the future A event.  Structural equality is a
finite marked-isomorphism cylinder, nominal names are quotiented, intermediate
real times are integrated over, and the last specified output contributes the
Borel inequality `t_final <= Delta`.

The underlying path event is separately defined as

```text
S_K(Delta)
 = {the first q A-component rings are the frozen anchor/broadcast/echo path,
    and the qth ring occurs by Delta}.
```

Branch F need not observe silent component rings for `S_K` to be a probability
subevent.  Running that path necessarily produces the specified initial
A-output prefix, so

```text
S_K(Delta) subset U_K^anchor(Delta).
```

No after-echo silence factor is needed because `U_K` explicitly says nothing
about outputs after the final specified echo.

### 2.1 Exact path probability and liminf

For a target with `n` actors and `q=2n-1`, the anchored path has no births, so
its component ring rate remains `n`.  Therefore

```text
P_K(S_K(Delta))
 = p_echo(K) * ErlangCDF(q,n,Delta)
 = c_K Delta^q + O(Delta^(q+1)),
```

with `c_K>0` equal to the product of the continuous path rates divided by
`q!`.  Since `S_K subset U_K`, the repaired conclusion

```text
liminf_(Delta->0) P_K(U_K^anchor(Delta))/Delta^q >= c_K > 0
```

is exact.

For nonisomorphic `K'`, the all-finite anchored argument still gives either
zero support or at least one catch-up ring in addition to all `q` distinct
anchor-cone nodes.  Starting from a fixed finite source, actor count grows by
at most one per ring, so total rates through a fixed `(q+1)`-ring prefix are
bounded.  Consequently

```text
P_K'(U_K^anchor(Delta)) = 0 or O(Delta^(q+1)).
```

The target liminf and source big-O now compare well-defined probabilities and
imply different conditional Branch-F laws for sufficiently small positive
`Delta`.  No hidden pre/post mark or silent-ring observation has been added to
the query.

## 3. Attachment witness — pass

The new exact witness begins from the seed, lets B birth an extra child and
lets that child idle remotely.  It then runs the seed target path

```text
A idle; A -> B; B -> A.
```

The regression verifies simultaneously that:

```text
remote child idle       is not in final A ancestry;
child attachment birth  is in final A ancestry;
source prefix trace     differs from the seed target trace.
```

This is the right witness for the repaired general wording.  It avoids the
false stronger claim that every record internal to an extra subtree must be
collected.  The first unmatched actor on a birth-tree path has an immutable
attachment birth touching a matched parent; the target echo touches that
parent, so that boundary record contaminates the exact target prefix even when
later records wholly inside the extra subtree remain hidden.

The witness is a finite regression for the first-unmatched-attachment lemma,
not presented as its all-size proof.  The note's rooted-tree argument owns the
general statement.

## 4. Carrier wording — pass

The original phrase “every exact alternative is a lossless recoding” was too
strong because a sufficient carrier may retain irrelevant extra information.
The repaired note now distinguishes three statements correctly:

1. tomographic injectivity makes the minimal Branch-F predictive quotient
   isomorphic to `[K_A]_g`;
2. every deterministic exact sufficient carrier determines that quotient;
3. a nonminimal exact carrier may strictly refine it, while only a minimal
   exact carrier is a lossless recoding of the quotient.

This follows directly from

```text
B(h)=B(h') implies [K_A(h)]_g=[K_A(h')]_g.
```

The component class itself remains sufficient because the D34b future
generator is a function of that current class.  Thus the repaired wording
preserves predictive identity without making a false uniqueness claim about
all implementations.

The output and E11 use the same exact ceiling: “minimal predictive quotient”
for the component gauge class and “every exact carrier determines it, while
nonminimal carriers may refine it.”

## 5. Round-1 m2 — discrete-only inverse tower closed

Every repaired occurrence now confines the immediate finite inverse tower to
the **discrete serialized event-content skeleton after elapsed-time marks are
forgotten**.  At each fixed event depth that grammar has a finite labeled
level, so its ordinary prefix end space is available.

The note also states the necessary negative half:

- full timed prefix levels are uncountable;
- timed completion requires an explicit topology or finite time quotients;
- calling such a timed marked completion profinite requires finite-discrete
  quotients;
- timed predictive continuity, construction-order-gauge bonding maps, v9
  stem-spectrum identification and a finite physical completed-history record
  remain `OPEN`.

The executable ceiling key is correspondingly renamed to

```text
serialized discrete event-content prefix inverse-limit host,
```

and E11 explicitly refuses a timed/gauge-quotient profinite bridge.  No compact
timed mark space or profinite completion is silently inferred.

## 6. Closing ceiling

Both findings from this stream are closed without a new opening.  The accepted
result remains exactly:

> At every legal finite stop of the chosen passive D34b law, exact prediction
> of complete future A-touching ancestry determines A's whole finite connected-
> component history modulo rooted marked gauge.  The component class is
> sufficient, the minimal exact predictive quotient is isomorphic to it, and
> no uniform finite information capacity exists over unbounded growth.

This is a theorem about the chosen model and exact query.  It does not provide
a timed profinite/v9 bridge, a quantum process, spacetime geometry, `G`, or the
interactive click law of nature.

**Final count: 0B / 0M / 0m / 0n.  Predictive/profinite stream closing-delta
clean at the stated ceiling.**
