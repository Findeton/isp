# Restricted Renormalized Universality of the Leading Bond-Centered Thin-Slab Law

*Exact regulator comparison, the $\lambda$-family realization, and the theorem-level completion of phase 3 in relativistic ISP*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 4 in the relativistic ISP sequence; exact phase-3 completion at leading visible order

## Abstract

The explicit free-model sequel already established the two facts any honest universality paper must respect. First, raw rule uniqueness fails: the present local-intervention axioms admit continuous families of admissible localized deformation rules with distinct leading comparison coefficients. Second, the naive site-centered continuum limit fails: the stable continuum object is the bond-centered action of the exchange algebra on smooth sampled profiles. The right universality question is therefore not whether all admissible microscopic regulators coincide. It is whether, after the correct onset renormalization, the same leading bond-centered tangential operator survives.

That is the exact scope of the present paper. We isolate the leading-order regulator comparison already justified by the existing free-model stack. The Lie–Trotter and collar-excision constructions are treated as distinct regularizations of the same localized finite-deformation problem; the exact $\lambda$-family provides a nontrivial admissible class with explicit scaling; and the bond-centered collar-excision thin-slab theorem supplies the common tangential operator. We then prove the strongest theorem-level universality statement presently supported: restricted onset-renormalized universality at the first visible exchange order, together with an exact realization of that universality for the $\lambda$-family on smooth sampled profiles.

This closes phase 3 at the strongest exact scope now available. It does not prove microscopic rule uniqueness, and it does not prove broader support-prototype stability beyond the leading order realized by the exact family. Those are later proof burdens. What phase 3 now completes is narrower and firmer: the theorem-level leading-order universality statement compatible with the existing exact results, together with its geometric reading in the supported-hypersurface architecture of relativistic ISP.

Scope note. This file retains its earlier path for continuity, but its theorem-level scope is now limited to leading-order restricted universality. The admissible regulators used here are mathematically admissible localized-deformation rules inside the stated finite model; physical rule selection would require additional operational or dynamical criteria. Broader prototype-level regulator stability is deferred explicitly to a later phase.

## Introduction

Phase 3 should never have been a rule-selection phase. The explicit free-model sequel already proved that the present local-intervention axioms do not determine a unique localized deformation rule. It also proved that the most naive site-centered thin-slab limit of the leading singleton coefficient diverges. So the correct universality target has to be weaker than microscopic uniqueness and stronger than a vague continuum slogan.

The correct target is onset-renormalized universality of the leading bond-centered exchange law. One asks whether different admissible regulators, once divided by their first visible onset factor, generate the same leading tangential operator on smooth sampled profiles. That is exactly the kind of statement one can defend from the current stack without inventing unsupported higher-order results or smuggling in extra amplitude-level structure. It is also the formulation most faithful to the Barandes viewpoint: start from the exact probabilistic transition-law data and ask what structural content survives there.

This paper therefore does three things. First, it reformulates the exact regulator facts already proved in the free-model sequel. Second, it states and proves the restricted onset-renormalized universality theorem at the leading visible order. Third, it shows that the exact $\lambda$-family realizes that theorem and shares the same bond-centered tangential operator after normalization. That is the theorem-level completion of phase 3.

## Exact regulator facts from the free-model sequel

**Definition 1**

(Leading-order regulator family).

A leading-order regulator family for localized finite deformations is a collection of exact primitive kernels and comparison maps satisfying
$$
J_R^{(\alpha)}(\Delta)=I+c_\alpha\Delta^{2\kappa_\alpha}\,\mathcal K_R^{(\alpha)}+O(\Delta^{2\kappa_\alpha+2}),
$$
for some $c_\alpha>0$ and integer onset exponent $\kappa_\alpha\ge 1$, together with the corresponding inverse expansion and the same quasilocal support notion used throughout the free-model papers.

**Proposition 1**

(Exact leading-order regulator facts).

The present free-model stack yields the following exact facts.

1. *Lie–Trotter onset.* The bulk-then-collar Lie–Trotter rule begins at order $\Delta^4$, so $\kappa_{\mathrm{LT}}=2$.
2. *Collar-excision onset.* The collar-excision rule begins at order $\Delta^2$, so $\kappa_{\mathrm{exc}}=1$.
3. *Exact $\lambda$-family scaling.* For every finite interval support $R$ and every $0 < \lambda\le 1$,
  $$
  A_{R,\lambda}^{(1)}=\lambda(2-\lambda)A_R^{(1)}.
  $$
4. *Exact bond-centered leading operator.* The leading collar-excision singleton exchange bracket reduces, after bond-centered spatial renormalization, to
  $$
  K_\parallel[\beta]=\Bigl(\beta\partial_x+\frac12\partial_x\beta\Bigr)(I-\alpha)
  $$
  on smooth sampled profiles.

