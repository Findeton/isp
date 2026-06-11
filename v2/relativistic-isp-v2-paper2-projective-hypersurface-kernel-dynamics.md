# Projective Hypersurface Kernel Dynamics for Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

V2 Paper 2 consolidated draft

Date: 2026-05-13

Status: theorem-framework draft. This paper supplies the projective/refinement language needed after the free stochastic-curvature theorem and before interacting inverse-control estimates. It proves exact naturality theorems for primitive kernels, comparison maps, and exchange defects, and it states the asymptotic error-propagation version that later continuum papers will actually need.

## Abstract

The finite relativistic ISP benchmark stack proves exact statements on fixed regulated configuration spaces. That is not yet a continuum covariance structure. On a finite set, a stochastic isomorphism whose inverse is stochastic is only a permutation, so nontrivial covariance across changed hypersurfaces, lattices, cutoffs, or support discretizations cannot be obtained from finite stochastic relabeling alone.

This paper defines regulated hypersurface configuration systems, projective states, cylinder effects, projectively compatible endpoint kernels, localized deformation kernels, comparison maps, and exchange defects. The central theorem is a naturality theorem: if reference and localized finite kernels are compatible under coarse-graining, then the induced comparison maps and exchange defects are compatible under the same coarse-graining. A second theorem gives the corresponding error bounds when compatibility holds only asymptotically.

The result does not prove Lorentz covariance, a continuum QFT reconstruction, a Haag-Kastler net, gauge-cutoff convergence, or interacting locality. Its role is more basic: it says what it would mean for the finite ISP kernels and exchange defects in different regulators to be representatives of the same continuum-directed stochastic dynamics.

## 1. Scope And Non-Claims

Established here:

1. finite stochastic isomorphisms cannot carry nontrivial continuum covariance by themselves;
2. projective regulated hypersurface configuration systems can be defined with stochastic coarse-graining maps;
3. compatible kernel families act on projective states and cylinder effects;
4. comparison maps inherit exact projective compatibility from primitive reference and localized kernels;
5. exchange defects inherit exact projective compatibility from comparison maps;
6. approximate projective compatibility propagates to comparison maps and exchange defects under explicit inverse-control bounds;
7. foliation compatibility can be stated as equality of projective endpoint morphisms, or as equality modulo a separately specified projective tangential correction.

Not proved here:

1. existence of a nontrivial Lorentz-covariant continuum ISP;
2. exact block-spin compatibility of the free Dirac lattice kernels;
3. a primitive smooth-lapse kernel theorem beyond V2 Paper 1's log-smeared finite-slab construction;
4. interacting quasilocality or uniform inverse control;
5. gauge-cutoff, volume, or compact-rotor convergence;
6. continuum Haag-Kastler reconstruction;
7. metric reconstruction or gravity.

The point is infrastructure, not a new physics result. In particular, projective naturality is a compatibility language, not a Lorentz-covariance theorem. A covariance theorem would still have to construct physically meaningful regulator changes for a class of hypersurface deformations and prove that the associated endpoint laws satisfy the exact or asymptotic naturality conditions below. Paper 3 can now ask whether interacting finite-range systems satisfy the inverse and locality hypotheses exported below.

## 2. Dependency Ledger From The Current Corpus

The framework uses the following established finite inputs.

1. `relativity-indivisible-rewrite.html` supplies hypersurface kernels, finite localized deformations, comparison maps, exchange defects, the indivisibility warning, and the finite-stochastic-isomorphism obstruction.
2. `collar-excision-exchange-defect.html`, `exact-localized-finite-deformations-free-dirac-exchange-defect.html`, and the bond-centered sequel papers supply exact free one-particle fixed-regulator exchange-defect data.
3. `relativistic-isp-v2-paper1-free-stochastic-curvature-theorem.md` proves the first continuum-facing exchange-curvature theorem at the free one-particle scope.
4. `localized-controls-detectors-operational-relativity-isp.html`, `einstein-causality-bridge-exchange-defect-haag-kastler-relativistic-isp.html`, and `boundary-flux-resolved-einstein-causality-relativistic-isp.html` motivate the dual cylinder-effect language and the raw/operational/observable separation.
5. The Fock and gauge benchmark papers show why later projective systems must allow sector labels, centers, and cutoff maps; they do not yet supply cutoff-uniform continuum theorems.

This paper deliberately does not import Hilbert-space locality, Haag-Kastler axioms, or Markov divisibility as primitive assumptions.

