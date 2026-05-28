# Explicit Higher Coefficients and First Nontrivial Singleton Strip Moments

*Exact boundary-active $A^{(2)}$ data and the first $d=3$ exchange coefficient in relativistic ISP*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 7 in the relativistic ISP sequence; exact singleton $A^{(2)}$ data at the first genuinely new higher-order exchange level

## Abstract

Phase 4 isolated the first genuinely higher-order singleton exchange problem but left its coefficient algebra unresolved: at distance $d=3$ one needs the order-$\Delta^4$ singleton coefficient $A_n^{(2)}$ and the strip moments it induces. This paper closes that first explicit burden exactly for the collar-excision rule in the one-particle lattice-Dirac model.

The main result is local and exact. We compute the full boundary-active block of $A_n^{(2)}$ relevant to the first separation-controlled commutator. Although the interior of $A_n^{(2)}$ already contains mass-dependent terms and is not symmetric, the boundary-facing shell that communicates across a distance-three gap is mass-independent. Combining that block with the exact leading coefficient $A_n^{(1)}$ yields an explicit decomposition of
$$
C_{n,n+3}^{(3)}:=[A_n^{(1)},A_{n+3}^{(2)}]+[A_n^{(2)},A_{n+3}^{(1)}]
$$
into three bond-flip strips, two same-spin two-step strips, and one new three-step spin-flip strip. The corresponding first strip moments are then read off exactly. The point is Barandes-style and algebraic: before claiming a higher-order continuum law, one should first extract the exact strip data from the transition-law coefficients themselves. This paper does that at the first nontrivial higher-order singleton level and no further.

## Introduction

Phase 4 of the present sequence closed the structural higher-order problem at the right exact level. It proved that higher-order exchange coefficients factor through finite overlap windows and that the first genuinely new singleton case occurs at distance $d=3$, where the exchange defect begins with
$$
E_{\{n\},\{n+3\}}(\Delta)
=
I+\Delta^6\Bigl([A_n^{(1)},A_{n+3}^{(2)}]+[A_n^{(2)},A_{n+3}^{(1)}]\Bigr)+O(\Delta^8).
$$
What phase 4 did not do was compute the actual order-$\Delta^4$ coefficient $A_n^{(2)}$ or the strip moments entering that first new commutator.

That omission was unavoidable there, but not here. The present paper performs the first exact non-leading coefficient computation for the explicit free model. From the Barandes point of view, this is the correct next step: not to invent a continuum operator in advance, and not to guess a symmetry that the exact coefficient algebra has not earned, but to compute the concrete local coefficient data and ask what strip channels they actually generate.

**Main results (informal).**

1. *Exact boundary-active singleton $A^{(2)}$ block.* The entries of $A_n^{(2)}$ with one site at the outer shell $n\pm2$ and the other inside the active strip are computed exactly. That block is mass-independent even though the full $A_n^{(2)}$ is not.
2. *Exact first higher-order singleton exchange coefficient.* The distance-three coefficient $C_{n,n+3}^{(3)}$ closes exactly on six strip channels: three bond-flip strips, two same-spin two-step strips, and one new three-step spin-flip strip.
3. *Exact first strip moments.* Because the singleton coefficient functions are supported only at separation $r=3$, the first strip moments entering phase 4 are obtained exactly and explicitly from that strip decomposition.

Scope note. The paper is intentionally narrow. It treats the collar-excision rule, singleton supports, and the first genuinely new visible case $d=3$. It does not claim a full classification of $A_R^{(2)}$ for arbitrary supports, nor a general higher-order continuum theorem beyond the exact strip moments computed here.

## Setup and the exact strip basis

Let $R_n:=\{n\}$ and write the corresponding collar-excision comparison map as
$$
J_n(\Delta)=I+\Delta^2A_n^{(1)}+\Delta^4A_n^{(2)}+O(\Delta^6).
$$
We use the same one-particle lattice-Dirac model and the same exact leading coefficient $A_n^{(1)}$ established in the explicit free-model sequel. Throughout,
$$
h:=\frac{1}{2a}.
$$
For the pair $(R_n,R_{n+3})$, phase 4 gives the first separation-controlled higher-order coefficient
$$
C_{n,n+3}^{(3)}=[A_n^{(1)},A_{n+3}^{(2)}]+[A_n^{(2)},A_{n+3}^{(1)}].
$$

**Definition 1**

(Exact strip basis for the singleton $d=3$ coefficient).

Define the antisymmetric strip operators
$$
F_{n+1/2}
:=
\sum_{s\in\{\uparrow,\downarrow\}}
\Bigl(
|n+1,\bar s\rangle\langle n,s|
-
|n,s\rangle\langle n+1,\bar s|
\Bigr),
$$
$$
S_{n,n+2}
:=
\sum_{s\in\{\uparrow,\downarrow\}}
\Bigl(
|n,s\rangle\langle n+2,s|
-
|n+2,s\rangle\langle n,s|
\Bigr),
$$
and the new three-step spin-flip strip
$$
T_{n,n+3}
:=
\sum_{s\in\{\uparrow,\downarrow\}}
\Bigl(
|n+3,\bar s\rangle\langle n,s|
-
|n,s\rangle\langle n+3,\bar s|
\Bigr).
$$

