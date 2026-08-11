# PER-L (paper 28) — K1 OPERATOR-LENS HOSTILE REVIEW

*Seat K1 of the panel frozen at v14 ledger #218 (launched at #220).  Object at
commit 9fcc081.  Hashes verified at start and again at the end of the review,
unmoved:*

```
bd0298e2a482  v14/paper-28-perl.md
976d5b9e4ac8  v14/code/perl_exact.py
e4ff37a7a13e  v14/code/perl_output.txt
54ec5a9e9b72  v14/code/perl_receipt.json
973b160d52ed  v14/note-perl-pin.md
```

**GRADE: AWF — ACCEPT WITH FIXES.**

**Recomputations: 741**, all from an instrument built from nothing for this
review.  The field Q(ζ₂₄) is carried in a *different representation* from the
delivered one — an 8-tuple over the basis (1, √2, √3, √6, i, i√2, i√3, i√6)
with integer numerators over a common denominator — so no line of the
delivered arithmetic is reused, and the delivered code was never called as an
oracle.  Scratch at
`…/scratchpad/perl-op/` (`k1field.py`, `t1_stage1.py`, `t2_charp.py`,
`gray_dds.py`, `t4_probe.py`, `t5b.py`, `t6_L7witness.py`, `t7_pool.py`,
`t8_fingerprint.py`, plus a provisioned off-tree mirror).

**Zero false computed numbers outside §7.**  Every number in Stages 1–5 that I
rebuilt came back identical, including the 1,952,424-map total, the 2,940
axis-and-lag objects, the registered 54, the pool triple 58/42/106, the
eigenphase lattice 8/24/8 and all nine b₁ values.  The one place the unit is
wrong is the place it nominated itself: **the band**.

---

## 1. What reproduced exactly

**The DDS theorem (target 1) is sound, and its field-freeness is real.**  I
re-derived it independently.  The proof needs exactly two properties — the
coefficient field has no zero divisors, and the involution is injective — and
both hold in any field with an order-2 (or trivial) automorphism.  The unit
proves it in one line and never exercises it outside characteristic zero, so I
exercised it there: **318 exhaustive full-map scans over F₂, F₃, F₅, F₇, F₁₁,
F₄, F₉, F₂₅ and F₄₉**, with the involution taken as the Frobenius *computed in
the field* and verified to be an order-2 field automorphism (never assumed to
be b ↦ −b, which is false in characteristic 2).  **Zero violations.**  The
theorem holds in F₄, where 1 = −1 and the involution is non-trivial — the
hardest case, and the one the char-0 exercise cannot see.

Two collateral confirmations of the theorem's own commentary: the three-term
stencil {0,a,−a} fails to be DDS-free at exactly orders 2, 3 and 4 (order 2 the
axis is an involution, order 4 its double is, order 3 the stencil is a whole
coset), so 4 is the largest, as §3.3 says; and Sidon ⇒ DDS-free is strict, with
the parents' own stencil as the witness.

**Stage 1 (targets 2, 3) reproduced row for row.**  All eighteen arenas, every
column — Sidon status, DDS-freeness, the full difference-multiplicity profile,
the unitary count and the non-monomial count.  The LINK stencil is Sidon at
every rung with 24 unitary / 0 non-monomial; the four local axes carry
multiplicities [2,2,1,1] at L = 6 and L = 8 and are monomial-only exhaustively;
48 → 0 → 0 on the axis stencil.  Sufficiency 18 of 18; necessity fails at 10;
13 of 18 DDS-free and all monomial-only.  My independent map total is
**1,952,424**, to the unit.

