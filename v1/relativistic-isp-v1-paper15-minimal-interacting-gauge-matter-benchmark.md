# Minimal Genuinely Interacting Gauge-Matter Benchmark in Relativistic ISP

*Fixed finite $Z_2$ matter-link sectors, exact physical-sector elimination, a conventional-physics interpretation, and finite-block validation*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Refocused benchmark draft for Paper 15 in the relativistic ISP sequence; the broader reduced-strip and overlap package has been extracted to a companion draft

## Abstract

The present relativistic ISP stack already closes a static lattice-$U(1)$ benchmark, a finite dynamical Abelian matter-link benchmark, an operational detector/control phase, an induced-net Einstein-causality bridge, and a boundary-flux-resolved refinement of physical-sector locality. What it did not yet contain at benchmark level was the first case in which exact physical-sector elimination itself produces a reduced matter Hamiltonian that is no longer bilinear while all primitive objects remain exact finite configuration-space objects. That is the purpose of the present paper.

As the smallest clean benchmark of that type, we introduce a fixed finite one-dimensional periodic $Z_2$ lattice gauge theory with fermionic matter. The model is finite-dimensional from the start: matter occupies a finite fermionic configuration space, links carry two-state $Z_2$ electric variables, and the combined gauge-invariant Hamiltonian is defined directly on the matter-link space. We prove exact Gauss-sector decomposition and then show that on every compatible fixed Gauss sector and fixed global $Z_2$ flux block the link field can be eliminated exactly. The resulting reduced Hamiltonian contains ordinary fermion hopping together with a parity-string electric term depending nonlinearly on the occupation configuration. In that precise reduced-space sense, the benchmark is the first genuinely interacting gauge-matter phase of the series. We then compute the first exact interaction-sensitive exchange-defect coefficient on the minimal reduced two-bond strip prototype.

Two additions sharpen the draft relative to the earlier expanded version. First, a dedicated conventional-physics section states explicitly what this reduced interaction does and does not mean from the standpoint of standard one-dimensional lattice gauge theory: the claim is about the exact reduced matter description after Gauss-law elimination, not yet about nonintegrability, duality obstruction, or a continuum interacting local-net theorem. Second, a finite-block validation section records direct numerical checks of the prototype comparison maps and exchange defects appearing in the proofs of the benchmark theorem and the first broader companion calculations. The broader reduced-strip and overlap coefficient package is now separated into a companion paper so that the benchmark result stands on its own.

Scope note. The theorem-level content of the present benchmark paper is the finite $Z_2$ matter-link setup, exact local gauge symmetry, exact Gauss-sector decomposition, exact physical/global-flux elimination, the reduced interacting matter Hamiltonian, the reduced finite-kernel primitive/comparison-map/exchange-defect package on each fixed block, the exact two-step support statement for the one-region reduced order-$\Delta^4$ coefficient, and the first exact interaction-sensitive exchange-defect coefficient on the minimal reduced two-bond strip prototype. The broader reduced-strip and overlap package has been extracted to the companion draft “Reduced-Strip and Overlap Coefficients for the Minimal Interacting $Z_2$ Gauge-Matter Benchmark in Relativistic ISP.”

## Introduction

The preceding paper closes the structural issue that had to be settled before any interacting benchmark could be maximally informative: on the physical Gauss sector, the finite matter-link benchmark fails naive factorization but obeys center-resolved locality once the correct boundary data are retained. That clarification changes the next question. The next question is no longer whether the noninteracting or preserving-class gauge benchmark already hid a better locality theorem. The next question is which interacting benchmark first tests how far the exact finite-kernel machinery can go once genuine physical-sector interaction is present.

The roadmap answer is conservative for good reason. The first genuinely interacting benchmark should not be a compact-rotor $U(1)$ theory on which the primitive kernels immediately cease to be finite matrices, and it should not be a continuum model imported before the finite stochastic problem has even been fixed. The cleanest next benchmark is the smallest finite-dimensional gauge theory in which Gauss-law elimination leaves a nontrivial reduced matter Hamiltonian on each physical sector. In one spatial dimension, the natural choice is a finite periodic $Z_2$ lattice gauge theory with fermionic matter.

