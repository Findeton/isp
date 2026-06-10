# Paper 17 (v6) - SHARD: (M) Phase I - The Constrained Inverse Search

Author: Felix Robles Elvira

Subtitle:

```text
The Standard-Model inverse problem, opened as a BOUNDED ENUMERATION.
Phase I runs the theorem-grade filter stack built by Papers 8-16 -
anomaly cancellation (P14), genuine chirality, baryon closure (P8's
w = 3 binding law), generation replication - exhaustively over small
record codes, and returns STRUCTURE THEOREMS, not samples: (1) the
generation predicate FACTORIZES through the anomaly filter (replication
multiplies every anomaly sum by 3), so three-generation chiral record
matter requires base size >= 3 and hence at least 9 + 9 Weyl entries -
zero survivors below that, by complete enumeration at every code
tested; (2) the closure census over all six minimal chiral bases
selects Z_3 as the SMALLEST universally closing code, by the visible
mechanism that every minimal base's total charge is divisible by 3 - a
triality-flavored hint, reported as an observation; (3) the 4d cubic
filter kills everything below FIVE Weyl fields (minimal genuinely
chiral 4d U(1) spectrum: {-9,-5,-1,7,8}), and the classic
{-4,-4,1,1,1,5} appears at size 6 carrying a multiplicity-3
color-shadow.  And the two Standard-Model receipts: one generation in
6Y units passes BOTH record-filter sums EXACTLY (the hypercharge
miracle, machine-verified: sum q = 0, sum q^3 = 0), and every SM Weyl
field satisfies 2t + 3d + Y6 = 0 mod 6 - the faithful gauge code is
the Z_6 QUOTIENT, so the (M) search must target the quotient character
lattice, not the naive product.  Phase II is named and gated: the
nonabelian lift of the multiplicity-3 structure, blocked on D10
```

This paper executes the final item of the standing plan.  (M) was the
named kernel item "which ledgers nature instantiates" (P7 10.4/14.6
item 13); its preconditions - relation-code laws (P8), fermions forced
(P9/P11), the anomaly filter (P14) - are all now theorems, and this is
the first run of the search itself.

## 0. Verdict

```text
THE CANDIDATE SPACE AND THE FILTER STACK.  Candidates: chiral record
spectra (L-stack, R-stack) of code characters with integer charge
lifts; chirality from orientation classes (P9); statistics already
theorem-level (P11).  Filters, each theorem-grade:
  F1 ANOMALY (P14): n_L = n_R, sum q equal, sum q^2 equal (2d screen);
     sum q = 0, sum q^3 = 0 (4d, all-left convention - the cubic is a
     named import, the linear is lattice-grounded by P14).
  F2 GENUINE CHIRALITY: L != R (vector-like content is empty physics).
  F3 BARYON CLOSURE (P8: w = 3 binds): some charge triple sums to zero
     in the code - the ledger admits a bound 3-composite.
  F4 GENERATIONS: the spectrum is 3 identical copies of a base.

RESULT 1 (the factorization theorem; PROVED + verified by exhaustion).
Replication by g multiplies every anomaly sum by g, so an F4 spectrum
passes F1 iff its BASE does; chirality likewise.  With P14's
exhaustion theorem (no chiral base below size 3):

   MINIMAL THREE-GENERATION CHIRAL RECORD MATTER = 9 + 9 WEYL ENTRIES.

Machine: ZERO full-cascade survivors at stack sizes 3 and 6 across all
codes Z_5..Z_12 - complete enumerations (raw spectra up to 213,444 per
code), not samples.  The SM, with base 15 replicated 3x, sits above
the bound, consistently.

RESULT 2 (the closure census; observation at stated scope).  All six
minimal chiral bases (size 3, charges <= 8) baryon-close in Z_3 - and
in Z_4, Z_6, Z_9 - with Z_3 the smallest, by a visible mechanism:
every minimal base's TOTAL charge (9, 12, 12, 15, 15, 18) is divisible
by 3, so the full stack is its own closing triple.  Triality-flavored;
reported as a Phase-I observation, NOT a derivation of color.

RESULT 3 (the 4d filter; complete enumeration |q| <= 9).  The cubic
constraint is far harder than the 2d screen: no genuinely chiral 4d
U(1) spectrum below size 5; the minimal solutions are
{-9,-5,-1,7,8} (size 5; 2 solutions) and at size 6 the classic
{-4,-4,1,1,1,5} family - which carries a charge of multiplicity 3:
the color-shadow structure appears spontaneously among minimal
solutions (2 of 4).

THE STANDARD-MODEL RECEIPTS (machine-verified, exact):
  HYPERCHARGE: one generation, all-left Weyl, 6Y units
    (Q: 6x(+1), u^c: 3x(-4), d^c: 3x(+2), L: 2x(-3), e^c: 1x(+6)):
    sum q = 0 and sum q^3 = 0 EXACTLY - the hypercharge miracle is a
    record-filter receipt, generation by generation (nu^c neutral).
  THE Z_6 QUOTIENT: every SM field satisfies 2t + 3d + Y6 = 0 mod 6
    (t triality, d duality): the faithful gauge code of the Standard
    Model is SU(3) x SU(2) x U(1) / Z_6.  In record terms: THE
    RELATION-CODE CHARACTER LATTICE IS THE QUOTIENT LATTICE - the (M)
    search's true target object, now pinned.

PHASE II, NAMED AND GATED: lift the multiplicity-3 charges to genuine
triality-code (nonabelian) representations, with the closure census as
the selection mechanism - blocked on D10 (nonabelian record
statistics) exactly as P9 anticipated; and the dynamical filters
(binding spectra, P8's laws at scale) once candidates survive the
kinematic stack.
```

