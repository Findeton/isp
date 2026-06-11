# Relativistic ISP V4 Paper 12: Residual Source Ward-Stein Four-Route Decision

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed finite residual-source investigation of the four primitive
Paper-11 actual-law routes, including the Einstein-style finite
Bianchi-Hodge principle-stack audit and the Paper-7 residual-complex
instantiation test.

## Abstract

Paper 11 reduces the actual-law selection problem to four primitive finite
same-law targets:

$$
\boxed{
\begin{gathered}
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}RN\text{-}DEFECT},\\
\mathrm{V4P11\text{-}SHORT\text{-}FISHER\text{-}PACKET\text{-}BRIDGE},\\
\mathrm{V4P11\text{-}ACTUAL\text{-}MOMENT\text{-}TIGHTNESS},\\
\mathrm{V4P11\text{-}ACTUAL\text{-}HIGH\text{-}PROB\text{-}FLOOR}.
\end{gathered}
}
$$

Paper 12 investigates all four routes from a common first-principles
viewpoint:

$$
\boxed{
\hbox{probe the actual finite law by finite residual sources.}
}
$$

The central finite object is the residual-source response function

$$
\Psi_a(J)
:=
\log\mathbb E_a^{act}
\exp\langle J,{\mathcal R}_a(Q_a)\rangle,
$$

where \({\mathcal R}_a\) is the Paper-7/Paper-8 residual vector and

$$
{\mathcal A}_a=\|{\mathcal R}_a\|^2.
$$

The main result is an honest four-route decision:

1. a residual-source Ward identity by itself centers the residual but does
   not control the residual variance;
2. a residual-source curvature bound or Stein coercivity estimate would
   prove the moment/tightness route;
3. an information-projection theorem would prove the RN route, but only if
   the actual law is characterized by the same finite constraints as the
   good reference law;
4. a Fisher route is exactly Hellinger closeness and can only be sourced by
   a genuine finite response contraction;
5. a high-probability floor is exactly a finite linear-programming/Farkas
   certificate against residual-small mass.

The Einstein-style continuation then asks whether a finite analogue of
covariance plus Bianchi identity can source the missing coercivity.  The
answer is conditional and sharp: finite covariance gives Ward identities,
finite Bianchi/Jacobi structure gives closedness, but residual smallness
requires a finite Hodge gap and control of harmonic residual modes.

Thus Paper 12 does not claim that the actual finite law is already solved.
It does something narrower and sharper: it proves what a non-bookkeeping
same-law theorem must look like, gives finite positive theorems for each
route, proves no-free-lunch obstructions for each route, and identifies the
best next positive primitive package:

$$
\boxed{
\mathrm{V4P12\text{-}FINITE\text{-}BIANCHI\text{-}HODGE\text{-}COERCIVITY}.
}
$$

This is the most promising positive target because it attacks the actual
residual moment directly through finite covariance, Bianchi/Ward structure,
and a coercive Hodge estimate, without inventing a comparison law and without
requiring an actual-to-good statistical closeness theorem first.

The residual Stein theorem remains the analytic expression of this package:
finite Bianchi-Hodge coercivity is the structured way to try to prove
residual-source Stein coercivity.

## 0. Imports And Barandes Discipline

### Import 0.1: Actual Finite Law

From Paper 11, let

$$
\mathbb P_a^{act}
$$

be the actual finite probability law on the total finite record space
\(\Omega_a\).  Let

$$
Q_a\sim\mathbb P_a^{act}.
$$

### Import 0.2: Residual Vector And Penalty

Let \(V_a\) be the finite residual-vector space containing the finite
constraint-algebra and covariance residuals.  The residual map is

$$
{\mathcal R}_a:\Omega_a\to V_a.
$$

The residual penalty is

$$
{\mathcal A}_a(q)
:=
\|{\mathcal R}_a(q)\|^2.
$$

In Paper-8/Paper-11 notation this expands as

$$
{\mathcal A}_a(q)
=
\sum_{DD}\|R_{DD,a}^q\|^2
+\sum_{DH}\|R_{DH,a}^q\|^2
+\sum_{HH}\|R_{HH,a}^q\|^2
+\|{\mathcal E}_{cov,a}^q\|^2.
$$

### Import 0.3: Good Configurations

Paper 11 defines

$$
{\mathsf G}_a(\epsilon)
:=
\{q:\Pi_a(q)\in{\mathsf GoodPkt}_a(\epsilon)
\hbox{ and }{\mathcal A}_a(q)\le\epsilon\}.
$$

The positive actual-law target is

$$
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1,
\qquad
\epsilon_a\downarrow0.
$$

### Barandes Rule 0.4

Paper 12 may use only:

1. finite record spaces;
2. finite probability laws;
3. finite source tilts of those laws;
4. finite Radon-Nikodym, entropy, Hellinger, Fisher, and linear-programming
   identities;
5. finite comparison maps that act on record labels.

Paper 12 may not use:

1. Einstein equations as primitive dynamics;
2. continuum path integrals as measures over histories;
3. hidden Markov substeps inside an indivisible whole-slab law;
4. Hilbert-space phase as ontology;
5. a declared residual-small law as a substitute for the actual law.

The rule is:

$$
\boxed{
\hbox{any primitive theorem must be a theorem about }\mathbb P_a^{act}.
}
$$

## 1. Residual-Source Response

### Definition 1.1: Residual-Source Tilt

For \(J\in V_a^*\), define the residual-source partition function

$$
Z_a(J)
:=
\mathbb E_a^{act}
\exp\langle J,{\mathcal R}_a(Q_a)\rangle.
$$

Define

$$
\Psi_a(J):=\log Z_a(J).
$$

When \(Z_a(J)<\infty\), which is automatic on the finite space
\(\Omega_a\), define the tilted law

$$
\mathbb P_{a,J}(q)
:=
\frac{
\mathbb P_a^{act}(q)
\exp\langle J,{\mathcal R}_a(q)\rangle
}{Z_a(J)}.
$$

### Proposition 1.2: Source Derivatives Are Actual Residual Cumulants

For \(u,v\in V_a^*\),

$$
D_u\Psi_a(0)
=
\mathbb E_a^{act}\langle u,{\mathcal R}_a\rangle,
$$

and

$$
D_uD_v\Psi_a(0)
=
\mathrm{Cov}_a^{act}
\bigl(\langle u,{\mathcal R}_a\rangle,
\langle v,{\mathcal R}_a\rangle\bigr).
$$

If \(\{e_i\}\) is an orthonormal basis of \(V_a\) and \(\{e_i^*\}\) is the
dual basis, then

$$
\mathbb E_a^{act}[{\mathcal A}_a]
=
\sum_i
\left(D_{e_i^*}D_{e_i^*}\Psi_a(0)
+D_{e_i^*}\Psi_a(0)^2\right).
$$

Proof.

Differentiate the finite sum defining \(Z_a(J)\), then differentiate
\(\log Z_a(J)\).  The last identity is the variance plus mean-square
decomposition of \(\mathbb E\|{\mathcal R}_a\|^2\).  `square`

### Corollary 1.3: Residual Moment Is Source Curvature

The moment route is equivalent to proving:

$$
\sum_i D_{e_i^*}D_{e_i^*}\Psi_a(0)\to0
$$

and

$$
\sum_i D_{e_i^*}\Psi_a(0)^2\to0.
$$

Proof.

Immediate from Proposition 1.2.  `square`

### Verdict 1.4

This is the first useful change of viewpoint.  The difficult quantity

$$
\mathbb E_a^{act}[{\mathcal A}_a]
$$

is not an opaque average anymore.  It is the trace of the finite
residual-source Hessian plus the squared residual-source gradient at zero.

But this identity alone is not an estimate.  The next question is whether a
finite symmetry, exchange rule, or Stein identity forces that gradient and
Hessian to be small.

## 2. Route I: Moment/Tightness By Residual-Source Ward Or Stein Coercivity

This is the preferred positive route because it attacks the residual moment
under the actual law directly.

### Definition 2.1: Residual-Source Ward Centering

The actual law satisfies residual-source Ward centering at scale \(\eta_a\)
if

$$
\left\|
\mathbb E_a^{act}[{\mathcal R}_a]
\right\|
\le
\eta_a.
$$

Equivalently,

$$
\sup_{\|u\|_*\le1}
\left|D_u\Psi_a(0)\right|
\le
\eta_a.
$$

### Proposition 2.2: Centering Alone Does Not Prove Moment Decay

There are finite actual laws with exact residual-source Ward centering but
with residual moment bounded away from zero.

Proof.

Let \(V_a=\mathbb R\), \(\Omega_a=\{-1,+1\}\), and
\({\mathcal R}_a(q)=q\).  Let \(\mathbb P_a^{act}(-1)=
\mathbb P_a^{act}(+1)=1/2\).  Then

$$
\mathbb E[{\mathcal R}_a]=0,
$$

but

$$
\mathbb E[{\mathcal A}_a]
=
\mathbb E[{\mathcal R}_a^2]
=1.
$$

Thus Ward centering controls the source gradient but not the source
curvature.  `square`

### Definition 2.3: Residual-Source Curvature Bound

The actual law satisfies residual-source curvature smallness at scale
\(\kappa_a\) if

$$
\operatorname{Tr}_{V_a}
\operatorname{Hess}\Psi_a(0)
:=
\sum_iD_{e_i^*}D_{e_i^*}\Psi_a(0)
\le
\kappa_a
$$

for an orthonormal residual basis.

### Theorem 2.4: Source Gradient Plus Curvature Proves Moment Route

If residual-source Ward centering holds with \(\eta_a\to0\) and
residual-source curvature smallness holds with \(\kappa_a\to0\), then

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

If, in addition, regularity tightness and uniform residual integrability hold
as in Paper 11, then

$$
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1
$$

for some \(\epsilon_a\downarrow0\).

Proof.

By Proposition 1.2,

$$
\mathbb E_a^{act}[{\mathcal A}_a]
=
\operatorname{Tr}\operatorname{Hess}\Psi_a(0)
+\|\mathbb E_a^{act}{\mathcal R}_a\|^2
\le
\kappa_a+\eta_a^2.
$$

The second assertion is Paper 11 Theorem 13.12.  `square`

### Definition 2.5: Finite Stein Pair For Residuals

A finite Stein pair for \({\mathcal R}_a\) consists of:

1. a finite comparison graph \(G_a=(\Omega_a,E_a)\);
2. antisymmetric edge currents \(J_e(q,q')=-J_e(q',q)\);
3. a finite difference operator

   $$
   \nabla_e f(q,q'):=f(q')-f(q);
   $$

4. residual potentials \(\Phi_{a,i}\) for each residual coordinate
   \({\mathcal R}_{a,i}\);
5. a defect vector \(B_a(q)\);

such that, for every test function \(f:\Omega_a\to\mathbb R\),

$$
\mathbb E_a^{act}
\left[
{\mathcal R}_{a,i} f
\right]
=
\mathbb E_a^{act}
\left[
\sum_{e}J_{e,i}\nabla_e f
\right]
+
\mathbb E_a^{act}[B_{a,i}f].
$$

The identity is Barandes-aligned when \(G_a\), \(J_e\), \(\Phi_{a,i}\), and
\(B_a\) are finite record-level objects.

### Definition 2.6: Stein Coercivity

The Stein pair is coercive at scales \((\alpha_a,\beta_a)\) if

$$
\mathbb E_a^{act}
\left[
\sum_i\left(\sum_e J_{e,i}\nabla_e f_i\right)^2
\right]
\le
\alpha_a
\mathbb E_a^{act}
\left[\sum_i f_i^2\right]
$$

for all finite vector tests \(f=(f_i)\), and

$$
\mathbb E_a^{act}\|B_a\|^2\le\beta_a.
$$

### Theorem 2.7: Residual Stein Coercivity Implies Moment Decay

Assume a finite Stein pair exists.  If it is coercive with

$$
\alpha_a\to0,
\qquad
\beta_a\to0,
$$