This choice is conservative in exactly the Barandes sense. The enlarged problem remains an ordinary finite configuration-space problem. The gauge field is dynamical, but each link carries only two electric states. The primitive kernels, localized deformations, comparison maps, and exchange defects therefore remain exact finite objects on every fixed benchmark size. At the same time, the benchmark is genuinely interacting in the specific sense that matters here: after exact sector reduction, the effective matter Hamiltonian is not merely a free bilinear benchmark with a passive background attached afterward. It contains a nontrivial string-electric term that depends on the occupation profile itself.

That qualification matters. The phrase *genuinely interacting* in the present paper always refers to the *reduced matter description after exact Gauss-sector/global-flux elimination*. In those reduced variables the electric contribution is not a one-body operator; it is a parity-string interaction. At the same time, that reduced interaction is generally nonlocal in the chosen reduced coordinates, because the elimination trades local link data for occupation-prefix strings. The unreduced matter-link benchmark itself remains a local finite lattice gauge theory. Section VI returns to this point in conventional lattice-gauge-theory language.

The conceptual role of the present paper is therefore narrow and deliberate. It fixes the correct benchmark, proves the exact reduction theorem that makes the phrase “genuinely interacting gauge-matter benchmark” mathematically literal at finite scope, and computes the first exact interaction-sensitive coefficient on the right reduced-strip prototype. The broader reduced-strip and overlap package is real progress, but it obscures the benchmark if it is left in the same manuscript; it now lives in the companion draft.

**Main results (informal).**

1. *Exact finite $Z_2$ benchmark.* The first genuinely interacting gauge-matter phase can be formulated on an ordinary finite matter-plus-link configuration space with two-state link variables.
2. *Exact local gauge symmetry.* The combined Hamiltonian and the localized mixed-support deformations commute with the local $Z_2$ Gauss generators.
3. *Exact Gauss-sector decomposition.* The full and localized dynamics decompose exactly into fixed Gauss sectors.
4. *Exact physical-sector elimination.* On each compatible Gauss sector and fixed global $Z_2$ flux block, the link-electric data are reconstructed exactly from matter data and the global flux label.
5. *Reduced interacting Hamiltonian.* The transported Hamiltonian on the reduced sector contains ordinary hopping together with a parity-string electric term that is not reducible to a one-body occupation operator.
6. *Exact reduced finite-kernel setup.* Primitive kernels, comparison maps, and exchange defects remain exact finite objects on each reduced block.
7. *Exact two-step support of the one-region reduced $\Delta^4$ coefficient.* The first nontrivial one-region reduced coefficient beyond order $\Delta^2$ already leaves all exterior data outside the two-step neighborhood unchanged.
8. *Exact first interaction-sensitive reduced-strip prototype coefficient.* On the minimal reduced two-bond strip prototype, the first disjoint site-block exchange channel is explicit through the first order at which the reduced diagonal interaction changes its value.
9. *Conventional-physics clarification.* The interaction claim is about the exact reduced description after elimination; the paper does not yet claim nonintegrability, absence of a simpler dual formulation, or a continuum interacting local-net theorem.
10. *Finite-block validation.* The prototype comparison maps and exchange defects used in the benchmark theorem and first companion calculations are directly reproducible by exact finite-matrix evaluation.

## Fixed finite $Z_2$ matter-link benchmark

**Definition 1**

(Fixed finite periodic $Z_2$ matter-link configuration space).

Fix a ring of $L$ sites labeled modulo $L$ and let
$$
\Omega_L^{\mathrm{matt}}:=\{X\subseteq \Lambda_L\}
$$
be the spinless fermion occupation space, where $X$ records the occupied sites and
$$
N_n(X)\in\{0,1\}
$$
denotes the occupation number at site $n$. Let each link carry a two-state electric variable
$$
\varepsilon_{n+1/2}\in\{\pm 1\}.
$$
The full finite matter-link configuration space is
$$
\Omega_L^{Z_2}:=\Omega_L^{\mathrm{matt}}\times\{\pm 1\}^{L},
$$
whose elements are written
$$
\omega=(X,\boldsymbol\varepsilon),
\qquad
\boldsymbol\varepsilon=(\varepsilon_{1/2},\varepsilon_{3/2},\dots,\varepsilon_{L-1/2}).
$$

