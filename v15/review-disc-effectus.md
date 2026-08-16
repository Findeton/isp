# K2 EFFECTUS — DISC (paper-47) — HOSTILE REVIEW

**Seat:** K2 EFFECTUS, three-seat hostile panel, v15 unit 5 (DISCRIMINATOR).
**Object, hashes verified at open and re-verified at close (all five match the
mandate):** `v15/paper-47-disc.md` `b12c4c67bac8` (654 lines) ·
`v15/code/disc_exact.py` `1d98d618c6bc` (3,099) · `v15/code/disc_output.txt`
`dc79343de5d0` (38) · `v15/code/disc_receipt.json` `c745ef39fded` (1,128) ·
`v15/note-disc-pin.md` `dbe7b26bb0d0` (2).
**Authority:** the pin; `v15/PLAN.md` (W1, W2, W-ABLATION-NOT-PREDICTION);
`v15/LOG.md` #2 (the six DISC orders) and #5; RUNBOOK through E-33.
**Status of this review:** CANDIDATE UNTIL ADJUDICATION.

---

## GRADE

**ACCEPT-WITH-MAJOR-REPAIRS.**

The measured content stands. Across 130 independent recomputations of delivered
quantities I found **zero false numbers** — every site occupation, every inverse
participation ratio, every total variation, every branch count, every fiber
count, every shot count and the whole §9 modulus table reproduce exactly from an
independent driver. The unit's central negative result is not merely intact: I
strengthened it. Sweeping a memoryless null class **6.7× wider in coins than the
one the unit swept** — 240 non-covariant integral coins × every start site ×
every direction, 9,360 configurations — produced **zero** reproductions of ISP's
tick-3 law at either plane. The finding survives a much harder opponent than the
one it was tested against.

Eight majors are nonetheless charged, and none of them is about a number. Three
are false statements the paper makes about its own instrument or its own
comparison; three are vouching gates that are materially weaker than the prose
describing them; one is a PLAN-named standard that is entirely absent; one is an
internal contradiction between two sealed receipt keys and two published
sections. The repairs are in the vouching layer and the prose, not the physics.

---

## THE MANDATE'S SIX QUESTIONS, RULED

