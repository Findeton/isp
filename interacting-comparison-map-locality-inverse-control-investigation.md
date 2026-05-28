# Investigation: V2 Paper 3 - Interacting Comparison-Map Locality and Inverse Control

Author: Felix Robles Elvira

Date: 2026-05-13

Purpose: investigate the third V2 viability gate after the free stochastic-curvature theorem and the projective hypersurface-kernel framework. Paper 3 asks whether finite-range interacting dynamics can control the raw ISP comparison maps

```math
J_R=\Gamma_R\Gamma_0^{-1}
```

and their exchange defects under regulator refinement, rather than only in isolated fixed finite benchmarks.

Suggested paper title: `Quasilocality and Inverse Control for Interacting ISP Comparison Maps`.

Consolidated draft now created:

`relativistic-isp-v2-paper3-interacting-comparison-map-locality.md`

## Executive Verdict

V2 Paper 3 is the first genuinely dangerous post-Paper-2 test. Paper 2 supplies the projective language and shows exactly how refinement errors are amplified by `Gamma_0^{-1}`, `J_R`, and `J_R^{-1}`. Paper 3 must now decide whether those inverse objects remain local enough in interacting systems.

The current corpus contains important precursors:

- exact fixed finite interacting gauge-matter blocks;
- exact Gauss-sector decompositions;
- fixed-benchmark sectorwise inverse control in the dynamical Abelian matter-link model;
- first interaction-sensitive reduced-strip coefficients for finite `Z_2` and truncated compact `U(1)` benchmarks;
- finite validation scripts for prototype coefficients.

Before the consolidated Paper 3 draft, the corpus did not contain a V2 Paper 3 theorem. The consolidated draft now gives a theorem/no-go paper: it proves the global-norm obstruction, records fixed finite inverse control, proves finite-slab LC-log for the bounded finite-range/common-collar class by a paired-word activity/KP theorem, and isolates the remaining scope question for gauge sectors, reductions, cutoff families, and refinement maps.

The central lesson is severe:

> A global matrix norm is the wrong primary topology for a continuum-facing Paper 3 theorem. In a many-body finite-range system, `Gamma_0(\Delta)-I` can have norm growing with volume even when all microscopic terms are local. A global Neumann bound for `Gamma_0^{-1}` may therefore force `Delta^2 |Lambda| << 1`, which is useless as a continuum locality principle. Paper 3 should instead use anchored local, cylinder-effect, or exponential quasilocal norms for the localized defect `J_R-I` and for exchange defects.

The strongest safe target is therefore a local inverse theorem:

> For bounded finite-range lattice Hamiltonians with finite local configuration spaces, localized collar deformations, and a regulator-compatible support system, the formal coefficients of `J_R-I` are linked-cluster local around `R`; under an explicit anchored quasilocal inverse hypothesis, or after proving such a hypothesis by a cluster expansion, `J_R`, `J_R^{-1}`, and `E_{R,S}` obey regulator-stable support-window or exponential-tail bounds. The theorem must be stated sectorwise for gauge systems and must not identify raw comparison maps with observables.

If this fails, interacting ISP may remain a fixed finite benchmark framework rather than a continuum covariant relativistic dynamics.

## Why Paper 3 Follows Paper 2

Paper 2 exported the exact burden:

1. choose a topology/test sector;
2. prove primitive refinement estimates;
3. control `Gamma_0^{-1}`;
4. control `J_R` and `J_R^{-1}`;
5. control support windows for `E_{R,S}`;
6. handle sectors and centers explicitly;
7. keep raw comparison maps separate from operational observables.

Paper 3 is the first place these hypotheses can either be proved in an interacting class or shown to be too strong.

The subtlety is that ordinary Hamiltonian locality does not automatically imply ISP comparison-map locality. Lieb-Robinson bounds control Heisenberg commutators of local observables. The ISP object is instead a group commutator of pseudo-stochastic maps built from Born-squared primitive kernels and their inverses:

```math
E_{R,S}
=
J_RJ_SJ_R^{-1}J_S^{-1},
\qquad
J_R=\Gamma_R\Gamma_0^{-1}.
```

The inverse and the Born-squared projection are the two nonstandard steps. Paper 3 lives exactly there.

## Existing Inputs From The Corpus

### Input 1: Paper 2 gives the projective error identity

Paper 2 proves that if

```math
R_0=P_1A^{a'}-A^aP_0,
\qquad
R_R=P_1B_R^{a'}-B_R^aP_0,
```

then

```math
P_1J_R^{a'}-J_R^aP_1
=
(R_R-J_R^aR_0)(A^{a'})^{-1}.
```

Thus primitive refinement is not enough. The reference inverse and comparison map must be controlled in the same topology used for the refinement errors.

### Input 2: the relativistic architecture already warns against a Lieb-Robinson shortcut

The architecture paper explicitly notes that Lieb-Robinson bounds do not by themselves control

```math
\Gamma_R,\quad \Gamma_0^{-1},\quad J_R,\quad E_{R,S}.
```

They may guide the proof, but a separate bridge theorem is required. Paper 3 should not cite Lieb-Robinson as if it directly proves ISP locality.

### Input 3: the dynamical Abelian finite-link paper has the closest precursor

The dynamical Abelian gauge-field paper proves, at fixed finite lattice size and fixed finite link cutoff, a sectorwise mixed quasilocal filtration and a finite-family inverse bound. In its notation,

```math
J_R^{(S,\mathbf g)}(\Delta)
=
I+\sum_{m\ge2}\Delta^mA_{R,\mathbf g}^{[m],(S)},
```

with `A_{R,g}^{[m],(S)}` supported in an `m`-step mixed neighborhood, and with sectorwise bounds on `Gamma_0^{-1}`, `J_R`, and `J_R^{-1}` for sufficiently small `Delta`.

Important limitation: the constants depend on fixed lattice size and fixed link cutoff. This is not yet a regulator-stable V2 theorem.

### Input 4: the `Z_2` interacting benchmark proves exact finite blocks, not uniform locality

The minimal interacting `Z_2` gauge-matter paper proves exact physical-sector/global-flux elimination and a reduced matter Hamiltonian with a parity-string electric term. It also computes a first interaction-sensitive reduced-strip coefficient.

Important limitation: the reduced matter variables are nonlocal after Gauss-law elimination. That is conventional in one-dimensional gauge theory, but it means reduced-coordinate locality is not the right primitive locality notion for Paper 3. If Paper 3 uses this benchmark, the clean locality statement should be made in the unreduced matter-link variables or in a center-resolved sector language.

