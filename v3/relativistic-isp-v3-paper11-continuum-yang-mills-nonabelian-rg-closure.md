# Relativistic ISP V3 Paper 11: Finite-Battery Non-Abelian RG Closure Toward Continuum Yang-Mills

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: continuum-RG investigation draft. This paper takes the finite-battery
non-Abelian cutoff and local-RG machinery of Paper 10 and asks whether it can
be pushed into a genuine continuum-facing Yang-Mills scaling window.

This paper does not assume that finite projective gauge control already proves
continuum Yang-Mills. The central distinction is:

```text
perfect blocking:
  exact finite-battery whole-process pushforward, generally nonlocal;

local Yang-Mills/Wilson blocking:
  approximate replacement of the perfect block by a local gauge-invariant
  ansatz, controlled only if explicit residuals vanish in the scaling limit.
```

The Barandes-aligned rule remains: do not compose undeclared subprocesses as
if the whole process were Markov divisible; do not derive charged gauge data
from scalar Gamma-only records; and do not hide spin, representation,
instrument, or determinant data.

After the Paper-10 projective-continuum audit, Paper 11 is also not allowed to
treat exact finite perfect-block pushforward as an already constructed
continuum tower. It may use the perfect block as a same-record finite
reference and then must prove, assume, or explicitly park each local-action,
tightness, uniqueness, nontriviality, and loop-continuity gate.

## 1. Import Contract From Paper 10

Paper 11 may use the following theorem-level or named conditional structures
from Paper 10.

1. A finite `SU(2)` Peter-Weyl gauge battery over compact link endpoint
   space.
2. Haar gauge projection, finite Gauss sectors, and boundary representation
   centers.
3. Representation-cutoff and lattice-coarsening projective maps.
4. Heat-bath reference-kernel inverse control on every finite battery.
5. Conditional comparison-map and exchange-defect transfer under PC/KCOMP.
6. A smooth-background charged plaquette target
   `a^{-2}(\rho(U_P)-I)\to d\rho(F_{\mu\nu})`.
7. Exact two-dimensional heat-kernel blocking.
8. Exact finite-battery perfect blocking in any dimension.
9. A local-action residual
   `\delta_{\rm locRG}^{\mathcal F}` measuring the gap between the exact
   perfect block and a chosen local ansatz.
10. A response-rank/local-projection theorem bounding that residual on finite
    batteries.
11. Tiny-battery closure tests: scalar loops close under covariance rank;
    charged curvature requires charged instruments; Wilson matter requires
    matter operators; no-Wilson detail labels remain typed branch data.
12. A Gamma-only no-go theorem for full charged gauge reconstruction.

Paper 11 may not use Paper 10 to claim:

```text
continuum Yang-Mills;
QCD;
mass gap;
Wilson-loop area law;
confinement;
OS/Wightman reconstruction;
Gamma-only charged gauge reconstruction;
unconditional higher-dimensional local RG;
an unconditional same-record continuum tower.
```

## 1A. RG Closure Audit For Paper 20

Paper 20 needs more than the Paper-11 continuum-facing RG scaffold. In
particular, the strict SEL2 surface route needs an actual coefficient source
for the same pushed-forward record law, not merely a positive symbol in a
local-RG ledger.

### Definition 1A.1: Paper-20 Tree-Rate Source Data

For the active SEL2 scalar block record, Paper 20 needs all of the following
on one common record law.

1. A central block-plaquette coefficient
   ```math
   \widetilde a_{\rho,j}^{\rm SEL2}
   =
   {1\over d_\rho}
   \int \chi_\rho(U)\,K_{p,j}^{\rm SEL2}(U)\,dU
   ```
   or an equivalent normalized coefficient, with the normalization fixed
   before comparison.
2. Cofinal positivity and subunitarity:
   ```math
   0<\widetilde a_{\rho,j}^{\rm SEL2}<1.
   ```
3. A positive rate:
   ```math
   \widetilde\kappa_\rho^{\rm SEL2}
   =
   \liminf_j -\log \widetilde a_{\rho,j}^{\rm SEL2}>0.
   ```
4. A coefficient-time comparison, if the rate is sourced through a heat-kernel
   proxy:
   ```math
   \widetilde a_{\rho,j}^{\rm SEL2}
   =
   \exp\left(-{1\over2}C_2(\rho)T_j^{\rm SEL2}\right)
   +\varepsilon_{\rho,j},
   ```
   with a lower bound
   ```math
   T_-^{\rm SEL2}
   :=
   \liminf_j T_j^{\rm SEL2}
   ```
   and an error `\varepsilon_{\rho,j}` small enough not to destroy the
   rate gate.
5. A heat-kernel comparison residual on the same record:
   local projection, chart, counterterm, volume, collar, and tail errors must
   be charged in the same scalar coefficient ledger and may not be imported
   from a smeared Wilson-loop anchor.

This is the source content behind the Paper-20 gate
`P20-SEL2-TREE-RATE-GATE`.

### Theorem 1A.2: Paper 11 Does Not Supply `P20-SEL2-TREE-RATE-GATE`

Paper 11 does not prove `P20-SEL2-TREE-RATE-GATE`. It supplies conditional RG
residual summability, perturbative trajectory tracking, and a smeared
Wilson-loop nontriviality anchor. These are not the same as the SEL2
block-plaquette coefficient-time lower bound required by Paper 20.

### Proof

The strong-coupling route gives a genuine heat-kernel character smallness
regime at sufficiently large heat time for fixed finite block depth. But
Theorem SC.9 below states that this Haar-background character KP margin does
not continue unchanged to the asymptotically-free continuum trajectory, where
the microscopic heat time tends toward the weak-coupling direction.

The AF route replaces strong-coupling KP by local weak-coupling residual
summability. Theorems AF.28--AF.32 track the perturbative inverse-coupling
ledger and preserve a smeared Wilson-loop anchor in a weak-coupling reference
window. They do not compute the raw or normalized SEL2 block-plaquette central
character coefficient, do not prove a cofinal lower bound for
`T_j^{\rm SEL2}`, and do not compare that coefficient to a heat kernel with
summable same-record errors.

Therefore Paper 11 can feed Paper 20 only as a conditional residual and
trajectory ledger. The actual coefficient-time/rate source must be proved in
Paper 20 or a later source paper. `square`

### Corollary 1A.3: Allowed And Forbidden Paper-20 Imports

Paper 20 may import from Paper 11:

```text
CYM-RG residual bookkeeping;
strong/subsequential distinction;
local-action residual definitions;
one-block AF locality-margin form;
conditional multiscale summability;
perturbative inverse-coupling trajectory ledger;
smeared Wilson-loop anchor as a nontriviality benchmark.
```

Paper 20 may not import from Paper 11:

```text
T_-^{SEL2}>0 for the actual SEL2 block coefficient;
the SEL2 heat-kernel coefficient comparison;
P20-SEL2-TREE-RATE-GATE;
Wilson-loop area law;
mass gap;
confinement;
unsmeared Wilson-loop source constants.
```

## 2. Nested Test Batteries

Let `K_a` be a finite four-dimensional hypercubic lattice approximating either
a fixed physical box or a finite-volume torus. Let `G=SU(2)`. A refinement net
has

```math
a\downarrow0,\qquad
J(a)\uparrow\infty,
```

where `J(a)` is the Peter-Weyl representation cutoff.

For each integer `n`, choose finite parameters:

```math
L_n,\ R_n,\ q_n,\ j_n,\ s_n,
```

where `L_n` bounds lattice loop length, `R_n` bounds physical diameter,
`q_n` bounds product degree, `j_n` bounds tested representations, and `s_n`
bounds the number of charged/matter sources.

### Definition 2.1: Scalar Loop Battery

The scalar battery `{\mathcal F}^{\rm sc}_n(a)` is the finite real span of
products of at most `q_n` records

```math
W_\rho(C_a)
=
{\rm Re}\,{\rm tr}_\rho\left(\prod_{e\in C_a}U_e\right),
```

where:

1. `C_a` is a lattice loop with length at most `L_n` and physical diameter at
   most `R_n`;
2. `\rho` has spin `j\le j_n`;
3. loops related by exact lattice symmetries or exact trace identities are
   represented once in a quotient basis.

### Definition 2.2: Charged Curvature Battery

The charged battery `{\mathcal F}^{\rm ch}_n(a)` is generated by
`{\mathcal F}^{\rm sc}_n(a)` and finitely many framed records

```math
\Phi_{P,\rho,u,v}^{\rm tr}
=
a^{-2}
\left\langle u,
\left(\rho(U_P)-\frac{\chi_\rho(U_P)}{d_\rho}I\right)v
\right\rangle,
```

where `P` is a plaquette or clover plaquette in the declared region and
`u,v` are source/sink frame vectors in `V_\rho`.

These records are not scalar Gamma records. They are declared charged
instruments.

### Definition 2.3: Wilson Matter Battery

The Wilson matter battery `{\mathcal F}^{\rm W}_n(a)` is generated by
`{\mathcal F}^{\rm ch}_n(a)` and finitely many Wilson-Dirac source
contractions

```math
S_\ell(U)
=
\langle \eta_\ell,(D_W[U]+M)^{-1}\xi_\ell\rangle,
```

on a declared invertible or infrared-regularized finite Wilson-Dirac domain,
together with gauge-invariant bilinears and optional determinant/reweighting
records whose sign or phase prescription is explicitly declared.

### Definition 2.4: Detail-Preserving Battery

The no-Wilson detail-preserving battery `{\mathcal F}^{\rm det}_n(a)` is
generated by `{\mathcal F}^{\rm ch}_n(a)` and declared taste/detail records.
The detail labels are operational records. They may be projected, averaged, or
rejected only by a declared instrument with recorded outcomes.

### Definition 2.5: Nested Battery Family

The Paper-11 battery family is any nested sequence

```math
{\mathcal F}_1(a)\subset{\mathcal F}_2(a)\subset\cdots
```

chosen from the four types above, with parameters increasing so that every
fixed smooth Wilson-loop test and every declared finite charged/matter test is
eventually represented along the refinement net.

## 3. Nested Local Operator Bases

Let `{\mathcal A}_k(a)` be a finite set of bounded local gauge-invariant
operators on `K_a`. The bases are nested:

```math
{\mathcal A}_k(a)\subset{\mathcal A}_{k+1}(a).
```

The conservative pure-gauge basis contains:

1. plaquette character or heat-kernel terms;
2. rectangle Wilson-loop terms;
3. chair/parallelogram terms;
4. larger local Wilson-loop terms with bounded physical diameter;
5. clover curvature terms paired with charged source/sink frames when charged
   records are included;
6. symmetry-allowed improvement terms.

The Wilson matter extension contains:

1. Wilson mass and hopping counterterms;
2. gauge-invariant source terms for declared source contractions;
3. determinant or reweighting terms when a dynamical prescription is declared.

The no-Wilson extension contains taste/detail local terms only when those
records are part of the declared branch.

Given a finite basis `A_1,\ldots,A_p`, define the local ansatz

```math
d\mu^{\rm loc}_{a,k,\theta}
=
\frac{\exp(\sum_{\alpha=1}^p\theta_\alpha A_\alpha)}
{Z_{a,k}(\theta)}
d\nu_a,
```

where `\nu_a` is a positive reference measure, usually the heat-kernel gauge
measure restricted to the declared finite battery. If a determinant phase is
complex or sign-changing, it is not hidden in `d\mu^{\rm loc}`; it is treated
as a declared reweighting record.

## 4. Finite-Step Monotonicity

Let `\mu_b^{\rm perf}` be the exact perfect block from a fine lattice to a
coarse lattice, restricted to a finite battery `{\mathcal F}_n(b)`. Define

```math
\delta_{n,k}(a,b)
=
\inf_{\theta\in\Theta_{k}}
\sup_{\|F\|_{{\mathcal F}_n}\le1}
\left|
\mu_b^{\rm perf}(F)-\mu^{\rm loc}_{b,k,\theta}(F)
\right|.
```

### Theorem 4.1: Monotonicity Under Ansatz Enlargement

If `{\mathcal A}_k\subset{\mathcal A}_{k+1}` and the parameter domain
`\Theta_k` embeds in `\Theta_{k+1}` by setting the new couplings to zero, then

```math
\delta_{n,k+1}(a,b)\le\delta_{n,k}(a,b)
```

for every fixed finite battery `{\mathcal F}_n`.

### Proof

The infimum defining `\delta_{n,k+1}` is taken over a set of local ansatz
states containing the `k`-th ansatz family as a subset. Taking an infimum over
a larger set cannot increase the value. `square`

### Corollary 4.2: Existence Of A Finite-Battery Closure Limit

For fixed `n,a,b`, the monotone limit

```math
\delta_{n,\infty}(a,b)
=
\lim_{k\to\infty}\delta_{n,k}(a,b)
```

exists.

### Proof

The residuals are nonnegative and monotone nonincreasing in `k`. Therefore
they have an infimum, equal to the displayed limit. `square`

## 5. Closure/Obstruction Dichotomy

### Definition 5.1: Local Closure And Stable Obstruction

For a fixed finite battery, local closure at scale step `a\to b` means

```math
\delta_{n,\infty}(a,b)=0
```

after quotienting exact battery redundancies and declaring all allowed branch
records.

A stable obstruction means

```math
\delta_{n,\infty}(a,b)>0,
```

or that every operator needed to reduce the residual falls outside the
declared allowed class: nonlocal, gauge-noncovariant, reflection-positivity
violating, untyped charged, or forbidden by the branch ontology.

### Theorem 5.2: Finite-Battery Closure/Obstruction Dichotomy

For every fixed finite battery and fixed scale step, exactly one of the
following holds:

1. the local ansatz family closes the battery, so `\delta_{n,\infty}=0`;
2. a stable residual remains, so `\delta_{n,\infty}>0`;
3. the residual can be reduced only by leaving the declared operator class,
   in which case the obstruction is typed by the first forbidden direction.

### Proof

By Corollary 4.2 the nonnegative residual sequence has a limit. If the limit
is zero, closure holds. If the limit is positive while the operator class is
exhausted, a stable residual remains. If the only way to reduce the residual
requires a nonlocal, noncovariant, reflection-positivity violating, or untyped
operator, then closure in the declared class fails by definition and the
first such direction gives the typed obstruction. `square`

### Obstruction Classes

The obstruction is reported as one of:

1. **truncation artifact:** removed by a larger symmetry-allowed local basis;
2. **charged enrichment:** removed only by declared charged instruments;
3. **matter enrichment:** removed only by Wilson matter source/counterterms or
   determinant/reweighting records;
4. **detail retained record:** no-Wilson taste/detail data remain visible;
5. **nonlocal perfect-block residue:** no local symmetry-allowed basis spans
   the direction;
6. **positivity/sign obstruction:** the needed prescription violates the
   positivity required for the target continuum interface.

## 6. Sharp Scaling Window Hypothesis

Paper 10 used `YM-LIM` as a high-level gate. Paper 11 refines it.

### Hypothesis CYM-RG: Continuum Yang-Mills RG Closure Window

There exist choices

```math
n=n(a),\qquad k=k(a),\qquad J=J(a),\qquad
\theta=\theta(a),
```

and a finite-volume or thermodynamic-volume prescription such that, for every
fixed target test eventually included in `{\mathcal F}_{n(a)}(a)`,

```math
\delta_{n(a),k(a)}(a,ba)
+\epsilon_{\rm tail}(a)
+\epsilon_{\rm proj}(a)
+\epsilon_{\rm OS}(a)
+\epsilon_{\rm Euc}(a)
\longrightarrow0.
```

Here:

1. `\delta_{n,k}` is the local-action residual against the perfect block;
2. `\epsilon_{\rm tail}` is the error from tests or local operators not yet
   included in the finite battery/basis;
3. `\epsilon_{\rm proj}` is the Peter-Weyl and lattice projectivity residual;
4. `\epsilon_{\rm OS}` measures reflection-positivity defect on the tested
   finite family;
5. `\epsilon_{\rm Euc}` measures Euclidean covariance defect on the tested
   finite family.

### Lemma 6.1: Paper-10 Residuals Are Subsumed By CYM-RG

If Hypothesis CYM-RG holds for a battery containing the Paper-10 finite tests,
then the Paper-10 PC/KCOMP/RG-D residual gates vanish on those tests.

### Proof

The local-action residual bounds the deviation between the perfect block and
the declared local ansatz. The projectivity term controls representation and
lattice cutoff loss. The tail term is zero on tests already included in the
finite battery. Thus the primitive and comparison-map residual estimates of
Paper 10 receive vanishing inputs. `square`

### Definition 6.2: Strong And Subsequential CYM-RG

There are two useful strengths of the scaling gate.

**Subsequential CYM-RG** means that the CYM-RG residual ledger tends to zero
along at least one refinement subsequence

```math
a_r\downarrow0.
```

**Strong CYM-RG** means that the residual ledger tends to zero along the full
declared refinement path and the bounded Wilson-loop test expectations have a
unique subsequential limit on the declared countable tested class.

Subsequential CYM-RG is enough for a subsequential Wilson-loop interface.
Strong CYM-RG is the appropriate residual condition for a path-independent
continuum functional, once nontriviality and loop-topology continuity are also
established.

### Definition 6.3: Local Expansion Tail

Fix a coarse scale and a finite battery. Suppose the perfect block is
absolutely continuous with respect to the local reference measure `\nu_b` and
has a bounded log-density

```math
d\mu_b^{\rm perf}
=
\frac{e^{H_b^{\rm perf}}}{\nu_b(e^{H_b^{\rm perf}})}d\nu_b.
```

Let the local ansatz basis provide a truncated log-density `H_{b,k}`. The
uniform local expansion tail is

```math
\eta_{b,k}
=
\|H_b^{\rm perf}-H_{b,k}\|_\infty.
```

When the perfect block admits a polymer or local-loop expansion

```math
H_b^{\rm perf}
=
\sum_X c_X A_X,
```

and `H_{b,k}` keeps the declared local terms, a sufficient bound is

```math
\eta_{b,k}
\le
\sum_{X\notin{\mathcal A}_k}|c_X|\,\|A_X\|_\infty.
```

This is where the hard gauge-theory analysis lives: proving a summable local
expansion tail for four-dimensional non-Abelian blocks is not automatic.

### Theorem 6.4: Local Expansion Tail Implies Residual Decay

If `\eta_{b,k}<\infty`, then for every bounded battery with `\|F\|_\infty\le1`,

```math
\left|
\mu_b^{\rm perf}(F)-\mu^{\rm loc}_{b,k}(F)
\right|
\le
e^{2\eta_{b,k}}-1.
```

Consequently,

```math
\delta_{n,k}(a,b)
\le
e^{2\eta_{b,k}}-1
```

for any local ansatz whose log-density is `H_{b,k}`. In particular,
`\eta_{b,k}\to0` implies local-action residual decay.

### Proof

Let `K=H_{b,k}` and `H=H_b^{\rm perf}`. Since `\|H-K\|_\infty\le\eta`, the
density ratio satisfies

```math
e^{-2\eta}
\le
\frac{d\mu_H}{d\mu_K}
\le
e^{2\eta}.
```

Therefore for `\|F\|_\infty\le1`,

```math
|\mu_H(F)-\mu_K(F)|
\le
\mu_K\left(\left|\frac{d\mu_H}{d\mu_K}-1\right|\right)
\le
e^{2\eta}-1.
```

Taking the supremum over the finite battery gives the residual estimate.
`square`

### Corollary 6.5: Exponential-Tail Residual Bound

If the omitted local expansion terms obey

```math
\sum_{X\notin{\mathcal A}_k}|c_X|\,\|A_X\|_\infty
\le
C e^{-mR_k}
```

for a locality radius `R_k\to\infty`, then

```math
\delta_{n,k}(a,b)
\le
\exp(2Ce^{-mR_k})-1
=
O(e^{-mR_k}).
```

This gives a concrete residual-decay route: prove locality of the perfect
block strongly enough that the local ansatz tail is summable.

## 6A. Strong-Coupling Local Expansion Program

This section gives the first controlled route to residual decay. It is a
strong-coupling theorem program, not the full continuum scaling theorem. The
point is to prove that Paper 11 is not only a formal gate: in a genuine
four-dimensional non-Abelian regime, finite-battery local closure follows from
a standard polymer-smallness mechanism.

### Definition SC.1: Strong-Coupling Heat-Kernel Regime

Fix a finite four-dimensional lattice and the `SU(2)` heat-kernel plaquette
measure

```math
d\mu_t(U)
=
\frac{1}{Z_t}
\prod_p K_t(U_p)\prod_e dU_e.
```

The strong-coupling heat-kernel regime for a declared block map is a parameter
region in which the exact perfect-block density with respect to a local
coarse reference `\nu_b` admits a polymer expansion

```math
H_b^{\rm perf}
=
\sum_{\Gamma} \phi(\Gamma),
```

where:

1. each polymer `\Gamma` is a finite connected set of coarse plaquettes,
   links, or local cells;
2. `\phi(\Gamma)` is a bounded gauge-invariant local activity supported on
   `\Gamma`;
3. incompatible polymers are those with overlapping support or touching
   declared collars;
4. the polymer family is stable under finite Peter-Weyl projection on the
   declared battery.

This is a property to prove for the chosen blocking prescription. It is not
automatic from compactness of `SU(2)`.

### Hypothesis SC-KP: Kotecky-Preiss Smallness

There is a nonnegative size function `|\Gamma|`, a distance/diameter
`{\rm diam}(\Gamma)`, and constants `\alpha>0`, `\mu>0` such that the polymer
activities satisfy

```math
\|\phi(\Gamma)\|_\infty
\le
z(\Gamma),
```

and, for every polymer `\Gamma`,

```math
\sum_{\Gamma'\not\sim\Gamma}
z(\Gamma')e^{\alpha|\Gamma'|+\mu\,{\rm diam}(\Gamma')}
\le
\alpha|\Gamma|.
```

Here `\Gamma'\not\sim\Gamma` means that the two polymers are incompatible.

This is the named analytic smallness assumption of the strong-coupling
program. In conventional lattice-gauge language it is the place where the
strong-coupling/cluster expansion estimate must be supplied.

### Theorem SC.2: SC-KP Gives A Local Perfect-Block Expansion

Assume the strong-coupling heat-kernel regime and Hypothesis SC-KP. Then the
perfect-block log-density admits an absolutely convergent local expansion on
every finite battery:

```math
H_b^{\rm perf}
=
\sum_{\Gamma}\phi^T(\Gamma),
```

where the truncated/connected activities satisfy an exponential tail bound:

```math
\sum_{{\rm diam}(\Gamma)>R}
\|\phi^T(\Gamma)\|_\infty
\le
C_{\mathcal F}e^{-mR}
```

for constants `C_{\mathcal F}<\infty` and `m>0` depending on the declared
finite battery and the KP margin.

### Proof

Under SC-KP, the abstract polymer cluster expansion converges absolutely in
the Banach algebra of bounded finite-battery functions. The logarithm of the
polymer partition functional is the sum over connected clusters. The
Kotecky-Preiss bound with the diameter weight gives exponential decay of
connected cluster activities in the diameter. Summing all connected clusters
with diameter larger than `R` gives the displayed tail. Gauge invariance is
preserved because every activity is gauge-invariant and the Banach algebra
operations preserve gauge-invariant functions. `square`

### Corollary SC.3: Strong-Coupling Local RG Residual Decay

Let the local ansatz `{\mathcal A}_k` include every connected polymer activity
with diameter at most `R_k`. Under the hypotheses of Theorem SC.2,

```math
\eta_{b,k}
\le
C_{\mathcal F}e^{-mR_k}
```

and hence

```math
\delta_{n,k}(a,b)
\le
\exp(2C_{\mathcal F}e^{-mR_k})-1
=
O(e^{-mR_k}).
```

### Proof

The omitted part of the perfect-block log-density is exactly the sum of
connected polymer activities with diameter larger than `R_k`. Theorem SC.2
bounds this omitted tail, and Corollary 6.5 converts the tail estimate into a
finite-battery local-action residual bound. `square`

### Theorem SC.4: Strong-Coupling Finite-Battery Interface

Assume:

1. the strong-coupling heat-kernel regime and SC-KP hold uniformly on a fixed
   finite physical volume for the chosen block steps;
2. the ansatz radius `R_k` tends to infinity along the refinement path so that
   `e^{-mR_k}\to0`;
3. the Peter-Weyl projection, reflection-positivity, and Euclidean covariance
   defects in CYM-RG vanish on the declared finite scalar Wilson-loop battery.

Then the scalar Wilson-loop battery satisfies subsequential CYM-RG. If the
scale-stability, anchored nontriviality, and loop-continuity gates of Section
8 also hold, then Theorem 10.2 gives a unique nontrivial continuum-facing
Wilson-loop functional on that tested scalar class.

### Proof

Corollary SC.3 gives local-action residual decay. The remaining CYM-RG defects
vanish by assumption. Therefore subsequential CYM-RG holds. The final
sentence is exactly the five-gate upgrade theorem. `square`

### Definition SC.5: Heat-Kernel Character Smallness

Normalize Haar measure so that `\int dU=1`. The `SU(2)` heat kernel has the
Peter-Weyl expansion

```math
K_t(U)
=
1+
\sum_{j\in\frac12{\mathbb N},\,j>0}
d_j e^{-\frac12 c_j t}\chi_j(U),
\qquad
d_j=2j+1,\quad c_j=j(j+1).
```

Define the strong-coupling character norm

```math
\varepsilon(t)
=
\sum_{j>0}d_j^2 e^{-\frac12 c_j t}.
```

Then

```math
\|K_t-1\|_\infty\le\varepsilon(t),
\qquad
\varepsilon(t)\downarrow0
\quad\text{as}\quad t\to\infty.
```

For a finite Peter-Weyl cutoff `J`, define

```math
\varepsilon_J(t)
=
\sum_{0<j\le J}d_j^2 e^{-\frac12 c_j t}.
```

The cutoff version satisfies the same bound for the projected kernel. The
uncutoff expression is finite for every `t>0`, because `c_j` grows
quadratically in `j`.

### Lemma SC.6: Character Smallness Gives A Plaquette Polymer Gas

On a finite four-dimensional lattice,

```math
\prod_p K_t(U_p)
=
\prod_p(1+r_t(U_p)),
\qquad
\|r_t\|_\infty\le\varepsilon(t),
```

and hence

```math
\prod_p K_t(U_p)
=
\sum_{Y\subseteq P}
\prod_{p\in Y}r_t(U_p).
```

After Haar integration over any set of fine links and conditioning on any
declared coarse links, every term is supported on the coarse cells touched by
the connected components of `Y`. If `Y=Y_1\cup\cdots\cup Y_m` is the
decomposition into connected plaquette components, the corresponding
contribution factors over the components up to the declared block collars.

### Proof

The first identity is the character expansion with the trivial representation
split off. The product expansion is finite on a finite lattice. Haar
integration is a contraction in the sup norm, so the bound
`\|r_t\|_\infty\le\varepsilon(t)` survives every link integration. A term only
depends on link variables adjacent to plaquettes in `Y`; after the block map is
applied, it can only affect the coarse cells in the block-collar image of
`Y`. Disjoint connected components with separated collars involve disjoint
fine-link variables and therefore factor. `square`

### Theorem SC.7: Finite-Block SC-KP Verification At Large Heat Time

Fix:

1. dimension `d=4`;
2. a local block map with block ratio `s<\infty` and collar width `w<\infty`;
3. a finite Peter-Weyl cutoff `J`, or else the full heat kernel with
   `\varepsilon(t)` as above;
4. a finite number `N_b` of block steps;
5. a finite scalar Wilson-loop battery.

Write

```math
\varepsilon_*(t)=
\begin{cases}
\varepsilon_J(t),&\text{with Peter-Weyl cutoff }J,\\
\varepsilon(t),&\text{without a cutoff.}
\end{cases}
```

There are constants

```math
A=A(d,s,w,N_b,*),\qquad
B=B(d,s,w,N_b,*),\qquad
r_0=r_0(d,s,w,N_b)
```

such that the exact `N_b`-step blocked heat-kernel density admits a polymer
representation with activities satisfying

```math
\|\phi(\Gamma)\|_\infty
\le
A\,|\Gamma|\,
\left(B\,\varepsilon_*(t)\right)^{|\Gamma|}
```

whenever the right-hand side is finite. The symbol `*` records whether the
finite cutoff or uncutoff heat-kernel bookkeeping is being used. Moreover,
`{\rm diam}(\Gamma)\le r_0|\Gamma|` for the generated coarse polymers.

Consequently, for any chosen `\alpha>0` and `\mu>0`, SC-KP holds whenever

```math
C_{d,s,w,N_b,*}\,
B\,\varepsilon_*(t)\,
e^{\alpha+\mu r_0}
<
1,
```

where `C_{d,s,w,N_b,*}` bounds the number of connected coarse polymers of a
given size incompatible with a fixed polymer. In particular, for fixed
`d,s,w,N_b,*,\alpha,\mu`, SC-KP holds for all sufficiently large `t`.

### Proof

Use Lemma SC.6 before the block integrations. Each occupied fine plaquette
contributes at most `\varepsilon_*(t)`. A connected coarse
polymer of size `|\Gamma|` can be generated only by connected fine plaquette
sets contained in a bounded `N_b`-step collar thickening of `\Gamma`. The number
of such connected fine plaquette sets of size `n` touching a fixed coarse cell
is bounded by a lattice-animal estimate `C_0^n`, where `C_0` depends only on
`d,s,w,N_b` and on the declared representation bookkeeping. Summing over
`n\ge|\Gamma|` gives the activity bound after increasing `A` and `B`.

For the KP condition, any polymer incompatible with `\Gamma` must intersect
the finite collar-neighborhood of `\Gamma`. The number of incompatible
connected polymers of size `m` is bounded by `C_{d,s,w,N_b,*}^{m}|\Gamma|`.
Therefore

```math
\sum_{\Gamma'\not\sim\Gamma}
z(\Gamma')e^{\alpha|\Gamma'|+\mu{\rm diam}(\Gamma')}
\le
A|\Gamma|
\sum_{m\ge1}
m
\left(
C_{d,s,w,N_b,*}B\varepsilon_*(t)e^{\alpha+\mu r_0}
\right)^m.
```

If the displayed smallness condition is strengthened slightly so that the
last geometric series is at most `\alpha/A`, the KP inequality follows. Since
`\varepsilon_J(t)\to0` and `\varepsilon(t)\to0` as `t\to\infty`, the condition
holds at sufficiently large heat time. `square`

### Corollary SC.8: Imported SC-KP For Blocked Four-Dimensional `SU(2)`

For every fixed finite block depth, fixed local block prescription, fixed
finite battery, and fixed Peter-Weyl cutoff, the blocked four-dimensional
`SU(2)` heat-kernel measure satisfies SC-KP at sufficiently strong coupling
`t\ge t_{\rm sc}`. Therefore the residual-decay conclusion of Corollary SC.3
and the strong-coupling finite-battery interface of Theorem SC.4 hold in that
regime.

