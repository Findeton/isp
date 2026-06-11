# Relativistic ISP V3 Paper 5: Wilson Single-Species QFT Benchmark

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: first theorem-level draft. This paper is Follow-Up A after V3 Paper 4:
the conservative Wilson route whose job is to compare relativistic ISP with a
standard single-species relativistic QFT target.

The paper is intentionally not the no-Wilson/new-physics branch. The
no-Wilson branch keeps the retained detail sector as physical taste data and
should be developed separately. Here the target is narrower:

```text
detail-preserving projective ISP trunk
+ declared Wilson term
+ declared Wilson smearing/CAR representation package
+ declared finite-energy operational instruments
-> tested single-species Dirac/CAR QFT benchmark.
```

## 1. Main Question

Can the Wilson branch of relativistic ISP reproduce the tested local data of a
standard single-species Dirac/CAR QFT, including the interacting curvature
channels developed in V3 Paper 4?

The precise benchmark is:

1. Wilson detail modes are retained in the finite process but decouple from
   finite-energy tests by a declared Wilson gap/Feshbach estimate.
2. The Wilson physical branch has smearing, polarization, propagator, and local
   CAR convergence to the single-species massive Dirac target.
3. The concrete off-diagonal mass-channel interaction has an immediate
   `gDelta^4` stochastic-curvature channel.
4. Compactly supported density-density interactions have a delayed `gDelta^6`
   stochastic-curvature channel.
5. Local operational instruments turn those algebraic channels into tested
   effects/correlations.

This is a benchmark paper, not a Gamma-only reconstruction paper.

## 2. Barandes-Aligned Discipline

The Wilson branch is allowed only if the following are declared.

```text
1. The retained detail/doubler sector exists in the finite process.
2. The Wilson term is an explicit dynamical modification, not an erasure rule.
3. The tested finite-energy instruments cannot excite the detail sector in the
   continuum limit because of a proved gap/Feshbach estimate.
4. CAR, polarization, vacuum, and field instruments are representation data,
   not data secretly recovered from Gamma alone.
5. No unobserved partial stochastic kernels are composed as if the primitive
   whole process were Markov-divisible.
```

Thus the claim is not:

```text
Gamma alone -> QFT.
```

The claim is:

```text
declared enriched Wilson ISP data -> tested single-species QFT benchmark.
```

## 3. Import Contract

From V3 Paper 3 this paper imports:

1. the detail-preserving all-mode projective trunk;
2. the Wilson gap estimate `G_a>=c/a`;
3. Wilson smearing maps `I_a^W`;
4. Wilson one-particle convergence to the massive Dirac target;
5. Wilson polarization convergence;
6. Wilson propagator convergence on finite spacetime test windows;
7. Wilson-admissible interaction stability by Feshbach estimates.

From V3 Paper 4 this paper imports:

1. the primitive coefficient formula
   ```math
   Q(H)_{xy}=|H_{xy}|^2,\qquad x\ne y;
   ```
2. the first interaction derivative
   ```math
   (DQ_H(V))_{xy}=2{\rm Re}(\overline{H_{xy}}V_{xy});
   ```
3. the delayed diagonal coefficient `{\mathcal D}^{(4)}_{H,V}`;
4. the concrete smooth-core off-diagonal mass-channel mixed-curvature limit;
5. the concrete smooth-core delayed density-density `gDelta^6` limit.

This paper must not import:

1. a full interacting Wightman/Haag-Kastler reconstruction theorem;
2. nonperturbative renormalization;
3. a Gamma-only derivation of the CAR algebra;
4. no-Wilson taste removal;
5. Lorentz covariance beyond the finite spacetime test windows already proved.

## 4. Wilson Benchmark Data

Let the continuum one-particle target be

```math
{\mathcal H}_D=L^2({\mathbb R};{\mathbb C}^s),
\qquad
h_D(k)=\alpha k+m\beta,
```

with `m>0`, `\alpha^2=\beta^2=1`, and
`\alpha\beta+\beta\alpha=0`.

Let the Wilson lattice one-particle symbol be

```math
h_a^W(k)
=
\alpha\frac{\sin(ak)}a
+
\beta\left(m+\frac r a(1-\cos(ak))\right),
\qquad r>0.
```

Let `I_a^W` be the declared Wilson smearing map from Paper 3, with band
cutoff `\Lambda(a)` satisfying

```math
\Lambda(a)\to\infty,
\qquad
a\Lambda(a)\to0.
```

