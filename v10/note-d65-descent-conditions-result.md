# D65 — result: **DC1 FAILS, and the failure is EXACTLY a mass-ratio coboundary.** The generated law's *normalised* kernel does not descend to a record measure; its *unnormalised* weight does.

**Status: GREEN-UNREVIEWED, 2026-07-26.**  An independent hostile round
follows and nothing here is terminal.  Pin
`note-d65-descent-conditions-pin.md` (STRICT, frozen and committed
before this file existed).  Receipt
`v10/code/d65_descent_conditions_exact.py`, output
`v10/data/d65_descent_conditions_exact.out` — **28 PASS / 3 FAIL,
exit 0, 224.5 s wall clock** (run from the repo root), byte-identical
under three `PYTHONHASHSEED`s (0 / 12345 / 777, timing lines
excepted).  **All three FAILs are the same pre-registered negative**:
DC1(a), its refined-record sub-census DC1(f), and DC3(3) — which *is*
DC1 — are one finding counted three times, and the pin registered
that finding as a deliverable before any computation ran.

Parents: paper 29 (`relativistic-isp-v10-paper29-where-the-action-cocycle-lives.md`
— Theorem 1's refined cylinder cocycle and F1, Theorem 2's finite
boundary sufficiency and F2, §4.3's five durable-record hypotheses,
§9.2's slot table, Theorem 5); D59 (the two click-law objects meet at
**one missing map**; six supplied-not-derived items); D61 ((H1)
[THEOREM]) and D62 ((H2) [THEOREM]) — together making d44a's closure
theorem unconditional at this scope; d44a (36 states, 176 keys, the
committed masses); d42b3 (the admission layer, `canon`, and the
gradient completion); D49/D50 (the settled dichotomy and the
form-is-a-choice caveat).

**Scope, non-negotiable and load-bearing in every sentence below:
TWO-ACTOR, DELIVERY-FREE, d42a — the exhaustive depth-6 family
(34,375 histories, census `[1, 6, 32, 176, 976, 5280, 27904]`, 36
sigma states, 176 transition keys).**  Nothing here transfers to the
identified (action-line) click law.  Paper 29's missing map remains
open; this unit measured **one segment of it, from the generated side
only**.

---

## 1. DC1 — the census, in full

The test, exactly as pinned: `P(e|H) = menu weight / menu mass`, exact
`Fraction`s; a pair `{a, b}` of distinct menu events at `H`
**COMMUTES** when both orders are admissible and
`sigma(Hab) = sigma(Hba)` — which by (H1)+(H2) means the two
continuations carry *the same entire future law*; the identity under
test is

```
        P(a|H) · P(b|Ha)  =?  P(b|H) · P(a|Hb).
```

Every count below is over **ORDERED** pairs.  This is not pedantry:
the ratio defect `d` **inverts** under the swap of `a` and `b`, so a
census taken on one direction per unordered pair would depend on
which element the enumeration happens to call `a`.  Recording both
directions makes every census order-canonical, and the DET(a) gate
holds that discipline by re-running the depth-≤3 sub-census with the
parent list and every menu reversed.

**The census is EXHAUSTIVE over every parent of the family — the
deepest level included in full.  Nothing is sampled.**

| category | ordered pairs |
|---|---|
| ordered pairs `(a, b)` of distinct menu events | **794,570** (= 2 × 397,285 unordered) |
| NEITHER order admissible (mutual exclusion) | 129,284 |
| exactly ONE order admissible (admissibility asymmetry) | **0** |
| both orders admissible | 665,286 |
|  … of which `sigma(Hab) ≠ sigma(Hba)` (non-commuting, excluded by name) | **0** |
|  … of which COMMUTING | 665,286 |
|  …  … identity **HOLDS** | 576,654 |
|  …  … identity **FAILS** | **88,632** |

Per parent depth `[ordered pairs, commuting, defects]`:
`0: [30, 26, 0]`, `1: [140, 124, 24]`, `2: [832, 656, 192]`,
`3: [4672, 3648, 864]`, `4: [24416, 19744, 3456]`,
`5: [124992, 103744, 14976]`, `6: [639488, 537344, 69120]`.

Two census facts that were open before the run and are worth naming
on their own:

* **Admissibility on a menu pair is SYMMETRIC** — zero asymmetric
  pairs.  Either both orders run or neither does.
