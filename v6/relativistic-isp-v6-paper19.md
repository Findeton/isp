# Paper 19 (v6) - SHARD: Run 2 - The Zoo, and the Floor That Survived

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Tier 0 of the candidacy plan: consolidation.  The Standard-Model floor
survives the representation zoo - with color up to {6, 6bar, 8}, weak
up to the triplet, |Y6| <= 12, and exhaustive enumeration at the floor
region, THE SM GENERATION AND ITS CONJUGATE REMAIN THE ONLY genuinely
chiral anomaly-free contents at 15 Weyl; no exotic color or weak
triplet reaches the floor (the computed cubic cost A(6) = +-7 and the
dimension cost are both prohibitive), and the first competitor is ONE
exotic-hypercharge theory at 16 Weyl and six multiplets.  And a
refutation, in the corpus tradition: the triality-divisibility
conjecture (P17) is FALSE - first counterexample {1,6,9 | 3,3,10} at
total charge 16 - demoting the divisibility to a small-charge
phenomenon while leaving Paper 18's center derivation untouched (it
explained the appearance; it never relied on it)
```

## 0. Verdict

```text
RUN 2 (p19a; exhaustive within caps).  Pool: 75 multiplets (color
{1, 3, 3bar, 6, 6bar, 8} with the p18e-COMPUTED anomaly data; weak
{1, 2, 3}, T(3) = 2, integer isospin exempt from Witten; |Y6| <= 12 on
the Z_6 lattice).  Caps: <= 5 multiplets and <= 16 Weyl (full zoo);
<= 6 multiplets (fundamental/doublet pool).

  full zoo:    EXACTLY TWO contents at/below 16 Weyl - the SM
               generation (15 Weyl) and its conjugate.  NOTHING with
               exotic color or weak triplets reaches the floor.
  6 multiplets (fund/doublet): the first competitor appears - one
               exotic-hypercharge theory (a conjugate pair) at
               16 Weyl, charges to |Y6| = 12:
               (1,1,-6)+(1,1,+12)+(1,2,-3)+(3,2,+1)+(3b,1,-10)+(3b,1,+8).
  THE FLOOR IS CONSOLIDATED: minimal chiral record matter under the
  full small-rep zoo = the Standard Model generation, uniquely.

THE REFUTATION (p19b).  The P17 divisibility observation (all minimal
chiral bases have total charge divisible by 3) is FALSE at scale:
  Q_max =  8:   6 base pairs, 0 counterexamples;
  Q_max = 15:  74 pairs, 18 counterexamples - first:
               {1, 6, 9 | 3, 3, 10}, total 16;
  Q_max = 25: 482 pairs, 156 counterexamples.
The Z_3 closure census was a SMALL-CHARGE phenomenon.  Status of the
center story: UNAFFECTED - Paper 18 derived the Z_3 structure from the
reconstructed group's center, and only EXPLAINED why the small bases
showed it; the conjecture dies, the theorem stands.
```

## 1. Method and reproducibility

```text
code/v6_p19a_zoo_search_campaign.py      run 2: the zoo (pruned DFS,
                                         exhaustive within caps)
code/v6_p19b_divisibility_campaign.py    the divisibility scan
```

Both scripts rerun bit-identically.  Anomaly data for the zoo reps
from p18e (computed from generators); weak-triplet Dynkin index
T(3) = 2 from the spin-1 formula j(j+1)(2j+1)/3.  Caps stated in
place; everything inside them is complete enumeration.

## 2. The search, formally

### 2.1 The candidate space

A multiplet is a triple (c, w, Y6) with c in {1, 3, 3bar, 6, 6bar, 8}
(triality t = 0, 1, 2, 2, 1, 0; cubic coefficient A = 0, +1, -1, +7,
-7, 0; Dynkin T = 0, 1/2, 1/2, 5/2, 5/2, 3), w in {1, 2, 3} (duality
d = 0, 1, 0; Dynkin T_w = 0, 1/2, 2), and Y6 an integer with
|Y6| <= 12 on the Z_6 lattice: 2t + 3d + Y6 = 0 mod 6.  The trivial
multiplet (1, 1, 0) is excluded.  A content is a multiset of
multiplets; its Weyl count is sum of dim(c) x dim(w).

### 2.2 The predicate stack

```text
  SU(3)^3:        sum A(c) dim(w)            = 0
  SU(3)^2-U(1):   sum T(c) dim(w) Y6         = 0
  SU(2)^2-U(1):   sum T(w) dim(c) Y6         = 0
  U(1)^3:         sum dim Y6^3               = 0
  U(1)-grav:      sum dim Y6                 = 0
  WITTEN:         sum over w = 2 multiplets of dim(c)  even
  CHIRALITY:      the content differs from its conjugate
                  ((c, w, Y) -> (cbar, w, -Y))
