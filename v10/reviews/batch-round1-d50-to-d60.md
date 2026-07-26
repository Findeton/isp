# BATCH ROUND 1 — INDEPENDENT HOSTILE REVIEW OF SEVEN GREEN-UNREVIEWED UNITS

**Frozen:** 2026-07-26.
**Units under review:** D50 (#421/#422), D51 (#423/#424), D53 (#426),
D55c (#434/#435), D57 (#434/#436), D58 (#438/#439), D60 (#447/#448).
**Reviewers:** three independent Opus 5 workers, no prior context,
recompute-not-trust; findings pooled here by the lead. Every number below
was produced by code written for this review and run against the committed
layers from the repo root. Scratch under
`/private/tmp/claude-501/.../scratchpad/` (`rev/`, `d51rev/`, `d53rev/`).
Calibration: `reviews/d54-round1-hostile-review.md` and
`reviews/d55-round1-hostile-review.md`.

---

## GLOBAL VERDICT

| unit | verdict |
|---|---|
| **D50** — "the form is a choice" | **REVISE. 1 BLOCKER / 1 MAJOR / 5 MINOR / 2 NIT.** |
| **D51** — the H1 reduction | **REVISE. 2 BLOCKER / 3 MAJOR / 8 MINOR / 2 NIT.** |
| **D53** — the empty-trace capacity correction | **REVISE. 1 BLOCKER / 2 MAJOR / 3 MINOR / 2 NIT.** |
| **D55c** — the M^{3+1} control | **REVISE. 1 BLOCKER / 2 MAJOR / 4 MINOR / 2 NIT.** |
| **D57** — the sector-exact closure | **REVISE. 1 BLOCKER / 1 MAJOR / 6 MINOR / 2 NIT.** |
| **D58** — the atlas instrument | **REVISE. 1 BLOCKER / 2 MAJOR / 5 MINOR / 3 NIT.** |
| **D60** — the crystal | **REVISE. 0 BLOCKER / 3 MAJOR / 5 MINOR / 3 NIT.** |

**Every constructed object in the batch survived.** The brick record, the
M^{3+1} census, the refinement fixpoint, the 209-key projection sweep, the
D53 audit table, the completion sweep — all reproduce exactly under code
that shares nothing with the receipts. Nothing in this batch is a
construction failure.

**The pattern of the two prior rounds holds, with one break.** Five of the
seven BLOCKERs are again interpretation sentences: D51's inverted
`sigma`-implication and its false mechanism, D53's false necessity claim,
D55c's density-scoped null sold as a universal, D57's refuted mechanism for
the alphabet. **Two are not** — and this is the batch's news:

* **D58's M^{3+1} control is not a sprinkling.** `latt4` draws `s % box`
  from an LCG mod `2^31`; with `box = 32` (a power of two) the committed
  control is **32 distinct points wearing 120 labels**, 8 spatial values
  per axis. Its flagged "finding candidate" reverses sign against genuine
  sprinklings.
* **D50's principal measurement is arithmetically wrong.** Its I2/I3/I5
  constraint rows are not the differential of the demand — half the product
  rule is missing. Correct completion dimensions are **12 / 32 / 125**, not
  10 / 28 / 107; the ported D49 figure **119 becomes 137**. The conclusion
  is unchanged and in fact strengthened, but the published exact numbers
  are not the numbers.

**Three defects propagate across unit boundaries** and must be repaired
together, not unit by unit:

1. `latt4`'s power-of-two degeneracy hits **D55c** (one of four records,
   6.3% of the capable census — not load-bearing), **D58** (load-bearing:
   it *is* the M^{3+1} control) and **D60** (its cited comparators).
2. **D53's** false "SKY-A/C can never shatter" told the programme to test
   only SKY-B under SC5; **D55c** obeyed, and missed the reading under
   which the discriminator fires.
3. **D50's** linearization error is inherited from **D49** — SF0(b)'s port
   check certifies the error rather than catching it, and 119 is quoted
   corpus-wide.

**Three positive reversals** the round supplies: D55c's pre-registered
discriminator, disowned on sparse evidence, in fact **succeeds** at higher
density; D50's negative is **constructively rigorous** (an exact line of
strictly-positive non-proportional completions, not merely a tangent
count); D58's flagged overlap finding candidate is **resolved — negatively
— by a matched comparison the unit called a residue**.

---
---

# D50 — "the form is a choice"

**VERDICT: REVISE. 1 BLOCKER / 1 MAJOR / 5 MINOR / 2 NIT.**

Files: `note-d50-is-the-form-a-law-pin.md`,
`note-d50-form-law-or-choice-result.md`,
`code/d50_form_law_or_choice_exact.py` + `data/…out`, LOG #421/#422.

The AST surgery is sound, the sweep runs, the trend is real, and the
unit's headline — **depth-stationarity does not force the form; the form
is a choice; B2's restriction is permanent** — survives everything and is
*stronger* than the unit claims. What does not survive is the arithmetic
of the quantity the headline is stated in.

## BLOCKER 1 — the I2/I3/I5 constraint rows are not the demand's differential; 10/28/107 and the ported 119 are wrong

**Where.** `demand_rows(...)`, the `'bis'` / `'stat'` branch (lines
197–219); every number it produces: SF0(b)'s port check (`bisimulation
free = 119`), SF3's headline (`I3 completion dims = [10, 28, 107]`), SF4,
SF2, SF5, the VERDICT block, LOG #422 ("dimension **10, 28, 107**"), and
the result note.

**The defect.** The demand is *"the completed class-to-class transfer is a
function of the class"*: with `A_c(b) = Σ_{e:cls=c} q·Z(h0+e)`,
`B_c(b) = Σ q·Z(h1+e)`, the condition is

```
    F_c(b)  =  A_c(b)·Z_{h1}(b)  −  B_c(b)·Z_{h0}(b)  =  0
```

— **quadratic** in `b`, since `A_c, B_c, Z_{h0}, Z_{h1}` are all linear.
Its differential at `b*` needs the product rule in full:

```
 dF_c[v] = A_c(v)·Z_{h1}(b*) + A_c(b*)·Z_{h1}(v)
         − B_c(v)·Z_{h0}(b*) − B_c(b*)·Z_{h0}(v)
```

The receipt computes only the first and third terms
(`row.append(A_ * Zs[h1] - B_ * Zs[h0])`). The omitted pair is
`A_c(b*)·BAS_j[h1] − B_c(b*)·BAS_j[h0]`, which is generically nonzero
because a boundary perturbation moves `Z` at interior nodes too.

**This is not a convention: the same file gets it right elsewhere.** The
`'ren'` branch (I1) computes the *full* product rule
(`A_*za[j] + C_*zh[j] - B_*zb[j] - D_*zr[j]`). One demand is linearized
correctly and the other is not, in the same function.

**My recomputation** (`/private/tmp/.../rev/d50lin.py`; D49's state
imported the same way — it is the only source of the layer — but every
rank and every row is mine). The decisive test is exact in `t`: `F_c` is
quadratic, so `(F(1) − F(−1))/2` **is** `dF/dt|₀` exactly, over Fractions,
with no numerics:

```
[EXACT-IN-t TEST at D = 2, random rational direction v]
  rows tested = 16;  b* OFF the demand variety (residual != 0) in 0
  d50's row . v  == dF/dt|0  in   0/16
  FULL  row . v  == dF/dt|0  in  16/16

[I1 'ren' rows, same test at D = 4]
  rows = 6   b* off-variety = 0   rows matching dF/dt = 6/6      <- correct
```

`b*` sits exactly on the demand variety (residual 0 everywhere), so the
tangent-space framing is legitimate; only the tangent is miscomputed.

**The corrected table** (my rank, my rows, exact Fractions):

```
 D   NB rankM | kind   d50rank d50free d50comp |  FULLrank FULLfree FULLcomp
 2   23   22  | bis        10      13      12  |       9       14       13
 2   23   22  | stat       12      11      10  |      10       13       12
 3   84   83  | bis        49      35      34  |      46       38       37
 3   84   83  | stat       55      29      28  |      51       33       32
 4  313  312  | bis       194     119     118  |     176      137      136
 4  313  312  | stat      205     108     107  |     187      126      125
```

So: **I3 completion dimension is 12 / 32 / 125, not 10 / 28 / 107.**
**I2 boundary-free at depth 4 is 137, not 119** — and 119 is D49/B2's
published figure, quoted throughout the corpus. SF0(b) is advertised as
the anchor that would catch exactly this ("a disagreement here would be
anchor breakage"); because D50 reproduces D49's *method*, the port check
certifies the error instead of catching it. The whole point of a port
check is defeated by porting the bug with the state.

**Damage: the conclusion strengthens.** The corrected dimensions are
*larger*, still monotone, still ≫ 0, so I3 does not force the form — more
freely than reported. And SF4 survives verbatim under correction:

```
[I5 = I3 + foliation]
  D=2: d50 I3comp=10  I5comp=10  || FULL I3comp=12  I5comp=12
  D=3: d50 I3comp=28  I5comp=28  || FULL I3comp=32  I5comp=32
  D=4: d50 I3comp=107 I5comp=107 || FULL I3comp=125 I5comp=125
```

Foliation-invariance adds nothing under either linearization. Every
qualitative claim in LOG #422 stands. Every quantitative one must be
restated, and D49's 119 must be forward-corrected wherever it is quoted.

## MAJOR 1 — SF6, the negative control, is vacuous at two of its three depths

SF6 gates "I1 must stay LOOSE at every depth … if it did [collapse], the
instrument would be measuring its own construction." The receipt's own
SF5 output shows why it cannot fail at D = 2 or D = 3:

```
  D = 2: I1     0 constraints (rank 0)
  D = 3: I1     0 constraints (rank 0)
  D = 4: I1     6 constraints (rank 5)
```

**I1 imposes nothing at all** below depth 4 (the renewal pair `H3`/`h2e`
does not exist in a depth-2 or depth-3 truncation), so
`compdim = rank(M) = NB − 1` is forced, and SF6's `> 0` is a theorem-pass
at two of three depths. Pin §5 SF5 says in terms: *"A demand that is
vacuous at shallow depth must not read as a constraint."* The receipt
**prints** the zeros — honest — and then **counts those depths as
negative-control passes anyway**. The instrument is validated at one
depth, not three.

## MINOR 1 — "MORE THAN DOUBLES the constraint count" is false at two of the three depths

SF4's label and LOG #422 both say I5 "**MORE THAN DOUBLES** the constraint
count — 25 vs 16, 210 vs 109, 1,374 vs 610". `25/16 = 1.56`;
`210/109 = 1.93`. It more than doubles only at D = 4 (`2.25`). The gate's
actual predicate is `>`, which is correct; only the sentence overstates —
in three places.

## MINOR 2 — the one-sidedness doctrine is applied *conservatively*, and the unit is entitled to more than it takes

Pin §4(1): "a count > 1 (modulo overall scaling) is **RIGOROUS** in the
negative direction: it exhibits nearby non-proportional completions." As
stated that is not automatic — a kernel of the linearization exhibits a
nearby *solution* only at a regular point of the (quadratic) demand
variety, and the receipt never argues regularity. But the stronger fact is
true and cheap, and I certify it constructively: a kernel direction `v`
(corrected rows) with `Mv ≠ 0` generates a whole **line inside the
variety**, exactly:

```
[is a kernel direction an ACTUAL nearby solution?]
  D=2: nullspace dim=13; EXACT I3 residual at b*+1·v : 0/16 rows violated;
                                     at b*+(1/3)·v : 0/16
  D=3: nullspace dim=33; EXACT I3 residual at b*+1·v : 0/109 violated;
                                     at b*+(1/3)·v : 0/109
[and the nearby points are honest completions]
  D=2 t=1/10 : Z > 0 everywhere = True; completion DIFFERS from b* = True
  D=3 t=1/50 : Z > 0 everywhere = True; completion DIFFERS from b* = True
