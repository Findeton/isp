# Paper 50 (v6) - SHARD: Spherical Screens - the First Law on Balls, the Conformal Weight Recognized, and a Departure in the Angular Sector (FULL VERSION)

Preprint, not peer reviewed, version 2026-06-13.  FULL VERSION
- the full $l_c$-swept area coefficient now CONVERGES (FORK D
resolved: $a \to$ Srednicki's 0.295 with no fitted tail, so
$U_G = 1$ within method systematics $\sim 10^{-3}$, straddling
unity; code/v6_p50_full_lc_campaign.py) and the angular
departure is decomposed and attributed to the centrifugal
profile (code/v6_p50_full_qldecomp_campaign.py); the remaining
parallel harness is a tooling-only successor.

Author: Felix Robles Elvira

Subtitle:

```text
The planar scope closed (P44/P48/P49: energy and momentum
price by the boost law, sector-universal, G = 1/(4 nu)).  P50
opens the SPHERICAL scope - registered NOT-claimed since P44 -
by partial-wave reduction: a 3+1 massless scalar becomes a
tower of radial chains K_l = tridiag(2,-1,-1) + diag(l(l+1)/r^2),
the ball of radius R is the inner block [0, R), and the ball
entropy is S_ball = sum_l (2l+1) S_l(R).  THREE-LEVEL
DISCIPLINE held (the P49 lesson - identity never masquerades
as physics):
RESULT 1 - THE WEIGHT IS RECOGNIZED (the unification): the
finite-box ball's conformal first-law weight has a CLOSED FORM,
w_ball(r;R,L) = (2L/pi) sin(pi(R-r)/2L) sin(pi(R+r)/2L)
/ sin(pi R/L) - and it is the SAME OBJECT as P44's two-wall
g_box (g_box(R-r; N-R, N)*d): an exact algebraic identity (one
expression in two parameterizations; the 2.2e-16 is the float
evaluation of the reparameterization, a recognition, not an
independent cross-check).  Its L -> infinity limit is the
Casini-Huerta weight (R^2-r^2)/(2R) (4.9e-10) - a GENUINE
analytic limit (real content, unlike the reparameterization).
P48's "finite-box residual" was the spherical conformal weight
all along; the strip's two-wall correction and the ball's
curvature weight are literally one formula.
The s-wave reduction is an exact identity (K-MIRROR, rel 0.0
in mp): the l = 0 ball block is the mirror image of the planar
wedge, so s-wave ball completion AT FIXED N is P48's planar
completion re-expressed - declared, not sold as new physics.
RESULT 2 - THE S-WAVE FIRST LAW COMPLETES ON BALLS, including
the NEW DEEP-PROBE REGIME: r_sph = dK_exact / [2 pi sum_r
w_ball(r) dT00(r)] = 1.0020 / 1.0028 / 1.0035 at d/R =
0.25/0.50/0.75 (N = 192, mp floor-converged, leakage exactly
0.0) - strict on centrals at the declared R_eff = R + 1/2.
The deep d/R = 0.75 probe reaches the O(1) two-wall regime
NEVER accessed planarly (P48 lived at the percent-level second
wall); it completes.  The dominant systematic is the spherical
offset R_eff in {R, R+1/2, R+1} (4.9% at the deep probe,
shrinking with depth).
RESULT 3 - G IS GEOMETRY-UNIVERSAL AT MATCHED REGULATOR
(FORK D RESOLVED: CONVERGED, full version): G = 1/(4 nu)
cancels in every kernel ratio, so the coupling lives in the
capacity AREA DENSITY nu_A = S/A.  The ball area law
S_ball(R) = a R^2 + ... has area coefficient a determined by
the FULL l_c-SWEEP (code/v6_p50_full_lc_campaign.py): the
explicit-only a converges 0.047/0.167/0.248/0.280/0.291/0.294/
0.2950/0.29531 at l_c = 40/80/160/320/640/1280/2560/5120 with
GEOMETRICALLY-shrinking increments (ratio -> 0.286), the last
increment 2.7e-4 < 1e-3 (the l-SUM is EXPLICITLY CONVERGED, no
fitted tail); a geometric Richardson step gives a_inf = 0.29542
== Srednicki's coefficient 0.295 (the explicit a(5120) = 0.29531
already agrees to 4e-4).  Then nu_sph = a_inf/(4 pi) = 0.023509
and the planar transverse-momentum integral on the same chain
gives nu_planar = 0.023514, so U_G = nu_sph/nu_planar = 0.99978
(Richardson) or 0.99940 (explicit a).  HONESTY on the U_G
precision: the nu_sph/Richardson axis is rock-stable, but
nu_planar carries a k-integral CUTOFF systematic that DOMINATES
the U_G band -- sweeping kmax = 10..40 gives U_G =
0.99925/0.99978/1.00022/1.00038/1.00050, a band ~1.3e-3 that
STRADDLES 1.  So the honest claim is U_G = 1 within method
systematics (~1e-3), with U_G straddling unity -- which still
firmly establishes GEOMETRY-UNIVERSALITY (the early version's
0.9988 leaned on a fitted tail; the converged l_c-sweep replaces
it), but is NOT a 5-digit determination.  The l_c-CONVERGENCE of
a (FORK D's actual content) is genuine and orthogonal to this
nu_planar-cutoff axis.  PRECISION (per the corpus rule):
the entanglement entropy is FLOAT-SAFE -- unlike the modular
kernel F(nu)=log((nu+1/2)/(nu-1/2)), the entropy has no
near-vacuum divergence (as nu->1/2, (nu-1/2)log(nu-1/2)->0) --
VERIFIED by mpmath dps-80 anchors agreeing with float64 to
~1e-9, so the l_c-sweep runs float-safe (the rule honored by
proof, not assumption).  This also closes the prerequisite
(converged nu) for Paper 53's S3 coefficient cross-check.  The
sphere even
rediscovers the offset: the area fit's measured delta =
b/(2a) = 0.582 ~ +1/2.  THE BARE-NU CROSS-REGULATOR
COMPARISON IS DECLARED MEANINGLESS: nu_planar(radial) = 0.0235
vs P44's nu_inf = 0.0242620 (square transverse lattice) differ
by the regulator, not the coupling - only U_G at matched
regulator is the kill (the march-design directive, as a
receipt).
THE HEADLINE - A REAL DEPARTURE IN THE ANGULAR SECTOR (NOT a
comparator artifact): the centrifugal term l(l+1)/r^2 IS the
angular-gradient energy density (P49 priced kinetic =
radial-gradient; this is the THIRD component).  The double
ratio q_l = r_sph(l) / r_planar(local mass) comes back below 1,
FLOOR-CONVERGED - the sphere's angular response is NOT the
constant-mass planar comparator's.  THE DECISIVE TEST: does
ANY reasonable local mass restore universality?  Run across
FOUR comparator masses - screen l(l+1)/R_eff^2, probe-local
l(l+1)/r0^2, and the centrifugal potential AVERAGED over the
energy profile and over the probe - q_1 stays in [0.825,
0.912], every value below 0.97.  No reasonable mass restores
it: the angular departure is NOT a comparator-mass artifact;
flat-screen universality is BROKEN in the angular sector at
this scope - the first such departure in the corpus.  WHAT IS
OPEN is the MAGNITUDE, not the reality: the screen-mass 0.912
is the most-generous (smallest-mass) endpoint, the r-averaged
masses sit lower (~0.83), so the curvature-vs-centrifugal-
profile DECOMPOSITION (which sets the magnitude) is the
registered question.  The out-of-window trend confirms the
direction: at l = 4 all four masses cluster tightly at ~0.74.
NOT claimed: tensor components, Lorentzian dynamics, radiation;
the angular departure's interpretation; the full l_c-swept
area systematic; the box / two-R / convention-sweep anchor
expansion; anything beyond this early pass's quoted floors.
```

