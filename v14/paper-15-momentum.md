# R4b — momentum: reading the dispersions

*v14, the limit programme, paper 15. Instrument:
`v14/code/r4b_momentum_exact.py`; artifacts `r4b_momentum_output.txt` and
`r4b_momentum_receipt.json`. Exact arithmetic throughout: the field is
Q(ζ₈) carried as four-tuples of rationals, eigenphases are exact elements of
Z/8, velocities are exact rationals, and there is no float anywhere.*

---

## Fifty-Seven Dispersions, and the Scale That Cannot Resolve Them

**The parent unit measured a family and never read its momentum.** Its
verdict-bearing stratum is 58 circulant families on a small periodic lattice;
every one of them is diagonal in the lattice characters, so every one of them
has an exact dispersion relation, and the parent's panel noticed — in a review
row, not in the delivery — that all but one of those dispersions is
non-constant. This unit reads them.

The reading is exact and complete. Every eigenvalue is an eighth root of
unity, so every eigenphase is an exact element of Z/8 and no branch, no
approximation and no field extension is needed anywhere. **57 of 58 families
MOVE**; the one that does not is C004, and it is the identity — the census's
own no-motion control, returning the head's other value. The speed spectrum is {0, 1, 2},
the maximal group speed is VMAX = 2, and 18 of the 19 circulant classes move.

The propagation bound the parent left open comes back empty, and the emptiness
is deeper than the admitted scale. VMAX equals the max-norm diameter of the
lattice, so the cone after a single step of the fastest family already covers
16 of 16 sites — and that is a **theorem about even periodic lattices**, not a
resolution failure of L = 4: the group speed is a phase advance per momentum
step and is therefore bounded by L/2, which is exactly the diameter, while the
monomial shift by the antipodal offset is a family member at every even L and
attains it. No enlargement of the lattice makes this constraint bite. What the
admitted size does control is the count of interior max-norm radii — one here,
3 at L = 8 — and that is the genuine resolution parameter. The group speed is
not a reach bound family by family either: measured against each family's own
one-step reach, 8 families overshoot it, 14 fall below it, 36 meet it exactly,
so an upper bound is falsified by the overshooters and a lower bound by the
undershooters. A velocity that both overshoots and undershoots the support it
came from is not a light-cone velocity.

Two results were not asked for. First, **the velocity convention is not free at
this alphabet**, and its two coordinates are not free in the same way. The
difference **stencil** is *forced*: the definition's own normalisation — a
monomial shift by an offset o has velocity o — holds at 384 of 384 non-antipodal monomial coordinates
under the forward and the backward difference and fails under the central one,
so the stencil is forced to 2 by the definition rather than declared against
it. The antipodal-tie **lift** is then *selected*: the Born drift of a family
equals the winding of its eigenphase for 58 of 58 families under exactly one of
the 9 tie-reading pairs, against a best other of 39 of 58. What both mechanisms
leave behind is a declared remainder: the residual fiber is 2 — forward and
backward — measured inert on every quantity reported here and differing only in
the sign of the velocity at 768 of 1856 cells. And the selecting identity is an
**arena instrument, not a law**: rebuilt exactly over the wider field the
parent's panel exhibits at this same lattice size, it returns two different
numbers — the Born drift is -1/2 and the winding is -1 — and the identity
fails.

Second, **the tension the panel called "charge without momentum" is a
cancellation in the arithmetic of the average, not an absence of motion.** The
42 non-monomial families have exactly zero net transport in both spaces at the
selected reading, and all 42 of them MOVE: non-constant dispersion, nonzero group
velocity at individual momenta, summing to nothing over the dual torus. How
much of that zero survives the tie is measured rather than assumed: it is
reading-independent for 24 of the 42 in position space and for 30 of the 42 on the dual torus. The
12 families with nonzero winding are every one of them monomial — and the
monomial generators are exactly the ones on which the parent's Markovian
control shows the defect vanishes identically. Momentum was never missing from
this family; it was on the symbol, where the census of generators could not see
it. On the symbol it separates: 58 distinct reduced dispersions, one per
family, and — the comparison the parent's label deficit actually calls for —
the multiset of member dispersions separates 19 of 19 circulant classes, where
the parent's conjugacy invariants give 14 distinct invariant labels for 22 extended classes.

---

## 1. The question, and what would have answered it the other way

The parent unit's terminal verdict registers motion as not forbidden and reads
none of it. Its successor register names two objects it computes and does not
report: the character-basis dispersions of the circulant family, and the
observation that the admitted lattice is where a propagator cannot be resolved.
This unit is that successor. It asks four things, in order:

1. What are the eigenphases, exactly, for every family at every momentum?
2. Which families and which classes MOVE, and by what velocity?
3. Does the maximal group speed bound anything the parent measured?
4. What, exactly, is the charge-without-momentum tension a statement about?

