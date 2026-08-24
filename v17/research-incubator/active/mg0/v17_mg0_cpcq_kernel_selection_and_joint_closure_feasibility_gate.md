# ISP v17 — CP-CQ kernel selection and joint-closure feasibility gate

## Why positivity and covariance do not yet choose the physical gravity law

**Status:** COMPLETE AUTHOR-SIDE MATHEMATICAL/PHYSICAL FEASIBILITY GATE / NOT A CANDIDATE / NOT INDEPENDENTLY REVIEWED
**Date:** 2026-08-24
**Scientific result awarded:** none
**Authority created:** none
**Official pin, model, review, experiment, gravity paper, or ontology selection:** none

---

## 0. Executive result

The CP-CQ family-readiness audit found a strong mathematical class but no
single physical member. This gate asks whether the missing member can already
be selected by imposing the principles the family advertises:

$$
\text{complete positivity}
+\text{spatial covariance}
+\text{fixed Newtonian mean response}
+\text{conservation}
+\text{constraint propagation}.
\tag{1}
$$

The test separates two logically different questions. For the conditions that
are simultaneously defined on the same controlled weak-field member—complete
positivity, declared spatial covariance, and fixed mean response—the exact
answer is **no**. Exact conservation and full constraint propagation have not
been closed on that same member, so the stronger five-condition conjunction
is presently **untested**, not refuted.

For a finite Fourier-mode band of the continuous Markovian weak-field scalar
sector, complete positivity reduces mode by mode to

$$
2d_2(k)d_0(k)\ge |d_1(k)|^2.
\tag{2}
$$

After the mean-response coefficient $d_1(k)$ is fixed, every positive
symmetry-invariant function $f(k)$ and every nonnegative slack function
$s(k)$ define an admissible member through

$$
d_0(k)=f(k),
\qquad
d_2(k)=\frac{|d_1(k)|^2}{2f(k)}+s(k).
\tag{3}
$$

Conversely, every strictly positive solution has this form. The functions
$f$ and $s$ change decoherence and gravitational noise, so they are physically
inequivalent rather than gauge labels. Positivity, the spatial symmetry, and
the fixed mean response therefore define a convex admissible slice; they do not choose
the law of our universe.

Three further results sharpen the obstruction.

1. In the gravity normalization $4D_2\succeq D_0^{-1}$, saturating the bound
   still leaves an arbitrary positive function $D_0(k)$.
2. If both saturated kernels are required to be finite-order local scalar
   differential operators, their Fourier symbols must be constants. The only
   jointly local saturated solution is therefore ultralocal. The audited
   continuum controls associate that corner with uncontrolled ultraviolet
   heating or adverse constant-kernel behavior.
3. Exact conservation is an independent adjoint-generator equation. It is not
   implied by CP or covariance, and even when relational Lindblad operators
   conserve a total charge, their nonnegative rates remain unselected.

The present sources do not supply a closed nonlinear constraint/conservation
system that reduces this slice to a unique or finite source-fixed member.

The disposition is

$$
\boxed{
\begin{gathered}
\text{CP + SPATIAL COVARIANCE + FIXED MEAN RESPONSE: NONSELECTING,}\\
\text{SATURATION: NONSELECTING,}\\
\text{SATURATION + TWO-SIDED FINITE-ORDER LOCALITY: ULTRALOCAL CORNER,}\\
\text{CONSERVATION: INDEPENDENT DUTY / GENERALLY RATE-NONSELECTING,}\\
\text{FULL CONSTRAINT-CONSERVATION KERNEL SELECTION: NOT AVAILABLE.}
\end{gathered}}
\tag{4}
$$

The author-side ceiling is

$$
\boxed{
\text{KSG-L2 — EXACT WEAK-FIELD KERNEL UNDERDETERMINATION AND LOCALITY BOUNDARY.}
}
\tag{5}
$$

This is not a no-go theorem against classical gravity. It identifies the
additional physics a viable member must provide: a stable state and detailed
balance, a microscopic environment or memory law, a constraint-preserving
relational carrier, an RG fixed point that preserves CP, independently fixed
spectral data, or another explicit selector.