**The control (target 4) reproduced, and its provenance is stronger than the
paper claims.**  Z₃², THIRDS-19, 130,321 maps → 78 unitary → **54
non-monomial**, all on the single support {(1,0),(1,1),(1,2)} — the coset of an
order-3 cyclic subgroup, as stated.  Alphabet relativity confirmed: 0 over the
parents' 25.  Additional finding in the unit's favour: scanning that 3-element
coset *alone* over THIRDS-19 gives **72 unitary / 54 non-monomial**, which is
exactly the "K2's 19-value probe (72/54 axis)" of the paper-20 adjudication's
seat-conflict ruling 2.  So the reproduction is not merely numerically equal to
the registered 54 — it is the same object, and the unit could say so.  The
L = 4 contrast is also right: 48 splits 32 (on {(1,0),(1,1),(1,2)}, which at
L = 4 is *not* a coset) + 16 (on the involution-separated pair
{(1,0),(1,2)}), so "a different mechanism entirely" is accurate.

**Stage 2 (target 6) reproduced from a pool I built myself.**  Axes 9/19/33;
per-axis gauge classes 4 at order 2, 3 at order 3, 9 at order 4, 3 at orders
6 and 8; the gauge acts freely at every rung (every orbit exactly 8).  Pool
**58 / 42 / 106**, and §8's explanation of the non-monotonicity is exactly
right — I confirmed the identity pool = Σ(per-axis classes) − (axes − 1) at all
three rungs (66−8, 60−18, 138−32).  Non-monomial families 42/6/42; local
non-monomial 24/0/0; static 1/1/1; cells 928/1512/6784; velocity cells
1856/3024/13568.  **VMAX = 2, 3, 4 = diameter = L/2**, attained.  Interior
radii 1, 2, 3.  Eigenphase lattice **8, 24, 8 = lcm(8, L)**, with zero
off-lattice eigenvalues at every rung.  Dispersion separates families 58/58,
42/42, 106/106.  Non-integer-velocity families 0 / 6 / 0, and the witness is
**axis [0,3] of order 2 at speed −3/2** — identical to the delivered witness.
I also verified the mechanism by hand: the two-term generator on an order-2
axis has symbol ζ₈^{±1} alternating with the parity of k, a quarter-turn per
momentum step, so v = −L/4, non-integer exactly when 4 ∤ L.

**Stage 3 (target 7) reproduced on all 64 antidiagonal coins.**  The coin
family is 640 = 64 + 64 + 512 with nothing left over and no lattice size
entering.  All eighteen rung-and-stencil rows identical at all three rungs,
with the set-equality certificate (containment in the product of alternating
groups on the orbits *plus* equal cardinality, evaluated per object) passing
everywhere: S1-ONE 3/3, S2-EDGE 60/5, S2-CORNER 9/6 as 3+3, S2-APART 9/6 as
3+3, S3-ROW 2520/7, S4-BLOCK 20160/8.  Global support 16/36/64 = the volume,
one orbit, every plaquette holonomy a 3-cycle.  Parity strata are perfect
matchings at every rung.

**Stage 4 (target 8) reproduced, all nine rows.**  Neighbours, offsets,
completeness, locality and every b₁ (49, 105, 109, 397, 595, 193, 705, 1473,
1953).  The join holds: locality-admitting widths 1/2/3 = interior radii
1/2/3.  The paper is right that this is an identity rather than a coincidence
— both count {1, …, L/2 − 1} — and it says so.

**Stage 5 (target 9): all 24 rows and all 72 cells check, and the tally
11 persist / 5 break / 8 transform is right.**

**Instrument surface (target 10).**  Ten sources, 38 path-value anchors, 9
verbatim windows, 48 mutants, 60 gate-ledger rows — all counted from the source
and matching the prose.  I re-verified all **9 verbatim windows against their
sources with my own normaliser** (whitespace + markdown-prefix): 9 of 9
verbatim, all above the declared 60-character floor.  The off-tree claim holds:
in a provisioned mirror with no version control the plain run exits 0 and
writes artifacts **byte-identical** to the committed ones (e4ff37a7a13e and
54ec5a9e9b72).  Two mutants of my own devising, outside the declared registry,
applied to the source and run out of process:

