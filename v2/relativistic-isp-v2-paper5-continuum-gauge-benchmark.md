# Toward a Continuum Gauge Benchmark for Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V2 Paper 5 initial draft

Date: 2026-05-14

Updated: 2026-05-15

Status: theorem-structured draft with explicit open inputs. This paper gives
the first open-chain compact `U(1)` gauge benchmark package for relativistic
ISP: finite Gauss-sector kernels, center-resolved cutoff control,
center/cutoff/Gauss detector records, a concrete local continuum statistic, a
renormalized contact exchange law, and compact-rotor local-statistic transfer
under stated tightness hypotheses. It also proves a two-state obstruction to
unconditional full Hamiltonian slab inverse control. It does not claim
non-Abelian gauge theory, a continuum Haag-Kastler net, QFT reconstruction, or
growing-volume compact-rotor inverse control.

## Abstract

V2 Papers 1-4 establish a finite-to-projective relativistic ISP stack:
stochastic hypersurface kernels, projective compatibility, interacting
comparison-map locality under explicit inverse-control hypotheses, and
operational detector instruments. The next non-gravitational viability test is
gauge theory. Gauge fields stress the framework in exactly the right way: local
constraints create boundary-center sectors, finite link truncations can fail
under volume growth, and matter-only locality is not the correct operational
baseline.

This paper constructs a conservative `1+1D` compact `U(1)` gauge-matter
benchmark on open finite intervals, with electric-flux cutoff `K`, lattice
spacing `a`, and volume `L`. The finite regulated configuration spaces are
exact stochastic objects. The open-chain Gauss law resolves link fluxes from
matter plus a boundary flux center, forcing local statistics and detector
records to be center-resolved.

The main positive result is Main Theorem M. Under bounded charge alphabet,
tight local centers, local finite electric energy, explicit cutoff scaling,
Paper-4-compatible detector records, and an assumed compact-rotor local
thermodynamic limit, finite-cutoff ISP local gauge statistics converge to the
same local limit. A clipped local electric-energy statistic is computed
explicitly on deterministic electric profiles and finite mixtures. The
sufficient cutoff scaling is conservative under only second-moment energy
control, `a(K-r)^2 -> infinity`, and improves to `a(K-r-B)^3 -> infinity` when
Gauss-law slope and tight local centers are used.

The exchange side is also made concrete. The first two-bond center-resolved
exchange coefficient is `1/(16a^4)`. Under microscopic scaling
`\Delta=\kappa a`, contact mixed corridors have a finite renormalized exchange
channel, while positive physical separation gives exponentially vanishing
exchange. The main obstruction is equally explicit: the full Hamiltonian
Born-squared slab has a two-state resonance that prevents unconditional uniform
inverse control across arbitrary refinements. Thus Paper 5 earns an open-chain
local gauge benchmark package, not a full continuum gauge QFT.

## 1. Scope And Non-Claims

Established in this initial draft:

1. the conservative Paper 5 target is fixed: `1+1D` compact Abelian
   gauge-matter dynamics, not full QFT and not non-Abelian gauge theory;
2. the first theorem package is fixed to an open chain rather than a periodic
   ring;
3. finite electric-flux truncated configuration spaces are defined;
4. Gauss-law sectors and boundary flux centers are explicit;
5. an explicit Schwinger-like finite Hamiltonian/lift is fixed;
6. exact finite Gauss-sector preservation is stated and proved at the kernel
   level;
7. the open-chain Gauss reduction is stated, including the center dependence;
8. a no-truncation window theorem identifies when finite `K` agrees with the
   compact-rotor sector for a declared local operation;
9. a finite-energy cutoff-tail estimate is stated for local cylinder states;
10. a center-resolved locality theorem separates fixed-center statistics from
   unresolved center mixtures;
11. the first center-resolved exchange coefficient target is computed on a
   minimal two-bond strip;
12. an admissible local cutoff scaling regime `K(a,L)` is stated and tied to
   finite-energy cutoff tails;
13. a first concrete continuum-facing local electric-energy statistic is
   formulated with a cutoff-stability bound and a proved continuum limit on
   deterministic center-profile preparations;
14. a concrete center/cutoff/Gauss detector record family and deterministic
   readout protocol are specified;
15. a restricted finite-depth inverse-control theorem and a full-slab warning
   are stated;
16. the two-bond exchange coefficient is extended to a corridor-onset, tail,
   and renormalized contact law;
17. fixed-volume and growing-volume `K -> infinity` compact-rotor stability
   transfer theorems are proved for local statistics under finite
   electric-energy/tight-center hypotheses;
18. a claim audit, dependency graph, and central theorem package make the
   theorem status explicit;
19. a projective/cutoff residual ledger is stated for continuum-facing gauge
   statistics;
20. the operational interface from Paper 4 is imported without identifying raw
   gauge comparison maps with observables.

Not established here:

1. a growing-volume compact-rotor inverse-control theorem;
2. cutoff-uniform inverse control for all gauge sectors;
3. a volume-uniform interacting exchange-defect theorem;
4. non-Abelian gauge theory;
5. a continuum Haag-Kastler net;
6. QFT reconstruction from gauge-sector stochastic kernels;
7. gravity or dynamical spacetime.

The central discipline is:

```text
finite gauge kernel
-> Gauss-sector block
-> center-resolved projective family
-> calibrated detector instrument
-> continuum-facing local statistic.
```

Skipping any arrow is an overclaim.

### Result Classification

Unconditional finite and model-limit facts in this draft:

1. Theorem 1: gauge-compatible finite kernels preserve Gauss sectors.
2. Definition 1A and Theorem 1B: the concrete open-chain finite
   Hamiltonian/lift is gauge-compatible and center preserving.
3. Proposition 2: open-chain Gauss law resolves link flux from matter plus a
   boundary center.
4. Theorem 3 and Corollary 3A: finite cutoff agrees with the rotor sector on a
   no-truncation window.
5. Lemma 3B: finite electric energy bounds cutoff-boundary mass.
6. Proposition 4 and Theorem 4A: center-resolved operational statistics are
   convex mixtures over boundary sectors, so unresolved centers cannot be
   treated as a single local sector.
7. Proposition 6A: the minimal open-chain two-bond strip has a nonzero
   center-resolved exchange coefficient `1/(16a^4)` whenever the two required
   gauge hops are admissible.
8. Definition 5A and Theorem 5B: locally admissible cutoff scaling is sufficient
   for uniform local cutoff stability.
9. Theorem 5G and Corollary 5H: Gauss law and tight local centers improve the
   sufficient cutoff scaling from `K>>a^{-1/2}` to `K>>a^{-1/3}`, while bounded
   profile classes need only eventual cutoff dominance.
10. Example 5C: the clipped local electric-energy statistic is a concrete
   continuum-facing gauge statistic.
11. Definition 5D, Theorem 5E, and Corollary 5F: this statistic has a proved
   continuum limit on admissible deterministic electric profiles and finite
   center-profile mixtures.
12. Definition 4B, Theorem 4C, Protocol 4D, and Theorem 4E: detector records
   can include local center, cutoff, and Gauss flags in a concrete Paper
   4-compatible readout instrument.
13. Proposition 6B: finite-depth comparison maps have uniform inverse control
   under an explicit Neumann smallness condition.
14. Theorem 6D: the full Hamiltonian Born-squared slab has an unavoidable
   two-state resonance obstruction to unconditional uniform inverse control.
15. Theorem 6C and Theorem 6F: separated mixed regions have corridor-supported
   exchange onset, an exponential corridor-tail bound, and a renormalized
   contact-channel continuum law.
16. Theorem 7, Definition 7A, and Theorem 7B: fixed-volume and growing-volume
   compact-rotor local statistics are stable under finite-energy/tight-center
   hypotheses, assuming the rotor growing-volume local limit exists.
17. Main Theorem M: the open-chain local gauge benchmark package transfers
   local operational statistics and renormalized contact exchange under the
   stated tightness, cutoff, detector, rotor-limit, and inverse-control
   hypotheses.

Conditional continuum-facing statements:

1. Theorem 5: local cylinder statistics are projectively stable if cutoff,
   volume, kernel, record, and center residuals vanish.
2. Theorem 6: gauge operational exchange transfers from Paper 3 only if
   center-resolved gauge-compatible comparison maps satisfy uniform anchored
   inverse control.

### Claim Audit

| Result | Status | What Is Earned | Main Hypotheses Or Open Inputs |
|---|---|---|---|
| Theorem 1 | proved finite | Born-squared kernels preserve Gauss blocks when the lift is block diagonal | finite declared lift; invertibility only on tested block |
| Definition 1A / Theorem 1B | proved finite | concrete open-chain Hamiltonian preserves Gauss law and boundary centers | open chain; finite `K`; interior hopping convention |
| Proposition 2 | proved finite | open-chain Gauss law reduces link flux to matter plus boundary center | interval geometry |
| Theorem 3 / Corollary 3A | proved finite | finite cutoff agrees with rotor on no-truncation supports and reachable hulls | cutoff margin exceeds operation or reachable radius |
| Lemma 3B | proved finite estimate | local electric energy bounds cutoff-boundary mass | second moment only; conservative |
| Corollary 3C | obstruction | full open-chain space needs `K` growth with volume without restrictions | unrestricted centers and charge sectors |
| Definition 5A / Theorem 5B | proved model-limit estimate | `a(K-r_*)^2 -> infinity` gives local cutoff stability | black-box finite local energy |
| Theorem 5G / Corollary 5H | proved model-limit estimate | tight center plus Gauss slope improves sufficient scaling to `a(K-r_*-B)^3 -> infinity` | bounded charge alphabet and center tightness |
| Example 5C | constructed statistic | clipped local electric energy is a bounded center-resolved gauge statistic | operational reading of local link flux |
| Definition 5D / Theorem 5E / Corollary 5F | proved model-limit | Example 5C converges for deterministic profiles and finite profile mixtures | admissible step profiles; bounded profile cutoff dominance |
| Proposition 4 / Theorem 4A | proved finite | unresolved centers give mixtures; locality is center-resolved | instruments preserve center sectors |
| Definition 4B / Theorem 4C | conditional detector transfer | center/cutoff/Gauss records satisfy Paper 4 naturality with explicit residuals | record naturality and residual bounds |
| Protocol 4D / Theorem 4E | proved protocol transfer | deterministic readout plus confusion channel gives explicit detector residual | collar variables preserved on good block; confusion channels compared |
| Theorem 5 | conditional transfer | local operational statistics are projectively stable when all residuals vanish | projective compatibility; detector naturality; cutoff, center, Gauss residuals |
| Theorem 6 | conditional transfer | raw gauge exchange transfers to operational exchange after calibration | inverse control and detector realization |
| Proposition 6B | proved finite-depth theorem | finite-depth comparison maps have Neumann inverse control | `\|G_j-I\|_\nu<1`; bounded depth |
| Theorem 6D / Corollary 6E | obstruction plus alternatives | unconditional full Hamiltonian slab inverse control fails across arbitrary refinements | two-state resonance; replacement topology or resonance avoidance needed |
| Proposition 6A | proved finite coefficient | first two-bond exchange coefficient is `1/(16a^4)` when admissible | no-truncation two-bond strip |
| Theorem 6C | proved finite-slab estimate | exchange onset and corridor tail are controlled in small-slab expansion | `q_*\theta<1`; small-slab expansion |
| Theorem 6F | proved model-limit law | `Delta=\kappa a` gives finite contact exchange and vanishing positive-separation exchange | `q_*\kappa^2/4<1`; contact strip projection |
| Theorem 7 | proved fixed-volume transfer | compact-rotor local statistics are stable as `K -> infinity` at fixed volume | finite local energy or finite support |
| Definition 7A / Theorem 7B | conditional growing-volume transfer | finite cutoff inherits a growing-volume rotor local limit | rotor local thermodynamic limit is an input |