## 3. Finite Stochastic Isomorphisms Are Only Relabelings

Let `V_C=R^C` for a finite configuration set `C`. A matrix `T:V_C -> V_D` is column-stochastic if its entries are nonnegative and `1_D^T T=1_C^T`.

### Lemma 1: finite stochastic isomorphism obstruction

If `T` is a square column-stochastic matrix and both `T` and `T^{-1}` are column-stochastic, then `T` is a permutation matrix.

Proof. Since `T,T^{-1}` have nonnegative entries and `TT^{-1}=I`, for `i != j`

```math
0=(TT^{-1})_{ij}=\sum_k T_{ik}(T^{-1})_{kj}.
```

Every summand is nonnegative, so if `T_{ik}>0`, then `(T^{-1})_{kj}=0` for every `j != i`. Thus one positive entry in column `k` of `T` forces row `k` of `T^{-1}` to be supported only at `i`. If the same column of `T` had another positive entry `T_{\ell k}>0` with `\ell != i`, the same argument would force row `k` of `T^{-1}` to be supported only at `\ell`, hence row `k` would be zero, contradicting invertibility. Therefore each column of `T` has at most one positive entry. Since `T` is column-stochastic, each column has exactly one positive entry and that entry is `1`. Invertibility then forces these entries to occupy distinct rows. Hence `T` is a permutation. `square`

Therefore a nontrivial covariance theory cannot identify regulated descriptions by stochastic isomorphisms with stochastic inverses. It needs coarse-graining/refinement, embeddings, or a continuum/projective limit.

## 4. Regulated Hypersurface Configuration Systems

For each Cauchy hypersurface `Sigma`, choose a directed regulator set `I_Sigma`. A regulator `a in I_Sigma` specifies a finite configuration set

```math
C_{\Sigma,a}
```

and the real vector space

```math
V_{\Sigma,a}=R^{C_{\Sigma,a}}.
```

The probability simplex is

```math
\Delta_{\Sigma,a}
=\{p\in V_{\Sigma,a}:p_c\ge0,\;1^Tp=1\}.
```

For each refinement `a' >= a`, choose an admissible coarse-graining map

```math
P_{\Sigma,a\leftarrow a'}:V_{\Sigma,a'}\to V_{\Sigma,a}.
```

Admissibility means:

1. `P_{\Sigma,a\leftarrow a'}` is column-stochastic;
2. `P_{\Sigma,a\leftarrow a}=I`;
3. `P_{\Sigma,a\leftarrow a''}=P_{\Sigma,a\leftarrow a'}P_{\Sigma,a'\leftarrow a''}` for `a''>=a'>=a`;
4. `P_{\Sigma,a\leftarrow a'}` has full row rank whenever cylinder effects are meant to embed faithfully.

The full-row-rank clause is not cosmetic. Without it, distinct coarse effects may collapse after pullback to fine regulators.

For deterministic refinement there is a restriction map of configurations

```math
r_{\Sigma,a\leftarrow a'}:C_{\Sigma,a'}\to C_{\Sigma,a}
```

and

```math
[P_{\Sigma,a\leftarrow a'}]_{c,c'}=1
\quad\Longleftrightarrow\quad
c=r_{\Sigma,a\leftarrow a'}(c').
```

Stochastic coarse-graining is also allowed, but then the physical meaning of the induced cylinder effects must be stated.

## 5. Projective States And Cylinder Effects

A projective state on `Sigma` is a family

```math
p_\Sigma=(p_{\Sigma,a})_{a\in I_\Sigma},
\qquad p_{\Sigma,a}\in\Delta_{\Sigma,a},
```

such that

```math
P_{\Sigma,a\leftarrow a'}p_{\Sigma,a'}=p_{\Sigma,a}
```

for every `a' >= a`.

This is a finite-regulator version of cylinder-measure consistency. It does not by itself assert that there is a countably additive continuum measure on an infinite configuration space. Such a statement would require separate compactness, standard-Borel, or Kolmogorov-extension hypotheses.

The dual pullback

```math
P_{\Sigma,a\leftarrow a'}^*:
V_{\Sigma,a}^*\to V_{\Sigma,a'}^*
```

maps a coarse effect to a fine cylinder effect. Two effects `e_a in V_{\Sigma,a}^*` and `e_b in V_{\Sigma,b}^*` represent the same cylinder effect if there exists a common refinement `c >= a,b` such that

