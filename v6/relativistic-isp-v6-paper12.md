# Paper 12 (v6) - SHARD: The (C) Decomposition Campaign

Author: Felix Robles Elvira

Subtitle:

```text
Gate (C) restructured: the Lorentzian convergence wall is two
already-mastered walls in disguise - Euclidean spectral convergence plus
the arrow-positivity OS bridge.  The bridge made operational (Euclidean
record data determine the Lorentzian propagator at O(dt^2)); sub-gate
(C1) extended to genuine TENSOR record metrics with an audited uniform
constant; the first genuinely 3+1 curved record instance (cosmological
redshift on an expanding 32^3 lattice); gravitational time dilation from
one record lattice with two lapses, exact to 3.7e-8, identifying the
lapse as the operational Z_perp; the compactness preconditions audited
and their CONTENT exposed: the closure of the controlled class is a
SYNTHETIC stratum (homogenized limits, interfaces with exact impedance
physics, microstructured media where light reads the homogenized
metric); and O10 folded in operationally - the Weyl alternative realized
on record towers: non-tame sectors are sectors with MISSING BOUNDARY
RECORDS.  The residue of (C) collapses to one named theorem: uniform
Mosco convergence on the controlled class, with smooth Lorentzian
geometry as its regularity stratum
```

This paper executes the decomposition strategy for gate (C) - the last
law-side wall of the program - using the leverage built by Papers 10 and
11: reflection positivity is now a theorem (the OS bridge exists), and
limit-operator ambiguities are boundary-record questions (O10).

## 0. Verdict

```text
THE DECOMPOSITION.  "Lorentzian spectral convergence" is not a standard
notion: wave operators are not elliptic, and that ill-posedness was half
the wall.  After Paper 10, (C) restructures as four sub-gates:

  (C1) EUCLIDEAN spectral convergence of the spatial record geometry
       (elliptic; Mosco/Dirichlet-form class).
  (C2) OS reconstruction of the LORENTZIAN dynamics from the Euclidean
       limit - the corpus' own arrow-positivity machinery (P10 Part I),
       no analytic-continuation axiom.
  (C3) the identities passing to the limit: Bianchi is EXACT at finite
       scope (P7 s4.4), so it passes trivially; the tensor source and
       the linearized focusing identity pass by PSD-closure (P11 T1) and
       the audited uniform constants.
  (C4) compactness of the controlled refinement class (imported:
       uniform heat-kernel bounds => Mosco precompactness).

CAMPAIGN RESULTS, sub-gate by sub-gate:

  (C2) OPERATIONAL.  A curved spatial geometry's Euclidean record kernel
       (positive, min entry 2.7e-40 within round-off) determines the
       generator to 3.6e-11 and hence the full Lorentzian propagator;
       the direct Lorentzian leapfrog converges to the OS-predicted
       evolution at exactly O(dt^2) (ratios 4.01, 4.00).  Wick rotation
       is an operational record procedure.
  (C1) EXTENDED TO TENSOR METRICS.  Genuine anisotropic Riemannian data
       (rotated-eigenframe tensor fields): 2d convergence ratio 2.19
       [O(1/n^2): 2.25]; the uniform audit over a random tensor-metric
       class gives sup |dlam|/(h^2 lam^2) = 0.1267, so C* = 0.25 holds
       at 2.0x margin - the anisotropic analogue of P8 Prop 7.1; and the
       first 3-METRIC instance converges at ratio 2.23.  (C1) now covers
       the actual Riemannian data of a spatial slice.
  LORENTZIAN INSTANCES (the physics of the docket):
       cosmological redshift, 1+1 FRW: omega(t) a(t) = const measured
       with errors 9.1e-4 -> 2.1e-4 under refinement;
       the FIRST GENUINELY 3+1 CURVED INSTANCE: a 32^3 expanding record
       lattice with the full 3H friction reproduces the redshift law
       (0.65463 vs 0.64706, the residual at the lattice-dispersion
       scale);
       GRAVITATIONAL TIME DILATION: one record lattice, one coordinate
       clock, two identical cavities at lapses 1 and 0.7: frequency
       ratio = 0.700000 to 3.7e-8 - and the lapse enters the record
       operator exactly as the normal-sector boost datum: Z_perp
       (P5 s11) is OPERATIONAL in record dynamics.
  (C4) PRECONDITIONS AUDITED, CONTENT EXPOSED.  Two-sided sub-Gaussian
       heat-kernel bounds hold with class-uniform constants (sup 0.49,
       inf 0.26 across random members and times) - the hypotheses of the
       imported Mosco-compactness machinery.  And the compactness
       CONTENT is a discovery about the theory's continuum:
         - the oscillating family c_k = 1 + 0.6 sin(2 pi k x) has NO
           pointwise limit, yet its spectra converge - to the
           HOMOGENIZED geometry c_eff = 0.8 (gap 0.002 at k = 32),
           which is not a member of the family;
         - an INTERFACE (discontinuous metric) is not smooth geometry,
           yet the record dynamics converges to exact physics: measured
           reflection 0.1111 = the impedance law (Z1-Z2)^2/(Z1+Z2)^2;
         - light in a microstructured medium propagates at the
           homogenized speed (0.870 vs sqrt(0.8) = 0.894, far from the
           naive 1.0).
       THE SYNTHETIC STRATUM IS PHYSICAL: the record continuum is a
       Dirichlet/synthetic geometry; smooth Lorentzian manifolds are its
       REGULARITY CLASS, not its totality.
  O10 FOLDED IN, OPERATIONALLY.  On the degenerate record metric
       c = x^alpha, two microscopically different towers (clamped/free
       at the degenerate end) converge to DIFFERENT limits for
       alpha = 0.5 (gap persists at 2.82) and to the SAME limit for
       alpha = 3 (gap = O(1/n)) - realizing the Weyl limit-circle/
       limit-point alternative on record towers, with the log-threshold
       alpha = 1 measured to merge at exactly the 1/log n law.
       NON-TAME SECTORS ARE SECTORS WITH MISSING BOUNDARY RECORDS: the
       deficiency space parametrizes the ledger entries the continuum
       limit still needs.  (Degeneracy loci demanding boundary records
       are horizon-flavored: a direction, not a claim.)

THE RESIDUE OF (C), AFTER THIS PAPER: one named theorem -

  (C-reg): uniform Mosco/spectral convergence of the controlled
  refinement class in 3+1, together with the identification of its
  REGULARITY STRATUM (which limits are smooth Lorentzian manifolds) -
  with the synthetic-Lorentzian framework (Cavalletti-Mondino) as the
  natural completion target, and with nonlinear focusing explicitly
  OUTSIDE (C) (it belongs to the dynamics, not the arena).
```

