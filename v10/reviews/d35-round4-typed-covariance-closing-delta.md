# D35 round 4 — typed-covariance closing delta

**Frozen target:** commit
`d414c56de480fd692630c1d7b3b10ada44cb60f7`.

**Lane:** typed freshness, actor/event alpha covariance, exact projectivity,
multi-call continuation and completed-history extension.

**Verdict:** **PASS — THE TYPED IDENTITY REPAIR CLOSES THE ROUND-3
FRESHNESS MAJOR AND PRESERVES THE ROW-2 COMPLETION THEOREM.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

## 1. Fresh reproduction

I reran `d35d_typed_identity_terminal_exact.py` under fresh independent hash
seeds `244948974` and `264575131`.  Both processes exited zero and were
byte-identical to each other and to the committed receipt.

Exact identities reproduce as:

```text
source
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

stdout
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574

internal science
79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c
```

The executable again prints `PASS 18/18`.

## 2. Typed domains — pass

The repair uses distinct value domains rather than printable prefixes:

```text
actor-supplied
actor-generated
event-supplied
event-generated
actor-control
event-control
```

Generated actor and event identities contain component namespace, root causal
ordinal and call path.  Their dataclass domain tags make them unequal to every
supplied display string, even when the strings print like a future generated
identity.  Actor-generated and event-generated values are also mutually
distinct despite sharing coordinates.

Independent inspection of the first generated laws found exactly:

```text
initial actor domains       actor-supplied
initial event domains       event-supplied
grown actor domains         actor-supplied, actor-generated
grown event domains         event-supplied, event-generated
```

No raw display text is used as generated storage identity.

## 3. Independent collision and projectivity probes — pass

I independently accumulated the complete first-cylinder marginal from the
primitive second-call branches; I did not use the executable's summary gate.
For both Q1 and Q2:

```text
unrenamed law                    16 / 408 / 408
ordinary actor/event alpha       16 / 408 / 408
call-one display collision       16 / 408 / 408
full marginal mismatches          0
old-root persistence failures     0
```

Here the three numbers are complete first atoms, second refinements and
persistence checks.

The call-one adversary renames seed display `A0` to
`EROOT-CAP-0::T1:r`.  It no longer collides with the typed generated event.
The complete first and second laws remain normalized and projective.

The delayed adversary renames `A0` to `EROOT-CAP-0::T5:r`.  Six consecutive
calls complete in each Q cell, with root ordinal six; the former sixth-call
failure is gone.

The actor adversary renames D's display to `NROOT-CAP-0::T0:r`.  All 16 first
branches remain present with exact total mass one, including the root-birth
branch.  The supplied actor value cannot collide with a generated newborn.

## 4. Multi-call continuation and completion — pass

Independent eight-call runs under FIFO, LIFO and canonical mailbox service
produce identical complete physical keys in Q1 and Q2, with root-owned ordinal
eight.  All 16 first states also have normalized second-call kernels.

The Ionescu--Tulcea assumptions therefore remain intact:

1. every reachable finite rooted state has a finite normalized next-call
   kernel;
2. strict child descent makes each call finite;
3. the typed finite-state union is countable; and
4. generated identities remain fresh at every finite ordinal/path.

The late-collision probe is important here: it confirms that alpha-equivalent
display choices cannot make a future kernel disappear at a selected ordinal.
The completed rooted-call measure and persistent event-DAG pushforward now
descend to the declared typed alpha quotient.

The root ordinal remains causal record succession, not duration, a rate,
metric proper time or a global opportunity counter.

## 5. Scope and disposition

The accepted result remains:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

Typed covariance does not select Q or g, remove the supplied root, solve
overlapping peer diamonds, construct the v9 spectrum bridge, recover spacetime
or identify nature's law.  Those ceilings remain explicit.

Both diff-hygiene ranges are clean:

```text
git diff --check 8a9bb98..d414c56
git diff --check de51b4e..d414c56
```

## 6. Final tally

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final recommendation:** accept the typed covariance close.  No further
probability, projectivity, freshness or completion repair is requested in
this lane.