Remark.

At leading singleton order the exact commutators closed only on the $F$ and $S$ strip families. The operator $T_{n,n+3}$ is the first genuinely new strip channel forced by higher-order coefficient data.

## Exact boundary-active singleton $A^{(2)}$ data

**Proposition 1**

(Exact boundary-active block of the singleton coefficient $A_n^{(2)}$).

For the collar-excision rule and the singleton support $R_n=\{n\}$, the only nonzero entries of $A_n^{(2)}$ with one site in the outer shell $\{n-2,n+2\}$ and the other in the active local strip $\{n-2,n-1,n,n+1,n+2\}$ are
$$
\begin{aligned}
\langle n-2,\uparrow|A_n^{(2)}|n-2,\uparrow\rangle &= -\frac{1}{12}h^4, &
\langle n-2,\uparrow|A_n^{(2)}|n-1,\downarrow\rangle &= \frac13 h^4, \\
\langle n-1,\uparrow|A_n^{(2)}|n-2,\downarrow\rangle &= -\frac23 h^4, &
\langle n,\uparrow|A_n^{(2)}|n-2,\uparrow\rangle &= \frac34 h^4, \\
\langle n-2,\uparrow|A_n^{(2)}|n,\uparrow\rangle &= -\frac14 h^4,
\end{aligned}
$$
$$
\begin{aligned}
\langle n+2,\uparrow|A_n^{(2)}|n+2,\uparrow\rangle &= -\frac{1}{12}h^4, &
\langle n+2,\uparrow|A_n^{(2)}|n+1,\downarrow\rangle &= \frac13 h^4, \\
\langle n+1,\uparrow|A_n^{(2)}|n+2,\downarrow\rangle &= -\frac23 h^4, &
\langle n,\uparrow|A_n^{(2)}|n+2,\uparrow\rangle &= \frac34 h^4, \\
\langle n+2,\uparrow|A_n^{(2)}|n,\uparrow\rangle &= -\frac14 h^4,
\end{aligned}
$$
together with the identical spin-flipped partners obtained by $\uparrow\leftrightarrow\downarrow$.

Proof.

Write the kernel expansions
$$
\Gamma(e^{-i\Delta B_n})=I+\Delta^2L_n+\Delta^4M_n+O(\Delta^6),
\qquad
\Gamma_0(\Delta)=I+\Delta^2L_0+\Delta^4M_0+O(\Delta^6).
$$
Then
$$
A_n^{(1)}=L_n-L_0,
\qquad
A_n^{(2)}=M_n-M_0-A_n^{(1)}L_0.
$$
The quasilocal filtration already proved in the exact free-model sequel gives $\operatorname{supp}A_n^{(2)}\subset\{n-2,\dots,n+2\}$, so only finitely many matrix elements can appear. Exact evaluation of the twenty boundary-active matrix elements displayed above gives precisely those coefficients, and no others occur.

$ \square $

Remark.

The entire boundary-active block is mass-independent. This is not true of the full coefficient $A_n^{(2)}$, only of the outer shell that can communicate across a distance-three gap.

**Remark (the full $A_n^{(2)}$ is not symmetric).**

One should not impose a transpose symmetry that the exact coefficient algebra has not earned. For example,
$$
\langle n,\uparrow|A_n^{(2)}|n+2,\uparrow\rangle=\frac34 h^4,
\qquad
\langle n+2,\uparrow|A_n^{(2)}|n,\uparrow\rangle=-\frac14 h^4,
$$
so $A_n^{(2)}\neq (A_n^{(2)})^\top$ already in the singleton case.

**Remark (interior mass dependence).**

The mass independence of Proposition 1 is an outer-shell fact, not a full-coefficient fact. For example,
$$
\langle n,\uparrow|A_n^{(2)}|n,\uparrow\rangle=\frac92 h^4-\frac23 m^2h^2,
\qquad
\langle n,\uparrow|A_n^{(2)}|n+1,\downarrow\rangle=-3h^4+\frac13 m^2h^2.
$$
Thus mass information really does enter at order $\Delta^4$; it simply drops out of the first distance-three communication channel.

## Exact first nontrivial higher-order singleton exchange coefficient

**Theorem 1**

(Exact strip decomposition of the first nontrivial singleton coefficient).

