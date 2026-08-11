# PER-L — the L-ladder persistence census

*ISP v14, unit PER-L (paper 28).  Pin: `v14/note-perl-pin.md`, frozen at v14
ledger #196.  Parents at their terminal commits: R4 (paper 10, commit
583cae7), R4b (paper 15, commit 6d32993), R5 (paper 18, commit 987cd73), R2
(paper 02, terminal), and the paper-20 adjudication, whose SUCCESSOR REGISTER
carries the prediction this unit was built to test.  Instrument:
`v14/code/perl_exact.py`, with `perl_output.txt` and `perl_receipt.json`.
Between delivery and adjudication every headline here is a candidate reading.*

```
PERL-SIDON-SUFFICIENT-NOT-NECESSARY
PERL-SIDON-SUFFICIENT-NOT-NECESSARY<SIDON=SUFFICIENCY-HOLDS-AT-3-OF-3-SIDON-ARENAS(VACUOUS-AT-THE-OTHER-15;THE-IMPLICATION-HOLDS-AT-ALL-18);LINK-STENCIL-SIDON-AND-MONOMIAL-ONLY-AT-L-6-AND-8(0-AND-0-NON-MONOMIAL-OF-24-AND-24-UNITARY);NECESSITY-FAILS-AT-10-ARENAS(FIRST-IN-THE-DECLARED-ORDER=L-6-AXIS-0-1;ALL-4-LOCAL-AXES-AT-L-6-FAIL-TOGETHER)|CONTROL=THE-FOURTH-DIRECTION-DEATH-DOES-NOT-TRANSPORT(REGISTERED-54-REPRODUCED-AT-THE-CONTROL-RUNG-L-3;48-AT-L-4;0-AND-0-AT-L-6-AND-L-8-BY-THEOREM-OVER-ANY-FIELD-WITH-AN-INVOLUTION;ALPHABET-RELATIVE-0-NON-MONOMIAL-OVER-THE-25-ELEMENT-ALPHABET-OF-THE-PARENTS)|LAW=DDS-FREE-FORCES-MONOMIAL-OVER-ANY-FIELD-WITH-AN-INVOLUTION(NO-DIFFERENCE-DOUBLED-SUBSET;13-OF-18-ARENAS-DDS-FREE-AND-ALL-MONOMIAL-ONLY;SIDON-STRICTLY-STRONGER-AT-10-ARENAS;EXERCISED-IN-9-FINITE-FIELDS-AT-104-EXHAUSTIVE-SCANS)|VMAX=DIAMETER-AT-EVERY-RUNG(2;3;4=L/2)|INTERIOR-RADII=1;2;3(THE-3-AT-L-8-REGISTER-CLAIM-RE-DERIVED-FROM-A-POOL-BUILT-HERE;EQUAL-TO-THE-LOCALITY-ADMITTING-WIDTH-SET-BY-THEOREM(BOTH-ARE-{1..diam-1}))|FINGERPRINT=(ORDER,SUPPORT)-PROFILE-IDENTICAL-AT-ALL-3-RUNGS-ON-ALL-64-ANTIDIAGONAL-COINS(S1-ONE=A3;S2-EDGE=A5;S2-CORNER=A3 x A3;S2-APART=A3 x A3;S3-ROW=A7;S4-BLOCK=A8);GLOBAL-SUPPORT-IS-THE-VOLUME-16;36;64;NO-GROUP-SELECTION-LAW-CLAIMED|SCALE=THE-PARENTS-UNIQUE-SIZE-IS-WINDOW-RELATIVE(ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-L-WITH-L>=2r+2-WHOSE-RADIUS-r-BALL-CARRIES-A-DIFFERENCE-DOUBLED-SUBSET-REALISED-OVER-THE-ALPHABET;WIDTH-1={4};WIDTH-2={6,7,8};WIDTH-3={8,10,12};TWO-MECHANISMS(INVOLUTION-PAIR-EVEN-L<=4r;PERFECT-DIFFERENCE-SET-AT-L-7-r-2);EVENNESS-IS-NOT-A-LAW;BOTH-HALVES-FORCED(LOCALITY-BELOW-2r+2;INJECTIVITY-ABOVE-4r;EXHAUSTED-CENSUS-TO-SUPPORT-CEILING-4-BETWEEN);ALPHABET-RELATIVE(THE-ORDER-3-COSET-AT-L-9-r-3-CARRIES-0-OVER-THE-PARENTS-25-AND-54-OVER-THE-19-VALUE-PROBE))|BREAKS=LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-6;INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS;THE-6-NON-INTEGER-FAMILIES-ARE-THE-6-DDS-PERMITTED-NON-MONOMIAL-FAMILIES);EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(8,L)(8;24;8)|TABLE=24-ROWS(11-PERSIST(7-FORCED;4-CONTINGENT);5-BREAK;8-TRANSFORM)|SCOPE=D=2;RUNGS=L-IN-{4,6,8}+CONTROL-RUNG-L-3;FIELD=Q(ZETA-24);ALPHABET=25;WIDTHS={1,2,3};BAND-SWEEP=L-IN-2..14;STENCIL=3-TERM-AXIS-AND-THE-ANCHORED-LINK-SET;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));SECTOR=SINGLE-OCCUPATION;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-TRANSPORT-NUMBER-INHERITED;PERSISTENCE-AT-DECLARED-FINITE-RUNGS-ONLY>
```

## The Prediction Is Half Right, and the Half That Fails Is the Interesting One

A terminal unit of this programme registered a prediction: the monomial-only
theorem — the statement that a unitary generator on a declared offset set can
only be a deterministic shift — *is a Sidon property of the offset set*, and
therefore transports verbatim wherever the offsets are Sidon and dies the
moment a fourth direction is declared.  This unit is the programme's first
test of such a prediction at rungs the predictor never saw.

It passes in one direction and fails in the other, and both are measured.
Sidon does force the collapse: at the anchored link stencil, which is Sidon at
every rung of the ladder, the exhaustive scan finds no non-monomial unitary at
all.  But the collapse does not require Sidon.  At L = 6 and L = 8 the local
axis stencil is *not* Sidon — two of its four nonzero differences are realised
twice — and the collapse happens anyway, exhaustively.  Measured:
the sufficiency direction holds at every one of the 18 declared arenas, and
the converse fails at 10 of them.  The sufficiency direction is a material
implication, so it is vacuous wherever its antecedent is false:
the implication is substantively tested at the 3 Sidon arenas and holds vacuously at the other 15,
and the head carries the honest denominator rather than the flattering one.
The prediction's control fares worse still: the declared fourth
direction that kills interference at the control rung, and again at the parent
rung, kills nothing at all at L = 6 or L = 8.

What replaces the prediction is sharper than it was, and it is a theorem
rather than a correlation.  Call an offset set **difference-doubled** when
every nonzero difference realised inside it is realised at least twice.  Then
the support of *any* unitary map is difference-doubled — one line from the
unitarity condition — so if no subset of the declared offset set of size at
least two is difference-doubled, every unitary map on it is monomial, over any
field equipped with an involution.  Sidon is the special case in which *every*
internal difference is simple.  The two conditions coincide at the parent rung
and part company at the next one, which is exactly where the prediction breaks.

