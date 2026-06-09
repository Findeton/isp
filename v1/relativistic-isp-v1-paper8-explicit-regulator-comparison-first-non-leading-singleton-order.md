# Explicit Regulator Comparison at the First Non-Leading Singleton Order

*Interior-shell nonuniversality, boundary-shell scaling, and exact $c_\lambda^2$ strip-moment universality*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 8 in the relativistic ISP sequence; exact first non-leading regulator comparison in the singleton class

## Abstract

Phase 5 identified normalized strip moments as the correct regulator-stability data, but the first explicit non-leading comparison still had to be performed. This paper does that at the first genuinely new singleton order for the admissible family
$$
U_n^{(\lambda)}(\Delta)=e^{-i\Delta(H_D-\lambda C_n)},
\qquad
c_\lambda:=\lambda(2-\lambda).
$$

The answer is sharper than either a naive universality claim or a naive nonuniversality claim. The full singleton coefficient $A_{n,\lambda}^{(2)}$ is *not* equal to $c_\lambda A_n^{(2)}$: the difference is an exact interior-shell operator with nonzero mass-dependent entries for every $0<\lambda<1$. So raw one-region non-leading coefficient data are genuinely regulator-dependent. But the boundary-facing shell of $A_{n,\lambda}^{(2)}$ that actually communicates across a gap of three lattice steps still scales exactly by the same factor $c_\lambda$. Consequently, the first separation-controlled exchange coefficient obeys the exact identity
$$
C_{n,n+3;\lambda}^{(3)}=c_\lambda^2\,C_{n,n+3}^{(3)},
$$
and the normalized first strip moments are regulator-independent throughout the admissible $\lambda$-family. Thus the first non-leading singleton comparison answers the physical question precisely: some regulator differences survive microscopically in $A^{(2)}$, but they do not yet survive in the first normalized strip-moment data. The Lie-Trotter benchmark remains a different onset class and is therefore an explicit contrast, not a same-order comparator, at this stage.

## Introduction

Phase 5 reformulated the regulator question in the right language. “Same continuum law” cannot mean equality of raw local coefficients, because that already fails at leading order across the admissible $\lambda$-family. What it could still mean is equality of the properly normalized strip-moment data extracted from the exact exchange algebra.

The first place where that question becomes genuinely nontrivial is the singleton distance-three coefficient computed in phase 6. At that order one must compare order-$\Delta^4$ one-region coefficients, not just the already-known leading coefficient $A_n^{(1)}$. The purpose of the present paper is to perform that exact comparison and to say, without overclaiming, which regulator differences are merely onset artifacts and which are genuine microscopic nonuniversality.

**Main results (informal).**

1. *Exact raw nonuniversality.* The full singleton coefficient $A_{n,\lambda}^{(2)}$ is not a simple multiple of the collar-excision coefficient $A_n^{(2)}$ for $0 < \lambda < 1$.
2. *Exact location of the new regulator dependence.* The difference $A_{n,\lambda}^{(2)}-c_\lambda A_n^{(2)}$ is supported entirely in the interior shell $\{n-1,n,n+1\}$.
3. *Exact first non-leading strip-moment universality.* The distance-three singleton exchange coefficient nevertheless obeys
  $C_{n,n+3;\lambda}^{(3)}=c_\lambda^2C_{n,n+3}^{(3)}$, so the normalized first strip moments coincide across the whole admissible $\lambda$-family.
4. *Lie-Trotter contrast.* The Lie-Trotter rule remains in a distinct onset class with $J_n^{\mathrm{LT}}=I+O(\Delta^4)$ and $E_{n,n+3}^{\mathrm{LT}}=I+O(\Delta^8)$, so no same-order distance-three comparison exists there.

Scope note. The exact comparison carried out here is the first non-leading singleton comparison inside the common $\Delta^2$-onset class. We do not claim a full higher-order regulator classification for larger support types, and we do not claim a same-order strip-moment comparison with the Lie-Trotter benchmark, whose exchange onset is later.

## Setup

For the singleton support $R_n=\{n\}$, define
$$
J_n^{(\lambda)}(\Delta)
=
I+\Delta^2A_{n,\lambda}^{(1)}+\Delta^4A_{n,\lambda}^{(2)}+O(\Delta^6),
$$
with the collar-excision rule recovered at $\lambda=1$:
$$
A_n^{(k)}:=A_{n,\lambda=1}^{(k)}.
$$
The exact leading-order result from the explicit free-model sequel is
$$
A_{n,\lambda}^{(1)}=c_\lambda A_n^{(1)},
\qquad
c_\lambda:=\lambda(2-\lambda).
$$
The new comparison object is therefore
$$
D_n^{(\lambda)}:=A_{n,\lambda}^{(2)}-c_\lambda A_n^{(2)}.
$$

