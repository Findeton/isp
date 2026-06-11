# Paper 13 (v6) - SHARD: The Horizon Campaign

Preprint, not peer reviewed, version 2026-06-10.

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
sampling; all five scripts rerun bit-identically).  Imports, named:
Bessel zeros (cone spectra); the smooth-step closed form (Landau-
Lifshitz class scattering); the chord finite-size form for end-interval
entropy (CFT, c = 1); Bisognano-Wichmann as the CONTINUUM target the
lattice receipt approximates.  Corpus inputs: the lapse record operator
and Z_perp identification (P12 5.2), the boundary-record classification
(P12 7), the OS bridge (P12 3 / P10 Part I), the flat-collar T = 1/2pi
thermality theorems (P4-P6), the Gaussian record towers (P11 Part I).

## 2. Route 1: the near-horizon record operator

### 2.1 The structural identity, with proof

**Proposition 1 (tortoise freeness).**  Let N: (0, 1] -> (0, infinity)
be any lapse profile and define the record (tortoise) coordinate
y(x) = - int_x^1 dxi / N(xi), so dy = dx / N.  Then on L^2(dx/N),

```text
   A_N u := -N d/dx ( N du/dx )  =  - d^2 u / dy^2     EXACTLY.
```

*Proof.*  By the chain rule, N d/dx = (dx/dy)^{-1} ... more directly:
d/dy = (dx/dy) d/dx = N d/dx, since dx/dy = N.  Hence
A_N = -(N d/dx)(N d/dx) = -(d/dy)^2.  Symmetry: for u, v vanishing at
the ends, <u, A_N v>_{dx/N} = int u (-(N v')') dx = int N u' v' dx,
symmetric and positive.  The measure dx/N is exactly dy, so the
operator is THE free Laplacian on the record interval [-Y, 0] with
Y = int_0^1 dx/N.                                                QED

Every lapse geometry is free in record coordinates; all horizon physics
is the geometry of the map x -> y.  Three corollaries become the
route's receipts: (a) the record distance to the locus is Y(x_min) =
int_{x_min}^1 dx/N, divergent for N = kappa x as (1/kappa) ln(1/x_min);
(b) the spectrum on [x_min, 1] with Dirichlet ends is exactly
(k pi / Y)^2; (c) a record null ray moves at unit speed in y, hence
dx/dt = -N(x) and, for N = kappa x, x(t) = x_0 e^{-kappa t}.

### 2.2 Receipts

```text
(i) record distance (lattice sum of dx/N vs (1/kappa) ln(1/x_min)):
   x_min = 1e-2:  Y = 4.605170  vs  4.605170   (rel err 5.5e-8)
   x_min = 1e-4:  Y = 9.210342  vs  9.210340   (rel err 2.2e-7)
(ii) exact free structure (lam_1..4 vs (k pi / Y)^2, x_min = 1e-3):
   n = 2000: max rel err 4.78e-6;  n = 4000: 1.20e-6;  ratio 4.00
   [O(h^2): 4.00 - the equivalence holds on the lattice as in the
   continuum]
(iii) mode pileup (modes below Lambda = 400 vs (sqrt(Lambda)/pi) Y):
   x_min = 1e-2: 29 (pred 29.32);  1e-3: 43 (43.98);
   1e-4: 58 (58.63);  1e-5: 73 (73.29)
   increments per decade: 14, 15, 15  vs  (20/pi) ln 10 = 14.66
(iv) infall (packet centroid, geometric grid, symmetrized leapfrog):
   kappa = 1.0:  fitted d ln x_c / dt = -1.0000   (err 1.6e-6)
   kappa = 0.5:  fitted d ln x_c / dt = -0.5000   (err 2.7e-6)
```

### 2.3 Readings

1. The horizon is not a place where the operator degenerates - in
   record coordinates nothing degenerates; the horizon is a place
   PUSHED TO INFINITE RECORD DISTANCE.  All near-horizon "pathology"
   in coordinate language is the pullback of perfectly free physics
   through the exponential map.
2. The counting function's unbounded log growth is the spectral
   signature of infinite record volume: log-many modes per decade of
   approach.  This is the kinematic seed of route 5's capacity laws.
3. The infall receipt is exact to 2e-6 because it is geometry, not
   dynamics: the packet rides the unit-speed record cone, and the
   exponential approach rate IS the surface gravity.  No tuning enters
   anywhere in this route - both receipts are zero-parameter.

## 3. Route 2: the temperature, twice

### 3.1 The Euclidean receipt: temperature = no-extra-record condition

**Setup.**  The Euclidean record geometry of the static lapse metric is
ds^2 = dx^2 + N(x)^2 dtau^2 with tau identified modulo a period beta.
Near a locus where N ~ kappa x, set rho = x and angle phi = kappa tau:
the metric is ds^2 = drho^2 + rho^2 dphi^2 with phi of period
kappa beta - a CONE of total angle kappa beta, smooth at the tip iff
kappa beta = 2 pi.

**The spectral form of smoothness.**  Decompose in angular modes
e^{2 pi i m tau / beta}: the radial operator for mode m is

```text
   A_m = -(1/x) d(x d.) + nu^2 / x^2,    nu = 2 pi m / (kappa beta),
```

on (0, 1] with Dirichlet at x = 1, in the measure x dx.  Its ground
eigenvalue is the squared first Bessel zero j_{nu,1}^2 and its ground
mode behaves as x^nu at the tip.  Smoothness at the tip = analyticity
of the m = 1 mode = exponent exactly 1 = nu = 1 = beta = 2 pi / kappa.
In the boundary-record language of P12 Section 7: for every OTHER
period the tip is a conical defect - a locus DEMANDING a boundary
record; the unique no-extra-record period is 2 pi / kappa.

**Receipts (kappa = 1; radial finite-volume, n = 20000; Bessel zeros
by bracketed root-finding on J_nu).**

```text
 kappa*beta/2pi    nu       sqrt(lam_1)   j_{nu,1}     tip exponent
     0.80         1.250      4.16532      4.16543        1.2497
     1.00         1.000      3.83161      3.83171        0.9997
     1.25         0.800      3.55969      3.55978        0.7997
 smooth period, full check: lam_1..3(m=1) vs j_{1,k}^2: rel errs
 5.0e-5, 5.0e-5, 5.0e-5
```

**The bridge to temperature.**  By Paper 12's OS bridge (itself riding
P10's reflection-positivity theorem), the Euclidean record law at
period beta reconstructs the Lorentzian wedge dynamics, and the
reconstructed state satisfies the KMS condition at temperature
T = 1/beta.  The unique smooth (no-extra-record) period therefore
assigns the wedge the temperature

```text
   T = kappa / 2 pi    (= 0.159155 at kappa = 1).
```

Temperature is a SMOOTHNESS condition: the horizon radiates at exactly
the rate at which its Euclidean tip needs no extra ledger entry.  This
is the record-native face of the Gibbons-Hawking argument, with
"regularity of the Euclidean section" replaced by the corpus' own
boundary-record demand (P12), and with the analytic continuation
replaced by a theorem (the OS bridge).

### 3.2 The Lorentzian receipt: Bisognano-Wichmann on the record lattice

**Setup.**  The flat record chain (n = 3000 sites, mass 0.02, Dirichlet
ends) in its ground state - the record vacuum, i.e. the Gaussian state
of P11's tower with covariances X = (1/2) A^{-1/2}, P = (1/2) A^{+1/2}.
Reduce to the WEDGE: the last 600 sites (a single entangling cut; the
far wall sits 12 correlation lengths away).  For a Gaussian state the
reduced state is Gaussian and its entanglement (modular) Hamiltonian
is quadratic; its single-particle modular energies are

```text
   eps_k = ln( (nu_k + 1/2) / (nu_k - 1/2) ),
```

with nu_k the symplectic eigenvalues of the reduced covariance pair
(eigenvalues of sqrt(X_V P_V)).  Independently, build the BOOST record
operator on the same wedge: K = sum_j x_j h_j with x_j = j + 1/2 the
distance from the cut, i.e. kinetic weights x_j, bond weights x_{j+1/2},
mass weights x_j m^2; its normal-mode frequencies omega_k come from
the generalized eigenproblem sqrt(T_w) V_w sqrt(T_w).  The continuum
Bisognano-Wichmann theorem says the modular Hamiltonian of a half-space
in the vacuum IS 2 pi times the boost: the lattice receipt tests
eps_k = 2 pi omega_k with both sides computed independently.

**Receipts.**

```text
  k    eps_k (modular)    2pi omega_k (boost)    ratio/2pi
  1       1.64727             1.64731            0.999975
  2       4.94181             4.94194            0.999975
  3       8.23635             8.23656            0.999975
  4      11.53089            11.53118            0.999975
  5      14.82544            14.82581            0.999975
  6      18.11998            18.12043            0.999975
  7      21.41452            21.41505            0.999975
  8      24.70911            24.70968            0.999977
  (levels beyond eps ~ 33 saturate double precision: nu - 1/2 ~ 1e-14)
```

**Readings.**

1. The identity holds UNIFORMLY to 2.5e-5 across the entire resolvable
   modular spectrum - far beyond the few-percent agreement typical of
   entanglement-Hamiltonian lattice studies.  The residual is
   LEVEL-INDEPENDENT: a single cut-placement systematic (the half-site
   ambiguity in where x = 0 sits), not an accumulating lattice error.
2. That ambiguity has a corpus name: the boost generator IS the
   alpha = 1 threshold operator of P12's boundary-record
   classification (continuum form K ~ -d(x d.)); the boundary-record
   freedom that operator carries at its degenerate end is exactly the
   cut-placement freedom, and it shows up as one global 2.5e-5 scale.
3. The two receipts of this route are INDEPENDENT: 3.1 uses Euclidean
   geometry plus the OS bridge; 3.2 uses the Lorentzian ground state
   plus the boost operator.  They agree on T = kappa/2pi.  The modular
   spacing Delta eps ~ 3.29 ~ 2 pi^2 / ln(L)-class previews route 5's
   capacity quanta.

## 4. Route 3: the record censorship criterion

### 4.1 The classification theorem

**Theorem (record censorship, tower scope).**  Let N = x^beta on
(0, 1] and consider the clamped (Dirichlet at x_min) and free (Neumann
at x_min) record towers as x_min -> 0, with grids uniform in the record
coordinate.  By Proposition 1 every tower is the free Laplacian on an
interval of record length Y(x_min) = int_{x_min}^1 x^{-beta} dx, so:

```text
(a) beta < 1:  Y -> Y_inf = 1/(1-beta) FINITE.  The two towers
    converge to the free Laplacian on [0, Y_inf] with DIFFERENT
    boundary conditions: lam_1 -> (pi/Y_inf)^2 (clamped) vs
    (pi/2Y_inf)^2 (free) - two distinct continuum theories.  The locus
    is a regular endpoint at finite record distance; the limit is
    undetermined until a boundary record decides: NAKED.
(b) beta >= 1:  Y -> infinity.  Both towers collapse onto the same
    free half-line geometry: lam_1 -> 0 with lam_1 Y^2 -> pi^2 and
    pi^2/4 respectively - the clamped/free label is displaced to
    infinite record distance, invisible to every sealed diamond at
    finite distance: CENSORED.  The degeneracy is a HORIZON.
(c) beta = 1 is marginal: Y ~ ln(1/x_min) - the logarithmic threshold,
    the same marginality P12 measured at alpha = 1; beta = 2 censors
    at power rate (Y ~ 1/x_min).
```

*Proof.*  Immediate from Proposition 1: each tower is exactly a free
interval of length Y(x_min) with Dirichlet at the outer end and
Dirichlet/Neumann at the inner end, whose eigenvalues are known in
closed form; the only question is the behavior of Y, which is the
elementary integral above.                                       QED

The content is the REFRAMING: P12's Weyl limit-point/limit-circle
classification asked whether a boundary condition is needed; the lapse
form shows the need is equivalent to FINITENESS OF RECORD DISTANCE,
which is an operational, sealed-diamond-accessible quantity.  Cosmic
censorship, record-native: nature does not forbid naked loci - it
prices them as incomplete ledgers; horizons are the degeneracies whose
missing entry no finite observer can reach.

### 4.2 Receipts

```text
 beta   x_min    lam1_clamped   lam1_free    lam1_c*Y^2  lam1_f*Y^2     Y
 0.50   1e-2      3.046174      0.761543      9.8696      2.4674      1.800
 0.50   1e-3      2.631180      0.657795      9.8696      2.4674      1.937
 0.50   1e-4      2.517498      0.629374      9.8696      2.4674      1.980
 0.75   1e-4      0.761543      0.190386      9.8696      2.4674      3.600
 1.00   1e-4      0.116345      0.029086      9.8696      2.4674      9.210
 2.00   1e-4      0.000000      0.000000      9.8696      2.4674   9999.000
 (every row pinned at pi^2 = 9.8696 and pi^2/4 = 2.4674: the towers
  ALWAYS realize the free interval; beta only decides whether Y
  converges - beta = 0.5 rows converge to the distinct finite targets
  pi^2/4 = 2.4674 and pi^2/16 = 0.6169 as x_min -> 0)
```

### 4.3 Extremal coldness

For the family N = x(x + a)/(1 + a) the surface gravity is
kappa_a = N'(0) = a/(1+a); the cone analysis of 3.1 applies near the
tip with kappa -> kappa_a, so the smooth period is beta = 2pi/kappa_a.
Receipts (tip exponent of the m = 1 Euclidean mode, fit window above
the inner-cutoff contamination):

```text
   a     kappa_a     exponent at 2pi/kappa_a     at 2pi (naive)
  0.50   0.3333            0.9926                   2.9779
  0.25   0.2000            0.9853                   4.9269
  (naive-period exponents land at 1/kappa_a, as the cone formula
   predicts; the ~1e-2 residual at the smooth period is the O(x/a)
   curvature correction inside the fit window)
```

T = N'(0)/2pi tracks the surface gravity; as a -> 0 the smooth period
diverges and the Euclidean tip degenerates to a CUSP no period closes:
EXTREMAL RECORD HORIZONS ARE COLD.  In the censorship language: the
extremal locus (beta = 2) censors at power rate and radiates at zero
temperature - maximal censorship, minimal emission.

## 5. Route 4: greybody factors are record-impedance physics

### 5.1 The barrier and the closed form

In record coordinates a transverse-massive record mode obeys
u_tt = u_yy - V(y) u with V(y) = N(y)^2 m_perp^2: THE LAPSE-SQUARED
MASS TERM IS THE GREYBODY BARRIER - zero at the horizon (where N -> 0:
infinite redshift turns any rest mass off), m_perp^2 in the flat
region.  Choose the Rindler-to-flat profile N^2 = 1/(1 + e^{-2kappa y})
(exactly N = e^{kappa y} = kappa x near the horizon, N = 1 at
infinity): the barrier is the exactly solvable smooth step
V = m^2/(1 + e^{-2 kappa y}), with reflection coefficient (named
import: Landau-Lifshitz class scattering)

```text
   R(omega) = [ sinh( pi (k - q) / 2 kappa )
              / sinh( pi (k + q) / 2 kappa ) ]^2,
   k = omega,   q = sqrt(omega^2 - m_perp^2)     (omega > m_perp);
   R = 1 for omega <= m_perp (no propagating transmitted channel).
```

The two limits carry the physics: as kappa -> infinity the sinh's
linearize and R -> ((k - q)/(k + q))^2 - EXACTLY Paper 12's
sharp-interface impedance law with Z = sqrt(c); as kappa -> 0 the
reflection vanishes exponentially (adiabatic transparency).  Since the
step width in record coordinates is 1/(2 kappa) = 1/(4 pi T_H), the
greybody filter is THE IMPEDANCE MISMATCH OF THE NEAR-HORIZON COLLAR
SMOOTHED OVER THE THERMAL RECORD WIDTH: hot horizons scatter like
sharp seams, cold ones are transparent.

### 5.2 Receipts

```text
(i) record-mode ODE (RK4) vs closed form (kappa = 0.5, m = 1):
   omega = 1.05:  0.01753891 vs 0.01753891   |diff| 1.5e-14
   omega = 1.20:  0.00022365 vs 0.00022365   5.4e-16
   omega = 1.50:  6.5e-7 class                4.7e-17
(ii) limits:
   kappa = 2, 8, 32:  R = 0.006275, 0.019543, 0.021172
   sharp-interface impedance law ((k-q)/(k+q))^2 = 0.021286
   kappa = 0.125:  R = 3.9e-25  (adiabatic transparency)
(iii) record-native packet (lattice leapfrog, omega_0 = 1.2,
   kappa = 2): reflected energy fraction 0.05079 vs flux-weighted
   band average 0.05080   (|diff| 1.7e-5)
(iv) below the barrier: |R - 1| = 2.2e-16 / 0.0  (total reflection)
```

The flux-weighting in (iii) matters and is stated: the packet's
reflected ENERGY fraction equals the band average of R against the
energy-flux weight k^2 |u_hat(k)|^2, not the bare spectral weight -
with it, the record dynamics realizes the closed form to 1.7e-5.

### 5.3 Composition

The emission of the lapse horizon in each transverse channel is the
route-2 thermal spectrum at T = kappa/2pi filtered by the transmission
Gamma(omega) = 1 - R(omega), with a hard gap below m_perp: massive
channels open only above their barrier top.  This is the standard
greybody composition (named frame: Page), with both factors now
record-native: the temperature from 3.1's no-extra-record condition,
the filter from the lapse-squared barrier.

## 6. Route 5: capacity - the ledger behind the seam

### 6.1 Definitions

For a Gaussian record state reduced to a region V, the record entropy
is the symplectic entropy S = sum_k [(nu_k + 1/2) ln(nu_k + 1/2)
- (nu_k - 1/2) ln(nu_k - 1/2)], and the modular ledger is the discrete
set {eps_k} of 3.2.  "Record depth" for an end interval of length L in
a finite chain of n sites is the chord (2n/pi) sin(pi L / n) - the
finite-size form (named import: CFT, c = 1).

### 6.2 Receipts

```text
(i) 1+1, single seam (massless chain, n = 4000, end interval):
     L      S(L)        S - (1/6) ln(chord)
      64   0.780091        -0.028510
     128   0.894754        -0.029161
     256   1.009108        -0.029488
     512   1.121075        -0.029654
    1024   1.222661        -0.029737
   fitted ln-coefficient 0.16622 vs 1/6 = 0.16667 (err 4.4e-4):
   ONE SIXTH OF A NAT PER E-FOLD of record depth, with the additive
   constant stable to ~1e-3 over 16x in depth.
(ii) 2d, line cut (n x n lattices, mass 0.05, half-plane regions):
   S = 0.07222 * (cut length) - 0.157, max residual 2.7e-3 across
   n = 12..28: the record AREA LAW - capacity extensive in the seam
   area; the slope is a lattice constant, the LAW is the linearity.
(iii) capacity quanta: the modular spectrum is DISCRETE with spacing
   closing logarithmically: the one-constant law
   Delta eps = 2 pi^2 / ln(c L), calibrated at L = 128 (c = 8.104),
   predicts 2.36947 at L = 512; measured 2.34528 (1%).
```

### 6.3 Readings

1. This realizes Paper 7's C5 direction (capacity quantization /
   horizon-spectrum discreteness) at finite record scope: the ledger
   sealed behind a horizon seam is counted in discrete modular quanta;
   its total grows with seam area (2d) or logarithmically with depth
   (1+1); the discreteness signature - the level spacing - closes only
   logarithmically, i.e. it remains experimentally meaningful at any
   finite depth.
