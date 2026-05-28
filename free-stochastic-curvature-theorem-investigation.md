# Full Investigation: V2 Paper 1 - The Free Stochastic-Curvature Theorem

Author: Felix Robles Elvira

Date: 2026-05-12

Purpose: investigate, in proof-level detail, what it would take to turn the existing free relativistic ISP exchange-defect papers into the first genuine continuum viability theorem. This is the first V2 paper because it tests whether the finite exchange-defect machinery is stochastic curvature in a physics-relevant sense or only a finite-lattice algebraic phenomenon.

Consolidated paper draft: `relativistic-isp-v2-paper1-free-stochastic-curvature-theorem.md`.

Follow-up proof artifacts: `coefficient-level-free-stochastic-curvature-theorem.md` proves the Tier 1 coefficient-level theorem identified below. `finite-slab-free-stochastic-curvature-theorem.md` proves a narrow Tier 2 finite-slab theorem for log-smeared exact comparison maps under `Delta(a)/a^2 -> 0`. Broader primitive-kernel smooth-lapse finite-slab regularizations remain open.

## Executive Conclusion

The original investigation found that the stack did not yet prove the full Free Stochastic-Curvature Theorem, but it did provide enough exact finite input to make the theorem plausible and sharply formulable. The Tier 1 coefficient-level theorem has now been proved, and a narrow log-smeared Tier 2 finite-slab theorem has also been proved. The broader primitive-kernel finite-slab theorem is still not proved.

The correct next move is a two-stage theorem:

1. **Coefficient-level curvature theorem.** Extract the normalized exchange-curvature coefficient from the exact finite `Delta` expansion, then prove its bond-centered continuum action on smooth sampled profiles. Status: proved in `coefficient-level-free-stochastic-curvature-theorem.md` at the leading collar-excision and normalized `lambda`-family scope.
2. **Finite-slab curvature theorem.** After the coefficient theorem is proved, control the finite-`Delta` remainder in a joint lattice-spacing/slab-size limit. Status: proved for log-smeared exact comparison maps under `Delta(a)/a^2 -> 0`; open for broader primitive smooth-lapse kernels.

Trying to prove the finite-slab theorem first would be premature. The symbol

```math
E_{N,M}(a,\Delta)
```

is not yet an earned object for smooth lapse profiles `N,M`. It has to be defined from localized finite deformations or from a weighted deformation rule. The existing papers prove exact statements for finite regions, singleton supports, support prototypes, and the `lambda`-family. V2 Paper 1 must build the smooth-lapse object from those data.

The realistic theorem target is therefore:

> The exact normalized coefficient-level exchange curvature of the free `1+1D` Dirac ISP converges, on smooth compactly supported profiles, to the tangential hypersurface-deformation operator `K_parallel[N partial_x M - M partial_x N]`, and the result is stable across the admissible `lambda` regulator family.

Only after that should one promote the result to a finite-slab theorem with explicit `Delta(a)` control.

## Existing Exact Inputs

The investigation rests on the following established finite results.

### Input 1: Free lattice Dirac kernel package

The free one-particle model uses the periodic lattice `Lambda_L = Z/LZ`, site-spin basis

```math
C_L = \Lambda_L \times \{\uparrow,\downarrow\},
```

and Hamiltonian

```math
H_D = K + M,
\qquad
K = -\frac{i}{2a}\alpha(T_+ - T_-),
\qquad
M = m\beta,
```

with `alpha = sigma_x`, `beta = sigma_z`. For any unitary `U`, the primitive stochastic kernel is

```math
\Gamma(U)_{AB} = |U_{AB}|^2.
```

The reference slab is

```math
\Gamma_0(\Delta)=\Gamma(e^{-i\Delta H_D}).
```

### Input 2: Collar-excision localized deformations

For finite interval support `R`, the collar Hamiltonian `C_R` contains the mass terms in `R` and the kinetic bonds incident on `R`; the bulk Hamiltonian is `B_R = H_D - C_R`. The collar-excision localized kernel is