```math
P_{\Sigma,a\leftarrow c}^*e_a
=
P_{\Sigma,b\leftarrow c}^*e_b.
```

Operational covariance statements should be made on these cylinder-effect classes, not on a single regulator's effect space.

## 6. Projective Endpoint Kernels

For two hypersurfaces `Sigma_0,Sigma_1`, a regulated endpoint kernel is a column-stochastic map

```math
\Gamma_{\Sigma_1\leftarrow\Sigma_0}^{a_1,a_0}
:
V_{\Sigma_0,a_0}\to V_{\Sigma_1,a_1}.
```

When a common regulator index is available, write it as `Gamma^a`. In general one should allow a cofinal directed set of compatible pairs `(a_1,a_0)`.

In the equal-index notation, exact projective compatibility is the naturality square

```math
P_{\Sigma_1,a\leftarrow a'}
\Gamma_{\Sigma_1\leftarrow\Sigma_0}^{a'}
=
\Gamma_{\Sigma_1\leftarrow\Sigma_0}^{a}
P_{\Sigma_0,a\leftarrow a'}.
```

This square compares different regulators for the same endpoint stochastic law. It is not a Markov-composition axiom through intermediate hypersurfaces.

The ISP-divisibility axiom that must not be imposed is

```math
\Gamma_{\Sigma_2\leftarrow\Sigma_0}
=
\Gamma_{\Sigma_2\leftarrow\Sigma_1}
\Gamma_{\Sigma_1\leftarrow\Sigma_0}.
```

Such a factorization may hold in special divisible cases, but it is not part of the projective framework.

## 7. Localized Kernels And Support Systems

A regulated support system for a spacetime or hypersurface region `R` is a family

```math
R_a\subset \mathcal L_{\Sigma,a},
```

where `\mathcal L_{\Sigma,a}` denotes the finite set of regulated cells, links, modes, or local degrees of freedom on `Sigma`. This distinction matters: `C_{\Sigma,a}` is the set of full configurations, while `R_a` labels where a deformation is supported. In constrained gauge sectors, a region label need not define an independent tensor factor of `V_{\Sigma,a}`.

The support family is compatible if the coarse image of `R_{a'}` lies inside `R_a` up to a declared collar:

```math
\rho_{\Sigma,a\leftarrow a'}(R_{a'})
\subseteq
N_{\ell(a,a')}(R_a).
```

Here `\rho_{\Sigma,a\leftarrow a'}` is the induced coarse-graining map on regulated cells or local degrees of freedom, not the probability coarse-graining map `P_{\Sigma,a\leftarrow a'}` on full configuration distributions.

The collar allowance is needed because localized finite deformations in the free and gauge papers naturally carry boundary strips.

A localized endpoint kernel is a family

```math
\Gamma_{R_a}^a:V_{\Sigma_0,a}\to V_{\Sigma_1,a}
```

with the same naturality requirement:

```math
P_{\Sigma_1,a\leftarrow a'}\Gamma_{R_{a'}}^{a'}
=
\Gamma_{R_a}^aP_{\Sigma_0,a\leftarrow a'}.
```

For gauge systems, this definition must usually be replaced by a center-resolved version. If `z_a` denotes a boundary-flux or center label and `q_{a\leftarrow a'}(z_{a'})=z_a`, then all maps should be defined fiberwise on

```math
V_{\Sigma,a,z_a}
```

and coarse-graining should respect the center map. A single unfibered projection is generally too crude for Gauss-law sectors.

## 8. Projective Action On States And Effects

### Theorem 1: projective kernel action

Let `Gamma^a:V_{\Sigma_0,a}->V_{\Sigma_1,a}` be an exact projectively compatible family of column-stochastic kernels. Then:

1. `Gamma` maps projective states on `Sigma_0` to projective states on `Sigma_1`;
2. `Gamma^*` maps cylinder effects on `Sigma_1` to cylinder effects on `Sigma_0`.

Proof. Let `p` be a projective state. For `a' >= a`,

```math
P_{\Sigma_1,a\leftarrow a'}\Gamma^{a'}p_{\Sigma_0,a'}
=
\Gamma^aP_{\Sigma_0,a\leftarrow a'}p_{\Sigma_0,a'}
=
\Gamma^ap_{\Sigma_0,a}.
```

Thus `(Gamma^ap_{\Sigma_0,a})_a` is compatible. The effect statement is the dual naturality square. `square`