Without a Peter-Weyl cutoff the same statement holds if the uncutoff
character norm `\varepsilon(t)` is used and the chosen heat time makes the
geometric smallness condition finite and less than one.

### Import Note

The abstract convergence input is the Kotecky-Preiss polymer theorem. What
Paper 11 adds is the ISP-specific verification route: heat-kernel character
smallness plus local whole-block pushforward gives polymer activities small
enough for KP on finite batteries. This is Barandes-aligned because the block
map is an exact whole-process pushforward; no undeclared intermediate kernel
composition is being assumed.

### Theorem SC.9: Character SC-KP Does Not Continue To The AF Trajectory

The strong-coupling character-smallness proof cannot be continued unchanged
to the four-dimensional asymptotically-free continuum trajectory.

More precisely, the heat-kernel continuum direction corresponds to
`t(a)\downarrow0` after the usual weak-coupling tuning. Along such a path,
for any cutoff `J\ge1/2`,

```math
\varepsilon_J(t(a))
\ge
d_{1/2}^2 e^{-\frac12 c_{1/2}t(a)}
\longrightarrow
d_{1/2}^2
=4,
```

and the uncutoff norm `\varepsilon(t(a))` diverges as `t(a)\downarrow0`.
Therefore the KP smallness condition in Theorem SC.7 fails for the
Haar-background character polymer expansion.

### Proof

The first nontrivial representation already gives a non-small lower bound in
the cutoff character norm. Removing the cutoff only adds positive terms, and
the heat kernel approaches a delta distribution rather than a small
perturbation of Haar as `t\downarrow0`. Thus the expansion around the Haar
product background is the wrong expansion for the weak-coupling continuum
trajectory. `square`

### Definition SC.10: AF Locality-Margin Replacement

An asymptotic-freedom locality-margin replacement is a multiscale expansion
for the exact whole-block pushforward in which, after gauge fixing only as a
computational representation choice, each scale `r` admits a density of the
form

```math
\frac{d\mu_{r+1}^{\rm perf}}{d\nu_{r+1}}
=
\exp(-S_{r+1}^{\rm loc})
\left(
1+\sum_X K_{r+1}(X)
\right),
```

or equivalently a logarithmic polymer expansion, with:

1. `S_{r+1}^{\rm loc}` gauge-invariant after reconstruction from the fixed
   gauge representation;
2. the polymer remainders `K_{r+1}(X)` supported on scale-`r+1` connected
   blocks;
3. a scale-dependent margin

```math
\sum_{X\ni x}
\|K_{r+1}(X)\|_{\mathcal B_r}
e^{\alpha_r |X|+\mu_r{\rm diam}_r(X)}
\le
\eta_r;
```

4. a summability condition

```math
\sum_{r\ge r_0}\eta_r<\infty;
```

5. reflection-positivity, Euclidean-covariance, and gauge-invariance defects
   tracked in the CYM-RG ledger.

The Banach norm `\|\cdot\|_{\mathcal B_r}` may include finitely many
field/fluctuation derivatives and finite-battery observable derivatives. This
is not a new ontology. It is a calculational representation of the same
whole-process kernel.

### Theorem SC.11: AF Locality Margin Replaces SC-KP In Paper 11

If the asymptotic-freedom locality-margin replacement holds along a refinement
path and the finite local ansatz at scale `r` includes all scale polymers of
diameter at most `R_r`, then the local-action residual satisfies

```math
\eta_{\rm locRG}(r)
\le
\sum_{{\rm diam}_r(X)>R_r}
\|K_r(X)\|_{\mathcal B_r}
\le
\eta_r e^{-\mu_r R_r}.
```

If

```math
\sum_r \eta_r e^{-\mu_r R_r}<\infty,
```

then the residual part of strong CYM-RG is summable. If the remaining CYM-RG
defects are also summable and the uniqueness, nontriviality, and continuity
gates of Sections 8 and 10 hold, Paper 11 reaches the continuum-facing
Yang-Mills interface on the declared tested class.

### Proof

The proof is the same residual-tail mechanism as Theorem 6.4, with the
strong-coupling KP tail replaced by the scale-dependent AF polymer tail. The
summability condition gives Cauchy stability of the tested functionals along
the full refinement path. The remaining conclusion is exactly Theorem 10.2.
`square`

### Proposition SC.12: The Continuum-Trajectory Trichotomy

There are three logically distinct ways to relate the strong-coupling margin
to continuum Yang-Mills.

1. **Literal survival.** The same Haar-background character KP margin remains
   valid as `t(a)\downarrow0`. This is impossible by Theorem SC.9.
2. **Renormalized survival.** After each exact whole-block pushforward, the
   effective density is recentered around a weak-field/local-background
   reference and satisfies a new polymer margin. This is not literal SC-KP;
   it is an AF locality-margin theorem in different coordinates.
3. **Replacement.** The strong-coupling expansion is used only as a controlled
   finite-battery benchmark, while continuum Yang-Mills is attacked directly
   through a multiscale weak-coupling expansion, with gauge fixing,
   small-field/large-field decomposition, counterterms, and reflection
   positivity tracked in the CYM-RG ledger.

Thus Paper 11 has a proved strong-coupling local expansion route and a precise
continuum proof obligation. The next theorem needed for actual continuum
Yang-Mills is not "SC-KP for small `t`"; it is the AF locality-margin
replacement of Definition SC.10.

### AF Proof Obligations

To turn the replacement into a theorem, one must prove the following on the
declared growing batteries:

1. a gauge-covariant small-field chart and a controlled large-field remainder;
2. a local background action `S_r^{\rm loc}` with the correct running coupling
   and counterterm ledger;
3. a polymer remainder bound in a Banach norm strong enough to test Wilson
   loops and typed charged records;
4. summability of the scale margins `\eta_r`;
5. preservation or summable violation of reflection positivity and Euclidean
   covariance;
6. an anchored nontrivial Wilson-loop test and a loop-continuity modulus.

This list is deliberately stronger than compactness. Compactness gives
subsequences. Continuum Yang-Mills needs uniqueness, nontriviality, and
continuity.

### Definition AF.1: One-Block Geometry Constants

Fix one refinement step from scale `r` to scale `r+1`, with block ratio
`s=b/a`. Let `{\mathbb B}_{r+1}` be the finite set of coarse blocks in the
finite physical volume. Declare two coarse blocks adjacent if their
one-block collars touch. Let

```math
D_B
=
\max_{x\in{\mathbb B}_{r+1}}
\#\{y:y\sim x\}
```

be the maximum degree of this block-collar graph. A polymer is a nonempty
connected set `X\subset{\mathbb B}_{r+1}`. Its graph diameter is
`{\rm diam}_B(X)`.

The standard lattice-animal bound gives

```math
N_m(x)
:=
\#\{X\ni x:X\text{ connected}, |X|=m\}
\le
(eD_B)^{m-1}.
```

Let `C_{\rm col}` be the largest number of coarse blocks whose collars can
touch the collar of a fixed coarse block. If `X` is incompatible with `Y`,
then `X` contains at least one block in a `C_{\rm col}|Y|`-sized neighborhood
of `Y`.

For a finite battery `{\mathcal F}` let `N_{\mathcal F}` be the number of
coarse blocks intersecting the supports and collars of all tests in the
battery after the one-block map, and let `M_{\mathcal F}` be the norm
conversion constant from the polymer Banach norm to the dual battery norm:

```math
\sup_{\|F\|_{\mathcal F}\le1}
|\langle K(X),F\rangle|
\le
M_{\mathcal F}\|K(X)\|_{\mathcal B_r}
```

whenever `X` touches the battery support. These constants are finite in finite
volume and finite battery.

### Hypothesis AF-1B: One-Block Weak-Coupling Input Estimates

At scale `r`, let `g_r` be the running weak coupling. Assume the exact
one-block whole-process pushforward admits, after gauge fixing only as a
coordinate representation, a decomposition

```math
\frac{d\mu_{r+1}^{\rm perf}}{d\nu_{r+1}}
=
\exp(-S_{r+1}^{\rm loc})
\left(
1+\sum_X K_r(X)
\right),
```

where `S_{r+1}^{\rm loc}` is gauge-invariant after reconstruction and the
connected polymer activities split as

```math
K_r(X)
=
K_r^{\rm sf}(X)+K_r^{\rm lf}(X)+K_r^{\rm rem}(X).
```

Here `sf` means small-field perturbative contribution, `lf` means large-field
remainder, and `rem` means counterterm/truncation remainder. Suppose there
are explicit nonnegative constants

```math
a_{\rm sf},a_{\rm lf},a_{\rm rem},
\quad
b_{\rm sf},b_{\rm lf},b_{\rm rem},
\quad
c_{\rm lf}>0,
\quad
p\ge1
```

such that for every connected polymer `X`,

```math
\|K_r^{\rm sf}(X)\|_{\mathcal B_r}
\le
a_{\rm sf}(b_{\rm sf}g_r^p)^{|X|},
```

```math
\|K_r^{\rm lf}(X)\|_{\mathcal B_r}
\le
a_{\rm lf}(b_{\rm lf}e^{-c_{\rm lf}/g_r^2})^{|X|},
```

and

```math
\|K_r^{\rm rem}(X)\|_{\mathcal B_r}
\le
a_{\rm rem}(b_{\rm rem}g_r^{p+1})^{|X|}.
```

Define

```math
A_0=\max(a_{\rm sf},a_{\rm lf},a_{\rm rem}),
```

and

```math
Q_r
=
b_{\rm sf}g_r^p
+b_{\rm lf}e^{-c_{\rm lf}/g_r^2}
+b_{\rm rem}g_r^{p+1}.
```

Then

```math
\|K_r(X)\|_{\mathcal B_r}
\le
A_0Q_r^{|X|}.
```

### Theorem AF.2: One-Block AF Locality Margin With Explicit Constants

Assume Definition AF.1 and Hypothesis AF-1B. Choose locality weights
`\alpha>0` and `\mu>0`. If

```math
\zeta_r
:=
eD_B Q_r e^{\alpha+\mu}
<
1,
```

then the one-block activities satisfy the explicit AF locality margin

```math
\sum_{X\ni x}
\|K_r(X)\|_{\mathcal B_r}
e^{\alpha|X|+\mu{\rm diam}_B(X)}
\le
\eta_r^{\rm 1B},
```

with

```math
\eta_r^{\rm 1B}
=
\frac{A_0Q_r e^\alpha}{1-\zeta_r}.
```

Moreover, the KP-style incompatible-polymer bound holds whenever

```math
C_{\rm col}\eta_r^{\rm 1B}\le\alpha,
```

because then, for every connected `Y`,

```math
\sum_{X\not\sim Y}
\|K_r(X)\|_{\mathcal B_r}
e^{\alpha|X|+\mu{\rm diam}_B(X)}
\le
\alpha |Y|.
```

Finally, if the local ansatz keeps all one-block polymer activities with
`{\rm diam}_B(X)\le R_r`, then the finite-battery one-block local-RG residual
obeys

```math
\eta_{{\rm locRG},{\mathcal F}}^{\rm 1B}(r)
\le
M_{\mathcal F}N_{\mathcal F}\,
\eta_r^{\rm 1B}e^{-\mu R_r}.
```

### Proof

For connected polymers with `|X|=m` and `X\ni x`, Definition AF.1 gives at
most `(eD_B)^{m-1}` choices. Also
`{\rm diam}_B(X)\le m-1`. Hence

```math
\sum_{X\ni x}
\|K_r(X)\|_{\mathcal B_r}
e^{\alpha|X|+\mu{\rm diam}_B(X)}
\le
\sum_{m\ge1}
(eD_B)^{m-1}
A_0Q_r^m
e^{\alpha m+\mu(m-1)}.
```

This is the geometric series

```math
A_0Q_r e^\alpha
\sum_{m\ge1}\zeta_r^{m-1}
=
\frac{A_0Q_r e^\alpha}{1-\zeta_r},
```

provided `\zeta_r<1`.

If `X` is incompatible with `Y`, then `X` contains a block in a
`C_{\rm col}|Y|`-sized collar-neighborhood of `Y`. Summing the previous
one-point estimate over that neighborhood gives
`C_{\rm col}|Y|\eta_r^{\rm 1B}`, which is at most `\alpha|Y|` by the displayed
condition.

For the residual tail, if `{\rm diam}_B(X)>R_r`, then
`e^{-\mu R_r}e^{\mu{\rm diam}_B(X)}\ge1`. Therefore the omitted polymer tail
touching any fixed battery block is bounded by
`\eta_r^{\rm 1B}e^{-\mu R_r}`. Multiplying by the number
`N_{\mathcal F}` of battery-touching coarse blocks and by the norm conversion
constant `M_{\mathcal F}` gives the finite-battery residual estimate. `square`

### Lemma AF.3: Explicit Large-Field Suppression Constant For `SU(2)`

For `U\in SU(2)`, write `U=\exp(i\theta\,n\cdot\sigma)` with
`0\le\theta\le\pi`. Then

```math
1-\frac12{\rm Re\,Tr}(U)
=
1-\cos\theta
\ge
\frac{2}{\pi^2}\theta^2.
```

For the Wilson plaquette action

```math
S_p(U)=\frac{4}{g_r^2}
\left(1-\frac12{\rm Re\,Tr}(U)\right),
```

any plaquette with `\theta\ge\rho` has action at least

```math
S_p(U)\ge\frac{8\rho^2}{\pi^2g_r^2}.
```

Thus a large-field component containing at least `n` bad plaquettes has bare
Boltzmann suppression at most

```math
\exp\left(-\frac{8\rho^2}{\pi^2g_r^2}n\right),
```

before finite entropy and Jacobian constants are absorbed into
`b_{\rm lf}`. In Hypothesis AF-1B one may therefore take

```math
c_{\rm lf}<\frac{8\rho^2}{\pi^2}
```

after leaving margin for those finite constants.

### Proof

The elementary inequality `1-\cos\theta\ge2\theta^2/\pi^2` holds on
`[0,\pi]`. Substitution into the Wilson plaquette action gives the displayed
bound. A component with `n` bad plaquettes contributes the product of the
individual Boltzmann suppressions; finite local entropy and coordinate
Jacobians change only the prefactor/base `b_{\rm lf}`. `square`

### Proposition AF.4: One-Block AF Theorem Does Not Yet Prove Continuum YM

Theorem AF.2 proves a finite-volume, finite-battery, one-block locality
margin from explicit one-block weak-coupling estimates. To obtain the AF
locality-margin replacement of Definition SC.10 along a continuum refinement
path, one must additionally prove:

1. the constants `A_0,D_B,C_{\rm col},M_{\mathcal F},N_{\mathcal F}` remain
   controlled under the declared growing-battery schedule;
2. the couplings and perturbative order make
   `\sum_r\eta_r^{\rm 1B}<\infty`, or at least
   `\sum_r\eta_r^{\rm 1B}e^{-\mu R_r}<\infty`;
3. the local action `S_{r+1}^{\rm loc}` has the correct Yang-Mills running
   coupling and allowed counterterm ledger;
4. reflection positivity, Euclidean covariance, and gauge reconstruction
   defects are exact or summable;
5. nontriviality and loop-continuity gates hold.

This is the precise next frontier after the one-block theorem.

### Definition AF.5: Gauge-Fixed One-Block Analytic Package

Fix one finite-volume block step and use the **block axial-tree gauge** as the
default coordinate gauge: in every block collar choose a rooted spanning tree,
set tree links to the identity by a local gauge transform, and use logarithms
of the remaining non-tree links and coarse boundary links as coordinates.
Residual root gauge freedom is either fixed by a declared root convention or
integrated back into the Haar projection. The gauge is used only to
coordinatize the exact whole-process pushforward. The reconstructed statements
are gauge-invariant.