```

### 2.3 The enumeration

Pruned depth-first search over the dim-sorted pool: a branch is cut
when the remaining Weyl budget (16) cannot accommodate the smallest
available multiplet or the multiplet cap (5 full zoo / 6 restricted)
is reached.  Within the caps the enumeration is COMPLETE - every
claim below is exhaustive, not sampled.  The Weyl cap is justified by
the question: only the FLOOR region matters for minimality; larger
contents cannot compete with a 15-Weyl solution.

## 3. Run 2 results

### 3.1 The full zoo

```text
  pool: 75 multiplets; caps <= 5 multiplets, <= 16 Weyl; EXHAUSTIVE
  genuinely chiral anomaly-free contents found: 2
   15 Weyl: (1,1,+6) + (1,2,-3) + (3,2,+1) + (3b,1,-4) + (3b,1,+2)
            <- THE SM GENERATION
   15 Weyl: the conjugate
```

Why the exotics fail at the floor, mechanically: a single 6 or 6bar
costs A = +-7 in the cubic - cancelling it inside 16 Weyl requires
either seven fundamentals of opposite orientation (dimension cost
already 6 + 21 > 16) or a conjugate exotic pair (vector-like in
color, hence pushed toward overall vector-likeness by the remaining
predicates at this size); the 8 is anomaly-free but costs 8 or 16
Weyl by itself and is self-conjugate in color; weak triplets cost a
factor 3 in every colored dimension.  The cubic cost and the
dimension cost both protect the floor.

### 3.2 The extended fundamental/doublet pool

```text
  caps <= 6 multiplets, <= 16 Weyl: 4 contents = the SM pair plus ONE
  exotic-hypercharge theory (a conjugate pair) at 16 Weyl:
   (1,1,-6) + (1,1,+12) + (1,2,+3->-3 pattern) + (3,2,+1)
   + (3b,1,-10) + (3b,1,+8)  [and conjugate]
```

The first competitor: heavier by one Weyl fermion and two extra
multiplets, with hypercharges to |Y6| = 12 and no exotic color - an
anomaly-free chiral variant of the known exotic-hypercharge family.
Its existence is a feature of the census, not a threat to the floor:
minimality still selects the SM uniquely.

## 4. The divisibility refutation

The P17 observation - every minimal chiral base (size-3 stacks passing
the 2d anomaly predicates) has total charge divisible by 3 - tested by
complete enumeration with (sum, sum-of-squares) bucketing:

```text
  Q_max =  8:    6 chiral base pairs;   0 counterexamples
  Q_max = 15:   74 pairs;  18 counterexamples
                first: L = {1, 6, 9}, R = {3, 3, 10}  (sum 16;
                sum of squares 118 = 118: a valid chiral base)
  Q_max = 25:  482 pairs; 156 counterexamples
```

REFUTED.  The divisibility was a small-charge phenomenon: at charge
bound 8 the solution set is too sparse to reveal the non-divisible
families.  In the corpus tradition (the Triangle Law, the d-reading of
record-SSB), the refutation is recorded as a result: conjectures get
killed in public.  Paper 18's center theorem - closure = center
neutrality, the Z_3 census as the center shadow - is UNAFFECTED: it
derived the structure of the closure predicate, not the divisibility
of base sums, and only explained why the small-charge census LOOKED
triality-locked.

## 5. What this paper proves and does not prove

Proves (exhaustively, at stated caps): the SM-floor uniqueness under
the zoo; the identity and uniqueness of the first competitor (16 Weyl,
exotic hypercharges); the refutation of the divisibility conjecture
with explicit counterexamples; the mechanical reading of why exotic
color cannot reach the floor (Section 3.1).

Does not prove: anything beyond the caps (reps above 8/triplet,
contents above 6 multiplets or 16 Weyl - the floor argument makes
larger contents irrelevant to MINIMALITY, but the full theory space is
of course bigger); dynamical selection of the floor (Tier 2 of the
plan).

## 6. The kernel after Paper 19

```text
(M)-Phase-II-run-2: EXECUTED.  The floor is the SM generation,
   uniquely, under the small-rep zoo; first competitor catalogued
   (16 Weyl, exotic hypercharge).  The divisibility conjecture is
   REFUTED (corpus ledger updated); the center theorem (P18) stands.
KERNEL: unchanged otherwise - { (C-reg-b), (M)-dynamics, (V),
   (PR-RP) } + { O7, O8-remainder, O11-remainder, D10-refinements }.
NEXT (per the candidacy plan): Tier 1 - the record scalar (Paper 20)
   and the generation problem (Paper 21).
```

## References and literature map

- Papers 17-18 (internal): the filter stack, the Z_6 lattice, the
  computed anomaly data, the center derivation.
- B. C. Allanach, B. Gripaios, J. Tooby-Smith, Phys. Rev. Lett. 125,
  161601 (2020): systematic anomaly-free enumerations (context for
  the exotic-hypercharge competitor).
- R. Slansky, Phys. Rep. 79, 1 (1981): representation data
  (cross-check for the zoo's computed coefficients).
```