## 1. Method and reproducibility

```text
code/v6_p17a_screen_cascade_campaign.py   the 2d cascade, factorization
                                          theorem, closure census
code/v6_p17b_sm_filter_campaign.py        the 4d filter, SM receipts,
                                          Z_6 quotient, structure scan
```

All enumerations are EXHAUSTIVE at their stated scopes (charge bounds,
stack sizes, code orders printed in place); no sampling.  Named
imports: the 4d cubic anomaly condition (the triangle); the SM
hypercharge assignments and the Z_6 global-structure fact (known;
machine-rechecked here as record receipts).  Corpus inputs: the P14
anomaly filter with its lattice-grounded linear predicate and
exhaustion theorem; P8's single-relation binding law (the closure
predicate); P9's orientation-class chirality; P11's statistics
theorem.

## 2. The cascade (p17a)

```text
   N    k   raw spectra   F1 anomaly   F2 chiral   F3 closure   F4 gen
    5   3         400          22          2           2          0
    6   3        1225          37          2           2          0
    8   3        7056          88          4           4          0
   12   3       81796         320         34          24          0
    6   6       44100         282         72          72          0
    7   6      213444         ...        314 (F1-F3)               0
```

Zero three-generation survivors everywhere - and Section 0's
factorization theorem says why: F4 commutes with F1/F2, so the base
must itself be anomaly-free and chiral, impossible below size 3 (P14).
The corollary - minimal three-generation chiral record matter is 9 + 9
Weyl entries - is the first structural prediction of the inverse
search: any SHARD matter sector with generation structure has at least
this complexity.  (A negative result with content, in the corpus
tradition of the Triangle Law refutation.)

## 3. The closure census (p17a)

```text
  base (L | R)              closing codes N <= 12
  {1,4,4} | {2,2,5}         3, 4, 6, 9, 12
  {1,5,6} | {2,3,7}         3, 4, 6, 7, 8, 9, 11, 12
  {2,5,5} | {3,3,6}         3, 4, 5, 6, 9, 12
  {2,6,7} | {3,4,8}         3, 4, 5, 6, 7, 8, 9, 10, 11
  {3,6,6} | {4,4,7}         3, 4, 5, 6, 9, 12
  {4,7,7} | {5,5,8}         3, 4, 5, 6, 7, 9, 12
  census: Z_3 6/6, Z_4 6/6, Z_5 4/6, Z_6 6/6, Z_7 3/6, Z_8 2/6, Z_9 6/6
  stack totals: 9, 12, 12, 15, 15, 18 - all divisible by 3
```

Z_3 is the smallest code closing every minimal chiral base, and the
mechanism is elementary once seen: the minimal bases' total charges
are all multiples of 3.  Whether that divisibility persists at larger
charge bounds is a checkable conjecture (named: the TRIALITY
DIVISIBILITY observation); if it does, the triality code is selected
by anomaly freedom + minimality alone.  Reported at stated scope.

## 4. The 4d filter and the Standard Model (p17b)

```text
size 3, |q| <= 9:  0 genuinely chiral solutions
size 4:            0
size 5:            2   (minimal: {-9,-5,-1,7,8})
size 6:            4   (smallest by charge: {-5,-1,-1,-1,4,4};
                        2 of 4 carry a multiplicity-3 charge)
SM, one generation (6Y):  sum q = 0,  sum q^3 = 0   EXACTLY
Z_6 receipt: 2t + 3d + Y6 = 0 mod 6 for all five field types
```

Three readings:

1. **The 4d stack is the hard one.**  The cubic kills everything below
   five Weyl fields - chiral matter in 4d is structurally expensive,
   and the SM's 15 per generation is not extravagant.
2. **The SM passes the record filters exactly.**  The hypercharge
   miracle (both sums vanishing on the actual assignments) is now a
   corpus receipt; with three generations the factorization theorem
   applies and the sums still vanish.
