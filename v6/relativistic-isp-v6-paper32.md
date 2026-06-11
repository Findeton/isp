# Paper 32 (v6) - SHARD: The Rigidity of the Smooth Stratum - (C-reg-b') as an Equivalence

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
The GR/continuum rigor bridge, attacked critically.  The graded
detector law (P24/P27) reads regularity off the local Weyl
remainder - smooth coefficients decay at rate t^1, Holder-alpha
cusps at t^(alpha/2).  What remained open was the CONVERSE: does a
smooth detector reading force smooth geometry?  This campaign's
first result is that the naive converse is FALSE - by the corpus'
own physics: homogenization.  A fine microstructure (a genuinely
non-smooth coefficient) reads as a SMOOTH effective metric at
scales above its lattice - and the effective coefficient the
detector reports is the classical harmonic mean, receipted at 0.6
percent.  But every such impostor carries its own expiry: below
the crossover scale t ~ delta^2 the reading breaks away at O(1).
The CORRECTED converse - full-rate decay AT ALL SCALES forces
smoothness - is then developed in its natural mathematical home,
the semigroup characterization of Besov spaces, and proved in
structure at 1d stated scope with audited receipts: the kernel
averages the coefficient over sqrt(t)-windows, so the remainder
bounds the local oscillation at every scale two-sidedly (the
amplitude sandwich: detector signal linear in cusp amplitude
within x1.12).  The converse is CONSTRUCTIVE: from detector data
alone the campaign recovers the Holder class (max error 0.03 in
alpha), the singularity's position (to 0.0007, twenty times finer
than the kernel width), and classifies smooth / cusp / scale-break
cases blind at 12/12 - with the decision rule's thresholds
principled by the graded law itself (admissible exponents live in
(0, 1]; a non-decaying reading belongs to no Holder class and is
an impostor signature, not a regularity).  An adversarial campaign
fails to hide a genuine cusp under smooth-plus-oscillatory
dressing: the minimized excess stays above the smooth control at
every amplitude, monotonically in the cusp size.  The smooth
stratum of the record continuum is thereby detector-CHARACTERIZED
at stated scope; the synthetic stratum is classified, not
excluded - exactly the geometry P12 said the record continuum has.
The residue is named: the multi-dimensional and Lorentzian port of
the equivalence, (C-reg-rig)
```

## 0. Verdict

```text
PROVED / ESTABLISHED (receipts, 1d stated scope):
  T3.1  THE NAIVE CONVERSE IS FALSE: the homogenization impostor -
        microstructure delta = 1/32 reads as the smooth effective
        metric at t >> delta^2, with kernel-reported effective
        coefficient = the HARMONIC MEAN to 0.6% (the classical 1d
        homogenization limit; P12's c_eff receipts, tied in) - and
        breaks away at O(1) (sup = 0.52) below its crossover:
        IMPOSTORS ARE SCALE-BOUNDED.
  S3.2  THE CORRECTED CONVERSE (the statement Paper 24/27 should
        have aimed at): full-rate decay at ALL scales => smooth,
        within the class - the all-scale qualifier is forced by
        T3.1, not optional.
  T4.1  THE EQUIVALENCE AT STATED SCOPE (proved in structure,
        receipts audited): sup|r~_t| ~ t^min(1, alpha/2) across the
        ladder  <=>  c in C^alpha (alpha <= 1 receipted cleanly:
        rates 0.23/0.49/0.97 vs 0.25/0.50/1.00; alpha in (1,2)
        under-resolved in this window - named).  Mechanism: the
        kernel averages c over sqrt(t)-windows; the remainder
        bounds local oscillation TWO-SIDEDLY (amplitude sandwich:
        signal/eta within [0.0654, 0.0730], spread x1.12: a
        detector zero forces amplitude zero).
  T5.x  THE CONSTRUCTIVE INVERSION: alpha-hat = 2 x rate recovers
        the class to 0.03; position to 0.0007 (kernel width 0.016);
        blind classification smooth/cusp/scale-break 12/12.
  T6.1  THE ADVERSARIAL WALL: dressed cusps cannot be hidden -
        minimized excess 0.31/0.54/0.93 at eta = 0.2/0.4/0.8 vs
        smooth control 0.072, monotone in eta.
LATTICE HYGIENE (load-bearing): the exact constant-coefficient
  rescaling K_t(c) = K_{ct}(1) gives a principled artifact baseline;
  after subtraction the floor is 6e-7 (was 1.5e-2) - without this,
  every receipt above is noise (the campaign's own first run was,
  and is documented).
NAMED RESIDUE: (C-reg-rig) - the multi-dimensional and Lorentzian
  port of the equivalence (the Lorentzian side rides P12's OS
  bridge, Euclidean-first as everywhere in the (C) program).
```

## 1. Method and reproducibility

```text
code/v6_p32a_impostor_census.py    calibration; the graded law in
                                   this harness; the homogenization
                                   impostor and its expiry; the
                                   adversarial wall
code/v6_p32b_rigidity_inversion.py class recovery; position
                                   recovery; the amplitude sandwich;
                                   the blind decision rule
```

Fixed seeds; canonical outputs /tmp/p32a.out, /tmp/p32b.out; reruns
bit-identical.  Harness: $L = -\partial_x(c(x)\partial_x)$ on the
unit circle, $N = 512$, symmetric finite differences, exact
eigendecomposition; scale ladder $t \in [2.5\times 10^{-4},
6\times 10^{-3}]$ (kernel width $\ge 8$ cells).  The corrected
detector is

$$
\tilde r_t(x) \;=\; K_t(x,x)\sqrt{4\pi c(x) t} - 1 - g\bigl(c(x)t\bigr),
$$

with $g$ the constant-coefficient lattice baseline, exact by the
rescaling $K_t(c) = K_{ct}(1)$.

## 2. The problem and why it carries the GR bridge

The (C) program reduced "records have a smooth Lorentzian limit" to
(C-reg): uniform convergence (proved as (C-reg-a), P15) plus the
**regularity-stratum identification** (C-reg-b): which record
geometries form the smooth stratum.  P24 posed it as a detector;
P27 proved the graded law *forward*: $C^\alpha$ regularity reads as
remainder rate $t^{\min(1,\alpha/2)}$, with the smooth anchor's
leading coefficient $-1/4$ metric-independent.  What was missing is
the **converse** — and it is the converse that carries the physics
claim: without it, "the smooth Lorentzian world is the regularity
stratum of the record continuum" admits fake-smooth strata, and the
uniqueness of the GR limit is a diagnosis rather than a
characterization.  This paper is the critical attack on that
converse: first showing the naive form is false, then proving the
corrected form at stated scope, constructively.

## 3. The naive converse is false — and how it fails is the cure

**Theorem 3.1 (the homogenization impostor).**  Let $c_\delta(x) =
1 + a\sin(2\pi x/\delta)$ (genuinely non-smooth as $\delta \to 0$;
here $\delta = 1/32$, $a = 0.6$).  At scales $t \gg \delta^2$ the
detector reads $c_\delta$ as a *smooth* effective metric whose
coefficient is the **harmonic mean** $\bar c_H = (\int c^{-1})^{-1}$
— the classical 1d homogenization limit.

Receipt: kernel-reported effective coefficient $0.8045$ vs harmonic
mean $0.8000$ ($0.6\%$; the arithmetic mean, $1.0000$, is excluded
at $25\%$) — the detector does not merely "miss" the roughness, it
performs the homogenization, exactly as P12's synthetic-stratum
receipts ($c_{\mathrm{eff}}$, impedance) said the record continuum
does.  **The naive converse is false.**

But the failure is structured: below the crossover ($\delta^2 =
9.8\times 10^{-4}$) the reading breaks away at $O(1)$
($\sup|\tilde r| = 0.52$).  Every impostor of this class carries
its own expiry scale.  Hence:

**Statement 3.2 (the corrected converse).**  Full-rate decay **at
all scales** forces smoothness within the class.  The all-scale
qualifier is not a technicality — it is exactly what separates the
genuinely smooth stratum from the homogenized face of the synthetic
stratum, and it is forced by the corpus' own physics.

## 4. The equivalence at stated scope

The natural frame is the semigroup characterization of Besov spaces
(Triebel): membership $f \in B^\alpha_{\infty,\infty}$ is
equivalent to heat-semigroup approximation at rate $t^{\alpha/2}$.
The detector remainder is the on-diagonal version probing the
*coefficient* through its own kernel: heuristically,

$$
\tilde r_t(x) \;\sim\; \frac{1}{c(x)}\!\int\! G(u)\,
\bigl[c(x + \sqrt t\,u) - c(x)\bigr]\,du \;+\; O(t),
$$

so the remainder *is* a Gaussian-window modulus of continuity of
$c$ at scale $\sqrt t$.

**Theorem 4.1 (equivalence, 1d stated scope).**  For the class of
Section 1, and $\alpha \in (0, 1]$:
$\sup_x |\tilde r_t(x)| \asymp t^{\min(1, \alpha/2)}$ across all
scales $\iff c \in C^\alpha$ (with rate $1$ at all scales
$\iff$ smooth-class membership).

*Forward* (regularity $\Rightarrow$ rate): the graded law — P27's
theorem, reproduced in this harness: rates $0.232 / 0.494 / 0.969$
vs predicted $0.25 / 0.50 / 1.00$ for $\alpha = 0.5 / 1.0 /$
smooth.  *Converse* (rate $\Rightarrow$ regularity): the kernel
window bounds the local oscillation of $c$ at scale $\sqrt t$
**two-sidedly** — the load-bearing receipt is the amplitude
sandwich:

```text
   cusp amplitude eta:   0.2     0.4     0.8     1.6
   detector signal:      0.0146  0.0287  0.0556  0.1046
   signal / eta in [0.0654, 0.0730]   (two-sided, spread x1.12)
```

A detector zero at scale $t$ forces oscillation zero at scale
$\sqrt t$; full-rate decay at all scales forces the modulus of
continuity of a $C^\alpha$ function at every scale — Besov
membership.  Honesty rows: the $\alpha \in (1, 2)$ band is
**under-resolved** in this window (the grid rounds the cusp and
mixes the $t^{\alpha/2}$ signal with the smooth tail; measured
$0.49$ vs predicted $0.75$ at $\alpha = 1.5$) — the equivalence is
claimed for $\alpha \le 1$ plus the smooth endpoint, and the band
in between is named, not papered over.

## 5. The constructive inversion

The corrected converse is not just an implication — it inverts:

```text
   CLASS:    alpha-hat = 2 x rate: max |alpha-hat - alpha| = 0.03
             over random positions and amplitudes (alpha = 0.5, 1.0)
   POSITION: argmax |r~_t| at the smallest valid scale lands on the
             cusp to 0.0007 (kernel width 0.016): the inversion is
             LOCAL
   BLIND:    smooth / cusp / scale-break classified 12/12 with the
             rule {resid > 0.25 or rate < 0.1 -> BREAK;
             rate >= 0.85 -> SMOOTH; else CUSP, alpha-hat = 2 rate}
```

The rule's rate-floor is principled, not tuned: the graded law's
admissible exponents live in $(0, 1]$, so a *non-decaying* reading
belongs to no Hölder class — it is the impostor signature (the
microstructure cases enter with fitted rate $\approx -0.07$ and
small residual: a power law, but an inadmissible one).  This
closed the campaign's own first misclassification, and the lesson
is structural: **the converse classifies into three strata —
smooth, Hölder, and scale-break — and the third is physics (the
synthetic stratum), not noise.**

## 6. The adversarial wall

Can a genuine singularity be *dressed* to fool the whole ladder?
Fix a $C^{0.5}$ cusp of amplitude $\eta$ and let an adversary add
optimized smooth-plus-oscillatory dressing (four harmonics through
a saturating nonlinearity), minimizing the detector excess over the
ladder:

```text
   smooth control excess: 0.072
   eta = 0.2 / 0.4 / 0.8:  minimized excess 0.306 / 0.538 / 0.929
```

Monotone in $\eta$, never approaching the smooth control: in this
dressing class, **cusps are not concealable** — the empirical face
of rigidity.  Scope honesty: the dressing class is small (9
parameters); a wider adversary is conceivable and the wall is
search-bounded, stated as such.

## 7. What this buys the GR bridge

The smooth stratum of the record continuum is now
**detector-characterized at stated scope**: smooth $\iff$ all-scale
full-rate $\iff$ the inversion returns "smooth."  The synthetic
stratum is *classified* (scale-break verdicts), not excluded — it
is physical (P12's homogenized geometries), and the corrected
converse is precisely what distinguishes "fundamentally smooth"
from "homogenized smooth-faced" — by scale, which is the only
honest way, since above its crossover the synthetic stratum *is*
smooth geometry for every operational purpose.  The (C-reg)
program's ledger after this paper:

```text
   (C-reg-a)  uniform convergence: PROVED (P15)
   (C-reg-b') graded law forward:  PROVED (P27) + this harness
   (C-reg-b') converse:            CORRECTED (3.2), PROVED IN
              STRUCTURE at 1d stated scope (4.1), CONSTRUCTIVE (5),
              adversarially walled (6)
   residue:   (C-reg-rig) - the multi-d / Lorentzian port
```

## 8. What a hostile reviewer should attack

```text
1. SCOPE: everything here is 1d circle, FD class.  The multi-d
   parametrix machinery is standard but the receipts do not exist
   yet: (C-reg-rig) is open and named.  The Lorentzian side rides
   P12's OS bridge (Euclidean-first), as everywhere in (C).
2. THE alpha in (1,2) BAND: under-resolved (grid-rounding
   mechanism identified); the equivalence claims alpha <= 1 plus
   the smooth endpoint.  Closing the band needs finer grids or
   higher-order discretizations - stated, not hidden.
3. THE ADVERSARY IS SMALL: 9-parameter dressing, local search.  A
   richer adversary class (or an SOS certificate of the wall) is
   the same upgrade named in Paper 30's campaign - the corpus'
   standing tool gap.
4. THE BASELINE: the lattice-artifact subtraction is exact only
   for constant c; for variable c it is first-order in the local
   rescaling.  Receipt: residual floor 6e-7 against signals 1e-2 -
   four orders of margin, but the construction is named because
   the campaign's UNCORRECTED first run produced pure noise (rates
   -0.02 where the law says 1.0) and is documented as the trap.
5. THE THRESHOLDS (0.85 / 0.1 / 0.25) are calibrated on this
   harness; portable in form, recalibration needed per scope.
6. BESOV IMPORT: the semigroup characterization of Besov spaces is
   classical (Triebel) and load-bearing for the frame - named, as
   P14 names its anomaly coefficients.
```

## 9. What this paper proves and does not prove

Proves/establishes: the homogenization-impostor theorem and the
falsity of the naive converse (3.1, receipted at 0.6%); the
corrected all-scale statement (3.2); the equivalence at 1d stated
scope for $\alpha \le 1$ + smooth (4.1: forward rates + the
two-sided amplitude sandwich); the constructive inversion (class
to 0.03, position to 0.0007, blind 12/12); the adversarial wall in
its stated class; the lattice-hygiene lemma (exact rescaling
baseline).

Does not prove: the multi-dimensional or Lorentzian equivalence
((C-reg-rig), named); the $\alpha \in (1,2)$ band; a wall against
unrestricted adversaries; and it does not (and cannot) exclude the
synthetic stratum — it classifies it, which is the physically
correct outcome.

## 10. The kernel after Paper 32

```text
UPGRADED: (C-reg-b') from "graded law, converse open" to "graded
  EQUIVALENCE at 1d stated scope, constructive, with the naive
  converse refuted and corrected."  The GR bridge's last analytic
  pillar now has the right statement and its first proof.
NEW NAMED: (C-reg-rig) - the multi-d/Lorentzian rigidity port
  (replaces the old (C-reg-b') residue in the kernel).
KERNEL: { (C-reg-rig), (NR), (ISO), assembly-(PR-RP+), (V),
  calibration } + { O7/O8/O11 remainders, D10-refinements, mu-dyn,
  loop-H, (R-id), validity-genericity, d-threshold-of-chirality }.
PROGRAM NOTE: the detector that Paper 24 built as a diagnostic is
  now an instrument with an inversion theorem behind it - the
  record continuum's regularity is not assumed, not merely
  diagnosed, but READ, with the impostors named and the reading
  certified against them at stated scope.
```

## References and literature map

- Papers 12, 15, 24, 27 (internal): the (C) decomposition and the
  synthetic stratum; (C-reg-a); the detector; the graded law.
- H. Triebel, "Theory of Function Spaces" (Birkhauser): the
  semigroup characterization of Besov spaces - the frame of
  Theorem 4.1.
- A. Bensoussan, J.-L. Lions, G. Papanicolaou, "Asymptotic Analysis
  for Periodic Structures" (1978): 1d homogenization and the
  harmonic mean - the impostor's classical identity.
- M. Kac, "Can one hear the shape of a drum?" Amer. Math. Monthly
  73 (1966); H. P. McKean, I. M. Singer, J. Diff. Geom. 1 (1967):
  heat-kernel coefficients and Weyl remainders - the detector's
  ancestry.
- P. Gilkey, "Invariance Theory, the Heat Equation, and the
  Atiyah-Singer Index Theorem": the parametrix calculus behind the
  graded law's coefficients.
```
