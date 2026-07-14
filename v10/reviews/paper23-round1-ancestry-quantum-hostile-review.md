# Paper 23 round 1 — ancestry/quantum hostile review

**Terminal source:** D34f at commit
`398077e4b9008c3f203e06ac32ebffebdf817564`.

**Exact paper target:** commit
`540ddf164438335a9ce14e849e43168f9af338b3`.

**Verdict:** **PASS — PAPER 23 FAITHFULLY SYNTHESIZES TERMINAL D34f AT ITS
EXACT CLAIM CEILING.**

**Count:** **0 blocker / 0 major / 0 minor / 0 nit.**

The paper keeps the load-bearing distinction between an observable future-A
prefix and an unobserved exact component-ring path.  It carries the repaired
first-unmatched-attachment argument, states carrier minimality correctly, and
uses “world-component-sized” as a predictive-information statement rather
than as a central-store or global-update claim.  I found no alternative-cut
or extra-branch emulator and no quantum, profinite or spacetime result
promoted beyond terminal D34f.

## 1. Artifact, receipt and review-accounting cross-check

`git diff --check 398077e 540ddf1` is clean.  The candidate paper SHA-256 is:

```text
bfd3ab67ec12e285b3d5011b07a9b7a6453971f59f7ecad02863ea7f2c3a893e
```

The terminal source artifacts currently hash as:

```text
D34f terminal note
fccb527348501ac5c282b0ccc95a32a8a2920bde16b48a25f2eb0baf76c7fcde

exact code
0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef

committed stdout
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2
```

I reran the terminal executable under fresh hash seed `32452843`.  It exited
zero, printed `11/11`, and was byte-identical to the committed stdout.  The
fresh stdout hash was again

```text
de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2,
```

and the internal scientific digest was

```text
ee023eb38cbe5c61acd888128838e210a461eb636a553ed6142132a6bdbc29ee.
```

Paper 23 reproduces the terminal ledger correctly:

```text
gates                                      11/11
reachable levels                          1,6,40,304,2576
cumulative states                         2927
wire incidences                           20148
sorted/reverse sweeps                     2927/2927
anchored echoes                           2927
gauge checks                              351
gauge classes/traces                      351/351
direct continuation attempts             7410
equal-or-lower-order emulators            0
bare coefficients                         1/1152 and 1/576
anchored target/catch-up                  1/192 and 1/1536
attachment witness                        1/1
binary-family sizes                       2,4,8,16,32,64
finite gauge-class counts                 1,6,40,304
```

Its review history is also exact.  The three round-1 counts were respectively
`0/0/2/0`, `0/0/0/0` and `0/0/2/0`; all three closing deltas report
`0/0/0/0`.  The stated 1,096 extra-subtree placements and 17,390 expanded
canonical comparisons appear in the terminal boundary/locality delta, with
zero emulators.  The two-level hidden-internal-record attack and the strict
`S subset U` six-ring witness appear in the terminal ancestry and boundary
deltas.  Commit `398077e` is correctly identified as the terminal D34f
freeze.

## 2. Branch-F future-query typing — pass

Paper 23 defines Branch F as the ordered process of every future event
touching A, with each event's complete typed ancestry and elapsed occurrence
time from the conditioning stop.  Its discriminator is the measurable event

```text
U_K^anchor(Delta)
 = {the initial future A-output prefix has K's canonical structural echo
    trace and its final specified output occurs by Delta}.
```

The paper separately defines `S_K(Delta)` as the event that the first `q`
component rings follow one selected anchor/broadcast/echo path.  Branch F need
not observe those component rings.  The proof uses only

```text
S_K subset U_K;
P_K(S_K) = c_K Delta^q + O(Delta^(q+1));
liminf P_K(U_K)/Delta^q >= c_K > 0.
```

That is the terminal repaired logic.  Intermediate event times, silent remote
rings and nominal labels are integrated or quotiented rather than added to
the query.  The final time inequality is already licensed by Branch F.  The
prefix puts no condition on later A outputs, so it does not conceal an
after-echo survival requirement.

The paper also explicitly records a `q+1` hidden-event realization with the
same observable A-prefix.  This is important: it demonstrates that `U` is
larger than the exact path event instead of quietly treating them as equal.

