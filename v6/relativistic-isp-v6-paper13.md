# Paper 13 (v6) - SHARD: The Horizon Campaign

Author: Felix Robles Elvira

Subtitle:

```text
Record horizons from the lapse-degeneracy locus: the two tools Paper 12
built (the operational lapse and the boundary-record classification)
fused with the corpus' thermality theorems.  The lapse operator is
EXACTLY the free Laplacian in the record (tortoise) coordinate, for
every lapse profile - so a horizon is a locus at infinite record
distance, with log-many modes per decade of approach and exponential
infall at the surface-gravity rate (measured to 2e-6).  TEMPERATURE BY
TWO INDEPENDENT RECEIPTS: the Euclidean record geometry is smooth at the
tip - demands NO boundary record - at the UNIQUE period beta = 2pi/kappa
(Bessel match 1e-5, tip exponent 0.9997), and the record vacuum reduced
to a wedge is thermal in the boost modes at T = 1/2pi, with the
Bisognano-Wichmann identity eps_k = 2pi omega_k holding UNIFORMLY TO
2.5e-5 across the entire resolvable modular spectrum.  THE RECORD
CENSORSHIP CRITERION: a lapse degeneracy N ~ x^beta is a horizon iff
beta >= 1, exactly when its extension ambiguity is displaced to infinite
record distance (CENSORED); for beta < 1 the locus sits at finite record
distance and demands a boundary record (NAKED) - the Weyl alternative of
Paper 12, upgraded to a censorship theorem.  Extremal horizons are COLD
(the smooth period tracks 1/N'(0), receipts at two parameters).
GREYBODY FACTORS ARE RECORD-IMPEDANCE PHYSICS: the lapse-squared mass
term is the barrier, the closed form is verified to 1e-14, the sharp-
step limit IS Paper 12's interface impedance law, and the record lattice
itself realizes the filter to 1.7e-5.  CAPACITY: the ledger sealed
behind a horizon seam grows by exactly ONE SIXTH OF A NAT PER E-FOLD in
1+1 (4.4e-4), is EXTENSIVE IN CUT AREA in 2d (the record area law), and
is counted in DISCRETE QUANTA with log-closing spacing - Paper 7's C5
direction, realized at finite scope
```

This paper executes the five-route horizon program enabled by Paper 12:
route 1 (the near-horizon record operator), route 2 (the temperature),
route 3 (the censorship classification), route 4 (greybody factors),
route 5 (capacity and entropy).  Everything below is at finite record
scope: continuum limits of the statements ride on (C-reg) where noted.

## 0. Verdict