---

## 1. Binding scope

1. The exact theorem is finite dimensional and mode band limited.
2. It concerns the continuous Markovian scalar CP-CQ class.
3. It assumes a supplied weak-field spatial scaffold and Fourier modes.
4. The mean Newtonian response is held fixed rather than derived.
5. The theorem classifies a fixed-response slice of the CP coefficient cone;
   it does not classify every
   nonlinear or non-Markovian hybrid law.
6. Spatial covariance means invariance under the declared finite symmetry
   group of the retained mode set. It is not full spacetime diffeomorphism
   invariance.
7. The locality corollary separately assumes a continuum translation-
   invariant scalar differential-operator representation.
8. The locality corollary uses saturation of the CP trade-off. It does not
   apply to arbitrary positive slack.
9. The conservation discussion distinguishes expectation conservation,
   conservation of all moments, local continuity, and constraint propagation.
10. The Feng–Marletto–Vedral theorem is used only inside its one-way
    sequential classical-control class.
11. Oppenheim–Reznik relational Lindblad constructions show possibility in an
    enlarged relational quantum system; they do not themselves construct a
    CP-CQ gravity member.
12. Canonical, covariant, weak-field, renormalization, scattering, and
    dilation results remain separate.
13. A free kernel cannot be fitted after the target and then called selected.
14. No official candidate, pin, review, Paper 04B parent, Paper 06/07 model,
    experiment, or ontology follows.

---

## 2. Dependency and exact source receipts

The thirteen-source family classification is inherited from
`v17_mg0_postquantum_classical_gravity_family_pre_authorization_readiness_audit.md`
at SHA-256

```text
6607ef80595962de797aca6c5ac04b6073630e73e7f0e640aae03a555f20bf65
```

The present gate adds two exact conservation sources.