then

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

Proof.

Apply the Stein identity with \(f_i={\mathcal R}_{a,i}\) and sum over \(i\):

$$
\mathbb E\|{\mathcal R}_a\|^2
=
\mathbb E
\left[
\sum_i\sum_eJ_{e,i}\nabla_e{\mathcal R}_{a,i}
\right]
+
\mathbb E\langle B_a,{\mathcal R}_a\rangle.
$$

By Cauchy-Schwarz and the coercivity hypothesis,

$$
\left|
\mathbb E
\sum_i\sum_eJ_{e,i}\nabla_e{\mathcal R}_{a,i}
\right|
\le
\sqrt{\alpha_a}
\sqrt{\mathbb E\|{\mathcal R}_a\|^2}.
$$

Also,

$$
\left|
\mathbb E\langle B_a,{\mathcal R}_a\rangle
\right|
\le
\sqrt{\beta_a}
\sqrt{\mathbb E\|{\mathcal R}_a\|^2}.
$$

Let

$$
X_a:=\sqrt{\mathbb E\|{\mathcal R}_a\|^2}.
$$

Then

$$
X_a^2\le(\sqrt{\alpha_a}+\sqrt{\beta_a})X_a.
$$

Hence

$$
X_a\le\sqrt{\alpha_a}+\sqrt{\beta_a},
$$

and the residual moment tends to zero.  `square`

### Proposition 2.8: Stein Coercivity Is Not In The Current Corpus

The current V4 corpus does not prove the existence of a finite residual
Stein pair with \(\alpha_a,\beta_a\to0\).

Proof.

Papers 4-7 define finite source-response and residual objects.  Papers 8-11
define residual penalties, conditioned sectors, actual laws, and transfer
mechanisms.  None of those papers constructs finite comparison currents
whose integration-by-parts identity returns the residual vector itself, and
none proves the coercivity estimate of Definition 2.6.  `square`

### Verdict 2.9: Moment Route

The moment route has a real positive theorem:

$$
\boxed{
\mathrm{V4P12\text{-}RESIDUAL\text{-}SOURCE\text{-}STEIN\text{-}COERCIVITY}
\Longrightarrow
\mathrm{V4P11\text{-}ACTUAL\text{-}MOMENT\text{-}TIGHTNESS}.
}
$$

It also has a clear obstruction: centering/Ward identities alone do not
control residual variance.  The missing primitive is exactly a finite
curvature or Stein-coercivity estimate under \(\mathbb P_a^{act}\).

## 3. Route II: RN Defect By Information Projection

The RN route compares the actual law to the canonical good reference law
\(\pi_a^{good}\).  The danger is that \(\pi_a^{good}\) may be an invented
comparison object.  The only honest positive route is to prove that both
laws arise from the same finite constraint principle.

### Definition 3.1: Finite Constraint Class

Let \(F_{a,1},\ldots,F_{a,m_a}\) be finite observables on \(\Omega_a\), and
let \(c_{a,k}\) be finite target values.  Define the finite constraint class

$$
{\mathcal C}_a
:=
\left\{
P\in{\mathcal P}(\Omega_a):
\mathbb E_P[F_{a,k}]=c_{a,k}
\hbox{ for all }k
\right\}.
$$

### Definition 3.2: Same-Constraint I-Projection

Given a strictly positive finite base law \(\rho_a\), the I-projection of
\(\rho_a\) onto \({\mathcal C}_a\) is the law

$$
P_a^*
:=
\arg\min_{P\in{\mathcal C}_a}H(P\mid\rho_a),
$$

when it exists.

### Theorem 3.3: Finite I-Projection Form

If \({\mathcal C}_a\) is nonempty and contains a strictly positive law, then
the I-projection exists and has exponential-family form

$$
P_a^*(q)
=
\frac{
\rho_a(q)\exp\left(\sum_k\lambda_{a,k}F_{a,k}(q)\right)
}{
\sum_r\rho_a(r)\exp\left(\sum_k\lambda_{a,k}F_{a,k}(r)\right)
}
$$

for some finite multipliers \(\lambda_{a,k}\), up to redundant constraints.

Proof.

This is finite-dimensional convex optimization.  The entropy is strictly
convex on the positive simplex modulo redundant directions.  Lagrange
multipliers for the affine constraints give the displayed form.  `square`

### Theorem 3.4: RN Defect From Constraint Slack

Let \(\pi_a^{good}\) and \(\mathbb P_a^{act}\) be strictly positive finite
laws.  Suppose

$$
\pi_a^{good}(q)
=
\frac{\rho_a(q)e^{-S_a(q)}}{Z_a}
$$

and

$$
\mathbb P_a^{act}(q)
=
\frac{\rho_a(q)e^{-S_a(q)+E_a(q)}}{\widetilde Z_a},
$$

where \(S_a\) is the good residual score and \(E_a\) is a finite defect
observable.  Then

$$
\log\left\|
\frac{d\mathbb P_a^{act}}{d\pi_a^{good}}
\right\|_\infty
\le
\operatorname{osc}(E_a),
$$

where

$$
\operatorname{osc}(E_a):=\max_qE_a(q)-\min_qE_a(q).
$$

Also,

$$
H(\mathbb P_a^{act}\mid\pi_a^{good})
\le
\operatorname{osc}(E_a).
$$

Proof.

The log density ratio is

$$
\log\frac{d\mathbb P_a^{act}}{d\pi_a^{good}}(q)
=
E_a(q)-\log\mathbb E_{\pi_a^{good}}e^{E_a}.
$$

The normalizing term lies between \(\min E_a\) and \(\max E_a\), giving the
supremum bound.  The entropy is the expectation of the same log ratio under
\(\mathbb P_a^{act}\), hence is bounded by the same oscillation.  `square`

### Corollary 3.5: RN Route Positive Criterion

If \(\pi_a^{good}({\mathsf G}_a(\epsilon_a)^c)\le e^{-r_a}\) and the
actual law has the same finite exponential form as \(\pi_a^{good}\) up to a
defect \(E_a\) with

$$
\operatorname{osc}(E_a)=o(r_a),
$$

then

$$
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1.
$$

Proof.

Combine Theorem 3.4 with Paper 11 Corollary 13.5.  `square`

### Proposition 3.6: Same Constraints Are Essential

Without a constraint or exponential-form theorem relating
\(\mathbb P_a^{act}\) to \(\pi_a^{good}\), RN domination is false.

Proof.

Let \(B_a={\mathsf G}_a(\epsilon_a)^c\) and suppose
\(\pi_a^{good}(B_a)=e^{-r_a}\).  Define an actual law by conditioning mostly
on \(B_a\):

$$
\mathbb P_a^{act}
=
\frac12\pi_a^{good}(\cdot\mid B_a)
+
\frac12\pi_a^{good}(\cdot\mid B_a^c).
$$

Then \(\mathbb P_a^{act}(B_a)=1/2\), while the RN and entropy defects are
order \(r_a\) by Paper 11 Theorem 13.4.  All objects are finite and can be
made strictly positive by adding an arbitrarily small full-support collar.
`square`

### Proposition 3.7: Current-Corpus RN Status

The current corpus does not prove that \(\mathbb P_a^{act}\) is an
I-projection, maximum-entropy law, minimum-defect law, or exponential-family
perturbation of \(\pi_a^{good}\) with subcritical defect.

Proof.

Papers 6-11 allow many actual finite kernels with the same record alphabets
and packet maps.  No theorem in the corpus states that the actual law is
selected by the residual score \(S_a={\mathcal A}_a+\lambda_aK_a\), or by the
same finite constraints that define \(\pi_a^{good}\).  `square`

### Verdict 3.8: RN Route

The RN route is viable only if Paper 12 or a later paper proves:

$$
\boxed{
\mathrm{V4P12\text{-}ACTUAL\text{-}IPROJ\text{-}RN\text{-}DEFECT}.
}
$$

That theorem would say that the actual finite law is a same-constraint
information projection or subcritical exponential perturbation of the good
reference law.  Without such a theorem, RN domination is not merely missing;
it is unconstrained.

## 4. Route III: Fisher/Hellinger By Finite Response Contraction

The Fisher route is geometrically elegant but unforgiving.  Paper 11 proves
that a short Fisher bridge is exactly Hellinger closeness.

### Definition 4.1: Good-Law Hellinger Gap

Let

$$
H_a^2(P,Q)
:=
1-\operatorname{Aff}(P,Q)
$$

be the squared Hellinger gap under the Paper-11 convention.

The Fisher route requires

$$
H_a^2(\mathbb P_a^{act},\pi_a^{good})\to0.
$$

### Theorem 4.2: Response Contraction Implies Fisher Route

Suppose there is a finite source flow \(t\mapsto P_{a,t}\) on
\({\mathcal P}(\Omega_a)\) with

$$
P_{a,0}=\mathbb P_a^{act},
\qquad
P_{a,T_a}=\pi_a^{good},
$$

and Fisher speed

$$
I_a(t)
:=
\mathbb E_{a,t}
\left[
\left(\partial_t\log P_{a,t}\right)^2
\right].
$$

If

$$
\int_0^{T_a}\sqrt{I_a(t)}\,dt\to0,
$$

then

$$
H_a^2(\mathbb P_a^{act},\pi_a^{good})\to0
$$

and hence the Paper-11 Fisher route proves actual good-configuration
concentration whenever \(\pi_a^{good}\) is good.

Proof.

This is Paper 11 Theorem 13.8 and Corollary 13.9.  `square`

### Proposition 4.3: A Source Path Alone Gives No Estimate

The mere existence of a finite source path between \(\mathbb P_a^{act}\) and
\(\pi_a^{good}\) gives no Fisher smallness.

Proof.

Every two strictly positive finite laws are connected by the mixture path

$$
P_t=(1-t)\mathbb P_a^{act}+t\pi_a^{good}.
$$

But the shortest Fisher length is

$$
2\arccos\operatorname{Aff}(\mathbb P_a^{act},\pi_a^{good}),
$$

which can be bounded away from zero.  Thus path existence is automatic and
irrelevant; only a small-length theorem matters.  `square`

### Definition 4.4: Fisher Residual Projection

Let \({\mathcal M}_a\) be a finite source-response model manifold containing
the actual law.  Let \({\mathcal N}_a\subset{\mathcal M}_a\) be the
good-residual submanifold.  A Fisher residual projection estimate at scale
\(\ell_a\) is

$$
d_{FR}(\mathbb P_a^{act},{\mathcal N}_a)
\le
\ell_a,
\qquad
\ell_a\to0.
$$

### Theorem 4.5: Fisher Projection Plus Good Model Proves The Route

If \({\mathcal N}_a\) contains a good law \(\pi_a^{good}\) with

$$
\pi_a^{good}({\mathsf G}_a(\epsilon_a)^c)\to0,
$$

and if

$$
d_{FR}(\mathbb P_a^{act},{\mathcal N}_a)\to0,
$$

then actual good-configuration concentration holds.

Proof.

Choose \(Q_a\in{\mathcal N}_a\) with

$$
d_{FR}(\mathbb P_a^{act},Q_a)\to0.
$$

Fisher-Rao distance controls total variation on finite spaces, so

$$
|\mathbb P_a^{act}(B_a)-Q_a(B_a)|\to0
$$

for \(B_a={\mathsf G}_a(\epsilon_a)^c\).  Since \(Q_a\) is good, the actual
bad probability tends to zero.  `square`

### Proposition 4.6: Current-Corpus Fisher Status

The current corpus does not prove a finite Fisher residual projection
estimate.

Proof.

Existing finite source-response calculus gives Fisher metrics and response
derivatives.  It does not prove that the actual law is at small Fisher-Rao
distance from any good-residual submanifold.  `square`

### Verdict 4.7: Fisher Route

The Fisher route is not wrong, but it is not easier than the moment route
unless a response-contraction theorem exists:

$$
\boxed{
\mathrm{V4P12\text{-}FISHER\text{-}RESIDUAL\text{-}PROJECTION}.
}
$$

