# SMU (paper-27) — K2 EFFECTUS-LENS HOSTILE REVIEW

**Seat:** K2 (EFFECTUS — claims, licensure, registers, the forward road).
**Protocol:** v14 ledger #235, row K2.
**Object, hash-verified at open and at close (all five match the ledger):**

| object | pinned | measured |
|---|---|---|
| `v14/paper-27-smu.md` | `d14689919289` | `d14689919289` |
| `v14/code/smu_exact.py` | `394cbfca621c` | `394cbfca621c` |
| `v14/code/smu_output.txt` | `0bf6cc0502e6` | `0bf6cc0502e6` |
| `v14/code/smu_receipt.json` | `808aca088ff6` | `808aca088ff6` |
| `v14/note-smu-pin.md` (pin) | `a1fca5e7b238` | `a1fca5e7b238` |

Working tree copies are byte-identical to the objects at 6d8582e. No sibling's
uncommitted state was read.

**GRADE: AWF — ACCEPT WITH FIXES.**
**~131 seat recomputations. ZERO delivered numbers moved.** Every published
number this seat could reach reproduced exactly: the four spreads at both
denominators, all 20 cells of the §6 table, all 12 Wilson rows (reduced to
three sector averages and re-predicted), the 55-target enumeration, the
inherited parent masses at 12 of 12 cells, the fibre inventory, the anchor and
gate totals, and the verdict string at paper = output = receipt. **No finding
below is a false number.** All four MAJORs are licensure findings: claims the
measurements do not carry as stated, in a unit whose measurements are sound.

The head word **`SMU-DYNAMICS-RELATIVE` survives.** Its comparative clause,
its privilege claim, half of its price clause and one of its self-descriptions
do not survive as written.

---

## 1. THE PRIVILEGE QUESTION (decisive — the QCD road hangs on it)

### 1.1 What the instrument actually declares

`smu_exact.py:1713-1729`. For each of the six sector→position assignments the
transition law is built as

```
    P = [dict(enumerate(tgt)) for _ in range(n)]
```

— **every row of the law-native chain is the same vector `tgt`.** The kernel is
rank one. Its unique stationary measure is `tgt` itself, identically, for any
`tgt`; no property of this arena, of the Γ-triple, or of the carrier enters.
The exact solve at 640 states recovers a vector that was written down before
the solve began.

This is not a defect of the computation — the paper says plainly that the step
"discards the current coin and draws a new one" — but it settles the privilege
question, and it settles it harder than the ledger's framing anticipated. The
question was posed as *rate motivated / construction declared*. The measured
answer is: **the construction is declared, and the dynamics does no work at
all.** What is "derived" is the draw law read back.

### 1.2 The three declared ingredients, in order of severity

1. **The cross-arena identification (unpinned; the real blocker).** Paper-16's
   triple `(15/38, 5/19, 13/38)` is a law over the *transport law's three
   positions*, at carrier-free scope (`paper-16` head:
   `TARGETS=HIT-AT-THE-LAW-VALUES-AT-CARRIER-FREE-SCOPE`, leg-independent,
   step-normaliser law-native under an arbitrary re-pricing). SMU identifies
   those three positions with R5's three **coin sectors**
   (DIAGONAL/ANTIDIAGONAL/BALANCED). Nothing pins that identification. It is
   the same object paper-23 measured and found empty: candidate (a),
   `PUSHFORWARD=NO-PINNED-CORRESPONDENCE-TO-THIS-ARENA (WELD2 120 rows, 60
   distinct candidates, 0 found at this carrier)`. The unit's §11 frames the
   open question one level too shallow — as "whether the sector-to-position
   assignment can be forced" (fibre 6) — when forcing an assignment *between*
   two 3-element index sets presupposes that the two index sets have been
   identified at all, which is precisely the 0-found row.
2. **Which sector carries which position** — fibre 6, all six built, measured
   verdict-determining, and measured to move the answer the most: the
   DEFECT-CARRYING mass runs 15/76 → 45/152 across this axis, and the head's
   own widest spread is attained between a member of this fibre and the
   counting measure.
3. **Uniform inside each sector** — declared, with no argument offered. Note
   what it is: the counting measure, reused inside the grading, i.e. the
   parent's own declared null re-entering as an unexamined ingredient of the
   candidate that is supposed to beat it.
4. **State-independence** — the rank-one fact of §1.1.

### 1.3 The internal inconsistency this exposes

§9 demotes the Metropolis rows in explicit terms:

> Both orbit-uniform nulls are also reached, but by chains built *from* those
> measures: that is the surjection of section 7 and not a second derivation,
> and the paper counts it as pricing rather than as evidence.

The law-native chain is the **same species, more extremely**: Metropolis at π
is a chain whose stationary measure is π; the resampling chain at π is a chain
whose every row *is* π. By the criterion §9 applies to (f), family (c) is
pricing and not evidence too. The paper instead lists it under "Decided" as
"**a new measure is derived** by the law-native resampling" and §11 calls it
"the only candidate in this census with a claim to be more than a
declaration." That claim is not wrong in substance — the *numbers* did come
from a confirmed law and nobody chose them as a measure — but it is carried by
the wrong noun. The content is a **transported law value**, not a derivation
by dynamics.

