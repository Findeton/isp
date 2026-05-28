# Higher Coefficients and Strip-Moment Closure in the Bond-Centered Thin-Slab Law

*Exact higher-order overlap structure and the strip-moment criterion in relativistic ISP*

Author: Felix Robles Elvira

Draft preprint

Date: March 2026

Paper 5 in the relativistic ISP sequence; exact higher-order structure plus conditional strip-moment closure

## Abstract

The exact free one-particle exchange-defect package already proves more about the higher-order problem than the older bridge draft made explicit. The comparison maps admit a quasilocal filtration
$$
J_R(\Delta)=I+\sum_{k\ge 1}\Delta^{2k}A_R^{(k)},
$$
with $\supp A_R^{(k)}\subset\mathcal N_k(R)$, and the first visible defect coefficient for disjoint supports is
$$
C_{R,S}^{(\mu_1)}=\sum_{p+q=\mu_1}[A_R^{(p)},A_S^{(q)}].
$$
This paper isolates the exact higher-order content of those facts instead of leaving it scattered across roadmap prose.

First, we prove an exact overlap-factorization statement: every product $A_R^{(p)}A_S^{(q)}$ factors through the finite overlap window $\mathcal N_p(R)\cap\mathcal N_q(S)$. Consequently, the first higher-order exchange coefficient is already an overlap-window datum of the exact kernel algebra itself. Second, we formulate, but do not prove in full generality, the correct higher-order continuum criterion. Under an explicit strip-closure hypothesis with finite first moments, the smeared higher-order exchange commutator again reduces to a bond-centered first-order tangential operator on smooth sampled profiles. The point is Barandes-style and structural: the continuum object is not an entrywise matrix limit but the bond-centered action of the exact transition-law algebra on smooth data.

## Introduction

Phase 2 closed the exact leading support-level boundary law, and phase 3 closed the strongest exact leading-order universality statement currently justified. But neither result exhausted the higher-order problem. The exact free one-particle paper already established the quasilocal filtration for *all* higher coefficients and the exact defect-order formula for *all* disjoint finite interval pairs. What it did not do was spell out what those exact facts already imply for the structure of the higher-order exchange algebra.

That structural step matters. From the Barandes point of view, one should not begin by asking for a Hilbert-space representation-theoretic story or an entrywise continuum matrix limit. One should begin from the exact transition-law data and ask what the exchange algebra itself forces. At higher order, the right first question is therefore not yet “what is $A_R^{(2)}$ explicitly?” but “through what exact local overlap data can a coefficient pair $A_R^{(p)}$, $A_S^{(q)}$ communicate at all?” Once that question is answered, the right continuum criterion can be stated cleanly.

**Main results (informal).**

1. *Exact overlap-factorization.* Every higher-order coefficient product $A_R^{(p)}A_S^{(q)}$ factors through the finite overlap window $\mathcal N_p(R)\cap\mathcal N_q(S)$, so the first visible higher-order exchange coefficient is already an exact overlap-window datum.
2. *Exact first higher-order package.* The first visible higher-order coefficient is the sum of those overlap-window contributions with $p+q=\mu_1(R,S)$; the first genuinely new case is $\mu_1=3$, where $A^{(2)}$ enters for the first time.
3. *Conditional strip-moment reduction.* If the exact higher-order commutators close on finitely many bond-centered strip channels with finite first moments, then the smeared commutator again has a bond-centered first-order tangential continuum action on smooth sampled profiles.

Scope note. This paper isolates exact higher-order exchange structure and states the strip-moment closure theorem in conditional form. It does not yet compute general formulas for $A_R^{(2)}$ or classify all higher-order strip channels explicitly.

## Exact higher-order overlap structure

**Definition 1**

(Higher-order overlap windows and onset index).

For disjoint finite intervals $R,S\subset\Lambda_L$ and integers $p,q\ge 1$, define
$$
\Omega_{R,S}^{(p,q)}:=\mathcal N_p(R)\cap\mathcal N_q(S),
$$
and let $P_{R,S}^{(p,q)}$ denote the projector onto configurations whose site labels lie in $\Omega_{R,S}^{(p,q)}$. Define the exact onset index
$$
\kappa(R,S):=\mu_1(R,S):=\min\bigl\{p+q:\ p,q\ge 1,\ \Omega_{R,S}^{(p,q)}\neq\varnothing\bigr\}.
$$
For a nonwrapping pair
$$
R=[r_-,r_+],\qquad S=[s_-,s_+],\qquad r_+<s_-,
$$
one has
$$
\Omega_{R,S}^{(p,q)}=[\,s_--q,\ r_++p\,].
$$

**Proposition 1**

(Exact overlap-factorization of coefficient products).