| source | exact version | bytes | SHA-256 | role |
|---|---:|---:|---|---|
| Oppenheim and Reznik, [*Fundamental destruction of information and conservation laws*](https://arxiv.org/abs/0902.2361) | `0902.2361v1` | 496079 | `6c36cc7167da3375fa6831873db59e877c0f534fa094467f7f5d7ce08fe6bffc` | relational Lindblad conservation and generalized Noether boundary |
| Feng, Marletto, Vedral, [*Conservation Laws and the Non-Classicality of Gravity*](https://arxiv.org/abs/2311.08971) | `2311.08971v5` | 402478 | `22c46a0ef1c2d4441fab4f12e97e20ddf746a0efab5ec6f4a20297bf84b5ad68` | additive-conservation no-go in a one-way sequential classical-control class |

The load-bearing inherited sources are:

- [the two-class CP-CQ theorem](https://arxiv.org/abs/2203.01332);
- [the decoherence–diffusion trade-off](https://arxiv.org/abs/2203.01982);
- [canonical gravity constraints](https://arxiv.org/abs/2011.15112);
- [covariant CQ path integrals](https://arxiv.org/abs/2302.07283);
- [the weak-field gravity member](https://arxiv.org/abs/2307.02557);
- [pure-gravity renormalization](https://arxiv.org/abs/2402.17844);
- [the canonical-relativity divergence critique](https://arxiv.org/abs/2404.07723);
- [constant-kernel scattering](https://arxiv.org/abs/2412.04839);
- [dilation and conservation controls](https://arxiv.org/abs/2506.15291); and
- [linearized stochastic gravity modes](https://arxiv.org/abs/2605.05375).

No secondary review is used to enlarge a primary claim.

---

## 3. The frozen finite-band domain

Let $K$ be a finite nonempty set of mode labels. Let a finite spatial symmetry
group $G$ act on $K$, and require $K$ to be closed under $k\mapsto-k$.

For each mode, retain a scalar quantum-decoherence coefficient $d_0(k)$, a
fixed backreaction coefficient $d_1(k)$, and a classical-diffusion coefficient
$d_2(k)$. Reality and symmetry require

$$
\begin{aligned}
d_j(gk)&=d_j(k), &&g\in G,\\
d_0(-k)&=d_0(k),\\
d_2(-k)&=d_2(k),\\
d_1(-k)&=d_1(k)^*.
\end{aligned}
\tag{6}
$$

The modewise CP block is

$$
B(k)=
\begin{pmatrix}
2d_2(k) & d_1(k)\\
d_1(k)^* & d_0(k)
\end{pmatrix}.
\tag{7}
$$

The fixed-response admissible set is

$$
\mathcal C_K(d_1)
=
\left\{
(d_0,d_2):B(k)\succeq0\ \text{for every }k\in K
\right\}.
\tag{8}
$$

The restriction to a finite band has four purposes.

1. No distributional kernel is needed.
2. No ultraviolet or infrared limiting claim is hidden in the theorem.
3. Positivity is ordinary finite matrix positivity.
4. Operational inequivalence can be tested one retained mode at a time.

If an exact selector already fails here, taking a continuum limit cannot make
the same premises uniquely selecting without adding new conditions.

---

## 4. The kernel-slice classification theorem

### Theorem K1 — complete parameterization

Assume $d_0(k)>0$ on every retained mode. Fix $d_1(k)$. Then

$$
(d_0,d_2)\in\mathcal C_K(d_1)
\tag{9}
$$

if and only if there exist functions

$$
f:K\to(0,\infty),
\qquad
s:K\to[0,\infty)
\tag{10}
$$

obeying the declared symmetries such that

$$
d_0(k)=f(k),
\qquad
d_2(k)=\frac{|d_1(k)|^2}{2f(k)}+s(k).
\tag{11}
$$

#### Proof

For a $2\times2$ Hermitian matrix with lower-right entry $d_0(k)>0$,
positivity is equivalent to positivity of its Schur complement:

$$
2d_2(k)-\frac{|d_1(k)|^2}{d_0(k)}\ge0.
\tag{12}
$$

Set $f(k)=d_0(k)$ and

$$
s(k)
=
d_2(k)-\frac{|d_1(k)|^2}{2d_0(k)}.
\tag{13}
$$

Then $f>0$ and $s\ge0$, giving Equation (11). Conversely, substituting
Equation (11) into the determinant gives

$$
\det B(k)=2f(k)s(k)\ge0,
\tag{14}
$$

while both diagonal entries are nonnegative. Hence $B(k)\succeq0$.
Symmetry is inherited modewise. $\square$

### 4.1 Null-support extension

If $d_0(k)=0$, block positivity requires $d_1(k)=0$. The coefficient $d_2(k)$
may then be any nonnegative symmetry-invariant value. Null decoherence can
therefore occur only on modes with no corresponding backreaction in this
class. This is the scalar form of the generalized-inverse support condition.

---

## 5. Exact nonselection consequences

### Corollary K1.1 — finite-orbit nonuniqueness

Let $K/G$ contain $N$ symmetry orbits on which $d_1\ne0$. Even after $d_1$ is
fixed, the saturated face $s=0$ contains at least one independent positive
number $f_a$ per orbit:

$$
f(k)=f_a
\quad\text{for }k\in\mathcal O_a.
\tag{15}
$$

Thus the premises do not select a unique law even on a finite band.

### Corollary K1.2 — continuum functional freedom

For a rotationally invariant continuum band, $f$ and $s$ may be arbitrary
admissible functions of $|k|$. The residual freedom is infinite dimensional.

### Corollary K1.3 — physical inequivalence

Choose two admissible functions $f\ne f'$ on a retained mode $k_0$. Then at
least one of

$$
d_0(k_0)\ne d'_0(k_0),
\qquad
d_2(k_0)\ne d'_2(k_0)
\tag{16}
$$

holds. The two members predict different decay of a matter coherence carrying
$k_0$, different classical noise at $k_0$, or both. They are therefore
operationally different members, not alternative descriptions of one law.

### Corollary K1.4 — slack nonselection

Even if another principle fixes $f$, complete positivity permits arbitrary
$s\ge0$. Saturating the trade-off is an additional physical postulate, not a
consequence of CP.

---

## 6. The gravity-normalized form

In the normalized weak-field member, the trade-off is written

$$
4D_2\succeq D_0^{-1}.
\tag{17}
$$

For commuting scalar Fourier kernels this becomes

$$
4d_2(k)\ge\frac{1}{d_0(k)}.
\tag{18}
$$

All strict solutions are

$$
d_0(k)=f(k)>0,
\qquad
d_2(k)=\frac{1}{4f(k)}+s(k),
\qquad
s(k)\ge0.
\tag{19}
$$

Saturation removes $s$ but not $f$:

$$
4d_2(k)d_0(k)=1.
\tag{20}
$$

The Newtonian drift/constraint fixes the mean Poisson response in the audited
member, while the source explicitly leaves the functional form of the
decoherence and diffusion kernels unspecified. Equation (19) makes that
residual selection problem exact.

---

## 7. Explicit hostile counterfamily

On a finite radial band $0<k_{\min}\le|k|\le k_{\max}$, fix the same mean
response and consider saturated members

$$
\begin{array}{lll}
F_0:&d_0(k)=\alpha,&d_2(k)=\dfrac{1}{4\alpha},\\[2mm]
F_1:&d_0(k)=\alpha(1+\ell^2|k|^2),
&d_2(k)=\dfrac{1}{4\alpha(1+\ell^2|k|^2)},\\[2mm]
F_2:&d_0(k)=\alpha e^{\ell^2|k|^2},
&d_2(k)=\dfrac{e^{-\ell^2|k|^2}}{4\alpha}.
\end{array}
\tag{21}
$$

For $\alpha,ell>0$, all three are positive, homogeneous, isotropic, and
saturate the same CP trade-off. They differ in their noise and decoherence
spectra.

Adding

$$
s(k)=\eta\frac{|k|^2}{1+\ell^2|k|^2},
\qquad \eta\ge0,
\tag{22}
$$

produces a further unsaturated family without altering the fixed mean drift.

No member in (21)–(22) is proposed as reality. Their purpose is to refute
selection by the frozen premises.

---

## 8. Saturation versus two-sided locality

### Theorem K2 — polynomial-inverse rigidity

Assume a translation-invariant continuum scalar sector in which

$$
D_0=p(-\Delta),
\qquad
D_2=q(-\Delta),
\tag{23}
$$

and $p,q$ are real finite-degree polynomials that are strictly positive on
$[0,\infty)$. If the normalized trade-off is saturated on every Fourier mode,

$$
4D_2D_0=I,
\tag{24}
$$

then $p$ and $q$ are positive constants.

#### Proof

In Fourier space, Equation (24) is

$$
4p(|k|^2)q(|k|^2)=1
\tag{25}
$$

for every $|k|^2\ge0$. Therefore the polynomial

$$
4p(x)q(x)-1
\tag{26}
$$

vanishes on an infinite set and is identically zero. Hence

$$
\deg p+\deg q=0,
\tag{27}
$$

so both degrees vanish. $\square$

### 8.1 Physical meaning

For finite-order scalar differential kernels, simultaneous locality plus
saturation forces the ultralocal constant-symbol corner. A nonconstant
saturated spectrum requires at least one inverse/nonlocal/pseudodifferential
kernel.

The theorem does not say nonlocality is forbidden. It says that the theory
must name and justify where it enters.

### 8.2 The locality boundary

The audited Diósi control shows that distributionally local Markovian
decoherence and diffusion kernels in relativistic point fields generate
uncontrolled local heating proportional to $\delta(0)$. The constant-kernel
Yukawa member separately exhibits no stable classical vacuum and adverse
scattering behavior.

Combining those source-scoped controls with Theorem K2 yields the conditional
boundary

$$
\boxed{
\begin{gathered}
\text{SATURATED + MARKOVIAN + SCALAR + TWO-SIDED FINITE-ORDER LOCAL}\\
\Longrightarrow
\text{ULTRALOCAL CORNER,}\
\text{WHICH REQUIRES A REGULATOR, NEW BALANCE LAW, OR ABANDONED PREMISE.}
\end{gathered}}
\tag{28}
$$

Allowed exits include:

1. positive slack above saturation;
2. a nonlocal spatial kernel;
3. non-Markovian spacetime correlations;
4. field-dependent kernels;
5. a finite physical regulator or discreteness scale;
6. additional tensor channels;
7. friction/detailed balance; or
8. a different fundamental matter–geometry carrier.

Each exit is new physical structure and must be charged.

---

## 9. Scale covariance narrows but does not select

### Theorem K3 — positive homogeneous spectra

Let $f:(0,\infty)\to(0,\infty)$ satisfy

$$
f(\lambda k)=\lambda^\sigma f(k)
\tag{29}
$$

for every $k,\lambda>0$. Then

$$
f(k)=c k^\sigma,
\qquad
c=f(1)>0.
\tag{30}
$$

#### Proof

Set $k=1$ and $\lambda=k$ in Equation (29). $\square$

At saturation,

$$
d_0(k)=c k^\sigma,
\qquad
d_2(k)=\frac{1}{4c}k^{-\sigma}.
\tag{31}
$$

Exact scale covariance therefore collapses functional freedom to an exponent
and coefficient, but it does not select the coefficient. Dimensional analysis
may fix $\sigma$ after the carrier and action are supplied; it still does not
determine $c$.

The pure-gravity renormalization programme may further restrict running
couplings and pole prescriptions. Its source-fixed result is presently
pure-gravity and partial; it does not select the matter-coupled kernel or prove
that the RG flow preserves the admissible positive coupling region.

---

## 10. Conservation is an independent equation

Let $\mathcal L$ be the generator of a normalized dynamical semigroup and
$\mathcal L^\dagger$ its Heisenberg adjoint. An observable $Q$ has conserved
expectation for every admitted state if

$$
\mathcal L^\dagger Q=0.
\tag{32}
$$

Conservation of its complete distribution is stronger and may require

$$
\mathcal L^\dagger Q^n=0
\tag{33}
$$

for an appropriate separating family of powers or spectral projectors.
Local conservation is stronger again: it requires a continuity equation and
boundary flux.

Neither block positivity (7) nor covariance of the coefficient functions
implies Equation (32). The Hotta–Murk–Terno rotationally invariant CP-CQ toy
model is an explicit counterexample: the equations are rotationally invariant
while total angular momentum decays.

### 10.1 Rate-nonselection under exact conservation

For a Lindblad generator

$$
\mathcal L(\rho)
=
-i[H,\rho]
+\sum_a\gamma_a
\left(
L_a\rho L_a^\dagger
-\frac12\{L_a^\dagger L_a,\rho\}
\right),
\tag{34}
$$

if

$$
[H,Q]=0,
\qquad
[L_a,Q]=0
\tag{35}
$$

for every $a$, then $\mathcal L^\dagger Q=0$ for every choice of rates
$\gamma_a\ge0$.

Thus even exact conservation generally constrains the admissible operators
without selecting their rates. Relational Lindblad operators can commute with
a total momentum while changing subsystem momenta, as constructed by
Oppenheim and Reznik. The interaction can be nontrivial and exactly conserve
the total charge, but the relational carrier and rate law are additional
physics.

### 10.2 The one-way sequential no-go

Feng, Marletto, and Vedral assume a strict classical sector with one preferred
observable and infinitesimal dynamics decomposable into:

1. sector-local operations; followed by
2. classical-to-quantum controlled channels;

with no quantum-to-classical control capable of generating nonclassical
correlations. Inside that class, exact additive conservation forbids the
classical system from changing the corresponding local quantum observable.

This is a strong hostile control. It does not automatically apply to a CP-CQ
backreaction law in which quantum information stochastically changes the
classical distribution, to a theory with an explicit noise/reference carrier,
or to a non-Markovian whole-process law.

The correct fork is

$$
\begin{array}{ll}
\text{one-way sequential classical control}
&\Rightarrow\text{exact-exchange no-go at the theorem scope},\\
\text{genuine CQ feedback or enlarged carrier}
&\Rightarrow\text{the no-go hypothesis is left; conservation must be rebuilt}.
\end{array}
\tag{36}
$$

Leaving the hypothesis is not a pass. It identifies the missing carrier and
balance law.

---

## 11. Constraint propagation is not yet a selector theorem

For constraints $C_a$, a candidate needs a typed relation such as

$$
\mathcal L^\dagger C_a
=
\sum_b M_a{}^b C_b
\tag{37}
$$

on the physical domain, or its covariant path-integral/BRST counterpart.

The audited canonical discrete class derives generalized constraints but does
not close their algebra without additional constraints or restricted lapse and
shift. The covariant path-integral family supplies diffeomorphism-invariant
examples and linearized mode/constraint progress, but not one full nonlinear
matter-coupled proof of Equation (37).

Consequently, the proposition

$$
\text{full constraints select }D_0,D_2
\tag{38}
$$

is presently neither proved nor refuted. It cannot be used to choose a member
before the constraint equations and their solution class are printed.

Even a future closure proof need not imply uniqueness. Gauge theories and GR
normally admit coupling constants, states, boundary data, and physically
different solutions after their constraints close.

---

## 12. Stable vacuum and detailed balance: the missing physical lever

The constant-kernel scattering control exposes a deeper problem: pure
diffusion without friction has no stable classical vacuum. A stationary state
requires a balance between drift/damping and diffusion.

For a linear mode with drift matrix $A$, covariance $\Sigma$, and noise
$D_2$, stationarity has the Lyapunov form

$$
A\Sigma+\Sigma A^\dagger+2D_2=0.
\tag{39}
$$

Equation (39) can restrict $D_2$ only after the theory supplies:

1. the damping/friction $A$;
2. the physical stationary or vacuum covariance $\Sigma$;
3. the time or relational ordering used to define stationarity;
4. the degrees that receive the compensating energy and momentum; and
5. the microscopic reason for detailed balance.

An external heat bath can provide these ingredients in an effective theory.
A fundamental theory of the universe cannot hide that bath outside the model.

This suggests a higher-leverage selector than saturation alone:

$$
\boxed{
\text{CP} + \text{CONSTRAINTS} + \text{CONSERVATION}
+\text{STABLE VACUUM/DETAILED BALANCE}.}
\tag{40}
$$

No audited CP-CQ gravity member yet closes Equation (40) with interacting
matter and without an unaccounted environment.

---

## 13. Additional physics that could select a member

| possible selector | what it must determine | principal danger |
|---|---|---|
| relational conservation law | carrier, charge flow, admissible Lindblad operators and rates | reference/environment smuggled in |
| stable vacuum/detailed balance | damping, diffusion, state, temperature or ground condition | external bath or clock hidden |
| nonlinear constraint closure | tensor kernels and gauge-compatible support | existence without uniqueness |
| Lorentz-covariant memory law | spacetime kernel and causal composition | non-Markovian target action inserted |
| RG fixed point preserving CP | coupling flow, pole prescription, UV completion | pure-gravity pass donated to matter |
| microscopic quantum dilation | environment, initial state, coupling and pointer algebra | quantum answer merely renamed |
| cosmological boundary law | state and long-wavelength spectrum | contingent state mistaken for law |
| empirical spectral calibration | finite parameters measured independently | fitted function with no prediction |
| new indivisible joint ontology | complete matter–geometry law and records | contextual lookup table |

None is free. A valid selector must reduce the admissible set before held-out evaluation
and expose a possible failure result.

---

## 14. Hostile counterfamilies and attacks

### 14.1 Mathematical attacks

1. **Orbit freedom:** change $f$ on one symmetry orbit.
2. **Slack freedom:** hold $f$ fixed and vary $s\ge0$.
3. **Null mode:** set $d_0=d_1=0$ and vary $d_2$.
4. **Matrix rotation:** in a multi-channel member, rotate within a degenerate
   positive kernel subspace.
5. **Generalized-inverse ambiguity:** alter coefficients on the null support.
6. **Band extension:** two members agree on calibrated modes and differ on a
   held-out mode.

### 14.2 Locality and continuum attacks

7. **Inverse-kernel attack:** a local $D_0$ produces nonlocal saturated $D_2$.
8. **Ultralocal heating:** both kernels become delta-local and generate a UV
   divergence.
9. **Cutoff selection:** a regulator is chosen after seeing the bound.
10. **Discreteness laundering:** a numerical grid is called fundamental.
11. **Finite-band overclaim:** the exact finite theorem is extrapolated to all
    continuum modes.
12. **Lorentz slide:** spatial isotropy is called spacetime covariance.

### 14.3 Conservation attacks

13. **Symmetry-equals-conservation:** covariance is used instead of
    $\mathcal L^\dagger Q=0$.
14. **Mean-only balance:** first-moment conservation hides variance growth.
15. **Noise sink:** missing charge is assigned to an unrecorded noise field.
16. **Apparatus sink:** source supports absorb momentum outside the parent.
17. **Relational carrier omission:** a reference needed for conservation is
    not included in the state.
18. **Feng overreach:** a one-way-control theorem is applied to genuine
    bidirectional feedback.
19. **Feng evasion:** “feedback” is asserted without a CP joint construction.
20. **Rate freedom:** conserved relational operators are fixed but their rates
    remain arbitrary.

### 14.4 Constraint and state attacks

21. **Initial-only constraint:** the constraint holds at one slice and drifts.
22. **Gauge-noise confusion:** a constraint mode is sampled as a physical
    stochastic degree.
23. **Linearized donation:** quadratic closure is called nonlinear closure.
24. **Vacuum-by-declaration:** a delta field state immediately diffuses.
25. **Friction retrofit:** damping is added only after instability appears.
26. **KMS import:** a temperature/time flow is supplied without physical
    origin.
27. **Cosmology-law merge:** an initial spectrum is called a coupling law.

### 14.5 Empirical attacks

28. **Kernel fitting:** a free function absorbs every dataset.
29. **Member switching:** different kernels are used for decoherence, noise,
    and scattering tests.
30. **Bound reuse:** calibration data are reported as validation.
31. **Composite-body shortcut:** macroscopic transfer is assumed.
32. **Null flexibility:** every null is blamed on a different cutoff or
    memory scale.
33. **No complete record:** only a selected variance, not the full profile, is
    predicted.

---

## 15. What a genuine selection theorem must prove

A future theorem must freeze:

1. the carrier and physical mode algebra;
2. the mean response $d_1$;
3. the full CP admissible set at fixed response;
4. the spatial and spacetime symmetry group;
5. locality or the allowed nonlocality class;
6. constraint propagation;
7. charge and boundary-flux conservation;
8. the vacuum/stationary state and its stability;
9. Markovian memory or its replacement;
10. ultraviolet behavior and regulator origin;
11. material readers and complete records;
12. parameter provenance; and
13. the exact equivalence relation under which two kernels are the same law.

It must then show one of:

$$
\begin{aligned}
&\text{unique member modulo physical equivalence};\\
&\text{finite predeclared family};\\
&\text{residual parameters independently calibratable};\\
&\text{empty admissible class};\\
&\text{or irreducible contingent/cosmological input explicitly identified}.
\end{aligned}
\tag{41}
$$

“Choose the simplest kernel” is not a theorem unless simplicity is a fixed
physical principle with a hostile countercontrol.

---

## 16. MG0 consequences

The result changes the MG0 routing in four precise ways.

1. A CP-CQ **family** cannot enter the reciprocal benchmark; only a fixed
   member can.
2. The weak-field trade-off is a consistency condition, not a selector law.
3. Conservation must include the noise/reference/apparatus carrier rather
   than being inferred from covariance.
4. Stable-vacuum and detailed-balance duties must be added to any future
   member freeze.

The result does not change:

1. MG0's form-neutrality;
2. the prohibition on using gravity to select an incomplete matter ontology;
3. the requirement for two genuinely different complete matter laws;
4. the closure of Papers 06/07; or
5. the absence of an official gravity model.

---

## 17. Outcome ladder

### KSG-L0 — ill-typed comparison

The response, decoherence, and diffusion kernels act on different unprinted
spaces or use incompatible conventions.

### KSG-L1 — CP admissible set reconstructed

The coefficient space and positivity conditions are source-fixed, but member
selection is not tested.

### KSG-L2 — exact underdetermination and locality boundary

The finite-band fixed-response slice is parameterized, counterfamilies are explicit,
saturation nonselection is proved, and the two-sided locality corollary is
derived.

**Current level.**

### KSG-L3 — conservation/constraint selector equations closed

One full member class has exact charge balance, stable constraint propagation,
and a typed physical quotient.

### KSG-L4 — finite or unique source-fixed member family

The added physics reduces the admissible set to a unique member, a finite family, or
independently calibratable parameters.

### KSG-L5 — stable vacuum and matter closure

The same member has a stable state, interacting matter, controlled UV
behavior, and complete readers.

### KSG-L6 — prospective transfer readiness

One member can be pinned before held-out matter–gravity evaluation.

No official rung follows from this author-side ladder.

---

## 18. Maximum legitimate claim

The strongest justified statement is:

> In the finite-band continuous Markovian scalar CP-CQ weak-field class,
> complete positivity, declared spatial covariance, and a fixed mean
> backreaction determine a convex admissible set rather than a unique decoherence and
> diffusion law. Saturating the trade-off still leaves an arbitrary positive
> spectral function. Requiring both saturated kernels to be finite-order local
> scalar differential operators forces the ultralocal constant-symbol corner,
> whose continuum realizations face the audited heating and stability
> controls. Exact conservation is a separate adjoint-generator condition and
> generally leaves rates unselected. No published full nonlinear
> matter-coupled constraint/conservation theorem presently collapses this
> freedom to a freeze-ready gravity member.

The following claims are barred:

1. CP-CQ gravity is impossible;
2. gravity must be quantum;
3. all relativistic hybrid kernels diverge;
4. conservation forbids every classical mediator;
5. covariance fixes the noise spectrum;
6. saturation is physically mandatory;
7. an RG argument already selects the matter theory;
8. the finite-band theorem decides the continuum;
9. a field-dependent kernel can be selected after observing the target; or
10. a stable vacuum can be declared without a balance law.

---

## 19. Routing decision

```text
FINITE-BAND FIXED-RESPONSE CP SET:    EXACTLY PARAMETERIZED
FIXED MEAN RESPONSE:                  DOES NOT SELECT DECOHERENCE/DIFFUSION
SPATIAL COVARIANCE:                   ORBIT/FUNCTIONAL FREEDOM REMAINS
SATURATION:                           SLACK REMOVED / FUNCTION REMAINS
TWO-SIDED FINITE-ORDER LOCALITY:      CONSTANT-SYMBOL CORNER ONLY
CONSERVATION FROM CP/COVARIANCE:      DOES NOT FOLLOW
CONSERVATION RATE SELECTION:          DOES NOT FOLLOW GENERALLY
FULL NONLINEAR CONSTRAINT SELECTION:  NOT AVAILABLE
STABLE VACUUM/DETAILED BALANCE:       MISSING PHYSICAL LEVER
AUTHOR-SIDE CEILING:                  KSG-L2
FREEZE-READY CP-CQ MEMBER:            NONE
OFFICIAL MG0 AUTHORITY:               NONE
ONTOLOGY/QUANTUM-GRAVITY VERDICT:     NONE
```

The highest-value next author-side question is whether a closed-system stable
vacuum and exact relational conservation can be formulated for one covariant
member without importing an external bath, target spectrum, or quantum
dilation as the answer. This gate does not authorize that member or an
official successor.