```math
\Gamma_R(\Delta)=\Gamma(e^{-i\Delta B_R}),
```

and the comparison map is

```math
J_R(\Delta)=\Gamma_R(\Delta)\Gamma_0(\Delta)^{-1}.
```

This comparison map is algebraic. It is not required to be stochastic.

### Input 3: Exact quasilocal filtration

For every finite interval `R`, the collar-excision comparison map has the exact expansion

```math
J_R(\Delta)=I+\sum_{k\ge 1}\Delta^{2k}A_R^{(k)},
\qquad
\operatorname{supp} A_R^{(k)}\subset N_k(R).
```

Its inverse has the corresponding support-growth filtration in the small-slab regime where the reference kernel is invertible.

Important limitation: the existing result is fixed finite-lattice scope. Constants may depend on lattice size, mass, spacing, and support data unless a separate uniform estimate is proved.

### Input 4: Exact leading coefficient

For singleton `R={n}`,

```math
J_n(\Delta)=I+\Delta^2 A_n^{(1)}+O(\Delta^4),
```

and `A_n^{(1)}` is supported on `N_1({n})`. Its off-diagonal entries are deleted-bond data of size `1/(4a^2)`, its diagonal entries enforce column-sum zero, and it is mass-independent. The first mass-sensitive information enters at `A_n^{(2)}`.

### Input 5: Exchange-defect order formula

For disjoint supports `R,S`, the exchange defect has the leading expansion

```math
E_{R,S}(\Delta)=I+\Delta^{2\mu_1(R,S)}C_{R,S}^{(\mu_1)}+O(\Delta^{2\mu_1(R,S)+2}),
```

where

```math
C_{R,S}^{(\mu_1)}=
\sum_{p+q=\mu_1(R,S)}[A_R^{(p)},A_S^{(q)}].
```

For singleton supports at distance `d=2`, the leading coefficient is

```math
[A_n^{(1)},A_{n+2}^{(1)}],
```

with exact same-spin antisymmetric transfer entries of magnitude `1/(16a^4)`. For `d=3`, the first coefficient is

```math
[A_n^{(1)},A_{n+3}^{(2)}]+[A_n^{(2)},A_{n+3}^{(1)}].
```

### Input 6: Bond-centered tangential target

The leading bond-centered reduction identifies the tangential pseudo-generator

```math
K_\parallel[\beta]
=\left(\beta\partial_x+\frac12\partial_x\beta\right)(I-\alpha),
\qquad
\beta=N\partial_xM-M\partial_xN.
```

The crucial lesson is that the site-centered entrywise continuum limit fails. The stable object is the bond-centered action of the exchange-strip algebra on smooth sampled profiles.

### Input 7: Regulator facts

The present local-intervention axioms do not select a unique microscopic rule. The admissible `lambda` family

```math
U_R^{(\lambda)}(\Delta)=e^{-i\Delta(H_D-\lambda C_R)},
\qquad
c_\lambda=\lambda(2-\lambda),
```

obeys

```math
A_{R,\lambda}^{(1)}=c_\lambda A_R^{(1)}.
```

At the first non-leading singleton order, the full coefficient `A_{n,lambda}^{(2)}` is not simply `c_lambda A_n^{(2)}`, but the boundary-facing shell relevant to the first distance-three exchange still scales so that

```math
C_{n,n+3;\lambda}^{(3)}=c_\lambda^2 C_{n,n+3}^{(3)}.
```

Thus raw coefficient universality fails, but normalized strip-moment universality survives in the first tested cases.

## What Is Not Yet Defined

The V2 target theorem uses notation like

```math
E_{N,M}(a,\Delta)
```

for smooth lapse profiles `N,M`. The current finite papers do not yet define that object. They define exchange defects for finite regions or finite supports.

This is not a minor notation issue. It is the first technical gate of V2 Paper 1.