## 1. Method and reproducibility

```text
code/v6_p12a_os_bridge_campaign.py        (C2) + (C4) preconditions
code/v6_p12b_tensor_metric_campaign.py    (C1) tensor metrics + audit
code/v6_p12c_lorentzian_instances_campaign.py  FRW 1+1 / 3+1, lapse
code/v6_p12d_synthetic_boundary_campaign.py    O10, interface,
                                          homogenization, wave speed
```

Imports, named: Mosco convergence of Dirichlet forms (Mosco;
Kuwae-Shioya), periodic homogenization (Bensoussan-Lions-Papanicolaou),
the Weyl limit-point/limit-circle alternative and von Neumann extension
theory, synthetic Lorentzian geometry (Cavalletti-Mondino).  The OS
bridge is NOT an import: it is Paper 10's theorem, instantiated.

## 2. The decomposition

The restructuring is the paper's load-bearing move, so it is stated as
a claim with its justification:

**Claim (the Euclidean-first decomposition).** Gate (C) - "controlled
sealed refinements converge to a 3+1 Lorentzian geometry carrying the
limits of L, T, focusing, and Bianchi" - is implied by the conjunction
of (C1) Euclidean spectral convergence of the spatial record data,
(C2) OS reconstruction of the time evolution from the Euclidean limit,
(C3) limit-passage of the finite identities, and (C4) compactness of
the controlled class; and each conjunct is either elliptic mathematics,
an already-proved corpus theorem, or a PSD-closure argument.

