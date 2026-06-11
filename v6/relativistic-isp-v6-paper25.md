# Paper 25 (v6) - SHARD: Calibration and the Prediction Ledger

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

> **CORRECTION/UPDATE NOTE (2026-06-11, publishable-campaign
> review).**  (1) The neutrino-step registration (P28-era) was
> rebuilt twice; FINAL FORM: the registered content is the
> UNDRESSED SPECTRUM POINT m1:m2:m3 = eps:sqrt(eps):1 (S_nu =
> 0.17556); the band and the free-coefficient exponent forms are
> withdrawn (the 68% coefficient spread covers the whole exponent
> axis - zero discriminating power); EXPECTED OUTCOME at current
> centrals: ~5.6 sigma JUNO exclusion - the claim is expected to
> die, pre-committed (v6/publishable/paper-VII; external
> registration file, CORRECTION 2).  (2) P-Maj's consequence
> "0nbb at some level" is NOT by itself a falsifier (no rate
> floor); the row's operative falsifier remains "Dirac-only
> neutrinos established."  (3) P-Z6 scope: a confirmed
> millicharged particle kills the Z6 quotient DERIVATION, not the
> record ontology (alternative-seal worlds survive) - stated so
> the falsifier does not appear to cover more than it does.

Subtitle:

```text
The endgame of the candidacy plan.  The operator ledger of the
reconstructed content, enumerated and receipted: the only dimension-3
entry is the Majorana nu^c nu^c (P23's theorem); dimension 4 holds
exactly the three Yukawas plus the Dirac-neutrino seam; dimension 5 is
the Weinberg operator; baryon violation first enters at dimension 6
and EVERY channel conserves B - L.  Five falsifiable predictions
follow: P-nu (nu_R exists, conditional on the family fiber), P-Maj
(Majorana neutrinos, 0nbb != 0), P-BL (proton decay in B-L-conserving
channels only; n-nbar doubly suppressed), P-eps (hierarchy steps are
powers of eps_record = 0.0318, currently 9/9), P-mass (every charged
mass proportional to v).  The candidacy table assembles the arc:
gauge group an OUTPUT, matter content a UNIQUE FLOOR, hypercharges
FORCED, one lattice-minimal scalar, generations PRICED at three,
signs PASSED, masses PROTECTED, gravity and quantum mechanics the
original corpus - conditional on two bounded mathematical residues
and one external calibration measurement.  VERDICT: SHARD IS A
CANDIDATE ROUTE TOWARD THE STANDARD MODEL, with every clause of that
sentence carrying a theorem, an exhaustive enumeration, or a machine
receipt, and every kill condition on record as tested and passed
```

## 0. Verdict

```text
THE OPERATOR LEDGER (p25a; hypercharge sums exact, color epsilon
invariance 8.9e-16):
  dim 3:  nu^c nu^c                 (dB, dL) = (0, -2)   Majorana
  dim 4:  Q u^c H, Q d^c H*, L e^c H*, L nu^c H   (0,0)  the seams
  dim 5:  (L H)(L H)                (0, -2)   light Majorana channel
  dim 6:  QQQL, u^c u^c d^c e^c, u^c d^c d^c nu^c  (+-1, +-1)
          ALL WITH B - L = 0.
Readings: lepton number is broken only by the Majorana sector (by two
units); baryon number only at dimension 6 with B - L exact; the
neutrino has both Dirac and Majorana channels - the seesaw is complete.

THE PREDICTIONS:
  P-nu    nu_R exists                    [conditional: (F-fiber), P21]
  P-Maj   Majorana neutrinos; 0nbb != 0  [M1 + Weinberg channel]
  P-BL    B-violation conserves B - L: p -> e+ pi0 class allowed
          (suppressed by the record cutoff squared); n-nbar needs
          dim 9: doubly suppressed       [the ledger]
  P-eps   hierarchy steps are powers of eps_record = 0.0318 within
          [eps^2, sqrt(eps)]             [pattern claim: 9/9, P23]
  P-mass  every charged fermion mass proportional to v   [M1]
Each row names its falsifier (Section 3).

VERDICT.  At stated scopes, conditional on two bounded mathematical
residues ((C-reg-b) equivalence, multi-letter Anderson) and one
external measurement: SHARD IS A CANDIDATE ROUTE TOWARD THE STANDARD
MODEL.  What "candidate" means here, precisely: the framework HOSTS
the SM's structure with no contradiction at any tested point, OUTPUTS
several of its inputs (gauge group, hypercharges, content floor, the
neutrino's special status), and carries five falsifiable rows.  What
it does not mean: no dynamical derivation of the generation count,
textures, or any dimensionful number is claimed - those are the SM's
own opens, hosted, plus the corpus' named residues.
```