For disjoint finite intervals $R,S$ and integers $p,q\ge 1$,
$$
A_R^{(p)}A_S^{(q)}=A_R^{(p)}P_{R,S}^{(p,q)}A_S^{(q)},
\qquad
A_S^{(q)}A_R^{(p)}=A_S^{(q)}P_{R,S}^{(p,q)}A_R^{(p)}.
$$
In particular, if $\Omega_{R,S}^{(p,q)}=\varnothing$, then
$$
[A_R^{(p)},A_S^{(q)}]=0.
$$

Proof.

By the exact quasilocal filtration,
$$
\supp A_R^{(p)}\subset\mathcal N_p(R),
\qquad
\supp A_S^{(q)}\subset\mathcal N_q(S).
$$
For a matrix entry of the product,
$$
[A_R^{(p)}A_S^{(q)}]_{AB}
=
\sum_C [A_R^{(p)}]_{AC}[A_S^{(q)}]_{CB},
$$
the intermediate configuration $C$ can contribute only if its site label lies simultaneously in $\mathcal N_p(R)$ and in $\mathcal N_q(S)$, hence in $\Omega_{R,S}^{(p,q)}$. Inserting the projector $P_{R,S}^{(p,q)}$ therefore does not change the sum. The same argument gives the second identity. If $\Omega_{R,S}^{(p,q)}$ is empty, then both products vanish.

$ \square $

Remark.

This is the exact higher-order analog of the leading boundary-packet lesson. Exchange does not arise because two support volumes are both “large.” It arises because the exact localized coefficient algebra acquires a nonempty overlap window through which one coefficient can feed the other.

**Theorem 1**

(Exact first higher-order exchange package).

Let $R,S$ be disjoint finite intervals and let $\kappa:=\mu_1(R,S)$. Then
$$
E_{R,S}(\Delta)=I+\Delta^{2\kappa}C_{R,S}^{(\kappa)}+O(\Delta^{2\kappa+2}),
$$
with
$$
C_{R,S}^{(\kappa)}
=
\sum_{p+q=\kappa}[A_R^{(p)},A_S^{(q)}]
=
\sum_{p+q=\kappa}
\Bigl(
A_R^{(p)}P_{R,S}^{(p,q)}A_S^{(q)}

-A_S^{(q)}P_{R,S}^{(p,q)}A_R^{(p)}
\Bigr).
$$
If $\kappa\ge 3$, then every summand contains at least one coefficient of order $\ge 2$.

Proof.

The exact defect-order formula from the free one-particle exchange-defect paper gives
$$
C_{R,S}^{(\kappa)}=\sum_{p+q=\kappa}[A_R^{(p)},A_S^{(q)}].
$$
Apply Proposition 1 term by term to each commutator in that sum. If $\kappa\ge 3$, the constraints $p,q\ge 1$ force at least one of $p,q$ to be $\ge 2$.

$ \square $

**Corollary 1**

(First genuinely higher-order visible case).

If $\mu_1(R,S)=3$, then
$$
C_{R,S}^{(3)}=[A_R^{(1)},A_S^{(2)}]+[A_R^{(2)},A_S^{(1)}],
$$
and equivalently
$$
C_{R,S}^{(3)}
=
A_R^{(1)}P_{R,S}^{(1,2)}A_S^{(2)}
-A_S^{(2)}P_{R,S}^{(1,2)}A_R^{(1)}
+A_R^{(2)}P_{R,S}^{(2,1)}A_S^{(1)}
-A_S^{(1)}P_{R,S}^{(2,1)}A_R^{(2)}.
$$

Proof.

When $\mu_1(R,S)=3$, the only admissible pairs with $p,q\ge 1$ and $p+q=3$ are $(1,2)$ and $(2,1)$. Insert them into Theorem 1.

$ \square $

Remark.

This is the first point at which genuinely new coefficient data are unavoidable. Because $A_R^{(1)}$ is already known to be mass-blind while higher coefficients need not be, $\mu_1=3$ is also the first visible order at which mass-dependent exchange structure can enter.

## Support prototypes and strip-moment closure

The exact overlap package says where higher-order exchange lives. The next question is when that exact exchange algebra has a stable bond-centered continuum action. The right criterion is not an entrywise matrix limit. It is closure on finitely many strip channels with finite first moments.

**Definition 2**

(Translated coefficient families).

Let $\sigma$ label a support type, for example a singleton, an interval of fixed width, or a finite union of local cells. For each order $p\ge 1$, let $A_{\sigma,n}^{(p)}$ denote the order-$\Delta^{2p}$ coefficient attached to the translate of type $\sigma$ centered at lattice site $n$. Define the smeared operator
$$
\mathcal K_{\sigma,a}^{(p)}[N]
:=
a\sum_n N_nA_{\sigma,n}^{(p)}.
$$

**Definition 3**

(Bond-centered admissible strip channels).