This theorem would be a genuine same-law analytic input.  Without it, the
Fisher route restates the need for actual/good statistical closeness.

## 5. Route IV: High-Probability Floor By Finite Certificates

The floor route asks for a negative theorem:

$$
\mathbb P_a^{act}({\mathcal A}_a\ge\delta)\to1.
$$

This should not be guessed.  It should be decided by finite feasibility or
dual certificates.

### Definition 5.1: Residual-Small Event

For \(\delta>0\), define

$$
L_a(\delta):=\{q\in\Omega_a:{\mathcal A}_a(q)<\delta\}.
$$

The high-probability floor is equivalent to

$$
\mathbb P_a^{act}(L_a(\delta))\to0.
$$

### Definition 5.2: Finite Actual Constraint Relaxation

Let \({\mathcal K}_a\) be the finite convex set of laws satisfying all
current-corpus linear actual-law constraints known at regulator \(a\):

$$
{\mathcal K}_a
:=
\left\{
P\in{\mathcal P}(\Omega_a):
\mathbb E_P[F_{a,k}]=c_{a,k},
\quad
\mathbb E_P[G_{a,\ell}]\le d_{a,\ell}
\right\}.
$$

This is a relaxation unless the constraints characterize
\(\mathbb P_a^{act}\) exactly.

### Theorem 5.3: Finite LP Floor Certificate

Fix \(\delta>0\).  The bound

$$
\sup_{P\in{\mathcal K}_a}P(L_a(\delta))\le\varepsilon_a
$$

holds if and only if there exist finite multipliers
\(\alpha_k\in\mathbb R\), \(\beta_\ell\ge0\), and \(\gamma\in\mathbb R\)
such that, for every \(q\in\Omega_a\),

$$
{\bf 1}_{L_a(\delta)}(q)
\le
\gamma+\sum_k\alpha_kF_{a,k}(q)+\sum_\ell\beta_\ell G_{a,\ell}(q),
$$

and

$$
\gamma+\sum_k\alpha_kc_{a,k}+\sum_\ell\beta_\ell d_{a,\ell}
\le
\varepsilon_a.
$$

Proof.

This is finite linear-programming duality.  The primal maximizes the mass of
\(L_a(\delta)\) over the finite polytope \({\mathcal K}_a\).  The displayed
inequality is the dual domination certificate for the indicator of
\(L_a(\delta)\).  Strong duality holds for finite feasible polytopes.
`square`

### Corollary 5.4: Floor Certificate Proves Actual Floor

If \(\mathbb P_a^{act}\in{\mathcal K}_a\) and

$$
\sup_{P\in{\mathcal K}_a}P(L_a(\delta))\to0,
$$

then

$$
\mathbb P_a^{act}({\mathcal A}_a\ge\delta)\to1.
$$

Proof.

Since \(\mathbb P_a^{act}\in{\mathcal K}_a\),

$$
\mathbb P_a^{act}(L_a(\delta))
\le
\sup_{P\in{\mathcal K}_a}P(L_a(\delta)).
$$

The right side tends to zero.  `square`

### Proposition 5.5: Residual-Small Feasibility Falsifies A Floor From The
Current Constraints

If there exists \(P_a\in{\mathcal K}_a\) with

$$
P_a(L_a(\delta))\ge c>0
$$

along a subsequence, then the current constraint relaxation cannot prove a
high-probability floor at level \(\delta\).

Proof.

The supremum over \({\mathcal K}_a\) is at least \(c\), so the LP certificate
of Theorem 5.3 with \(\varepsilon_a\to0\) cannot exist.  `square`

### Proposition 5.6: Full-Support Actual Laws Usually Defeat Support Floors

If the actual law is strictly positive on a residual-small configuration,
then a direct support floor is false, even if a high-probability floor might
still hold.

Proof.

Strict positivity puts the residual-small point in the support.  A support
floor requires every support point to have residual bounded below.  But the
probability of that point may be exponentially small, so this does not by
itself rule out a high-probability floor.  `square`

### Verdict 5.7: Floor Route

The high-probability floor route is completely finite and decidable at each
regulator once \({\mathcal K}_a\), \({\mathcal A}_a\), and \(\Omega_a\) are
explicit.  The missing input is not conceptual.  It is an actual finite
constraint table strong enough to force

$$
\sup_{P\in{\mathcal K}_a}P({\mathcal A}_a<\delta)\to0.
$$

The route is therefore:

$$
\boxed{
\mathrm{V4P12\text{-}LP\text{-}FLOOR\text{-}CERTIFICATE}.
}
$$

The current corpus does not provide such a certificate.

## 6. Cross-Route Logic

The four routes are not independent.  The following finite implications are
useful for deciding what to try first.

### Proposition 6.1: Moment Route Excludes High-Probability Floor

If

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0,
$$

then no high-probability floor at any fixed \(\delta>0\) can hold.

Proof.

By Markov,

$$
\mathbb P_a^{act}({\mathcal A}_a\ge\delta)
\le
\delta^{-1}\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

`square`

### Proposition 6.2: High-Probability Floor Excludes Positive Routes

If for some \(\delta>0\),

$$
\mathbb P_a^{act}({\mathcal A}_a\ge\delta)\to1,
$$

then actual good-configuration concentration is impossible for every
\(\epsilon_a<\delta\) eventually.

Proof.

This is Paper 11 Proposition 13.16.  `square`

### Proposition 6.3: Fisher Closeness To A Good Moment Law Gives Moment
Closeness Under Bounded Residuals

Assume

$$
\operatorname{Aff}(\mathbb P_a^{act},\pi_a^{good})\to1,
$$

and suppose

$$
\sup_{q\in\Omega_a}{\mathcal A}_a(q)\le M_a
$$

with

$$
M_a\,
\|\mathbb P_a^{act}-\pi_a^{good}\|_{TV}\to0.
$$

If

$$
\mathbb E_{\pi_a^{good}}[{\mathcal A}_a]\to0,
$$

then

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

Proof.

The expectation difference is bounded by

$$
M_a\|\mathbb P_a^{act}-\pi_a^{good}\|_{TV}.
$$

Hellinger closeness implies total-variation closeness.  `square`

### Proposition 6.4: RN Defect Can Transfer Good Events Without Small Total
Variation

The entropy condition

$$
H(\mathbb P_a^{act}\mid\pi_a^{good})=o(r_a)
$$

with

$$
\pi_a^{good}(B_a)\le e^{-r_a}
$$

can force \(\mathbb P_a^{act}(B_a)\to0\) even if the entropy does not tend
to zero.

Proof.

Paper 11 Corollary 13.5 uses entropy small relative to \(r_a\), not
absolutely small.  Hence RN/entropy transfer is a large-deviation transfer,
whereas Fisher/Hellinger is a global closeness theorem.  `square`

### Verdict 6.5: Route Priority

The best order is:

1. try moment/tightness through residual-source curvature or Stein
   coercivity;
2. try RN only if a same-constraint information-projection principle appears;
3. try Fisher only if a real finite response-contraction theorem appears;
4. run the LP floor route as a falsification/negative certificate in
   parallel.

## 7. Exhaustive Route Table

| Route | Positive theorem in Paper 12 | No-free-lunch obstruction | Current-corpus status |
|---|---|---|---|
| Moment/tightness | residual-source gradient plus curvature, or Stein coercivity, gives \(\mathbb E{\mathcal A}_a\to0\) | Ward centering alone leaves variance uncontrolled | not sourced |
| RN defect | same-constraint I-projection or subcritical exponential defect transfers good concentration | arbitrary actual laws can put fixed mass on the bad event with order-\(r_a\) defect | not sourced |
| Fisher/Hellinger | finite response contraction/Fisher projection gives closeness to a good law | source path existence is automatic and gives no smallness | not sourced |
| High-probability floor | finite LP/Farkas certificate forces residual-small mass to zero | residual-small feasible laws falsify floor from current constraints | not sourced |

## 8. Current-Corpus Final Decision

### Theorem 8.1: Paper-12 Four-Route Decision

Within the current V4 corpus, none of the four primitive Paper-11 targets is
proved unconditionally:

$$
\boxed{
\begin{gathered}
\mathrm{V4P11\text{-}ACTUAL\text{-}PACKET\text{-}RN\text{-}DEFECT}^{cur}
\quad\hbox{not sourced},\\
\mathrm{V4P11\text{-}SHORT\text{-}FISHER\text{-}PACKET\text{-}BRIDGE}^{cur}
\quad\hbox{not sourced},\\
\mathrm{V4P11\text{-}ACTUAL\text{-}MOMENT\text{-}TIGHTNESS}^{cur}
\quad\hbox{not sourced},\\
\mathrm{V4P11\text{-}ACTUAL\text{-}HIGH\text{-}PROB\text{-}FLOOR}^{cur}
\quad\hbox{not sourced}.
\end{gathered}
}
$$

But each route is now reduced to a precise finite primitive:

$$
\boxed{
\begin{gathered}
\mathrm{V4P12\text{-}ACTUAL\text{-}IPROJ\text{-}RN\text{-}DEFECT},\\
\mathrm{V4P12\text{-}FISHER\text{-}RESIDUAL\text{-}PROJECTION},\\
\mathrm{V4P12\text{-}RESIDUAL\text{-}SOURCE\text{-}STEIN\text{-}COERCIVITY},\\
\mathrm{V4P12\text{-}LP\text{-}FLOOR\text{-}CERTIFICATE}.
\end{gathered}
}
$$

Proof.

The moment route is settled by Theorem 2.4, Theorem 2.7, Proposition 2.8,
and Verdict 2.9.  The RN route is settled by Theorems 3.3 and 3.4,
Corollary 3.5, Propositions 3.6 and 3.7, and Verdict 3.8.  The Fisher route
is settled by Theorem 4.2, Proposition 4.3, Theorem 4.5, Proposition 4.6,
and Verdict 4.7.  The high-probability floor route is settled by Theorem
5.3, Corollary 5.4, Propositions 5.5 and 5.6, and Verdict 5.7.  `square`

### Corollary 8.2: Best Next Primitive

Before imposing the Einstein-style finite Bianchi-Hodge stack of Section 10,
the best direct positive primitive is

$$
\boxed{
\mathrm{V4P12\text{-}RESIDUAL\text{-}SOURCE\text{-}STEIN\text{-}COERCIVITY}.
}
$$

Proof.

RN and Fisher routes require comparison to a good reference law.  Those
comparisons are powerful but first need a theorem identifying the actual law
with a constraint projection or a small Fisher neighborhood.  The moment
route instead asks for an estimate directly under \(\mathbb P_a^{act}\).
Among direct estimates, Ward centering is insufficient by Proposition 2.2,
so the first nontrivial positive target is curvature or Stein coercivity.
`square`

Section 10 refines this direct target into the more structured finite
Bianchi-Hodge package.

### Corollary 8.3: Best Negative Parallel Test

The best negative parallel test is

$$
\boxed{
\mathrm{V4P12\text{-}LP\text{-}FLOOR\text{-}CERTIFICATE}.
}
$$

Proof.

The high-probability floor is the real negative twin of actual good
concentration.  The LP/Farkas route is finite, explicit, and falsifiable at
each regulator once the actual constraint table is specified.  `square`

## 9. Concrete Next Work Program

Paper 12 leaves no structural route unexplored.  The next work should not
add more packet labels.  It should try to prove or falsify one of the
following finite primitive statements.

### Target 9.0: Finite Bianchi-Hodge Coercivity

Construct a finite residual complex

$$
C_a^0\xrightarrow{d_a}C_a^1\xrightarrow{D_a}C_a^2,
\qquad
D_ad_a=0,
$$

identify

$$
{\mathcal R}_a(q)\in C_a^1,
$$

and prove, under the actual law,

$$
\mathbb E_a^{act}\|D_a{\mathcal R}_a\|^2
+\mathbb E_a^{act}\|d_a^*{\mathcal R}_a\|^2
+\mathbb E_a^{act}
\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2
\to0
$$

