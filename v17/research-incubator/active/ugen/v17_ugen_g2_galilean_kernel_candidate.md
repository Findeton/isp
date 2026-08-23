# ISP v17 — U-Gen G2 Galilean kernel candidate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS/PHYSICS CANDIDATE / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Question and bounded answer

G1 left its magnitude data and phase-complete carrier as independent inputs.
G2 asks the narrowest physical question that can reduce that debt without
inventing a new microscopic ontology:

> In the fixed-background, free, spinless, nonrelativistic one-particle sector,
> do projective Galilei covariance and exact composition determine the coherent
> endpoint carrier? If they do, is that carrier itself an ordinary-positive
> transition law on position?

The author-side answer is asymmetric.

1. A strongly continuous irreducible **projective unitary** representation of
   the Galilei group, with nonzero mass central charge, fixes the free generator
   to

   $$
   H=\frac{P^2}{2m}+E_0I
   $$

   and hence fixes the standard oscillatory free kernel, up to the energy-origin
   phase and distributional branch.
2. This is a genuine reduction of the free aggregate-kernel oracle, but it is
   not a derivation of quantum theory from Galilean relativity. Projective
   unitarity, complex or oriented-real composition, the position system,
   $m$, $\hbar$, Euclidean spatial geometry, and external time are premises.
3. The real-time kernel is not an ordinary transition density on exact
   position. Its modulus square is constant in space and nonintegrable.
4. For normalized preparations and finite-resolution records, ordinary record
   probabilities are exact, but they depend on the full phase-complete
   preparation and instrument. They do not form a universal position-only
   Markov kernel.
5. The continuation $t=-i\tau$ yields the positive heat kernel with
   $\nu=\hbar/(2m)$, which is a genuine Markov semigroup when the energy origin
   is removed. This is Euclidean-time probability, not automatically physical
   real-time actuality.

No level is awarded before a separate pin and independent review.

---

## 1. Exact input contract

### 1.1 Declared physical control sector

G2 fixes one control theory, not a fundamental universe:

$$
\mathfrak G_2=
(d,\mathbb R^d,dx,t,m,\hbar,\mathcal H,X,P,J,B,H,U).
$$

The entries are:

1. a supplied integer $d\geq1$;
2. flat Euclidean configuration space $\mathbb R^d$ with Lebesgue measure
   $dx$;
3. an external Newtonian time parameter $t\in\mathbb R$;
4. a fixed positive mass $m$;
5. a fixed positive action scale $\hbar$;
6. the one-particle Hilbert carrier

   $$
   \mathcal H=L^2(\mathbb R^d,dx);
   $$

7. the standard position system $X$ and translation generators $P_i$;
8. rotations $J_{ij}$ and boosts $B_i$;
9. a strongly continuous irreducible projective unitary Galilei
   representation with mass central charge $m$; and
10. a time-translation group

   $$
   U_t=e^{-itH/\hbar}.
   $$

The representation is restricted to one free spinless sector. Internal energy
may contribute one scalar $E_0I$.

### 1.2 Premises explicitly not derived

G2 does not derive:

1. why nature uses rays, unitary maps, or an oriented two-real-dimensional
   correlation carrier;
2. the Born record rule;
3. $m$, $\hbar$, $d$, flatness, Lebesgue measure, or external time;
4. the physical existence of exact position eigenstates;
5. one actual continuous path;
6. an interaction, apparatus, field, QFT, or gravity law;
7. a fundamental distinction between real and imaginary time; or
8. a cosmological state or boundary condition.

The word **free** means that the representation contains no independently
supplied interaction operator. Galilei invariance alone permits many-body
relative-coordinate interactions and therefore cannot select a general
interacting Hamiltonian.

---

## 2. Proposition G2-A — the free generator inside a quantum Galilei sector

Use the centrally extended Galilei commutators

$$
[B_i,P_j]=i\hbar m\delta_{ij}I,
\qquad
[B_i,H]=i\hbar P_i,
$$

together with the usual translation and rotation relations. Define

$$
C:=H-\frac{P^2}{2m}.
$$

Then

$$
\begin{aligned}
[B_i,P^2]
&=\sum_j\bigl([B_i,P_j]P_j+P_j[B_i,P_j]\bigr)\\
&=2i\hbar mP_i,
\end{aligned}
$$