Remark.

The decisive point is finiteness. At fixed $L$, the matter configuration space and the link-electric configuration space are both finite, so all kernel-level objects remain finite matrices throughout the benchmark.

**Definition 2**

($Z_2$ link operators and matter operators).

On each link define Pauli operators
$$
\widehat X_{n+1/2},\qquad \widehat Z_{n+1/2},
$$
with
$$
\widehat X_{n+1/2}|\varepsilon\rangle=\varepsilon |\varepsilon\rangle,
\qquad
\widehat Z_{n+1/2}|\varepsilon\rangle=|-\varepsilon\rangle.
$$
On the matter sector let
$$
c_n,\quad c_n^\dagger,\quad \widehat N_n=c_n^\dagger c_n
$$
be the fermionic annihilation, creation, and occupation operators. Fix background parities
$$
q_n^{\mathrm{bg}}\in\{0,1\}.
$$

**Definition 3**

(Gauge generators and the combined benchmark Hamiltonian).

Define the local $Z_2$ Gauss generators by
$$
\widehat G_n:=\widehat X_{n-1/2}(-1)^{\widehat N_n+q_n^{\mathrm{bg}}}\widehat X_{n+1/2},
$$
and the gauge-invariant matter-link Hamiltonian by
$$
\widehat H_{L}^{Z_2}
:=
m\sum_{n=0}^{L-1}(-1)^n\widehat N_n
-t\sum_{n=0}^{L-1}\bigl(c_n^\dagger \widehat Z_{n+1/2} c_{n+1}+c_{n+1}^\dagger \widehat Z_{n+1/2} c_n\bigr)
-h\sum_{n=0}^{L-1}\widehat X_{n+1/2},
$$
with periodic site indexing.

**Proposition 1**

(Exact local gauge symmetry and Gauss-sector decomposition).

For every site $n$,
$$
[\widehat G_n,\widehat H_{L}^{Z_2}]=0.
$$
Hence the full dynamics, every polynomial in the Hamiltonian, and every finite-time propagator decompose exactly into common eigenspaces of the commuting family $\{\widehat G_n\}_{n=0}^{L-1}$.

Proof sketch.

The mass term commutes with every $\widehat G_n$ because it depends only on the occupations. The electric term commutes because it is diagonal in the same $\widehat X$ variables that appear in the Gauss generators. For the hopping term, the two fermion operators change the parities at the two endpoint sites while the link operator $\widehat Z_{n+1/2}$ flips the adjacent $\widehat X_{n+1/2}$ eigenvalue. These changes compensate exactly in the adjacent Gauss generators, so the full term commutes with every $\widehat G_n$.

$ \square $

## Exact physical-sector elimination on fixed global-flux blocks

**Definition 4**

(Compatible Gauss sector and global-flux seed).

Fix a Gauss-sector label
$$
\mathbf g=(g_0,\dots,g_{L-1}),\qquad g_n\in\{\pm 1\},
$$
and a global-flux seed $w\in\{\pm 1\}$. Write $\Omega_{L,\mathbf g,w}^{\mathrm{red}}$ for the set of matter configurations $X\in\Omega_L^{\mathrm{matt}}$ satisfying
$$
\prod_{n=0}^{L-1} g_n=\prod_{n=0}^{L-1}(-1)^{N_n(X)+q_n^{\mathrm{bg}}},
$$
so that the recursive Gauss law closes consistently around the ring.

**Theorem 1**

(Exact recursion and physical-sector elimination on fixed $(\mathbf g,w)$).

Fix a compatible Gauss sector $\mathbf g$ and global-flux seed $w$. Then:

1. *Exact recursion.* Every basis state in the corresponding sector satisfies
  $$
  \varepsilon_{n+1/2}=g_n(-1)^{N_n(X)+q_n^{\mathrm{bg}}}\varepsilon_{n-1/2},
  $$
  hence
  $$
  \varepsilon_{n+1/2}=w\prod_{j=0}^{n} g_j(-1)^{N_j(X)+q_j^{\mathrm{bg}}}.
  $$
