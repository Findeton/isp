# Investigation: From Stochastic Curvature to Gravity

Author: Felix Robles Elvira

Date: 2026-05-12

Purpose: investigate whether the first-principles ISP leap can honestly become a route toward unifying gravity and quantum physics. The rule of this memo is conservative: gravity is not allowed to enter as a slogan. It enters only if the stochastic-curvature structure first earns the mathematical role played by hypersurface geometry.

## Verdict

The path is scientifically interesting, but gravity is not yet earned.

The existing ISP stack supports this narrower claim:

> Exact finite stochastic kernels, localized comparison maps, and exchange defects may provide a probability-first route to relativistic quantum integrability.

It does not yet support this stronger claim:

> The same structure already gives quantum gravity or dynamical spacetime.

The bridge to gravity becomes legitimate only if exchange-defect curvature can do more than reproduce a flat-background tangential bracket in a free model. It must begin to reconstruct, or at least operationally identify, the spatial metric data that appear in the hypersurface-deformation algebra.

The immediate target is therefore not "quantize gravity." The immediate target is:

> Show that stochastic exchange curvature determines the geometric structure functions of hypersurface deformation.

If that works, gravity becomes the next rational question. If it fails, the program may still be a strong probability-first reformulation of quantum dynamics, but not a unification route.

## What Is Already Earned

The corpus currently earns four important ingredients.

1. **Finite-kernel primacy.** Relativistic ISP is organized around exact kernels between Cauchy hypersurface configuration spaces, not around a preferred time-slice generator.

2. **Localized comparison maps.** A bounded deformation region `R` defines an algebraic relative map

```math
J_R = \Gamma_R \Gamma_0^{-1},
```

where the inverse is algebraic and need not be stochastic.

3. **Exchange defects.** Two localized deformation regions define an order-comparison datum

```math
E_{R,S} = J_{S|R} J_R (J_{R|S}J_S)^{-1}.
```

The free-model papers show that this defect is not arbitrary noise. At leading order it is boundary/strip controlled, and after bond-centered renormalization it yields a tangential pseudo-generator of the form

```math
K_parallel[\beta]
  = (\beta \partial_x + \tfrac12 \partial_x\beta)(I-\alpha),
\qquad
\beta = N\partial_x M - M\partial_x N.
```

4. **Gauge and locality bookkeeping.** The gauge papers show that exact finite stochastic kernels can carry Gauss-sector block structure, boundary-flux centers, and center-resolved locality. The induced-net papers show how exchange-trivial or commuting operational layers imply finite Einstein-causality statements at benchmark scope.

These are real. They make the stochastic-curvature idea worth investigating.

## What Is Not Yet Earned

The present stack does not yet earn any of the following:

1. A full continuum QFT reconstruction theorem.
2. A nontrivial Lorentz-covariant stochastic functor beyond finite relabeling/projective templates.
3. A full Dirac-Schwinger algebra in an interacting field theory.
4. A metric reconstructed from `Gamma`-level data.
5. Dynamical geometry.
6. Einstein's equations.
7. A quantum-gravity Hilbert space, path integral, spin foam, causal set, or canonical constraint theory.

The honest status is: the free exchange-defect result touches the same algebraic interface where QFT and gravity meet, but only at the first foothold.

## The Conceptual Hinge

The hinge is the normal-normal surface-deformation bracket:

```math
[H[N],H[M]] = D[\beta],
\qquad
\beta^i = h^{ij}(N\partial_j M - M\partial_j N).
```

For ordinary QFT on a fixed background, `h^{ij}` is fixed geometry. For canonical general relativity, `h^{ij}` is a dynamical phase-space field. This distinction is the whole gravity question.

The ISP program currently aims at the left side of the hinge: can exact stochastic exchange defects reproduce the hypersurface-deformation bracket at all?

Gravity begins only on the right side: can the same stochastic data identify `h^{ij}` as an emergent, variable, dynamically constrained object?

So the key research question is:

> Can the coefficient of the stochastic exchange curvature be read as an inverse spatial metric, rather than inserted from outside?

That is the first true gravity gate.

## Minimal Mathematical Formulation

Let `Hyp(M)` be a suitable class of Cauchy hypersurfaces or regulated hypersurface embeddings. Over each `Sigma`, place a configuration set `C_Sigma` and probability simplex `Delta(C_Sigma)`. A stochastic connection is a rule assigning to a finite slab or path `gamma: Sigma_0 -> Sigma_1` a stochastic kernel