so

$$
[B_i,C]=0.
$$

$C$ also commutes with translations, rotations, and time translations in the
free irreducible sector. Schur's lemma therefore gives

$$
\boxed{H=\frac{P^2}{2m}+E_0I.}
$$

### Scope of the derivation

This proposition derives the dispersion relation **inside** the declared
projective unitary representation. It does not show that classical Galilean
relativity forces a Hilbert space, a complex phase, or the central extension.
The mass cocycle and the quantum carrier are load-bearing premises.

$E_0$ is the internal-energy Casimir. Within one closed real-time sector it
contributes only a common phase. It becomes nontrivial for Euclidean
normalization, superposed mass/internal-energy sectors, or coupling to gravity.

---

## 3. Proposition G2-B — free real-time coherent kernel

For $t\neq0$, define the distributional kernel

$$
K_t(x,y)=\langle x|U_t|y\rangle.
$$

Fourier resolution gives

$$
K_t(x,y)
=\frac1{(2\pi\hbar)^d}
\int_{\mathbb R^d}d^dp\,
\exp\!\left[
\frac{i}{\hbar}p\cdot(x-y)
-\frac{it}{\hbar}\left(\frac{p^2}{2m}+E_0\right)
\right].
$$

For $t>0$, the boundary-value Gaussian is

$$
\boxed{
K_t(x,y)=
e^{-iE_0t/\hbar}
\left(\frac{m}{2\pi i\hbar t}\right)^{d/2}
\exp\!\left[
\frac{im|x-y|^2}{2\hbar t}
\right].}
$$

For $t<0$, the distributional branch is fixed by

$$
K_{-t}(x,y)=\overline{K_t(y,x)}.
$$

The limit $t\to0$ is not pointwise. It is the distributional identity

$$
K_t\longrightarrow\delta(x-y).
$$

### 3.1 Exact coherent composition

For composable times $s,t$,

$$
\boxed{
\int_{\mathbb R^d}d^dz\,
K_t(x,z)K_s(z,y)=K_{t+s}(x,y).}
$$

This follows directly from the momentum representation or oscillatory Gaussian
composition. Unitarity is the distinct identity

$$
\int d^dz\,
K_t(x,z)\overline{K_t(y,z)}
=\delta(x-y).
$$

The second identity—not an $L^1$ normalization of $|K_t|^2$—is what preserves
the norm of a wavepacket.

### 3.2 What G2 has actually derived

Within the frozen control sector, G2 determines:

1. the free dispersion relation;
2. the endpoint phase $m|x-y|^2/(2\hbar t)$;
3. the time-dependent prefactor;
4. the distributional branch fixed by identity and unitarity; and
5. exact coherent concatenation.

It does **not** determine a countably additive fine-path amplitude measure
$a(h)$ on continuum histories. It derives the aggregate free kernel and its
finite-slice factor, not G1's general interacting history magnitude law.

---

## 4. Proposition G2-C — exact-position modulus-square obstruction

For every $t\neq0$,

$$
|K_t(x,y)|^2
=\left(\frac{m}{2\pi\hbar|t|}\right)^d.
$$

Therefore

$$
\int_{\mathbb R^d}d^dx\,|K_t(x,y)|^2=\infty.
$$

Consequently,

$$
\boxed{|K_t(x,y)|^2\text{ is not a transition-probability density in }x.}
$$

There are three mutually reinforcing reasons.

1. The integral diverges.
2. $K_t$ has units $L^{-d}$, so $|K_t|^2$ has units $L^{-2d}$ rather than the
   $L^{-d}$ required of a position density.
3. $|y\rangle$ is a generalized vector, not a normalized state in
   $L^2(\mathbb R^d)$.

Dividing by the infinite integral is not a probability construction. Boxing,
latticizing, or coarse-graining the theory changes the preparation and record
interface and must be charged as a regulator or physical instrument.

### 4.1 The obstruction does not refute positive ontology

This proposition excludes one specific identification:

$$
p_t(x\mid y)\stackrel{\rm false}{=}|K_t(x,y)|^2
$$

on exact continuum position. It does not exclude:

1. ordinary probabilities for normalized preparations and records;
2. an indivisible first-order law on a finite or operational state space;
3. positive paths on an enlarged state including phase/current data;
4. Nelson, Bohm, Bell, collapse, or other actuality laws; or
5. a positive whole-experiment law that is not a position Markov process.

---

## 5. Proposition G2-D — position density alone is not future sufficient

Suppose a state-independent positive position kernel $p_t(x\mid y)$ reproduced
the free quantum evolution of every normalized preparation through

$$
\rho_t(x)=\int d^dy\,p_t(x\mid y)\rho_0(y).
$$

Choose normalized wavepackets $\phi_L,\phi_R$ with disjoint initial support and
define

$$
\psi_\theta
=\frac1{\sqrt2}
\bigl(\phi_L+e^{i\theta}\phi_R\bigr).
$$

All $\theta$ have the same initial density,

$$
|\psi_\theta|^2
=\frac12\bigl(|\phi_L|^2+|\phi_R|^2\bigr).
$$

After free propagation, once the packets overlap,

$$
|U_t\psi_\theta|^2
=\frac12\left(
|U_t\phi_L|^2+|U_t\phi_R|^2
+2\operatorname{Re}
\left[e^{i\theta}(U_t\phi_R)
\overline{(U_t\phi_L)}\right]
\right),
$$

which generally depends on $\theta$. A kernel acting only on $\rho_0$ would
predict the same future density for every $\theta$, a contradiction.

Thus

$$
\boxed{
\text{exact position density is not a positive future-sufficient cut for
all free quantum preparations}.}
$$

This is not a no-go for all positive stochastic theories. It proves that the
missing relational phase/current information must live somewhere: in an
enlarged state, a context, a non-Markov/indivisible whole law, a pair-history
object, or an imported quantum carrier.

---

## 6. Finite-resolution operational probability is exact but contextual

Let $\psi_0\in L^2(\mathbb R^d)$ be normalized and let

$$
\{E_r\}_{r\in R},
\qquad
E_r\geq0,
\qquad
\sum_rE_r=I,
$$

be a declared finite-resolution record POVM. Then

$$
\boxed{
p(r\mid\psi_0,t,\mathcal E)
=\langle\psi_0,
U_t^\dagger E_rU_t\psi_0\rangle}
$$

is an ordinary normalized record law.

This is not a universal $p_t(x\mid y)$. It depends on:

1. the full phase-complete preparation $\psi_0$;
2. the detector effects $E_r$;
3. the external duration $t$;
4. the fixed Hamiltonian and background; and
5. any physical intermediate instrument.

A narrow packet $\phi_{y,\sigma}$ can approximate a localized preparation,
but the resulting record law depends on its width, shape, phase, and detector.
The formal $\sigma\to0$ limit does not create a normalized exact-position
transition density on all of $\mathbb R^d$.

---

## 7. Proposition G2-E — an intermediate position instrument is a division

Let $s\in(0,t)$ and let $\{M_z\}$ be a complete registered intermediate
instrument with

$$
\sum_zM_z^\dagger M_z=I.
$$

If the outcome $z$ becomes a stable, future-sufficient record, the joint record
law is

$$
p(z,r)
=\left\|
E_r^{1/2}U_{t-s}M_zU_s\psi_0
\right\|^2.
$$

The unconditioned later probability is

$$
p_{\rm rec}(r)=\sum_zp(z,r).
$$

Without that physical instrument, the coherent law is

$$
p_{\rm unrec}(r)
=\left\|E_r^{1/2}U_t\psi_0\right\|^2.
$$

In general,

$$
p_{\rm rec}(r)\neq p_{\rm unrec}(r).
$$

Inserting the identity

$$
I=\int d^dz\,|z\rangle\langle z|
$$

inside an amplitude is not a physical division. Replacing the coherent
integral by a sum of squared terms describes a measurement/dephasing
interaction and is a different experiment.

This is the continuum operational counterpart of G1's retained-record versus
coherent-eraser distinction.

---

## 8. Finite unistochastic control and Barandes indivisibility

On a finite operational carrier, a unitary matrix $U_t$ defines

$$
\Gamma_t(j\mid i)=|(U_t)_{ji}|^2,
$$

which is column-stochastic. Yet coherent composition gives

$$
\Gamma_{t+s}(k\mid i)
=\left|
\sum_j(U_t)_{kj}(U_s)_{ji}
\right|^2,
$$