Let `A` denote fine fluctuation coordinates around a coarse background `V`.
Let `\rho\in(0,\pi)` be the small-field radius. The package
`AF-GF(r)` consists of the following explicit constants:

```math
\lambda_r,\ C_{\rm cov},\ m_{\rm cov},\
C_3,\ C_4,\ C_J,\ C_{\rm ct},\
C_{\rm ent},\ C_{\rm Jac},\ C_{\rm obs}.
```

They mean:

1. **Chart and Jacobian.** On the small-field region
   `|\theta_p|\le\rho`, the logarithm chart and gauge slice are unique on
   each block collar, and the Jacobian satisfies

   ```math
   |\log J(A)-\log J(0)|
   \le
   C_J\sum_b \|A\|_{b}^{2}.
   ```

2. **Gauge-fixed coercivity.** The quadratic part of the gauge-fixed action
   satisfies

   ```math
   \langle A,H_r A\rangle
   \ge
   \lambda_r\|A\|_{1,r}^{2}
   ```

   on the orthogonal complement of residual gauge zero modes.

3. **Covariance localization.** The Gaussian covariance
   `C_r=g_r^2H_r^{-1}` admits a block-local decomposition or bound

   ```math
   \|C_r(b,b')\|
   \le
   C_{\rm cov}g_r^2 e^{-m_{\rm cov}d_B(b,b')}.
   ```

4. **Local Taylor remainder.** The non-quadratic small-field action on a block
   collar obeys

   ```math
   |V_{\rm int}(A;b)|
   \le
   C_3 g_r\|A\|_{b}^{3}
   +C_4 g_r^2\|A\|_{b}^{4}.
   ```

5. **Counterterm/truncation remainder.** After extracting the declared local
   action `S_{r+1}^{\rm loc}`, the leftover local counterterm error obeys

   ```math
   |V_{\rm ct}(A;b)|
   \le
   C_{\rm ct}g_r^{p+1}(1+\|A\|_{b}^{4}).
   ```

6. **Large-field suppression.** A connected large-field component with `n`
   bad plaquettes has measure contribution bounded by

   ```math
   (C_{\rm ent}C_{\rm Jac})^n
   \exp(-c_{\rm lf}/g_r^2\,n),
   ```

   with `c_{\rm lf}<8\rho^2/\pi^2` allowed by Lemma AF.3.

7. **Observable derivative control.** The finite battery observables obey the
   Banach-norm conversion bound with constant `C_{\rm obs}` on every touched
   block collar.

The covariance localization item is the delicate one. If the raw massless
covariance does not satisfy it, one must prove an equivalent finite-range
multiscale covariance decomposition and assign its scale components to typed
polymers. Without such a localization statement, AF-1B is not proved.

### Lemma AF.6: Small-Field Gaussian Moment Bound

Assume `AF-GF(r)`. For every block-collar local polynomial `P(A)` of degree
`q` with coefficient norm `\|P\|_{\rm coeff}`, its Gaussian expectation under
the covariance `C_r` satisfies

```math
\left|
{\mathbb E}_{C_r}P(A)
\right|
\le
\|P\|_{\rm coeff}
(q-1)!!
\left(C_{\rm cov}g_r^2\right)^{q/2}
```

with the convention `(q-1)!!=1` for `q=0,1`.

### Proof

The finite-dimensional Wick formula writes the expectation as a sum over
pairings. Each contraction is bounded by the covariance norm
`C_{\rm cov}g_r^2`. There are at most `(q-1)!!` pairings. `square`

### Lemma AF.7: Small-Field Connected Activity Bound

Assume `AF-GF(r)`. Let

```math
L_r
=
eD_B e^{-m_{\rm cov}}
```

and define

```math
B_{\rm sf}
=
C_{\rm obs}
\left(
6C_3C_{\rm cov}^{3/2}
+24C_4C_{\rm cov}^{2}
+C_JC_{\rm cov}
+\frac{L_rC_{\rm cov}}{1-e^{-m_{\rm cov}}}
\right)
```

whenever `e^{-m_{\rm cov}}<1`. Then the connected small-field polymer
activities obey

```math
\|K_r^{\rm sf}(X)\|_{\mathcal B_r}
\le
\left(B_{\rm sf}g_r\right)^{|X|}
```

for sufficiently small `g_r` with `B_{\rm sf}g_r<1`.

### Proof

Expand the small-field density around the Gaussian quadratic part. Each
interaction insertion is local to a block collar. Lemma AF.6 bounds cubic
vertices by `6C_3C_{\rm cov}^{3/2}g_r`, quartic vertices by
`24C_4C_{\rm cov}^{2}g_r^2`, and the Jacobian quadratic correction by
`C_JC_{\rm cov}g_r^2`. The finite-battery observable derivatives are bounded
by `C_{\rm obs}`. Connectedness is enforced by the standard forest expansion:
to connect `|X|` blocks one needs at least `|X|-1` covariance links, and the
sum over links crossing block distance is bounded by the displayed
`L_rC_{\rm cov}/(1-e^{-m_{\rm cov}})` factor. Enlarging the constant absorbs
the harmless higher powers of `g_r` and the finite local combinatorics.
`square`

### Lemma AF.8: Counterterm Remainder Activity Bound

Assume `AF-GF(r)`. Define

```math
B_{\rm rem}
=
C_{\rm ct}(1+3C_{\rm cov}^{2})C_{\rm obs}.
```

Then the counterterm/truncation activities obey

```math
\|K_r^{\rm rem}(X)\|_{\mathcal B_r}
\le
\left(B_{\rm rem}g_r^{p+1}\right)^{|X|}.
```

### Proof

The counterterm remainder is local by construction after extracting
`S_{r+1}^{\rm loc}`. Lemma AF.6 bounds
`{\mathbb E}(1+\|A\|_b^4)` by `1+3C_{\rm cov}^2g_r^4`, which is bounded by
`1+3C_{\rm cov}^2` for `g_r\le1`. Multiplying by the observable conversion
constant gives the displayed local activity bound. Connected products are
handled by the same finite-block polymer bookkeeping as in Lemma AF.7.
`square`

### Lemma AF.9: Large-Field Activity Bound

Assume `AF-GF(r)`. Define

```math
B_{\rm lf}=C_{\rm ent}C_{\rm Jac}C_{\rm obs}.
```

Then the large-field activities obey

```math
\|K_r^{\rm lf}(X)\|_{\mathcal B_r}
\le
\left(B_{\rm lf}e^{-c_{\rm lf}/g_r^2}\right)^{|X|}.
```

### Proof

A connected large-field polymer of `|X|` coarse blocks contains at least one
bad plaquette per touched block after increasing the collar convention if
necessary. Lemma AF.3 gives the plaquette Boltzmann suppression; finite local
entropy, chart Jacobians, and finite-battery observable derivatives are
absorbed into `B_{\rm lf}`. `square`

### Theorem AF.10: Gauge-Fixed One-Block Analysis Implies AF-1B

Assume `AF-GF(r)` and `g_r\le1`. Then Hypothesis AF-1B holds with

```math
p=1,
\qquad
a_{\rm sf}=a_{\rm lf}=a_{\rm rem}=1,
```

```math
b_{\rm sf}=B_{\rm sf},\qquad
b_{\rm lf}=B_{\rm lf},\qquad
b_{\rm rem}=B_{\rm rem},
```

and `c_{\rm lf}` as in the large-field suppression item of `AF-GF(r)`.
Equivalently,

```math
Q_r
=
B_{\rm sf}g_r
+B_{\rm lf}e^{-c_{\rm lf}/g_r^2}
+B_{\rm rem}g_r^{2}.
```

Therefore, if

```math
eD_B e^{\alpha+\mu}Q_r<1
```

and

```math
C_{\rm col}
\frac{Q_r e^\alpha}{1-eD_Be^{\alpha+\mu}Q_r}
\le
\alpha,
```

then the one-block AF locality margin and residual tail of Theorem AF.2
hold.

### Proof

Lemma AF.7 supplies the small-field term with `p=1`. Lemma AF.9 supplies the
large-field term. Lemma AF.8 supplies the counterterm/truncation term with
order `g_r^2`. These are precisely the three estimates required by
Hypothesis AF-1B. The final statement is Theorem AF.2 with `A_0=1`. `square`

### Theorem AF.11: Iteration Of One-Block Constants

Assume `AF-GF(r)` holds for all `r\ge r_0` with uniform constants

```math
D_B\le D,\quad C_{\rm col}\le C_{\rm col}^*,\quad
B_{\rm sf}\le B_s,\quad B_{\rm lf}\le B_l,\quad
B_{\rm rem}\le B_c,
\quad c_{\rm lf}\ge c_*,
```

and with battery growth satisfying

```math
M_{{\mathcal F}_r}N_{{\mathcal F}_r}\le G_r.
```

Let

```math
Q_r^*
=
B_sg_r+B_l e^{-c_*/g_r^2}+B_cg_r^2,
```

and choose fixed `\alpha,\mu>0` such that

```math
\zeta_r^*
:=
eD e^{\alpha+\mu}Q_r^*
\le
\frac12
```

for all `r\ge r_0`. Then

```math
\eta_r^{\rm 1B}
\le
2Q_r^*e^\alpha.
```

If the truncation radii `R_r` satisfy

```math
\sum_{r\ge r_0}
G_r Q_r^* e^{-\mu R_r}
<\infty,
```

then the local-RG residual tail is summable:

```math
\sum_{r\ge r_0}
\eta_{{\rm locRG},{\mathcal F}_r}^{\rm 1B}(r)
<\infty.
```

In particular, if `G_r\le C_G r^q`, `g_r^2\le C_g/\log r`, and the extracted
local action is chosen so that

```math
Q_r^*=O(g_r^{p_s})+O(e^{-c_*/g_r^2})
```

for some `p_s>0`, then choosing

```math
R_r
\ge
\frac{(q+3)\log r}{\mu}
```

makes the residual series summable.

### Proof

The first estimate follows from Theorem AF.10 and Theorem AF.2:
`(1-\zeta_r^*)^{-1}\le2`. Multiplying the residual tail by the battery growth
bound gives

```math
\eta_{{\rm locRG},{\mathcal F}_r}^{\rm 1B}(r)
\le
2e^\alpha G_r Q_r^*e^{-\mu R_r}.
```

The displayed summability condition gives the result. For the example
schedule, the large-field term is a negative power of `r` after the standard
asymptotic-freedom relation `g_r^2\le C_g/\log r`; the perturbative remainder
may decay only logarithmically, so the growing local radius is essential. The
chosen `R_r` contributes a factor at most `r^{-(q+3)}`, which makes the
product with polynomial battery growth summable even with logarithmic
perturbative decay. `square`

### Theorem AF.12: Block Axial-Tree Gauge Proves Finite-Volume `AF-GF(r)`

Fix one finite-volume lattice, one block step, one finite battery, and the
block axial-tree gauge of Definition AF.5. Let `{\mathcal C}_r` be the finite
set of block collars and let `E_T` be the non-tree link coordinates after
tree links have been set to the identity. Let

```math
\ell_T
=
\max_{e\in E_T}
\#\{\text{plaquettes in a chosen fundamental surface for }e\}.
```

Choose the small-field radius so that

```math
0<\rho<\frac{\pi}{4\ell_T}.
```

Let `H_T` be the Hessian of the Wilson action in the non-tree coordinates at
the identity background, restricted to the orthogonal complement of residual
root gauge modes. Define

```math
\lambda_T
=
\min_{\|A\|_{1,r}=1}\langle A,H_TA\rangle.
```

Assume the block boundary convention fixes residual flat modes so that
`\lambda_T>0`. For any chosen `m_*>0`, define

```math
C_{\rm cov}^{T}(m_*)
=
\max_{b,b'\in{\mathcal C}_r}
e^{m_*d_B(b,b')}
\|H_T^{-1}(b,b')\|
```

Let `U(A)` be the tree-gauge reconstruction map from non-tree logarithmic
coordinates to link variables. Define the local derivative constants on the
small-field coordinate ball by

```math
C_3^T
=
\frac{1}{6}
\max_b
\sup_{\|A\|_b\le 2\ell_T\rho}
\|D^3S_b(U(A))\|,
```

```math
C_4^T
=
\frac{1}{24}
\max_b
\sup_{\|A\|_b\le 2\ell_T\rho}
\|D^4S_b(U(A))\|,
```

and

```math
C_J^T
=
\sup_{0<\|A\|\le2\ell_T\rho}
\frac{|\log J(A)-\log J(0)|}{\|A\|^2}.
```

For the declared local action extraction, define

```math
C_{\rm ct}^T
=
\sup_b\sup_{\|A\|_b\le2\ell_T\rho}
\frac{|V_{\rm ct}(A;b)|}
{g_r^{p+1}(1+\|A\|_b^4)}.
```

For the finite battery, define

```math
C_{\rm obs}^T
=
\max_{\|F\|_{\mathcal F}\le1}
\max_b
\sup_{\|A\|_b\le2\ell_T\rho}
\sum_{j\le4}\|D^jF_b(U(A))\|.
```

Finally, let `D_f` be the maximum degree of the fine plaquette adjacency graph
inside a block collar and set

```math
C_{\rm ent}^T=eD_f,
\qquad
C_{\rm Jac}^T=\exp(C_J^T(2\ell_T\rho)^2).
```

Then `AF-GF(r)` holds in this finite volume with the explicit choices

```math
\lambda_r=\lambda_T,\quad
C_{\rm cov}=C_{\rm cov}^{T}(m_*),\quad
m_{\rm cov}=m_*,
```

```math
C_3=C_3^T,\quad C_4=C_4^T,\quad C_J=C_J^T,\quad
C_{\rm ct}=C_{\rm ct}^T,
```

```math
C_{\rm ent}=C_{\rm ent}^T,\quad
C_{\rm Jac}=C_{\rm Jac}^T,\quad
C_{\rm obs}=C_{\rm obs}^T,
```

and any

```math
c_{\rm lf}<\frac{8\rho^2}{\pi^2}.
```

### Proof

Tree gauge gives a unique representative after the rooted tree links are set
to the identity; only the root gauge freedom remains, and it is fixed or
Haar-averaged by declaration. For a non-tree link, the tree path plus that
link forms a fundamental cycle. In the small-field region the holonomy around
that cycle is a product of at most `\ell_T` plaquette holonomies. The choice
`\rho<\pi/(4\ell_T)` keeps every reconstructed non-tree link inside the
injectivity radius of the logarithm map, with coordinate norm bounded by
`2\ell_T\rho`. This proves the chart part.

The Haar measure in exponential coordinates on compact `SU(2)` has a smooth
positive Jacobian on the ball `\|A\|\le2\ell_T\rho`; the displayed definition
of `C_J^T` is finite and gives the Jacobian estimate.

The quadratic Wilson action in tree-gauge coordinates is a finite positive
quadratic form after residual flat/root modes are removed by the boundary
convention. Its smallest Rayleigh quotient is exactly `\lambda_T`, giving
coercivity. The Gaussian covariance is `C_r=g_r^2H_T^{-1}`. Since the collar
graph is finite, `C_{\rm cov}^{T}(m_*)` is finite for every fixed `m_*>0`,
and the displayed covariance localization bound follows by definition.

The Taylor bounds for the non-quadratic action and the counterterm remainder
follow from the finite suprema defining `C_3^T,C_4^T,C_{\rm ct}^T`. The
observable derivative bound follows from the finite battery and compact
small-field coordinate ball, giving `C_{\rm obs}^T`.