```text
THE SETUP.  A horizon in SHARD is not an input: it is a lapse-degeneracy
locus N -> 0 of the record operator A_N = -N d(N d.) that Paper 12 made
operational (lapse = Z_perp = local clock rate).  The single structural
fact driving all five routes:

  A_N = -(N d/dx)^2 = -d^2/dy^2,   y = int dx/N  (record coordinate),

EXACTLY, for every lapse profile - the lapse geometry is free in record
coordinates, and all horizon physics is the geometry of the map x -> y.

ROUTE 1 (the near-horizon operator).  For N = kappa x the locus sits at
  INFINITE record distance (Y = (1/kappa) ln(1/x_min), lattice receipt
  2e-7); the lapse spectrum is the free spectrum (kpi/Y)^2 at O(h^2)
  (ratio 4.00); the counting function grows by (sqrt(L)/pi)(ln 10)/kappa
  per decade of approach (measured increments 14, 15, 15 vs 14.66):
  modes PILE UP at the horizon; infalling record packets obey
  x(t) = x_0 e^{-kappa t} (fitted slopes -1.0000, -0.5000; errs 2e-6,
  3e-6): the locus is never reached at finite record time.

ROUTE 2 (the temperature, two independent receipts).
  EUCLIDEAN (riding P12's OS bridge): the Euclidean record geometry
  ds^2 = dx^2 + N^2 dtau^2 near the locus is a cone of angle kappa beta.
  The m = 1 spectrum is j_{nu,1}^2 with nu = 2pi/(kappa beta) (machine:
  4.16532/3.83161/3.55969 vs 4.16543/3.83171/3.55978) and the tip mode
  exponent is nu (1.2497/0.9997/0.7997): the tip is SMOOTH - demands no
  boundary record - at exactly ONE period, beta = 2pi/kappa.  The
  temperature is a no-extra-record condition: T = kappa/2pi.
  LORENTZIAN (Bisognano-Wichmann on the record lattice): the record
  vacuum reduced to a half-line wedge is Gaussian-thermal with respect
  to the BOOST record operator: the single-particle modular energies
  satisfy eps_k = 2pi omega_k UNIFORMLY TO 2.5e-5 across all eight
  double-precision-resolvable levels - T = 1/(2pi) per unit surface
  gravity, the flat-collar T = 1/2pi theorems (P4-P6) promoted to the
  wedge.  The level-independent 2.5e-5 residual is the half-site
  cut-placement ambiguity: the boost generator IS the alpha = 1
  threshold operator of P12's boundary-record classification.

ROUTE 3 (the censorship criterion).  For N = x^beta the record distance
  Y = int dx/N is FINITE iff beta < 1, and the lapse form is always free
  in record coordinates, so the entire classification is one quantity:
    beta < 1: the locus is a regular endpoint at FINITE record distance:
      clamped and free towers converge to DIFFERENT continuum theories
      (beta = 0.5: lam_1 -> pi^2/4 vs pi^2/16, exact targets): a
      boundary record is DEMANDED: the degeneracy is NAKED.
    beta >= 1: infinite record distance: both towers collapse onto the
      SAME free geometry (lam_1 Y^2 pinned at pi^2 / pi^2/4 to 4 digits
      in every row while lam_1 -> 0): the extension ambiguity rides AT
      INFINITE RECORD DISTANCE, invisible to every sealed diamond:
      CENSORED: the degeneracy is a HORIZON.
  beta = 1 (Rindler) is the marginal case - Y diverges logarithmically,
  the same log threshold P12 measured at alpha = 1.  RECORD COSMIC
  CENSORSHIP: horizon = degeneracy whose boundary-record demand is
  displaced to infinite record distance.  EXTREMAL COLDNESS: for
  N = x(x+a)/(1+a) the tip is smooth only at beta = 2pi/N'(0) (tip
  exponents 0.9926/0.9853 at the predicted period vs 2.9779/4.9269 at
  the naive one): T = N'(0)/2pi -> 0 in the extremal limit - extremal
  record horizons are cold, their Euclidean tip a cusp no period closes.

ROUTE 4 (greybody factors = record impedance).  In record coordinates a
  massive mode sees the barrier V(y) = N(y)^2 m^2: the lapse-squared
  mass term.  For the Rindler-to-flat profile N^2 = 1/(1+e^{-2 kappa y})
  the barrier is the exactly solvable smooth step:
    R = [sinh(pi(k-q)/2kappa) / sinh(pi(k+q)/2kappa)]^2,
  verified by record-mode integration to 1.5e-14; the kappa -> infinity
  limit IS Paper 12's sharp-interface impedance law ((k-q)/(k+q))^2
  (0.021172 at kappa = 32 vs 0.021286); kappa -> 0 is transparent
  (3.9e-25): the greybody filter is the impedance mismatch smoothed over
  the thermal record width 1/(4 pi T_H).  The record lattice itself
  realizes the filter: packet energy split 0.05079 vs flux-weighted
  band average 0.05080 (1.7e-5).  Below the barrier, R = 1 to machine
  precision: each massive channel opens only above m_perp.
  Composition: Hawking flux = (route-2 thermal spectrum at kappa/2pi)
  x Gamma(omega), with Gamma = 1 - R.

ROUTE 5 (capacity).  The record entropy sealed behind a single seam in
  1+1 grows as S = (1/6) ln(record depth) + const: measured coefficient
  0.16622 vs 1/6 (4.4e-4), with S - (1/6) ln(depth) constant to 1e-3
  over 16x in depth: ONE SIXTH OF A NAT PER E-FOLD.  In 2d the wedge
  entropy is EXTENSIVE IN THE CUT AREA (S = 0.07222 n - 0.157, max
  residual 2.7e-3): the record area law, slope a lattice constant - the
  LAW is the linearity.  The modular ledger is DISCRETE with spacing
  closing logarithmically (one-constant law Delta eps = 2pi^2/ln(cL):
  predicted 2.369 vs measured 2.345 across a factor 4 in depth): P7's
  C5 capacity-quantization direction, realized at finite record scope.

WHAT THIS BUYS THE KERNEL: nothing in the kernel list changes - and
that is the point: Hawking-flavored physics needed NO new assumptions.
Temperature, censorship, greybody, and capacity all came out of the
existing theorems (arrow-positivity/RP, the OS bridge, the lapse
operator, the boundary-record classification) instantiated at the
degeneracy locus.  The continuum-scope versions ride on (C-reg).
```