### 1.4 THE RULING — the honest form

> **`LAW-VALUED-RATE / IDENTIFICATION-DECLARED / CONSTRUCTION-DECLARED /
> DYNAMICS-INERT`**
>
> Short form for the head and for ACT's inheritance:
> **`LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`.**

`LAW-RATED-CONSTRUCTION-DECLARED` alone is **too generous** and this seat does
not license it: it implies the dynamics contributes the measure and the law
contributes the rate, whereas the dynamics contributes nothing and the law
contributes three numbers whose route onto this carrier is unpinned.

### 1.5 What would upgrade it to DERIVED — exactly

- **Route A — the only route on which "law-native *dynamics*" would mean
  anything: a pinned correspondence.** Find a correspondence from the
  Γ-iteration's carrier to R5's configurations and push Γ's own kernel
  forward; then the chain, not only its three numbers, is law-native, and its
  stationary measure is derived. **Status: BLOCKED at a named, measured
  object** — paper-23's row (a), 0 found at this carrier, all 8 found rows in
  the corpus dying at the same site-count blade (9 sites against 16).
  Additionally, even granted a correspondence, Γ's law is column-stochastic
  **between cut spaces** (`102 of 102 columns over 10 cut pairs`), not an
  endomorphism of one carrier; the Markov object in that unit is the *history*
  chain ("the history chain is Markov by construction"). **So Γ's own kernel
  does not canonically induce a chain on the coins — the answer to the
  ledger's second sub-question is NO, twice over: no correspondence, and no
  endomorphism even with one.**
- **Route B — force ingredients 2–4 by argument.** Even if fully successful,
  the chain stays rank one, so what would be derived is a **measure by
  transport**, not a measure by dynamics. Worth doing; worth not calling a
  dynamics.
- **Route C — the one the QCD chain is actually chartered for: an action.**
  Gibbs is the measure source that needs no dynamics at all, and paper-23
  killed it only conditionally — `(f) GIBBS = NO-ACTION-NO-COUPLING-BY-THE-
  PARENTS-OWN-DECLARATION`. ACT is chartered to supply exactly the missing
  object. If ACT supplies an action, the measure follows without any dynamics
  declaration, and §7's surjection becomes a *tool* rather than a *price*.

### 1.6 ACT's INHERITANCE ROW (write this into the successor register)

> **ACT inherits the law-native π as the leading candidate and inherits it
> stamped.** `LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`,
> sector-graded at (15/38, 5/19, 13/38), invariant, a point of paper-23's
> simplex — the first point of that simplex anything in the corpus has
> supplied, and supplied by transport, not by dynamics. Inside the
> conserved-price frame it is **one declared point of a 207-dimensional
> simplex whose every point is reachable by a covariant irreducible chain**;
> its privilege over the other 207 numbers is that three of its numbers came
> from a confirmed law, and its debt is the identification that put them here.
> **ACT must not treat it as a derived measure, and must not spend it as one.**
> The honest use is as a *control*: whatever measure an action supplies,
> compare it to the law-native point and report the distance. If they agree,
> that agreement is the first real evidence in this arena; if the action route
> dies, the law-native point is what the programme has, at its stamp.

---

## 2. THE CONSERVED-PRICE SENTENCE — LICENSURE

**"The declaration was relocated, not removed."** This is the unit's best
sentence and this seat licenses it — with two boundaries, one of which is a
MAJOR.

### 2.1 What is proved

The Metropolis construction is uniform in its target: at a **full-support**
target π that is orbit-constant, the uniform-proposal chain is π-reversible
(so π is stationary), irreducible (so π is unique), and covariant (the uniform
proposal is permutation-invariant, and orbit-constancy of π makes the
acceptance ratio equivariant). That is a genuine theorem, arena-independent,
requiring only a finite carrier, a symmetric irreducible proposal and a group
action. This unit instantiates it at 3 declared targets and verifies it
**exhaustively** on a 4-state carrier at denominator 12: I re-enumerated the
target set independently — compositions of 12 into 3 positive parts,
`C(11,2) = 55` — and confirm **55, 0 failures**, and that every one of the 55
has full support by construction (`a,b,c ≥ 1`).

**This is the unit's exportable theorem, and this seat affirms it as such:**

> *A construction uniform in its target makes the dynamics fibre surject onto
> the very simplex the dynamics was supposed to select from. Relocating a
> declaration from a measure to a dynamics therefore conserves its dimension.
> What such a move buys is not a smaller price but a different place to argue.*

### 2.2 Boundary 1 — interior, not simplex (MINOR)

