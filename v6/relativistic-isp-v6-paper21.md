# Paper 21 (v6) - SHARD: The Generation Problem

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
3bar): MINIMAL PROTECTED REPLICATION = 3.  The record-native answer to
"why not two generations": two would not have survived as structure.

THEOREM G2 (gauging; p21b, exhaustive).  A record family fiber is
gauge (P18).  g = 3 over the bare SM content (dims {6,3,3,2,1},
sum 15 odd): NO chirality assignment cancels the SU(3)_H cubic.  With
nu^c (sum 16): exactly 2 of 64 assignments pass both SU(3)_H^3 and
SU(3)_H^2-U(1)_Y - the unique embedding up to conjugation:

    3_H: (Q, L)        3bar_H: (u^c, d^c, e^c, nu^c)

(left-handed doublets vs right-handed singlets: the family code SEES
the chirality split).  g = 2 contrast: Witten parity also fails at 15
and passes at 16 - but g = 2 is unprotected by G1.

THE FORCED PREDICTION (conditional, falsifiable).  Named hypothesis
(F-fiber): generation replication is a record degeneracy fiber.  Under
it: g >= 3 (G1), the fiber is gauge (P18), and anomaly freedom FORCES
the sixteenth Weyl fermion: NU_R EXISTS.  16 per generation-stack is
the SO(10)-spinor count - noted as a direction, not a claim.  If
nu_R-less neutrino physics were established (pure Majorana from
dim-5 only, no sterile state at any scale), (F-fiber) dies - the
hypothesis is falsifiable, which is its value.
```

## 1. Method and reproducibility

```text
code/v6_p21a_generation_protection_campaign.py  G1 + the epsilon seam
code/v6_p21b_family_gauging_campaign.py         G2 + the forced nu_R
```

Corpus inputs: P18 (fibers are gauge; R2/R3), P17/P19 (the content the
fiber replicates), p18e (the predicate machinery).  The invariant
dimensions are exact nullspace computations; the assignment scan is
the complete 2^6 enumeration.

## 2. What this paper proves and does not prove

Proves: G1 (with the g = 2 seam exhibited); G2 (impossibility at 15,
uniqueness at 16, by exhaustion); the conditional forcing of nu_R
under (F-fiber).

Does not prove: (F-fiber) itself - that replication IS a fiber is the
named hypothesis, motivated by the corpus' fiber ontology but not
derived; g = 3 against g >= 4 beyond minimality (a four-family fiber
is protected and gaugeable with suitable content - economy, not
theorem, picks 3); the family-symmetry breaking pattern (masses split
the generations: Paper 23's layer); the SO(10) reading (direction).

## 3. The kernel after Paper 21

```text
GENERATIONS: PRICED - protected iff g >= 3 (G1); gauge-consistent at
  g = 3 iff nu_R exists, with the unique embedding (G2).
NEW NAMED: (F-fiber) the replication-is-a-fiber hypothesis, now
  carrying a falsifiable consequence (nu_R).
PREDICTION LEDGER (for Paper 25): P-nu: the right-handed neutrino
  exists [conditional on (F-fiber)].
KERNEL otherwise unchanged.
```

## References and literature map

- Papers 17-19 (internal): the content; P18: fibers are gauge.
- E. Witten, Phys. Lett. B 117, 324 (1982): the SU(2) global anomaly
  (the g = 2 parity check).
- H. Georgi, in Particles and Fields (1975); H. Fritzsch and
  P. Minkowski, Ann. Phys. 93, 193 (1975): SO(10) and the 16 (the
  noted direction).
- T. Yanagida; M. Gell-Mann, P. Ramond, R. Slansky (1979): nu_R and
  the seesaw (consumed in Paper 23).
```