### Dependency Graph

The logical spine is:

```text
finite open-chain gauge kinematics
-> Gauss-sector and center decomposition
-> cutoff/no-truncation control
-> center-resolved detector records
-> projective local operational statistics
-> compact-rotor/local-continuum transfer.
```

The main dependencies are:

1. **Gauge kinematics:** Theorem 1B and Proposition 2 feed every later result.
   Without the open-chain center recursion, cutoff tails and local detector
   records are not well-defined.
2. **Cutoff control:** Lemma 3B gives the black-box second-moment bound.
   Theorem 5G improves it only after adding bounded charges and tight local
   centers.
3. **Concrete statistic:** Example 5C depends on cutoff control. Theorem 5E
   removes the abstract rotor-limit input only for deterministic profile
   preparations and finite mixtures.
4. **Operational detector layer:** Definition 4B, Protocol 4D, and Theorem 4E
   depend on the center decomposition and on explicit cutoff/Gauss flags.
   Theorem 5 then imports Paper 4 naturality.
5. **Exchange layer:** Proposition 6A gives the first finite coefficient.
   Theorem 6C gives the corridor tail. Theorem 6F gives the renormalized
   contact law only in the microscopic small-step scaling
   `\Delta=\kappa a`.
6. **Inverse-control risk:** Proposition 6B proves finite-depth inverse control.
   Theorem 6D rules out unconditional full Hamiltonian slab inverse control
   across arbitrary refinements.
7. **Compact-rotor transfer:** Theorem 7 is fixed-volume. Theorem 7B is
   growing-volume only after assuming the compact-rotor local thermodynamic
   limit exists.

The remaining external inputs are therefore exactly:

1. a physically motivated compact-rotor local thermodynamic limit;
2. a replacement for full-slab inverse control, such as resonance avoidance,
   observable-subspace inverse control, or a renormalized inverse topology;
3. a physical detector model that realizes the abstract confusion channel;
4. a continuum interpretation of the renormalized contact exchange channel.

### Main Theorem M: open-chain local gauge benchmark package

Fix the open-chain compact `U(1)` gauge-matter benchmark of Definition 1A on a
directed refinement net `\alpha=(a,L,K)`. Let `I` be a compact physical
interval and let all tested preparations be physical Gauss-sector preparations
with:

1. bounded local charge alphabet `Q_*<\infty`;
2. tight local incoming center `c_A`;
3. uniformly bounded local electric energy on the mixed collar of `I`;
4. cutoff scaling satisfying, after choosing `B` with small center tail,

```math
a(K(a,L)-r_*-B)^3\longrightarrow\infty;
```

5. detector records implemented by Protocol 4D with classical confusion
   residual `\epsilon_R -> 0`;
6. Gauss leakage and center mismatch residuals tending to zero;
7. a compact-rotor growing-volume local limit for the tested rotor statistic.

Then every bounded center-resolved local statistic built from the protocol has
the same continuum limit in the finite-cutoff ISP benchmark as in the
compact-rotor local limit:

```math
\lim_{a\to0}\lim_{L\to\infty}
e_a^T\mathsf I_{A,\alpha}^{K(a,L)}p_{\alpha,K(a,L)}
=
\lim_{a\to0}S_I^{a,\mathrm{rot},\infty},
```

provided the limit on the right exists.

Moreover, for the clipped local electric-energy statistic of Example 5C, the
right-hand side is explicitly computed on deterministic admissible electric
profiles:

```math
\min\left\{
1,
\frac{1}{M}\frac{g^2}{2}\int_I e(x)^2\,dx
\right\},
```

and extends by linearity to finite mixtures of such profiles.

For operational exchange, if the primitive comparison dynamics is taken in a
finite-depth inverse-controlled class and the microscopic slab scales as
`\Delta=\kappa a` with `q_*\kappa^2/4<1`, then contact mixed corridors have a
finite renormalized exchange channel

```math
\frac{1}{16}[\mathsf Q_r^b,\mathsf Q_{r+1}^b]+O(\kappa^2),
```

while exchange between regions at positive physical separation vanishes
exponentially in `1/a`.

Finally, no version of this main theorem may replace the finite-depth or
renormalized inverse-control hypothesis by unconditional full Hamiltonian slab
inverse control: Theorem 6D gives a two-state resonance obstruction.

Proof. The finite gauge and center structure is Theorem 1B plus Proposition 2.
Cutoff leakage is controlled by Theorem 5G and Corollary 5H. Detector naturality
is Theorem 4E, and the projective statistic transfer is Theorem 5. The
growing-volume compact-rotor cutoff transfer is Theorem 7B. The explicit
electric-energy limit is Theorem 5E and Corollary 5F. The exchange statement is
Proposition 6A plus Theorem 6C and Theorem 6F, with finite-depth inverse control
supplied by Proposition 6B. The exclusion of unconditional full-slab inverse
control is exactly Theorem 6D. `square`

## 2. Inputs From V2 Papers 1-4

Paper 5 uses the following exported structure.

1. **Paper 1:** exchange defects become continuum-facing only after a controlled
   normalization and regulator limit.
2. **Paper 2:** projective states, cylinder effects, and refinement residuals are
   the right language for changing regulators.
3. **Paper 3:** raw comparison maps and exchange defects are useful only in an
   anchored topology with explicit inverse-control hypotheses.
4. **Paper 4:** operational claims require detector instruments, record sectors,
   calibrated residuals, screening for postselection, and projective detector
   naturality.

Paper 5 adds one new layer: **Gauss-law constrained projective structure**.
The local configuration space is not a tensor product of independent matter
regions. Boundary flux centers must be tracked.

## 3. Conservative Target

The target is an interval lattice in `1+1D`.

Let the sites be

```math
\Lambda_L=\{1,\ldots,L\}
```

and links be

```math
\Lambda_L^{\ell}=\{0,\ldots,L\},
```

where links `0` and `L` are boundary links. The matter variable at site `x` is a
finite charge variable

```math
n_x\in N_x,
```

with charge

```math
q_x(n_x)\in\mathbb Z.
```

For the minimal staggered benchmark one may take

```math
N_x=\{0,1\},
\qquad
q_x(n_x)=n_x-\rho_x,
```

with fixed background charge `rho_x` chosen so the total charge sector is
integer-compatible.

The compact `U(1)` electric flux on link `ell` is truncated to

```math
E_\ell\in\{-K,-K+1,\ldots,K\}.
```

The regulated finite configuration space before imposing Gauss law is

```math
C_{L,K}^{\mathrm{raw}}
=
\prod_{x=1}^L N_x
\times
\{-K,\ldots,K\}^{L+1}.
```

The physical finite configuration space is the Gauss-law subset

```math
C_{L,K}^{\mathrm{G}}
=
\left\{
(n,E)\in C_{L,K}^{\mathrm{raw}}:
E_x-E_{x-1}=q_x(n_x)\ \text{for every }x
\right\}.
```

The finite ordered state space is

```math
V_{L,K}^{\mathrm{G}}:=\mathbb R^{C_{L,K}^{\mathrm{G}}},
\qquad
V_{L,K,+}^{\mathrm{G}}:=\mathbb R_+^{C_{L,K}^{\mathrm{G}}}.
```

The boundary flux

```math
b:=E_0
```

is a center label. On an interval it is not optional bookkeeping: it determines
all link fluxes once the matter charges are known.

For the first complete Paper 5 theorem package, the benchmark is now fixed more
sharply:

```text
open chain, spinless staggered matter, compact U(1) electric links,
finite electric cutoff K, fixed boundary center b, and no periodic global-flux
tower.
```

The periodic ring and its global electric-flux tower are deferred. This is a
choice of rigor, not a claim that periodic gauge theory is unimportant. The open
chain is the smallest setting in which Gauss centers, cutoff tails, mixed
site-link collars, and operational detector statistics are all already forced.

## 4. Gauge-Compatible Primitive Kernels

A finite primitive slab kernel is a stochastic matrix

```math
\Gamma_{L,K}:V_{L,K}^{\mathrm{G}}\to V_{L,K}^{\mathrm{G}}.
```

For comparison with the Hilbert-gauge benchmark, one may obtain it from a
declared finite gauge-invariant lift

```math
U_{L,K}(\Delta)=e^{-i\Delta H_{L,K}},
\qquad
\Gamma_{L,K}(c'|c)=|U_{L,K}(c'|c)|^2,
```

where `H_{L,K}` preserves `C_{L,K}^{G}`. This lift is not hidden Hilbert-space
locality. In Paper 5 it is a declared benchmark control used to generate finite
stochastic kernels. The phase/lift data are part of the benchmark, not recovered
from one stochastic endpoint kernel.

Localized deformations are allowed only when they are gauge-compatible. A local
matter hop, for example, must be accompanied by the corresponding link-flux
shift so that

```math
E_x-E_{x-1}=q_x
```

remains true at every site. Thus the support of a local gauge operation is a
mixed site-link collar, not a pure set of sites.

### Theorem 1: finite Gauss-sector preservation

Let the raw finite configuration space decompose into Gauss sectors

```math
C_{L,K}^{\mathrm{raw}}
=
\bigsqcup_g C_{L,K}^{g},
```

where `g=(g_1,\ldots,g_L)` records the Gauss residuals

```math
g_x:=E_x-E_{x-1}-q_x(n_x).
```

If a declared finite lift `U_{L,K}` is block diagonal in this decomposition,

```math
U_{L,K}
=
\bigoplus_g U_{L,K}^{g},
```

then the Born-squared primitive kernel is also block diagonal:

```math
\Gamma_{L,K}
=
\bigoplus_g \Gamma_{L,K}^{g}.
```

In particular, the physical Gauss sector `g=0` is invariant. The same holds for
every localized gauge-compatible deformation `\Gamma_R` and therefore for
comparison maps and exchange defects restricted to an invertible Gauss block:

```math
J_R^0=\Gamma_R^0(\Gamma_0^0)^{-1},
\qquad
E_{R,S}^0=J_R^0J_S^0(J_R^0)^{-1}(J_S^0)^{-1}.
```

Proof. If `U(c'|c)=0` whenever `c` and `c'` lie in different Gauss sectors, then
`|U(c'|c)|^2=0` across the same sector split. Hence `\Gamma` is block diagonal.
The physical block is invariant by restriction. If both `\Gamma_R` and
`\Gamma_0` are block diagonal and `\Gamma_0^0` is invertible on the tested
physical block, then `J_R^0` and `E_{R,S}^0` are the corresponding blockwise
algebraic maps. `square`

This theorem is finite and exact. It does not prove uniform inverse control as
`L` or `K` grows.

### Definition 1A: concrete open-chain finite Hamiltonian/lift

For the first Paper 5 benchmark, take

```math
N_x=\{0,1\},
\qquad
q_x(n_x)=n_x-\rho_x,
\qquad
\rho_x\in\mathbb Z,
```

on an open chain. Let `\mathbf 1_x` be the unit occupation change at site `x`
and let `\eta_x` be the unit electric-flux change on link `x`, the link between
sites `x` and `x+1`.

For `x=1,\ldots,L-1`, define the right-hop partial isometry `T_x^+` on the
physical basis by

```math
T_x^+|n,E\rangle
=
\begin{cases}
|n-\mathbf 1_x+\mathbf 1_{x+1},\,E-\eta_x\rangle,
&
n_x=1,\ n_{x+1}=0,\ E_x>-K,\\
0,&\text{otherwise}.
\end{cases}
```

