# Paper 20 (v6) - SHARD: The Record Scalar and EWSB

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Tier 1a of the candidacy plan.  A record scalar is a trivial-
projective-fiber excitation (bosonic by Theorem R2, P18) in any gauge
representation - AVAILABLE by construction, so the content is in the
structure: THE HIGGS HYPERCHARGE IS THE MINIMAL LATTICE POINT of the
colorless weak-doublet class (Y6 = 3 mod 6: |Y6| = 3 is the floor);
ONE such doublet serves ALL THREE Yukawa seams (u-, d-, e-type
invariant tensors built explicitly from the record pairings - trace
and epsilon - and verified at 5e-16), and the seam census shows H is
strictly maximal (3 seam pairs; no other small-zoo scalar exceeds 2).
The EWSB mechanism is promoted from Paper 8's honest analogy to a
computed tree-scope mechanism: the lifted vacuum carries exactly three
Goldstone zero modes and m_h^2 = 4 mu^2; the record gauge mass matrix
delivers the W pair, the Z, and a photon whose direction is EXACTLY
the electric charge (Q<phi> = 0 to machine zero, photon overlap
1.0000000000); and m_W/m_Z = cos(theta_W) to 1e-16 across sampled
couplings - the custodial tree structure of the lattice-minimal
doublet.  Loop stability and the dynamical origin of mu^2 < 0 are
NAMED OPENS - the kill condition (sealed positivity obstructing the
scalar seam) DID NOT FIRE
```

## 0. Verdict

```text
AVAILABILITY (theorem-level, from P18 R2): a spin-0 record excitation
has projective sign (+1): eps = +P: bosonic; any gauge rep is
admissible fiber data.  A fundamental record scalar EXISTS in the
ontology; compositeness is not forced.

STRUCTURE (p20a):
  lattice minimality: Y6 = 3 mod 6 for a colorless weak doublet -
    smallest |Y6| = 3 = THE HIGGS HYPERCHARGE (Y = 1/2): nature's
    scalar sits at the lattice floor of its class.
  the three seams: u-type Q x u^c x H (color delta x weak epsilon;
    Y: 1 - 4 + 3 = 0), d-type Q x d^c x H* (delta x delta;
    1 + 2 - 3 = 0), e-type L x e^c x H* (delta; -3 + 6 - 3 = 0):
    explicit invariant tensors, residuals 4.9e-16 / 5.6e-16 under
    sampled gauge action.  ONE doublet serves all three.
  the census: H serves 3 seam pairs of the SM content; the best
    competitor (colored scalars) serves 2: H is strictly maximal -
    the record scalar sector needs exactly one doublet.