### Input 5: the truncated compact `U(1)` benchmark is finite at fixed `K`, but not a `K -> infinity` theorem

The truncated compact `U(1)` paper proves exact finite matrices at fixed link cutoff `K`, exact sector elimination under a no-truncation condition, and a Coulomb-string reduced Hamiltonian.

Important limitation: Paper 3 cannot treat this as compact-rotor control. Bounds may depend on `K`; the no-truncation domain may change under refinement; and the full compact rotor has an infinite electric-flux tower. A V2 Paper 3 theorem can use fixed `K` as a finite benchmark but must not claim `K`-uniformity unless it proves it.

### Input 6: reduced-strip companion calculations organize coefficients but do not replace inverse control

The reduced-strip/overlap companion shows how broader interacting coefficients appear or vanish at specific orders and identifies finite strip bases.

Important limitation: coefficient bookkeeping is not the same as a finite-slab inverse theorem. It supplies exact local data that Paper 3 may use, but it does not control `Gamma_0^{-1}` or `J_R^{-1}` under volume/cutoff growth.

## The Main Obstruction: Global Norms Are Too Strong

At fixed finite size, every primitive kernel satisfies

```math
\Gamma_0(\Delta)=I+O(\Delta^2),
```

because the Born-squared kernel has no linear term. In a global induced matrix norm, however, the coefficient can scale with the number of local terms. For a many-body lattice with `|Lambda|` sites,

```math
\|\Gamma_0(\Delta)-I\|_{\mathrm{global}}
\sim
O(|\Lambda|\Delta^2)
```

is the natural generic scaling.

A Neumann estimate in that norm gives

```math
\Gamma_0(\Delta)^{-1}
=
\sum_{\ell\ge0}(I-\Gamma_0(\Delta))^\ell
```

only when `|\Lambda|\Delta^2` is small. That is a fixed-finite-matrix theorem, not a continuum locality theorem. It would force the slab thickness to shrink with volume before one has even studied relativistic scaling.

The consolidated Paper 3 draft strengthens this warning with an independent product example where the actual global inverse norm grows like `exp(c|\Lambda|\Delta^2)`.

Therefore Paper 3 must choose a local topology. Plausible options:

1. **Anchored defect norms.** Measure `J_R-I` by how far its active configuration change lies from the support `R`.
2. **Cylinder-effect seminorms.** Test maps only against effects supported in a fixed coarse region and require decay with separation from `R`.
3. **Exponential quasilocal norms.** Weight transition entries by an exponential of the distance from the changed cells to the anchor region.
4. **Sectorwise versions.** In gauge systems, define any of the above fiberwise over Gauss-sector or boundary-center labels.

The global matrix norm may remain useful for fixed finite validation, but it should not be the main V2 topology.

## First-Principles Route To Hypothesis LC

The object that should be local is not `Gamma_0^{-1}` by itself. The local object is the relative comparison map

```math
J_R=\Gamma_R\Gamma_0^{-1}.
```

This is analogous to a Radon-Nikodym derivative or a relative Gibbs weight: the absolute normalization of a large system may be extensive, while the ratio between two laws that differ only in a local collar should be local after disconnected exterior pieces cancel.

Three simple laboratories make the issue tangible.

1. **Exact product cancellation.** If `C=C_A\times C_B`, `Gamma_0=Gamma_A\otimes Gamma_B`, and `Gamma_R=Gamma_A^R\otimes Gamma_B`, then

```math
J_R=(\Gamma_A^R\Gamma_A^{-1})\otimes I_B.
```

The exterior inverse cancels exactly, even when `\|\Gamma_B^{-1}\|` is huge in a global norm.

This same example rules out a naive proof. The primitive difference is

```math
\Gamma_R-\Gamma_0
=
(\Gamma_A^R-\Gamma_A)\otimes\Gamma_B
=
(\Gamma_A^R-\Gamma_A)\otimes I_B
+
(\Gamma_A^R-\Gamma_A)\otimes(\Gamma_B-I_B).
```

The second term can contain far-away exterior transitions at order `O(\Delta^4)`. Therefore `\Gamma_R-\Gamma_0` need not be entrywise anchored, even when `J_R` is exactly anchored. The cancellation is genuinely relative/logarithmic.

2. **Finite-depth circuit light cones.** If a localized deformation changes only gates inside a finite circuit light cone, and the circuit is buffered so the cone and complement factor, then the same product cancellation applies. This gives an exact LC theorem for clean circuit laboratories. A realistic proof route is: prove exact cancellation for buffered Trotter circuits or anchored LC estimates for generic Trotter circuits, prove anchored convergence to continuous-time kernels, then pass the cancellation to the limit.

3. **Diagonal interaction plus hopping.** A purely diagonal interaction is invisible to primitive `Gamma` kernels because entrywise squared modulus removes phases. Interaction-sensitive coefficients appear only when local hopping paths sample diagonal energy gaps. Thus every primitive difference word has at least one collar-linked component, but disconnected exterior components may accompany it. The real question is whether those exterior components cancel in the relative/logarithmic object.

The strongest mathematical target is the connected logarithmic defect

```math
L_R=\log J_R.
```

If `L_R` is anchored quasilocal with `\|L_R\|_{\mathcal A_{\mu,R}}=O(\Delta^2)`, then

```math
J_R=e^{L_R},
\qquad
J_R^{-1}=e^{-L_R},
```

and both comparison-map locality and inverse locality follow by Banach-algebra calculus. Conceptually, this is the linked-cluster theorem in its cleanest form: disconnected reference pieces may occur in raw expansions, but they should not survive in the connected cumulant generator anchored at the collar.

## Proof Audit Of The Section 13 Checklist

The Section 13 checklist in the consolidated draft separates into finished, conditional, and genuinely missing items.