2. *Exact elimination.* The map $\iota_{\mathbf g,w}:\Omega_{L,\mathbf g,w}^{\mathrm{red}}\to \Omega_L^{Z_2}$ sending $X$ to the unique sector-compatible matter-link configuration $\bigl(X,\boldsymbol\varepsilon^{(\mathbf g,w)}(X)\bigr)$ is a bijection onto the fixed $(\mathbf g,w)$ block of the full benchmark.
3. *Reduced Hamiltonian.* Transporting the fixed-block Hamiltonian through $\iota_{\mathbf g,w}$ yields a reduced matter Hamiltonian $\widehat H_{\mathbf g,w}^{\mathrm{red}}$ acting on the reduced matter space alone.

**Corollary 1**

(Explicit reduced interacting Hamiltonian).

On the reduced matter space of a fixed compatible pair $(\mathbf g,w)$, the transported Hamiltonian has the form
$$
\widehat H_{\mathbf g,w}^{\mathrm{red}}
=
m\sum_{n=0}^{L-1}(-1)^n\widehat N_n
-t\sum_{n=0}^{L-1}\bigl(c_n^\dagger c_{n+1}+c_{n+1}^\dagger c_n\bigr)
-h\sum_{n=0}^{L-1}w\prod_{j=0}^{n} g_j(-1)^{\widehat N_j+q_j^{\mathrm{bg}}}.
$$

**Proposition 2**

(Genuine interaction on the reduced sector).

Assume $L\ge 3$ and $h\neq 0$. Then the electric part of $\widehat H_{\mathbf g,w}^{\mathrm{red}}$ cannot be reduced to a constant plus a one-body occupation operator $a_0+\sum_n a_n \widehat N_n$.

Remark.

This is the benchmark’s whole point. The claim is deliberately narrower than any statement about nonintegrability, chaos, or irreducibility under further duality transformations; the point here is only that exact physical-sector elimination no longer leaves a purely bilinear matter Hamiltonian.

## Reduced Primitive Kernels, Comparison Maps, and Exchange Defects

Once a fixed compatible pair $(\mathbf g,w)$ has been chosen, the reduced benchmark is again an ordinary finite stochastic problem. That is the exact continuation of the ISP methodology, now at genuinely interacting gauge-matter scope.

**Definition 5**

(Reduced primitive kernel package on a fixed $(\mathbf g,w)$ block).

Fix a reference slab and a gauge-compatible mixed region $R$. Let $\widehat H_{\mathbf g,w}^{\mathrm{red}}$ be the reduced Hamiltonian of Corollary 1 and let $\widehat H_{R,\mathbf g,w}^{\mathrm{red}}$ denote the corresponding reduced localized Hamiltonian obtained by transporting the mixed-support localized deformation of the full $Z_2$ benchmark through the elimination map $\iota_{\mathbf g,w}$. Define the reduced primitive kernels, comparison maps, and exchange defects exactly as in the previous papers, but now on the finite reduced configuration space $\Omega_{L,\mathbf g,w}^{\mathrm{red}}$.

**Theorem 2**

(Exact finite-kernel interacting benchmark package on fixed reduced blocks).

For every fixed compatible pair $(\mathbf g,w)$:

1. the reduced configuration space is finite;
2. the reduced full and localized propagators are finite matrices;
3. the corresponding primitive kernels, comparison maps, and exchange defects are therefore exact finite objects on the reduced interacting benchmark.

**Definition 5A**

(Reduced bond-transfer kernels on a fixed $(\mathbf g,w)$ block).