## 9. Comparison-Map Naturality

Let

```math
A^a=\Gamma_0^a:V_{\Sigma_0,a}\to V_{\Sigma_1,a}
```

be a reference endpoint kernel and

```math
B_R^a=\Gamma_R^a:V_{\Sigma_0,a}\to V_{\Sigma_1,a}
```

be a localized endpoint kernel. Assume `A^a` is a linear isomorphism for the slab/regulator range under discussion. The comparison map is

```math
J_R^a=B_R^a(A^a)^{-1}:V_{\Sigma_1,a}\to V_{\Sigma_1,a}.
```

Since `A^a` and `B_R^a` are column-stochastic, `J_R^a` preserves normalization:

```math
1^TJ_R^a=1^T.
```

It need not be stochastic. Negative entries are allowed; `J_R^a` is an algebraic pseudo-stochastic comparison map.

### Theorem 2: exact comparison-map naturality

Assume the reference and localized kernels satisfy

```math
P_1A^{a'}=A^aP_0,
\qquad
P_1B_R^{a'}=B_R^aP_0,
```

where

```math
P_i=P_{\Sigma_i,a\leftarrow a'}.
```

If `A^a` and `A^{a'}` are invertible, then

```math
P_1J_R^{a'}=J_R^aP_1.
```

Proof. From `P_1A^{a'}=A^aP_0`,

```math
(A^a)^{-1}P_1=P_0(A^{a'})^{-1}.
```

Therefore

```math
P_1J_R^{a'}
=P_1B_R^{a'}(A^{a'})^{-1}
=B_R^aP_0(A^{a'})^{-1}
=B_R^a(A^a)^{-1}P_1
=J_R^aP_1.
```

`square`

If the comparison maps are invertible and `P_1J_R^{a'}=J_R^aP_1`, then their inverses also intertwine:

```math
P_1(J_R^{a'})^{-1}=(J_R^a)^{-1}P_1.
```

This follows by multiplying the intertwining relation on the right by `(J_R^{a'})^{-1}` and on the left by `(J_R^a)^{-1}`.

## 10. Exchange-Defect Naturality

For two regulated support systems `R,S`, define

```math
E_{R,S}^a
=
J_R^aJ_S^a(J_R^a)^{-1}(J_S^a)^{-1}.
```

### Theorem 3: exact exchange-defect naturality

Under the hypotheses of Theorem 2 for `R` and `S`, and assuming `J_R^a,J_S^a,J_R^{a'},J_S^{a'}` are invertible, one has

```math
P_1E_{R,S}^{a'}=E_{R,S}^aP_1.
```

Proof. Apply Theorem 2 to `J_R` and `J_S`, apply the inverse intertwining relation to their inverses, and multiply the four intertwinings in order:

```math
P_1J_R^{a'}J_S^{a'}(J_R^{a'})^{-1}(J_S^{a'})^{-1}
=
J_R^aJ_S^a(J_R^a)^{-1}(J_S^a)^{-1}P_1.
```

`square`

Thus stochastic curvature, when represented by exchange defects, is not a single finite matrix. It is a compatible projective family of pseudo-stochastic endpoint automorphisms.

## 11. Approximate Naturality And Error Propagation

Exact projective compatibility is too strong for many continuum limits. V2 Paper 1 proves convergence of normalized exchange defects on sampled smooth profiles; it does not prove exact block-spin equality of all finite Dirac kernels. Paper 2 therefore also needs an asymptotic theorem.

### Theorem 4: error propagation under approximate naturality

Fix norms on the finite vector spaces. Suppose

```math
R_0=P_1A^{a'}-A^aP_0,
\qquad
R_R=P_1B_R^{a'}-B_R^aP_0.
```

Then the comparison-map naturality defect is exactly

```math
P_1J_R^{a'}-J_R^aP_1
=
(R_R-J_R^aR_0)(A^{a'})^{-1}.
```

Consequently,

```math
\|P_1J_R^{a'}-J_R^aP_1\|
\le
(\|R_R\|+\|J_R^a\|\|R_0\|)
\|(A^{a'})^{-1}\|.
```

This is the basic inverse-control bottleneck: small primitive-kernel refinement errors are useful only if the reference inverse and comparison map are controlled in the same norm/topology.

If

```math
\delta_R=P_1J_R^{a'}-J_R^aP_1,
```

