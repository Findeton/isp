# Relativistic ISP V3 Paper 31: Same-Law Source-Response Calculus And Curvature Campaign

Author: Felix Robles Elvira

Date: 2026-05-26

## Abstract

Paper 30 ends with a genuine change of viewpoint.  The heat-bad full-block
obstruction is no longer treated as an unknown table entry to be guessed.
It is rewritten as a trace-dual supremum of first responses of same-law
finite source pressures.  This paper develops that idea as a general
calculus.

The goal is not to introduce path integrals, hidden Markov bridges, or a
cleaner comparison law.  The goal is to make the impossible quantities
natural inside the actual finite adaptive law.  A missing same-law value is
recast as a derivative at source strength zero; a missing norm bound becomes
a supremum over deterministic dual probes; a Dobrushin row becomes a mixed
boundary/interior response; a defect-polymer activity becomes a connected
cumulant; a lower-floor witness becomes a sign-coherent source slope.

The paper begins by defining a finite same-law source pressure
$$
\Psi_{\mathbf V}^{N,j}(\mathbf s)
=
\log
\mathbf E_{N,j}^{act}
\exp\left\{\sum_i s_iV_i^{N,j}\right\},
$$
where the expectation is always taken under the actual adaptive finite DLR
law.  It then prints the derivative dictionary:

1. first derivatives are values;
2. second derivatives are covariances and susceptibilities;
3. mixed boundary/interior derivatives are influence rows;
4. higher derivatives are connected cumulants and Mobius activities;
5. trace-dual suprema are norm debits;
6. Peter-Weyl coefficient probes are Fourier-source derivatives;
7. sign-coherent slopes are lower-floor witnesses;
8. source neutrality plus curvature gives upper debits.

The first worked target remains the Paper-30 heat-bad matrix
$$
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
=
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$
But the calculus is deliberately general: it is exported to the Paper-29
low-mode entries, RN-MIXAMP rows, primitive residual atoms, Dobrushin rows,
defect KP/Mobius activities, bridge residual tilt, and Peter-Weyl tail
gates.

The source-response identity is not a proof of smallness by itself.  It is
a new shape for the proof.  The live positive theorem becomes source
neutrality, source curvature, a Ward identity, a log-Sobolev or concentration
bound, a Peter-Weyl source-tail theorem, or a sign-coherent source-floor
witness.

## 0. Same-Law Convention

### Convention 0.1: Actual Law Only

Throughout this paper, \(\mathbf E_{N,j}^{act}\) denotes expectation under
the actual adaptive finite DLR law after the `SEL2` pushforward and all
licensed Paper-20--30 reductions that are explicitly imported.

When a source parameter \(s\) is introduced, it is not a new physical law.
It is a deterministic generating-function parameter.  All physical values
are derivatives at \(s=0\), evaluated under the actual law.

Thus the source pressure
$$
\Psi(s)=\log\mathbf E_{N,j}^{act}e^{sV}
$$
is a same-law object.  For \(s\ne0\), it is only a probe.  It is not a hidden
Markov dynamics, not a heat-kernel replacement, not a comparison measure,
and not a substitute Yang-Mills theory.

### Convention 0.2: Finite Regularity

All finite derivatives below are taken before the cofinal limit.  At fixed
\((N,j)\), the underlying chart, Peter-Weyl cutoff, retained block family,
and regularized finite DLR conditional are finite-dimensional.  Hence
differentiation under the finite integral is legitimate for bounded source
observables.

The cofinal assertions always come after the finite identities have been
proved.

## 1. General Source Pressure

### Definition 1.1: Source Family

A same-law source family is a finite list of real bounded observables
$$
\mathbf V^{N,j}
=
(V_1^{N,j},\ldots,V_m^{N,j})
$$
on the actual finite DLR probability space.  The observables may be scalar
readouts, trace-dual pairings of finite matrices, boundary probes, interior
defect insertions, Peter-Weyl coefficients, or signed retained-row
functionals.

For \(\mathbf s=(s_1,\ldots,s_m)\), define the source pressure
$$
\Psi_{\mathbf V}^{N,j}(\mathbf s)
:=
\log
\mathbf E_{N,j}^{act}
\left[
\exp\left\{
\sum_{i=1}^m s_iV_i^{N,j}
\right\}
\right].
$$

### Lemma 1.2: First Derivative Is The Actual Value

For each \(i\),
$$
\partial_i\Psi_{\mathbf V}^{N,j}(0)
=
\mathbf E_{N,j}^{act}[V_i^{N,j}].
$$

Proof.

Differentiate the finite generating function at \(\mathbf s=0\):
$$
\partial_i\Psi(0)
=
{\mathbf E[V_i e^0]\over \mathbf E[e^0]}
=
\mathbf E[V_i].
$$
`square`

### Lemma 1.3: Second Derivative Is Covariance

For \(i,k\),
$$
\partial_i\partial_k\Psi_{\mathbf V}^{N,j}(0)
=
\operatorname{Cov}_{N,j}^{act}(V_i,V_k).
$$

Proof.

This is the standard finite derivative identity for the logarithm of the
moment generating function:
$$
\partial_i\partial_k\Psi(0)
=
\mathbf E[V_iV_k]
-
\mathbf E[V_i]\mathbf E[V_k].
$$
`square`

### Lemma 1.4: Higher Derivatives Are Joint Cumulants

For any \(r\ge1\),
$$
\partial_{i_1}\cdots\partial_{i_r}
\Psi_{\mathbf V}^{N,j}(0)
=
\kappa_{N,j}^{act}(V_{i_1},\ldots,V_{i_r}),
$$
the joint cumulant of the listed actual-law observables.

Proof.

The logarithm of the finite moment generating function is the cumulant
generating function. `square`

## 2. The Derivative Dictionary

This section lists the source-response forms that can replace missing value
tables.  The point is not that every derivative is small.  The point is that
every missing value theorem has a precise derivative analogue.

### Dictionary 2.1: Linear Values

An actual same-law value
$$
\mathbf E_{N,j}^{act}[F]
$$
is the first source derivative of
$$
\Psi_F(s)=\log\mathbf E_{N,j}^{act}e^{sF}.
$$

This covers:

1. primitive residual atom values;
2. retained row weights;
3. bridge signed values;
4. low-mode matrix entries after choosing a matrix coefficient probe;
5. direct heat-bad source slopes.

### Dictionary 2.2: Trace-Norm Debits

For a finite matrix-valued actual object \(M_\Gamma(\omega)\), define a
trace-dual probe \(Q_\Gamma\) with \(\|Q_\Gamma\|_{op}\le1\), and set
$$
V_Q(\omega)
=
\sum_\Gamma
{1\over2}
\operatorname{Re}\operatorname{Tr}(Q_\Gamma^*M_\Gamma(\omega)).
$$
Then
$$
\sum_\Gamma {1\over2}\|M_\Gamma\|_1
=
\sup_Q
\partial_s\Psi_Q(0),
$$
after the same normalization used in the relevant ledger.