## 1. Method and reproducibility

```text
code/v6_p13a_near_horizon_campaign.py    route 1: distance, pileup, infall
code/v6_p13b_temperature_campaign.py     route 2: cone + Bisognano-Wichmann
code/v6_p13c_censorship_campaign.py      route 3: censorship line, extremal
code/v6_p13d_greybody_campaign.py        route 4: barrier, limits, packet
code/v6_p13e_capacity_campaign.py        route 5: 1/6 nat, area law, quanta
```

Every printed number is machine-generated by the scripts above (numpy/
scipy; the Gaussian wedge machinery uses exact covariance algebra, no
sampling).  Imports, named: Bessel zeros (cone spectra); the smooth-step
closed form (Landau-Lifshitz class scattering); the chord finite-size
form for end-interval entropy (CFT, c = 1); Bisognano-Wichmann as the
CONTINUUM target the lattice receipt approximates.  Corpus inputs: the
lapse record operator and Z_perp identification (P12 5.2), the
boundary-record classification (P12 7), the OS bridge (P12 3 / P10
Part I), the flat-collar T = 1/2pi thermality theorems (P4-P6), the
Gaussian record towers (P11 Part I).

## 2. Route 1: the near-horizon record operator

The single structural fact: N d/dx = d/dy with y = int dx/N, so

    A_N = -N d(N d.) = -d^2/dy^2    EXACTLY, for every lapse profile.

The lapse geometry is FREE in record coordinates; horizon physics is
the geometry of the map x -> y.  For N = kappa x, y = (1/kappa) ln x:

```text
record distance:  Y(x_min) = (1/kappa) ln(1/x_min); lattice tracks it
                  to 5.5e-8 (x_min = 1e-2) and 2.2e-7 (1e-4).
free structure:   lam_1..4 vs (k pi / Y)^2: max rel err 4.78e-6 (n=2000)
                  -> 1.20e-6 (n=4000), ratio 4.00 [O(h^2)].
mode pileup:      modes below Lambda = 400 for x_min = 1e-2..1e-5:
                  29, 43, 58, 73 (predicted 29.3, 44.0, 58.6, 73.3);
                  increments per decade 14, 15, 15 vs (sqrt(L)/pi) ln 10
                  = 14.66: log-many modes per decade, without bound.
infall:           packet centroid obeys x(t) = x_0 e^{-kappa t}:
                  fitted d ln x_c/dt = -1.0000 (kappa = 1, err 1.6e-6)
                  and -0.5000 (kappa = 0.5, err 2.7e-6).
```

The horizon is at infinite record distance behind a free geometry; the
exponential approach at the surface-gravity rate and the spectral pileup
are its two operational signatures.  (Both are exact statements about
the finite lattice towers - no continuum import.)

## 3. Route 2: the temperature, twice

### 3.1 The Euclidean receipt: temperature = no-extra-record condition

The Euclidean record geometry of the static lapse metric is
ds^2 = dx^2 + N^2 dtau^2 with tau-period beta; near the locus this is a
cone of total angle kappa beta.  Receipts (kappa = 1, m = 1 sector,
nu = 2pi/(kappa beta)):

```text
 kappa*beta/2pi    nu       sqrt(lam_1)   j_{nu,1}     tip exponent
     0.80         1.250      4.16532      4.16543        1.2497
     1.00         1.000      3.83161      3.83171        0.9997
     1.25         0.800      3.55969      3.55978        0.7997
 smooth period, lam_1..3 vs j_{1,k}^2: rel errs 5.0e-5 each
```

The tip carries a conical defect - a demand for a boundary record at
the degeneracy, in P12's classification - for every period EXCEPT
beta = 2pi/kappa, where the record geometry is the smooth disk (mode
exponent exactly 1: analytic tip).  Via the OS bridge, the Euclidean
record law at this unique period reconstructs the Lorentzian wedge
dynamics: the wedge state is KMS at

    T = 1/beta = kappa/2pi  (= 0.159155 at kappa = 1).

Temperature is a smoothness condition: the horizon radiates at exactly
the rate at which its Euclidean tip needs no extra ledger entry.

### 3.2 The Lorentzian receipt: Bisognano-Wichmann on the record lattice

The record vacuum (ground state of the flat record chain, P11's tower;
n = 3000, mass 0.02), reduced to a half-line wedge of 600 sites with a
single cut, is Gaussian-thermal with respect to the BOOST record
operator K = sum_j x_j h_j on the same wedge:

```text
  k    eps_k (modular)    2pi omega_k (boost)    ratio/2pi
  1       1.64727             1.64731            0.999975
  2       4.94181             4.94194            0.999975
  ...
  8      24.70911            24.70968            0.999977
```

The identity eps_k = 2pi omega_k holds UNIFORMLY TO 2.5e-5 across the
entire double-precision-resolvable modular spectrum (levels beyond
eps ~ 33 saturate round-off: nu - 1/2 ~ 1e-14).  This is the
Bisognano-Wichmann property realized on the record lattice: T = 1/2pi
per unit surface gravity, the flat-collar modular temperature of
Papers 4-6 promoted to the wedge.  Two structural notes:

1. The residual is LEVEL-INDEPENDENT - a single cut-placement
   systematic (the half-site ambiguity in where x = 0 sits), not an
   accumulating lattice error.  The boost generator is exactly the
   alpha = 1 THRESHOLD operator of P12's boundary-record
   classification: the ambiguity that operator carries at its
   degenerate end is the cut-placement freedom, and it shows up as one
   global scale shift of 2.5e-5.
2. The two receipts are independent: 3.1 uses only Euclidean geometry
   plus the OS bridge; 3.2 uses only the Lorentzian ground state plus
   the boost operator.  They agree on T = kappa/2pi.

## 4. Route 3: the record censorship criterion

For N = x^beta everything reduces to one quantity - the record distance
to the locus, Y = int_0 dx/x^beta, finite iff beta < 1.  Clamped vs
free record towers (grids uniform in the record coordinate):

```text
 beta   x_min    lam1_clamped   lam1_free    lam1_c*Y^2  lam1_f*Y^2     Y
 0.50   1e-4      2.517498      0.629374      9.8696      2.4674      1.980
 0.75   1e-4      0.761543      0.190386      9.8696      2.4674      3.600
 1.00   1e-4      0.116345      0.029086      9.8696      2.4674      9.210
 2.00   1e-4      0.000000      0.000000      9.8696      2.4674   9999.000
 (all x_min rows pinned at pi^2 = 9.8696 and pi^2/4 = 2.4674)
```

The towers ALWAYS realize the free interval of length Y(x_min) - the
classification is entirely in whether Y converges:

```text
beta < 1 (NAKED): Y finite (e.g. 2 at beta = 0.5; 4 at beta = 0.75):
  lam_1 converges to TWO DIFFERENT exact limits (beta = 0.5: clamped ->
  pi^2/4 = 2.4674, free -> pi^2/16 = 0.6169): the locus is a regular
  endpoint at finite record distance, the continuum theory is
  undetermined until a boundary record decides.
beta >= 1 (CENSORED = HORIZON): Y diverges: both towers collapse onto
  the same free record geometry; the clamped/free label survives only
  as a tag riding AT INFINITE RECORD DISTANCE - invisible to every
  sealed diamond at finite distance.
beta = 1 marginal: Y ~ ln(1/x_min) - Rindler sits exactly at P12's
  logarithmic threshold; beta = 2 censors at power rate.
```

**Record cosmic censorship (finite-scope theorem + classification).** A
lapse degeneracy is a horizon precisely when its self-adjoint-extension
ambiguity (its boundary-record demand, P12 7) is displaced to infinite
record distance.  Naked degeneracies are exactly those whose missing
ledger entry sits at finite record distance.  This upgrades P12's Weyl
classification into a censorship criterion: the record ontology does
not FORBID naked loci - it prices them: a naked locus is an incomplete
ledger, a horizon is a complete one.

**Extremal coldness.** For N = x(x+a)/(1+a) (surface gravity
kappa_a = a/(1+a)), the Euclidean tip is smooth only at the predicted
period:

```text
   a     kappa_a     tip exponent at 2pi/kappa_a   at 2pi (naive)
  0.50   0.3333            0.9926                     2.9779
  0.25   0.2000            0.9853                     4.9269
```

T = N'(0)/2pi tracks the surface gravity; as a -> 0 the smooth period
diverges and the tip degenerates to a cusp no period closes: EXTREMAL
RECORD HORIZONS ARE COLD.  (The residual 1e-2 in the exponent is the
O(x/a) curvature correction inside the fit window - it shrinks with the
window, receipt at stated scope.)

## 5. Route 4: greybody factors are record-impedance physics