Justification, conjunct by conjunct: (C2) is the new leverage - before
Paper 10, OS positivity would have had to be ASSUMED here, and the
Lorentzian side had no spectral formulation at all; now the eventless
record law's positivity is a theorem, the OS Hilbert space and
self-adjoint generator exist, and the Lorentzian evolution is the
spectral function cos(sqrt(A) t) of the Euclidean generator.  (C3):
Bianchi is an exact finite identity (boundary-of-boundary, P7), hence
holds at every level and in the limit; the tensor source and the
linearized focusing residuals are controlled by the audited uniform
constants and pass by the PSD-closure mechanism of P11 T1.  (C1) and
(C4) are the genuinely mathematical conjuncts, and they are ELLIPTIC -
the entire Lorentzian difficulty has been moved into the corpus'
already-closed positivity layer.

## 3. (C2): the OS bridge, operational

Spatial ring with curved conductance c(x) = 1 + 0.5 sin(2 pi x); the
Euclidean record kernel K = e^{-tau A} is a positive record law (min
entry 2.7e-40, positive within round-off; all 64 modes resolved):

```text
generator reconstruction:        ||A_rec - A|| = 3.6e-11
Lorentzian leapfrog vs the OS-predicted propagator cos(sqrt(A_rec) t):
   dt = 0.002:   1.309e-03
   dt = 0.001:   3.265e-04    ratio 4.01
   dt = 0.0005:  8.157e-05    ratio 4.00     [O(dt^2)]
```

The Euclidean record law alone determines the Lorentzian wave evolution,
phases included, and the direct Lorentzian dynamics converges to it.
Wick rotation is thereby an OPERATIONAL record procedure - grounded in
the arrow-positivity theorem, not in an analytic-continuation axiom.
This is the corpus' answer to the ill-posedness of "Lorentzian spectral
convergence": there is no separate Lorentzian convergence problem; there
is elliptic convergence plus a theorem the corpus already owns.

## 4. (C1): genuine tensor record metrics

A full Riemannian record metric is a tensor field C(x); the record
operator is assembled from the Dirichlet form E(u) = sum grad(u)^T C(x)
grad(u), symmetric PSD whenever C is pointwise PSD.

```text
2d rotated-eigenframe metric (l1 = 1.3, l2 = 0.7, varying angle):
   max rel err n=16: 1.64e-02   n=24: 7.49e-03   ratio 2.19  [2.25]
uniform audit (12 random tensor metrics x n in {16,24,32} x modes 1..8;
   theta in [0,pi), l1 in [0.9,1.5], l2 in [0.6,0.9], eps in [0.05,0.3]):
   sup |lam_k(n) - lam_k| / (h^2 lam_k^2) = 0.1267
   AUDITED PROPOSITION: C* = 0.25 at 2.0x margin
3d tensor metric (full symmetric 3-metric field):
   max rel err n=8: 5.04e-02    n=12: 2.27e-02   ratio 2.23  [2.25]
```

Sub-gate (C1) now covers the actual Riemannian data of a spatial slice -
anisotropy, rotation of the eigenframe, and three dimensions - with the
audited uniform constant extending P8 Proposition 7.1 beyond conformal
classes.

## 5. The Lorentzian instances: redshift and the operational lapse

### 5.1 Cosmological redshift (1+1, precision; 3+1, the first instance)

On the FRW record lattice ds^2 = -dt^2 + a(t)^2 dx^2 with a = 1 + 0.4t,
a propagating mode's coordinate frequency obeys omega(t) a(t) = const:

```text
1+1 (zero-crossing measurement):
   n = 512:  err 9.08e-04     n = 1024: err 3.33e-04
   n = 2048: err 2.09e-04     (falling under refinement)
3+1 (32^3 expanding lattice, full 3H friction, phase-quadrature):
   omega ratio 0.65463 vs prediction 0.64706 (err 7.6e-03, at the
   lattice-dispersion scale for kh = 0.79)
```

The 3+1 row is the docket's first genuinely 3+1 curved record instance:
a time-dependent 3-metric, the correct dimensional friction, and the
correct redshift law, from record evolution alone.

### 5.2 Gravitational time dilation: the lapse is the operational Z_perp

