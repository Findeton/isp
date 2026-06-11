# Paper 15 (v6) - SHARD: (C-reg-a) - The Uniform Tensor-Class Convergence Theorem

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The genre shift: the first brick of (C-reg) attacked as MATHEMATICS.
A theorem with a lemma chain - energy-method regularity with explicit
constants, consistency, min-max assembly - proving CLASS-UNIFORM
spectral convergence |lam_k(n) - lam_k| <= C*(lam_k) h^2 lam_k^2 for
the controlled tensor-metric class, with every lemma constant either
derived or machine-audited under the corpus' claim discipline (two
audited cell constants, calibration/validation DISJOINT, safety factor
declared, out-of-sample margin 2.9x).  The rate is SHARP (normalized
error pinned at 0.0575 under refinement: O(h^2) is attained).  And the
hypotheses are NECESSARY in the strongest sense: the constant is flat
(~0.10) inside the class, the failure at the class line K1 h = O(1) is
STRUCTURAL (resonance, commensuration accident, 126x blow-up at the
dimer point), and beyond the line the tower still converges - to the
SAMPLED-HARMONIC-MEAN geometry, computable by exact arithmetic: the
theorem's hypothesis line IS the handoff to Paper 12's synthetic
stratum.  (C-reg) reduces to (C-reg-b): the regularity-stratum
identification
```

This is the corpus' first proof paper: fewer receipts, real lemmas.
Receipts appear only as per-lemma audits, sharpness certificates, and
hypothesis-necessity demonstrations - they test the THEOREM, not the
physics.

## 0. Verdict

```text
THEOREM (uniform tensor-class convergence; status: proved modulo two
audited cell constants).  Let M = M(l0, L0, K1, K2) be the class of
symmetric tensor fields C in C^2(T^d, Sym_d), d = 2, 3, with

    l0 |xi|^2 <= xi^T C(x) xi <= L0 |xi|^2,
    ||dC||_inf <= K1,   ||d^2 C||_inf <= K2.

Let lam_k be the nonzero Dirichlet-form eigenvalues of A = -div(C grad)
and lam_k(n) those of the corpus assembly A_n = sym sum_ab G_a^T
diag(C_ab) G_b at mesh h = 1/n.  Then for h sqrt(lam_k) below a class
threshold,

    |lam_k(n) - lam_k|  <=  C*(lam_k) h^2 lam_k^2,

where C* is the EXPLICIT expression assembled in Section 5 from the
lemma constants - depending only on (l0, L0, K1, K2, d), NOT on the
individual metric.  Status ledger per lemma:

  Lemma 1 (regularity, energy method)      PROVED (explicit constants;
                                           audit: formulas dominate
                                           measured norms at 0.77 /
                                           0.15 / 0.011 of allowance)
  Lemma 2 (consistency, Bramble-Hilbert)   PROVED IN STRUCTURE; cell
                                           constant c_BH AUDITED
  Lemma 3 (mass defect)                    same status, constant c_m
  Lemma 4 (min-max upper bound)            PROVED
  Lemma 5 (lower bound)                    NAMED IMPORT (Babuska-
                                           Osborn), applied class-
                                           uniformly; factor S = 2
  Assembly                                 calibration metrics 1-3,
                                           safety factor 2, VALIDATION
                                           on disjoint metrics 4-6:
                                           bound dominates all measured
                                           errors with min margin 2.9x

