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
PERL-SIDON-SUFFICIENT-NOT-NECESSARY<SIDON=SUFFICIENCY-HOLDS-AT-18-OF-18-ARENAS;LINK-STENCIL-SIDON-AND-MONOMIAL-ONLY-AT-L-6-AND-8(0-AND-0-NON-MONOMIAL-OF-24-AND-24-UNITARY);NECESSITY-FAILS-AT-10-ARENAS(FIRST=L-6-AXIS-0-1)|CONTROL=THE-FOURTH-DIRECTION-DEATH-DOES-NOT-TRANSPORT(REGISTERED-54-REPRODUCED-AT-THE-CONTROL-RUNG;48-AT-L-4;0-AT-L-6-AND-L-8;ALPHABET-RELATIVE-0-OF-25-OVER-THE-PARENTS-OWN-ALPHABET)|LAW=DDS-FREE-FORCES-MONOMIAL-OVER-ANY-FIELD(NO-DIFFERENCE-DOUBLED-SUBSET;13-OF-18-ARENAS-DDS-FREE-AND-ALL-MONOMIAL-ONLY;SIDON-STRICTLY-STRONGER-AT-10-ARENAS)|VMAX=DIAMETER-AT-EVERY-RUNG(2;3;4=L/2)|INTERIOR-RADII=1;2;3(THE-3-AT-L-8-REGISTER-CLAIM-CONFIRMED;EQUAL-TO-THE-LOCALITY-ADMITTING-WIDTH-COUNT-AT-EVERY-RUNG)|FINGERPRINT=(ORDER,SUPPORT)-PROFILE-IDENTICAL-AT-ALL-THREE-RUNGS-ON-ALL-64-ANTIDIAGONAL-COINS(S1-ONE=A3;S2-EDGE=A5;S2-CORNER=A3 x A3;S2-APART=A3 x A3;S3-ROW=A7;S4-BLOCK=A8);GLOBAL-SUPPORT-IS-THE-VOLUME-16;36;64;NO-GROUP-SELECTION-LAW-CLAIMED|SCALE=THE-PARENTS-UNIQUE-SIZE-IS-WINDOW-RELATIVE(ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-EVEN-L-IN-[2r+2,4r];WIDTH-1={4};WIDTH-2={6,8};WIDTH-3={8,10,12};PRESENCE-CONSTRUCTIVE-ABSENCE-FORCED-ONLY-AT-WIDTH-1)|BREAKS=LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-6;INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS);EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(8,L)|TABLE=24-ROWS(11-PERSIST;5-BREAK;8-TRANSFORM)|SCOPE=D=2;RUNGS=L-IN-{4,6,8};FIELD=Q(ZETA-24);ALPHABET=25;STENCIL=3-TERM-AXIS-AND-THE-ANCHORED-LINK-SET;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));SECTOR=SINGLE-OCCUPATION;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-TRANSPORT-NUMBER-INHERITED;PERSISTENCE-AT-DECLARED-FINITE-RUNGS-ONLY>
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
the converse fails at 10 of them.  The prediction's control fares worse still: the declared fourth
direction that kills interference at the control rung, and again at the parent
rung, kills nothing at all at L = 6 or L = 8.

What replaces the prediction is sharper than it was, and it is a theorem
rather than a correlation.  Call an offset set **difference-doubled** when
every nonzero difference realised inside it is realised at least twice.  Then
the support of *any* unitary map is difference-doubled — one line from the
unitarity condition — so if no subset of the declared offset set of size at
least two is difference-doubled, every unitary map on it is monomial, over any
field closed under conjugation.  Sidon is the special case in which *every*
internal difference is simple.  The two conditions coincide at the parent rung
and part company at the next one, which is exactly where the prediction breaks.

The rest of the ladder is a table.  The even-L theorem holds: the maximal
group speed equals the max-norm diameter at all three rungs.  The register's
own successor parameter is confirmed: the interior-radius count is 1, 2 and 3,
and — this is new — it is also the number of window widths at which the
inherited locality criterion still returns locality, so the parent's
resolution parameter and R2's window-width law are the same number.  The gauge
fingerprint is inert along L: the (order, support) profile is identical at all
three rungs, on every coin of the antidiagonal sector.  Five invariants break,
all of them at L = 6, and one of them is the parent's own headline family.

And one row is a reversal rather than a break.  R4's admissible set was a
single lattice size, and this unit re-derives that set at R4's own window
width — and then finds that it is the width-1 section of a band.  At window
width 1 the admitted set is [4]; at window width 2 it is [6, 8], and at width
3 it is [8, 10, 12].  The uniqueness was real and it was resolution-relative,
and the two sizes the pin sent this unit to visit are exactly the two the next
window admits.