1. **Global-norm obstruction.** Done. The product two-state example is a real no-go for global Neumann control because both `\|\Gamma_N-I\|_1` and `\|\Gamma_N^{-1}\|_1` scale with volume.
2. **Fixed finite inverse control.** Done at finite-matrix level. The proof is finite-dimensional analyticity plus a Neumann neighborhood at `Delta=0`. It is intentionally not regulator-stable.
3. **Precise local topology.** Mostly closed at the abstract level. The draft now defines an anchored tree-polymer Banach algebra, proves the inverse/exponential/log calculus, and records a bulk-to-anchored commutator estimate. The remaining burden is to show the actual ISP objects satisfy those bounds.
4. **Hypothesis LC or LC-log.** Proved for the bounded finite-range, uniformly finite local-dimension, common-support collar-deformation class. The product warning above shows that the proof cannot be "`Gamma_R-Gamma_0` is local, therefore `J_R` is local." The consolidated draft proves fixed-order LC-log locality by disjoint-union factorization and cumulant cancellation, reduces finite-slab convergence to coefficient majorants, and then proves those majorants with a paired-word Born-squared activity/KP theorem. Proposition 10 has now been proof-hardened with an explicit operator-valued KP logarithm, analytic log branch, complex-vs-real stochasticity caveat, volume-uniform constants, and noncommutative activity-cluster norm control. Outside this class, especially in reduced nonlocal gauge coordinates or cutoff-removal limits, LC-log remains a hypothesis to be checked.
5. **Theorems 2 through 5.** Done inside the Proposition 10 class for inverse and exchange locality. Theorem 4 now gives a concrete two-anchor corridor/window theorem with exponential outside-window tails and a coefficient onset bound. Theorem 5 makes the projective handoff honest: primitive refinement errors must either beat the reference inverse `(A^{a'})^{-1}` in raw form or be proved directly as reference-renormalized residual estimates `\widehat R_0,\widehat R_R`.
6. **Sectorwise gauge variants.** Done at theorem-framework level. Section 11 now proves a sectorwise common-collar inverse theorem for invariant coordinate sectors, or for center-resolved fibers with an explicitly supplied sector tree-polymer norm. A worked benchmark must still specify the sector family, center labels, boundary-flux maps, and whether constants are uniform over that family.
7. **Paper 4 export.** Done at theorem-framework level. The consolidated draft now includes a Paper 4 Export Box: raw `J_R` and `E_{R,S}` are algebraic relative-dynamics maps with locality bounds, not observables/effects/instruments. Operational instruments require extra structure and their own inherited-locality proof.

The decisive unresolved question is therefore no longer the finite-slab estimate for ordinary bounded finite-range common-collar systems. It is now the scope question:

> Which gauge sectors, reductions, cutoff families, and refinement maps satisfy the common-support finite-range hypotheses and preserve the tree-polymer topology?

## LC-Log Proof Skeleton

The cleanest proof route is to work with logarithms of the primitive kernels before forming `J_R`.

Define

```math
W_0^\Lambda(\Delta)=\log\Gamma_0^\Lambda(\Delta),
\qquad
W_R^\Lambda(\Delta)=\log\Gamma_R^\Lambda(\Delta),
\qquad
D_R^\Lambda(\Delta)=W_R^\Lambda(\Delta)-W_0^\Lambda(\Delta).
```

Then

```math
J_R^\Lambda
=
\exp(W_0^\Lambda+D_R^\Lambda)\exp(-W_0^\Lambda),
```

and the desired connected comparison generator is

```math
L_R^\Lambda
=
\log J_R^\Lambda
=
\log\left(\exp(W_0^\Lambda+D_R^\Lambda)\exp(-W_0^\Lambda)\right).
```

A proof of LC-log would follow from four lemmas.

1. **Reference-log polymer lemma.** `W_0^\Lambda` has a connected local polymer expansion. Its coefficient of order `Delta^m` is supported on connected interaction clusters of size/radius `O(m)`, with volume-independent polymer norm.
2. **Anchored log-difference lemma.** `D_R^\Lambda` has a connected polymer expansion in which every connected cluster touches the collar where `H_R` differs from `H`.
3. **BCH anchoring lemma.** Every nested commutator in

```math
\log\left(\exp(W_0+D_R)\exp(-W_0)\right)
```

contains at least one `D_R`. Since commutators of disjoint local factors vanish or factor trivially, the support of every connected term is reached by an overlapping chain from `R`.
4. **Small-slab convergence lemma.** The chosen polymer norm makes the logarithm and BCH series converge for `|\Delta|<Delta_*`, with `Delta_*` independent of total volume.

At fixed order, the first three lemmas would already prove coefficient-level LC. The fourth lemma is what upgrades the result to a finite-slab theorem.

After the latest draft pass, the purely algebraic part of lemma 3 is no longer the bottleneck: the tree-polymer Banach algebra and the bulk-to-anchored commutator estimate provide the needed BCH support control. More precisely, if `W_0=log Gamma_0` is bulk-polymer bounded, `D_R=log Gamma_R-log Gamma_0` is anchored-tree bounded, and the BCH series converges after a decay-rate loss, then `L_R=log(exp(W_0+D_R)exp(-W_0))` is anchored-tree bounded with size controlled by `D_R`.

The draft now also proves the fixed-order version of lemmas 1 and 2. At each order in `Delta`, `log Gamma_0` has only connected polymer coefficients, and `log Gamma_R-log Gamma_0` has only connected coefficients linked to the collar. The proof uses two facts: finite-range words have bounded connected components at fixed order, and disjoint-union factorization makes the matrix logarithm additive, so disconnected products cancel in the cumulant. Proposition 10 upgrades this to a finite-slab theorem for the bounded finite-range common-collar class by constructing paired-word activities and applying a KP/tree-graph bound.

### The convergence problem

The current draft has reduced the finite-slab problem to the following coefficient-majorant estimates. Write

```math
W_0^\Lambda(\Delta)
=
\sum_{m\ge2}\Delta^mW_{0,m}^\Lambda,
\qquad
D_R^\Lambda(\Delta)
=
\sum_{m\ge2}\Delta^mD_{R,m}^\Lambda.
```

After decomposing these coefficients into connected polymers, it is enough to prove constants `A_0,A_R,B,\mu`, independent of total volume, such that

```math
\sup_{x\in\Lambda}
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{\mu\operatorname{diam}(X)}
\|W_{0,m,X}^\Lambda\|_{1,X}
\le A_0B^m
```

and

```math
\sum_{\substack{X\ \mathrm{connected}}}
e^{\mu\ell_R(X)}
\|D_{R,m,X}^\Lambda\|_{1,X}
\le A_RB^m
```

for all `m>=2`. These bounds are stronger than fixed-order locality but much weaker than global matrix-norm control. They allow large disconnected reference propagation in `Gamma_0`; they only forbid connected logarithmic coefficients from growing faster than exponentially or from detaching from the collar in the relative log-difference.

If these estimates hold, summing over `m` gives convergent bulk and anchored logarithms for `|\Delta|<B^{-1}`. Since the resulting norms are `O(\Delta^2)`, the BCH step for

```math
L_R=\log(\exp(W_0+D_R)\exp(-W_0))
```

is then inside the usual small-norm Banach-Lie convergence radius after shrinking `Delta_*` by a volume-independent factor. Thus BCH convergence should not be treated as the main combinatorial obstacle; the real obstacle is the connected-log majorant.