```

So there is an exact one-parameter family of **strictly positive,
genuinely different** completions satisfying depth-stationarity. The
negative is not "rigorous by doctrine"; it is *constructive*, and the unit
should say so — that is a materially stronger statement than a tangent
count and it costs one gate.

## MINOR 3 — SF3, the PRIMARY TARGET, has a predicate that cannot fail

`check("SF3 [THE PRIMARY TARGET] …", True if stat_dims else False, …)` —
i.e. `len(stat_dims) > 0`. It is a reporting gate, which is legitimate
under the pin's exit-0-either-way falsifier, but D58's A3 shows the house
style: reporting gates are *labelled* as such. SF3 is not, and it is the
gate the unit is named for. (SF7's anti-vacuity scan passes it because
`stat_dims` is run-bound — the scan's declared scope, correctly stated.)

## MINOR 4 — the pin's determinism gate was not built

Pin §5 SF7: "determinism gated across `PYTHONHASHSEED` 0/7/61/999 (D49's
own A4 defect makes this non-optional)." SF7 implements the AST scan only;
there is no hash-seed gate anywhere in the receipt. I ran it (three seeds,
identical output), so nothing is wrong — but a pin clause marked
"non-optional" was dropped silently.

## MINOR 5 — the AST strip is correct but under-gated in one direction

`_is_gate` strips `check`/`print` and *any* `sys.exit`. The receipt gates
`_exits == 1`, which is the repair for the own-defect (1). But the strip
also removes `check()` calls whose **side effects** D49 might have relied
on; it does not verify that no stripped statement bound a name. I checked:
D49's `check()` is pure (it only mutates `PASS`/`FAIL` and prints) and no
`print` binds anything, so the surgery is sound — but the gate that would
certify it (no `Store` context inside a stripped node) is one line and is
absent. Also `_body`'s count (`statements kept = … of …`) is printed but
never compared to anything.

## NIT 1 — no depth-5 attempt is recorded, only asserted

The declared cap says D = 5's exact rank "did not finish in 10 minutes and
was cut". That is a declaration in a comment, not a receipt artefact —
there is no timing gate and no partial output. The declaration is
honest and I do not doubt it; it simply is not a record.

## NIT 2 — the completion-map rank is printed but its interpretation is not stated

`rank(M) = 22 / 83 / 312` = `NB − 1` at every depth. The 1-dimensional
kernel is exactly the overall-scaling direction, which is *why*
`compdim = 0 ⇔ one ray` is the right reading. The receipt relies on this
and never says it. (I verified `rank(M) = NB − 1` at all three depths.)

## Checked and CLEAN (D50)

* **Receipt rerun:** `9 PASS / 0 FAIL`, `EXIT 0`, rc 0; output matches the
  committed `.out`. Deterministic across `PYTHONHASHSEED` 0/7/999.
* **The AST surgery works and the anchor holds** in the sense that
  matters: `len(BYLEN[4]) = 976`, cumulative through depth 4 = `1191`,
  `_exits = 1`. The unit's own owned defect (3) — that paper 30's
  much-quoted 1,191 is *cumulative*, with 976 at the layer — is correct and
  is a genuinely useful correction. **`b*` lies exactly on every demand
  variety** (residual 0 at every row, all depths).
* **`completion_rows` is the right object and is correctly linearized.**
  `r(h,e) = Z(h+e)/Z(h)`; the quotient rule gives numerator
  `v(h+e)Z(h) − Z(h+e)v(h)`, exactly the committed row. The
  per-row positive scale `Z(h)²` does not move the rank. This *is* "the
  image of the boundary-to-completion differential restricted to the
  demand's tangent space", and the identity used to compute it —
  `dim M(ker D) = rank([D;M]) − rank(D)` — is correct
  (`dim M(V) = dim V − dim(V ∩ ker M)`). **So the answer to the brief's
  question is yes: the completion dimension is the right quantity, and B1's
  lesson is correctly applied.** The defect is in `D`, not in `M`.
* **I5's foliation rows are correct** (`BAS[j][mem[0]] − BAS[j][hk]` is the
  differential of a linear condition) and SF4's conclusion is
  linearization-independent (table above).
* **SF5's strictness claim is real:** I3 has strictly more constraints than
  I2 at every depth (16 > 14, 109 > 101, 610 > 589) under either
  linearization, and strictly higher rank. The unit is not re-measuring B2.
* **The §3 post-mortem is correct.** The pin's sketch needs
  `Z(h+e)/Z(h)` to be a function of the two classes *event by event*; the
  record-level demand equates class-to-class transfers **summed over
  events**, so the path-consistency step never gets its hypothesis. I
  confirmed the coded demand is the aggregated one, and that the
  aggregated reading is the observable one. The diagnosis is sound and it
  is the unit's best paragraph.
* **Provenance:** `0cf42ed` (LOG #421 + pin, **no code**, 17:36) →
  `5500fe0` (receipt + `.out` + result note + LOG #422, 18:57). The pin
  genuinely preceded the code by 81 minutes.
* **The three owned defects** (silent exit-0 on run 1; the `_rank` width
  closure; the 1,191-vs-976 anchor error) are disclosed with mechanisms and
  are not counted against the unit anywhere in this review. The
  pre-registration — expectation *and its argument* written out first, then
  refuted — is exemplary and is what makes the unit legible.

---
---

# D51 — the H1 reduction

**VERDICT: REVISE. 2 BLOCKER / 3 MAJOR / 8 MINOR / 2 NIT.**

Files: `note-d51-h1-menu-visibility-pin.md`,
`code/d51_menu_visibility_exact.py` + `data/…out`, LOG #423/#424. No
result note.

The d42a admission layer was re-implemented from scratch for this review
(DFS reachability instead of the incremental union, brute-force MIS,
explicit permutation replay for PK1) and agrees with the committed
`d42b3` layer on all 6,471 histories — menus *with exact weights* and
posets — **zero mismatches**. Every published number reproduces exactly.
Both BLOCKERs are interpretation sentences.

## BLOCKER 1 — "since sigma IS an abstraction of exactly those projections, menus are sigma-determined here" is inverted; and (H2) is not settled — d44a already had both, stronger and two depths deeper

**Where.** Receipt VERDICT block; MV4's label ("(H2) IS SETTLED HERE, not
left dangling as d44a left it"); LOG #424; propagated verbatim into
`THE-THEORY-SO-FAR.md` §B3.2 and §B10.3.

**The defect.** D51's `projections()` key is **not** `sigma` — the receipt
never loads `sigma` at all (MINOR 6) — and it *refines* it:

```
distinct committed-sigma states on the depth-5 family = 32
distinct D51 projection keys                          = 209
D51 key determines sigma?   keys with >1 sigma state  = 0    <- REFINES sigma
sigma determines D51 key?   sigma states with >1 key  = 32   <- all 32, strictly
```

"`sigma` is an abstraction of the projections" means *projections ⇒
sigma*. MV3's `projections-equal ⇒ menus-equal` is therefore **implied
by** sigma-determination, not the converse. The same inversion voids MV4:
`key(h) → key(h+e)` says nothing about `sigma(h) → sigma(h+e)`, because
`sigma(h)` does not determine `key(h)`.

**And the real statements were already committed, two depths deeper.**
`d44a`'s CG1 is (H1) verbatim (34,375 histories, 36 sigma-classes, zero
exceptions; CG7b extends to 145,408 depth-7 transitions); CG2 is (H2)
verbatim. So "d44a leaves (H2) undetermined" is **false about d44a's
receipt**; what d44a left open is the logical question, which its note
answers in the *opposite* direction ("(H2) … NOT a consequence of (H1)").
Run on the same family with the committed `sigma` and renamed
weighted menus:

```
(H1) depth<=5, COMMITTED sigma, RENAMED menus with exact weights:
     sigma states = 32, states carrying >1 renamed menu = 0
(H2) depth<=5, COMMITTED sigma + renamed event:
     keys = 140, keys with >1 successor sigma = 0
```

Both hold — but they are d44a's results at a shallower depth. D51's
positive content is strictly subsumed by its own parent.

## BLOCKER 2 — MV2's mechanism cannot happen: an actor's own live proposals are ALWAYS in its own noop cone

**Where.** MV2's label, the VERDICT, LOG #424 ("Mechanism, **exhibited**"),
and the book §B3.2/§B10.3.

`regs_of(('p',a,b,x)) = {a}`, so every proposal by `a` lies on `a`'s own
register chain and is in `a`'s cone; any arb resolving it also touches
`a`'s register, so liveness agrees in both views:

```
actor's OWN live proposals identical in noop cone and full view: 12942/12942
every a-authored event of h lies in a's noop cone:               61804/61804
initiator in regs_of(e), over every menu-offered event:          34374/34374
```

**The real mechanism is missed SUPERSESSION**, and no witness is printed
anywhere in the receipt. Shortest witnesses of both fibre elements:

```
full (F,F) -> cone (T,F):  1004 occurrences
  actor A, h = [ ('p','B',v0,1), ('r','B',{('B',v0,1)},{('B',v0,1)}) ]
  A has proposed NOTHING.  B self-arbitrated, superseding v0.  Full view:
  v0 superseded -> has_p False.  A's cone is EMPTY -> has_p True.

full (F,F) -> cone (F,T):  1960 occurrences
  actor A, h = [ ('p','B',v0,1), ('r','B',…), ('p','A',v0,0) ]
  A's own proposal is in A's cone in BOTH views; the cone misses B's ARB,
  so it still sees v0 un-superseded -> has_r True.
```

The quoted clause is operative in neither. **The conclusion survives** —
re-established directly on option sets rather than the two bits:

```
prop_options(cone) vs prop_options(full), 12,942 (h,a) pairs:
   equal 11,938   cone STRICTLY MORE 1,004   cone strictly fewer 0
```

Told the obstruction is the own-proposal exclusion, a reader looks for an
argument handling that clause; the actual obstruction is that a lagged
view does not know its base has been superseded — much harder, and
precisely what LOG #432 later hit at transport.

## MAJOR 1 — the reduction reads a FIFTH thing: `view.pred`, via `incomparable()` → `edges()` → `mis_of` (membership) and `PK1` (weights)

Every `View` access on the admission-and-enumeration path, read line by
line from `d42b3` 108–218:

| reader | View data touched |
|---|---|
| `prop_options_in_view` | `holdings(a)`, `superseded`, `live` |
| `arb_components_in_view` | `components()`, `superseded`, `props` |
| `View.components` | `live`, `edges()` |
| `View.edges` | `props`, **`incomparable()` → `self.pred`** |
| `triples`, `edge_triples_of` (`'r'` branch) | `props`, **`edges()` → `self.pred`** |
| `candidates_for` (enumeration) | **`full.arbs`**, `full.live`, `full.props` |

`edge_triples_of` feeds `mis_of` (an **admissibility** test) and
`PK1(...)[wkey]` (the **weight**). `components()` records only the
partition; the edge set inside a component is strictly finer, and D51's
`projections()` drops it. This is D55 MAJOR 1's class — the omitted read is
where the weights live.

**At this scope it is inert, but by a theorem the unit never states, and
that theorem is (H0):**

```
views inspected = 40,845
same-base live-proposal pairs = 3,048;  COMPARABLE ones = 0
component sizes seen = {1: 18436, 2: 2540}
(base, member-triples) keys = 70;  keys carrying MORE THAN ONE edge set = 0
```

That is verbatim (H0)'s fourth clause. The committed `sigma` records the
edge set `E` explicitly, so d44a judged it necessary; D51 drops it without
argument. "[STRUCTURAL, exact]" must become "exact **given (H0)**".

## MAJOR 2 — MV1's headline surprise is forced by `regs_of`, and the pin's §5 fails for a reason the receipt never finds

`regs_of(('p',a,b,x)) = {a} = regs_of(('n',a))` — a propose candidate's
view **is** its actor's noop cone:

```
'p' candidate view == its actor's noop cone:  12916/12916
exceed by kind: {'r': 2032}    equal by kind: {'p': 12916, 'r': 6484}
```

So "p candidates lag too" is the idle lag recounted with different
multiplicities, not a second refutation; and pin §2's "a propose
additionally pulls in the wires the event touches" is false.

Pin §5 asserts `pred[e]` contains every live proposal on the base `b` the
candidate touches. Proposals are carried on the **proposer's register**,
not the base wire, and a propose does not touch wire `b` at all:

```
"pred[e] contains every live proposal on base b":
   'p' candidates  10476/12916   MISSES 2440
   'r' candidates   6484/8516    MISSES 2032