---

## 1. The question, and what would have answered it the other way

The pin asks whether the forced results of the L = 4 arc persist at L = 6 and
L = 8, with a per-invariant verdict and an exact witness for each.  Stage 1 is
decisive and is reported in the head regardless of everything else: the
registered Sidon prediction either passes per arena or it does not.

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
> field closed under conjugation.

*Proof.*  Suppose some m ≠ 0 is realised inside supp(c) by exactly one ordered
pair (v, w), so v − w = m.  Then A(m) has exactly one term and reads
c_v · conj(c_w) = 0; but v and w lie in the support, so neither factor
vanishes.  Contradiction.  Hence every internal difference is realised at
least twice.  The consequence is immediate: a support of size at least two
would be a difference-doubled subset of S. ∎

A Sidon set — one in which every nonzero difference is realised exactly once —
has no difference-doubled subset at all, so Sidon implies the hypothesis.  The
implication is strict, and the witness is the parents' own stencil: {0, a, −a}
with a of order at least 5 realises ±a twice and ±2a once, so it is not Sidon,
yet the simple differences ±2a already forbid a support containing both a and
−a, and the remaining lag then forbids the rest.  The criterion is
combinatorial, it names no field, and it is exhaustive over subsets at every
arena this unit declares.

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
rung of §3.4.*

Read off the table:
the link stencil is Sidon at every rung, and its scan returns 24 unitary maps
of which 0 are non-monomial at L = 6; at L = 8 the same stencil returns 24
unitary maps and 0 non-monomial.  So the prediction's own direction — Sidon
offsets force the collapse — **passes at both new arenas**, and it passes for
the reason the prediction gave.

Against that,
the local axis stencil carries 48 non-monomial unitaries at the parent rung,
and 0 at L = 6 and 0 at L = 8, with the same non-Sidon difference
multiplicities [2, 2, 1, 1].  The Sidon status of that stencil does not move
along the ladder — it is false at every rung — while the conclusion it was
supposed to control moves at L = 6.  That is the converse failing, and it is
the first place in this programme where a registered prediction has been
measured wrong at a rung its author never ran.

Every DDS-free arena is monomial-only, with no exception anywhere on the
table.  The count `13 of 18` is stamped COUNTING-ONLY in the receipt: it is a
coverage report over this unit's own declared arena list, which is not a
sample of any population.

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
non-monomial local generators was {2, 4} with an unexplained gap at 3, and the
gap is now explained: at order 3 the stencil is a full coset of a cyclic
subgroup, so it *is* difference-doubled and the criterion forbids nothing —
the emptiness there is alphabet-relative, exactly as the parent declared it,
and not structural.

### 3.4 The control: the fourth-direction death does not transport

The registered control says that declaring a fourth direction kills the
theorem and that 54 non-monomial unitaries appear.  That number is reproduced
here independently, from the definitions, at the control rung and over the
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

*Scope: exhaustive over each probe alphabet at the control rung.*

Two things follow, and both are disclosures the register did not carry.

**The count is alphabet-relative.**  Over the parents' own 25-element
alphabet the same offset set at the same rung carries no non-monomial unitary
whatever.  The death is a joint property of the offset set and the alphabet:
the offset set makes it *possible* by carrying a difference-doubled subset,
and the alphabet decides whether anything realises it.  The verdict carries
the disclosure rather than the bare 54.

**The death does not transport up the ladder.**  Measured along the rungs,
the same fourth direction carries 48 non-monomial unitaries at L = 4 and 0 at
L = 6 and 0 at L = 8.  At
the control rung the mechanism is a coset of a cyclic subgroup of order 3; at
the parent rung it is a different mechanism entirely — two of the four offsets
differ by an involution, which doubles that difference all by itself.  At
L = 6 and L = 8 neither mechanism is available to those four offsets, the set
is DDS-free, and the collapse is forced.  "Dies at any declared fourth
direction" is therefore false as stated: it dies at a fourth direction that
introduces a difference-doubled subset, and whether a given fourth direction
does that is a property of the rung.

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

**The register's parameter is confirmed and then joined to something else.**
Measured at each rung,
the interior-radius count is 1, 2 and 3 — the momentum parent's own successor
claim of three at L = 8, anchored at its receipt and now measured.  §6 shows
that the same three numbers count something the parent was not measuring.