For large fields, Lemma AF.3 gives the plaquette suppression with any
`c_{\rm lf}<8\rho^2/\pi^2`; the number of connected bad-plaquette sets of
size `n` touching a fixed plaquette is bounded by `(eD_f)^n`, and the
Jacobian on each bad collar is bounded by `C_{\rm Jac}^T`. This gives the
large-field item. All seven items in `AF-GF(r)` are therefore verified.
`square`

### Corollary AF.13: Finite-Volume Block-Axial One-Block Locality

Under the hypotheses of Theorem AF.12, if the resulting constants satisfy the
smallness inequalities of Theorem AF.10, then the exact one-block
whole-process pushforward in block axial-tree gauge satisfies the one-block
AF locality margin and the finite-battery residual estimate of Theorem AF.2.

### Proof

Theorem AF.12 proves `AF-GF(r)`. Theorem AF.10 converts `AF-GF(r)` into
`AF-1B`, and Theorem AF.2 converts `AF-1B` into the locality margin and
residual tail. `square`

### Theorem AF.14: Conditional Multiscale Summability Theorem

Fix a refinement path `r\ge r_0` with finite volumes and nested finite
batteries `{\mathcal F}_r`. Assume:

1. **Uniform block-axial analytic package.** The block axial-tree gauge
   constants of Theorem AF.12 obey the uniform bounds required in
   Theorem AF.11:

   ```math
   D_B\le D,\quad C_{\rm col}\le C_{\rm col}^*,\quad
   B_{\rm sf}\le B_s,\quad B_{\rm lf}\le B_l,\quad
   B_{\rm rem}\le B_c,\quad c_{\rm lf}\ge c_*.
   ```

2. **Uniform covariance localization or finite-range replacement.** The
   weighted inverse-Hessian constants `C_{\rm cov}^{T}(m_*)` are uniformly
   bounded, or the covariance has a finite-range multiscale decomposition
   whose scale components satisfy the same bound after being assigned to
   typed polymers.

3. **Battery growth.**

   ```math
   M_{{\mathcal F}_r}N_{{\mathcal F}_r}\le G_r.
   ```

4. **Running-coupling smallness.** With

   ```math
   Q_r^*
   =
   B_sg_r+B_l e^{-c_*/g_r^2}+B_cg_r^2,
   ```

   there are fixed `\alpha,\mu>0` such that

   ```math
   eD e^{\alpha+\mu}Q_r^*\le\frac12.
   ```

5. **Local-radius summability.** The ansatz radii `R_r` obey

   ```math
   \sum_{r\ge r_0}G_rQ_r^*e^{-\mu R_r}<\infty.
   ```

6. **Ledger summability.** The projectivity, reflection-positivity,
   Euclidean-covariance, and gauge-reconstruction defects in CYM-RG are
   summable along the same path.

Then the local-RG residuals are summable:

```math
\sum_{r\ge r_0}
\eta_{{\rm locRG},{\mathcal F}_r}^{\rm 1B}(r)
<\infty.
```

Consequently, the residual-decay gate in strong CYM-RG holds on the declared
growing battery. If, in addition, the scale-stability, anchored
nontriviality, loop-continuity, and typed charged/matter control gates of
Sections 8--10 hold, then Paper 11 reaches the continuum-facing Yang-Mills
interface on that tested class.

### Proof

Theorem AF.12 gives finite-volume `AF-GF(r)` in block axial-tree gauge.
Assumptions 1 and 2 upgrade those finite-volume constants to the uniform or
typed finite-range constants required by Theorem AF.11. Theorem AF.11 then
gives

```math
\eta_{{\rm locRG},{\mathcal F}_r}^{\rm 1B}(r)
\le
2e^\alpha G_rQ_r^*e^{-\mu R_r}.
```

Assumption 5 makes the right-hand side summable. Assumption 6 adds the other
CYM-RG defects to the same summable ledger. The final continuum-facing
conclusion is exactly the five-gate theorem, Theorem 10.2. `square`

### Corollary AF.15: What Is Still Not Proved

Theorem AF.14 is not an unconditional construction of four-dimensional
continuum Yang-Mills. Its nontrivial unproved input is the uniform item 2:

```text
uniform covariance localization or an equivalent finite-range covariance
decomposition compatible with gauge reconstruction and reflection positivity.
```

Finite-volume block axial-tree gauge proves that the constants exist at each
fixed scale. It does not by itself prove that they remain useful as the
volume grows and the continuum limit is approached.

### Definition AF.16: Fixed-Ratio Block-Conditioned Scheme

A refinement path uses a fixed-ratio block-conditioned scheme if:

1. the block ratio `s` and collar width `w` are independent of `r`;
2. all block axial-tree gauges use a tree chosen from a finite list of
   templates, transported by lattice symmetries;
3. the quadratic fluctuation variables are split into coarse boundary
   variables `B_r` and fine block-interior variables `I_r`;
4. after the boundary variables are held fixed, the interior Hessian

   ```math
   H_{I_rI_r}
   ```

   is block diagonal over the declared block collars;
5. all norms in Theorems AF.10--AF.14 are scale-normalized block norms, so
   one block collar has the same finite-dimensional model at every scale;
6. the nested batteries satisfy an admissible growth bound

   ```math
   M_{{\mathcal F}_r}N_{{\mathcal F}_r}\le G_r.
   ```

This scheme is not a Markov-divisibility assumption. It is an exact Gaussian
conditioning identity inside the one-step whole-process pushforward, followed
by a local polymer expansion of the interacting remainder.

### Theorem AF.17: Uniform Geometry, Chart, Jacobian, And Local Derivative Constants

In a fixed-ratio block-conditioned scheme, the following constants from
Theorem AF.12 are uniform in the refinement scale `r`:

```math
\ell_T,\ D_B,\ C_{\rm col},\ D_f,\ C_{\rm ent},\
C_J,\ C_{\rm Jac},\ C_3,\ C_4.
```

Moreover, if the local action extraction rule has uniformly bounded
coefficient ledger through order `p+1`, then `C_{\rm ct}` is uniform. If the
battery derivative growth is admissible, then the only observable-dependent
degradation is the declared factor `G_r`.

### Proof

Fixed block ratio and collar width leave only finitely many block-collar
combinatorial templates. Therefore the tree-cycle length `\ell_T`, block
graph degree `D_B`, collar incompatibility constant `C_{\rm col}`, fine
plaquette adjacency degree `D_f`, and entropy constant `C_{\rm ent}=eD_f` are
uniform.

The small-field radius is chosen from the uniform bound on `\ell_T`, so the
tree-gauge coordinate ball is the same compact subset of a fixed
finite-dimensional model at every scale. The Haar Jacobian and the local
Wilson action are smooth on that compact set. Their derivative suprema give
uniform `C_J,C_{\rm Jac},C_3,C_4`. A uniformly bounded counterterm ledger gives
uniform `C_{\rm ct}` by the same compactness argument. Observable derivatives
are not uniformly bounded for arbitrary growing batteries; their allowed
growth is exactly what `G_r` records. `square`

### Theorem AF.18: Block Conditioning Gives Uniform Finite-Range Covariance

Assume the fixed-ratio block-conditioned scheme and suppose that each
Dirichlet block-interior Hessian template satisfies the uniform Poincare
bound

```math
\langle A_I,H_{II}^{(b)}A_I\rangle
\ge
\lambda_D\|A_I\|_{1,b}^{2},
\qquad
\lambda_D>0.
```

Then the conditional Gaussian covariance for the fine interior variables,
given the coarse boundary variables, has finite range and uniform norm:

```math
C_{I|B}^{(r)}
=
g_r^2 H_{I_rI_r}^{-1}
=
\bigoplus_b g_r^2 (H_{II}^{(b)})^{-1},
```

and

```math
\|C_{I|B}^{(r)}(b,b')\|
=0
\quad\text{if } b\ne b',
```

while

```math
\|C_{I|B}^{(r)}(b,b)\|
\le
\frac{g_r^2}{\lambda_D}.
```

Consequently the covariance-localization item of `AF-GF(r)` holds uniformly
with, for example,

```math
m_{\rm cov}=1,
\qquad
C_{\rm cov}=\lambda_D^{-1}.
```

### Proof

For a finite positive Gaussian with variables split as `(A_I,A_B)`, the
standard Schur-complement identity writes the measure as a marginal in
`A_B` times a conditional Gaussian in `A_I` with covariance
`g_r^2H_{I_rI_r}^{-1}`. Because the boundary variables include the collar
links through which different interiors communicate, `H_{I_rI_r}` is block
diagonal over the block interiors. Hence the conditional covariance is a
direct sum of block covariances and has zero cross-block range.

The Poincare bound gives
`\|(H_{II}^{(b)})^{-1}\|\le\lambda_D^{-1}` in the normalized block norm.
Multiplying by `g_r^2` gives the displayed covariance bound. Since
`g_r\le1` in the weak-coupling tail, the `AF-GF(r)` convention
`\|C_r(b,b')\|\le C_{\rm cov}g_r^2e^{-m_{\rm cov}d_B(b,b')}` holds with
`C_{\rm cov}=\lambda_D^{-1}` and any fixed positive `m_{\rm cov}` after
possibly increasing `C_{\rm cov}` on the finite set of same-block entries.
`square`

### Corollary AF.19: Uniform `AF-GF(r)` From Block-Conditioned Axial Gauge

In a fixed-ratio block-conditioned scheme satisfying the Dirichlet Poincare
bound of Theorem AF.18 and a uniformly bounded counterterm ledger, the
constants in `AF-GF(r)` are uniform in `r`, except for the declared battery
growth factor `G_r`. Therefore the hypotheses of Theorem AF.14 reduce to the
summability inequality

```math
\sum_{r\ge r_0}G_rQ_r^*e^{-\mu R_r}<\infty
```

plus the summability of reflection-positivity, Euclidean-covariance,
projectivity, and gauge-reconstruction defects.

### Proof

Theorem AF.17 gives uniform geometry, chart, Jacobian, local Taylor, and
counterterm constants. Theorem AF.18 gives uniform finite-range covariance.
Together these are precisely the uniform `AF-GF(r)` constants required by
Theorem AF.14. `square`

### Corollary AF.20: Slow Degradation Schedule

Suppose the fixed-ratio block-conditioned scheme holds and the remaining
non-geometric constants degrade at most polynomially:

```math
G_rQ_r^*\le C r^q(\log r)^{\beta}
```

for some finite `C,q,\beta`. If

```math
R_r\ge\frac{(q+2)\log r+(\beta+2)\log\log r}{\mu},
```

then

```math
\sum_{r\ge r_0}G_rQ_r^*e^{-\mu R_r}<\infty.
```

Thus polynomial or logarithmic degradation of the constants can be absorbed by
a slowly growing local ansatz radius.

### Proof

The chosen `R_r` gives

```math
e^{-\mu R_r}
\le
r^{-(q+2)}(\log r)^{-(\beta+2)}.
```

Multiplying by `Cr^q(\log r)^\beta` gives a summable upper bound
`Cr^{-2}(\log r)^{-2}`. `square`

### Definition AF.21: Ledger-Compatible Block Conditioning

A fixed-ratio block-conditioned scheme is ledger-compatible if, for each
one-step exact whole-process pushforward, the following five conditions hold.

1. **Exact disintegration.** The finite measure in block axial-tree
   coordinates factors as an exact conditional identity

   ```math
   d\mu_r(A_I,A_B)
   =
   d\mu_r^{B}(A_B)\,
   d\mu_r^{I|B}(A_I|A_B),
   ```

   with no replacement of the whole process by an undeclared Markov
   subprocess.

2. **Local Schur action ledger.** The logarithm of the boundary marginal
   `d\mu_r^B` is decomposed as

   ```math
   -\log d\mu_r^{B}
   =
   S_{r+1}^{\rm loc}
   +\sum_X K_r(X)
   +{\rm const},
   ```

   where `S_{r+1}^{\rm loc}` contains the declared running coupling and
   allowed local counterterms.

3. **Gauge reconstruction.** The gauge-fixed conditional identity is averaged
   over residual root gauges and reconstructed as a gauge-invariant statement
   on link variables.

4. **RP/covariance ledger.** Reflection positivity and Euclidean covariance
   are either exact for the block prescription or produce declared defects
   `\epsilon_{{\rm RP},r}` and `\epsilon_{{\rm Euc},r}`.

5. **Anchor preservation.** There is a bounded Wilson-loop test `T_*` and
   constants `T_{\rm triv},c_*>0` such that the exact blocked measure satisfies

   ```math
   |\mu_r^B(T_*)-T_{\rm triv}|\ge c_*,
   ```

   or the paper explicitly marks nontriviality as still open.

### Theorem AF.22: Exact Disintegration Preserves Whole-Process Semantics

In a finite block axial-tree gauge, exact conditioning on coarse boundary
variables preserves the whole-process pushforward. For every bounded
gauge-invariant battery test `F`,

```math
\int F\,d\mu_r
=
\int
\left(
\int F(A_I,A_B)\,d\mu_r^{I|B}(A_I|A_B)
\right)
d\mu_r^B(A_B).
```

Consequently replacing the interior Gaussian covariance by the conditional
finite-range covariance in the one-block expansion is not a Markov
divisibility assumption; it is an exact disintegration of the same finite
measure, followed by an expansion of the conditional integral.

### Proof

The block axial-tree coordinate map is a measurable bijection modulo the
declared residual root gauge averaging on the small-field chart, and the
large-field complement is included as a declared remainder. On a finite
measure space, the regular conditional distribution with respect to the
boundary sigma-algebra exists. The displayed identity is the tower property
of conditional expectation. No intermediate stochastic kernel is introduced
as physical dynamics; the full expectation is still the original one-step
whole-process expectation. `square`

### Theorem AF.23: Schur Complement Gives The Running Local Action Ledger

For the quadratic small-field part, write the gauge-fixed Hessian in boundary
and interior variables as

```math
H_r
=
\begin{pmatrix}
H_{BB}&H_{BI}\\
H_{IB}&H_{II}
\end{pmatrix}.
```

If `H_{II}` satisfies the uniform Dirichlet Poincare bound, then integrating
the conditional interior Gaussian produces the exact boundary quadratic form

```math
H_{B}^{\rm eff}
=
H_{BB}-H_{BI}H_{II}^{-1}H_{IB},
```

and determinant term

```math
\frac12\log\det H_{II}.
```

If the fixed-ratio block templates are translation/rotation symmetric up to
declared lattice defects, then `H_B^{\rm eff}` decomposes into:

```math
S_{r+1}^{\rm loc,quad}
+\sum_X K_r^{\rm quad}(X),
```

where the local part renormalizes the plaquette/rectangle/counterterm ledger
and the remainder is supported in block collars with the same finite-range
structure as the conditional covariance.

### Proof

This is the finite-dimensional Gaussian integration formula. Completing the
square in `A_I` yields the Schur complement for the boundary quadratic form
and the determinant normalization. Because `H_{II}^{-1}` is block diagonal
over conditioned interiors and the block templates are finite and
symmetry-controlled, the induced boundary terms are sums of local terms on
the corresponding block collars plus symmetry-defect terms already tracked in
the Euclidean covariance ledger. The local terms are exactly the allowed
coupling/counterterm updates in `S_{r+1}^{\rm loc}`; everything else is a
typed polymer remainder. `square`

### Theorem AF.24: Gauge Reconstruction Compatibility

Assume ledger-compatible block conditioning. If the original finite-lattice
measure is gauge-invariant and the root-gauge variables are either fixed with
Faddeev-Popov normalization or averaged back with Haar measure, then the
boundary marginal and the reconstructed local action are gauge-invariant on
all scalar Wilson-loop tests. Charged tests remain valid only when their
source/sink frames are declared typed instruments.

