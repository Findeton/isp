# Reduced-Strip and Overlap Coefficients for the Minimal Interacting $Z_2$ Gauge-Matter Benchmark in Relativistic ISP

Preprint, not peer reviewed, version 2026-05-28.

*Companion draft to the benchmark paper: broader reduced-strip structure, first four-site coefficients, fixed-strip blocks, and the first overlap shell*

Author: Felix Robles Elvira

Companion draft

Date: March 2026

Extracted from the earlier expanded Paper 15 drafting pass so that the benchmark theorem and the broader coefficient package can be read separately

## Abstract

This companion paper collects the broader reduced-strip and overlap calculations that were previously bundled into the expanded benchmark draft for Paper 15. The benchmark choice itself, the exact Gauss-law elimination theorem, and the first interaction-sensitive three-state prototype coefficient now live in the benchmark paper. The present companion begins where that paper stops: with the question of what survives beyond the minimal reduced two-bond prototype.

At the exact scope extracted here, the disjoint reduced site-block problem is sharpened in three stages. First, no disjoint reduced site-block pair beyond the minimal prototype carries an order-$\Delta^4$ exchange term, and the first broader candidate coefficient is reduced exactly to an order-$\Delta^6$ commutator formula built from the reduced one-region $\Delta^2$ and $\Delta^4$ data. Second, for the first broader class $R_n^{\mathrm{red}},R_{n+3}^{\mathrm{red}}$, the relevant inner-facing boundary-active reduced $\Delta^4$ blocks are explicit on the minimal compressed one-particle and two-particle shells, and the resulting four-site prototype already carries a nonzero end-to-end order-$\Delta^6$ channel. Third, beyond the solved $\ell=3$ family the exact order-$\Delta^6$ coefficient vanishes identically, the next burden is reduced to an order-$\Delta^8$ commutator formula, and the pure two-step overlap shell on the first overlap class $R_n^{\mathrm{red}},R_{n+4}^{\mathrm{red}}$ is already explicit on the minimal one-particle five-site prototype.

## Introduction

Once the benchmark paper has isolated the first interaction-sensitive reduced two-bond prototype coefficient, the next task is no longer benchmark choice. It is bookkeeping on longer reduced strips. The main structural questions are straightforward to state. Does any broader disjoint reduced site-block pair still contribute at order $\Delta^4$? If not, at what first order can a broader coefficient appear? And once it appears, on what exact finite strip basis does it close?

**Main extracted results (informal).**

1. *No broader order-$\Delta^4$ disjoint exchange.* For every disjoint reduced site-block pair with separation $\ell\ge 3$, the order-$\Delta^4$ exchange coefficient vanishes.
2. *First broader structural reduction.* The first broader candidate coefficient occurs at order $\Delta^6$ and is reduced exactly to commutators of the reduced one-region $\Delta^2$ and $\Delta^4$ data.
3. *First broader boundary-active shell data.* On the first broader class $R_n^{\mathrm{red}},R_{n+3}^{\mathrm{red}}$, the relevant inner-facing reduced $\Delta^4$ shell data are explicit on the minimal compressed one-particle and two-particle three-site shells.
4. *First broader four-site prototype coefficient.* The minimal broader four-site reduced-strip prototype already carries a nonzero order-$\Delta^6$ end-to-end spanning-active channel with coefficient $\tfrac12 t^6$.
5. *Fixed-strip block refinements.* With frozen exterior data and inactive outer bonds, the same broader coefficient admits exact one-particle, two-particle, and three-particle strip-sector decompositions.
6. *Post-$\Delta^6$ vanishing.* Every broader disjoint reduced site-block class beyond the solved $\ell=3$ family has vanishing order-$\Delta^6$ coefficient.
7. *First overlap reduction.* The next candidate coefficient is reduced to an order-$\Delta^8$ commutator formula, and on the first overlap class the pure $(4,4)$ shell already isolates to $[A_n^{[4],\mathrm{red}},A_{n+4}^{[4],\mathrm{red}}]$.
8. *First overlap prototype matrix.* On the minimal one-particle five-site overlap prototype, the pure two-step overlap shell is explicit and has end-to-end entry $\tfrac{3}{16}t^8$.

## Broader Reduced-Strip Structure

**Proposition A**

(No order-$\Delta^4$ disjoint site-block exchange beyond the minimal prototype).

For every compatible pair $(\mathbf g,w)$ and every disjoint reduced site-block pair $R_n^{\mathrm{red}},R_{n+\ell}^{\mathrm{red}}$ with $\ell\ge 3$,
$$
E_{n,n+\ell;\mathbf g,w}^{\mathrm{red}}(\Delta)=I+O(\Delta^6).
$$

