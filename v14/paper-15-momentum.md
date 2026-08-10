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
own no-motion control, returning the head's other value. The velocity spectrum
is {0, 1, 2}, the maximal group speed is VMAX = 2, and 18 of the 19 circulant
classes move.

The propagation bound the parent left open comes back empty, and it comes back
empty twice over. VMAX equals the max-norm diameter of the lattice, so the cone
after a single step of the fastest family already covers 16 of 16 sites: the
constraint excludes no separation the parent's two-point tables could carry,
and those tables sit at their ceilings anyway. And the group speed is not even
a reach bound family by family: measured against each family's own one-step
reach, 8 families overshoot it, 14 fall below it, 36 meet it exactly. A
velocity that both overshoots and undershoots the support it came from is not a
light-cone velocity. The parent's closing observation — that the local family
lives exactly where the propagator cannot be resolved — becomes a measured
relation in both spaces at once: on the site side the torus has exactly one
max-norm radius strictly between zero and its diameter, and one step crosses
the whole diameter; on the momentum side the phase difference reaches its
antipodal, direction-free value at 320 of 1856 cells, in 19 of 58 families.

Two results were not asked for. First, **the velocity convention is not free.**
The antipodal tie — the displacement of half the lattice, which is its own
negative — has to be resolved twice, once in position space and once on the
dual torus, and there are 9 ways to do it. Exactly one of them makes the Born
drift of a family equal the winding of its eigenphase, and it does so for
58 of 58 families; the best any other pairing manages is 39 of 58. The reading
that works is the one that resolves both ties the same way, by averaging, and
it is also — measured, not assumed — the reading under which the parent panel's
one-step drift table comes out exactly as the panel printed it. A convention
that was expected to be declared turns out to be selected by an identity.

Second, **the tension the panel called "charge without momentum" is a
cancellation, not an absence.** The 42 interfering families all have exactly
zero net transport, in both spaces, and every one of them MOVES: non-constant
dispersion, nonzero group velocity at individual momenta, summing to nothing
over the dual torus. The 12 families with nonzero winding are every one of
them monomial — and the monomial generators are exactly the ones on which the
parent's Markovian control shows the defect vanishes identically. Momentum was never missing from this family; it was on the
symbol, where the census of generators could not see it. On the symbol it
separates completely: 58 distinct reduced dispersions where the parent's
conjugacy invariants give 14 distinct invariant labels for 22 classes.

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
`R4B-BLOCKED-AT`, and the head is derived from the census by a law with all
three reachable: with the census's motion count zeroed, the head law returns
`R4B-NO-MOTION`, and a gate proves it. The unit would have returned
`R4B-BLOCKED-AT` if the eigenvalues had not been roots of unity — the
eigenphase would then have had no exact representation in the declared field,
and the census would have stopped rather than approximate one.

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
equation M χ_k = λ(k) χ_k is verified as an exact matrix identity at all
928 cells, one per (family, momentum) pair — the eigenphase is not a convention
here, it is a verified eigenvalue. The six declared controls are measured *not* to be
diagonal in this basis, so the census's restriction to the circulant family is
a measurement rather than an assumption, and the 3 classes those controls form
carry no Bloch dispersion at all.

## 3. The dispersion census, exact

The census runs over 58 circulant families and 16 momenta:
928 (family, momentum) cells, exhaustive, not sampled.

**Every eigenvalue is an eighth root of unity.** Measured: every one of the
928 eigenvalues is an 8th root of unity, and independently every one has exact
unit modulus λ·λ̄ = 1. So the eigenphase is the exact exponent s(k) ∈ Z/8 with
λ(k) = ζ₈^{s(k)}, and the dispersion is an exact integer-valued function on the
dual torus.