3. **The target object is the quotient lattice.**  The Z_6 receipt
   pins what "(M) finds the SM" would even mean: the relation code to
   search for is the Z_6 quotient's character lattice, not the naive
   product group - a precise correction to the search specification,
   delivered by a six-line machine check.

## 5. What this paper proves and does not prove

Proves (at stated, exhaustively enumerated scopes): the factorization
theorem and the 9 + 9 minimality corollary; the zero-survivor results
at stack sizes 3 and 6 for all codes tested; the closure census and
its divisibility mechanism; the 4d minimal-size results (nothing below
5; the explicit minimal solutions); the SM hypercharge and Z_6
receipts.

Does not prove: anything about WHICH spectrum nature instantiates
beyond the structural bounds (that is the search's continuing job);
the triality-divisibility observation beyond charge bound 8 (named
conjecture, checkable); the 4d cubic predicate from record data (named
import - the 4d analogue of P14's lattice grounding is open); the
nonabelian lift (Phase II, gated on D10); all dynamical filters
(binding spectra, masses - they need (M)'s dynamic layer and the
calibration contact).

## 6. The kernel after Paper 17

```text
(M)  PHASE I EXECUTED: the search is a bounded enumeration with
     theorem-grade filters.  Structural outputs:
       - minimal chiral base = 3 (P14, used);
       - minimal three-generation chiral content = 9 + 9 (THEOREM);
       - closure census: Z_3 smallest universal closer at minimal
         scope (observation + named divisibility conjecture);
       - 4d minimal chiral size = 5 (exhaustion);
       - the SM target = the Z_6 quotient character lattice (pinned).
     PHASE II (named): nonabelian triality lift - GATED ON D10;
     dynamical filters gated on calibration/(M)-dynamics.
KERNEL: { (C-reg-b), (M)-Phase-II, (V), (PR-RP) } +
        { D10, O7, O8-remainder, O11-remainder }.
[Paper 18 update: THE GATE IS OPEN - D10 discharged (record
     Doplicher-Roberts theorem): statistics = (-1)^(2m) P, gauge
     algebra reconstructed from exchange, and THIS PAPER'S census is
     DERIVED: the closure predicate is center neutrality, the Z_3
     census is the center of the reconstructed group, the
     multiplicity-3 charges lift to U(3) fundamentals with the abelian
     charge on det U(3).  Phase II is posed as a representation
     search.  See Paper 18.]
[Paper 18 Part II update: PHASE II RUN 1 EXECUTED - the nonabelian
     predicates computed from generators, and the exhaustive search at
     fundamental/doublet scope on the Z_6 lattice returns THE STANDARD
     MODEL GENERATION AS THE UNIQUE MINIMAL genuinely chiral
     anomaly-free content (nothing below 15 Weyl, nothing else at 15,
     robust to |Y6| <= 12).  Run 2: higher reps, larger contents, the
     generation/mass layer.  See Paper 18 5.5.]
```

## 7. Status

```text
Cascade:   exhaustive, zero 3-generation survivors below 9 + 9
           (factorization theorem); pruning to 44,100x demonstrated.
Census:    Z_3 universal at minimal scope; totals 9..18 all
           divisible by 3 (mechanism visible; conjecture named).
4d:        minimal chiral size 5 ({-9,-5,-1,7,8}); color-shadow
           multiplicity-3 in 2/4 of size-6 minimals.
SM:        hypercharge receipt exact (0, 0); Z_6 quotient receipt
           exact (all five field types).
Next:      Phase II nonabelian lift (D10-gated); triality-divisibility
           check at larger bounds; 4d lattice grounding of the cubic.
```

## References and literature map

- Papers 8, 9, 11, 14 (internal): the relation-code laws and binding
  (P8), orientation-class chirality (P9), statistics as theorem (P11),
  the anomaly filter, exhaustion theorem, and lattice grounding (P14).
- S. L. Adler; J. S. Bell and R. Jackiw (1969); D. J. Gross and
  R. Jackiw (1972): the 4d anomaly conditions (the cubic import).
- C. Q. Geng and R. E. Marshak, Phys. Rev. D 39, 693 (1989); J. A.
  Minahan, P. Ramond, R. C. Warner, Phys. Rev. D 41, 715 (1990):
  anomaly constraints determining hypercharge - the literature face of
  Section 4's receipt.
- B. C. Allanach, B. Gripaios, J. Tooby-Smith, Phys. Rev. Lett. 125,
  161601 (2020): systematic anomaly-free chiral U(1) enumerations (the
  modern context for the size-5/6 census).
- J. C. Baez and J. Huerta, Bull. AMS 47 (2010); D. Tong, "Line
  operators in the Standard Model," JHEP (2017): the SM's Z_6 global
  structure (Section 4's quotient receipt).
```