whereas a positive restart at the intermediate basis gives

$$
(\Gamma_t\Gamma_s)(k\mid i)
=\sum_j|(U_t)_{kj}|^2|(U_s)_{ji}|^2.
$$

Cross terms make these unequal generically:

$$
\boxed{\Gamma_{t+s}\neq\Gamma_t\Gamma_s.}
$$

That inequality is not a normalization defect. It is the precise reason a
Barandes-style unistochastic endpoint law can be ordinary-positive and still
indivisible through an unrecorded intermediate basis.

The continuum free kernel adds a separate warning: generalized exact-position
columns are not normalized states, so finite-dimensional unistochastic
language cannot be transferred to $|K_t(x,y)|^2$ without specifying physical
preparations, records, and measure.

---

## 9. Proposition G2-F — Euclidean continuation gives a positive semigroup

For $\tau>0$, analytically continue

$$
t=-i\tau.
$$

Then

$$
T_\tau=e^{-\tau H/\hbar}
$$

has free kernel

$$
H_\tau(x,y)
=e^{-E_0\tau/\hbar}
\left(\frac{m}{2\pi\hbar\tau}\right)^{d/2}
\exp\!\left[-\frac{m|x-y|^2}{2\hbar\tau}\right].
$$

Choose the energy origin $E_0=0$ and set

$$
\nu=\frac{\hbar}{2m}.
$$

Then

$$
\boxed{
H_\tau(x,y)
=\frac1{(4\pi\nu\tau)^{d/2}}
\exp\!\left[-\frac{|x-y|^2}{4\nu\tau}\right].}
$$

This kernel satisfies

$$
H_\tau(x,y)\geq0,
\qquad
\int d^dx\,H_\tau(x,y)=1,
$$

and the Chapman--Kolmogorov law

$$
\int d^dz\,H_\tau(x,z)H_\sigma(z,y)
=H_{\tau+\sigma}(x,y).
$$

It is exactly the transition density of Brownian motion with diffusion
coefficient $\nu$.

### 9.1 The energy-origin control

For $E_0\neq0$,

$$
\int d^dx\,H_\tau(x,y)=e^{-E_0\tau/\hbar}.
$$

An additive energy constant is a common phase in one closed real-time sector,
but it changes Euclidean mass normalization. Obtaining a Markov kernel requires
fixing or renormalizing the energy origin. Analytic continuation therefore does
not preserve every item that was operationally gauge-like in real time.

---

## 10. Real time and Euclidean time are not two names for one probability law

The two carriers have different mathematical and physical types:

| coordinate | real time | Euclidean parameter |
|---|---|---|
| evolution | unitary group $e^{-itH/\hbar}$ | positive contraction semigroup $e^{-\tau H/\hbar}$ |
| kernel | oscillatory distribution | heat kernel |
| composition | coherent amplitude integral | Chapman--Kolmogorov integral |
| reversibility | group inverse exists | inverse is generally unbounded/non-Markov |
| norm | $L^2$ norm preserved | $L^2$ contraction; $L^1$ Markov only after conditions |
| path object | no ordinary Wiener measure supplied | Wiener measure exists in free case |
| boosts | projective unitary phase | continued boost factor is not a unit-modulus phase |

The formal substitution $t=-i\tau$ maps equations and kernels under analytic
conditions. It does not establish that $\tau$ is an actual clock reading, that
Brownian paths occur in real time, or that real-time quantum interference is a
hidden ordinary Markov process.

---

## 11. Time slicing: where a positive path measure appears and disappears

For $t=N\epsilon$, the real-time free kernel has the formal cylinder limit

$$
\begin{aligned}
K_t(x_N,x_0)
=\lim_{N\to\infty}
&\left(\frac{m}{2\pi i\hbar\epsilon}\right)^{Nd/2}
\int\prod_{j=1}^{N-1}d^dx_j\\
&\times
\exp\!\left[
\frac{im}{2\hbar\epsilon}
\sum_{j=1}^{N}|x_j-x_{j-1}|^2
\right].
\end{aligned}
$$

Every factor is oscillatory. Taking absolute values destroys the cancellations
that produce the distributional identity and coherent composition. On
unbounded space the absolute integral is already divergent.