The rest of the ladder is a table.  The even-L theorem holds: the maximal
group speed equals the max-norm diameter at all three rungs.  The register's
own successor parameter is re-derived from a pool this unit built itself: the
interior-radius count is 1, 2 and 3, and it is also the number of window
widths at which the inherited locality criterion still returns locality —
the same *set*, not merely the same count, and by a theorem about the two
definitions rather than by a coincidence.  The gauge
fingerprint is inert along L: the (order, support) profile is identical at all
three rungs, on every coin of the antidiagonal sector.  Five invariants break,
all of them at L = 6, and they are one mechanism with a residue.

And one row is a reversal rather than a break.  R4's admissible set was a
single lattice size, and this unit re-derives that set at R4's own window
width — and then finds that it is the width-1 section of a band.
At window width 1 the admitted set is [4], and
at window width 2 it is [6, 7, 8], and at width 3 it is [8, 10, 12].
The uniqueness was real and it was resolution-relative.  The odd size in the
width-2 section is the sharp part: it is carried by a *perfect difference
set*, a second mechanism the cheap construction cannot see, and it is why the
band's evenness — which an earlier reading of this unit asserted as a law — is
not a law at all.

---

## 1. The question, and what would have answered it the other way

The pin asks whether the forced results of the L = 4 arc persist at L = 6 and
L = 8, with a per-invariant verdict and an exact witness for each.  Stage 1 is
decisive and is reported in the head regardless of everything else: the
registered Sidon prediction either passes per arena or it does not.

The register's third leg — transport to paper-20's own R = 4 arena — is not
tested here; this unit never enters the R-ladder.  Section 11.5 closes that leg
by theorem instead, which is cheaper than the census it replaces.

Five outcomes were pre-registered, three of them Sidon verdicts, and two of
those three are not the one delivered.
`PERL-SIDON-CONFIRMED-BOTH-WAYS` would have been the head had the
biconditional survived — had every non-Sidon arena carried a non-monomial
unitary.  `PERL-SIDON-REFUTED` would have been the head had a Sidon arena
carried one, which would have falsified the prediction outright and taken the
parent theorem's mechanism with it.  Both were reachable: the instrument scans
the offset sets exhaustively over the declared alphabet and reports what it
finds, and at the parent rung it finds 48 non-monomial unitaries on the very
stencil that is empty two rungs up.  The delivered head is the third,
`PERL-SIDON-SUFFICIENT-NOT-NECESSARY`, and the two legs that produce it are
measured separately and gated separately.  The other two pre-registered forms
are blocking outcomes — `PERL-BLOCKED-AT-THE-FAMILY-GENERALISATION` had the
declared rule failed to reproduce the parent's pool at the parent rung, and
`PERL-BLOCKED-AT-THE-EIGENPHASE-LATTICE` had an eigenvalue at a new rung
turned out not to be a root of unity, which would have made the dispersion
census inexact and stopped the ladder there.  Both are gated, and neither
fired.

What this unit does **not** do is take a limit.  Persistence at three declared
finite rungs is what is measured; the verdict says so in as many words, and no
transport number is inherited from the momentum parent, whose scope stamp
travels with its rows.

## 2. The arena, and the generalisation rule, declared

Nothing about the stage is chosen here.  The dimension, the coefficient
alphabet, the connective, the anchored link set and the stencil are read from
the parents' receipts at named paths and gated against the values frozen in
this unit's declaration; a drifted parent dies at the byte anchors before a
number is computed.  Ten files are read at run time, all hash-pinned, and no
other repository state is touched — no ledger, no status file, no other unit's
working copy, and no subprocess.

The declared rungs are L = 4, L = 6 and L = 8, and there is a **fourth lattice
size in the sweep**: the control of section 3.4 runs at L = 3, paper-20's own
arena, which is where the registered count lives.  It is named in the scope
segment beside the ladder, and the scope segment is rendered from the same two
constants the run uses.

**The family-generalisation rule is declared, and its fiber is priced.**  R4's
construction is applied verbatim at each rung: the axis set is every nonzero
offset modulo sign — exhaustive, not sampled, with fiber the axis count at
that rung and every instance run; the stencil is the parent's three-term
{0, a, −a}; the alphabet is the parent's 25 elements, held fixed along L
because a moving alphabet would make the rungs incomparable; and the quotient
is the parent's global-phase gauge, which is measured to act freely at every
rung.  The rule is not new machinery, and the gate that proves it is not new
machinery is the one that matters: run at the parent rung it returns the
parent's own pool exactly.

The arithmetic is exact throughout.  The field is Q(ζ_24), which contains the
parents' Q(ζ_8) together with the sixth and third roots of unity the L = 6 and
control rungs need; its defining polynomial is computed by exact division
rather than typed, the representation is canonical, and an AST scan of the
instrument plus a recursive type scan of the receipt gate the absence of
floats.

**Two independent routes build the pool at the parent rung.**  The delivery
route evaluates the unitarity condition at the lags that can receive a term,
and the fact that no other lag can is bound as a gate over every axis and
every lag of the group — 2940 axis-and-lag objects are bound.  The second
route is the parent's own criterion written over the whole torus, with no
structural shortcut at all, and the two routes return the same generators.

## 3. Stage 1 — the Sidon test

### 3.1 The criterion, and the theorem that replaces the prediction

A generator is a coefficient map c on a declared offset set S; its matrix
moves an occupied site by v with amplitude c_v, and it is unitary exactly when
its periodic autocorrelation A(m) = Σ_v c_v conj(c_{v+m}) is a delta.  For
m ≠ 0 the terms of A(m) are precisely the ordered pairs of the support with
difference m.  Everything in this section follows from reading that sentence
as a counting statement.

> **Theorem (the DDS criterion).**  Let S be an offset set in a finite abelian
> group and let c be a unitary coefficient map supported on S.  Then supp(c)
> is *difference-doubled*: every nonzero difference realised inside it is
> realised at least twice.  Consequently, if no subset of S of size at least
> two is difference-doubled, every unitary map on S is monomial — over any
> field equipped with an involution, the trivial involution included.

*Proof.*  Suppose some m ≠ 0 is realised inside supp(c) by exactly one ordered
pair (v, w), so v − w = m.  Then A(m) has exactly one term and reads
c_v · conj(c_w) = 0; but v and w lie in the support, so neither factor
vanishes.  Contradiction.  Hence every internal difference is realised at
least twice.  The consequence is immediate: a support of size at least two
would be a difference-doubled subset of S. ∎

The proof uses exactly two properties — a product of two nonzero elements is
nonzero, and the involution takes nonzero to nonzero — so the phrase to use is
*a field equipped with an involution*, not "a field closed under conjugation":
a field is not closed under conjugation, and what the argument needs is the
extra structure.  Section 3.5 exercises the theorem outside characteristic
zero, where the distinction bites.

A Sidon set — one in which every nonzero difference is realised exactly once —
has no difference-doubled subset at all, so Sidon implies the hypothesis.  The
implication is strict, and the witness is the parents' own stencil: {0, a, −a}
with a of order at least 5 realises ±a twice and ±2a once, so it is not Sidon,
yet the simple differences ±2a already forbid a support containing both a and
−a, and the remaining lag then forbids the rest.  The criterion is
combinatorial, it names no field, and it is exhaustive over subsets at every
arena this unit declares.

**The criterion subsumes four earlier results, not three.**  Beyond R4's
order-collapse theorem and paper-20's coset mechanism, R4 also proved a
**Moore-ball collapse** — *let L ≥ 5 and let U be a unitary generator on
(Z_L)² whose coefficient map is supported inside the radius-one Chebyshev
ball; then U is monomial* — with the consequence that no local stencil
whatever admits a non-monomial unitary at any L ≥ 5, over any field.  R4's
proof runs through the aperiodic cross-correlation and an integral-domain
argument.  The DDS criterion gets it in two lines from a subset census, and
this unit's width-1 row (section 7) is that statement re-proved by counting.
The novelty at width 1 is the proof, not the fact.

