# D65 — result: **DC1 fails on the refined sub-census, as a pure mass-ratio coboundary.** The generated law's *normalised* kernel does not descend to a record measure; its *unnormalised* weight is order-independent (and is not itself a measure). The defect is **REPAIRABLE**, and the corpus's completions are **among** the repairs — `Ẑ`'s measure genuinely descends (now gated) — but the repair space is **573-dimensional**, and the selection down to `Ẑ` is **D50's form choice, not descent**.

**Status: ROUND-1 REVIEWED AND REPAIRED, 2026-07-26.**  The
independent hostile round is
`reviews/d65-round1-hostile-review.md` — **REVISE: 1 BLOCKER /
5 MAJOR / 8 MINOR / 3 NIT**, with the arithmetic verdict *"every
single number reproduces"*.  Every finding is applied here and in the
receipt; **every number the referee produced has been independently
recomputed in this receipt and every one of them holds** — the repair
ranks and dimensions, the hierarchy, both witnesses (including the
referee's own exact fractions, reconstructed by a deterministic scan
rather than imported), the class-level census, the eigen-structure and
the cut masses.  The single exception is not a disagreement: witness
(i)'s count of broken record-constancy equations depends on *which*
kernel direction is taken, and the two constructions take different
ones (§3.1); the verdict it certifies is direction-independent.
Nothing the round confirmed has been withdrawn: the defect structure, the
exhaustive census, the witnesses and the consequence sentence all
stand exactly as delivered.  What changed is what the numbers were
said to MEAN.