The theorem must decide which object is being sent to the continuum:

1. **Coefficient-level smeared curvature.** Use the exact expansion coefficients `C_{R,S}^{(mu)}` and build a bilinear smeared operator from translated strip channels and sampled lapse profiles.
2. **Finite-slab smeared group commutator.** Define actual smoothed comparison maps `J_N`, `J_M` for lapse profiles and set `E_{N,M}=J_NJ_MJ_N^{-1}J_M^{-1}`.
3. **Region-approximation limit.** Approximate smooth lapse profiles by finite unions of support regions and take a refinement limit of their exchange defects.

The recommended path is to prove option 1 first. Options 2 and 3 require additional product, Trotter, and remainder estimates that are not yet in the stack.

## The Theorem Ladder

### Tier 0: Existing finite coefficient ledger

This tier is already present in the current papers. It gives exact finite expansions and exact support/strip structure at selected leading and first non-leading scopes.

### Tier 1: Coefficient-level stochastic-curvature theorem

This is the first new theorem V2 Paper 1 should prove.

For smooth compactly supported lapses `N,M`, define a coefficient-level smeared curvature operator

```math
\mathcal C_a^{(\lambda)}[N,M]
```

from the exact finite exchange coefficients of translated singleton and support-prototype pairs. After onset normalization by `c_lambda^2` and spatial bond-centered renormalization by a factor `R_a`, prove

```math
\left\|
R_a c_\lambda^{-2}\mathcal C_a^{(\lambda)}[N,M]\iota_a\phi
-\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi
\right\|_{\ell^2_a}
\le C a\,\mathcal N(N,M,\phi),
```

for smooth compactly supported spinor profiles `phi`, where `iota_a` is the sampling map and `N,M` have support away from the periodic seam.

The exact rate `O(a)` is a target, not a given. If the best rate is weaker, the theorem should state the weaker rate.

### Tier 2: Finite-slab stochastic-curvature theorem

Once Tier 1 is proved, define finite-lapse comparison maps `J_N(a,Delta)` and `J_M(a,Delta)` and prove

```math
Z_{a,\Delta}c_\lambda^{-2}
\bigl(E_{N,M}^{(\lambda)}(a,\Delta)-I\bigr)\iota_a\phi
\to
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi
```

in a coupled limit `a -> 0`, `Delta -> 0` satisfying the correct small-slab condition.

This tier requires all Tier 1 estimates plus finite-`Delta` remainder control.

### Tier 3: Admissible-regulator theorem

After the `lambda` family is controlled, generalize from `lambda` to an admissible class of localized deformation rules. The admissible class should be defined by exact structural conditions, not by rhetorical similarity:

- exact kernel construction;
- common small-slab invertibility regime;
- quasilocal coefficient filtration;
- known onset exponent;
- strip-channel closure;
- normalized first strip moments matching the target tangential generator;
- uniform remainder bounds.

The Lie-Trotter rule should probably be treated as a separate onset class rather than part of the first common-onset theorem.

## Recommended Formal Setup

### Infinite-volume or large-ring convention

Use a large periodic ring only as a finite regulator. For continuum statements, impose:

```math
L(a)a\to\infty,
```

and require the supports of `N`, `M`, and `phi` to lie in a compact interval whose exchange collar does not meet the periodic seam for small enough `a`.

Equivalently, state the theorem first on the infinite lattice `Z` and recover the periodic-ring version by large-ring stabilization.

### Sampling map

Use the isometric one-particle sampling map

```math
(\iota_a\phi)_{n,s}=a^{1/2}\phi_s(an),
```

so that `ell^2` lattice norms approximate `L^2` norms:

```math
\sum_{n,s}|(\iota_a\phi)_{n,s}|^2
\approx
\int \sum_s |\phi_s(x)|^2 dx.
```

If earlier papers use unnormalized sampling, V2 Paper 1 should either translate them to this convention or state the conversion explicitly.

