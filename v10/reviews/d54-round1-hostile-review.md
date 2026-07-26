# D54 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D54 "the Dilworth gate" — `note-d54-dilworth-gate-pin.md`
(§1–§7 + §8 amendment), `code/d54_dilworth_gate_exact.py` +
`data/d54_dilworth_gate_exact.out`, `code/d54b_shatter_construction_exact.py` +
`data/d54b_shatter_construction_exact.out`,
`note-d54-dilworth-gate-result.md`, LOG #427 / #428.
**Reviewer:** independent Opus 5 worker, no prior context, recompute-not-trust.
Every number below was produced by code I wrote for this review, run against
the committed layers from the repo root; scratch scripts under `/tmp/d54rev/`.

**VERDICT: REVISE. 1 BLOCKER / 2 MAJOR / 8 MINOR / 3 NIT.**

The mathematical core survives everything I threw at it: the theorem's
premise is not merely gated but *provable* from the layer, the proof's
chain-cover step is sound under two different attributions, and the
20-actor / 42-event construction reproduces exactly — 16 distinct traces,
all 16 subsets, shattered 4-set — under code that shares nothing with
`d47a` but the definition. The BLOCKER is not in the theorem; it is in the
sentence the unit sells the theorem with. **"A sphere-like sky (shattering at
every m) requires unboundedly many actors" has an antecedent that no 2-sphere
sky satisfies:** caps on `S²` have VC dimension 4 and can never shatter 5
points, which I certify below with an exact Radon partition on rational
sphere points. The infinite-clocks doctrine is therefore *not* derived by
this route. It is rescuable by a different (and cheaper) argument, which I
supply and check.

---

## BLOCKER 1 — the infinite-clocks headline is unsupported: no 2-sphere sky "shatters at every m"