Set

```math
T_x^-=(T_x^+)^*.
```

Thus a unit positive charge moving right lowers the intervening electric flux by
one. This is the sign convention compatible with

```math
E_x-E_{x-1}=q_x(n_x).
```

Fix

```math
t_a:=\frac{1}{2a}
```

and define the finite Hamiltonian

```math
H_{L,K}
=
H_{\mathrm{hop}}+H_E+H_m,
```

with

```math
H_{\mathrm{hop}}
=
-t_a\sum_{x=1}^{L-1}(T_x^++T_x^-),
```

```math
H_E
=
\frac{g^2a}{2}\sum_{\ell=0}^{L}E_\ell^2,
```

and

```math
H_m
=
\sum_{x=1}^{L}m_x n_x.
```

The staggered choice `m_x=m(-1)^x` is the default Schwinger-like benchmark, but
the finite-sector facts below use only that `H_m` is diagonal in the occupation
basis. The declared primitive lift is

```math
U_{L,K}(\Delta)=e^{-i\Delta H_{L,K}},
\qquad
\Gamma_{L,K}(c'|c)=|U_{L,K}(c'|c)|^2.
```

### Theorem 1B: concrete lift preserves Gauss sectors and boundary centers

The hopping formula of Definition 1A preserves all Gauss residuals when read on
the raw configuration basis, and its restriction to the physical sector is a
finite Hermitian matrix on `\ell^2(C_{L,K}^{\mathrm{G}})`. It preserves every
boundary center `b=E_0`. Therefore `U_{L,K}(\Delta)` and `\Gamma_{L,K}` are
block diagonal in the physical decomposition

```math
C_{L,K}^{\mathrm{G}}
=
\bigsqcup_b C_{L,K}^{\mathrm{G}}(b).
```

Moreover, each elementary hopping term changes exactly one link flux by one and
only when the resulting basis vector remains inside the truncation window.

Proof. The diagonal terms `H_E` and `H_m` preserve every basis vector, hence
preserve Gauss residuals and `b`. The hopping calculation can be done on any raw
configuration for which the hop is allowed. For `T_x^+`, the charge at `x`
decreases by one, the charge at `x+1` increases by one, and the link flux `E_x`
decreases by one. Thus

```math
(E_x-1)-E_{x-1}
=
(E_x-E_{x-1})-1
=
q_x(n_x)-1,
```

while

```math
E_{x+1}-(E_x-1)
=
(E_{x+1}-E_x)+1
=
q_{x+1}(n_{x+1})+1.
```

All other Gauss equations are unchanged. The adjoint hop is the reverse
calculation. Endpoint truncation is handled by the partial-isometry definition,
which sends forbidden hops to zero rather than to a nonphysical state. Interior
hops do not touch `E_0`, so the boundary center is preserved. Hermiticity is
immediate from `T_x^-=(T_x^+)^*` and the real diagonal terms. Exponentiation and
entrywise Born squaring preserve the same block decomposition. `square`

## 5. Open-Chain Gauss Reduction And Boundary Centers

On an interval, Gauss law can be solved explicitly.

### Proposition 2: boundary-center Gauss reduction

Fix the boundary flux

```math
b:=E_0.
```

For every matter configuration `n`, Gauss law determines the link fluxes by

```math
E_x
=
b+\sum_{y=1}^x q_y(n_y),
\qquad
x=1,\ldots,L.
```

Therefore the physical truncated configuration space decomposes as

```math
C_{L,K}^{\mathrm{G}}
=
\bigsqcup_b C_{L,K}^{\mathrm{G}}(b),
```

where

```math
C_{L,K}^{\mathrm{G}}(b)
\cong
\left\{
n\in\prod_xN_x:
\left|b+\sum_{y=1}^xq_y(n_y)\right|\le K
\ \text{for all }x
\right\}.
```

Proof. Starting from `E_0=b`, recursively solve
`E_x=E_{x-1}+q_x(n_x)`. This gives the displayed formula. The truncation condition
is exactly the requirement that every determined link flux lies in
`[-K,K]`. `square`

The boundary flux `b` is a center variable. If it is not measured or fixed, a
state is a classical mixture over center sectors:

```math
p=\sum_b w_b p_b,
\qquad
w_b\ge0,
\qquad
\sum_bw_b=1.
```

Matter-only reduced statistics can therefore hide center dependence. Paper 5
must keep this visible.

## 6. Finite Cutoff And No-Truncation Windows

The compact rotor has `E_\ell\in\mathbb Z`, not `[-K,K]`. A finite truncation can
represent a local process exactly only if that process never tries to leave the
cutoff window.

Let a local gauge-compatible operation `O_A` have flux shift radius `r_A`, meaning
that on every link it changes electric flux by at most `r_A` on any single
allowed transition:

```math
|E_\ell'-E_\ell|\le r_A.
```

For a state `p`, define its cutoff margin

```math
m_K(p):=
\inf\{K-|E_\ell(c)|: p(c)>0,\ \ell\in\Lambda_L^\ell\}.
```

### Theorem 3: no-truncation window

Let `O_A^{\mathrm{rot}}` be a compact-rotor gauge-compatible local stochastic
operation and let `O_A^K` be its finite cutoff restriction. If a normalized state
`p` is supported in the physical sector and satisfies

```math
m_K(p)>r_A,
```

then

```math
O_A^Kp=O_A^{\mathrm{rot}}p
```

after identifying the finite cutoff states with the corresponding rotor states.
For an operation string `O_{A_m}\cdots O_{A_1}`, equality holds if

```math
m_K(p)>\sum_{j=1}^m r_{A_j}.
```

Proof. A single operation cannot produce any transition outside `[-K,K]` when
the initial support is farther than `r_A` from the cutoff boundary. Thus the
finite transition list and the rotor transition list coincide on the support of
`p`. Iterate the argument for operation strings, subtracting the possible flux
shift radius at each step. `square`

### Corollary 3A: concrete no-truncation for the open-chain lift

Let `H^{\mathrm{rot}}_{L}` denote the same open-chain Hamiltonian as
Definition 1A, but with electric fluxes `E_\ell\in\mathbb Z` rather than
`[-K,K]`. For a support set `S` in a fixed boundary center `b`, define its
Hamiltonian reachable hull by

```math
\operatorname{Reach}_H(S)
:=
\{c':\exists c\in S,\ \exists n\ge0\ \text{with }
\langle c'|H_L^{\mathrm{rot}\,n}|c\rangle\ne0\}.
```

Define the reachable flux radius

```math
r_H(S)
:=
\max_{c\in S,\ c'\in\operatorname{Reach}_H(S),\ \ell}
|E_\ell(c')-E_\ell(c)|.
```

For an open chain with finite matter alphabet, `r_H(S)` is finite on every fixed
finite interval. If

```math
m_K(S):=
\inf\{K-|E_\ell(c)|:c\in S,\ell\in\Lambda_L^\ell\}
>
r_H(S),
```

then

```math
e^{-i\Delta H_{L,K}}\psi
=
e^{-i\Delta H_L^{\mathrm{rot}}}\psi
```

for every Hilbert vector `\psi` supported in `S`, after identifying the finite
states with their rotor counterparts. Consequently the Born-squared kernels
also agree on that support.

For the local gate factor

```math
G_x(\delta):=\exp\{-i\delta[-t_a(T_x^++T_x^-)]\},
```

the flux shift radius is exactly `1`. For diagonal electric and mass gates it is
`0`. Hence any declared finite string of `M` bond gates and diagonal gates has
no-truncation radius at most `M`, and at most the number of bond gates touching a
given tested link for link-local estimates.

ISP caveat. This gate string is a declared Hilbert-lift construction used to
bound the finite reachable hull before Born squaring. It is not an assumption
that an arbitrary endpoint stochastic kernel is Markov-divisible through the
individual gates. If the individual gate records are not declared physical
division events, the stochastic object used by Paper 5 is the whole declared
operation or slab and its Born-squared endpoint kernel.

Proof. In a fixed open-chain center sector, Gauss law expresses every link flux
as the boundary center plus a finite matter prefix. Since the finite interval
has only finitely many matter configurations, the set of matter configurations
reachable from `S` is finite, and so is `r_H(S)`. If the cutoff margin exceeds
this radius, every basis vector appearing in the rotor reachable hull lies
inside `[-K,K]`; the finite and rotor Hamiltonian matrices therefore have the
same rows and columns on the invariant hull generated by `S`. Functional
calculus gives equality of the exponentials there, and entrywise absolute
squares give equality of primitive kernels. A single bond gate only swaps the
two adjacent occupations and shifts the intervening link by `\pm1`; diagonal
gates shift no flux. The string bound follows by composition. `square`

### Lemma 3B: finite-energy cutoff-tail estimate

Let `A^\ell` be the finite set of links on which a tested local operation can
read or shift electric flux, and let `r` be the operation's flux shift radius.
For `K>r`, define the cutoff-boundary event

```math
B_{K,r}(A)
:=
\{c:\exists \ell\in A^\ell\ \text{with } |E_\ell(c)|\ge K-r\}.
```

For a normalized state `p`, set

```math
\mathcal E_A(p)
:=
\sum_{\ell\in A^\ell}
\frac{g^2a}{2}\,
\mathbb E_p[E_\ell^2].
```

If `g>0`, then

```math
p(B_{K,r}(A))
\le
\frac{2\mathcal E_A(p)}
{g^2a(K-r)^2}.
```

Moreover, for any local effect `0\le e\le1`,

```math
\left|e^T(O_A^K-O_A^{\mathrm{rot}})p\right|
\le
2\,p(B_{K,r}(A))
\le
\frac{4\mathcal E_A(p)}
{g^2a(K-r)^2}.
```

Proof. If `B_{K,r}(A)` occurs, then
`\sum_{\ell\in A^\ell}E_\ell^2\ge(K-r)^2`. Markov's inequality gives the first
bound after multiplying by `g^2a/2`. On the complement of `B_{K,r}(A)`,
Theorem 3 gives exact agreement between the finite and rotor operations. The
two operations may differ only on the exceptional mass
`\varepsilon=p(B_{K,r}(A))`; pairing subnormalized positive outputs with an
effect bounded by one gives a total possible difference at most `2\varepsilon`.
`square`

### Corollary 3C: volume-growth obstruction

Without restrictions on charge sectors or boundary flux, representing the full
open-chain physical space requires

```math
K\ge
\max_{n,b,x}
\left|
b+\sum_{y=1}^xq_y(n_y)
\right|,
```

which typically grows with `L`. Therefore a compact-rotor continuum theorem does
not follow from any fixed `K` finite benchmark. One must either:

1. let `K=K(a,L)` grow in a controlled way;
2. restrict to a finite-energy or bounded-flux sector;
3. prove that the tested local cylinder statistics have negligible cutoff-boundary
   mass.

This is the first major Paper 5 pass/fail gate.

## 7. Projective Gauge Families

A continuum-facing gauge benchmark is a directed family indexed by

```math
\alpha=(a,L,K)
```

with `a -> 0`, `L -> infinity`, and `K -> infinity` along an admissible scaling
regime. The projective maps must preserve three structures:

1. matter cylinder variables;
2. link-flux or integrated electric-flux variables;
3. boundary-center labels.

Let

```math
P_{\alpha\leftarrow\alpha'}:
V_{\alpha'}^{\mathrm{G}}\to V_\alpha^{\mathrm{G}}
```

be a positive coarse-graining map. A cylinder effect `e_\alpha` is compatible
with refinement when

```math
e_{\alpha'}=P_{\alpha\leftarrow\alpha'}^Te_\alpha.
```

Primitive kernels are projectively compatible on a tested class if

