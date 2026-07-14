# D34f round 2 — boundary/locality closing delta

**Frozen repaired target:** commit
`04ddda89d6be95823c3c430ac6df2278a8bcdcc0`.

**Compared against:** the frozen round-1 repair protocol at `d6e852f` and the
original provisional target at `4c24987`.

**Exact delta target:** attack the new first-unmatched-attachment lemma, extra
actors and remote subtrees, Branch-F prefix-cylinder measurability, the
component/local clock ceiling and the executable attachment witness; then
check that no accepted persistence, reconstruction, returnability, gauge,
tomography or information result regressed.

**Exact verdict:** **CLOSING DELTA CLEAN — THE REPAIR CLOSES THE EXTRA-SUBTREE
AND OBSERVABLE-CYLINDER OPENINGS WITHOUT REGRESSION.**

**Count:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

## 1. Frozen artifact reproduction

The repaired artifacts have SHA-256:

```text
note
a78311c8fb188813373f2c75141fcd34051e44455f81fd89b94ec713e53d4083

source
0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef

committed stdout
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2
```

I reran the executable under fresh `PYTHONHASHSEED=6700417`. It exited zero,
printed `11/11 PASS`, reproduced attachment witness `1/1`, and byte-matched
the committed stdout:

```text
fresh stdout SHA-256
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2

internal receipt digest
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee
```

Both `git diff --check d6e852f..04ddda8` and the current worktree diff check
are clean. The source and stdout hashes changed because the repair adds the
attachment witness and corrects the E8/E11 narration. The mathematical
summary digest is unchanged because its ledger fields are unchanged.

The exact engine still reports:

```text
gates                                      11/11
reachable labeled levels                  1, 6, 40, 304, 2576
cumulative states                         2927
wire incidences                           20148
sorted/reverse sweeps                     2927 / 2927
anchored echoes                           2927
gauge checks                              351
gauge classes/traces                      351 / 351
direct continuation checks                7410
equal-or-lower-order emulators            0
binary family                             2, 4, 8, 16, 32, 64
verdict                                   COMPONENT PREDICTIVE-IDENTITY /
                                          UNBOUNDED
```

## 2. First-unmatched-attachment lemma

The round-1 overstatement was that every internal record of an extra subtree
must be collected by K's target echo. That is false: after a remote branch has
returned inward, a later event wholly inside it can remain outside the final A
ancestry. The repaired lemma needs only the boundary of the extra subtree.

Take a target component K and a nonisomorphic source K'. Match their largest
common rooted marked actor/event structure. If K' contains an unmatched
subtree, follow its birth-tree path toward A and choose the first unmatched
actor. Its parent is matched. The actor's immutable attachment birth touched
that matched parent before the stop.

K's anchored target path touches every matched actor:

- A is touched by the anchor;
- every non-root actor is touched during outward broadcast and inward echo;
- every internal parent is touched by its target child interactions and, if
  non-root, by its own parent interactions.

Wire persistence therefore places the attachment birth in the matched
parent's next target event and ultimately in the specified Branch-F prefix.
K's target trace has no such actor/attachment record. A proper extra subtree
thus has zero support for the exact target prefix even if every later record
wholly inside that subtree remains hidden.

This argument also covers the edge cases:

- if the extra actor attaches directly to A, the fresh A anchor immediately
  inherits the attachment from A's old tip;
- if the matched parent is a target leaf, its inward interaction carries the
  attachment toward A;
- if the source has both an extra branch and a missing target record, the
  visible attachment cannot manufacture the missing record with its required
  kind, parentage, initiator ordinal and predecessors; the missing record
  still requires a catch-up ring;
- if an apparent extra actor can be relabeled into the target marked tree,
  then it was not unmatched under the rooted marked gauge in the first place.

The all-size result is an induction on the first divergent rooted-tree edge,
not an extrapolation from one finite example.

## 3. Independent extra-subtree attack

I nevertheless expanded the executable's one seed witness over every actor of
every state in the registered levels zero through three. For each target and
each actor I:

1. added an unmatched leaf at that actor;
2. appended one idle wholly on the new leaf;
3. ran K's exact anchored path while deliberately ignoring the extra edge;
4. inspected the final A ancestry and canonical Branch-F prefix.

The exact ledger was:

```text
target/attachment placements              1096
missing attachment births at A            0
remote internal idles incorrectly at A    0
target-prefix emulators                    0
```

Thus all 1,096 cases exhibit the intended sharp behavior: the first attachment
is visible, the later internal idle is not, and the source cannot reproduce
the target prefix. This directly attacks extra leaves at A, at internal
vertices and at target leaves, across nonuniform degrees and event histories.

The committed smaller witness is also correct. Starting from the seed, B
births an extra child, that child idles, and the source then executes the seed
target path

```text
A idle; A -> B; B -> A.
```

The child's idle is absent from the final A ancestry, its attachment birth is
present, and the canonical prefix differs from the seed target. E9 now gates
all three facts before printing `attachment witness=1/1`.

## 4. Prefix cylinder versus exact path subevent

The repaired observable is now well typed:

```text
U_K(Delta)
 = {the initial future A-output prefix has K's canonical structural anchored
    echo trace, and its final specified A output occurs by Delta}.
```

Branch F supplies exactly the required fields: the ordered future events that
touch A, their finite typed transitive ancestries and each A event's elapsed
time. Structural prefix equality is a finite marked-isomorphism condition;
the final time condition is the Borel event `t_final <= Delta`. Earlier real
times and silent off-A events are integrated out. No pre/post label, global
event count or remote timestamp has been added to the query.