### Discrete lapse samples

For smooth compactly supported lapse profiles, set

```math
N_n=N(an),
\qquad
M_n=M(an),
```

or, for bond-centered expressions,

```math
N_{n+1/2}=N(a(n+1/2)),
\qquad
M_{n+1/2}=M(a(n+1/2)).
```

The theorem must specify which convention is used. Different conventions should differ only by controlled `O(a)` errors if the construction is robust.

### Tangential target

The target operator is

```math
K_\parallel[\beta]
=\left(\beta\partial_x+\frac12\partial_x\beta\right)(I-\alpha),
\qquad
\beta=N\partial_xM-M\partial_xN.
```

Convergence should be strong convergence on the dense test domain `C_c^infty(R,C^2)`, not operator-norm convergence on the full Hilbert space, because the target is a first-order differential operator.

## The Main Scaling Problem

The finite coefficients have powers of `a` inherited from the Dirac kinetic term:

```math
A_n^{(1)}=O(a^{-2}),
\qquad
[A_n^{(1)},A_{n+r}^{(1)}]=O(a^{-4}).
```

This makes the normalization nontrivial. One cannot guess the spatial renormalization from an entrywise matrix limit, because the entrywise limit is known to fail. The normalization must be derived from the bond-centered strip action and its first moment.

The finite-slab parameter has its own problem. The Dirac Hamiltonian norm scales like `O(a^{-1})`, so a fixed `Delta` is not uniformly small as `a -> 0`. Any finite-`Delta` theorem must either:

1. extract the formal `Delta` coefficient first, then take `a -> 0`; or
2. impose a coupled thin-slab scaling such as `Delta/a -> 0` or another condition strong enough to control the expansion remainder.

This is why Tier 1 should precede Tier 2.

## Candidate Coefficient-Level Definition

Suppose the exact translated exchange coefficient admits a strip decomposition

```math
C_{n,n+r}^{(\mu)}=
\sum_{\chi} q_{r,\chi}(a)X_{n,r,\chi},
```

where `X_{n,r,chi}` are antisymmetric bond- or strip-centered difference operators and `q_{r,chi}(a)` are exact coefficient weights.

Define the smeared coefficient-level curvature by

```math
\mathcal C_a[N,M]
=
\sum_{n}\sum_{r,\chi}
\bigl(N_nM_{n+r}-M_nN_{n+r}\bigr)
q_{r,\chi}(a)X_{n,r,\chi},
```

with the sum restricted to the active strip channels proved in the finite coefficient papers.

The desired Taylor mechanism is

```math
N_nM_{n+r}-M_nN_{n+r}
=
ra\,(N\partial_xM-M\partial_xN)(an)+O(a^2).
```

The strip operator action contributes the bond-centered difference part. The first moments of the strip coefficients must combine to give the `1` and `1/2` weights in

```math
\beta\partial_x+\frac12\partial_x\beta.
```

This is the exact place where the earlier strip-moment papers enter.

## Required Lemmas

### Lemma 1: canonical strip decomposition

For the relevant translated singleton and finite-support coefficient classes, express the active exchange coefficient in a common finite strip-channel basis.

Known status: proved for leading singleton and first non-leading singleton cases; conditional for broad support prototypes.

V2 burden: identify the minimal strip family needed for the first theorem and prove closure for that family without assuming a broader unproved classification.

### Lemma 2: moment identities

Compute the normalized zeroth and first strip moments of the active channels and prove that they yield exactly the tangential operator coefficients.

Known status: first moment data are available in the leading and first non-leading singleton cases.

V2 burden: assemble them into one continuum estimate with a single sampling convention and normalization.

### Lemma 3: Taylor remainder bound

For `N,M,phi in C_c^infty`, prove that the difference between the discrete smeared strip action and the continuum operator is bounded by a controlled power of `a`.

This is a standard finite-difference estimate, but it must be written with the exact spinor strip operators used by the ISP coefficients.