**Proposition B**

(First broader order-$\Delta^6$ reduction).

For $\ell\ge 3$ one has
$$
E_{n,n+\ell;\mathbf g,w}^{\mathrm{red}}(\Delta)=I+\Delta^6 C_{n,n+\ell;\mathbf g,w}^{[6],\mathrm{red}}+O(\Delta^8),
$$
with
$$
C_{n,n+\ell;\mathbf g,w}^{[6],\mathrm{red}}=
\bigl[A_{n,\mathbf g,w}^{[2],\mathrm{red}},A_{n+\ell,\mathbf g,w}^{[4],\mathrm{red}}\bigr]+
\bigl[A_{n,\mathbf g,w}^{[4],\mathrm{red}},A_{n+\ell,\mathbf g,w}^{[2],\mathrm{red}}\bigr].
$$

## First Broader Four-Site Class

**Proposition C**

(First broader boundary-active shell data).

On the minimal compressed three-site one-particle shell for the one-region reduced coefficient, the right boundary-active block already closes with universal entries
$$
\langle Z|A_{n,\mathbf g,w}^{[4],\mathrm{red}}|Z\rangle=-\frac{1}{12}t^4,
\qquad
\langle Z|A_{n,\mathbf g,w}^{[4],\mathrm{red}}|Y\rangle=\frac13 t^4,
$$
$$
\langle Y|A_{n,\mathbf g,w}^{[4],\mathrm{red}}|Z\rangle=-\frac23 t^4,
\qquad
\langle X|A_{n,\mathbf g,w}^{[4],\mathrm{red}}|Z\rangle=\frac34 t^4,
\qquad
\langle Z|A_{n,\mathbf g,w}^{[4],\mathrm{red}}|X\rangle=-\frac14 t^4,
$$
with the left boundary-active block given by reflection.

**Proposition D**

(First broader four-site prototype coefficient).

On the minimal broader four-site reduced-strip prototype,
$$
\bigl[C_{n,n+3;\mathbf g,w}^{[6],\mathrm{proto}}\bigr]_{X_3,X_0}=\frac12 t^6,
\qquad
\bigl[C_{n,n+3;\mathbf g,w}^{[6],\mathrm{proto}}\bigr]_{X_0,X_3}=-\frac12 t^6.
$$

**Proposition E**

(Fixed-strip block structure at the first broader class).

With frozen exterior data and inactive outer bonds, the full fixed-strip coefficient preserves strip particle number. The zero-particle and four-particle blocks vanish identically, the one-particle block reduces to the already-computed six-channel decomposition, the two-particle block is explicit and interaction sensitive, and the three-particle block is explicit with exact local-gap cancellation.

**Validation remark.**

The current finite-matrix validation script checks this statement at three levels. On an explicit frozen-exterior one-particle four-site fiber with generic diagonal energies and inactive outer bonds, the extracted order-$\Delta^6$ matrix matches the same six-channel decomposition as the minimal four-site prototype, with worst relative error below $10^{-6}$. On the full four-site fixed-strip state space, the computed defect is block diagonal by strip particle number at the tested precision, the zero-particle and four-particle sectors are exactly trivial, and the embedded one-particle block agrees with the same six-channel matrix at the $10^{-6}$ level. The script also extracts the two-particle order-$\Delta^6$ block and compares an interacting parameter choice against the electric-free case; for the tested data the difference is numerically nonzero, providing a direct interaction-sensitivity diagnostic for that block.

## Post-$\Delta^6$ Vanishing and First Overlap Shell

**Proposition F**

(No order-$\Delta^6$ disjoint-site exchange beyond the solved $\ell=3$ family).

For every disjoint reduced site-block pair with separation $\ell\ge 4$,
$$
E_{n,n+\ell;\mathbf g,w}^{\mathrm{red}}(\Delta)=I+O(\Delta^8).
$$

**Proposition G**

(First overlap-class reduction).

Beyond the solved $\ell=3$ family, the next candidate coefficient is reduced exactly to an order-$\Delta^8$ commutator formula built from the logarithmic one-region coefficients $\Lambda^{[2]}$, $\Lambda^{[4]}$, and $\Lambda^{[6]}$. On the first overlap class $R_n^{\mathrm{red}},R_{n+4}^{\mathrm{red}}$, the pure two-step overlap shell already reduces to
$$
[A_n^{[4],\mathrm{red}},A_{n+4}^{[4],\mathrm{red}}].
$$

**Proposition H**

(Minimal one-particle overlap prototype matrix).