A plausible proof route is:

1. bound Duhamel words for `e^{-i\Delta H}` by connected supports growing at finite speed;
2. show the Born-squared projection only pairs two such words and changes constants, not the connected support velocity;
3. define connected logarithmic coefficients by a polymer cumulant/Mobius transform;
4. use a tree-graph or Kotecky-Preiss estimate to replace the naive Bell-number/factorial cumulant count by an exponential `B^m` bound.

The fourth step is the danger point. If the best available absolute bound grows like `m! C^m`, the power series has zero radius in the required polymer norm and item 4 remains unproved. If a counterexample exists, it must show either superexponential connected-log growth or an unanchored connected component in `D_R`; a far-away primitive term in `Gamma_R-Gamma_0` is not enough, because disconnected primitive pieces may still vanish in the relative logarithm.

### The next estimate: activity first, logarithm second

The missing estimate should not be attacked by trying to prove `\Gamma_0-I` is small in a connected polymer norm. The product benchmark already refutes that target: even independent on-site kernels produce `\Gamma_0-I` terms supported on arbitrary disconnected subsets. The logarithm is local because those terms are products of independent activities, not because the primitive defect is itself connected-local.

The right next theorem is therefore an activity theorem.

For complex estimates, use the holomorphic extension

```math
\Gamma_H^\Lambda(z)
:=
e^{-izH_\Lambda}\odot e^{iz\overline{H_\Lambda}},
```

where `\odot` is entrywise product. For real `z=\Delta`, this equals the Born-squared kernel `|e^{-i\Delta H_\Lambda}|^2`. This avoids treating an absolute value as holomorphic and keeps the no-linear-term stochastic onset in the one-variable Taylor expansion.

For connected polymers `X`, seek analytic local activities `\zeta_X^\Lambda(z)` such that

```math
\Gamma_H^\Lambda(z)
=
\sum_{\mathcal F\ \mathrm{compatible}}
\prod_{X\in\mathcal F}\zeta_X^\Lambda(z),
```

where compatible means disjoint support and the empty family contributes `I`. For the localized kernel, seek activities `\zeta_{R,X}^\Lambda(z)` and differences

```math
\delta\zeta_X^\Lambda(z)=\zeta_{R,X}^\Lambda(z)-\zeta_X^\Lambda(z).
```

The sufficient bounds are Kotecky-Preiss type:

```math
\sup_{x\in\Lambda}
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{a|X|+\mu\operatorname{diam}(X)}
\|\zeta_X^\Lambda(z)\|_{1,X}
\le \kappa(z),
```

and

```math
\sum_{\substack{X\ \mathrm{connected}}}
e^{a|X|+\mu\ell_R(X)}
\|\delta\zeta_X^\Lambda(z)\|_{1,X}
\le \kappa_R(z),
```

with `\kappa,\kappa_R` below the KP threshold and `O(z^2)`. Then the standard cluster expansion for the logarithm gives

```math
\log\Gamma_0^\Lambda
=
\sum_{\mathrm{connected\ activity\ clusters}} \mathrm{Ursell}\cdot
\prod \zeta_X^\Lambda,
```

and the difference `\log\Gamma_R-\log\Gamma_0` is a sum of connected activity clusters with at least one marked `\delta\zeta`. The first estimate gives a bulk polymer bound; the marked estimate gives an anchored tree bound. Cauchy's estimate on a fixed circle `|z|=\rho_0` then gives exponential coefficient growth `B^m`.

This route is stronger and cleaner than direct coefficient bookkeeping. It reduces the missing estimate to two concrete lemmas:

1. **Born-squared activity representation.** Construct compatible connected activities for `\Gamma_0` and `\Gamma_R` from the finite-range Hamiltonian.
2. **Activity KP smallness.** Prove the two displayed activity bounds uniformly in total volume for `|z|<\Delta_*`.

The first lemma is structural. It must preserve tensor factorization on disconnected regions and must be stated at the `\Gamma=|U|^2` level, because bounding `U` and squaring naively loses the `O(\Delta^2)` stochastic onset.

The promising construction is by paired Duhamel words. Expand the two factors in

```math
\Gamma_H(z)=e^{-izH}\odot e^{iz\overline H}.
```

A paired word is

```math
\Omega=(Y_1,\ldots,Y_p;Z_1,\ldots,Z_q),
```

with local contribution

```math
K_\Omega(z)
=
\frac{(-iz)^p(iz)^q}{p!\,q!}
\left(h_{Y_p}\cdots h_{Y_1}\right)
\odot
\left(\overline h_{Z_q}\cdots\overline h_{Z_1}\right).
```

The entrywise product does not create a new norm problem. In local column-sum norm,

```math
\|A\odot B\|_1
=
\max_j\sum_i |A_{ij}B_{ij}|
\le
\|A\|_1\|B\|_1,
```

and tensor products over disjoint factors multiply norms. Thus

```math
\|K_\Omega(z)\|_{1,\operatorname{supp}\Omega}
\le
\frac{|z|^{p+q}}{p!\,q!}J_1^{p+q}.
```

Let the support hypergraph of `\Omega` have hyperedges `Y_i` and `Z_j`. Define

```math
\zeta_X(z)
=
\sum_{\substack{\Omega:\operatorname{supp}\Omega=X\\
\operatorname{supp}\Omega\ \mathrm{connected}}}
K_\Omega(z).
```

Then disconnected paired-word components factor over disjoint tensor factors. The only combinatorial point is the shuffle identity: summing all interleavings of the amplitude subwords and conjugate subwords assigned to distinct connected components gives exactly the product of the component activities with coefficient `1/(p!\,q!)`. Therefore

```math
\frac1{p!\,q!}
\frac{p!}{\prod_jp_j!}
\frac{q!}{\prod_jq_j!}
=
\prod_j\frac1{p_j!\,q_j!},
```

where component `j` carries `p_j` amplitude terms and `q_j` conjugate terms. This is the two-channel version of the usual exponential formula.

```math
\Gamma_H^\Lambda(z)
=
\sum_{\mathcal F\ \mathrm{compatible}}
\prod_{X\in\mathcal F}\zeta_X^\Lambda(z).
```

This is the activity representation used in Proposition 10.

The second lemma is analytic. The plausible word count is favorable: an ordered Duhamel word of length `n` connected to a fixed cell has at most `C^n n!` choices, while the time-ordered coefficient contributes `1/n!`, leaving `C^n`. Born-squared coefficients pair two such words with total order `m`, producing another exponential bound after absorbing the number of splits `p+q=m`. With the paired-word definition, these connected word bounds act directly on the compatible activities; the KP/tree-graph estimate is then used for the logarithm, not to repair a factorially bad activity count.