### 3.2 The arenas, and what the scan finds

Eighteen arenas are declared: at each rung, the anchored link stencil, the
three-term stencil at each of the four local axes, and the link stencil with
the fourth direction paper-20 declared.  Each is scanned exhaustively over the
parents' 25-element alphabet.

| L | arena | Sidon | DDS-free | difference multiplicities | unitary | non-monomial |
|---|---|---|---|---|---|---|
| 4 | LINK | True | True | [1, 1, 1, 1, 1, 1] | 24 | 0 |
| 4 | AXIS-0-1 | False | False | [2, 2, 2] | 72 | 48 |
| 4 | AXIS-1-0 | False | False | [2, 2, 2] | 72 | 48 |
| 4 | AXIS-1-1 | False | False | [2, 2, 2] | 72 | 48 |
| 4 | AXIS-1-3 | False | False | [2, 2, 2] | 72 | 48 |
| 4 | LINK-PLUS-4TH | False | False | [2, 2, 2, 1, 1, 1, 1, 1, 1] | 80 | 48 |
| 6 | LINK | True | True | [1, 1, 1, 1, 1, 1] | 24 | 0 |
| 6 | AXIS-0-1 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 6 | AXIS-1-0 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 6 | AXIS-1-1 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 6 | AXIS-1-5 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 6 | LINK-PLUS-4TH | False | True | [2, 2, 1, 1, 1, 1, 1, 1, 1, 1] | 32 | 0 |
| 8 | LINK | True | True | [1, 1, 1, 1, 1, 1] | 24 | 0 |
| 8 | AXIS-0-1 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 8 | AXIS-1-0 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 8 | AXIS-1-1 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 8 | AXIS-1-7 | False | True | [2, 2, 1, 1] | 24 | 0 |
| 8 | LINK-PLUS-4TH | False | True | [2, 2, 1, 1, 1, 1, 1, 1, 1, 1] | 32 | 0 |

*Scope: exhaustive over the declared alphabet raised to the offset count at
every row; 1952424 coefficient maps are scanned in all, counting the control
rung of section 3.4.*

Read off the table:
the link stencil is Sidon at every rung, and its scan returns 24 unitary maps
of which 0 are non-monomial at L = 6; at L = 8 the same stencil returns 24
unitary maps and 0 non-monomial.  So the prediction's own direction — Sidon
offsets force the collapse — **passes at both new arenas**, and it passes for
the reason the prediction gave.

Against that,
the local axis stencil carries 48 non-monomial unitaries at the parent rung,
and 0 at L = 6 and 0 at L = 8, with the same non-Sidon
difference multiplicities [2, 2, 1, 1].  The Sidon status of that stencil does not move
along the ladder — it is false at every rung — while the conclusion it was
supposed to control moves at L = 6.  That is the converse failing, and it is
the first place in this programme where a registered prediction has been
measured wrong at a rung its author never ran.  The failure is not localised
to one arena: at L = 6 **all four local axes** are non-Sidon, DDS-free and
monomial-only simultaneously, so they fail together and "the first one" names
the head of the declared arena list and nothing more.

Every DDS-free arena is monomial-only, with no exception anywhere on the
table, and
the count 13 of 18 is stamped COUNTING-ONLY in the receipt: it is a
coverage report over this unit's own declared arena list, which is not a
sample of any population.  So is the 3 of 3 of the substantive sufficiency
row, and so is the necessity count; the census that finds them scans the
rendered paper and the verdict string rather than a list this unit volunteers.

### 3.3 Why the two rungs differ, exactly

At order 4 the stencil {0, a, −a} has 2a = −2a, so *all three* of its nonzero
differences are doubled and the criterion forbids nothing; the alphabet then
supplies 48 solutions.  At order 6 and order 8 the element 2a is no longer its
own negative, ±2a become simple, and the criterion forbids everything but a
shift.  A local axis has order exactly L, so the parent rung is the last rung
at which a local axis can carry interference at all: the three-term stencil
fails to be difference-doubled-free exactly at orders 2, 3 and 4 — at order 2
the axis is itself an involution, at order 4 its double is, and at order 3 the
stencil is a whole coset — and 4 is the largest of the three.  The parent's own presence set for
non-monomial local generators was {2, 4} with a gap at 3 that the parent
declared alphabet-relative without giving a mechanism, and the mechanism is
now supplied: at order 3 the stencil is a full coset of a cyclic
subgroup, so it *is* difference-doubled and the criterion forbids nothing —
the emptiness there is alphabet-relative, exactly as the parent declared it,
and not structural.  The criterion does not *subsume* the order-3 gap; it
declines to forbid there, which is why the emptiness has to be a fact about
the alphabet.

### 3.4 The control: the fourth-direction death does not transport

The registered control says that declaring a fourth direction kills the
theorem and that 54 non-monomial unitaries appear.  That number is reproduced
here independently, from the definitions, at the control rung — which is
**L = 3, paper-20's own rung, not a rung of this ladder** — and over the
probe alphabet that produces it: the registered count is reproduced exactly:
54 non-monomial unitary maps, with the same witness support — the three
offsets that form a coset of a cyclic subgroup.

| arena | alphabet | size | maps | unitary | non-monomial |
|---|---|---|---|---|---|
| LINK | R4-25 | 25 | 15625 | 24 | 0 |
| LINK | UNIT-7 | 7 | 343 | 18 | 0 |
| LINK | THIRDS-19 | 19 | 6859 | 18 | 0 |
| LINK-PLUS-4TH | R4-25 | 25 | 390625 | 32 | 0 |
| LINK-PLUS-4TH | UNIT-7 | 7 | 2401 | 24 | 0 |
| LINK-PLUS-4TH | THIRDS-19 | 19 | 130321 | 78 | 54 |

*Scope: exhaustive over each probe alphabet at the control rung L = 3.*

Two things follow, and both are disclosures the register did not carry.

**The count is alphabet-relative.**  Over the parents' own 25-element
alphabet the same offset set at the same rung carries no non-monomial unitary
whatever.  The death is a joint property of the offset set and the alphabet:
the offset set makes it *possible* by carrying a difference-doubled subset,
and the alphabet decides whether anything realises it.  The verdict carries
the disclosure rather than the bare 54.  The same disclosure is carried by the
SCALE clause, for the same reason and with its own measured witness
(section 7): admission at a window width is a joint property of the ball and
the alphabet, and the 19-value probe that produces the control's 54 produces a
non-monomial unitary at an odd size the parents' 25 leaves empty.

**The death does not transport up the ladder.**  Measured along the rungs,
the same fourth direction carries 48 non-monomial unitaries at L = 4 and 0 at
L = 6 and 0 at L = 8.  At
the control rung the mechanism is a coset of a cyclic subgroup of order 3; at
the parent rung it is a different mechanism entirely — two of the four offsets
differ by an involution, which doubles that difference all by itself.  At
L = 6 and L = 8 neither mechanism is available to those four offsets, the set
is DDS-free, and the collapse is forced.  Those two zeros are therefore
**theorems, not scans**: a DDS-free offset set is monomial-only over any field
with an involution, so the zeros hold over every alphabet, not merely over the
parents' 25.  "Dies at any declared fourth
direction" is therefore false as stated: it dies at a fourth direction that
introduces a difference-doubled subset, and whether a given fourth direction
does that is a property of the rung.