**Definition 1**

(Interior and boundary shells for the singleton $A^{(2)}$ comparison).

For the singleton centered at $n$, call
$$
\{n-1,n,n+1\}
$$
the

*interior shell*

and
$$
\{n-2,n+2\}
$$
the

*boundary shell*

of the order-$\Delta^4$ coefficient. The boundary-active block consists of matrix entries with one site in the boundary shell and the other site in $\{n-2,n-1,n,n+1,n+2\}$.

## Exact raw nonuniversality at order $\Delta^4$

**Proposition 1**

(Exact interior-shell correction to the singleton coefficient).

For the admissible $\lambda$-family one has
$$
D_n^{(\lambda)}:=A_{n,\lambda}^{(2)}-c_\lambda A_n^{(2)},
\qquad c_\lambda=\lambda(2-\lambda),
$$
and $D_n^{(\lambda)}$ is supported entirely in the interior shell $\{n-1,n,n+1\}$. Its nonzero entries are generated by the exact formulas
$$
\langle n,\uparrow|D_n^{(\lambda)}|n,\uparrow\rangle
=
-\frac{4}{3}\lambda(1-\lambda)^2(2-\lambda)h^4
-\frac16\lambda(1-\lambda)^2(4-\lambda)m^2h^2,
$$
$$
\langle n,\uparrow|D_n^{(\lambda)}|n+1,\downarrow\rangle
=
\frac23\lambda(1-\lambda)^2(2-\lambda)h^4
+\frac{1}{12}\lambda(1-\lambda)^2(4-\lambda)m^2h^2,
$$
$$
\langle n-1,\uparrow|D_n^{(\lambda)}|n+1,\uparrow\rangle
=
-\frac14\lambda(1-\lambda)^2(2-\lambda)h^4,
$$
together with their reflected partners and spin-flipped partners.

Proof.

Expand the exact kernel ratio
$$
J_n^{(\lambda)}(\Delta)
=
\Gamma\!\bigl(e^{-i\Delta(H_D-\lambda C_n)}\bigr)\Gamma_0(\Delta)^{-1}
$$
to order $\Delta^4$ exactly, subtract $c_\lambda A_n^{(2)}$, and collect coefficients. The resulting difference has exactly eighteen nonzero entries, all confined to the interior shell. The displayed formulas generate that entire list by reflection and spin flip.

$ \square $

**Corollary 1**

(Raw non-leading scaling fails).

For every $0

<

\lambda

<

1$,
$$
A_{n,\lambda}^{(2)}\neq c_\lambda A_n^{(2)}.
$$

Proof.

For $0

<

\lambda

<

1$ the central diagonal correction in Proposition 1 is nonzero, so $D_n^{(\lambda)}\neq0$.

$ \square $

Remark.

This is genuine microscopic nonuniversality. It is already present in the exact one-region coefficient algebra before any continuum limit is discussed, and it includes mass-dependent terms.

## Boundary-shell scaling and exact first strip-moment universality

**Proposition 2**

(Exact boundary-shell scaling).

Every boundary-active entry of the singleton coefficient scales exactly by $c_\lambda$:
$$
\bigl(A_{n,\lambda}^{(2)}\bigr)_{\mathrm{boundary\text{-}active}}
=
c_\lambda\,
\bigl(A_n^{(2)}\bigr)_{\mathrm{boundary\text{-}active}}.
$$
Equivalently,
$$
\bigl(D_n^{(\lambda)}\bigr)_{\mathrm{boundary\text{-}active}}=0.
$$

Proof.

By Proposition 1, the full difference $D_n^{(\lambda)}$ is supported entirely in the interior shell $\{n-1,n,n+1\}$. Hence it has no boundary-active entry.

$ \square $

**Theorem 1**

(Exact $c_\lambda^2$ scaling of the first non-leading singleton exchange coefficient).

Let
$$
C_{n,n+3;\lambda}^{(3)}
:=
[A_{n,\lambda}^{(1)},A_{n+3,\lambda}^{(2)}]+[A_{n,\lambda}^{(2)},A_{n+3,\lambda}^{(1)}].
$$
Then
$$
\boxed{
C_{n,n+3;\lambda}^{(3)}=c_\lambda^2\,C_{n,n+3}^{(3)}.}
$$
Equivalently, using the exact phase-6 decomposition,
$$
C_{n,n+3;\lambda}^{(3)}
=
c_\lambda^2h^6\Bigl(
-\frac{1}{12}F_{n+1/2}
+\frac13 F_{n+3/2}
-\frac{1}{12}F_{n+5/2}
+\frac{5}{12}\bigl(S_{n,n+2}+S_{n+1,n+3}\bigr)
+\frac12 T_{n,n+3}
\Bigr).
$$