More explicitly, let the local terms have range `r`, bounded overlap degree, and bounded local column norm `J_1`. If `\omega=(Y_1,\ldots,Y_n)` is an ordered word of local supports whose overlap graph is connected and touches a fixed cell `x`, then

```math
N_n(x)\le C_0^n n!.
```

One way to see the factorial is to expose a spanning tree of the word: at the `k`th step there are at most `Ck` local supports that can touch the already exposed connected cluster. The exponential coefficient cancels it:

```math
\sup_x
\sum_{\substack{\omega\ \mathrm{connected}\\\omega\ni x\\|\omega|=n}}
e^{\mu\operatorname{diam}(\omega)}
\frac{\|h_{Y_n}\cdots h_{Y_1}\|_{1,\operatorname{supp}\omega}}{n!}
\le
\left(C_1J_1e^{\mu r}\right)^n.
```

For the Born-squared coefficient at order `m`, write `m=p+q` and pair a length-`p` amplitude word with a length-`q` conjugate word. The same estimate gives

```math
\sum_{p+q=m}
\left(C_1J_1e^{\mu r}\right)^p
\left(C_1J_1e^{\mu r}\right)^q
\le
(C_\Gamma)^m.
```

So the word expansion itself is not the enemy. With the paired-word activity definition, the KP smallness estimate becomes

```math
\sup_x
\sum_{\substack{X\ni x\\X\ \mathrm{connected}}}
e^{a|X|+\mu\operatorname{diam}(X)}
\|\zeta_X^\Lambda(z)\|_{1,X}
\le
\sum_{m\ge2}
\left(C_2J_1e^{as+\mu r}|z|\right)^m.
```

For a localized deformation, the activity difference is the same connected paired-word sum with at least one marked collar term. Use the common-support convention

```math
H_\Lambda=\sum_{Y\in\mathcal E_\Lambda}h_Y,
\qquad
H_{R,\Lambda}=\sum_{Y\in\mathcal E_\Lambda}(h_Y+c_{R,Y}),
```

with `c_{R,Y}=0` outside the collar scaffold and

```math
\|h_Y\|_{1,Y},\ \|h_Y+c_{R,Y}\|_{1,Y}\le J_{\mathrm{def}},
\qquad
\sum_Ye^{a|Y|+\mu\ell_R(Y)}\|c_{R,Y}\|_{1,Y}\le C_R.
```

If the original decompositions use different supports, refine to the union and add zero terms. Then every term in `\delta\zeta_X` contains at least one marked `c_{R,Y}` factor, and connected exposure from the first marked factor gives

```math
\sum_{\substack{X\ \mathrm{connected}}}
e^{a|X|+\mu\ell_R(X)}
\|\delta\zeta_X^\Lambda(z)\|_{1,X}
\le
C_R
\sum_{m\ge2}
\left(C_3J_{\mathrm{def}}e^{as+\mu r}|z|\right)^m.
```

Thus the right side is still `O(z^2)`. Proposition 10 packages these estimates into a finite-slab activity/KP theorem for bounded finite-range Hamiltonians with uniformly finite local dimension and a collar family satisfying the displayed common-support marked-term bound.

The order-`z` term vanishes directly. For a local Hermitian term,

```math
(-iz h_Y)\odot I_Y
+
I_Y\odot(iz\overline h_Y)
=0,
```

because the entrywise product with `I_Y` keeps only the diagonal, and Hermitian matrices have real diagonal entries.

Remaining obligation: check that each intended benchmark or sector presentation satisfies the common-support collar hypothesis with constants uniform in the regulator family being claimed.

### Low-order sanity checks

At order `Delta^2`, `\log\Gamma_0` equals the `Delta^2` coefficient of `\Gamma_0-I`, so locality reduces to the usual local-transition statement. The anchored difference is local because changing `H` only in the collar changes the order-`Delta^2` transition weights only there.

At order `Delta^4`, the first nontrivial disconnected cancellation appears:

```math
\log(I+\Delta^2G_2+\Delta^4G_4+\cdots)
=
\Delta^2G_2
+
\Delta^4\left(G_4-\frac12G_2^2\right)
+
O(\Delta^6).
```

In a product system, `G_4` contains disconnected products of two independent `G_2` events, while `-\frac12G_2^2` subtracts the disconnected contribution in the connected logarithm. This is the concrete algebraic mechanism that the all-order LC-log theorem must generalize.

### Possible obstructions

LC-log can fail, or remain unproved, for precise reasons:

1. the Born-squared projection may not admit a volume-stable connected polymer logarithm in the proposed norm;
2. reduced gauge variables may create long strings, making the wrong coordinate system look nonlocal;
3. compact-rotor or `K -> infinity` limits may destroy finite local dimension and finite-matrix analyticity;
4. sector constants may be finite in each block but unstable over the sector family needed for refinement;
5. coarse-graining maps may fail to preserve the same polymer/cylinder topology used for inverse control.

These are not cosmetic risks. Any one of them would force Paper 3 to remain a conditional/no-go paper rather than a positive interacting-continuum theorem.

## Recommended Formal Setup

### Local configuration system

Let `Lambda_a` be a finite graph or cell complex with bounded degree and finite local configuration spaces. Let

```math
C_a=\prod_{x\in\Lambda_a}C_x
```

in the unconstrained case. In gauge systems, replace this by a full matter-link configuration space or by a center-resolved physical sector.

For two configurations `c,c'`, define the changed-cell set

```math
\operatorname{chg}(c,c')
=
\{x:c_x\ne c'_x\}.
```

For a region `R`, define the distance of a transition from `R` by

```math
d_R(c,c')
=
\operatorname{dist}(\operatorname{chg}(c,c'),R),
```

with `d_R(c,c)=0`.

### Anchored quasilocal norm

For a normalization-preserving map `K` anchored at `R`, define a candidate anchored norm

```math
\|K\|_{\mu,R}
=
\sup_c\sum_{c'} |K_{c',c}| e^{\mu d_R(c,c')}.
```

This is only a starting point. For many-body maps with extensive independent changes, one may need a polymer norm that decomposes `K-I` into connected clusters anchored at `R`. The investigation should state this explicitly rather than pretending the first norm is automatically complete.

### Anchored tree-polymer norm

The concrete topology now recommended for Paper 3 is an anchored tree-polymer norm.