```math
\Gamma_\gamma : \Delta(C_{\Sigma_0}) \to \Delta(C_{\Sigma_1}).
```

Localized deformations define relative transports `J_R`. Their group-commutator type defect is the finite curvature two-cell.

The continuum target is not simply that curvature vanishes. The target is that the exchange of two normal deformations is equivalent to a tangential deformation:

```math
\mathcal F(N,M) = K_i[h^{ij}(N\partial_jM - M\partial_jN)]
```

after the correct normalization, continuum limit, and quotient by representation/lift gauge.

The stochastic connection is therefore viable only if these objects can be defined without smuggling in Hilbert-space phase, circuit structure, or a background metric beyond the hypotheses of the test being run.

## Gate 1: Free Stochastic Curvature Theorem

**Question.** Does the 1+1D free Dirac finite-kernel exchange defect have a regulator-independent continuum limit as a tangential deformation operator?

**Current status.** Partially supported. Existing papers give exact finite leading coefficients, rule non-uniqueness, onset-renormalized leading universality, and a bond-centered tangential operator. The missing step is uniform continuum control.

**The theorem needed.** For smooth compactly supported `N`, `M`, and test spinor profile `phi`, prove

```math
\lim_{a\to 0} Z_a\bigl(E_{N,M}(a,\Delta)-I\bigr)\iota_a\phi
 = K_parallel[N\partial_xM-M\partial_xN]\phi
```

with a precise relation between `a`, `Delta`, normalization `Z_a`, support sampling, admissible regulator class, and error bounds.

**Pass condition.** A theorem with explicit estimates, not just coefficient matching.

**Fail condition.** The limit depends on the microscopic localized-deformation rule, the normalization, the support sampling, or the order in which `a` and `Delta` are taken.

**Meaning for gravity.** Passing Gate 1 does not give gravity. It only proves that stochastic curvature can reproduce the first relativistic integrability datum in the simplest free setting.

## Gate 2: Metric-from-Stochastic-Curvature Lemma

This is the first genuine conceptual leap toward gravity.

**Question.** In more than one spatial dimension, can the exchange curvature determine the tensor `h^{ij}` in

```math
\beta^i = h^{ij}(N\partial_jM - M\partial_jN)?
```

**Lemma schema.** Suppose a continuum stochastic-curvature limit defines a bilinear antisymmetric map

```math
B(N,M) = \mathcal F(N,M)
```

and suppose there is a faithful tangential representation `K_i[v^i]`, meaning `K_i[v^i]=0` only for geometrically trivial shifts. If, locally,

```math
B(N,M) = K_i[C^{ij}(x)(N\partial_jM - M\partial_jN)]
```

for all compactly supported `N,M`, and if `C^{ij}` is symmetric, positive, and transforms tensorially under changes of hypersurface coordinates, then `C^{ij}` can be identified as an inverse spatial metric or inverse metric density, depending on the normalization convention.

**Why this matters.** The Dirac-Schwinger bracket contains the spatial metric as a structure function. If stochastic curvature can recover that coefficient from `Gamma`-level data, then geometry has become visible inside the stochastic connection.

**Pass condition.** A 2+1D or 3+1D free-field benchmark in which the extracted coefficient transforms as `h^{ij}` and is not manually inserted into the comparison-map definition except as part of a controlled fixed-background test.

**Fail condition.** The coefficient is regulator-dependent, non-tensorial, not positive, not symmetric, or only recoverable by adding Hilbert-space/lift data not determined by the stochastic connection.

**Meaning for gravity.** Passing Gate 2 would justify saying that ISP has a route to emergent spacetime geometry. It still would not give dynamical gravity.

## Gate 3: Fixed Curved Background Test

**Question.** Can the stochastic-curvature construction work on a fixed curved spacetime background, where `h^{ij}(x)` varies with position?

**Setup.** Use a conservative regulated model: for example, a Dirac or scalar field on a fixed curved 1+1D or 2+1D background, or a Regge-like spatial discretization with known local metric data. Define finite hypersurface configuration spaces, reference kernels, localized deformations, and exchange defects.

**Required result.** The normalized exchange curvature must recover

```math
\beta^i(x) = h^{ij}(x)(N\partial_jM - M\partial_jN)
```

with local error control and correct behavior under refinement.