Let `{\mathcal F}_{a,W}^{\le N,E,O}` denote the tested finite-particle,
finite-energy, local Wilson sector over a bounded spacetime window `O`. Let
`P_a` be the physical Wilson projector and `Q_a=1-P_a` the detail/doubler
projector.

## 5. Theorem: Wilson Single-Species Tested-QFT Benchmark

Assume:

1. Wilson smearing, polarization, and propagator convergence from Paper 3;
2. the Wilson detail gap and Feshbach estimate;
3. Wilson-admissible interactions on the tested sector;
4. the Paper 4 smooth-core interacting curvature estimates;
5. compatible finite operational instruments for the local CAR polynomials
   tested below.

Then for every finite family of compactly supported test spinors
`f_1,\ldots,f_n`, every finite local CAR polynomial `A`, and every fixed
finite spacetime test window,

```math
\omega_{a,W}^{\rm ISP}(A_a(I_a^Wf_1,\ldots,I_a^Wf_n))
\to
\omega_D(A(f_1,\ldots,f_n)),
```

where `\omega_D` is the single-species Dirac quasi-free target state, corrected
perturbatively by the declared Wilson-admissible interaction when the
interaction is turned on.

Moreover the interacting exchange-defect coefficients converge on the tested
domain:

```math
{\mathfrak C}_{a,W}[N,M;g]
\to
K_{\parallel,W}[N\partial_xM-M\partial_xN]
+
g{\mathfrak C}_{W}^{(1)}[N,M]
+
g^2{\mathfrak C}_{W}^{(2)}[N,M]
```

for off-diagonal interactions satisfying ICURV-2, while compactly supported
diagonal density-density interactions contribute first through the delayed
coefficient

```math
g\,{\mathfrak C}_{W}^{(dd,del)}[N,M]
```

at exchange order `gDelta^6`.

### Proof

The local CAR polynomial convergence is the Wilson Fock/local-net convergence
from Paper 3. Detail/doubler fields do not contribute because the finite-energy
spectral projection is contained in the physical block for sufficiently small
`a`, and interaction-induced physical/detail mixing is suppressed by the
Feshbach estimate.

The curvature statement is V3 Paper 4 restricted to the Wilson branch. For
off-diagonal interactions, the first coefficient is `DQ_H(V)`, so the mixed
curvature appears in the `Delta^4` exchange-defect coefficient. For diagonal
density-density interactions, `DQ_H(V)=0`; the first coefficient is the
delayed `{\mathcal D}^{(4)}_{H,V}`, so the exchange contribution appears at
`gDelta^6`. The smooth-core estimates from Paper 4 give the strong tested
limits. `square`

## 6. Graph-Domain Upgrade Of The Smooth-Core Limits

Paper 4 proves the two concrete interacting curvature limits on the declared
smooth core. For a standard-QFT benchmark, the next useful strengthening is a
graph-domain estimate with explicit domain and convergence type.

Let `H_{a,W}^{\rm phys}=P_aH_{a,W}P_a` be the physical Wilson generator on a
fixed finite-particle sector and fixed compact local/spacetime window. For an
integer `s>=0`, define the tested Wilson graph norm

```math
\|\Psi\|_{W,s,a}
=
\sum_{j=0}^{s}\|(1+|H_{a,W}^{\rm phys}|)^j\Psi\|.
```

Let `{\mathcal D}_{W,s}` be the continuum graph domain of the corresponding
single-species Dirac/Fock generator, and let `I_a^W{\mathcal D}_{W,s}` denote
the declared Wilson lattice approximation of that domain. Convergence below
means:

```math
\|T_a I_a^W\Psi-I_a^WT\Psi\|_{W,t,a}\to0
```

for every fixed `\Psi\in{\mathcal D}_{W,s}`.

### Theorem 6.1: Tested Graph-Domain Stability

Fix `s>=4`, compactly supported smooth lapses `N,M`, a fixed finite-particle
number, and a fixed local/spacetime test window. The Wilson coefficient
families

```math
{\mathcal B}_{a,W}^{\mu}[N],
\qquad
{\mathcal B}_{a,W}^{(4),dd}[N],
\qquad
{\mathcal B}_{a,W}^{A}[N]
```

satisfy uniform graph bounds, for all sufficiently small `a`,

```math
\|{\mathcal B}_{a,W}^{\mu}[N]\Psi_a\|_{W,s,a}
\le
C_N\|\Psi_a\|_{W,s,a},
```

