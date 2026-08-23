# ISP v17 — U-Gen C3 additive-action character theorem candidate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Purpose and maximum scope

This note isolates the exact mathematical content of the often-written rule

$$
e^{iS/\hbar}.
$$

It does not assume that an action is ontic, that paths are actual, or that
quantum theory has been derived. It asks a narrower question:

> If a one-dimensional relative transport factor depends only on an additive
> action difference, composes multiplicatively, and is measurably controlled,
> what functional form is possible?

The answer is a continuous character of the additive action group. On
$\mathbb R$, that character has the form $e^{i\kappa s}$. The theorem explains
the exponential once its premises are supplied. It does not select the
physical action, $\kappa$, the complex one-dimensional carrier, the history
space, the summation rule, or an actuality law.

---

## 1. Typed setup

Let $s\in\mathbb R$ denote a signed action difference between two alternatives
with the same registered source and readout boundary. The sign reverses when
the alternatives are exchanged.

Let

$$
\chi:\mathbb R\longrightarrow U(1)
$$

be the relative transport assigned to that difference. The candidate premises
are:

1. **identity:** $\chi(0)=1$;
2. **sequential composition:** $\chi(s+t)=\chi(s)\chi(t)$;
3. **physical regularity:** $\chi$ is Borel measurable.

The composition premise is not a consequence of endpoint probabilities. It
asserts that two independently typed action-bearing segments concatenate and
that no additional context variable changes the relative transport.

The measurability premise excludes physically unpreparable discontinuous
characters. It is a genuine premise, not a notational convenience.

---

## 2. Theorem A — measurable additive-action character

**Theorem A.** Every Borel-measurable group homomorphism

$$
\chi:(\mathbb R,+)\longrightarrow U(1)
$$

has a unique $\kappa\in\mathbb R$ such that

$$
\boxed{\chi(s)=e^{i\kappa s}}
$$

for all $s\in\mathbb R$.

### Proof

First prove continuity at zero. Let $U$ be any neighborhood of $1$ in
$U(1)$. Choose an open arc $V$ about $1$ such that

$$
VV^{-1}\subset U.
$$

Compactness of $U(1)$ gives finitely many $z_1,\ldots,z_m$ whose translates
$z_jV$ cover $U(1)$. For a bounded interval $I$ of positive Lebesgue measure,
the measurable sets

$$
A_j=I\cap\chi^{-1}(z_jV)
$$

cover $I$, so at least one $A_j$ has positive measure. The Steinhaus theorem
then says that $A_j-A_j$ contains a neighborhood $O$ of zero. If
$h=a-b\in O$ with $a,b\in A_j$, then

$$
\chi(h)=\chi(a)\chi(b)^{-1}\in VV^{-1}\subset U.
$$

Thus $\chi$ is continuous at zero and hence everywhere.

Choose $\delta>0$ so that $\chi((-\delta,\delta))$ lies in an arc on which a
continuous argument is defined. Write

$$
\chi(s)=e^{i\theta(s)}
$$

there, with $\theta(0)=0$. On a sufficiently smaller interval, the
homomorphism identity and the absence of a $2\pi$ wrap give

$$
\theta(s+t)=\theta(s)+\theta(t).
$$

A continuous local solution of the Cauchy equation is linear, so there is a
$\kappa\in\mathbb R$ with $\theta(s)=\kappa s$ near zero. For arbitrary
$s$, choose $n$ large enough that $s/n$ is in this neighborhood. Then

$$
\chi(s)=\chi(s/n)^n=e^{i\kappa s}.
$$