This covers:

1. Paper-30 heat-bad absolute debit;
2. full-block switching defect;
3. weighted oddness debits;
4. projected residual/Jacobian debits;
5. finite dual certificate residual directions.

### Dictionary 2.3: Operator Norms And Spectral Rows

For a finite operator \(T\) on a low-mode space,
$$
\|T\|_{op}
=
\sup_{\|x\|=\|y\|=1}
\operatorname{Re}\langle y,Tx\rangle.
$$
Each matrix element
$$
\operatorname{Re}\langle y,Tx\rangle
$$
is a first source response for the corresponding dual vector probe.

Thus a strict low-mode spectral gap can be attacked by proving a uniform
source-response bound over all unit vector probes.

### Dictionary 2.4: Oscillation And Range

For a scalar finite Hamiltonian \(H\), the oscillation
$$
\operatorname{osc}(H)
=
\sup_{a,b}(H(a)-H(b))
$$
is the supremum over signed two-point probes of total mass zero.  Equivalently,
it is a norm dual to signed zero-mass test charges.

Hence a range or one-line-width bound can be treated as a source-response
bound over signed zero-mass probes.

### Dictionary 2.5: Boundary Influence Rows

Let \(A_x\) be an interior observable and \(B_y\) a boundary source probe.
Define
$$
\Psi_{x,y}(s,t)
=
\log
\mathbf E^{act}
\exp\{sA_x+tB_y\}.
$$
Then
$$
\partial_s\partial_t\Psi_{x,y}(0,0)
=
\operatorname{Cov}^{act}(A_x,B_y).
$$

This is the infinitesimal version of a Dobrushin row.  A full Dobrushin
coefficient still requires a uniform nonlinear boundary variation estimate,
but the mixed derivative is the natural local object.

### Dictionary 2.6: Mixed RN And Cross-Ratio Rows

For endpoint probes \(A_u,A_v\) and a residual observable \(R\), the mixed
response
$$
\partial_u\partial_v\Psi(0)
$$
or the fourth response
$$
\partial_u\partial_v\partial_{\bar u}\partial_{\bar v}\Psi(0)
$$
is the source-response form of RN-MIXAMP and related cross-ratio tests.

Endpoint-additive terms vanish under the mixed derivative.  This matches the
Paper-26/Paper-29 lesson: mixed ratios see only the mixed part, not the full
conditional kernel.

### Dictionary 2.7: Connected Activities And Mobius/KP Terms

For a family of local defect probes \(\{F_x\}_{x\in A}\),
$$
\partial_A\Psi(0)
:=
\prod_{x\in A}\partial_{s_x}
\Psi(\mathbf 0)
$$
is the connected cumulant
$$
\kappa^{act}(\{F_x\}_{x\in A}).
$$

Thus defect polymer activities and Mobius activities are higher source
derivatives.  KP smallness can be attacked by connected-source derivative
decay rather than by pointwise atom recovery.

### Dictionary 2.8: Peter-Weyl Coefficients

Let \(c_{\lambda,mn}\) be a Peter-Weyl coefficient of an actual residual or
bridge observable.  If \(D_{\lambda,mn}\) is the corresponding deterministic
matrix-coefficient probe, then
$$
c_{\lambda,mn}
=
\mathbf E^{act}[D_{\lambda,mn}]
=
\partial_s\Psi_{\lambda,mn}(0).
$$

A Peter-Weyl tail theorem can therefore be reframed as a weighted
source-response summability theorem over high \(\lambda\).

### Dictionary 2.9: Ward And Schwinger-Dyson Source Derivatives

If \(X\) is a compact-Lie infinitesimal vector field and \(F\) is a source
probe, finite integration by parts gives identities of the schematic form
$$
\mathbf E^{act}[XF]
=
-
\mathbf E^{act}[F S_X],
$$
where \(S_X\) is the actual residual/Jacobian score.  In source language,
both sides are first responses of derived probes.

Thus Ward identities can be treated as exact relations among source
derivatives.

### Dictionary 2.10: Floors As Source Slopes

A sign-coherent floor witness is a lower bound
$$
\liminf_{(N,j)}
\left|
\partial_s\Psi_Q^{N,j}(0)
\right|
\ge M_*,
$$
for a probe \(Q\) whose sign and normalization survive the retained ledger.

This is the same object as a positive source response, but interpreted as a
negative/falsifying theorem when it exceeds the Branch-A budget.

## 3. Source Neutrality, Curvature, And Debit Bounds

### Definition 3.1: Source Neutrality

For a source family \({\mathcal Q}\), `P31-SRC-NEUT(a,rho;Qfam)` asserts
that cofinally, for every \(Q\in{\mathcal Q}\),
$$
\left|
\Psi_Q^{N,j}(a)-\Psi_Q^{N,j}(-a)
\right|
\le2\rho.
$$

This says the source pressure is nearly even over the interval \([-a,a]\).

### Definition 3.2: Source Curvature

`P31-SRC-CURV(a,chi;Qfam)` asserts that cofinally, for every
\(Q\in{\mathcal Q}\) and every \(|s|\le a\),
$$
\left|
{\partial^2\over\partial s^2}
\Psi_Q^{N,j}(s)
\right|
\le\chi.
$$

Since
$$
\Psi_Q''(s)
=
\operatorname{Var}_{s,Q}(V_Q),
$$
for real scalar \(V_Q\), this is a same-law susceptibility bound for the
tilted finite generating function.

### Lemma 3.3: Neutrality Plus Curvature Bounds First Response

If `P31-SRC-NEUT(a,rho;Qfam)` and `P31-SRC-CURV(a,chi;Qfam)` hold, then
$$
\sup_{Q\in{\mathcal Q}}
\left|
\partial_s\Psi_Q^{N,j}(0)
\right|
\le
{\rho\over a}+{\chi a\over2}
$$
cofinally.

Proof.

This is the calculus estimate from Paper 30 Lemma 146.2, applied uniformly
over the source family \({\mathcal Q}\). `square`

### Corollary 3.4: Constant-Curvature Optimization

If \(\rho\) and \(\chi\) are independent of \(a\), the optimized debit is
$$
\sqrt{2\rho\chi}.
$$

Thus the source-response route wants either strong near-evenness, small
curvature, or a choice of source scale \(a\) that balances the two.

## 4. Export To The Paper-30 Heat-Bad Object

### Definition 4.1: Paper-30 Heat-Bad Source Family

Let
$$
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
=
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right).
$$

