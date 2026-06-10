# Paper 19 (v6) - SHARD: Run 2 - The Zoo, and the Floor That Survived

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

Anomaly data for the zoo reps from p18e (computed from generators);
weak-triplet Dynkin index T(3) = 2 from the spin-1 formula.  Caps
stated in place; everything inside them is complete enumeration.

## 2. What this paper proves and does not prove

Proves (exhaustively, at stated caps): the SM-floor uniqueness under
the zoo; the identity and uniqueness of the first competitor (16 Weyl,
exotic hypercharges); the refutation of the divisibility conjecture
with explicit counterexamples.

Does not prove: anything beyond the caps (reps above 8/triplet,
contents above 6 multiplets or 16 Weyl - the floor argument makes
larger contents irrelevant to MINIMALITY, but the full theory space is
of course bigger); dynamical selection of the floor (Tier 2).

## 3. The kernel after Paper 19

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
- B. C. Allanach, B. Gripaios, J. Tooby-Smith (2020): systematic
  anomaly-free enumerations (context for the exotic-hypercharge
  competitor).
```