If $e^{i\kappa s}=e^{i\kappa' s}$ for every real $s$, continuity near zero
forces $\kappa=\kappa'$. This proves uniqueness. $\square$

---

## 3. What each premise buys

| premise | earned conclusion | escape if removed |
|---|---|---|
| signed additive scalar $s$ | one additive control group | vector, non-Abelian, path-dependent, or contextual transport |
| $U(1)$-valued transport | scalar relative phase | higher-rank Gram transport or nonunit-modulus influence |
| homomorphism | exponential composition | memory, boundary, or interaction data enter at the seam |
| measurability | continuity and ordinary character | discontinuous Hamel-basis characters |
| one common $\chi$ | universal $\kappa$ within the registered domain | species-, sector-, or context-dependent constants |

The theorem is therefore a conditional classification, not a physical
derivation of quantum mechanics.

---

## 4. Corollary A1 — reversal

The character law gives

$$
\chi(-s)=\chi(s)^{-1}=\overline{\chi(s)}.
$$

Reversing the signed action difference complex-conjugates the relative
transport. Whether the sign of $\kappa$ is operationally fixed depends on an
independently oriented phase reference. If all reference conventions are also
conjugated, $\kappa$ and $-\kappa$ may represent the same complete operational
profile.

---

## 5. Corollary A2 — several additive controls

For a Borel-measurable character

$$
\chi:(\mathbb R^d,+)\longrightarrow U(1),
$$

there is a unique $k\in\mathbb R^d$ such that

$$
\chi(s)=e^{ik\cdot s}.
$$

This exposes a universality debt. If kinetic, electromagnetic, gravitational,
and internal-energy action contributions are entered as independent
coordinates, composition alone permits different coefficients. A single
coefficient $\kappa$ follows only if the physical input is already their
common total action or another principle identifies the coordinates.

---

## 6. Corollary A3 — topology changes the character set

If the physical action coordinate is periodic,

$$
s\in\mathbb R/L\mathbb Z,
$$

its continuous characters are

$$
\chi_n(s)=e^{2\pi i n s/L},\qquad n\in\mathbb Z.
$$

Thus topology can quantize allowed character sectors. It does not select
$L$, the topology, or the realized integer $n$.

For a multiply connected configuration space, the relevant object can instead
be a representation of a fundamental group. That case is not reduced to an
endpoint scalar unless the representation and sector are supplied.

---

## 7. Proposition B — operational quadrature identification

Suppose a registered balanced two-alternative experiment provides two
independently typed readouts with probabilities

$$
\begin{aligned}
p_c(s)&=\frac12\left[1+V\cos(\kappa s+\delta)\right],\\
p_s(s)&=\frac12\left[1+V\sin(\kappa s+\delta)\right],
\end{aligned}
$$

where $V>0$ is visibility and $\delta$ is a fixed apparatus offset. Define the
observable complex fringe coordinate

$$
Z(s)=\bigl(2p_c(s)-1\bigr)+i\bigl(2p_s(s)-1\bigr).
$$

Then

$$
Z(s)=Ve^{i(\kappa s+\delta)}
$$

and the ratio

$$
\frac{Z(s)}{Z(0)}=e^{i\kappa s}
$$

removes both visibility and the constant phase origin. If $s$ is scanned on
an open interval containing zero, the ratio uniquely identifies $\kappa$.

This proposition does not make $Z$ ontic. It is a compact encoding of two
families of observed record probabilities.

### Sampling limitations

1. If only $s=m\Delta$ is sampled, then

   $$
   \kappa\sim\kappa+\frac{2\pi n}{\Delta}
   $$

   remains an alias family.
2. If only the cosine quadrature is measured, simultaneous conjugation
   $(\kappa,\delta)\mapsto(-\kappa,-\delta)$ is invisible.
3. If $V=0$, no phase information is present.
4. Finite noisy data identify a confidence or credible region, never an exact
   real number.

---

## 8. Proposition C — finite phase points do not select a global law

Let $F=\{s_1,\ldots,s_n\}\subset\mathbb R$ be any finite calibration and
holdout set. Even if

$$
z_j=e^{i\kappa s_j}
$$

is observed exactly at every $s_j$, infinitely many continuous maps

$$
\widetilde\chi:\mathbb R\longrightarrow U(1)
$$

agree on $F$ and differ elsewhere.

### Proof

Choose any nonzero continuous real function $g$ satisfying $g(s_j)=0$ for
all $j$, for example a bounded multiple of

$$
\prod_j\frac{(s-s_j)^2}{1+(s-s_j)^2}.
$$

Then

$$
\widetilde\chi(s)=e^{i[\kappa s+g(s)]}
$$

agrees with the character on $F$ and differs elsewhere. $\square$

Therefore finite experiments support the homomorphism law but cannot prove it
without a declared law class. The concatenation tests in C3 must attack that
class assumption directly.

---

## 9. Proposition D — action shift and boundary gauge

If an action changes by an endpoint term

$$
S[h]\mapsto S[h]+f(b_{m out})-f(b_{m in}),
$$

then the amplitude character changes by boundary phases. For two alternatives
with the same input and output boundaries, their relative phase is unchanged.

This is the finite-history form of the familiar fact that total derivatives
or gauge transformations can alter path representatives without changing a
closed relative holonomy. A future experiment contract must compare
gauge-invariant complete predictions, not absolute path phases.

---

## 10. Relation to the C2 kernel decomposition

For a rank-one history kernel with weights $w_j$ and additive actions $S_j$,
the character supplies

$$
a_j=\sqrt{w_j}\,e^{i\kappa S_j},
\qquad
D_{jk}=\sqrt{w_jw_k}\,e^{i\kappa(S_j-S_k)}.
$$

The action character fills only the rank-one correlation coordinate. It does
not determine the weights $w_j$, the allowed histories, the boundary state,
or the record partition. Higher-rank kernels require more than one scalar
character, such as unresolved environment vectors or a mixed boundary state.

---

## 11. Hostile mathematical controls

1. **Endpoint-only mutant:** $\chi$ is inferred from endpoint probabilities
   that carry no relative phase.
2. **Lookup mutant:** a separate $\chi_E$ is tabulated for each experiment.
3. **Seam-memory mutant:** $\chi(s+t)$ secretly receives the split $(s,t)$.
4. **Nonmeasurable mutant:** a Hamel-basis character is called physically
   preparable.
5. **Vector-collapse mutant:** several action coordinates are silently given
   one coefficient.
6. **Topology-erasure mutant:** a noncontractible loop is treated as an
   endpoint gauge.
7. **Quadrature-import mutant:** the target phase is inserted through the
   reference readout.
8. **Aliasing mutant:** a discrete calibration grid is reported as a unique
   $\kappa$.
9. **Visibility mutant:** loss of contrast is interpreted as a phase failure.
10. **Conjugation mutant:** a convention-level sign is promoted to new
    physics.
11. **Finite-interpolation mutant:** agreement on finitely many points is
    called a derivation of the global character.
12. **Rank-one promotion:** the character theorem is applied to a higher-rank
    decoherence kernel without proving rank one.

---

## 12. What the theorem does and does not explain

It explains conditionally:

$$
\text{additive action}
+\text{multiplicative scalar transport}
+\text{measurability}
\Longrightarrow e^{i\kappa S}.
$$

It does not explain:

1. why the physical control is an action;
2. why the transport is scalar and $U(1)$-valued;
3. why amplitudes for alternatives add;
4. why $\kappa$ is universal or equals $1/\hbar$;
5. which action and fields occur in nature;
6. why any history is actual;
7. why records obey the Born rule;
8. the Standard Model;
9. spacetime or gravity; or
10. a new empirical prediction.

This object is suitable only as author-side mathematics pending independent
review.