Every target reached is full support: the three real-carrier targets, and all
55 toy targets by the `a,b,c ≥ 1` enumeration. The reach is onto the **relative
interior**. §7 discloses this ("the reach is onto the simplex's interior and
onto its boundary only through the reducible arm"); the head does not. The
dimension count (207/119) is unaffected — the interior is full-dimensional —
so this is a MINOR with a one-token repair.

### 2.3 Boundary 2 — does non-covariance enlarge it? YES, and the unit
measures one point where it could state a corollary

The control is one instance: one non-invariant full-support target, reached
exactly, measured not orbit-constant and not gauge-covariant. But the theorem
of §2.1 is **silent about invariance except through covariance**: at *any*
full-support target, invariant or not, the same construction returns a chain
with that target as its unique stationary measure. Hence:

> **The full dynamics fibre surjects onto the interior of the whole 639-simplex.
> A bare dynamics declaration costs 639 numbers, not 207.**

The unit owns the qualitative version ("it is covariance, and not dynamics,
that confines the answer to the parent's object") but not the number. **The
price is conserved *only under a retained covariance declaration*; without it
the price rises by 432.** That is a free corollary of the unit's own theorem
and it sharpens the sentence into its final form:

> *The declaration was relocated, not removed — and it was relocated at equal
> price only because covariance was declared again on the far side. Dropped,
> the same move costs 639 numbers instead of 207.*

### 2.4 The scope in which the sentence is licensed

At the **chart-32 reading**, on the 640-configuration carrier, over covariant
irreducible chains with full-support stationary measures: **licensed exactly.**
The extension half is not (MAJOR-3 below).

---

## 3. DOES PAPER-23 NEED AN ANNOTATION? — RULING: **YES. A CORRECTION
ANNOTATION, NOT AN ERRATUM AND NOT A SCOPE ANNOTATION.**

### 3.1 The defect

Paper-23 carries, in its terminal head and again in its §4.10 body,

> `A-COVARIANT-CHAIN-DERIVES-IFF-IT-IS-IRREDUCIBLE`
> "...it fixes that point uniquely exactly when **irreducibility** supplies the
> transitivity the symmetry group does not."

The forward half is true. The converse is false: the stationary simplex has
dimension (closed classes − 1), so a chain with a transient class and one
closed class fixes a measure without being irreducible. SMU exhibits the
witness (3 states, 2 communicating classes, 1 closed, kernel dimension 1) and
verifies the dimension identity exhaustively over the 3-state support family —
I confirm the family size is `7³ = 343` and that it is exhaustive **for the
structural claim**, since the class decomposition and hence the kernel
dimension depend only on the support pattern.

### 3.2 Why the paper-12 precedent does not fit

`v14/note-paper12-scope-annotation.md` rests on **two different objects** —
padded eq-22 versus the rectangular feasibility problem — with the standing
formula "their claims were form-scoped and remain true at their own scope."
Here there is one object (finite Markov chains) and one statement, whose
biconditional is simply too strong. Calling it "true at its own scope" would be
inaccurate: paper-23 had **no chains at all**, so the scope in which its
biconditional is safe is empty. The R5 precedent (a *strengthening* note) does
not fit either — nothing is strengthened.

### 3.3 Why it is not an erratum

Nothing of paper-23's moves. No number, no verdict, no census row depends on
the criterion: it was the forward requirement attached to a **named-absent**
row, never applied. And SMU measures that on this census the two readings
coincide — 0 transient classes across all 18 instances — so the correction
does not disturb even the successor's verdicts.

### 3.4 THE REGISTER ROW

> **PAPER-23 TAKES A CORRECTION ANNOTATION, NOT AN ERRATUM.** Terminal paper
> untouched (paper-12 / R4 precedent for the *mechanism*; new species for the
> *ground*). Standing note, e.g. `v14/note-paper23-criterion-annotation.md`,
> registered by the SMU adjudication, saying exactly:
>
> 1. The inherited form is **sufficient and not necessary**. The sharp
>    condition is `EXACTLY ONE CLOSED COMMUNICATING CLASS`; the stationary
>    simplex has dimension (closed classes − 1); irreducibility implies one
>    closed class and not conversely.
> 2. The witness: 3 states, 2 communicating classes, 1 closed, simplex
>    dimension 0 — it derives, and it is not irreducible.
> 3. **Nothing of paper-23 moves**: the criterion was the forward requirement
>    of a named-absent row and was never applied to a chain; on paper-27's
>    census the two readings return the same 12 deriving instances (0 transient
>    classes at 18 of 18).
> 4. **Corpus-wide caution, in the paper-12 register's voice:** any unit that
>    inherits "derives iff irreducible" from paper-23's head is quoting a
>    biconditional whose converse fails, and must gate on the **closed-class
>    count**. Where the two coincide, say so and measure it (as paper-27 does);
>    do not assume it.

---

## 4. THE HEAD'S LICENSURE — THE SPREAD COMPARISON

### MAJOR-1 — `SO-DECLARING-A-DYNAMICS-MOVES-THE-PARENTS-OWN-HEADLINE-SETS-FURTHER` IS AN UNLICENSED INFERENCE

The ledger asked whether 153/380-vs-27/130 is apples-to-apples: same headline
sets, same denominators' meaning. **Sets: yes. Denominators: yes. Comparison
class: NO — and the failure is decisive.**

Measured, by this seat, from the receipt:

| check | result |
|---|---|
| paper-23's three measures present in SMU's census | **yes — all three**: counting (composition walk *and* Metropolis-at-counting), orbit-uniform chart-32, orbit-uniform chart-128 |
| their masses on the four headline sets | **identical at 12 of 12 cells** |
| paper-23's widest spread over its own three | **27/130** (recomputed) |
| **SMU's widest spread restricted to those same three** | **27/130 — exactly, no movement at all** |
| SMU's widest over 11 covariant deriving instances | 153/380 |

So the parent's comparison class is a **subset** of the successor's, and
max-over-a-superset ≥ max-over-a-subset is arithmetic, not physics. The
increase from 27/130 to 153/380 is produced entirely by the **six new
law-native measures** entering the same comparison — i.e. by a bigger census,
not by the dynamics-versus-measure distinction the sentence draws. Held at
fixed comparison class, **declaring a dynamics moved the parent's headline sets
by exactly nothing.**

The unit's own §7 and §8 make this sharper. Each headline set is a union of
orbits with non-empty complement, so the orbit point-masses are extreme points
of the invariant simplex at which its mass is 1 and 0. **The range of every
headline set's mass over the invariant simplex is exactly [0, 1]** — the same
argument §8 runs for the Wilson observable, applied to an indicator. Over the
covariant *irreducible* fibre it is the open interval (0, 1). So the
theorem-level answer to "how far can a declaration move these sets?" is
**everything**, and 153/380 is a fact about six declared instances, not about
what declaring buys.

**REPAIR (exact).**
- Head, PRICE/RELATIVITY segments: replace
  `AGAINST-THE-PARENTS-WIDEST-OVER-INVARIANT-MEASURES-27/130-SO-DECLARING-A-DYNAMICS-MOVES-THE-PARENTS-OWN-HEADLINE-SETS-FURTHER`
  with
  `AT-THE-PARENTS-OWN-THREE-MEASURES-THIS-CENSUS-REPRODUCES-27/130-EXACTLY|THE-RISE-TO-153/380-IS-THE-SIX-NEW-LAW-NATIVE-MEASURES-ENTERING-THE-SAME-COMPARISON-NOT-A-DYNAMICS-EFFECT|OVER-THE-WHOLE-COVARIANT-FIBRE-THE-RANGE-OF-EVERY-HEADLINE-SET-IS-[0,1]-BY-THE-SURJECTION`.
- §6: add the restricted-comparison row (27/130 reproduced) and the [0,1]
  theorem sentence; state that three of the four table columns are the parent's
  own measures.
- §9 "Decided" bullet "**The measure moves**, and the movement is priced on the
  parent's own sets, wider than the parent's own spread over invariant
  measures" → "...wider than the parent's own spread **over its own three named
  nulls**, and narrower than the [0,1] the surjection licenses."

**The head word is unaffected.** The measures do disagree (10 distinct vectors
over 12 deriving instances, verified entry by entry); `SMU-DYNAMICS-RELATIVE`
stands. It is the comparative clause that is unlicensed.

### MINOR-1 — the parent's number is described in a way that invites the [0,1] misreading

§6: "the parent's widest spread over invariant measures was 27/130." Read
plainly this claims a range over *the invariant measures*, which is 1. It is a
max over three named nulls. Repair: "over its own three named nulls." (Paper-23
carries the same looseness; correcting it here is enough — this is not a second
annotation, since paper-23's own §7 names its three measures in the sentence
before.)

---

## 5. THE WILSON SEGMENT AND THE [0,4] SENTENCE

### 5.1 Recomputed — and internally over-determined (12 rows → 3 unknowns)

I reduced the whole segment to three sector averages and re-predicted every
row. Solving from three rows only (LAW-NATIVE-012, LAW-NATIVE-021,
COMPOSITION-LEFT):

> **DIAGONAL average = 2, ANTIDIAGONAL average = 1, BALANCED average = 5/4.**

All six law-native expectations then predict exactly (225/152, 111/76, 205/152,
207/152, 107/76, 219/152 — 6 of 6). COMPOSITION-RIGHT and METROPOLIS-AT-COUNTING
both return 13/10. Independently: total observable mass over the carrier = 832;
the 64 singleton gauge orbits are exactly the DIAGONAL sector (confirmed twice —
the orbit profile `[[1,64],[4,144]]`, and the DIAGONAL mass under orbit-uniform
chart-32 being 64/208 = 4/13), which predicts the orbit-uniform chart-32
expectation as **19/13, exactly as published**. The full-trace offset is **12 =
16 − 4 at all 12 rows**, matching "the same quantity plus the untouched
identity". I also decomposed all four headline-set masses under the law-native
grading into integer sector intersections, and every one resolves exactly:
NON-FLAT = 56+64+512, NON-COMMUTING = 0+64+512, DEFECT-CARRYING = 0+0+384,
DIAGONAL = 64+0+0 — consistent with paper-23's abelian arm and its "Haar carries
0 of 384 defect coins".

**Verdict on the segment: sound, stamped, and licensed by the pin.** The
conditional stamp is enforced per row and to arbitrary depth, 12 of 12.

### 5.2 "Covariance pins the expectation nowhere" — LICENSED

Given the measured facts (observable orbit-constant; min 0 and max 4 each
attained on an orbit of size 1; those orbits extreme points of the invariant
simplex), the expectation's range over the invariant simplex is exactly [0, 4]
— the observable's entire range. The sentence is licensed as written. (The
min/max measurement itself is K1's row; every consequence of it that I could
reach is consistent.)

### 5.3 Its QCD implication — stated honestly, and worth stating harder

§8's closing is honest: "An expectation on this arena is not a number the arena
has; it is a coordinate of the declaration." The implication the successor
chain needs, and which the paper leaves implicit, is the sharp one:

> **Covariance constrains no expectation on this carrier at all — not weakly,
> not partially: the reachable range is the observable's full range.** So no
> Wilson number in this arena means anything until a measure arrives by a route
> that is not a declaration. Paper-23 closed eight such routes and left Gibbs
> alive only conditionally ("no action, no coupling *by the parent's own
> declaration*"). **ACT is therefore not one option among several: it is the
> only surviving route to an expectation with content, and POT's confinement
> gate is unaskable until it lands.** A second observable with a narrower range
> would be the first thing this arena hands over free (§11 already registers
> this — it should be flagged as the cheap falsifier it is).

---

## 6. THE CHART-128 OFF-CARRIER SURPRISE — THE SCOPE ROW

**What was measured.** 64 of 128 extension elements carry a uniform
configuration off the 640 carrier (mixed reversal flag); 32 reverse no link and
32 reverse every link; the smallest carrier on which the extension acts is the
1248-state orbit closure, on which the walk has 336 closed classes and a
335-dimensional stationary simplex.

**What it means — and does not mean.** It is **not** an error in paper-23, and
the paper is right to say so. Paper-23 took a **fixed locus**, and a fixed locus
is invariant only for elements normalising the group that fixes it; paper-23
independently measured that at the extension the chart-fixed locus is 32
configurations, not 640 (`32-AT-THE-EXTENSION-WHERE-REVERSAL-FORCES-U=XUX`).
Its 120 orbits / 119-simplex at "the chart-128 reading" are orbits of the
**residual gauge group of order 8**, which does act on the 640 carrier — and
SMU welds those classes to the parent's orbits **as sets** at both readings.

**The scope fact worth registering** is about the *naming*, and it has teeth:

> **"The chart-128 reading" names a gauge reading, not a chart action.** At
> that reading the 640 carrier supports a *census* but not a chart *dynamics*.
> A dynamics at the extension reading lives on the 1248-state closure, whose
> stationary simplex is **335**-dimensional. So the price at the extension is
> 119 for a measure on the parent's carrier and 335 for a dynamics on the
> carrier the extension actually acts on. The two numbers answer different
> questions and the unit publishes only the first inside the price sentence.

---

## 7. MAJOR-3 — THE "119 AT THE EXTENSION" HALF OF THE PRICE SENTENCE IS NOT MEASURED

`smu_exact.py:1856-1864`: `gauge_covariant` is computed as
`covariance_failures(P, n, S["_G4"])` — **the order-4 residual group at the
chart-32 reading, and only that group, at every instance.** No instance is
tested for covariance under the order-8 group; every Metropolis instance
declares `covariance_group = "THE-RESIDUAL-GAUGE-GROUP-CHART-32"`; and
`surjection.price_chart_128 = 119` is an inherited path-value from paper-23's
receipt (`PV-SIMP128`), not a measurement of this unit.

So the head's

> `THE-COVARIANT-DYNAMICS-FIBRE-SURJECTS-ONTO-THE-INVARIANT-SIMPLEX-SO-A-
> DECLARATION-STILL-SUPPLIES-207-INDEPENDENT-NUMBERS-AT-THE-ANCHORED-READING-
> AND-119-AT-THE-EXTENSION`

asserts as this unit's surjection a number for which no covariant chain was
built at that reading. The theorem covers it and I expect it to hold — the
orbit-uniform chart-128 measure is invariant under the order-8 group, so its
Metropolis chain is covariant under it — but **expected is not measured**, and
"the 11 gauge-covariant deriving instances" in the head likewise means
*covariant under the order-4 group*, unqualified.

**REPAIR (cheap and exact).** Add a second covariance column: run
`covariance_failures(P, n, G8)` at every instance on the 640 carrier and
publish it per row; require it to be 0 at the Metropolis-at-orbit-uniform-
chart-128 instance before the head may say 119. If it passes, the sentence is
licensed at both readings and the head can say so. If any instance fails, the
"11 gauge-covariant" count is reading-relative and must be labelled.
Simultaneously qualify the head: `...119-AT-THE-EXTENSION-READING-OF-THE-GAUGE-
GROUP-ON-THE-PARENTS-CARRIER(A-DYNAMICS-AT-THE-EXTENSION-LIVES-ON-THE-1248-
STATE-CLOSURE-WHERE-THE-SIMPLEX-IS-335)`.

---

## 8. MAJOR-4 — THE SWEEP SELF-DESCRIPTION IS FALSE AT 2 OF 7 AXES, AND THE
GATE THAT CERTIFIES IT EXEMPTS EXACTLY THOSE TWO

§10: "every declared dynamics axis is DECLARED-AND-SWEPT, **with the number of
instances built equal to the fibre at every one of them, so no member of a
declared fibre is left unrun**."

The unit's own receipt:

| axis | fibre | instances built |
|---|---|---|
| WHICH-CHART-GROUP | 2 | 2 ✓ |
| WHICH-RESIDUAL-READING | 2 | 2 ✓ |
| WHICH-SECTOR-CARRIES-WHICH-POSITION | 6 | 6 ✓ |
| WHICH-SIDE-COMPOSES | 2 | 2 ✓ |
| WHICH-SIDE-MULTIPLIES | 2 | 2 ✓ |
| **WHICH-INVARIANT-TARGET** | **THE-INVARIANT-SIMPLEX-ITSELF** | **3** ✗ |
| **WHICH-TARGET-THE-CONTROL** | **THE-WHOLE-SIMPLEX** | **1** ✗ |

And `G-FIBRE-INVENTORY`'s predicate (`smu_exact.py:2570-2573`):

```
    swept_ok = all(r["instances_built"] == r["fibre"] for r in rows
                   if isinstance(r["fibre"], int) ...)
```

— the two string-fibre rows are silently exempted by a type test, while the
gate's *sealed statement* claims "every DECLARED axis is swept to the bottom …
so no member of a declared fibre is left unrun and the census cannot be a
sample of its own declaration." **The census IS a sample of its own declaration
along exactly the axis that carries the entire price**, and that is not a small
irony: §7's whole point is that this fibre is as large as the simplex.

This is the era's vacuous-clause family (GDL M1; the #34 line), in its
politest form: the exemption is honest in the data and false in the prose.

**REPAIR (exact).**
- §10: "Five declared axes have finite fibre and are swept to the bottom,
  instances equal to fibre. Two — the invariant target and the control target —
  have a fibre the size of the simplex itself and are **sampled**, at 3 and at
  1; what stands in for a sweep there is the surjection theorem plus its
  exhaustive small-carrier arm (55 targets at a declared denominator, 0
  failures), and this is disclosed rather than absorbed."
- Instrument: give the two rows status `DECLARED-AND-SAMPLED` and have the gate
  *test* them (require a non-empty `sampling_licence` field naming the arm that
  substitutes for the sweep) instead of skipping them by `isinstance`.

### MINOR-2 — one verdict-determining flag is structurally forced, not measured

`verdict_determining = len(distinct stationary vectors along the axis) > 1`.
For WHICH-TARGET-THE-CONTROL exactly one instance exists, so the flag is False
by construction — yet §10 says the flag "binds each row by its own measured
predicate — re-running that axis at another instance moves a published vector."
No re-run occurred, and moving that target demonstrably moves published numbers
(the control supplies the DEFECT-CARRYING mass 129/200 and the Wilson row
263/200). Repair: stamp it `NOT-MEASURED-FIBRE-SAMPLED-AT-1` rather than
`false`. **The five flags that are True are all genuinely measured** (≥2
instances, distinct published vectors) — audited and affirmed, including the
one that matters most, WHICH-SECTOR-CARRIES-WHICH-POSITION at 6 distinct
outcomes.

---

## 9. PROSE ↔ RECEIPT SWEEP

Everything checked reproduced. The complete list of what I re-derived is in §
"recomputations" below. Two wording findings:

### MINOR-3 — "Two of those columns reproduce paper-23's published masses exactly"

**Three do.** The §6 table's composition-walk column *is* the counting measure
and matches paper-23's counting column at 4 of 4 sets; both orbit-uniform
columns match at 4 of 4; 12 of 12 cells verified. What is *two* is the number
of **cells** anchored at named receipt paths in the parent's receipt
(`PV-P23-NC-COUNTING`, `PV-P23-NC-ORB32`, both in the NON-COMMUTING row), plus
`PV-P23-WIDEST`. Repair: "Three of those columns reproduce paper-23's published
masses exactly — the composition walk's column is the parent's counting
measure, and both orbit-uniform columns are its own nulls — and two of those
cells are additionally checked against named paths in the parent's receipt."

### MINOR-4 (flagged to K3, noted here because it touches a delivered number)

The numeral-coverage allowlist forgives the literal `119` as a structural
literal (the `#119` seal engraving). `119` is also a **measured** delivered
number — the extension simplex dimension and the extension price, in §4.2, §7
and the head. The one gate that would catch a wrong 119 in prose is the gate
that is told to forgive it. Same shape as GDL's M4. Repair: forgive engraving
references only in the `(#NNN)` form, not as bare numerals.

### Walls — SWEPT CLEAN

The must-not vocabulary (`area-law`, `string-tension`, `potential`,
`confinement`) occurs at exactly two places in the paper: inside the verdict
block's own `NO-AREA-LAW-NO-STRING-TENSION-NO-POTENTIAL-CLAIM` and inside §8's
declaring sentence — both declaring sentences, both removed first by the
sweep. `QCD` occurs once, as `NOT-QCD`. **0 loop families grown.** No
area-law, string-tension, potential or confinement claim exists anywhere in the
text. **E-24: clean.** "Probability" occurs twice, both times about the
arithmetic of the instrument or about a law-native vector that *is* a
probability vector; the configuration column is stamped COUNTING-ONLY; every
mass is labelled with the dynamics that produced it. No count is silently
promoted to a probability.

---

## 10. THE LICENSED CLAIM

What paper-27 may say, at the standard this seat can verify:

1. **On the parent's 640-configuration carrier, at the chart-32 reading, six
   declared families and 18 declared instances were run; 12 fix a unique
   measure and 6 do not**, uniqueness gated by the closed-class count and every
   vector verified against its own law at full size.
2. **The inherited criterion is corrected**: derives iff exactly one closed
   communicating class; irreducibility is sufficient and not necessary; the
   witness is exhibited and the dimension identity verified exhaustively over
   the 3-state support family. On this census the two readings agree (0
   transient classes at 18 of 18).
3. **The gauge walk's decomposition is the parent's orbit census, as sets, at
   both readings**, so its stationary simplex *is* the parent's invariant
   simplex, at dimensions 207 and 119.
4. **The Metropolis construction is uniform in its target**, so at the chart-32
   reading the covariant-irreducible-dynamics fibre surjects onto the **relative
   interior** of the parent's 207-simplex — instantiated at 3 targets, verified
   exhaustively at 55 targets on a declared small carrier. **The declaration was
   relocated, not removed**; and dropped covariance, the same move costs 639
   numbers, not 207. *(This is the unit's exportable theorem.)*
5. **The measure moves across the declared fibre** — 10 distinct stationary
   vectors over 12 deriving instances, compared entry by entry. **The census's
   internal spread is 153/380 on DEFECT-CARRYING; at the parent's own three
   measures the census reproduces the parent's 27/130 exactly; and over the
   whole covariant fibre the reachable range of every headline set's mass is
   [0,1].**
6. **A named null is derived from the arena's own multiplication** — the
   counting measure, by a doubly-stochastic rejection walk built only from the
   family's product and its closure under inverse. *(This row is the census's
   cleanest, and the one the paper undersells.)*
7. **A law-valued point of the parent's simplex is supplied for the first
   time** — sector-graded at (15/38, 5/19, 13/38), invariant — **by transport,
   not by dynamics**, at the stamp of §1.4, with the identification unpinned.
8. **Expectations are computable and are computed, each conditional on its
   declared dynamics at 12 of 12 rows** — and **covariance pins none of them**:
   the reachable range over the invariant simplex is the observable's full
   range [0,4].
9. **The extension does not act on the parent's carrier**; the smallest carrier
   on which it does is the 1248-state closure. This is a scope fact about a
   naming, not an error in the parent.

What it may **not** say without the repairs above: that declaring a dynamics
moved the parent's sets further than declaring a measure did (§4); that the
law-native family derived a measure (§1); that the price is conserved at the
extension reading as a measurement of this unit (§7); that every declared fibre
was swept to the bottom (§8).

---

## 11. THE SUCCESSOR REGISTER

**ACT (the action unit) — inherits three things.**
- **The inheritance row of §1.6**, verbatim: the law-native π as leading
  candidate, at its stamp, inside the conserved-price frame, to be used as a
  control and never spent as a derived measure.
- **The price frame**: 207 numbers at the chart-32 reading (639 without
  covariance); an action that supplies a Gibbs measure pays that price by a
  route that is not a declaration, and that is the *only* known such route left
  after paper-23's census and this unit's relocation theorem.
- **The unaskability warning**: no Wilson number has content before ACT lands
  (§5.3). POT's confinement gate is downstream of that, not of this unit.
- **A cheap first move for ACT, from this unit's own opens**: search for a
  gauge-invariant functional whose range over the invariant simplex is
  *narrower* than its own range. Any such functional is the first quantity this
  arena hands over free; a functional whose range is a point would be a derived
  number. Cost is small and the outcome is decisive either way.

**OCC — one real crossover, and it is not the one the doubly-stochastic fact
suggests.** The `640 of 640` inverse-closure that makes the composition walk
doubly stochastic is a fact about the *coin family's* group structure, not
about occupancy; it does not bear on the ceiling question and this seat does
not register it as an occupancy connection. What OCC *should* take is the
method: **a "derived" ceiling must be gated on a predicate that could return
the other answer, and a construction built from the object it is supposed to
select is pricing, not evidence** (§1.3). OCC's seed conditional is exactly the
species where that distinction bites.

**FCK — inherits the same discipline** plus the concrete lesson that a rank-one
("resample from the target") extension of a dynamics derives nothing; a
number-changing dynamics must be state-dependent to carry content.

**GDL-1a / REQ2 — no crossover found.** Neither depends on the configuration
measure, and this unit's objects do not reach them. Registered as *checked and
empty* rather than unexamined.

**Carried forward from this unit's own §11, re-priced by this seat:**
- **The correspondence question** (paper-23's row (a)) is promoted: it is no
  longer only a measure-source question, it is the **gate on whether "law-native
  dynamics" can ever mean anything in this arena** (§1.5, Route A).
- **The 1248-state closure** is the first carrier where locality is not
  degenerate and where the extension genuinely acts — the natural home for both
  the re-asked census and the first locality-sensitive dynamics.
- **Forcing the sector→position assignment** stays open but is demoted: even
  fully forced it yields a transported measure, not a derived dynamics.

---

## 12. RECOMPUTATIONS (~131), AND WHAT THEY FOUND

| block | count | result |
|---|---|---|
| pinned hashes (5 objects, open and close) | 5 | all match |
| verdict string: paper fence = output = receipt | 3 | identical; single fence in the paper |
| §6 table, every cell vs receipt | 20 | 20/20 exact |
| spreads, 4 sets × 2 denominators, from the mass tables | 8 | 8/8 exact (153/380, 1701/3800, 28/95 ×2, 7/190) |
| parent masses reproduced (4 sets × 3 measures) | 12 | 12/12 identical to paper-23 |
| parent's widest over its own 3; SMU restricted to the same 3 | 2 | both 27/130 — **MAJOR-1** |
| distinct measures per headline row | 4 | 7/6/6/6, consistent with 10 distinct vectors |
| Wilson: 3 sector averages solved; 6 law-native re-predicted; 2 duplicates; 12 full-trace offsets; OU-32 from orbit structure; DIAGONAL = 64/208 | 27 | all exact (D=2, A=1, B=5/4; offset 12 everywhere) |
| headline-set masses decomposed into integer sector intersections | 4 | all resolve exactly |
| range over the invariant simplex, 4 headline sets (theorem-level) | 4 | [0,1] each — **MAJOR-1** |
| exhaustive Metropolis arm: target enumeration | 1 | 55 = C(11,2), all full support — interior only |
| dimension-theorem family size | 1 | 343 = 7³, exhaustive for the structural claim |
| fibre inventory: 11 rows (built vs fibre) + 7 flags | 18 | 2 rows unswept, 1 flag forced — **MAJOR-4, MINOR-2** |
| totals: anchors 9+30+12=51; gates 52+5+2=59 vs 57 sealed; waiver 34+16=50; sectors 64+64+512=640; orbit profiles ×2; monomial 5×128=640 | 8 | all consistent |
| Γ-triple: 4 anchors vs paper-16's published law; sums to 1 | 5 | exact; law-native and leg-independent confirmed at source |
| law-native kernel: rank-one structure; stationary = draw law | 2 | confirmed — **MAJOR-2** |
| covariance group actually tested at every instance | 1 | G4 only — **MAJOR-3** |
| chart-128: 32+32+64=128; closure 1248; 336 closed | 3 | consistent |
| wall sweep; E-24 probability-word sweep | 2 | clean |
| "two columns reproduce" | 1 | three do — **MINOR-3** |

**Zero delivered numbers moved. No false theorem found. No false number found.**

---

## 13. SUMMARY OF FINDINGS

| # | severity | finding | repair |
|---|---|---|---|
| MAJOR-1 | head | the 153/380-vs-27/130 comparison is max-over-superset vs max-over-subset; at fixed comparison class the census reproduces 27/130 exactly; the surjection licenses [0,1] | rewrite the head's RELATIVITY clause + §6 + §9 bullet (§4 above) |
| MAJOR-2 | decisive | the law-native chain is rank one — its "derived" measure is its declared draw law; and the Γ-triple's route onto the sectors is an unpinned cross-arena identification (paper-23's 0-found row) | adopt `LAW-RATED-CONSTRUCTION-DECLARED-AT-AN-UNPINNED-IDENTIFICATION`; move family (c) beside (f) in §9's pricing/evidence distinction; rewrite §11's open at the identification level |
| MAJOR-3 | head | "119 at the extension" is inherited, not measured: covariance is only ever tested against the order-4 group | add the order-8 covariance column and gate it, or qualify the head |
| MAJOR-4 | honesty | "no member of a declared fibre is left unrun" is false at 2 of 7 axes; the gate exempts exactly those two by an `isinstance` test | `DECLARED-AND-SAMPLED` status + a gate that tests the sampled rows (§8) |
| MINOR-1 | prose | "the parent's widest spread over invariant measures" invites the [0,1] misreading | "over its own three named nulls" |
| MINOR-2 | flag | the control axis's `verdict_determining: false` is forced by having one instance | stamp `NOT-MEASURED-FIBRE-SAMPLED-AT-1` |
| MINOR-3 | prose | "two of those columns" — three do; two *cells* are anchored | reword per §9 |
| MINOR-4 | K3's row | the coverage allowlist forgives `119`, a delivered measured number | forgive `(#NNN)` forms only |
| RULING | register | paper-23 takes a **CORRECTION ANNOTATION**, not an erratum, not a scope annotation | standing note, four clauses, §3.4 |

**Grade: AWF.** The measurements are sound and the unit's central theorem — the
relocation-at-conserved-price of a declaration — is real, exportable and
correctly identified as the thing this unit was built to say. The fixes are to
what the unit claims those measurements show.
