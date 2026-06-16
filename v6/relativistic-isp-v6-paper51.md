# Paper 51 (v6) - SHARD: Ledger Radiation - Causal Conserving Dynamics, the Generic Multipole Frequency Law, and the Limit at the Quadrupole Hierarchy (the Long March's Dynamics Closer)

Preprint, not peer reviewed, version 2026-06-13.

Author: Felix Robles Elvira

Subtitle:

```text
The long march closed the STATIC first-law sector (P44-P50:
modular response = boost law, capacity coupling G = 1/(4 nu),
planar / momentum / spherical).  P51 is its final step and its
FIRST dynamics result: real-time radiation, via the chain's
intrinsic real-time Hamiltonian (phonon) evolution of the P50
partial-wave radial chains K_l = tridiag(2,-1,-1) +
diag(l(l+1)/r^2), x'' = -K x + f(r,t) - the time-extended
covariance instrument P42-W1 registered, P44 validated against
the static route at 1.2e-14.  float64 (the real-time
Hamiltonian sector is float-safe - the complement of the
P48-P50 mpmath wall; declared).  This is a MODEST, HONEST
closer: two robust results and one honestly-stated limit.
ROBUST RESULT 1 - CAUSAL, CONSERVING REAL-TIME DYNAMICS: the
source emits phonons at the lattice sound speed c_s = 1,
CAUSALLY (the wavefront arrives at t = R/c_s, pre-arrival flux
2e-11 of signal), with the bond energy current EXACTLY
conserved (continuity dE/dt + div j = f.v to 5e-26);
screen-independent (1.6%), absorber-robust (0.0%), the two
production tools agreeing to 0%.
ROBUST RESULT 2 - THE GENERIC MULTIPOLE FREQUENCY LAW: the
radiated power obeys P_l ~ Omega^(2l+2) (deep-zone exponents
EXACTLY 2/4/6/8) - the centrifugal-barrier (kr)^(2l)
partial-wave suppression (textbook scalar radial Helmholtz,
Jackson).  l=2 -> Omega^6, the SAME omega-power as the GR
quadrupole formula, but a GENERIC-SCALAR fact, NOT
gravitational (stated plainly - no stress-energy, no spin-2).
THE LIMIT (the honest result, NOT dressed as an achievement):
the scalar dynamics does NOT reproduce gravitational
quadrupole DOMINANCE.  Conserving the source's low moments
zeroes the corresponding multipole's LEADING coupling, but
this is leading-order QUADRATIC-FORM bookkeeping (P_l ~ M_l^2,
P_0/M_0^2 constant to 6e-14) - the SAME machinery as the
eta-leakage, NOT a deep mechanism (graded consistently).  And
after conservation the quadrupole is the SMALLEST radiating
multipole - the ORDERING is the robust claim, not a ratio
(P_1/P_2 is k r0-dependent, 9646..37 across k r0 = 0.05..0.8;
the quadrupole smallest at EVERY k r0, more so deeper in the
zone), stable to 1% over r0 = 5..80 at fixed k r0 (the
radiation zone; a fixed-Omega r0-sweep would leave the zone
and is NOT the comparison - declared).  The
gravitational quadrupole DOMINANCE - the lowest radiating
multipole being l=2 - requires the spin-2 / stress-energy
structure (whose conserved currents have NO radiative monopole
or dipole at all; textbook GR, correctly GATED), which the
scalar modular framework does NOT contain.  THE HONEST NET:
the scalar ledger's dynamics reaches the generic multipole
structure - causal conserving radiation and the
centrifugal-barrier frequency law - and no further; the
gravitational quadrupole hierarchy is the gated tensor
sector's.  THE eta CONVERSION (honest): breaking conservation
reopens the monopole as P_0 ~ eps^2, largely a tautology of
the same quadratic form; the substantive content is only the
CONVERSION packaging (a bound on monopole gravitational
radiation bounds the ledger's entropy-production eta, value
registered-OPEN).  NOT claimed: the quadrupole dominance / the
gravitational hierarchy; the TT polarization; the relativistic
null propagation (only dispersive phonon causality); the GR
coefficient 1/5 G/c^5; the eta value; back-reaction; any deep
mechanism beyond the leading-order quadratic-form bookkeeping.
```