```

The pinned route dies on its own premise in 4,472 exhibited cases — a
cleaner refutation than the one claimed.

## MAJOR 3 — MV2's preamble contradicts MV1's own printed numbers, and the collapse it licenses leaves the `'r'` branch untested

Lines 201–204, printed directly under MV1's output: "MV1 shows p/r
candidates read the full-view values, so those are sigma-determined
outright." MV1's own output three lines above is `p 5,636/12,916`,
`r 3,820/8,516`. The preamble asserts the negation of the gate it follows,
and it is the sole justification for MV2 testing only the idle 2-bit pair.
Accidentally sound for `'p'` (MAJOR 2, a fact the receipt never notices);
**unsound for `'r'`**, whose view is a larger object running through
`arb_components_in_view`, `mis_of` and `PK1`. MV2 never touches it.

## MINOR 1 — MV3/MV4 capped at depth 5 against the pin's explicit instruction to beat d44a's depth 7

`CAP = 5`, hard-coded, no feasibility statement, 5.5 s runtime. Extended:

```
depth 6: total  34,375   MV3 keys =  481 violations = 0  MV4 pairs = 1122 viol = 0
depth 7: total 179,783   MV3 keys = 1089 violations = 0  MV4 pairs = 2530 viol = 0
```

Matches d44a's own 179,783 / 145,408. Damage nil — supplied by the referee.

## MINOR 2 — MV5 does not implement the pinned mutant, and 63% is a sampling artefact

The receipt drops the **lowest-indexed** proposal in the view with no
author test, and `break`s after the first `'r'` candidate:

```
receipt protocol (first 'r' per history):   tested = 4760  changed = 3008 (63%)
exhaustive over all 'r' candidates:         tested = 8512  changed = 6024 (70%)
the PINNED mutant (opponent-authored drop): tested = 2992  changed = 1776 (59%)
dropped proposal authored by the candidate's OWN actor: 7016 of 8512 (82%)
```

In 82% of cases it hides the candidate's *own* proposal — the opposite of
the pinned probe. "63%" is quoted three times as if it characterised the
object.

## MINOR 3 — invented threshold in MV5

Pin demands "must CHANGE **some** menu" (`> 0`); the receipt gates
`mut_changed > mut_tested // 2`. A 50% bar appears nowhere in the pin and
sits just under an observed 63%.

## MINOR 4 — dead variables, and the one witness the receipt computes is discarded

`live_keys` (never read); `multi` (never read, **and constant-true**:
`len([1 for h in FAM]) and len(v) >= 1`); `first_diff` — the MV1
counterexample witness — assigned and **never printed**, against pin §4
MV6's "witness branch live AND exercised". Unused imports `canon`, `V0`,
`Fr`. Six instances of the D54 MINOR-4 class; the receipt exhibits *no*
witness for any of its three negatives.

## MINOR 5 — three theorem-passes, unlabelled

`MV0(a)` is a `callable(...)` smoke test. **MV0(b)'s `opp_only` clause
cannot fail** — every event's initiator is in its own register set
(34,374/34,374), so every `a`-authored event is inside `a`'s cone
(61,804/61,804); extras are *never* `a`-authored, as a theorem of
`event_poset`. It is presented as a finding in LOG #424. And MV0(b)'s
"equal in 19,400" is 66.6% forced (12,916 are propose candidates).

## MINOR 6 — MV0(a)'s label misdescribes what is anchored, and `sigma` is never loaded

The tuple tested is `(candidates_for, admissible, prop_options_in_view,
arb_components_in_view)` — not the four projections; `projections()` is
re-implemented in D51. Pin §4 MV0 commits "`sigma` from the committed
d44a/D49 source"; `sigma` is never imported, ported or evaluated. For a
unit whose every conclusion is a statement about `sigma`, this is the
load-bearing pin promise, and it is the omission that made BLOCKER 1
possible — the comparison takes 3 seconds and immediately exhibits 209 → 32.

## MINOR 7 — MV1 and MV2 now assert the author's *negative* findings as pass conditions

LOG #424 confesses the original defect ("A gate that asserts the author's
hypothesis is not a gate") and commits its mirror image: MV1's predicate
is `by_kind['p'][1] < by_kind['p'][0] and …`; MV2's is
`not idle_determined and …`. On a family where the negatives do not occur
the receipt exits 1 on a *stronger* result.

## MINOR 8 — "MV3 … is the menu-level form of MV1+MV2" is not true

MV3 reads **only full views**; MV1/MV2 are about *candidate* views. MV3
neither implies nor is implied by either. (MV3 gives `keys = 209`,
violations 0 with *and* without weights, so "with exact weights" is honest
but not discriminating at this depth.)

## NIT 1 — no result note

D51 ships as pin + receipt + LOG. The reduction claim, residue and scope
live only in a `print()` block and a LOG entry — and all three defective
sentences reached `THE-THEORY-SO-FAR.md` from there. Repairs must reach
the book.

## NIT 2 — MV0's tally is complete but never says so

`less = 0`, `incomparable = 0`, `2,032 + 19,400 = 21,432 = 12,916 + 8,516`.
The census is exhaustive; the receipt does not state the trichotomy.

## Checked and CLEAN (D51)

* **Receipt rerun:** `8 PASS / 0 FAIL`, `EXIT 0`, rc 0, 5.5 s;
  **byte-identical** to the committed `.out`; identical under
  `PYTHONHASHSEED` 0/7/12345.
* **The layer, independently re-implemented**, agrees on all 6,471
  histories: 0 menu mismatches (events *and* exact `Fraction` weights),
  0 poset mismatches.
* **Family census** `{0:1,1:6,2:32,3:176,4:976,5:5280} = 6,471`, extended
  to 34,375 (d6) and 179,783 (d7, layer 145,408) — matching d49's and
  d44a's committed figures from code sharing nothing with either.
* **Every published number reproduces:** MV0 2032 / 19400 / max 4 /
  opponent-only; MV1 `n 4606/12942`, `p 5636/12916`, `r 3820/8516`; MV2's
  fibre map; MV5 4760/3008; MV3 209 keys, 0 violations; MV4 498 pairs,
  0 violations; MV6 8 calls, 0 bare. Zero discrepancies with LOG or `.out`.
* **D46a reproduced independently:** 1,016 of 12,942 actor-histories
  (7.85%), max excess 4; MV0's 2,032 is the same phenomenon per
  `(actor, candidate)`.
* **No admission/enumeration gap** (the D55 MAJOR-1 failure mode is
  absent): 106,748 events probed, 0 admissible-but-not-enumerated;
  `bases == holdings(A) ∪ holdings(B)` on 6,471/6,471.
* **The AST anti-vacuity scan is REAL — and better than D54's or D55's:**
  MV6 *does* require a run-bound name. Injecting one bare-constant
  `check()` gives `bare/unbound = 1`, `[FAIL] MV6`, exit 1.
* **The fifth read is inert at this scope** (0 of 3,048 same-base live
  pairs comparable in any of 40,845 views), so MAJOR 1 is a labelling and
  (H0)-dependence defect, not a computational error.
* **Provenance clean:** `93cb178` (LOG #423 + pin, **no code**, 19:41:41)
  → `abad0ba` (receipt + `.out` + LOG #424, 19:46:08).
* **Scope carried and later confirmed** by LOG #432's independent probe.
* **The self-corrections are exemplary** and are not counted against the
  unit anywhere: the pinned route declared refuted by the author's own
  receipt, three mis-specified gates confessed, and MV1's label saying the
  §5 sketch "is NOT quietly dropped". That discipline is why the defects
  above are findable at all.

---
---

# D53 — the empty-trace capacity correction

**VERDICT: REVISE. 1 BLOCKER / 2 MAJOR / 3 MINOR / 2 NIT.**

Files: `code/d53_sky_capacity_exact.py` + `data/…out`, LOG #426, and the
book's §B5.4 (which carries it as `[EXACT]`).

Every number in the audit reproduces exactly and the strata really are
D47's. What does not survive is the sentence the unit is named for.

## BLOCKER 1 — the structural theorem is false; SKY-A and SKY-C *do* shatter, on genuine Minkowski records

**Where.** Module docstring, banner, gate **SC1**'s label ("a system with
no empty trace cannot shatter ANY set, for any k >= 1"), gate **SC3** ("**SKY-A
and SKY-C can NEVER shatter, at any width or depth**"), the printed
STRUCTURAL REASON, the VERDICT, LOG #426, and the book §B5.4 under `[EXACT]`.

**The defect, in one line.** Shattering `S` requires a row **disjoint from
`S`**, i.e. `∅ ∈ {r ∩ S}` — not `∅ ∈ rows`. The two coincide only when `S`
is the *entire* direction set.

Minimal counterexample, decided by `d47a`'s **own** `shattered_set`:

```
rows = [{0}, {1}]   cols = [0,1]   empty row present: False
  d47a shattered_set(rows, [0,1], 1) = (0,)      <- a shattered 1-set
```

At the unit's own `k = 4`, on a genuine finite poset (base `e`, five covers,
one event above each non-empty `T ⊆ {c1..c4}`; 21 events, transitivity
verified by exhaustive triple check):

```
d47a sky(C, e=0, 'A'):  |dirs| = 5   rows = 16 distinct
  EMPTY ROW PRESENT = False    min row size = 1
  d47a shattered_set(rows, dirs, 4) = [c1, c2, c3, c4]     <- SHATTERED
SKY-C on the dual: |dirs|=21, empty row present = False, shattered 4-set = (1,2,3,4)
```

`c5`'s own trace `{c5}` supplies the empty trace *on the 4-set* while being
non-empty as a row. That mechanism is available at every width ≥ 5.

**And it happens in Minkowski.** A genuine exact-integer `M^{3+1}`
sprinkling (N = 300, all points distinct, order verified transitive), run
through `d47a`'s own `sky()`/`shattered_set()`:

```
SKY-A: shattered 4-sets at 24 base events
  e=29 |dirs|=22 |rows|=84 EMPTY TRACE=False shattered 4-set=(31, 92, 200, 245)
  the 16 traces on that 4-set: [] [31] [92] [200] [245] [31,92] … [31,92,200,245]
SKY-C: shattered 4-sets at 30 base events
  e=1  |dirs|=21 |rows|=76 EMPTY TRACE=False shattered 4-set=(31, 42, 97, 218)
```

Even on the records D53 audits, SKY-C shatters **3-sets** at 49 of 117
capable base events on `d47a`'s own `lattice_points(160)`, with zero empty
rows anywhere.

**What survives, and should be kept:** for a finite **transitive** poset
every SKY-A and SKY-C trace is non-empty, hence *a SKY-A/SKY-C sky can
never shatter its FULL direction set* (`k = |dirs|`). That is all the
empty-trace argument buys.

**What must be withdrawn:** SC1's universal claim; SC3's "can NEVER
shatter, at any width or depth"; "residue 2 is answered, and negatively";
"only SKY-B is usable"; the VERDICT's "dead for this test at every width
and depth"; and the book's `[EXACT]` label. D54's `K9-A`/`K9-C`
`[THEOREM-PASS]` labels remain correct *for the no-empty-trace fact they
gate*, but D54's pin inherits the false reason.

## MAJOR 1 — SC5 is not a necessary condition, and three downstream units gate on it

`capable()`'s docstring makes it necessity ("**only if** … the empty trace
is among them") and SC5's label makes it binding on all future sky units.
The first two clauses are necessary; the third is not, so SC5
**false-negatives**. On D53's own 554 pairs, with the empty-trace clause
replaced by nothing:

```
   SKY-A: >=4 dirs and >=16 distinct rows:  69   (SC5 admits 0)
   SKY-B: >=4 dirs and >=16 distinct rows:  52   (SC5 admits 52)
   SKY-C: >=4 dirs and >=16 distinct rows:  75   (SC5 admits 0)
   corrected total = 196, against SC5's 52
```

Consumers: `d54`, `d54b` K6, the D54 round-1 referee control, D55, and
`d55c` — whose entire M^{3+1} census is gated by it, so it never tests the
skies where the D53 mechanism shows up (71 untested skies on d55c's own
records; all zero, so no damage *there*, but the gate is wrong in principle
and it is what makes D55c blind to SKY-A/C).

## MAJOR 2 — "a TAUTOLOGY, not a measurement" is overstated: 144 of the 415 were genuinely capable

```
   D47-decidable                                        = 554
   without the empty trace ("structurally incapable")    = 415
     ... of which |dirs| >= 5 (empty-trace argument gives
         NO obstruction on any 4-subset at all)          = 335
     ... of which >= 16 distinct traces (the CORRECTED
         necessary condition is satisfied)               = 144
   best |{r & S}| over any 4-set, all three kinds        = 13 of 16
```

144 of the 415 pass the corrected necessary condition and reach 13 of the
16 required traces on their best 4-set; D47's zero over them is a real
measurement. The genuinely vacuous count is **271, not 415**, and the
"10.7× reduction" is a **2.8× reduction** (554 → 196).

## MINOR 1 — the true lemma needs two hypotheses the unit never states, and its stated reason is false for the covers themselves

"every event strictly above it lies above at least one cover" is **false
for the covers** — a cover lies above no cover. The trace survives only
because `d47a` writes `frozenset(c for c in dirs if c == f or C[c][f])`;
the reflexive `c == f` clause is load-bearing:

```
SKY-A on the 21-event poset WITHOUT the `c == f` clause: empty row = True
```

Second, the lemma needs **transitivity**, nowhere stated or gated:

```
C: 0<1, 0<2, 0<3, 1<2, 2<3, NOT 1<3   (acyclic, non-transitive)
  d47a SKY-A dirs = [1]   rows = [[], [1]]   EMPTY ROW = True
```

Minkowski and the transport `event_poset` are both transitive, so nothing
in the corpus breaks — but a claim quantified over "every record at any
width or depth" must carry the hypothesis.

## MINOR 2 — gate audit: 2 of 6 gates are theorem-passes, the headline numbers ride in one of them, and the structural claim is never gated

* **SC1 cannot fail.** Its "cap system" is built in-line as the literal
  power set of `{0,1,2,3}`; the arc clause includes the `ln = 0` term, so
  `∅ ∈ rows` for every `n` (checked n = 3..9). Zero falsifiable content —
  and it is the gate carrying the *false* necessity claim.
* **SC5 cannot fail.** `strict <= tot_dec` holds identically (≥16 traces
  ⊂ ≥2 traces). **Both headline numbers (52 skies, 10.7×) are printed in
  the detail string of a gate that cannot fail.**
* **SC0** is a `callable(...)` smoke test. **SC4** re-checks arcs and caps;
  none of the four "UNTOUCHED" claims in its label is tested by its
  predicate.
* Genuinely falsifiable: **SC2**, **SC3** — 2 of 6. The structural claim
  itself is printed as unconditional prose and is gated by nothing.

## MINOR 3 — the damage list omits the one D47b result that *is* damaged

`d47b` **TG3/TG4** runs the identical `len(dirs) < 4 or len(rows) < 2`
gate over all three sky kinds on transport skies and reports shattered
4-sets over that stratum — precisely the stratum D53 calls a tautology. It
is absent from a list whose whole point is completeness.

## NIT 1 — SC4's predicate tests none of its label

`_has_empty_cap and shattered_set(...) is None` re-derives SG0(a); the
label is a four-item damage assessment.

## NIT 2 — `capable(dirs, rows, k=4)` is written generic in `k` and only ever called at `k = 4`

The generality of the signature makes the false clause look like a general
law; at `k = |dirs|` it would even be correct.

## Checked and CLEAN (D53)

* **Receipt rerun:** `6 PASS / 0 FAIL`, `EXIT 0`, rc 0; **byte-identical**
  to the committed `.out`.
* **My generators equal D47a's** (point lists and causal matrices exact for
  N = 40, 80, 160; all orders transitive).