with a uniform Hodge gap off \({\mathcal H}_a\).  This is the finite
Einstein-style route: Bianchi, conservation/codivergence, harmonic control,
and coercivity.

### Target 9.1: Residual Stein Coercivity

Construct finite comparison currents \(J_{e,i}\) and defects \(B_{a,i}\)
such that

$$
\mathbb E_a^{act}[{\mathcal R}_{a,i}f]
=
\mathbb E_a^{act}\left[\sum_eJ_{e,i}\nabla_ef\right]
+
\mathbb E_a^{act}[B_{a,i}f],
$$

with

$$
\alpha_a+\beta_a\to0.
$$

This would prove the positive moment route.

### Target 9.2: Residual Source Curvature

Prove directly that

$$
\|\nabla\Psi_a(0)\|^2+\operatorname{Tr}\operatorname{Hess}\Psi_a(0)\to0.
$$

This is equivalent to actual residual \(L^2\) decay.

### Target 9.3: Actual I-Projection

Find finite constraints \({\mathcal C}_a\) that genuinely characterize
\(\mathbb P_a^{act}\) and show that \(\pi_a^{good}\) is the same-constraint
I-projection up to a subcritical defect.

### Target 9.4: Fisher Residual Projection

Build a finite response model manifold \({\mathcal M}_a\), a good submanifold
\({\mathcal N}_a\), and prove

$$
d_{FR}(\mathbb P_a^{act},{\mathcal N}_a)\to0.
$$

### Target 9.5: LP Floor Certificate

Write the current actual-law constraints as a finite polytope
\({\mathcal K}_a\), then solve or symbolically dualize:

$$
\sup_{P\in{\mathcal K}_a}P({\mathcal A}_a<\delta).
$$

If this tends to zero, V4 has a negative floor theorem.  If it stays bounded
below, the current constraints cannot prove the floor.

## 10. Einstein-Style Finite Bianchi-Hodge Principle Stack

The Einstein lesson is not "guess the right estimate."  It is to find a
principle stack that makes the estimate almost forced.  In GR the relevant
stack is equivalence, covariance, Bianchi identity, stress conservation, and
the Newtonian/known-physics limit.  The finite ISP analogue must be stated
without importing continuum Einstein equations.

The candidate stack is:

1. finite exchange equivalence;
2. finite law covariance or quasi-invariance;
3. finite Bianchi/Jacobi identity for exchange curvature;
4. finite source conservation or codivergence control;
5. finite Hodge/coercive gap plus harmonic-sector control.

The question is whether this stack proves actual residual moment decay:

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

### Definition 10.1: Finite Exchange Equivalence Data

Finite exchange equivalence data consist of:

1. a finite record space \(\Omega_a\);
2. a finite set \({\mathcal U}_a\) of admissible exchange moves;
3. for each \(u\in{\mathcal U}_a\), a partial bijection

   $$
   T_u:\operatorname{dom}(T_u)\to\operatorname{ran}(T_u)
   $$

   on \(\Omega_a\);
4. a finite comparison residual \({\mathcal R}_a(q)\in V_a\);
5. a finite source-response class of tests \(f:\Omega_a\to\mathbb R\).

The data are Barandes-aligned when \(T_u\) acts only on finite records and
does not split the whole-slab transition into hidden substeps.

### Definition 10.2: Finite Law Covariance

The actual law is exactly covariant under \(T_u\) if

$$
\mathbb P_a^{act}(T_uA)=\mathbb P_a^{act}(A)
$$

for all events \(A\subset\operatorname{dom}(T_u)\).  It is covariant up to
defect \(\xi_a(u)\) if

$$
\sup_{\|f\|_\infty\le1}
\left|
\mathbb E_a^{act}
\left[
f(T_uQ_a)-f(Q_a)
\right]
\right|
\le
\xi_a(u).
$$

### Proposition 10.3: Finite Covariance Gives Ward Identities

If exact finite law covariance holds for \(T_u\), then

$$
\mathbb E_a^{act}
\left[
f(T_uQ_a)-f(Q_a)
\right]
=0
$$

for every bounded finite test \(f\).  If covariance holds up to defect
\(\xi_a(u)\), then the absolute value of the same expression is at most
\(\xi_a(u)\|f\|_\infty\).

Proof.

This is change of variables under a finite partial bijection.  The defective
case is exactly Definition 10.2 after rescaling \(f\).  `square`

### Verdict 10.4

Finite covariance is the analogue of general covariance at the level of
record laws.  It gives Ward identities.  But, by Paper 12 Proposition 2.2,
Ward centering alone does not control residual variance.

### Definition 10.5: Finite Residual Complex

A finite residual complex is a sequence of finite-dimensional Hilbert spaces
and linear maps

$$
C_a^0
\xrightarrow{d_a}
C_a^1
\xrightarrow{D_a}
C_a^2
$$

with

$$
D_ad_a=0.
$$

The residual vector is regarded as

$$
{\mathcal R}_a(q)\in C_a^1.
$$

The finite Bianchi defect is

$$
{\mathcal B}_a(q):=D_a{\mathcal R}_a(q)\in C_a^2.
$$

The finite codivergence/source defect is

$$
{\mathcal C}_a(q):=d_a^*{\mathcal R}_a(q)\in C_a^0.
$$

The harmonic residual space is

$$
{\mathcal H}_a
:=
\ker D_a\cap\ker d_a^*.
$$

Let \(\Pi_{{\mathcal H}_a}\) denote orthogonal projection onto
\({\mathcal H}_a\).

### Definition 10.6: Finite Bianchi-Ward Control

The actual law satisfies finite Bianchi-Ward control at scales
\((b_a,c_a,h_a)\) if

$$
\mathbb E_a^{act}\|D_a{\mathcal R}_a\|^2\le b_a,
$$

$$
\mathbb E_a^{act}\|d_a^*{\mathcal R}_a\|^2\le c_a,
$$

and

$$
\mathbb E_a^{act}
\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2\le h_a.
$$

The first estimate is the Bianchi side.  The second is the conservation or
codivergence side.  The third kills finite harmonic residual modes.

### Definition 10.7: Finite Hodge Gap

The residual complex has Hodge gap \(\lambda_a>0\) off the harmonic sector if
for every \(r\in C_a^1\) orthogonal to \({\mathcal H}_a\),

$$
\|D_ar\|^2+\|d_a^*r\|^2
\ge
\lambda_a\|r\|^2.
$$

### Theorem 10.8: Finite Bianchi-Hodge Coercivity Implies Moment Decay

Assume the finite residual complex has Hodge gap \(\lambda_a\) with

$$
\inf_a\lambda_a>0.
$$

If finite Bianchi-Ward control holds with

$$
b_a+c_a+h_a\to0,
$$

then

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

Proof.

For each \(q\), decompose

$$
{\mathcal R}_a(q)
=
r_a^\perp(q)+r_a^H(q),
$$

where \(r_a^H=\Pi_{{\mathcal H}_a}{\mathcal R}_a\) and
\(r_a^\perp\perp{\mathcal H}_a\).  Since \(D_a\) and \(d_a^*\) vanish on the
harmonic sector,

$$
D_ar_a^\perp=D_a{\mathcal R}_a,
\qquad
d_a^*r_a^\perp=d_a^*{\mathcal R}_a.
$$

By the Hodge gap,

$$
\|r_a^\perp\|^2
\le
\lambda_a^{-1}
\left(
\|D_a{\mathcal R}_a\|^2+\|d_a^*{\mathcal R}_a\|^2
\right).
$$

Therefore

$$
\|{\mathcal R}_a\|^2
\le
\lambda_a^{-1}
\left(
\|D_a{\mathcal R}_a\|^2+\|d_a^*{\mathcal R}_a\|^2
\right)
+\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2.
$$

Taking actual expectations gives

$$
\mathbb E_a^{act}[{\mathcal A}_a]
\le
\lambda_a^{-1}(b_a+c_a)+h_a,
$$

which tends to zero.  `square`

### Corollary 10.9: Bianchi-Hodge Proves The Paper-11 Positive Route

If the hypotheses of Theorem 10.8 hold, and the regularity/tail hypotheses
from Paper 11 Theorem 13.12 hold, then

$$
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1
$$

for some \(\epsilon_a\downarrow0\).

Proof.

Theorem 10.8 gives actual residual moment decay.  Paper 11 Theorem 13.12
converts moment decay plus regularity/tail control into good-configuration
concentration.  `square`

### Proposition 10.10: Bianchi Alone Does Not Bound Residuals

The estimate

$$
D_a{\mathcal R}_a=0
$$

does not imply

$$
\mathbb E_a^{act}\|{\mathcal R}_a\|^2\to0.
$$

Proof.

Let \(C_a^0=0\), \(C_a^1=\mathbb R\), \(C_a^2=0\).  Then \(D_a=0\), so every
residual is Bianchi-closed.  Let \({\mathcal R}_a(q)=1\) for every record.
Then \(D_a{\mathcal R}_a=0\), but

$$
\mathbb E_a^{act}\|{\mathcal R}_a\|^2=1.
$$

This is a pure harmonic residual.  `square`

### Proposition 10.11: Bianchi Plus Codivergence Still Leaves Harmonic Modes

Even if

$$
D_a{\mathcal R}_a=0
$$

and

$$
d_a^*{\mathcal R}_a=0,
$$

the residual need not be small unless the harmonic projection is controlled.

Proof.

Take any residual complex with nonzero harmonic vector \(h\in{\mathcal H}_a\).
Let \({\mathcal R}_a(q)=h\) for every record.  Then both Bianchi and
codivergence defects vanish, while

$$
\|{\mathcal R}_a(q)\|^2=\|h\|^2.
$$

`square`

### Proposition 10.12: Hodge Gap Alone Does Not Supply Source Control

A uniform Hodge gap does not prove residual moment decay unless the actual
law supplies small Bianchi and codivergence defects.

Proof.

Let the complex have no harmonic sector and a fixed positive Hodge gap.  Pick
a nonzero \(r\in C_a^1\) and define \({\mathcal R}_a(q)=r\) for every record.
Then

$$
\|{\mathcal R}_a\|^2
$$

is fixed.  The Hodge estimate says this norm is controlled by
\(\|D_ar\|^2+\|d_a^*r\|^2\), not that those two quantities are small.  `square`

### Definition 10.13: Finite Einstein-Style Stack

The finite Einstein-style stack holds at scales
\((\xi_a,b_a,c_a,h_a,\lambda_a)\) if:

1. finite exchange covariance holds with defect \(\xi_a\to0\);
2. the exchange residuals form a finite residual complex;
3. Bianchi defect satisfies \(b_a\to0\);
4. conservation/codivergence defect satisfies \(c_a\to0\);
5. harmonic residual mass satisfies \(h_a\to0\);
6. the Hodge gap has \(\inf_a\lambda_a>0\);
7. regularity/tail control from Paper 11 holds.

### Theorem 10.14: Finite Einstein-Style Stack Closes The Positive Route

If the finite Einstein-style stack holds, then

$$
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1
$$

for some \(\epsilon_a\downarrow0\).

Proof.

Items 3 through 6 are exactly Theorem 10.8.  Item 7 is exactly the additional
regularity/tail input needed by Paper 11 Theorem 13.12.  Finite covariance
and the residual complex provide the record-level meaning of the Bianchi and
codivergence estimates.  `square`

### Proposition 10.15: Current-Corpus Status Of The Einstein-Style Stack

The current corpus does not prove the finite Einstein-style stack.

Proof.

Papers 4 and 5 source fixed-background enriched metric and curvature
diagnostics.  Papers 6 and 7 introduce finite geometry configurations and
residuals.  Papers 8 through 12 identify residual penalties, side decisions,
actual laws, transfer mechanisms, and residual-source response calculus.

However, the current corpus does not prove all of:

1. an actual finite residual complex with \(D_ad_a=0\) for the full Paper-7
   residual vector;