For $\tau=N\epsilon$, the Euclidean expression is

$$
\begin{aligned}
H_\tau(x_N,x_0)
=\lim_{N\to\infty}
&\left(\frac{m}{2\pi\hbar\epsilon}\right)^{Nd/2}
\int\prod_{j=1}^{N-1}d^dx_j\\
&\times
\exp\!\left[-
\frac{m}{2\hbar\epsilon}
\sum_{j=1}^{N}|x_j-x_{j-1}|^2
\right],
\end{aligned}
$$

whose finite-dimensional marginals define Wiener measure consistently.

Thus the free path-law fork is exact:

$$
\boxed{
\text{real time: coherent complex cylinder carrier}
\quad\leftrightarrow\quad
\text{Euclidean time: ordinary-positive Wiener law}.}
$$

The arrow is analytic continuation, not an ontological identification.

---

## 12. Potential and Feynman--Kac control

For

$$
H=-\frac{\hbar^2}{2m}\Delta+V,
$$

the Euclidean semigroup can, under standard analytic conditions, be represented
schematically by

$$
(e^{-\tau H/\hbar}f)(x)
=\mathbb E_x\!\left[
e^{-\hbar^{-1}\int_0^\tau V(X_s)ds}
f(X_\tau)
\right].
$$

The exponential is a path weight, killing, or amplification factor. The
resulting kernel is generally not normalized as a Markov transition law.
Producing a conservative diffusion may require an energy shift and a positive
ground-state/Doob transform. Those are additional spectral and boundary data,
not consequences of free Galilei symmetry.

Feynman--Kac therefore supplies a rigorous Euclidean bridge. It does not derive
the interacting real-time quantum law from an ordinary positive path ontology.

---

## 13. Relation to Nelson N1

G2 and N1 share the numerical scale

$$
\nu=\frac{\hbar}{2m}.
$$

But the heat kernel alone does not produce Nelson stochastic mechanics. N1
additionally supplies:

1. forward and backward drifts;
2. a time-dependent density $\rho$;
3. current and osmotic velocities;
4. a symmetric mean acceleration;
5. the mean-Newton law;
6. phase-complete initial current data; and
7. a global-sector rule, which N1 presently lacks.

Euclidean Brownian motion is consequently a prior-art scale and positivity
control for N1, not a derivation of N1's physical real-time path ontology.

---

## 14. Relation to G1 and the native-generator slot

G2 reduces one G1 debt at one sharply bounded scope:

| G1 coordinate | G2 free-sector status |
|---|---|
| endpoint coherent carrier $K_t$ | derived from quantum Galilei premises |
| endpoint magnitude/prefactor | derived distributionally |
| action phase | fixed as free classical action divided by $\hbar$ |
| fine-history positive magnitude $a(h)$ | not constructed |
| interaction | absent |
| stable record grammar | supplied instrument |
| complete adaptive process | absent |
| actuality | not selected |
| internal time | absent |

This earns input-origin progress only relative to supplying the entire free
kernel by hand. It does not fill the native ISP slot because the representation
that fixes the kernel is already projective quantum kinematics.

---

## 15. Relation to MG0 and gravity

G2 is a fixed-geometry quantum-limit control for a future MG0 candidate. It
shows what such a candidate must reproduce in a nonrelativistic free sector and
which parts are not ordinary position probability.

It supplies no matter--geometry law because it assumes:

1. fixed Euclidean configuration geometry;
2. external Newtonian time;
3. fixed mass;
4. no reciprocal source or response;
5. no constraints or diffeomorphism quotient; and
6. no GR or QFT limit.

Replacing $m$, $dx$, or $t$ by metric-dependent quantities would be a new
candidate and cannot be inferred from this packet.

---

## 16. Explanatory input ledger

| coordinate | status |
|---|---|
| Galilei group | declared low-energy spacetime symmetry |
| projective unitary representation | declared quantum premise |
| mass cocycle $m$ | sector label / not derived |
| action scale $\hbar$ | calibrated input / not derived |
| dimension and flat metric | declared control background |
| external time | declared control |
| free generator | derived within premises |
| real-time kernel and prefactor | derived within premises |
| ordinary exact-position transition law | refuted for $|K_t|^2$ |
| normalized record law | exact given normalized preparation and POVM |
| position-only future-sufficient cut | refuted for all phase sectors |
| Euclidean heat kernel | derived by analytic continuation |
| Euclidean Wiener path law | exact in free case |
| continuation as physical principle | absent |
| Nelson real-time actuality | not derived |
| interacting/QFT compiler | absent |
| internal time/gravity | absent |
| empirical deviation | none |