The pre-registered outcomes are `R4B-DISPERSION-READ`, `R4B-NO-MOTION` and
`R4B-BLOCKED-AT`, and the head is derived from the census by a law all three of
whose outcomes are exercised: with the census's motion count zeroed the head
law returns `R4B-NO-MOTION`, and with one eigenvalue outside μ₈ it returns
`R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8` — the branch the census closes, since
the eigenphase would then have had no exact representation in the declared
field and the census would have stopped rather than approximate one. Both
counterfactuals are gated, not read off the source.

A word on what a positive answer here does *not* buy. Reading a dispersion is
not building a particle. Nothing in this unit constructs a state, propagates
one, or takes a limit. The dispersion is a property of the generator, read in
the basis that diagonalises it; the group velocity is a discrete derivative of
that property; and the whole reading lives on a lattice with 16 sites and
16 momenta.

## 2. The arena, inherited and rebuilt

Everything about the stage is inherited from the parent at hash-pinned paths
and nothing about it is retyped. The lattice size and the dimension are read
from the parent's receipt (L = 4, d = 2), as are the alphabet (25 elements),
the pool (64 generators), the stencil, the sector, the class counts, the
two-point ceilings, the Markovian control and the connective. The connective
clause travels verbatim, as the parent's adjudication requires:
`CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))`. The momentum lattice is
this unit's own declaration, and the pin's sentence declaring it is anchored:
the dual torus, 16 momenta, declared as data.

The family itself is **rebuilt, not imported**. The parent's program is read as
bytes for its digest and is never imported and never executed; the coefficient
alphabet — zero together with ζ₈^t times a modulus in {1, 1/2, 1/√2} — the
9 axes, the unitarity criterion and the gauge quotient are reimplemented here
from the definitions in the parent's paper, over a different exact
representation of the same field. The rebuild is then gated against the
parent's rows object by object:

| gate | what it binds |
|---|---|
| `G-REBUILD-BIJECTION` | every rebuilt coefficient map matches exactly one parent row modulo the global phase, in both directions |
| `G-REBUILD-INVARIANTS` | for every matched pair: axis, axis order, support, radius, monomiality |
| `G-REBUILD-CONTROLS` | the six declared controls, in the parent's construction order |
| `G-CLASS-PARTITION-REBUILT` | every rebuilt class's member set is one of the parent's, set for set |

This is what makes the unit's numbers comparable to the parent's at all: the
two programs share no code and no representation, and the objects are
identified by their content.

The characters are the 16 functions χ_k(x) = ζ₄^{k·x}. For a circulant with
coefficient map c, the symbol is λ(k) = Σ_o c_o ζ₄^{−k·o}, and the eigenvalue
equation M χ_k = λ(k) χ_k is verified as an exact matrix identity at all 928 cells, one per (family, momentum) pair — the eigenphase is not a convention
here, it is a verified eigenvalue.

That the census's domain is exactly the circulant family is not an assumption,
and it is more than a measurement: a generator is diagonal in the lattice
characters if and only if it commutes with every translation, that is, iff its
translation stabiliser is the whole group of 16. The generators with the full
stabiliser are measured to be exactly the 58 circulants; every control's
stabiliser is proper — 8 for the four brickwork generators, index two, and
1 and 2 for the two scrambled ones — so no control *can* be Bloch diagonal, and
the 3 classes carry no Bloch dispersion at all. The measurement and the
forcing agree.

## 3. The dispersion census, exact

The census runs over 58 circulant families and 16 momenta:
928 (family, momentum) cells, exhaustive, not sampled.

**Every eigenvalue is an eighth root of unity.** Measured: every one of the 928 eigenvalues is an 8th root of unity, and independently every one has exact
unit modulus λ·λ̄ = 1. So the eigenphase is the exact exponent s(k) ∈ Z/8 with
λ(k) = ζ₈^{s(k)}, and the dispersion is an exact integer-valued function on the
dual torus.

This is forced, and the reason is worth stating because it is what makes the
whole census exact — including the step the argument turns on. Every
coefficient has a 2-power denominator, and 2 is totally ramified in Q(ζ₈), so a
symbol of unit modulus is an **algebraic integer**: that step is not free (the
number (3+4i)/5 has all conjugates of modulus one and is not a root of unity),
and it is measured rather than asserted — all 928 symbols are algebraic integers, each certified by the
integrality of the characteristic polynomial of multiplication by it. Being a
unit of Z[ζ₈] all of whose conjugates have modulus one — complex conjugation is
central in the Galois group, so σ(λ)·σ(λ)‾ = σ(λλ̄) = 1 for every σ — it is by
Kronecker's theorem a root of unity, and the roots of unity in Q(ζ₈) are
exactly the eight powers of ζ₈. The finite legs are gated with it: the odd part
of every coefficient denominator is one, and the field contains exactly eight
roots of unity.

The eigenphase itself is not gauge invariant — multiplying a generator by ζ₈^t
shifts s(k) by t uniformly, which is measured for every family and every phase
— so the census reports the **reduced dispersion** σ(k) = s(k) − s(0), which
is. Everything downstream is built from differences of s and inherits the
invariance. At the pool's own gauge every exponent that occurs is even, so
every eigenvalue is in fact a fourth root of unity there; that is not the
invariant statement, because the gauge moves the exponents off the even
sublattice and μ₈ is what survives it.