* **The SC2 table is exact**, my own sky/trace code: SKY-A 261/0/201/0;
  SKY-B 235/225/142/139; SKY-C 258/0/211/0; `201+211+142 = 554`;
  `554 − 139 = 415`.
* **The strata really are D47's:** `d47a`'s committed `.out` reports SG3b
  decidable by N as `[(40,64),(80,159),(160,331)]` = 554 — identical
  population.
* **SC5 arithmetic correct:** 52 corrected-capable skies (all SKY-B);
  `554/52 = 10.65`, printed 10.7×.
* **The no-empty-trace *fact* is real and is a theorem** on finite
  transitive posets (with MINOR 1's two hypotheses). SKY-A 0/261 and
  SKY-C 0/258 is not an accident of the sample.
* **The zero-shattering results all hold.** Ungated shatter-4 over every
  sky with ≥ 4 directions on all three D47 records: 0 / 0 / 0; best
  `|{r ∩ S}|` = 13/16 in all three. Nothing D47 measured is overturned.
* **Honest provenance.** The unit is a self-audit that found a real defect
  in a receipt of the same author's, and the "why the defect survived
  D47's own validation" paragraph is accurate as far as it goes. None of
  that is counted against it.

---
---

# D55c — the M^{3+1} control

**VERDICT: REVISE. 1 BLOCKER / 2 MAJOR / 4 MINOR / 2 NIT.**

Files: `note-d55c-m31-control-pin.md`, `code/d55c_m31_control_exact.py` +
`data/…out`, LOG #434/#435.

The instrument is sound and the census is exact — 1,578 and 740 reproduce
with zero shatterings, `mink4` is correct event for event, the pin
genuinely preceded the code. But **the headline is an artefact of the four
boxes chosen, and it reverses.**

## BLOCKER 1 — the zero is a density artefact; at higher density genuine M^{3+1} shatters 4 and the discriminator fires

**Where.** Gate **C3**'s detail and label; LOG #435 in five places
("Genuine discrete 3+1 skies do NOT shatter 4"; "THE DISCRIMINATOR READING
FAILS"; "NO sprinkled Minkowski record of ANY tested dimension shatters at
all"; "separates ENGINEERED COORDINATION from sprinkled geometry"; "The
meter measures the grammar, not geometry"); and LOG #436's STANDING
REDIRECT, which cites the reframe as support.

**The four committed configurations are sparse, and the density *falls*
across the sweep:**

```
  N= 80 box=24 : volume=  1327104  density=6.028e-05
  N=120 box=32 : volume=  4194304  density=2.861e-05
  N=160 box=40 : volume= 10240000  density=1.563e-05
  N=200 box=40 : volume= 10240000  density=1.953e-05
```

Running **D55c's own loop verbatim** (SKY-B, depths 1..10, the SC5 gate,
`shattered_set(...,4)`) on records that combine large `N` with higher
density:

```
M^{3+1} N=300 T=120 box=30 (dens 9.26e-05): capable(4)=1339  SHATTER-4= 395
M^{3+1} N=400 T=120 box=30 (dens 1.24e-04): capable(4)=2136  SHATTER-4=1050
M^{3+1} N=300 T= 80 box=20 (dens 4.69e-04): capable(4)=1363  SHATTER-4= 501
  shatter-4 by depth, N=300 T=120 box=30:
    {1: 2, 2: 17, 3: 51, 4: 75, 5: 92, 6: 74, 7: 53, 8: 31}  -- all inside the window
```

Re-verified with `d47a`'s **own** AST-extracted `sky()`/`shattered_set()`:

```
SKY-B event=0 depth=5 |dirs|=24 |rows|=92 empty=True SHATTERED 4-SET=(12,20,29,130)
  all 16 traces on it: [] [12] [20] [29] [130] [12,20] … [12,20,29,130]
SKY-B event=3 depth=3 |dirs|=21 |rows|=84 SHATTERED 4-SET=(16,45,129,245)
```

**It is density, not the generator.** At the *committed* density with the
same clean generator: `N=200 T=160 box=40 (1.95e-05)` → `capable(4)=917,
SHATTER-4=0, best 15/16`. The transition sits between ~`2e-05` and
~`9e-05`, and the committed records were **one trace short**.

**The matched 2+1 control — same N, T, box, seed, only the dimension
differs:**

```
M^{2+1} N=300 T=120 box=30: capable(4)=1484  SHATTER-4=0
M^{2+1} N=400 T=120 box=30: capable(4)=2157  SHATTER-4=0
```

**So the pre-registered discriminator holds.** Under SKY-A — the reading
D53 wrongly excluded — it is sharper, on a matched density ladder:

```
                        capable(4)                SHATTER-4        best |{r&S}|
  M^{2+1} N=150..500:  56/100/137/189/288/375     0 everywhere        15/16
  M^{3+1} N=150..500:  91/132/182/226/316/407     0/4/14/24/89/194    16/16
```

**And it is not merely sky size** (the trap D54 round 1 named).
Size-controlled, SKY-A, pooled over N = 200..500:

```
  M^{2+1}: |dirs|4-7: 0/173  8-11: 0/526  12-15: 0/304  16-19: 0/72  20-23: 0/14
  M^{3+1}: |dirs|4-7: 0/18   8-11: 1/162  12-15: 7/314  16-19: 63/337 20-23: 117/253
                                                       24-27: 88/127 28-31: 42/45
```

At `|dirs| = 12–15` the samples are comparable (304 vs 314) and the split
is 0 vs 7.

**The halt condition survives, and the continuum calibration transfers
exactly.** Shatter-5 on dense genuine `M^{3+1}` under every reading:

```
  SKY-A N=300/400/500: capable(5)=186/278/370  SHATTER-5=0  best 26/27/28 of 32
  SKY-C N=300/400/500: capable(5)=189/277/368  SHATTER-5=0  best 25/27/28 of 32
```

Sprinkled 2+1 shatters 3 and never 4 (arcs shatter 3); sprinkled 3+1
shatters 4 and never 5 (caps shatter 4; Radon stops at 5). **That is the
opposite of LOG #435's conclusion, and a better result than the one it
replaces.** What the four committed records license is: *at the sampled
densities (≤ 6e-05) no SKY-B sky of a sprinkled M^{3+1} record shatters 4*
— a scoped negative about a sparsity regime.

## MAJOR 1 — "NO sprinkled record of ANY tested dimension shatters at all" is false on D55c's own four records

The residue LOG #435 lists as open was already decided by the data in
hand. On **D55c's own configurations**, gated at `≥ 3 dirs, ≥ 8 traces`:

```
  N= 80 box=24: capable(3)= 260  shatter3=   0
  N=120 box=32: capable(3)= 173  shatter3=   0
  N=160 box=40: capable(3)= 665  shatter3= 382
  N=200 box=40: capable(3)=1053  shatter3= 705
  TOTAL: 2,151 capable, 1,087 SHATTER-3
```

and on genuine `M^{2+1}`, including `d47a`'s own records
(`N=160: 1002 capable, 492 shatter3`). Sprinkled records do not sit at
meter reading ~0; they sit at **3** — the circle's rung on D55's ladder.

## MAJOR 2 — the headline is gated by nothing, and the receipt contains no positive control

* **C3's predicate is `cap4 > 0`.** It passes whether `sh4` is 0 or 1,578.
* **C3 ⊂ C2** (`cap4 >= 200` implies `cap4 > 0`) — an unlabelled
  theorem-pass.
* **Nothing exercises `shattered_set` on a system that DOES shatter.**
  `first4` is never assigned; the witness branch is dead. **A
  `shattered_set` stuck at `None` would pass all four gates** and produce
  this exact output. `d47a`'s founding SG1 doctrine (a true positive *and*
  a true negative before the instrument is declared fit) is not carried
  into the unit that most needs it.
* Falsifiable content: **C0, C1, C2** — 3 of 4, and C0 only weakly.

## MINOR 1 — the pin's "fixed-box density control" is not implemented

Pin §2 promises it ("the D49-round B1 lesson: growing boxes confound").
`CONFIGS = [(80,24,7),(120,32,8),(160,40,9),(200,40,10)]` — three boxes,
growing with N; density falls **3.9×** across the first three. This is
verbatim the defect `d47a`'s own SG10 round-1 R2 correction withdrew a
headline over, and that the book records as `[EXACT]`: *"the correct
Minkowski variable is DENSITY, not point count."* Given BLOCKER 1, this is
load-bearing.

## MINOR 2 — the point generator is degenerate at power-of-two boxes

`latt4` draws `s % box` from an LCG mod `2^31`, whose low `k` bits have
period `2^k`, and consumes four draws per point:

```
  N= 80 box=24 seed= 7 -> DISTINCT =  74 / 80   mult hist {1:69, 2:4, 3:1}
  N=120 box=32 seed= 8 -> DISTINCT =  32 /120   mult hist {3:8, 4:24}  <-- power of two
  N=160 box=40 seed= 9 -> DISTINCT = 157 /160
  N=200 box=40 seed=10 -> DISTINCT = 196 /200
  every spatial axis takes exactly box/4 distinct values (spacing-4 sublattice)
```