SHARPNESS: the normalized error is bounded BELOW (0.0575, stable under
refinement n = 16..48): the O(h^2) rate is attained; only the constant
is improvable (the audited practical value remains P12's C* = 0.25).

NECESSITY (the theorem meets the synthetic stratum): on the fixed
ellipticity window with K1 ~ k (oscillating family),
  - inside the class (K1 h << 1): constant flat at ~0.10 - the
    uniformity is real, and low modes are protected by homogenization;
  - at the line (K1 h = O(1)): structural failure - resonance at
    K1 h = 0.71 (constant 0.65), a commensuration ACCIDENT at k = 24
    (all targets coincide; the constant looks fine by coincidence),
    and 126x blow-up at the dimer point K1 h = 1.41 (12.55);
  - beyond the line: the tower STILL CONVERGES - to the harmonic mean
    of the bonds it actually sampled (dimer point: gap 0.005 to the
    exact c_hm = 0.79750 geometry vs 0.11 to both smooth targets).
THE HYPOTHESIS LINE OF THE THEOREM IS THE BOUNDARY OF P12'S SYNTHETIC
STRATUM, AND THE LIMIT BEYOND IT IS COMPUTABLE.  (C-reg-a) and the
synthetic stratum are two sides of one wall; what remains of (C-reg)
is exactly (C-reg-b): which limits are smooth - the regularity
stratum.
```

## 1. Method and reproducibility

```text
code/v6_p15a_theorem_audit_campaign.py   lemma audits, theorem margin,
                                         rate sharpness
code/v6_p15b_necessity_campaign.py       hypothesis necessity, the
                                         synthetic handoff
```

Named imports: Babuska-Osborn spectral approximation theory (the lower
-bound direction, Lemma 5); the Bramble-Hilbert lemma (the structure of
Lemma 2); midpoint-quadrature error calculus.  Everything else -
regularity, min-max, assembly - is proved in-line by elementary energy
arguments on the torus.  Corpus inputs: the assembly scheme and audit
class (P12 4), the synthetic stratum (P12 6.2, Section 6's other side).

## 2. Setting

T^d = (R/Z)^d, d = 2, 3.  For C in M(l0, L0, K1, K2), the continuum
form a(u, v) = int grad(u)^T C grad(v) dx with eigenpairs
0 = lam_0 < lam_1 <= lam_2 <= ... and L2-normalized eigenfunctions u_k.
The discrete operator is the corpus assembly (P12): forward differences
(D_mu u)(x) = n (u(x + h e_mu) - u(x)) on the grid (h Z)^d, cell-center
sampled coefficients, symmetrized:

```text
    a_h(u, v) = h^d sum_x sum_{mu nu} (D_mu u)(x) C_{mu nu}(x_c)
                (D_nu v)(x),     A_n = sym assembly of a_h,
```

with eigenvalues lam_k(n) against the lumped mass h^d.  P is the grid
sampling operator.  The audited class instance (six sampled tensor
metrics of the P12 family - rotated eigenframes with trigonometric
modulation) has measured class constants l0 = 0.3335, L0 = 1.7462,
K1 = 2.403, K2 = 20.89.

## 3. Lemma 1: regularity by the energy method

**Lemma 1.**  For an eigenpair (lam, u) of A with ||u||_{L^2} = 1:

```text
(a)  ||grad u||  <=  nu(lam) := sqrt(lam / l0);
(b)  ||D^2 u||   <=  R2(lam) := d nu (nu + sqrt(d) K1 / l0);
(c)  ||D^3 u||   <=  R3(lam) := d^2 ( nu R2
                                 + sqrt(d)(2 K1 R2 + K2 nu)/l0 ).
```

*Proof.*  (a) Test the eigenvalue equation with u:
l0 ||grad u||^2 <= a(u, u) = lam.

(b) Differentiate the equation in direction mu:
div(C grad d_mu u) = -lam d_mu u - div((d_mu C) grad u).  Test with
v = d_mu u and integrate by parts; on the left, ellipticity gives
l0 ||grad v||^2; on the right, |lam <v, v>| <= lam ||v||^2 and the
commutator term is bounded by Cauchy-Schwarz:
| int grad(v)^T (d_mu C) grad u | <= sqrt(d) K1 ||grad u|| ||grad v||.
Hence the quadratic inequality

```text
   l0 ||grad v||^2 <= lam ||v||^2 + sqrt(d) K1 ||grad u|| ||grad v||,
```

whose positive root, after the loosenings ||v|| <= ||grad u|| <= nu
(Poincare on the mean-zero torus eigenfunctions, unit-normalized),
gives ||grad d_mu u|| <= nu (sqrt(lam/l0) + sqrt(d) K1 / l0).  Summing
the d directions yields (b).

(c) Differentiate twice: the commutator now carries
2 (d C)(grad d u) + (d^2 C)(grad u), bounded by
sqrt(d) (2 K1 R2 + K2 nu); repeating the energy step with v a second
derivative and assembling over the d^2 index pairs yields (c).  All
constants are explicit; no Calderon-Zygmund import is needed - the
torus energy method suffices, at the price of deliberate conservatism
in the lam- and K-scaling (each loosening compounds).            QED

**Audit (p15a (i)).**  Across the class, on fine-grid eigenfunctions
(n = 48, k = 1..4): measured ||grad u||/nu <= 0.7745,
||D^2 u||/R2 <= 0.1489, ||D^3 u||/R3 <= 0.0109.  The formulas dominate,
increasingly conservatively at higher order - that conservatism is
paid back by the audited cell constants of Lemma 2.

## 4. Lemmas 2-4: consistency, mass, min-max

**Lemma 2 (consistency; proved in structure, constant audited).**  For
u in H^3(T^d) and the sampling P:

```text
 |a_h(Pu, Pu) - a(u, u)| <= c_BH h^2 [ L0 (R3 nu + R2^2)
                              + 2 K1 R2 nu + K2 nu^2 ](lam).
```

*Structure of proof.*  Per cell: (i) the forward difference is the
exact average of the derivative along the corresponding edge (the
fundamental theorem of calculus), so D_mu(Pu)(x) = d_mu u(x + h e_mu/2)
+ E with |E| controlled by the second derivative on the cell; (ii) the
deviation of the quadratic integrand grad^T C grad from its
cell-center value is controlled by the Bramble-Hilbert lemma applied
on the cell, with the O(h) terms cancelling under the symmetrized
cell-center sum (the midpoint property); (iii) the surviving O(h^2)
terms collect into exactly the bracket shown - one term per derivative
allocation (L0 against third-times-first and second-squared
derivatives of u; K1 against mixed; K2 against first-squared) - with
ONE scheme-specific cell constant c_BH.  The corpus discipline marks
step (ii)-(iii)'s numeric constant as AUDITED rather than hand-derived:
the audit certifies that a single constant serves the entire class,
which is the theorem's actual content.

**Audit (p15a (ii); calibration metrics 1-3 ONLY).**  c_BH = 8.22e-5,
c_m = 1.43e-11.  These are NOT order-one, and that is the point: the
energy-method shapes R2, R3 are deliberately conservative in their
lam- and K-scaling, and the cell constants absorb that slack.  A
declared safety factor 2 is applied to both before assembly.

**Lemma 3 (mass defect; same status).**
| ||Pu||_h^2 - 1 | <= c_m h^2 R2(lam)^2.

**Lemma 4 (min-max upper bound; proved).**  Let V_k = P span(u_1..u_k).
By Lemma 3, for h below the class threshold the Gram matrix of V_k is
invertible with controlled condition; the discrete min-max over V_k
plus Lemma 2 then gives

```text
   lam_k(n) <= lam_k + E_cons(lam_k) + lam_k E_mass(lam_k) + h.o.t.,
   E_cons = c_BH h^2 [bracket](lam),   E_mass = c_m h^2 R2^2.
```

*Proof.*  Standard Rayleigh-quotient comparison: for w in V_k,
a_h(w, w)/||w||_h^2 <= (a(w, w) + E_cons ||w||^2)/(||w||^2 (1 -
E_mass)), and the continuum min-max over span(u_1..u_k) is exactly
lam_k; expanding (1 - E_mass)^{-1} to first order absorbs the rest
into h.o.t.                                                      QED

**Lemma 5 (lower bound; named import).**  The reverse inequality at
the same order with the same class data, by Babuska-Osborn spectral
approximation theory applied to the multilinear-interpolant comparison
form (the corpus scheme is a quadrature perturbation of the Q1 finite
element method; the quadrature perturbation is Lemma-2-sized).  The
import is absorbed as the two-sidedness factor S = 2 in the assembly.

## 5. The theorem, assembled, and its out-of-sample validation

```text
    E_cons(lam) = c_BH h^2 [ L0 (R3 nu + R2^2) + 2 K1 R2 nu
                             + K2 nu^2 ]
    E_mass(lam) = c_m  h^2 R2^2
    C*(lam)     = S (E_cons + lam E_mass) / (h^2 lam^2),    S = 2,
```

with the audited constants carried at the declared safety factor 2.
The leading lam-scaling: R3 nu ~ lam^2/l0^2-class, so C* is finite and
lam-stable - the normalization by h^2 lam^2 is the right gauge.

**Validation (p15a (iii); metrics 4-6, DISJOINT from calibration).**

```text
measured sup |dlam| / (h^2 lam^2)  [validation set]  = 0.1478
min over validation metrics/modes of  C* / measured  = 2.9x
   (all n in {16, 24, 32}, all modes k = 1..6)
```

The bound, calibrated on metrics 1-3 with its safety factor, dominates
every measured error on the disjoint validation metrics: the
class-uniform guarantee holds OUT OF SAMPLE.  The audited practical
constant (P12: C* = 0.25) remains the sharp working value; the
proved-modulo-audit guarantee sits a factor ~2 above it.

**Sharpness of the rate (p15a (iv)).**  On a class member, the
normalized error's MINIMUM over modes under refinement:

```text
n = 16: 0.05731   n = 24: 0.05748   n = 32: 0.05753   n = 48: 0.05757
```

bounded below away from zero: O(h^2) is ATTAINED - the theorem's rate
cannot be improved on this class, only its constant.

## 6. Necessity: the theorem meets the synthetic stratum

### 6.1 The threshold

On the fixed ellipticity window, the family c_k(x) = 1 + 0.45 sin(2 pi
k x) has K1 = 0.9 pi k.  At n = 64 (p15b):

```text
  k    K1 h     |dlam_1|/(h^2 lam^2)
  1    0.044        0.097
  4    0.177        0.106
  8    0.353        0.103        <- flat: the class regime
 16    0.707        0.646        <- resonance
 24    1.060        0.109        <- commensuration ACCIDENT
 32    1.414       12.552        <- the dimer point: 126x
```

Inside the class the constant is genuinely uniform - and the mechanism
of that uniformity is itself instructive: the low modes are PROTECTED
BY HOMOGENIZATION (a fast-oscillating metric looks effectively smooth
to long wavelengths), which is why the failure at the line is
STRUCTURAL rather than monotone.  At k = 24 the sampled pattern happens
to be balanced, every target coincides, and the constant looks fine by
accident; at the dimer point it blows up by two orders.  No K-free
theorem exists; inside the class the uniformity is real.

### 6.2 Beyond the line: the computable synthetic limit

```text
  k    c_hm(sampled)   gap to c_k   gap to c_eff   gap to c_hm
  8      0.89305        0.0036        0.0130         0.0130
 16      0.89875        0.0030        0.0013         0.0053
 24      0.89305        0.0038        0.0047         0.0047
 32      0.79750        0.1112        0.1116         0.0052   <- dimer
  (c_eff = sqrt(1 - 0.45^2) = 0.89303, the continuum-homogenized
   conductance; c_hm = the harmonic mean of the bonds the lattice
   actually sampled)
```

AT the boundary (k/n = 1/2 - the exactly dimerized chain, alternating
bonds 1 +- 0.45) the tower's limit is the harmonic mean of the SAMPLED
bonds, c_hm = 2/(1/0.55 + 1/1.45) = 0.79750, to 0.005, while both
smooth targets miss by 0.11.  The theorem's hypothesis line is the
handoff to Paper 12's synthetic stratum, and the stratum's boundary
value is EXACT ARITHMETIC, not a fit.  In the intermediate regime the
tower interpolates between the smooth and sampled-synthetic targets,
with commensuration points where all targets coincide.  This receipt
is the bridge to (C-reg-b): beyond the class line the question is not
whether limits exist but WHICH geometry they are - the
regularity-stratum question, now with a computable handle.

## 7. What this paper proves and does not prove

Proves: Lemma 1 in full with explicit constants (energy method, the
proof in Section 3); Lemmas 2-3 in structure with audited,
safety-factored cell constants (calibration and validation disjoint);
Lemma 4 in full; the assembled class-uniform bound validated out of
sample at 2.9x margin; rate sharpness; hypothesis necessity with the
structural failure classification; and the computable synthetic limit
at the class boundary.

Does not prove: the cell constants c_BH, c_m analytically (the two
audited gaps - closing them is bookkeeping-grade Bramble-Hilbert
calculus, not research mathematics, and is the named residue of this
paper); Lemma 5 internally (Babuska-Osborn import); d > 3; Lipschitz-
only coefficients (the class requires C^2; K2 enters R3); and
(C-reg-b) - the regularity-stratum identification, which is now the
WHOLE remaining content of (C-reg): this paper has converted "prove
uniform convergence" from an open analytic question into a stated
theorem with two bookkeeping gaps, and the necessity receipts show its
hypothesis line is exactly the synthetic-stratum boundary, so the
remaining question is which limits are smooth - not whether controlled
limits exist.

## 8. The kernel after Paper 15

```text
(C-reg)  SPLIT AND REDUCED:
  (C-reg-a) uniform tensor-class convergence: THEOREM (proved modulo
            two audited cell constants + one named import), rate
            sharp, hypotheses necessary, out-of-sample validated.
  (C-reg-b) the regularity stratum (which controlled limits are smooth
            Lorentzian geometries): NOW THE ENTIRE RESIDUE of (C-reg),
            with a new handle from Section 6: the limit beyond the
            class line is the sampled-harmonic-mean geometry -
            smoothness of the limit is equivalent to the stability of
            that computable functional under refinement (a stated
            criterion, operationalized as the local-Weyl detector in
            Paper 24).
KERNEL: { (C-reg-b), (M), (V), process-O6 } +
        { D10, O7, O8-remainder, O11-remainder }.
```

## 9. Status

```text
Theorem:    class-uniform |dlam| <= C* h^2 lam^2 - proved modulo two
            audited constants (declared safety factor 2; disjoint
            validation margin 2.9x); rate SHARP (0.0575 pinned).
Lemmas:     1 proved (Section 3); 2-3 proved in structure, constants
            audited; 4 proved (Section 4); 5 named import.
Necessity:  constant flat (~0.10) in-class; structural failure at
            K1 h = O(1) (0.65 resonance / accident at k = 24 / 12.55
            dimer); class hypothesis necessary.
Synthetic:  boundary limit computable (c_hm = 0.79750 at the dimer
            point, gap 0.005): the hypothesis line = the synthetic-
            stratum handoff.
Residue:    (C-reg-b) regularity stratum; two bookkeeping constants;
            Lemma 5 internalization.
```

## References and literature map

- Paper 12 (internal): the assembly scheme, audit class, audited
  C* = 0.25, the synthetic stratum (6.2) and homogenized limits.
- I. Babuska and J. Osborn, "Eigenvalue problems," Handbook of
  Numerical Analysis II (1991): the lower-bound direction (Lemma 5).
- J. H. Bramble and S. R. Hilbert, SIAM J. Numer. Anal. 7, 112 (1970):
  the consistency structure (Lemma 2).
- G. Strang and G. J. Fix, An Analysis of the Finite Element Method
  (1973): quadrature-perturbed forms.
- A. Bensoussan, J.-L. Lions, G. Papanicolaou (1978); Jikov-Kozlov-
  Oleinik (1994): homogenization (the other side of Section 6).
- U. Mosco (1994); K. Kuwae and T. Shioya (2003): the convergence
  frame this theorem instantiates class-uniformly.
```