This is forced, and the reason is worth stating because it is what makes the
whole census exact. Every coefficient has a 2-power denominator, so a symbol of
unit modulus is a unit of Z[ζ₈] all of whose conjugates have modulus one —
complex conjugation is central in the Galois group, so σ(λ)·σ(λ)‾ = σ(λλ̄) = 1
for every σ. By Kronecker's theorem such a number is a root of unity, and the
roots of unity in Q(ζ₈) are exactly the eight powers of ζ₈. The finite legs of
that argument are gated: the odd part of every coefficient denominator is one,
and the field contains exactly eight roots of unity.

The eigenphase itself is not gauge invariant — multiplying a generator by ζ₈^t
shifts s(k) by t uniformly, which is measured for every family and every phase
— so the census reports the **reduced dispersion** σ(k) = s(k) − s(0), which
is. Everything downstream is built from differences of s and inherits the
invariance.

Three facts come out of the census.

**The non-constant count.** 57 of 58 families MOVE, and the exception is
unique. The constant family is identified rather than counted: it is C004, and
it is the identity — support one, radius zero, matrix equal to the identity up
to the declared global phase, reduced dispersion identically zero. It is this
unit's no-motion control, and the motion head is required to return its other
value there.

**The parity invariant.** The parity of s(k) is constant on every family:
58 of 58, gated. The reason is the grading: Q(ζ₈) splits as Q(i) ⊕ ζ₈·Q(i),
the unitarity constraints keep a generator's coefficients inside one part, and
ζ₄ ∈ Q(i) preserves it. What is measured is the consequence — every phase
difference is even, so every group velocity is an *integer*, never a
half-integer.

**The symbol separates.** There are 58 distinct reduced dispersions, one per
family. That is forced (the character transform is invertible, and reducing by
s(0) is exactly the global-phase quotient) and it is measured. The contrast is
the point: the parent's conjugacy census gives 14 distinct invariant labels for
its 22 extended classes, with one label shared by four classes. The label the
class table lacks was available in the symbol the whole time.

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

## 4. Group velocity: the definition, its fiber, and the tie

The primitive is the phase difference Δ_j s(k) = s(k + e_j) − s(k), an exact
element of Z/8, gauge invariant and branch free. Every reading of a velocity is
a reading of that.

**The declared definition.** v_j(k) = −(L/2π)·[θ(k+e_j) − θ(k)] with
θ = 2πs/8, which reduces to v_j(k) = −lift(Δ_j s(k))/2. The sign is fixed by
the requirement that a monomial shift by an offset o have velocity o, and that
is what it does. Because every Δ_j s is even — all 1856 cells — the lift is an
even integer and the velocity is an integer.

**The tie, and why there is one.** A lift of Δ_j s to an integer is unique
except at one value. Δ_j s = 4 is a phase advance of exactly π per momentum
step: a displacement of L/2 = 2, which on this torus is its own negative. The
phase does not determine a direction there, because there is no direction to
determine. That value occurs at 320 of 1856 cells, in 19 of 58 families.

**The speed is branch free.** The speed of a cell is the circle distance of its
phase difference to zero, halved — an exact rational that does not depend on
how the antipode is signed. Measured: the speed spectrum is {0, 1, 2} and
VMAX = 2.

**The fiber is printed.** Three readings of the tie (averaged, positive,
negative) times three difference stencils (forward, backward, central) give
9 readings, all computed. Against the declared one:

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
the tie as the whole of the ambiguity.

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

So: 18 of the 19 circulant classes MOVE, one is static, and 3 classes carry no
Bloch dispersion. The aliased cells are not scattered, and the reason is worth
seeing: a cell's speed is 2 exactly when its phase difference is antipodal, so
the classes whose maximal speed is 2 are precisely the classes with aliased
cells. **The top of the speed spectrum is the resolution limit itself.**

## 6. The propagation bound, and the resolution relation

A propagation bound would say that content moves at most VMAX per step. There
are two ways to ask whether that says anything here, and both come back empty.

**The cone.** VMAX = 2 and the torus has max-norm diameter 2, so the cone after
one step already covers 16 of 16 sites. The parent's composed segment is two
steps; its two-point tables carry 16 of 16 separations and a maximal defect
radius of 2 of 2 — both at their ceilings, and the ceiling disclosure travels
with them here. A cone that contains the whole torus excludes nothing, and it
excludes nothing at every step count from one upward.