| mutant | perturbation | outcome |
|---|---|---|
| MUT-K1-A | band's predicted formula `4r` → `4r+2` | exit 1 at **G-BAND-LAW**, artifacts untouched |
| MUT-K1-B | DDS predicate `k>=2` → `k>=3` | exit 1 at **G-DDS-CRITERION-SOUND**, artifacts untouched |

**Numeral sweep**: 76 distinct numerals, 718 occurrences.  Every measurement
numeral is accounted for by a recomputation above; the residue is provenance
references (#91, #119, #125, #148, #196, E-22/23/24, paper numbers), which are
outside my lens.

---

## 2. MAJOR-1 — THE BAND IS FALSIFIED AT WIDTH 2, INSIDE THE DECLARED ALPHABET

§9 says: *"A reviewer who wants to break this unit should attack there first:
exhibit a size outside the predicted band at width 2 carrying a local
non-monomial unitary."*  Done.

**L = 7 at window width 2 is admitted, over the parents' own 25-element
alphabet.**

- Locality holds: the radius-2 ball is 25 sites of 49, so 24 neighbours against
  48 nonzero offsets — not complete.
- The support S = {(0,0), (0,1), (0,2), (0,5)} lies inside the radius-2 ball
  (Chebyshev norms 0, 1, 2, 2).
- S is difference-doubled: all six nonzero differences realised exactly twice.
  It is a (7,4,2) difference set — the complement of the Fano/Singer (7,3,1)
  set — and it is *not* an involution-separated pair, which is why the unit's
  witness search cannot see it (Z₇² has no involution at all).
- **c = ½(δ₍₀,₀₎ + δ₍₀,₁₎ − δ₍₀,₂₎ + δ₍₀,₅₎)**, every coefficient ζ₈^t/2 and
  therefore in the declared alphabet, is unitary and non-monomial.  There are
  8 such maps on that support.

Verified three ways: the periodic autocorrelation is a delta (A(0) = 1, all six
realised lags 0); the **full 49 × 49 matrix satisfies U†U = I exactly, 2401
entries checked, 0 mismatches**; and the offsets/locality conditions above.

Consequence: the admitted set at width 2 is **[6, 7, 8]**, not [6, 8].  The
falsified sentences are

- the verdict clause `ADMITTED-SIZES-AT-WIDTH-r-ARE-THE-EVEN-L-IN-[2r+2,4r]`
  and `WIDTH-2={6,8}` — a set equality, and false;
- §7 table row `| 2 | [6, 8] | [6, 8] |`, and §7's *"at window width 2 it is
  [6, 8]"*;
- the abstract's *"the two sizes the pin sent this unit to visit are exactly
  the two the next window admits"* — the next window admits three sizes;
- the §8 persistence row *"the window widths at which this size is admitted"*
  is unaffected for L ∈ {4,6,8} but is derived from a law that is now wrong.

**Why the gate could not catch it.**  `band_witness` calls `doubled_pair`,
which returns only pairs whose difference is an involution.  The `admitted` set
is therefore *the set of sizes carrying that one mechanism*, and `predicted` is
the closed form of that same mechanism's existence condition (L even, L ≤ 4r,
plus locality).  `G-BAND-LAW` compares the two and cannot fail for
mathematical reasons — MUT-K1-A shows it fires only when the closed form is
edited away from its own antecedent.  §7's prose is careful enough to say
"the cheapest one is a pair of offsets differing by an involution", but the
table column is headed "admitted sizes" and the verdict says "ARE".

**REPAIR (exact).**  Three options, in decreasing order of ambition.

1. *Adopt the closed census* (recommended — see MINOR-1, it is cheap and total):
   publish admitted = [4] / [6, 7, 8] / [8, 10, 12] over the declared alphabet,
   with the L = 7 witness above as a second constructive row, and restate the
   law as: **L is admitted at width r iff L ≥ 2r+2 and the radius-r ball
   carries a difference-doubled subset realised over the alphabet; two
   mechanisms occur in the declared sweep — an involution-separated pair (even
   L ≤ 4r) and a perfect quadruple (L = 7 at r = 2).**  The headline survives
   in its important part: the parent's unique size is still the width-1
   section, and the width-1 row is still exactly [4].