MECHANISM (p20b, tree scope):
  vacuum: |<phi>| = sqrt(mu^2/2 lam) (numeric err 2e-9); fluctuation
    spectrum = THREE zeros + m_h^2 = 4 mu^2 exactly.
  gauge masses: eigenvalues {0, mW^2 x2, mZ^2} exact in the record
    normalization (g^2 v^2/8, (g^2+g'^2) v^2/8); the massless
    direction = (g' W3 + g B)/sqrt(g^2+g'^2), overlap 1.0000000000;
    Q = T3 + Y/2 annihilates the vacuum EXACTLY.
  the tree relation: m_W/m_Z = cos(theta_W) to 1e-16 across sampled
    couplings: custodial structure of the doublet, machine-verified.

KILL-CONDITION STATUS: the plan's scalar kill condition (sealed
positivity obstructing the scalar-matter seam) DID NOT FIRE: the
trilinear seam weights are real gauge invariants, admissible at
quadratic record scope.  NAMED OPENS: loop-scope stability of the
record scalar weight; the dynamical origin of mu^2 < 0 (whether the
record RG drives the lifting, P10 machinery); the hierarchy problem in
record terms (why mu << cutoff) - all honest residues, none fatal to
candidacy (they are the SM's own opens).
```

## 1. Method and reproducibility

```text
code/v6_p20a_record_scalar_campaign.py   structure: lattice floor,
                                         seam tensors, census
code/v6_p20b_record_ewsb_campaign.py     mechanism: vacuum, masses,
                                         photon = Q, tree relation
```

Both scripts rerun bit-identically.  Corpus inputs: P18 R2 (bosonic
trivial fiber), the Z_6 lattice (P17/P18), the reconstructed
SU(2) x U(1) fibers.  The Goldstone/Higgs mechanism algebra is
standard (named import at structure level); the receipts verify the
RECORD realization lands on it exactly.

## 2. Availability and lattice minimality

### 2.1 Availability

By Theorem R2 (P18), the statistics of a record excitation is
eps = (-1)^(2m) P: a trivial projective fiber (m = 0) gives eps = +P -
Bose statistics - in ANY gauge representation, since the fiber data
and the projective layer are independent.  A fundamental record scalar
therefore EXISTS in the ontology; whether nature's Higgs is
fundamental or composite is not decided here, but compositeness is not
FORCED, which is what the candidacy plan needed to know.

### 2.2 The lattice floor of the scalar class

The Z_6 quotient lattice (P17 5.3, consumed structurally since P18
Part II) constrains every multiplet by 2t + 3d + Y6 = 0 mod 6.  For a
colorless (t = 0) weak doublet (d = 1): Y6 = -3 = 3 mod 6, so the
allowed hypercharges are Y6 in {..., -9, -3, +3, +9, ...} and the
smallest magnitude is |Y6| = 3, i.e. Y = 1/2: THE HIGGS HYPERCHARGE IS
THE MINIMAL LATTICE POINT OF ITS CLASS.  The observed scalar sits at
the floor of the quotient lattice exactly as the observed fermions sit
at the floor of the chiral filter (P18 Part II/P19) - the same
minimality principle, twice.

## 3. The Yukawa seams

### 3.1 The three invariant tensors

With the SM content (P19 floor) and one doublet H at Y6 = +3, the
gauge-invariant trilinear seams are built from exactly two record
pairings - the color trace delta (3 x 3bar -> 1) and the weak epsilon
(2 x 2 -> 1) or weak delta (2 x 2bar -> 1):

```text
  u-type:  Q (3,2,+1)  x  u^c (3b,1,-4)  x  H   (1,2,+3):
           C_u = delta_(c cbar) x eps_(ab);    Y: 1 - 4 + 3 = 0
  d-type:  Q (3,2,+1)  x  d^c (3b,1,+2)  x  H* (1,2,-3):
           C_d = delta_(c cbar) x delta_(a abar);  Y: 1 + 2 - 3 = 0
  e-type:  L (1,2,-3)  x  e^c (1,1,+6)   x  H* (1,2,-3):
           C_e = delta_(a abar);               Y: -3 + 6 - 3 = 0
```

Machine receipts: the color delta is invariant under 3 x 3bar
(residual 4.9e-16 over sampled SU(3)); the weak epsilon transforms
with det U = 1 under SU(2) (4.9e-16) and the weak delta is invariant
under 2 x 2bar (5.6e-16).  ONE lattice-minimal doublet (and its
conjugate) serves all three seams - the SM's one-Higgs economy is
reproduced, not assumed.

### 3.2 The seam census

For every scalar multiplet in the small zoo ({1, 3, 3bar} x {1, 2},
|Y6| <= 9 on the lattice), count the SM field pairs it can couple to
invariantly (color pairing exists, weak pairing exists, hypercharges
sum to zero with either the scalar or its conjugate):

```text
   scalar (1,2,-3):  3 seam pairs   <- H (and conjugate): MAXIMAL
   scalar (1,2,+3):  3
   best competitors (colored scalars (3,1,-2), (3b,1,+2), (3b,1,+8)):
                     2 seam pairs each
```

H is strictly seam-maximal: no single small-zoo scalar couples to more
SM seam pairs.  The record scalar sector needs exactly one doublet -
and the colored competitors at 2 seams are the leptoquark shadows,
catalogued and not needed.

## 4. The EWSB mechanism at tree scope

### 4.1 The lifted vacuum

The record weight V(phi) = -mu^2 |phi|^2 + lam |phi|^4 on the doublet
(real-field convention, 4 real components): minimization gives
|<phi>| = sqrt(mu^2 / 2 lam) (machine: numeric minimizer agrees to
2.1e-9 at mu^2 = 1.7, lam = 0.9), and the Hessian at the vacuum has
spectrum

```text
   { -1.5e-8, -1.5e-8, -1.5e-8, 6.800000 } = three EXACT zeros (the
   would-be Goldstones) + one massive mode m_h^2 = 4 mu^2 = 6.800000.
```

The three flat directions are the broken-generator orbit; their fate
is the gauge sector's business (4.2).  The dynamical ORIGIN of
mu^2 < 0 - whether the record RG drives the lifting, as P8's analogy
suggested - is the named open (mu-dyn).

### 4.2 The gauge mass matrix and the photon

With <phi> = (0, v)/sqrt(2), couplings (g, g, g, g') on the generators
(T_1, T_2, T_3, Y), the record gauge mass matrix
M^2_ab = (1/2) Re <phi| {g_a T_a, g_b T_b} |phi> has the exact
spectrum (record normalization; ratios convention-free):

```text
   0,   mW^2 = g^2 v^2/8  (x2),   mZ^2 = (g^2 + g'^2) v^2/8.
```

Receipts: eigenvalues {3.5e-18, 0.052812, 0.052812, 0.068125} at
(g, g') = (0.65, 0.35), v = 1; the massless eigenvector overlaps
(g' W_3 + g B)/sqrt(g^2 + g'^2) at 1.0000000000; and the unbroken
charge Q = T_3 + Y/2 annihilates the vacuum EXACTLY (||Q phi|| = 0.0):
THE MASSLESS RECORD DIRECTION IS ELECTROMAGNETISM - derived from the
lattice-minimal doublet's vacuum orientation, not chosen.

### 4.3 The custodial tree relation

Across sampled couplings:

```text
   g = 0.710, g' = 0.408:  m_W/m_Z = 0.86723509 = cos(theta_W) (0.0)
   g = 0.391, g' = 0.417:  0.68374037 = cos(theta_W)   (1.1e-16)
   g = 0.833, g' = 0.583:  0.81936185 = cos(theta_W)   (1.1e-16)
```

m_W/m_Z = cos(theta_W) to machine precision: the custodial tree
structure (rho = 1) of the DOUBLET representation - a triplet scalar
would violate it, so the lattice-minimal choice is also the
custodially safe one, as observed.

## 5. What this paper proves and does not prove

Proves (at stated scope): availability (R2 corollary); the lattice
minimality of the Higgs hypercharge (Section 2.2, an exact lattice
statement); existence and exactness of the three Yukawa seam
invariants with one doublet (4.9e-16/5.6e-16); the seam-census
maximality of H; the tree-scope EWSB spectrum (3 + 1, m_h^2 = 4 mu^2
exact); the exact identification of the unbroken charge with
electromagnetism; the custodial tree relation at 1e-16.

Does not prove: loop-scope stability of the record scalar weight
(loop-H, named); dynamical mu^2 < 0 (mu-dyn, named: the record-RG
lifting question); the hierarchy problem (why mu << cutoff); Yukawa
VALUES (Paper 23's layer); custodial violation patterns beyond tree.
These are the Standard Model's own open problems, hosted - none is a
SHARD-specific obstruction, which is what the kill condition tested.

## 6. The kernel after Paper 20

```text
EWSB: promoted analogy -> computed tree mechanism; H = lattice-minimal
  doublet, seam-maximal; kill condition passed.
NEW NAMED: (mu-dyn) the dynamical origin of the lifting sign;
  (loop-H) loop-scope record scalar stability.
KERNEL otherwise unchanged: { (C-reg-b), (M)-dynamics, (V), (PR-RP) }
  + { O7, O8-remainder, O11-remainder, D10-refinements, mu-dyn,
      loop-H }.
```

## References and literature map

- Papers 8, 17, 18 (internal): the EWSB analogy (now promoted), the
  Z_6 lattice, R2 and the reconstructed fibers.
- P. W. Higgs; F. Englert and R. Brout (1964); S. Weinberg (1967):
  the continuum mechanism (the structure-level import).
- M. Veltman, Nucl. Phys. B 123, 89 (1977); P. Sikivie et al., Nucl.
  Phys. B 173, 189 (1980): custodial symmetry (the tree relation's
  continuum face).
```