A local map `K_X` is supported in a finite cell set `X` when it changes no cells outside `X` and its entries depend only on the incoming/outgoing restrictions to `X`. For defects, require zero column sums. Let `R_*` be the collar where `H_R` differs from `H`, together with a fixed bounded connecting scaffold if needed. Define `\ell_R(X)` as the extra graph length of the smallest connected cell subgraph containing `X\cup R_*`, beyond the fixed scaffold for `R_*`.

Define

```math
\|K\|_{\mu,R}^{\mathrm{tree}}
=
\inf_{K=\sum_XK_X}
\sum_X e^{\mu\ell_R(X)}\|K_X\|_{1,X}.
```

This norm is designed to make the product warning mathematically visible. A far-away exterior factor is expensive because the tree connecting it to `R_*` is long. If that factor cancels in `J_R` or `L_R`, the tree norm remains finite; if it survives, LC fails.

The key algebraic estimate is straightforward at the level of local pieces:

```math
\operatorname{supp}(K_XL_Y)\subseteq X\cup Y,
\qquad
\ell_R(X\cup Y)\le\ell_R(X)+\ell_R(Y).
```

Hence the tree norm is the right candidate Banach algebra norm for the conditional inverse, exponential, and commutator arguments.

The consolidated draft now closes this abstract algebra step. The weighted local-piece direct sum

```math
\mathfrak P_{\mu,R}
=
\{(K_X)_X:\sum_X e^{\mu\ell_R(X)}\|K_X\|_{1,X}<\infty\}
```

is Banach, and the tree-polymer defect space is the quotient by representations that sum to zero globally. Because

```math
\operatorname{supp}(K_XL_Y)\subseteq X\cup Y,
\qquad
\ell_R(X\cup Y)\le\ell_R(X)+\ell_R(Y),
```

the quotient is a Banach algebra after adjoining the identity. Therefore Neumann inverses, exponentials, and logarithms are controlled by ordinary Banach-algebra series.

The draft also records the needed mixed estimate: if `W` is bulk-local and `D` is anchored, then for `0<\nu<\mu`,

```math
\|[W,D]\|_{\nu,R}^{\mathrm{tree}}
\le
C\|W\|_{\mu}^{\mathrm{bulk}}\|D\|_{\mu,R}^{\mathrm{tree}}.
```

Only overlapping local pieces contribute to the commutator; the loss from `\mu` to `\nu` absorbs the number of possible overlaps. This is what lets BCH terms involving the bulk reference logarithm remain anchored.

The same estimate with both inputs bulk makes the bulk-polymer space a Banach-Lie algebra after decay loss, while the anchored tree-polymer space is an ideal for the bulk action. This is why, once the connected logarithms are genuinely small in these norms, BCH convergence is a standard small-norm issue rather than a new source of long-range support.

For the bulk reference logarithm `W_0=\log\Gamma_0`, the companion norm should be a per-cell bulk polymer norm:

```math
\|W\|_{\mu}^{\mathrm{bulk}}
=
\sup_{x\in\Lambda}
\inf_{W=\sum_XW_X}
\sum_{X\ni x}e^{\mu\operatorname{diam}(X)}\|W_X\|_{1,X}.
```

Then the LC-log target is:

```math
\|W_0\|_{\mu}^{\mathrm{bulk}}\le C\Delta^2,
\qquad
\|D_R\|_{\mu,R}^{\mathrm{tree}}\le C\Delta^2,
\qquad
\|L_R\|_{\mu,R}^{\mathrm{tree}}\le C\Delta^2.
```

### Local Hamiltonian class

Assume a bounded finite-range Hamiltonian

```math
H_a=\sum_{X\subset\Lambda_a}h_X,
```

with:

1. `diam(X)<=r`;
2. `\|h_X\|\le J`;
3. each cell belongs to at most `b` supports `X`;
4. finite local dimension bounded uniformly in `a`;
5. sector projections or center labels fixed when constraints are present.

Localized deformation is modeled by deleting or modifying a collar term:

```math
H_{R,a}=H_a-C_{R,a}.
```

The primitive kernels are

```math
\Gamma_0^a(\Delta)=|e^{-i\Delta H_a}|^2,
\qquad
\Gamma_R^a(\Delta)=|e^{-i\Delta H_{R,a}}|^2.
```

This includes the existing collar-excision philosophy while making the local-interaction hypotheses explicit.

## Theorem Ladder For Paper 3

### Theorem A: fixed-order linked-cluster locality

Target statement:

For bounded finite-range Hamiltonians in the class above, the coefficient of order `Delta^m` in

```math
J_R^a(\Delta)-I
```

depends only on the `m`-step neighborhood of `R`, up to the precise parity/order convention produced by the Born-squared kernel. Equivalently, if two configurations agree on `N_m(R)`, then the coefficient cannot distinguish their exterior data.

A stronger version proves this for the connected logarithmic defect `L_R^a=\log J_R^a` first, then obtains `J_R-I` and `J_R^{-1}-I` by exponentiation.

Why it matters:

This is the interacting analogue of the free quasilocal filtration. It is coefficient-level and should be the first theorem because it avoids the global inverse-norm problem.

Status:

The consolidated draft proves this at fixed formal order and, by Proposition 10, at finite-slab level for the bounded finite-range/common-collar class. What remains is to check the hypotheses in each gauge-sector and refinement setting.

Proof strategy:

Use Duhamel expansions of `e^{-i\Delta H_R}` relative to `e^{-i\Delta H}`. Every term in the difference contains at least one collar insertion. A word of length `m` can only grow the connected active cluster by `m` interaction-graph steps. The inverse `\Gamma_0^{-1}` must be handled coefficientwise; its disconnected global pieces should cancel against the reference part, leaving only linked clusters attached to `R`.

This cancellation is the first real proof burden; the paired-word activity proof is the current route for proving it rather than assuming it.

### Theorem B: fixed finite inverse-control theorem

Target statement:

At fixed lattice size, cutoff, and sector family, there is a small `Delta_*` such that `Gamma_0^a`, `J_R^a`, and `J_R^a^{-1}` exist and satisfy finite matrix bounds.

Status:

This is essentially already available in the fixed finite dynamical Abelian benchmark and follows generally by finite-dimensional analyticity. It is not enough for V2 Paper 3 unless its limitations are made explicit.

### Theorem C: volume-stable anchored inverse theorem

Target statement:

There exist constants `Delta_*`, `C`, and `mu>0`, independent of volume at fixed local dimension and local coupling, such that