`(120, 32, 8)` is 32 distinct locations carrying ~3.75 mutually
incomparable coincident events each. **Damage bounded:** it contributes
100 of 1,578 capable(4) (6.3%) and 28 of 740 capable(5) (3.8%), is the
weakest record (best `|{r ∩ S}|` = 9/16 vs 14 and 15), and consumed 62 of
111 s of runtime. The census is not driven by it — but a "genuine
sprinkling" that is 27% distinct should not be in a control, and the
spacing-4 sublattice means none of the four records is a free sprinkling.
(`d47a`'s 2+1 generator is clean: 40/40, 80/80, 159/160.) **The same
generator is load-bearing in D58 — see that unit's BLOCKER.**

## MINOR 3 — silent depth cap: the sweep stops at 10 while the records run to 12

Maximum future height-offset per record: **9, 4, 11, 12**. Completing the
range: `N=160` capable(4) 597 unchanged, shatter 0; `N=200` capable(4)
**848 (+19)**, shatter 0. Damage nil; the claim was not established over
the records' own depth range. (At `N=120` the record's height is 4, so six
of the ten swept depths are empty — the sweep is simultaneously over- and
under-specified.)

## MINOR 4 — the capacity diagnostic is unreported, and it is the difference between C3 and C1

```
  best |{r & S}| over 4-subsets, N=200 box=40: {8:114, 9:1, 11:144, 12:39,
                                                13:344, 14:120, 15:69}
  best |{r & S}| over 5-subsets, N=200 box=40: {16:114, 17:115, 18:88, 19:61,
                                                20:48, 21:67}
```

**C3's shatter-4 null was strong** — 69 skies one trace short — which is
why it collapses under a modest density increase. **C1's shatter-5 null is
weak**: the richest sky carried 21 of 32, so the *halt condition* passed
with a wide margin of incapacity — D53's own tautology trap one rung up,
on the gate the pin calls the halt condition. (It does survive properly
under SKY-A/SKY-C on dense 3+1: 0 shatter-5, best 28/32.)

## NIT 1 — the C0 anchor has weak bite

It constrains only the `z = 0` restriction. A deliberately broken `mink4`
that drops the `z` term entirely passes it (verified). One assertion at
`z ≠ 0` would close it.

## NIT 2 — two small pin deviations

Pin §2 promises a per-`(N, box, depth)` census; the receipt prints one
depth-aggregated line per `(N, box)`. C2's threshold is `cap4 >= 200`
under the label "exceeds several hundred pairs".

## Checked and CLEAN (D55c)

* **Receipt rerun:** `4 PASS / 0 FAIL`, rc 0, 116 s; output identical to
  the committed `.out` modulo the wrapper's `RC=0`.
* **`mink4` verified independently.** My own 4D exact causal order from the
  definition: on `(80,24,7)`, `(120,32,8)`, `(40,12,3)` — **point lists
  identical, causal matrices identical**. Irreflexive, antisymmetric,
  **transitive by construction** (all triples verified; no closure needed).
  Lightlike pairs correctly *included* (69 at `(80,24,7)`), self-pairs
  excluded, `dt > 0` strict. The sprinkling is deterministic.
* **The z = 0 anchor holds** under my `mink4` as well as theirs.
* **The whole census reproduces exactly** with my own SKY-B, capacity gate
  and shatter search: `52/100/597/829 = 1,578` capable(4);
  `0/28/219/493 = 740` capable(5); **0** shatter-4 and **0** shatter-5 at
  every committed configuration. LOG #435's numbers all match.
* **Provenance:** `e77215b` (LOG #434 + pin, no code) → `f38e98c` (receipt
  + `.out` + LOG #435). The pre-registration is exemplary — shatter-4
  declared **OPEN with a weak positive lean**, reported against the lean
  without flinching. That the lean turns out to have been *right* is not
  held against the unit; the pre-registration is what makes the reversal
  legible.
* **The halt condition is not tripped anywhere reachable:** zero shatter-5
  at every density tried, under SKY-B, SKY-A and SKY-C, best 28 of 32.
* **Anisotropic and diamond regimes behave as expected:** long-thin boxes
  give `capable(4) = 0` (no information either way); a causal-diamond
  sprinkling at `N=250, R=60` gave 116 capable and one shatter-4 —
  consistent with BLOCKER 1's density picture.

---
---

# D57 — the sector-exact closure

**VERDICT: REVISE. 1 BLOCKER / 1 MAJOR / 6 MINOR / 2 NIT.**

Files: `note-d57-sector-exact-pin.md`,
`code/d57_sector_exact_refinement.py` + `data/…out`, LOG #434/#436.

The refinement is correct, the algorithm computes what it says, and the
per-depth counts reproduce exactly at all four caps under an independent
implementation. Ground (2) — the refinement blow-up — stands, and I
strengthen it with the witness the pin promised and never printed. Ground
(1) — the one LOG #437 records as *carrying the verdict* — does not.

## BLOCKER 1 — "the arb sector prices 1/4 divided by the number of components, and the component count grows with depth" is refuted by the unit's own exhaustive data; the alphabet-infiniteness claim is unsupported

**Where.** Gate **S1**'s label ("**1/8 appears** — the arb sector prices
1/4 DIVIDED BY THE NUMBER OF COMPONENTS, so totals live in `{k/(4m)}` and
the component count `m` grows with depth (more bases, more live pairs).
**THE SECTOR ALPHABET IS NOT FINITE**"); the receipt VERDICT; LOG #436
("the arbitration sector prices 1/4 DIVIDED BY THE COMPONENT COUNT, and
components grow with depth … **THE SECTOR ALPHABET IS NOT FINITE**"); and
LOG #437's adjudication ("D57 ground (1) (structural, exact) **carries the
verdict**, ground (2) corroborates").

**The layer says otherwise.** `d42b1` line 328, the `'r'` branch of
`admissible`, is

```python
    D = len(comps) + len(view.merge_pairs(a))
    return True, F(1, 4) / D * law(ckey, et)[wkey]
```

— components **plus merge pairs**, not components. **My recomputation over
the entire exhaustive cap-6 family (243,769 histories, every arbitration
candidate, `(|comps|, |merge_pairs|, D, q)` recorded per event):**

```
SECTOR ALPHABET BY TYPE (cap 6, exhaustive):
   type 'd': ['1/4']        type 'm': ['1/4', '1/8']
   type 'p': ['1/4']        type 'r': ['1/2', '1/4', '1/8']
   type 'n': ['1/2', '1/4', '3/4']   (excluded by S1's ty != 'n' filter)

  arb sector total 1/2 : witness depth 6 actor A
    per-event (|comps|, |merge_pairs|, D, q)
        = [(1,0,1,1/4), (1,0,1,1/8), (1,0,1,1/8)]      sum = 1/2
  arb sector total 1/8 : witness depth 6 actor B
    per-event = [(1, 1, 2, 1/8)]                        sum = 1/8

COMPONENT / MERGE-PAIR CENSUS BY DEPTH (the census pin §3 promised):
   depth 1: max|comps|=1 max|merge_pairs|=0 max D=1
   depth 2: max|comps|=1 max|merge_pairs|=0 max D=1
   depth 3: max|comps|=1 max|merge_pairs|=0 max D=1
   depth 4: max|comps|=1 max|merge_pairs|=0 max D=1
   depth 5: max|comps|=1 max|merge_pairs|=0 max D=1
   depth 6: max|comps|=1 max|merge_pairs|=1 max D=2
```

**The component count is 1 at every depth, without exception, over every
one of the 243,769 histories the unit itself enumerated.** It does not
grow. The 1/8 witness has `D = 2` and that 2 comes **entirely from a merge
pair**. So the stated mechanism is false twice over: the denominator is
not the component count, and the component count does not grow.

**Consequence.** "THE SECTOR ALPHABET IS NOT FINITE" is an extrapolation
from a three-element observed alphabet `{1/2, 1/4, 1/8}` — finite,
exhaustively verified to depth 6 — via a premise the same data refutes.
The logic that would make it matter is sound (if `R` is finite and
lumpable then `T_s(h,c)` is constant on classes, so at most `|R|·|sectors|`
distinct totals appear; infinitely many values ⇒ no finite `R`) — but its
antecedent is not established. **The finite-alphabet prerequisite has not
been shown to fail.**

Ground (1) must be withdrawn as stated. It is plausibly rescuable — see
MAJOR 1 for why not at this scope, and for what a rescue would have to
show.

## MAJOR 1 — at the unit's own scope the alternative growth route is provably capped, so the observed alphabet may be complete

The merge-pair route is the only one the data supports, and at 2-actor
scope it is bounded by 1. `merge_pairs(a)` requires two held created
versions with **incomparable creation events**. Every arb or merge by `A`
has `A` in its register set (`regs_of` gives `props ∪ {vname}` for `'r'`,
where `arb_components_in_view` requires `a ∈ proposers`; and
`{a, ('mw',a,pk)}` for `'m'`), so **all creations authored by one actor lie
on that actor's register chain and are pairwise comparable**. With two
actors there are exactly two chains, so at most one incomparable pair:
`|merge_pairs(a)| ≤ 1`, hence `D ≤ |comps| + 1`, at every depth.

Combined with `max|comps| = 1` throughout the enumerated window, the
observed `{1/2, 1/4, 1/8}` is consistent with being the *complete* alphabet
at the unit's own scope. A rescue must either exhibit `|comps| ≥ 2` (I
believe it is reachable near depth 8 via the two-independent-arbs
divergence, but it is not exhibited anywhere and cap 6 cannot see it) or
move to ≥ 3 actors — a scope change. Neither is in the receipt.

## MINOR 1 — the pin promised a component census and a refinement witness; neither is delivered

Pin §3: "growing = blow-up, reported with the **component census** (which
distinction drives growth)"; "**witness pair printed** for the first
refinement at each iteration". The receipt prints neither. Both are
load-bearing: the census is the evidence for BLOCKER 1's claim, and the
witness is the evidence for the headline "even depth 3 crept at cap 6",
which rests on a single `16 → 17`. I supply both. The census is above; the
witness (my own refinement, cap 5 vs cap 6 class maps compared):

```
depth-3 histories: 452   cap5 classes: 16   cap6 classes: 17
SPLIT: one cap5 class of 84 histories splits 64 / 20 at cap6
  cap6 class A (64 histories), example:
     ('n','B'), ('n','B'), ('d','A','B',('v','v0'))
  cap6 class B (20 histories), example:
     ('p','B',('v','v0'),1),
     ('r','B',{('B',('v','v0'),1)},{('B',('v','v0'),1)}),
     ('d','B','A',('v',('v','v0'),(1,),('B',),'B'))
```

The split separates *nothing has been created* from *B has minted a version
and delivered it* — a substantive distinction over 20 histories, not a
marginal one-off. **This strengthens the unit's blow-up reading.**

## MINOR 2 — S1's predicate contains a conjunct that is true of every Fraction

```python
      quant_tested > 0
      and all((v * 4).denominator >= 1 for v in ALPH)      # always True
      and Fr(1, 8) in ALPH
```

`Fraction.denominator` is `≥ 1` by construction. The gate reduces to
`1/8 ∈ ALPH` — i.e. it certifies that the author's own observation
occurred, and certifies nothing about the "totals are exact rationals of
the form `k/(4m)`" claim in its label.

## MINOR 3 — `quant_bad` is computed and never gated (D54 MINOR-4 class)

`quant_bad` (= 704) counts totals outside `k/4`; it appears only in the
detail string. Nothing gates it in either direction, so the "twice
refuted" story is a printout.

## MINOR 4 — "totals tested = 1,084,928" double-counts across nested caps

`ALPH` and `quant_tested` accumulate *outside* the cap loop, and the cap-3
family is a prefix-subfamily of cap 4, of cap 5, of cap 6. My decomposition:

```
  cap 3: |FAM|=   521  non-idle sector totals=   2076
  cap 4: |FAM|=  3969  non-idle sector totals=  15676
  cap 5: |FAM|= 30729  non-idle sector totals= 120148
  cap 6: |FAM|=243769  non-idle sector totals= 947028
  SUM = 1,084,928   <- what the receipt reports as "totals tested"
```

The distinct count is **947,028**. Damage nil (the alphabet is a set), but
the advertised census is inflated ~1.15×.