* **The menu is NOT all-concurrent.**  129,284 ordered pairs are
  *mutually exclusive*: `{('p','p'): 33,338, ('r','r'): 31,304}`.
  The shortest witness is at the root — `p_A(v0,0)` and `p_A(v0,1)`
  cannot follow one another in either order, because
  `prop_options_in_view` refuses a base already carrying the actor's
  live proposal.  Concurrency here is a property of the pair, not of
  the menu.
* **Wherever both orders do run, they already agree on the successor
  state** — zero non-commuting pairs.  At this scope the pin's
  "commuting" class is exactly the "both orders admissible" class.

### 1.1 The structure of the failure — complete, not partial

The pin pre-registered the lean: *DC1 likely holds for
disjoint-actor propose pairs by symmetry, and the genuine risk sits
at pairs whose intermediate states have DIFFERENT masses; if it fails
exactly there, the pattern should be a function of sigma alone.*
**The lean was right on every clause**, and the receipt gates the
sharpest available form of it.

1. **The RAW cocycle holds everywhere.**  `q(a|H)·q(b|Ha) =
   q(b|H)·q(a|Hb)` on **all 665,286** commuting ordered pairs — raw
   ratio spectrum `{1: 665286}`, zero exceptions (DC1(b)).  The
   generated law's *unnormalised* history weight is order-independent
   across every commuting square.  **The entire defect lives in the
   normalisation.**
2. **The defect is exactly the intermediate-mass ratio.**  For every
   commuting pair, `d = M(sigma(Hb)) / M(sigma(Ha))`, with `M` the
   per-state menu mass — a function of sigma alone (gated in N4:
   zero mass-splitting classes; 34 states of mass 2 and 2 states of
   mass 5/2, the two values being read off d44a's committed SB2
   row-sum line, never typed in).  Zero exceptions on 665,286 pairs
   (DC1(c)).  **The defect is the coboundary of a function of sigma:
   a mass-ratio cocycle and nothing else.**
3. **Spectrum:** `{1: 576654, 4/5: 44316, 5/4: 44316}` — exactly the
   ratio set `{M'/M''}` of the two masses, and symmetric as it must
   be under the ordered census.
4. **It is a function of `(sigma(H), class(a), class(b))` alone.**
   Tested at two key resolutions, both ordered: (A) the two events
   renamed separately by the committed `canon_pair`, (B) renamed
   jointly by `canon_pair2` (gated in N5 against `canon_pair` itself).
   616 classes each, **zero splitting classes** under either (DC1(d)).
   Because a class fixed by an automorphism swapping `a` and `b`
   receives both `d` and `1/d`, this simultaneously forces `d = 1` on
   every self-swapped class.
5. **It vanishes exactly on the same-mass subclass.**  Same-mass
   intermediates: `{1: 576654}` — no defect anywhere.  Mass-mixed
   intermediates: `{4/5: 44316, 5/4: 44316}` — a defect *everywhere*
   (DC1(e)).  The two sets partition the commuting pairs.  This is
   the natural subclass, and the failure is confined to it exactly.
6. **It is confined to 6 of the 36 sigma states** — indices 1, 2, 3,
   5, 6, 7, of which 1 and 3 are the two mass-5/2 states.  The other
   30 states carry `{1: …}` and nothing else.
7. **By ordered pair class**, `(n,n)`, `(p,p)` and `(r,r)` pairs never
   defect; the defects sit at the mixed-tag classes `(n,p)/(p,n)`,
   `(n,r)/(r,n)`, `(p,r)/(r,p)`.  This is a *consequence* of item 5,
   not an independent criterion: the mass jump is what a mixed pair
   can produce.