```math
\left\|
P_{\alpha\leftarrow\alpha'}\Gamma_{\alpha'}
-
\Gamma_\alpha P_{\alpha\leftarrow\alpha'}
\right\|_{1,\mathrm{test}}
\le
\epsilon_{\mathrm{ker}}(\alpha',\alpha).
```

For gauge theory there are additional residuals:

```math
\epsilon_{\mathrm{cut}}:
\text{ mass near or crossing the electric cutoff boundary},
```

```math
\epsilon_{\mathrm{cent}}:
\text{ boundary-center mismatch or unresolved center mixing},
```

```math
\epsilon_{\mathrm{G}}:
\text{ Gauss-sector leakage under approximate dynamics or coarse-graining}.
```

In exact gauge-compatible finite blocks, `\epsilon_{\mathrm{G}}=0`. In approximate or
lossy coarse-grained models it must be measured.

### Definition 5A: locally admissible cutoff scaling

Let `I` be a fixed compact physical interval and let `A_a^\ell(I)` be the set of
lattice links whose geometric links meet `I`, enlarged by the fixed detector or
operation collar. A tested preparation family `p_{a,L,K}^b` is locally
finite-electric-energy on `I` if

```math
\sup_{a,L,K}
\mathcal E_{A_a(I)}(p_{a,L,K}^b)
\le E_I<\infty,
```

where

```math
\mathcal E_{A_a(I)}(p)
=
\sum_{\ell\in A_a^\ell(I)}
\frac{g^2a}{2}\mathbb E_p[E_\ell^2].
```

For a tested operation family with flux shift radius bounded by `r_*`, a cutoff
choice `K=K(a,L)` is locally admissible on `I` when

```math
K(a,L)>r_*,
\qquad
a\bigl(K(a,L)-r_*\bigr)^2\longrightarrow\infty
```

along the refinement net. Equivalently, a power-law choice

```math
K(a,L)=\lceil a^{-\beta}\rceil
```

is locally admissible for finite-energy tests whenever

```math
\beta>\frac12.
```

This is a local-cylinder condition. It is not a claim that the entire infinite
volume has no cutoff-boundary mass.

### Theorem 5B: local cutoff stability under admissible scaling

Fix a compact physical interval `I`, a fixed center sector `b`, and a tested
operation/effect pair whose flux shift radius is at most `r_*` and whose support
is contained in `A_a(I)`. If `p_{a,L,K}^b` is locally finite-electric-energy on
`I` with bound `E_I`, then

```math
\epsilon_{\mathrm{cut}}(a,L,K;I)
:=
\sup_{0\le e\le1}
\left|e^T(O_{A_a}^{K}-O_{A_a}^{\mathrm{rot}})p_{a,L,K}^b\right|
\le
\frac{4E_I}
{g^2a(K(a,L)-r_*)^2}.
```

Thus every locally admissible cutoff scaling sends
`\epsilon_{\mathrm{cut}}(a,L,K;I)` to zero uniformly in the total volume `L`,
provided the local energy bound is uniform in `L`.

Proof. This is Lemma 3B with `A^\ell=A_a^\ell(I)` and `r=r_*`. The right-hand
side tends to zero exactly when `a(K-r_*)^2 -> infinity`. No union bound over
all links in the total volume is used, so the estimate is local-cylinder and
volume-uniform on the tested class. `square`

The condition `a(K-r_*)^2 -> infinity` is a conservative black-box condition:
it uses only local electric-energy control and ignores the extra one-dimensional
Gauss-law geometry. It is therefore safe, but not the best available condition
for center-tight gauge preparations.

### Theorem 5G: Gauss-slope improved cutoff scaling

Assume the local charge alphabet is uniformly bounded and nontrivial:

```math
0<Q_*:=\sup_{x,n_x}|q_x(n_x)|<\infty.
```

Let `A=[r,s]` be the tested site interval and let `c_A=E_{r-1}` be its incoming
local center. For `B\ge0`, write

```math
G_B:=\{|c_A|\le B\}.
```

Let `h:=K-r_*` and assume `h>B+4Q_*`. For every normalized physical preparation
with local electric-energy bound `\mathcal E_A(p)\le E_I`,

```math
p(B_{K,r_*}(A))
\le
p(G_B^c)
+
\frac{32Q_*E_I}
{g^2a(h-B)^3}.
```

Consequently, on any tested class with tight local centers, the cutoff leakage
vanishes whenever

```math
a\bigl(K(a,L)-r_*-B\bigr)^3\longrightarrow\infty
```

after choosing `B` so that `p(G_B^c)` is small uniformly on the class. In
particular, if the local center is uniformly bounded and

```math
K(a,L)=\lceil a^{-\beta}\rceil,
```

then every

```math
\beta>\frac13
```

is sufficient for local cutoff stability under the same finite-energy
hypothesis.

Proof. On the event `G_B\cap B_{K,r_*}(A)`, some active link has
`|E_\ell|\ge h` while the incoming center satisfies `|E_{r-1}|\le B`. Gauss law
and the bounded charge alphabet imply the discrete Lipschitz bound

```math
|E_x-E_{x-1}|\le Q_*.
```

To rise from magnitude at most `B` to magnitude at least `h`, the electric
profile must contain at least order `(h-B)/Q_*` links whose magnitude is at
least order `h-B`. More explicitly, for `h>B+4Q_*`,

```math
\sum_{\ell\in A^\ell}E_\ell^2
\ge
\frac{(h-B)^3}{16Q_*}.
```

Therefore

```math
\mathcal E_A(c)
=
\frac{g^2a}{2}\sum_{\ell\in A^\ell}E_\ell(c)^2
\ge
\frac{g^2a(h-B)^3}{32Q_*}
```

on the good-center cutoff event. Markov's inequality gives the displayed bound,
and the scaling statements follow. `square`

### Corollary 5H: cutoff regimes by preparation class

The cutoff scale required by Paper 5 depends on what is assumed about the tested
preparations:

1. **Black-box finite local energy:** `a(K-r_*)^2 -> infinity` is sufficient by
   Theorem 5B. This is robust but conservative.
2. **Finite local energy plus tight local center and bounded charge alphabet:**
   `a(K-r_*-B)^3 -> infinity` is sufficient by Theorem 5G; power laws need only
   `K>>a^{-1/3}`.
3. **Deterministic bounded electric profiles:** if `K` eventually exceeds the
   profile bound, cutoff leakage is exactly zero on the tested collar.
4. **Uniformly bounded-flux preparation classes:** if
   `p(\max_{\ell\in A^\ell}|E_\ell|>B)=0` for a fixed `B`, then any
   `K>B+r_*` is sufficient.
5. **Direct tail-controlled classes:** if a model-specific estimate gives

```math
p(B_{K,r_*}(A))\le \tau_A(K-r_*),
\qquad
\tau_A(u)\to0,
```

then Paper 5 may use that tail directly instead of either power-law condition.

Thus the `K>>a^{-1/2}` condition should be read as a universally safe
second-moment fallback, not as a physical prediction of the gauge benchmark.
If `Q_*=0`, the local electric field is constant inside each center sector, so
cutoff leakage is controlled entirely by the center-tail term.

### Example 5C: clipped local electric-energy statistic

For a compact physical interval `I`, define the local electric energy random
variable

```math
X_{I,a}(c)
:=
\frac{g^2a}{2}
\sum_{\ell\in A_a^\ell(I)}E_\ell(c)^2.
```

For a clipping scale `M>0`, define the bounded cylinder effect

```math
e_{I,M,a}(c)
:=
\min\{1,X_{I,a}(c)/M\}.
```

The statistic

```math
S_{I,M}^{a,K}(p)
:=
e_{I,M,a}^Tp
```

is a concrete center-resolved gauge statistic. It is not raw exchange curvature,
and it is not a matter-only observable: it reads the electric center-resolved
link content in the local collar.

If the corresponding compact-rotor statistic `S_{I,M}^{a,\mathrm{rot}}` has a
projective continuum limit `S_{I,M}^{\mathrm{cont}}` on a tested preparation
family, then under the locally admissible scaling of Theorem 5B,

```math
\left|
S_{I,M}^{a,K(a,L)}(p_{a,L,K}^b)
-
S_{I,M}^{\mathrm{cont}}
\right|
\le
\frac{4E_I}{g^2a(K(a,L)-r_*)^2}
+
\left|
S_{I,M}^{a,\mathrm{rot}}(p_{a,L}^{\mathrm{rot},b})
-
S_{I,M}^{\mathrm{cont}}
\right|.
```

Hence this statistic is controlled by two visible burdens: finite-cutoff
leakage and the rotor/projective continuum limit. Paper 5 proves the first
burden here; the second is a genuine continuum input, not a finite-matrix fact.
For center-tight bounded-charge preparation classes, the finite-cutoff term may
be replaced by the improved Theorem 5G bound.

### Definition 5D: admissible deterministic electric profiles

Fix a compact physical interval `I=[x_-,x_+]`. An integer-valued continuum
electric profile on `I` is a bounded function

```math
e:I\to\mathbb Z
```

that is constant except at finitely many jump points. It is admissible for the
chosen matter alphabet if, for every jump of size `\Delta e`, the local charge
alphabet can realize that Gauss jump:

```math
\Delta e\in q_x(N_x)
```

after placing the jump on a lattice site near the continuum jump point. The
constant profile `e(x)=b` is admissible in any active interval whose matter
alphabet contains a neutral local state `q_x(n_x)=0`; this is the default
charge-neutral subcase used below.

For a lattice spacing `a`, choose a lattice electric profile `E_a` by assigning
to each active link the integer value of `e` at a representative point on that
link, and place the finitely many required matter charges at the corresponding
jump sites. The resulting active configuration satisfies Gauss law by
construction:

```math
E_x-E_{x-1}=q_x(n_x).
```

Let `p_a^e` be the point-mass preparation on this center-resolved active
configuration, extended arbitrarily outside the tested collar as long as the
extension remains physical and has no effect on `e_{I,M,a}`.

### Theorem 5E: continuum limit of the clipped electric-energy statistic

Let `e:I\to\mathbb Z` be an admissible deterministic electric profile and let
`p_a^e` be the associated center-resolved lattice preparation of Definition 5D.
Assume `K(a,L)>\|e\|_\infty` eventually. Then the statistic of Example 5C has
the continuum limit

```math
\lim_{a\to0}
S_{I,M}^{a,K(a,L)}(p_a^e)
=
\min\left\{
1,
\frac{1}{M}
\frac{g^2}{2}
\int_I e(x)^2\,dx
\right\}.
```

In particular, for the charge-neutral constant-center profile `e(x)=b`,

```math
\lim_{a\to0}
S_{I,M}^{a,K(a,L)}(p_a^b)
=
\min\left\{
1,
\frac{g^2b^2|I|}{2M}
\right\}.
```

This is a genuine growing-volume local continuum statement: the limit depends
only on the fixed physical interval `I`, the center-resolved profile on `I`, and
the local clipping scale `M`, not on the total lattice volume.

Proof. On `p_a^e`, the statistic is the deterministic number

```math
S_{I,M}^{a,K}(p_a^e)
=
\min\left\{
1,
\frac{1}{M}
\frac{g^2a}{2}
\sum_{\ell\in A_a^\ell(I)}E_a(\ell)^2
\right\}.
```

Since `e` is bounded and has only finitely many jumps, the sum is an ordinary
Riemann sum:

```math
a\sum_{\ell\in A_a^\ell(I)}E_a(\ell)^2
\longrightarrow
\int_I e(x)^2\,dx.
```