The exact path event

```text
S_K(Delta)
 = {the first q component rings are the frozen anchor/broadcast/echo path and
    ring q occurs by Delta}
```

is an underlying probability subevent. It need not itself be observable by
Branch F. Every S path emits the specified initial A prefix, so
`S_K(Delta) subset U_K(Delta)`.

I constructed an exact witness that this inclusion is genuinely strict. Let
B have a child C before the stop. The prescribed target echo uses five rings:

```text
A idle; A -> B; B -> C; C -> B; B -> A.
```

After `C -> B`, insert a C-idle and only then execute `B -> A`. The new idle
is after C's return and never reaches A. The six-ring path has exactly the
same initial Branch-F A-output prefix as the five-ring target path:

```text
target path rings                         5
hidden-event path rings                   6
canonical A prefixes equal                true
hidden C idle in final A ancestry         false
```

This is precisely why U must not be equated with S. It also confirms the
small-time accounting: the target path contributes at order `Delta^q`, while
this hidden-event enlargement contributes no earlier than
`Delta^(q+1)`.

## 5. Small-time upper bound after the repair

Every exact target prefix contains the `q=2|K|-1` distinct anchored event
records in its visible ancestries. They must all occur after the conditioning
stop because each contains the newly created anchor.

For a nonisomorphic source K':

- an extra/incompatible record on a matched wire or the first attachment of
  an extra subtree contaminates the target prefix, giving zero support; or
- a missing target record, actor or edge requires a non-target catch-up ring
  in addition to all q anchored records.

Silent component events allowed by U cannot lower that ring count; they only
increase it. Starting from any fixed finite K', the actor population increases
by at most one per ring, so the total rate is bounded over every fixed
`q+1`-ring prefix. Standard finite-prefix CTMC counting then gives

```text
P_K'(U_K(Delta)) = 0 or O(Delta^(q+1)).
```

For K, the chosen birth-free echo retains component rate n and has exact
positive subevent probability

```text
P_K(S_K(Delta))
 = p_echo(K) ErlangCDF(q,n,Delta)
 = c_K Delta^q + O(Delta^(q+1)),  c_K>0.
```

Therefore the repaired positive-liminf statement for U is valid and avoids
the old unsigned-big-O inequality.

## 6. Component locality and clock ceiling

The repair does not introduce a universal commit order. The primitive D34b
model still assigns an independent rate-one process to each actor. For a
fixed finite A component with n actors, the superposed component process has
rate n. This is a convenient conditional calculation, not a new record-owned
clock and not relativistic proper time.

For the exact echo path there are no births, so n remains constant and the
Erlang formula is exact. A source catch-up path may contain births and hence
varying rates, but only positivity and the event-count exponent are used for
the upper bound.

I repeated the disconnected-factor control. Adding an unrelated P--Q
component leaves A's continuous idle rate at `1/2`. Only an artificial global
embedded race changes:

```text
A continuous rate, alone/with P--Q        1/2 / 1/2
global-depth share, alone/with P--Q       1/4 / 1/8
```

The theorem uses the former and explicitly rejects the latter as a regional
physical clock. Fixed construction time remains a mathematical conditioning
scope; A-own-ring and A-wire-event hitting times are record-local stopping
scopes inherited from D34b's strong-Markov/nonexplosion result. Elapsed future
time has an arbitrary origin but is part of Branch F. None of these claims
identifies an actor counter with proper time or supplies Lorentz geometry.

## 7. Regression against round 1

I reran the complete independent round-1 boundary battery against `04ddda8`.
It remains `8/8 PASS`:

```text
10-actor / 23-old-event reconstruction          PASS
sorted and reversed branched collection         PASS / PASS
branched anchor broadcast/echo                   PASS
10 interleaved extra-event collection           PASS
fresh six-actor nominal gauge/transport          PASS
depth-one emulator comparisons                   17390, zero emulators
disconnected continuous factorization            PASS
```

The note preserves the earlier claim ceilings and improves two of them:

- every exact sufficient carrier determines the component quotient, but only
  a minimal carrier must be a lossless recoding of it;
- only the discrete event-content prefix skeleton has the immediate finite
  inverse tower; timed completion, gauge bonding maps, predictive continuity
  and the v9 identification remain open.

Nothing in the delta derives the D34b law, changes its coefficients, adds
component joining or sealing, installs causal speed, defines quantum
operations, makes a cone/dimension claim or fixes `G`.

## 8. Closing disposition

The round-1 openings assigned to this stream are closed:

```text
first-unmatched-attachment failure          0
extra-actor/subtree target emulators        0
prefix-cylinder measurability failure       0
silent-path small-time-order failure        0
component-factorization regression          0
global-clock or proper-time promotion       0
prior theorem regression                    0
```

The surviving result remains:

> At every legal finite stop of the chosen passive D34b law, the exact
> complete Branch-F future law determines A's whole finite connected-component
> history modulo rooted marked gauge. That component class is sufficient, the
> minimal predictive quotient is isomorphic to it, and the exact information
> requirement has no uniform finite bound over unbounded growth.

This is a model theorem at an exact full-ancestry query, not the interactive
click law of nature.

**Final count:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

**Final verdict:** **CLOSING DELTA CLEAN — COMPONENT PREDICTIVE-IDENTITY /
UNBOUNDED SURVIVES THE REPAIRED BOUNDARY/LOCALITY REVIEW.**