For a bond $b=n+\tfrac12$ and reduced configurations $X,X'\in \Omega_{L,\mathbf g,w}^{\mathrm{red}}$, define the reduced bond-transfer kernel by
$$
\bigl[\mathsf T_b^{(\mathbf g,w)}\bigr]_{X',X}
:=
\begin{cases}
1, & X' \text{ is obtained from }X\text{ by moving one fermion across }b,\\
0, & \text{otherwise}.
\end{cases}
$$
Let $\mathsf D_b^{(\mathbf g,w)}$ be the corresponding diagonal degree kernel and set $\mathsf Q_b^{(\mathbf g,w)}:=\mathsf D_b^{(\mathbf g,w)}-\mathsf T_b^{(\mathbf g,w)}$.

**Proposition 3**

(Exact first one-region coefficient on reduced site blocks).

On every fixed compatible pair $(\mathbf g,w)$,
$$
J_{R_n^{\mathrm{red}},\mathbf g,w}(\Delta)=I+\Delta^2 A_{n,\mathbf g,w}^{[2],\mathrm{red}}+O(\Delta^4),
$$
with
$$
A_{n,\mathbf g,w}^{[2],\mathrm{red}}=t^2\Bigl(\mathsf Q_{n-1/2}^{(\mathbf g,w)}+\mathsf Q_{n+1/2}^{(\mathbf g,w)}\Bigr).
$$

**Proposition 3A**

(Exact two-step reduced support of the one-region $\Delta^4$ coefficient).

For every fixed compatible pair $(\mathbf g,w)$ and reduced site block $R_n^{\mathrm{red}}$, there exists an exact coefficient $A_{n,\mathbf g,w}^{[4],\mathrm{red}}$ such that
$$
J_{R_n^{\mathrm{red}},\mathbf g,w}(\Delta)=I+\Delta^2A_{n,\mathbf g,w}^{[2],\mathrm{red}}+\Delta^4A_{n,\mathbf g,w}^{[4],\mathrm{red}}+O(\Delta^6),
$$
and if $\bigl[A_{n,\mathbf g,w}^{[4],\mathrm{red}}\bigr]_{X',X}\neq 0$, then $X$ and $X'$ agree outside the two-step neighborhood $\{n-2,n-1,n,n+1,n+2\}$.

## First Exact Interacting Coefficient on the Minimal Reduced Strip Prototype

**Definition 6**

(Minimal reduced two-bond strip prototype and diagonal energy gaps).

Fix disjoint reduced site blocks $R_n^{\mathrm{red}}$ and $R_{n+2}^{\mathrm{red}}$, and let $\mathcal E_{\mathbf g,w}(X)$ denote the reduced diagonal energy of a configuration $X$,
$$
\mathcal E_{\mathbf g,w}(X):=m\sum_{r=0}^{L-1}(-1)^rN_r(X)-h\sum_{r=0}^{L-1}\lambda_r\sigma_r(X),
$$
where $\lambda_r:=w\prod_{j=0}^{r}g_j(-1)^{q_j^{\mathrm{bg}}}$ and $\sigma_r(X):=\prod_{j=0}^{r}(-1)^{N_j(X)}$. The associated minimal reduced two-bond strip prototype is the compressed three-state problem built from basis configurations $X,Y,Z$ that agree outside $\{n,n+1,n+2\}$ and have local occupations $001$, $010$, and $100$, respectively. Define the corresponding reduced diagonal energy gaps by
$$
\delta_{n+3/2}(X):=\mathcal E_{\mathbf g,w}(X)-\mathcal E_{\mathbf g,w}(Y),
\qquad
\delta_{n+1/2}(Y):=\mathcal E_{\mathbf g,w}(Z)-\mathcal E_{\mathbf g,w}(Y).
$$

**Theorem 3**

(First exact interaction-sensitive coefficient on the minimal reduced two-bond strip prototype).

Fix a compatible pair $(\mathbf g,w)$. Let $J_{n,\mathbf g,w}^{\mathrm{proto}}(\Delta)$ and $J_{n+2,\mathbf g,w}^{\mathrm{proto}}(\Delta)$ denote the site-block comparison maps compressed to the prototype basis $\{X,Y,Z\}$, and define the corresponding exchange defect
$$
E_{n,n+2;\mathbf g,w}^{\mathrm{proto}}(\Delta)
:=
J_{n,\mathbf g,w}^{\mathrm{proto}}(\Delta)J_{n+2,\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigl[J_{n,\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigr]^{-1}\bigl[J_{n+2,\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigr]^{-1}.
$$
Then
$$
\bigl[E_{n,n+2;\mathbf g,w}^{\mathrm{proto}}(\Delta)\bigr]_{Z,X}
=
t^4\Delta^4
+
t^4\left[\frac{13}{6}t^2-\frac{1}{12}\Bigl(\delta_{n+3/2}(X)^2+\delta_{n+1/2}(Y)^2\Bigr)\right]\Delta^6
+O(\Delta^8).
$$

Remark.

Theorem 3 is the first exact interacting coefficient actually earned by Paper 15. It is the benchmark result that the expanded draft was in danger of burying under its later strip package.

## Conventional Physics Interpretation

It is worth stating explicitly how this benchmark sits relative to standard one-dimensional lattice gauge theory. The unreduced model of Definition 3 is an ordinary finite $Z_2$ lattice gauge theory with fermionic matter on a periodic one-dimensional lattice. In that unreduced description the locality statement is the standard microscopic one: matter lives on sites, gauge variables live on links, Gauss generators impose the local constraint, and the Hamiltonian couples nearest-neighbor matter transport to a link flip.

What is new is the exact reduced matter description obtained after solving the Gauss law on a fixed sector and fixed global-flux block. In one spatial dimension that elimination is expected to trade local link data for nonlocal strings in whatever reduced coordinates one chooses. The prefix-parity strings in Corollary 1 are the finite $Z_2$ version of that phenomenon. They therefore should not be read as a failure of microscopic locality in the underlying gauge theory. They are the price of eliminating constrained link variables in a one-dimensional gauge system and writing everything in matter variables alone.

In more conventional lattice-gauge-theory language, the benchmark sits in a familiar part of the landscape. The fixed $(\mathbf g,w)$ reduction is the one-dimensional finite-volume analogue of solving the Gauss law after choosing a gauge-invariant sector and then keeping the residual global flux datum that survives on the ring. The label $w$ plays exactly that role: it is not a local degree of freedom, but a topological sector label left over after the local recursion has been solved. Readers coming from the standard Wegner / Fradkin-Susskind / Kogut line of thought should therefore think of Corollary 1 as an exact finite-sector elimination formula, not as an exotic claim that the underlying $Z_2$ gauge theory has become fundamentally nonlocal.

The same comparison helps calibrate the phrase *genuinely interacting*. In standard one-dimensional $Z_2$ gauge-matter systems, gauge fixing, duality, and fermion-to-spin rewritings can move apparent nonlocality and interaction between different variable choices. The present paper does not claim to outrun that literature. Its narrower claim is that, in the exact reduced occupation variables selected by the ISP elimination map, the electric contribution is no longer a one-body term and the first reduced exchange-defect correction already depends on the resulting gap data. That is a meaningful benchmark statement even before one decides whether another dual description may simplify the same physics.

This is also why the phrase *genuinely interacting* has to be handled with care. Proposition 2 proves a sharp reduced-space statement: on the fixed reduced block the electric term is not a constant plus a one-body occupation operator. That is enough to show that exact elimination no longer leaves a purely bilinear matter problem in the chosen reduced coordinates. It is *not* yet a theorem that the model is nonintegrable, chaotic, or impossible to simplify by a further duality or nonlocal change of variables. One-dimensional $Z_2$ gauge-matter systems are precisely the class in which dual reformulations can be subtle and powerful, so a stronger claim would need independent work beyond the benchmark theorem.

**Physics boundary.**

The invariant claim of the present paper is therefore modest but real: exact Gauss-law elimination on the minimal finite $Z_2$ benchmark produces a reduced matter Hamiltonian that is non-bilinear in the reduced occupation variables, and the first reduced exchange-defect correction already depends on the resulting gap data. Whether that reduced interaction is the most informative variable choice, or whether a simpler dual description exists, is intentionally left open here.

## Finite-Block Validation

The benchmark and companion prototype formulas can be checked directly because all matrices involved are finite and small. A companion validation script, *validate_minimal_interacting_gauge_matter_benchmark.py*, evaluates the relevant finite-dimensional propagators, primitive kernels, comparison maps, and exchange defects by direct matrix computation. The checks are deliberately finite and local: they reproduce the exact compressed matrices used in the proofs rather than attempting an unnecessary large-volume simulation.

Three validations are especially useful. First, on the three-state prototype of Theorem 3, direct evaluation recovers the order-$\Delta^4$ and order-$\Delta^6$ coefficients of the spanning-active exchange-defect entry. Second, on the three-state one-region shell used in the companion paper, direct evaluation of the one-region comparison map reproduces the order-$\Delta^4$ coefficients of the right boundary-active block. Third, on the four-state broader prototype used for the first companion coefficient, direct evaluation of the two comparison maps reproduces the end-to-end order-$\Delta^6$ coefficient. The current validation layer now also checks both an explicit frozen-exterior one-particle four-site fiber and the full four-site fixed-strip state space with generic diagonal energies and inactive outer bonds. In the latter check, the exact block decomposition by strip particle number is visible numerically: cross-sector entries vanish, the vacuum and fully occupied sectors remain trivial, and the embedded one-particle block matches the same six-channel decomposition used in the companion draft. Finally, the script extracts the two-particle order-$\Delta^6$ block on the same fixed strip and compares an interacting parameter choice against the electric-free case, giving a direct numerical diagnostic that the two-particle block is interaction sensitive for the tested data.

For the current validation script, the extracted Theorem 3 prototype coefficients agree with the stated values at relative errors $2\times 10^{-15}$ for the order-$\Delta^4$ term and $6.4\times 10^{-12}$ for the order-$\Delta^6$ term. On the first broader shell, the off-diagonal Proposition 4C entries are reproduced at relative errors between $10^{-15}$ and $10^{-10}$. On the first broader four-site prototype, the extracted Proposition 4D coefficient agrees with $\tfrac12 t^6$ at relative error $2.4\times 10^{-14}$. On a generic frozen-exterior one-particle four-site fiber, the full extracted order-$\Delta^6$ matrix agrees with the expected six-channel decomposition with worst relative error $6.7\times 10^{-7}$. On the full four-site fixed-strip state space, the numerically extracted defect is exactly block diagonal by strip particle number at the tested precision, the zero-particle and four-particle sectors are exactly trivial, and the embedded one-particle block agrees with the expected six-channel matrix with worst relative error $1.2\times 10^{-6}$. On the same fixed strip, the extracted two-particle order-$\Delta^6$ block is antisymmetric up to $6.1\times 10^{-7}$ and differs from the electric-free block by a maximum entry size $1.3\times 10^{-6}$ for the tested parameter choice, which is consistent with the companion paper’s interaction-sensitive two-particle claim. At benchmark stage, that is the right kind of independent check: the exact finite prototype formulas are not only derivable on paper but directly recoverable from the underlying matrices.

## Conclusion

The current relativistic ISP stack had reached the point where “interacting benchmark” needed to stop being a slogan and become a finite exact object. This draft fixes that object. The first genuinely interacting benchmark is naturally a finite periodic $Z_2$ lattice gauge theory with fermionic matter, because it preserves the exact finite-kernel methodology while producing a genuinely interacting reduced matter Hamiltonian after exact sector elimination.

The benchmark is now cleaner than in the earlier expanded draft for three reasons. The benchmark theorem and its first exact prototype coefficient stand without the later strip package obscuring them. The conventional-physics interpretation now says directly what the reduced interaction does and does not mean. And the finite-block validation layer makes the first benchmark formulas independently checkable by exact matrix evaluation. The next step is no longer to enlarge the prose around the benchmark. It is to finish the extracted companion program on broader reduced strips and overlap shells, and only then decide how much of that structure survives more ambitious continuations.

## References

1. [1] Anonymous, “Dynamical Abelian Gauge Field and Gauss-Law Sectors in Relativistic ISP,” preprint (2026).
2. [2] Anonymous, “Boundary-Flux-Resolved Einstein Causality in Relativistic ISP,” preprint (2026).
3. [3] Anonymous, “Reduced-Strip and Overlap Coefficients for the Minimal Interacting $Z_2$ Gauge-Matter Benchmark in Relativistic ISP,” companion draft (2026).
4. [4] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025).
5. [5] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” preprint (2025).
6. [6] F. J. Wegner, “Duality in Generalized Ising Models and Phase Transitions without Local Order Parameters,” *J. Math. Phys.* **12**, 2259 (1971).
7. [7] E. Fradkin and L. Susskind, “Order and Disorder in Gauge Systems and Magnets,” *Phys. Rev. D* **17**, 2637 (1978).
8. [8] J. B. Kogut, “An Introduction to Lattice Gauge Theory and Spin Systems,” *Rev. Mod. Phys.* **51**, 659 (1979).
9. [9] U.-J. Wiese, “Ultracold Quantum Gases and Lattice Systems: Quantum Simulation of Lattice Gauge Theories,” *Annalen der Physik* **525**, 777 (2013).