**The reach.** The bound can also be asked of each family separately, against
the thing a bound is supposed to constrain: the max-norm reach of one step,
which for a circulant is exactly its support radius. Measured family by family:
8 families overshoot it, 14 fall below it, 36 meet it exactly. Every overshooting
family is an aliased one — a radius-1 stencil reporting a speed of 2 — and the
undershoot sits at radius-2 families whose phase advances by only one unit of
displacement per momentum step. The group speed is therefore neither an upper
nor a lower bound on the propagation reach at this scale. **It is not a
light-cone velocity.**

**The resolution relation.** The parent observed that the local family lives
exactly where the propagator cannot be resolved. Made precise, in both spaces:

- *Position side.* The lattice has three max-norm radius classes, 0, 1 and 2;
  its diameter is 2; the only radius strictly between zero and the diameter is
  1. A front can therefore take at most one distinguishable value before it has
  covered everything — and the fastest family covers everything in a single
  step.
- *Momentum side.* The dual torus carries 4 points per axis and the phase takes
  8 values, so the phase difference per momentum step reaches the antipodal,
  direction-free value at 320 of 1856 cells in 19 of 58 families. Where it
  does, the velocity has a magnitude and no direction.

Neither side is an artifact of the instrument: the first is a property of the
lattice the parent's uniqueness theorem selected, and the second is a property
of its dual. The observation is now a measured relation, not a remark.

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
9 reading pairs. The result:

| drift reading \ winding reading | tie-averaged | positive | negative |
|---|---|---|---|
| **tie-averaged** | **58** | 39 | 39 |
| **positive** | 33 | 25 | 32 |
| **negative** | 33 | 32 | 25 |

**Exactly 1 of the 9 reading pairs makes the two agree for every family**: the
tie-averaged reading on both sides, at 58 of 58 families. The best any other pair achieves
is 39 of 58. The convention is selected by the identity rather than declared
against it — which is why the declared reading in section 4 is the averaged
one.

That same reading identifies a convention that was never stated. The parent's
panel published a one-step drift table by support:

| support | generators | nonzero drift |
|---|---|---|
| 1 (monomial) | 16 | 12 |
| 2 | 18 | 0 |
| 3 | 24 | 0 |

Under the tie-averaged reading, and only under it, this unit's independent
rebuild reproduces those rows exactly — 16 | 12, 18 | 0, 24 | 0. Under the
positive reading the same three rows read 16 | 15, 18 | 10 and 24 | 8. The
panel's table was taken under the reading that averages the antipodal tie, and
that fact is now measured rather than inferred.

## 8. Charge without momentum: the measured statement and its readings

The parent's operator review put the tension sharply: the translation group is
the only part of the arena that could carry a momentum label, and on the
circulant family it acts with a single orbit type — trivially. That is
re-derived here as a measurement on every generator rather than inherited:
conjugation by a translation fixes all 58 circulants, whose stabiliser is the
whole group of 16, and fixes no control — the four brickwork generators have an
index-two stabiliser of 8. The class census
therefore produced charge-like invariants and no momentum-like invariant
whatever. The effectus review put the position-space half of it: the generators
that move never interfere, and the generators that interfere never move.

What this unit measures:

- **The interfering families all move.** 42 interfering families carry
  non-constant dispersions and nonzero group velocities at individual momenta.
  Every one of them is MOVES.
- **They transport nothing.** All 42 have exactly zero net transport, in both
  spaces: zero drift and zero winding.
- **Only the monomials transport.** 12 families with nonzero winding, every one
  of them monomial, out of 16 monomial families (the identity and the three
  self-antipodal shifts have zero net transport for the reason section 7
  gives). The parent's Markovian control puts the other half of the statement
  in place, and this unit binds it to its own count rather than quoting it:
  the control's 1792 pairs are exactly the pairs of the 64 with a monomial
  member, 64² − 48², so the generators on which the composition defect
  vanishes identically — 0 of 1792 — are precisely this unit's 16 monomial
  families.