Let \({\mathcal Q}_{HB}\) be the family of deterministic block probes
\(Q=\{Q_\Gamma\}\) satisfying
$$
\|Q_\Gamma\|_{op}\le1,
\qquad
Q_\Gamma=P_{\Gamma,bad}^{HK}Q_\Gamma P_{\Gamma,bad}^{HK}.
$$

Define
$$
V_Q^{HB,N,j}
=
{1\over Z_B^{N,j}(\eta)}
\sum_\Gamma
{1\over2}
\operatorname{Re}\operatorname{Tr}
\left(
Q_\Gamma^*
\mathcal W_{\Gamma,bad}^{N,j}(\delta)
\right),
$$
and
$$
\Psi_Q^{HB,N,j}(s)
=
\log\mathbf E^{act}_{N,j}e^{sV_Q^{HB,N,j}}.
$$

### Theorem 4.2: Heat-Bad Source Calculus Recovers Paper 30

For the family \({\mathcal Q}_{HB}\),
$$
\mathrm{P31\text{-}SRC\text{-}NEUT}(a,\rho;{\mathcal Q}_{HB})
+
\mathrm{P31\text{-}SRC\text{-}CURV}(a,\chi;{\mathcal Q}_{HB})
$$
implies
$$
\mathrm{P30\text{-}HKBAD\text{-}ABS}
\left(\delta,{\rho\over a}+{\chi a\over2}\right).
$$

Proof.

Paper 30 Lemma 145.2 identifies the heat-bad absolute debit with the
supremum of the first response over \({\mathcal Q}_{HB}\).  Lemma 3.3 bounds
that response. `square`

### Corollary 4.3: First Paper-31 Live Gate