2. *Demote to a presence band*: rename the column "sizes with a constructive
   witness", change "ARE" to "INCLUDE" in the verdict, and delete the
   "exactly the two" sentence from the abstract.
3. At minimum, stamp the law `INVOLUTION-PAIR-MECHANISM-ONLY` everywhere it
   appears.

The §7 hedge (*"the complement is declared open, not claimed"*) protects the
paper's honesty at the paragraph level — it names precisely the risk that
materialised — but it does not protect the set equality asserted in the verdict,
the table and the abstract.

---

## 3. MAJOR-2 — THE BAND LAW IS ALSO ALPHABET-RELATIVE, AND UNSTAMPED

The unit makes a great deal, correctly, of the control's alphabet relativity
(§3.4: *"The count is alphabet-relative … The verdict carries the disclosure
rather than the bare 54"*), and §3.3 states plainly that the order-3 emptiness
is *"alphabet-relative … and not structural"*.  The band law's **evenness
clause rests on exactly that alphabet-relative emptiness**, and carries no such
stamp.

Measured: an order-3 coset fits inside the radius-r ball iff 3 | L and L ≤ 3r.
Crossed with locality (L ≥ 2r+2) that lands on exactly one size in the declared
sweep — **L = 9 at width 3** — where the coset {(0,0), (3,0), (6,0)} sits in
the radius-3 ball (norms 0, 3, 3) and locality holds (49 of 81).  On that
support:

| alphabet | maps | unitary | non-monomial |
|---|---|---|---|
| R4-25 | 15625 | 24 | 0 |
| UNIT-7 | 343 | 18 | 0 |
| THIRDS-19 | 6859 | 72 | **54** |

So over **the unit's own THIRDS-19 probe**, L = 9 is admitted at width 3 and
the even-L law fails again.  (Sharper still: over THIRDS-19 the involution-pair
witness does not exist at all — no two of its squared moduli {1/9, 4/9, 1} sum
to 1 — so the width-3 admitted set over THIRDS-19 is disjoint from the
predicted [8, 10, 12].)

**REPAIR.**  Give the SCALE clause the same disclosure the CONTROL clause
already has: the evenness of the band is a joint property of the ball *and the
alphabet*; over the parents' 25 the order-3 mechanism is empty (§3.3's own
row), and over the 19-value probe this unit runs at the control rung it is not.
One sentence in §7 and one stamp in the verdict.

---

## 4. MINORS

**MINOR-1 — the absence half is forced at *every* width, not only width 1; the
unit underclaims, and closing it is what produces MAJOR-1.**  Two closures the
unit lacked, both cheap:

*(a) The injectivity theorem.*  Lift the radius-r ball to {−r..r}² ⊂ Z².  Two
lifted differences lie in {−2r..2r}² and are congruent mod L only if they
differ by L·e with |L·e_i| ≤ 4r, so **e = 0 whenever L ≥ 4r+1**; then the
extremal difference under a functional injective on the lifted difference box
is realised by exactly one ordered pair, so the ball is DDS-free and every
local map is monomial.  This closes every size above 4r at every width.
Checked exhaustively at r = 1 (2⁹ subsets, all L ∈ [3,14]) and r = 2 (full 2²⁵
Gray-code subset census at L = 9 and L = 10): DDS-free, no exceptions.

*(b) The support-size ceiling.*  The declared alphabet has |c|² ∈ {1/4, 1/2, 1},
so a unitary map's squared moduli sum to 1 with **at most four nonzero
coefficients**, with the profile forced (|S| = 2 → (½,½); |S| = 3 →
(½,¼,¼); |S| = 4 → (¼,¼,¼,¼)).  Combined with the DDS theorem this makes the
whole band question a finite census over subsets of size 2, 3, 4 of the ball —
which I ran to completion at all three declared widths and all thirteen
declared sizes.  Result: [4] / [6, 7, 8] / [8, 10, 12].  The |S| = 4 case
reduces further to a vanishing sum of 8th roots of unity, which vanishes iff
the exponent multiset pairs e with e+4.