Pin `note-d65-descent-conditions-pin.md` (STRICT, frozen and
committed before the receipt existed; its DC1 predicate is the coarse
one and is gated as written).  Receipt
`v10/code/d65_descent_conditions_exact.py`, output
`v10/data/d65_descent_conditions_exact.out` — **39 PASS / 3 FAIL,
exit 0, 335.9 s wall clock** (run from the repo root), byte-identical
under `PYTHONHASHSEED` variation — default / 7 / 12345, re-verified
this round, timing lines excepted.  (One hash-order hazard *was*
introduced by the round-1 repairs and removed before delivery: the new
repair-space block ordered record classes by `repr`, whose value for a
`frozenset` is seed-dependent; it now orders them by first occurrence
in the enumerator's own history order.)  **The three FAILs are TWO statements, not one:** DC1(a)
(= DC3(3), literally the same predicate) and **DC1(f)**, a different
predicate over a different population under a strictly stronger
hypothesis — and DC1(f) is the one paper 29's theorem speaks to.  The
pin registered the finding as a deliverable before any computation
ran.

Parents: paper 29 (`relativistic-isp-v10-paper29-where-the-action-cocycle-lives.md`
— Theorem 1's refined cylinder cocycle and F1, **§3/§3.1's refined-vs-
coarse distinction**, Theorem 2's finite boundary sufficiency and F2,
§4.3's five durable-record hypotheses, §9.2's slot table, Theorem 5);
D59 (the two click-law objects meet at **one missing map**; six
supplied-not-derived items); D61 ((H1) [THEOREM]) and D62 ((H2)
[THEOREM]) — together making d44a's closure theorem unconditional at
this scope; d44a (36 states, 176 keys, the committed masses); d42b3
(the admission layer, `canon`, and the gradient completion); D49/D50
(the settled dichotomy and the form-is-a-choice caveat).

**Scope, non-negotiable and load-bearing in every sentence below:
TWO-ACTOR, DELIVERY-FREE, d42a — the exhaustive depth-6 family
(34,375 histories, census `[1, 6, 32, 176, 976, 5280, 27904]`, 36
sigma states, 176 transition keys each with a single successor,
5,548 record classes).**  Nothing here transfers to the identified
(action-line) click law.  Paper 29's missing map remains open; this
unit measured **one segment of it, from the generated side only**.

---

## 1. DC1 — the census, and which census is load-bearing

The test, exactly as pinned: `P(e|H) = menu weight / menu mass`, exact
`Fraction`s; the identity under test is

```
        P(a|H) · P(b|Ha)  =?  P(b|H) · P(a|Hb).
```

**Two different hypotheses were censused, and only one of them is
Theorem 1's.**  Paper 29 §3 defines commutation *at the refined record
level* — "both orders denote the same cylinder: `[Hab] = [Hba]`.  This
is a statement about record identity, not merely equality of a coarse
terminal state" — and §3.1 says what the theorem does **not** require:
"The theorem does not require equal weights for two distinct serial
histories that later push to one quotient atom."  The pin's DC1
predicate calls a pair commuting when `sigma(Hab) = sigma(Hba)`, which
is exactly equality of a coarse terminal state.  So:

* **DC1(f) — the refined-record sub-census — is THE LOAD-BEARING
  TEST.**  `32,256` failures on `425,334` refined-record-identical
  ordered pairs (7.58%), spectrum `{1: 393078, 4/5: 16128,
  5/4: 16128}`.
* **DC1(a) — the wider sigma-commuting census — is context.**  `88,632`
  failures on `665,286` ordered pairs (13.32%).  `56,376` of those
  failures — 63.6% of the headline — sit on pairs that are
  sigma-commuting but **not** refined-record identical, which is
  precisely the class §3.1 exempts.  They carry **no descent
  content**, and the receipt now exhibits a genuine positive
  record-cylinder measure that fails this same wider test
  (DC1-R(f)).  DC1(a) is not by itself a descent test.

Every count below is over **ORDERED** pairs (the ratio defect `d`
inverts under the swap, so an unordered census would depend on which
element the enumeration calls `a`).

**The census is EXHAUSTIVE over every parent of the family — the
deepest level included in full.  Nothing is sampled.**

| category | ordered pairs |
|---|---|
| ordered pairs `(a, b)` of distinct menu events | **794,570** (= 2 × 397,285 unordered) |
| NEITHER order admissible (mutual exclusion) | 129,284 |
| exactly ONE order admissible (admissibility asymmetry) | **0** |
| both orders admissible | 665,286 |
|  … of which `sigma(Hab) ≠ sigma(Hba)` (non-commuting, excluded by name) | **0** |
|  … of which **σ-COMMUTING** (the pin's coarse class) | 665,286 |
|  …  … identity HOLDS / FAILS | 576,654 / **88,632** |
|  … of which **REFINED-RECORD IDENTICAL** (Theorem 1's own hypothesis) | **425,334** |
|  …  … identity HOLDS / FAILS | 393,078 / **32,256** |
|  … σ-commuting but NOT refined-identical (§3.1 exempts) | 239,952 |
|  …  … identity FAILS (no descent content) | 56,376 |

Per parent depth `[ordered pairs, commuting, defects]`:
`0: [30, 26, 0]`, `1: [140, 124, 24]`, `2: [832, 656, 192]`,
`3: [4672, 3648, 864]`, `4: [24416, 19744, 3456]`,
`5: [124992, 103744, 14976]`, `6: [639488, 537344, 69120]`.

**What the census is evidence FOR — its actual information content.**
By (H1) and (H2) every quantity in the DC1 census is a function of
`(sigma(H), renamed a, renamed b)`, so the 794,570 ordered pairs
collapse onto the pair classes of the 36-state chain.  Computed
independently from one representative history per state (DC1(i)):

```
  sum over the 36 states of m(m-1)                    = 720
     ... both orders admissible (sigma-commuting)     = 616
     ... neither order admissible (exclusive)         = 104
     ... exactly one order admissible                 =   0
  ordered pair classes found by the exhaustive sweep  = 616  (0 splits)
```

So **every class is realised inside the depth-6 family, the census
carries 720 class-level facts, and the 794,570 pairs are ~1,100
instances of each.**  The multiplicity is replication, not
independent confirmation.  This is not a weakening: it is what makes
the all-depth reading available at all (see residue 4).

**Three census facts that were open before the run and are worth
naming on their own:**

* **Admissibility on a menu pair is SYMMETRIC** — zero asymmetric
  pairs.  Either both orders run or neither does.
* **The menu is NOT all-concurrent.**  129,284 ordered pairs are
  *mutually exclusive*: `{('p','p'): 33,338, ('r','r'): 31,304}`.
  The shortest witness is at the root — `p_A(v0,0)` and `p_A(v0,1)`
  cannot follow one another in either order, because
  `prop_options_in_view` refuses a base already carrying the actor's
  live proposal.
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
   ratio spectrum `{1: 665286}`, zero exceptions (DC1(b)).  **The
   entire defect lives in the normalisation.**  Stronger, and now
   gated (DC1-R(i)): the raw path weight `q(h) = Π q` is constant on
   **all 5,548 record classes** of the family, so the unnormalised
   weight is a *function of the record*.  It is **not a measure**: it
   is not additive along cuts — the cut masses are
   `1, 2, 4, 257/32, 1037/64, 2101/64, 68313/1024` — which is exactly
   why a completion is needed at all.
2. **The defect is exactly the intermediate-mass ratio.**  For every
   commuting pair, `d = M(sigma(Hb)) / M(sigma(Ha))`, with `M` the
   per-state menu mass — a function of sigma alone (gated in N4, now
   an anchor: zero mass-splitting classes; 34 states of mass 2 and 2
   states of mass 5/2, the two values read off d44a's committed SB2
   row-sum line, never typed in).  Zero exceptions on 665,286 pairs
   (DC1(c)).  **The defect is the coboundary of a function of sigma:
   a mass-ratio cocycle and nothing else.**
3. **Spectrum:** `{1: 576654, 4/5: 44316, 5/4: 44316}` — exactly the
   ratio set of the two masses, and symmetric as it must be under the
   ordered census.
4. **It is a function of `(sigma(H), class(a), class(b))` alone**
   (DC1(d)) — 616 classes under each of two ordered key resolutions,
   zero splitting classes under either.  *[COROLLARY of DC1(c) +
   N2(b): given `d = M/M` and given that `sigma(Ha)` is a function of
   `(sigma(H), renamed a)` — CG3a, re-gated in N2(b) with 176 keys
   and zero double successors — this cannot come out otherwise.  It
   is printed for the class COUNT, which is the census's information
   content.]*  Because a class fixed by an automorphism swapping `a`
   and `b` receives both `d` and `1/d`, this simultaneously forces
   `d = 1` on every self-swapped class.
5. **It vanishes exactly on the same-mass subclass.**  Same-mass
   intermediates: `{1: 576654}`.  Mass-mixed: `{4/5: 44316,
   5/4: 44316}` — a defect *everywhere* (DC1(e)).  *[COROLLARY of
   DC1(c): `M/M = 1` iff the masses agree.]*
6. **It is confined to 6 of the 36 sigma states**, of which two are
   the mass-5/2 states.  *[ENTAILED, not an independent localisation:
   given DC1(c) and a two-valued mass, a state defects **iff** its
   menu contains two events leading to states of different mass.]*
7. **By ordered pair class**, `(n,n)`, `(p,p)` and `(r,r)` pairs never
   defect; the defects sit at the mixed-tag classes.  *[Consequence of
   item 5.]*

**The witness, at depth 1** (`H = [p_A(v0,0)]`, `a` = A's self-arb,
`b` = `p_B(v0,1)`): `q(a|H)=1/4`, `q(b|Ha)=1/8`, `q(b|H)=1/8`,
`q(a|Hb)=1/4` — raw products identical at `1/32` — but
`N(Ha) = 2` while `N(Hb) = 5/2`, so `d = 5/4`.  This is the d42b3
G-T2 witness pair, seen from the descent side: the mass jumps from 2
to 5/2 exactly when the blind conflict group becomes visible in the
join view (the quarter law's excess).

---

## 2. What DC1's failure does and does not say

**It says (exactly this, and no wider):** *at this scope, there is no
positive measure on refined record cylinders whose conditionals are
the generated law's normalised menu kernel.*  This is paper 29
Theorem 1's **contrapositive**, applied to a conditional system that
satisfies every one of Theorem 1's hypotheses — all displayed
conditioning cylinders positive (DC3(4): 179,782 menu entries, zero
non-positive, smallest weight 1/8) and a **common refined cylinder**
(DC1(f), 16,128 unordered refined-identical failing squares) — and
still has unequal products.  **The carrier of this sentence is
DC1(f), not DC1(a).**

**It is NOT an F1 hit.**  F1 asks for *a positive refined cylinder
measure* with unequal conditional products; Theorem 1 forbids that,
and Theorem 1 is a theorem.  What is exhibited here is a **conditional
system that is not induced by any such measure**.

**It says nothing about the action line.**  No claim is made or
implied that the action line's conditional measure is the same
measure, or a different one, or related to this one.  The map is an
*identification problem*, not an existence problem, and this unit did
not touch it.

**It does not retract the closure theorem, (H1), (H2), or the
six-state chain.**  Those are statements about the *admissibility and
weight* law; DC1 is a statement about the *normalised* law's descent.

---

## 3. The completion corollary, and **the repair space**

**[PROOF — two lines, from two gated ingredients.]**  The hypothesis
the proof uses is exactly one equation:

```
        Z(Hab) = Z(Hba)      for every commuting pair.
```

Given it, both displayed products telescope,

```
    P_Z(a|H)·P_Z(b|Ha) = q(a|H)·q(b|Ha)·Z(Hab)/Z(H),
    P_Z(b|H)·P_Z(a|Hb) = q(b|H)·q(a|Hb)·Z(Hba)/Z(H),
```

and the two right-hand sides are equal: the raw products agree by
**DC1(b)** (gated, zero exceptions on 665,286 pairs), and the two `Z`
values agree by hypothesis.  A completion factoring through
`(depth, sigma)` satisfies that hypothesis, because `|Hab| = |Hba|`
and `sigma(Hab) = sigma(Hba)` *is the definition of the commuting
class*.  ∎

**The proof is an IMPLICATION, and `(depth, sigma)`-factoring is one
sufficient condition among many.**  The first delivery of this unit
read it as an equivalence and wrote that the completions the
dichotomy line forced are *precisely* the objects that repair
descent.  **That is false in both directions, and the receipt now
measures by how much (DC1-R).**

### 3.1 The repair space, exactly

Truncate at depth `D`; let `Z` be free and positive on the depth-`D`
histories and extend it downward by the completion recursion
`Z(h) = Σ_e q(e|h) Z(h+e)` (d42b3's own gradient construction — it is
what makes `P_Z(e|h) = q Z(h+e)/Z(h)` a normalised kernel).  Then
"repairs the defect" and "descends to the record" are two *different*
linear systems, both solved exactly over **Q** (sparse rational
elimination; no modular shortcut, no float):

```
  D = 4 :  free variables (depth-4 histories)        976
           repair constraints Z(Hab) = Z(Hba)        403   EXACT rank 403
           dim of the POSITIVE REPAIR CONE                   = 573
           dim of the (depth, sigma) family inside it        =  28
           dim of the record-constant (descending) family    = 313
           dim of REPAIRS THAT ALSO DESCEND                  = 205
           repair rows NOT implied by record-constancy       = 152 of 403
             (= exactly the rows whose two corners carry different records)

  D = 5 :  variables 5280, repair constraints 2227, EXACT rank 2227
           dim repair cone 3053   vs  (depth, sigma) 32,
           record-constant 1138          — the gap WIDENS with depth
```

`Z ≡ 1` solves both systems, so each solution space meets the
positive orthant in an **open** cone: every dimension above is a
dimension of strictly positive completions.  The `(depth, sigma)`
family is a 28-dimensional slice (each of its basis vectors verified
against all 403 repair equations — the corollary, instantiated),
leaving **545 independent directions of strictly positive repairs
transverse to the corpus's family**.  That slice sits *inside* the
descending sub-cone, and the containment is gated rather than
assumed: record identity implies σ identity — **0 of the 5,548**
record classes carries two σ values, a property of *this* record
functor (residue 3), not a general fact.

**Two exact witnesses, both strictly positive, both reconstructed
inside the receipt by deterministic constructions (not imported):**

* **(i) repairs, does not descend** (DC1-R(e)).  `Z = 1 + v/100` with
  `v` the first kernel direction of the repair system that is not
  record-constant (read off the exact echelon, scaled to `max|v| =
  1`): strictly positive, **zero** violations of all 403
  commuting-square identities, and **two record classes (of sizes 4
  and 6) carrying two different `μ_Z` masses each**.  So `P_Z` repairs
  every square the census tests while `μ_Z` is *not* a function of the
  record: there is no record-cylinder measure behind it.
  *"Annihilates the defect" does not imply "repairs descent".*  (The
  exact violation counts are a property of which kernel direction is
  taken — the referee's own witness of this shape reported four
  broken record-constancy equations with a size-4 class.  The verdict
  is direction-independent.)
* **(ii) descends, does not repair** (DC1-R(f)).  `Z = 1` on the
  boundary cut except on one record class set to `101/100`, extended
  by the same recursion: `μ_Z` is a strictly positive measure on
  refined record cylinders (constant on all 427 record classes of
  depth ≤ 4, additive along cuts by the recursion) — and it violates
  σ-commuting square identities.  232 of the 313 single-class
  perturbations break at least one, and **16** of them reproduce the
  round-1 referee's own witness **exactly** — the receipt exhibits the
  first in its deterministic scan:

  ```
    H = ()   a = ('p','B',v0,1)   b = ('n','B')
    P_Z(a|H) P_Z(b|Ha) = 39003/1659203
    P_Z(b|H) P_Z(a|Hb) =   3000/127631     (sigma equal, RECORDS DIFFER)
    ratio 13001/13000; squares broken: 2
  ```

  (The referee printed the same construction at another pair of the
  same shape — a propose at the root and that same actor's idle — with
  the same two products, the same ratio and the same verdict.)

  *"Repairs descent" does not imply "annihilates the defect"* — and,
  since the offending pair's two records **differ**, this is also the
  direct evidence that DC1(a) is not a descent test (§1).

### 3.2 The hierarchy, and what selects the corpus's completion

```
   repair cone (573)  ⊃  repairs that also descend (205)  ⊃
   (depth, sigma) family (28)  ⊃  depth-stationary form (1 ray = D49's Ẑ)
```

**The object that collapses 573 → 1 is D50's FORM choice, not
descent.**  That was already the note's own price paragraph ("the
stationary FORM of `Z` is a CHOICE"); the number now says how much
the choice buys.

**And the corpus's completion really does descend — now gated
(DC1-R(h)), where the first delivery only asserted it.**  For the
transfer operator `(T f)(s) = Σ_e q(e|s) f(s·e)` on the 36 states:

```
  ker(T - 2I) : dim 1, generator STRICTLY POSITIVE, values {1, 4/3, 7/3}
                with multiplicities {29, 5, 2}   (= D49's f = (4,4,3,7,3,3)/3)
  ker(T - I)  : dim 1, MIXED SIGNS   (no depth-ungraded completion of this form)
  ker(T - 5/2 I), ker(T - 9/4 I) : empty
  Ẑ(h) = 2^-|h| f(sigma(h)) :  harmonicity violations 0 (all depths of the family)
  mu_Ẑ = q·Ẑ constant on record classes :  0 splits of 5,548
```

So `Ẑ` is a positive λ = 2 harmonic completion whose measure **is** a
function of the record: genuine descent, and an extra fact, not a
corollary of the two lines (by witness (i), the square identity does
not imply it).

**d42b3's gradient completion is not "an independent completion of a
different shape".**  It is `Z ≡ 1` at depth 4 pulled back by the same
recursion, and it factors through `(depth, sigma)` — 64 occupied
`(depth, sigma)` cells, **zero** carrying two values — so its
zero-failure result (DC1-C) is an **instance of the corollary**, not
independent evidence for it.  It is kept for its two d42b3 anchors,
now both re-derived: `Z(∅) = 1037/64`, which is *exactly* the depth-4
raw cut mass (so it certifies that the recursion ran), and the
deformation census (interior 215, interior cut classes 114, deformed
21, root included).  Its domain is the **39** parents of depth ≤ 2 —
403 unordered commuting pairs = 806 in this note's ordered unit, of
which 251 are refined-record identical and 152 are not.

**The meeting of the two lines, stated at its true strength.**  The
descent defect names the **job** a completion has to do, and the
corpus's completions are **among** the objects that do it (and `Ẑ`'s
measure genuinely descends).  It does **not** single them out.  The
successor question sharpens to: *is there any record-level demand
that cuts the 573 down to the 28, or is the completion family
selected only by the stationary form?* — which is D50 again, now with
a number attached.

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
  **zero** carrying two different renamed menus, 34,375 histories
  swept (DC2(a) — the only falsifiable gate of the three);
* the **36-row normalised kernel `K(·|sigma)` printed in full**,
  exact `Fraction`s;
* every history's normalised renamed menu equals its printed row
  (DC2(b) — *corollary of DC2(a); it can only fail if DC2(a) does*);
* every row sums to exactly 1 (DC2(c) — *reporting-only, cannot
  fail*: it is division by the row's own mass).

---

## 5. DC3 — the five durable-record hypotheses (paper 29 §4.3)

| # | hypothesis | label | verdict |
|---|---|---|---|
| 1 | exclusive & exhaustive durable alternatives (gated as: enumeration completeness of `candidates_for` against `admissible`) | **SUBSTANTIVE** | **PASS** |
| 2 | decoherence of the queried record algebra | **REPORTING-ONLY** | trivially satisfied, **uninformative** |
| 3 | one common refined cylinder | **= DC1(a), same predicate** | **FAIL** |
| 4 | positivity of every displayed conditioning cylinder | **SUBSTANTIVE** | **PASS** |
| 5 | sufficient declared boundary | **RESTATEMENT (= DC2(a))** | satisfied |

**(1)** is a real two-sided gate, with its scope now stated exactly:
the adversarial pool — **718,570** events over the tokens each history
has uttered, plus **22,762** on the unrestricted surface at depth ≤ 4
— is built independently of `candidates_for`, but the *verdict* on
each pool event is d42b3's own `admissible`, which `candidates_for`
also calls.  So what the gate establishes is **enumeration
completeness and non-redundancy of `candidates_for` against
`admissible`** — zero duplicates, zero omitted admissible events,
zero refused-but-listed, zero weight disagreements — and not the
grammar's exclusivity in any sense independent of the layer.

**(2)** holds *for the empty reason*.  The generated law is a
classical stochastic process on records, so its decoherence
functional is diagonal by construction.  **This is where the map's
remaining segment lives, and the receipt says so in the output.**
Paper 29's hypothesis (2) is a condition on class *operators* and
their Gram functional (§4.1–§4.2).  The generated line **has no
functional level at all** — and **this unit does not build one**.
That segment is exactly where D59's *record instrument* and paper 29
§9.2's *preferred durable algebra* still sit.

**(4)** is substantive — a single zero weight would make a displayed
conditional undefined and would void DC1's test on that pair.  Every
menu weight is a strictly positive exact `Fraction` (179,782 entries,
smallest 1/8), every mass positive, and the support is exactly the
admissible set by (1).

---

## 6. DC4 — D59's six supplied-not-derived items, re-scored

**No item moves.**  (Round-1 MAJOR 2: the first delivery moved item 1.
It should not have.)

| # | item | verdict |
|---|---|---|
| 1 | boundary state | **stands** — it is the action line's slot |
| 2 | measure and contour | stands; **now priced with a number** |
| 3 | renormalization | stands; untouched |
| 4 | record instrument | stands; DC3(2) says why it cannot move |
| 5 | generated record grammar | stands *for the action line*; never supplied on the generated line |
| 6 | clock dictionary | stands; untouched |

**1. Boundary state — STANDS.**  D59's six items are quoted from
paper 29's abstract, where the possessive is the *identified* law's:
the corpus supplies rather than derives **its** boundary state, and
§9.2's slot table names the object — "boundary/cosmological state —
selects amplitudes and long-range correlations".  The generated line's
`sigma` was never on that list, so it cannot move *on* that list; item
5 has exactly this shape and is scored the same way.  **The positive
statement belongs beside the ledger, not on it:** on the generated
side the declared boundary statistic is *not supplicated* — `sigma`
is **constructed** from the committed layer, its sufficiency is
(H1) + (H2), and the 36-row kernel is printed.  The generated line has
a **derived boundary statistic**; D59's item — the action line's
boundary/cosmological state — is untouched by every gate here.  *This
costs the unit nothing real: the theorem content survives verbatim.*

**2. Measure and contour — stands, and DC1 sharpens exactly why.**
The generated law has an order-independent unnormalised weight
(DC1(b)) and a normalised kernel that is *not* order-independent
(DC1(f)/DC1(a)); the gap is the coboundary of the state-mass function
(DC1(c)).  A measure on record cylinders therefore requires a
**completion** — supplied data, whose form D50 already showed is a
choice.  Now **priced with a number** (§3): the repair cone is
573-dimensional at the depth-4 truncation, 205 of those dimensions
also descend, 28 are the `(depth, sigma)` family, and the selection
down to one ray is the form choice.

**3. Renormalization — stands.**  No gate here concerns a continuum
limit, a regulator or a scale.

**4. Record instrument — stands.**  DC3(2) is reporting-only; the
generated line cannot derive which alternatives decohere or which
algebra is queried, because it has no functional level.  DC3(1)
establishes something narrower and worth keeping distinct: a record
**grammar** fact, not a record **instrument** fact.

**5. Generated record grammar — stands for the action line.**  The
d42a grammar exists and this unit gated its enumeration completeness
(DC3(1)) and its boundary sufficiency (DC2) — but **nothing here
connects it to D15 action content**.  Paper 29's Theorem 5 is
untouched.

**6. Clock dictionary — stands.**  No gate produces a rate, a unit or
a time coordinate.

---

## 7. Licensed claims — and the ones this unit forbids

**Licensed, at two-actor delivery-free d42a scope on the exhaustive
depth-6 family:**

1. The generated law's normalised menu kernel **fails** the
   commuting-square identity on **32,256 of 425,334
   refined-record-identical ordered pairs** (the load-bearing test),
   and on 88,632 of 665,286 σ-commuting ordered pairs — of which
   56,376 lie outside Theorem 1's hypothesis and carry no descent
   content.
2. The failure is **exactly** `d = M(sigma(Hb))/M(sigma(Ha))` — the
   coboundary of the per-state menu mass — with zero exceptions; it
   is a function of `(sigma(H), class(a), class(b))`; it vanishes on
   same-mass intermediates and occurs at every mass-mixed pair; it is
   confined to 6 of 36 states.  The evidential content of that census
   is **720 class-level facts** (616 commuting + 104 exclusive), each
   replicated ~1,100 times by the exhaustive sweep.
3. The **unnormalised** weight satisfies the identity everywhere, and
   is constant on all 5,548 record classes — it is **order-independent
   and a function of the record**, but it is **not a measure** (the
   cut masses `1, 2, 4, 257/32, …` are not conserved).
4. Consequently **no positive measure on refined record cylinders has
   the generated normalised kernel as its conditionals** at this
   scope.
5. **The defect is repairable, and the repair space is large.**  At
   the depth-4 truncation the positive repair cone has dimension
   **573**; the completions that *also* descend form a **205**-
   dimensional sub-cone; the `(depth, sigma)` family the dichotomy
   line forced is a **28**-dimensional slice of it; D49's `Ẑ` is one
   ray inside that slice.  Square-repair and descent imply each other
   in **neither** direction (two positive witnesses).  The corpus's
   completions are **among** the repairs; the selection down to `Ẑ`
   is **D50's form choice, not descent**.
6. **D49's `Ẑ` genuinely descends**: it is the unique (up to scale)
   positive λ = 2 harmonic completion of its form, and `μ_Ẑ = q·Ẑ` is
   constant on all 5,548 record classes.
7. `pi = sigma` is a sufficient declared boundary and the 36-row
   kernel exists and is printed — **as a restatement of (H1)+(H2)**.
8. Hypotheses (1) and (4) of paper 29 §4.3 hold on the generated law;
   (2) holds vacuously; (3) fails; (5) is (7) above.

**Where the independent evidence actually sits.**  Of the receipt's 42
gates, the falsifiable ones are: N0(a)–(e), N1, N2, N2(b), N3, N4, N5
(the provenance and anchor block), **DC1(a)**, **DC1(b)**, **DC1(c)**,
**DC1(f)**, **DC1(i)**, **DC1-R(a)–(i)**, DC2(a), DC3(1), DC3(1′),
DC3(4).  The rest are labelled in the receipt for what they are:
*corollaries* of a gate that implies them (DC1(d), DC1(e), DC1-C,
DC2(b)), *reporting-only / cannot-fail* lines (DC1(g), DC1(h),
DC2(c), DC3(2), DET(a), DET(b), DC4), and *the same predicate counted
twice* (DC3(3) = DC1(a), DC3(5) = DC2(a)).  A reader wanting the
unit's evidence should read the first list.

**Explicitly NOT licensed (do not quote):**

* anything about the identified/action-line click law, its measure, or
  whether it is "the same measure" — the map is untouched;
* "the completions the dichotomy line forced are **precisely** the
  objects that repair descent" — **false in both directions** (§3);
* "the generated law descends to a record measure" *without* the
  completion clause and its D50 price;
* "the generated law does not descend" *without* the normalised/
  unnormalised distinction — the unnormalised weight is
  order-independent (though it is not itself a measure);
* "the unnormalised weight descends to a record measure" — it does
  not; it is order-independent and record-constant, and not additive
  along cuts;
* D59's boundary-state item as **moved** — it stands;
* the 88,632 figure as the descent failure count — the descent
  failure count is 32,256 on 425,334;
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
   record functor changes which pairs are in DC1(f)'s subclass.  The
   containment (refined ⊆ σ-commuting) holds because `canon`-identity
   implies σ-identity — verified for **this** functor (0 σ splits over
   5,548 classes) and *not* a general fact: a coarser functor need not
   have it, and then DC1(f)'s class need not sit inside DC1(a)'s.
4. **Depth — now mostly discharged, and precisely.**  The class-level
   census (§1) is *complete*: `720 = 616 + 104 = Σ m(m−1)` over all 36
   states, with every class realised in the family.  With (H1) + (H2)
   that reduces the all-depth statements of DC1(b) and DC1(c) to a
   finite check over the 616 commuting classes — which is exactly what
   the receipt ran.  **What actually remains** is a
   renaming-composition lemma: that "`b` renamed at `Ha`" is a
   function of `(sigma(H), renamed a, renamed b)`, i.e. the
   well-definedness of `canon_pair2`, which N5 gates only on the
   diagonal at depth ≤ 2 (the family-wide evidence is the agreement of
   the two independent key resolutions).  Note also that DC1(b) does
   **not** follow from (H1)+(H2): the raw cocycle is a fact about the
   weight layer, and it is the class-completeness argument that
   carries it to all depths.
5. **The repair space beyond the truncation.**  573 and 3,053 are
   dimensions at the depth-4 and depth-5 truncations.  A depth-free
   statement of the repair cone (and of whether any record-level
   demand cuts it to the `(depth, sigma)` family) is the successor's
   obligation — the sharpened form of D50.
6. **Three actors, transport** — out of scope, as always.

---

## 9. What round 1 changed

The round confirmed the arithmetic in full ("every single number
reproduces", including an independent rebuild of the family, the state
partition, the record functor and the pair keys) and added two facts
in the unit's favour, both now gated here: the raw path weight is
constant on all 5,548 record classes, and D49's `Ẑ` is a real positive
λ = 2 harmonic completion whose measure descends.

| # | finding | disposition |
|---|---|---|
| BLOCKER 1 | the repair space was never computed; "precisely" is false in both directions | **repair space computed and gated** (DC1-R(a)–(i)); the hierarchy 573 ⊃ 205 ⊃ 28 ⊃ 1 printed; both witnesses reconstructed; the claim withdrawn and inverted |
| MAJOR 1 | the headline tested a hypothesis §3.1 exempts | headline is now DC1(f) (32,256 / 425,334); the wider census is context, with its 56,376 exempt failures named |
| MAJOR 2 | the ledger's boundary-state move conflated two objects | item 1 **stands**; `moved == 0`; the generated line's derived statistic stated beside the ledger |
| MAJOR 3 | "three FAILs, one finding" | **two statements**: DC1(a) (= DC3(3)) and DC1(f) |
| MAJOR 4 | "two gated instances" are one shape; twelve PASSes cannot fail | DC1-C relabelled an *instance* of the corollary; every entailed / tautological / constant gate relabelled; the independent-evidence map is §7 |
| MAJOR 5 | the census's information content | 720 class-level facts gated (DC1(i)) and stated beside the pair count; residue 4 re-stated and mostly discharged |
| MINORs 1–8, NITs 1–3 | wording, scope, anchors | title corrected (order-independent, not "descends"); `Ẑ`'s descent gated; DC1-C's domain/orientation/anchors stated; VERDICT prose predicate-guarded; N3/N4 made anchors and CG3a re-gated (N2(b)); "6 of 36" marked entailed; DC3(1) relabelled; N5's depth and narrowness stated; `Z(∅)` identified as the depth-4 cut mass with a second anchor added; residue 3 scoped |

Everything the round did **not** contest — the defect structure, the
exhaustive census, the witnesses, the F1 refusal, the scope discipline
and the pin's pre-registration — stands unchanged.
