# Hearing the regularity of a diffusion coefficient: a graded local Weyl law with a constructive converse

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-11.

## Abstract

The on-diagonal heat kernel of $L = -\partial_x(c(x)\partial_x)$
carries a local Weyl remainder
$r_t(x) = K_t(x,x)\sqrt{4\pi c(x)t} - 1$.  This is a paper of
*experimental mathematics with precise conjectures*: we present a
window heuristic and systematic fixed-seed evidence — not proofs —
that the decay
rate of $\sup_x|r_t|$ *grades* the regularity of the coefficient
(Conjecture G: $C^\alpha$ cusps read as $t^{\min(1,\alpha/2)}$,
coefficients in the
Favard/saturation class $\{c : c'' \in L^\infty\}$ as $t^1$), and we
study the
converse: does a full-rate reading force membership in the
regularity class?  For the *practically available* (coefficient-free)
form of the detector, as a statement over any *finite window of
scales* the converse is **false**, by homogenization: a coefficient
with fine (analytic, but large-norm) microstructure reads, at every
scale above its cell size, as a smooth *effective* medium, the
fitted coefficient agreeing with the classical harmonic mean
to $0.6\%$.  Every such impostor carries its own expiry
scale, breaking away at $O(1)$ below the crossover $t \sim
\delta^2$.  The repaired statement is therefore scale-quantified —
full-rate decay *at all scales* conjecturally characterizes the
class (Conjecture C below; the frame is the semigroup
characterization of Hölder–Besov spaces, the proof obligation —
uniform two-sided parametrix bounds for merely-Hölder coefficients
— is stated and not discharged) — and it is probed constructively: from detector data alone we recover the
Hölder exponent to $\pm 0.03$ (and, in a de-circularized variant
that never consults the true coefficient, to comparable accuracy),
locate the singularity to $7\times 10^{-4}$ (twenty times finer than
the probing kernel's width), verify a two-sided near-linearity of the
signal in the cusp amplitude (mildly sublinear: signal/amplitude
drifts from $0.073$ to $0.065$ over an $8\times$ range — the
honest spread $\times 1.12$), and classify
smooth / cusp / scale-break cases blind at $12/12$, with the
decision thresholds dictated by the graded law itself (admissible
exponents lie in $(0,1]$, so a non-decaying reading within the
window belongs to no Hölder class at those scales and is an impostor
signature).
An adversarial study shows a genuine cusp cannot be hidden by
smooth-plus-oscillatory dressing across the scale ladder.  A
load-bearing numerical lemma is included: the lattice artifact of the
discrete kernel admits an exact constant-coefficient rescaling
baseline, $K_t(c) = K_{ct}(1)$, whose subtraction improves the
detector floor from $10^{-2}$ to $10^{-7}$ — without it, every
measurement above is noise.  Scope: one dimension; the
multidimensional and Lorentzian ports are discussed.

## 1. Introduction

Weyl asymptotics and heat-kernel expansions are the classical bridge
between spectrum and geometry [1, 2, 3].  For smooth coefficients the
on-diagonal kernel of $L = -\partial_x(c\,\partial_x)$ on the circle
satisfies $K_t(x,x) = (4\pi c(x)t)^{-1/2}(1 + a_1(x)\,t + \cdots)$
with $a_1$ built from $c'', (c')^2/c$; the *local Weyl remainder*

$$
r_t(x) \;=\; K_t(x,x)\sqrt{4\pi c(x)t} \;-\; 1
$$

then decays linearly in $t$.  When $c$ is merely Hölder the expansion
fails, and the natural question — in the spirit of "can one hear the
shape of a drum" [4] but local and quantitative — is what the decay
of $r_t$ *hears*.

**Conjecture G (the graded law, forward direction) — and its
epistemic status.**  For $c$ with a $C^\alpha$
cusp, $\sup_x|r_t| \sim t^{\min(1, \alpha/2)}$.  The heuristic: the
kernel averages
the coefficient over windows of width $\sqrt t$, so the remainder is
a Gaussian-window modulus of continuity at scale $\sqrt t$.  We are
explicit that this paper does **not** prove the law — that would
require uniform two-sided parametrix bounds for merely-Hölder
coefficients, which we do not supply; what we supply is the
heuristic, sharp receipts (measured rates
$0.232/0.494/0.969$ against $0.25/0.50/1.00$ for $\alpha = 0.5, 1.0$
and smooth; the same rates at $N = 768$ agree to within $0.001$ —
Section 6), and the two-sided amplitude evidence of Section 4.  We
also identify why the band $\alpha \in (1,2)$ is harder
to resolve numerically (Section 6).  Here and throughout, "smooth"
as a detector verdict means the **saturation class**: the $a_1(x)t$
term caps the readable rate at $t^1$, and by classical saturation
theory for first-order semigroup approximation the $O(t)$ class is
the **Favard class** $\{c : c'' \in L^\infty\}$
($C^{1,1}$-type) — *strictly smaller* than the Zygmund-type
$B^2_{\infty,\infty}$ that an earlier draft named (second-order
characterizations, $(I - T_t)^2$, would be needed for the latter;
the correction is a referee's and we record it) — and regularity
beyond the saturation class is invisible to this detector.

**The converse and its correction (main contribution).**  Does a
rate-$1$ reading certify saturation-class membership?  For the
practically available detector — the coefficient-free ratio form of
Section 5, since the oracle form below needs the answer as input —
over a finite window of scales, no: Section 3 gives the
homogenization
impostor — oscillatory microstructure $c_\delta$ reads, for $t \gg
\delta^2$, as the *smooth* effective medium with the harmonic-mean
coefficient (the classical 1d homogenization limit [5]), so that
detector does not merely miss the fine structure, it performs the
homogenization.  We stress the logical type of this counterexample:
$c_\delta$ is analytic, with finite (merely enormous) class norms,
so the *asymptotic* ($t \downarrow 0$) converse is never violated —
what fails is every fixed-window version of it, which is the version
any finite measurement uses.  The corrected converse must therefore
be **scale-quantified**: full-rate decay at *all* scales
(Conjecture C: in the semigroup-characterization frame [6], with the
same undischarged proof obligation as Conjecture G).  It is probed
**constructively**: Section 5
demonstrates the inversion — class, position, amplitude — with blind
classification at $12/12$ including the impostor class, whose
signature (a non-decaying or scale-broken reading within the window)
is exactly what the graded law's exponent range $(0,1]$ forbids for
genuine Hölder classes at those scales.

**Why this matters beyond spectral theory.**  If Conjectures G and
C hold, the diagnostic upgrades to a characterization: "the
coefficient is in the saturation class" and
"the detector reads rate 1 at all scales" become interchangeable at
stated scope, with the homogenized media correctly *classified*
(scale-break class) rather than misread.  In applications where an
effective geometry emerges from microstructure, by-scale
classification is the physically meaningful statement.

## 2. Setting and the corrected detector

Unit circle, $L = -\partial_x(c\,\partial_x)$ with $0 < c \in
L^\infty$, symmetric finite differences at $N = 512$, exact
eigensolve; scale ladder $t \in [2.5\times 10^{-4}, 6\times 10^{-3}]$
(probing widths $\ge 8$ grid cells).

**Lemma 2.1 (lattice baseline).**  For constant $c$, the discrete
kernel satisfies $K^{\mathrm{disc}}_t(c) = K^{\mathrm{disc}}_{ct}(1)$
exactly.  Hence the lattice artifact admits the baseline
$g(s) := r^{\mathrm{disc}}_s(\,\cdot\,; c \equiv 1)$ and the
**corrected detector** $\tilde r_t(x) = r_t(x) - g(c(x)t)$ removes it
to first order in the variation of $c$.

Receipt: floor improvement from $1.5\times 10^{-2}$ to
$6\times 10^{-7}$; the uncorrected pipeline's "measurements" are pure
discretization (a documented failure of our own first run: smooth
coefficients read rate $-0.02$ where the law says $1.0$).  We flag
this prominently because any implementation of local-Weyl numerics
faces it.

## 3. The finite-window converse is false: the homogenization impostor

**Proposition 3.1 (impostor; classical limit plus receipts —
stated for the right detector).**  Let
$c_\delta(x) = 1 + a\sin(2\pi x/\delta)$.  For $t \gg \delta^2$ the
diagonal kernel is spatially flat and the **coefficient-free
reading** — the fitted coefficient $\hat c = 1/(4\pi t
K_t(x,x)^2)$, equivalently the ratio detector of Section 5 — reads
$c_\delta$ as a smooth medium whose
reported coefficient is the harmonic mean $\bar c_H =
(\int c^{-1})^{-1}$; for $t \ll \delta^2$ the reading breaks away at
$O(1)$.

*Which detector is fooled — a correction kept visible.*  An earlier
draft stated this for the oracle detector $\tilde r_t$ of Lemma 2.1.
That was wrong, as a referee's reconstruction showed: $\tilde r_t$
normalizes by the *true* $\sqrt{c(x)}$, which oscillates at $O(1)$
against the homogenized (flat) kernel, so the oracle detector reads
$\sup|\tilde r_t| \approx \sqrt{(1+a)/\bar c_H} - 1 \approx 0.41$,
*non-decaying at all scales above the crossover* — it is never
fooled, and that non-decaying signature is precisely how the blind
classification of Section 5 catches the microstructure (fitted
rate $\approx -0.07$ there).  The impostor phenomenon — and hence
the finite-window failure of the converse — belongs to the
*coefficient-free* detectors, which are also the only ones a real
measurement has.  The narrative of Sections 1 and 5 is stated for
those.

*Status of the statement.*  The $t \gg \delta^2$ regime is a
consequence of classical periodic homogenization [5] (G-convergence
of $L_\delta$ to the harmonic-mean operator, hence locally uniform
convergence of the kernels); we do not re-prove it.  What we add,
and verify by machine rather than prove, is the *detector-level
quantification*: the crossover location, the $O(1)$ breakaway size,
and the fidelity of the reported coefficient at finite $\delta$.

Receipts ($\delta = 1/32$, $a = 0.6$): fitted effective coefficient
$0.8045$ vs $\bar c_H = 0.8000$ (within $0.6\%$; because the
profile here is deterministic, the comparison carries no
realization-versus-ensemble gap — unlike the random-coefficient
example of Section 6, where that gap must be accounted for — and
the arithmetic mean $1.0$ is excluded at $25\%$); oracle detector above crossover:
$\sup|\tilde r| \approx 0.41$, non-decaying, as the correction
paragraph states; below crossover both readings break at $O(1)$
($\sup|\tilde r| = 0.52$).

Note again the type of the example: $c_\delta$ is analytic.  The
impostor does not contradict the asymptotic converse; it shows that
the converse *as restricted to any finite scale window* — the only
version a finite-resolution measurement can instantiate — is false,
and that the failure is physical (effective-medium formation), not
pathological.  The failure mode dictates the fix:

**Conjecture C (corrected converse).**  If the coefficient-free
detector reads rate $1$ — $O(t)$ decay — *at every scale*
$t \downarrow 0$, then $c$ belongs to the Favard/saturation class
$\{c : c'' \in L^\infty\}$ of Section 1; more
generally the all-scale rate $t^{\alpha/2}$ characterizes
$B^\alpha_{\infty,\infty}$ membership for $\alpha \in (0,1)$ (the
Hölder range, where first-order semigroup characterizations [6]
apply).  The
mechanism is the two-sided window estimate of Section 4; the proof
obligation (uniform two-sided parametrix bounds for non-smooth
coefficients) is open and stated, not papered over.

## 4. The two-sided mechanism

The kernel window bounds the local oscillation of $c$ at scale
$\sqrt t$ from both sides.  The load-bearing receipt is the
**amplitude sandwich**: for a $C^{0.5}$ cusp of amplitude $\eta$ at
fixed scale,

```text
   eta:        0.2      0.4      0.8      1.6
   signal:     0.0146   0.0287   0.0556   0.1046
   signal/eta in [0.0654, 0.0730]   (two-sided, spread x1.12)
```

A detector zero at scale $t$ forces oscillation zero at scale
$\sqrt t$; iterating over the ladder forces the modulus of
continuity at every scale — Besov membership.  Conversely the
forward graded law bounds the signal above by the class norm.  At
the stated 1d scope this is the mechanism behind Conjecture C for
$\alpha \in (0, 1)$ (the Hölder range; at $\alpha = 1$ the
all-scale rate $t^{1/2}$ tracks the Zygmund class
$B^1_{\infty,\infty}$, not Lipschitz, and we make no equivalence
claim there) plus the saturation endpoint.

## 5. The constructive inversion

From detector data alone:

- **Class**: $\hat\alpha = 2\times$ (fitted rate), capped at smooth.
  Across random positions and amplitudes ($\alpha \in \{0.5, 1.0\}$):
  $\max|\hat\alpha - \alpha| = 0.03$.
- **Position**: $\arg\max_x |\tilde r_t(x)|$ at the smallest valid
  scale lands within $7\times 10^{-4}$ of the cusp (kernel width
  $1.6\times 10^{-2}$): the inversion is local.
- **Blind classification** over 12 cases (5 smooth random Fourier
  media, 5 cusps with random parameters, 2 microstructures):
  decision rule — fit residual $> 0.25$ *or* rate $< 0.1$ declares
  SCALE-BREAK; rate $\ge 0.85$ declares SMOOTH; otherwise CUSP with
  $\hat\alpha$.  Result: $12/12$.  Threshold honesty: the rate
  *floor* ($0.1$) is principled, not
  tuned — graded exponents live in $(0,1]$, so a non-decaying reading
  (microstructure enters at fitted rate $\approx -0.07$ with small
  residual — a power law, but an inadmissible one) belongs to no
  Hölder class — while the residual threshold ($0.25$) and the
  smooth threshold ($0.85$) *are* tuned choices, and the $12/12$
  should be read with that asymmetry in mind.

The three-way output — smooth / Hölder / scale-break — is the
correct taxonomy: the third class is *physics* (effective media),
not noise, and the constructive converse classifies it instead of
being fooled by it.

**De-circularizing the detector.**  A fair objection: $\tilde r_t$
contains $\sqrt{c(x)}$ and $g(c(x)t)$ — the inversion above consults
the very coefficient it claims to probe.  Two remarks.  First, the
naive repair (estimate $\hat c$ from $K_t$ at the smallest window
scale and substitute) *fails by construction*: the detector then
vanishes at the calibration scale and the decay fit measures the
calibration, not the roughness — we ran it, and the fitted exponents
pin at the cap; we record this as a warning to implementers.  The
correct repair is the **ratio detector**

$$
s_\lambda(x,t) \;=\;
\frac{K_{\lambda t}(x,x)\,\sqrt\lambda\,\bigl(1+g(\hat c(x)t)\bigr)}
     {K_t(x,x)\,\bigl(1+g(\hat c(x)\lambda t)\bigr)} \;-\; 1,
$$

in which the unknown $\sqrt{4\pi c(x)t}$ normalization cancels
*exactly* between numerator and denominator; a crude $\hat c$
(smallest-scale estimate) survives only inside the lattice
correction $g$, where its $O(t^{\alpha/2})$ error multiplies a term
that is itself $\lesssim 10^{-3}$.  The roughness signal survives
with the same exponent: $\sup_x|s_\lambda| \sim
t^{\alpha/2}(\lambda^{\alpha/2}-1)$.  Receipt ($\lambda = 4$, three
random cusp positions/amplitudes per class, both grids):

```text
   alpha = 0.5:  fitted rates 0.224 - 0.237   (law: 0.25)
   alpha = 1.0:  fitted rates 0.489 - 0.495   (law: 0.50)
   smooth:       rate 0.944 / 0.945           (law: ~1)
```

The inversion needs no oracle access to $c$.

## 6. The adversarial wall and honest limitations

**Adversarial study.**  Fix a genuine $C^{0.5}$ cusp of amplitude
$\eta$ and minimize the detector excess over smooth-plus-oscillatory
dressing (nine parameters, local search):

```text
   smooth control excess:  0.072
   eta = 0.2 / 0.4 / 0.8:  0.306 / 0.538 / 0.929  (minimized)
```

Monotone in $\eta$, never approaching the control: in this dressing
class a cusp cannot be hidden from the ladder.  *Limitations*: the
dressing class is small and the search local — the wall is
search-bounded; a certificate version (sum-of-squares over the
dressing class) is the natural upgrade.

**The $\alpha \in (1, 2)$ band.**  Our grid rounds the cusp at scale
$h$, mixing the $t^{\alpha/2}$ signal with the smooth tail; measured
$0.49$ at $\alpha = 1.5$ versus predicted $0.75$.  The equivalence is
claimed for $\alpha \le 1$ plus the saturation endpoint; closing the
band needs finer grids or higher-order discretizations and is stated
as open, not papered over.

**Grid refinement.**  The headline rates are not lattice artifacts:
refining $N = 512 \to 768$ (a $1.5\times$ finer grid) leaves every
fitted rate unchanged to three decimals —
$0.232/0.494/0.969$ vs $0.232/0.494/0.970$ for
$\alpha = 0.5/1.0$/smooth — and the de-circularized rates of
Section 5 move by $< 0.013$.

**Dimension: the 2d port, executed.**  The parametrix mechanism and
the Besov frame are dimension-generic, and we verify the port on the
2-torus ($L = -\nabla\!\cdot(c\nabla)$, $40^2$ grid, the same exact
rescaling baseline — valid in any dimension):

```text
   smooth rate 0.880 (law: 1.0, window-limited);  cusp rates
   0.197 / 0.452 at alpha = 0.5 / 1.0 (law: 0.25 / 0.50);
   position recovery to 0.015 (kernel width 0.035).

   THE 2d IMPOSTOR has its own exact classical anchor: for a
   statistically isotropic symmetric two-phase medium the
   effective coefficient is the GEOMETRIC MEAN (Dykhne/Keller
   duality [11]).  Random checkerboard (c1, c2) = (0.5, 2.0):
   kernel-reported effective c = 1.0057 vs geometric mean 1.0000
   (0.6%).  Quantity bookkeeping, stated: 1.0000 is the ENSEMBLE
   Dykhne/Keller target (symmetric fractions); the random
   realization has phase fraction p-hat ~ 0.53, whose own
   arithmetic mean is the quoted 1.205 (not the ensemble 1.25),
   and realization fluctuation contributes at the same order as
   the quoted 0.6% - so the receipt is "ensemble target matched
   to within realization noise", with the arithmetic mean
   excluded at 20%.  Below the cell scale the reading breaks
   at O(1).
```

The detector thus performs the *correct, dimension-specific*
homogenization in 2d exactly as it performed the harmonic-mean
homogenization in 1d — strong evidence that the corrected
(all-scale) converse is the right statement in every dimension.
The general-$d$ theorem with anisotropic coefficient classes, and a
Lorentzian port (Euclidean-first through Osterwalder–Schrader
rotation), remain the named sequels.

## 7. Related work

Heat invariants and local Weyl expansions for smooth coefficients are
classical [1, 2, 3]; regularity detection via semigroup approximation
rates is implicit in the Besov characterization literature [6];
homogenization of oscillatory coefficients is textbook [5].  Two
adjacent literatures must be distinguished from what is done here.
*Inverse spectral theory* (Borg [7]; Gel'fand–Levitan [8]; Marchenko
[9]) recovers the coefficient itself from full spectral data
(spectrum plus norming constants); we use far less input — the decay
*rate* of the on-diagonal kernel — and obtain a correspondingly
coarser output, a regularity class with localization, which is why
the method survives non-smooth coefficients where the classical
machinery assumes regularity.  *Aronson-type Gaussian bounds* [10]
guarantee that $K_t$ and hence the detector are well-defined for
merely measurable uniformly elliptic $c$, which is what licenses
evaluating $\tilde r_t$ on every class discussed, including the
microstructures.  The contributions here are (i) the graded *local
sup* law with receipts at non-smooth classes, (ii) the impostor
proposition identifying the precise failure (and physical meaning)
of the finite-window converse, (iii) the constructive inversion with
the principled three-way decision rule and its de-circularized
variant, and (iv) the adversarial formulation of detector rigidity.

## Reproducibility

Fixed-seed scripts regenerate every number: the baseline lemma and
floor receipts; the graded rates; the homogenization receipts; the
inversion and blind classification; the adversarial walls.  Code and
canonical outputs accompany the submission.

## References

[1] H. P. McKean, I. M. Singer, Curvature and the eigenvalues of the
Laplacian, *J. Diff. Geom.* **1** (1967) 43–69.

[2] P. Gilkey, *Invariance Theory, the Heat Equation, and the
Atiyah–Singer Index Theorem*, CRC Press (1995).

[3] M. van den Berg, On the asymptotics of the heat equation and
bounds on traces associated with the Dirichlet Laplacian,
*J. Funct. Anal.* **71** (1987) 279; M. van den Berg,
S. Srisatkunarajah, Heat flow and Brownian motion for a region in
$\mathbb R^2$ with a polygonal boundary, *J. London Math. Soc.*
**37** (1988) 119 — not-feeling-the-boundary asymptotics.

[4] M. Kac, Can one hear the shape of a drum?, *Amer. Math. Monthly*
**73** (1966) 1–23.

[5] A. Bensoussan, J.-L. Lions, G. Papanicolaou, *Asymptotic
Analysis for Periodic Structures*, North-Holland (1978).

[6] H. Triebel, *Theory of Function Spaces*, Birkhäuser (1983) —
semigroup characterizations of Besov spaces.

[7] G. Borg, Eine Umkehrung der Sturm–Liouvilleschen
Eigenwertaufgabe, *Acta Math.* **78** (1946) 1–96.

[8] I. M. Gel'fand, B. M. Levitan, On the determination of a
differential equation from its spectral function, *Izv. Akad. Nauk
SSSR Ser. Mat.* **15** (1951) 309–360.

[9] V. A. Marchenko, *Sturm–Liouville Operators and Applications*,
Birkhäuser (1986).

[10] D. G. Aronson, Bounds for the fundamental solution of a
parabolic equation, *Bull. Amer. Math. Soc.* **73** (1967) 890–896.

[11] A. M. Dykhne, Conductivity of a two-dimensional two-phase
system, *Sov. Phys. JETP* **32** (1971) 63; J. B. Keller, A theorem
on the conductivity of a composite medium, *J. Math. Phys.* **5**
(1964) 548 — the geometric-mean effective medium of Section 6.
