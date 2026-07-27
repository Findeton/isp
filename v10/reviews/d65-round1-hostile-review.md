# D65 — ROUND 1 INDEPENDENT HOSTILE REVIEW

**Frozen:** 2026-07-26.
**Unit under review:** D65 "the descent conditions" —
`note-d65-descent-conditions-pin.md` (STRICT, committed at `5afc5de`,
before the receipt), `note-d65-descent-conditions-result.md`
(GREEN-UNREVIEWED), `code/d65_descent_conditions_exact.py` +
`data/d65_descent_conditions_exact.out` (28 PASS / 3 FAIL, exit 0),
LOG #467.
**Reviewer:** independent Opus 5 worker, no prior context, no loyalty to the
unit, recompute-never-trust. Every number below was produced by code I wrote
for this review (`base.py`, `census.py`, `probe1..11.py`, scratch under
`/private/tmp/claude-501/.../scratchpad/d65rev/`): my own family enumerator,
my own state normal form (nested tuples, holdings as *sets*, no `repr`
serialisation — sharing nothing with d44a's `ser`/`canon_sigma`), my own
record functor, my own canonical event renaming and pair keys, my own
commuting predicate, my own exact products, my own transfer matrix and
rational linear algebra. The only object I share with the unit is the layer
under test (`d42b3`'s `candidates_for` / `admissible` / `event_poset` /
`View` / `triples` / `vname` / `V0`). Calibration:
`reviews/d62-round1-hostile-review.md` and `reviews/d64-round1-hostile-review.md`.

**VERDICT: REVISE. 1 BLOCKER / 5 MAJOR / 8 MINOR / 3 NIT.**

**The arithmetic is flawless — every single number reproduces.** From my own
instrument: the family census `[1, 6, 32, 176, 976, 5280, 27904]` = 34,375;
36 states; the mass function 34 × 2 and 2 × 5/2 with zero splits;
**794,570 / 129,284 / 0 / 665,286 / 0 / 665,286 / 576,654 / 88,632**; the
exclusion tags `{('p','p'): 33338, ('r','r'): 31304}`; all seven per-depth
rows exactly; the refined sub-census **425,334 / 32,256** with spectrum
`{1: 393078, 4/5: 16128, 5/4: 16128}`; the defect spectrum
`{1: 576654, 4/5: 44316, 5/4: 44316}`; the raw spectrum `{1: 665286}`;
**zero** pairs where `d ≠ M(σ(Hb))/M(σ(Ha))`; the same-mass/mass-mixed
partition; the entire by-ordered-class table entry for entry; six defecting
σ-states of which two carry mass 5/2; the depth-1 witness; **616** ordered
pair classes with **zero** splits and **176** keys with **zero** double
successors. The receipt reruns 28 PASS / 3 FAIL, exit 0, byte-identical to
the committed `.out` apart from timing, at `PYTHONHASHSEED` default, 7 and
12345. Two facts the unit does *not* gate and I checked anyway both land in
its favour: the raw path weight `q(h) = Π q` is constant on **all 5,548**
record classes at every depth ≤ 6 (so the "unnormalised weight is
order-independent" claim is true in a much stronger global form than the
adjacent-square census establishes), and D49's `Ẑ` is real — I rebuilt the
36-state transfer and `dim ker(T − 2I) = 1` with a strictly positive
generator taking exactly the values `{1, 4/3, 7/3}`, `λ = 1` has a
mixed-sign generator, and `μ_Ẑ = q·Ẑ` is constant on all 5,548 record
classes.

**The BLOCKER is a computation the unit did not run: how big is the space of
completions that repair the defect?** The answer is: enormously bigger than
the completion family. At the depth-4 truncation the repair cone has
**dimension 573 of 976**; the `(depth, σ)`-factoring family inside it has
dimension **28**. And "annihilates the defect" is not "repairs descent" —
neither implies the other, and I exhibit a strictly positive **measure on
refined record cylinders** whose conditionals violate the unit's
commuting-square identity, plus a strictly positive **repair** whose induced
measure is not a function of the record. LOG #467's "the completions the
dichotomy line forced are **precisely** the objects that repair descent" is
false in both directions.

**The five MAJORs are about what the census means and what it is evidence
for.** The headline hypothesis is one paper 29 §3.1 *explicitly exempts*, so
56,376 of the 88,632 headline failures carry no descent content; the ledger
move conflates the action line's slot with the generated line's own object
and contradicts the unit's own treatment of item 5; the "three FAILs, one
finding" framing hides that the only load-bearing one of the three is the
distinct one; the corollary's two "gated instances" are one shape and one of
the two gates cannot fail; and the exhaustive 794,570-pair census carries
exactly **720** class-level facts — a fact which, to the unit's credit,
discharges most of its own residue 4.

---

## BLOCKER 1 — the repair space is 573-dimensional, not the completion family: "precisely" is false, and "annihilates the defect" is neither necessary nor sufficient for descent

**Where.** LOG #467 ("COROLLARY [PROOF, 2 lines]: any completion factoring
through (depth, sigma) annihilates the defect IDENTICALLY … **THE TWO LINES
MEET: the completions the dichotomy line forced are precisely the objects
that repair descent.**"); note §3 (the corollary, its blockquote "the same
law read through the corpus's own selected completion **does** [descend]"),
note §1's title clause, licensed claim 5, receipt's printed corollary block.

**Defect.** The two-line telescoping proof is **correct** — I verified it
symbolically and numerically — but it proves an implication, and the unit
reads it as an equivalence. The proof uses exactly one property of `Z`:

```
    Z(Hab) = Z(Hba)   for every commuting pair.
```

`(depth, σ)`-factoring is a *sufficient* condition for that, and a very
special one. The necessary-and-sufficient condition is the displayed
equation itself, and the space of positive harmonic completions satisfying
it is not small. Nobody asked how big it is. Separately, the *descent*
statement needs something the corollary never touches: `μ_Z = q·Z` must be
constant on **record classes**, which is a different (and inequivalent) set
of equations.

**Recomputation (mine).** Truncate at depth `D`; `Z` free and positive on the
depth-`D` histories, extended downward by the completion recursion
`Z(h) = Σ_e q(e|h) Z(h+e)` (which is what makes `P_Z(e|h) = q Z(h+e)/Z(h)` a
normalised kernel — d42b3's own gradient construction). Impose the repair
equations for every commuting pair whose square closes inside the
truncation. Exact rational rank:

```
  D = 4 :  variables 976   repair constraints 403   EXACT rank 403
             dim of the positive repair cone            = 573
             dim of the (depth, sigma)-factoring family =  28
             dim of the record-constant family          = 313
             dim of repairs THAT ALSO DESCEND           = 205
             repair-space  ⊆ record-constant ?  NO
             record-constant ⊆ repair-space  ?  NO
             (152 of the 403 repair rows are not implied by
              record-constancy)

  D = 5 :  variables 5280  repair constraints 2227  rank 2227 (mod p,
             hence exactly 2227 over Q since rank ≤ #rows)
             dim of the repair cone = 3053  vs  (depth,sigma) = 32,
             record-constant = 1138
```

`Z ≡ 1` solves every constraint, so the solution space meets the positive
orthant in an *open* cone; the `(depth, σ)`-factoring family is a
28-dimensional slice of it, leaving **545 independent directions of strictly
positive repairs transverse to the corpus's family**. Two explicit witnesses,
both strictly positive and both exact:

```
  (i)  Z = 1 + (1/100)·v,  v a kernel direction of the 403 repair rows:
         strictly positive; satisfies ALL 403 commuting-square identities;
         violates 4 record-constancy equations; a record class with 4
         histories carries 2 different Z values.
       => P_Z repairs every square the unit censuses, and mu_Z is NOT a
          function of the record: NO record-cylinder measure. "Annihilates
          the defect" does not imply "repairs descent".

  (ii) Z record-constant at the boundary (one class perturbed to 101/100),
       extended by the same recursion:
         mu_Z constant on 427/427 record classes at depth <= 4 — it IS a
         positive measure on refined record cylinders — and it VIOLATES
         2 of the 403 sigma-commuting square identities:
           H = ()  a = ('p','A',v0,0)  b = ('n','A')
           P_Z(a|H)P_Z(b|Ha) = 39003/1659203
           P_Z(b|H)P_Z(a|Hb) =   3000/127631      (records differ, sigma equal)
       => "repairs descent" does not imply "annihilates the defect" either.
```

The real hierarchy, which is what the unit should print, is

```
   repair cone (573)  ⊃  repairs that descend (205)  ⊃
   (depth,sigma) family (28)  ⊃  depth-stationary form (1 ray = D49's Zhat)
```

and the object that collapses 573 → 1 is **D50's form choice**, not descent.
The note *says* this in its own price paragraph ("the stationary FORM of `Z`
is a CHOICE") and then LOG #467 says the opposite.

**What must change.** (a) LOG #467's "precisely" sentence must be withdrawn
or inverted: the completions the dichotomy line forced are *one 28-dimensional
slice, and inside it one ray, of a 573-dimensional repair cone*. (b) The
corollary must state its actual hypothesis (`Z(Hab) = Z(Hba)`) and note that
`(depth, σ)`-factoring is one sufficient condition among many. (c) The
descent sentence must be separated from the defect sentence: for `Ẑ`
specifically descent **does** hold (I verified `μ_Ẑ` constant on all 5,548
record classes — see MINOR 2, it is ungated), but that is an extra fact, not
a corollary of the two lines. (d) The successor question sharpens to: *is
there any record-level demand that cuts the 573 down to the 28, or is the
completion family selected only by the stationary form?* — which is D50
again, now with a number attached.

---

## MAJOR 1 — the headline census tests a hypothesis paper 29 §3.1 EXPLICITLY exempts; 56,376 of the 88,632 failures carry no descent content, and a genuine record measure fails the same test

**Where.** Pin §2's DC1 definition ("`sigma(Hab) = sigma(Hba)` … which is the
generated analog of paper 29's record-cylinder identity `[Hab] = [Hba]`");
note §1's census table (the word **COMMUTING** attached to 665,286); note §7
licensed claim 1 (88,632 first, 32,256 second); LOG #467's headline; receipt
DC1(a), which is the pin's primary predicate and the gate that "decided the
unit".

**Defect.** Paper 29 §3 defines commutation *at the refined record level*:
"Two record extensions `a` and `b` commute at the refined record level when
both orders denote the same cylinder: `[Hab] = [Hba]`. **This is a statement
about record identity, not merely equality of a coarse terminal state.**"
And §3.1, immediately after the proof, says what the theorem does **not**
require: "The theorem does not require equal weights for two distinct serial
histories that later push to one quotient atom." §4.3's hypothesis (3) is "one
common refined cylinder **or a declared pushforward atom**" — in the
pushforward reading the requirement is the *sum* rule, not the conditional
product identity.

σ-equality is exactly "equality of a coarse terminal state". So the unit's
primary class is the one paper 29 names and then exempts, and it is a
*weaker* hypothesis, which *inflates* the failure count. The unit knows the
distinction — DC1(f) is there and §1.2 declares the identification as
interpretive — but the pin made the coarse test primary, the census table
gives the coarse class the name "COMMUTING", and every headline number
(88,632; 665,286) is the coarse one. The consequence sentence in §2 is
carried by DC1(f) alone.

**Recomputation (mine).** Two facts, neither of which appears in the unit.

```
  (a) the refined class is a PROPER subclass, and the excess is where the
      exemption bites:
        sigma-commuting ordered pairs             665,286
        refined-record-identical (canon equal)    425,334
        sigma-commuting but NOT record-identical  239,952
        failures inside the refined class          32,256   (7.58%)
        failures OUTSIDE it                        56,376   (63.6% of 88,632)
      Record identity implies sigma identity everywhere (0 sigma splits over
      all 5,548 record classes), so the containment is one-way, as the unit
      says.

  (b) no record measure is REQUIRED to satisfy DC1(a)'s test. Witness (ii)
      of BLOCKER 1 is a strictly positive measure on refined record
      cylinders (mu constant on 427/427 record classes) whose conditionals
      violate 2 of the 403 sigma-commuting squares — at a pair whose two
      records DIFFER. Theorem 1 is untouched; DC1(a) is simply not a
      descent test.
```

**What must change.** DC1(f)'s numbers become the headline and DC1(a)'s
become the reporting line, with §3.1 quoted beside them; the census table's
"COMMUTING" row must be renamed (it is the *σ-commuting* row, and the
refined row is the Theorem-1 row); licensed claim 1 must lead with
32,256 / 425,334; LOG #467's opening census must carry the same correction.
The pin cannot be edited, but the result note must record that the pin's DC1
predicate was the coarse one and that the load-bearing verdict rests on the
sub-census.

---

## MAJOR 2 — DC4's "boundary state MOVES" conflates the action line's slot with the generated line's own statistic, and contradicts the unit's own treatment of item 5

**Where.** Pin §2 DC2 ("the first supplied-not-derived item of D59's list
(the boundary state) is, at this scope, derived"); note §6 table row 1
("**MOVES — for the GENERATED line only**") and its ground paragraph;
receipt's `LEDGER` entry 1 and the DC4 gate ("exactly one of D59's six items
moves"); LOG #467 ("D59's boundary-state item **moves to DERIVED** for the
generated line").

**Defect.** D59's six items are quoted from paper 29's abstract: "the D15
low-energy action is retained, yet the corpus still supplies rather than
derives **its** boundary state, measure and contour, renormalization, record
instrument, generated record grammar and clock dictionary." The possessive is
the *identified law's*. §9.2's slot table names the object: "boundary/
cosmological state — selects amplitudes and long-range correlations". The
generated line's `σ` was never on that list, so it cannot move *on* that
list. The unit's own qualification says exactly this ("that is a **different
object**, and it remains supplied. What moved is the generated line's *own*
boundary statistic — the counterpart of the slot, not the slot") — and then
the table cell, the gate, the pin and the LOG all say MOVES.

The internal inconsistency is decisive: **item 5 is structurally identical
and is scored the other way.** Note §6 row 5: "generated record grammar —
**stands** *for the action line*; never supplied on the generated line …
nothing here connects it to D15 action content." Item 1 has precisely that
shape: stands for the action line, never supplied on the generated line,
nothing connects it to D15. Two identical situations, two different verdicts,
and the difference is which one the headline wanted.

**Recomputation (mine).** None needed; this is a reading, and I checked it
against the source: paper 29 abstract lines 48–52, §9.2's table, and D59 §2's
quotation block. All three carry the same possessive. Nothing in DC2 touches
an action-line object: DC2(a)/(b)/(c) are (H1)/(H2) restated on the generated
family, exactly as the unit says.

**What must change.** Row 1 becomes **STANDS** with the same wording as row
5, and the *positive* generated-side statement moves out of the ledger into
its own sentence beside it ("the generated line has a **derived** boundary
statistic and a printed 36-row kernel; D59's item, which is the action line's
boundary/cosmological state, is untouched"). `moved == 1` becomes
`moved == 0`, and LOG #467's DC2 sentence must be corrected. Note that this
*costs the unit nothing real* — the theorem content (σ is constructed, its
sufficiency is (H1)+(H2)) survives verbatim; only the ledger row is wrong.

---

## MAJOR 3 — "three FAILs, one finding counted three times" is ONE statement counted twice plus a SECOND, distinct test — and the distinct one is the only load-bearing one

**Where.** Note's status line ("**All three FAILs are the same
pre-registered negative**: DC1(a), its refined-record sub-census DC1(f), and
DC3(3) — which *is* DC1 — are one finding counted three times"); LOG #467
("all three FAILs the ONE pre-registered negative counted thrice").

**Defect.** DC3(3)'s predicate is the Python variable `DC1_HOLDS` — literally
the same test, so that one is a copy and the framing is right about it.
DC1(f) is **not** a copy: it is a different predicate over a different
population (425,334 vs 665,286), with a different failure rate (7.58% vs
13.32%), under a *strictly stronger and differently-motivated* hypothesis —
and by MAJOR 1 it is the only one of the three from which paper 29's
contrapositive follows. Calling it a duplicate is exactly backwards: the
unit's own §2 consequence paragraph cites DC1(f), not DC1(a), as the
hypothesis that makes the conclusion valid. Folding it into "one finding"
buries the one number that carries the result and makes the FAIL count look
like reporting noise.

**Recomputation (mine).** The two predicates are not logically coupled:
BLOCKER 1's witness (ii) is a positive record-cylinder measure that fails
DC1(a)'s test while satisfying descent, so DC1(a) can fail where DC1(f) has
nothing to say. Here both fail, but neither entails the other — 56,376 of the
88,632 DC1(a) failures lie outside DC1(f)'s population entirely, and the
32,256 inside it are the only ones the consequence uses.

**What must change.** "3 FAILs = 2 statements: DC1(a) (= DC3(3)) and DC1(f),
the latter being the one paper 29's theorem speaks to."

---

## MAJOR 4 — the corollary's two "gated instances" are ONE shape, DC1-C cannot fail, and twelve of the twenty-eight PASSes are entailed, tautological or constant

**Where.** Note §3 ("The receipt also exhibits an **independent** completion
of a **different shape**: d42b3's depth-4 gradient completion `Z`"); licensed
claim 5 ("D49's `Ẑ` is one, d42b3's gradient `Z` is another of a different
shape"); LOG #467 ("d42b3's gradient Z is an independent gated instance (403
pairs, 0 failures)"); receipt gates DC1(c)/(d)/(e)/(g)/(h), DC1-C, DC2(b)/(c),
DC3(2)/(3)/(5), DC4, DET(a)/(b).

**Defect (a) — the "different shape" has the same shape.** The gradient `Z`
is `Z ≡ 1` at depth 4 pulled back by `Z(h) = Σ_e q(e|h) Z(h+e)`. Since the
menu with its weights is a function of σ ((H1)) and σ updates by a function
of (σ, renamed event) ((H2)), the recursion preserves σ-functionality
downward. So `Z` factors through `(depth, σ)` — the very hypothesis of the
corollary — and DC1-C is an *instance* of the two-line proof, not independent
evidence for it.

```
  gradient Z, depths 0..4:  (depth, sigma) cells 64
                            cells carrying more than one Z value:  0
                            record classes carrying two values:    0
  Z(empty) = 1037/64  (= the depth-4 raw cut mass, see NIT 2)
```

Given DC1(b) (gated, 0 exceptions) the DC1-C predicate `zn_def == 0` is
therefore a theorem of the corollary — it cannot fail.

**Defect (b) — the entailment/tautology census.** Of the 28 PASSes:

```
  DC1(c) => DC1(e)          same-mass <=> d = 1 is immediate from d = M/M
  DC1(c) + CG3a => DC1(d)   sigma(Ha) is a function of (sigma(H), renamed a)
                            [my own: 176 keys, 0 with two successors], so
                            d = M(sigma Hb)/M(sigma Ha) is a function of the
                            key-A pair key by construction.  DC1(d)'s 616
                            classes and 0 splits cannot come out otherwise
                            (key B has the same 616 classes, so the two
                            resolutions agree and neither adds evidence).
  DC1(g)   all four conjuncts are counter-construction tautologies:
             n_pairs == 2*n_unord   (both incremented in one place, by 2 and 1)
             n_pairs == neither + onesided + both   (mutually exclusive
                                                     branches of one if/else)
             n_both == n_sigdiff + n_comm           (likewise)
             n_defect <= n_comm                     (n_defect only ever
                                                     increments inside the
                                                     commuting branch)
  DET(a)   re-runs the same sub-census with the parent list and menus
           reversed; the enumeration is a full double loop over an unordered
           pair set, and every pair records BOTH d and 1/d, so both the count
           and the spectrum are order-invariant by construction.
  DET(b)   predicate is `isinstance(CACHE[h], list)`; CACHE is filled with
           the enumerator's return value.
  DC4      predicate is `moved == 1 and len(LEDGER) == 6` over a hand-written
           literal list in the same file.
  DC2(b)   admitted in its own label ("can only fail if DC2(a) fails")
  DC2(c)   admitted ("cannot fail")
  DC3(2)   predicate is the constant True (admitted)
  DC1(h)   predicate is the constant True (admitted)
  DC3(5)   == DC2(a)  (admitted);  DC1-C  entailed, see Defect (a)
  and, among the FAILs, DC3(3) == DC1(a) (admitted)
```

**Twelve** of the twenty-eight PASSes cannot fail — DC1(d), DC1(e), DC1(g),
DC1(h), DC1-C, DC2(b), DC2(c), DC3(2), DC3(5), DC4, DET(a), DET(b). The
genuinely falsifiable set is N0(a)–(e), N1, N2 (anchors), N3, N4, N5,
**DC1(a)**, **DC1(b)**, **DC1(c)**, **DC1(f)**, DC2(a), DC3(1), DC3(1′),
DC3(4) — sixteen gates, which is still a respectable receipt. The D62 round's
standard is that the *label* must say so.

**What must change.** "an independent completion of a different shape" →
"a second member of the same family, whose DC1-C gate is an instance of the
corollary"; the entailed gates relabelled as corollaries of the gate that
implies them (the d63/d64 idiom); DC1(g) and DET(a)/(b) printed as
bookkeeping lines, not gates.

---

## MAJOR 5 — the exhaustive census is 720 class-level facts, not 794,570 independent ones — and that same computation discharges most of the unit's residue 4

**Where.** Note §1 ("The census is EXHAUSTIVE over every parent of the
family … **Nothing is sampled**"), §1.1's repeated "zero exceptions on
665,286 pairs", licensed claims 2–3, LOG #467's "THE CENSUS, EXHAUSTIVE
(nothing sampled…)", and residue 4 ("The all-depth statement follows from
(H1)+(H2) plus the mass-function argument, but it is *stated* here, not
mechanized; a depth-free proof of DC1(c) is a one-page obligation the
successor should discharge").

**Defect.** By (H1) and (H2) — both THEOREMS, and both re-derived in this
receipt's own N2 — every quantity in the DC1 census is a function of
`(σ(H), renamed a, renamed b)`. So the 794,570 ordered pairs collapse onto
the pair classes of the 36-state chain, and the census's evidential content
is that class count, not the pair count. The multiplicity (~1,080 pairs per
class) is replication, not independent confirmation. The note's rhetoric
("665,286 pairs, zero exceptions" repeated five times) reads as 665,286
independent tests.

**Recomputation (mine).** Taking one representative history per state and
enumerating that state's own menu pairs:

```
  sum over the 36 states of m(m-1)                    = 720
     ... of which both orders admissible (commuting)  = 616
     ... of which neither order admissible (exclusive)= 104
     ... of which exactly one order admissible        =   0
  and the family-wide pair-class census gives the same 616 (0 splits),
  so EVERY class is realised inside the depth-6 family.
```

**The constructive half, and it is worth more than the criticism.** Because
the class census is *complete* (720 = 616 + 104 = Σ m(m−1) over all 36
states), residue 4's "one-page obligation" is nearly discharged by the unit's
own data: (H1) + (H2) reduce the all-depth statements of DC1(b) and DC1(c) to
a finite check over the 616 commuting classes, and that check is exactly what
the receipt ran. What actually remains is a renaming-composition lemma (that
"`b` renamed at `Ha`" is a function of `(σ(H), renamed a, renamed b)` — the
content of `canon_pair2`'s well-definedness, gated at depth ≤ 2 only, see
MINOR 8). Residue 4 should say that, and should *not* say that DC1(b) follows
from (H1)+(H2): the raw cocycle is a fact about the weight layer, not a
consequence of the two closure theorems, and the class-completeness argument
is what carries it to all depths.

**What must change.** State the class count beside the pair count everywhere
the pair count appears; restate residue 4 as above.

---

## MINOR 1 — the title's "its unnormalised weight does [descend to a record measure]" — the unnormalised weight is not a measure

The note's title is "The generated law's *normalised* kernel does not descend
to a record measure; its *unnormalised* weight does." What descends is the
*function* `q(h)` (I verified: constant on all 5,548 record classes). It is
not a measure on cylinders, because it is not additive along cuts — that is
the whole reason a completion is needed:

```
  sum over |h| = n of q(h):  n=0..6:  1, 2, 4, 257/32, 1037/64, 2101/64, 68313/1024
```

§2 states it correctly ("order-independent unnormalised history weight"); the
title and the §3 blockquote invite the stronger reading. One word ("descends"
→ "is order-independent") fixes it.

## MINOR 2 — the descent claim for `Ẑ` is never gated (it is true; I checked)

§3's blockquote — "the same law read through the corpus's own selected
completion **does** [descend]" — is a statement about `μ_Ẑ` being a measure on
record cylinders. The receipt gates only the local squares, and only for the
*gradient* `Z` on 403 pairs at depth ≤ 4; `Ẑ` itself is never instantiated in
the receipt at all (it appears only in a printed paragraph). By BLOCKER 1 the
square identity does not imply descent, so the sentence is unsupported as
printed. It is nonetheless **true**, and here is the missing gate:

```
  Zhat(h) = 2^-|h| f(sigma(h)), f the positive lambda=2 eigenvector:
     dim ker(T - 2I) = 1, generator strictly positive, values {1, 4/3, 7/3}
        with multiplicities {29, 5, 2}  (= (3,4,7)/3, i.e. D49's f)
     lambda = 1: kernel dim 1, MIXED SIGNS (so no depth-ungraded completion)
     lambda = 5/2 and 9/4: kernel empty
     harmonicity  sum_e q(e|h) Zhat(h+e) = Zhat(h):  0 violations, depth <= 5
     mu_Zhat = q.Zhat constant on record classes:    0 violations of 5,548
```

Adopt those four lines as a gate; they are cheap and they are the actual
content of the sentence.

## MINOR 3 — DC1-C's "403 commuting pairs" is an unordered count inside an ordered-census note, and its domain is 0.6% of the family

Every census in the unit is ordered *by explicit design* (§1's paragraph on
why). DC1-C's loop increments once per unordered pair, so its 403 is 806 in
the note's own unit. Its domain is the 39 parents of depth ≤ 2 (0.11% of the
family); 251 of the 403 pairs are refined-record-identical, 152 are not. All
three numbers belong in §3.

## MINOR 4 — the VERDICT block's prose is not guarded by the gates it cites

Under `if not DC1_HOLDS:` the receipt prints "the RAW products always agree
(DC1(b))", "the entire defect is … exactly `d = M(σ(Hb))/M(σ(Ha))`
(DC1(c))", "it is a function of (σ(H), class(a), class(b)) alone (DC1(d))",
"it VANISHES exactly on same-mass intermediates (DC1(e))" — with no
predicate. Had any of those gates failed, the verdict paragraph would still
assert them. `substantive_ok` is computed two lines later and printed as a
word, but nothing conditions the prose on it. Same class as D64's MINOR 1.

## MINOR 5 — the two gates the defect formula rests on are not anchors, and CG3a is never re-gated

`N3` (the layer's own sanity counters) and `N4` (mass is a function of σ)
carry `anchor=False`, so a break in either exits 0 while DC1(c)'s meaning
evaporates. Separately, `NKEY[...] = SIG[h+e]` **overwrites**: the receipt
counts 176 keys but never checks that each key has a *single* successor state
— which is the property (d44a CG3a / (H2)) that makes DC1(d) meaningful. I
re-derived it independently (176 keys, 0 with two successors); the receipt
should too, in one line.

## MINOR 6 — "confined to 6 of the 36 states" is entailed, and it is not a localisation of the pathology

Given DC1(c) and a two-valued mass, a parent state carries a defect **iff**
its menu contains two events leading to states of different mass. So the
6/36 count is a statement about which parent states admit a mass-mixed pair —
a corollary, printed as if it were an independent containment result ("The
other 30 states carry `{1: …}` and nothing else"). Item 7 of §1.1 is already
correctly labelled a consequence; item 6 should be too.

## MINOR 7 — DC3(1)'s "independently constructed adversarial pool" is judged by the same `admissible` that builds the menu

The pool of 718,570 events is genuinely independent of `candidates_for`; the
*verdict* on each pool event is `adm(list(h), e)` — d42b3's own
`admissible`, which is also what `candidates_for` calls. So the gate tests
that `candidates_for`'s *enumeration* is complete and non-redundant with
respect to `admissible`. That is a real and worthwhile test (and it passes on
my rebuild too), but it is not a test of the grammar's exclusivity or
exhaustiveness in any sense independent of the layer. The label should say
"enumeration completeness of `candidates_for` against `admissible`".

## MINOR 8 — N5 gates the joint key at depth ≤ 2 (214 transitions) while the 616-class result uses it family-wide

`canon_pair2` is tied to the committed `canon_pair` only through
`canon_pair2(h, e, e)` at histories of depth ≤ 2. DC1(d)'s key-B census runs
over all 665,286 commuting pairs. The diagonal check also cannot detect the
one thing that matters for a *pair* key — that the two events are renamed
under one common bijection — because on the diagonal there is only one event.
(I built my own pair key independently and got the same 616 classes and 0
splits, so nothing is wrong; the gate is just much narrower than its use.)

## NIT 1 — "Two census facts … " followed by three bullets

Note §1. The third bullet (zero non-commuting pairs) is the one that gets
used later.

## NIT 2 — the `Z(∅) = 1037/64` anchor is the depth-4 raw cut mass

`Σ_{|h|=4} q(h) = 1037/64` exactly, so the anchor certifies that the
recursion was run, not that the gradient completion is the one d42b3 selected.
A second anchor (a value at depth 2 or 3, or d42b3's 21-of-114 deformation
count) would carry more.

## NIT 3 — residue 3's parenthetical is functor-specific

"A coarser or finer record functor changes which pairs are in DC1(f)'s
subclass, **though not DC1(a)'s verdict (the sigma-commuting class contains
it)**." The containment holds because `canon`-identity implies σ-identity —
which I verified for `canon` (0 σ splits over 5,548 classes) but which is a
property of *that* functor. A coarser functor need not have it, and then
DC1(f)'s class is not inside DC1(a)'s.

---

## Checked and CLEAN (D65)

Everything below is my own recomputation unless stated.

**A. Receipt rerun.** `28 PASS / 3 FAIL`, **exit code 0** (captured), three
times (279.9 s / 212.2 s / 209.4 s; committed 224.5 s). Output byte-identical
to the committed `.out` apart from the timing lines, at the default seed and
at `PYTHONHASHSEED` 7 and 12345. The three FAILs are DC1(a), DC1(f), DC3(3) and
nothing else; `ANCHOR_FAIL` is tracked separately from `FAIL`, so a
FAIL-tagged gate cannot mask an anchor break, and `sys.exit(1 if ANCHOR_FAIL
else 0)` is exactly the pin's exit protocol. The pin's F-DC1 fired and the
unit reports it as the deliverable, which is what pre-registration is for.

**B. The family and the state space, rebuilt.** My own BFS enumerator over
the committed `candidates_for` reproduces `[1, 6, 32, 176, 976, 5280,
27904]` = 34,375. My own state normal form — nested sorted tuples, holdings
as sets, no `repr`, canonicalised over base bijections — induces **exactly**
d44a's partition (36 ↔ 36, zero splitting classes in either direction) and
the mass function is σ-functional with values `{2 × 34, 5/2 × 2}`, zero
splits.

**C. The whole DC1 census.** 397,285 unordered / 794,570 ordered;
129,284 mutually exclusive with tags `{('p','p'): 33338, ('r','r'): 31304}`;
**0** asymmetric; 665,286 both-orders; **0** σ-differing; 576,654 hold;
88,632 fail. Per-parent-depth `[30,26,0] [140,124,24] [832,656,192]
[4672,3648,864] [24416,19744,3456] [124992,103744,14976]
[639488,537344,69120]` — every row exact. The root mutual-exclusion witness
(`p_A(v0,0)` vs `p_A(v0,1)`) reproduces, and the mechanism is as stated
(`prop_options_in_view` refuses a base already carrying the actor's live
proposal).

**D. The structure of the failure.** Raw spectrum `{1: 665286}` — the raw
cocycle holds on every commuting pair. `d = M(σ(Hb))/M(σ(Ha))` with **zero**
exceptions on 665,286. Spectrum `{1: 576654, 4/5: 44316, 5/4: 44316}`.
Same-mass `{1: 576654}`, mass-mixed `{4/5: 44316, 5/4: 44316}` — a clean
partition. The by-ordered-class table reproduces entry for entry, including
that `(n,n)`, `(p,p)`, `(r,r)` never defect. Six defecting σ-states, two of
them the mass-5/2 states (my state indices differ from the receipt's because
my normal form sorts differently; the multiset of per-state spectra is
identical). The depth-1 witness reproduces exactly:
`q = 1/4, 1/8, 1/8, 1/4`, raw products `1/32` both ways, `N(Ha) = 2`,
`N(Hb) = 5/2`, `d = 5/4`.

**E. The refined sub-census.** My own record functor (canonical labelled DAG
over my own poset) gives 425,334 refined-identical ordered pairs, 32,256
failures, spectrum `{1: 393078, 4/5: 16128, 5/4: 16128}`. Record classes by
depth: `1 / 6 / 23 / 84 / 313 / 1138 / 3983` (5,548 total — the same layer
census D49 reports).

**F. The σ-functionality claims.** My own canonical event renaming and pair
keys, built from my own state canonicalisation: **176** `(σ, renamed event)`
keys with **0** carrying two successor states; **616** ordered pair classes
with **0** carrying two defect values. The self-swap argument in §1.1 item 4
is sound: a class fixed by an automorphism exchanging `a` and `b` receives
both `d` and `1/d`, forcing `d = 1`.

**G. Facts the unit does not gate, checked, all in its favour.** (i) The raw
path weight is constant on **all 5,548** record classes at every depth ≤ 6 —
the "unnormalised weight descends" claim is true globally, not merely on
adjacent squares, which is a stronger result than the unit claims. (ii) The
menus are *literally* equal (not merely equal up to renaming) across each
record class, 0 of 5,548 — so "the kernel is a function of the record" is
well-posed, which claim (ii) presupposes. (iii) Record identity implies σ
identity, 0 splits. (iv) **The birth probe**: over all parents of depth ≤ 4
and all 34,368 `(a, b)` continuations, there is **no** case where `b` is
admissible after `a`, causally independent of `a`, and *not* already in the
menu at `H`. So the menu-pair census does not miss any last-two swap
opportunity — the "zero asymmetry" fact has a companion, and both hold.
(v) D49's `Ẑ` is real and harmonic (MINOR 2).

**H. Positivity and the two consequence sentences.** Every menu weight is a
strictly positive `Fraction`, smallest `1/8`, 179,782 entries — so all three
displayed conditioning cylinders in every square are positive and Theorem 1's
hypotheses are met on the refined class. Consequently the §2 conclusion
("no positive measure on refined record cylinders has the generated
normalised kernel as its conditionals, at this scope") **stands**, carried by
DC1(f)'s 16,128 unordered refined-identical failing squares. The refusal to
call it an F1 hit is correct and is the best judgement in the note: F1 asks
for a *measure* with unequal products; what is exhibited is a conditional
system that is not induced by any measure. That distinction is drawn
precisely and I could not break it.

**I. DC2, DC3, and the printed kernel.** Fibre constancy: 36 fibres, zero
carrying two different renamed menus, 34,375 histories — reproduced. All 36
rows sum to 1. My own independently written pool over the tokens each
history has uttered, at the **unrestricted** surface (arbitrary multi-base
ckeys, every winner subset) over every history of depth ≤ 4, reproduces the
receipt's DC3(1′) exactly — **22,762** pool events, **0** omitted admissible
events, **0** refused-but-listed, **0** weight disagreements — and my own
positivity sweep gives **179,782** menu entries, smallest weight **1/8**,
zero non-positive weights and zero histories with a duplicated menu entry.
Subject to MINOR 7's label point, the gate is sound. DC3(2)'s honesty is exemplary:
the "trivially satisfied AND uninformative" framing, the explicit statement
that the generated line has no functional level and that this unit does not
build one, and the naming of that segment as where the map is widest, are all
correct and are the most valuable prose in the unit.

**J. Caps, slices, determinism, thresholds.** No caps: the depth is a CLI
argument, printed, with the anchors disabled off-default; the per-parent
`local` menu cache is cleared at the deepest level and is not a truncation.
The d44a slices are pure definitions (0 `sys.exit`, 0 top-level `check`, 0
top-level `print`) and the d42b3 prefix is cut before its first print — I
re-ran the same extraction independently. No invented thresholds: the two
mass values are read off d44a's committed row-sum line rather than typed
(N0(e)), and the only depths in the file are the family cap, `ZD = 4` (d42b3's
own) and the ≤ 2 / ≤ 3 / ≤ 4 sub-census scopes, all printed. No set iteration is load-bearing in my own
instrument either (every ordering comes from the enumerator's list or from
`sorted(..., key=repr)`), and the receipt is byte-identical at
`PYTHONHASHSEED` default / 7 / 12345 on my machine.

**K. Provenance and pin discipline.** The pin is STRICT, 123 lines, committed
at `5afc5de` **before** the receipt and the result note (`a5f99c1`). DC1 is
genuinely pre-registered both ways ("BOTH outcomes pre-registered as
results"), the pin's lean names the mass-mixed pairs as the risk *before* the
run and is reported as landing rather than quietly dropped, and the pin's own
F-DC2 ("mislabelling DC2 as new") is honoured emphatically in §4 and in the
receipt banner. The three "explicitly NOT licensed" bullets in §7 are the
right ones.

**L. Scope.** Every sentence in the note stays at two-actor delivery-free
d42a on the exhaustive depth-6 family. No transfer to the identified law is
claimed anywhere; the map is treated as an identification problem throughout;
no claim is made about the action line's measure; the D50 price on the
completion is carried at every mention; residue 2 (the coboundary form may
not survive three actors or delivery) is exactly the right caveat and is
stated unprompted. Subject to BLOCKER 1 and MAJORs 1–3, no claim exceeds the
swept census.

---

# DELTA — adjudication and repairs (campaign side, 2026-07-26)

**Verification of the BLOCKER.**  The repair-space computation is now
GATED IN THE RECEIPT (DC1-R(a)-(i)): exact rational rank over Q at
D = 4 — 976 variables, 403 independent constraints, positive repair
cone dim 573; the (depth, sigma) family dim 28 (545 transverse
directions); record-constant (descending) family dim 313; repairs
AND descend dim 205; D = 5 widens the gap (2227 / 3053 / 32 / 1138).
Both inequivalence witnesses gated (a positive square-repairing Z
whose mu is not record-constant; a positive record measure breaking
2 sigma-commuting squares, reproducing the referee's exact
fractions).  **The hierarchy 573 ⊃ 205 ⊃ 28 ⊃ 1(Zhat) is printed as
the gate verdict, with the collapse attributed to D50's form choice,
not descent.**  Every referee number reproduced with zero
contradictions; the one divergence (witness (i)'s broken-count) is
construction-specific and flagged in both files.

**Repairs applied (receipt 39 PASS / 3 FAIL, exit 0, 336 s; note
retitled):** MAJOR 1 — the headline is the REFINED sub-census
(32,256 / 425,334); the 56,376 wider failures are outside Theorem
1's hypothesis and demoted to context (a genuine record measure
fails the same wider test).  MAJOR 2 — the ledger item STANDS
(moved == 0 gated); the generated line's derived boundary statistic
is stated beside it, not in its place.  MAJOR 3 — the three FAILs
are TWO statements (DC1(f) load-bearing; DC1(a) = DC3(3) context).
MAJOR 4 — evidence map: 29 falsifiable of 42 gates, corollary/
reporting markers throughout; DC1-C fixed.  MAJOR 5 — 720
class-level facts stated; residue 4 near-discharged.  The two
ungated-true claims now gated: the raw weight is constant on ALL
5,548 record classes (and is NOT a measure — cut masses printed);
Zhat is the unique positive lambda = 2 harmonic completion and
mu_Zhat GENUINELY DESCENDS (constant on all 5,548 classes).  All
MINOR/NIT items applied; a worker-introduced hash-order hazard was
caught and removed before delivery; three-seed byte-identity
re-verified.

**Verdict after repairs: the unit stands as restated** — the defect
structure exhaustively measured, descent repairable with the
completions AMONG the repairs (and Zhat's descent now a gated
theorem-grade fact), the selection priced to D50's form choice.
LOG #467's "precisely" sentence is forward-corrected at #468.
TERMINAL for round 1.