### 3.5 The theorem outside characteristic zero

The field-freeness of section 3.1 is a claim about a proof, and a proof read
only in characteristic zero is a proof read in one place.  The instrument
therefore exercises the theorem in nine finite fields — F_2, F_3, F_5, F_7,
F_11, F_4, F_9, F_25 and F_49 — with the involution taken as the **Frobenius
computed in the field**, never assumed to be b ↦ −b, which is the identity in
characteristic 2.  The involution is verified exhaustively to be an order-2
(or trivial) field automorphism before a single map is scanned.

The arenas are the parent's own three-term stencil at every order the order
census sweeps, together with the anchored link set and the link-plus-fourth
set on small tori.  Every (field, arena) pair small enough for an exhaustive
scan is run:
104 exhaustive scans over 9 finite fields, 0 violations.
Of those, 63 are on DDS-free offset sets, and every one of them returns a
monomial-only arena.

The case worth naming is F_4, where 1 = −1: there b ↦ −b is the identity, the
Frobenius is not, and characteristic zero cannot exhibit the configuration at
all.  The theorem holds there too.  The four (field, arena) pairs above the
declared scan window are listed in the receipt rather than run; the theorem is
*proved*, and this exercise is what stops the proof from being read in one
characteristic only.

## 4. Stage 2 — VMAX = diameter, and the interior radii

The momentum parent proved that the maximal group speed equals the max-norm
diameter at every even size, and verified it over a range by an argument about
the antipodal monomial shift.  This unit re-derives it in-unit at the two new
rungs, from a pool it built itself, and does not silently re-run the parent's
own sweep.

| L | families | cells | VMAX | diameter | interior radii | eigenphase lattice |
|---|---|---|---|---|---|---|
| 4 | 58 | 928 | 2 | 2 | 1 | 8 |
| 6 | 42 | 1512 | 3 | 3 | 2 | 24 |
| 8 | 106 | 6784 | 4 | 4 | 3 | 8 |

*Scope: exhaustive over the rebuilt pool and the full dual torus at each rung.*

In the ladder's own terms,
the maximal group speed is 2, 3 and 4, and the max-norm diameter is the same
number at each rung.  The ceiling is not merely a bound: the monomial shift by
the antipodal offset is a unitary member of the built family at every rung and
a family of the pool attains L/2 there, which is gated separately from the
bound itself.

**The register's parameter is re-derived, and then joined to something else.**
Measured at each rung,
the interior-radius count is 1, 2 and 3.  The momentum parent's own table
already carries these rows — it tabulates the interior radii at L in
{4, 6, 8, 10, 12} and its prose says "one here, 3 at L = 8" — and the quantity
is the number of radius classes strictly between 0 and the diameter, that is
L/2 − 1, by inspection.  What this unit adds is not the number but the route:
it is re-derived from a pool this unit built itself, and section 6 shows that
the same three numbers count something the parent was not measuring.

**One invariant breaks here, and its witness is exact.**  The parent measured
that every group velocity on its stage is an integer, over all of its velocity
cells, and derived the reason from a parity grading of the coefficient field.
Re-measured along the ladder: 6 families at L = 6 carry a velocity that is
not an integer.  The witness is an order-2 axis carrying a two-term generator,
whose phase advances by a quarter turn per momentum step and
whose speed is 3/2.  The property survives at L = 8, but not for the parent's
reason — there it survives because the eigenphase lattice and the lattice size
coincide, so the velocity is a lift and nothing else.

The momentum parent's scope inventory requires a successor that inherits its
reading to match all three velocity coordinates — the stencil, the lift and
the residual.  Two are declared in section 11; the third, the residual fiber
the parent measured inert, is not re-measured here, and the break survives it:
the parent's residual varies the *sign* only, and this witness sits at a phase
step of ±6 in Z/24 rather than at the tie at 12, so no choice of lift can
reach it.

**The eigenphase lattice itself transforms, and the law is clean.**  Measured
over the whole declared gauge orbit, the eigenvalues at rung L generate the
group of lcm(8, L)-th roots of unity: 8, 24 and 8.  The 8 is not a fact about
the stage and not a free constant either: it is the order of the declared
global-phase gauge group, which this unit measures to act freely at every
rung.  The law is Z/lcm(|gauge|, L), and the parent's Z/8 was the coincidence
lcm(8, 4) = 8.  Every eigenvalue
at every cell of every rung is a root of unity — that survives, and it is what
makes the census exact.

## 5. Stage 3 — the gauge fingerprint along L

The gauge parent's coin family is derived from the same coefficient alphabet
as the generators, and the derivation mentions no lattice size at all: the
derived coin family has 640 members at every rung, splitting into 64 diagonal,
64 antidiagonal and 512 balanced with nothing left over.  What does depend on
the rung is the arena the coins act on — 2L² links, L² plaquettes, and four
parity strata, each measured to be a perfect matching of the site set at every
rung of the ladder.

In this unit's own run,
the profile is measured at 18 rung-and-stencil rows and is identical at all
three rungs, on every one of the 64 antidiagonal coins:

| stencil | order | support | orbits | class | L = 4 | L = 6 | L = 8 |
|---|---|---|---|---|---|---|---|
| S1-ONE | 3 | 3 | 3 | A3 | same | same | same |
| S2-EDGE | 60 | 5 | 5 | A5 | same | same | same |
| S2-CORNER | 9 | 6 | 3 + 3 | A3 x A3 | same | same | same |
| S2-APART | 9 | 6 | 3 + 3 | A3 x A3 | same | same | same |
| S3-ROW | 2520 | 7 | 7 | A7 | same | same | same |
| S4-BLOCK | 20160 | 8 | 8 | A8 | same | same | same |

*Scope: exhaustive over the antidiagonal sector at every listed stencil and
every rung; the certificate is set equality — containment in the product of
the alternating groups on the orbits, plus equal cardinality — evaluated per
object, never as a fingerprint of element orders.*

**Twelve of these eighteen rows are the gauge parent's own.**  Its refinement
table publishes the same six-stencil profile at L = 4 and at L = 8, on the same
64 antidiagonal coins.  The six rows at L = 6 are new, and what they add is
that the parent's non-wrapping argument covers a rung *between* its two.

The alternating-on-orbits character therefore persists, and it persists for a
reason the unit measures rather than assumes: no declared local stencil wraps
at any rung, so the generators at the three rungs are the same maps on the
same relative coordinates.  The forcing sentence is the gauge parent's — it
wrote, at its own doubling step, that local stability could not have come out
otherwise at any size at least as large as the widest declared stencil — and
it is quoted rather than rediscovered here.

At the global stencil the support is the volume.  Every plaquette holonomy is
measured to be a three-cycle and the family is measured to be transitive on
the whole site set; the *class* is the gauge parent's, argued there and not
re-argued here, and the classical theorem it rests on needs primitivity rather
than transitivity, which is a reason to leave the argument where it was made.
What this unit publishes is the support:
the global support is 16, 36 and 64, which is the volume at each rung — the
two outer values are the gauge parent's own anchored numbers, and the middle
one is new.

**No group-selection law is claimed here.**  That question belongs to a
different unit.  What is entered is the datum: the fingerprint is inert along
the ladder, and the only thing that moves is the volume.

## 6. Stage 4 — locality windows