## MINOR 5 — no anti-vacuity scan and no determinism gate, alone among its siblings

`d54`, `d54b`, `d55`, `d58`, `d60` and `d50` all carry an AST
anti-vacuity scan under LOG #403 MA-2; `d57` carries none — which is how
MINOR 2's always-true conjunct survived. The pin's "Exact Fractions; no
silent caps" discipline is met, but there is no `PYTHONHASHSEED` gate
either (I ran three seeds: identical).

## MINOR 6 — S2's stated decider and its implemented decider are different, and the stated one contains an invented threshold

The label says the signal is stabilization "once the cap moves **2+ levels
past d**". The implemented gate is `vals[-1] == vals[-2]` for any depth
with ≥ 3 cap values — which at `d = 4` compares lookaheads 1 and 2, not
"2+ levels past". And the "2+ levels" number is justified nowhere: depth 2
is stable from lookahead 1 onward (9, 9, 9, 9), which contradicts the
stated rule's premise. The verdict is unaffected — every comparable depth
fails the criterion under either reading — but the rule as written is an
invented constant, the thing the corpus's own D58 lesson forbids.

## NIT 1 — the docstring and banner are stale: cap 6 was run

Docstring: "at caps 3/4/5". Banner: "Caps 3/4/5 exhaustive; **cap 6 CUT
for runtime and declared (residue)**." The loop is `for CAP in (3,4,5,6)`
and cap 6 ran, and its result is the unit's headline. Two stale statements
in the file's own front matter.

## NIT 2 — the `'n'` sector is excluded from "the sector alphabet" without saying so

`if ty != 'n'` silently omits the idle sector, whose totals are
`{1/4, 1/2, 3/4}` (my census) — finite by construction from the three
quarter-bits. The claim "THE SECTOR ALPHABET IS NOT FINITE" is about
non-idle sectors only, and the label does not say so.

## Checked and CLEAN (D57)

* **Receipt rerun:** `3 PASS / 0 FAIL`, exit 0; output matches the
  committed `.out`. Deterministic across `PYTHONHASHSEED` 0/7/999.
* **The refinement is the coarsest sector-lumpable partition, and the
  starting point is legitimate.** Lumpability implies agreement on each
  sector *total* (sum `T_s(h,c)` over all `c`), so every lumpable partition
  refines the sector-signature partition; the greatest fixpoint below it is
  therefore the same object as the greatest fixpoint below the trivial
  partition. Starting from the signature partition is correct, not a
  finer-than-coarsest start.
* **The fixpoint counts reproduce EXACTLY under my own independent
  implementation** (my own enumerator, my own signature, my own iteration):

  ```
    cap 3: |FAM|=   521 iters=4 per-depth={0:1, 1:3, 2:9, 3:7}
    cap 4: |FAM|=  3969 iters=5 per-depth={0:1, 1:3, 2:9, 3:16, 4:9}
    cap 5: |FAM|= 30729 iters=6 per-depth={0:1, 1:3, 2:9, 3:16, 4:23, 5:11}
    cap 6: |FAM|=243769 iters=7 per-depth={0:1, 1:3, 2:9, 3:17, 4:27, 5:33, 6:16}
  ```

  Identical to the receipt at every cap and every depth, including the
  headline `16 → 16 → 17` creep at depth 3.