### Proof

Gauge fixing is a change of coordinates on gauge orbits, with the residual
root action accounted for by either normalization or Haar averaging. Scalar
Wilson loops are class functions on closed parallel transports, so their
expectations are unchanged by choosing the block axial-tree representative
and then reconstructing. The Schur complement and determinant terms are
computed in coordinates but originate from a gauge-invariant finite measure;
after residual averaging they define gauge-invariant scalar functionals.
Framed charged records transform at their endpoints and therefore require the
declared charged instruments, exactly as in the earlier Gamma-only no-go.
`square`

### Theorem AF.25: RP And Euclidean Covariance Ledger Compatibility

Assume ledger-compatible block conditioning. If the block partition,
tree-template choice, and local ansatz are invariant under a finite subgroup
`\mathcal G_r` of lattice Euclidean symmetries, then the one-step
Euclidean-covariance defect is bounded by the template mismatch:

```math
\epsilon_{{\rm Euc},r}
\le
\sup_{g\in{\mathcal G}_{\rm tested}}
\|g{\mathcal T}_r-{\mathcal T}_r\|_{\rm ledger},
```

where `{\mathcal T}_r` denotes the declared block/tree template data. If the
conditional integration is performed symmetrically across a reflection plane,
or by averaging the reflected pair of block prescriptions, then reflection
positivity is preserved on the tested positive-side battery up to a declared
defect `\epsilon_{{\rm RP},r}` equal to the corresponding asymmetry norm.

If

```math
\sum_r
(\epsilon_{{\rm Euc},r}+\epsilon_{{\rm RP},r})<\infty,
```

then these defects are compatible with strong CYM-RG.

### Proof

Euclidean covariance is an equality when the finite blocking data commute
with the tested symmetry. When they do not, applying a symmetry changes only
the finite template data, and the resulting difference is bounded by the
declared ledger norm. Reflection positivity is preserved by exact symmetric
conditional integration because it is just integration of positive-side
functions against a positive conditional measure. If a non-symmetric tree
choice is used, averaging over the reflected pair restores positivity on the
averaged prescription; any failure to average exactly is recorded as
`\epsilon_{{\rm RP},r}`. Summability makes the accumulated defect finite and
vanishing in the strong-CYM-RG residual ledger. `square`

### Theorem AF.26: Anchored Nontriviality Is Preserved By The Compatible Block Decomposition

Assume ledger-compatible block conditioning and suppose a bounded Wilson-loop
anchor satisfies

```math
|\mu_r^B(T_*)-T_{\rm triv}|\ge c_*
```

along the refinement path. If the local ansatz residual on `T_*` satisfies

```math
|\mu_r^{\rm loc}(T_*)-\mu_r^B(T_*)|\le\delta_r,
\qquad
\sum_r\delta_r<\infty,
```

and eventually `\delta_r\le c_*/2`, then the reconstructed local-RG path has

```math
|\mu_r^{\rm loc}(T_*)-T_{\rm triv}|\ge c_*/2
```

eventually. Therefore every continuum limit obtained from that path is
nontrivial on the anchored test.

### Proof

By the triangle inequality,

```math
|\mu_r^{\rm loc}(T_*)-T_{\rm triv}|
\ge
|\mu_r^B(T_*)-T_{\rm triv}|
-|\mu_r^{\rm loc}(T_*)-\mu_r^B(T_*)|
\ge
c_*-\delta_r.
```

For all sufficiently large `r`, this is at least `c_*/2`. The lower bound is
closed under subsequential or full limits. `square`

This is a preservation theorem, not a proof that the anchor exists. Producing
the anchor is the remaining nontriviality problem for the chosen continuum
trajectory.

### Theorem AF.27: Compatibility Package Feeds The Five-Gate Theorem

Assume:

1. fixed-ratio block-conditioned axial gauge with the uniformity conditions
   of Corollary AF.19 or the slow-degradation schedule of Corollary AF.20;
2. ledger-compatible block conditioning in the sense of Definition AF.21;
3. local-radius summability and defect summability as in Theorem AF.14;
4. an anchored Wilson-loop test satisfying Theorem AF.26;
5. loop-continuity and typed charged/matter control.

Then the block-conditioned finite-range covariance decomposition is
compatible with the exact whole-process Yang-Mills RG ledger and yields the
continuum-facing Yang-Mills interface on the declared tested class.

### Proof

Theorem AF.22 gives exact whole-process semantics. Theorem AF.23 supplies the
running local action and polymer ledger. Theorem AF.24 gives gauge
reconstruction. Theorem AF.25 supplies summable reflection-positivity and
Euclidean-covariance ledger control. Theorem AF.14 gives summable local-RG
residuals. Theorem AF.26 supplies nontriviality transfer. With loop
continuity and typed record control, the hypotheses of the five-gate theorem
are satisfied. `square`

### Definition AF.28: Renormalized Yang-Mills Trajectory Ledger

Fix the refinement orientation

```math
a_{r+1}=a_r/s,
\qquad s>1,
```

so increasing `r` moves toward the ultraviolet continuum limit. Let

```math
u_r=\frac{1}{g_r^2}.
```

For pure `SU(2)` Yang-Mills, define the one-loop inverse-coupling coefficient

```math
\beta_{\rm inv}
=
\frac{11}{12\pi^2}.
```

A ledger-compatible block-conditioned scheme tracks the perturbative
Yang-Mills trajectory on the declared finite battery if the local action
ledger has:

1. coupling update

   ```math
   |u_{r+1}-u_r-\beta_{\rm inv}\log s|
   \le
   A_\beta g_r^2+\xi_r;
   ```

2. irrelevant local couplings `h_{r,j}` satisfying

   ```math
   |h_{r+1,j}|
   \le
   s^{-\Delta_j}|h_{r,j}|+\xi_{r,j},
   \qquad
   \Delta_j>0;
   ```

3. summable ledger errors

   ```math
   \sum_r
   \left(
   \xi_r+\sum_j\xi_{r,j}
   \right)
   <\infty;
   ```

4. no relevant gauge-invariant pure-gauge coupling other than the
   Yang-Mills coupling is generated, except for declared finite-volume or
   boundary terms whose effects vanish in the tested battery.

The coefficient is written for pure `SU(2)`. For `SU(N)` it is replaced by
`11N/(24\pi^2)` in the same inverse-coupling convention.

### Theorem AF.29: Ledger Tracking Gives The Perturbative YM Trajectory

Assume Definition AF.28 and suppose `g_r^2\le c/\log r` along the refinement
tail. Then the running inverse coupling satisfies

```math
u_r
=
u_{r_0}
\beta_{\rm inv}(r-r_0)\log s
 +O\left(\sum_{k=r_0}^{r-1}g_k^2\right)
 +O\left(\sum_{k=r_0}^{\infty}\xi_k\right).
```

Moreover, every irrelevant coupling with `\Delta_j>0` obeys

```math
|h_{r,j}|
\le
s^{-\Delta_j(r-r_0)}|h_{r_0,j}|
\sum_{k=r_0}^{r-1}
s^{-\Delta_j(r-1-k)}\xi_{k,j},
```

and hence tends to zero if the error sequence is summable.

Therefore the local action ledger tracks the intended perturbative
asymptotically-free Yang-Mills trajectory on the declared finite battery,
up to the stated summable and logarithmic errors.

### Proof

Sum the coupling recurrence from `r_0` to `r-1`. The one-loop term telescopes
to `\beta_{\rm inv}(r-r_0)\log s`; the remaining terms are bounded by the
two displayed error sums. The irrelevant-coupling estimate is the standard
iteration of an affine contraction. Since `s^{-\Delta_j}<1`, the homogeneous
term decays and a summable forcing term produces a vanishing tail. `square`

### Definition AF.30: Smeared Wilson-Loop Anchor

Let `C` be a fixed smooth continuum loop, `\rho` a nontrivial representation,
and `\tau>0` a fixed physical smearing radius. Let

```math
W_{\rho,\tau}(C)
=
\frac{1}{d_\rho}{\rm Re\,Tr}_\rho\,{\mathcal P}
\exp\left(\oint_C A_\tau\right)
```

be the corresponding smeared scalar Wilson-loop test. Define the perturbative
Gaussian loop coefficient

```math
I_\tau(C)
=
\int_C\int_C
\dot x^\mu(t)\dot x^\nu(t')
D_{\mu\nu}^{(\tau)}(x(t)-x(t'))\,dt\,dt',
```

where `D^{(\tau)}` is the gauge-fixed covariance after smearing and
projection to scalar Wilson-loop data. The anchor is admissible if

```math
I_\tau(C)>0.
```

For a nontrivial smooth loop with nonzero smeared gauge-field form factor,
this positivity is the perturbative statement that the loop couples to the
gauge fluctuation field.

### Theorem AF.31: Perturbative Smeared Wilson-Loop Anchor

Assume the ledger-compatible scheme tracks the perturbative Yang-Mills
trajectory in the sense of Definition AF.28. Fix a physical reference scale
where the renormalized coupling satisfies

```math
0<g_-^2\le g_R^2\le g_+^2,
```

with `g_+` small enough for the smeared Wilson-loop expansion. Suppose the
local-RG approximation gives, uniformly along the tested path,

```math
\mu_r(W_{\rho,\tau}(C))
=
1
-
\frac12 C_2(\rho)I_\tau(C)g_R^2
 +{\mathcal R}_r,
```

with

```math
|{\mathcal R}_r|
\le
\frac14 C_2(\rho)I_\tau(C)g_R^2.
```

Then `W_{\rho,\tau}(C)` is an anchored nontrivial Wilson-loop test with
trivial reference value `T_{\rm triv}=1` and gap

```math
c_*
=
\frac14 C_2(\rho)I_\tau(C)g_-^2.
```

### Proof

The expansion and remainder bound imply

```math
|1-\mu_r(W_{\rho,\tau}(C))|
\ge
\frac12 C_2(\rho)I_\tau(C)g_R^2
-
\frac14 C_2(\rho)I_\tau(C)g_R^2
=
\frac14 C_2(\rho)I_\tau(C)g_R^2.
```

Using `g_R^2\ge g_-^2` gives the displayed uniform lower bound. `square`

This is not a confinement or mass-gap theorem. It is a perturbative
nontriviality anchor at a fixed physical reference scale, using a smeared
Wilson-loop test in a controlled weak-coupling window.

### Theorem AF.32: Trajectory Tracking Plus Anchor Closes The Paper-11 Interface

Assume:

1. the compatibility package of Theorem AF.27;
2. the perturbative trajectory ledger of Definition AF.28 and Theorem AF.29;
3. the smeared Wilson-loop anchor of Theorem AF.31;
4. loop-continuity and typed charged/matter control on the declared battery.

Then the ledger-compatible block-conditioned scheme tracks the intended
perturbative continuum Yang-Mills trajectory on the tested class and has a
nontrivial anchored Wilson-loop test. Consequently Paper 11 reaches the
continuum-facing Yang-Mills interface on that tested class.

### Proof

Theorem AF.29 identifies the local action ledger with the perturbative
asymptotically-free Yang-Mills trajectory, with irrelevant couplings tending
to zero and summable ledger errors. Theorem AF.31 supplies the nontrivial
anchor. Theorem AF.27 then feeds residual summability, gauge reconstruction,
RP/covariance ledger compatibility, and nontriviality into the five-gate
interface theorem. `square`

### Boundary Of The Gauge-Fixed Derivation

Theorem AF.12 proves finite-volume `AF-GF(r)` for the block axial-tree gauge.
Theorems AF.17--AF.18 prove that the constants are uniform under the
fixed-ratio block-conditioned scheme with a uniform Dirichlet Poincare bound.
Corollary AF.20 proves that polynomial or logarithmic degradation can be
absorbed by a slowly growing local radius.

The remaining warning is now more specific. The proof does not say that the
raw global massless covariance is exponentially local. It says that the
conditional fine-block covariance is finite range after coarse boundary
variables are held fixed. The continuum proof must therefore show that this
block-conditioned decomposition is compatible with the exact whole-process
pushforward, the running local Yang-Mills action, reflection positivity,
Euclidean covariance, and gauge reconstruction. If that compatibility fails,
the AF locality-margin route fails at the correct place rather than being
hidden inside notation.

### Boundary Of The Strong-Coupling Result

The strong-coupling program gives a controlled positive route for finite
four-dimensional non-Abelian batteries. It does not by itself prove the
continuum Yang-Mills scaling window. The remaining extrapolation problem is:

```text
Can the SC-KP locality margin be continued, replaced, or renormalized along
the asymptotically-free continuum scaling trajectory?
```

Theorem SC.9 says that the literal Haar-background character KP margin does
not survive that trajectory. The viable continuum route must therefore replace
SC-KP by an AF locality margin of the sort in Definition SC.10, or by an
equivalent multiscale theorem. If that replacement is proved, Paper 11 becomes
a route to continuum Yang-Mills. If not, it remains a rigorous
controlled-regime non-Abelian ISP/Yang-Mills interface plus a clear obstruction
to the local-action continuum target.

## 7. Reflection Positivity And Gauge Invariance Preservation

### Definition 7.1: RP-Admissible Ansatz

A local ansatz family is reflection-positive admissible on a finite battery if
for every reflection `\vartheta` through a lattice hyperplane and every
positive-side test `F` in the battery,

```math
\mu^{\rm loc}_{a,k,\theta}((\vartheta F)F)\ge -\epsilon_{\rm RP}(a,k).
```

It is exactly RP-admissible if `\epsilon_{\rm RP}=0`.

### Theorem 7.2: Convex RP Preservation On Finite Batteries

If `\mu_1,\ldots,\mu_r` are reflection-positive normalized functionals on a
finite battery and `\lambda_i\ge0`, `\sum_i\lambda_i=1`, then

```math
\mu=\sum_i\lambda_i\mu_i
```

is reflection-positive on that battery.

### Proof

For every positive-side test `F`,

```math
\mu((\vartheta F)F)
=
\sum_i\lambda_i\mu_i((\vartheta F)F)\ge0.
```

`square`

### Theorem 7.3: Gauge Invariance Under Gauge-Invariant Completion

If the reference measure is gauge-invariant and every added local operator
`A_\alpha` is gauge-invariant, then every local ansatz
`\mu^{\rm loc}_{a,k,\theta}` is gauge-invariant.

### Proof

The Radon-Nikodym factor
`\exp(\sum_\alpha\theta_\alpha A_\alpha)` is gauge-invariant. Multiplying a
gauge-invariant measure by a gauge-invariant density and normalizing preserves
gauge invariance. `square`

### Reflection-Positivity Boundary

Theorem 7.3 is automatic for gauge-invariant completions. Reflection
positivity is not automatic. Paper 11 must track it as either:

1. exact, for heat-kernel/character-positive constructions where the RP proof
   applies;
2. approximate, with explicit `\epsilon_{\rm OS}`;
3. failed, if a needed local completion violates finite-battery positivity.

## 8. Continuum Yang-Mills Candidate Functional

Let `C_1,\ldots,C_m` be piecewise smooth continuum loops and
`\rho_1,\ldots,\rho_m` finite-dimensional `SU(2)` representations. Choose
lattice approximants `C_{i,a}` and define

```math
S_a(C_1,\rho_1;\ldots;C_m,\rho_m)
=
\mu^{\rm loc}_{a,k(a),\theta(a)}
\left(
\prod_{i=1}^m W_{\rho_i}(C_{i,a})
\right).
```

### Definition 8.1: Continuum-Facing Yang-Mills Functional

A continuum-facing Yang-Mills functional on a tested loop class is a limit

