# ISP v17 — U-Gen G2 positive-transition and Euclidean gate

**Status:** ACTIVE AUTHOR-SIDE CONTROL DOSSIER / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Purpose

This dossier tries to break the G2 candidate before any freeze. It separates
five statements that are often conflated:

1. projective Galilei symmetry fixes a free **quantum** generator;
2. that generator has a coherent distributional kernel;
3. normalized preparations and instruments have ordinary record
   probabilities;
4. the kernel modulus square is an exact-position transition probability;
5. Euclidean continuation supplies an actual real-time path law.

The first three are compatible. Statement 4 is false on
$\mathbb R^d$. Statement 5 is unearned.

All controls are analytic. No numerical scan, implementation, lattice, or
curve fit can alter the verdict.

---

## 1. Rebuild control G2-C1 — central-charge algebra

Assume

$$
[B_i,P_j]=i\hbar m\delta_{ij}I,
\qquad
[B_i,H]=i\hbar P_i.
$$

Then

$$
[B_i,P^2/(2m)]=i\hbar P_i,
$$

and

$$
[B_i,H-P^2/(2m)]=0.
$$

In one irreducible free spinless sector, the residual operator is central and
therefore scalar:

$$
H=P^2/(2m)+E_0I.
$$

### Mutants

1. **Zero-mass mutant:** $m=0$ invalidates the division and belongs to a
   different representation class.
2. **Reducible mutant:** a direct sum may carry distinct $E_0$ values; Schur's
   scalar conclusion then holds only blockwise.
3. **Interaction mutant:** $V(X)$ breaks boost commutation unless the enlarged
   physical system and transformation law are supplied.
4. **Classical-symmetry mutant:** delete the projective unitary carrier. The
   conclusion no longer follows.

The control therefore validates a conditional quantum-sector theorem, not a
symmetry-only derivation of quantization.

---

## 2. Rebuild control G2-C2 — Fourier branch and dimensions

For $t>0$,

$$
K_t(r)=\frac1{(2\pi\hbar)^d}
\int d^dp\,
e^{ip\cdot r/\hbar}
e^{-itp^2/(2m\hbar)}
$$

evaluates by the boundary prescription $t\mapsto t-i0$ to

$$
K_t(r)=
\left(\frac{m}{2\pi i\hbar t}\right)^{d/2}
e^{imr^2/(2\hbar t)}.
$$

The prefactor has units

$$
[K_t]=L^{-d},
$$

as required for

$$
\psi_t(x)=\int d^dy\,K_t(x-y)\psi_0(y).
$$

### Branch control

An arbitrary square-root phase fails at least one of:

1. the distributional $t\to0$ identity;
2. $K_{-t}(x,y)=\overline{K_t(y,x)}$; or
3. exact convolution.

The branch is therefore not a fitted fringe parameter.

---

## 3. Rebuild control G2-C3 — coherent convolution

In momentum space,

$$
\begin{aligned}
\int d^dz\,K_t(x,z)K_s(z,y)
&=\int\frac{d^dp\,d^dq}{(2\pi\hbar)^{2d}}
e^{ip\cdot x/\hbar-iq\cdot y/\hbar}\\
&\quad\times
e^{-itp^2/(2m\hbar)-isq^2/(2m\hbar)}
\int d^dz\,e^{i(q-p)\cdot z/\hbar}\\
&=\int\frac{d^dp}{(2\pi\hbar)^d}
e^{ip\cdot(x-y)/\hbar}
e^{-i(t+s)p^2/(2m\hbar)}\\
&=K_{t+s}(x,y).
\end{aligned}
$$

The delta distribution produced by the $z$ integral is the load-bearing
normalization. There is no intermediate stochastic sum in this identity.

---

## 4. Hostile control G2-C4 — kernel-as-probability mutant

The proposed transition density

$$
p_t(x\mid y)=|K_t(x,y)|^2
$$

has

$$
p_t(x\mid y)=
\left(\frac{m}{2\pi\hbar|t|}\right)^d
$$

and therefore

$$
\int d^dx\,p_t(x\mid y)=\infty.
$$

It also has units $L^{-2d}$. This is an exact type failure, not a numerical
normalization error.

### Disallowed repairs

1. Divide by $\infty$.
2. Choose an arbitrary finite window after seeing the detector range.
3. put space in a box and call the box emergent;
4. discretize position and omit the cell-volume dependence;
5. replace the generalized source $|y\rangle$ by a wavepacket without charging
   the wavepacket; or