**Pass condition.** The extracted `h^{ij}(x)` agrees with the known background metric in the continuum/refinement limit.

**Fail condition.** The construction only works in flat coordinates, or it requires a preferred slicing not removable by covariance/functoriality data.

**Meaning for gravity.** Passing Gate 3 would show that stochastic curvature can see background geometry. It still would not make geometry dynamical.

## Gate 4: Stress-Energy and Response

Gravity couples to energy and momentum, not merely to geometry labels. Before dynamical spacetime is attempted, the stochastic program needs a response theorem.

**Question.** Does varying the background geometric data in the stochastic connection produce a conserved stress-energy-like response?

In ordinary QFT, stress-energy appears as the response to metric variation and obeys conservation identities tied to diffeomorphism invariance. The stochastic analogue should identify a response functional

```math
T_{ij}^{ISP} \sim \frac{\delta \log \mathcal W[\Gamma,J,E]}{\delta h^{ij}}
```

or a purely finite-kernel replacement for such a variation. The symbol `\mathcal W` is deliberately schematic: the program must decide whether the varied object is likelihood, entropy production, exchange curvature, an induced action, or a reconstruction functional.

**Pass condition.** A Ward-identity-like conservation statement follows from stochastic hypersurface-deformation consistency, not from importing a Hilbert-space stress tensor by hand.

**Fail condition.** Stress-energy cannot be defined without returning to ordinary amplitude-level QFT as primitive.

**Meaning for gravity.** Passing Gate 4 would make a semiclassical-gravity question meaningful. It would still not prove Einstein dynamics.

## Gate 5: Dynamical Geometry

Only here should the program say it is investigating gravity directly.

**Question.** Can geometry be included among the configuration variables while preserving stochastic-kernel primacy and hypersurface-deformation closure?

A conservative finite version would enlarge the hypersurface configuration space from matter data to joint matter-geometry data:

```math
C_\Sigma^{total} = C_\Sigma^{matter} \times C_\Sigma^{geom}.
```

Examples of finite geometry data could include Regge edge lengths, discrete triad variables, causal-cell adjacency labels, or other regulated spatial-geometry variables. The primitive object would be a stochastic kernel on this enlarged configuration space, not a wave functional on metrics assumed at the start.

The closure target becomes anomaly freedom of stochastic hypersurface-deformation curvature:

```math
\mathcal F_{total}(N,M)
  = K_i^{total}[h^{ij}(q)(N\partial_jM - M\partial_jN)]
```

where `q` denotes the geometry configuration.

**Pass condition.** The stochastic exchange law closes with a geometry-dependent structure function, has a consistent gauge/redundancy quotient, and reduces to known matter QFT on fixed backgrounds when geometry is frozen.

**Fail condition.** Closure requires arbitrary nonlocal data, violates stochastic positivity at the finite-slab level, or cannot define a projective/refinement limit.

**Meaning for gravity.** Passing Gate 5 would justify calling the program a candidate quantum-gravity framework.

## Gate 6: Einstein Dynamics and Physical Limits

Even a stochastic geometry with dynamical metric variables is not yet general relativity. It must recover the correct physical limits.

The long-range requirements are:

1. **Hamiltonian/momentum constraint limit.** The stochastic closure conditions must reproduce the gravitational constraint algebra in a representation where geometry variables are dynamical.
2. **Semiclassical limit.** Suitable coarse states must satisfy something like

```math
G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,\langle T_{\mu\nu}\rangle
```

or a clearly specified correction to it.

3. **Newtonian/weak-field limit.** The framework must recover Poisson gravity and weak gravitational time dilation in an appropriate limit.
4. **Linearized spin-2 limit.** Around flat backgrounds, the dynamical geometry excitations must behave like the correct massless spin-2 degrees of freedom, or the theory must explicitly explain why the low-energy limit differs.
5. **No preferred foliation.** Predictions must be independent of the hypersurface path used to compute them, up to the permitted stochastic gauge equivalences.
6. **Matter compatibility.** Gauge fields, fermions, and interacting matter must couple to the same geometry data that appear in the stochastic curvature bracket.

These are not optional. Without them, one may have a stochastic geometry, but not a viable unification of gravity and quantum physics.

## The Most Important New Theorem Target

The next theorem after the 1+1D free stochastic-curvature theorem should be:

### Metric Reconstruction from Stochastic Exchange Curvature