## 1. Method and reproducibility

```text
code/v6_p25a_prediction_ledger_campaign.py   the ledger, predictions,
                                             and assembly
```

The script reruns bit-identically.  All operator rows carry machine
receipts (hypercharge sums, epsilon invariance, weak contractions via
P20); the assembly table cites its papers row by row.

## 2. The operator ledger

### 2.1 The bookkeeping

Every gauge-invariant operator of the SM + nu_R + H content at low
dimension, with its exact quantum numbers (machine: hypercharge sums;
color-epsilon SU(3) invariance at 8.9e-16; weak contractions per P20):

```text
   operator             dim   sum Y6   dB   dL   B-L   role
   nu^c nu^c            3       0      0    -2    +2   Majorana (M1)
   Q u^c H              4       0      0     0     0   u-Yukawa
   Q d^c H*             4       0      0     0     0   d-Yukawa
   L e^c H*             4       0      0     0     0   e-Yukawa
   L nu^c H             4       0      0     0     0   Dirac-nu
   (L H)(L H)           5       0      0    -2    +2   Weinberg
   Q Q Q L              6       0     +1    +1     0   proton decay
   u^c u^c d^c e^c      6       0     -1    -1     0   proton decay
   u^c d^c d^c nu^c     6       0     -1    -1     0   proton decay
```

### 2.2 Readings

1. Lepton number is broken ONLY by the Majorana sector, by two units
   - the dim-3 term M1 made unique, and its dim-5 (Weinberg) light
   shadow.  The neutrino has both Dirac (dim-4) and Majorana channels:
   the seesaw is COMPLETE within the lattice-allowed operator set.
2. Baryon number is exact through dimension 5 and first violated at
   dimension 6 - and EVERY dim-6 channel conserves B - L (the color
   epsilon forces three quark fields, the lattice forces the fourth
   field's hypercharge into the lepton sector).  B - L violation in
   the baryon sector requires dimension 9: doubly cutoff-suppressed.
3. With calibration absent, RATES are not predicted - the cutoff
   scale is the one external dimensionful contact (Section 4) - but
   CHANNEL STRUCTURE is, and channel structure is falsifiable.

## 3. The predictions, with falsifiers

```text
P-nu   nu_R exists (the 16th Weyl).  [Conditional on (F-fiber), P21.]
       FALSIFIER: established nu_R-less neutrino physics (no sterile
       state at any scale) kills P-nu and (F-fiber) with it.
P-Maj  Neutrinos are Majorana; neutrinoless double-beta decay is
       nonzero.  [M1 is unconditional given the content; the Weinberg
       channel exists.]  FALSIFIER: Dirac-only neutrinos established
       (0nbb excluded through the full mass-ordering bands).
P-BL   All baryon violation conserves B - L: p -> e+ pi0 class
       allowed at dim-6/Lambda^2; n-nbar oscillation and B-L-violating
       decay channels doubly suppressed (dim 9).  FALSIFIER: observed
       B-L-violating nucleon decay or n-nbar oscillation at rates
       implying low-dimension operators.
P-eps  Fermion hierarchy steps are powers of eps_record = 0.0318
       within [eps^2, sqrt(eps)] up to O(1).  [Pattern claim: 9/9
       observed steps comply, P23.]  FALSIFIER: any established
       fermion mass ratio step far outside the band.
P-mass Every charged fermion mass is proportional to v.  [M1.]
       FALSIFIER: a charged fermion mass component not tracking the
       Higgs vacuum (precision Higgs-coupling deviations of the
       wrong, non-proportional form).
```

Noted directions, NOT ledger rows: the strong-CP status (the record
gauge measures constructed in this corpus are reflection-positive,
hence carry real positive weights at construction scope - suggesting
theta = 0 structurally; whether theta stays zero under full matter
coupling is open, so it is a direction); dark energy (the corpus' old
(V)/C4 direction: Lambda as sealed-packet state data permits w(z)
drift - distinguishable in principle, no value predicted); dark
matter (nothing forced; sterile nu_R is hosted, not selected).

## 4. The calibration requirement

The corpus' own gauge theorems (P6.1: A_rec is gauge; all geometric
statements dimensionless) imply that exactly ONE dimensionful contact
- a measurement, not a theorem - converts the structure into numbers:
fixing the record scale against any one measured quantity (G in SI
units, a fermion mass in GeV, the cutoff against a decay bound) prices
every other dimensionful claim.  Until that contact: channel
structures, ratios, and pattern claims are the falsifiable content
(Section 3); after it: rates and absolute masses join the ledger.
This is stated as a feature of the discipline, not an apology: the
theory declares precisely where its one external number lives.