The locality criterion is R2's, ported verbatim from its receipt: locality
exists at a rule iff some connected component of that rule's overlap graph is
not complete.  R4 applied it at radius one and swept the *dimension*, finding
the same threshold at every dimension.  R2's own width law says what the
missing coordinate is: locality survives exactly while the window is narrower
than the diameter of the index set.  This unit applies the criterion at that
coordinate — the window width r of the neighbourhood ball — and recomputes
only the new rows.  R2's census is cited and not re-run.

| L | r | neighbours | nonzero offsets | complete | locality | b₁ |
|---|---|---|---|---|---|---|
| 4 | 1 | 8 | 15 | no | yes | 49 |
| 4 | 2 | 15 | 15 | yes | no | 105 |
| 6 | 1 | 8 | 35 | no | yes | 109 |
| 6 | 2 | 24 | 35 | no | yes | 397 |
| 6 | 3 | 35 | 35 | yes | no | 595 |
| 8 | 1 | 8 | 63 | no | yes | 193 |
| 8 | 2 | 24 | 63 | no | yes | 705 |
| 8 | 3 | 48 | 63 | no | yes | 1473 |
| 8 | 4 | 63 | 63 | yes | no | 1953 |

*Scope: every width from one up to the first complete window at each rung.*

Counted from the table above,
the number of window widths admitting locality is 1, 2 and 3.  That is the
interior-radius count, rung for rung — and the agreement is **forced by the
two definitions rather than measured across two instruments**.  Completeness
is "the radius-r ball covers the torus", so locality survives exactly while
r is less than the diameter, and the locality-admitting widths are
{1, …, diam − 1}; the interior radii are the radius classes strictly between 0
and the diameter, which is the same set.  It is an identity of *sets*, not of
counts, it holds for any connective and any L, and the instrument measures it
that way: across every size of the band sweep — 13 sizes, 6 of them odd —
the two sets agree and both are {1, …, diam − 1}.  That makes it the one
result here that says anything about odd rungs and says it honestly.

R2's partition corollary transports too, and is run as the control: every
blockwise atlas of this stage — the torus cut into b × b blocks for every
divisor b — is measured clique-only at every rung.  The adjacency is
*evaluated*: every pair inside a cell is tested against the same-chart
relation and counted, and every pair across two cells is tested and required
to be non-adjacent.  So no partition of this stage can produce a non-complete
component, and locality here is carried by the sliding window and by nothing
else, which is the shape R2 measured on its own arena.

## 7. The band: the parent's unique size is the width-1 section

R4's precheck met two requirements at one point.  Locality required L at least
4; a non-monomial local generator required L at most 4; the admissible set was
a single size.  Both halves are re-derived here at R4's own width, and both
halves move when the width does.

*Locality* at width r fails exactly when the radius-r ball covers the torus,
which happens at 2r + 1 ≥ L; so locality requires L ≥ 2r + 2, and at r = 1
that is the parent's own threshold.  *Interference* at width r requires a
difference-doubled subset inside the ball **that the alphabet realises**.  Two
things make that a decidable question rather than an open one.

**The support-size ceiling.**  The declared alphabet's squared moduli are
1/4, 1/2 and 1, so a unitary map's squared moduli sum to 1 with at most four
nonzero coefficients and the profile is forced: two of squared modulus 1/2, or
one of 1/2 with two of 1/4, or four of 1/4.  Measured from the rebuilt
alphabet rather than assumed:
a unitary map over this alphabet has at most 4 nonzero coefficients.
The whole admission question is then a finite census over the ball's subsets
of size two, three and four.

**The injectivity theorem.**  Lift the radius-r ball to {−r, …, r}² in Z².
Two lifted differences lie in {−2r, …, 2r}² and are congruent mod L only if
they differ by L·e with |L·e_i| ≤ 4r, so e = 0 whenever L ≥ 4r + 1; the
lifted difference map is then injective, every internal difference of the ball
is realised by exactly one ordered pair, and the ball is difference-doubled-
free.  The hypothesis is evaluated over the whole lifted difference box at
every width and size of the sweep, and the measured injectivity agrees with
the threshold 4r + 1 at every one of them.

So the absence half is forced everywhere: below 2r + 2 by locality, above 4r
by injectivity, and in between by an exhaustive census that the ceiling makes
finite.  The census runs and decides.

| r | admitted sizes | involution-pair section | beyond that mechanism |
|---|---|---|---|
| 1 | [4] | [4] | - |
| 2 | [6, 7, 8] | [6, 8] | [7] |
| 3 | [8, 10, 12] | [8, 10, 12] | - |

*Scope: every width in {1, 2, 3} against every size from 2 to 14; presence is
constructive and verified against the parent's whole-torus criterion at every
admitted size, and absence is exhausted at every excluded size that locality
does not already exclude.*

Reading the table:
at window width 1 the admitted set is [4], re-proving the parent's own
radius-one ball theorem by a second, counting argument, and
at window width 2 it is [6, 7, 8], and at width 3 it is [8, 10, 12].

**Two mechanisms, and evenness is not a law.**  The cheap one is a pair of
offsets differing by an involution, which exists exactly when the ball reaches
halfway across the torus — that is when L is even and L ≤ 4r.  A pair like
that carries an explicit unitary: put 1/√2 on one offset and i/√2 on the
other, both in the parents' declared alphabet, and the single surviving lag
reads twice the real part of c_v · conj(c_w), which vanishes.  That
construction has its own section, and the closed form "the even L in
[2r+2, 4r]" is exactly right *about it* — a true combinatorial identity, gated
as such, at all three widths.  It is not the admitted set.

The second mechanism is a **perfect difference set**.  At L = 7 and width 2
the support {(0, 0), (0, 1), (0, 2), (0, 5)} lies inside the radius-2 ball,
with
Chebyshev norms 0, 1, 2 and 2, and every one of its six nonzero differences is
realised exactly twice: it is a (7, 4, 2) difference set, the complement of
the Fano set.  On it, c = ½(δ₍₀,₀₎ + δ₍₀,₁₎ − δ₍₀,₂₎ + δ₍₀,₅₎) has every
coefficient in the declared alphabet, is non-monomial, and is unitary.  The
witness is verified two ways in-run: the periodic autocorrelation is a delta,
and
the full 49 by 49 matrix satisfies U-dagger-U = I, all 2401 entries checked, 0 mismatches.
Locality holds at that cell, and it is gated with the rest of the witness.

The species matters more than the size.  **Z_7² contains no involution at
all**, so the pair mechanism is not merely absent at L = 7, it is
structurally unavailable, and a search built on it is blind to this witness by
construction.  An earlier reading of this unit asserted the band's evenness as
a law; the law was the section of one construction, and the construction's
own section is what section 7's third column now reports.

**The clause is alphabet-relative, and the disclosure is measured.**  Whether
a difference-doubled subset realises anything is a property of the alphabet,
exactly as in section 3.4.  The measured witness is the order-3 coset
{(0, 0), (3, 0), (6, 0)} inside the radius-3 ball at L = 9, where locality
holds:
it is difference-doubled with multiplicities [3, 3], and it
carries 0 non-monomial unitaries over the parents' 25 and 54 over the 19-value probe
— the control's own count, at an odd size, three widths up.  So the width-3
section published above is the section *over the parents' alphabet*, and the
verdict says so in the SCALE clause itself.