**Source of the statement.**

Items (1), (2), and (4) are proved in the explicit free-model sequel, and item (3) is its exact $\lambda$-family scaling theorem. The present paper uses them as exact input.

$\square$

Remark.

These facts already rule out two tempting but incorrect universality notions: raw microscopic uniqueness and raw entrywise matrix universality. Different admissible regulators do not even begin at the same visible order, and the stable continuum object is bond-centered rather than site-centered.

## Restricted onset-renormalized universality

**Theorem 1**

(Restricted onset-renormalized universality at the leading visible order).

Let $\alpha$ label a class of admissible leading-order regulators such that, for every bounded interval support $R$,
$$
J_R^{(\alpha)}(\Delta)=I+c_\alpha\Delta^{2\kappa_\alpha}\,\mathcal K_R+O(\Delta^{2\kappa_\alpha+2}),
$$
with the same normalized leading operator $\mathcal K_R$ across the class. Assume moreover that for the support pair under consideration:

1. the corresponding inverse expansions hold;
2. the first nonzero exchange contribution is generated by the commutator of the normalized leading terms; and
3. the bond-centered continuum action of $[\mathcal K_R,\mathcal K_S]$ on smooth sampled profiles exists.

Then the renormalized exchange defect
$$
\widehat E_{R,S}^{(\alpha)}(\Delta)
:=
\frac{E_{R,S}^{(\alpha)}(\Delta)-I}{c_\alpha^2\Delta^{4\kappa_\alpha}}
$$
satisfies
$$
\widehat E_{R,S}^{(\alpha)}(\Delta)
=
[\mathcal K_R,\mathcal K_S]+O(\Delta^2),
$$
and every regulator in the class therefore shares the same leading tangential continuum bracket.

Proof.

Insert the normalized leading expansions of $J_R^{(\alpha)}$ and $J_S^{(\alpha)}$ into the group-commutator definition of the exchange defect. The first nonzero term is the commutator of the normalized leading operators, multiplied by $c_\alpha^2\Delta^{4\kappa_\alpha}$. Dividing by that factor removes the regulator-dependent onset data and leaves the common commutator. Assumption (3) identifies its bond-centered continuum action.

$\square$

Remark.

This is the strongest universality theorem compatible with the present exact results. It is intentionally weaker than rule selection and intentionally stronger than a generic continuum slogan. The universal object is the normalized leading bond-centered exchange bracket.

## Exact realization by the $\lambda$-family

**Corollary 1**

(Exact finite-lattice universality test for the $\lambda$-family).

Let $R,S$ be any support pair whose first visible exchange order is generated by the leading coefficients. With
$$
c_\lambda:=\lambda(2-\lambda),
$$
one has
$$
E_{R,S}^{(\lambda)}(\Delta)
=
I+c_\lambda^2\Delta^4[A_R^{(1)},A_S^{(1)}]+O(\Delta^6),
$$
and therefore
$$
\frac{E_{R,S}^{(\lambda)}(\Delta)-I}{c_\lambda^2\Delta^4}
=
[A_R^{(1)},A_S^{(1)}]+O(\Delta^2).
$$
Thus the exact $\lambda$-family realizes restricted onset-renormalized universality at the first visible exchange order.

Proof.

The exact scaling identity
$$
A_{R,\lambda}^{(1)}=c_\lambda A_R^{(1)}
$$
implies
$$
[A_{R,\lambda}^{(1)},A_{S,\lambda}^{(1)}]=c_\lambda^2[A_R^{(1)},A_S^{(1)}].
$$
By hypothesis, the first visible exchange term is generated by these leading coefficients, so the displayed defect expansion follows. Dividing by $c_\lambda^2\Delta^4$ yields the normalized statement.

$\square$

Remark.

This corollary is exact and finite-lattice. It does not yet use the continuum operator. It shows that the exact admissible family singled out by the no-go lemma already exhibits a nontrivial renormalized universality mechanism at the first visible order.

## Exact bond-centered universality of the leading tangential operator

**Definition 2**

(Leading smeared singleton operators for the $\lambda$-family).

For the singleton-support leading coefficients, define
$$
\mathcal K_{a,\lambda}[N]:=a\sum_n N_nA_{n,\lambda}^{(1)},
\qquad
\mathcal K_a[N]:=a\sum_n N_nA_n.
$$
Write
$$
\beta:=N\partial_xM-M\partial_xN,
$$
and let $\iota_a\phi$ denote the lattice sampling of a smooth compactly supported two-component profile $\phi$.

**Theorem 2**

(Exact leading-order bond-centered universality for the $\lambda$-family).

For every $0

<