**Where.** `note-d54-dilworth-gate-result.md` §1, the theorem's third
sentence ("**Shatter-4 requires at least 6 actors; a sphere-like sky
(shattering at every m) requires unboundedly many.**") and the paragraph
"What the theorem delivers for the programme" ("**A sky rich enough to be a
2-sphere requires unboundedly many actors, by Sperner's count applied to
actor sequentiality.**" / "the author's infinite-clocks doctrine … is no
longer a doctrine at this scope"). Same claim: pin §3 ("a sphere-like sky —
shattering at every k — requires unboundedly many actors"; "derives the
author's infinite-clocks doctrine as a THEOREM"), receipt
`d54_dilworth_gate_exact.py` gate **T-SPERNER** label ("a sphere-like sky
requires UNBOUNDEDLY MANY: the infinite-clocks doctrine as arithmetic"),
LOG #428 ("**A SPHERE-LIKE SKY NEEDS UNBOUNDEDLY MANY — the author's
infinite-clocks doctrine is now a THEOREM at gated scope**").

**The defect.** The implication *"shatters at every m ⇒ unboundedly many
actors"* is valid. But it is applied to a 2-sphere sky, and **a 2-sphere sky
does not shatter at every m — it shatters at most 4.** Caps on `S²` are
halfspace traces on points in convex position; halfspaces in `R³` have VC
dimension 4 (Radon). So the antecedent is satisfied by *no* cap system on
the sphere, the implication never fires on the object it is invoked for, and
the "unboundedly many actors" / "infinite clocks as a theorem" claim is
unsupported by the Dilworth gate.

This is exactly the sentence the corpus's own instrument was one line away
from catching: `d47a` defines `max_shattered(rows, cols, kmax=5)` and then
**never calls it** — its separator stops at "caps shatter 4" (SG0(c)) and
never asks whether caps shatter 5. A 5-point sphere configuration was never
built anywhere in the corpus.

**My recomputation** (`/tmp/d54rev/sphere.py`, exact `Fraction`s, five
rational points on the unit sphere via stereographic projection, all
verified `x²+y²+z²=1`):

```
5 exact rational points on S²: (0,0,1) (1,0,0) (0,1,0) (-1,0,0) (36/49,24/49,23/49)
affine dependence  lambda = [-23/49, -19/49, -24/49, 17/49, 1]
    sum(lambda) = 0        sum(lambda_i * p_i) = (0, 0, 0)
RADON PARTITION: conv{3,4} meets conv{0,1,2}
   => the subset {3,4} is NOT cut off by ANY halfspace
   => no 5 points of S^2 can be shattered by caps.  VC dim of caps = 4.

independent grid corroboration (all rational normals in [-3,3]^3, all
midpoint thresholds):  cap traces realized on these 5 points = 30 of 32
   5-set shattered?  False.   missing subset found: {3,4}  (= the Radon pair)
   max shattered k  = 4
```

Two independent certificates (an exact affine dependence, and a
constructive enumeration that finds 30/32 and misses precisely the
Radon-blocked complementary pair) agree: shattering stops at 4 on the
sphere.

**The repair, verified.** The conclusion the author wants is reachable — by
*trace counting* instead of Sperner, and it does not need shattering at all.
The nested-trace lemma gives: one actor's chain in `B_n` has at most `n+1`
elements, so `k` actors realize at most `k(n+1)` distinct traces. The number
of distinct halfspace-separable subsets of `n` points in general position in
`R^d` is exactly `2·Σ_{i≤d} C(n-1,i)` (I checked the `d=2` case against a
brute-force arc enumeration for `n = 4,5,6,7,8,12`: `14,22,32,44,58,134`,
exact agreement, and `d=3` at `n=4` gives 16 = `d47a`'s own tetrahedron
count). Hence:

```
   n | circle traces | sphere traces | forced actors (>= traces/(n+1))
     |    (d=2)      |    (d=3)      |   circle      sphere
   4 |      14       |      16       |     3            4
   6 |      32       |      52       |     5            8
  10 |      92       |     260       |     9           24
  16 |     242       |    1152       |    15           68
  32 |     994       |    9984       |    31          303
```

`Θ(n³)/(n+1) = Θ(n²) → ∞`. So "a continuum of directions needs unboundedly
many actors" **is** a consequence of the nested-trace lemma — via counting,
not via Sperner, and with no appeal to shattering. That is a stronger and
cheaper result than the one claimed, and it is not what the note, the
receipt label, or LOG #428 says. The claim as written must be withdrawn and
replaced; T-SPERNER's label must stop asserting the sphere consequence.

---

## MAJOR 1 — "width is the provable price of DIMENSION" is not what the theorem prices

**Where.** `note-d54-dilworth-gate-result.md` §1, last line of "What the
theorem delivers": "Width is not merely the observed scaling variable
(D47b); it is the *provable price* of dimension." Echoed in LOG #428
("Width is not just D47b's observed scaling variable; it is the provable
price of dimension").

**The defect.** The same theorem, applied to a **2+1 celestial circle**,
forces unboundedly many actors too. Nothing in the Dilworth gate is
dimension-sensitive except a constant. From the table above (recomputed as
in BLOCKER 1, and cross-checked against brute-force arc systems):

* circle with `n` directions: `n² − n + 2` traces, so actors
  `≥ (n²−n+2)/(n+1) ≈ n − 2` → **unbounded**;
* sphere with `n` directions: `Θ(n³)` traces, so actors `≥ Θ(n²)` →
  unbounded.

Both diverge. The genuinely dimension-specific content of the gate is only
the shatter offset: arcs shatter 3 ⇒ a circle sky needs `≥ C(3,1) = 3`
actors; caps shatter 4 ⇒ a sphere sky needs `≥ C(4,2) = 6` actors
(and, per BLOCKER 1, no more from this route, because neither shatters
higher). **3 versus 6.** That is the whole dimensional signal. Width is the
provable price of *sky size* (direction count, trace count); dimension buys
a factor, not the divergence. The sentence as written attributes the
divergence to dimension and is unsupported.

---

## MAJOR 2 — the "not realizable as a 2+1 celestial sky" arrow is broken by the corpus's own demotion, and D54 does not carry it

**Where.** `note-d54-dilworth-gate-result.md` §3 **MAY**: "the transport
layer admits a record whose SKY-B(5) sky is **not realizable as a 2+1
celestial sky** — arcs on a circle cannot shatter a 4-set (D47a SG0,
constructed, not cited). This is the first obstruction certificate against
2+1 in the corpus". Same in gate **K7**'s label and LOG #428.

**The defect.** The inference is `shatter-4 ⇒ not an arc system ⇒ not a 2+1
celestial sky`. The first arrow is a theorem (I re-verified it, see CLEAN
below). **The second arrow is false for discrete records, and `d47a` already
found this and called it a DEMOTION** — it rejected 121 of 554 genuine 2+1
skies as non-arc systems and concluded "a discrete sky of real Minkowski is
therefore NOT generally an arc system". D54 cites SG0 and does not carry
SG3b's demotion, so the only support offered for the headline is an arrow
the corpus has already retired.

**My recomputation** (`/tmp/d54rev/arcs.py`; exact-rational `M^{2+1}`
records generated by `d47a`'s own integer-congruence generator, exact
squared-interval causal order, SKY-B at depths 1..8, restricted to
SC5-capable skies — the corrected D53 condition — and decided by my own
cyclic-consecutive-ones search with the same cap 8):

```
   N=60  box=40 : ARC=  1  NOT-ARC= 13  UNDECIDED-BY-CAP= 16
   N=80  box=80 : ARC= 27  NOT-ARC=  4  UNDECIDED-BY-CAP= 30
   N=120 box=60 : ARC= 52  NOT-ARC=138  UNDECIDED-BY-CAP= 93
   N=160 box=160: ARC= 99  NOT-ARC= 63  UNDECIDED-BY-CAP=317
   TOTAL        : ARC=179  NOT-ARC=218  UNDECIDED=456
```

**218 of the 397 decided SC5-capable SKY-B skies of genuine exact `M^{2+1}`
records are not arc-realizable** — a majority. "Not an arc system" therefore
cannot carry "not a 2+1 sky" for discrete records. Either the claim retreats
to the strict stipulation *"a 2+1 celestial sky means an arc system on the
circle of directions"* (in which case it says nothing about whether the
record could be a discrete 2+1 causal set — which is what "obstruction
against 2+1" is read as, and what `d47a`'s own halt condition is built
around), or it must be re-founded on the shatter-4 null over genuine 2+1
records.

**The sound version exists, and I established it** (see MINOR 1): over 1,925
SC5-capable `(base event, depth)` pairs across seven exact `M^{2+1}` records
at SKY-B depths 1..10, **zero** shattered 4-sets, while this record shatters.
That is a real empirical separator and it is the claim the unit is entitled
to. It requires the word "empirical", and it requires the control to be run —
which the unit never did at its own reading.

---

## MINOR 1 — the halt-condition control was never re-run at the reading the certificate is read in

`d47a` pin §6 makes the Minkowski control binding: if a genuine exact
`M^{2+1}` record shatters a 4-set, the SKY DEFINITION is at fault and the
unit must HALT AND RE-PIN. `d47a`'s SG3/SG3b discharge that control with
`sky(C, e, kind)` — i.e. **SKY-B at the committed default `SKYB_DEPTH = 2`
only** (`d47a` line 322: `def sky(C, e, kind, depth=SKYB_DEPTH)`; SG3b calls
it with no depth argument). D54 reads its certificate at **SKY-B(5)**, a
reading whose Minkowski control had never been run anywhere in the corpus.
Changing the depth changes the definition; the control obligation transfers
with it, and neither D54 receipt discharges it.

I discharged it (`/tmp/d54rev/mink.py`, SKY-B depths 1..10, SC5 gating):

```
lattice N=40  box=40 : SC5-capable (e,d) pairs=  0   SHATTERED=0
lattice N=60  box=40 : SC5-capable        =  30   SHATTERED=0
lattice N=80  box=80 : SC5-capable        =  61   SHATTERED=0
lattice N=80  box=40 : SC5-capable        =  46   SHATTERED=0
lattice N=120 box=60 : SC5-capable        = 325   SHATTERED=0
lattice N=160 box=160: SC5-capable        = 589   SHATTERED=0
lattice N=200 box=60 : SC5-capable        = 874   SHATTERED=0
TOTAL over genuine M^{2+1}, SKY-B depths 1..10: 1925 capable pairs, 0 SHATTERED
```

Damage: **none** — the halt condition is not tripped, and this is by far the
strongest control the shatter-4 instrument has ever had (1,925 capable pairs
against D53's re-audited 139). But it was a missing gate on the unit's own
headline reading, and it was supplied by the referee, not the receipt.

## MINOR 2 — the pin's per-`d` reporting was promised and not delivered; the omission *understated* the result

Pin §5: "The depth parameter is **reported per d in {1..6}**; a success
under one d is READING-RELATIVE and says so (the blueprint targets d = 5)."
`d54b` reports one depth only, and derives it from the blueprint
(`sky_report`: `DEPTH = hh[dirs_idx[0]] - hh[E_IDX]`). The promised table is
absent. My table (`/tmp/d54rev/indep.py`, my own SKY-B and shatter code, on
the rebuilt 42-event record):

```
 d=1: |dirs|=1  distinct traces= 1  empty=False  subsets(ABCD)= 0/16  shatter4=None
 d=2: |dirs|=2  distinct traces= 4  empty=True   subsets      = 1/16  shatter4=None
 d=3: |dirs|=3  distinct traces= 8  empty=True   subsets      = 1/16  shatter4=None
 d=4: |dirs|=4  distinct traces=16  empty=True   subsets      = 1/16  shatter4=(5,8,11,13)
 d=5: |dirs|=4  distinct traces=16  empty=True   subsets      =16/16  shatter4=(9,12,14,15)
 d=6: |dirs|=4  distinct traces=16  empty=True   subsets      = 1/16  shatter4=(16,17,21,24)
 d=7: |dirs|=4  distinct traces=11  empty=True                        shatter4=None
 d=8: |dirs|=5  distinct traces= 8  empty=True                        shatter4=None
```

The record shatters a 4-set at **three** depths (4, 5, 6) on three different
direction sets, all SC5-capable. The unpinned omission cost the unit a
stronger, less reading-relative statement. (For contrast, the 9-actor
negative exhibit shatters at **no** depth 1..8 — I checked; its best is 8
distinct traces at `d=5`.)

## MINOR 3 — premise P is a THEOREM of the layer; the note's "[EXACT at tested scope]" understates it

`note-d54-dilworth-gate-result.md` §1 (i) and "Scope of each step": "(i) is
gated, not proven from the grammar — the theorem is EXACT at every scope
where (i) holds, and (i) is corroborated, zero exceptions". A three-line
proof is available from `d42b1` itself:

1. `event_poset` (d42b1 lines 81–91) chains every register: for a register
   `r`, the events touching `r` in index order `i₁<…<i_m` satisfy
   `i_t ∈ pred[i_{t+1}]`, and `pred` is transitive by induction on the same
   loop. So **any two events sharing a register are comparable**, always.
2. For every event type, the initiator is among the registers: `regs_of` gives
   `{e[1]}` for `p`/`n`, `{e[1],e[2]}` for `d`, `{e[1], ('mw',…)}` for `m`,
   and `props ∪ {vname}` for `r` — where `arb_components_in_view` (line 237)
   *requires* `a ∈ {proposers}`, so `e[1] ∈ regs_of(e)` for admissible arbs.
3. Hence same-initiator ⇒ same register ⇒ comparable. ∎

Verified (`/tmp/d54rev/premise.py`): **30,728 menu-offered events** across the
exhaustive 2-actor family (types `p 8124 / d 9934 / n 7938 / r 4732`),
**0 with initiator outside its registers**; the foreign arb
`('r','B',{('A',v0,0)},…)` is refused by the layer while `('r','A',…)` is
admitted. And the *stronger* register-sharing form of P over the receipt's
own families: **226,223 register-sharing pairs, 0 incomparable** (my own
closure). The theorem is unconditionally exact at transport scope, not
"exact at tested scope"; the label is the defect, in the conservative
direction.

## MINOR 4 — the T-LEMMA sweep never reaches the regime the theorem is used in, and the receipt computes the fact then discards it

`d54_dilworth_gate_exact.py` accumulates `used` (groups with more than one
distinct trace) and `chain_counts` (per-sky group counts) and **never reads
either** — dead variables. That is precisely the informativeness data. I
re-instrumented the sweep (`/tmp/d54rev/sweepaudit.py`, reproducing the
receipt's 15,909 skies / 33,546 groups exactly):

```
|dirs| distribution over the 15,909 skies : {2: 15850, 3: 59}
skies with >= 4 directions                : 0
distinct traces per sky                   : {2:5615, 3:9150, 4:1099, 5:31, 6:12, 7:2}
max distinct traces in ANY swept sky      : 7      (SC5 needs >= 16)
groups with >= 2 distinct traces          : 12,933 of 33,546  = 38.6%
trace-pair comparisons actually performed : 31,372
```

So: the corroboration is **not vacuous** (31,372 real comparisons, 12,933
non-trivial groups) — but 61.4% of the advertised "33,546 per-actor groups"
carry a single trace value, where nestedness has no pair to test, and **not
one swept sky has 4 directions or more than 7 distinct traces**, i.e. the
lemma is never corroborated in the 4-direction/16-trace regime where the
theorem is applied. The sweep also runs only `d ∈ {1,2,3}`, never the `d=5`
of the headline. T-SWEEP declares its own vacuity honestly; T-LEMMA declares
no scope at all, and the result note's "corroborated over 15,909 skies
(33,546 per-actor groups)" inherits the unqualified count. (Nesting is
depth- and width-independent by the proof, and I verified it directly at
`d=5` on both constructed records, so the damage is bounded to the labelling.)

## MINOR 5 — "the construction SATURATES the theorem" is false as stated, and the true saturation fact is unreported

Gate **K8** label and result note §2: "the construction SATURATES the
theorem, it does not beat it", with the detail `contributing actors = 16
(bound: 6), total = 20`. 16 chains against a bound of 6 is not saturation,
and §5 residue 1 concedes the gap is real — the note contradicts itself
across three pages. What K8 actually gates is `contributing >= 6`, a
one-sided consistency check.

The genuinely interesting fact, which I computed and which is absent from
the unit: **the realized 16-trace family's exact minimum chain cover is 6 —
the Dilworth bound, attained.** (`/tmp/d54rev` matching computation:
minimum chain cover = `|F| − maximum matching` in the strict-comparability
bipartite graph of the realized family; result 6 for the courier record, 4
for the 8-trace negative exhibit.) So the family is Dilworth-tight while the
actor spend is 16 (initiator attribution) or 20 (wire attribution). Residue 1
should say that: the 6-vs-20 gap is entirely architectural — a scheduling
cost of backflow — not a slack in the family.

## MINOR 6 — two of eleven gates in `d54b` are theorem-passes, unlabelled

`K9-A` and `K9-C` ("SKY-A/SKY-C on this record has NO empty trace") cannot
fail: D53 established structurally that SKY-A and SKY-C **can never** carry
the empty trace, for any record at any width or depth (LOG #426: "the
directions are the COVERS of the base event, so every event strictly above
it lies above at least one cover"). The label says "reproduced on the
constructed object", which is honest about provenance but does not name the
gate as a theorem-pass, and both are counted in the advertised 11 PASS. This
is the D44c-P round-1 P1 defect class (67,403 "certifications" that were
theorem-passes) in miniature. Same class, smaller: `K4`'s
`inc_ok` (pairwise incomparability of the directions) is implied by `K4`'s
own equal-height clause, since `x < y ⇒ h[x] < h[y]`.

## MINOR 7 — the anti-vacuity apparatus is weaker than its labels suggest

* `d54`'s mutant **M1** evaluates
  `not (frozenset({0,1}) <= frozenset({1,2}) or frozenset({1,2}) <= frozenset({0,1}))`
  on hand-written literals. Its verdict is fixed at authoring time and it
  never touches the sweep's code path (the sweep inlines its own comparison
  rather than calling a shared predicate). It tests Python's `frozenset.__le__`,
  not the instrument. A real mutant would inject a crossing trace pair into
  the per-initiator grouping and confirm `nest_bad` increments.
* `d54b`'s **K10** builds `_bound` (the run-bound-name set) and then never
  uses it: `_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]`.
  The scan is therefore strictly weaker than `d54`'s M3 and `d47a`'s SG8,
  both of which also require a run-bound name. The label is honestly scoped
  ("no bare-constant predicates, nothing more"), so this is hygiene plus dead
  code, not misdescription.

## MINOR 8 — the written proof's trace is not the instrument's trace, and the shatter step skips a (true) restriction

`note-d54-dilworth-gate-result.md` §1 (ii): "their down-sets are nested, so
the traces they contribute — down-set ∩ directions — form a chain". The
committed instrument's trace is `{c ∈ dirs : c == f or c < f}`, i.e.
`(down(f) ∪ {f}) ∩ dirs`, not `down(f) ∩ dirs`. The conclusion survives —
`x < y ⇒ down(x) ∪ {x} ⊆ down(y) ⊆ down(y) ∪ {y}` — but the proof as written
does not define the object the receipt measures, and the `c == f` clause is
exactly the one the brief flagged. One line fixes it.

Second gap in the same step: the theorem is stated for "all `2^m` subsets of
an `m`-element direction set", and shattering is folded in with "in
particular". When `|dirs| > m` the shattered family is `{r ∩ S}`, not `{r}`;
the bound transfers because `r ↦ r ∩ S` is monotone (so a chain of rows maps
to a chain of intersections), but that step is unwritten — and it is
exercised, since T-SWEEP's parenthetical reasons about SC5-capable skies
generally. One line fixes this too.

## NIT 1 — stale verdict text in `d54`

The VERDICT block prints "Sperner corroborated to k = 5" while the T-SPERNER
gate runs `k = 1..6` and reports `(k, SCD chains, middle layer)` up to
`(6, 20, 20)`; the result note and LOG both say `m ≤ 6`. The printed line is
a leftover.

## NIT 2 — the pin's Sperner gate was substituted, correctly, without amending the pin

Pin §3 committed "Sperner corroborated by brute force for k <= 5"; the
receipt substitutes the dBTK recursion, with the reason in an in-code comment
(`2^32` antichain masks at `k=5`, unrunnable) and in LOG #428. The
substitution is logically *sufficient* — a chain partition of size `N` bounds
every antichain by `N`, and the middle layer realizes `N`, so
min-cover = max-antichain = `N` exactly — so this is not a weakening. But §3
of the pin still reads as if brute force were run.

## NIT 3 — the first-run failing receipt survives only in git

`e07582c` committed the honest failing output (`9 PASS / 3 FAIL`, `EXIT 1`,
`K6/K7/K8` red on the 9-actor blueprint) and `9a73cb7` overwrote it. The
failure is preserved in pin §8 A1, in LOG #428 and as gate N1, so nothing is
hidden — but the result note's negative-exhibit paragraph does not point a
reader at `e07582c` where the original red gates are legible.

---

## Checked and CLEAN

Everything below is my own recomputation, not a reading of the receipts.

**A. Receipts rerun.** From the repo root: `python3
v10/code/d54_dilworth_gate_exact.py` → `9 PASS / 0 FAIL`, `EXIT 0`, rc 0;
`python3 v10/code/d54b_shatter_construction_exact.py` → `11 PASS / 0 FAIL`,
`EXIT 0`, rc 0. Both outputs **byte-identical** to the committed `.out` files
(diff clean modulo the wrapper's `RC=` line). No hidden nondeterminism.

**B. The construction, independently verified.** I rebuilt both histories by
re-running the specification sequence against the committed
`candidates_for` (nothing constructed freehand; every event taken from the
menu, `refusal = None`), then computed **everything else with my own code**:

* the layer's `event_poset` equals my own from-scratch register-chain
  transitive closure (Floyd–Warshall over the cover graph) on **both**
  records — `True` in each case; the relation is transitive, antisymmetric
  and irreflexive (checked over all triples);
* PART 1 = 31 events / 9 actors; PART 2 = **42 events / 20 actors**;
* `E` at index 1, height 1; the four direction events at indices
  `9, 12, 14, 15`, all at height 6, all strictly above `E`, offset **5**;
  **no other future event sits at that offset** (so `K5` is not circular:
  extra events at the offset would break it);
* SKY-B(5) at `E`: **16 distinct traces, empty trace present, all 16 subsets
  of {A,B,C,D} realized, shattered 4-set = (9,12,14,15)**. SC5 satisfied by
  my own count (`≥4` directions ✓, `≥16` distinct traces ✓, empty ✓).
  The receipt's K4/K5/K6/K7 reproduce exactly.

**C. The proof's steps.**
* (i) ⇒ (ii): same-initiator events share the initiator's register, hence are
  comparable — see MINOR 3, where it is proven, not just gated. The
  initiator assignment `e ↦ e[1]` is single-valued, so the cover is a
  partition and no event is double-counted (the brief's delivery edge case is
  clean: a delivery is attributed to its sender only).
* Down-set nesting is genuine: the layer's poset is transitive (verified), so
  `x < y ⇒ down(x) ⊆ down(y)`, and the per-initiator families are nested on
  both constructed records at `d=5` (`all-nested = True`).
* **The theorem is robust to the attribution.** Because register-sharing
  events are *also* totally ordered, the WIRE attribution works too: on the
  42-event record both the 16 initiator groups and the 20 wire groups are
  nested families. The bound `≥6` is unaffected either way.
* Direction sets are antichains under all three committed definitions
  (SKY-B by equal height, SKY-A/C by minimality), so the theorem's "any sky
  whose direction set is an antichain" is not a hidden restriction — and the
  gating to SKY-B / `d ∈ {1,2,3}` in the sweep is a scope statement about the
  *corroboration*, not about the theorem.
* The counting is right and the bound is `≥ 6`, not weaker: the 6 pairs of
  `B₄` are pairwise incomparable, a chain meets an antichain at most once,
  and chains containing extra non-pair elements do not help. I recomputed the
  minimum chain cover of the *realized* family exactly (Dilworth via maximum
  matching): **6**, matching the certificate from both sides.

**D. Stage 0 and Stage 1 counts reproduce exactly.** Rebuilding the same four
families (exhaustive `w2` cap 5 = 30,729 histories; walks at widths 3/4/6)
with my own closure: **218,795 actor-sharing pairs, 0 incomparable** —
identical to the receipt; **226,223 register-sharing pairs, 0 incomparable**
(the stronger form). Sweep: **15,909 skies, 33,546 per-actor groups, 0
non-nested pairs** — identical.

**E. Premise P on the very record the headline rests on.** The brief's
concern was that P was gated on widths 2/3/4/6 while the construction uses
20 actors. I tested P directly on both constructed records:
courier record **147 wire-sharing pairs, 0 incomparable** (register-sharing:
147, 0); 9-actor record **136 pairs, 0 incomparable** (registers: 136, 0). P
holds where it is used. The receipts never gated it there — but per MINOR 3
it is a theorem, so this is bounded to the labelling.

**F. Arcs cannot shatter 4 — independently reconstructed.** Full arc systems
(every cyclic interval) on `n = 4…12` points: `|rows| = 14,22,32,44,58,74,92,
112,134`, shatter-3 always `True`, shatter-4 always `None`. The structural
reason, computed rather than asserted: restricted to *any* 4 columns an arc
system realizes exactly **14 of 16** traces, missing precisely the two
"crossing" pairs (`S=(0,1,2,3)` misses `{0,2},{1,3}`; `S=(0,2,4,6)` misses
`{0,4},{2,6}`; `S=(0,1,4,5)` misses `{0,4},{1,5}`). So `shatter-4 ⇒ not an
arc system` is sound for arc systems on any number of points. (What that
buys is the subject of MAJOR 2.)

**G. The negative exhibit and its mechanism.** The 9-actor build is
admissible end to end (31 events, all menu-offered) and realizes exactly
`{}, {A}, {B}, {C}, {D}, {A,B}, {A,B,C}, {A,B,C,D}` = **8/16** at `d=5`, and
shatters at no depth 1..8. The mechanism statement is exactly what the poset
shows: `B`'s per-initiator trace family is `{}, {B}, {A,B}` — after `B`
delivers into `F` (which already holds `A`), every later send from `B` carries
`{A,B}`, so `G`'s chain is `{A,B} ⊂ {A,B,C} ⊂ {A,B,C,D}`, a duplicate of
`F`'s. "The sender's wire absorbs the receiver's accumulated past" is
literally `regs_of(('d',s,r,v)) = {s,r}` in `event_poset`: the delivery is a
join and everything later on the sender's wire is above the receiver's prior
events. Confirmed; and the courier repair is confirmed as the reason it
works — each courier's wire carries exactly one direction into a charged
accumulator (per-wire dumps `J:{A,B}`, `K:{A,B,C}`, `L:{B,C}`, `M:{A,C}`,
`N:{A,B,C,D}`, `O:{B,C,D}`, `P:{A,C,D}`, `Q:{B,D}`, `R:{A,D}`, `S:{C,D}`,
`T:{A,B,D}`).

**H. Blueprint fidelity to the pin.** PART 1 implements pin §4 exactly under
the renaming `A1..A4 → A,B,C,D`, `B1..B4 → F,G,H,I`: `F←A,B,C,D`;
`G←B,C,D`; `H←A,C,D`; `I←B,D,A`; then the two late pairs `A←D` (`{14}`) and
`C←D` (`{34}`), with all B-deliveries preceding the late receipts (the
load-bearing ordering constraint). PART 2 implements pin §8 A2's schedule
event for event: clean first receipts `A→F, B→G, A→H, B→I`; mints
`B→J; C→K,L,M; D→N,O,P,Q,R,S; A→T` (11 couriers, sources exactly as
pinned); sends `J→F, K→F, N→F; L→G, O→G; M→H, P→H; Q→I, T→I; R→A, S→C`.
`9 + 11 = 20` actors, 42 events. No silent re-engineering.

**I. Measure-freeness.** The builder reads `candidates_for`'s `(e, q)` pairs
and discards every `q` (`hits = sorted((e for e, q in menu if spec(e)),
key=repr)`); no gate in either receipt reads a weight. §3's "measure-free: no
completion, no normalization, no H1" is accurate.

**J. The B₄ / dBTK certificate.** The 6 pairs are pairwise incomparable; the
exhibited SCD is 6 strict chains covering all 16 subsets; the dBTK recursion
gives, for `k = 1..6`, chain partitions of sizes `1,2,3,6,10,20` and middle
layers of the same sizes, `= C(k, ⌊k/2⌋)`. Partition, strictness and
antichain properties all recompute. The two-sided argument
(min chain cover = max antichain = `C(k,⌊k/2⌋)`) is valid as gated.

**K. Record fidelity.** `git log` order is correct and clean:
`0cf761d` (LOG #427 + pin, **no code**) → `e07582c` (both receipts, both
`.out`s, pin §8 amendment) → `9a73cb7` (LOG #428, result note, revised
`d54b`). The pin genuinely preceded the code. Every number in LOG #427/#428
matches the receipts' actual output: 218,795 / 15,909 / 33,546 / `9 PASS 0
FAIL` / `11 PASS 0 FAIL` / 31 events 8/16 / 42 events / 20 actors / 16
contributing / `d = 5`. Result-note numbers likewise. §4 is labelled
`[MY READING]`; §5 residues are honest. The pre-registration failure (the
pinned blueprint refuted by its own run and kept as gate N1) is exemplary and
is not counted against the unit anywhere in this review.

---

## Final verdict

**REVISE.** The Dilworth gate itself is in better shape than the unit claims:
its premise is a theorem of `d42b1` rather than a gated empirical fact
(MINOR 3), its chain-cover step survives two independent attributions, and the
construction is real — I rebuilt it from the committed menu and confirmed the
shattered 4-set with code that shares no line with `d47a`, and it shatters at
three depths rather than the one reported (MINOR 2). The 42-event record is a
genuine object and its shadow family is Dilworth-tight at exactly 6 chains
(MINOR 5). Nothing I could throw at Stage 0, Stage 1, the construction, the
negative exhibit, the arithmetic or the provenance broke any of it, and the
Minkowski halt control — which the unit never ran at its own reading —
passes with 1,925 capable pairs and zero shatterings when I run it
(MINOR 1).

What must change is the *interpretation layer*, and it must change in three
places. The BLOCKER is a sentence, not a computation: "a sphere-like sky
(shattering at every m)" describes nothing, because caps on `S²` shatter 4
and never 5 — I certify this with an exact Radon partition — so the
Sperner route does not derive infinite clocks, and "the infinite-clocks
doctrine is now a THEOREM" must be withdrawn as stated. It is rescuable, and
by a better argument than the one lost: `Θ(n³)` cap traces against chains of
length `n+1` forces `Θ(n²)` actors, with no shattering anywhere in the
derivation. But that same argument prices a 2+1 *circle* at `Θ(n)` actors
(MAJOR 1), so "the provable price of dimension" must become "the provable
price of sky size", with `3` versus `6` as the entire dimensional signal.
And the 2+1 obstruction reading (MAJOR 2) must be re-founded on the
shatter-4 null over genuine Minkowski records rather than on the
arc-realizability arrow that `d47a` itself demoted — a majority (218/397) of
genuine 2+1 SKY-B skies are not arc systems, and D54 cites the arrow without
the demotion.

None of the three requires new physics or a new receipt: one withdrawal, one
substituted argument (verified here), one re-founded inference (whose
supporting control is also supplied here). Nothing in this unit is citable
until those edits land and a delta records them.

---

# DELTA — repairs verified, 2026-07-26

Post-repair state: `d54_dilworth_gate_exact.py` **9 PASS / 0 FAIL**,
`d54b_shatter_construction_exact.py` **12 PASS / 0 FAIL** (K11 added),
both exit 0.

**BLOCKER 1 REPAIRED.**  The sphere-via-Sperner claim is withdrawn
everywhere it appeared: the theorem statement (result note §1) now ends
at "shatter-4 requires at least 6 actors"; the T-SPERNER gate label and
the receipt verdict carry the VC-dimension-4 correction explicitly; the
pin gains §9(i); LOG #429 forward-corrects #427/#428.  The
infinite-clocks conclusion is restated via the round's TRACE-COUNTING
route (Θ(n³) cap traces vs n+1 per chain ⇒ Θ(n²) actors),
`[REFEREE-CARRIED]`, with in-receipt promotion queued as residue 1b.

**MAJOR 1 REPAIRED.**  "Provable price of dimension" → "provable price
of SKY SIZE" in the note and reading; the dimensional signal is stated
as the shatter offset (3 vs 6), with the circle's own unboundedness
(n−2) carried alongside.

**MAJOR 2 REPAIRED.**  K7's label and the note's §3 MAY now state:
shatter-4 ⇒ not an arc system (theorem); "not a 2+1 sky" only under
the strict arc-model stipulation, said aloud with the demotion's
218/397 recount; the sound discrete separation is EMPIRICAL, resting
on the round's 1,925-capable-pair zero-shattering Minkowski control
`[REFEREE-CARRIED]` (per-reading halt control = MINOR 1, discharged by
the referee; in-receipt promotion queued).

**MINORS.**  1 — control carried as above.  2 — per-d table now gate
K11: the record shatters at d = 4, 5, 6 and at no other depth in 1..8
(the omission had understated the result).  3 — premise P relabelled a
THEOREM OF THE LAYER in the proof, sweep demoted to corroboration.
4 — dead variables removed; T-LEMMA now prints its |dirs|/trace census
and declares the regime limit in the gate text.  5 — "saturates"
withdrawn; the realized family's min chain cover = 6 (Dilworth-tight)
now gated in-receipt (K8).  6 — K9-A/C labelled [THEOREM-PASS]; K4's
derived incomparability clause labelled.  7 — M1 now calls the sweep's
own `is_nested` predicate; K10's dead `_bound` removed.  8 — the
proof's trace definition is now the instrument's (reflexive), and the
restriction-monotonicity line added.  **NITS.**  1 — stale verdict line
removed.  2 — pin §9(ii).  3 — the result note now points at `e07582c`
for the original failing output.

**TERMINAL** for round 1.  What stands after the round: the Dilworth
gate as an unconditional theorem of the transport layer; the 42-event
shattering record, verified independently, shattering at three depths;
the arc-system obstruction as a theorem and the discrete-2+1
separation as an empirical result with a 1,925-pair control; and the
corrected accounting — width prices sky size, the shatter ladder
prices dimension.