then the inverse comparison maps satisfy

```math
P_1(J_R^{a'})^{-1}-(J_R^a)^{-1}P_1
=
-(J_R^a)^{-1}\delta_R(J_R^{a'})^{-1}.
```

Thus

```math
\|P_1(J_R^{a'})^{-1}-(J_R^a)^{-1}P_1\|
\le
\|(J_R^a)^{-1}\|\|\delta_R\|\|(J_R^{a'})^{-1}\|.
```

For the exchange defect, set

```math
X_1=J_R,\quad X_2=J_S,\quad X_3=J_R^{-1},\quad X_4=J_S^{-1},
```

and let

```math
\delta_i=P_1X_i^{a'}-X_i^aP_1.
```

Then a telescoping expansion gives

```math
P_1X_1^{a'}X_2^{a'}X_3^{a'}X_4^{a'}
-X_1^aX_2^aX_3^aX_4^aP_1
```

```math
=
\delta_1X_2^{a'}X_3^{a'}X_4^{a'}
+X_1^a\delta_2X_3^{a'}X_4^{a'}
+X_1^aX_2^a\delta_3X_4^{a'}
+X_1^aX_2^aX_3^a\delta_4.
```

Therefore asymptotic primitive-kernel naturality implies asymptotic exchange-defect naturality provided the reference inverses, comparison maps, and comparison-map inverses remain bounded in the topology being used.

This theorem is the exact handoff to Paper 3. Interacting locality is not just a Lieb-Robinson question for Hamiltonian observables; it must also control `Gamma_0^{-1}`, `J_R`, and `J_R^{-1}` after Born-squared projection and coarse-graining.

## 12. Foliation Compatibility As A Projective Statement

Let `P` and `Q` be two regulated hypersurface paths with the same endpoints. In an indivisible ISP, `P` and `Q` should assign endpoint kernels to the whole path or slab; they need not factor through every intermediate hypersurface.

An exact projective path morphism is a compatible endpoint-kernel family

```math
\Gamma_P^a:V_{\Sigma_0,a}\to V_{\Sigma_1,a}.
```

Two paths are projectively equivalent if their endpoint morphisms are equal as pro-morphisms: for every coarse endpoint regulator there is a common refinement at which the two fine representatives give the same pushed-down endpoint law.

In equal-index notation, the simplest exact condition is

```math
P_{1,a\leftarrow a'}\Gamma_P^{a'}
=
P_{1,a\leftarrow a'}\Gamma_Q^{a'}
```

as maps `V_{\Sigma_0,a'} -> V_{\Sigma_1,a}` from the same refined initial space. Equivalently, the two paths give the same outcome on every projective initial state after final coarse-graining. If a coarse-to-coarse representative is desired, an additional injection or section from `V_{\Sigma_0,a}` to `V_{\Sigma_0,a'}` must be specified; Paper 2 does not make such a section canonical.

Curvature-corrected foliation compatibility is not equality. It requires an additional projective family `T_\beta^a` representing the tangential deformation generated by

```math
\beta=N\partial M-M\partial N.
```

Then one may ask for

```math
\Gamma_P^a
=
T_\beta^a\Gamma_Q^a
```

exactly, asymptotically, or on cylinder effects/test states. V2 Paper 1 identifies the free one-particle candidate for the infinitesimal tangential action. Paper 2 only supplies the projective language in which such a correction can be compared across regulators.

To make curvature-corrected equivalence an actual equivalence relation, the declared tangential corrections must form a compatible projective group or groupoid, at least to the perturbative order being claimed. Without that closure statement, it is only a comparison criterion, not a covariance theorem.

## 13. How V2 Paper 1 Fits

V2 Paper 1 proves, at the free `1+1D` one-particle scope, that

```math
Z_{a,\Delta}
(E_a[N,M]-I)\iota_a\phi
\to
\iota_aK_\parallel[N\partial_xM-M\partial_xN]\phi
```

on sampled smooth compactly supported profiles, with the precise normalization and very-thin-slab scaling stated there.

Paper 2 should not restate that as exact projective compatibility of the full finite kernels. The honest interpretation is:

1. the finite exchange defects `E_a[N,M]` are regulated representatives of a continuum-directed exchange-curvature datum;
2. the test profiles `\iota_a\phi` define the smooth cylinder/test sector on which the limit is controlled;
3. any stronger claim that different lattice spacings are representatives of one exact projective family would need additional block-spin or sampling naturality estimates;
4. the approximate naturality theorem above says exactly what those estimates would have to control.