## 0. Question, route, the claim-vs-gated boundary

The long march closed the static first-law sector (P44-P50).
P51 is the final step and the first *dynamics* result: does the
ledger's real-time evolution reproduce gravitational radiation?
The honest answer, found here: it reproduces two *generic*
ingredients (causal conserving dynamics; the multipole
frequency law) and *not* the gravitational quadrupole
hierarchy, which needs the gated spin-2 sector.

**The route.**  Real-time Hamiltonian (phonon) dynamics of the
P50 partial-wave radial chains, $\ddot x = -Kx + f(r,t)$; the
radiated power $P_l$ at a distant screen is the multipole
spectrum.  The chain's *intrinsic* real-time evolution (the
time-extended covariance instrument P42-W1 registered; P44
validated the time-extended Williamson machinery against the
static route at $1.2\times10^{-14}$) - **not** the relativistic
spacetime structure (gated by P42's no-go), **not** the TT
polarization (gated).  float64: the real-time Hamiltonian
sector is float-safe, the complement of the P48-P50 mpmath wall
(declared).

**The claim-vs-gated boundary** (stated here, in W0, and in the
verdict).  TWO ROBUST CLAIMS (gate-free): (i) the real-time
phonon dynamics is causal and conserving; (ii) the multipole
frequency hierarchy $P_l \sim \Omega^{2(l+1)}$ - a **generic
scalar** fact (the centrifugal-barrier suppression, textbook
radial Helmholtz, no gravitational content).  THE LIMIT, also
claimed (the honest result, not an achievement): the scalar
dynamics does not reproduce gravitational quadrupole
*dominance* - after conservation the quadrupole is the smallest
radiating multipole, robustly; the dominance needs spin-2.
HONESTY on the suppression: conserving a moment $M_l$ zeroes
that multipole's leading coupling, but $P_l \sim M_l^2$ is a
leading-order *quadratic-form* identity (the same bookkeeping
as the $\eta$-leakage), not a deep mechanism.  GATED: the
quadrupole dominance / the gravitational hierarchy (needs
spin-2); the TT polarization; the relativistic null propagation
(only dispersive phonon causality, $c_s = 1$; P42 no-go); the
GR coefficient $1/5\,G/c^5$.  The "mass" / "momentum" reading
of $M_0, M_1$ is an *analogy*, stated - they are scalar-charge
moments.

Receipts: `code/v6_p51_ledger_radiation_campaign.py`, canonical
`/tmp/v6_p51_campaign.out`, bit-identical rerun verified;
ledger from computed flags.

## 1. Robust result 1 - causal, conserving dynamics (W0)

```text
  K-RAD0:  max|K_(l=0) - K_planar| = 0.0 exact (reuses P50)
  K-CONT:  energy-current continuity |dE/dt + div j - f.v| at a
           far site = 5.4e-26 (the EXACT conserved bond current)
  K-CAUSAL: c_s = 1; front arrives t = 266 (predicted 270);
           pre-arrival flux / signal = 1.5e-11
  CLEAN WINDOW: reflections return t_reflect = 870; reads in
           [270, 870]
  K-REFL:  steady power (absorbing BC) = 2.01e-1; screen-
           independence 1.6%, absorber-robustness 0.0%
  CROSS-CHECK: outgoing-Green P_0 = 2.005e-1 vs damped real-time
           2.010e-1 (agree 0%)
```

The source emits phonons at $c_s = 1$, **causally** - the
wavefront arrives at $t = R/c_s$ (the front speed is the max
group velocity; finite-$k$ packets are slower, no mode exceeds
$c_s$), pre-arrival flux $1.5\times10^{-11}$ - with the **bond
energy current the exact conserved current** (continuity to
$5\times10^{-26}$; unique up to a total-derivative gauge, the
screen-integrated flux gauge-invariant).  An absorbing layer
removes reflection contamination (screen-independent $1.6\%$,
absorber-robust $0.0\%$), and the two production tools agree to
$0\%$.  The real-time dynamics is instrument-grade - the
genuine achievement of this step.

## 2. Robust result 2 - the generic multipole frequency law (W2)

In the radiation zone the radiated power per channel scales as
$P_l \sim \Omega^p$:

```text
  window k r0 = 0.12-0.40: p = 1.95/3.97/5.97/7.97
  deep zone k r0 = 0.08-0.24: p = 1.98/3.99/5.99/7.99 = 2/4/6/8
```

The radiated power obeys $P_l \sim \Omega^{2(l+1)}$ - exact in
the deep zone (exponents $2/4/6/8$).  This is the
**centrifugal-barrier partial-wave law**: each multipole order
is suppressed by two more powers of $kr$ (textbook scalar
radial Helmholtz, Jackson), a *generic scalar* fact with no
gravitational content.  The quadrupole's $P_2 \sim \Omega^{6}$
is the *same $\Omega$-power* as the GR quadrupole formula, but
for the generic-scalar reason (the $l = 2$ centrifugal
barrier), not the gravitational one.  FORK Q: $p = 2(l+1)$
holds.  The exponent is claimed; the coefficient and the
gravitational reading are gated.

## 3. The limit - no quadrupole dominance (W1)

Conserving the source's low moments ($M_0 = \sum f$, $M_1 =
\sum r f$, to machine precision) suppresses the corresponding
multipole's leading coupling:

```text
  monopole leading-coupling suppression (M_0=M_1=0):
    P_0 -> 1.9e-4 of generic (5212x); dipole -> 8.6e-2 (12x)
  QUADRATIC-FORM receipt: P_0 / M_0^2 = 0.0306 constant to 6e-14
  ordering (M_0=M_1=0): P_1 > P_0 > P_2 (the quadrupole smallest)
  ROBUSTNESS (fixed k r0 = 0.4, source size r0 = 5..80):
    P_1/P_2 = 11.1/11.1/11.2/11.1/11.2 (stable to 1%)
  k r0-dependence (the ratio is NOT fixed - the ORDERING is the
    claim): P_1/P_2 = 9646/2462/614/151/37 at k r0 =
    0.05/0.1/0.2/0.4/0.8 - quadrupole smallest at EVERY k r0,
    increasingly so deeper in the zone
  deeper-kill (M_0..M_2=0 / M_0..M_3=0): lowest-radiating
    l = 0 / 1 (no monotone march to higher l)
```

**The suppression is bookkeeping, not a mechanism.**  $P_{\rm
rad}$ is a *quadratic form* in the source, and at leading order
$P_l \sim M_l^2$ - the receipt $P_0/M_0^2 = 0.0306$ constant to
$6\times10^{-14}$ confirms it - so "kill $M_l$, suppress $P_l$"
is a leading-order quadratic-form identity, the *same*
machinery as the $\eta$-leakage of Section 4 (which we likewise
call a tautology), not a deep dynamical mechanism.  Graded
consistently, declared.  (The dipole suppression is also
*feeble* - $12\times$, vs the monopole's $5212\times$ -
because $M_1 = 0$ is a much weaker condition on this lattice;
stated.)

**The quadrupole does not dominate - the honest limit.**  After
conservation the ordering is $P_1 > P_0 > P_2$: the quadrupole
is the **smallest** of the three low multipoles.  The *robust*
claim is the **ordering**, not a specific ratio - $P_1/P_2$ is
strongly $kr_0$-dependent ($9646/2462/614/151/37$ at $kr_0 =
0.05$-$0.8$), so the quadrupole is the smallest at *every*
$kr_0$ across the zone, and *increasingly* subordinate deeper
in it.  At fixed $kr_0 = 0.4$ the ordering is stable to $1\%$
across source size $r_0 = 5$-$80$ (a fixed-$\Omega$
$r_0$-sweep would *leave* the radiation zone, $kr_0 \to O(1)$,
and is not the right comparison - declared).  Killing deeper
moments does not march the lowest radiator to higher $l$ (it
returns to $l = 0$ then $l = 1$); the residual floor has no
clean multipole ordering - and its *value* ($P_0/P_2 \approx
6.4$) is genuine dynamics (the chain's coupling to higher
moments), the one non-bookkeeping fact in the suppression
story.