**The witness, at depth 1** (`H = [p_A(v0,0)]`, `a` = A's self-arb,
`b` = `p_B(v0,1)`): `q(a|H)=1/4`, `q(b|Ha)=1/8`, `q(b|H)=1/8`,
`q(a|Hb)=1/4` — raw products identical at `1/32` — but
`N(Ha) = 2` while `N(Hb) = 5/2`, so `d = 5/4`.  This is the d42b3
G-T2 witness pair, seen from the descent side: the mass jumps from 2
to 5/2 exactly when the blind conflict group becomes visible in the
join view (the quarter law's excess).

### 1.2 The refined-record sub-census

Paper 29's literal hypothesis is `[Hab] = [Hba]` **at the refined
record level**.  The generated line's record-identity functor is
d42b3's committed `canon` (the canonical labelled DAG of a history —
the same functor d42b3's own diamond census and G-T2 use).  *That
identification is an interpretive step and is declared as such.*
On the strictly stronger hypothesis:

* refined-identical ordered pairs: **425,334** (of 665,286 commuting);
* identity **FAILS** on **32,256** of them;
* spectrum `{1: 393078, 4/5: 16128, 5/4: 16128}`.

So the failure survives the strongest reading of the hypothesis.  The
remaining 56,376 failures sit on pairs that commute in the sigma sense
without being refined-record identical.

---

## 2. What DC1's failure does and does not say

**It says (exactly this, and no wider):** *at this scope, there is no
positive measure on refined record cylinders whose conditionals are
the generated law's normalised menu kernel.*  This is paper 29
Theorem 1's **contrapositive**, applied to a conditional system that
satisfies every one of Theorem 1's hypotheses — all three displayed
conditioning cylinders positive (DC3(4): 179,782 menu entries, zero
non-positive, smallest weight 1/8) and a common refined cylinder
(DC1(f)) — and still has unequal products.

**It is NOT an F1 hit.**  F1 asks for *a positive refined cylinder
measure* with unequal conditional products; Theorem 1 forbids that,
and Theorem 1 is a theorem.  What is exhibited here is a **conditional
system that is not induced by any such measure**.  The difference is
the whole content: the generated normalised law is *order-weighted*,
so it is not a measure's conditionals — it is not a counterexample to
the theorem about measures.

**It says nothing about the action line.**  No claim is made or
implied that the action line's conditional measure is the same
measure, or a different one, or related to this one.  The map is an
*identification problem*, not an existence problem, and this unit did
not touch it.

**It does not retract the closure theorem, (H1), (H2), or the
six-state chain.**  Those are statements about the *admissibility and
weight* law; DC1 is a statement about the *normalised* law's descent.
The unnormalised weight is exactly as order-independent as one could
ask (DC1(b)).

---

## 3. The completion corollary

**[PROOF — two lines, from two gated ingredients.]**  Let `Z` be any
positive completion that factors through `(depth, sigma)`, i.e.
`Z(h) = Ẑ(|h|, sigma(h))`.  Then for every commuting pair both
displayed products telescope,

```
    P_Z(a|H)·P_Z(b|Ha) = q(a|H)·q(b|Ha)·Z(Hab)/Z(H),
    P_Z(b|H)·P_Z(a|Hb) = q(b|H)·q(a|Hb)·Z(Hba)/Z(H),
```

and the two right-hand sides are equal: the raw products agree by
**DC1(b)** (gated, zero exceptions on 665,286 pairs), and
`Z(Hab) = Z(Hba)` because `|Hab| = |Hba|` and `sigma(Hab) =
sigma(Hba)` *is the definition of the commuting class*.  ∎

**The corpus already has such a completion.**  D49's root-free
completion `Ẑ(h) = 2^(−|h|)·f(class(sigma(h)))` (λ = 2,
`f = (4,4,3,7,3,3)/3`) has exactly that shape and is normalised per
cut at every depth at this scope.  So:

> **The generated law's normalised MENU kernel does not descend; the
> same law read through the corpus's own selected completion does.**

The price is named and unchanged — **D50: the stationary FORM of `Z`
is a CHOICE, i.e. supplied, not derived.**  That is why DC4 item 2
below *stands as supplied* and is *priced* rather than moved.

The receipt also exhibits an **independent** completion of a different
shape: d42b3's depth-4 gradient completion `Z`, re-derived and
anchored to d42b3's own committed numbers (`Z(∅) = 1037/64`, `Z > 0`
throughout, `Z` constant on canonical classes).  Under `P_Z` the
identity holds on all 403 commuting pairs inside `Z`'s domain, zero
failures (DC1-C).  Its cost is d42b3's own: within-cut ratio
deformation at 21 of 114 interior cut classes, the root included.

---

## 4. DC2 — a RESTATEMENT, and it must not be sold as anything else

Paper 29 Theorem 2 says a boundary-only kernel exists **exactly when**
the next-record law is constant on the declared boundary's fibres.
With `pi = sigma`, that condition **IS (H1)** — a theorem of D61 —
and the state update is (H2), a theorem of D62.  **Nothing new is
proved in DC2.**  The pin's F-DC2 is precisely the sin of
mislabelling it as new; it is not new.