\lambda\le 1$ one has
$$
\mathcal K_{a,\lambda}[N]=c_\lambda\mathcal K_a[N].
$$
Consequently, for every smooth compactly supported two-component profile $\phi$,
$$
\frac{1}{c_\lambda^2}
[\mathcal K_{a,\lambda}[N],\mathcal K_{a,\lambda}[M]]\iota_a\phi
=
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a).
$$
Thus the entire exact admissible $\lambda$-family shares the same leading bond-centered tangential operator after onset renormalization.

Proof.

For singleton supports, the exact scaling theorem gives
$$
A_{n,\lambda}^{(1)}=c_\lambda A_n.
$$
Hence
$$
\mathcal K_{a,\lambda}[N]=a\sum_nN_nA_{n,\lambda}^{(1)}=c_\lambda a\sum_nN_nA_n=c_\lambda\mathcal K_a[N].
$$
Therefore
$$
\frac{1}{c_\lambda^2}[\mathcal K_{a,\lambda}[N],\mathcal K_{a,\lambda}[M]]
=[\mathcal K_a[N],\mathcal K_a[M]].
$$
Apply the exact bond-centered collar-excision thin-slab theorem, which identifies the right-hand side with
$$
\iota_a\bigl(K_\parallel[\beta]\phi\bigr)+O(a)
$$
on smooth sampled profiles.

$\square$

Remark.

This theorem closes phase 3 at the strongest exact scope now available. It does not prove that every conceivable regulator family shares the same limit. It proves that the exact nontrivial family already realized inside the free-model sequel does share the same leading bond-centered tangential operator after onset normalization.

## Geometric reading in the supported-hypersurface architecture

The architecture paper argued that relativistic ISP should be organized around exact finite hypersurface kernels and localized supported deformations, with the exchange defect playing the role of the finite Dirac–Schwinger datum. Theorem 2 gives the precise leading-order operator that survives this program in the explicit free-model realization.

At leading visible order, the renormalized operator depends only on the antisymmetrized deformation profile $\beta$ and the bond-centered exchange density singled out by the exact local algebra. In that sense it is the leading tangential exchange datum attached to a pair of supported finite hypersurface deformations whose first visible order is generated by the leading coefficients. No additional wave-function ontology is needed to read that statement: it is already encoded in the exact transition-law algebra itself.

Remark.

The geometric reading is intentionally leading-order and intentionally exact only at that scope. Broader support-prototype stability, higher-coefficient geometric closure, and all ontology-expanding phases belong later in the program.

## What phase 3 now closes and what it defers

With the scope fixed this way, phase 3 is complete in the following exact sense.

1. *Restricted universality theorem.* The strongest universality statement compatible with the present explicit free-model results has been isolated and proved.
2. *Exact family realization.* The nontrivial admissible $\lambda$-family realizes that theorem at the first visible exchange order.
3. *Exact common tangential limit.* After onset normalization, the exact $\lambda$-family shares the same leading bond-centered tangential operator on smooth sampled profiles.
4. *Geometric placement.* The leading operator has been placed explicitly within the supported-hypersurface architecture of relativistic ISP.

Just as important is what is deliberately deferred.

1. *Microscopic rule uniqueness.* It is not available and is not claimed.
2. *Broader prototype-level regulator stability.* This requires exact higher-coefficient strip moments beyond the present scope.
3. *Higher-order universality.* No claim is made beyond the first visible order already realized by the exact family.
4. *Fock, gauge, and detector phases.* These remain later, strictly dependent phases.

**Strategic remark.**

Narrowing the phase this way is what makes it theorem-level. The broader universality questions are real, but they must sit downstream of exact higher-coefficient calculations rather than inside a prematurely broadened phase-3 paper.

## Conclusion

Phase 3 is now complete at the strongest exact scope supported by the existing relativistic ISP stack. The right universality statement is onset-renormalized, bond-centered, and leading-order. It is realized exactly by the nontrivial $\lambda$-family, and it yields the same leading tangential operator after normalization.

This is also the right conclusion from the Barandes point of view. The exact probabilistic transition-law algebra is primary. One does not repair regulator dependence by imposing extra representational structure that the transition law itself has not earned. Instead one identifies the structural content that survives there. At leading order, that content is now exact. The next real proof burden is not more rhetoric about universality, but exact higher-coefficient strip-moment control beyond the leading visible order.

## References

1. [1] Anonymous, “Toward Lorentz-Covariant Indivisible Stochastic Processes: Spatial Locality, Temporal Indivisibility, and Localized Finite Deformations,” preprint (2026).
2. [2] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
3. [3] Anonymous, “Exact Localized Finite Deformations and the Free Dirac Exchange-Defect Theorem,” preprint (2026).
4. [4] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
5. [5] J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085 (2023; rev. 2026).
6. [6] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192 (2025).