For singleton supports $R_n=\{n\}$ and $R_{n+3}=\{n+3\}$,
$$
C_{n,n+3}^{(3)}
:=
[A_n^{(1)},A_{n+3}^{(2)}]+[A_n^{(2)},A_{n+3}^{(1)}]
$$
is exactly
$$
\boxed{
C_{n,n+3}^{(3)}
=
h^6\Bigl(
-\frac{1}{12}F_{n+1/2}
+\frac13 F_{n+3/2}
-\frac{1}{12}F_{n+5/2}
+\frac{5}{12}\bigl(S_{n,n+2}+S_{n+1,n+3}\bigr)
+\frac12 T_{n,n+3}
\Bigr).}
$$

Proof.

Phase 4 already reduces the distance-three coefficient to the two commutators displayed above. For this separation, the overlap windows are the single sites $n+1$ and $n+2$, so only the boundary-active shell of Proposition 1 can contribute. Insert those exact $A^{(2)}$ entries together with the exact leading singleton coefficient $A_n^{(1)}$ from the explicit free-model sequel. Direct multiplication yields twenty-four nonzero matrix entries. Grouping those entries into the antisymmetric strip basis of Definition 1 gives exactly the displayed combination and no further channel.

$ \square $

**Corollary 1**

(Exact first strip moments for the singleton $d=3$ coefficient).

In the notation of phase 4, the singleton channel coefficients are supported only at support displacement $r=3$ and are
$$
c_F^{\mathrm{L}}(3)=-\frac{1}{12}h^6,\qquad
c_F^{\mathrm{M}}(3)=\frac13 h^6,\qquad
c_F^{\mathrm{R}}(3)=-\frac{1}{12}h^6,
$$
$$
c_S^{\mathrm{L}}(3)=\frac{5}{12}h^6,\qquad
c_S^{\mathrm{R}}(3)=\frac{5}{12}h^6,\qquad
c_T(3)=\frac12 h^6.
$$
Hence the corresponding first strip moments are
$$
C_F^{\mathrm{L}}=-\frac14 h^6,\qquad
C_F^{\mathrm{M}}=h^6,\qquad
C_F^{\mathrm{R}}=-\frac14 h^6,
$$
$$
C_S^{\mathrm{L}}=\frac54 h^6,\qquad
C_S^{\mathrm{R}}=\frac54 h^6,\qquad
C_T=\frac32 h^6.
$$

Proof.

Theorem 1 shows that the coefficient functions are supported only at the singleton separation $r=3$. The first strip moment is therefore just $r$ times the channel coefficient: $C=3c(3)$. Applying that identity channel by channel gives the displayed values.

$ \square $

Remark.

The first separation-controlled higher-order singleton exchange coefficient is mass-independent even though the full $A_n^{(2)}$ is not. The exact reason is now visible: only the outer shell of $A_n^{(2)}$ can feed the distance-three commutator, and that shell has no $m$-dependence.

## Barandes-style reading of what phase 6 closes

The main conceptual lesson is not that one has found a new continuum operator by guesswork. It is that the exact transition-law coefficient algebra has now been pushed one real step beyond the leading singleton sector. The higher-order strip basis was not assumed; it was extracted. The first strip moments were not postulated; they were computed. And the lack of symmetry of $A_n^{(2)}$ was not repaired by aesthetics; it was left exactly as the local algebra gives it.

At this phase the honest claim is therefore precise and limited:

1. the exact boundary-active singleton coefficient $A_n^{(2)}$ is now known;
2. the first nontrivial higher-order singleton exchange coefficient $C_{n,n+3}^{(3)}$ is now known;
3. the first strip moments entering the phase-4 strip-moment criterion are now known in that singleton class.

What is still outside the present claim is equally important. We do not yet classify all higher-order channels for larger support prototypes, and we do not yet claim a full higher-order continuum law beyond the exact strip moments computed here. Those are later burdens. The present paper closes only the first explicit one.

## Conclusion

Phase 6 is now complete at the strongest honest scope presently reached: the first nontrivial singleton higher-order coefficient has been computed exactly, its strip decomposition has been identified exactly, and its first strip moments have been extracted exactly. This is the first point in the relativistic ISP stack where a genuinely new higher-order coefficient algebra has been turned into explicit finite strip data rather than left as a structural theorem.

That exact local computation immediately sets up the next question. Once the relevant singleton $A^{(2)}$ block is known, one can ask which parts of it are regulator artifacts and which survive in the normalized strip moments. The next paper answers exactly that question at the same non-leading singleton order.

## References

1. [1] Anonymous, “Toward Lorentz-Covariant Indivisible Stochastic Processes: Spatial Locality, Temporal Indivisibility, and Localized Finite Deformations,” preprint (2026).
2. [2] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
3. [3] Anonymous, “Exact Localized Finite Deformations and the Free Dirac Exchange-Defect Theorem,” preprint (2026).
4. [4] Anonymous, “Higher Coefficients and Strip-Moment Closure in the Bond-Centered Thin-Slab Law,” preprint (2026).
5. [5] Anonymous, “Broader Regulator Stability Across Support Prototypes,” preprint (2026).
6. [6] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