### Lemma 4: regulator normalization

For the `lambda` family, prove that the normalized coefficient-level curvature satisfies

```math
c_\lambda^{-2}\mathcal C_a^{(\lambda)}[N,M]
=
\mathcal C_a^{(1)}[N,M]+\text{controlled error},
```

at the theorem's stated scope.

Known status: exact at leading order and at the first non-leading singleton strip-moment level.

V2 burden: decide whether the theorem covers only those exact scopes or proves a larger common-onset class.

### Lemma 5: finite-slab remainder control

If Tier 2 is attempted, prove that after normalization the remainder

```math
O(\Delta^{2\mu+2})
```

vanishes in the coupled `a,Delta` limit. This requires bounds on the `a`-dependence of higher coefficients.

Expected condition: something like `(Delta/a)^2 -> 0`, though the exact condition must be derived.

Known status: not proved in the current stack.

## Recommended Theorem Statements

### Theorem A: coefficient-level collar-excision theorem

For collar-excision singleton-supported free Dirac exchange coefficients, the normalized bond-centered smeared curvature operator converges strongly on `C_c^infty(R,C^2)` to

```math
K_\parallel[N\partial_xM-M\partial_xN].
```

This theorem should be the first hard target.

### Theorem B: coefficient-level `lambda`-family theorem

For `0<lambda<=1`, the same coefficient-level limit holds after division by `c_lambda^2`, at every strip-moment scope where the exact lambda-family scaling has been proved.

This should be stated carefully. If only leading and first non-leading singleton moments are known, then the theorem should not pretend to cover all supports and all higher orders.

### Theorem C: finite-slab collar-excision theorem

For a specified smooth-lapse finite deformation rule and a specified coupled scaling `Delta(a)`, the normalized finite exchange defect converges to the same tangential operator.

This theorem should be attempted only after Theorem A and the necessary remainder estimates.

### Theorem D: finite-slab admissible-regulator theorem

For a structural admissible class of regulators, the finite-slab theorem is regulator-independent after onset normalization.

This is too broad for the first V2 paper unless the admissible class is kept narrow.

## The Best Scope For V2 Paper 1

The best first version is not the strongest imaginable theorem. It is this:

> Prove Theorem A and Theorem B for the exact leading and first non-leading singleton strip data already available, while formulating Theorem C as the next finite-slab extension and listing the precise remainder estimates it requires.

This would be a real advance because it would convert the existing finite coefficient papers into a single continuum operator theorem on smooth data. It would also avoid overclaiming all-support/all-order regulator stability.

## Proof Strategy

1. **Normalize notation.** Put the free lattice, spinor basis, sampling convention, and large-ring condition in one place.
2. **Restate exact finite inputs.** Import the comparison-map expansion, support filtration, leading coefficient, distance-two/distance-three exchange coefficients, and `lambda` scaling as propositions.
3. **Define smeared coefficient curvature.** Build the operator from exact translated strip coefficients and sampled lapse profiles.
4. **Compute discrete antisymmetry.** Show that `N_nM_{n+r}-M_nN_{n+r}` gives the sampled beta field to first order in `a`.
5. **Evaluate strip action.** Apply the exact strip basis to `iota_a phi` and use Taylor expansion to recover `beta partial_x phi + (1/2)(partial_x beta)phi`, including the spin projector `(I-alpha)`.
6. **Prove error estimates.** Bound the residual by a finite number of derivatives of `N`, `M`, and `phi`.
7. **Insert regulator normalization.** Use `c_lambda` identities and strip-moment equality to prove regulator independence at the stated scope.
8. **State finite-slab extension conditions.** Record exactly which coefficient-growth and remainder bounds are still needed for a true finite-slab theorem.

## Main Risks

### Risk 1: no canonical smooth-lapse comparison maps

