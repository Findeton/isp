# PAPER-10 (R4) — SCOPE ANNOTATION, NOT AN ERRATUM

**Status:** registered by the PER-L joint adjudication
(`v14/note-perl-adjudication.md`, ruling 3, commit 44d65a3) and written
here as a standing note.  **Paper-10 is terminal and is not edited, and
neither is paper-15.**  R4's claim was true of its own object; what
follows records which object that was, and where a wider object gives a
different answer.

The register row below is the adjudication's, lifted from the seat
finding it adopted, and it is the operative content of this note.

> **PAPER-10 (R4) — SCOPE ANNOTATION, NOT AN ERRATUM.**  R4's
> `SCALE=L=4-UNIQUE` is a theorem at R4's declared window radius, which is one:
> the locality half sweeps the radius-one max-norm ball (§2, "each with its own
> radius-one ball"), and the interference half is proven for the whole
> radius-one ball, field-free (§3, Moore-ball collapse).  Both are true of that
> object.  R4's head string carries the forced connective but not the radius.
> PER-L measures the same two requirements at window widths 2 and 3 and finds
> they meet again — at {6,8} and at {8,10,12} respectively, by an
> involution-pair construction verified against R4's own whole-torus criterion.
> Nothing of R4 is withdrawn: at radius one the admitted set is {4} and PER-L
> re-proves the absence half by a second, counting proof of R4's own ball
> theorem.  What is annotated is the reading: **`L = 4 is unique` is a
> statement about the parent's window, as `MAX-NORM` is a statement about the
> parent's link set — the same species of relativity R4 §12 already
> registered, on a second coordinate.**  The R4 §11 and R4b §9 trichotomies
> ("widen the modulus set / leave the local class / leave the admitted size")
> gain a named fourth branch, *widen the window*, which sits inside "leave the
> local class" only because "local" there means radius-one.  Paper-10 and
> paper-15 are terminal and are not edited.

**One thing in that row was overtaken by the repair pass it launched.**
The width-2 section is **{6, 7, 8}**, not {6, 8}: the involution-pair
construction the row names is one mechanism of two, and the odd size is
carried by the other.  The annotation's content is unaffected — the
relativity is the same relativity, on the same coordinate — but the
section is recorded here at its measured value, and section 2 below is
where the two mechanisms separate.

---

## 1. The two objects

R4's §3 concludes, in its own words:

> **Theorem (Moore-ball collapse).** *Let L ≥ 5 and let U be a unitary
> generator on (Z_L)² whose coefficient map is supported inside the
> radius-one Chebyshev ball {−1,0,1}². Then U is monomial.*

and its precheck meets that against a locality threshold — locality
requires L ≥ 4 — to give the admissible set {4}.  **Both halves are
statements about the radius-one ball.**  R4's §2 says so where it
declares the arena ("Two Boolean connectives … each with its own
radius-one ball") and its §3 says so in the statement of the theorem.

PER-L asks the same two questions at a **window width r** that is a free
coordinate rather than a fixed one: locality is R2's criterion applied
to the radius-r neighbourhood ball, and interference is the existence of
a non-monomial unitary supported inside that ball over the same declared
alphabet.  At r = 1 the two objects coincide and the answers coincide.
Above r = 1 they are different objects.

Neither answer transfers to the other, and neither refutes the other.
R4's statement is true of the radius-one object at every L in its swept
range.  PER-L's statement is true of the radius-r object at r ∈ {1, 2, 3}.

## 2. The cell where they diverge: L = 6 at width 2, and L = 7 at width 2

At **L = 6**, both hold at once:

| object | verdict at L = 6 |
|---|---|
| R4's radius-one ball | no non-monomial unitary exists — the Moore-ball collapse, field-free; the size is not admitted |
| PER-L's radius-two ball | an explicit non-monomial unitary exists on an involution-separated pair, verified against R4's own whole-torus criterion; the size is admitted |

The mechanism is visible and is the point of the annotation.  **The
window width decides whether the ball is wide enough to reach halfway
across the torus.**  An involution-separated pair of offsets doubles its
own difference all by itself, and the radius-r ball contains such a pair
exactly when L is even and L ≤ 4r.  At r = 1 that means L ≤ 4; at r = 2
it means L ≤ 8.  The collapse bound is not a property of the lattice; it
is a property of the pair (lattice, window).

At **L = 7** a second mechanism appears, and it is the reason this note
records the section rather than a closed form.  The support
{(0, 0), (0, 1), (0, 2), (0, 5)} lies inside the radius-two ball of
(Z_7)², and every one of its six nonzero differences is realised exactly
twice: it is a (7, 4, 2) perfect difference set.  On it,
c = ½(δ₍₀,₀₎ + δ₍₀,₁₎ − δ₍₀,₂₎ + δ₍₀,₅₎) has every coefficient in R4's
own 25-element alphabet and is a non-monomial unitary — verified by the
periodic autocorrelation and again by the full 49 × 49 matrix identity
U†U = I, 2401 entries, zero mismatches.  **(Z_7)² contains no involution
at all**, so the pair mechanism is not merely absent there; it is
structurally unavailable, and a search built on it is blind to this
witness by construction.  The width-2 section is therefore {6, 7, 8}.

The comparison cell is **L = 4 itself**, where nothing moves: at width 1
the admitted set is exactly {4}, and PER-L re-derives R4's absence half
by a second, counting proof of R4's own ball theorem — the DDS criterion
applied to the nine-offset ball, exhaustive over its subsets.  R4's
uniqueness claim is re-proved, not weakened.

## 3. The corpus-wide caution

**Any claim in this corpus of the form "locality requires L ≥ n" or "the
collapse bound is L ≤ n" is window-scoped unless the window is declared
beside it.**  Both thresholds are joint properties of the lattice and the
neighbourhood radius, and a head string that carries the connective but
not the radius under-determines its own object.

Two further scopings travel with that one, and both are measured in
PER-L:

- **Alphabet.**  Whether a difference-doubled subset of the ball carries
  a non-monomial unitary is decided by the alphabet.  Over the parents'
  25 the order-3 coset inside the radius-three ball at L = 9 carries
  none; over the 19-value probe the corpus already uses at paper-20's
  own rung it carries 54.  Every section in PER-L §7 is a section *over
  the parents' alphabet* and says so.
- **Connective.**  R4 §12 already registered this one: the unique scale
  is a theorem about the declared link set of the record stage, not a
  law of the substrate.  The window is the second coordinate of that
  same species of fact, which is why this is an annotation and not an
  erratum.

## 4. What this note does and does not do

**Does.**  It records that R4's `SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=4;
NON-MONOMIAL-LOCAL-AXIS-ONLY-IF-L<=4)` and the `SCOPE` segment beside it
are **width-1-relative**, and that the head string does not carry the
radius although the body proves both halves at it.  It records that the
R4 §11 and R4b §9 trichotomies — *widen the modulus set / leave the
local class / leave the admitted size* — gain a fourth named branch,
**widen the window**, which sits inside "leave the local class" only
because "local" there means radius-one.  It records the measured
sections at the widths PER-L swept: {4} at width 1, {6, 7, 8} at width
2, {8, 10, 12} at width 3, over the parents' alphabet.

**Does not.**  It does not withdraw anything of R4 or of R4b.  It does
not edit paper-10 or paper-15, which are terminal.  It does not claim
anything about window widths above 3, which PER-L does not sweep, nor
about alphabets other than the ones PER-L declares.  It does not touch
paper-20 or its adjudication note, whose record of what was registered
is itself a datum.

## 5. Provenance

- **PER-L (paper 28), `v14/paper-28-perl.md` §7**, and its instrument
  `v14/code/perl_exact.py`: the gates `G-LOCALITY-WINDOWS`,
  `G-BAND-PAIR-MECHANISM`, `G-BAND-LAW`, `G-BAND-ABSENCE-FORCED`,
  `G-BAND-INJECTIVITY`, `G-SUPPORT-CEILING`,
  `G-L7-DIFFERENCE-SET-WITNESS`, `G-L7-IN-THE-SECTION` and
  `G-ODD-COSET-ALPHABET-RELATIVE`.
- **R4 (paper 10)** at commit 583cae7, §2, §3, §11 and §12; **R4b
  (paper 15)** at commit 6d32993, §4, §6 and §9.
- The panel that produced the annotation: `v14/review-perl-operator.md`
  (the L = 7 witness and the completed census),
  `v14/review-perl-effectus.md` (the register row lifted above and the
  L = 9 alphabet-relative counterexample), `v14/review-perl-instrument.md`.
- The adjudication that ordered it: `v14/note-perl-adjudication.md`,
  ruling 3 and order U15, at v14 ledger #228.