---

## 17. Permitted outcome ladder

No rung is presently awarded. A future review may assign at most one of:

### G2-L0 — PREMISE OR KERNEL FAILURE

The projective representation, generator derivation, branch, or composition
law is inconsistent.

### G2-L1 — FREE QUANTUM CARRIER RECONSTRUCTED

The free coherent kernel is derived inside the printed projective Galilei
sector, with no claim beyond that sector.

### G2-L2 — REAL-TIME POSITION-PROBABILITY OBSTRUCTION

L1 survives and $|K_t|^2$ is proved not to be a continuum exact-position
transition law; the phase-density future-sufficiency counterexample survives.

### G2-L3 — OPERATIONAL INDIVISIBILITY CONTROL

L2 survives together with exact finite-resolution record and
recorded/unrecorded-seam controls.

### G2-L4 — EUCLIDEAN POSITIVE-LAW FORK

L3 survives and the heat/Wiener semigroup is derived with all energy-origin,
potential, and clock-semantic caveats.

### G2-L5 — PHYSICAL CONTINUATION OR ACTUALITY PRINCIPLE

One independently motivated principle selects a physical path/referent and
connects it to real-time records without importing the quantum answer.

### G2-L6 — SCALABLE COMMON LAW

The same immutable law extends to interactions, adaptive instruments, QFT,
internal time, and reciprocal matter--geometry dynamics.

The author-side packet attempts only L1--L4. L5 and L6 remain empty.

---

## 18. Current author-side verdict

```text
FREE GENERATOR FROM PROJECTIVE GALILEI DATA:    DERIVED AT DECLARED SCOPE
FREE REAL-TIME COHERENT KERNEL:                 DERIVED AT DECLARED SCOPE
QUANTUM KINEMATICS FROM GALILEAN RELATIVITY:    NOT DERIVED
EXACT-POSITION |K|^2 TRANSITION DENSITY:        FAILS / NONNORMALIZABLE
POSITION DENSITY AS FUTURE-SUFFICIENT CUT:      FAILS FOR PHASE FAMILY
NORMALIZED FINITE-RECORD LAW:                   EXACT GIVEN PREP + INSTRUMENT
UNRECORDED INTERMEDIATE POSITION AS DIVISION:   REFUTED
FINITE UNISTOCHASTIC INDIVISIBILITY:            EXACT CONTROL
EUCLIDEAN HEAT / WIENER LAW:                    EXACT FREE CONTROL
REAL-TIME ACTUAL PATH FROM WICK ROTATION:       NOT DERIVED
G1 FINE-HISTORY MAGNITUDE LAW:                  NOT DERIVED
NELSON DYNAMICS:                                NOT DERIVED
INTERACTION / QFT / INTERNAL TIME / GRAVITY:    ABSENT
OFFICIAL PIN / REVIEW / RESULT:                 NONE
```

---

## 19. Maximum legitimate author-side claim

If the exact mathematics survives future review, G2 could claim only:

> Within a declared free spinless projective-unitary Galilei sector, symmetry,
> irreducibility, and composition fix the standard coherent propagator rather
> than an ordinary exact-position transition density. Its modulus square is
> nonnormalizable on continuum position, and position density alone is not
> future sufficient across relative-phase preparations. Imaginary-time
> continuation yields the positive heat/Wiener semigroup with
> $\nu=\hbar/(2m)$, but supplies no physical principle identifying Euclidean
> paths with real-time actuality. The result reduces one free-kernel input while
> locating the remaining ontology and clock law.

It could not claim:

1. derivation of quantum mechanics from classical symmetry;
2. proof that complex numbers are material;
3. impossibility of ordinary-positive quantum ontology;
4. derivation of Barandes' law;
5. derivation of Nelson dynamics;
6. a continuum fine-history probability law in real time;
7. an interaction, QFT, spacetime, or gravity law; or
8. an empirical discovery.