Suppose that for each active channel label $(\ell,\chi)$ there is a translated antisymmetric strip-operator family $X_{n+1/2}^{(\ell,\chi)}$ and a corresponding smeared bond-centered density $\mathcal T_a^{(\ell,\chi)}[\beta]$ such that, for every smooth compactly supported two-component profile $\phi$,
$$
\mathcal T_a^{(\ell,\chi)}[\beta]\iota_a\phi
=
\iota_a\bigl(K_{\ell,\chi}[\beta]\phi\bigr)+O(a),
$$
where $K_{\ell,\chi}[\beta]$ is first-order in derivatives and local in $\beta$. Call such a family

*bond-centered admissible*

.

**Hypothesis 1**

(Exact strip closure with finite first moments).

Fix support types $\sigma,\tau$ and orders $p,q$. Assume:

1. *strip closure:* $$
  [A_{\sigma,n}^{(p)},A_{\tau,m}^{(q)}]
  =
  \sum_{(\ell,\chi)}
  c_{\sigma,\tau}^{(p,q;\ell,\chi)}(m-n)\,
  X_{n+1/2}^{(\ell,\chi)},
  $$
  for finitely many strip channels $(\ell,\chi)$ and finitely supported coefficient functions $c_{\sigma,\tau}^{(p,q;\ell,\chi)}$;
2. *antisymmetry:* $c_{\sigma,\tau}^{(p,q;\ell,\chi)}(r)=-c_{\tau,\sigma}^{(q,p;\ell,\chi)}(-r)$;
3. *finite first moments:* $$
  C_{\sigma,\tau}^{(p,q;\ell,\chi)}
  :=
  \sum_r r\,c_{\sigma,\tau}^{(p,q;\ell,\chi)}(r)
  $$
  exist for all active channels.

**Conditional Theorem 2**

(Higher-order bond-centered thin-slab reduction under strip closure).

Assume Hypothesis 1, and assume moreover that each active strip channel is bond-centered admissible in the sense of Definition 3. Then for every smooth compactly supported two-component profile $\phi$ one has
$$
[\mathcal K_{\sigma,a}^{(p)}[N],\mathcal K_{\tau,a}^{(q)}[M]]\,\iota_a\phi
=
\sum_{(\ell,\chi)}
C_{\sigma,\tau}^{(p,q;\ell,\chi)}
\mathcal T_a^{(\ell,\chi)}[\beta]\iota_a\phi
+O(a),
$$
with
$$
\beta=N\partial_xM-M\partial_xN.
$$
Consequently,
$$
[\mathcal K_{\sigma,a}^{(p)}[N],\mathcal K_{\tau,a}^{(q)}[M]]\,\iota_a\phi
=
\iota_a\bigl(K_{\parallel;\sigma,\tau}^{(p,q)}[\beta]\phi\bigr)+O(a),
$$
where
$$
K_{\parallel;\sigma,\tau}^{(p,q)}[\beta]
:=
\sum_{(\ell,\chi)}
C_{\sigma,\tau}^{(p,q;\ell,\chi)}
K_{\ell,\chi}[\beta].
$$
Thus every coefficient pair with strip closure and finite first moments has the same bond-centered continuum form: an antisymmetrized first-order tangential operator controlled by strip moments.

Proof.

Start from
$$
[\mathcal K_{\sigma,a}^{(p)}[N],\mathcal K_{\tau,a}^{(q)}[M]]
=
a^2\sum_{n,m}N_nM_m[A_{\sigma,n}^{(p)},A_{\tau,m}^{(q)}].
$$
Insert the strip-closure expansion from Hypothesis 1 and set $r=m-n$:
$$
=
a^2\sum_{n,r}
N_nM_{n+r}
\sum_{(\ell,\chi)}
c_{\sigma,\tau}^{(p,q;\ell,\chi)}(r)\,X_{n+1/2}^{(\ell,\chi)}.
$$
Antisymmetrizing under $(n,\sigma,p)\leftrightarrow(n+r,\tau,q)$ replaces $N_nM_{n+r}$ by
$N_nM_{n+r}-N_{n+r}M_n$.
Smoothness gives
$$
N_nM_{n+r}-N_{n+r}M_n
=
ar\,\beta(x_{n+r/2})+O(a^2),
$$
uniformly on the finite set of active displacements. Summing over $r$ therefore produces the first moments $C_{\sigma,\tau}^{(p,q;\ell,\chi)}$ multiplying the bond-centered admissible strip densities. The assumed profile-action limit of each strip density then yields the continuum operator.

$ \square $

**Corollary 2**

(The leading support-order theorem is the first strip-closure case).

The phase-2 nearby-support boundary law and the phase-3 leading-order universality benchmark are the special $p=q=1$ instances of Conditional Theorem 2. The first genuinely new higher-order visible case is $\mu_1=3$, where the relevant strip moments come from the $(p,q)=(1,2)$ and $(2,1)$ channel families isolated in Corollary 1.