2. The Bekenstein-Hawking AREA COEFFICIENT is NOT derived: the 2d
   slope is a lattice constant, and converting nats per seam cell into
   nats per Planck area is precisely the calibration contact (P7 14.1
   item 6).  What IS derived is the FORM of the law and its quanta.
3. Routes 2 and 5 share machinery and meaning: the modular ledger that
   prices the wedge's temperature is the same discrete ledger whose
   count is the horizon's capacity - in record ontology, temperature
   and entropy are two readings of one boost spectrum.

## 7. What this paper proves and does not prove

Proves, with machine verification at the printed values: Proposition 1
(tortoise freeness, with its lattice receipts at O(h^2)) and its three
corollaries (distance, pileup, infall at surface-gravity rate); the
cone-smoothness selection of beta = 2pi/kappa with the
defect-as-boundary-record reading and the full-spectrum Bessel check;
the Bisognano-Wichmann identity on the record lattice at 2.5e-5
uniform with the cut-systematic identified; the censorship
classification theorem (4.1) with its exact distinct limits below the
line and universal collapse above it; extremal coldness at two
parameters; the closed-form greybody factor from record scattering
with both limits and the record-native packet receipt; the
1/6-nat-per-e-fold law, the 2d area law, and the log-closing capacity
quanta.