On the minimal one-particle five-site overlap prototype, the pure two-step overlap shell is explicit as a universal order-$\Delta^8$ matrix and has end-to-end entry $\tfrac{3}{16}t^8$.

**Proposition H$'$**

(Explicit overlap prototype matrix).

On the minimal one-particle five-site overlap prototype with zero on-site energies and unit hopping $t=1$, the pure two-step overlap shell $[A_n^{[4],\mathrm{red}},A_{n+4}^{[4],\mathrm{red}}]$ closes on the universal order-$\Delta^8$ matrix (rows and columns indexed by sites $0,1,2,3,4$)
$$
\bigl[A_n^{[4],\mathrm{red}},A_{n+4}^{[4],\mathrm{red}}\bigr]
=
t^{8}\,
\begin{pmatrix}
0 & 0 & -\tfrac{1}{16} & \tfrac{1}{4} & -\tfrac{3}{16} \\
0 & 0 & \tfrac{1}{18} & -\tfrac{2}{9} & \tfrac{1}{6} \\
-\tfrac{1}{48} & \tfrac{1}{36} & 0 & -\tfrac{1}{36} & \tfrac{1}{48} \\
-\tfrac{1}{6} & \tfrac{2}{9} & -\tfrac{1}{18} & 0 & 0 \\
\tfrac{3}{16} & -\tfrac{1}{4} & \tfrac{1}{16} & 0 & 0
\end{pmatrix}.
$$
Every entry is a rational multiple of $t^8$, every row and column sums to zero, and the matrix is mirror-antisymmetric, $M_{ij}=-M_{4-i,\,4-j}$. The end-to-end entry $M_{4,0}=\tfrac{3}{16}t^{8}$ of Proposition H is visible in the lower-left corner.

**Proposition H$''$**

(Remaining universal entry of $A^{[4],\mathrm{red}}$).

On the three-site boundary-active block of Proposition C, double stochasticity of $\Gamma$ forces each row and each column of $A^{[4],\mathrm{red}}$ to sum to zero. Together with the five universal entries of Proposition C, those constraints leave one free entry, which takes the universal value
$$
\langle Y|A_{n,\mathbf g,w}^{[4],\mathrm{red}}|X\rangle = -\tfrac{4}{3}t^{4},
$$
and hence the full three-site active block reads
$$
A_{n,\mathbf g,w}^{[4],\mathrm{red}}\Big|_{\{X,Y,Z\}}
=
t^{4}\,
\begin{pmatrix}
\tfrac{19}{12} & -\tfrac{7}{3} & \tfrac{3}{4} \\
-\tfrac{4}{3} & 2 & -\tfrac{2}{3} \\
-\tfrac{1}{4} & \tfrac{1}{3} & -\tfrac{1}{12}
\end{pmatrix}.
$$

**Validation remark.**

The finite-matrix validation script now also records an explicit Proposition H check. On the five-site one-particle prototype above, it fits $A_n^{[4],\mathrm{red}}$ and $A_{n+4}^{[4],\mathrm{red}}$ from the comparison maps $J_n(\Delta)$ and $J_{n+4}(\Delta)$ at four small $\Delta$ values, extracts the $\Delta^4$ coefficient in each entry, and forms the commutator. The extracted end-to-end entry $[A_n^{[4],\mathrm{red}},A_{n+4}^{[4],\mathrm{red}}]_{4,0}$ agrees with $\tfrac{3}{16}t^8$ with relative error below $2\times 10^{-10}$. Every other entry of the $5\times 5$ matrix in Proposition H$'$ is reproduced at the same precision. The three-site active block of $A_n^{[4],\mathrm{red}}$ reported in the script matches the matrix of Proposition H$''$, recovering the five entries of Proposition C and exhibiting the additional universal entry $\langle Y|A^{[4],\mathrm{red}}|X\rangle=-\tfrac{4}{3}t^4$ directly from the finite-matrix data.

## Conclusion

Read together, the two Paper 15 drafts now say something cleaner than the earlier expanded manuscript said by itself. The benchmark paper proves that exact Gauss-law elimination already produces a reduced interacting matter problem and a first interaction-sensitive prototype coefficient. The present companion shows how the next strip and overlap burdens are organized once that benchmark is in hand.

## References

1. [1] Anonymous, “Minimal Genuinely Interacting Gauge-Matter Benchmark in Relativistic ISP,” benchmark draft (2026).
2. [2] Anonymous, “Dynamical Abelian Gauge Field and Gauss-Law Sectors in Relativistic ISP,” preprint (2026).
3. [3] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” preprint (2025).