## 3. Conditioning-cut attacks — no emulator

The fresh anchor is a future A output, not a pre/post label inserted into an
old ancestor.  Every target echo node contains that anchor, so all `q=2n-1`
target nodes must occur after the source's conditioning stop.

I independently reran both cut directions.

### 3.1 Earlier cut

Let the target past contain an old B-idle.  Starting from the earlier seed cut
can reproduce exactly the same anchored Branch-F prefix, but only through:

```text
B idle catch-up; A idle anchor; A -> B; B -> A.
```

The target uses three rings and the earlier source uses four.  The prefixes
are exactly equal, confirming that the paper does not rely on an unobservable
old/new mark.  The catch-up nevertheless remains one ring beyond all three
anchor-cone events, giving the required `q+1` order.

### 3.2 Later cut after two A outputs

I conditioned the seed echo after both the anchor and `A -> B`, then retained
only the final `B -> A` as a future output.  Exact closure gave:

```text
anchor still in final ancestry             True
A -> B still in final ancestry             True
target future A outputs                     3
later-cut future A outputs                  1
complete prefixes equal                     False
```

Ancestry alone cannot locate the cut, but Branch F is the complete ordered
future process.  Events that crossed to the past remain ancestors while
ceasing to be future outputs.  The prefix therefore distinguishes the cut
without a global event counter, a remote timestamp or an internal pre/post
flag.

The paper explains this mechanism accurately and does not revive the rejected
bare-sweep argument.

## 4. First-unmatched-attachment — pass

The paper states the repaired lemma at the correct strength.  It does not say
that every internal record of an extra subtree must reach A.  Instead:

- an extra record on a matched actor persists into that actor's target touch;
- the first unmatched actor along an extra birth-tree branch has an immutable
  attachment birth that touched a matched parent; and
- the target echo touches that parent, forcing the attachment record into the
  A-prefix even when deeper records remain hidden.

Missing target content is the complementary case.  It requires at least one
catch-up event in addition to all `q` distinct anchor-descended target nodes.
Incompatible or rearranged marked histories reduce to a visible extra record,
a missing target record, or both.  Hence a nonisomorphic source has zero
support or needs at least `q+1` rings.

### 4.1 New direct-A attachment attack

I attacked the boundary case where the unmatched branch attaches directly to
A, rather than to a remote matched actor.  Starting from the seed, the source
history was:

```text
A births X; X births Y; Y idles.
```

I then ran only the seed target's three events, ignoring X and Y:

```text
A idle anchor; A -> B; B -> A.
```

The exact result was:

```text
same-three-ring target prefixes equal      False
A-to-X attachment in anchor ancestry       True
X-to-Y birth in final A ancestry           False
Y idle in final A ancestry                 False
```

This is the root edge case of the all-finite lemma.  The extra internal
records remain genuinely hidden, while the attachment birth is inherited by
the very first future anchor because it already sits in A's pre-stop tip.
There is no same-order emulator.

The proof remains law-relative.  Edge deletion, destructive sealing or
history overwrite could defeat its persistence premise, but the paper
explicitly excludes those operations from D34b and makes no theorem for such
laws.

## 5. Predictive carrier minimality — pass

Paper 23 cleanly distinguishes:

```text
the component gauge class is sufficient;
every deterministic exact sufficient carrier determines that class;
the minimal predictive quotient is isomorphic to the class;
only a minimal carrier must be its lossless recoding.
```

This allows both kinds of harmless compression/refinement.  Reconstructible
cached counts, degrees, tips and parities need not be stored twice.  Conversely
a nonminimal carrier may retain an irrelevant bit, nominal serialization or
other extra information.  What is forbidden is merging two component gauge
classes whose Branch-F laws the anchored cylinder separates.

The M-bit theorem supports exactly the stated capacity conclusion.  For every
M it produces `2^M` positive-cylinder, predictively distinct histories at a
common finite-time scope.  It proves no uniform finite worst-case bit bound;
it does not forbid an unbounded integer or other lossless variable-length
serialization.  The paper's wording respects that distinction.