So on a *scalar* field the lowest radiating multipole after
low-moment conservation is *not* the quadrupole.  The
gravitational quadrupole *dominance* - $l = 2$ as the leading
radiator - requires the **spin-2 / stress-energy structure**:
the gravitational source's conserved currents (the
stress-energy tensor) have *no* radiative monopole or dipole
content at all (textbook GR - mass-energy conservation kills
the monopole, momentum and angular-momentum conservation the
dipole).  That structure is **gated** (the tensor arc, P42's
no-go territory), and the scalar modular framework does not
contain it.  FORK H: the quadrupole does not dominate - the
limit, stated plainly, not dressed as a "boundary located."
P51 reaches the generic multipole structure and no further.

## 4. The eta-conversion - honest about its content (W3)

```text
  (A) residual floor P_0/P_2 (M_0=M_1=0) a/r0-indep: 6.46..6.49
  (B) break conservation by eps: P_0 ~ eps^2.11
```

**(A)** The residual floor is *physical* (independent of the
moment-discretization $a/r_0$).  **(B)** Breaking conservation
by $\epsilon$ reopens the monopole as $P_0 \sim
\epsilon^{2.11}$.  **Honest:** since $P_{\rm rad}$ is a
quadratic form, "add an $\epsilon$-monopole, get $\epsilon^2$
monopole power" is largely a tautology of the quadratic form,
not a deep prediction - the *same* observation as the
suppression bookkeeping of Section 3.  The only substantive
content is the **conversion packaging**: the map (monopole
radiated power) $\leftrightarrow$ (conservation-breaking
scale)$^2$ means any future bound on monopole gravitational
radiation bounds the ledger's entropy-production rate $\eta$ -
resting on the gated, registered-open $\eta$ value.  FORK E:
the conversion is exhibited; the $\eta$ value is open; no deep
prediction is claimed.

## 5. Ledger and verdict

```text
  K-RAD0   l=0 chain == planar (0)            -> did not fire
  K-CONT   energy-current continuity (5e-26)  -> did not fire
  K-CAUSAL front at R/c_s, pre-arrival 2e-11  -> did not fire
  K-REFL   screen-indep 2% / absorber 0.0%    -> did not fire
  W1 SUPPRESSION (bookkeeping): M_0=M_1=0 zeroes leading monopole
    5212x, dipole 12x; P_0/M_0^2 const to 6e-14 -> quadratic-form
    bookkeeping (= the eta machinery), NOT a deep mechanism
  W1 HIERARCHY: ordering P_1 > P_0 > P_2 (P_1/P_2 = 20.7,
    P_0/P_2 = 6.4), ROBUST at fixed k r0 across r0=5..80 (1%)
    -> FORK H: NO, the quadrupole does not dominate (the LIMIT;
    gravitational dominance needs spin-2 - textbook GR, GATED)
  W2 FREQUENCY LAW (generic scalar): deep-zone p = 1.98/3.99/
    5.99/7.99 = 2/4/6/8 (centrifugal barrier, Jackson) -> FORK Q:
    p = 2(l+1) HOLDS (l=2 -> Omega^6, generic-scalar)
  W3 ETA: physical floor; P_0 ~ eps^2.11 (quadratic-form
    tautology); CONVERSION is the only content -> FORK E
  REGISTERED (NOT claimed): the QUADRUPOLE DOMINANCE / the
    gravitational hierarchy (needs spin-2); the TT polarization;
    the relativistic null propagation (dispersive phonon
    causality only, c_s = 1); the GR coefficient 1/5 G/c^5; the
    eta value; back-reaction; any deep mechanism beyond the
    leading-order quadratic-form bookkeeping; mp precision (the
    real-time sector is float-safe - declared)
  (ledger generated from computed flags in the canonical)
```