6. call unitarity's delta orthogonality an $L^1$ normalization.

---

## 5. Positive control G2-C5 — normalized Gaussian preparation

In one dimension take

$$
\psi_0(x)=
\frac1{(2\pi\sigma^2)^{1/4}}
\exp\!\left[
-\frac{(x-x_0)^2}{4\sigma^2}
+\frac{ip_0x}{\hbar}
\right].
$$

Free evolution gives a normalized density centered at

$$
x_0+\frac{p_0t}{m}
$$

with variance

$$
\sigma_t^2
=\sigma^2+
\left(\frac{\hbar t}{2m\sigma}\right)^2.
$$

Thus

$$
|\psi_t(x)|^2
=\frac1{\sqrt{2\pi\sigma_t^2}}
\exp\!\left[
-\frac{(x-x_0-p_0t/m)^2}{2\sigma_t^2}
\right]
$$

is an ordinary probability density.

This control prevents overclaiming. The failure of $|K_t|^2$ does not mean
quantum theory lacks ordinary outcome probabilities. It means the normalized
preparation—not a position delta—is part of the experiment.

The dependence on $\sigma$ also defeats a claimed universal point-source
transition law.

---

## 6. Hostile control G2-C6 — same density, different phase

Let $\phi_L$ and $\phi_R$ have disjoint support. The family

$$
\psi_\theta=
\frac{\phi_L+e^{i\theta}\phi_R}{\sqrt2}
$$

has a common initial density. After overlap, the later density contains

$$
2\operatorname{Re}
\left[e^{i\theta}(U_t\phi_R)
\overline{(U_t\phi_L)}\right].
$$

Any positive transition law whose complete input is only $\rho_0(x)$ predicts
one common future density and fails at least two values of $\theta$.

### Escape branches that remain live

1. augment the state by a current, phase, connection, or predictive memory;
2. use a whole-process law that is not Markov through position density;
3. make the response contextual to the complete preparation;
4. use a pair-history/decoherence object; or
5. supply standard quantum dynamics plus a separate actuality law.

Every escape has a ledger cost. None is refuted by this control.

---

## 7. Exact finite control G2-C7 — indivisible unistochastic composition

Use the real rotation

$$
U(\theta)=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}
$$

and its endpoint law

$$
\Gamma(\theta)=|U(\theta)|^{\odot2}
=\begin{pmatrix}
\cos^2\theta&\sin^2\theta\\
\sin^2\theta&\cos^2\theta
\end{pmatrix}.
$$

Then

$$
\Gamma(\pi/4)^2
=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
$$

whereas

$$
\Gamma(\pi/2)
=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Thus

$$
\Gamma(\pi/2)
\neq
\Gamma(\pi/4)\Gamma(\pi/4).
$$

The coherent carrier composes; its entrywise square does not. An actual stable
record at the seam changes the experiment and licenses the stochastic product.

---

## 8. Instrument control G2-C8 — record versus inserted resolution

For a normalized state and a finite intermediate instrument $\{M_z\}$,

$$
p_{\rm rec}(r)
=\sum_z
\|E_r^{1/2}U_{t-s}M_zU_s\psi_0\|^2.
$$

Without the instrument,

$$
p_{\rm unrec}(r)
=\|E_r^{1/2}U_t\psi_0\|^2.
$$

The hostile mutant inserts a formal resolution of identity into the amplitude
and then squares each component separately. That silently changes
$p_{\rm unrec}$ into $p_{\rm rec}$.

The control must include both:

1. a retained stable outcome, where division is licensed; and
2. a coherent mark/eraser or no-instrument case, where it is not.

---

## 9. Rebuild control G2-C9 — heat kernel normalization

Set

$$
\nu=\frac{\hbar}{2m},
\qquad
H_\tau(x,y)=
(4\pi\nu\tau)^{-d/2}
e^{-|x-y|^2/(4\nu\tau)}.
$$

The Gaussian integral gives

$$
\int d^dx\,H_\tau(x,y)=1.
$$

Completing the square gives

$$
\int d^dz\,H_\tau(x,z)H_\sigma(z,y)
=H_{\tau+\sigma}(x,y).
$$

The variance per coordinate is

$$
\mathbb E[(X_\tau-X_0)^2]=2\nu\tau,
$$

so the stochastic differential convention is