Remark.

Conditional Theorem 2 is deliberately formulated at the coefficient-algebra level rather than the kernel-entry level. That is exactly the lesson of the explicit free-model sequel: the wrong continuum object is the raw entrywise matrix coefficient, while the right continuum object is the bond-centered action of the exchange algebra on smooth sampled profiles.

## Barandes-style reading of the higher-order problem

The higher-order problem is often described as if its main burden were combinatorial bookkeeping. That is too shallow. The real issue is conceptual. The exact transition law already knows the localized support growth, the exact onset order, and the overlap windows through which higher-order exchange can first occur. What it does *not* yet know is whether the resulting overlap-window algebra closes on a finite family of strip channels with stable first moments.

So the next proof burden is not to impose an external continuum representation and hope the algebra follows. It is to derive the strip channels and their first moments from the exact kernel algebra itself. Only then has the transition law earned a higher-order continuum operator. That is the Barandes perspective carried one level beyond the leading singleton sector.

Remark.

The exact overlap-factorization theorem is already useful even before explicit $A_R^{(2)}$ formulas are known. It tells us where to look: one does not need the entire support volume or a global matrix limit. One needs the active overlap windows and the strip moments of the channel coefficients that survive antisymmetrization.

## What phase 4 now closes and what it defers

With the scope fixed this way, phase 4 is complete in the following exact sense.

1. *Exact higher-order overlap windows.* The higher-order coefficient products are shown to factor exactly through finite overlap windows determined by the quasilocal filtration.
2. *Exact first higher-order exchange package.* The first visible higher-order exchange coefficient is isolated exactly as a finite sum of overlap-window commutators with $p+q=\mu_1(R,S)$.
3. *Strip-moment criterion.* The correct higher-order continuum theorem is stated cleanly: strip closure plus finite first moments imply a bond-centered first-order tangential action on smooth sampled profiles.
4. *Proper placement of the first nontrivial new case.* The visible order $\mu_1=3$ is identified as the first genuinely higher-coefficient exchange problem.

Just as important is what this paper deliberately does not claim.

1. *Explicit formulas for $A_R^{(2)}$ and beyond.* Those are not yet computed here for nontrivial prototype classes.
2. *Exact classification of active higher-order strip channels.* Hypothesis 1 states the right target, but the full channel list still has to be derived from the kernels.
3. *Exact first strip moments at non-leading order.* The theorem gives the criterion, not yet the explicit moments.
4. *Broader cross-regulator stability.* That is the subject of the next paper once the correct higher-order invariants have been identified.

**Strategic remark.**

This is not a retreat from phase 4. It is the exact completion of phase 4 at the strongest scope the present record can genuinely support. The paper now tells us precisely what the higher-order proof burden is, rather than pretending that explicit $A^{(2)}$-level closure is already in hand.

## Conclusion

Phase 4 is now complete at the strongest honest scope supported by the current relativistic ISP stack. The exact kernel algebra already fixes the higher-order overlap windows and the precise form of the first visible higher-order exchange coefficient. What remains unresolved is not where higher-order exchange lives, but how the exact coefficient algebra decomposes into strip channels and what first moments those channels carry.

That is the right next step from the Barandes perspective. One should not import extra ontology to repair an unfinished local algebra. One should continue the exact transition-law analysis until the higher-order bond-centered structure either closes or fails. The next paper therefore turns to regulator stability at precisely that level: not raw coefficient equality, but normalized strip-moment stability across support prototypes.

## References

1. [1] Anonymous, “Toward Lorentz-Covariant Indivisible Stochastic Processes: Spatial Locality, Temporal Indivisibility, and Localized Finite Deformations,” preprint (2026).
2. [2] Anonymous, “Localized Finite Deformations and the Free Dirac Exchange Defect in Relativistic Indivisible Stochastic Processes: Lie-Trotter and collar-excision rules, rule non-uniqueness, bond-centered thin-slab reduction, and renormalized universality,” preprint (2026).
3. [3] Anonymous, “Exact Localized Finite Deformations and the Free Dirac Exchange-Defect Theorem,” preprint (2026).
4. [4] Anonymous, “Exact Leading Support-Level Boundary Law for the Bond-Centered Thin-Slab Program,” preprint (2026).
5. [5] Anonymous, “Restricted Renormalized Universality of the Leading Bond-Centered Thin-Slab Law,” preprint (2026).
6. [6] J. A. Barandes, “The Stochastic-Quantum Correspondence,” *Philosophy of Physics* **3**, 8 (2025); arXiv:2302.10778.
7. [7] J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085 (2023; rev. 2026).
8. [8] J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192 (2025).