**(1) Are the #2 orders genuinely folded?** Six of seven, yes; one partially.
Class word at every headline use — **YES** (title, `**Class:**` line, §"What kind
of result this is", head string). Demotion census primary in head and §2 —
**YES**. DISC-2 named not attempted — **YES** (§12, §14, head `SUCCESSOR=`).
Falsifier computational-regression-scoped — **YES** everywhere (one minor, m-2).
m=q internal/construction-dependent — **YES** at every mention but one (m-6).
Structure-pricing as a real comparison — **NO** (MAJOR-4). Memorylessness and
finite-horizon absorbability disclosed *where the finding is claimed* —
**PARTIAL** (m-3): the absorbability sentence occurs at exactly two places in the
object, §12's scope bullet and the head's `SCOPE=` segment, and nowhere in §6,
which is where Q147/Q148 are answered.

**(2) W-ABLATION-NOT-PREDICTION, swept and probed.** The paper's own prose is
clean — I found no live violation in any voice. The wall is not. **MAJOR-3**:
four of five planted paraphrases survive, including three of the four readings
the mandate names.

**(3) The NOT-EXPRESSIBLE ruling.** **LICENSED AND APPLIED CONSISTENTLY.** The
pin licenses the distinction in its own words; all six ISP-only observables are
classed DEFINITIONAL; the AST gate G-NULL-HAS-NO-RECORD gives the class
structural (not merely asserted) support; and the paper refuses the row as a
discriminant three times (§2, §11, and by excluding it from "the only ones that
carry weight"). One consequence is unowned: the row it says carries no weight is
still one tenth of the primary fraction (MAJOR-8).

**(4) The anti-strawman claim.** **PR3 is honest, and at AG(2,3) it is provably
the null's best available configuration — but §3's sentence generalising that is
false, and I measured the counterexample.** See MAJOR-5. No other PR row weakens
the null; PR2 (register parity) is the rule that forbids the null the enlarged
register, and the paper owns that correctly by registering DISC-2.

**(5) The tick-3 mechanism sentence.** **NARRATIVE, AND CORRECTLY LABELLED.**
§8 opens by saying the tick number is the measurement and what follows "is an
account of it, offered as an account: it explains the tick number, it is not
gated, and section 14 registers it as unproved," and §14 does register it. This
is the strongest piece of discipline in the paper and it should be cited as
precedent. The account's two load-bearing sub-claims are true on inspection
(no amplitude survives at the start site after the shift, since no declared
direction is zero; and (1,0)+(0,1)=(1,1) closes over both F_2 and F_3), but
neither is gated, which §14 says.

**(6) Referent binding, scope stamps, E-24, #299.** Referent binding —
**MAJOR-2** (the gate binds 3 of 337 numerals; four of six universes bind
nothing; the paired leg never fires). The headline scalars themselves are
unnamed — **MAJOR-7**. Scope stamps are present and unusually good (§12's
"Not decided, and named" is five real bullets). E-24 — **m-10**, three
unstamped fractions. #299-extended feasibility — **MAJOR-6**, absent.

---

## MAJORS

### MAJOR-1 — "an independent reconstruction" is the same function called twice

**The claim (paper, §front matter):** "The complete string is compared for
equality against an independent reconstruction that reads only the receipt
payload and re-renders every segment with its own format strings."

**The measurement.** `disc_exact.py` line 2317 `head = k_rebuild_head(R)`;
line 2325 `rebuilt = k_rebuild_head(R)`; line 2330 gates `head == rebuilt`.
There is exactly one head renderer in the object. G-S1-DISJOINT-CODE reports the
comparator region at 8 functions (`k_int_from`, `k_frac_from`,
`k_first_difference`, `k_agreement_checks`, `k_total_variation`, `k_max_gap`,
`k_shots`, `k_rebuild_head`); `k_rebuild_head` is the only one that renders a
head, and it is called on the same payload object both times. The gate can
therefore detect exactly one failure mode — a string edit applied to `head`
between the two calls, which is what MUT-HEAD and MUT-CLASS do
(`head.replace(...)`). It cannot detect a wrong format string, a wrong payload
key, a mislabelled segment or a stale field, because both sides of the equality
are produced by the same code from the same input.

**Why it is a major.** RUNBOOK §14 (Γ-main's own G-VERDICT-EQUALITY; R4 MAJOR-6)
engraves that delivery code must share "NOTHING with its builder — neither code,
nor inputs, nor typed literals", and names "the same concatenation written twice"
as the measured failure mode. This is that shape, under that gate name, with a
paper sentence asserting the opposite. It is also registered-unimplemented family
S-2, "two 'independent' routes through one shared component" — and the paper
elsewhere claims S-1 is met *by construction*, which makes the S-2 exposure
harder to read as an oversight.

**Licensed sentence (exact) until a second renderer exists:**

> The complete string is rebuilt from the receipt payload by the comparator and
> compared for equality against the delivered head, so a head edited after its
> gate cannot be delivered; the rebuild is not an independent route — one
> renderer produces both sides — and a second renderer is registered in
> section 14.

**Repair (preferred):** write the second renderer in the paper-side region with
its own segment order and its own separators, and gate the two against each
other after normalising order. Cost: ~40 lines.

### MAJOR-2 — G-PAPER-REFERENTS binds 3 numerals of 337; four of six universes bind nothing

**The measurement.** Receipt `paper_coverage.scanned = 337`;
`paper_referents.occurrences_checked = 3`. **0.89%.** I reconstructed the
registry from the sealed `universes` value and ran it against the paper: the
three bound occurrences are `{12, 6, 6}`, all from the single sentence "Of the 12
declared observables, 6 are formable in both models and 6 are formable only where
a record exists."

Occurrences of each declared subject noun in the paper:

| universe | declared nouns | occurrences in the paper |
|---|---|---|
| the fiber | fiber point / fiber points | **0** (the head's `NON-TRIVIAL-FIBER-POINTS` is hyphenated and inside the fence the gate strips) |
| the coin census | covariant coin / covariant coins | **0** |
| the modulus sweep | declared modulus / declared moduli | **0** |
| the census | sealed result(s) / census row(s) | 1 (a sentence with no numeral) |
| the coin family | coin of the carrier / coins of the shared family / link coin(s) | 2 (both inside quoted parent sentences) |
| the observable census | declared observable(s) | 1 |

The fiber universe — the one carrying 372, 294, 78, 6216, the first-difference
tick and the agreement upper bound, i.e. every number in the `ABLATION-EFFECT=`
and `AGREEMENT=` segments of the head — binds **nothing**, because the paper
says "points of the sweep", "interfering points" and "point of a swept fiber",
never "fiber point". The four `A of B` numeral pairs the paper does carry in
prose (512 of 640 ×2, 294 of 294, 6 of 12) all fall in sentences with no declared
noun, so **E-30's PAIRED leg fires zero times in this object**. MUT-REFERENT
plants `4242` beside "declared observables" — the one live noun — so the recipe
moves its key while exercising the only sentence in the paper where the gate can
fire at all.

**Compounding (E-23):** §13 describes this gate as "every numeral of every prose
sentence whose subject noun names a declared universe is resolved against that
universe alone, per occurrence and with the fenced block stripped, so the run's
own verdict cannot discharge the paper's obligations." Every clause is true and
the sentence conveys comprehensive coverage of an object where the gate touches
under one percent of the numerals.

**Repair:** declare the nouns the paper actually uses ("point of the sweep",
"interfering point", "trivial coin point", "site-by-tick comparison", "coin",
"modulus", "observable", "tested result"), and add a gate leg requiring each
declared universe to bind at least one occurrence — a universe that binds nothing
is a carried-and-unused family under TPL-2.

### MAJOR-3 — the new wall is defeated by four of five natural paraphrases

The wall the user engraved at #2 and the paper advertises in §13 ("it bans the
reading in which an ablation effect is reported as a first prediction, in the
voices a paper would use"). I planted six sentences and scanned all three walls.

| planted sentence | verdict |
|---|---|
| CONTROL: "Section 6 is the first parameter-free prediction of this theory." | **DIES** (W-ABLATION-NOT-PREDICTION) |
| "The third-tick site occupation is the observable that **distinguishes ISP from standard quantum mechanics**: no ordinary coined walk reaches the value section 6 publishes." | **SURVIVES** |
| "This is the theory's **first prediction** in which no number was adjusted to obtain it…" | DIES |
| "A single run of the deciding experiment would **falsify ISP** if the third-tick occupation came out at the record-free value." | **SURVIVES** |
| "The prediction of section 6 is **parameter-free**, and it is ISP's first." | **SURVIVES** |
| "ISP therefore **predicts an effect** that ordinary quantum walks do not exhibit, and the effect is physical." | **SURVIVES** |

Three of the four readings the mandate names — *distinguishes ISP from QM*,
*falsifies ISP-as-nature*, *parameter-free prediction* — walk straight through.
The cause is structural: five of the six negative legs are anchored on literal
word-orders ("first parameter-free prediction", "this is … first … prediction",
"external/empirical/experimental prediction of ISP", "tests ISP against nature"),
so any reordering or synonym escapes. E-27 requires walls to be **semantic**.
The three positive legs are all carried and are fine.

**Repair — legs to add (each verified against the clean paper to be
non-firing):**

```
r"(?:distinguish(?:es|ed|ing)?|separates?|tells? apart|parts? company) "
r"[\w\s,'-]{0,40}\bfrom\b[\w\s,'-]{0,30}(?:quantum (?:mechanics|theory)|"
r"ordinary quantum|standard quantum|textbook quantum)"
r"(?:would |could |will |can )?(?:falsif(?:y|ies|ied)|refut(?:e|es|ed)|"
r"disprov(?:e|es|ed)) (?:isp|the theory|this model)\b"
r"(?:isp|the theory|this model) (?:therefore |thus )?predicts?\b"
r"\bprediction\b[\w\s,'-]{0,25}\b(?:is|was) (?:parameter-free|free of "
r"(?:all|any) parameters)"
r"\bisp's first\b"
```

### MAJOR-4 — "zero adjustable numbers" contradicts the unit's own sealed scope key and §9

**The claim (§7):** "Five structures, zero adjustable numbers between them."
Head: `PRICE=ISP-CARRIES-5-STRUCTURES-THE-NULL-DOES-NOT-AND-0-ADJUSTABLE-NUMBERS`.

**The contradiction, in the object's own sealed values.**
`disc_receipt.json → scope.declared_free_axes` =
`['coin class', 'start site', 'coin direction', 'emission reading', 'arena',
'modulus']`. The **modulus is a declared free axis of this very run**, and §9's
own table measures it moving the headline observable across five distinct values
at AG(2,2) (58235/177147, 43392899/129140163, 4680635/14348907,
41546723/129140163, 41655923/129140163 — I reproduced all five, and all five
branch counts). A number that takes five values and moves the published
observable at every one of them is an adjustable number unless something forces
it; §9 argues it is forced, and the head stamps that forcing
`CONSTRUCTION-DEPENDENT`. So the honest price is "zero adjustable numbers given a
construction-dependent forcing", and §7 states it flatly with no conditional and
no cross-reference to §9.

**The pricing is also a gesture at the arithmetic level.** `STRUCTURE_PRICE`
(lines 157–168) is a five-row typed tuple whose third field is the literal `0` in
every row. G-STRUCTURE-PRICED's predicate is `not price_missing and adjustable
== 0`, where `adjustable` is the sum of those five typed zeros — a tautology.
MUT-PRICE drops a row, which moves `price_missing`, not the price. **No
measurement anywhere in the object establishes that any of the five structures
introduces zero adjustable numbers**, and the one number the run demonstrably
*does* carry as a dial is missing from the table.

**Licensed sentences (exact):**

> Five structures, and no adjustable number among them **once the phase modulus
> is fixed**. The modulus is the one number this comparison carries as a dial:
> section 9 measures it taking five distinct values at the smaller plane and
> moving the headline observable at every one of them, and section 9's forcing of
> it to the field order is construction-dependent in the parent's own sense. The
> price is therefore five structures and zero dials **conditional on that
> forcing**, and the conditional is the honest form.

Add the sixth row to the table: `| the phase modulus m | the map from a count to
a phase is read at modulus m | 1, forced to q by §9 given the parent's
construction |`, and change the head segment to
`…AND-0-ADJUSTABLE-NUMBERS-GIVEN-THE-CONSTRUCTION-DEPENDENT-MODULUS-FORCING`.

### MAJOR-5 — §3's anti-strawman sentence is false as measured, at AG(2,2)

**The claim (§3):** "Nothing in what follows is bought by changing the arena, the
alphabet, the coin, the state or the horizon."

**The measurement (mine; the unit never took it).** The §6 sweep varies the coin
of *both arms together*; it never varies the null's coin against a fixed ISP arm,
so §3's sentence is unmeasured in the delivered object. I ran two sweeps against
the canonical ISP declaration (Grover, origin, first direction, reading A, m=q):

| null class | configurations | distinct tick-3 laws reachable | exact reproductions of ISP | best max-gap AG(2,3) | best max-gap AG(2,2) |
|---|---|---|---|---|---|
| PR3-locked (ISP's own coin, origin, dir 0) | 1 per arena | — | 0 | 1024/19683 | 10144/59049 |
| the arena's own S_3-covariant census × every site × every direction | 972 + 48 | 90 / 16 | **0** | 1024/19683 | 10144/59049 |
| **all 240 integral coins with M Mᵀ = 9I, entries in [−3,3]** (covariance dropped) × every site × every direction | 6,480 + 2,880 | 171 / 76 | **0** | 1024/19683 | **8200/59049** |

Two rulings follow.

**(a) The finding is stronger than the unit claims, and this should be
adopted.** Over 9,360 memoryless configurations — same arena, same register
dimension, same shift, same one-basis-vector start, same horizon, no record —
**not one** reproduces ISP's tick-3 site-occupation law at either plane; and over
the census sub-sweep (1,020 configurations) no free-null tick-3 inverse
participation ratio equals ISP's published value either. That
is a materially harder opponent than PR3's census, and it is cheap: the whole
sweep runs in a few minutes on the unit's own primitives, with no new machinery.

**(b) §3's sentence is false at AG(2,2), and a published number moves.** A
memoryless plain coined walk with the non-covariant integral coin
`((-1,-2,-2),(-2,2,-1),(-2,-1,2))` at the origin in direction 0 reaches max-gap
**8200/59049** against ISP, strictly closer than the PR3 null's **10144/59049**.
Feeding that gap through the unit's own `k_shots` at confidence denominator 100
gives **5,186** shots against the published **3,389** — a 1.53× understatement of
the deciding cost against the closest memoryless opponent. At AG(2,3) PR3 ties
the best of all 6,480 (1024/19683), so the sentence is true there and false here.

**Licensed sentences (exact):**

> The reading to hold on to is PR3. The null is not given a textbook coin of its
> own and then beaten with a coin chosen afterwards: it is given the very coin
> the ISP model uses, drawn from the very census the ISP model draws from, at
> every point of the sweep. **Whether a different coin would help the null is
> measured rather than assumed: over every coin of the arena's own census and
> over all 240 integral coins satisfying M Mᵀ = 9I with entries in [−3,3], at
> every start site and every internal direction, no memoryless walk reproduces
> the third-tick law at either plane. PR3 is the null's best configuration at the
> larger plane; at the smaller a non-covariant coin comes closer — max-gap
> 8200/59049 against the PR3 null's 10144/59049 — so the published separation is
> the separation at the declared coin and not the smallest one a record-free walk
> achieves.** That parity is what makes the comparison an ablation rather than a
> contest between two theories.

§11's shot table then needs a row or a footnote: the 3,389 is the cost against
the PR3 null; against the closest memoryless walk measured here it is 5,186.

### MAJOR-6 — #299-extended feasibility is absent, and the pin's outcome words were replaced without a mapping

`PLAN.md` §Standards binds "#299-as-extended feasibility at the committed
corpus"; RUNBOOK §B backfill engraves "#299 (+#319, +#348-extension)
pre-registered outcomes with feasibility argued against the committed corpus, at
the declared row list"; the pin's last line reads "Feasibility both ways by
construction."

**The measurement:** the string `feasib` occurs **0 times** in
`paper-47-disc.md` and **0 times** in `disc_exact.py`. There is no feasibility
argument, no feasibility key in the receipt, and no gate.

**Second half.** The pin pre-registers three outcome words:
`DISC-FOUND-<the observable>` / `DISC-NULL-REPRODUCES-ALL-TESTED` /
`DISC-BLOCKED`. **None of the three occurs anywhere in the object.** The
instrument carries a two-valued pair (line 1666–1668):
`RECORD-BACKREACTION-DETECTED-AT-TICK-%d` and
`RECORD-BACKREACTION-NOT-DETECTED-IN-THE-SWEPT-WINDOW`. The rename of the
positive word is authorised by #2 and disclosed in the paper's status block; the
disappearance of the pin's other two is not disclosed anywhere, and
`DISC-BLOCKED` has no route in the instrument at all — `disc_found` is a boolean.

**Repair.** Add a short feasibility paragraph arguing, against the committed
corpus, that `RECORD-BACKREACTION-NOT-DETECTED-IN-THE-SWEPT-WINDOW` was reachable
before the run (it is: MUT-VALUES switches the coupling off and drives the
payload to it, which is the machine-checked demonstration the argument needs),
and one sentence mapping the pin's three words onto the delivered two —
`DISC-NULL-REPRODUCES-ALL-TESTED` is the census's own limit at
`PRIMARY=…10-OF-10`, and `DISC-BLOCKED` is unreachable by construction and should
be declared retired rather than left silent.

### MAJOR-7 — the head's two most prominent numbers name no quantity

§6 states "their site occupations compared site by site and tick by tick", then
"At the canonical declaration … the values are these", then a table whose columns
are `arena | tick | ISP | the null | total variation`. **The ISP and null columns
are not site occupations and are not named anywhere in §6.** I recomputed them
from the site tables printed twelve lines below: they are inverse participation
ratios — Σ p(x)² — and the instrument agrees, storing them under
`discriminant.q3.isp_ipr` / `null_ipr` and rendering them into the head as
`VALUES-AT-AG-2-3=ISP-33596579/129140163-VS-NULL-40411/177147`. The only place in
the paper that names the quantity is §9's table header ("tick-3 inverse
participation"), three sections later, for one of the two arenas.

The instrument knows the referent; the paper drops it, at the head. §11 then
compounds it: "takes any value other than the one published in section 6" —
singular, with two different published quantities in §6 to choose from.

**Licensed sentence (exact):** replace the §6 lead-in with

> At the canonical declaration — the Grover coin, the origin, the first internal
> direction, the Born-menu emission — the third-tick **inverse participation
> ratio**, Σ_x p₃(x)², takes these values on the two sides, with the total
> variation between the two full site distributions beside them.

and change the table header to
`| arena | tick | ISP inverse participation | the null's | total variation |`,
and the head's segments to `IPR-AT-AG-2-3=ISP-…-VS-NULL-…`.

### MAJOR-8 — the census gate is a cardinality identity, and the ten-row denominator is heterogeneous

**The gate.** G-Q155-CENSUS-TOTAL's predicate is
`rep + nrep + nexp == len(CENSUS) and nrep > 0` (line 2201). `CENSUS` is a
ten-row typed list whose *rulings* are literals; only the evidence strings
interpolate measurements. **No gate anywhere binds a row's ruling to its
evidence.** MUT-CENSUS rewrites every NOT-REPRODUCED to REPRODUCED and dies on
the `nrep > 0` clause — that is the ISP-unflattering direction only. A flip the
other way (any REPRODUCED → NOT-REPRODUCED) leaves the predicate satisfied
identically; only G-PAPER-CLAIMS, which compares the rendered table against the
paper's, would notice, and it would not notice a change made in both places. The
gate statement's own words — "every one of {census_rows} declared sealed results
is ruled by a measurement taken in this run" — describe a per-object binding the
predicate does not perform (RUNBOOK §14: "a predicate on an aggregate — a count …
— is vacuous at the per-object level").

**The denominator.** The ten rows are not the same kind of object:

| kind | rows | rulings |
|---|---|---|
| sealed parent results, lattice carrier (POT ×4, ACT ×1) | 5 | all REPRODUCED |
| sealed parent result, walk carrier (paper-20 coin register) | 1 | REPRODUCED |
| a measurement made here, not a sealed parent result (ticks 1–2) | 1 | REPRODUCED |
| the finding itself, not a parent result (tick 3 on) | 1 | NOT-REPRODUCED |
| a parent's **registered-and-unrun** successor test (NDEP's modulus) | 1 | NOT-REPRODUCED |
| a bundle of six definitional absences counted as one row | 1 | NOT-EXPRESSIBLE |

Every row that ISP "wins" sits in the group whose status as a *parent result* is
weakest. §12 discloses one half of this ("Six of them are sealed results of three
parents") and not the other — that neither NOT-REPRODUCED row is a sealed parent
result. Three further granularity facts move the headline fraction and are
unowned: the six definitional observables are bundled to one row while POT's four
results are counted separately; the row the paper itself rules carries no weight
is nonetheless one tenth of the primary fraction (on the paper's own ruling the
honest figure is **7 of 9**); and five of the seven reproductions are measured
against a *different null on a different carrier* (a uniform configuration plus
the counting measure on POT's L=4 lattice) than the head's single
`NULL=PLAIN-COINED-WALK` token names. §14 discloses the carrier split; nothing
discloses the referent split.

**Repair.** (i) Gate each ruling against its own evidence predicate — a
REPRODUCED row must carry a measured equality, a NOT-REPRODUCED row a measured
inequality — and add a mutant that flips a ruling in the ISP-flattering
direction. (ii) Add a provenance column to §2's table (`sealed parent result` /
`measured here` / `parent's unrun registered test` / `definitional bundle`) and
state the 7-of-9 figure beside the 7-of-10. (iii) Split the head's `NULL=` token
into the walk null and the lattice null.

---

## MINORS

**m-1.** §11: "The first column is the largest single-site gap between the two
predictions." The first column is `arena`; the gap is the second. The same
paragraph's "third column" (shots) and "fourth" (branches) are correct on the
full indexing, so the sentence is internally inconsistent. Fix: "The second
column…".

**m-2.** The head's `FALSIFIER=COMPUTATIONAL-REGRESSION-TEST-ON-A-PROPOSED-
REALIZATION` segment carries `SHOTS=36948…AND-3389…` beside it. A regression test
needs zero shots; the shot counts price a preparation the corpus has no mapping
for, which §11 says plainly and the head does not. Fix:
`SHOTS-IF-EVER-REALIZED=…` or move to its own segment.

**m-3.** Memorylessness reaches §1 (line 92, attached to the *reproduction*
reading) and §12; **finite-horizon absorbability reaches only §12 and the head's
`SCOPE=` segment.** §6, where Q147/Q148 are answered and the finding is stated,
carries only the weaker "the class of models that could reproduce it is not swept
here". Licensed addition to §6, after that clause: "and the sharper limit is that
the null compared here is memoryless — at a finite horizon a record is always
absorbable into an enlarged state description, so nothing here excludes a
memory-bearing model from reproducing these same numbers."

**m-4.** §6's "total variation" column and §11's "largest site gap" column carry
identical values at both arenas (1024/19683; 10144/59049) under different names.
They coincide because at each plane one site absorbs the entire probability
movement — a fact worth one clause, since as printed a reader may take them for
two independent measurements.

**m-5.** "The null" denotes two objects: the coined walk on AG(2,q), and (§10) a
uniform configuration plus the counting measure on POT's L=4 carrier. Compounded
by a name collision the paper does not flag: POT's *own* head calls the weight
system at which it reports 13/10 "THE-NULL". Fix: name the second object "the
record-free lattice arm" throughout §10.

**m-6.** §2's census row for the modulus ("paper-39 the connection modulus read
at the smaller arena | NOT-REPRODUCED | …") is the one mention of m=q that
carries neither the internal-check nor the construction-dependent stamp that §9,
§12 and the head all carry. Add "; internal, construction-dependent" to the
evidence cell.

**m-7.** Dead code: lines 1438–1442 compute `canonical[q]` and line 1447
unconditionally overwrites it with `GROVER`; `canonical` is then never read. A
carried-and-unused object, which TPL-2 forbids as a family. Delete.

**m-8.** §11's falsifier disjunction — "if its site occupation at the third tick
equals the record-free null's, **or** takes any value other than the one
published" — has a second clause that strictly subsumes the first. Harmless, but
it is the sealed falsifier statement (E-23 surface). Keep the first clause only
if it is meant to name the *diagnostic* case, and say so.

**m-9 (with teeth).** The G-SCOPE-DECLARED waiver's stated forcing is false. Its
text: "a declaration census with no measured predicate to corrupt; its content is
the axis list, **which G-VERDICT-EQUALITY carries into the head**." The head
carries `scope.word`, not `declared_free_axes`; I checked each axis against the
delivered head string — `coin class`, `start site`, `coin direction`, `emission
reading` and `modulus` appear **nowhere** in it, only `arena` does (as
`ARENAS=`). The machine-checked forcing actually evaluated is
`len(R["scope"]["declared_free_axes"]) > 0` — non-emptiness, a cardinality
predicate. E-23 exists for exactly this ("a description-inverted mutant is a
false waiver wearing a green badge"). Fix: either render the axis list into the
head, or restate the waiver as "its content is the axis list, whose non-emptiness
is the forcing; the list is not carried into the head."

**m-10 (E-24).** Three published fractions declare no measure and carry no
COUNTING-ONLY stamp: "present at 512 of 640 coins", "Seven of the ten tested
results", "Of the 12 declared observables, 6 …". The exhaustive fractions
(294/294, 6216/6216, 5/5, 640/640) are universally quantified and so measure-free;
the plaquette expectation is correctly stamped "counting". Fix: stamp the three.

**m-11.** POT's own head reports **four** plaquette expectations
(`13/10@THE-NULL, 262244/65615@…, 4294967399/4294967375@…, 225/152@…`) and stamps
all four `CONDITIONAL-ON-THE-DECLARED-WEIGHTS`. DISC quotes the 13/10 without
POT's conditionality stamp. The reproduction ruling is still correct — PR7 hands
the null the very measure POT's 13/10 is taken at — but the parent's own
conditional should travel with the number.

---

## WHAT SHOULD BE CITED AS PRECEDENT

1. **§8's account discipline.** A mechanism sentence stated as an account,
   explicitly ungated, registered as unproved in the successor register, with the
   successor's two exits named ("prove it or find the arena where it fails").
   This is the model form for narrative mechanism in this corpus.
2. **The AST-disjointness of the three regions** and G-NULL-HAS-NO-RECORD, which
   make the null's lack of a record a property of the source rather than a
   sentence in the paper. It is the first real mechanism the corpus has for
   registered family S-1.
3. **The refusal of the NOT-EXPRESSIBLE row as a discriminant**, stated three
   times and applied.
4. **The concession as the head.** The unit leads with its own demotion census.
   That is the shape v15 #2 asked for and it was delivered.

---

## MEASUREMENT LEDGER

**130 independent recomputations of delivered quantities — 0 disagreements, 0
false numbers.** Breakdown: 10 (five sha256-12 + five line counts, at open and at
close) · 18 (all four IPRs, both TVs, both max-gaps, both shot counts, four
sum-to-one checks, two signed-difference-zero checks, two differing-site counts,
all re-derived from the published site tables alone) · 32 (both arms rebuilt
through an independent driver: 9+1+1 and 9+1 at AG(2,3), 4+1+1 and 4+1 at
AG(2,2) — every site value, IPR and branch count matched) · 10 (§9's modulus
table, five IPRs and five branch counts) · 6 (coin censuses 36/6/1 and 4/2/1) ·
12 (fiber sweep recounted from scratch: 270/270, 54/54, 24/24, 24/24, and the
derived 294, 78, 372, 6216) · 8 (first-difference tick per coin class, six at
AG(2,3) and two at AG(2,2)) · 2 (the Chebyshev derivation and its 1/C bound) ·
4 (the modulus-descent theorem re-derived at each prime order: m∣q ∧ m≥q ⇒ m=q) ·
9 (the lattice quartic leg rebuilt from the alphabet up: alphabet 25, coins 640,
unitary rows 80, sectors 64/64/512, distribution {−2:144, 0:352, 2:144},
counting expectation 0) · 5 (stencil 37³=50653; the 3^k denominators
19683/59049/129140163/177147) · 12 (six parent anchors located in
their parents' own bytes; six parent sealed values matched, including both branch
ladders and both inverse participation ratios of paper-20).

**New measurements the unit never took:** 10,380 memoryless null configurations
(972 + 48 over the arena's own census; 6,480 + 2,880 over 240 non-covariant
integral coins), yielding 12 aggregates — zero exact reproductions of ISP's
tick-3 law anywhere, 90/16 and 171/76 distinct reachable laws, and the AG(2,2)
counterexample to §3 (max-gap 8200/59049, shots 5,186).

**Instrument probes:** 18 wall scans (6 planted texts × 3 walls), 12 referent
probes (10 noun counts, the occurrence count, the 3-of-337 ratio), 10 targeted
mutant runs, 1 full `--no-write` run (36 gates, transcript byte-matching the
delivered `disc_output.txt`).

**Targeted mutant battery (10 of 36 recipes, re-run by this seat):** MUT-CENSUS,
MUT-PRICE, MUT-WALL, MUT-WALL-POSITIVE, MUT-REFERENT, MUT-CLASS, MUT-HEAD,
MUT-VALUES, MUT-EXPRESS, MUT-FALSIFIER — **10/10 died at their declared gate,
with the named target key moved and the hook used in every case.** The battery
mechanism is sound; the majors charged above are about what the *gates* test, not
about whether the recipes reach them. MUT-VALUES is also the machine-checked
demonstration MAJOR-6's feasibility paragraph needs: switching the coupling off
drives the payload to the alternative outcome word and dies at
G-DISCRIMINANT-VALUES, which is exactly the #299 argument the object does not
make in prose.

---

## CLOSING

No number in this object is wrong, and its negative result is more robust than it
claims. What it delivers less of than it says is *vouching*: one gate compares a
function with itself, one binds 0.89% of the numerals it is described as binding,
one waiver's forcing is false, one wall lets three of four named readings past,
one census gate counts rows instead of checking them, and one PLAN-named standard
is absent. Two published sentences are false — the "independent reconstruction"
and "nothing … is bought by changing … the coin" — and one published price
contradicts the run's own sealed axis list. All of it is repairable without
touching a measurement.

**GRADE: ACCEPT-WITH-MAJOR-REPAIRS. CANDIDATE UNTIL ADJUDICATION.**