For a regulated free relativistic field in at least two spatial dimensions, assume exact finite stochastic kernels and localized deformation maps satisfy quasilocal filtration, invertibility in a common small-slab regime, and a regulator-stable bond/face-centered exchange-curvature limit. Then the normal-normal stochastic exchange curvature defines a local bilinear map on lapse pairs. If this map is faithful modulo tangential relabelings and first-order in derivatives of the lapses, its coefficient is a symmetric contravariant tensor density. Under the fixed-background benchmark hypotheses, that tensor density is the inverse spatial metric density of the background.

This theorem would not be gravity yet. It would be the first theorem saying: the stochastic connection can see metric geometry.

## Why The Dirac-Schwinger Interface Is Special

The Dirac-Schwinger or hypersurface-deformation algebra is the right place to look because it is shared by three things:

1. Relativistic field evolution on arbitrary hypersurfaces.
2. Foliation independence and no-superluminal-signaling structure.
3. Canonical general relativity, where the spatial metric enters the algebra as a dynamical structure function.

But this also makes it easy to overclaim. Reproducing the algebra on a fixed background gives relativistic covariance. It does not automatically give Einstein dynamics. To reach gravity, the ISP program must explain why the structure function is itself a stochastic degree of freedom and why its dynamics reduce to general relativity.

## Main Objections To Track

1. **Gamma insufficiency.** `Gamma` may not contain enough information to recover local energy, phase, spin connection, or stress-energy.
2. **Lift ambiguity.** Different Hilbert/circuit realizations may share the same stochastic connection but differ physically.
3. **Regulator dependence.** The exchange-curvature limit may depend on local deformation rules or discretization details.
4. **Finite covariance obstruction.** Finite stochastic isomorphisms with stochastic inverses are only permutations, so nontrivial boosts require projective/refinement/continuum structure.
5. **Raw-versus-observable confusion.** Raw comparison maps are not local observables. Locality claims must pass through operational or induced-effect structures.
6. **Anomaly risk.** Constraint/hypersurface-deformation closure can fail after quantization or stochastic coarse-graining.
7. **Dynamical-metric overreach.** A background metric appearing in a bracket is not a gravitational field unless it can vary and obey dynamics.

These objections are not discouraging. They are the experiment. A rigorous program should try to make one of them fail decisively.

## Immediate Work Program

The next work should proceed in this order.

1. **Formalize stochastic connection language.** Define the bundle over hypersurfaces, slab-path transports, localized relative maps, gauge equivalences, and finite curvature two-cells precisely.

2. **Prove the 1+1D free stochastic-curvature theorem.** Convert existing coefficient and leading-universality results into a uniform continuum theorem with explicit estimates.

3. **Build a 2+1D flat-background benchmark.** Use the simplest free relativistic lattice model where the bracket has multiple spatial directions. Extract whether the coefficient of `N partial_j M - M partial_j N` behaves like `h^{ij}`.

4. **State and test the metric-reconstruction lemma.** Decide which assumptions are mathematical necessities and which can be verified from exact finite kernels.

5. **Search for lift counterexamples.** Try to construct two stochastic connections with identical exchange curvature but inequivalent local QFT physics. If such examples exist under the proposed axioms, the invariant is incomplete.

6. **Only then attempt fixed curved backgrounds.** The first curved-background test should be a reconstruction test, not a dynamical-gravity claim.

7. **Only after that attempt dynamical geometry.** Introduce finite geometry variables and ask whether stochastic exchange closure selects a gravitational constraint structure.

## Decision Rule

Do not move to a gravity paper until Gates 1 and 2 are substantially passed.

The next legitimate paper is not yet `Gravity from ISP`. It is:

`Metric Data from Stochastic Exchange Curvature`

or, more conservatively:

`The Hypersurface-Deformation Test for Relativistic ISP`.

If that paper succeeds, the gravity program becomes scientifically motivated. If it fails, the failure will still be valuable because it will locate exactly where stochastic transition data stop short of spacetime geometry.

## Bottom Line

The unification path is real enough to investigate, but it is a path through a narrow mathematical gate:

> stochastic exchange curvature -> hypersurface-deformation structure -> metric reconstruction -> background curved covariance -> stress-energy response -> dynamical geometry -> Einstein/quantum-gravity limits.

Right now the program is between the first and second arrows. The next rigorous leap is not to add gravity. It is to show that the exchange curvature can reconstruct metric data.