In record coordinates a transverse-massive record mode obeys
u_tt = u_yy - V u with V(y) = N(y)^2 m_perp^2 - the lapse-squared mass
term IS the greybody barrier (zero at the horizon, m^2 at infinity).
For the Rindler-to-flat profile N^2 = 1/(1 + e^{-2 kappa y}) the barrier
is the exactly solvable smooth step, R = [sinh(pi(k-q)/2kappa) /
sinh(pi(k+q)/2kappa)]^2 with k = omega, q = sqrt(omega^2 - m^2):

```text
(i)  record-mode ODE vs closed form (kappa = 0.5, m = 1):
      omega 1.05: 0.01753891 vs 0.01753891  (|diff| 1.5e-14)
      omega 1.20: 0.00022365 vs 0.00022365  (5.4e-16)
(ii) the two limits:
      kappa = 32: R = 0.021172 vs sharp-interface impedance law
        ((k-q)/(k+q))^2 = 0.021286  - P12's seam physics recovered;
      kappa = 0.125: R = 3.9e-25 - adiabatic transparency.
(iii) record-native: lattice packet energy split 0.05079 vs
      flux-weighted band average 0.05080  (|diff| 1.7e-5).
(iv) below the barrier: |R - 1| = 2.2e-16 / 0.0 - total reflection.
```

The greybody filter is the impedance mismatch of the near-horizon
collar smoothed over the thermal record width 1/(2 kappa) = 1/(4 pi
T_H): hot horizons scatter like sharp seams (P12's interface), cold
ones are transparent.  Composition statement: the emission of the lapse
horizon in each channel is the route-2 thermal spectrum at T = kappa/2pi
filtered by Gamma(omega) = 1 - R(omega), with a hard gap below m_perp.

## 6. Route 5: capacity - the ledger behind the seam

```text
(i)  1+1, single seam: S - (1/6) ln(record depth) constant to ~1e-3
     over 16x in depth (chord form); fitted ln-coefficient 0.16622 vs
     1/6 = 0.16667 (err 4.4e-4): ONE SIXTH OF A NAT PER E-FOLD.
(ii) 2d, line cut: S = 0.07222 * (cut length) - 0.157, max residual
     2.7e-3 across n = 12..28: the record AREA LAW - capacity extensive
     in the seam area; the slope is a lattice constant, the LAW is the
     linearity.
(iii) capacity quanta: the modular ledger is DISCRETE; level spacing
     closes logarithmically: one-constant law Delta eps = 2pi^2/ln(cL)
     calibrated at L = 128 (c = 8.104) predicts 2.36947 at L = 512;
     measured 2.34528 (1%): the boost log-box of route 2.
```

This realizes Paper 7's C5 direction (capacity quantization /
horizon-spectrum discreteness) at finite record scope: the ledger
sealed behind a horizon seam is counted in discrete modular quanta, its
total grows with the seam area (2d) or logarithmically with depth
(1+1), and the discreteness signature - level spacing - closes only
logarithmically.  The Bekenstein-Hawking AREA COEFFICIENT is NOT
derived: it is the calibration question (the nat-to-Planck-area
constant), explicitly part of what (C)/(M) must jointly fix (P7 14.1
item 6).

## 7. What this paper proves and does not prove

Proves, with machine verification at the printed values: the exact
tortoise-freeness of the lapse operator and its three horizon
signatures (distance, pileup, infall at surface-gravity rate); the
cone-smoothness selection of beta = 2pi/kappa with the defect-as-
boundary-record reading; the Bisognano-Wichmann identity on the record
lattice at 2.5e-5 uniform; the censorship classification (naked iff
finite record distance, with exact distinct limits below the line and
universal collapse above it) and extremal coldness; the closed-form
greybody factor from record scattering with both limits and the
record-native packet receipt; the 1/6-nat-per-e-fold law, the 2d area
law, and the log-closing capacity quanta.

Does not prove: the continuum (3+1, curved, interacting) versions of
any of these - they ride on (C-reg) (P12) and on matter coupling
(process-O6); the Bekenstein-Hawking coefficient (calibration, P7 14.1
item 6); back-reaction and evaporation dynamics (the nonlinear regime,
explicitly outside (C) per P12 8); the black-hole information ledger
beyond the kinematic capacity statements of route 5.  The
Bisognano-Wichmann receipt is a finite-lattice realization of a
continuum theorem, not a new proof of it; its corpus content is that
the record vacuum and boost operator land on it with no tuning.

## 8. The kernel after Paper 13