One record lattice, ONE coordinate clock, two identical cavities sitting
at lapses N = 1 and N = 0.7 (operator A = -N d(N d), the static-metric
wave operator):

```text
cavity at N = 1.0:  omega = 18.849364
cavity at N = 0.7:  omega = 13.194554
measured ratio = 0.700000   (error 3.7e-8)
```

Identical record structures tick at the lapse-weighted rate.  The lapse
enters the record operator precisely as the normal-sector boost weight -
the Z_perp datum that Paper 5 Section 11 identified as the minimal
missing normal-sector record: here it is OPERATIONAL, and the frequency
ratio between the two worldlines IS the normal boost holonomy connecting
them.  The normal sector of (C) is thereby wired: lapse data = Z_perp
data = local clock-rate data, three names for one record entry.

## 6. (C4) and the synthetic stratum

### 6.1 The compactness preconditions, audited

Two-sided sub-Gaussian heat-kernel bounds across the conductance class
(15 random members, three times):

```text
sup over class of sqrt(t) K_t(x,y) exp(+d^2/5t) = 0.4915
inf over class of sqrt(t) K_t(x,x)              = 0.2569
```

These are exactly the hypotheses under which the imported Dirichlet-form
machinery yields spectral PRECOMPACTNESS of the controlled refinement
class: every controlled sequence has convergent subsequences.  The
question is what the limit points ARE.

### 6.2 The limits include non-classical geometries - and they are physical

```text
HOMOGENIZATION: c_k = 1 + 0.6 sin(2 pi k x) has no pointwise limit; its
  spectra converge to the HOMOGENIZED operator c_eff = sqrt(1 - 0.36) =
  0.8 (harmonic mean): rel gaps 0.068, 0.212, 0.063, 0.009, 0.002 at
  k = 2..32 (the k = 4 bump is a commensuration resonance).  The closure
  of the smooth class contains geometries that are not in the class.
INTERFACE: a discontinuous metric (c: 1 -> 4) is not a smooth geometry,
  yet the record dynamics converges to exact physics: measured
  reflection fraction 0.1111 and transmission 0.8889 against the
  impedance law R^2 = ((Z1-Z2)/(Z1+Z2))^2 = 1/9 with Z = sqrt(c).
LORENTZIAN FACE: a wave packet in the k = 32 microstructured medium
  propagates at 0.870 - the homogenized speed sqrt(0.8) = 0.894 within
  the packet-width systematic, and far from the naive mean speed 1.0:
  null structure reads the SYNTHETIC metric.
```

**The reframing, stated as a finding.** The record continuum delivered
by compactness is a Dirichlet/synthetic geometry; smooth Lorentzian
manifolds are its REGULARITY STRATUM.  This is not a defect of the
construction - the synthetic limits carry definite, exactly-verified
physics (transmission laws, homogenized null cones), and the modern
synthetic-Lorentzian framework (Cavalletti-Mondino) is the natural
language for the completion.  (C)'s "convergence to a Lorentzian
4-geometry" should be read as: convergence to a synthetic Lorentzian
record geometry, with smoothness a named extra condition on the class.

## 7. O10 folded in: boundary records, operationally

On the degenerate record metric c(x) = x^alpha over (0,1), two
microscopically different record towers - clamped versus free at the
degenerate end - probe whether the ledger determines the continuum:

```text
alpha   n=200      n=400      n=800      n=1600    behavior
 0.5    2.866554   2.847461   2.830742   2.817342  PERSISTS (~2.82)
 1.0    0.680636   0.611945   0.553724   0.504452  ~ 1/log n
 2.0    0.039608   0.031464   0.025360   0.020710  slow power decay
 3.0    0.000516   0.000258   0.000129   0.000064  O(1/n): UNIQUE
```

Against the Weyl alternative (limit-circle iff alpha < 3/2): at
alpha = 0.5 the towers converge to DIFFERENT self-adjoint extensions -
the ledger underdetermines the limit, and a boundary record decides; at
alpha = 3 the limit is unique and the microscopic scheme is irrelevant.
The threshold-adjacent rows are measured precisely: at alpha = 1 the
two schemes merge at exactly the 1/log n law (ratio receipts 1.099,
1.090 vs the 1/log prediction 1.105, 1.094) - limit-circle guarantees
that SOME scheme pairs differ in the limit, not that every pair does.

