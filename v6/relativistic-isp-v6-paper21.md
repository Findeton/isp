# Paper 21 (v6) - SHARD: The Generation Problem

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Tier 1b of the candidacy plan.  Two theorems and one forced
prediction.  THE PROTECTION THEOREM: a record family fiber of
dimension g carries a family-invariant mass seam iff g <= 2 (computed
invariant-bilinear dimensions 1, 1, 0, 0 for g = 1..4; the g = 2 seam
is SU(2)'s epsilon, exhibited at 4.5e-16) - so a two-family
replication can be erased by its own ledger and THREE IS THE MINIMAL
PROTECTED REPLICATION.  THE GAUGING THEOREM: by P18's reconstruction a
family fiber is gauge; for g = 3 over the bare SM content the cubic
anomaly can NEVER cancel (the dimension sum 15 is odd), and WITH the
sixteenth Weyl fermion the exhaustive 64-assignment scan leaves
EXACTLY ONE embedding up to conjugation: (Q, L | u^c, d^c, e^c, nu^c).
THE FORCED PREDICTION: under the named hypothesis (F-fiber) -
replication is a record fiber - THE RIGHT-HANDED NEUTRINO MUST EXIST.
Generations are not derived; they are PRICED: protected only in
threes, gaugeable only with nu_R, embedded uniquely
```

## 0. Verdict

```text
THEOREM G1 (protection; p21a, exact nullspace computation).
dim Inv(fund x fund) of the U(g) family code = 1, 1, 0, 0 for
g = 1, 2, 3, 4.  The g = 2 invariant is the epsilon pairing
(pseudo-reality; invariance receipt 4.5e-16): a two-family fiber
carries its own family-singlet mass seam and the replication can be
lifted pairwise.  g = 3 carries NO invariant pairing (3 x 3 = 6 +
3bar): MINIMAL PROTECTED REPLICATION = 3.

THEOREM G2 (gauging; p21b, exhaustive).  A record family fiber is
gauge (P18).  g = 3 over the bare SM content (dims {6,3,3,2,1},
sum 15 odd): NO chirality assignment cancels the SU(3)_H cubic.  With
nu^c (sum 16): exactly 2 of 64 assignments pass both SU(3)_H^3 and
SU(3)_H^2-U(1)_Y - the unique embedding up to conjugation:

    3_H: (Q, L)        3bar_H: (u^c, d^c, e^c, nu^c).

g = 2 contrast: Witten parity also fails at 15 and passes at 16 - but
g = 2 is unprotected by G1.

THE FORCED PREDICTION (conditional, falsifiable).  Named hypothesis
(F-fiber): generation replication is a record degeneracy fiber.  Under
it: g >= 3 (G1), the fiber is gauge (P18), and anomaly freedom FORCES
the sixteenth Weyl fermion: NU_R EXISTS.  16 per generation-stack is
the SO(10)-spinor count - noted as a direction, not a claim.
```

## 1. Method and reproducibility

```text
code/v6_p21a_generation_protection_campaign.py  G1 + the epsilon seam
code/v6_p21b_family_gauging_campaign.py         G2 + the forced nu_R
```

Both scripts rerun bit-identically.  Corpus inputs: P18 (fibers are
gauge; R2/R3), P17/P19 (the content the fiber replicates), p18e (the
predicate machinery).  The invariant dimensions are exact nullspace
computations; the assignment scan is the complete 2^6 enumeration.

## 2. Theorem G1: protection

### 2.1 The question, in record terms

In SHARD a family structure is a degeneracy fiber of dimension g; by
P18's reconstruction it carries a U(g) family code.  A replication is
PROTECTED if no family-invariant fermion mass pairing exists -
otherwise the ledger can seal a mass seam that lifts the copies
pairwise (the replication is "Higgsable away" by its own structure)
and the multiplicity is not structural.  The mass pairing of two
fund-of-U(g) fermions is a bilinear on fund x fund, so protection is
decided by dim Inv(fund x fund).

### 2.2 The theorem and its proof

**Theorem G1.**  dim Inv_{SU(g)}(fund x fund) = 1 for g = 1, 2 and
0 for g >= 3.  Consequently the minimal protected replication is 3.

*Proof.*  fund x fund decomposes as Sym^2 + Lambda^2.  An invariant
bilinear is an invariant vector in the dual; for SU(g), Lambda^2(C^g)
contains the invariant epsilon iff g = 2 (the determinant form needs g
indices), and Sym^2 never contains one for g >= 2; for g = 1 the
product is the trivial character.  Hence 1, 1, 0, 0, ... and a g = 2
fiber carries exactly the epsilon seam: psi_i eps^{ab} psi_j pairs the
two families into a family singlet, liftable by any scalar singlet
weight.  For g >= 3 no family-invariant pairing exists: any mass term
must BREAK the family code, i.e. masses can only arise from family-
breaking seams (the observed structure: generations differ only by
their masses).                                                    QED

Machine receipts: exact nullspace dimensions 1, 1, 0, 0 for
g = 1..4; the epsilon invariance ||U^T eps U - eps|| = 4.5e-16 over
sampled SU(2).

### 2.3 Reading

The record-native answer to "why not two generations": two would not
have survived as structure - the ledger itself supplies the seam that
erases them.  Three is the SMALLEST replication the ledger cannot
erase.  (g = 4 is also protected but larger; minimality, not theorem,
prefers 3 - stated honestly.)

## 3. Theorem G2: gauging the family fiber

### 3.1 Setup

By P18 R3(b), a record degeneracy fiber IS gauge: its U(g) must
satisfy the seam/anomaly predicates like any other factor.  Take
g = 3 (minimal protected) with each SM multiplet assigned to 3_H or
3bar_H of the family SU(3)_H.  The two binding conditions:

```text
   SU(3)_H^3:        sum (+-) dim(multiplet) = 0
   SU(3)_H^2-U(1)_Y: sum (+-) dim(multiplet) Y6(multiplet) = 0
```

(signs +- for 3_H vs 3bar_H; T(fund) = 1/2 common, cancelled).

### 3.2 The theorem

**Theorem G2.**  (a) Over the bare SM content (multiplet dimensions
{6, 3, 3, 2, 1}, total 15) no assignment cancels the cubic: an equal
partition of an odd total is impossible.  (b) With nu^c (dims
{6, 3, 3, 2, 1, 1}, total 16), exactly 2 of the 64 assignments pass
both conditions - the embedding

```text
   3_H: (Q, L)     3bar_H: (u^c, d^c, e^c, nu^c)
```

and its global conjugate.  *Proof of (a)*: parity.  *Proof of (b)*:
complete enumeration (the scan is the proof; the mixed condition
computes as +6 (Q) -(-12) (u^c) -(+6) (d^c) +(-6) (L) -(+6) (e^c)
-(0) (nu^c) = 6 + 12 - 6 - 6 - 6 = 0 for the displayed assignment, and
the scan shows no other sign pattern balances both sums).        QED

### 3.3 Readings

1. **nu_R is FORCED by any gauged family fiber.**  The sixteenth Weyl
   fermion is not optional decoration: without it the family gauge is
   anomalous for g = 3 (cubic, parity) AND for g = 2 (Witten: 15
   doublets is odd).  Under (F-fiber), the right-handed neutrino is a
   structural necessity - the prediction P-nu of the ledger.
2. **The embedding sees the chirality split.**  The unique assignment
   puts the left-handed doublets (Q, L) on one side of the family code
   and the right-handed singlets on the other - the family gauge
   DISTINGUISHES handedness, a structural echo of the SM's own
   left-right asymmetry, delivered by an anomaly scan.
3. **16 = the SO(10) spinor count** - noted as a direction.  The
   forced content per generation-stack is exactly the spinor 16 of
   SO(10); whether the record ontology's fiber towers assemble into a
   unified code is not claimed, only flagged.

## 4. The hypothesis (F-fiber), honestly

What is NOT derived: that replication IS a fiber.  Three identical
copies of the matter ledger could a priori be three separate sectors.
The corpus motivation for (F-fiber): identical replication with NO
distinguishing record is a silent label, and silent labels are
excluded by P4's silent-seam principle (the same mechanism as P18 R2)
- the only record-admissible host for unlabeled multiplicity is a
degeneracy fiber, where the label is gauge.  This argument is stated
as the candidate DERIVATION of (F-fiber) and left at hypothesis status
pending its own campaign; its falsifier is concrete: a three-
generation record model where the replication is demonstrably not a
fiber would show the hypothesis has content and alternatives.

Falsifiability of the chain: if nu_R-less neutrino physics were
established (no sterile state at any scale, pure dim-5 Majorana
only), (F-fiber) dies - the hypothesis carries an experimental kill
switch, which is its value.

## 5. What this paper proves and does not prove

Proves: G1 (Section 2.2, with the g = 2 seam exhibited and the
invariant dimensions computed exactly); G2 (impossibility at 15 by
parity, uniqueness at 16 by exhaustion); the conditional forcing of
nu_R under (F-fiber).

Does not prove: (F-fiber) itself (Section 4: named hypothesis with a
candidate silent-seam derivation and a stated falsifier); g = 3
against g >= 4 beyond minimality; the family-symmetry breaking pattern
(masses split the generations: Paper 23's layer); the SO(10) reading
(direction).

## 6. The kernel after Paper 21

```text
GENERATIONS: PRICED - protected iff g >= 3 (G1); gauge-consistent at
  g = 3 iff nu_R exists, with the unique embedding (G2).
NEW NAMED: (F-fiber) the replication-is-a-fiber hypothesis, now
  carrying a falsifiable consequence (nu_R) and a candidate
  derivation route (silent-seam).
PREDICTION LEDGER (for Paper 25): P-nu: the right-handed neutrino
  exists [conditional on (F-fiber)].
KERNEL otherwise unchanged.
```

## References and literature map

- Papers 4, 17-19 (internal): silent-seam exclusion (P4), the content
  (P17/P19); P18: fibers are gauge.
- E. Witten, Phys. Lett. B 117, 324 (1982): the SU(2) global anomaly
  (the g = 2 parity check).
- H. Georgi, in Particles and Fields (1975); H. Fritzsch and
  P. Minkowski, Ann. Phys. 93, 193 (1975): SO(10) and the 16 (the
  noted direction).
- T. Yanagida; M. Gell-Mann, P. Ramond, R. Slansky (1979): nu_R and
  the seesaw (consumed in Paper 23).
```