**Verdict.**  The long march's dynamics closer - a modest,
honest result.  Two things hold robustly: the ledger's
real-time phonon dynamics is **causal and conserving** ($c_s =
1$, front at $t = R/c_s$, the energy current exact), and the
radiated multipole power follows the **generic-scalar
centrifugal-barrier frequency law** $P_l \sim \Omega^{2(l+1)}$
(deep-zone exponents $2/4/6/8$; the quadrupole's $\Omega^6$
shared with GR for the generic-scalar reason).  And the
**limit** is stated plainly: the scalar dynamics does *not*
reproduce gravitational quadrupole dominance - after
conservation the quadrupole is the smallest radiating multipole
(robustly, at fixed $k r_0$), the "suppression" of the lower
multipoles is leading-order quadratic-form bookkeeping (the
same machinery as the $\eta$-leakage), and the gravitational
quadrupole dominance requires the spin-2 / stress-energy
structure that the scalar modular framework does not contain
(textbook GR, correctly gated).  For the gravitational ledger:
*at the dynamics level, the scalar ledger reaches the generic
multipole structure - causal conserving radiation and the
centrifugal-barrier frequency law - and no further; the
gravitational quadrupole hierarchy is the gated tensor sector's
work.*  NOT claimed: the quadrupole dominance / gravitational
hierarchy; the TT polarization; the relativistic null
propagation; the GR coefficient $1/5\,G/c^5$; back-reaction;
the $\eta$ value; any deep mechanism beyond the quadratic-form
bookkeeping.

This closes the long march: P47 (the tower receipt), P48 (the
hydrodynamic completion), P49 (momentum currency), P50
(spherical screens, early), P51 (ledger radiation) - the static
scalar first-law sector built end to end, its first step into
dynamics taken, and the limit at the tensor / spin-2 boundary
named honestly as the work that lies beyond the scalar modular
framework.

## Receipts

```text
code/v6_p51_ledger_radiation_campaign.py   the campaign
/tmp/v6_p51_campaign.out                   canonical
                        (BIT-IDENTICAL, ledger from flags)
W0: K-RAD0 0.0; K-CONT 5.4e-26; K-CAUSAL front 266 vs 270,
pre-arrival 1.5e-11; c_s = 1; window [270, 870]; K-REFL 1.6% /
0.0%; two-tool 0%.
W1: M_0=M_1=0 monopole 5212x / dipole 12x; P_0/M_0^2 = 0.0306
const to 6e-14 (quadratic form); ordering P_1 > P_0 > P_2
(P_1/P_2 = 20.71, P_0/P_2 = 6.38); robustness fixed k r0 = 0.4,
P_1/P_2 = 11.1/11.1/11.2/11.1/11.2 over r0 = 5..80 (1%); deeper-
kill lowest-l 0/1.
W2: window p = 1.953/3.968/5.973/7.974; deep-zone p = 1.982/
3.987/5.988/7.990 = 2/4/6/8.
W3: floor 6.46/6.45/6.45/6.49 (a/r0 = 0.10..0.013); leakage
P_0 ~ eps^2.11 (quadratic-form tautology).
float64 (real-time Hamiltonian sector, float-safe - declared,
NOT the P48-P50 mp kernel sector); deterministic, no RNG.
Literature: the quadrupole formula (Einstein; Landau-Lifshitz);
the centrifugal-barrier partial-wave suppression (Jackson);
P42 (the rotation no-go; the time-extended null instrument W1);
P44 (the lightcone receipt; the time-extended Williamson
machinery at 1.2e-14); P50 (the radial chains); the SHARD
record-dynamics framework (the eta scale).
```