2. actual-law \(L^2\) smallness of the Bianchi defect \(D_a{\mathcal R}_a\);
3. actual-law \(L^2\) smallness of the codivergence/source defect
   \(d_a^*{\mathcal R}_a\);
4. actual-law control of the harmonic residual projection;
5. a uniform finite Hodge gap on the non-harmonic residual sector.

Thus the stack is a precise new primitive package, not a theorem already
contained in the current corpus.  `square`

### Corollary 10.16: Einstein-Style Route Refines Stein Coercivity

The finite Bianchi-Hodge route is a structured way to try to prove
residual-source Stein coercivity.  It decomposes the needed coercivity into:

1. Bianchi smallness;
2. codivergence/source smallness;
3. harmonic-sector elimination;
4. Hodge spectral gap.

Proof.

Theorem 10.8 is exactly a coercive estimate for the residual norm.  Stein
coercivity in Section 2 proves the same residual moment conclusion by an
integration-by-parts route.  The Bianchi-Hodge route identifies a geometric
finite complex whose Hodge estimate would supply that coercivity.  `square`

### Verdict 10.17

The Einstein-style path is not dead and not solved.  It is the most
principled positive route because it tries to make residual smallness follow
from finite covariance, Bianchi/Jacobi structure, conservation, and a Hodge
gap rather than from an arbitrary comparison law.

But it does not escape the same-law requirement.  The new primitive theorem
would be:

$$
\boxed{
\mathrm{V4P12\text{-}FINITE\text{-}BIANCHI\text{-}HODGE\text{-}COERCIVITY}.
}
$$

This theorem must be proved under the actual finite law
\(\mathbb P_a^{act}\).  Without the Hodge gap and harmonic control, Bianchi
identities are only structural identities, not value estimates.

## 11. Paper-7 Residual Complex Instantiation Test

Section 10 proves the abstract finite Bianchi-Hodge theorem.  The next
question is whether the actual Paper-7 residual package can instantiate the
complex

$$
C_a^0\xrightarrow{d_a}C_a^1\xrightarrow{D_a}C_a^2,
\qquad
D_ad_a=0.
$$

This section tests that possibility inside Paper 12.

### Import 11.1: Paper-7 Multiplicative Residuals

Paper 7 defines finite comparison maps

$$
D_a[v],
\qquad
H_a[N],
$$

on the finite total effect space.  It defines multiplicative residuals

$$
R_{DD,a}[v,w],
\qquad
R_{DH,a}[v,N],
\qquad
R_{HH,a}[N,M].
$$

These are comparison-map residuals, not automatically vectors in a linear
cochain complex.

### Definition 11.2: Vectorization Gate

The Paper-7 residuals pass the vectorization gate if there is a finite
linear residual coordinate map

$$
\mathfrak v_a:
\{\hbox{tested comparison-map residuals}\}
\to W_a
$$

such that:

1. \(\mathfrak v_a(I)=0\);
2. \(\|\mathfrak v_a(R)\|\) is equivalent to the declared Paper-7 residual
   norm on the tested observable class;
3. \(\mathfrak v_a\) is defined on finite record/effect data only;
4. no continuum logarithm or Hilbert phase is used as primitive.

One canonical choice is

$$
\mathfrak v_a(R):=(R-I)|_{{\mathcal O}_a},
$$

viewed as a finite operator on the declared observable test space
\({\mathcal O}_a\).

### Proposition 11.3: Vectorization Gate Passes Conditionally

If \({\mathcal O}_a\) is finite-dimensional and the Paper-7 residual norm is
the operator norm of \(R-I\) on \({\mathcal O}_a\), then

$$
\mathfrak v_a(R)=(R-I)|_{{\mathcal O}_a}
$$

passes the vectorization gate.

Proof.

The map is finite and linear in the operator difference \(R-I\).  It sends
the identity residual to zero.  Its norm is exactly the declared residual
norm.  It uses only finite comparison maps on finite effect spaces.  `square`

### Verdict 11.4

The residual-complex route is not blocked at vectorization.  The safe
Barandes-aligned vector is the finite operator defect \(R-I\), not a
continuum logarithm of \(R\).

### Definition 11.5: Residual One-Space \(C_a^1\)

Let \({\mathcal T}_a\) be the finite tangential test-label set and
\({\mathcal N}_a\) the finite lapse-label set.  Define

$$
C_a^1
:=
C_{DD,a}^1\oplus C_{DH,a}^1\oplus C_{HH,a}^1
\oplus C_{cov,a}^1,
$$

where

$$
C_{DD,a}^1
:=
\bigoplus_{v,w\in{\mathcal T}_a}W_a,
$$

$$
C_{DH,a}^1
:=
\bigoplus_{v\in{\mathcal T}_a,\ N\in{\mathcal N}_a}W_a,
$$

and

$$
C_{HH,a}^1
:=
\bigoplus_{N,M\in{\mathcal N}_a}W_a.
$$

The covariance residual component \(C_{cov,a}^1\) is the finite vector space
containing the dynamical covariance error \({\mathcal E}_{cov,a}\).

The Paper-7 residual vector is

$$
{\mathcal R}_a(q)
:=
\left(
\mathfrak v_a(R_{DD,a}^q),
\mathfrak v_a(R_{DH,a}^q),
\mathfrak v_a(R_{HH,a}^q),
{\mathcal E}_{cov,a}^q
\right)
\in C_a^1.
$$

### Definition 11.6: Finite Label Jacobi Defect

Let

$$
[\cdot,\cdot]_a
$$

denote the declared finite bracket on tangential and normal test labels,
including the geometry-dependent \(HH\to D\) structure function.  The finite
label Jacobi defect is the trilinear expression

$$
{\mathsf Jac}_a(\alpha,\beta,\gamma)
:=
[\alpha,[\beta,\gamma]_a]_a
+[\beta,[\gamma,\alpha]_a]_a
+[\gamma,[\alpha,\beta]_a]_a,
$$

where \(\alpha,\beta,\gamma\) range over the tested tangential/normal labels,
with the understood finite geometry dependence in the \(HH\) bracket.

### Definition 11.6A: Paper-7 Label Bracket Table

Write a tangential label as \(D(v)\) and a normal label as \(H(N)\).  The
Paper-7 benchmark bracket table is:

$$
[D(v),D(w)]_a
:=
D([v,w]_a),
$$

$$
[D(v),H(N)]_a
:=
H({\mathcal L}_{v,a}N),
$$

$$
[H(N),D(v)]_a
:=
-H({\mathcal L}_{v,a}N),
$$

and

$$
[H(N),H(M)]_a
:=
D(\beta_a(g;N,M)),
$$

where

$$
\beta_a(g;N,M)^i
=
I_a(g)^{ij}(N\partial_jM-M\partial_jN).
$$

This table is finite once the test-label sets, finite derivatives, and metric
readout \(I_a(g)^{ij}\) are fixed.

### Definition 11.6B: Four Jacobi Sector Defects

The finite label Jacobi defect decomposes into four sectors.

The \(DDD\) defect is

$$
{\mathsf Jac}_{DDD,a}(u,v,w)
:=
[u,[v,w]_a]_a
+[v,[w,u]_a]_a
+[w,[u,v]_a]_a.
$$

The \(DDH\) defect is

$$
{\mathsf Jac}_{DDH,a}(v,w;N)
:=
{\mathcal L}_{v,a}{\mathcal L}_{w,a}N
-{\mathcal L}_{w,a}{\mathcal L}_{v,a}N
-{\mathcal L}_{[v,w]_a,a}N.
$$

The \(DHH\) defect is

$$
\begin{aligned}
{\mathsf Jac}_{DHH,a}(v;N,M)
:={}&
[v,\beta_a(g;N,M)]_a\\
&-\beta_a(g;{\mathcal L}_{v,a}N,M)
-\beta_a(g;N,{\mathcal L}_{v,a}M)
+{\mathsf MetCov}_{a}(v;N,M).
\end{aligned}
$$

Here \({\mathsf MetCov}_{a}(v;N,M)\) is the finite metric-covariance defect
measuring failure of the metric readout \(I_a(g)^{ij}\) and finite
derivatives to transform naturally under the tangential label \(v\).  If the
finite metric readout and derivative table are exactly tangentially
covariant, then

$$
{\mathsf MetCov}_{a}(v;N,M)=0.
$$

The \(HHH\) defect is

$$
\begin{aligned}
{\mathsf Jac}_{HHH,a}(N,M,L)
:={}&
{\mathcal L}_{\beta_a(g;M,L),a}N
+{\mathcal L}_{\beta_a(g;L,N),a}M\\
&+{\mathcal L}_{\beta_a(g;N,M),a}L
+{\mathsf NorMet}_{a}(N,M,L).
\end{aligned}
$$

Here \({\mathsf NorMet}_{a}(N,M,L)\) is the finite normal-geometry response
defect measuring whether the geometry-dependent structure function
\(\beta_a(g;\cdot,\cdot)\) is transported consistently under the normal
comparison labels.  In a frozen-background bracket test this term is
declared zero; in a dynamical-geometry test it must be sourced by the actual
finite geometry update.

### Proposition 11.6C: Jacobi Table Computation

For the Paper-7 label table, the full finite label Jacobi defect vanishes if
and only if the following four sector conditions hold on the tested label
sets:

$$
{\mathsf Jac}_{DDD,a}=0,
$$

$$
{\mathsf Jac}_{DDH,a}=0,
$$

$$
{\mathsf Jac}_{DHH,a}=0,
$$

and

$$
{\mathsf Jac}_{HHH,a}=0.
$$

Equivalently, the four required finite identities are:

1. the finite tangential bracket satisfies Jacobi;
2. finite lapse transport is a representation of the finite tangential
   bracket;
3. the finite \(\beta_a\) structure function is tangentially equivariant;
4. the finite \(\beta_a\) structure function satisfies the cyclic \(HHH\)
   identity, including any normal-geometry response defect.

Proof.

Evaluate

$$
[\alpha,[\beta,\gamma]_a]_a
+[\beta,[\gamma,\alpha]_a]_a
+[\gamma,[\alpha,\beta]_a]_a
$$

using the table in Definition 11.6A.

For three tangential labels one obtains exactly
\({\mathsf Jac}_{DDD,a}\).

For two tangential labels and one lapse, the cyclic sum is

$$
H\!\left(
{\mathcal L}_{v,a}{\mathcal L}_{w,a}N
-{\mathcal L}_{w,a}{\mathcal L}_{v,a}N
-{\mathcal L}_{[v,w]_a,a}N
\right),
$$

which is the \(DDH\) defect.

For one tangential label and two lapse labels, the cyclic sum is

$$
D\!\left(
[v,\beta_a(g;N,M)]_a
-\beta_a(g;{\mathcal L}_{v,a}N,M)
-\beta_a(g;N,{\mathcal L}_{v,a}M)
 \right),
$$

plus the finite metric-covariance defect.  This is
\({\mathsf Jac}_{DHH,a}\).

For three lapse labels, the cyclic sum is the normal label

$$
H\!\left(
{\mathcal L}_{\beta_a(g;M,L),a}N
+{\mathcal L}_{\beta_a(g;L,N),a}M
+{\mathcal L}_{\beta_a(g;N,M),a}L
\right),
$$

plus any normal-geometry response defect.  This is
\({\mathsf Jac}_{HHH,a}\).  `square`

### Theorem 11.6D: Finite Label-Jacobi Gate

The finite label-Jacobi gate for the Paper-7 residual-complex route passes
exactly on sectors where

$$
\|{\mathsf Jac}_{DDD,a}\|
+\|{\mathsf Jac}_{DDH,a}\|
+\|{\mathsf Jac}_{DHH,a}\|
+\|{\mathsf Jac}_{HHH,a}\|
\to0,
$$

with the \(DHH\) and \(HHH\) terms including the finite metric-covariance and
normal-geometry response defects.  If these defects do not vanish, then the
linear Bianchi operator can only satisfy