Proof.

Write
$$
A_{n,\lambda}^{(2)}=c_\lambda A_n^{(2)}+D_n^{(\lambda)}.
$$
Then
$$
C_{n,n+3;\lambda}^{(3)}
=
c_\lambda^2C_{n,n+3}^{(3)}
+c_\lambda\Bigl([A_n^{(1)},D_{n+3}^{(\lambda)}]+[D_n^{(\lambda)},A_{n+3}^{(1)}]\Bigr).
$$
Now $A_n^{(1)}$ is supported on $\{n-1,n,n+1\}$, while Proposition 1 gives
$$
\operatorname{supp}D_{n+3}^{(\lambda)}\subset\{n+2,n+3,n+4\},
\qquad
\operatorname{supp}D_n^{(\lambda)}\subset\{n-1,n,n+1\},
$$
and $A_{n+3}^{(1)}$ is supported on $\{n+2,n+3,n+4\}$. Thus the mixed products vanish:
$$
A_n^{(1)}D_{n+3}^{(\lambda)}=D_{n+3}^{(\lambda)}A_n^{(1)}=0,
\qquad
D_n^{(\lambda)}A_{n+3}^{(1)}=A_{n+3}^{(1)}D_n^{(\lambda)}=0.
$$
Therefore the extra commutators vanish and only the $c_\lambda^2C_{n,n+3}^{(3)}$ term remains. Inserting the exact phase-6 formula for $C_{n,n+3}^{(3)}$ gives the displayed strip decomposition.

$ \square $

**Corollary 2**

(Exact normalized first strip-moment universality at the first non-leading singleton order).

After dividing by $c_\lambda^2$, the first strip moments of the singleton distance-three coefficient are independent of $\lambda$:
$$
\widehat C_F^{\mathrm{L}}=-\frac14 h^6,\qquad
\widehat C_F^{\mathrm{M}}=h^6,\qquad
\widehat C_F^{\mathrm{R}}=-\frac14 h^6,
$$
$$
\widehat C_S^{\mathrm{L}}=\frac54 h^6,\qquad
\widehat C_S^{\mathrm{R}}=\frac54 h^6,\qquad
\widehat C_T=\frac32 h^6.
$$

Proof.

Theorem 1 multiplies every channel coefficient at separation $r=3$ by the same factor $c_\lambda^2$. Dividing by that factor therefore returns the exact phase-6 strip moments.

$ \square $

Remark.

This is the precise answer to the phase-5 physical question. Regulator differences do survive in the raw one-region non-leading coefficient $A^{(2)}$, but they do

*not*

yet survive in the first normalized strip-moment data extracted from the first separation-controlled singleton exchange coefficient.

## Lie-Trotter as onset-class contrast

**Remark (honest scope of the cross-regulator comparison).**

The Lie-Trotter benchmark does not belong to the same onset class as the collar-excision and admissible $\lambda$-family rules. The exact free-model sequel proved
$$
J_n^{\mathrm{LT}}(\Delta)=I+O(\Delta^4),
\qquad
E_{n,n+3}^{\mathrm{LT}}(\Delta)=I+O(\Delta^8).
$$
So there is no same-order distance-three coefficient in the Lie-Trotter case to compare with $C_{n,n+3}^{(3)}$. At the present phase the honest exact comparison therefore closes inside the common $\Delta^2$-onset family, while Lie-Trotter remains an explicit contrasting regulator with later onset rather than a same-order normalized strip-moment comparator.

## Conclusion

Phase 7 is now complete at the strongest honest singleton scope presently reached. The first explicit non-leading regulator comparison has been carried out exactly. It shows that raw one-region higher coefficients are genuinely regulator-dependent, but that the first separation-controlled singleton strip moments are nevertheless onset-renormalized universal throughout the admissible $\lambda$-family.

That is a stronger answer than the earlier roadmap could provide. It does not collapse everything into universality, and it does not collapse everything into nonuniversality. It separates the two. The exact microscopic transition-law algebra already knows both facts, and phase 7 now states them explicitly.

## References

1. [1] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
2. [2] Anonymous, “Broader Regulator Stability Across Support Prototypes,” preprint (2026).
3. [3] Anonymous, “Explicit Higher Coefficients and First Nontrivial Singleton Strip Moments,” preprint (2026).
4. [4] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