Three facts come out of the census.

**The non-constant count.** 57 of 58 families MOVE, and the exception is
unique. The constant family is identified rather than counted: it is C004, and it is the identity — support one, radius zero, matrix equal to the identity up
to the declared global phase, reduced dispersion identically zero. It is this
unit's no-motion control, and the motion head is required to return its other
value there.

**The parity invariant.** The parity of s(k) is constant on every family:
58 of 58, gated. The reason is the grading: Q(ζ₈) splits as Q(i) ⊕ ζ₈·Q(i),
the unitarity constraints keep a generator's coefficients inside one part, and
ζ₄ ∈ Q(i) preserves it. What is measured is the consequence — every phase
difference is even, so every group velocity is an *integer*, never a
half-integer.

**The symbol separates — and what it separates is families.** There are 58 distinct reduced dispersions, one per family. That is forced (the character
transform is invertible, and reducing by s(0) is exactly the global-phase
quotient) and it is measured. It is *not* a class label: the reduced
dispersion is constant on only the four singleton classes, and on every larger
class it takes as many values as the class has members. The like-for-like
statement is the multiset: the multiset of member reduced dispersions is a
class invariant by construction, and it separates 19 of 19 circulant classes, where the
parent's conjugacy census gives 14 distinct invariant labels for its 22 extended classes, one label
shared by four of them. The label the class table lacks was available in the
symbol the whole time.

Sample rows, reduced dispersions written as the 16 values of σ in
lexicographic order of k:

| family | support | radius | σ(k) | v_max | head |
|---|---|---|---|---|---|
| C004 | 1 | 0 | 0000000000000000 | 0 | STATIC |
| C000 | 3 | 1 | 0022002200220022 | 1 | MOVES |
| C001 | 3 | 1 | 0660066006600660 | 1 | MOVES |
| C002 | 3 | 1 | 0220022002200220 | 1 | MOVES |
| C003 | 3 | 1 | 0066006600660066 | 1 | MOVES |
| C007 | 1 | 1 | 0642064206420642 | 1 | MOVES |

## 4. Group velocity: the definition, its two coordinates, and the tie

The primitive is the phase difference Δ_j s(k) = s(k + e_j) − s(k), an exact
element of Z/8, gauge invariant and branch free. Every reading of a velocity is
a reading of that.

**The declared definition.** v_j(k) = −(L/2π)·[θ(k+e_j) − θ(k)] with
θ = 2πs/8, which reduces to v_j(k) = −lift(Δ_j s(k))/2. Because every Δ_j s is
even — all 1856 cells — the lift is an even integer and the velocity is an
integer.

**The definition has two coordinates, and they are data.** A reading is a
difference *stencil* (forward, backward, central) together with a *lift* of the
antipodal tie (averaged, positive, negative): 9 readings, all computed. They
do not resolve the same way, and the paper does not pretend they do.

**The stencil is forced.** The definition carries its own normalisation: a
monomial shift by an offset o must have velocity o. Read as a criterion rather
than as a remark, that is a test with a verdict. Measured over every monomial
family, every momentum, every direction and every non-antipodal offset
coordinate — the coordinates at which the requirement is not degenerate:

| stencil | monomial normalisation | admitted |
|---|---|---|
| forward | 384 of 384 | yes |
| backward | 384 of 384 | yes |
| central | 128 of 384 | no |

The central stencil fails the definition's own sign-fixing requirement. The
stencil coordinate is therefore forced to 2 by the definition, not chosen against it,
and the fiber of 9 is 3 lifts times 2 admissible stencils.

**The tie, and why there is one.** A lift of Δ_j s to an integer is unique
except at one value. Δ_j s = 4 is a phase advance of exactly π per momentum
step: a displacement of L/2 = 2, which on this torus is its own negative. The
phase does not determine a direction there, because there is no direction to
determine. That value occurs at 320 of 1856 cells, in 19 of 58 families.

**The speed is branch free.** The speed of a cell is the circle distance of its
phase difference to zero, halved — an exact rational that does not depend on
how the antipode is signed. That is independence of the *lift*, of all three;
independence of the stencil is a different statement and is measured below.

**The fiber is printed.** Against the declared reading:

| tie reading | stencil | cells agreeing with the declared reading |
|---|---|---|
| tie-averaged | forward | 1856 |
| tie-averaged | backward | 1088 |
| tie-averaged | central | 832 |
| positive | forward | 1536 |
| positive | backward | 768 |
| negative | forward | 1536 |
| negative | backward | 768 |
| positive | central | 704 |
| negative | central | 704 |

At the declared stencil the other two tie readings agree everywhere except at
the aliased cells, and nowhere else — that is gated, and it is what identifies
the tie as the whole of the lift ambiguity.