**One invariant breaks here, and its witness is exact.**  The parent measured
that every group velocity on its stage is an integer, over all of its velocity
cells, and derived the reason from a parity grading of the coefficient field.
Re-measured along the ladder: 6 families at L = 6 carry a velocity that is
not an integer.  The witness is an order-2 axis carrying a two-term generator,
whose phase advances by a quarter turn per momentum step and
whose speed is 3/2.  The property survives at L = 8, but not for the parent's
reason — there it survives because the eigenphase lattice and the lattice size
coincide, so the velocity is a lift and nothing else.

**The eigenphase lattice itself transforms, and the law is clean.**  Measured
over the whole declared gauge orbit, the eigenvalues at rung L generate the
group of lcm(8, L)-th roots of unity: 8, 24 and 8.  The parent's Z/8 was not a
fact about the stage; it was the coincidence lcm(8, 4) = 8.  Every eigenvalue
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

The alternating-on-orbits character therefore persists, and it persists for a
reason the unit measures rather than assumes: no declared local stencil wraps
at any rung, so the generators at the three rungs are the same maps on the
same relative coordinates.  Local stability could not have come out otherwise
at any size at least as wide as the widest declared patch, and the unit says
so instead of reporting a coincidence.

At the global stencil the support is the volume and the class follows from the
generator type: every plaquette holonomy is a three-cycle and the family is
transitive on the whole site set, so the classical theorem gives the full
alternating group on a support that is exactly L².  Measured,
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
interior-radius count, rung for rung.  The two quantities were introduced by
different parents for different reasons — one is a resolution parameter of the
torus, the other is a locality census over a sliding neighbourhood — and they
are the same number because both count the radii strictly between the point
and the diameter.  The joint is gated.

R2's partition corollary transports too, and is run as the control: every
blockwise atlas of this stage — the torus cut into b × b blocks for every
divisor b — is clique-only at every rung, so no partition of this stage can
produce a non-complete component.  Locality here is carried by the sliding
window and by nothing else, which is the shape R2 measured on its own arena.

## 7. The band: the parent's unique size is the width-1 section

R4's precheck met two requirements at one point.  Locality required L at least
4; a non-monomial local generator required L at most 4; the admissible set was
a single size.  Both halves are re-derived here at R4's own width, and both
halves move when the width does.

*Locality* at width r fails exactly when the radius-r ball covers the torus,
which happens at 2r + 1 ≥ L; so locality requires L ≥ 2r + 2, and at r = 1
that is the parent's own threshold.  *Interference* at width r requires a
difference-doubled subset inside the ball, and the cheapest one is a pair of
offsets differing by an involution — which exists exactly when the ball is
wide enough to reach halfway across the torus, that is when L ≤ 4r and L is
even.  A pair like that carries an explicit unitary: put 1/√2 on one offset
and i/√2 on the other, both in the parents' declared alphabet, and the single
surviving lag reads twice the real part of their product, which vanishes.
Every witness in the table below is checked against the parent's whole-torus
criterion.

| r | admitted sizes | predicted: even L in [2r+2, 4r] |
|---|---|---|
| 1 | [4] | [4] |
| 2 | [6, 8] | [6, 8] |
| 3 | [8, 10, 12] | [8, 10, 12] |

*Scope: every width in {1, 2, 3} against every size from 2 to 14; presence is
constructive and verified at every admitted size.*

Reading the table:
at window width 1 the admitted set is [4], reproducing the parent's anchored
admissible-scale set from a completely different argument, and
at window width 2 it is [6, 8], and at width 3 it is [8, 10, 12].

**The honest half.**  The presence direction is constructive: an explicit
non-monomial unitary is exhibited and verified at every admitted size.  The
absence direction — that no non-monomial unitary exists at the sizes *not*
listed — is forced only at width 1, where the difference-doubled subset census
over the nine-offset ball is exhaustive over all of its subsets.  At wider
windows the ball is too large for that census and the complement is declared
open, not claimed.  The band is therefore a **presence** band above width 1,
and the verdict says so.

The reading is nevertheless sharp.  The parent's headline — one lattice size
admits a local family carrying interference — is true, is re-derived, and is a
statement about the parent's *window*, not about the lattice.  Widen the
window by one and the same coincidence recurs at exactly the two rungs this
unit was sent to visit.

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
| the local AXIS stencil is DDS-free | False | True | True | BREAKS-AT-L=6 |
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