## 6. “World-sized” does not mean a central world ledger

From the connected `A--B` seed, births preserve connectedness and D34b never
deletes edges, so the generated world is one component.  Calling the exact
ancestry boundary “world-component-sized” is therefore legitimate as a
statement about the minimal predictive equivalence class.

The paper immediately supplies the necessary negative interpretation:

- it does not say one record physically stores the entire component;
- the component history may remain distributed over record wires;
- it does not require a simulator to scan all records before each click; and
- independent local actor rings remain the execution rule.

There is no contradiction between local generation and a global-sized exact
predictive state.  Local updates can preserve remote information whose
unlimited-horizon return remains possible.  The theorem characterizes which
past distinctions the complete future law remembers; it does not introduce a
central CPU, global commit order or proper-time clock.

The paper also avoids an asymptotic-size overclaim.  “Component-sized” means
isomorphic to the full rooted marked component class up to lossless coding,
while the explicit quantitative consequence is only the proved unbounded
M-bit worst-case lower bound.

## 7. Profinite, quantum and spacetime refusals — clean

The immediate inverse tower is restricted to the discrete serialized
event-content skeleton after real elapsed times are forgotten.  Paper 23
correctly leaves open:

- a topology or finite time quotients for full timed prefixes;
- construction-order-gauge bonding maps;
- identification with the v9 unmarked stem spectrum;
- predictive continuity on a completion; and
- a finite physical record carrying a completed infinite-history point.

The phrase “profinite-adjacent host” is appropriately weaker than a completed
timed profinite identification.  Profinite organization is not used to shrink
the finite-stop predictive quotient or select the law.

The quantum ceiling is equally explicit.  D34f constructs no controlled
quantum process, intrinsic operation law, quantum carrier width,
process-tensor Markov order or actor-to-D34c quantum lift.  The proposed
controlled quantum lift is listed as an open investigation, not as a result.

No causal speed, Lorentz cone, dimension, proper-time ruler, metres, seconds
or value of `G` is inferred.  The anchor broadcast is a positive-probability
sequence on the chosen actor graph, not a spacetime signal path.  The paper
correctly requires any future surviving click law to rerun the v9 cone, scale
and dimension diagnostics.

## 8. Conclusions and open problems — proportionate

The closed list is confined to the passive D34b law, finite legal stops and
the exact unlimited-horizon complete-ancestry query.  Within that scope the
paper is entitled to stop searching for a proper exact quotient: tomography
makes the full component gauge class the minimal predictive quotient.

The proposed ways to obtain a smaller operational boundary—finite horizons,
coarser observations, approximation, attenuation, sealing, causal horizons
or a different grammar—change a theorem input rather than pretending to
evade it.  The further open branches on timed completions, controlled quantum
generation, law selection and geometry are all explicitly conditional.  The
paper never upgrades D34b from chosen exemplar to nature's rulebook.

One wording limit remains load-bearing and is preserved throughout: the
result applies to **deterministic exact sufficient carriers**.  No claim is
made about approximate, finite-error or intervention-dependent quantum
carriers.

## 9. Final disposition

| Audit target | Disposition |
|---|---|
| Paper/terminal delta | clean |
| Exact hashes and `11/11` receipt | reproduced |
| Review counts and added-attack ledgers | exact |
| Branch-F observable prefix | correctly typed |
| Hidden pre/post mark | absent |
| Earlier cut | same trace only at `q+1` |
| Later cut | loses prior A events as future outputs |
| First-unmatched attachment | all-finite argument retained |
| Direct-A extra branch | attachment immediately visible |
| Minimal versus nonminimal carriers | correct |
| “World-sized” interpretation | information state, not central store |
| Timed/profinite/v9 bridge | explicitly open |
| Quantum lift | explicitly open |
| Spacetime, units and `G` | explicitly absent |
| Law selection | explicitly open |

**Final count:** **0B / 0M / 0m / 0n.**

**Recommendation:** accept Paper 23 at the candidate's current theorem
ceiling.  No paper repair is required by this hostile stream.  The result is
an exact predictive-state theorem for the chosen passive law, not a central
universe ledger, quantum history law, profinite completion or spacetime
derivation.