Does not prove: the continuum (3+1, curved, interacting) versions of
any of these - they ride on (C-reg) (P12) and on matter coupling
(process-O6); the Bekenstein-Hawking coefficient (calibration, P7 14.1
item 6); back-reaction and evaporation dynamics (the nonlinear regime,
explicitly outside (C) per P12 8); the black-hole information ledger
beyond the kinematic capacity statements of route 5.  The
Bisognano-Wichmann receipt is a finite-lattice realization of a
continuum theorem, not a new proof of it; its corpus content is that
the record vacuum and boost operator land on it with no tuning, and
that the residual is the P12 threshold ambiguity, named.

## 8. The kernel after Paper 13

```text
KERNEL: unchanged - { (C-reg), (M), (V), process-O6 } +
        { D10, O7, O8, O10-closed, O11-remainder }.  Deliberately so:
        every horizon result above is the EXISTING theorems
        instantiated at the degeneracy locus; Hawking-flavored physics
        demanded no new axioms and added no new kernel items.
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
                 ambiguity (3.2) and AS Rindler marginality (4.1c).
NEW NAMED DIRECTIONS (not kernel):
  H-evap: back-reaction/evaporation - needs nonlinear dynamics (outside
          (C)) plus matter coupling (process-O6).
  H-info: the information ledger across the seam - route 5 gives the
          kinematic capacity; the dynamical statement needs H-evap.
  H-BH:   the Bekenstein-Hawking coefficient = the calibration contact
          (P7 14.1 item 6), now with a concrete object to calibrate
          (the route-5 slope).
```

**[Paper 26 update.]** The capacity results of this route became the
BOUNDARY TERM of the pre-click capacity law for quantum processors
(K_pre <= min(boundary, rate, channel) - leakage): the record area law
supplies the record-native term of the min, with rate and channel
capacities as named imports.  See Paper 26, Section 2.

## 9. Status

```text
Route 1: CLOSED at lattice scope - exact tortoise-freeness (Prop. 1);
         pileup 14.66/decade; infall slope -kappa to 2e-6.
Route 2: TEMPERATURE ESTABLISHED at stated scope - Euclidean: unique
         no-defect period (Bessel 1e-5, exponent 0.9997); Lorentzian:
         BW at 2.5e-5 uniform over eight modular levels.  T = kappa/2pi.
Route 3: CENSORSHIP CRITERION proved at tower scope (Theorem 4.1) -
         naked iff finite record distance (beta < 1); Rindler marginal
         (log); extremal cold (period tracks 1/N'(0)).
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