## 0. Question, route, instruments

The energy (P48) and momentum (P49) sectors closed at *planar*
scope: coherent perturbations of the chain vacuum obey the
boost law, completing to the two-wall BW target $g_{\rm box}$
with capacity coupling $G = 1/(4\nu)$, sector-universal.  The
*spherical* scope has been registered NOT-claimed since P44.
P50 opens it.

**The route.**  A $3+1$ massless scalar decomposes into
partial-wave radial chains $K_l = \mathrm{tridiag}(2,-1,-1) +
\mathrm{diag}\big(l(l+1)/r^2\big)$, $r = x+1$, Dirichlet at $r
= 0$ (the $u = r\phi$ regularity image, not a physical wall)
and $r = N+1$; the ball of radius $R$ is the inner block
$[0, R)$, and $S_{\rm ball}(R) = \sum_l (2l+1)\, S_l(R)$.

**The discipline** (P49's three-level lesson).  *Identities*
(W0, declared, never sold as measurement): the $l = 0$
reduction and the closed-form weight.  *Measurements*: the
s-wave completion (W1), the angular sector (W2), the coupling
universality (W3).  Every exact anchor carries its own floor
sweep (dps 80, floors $10^{-30}/10^{-45}/10^{-60}$, growth
gate $10^{-2}$); per-anchor leakage killed at exactly $0.0$;
the spherical offset $R_{\rm eff} \in \{R, R+\tfrac12, R+1\}$
swept; bounds floored; ledger from computed flags; bit-identical
rerun verified.

Receipts: `code/v6_p50_spherical_screens_campaign.py`,
canonical `/tmp/v6_p50_campaign.out`.

## 1. The weight is recognized (W0)

```text
  K-RAD0:  max|K_(l=0) - K_planar| = 0.0 exactly (the l=0
           chain IS the planar chain)
  THE WEIGHT: max rel|w_ball(L=N) - g_box(P44)*d| = 2.2e-16
           max rel|w_ball(L=1e6) - w_CH (R_eff=24.5)| = 4.9e-10
  K-MIRROR: mp ball pairing (mirrored-wedge analytic vs direct
           radial eigsy) rel diff = 0.0 (exact in mp)
  K-DENS:   improved-vs-chain density residual = -9.3e-4
           (consistency, honest - NOT an exact identity);
           3d-canonical offset = -pi|u|^2/R_eff at the 9% level
```

The finite-box ball's first-law weight has a closed form, and
it is **the same object as P44's two-wall $g_{\rm box}$** - an
exact algebraic identity (one expression in two
parameterizations; the $2.2\times10^{-16}$ is the float
evaluation of the reparameterization, so this is a
*recognition*, not an independent-route cross-check).  Its
continuum ($L\to\infty$) limit is the Casini-Huerta conformal
weight $(R^2-r^2)/(2R)$ - a *genuine* analytic limit (real
content, unlike the reparameterization).  The unification: the
strip's two-wall correction (P44/P48) and the ball's curvature
weight are literally *one formula*.  P48's registered
"finite-box residual" was the spherical conformal weight all
along.

The s-wave reduction is an exact identity (**K-MIRROR**, rel
$0.0$ in mp): the $l = 0$ ball block $[0, R)$ is the mirror
image of the planar wedge $[N-R, N)$, so s-wave ball
completion at fixed $N$ *is* P48's planar completion
re-expressed - declared as instrument calibration, not new
physics.  Honesty: under $w_{\rm ball}$ the chain $T_{00}$
tracks the conformally improved 3d density only to $\sim
10^{-3}$ (not exactly - the calibration measured it), so
**K-DENS is a consistency receipt with a printed residual**,
not the exact identity an earlier design step had assumed.

## 2. The s-wave first law completes on balls (W1)

Exact anchors, $N = 192$, all leakages exactly $0.0$ (K-LEAK),
float clip-14 droop receipts at identical geometry:

```text
  d/R = 0.25 (r0 = 18): float14 0.9814 | r_sph = 1.0020
    [floor +1.5e-5; R_eff offsets 14.5%]; target 1
  d/R = 0.50 (r0 = 12): float14 0.9455 | r_sph = 1.0028
    [floor +1.5e-4; R_eff offsets 7.0%]; target 1
  d/R = 0.75 (r0 =  6): float14 0.8948 | r_sph = 1.0035
    [floor +3.9e-4; R_eff offsets 4.9%]; target 1
  FORK C-s (deep probe d/R = 0.75): r_sph = 1.0035 +- 0.049;
    strict 0.03 on centrals: PASS; 1 within syst: yes
  R_eff-robustness (deep probe, R_eff = 24/24.5/25):
    r_sph = 1.0286/1.0035/0.9796 - ALL within strict 0.03
```

The s-wave first law **completes to the closed-form conformal
weight** (mp floor-converged; the float droop - 0.98/0.95/0.89
- lifts to $\sim 1.00$, exactly as in the planar campaigns).
The headline is the deepest probe: $d/R = 0.75$ reaches the
$O(1)$ two-wall regime *never accessed planarly* (P48 lived
where the second wall was a percent-level residual), and it
completes, strict on centrals - and crucially, **the deep-probe
completion is robust to the offset choice**: all three $R_{\rm
eff} \in \{R, R+\tfrac12, R+1\}$ give $r_{\rm sph}$ within
strict $0.03$ of $1$, so the completion verdict is not an
artifact of $R_{\rm eff} = R+\tfrac12$.  The spherical offset
is the dominant systematic (14.5% at the shallow probe,
shrinking to 4.9% at the deep probe where the weight is most
curved) - the analog of the planar boost-offset spread, larger
here; the shallow probe is strict *only* at $R+\tfrac12$ and is
quoted with its systematic, while the load-bearing deep-probe
claim is offset-robust.

## 3. The angular sector - a real departure, not a comparator
artifact (W2)

The centrifugal term $l(l+1)/r^2$ *is* the angular-gradient
energy density.  P49 established kinetic = radial-gradient
pricing; this tests the third component.  The double ratio
$q_l = r_{\rm sph}(l) / r_{\rm planar}(m_l)$ cancels the massive
form factor both legs carry, leaving the centrifugal shape -
and the comparator is run across **four** local-mass choices
(screen $l(l+1)/R_{\rm eff}^2$, probe-local $l(l+1)/r_0^2$, and
the centrifugal potential averaged over the energy profile and
over the probe), the decisive test of whether any reasonable
mass restores universality:

```text
  l = 1 (m_l*l_E = 0.35, in-window): r_sph = 0.9747
   q_1 (screen/probe/dT00-avg/u2-avg) =
     0.9116 / 0.8380 / 0.8254 / 0.8344  range [0.825, 0.912]
   q(screen) floor sweep 0.9122/0.9116/0.9116 (converged)
  l = 2 (m_l*l_E = 0.57, OUT-of-window): range [0.767, 0.846]
  l = 4 (m_l*l_E = 0.88, OUT-of-window): range [0.744, 0.776]
  l = 8 (m_l*l_E = 1.39, OUT-of-window): range [0.733, 0.750]
```

**A real departure, and no comparator mass restores it.**
$q_l < 1$, floor-converged - the sphere's angular response is
*not* the constant-mass planar comparator's.  The decisive
test: across all four reasonable local masses, $q_1$ stays in
$[0.825, 0.912]$, every value below $0.97$.  The centrifugal
potential does vary across the ball (so the comparator mass is
ambiguous), but **no choice of constant mass restores
universality** - so the departure is *not* a comparator-mass
artifact.  **Flat-screen universality is broken in the angular
sector at this scope** - the first such departure in the
corpus.

**The curvature-versus-centrifugal-profile decomposition
(full version, code/v6_p50_full_qldecomp_campaign.py).** The
departure is attributed to the **centrifugal-potential
PROFILE**, not the geometric curvature, by three facts that
together pin it (mp dps 80): (i) the weight is **matched** -
$q_l$ uses the conformal $w_{\rm ball}$ for *both* the sphere
and the planar comparator, so the geometric curvature is not a
free variable in $q_l$; $q_l$ isolates the centrifugal
potential.  The named residual cross-term is now *quantified*:
the diagnostic $q_{\rm weight}$ (conformal-vs-linear weighting
of the *same* $dT_{00}$ - a quantity $q_l$ never uses) drifts
only $1.350 \to 1.346 \to 1.340 \to 1.332$ across $l = 0/1/2/4$,
a $\sim 1.3\%$ $l$-dependent (profile $\times$ curvature)
coupling - and the departure $1 - q_l = 0.107/0.166/0.215$
exceeds it by $\sim 12$-$25\times$, so the **profile dominates**
and the cross-term is a bounded $\sim 1\%$ residual, not a free
ambiguity.  (ii) $l = 0$ (no centrifugal) **completes**,
$q = 1.000$ - curvature alone produces no departure; (iii) the
departure grows monotonically with the centrifugal strength
$l(l+1)$: $q_l = 0.893 / 0.834 / 0.785$ at $l = 1/2/4$
($R = 20$), and (W2) no constant mass restores it - the
*varying* potential. So the angular departure is the
radially-varying centrifugal potential's imprint on the
modular charge, with the conformal weight matched out.  This
**sharpens** the early "magnitude open" to "attributed to the
centrifugal profile"; the residual finer question is
pure-profile vs the (profile $\times$ curvature) cross-term.
The box/two-$R$ s-wave robustness is confirmed in the *ratio*
$q_l$, which is convention-independent.  A caution on the
absolute charge: the decomposition harness uses
$R_{\rm eff} = R - \tfrac12$, the *opposite* offset to the
locked W1's $R_{\rm eff} = R + \tfrac12$, so its bare
$r_{\rm sph}(l=0) = 1.26/1.13/1.08$ at $R = 16/20/24$ sits
*above* 1 (rather than W1's $1.002$); this $R_{\rm eff}$
offset cancels in $q_l = r_{\rm sph}/r_{\rm planar}$ (both legs
share it), so the decomposition is unaffected.  What the
harness adds is the box-size stability: at $R = 24$,
$r_{\rm sph}(l=0)$ agrees to $0.2\%$ between $N = 96$ and
$N = 144$, and the bare charge trends toward 1 as $R$ grows -
the s-wave completion (whose matched-$R_{\rm eff}$ value
$\approx 1.002$ is W1's).  The
out-of-window trend confirms the direction and tightens with
$l$: at $l = 4$ all four masses cluster at $\sim 0.744$
(range $0.032$ wide), the departure becoming mass-robust as
the angular gradient grows.  At this geometry only $l = 1$
sits in the hydrodynamic window ($m_l\ell_E < 0.5$); $l =
2/4/8$ are out-of-window species rows, the trend.  The early
version names a genuine effect and registers its open
magnitude - it does not overclaim the decomposition.

## 4. G is geometry-universal at matched regulator (W3)

$G = 1/(4\nu)$ cancels in every kernel ratio, so the coupling
lives in the capacity *area density* $\nu_A = S/A$.  The ball
area law (float64; entropy is float-safe, the complement of
the kernel's float wall):

```text
  S_ball(R) = a R^2 + b R + c (R = 8..24, l-sum EXPLICIT to
   l_c = 5120, NO fitted tail): a(5120) = 0.29531, Richardson
   a_inf = 0.29542 (Srednicki 0.295)
  nu_sph = a_inf/(4 pi) = 0.023509
  nu_planar = (1/2pi) Int k S(k;R) dk (same chain, kmax=12) = 0.023514
  U_G = nu_sph/nu_planar = 0.99978 (Richardson) / 0.99940 (explicit)
  l_c convergence: explicit a CONVERGES 0.047/0.167/0.248/0.280/
   0.291/0.294/0.2950/0.29531 at l_c = 40..5120, last increment
   2.7e-4 < 1e-3 (FORK D RESOLVED: converged, no fitted tail)
  U_G systematic: nu_planar kmax-sweep 10..40 -> U_G =
   0.99925..1.00050 (band ~1.3e-3, STRADDLES 1, nu_planar-cutoff
   dominated); U_G = 1 within systematics -> geometry-universal
  measured offset delta = b/(2a) = 0.58 ~ +1/2
  bare-nu: nu_planar(radial) = 0.0235 vs P44 nu_inf = 0.0242620
   - DIFFERENT REGULATOR, comparison DECLARED MEANINGLESS
```

The capacity coupling is **geometry-universal**: the sphere's
area-law $\nu$ matches the planar transverse-momentum-integral
$\nu$ on the same chain machinery, $U_G = 1$ within method
systematics ($\sim 10^{-3}$).  The full $l_c$-sweep (Result 3,
above) settled this: the explicit area coefficient $a$
*converges* to Srednicki's $0.295$ with no fitted tail (last
increment $2.7\times10^{-4}$ at $l_c = 5120$), giving
$\nu_{\rm sph} = 0.023509$; the residual $\sim 10^{-3}$ $U_G$
band is the $\nu_{\rm planar}$ $k$-integral cutoff (under which
$U_G$ *straddles* unity, $0.99925$-$1.00050$), not a failure of
$a$ to converge.  The sphere even rediscovers the offset
convention ($\delta = 0.58 \sim +\tfrac12$).  And the coupling-universality kill is
stated as
the march design directed: the *bare* $\nu$ comparison across
regulators (radial $0.0235$ vs P44's square-lattice
$0.0242620$) is **declared meaningless** - they differ by the
cutoff, not the physics; only $U_G$ at matched regulator is
the receipt.

## 5. Ledger and verdict

```text
  K-RAD0   l=0 chain == planar (0)            -> did not fire
  K-MIRROR ball == mirrored wedge (0, mp)     -> did not fire
  K-DENS   improved-vs-chain residual -9e-4 (consistency, honest)
  K-LEAK   every anchor leakage 0.0           -> did not fire
  K-FLOOR  W1 growth <= 1e-2                  -> did not fire
  THE WEIGHT w_ball == P44 g_box (2e-16); CH = L->inf (5e-10)
  W1 s-wave: r_sph = 1.002/1.003/1.003 at d/R = 0.25/0.50/0.75
    -> FORK C-s: COMPLETION (deep probe strict, R_eff-robust:
    1.0286/1.0035/0.9796 all within 0.03)
  W2 angular: q_1 in [0.825, 0.912] across 4 comparator masses,
    all < 0.97 -> FORK B: DEPARTURE, no mass restores
    universality (real, NOT an artifact); decomposition (full
    version) attributes it to the CENTRIFUGAL PROFILE (weight-
    matched, l=0 completes, grows with l(l+1)); cross-term ~1.3%
  W3 G: U_G = 1 within systematics ~1e-3 (FORK D RESOLVED: a
    l_c-CONVERGED 0.047..0.29531 at l_c 40..5120, no fitted tail,
    Richardson a_inf=0.29542=Srednicki; U_G straddles 1 under the
    nu_planar kmax-sweep 0.99925..1.00050); delta = 0.58 ~ +1/2;
    bare-nu cross-regulator declared meaningless
  REGISTERED (early -> successor): the angular departure's
    MAGNITUDE / curvature-vs-profile decomposition (the
    comparator-mass sweep); the full l_c-swept area systematic;
    box / two-R / convention-sweep anchors; the parallel
    harness; tensor / Lorentzian / radiation scopes
```

**Verdict (early).**  The spherical scope opens with one
recognition, two completions, and one genuine departure.  *The
weight is recognized*: the ball's finite-box conformal weight
is the same formula as P44's two-wall $g_{\rm box}$ (an exact
reparameterization), with the Casini-Huerta weight its genuine
continuum limit - P48's "finite-box residual" was the
spherical conformal weight all along.  *The s-wave first law
completes on balls*, including the deep $d/R = 0.75$ regime
never reached planarly, strict on centrals and robust to the
offset choice.  *G is geometry-universal* at matched regulator
($U_G = 1$ within method systematics $\sim 10^{-3}$, $a$ now
$l_c$-converged in the full version, straddling unity under the
$\nu_{\rm planar}$ cutoff), with the bare-$\nu$
cross-regulator comparison declared meaningless as the march
design directed.  And *the angular sector shows a real
departure* from flat-screen universality: $q_l$ stays in
$[0.825, 0.912]$ across every reasonable comparator mass, so
the departure is **not a comparator artifact** - the first
measured break from flat-screen universality in the corpus,
with its magnitude (the curvature-versus-profile decomposition)
the registered open question.  For the gravitational ledger:
*at first-law scope, the ledger prices a ball by the conformal
weight that is the curvature face of P44's two-wall correction,
with the same capacity coupling $G = 1/(4\nu)$ - geometry-
universal in the radial and s-wave sectors, and genuinely
DIFFERENT in the angular sector (a real departure, its
magnitude open).*  NOT claimed: tensor components, Lorentzian
dynamics, radiation; the angular departure's magnitude /
curvature-vs-profile decomposition; the full $l_c$ systematic;
anything beyond this early pass's quoted floors.

## Receipts

```text
code/v6_p50_spherical_screens_campaign.py  the campaign (EARLY)
/tmp/v6_p50_campaign.out                   canonical
W0: K-RAD0 0.0; w_ball==g_box 2.2e-16; CH limit 4.9e-10;
K-MIRROR 0.0 (mp); K-DENS -9.3e-4; 3d-canon 9%.
W1: r_sph 1.0020/1.0028/1.0035 at d/R 0.25/0.50/0.75
(floors 1.5e-5/1.5e-4/3.9e-4; R_eff offsets 14.5/7.0/4.9%;
float14 0.9814/0.9455/0.8948).
W2: q_1 over 4 masses (screen/probe/dT00-avg/u2-avg) =
0.9116/0.8380/0.8254/0.8344, range [0.825, 0.912] (all < 0.97;
screen floor sweep 0.9122/0.9116/0.9116); l=2/4/8 ranges
[0.767,0.846]/[0.744,0.776]/[0.733,0.750].
W1 R_eff-robustness (deep probe): 1.0286/1.0035/0.9796 all
within strict 0.03.
W3 (full version): a converges to a_inf = 0.29542 (explicit
a(5120) = 0.29531, l-sum to l_c = 5120, no fitted tail),
nu_sph = 0.023509, nu_planar = 0.023514 (kmax=12), U_G = 0.99978
(Richardson) / 0.99940 (explicit); FORK D RESOLVED, U_G = 1
within ~1e-3 systematics (nu_planar kmax-sweep straddles 1,
0.99925..1.00050); delta = 0.58; bare-nu 0.0235 vs P44 0.0242620.
q_l decomposition: angular departure attributed to the
centrifugal profile (weight-matched; l=0 completes q=1.000;
q_l = 0.893/0.834/0.785 grows with l; cross-term ~1.3%).
Reproduction note: the floor clamp nu = 1/2 + floor needs
working precision beyond the floor's digits (dps 80 over
floors to 1e-60); at dps <= 60 the 1e-60 clamp underflows.
EARLY-VERSION SCOPE: a first complete pass for review; the
anchor expansion, full l_c systematic, and parallel harness
are declared successors.
Literature: Bisognano-Wichmann; Casini-Huerta (the ball
modular Hamiltonian); Casini-Huerta-Myers; Cardy-Tonni
(strip-to-circle doubling); Srednicki (the area law); P44
(the two-wall g_box and nu_inf); P48 (the energy sector and
the finite-box completion); P49 (the sector-universality
discipline and the three-level architecture).
```