- **The momentum label exists and separates.** 58 distinct reduced dispersions
  for 58 families, against 14 distinct invariant labels for 22 extended
  classes.

Three readings of the tension are available, and this unit names all three
rather than deciding between them:

1. **Category.** The parent censused *generators* under conjugation, and
   translations act trivially there by construction. Momentum is a label of the
   *state*, and it lives on the symbol. On this reading the missing momentum
   label is a fact about what was classified, not about the physics, and the
   symbol supplies the grading the labels lack — which is what the operator
   review's second route proposed and what section 3 measures.
2. **Cancellation.** Motion is present at every momentum and cancels over the
   dual torus for every interfering family. On this reading "charge without
   momentum" is exactly true of the *net* transport and exactly false of the
   momentum-resolved velocity, and the two halves of the panel's sentence are
   about different objects.
3. **Resolution.** At this scale the dual torus is too coarse to separate the
   first two: 19 of 58 families have a direction-free phase difference
   somewhere, and the velocity read-off there has a magnitude and no sign. On
   this reading the tension is a resolution artifact of the admitted lattice —
   which is the parent's own propagator observation, arriving from the other
   side.

The measurements support 2 outright, support 1 as a structural fact, and
measure the size of 3. Deciding among them needs a scale this stage does not
have.

## 9. What this decides, and what it does not

**Decided.** The dispersions exist, are exact, and are read: 57 of 58 families
MOVE, 18 of the 19 circulant classes move, the velocity spectrum is {0, 1, 2},
VMAX = 2. The eigenphase lattice is Z/8 and the velocities are integers, both
for stated reasons and both gated. The propagation bound is empty in both
senses available at this scale. The drift and the winding agree for every
family under exactly one of the 9 reading pairs, and that pair is the one the
parent's panel used.

**Not decided.** Whether any of this survives a widened modulus set, a larger
lattice, or a family that is not circulant. The parent's uniqueness theorem
confines the local non-monomial family to this one lattice size, so a
dispersion measurement that resolves a front must leave the local class, widen
the alphabet, or leave the admitted size — the successor register carries that.
Nothing here is a claim about a continuum, an infinite volume, a long time, or
an interacting theory.

**Not executed.** No state is propagated and no wavepacket is built; the
velocity is read off the exact eigenphase. No defect is recomputed — every
defect number is inherited from the parent's receipt at a hash-pinned path. The
non-circulant controls are measured not to be Bloch diagonal and are then left
alone: the finer decomposition their index-two translation stabiliser would
allow is not built. The alphabet is not widened, so the effectus review's
constructive motion-carrying generator over a larger field is not built here.
Indivisibility is declared by the division-event times and is never measured,
exactly as in the parent.

## 10. The instrument

67 gates, all passed — 64 carrying their own injection falsifier and 3 their
registered forcing; 66 declared mutants, all dead, and every one killed by the
gate it was declared to falsify. 41 anchors: 8 file-bytes anchors,
20 path-value anchors and 13 verbatim-text anchors, each verbatim window bound
to the named gate that consumes it.

Gates bind objects rather than cardinalities. The rebuild is bound family by
family across two exact representations; the motion head is bound family by
family to its own dispersion; the class partition is bound set by set; the
eigenvalue equation is checked as a matrix identity at every cell, not sampled.
Coverage of the ledger is itself measured twice over: one gate requires every
gate this unit evaluates to be the declared target of at least one mutant — the
only exceptions being the three evaluated after the in-process sweep closes,
each of which registers the mechanism that falsifies it instead — and another
requires every verbatim anchor to name a gate that exists and is reached, so a
window bound to a gate the run never evaluates is caught rather than displayed.