Two remarks on reading it.  Every BREAKS row breaks at the same rung, and they
are not five independent failures: four of them are one failure seen from four
sides — the local family collapses to shifts at L = 6, which is the DDS
criterion turning on — and the fifth, the integer velocities, is unrelated and
lives in the momentum layer.  And five of the eight TRANSFORMS rows carry
closed-form laws rather than lists: VMAX is L/2, the interior radii and the
admitted window widths are L/2 − 1, the global support is L², and the
eigenphase lattice is lcm(8, L).  A sixth, the widths at which a size is
admitted, is the band law of §7 read the other way round.  The two pool counts
are the rows with no one-line law: the pool carries 58 circulant families at
L = 4, 42 at L = 6 and 106 at L = 8, and the non-monotonicity is real — it is the sum of per-axis
gauge classes less the identity they share, and the per-axis class count
depends on the axis's order, which depends on L arithmetically rather than
monotonically.

## 9. What this decides, and what it does not

**Decided.**  The registered Sidon prediction is half right and the halves are
separated: sufficiency holds at every declared arena, necessity fails at ten
of them, and the first counterexample is the parents' own stencil at the first
new rung.  The exact replacement is a theorem about difference multiplicities
that is field-free and subsumes the parent's order-collapse theorem, its
alphabet-relative gap at order 3, and the control's coset mechanism as three
instances of one criterion.  The even-L VMAX theorem holds at both new rungs
in-unit.  The momentum register's interior-radius claim is confirmed, and is
identified with the locality-admitting width count.  The gauge fingerprint is
inert along the ladder.  The parent's unique admissible size is re-derived and
shown to be the width-1 section of a band whose next section is exactly the
two rungs measured here.

**Not decided.**  Nothing about limits: three finite rungs are three finite
rungs, and no continuum, scaling or thermodynamic reading is licensed by
anything here.  Nothing about odd rungs, which the pin did not declare and
which the even-L theorem does not cover.  Nothing about the absence half of
the band above width 1 — declared open above.  Nothing about which group the
holonomy prefers: the fingerprint datum is entered, and the selection question
is another unit's.  No transport number is inherited from the momentum parent,
whose scope stamp forbids it.  And nothing here is a claim about non-uniform
gauge configurations, which the gauge parent did not sweep and this unit does
not either.

**The one reading that most wants a second look** is the band.  It reverses a
parent's headline in the direction of *less* specialness for L = 4, and it
does so with a one-sided argument above the parent's own width.  A reviewer
who wants to break this unit should attack there first: exhibit a size outside
the predicted band at width 2 carrying a local non-monomial unitary, or show
that the absence half fails somewhere the paper claims nothing.

## 10. The instrument

The instrument is a single file with an argv whitelist: an unknown flag, an
unknown mutant name, a missing flag argument and a non-existent
`--verify-paper` path all exit 2.  `--selftest` corrupts one anchor in memory,
confirms the run dies at the anchor gate, writes nothing and exits 1.
`--mutant NAME` runs the pipeline with one named perturbation active and must
die at that perturbation's declared gate.  `--break-anchor NAME` exercises the
three anchor gates by their own names.  The delivery run is the only writer,
and a failing run writes nothing at all.

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
reason it cannot be; the gate ledger is chained, each row's digest folding in
its predecessor; the artifacts are written from the sealed payload through
temporaries moved into place only after the bytes match; and the terminal
integrity check compares the bytes on disk against the gate-time seal, never a
re-derivation from disk.

**Coverage** follows E-22 exactly.  The numeral scan covers prose, tables,
fenced blocks and inline code spans alike, with the spans additionally scanned
in their own right so that a scanner blind to backticks would be caught.
Fenced blocks are gated by *multiset* equality against blocks rendered from
the receipt — this paper carries the verdict block twice, which is precisely
the configuration a containment gate cannot see.  Table rows render as claims:
every row of the persistence table and of the arena table is generated from
the receipt and required to be present as written.  Every claim carries
polarity: perturbing the receipt key it renders from moves the claim, and the
moved claim is no longer found in the paper.

**Falsifiers** follow E-23: every published mutant description names a switch
that exists in this file, and the check is a gate rather than a promise.  Every
gate is either FALSIFIABLE with a named mutant, WAIVED with a named forcing —
seven are, and each says why no in-process mutant can reach it — or
STRUCTURAL, meaning it compares two independently computed objects, or
evaluates a per-object predicate over a table it did not build, and cannot
pass unless they agree.  The ledger is built over every gate the run will
reach rather than only the ones already closed, and a separate gate requires
the closed ledger to have an entry for every gate row — because a gate that
runs after the ledger is written is not thereby unguarded.

**Measure** follows E-24: the two fractions this unit publishes are stamped
COUNTING-ONLY in the receipt, with the reason.  No count is presented as a
probability.

**#91 at its own hands.**  The instrument derives the repository root from its
own path, reads nothing outside its declared list, and never invokes a
subprocess — in particular never `git`.  A copy that is missing a declared
source aborts loudly and cleanly, naming what is absent, before a single gate
runs and without writing anything.  The delivery run byte-reproduces off-tree
and in a directory with no version control at all.