```math
\|J_R^a(\Delta)-I\|_{\mu,R}\le C\Delta^2,
\qquad
\|(J_R^a(\Delta))^{-1}-I\|_{\mu,R}\le C\Delta^2
```

for `|\Delta|<Delta_*`, with analogous sectorwise statements in gauge systems.

This is the core V2 Paper 3 theorem. It is now proved for the bounded finite-range/common-collar class: use the paired-word Born-squared polymer-activity expansion with KP smallness, deduce the connected-log coefficient majorants, then apply the tree-polymer exponential and inverse calculus. Outside that class, it remains a named hypothesis.

Possible proof route:

For the common-collar class, use Proposition 10 and the tree-polymer calculus. For other systems, develop an analogous polymer or cluster expansion for the connected defect `L_R=\log J_R`, or carry LC-log as an explicit hypothesis. The reference inverse should be expanded only after subtracting the common global reference propagation, so disconnected components not linked to `R` cancel.

With the tree-polymer norm, a positive proof should target the exponential representation:

```math
J_R=e^{L_R},
\qquad
J_R^{-1}=e^{-L_R}.
```

If `\|L_R\|_{\mu,R}^{\mathrm{tree}}\le C\Delta^2`, then

```math
\|J_R-I\|_{\mu,R}^{\mathrm{tree}},
\ \|J_R^{-1}-I\|_{\mu,R}^{\mathrm{tree}}
\le e^{C\Delta^2}-1.
```

This bypasses a global inverse estimate and turns inverse control into a local logarithm theorem.

### Theorem D: exchange-defect support/window theorem

Status: upgraded in the consolidated draft to a concrete two-anchor theorem.

If `J_R`, `J_R^{-1}`, `J_S`, and `J_S^{-1}` obey anchored quasilocal bounds,
define the corridor excess length

```math
\ell_{R:S}(Z)=\tau(R_*\cup S_*\cup Z)-\tau(R_*\cup S_*).
```

The theorem proves

```math
\|E_{R,S}-I\|_{\nu,R:S}^{\mathrm{corr}}
\le
C e^{-\nu d(R_*,S_*)}
\|J_R-I\|_{\mu,R}
\|J_S-I\|_{\mu,S}
\|J_R^{-1}\|_{\mu,R}^{+}
\|J_S^{-1}\|_{\mu,S}^{+},
```

where the four norm factors are multiplied. Hence the outside-window tail is

```math
\|E_{R,S}-I\|_{>w}^{(1),R:S}
\le
C\Delta^4e^{-\nu(d(R_*,S_*)+w)}
```

inside the finite-slab LC-log window. It also proves the coefficient onset
bound: if `J_R-I` and `J_S-I` have order-`m` supports in `N_{vm}(R_*)` and
`N_{vm}(S_*)`, then `[\Delta^m](E_{R,S}-I)=0` for `m<4` and whenever
`vm<d(R_*,S_*)`.

This theorem converts comparison-map control into the raw exchange-defect
locality needed before operational reconstruction.

### Theorem E: projective/refinement transfer

Target statement:

If the primitive interacting kernels satisfy the Paper 2 refinement estimates in the same local topology after the reference-inverse bottleneck is controlled,

```math
\widehat R_0=
(P_1\Gamma_0^{a'}-\Gamma_0^aP_0)(\Gamma_0^{a'})^{-1},
\qquad
\widehat R_R=
(P_1\Gamma_R^{a'}-\Gamma_R^aP_0)(\Gamma_0^{a'})^{-1},
```

with `\|\widehat R_0\|_{\mathrm{loc}},\|\widehat R_R\|_{\mathrm{loc}}\to0`, then Theorem C and Paper 2's error identity imply refinement compatibility of `J_R` and `E_{R,S}`.

This is the bridge from raw interacting locality to continuum-directed covariance.

The raw version is also possible, but then the primitive errors must be small
enough to beat `\|(\Gamma_0^{a'})^{-1}\|`. The refinement theorem also needs
one topology-specific hypothesis: coarse-graining maps must be bounded between
the tree-polymer algebras, with a uniform bound on tree-length distortion.
Without that, even correct LC-log estimates at each regulator do not
necessarily project to compatible comparison maps.

## Best Scope For V2 Paper 3

The best first scope is not compact `U(1)` and not a full continuum QFT. It is:

1. bounded finite local dimension;
2. bounded finite-range interactions;
3. collar-excision or equivalent localized deformations;
4. unconstrained systems or center-resolved finite gauge sectors;
5. a local/anchored topology rather than a global matrix norm;
6. coefficient-level linked-cluster locality proved unconditionally;
7. finite-slab anchored inverse control proved either unconditionally by a cluster expansion or stated as a precisely isolated hypothesis.

The most conservative worked benchmark is the unreduced finite `Z_2` matter-link gauge system, because it has finite local dimension independent of any truncation. The reduced `Z_2` matter-only picture is useful for interaction-sensitive coefficients but poor as a primitive locality arena because the Gauss-law strings are nonlocal in the reduced coordinates.

The truncated compact `U(1)` benchmark is a useful second example at fixed `K`, with constants allowed to depend on `K`. It should not be used for `K -> infinity` claims in Paper 3.

## Minimal Publishable Paper 3

A minimal successful V2 Paper 3 should prove or clearly refute:

1. a global-norm warning/no-go showing why fixed finite Neumann estimates are not enough for continuum locality;
2. a precise local topology for raw comparison maps;
3. fixed-order linked-cluster locality, preferably via `L_R=\log J_R` and then exponentiation to `J_R-I`, for bounded finite-range interactions;
4. a finite-slab convergence theorem, now supplied by the paired-word Born-squared activity/KP theorem for the bounded finite-range/common-collar class, upgrading fixed-order LC-log to anchored bounds for `L_R`, `J_R`, and `J_R^{-1}`;
5. inverse coefficient locality for `J_R^{-1}`;
6. an exchange-defect support/window theorem derived from the comparison-map bounds;
7. sectorwise versions for finite gauge constraints;
8. a clear statement of what remains conditional for finite slabs and refinement estimates.

If a benchmark lies outside the Proposition 10 class, the paper should say so and make that benchmark conditional or provide a counterexample. The finite-slab theorem should not be silently exported to reduced nonlocal coordinates, cutoff-removal limits, or sector families whose constants are not uniform.

For item 7, the export to Paper 4 should be explicit:

1. raw `J_R` maps are algebraic relative-dynamics maps, not effects or observables;
2. pseudo-stochastic signs are allowed and do not define operational probabilities by themselves;
3. operational instruments must be added and checked separately;
4. exchange-window bounds are raw support/control data, not a Haag-Kastler reconstruction theorem.