```math
\|{\mathcal B}_{a,W}^{A}[N]\Psi_a\|_{W,s,a}
\le
C_{N,A}\|\Psi_a\|_{W,s,a},
```

and

```math
\|{\mathcal B}_{a,W}^{(4),dd}[N]\Psi_a\|_{W,s-3,a}
\le
C_{N,dd}\|\Psi_a\|_{W,s,a}.
```

They converge strongly in these graph topologies to their continuum Wilson
targets. Consequently the off-diagonal mass-channel, Peierls-current, and
delayed density-density mixed-curvature coefficients converge as quadratic
forms on `{\mathcal D}_{W,s}`:

```math
\langle I_a^W\Phi,
{\mathfrak C}_{a,W}^{X}[N,M]I_a^W\Psi\rangle
\to
\langle \Phi,
{\mathfrak C}_{W,\rm cont}^{X}[N,M]\Psi\rangle,
\qquad
X\in\{\mu,A,dd\}.
```

For `X=dd`, this is the delayed exchange coefficient at order `gDelta^6`.
For `X=\mu,A`, it is the immediate mixed coefficient at order `gDelta^4`.

### Proof

The mass-channel coefficient is a bounded local multiplication stencil, so it
is graph-bounded of order zero. The Peierls-current coefficient is also
bounded on the Wilson physical band by Theorem 7.1 below; its commutators with
powers of `H_{a,W}^{\rm phys}` are finite sums of local stencils with smooth
compact coefficients, so it is graph-bounded on every fixed graph order.

The delayed density-density coefficient is a finite sum of terms containing
at most three free local Wilson stencils and one bounded compactly supported
density interaction. Hence it is graph-bounded of order three. The Wilson
symbol estimates from Paper 3 give strong convergence of `H_a^j` to `H_D^j`
for `j<=3` on the declared Wilson graph core, and the compact support of the
lapses prevents volume growth. Density of the smooth core in
`{\mathcal D}_{W,s}` and the uniform graph bounds extend the convergence to
the graph closure. The quadratic-form convergence follows by applying these
operator convergences to each term in the mixed commutator and adding and
subtracting the continuum target. `square`

## 7. Wilson Current/Hopping Interaction With `1/a` Hopping Scale

The physically important off-diagonal perturbation is not merely an onsite
mass-channel modulation. It is the current/hopping perturbation. Naively this
looks dangerous because the Wilson hopping term scales like `1/a`.

The correct Wilson perturbation is introduced by a Peierls link phase. Put
links at midpoints and write

```math
U_{n+1/2}(\lambda)=\exp(i\lambda a A_{n+1/2}),
\qquad
A_{n+1/2}=A(a(n+1/2)),
```

with `A\in C_c^\infty({\mathbb R};{\mathbb R})`. The gauged Wilson operator is

```math
\begin{aligned}
(h_{a,A}^Wu)_n
&=
-\frac{i\alpha}{2a}
\left(
U_{n+1/2}u_{n+1}
-
U_{n-1/2}^{*}u_{n-1}
\right)
+m\beta u_n
\\
&\quad
+\frac{r\beta}{2a}
\left(
2u_n
-
U_{n+1/2}u_{n+1}
-
U_{n-1/2}^{*}u_{n-1}
\right).
\end{aligned}
```

The first variation

```math
v_a^A=\left.\frac d{d\lambda}h_{a,A}^W\right|_{\lambda=0}
```

is

```math
\begin{aligned}
(v_a^Au)_n
&=
\frac{\alpha}{2}
\left(
A_{n+1/2}u_{n+1}
+
A_{n-1/2}u_{n-1}
\right)
\\
&\quad
+\frac{ir\beta}{2}
\left(
-A_{n+1/2}u_{n+1}
+
A_{n-1/2}u_{n-1}
\right).
\end{aligned}
```

The factor `a` in the link phase cancels the `1/a` hopping scale.

### Theorem 7.1: Peierls Current Perturbation Is Wilson-Admissible

On the Wilson physical branch,

```math
v_a^AI_a^Wf
\to
I_a^W(A(x)\alpha f)
```

for every Schwartz spinor `f`. More quantitatively,

```math
\|v_a^AI_a^Wf-I_a^W(A\alpha f)\|_a
\le
C_{A,f}\left(a\Lambda(a)+\Lambda(a)^{-q}\right)
```