$$
D_a^{lin}d_a=0
$$

after quotienting, enriching the finite label architecture, or restricting
to a smaller tested sector.

Proof.

Proposition 11.6C identifies the full Jacobiator with the four displayed
sector defects.  Proposition 11.8 below shows that the obstruction to
\(D_a^{lin}d_a=0\) is exactly the finite label Jacobi defect.  Therefore the
gate passes precisely when these defects vanish or are small at the needed
rate.  `square`

### Verdict 11.6E: Current-Corpus Status Of Step 1

Step 1 is now fully reduced to a finite table.  The current corpus supplies
the symbolic bracket entries, but it does not yet prove the four sector
defects vanish for the actual finite test-label architecture:

1. \(DDD\) requires exact finite tangential Jacobi;
2. \(DDH\) requires lapse transport to represent the finite tangential
   bracket;
3. \(DHH\) requires tangential covariance of the finite metric readout and
   derivative table;
4. \(HHH\) requires a cyclic beta identity plus control of the normal
   geometry-response defect.

Thus the label-Jacobi gate is not closed unconditionally, but it is now
sharp: the next calculation is not vague.  It is the evaluation of these
four finite defects for the chosen regulator/test-label architecture.

### Definition 11.6F: Quantitative Four-Sector Jacobi Errors

For normalized tested labels, define the four finite Jacobi error moduli

$$
J_{DDD,a}
:=
\sup_{\|u\|,\|v\|,\|w\|\le1}
\|{\mathsf Jac}_{DDD,a}(u,v,w)\|,
$$

$$
J_{DDH,a}
:=
\sup_{\|v\|,\|w\|,\|N\|\le1}
\|{\mathsf Jac}_{DDH,a}(v,w;N)\|,
$$

$$
J_{DHH,a}
:=
\sup_{\|v\|,\|N\|,\|M\|\le1}
\|{\mathsf Jac}_{DHH,a}(v;N,M)\|,
$$

and

$$
J_{HHH,a}
:=
\sup_{\|N\|,\|M\|,\|L\|\le1}
\|{\mathsf Jac}_{HHH,a}(N,M,L)\|.
$$

The Step-1 label-Jacobi gate is the assertion

$$
J_{DDD,a}+J_{DDH,a}+J_{DHH,a}+J_{HHH,a}\to0.
$$

### Proposition 11.6G: Kinematic Evaluation Of The \(DDD\) And \(DDH\)
Sectors

Assume the tested tangential labels are induced from one finite
embedding-flow transport architecture, and that the finite tangential
bracket and finite lapse action are the commutator and scalar transport
actions of that same architecture, up to errors

$$
\eta^T_a\to0,
\qquad
\eta^L_a\to0.
$$

Then

$$
J_{DDD,a}\le C\eta^T_a,
\qquad
J_{DDH,a}\le C(\eta^T_a+\eta^L_a).
$$

In particular, in the enriched fixed-background architecture of Paper 5,
where the tested maps are chosen from a projectively compatible
embedding-flow table, the \(DDD\) and \(DDH\) gates are kinematic and close
at the regulator accuracy.

Proof.

For an exact same-architecture tangential table, the labels are represented
by one finite-dimensional family of smooth vector fields, or by finite
projections of such fields.  The unprojected vector-field bracket satisfies
Jacobi.  Projecting this bracket onto the declared finite tangential label
table introduces only the bracket projection error \(\eta^T_a\).  This gives
the first estimate.

For \(DDH\), the lapse action is the scalar representation of the same
tangential transport.  Thus

$$
[{\mathcal L}_{v,a},{\mathcal L}_{w,a}]N
=
{\mathcal L}_{[v,w]_a,a}N
+
O(\eta^T_a+\eta^L_a).
$$

Taking the supremum over normalized tested labels gives the second estimate.
`square`

### Proposition 11.6H: \(DHH\) Reduces To Tangential Naturality Of The Metric
Readout

Let

$$
{\mathsf TMet}_{a}(v;N,M)
:=
[v,\beta_a(g;N,M)]_a
-\beta_a(g;{\mathcal L}_{v,a}N,M)
-\beta_a(g;N,{\mathcal L}_{v,a}M)
+{\mathsf MetCov}_{a}(v;N,M).
$$

Then

$$
J_{DHH,a}
=
\sup_{\|v\|,\|N\|,\|M\|\le1}
\|{\mathsf TMet}_{a}(v;N,M)\|.
$$

Consequently, \(DHH\) is closed exactly when the finite metric readout
\(I_a(g)^{ij}\), finite derivative table, and finite tangential transport
are natural for one another on the tested labels.

In a fixed enriched background with the Paper-5 compatible transport
architecture and Paper-6 regular metric readout, this error tends to zero
with the transport and interpolation errors.  In the dynamical
matter-geometry law, this is not automatic: it is precisely a finite
tangential covariance requirement on the actual metric-update/readout
package.

Proof.

The displayed expression is Definition 11.6B's \(DHH\) Jacobi defect.  If
the finite metric readout is transported naturally, then the vector field
\(\beta_a(g;N,M)\) transforms as the metric contraction of the transported
lapses.  The three non-covariance terms cancel, leaving only the declared
\({\mathsf MetCov}_a\), which is zero or regulator-small by hypothesis.

Conversely, if the \(DHH\) defect vanishes for all tested \(N,M\), then the
finite table cannot distinguish the transported \(\beta_a\) from the
\(\beta_a\) built from transported lapse data.  That is exactly tangential
naturality of the metric readout on the tested finite sector.  `square`

### Proposition 11.6I: The \(HHH\) Sector Splits Into A Frozen Algebraic
Identity And A Normal-Geometry Response

Write

$$
\begin{aligned}
{\mathsf Cyc}\beta_a(N,M,L)
:={}&
{\mathcal L}_{\beta_a(g;M,L),a}N
+{\mathcal L}_{\beta_a(g;L,N),a}M\\
&+{\mathcal L}_{\beta_a(g;N,M),a}L .
\end{aligned}
$$

Then

$$
{\mathsf Jac}_{HHH,a}
=
{\mathsf Cyc}\beta_a+{\mathsf NorMet}_a.
$$

If the test is a frozen-background test with a symmetric finite inverse
metric \(I_a(g)^{ij}=I_a(g)^{ji}\), a common finite derivative table in the
definition of both \(\beta_a\) and \({\mathcal L}_{\beta,a}\), and
\({\mathsf NorMet}_a=0\), then

$$
{\mathsf Cyc}\beta_a(N,M,L)=0
$$

algebraically for all tested lapse labels.  Hence the frozen-background
\(HHH\) sector closes.

For a dynamical geometry test, however, the term
\({\mathsf NorMet}_a\) is not optional.  It measures the response of the
metric component of the finite configuration under the normal comparison
labels.  The current corpus does not prove

$$
\mathbb E_a^{act}\|{\mathsf NorMet}_a\|^2\to0
$$

or a deterministic regulator bound on \({\mathsf NorMet}_a\).

Proof.

The first equation is the definition of the \(HHH\) defect.

For the frozen-background algebraic cancellation, expand the first cyclic
term:

$$
{\mathcal L}_{\beta_a(g;M,L),a}N
=
I_a(g)^{ij}(M\partial_jL-L\partial_jM)\partial_iN.
$$

Adding the two cyclic rotations gives

$$
\begin{aligned}
{}&
I_a^{ij}(M\partial_jL-L\partial_jM)\partial_iN\\
&+
I_a^{ij}(L\partial_jN-N\partial_jL)\partial_iM\\
&+
I_a^{ij}(N\partial_jM-M\partial_jN)\partial_iL.
\end{aligned}
$$

Because \(I_a^{ij}\) is symmetric and scalar multiplication is commutative,
the six terms cancel in pairs.  No continuum limit is being used.  This is a
finite algebraic identity on the declared table.

In a dynamical geometry test, the \(HH\to D\) structure function depends on
the metric record, and the normal comparison maps also change that metric
record.  The missing contribution is exactly
\({\mathsf NorMet}_a\).  Without an actual finite normal-response identity,
the frozen cancellation does not prove the dynamical \(HHH\) sector.  `square`

### Theorem 11.6J: Current-Corpus Evaluation Of The Four Jacobi Sectors

The current corpus evaluates the four Step-1 Jacobi sectors as follows.

1. \(DDD\) is kinematic and closes in a projectively compatible
   embedding-flow architecture.
2. \(DDH\) is kinematic and closes when lapse transport is the scalar
   representation of the same tangential finite transport.
3. \(DHH\) closes in the enriched fixed-background sector, but in the
   dynamical matter-geometry sector it requires a same-law tangential metric
   covariance estimate.
4. \(HHH\) closes algebraically in the frozen-background sector, but in the
   dynamical matter-geometry sector it requires a same-law normal metric
   response estimate.

Therefore the fixed-background/enriched Paper-5 algebra can be made
Jacobi-compatible, but the full Paper-7 dynamical residual-complex route is
not yet closed.  The live primitive is

$$
\boxed{
\mathrm{V4P12\text{-}NORMAL\text{-}GEOMETRY\text{-}JACOBI\text{-}RESPONSE}
}
$$

together with the tangential covariance companion

$$
\boxed{
\mathrm{V4P12\text{-}TANGENTIAL\text{-}METRIC\text{-}NATURALITY}.
}
$$

Proof.

Items 1 and 2 are Proposition 11.6G.  Item 3 is Proposition 11.6H.  Item 4
is Proposition 11.6I.

The distinction between fixed-background closure and dynamical closure is
essential.  Fixed-background closure only says that a declared enriched
metric table and compatible finite transports reproduce the hypersurface
bracket algebra.  The Paper-7 route asks more: it asks that the actual finite
matter-geometry law move the metric record under normal and tangential
comparison labels in the way required by the same finite algebra.  That is
not sourced by the current corpus.  `square`

### Corollary 11.6K: Step-1 Settlement

Step 1 is settled at current-corpus level.

The answer is positive for the frozen/enriched kinematic test:

$$
J_{DDD,a}+J_{DDH,a}+J_{DHH,a}+J_{HHH,a}\to0
$$

can be forced by choosing compatible finite embedding-flow transports,
regular metric readouts, and a symmetric common \(\beta_a\) table.

The answer is not yet positive for the dynamical Paper-7 residual complex.
There the same formal symbols contain actual geometry-update content, and
the current corpus does not source the two estimates

$$
\mathbb E_a^{act} J_{DHH,a}^2\to0,
\qquad
\mathbb E_a^{act} J_{HHH,a}^2\to0.
$$

The decisive new finite theorem is therefore not another bracket table.  It
is a normal/tangential metric-response theorem for the actual
matter-geometry law.

### Definition 11.6L: Finite Equivalence Principle For Normal Metric Response

Let

$$
{\mathsf I}_{a}^{ij}\in V_a^{tot}
$$

be the finite inverse-metric readout observable.  For a normal comparison
label \(N\), define the operational normal metric response by

$$
\delta_{N,a}{\mathsf I}^{ij}
:=
H_a[N]{\mathsf I}_{a}^{ij}-{\mathsf I}_{a}^{ij}.
$$

This is not a hidden time derivative.  It is the finite difference between
two record-level comparison questions:

1. ask for the metric readout directly;
2. first compare the hypersurface normally by \(H_a[N]\), then ask for the
   same metric readout.

The finite equivalence principle for normal metric response is the assertion
that, on the tested metric observables and lapse labels, this response is
the same response that appears in the normal-normal hypersurface exchange
bracket.  Equivalently, the same finite rule that changes the metric readout
under \(H_a[N]\) must also be the rule used when the geometry-dependent
structure function

$$
\beta_a(g;M,L)^i
=
{\mathsf I}_{a}^{ij}
(M\partial_jL-L\partial_jM)
$$

is transported through a third normal comparison.

The finite theorem target is:

$$
\boxed{
\mathrm{V4P12\text{-}FINITE\text{-}EQUIV\text{-}NORMAL\text{-}RESPONSE}
}
$$