The reading is nevertheless sharp, and it is a second relativity rather than a
reversal.  R4 registered, in its own false-claim register, that its unique
scale is a theorem about the declared link set of the record stage rather than
a law of the substrate — connective-relativity, registered by the parent
itself.  Window-relativity is the second coordinate of the same species of
fact.  The parent's headline — one lattice size admits a local family carrying
interference — is true, is re-derived, and is a statement about the parent's
*window*.  At radius one the admitted set is still exactly [4], and both
halves are still forced there.

## 8. Stage 5 — the persistence table

One row per invariant, three cells per row, and a verdict bound to its own
cells: PERSISTS requires the three to agree, BREAKS and TRANSFORMS require
them not to.  The binding is per row and never in aggregate.

| invariant | L = 4 | L = 6 | L = 8 | verdict |
|---|---|---|---|---|
| the LINK stencil is Sidon | True | True | True | PERSISTS |
| monomial-only on the LINK stencil | 0 | 0 | 0 | PERSISTS |
| the local AXIS stencil is Sidon | False | False | False | PERSISTS |
| non-monomial generators on a local AXIS stencil | 48 | 0 | 0 | BREAKS-AT-L=6 |
| the local AXIS stencil carries a difference-doubled subset | True | False | False | BREAKS-AT-L=6 |
| the fourth-direction death | 48 | 0 | 0 | BREAKS-AT-L=6 |
| circulant families in the pool | 58 | 42 | 106 | TRANSFORMS |
| non-monomial families in the pool | 42 | 6 | 42 | TRANSFORMS |
| local non-monomial families in the pool | 24 | 0 | 0 | BREAKS-AT-L=6 |
| VMAX | 2 | 3 | 4 | TRANSFORMS |
| VMAX equals the max-norm diameter | True | True | True | PERSISTS |
| interior radii | 1 | 2 | 3 | TRANSFORMS |
| locality-admitting window widths | 1 | 2 | 3 | TRANSFORMS |
| static families | 1 | 1 | 1 | PERSISTS |
| the reduced dispersion separates families | True | True | True | PERSISTS |
| every eigenvalue is a root of unity | True | True | True | PERSISTS |
| the eigenphase lattice | 8 | 24 | 8 | TRANSFORMS |
| all group velocities are integers | True | False | True | BREAKS-AT-L=6 |
| the coin family and its sector split | 640=64+64+512 | 640=64+64+512 | 640=64+64+512 | PERSISTS |
| the parity strata are perfect matchings | True | True | True | PERSISTS |
| the (order, support) profile | S1-ONE=3/3;S2-EDGE=60/5;S2-CORNER=9/6;S2-APART=9/6;S3-ROW=2520/7;S4-BLOCK=20160/8 | S1-ONE=3/3;S2-EDGE=60/5;S2-CORNER=9/6;S2-APART=9/6;S3-ROW=2520/7;S4-BLOCK=20160/8 | S1-ONE=3/3;S2-EDGE=60/5;S2-CORNER=9/6;S2-APART=9/6;S3-ROW=2520/7;S4-BLOCK=20160/8 | PERSISTS |
| the holonomy is alternating on each of its orbits | True | True | True | PERSISTS |
| the global support | 16 | 36 | 64 | TRANSFORMS |
| the window widths at which this size is admitted | [1] | [2] | [2, 3] | TRANSFORMS |

In total,
the persistence table carries 24 rows: 11 persist, 5 break and 8 transform.

**A survival and a theorem are not the same fact, and the table says which is
which.**  Every row carries its modality in the receipt, and
7 of the 11 PERSISTS rows are theorems restated at three rungs and 4 are contingent survivals.
The seven forced ones are: the link set is Sidon at every L ≥ 3, one line from
its differences; monomial-only on the link set then follows from the DDS
theorem over any field with an involution; the three-term stencil realises ±a
twice at every order at least 3, so it is non-Sidon at every rung; VMAX equals
the diameter by the momentum parent's even-L theorem; the coin family carries
no L by its own definition; and the profile and the alternating character are
forced by non-wrapping, which is the gauge parent's argument.  The four
contingent survivals are the static-family count, the separation of families
by the reduced dispersion, the root-of-unity property of every eigenvalue, and
the perfect-matching property of the parity strata.

Two further remarks on reading it.  Every BREAKS row breaks at the same rung,
and they are **one mechanism with a residue**, not five independent failures.
Four of them are one failure seen from four sides — the local family collapses
to shifts at L = 6, which is the DDS criterion turning on.  The fifth, the
integer velocities, is not independent of the other four: a monomial generator
is a shift, and under the parent's own forced normalisation its velocity is
the negated offset, an integer at every rung.  So a non-integer velocity can
only ever live on the non-monomial residue — measured, no monomial family at
any rung carries one — and at L = 6 that residue is the whole of it:
the 6 non-integer-velocity families at L = 6 are the 6 non-monomial families,
all of them on order-2 axes, whose stencil is difference-doubled by the
involution alone.  That is the one place the criterion still permits
interference at that rung, and it is where the break stands.

And five of the eight TRANSFORMS rows carry
closed-form laws rather than lists: VMAX is L/2, the interior radii and the
admitted window widths are L/2 − 1, the global support is L², and the
eigenphase lattice is lcm(8, L).  A sixth, the widths at which a size is
admitted, is the band law of section 7 read the other way round — and every
*exclusion* in that row is forced: locality fails at L = 4 for widths at least
2 and at L = 6 for width 3, and the radius-one ball census is exhausted at
L = 6 and L = 8.  It is the strongest row in the table.  The two pool counts
are the rows with no one-line law: the pool carries 58 circulant families at
L = 4, 42 at L = 6 and 106 at L = 8, and the non-monotonicity is real — it is the sum of per-axis
gauge classes less the identity they share, and the per-axis class count
depends on the axis's order, which depends on L arithmetically rather than
monotonically.

## 9. What this decides, and what it does not

**Decided.**  The registered Sidon prediction is half right and the halves are
separated: the sufficiency implication holds at every declared arena and is
substantively tested at the Sidon ones, necessity fails at ten of them, and
the counterexample is the parents' own stencil at the first new rung, on all
four local axes at once.  The exact replacement is a theorem about difference
multiplicities that is field-free — exercised in nine characteristics, not
only argued — and it subsumes the parent's order-collapse theorem, the
parent's radius-one Moore-ball collapse and the control's coset mechanism as
three instances of one criterion, while accounting for the parent's order-3
gap by showing the criterion is silent there.
The even-L VMAX theorem holds at both new rungs
in-unit.  The momentum register's interior-radius claim is re-derived from a
pool built here, and identified — by a theorem about the two definitions, at
odd sizes as well as even — with the locality-admitting width set.  The gauge
fingerprint is inert along the ladder.  The parent's unique admissible size is
re-derived and shown to be the width-1 section of a band whose sections are
now decided on both sides, with evenness withdrawn as a law and the
alphabet-relativity stamped where it belongs.

**Not decided.**  Nothing about limits: three finite rungs are three finite
rungs, and no continuum, scaling or thermodynamic reading is licensed by
anything here.  Nothing about odd rungs *of the ladder*, which the pin did not
declare and which the even-L theorem does not cover — with two named
exceptions, both measured: the width/interior-radius identity holds at odd
sizes by theorem, and the band's width-2 section contains the odd size 7.
Nothing about window widths above 3, which are not swept.  Nothing about which
group the holonomy prefers: the fingerprint datum is entered, and the
selection question is another unit's.  No transport number is inherited from
the momentum parent, whose scope stamp forbids it.  And nothing here is a
claim about non-uniform gauge configurations, which the gauge parent did not
sweep and this unit does not either.