The clipping map `y\mapsto\min\{1,y/M\}` is continuous, so the displayed limit
follows. If `K(a,L)>\|e\|_\infty`, no cutoff event occurs on the active links;
hence the finite cutoff and rotor statistics agree on this preparation for all
sufficiently small `a`. `square`

### Corollary 5F: finite mixtures of deterministic center profiles

Let

```math
p_a
=
\sum_{j=1}^N w_jp_a^{e_j},
\qquad
w_j\ge0,
\qquad
\sum_jw_j=1,
```

where each `e_j:I\to\mathbb Z` is an admissible deterministic profile and
`K(a,L)>\max_j\|e_j\|_\infty` eventually. Then

```math
\lim_{a\to0}
S_{I,M}^{a,K(a,L)}(p_a)
=
\sum_{j=1}^N
w_j
\min\left\{
1,
\frac{1}{M}
\frac{g^2}{2}
\int_I e_j(x)^2\,dx
\right\}.
```

Thus Example 5C is no longer merely a conditional statistic: it has a proved
continuum limit on a nonempty center-resolved preparation class, including
constant-flux sectors and finite mixtures of admissible step-flux sectors.

Proof. The statistic is linear in the preparation `p_a`, and Theorem 5E applies
to each component. `square`

## 8. Center-Resolved Operational Statistics

Let `b` label boundary flux centers and let `\Pi_b` be the sector projection.
A center-resolved detector instrument has outcome labels `(o,b)` or otherwise
conditions on a fixed center sector.

### Proposition 4: unresolved centers give mixtures, not one local sector

Let an operational statistic in a fixed center sector be

```math
S_b(e,p_b)
:=
e^T\mathsf I_b p_b.
```

For a center-unresolved preparation

```math
p=\sum_bw_bp_b,
```

and an instrument preserving center sectors,

```math
\mathsf I=\bigoplus_b\mathsf I_b,
```

the observed statistic is

```math
S(e,p)
=
\sum_bw_bS_b(e,p_b).
```

Unless all `S_b` agree on the tested class, there is no single center-independent
local statistic.

Proof. Apply the block decomposition and linearity:

```math
e^T\mathsf I p
=
\sum_bw_be^T\mathsf I_bp_b.
```

`square`

This is not a defect. It is gauge theory. Boundary centers are part of the
physical local algebra. Matter-only reductions are allowed only after the
center mixture is declared.

### Theorem 4A: center-resolved locality bound

Let `A=[r,s]` be a finite interval of sites and let

```math
c_A:=E_{r-1}
```

be the incoming electric flux at the left boundary of `A`. Inside `A`, Gauss law
gives

```math
E_x
=
c_A+\sum_{y=r}^{x}q_y(n_y),
\qquad
r\le x\le s.
```

Thus a gauge-compatible instrument supported in the mixed collar of `A` is local
only after the local center `c_A` is fixed or explicitly included among the
record labels.

Let an instrument decompose as

```math
\mathsf I_A=\bigoplus_c\mathsf I_{A,c}
```

with respect to `c_A`, and let

```math
p_A=\sum_c w_cp_{A,c}
```

be the center decomposition of the tested local preparation, with each
`p_{A,c}` normalized when `w_c>0`. For any effect `0\le e_A\le1`,

```math
S_A(e_A,p_A)
=
\sum_cw_cS_{A,c}(e_A,p_{A,c}),
\qquad
S_{A,c}:=e_A^T\mathsf I_{A,c}p_{A,c}.
```

If one replaces the center-resolved statistic by a representative center `c_0`,
the error is bounded by

```math
\left|
S_A(e_A,p_A)-S_{A,c_0}(e_A,p_{A,c_0})
\right|
\le
\sum_cw_c
\left|
S_{A,c}(e_A,p_{A,c})-S_{A,c_0}(e_A,p_{A,c_0})
\right|
\le
\operatorname{osc}_c S_{A,c}.
```

Consequently a matter-only local statistic is justified only on a tested class
for which

```math
\operatorname{osc}_c S_{A,c}
\le
\epsilon_{\mathrm{cent}}(A).
```

Proof. The displayed recursion is Proposition 2 applied with left boundary
`r-1` instead of the global boundary. The statistic decomposition is linearity
over the direct-sum center blocks. The error estimate is the triangle
inequality, followed by the definition of the oscillation over tested center
sectors. `square`

### Definition 4B: center-cutoff-Gauss detector records

A gauge-compatible local detector on `A=[r,s]` must record more than an outcome
`o`. Its minimal Paper 4-compatible record label is

```math
\omega_A=(o,c_A,\chi_{\mathrm{cut}},\chi_{\mathrm{G}}),
```

where:

1. `o` is the ordinary detector outcome;
2. `c_A=E_{r-1}` is the incoming local center;
3. `\chi_{\mathrm{cut}}\in\{0,1\}` flags whether the tested operation entered
   the cutoff-boundary event `B_{K,r_*}(A)`;
4. `\chi_{\mathrm{G}}\in\{0,1\}` flags Gauss-sector leakage.

In the exact finite gauge blocks of Definition 1A, `\chi_{\mathrm{G}}=0`
identically. It
is still included because approximate coarse-grained detectors and lossy
records must expose Gauss leakage rather than hide it in the outcome channel.

A detector instrument has the form

```math
\mathsf I_A
=
\bigoplus_{c_A}
\sum_{o,\chi_{\mathrm{cut}},\chi_{\mathrm{G}}}
\mathsf I_{A}^{o,c_A,\chi_{\mathrm{cut}},\chi_{\mathrm{G}}},
```

with positive components whose sum is column-stochastic on the tested physical
block.

### Theorem 4C: recorded gauge detectors are Paper 4-compatible

Consider two refinements `\alpha'\ge\alpha` of the same physical interval `A`.
Suppose:

1. the detector's ordinary outcome channel has Paper 4 record-naturality
   residual `\epsilon_{\mathrm{rec}}^{0}`;
2. the local center is either exactly preserved by the projective map or has
   mismatch residual `\epsilon_{\mathrm{cent}}`;
3. the cutoff-boundary event has probability at most
   `\epsilon_{\mathrm{cut}}`;
4. Gauss leakage has probability at most `\epsilon_{\mathrm{G}}`.

Then the recorded detector family satisfies

```math
\left\|
P_{\alpha\leftarrow\alpha'}\mathsf I_{A,\alpha'}
-
\mathsf I_{A,\alpha}P_{\alpha\leftarrow\alpha'}
\right\|_{1,\mathrm{test}}
\le
\epsilon_{\mathrm{rec}}^{0}
+
\epsilon_{\mathrm{cent}}
+
2\epsilon_{\mathrm{cut}}
+
\epsilon_{\mathrm{G}}.
```

For the exact open-chain finite benchmark with fixed local center and no cutoff
event on the tested support, this reduces to the ordinary Paper 4 detector
naturality residual.

Proof. Decompose the record space into the direct sum over `c_A`,
`\chi_{\mathrm{cut}}`, and `\chi_{\mathrm{G}}`. On the good block
`(\chi_{\mathrm{cut}},\chi_{\mathrm{G}})=(0,0)` with matching center, the only
mismatch is the ordinary detector residual. Center mismatch contributes
`\epsilon_{\mathrm{cent}}`. Gauss leakage contributes
`\epsilon_{\mathrm{G}}`. The cutoff bad mass can be routed differently before
and after coarse-graining, so its worst-case contribution to a column-norm
comparison is twice its probability. Summing the disjoint record contributions
gives the bound. `square`

### Protocol 4D: explicit center-cutoff-Gauss readout

Fix a tested interval `A=[r,s]`, a flux-shift radius budget `r_*`, and a finite
outcome partition

```math
\mathcal O_A=\{O_1,\ldots,O_m\}
```

of the local site-link configurations on the mixed collar of `A`. The explicit
detector protocol is:

1. read the incoming center `c_A=E_{r-1}`;
2. compute the local Gauss residuals

```math
g_x=E_x-E_{x-1}-q_x(n_x),
\qquad
r\le x\le s;
```

3. set `\chi_{\mathrm{G}}=1` iff some `g_x\ne0`;
4. set `\chi_{\mathrm{cut}}=1` iff some active link satisfies
   `|E_\ell|\ge K-r_*`;
5. set `o=i` iff the collar configuration lies in `O_i`;
6. append the record

```math
\omega_A=(o,c_A,\chi_{\mathrm{cut}},\chi_{\mathrm{G}})
```

without changing the underlying physical configuration.

As a deterministic instrument on the extended configuration-record space,

```math
[\mathsf D_A]_{(c,\omega),c_0}
=
\mathbf 1_{\{c=c_0\}}\,
\mathbf 1_{\{\omega=\omega_A(c_0)\}}.
```

A noisy detector is obtained by composing this deterministic readout with a
column-stochastic classical confusion channel

```math
R_A(\omega_{\mathrm{obs}}|\omega_{\mathrm{true}}).
```

Thus

```math
\mathsf I_A^R
=
R_A\mathsf D_A.
```

### Theorem 4E: protocol naturality and explicit residual

Let `\alpha'\ge\alpha` be two refinements of the same tested physical interval
`A`. Suppose the coarse-graining map preserves the collar variables used in
Protocol 4D on the good record block:

```math
c_A,\quad
o,\quad
\chi_{\mathrm{cut}}=0,\quad
\chi_{\mathrm{G}}=0.
```

Let `R_{\alpha'}` and `R_\alpha` be the classical detector confusion channels,
coarse-grained to the same record alphabet. Define

```math
\epsilon_R
:=
\sup_{\omega}
\frac12
\sum_{\omega_{\mathrm{obs}}}
\left|
R_{\alpha'}(\omega_{\mathrm{obs}}|\omega)
-
R_{\alpha}(\omega_{\mathrm{obs}}|\omega)
\right|.
```

Then on normalized tested preparations,

```math
\left\|
P_{\alpha\leftarrow\alpha'}\mathsf I_{A,\alpha'}^{R}
-
\mathsf I_{A,\alpha}^{R}P_{\alpha\leftarrow\alpha'}
\right\|_{1,\mathrm{test}}
\le
2\epsilon_R
+
\epsilon_{\mathrm{cent}}
+
2\epsilon_{\mathrm{cut}}
+
\epsilon_{\mathrm{G}}.
```

In particular, for exact readout `R=I`, exact center matching, exact Gauss
blocks, and no cutoff-boundary mass, the protocol is exactly natural:

```math
P_{\alpha\leftarrow\alpha'}\mathsf D_{A,\alpha'}
=
\mathsf D_{A,\alpha}P_{\alpha\leftarrow\alpha'}.
```

Proof. On the good block the deterministic record is a cylinder function of the
variables preserved by the coarse-graining map, so deterministic readout
commutes exactly with projection. The only good-block discrepancy for noisy
detectors is the total-variation mismatch of the classical confusion channels,
which contributes at most `2\epsilon_R` in column norm. The bad center, cutoff,
and Gauss blocks are disjoint exceptional record sectors and contribute the
same residuals as in Theorem 4C. `square`

## 9. Continuum-Facing Stability Theorem

### Theorem 5: conditional projective stability of gauge operational statistics

Fix a local cylinder effect `e_\alpha`, a center-resolved preparation class
`\mathcal P_\alpha^b`, and a gauge-compatible operational instrument
`\mathsf I_\alpha^b`. Let `\alpha'\ge\alpha`. Suppose:

1. primitive kernel compatibility holds with residual `\epsilon_{\mathrm{ker}}`;
2. detector record-sector naturality holds with residual `\epsilon_{\mathrm{rec}}`;
3. electric cutoff leakage is bounded by `\epsilon_{\mathrm{cut}}`;
4. boundary-center mismatch is bounded by `\epsilon_{\mathrm{cent}}`;
5. Gauss-sector leakage is bounded by `\epsilon_{\mathrm{G}}`;
6. the tested preparation/effect pair is compatible under the projective maps.