$$
dX_\tau=\sqrt{2\nu}\,dW_\tau.
$$

This matches N1's noise normalization but not its complete dynamics.

---

## 10. Energy-origin control G2-C10

For

$$
H=P^2/(2m)+E_0I,
$$

real time gives the common phase

$$
e^{-iE_0t/\hbar},
$$

which cancels from closed-sector Born probabilities. Euclidean continuation
gives

$$
e^{-E_0\tau/\hbar},
$$

so the kernel integrates to that factor rather than one.

The control rejects both mistakes:

1. calling $E_0$ absolutely observable in every real-time experiment; and
2. silently retaining arbitrary $E_0$ while calling the Euclidean kernel
   Markov-normalized.

A global energy shift may cease to be empirically silent when gravity, mass
superpositions, thermodynamic normalization, or additional sectors enter.
G2 derives none of those extensions.

---

## 11. Boost/continuation control G2-C11

Real Galilei boosts act projectively on wavefunctions. In one standard
convention the multiplier is

$$
\exp\!\left[
\frac{im}{\hbar}
\left(v\cdot x-\frac12v^2t\right)
\right],
$$

combined with the shifted argument $x-vt$. The multiplier has unit modulus.

Under $t=-i\tau$, the continued expression is not simply the law of a
zero-drift Brownian particle viewed in another inertial frame. A real-frame
boost changes Brownian drift, and comparison of path measures requires a
Radon--Nikodym/Girsanov factor.

Therefore the heat kernel retains translation, rotation, and parabolic
composition structure, but it is not licensed as the same projective unitary
Galilei law with the word “time” relabeled.

---

## 12. Potential control G2-C12 — Feynman--Kac is weighted, not automatically Markov

For a scalar potential, the Euclidean representation includes

$$
\exp\!\left[-\frac1\hbar
\int_0^\tau V(X_s)ds\right].
$$

For constant $V_0$ this multiplies the free kernel by

$$
e^{-V_0\tau/\hbar}.
$$

Unless $V_0=0$ or a compensating energy shift is declared, total mass is not
one. A nonconstant potential generally produces killing or weighting rather
than a conservative transition probability.

A ground-state transform

$$
p_\tau^{(\varphi)}(x,y)
=e^{E\tau/\hbar}
\frac{\varphi(x)}{\varphi(y)}K_\tau^V(x,y)
$$

can be Markov when a strictly positive eigenfunction

$$
H\varphi=E\varphi
$$

exists under suitable conditions. But $\varphi$, $E$, the boundary domain,
and the selected stationary sector are added inputs. This construction cannot
be called a free derivation of a universal actuality law.

---

## 13. Euclidean-QFT control G2-C13

Positive Euclidean kernels are not by themselves relativistic quantum field
theories. Reconstruction requires a coherent family of Euclidean correlation
functions and additional axioms, including reflection positivity, symmetry,
regularity, and clustering/appropriate spectral conditions.

The hostile mutant takes one one-particle heat kernel and declares:

$$
\text{positive Euclidean path law}
\Longrightarrow
\text{Lorentzian QFT ontology}.
$$

G2 rejects that implication. Osterwalder--Schrader reconstruction is a
conditional reconstruction theorem, not an ontology selector and not a
derivation of the interacting Euclidean measure.

---

## 14. Nelson control G2-C14

The equality

$$
\nu=\hbar/(2m)
$$

is necessary for the printed free heat kernel and for N1's calibrated
diffusion, but it is not sufficient to derive N1.

Two theories can share that scale while differing in:

1. the parameter called physical time;
2. forward/backward drifts;
3. mean acceleration;
4. force law;
5. phase/current state;
6. global circulation sectors; and
7. measurement/process semantics.

The mutant “heat kernel = Nelson quantum mechanics” therefore fails typing.

---

## 15. Complete hostile-control battery

Any future G2 review must attack at least the following.

1. **Quantum-premise laundering:** infer Hilbert/ray structure from classical
   Galilean relativity.
2. **Central-charge laundering:** call the numerical mass derived because it
   labels a representation.
3. **Action-scale laundering:** call $\hbar$ derived because it appears in the
   cocycle convention.
4. **Dimension laundering:** infer $d$ from a theorem that assumes
   $\mathbb R^d$.
5. **Metric laundering:** call the Euclidean norm emergent.
6. **Clock laundering:** call external $t$ or $\tau$ an operational/internal
   clock.