What DC2 *does* deliver is the **identification and the exhibit**:

* fibre constancy re-affirmed directly on the family — 36 fibres,
  **zero** fibres carrying two different renamed menus, 34,375
  histories swept (DC2(a));
* the **36-row normalised kernel `K(·|sigma)` printed in full**,
  exact `Fraction`s, rows labelled by state index, mass and
  serialised state (see the receipt output);
* every history's normalised renamed menu equals its printed row —
  so the printed object *is* the law, not a summary of it (DC2(b));
* every row sums to exactly 1 (DC2(c) — division by the row's own
  mass; a reporting line, and labelled so).

---

## 5. DC3 — the five durable-record hypotheses (paper 29 §4.3)

| # | hypothesis | label | verdict |
|---|---|---|---|
| 1 | exclusive & exhaustive durable alternatives | **SUBSTANTIVE** | **PASS** |
| 2 | decoherence of the queried record algebra | **REPORTING-ONLY** | trivially satisfied, **uninformative** |
| 3 | one common refined cylinder | **SUBSTANTIVE** | **FAIL** (= DC1) |
| 4 | positivity of every displayed conditioning cylinder | **SUBSTANTIVE** | **PASS** |
| 5 | sufficient declared boundary | **RESTATEMENT** | satisfied (= DC2) |

**(1)** is a real two-sided gate and neither side is excluded a
priori: the menu could repeat an alternative (not exclusive) or omit
an admissible one (not exhaustive).  Against an **independently
constructed** adversarial pool of well-formed events over the tokens
each history has uttered — **718,570** pool events across all 34,375
histories — there are zero duplicates, zero omitted admissible
events, zero refused-but-listed events and zero weight disagreements.
The pool's single-base restriction on arb ckeys is itself lifted at
depth ≤ 4 (22,762 events, zero violations), so the restriction is not
load-bearing.

**(2)** holds *for the empty reason*.  The generated law is a
classical stochastic process on records — sigma is a serialised
finite state, the menu a finite set of exact `Fraction` weights, the
queried algebra the algebra of history cylinders — so its decoherence
functional is diagonal by construction.  **This is where the map's
remaining segment lives, and the receipt says so in the output.**
Paper 29's hypothesis (2) is a condition on class *operators* and
their Gram functional `D(α,β) = ⟨v_α, v_β⟩` (§4.1–§4.2).  The
generated line **has no functional level at all** — no amplitudes, no
class operators, no Gram functional — and **this unit does not build
one**.  The segment of the map running from a decoherence functional
to a generated record measure is untouched, and it is exactly where
D59's *record instrument* and paper 29 §9.2's *preferred durable
algebra* still sit.

**(4)** is substantive — a single zero weight would make a displayed
conditional undefined and would void DC1's test on that pair.  Every
menu weight is a strictly positive exact `Fraction` (179,782 entries,
smallest 1/8), every mass positive, and the support is exactly the
admissible set by (1): the law never displays a zero-mass alternative.

---

## 6. DC4 — D59's six supplied-not-derived items, re-scored

No item moves without a gate above it.  One moves; five stand.

| # | item | verdict |
|---|---|---|
| 1 | boundary state | **MOVES — for the GENERATED line only** |
| 2 | measure and contour | stands; **now priced** |
| 3 | renormalization | stands; untouched |
| 4 | record instrument | stands; DC3(2) says why it cannot move |
| 5 | generated record grammar | stands *for the action line*; never supplied on the generated line |
| 6 | clock dictionary | stands; untouched |

**1. Boundary state — MOVES, with a boundary on the move itself.**
Ground: DC2(a)/DC2(b) carried by (H1) [D61] + (H2) [D62].  Paper 29
Theorem 2 asks for a declared boundary statistic whose fibres carry a
constant next-record law.  On the generated side that statistic is
**not supplicated**: sigma is *constructed* from the committed layer
and its sufficiency is a *theorem*, with the 36-row kernel printed.
**The honest qualification, which must travel with the claim:** paper
29 §9.2's slot is the *boundary/cosmological state of the action
line*, which selects amplitudes and long-range correlations.  That is
a **different object**, and it remains supplied.  What moved is the
generated line's *own* boundary statistic — the counterpart of the
slot, not the slot.