Then, for normalized tested preparations,

```math
\left|
e_\alpha^T
\left(
P_{\alpha\leftarrow\alpha'}\mathsf I_{\alpha'}^b
-
\mathsf I_\alpha^bP_{\alpha\leftarrow\alpha'}
\right)p_{\alpha'}
\right|
\le
\epsilon_{\mathrm{ker}}
+
\epsilon_{\mathrm{rec}}
+
\epsilon_{\mathrm{cut}}
+
\epsilon_{\mathrm{cent}}
+
\epsilon_{\mathrm{G}}.
```

If every residual on the right tends to zero along the directed refinement net,
then the center-resolved operational statistic has a projective continuum limit.

Proof. This is Paper 4's projective record-instrument transfer with the gauge
residuals made explicit. The kernel and record terms are controlled exactly as
in Paper 4. Cutoff leakage accounts for the mass whose rotor evolution is not
represented by the finite `K` block. Center mismatch accounts for coarse-graining
or comparing different boundary-flux sectors. Gauss leakage accounts for any
failure to remain inside the physical block. Pairing with `0\le e\le1` cannot
increase the column-norm residual. `square`

This theorem is conditional but important. It says exactly what Paper 5 must
prove in a model, and exactly how failure is measured.

## 10. Gauge-Compatible Comparison Maps And Exchange Defects

For a gauge-compatible localized deformation in mixed site-link collar `R`,
define on a fixed center sector

```math
J_R^{b}
:=
\Gamma_R^b(\Gamma_0^b)^{-1}.
```

The raw gauge exchange defect is

```math
E_{R,S}^{b}
:=
J_R^bJ_S^b(J_R^b)^{-1}(J_S^b)^{-1}.
```

Paper 5 does not assume these maps are operational observables. Paper 4 says
they become testable only after detector realization and projection onto
preparation/effect pairs.

### Theorem 6: conditional gauge operational exchange transfer

Fix center sector `b`. Suppose:

1. `J_R^b`, `J_S^b`, and their inverses exist on the tested finite gauge block;
2. the raw exchange defect satisfies a center-resolved corridor estimate

```math
\|E_{R,S}^{b}-I\|_{\nu,R:S}^{\mathrm{corr}}
\le
B_{\alpha,K,L}(R,S);
```

3. gauge-compatible detector instruments realize calibrated operational
responses

```math
\mathscr J_R^{\mathrm{op},b}
=
J_R^b+\mathcal D_R^b,
\qquad
\mathscr J_S^{\mathrm{op},b}
=
J_S^b+\mathcal D_S^b;
```

4. the operational exchange calibration residual on the tested pair is
`\varepsilon_{\mathrm{ex}}^b(e,p;R,S)`.

Then Paper 4's exchange theorem gives

```math
\left|
\Delta_{R,S}^{\mathrm{op},b}(e,p)
\right|
\le
C_{\mathrm{corr}}(e,p;R,S)
B_{\alpha,K,L}(R,S)
+
\varepsilon_{\mathrm{ex}}^b(e,p;R,S).
```

If the bound tends to zero under refinement, the tested gauge operational
exchange is continuum-compatible. If it converges to a nonzero center-resolved
limit, that limit is a candidate gauge-sector stochastic curvature observable.

Proof. This is Theorem 13 of Paper 4 applied inside one Gauss/boundary-center
block. The new gauge burden is only the proof of the center-resolved corridor
estimate and the detector realization residual. `square`

### Proposition 6B: restricted finite-depth inverse control

Let `\|\cdot\|_{\nu}` be an anchored corridor norm of the type used in Paper 3,
adapted to mixed site-link collars and fixed center sector `b`. Suppose the
reference primitive is a finite-depth product of local gauge-compatible gates

```math
\Gamma_0^b
=
G_D^b\cdots G_1^b
```

on the tested block, and suppose each gate satisfies

```math
\|G_j^b-I\|_{\nu}\le\eta_j,
\qquad
0\le\eta_j<1.
```

Then each `G_j^b` is invertible on the anchored Banach space and

```math
\|(G_j^b)^{-1}\|_{\nu}
\le
\frac{1}{1-\eta_j}.
```

Consequently

```math
\|(\Gamma_0^b)^{-1}\|_{\nu}
\le
\prod_{j=1}^D\frac{1}{1-\eta_j}.
```

If the depth `D` and the numbers `\eta_j` are bounded independently of `L` and
`K`, this is a genuine volume- and cutoff-uniform inverse-control theorem for
that finite-depth benchmark class.

Proof. The Neumann series

```math
(G_j^b)^{-1}
=
\sum_{n\ge0}(I-G_j^b)^n
```

converges in the anchored norm whenever `\eta_j<1`, giving the displayed bound.
The inverse of a product is the reverse product of the inverses. Uniformity is
inherited exactly from fixed depth and uniform `\eta_j`. `square`

This proposition is intentionally restricted. It does not prove inverse control
for the full Hamiltonian slab `\Gamma_0^b(\Delta)=|e^{-i\Delta H_{L,K}}|^2` at
fixed physical `\Delta`. With `t_a=1/(2a)`, even a single hopping cell has
small-slab parameter roughly `\Delta^2/(4a^2)`. A Neumann proof around the
identity therefore requires `\Delta/a` small at the cell level or a different
renormalized inverse argument. This is the central remaining inverse-control
risk for Paper 5.

### Theorem 6D: two-state obstruction to full-slab inverse control

Unconditional uniform inverse control for the full Hamiltonian Born-squared slab

```math
\Gamma_0^b(\Delta)
=
\left|e^{-i\Delta H_{L,K}}\right|^2
```

cannot hold over arbitrary lattice refinements at fixed physical slab time
`\Delta>0`, even before taking large volume.

More precisely, consider the open chain with two sites and one admissible unit
charge in a fixed center sector. Let `c_L` and `c_R` be the two physical states
with the charge on the left or right site, with the link flux shifted according
to Gauss law. On this two-state sector the Hamiltonian has the form, up to an
irrelevant scalar,

```math
H_2(a)
=
\begin{pmatrix}
\delta_a/2 & -t_a\\
-t_a & -\delta_a/2
\end{pmatrix},
\qquad
t_a=\frac{1}{2a},
```

where `\delta_a` is the diagonal energy gap between the two configurations.
Set

```math
\Omega_a
:=
\sqrt{t_a^2+\frac{\delta_a^2}{4}},
\qquad
\lambda_a
:=
\frac{t_a^2}{\Omega_a^2}.
```

The full Born-squared slab restricted to this sector is

```math
\Gamma_2(a,\Delta)
=
\begin{pmatrix}
1-p_a & p_a\\
p_a & 1-p_a
\end{pmatrix},
\qquad
p_a
=
\lambda_a\sin^2(\Omega_a\Delta).
```

Therefore

```math
\det\Gamma_2(a,\Delta)
=
1-2p_a,
```

and every matrix norm that controls the inverse on this two-state sector obeys

```math
\|\Gamma_2(a,\Delta)^{-1}\|
\ge
\frac{1}{|1-2p_a|}.
```

If `|\delta_a|/t_a -> 0` as `a -> 0`, which holds for bounded local mass and
electric diagonal gaps on bounded-flux local states, then for every fixed
`\Delta>0` there are refinement sequences `a_n -> 0` for which

```math
|1-2p_{a_n}|\longrightarrow0.
```

Along such sequences, `\|\Gamma_2(a_n,\Delta)^{-1}\|` diverges. In the exactly
resonant case `\delta_a=0`, the slab is singular whenever

```math
\Omega_a\Delta
=
\frac{\pi}{4}+\frac{k\pi}{2},
\qquad
k\in\mathbb Z.
```

Consequently Paper 5 cannot claim cutoff- and volume-uniform inverse control
for the full Hamiltonian slab without an additional hypothesis, such as
microscopic small-step control, resonance avoidance, detector coarse-graining
that removes the bad mode, or a different renormalized inverse topology.

Proof. The two-state sector is invariant for the two-site open chain. The
displayed Hamiltonian is the standard two-level hopping Hamiltonian after
subtracting the average diagonal energy. Exponentiating it gives transition
probability

```math
p_a
=
\frac{t_a^2}{t_a^2+\delta_a^2/4}
\sin^2\!\left(\Delta\sqrt{t_a^2+\delta_a^2/4}\right).
```

Taking entrywise squared moduli gives the displayed stochastic matrix. Its
eigenvalues are `1` and `1-2p_a`, so the inverse norm is at least
`|1-2p_a|^{-1}` whenever the inverse exists. If `|\delta_a|/t_a -> 0`, then
`\lambda_a -> 1` and `\Omega_a\Delta -> \infty`. Choosing refinement values
with `\Omega_a\Delta` arbitrarily close to `\pi/4+k\pi/2` makes
`p_a -> 1/2`. The resonant formula is the special case `\lambda_a=1`. `square`

### Corollary 6E: viable inverse-control regimes after the obstruction

After Theorem 6D, the honest inverse-control targets are restricted alternatives:

1. **Microscopic small-step regime:** take slabs with `\Delta/a` small enough
   that the Neumann bound of Proposition 6B applies locally.
2. **Finite-depth circuit regime:** declare the primitive gauge dynamics as a
   bounded-depth product of calibrated local stochastic gates with uniform
   `\eta_j<1`.
3. **Resonance-avoiding full slabs:** impose an explicit lower bound

```math
\inf_{\alpha}
|1-2p_{\alpha}|
\ge
c_{\mathrm{res}}>0
```

on every two-state hopping channel in the tested class.
4. **Observable-subspace inverse control:** prove that the bad inverse mode is
   not seen by the preparation/effect/detector pairs used operationally.
5. **Renormalized inverse topology:** replace global matrix inverse control by
   a topology that weights or quotients the rapidly oscillating cell-scale modes.

Only items 1 and 2 are currently theorem-level in this paper. Items 3-5 are
research programs, not assumptions that may be silently imported.

### Proposition 6A: first open-chain center-resolved exchange coefficient

Work in the concrete Hamiltonian of Definition 1A, fix a boundary center `b`,
and assume the relevant states have no-truncation margin larger than `2` on the
two active links. For a bond `x`, let `\mathsf T_x^b` be the one-hop indicator
kernel on `C_{L,K}^{\mathrm{G}}(b)`:

```math
[\mathsf T_x^b]_{c',c}
=
1
```

iff `c'` is obtained from `c` by one admissible gauge hop across bond `x`, and
zero otherwise. Let

```math
[\mathsf D_x^b]_{c,c}
:=
\sum_{c'\ne c}[\mathsf T_x^b]_{c',c},
\qquad
\mathsf Q_x^b:=\mathsf D_x^b-\mathsf T_x^b.
```

For the gauge-compatible site-link block

```math
R_r:=(\{r\},\{r-1,r\}),
```

use the standard localized comparison deformation that deletes the hopping
cells incident on the block while leaving the diagonal mass and electric cells
unchanged. The comparison map then has the small-slab expansion

```math
J_{R_r}^b(\Delta)
=
I+\Delta^2A_{R_r}^{[2],b}+O(\Delta^4),
```

with

```math
A_{R_r}^{[2],b}
=
t_a^2(\mathsf Q_{r-1}^b+\mathsf Q_r^b)
=
\frac{1}{4a^2}(\mathsf Q_{r-1}^b+\mathsf Q_r^b).
```

For the disjoint pair `R_r` and `R_{r+2}`, the first coupled exchange coefficient
is