**The residual fiber is 2, and it is measured inert.** Once the normalisation
has forced the stencil and section 7's identity has selected the lift, forward
and backward both survive. They are not the same velocity field: they disagree
on the sign of the velocity at 768 of 1856 cells. Every quantity this unit
reports is nevertheless identical under both — the per-family maximal speed
family by family, the speed spectrum, VMAX, the aliasing census and the motion
head — and that invariance is gated rather than assumed. What the residual
declaration buys is a cell-level labelling and nothing else.

The disclosure the exclusion of the central stencil earns is worth printing,
because it is what the segment would have said under a reading the definition
rejects: under the central stencil the maximal speed is 1, strictly below the
diameter, the one-step cone covers 9 of 16 sites, the aliased cells are 512 in
24 families, and the reach partition is 0 over, 41 under, 17 equal. Every
number in section 6 moves. It is excluded by the definition's own
normalisation, and the exclusion is now a gate rather than a preference.

The other declared item of the pair is the character convention, and the census
is recomputed under its other member rather than argued about. The conjugate
convention relabels the dual torus by k ↦ −k; measured family by family, the
speed multiset, the motion head and the aliasing count come out identical, and
the signed velocity and the winding come out exactly negated. The labelling and
the sign in the velocity formula are therefore one declaration and not two: a
reader who prefers the other character gets the same physics with the same
numbers, provided the sign travels with it.

## 5. The motion head, family by family and class by class

Every family carries its own head, bound to its own computed dispersion by its
own predicate: 58 individual verdicts, with no aggregate standing in for any of
them. Two independent routes — non-constant phase, and some nonzero cell speed
— agree on every one. The head is two-way at the control. And it is constant on
every extended class, as it must be (the point group permutes the dual torus
and preserves the max norm) and as it is measured to be, class by class,
together with the maximal speed.

| class | size | supp | radius | v_max | aliased cells | head |
|---|---|---|---|---|---|---|
| C004 | 1 | 1 | 0 | 0 | 0 | STATIC |
| C000 | 4 | 3 | 1 | 1 | 0 | MOVES |
| C001 | 4 | 3 | 1 | 1 | 0 | MOVES |
| C007 | 4 | 1 | 1 | 1 | 0 | MOVES |
| C005 | 4 | 2 | 1 | 2 | 32 | MOVES |
| C009 | 2 | 2 | 2 | 1 | 0 | MOVES |
| C010 | 2 | 2 | 2 | 1 | 0 | MOVES |
| C011 | 2 | 1 | 2 | 2 | 32 | MOVES |
| C020 | 4 | 3 | 1 | 1 | 0 | MOVES |
| C021 | 4 | 3 | 1 | 1 | 0 | MOVES |
| C026 | 4 | 1 | 1 | 1 | 0 | MOVES |
| C024 | 4 | 2 | 1 | 2 | 64 | MOVES |
| C028 | 4 | 3 | 2 | 1 | 0 | MOVES |
| C029 | 4 | 3 | 2 | 1 | 0 | MOVES |
| C034 | 4 | 1 | 2 | 2 | 64 | MOVES |
| C032 | 4 | 2 | 2 | 2 | 96 | MOVES |
| C055 | 1 | 2 | 2 | 1 | 0 | MOVES |
| C056 | 1 | 2 | 2 | 1 | 0 | MOVES |
| C057 | 1 | 1 | 2 | 2 | 32 | MOVES |
| B058 | 4 | — | 1 | — | — | NOT-BLOCH-DIAGONAL |
| S062 | 1 | — | 2 | — | — | NOT-BLOCH-DIAGONAL |
| S063 | 1 | — | 2 | — | — | NOT-BLOCH-DIAGONAL |

So: 18 of the 19 circulant classes MOVE, one is static, and 3 classes carry no Bloch dispersion. The aliased cells are not scattered, and where they sit is
forced by the two definitions rather than discovered: a cell's speed is 2
exactly when its phase difference is antipodal, which is exactly when the cell
is aliased, so the classes whose maximal speed is 2 are precisely the classes
with aliased cells. The neighbouring fact is a measurement and survives: the
families that overshoot their own reach are exactly the radius-1 aliased ones.

## 6. The propagation bound, and the resolution relation

A propagation bound would say that content moves at most VMAX per step. There
are two ways to ask whether that says anything here, and both come back empty —
one of them for a reason no lattice size can repair.

**The cone, and why it is structural.** VMAX = 2 and the torus has max-norm
diameter 2, so the cone after one step already covers 16 of 16 sites. Two
things are worth separating. The ceiling is forced before any family is built:
phase differences lie in Z/8, so the halved circle distance cannot exceed 2,
and the diameter of (Z₄)² is 2. What the census adds is that the ceiling is
*attained*. And the coincidence is not a coincidence at this size — it is a
theorem at every even size. The group speed is a phase advance per momentum
step, so it is bounded by L/2, which is exactly the max-norm diameter; and the
monomial shift by the antipodal offset is a unitary member of the axis family
at every even L and attains it. Exercised at L in {4, 6, 8, 10, 12}:

| L | diameter | antipodal monomial speed | interior radii |
|---|---|---|---|
| 4 | 2 | 2 | 1 |
| 6 | 3 | 3 | 2 |
| 8 | 4 | 4 | 3 |
| 10 | 5 | 5 | 4 |
| 12 | 6 | 6 | 5 |

The one-step cone therefore covers the whole torus at every even L, and no
enlargement of the lattice makes this constraint bite. The parent's composed
segment is two steps; its two-point tables carry 16 of 16 separations and a maximal defect radius of 2 of 2 — both at their ceilings, and the ceiling
disclosure travels with them here. A cone that contains the whole torus
excludes nothing, and it excludes nothing at every step count from one upward.

**The reach, and which count falsifies which bound.** The bound can also be
asked of each family separately, against the thing a bound is supposed to
constrain: the max-norm reach of one step, which for a circulant is exactly its
support radius. Measured family by family: 8 families overshoot it, 14 fall below it, 36 meet it exactly. The direction matters and is derived rather than
labelled. An **upper** bound on the reach is falsified exactly by the families
whose speed exceeds it — the 8 overshooters, every one of them a radius-1
stencil reporting a speed of 2. A **lower** bound is falsified exactly by the
14 undershooters, radius-2 families whose phase advances by only one unit of
displacement per momentum step; those families are perfectly consistent with an
upper bound and merely fail to make it tight. Both bounds fail, at different
counts. The group speed is neither an upper nor a lower bound on the
propagation reach at this scale. **It is not a light-cone velocity.**

**The resolution relation.** The parent observed that the local family lives
exactly where the propagator cannot be resolved. Made precise, in both spaces —
and the two sides are of different kinds, which the unit says rather than
blurs:

- *Position side — a property of the admitted lattice, not of the family.* The
  lattice has three max-norm radius classes, 0, 1 and 2; its diameter is 2; the
  only radius strictly between zero and the diameter is 1. A front can
  therefore take at most one distinguishable value before it has covered
  everything. This leg would read the same if the pool were empty; the
  dispersion enters it only through the cone, which the paragraph above shows
  is structural. The interior-radius count — one here, 3 at L = 8 — is the
  successor's parameter, not this unit's finding.
- *Momentum side — the measurement.* The dual torus carries 4 points per axis
  and the phase takes 8 values, so the phase difference per momentum step
  reaches the antipodal, direction-free value at 320 of 1856 cells, in 19 of 58 families. Where it does, the velocity has a magnitude and no direction.

## 7. Transport: the drift, the winding, and the one reading that joins them

Two quantities answer "how far does one step move it".

*The drift* is the Born expectation of the one-step displacement,
⟨Δx⟩ = Σ_o |c_o|² o, computed in position space from the coefficient map.
*The winding* is the mean group velocity over the dual torus, which by
telescoping is the winding number of the eigenphase around each cycle. They are
different functionals of the same object, computed by different code from
different inputs.

Both carry the same tie, in the same place. In position space, the offset of
max-norm L/2 is its own negative and its signed displacement is undetermined;
on the dual torus, the antipodal phase difference is its own negative and its
signed velocity is undetermined. There are three readings on each side, so
9 tie-reading pairs. The result:

| drift reading \ winding reading | tie-averaged | positive | negative |
|---|---|---|---|
| **tie-averaged** | **58** | 39 | 39 |
| **positive** | 33 | 25 | 32 |
| **negative** | 33 | 32 | 25 |

**Exactly 1 of the 9 tie-reading pairs makes the two agree for every family**:
the tie-averaged reading on both sides, at 58 of 58 families. The best any other
pair achieves is 39 of 58.

**What the identity selects is the tie, and it is blind to the stencil.** The
winding is identical family by family under the forward and the backward
difference — measured — so both reach the identity, and over the full 27
lift × lift × stencil readings the identity holds at 2 of the 27 readings, not at one.
The identity cannot see half of the velocity definition, and the stencil is
fixed by the normalisation of section 4 instead. Together the two mechanisms
leave the residual fiber of 2 that section 4 measures inert.

**And the identity is an arena instrument, not a property of the definition.**
The parent's panel exhibits, at this same lattice size, a unitary two-term
generator over a wider field — c_a = 1/2 at a = (1,0) and c_{−a} = i·√3/2, over
Q(i,√3) — whose sentence is anchored verbatim in this unit's declaration. It is
rebuilt here exactly, in a second field constructed for this one purpose and
used nowhere else: it is unitary at all 16 lags, its eigenphases are exact in Z/12
and every one of them leaves the declared field, its forward differences lift
to 5, 1, 5, 1 with sum 12, and the Born drift is -1/2 and the winding is -1. They are different
numbers. The identity that fixes the convention here fails at the first
widening of the modulus set, so it may serve as an instrument for selecting the
tie in this arena and never as the conclusion that the velocity definition is
not free. Whether it fails generically is open, and it is registered in
section 11 as this unit's most consequential open.

That same reading identifies a convention that was never stated. The parent's
panel published a one-step drift table by support; this unit's independent
rebuild reproduces it, and computes the alternatives it is silent about:

| support | generators | nonzero drift, tie-averaged | positive | negative |
|---|---|---|---|---|
| 1 (monomial) | 16 | 12 | 15 | 15 |
| 2 | 18 | 0 | 10 | 10 |
| 3 | 24 | 0 | 8 | 8 |

Under the tie-averaged reading, and only under it, the three rows come out as
the panel printed them — 16 | 12, 18 | 0, 24 | 0. Under either alternative they
read 16 | 15, 18 | 10 and 24 | 8. The exclusion is evaluated over all three
lifts rather than asserted for one. The panel's table was taken under the
reading that averages the antipodal tie, and that fact is now measured rather
than inferred.

## 8. Charge without momentum: the measured statement and its readings

The parent's operator review put the tension sharply: the translation group is
the only part of the arena that could carry a momentum label, and on the
circulant family it acts with a single orbit type — trivially. That is
re-derived here as a measurement on every generator rather than inherited:
conjugation by a translation fixes all 58 circulants, whose stabiliser is the
whole group of 16, and fixes no control. The class census therefore produced
charge-like invariants and no momentum-like invariant whatever. The effectus
review put the position-space half of it: the generators that move never
interfere, and the generators that interfere never move.

What this unit measures. The word for the 42 is **non-monomial**, which is what
the instrument tests; interference is not asserted of them by a rename, it is
inherited by binding each of them to the parent's own rows:

- **The non-monomial families all move.** 42 non-monomial families carry
  non-constant dispersions and nonzero group velocities at individual momenta.
  Every one of them is MOVES: all 42 of them MOVE.
- **The word is earned, not assumed.** In the parent's 4096-row defect census
  the generators whose *diagonal* composition defect is nonzero are exactly
  this unit's non-monomial families, 42 of 42, and the generators on which the
  defect vanishes across every pair they appear in are exactly its 16 monomial families. No defect is recomputed here; the binding is to the anchored
  receipt.
- **They transport nothing — at the selected reading, and how much of that is
  the reading is measured.** All 42 have exactly zero net transport in both
  spaces under the declared tie. The zero is reading-independent for 24 of the 42 in position space and for 30 of the 42 on the dual torus; for the
  remaining 18 and 12 it is the antipodal average, and the 12 are exactly the
  non-monomial families that carry aliased cells. The reading-independent part
  is the object a successor inherits.
- **Only the monomials transport.** 12 families with nonzero winding, every one of them monomial, out of 16 monomial families (the identity and the three
  self-antipodal shifts have zero net transport for the reason section 7
  gives). The parent's Markovian control puts the other half of the statement
  in place, and this unit binds it to its own count rather than quoting it:
  the control's 1792 pairs are exactly the pairs of the 64 with a monomial
  member, 64² − 48², so the generators on which the composition defect
  vanishes identically — 0 of 1792 — are precisely this unit's 16 monomial families.
- **The momentum label exists and separates.** 58 distinct reduced dispersions for 58 families, and, class for class, the dispersion multiset separating
  19 of 19 circulant classes.

Three readings of the tension are available, and this unit names all three
rather than deciding between them:

1. **Category.** The parent censused *generators* under conjugation, and
   translations act trivially there by construction. Momentum is a label of the
   *state*, and it lives on the symbol. On this reading the missing momentum
   label is a fact about what was classified, not about the physics, and the
   symbol supplies the grading the labels lack — at the class level through the
   multiset, which is the form the parent's deficit actually calls for.
2. **Cancellation, in the arithmetic of the average.** Motion is present at
   every momentum and sums to zero over the dual torus for every non-monomial
   family. On this reading "charge without momentum" is exactly true of the
   *net* transport and exactly false of the momentum-resolved velocity, and the
   two halves of the panel's sentence are about different objects. Nothing is
   propagated anywhere in this unit and no coherence functional is computed, so
   the word describes a sum of nonzero summands that vanishes and claims
   nothing about a state.
3. **Resolution.** At this scale the dual torus is too coarse to separate the
   first two: 19 of 58 families have a direction-free phase difference
   somewhere, and the velocity read-off there has a magnitude and no sign.

The measurements support 2 outright on its reading-independent part — 24 of the
42 in position space, 30 of the 42 on the dual torus — support 1 as a
structural fact, and on the remaining 18 and 12 they *are* the size of 3.
Deciding among them needs a scale this stage does not have. And nothing here is
theorem-forced: the zero net transport of the non-monomial families is
alphabet-relative, which section 7's witness exhibits at this same lattice
size.

## 9. What this decides, and what it does not

**Decided.** The dispersions exist, are exact, and are read: 57 of 58 families MOVE, 18 of the 19 circulant classes move, the speed spectrum is {0, 1, 2},
VMAX = 2. The eigenphase lattice is Z/8 and the velocities are integers, both
for stated reasons and both gated. The propagation bound is empty in both
senses available at this scale, and its cone half is empty at every even scale.
The drift and the winding agree for every family under exactly one of the
9 tie-reading pairs; that pair is the one the parent's panel used; and the
agreement is a fact about this alphabet, not about the definition.