**2. Measure and contour — stands, and DC1 sharpens exactly why.**
The generated law has an order-independent unnormalised weight
(DC1(b)) and a normalised kernel that is *not* order-independent
(DC1(a)); the gap between them is precisely the coboundary of the
state-mass function (DC1(c)).  A measure on record cylinders
therefore requires a **completion** — supplied data, whose form D50
already showed is a choice.  §3 exhibits two completions that work.
Not derived; **now precisely priced**: the price is exactly one
coboundary, and the corpus has already paid it once (D49).

**3. Renormalization — stands.**  No gate in this unit concerns a
continuum limit, a regulator or a scale.  The generated law is finite
and combinatorial; the unit produced no fact about this slot.

**4. Record instrument — stands.**  DC3(2) is reporting-only; the
generated line cannot derive which alternatives decohere or which
algebra is queried, because it has no functional level.  What DC3(1)
establishes is narrower and worth keeping distinct: the generated
line's *own* alternative set is exclusive and exhaustive and its
support is exactly the admissible set.  That is a record **grammar**
fact, not a record **instrument** fact.

**5. Generated record grammar — stands for the action line.**  D59's
item is that the identified (D15) law has not been given a generated
record grammar.  The d42a grammar exists and this unit gated its
exclusivity/exhaustiveness (DC3(1)) and its boundary sufficiency
(DC2) — but **nothing here connects it to D15 action content**.
Paper 29's Theorem 5 is untouched.

**6. Clock dictionary — stands.**  No gate produces a rate, a unit or
a time coordinate.  Paper 29's Theorem 1 needs no time coordinate and
neither does this receipt.

---

## 7. Licensed claims — and the ones this unit forbids

**Licensed, at two-actor delivery-free d42a scope on the exhaustive
depth-6 family:**

1. The generated law's normalised menu kernel **fails** the
   commuting-square identity on 88,632 of 665,286 commuting ordered
   pairs, and on 32,256 refined-record-identical ordered pairs.
2. The failure is **exactly** `d = M(sigma(Hb))/M(sigma(Ha))` — the
   coboundary of the per-state menu mass — with zero exceptions;
   it is a function of `(sigma(H), class(a), class(b))`; it vanishes
   on same-mass intermediates and occurs at every mass-mixed pair;
   it is confined to 6 of 36 states.
3. The **unnormalised** weight satisfies the identity everywhere.
4. Consequently **no positive measure on refined record cylinders has
   the generated normalised kernel as its conditionals** at this
   scope.
5. Any completion factoring through `(depth, sigma)` annihilates the
   defect; D49's `Ẑ` is one, d42b3's gradient `Z` is another of a
   different shape.
6. `pi = sigma` is a sufficient declared boundary and the 36-row
   kernel exists and is printed — **as a restatement of (H1)+(H2)**.
7. Hypotheses (1) and (4) of paper 29 §4.3 hold on the generated law;
   (2) holds vacuously; (3) fails; (5) is (6) above.

**Explicitly NOT licensed (do not quote):**

* anything about the identified/action-line click law, its measure, or
  whether it is "the same measure" — the map is untouched;
* "the generated law descends to a record measure" *without* the
  completion clause and its D50 price;
* "the generated law does not descend" *without* the normalised/
  unnormalised distinction — the unnormalised weight descends;
* any of the above at three-actor scope, at transport scope, or
  beyond the exhaustive depth-6 family;
* DC2 as a new result of any kind.

---

## 8. Residues

1. **The map's functional segment is untouched and named.**  The
   generated line has no class operators and no Gram functional; DC3(2)
   is therefore uninformative and will stay uninformative until a
   functional level is built.  That, not DC1, is where the missing map
   is widest.
2. **Whether the defect's coboundary form survives beyond this scope.**
   `M` takes two values here because the quarter law's excess is
   binary at two actors.  At three actors or with delivery the mass
   spectrum changes and the coboundary statement must be re-derived,
   not carried.
3. **The refined-record identification.**  `canon` was *chosen* as the
   generated line's record-identity functor.  A coarser or finer
   record functor changes which pairs are in DC1(f)'s subclass, though
   not DC1(a)'s verdict (the sigma-commuting class contains it).
4. **Depth.**  The census is exhaustive to depth 6 with transitions
   into depth 8.  The all-depth statement follows from (H1)+(H2) plus
   the mass-function argument, but it is *stated* here, not
   mechanized; a depth-free proof of DC1(c) is a one-page obligation
   the successor should discharge.
5. **Three actors, transport** — out of scope, as always.