The finite papers define `J_R` for finite regions. A smooth-lapse theorem needs either coefficient-level smearing or a new weighted deformation rule. If this choice is not made carefully, the theorem will be ambiguous.

Mitigation: prove coefficient-level curvature first, where the smearing is over exact translated coefficient data.

### Risk 2: contact terms survive

The `d=1` and `d=2` exchange floors may produce local contact terms. The theorem must show either that they combine into the desired bond-centered operator or that a principled subtraction/renormalization removes non-geometric contact artifacts.

Mitigation: keep the active strip decomposition explicit and track every zeroth and first moment.

### Risk 3: finite-slab remainders are nonuniform in `a`

Because `H_D=O(a^{-1})`, a fixed slab size is not uniformly perturbative. Formal coefficient convergence does not automatically imply finite-slab convergence.

Mitigation: separate Tier 1 and Tier 2. Require a coupled thin-slab condition for Tier 2.

### Risk 4: regulator stability stops at the tested cases

The `lambda` family behaves well at leading and first non-leading singleton strip-moment level, but raw nonuniversality is real.

Mitigation: state the theorem only at the exact strip-moment scopes already proved, or add new coefficient computations before broadening.

### Risk 5: the limit is basis/lift dependent

The theorem uses the fixed position-spin configuration basis and the Born-squared kernel. That is appropriate for the current free benchmark, but it should not be advertised as basis-independent QFT reconstruction.

Mitigation: keep the theorem as a free benchmark theorem and defer representation-independence questions to V2 Paper 6.

## Concrete Work Products

V2 Paper 1 should include the following artifacts.

1. **Theorem ledger.** A table listing which finite results are used as exact input and which are newly proved.
2. **Notation table.** `a`, `Delta`, `L(a)`, `iota_a`, `N_n`, `M_n`, `beta`, `c_lambda`, `R_a`, `Z_{a,Delta}`.
3. **Strip-channel table.** Active channels, coefficient weights, zeroth moments, first moments, and regulator scaling factors.
4. **Sampling lemma.** Strong convergence of the exact strip action on `C_c^infty` sampled profiles.
5. **Regulator lemma.** Exact `lambda` normalization at the included strip scopes.
6. **Failure appendix.** Explicitly show why site-centered entrywise convergence fails and why fixed `Delta` is not a safe continuum scaling.
7. **Optional validation script.** A small pure-stdlib script that numerically samples smooth compactly supported `N`, `M`, and `phi` on increasing lattices and checks convergence of the exact strip-channel operator, not the full finite-slab defect.

## Minimal Pass/Fail Criteria

Pass if V2 Paper 1 proves at least:

```math
R_a\mathcal C_a[N,M]\iota_a\phi
\to
\iota_a K_\parallel[N\partial_xM-M\partial_xN]\phi
```

for collar-excision coefficient-level curvature, with explicit normalization and error bounds.

Stronger pass if the same theorem includes the normalized `lambda` family.

Full pass if it also proves a finite-slab version for a coupled `Delta(a)` scaling.

Fail if:

- no canonical smeared curvature can be defined from the exact finite data;
- contact terms cannot be controlled;
- the continuum operator depends on regulator details after normalized strip moments are included;
- the required remainders diverge under every physically meaningful thin-slab scaling.

## Relation To Gravity

None. This paper is non-gravitational.

If the theorem succeeds, it shows that relativistic ISP has a regulator-stable stochastic analogue of the hypersurface-deformation bracket in the simplest free setting. That is a prerequisite for later metric reconstruction. It is not metric reconstruction and not dynamical geometry.

## Recommended Immediate Next Step

Write V2 Paper 1 around Theorem A first:

`Coefficient-Level Free Stochastic Curvature in Relativistic ISP`

Then add a final section titled:

`From Coefficients to Finite Slabs: the Remaining Uniformity Burden`

That structure would keep the paper honest. It would deliver the first continuum stochastic-curvature theorem while making clear why the full finite-slab and general-regulator versions still require additional estimates.