**The one reading that most wants a second look** is still the band, but not
where an earlier reading of this unit pointed.  The attack it invited — a size
outside the predicted band at width 2 carrying a local non-monomial unitary —
succeeded, at L = 7, and the repair was to decide the band rather than to
narrow the claim.  What is left exposed is the *alphabet*: every section above
is a section over the parents' 25, the order-3 coset at L = 9 shows the
sections move when the alphabet does, and no claim is made here about the
union over alphabets.

## 10. The instrument

The instrument is a single file with an argv whitelist: an unknown flag, an
unknown mutant name, a missing flag argument and a non-existent
`--verify-paper` path all exit 2.  `--selftest` corrupts one anchor in memory,
confirms the run dies at the anchor gate, writes nothing and exits 1.
`--mutant NAME` runs the pipeline with one named perturbation active and must
die at that perturbation's declared gate.  `--break-anchor NAME` exercises the
three anchor gates by their own names.  `--verify-paper` runs the same final
coverage pass the delivery run runs, so the flag a reviewer is invited to use
is not weaker than the path it stands in for.  The delivery run is the only
writer, and a failing run writes nothing at all — including on the post-write
path, where the previous artifacts are copied aside before the move and
restored if the on-disk check fires.

**Anchors.**  Ten hash-pinned sources, 38 path-value anchors read from the
parents' receipts at named paths, and 9 verbatim windows each bound to the
gate that consumes it and each pinned by the digest of its exact bytes and a
declared length floor.  Text gates normalise whitespace *and* markdown
prefixes on both sides (#125), so a quotation that is line-wrapped, indented,
bulleted or blockquoted in its source is still the same characters in the same
order.

**The seal.**  Every published object is digested at the moment its gate
passes (#119); the manifest is total (#148), so every published receipt key is
either sealed at its gate or named in the declared-unsealed list with the
reason it cannot be; every seal is taken at the gate that **closes its
value**, and the three whose values cannot exist before the final gate are
named as such in a published window report rather than left to be discovered;
the gate ledger is chained, each row's digest folding in
its predecessor; the artifacts are written from the sealed payload through
temporaries moved into place only after the bytes match; and the terminal
integrity check compares the bytes on disk against the gate-time seal, never a
re-derivation from disk.

**Coverage** follows E-22 exactly.  The numeral scan covers prose, tables,
fenced blocks and inline code spans alike, with the spans additionally scanned
in their own right so that a scanner blind to backticks would be caught.  The
licence set carries **no blanket range**: a numeral is structural only if it
is a heading number computed from the paper's own heading lines, a digit run
inside a commit-sha token the paper cites, or one of the named engravings and
paper references, each with the reason it appears.  Everything else must be
licensed by a value in the receipt.
Fenced blocks are gated by *multiset* equality against blocks rendered from
the receipt — this paper carries the verdict block twice, which is precisely
the configuration a containment gate cannot see.  Table rows render as claims,
and **all seven of this paper's tables render**: the persistence table, the
arena table, the control table, the dispersion table, the profile table, the
locality table and the band table, 69 rows in all.  Every claim carries
polarity: perturbing the receipt key it renders from moves the claim, and the
moved claim is no longer found in the paper.

**Falsifiers** follow E-23, and a published description is bound to its branch
three ways: the switch exists in this file; the digest of the guarded source
equals a digest pinned in the frozen registry, so code cannot drift away from
its description; and the description's leading verb must lie in the verb set
of its declared effect class, so a description cannot be inverted while its
code stands still.  Every
gate is either FALSIFIABLE with a named mutant, WAIVED with a named forcing —
each saying why no in-process mutant can reach it — or STRUCTURAL **through an
explicit registry that names the two independently computed objects its
predicate compares**.  There is no default branch: a gate fitting none of the
three is UNCLASSIFIED and dies.  The ledger is built over every gate the run
will reach rather than only the ones already closed, and a separate gate
requires the closed ledger to have an entry for every gate row — because a
gate that runs after the ledger is written is not thereby unguarded.

**Measure** follows E-24, and the fraction census **scans rather than
self-selects**: every fraction-shaped construction in the rendered paper and
in the emitted verdict string is found by pattern, each hit must be covered by
a stamped row built from a receipt value, and a declared row that no hit
reaches fails as a dead declaration.  No count is presented as a probability.

**The head is derived.**  No verdict segment carries a typed measurement: the
sections, the sets, the counts, the rung list and the control rung are all
rendered from receipt tables.  The head and every segment are bound twice —
re-derived from the receipt's primitive tables by a comparator that shares no
literal and no format string with the builder, and then the emitted string is
*parsed back* into structured values and compared against them by equality.

**#91 at its own hands.**  The instrument derives the repository root from its
own path, reads nothing outside its declared list, and never invokes a
subprocess — in particular never `git`.  A copy that is missing a declared
source aborts loudly and cleanly, naming what is absent, before a single gate
runs and without writing anything.  The delivery run byte-reproduces off-tree
and in a directory with no version control at all.

## 11. Deviations, and the register of scope

- The declared subset window: the naive difference-doubled subset census, over
  all subsets of an offset set, is exhaustive at size at most 12, which covers
  every arena declared here and every radius-one ball — which is everything it
  is asked for.  The ball census at wider windows runs by a bounded route up
  to the computed support ceiling, which is exhaustive for unitarity, and the
  two routes are bound against each other set for set.  No absence claim rests
  on the window.  Inventoried as a DECLARED-WINDOW.
- The char-p scan window: every (field, arena) pair small enough is scanned
  exhaustively and the rest are listed rather than run.  The theorem is
  proved; the exercise is what stops the proof from being read in one
  characteristic only.  Inventoried as a DECLARED-WINDOW.
- The window widths are genuinely free and three are run: the parent's own,
  and the two above it that still admit locality on this ladder.  Nothing
  above width 3 is measured and the SCALE clause is scoped to the widths run.
- The band sweep range is genuinely free: sizes 2 to 14, chosen to contain
  every size either mechanism's closed form can reach at the declared widths
  with margin.  Above the sweep the injectivity theorem forces absence at
  every width, so the range is a presentation choice and not a scope limit.
- The probe alphabets at the control rung are genuinely free and three are
  run; the registered count is alphabet-relative and the relativity is
  measured rather than hidden.  So is the SCALE clause's.
- The rungs are the pin's, the control rung is paper-20's, the fourth
  direction is paper-20's, the plaquette stencils are the gauge parent's, and
  the locality criterion is R2's — all carried verbatim so that the
  comparisons are like for like.
- The gauge parent's own restriction travels: only uniform coin
  configurations are swept, at every rung, and the non-uniform space is not
  entered.
- The momentum parent's velocity reading travels: the forward stencil with the
  tie averaged.  The residual fiber it measured inert is not re-measured here;
  section 4 says why the break survives that.
- No odd rung of the *ladder* is measured; the even-L theorem does not cover
  them and the pin did not declare them.  The two odd-size results this unit
  does carry — the width/radius identity and the L = 7 band cell — are named
  in section 9 rather than folded into the ladder.

### 11.5 The successor register

**The registered prediction is recorded as three parts, not as a fraction.**
A half-right prediction has parts, and a fraction destroys the information the
parts carry.

1. **Mechanism — CONFIRMED AND STRENGTHENED.**  "The monomial theorem is a
   Sidon property of the offset set", sufficiency direction: the implication
   holds at every declared arena, is substantively tested at the Sidon ones,
   and is now a theorem with a *weaker* hypothesis, since DDS-free is strictly
   weaker than Sidon.  Tested at rungs the predictor never ran.
2. **Transport to the R = 4 arena — CLOSED BY THEOREM, NOT BY MEASUREMENT.**
   The anchored link set is Sidon at every L ≥ 3, hence difference-doubled-
   free, hence monomial-only over any field with an involution — including
   paper-20's own coefficient ring.  The register's named target needs no scan
   and no R-ladder run.  This unit did not enter the R-ladder; the leg is
   closed anyway, and paper 29 inherits it as a corollary rather than as a
   census.
3. **Control — REFUTED AS STATED.**  The 54 is reproduced exactly with the
   same witness support, and it is alphabet-relative; the death does not
   transport up the ladder, and there by theorem.  The universal quantifier
   ("any declared fourth direction") entered at the *compression* from the
   seat finding to the register, not at the measurement — the seat finding
   named the specific fourth direction, the specific probe alphabet and the
   mechanism.  That is a governance datum rather than a physics one, and the
   record of what was registered is not edited to hide it.

**The theorem is a result, not a bet.**  `DDS-free ⟹ monomial-only` has a
proof; no measurement can falsify it, and putting it in a prediction ledger
would corrupt the ledger's score.  It is registered in the result column.

**The new prediction is the converse.**  `DDS-carrying ⟹ interference
present`, registered NECESSARY-NOT-SUFFICIENT.  It holds at every
DDS-carrying arena on this unit's declared list, and it is **already falsified
once, alphabet-relatively**: the order-3 coset in the radius-3 ball at L = 9 is
difference-doubled and
carries 0 non-monomial unitaries over the parents' 25 and 54 over the 19-value probe.
Stated forward, what would refute it structurally is a difference-doubled
offset set whose non-monomial unitaries are empty over *every* alphabet closed
under the declared field's involution.  A difference-doubled set is a
permission; what converts a permission into a realisation is the alphabet.

**What paper 29 inherits, in order of value.**  (i) The transport leg above,
closed by theorem, so no scan is spent on it and the question becomes what its
*own* offset set is.  (ii) The alphabet-relativity discipline: every count of
non-monomial unitaries in this corpus is a joint property of the offset set
and the alphabet.  (iii) The coset mechanism as the live danger, since
paper-20's arena is over F_3 and cosets of order-3 subgroups are cheap there.
(iv) **Not** inherited: the L-ladder's window band, VMAX = L/2, the eigenphase
law and the interior-radius count — all four are statements about (Z_L)² with
this alphabet, and none has been asked of the R-ladder.

**The odd-rung gap** is correctly declared open for the ladder, and the odd-L
blade, when it runs, has its first two data already: the width/radius identity
at odd sizes, and the L = 7 cell of the width-2 band section.

## 12. The verdict

```
PERL-SIDON-SUFFICIENT-NOT-NECESSARY
PERL-SIDON-SUFFICIENT-NOT-NECESSARY<SIDON=SUFFICIENCY-HOLDS-AT-3-OF-3-SIDON-ARENAS(VACUOUS-AT-THE-OTHER-15;THE-IMPLICATION-HOLDS-AT-ALL-18);LINK-STENCIL-SIDON-AND-MONOMIAL-ONLY-AT-L-6-AND-8(0-AND-0-NON-MONOMIAL-OF-24-AND-24-UNITARY);NECESSITY-FAILS-AT-10-ARENAS(FIRST-IN-THE-DECLARED-ORDER=L-6-AXIS-0-1;ALL-4-LOCAL-AXES-AT-L-6-FAIL-TOGETHER)|CONTROL=THE-FOURTH-DIRECTION-DEATH-DOES-NOT-TRANSPORT(REGISTERED-54-REPRODUCED-AT-THE-CONTROL-RUNG-L-3;48-AT-L-4;0-AND-0-AT-L-6-AND-L-8-BY-THEOREM-OVER-ANY-FIELD-WITH-AN-INVOLUTION;ALPHABET-RELATIVE-0-NON-MONOMIAL-OVER-THE-25-ELEMENT-ALPHABET-OF-THE-PARENTS)|LAW=DDS-FREE-FORCES-MONOMIAL-OVER-ANY-FIELD-WITH-AN-INVOLUTION(NO-DIFFERENCE-DOUBLED-SUBSET;13-OF-18-ARENAS-DDS-FREE-AND-ALL-MONOMIAL-ONLY;SIDON-STRICTLY-STRONGER-AT-10-ARENAS;EXERCISED-IN-9-FINITE-FIELDS-AT-104-EXHAUSTIVE-SCANS)|VMAX=DIAMETER-AT-EVERY-RUNG(2;3;4=L/2)|INTERIOR-RADII=1;2;3(THE-3-AT-L-8-REGISTER-CLAIM-RE-DERIVED-FROM-A-POOL-BUILT-HERE;EQUAL-TO-THE-LOCALITY-ADMITTING-WIDTH-SET-BY-THEOREM(BOTH-ARE-{1..diam-1}))|FINGERPRINT=(ORDER,SUPPORT)-PROFILE-IDENTICAL-AT-ALL-3-RUNGS-ON-ALL-64-ANTIDIAGONAL-COINS(S1-ONE=A3;S2-EDGE=A5;S2-CORNER=A3 x A3;S2-APART=A3 x A3;S3-ROW=A7;S4-BLOCK=A8);GLOBAL-SUPPORT-IS-THE-VOLUME-16;36;64;NO-GROUP-SELECTION-LAW-CLAIMED|SCALE=THE-PARENTS-UNIQUE-SIZE-IS-WINDOW-RELATIVE(ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-L-WITH-L>=2r+2-WHOSE-RADIUS-r-BALL-CARRIES-A-DIFFERENCE-DOUBLED-SUBSET-REALISED-OVER-THE-ALPHABET;WIDTH-1={4};WIDTH-2={6,7,8};WIDTH-3={8,10,12};TWO-MECHANISMS(INVOLUTION-PAIR-EVEN-L<=4r;PERFECT-DIFFERENCE-SET-AT-L-7-r-2);EVENNESS-IS-NOT-A-LAW;BOTH-HALVES-FORCED(LOCALITY-BELOW-2r+2;INJECTIVITY-ABOVE-4r;EXHAUSTED-CENSUS-TO-SUPPORT-CEILING-4-BETWEEN);ALPHABET-RELATIVE(THE-ORDER-3-COSET-AT-L-9-r-3-CARRIES-0-OVER-THE-PARENTS-25-AND-54-OVER-THE-19-VALUE-PROBE))|BREAKS=LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-6;INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS;THE-6-NON-INTEGER-FAMILIES-ARE-THE-6-DDS-PERMITTED-NON-MONOMIAL-FAMILIES);EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(8,L)(8;24;8)|TABLE=24-ROWS(11-PERSIST(7-FORCED;4-CONTINGENT);5-BREAK;8-TRANSFORM)|SCOPE=D=2;RUNGS=L-IN-{4,6,8}+CONTROL-RUNG-L-3;FIELD=Q(ZETA-24);ALPHABET=25;WIDTHS={1,2,3};BAND-SWEEP=L-IN-2..14;STENCIL=3-TERM-AXIS-AND-THE-ANCHORED-LINK-SET;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));SECTOR=SINGLE-OCCUPATION;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-TRANSPORT-NUMBER-INHERITED;PERSISTENCE-AT-DECLARED-FINITE-RUNGS-ONLY>
```