7. **Kernel oracle:** insert the standard propagator rather than derive it
   from the pinned representation.
8. **Branch fitting:** choose the square-root phase after checking composition.
9. **Kernel-as-probability:** identify $|K|^2$ with a continuum transition
   density.
10. **Delta normalization:** treat $|y\rangle$ as a normalized preparation.
11. **Dimensional silence:** ignore the units of $|K|^2$.
12. **Infinite renormalization:** divide a constant density by an infinite
   volume.
13. **Box rescue:** use a finite box without charging boundary and recurrence
   effects.
14. **Lattice rescue:** use a finite unitary matrix as proof of continuum
   exact-position normalization.
15. **Cell-volume erasure:** omit detector resolution from a discretized law.
16. **Wavepacket substitution:** replace the source by a normalized packet
   while still claiming a point transition.
17. **Phase erasure:** propagate only $|\psi|^2$ and miss the two-packet
   control.
18. **Hidden state:** add phase/current memory without charging it.
19. **Formal-cut division:** square before summing at an unmeasured seam.
20. **Record/eraser conflation:** divide at a coherently erasable mark.
21. **Unistochastic-Markov conflation:** assume
   $|U_{t+s}|^2=|U_t|^2|U_s|^2$.
22. **Wick ontology:** call analytic continuation a physical history map.
23. **Euclidean clock:** treat $\tau$ as a measured duration without a clock
   interface.
24. **Boost silence:** claim unchanged Galilei probability covariance after
   continuation.
25. **Energy-origin silence:** retain $E_0$ but claim Markov normalization.
26. **Feynman--Kac normalization:** call a killed/weighted semigroup
   conservative.
27. **Doob-transform hiding:** insert a positive eigenfunction without ledger
   cost.
28. **Wiener-to-real-time leap:** infer real-time Brownian actuality from a
   Euclidean measure.
29. **OS shorthand:** infer QFT from positivity without reflection positivity
   and the remaining axioms.
30. **Nelson shorthand:** infer time-symmetric mean-Newton dynamics from the
   heat kernel.
31. **Free-to-interacting leap:** infer potentials, entanglement, or a parent
   interaction from the free representation.
32. **One-particle-to-QFT leap:** infer statistics, creation, local algebras,
   or renormalization.
33. **Complex materiality:** treat $i$ as ontic despite the equivalent oriented
   real-plane carrier.
34. **Positive no-go overreach:** claim all ordinary-positive quantum theories
   are impossible.
35. **Barandes refutation:** treat failure of a position Markov kernel as
   failure of an indivisible stochastic law.
36. **Gravity laundering:** replace the fixed metric or action by a gravity
   variable and claim MG0 progress.

---

## 16. Exact decision table

| test | author-side verdict | implication |
|---|---|---|
| projective Galilei algebra | passes at declared scope | free $H$ fixed blockwise |
| Fourier kernel | passes distributionally | coherent carrier fixed |
| coherent convolution | passes | amplitude composition exact |
| $|K|^2$ continuum normalization | fails exactly | not a point transition law |
| Gaussian preparation | passes | ordinary record density exists |
| phase-family future sufficiency | fails for position density | relational phase/current needed |
| finite unistochastic division | fails generically | unrecorded seam indivisible |
| retained record | passes with instrument | stochastic division is physical |
| free heat kernel | passes | Euclidean Markov law exists |
| arbitrary $E_0$ heat normalization | fails unless shifted/renormalized | energy origin charged |
| potential kernel as Markov | conditional/usually false | Feynman--Kac weight not enough |
| Euclidean-to-real actuality | unselected | extra physical principle needed |
| Nelson completion | absent | shared $\nu$ insufficient |
| QFT/gravity | absent | no promotion |

---

## 17. Stop conditions

G2 must stop rather than generate a repair chain if independent review finds:

1. a wrong Galilei commutator or representation quantifier;
2. a false branch, distribution, or convolution statement;
3. a normalized exact-position $|K|^2$ counterexample within the pinned
   continuum carrier;
4. a position-only Markov kernel reproducing the registered relative-phase
   family without hidden state/context;
5. an uncharged physical principle already present in the packet that selects
   Euclidean paths as real-time actuality; or
6. any promotion of the fixed-background control to QFT, spacetime, or gravity.

Semantic repair would require a new authorized successor. Editorial notation
or citation corrections may be made without changing the physics.

