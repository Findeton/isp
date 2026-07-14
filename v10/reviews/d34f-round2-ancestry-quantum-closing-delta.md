# D34f round 2 — ancestry/quantum closing delta

**Frozen protocol:** commit
`d6e852f0963a397f6a7350874e065b86d3afb7f6`.

**Original reviewed target:** commit
`4c2498772d48273548420c5e483d519976344f91`.

**Exact repaired target:** commit
`04ddda89d6be95823c3c430ac6df2278a8bcdcc0`.

**Verdict:** **PASS — ALL TWO ANCESTRY/CARRIER REPAIRS CLOSE, AND THE
PROTOCOL'S PREFIX/PROFINITE REPAIRS REMAIN CONSISTENT.**

**Count:** **0 blocker / 0 major / 0 minor / 0 nit.**

The repaired all-finite argument now uses the unavoidable attachment birth,
not the false claim that every record internal to an extra branch must itself
reach A.  The predictive-state conclusion is also at the right categorical
strength: every exact sufficient carrier determines the component quotient,
only a minimal exact carrier is a lossless recoding of it, and a nonminimal
carrier may refine it.  I found no new equal-or-lower-order emulator, hidden
cut mark, quantum promotion or geometry/profinite overclaim.

## 1. Exact delta and independent reproduction

`git diff --check d6e852f 04ddda8` is clean.  The repaired artifacts hash as:

```text
note
a78311c8fb188813373f2c75141fcd34051e44455f81fd89b94ec713e53d4083

code
0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef

committed stdout
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2
```

I reran the exact program under fresh hash seed `1618033`.  It exited zero,
printed `11/11`, and was byte-identical to the committed stdout.  Its stdout
SHA-256 was again

```text
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2,
```

with internal scientific digest

```text
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee.
```

The reproduced exact ledger remains:

```text
reachable labeled levels                 1,6,40,304,2576
cumulative states                        2927
wire incidences                          20148
sorted/reverse sweeps                     2927/2927
anchored echoes                           2927
gauge classes/traces                     351/351
direct continuation comparisons          7410
equal-or-lower-order emulators            0
bare equal-order coefficients             1/1152 versus 1/576
anchored q/q+1 coefficients               1/192 versus 1/1536
attachment witness                        1/1
binary-family sizes                       2,4,8,16,32,64
finite gauge-class counts                 1,6,40,304
```

All discrete masses and leading coefficients used by the verdict are
`Fraction` exact.  The exponential/Erlang rows remain evaluations of explicit
analytic formulas at 110-decimal working precision.  The scientific ledger
and digest did not change; the source/stdout hash changes are explained by the
new regression and corrected narration.

## 2. First-unmatched-attachment proof — closed

Round 1 found the sharp counterpressure: if `K'` extends target `K` by a
remote branch, records created wholly inside that branch need not enter the A
ancestry when one runs only K's target echo.  It was therefore insufficient
to say that every extra remote record is collected.

The repaired proof now makes the necessary finite-tree cut.  Match a maximal
common rooted actor/event substructure of K and K'.  Then:

1. an extra record on a matched actor persists into that actor's target touch;
2. if there is an extra actor, choose the first unmatched actor along its
   birth-tree path from the matched root.  Its birth touched a matched parent,
   and that immutable attachment record persists when the target echo later
   touches the parent; and
3. an incompatible altered record on a matched wire is immutable and is
   likewise exposed.

Those cases have zero support for K's exact structural prefix.  If instead K'
is missing target content, it must create at least one non-anchor-cone event
in addition to the `q=2n-1` distinct target events containing the new anchor.
It therefore needs at least `q+1` post-stop rings.  Rearranged parentage or an
incomparable marked DAG reduces to an extra/incompatible source record plus a
missing target record; it cannot evade the same dichotomy.

### 2.1 New deep-branch attack

I tested a larger case not in the committed regression.  The target was a
four-actor chain and therefore had a seven-event anchored echo.  The source
properly extended the target by:

```text
matched leaf D births X; X births Y; Y idles; X idles.
```

I then ran only the target's seven anchor/broadcast/echo operations, never
touching X or Y after the attachment.  Exact DAG closure gave:

```text
same-seven-ring Branch-F traces equal       False
D-to-X attachment birth visible at A        True
X-to-Y birth visible at A                    False
Y idle visible at A                          False
X idle visible at A                          False
```

This is the hostile configuration the lemma must own: multiple internal extra
records genuinely remain hidden, yet the first attachment witness is forced.
The repaired prose says exactly this, and the executable's smaller
`attachment witness=1/1` case is an appropriate regression rather than being
misrepresented as the all-finite proof.

I found no grammar operation that can erase the attachment, detach its child,
or rewrite the matched parent's tip.  Such operations would invalidate the
lemma in a different law, but none exists in the frozen D34b law.

## 3. Observable future prefix and conditioning cuts — closed

The repaired `U^anchor_K(Delta)` is defined solely by Branch F:

- the **initial future A-output prefix** has K's canonical structural echo
  trace; and
- the final specified A output occurs by elapsed time `Delta`.

It imposes no condition on later outputs.  The exact event `S_K(Delta)` that
the first `q` component rings follow one chosen path is now explicitly only a
probability subevent.  Consequently the valid statement is

```text
S_K subset U_K;
P_K(S_K) = c_K Delta^q + O(Delta^(q+1));
liminf P_K(U_K)/Delta^q >= c_K > 0.
```

No silent component ring or pre/post bit on an old ancestor is consumed by
the observable cylinder.

I verified that the distinction is substantive, not verbal.  On a
three-actor chain the prescribed anchored path has five component rings.  I
inserted a sixth, non-A idle on the leaf immediately after its last inward
transfer.  That idle was absent from the final A ancestry, and the resulting
Branch-F initial A-output prefix was exactly the same as the five-ring target:

```text
target path rings                           5
interleaved realization rings               6
observable initial prefixes equal           True
hidden idle absent from final A ancestry     True
```

Thus `S_K` is a proper subevent of `U_K`, just as the repair now requires.
The extra realization begins one small-time order later and cannot cancel the
positive `Delta^q` liminf supplied by `S_K`.

The shifted-cut attacks also remain closed:

- from an earlier cut, a missing old B-idle can reproduce the target trace
  only by one catch-up ring followed by all anchor-cone rings (`q+1` total);
- from a cut immediately after the anchor, the anchor remains in the final
  ancestry but is no longer itself a future A output.  On the seed echo the
  target has three future A outputs and the later-cut history has two, so their
  complete prefixes are unequal.

The discriminator therefore uses future sequence membership and elapsed
future time already present in Branch F, not a hidden global construction
cut.

## 4. Minimal versus nonminimal carriers — closed

The repaired statement now separates three claims:

```text
every exact sufficient carrier determines [K_A]_g;
the minimal predictive quotient is isomorphic to [K_A]_g;
only minimal exact carriers are lossless recodings of that quotient.
```

This survives the obvious refinement counterexample.  For example, a carrier
may retain `[K_A]_g` together with an irrelevant auxiliary bit or a nominal
serialization choice.  It remains sufficient but is not bijective to the
minimal quotient.  The current note explicitly permits this.  Conversely, if
a purported sufficient carrier merged two different component gauge classes,
the anchored prefix separating those classes would give different Branch-F
laws, contradicting sufficiency.  Therefore the weaker universal
“determines” claim and the stronger minimal-state isomorphism both follow.

The unbounded-information result is unaffected.  A refinement cannot reduce
the number of distinguishable carrier states required on the `2^M` family,
while lossless removal of cached/reconstructible fields is still allowed.

## 5. Timed, profinite, quantum and geometry ceilings — clean

The repaired note no longer calls the full timed Branch-F completion
profinite.  It states only that, after elapsed times are forgotten, the
locally finite discrete serialized event-content prefix tree has finite
levels and an ordinary inverse-limit end space.  It separately records that:

- timed prefix levels are uncountable and need an explicit topology or finite
  time quotients;
- construction-order-gauge bonding maps are not constructed;
- identification with the v9 unmarked stem spectrum is open;
- predictive continuity on a completion is open; and
- no one finite physical record is shown to carry a completed inverse-limit
  point.

Those are the correct ceilings.  Finite-level compatibility does not by
itself supply the timed or v9 bridge.

The ancestry theorem also remains classical and chosen-law-relative.  It
does not construct a quantum operation, intrinsic quantum boundary, Born
weight or quantum history law.  Nor does it infer proper time, a causal cone,
spacetime dimension, metric scale or `G`.  The only timing used in the
discriminator is the declared elapsed time of a future A output under the
chosen Poisson law.  I found no quantum, geometry or law-of-nature statement
smuggled into the repaired verdict.

## 6. Closing disposition

| Audit target | Disposition |
|---|---|
| Fresh exact execution | `11/11`, byte-identical, hashes exact |
| Observable A-prefix / exact path separation | closed |
| Hidden silent-ring requirement | absent |
| Hidden pre/post ancestry mark | absent |
| Earlier/later conditioning-cut attacks | closed |
| First-unmatched-attachment lemma | closed at all finite sizes |
| Deep extra branch with hidden internal records | attachment still exposes it |
| Missing/incompatible source history | zero support or at least `q+1` rings |
| Minimal predictive quotient | correctly isomorphic to component class |
| Nonminimal sufficient refinements | correctly allowed |
| Timed/profinite/v9 bridge | explicitly open |
| Quantum/geometry/G consequences | explicitly absent |

**Final count:** **0B / 0M / 0m / 0n.**

**Recommendation:** close this hostile stream and retain
`COMPONENT PREDICTIVE-IDENTITY / UNBOUNDED` at D34f's exact ceiling.  The
result is a theorem about complete durable ancestry under the selected passive
D34b law.  It does not select that law for nature or solve the later
quantum/profinite/spacetime bridges.