```math
S(C_1,\rho_1;\ldots;C_m,\rho_m)
=
\lim_{a\to0}S_a(C_1,\rho_1;\ldots;C_m,\rho_m)
```

that is:

1. gauge-invariant;
2. Euclidean covariant on the tested loop class;
3. reflection-positive on the tested loop class;
4. continuous under the declared loop topology;
5. nontrivial.

### Definition 8.2: Countable Bounded Wilson-Loop Test Class

A countable bounded Wilson-loop test class is an enumeration

```math
T_1,T_2,\ldots
```

where each `T_r` is a finite product of Wilson-loop traces in finite
representations, evaluated on chosen lattice approximants. Each test has a
uniform bound

```math
|T_r|\le B_r<\infty
```

on every finite lattice.

This class includes scalar Wilson-loop products. It does not automatically
include normalized charged curvature records such as
`a^{-2}(\rho(U_P)-I)`, unless a separate uniform bound or smearing/truncation
prescription is declared.

### Theorem 8.3: Diagonal Subsequence Compactness For Wilson-Loop Tests

Let `a_j\downarrow0` be any refinement sequence. For every countable bounded
Wilson-loop test class and every sequence of normalized finite-lattice
functionals `\mu_{a_j}`, there is a subsequence `a_{j_r}\downarrow0` such
that

```math
\lim_{r\to\infty}\mu_{a_{j_r}}(T_q)
```

exists for every `q`.

If each finite-lattice functional is gauge-invariant, the limiting functional
is gauge-invariant on the tested scalar loop class. If the reflection
positivity and Euclidean covariance defects tend to zero along the subsequence,
then the limiting functional is reflection-positive and Euclidean covariant
on the tested class.

### Proof

For fixed `T_1`, the sequence `\mu_{a_j}(T_1)` lies in the compact disk
`|z|\le B_1`, so it has a convergent subsequence. From that subsequence extract
a further subsequence on which `T_2` converges, and continue. The diagonal
subsequence makes every `T_q` converge.

Gauge invariance is an equality on every finite lattice and therefore passes
to the pointwise limit. Reflection positivity and covariance are finite
inequalities/equalities up to defects; if the defects tend to zero, the
limiting inequalities/equalities hold. `square`

### Corollary 8.4: Convergence Is Not An Independent Assumption For Countable Bounded Tests

For countable bounded Wilson-loop tests, Paper 11 does not need to assume
existence of a subsequential limit. It is automatic by Theorem 8.3. What
remains nontrivial is:

1. uniqueness of the limit along the full refinement path;
2. nontriviality of the limit;
3. continuity in a continuum loop topology beyond the countable tested class;
4. inclusion of unbounded charged curvature or matter records.

### Theorem 8.5: Conditional Continuum-Facing Yang-Mills Interface

Assume subsequential CYM-RG along `a_r\downarrow0` for a countable bounded
Wilson-loop test class. Assume also:

1. the finite-lattice local ansatz functionals have uniformly bounded
   moments on every fixed tested Wilson-loop family;
2. the loop approximants are stable under refinement;
3. the finite-battery functionals are asymptotically reflection-positive and
   Euclidean covariant, with defects included in CYM-RG.

Then there is a subsequence defining a gauge-invariant, reflection-positive,
Euclidean-covariant Wilson-loop functional on the countable tested class.

If strong CYM-RG holds, the subsequential functional is unique on the tested
class and therefore defines the full refinement-path limit there.

If the resulting functional is also nontrivial and continuous in the declared
loop topology, then it satisfies Definition 8.1 on that tested class.

### Proof

Theorem 8.3 supplies a subsequence on which all countable bounded Wilson-loop
tests converge. Gauge invariance follows from Theorem 7.3 and passage to the
limit. Reflection positivity and Euclidean covariance follow by taking limits
of finite-battery inequalities and covariance identities with defects tending
to zero. Strong CYM-RG adds uniqueness of subsequential limits, so the
subsequential construction is independent of the chosen subsequence. `square`

This theorem is the correct level of ambition for Paper 11. It does not prove
the constructive existence of four-dimensional Yang-Mills. It says exactly
which finite-battery ISP/RG conditions would supply a subsequential
Wilson-loop interface, and which extra conditions upgrade it to the
continuum-facing functional of Definition 8.1. The theorem has removed one
avoidable conditional: bounded countable Wilson-loop convergence is automatic
subsequentially.

### Definition 8.6: Scale-Stability Modulus

For a countable tested class `T_q`, define the one-step stability modulus

```math
\Delta_r(q)
=
\left|
\mu_{a_{r+1}}(T_{q,a_{r+1}})
-
\mu_{a_r}(T_{q,a_r})
\right|.
```

A residual ledger `\Xi_r` controls the tested class if, for each fixed `q`,
there is a finite constant `C_q` such that

```math
\Delta_r(q)\le C_q\Xi_r.
```

### Theorem 8.7: Summable Scale-Stability Gives Uniqueness

If for every fixed tested Wilson-loop record `T_q`,

```math
\sum_{r=1}^\infty \Delta_r(q)<\infty,
```

then `\mu_{a_r}(T_{q,a_r})` converges along the full refinement path. In
particular, all subsequential limits agree on the countable tested class.

If `\Delta_r(q)\le C_q\Xi_r` and `\sum_r\Xi_r<\infty`, then the same
conclusion holds.

### Proof

For `s>r`,

```math
\left|
\mu_{a_s}(T_{q,a_s})-\mu_{a_r}(T_{q,a_r})
\right|
\le
\sum_{\ell=r}^{s-1}\Delta_\ell(q).
```

The tail of the summable series tends to zero, so the sequence is Cauchy.
The second statement follows by comparison with `\sum C_q\Xi_r`. `square`

This is the practical uniqueness criterion. Strong CYM-RG can be proved by
showing summable scale-stability, rather than by assuming uniqueness as a
black box.

### Theorem 8.8: Anchored Nontriviality Criterion

Let `T_*` be a bounded Wilson-loop test. Suppose there is a number `c_*>0` and
a reference trivial value `T_{\rm triv}` such that along the full scaling path,
or along the subsequence under consideration,

```math
\left|
\mu_a(T_{*,a})-T_{\rm triv}
\right|
\ge c_*.
```

Then any limiting Wilson-loop functional on that path or subsequence is
nontrivial.

### Proof

The inequality is closed under limits. Therefore the limiting functional
assigns `T_*` a value separated from the trivial reference by at least
`c_*`. It cannot be the trivial functional. `square`

The paper does not prove such an anchor from first principles. It identifies
the finite observable that must remain nontrivial in the scaling window.

### Definition 8.9: Loop-Topology Modulus

Let `d_{\rm loop}` be the declared metric on the tested continuum loop class.
The finite-lattice loop tests have a uniform continuity modulus if there are
functions `\omega(\delta)\to0` and errors `\zeta(a)\to0` such that

```math
\left|
\mu_a(W_\rho(C_a))-\mu_a(W_\rho(C'_a))
\right|
\le
\omega(d_{\rm loop}(C,C'))+\zeta(a)
```

for all tested loops `C,C'` and their chosen lattice approximants.

### Theorem 8.10: Uniform Loop Modulus Gives Continuity

If a limiting Wilson-loop functional exists and the finite-lattice tests have
a uniform loop-topology modulus, then the limiting functional is continuous in
`d_{\rm loop}`.

### Proof

Take the limit along the convergent path or subsequence in the inequality of
Definition 8.9. The error `\zeta(a)` vanishes, leaving

```math
|S(W_\rho(C))-S(W_\rho(C'))|
\le
\omega(d_{\rm loop}(C,C')).
```

Since `\omega(\delta)\to0`, the limiting functional is continuous. `square`

## 9. Matter Boundary

Paper 11 separates four targets.

### Pure Yang-Mills

The pure target uses only scalar Wilson loops and charged curvature probes.
Its main gates are local RG closure, reflection positivity, and continuum
loop-limit tightness.

### Valence Wilson Matter

Valence matter adds finite Wilson-Dirac source contractions to the battery but
does not modify the gauge measure by a dynamical determinant. Its main gate is
whether Wilson matter source/counterterm operators close the response rank
without breaking the gauge/RP structure of the gauge background.

### Dynamical Wilson Matter

Dynamical matter adds determinant or reweighting records. A positive even-
flavor determinant prescription may define a positive finite state; a complex
phase or sign must be kept as a reweighting instrument. The main gates are:

1. positivity or controlled sign/phase reweighting;
2. anomaly and chiral bookkeeping;
3. uniform determinant control;
4. compatibility with the local RG closure algorithm.

### No-Wilson Detail-Preserving Matter

The no-Wilson branch keeps taste/detail labels as records. It can match a
Wilson target only after declared projection, taste-blinding, or accepted
sector conditioning. Otherwise it is a multi-taste or retained-record branch,
not a failed Wilson regularization.

### Definition 9.1: Controlled Charged Record

A charged curvature record `\Phi_a` is controlled on a refinement path if one
of the following is declared.

1. **Bounded truncation:** records `\Phi_{a,R}` satisfy
   `|\Phi_{a,R}|\le R` and the truncation error obeys
   ```math
   \sup_a |\mu_a(\Phi_a-\Phi_{a,R})|\to0
   \qquad (R\to\infty).
   ```
2. **Smeared bounded record:** the continuum target is represented by smeared
   lattice records that are uniformly bounded on the tested class.
3. **Moment-tight record:** there is `p>1` and `C_p<\infty` with
   ```math
   \sup_a \mu_a(|\Phi_a|^p)\le C_p,
   ```
   and the family is uniformly integrable.

The point is ontological as much as analytic: charged curvature is not scalar
Gamma data. It becomes part of the continuum interface only when the charged
instrument and its boundedness/tightness prescription are declared.

### Theorem 9.2: Controlled Charged Records Extend The Compactness Argument

For any countable family of controlled charged records, diagonal subsequence
compactness extends from scalar Wilson loops to the scalar-plus-charged tested
class. If the charged records are included in the CYM-RG residual ledger, then
their comparison-map and exchange-defect limits are controlled by the same
residual estimates as scalar tests.

### Proof

For bounded charged records, the proof is identical to Theorem 8.3. For
truncated records, first pass to a diagonal subsequence for each fixed
truncation level, then send the truncation level to infinity using the
declared truncation error. For moment-tight records, uniform integrability
gives the same truncation step by standard `L^p` tail control. The residual
statement follows from Paper 10's propagation of local residuals to
comparison maps and exchange defects. `square`

### Definition 9.3: Controlled Wilson Matter Record

A Wilson matter source contraction is controlled if the Wilson-Dirac block is
used with a declared infrared regulator or invertible-domain restriction such
that

```math
\|(D_W[U]+M)^{-1}\|\le C_M
```

on the tested finite domain, and the source vectors are uniformly bounded.

Dynamical determinant records are controlled if their normalized weights have:

1. nonzero denominators bounded away from zero on the tested path;
2. either positivity or an explicit sign/phase reweighting instrument;
3. uniform integrability sufficient to pass to bounded truncations.

### Theorem 9.4: Controlled Wilson Matter Records Extend The Interface

For a countable family of controlled Wilson matter records, diagonal
subsequence compactness extends to the scalar-plus-charged-plus-Wilson-matter
tested class. If the Wilson matter records are included in the local ansatz
and the CYM-RG residual ledger, then the subsequential interface includes
valence Wilson matter records.

Dynamical Wilson matter is included only as a positive state when the
determinant prescription is nonnegative. With sign or phase reweighting, the
result is a normalized reweighted functional, not automatically a positive
OS state.

### Proof

The inverse bound and source bounds make each valence source contraction
uniformly bounded, so Theorem 8.3 applies. Local ansatz inclusion and CYM-RG
then propagate residual control exactly as in Theorem 10.1 below. For
dynamical records, denominator control and uniform integrability permit the
same bounded-truncation compactness argument. Positivity is preserved only
for nonnegative weights; sign or phase reweighting produces a declared
normalized functional but not a positive state unless an additional positivity
argument is supplied. `square`

### Corollary 9.5: Charged And Matter Gates Are Now Explicit

The remaining charged/matter gates are not vague convergence assumptions.
They are:

1. declare the charged or matter instrument;
2. prove boundedness, truncation control, or uniform integrability;
3. include the corresponding local operators in the ansatz;
4. preserve or explicitly replace positivity.

If any item fails, the failure is a typed obstruction, not a failure of scalar
Wilson-loop compactness.

## 10. Main Paper-11 Theorem

### Theorem 10.1: Conditional Continuum Yang-Mills From ISP Local RG Closure

Suppose:

1. Paper-10 finite-battery projective gauge control holds on the refinement
   net;
2. subsequential CYM-RG holds for a nested pure-gauge or charged gauge battery
   on a countable bounded Wilson-loop test class;
3. the local ansatz is gauge-invariant and asymptotically reflection-positive;
4. charged curvature records are included whenever framed `F_{\mu\nu}` data
   are claimed.

Then the relativistic ISP non-Abelian gauge family has a subsequential
gauge-invariant, reflection-positive, Euclidean-covariant Wilson-loop
functional on the declared countable tested class. Moreover, comparison maps
and exchange defects converge along the same subsequence with residuals
bounded by the CYM-RG residual ledger.

If strong CYM-RG holds and the limiting functional is nontrivial and
continuous in the declared loop topology, then the result is a
continuum-facing Yang-Mills functional in the sense of Definition 8.1.

### Proof

Paper 10 supplies finite-battery projective control, perfect blocking,
local-residual propagation to comparison maps, and charged curvature targets.
Hypothesis CYM-RG makes the local-action residual, tail residual, projectivity
residual, reflection-positivity defect, and Euclidean covariance defect vanish
on the growing tested class. Theorem 8.5 gives the subsequential Wilson-loop
functional and the strong-limit upgrade when uniqueness holds. Paper-10
comparison-map propagation then gives convergence of `J_R` and `E_{R,S}` on
the same subsequence. Charged curvature claims require the charged
instruments by Paper 10's scalar Gamma no-go. Nontriviality and continuity are
exactly the extra hypotheses needed to satisfy Definition 8.1. `square`

### Theorem 10.2: Five-Gate Upgrade To A Strong Continuum Interface

Assume the Paper-10 finite-battery projective gauge control. Suppose, along a
declared full refinement path, the following five gates hold for the chosen
nested battery:

1. **Residual decay:** the perfect block admits local truncations with
   `\eta_{a,k(a)}\to0`, and the remaining projectivity/OS/Euclidean defects
   in CYM-RG vanish.
2. **Uniqueness:** the scale-stability moduli are summable on every fixed
   bounded Wilson-loop test, as in Theorem 8.7.
3. **Nontriviality:** an anchored Wilson-loop test satisfies Theorem 8.8.
4. **Continuity:** the finite-lattice Wilson-loop tests satisfy a uniform
   loop-topology modulus, as in Definition 8.9.
5. **Typed record control:** every charged or matter record included in the
   target is controlled in the sense of Definitions 9.1 and 9.3.

Then the ISP gauge family defines a unique nontrivial continuum-facing
Yang-Mills functional on the declared scalar Wilson-loop class. If controlled
charged records are included, the interface also contains the corresponding
framed curvature records. If controlled valence Wilson matter records are
included, the interface includes those valence matter records. Dynamical
matter is positive only under an explicitly positive determinant prescription.

### Proof