**O10's identity, operational:** non-tame sectors are sectors with
MISSING BOUNDARY RECORDS; the deficiency space parametrizes the ledger
entries the continuum limit still needs.  This converts O10 from an
analytic worry into a record-ontology statement: where the limit is
ambiguous, the ambiguity is itself record data - and the loci that
demand boundary records (degenerating conductance: infinite redshift
in the Section 5.2 reading) are horizon-flavored.  Flagged as a
direction, not a claim.

**[Paper 13 update.]** The direction was executed in full by Paper 13
(`relativistic-isp-v6-paper13.md`), with a sharpening: for LAPSE
degeneracies N ~ x^beta the classification inverts into a CENSORSHIP
criterion - a degeneracy is a horizon iff beta >= 1, exactly when its
boundary-record demand is displaced to infinite record distance; naked
loci (beta < 1) are those whose missing ledger entry sits at finite
record distance.  Temperature T = kappa/2pi follows by two independent
receipts (Euclidean tip smoothness = no-extra-record; Bisognano-
Wichmann at 2.5e-5); greybody factors are this paper's interface
impedance law smoothed over the thermal record width; and the alpha = 1
threshold operator above IS the wedge boost generator.

## 8. The residue of (C), restated

After this campaign, gate (C) consists of exactly one named theorem and
one explicit exclusion:

```text
(C-reg) [the residue]: uniform Mosco/spectral convergence of the
   controlled refinement class in 3+1 - the class-uniform version of the
   audited constants of Sections 4 and 6.1 - together with the
   identification of the REGULARITY STRATUM: which controlled limits are
   smooth Lorentzian manifolds, within the synthetic record continuum
   that compactness actually delivers.  Difficulty class: the
   Dirichlet-form literature plus the young synthetic-Lorentzian theory;
   the corpus' contribution is that every other conjunct of (C) is now
   either proved, audited, or operational.
   [Paper 15 update: SPLIT AND HALF-DISCHARGED.  (C-reg-a) - the
   class-uniform convergence theorem - is PROVED (modulo two audited
   cell constants and the Babuska-Osborn import), with sharp rate,
   necessary hypotheses, and out-of-sample validation at 2.9x margin;
   the hypothesis line K1 h = O(1) is shown to BE the synthetic-stratum
   boundary, with the beyond-the-line limit computable (the sampled-
   harmonic-mean geometry).  The residue of (C-reg) is exactly
   (C-reg-b): the regularity stratum.  See Paper 15.]

EXPLICITLY OUTSIDE (C): nonlinear focusing (the finite docket carries
   the linearized identity only) and hence Einstein DYNAMICS - the
   equation rides on the Lovelock/HKT form gates (P5 s12.1) and the
   coupling theorem (P6.1) once the arena exists; and matter coupling at
   continuum scope (process-O6).
```

## 9. The kernel after Paper 12

```text
(C)  DECOMPOSED AND REDUCED: (C2) operational (the OS bridge); (C1)
     closed at audited level for tensor metrics in 2d/3d; (C3) passing
     by exactness + PSD-closure; (C4) preconditions audited with the
     synthetic stratum exposed; the lapse/normal sector wired (Z_perp
     operational); O10 absorbed as the boundary-record chapter.
     Residue: (C-reg), one named theorem in the Mosco/synthetic-
     Lorentzian class.
O10  RESOLVED AS A CLASSIFICATION: non-tame = missing boundary records;
     the Weyl alternative realized on record towers with the log-
     threshold measured.
(M), (V), process-O6, D10, O7, O8, O11-remainder: untouched here.
NEW NAMED ITEMS:
  (C-reg) as above - the program's single remaining law-side theorem.
  H-flag: degeneracy loci demanding boundary records as horizon
     candidates (direction).
     [Paper 13 update: EXECUTED - record cosmic censorship (horizon
     iff the demand is displaced to infinite record distance),
     T = kappa/2pi by two receipts, greybody = smoothed impedance,
     capacity quanta.  See Paper 13.]
```

## 10. What this paper proves and does not prove