## 5. The candidacy table

```text
  gauge group      OUTPUT - reconstructed from exchange        (P18)
  matter content   UNIQUE minimal chiral floor = the SM     (P17-19)
  hypercharges     FORCED - anomalies + the Z_6 lattice     (P14-18)
  scalar sector    one doublet, lattice-minimal, seam-maximal  (P20)
  EWSB             tree mechanism exact; photon = Q exactly    (P20)
  generations      protected iff >= 3; gauged fiber forces nu_R (P21)
  QCD/QED signs    necessity + flow direction + condensate     (P22)
  masses           protected except nu^c; structural seesaw    (P23)
  hierarchy        grain = eps_record (pattern)                (P23)
  gravity + QM     the original corpus                       (P4-16)
  continuum        CONDITIONAL: (C-reg-b) detector-posed;
                   (PR-RP+) evidenced - both bounded           (P24)
  calibration      EXTERNAL: one dimensionful measurement
                   (the corpus' own gauge theorems say so)

KILL-CONDITION SCOREBOARD: wrong sign - PASSED (P22); scalar seam
obstruction - PASSED (P20); exotic floor flood - PASSED (P19);
(PR-RP) negative - NOT OBSERVED (evidenced positive, P24).
```

## 6. What this paper proves and does not prove

Proves/receipts: the operator ledger at the listed dimensions with
exact quantum-number bookkeeping; the B - L structure of the dim-6
sector; the five predictions as stated consequences of proved
structure (with their conditions and falsifiers named).

Does not prove: operator coefficients (calibration-dependent); proton
lifetime values; the strong-CP status (direction, not row); anything
about (V) beyond the direction note; the two bounded mathematical
residues (P24's named theorems).

## 7. The kernel after Paper 25 - the program's state

```text
KERNEL: { (C-reg-b) [detector-posed], (PR-RP+) [evidenced], (V),
          calibration [external] }
        + { O7-remainder, O8-remainder, O11-remainder,
            D10-refinements, mu-dyn, loop-H, (F-fiber) }.
Every law-side item is a precise classical statement or a named
hypothesis with falsifiable consequences.  The route from indivisible
stochastic processes to a Standard-Model candidate is, at stated
scopes, COMPLETE AS A CHAIN: records -> quantum kinematics -> Lorentz
signature -> gravity -> reflection positivity -> fermions -> gauge
group -> matter content -> EWSB -> masses -> predictions.
```

## References and literature map

- Papers 4-24 (internal): the chain.
- S. Weinberg, Phys. Rev. Lett. 43, 1566 (1979): the dim-5/6 operator
  classification (the ledger's continuum frame).
- W. J. Marciano; P. Nath and P. Fileviez Perez (reviews): proton
  decay channels and B - L (the P-BL frame).
- Particle Data Group: the mass ratios quoted at order of magnitude
  in P-eps.
```