Thus Paper 1 supplies the first nontrivial projective target; Paper 2 defines the arena and the error bookkeeping; Paper 3 must prove interacting inverse/locality estimates within that arena.

## 14. Gauge, Fock, And Operational Variants

The same abstract framework covers later variants only after their extra structure is retained.

For Fock-space lifts, the regulator maps must specify how occupation configurations are coarse-grained, whether particle number is preserved, and how sector-changing kernels are represented. A number-preserving second-quantized lift is not the same projective problem as a sector-changing local operation.

For gauge systems, the correct finite spaces are usually not naive tensor products over regions. Physical Gauss sectors carry boundary-flux centers and global or boundary labels. A projective gauge system should therefore be center-resolved:

```math
V_{\Sigma,a}
=
\bigoplus_{z_a}V_{\Sigma,a,z_a},
```

with coarse-graining maps compatible with `z_{a'} -> z_a`. Statements about induced locality or cylinder effects should be made fiberwise or after explicitly specifying how center mixtures are handled.

For operational observables, raw comparison maps `J_R` and exchange defects `E_{R,S}` are not themselves local observables. Operational instruments and effects should be constructed separately and then tested for compatibility with the cylinder-effect system.

## 15. Exported Hypotheses For V2 Paper 3

Paper 3 can now be stated as a theorem problem rather than a slogan. For an interacting finite-range benchmark, it must prove or refute the following.

**Paper 3 export box.**

For a regulator family, coarse-graining maps, and interacting benchmark class, Paper 3 must specify:

1. **Topology and test sector.** The norms or seminorms in which refinement errors, inverse bounds, and quasilocal tails are measured.
2. **Primitive refinement estimates.** Bounds
   ```math
   \|P_1\Gamma_0^{a'}-\Gamma_0^aP_0\|\le\epsilon_0(a,a'),
   \qquad
   \|P_1\Gamma_R^{a'}-\Gamma_R^aP_0\|\le\epsilon_R(a,a')
   ```
   with errors tending to zero in the declared refinement limit.
3. **Uniform reference inverse control.** Bounds on `\|(\Gamma_0^a)^{-1}\|` in the slab/regulator window being used, at least on the relevant test or cylinder sector.
4. **Comparison-map control.** Bounds on `\|J_R^a\|`, `\|(J_R^a)^{-1}\|`, and their support tails strong enough that Theorem 4 sends primitive refinement errors to vanishing comparison-map and exchange-defect errors.
5. **Quasilocal support control.** A regulator-compatible collar/window estimate for `J_R^a` and `E_{R,S}^a`.
6. **Sector handling.** If the benchmark has particle-number sectors, Gauss sectors, or boundary centers, all estimates must be sectorwise or center-resolved.
7. **Raw/operational separation.** Any observable-locality theorem must be stated for operational instruments/effects, not inferred directly from raw comparison-map locality.

If any of these fail generically, interacting relativistic ISP may remain a fixed-regulator benchmark program rather than a continuum covariant dynamics.

## 16. Failure Modes

Paper 2 should be considered failed, or at least incomplete, under any of the following outcomes.

1. No physically meaningful coarse-graining maps preserve enough information for comparison maps.
2. Reference-kernel inverses are unstable under refinement.
3. Local support systems cannot be chosen compatibly with coarse-graining and collars.
4. Gauge constraints force center data that the proposed projective system forgets.
5. Foliation compatibility can only be formulated by imposing Markov divisibility through intermediate slices.
6. The projective framework has no nontrivial examples even at the free one-particle test-profile level.

The sixth point is the main optional strengthening beyond this draft: construct at least one worked free one-particle projective/asymptotic family with explicit coarse-graining maps.

## 17. Conclusion

The first V2 paper proved that a free finite ISP exchange defect can converge to the tangential hypersurface-deformation action in a controlled setting. This second paper supplies the mathematical home for such data across changing regulators.

The correct continuum-facing object is not a finite stochastic isomorphism and not a Markov semigroup. It is a projective family of finite endpoint kernels, states, effects, localized comparison maps, and exchange defects, with exact or asymptotic naturality under coarse-graining. Once this structure is fixed, Paper 3 has a precise burden: prove that interacting comparison maps and their inverses remain sufficiently local and sufficiently controlled for these projective limits to survive.