Residual decay follows from Theorem 6.4 once the local expansion tail tends to
zero, and the remaining CYM-RG defects vanish by assumption. Summable
scale-stability gives uniqueness by Theorem 8.7. The anchored test gives
nontriviality by Theorem 8.8. The uniform loop modulus gives continuity by
Theorem 8.10. Controlled charged and matter records extend compactness and
residual control by Theorems 9.2 and 9.4. The result therefore satisfies the
requirements of Definition 8.1 on the scalar class, with the declared
extensions for charged and valence matter records. Positivity for dynamical
matter is exactly the positivity clause in Theorem 9.4. `square`

## 11. Main Obstruction Theorem

### Theorem 11.1: Stable Residual Obstructs The Standard Local Yang-Mills Target

Fix a nested battery and a declared class of local gauge-invariant ansatz
operators. Suppose that along every scaling path one of the following holds:

1. `\liminf \delta_{n(a),k(a)}(a,ba)>0`;
2. `\liminf \epsilon_{\rm OS}(a)>0`;
3. the local expansion tail does not vanish for any allowed local basis;
4. scale-stability is not summable and subsequential limits are nonunique;
5. every subsequential limit is trivial on the anchored tests;
6. no uniform loop-topology modulus exists on the declared loop class;
7. charged or matter records fail boundedness, truncation, or uniform
   integrability control;
8. the completion rule requires a nonlocal operator;
9. the completion rule requires an untyped charged, matter, or taste/detail
   record;
10. the determinant/reweighting prescription fails positivity or controlled
   normalization.

Then the standard local Yang-Mills/QCD target for that declared battery is not
proved by this ISP construction. More strongly, if the obstruction persists
after all symmetry-allowed local completions are included, the target fails on
that battery unless the target is enlarged to include the obstructing typed
data.

### Proof

The strong continuum-facing conclusion of Theorem 10.2 requires residual
decay, reflection positivity, uniqueness, nontriviality, continuity, typed
charged/matter control, and admissible local operators. Each listed
obstruction negates one of those requirements. If all allowed local
completions have been exhausted, the remaining direction cannot be represented
as standard local Yang-Mills/QCD data on the declared battery. Enlarging the
target by typed charged, matter, taste/detail, or nonlocal data changes the
target rather than proving the original one. `square`

## 12. Export To Paper 12

Paper 12 may use Paper 11 to say:

1. Paper 11 defines the growing-battery/local-RG gate from finite
   non-Abelian ISP to continuum-facing Yang-Mills.
2. Monotonicity under ansatz enlargement is theorem-level.
3. The closure/obstruction dichotomy is theorem-level for fixed finite
   batteries and becomes a scaling gate for continuum limits.
4. CYM-RG is the sharp hypothesis replacing vague continuum Yang-Mills claims,
   with subsequential and strong versions separated.
5. Reflection positivity and gauge invariance are separated: gauge invariance
   is automatic under gauge-invariant completion, while reflection positivity
   is a real constraint.
6. Pure Yang-Mills, valence Wilson matter, dynamical Wilson matter, and
   no-Wilson detail-preserving branches are distinct targets.
7. Bounded countable Wilson-loop convergence is automatic subsequentially by
   diagonal compactness.
8. Residual decay follows from a local expansion tail estimate; exponential
   local tails give exponential residual decay.
9. The strong-coupling local expansion program gives a concrete controlled
   route: heat-kernel character smallness proves SC-KP for fixed finite block
   depth at sufficiently large heat time, and SC-KP implies an exponentially
   decaying perfect-block local tail and hence exponentially small local-RG
   residuals on finite batteries.
10. The same character SC-KP margin cannot be continued unchanged to the
    asymptotically-free continuum trajectory; that route requires a
    Balaban-style or equivalent multiscale AF locality-margin replacement.
11. If an AF locality margin with summable scale tails is proved, it replaces
    SC-KP in the residual-decay gate and feeds into the same five-gate
    continuum interface theorem.
12. The one-block AF locality theorem gives an explicit finite-volume bridge:
    small-field, large-field, and counterterm remainder bounds with constants
    `A_0,Q_r,D_B,C_{\rm col}` imply a one-block margin
    `\eta_r^{\rm 1B}=A_0Q_r e^\alpha/(1-\zeta_r)` and a finite-battery
    residual bound `M_{\mathcal F}N_{\mathcal F}\eta_r^{\rm 1B}e^{-\mu R_r}`.
13. The gauge-fixed one-block package `AF-GF(r)` proves `AF-1B` when the
    chart/Jacobian, Hessian coercivity, covariance localization, Taylor
    remainder, counterterm, large-field, and observable-derivative constants
    are controlled.
14. The block axial-tree gauge proves finite-volume `AF-GF(r)` with explicit
    constants: a tree-cycle radius `\ell_T`, a Hessian eigenvalue
    `\lambda_T`, a weighted inverse-Hessian covariance constant
    `C_{\rm cov}^T(m_*)`, local derivative suprema, and finite battery
    derivative bounds.
15. Iteration of one-block constants is theorem-level: if the uniform
    constants make `eD e^{\alpha+\mu}Q_r^*\le1/2` and
    `\sum_r G_rQ_r^*e^{-\mu R_r}<\infty`, then the local-RG residual tail is
    summable across scales.
16. Conditional multiscale summability is theorem-level: uniform `AF-GF(r)`,
    uniform covariance localization or finite-range covariance decomposition,
    battery-growth control, local-radius summability, and ledger summability
    imply strong-CYM-RG residual summability.
17. Fixed-ratio block conditioning proves uniform geometry, chart, Jacobian,
    Taylor, counterterm, and finite-range conditional covariance constants
    under a uniform Dirichlet Poincare bound.
18. Polynomial or logarithmic degradation of the remaining constants is
    harmless if the local ansatz radius grows as in Corollary AF.20.
19. The remaining analytic gate is compatibility: the block-conditioned
    finite-range covariance decomposition must preserve the exact
    whole-process pushforward, running local action, reflection positivity,
    Euclidean covariance, and gauge reconstruction.
20. Compatibility is theorem-level under ledger-compatible block
    conditioning: exact disintegration preserves whole-process semantics, the
    Schur complement supplies the running local action ledger, residual root
    averaging reconstructs gauge-invariant scalar tests, and RP/covariance
    defects are summable ledger entries.
21. Nontriviality is preserved, not generated: an anchored Wilson-loop lower
    bound survives the compatible local-RG approximation if the residual on
    that anchor is eventually smaller than the anchor gap.
22. The perturbative Yang-Mills trajectory is tracked when the inverse
    coupling ledger satisfies
    `u_{r+1}-u_r=\beta_{\rm inv}\log s+O(g_r^2)+\xi_r`, irrelevant
    couplings contract, and the errors are summable.
23. A smeared Wilson-loop anchor exists in a controlled weak-coupling reference
    window when the leading perturbative coefficient
    `I_\tau(C)` is positive and the remainder is smaller than half the
    leading gap.
24. Trajectory tracking plus the smeared anchor closes the Paper-11
    continuum-facing interface on the declared perturbative tested class.
25. Paper 11 does not supply the Paper-20 SEL2 tree-rate source. In
    particular, it does not prove `T_-^{SEL2}>0`, the SEL2 block-plaquette
    heat-kernel coefficient comparison, or `P20-SEL2-TREE-RATE-GATE`; these
    remain same-record coefficient estimates for Paper 20 or a later source
    paper.
26. Uniqueness follows from summable scale-stability, nontriviality from an
    anchored nonzero loop test, and continuity from a uniform loop-topology
    modulus.
27. Controlled charged and matter records extend compactness and residual
    control once boundedness/truncation/uniform-integrability prescriptions
    are declared.
28. Conditional continuum-facing Yang-Mills follows from the five gates:
    residual decay, uniqueness, nontriviality, continuity, and typed
    charged/matter control.
29. Subsequential CYM-RG alone gives a subsequential Wilson-loop interface.
30. Stable residuals are meaningful obstructions, not algebraic nuisances.

Paper 12 may not say, unless separately proved:

```text
V3 has constructed four-dimensional continuum Yang-Mills;
V3 has proved the mass gap;
V3 has proved confinement or a Wilson-loop area law;
Paper 11 supplies the Paper-20 SEL2 tree-rate/source gate;
V3 has proved QCD;
V3 has removed the need for charged instruments or Wilson/no-Wilson branch
typing;
V3 has derived non-Abelian gauge theory from Gamma-only scalar endpoint data.
```

## Honest Status

Paper 11 does not solve four-dimensional continuum Yang-Mills. It does
something more modest but useful: it turns the continuum problem into a
precise finite-battery ISP/RG ledger and proves several gates inside that
ledger.

The proved pieces are:

1. finite-battery closure is monotone under ansatz enlargement;
2. bounded countable Wilson-loop tests have subsequential limits by diagonal
   compactness;
3. local expansion tails imply local-RG residual decay;
4. strong-coupling heat-kernel character smallness proves SC-KP at sufficiently
   large heat time for fixed finite block depth and finite batteries;
5. the same strong-coupling margin provably fails as the continuum
   asymptotically-free trajectory moves toward weak coupling;
6. one-block AF locality follows from explicit weak-coupling input estimates;
7. block axial-tree gauge proves the finite-volume analytic package
   `AF-GF(r)`;
8. `AF-GF(r)` implies `AF-1B`;
9. conditional multiscale summability follows from uniform `AF-GF(r)`,
   uniform covariance localization or finite-range covariance decomposition,
   battery-growth control, local-radius summability, and summable
   positivity/covariance/projectivity defects.
10. fixed-ratio block conditioning proves the needed uniform constants under
    a uniform Dirichlet Poincare bound, and polynomial/logarithmic degradation
    is absorbed by a slowly growing local ansatz radius.
11. ledger-compatible block conditioning proves compatibility with exact
    whole-process semantics, running local action, gauge reconstruction, and
    summable RP/covariance defects.
12. anchored nontriviality is preserved by the compatible decomposition, but
    the existence of the anchor is still a separate continuum-dynamics input.
13. the perturbative Yang-Mills trajectory is tracked by the inverse-coupling
    and irrelevant-coupling ledger when the one-loop `SU(2)` coefficient and
    summable errors are declared.
14. a smeared Wilson-loop anchor exists in a weak-coupling reference window
    when its Gaussian loop coefficient is positive and the perturbative
    remainder is controlled.
15. the SEL2 coefficient-time lower bound, heat-kernel coefficient comparison,
    and Paper-20 tree-rate gate are not supplied here.

So the answer to "do we have the multiscale summability theorem?" is:

```text
Yes, conditionally: Theorem AF.14 proves multiscale residual summability from
uniform AF-GF constants plus uniform covariance localization or an equivalent
finite-range covariance decomposition.

Closer than before, but still not unconditional: Theorems AF.17--AF.20 prove
uniform or slowly degrading constants for a fixed-ratio block-conditioned
scheme, and Theorems AF.21--AF.27 prove compatibility with the exact
whole-process Yang-Mills RG ledger under the declared ledger-compatible
conditions. Theorems AF.28--AF.32 then show that, in a controlled
weak-coupling reference window, the scheme tracks the perturbative
asymptotically-free Yang-Mills trajectory and has a smeared Wilson-loop
nontriviality anchor.
```

If the residuals vanish only subsequentially, ISP has a subsequential
Wilson-loop interface. If the residuals are summable, the limit is unique,
an anchored nontrivial loop survives, loop-continuity holds, and typed
charged/matter records are controlled, then ISP has a continuum-facing
Yang-Mills interface on the tested class. If one of those gates fails, the
failure is classified as an obstruction: nonlocal perfect-block data, missing
charged instruments, uncontrolled matter records, positivity/sign failure,
retained no-Wilson detail, triviality, discontinuity, nonunique limits, or
failure of uniform covariance localization.

The hard remaining analytic core is now sharper:

```text
extend the perturbative tested-class interface to a fully nonperturbative
continuum Yang-Mills construction: unsmeared/general Wilson-loop continuity,
nonperturbative nontriviality, possible mass-gap control, and removal or
control of reference-window restrictions.
```

That is the point at which Paper 11 genuinely meets the constructive
four-dimensional Yang-Mills problem. Everything before that has been reduced
to explicit finite-dimensional constants and summability inequalities.

## Follow-Up Programs Beyond Paper 11

Paper 11 ends with a perturbative, smeared, finite-battery continuum-facing
Yang-Mills interface. The next V3 papers should not collapse the remaining
problems into one vague "finish Yang-Mills" task. They are four distinct
programs.

### Program A: Renormalized Unsmeared Wilson Loops

**Owner:** V3 Paper 12.

**Goal:** pass from the smeared perturbative Wilson-loop anchor of Paper 11 to
renormalized unsmeared Wilson-loop functionals.

Paper 11 supplies:

1. a smeared Wilson-loop anchor in a controlled weak-coupling reference
   window;
2. a perturbative continuum-facing Wilson-loop interface on the tested class;
3. a residual ledger controlling local-RG approximation errors.

Paper 12 must prove or conditionally prove:

1. a smearing-removal scheme `\tau\downarrow0`;
2. perimeter and cusp renormalization factors `Z_\rho(C,a,\tau)`;
3. uniform boundedness/tightness of renormalized loop records;
4. continuity in a continuum loop topology;
5. nontriviality transfer from the smeared anchor to the renormalized
   unsmeared loop.

This is the nearest next step because it attacks the exact boundary of Paper
11: smeared perturbative loops are controlled, unsmeared Wilson loops are not.

### Program B: Nonperturbative Continuum Yang-Mills

**Owner:** V3 Paper 13.

**Goal:** upgrade the perturbative tested-class interface into a
nonperturbative continuum Yang-Mills functional.

Paper 13 must address:

1. tightness and uniqueness beyond weak-coupling reference windows;
2. nonperturbative control of the Wilson-loop functional on a dense loop
   algebra;
3. block-choice and gauge-chart independence;
4. reflection positivity and Euclidean covariance without merely summable
   regulator bookkeeping;
5. a nonperturbative nontriviality anchor.

This is harder than Paper 12 because it asks for continuum construction, not
only renormalized loop records.

### Program C: Mass Gap

**Owner:** V3 Paper 14.

**Goal:** prove a positive spectral gap for the continuum-facing gauge theory.

Paper 14 must define gauge-invariant glueball or field-strength correlators
and prove exponential clustering:

```math
|\langle O(x)O(y)\rangle-\langle O(x)\rangle\langle O(y)\rangle|
\le
C e^{-m|x-y|},
\qquad m>0,
```

with `m` surviving the continuum limit. It must then use reflection
positivity to convert Euclidean clustering into a Wightman spectral gap.

This cannot be imported from Paper 11. Paper 11 has locality residuals and a
perturbative anchor, not a nonperturbative mass-gap theorem.

### Program D: Confinement

**Owner:** V3 Paper 15.

**Goal:** prove confinement through an area law or an equivalent operational
criterion.

The natural Wilson-loop target is:

```math
\langle W_\rho(C)\rangle
\asymp
\exp(-\sigma\,{\rm Area}(C)-\kappa\,{\rm Perimeter}(C)+o({\rm Area}(C))),
\qquad
\sigma>0.
```

Paper 15 must distinguish genuine area-law confinement from perimeter
renormalization, smearing artifacts, and finite-volume effects. It must also
connect the area law to the ISP ontology: colored charged records are typed
instruments and do not appear as isolated physical scalar Gamma records.

### Final V3 Synthesis

The final V3 synthesis should come after these programs, not as Paper 12.
Unless the sequence changes again, the synthesis should be V3 Paper 16. Its
job is to decide what V3 has actually established:

```text
full continuum Yang-Mills/QFT reconstruction,
an enriched representation layer with controlled gauge benchmarks,
or a precise obstruction ledger.
```

The synthesis must not claim mass gap, confinement, QCD, or full continuum
Yang-Mills unless the intervening papers have proved the corresponding gates.