The first live Paper-31 positive gate is
$$
\boxed{
\mathrm{P31\text{-}HKBAD\text{-}SRC\text{-}NEUT}(a,\rho)
\quad+\quad
\mathrm{P31\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
}
$$

The gate is useful if
$$
{\rho\over a}+{\chi a\over2}
$$
fits inside the Paper-30 residual signed budget.

## 5. Export To Paper-29 Low-Mode Entries

### Definition 5.1: Low-Mode Dual Source Family

Let \(T_{e,\zeta,\circ}^{N,j}\) be the actual same-law conditional transfer
operator of Paper 28/Paper 29, and let
$$
\Pi_{\le L}
$$
be the low-mode projection.  For unit vectors \(x,y\) in the low-mode space,
define the dual entry probe
$$
V_{x,y}^{LM,N,j}
=
\operatorname{Re}
\left\langle
y,
\Pi_{\le L}T_{e,\zeta,\circ}^{N,j}\Pi_{\le L}x
\right\rangle.
$$

Let
$$
\Psi_{x,y}^{LM,N,j}(s)
=
\log\mathbf E^{act}_{N,j}e^{sV_{x,y}^{LM,N,j}}.
$$

### Lemma 5.2: Low-Mode Norm As Source Supremum

The low-mode operator norm satisfies
$$
\left\|
\Pi_{\le L}T_{e,\zeta,\circ}^{N,j}\Pi_{\le L}
\right\|
=
\sup_{\|x\|=\|y\|=1}
\partial_s\Psi_{x,y}^{LM,N,j}(0).
$$

Proof.

This is the operator-norm dual formula combined with Lemma 1.2. `square`

### Corollary 5.3: Low-Mode Source Gap Target

The Paper-29 low-mode gap can be attacked by proving a uniform source
response bound:
$$
\sup_{e,\zeta,x,y}
\partial_s\Psi_{x,y}^{LM,N,j}(0)
<
\theta_{\mathrm{crit}}-\kappa^{act}[L].
$$

Equivalently, prove source neutrality and source curvature for the low-mode
dual family.

This does not recover the missing conditional kernel.  It bypasses kernel
reconstruction by bounding every low-mode dual response.

## 6. Export To RN-MIXAMP And Cross-Ratio Rows

### Definition 6.1: Endpoint Mixed Source Pressure

Let \(A_u,A_v\) be endpoint source probes and \(R_{mix}\) the residual mixed
observable selected by the RN-MIXAMP row.  Define
$$
\Psi_{RN}^{N,j}(s,t)
=
\log
\mathbf E_{N,j}^{act}
\exp\{sA_u+tA_v+R_{mix}\}.
$$

The schematic mixed row is measured by
$$
\partial_s\partial_t\Psi_{RN}^{N,j}(0,0)
$$
after the endpoint-additive cancellations and retained-row normalizations
used in Papers 26--27.

### Lemma 6.2: Mixed Derivatives Kill Endpoint-Additive Terms

If
$$
R_{mix}(u,v)=r_1(u)+r_2(v)+c,
$$
then
$$
\partial_u\partial_v R_{mix}=0.
$$

Thus a mixed source derivative sees the doubly centered part of the residual
row, matching the RN-MIXAMP cancellation logic.

Proof.

Differentiate once in each endpoint variable.  Endpoint-additive summands
are killed by the derivative in the other variable. `square`

### Corollary 6.3: RN-MIXAMP Source Target

The direct RN-MIXAMP smallness theorem can be reframed as a bound on
endpoint mixed source derivatives.  This may help if a Ward/reflection
identity controls the mixed source pressure.  It does not, by itself,
recover the full low-mode conditional kernel, in agreement with Paper 29.

## 7. Export To Primitive Residual Values

### Definition 7.1: Primitive Residual Atom Sources

Let \(h_A^{N,j}\) be a primitive residual atom or retained defect atom from
Paper 29.  Define
$$
\Psi_A^{prim,N,j}(s)
=
\log
\mathbf E_{N,j}^{act}e^{s h_A^{N,j}}.
$$

Then
$$
\partial_s\Psi_A^{prim,N,j}(0)
=
\mathbf E_{N,j}^{act}[h_A^{N,j}].
$$

### Proposition 7.2: Source Response Does Not Magically Populate Atoms

The identity in Definition 7.1 is exact, but it does not by itself populate
the primitive residual atom values required by Paper 29.

Proof.

Paper 29 proves that primitive residual atom values are not determined by
RN-MIXAMP ratios or finite labels alone.  Rewriting an atom value as a first
source derivative changes the analytic target, but the derivative still
requires a source-neutrality, curvature, Ward, tail, or floor theorem.
`square`

### Corollary 7.3: Primitive Residual Source Routes

A positive Paper-31 route for primitive residual values must prove one of:

1. source neutrality and curvature for the atom family;
2. a Ward identity making the atom derivative vanish or small;
3. a connected-cumulant decay theorem for retained defect atoms;
4. a Peter-Weyl source-tail theorem for omitted atoms;
5. a sign-coherent source-slope floor.

## 8. Export To Dobrushin Rows

### Definition 8.1: Boundary-Interior Source Response

Let \(F_x\) be an interior observable and \(G_y\) a boundary probe.  Define
$$
\Psi_{xy}^{N,j}(s,t)
=
\log
\mathbf E_{N,j}^{act}e^{sF_x+tG_y}.
$$

The infinitesimal boundary influence is
$$
I_{xy}^{lin}
:=
\partial_s\partial_t\Psi_{xy}^{N,j}(0,0)
=
\operatorname{Cov}^{act}(F_x,G_y).
$$

### Definition 8.2: Source-Dobrushin Row

`P31-SRC-DOB(q,a)` asserts that the nonlinear boundary variation used in the
Paper-25/Paper-29 Dobrushin rows is bounded by a source-response majorant:
$$
\sum_y e^{ad(x,y)}
\sup_{\|G_y\|_{\mathrm{bd}}\le1}
\left|
\partial_s\partial_t\Psi_{xy}^{N,j}(0,0)
\right|
\le q<1
$$
cofinally, with the same row weights and boundary norm as the relevant
Dobrushin specification.

### Proposition 8.3: Linear Response Is Necessary But Not Always Sufficient

`P31-SRC-DOB(q,a)` is a valid infinitesimal Dobrushin target.  To recover
the full Dobrushin contraction, one must also control nonlinear boundary
variation away from zero or prove convexity that upgrades the infinitesimal
bound to a finite variation bound.

Proof.

Dobrushin coefficients are finite boundary perturbation suprema.  Mixed
second derivatives give their infinitesimal form.  A uniform convexity or
bounded-curvature theorem along the boundary source segment upgrades the
infinitesimal bound to a finite bound. `square`

## 9. Export To Defect KP And Mobius Activities

### Definition 9.1: Connected Source Activities

For local defect probes \(\{F_x\}_{x\in A}\), define
$$
\Psi_A(\mathbf s)
=
\log\mathbf E^{act}
\exp\left\{\sum_{x\in A}s_xF_x\right\}.
$$

The connected activity is
$$
\mathcal A_A^{conn}
=
\left.
\prod_{x\in A}\partial_{s_x}
\Psi_A(\mathbf s)
\right|_{\mathbf s=0}.
$$

### Lemma 9.2: Connected Activities Are Source Cumulants

$$
\mathcal A_A^{conn}
=
\kappa^{act}(\{F_x\}_{x\in A}).
$$

Proof.

This is Lemma 1.4. `square`

### Corollary 9.3: KP From Connected Source Decay

If the connected source cumulants obey
$$
\sum_{A\ni x}
e^{a|A|}
|\mathcal A_A^{conn}|
\le a_x
$$
with the Paper-29/Paper-30 KP weights, then the corresponding defect KP
smallness theorem is sourced.

This is the source-response version of the Mobius/KP route.

## 10. Export To Peter-Weyl Tails

### Definition 10.1: Fourier Source Probes

For a Peter-Weyl channel \(\lambda\) and matrix index \(m,n\), let
$$
D_{\lambda,mn}
$$
be the deterministic matrix-coefficient probe of the actual residual or
bridge observable.  Define
$$
\Psi_{\lambda,mn}^{PW}(s)
=
\log
\mathbf E^{act}e^{sD_{\lambda,mn}}.
$$

Then
$$
c_{\lambda,mn}
=
\partial_s\Psi_{\lambda,mn}^{PW}(0).
$$

### Definition 10.2: Source Peter-Weyl Tail

`P31-SRC-PWTAIL(A,c,L0)` asserts a cofinal bound
$$
\sum_{\lambda:\ C_2(\lambda)>L}
d_\lambda^p
\sup_{m,n}
\left|
\partial_s\Psi_{\lambda,mn}^{PW}(0)
\right|
\le
Ae^{-cL}
$$
for the relevant exponent \(p\) and channel family.

### Proposition 10.3: PW Tail Is A Response-Tail Theorem

`P31-SRC-PWTAIL` is exactly the source-response version of the same-law
Peter-Weyl coefficient decay repeatedly isolated in Papers 28--30.

Proof.

Peter-Weyl coefficients are first responses of Fourier probes.  Summability
of those responses is precisely a coefficient-tail theorem. `square`

## 11. Source Floors

### Definition 11.1: Source-Slope Floor

For a source family \({\mathcal Q}\), `P31-SRC-FLOOR(M*)` asserts that there
is a deterministic cofinal choice \(Q_{N,j}\in{\mathcal Q}\) such that
$$
\liminf_{(N,j)}
\left|
\partial_s\Psi_{Q_{N,j}}^{N,j}(0)
\right|
\ge M_*,
$$
and the sign, orientation, normalization, retained-row, and endpoint
conventions match the corresponding lower-floor ledger.

### Lemma 11.2: Source Floors Are Same-Law Lower Floors

If `P31-SRC-FLOOR(M*)` is proved for a Branch-A obstruction object and
\(M_*\) exceeds the remaining Branch-A budget, then that Branch-A route is
falsified.

Proof.

The source slope is the actual-law value of the obstructing retained
functional.  A sign-coherent lower bound above the budget cannot be absorbed
by the positive route. `square`

## 12. Obstruction Export Table

| obstruction | old form | source-response form | live theorem |
|---|---|---|---|
| Paper-30 heat-bad | \(\|\mathcal W_{bad}\|_1\) | \(\sup_Q\partial_s\Psi_Q(0)\) | `P31-HKBAD-SRC-NEUT + P31-HKBAD-SRC-CURV` |
| Paper-29 low-mode | missing \(T_{\le L}\) entries | unit-vector source responses | `P31-LOWMODE-SRCGAP` |
| Paper-28 tail | missing coefficient decay | Fourier source response summability | `P31-SRC-PWTAIL` |
| Paper-27 RN-MIXAMP | mixed RN row | endpoint mixed derivative | `P31-RNMIXAMP-MIXDER` |
| primitive residual atoms | missing atom values | atom source slopes | `P31-PRIMRES-SRCVAL` |
| Dobrushin rows | conditional variation | boundary/interior mixed response plus curvature upgrade | `P31-SRC-DOB` |
| defect KP | polymer activity values | connected cumulants | `P31-CONN-SRC-KP` |
| bridge residual tilt | doubly centered RN tilt | endpoint mixed source response | `P31-BRIDGE-TILT-SRC` |
| floor exits | lower predebit witness | sign-coherent source slope | `P31-SRC-FLOOR` |

## 13. First Live Work Packages

The paper now has the following concrete work packages.

1. Prove or falsify `P31-HKBAD-SRC-NEUT(a,rho)` from the known orientation,
   reflection, conjugation, and recoupling symmetries.
2. Prove or falsify `P31-HKBAD-SRC-CURV(a,chi)` using finite variance,
   Dirichlet, log-Sobolev, or Peter-Weyl source-tail estimates.
3. Apply the same two tests to the Paper-29 low-mode unit-vector source
   family.
4. Test whether Dobrushin influence rows admit a curvature upgrade from
   infinitesimal source response to finite boundary variation.
5. Test whether connected source cumulants give a better route to the
   defect KP/Mobius activity theorem.
6. If smallness fails, search for a sign-coherent source floor.

## 14. Pre-Closure Status After The First Calculus Print

The source-response calculus was first printed at the finite same-law level.
It proves a real reframing:
$$
\text{missing values}
\quad\leadsto\quad
\text{source derivatives at zero under the actual law}.
$$

At this stage it had not yet proved the needed source neutrality, curvature,
coefficient tail, or floor theorem.  Those were the live analytic targets
opened by the first pass.

This is progress because the target has changed form.  Instead of asking for
the whole conditional distribution, we can attack a family of response
inequalities.  If the response family has a symmetry, convexity, Ward, or
tail structure, it may be strictly easier than row reconstruction.  If it
does not, the source-slope formulation gives a clean route to a lower-floor
witness.

Sections 15--26 now close this menu as a calculus: every route is either
proved as an exact identity, conditionally reduced to a named same-law
primitive, or falsified as a current-corpus derivation.

## 15. Barandes Alignment Audit

This paper must be read through the indivisible-stochastic-process
discipline, not through a hidden dynamics discipline.  The local Barandes
papers used as alignment sources are:

1. Jacob A. Barandes, *The Stochastic-Quantum Correspondence*;
2. Jacob A. Barandes, *The Stochastic-Quantum Theorem*;
3. Jacob A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*.

The relevant alignment commitments are the following.

### Commitment 15.1: Configuration/Record Law First

The primitive object is a stochastic law on a configuration or record space.
Hilbert-space objects, Peter-Weyl coordinates, matrices, and operator
representations are calculational structures unless and until they are
projected back to same-law probabilities, conditionals, or record
functionals.

Paper 31 satisfies this commitment because every source pressure has the
form
$$
\Psi_V(s)
=
\log \mathbf E^{act}e^{sV},
$$
where \(V\) is an actual record functional and the expectation is under the
actual finite adaptive law.

### Commitment 15.2: No Markov Approximation

Barandes' indivisible stochastic processes are not assumed to divide into
Markov transition steps.  Markov chains are special cases or approximations,
not primitive structure.

Paper 31 satisfies this commitment because it never writes
$$
K(t_2,t_0)=K(t_2,t_1)K(t_1,t_0)
$$
for the adaptive law, and never infers finite boundary variation from an
unproved Markov generator.  The Dobrushin section explicitly says that a
mixed derivative is only infinitesimal and does not recover a finite
transition row by itself.

### Commitment 15.3: Source Parameters Are Not Dynamics

The parameter \(s\) in \(\Psi_V(s)\) is a deterministic probe parameter.  It
is not a physical intervention, not a division event, not a new DLR
specification, and not a replacement Yang-Mills measure.

When this paper writes a symbol such as
$$
\operatorname{Var}_{s,V}(V),
$$
it is shorthand for the ratio of same-law finite integrals obtained by
differentiating \(\log \mathbf E^{act}e^{sV}\).  It is not an assertion that
the tilted density is a new ontology or a new stochastic process.

### Commitment 15.4: Representation Variables Are Not Reified

Peter-Weyl coefficients, low-mode matrices, trace-dual probes, and
matrix-coefficient observables are admissible only as finite functions of
the actual record.  They are not additional beables and not hidden amplitude
variables.  Their role is the same as a Hilbert-space representation in the
Barandes dictionary: useful for calculation, not ontologically primary.

### Proposition 15.5: Paper 31 Is Barandes-Aligned

Paper 31 is aligned with the local Barandes corpus.

Proof.

Every source pressure is an actual-law exponential moment.  Every physical
quantity extracted from it is a derivative at \(s=0\).  No source pressure
is used as a substitute law at \(s\ne0\).  No Markov factorization, hidden
bridge process, off-law heat kernel, or comparison measure is introduced.
The matrix and Peter-Weyl objects are finite readouts of the same record
space, so they remain calculational representations rather than additional
ontology. `square`

### Corollary 15.6: The Remaining Risk Is Analytic, Not Interpretive

The source-response reframing is not rejected by Barandes alignment.  The
remaining risk is that the needed source neutrality, curvature, tail, or
floor estimate is a genuinely new same-law analytic theorem.  The
Barandes-aligned rule is therefore:

$$
\text{source calculus may re-express actual values, but may not replace them}.
$$

## 16. Universal Source Identities And No-Free-Smallness

The first closure pass is to separate identities from estimates.

### Theorem 16.1: Finite Source Calculus Is Complete At The Identity Level

At fixed finite \((N,j)\), every bounded actual-law observable \(V\) satisfies
$$
\partial_s \log \mathbf E^{act}e^{sV}\bigg|_{s=0}
=
\mathbf E^{act}[V],
$$
and every finite family \(V_1,\ldots,V_m\) satisfies
$$
\partial_{s_{i_1}}\cdots\partial_{s_{i_k}}
\log \mathbf E^{act}\exp\left\{\sum_{\ell=1}^m s_\ell V_\ell\right\}
\bigg|_{\mathbf s=0}
=
\kappa^{act}(V_{i_1},\ldots,V_{i_k}).
$$

Consequently every missing scalar value, finite matrix entry, trace-dual
norm debit, mixed endpoint response, connected activity, Peter-Weyl
coefficient, and floor witness listed in Section 12 has an exact
source-response representation.

Proof.

At fixed finite \((N,j)\), all source observables are bounded functions on a
finite or regularized finite-dimensional probability space.  Differentiation
under the finite integral is legitimate.  The logarithm of the moment
generating function is the cumulant generating function. `square`

### Proposition 16.2: No Universal Source Smallness

The identities in Theorem 16.1 do not imply smallness.

More precisely, let \(R>0\) and \(m\in[-R,R]\).  There is a two-point
finite probability space with a bounded observable \(V\in\{-R,R\}\) such
that
$$
\partial_s \log \mathbf E e^{sV}\bigg|_{s=0}
=
m.
$$

Proof.

Choose probabilities
$$
p_+=\frac12\left(1+\frac{m}{R}\right),
\qquad
p_-=\frac12\left(1-\frac{m}{R}\right),
$$
and let \(V=R\) on the first point and \(V=-R\) on the second point.  Then
\(\mathbf E[V]=m\), and the first derivative of the source pressure at zero
is \(\mathbf E[V]\). `square`

### Corollary 16.3: What Formal Source Calculus Can And Cannot Close

Source calculus can close:

1. exact identities;
2. equivalences between old value gates and source-response gates;
3. conditional implications from source neutrality, curvature, Ward,
   tail, or floor inputs.

Source calculus cannot close, by itself:

1. small first response;
2. strict low-mode spectral contraction;
3. Peter-Weyl tail decay;
4. nonlinear Dobrushin contraction;
5. sign-coherent floor;
6. primitive residual atom values.

Those require object-specific same-law information.

### Lemma 16.4: The Trivial Curvature Bound Is Not Enough

If \(V\) is bounded and
$$
\operatorname{osc}(V)\le R,
$$
then
$$
\Psi_V''(s)\le {R^2\over4}
$$
for every real \(s\), as a finite Hoeffding-type bound on the algebraic
source ratio.  This is usually too coarse for the Branch-A margins.

Proof.

The second derivative of the log moment generating function is the variance
of \(V\) under the finite exponential weighting.  Any random variable of
oscillation at most \(R\) has variance at most \(R^2/4\). `square`

### Corollary 16.5: Current-Corpus Closure Standard

For the rest of Paper 31, a route is called:

1. **proved** if the paper proves the required finite identity or
   implication;
2. **conditionally closed** if the paper proves exactly which primitive
   same-law theorem would finish it;
3. **falsified as a current-corpus derivation** if Theorem 16.1 and the
   imported Papers 20--30 do not determine the needed quantitative input,
   and Proposition 16.2 supplies finite same-identity models with different
   response values.

This is not the same as saying the mathematical theorem is false in actual
Yang-Mills.  It says the theorem is not derivable from the current corpus.

## 17. Closure Of The Heat-Bad Source Route

The first live target from Section 13 was
$$
\mathrm{P31\text{-}HKBAD\text{-}SRC\text{-}NEUT}(a,\rho)
\quad+\quad
\mathrm{P31\text{-}HKBAD\text{-}SRC\text{-}CURV}(a,\chi).
$$

### Lemma 17.1: Exact Odd Symmetry Would Prove Heat-Bad Neutrality

Suppose there is a measure-preserving involution
$$
\mathcal I:\Omega_{N,j}^{act}\to\Omega_{N,j}^{act}
$$
such that for every heat-bad dual probe \(Q\in{\mathcal Q}_{HB}\),
$$
V_Q^{HB,N,j}(\mathcal I\omega)=-V_Q^{HB,N,j}(\omega).
$$
Then
$$
\Psi_Q^{HB,N,j}(a)=\Psi_Q^{HB,N,j}(-a),
$$
so `P31-HKBAD-SRC-NEUT(a,0)` holds.

Proof.

Measure preservation gives
$$
\mathbf E^{act}e^{aV_Q}
=
\mathbf E^{act}e^{aV_Q\circ\mathcal I}
=
\mathbf E^{act}e^{-aV_Q}.
$$
Taking logarithms gives the claim. `square`

### Lemma 17.2: Exact Heat-Bad Odd Symmetry Is Not In The Current Corpus

Papers 20--30 do not prove the involution required by Lemma 17.1 for the
heat-bad family.

Proof.

Paper 30 separates bare signed parity from weighted heat-bad cancellation.
The heat-bad object contains the projected weighted matrix
$$
P_{\Gamma,bad}^{HK}(\delta)
\left(
D_\Gamma R_\Gamma\Sigma_\Gamma
+
U_\Gamma^*D_\Gamma R_\Gamma\Sigma_\Gamma U_\Gamma
\right),
$$
where the heat-bad projector, residual/Jacobian factor, and source matrix
need not change sign together under the known conjugation/orientation
symmetries.  Paper 30 explicitly leaves the weighted oddness theorem
`P30-HKBAD-WODD` unsourced.  Therefore the stronger exact involution of
Lemma 17.1 is not in the current corpus. `square`

### Lemma 17.3: Heat-Bad Curvature Is Only Trivially Bounded

The current corpus proves only the finite boundedness curvature estimate
obtained from Lemma 16.4 for the heat-bad source family.  It does not prove a
closing estimate for \(\chi\).

Proof.

The heat-bad probes are finite actual-record functionals, so boundedness at
fixed \((N,j)\) follows from the finite regularized construction.  This gives
some finite oscillation bound.  Papers 20--30 do not prove a cofinal
small-variance, log-Sobolev, Ward-cancellation, or Peter-Weyl tail estimate
for \(V_Q^{HB,N,j}\) uniformly over \(Q\in{\mathcal Q}_{HB}\).  Thus the only
available curvature control is the non-closing oscillation bound of Lemma
16.4. `square`

### Theorem 17.4: Heat-Bad Source Route Is Fully Reduced

The heat-bad source route is conditionally closed and falsified as a
current-corpus derivation.

More precisely:

1. if Lemma 17.1's odd involution or an equivalent near-evenness theorem is
   proved, heat-bad neutrality is sourced;
2. if a cofinal small curvature theorem is proved, heat-bad curvature is
   sourced;
3. without one of those new same-law theorems, the current corpus does not
   prove `P31-HKBAD-SRC-NEUT + P31-HKBAD-SRC-CURV` in a closing range.

Proof.

The conditional implication is Theorem 4.2.  Lemmas 17.2 and 17.3 prove that
the required primitive inputs are not contained in Papers 20--30.  Proposition
16.2 shows that a source derivative representation alone cannot force the
needed smallness. `square`

## 18. Closure Of The Low-Mode Source Gap Route

The low-mode route asks for
$$
\sup_{e,\zeta,x,y}
\partial_s\Psi_{x,y}^{LM,N,j}(0)
<
\theta_{\mathrm{crit}}-\kappa^{act}[L].
$$

### Lemma 18.1: Low-Mode Source Gap Is Exactly The Low-Mode Norm Gap

For the actual finite low-mode transfer operator,
$$
\sup_{\|x\|=\|y\|=1}
\partial_s\Psi_{x,y}^{LM,N,j}(0)
=
\left\|
\Pi_{\le L}T_{e,\zeta,\circ}^{N,j}\Pi_{\le L}
\right\|_{op}.
$$

Proof.

This is Lemma 5.2. `square`

### Proposition 18.2: Source Neutrality Would Be Stronger Than Needed

If the low-mode dual source family obeys
$$
\mathrm{P31\text{-}SRC\text{-}NEUT}(a,\rho;{\mathcal Q}_{LM})
\quad+\quad
\mathrm{P31\text{-}SRC\text{-}CURV}(a,\chi;{\mathcal Q}_{LM}),
$$
and
$$
{\rho\over a}+{\chi a\over2}
<
\theta_{\mathrm{crit}}-\kappa^{act}[L],
$$
then the low-mode gap closes.

Proof.

Apply Lemma 3.3 to the low-mode dual family and then Lemma 18.1. `square`

### Theorem 18.3: Low-Mode Source Gap Is Not Proved By The Current Corpus

The low-mode source route is conditionally closed and falsified as a
current-corpus derivation.

Proof.

Papers 28--29 define the actual low-mode conditional transfer matrix and
isolate the need for its entries or a strict spectral bound.  They also prove
that finite projected labels do not populate the missing same-law values.
Paper 31 rewrites each low-mode dual entry as a source derivative, but Lemma
18.1 shows this is exactly the operator norm being sought.  No current paper
proves a uniform low-mode source-neutrality, source-curvature, Ward, or
contractive theorem. `square`

## 19. Closure Of RN-MIXAMP And Bridge Mixed-Source Routes

The RN-MIXAMP source route asks for mixed endpoint derivatives that control
the doubly centered residual amplitude.

### Lemma 19.1: Mixed Source Derivatives Remove Endpoint Additive Terms

If
$$
R(u,v)=r_1(u)+r_2(v)+c+R_{dc}(u,v),
$$
where \(R_{dc}\) is doubly centered, then
$$
\partial_u\partial_vR(u,v)
=
\partial_u\partial_vR_{dc}(u,v).
$$

Proof.

Differentiate once in each endpoint variable. `square`

### Proposition 19.2: A Mixed Ward Identity Would Close The Route

Suppose the actual adaptive law satisfies a same-law identity of the form
$$
\partial_s\partial_t\Psi_{RN}^{N,j}(0,0)
=
\mathbf E^{act}[\mathcal E_{Ward}^{N,j}],
$$
where the Ward error obeys a cofinal bound inside the Paper-27 RN-MIXAMP
budget.  Then the RN-MIXAMP mixed-source route closes.

Proof.

Lemma 19.1 identifies the mixed derivative with the doubly centered part
seen by RN-MIXAMP.  The assumed Ward estimate bounds that part in the
correct ledger. `square`

### Theorem 19.3: Mixed-Source RN-MIXAMP Is Fully Reduced

The mixed-source route is conditionally closed and falsified as a
current-corpus derivation.

Proof.

Papers 26--27 prove that RN-MIXAMP smallness requires actual same-law
mixed-amplitude values, a spectral/tail theorem, a direct domination theorem,
or a lower floor.  Paper 31 replaces the mixed value by a mixed source
derivative.  Lemma 19.1 is a real simplification because endpoint-additive
pieces disappear.  But no current paper proves the needed mixed Ward
identity, mixed curvature estimate, or numerical mixed derivative bound for
the actual adaptive law.  Therefore the route is reduced to a new same-law
mixed-response theorem. `square`

## 20. Closure Of Primitive Residual Atom Sources

Primitive residual atom values were the earliest hard obstruction in Paper
29.  Paper 31 asks whether they become easier as source slopes.

### Lemma 20.1: Primitive Atom Source Slopes Are Exactly Atom Values

For every retained primitive atom \(h_A^{N,j}\),
$$
\partial_s\Psi_A^{prim,N,j}(0)
=
\mathbf E_{N,j}^{act}[h_A^{N,j}].
$$

Proof.

This is Definition 7.1. `square`

### Proposition 20.2: No Atom Value Is Generated By Source Formalism Alone

The source expression in Lemma 20.1 does not determine
\(\mathbf E^{act}[h_A]\) from finite labels, RN-MIXAMP ratios, or canonical
templates.

Proof.

Paper 29 proves that the primitive residual atom values are not determined
by the available finite label data.  Lemma 20.1 is an identity, not an
additional relation.  Proposition 16.2 gives finite source models with the
same formal derivative calculus and arbitrary first slope. `square`

### Theorem 20.3: Primitive Residual Source Route Is Closed Negative

The primitive atom route is closed negatively at the current-corpus level:
source slopes are exact, but they are exactly the missing atom values.  A
positive closure would require one of:

1. atom source neutrality and curvature;
2. a Ward identity forcing the atom slope to vanish or be small;
3. connected-cumulant decay covering the atom family;
4. Peter-Weyl tail domination of omitted atoms;
5. a sign-coherent atom floor.

None of these is proved in Papers 20--30. `square`

## 21. Closure Of The Dobrushin Source Route

Dobrushin rows are finite boundary variation suprema.  Source mixed
derivatives are infinitesimal.

### Lemma 21.1: Linear Response Is Necessary

If a finite Dobrushin row obeys a cofinal bound \(q<1\), then every
corresponding infinitesimal mixed source response is bounded by that row.

Proof.

Differentiate the finite boundary variation estimate at zero along any
admissible boundary source direction. `square`

### Lemma 21.2: Linear Response Is Not Sufficient In General

A bound on
$$
\partial_s\partial_t\Psi(0,0)
$$
does not imply a finite Dobrushin row bound without a uniform curvature or
convexity estimate along the boundary-source segment.

Proof.

Finite variation is controlled by integrating the derivative along a path in
boundary-source space.  A bound only at the origin supplies no control away
from the origin.  One may modify a finite moment generating function away
from zero while preserving its first mixed derivative at zero, so the finite
variation can be large. `square`

### Proposition 21.3: Curvature Upgrade Would Close Dobrushin

If the boundary/interior source family satisfies:

1. a cofinal infinitesimal row bound \(q_0<1\);
2. a cofinal curvature bound along every admissible boundary-source segment
   with total integrated error \(\epsilon\);
3. \(q_0+\epsilon<1\);

then the full Dobrushin row closes.

Proof.

Integrate the derivative of the conditional expectation along the boundary
source path.  The infinitesimal row supplies the origin term, and the
curvature bound controls the displacement along the path. `square`

### Theorem 21.4: Dobrushin Source Route Is Fully Reduced

The Dobrushin source route is conditionally closed and falsified as a
current-corpus derivation.

Proof.

Lemma 21.1 proves that Dobrushin smallness would imply source smallness.
Lemma 21.2 proves that the reverse implication needs a new nonlinear
curvature upgrade.  Papers 25--30 do not prove such an upgrade for the actual
adaptive law. `square`

## 22. Closure Of Defect KP And Mobius Source Cumulants

The connected-source route tries to replace atom recovery by cumulant decay.

### Lemma 22.1: Connected Activities Are Exactly Cumulants

For local defect probes \(\{F_x\}_{x\in A}\),
$$
\left.
\prod_{x\in A}\partial_{s_x}
\log\mathbf E^{act}
\exp\left\{\sum_{x\in A}s_xF_x\right\}
\right|_{\mathbf s=0}
=
\kappa^{act}(\{F_x\}_{x\in A}).
$$

Proof.

This is the standard cumulant identity from Theorem 16.1. `square`

### Proposition 22.2: KP Closure Requires Connected Decay

If
$$
\sum_{A\ni x}
e^{a|A|}
\left|
\kappa^{act}(\{F_y\}_{y\in A})
\right|
\le a_x
$$
with the Paper-29/Paper-30 KP weights, then the corresponding source-KP
route closes.

Proof.

This is Corollary 9.3 with the source derivative replaced by the equal
actual cumulant. `square`

### Theorem 22.3: Connected-Source KP Is Fully Reduced

The connected-source KP route is conditionally closed and falsified as a
current-corpus derivation.

Proof.

The source calculus proves that defect activities are cumulants.  It does
not prove exponential connected decay of those cumulants.  Such decay is
essentially the same type of same-law quantitative information as the
screened conditional influence theorem pursued in Papers 25--30.  The
current corpus supplies no cofinal connected-cumulant estimate in the
closing KP weights. `square`

## 23. Closure Of Peter-Weyl Source Tails

The Peter-Weyl route asks for source derivative summability over high
representations.

### Lemma 23.1: Fourier Source Slopes Are Exactly Peter-Weyl Coefficients

For each deterministic matrix-coefficient probe \(D_{\lambda,mn}\),
$$
\partial_s\Psi_{\lambda,mn}^{PW}(0)
=
\mathbf E^{act}[D_{\lambda,mn}]
=
c_{\lambda,mn}.
$$

Proof.

This is Definition 10.1. `square`

### Proposition 23.2: Tail Decay Needs Same-Law Regularity

A bound of the form
$$
\sum_{\lambda:\ C_2(\lambda)>L}
d_\lambda^p
\sup_{m,n}|c_{\lambda,mn}|
\le Ae^{-cL}
$$
requires same-law regularity, smoothing, analytic continuation, a finite-band
theorem, or an equivalent source-tail theorem for the actual residual
observable.

Proof.

Peter-Weyl summability is a regularity statement.  The coefficient identity
in Lemma 23.1 supplies the coefficients but not their decay.  Papers 28--30
explicitly separate finite low-mode data from the omitted tail and do not
prove finite-band support or cofinal decay for the actual adaptive law.
`square`

### Theorem 23.3: Peter-Weyl Source Tail Is Closed Negative

The Peter-Weyl source-tail route is closed negatively at the current-corpus
level.  The source calculus identifies the coefficients exactly, but the
decay theorem remains a primitive same-law regularity theorem.

## 24. Closure Of Source Floors

If smallness fails, a lower floor can still be valuable because it falsifies
Branch A cleanly.

### Lemma 24.1: Source Floors Are Actual Lower Floors

If there is a deterministic cofinal source choice \(Q_{N,j}\) such that
$$
\liminf_{(N,j)}
\left|
\partial_s\Psi_{Q_{N,j}}^{N,j}(0)
\right|
\ge M_*,
$$
then the corresponding actual retained functional has lower floor \(M_*\).

Proof.

The source derivative at zero is the actual expectation of the retained
functional. `square`

### Proposition 24.2: Floors Require Sign Coherence

A useful source floor requires a sign, orientation, normalization, and
retained-row convention that survive the cofinal limit.  Absolute size alone
is not enough if signs oscillate across retained rows or cofinal selectors.

Proof.

The floor must exceed the Branch-A budget in the same ledger where the upper
smallness theorem would be used.  If signs or normalizations drift, the
source slope is not a lower bound on that ledger. `square`

### Theorem 24.3: Source-Floor Route Is Fully Reduced

The floor route is conditionally closed and falsified as a current-corpus
derivation.

Proof.

Lemma 24.1 proves exact equivalence.  Proposition 24.2 states the missing
coherence requirement.  Papers 27--30 repeatedly isolate lower floors as
valid exits but do not prove a sign-coherent floor above the Branch-A budget.
`square`

## 25. Exhaustive Paper-31 Route Table

The routes opened by Paper 31 now have the following status.

| route | identity proved? | positive primitive needed | current-corpus status |
|---|---:|---|---|
| heat-bad absolute debit | yes | odd/near-even source symmetry or small curvature | conditionally closed; not proved |
| low-mode spectral gap | yes | uniform low-mode source response gap | conditionally closed; not proved |
| RN-MIXAMP mixed row | yes | mixed Ward/curvature/smallness theorem | conditionally closed; not proved |
| primitive residual atoms | yes | atom value, atom Ward, atom cumulant decay, or tail | closed negative |
| Dobrushin row | infinitesimal yes | nonlinear curvature upgrade | conditionally closed; not proved |
| defect KP/Mobius | yes | connected cumulant decay in KP weights | conditionally closed; not proved |
| Peter-Weyl tail | yes | same-law regularity/tail theorem | closed negative |
| lower floor | yes | sign-coherent cofinal floor witness | conditionally closed; not proved |

Here "not proved" means not proved by the current corpus, not false in the
actual Yang-Mills law.

## 26. Final Paper-31 Theorem

### Theorem 26.1: Source-Response Calculus Is Complete And Non-Closing

Paper 31 completely settles the source-response reframing opened by Paper
30:

1. every missing value obstruction in the Paper-26--30 Branch-A chain has an
   exact finite same-law source derivative representation;
2. the heat-bad absolute debit, low-mode norm, RN-MIXAMP mixed row,
   primitive atom value, Dobrushin infinitesimal row, defect cumulant,
   Peter-Weyl coefficient, and floor witness have all been mapped to source
   derivatives at \(s=0\);
3. the source formalism is Barandes-aligned because it uses no Markov
   factorization and no off-law measure;
4. the source formalism does not by itself imply smallness, tail decay,
   finite Dobrushin contraction, or a lower floor;
5. each positive route has been reduced to a named primitive same-law
   analytic theorem.

Proof.

Items 1 and 2 are Theorem 16.1 and Sections 17--24.  Item 3 is Proposition
15.5.  Item 4 is Proposition 16.2 together with the route-specific no-go
lemmas.  Item 5 is the exhaustive table in Section 25. `square`

### Corollary 26.2: Paper 31 Is Finished

The source-response idea is no longer an open menu.  It is closed as a
calculus:

$$
\boxed{
\text{source-response gives exact reformulations, not free confinement.}
}
$$

The next theorem must be one of the primitive same-law analytic inputs:

1. heat-bad source neutrality/curvature;
2. low-mode source response gap;
3. mixed RN-MIXAMP Ward/curvature control;
4. nonlinear source-Dobrushin upgrade;
5. connected source-cumulant decay;
6. same-law Peter-Weyl regularity/tail;
7. sign-coherent lower floor.

Further rearrangement of source derivatives inside Paper 31 will not move
the obstruction.  The next paper should choose one primitive input and attack
it directly.
