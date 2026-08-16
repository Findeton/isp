# DISC — the discriminator: a model-ablation benchmark, and what the null already reproduces

**Status:** `DELIVERED` — built against the frozen pin `v15/note-disc-pin.md`
(sha256-12 `dbe7b26bb0d0`, v15 ledger #1), and revised under the binding user
review at v15 ledger #2, which renamed the head, reclassed the unit and
promoted the reproduction census to the primary result. Verified to run: the
plain run byte-identical twice, every gate passed, every declared recipe dead
at its declared gate with the measured key it names actually moved, the
falsification self-test fatal at every leg and writing nothing. Between
delivery and adjudication every headline below is a **candidate reading**.

## Seven of the Ten Tested Results Are Reproduced Exactly by a Record-Free Null, and What the Record Layer Does Buy Shows Up as an Ablation Effect at the Third Tick

**Unit:** DISC, v15, paper-47. **Questions:** Q147, Q148, Q149, Q150, Q155.
**Class:** this unit is a model-ablation benchmark.
**Instrument:** `v15/code/disc_exact.py`.
**Artifacts:** `v15/code/disc_output.txt`, `v15/code/disc_receipt.json`.
**Inheritance, hash-verified at run time and by no other route:** the coupled
walk, its coin, its connection and its frozen-stage control come from the
coupling unit, `v14/paper-20-coupling.md` (`4824d190af73`); the pinned
observable and its gauge behaviour come from ACT, `v14/paper-34-act.md`
(`d933221780ed`); the loop family, the perimeter law, the closed form and the
spectral row come from POT, `v14/paper-36-pot.md` (`1e495318252d`); the
untested connection-modulus test comes from NDEP, `v14/paper-39-ndep.md`
(`e2293b8c3858`); the nine template families are imported from
`v14/code/era_template.py` (`d04a3eb58fbc`) and used rather than copied.
Every object below is **reimplemented** from those definitions; no
measurement is taken from any other unit's program.

**What kind of result this is.** The null built here is this theory with one
layer removed: same arena, same internal register, same coin, same shift,
same initial state, same horizon, and no record. That is why this unit is a model-ablation benchmark: every comparison below
measures what the record layer does, and no comparison here reaches beyond
the two programs it compares. Two consequences are load-bearing and
are stated at the top rather than in a caveat. First, the seven reproductions
are the primary result: they say that seven of the corpus's own sealed
results do not distinguish this theory from a plain coined walk. Second, the
one place the ablation bites is not a prediction about nature; it is a
difference between two programs, and section 11 states it as a regression
test on a proposed realization.

**Exactness.** Integers and `fractions.Fraction` only. Walk amplitudes are
carried as integer four-tuples over the basis of the twelfth cyclotomic ring
reduced modulo its own minimal polynomial, so every Born weight is an exact
rational and equality of states is equality of tuples; the lattice leg's link
operators are carried in doubled eighth-root coordinates exactly as their
parent carries them. An abstract-syntax-tree scan of this instrument's own
source and a recursive type scan of the receipt are both gates: no
floating-point literal occurs in the source and no floating-point value
occurs in the receipt.

**S-1 by construction.** The registered-unimplemented family the era template
names first — *the comparator is the builder* — is met here structurally
rather than promised. Three code regions are disjoint by machine check: the
null's, the ISP model's, and the comparator's. The comparator calls neither
builder; the null calls nothing of the ISP model's; and no function of the
null's region names any word of the declared record vocabulary in any
identifier or argument, so the null's lack of a record is a property of the
source and not a sentence in this paper.

**The seal.** Every published object is digested at the moment the gate that
vouches its own values passes; totality is recomputed from the payload's live
key set at the door rather than from a snapshot; the artifacts are staged,
read back, compared against the gate-time digests, promoted and re-verified
from the promoted path, with no staging residue left on any exit.

**The verdict, quoted exactly as the instrument emits it.** The complete
string is compared for equality against an independent reconstruction that
reads only the receipt payload and re-renders every segment with its own
format strings, and the paper's fenced blocks are compared as a multiset
against the single block this run licenses:

```
RECORD-BACKREACTION-DETECTED-AT-TICK-3 -- CLASS=MODEL-ABLATION-BENCHMARK;NULL=PLAIN-COINED-WALK;RULES=7;SHARED-WITH-ISP=ARENA-REGISTER-COIN-SHIFT-STATE-HORIZON;ABLATED=RECORD-LAYER-CONSERVED-PRICE-STRUCTURE -- PRIMARY=THE-RECORD-FREE-NULL-REPRODUCES-7-OF-10-TESTED-RESULTS;2-NOT-REPRODUCED;1-NOT-EXPRESSIBLE;REPRODUCED=PERIMETER-LAW+CLOSED-FORM+GAP+PLAQUETTE+QUARTIC-SIGN+COIN-REGISTER-RESTRICTION+THE-FIRST-TWO-TICKS -- LATTICE=PERIMETER-REPRODUCED-BY-THE-NULL;CLOSED-FORM-REPRODUCED-BY-THE-NULL;GAP-REPRODUCED-BY-THE-NULL;PLAQUETTE-REPRODUCED-BY-THE-NULL;QUARTIC-REPRODUCED-BY-THE-NULL -- AGREEMENT=6216-OF-6216-SITE-BY-TICK-CHECKS-EQUAL-THROUGH-TICK-2 -- ABLATION-EFFECT=FIRST-AT-TICK-3-AT-294-OF-294-NON-TRIVIAL-FIBER-POINTS;NEVER-AT-78-TRIVIAL-COIN-POINTS -- VALUES-AT-AG-2-3=ISP-33596579/129140163-VS-NULL-40411/177147;TV=1024/19683 -- VALUES-AT-AG-2-2=ISP-43392899/129140163-VS-NULL-58235/177147;TV=10144/59049 -- M-EQUALS-Q=FORCED-AND-OBSERVABLE;INTERNAL-CHECK-CLOSING-THE-PARENTS-REGISTERED-TEST-NOT-AN-EXTERNAL-PREDICTION;CONSTRUCTION-DEPENDENT;OBSERVABLE-AT-5-OF-5-DECLARED-MODULI -- PRICE=ISP-CARRIES-5-STRUCTURES-THE-NULL-DOES-NOT-AND-0-ADJUSTABLE-NUMBERS;PARAMETER-FREE-IS-NOT-STRUCTURE-FREE -- FALSIFIER=COMPUTATIONAL-REGRESSION-TEST-ON-A-PROPOSED-REALIZATION;SHOTS=36948-AT-AG-2-3-AND-3389-AT-AG-2-2 -- SUCCESSOR=DISC-2-THE-SIMPLEST-MEMORY-BEARING-NULL -- SCOPE=ONE-MEMORYLESS-NULL-NOT-A-CLASS;D=2;ARENAS=AG-2-2-AND-AG-2-3;READINGS=A-AND-B;AT-FINITE-HORIZON-A-RECORD-IS-ABSORBABLE-INTO-AN-ENLARGED-STATE;NO-OPERATIONAL-UNITS;NO-LABORATORY-CLAIM;NOT-AN-EXTERNAL-PREDICTION
```

(The string is one line; the gate compares that complete string.)

---

## 1. The question, and what the answer turned out to be

The pin asks the corpus's most uncomfortable question. Its own words:

> a plain d=2 discrete-time quantum walk / lattice model with the same arena size, no record layer, no conserved-price structure

is to be built honestly, given its own full-era instrument, and then run
against the candidate discriminants already in hand. If it reproduces
everything, the honest outcome is the null's, and every reproduction is a
demotion candidate.

It reproduces most of them, and the null compared here is memoryless, which
bounds what that reproduction means. Seven of the ten rows this unit put to the null
come back exactly, and among them are the results the corpus has quoted most
often about itself: the perimeter-only law, its three-term closed form, the
gap that closed form carries, the plaquette expectation, the pinned sign
observable, and the theorem that restricts the coin register. None of those
six distinguishes this theory from a plain coined walk. That is the primary
result of this unit and it is reported first because it is the one that
changes what the corpus may say about its own work.

What the record layer does buy is measured too, and it is smaller and
sharper than the reproductions are large. With the layer removed and everything
else held fixed, the two models agree exactly through the second tick and
differ from the third on, at every interfering point of a swept fiber. That is an ablation effect: it says the feedback layer is not
inert. It leaves entirely open what a different model might do
with the same numbers: the null is one model and not a class, and section 12
says exactly why that matters.

## 2. The primary result: what the record-free null already reproduces

Every result this unit put to the null is listed with its ruling and the
measurement that earned it. A reproduction is not a defeat of the parent that
proved it; it is a statement that the parent's result does not distinguish
this theory from a plain walk, and each one is a demotion candidate for the
adjudicator to price.

| parent result | ruling | evidence |
|---|---|---|
| paper-36 the rectangle ladder is a function of the perimeter alone | REPRODUCED | per-configuration at 3200 equal-perimeter comparisons, 0 disagreements; the null's own coin is in the family |
| paper-36 the three-term closed form at every coin | REPRODUCED | 0 closed-form failures over 640 coins |
| paper-36 the halving mode and its gap | REPRODUCED | present at 512 of 640 coins, the null's own among them with coefficients 2 -1 1 |
| paper-36 the plaquette counting expectation | REPRODUCED | 11 distinct values, expectation 13/10, 56 non-flat diagonal coins |
| paper-34 the off-diagonal quartic sign pinned to a single value | REPRODUCED | the null's counting measure returns 0; the odd twists reverse the observable at every coin |
| paper-20 the coin register is forced on this offset set | REPRODUCED | 18 unitary and 0 non-monomial over 50653 maps: arena-carried |
| paper-20 the walk's distribution at the first two ticks | REPRODUCED | 6216 site-by-tick comparisons, 0 violations, over all 372 points of the sweep |
| paper-20 the walk's distribution from the third tick on | NOT-REPRODUCED | unequal at both arenas; the first difference arrives at the same tick at 294 of 294 interfering points of the sweep |
| paper-39 the connection modulus read at the smaller arena | NOT-REPRODUCED | the null is the modulus-one point of the family; the tick-three distribution takes 5 distinct values over 5 moduli |
| paper-20 the record-side observable set | NOT-EXPRESSIBLE | 6 of 12 observables of the classification are formable only where a record exists |

Seven rulings of reproduction, two of non-reproduction and one of
non-expressibility. The last row is not a victory: a definitional absence is
not a discriminant, and it is listed so that the rulings above it are read as
the only ones that carry weight.

The honest reading of the reproductions is that they follow from the shared
ground — from a uniform configuration, from a counting measure, from an
offset set — and not from the record layer at all. Sections 8 and 9 give
each one its measurement. The honest reading of the two non-reproductions is
that they are one fact seen twice: the record's back-reaction on the walk
that writes it.

## 3. The null, declared before any row runs

A null tuned to lose proves nothing, so the null's parameters are fixed by
seven rules written into the instrument's own header before any measurement
is taken. Each rule hands the null a parity with the model it is compared
against; only two of them take anything away, and the two they take away are
exactly the two structures the pin's sentence names.

| rule | datum | the null's value |
|---|---|---|
| PR1 | ARENA | the null runs on the same site set as the ISP model it is compared against -- the points of AG(2,q) with periodic identification, d=2 |
| PR2 | REGISTER | the null's internal register has the same dimension as the ISP model's -- one basis vector per declared link direction |
| PR3 | COIN | the null carries the SAME coin as the ISP model it is compared against, taken from the same S_3-covariant census over the arena's own ring; the discriminator may not be won by changing the coin |
| PR4 | SHIFT | the null's shift is the same conditional translation, carrying the amplitude at a site along its own direction and leaving the direction alone |
| PR5 | STATE | the null starts in the same state as the ISP model -- one basis vector, at the same site and the same direction |
| PR6 | STRUCTURE | the null has NO record layer: its coin is constant in space and in time, it emits nothing, and no count field exists in its region |
| PR7 | MEASURE | where a census over configurations needs a measure the null uses the uniform counting measure -- it has no conserved-price structure and declares no weight system |

The reading to hold on to is PR3. The null is not given a textbook coin of
its own and then beaten with a coin chosen afterwards: it is given the very
coin the ISP model uses, drawn from the very census the ISP model draws
from, at every point of the sweep. Nothing in what follows is bought by
changing the arena, the alphabet, the coin, the state or the horizon. That
parity is what makes the comparison an ablation rather than a contest
between two theories.

## 4. The shared ground, and the coin the arena allows

The arena is shared and is declared shared: the points of an affine plane
with three declared link directions, the conditional translation that moves
an amplitude along its own direction, and the ring the amplitudes live in.
Everything else is one model's or the other's.

The coin family is the arena's own. Over the arena's ring the covariant
unitary coins are enumerated exhaustively and sorted into classes up to a
global phase.

| arena | solutions | classes up to phase | trivial classes |
|---|---|---|---|
| AG(2, 2) | 4 | 2 | 1 |
| AG(2, 3) | 36 | 6 | 1 |

At the larger plane this recomputes the parent's own two numbers from the
definition rather than quoting them. At the smaller plane the same census
returns a fiber that has collapsed: apart from the scalar class there is one
class and it is the Grover coin, so at that arena the coin is not a
declaration with a fiber but the only interfering choice the arena admits.

## 5. The ISP arm, rebuilt and anchored to its parent

The coupled walk is rebuilt here from its parent's definitions — the coin
multiplied by the record's own diagonal phase, the shift, a division event
emitted on a cell with that cell's post-coin Born weight, every branch of the
emission tree carried with no sampling and no pruning — and it is checked
against the parent before it is used for anything. The parent's control is
quoted in its own words:

> The frozen-stage control is the same walk, the same emission rule and the same branching, on counts that never update.

and that sentence enters the gate as a value: the control's own record is
measured to stand at its initial value everywhere while the coupled arm's
does not.

| quantity | this rebuild | the parent's sealed value |
|---|---|---|
| coupled branch ladder | 3 27 486 10527 284078 | 3 27 486 10527 284078 |
| control branch ladder | 3 27 486 9234 212382 | 3 27 486 9234 212382 |
| coupled inverse participation | 35971074413334039128803/239299329230617529590083 | 35971074413334039128803/239299329230617529590083 |
| control inverse participation | 2306155/14348907 | 2306155/14348907 |

Four sealed quantities of the parent, reproduced exactly by an independent
implementation. This is what licenses the ISP arm below; it is not a new
result and it is not counted as one.

## 6. The ablation effect

The sweep is a product of every declared axis: both arenas, every coin class
of each arena's own census, every start site, every internal direction, and
both emission readings. At each point the two models are run to the swept
horizon and their site occupations compared site by site and tick by tick.

| arena | coin | first difference | points |
|---|---|---|---|
| AG(2, 2) | non-trivial | 3 | 24 |
| AG(2, 2) | trivial | none | 24 |
| AG(2, 3) | non-trivial | 3 | 270 |
| AG(2, 3) | trivial | none | 54 |

Two readings come out of that table and neither is a count of anything else.
The first is the agreement: through the second tick the two models are equal
at every comparison taken, at every point, so nothing before the third tick
separates them. The second is the parting: at every point whose coin carries
interference the site occupations differ for the first time at the third
tick, and at every point whose coin is a scalar they never differ at all.
The discriminant requires interference: at the scalar coins the two models
never separate.

At the canonical declaration — the Grover coin, the origin, the first
internal direction, the Born-menu emission — the values are these.

| arena | tick | ISP | the null | total variation |
|---|---|---|---|---|
| AG(2, 3) | 3 | 33596579/129140163 | 40411/177147 | 1024/19683 |
| AG(2, 2) | 3 | 43392899/129140163 | 58235/177147 | 10144/59049 |

Site by site at the larger plane:

| site | ISP | the null |
|---|---|---|
| (0, 0) | 1/81 | 1/81 |
| (0, 1) | 68/729 | 68/729 |
| (0, 2) | 116/729 | 116/729 |
| (1, 0) | 32/729 | 32/729 |
| (1, 1) | 0 | 0 |
| (1, 2) | 2620/19683 | 116/729 |
| (2, 0) | 32/729 | 32/729 |
| (2, 1) | 1324/19683 | 68/729 |
| (2, 2) | 8800/19683 | 32/81 |

and at the smaller:

| site | ISP | the null |
|---|---|---|
| (0, 0) | 9824/19683 | 32/81 |
| (0, 1) | 8480/59049 | 80/729 |
| (1, 0) | 12617/59049 | 281/729 |
| (1, 1) | 8480/59049 | 80/729 |

The two distributions are not merely unequal in aggregate. At the larger
plane they agree at six of the nine sites, the parting is confined to the
remaining three, and the probability it moves among those three sums to zero,
as a probability must.

**Q147 and Q148, answered at this scope and no further.** The observable on
which a record-carrying model and its record-free ablation differ is the
site-occupation distribution at the third tick. Both models express it; both
are handed the same arena, alphabet, coin, initial state and horizon; the
values above are exact rationals on both sides. The prediction is free of
every parameter the null does not also carry. What it is not is a first
prediction of the theory: it is the measured effect of one layer, and the
class of models that could reproduce it is not swept here.

## 7. Parameter-free is not structure-free

The prediction is free of every parameter the null does not also carry, and
that is worth stating precisely rather than letting it stand for more than it
is: no number in this comparison is adjustable. The
record-carrying model carries structures the null does not, and each of them
is a commitment even though none of them introduces a dial.

| structure | what it is | adjustable numbers |
|---|---|---|
| the count field | one non-negative integer per cell, initialised uniform and monotone thereafter | 0 |
| the feedback rule | the coin at a site is multiplied by the diagonal of phases the site's own counts determine | 0 |
| the emission rule | one division event per step, on a cell drawn with that cell's own post-coin weight | 0 |
| the branch structure | the state is an ensemble over emission histories rather than a single trajectory | 0 |
| the phase character | the map from a count to a phase, taken to be a character of the arena's own scalar group | 0 |

Five structures, zero adjustable numbers between them. The absence of a dial
is what makes the ablation clean; it is not an argument that the structures
are free, and a successor that wants to argue the record layer is necessary
rather than merely effective has to argue against models that carry some of
these structures too — which is exactly the successor section 12 registers.

## 8. Why the third tick, and why not the second

That the two models agree exactly through the second tick and differ from the
third on is a measurement, and the measurement is the sweep of section 6.
What follows is an account of it, offered as an account: it explains the tick
number, it is not gated, and section 14 registers it as unproved.

At the initial record every cell carries the same count, so the record's
diagonal is a scalar multiple of the identity at every site and the coupled
walk is the null's walk times a global phase. The two are therefore equal at
the first tick, and no probability can tell them apart.

The first division event lands on a cell of the start site. After the shift
no amplitude remains at the start site, so no branch's coin reads a modified
cell at the second step, and the second tick is again equal on every branch —
which is why the agreement leg reaches two ticks and not one.

The third step is the first at which a coin can read a cell an earlier step
modified, and the reason is the arena's own closure. The three declared
directions are closed under addition — the third is the sum of the first two
— so a two-shift path can land on a site that a one-shift path had already
reached and whose cells the second step's emission had already touched. The
tick at which the coupling becomes visible is the closure time of that
elementary triangle, and it is the same at both planes because both planes
declare the same three directions.

A scalar coin never mixes the directions, so the record's diagonal stays a
diagonal and no probability moves. That is why the discriminant requires
interference: at the scalar coins the two models never separate.

## 9. The connection modulus: an internal check, closed

NDEP registered a successor test and did not run it. Its words:

> The concrete successor test is to build the connection at AG(2,2) over F_2 and see whether it forces m = 2, and to find an observable the modulus does move.

and its reading of the parent's derivation:

> AG(2,2) is over F_2, so read there it predicts m = 2, a determinate and q-carried answer

The derivation being read is the coupling unit's own:

> The link connection the record defines is therefore valued in the arena's own scalar group Z_3, and the walk's phase alphabet is the cube roots of unity.

That sentence has content, and the content is a forcing **given its own
construction**. A record cell's value is an arena scalar; the parent takes
the phase to be a character of the arena's scalar group; such a map is a
function of that scalar exactly when it is constant on residues modulo the
field order, and it tells the arena's own scalars apart exactly when it is
injective on them. The two conditions are decided by integer residues alone,
so the sweep is not confined to the moduli that happen to sit in one ring.

| field order | admissible moduli |
|---|---|
| 2 | 2 |
| 3 | 3 |
| 5 | 5 |
| 7 | 7 |

At every prime field order swept, one modulus survives both conditions and it
is the field order itself. Read at the smaller plane the parent's derivation
therefore fixes the modulus two, which is what NDEP said it fixed and what
this unit's descent leg now derives rather than repeats.

This closes an obligation the corpus wrote for itself. It is not an external
prediction, and the reason is in the construction: the forcing holds for the
phase-character reading the parent chose, and a different reading of what a
connection is would carry a different forcing. What the leg establishes is
that the parent's own choice is determinate where it had been untested.

The second half of the registered test is the observable. NDEP could not see
the modulus because its census read only the count field; the parent
disclosed the reason in its own voice —

> the walk consumes the count residue n mod 3, not the count

— so an observable that moves with the modulus has to be one the walk's
amplitudes carry. The site occupation at the third tick is such an
observable, and at the smaller plane it separates the whole declared window.

| modulus | tick-3 inverse participation | branches |
|---|---|---|
| 1 | 58235/177147 | 270 |
| 2 | 43392899/129140163 | 306 |
| 3 | 4680635/14348907 | 324 |
| 4 | 41546723/129140163 | 324 |
| 6 | 41655923/129140163 | 324 |

Every value in that column is distinct, so the modulus is not invisible at
the smaller plane and the registered test is decidable there. The row at
modulus one is the null: a phase alphabet with one element is no connection
at all, and the null sits inside this family as the point the parent's
construction excludes. The remaining member of the declared window, the
twelfth, leaves the rationals — its Born weights land in the real quadratic
subfield rather than in the rationals — and the run records that rather than
dropping it.

**The register's own opening.** The descent sweep runs at prime field orders,
where the additive group of the field is cyclic. At a prime power it is not,
and the same argument would have to be made with a character of an
elementary abelian group; the corpus's own trouble at the fourth order is
the same trouble, and this unit does not close it.

## 10. The reproductions, measured rather than conceded

The three results the corpus quotes most often are lattice results, and all
three are put to the null on the shared carrier with the null's own declared
measure. POT's perimeter law in its own words:

> At every coin of the carrier and at every pair of ladder shapes of equal perimeter, the loop observable takes the same value

is a per-configuration statement about a uniform configuration, and a uniform
configuration is a thing a plain lattice model has. Its spectral row:

> The ladder's own transfer content is the closed form of section 5: spectrum {1,1,1/2} and gap 1/2, verified at every coin of the carrier and unchanged at every declared row.

names a number that this unit pulls out of the sentence and compares against
the ratio the fitted halving term actually carries between consecutive
perimeters at the null's own coin. Its plaquette row:

> the plaquette's trace takes 11 distinct values on the carrier, its counting expectation is 13/10

names a counting expectation, and a counting expectation is the null's own
measure by PR7. And ACT's pinned observable —

> the sign of the fourth power of the two off-diagonal entries, added

— whose expectation ACT reports as follows:

> Its expectation under every admissible weight system is therefore the single value zero

is pinned by a pairing under the odd twists, and the pairing is a property of
the coin family rather than of any weight system.

| parent's result | measured on the shared carrier | the null's own coin |
|---|---|---|
| perimeter-only law | 3200 comparisons, 0 disagreements | in the family: True |
| three-term closed form | 0 failures over 640 coins | coefficients 2 -1 1 |
| halving mode | present at 512 of 640 coins | present: True |
| plaquette counting expectation | 11 distinct values | 13/10 |
| off-diagonal quartic sign | 352 zero, 144 plus, 144 minus | 0 |

All five rows reproduce. The null's own coin is a member of the shared
family; its fitted ladder carries a constant term, a term linear in the
perimeter and a halving term with the coefficients shown, so the mode that
carries the parent's gap is present at the null's coin and the gap is the
null's too. The counting expectation of the pinned observable is the
parent's single value exactly.

The coupling unit's coin-register theorem is in the same position, and the
reason is worth separating from the result.

| stencil | nonzero differences | multiplicities | unitary | non-monomial |
|---|---|---|---|---|
| the arena's link offsets | 6 | 1 | 18 | 0 |
| a collinear stencil | 2 | 3 | 216 | 198 |

The theorem is carried by the arena's offset set, not by the record: on a set
every one of whose nonzero differences is realised once, no unitary
coefficient map is anything but a monomial, while a collinear set admits
many. The null shares the arena, so it inherits the theorem. A result that
follows from the shared ground is not evidence for either model over the
other, and this unit says so.

## 11. What each model can express, and the regression test

The pin is explicit that an absence is not an argument:

> the record-side observables the null lacks by construction (state which are definitional vs measurable)

so every observable this unit touches is classed before it is used. The
classes are two: whether the quantity can be formed in both models, and
whether its unavailability in the null is a measured disagreement or a
definitional absence.

| observable | expressible in | class | why |
|---|---|---|---|
| site-occupation distribution p_t(x) | BOTH | MEASURABLE | a function of the state alone |
| inverse participation ratio | BOTH | MEASURABLE | a function of the site distribution |
| total variation between two ticks' distributions | BOTH | MEASURABLE | a function of distributions |
| loop observable on a uniform configuration | BOTH | MEASURABLE | a function of the link operators |
| off-diagonal quartic sign | BOTH | MEASURABLE | a function of the coin |
| plaquette counting expectation | BOTH | MEASURABLE | a function of the coin family and a measure |
| division-count field n_l(x) | ISP-ONLY | DEFINITIONAL | the null has no count field |
| emission field and its link-class marginal | ISP-ONLY | DEFINITIONAL | the null emits nothing |
| branch count of the emission tree | ISP-ONLY | DEFINITIONAL | the null has one trajectory |
| record curvature field on the elementary triangle | ISP-ONLY | DEFINITIONAL | a function of the count field |
| maximum cell count | ISP-ONLY | DEFINITIONAL | a function of the count field |
| admissibility exit probability | ISP-ONLY | DEFINITIONAL | admissibility is a property of the record |

Of the 12 declared observables, 6 are formable in both models and 6 are
formable only where a record exists. A definitional absence is not a
discriminant. The observable of section 6 is deliberately drawn from the
first half: it is a function of the walk's own state, which the null has, and
the two models disagree about its value rather than about its existence.

**Q149 and Q150, at the class this unit actually has.** The falsifier is a
**computational regression test on a proposed realization**, not an empirical
test of nature. A program that claims to realize this model is refuted at
either declared plane if its site occupation at the third tick equals the
record-free null's, or takes any value other than the one published in
section 6. The statement is sharp because the value is exact on both sides,
and the sweep shows that the tick at which the two models part does not move
with any declared axis. The values themselves are stated at the canonical
declaration and are not claimed invariant across the axes; what the sweep
gates is the parting, not the number.

The test is finite twice over.

| arena | largest site gap | shots | branches |
|---|---|---|---|
| AG(2, 3) | 1024/19683 | 36948 | 486 |
| AG(2, 2) | 10144/59049 | 3389 | 306 |

The first column is the largest single-site gap between the two predictions,
which is the quantity a two-outcome test measures. The third column is the
number of repeated preparations that would separate the two values, computed
by Chebyshev's inequality on that gap in exact rational arithmetic at a
declared confidence denominator of 100, with no logarithm and no float
anywhere in the derivation. The fourth is the cost of the deciding
simulation: the emission tree is exhausted at that many branches, so the
regression test is decidable on a laptop. The shot count is what an
experiment would cost **if** something realised the declared register and the
declared tick. No operational mapping to laboratory units exists in this
corpus, so the shot column is a scale and not an experimental proposal.

## 12. What this decides, what it does not, and the successor

**Decided, at the declared scope.**

- Seven of the ten tested results are reproduced exactly by a model with no
  record and no price, on the parents' own carriers, with the parents' own
  numbers. Six of them are sealed results of three parents, and none of the
  six distinguishes this theory from a plain coined walk.
- Removing the record layer and holding everything else fixed changes an
  observable both models form: the site occupation at the third tick. The
  tick is the same at both planes, at every interfering coin, every start
  site, every internal direction and both emission readings.
- The connection modulus the coupling unit's construction fixes is
  determinate at every prime field order swept, and it moves an observable at
  the plane where it had never been tested. That closes an internal
  obligation.
- The model's extra structures are five and its adjustable numbers are zero.
  Parameter-free is not structure-free.

**Not decided, and named.**

- The null compared here is memoryless: its coin is constant in space and in
  time. At a finite horizon a record is always absorbable into an enlarged
  state description, so nothing measured here excludes a memory-bearing model
  from reproducing the third-tick numbers as well.
- The null is one model and not a class. This unit compared one plain coined
  walk, specified in advance, against one theory; the space of simpler models
  is not swept and no statement about that space is made here.
- The difference is measured at two planes, at a sweep horizon of three ticks
  with a horizon of five for the headline arm at the smaller plane and for
  the fidelity arm at the larger, and at two emission readings. Whether it
  persists at larger planes, longer horizons or other arities is untested.
- Nothing here is an experimental number. No operational mapping to
  laboratory units exists in this corpus.
- The reproductions of section 2 are rulings about what those parents'
  results distinguish, not about whether they are true. Every one of them
  stands as its parent proved it.

**The successor, registered.** DISC-2 is the next opponent: the simplest
**memory-bearing** null — a finite-memory coin, a state-dependent coin, a
dynamically updated phase field, or an enlarged internal register — built to
the same parity rules and put to the same third-tick observable. That is the
model this unit's result does not touch, and it is named here rather than
attempted here.

## 13. The instrument

The instrument is a single file with one entry point and a whitelisted
argument list; anything outside the list exits two. The plain run writes both
artifacts and nothing else; the no-write run writes nothing; the render mode
emits exactly the tables, claims and fenced block this paper carries; the
self-test corrupts a transcript row, adds a key after the seal and edits a
sealed value, requires each to be refused, and writes nothing.

Every gate carries a recipe that names the measured key it must move, and the
harness digests that key before and after the recipe runs: a recipe that
leaves its key identical is a sentinel and dies as one, whatever it says
about itself. The recipes are corruptions of measurements rather than of
flags — the coupling switched off in the headline arm, the sweep stopped one
tick short of its own finding, the ladder shapes grouped by their longer side
instead of by their perimeter, the exponent misread out of the parent's own
sentence, the expectation taken over one sector instead of the carrier, the
modulus read at the wrong plane, the null's two routes given different coins,
the head re-classed to the reading this unit's review struck out. Two gates
carry waivers instead, each with a machine-checked forcing.

The verbatim anchors are read through one accessor that records the read, and
each is required to occur exactly once in its pinned parent's own bytes and
once in this paper's rendering under the same canonicalisation. Each is then
consumed by the gate its own column names, and consumed for its content: the
field order comes out of the coupling unit's sentence, the modulus out of
NDEP's two sentences, the gap out of POT's spectral sentence, the trace count
and the counting expectation out of POT's plaquette sentence, the exponent
out of ACT's definition, the spatial dimension out of the pin's own
description of the null.

The paper's tables, claims and fenced block are compared against this text by
multiset equality in both directions, keyed by the table each row was
rendered into; every numeral, every exact fraction and every spelled number
in this text is required to be a value the run measured, with the declared
identifier exemptions removed first and every exemption required to occur;
and every numeral of every prose sentence whose subject noun names a declared
universe is resolved against that universe alone, per occurrence and with the
fenced block stripped, so the run's own verdict cannot discharge the paper's
obligations. Three semantic walls run against the canonicalised text, one of
them bought by this unit's own review: it bans the reading in which an
ablation effect is reported as a first prediction, in the voices a paper
would use, and it requires this paper to carry the three sentences that keep
the class straight.

## 14. The successor register

Seven things this unit leaves named.

DISC-2, the memory-bearing null of section 12, is the first and the largest.

The account of section 8 is an account. The tick number is measured at every
point of the sweep; that the arena's elementary triangle is what fixes it is
an explanation the instrument does not gate, and a successor should either
prove it or find the arena where it fails.

The sweep's horizon is three ticks. The parting is established there and the
account explains it, but whether the two models' distributions ever
re-converge at a later tick is not measured, and a re-convergence would be a
finding rather than a repair.

The descent sweep runs at prime field orders. The prime-power case needs the
character of an elementary abelian group and is the corpus's own standing
trouble at the fourth order.

The emission reading is swept over the parent's two. A reading in which the
emission is not a function of the walk's amplitudes at all would change what
back-reaction means, and no such reading is built.

The lattice legs and the walk leg are run on different carriers, because
their parents are. A single carrier carrying both the loop observable and the
walk would let the perimeter law and the third tick be measured against one
another, and would be the natural successor object.

And the shot counts assume a preparation that this corpus has no mapping for.
Until the mapping exists the test is a regression test on a program,
decidable and cheap, and it is stated as one.