```math
E_{R_r,R_{r+2}}^b(\Delta)
=
I+\Delta^4 C_{r,r+2}^{b}+O(\Delta^6),
```

where

```math
C_{r,r+2}^{b}
=
t_a^4[\mathsf Q_r^b,\mathsf Q_{r+1}^b]
=
\frac{1}{16a^4}[\mathsf Q_r^b,\mathsf Q_{r+1}^b].
```

Thus the first nonzero coefficient lives on the mixed strip

```math
\Xi_{r,r+2}
:=
(\{r,r+1,r+2\},\{r,r+1\}).
```

More concretely, suppose `c` has a unit charge at site `r+2`, vacancies at
`r+1` and `r`, and fluxes `E_r(c),E_{r+1}(c)<K` so that the two leftward hops are
allowed. Let `c'` be obtained from `c` by moving that charge to site `r` and
raising both intervening link fluxes by one, as required by Gauss law in the
present sign convention. Then

```math
[C_{r,r+2}^{b}]_{c',c}
=
\frac{1}{16a^4},
\qquad
[C_{r,r+2}^{b}]_{c,c'}
=
-\frac{1}{16a^4}.
```

Proof. The order-`\Delta^2` off-diagonal coefficient of a Born-squared kernel
generated by a Hermitian Hamiltonian is the squared modulus of the corresponding
Hamiltonian matrix element. Each admissible hopping matrix element has modulus
`t_a=1/(2a)`. Deleting the hopping cells incident on `R_r` therefore contributes
`-t_a^2\mathsf T_x^b` off diagonal, while column normalization contributes
`+t_a^2\mathsf D_x^b` on the diagonal. Diagonal mass and electric terms do not
contribute to this order, giving the displayed formula for
`A_{R_r}^{[2],b}`.

The group commutator of two comparison maps whose first nontrivial terms are
order `\Delta^2` has leading coefficient
`[A_{R_r}^{[2],b},A_{R_{r+2}}^{[2],b}]`. All bond-kernel commutators vanish
except the facing pair on bonds `r` and `r+1`; hence the displayed formula for
`C_{r,r+2}^{b}`. For the representative entry, only one ordered product connects
`c` to `c'`: first hop from `r+2` to `r+1`, then from `r+1` to `r`. Each
off-diagonal `\mathsf Q` entry contributes `-1`, so the surviving ordered
product has coefficient `+t_a^4`. The reverse entry has the opposite sign by
antisymmetry of the commutator. `square`

This coefficient is center-resolved in the strict sense: the numeric coefficient
is universal for the minimal hopping benchmark, but whether the channel exists
depends on the center `b` through the Gauss-determined fluxes and the cutoff
admissibility inequalities. The Coulomb electric term affects higher-order
phase-sensitive coefficients and continuum scaling; it is not visible in this
first `\Delta^4` off-diagonal exchange entry.

### Theorem 6C: corridor onset and small-slab exchange tail

Let `R` and `S` be disjoint gauge-compatible mixed site-link regions in a fixed
open-chain center sector `b`. Define the mixed corridor

```math
W(R,S)
```

to be the smallest connected site-link interval containing the hopping cells
that can couple the right collar of `R` to the left collar of `S`. Let
`d_{\mathrm{hop}}(R,S)` be the minimum number of elementary gauge hops required
for an ordered hopping path to touch both localized comparison collars. For the
pair in Proposition 6A, `d_{\mathrm{hop}}=2`.

In the finite-depth small-slab expansion, write

```math
E_{R,S}^b(\Delta)
=
I+\sum_{n\ge d_{\mathrm{hop}}}
\Delta^{2n}C_{R,S}^{[2n],b}.
```

Then:

1. `C_{R,S}^{[2n],b}` is supported inside the `n`-hop enlargement of
   `W(R,S)`;
2. no coefficient of order below `2d_{\mathrm{hop}}` can contain a matrix entry
   whose transition touches both collars;
3. for every representative transition whose shortest admissible gauge-hop path
   has length `d`, the first possible coefficient has magnitude bounded by

```math
\left|[C_{R,S}^{[2d],b}]_{c',c}\right|
\le
N_d(R,S)\,t_a^{2d}
=
\frac{N_d(R,S)}{(4a^2)^d},
```

where `N_d(R,S)` is the number of admissible ordered shortest paths in the mixed
corridor.

Moreover, in one spatial dimension there is a constant `q_*` depending only on
the local hopping alphabet, not on total volume, such that `N_n(R,S)\le
C_{R,S}q_*^n`. With

```math
\theta:=\Delta^2t_a^2=\frac{\Delta^2}{4a^2},
```

the corridor tail obeys, for `q_*\theta<1`,

```math
\left\|
\sum_{n\ge d}
\Delta^{2n}C_{R,S}^{[2n],b}
\right\|_{\nu,W(R,S)}
\le
C_{R,S}\frac{(q_*\theta)^d}{1-q_*\theta}.
```

Proof. Every off-diagonal contribution to a Born-squared hopping coefficient
comes from ordered products of elementary gauge hops. A product with `n` hopping
factors can change only the variables in the `n`-hop mixed enlargement of the
active hopping cells, proving support. To touch both collars, an ordered product
must include at least a shortest connecting gauge-hop path, giving the onset
bound. Each elementary hopping contribution has squared modulus `t_a^2`; a
length-`d` ordered path therefore contributes at most `t_a^{2d}` in magnitude,
and summing shortest admissible paths gives the coefficient bound. In one
dimension the number of ordered local hopping words of length `n` in a fixed
corridor grows at most exponentially with a local alphabet constant `q_*`.
Summing the resulting geometric majorant gives the tail estimate. `square`

The theorem is deliberately a corridor estimate, not a full continuum exchange
law. It says what survives from Proposition 6A at the next level: exchange
curvature is forced to live in the mixed matter-link corridor, and separated
supports have an explicit onset/tail budget in the small-slab parameter.

### Theorem 6F: renormalized exchange corridor law

Choose a microscopic slab scaling

```math
\Delta(a)=\kappa a,
\qquad
0<\kappa<\frac{2}{\sqrt{q_*}},
```

where `q_*` is the corridor word-growth constant of Theorem 6C. Then

```math
\theta=\Delta(a)^2t_a^2=\frac{\kappa^2}{4},
\qquad
q_*\theta<1,
```

and the corridor tail estimate is uniform in the lattice spacing `a`.

For the adjacent two-bond corridor of Proposition 6A, define the renormalized
contact exchange channel

```math
\mathcal K_{r}^{b,\kappa}(a)
:=
\kappa^{-4}\,
\Pi_{\Xi_{r,r+2}}
\bigl(E_{R_r,R_{r+2}}^b(\kappa a)-I\bigr)
\Pi_{\Xi_{r,r+2}},
```

where `\Pi_{\Xi_{r,r+2}}` restricts to the minimal mixed strip. Then

```math
\mathcal K_{r}^{b,\kappa}(a)
=
\frac{1}{16}
[\mathsf Q_r^b,\mathsf Q_{r+1}^b]
+
O(\kappa^2)
```

in the anchored finite-strip norm, uniformly on no-cutoff center sectors. In
particular, the representative channel of Proposition 6A has renormalized
coefficient

```math
\frac{1}{16}+O(\kappa^2).
```

For regions whose physical separation is bounded below by `\rho>0`, the hop
distance satisfies `d_{\mathrm{hop}}(R,S)\ge c\rho/a` for a geometry constant
`c>0`. Hence

```math
\left\|
E_{R,S}^b(\kappa a)-I
\right\|_{\nu,W(R,S)}
\le
C_{R,S}
\frac{(q_*\kappa^2/4)^{c\rho/a}}
{1-q_*\kappa^2/4}
\longrightarrow0.
```

Thus the continuum corridor law has a sharp alternative:

1. microscopic contact corridors have a finite nonzero renormalized exchange
   channel;
2. positive physical separation gives vanishing exchange in the small-step
   continuum limit.

Proof. Substitute `\Delta=\kappa a` and `t_a=1/(2a)` in Proposition 6A:

```math
\Delta^4 C_{r,r+2}^{b}
=
\kappa^4a^4
\frac{1}{16a^4}
[\mathsf Q_r^b,\mathsf Q_{r+1}^b]
=
\frac{\kappa^4}{16}
[\mathsf Q_r^b,\mathsf Q_{r+1}^b].
```

After dividing by `\kappa^4`, the leading strip channel is `1/16` times the
commutator. The next exchange terms are higher order in the small parameter
`\theta=\kappa^2/4`, giving the `O(\kappa^2)` remainder in the finite-strip
anchored norm. For separated supports, Theorem 6C gives a geometric corridor
tail with ratio `q_*\theta=q_*\kappa^2/4<1`; the hop distance grows like
physical separation divided by `a`, so the bound tends to zero exponentially in
`1/a`. `square`

This is the first renormalized exchange law Paper 5 can honestly state. It is a
contact/corridor law, not yet a continuum gauge-field curvature operator on a
Haag-Kastler net. The theorem says which finite exchange data survive the
continuum scaling and which are forced to disappear by locality.

## 11. The Compact-Rotor Obstruction

The finite truncation `E\in[-K,K]` is not the compact rotor. The compact rotor
has infinite electric spectrum. On a periodic lattice, Gauss law can leave an
infinite global electric-flux tower even after local charges are fixed.

The first honest compact-rotor target is therefore not:

```text
replace K by infinity everywhere and assume finite-matrix proofs survive.
```

It is:

```text
prove local cylinder statistics are stable as K -> infinity in a center-resolved
finite-energy or no-truncation regime.
```

Paper 5 should treat the following as separate gates:

1. **Fixed volume, `K -> infinity`:** compact-rotor cutoff stability.
2. **Fixed physical size, `a -> 0`:** continuum scaling.
3. **Thermodynamic or large-volume limit:** boundary-center and energy-density
   control.
4. **Operational detector limit:** projective record stability and screening.

### Theorem 7: fixed-volume compact-rotor local stability

Fix `a>0`, `L<\infty`, a finite physical interval, and the open-chain
Hamiltonian of Definition 1A with rotor electric spectrum
`E_\ell\in\mathbb Z`. Let `O_A^{\mathrm{rot}}` be either:

1. a finite string of local bond and diagonal gates with total flux shift radius
   `r`, or
2. the full finite-volume open-chain Hamiltonian slab restricted to a fixed
   boundary center sector `b`.

For case 1, if a normalized rotor preparation has finite local electric energy
on the active links, then the finite cutoff statistic converges:

```math
\lim_{K\to\infty}
\sup_{0\le e\le1}
\left|
e^T(O_A^K-O_A^{\mathrm{rot}})p
\right|
=0.
```

For case 2, if the center sector `b` is fixed, then for every finite support set
`S` there is a finite `K_0(S,b)` such that for all `K\ge K_0(S,b)`,

```math
e^{-i\Delta H_{L,K}}\psi
=
e^{-i\Delta H_L^{\mathrm{rot}}}\psi
```

for every Hilbert vector `\psi` supported in `S`. Hence the associated
Born-squared finite-cutoff kernel agrees exactly with the rotor kernel on that
support. For center mixtures, the same conclusion holds up to the tail
probability of the boundary-center distribution.

Proof. Case 1 is Lemma 3B with fixed `a,L,r`; the denominator grows like
`(K-r)^2`, so the cutoff-boundary mass goes to zero. In case 2, fixed `L` and
fixed `b` leave only finitely many matter configurations, and Gauss law
determines finitely many possible link-flux profiles from any finite support
set. Choose `K_0` larger than all fluxes in the Hamiltonian reachable hull. Then
Corollary 3A gives exact equality. If `b` is not fixed, decompose into center
sectors; finite electric-energy or tight-center hypotheses make the omitted
large-`|b|` sector mass arbitrarily small. `square`