for every `q`, after increasing `C_{A,f,q}` if needed. The Wilson-term
variation is `O(a\Lambda(a))` on the physical band and therefore vanishes.

On fixed finite-particle finite-energy sectors,

```math
V_a^A=d\Gamma(v_a^A)
```

is Wilson-admissible. Its off-block correction is suppressed by the Wilson
gap, and its physical block converges to the continuum current coupling

```math
V_{\rm cont}^A
=
\int A(x)\psi^\dagger(x)\alpha\psi(x)\,dx.
```

### Proof

For constant `A`, the first variation of the symbol is

```math
\partial_kh_a^W(k)A
=
\left(\alpha\cos(ak)+r\beta\sin(ak)\right)A.
```

For smooth compactly supported `A(x)`, the same expression holds
pseudodifferentially on the Wilson physical band up to the usual commutator
errors controlled by derivatives of `A`. On the band `|k|<=\Lambda(a)`,

```math
\cos(ak)=1+O(a^2\Lambda(a)^2),
\qquad
\sin(ak)=O(a\Lambda(a)).
```

Thus

```math
\partial_kh_a^W(k)A
=
A\alpha+O(a\Lambda(a)).
```

The discarded high-momentum part gives the Schwartz tail
`O(\Lambda(a)^{-q})`. Since `a\Lambda(a)\to0`, the physical block converges to
the continuum current coupling. The variation is uniformly bounded on the
physical band, and the Wilson gap/Feshbach estimate controls physical/detail
mixing exactly as in Paper 3. `square`

### Corollary 7.2: Current-Coupling Mixed Curvature Limit

Let

```math
B_{n,W}^{A}
=
DQ_{H_{n,W}^{(0)}}(V_{n,W}^{A})
-
DQ_{H_{0,W}^{(0)}}(V_{0,W}^{A}).
```

Then for compactly supported smooth lapses `N,M`, the mixed expression

```math
[{\mathcal K}_{a,W}^{(0)}[N],{\mathcal B}_{a,W}^{A}[M]]
+
[{\mathcal B}_{a,W}^{A}[N],{\mathcal K}_{a,W}^{(0)}[M]]
```

has a strong tested graph-domain limit. The limit is the Wilson single-species
continuum current-coupling mixed curvature.

### Proof

The Peierls variation is off-diagonal in the declared configuration basis and
has the physical continuum limit proved in Theorem 7.1. Lemma 5.2 of Paper 4
therefore gives the coefficient `DQ_H(V)`. The graph-domain argument of
Theorem 6.1 applies, with the Peierls perturbation bounded on the physical
band and Wilson-suppressed off the physical band. `square`

## 8. Concrete Operational Local Instruments

Raw maps

```math
J_R,\qquad J_R^{-1},\qquad E_{R,S}
```

are algebraic relative-dynamics maps. They are not automatically observables.
To compare with standard QFT, this paper declares local operational
instruments.

For a bounded spatial region `O`, let `{\mathfrak A}_a^W(O)` be the Wilson
local CAR algebra generated by smeared lattice fields `\psi_a(I_a^Wf)` with
`{\rm supp}(f)\subset O`. Let

```math
{\mathfrak E}_a^W(O)
=
\{E\in{\mathfrak A}_a^W(O):0\le E\le I\}
```

be its finite effect system.

### 8.1 Density Instruments

For `f\in C_c^\infty(O)` with `0\le f\le1`, define the bounded finite-particle
local number observable

```math
N_a(f)=a\sum_n f(an)\rho_n.
```

For a finite Borel partition `{I_\ell}` of `[0,N_{\rm max}]`, define effects

```math
E_{a,\ell}^{\rho}=\chi_{I_\ell}(N_a(f)).
```

The corresponding instrument is the Lüders instrument

```math
{\mathcal I}_{a,\ell}^{\rho}(X)
=
E_{a,\ell}^{\rho\,1/2}XE_{a,\ell}^{\rho\,1/2}.
```

### 8.2 Current Instruments

For a compactly supported test field `A`, let `J_a(A)=d\Gamma(v_a^A)` be the
Wilson current observable from Section 7. On the finite-particle tested sector
it is bounded. A finite-resolution current instrument is defined by effects

```math
E_{a,\ell}^{J}=\chi_{I_\ell}(J_a(A)).
```

### 8.3 Exchange-Defect Instruments

Let

```math
E_{a}^{N,M}(\Delta)
=
J_N(\Delta)J_M(\Delta)J_N(\Delta)^{-1}J_M(\Delta)^{-1}
```