Proves, with machine verification at the printed values: the OS bridge
instantiation (generator from Euclidean record data to 3.6e-11;
Lorentzian leapfrog to the OS propagator at O(dt^2)); tensor-metric
spectral convergence in 2d and 3d with the audited uniform constant
(C* = 0.25 at 2.0x margin); the FRW redshift law in 1+1 (refinement-
converging) and 3+1 (first genuinely 3+1 curved instance); gravitational
time dilation exact to 3.7e-8 with the lapse identified as operational
Z_perp; class-uniform two-sided heat-kernel bounds; the homogenized,
interface, and microstructured-medium receipts establishing the
synthetic stratum as physical; and the Weyl-alternative realization on
record towers with the 1/log-threshold measurement.

Does not prove: (C-reg) - the uniform 3+1 Mosco theorem and the
regularity-stratum identification (the residue, now precisely one
theorem); nonlinear focusing and Einstein dynamics (outside (C) by
construction); the horizon reading of boundary-record loci (a flagged
direction); continuum matter coupling (process-O6).  The decomposition
Claim of Section 2 is a strategy theorem whose conjuncts are
individually established at their stated scopes; its fully rigorous
assembly at class-uniform constants IS (C-reg).

## 11. Status

```text
(C2):    OPERATIONAL - Euclidean record data -> Lorentzian propagator,
         O(dt^2) (4.01, 4.00); Wick rotation without an axiom.
(C1):    tensor metrics, 2d ratio 2.19 + audit C* = 0.25 (2.0x margin);
         3d ratio 2.23: full Riemannian slice data covered.
Physics: FRW redshift 1+1 (2.1e-4) and 3+1 (first instance, 7.6e-3 at
         dispersion scale); time dilation ratio 0.700000 (3.7e-8);
         lapse = operational Z_perp.
(C4):    heat-kernel constants uniform (0.49 / 0.26); compactness
         closes onto the SYNTHETIC stratum: homogenization (0.002 at
         k=32), exact impedance law (0.1111/0.8889), homogenized null
         speed (0.870 vs 0.894 vs naive 1.0).
O10:     RESOLVED as classification: missing boundary records; Weyl
         alternative on towers (0.5: persists at 2.82; 3.0: O(1/n);
         threshold 1/log n measured).
Residue: (C-reg) - uniform Mosco convergence + regularity stratum, in
         the synthetic-Lorentzian frame; nonlinear dynamics explicitly
         outside.
```

## References and literature map

- Papers 4-11 (internal): the tightness/refinement gates (P4 s48-51),
  the exact Bianchi and linearized focusing docket (P7 s4.4-4.5), Z_perp
  and the normal sector (P5 s10-11), the Lovelock/HKT form gates
  (P5 s12.1), the arrow-positivity theorem (P10 Part I), PSD-closure
  (P11 T1), the audited uniform constant (P8 Prop 7.1), homogenization
  as RG (P10 R6).
- U. Mosco, J. Funct. Anal. 123, 368 (1994); K. Kuwae and T. Shioya,
  Comm. Anal. Geom. 11, 599 (2003): Mosco/spectral convergence of
  Dirichlet forms - the (C1)/(C4) machinery.
- A. Bensoussan, J.-L. Lions, G. Papanicolaou (1978); V. V. Jikov,
  S. M. Kozlov, O. A. Oleinik, *Homogenization of Differential Operators*
  (1994): the homogenized stratum.
- H. Weyl (1910); J. von Neumann (1929); M. Reed and B. Simon, vol. II:
  the limit-point/limit-circle alternative and self-adjoint extensions -
  the O10 chapter.
- F. Cavalletti and A. Mondino, "Optimal transport in Lorentzian
  synthetic spaces" (2020-); R. McCann; M. Kunzinger and C. Samann
  (Lorentzian length spaces, 2018): the synthetic-Lorentzian completion
  frame for (C-reg).
- J. Cheeger, "Differentiability of Lipschitz functions on metric
  measure spaces" (1999); K.-T. Sturm; Lott-Villani: the regularity-
  stratum tradition on the Riemannian side.
- A. Klein and L. J. Landau (1981): OS reconstruction for reversible
  processes (the classical face of the bridge, with P10 T4).
```