The verdict carries 56 measured values, each with its own flip probe:
perturbing the receipt key a value renders from must move the complete
reconstruction. The complete verdict string — head included — is rebuilt from
the *serialized* receipt by a path that shares no helper and no head law with
the assembler, and the two strings are compared character for character. What
the two paths necessarily share is the segment grammar — that is the thing the
equality tests — and what they do not share is any value: every numeral in
either path is read from the computed counts, and the head is derived twice,
from two independently written copies of the head law. The head law is exercised in both directions: with the motion census
zeroed it returns the pin's other outcome.

The CLI is argv-parsed against a whitelist, exercised by its own probes, and
the permissive shape — the registered disease — fails the gate. No diagnostic
path can write: the self-test, the mutant runner and the anchor-break runner
all leave the parser with writing disabled, measured on the parser's output.
The self-test corrupts one anchor in memory, dies at the anchor gate and writes
nothing. A standing probe walks every gate call in the instrument's own source
and reports any predicate that reads the mutant switch; none does. An AST scan
establishes that the instrument never invokes a subprocess and never calls
git, so the run is correct off-tree and in a directory with no version control
at all — both tested. A final integrity gate is two-way: a deliberately
corrupted payload is written to a probe path and required to be detected before
the real artifacts are written, re-read, and required to match byte for byte,
with the verdict reconstructed from the bytes that landed on disk. Two plain
runs are byte-identical in both artifacts.

## 11. The successor register

**The alphabet, not the lattice.** Every negative result in section 6 is a
resolution result, and resolution is set by two numbers: the number of radius
classes on the site torus and the number of points per axis on its dual. Both
are fixed by L = 4, and L = 4 is forced by the parent's uniqueness theorem
*given its alphabet*. The effectus review exhibits a motion-carrying,
interference-carrying generator over a wider field at the same lattice size. A
successor that widens the modulus set gets a family in which drift and defect
coexist, and — this is the new part — a dual torus on which the aliasing census
of section 4 can be re-run to see whether the direction-free cells survive. If
they do, the resolution failure is structural; if they vanish, it belonged to
the alphabet.

**The non-abelian stratum has no dispersion yet.** The four brickwork
generators are measured here not to be diagonal in the character basis, and
they are the parent's only non-commuting generators — the stratum the gauge
rung is pinned to build on. Their translation stabiliser is measured here at 8,
index two in the group of 16, so they are block-diagonalised by a coarser
character set, in two-dimensional blocks.
Their eigenphases are the first thing a gauge unit will need and the first
thing that will not be in Q(ζ₈).

**The state census.** This unit reads the dispersion of *generators*. The
operator review's proposal was a census of (state, generator) pairs labelled by
(k, θ(k)); section 3 measures that the label separates the whole family, so the
census is now well posed. What it needs is a declared state sector, and that is
a decision, not a measurement.

## 12. Deviations, and the register of scope

The scope segment inherits the parent's verbatim and adds this unit's own
declaration: d = 2; L = 4; the field; the alphabet; 64 generators; the 3-term
axis stencil; single occupation; the dual torus with 16 momenta, declared;
`CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))`; indivisibility declared
by the division-event times; finite lattice only; no continuum claim; no
interacting-theory claim beyond the composed-segment defect. The unique scale
is a theorem about the anchored link set and the declared alphabet, not a law
of the substrate, and that qualification travels with every number here.

Declared items, with their fibers: the momentum lattice (declared by the pin,
fiber 1 at the admitted size); the character convention (fiber 2 — the
conjugate convention relabels the dual torus by k ↦ −k; the speeds, the heads
and the aliasing census are measured invariant under it and the signed
velocities are measured to negate, so it is declared jointly with the sign of
the velocity formula); the eigenphase branch (fiber 1 — the phase is the verified
eigenvalue's exponent, and the reduction by s(0) is the gauge quotient); the
velocity definition (fiber 9, printed in full in section 4, with the declared
member selected by the identity of section 7).

The programme's false-claim register stands where the parent's adjudication
left it: 5, all prose, none in a computed artifact.

---

*Every number in this paper is rendered from the receipt, and the coverage
check that enforces it runs inside the delivery run as a gate.*