```text
KERNEL: unchanged - { (C-reg), (M), (V), process-O6 } +
        { D10, O7, O8, O11-remainder }.  Deliberately so: every horizon
        result above is the EXISTING theorems instantiated at the
        degeneracy locus; Hawking-flavored physics demanded no new
        axioms and added no new kernel items.
UPGRADED / REALIZED:
  P12 H-flag  -> EXECUTED: degeneracy loci are horizons iff beta >= 1;
                 the boundary-record demand is the censorship criterion.
  P7 14.1(3)  -> the curved-collar transfer mechanism EXISTS at lapse
                 scope: T = kappa/2pi by two independent receipts
                 (curved-collar Hawking at record scope; the full
                 curved-background QFT version rides on (C-reg)).
  P7 C5       -> realized at finite scope (route 5): discrete modular
                 quanta, area law, 1/6 nat per e-fold.
  P12 alpha=1 threshold -> identified AS the boost generator's cut
                 ambiguity (3.2) and AS Rindler marginality (4).
NEW NAMED DIRECTIONS (not kernel):
  H-evap: back-reaction/evaporation - needs nonlinear dynamics (outside
          (C)) plus matter coupling (process-O6).
  H-info: the information ledger across the seam - route 5 gives the
          kinematic capacity; the dynamical statement needs H-evap.
  H-BH:   the Bekenstein-Hawking coefficient = the calibration contact
          (P7 14.1 item 6), now with a concrete object to calibrate
          (the route-5 slope).
```

## 9. Status

```text
Route 1: CLOSED at lattice scope - exact tortoise-freeness; pileup
         14.66/decade; infall slope -kappa to 2e-6.
Route 2: TEMPERATURE ESTABLISHED at stated scope - Euclidean: unique
         no-defect period (Bessel 1e-5, exponent 0.9997); Lorentzian:
         BW at 2.5e-5 uniform over eight modular levels.  T = kappa/2pi.
Route 3: CENSORSHIP CRITERION proved at tower scope - naked iff finite
         record distance (beta < 1); Rindler marginal (log); extremal
         cold (period tracks 1/N'(0): 0.9926/0.9853 vs 2.98/4.93).
Route 4: GREYBODY = thermal-smoothed record impedance - closed form to
         1.5e-14; P12 interface law as the sharp limit; record-native
         packet receipt 1.7e-5; sub-barrier R = 1 exact.
Route 5: CAPACITY realized - 1/6 nat per e-fold (4.4e-4); 2d area law
         (residual 2.7e-3); discrete quanta with log-closing spacing
         (1% one-constant prediction).
Kernel:  unchanged by design; H-evap, H-info, H-BH named as directions.
```

## References and literature map

- Papers 4-6, 10-12 (internal): flat-collar thermality T = 1/2pi and
  the modular/RP machinery (P4-P6); arrow-positivity and the OS bridge
  (P10 Part I, P12 3); the lapse record operator and Z_perp (P12 5.2);
  the boundary-record classification and the alpha = 1 threshold
  (P12 7); Gaussian record towers (P11 Part I).
- J. J. Bisognano and E. H. Wichmann, J. Math. Phys. 16, 985 (1975);
  W. G. Unruh, Phys. Rev. D 14, 870 (1976); S. W. Hawking, Comm. Math.
  Phys. 43, 199 (1975): the continuum targets of route 2.
- G. W. Gibbons and S. W. Hawking, Phys. Rev. D 15, 2752 (1977):
  Euclidean smoothness selecting the period (the cone receipt's
  continuum face).
- H. Casini and M. Huerta, J. Phys. A 42, 504007 (2009); I. Peschel and
  V. Eisler, J. Phys. A 42, 504003 (2009): Gaussian/lattice modular
  technology (the wedge machinery of 3.2 and route 5).
- P. Calabrese and J. Cardy, J. Stat. Mech. P06002 (2004): the c/6
  end-interval law and chord form.
- L. D. Landau and E. M. Lifshitz, Quantum Mechanics, Section 25
  problems: the smooth-step closed form (route 4).
- D. N. Page, Phys. Rev. D 13, 198 (1976): greybody-filtered Hawking
  flux (the composition statement's continuum face).
- R. Penrose, Riv. Nuovo Cim. 1, 252 (1969): cosmic censorship (the
  conjecture route 3 recasts in record terms).
- H. Weyl (1910); J. von Neumann (1929): the extension theory under
  the censorship classification (via P12 7).
```