**Not decided.** Whether any of this survives a widened modulus set, a larger
lattice, or a family that is not circulant — and, in particular, the domain of
validity of the selecting identity, of which this unit exhibits one
counterexample and no census. The parent's uniqueness theorem confines the
local non-monomial family to this one lattice size, so a dispersion measurement
that resolves a front must leave the local class, widen the alphabet, or leave
the admitted size — the successor register carries that. Nothing here is a
claim about a continuum, an infinite volume, a long time, or an interacting
theory.

**Not executed.** No state is propagated and no wavepacket is built; the
velocity is read off the exact eigenphase. No defect is recomputed — every
defect number is inherited from the parent's receipt at a hash-pinned path. The
non-circulant controls are measured not to be Bloch diagonal and are then left
alone: the finer decomposition their index-two translation stabiliser would
allow is not built. The alphabet is not widened as a census: the wider field
carries exactly one generator here, as a scope witness, and no result of this
unit is claimed for it. Indivisibility is declared by the division-event times
and is never measured, exactly as in the parent.

## 10. The instrument

82 gates, all passed — 81 of them evaluated inside the receipt, the last being
the terminal integrity gate, which the writing path evaluates against the bytes
it wrote and which the receipt therefore cannot carry. 79 carrying their own injection falsifier and 3 their registered forcing; 86 declared mutants, all dead, and every one killed by the
gate it was declared to falsify. 42 anchors: 8 file-bytes anchors,
20 path-value anchors and 14 verbatim-text anchors, each verbatim window
pinned by the digest of its own bytes, required to occur exactly once in its
source, and bound to the named gate that consumes it.

Gates bind objects rather than cardinalities, and they bind the rows the
artifact ships. The rebuild is bound family by family across two exact
representations; the motion head is bound family by family to its own
dispersion; the class partition is bound set by set; the eigenvalue equation is
checked as a matrix identity at every cell, not sampled. The published census
table is re-rendered from the state and compared field by field, so a control's
datum cannot ship under a census label and no field can move after the object
gates closed. Coverage of the ledger is itself measured twice over: one gate
requires every gate this unit evaluates to be the declared target of at least
one mutant — the only exceptions being the three evaluated after the in-process
sweep closes, each of which registers the mechanism that falsifies it instead —
and another requires every verbatim anchor to name a gate that exists and is
reached.

The verdict carries 74 measured values, each with its own flip probe:
perturbing the receipt key a value renders from must move the complete
reconstruction. The complete verdict string — head included — is rebuilt from
the *serialized* receipt by a path that shares no helper and no head law with
the assembler, and the two strings are compared character for character. What
the two paths necessarily share is the segment grammar — that is the thing the
equality tests — and what they do not share is any value: every numeral in
either path is read from the computed counts, and the head is derived twice,
from two independently written copies of the head law, whose three outcomes are
all exercised.

**The gate-to-disk seal.** A gate that fires on an object still mutable when
the artifact is built has not gated the artifact. Every object this run
publishes is digested at the moment its own gate passes — 18 sealed objects, the
verdict string and head, the counts, the census and class tables, the fiber and
agreement matrices, the drift tables, the stratification block, the anchor
tables, the waiver ledger, the mutant report, the totals and the coverage. The
payload may be sealed only if every earlier seal still verifies; the artifacts
are written from the sealed payload and from nothing else; and the terminal
integrity gate compares the bytes that landed on disk against those gate-time
digests, never against a re-derivation from those same bytes. The write is
staged through temporaries and moved into place only after it matches, so a
failing integrity check leaves the previous artifacts untouched. The gate's
negative control is unchanged and still fires: a deliberately corrupted payload
written to a probe path must be detected first.

The paper is an object under test, not a narration. Every claim string the
receipt renders must occur in it verbatim; every numeral in it must render from
a computed value or sit in a declared residue; and — because a numeral check is
blind to direction — every declared claim must occur the number of times the
instrument expects, with the polarity-bearing ones guarded against a declared
list of negators. All three run as gates inside the delivery run, and
`--verify-paper PATH` runs the same three against any file, exiting 1 on drift
and 2 on a path that does not exist.

The CLI is argv-parsed against a whitelist, exercised by its own probes, and
the permissive shape — the registered disease — fails the gate. No diagnostic
path can write: the self-test, the mutant runner and the anchor-break runner
all leave the parser with writing disabled, measured on the parser's output.
The self-test corrupts one anchor in memory, dies at the anchor gate and writes
nothing. A standing probe walks every gate call in the instrument's own source
and reports any predicate that reads the mutant switch by either shape — the
call or the bare global; none does. An AST scan establishes that the instrument
never invokes a subprocess and never calls git, so the run is correct off-tree
and in a directory with no version control at all — both tested. The receipt
carries the digest of the instrument that produced it. Two plain runs are
byte-identical in both artifacts.

## 11. The successor register