## 11. Deviations, and the register of scope

- The declared subset window: the difference-doubled subset census is
  exhaustive at offset sets of size at most 12, which covers every arena
  declared here and the radius-one ball.  Above that size only the pair
  criterion is used, and the absence direction is not claimed.  Inventoried as
  a DECLARED-WINDOW.
- The probe alphabets at the control rung are genuinely free and three are
  run; the registered count is alphabet-relative and the relativity is
  measured rather than hidden.
- The rungs are the pin's, the fourth direction is paper-20's, the plaquette
  stencils are the gauge parent's, and the locality criterion is R2's — all
  carried verbatim so that the comparisons are like for like.
- The gauge parent's own restriction travels: only uniform coin
  configurations are swept, at every rung, and the non-uniform space is not
  entered.
- The momentum parent's velocity reading travels: the forward stencil with the
  tie averaged.  The residual fiber it measured inert is not re-measured here.
- No odd rung is measured; the even-L theorem does not cover them and the pin
  did not declare them.

## 12. The verdict

```
PERL-SIDON-SUFFICIENT-NOT-NECESSARY
PERL-SIDON-SUFFICIENT-NOT-NECESSARY<SIDON=SUFFICIENCY-HOLDS-AT-18-OF-18-ARENAS;LINK-STENCIL-SIDON-AND-MONOMIAL-ONLY-AT-L-6-AND-8(0-AND-0-NON-MONOMIAL-OF-24-AND-24-UNITARY);NECESSITY-FAILS-AT-10-ARENAS(FIRST=L-6-AXIS-0-1)|CONTROL=THE-FOURTH-DIRECTION-DEATH-DOES-NOT-TRANSPORT(REGISTERED-54-REPRODUCED-AT-THE-CONTROL-RUNG;48-AT-L-4;0-AT-L-6-AND-L-8;ALPHABET-RELATIVE-0-OF-25-OVER-THE-PARENTS-OWN-ALPHABET)|LAW=DDS-FREE-FORCES-MONOMIAL-OVER-ANY-FIELD(NO-DIFFERENCE-DOUBLED-SUBSET;13-OF-18-ARENAS-DDS-FREE-AND-ALL-MONOMIAL-ONLY;SIDON-STRICTLY-STRONGER-AT-10-ARENAS)|VMAX=DIAMETER-AT-EVERY-RUNG(2;3;4=L/2)|INTERIOR-RADII=1;2;3(THE-3-AT-L-8-REGISTER-CLAIM-CONFIRMED;EQUAL-TO-THE-LOCALITY-ADMITTING-WIDTH-COUNT-AT-EVERY-RUNG)|FINGERPRINT=(ORDER,SUPPORT)-PROFILE-IDENTICAL-AT-ALL-THREE-RUNGS-ON-ALL-64-ANTIDIAGONAL-COINS(S1-ONE=A3;S2-EDGE=A5;S2-CORNER=A3 x A3;S2-APART=A3 x A3;S3-ROW=A7;S4-BLOCK=A8);GLOBAL-SUPPORT-IS-THE-VOLUME-16;36;64;NO-GROUP-SELECTION-LAW-CLAIMED|SCALE=THE-PARENTS-UNIQUE-SIZE-IS-WINDOW-RELATIVE(ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-EVEN-L-IN-[2r+2,4r];WIDTH-1={4};WIDTH-2={6,8};WIDTH-3={8,10,12};PRESENCE-CONSTRUCTIVE-ABSENCE-FORCED-ONLY-AT-WIDTH-1)|BREAKS=LOCAL-NON-MONOMIAL-FAMILY-EMPTY-FROM-L-6;INTEGER-VELOCITIES-FAIL-AT-L-6(SPEED-3/2-ON-AN-ORDER-2-AXIS);EIGENPHASE-LATTICE-TRANSFORMS-Z/lcm(8,L)|TABLE=24-ROWS(11-PERSIST;5-BREAK;8-TRANSFORM)|SCOPE=D=2;RUNGS=L-IN-{4,6,8};FIELD=Q(ZETA-24);ALPHABET=25;STENCIL=3-TERM-AXIS-AND-THE-ANCHORED-LINK-SET;CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1));SECTOR=SINGLE-OCCUPATION;INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES;FINITE-LATTICE-ONLY;NO-CONTINUUM-CLAIM;NO-TRANSPORT-NUMBER-INHERITED;PERSISTENCE-AT-DECLARED-FINITE-RUNGS-ONLY>
```