meaning:

$$
\mathbb E_a^{act}
\sup_{N,M,L}
\|{\mathsf NorMet}_a(N,M,L)\|^2
\to0.
$$

Plainly: a finite observer must not be able to tell whether the metric
record was updated by a normal comparison directly, or by the metric response
forced by the finite \(HH\to D\) exchange law.  That is the finite
Barandes-aligned analogue of the equivalence-principle idea at this gate.

### Definition 11.6M: The Three-Normal Switch Detector

For finite comparison maps \(A,B\), write the group commutator

$$
{\mathsf C}(A,B):=ABA^{-1}B^{-1}.
$$

For three lapse labels \(N,M,L\), define the predicted tangential shift
coming from the \(M,L\) normal pair by

$$
B_{ML,a}:=\beta_a(g;M,L).
$$

The smallest switch object that can see the \(HHH\) Jacobi obstruction is
not the corrected \(HH\) pair residual itself.  That would become
operationally invisible as soon as \(HH\) pair closure is good.  The \(HHH\)
question is subtler: it asks how a third normal comparison \(H_a[N]\) acts
on the tangential shift \(D_a[B_{ML,a}]\) produced by the other two normal
labels.

Define the corrected normal-tangential switch

$$
{\mathsf W}_{N|ML,a}
:=
{\mathsf C}(H_a[N],D_a[B_{ML,a}])\,
H_a[{\mathcal L}_{B_{ML,a},a}N].
$$

Here \({\mathcal L}_{B_{ML,a},a}N\) is understood as the finite projected
lapse label in the tested normal-label alphabet.  The projection error is
part of the same regulator error already present in the \(DDH\) and \(DHH\)
gates.

The sign is chosen because the leading bracket is

$$
[H(N),D(B_{ML})]_a=-H({\mathcal L}_{B_{ML},a}N).
$$

The cyclic three-normal detector is

$$
\begin{aligned}
{\mathsf SW}_{HHH,a}(N,M,L)
:={}&
{\mathsf W}_{N|ML,a}\,
{\mathsf W}_{M|LN,a}\,
{\mathsf W}_{L|NM,a}.
\end{aligned}
$$

For a finite metric observable \(G\in{\mathcal G}^{met}_a\), define the
detector value

$$
{\mathsf Det}_{HHH,a}(N,M,L;G)
:=
\left\|
{\mathsf SW}_{HHH,a}(N,M,L)G-G
\right\|_{{\mathcal O}_a}.
$$

The detector scale is

$$
{\mathsf Det}_{HHH,a}
:=
\sup_{N,M,L,G}
{\mathsf Det}_{HHH,a}(N,M,L;G),
$$

where \(N,M,L\) range over normalized tested lapse labels and
\(G\) ranges over normalized metric readout observables.

This detector is the Feynman-style finite experiment: let a normal-normal
pair produce its predicted tangential shift, switch that tangential shift
against the third normal comparison, correct by the predicted normal label,
cycle over the three choices, and ask whether any metric record can still
detect a leftover.

### Proposition 11.6N: The Switch Detector Is Barandes-Aligned

The three-normal switch detector is a finite record-law object.

Proof.

The detector uses only:

1. finite comparison maps \(H_a[N]\) and \(D_a[v]\) already introduced in
   Paper 7;
2. the finite metric readout \({\mathsf I}_a^{ij}\) introduced in Papers 6
   and 7;
3. the finite bracket vector \(\beta_a(g;N,M)\);
4. finite products, inverses, and observable norms on \(V_a^{tot}\).

It does not introduce a continuum path integral, a hidden Markov
subdivision, a Hilbert-space state, or Einstein equations as primitive
dynamics.  It is a finite question about whether two record-level comparison
procedures are operationally distinguishable.  `square`

### Theorem 11.6O: Detector Equivalence To Normal Geometry Jacobi Response

Assume:

1. the \(HH\) pair residuals
   \({\mathsf C}(H_a[N],H_a[M])D_a[-\beta_a(g;N,M)]-I\) are \(o(1)\) on
   the tested metric observables;
2. the metric observables \({\mathcal G}^{met}_a\) separate tested metric
   records with constant \(s_a^{-1}\) not diverging faster than the declared
   regulator accuracy;
3. the tangential \(DHH\) naturality error is \(o(1)\).

Then

$$
{\mathsf Det}_{HHH,a}\to0
\quad\Longleftrightarrow\quad
J_{HHH,a}\to0
$$