This is the compact-rotor result Paper 5 can honestly claim now. It is
fixed-volume/local-statistic stability. It is not yet a growing-volume
compact-rotor inverse theorem, and it is not a continuum QFT reconstruction.

### Definition 7A: growing-volume local rotor class

Fix a compact physical interval `I` and let `A_a(I)` be its mixed detector or
operation collar. A family of finite-volume compact-rotor preparations
`p_{a,L}^{\mathrm{rot}}` is locally admissible on `I` if:

1. the finite volumes exhaust the line while containing `A_a(I)`;
2. the local center `c_A` is tight uniformly in `L`:

```math
\lim_{B\to\infty}
\sup_{a,L}
p_{a,L}^{\mathrm{rot}}(|c_A|>B)=0;
```

3. the local electric energy is uniformly bounded:

```math
\sup_{a,L}
\mathcal E_{A_a(I)}(p_{a,L}^{\mathrm{rot}})
\le E_I<\infty;
```

4. the rotor local statistics of the tested operation/effect pair have a
   growing-volume local limit:

```math
S_{I}^{a,\mathrm{rot},\infty}
:=
\lim_{L\to\infty}
e_a^TO_{A_a}^{\mathrm{rot}}p_{a,L}^{\mathrm{rot}}
```

exists for each fixed `a`.

The fourth item is the genuine compact-rotor thermodynamic input. The first
three items are local tightness hypotheses supplied by the ISP gauge estimates.

### Theorem 7B: growing-volume compact-rotor cutoff transfer

Let `p_{a,L}^{\mathrm{rot}}` be locally admissible on `I` in the sense of
Definition 7A, assume the charge alphabet is bounded by `Q_*`, and let the
tested operation have flux shift radius at most `r_*`. Let `p_{a,L,K}` be the
finite-cutoff truncation of `p_{a,L}^{\mathrm{rot}}`, normalized on the event
that the active collar lies inside `[-K,K]`. Write

```math
\varepsilon_{0,K}(a)
:=
\sup_L
p_{a,L}^{\mathrm{rot}}
\left(\max_{\ell\in A_a^\ell(I)}|E_\ell|>K\right).
```

Then, for every `B` with `K-r_*-B>4Q_*` and
`\varepsilon_{0,K}(a)<1`,

```math
\limsup_{L\to\infty}
\sup_{0\le e_a\le1}
\left|
e_a^TO_{A_a}^{K}p_{a,L,K}
-
e_a^TO_{A_a}^{\mathrm{rot}}p_{a,L}^{\mathrm{rot}}
\right|
\le
2\sup_Lp_{a,L}^{\mathrm{rot}}(|c_A|>B)
+
\frac{64Q_*E_I}
{g^2a(K-r_*-B)^3}
+
\frac{2\varepsilon_{0,K}(a)}
{1-\varepsilon_{0,K}(a)},
```

where the final term is the total-variation cost of normalizing the active
finite-cutoff truncation. By Theorem 5G with `r_*=0`,
`\varepsilon_{0,K}(a)` vanishes under the same tight-center cubic cutoff
scaling. Consequently, if the centers are uniformly tight and

```math
a(K(a,L)-r_*-B)^3\longrightarrow\infty
```

after choosing `B` large, then the finite-cutoff growing-volume statistic has
the same local limit as the compact-rotor statistic:

```math
\lim_{a\to0}
\lim_{L\to\infty}
e_a^TO_{A_a}^{K(a,L)}p_{a,L,K(a,L)}
=
\lim_{a\to0}
S_{I}^{a,\mathrm{rot},\infty},
```

whenever the limit on the right exists.

Proof. Theorem 5G bounds the active-collar cutoff event uniformly in total
volume because it uses only `c_A`, the bounded charge alphabet, and the local
energy on `A_a(I)`. The stochastic output of the finite-cutoff operation and
the rotor operation agree on the complement of that cutoff event. Pairing with
`0\le e_a\le1` gives twice the bad-event probability, and truncation
normalization changes a probability measure by at most
`2\varepsilon_{0,K}/(1-\varepsilon_{0,K})` in total variation. Taking
`L -> infinity` does not change the estimate, since no term depends on exterior
volume except through the assumed center-tail and local-energy bounds. The final
statement is the triangle inequality between finite cutoff, finite-volume rotor,
and the assumed growing-volume rotor limit. `square`

Theorem 7B is the strongest compact-rotor statement earned here: growing volume
is allowed for local operational statistics, but the existence of the rotor
thermodynamic/local limit remains an input. The theorem transfers that limit to
the finite-cutoff ISP benchmark under explicit local tightness hypotheses.

If any gate fails, the finite gauge benchmark remains useful but is not a
continuum gauge theory.

## 12. Pass/Fail Ledger

Paper 5 passes at theorem-framework level if it proves:

1. exact finite Gauss-sector preservation for the chosen benchmark;
2. a center-resolved projective family of gauge configurations and instruments;
3. a no-truncation or cutoff-stability theorem with explicit `K` scaling;
4. at least one nontrivial local cylinder statistic with a controlled
   continuum-facing limit;
5. a clear operational exchange or locality theorem inside fixed center sectors;
6. a failure theorem or obstruction if compact-rotor or volume stability cannot
   be obtained.

After the present pass, items 1, 2, 3, and the local-statistic half of item 4
are in place at theorem-framework level. Theorem 5E and Corollary 5F now give a
concrete continuum limit for the clipped electric-energy statistic on a narrow
but nonempty class of center-resolved preparations. Item 5 is established for
finite-depth inverse-controlled tests, the explicit detector protocol, and the
renormalized corridor exchange law. Theorem 6D shows that unconditional full
Hamiltonian slab inverse control is not available across arbitrary refinements;
any full-slab version must add resonance avoidance, observable-subspace control,
or a renormalized inverse topology. Item 6 is partially resolved by Theorem 7
and Theorem 7B: fixed-volume compact-rotor stability and growing-volume
compact-rotor cutoff transfer hold for local statistics, while growing-volume
compact-rotor inverse control remains open.

Paper 5 fails as a continuum benchmark if:

1. `K` must grow uncontrollably with volume for all relevant local statistics;
2. boundary centers cannot be projectively controlled;
3. comparison-map inverses delocalize in gauge sectors;
4. matter-only operational statistics depend on hidden center mixtures;
5. detector records do not refine in the gauge benchmark;
6. the only way to recover gauge QFT is to add standard Hilbert-space local
   algebras as primitive.

## 13. Remaining Gaps And Open Inputs

The paper now has a coherent open-chain theorem package. The remaining gaps are
not cosmetic; each marks a boundary where a stronger physics claim would require
new work.

### Gap 1: physical flux-tail estimates

The cutoff results are currently driven by finite local electric energy, tight
local centers, bounded charge alphabet, and deterministic-profile examples.
This is enough for Main Theorem M, but it is not yet a physical state theorem.
The next step is to prove model-specific flux-tail estimates for natural rotor
state families, such as finite-temperature, ground-state, low-density, or
finite-energy-density preparations:

```math
p(B_{K,r_*}(A))\le\tau_A(K-r_*),
\qquad
\tau_A(u)\to0.
```

Such a result would replace the generic Markov/Gauss-slope cutoff estimates by
a sharper physical tail law.

### Gap 2: replacement for full-slab inverse control

Theorem 6D rules out unconditional full Hamiltonian slab inverse control across
arbitrary refinements. Paper 5 therefore cannot use

```math
\Gamma_0^b(\Delta)^{-1}
```

as a regulator-uniform object without extra structure. One of the following
must be developed before claiming a full Hamiltonian exchange theorem:

1. resonance avoidance for the tested slab sequence;
2. observable-subspace inverse control showing the bad mode is operationally
   invisible;
3. a renormalized inverse topology that quotients or weights cell-scale
   oscillatory modes;
4. a finite-depth circuit primitive replacing the full slab as the operational
   gauge dynamics.

### Gap 3: fluctuating continuum preparations

The clipped local electric-energy statistic has a proved continuum limit on
deterministic electric profiles and finite mixtures. A physically stronger
version should allow charge and flux fluctuations. A possible target is a
family `p_a` whose local electric profile laws converge weakly to a probability
law `\mu_I` on `L^2(I)` with uniform integrability of
`\int_I e(x)^2dx`. Then the expected limit should be

```math
\int
\min\left\{
1,
\frac{g^2}{2M}\int_I e(x)^2dx
\right\}
d\mu_I(e).
```

This is not proved here.

### Gap 4: continuum meaning of the contact exchange channel

Theorem 6F proves a renormalized contact mixed-corridor law:

```math
\frac{1}{16}[\mathsf Q_r^b,\mathsf Q_{r+1}^b]+O(\kappa^2).
```

What remains open is whether this contact channel has a canonical continuum
operator interpretation, or whether it remains a regulator-local stochastic
curvature coefficient. This is the main conceptual export question for later
papers.

### Gap 5: compact-rotor local thermodynamic limit

Theorem 7B transfers a compact-rotor growing-volume local limit to the
finite-cutoff ISP benchmark, but it does not prove that rotor local limit. A
complete gauge-continuum theorem needs a concrete state family for which

```math
\lim_{L\to\infty}
e_a^TO_{A_a}^{\mathrm{rot}}p_{a,L}^{\mathrm{rot}}
```

exists and is compatible with `a -> 0`.

### Gap 6: physical detector hardware model

Protocol 4D gives an exact mathematical readout and Theorem 4E handles a
classical confusion channel. A physical detector model should derive that
confusion channel from an explicit finite apparatus or coarse-grained record
process, rather than taking it as a declared stochastic post-processing map.

### Gap 7: periodic and non-Abelian gauge theory

The periodic compact `U(1)` ring has a global electric-flux tower that the
open-chain theorem deliberately avoids. Non-Abelian gauge theory adds local
representation labels, noncommuting constraints, and more complicated center
data. Both are deferred until the open-chain compact Abelian package is stable.

## 14. Paper 5 Export Box

Paper 5 may export to Paper 6 only the following, if proved:

1. center-resolved projective gauge-sector states;
2. cutoff-stable local gauge operational statistics;
3. gauge-compatible detector instruments with refinement residuals;
4. center-resolved operational exchange bounds;
5. a precise compact-rotor obstruction or theorem.

It may not export:

1. full local QFT reconstruction;
2. non-Abelian gauge theory;
3. continuum compact `U(1)` without a `K -> infinity` theorem;
4. matter-only locality that ignores boundary centers;
5. raw exchange defects as observables.

## 15. Summary

Paper 5 is the first serious gauge-continuum viability gate for relativistic
ISP. Its conceptual point is simple: gauge theory is not just another local
finite example. It forces the theory to handle constraints, centers, cutoff
limits, inverse-control failure modes, compact-rotor tails, and operational
readouts at the same time.

The conservative starting thesis is:

```text
Relativistic ISP can claim a continuum gauge benchmark only if finite
Gauss-sector kernels, center-resolved projective maps, cutoff-stable local
statistics, and Paper-4 detector instruments all converge together.
```

Main Theorem M is the current honest version of that claim for an open-chain
compact Abelian benchmark. It proves local statistic transfer and a
renormalized contact exchange law under explicit tightness, cutoff, detector,
rotor-limit, and inverse-control hypotheses, while Theorem 6D prevents the
paper from overclaiming full Hamiltonian slab inverse control. The remaining
gaps are now sharply localized: physical flux tails, a replacement inverse
topology, fluctuating state limits, contact-channel interpretation, a concrete
rotor thermodynamic limit, detector hardware, and periodic/non-Abelian gauge
extensions.