be the declared exchange-defect map on the tested Wilson sector. Let

```math
X_a^{N,M}(\Delta)
=
\frac{1}{2i\Delta^4}
\left(E_a^{N,M}(\Delta)-E_a^{N,M}(\Delta)^{*}\right)
```

for off-diagonal `gDelta^4` tests, and replace `\Delta^4` by `\Delta^6` for
the delayed density-density test after subtracting the free term. For
`\epsilon>0` small enough that `\| \epsilon X_a^{N,M}\|\le1`, define the
two-outcome weak effects

```math
E_{a,\pm}^{\rm ex}
=
\frac12(I\pm\epsilon X_a^{N,M}).
```

These are operational probes of the exchange-defect coefficient, not claims
that the raw algebraic map is itself an effect.

### 8.4 Detector-Record Instruments

A finite detector is represented by an explicit pointer factor
`{\mathcal H}_{D,a}` with orthogonal record projectors `{P_r}`. A detector
coupling over region `O` is a declared finite unitary or stochastic quantum
instrument on

```math
{\mathcal F}_{a,W}^{\le N,E,O}\otimes{\mathcal H}_{D,a}.
```

The record effects are

```math
E_{a,r}^{D}=U_a^{*}(I\otimes P_r)U_a.
```

The record space is not erased. Conditioning on a record is an operational
choice, and the reject/unobserved records remain part of the declared process.

### Theorem 8.1: Concrete Wilson Instrument Convergence

For every finite family of density, current, exchange-defect, and detector
instruments of the types above, with compactly supported smooth test data and
fixed finite outcome partitions, the Wilson finite-cutoff outcome
probabilities converge to the corresponding single-species Dirac/CAR outcome
probabilities:

```math
\omega_{a,W}^{\rm ISP}(E_{a,\ell})
\to
\omega_D(E_\ell).
```

If two spacetime-supported instruments are spacelike separated in the
continuum target, then their Wilson commutator expectation tends to zero on
the tested spacetime window.

### Proof

Density and current observables converge by the Wilson smearing and Peierls
current estimates. Their finite spectral partitions converge by functional
calculus on the fixed finite-particle tested sector. Exchange-defect
instruments converge by the coefficient convergence in Theorems 6.1 and 7.2
and by the delayed density-density estimate from Paper 4. Detector records
converge by the assumed compatible detector coupling and the local CAR
polynomial convergence. Spacelike commutator convergence is inherited from
the Wilson propagator convergence to the continuum Dirac causal propagator.
`square`

## 9. Benchmark Equivalence Theorem

Define a Wilson benchmark test battery `{\mathcal T}` to be a finite list of:

1. compactly supported CAR polynomial expectations;
2. density instrument outcome probabilities;
3. current instrument outcome probabilities;
4. exchange-defect weak-probe outcome probabilities;
5. detector-record probabilities;
6. spacelike commutator tests over a fixed spacetime window.

Each item in `{\mathcal T}` has a finite-cutoff Wilson ISP prediction
`P_{a,W}^{\rm ISP}(T)` and a single-species Dirac/CAR QFT prediction
`P_D^{\rm QFT}(T)` computed from the declared continuum target.

### Theorem 9.1: Wilson Benchmark Equivalence On Finite Test Batteries

Under the hypotheses of this paper, for every finite Wilson benchmark test
battery `{\mathcal T}`,

```math
\sup_{T\in{\mathcal T}}
\left|
P_{a,W}^{\rm ISP}(T)-P_D^{\rm QFT}(T)
\right|
\to0.
```

If the test battery includes the off-diagonal current/mass-channel exchange
probe, the convergence includes the immediate `gDelta^4` mixed-curvature
coefficient. If it includes compactly supported density-density exchange
probes, the convergence includes the delayed `gDelta^6` coefficient.

### Proof

The test battery is finite. CAR polynomial convergence follows from Paper 3.
Density, current, exchange-defect, and detector-record convergence follows
from Theorem 8.1. Taking the maximum over finitely many tests preserves
convergence. `square`

## 10. What Matches Standard QFT

On the declared Wilson benchmark, the following standard-QFT structures are
matched on tested finite families:

1. single-species one-particle massive Dirac dynamics;
2. CAR pairings for compactly supported smooth test spinors;
3. quasi-free vacuum finite-polynomial expectations;
4. equal-time local CAR net on a Cauchy surface;
5. finite spacetime-window propagator and microcausality tests;
6. Wilson-admissible local interactions on tested sectors;
7. off-diagonal current/mass-channel stochastic curvature;
8. delayed density-density stochastic curvature;
9. concrete density, current, exchange-defect, and detector-record statistics.

This is enough to call Paper 5 a positive Wilson benchmark against standard
relativistic QFT.

## 11. What Is Imported, Not Reconstructed

The following data are still imported as declared enrichment:

1. the Wilson smearing maps `I_a^W`;
2. the CAR/Fock representation functor;
3. the polarization/vacuum choice;
4. the Dirac gamma/Clifford structure;
5. the local operational instruments;
6. the Wilson term itself;
7. the finite-energy test class;
8. the decision to compare to the single-species Wilson physical branch.

This imported-data ledger is not a weakness of the paper. It is the
Barandes-aligned boundary: do not claim that endpoint stochastic kernels alone
carry information they do not carry.

## 12. Appendix: Why This Is Not Gamma-Only QFT Reconstruction

The Wilson benchmark is deliberately enriched. A full Gamma-only
reconstruction of interacting QFT would require the endpoint stochastic
kernels alone to determine the complex field algebra, polarization, local
observables, and instruments. They do not.

### Proposition 12.1: Phase-Orientation Ambiguity Of Gamma

Let `U(\Delta)` be a finite whole-process unitary in the declared
configuration basis and define

```math
\Gamma_{xy}(\Delta)=|U_{xy}(\Delta)|^2.
```

Then the conjugate process

```math
\widetilde U(\Delta)=\overline{U(\Delta)}
```

has the same `Gamma` for every `\Delta`, but reverses the complex orientation
of all commutator phases. Therefore `Gamma` alone cannot determine the
oriented complex Hilbert/CAR package.

### Proof

Entrywise absolute squares are unchanged by complex conjugation:

```math
|\widetilde U_{xy}(\Delta)|^2
=
|\overline{U_{xy}(\Delta)}|^2
=
|U_{xy}(\Delta)|^2.
```

But replacing `U` by `\overline U` sends `i` to `-i` in the representation
of oriented commutators and phase-sensitive field data. Hence any rule that
uses only `Gamma` must either identify the two complex orientations or import
extra orientation data. `square`

### Proposition 12.2: Instrument Underdetermination

The same finite stochastic kernel can be paired with inequivalent operational
effect systems unless the instruments are declared. Consequently local
observables are not determined by `Gamma` alone.

### Proof

`Gamma` assigns probabilities to transitions between the declared
configuration records. It does not specify which coarse-grainings, pointer
records, local CAR polynomials, current probes, or exchange-defect weak probes
are operationally available. Different declared effect systems can act on the
same transition kernel and ask different questions of it. Therefore the
instrument layer is additional structure. `square`

### Gamma-Only Boundary

This paper proves:

```text
Gamma + Wilson enrichment + instruments -> tested single-species QFT benchmark.
```

It does not prove:

```text
Gamma alone -> full interacting QFT.
```

That stronger statement would contradict the phase-orientation and instrument
underdetermination above unless additional data were silently smuggled into
the word `Gamma`.

## 13. What Remains Open After Paper 5

1. Upgrade tested graph-domain convergence to a more robust interacting
   continuum domain theorem.
2. Treat nonperturbative interacting QFT rather than finite perturbative
   benchmark channels.
3. Prove full Lorentz/foliation covariance for the interacting Wilson branch.
4. Extend from external current/background couplings to dynamical gauge fields.
5. Compare the Wilson benchmark with the no-Wilson detail-preserving
   multi-taste branch in a separate paper.
6. Identify operational experiments where Wilson ISP and standard QFT are
   empirically equivalent or diverge only through explicitly declared
   non-Wilson sectors.

## 14. Status

Paper 5 now has a positive theorem-level path:

```text
Paper 3 Wilson representation package
+ Paper 4 interacting curvature coefficients
+ Paper 5 tested graph-domain/instrument/benchmark-equivalence upgrade
-> Wilson single-species QFT benchmark.
```

The strongest honest conclusion is:

> Relativistic ISP, with the declared Wilson enrichment package, reproduces a
> tested single-species relativistic QFT benchmark and supports controlled
> interacting stochastic-curvature channels.

The strongest honest non-conclusion is:

> This does not prove Gamma-only reconstruction of full interacting
> relativistic QFT.