on the tested normal-label sector, up to the separation and pair-residual
errors.  More quantitatively, there are finite constants \(C_a,C'_a\) such
that

$$
{\mathsf Det}_{HHH,a}
\le
C_a
\left(
J_{HHH,a}
+\sup_{N,M}
\|{\mathsf C}(H_a[N],H_a[M])D_a[-\beta_a(g;N,M)]-I\|_{{\mathcal G}^{met}_a}
+J_{DHH,a}
\right),
$$

and

$$
J_{HHH,a}
\le
C'_a
\left(
{\mathsf Det}_{HHH,a}
+\sup_{N,M}
\|{\mathsf C}(H_a[N],H_a[M])D_a[-\beta_a(g;N,M)]-I\|_{{\mathcal G}^{met}_a}
+J_{DHH,a}
\right).
$$

Proof.

Expand the cyclic product
\({\mathsf SW}_{HHH,a}(N,M,L)\) on a metric observable \(G\).  Each
\({\mathsf W}_{N|ML,a}\) removes the leading normal label predicted by the
\([H,D]\) bracket after the \(M,L\) pair has produced the tangential
\(\beta\)-shift.  Therefore the first leftover visible to metric observables
is exactly the cyclic failure of the third-normal response to the
normal-normal tangential shift.

The part of that leftover caused by tangential transport of \(\beta_a\) is
the \(DHH\) naturality defect.  The part caused by imperfect pair closure is
the \(HH\) pair residual.  After those are subtracted, the remaining
metric-visible term is precisely the normal geometry response term
\({\mathsf NorMet}_a\) in the \(HHH\) Jacobi defect.

The first inequality follows by applying the triangle inequality to this
finite expansion on all normalized metric observables.  The second follows
from the separating-observable hypothesis: if metric observables cannot see
a residual, then it is zero on the tested metric sector up to the separation
constant.  `square`

### Corollary 11.6P: The Smallest Positive Theorem Now Needed

The Einstein-style and Feynman-style formulations meet at the same finite
target:

$$
\boxed{
\mathbb E_a^{act}{\mathsf Det}_{HHH,a}^2\to0
}
$$

together with \(HH\) pair residual smallness and tangential metric
naturality.  Under Theorem 11.6O this proves

$$
\mathbb E_a^{act}J_{HHH,a}^2\to0.
$$

Thus the next positive theorem can be stated without philosophy:

$$
\boxed{
\mathrm{V4P12\text{-}THREE\text{-}NORMAL\text{-}SWITCH\text{-}SMALLNESS}.
}
$$

It says that the actual finite matter-geometry law makes the cyclic
three-normal switch operationally invisible to finite metric readouts.

### Proposition 11.6Q: Current-Corpus Status Of The Switch Detector

The current corpus defines the detector but does not prove it is small under
\(\mathbb P_a^{act}\).

Proof.

Papers 5 and 6 supply fixed-background metric readouts and compatible
enriched transports.  Paper 7 introduces normal comparison maps and
residuals.  Papers 8 through 12 build selection, source-response, and
finite-complex criteria.  None of these papers proves that the actual
matter-geometry law makes

$$
{\mathsf Det}_{HHH,a}
$$

small in expectation or with high probability.  Nor do they prove the
opposite floor

$$
\mathbb P_a^{act}({\mathsf Det}_{HHH,a}\ge\delta)\to1.
$$

Therefore the detector is the correct next finite experiment, not a solved
estimate.  `square`

### Verdict 11.6R: Einstein-Feynman Step

The Einstein version is:

$$
\boxed{
\hbox{normal metric response must be the same finite rule that appears in }
HH\to D.
}
$$

The Feynman version is:

$$
\boxed{
\hbox{run the three-normal switch and ask whether metric records can see a
leftover.}
}
$$

They are the same mathematical target.  The live primitive is now the
actual-law switch estimate

$$
\boxed{
\mathrm{V4P12\text{-}THREE\text{-}NORMAL\text{-}SWITCH\text{-}SMALLNESS}
}
$$

or its negative twin, a high-probability switch floor.

### Definition 11.7: Linearized Bianchi Operator

Assume the tested labels carry finite transport operators

$$
\nabla_\alpha:C_a^1\to C_a^1
$$

acting on residual components by the declared finite comparison action.  The
linearized Bianchi operator

$$
D_a^{lin}:C_a^1\to C_a^2
$$

has components

$$
(D_a^{lin}r)_{\alpha\beta\gamma}
:=
\nabla_\alpha r_{\beta\gamma}
+\nabla_\beta r_{\gamma\alpha}
+\nabla_\gamma r_{\alpha\beta}
-r_{[\alpha,\beta]_a,\gamma}
-r_{[\beta,\gamma]_a,\alpha}
-r_{[\gamma,\alpha]_a,\beta},
$$

plus the corresponding covariance-residual components.  Here \(r\) denotes
the vectorized \(DD,DH,HH\) residual slots with a unified label notation.

### Proposition 11.8: Label Jacobi Is Necessary For A True Linear Complex

If the finite label Jacobi defect is not zero, then the formal pure-gauge
operator \(d_a\) built from label variations does not satisfy

$$
D_a^{lin}d_a=0
$$

exactly.  Instead the obstruction is the finite label Jacobi defect.

Proof.

For a pure gauge label perturbation \(\phi\), the coboundary \(d_a\phi\) has
the usual finite bracket form

$$
(d_a\phi)_{\alpha\beta}
=
\nabla_\alpha\phi_\beta-\nabla_\beta\phi_\alpha-\phi_{[\alpha,\beta]_a}.
$$

Applying \(D_a^{lin}\) and collecting cyclic terms leaves precisely the
finite Jacobiator
\({\mathsf Jac}_a(\alpha,\beta,\gamma)\) acting on \(\phi\), plus any
declared transport-defect terms.  Thus \(D_a^{lin}d_a=0\) requires the
tested finite bracket and transport to satisfy Jacobi.  `square`

### Corollary 11.9: First Instantiation Gate

The Paper-7 residuals can instantiate an exact linear residual complex only
on a label sector where

$$
{\mathsf Jac}_a=0
$$

and the finite transport action is compatible with the bracket.  If

$$
\|{\mathsf Jac}_a\|\not\to0,
$$

then the Bianchi-Hodge route cannot close on that sector without quotienting,
enrichment, or changing the finite bracket architecture.

### Definition 11.10: Nonlinear Bianchi Remainder

The raw Paper-7 residuals are multiplicative.  After vectorization, their
exact product Bianchi identity, if present, generally has the form

$$
D_a^{lin}{\mathcal R}_a
=
{\mathcal Q}_a({\mathcal R}_a,{\mathcal R}_a)
+{\mathcal J}_a,
$$

where \({\mathcal Q}_a\) is at least quadratic in the vectorized residuals
and \({\mathcal J}_a\) is the finite label/transport Jacobi defect.

### Theorem 11.11: Absorbable Nonlinear Bianchi Remainder

Assume:

1. the linear residual complex has Hodge gap \(\lambda_a\ge\lambda_*>0\);
2. the codivergence and harmonic controls satisfy

   $$
   \mathbb E_a^{act}\|d_a^*{\mathcal R}_a\|^2
   +\mathbb E_a^{act}\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2
   \to0;
   $$

3. the nonlinear Bianchi remainder obeys

   $$
   \mathbb E_a^{act}\|{\mathcal Q}_a({\mathcal R}_a,{\mathcal R}_a)\|^2
   \le
   \theta_a\,\mathbb E_a^{act}\|{\mathcal R}_a\|^2
   $$

   with \(\theta_a<\lambda_*/4\) eventually;
4. the Jacobi defect satisfies

   $$
   \mathbb E_a^{act}\|{\mathcal J}_a\|^2\to0.
   $$

Then

$$
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
$$

Proof.

By the Hodge estimate,

$$
\|{\mathcal R}_a\|^2
\le
\lambda_*^{-1}
\left(
\|D_a^{lin}{\mathcal R}_a\|^2
+\|d_a^*{\mathcal R}_a\|^2
\right)
+\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2.
$$

Use

$$
D_a^{lin}{\mathcal R}_a
=
{\mathcal Q}_a({\mathcal R}_a,{\mathcal R}_a)+{\mathcal J}_a
$$

and \(\|x+y\|^2\le2\|x\|^2+2\|y\|^2\).  Taking expectations gives

$$
X_a
\le
2\lambda_*^{-1}\theta_a X_a
+2\lambda_*^{-1}\mathbb E\|{\mathcal J}_a\|^2
+\lambda_*^{-1}\mathbb E\|d_a^*{\mathcal R}_a\|^2
+\mathbb E\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2,
$$

where \(X_a=\mathbb E\|{\mathcal R}_a\|^2\).  Since
\(2\lambda_*^{-1}\theta_a<1/2\), absorb the first term into the left side.
The remaining terms tend to zero.  `square`

### Definition 11.12: Codivergence Candidate

A codivergence candidate for the Paper-7 residual vector is a finite adjoint
operator

$$
d_a^*:C_a^1\to C_a^0
$$

whose components measure failure of finite source conservation, admissible
constraint preservation, or stress-response Ward compatibility.  A valid
codivergence candidate must be:

1. defined on the same vectorized residual slots as \(C_a^1\);
2. adjoint to a declared pure-gauge deformation \(d_a:C_a^0\to C_a^1\);
3. finite and record-level;
4. tied to actual-law source-response identities, not merely declared zero.

### Proposition 11.13: Stress Ward Is Not Yet A Codivergence Bound

The Paper-7 stress Ward identity is necessary but does not by itself source

$$
\mathbb E_a^{act}\|d_a^*{\mathcal R}_a\|^2\to0.
$$

Proof.

Paper 7 already proves that stress Ward constrains tangential
source-response but does not determine normal update probabilities or
finite normal/tangential closure.  A codivergence estimate for the full
residual vector must control \(DD,DH,HH\), and covariance residual
components.  The current stress Ward identity does not supply such an
\(L^2\) estimate.  `square`

### Definition 11.14: Harmonic Residual Audit

Given \(D_a^{lin}\) and \(d_a^*\), the harmonic audit computes

$$
{\mathcal H}_a
=
\ker D_a^{lin}\cap\ker d_a^*
$$

and asks whether the actual law controls

$$
\mathbb E_a^{act}
\|\Pi_{{\mathcal H}_a}{\mathcal R}_a\|^2.
$$

The audit has three possible outcomes:

1. \({\mathcal H}_a=0\), so no harmonic residual obstruction exists;
2. \({\mathcal H}_a\ne0\) but actual-law source constraints suppress it;
3. \({\mathcal H}_a\ne0\) and current constraints do not suppress it.

### Proposition 11.15: Nontrivial Harmonic Sector Blocks The Route Unless
Actual Suppression Is Sourced

If there is \(h_a\in{\mathcal H}_a\) with \(\|h_a\|=1\), and the current
actual-law constraints permit residual vectors with a fixed projection onto
\(h_a\), then finite Bianchi-Hodge coercivity is not provable from the
current constraints.

Proof.

For such a residual vector,

$$
D_a^{lin}h_a=0,
\qquad
d_a^*h_a=0,
$$

so Bianchi and codivergence tests do not see it.  Without an additional
actual-law estimate on the harmonic projection, the residual norm can remain
bounded away from zero while all closedness and codivergence defects vanish.
`square`

### Definition 11.16: Hodge Gap Computation

On the non-harmonic sector, define the finite Hodge Laplacian

$$
\Delta_a^{Hodge}
:=
(D_a^{lin})^*D_a^{lin}+d_ad_a^*
$$

acting on \(C_a^1\).  The Hodge gap is

$$
\lambda_a
:=
\min_{\substack{r\perp{\mathcal H}_a\\ \|r\|=1}}
\langle r,\Delta_a^{Hodge}r\rangle.
$$

### Proposition 11.17: Hodge Gap Is A Finite Spectral Problem

Once \(C_a^1\), \(D_a^{lin}\), and \(d_a^*\) are fixed, the Hodge gap is a
finite eigenvalue problem.  No continuum limit or Hilbert ontology is needed
to define it.

Proof.

All spaces are finite-dimensional real inner-product spaces.  The operator
\(\Delta_a^{Hodge}\) is a finite positive semidefinite matrix.  Its first
positive eigenvalue is exactly \(\lambda_a\).  `square`

### Proposition 11.18: Collapsing Hodge Gap Forces A New Regularity Or
Quotient Gate

If

$$
\lambda_a\to0,
$$

then the Bianchi-Hodge route cannot prove residual moment decay unless the
residual sector is restricted, quotient-gauged, or supplemented by a stronger
regularity estimate that compensates for \(\lambda_a^{-1}\).

Proof.

The coercive estimate of Theorem 10.8 contains the factor
\(\lambda_a^{-1}\).  If \(\lambda_a^{-1}\) diverges, the Bianchi and
codivergence defects must vanish faster than the inverse gap grows.  Without
such a rate, no moment decay follows.  `square`

### Theorem 11.19: Paper-7 Residual Complex Conditional Positive Theorem

The Paper-7 residual package proves the Paper-11 positive actual-law route if
all of the following hold:

1. vectorization gate passes;
2. finite label Jacobi/transport defect is zero or \(L^2\)-small;
3. nonlinear Bianchi remainder is absorbable;
4. a codivergence candidate \(d_a^*\) is sourced by actual finite
   source-response/conservation identities;
5. harmonic residual projection is \(L^2\)-small under \(\mathbb P_a^{act}\);
6. the finite Hodge gap is uniformly positive, or the defect rates dominate
   \(\lambda_a^{-1}\);
7. Paper-11 regularity/tail conditions hold.

Then

$$
\mathbb P_a^{act}(Q_a\in{\mathsf G}_a(\epsilon_a))\to1
$$

for some \(\epsilon_a\downarrow0\).

Proof.

Items 1 through 3 construct the Bianchi side
\(D_a^{lin}{\mathcal R}_a\) with small or absorbable defect.  Item 4 gives
codivergence control.  Item 5 removes harmonic residual modes.  Item 6 gives
the coercive Hodge estimate.  Therefore Theorem 10.8, or its nonlinear
absorption form Theorem 11.11, gives
\(\mathbb E_a^{act}[{\mathcal A}_a]\to0\).  Item 7 invokes Paper 11 Theorem
13.12.  `square`

### Theorem 11.20: Current-Corpus Residual Complex Verdict

The current corpus does not yet prove the Paper-7 residual complex positive
theorem unconditionally.

Proof.

The vectorization gate passes conditionally by Proposition 11.3.  But the
remaining gates are not sourced:

1. the finite label Jacobi gate has been reduced to the four explicit
   defects
   \({\mathsf Jac}_{DDD,a}\), \({\mathsf Jac}_{DDH,a}\),
   \({\mathsf Jac}_{DHH,a}\), and \({\mathsf Jac}_{HHH,a}\); the frozen
   enriched sectors close, but the dynamical \(DHH\) and \(HHH\) sectors
   still need actual tangential and normal metric-response estimates;
2. the multiplicative Paper-7 residuals have not been shown to obey an
   absorbable nonlinear Bianchi remainder under the actual law;
3. the Paper-7 stress Ward identity is not a full \(d_a^*{\mathcal R}_a\)
   \(L^2\) codivergence estimate;
4. the harmonic residual sector has not been computed or suppressed;
5. the finite Hodge gap has not been computed or bounded below.

Thus the residual complex route is a precise, testable positive program, but
not a completed theorem in the current corpus.  `square`

### Corollary 11.21: What To Do Next Inside This Route

The next concrete mathematical tasks are:

1. source the three-normal switch estimate
   \({\mathsf Det}_{HHH,a}\to0\) under the actual law, or prove a
   high-probability switch floor;
2. define \(D_a^{lin}\) on the vectorized \(DD,DH,HH,cov\) residual slots;
3. define the adjoint codivergence \(d_a^*\) from finite source-response
   identities;
4. compute \({\mathcal H}_a=\ker D_a^{lin}\cap\ker d_a^*\);
5. compute or bound the first positive eigenvalue of
   \(\Delta_a^{Hodge}\);
6. check whether the nonlinear multiplicative Bianchi remainder is
   absorbable under the actual law.

These are finite, Barandes-aligned tasks.  They are also the first place
where the Einstein-style path can either become a real positive theorem or
fail for a concrete reason.

### Verdict 11.22

The residual-complex instantiation test reduces the positive route to a
finite checklist.  It does not prove Branch V4 positive closure yet, but it
does replace the vague demand for "same-law value information" by a much
more geometric finite problem:

$$
\boxed{
\hbox{Does the Paper-7 residual vector form a finite Hodge complex with
actual-law small Bianchi, codivergence, and harmonic defects?}
}
$$

If yes, Paper 12 has a principled route to residual moment decay.  If no,
the Einstein-style Bianchi-Hodge path is falsified at a specific gate.

## 12. Final Settlement

Paper 12 fully investigates the four Paper-11 primitive routes.  The result
is neither a false optimism theorem nor a dead-end verdict.  It is a precise
map of the remaining mathematical force required.  The final continuation
tests whether the abstract Bianchi-Hodge stack can be instantiated by the
actual Paper-7 residuals.

The positive route with the best first-principles chance is:

$$
\boxed{
\mathrm{finite\ exchange\ covariance}
\Longrightarrow
\mathrm{Bianchi/Ward\ identities}
\Longrightarrow
\mathrm{Hodge/Stein\ coercivity}
\Longrightarrow
\mathbb E_a^{act}[{\mathcal A}_a]\to0.
}
$$

For the Paper-7 residual package, this becomes the finite checklist:

$$
\boxed{
\begin{gathered}
\hbox{vectorize }R_{DD},R_{DH},R_{HH},{\mathcal E}_{cov},\\
\hbox{prove three-normal switch smallness or a switch floor},\\
\hbox{define }D_a^{lin}\hbox{ and }d_a^*,\\
\hbox{control nonlinear Bianchi remainders},\\
\hbox{kill harmonic residual modes},\\
\hbox{and prove a finite Hodge gap.}
\end{gathered}
}
$$

The negative route with the cleanest finite decision procedure is:

$$
\boxed{
\mathrm{finite\ actual\ constraint\ polytope}
\Longrightarrow
\mathrm{LP/Farkas\ floor\ certificate}.
}
$$

The current-corpus status remains:

$$
\boxed{
\mathrm{V4P12\text{-}FOUR\text{-}ROUTE\text{-}UNCONDITIONAL\text{-}CLOSE}^{cur}
\quad\hbox{not proved}.
}
$$

But the attack surface has been reduced.  The next genuinely new theorem
must provide one of:

$$
\boxed{
\begin{gathered}
\hbox{Paper-7 residual-complex instantiation},\\
\hbox{finite Bianchi-Hodge coercivity},\\
\hbox{actual residual-source curvature smallness},\\
\hbox{actual residual Stein coercivity},\\
\hbox{actual same-constraint I-projection},\\
\hbox{actual Fisher residual projection},\\
\hbox{or an LP/Farkas high-probability floor certificate}.
\end{gathered}
}
$$

Among these, the most Barandes-aligned and least comparison-dependent
positive target is now the Paper-7 residual-complex instantiation test.  If
that finite checklist passes, finite Bianchi-Hodge coercivity becomes a real
same-law target rather than an abstract principle stack.  If it fails, the
Einstein-style route fails at a named finite gate.