## Stronger Version

A stronger Paper 3 would prove a genuine finite-slab theorem:

For the bounded finite-range class, there is a volume-independent `Delta_*` and anchored quasilocal norm such that `J_R`, `J_R^{-1}`, and `E_{R,S}` satisfy exponential locality bounds for all finite volumes and all supports of bounded geometry.

This would be a major result. It would make the interacting program viable enough to move naturally toward operational observable reconstruction.

## How Existing Interacting Benchmarks Fit

### Common-collar benchmark audit

Proposition 10 only applies to a benchmark presentation if the variables used
in the theorem have a primitive bounded-degree local graph, uniformly finite
local dimension over the claimed refinement family, bounded finite-range
Hamiltonian terms, collar deformations written on the same anchored support
family as the unperturbed Hamiltonian, and explicit sector/cutoff constants.

Under that audit:

1. unconstrained finite-dimensional spin/qudit systems pass;
2. dynamical Abelian finite-link systems pass only at fixed finite link space
   and fixed finite sector family unless refinement-uniform constants are
   proved;
3. unreduced minimal `Z_2` matter-link systems pass and are the best worked
   finite gauge candidate;
4. reduced `Z_2` matter-only systems are coefficient evidence, not automatic
   Proposition 10 inputs, because Gauss-law elimination can create strings or
   global parity data;
5. unreduced truncated compact `U(1)` systems pass at each fixed `K`, with
   constants allowed to depend on `K`;
6. compact-rotor or `K -> infinity` control is not obtained from the fixed-`K`
   theorem;
7. reduced-strip and overlap companions are ledgers and diagnostics, not
   finite-slab inverse-control evidence.

The paper should therefore advertise the theorem as an unreduced
common-collar local theorem. Reduced physical coordinates are useful only after
their inherited locality norm is proved separately.

### Finite quantum-simulator exchange-defect diagnostic

The consolidated draft now includes a technology-facing diagnostic rather than
a claimed QFT deviation. On a small spin/qudit or matter-link simulator, choose
`H`, localized deformations `H_R=H-C_R` and `H_S=H-C_S`, estimate the endpoint
probability matrices

```math
\Gamma_0=|e^{-i\Delta H}|^2,\qquad
\Gamma_R=|e^{-i\Delta H_R}|^2,\qquad
\Gamma_S=|e^{-i\Delta H_S}|^2,
```

then reconstruct

```math
J_R=\Gamma_R\Gamma_0^{-1},\qquad
J_S=\Gamma_S\Gamma_0^{-1},\qquad
E_{R,S}=J_RJ_SJ_R^{-1}J_S^{-1}.
```

The test is whether the raw exchange defect shows the Theorem 4 pattern:
fourth-order onset, separated-support onset suppression, and the
outside-window tail

```math
\|E_{R,S}-I\|_{>w}^{(1),R:S}
\lesssim
\Delta^4e^{-\nu(d_{R,S}+w)}.
```

This is a finite-regulator validation of the ISP exchange-curvature
bookkeeping, not a direct experimental difference from standard QFT. A genuine
operational prediction still belongs to Paper 4.

### Dynamical Abelian finite-link benchmark

Use it as the template for fixed finite sectorwise inverse control and mixed-support definitions. Do not treat its fixed `L,S` constants as continuum estimates.

### Minimal `Z_2` gauge-matter benchmark

Use the unreduced matter-link variables for locality and the reduced block for interaction-sensitive coefficient checks. The phrase "genuinely interacting" must remain tied to the reduced physical-sector Hamiltonian, not to a claim of continuum nonintegrability.

### Truncated compact `U(1)` benchmark

Use it as a fixed-`K` finite local-dimension example. State every estimate with its `K` dependence unless a real `K`-uniform theorem is proved. Respect the no-truncation condition as part of the sector definition.

### Reduced-strip/overlap companion

Use it as coefficient evidence and a source of finite strip bases. Do not use it as inverse-control evidence.

## Failure Modes

Paper 3 should be allowed to fail. The key failure modes are:

1. **Global inverse blowup.** Only global matrix-norm inverse control is available, forcing `Delta` to shrink with volume.
2. **No linked-cluster cancellation.** The reference inverse leaves disconnected global terms in `J_R-I`, destroying anchored locality.
3. **Reduced-coordinate nonlocality.** Gauge-sector elimination turns local matter-link dynamics into nonlocal strings and obscures the primitive locality statement.
4. **Cutoff instability.** Truncated `U(1)` bounds grow uncontrollably with `K`, blocking compact-rotor or continuum gauge claims.
5. **Sector instability.** Bounds hold in each fixed sector but not uniformly over the sector family relevant to refinement.
6. **Projective mismatch.** Coarse-graining maps do not preserve the local topology in which inverse control is proved.
7. **Raw/operational confusion.** A raw comparison-map support theorem is overstated as an observable-locality theorem.

## Relationship To Later V2 Papers

Paper 4 on operational observable reconstruction should not begin until Paper 3 separates two outcomes:

1. raw comparison maps have usable anchored locality, in which case operational instruments can be built on top of them; or
2. raw comparison maps are too nonlocal, in which case Paper 4 must introduce additional operational structure rather than pretending raw `J_R` maps are observable algebras.

Paper 5 on continuum gauge benchmarks needs Paper 3's sectorwise inverse-control machinery before asking for `K`-stability or Schwinger-model-like limits.

Paper 6 on QFT reconstruction needs Paper 3 to say whether stochastic kernel data carry local dynamics robustly enough to reconstruct anything beyond finite benchmark blocks.

## Recommended Immediate Work

Write Paper 3 as an inverse-locality theorem paper with a no-go spine, not as a broad interacting field-theory paper.

Recommended theorem order:

1. define the local/anchored topology;
2. prove the global-norm obstruction;
3. prove fixed-order linked-cluster coefficient locality;
4. prove or isolate the anchored finite-slab inverse theorem;
5. derive exchange-defect window bounds;
6. state sectorwise gauge variants;
7. state the projective refinement corollary using Paper 2.

Consolidated draft:

`relativistic-isp-v2-paper3-interacting-comparison-map-locality.md`

## Bottom Line

V2 Paper 3 should test whether interacting ISP has a real local inverse calculus. The existing finite interacting papers show that exact interacting blocks and first coefficients exist. They do not yet prove that comparison maps and exchange defects stay quasilocal under refinement. The correct next theorem is therefore not "interacting ISP works"; it is a sharp local inverse theorem, or a sharp no-go theorem explaining why the inverse destroys locality.