After (a) and (b) nothing in the declared sweep is open, and §11's
DECLARED-WINDOW deviation for the band can be retired.  (Note the true residue
before these closures was tiny — only L = 7 at r = 2 and L = 9, 11 at r = 3 —
and the counterexample was sitting in it.)

*Datum for the register:* the L = 7 radius-2 ball is **not** DDS-free — the
full 2²⁵ census finds 6,704,152 difference-doubled subsets — so the "ball too
large for that census" worry was well founded; it is the alphabet, not the
combinatorics, that makes the census finite.

**MINOR-2 — `G-PARTITION-COROLLARY` is inert.**  `blockwise_components`
hard-codes `"complete": True` and computes `"drawn"` and `"possible"` as the
same expression `n(n−1)/2`; no adjacency is ever evaluated.  So
`ok = all(c["complete"] …)` is unconditionally true and the gate cannot fail
for any reason of fact — its only falsifier, `MUT-PARTITION`, flips the
boolean directly rather than perturbing an object, which is the shape E-23 was
bought to catch.  §6's *"is run as the control … is clique-only at every rung"*
reports an assertion as a measurement, and the receipt publishes drawn/possible
pairs that a reader would take as evidence.  The underlying claim is *true* —
cells of a partition do not overlap, so each component is its own cell and is a
clique — which is why this is MINOR.  **Repair:** either compute the cell
adjacency honestly (check every pair of a cell shares a chart, and that no pair
across cells does) or restate §6 as a cited theorem and mark the gate
STRUCTURAL rather than falsifiable.

**MINOR-3 — "the first counterexample is L = 6 AXIS-0-1" is
enumeration-order-relative.**  All four local axes at L = 6 are non-Sidon,
DDS-free and monomial-only *simultaneously*; "first" names the head of the
declared arena list and nothing more.  **Repair:** say "at L = 6, on every one
of the four local axes", or stamp the ordering.

**MINOR-4 — "over any field closed under conjugation" is a category slip.**  A
field is not closed under conjugation; what is needed is a field *equipped with
an involution* (possibly trivial).  The theorem is correct as intended, and I
have now exercised it in nine positive-characteristic fields (see §1), which
the unit never does.  **Repair:** change the phrase to "over any field with an
involution (the trivial involution included)", and — recommended — cite the
char-p exercise, since "field-free" currently rests on a proof read only in
characteristic 0.

**MINOR-5 — the interior-radius "confirmation" is thinner than the verdict
sounds.**  R4b's own published table already carries the L = 6 and L = 8 rows
(interior radii 2 and 3, alongside L = 10 and 12), and the quantity is the
count of radius classes strictly between 0 and ⌊L/2⌋, i.e. L/2 − 1 — a fact
about the torus that no pool enters.  The paper is honest in §4 ("anchored at
its receipt and now measured"), but
`THE-3-AT-L-8-REGISTER-CLAIM-CONFIRMED` in the verdict reads as an independent
test of a live claim.  **Repair:** one clause noting the parameter is
L/2 − 1 by inspection and that R4b's table already exhibited it.

---

## 5. What I could not break

The Sidon head itself.  `PERL-SIDON-SUFFICIENT-NOT-NECESSARY` is correct on
every leg I could reach: sufficiency at 18 of 18, necessity failing at 10, the
replacement theorem true and genuinely field-free, the control reproduced and
correctly disclosed as alphabet-relative, and the whole of Stages 2–5 exact.
Five of the verdict's eight segments (SIDON, CONTROL, LAW, VMAX/INTERIOR,
FINGERPRINT) I recomputed end to end and would sign.  BREAKS and TABLE follow
from those.  **SCALE is the one that must move.**

The unit told the panel where to attack and the attack succeeded there and
nowhere else, which is the best evidence I can offer that the rest is solid.