**The alphabet, not the lattice — and not the cone.** Section 6's cone result
is structural and no lattice size repairs it, so a successor must not run L = 8
to test it. What L = 8 changes is the interior-radius count, 1 here and 3 at
L = 8, which governs whether a front can take distinguishable intermediate
values across several steps; that, and the multi-step front, are what an L = 8
census is for. One constraint comes with it: the parent's uniqueness theorem
confines the local non-monomial family to L ≤ 4, so an L = 8 census is a census
of monomials plus non-local families, and for monomials speed and reach
coincide identically — the reach partition will degenerate, and a successor
should pre-register that.

**The selection's domain — the most consequential open.** The drift = winding
identity is what selected the tie, so its domain of validity is the domain of
the selection. This unit exhibits one counterexample and runs no census. A
successor should census the identity's failure over a widened alphabet: if it
fails generically, the tie reverts to DECLARED and every transport number in
this paper becomes reading-relative in the way section 8's split already
measures for part of it. The same widening re-poses the aliasing question:
the widened generator's eigenphases leave μ₈, so the successor must first
determine the actual root order N and re-run the census in Z/N, where the
aliased value is N/2; whether it is still attained decides whether the
resolution failure is structural or belonged to the alphabet. Pre-register both
outcomes.

**The non-abelian stratum has no dispersion yet, and its exclusion is a
theorem.** The four brickwork generators are not diagonal in the character
basis, and section 2 gives the forcing rather than the observation: Bloch
diagonal iff the translation stabiliser is the whole group, and theirs is
measured at 8, index two in the group of 16. So they are block-diagonalised by
a coarser character set, in two-dimensional blocks. Their eigenphases are the
first thing a gauge unit will need and the first thing that will not be in
Q(ζ₈); a gauge unit's pin must declare the field it will construct, gate its
exactness, and carry a blocked-at-eigenphase outcome as this unit did.

**The state census, and what it may not inherit.** This unit reads the
dispersion of *generators*. The operator review's proposal was a census of
(state, generator) pairs labelled by (k, θ(k)); section 3 measures that the
label separates the whole family, so the census is now well posed. What it
needs is a declared state sector, and that is a decision, not a measurement.
It may inherit the momentum label. It may **not** inherit any transport number
from this unit: the zero net transport of the 42 is a Born average over the
dual torus *in the single-occupation sector*, which SCOPE declares, and a
multi-occupation sector changes the measure. The first question there is
sharp — build a state supported on the non-cancelling momenta of one
non-monomial family and measure its drift — and both outcomes should be
pre-registered.

## 12. Deviations, and the register of scope

The scope segment inherits the parent's verbatim and adds this unit's own
declaration: d = 2; L = 4; the field; the alphabet; 64 generators; the 3-term
axis stencil; single occupation; the dual torus with 16 momenta, declared; the
velocity reading, with its two coordinates named; the character convention,
declared jointly with the sign of the velocity formula;
`CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))`; indivisibility declared
by the division-event times; finite lattice only; no continuum claim; no
interacting-theory claim beyond the composed-segment defect. The unique scale
is a theorem about the anchored link set and the declared alphabet, not a law
of the substrate, and that qualification travels with every number here.

Declared items, with their fibers and their status:

| item | fiber | status | what fixes it |
|---|---|---|---|
| the momentum lattice | 1 | DECLARED (the pin) | the characters are the only simultaneous eigenbasis of the family at the admitted size |
| the character convention | 2 | DECLARED, jointly with the velocity sign | the speeds, heads and aliasing census measured invariant; signed velocity and winding measured to negate |
| the eigenphase branch | 1 | DECLARED | the phase is the verified eigenvalue's exponent; the reduction by s(0) is the gauge quotient |
| the velocity **stencil** | 3 → 2 | **FORCED** | the definition's own monomial normalisation: 384 of 384 against 128 of 384 |
| the velocity **lift** | 3 → 1 | **SELECTED, arena-relatively** | drift = winding at 58 of 58 against a best other of 39 of 58 — an instrument, and section 7's witness bounds it |
| the residual stencil | 2 | DECLARED, measured inert | every reported quantity identical; 768 of 1856 cells differ in the sign of the velocity alone |
| the non-monomiality of the 42 | — | BOUND, not renamed | each of the 42 tied to its own nonzero diagonal defect row in the parent's receipt |
| the selection criterion itself | — | **arena instrument, post hoc** | it fails over the wider field at this same lattice size; its domain is section 11's registered open |

Two entries deserve their own sentence, because they are what a reader must
carry away. The velocity reading is a declared arena coordinate in the sense
RUNBOOK §15 means: a successor that inherits SCOPE inherits the stencil, the
lift and the residual with it, and any cross-unit comparison must match all
three. And the drift = winding identity, being a property of this alphabet
rather than of the definition, enters this paper as an instrument and never as
a conclusion.

The programme's false-claim register stands where the parent's adjudication
left it: 5, all prose, none in a computed artifact. Every number in this paper
is rendered from the receipt; where a number is relative to a reading, the
reading is named beside it in the verdict rather than left to the prose.

---

*Every number in this paper is rendered from the receipt, and the coverage,
polarity and claim checks that enforce it run inside the delivery run as gates.*
