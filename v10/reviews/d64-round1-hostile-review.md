# D64 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D64 "the cocycle" — `note-d64-cocycle-pin.md`
(STRICT, committed at 7d65a3d, before the receipt), `note-d64-cocycle-result.md`
(GREEN-UNREVIEWED), `code/d64_cocycle_exact.py` + `data/d64_cocycle_exact.out`
(12 PASS / 0 FAIL, exit 0), LOG #464.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`indep.py` / `run1.py` … `run14.py`, scratch under
`/private/tmp/claude-501/.../scratchpad/d64rev/`): my own record builder
re-typed from the committed blueprints, my own immediate-predecessor relation
`P`, my own memoised-DFS transitive closure, my own longest-chain heights, my
own SKY-B, my own covers, my own port conventions and wire words, my own
fibre-map/classification/cocycle/closure code, my own sprinkling generator and
Minkowski order. The only object I share with the unit is the layer under test
(`d42b1`'s `candidates_for` / `admissible` / `regs_of` / `vname` / `V0`).
Calibration: `reviews/d63-round1-hostile-review.md` and
`reviews/d62-round1-hostile-review.md`.

**VERDICT: REVISE. 1 BLOCKER / 5 MAJOR / 7 MINOR / 4 NIT.**

**The arithmetic is completely sound.** Every figure in every table of the note
and the receipt reproduces exactly from my own driver: the anchor
(177 events, `47/59`, `1/3`, `max 4`, `ω = 100/137`; `d = 3` `137/177`,
`119/177`), the brick (`10/13`, `125/192`, `0`, `3`), the P-edge/cover counts
(335/328/7, 119/116/3, 175/168/7), 141 charts, 59 wide, 172 pairs, 137
wide–wide, 111 triples, the **57 / 115** split, the **29 / 108** wide split,
the `d = 3` rows, REGA's 85/87, all four control rows and both sprinklings
(247/3/244, 383/1/382, 370/4/366, 518/2/516) with **zero cocycle violations
anywhere**, including my own independent sprinkling rebuild. The receipt
reruns 12 PASS / 0 FAIL, exit 0, byte-identical to the committed `.out` apart
from six timing figures. PROBE 2's refusal to read the outcome at RAW is
correct and is to the unit's credit.

**The BLOCKER is a computation the unit did not run.** A structure group has
content only if its transition cocycle is *not* a coboundary. This one **is**.
There is an explicit per-chart relabelling after which **every** length-
preserving transition on the wide crystal becomes the identity. The atlas is
globally trivializable; `H¹ = 0`. The pin's G3 *letter* fired, but the
sentence attached to G3 — "the atlas carries a genuine structure group", "the
tensor programme has its object" — does not follow from what was measured.

**The five MAJORs are all about what the census means.** The group *name* is
not determined by the data (every non-identity transition is equally a
restriction of a 4-cycle); the 57/115 split is exactly the duplicate-chart /
proper-overlap split; the τ-vs-σ separation survives at one of the three
conventions the unit itself ran and dies under a fourth I built; the τ/σ
comparison is confounded by chart width and rests on 41 control pairs whose
overlap graph is a perfect matching; and the parity finding is a fact about
which pairs exist, not about transitions.

---

## BLOCKER 1 — the Z/2 transition cochain is a COBOUNDARY: the atlas IS globally trivializable, and "carries a G-structure" is not what was measured

**Where.** Note title ("**G3. THE ATLAS CARRIES A G-STRUCTURE — Z/2**"), §1
("the group generated is Z/2 = ⟨τ⟩"), §4 THE LICENSED CLAIM, §4's closing
paragraph ("It is a genuine structure group and it is the object the tensor
programme asked for"), §7 residue 7 ("The tensor/curvature programme now has
*an* object"), receipt C4 and the VERDICT gate, LOG #464.

**Defect.** The unit computes (i) that transitions are not all identity, (ii)
that the triangle cocycle holds, and (iii) that the partial maps close under
composition inside {restrictions of id, τ}. None of those distinguishes a
non-trivial Z/2 bundle from a trivial one. The decisive question — is the
Z/2-valued 1-cochain `g` a **coboundary**, i.e. is there a 0-cochain
`ε: charts → Z/2` with `g_ac = ε_a + ε_c`? — is never asked. If it is, the
"structure group" is pure gauge: a per-chart choice of which of the base
delivery's two wires is "port 0" removes every non-identity transition, the
holonomy of every loop in the nerve is trivial, and a curvature/connection
programme built on it starts at zero. Note that the unit already has half of
this in hand without noticing: its own alternative port order that swaps
`(sender, receiver)` globally is the *constant* ε, and it is precisely because
constants are coboundaries that a global swap cannot move the split. Nobody
asked what a non-constant ε does.

**Recomputation (mine).** Assign `g = 0` to the 30 identity-classified pairs
and `g = 1` to the 108 τ-classified pairs (the 138 length-preserving pairs;
the 7 length-changing and the 27 no-correspondence pairs carry no Z/2 value).
Propagate ε over the overlap graph by DFS and look for a contradiction:

```
  substrate DR(8,10,8), REG, d = 2:
     60 charts carry a labelled overlap, 138 labelled overlaps, 9 components
     COBOUNDARY inconsistencies found: 0        <-- g = delta(eps) EXACTLY
     eps distribution: 32 charts at 0, 28 charts at 1

  VERIFICATION by re-running the census with the relabelling applied
  (flip the first ROLE letter in the 28 charts with eps = 1):
     non-identity transitions among the 138 length-preserving pairs: 0
     all 172 pairs, (old class -> identity now?):
        tau x108 -> identity      identity x30 -> identity
        AMBIG x27 -> identity     length-changing x7 -> still non-identity
     => 165 of 172 pairs identity; the only survivors are the 7
        length-changing pairs, which are not fibre maps at all.

  And it is not a REG artefact:  DR(8,10,8) REGA d = 2 -> 0 inconsistencies
  as well; BRICK(8,14) and DR(8,10,0) trivially so (see MAJOR 4).
```

Also checked, and it makes the same point from the other side: the Z/2 lift of
the transitions satisfies the genuine Čech condition `g_ik = g_ij + g_jk` on
**108 triples with 0 violations** — a strictly stronger and cleaner test than
the receipt's partial-map form, and exactly the condition that (together with
the graph's cycle structure) makes the class trivial.

**What must change.** The measured cell is *"transitions not all identity, the
cocycle clean, and the class cohomologically trivial"* — which the pin's
trichotomy does not contain: G1's predicate is "all transitions are identity"
but G1's *sentence* is "the atlas is globally trivializable at this labeling",
and it is G1's sentence that is true. The unit must compute and report
`H¹ = 0`, state the explicit ε, and restate the licensed claim to something
like *"the atlas's transitions at this labeling are the coboundary of a
per-chart port choice; the Z/2 class is trivial, so the atlas is globally
trivializable and no non-trivial structure group is exhibited"*. §4's "it is
the object the tensor programme asked for" and §7 residue 7 must go or invert:
the successor question is not "is Z/2 enough" but "can any substrate carry a
transition class that is **not** a coboundary".

---

## MAJOR 1 — the group NAME is not determined by the data: every non-identity transition is equally a restriction of a 4-cycle, and ⟨τ⟩ is not the unique minimal consistent subgroup

**Where.** Note §1 ("**The group generated is Z/2 = ⟨τ⟩**, a fixed-point-free
involution of the 4-point wire fibre `{0,1}²`, i.e. the double transposition
`(00 10)(01 11)` in S₄"); §4 limit 1 ("⟨τ⟩ is **the smallest group containing
them**"); receipt C4's gate text; LOG #464.

**Defect.** No transition is a total permutation, so "the group" is chosen by
extending 2-point partial bijections to elements of S₄ — and the extension is
not unique. `⟨τ⟩` is the smallest by *order*, but it is **not** the unique
minimal by *inclusion*: there is a second, incomparable subgroup consistent
with every observed length-preserving map, and it is not a Z/2.

**Recomputation (mine).** Exhaustive: all 30 subgroups of S₄ reachable as
closures of ≤ 2 generators (which is all of them), tested against every
distinct length-preserving map observed on the substrate.

```
  the SIX distinct maps on DR(8,10,8), REG, d = 2 (145 of 172 pairs):
   [tau            ] x 55   {10->00, 11->01}   extensions in S4:
                              (00 10)(01 11)  and  (00 11 01 10)   <- a 4-CYCLE
   [tau            ] x 53   {00->10, 01->11}   extensions in S4:
                              (00 10)(01 11)  and  (00 10 01 11)   <- its inverse
   [identity       ] x 29   total, all 4 points          extensions: e only
   [identity       ] x  1   {00->00, 01->01}   extensions: e  and  (10 11)
   [length-changing] x  5 / x 2                extensions: none (not permutations)

  UNIQUELY-tau transitions: 0 of 108.  Every one is equally a restriction
  of an order-4 element.

  subgroups of S4 consistent with EVERY length-preserving map: 10
  MINIMAL BY INCLUSION: 2, and they are incomparable —
       { e, (00 10)(01 11) }                                  = Z/2 = <tau>
       { e, (00 01)(10 11), (00 10 01 11), (00 11 01 10) }     = Z/4
  Z/4 COCYCLE with the c-lift (tau-maps -> c and c^-1): 108 triples
  tested, 0 VIOLATIONS.  The cocycle does not discriminate either.
```

So "the group generated is Z/2" is a minimality convention, not a measurement,
and the Z/4 reading passes every test the unit runs. Note the asymmetry
against the unit's interest: on the two grammar **controls** `⟨σ⟩` *is* the
unique minimal-by-inclusion consistent subgroup (I checked), so the σ naming is
better founded than the τ naming that carries the headline. The honest form is
"every length-preserving transition is a restriction of an element of ⟨τ⟩ —
and equally of ⟨(00 10 01 11)⟩ ≅ Z/4; the data do not name the group", and
"fixed-point-free involution of the 4-point fibre" must lose its definite
article.

---

## MAJOR 2 — the 57/115 split is exactly the "same chart / proper overlap" split, and the unit's unique-identity-fraction finding is about chart DUPLICATION

**Where.** Note §1 and §2 (the 57/115 and 29/108 headline), §3 finding (a)
("what the wide crystal alone has is (i) a substantial **identity** fraction —
57 of 172 pairs, **the only substrate in this census with a trivializable
part**"), receipt C5, LOG #464.

**Defect.** The identity/non-identity dichotomy is, on this substrate at
`d = 2`, a perfect biconditional with a property of the *charts* that has
nothing to do with labels: two charts carry the identity transition **iff they
have the identical direction set**. The controls have no such pairs at all,
which is the whole of their "0 identity". So finding (a) says: the wide
crystal is the only substrate in the census that has distinct base events
sharing a whole `d = 2` chart. That is a statement about chart duplication, not
about trivializability.

**Recomputation (mine).** Cross-tabulating "`D_a == D_c`?" against "transition
is identity?" over every overlapping pair:

```
  DR(8,10,8) d=2:  (D_a==D_c, identity) -> {(True,True): 57, (False,False): 115}
                    ... an exact biconditional, both ways, 172/172.
  BRICK(8,14) d=2:  {(False,False): 58}     <- zero pairs with D_a == D_c
  DR(8,10,0)  d=2:  {(False,False): 68}     <- zero pairs with D_a == D_c

  And it is NOT a theorem, which is the second half of the problem:
  DR(8,10,8) d=3:  {(True,True): 54, (True,False): 1, (False,False): 218}
  BRICK(8,14) d=3: {(True,False): 52, (False,False): 4}   <- 52 pairs with
                    IDENTICAL direction sets and NON-identity transitions.

  Refinement of the same fact: the 29 total (4-point) identity maps are
  exactly the 29 wide-wide pairs with D_a == D_c; every one of the 59 wide
  charts carries the SAME label signature {00,01,10,11}, one word per
  direction, and there are only 30 distinct direction sets among them.
```

So on this substrate every chart-pair that overlaps *completely* transitions by
the identity, and every chart-pair that overlaps *partially* does not. The
unit should report the biconditional (it is striking and it is free), should
stop describing the 57 as "a trivializable part" of the atlas, and should
restate finding (a) as the duplication fact it is.

---

## MAJOR 3 — the τ/σ separation holds at exactly ONE of the three conventions the unit itself ran, and dissolves entirely under a fourth that its stated canonicity argument does not exclude

**Where.** Note **title** ("and the coupling changed WHICH involution it is"),
§3 finding (b), §4 limit 5, §7 residue 6, receipt C4/C5 gate text, LOG #464
("brick and uncoupled ring carry the OTHER involution sigma … IT CHANGED WHICH
INVOLUTION THE ATLAS CARRIES").

**Defect (a) — one of three, from the unit's own output.** The receipt runs
three instruments. Finding (b) is true at REG and false at both others, and the
note reports only half of that:

```
  substrate DR(8,10,8) d=2        controls (BRICK / DR(8,10,0)) d=2
  REG   {id 30, tau 108, lc 7}    {sigma 19} / {sigma 22}      <- finding (b)
  REGA  {id 58, tau  80, lc 7}    {other 14, sigma 5} / {other 16, sigma 6}
  COV   {id 58, tau  80, lc 7}    {other 19}          / {other 22}
```

Under REGA *and* under COV the controls carry **no nameable group at all**
(the 'other' class is non-empty), while the substrate keeps ⟨τ⟩ at all three.
§4 limit 5 mentions REGA dissolving the controls' σ; it does not mention that
COV — the unit's own register-free surrogate, the instrument it uses to make
the sprinkling and grammar columns commensurable — does the same. The note's
**title** and LOG #464 state (b) flatly.

**Defect (b) — the canonicity argument does not select the convention it
claims to.** The unit's argument is that the port order is "the layer's own
delivery tuple order `(sender, receiver)` … *because it is the layer's own*"
(§4 limit 5; receipt's ROLE docstring adds "it is defined chart-locally").
That argument fixes the *order within an event's register tuple*. It does not
fix **which endpoint of the P-edge the port index is read at**. Reading the
index at the event the step *enters* — "the wire I arrive on" — is exactly as
much "the layer's own tuple order", and gives a different world.

**Recomputation (mine) — my own fourth convention, IN (port index at the
TARGET event of each P-edge; everything else identical to ROLE):**

```
  DR(8,10,8) d=2   ROLE(=OUT): 57/115   maps {id 30, tau 108, lc 7}
                          IN:  0/172    maps {tau 30, SIGMA 54, OTHER 54, lc 7}
                         INA:  0/172    maps {tau 30, sigma 54, other 54, lc 7}
  BRICK(8,14) d=2  OUT: {sigma 19}      IN: {sigma 19}   (controls unchanged)
  DR(8,10,0)  d=2  OUT: {sigma 22}      IN: {sigma 22}

  minimal consistent subgroups under IN on the substrate: the Klein
  four-group {e,(00 01)(10 11),(00 10)(01 11),(00 11)(01 10)} and two
  others — no Z/2, and the 'other' class is NON-EMPTY, so the receipt's
  own C4 predicate (`len(badmaps) == 0`) would FAIL and no group could
  be named.  The substrate now carries sigma on 54 pairs: the
  substrate/control involution separation is GONE.
```

**In fairness to the unit, and stated because it matters:** IN is arguably
excludable, but by an argument the unit does not make. Under IN, for any
shared direction the two charts' words must differ — if the two paths pass
through the same intermediate event the first letters are ports of *distinct*
registers of that event, and if they pass through different intermediate
events the last letters are ports of distinct registers of the shared
direction. So IN *forces* non-identity, which is the same disease PROBE 2
convicts RAW of. But: (i) the receipt's PROBE 2 as implemented measures
`|regs(e) ∩ regs(e')|`, a **convention-independent** quantity, and its
argument is hand-written for RAW's first letter — it cannot detect this class
at all; (ii) the operational signature of a forced labeling, 0 identity at
100% of pairs, is exactly what the two grammar **controls** show at the
canonical ROLE labeling (0/58 and 0/68), and the receipt reads findings (a)
and (b) off them without ever asking whether *their* zero is forced — MAJOR 2
supplies a candidate mechanism (they have no `D_a == D_c` pairs). The unit
needs a *general* forcedness test, not a RAW-specific one, and it needs to
apply it to the controls.

---

## MAJOR 4 — the τ-vs-σ comparison is not matched: it compares the substrate's WIDE pairs against the controls' NARROW pairs, and the controls' σ rests on 41 pairs whose overlap graph is a perfect matching

**Where.** Note §3 finding (b) ("every length-preserving transition of the
uncoupled brick and of the uncoupled double ring is a restriction of **σ** …
So the coupling did not create a transition structure — **it changed which
involution the atlas carries**"), receipt C4/C5.

**Defect.** Three separate confounds, none reported.

**Recomputation (mine).**

```
  (i) WIDTH.  On the substrate, EVERY tau pair is a (4,4) wide-wide pair:
        tau           x108 : chart widths (4,4) x108
        identity      x 29 : (4,4) x29        + x1 at (2,2)
        no-correspond x 27 : (2,2) x27
        length-chang. x  7 : (2,4) x7
      The controls have NO wide charts at d = 2 at all, so their 19/22
      sigma pairs are narrow.  The comparison "substrate carries tau,
      controls carry sigma" is tau-on-(4,4) against sigma-on-narrow.
      At d = 3, where the controls DO have wide pairs (brick 52 of 56),
      the classification has no content: 1 of 61 and 1 of 56 pairs carry
      any single-valued map at all, and it is length-changing.  So NO
      matched comparison exists anywhere in the census.

  (ii) COVERAGE, never stated in the note.  Single-valued transitions:
        BRICK(8,14) d=2: 19 of 58 pairs (33%); the other 39 are
                          'card-mismatch', not 'ambiguous'
        DR(8,10,0)  d=2: 22 of 68 pairs (32%); the other 46 card-mismatch
      §3(b)'s universal "EVERY length-preserving transition of the
      controls" is a statement about 41 pairs out of 126.

  (iii) NO COMPOSITION.  The sigma-labelled overlap graph on both
      controls is a PERFECT MATCHING:
        BRICK(8,14): 38 charts, 19 edges, 19 components, all of size 2
        DR(8,10,0):  44 charts, 22 edges, 22 components, all of size 2
      No two sigma-overlaps share a chart.  There is nothing to compose,
      no triple, no cocycle and no closure content behind "the controls
      carry <sigma>"; it is 41 isolated 2-point partial bijections.
      (The substrate, by contrast, has 138 overlaps over 60 charts in 9
      components — genuine connectivity, which is what makes BLOCKER 1's
      coboundary question meaningful there and vacuous here.)
```

The sentence "the coupling changed which involution the atlas carries" is
therefore carrying three unstated confounds and one convention (MAJOR 3). At
minimum it needs the width qualifier, the coverage fractions and the
matching-graph fact beside it.

---

## MAJOR 5 — the parity "confirmation" is a fact about which pairs exist, and the coupled-wire lean is UNTESTED, not "refuted and inverted"

**Where.** Note §3 finding (c) both halves; receipt's "THE PIN'S LEAN, CHECKED
EXPLICITLY" gate; LOG #464 ("parity CONFIRMED … coupled-wires REFUTED AND
INVERTED").

**Defect.** The even height layers contain almost no transitions to be
non-identity. All 27 even-layer pairs that matter are the both-coupled pairs,
and they are **exactly** the 27 pairs the unit elsewhere reports as carrying no
single-valued correspondence at all — a coincidence of sets the note never
discloses, while presenting the same 27 pairs once as a refutation ("27 of 27
are IDENTITY") and once as a limitation ("27 of 172 carry no single-valued
correspondence"). At the fibre-map level the pin's lean is not refuted at the
coupled wires; it is **untested there**, because at exactly those pairs no
word-level correspondence exists.

**Recomputation (mine).**

```
  EVEN-layer pairs: 28 total
      classes: {no-correspondence: 27, identity: 1}
      coupled-base counts: {2: 27, 0: 1}      <- the 27 ARE the both-coupled
      wide-wide: 0 of 28
  ODD-layer pairs: 144 total
      classes: {tau: 108, identity: 29, length-changing: 7}
      wide-wide: 137 of 144       <- ALL 137 wide-wide pairs are odd

  per-layer h: id/non-id  (mine, reproduces the note exactly)
    17: 0/1  18: 1/0  19: 2/6  20: 1/0  21: 3/12  22: 2/0
    23: 4/16 24: 4/0  25: 4/16 26: 4/0 ... 33: 4/16 34: 4/0
  per-layer #both-coupled pairs: 20:1 22:2 24:4 26:4 28:4 30:4 32:4 34:4  (=27)
  per-layer #wide-wide pairs:    19:6 21:11 23:20 25:20 ... 33:20         (=137)
```

So "every non-identity pair sits at odd height" is equivalent to "the inter-ring
deliveries land in the even layers and the ring deliveries' wide charts in the
odd ones" — a placement fact about the blueprint, established before any
labeling is chosen. The alternating `4/16` vs `4/0` census is the alternation of
the *pair population*, not of the transitions. The "4 identity" in every even
row is 4 no-correspondence pairs. Finding (c) must say which of its two halves
is a labeling fact (neither) and must disclose the 27-pair identity.

---

## MINOR 1 — the set-level cocycle column is a dead test

Receipt C3, lines 688–692:
`if all(label(Wd[k][f], 'ROLE') == label(Wd[k][f], 'ROLE') for f in T)`.
That is an expression compared with itself; `setok` is the triple count and
`setviol` is 0 by construction, in every cell, printed as a measured column
`(set-level: ok/violations)`. Note §5 says "the receipt **computes** it and
reports it as a tautology" — it does not compute it. The *intended* test would
also be vacuous (the note's argument for that is correct), so nothing turns on
it, but a printed column that is `x == x` is exactly the class D63's round
called out.

## MINOR 2 — the 111 testable triples exercise exactly one group relation, on 2 fibre points each

My instrumentation of the receipt's own cocycle loop:

```
  111 triples, all tested (undef 0), fibre points tested per triple: {2: 111}
  total fibre points tested across the whole substrate cocycle test: 222
  class multiset of the three maps in each tested triple:
      (identity, tau, tau)                     x 108
      (identity, length-changing, length-ch.)  x   3
  triples involving at least one tau: 108 of 111
  every triple intersection has size exactly 2; all 111 lie in odd layers
  pairs occurring in some triple: 143 of 172 (the 27 no-correspondence
      pairs occur in NONE, so no triple is undefined for that reason)
```

**To the unit's credit, the answer to the obvious suspicion is no**: the
testable set does *not* avoid the non-identity transitions — 108 of 111 involve
a τ. But the test has one shape only: it verifies `τ ∘ τ = id` (as `0 + 1 = 1`)
108 times and nothing else. There is no `(id, id, id)` triple and no
`(τ, τ, τ)` triple. "All 111 testable triples cocycle-clean" should say what
relation was exercised and on how many fibre points. Separately: 3 of the 111
are triples of **length-changing** maps, which C4 excludes from the group "by
name" — the cocycle's scope and the group's scope differ, and that is unstated.

## MINOR 3 — control coverage is absent from the note's finding (b)

The note gives the pairs and the ROLE split for every control but never the
fraction carrying a transition map at all: 19/58 and 22/68 at `d = 2`, and
1/61 and 1/56 at `d = 3` (both length-changing). Every universal quantifier in
§3(b) ranges over those 41 pairs. §4 limit 4 discloses that the *cocycle* is
untested on the controls; the *classification*'s coverage gets no equivalent
sentence.

## MINOR 4 — vacuous halves inside the C4 predicate are counted as evidence

`_ctl_sigma = all(g[1][1] for g in _ctlG.values())` ranges over both depths.
At `d = 3` both grammar controls have **zero** length-preserving maps, so
`eq_sig` and `eq_pure` are both `all(...)` over an empty set — `True`
vacuously, and the printed line says "inside `<tau>` = True, inside `<sigma>` =
True" for a cell with nothing in it. The substrate's own `d = 3` line has the
same shape (2 identity maps, both flags True). D63's round asked for gates
labelled for what they measure; a vacuous True should be printed as vacuous.

## MINOR 5 — §7 residue 4 is self-contradictory and understates its own negative

Residue 4: "No overlap exhibits a total fibre permutation … Whether a substrate
exists whose wide–wide overlaps share **all four** directions — which would
force a total permutation and turn 'restriction of ⟨τ⟩' into 'element of ⟨τ⟩'
— is open and sharp." This substrate **has** 29 wide–wide overlaps sharing all
four directions (MAJOR 2), and every one of them forces the **identity**. The
sharp open question is a total *non-identity* transition, and the measured fact
here is the negative answer for this substrate: full overlap ⟹ identity. The
residue should be restated as the finding it already is.

## MINOR 6 — the headline 115 and the group's 108 are different populations

The 115 non-identity pairs include the 7 length-changing pairs that §4 limit 2
excludes from the group by name. The group-relevant non-identity count is 108.
The licensed-claim box puts "115 of 172" and "the length-preserving ones close
to Z/2" in one sentence without saying that the two counts differ. Separately,
the one 2-point "identity" map (`{00→00, 01→01}`) is equally a restriction of
the transposition `(10 11)`, so even the identity class is not uniquely named
at every pair.

## MINOR 7 — the determinism gate covers the substrate only; `reg_tuple`'s tie-break differs from `regs_of`'s

The probe digest is `MEAS[('DR(8,10,8)','REG',2)]` and `…,3)]` — the substrate's
REG cells. Finding (b), which lives entirely on the two grammar controls, is
not under the gate, and the layer does read `next(iter(frozenset))` in
load-bearing places: `regs_of` for an `'r'` event takes
`base = next(iter(op[2]))[1]`, while the receipt's `reg_tuple` takes
`sorted(op[2], key=repr)[0][1]` — a *different* tie-break, harmless here only
because every arbitration in these records has a single proposer (C0b would
catch a divergence, so this is a coverage note, not a bug). I verified
externally that my full substrate+control map census is byte-stable under
`PYTHONHASHSEED` 0 / 7 / 999 / 12345.

## NIT 1 — the printed exit line and the code disagree

The final line prints "exit 1 ONLY on **C0** anchor breakage" while C0a and C0b
also carry `anchor=True`; note §5 says "C0/C0a/C0b". Pin C6 says C0 only. One
of the three should move.

## NIT 2 — AST anti-vacuity is the weak form

`_vac` flags only `isinstance(c.args[1], ast.Constant)`; d47a's SG8 also
requires each predicate to reference a run-bound name. Same class as D63 NIT 3;
the scope caveat is carried elsewhere, so this is a note.

## NIT 3 — the exit-freedom scan is D63's, with D63's narrowness

`_no_exit` is carried verbatim, so it still misses e.g. an aliased exit, and
the slice check is the textual `'sys.exit' not in _slice`. Clean here, and
`_ext` keeps only defs/classes, so nothing module-level can fire; the gate is
just weaker than its label.

## NIT 4 — the C4 gate requires a nuisance to be present

`_grp_ok` includes `_sub2['kinds'].get('length-changing', 0) > 0`, so the gate
would **fail** on a substrate with no height-skipping P-edges — i.e. on a
cleaner substrate. It should test the classification, not the presence of the
artefact being excluded.

---

## Checked and CLEAN (D64)

Everything below is my own recomputation unless stated.

**A. Receipt rerun.** `12 PASS / 0 FAIL`, exit 0, 59.8 s and 60.9 s on two
runs. Output identical to the committed `.out` apart from six timing figures
(three per-cell costs, the build time, the total, the determinism-probe time).
No FAIL line anywhere.

**B. The substrates, rebuilt from the blueprints with my own driver.** My own
`Rec`/`pick`/`mint_and_spread`/`dl`/`brick`/`double_ring`, my own `P`, my own
memoised-DFS closure, my own longest-chain heights, my own SKY-B. All three
grammar substrates: **no refusal**, and **every menu pick had exactly one hit**
(min = max = 1 over all 177 / 65 / 97 steps). My closure of `P` **equals**
`d42b1`'s `event_poset` on all three. P-edge / cover / height-skipping counts:
`335 / 328 / 7`, `119 / 116 / 3`, `175 / 168 / 7` — the receipt's C0b row
exactly.

**C. The anchor.** `DR(8,10,8)`: 177 events, `d = 2` homogeneity `47/59`
(0.7966), `|D| ≥ 4` at `1/3`, `max |D| = 4`, mean ω `100/137` (0.7299);
`d = 3` `137/177` and `119/177`, `max |D| = 4`. `BRICK(8,14)`: `10/13`,
`125/192`, `0`, `3`. Every figure of D63's committed row and D60's, from my own
instrument. `DR(8,10,0)`: 97 events, `67/97`, `0`, `3` at `d = 2`.

**D. The chart and pair census.** 141 charts / 59 wide / 172 pairs / 137
wide–wide / 111 triples at `d = 2`; 137 / 119 / 273 / 263 at `d = 3`; brick
50/0/58 and 48/38/56; `DR(8,10,0)` 67/0/68 and 62/45/61. The P-path
enumeration reaches **exactly** SKY-B's `D_e(d)` at every event of every
substrate at both depths (`reach_ok = True` in all 18 grammar cells I ran).
Every overlapping pair is same-height (my pair enumeration over all chart
pairs, not just within layers, finds none crossing).

**E. Every number in note §2's tables.** RAW 0/172 and 0/273; **ROLE 57/115**
and wide **29/108**; `d = 3` ROLE 54/219 and 54/209; FIRST-raw 0/172; FIRST-role
57/115 at `d = 2` and 148/125 at `d = 3` (the "FIRST-role reproduces ROLE at
`d = 2` and not at `d = 3`" observation is correct); REGA 85/87 and 57/80.
Controls 0/58, 0/56, 0/68, 0/61. Sprinklings, from my own `latt`/`mink4`
rebuild: M²⁺¹ `d = 2` 247 pairs, 3/244, 153 wide; `d = 3` 383, 1/382, 279;
M³⁺¹ `d = 2` 370, 4/366, 217; `d = 3` 518, 2/516, 484. **Zero cocycle
violations in every one of those cells**, my own cocycle code.

**F. The map census and the closure.** 145 of 172 pairs carry a single-valued
transition; 6 distinct maps; pairs by class `{identity 30, tau 108,
length-changing 7}`; statuses `{ok 145, ambiguous 27}`. The four length-
preserving maps do close under composition-where-defined and every closure
element is a restriction of the identity or of τ — the receipt's C4 arithmetic
is right (what it *means* is BLOCKER 1 and MAJOR 1).

**G. The artifact probes.** PROBE 2: all 172 overlapping pairs have base events
with **disjoint** register sets — `{0: 172}` — in all six grammar cells; the
RAW tautology is real and the refusal to read the outcome there is correct and
is the best thing in the unit. PROBE 1: no blind cell; on the substrate, of
120 directions seen by ≥ 2 charts, ROLE's label is constant at 58 and
FIRST-role's at 62 — not blind, and the margin is honest. I also probed a
subtler tautology the note does not: the ROLE first letter is **not** a
function of the base event (only 4 of 141 charts, and 0 of 59 wide charts, use
a single port), and it is **not** determined by height parity (both parities
carry both letters), so the parity finding is not circular *through the
labeling* — it is circular through the pair population instead (MAJOR 5).

**H. Caps and cuts.** `CLOSURE_CAP = 3000` / `CLOSURE_OPS = 3000000` bind on
exactly the four sprinkling cells, which are printed and which name no group;
largest closure computed 1485. **No cap binds anywhere the result is read**:
the substrate's all-maps and length-preserving closures both complete (7 and 5
maps). 22 cells, 3,582 pairs, 5,769 triples, nothing truncated; the depths,
predicates (`|D| ≥ 2`, `|D| ≥ 4`, ≥ 2 shared directions, ≥ 1 triple direction)
and sprinkling parameters are all printed and all are D58's or the pin's. I
found no invented threshold anywhere in the receipt.

**I. Instrument hygiene.** The `d42b1` text slice cuts at its own banner and is
`sys.exit`-free; `_ext` keeps only defs/classes and named constants, so no
imported module-level statement can fire; the extracted-body counts printed in
C0a match the files (16/9/5/10/15 = 55). The substrate genuinely is D63's
function object by AST, not a re-typing — and my independent re-typing produces
the same 177 events.

**J. Provenance and pin discipline.** The pin is `STRICT`, 109 lines, committed
at `7d65a3d` **before** the receipt and the result note (`72bd3ac`). The
pre-registered trichotomy is the actual predicate of the verdict gate
(`VERDICT = 'G1' if nonid == 0 else ('G2' if viol > 0 else 'G3')`), so G1 and
G2 would have been reported by the same line. The pin's lean is reported as
landing split rather than quietly dropped (subject to MAJOR 5 on what "split"
means). Both the RAW and the REGA columns are printed beside the headline
rather than suppressed, and §4's five limits and §7's eight residues are
unusually forthcoming for a green-unreviewed note.

**K. Scope.** Pin §5 and note §6 carry every required clause — grammar layer,
the five swept substrates only, no measure (B1), no typicality, no
physical-object claim (#440), width ≤ 4 by W4b on every tensor sentence, D59
transfer disclaimed, D63's ends caveat noted and no band-membership sentence
made. The "Z/2 is a DISCRETE group" paragraph is the right instinct and
survives — but it is the wrong worry: the problem is not that the group is
small, it is that the class is trivial (BLOCKER 1). Subject to BLOCKER 1 and
MAJORs 1–4, no claim exceeds the swept census.

**L. Determinism.** My own full census (substrate **and** controls, all
conventions, maps and classifications) is byte-stable under `PYTHONHASHSEED`
0 / 7 / 999 / 12345. The receipt's own gate passes; MINOR 7 is about its
coverage, not its result.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-26)

**Verification of the BLOCKER.**  The coboundary computation is now
GATE C7 IN THE RECEIPT — the strongest verification available: the
receipt reproduces the referee's construction exactly (60 charts /
138 labelled overlaps / 9 components / 0 obstructions; eps = 32/28;
ALL 108 tau pairs become identity after the relabelling, 165/172
identity, only the 7 length-changing survive; Cech lift 108 triples
0 violations; REGA repeat 0 obstructions) — so the class IS a
coboundary and H1 = 0.  Had the referee been wrong, C7 would have
failed on rerun; it passed.

**Repairs applied (receipt 15 PASS / 0 FAIL; note retitled):**
1. BLOCKER: headline restated — "the transitions are non-trivial
   pair by pair, the cocycle is clean, and THE CLASS IS A COBOUNDARY
   — H1 = 0"; G3's letter fired on the pin's predicate but G1's
   SENTENCE is the true one (the pin's trichotomy lacked the measured
   cell, credited); "the tensor programme has its object" withdrawn —
   it starts at ZERO on the delivery crystal; the successor question
   sharpened to "can ANY substrate carry a non-coboundary class",
   with the two-port-symmetry reason to attack the arbitration
   crystal (a reason, not a promise).
2. MAJOR 1: new C4b — the extension census (10 consistent subgroups,
   2 incomparable minimal: <tau> and a Z/4; 0/108 uniquely-tau; the
   Z/4 lift passes the same triples) — the group NAME is undetermined
   and the note says so.
3. MAJOR 2: new C4c — the 57/115 split is an exact biconditional
   with chart duplication (identical direction sets), 172/172.
4. MAJOR 3/4: the tau/sigma contrast demoted to a labelled
   REG-convention observation (dies at REGA and COV; width-confounded;
   the controls' sigma graphs are perfect matchings, so no group is
   GENERATED there — each control transition is a sigma-restriction,
   pairwise).
5. MAJOR 5: parity restated as pair-existence; the coupled-wire lean
   restated as UNTESTED (the 27 both-coupled pairs ARE the
   no-correspondence pairs — gated equal).
6. MINORs/NITs: dead set-level column removed; populations stated
   once correctly (115 = 108 tau + 7 length-changing); vacuous d = 3
   halves excluded from predicates; residue 4 inverted; determinism
   scope in its label; SG8 anti-vacuity + alias-catching exit scan
   adopted; exit-family stated.

**Verdict after repairs: the unit stands as an INSTRUMENT result and
a NEGATIVE finding** — a validated transition-detection instrument
(with the decisive triviality test it was missing), and the honest
statement that the delivery crystal's atlas is globally
trivializable.  TERMINAL for round 1.