* **The boundary treatment does NOT bias toward blow-up — it biases toward
  closure, so the negative is conservative.** I ran the refinement a second
  time with the opposite boundary (the whole cap layer lumped into ONE
  class, the coarsest possible treatment):

  ```
    cap 4 boundary=trivial: {0:1, 1:3, 2:9, 3:7,  4:1}
    cap 5 boundary=trivial: {0:1, 1:3, 2:9, 3:16, 4:9,  5:1}
    cap 6 boundary=trivial: {0:1, 1:3, 2:9, 3:16, 4:23, 5:11, 6:1}
  ```

  Exactly: **cap-C-with-signature ≡ cap-(C+1)-with-trivial**, at every
  depth. So the signature boundary is worth precisely one extra level of
  lookahead, and both truncations *under*-refine relative to the untruncated
  fixpoint (the cap layer's true successors would split it further). The
  reported per-depth counts are therefore **lower bounds** on the true
  counts: observed growth is genuine growth, and the blow-up reading is the
  conservative one. **The brief's suspicion is answered in the unit's
  favour.**
* **Ground (2) stands.** Depth 3 crept `7 → 16 → 16 → 17`; depth 4
  `9 → 23 → 27`; depth 5 `11 → 33`. Nothing comparable stabilized. With the
  witness of MINOR 1 supplied, the reading "the refinement keeps splitting
  beyond its lookahead" is supported.
* **The refinement loop is correct.** `key` includes `cls[h]`, so
  refinement is monotone; equal class cardinality therefore implies the
  identical partition, so the `stable`-then-assign-then-break order is
  sound. All sorting is by `repr` of deterministic objects.
* **The 1/4 delivery-sector fact is real** — the `'d'`, `'p'` sectors carry
  exactly `1/4` throughout, and `'m'` carries `{1/4, 1/8}`. The author's
  own note that this was "sector-specific, not a law" is correct and is a
  genuine self-correction.
* **Provenance:** `e77215b` (LOG #434 + both pins, no code, 08:52) →
  `c3f9535` (receipt + `.out` + LOG #436, 09:08). The pin preceded the
  code by 16 minutes. The unit's two refutations of its own pre-registered
  law are recorded with mechanisms and are not counted against it.

---
---

# D58 — the atlas instrument

**VERDICT: REVISE. 1 BLOCKER / 2 MAJOR / 5 MINOR / 3 NIT.**

Files: `note-d58-atlas-instrument-pin.md`,
`code/d58_atlas_instrument_exact.py` + `data/…out`, LOG #438/#439. No
result note.

I rebuilt the entire atlas — my own poset closure, heights, SKY-B, cover
enumeration and overlap — and reproduced **every number in the receipt
exactly** (M21 77/51/11/465/0.1197; M31 88/57/31/2108/0.5398; SH4 17/44,
SH5 30/84, WALK 2/30, overlaps 0.473/0.468/1.000). The homogeneity gap A2
reports is real and survives. The overlap half of the instrument does not.

## BLOCKER 1 — the M^{3+1} control is not a sprinkling, and the flagged overlap finding candidate REVERSES against genuine ones

**Where.** `C31 = mink4(latt4(120, 32, 8))`; gate **A1**'s label (the
control validation, and the "FINDING CANDIDATE … **CONFOUNDED here by
differing sprinkling densities (box 60 vs 32)** — deconfounding it is a
residue"); gate **A3**; LOG #439 ("M^{3+1} N=120 — 73%, mean overlap ~0.54
(d=3: ~0.94). **THE M21-vs-M31 OVERLAP DIFFERENCE IS A FINDING CANDIDATE,
CONFOUNDED by differing densities**"); LOG #439's residue list; and D60,
which cites both numbers as comparators.

**The generator.** `latt4` draws each coordinate as `s % box` from an LCG
`s = (1103515245·s + 12345) mod 2^31`. The low `k` bits of that LCG have
period `2^k`; each point consumes exactly 4 draws, so a fixed coordinate
slot advances 4 steps per point and its low-`k`-bit subsequence has period
`2^{k−2}`. **When `box` is a power of two the sprinkling collapses.**
`box = 32` is the committed M^{3+1} control:

```
M31 box= 12  distinct points=102/120  distinct x-values= 3
M31 box= 16  distinct points= 16/120  distinct x-values= 4   <-- power of 2
M31 box= 20  distinct points=117/120  distinct x-values= 5
M31 box= 24  distinct points=109/120  distinct x-values= 6
M31 box= 32  distinct points= 32/120  distinct x-values= 8   <-- COMMITTED
M31 box= 40  distinct points=120/120  distinct x-values=10
M31 box= 48  distinct points=115/120  distinct x-values=12
M31 box= 64  distinct points= 64/120  distinct x-values=16   <-- power of 2
```

(Every spatial value is ≡ 2 mod 4 at every box — the low two bits of the
4-step subsequence are constant — so *no* box gives a free sprinkling; the
power-of-two case additionally collapses the point set.) The committed
control is **32 distinct spacetime locations wearing 120 labels**: ~3.75
mutually incomparable coincident events per location, max poset height 4.
The chart statistics are correspondingly deformed:

```
                              homog(|D|>=2)  |D|>=4  mean|D|  max|D|  mean omega
  M31 N=120 box=32 [DEGEN]        0.733       0.475   15.02     31       0.540
  M31 N=120 box=20 (genuine)      0.700       0.425    3.40     11       0.089
  M31 N=120 box=24 (genuine)      0.767       0.675    5.87     15       0.076
  M31 N=120 box=40 (genuine)      0.700       0.467    4.19     15       0.093
  M31 N=120 box=48 (genuine)      0.842       0.667    5.85     15       0.056
  M31 N=120 box=60 (genuine)      0.658       0.492    4.38     14       0.068
  M21 N=120 box=60 (D58's own)    0.642       0.425    3.26     11       0.120
```

Mean chart width **15.02 against 3.4–5.9**; max width 31 against 11–15.

**And the flagged finding candidate reverses.** LOG #439's headline number
is `M21 0.12 vs M31 0.54`. Against *genuine* M^{3+1} sprinklings at the
same `N`, mean overlap is **0.056–0.093 — below M21's 0.120.** The
difference is real, it is in the opposite direction, and it is not
density-confounded — it is generator-degeneracy plus MAJOR 1's structural
zeros. **The brief asked whether a matched comparison was cheap: it is (a
few seconds), I ran it, and it resolves the flagged finding candidate —
negatively.** The residue in LOG #439 can be closed, with the sign flipped.

**What survives:** A1's *homogeneity* validation. Genuine M^{3+1}
sprinklings give homogeneity 0.658–0.842, all comfortably above the
`>= 1/2` bar, so the instrument is validated on controls after all. What
must be withdrawn is every M^{3+1} *number* (73% / 0.54 / 0.94), the
"finding candidate" framing, and the density diagnosis. The control must
be rebuilt on a non-power-of-two box, and preferably on a generator that
does not sample a spacing-4 sublattice at all.

## MAJOR 1 — the pin's structural premise is false: cover pairs do NOT generally share a height layer, and the failures are the dominant term in the reported overlap

Pin §2: "for a cover pair `e ⋖ e'`, the sets `D_e(d)` and `D_e'(d−1)` live
at the **SAME height layer**." `D_e(d)` sits at absolute height `h[e]+d`;
`D_{e'}(d−1)` at `h[e']+d−1`. These coincide **iff `h[e'] − h[e] = 1`**,
which a cover pair does not guarantee (a cover's height can jump if it has
a taller incomparable predecessor). My census of the very pairs D58
measures:

```
  M21 N=120 box=60, d=2: cover-pair height gaps {1:180, 2:173, 3:69, 4:35, 5:7, 6:1}
                          zero-overlap fraction = 0.7333
  M31 N=120 box=32, d=2: cover-pair height gaps {1:1996, 2:112}
                          zero-overlap fraction = 0.2861
  brick m=8 (D60),  d=2: cover-pair height gaps {1:93, 2:3}
                          zero-overlap fraction = 0.0312
```

**285 of M21's 465 measured pairs (61%) have gap ≥ 2 and contribute a
structural zero** — not a measurement of poor charting. Removing them:

```
                              ALL pairs           GAP-1 ONLY        gap-1 share
  M21 N=120 box=60      465, mean 0.1197     180, mean 0.3093        0.387
  M31 N=120 box=32      2108, mean 0.5398   1996, mean 0.5701        0.947
  brick m=8 (D60)         96, mean 0.6510     93, mean 0.6720        0.969
```

So the reported `ω` is largely a measurement of **how chain-like the poset
is** (M21's max height is 15, the degenerate M31's is 4), not of how much
charts overlap. Restricted to gap-1 pairs and genuine sprinklings, M21
(0.31) is *above* M31 (0.19–0.24) — the same reversal as BLOCKER 1, by an
independent route.

## MAJOR 2 — `ω` is not an overlap: it is a chart-size ratio, and the "identity transition on the intersection" framing has nothing to measure

**Theorem (of the committed SKY-B definition).** For a cover pair
`e ⋖ e'`:

* if `h[e'] − h[e] = 1` then `D_{e'}(d−1) ⊆ D_e(d)`, so
  `ω(e,e') = |D_{e'}(d−1)| / |D_e(d)|`;
* otherwise `D_{e'}(d−1) ∩ D_e(d) = ∅`, so `ω(e,e') = 0` identically.

*Proof.* `D_e(d) = {f : e < f, h[f] = h[e]+d}` and
`D_{e'}(d−1) = {f : e' < f, h[f] = h[e']+d−1}`. If `h[e'] = h[e]+1` the
height conditions coincide and `e < e' < f ⇒ e < f`; otherwise the height
conditions are incompatible. ∎

Verified over 3,910 cover pairs on four different records — brick, M21,
M31 box 32, M31 box 48 — **zero violations of either clause**. And
independently: the Jaccard index `|A∩B|/|A∪B|` equals `ω` to the last
Fraction on all of them (`0.651/0.651`, `0.120/0.120`, `0.540/0.540`,
`0.056/0.056`, …), which is only possible under containment.

So there is no two-way overlap anywhere in the instrument: the
intersection is *always* the whole successor chart. The pin's "how much of
one chart survives into its neighbour" is a fair description of the
quantity; "the transition is the identity on their intersection" and "the
cocycle question becomes real only once non-identity transitions exist" are
not, because containment leaves nothing for a transition to act on
non-trivially. The instrument's second leg measures a **chart-size ratio
along covers**, and the atlas language should say so.

Consequence for the comparisons: `ω` systematically favours **thin-charted**
records. A record whose charts have 2–3 directions reaches high `ω` when a
neighbour retains 2; a record whose charts have 15–31 needs 15–31 to be
retained. That is exactly the asymmetry between the brick and the
sprinklings in D60.

## MINOR 1 — the `|D| >= 4` column is computed at every record and never compared

`atlas()` computes `w4` and stores it in `res[d]`; no gate and no printed
comparison uses it. It is the column that reverses the atlas verdict for
D60's brick (sprinklings 0.42–0.68, brick 0.000 — see D60 MAJOR 3), and it
was in hand. D54 MINOR-4 class, on the one variable that mattered.

## MINOR 2 — the overlap population is conditioned on the source chart only

`if len(DIRS[e]) < 2: continue` filters on `e` and never on `e'`. The
statistic is therefore computed on a self-selected subpopulation whose size
varies by two orders of magnitude across records (2 pairs for WALK, 2,108
for M31), and the receipt reports the means side by side with no
sample-size annotation. WALK's `mean omega = 1.00` — the **highest value in
the whole table** — rests on two pairs, and LOG #439 does not say so.

## MINOR 3 — A2's predicate cannot fail

`all(k in R for k in ('SH4','SH5','WALK'))` is true by construction three
lines after the three assignments. The pre-registered comparison
("engineered records PATHOLOGICAL as atlases") is in the *detail string*,
not the predicate. A3 is likewise a reporting gate — but A3 **is labelled
as such**, which is the right house style and makes A2's silence the
defect.

## MINOR 4 — the "sprinkling homogeneity floor 0.64" is a two-point floor

`spr_homog = min(M21, M31)` over exactly two records, one of which is
invalid (BLOCKER 1). Over five genuine M^{3+1} boxes and seven M^{2+1}
boxes I measure homogeneity from **0.642 to 0.842**, so 0.64 happens to
survive as a floor — but it is an empirical minimum over two samples,
propagated into D60 as a hard-coded comparator constant. Given LOG #439's
own lesson about invented constants, this deserves a range, not a number.

## MINOR 5 — no result note

D58's measurements, scope and residues live only in a `print()` block and
LOG #439, and D60 cites them from there. Repairs must reach LOG #439 and
D60's receipt constants together.

## NIT 1 — the generic walk is reported as "6%" and as "0.07" for the same 2/30

LOG #439 says "generic 2-actor walk **6%**"; A2's detail prints
"generic walk = **0.07**"; D60 hard-codes `WALK = Fr(7,100)`. All three are
`2/30 = 6.67%` under different rounding rules.

## NIT 2 — 100·w2//n floor-rounds the printed percentages

`100*w2//n` gives M21 "64%" for `77/120 = 64.17%`. Harmless, but it is the
number that becomes D60's `SPRINKLE_FLOOR = Fr(64,100)`, in the direction
that makes the comparator easier to clear.

## NIT 3 — pin-to-receipt in three minutes

`9a76ac7` (pin, no code, 09:56:16) → `439c75a` (187-line receipt + `.out`
+ LOG #439, 09:59:27). The record's order is correct and the pin contains
no code; a 191-second gap simply means the pre-registration's protective
value rests on the author's discipline rather than on the clock.

## Checked and CLEAN (D58)

* **Receipt rerun:** `5 PASS / 0 FAIL`, exit 0, 23 s; output matches the
  committed `.out`. Deterministic across `PYTHONHASHSEED` 0/7/999.
* **Every published number reproduces under my own atlas code** (my own
  poset closure, heights, SKY-B, covers, overlap; nothing from `d47a`
  except the definitions):

  ```
   M21 N=120 d=2: 120 events, |D|>=2 at 77, |D|>=4 at 51, max 11, 465 pairs, om 0.1197
   M31 N=120 d=2: 120 events, |D|>=2 at 88, |D|>=4 at 57, max 31, 2108 pairs, om 0.5398
   shatter-4 d=2: 44 events, 17 (0.386), max 3, om 0.473
   shatter-5 d=2: 84 events, 30 (0.357), max 3, om 0.468
   generic walk : 30 events,  2 (0.067), max 2, om 1.000
  ```

  Exact agreement, including the committed Fractions `73489/613800` and
  `1022991/1895092`.
* **A2's homogeneity gap is real and survives every correction.** Against
  the *corrected* sprinkling family (twelve genuine configurations,
  homogeneity 0.642–0.842) the engineered records sit at 0.357–0.386 and
  the generic walk at 0.067. The pre-registered conclusion — the grammar's
  shatter records are the opposite of atlases — stands untouched, and it is
  the unit's durable content.
* **The A1 self-correction is exemplary** and is not counted against the
  unit: a hard-pinned 1/3 overlap floor was discovered to be an invented
  constant, and the gate was restated to validate on homogeneity and
  *report* overlap. That restatement is what left the overlap numbers as
  reports rather than claims, which is why BLOCKER 1's damage is bounded.
* **The heights function is a genuine grading:** I verified
  `C[i][j] ⇒ h[i] < h[j]` over every ordered pair of every record used
  here, so SKY-B's directions are automatically a pairwise-incomparable
  antichain (no hidden restriction).
* **Provenance:** `9a76ac7` (LOG #438 + pin, no code) → `439c75a`
  (receipt + `.out` + LOG #439). Pin before code.

---
---

# D60 — the crystal

**VERDICT: REVISE. 0 BLOCKER / 3 MAJOR / 5 MINOR / 3 NIT.**

Files: `note-d60-crystal-question-pin.md`, `code/d60_crystal_exact.py` +
`data/…out`, LOG #447/#448. No result note.

**The object is real and it is forced.** I rebuilt the brick record from
the committed menu with my own driver and then re-ran the build with **all
eight actors offered at every one of the 65 steps** — the D55-round-1
full-width test — and got the identical record, with every specification
matching **exactly one** menu entry. My own poset, heights, SKY-B, covers
and overlap reproduce 50/65 and 0.6510 exactly. Nothing about the
construction is in doubt. The three MAJORs are about what the numbers are
compared to, what they are a function of, and which metric was chosen.

## MAJOR 1 — the comparators are cited from D58's invalid M^{3+1} control, and one of the two "above" claims does not survive a valid one

LOG #448: "homogeneity **77% — ABOVE the sprinkling floor (64%, M21) and
above M31's 73%**; mean overlap 0.65 — **above BOTH sprinkling
comparators (0.12 / 0.54)**." Both M31 numbers come from
`mink4(latt4(120, 32, 8))`, which is 32 distinct points wearing 120 labels
(D58 BLOCKER 1). Against genuine M^{3+1} sprinklings at the same `N`:

```
                            homogeneity(d=2)   mean omega(d=2)
  brick m=8 (65 events)          0.769              0.651
  M21 N=120 box=60               0.642              0.120
  M31 box=32 [D58's, DEGEN]      0.733              0.540
  M31 box=20 (genuine)           0.700              0.089
  M31 box=24 (genuine)           0.767              0.076
  M31 box=40 (genuine)           0.700              0.093
  M31 box=48 (genuine)           0.842              0.056
  M31 box=60 (genuine)           0.658              0.068
```

* The **overlap** claim strengthens: 0.651 against 0.056–0.120, not
  against 0.54. Good news for the unit, from a corrected comparator.
* The **homogeneity** claim does not: "above M31's 73%" is a claim against
  a non-sprinkling, and against genuine M^{3+1} the brick's 0.769 sits
  *inside* the sprinkling band (0.658–0.842) and **below** the box-48
  configuration. The licensed statement is "comparable to the sprinkling
  band", which is exactly what pin §3 pre-registered ("comparable to the
  sprinkling floor 0.64") — the LOG overstates its own pin.

## MAJOR 2 — 77% is a function of two unfixed blueprint parameters, and only one setting was run

The pin commits "**m** ring actors" and an unspecified number of rounds;
the receipt hard-codes `M = 8`, `ROUNDS = 14`. Both move the headline
monotonically or non-monotonically, and neither is gated. My sweep (the
generic even-`m` brick pairing, every event menu-selected, no refusals):

```
=== ROUNDS sweep at M = 8 ===
  R= 4 ( 25 ev): homog 0.440   |D|>=4 0.000  mean|D| 1.16  omega 0.583
  R= 8 ( 41 ev): homog 0.634   |D|>=4 0.000  mean|D| 1.80  omega 0.635
  R=14 ( 65 ev): homog 0.769   |D|>=4 0.000  mean|D| 2.25  omega 0.651   <- COMMITTED
  R=20 ( 89 ev): homog 0.831   |D|>=4 0.000  mean|D| 2.45  omega 0.656
  R=30 (129 ev): homog 0.884   |D|>=4 0.000  mean|D| 2.62  omega 0.660
  R=50 (209 ev): homog 0.928   |D|>=4 0.000  mean|D| 2.77  omega 0.663

=== RING-WIDTH sweep at 14 rounds ===
  M= 4 ( 33 ev): homog 0.788  max|D| 2   omega 0.960
  M= 6 ( 49 ev): homog 0.776  max|D| 3   omega 0.658
  M= 8 ( 65 ev): homog 0.769  max|D| 3   omega 0.651   <- COMMITTED
  M=10 ( 81 ev): homog 0.753  max|D| 3   omega 0.647
  M=12 ( 97 ev): homog 0.732  max|D| 3   omega 0.643
  M=16 (129 ev): homog 0.682  max|D| 3   omega 0.638
```

Homogeneity crosses the cited `0.64` comparator at about `R = 8` and rises
without bound toward 1; it *falls* with ring width and would drop below the
comparator at `M ≈ 20`. **"77%" is not a property of the mechanism; it is a
property of `(M=8, R=14)`.** The honest and considerably stronger claim is
the asymptotic one, which my sweep establishes and the unit does not
state: *the shortfall from 1 is entirely boundary* — see CLEAN below, where
the interior of the committed record reads **0.902** — *so a re-delivery
circuit's homogeneity tends to 1 as it runs.* That is a mechanism
statement, which is what the scale doctrine asks the unit to certify;
`0.769` is a snapshot.

## MAJOR 3 — "sprinkling-grade atlas profiles" holds on the two metrics chosen and fails on chart width, and D58 had already measured the number that shows it

LOG #448 and the commit message: "**ABOVE the sprinkling floor on both
metrics: sprinkling-grade atlases are admissible.**" On a third, equally
natural metric — chart *width*, the thing "|D| ≥ 2" is a threshold of — the
brick is at the floor:

```
                             |D|>=2   |D|>=4   mean|D|   max|D|
  brick m=8 (committed)       0.769    0.000     2.25       3
  brick at EVERY (M,R) tried  ≥0.44    0.000    ≤2.77       3
  M21 N=120 box=60            0.642    0.425     3.26      11
  M31 box=24 (genuine)        0.767    0.675     5.87      15
  M31 box=48 (genuine)        0.842    0.667     5.85      15
```

The brick has **no 4-direction chart anywhere, at any parameter setting**,
while both sprinkling families carry them at 42–68% of events. The unit
does report `brick max|D| = 3` (gate C5) and does say "1+1-thin by design",
which is honest — but it never places that number beside D58's own
`max = 11` and `max = 31`, and D58 computed a `|D| >= 4` column at every
record and never used it (D58 MINOR 1). The one comparison that cuts
against the headline was one line away in the parent unit and is not made.
"Sprinkling-grade" must be qualified to the two metrics it holds on, or
the width comparison must be reported alongside.

## MINOR 1 — the comparator constants are hand-transcribed *rounded printed percentages*, and one rounds in the unit's favour

```python
SPRINKLE_FLOOR  = Fr(64, 100)   # exact value 77/120 = 0.641666...
ENGINEERED_CEIL = Fr(39, 100)   # exact value 17/44  = 0.386363...
WALK            = Fr( 7, 100)   # exact value 2/30   = 0.066666...
```

D58 computed all three as exact Fractions; D60 re-enters them as two-digit
decimals read off a floor-rounded printout. `64/100 < 77/120`, so the
"TILES AT SPRINKLING GRADE" test is made *easier*; `39/100 > 17/44`, so C3's
gate is made *harder* (conservative). The margins are large enough that
nothing turns on it here — but in a corpus whose discipline is exact
Fractions and no invented constants, comparators should be imported, not
re-typed.

## MINOR 2 — `WALK` is a dead variable

Assigned at line 184, referenced by no predicate and no detail string
(C3's label quotes "generic walk 7%" as literal text). D54 MINOR-4 class.

## MINOR 3 — C5 is a theorem-pass, and C4 is an unlabelled reporting gate

`C5`'s predicate is `wmax1 >= 2`, which is *implied* by C3 having found
`h1 = 50/65 > 0` — if any event carries `|D| ≥ 2` then `max|D| ≥ 2`. `C4`'s
predicate is `om1 is not None and om2 is not None`, which is implied by
`pairs > 0`, which is implied by the same fact. Both are legitimate
reporting gates; D58's A3 shows the house style is to *say so*, and neither
does. That is 2 of the 7 advertised PASSes.

## MINOR 4 — at d = 3 the ordering the headline rests on reverses, and the LOG reports d = 3 without the comparison

```
  brick d=3: homogeneity 0.738   (LOG #448: "At d = 3: 73% / 0.71")
  M21 N=120 d=3: homogeneity 0.750     <- D58's own committed number
```

The brick is **below** the M^{2+1} sprinkling comparator at `d = 3`. LOG
#448 reports the brick's `d = 3` numbers and makes no comparison; the
"above the sprinkling floor" ordering is `d = 2`-specific and should say
so. (The overlap ordering does hold at both depths.)

## MINOR 5 — no result note

As with D58 and D51: the scope lines, the residues and the verdict live
only in a `print()` block and LOG #448, from which the book's D60 patch
takes them. Repairs must reach all three.

## NIT 1 — the receipt prints 76% and the LOG says 77%

`100*w2//n` floors `50/65 = 76.92%` to `76`; C3's `%.2f` rounds it to
`0.77`; LOG #448 and the commit message say `77%`. All three are the same
Fraction; the same file reports it two ways five lines apart.

## NIT 2 — pin-to-receipt in 102 seconds

`0056d59` (pin, no code, 11:20:05) → `d5b8e72` (223-line receipt + `.out`
+ a 209-line book patch + LOG #448, 11:21:47). Order in the record is
correct; the interval means the pre-registration's value here is the
author's discipline, not the clock. Recorded, not counted.

## NIT 3 — CRYSTAL-2D's phase generator degenerates at K = 3

`range(0, K-1, 2)` and `range(1, K-1, 2)` both yield a single index at
`K = 3`, so the four "phases" reduce to four fixed pair sets of three
deliveries each. The grid is therefore even smaller an object than "3×3, 46
events" suggests, which reinforces rather than contradicts the unit's own
"size is the named residue".

## Checked and CLEAN (D60)

Everything below is my own recomputation
(`/private/tmp/.../rev/indep.py`, `width.py`, `d60ctl.py`, `jac.py`).

**A. Receipt rerun.** `7 PASS / 0 FAIL`, exit 0; output **byte-identical**
to the committed `.out`. Identical under `PYTHONHASHSEED` 0/7/999.

**B. The brick record, rebuilt independently and FORCED.** I re-derived the
blueprint from the pin and drove `candidates_for` with my own builder:

```
  events = 65   refusal = None   actors = 8   prefix (mint+spread) = 9
  event census = {p:1, r:1, d:63, n:0, m:0}
  max hits per specification = 1      (1 => the record is FORCED)
  restricted menus: widths 2..10
  FULL-MENU replay (all 8 actors offered at every one of the 65 steps):
      events 65, refusal None, max hits 1, menu widths 79..136
      identical to the restricted-menu record: True
```

Every event is menu-offered against the *unrestricted* layer, and every
specification matches exactly one candidate, so nothing was tie-broken.
C1's claim is verified in its strongest form.

**C. The poset.** My own `regs_of` re-implementation plus my own
Floyd–Warshall closure equals the layer's `event_poset` exactly (1,830
ordered pairs); irreflexive, antisymmetric, transitive; heights are a
strict grading (`C[i][j] ⇒ h[i] < h[j]` on every pair).

**D. The atlas numbers, my own code end to end.**

```
  brick d=2: 65 events, |D|>=2 at 50 = 0.7692, max|D| = 3, 96 pairs, mean omega = 0.6510
  brick d=3: 65 events, |D|>=2 at 48 = 0.7385, max|D| = 4, 92 pairs, mean omega = 0.7120
  grid  d=2: 46 events, 23 = 0.500, max|D| = 3, mean omega 0.39
  grid  d=3: 46 events, 28 = 0.609, max|D| = 3, mean omega 0.48
```

Exact agreement with the receipt at every entry.

**E. The mint-and-spread prefix DEFLATES the headline — it does not inflate
it.** The brief's question, answered directly by computing the metrics on
the circuit-only suffix (the non-lattice prefix removed from the metric
population, the poset left whole):

```
  brick FULL (65 events)              d=2: homog 0.769  omega 0.651
  brick CIRCUIT-ONLY suffix (56 ev)   d=2: homog 0.786  omega 0.642
  brick PREFIX-ONLY (9 events)        d=2: homog 0.667  omega 0.750
```

The circuit alone reads **0.786**, *higher* than the published 0.769. The
non-lattice prefix costs the unit 1.7 points of homogeneity. No inflation.

**F. The residual shortfall is entirely boundary.** Dropping the bottom two
and top three height layers:

```
  brick INTERIOR (51 of 65 events) d=2: homog 0.902  |D|>=3 0.745  omega 0.650
  brick INTERIOR                   d=3: homog 0.922  |D|>=3 0.824  omega 0.709
```

**G. Size effects cut *against* the brick, and it clears anyway.** The
brief asked whether comparing a 65-event record to 120-event sprinklings is
fair. Sprinkling homogeneity is nearly size-independent, while the brick's
is strongly size-dependent (MAJOR 2), so the smaller record is the
handicapped one. Size-matched at N = 65:

```
  M21 N=65 box=30/40/60/90 : homog 0.662 / 0.677 / 0.662 / 0.646
  M31 N=65 box=20/24/40/48 : homog 0.662 / 0.708 / 0.523 / 0.754
  brick, 65 events         : homog 0.769
```

The brick still clears at matched size. The comparison is fair, and the
direction of the size effect favours the unit's conclusion.

**H. `|D| >= 2` is not trivially satisfied on a lattice** — the brief's
suspicion, tested and dismissed. The generic 2-actor walk (30 events, same
layer, same instrument) scores **0.067**; a pure chain scores 0; the
engineered courier records score 0.357–0.386. The metric discriminates
strongly among grammar records. What it *does* hide is the ceiling — see
MAJOR 3.

**I. Both crystals are admissible with no refusal**, and the actor and
event accounting checks out: brick `1 + 1 + 7 + 14×4 = 65`; grid
`1 + 1 + 8 + 12×3 = 46`.

**J. C3's ordering conclusion is robust to every correction in this
review.** Brick 0.769 > engineered ceiling 0.386 by a wide margin under
exact Fractions, and the grid's 0.500 likewise. The gate's *predicate*
(both crystals above the engineered ceiling) is the falsifiable part and it
is genuinely falsifiable — the grid at `R`-equivalent small sizes would
fail it.

**K. Provenance and LOG fidelity.** `0056d59` (LOG #447 + pin, **no code**)
→ `d5b8e72` (receipt + `.out` + LOG #448 + book patch). Every number in
LOG #448 matches actual output: 8 actors, 65 events, 14 rounds, 46 events,
9 actors, 12 phases, `7 PASS`, `max|D| = 3` for both. The scope paragraph
carries the grammar layer, the D59 missing-map transfer, the no-typicality
and no-object clauses (#440) — all four, and correctly. The self-correction
disclosed in LOG #448 ("C3's conjunct verdict hid that the brick ALONE
clears the floor; restated per-record") is exactly the right instinct and
is not counted against the unit.

---
---

## APPENDIX — repairs that must be made jointly

1. **`latt4`.** Replace the generator (non-power-of-two box at minimum;
   preferably draw from the high bits, which do not carry the LCG's
   low-bit periodicity). Then: rebuild D58's M^{3+1} control and every
   number derived from it; re-check D55c's `(120, 32, 8)` record;
   re-base D60's comparators.
2. **D53's SC5.** The empty-trace clause must come out of the *necessary*
   condition (it belongs to the `k = |dirs|` special case). Every consumer
   — `d54`, `d54b` K6, D55, `d55c` — must re-run with the corrected gate,
   and SKY-A/SKY-C must return to the field of view.
3. **D50's linearization.** Fix the `'bis'`/`'stat'` product rule; restate
   10/28/107 as 12/32/125; forward-correct D49/B2's 119 to 137 wherever it
   is quoted.
4. **D58's overlap.** Either restrict `ω` to unit-height-gap cover pairs
   and say so, or report the gap census alongside; and restate the
   "identity transition on the intersection" framing in light of the
   containment theorem.
5. **The book.** D51's three defective sentences are already in
   `THE-THEORY-SO-FAR.md` §B3.2/§B10.3, D53's is in §B5.4 under `[EXACT]`,
   and D55c's reframe is in the late-arrivals chapter and is cited by LOG
   #436's standing redirect. Repairs must land there in the same commit.

**None of the seven units is citable until its repairs land and a delta
records them.**

---

# DELTA — repairs verified, 2026-07-26

All seven units repaired by the repair pass and rerun green: D53
8 PASS, D55c 10 PASS, D58 8 PASS, D60 10 PASS, D57 8 PASS, D50
13 PASS, D51 12 PASS — all exit 0.  The coordinator independently
re-verified the load-bearing reversal with code sharing nothing with
the receipts: SKY-A shatter-4 at N = 300, box = 40 — **M³⁺¹: 17
events, M²⁺¹: 0**.  The discriminator is confirmed.

Corrected headlines now on the record (details in each receipt's
banner and result note): D53 — the true disjoint-row lemma, SKY-A/C
live, residue 2 REOPENED; D55c — the zero was a density artefact
through a SKY-B blinder, shatter-4 IS a two-sided-control dimension
discriminator; D58 — ω is a chart-size ratio, the overlap finding
closes with the SIGN FLIPPED, the homogeneity gap survives; D60 —
tiles at sprinkling-grade homogeneity (inside the band) with THIN
charts, d = 2 scope; D57 — ground (1) withdrawn, the verdict rests
on ground (2) alone, which the trivial-boundary control STRENGTHENS
(the counts are lower bounds); D50 — dimensions 12/32/125, the
negative now CONSTRUCTIVE, corpus-wide 119 → 137; D51 — the
projections REFINE sigma, (H1) not reduced in the claimed direction,
durable content = three refutations.  D61's closure of (H1) goes
through sigma directly and is untouched by D51's inversion.

Residual assignments, tracked: the LOG forward-corrections land at
#453; the book corrections land in the queued integration pass; the
stale SC5 consumers (d54 census line, d54b K6, d55 G5 label, d47b
TG3/TG4) are a named follow-up relabelling task — their gated records
carry the empty trace so no verdict changes, the damage is labels.
Two [REFEREE-CARRIED] numbers remain so-tagged.  **TERMINAL for the
batch round.**
