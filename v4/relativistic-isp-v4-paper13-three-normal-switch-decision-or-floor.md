# Relativistic ISP V4 Paper 13: Three-Normal Switch Decision Or Floor

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed finite decision framework for the Paper-12 three-normal
switch detector.  The paper proves the conditional positive switch theorem,
the exact weak/strong floor logic, the finite LP/Farkas floor certificate,
the Feynman/Einstein attacks on both positive mechanisms, and the
current-corpus no-source verdict.

## Abstract

Paper 12 turned the \(HHH\) normal-geometry Jacobi obstruction into the
finite three-normal switch detector

$$
{\mathsf Det}_{HHH,a}.
$$

Paper 13 asks the next smallest question:

$$
\boxed{
\hbox{does the actual finite matter-geometry law make the switch invisible,
or is there a switch floor?}
}
$$

The positive target is

$$
\boxed{
\mathbb E_a^{act}{\mathsf Det}_{HHH,a}^2\to0.
}
$$

Under Paper-12 pair closure and tangential naturality, this implies

$$
\mathbb E_a^{act}J_{HHH,a}^2\to0
$$

on the tested normal-label sector.  Therefore it closes the hardest
Step-1 Jacobi gate in the Paper-7 residual-complex route.

The negative target is a floor.  Paper 13 is careful: failure of smallness
does not automatically imply a probability-one floor.  The exact finite
logic is:

1. either the switch moment tends to zero;
2. or there is a weak positive-probability switch floor along a subsequence;
3. and a high-probability switch floor requires an additional
   anti-intermittency, support, or LP/Farkas certificate.

Paper 13 proves two conditional positive mechanisms:

$$
\boxed{
\mathrm{V4P13\text{-}SWITCH\text{-}STEIN\text{-}COERCIVITY}
\Longrightarrow
\mathbb E_a^{act}{\mathsf Det}_{HHH,a}^2\to0
}
$$

and

$$
\boxed{
\mathrm{V4P13\text{-}SWITCH\text{-}EQUIV\text{-}RESPONSE}
\Longrightarrow
\mathbb E_a^{act}{\mathsf Det}_{HHH,a}^2\to0.
}
$$

It also proves the finite negative certificate:

$$
\boxed{
\mathrm{V4P13\text{-}SWITCH\text{-}LP\text{-}FLOOR\text{-}CERTIFICATE}
\Longrightarrow
\mathbb P_a^{act}({\mathsf Det}_{HHH,a}\ge\delta)\to1.
}
$$

The current-corpus verdict is sharp and honest:

$$
\boxed{
\mathrm{V4P13\text{-}THREE\text{-}NORMAL\text{-}SWITCH\text{-}DECISION}^{cur}
\quad\hbox{not proved}.
}
$$

The current corpus defines the switch detector, but it does not yet source
switch Stein coercivity, switch equivalence response, or a switch LP floor
certificate.  Paper 13 therefore reduces the next V4 step to one finite
actual-law theorem rather than another layer of formal algebra.

The two positive mechanisms are attacked in both styles.  The Feynman attack
on Stein is a finite repair graph.  The Einstein attack on Stein is to
derive that repair graph from a normal-response principle rather than
inventing smoothing dynamics.  The Feynman attack on equivalence response is
the minimal switch table.  The Einstein attack on equivalence response is a
single finite normal-response rule for metric readouts and beta shifts.

## 0. Imports And Discipline

### Import 0.1: Actual Finite Law

For each regulator \(a\), the actual finite total-record law is

$$
\mathbb P_a^{act}
$$

on the finite total matter-geometry record space \(\Omega_a\).

### Import 0.2: Normal And Tangential Comparison Maps

From Paper 7, finite lapse labels \(N\) have normal comparison maps

$$
H_a[N]:V_a^{tot}\to V_a^{tot},
$$

and finite tangential labels \(v\) have tangential comparison maps

$$
D_a[v]:V_a^{tot}\to V_a^{tot}.
$$

These are finite operational comparison maps, not Hilbert operators and not
hidden intermediate Markov steps.

### Import 0.3: Metric Readout And Beta Shift

The finite inverse-metric readout is

$$
{\mathsf I}^{ij}_a.
$$

The geometry-dependent tangential shift predicted by a normal-normal pair is

$$
\beta_a(g;N,M)^i
=
{\mathsf I}^{ij}_a(N\partial_jM-M\partial_jN).
$$

### Import 0.4: Paper-12 Switch Detector

For three lapse labels \(N,M,L\), write

$$
B_{ML,a}:=\beta_a(g;M,L).
$$

The corrected normal-tangential switch is

$$
{\mathsf W}_{N|ML,a}
:=
{\mathsf C}(H_a[N],D_a[B_{ML,a}])\,
H_a[{\mathcal L}_{B_{ML,a},a}N],
$$

where

$$
{\mathsf C}(A,B):=ABA^{-1}B^{-1}.
$$

The cyclic switch is

$$
\begin{aligned}
{\mathsf SW}_{HHH,a}(N,M,L)
:={}&
{\mathsf W}_{N|ML,a}\,
{\mathsf W}_{M|LN,a}\,
{\mathsf W}_{L|NM,a}.
\end{aligned}
$$

For a finite metric observable \(G\), the detector value is

$$
{\mathsf Det}_{HHH,a}(N,M,L;G)
:=
\|{\mathsf SW}_{HHH,a}(N,M,L)G-G\|_{{\mathcal O}_a}.
$$

The detector scale is

$$
{\mathsf Det}_{HHH,a}
:=
\sup_{N,M,L,G}{\mathsf Det}_{HHH,a}(N,M,L;G).
$$

When the metric readout depends on the configuration \(q\), this detector is
understood pointwise:

$$
{\mathsf Det}_{HHH,a}(q).
$$

The actual-law question is therefore a finite probabilistic question about
the nonnegative random variable

$$
S_a(q):={\mathsf Det}_{HHH,a}(q)^2.
$$

### Barandes Rule 0.5

Paper 13 may use only finite record laws, finite comparison maps, finite
observables, finite source tilts, finite LP duality, and finite
integration-by-parts identities.

Paper 13 may not use:

1. Einstein equations as assumed dynamics;
2. continuum path integrals;
3. hidden Markov subdivisions inside the indivisible slab law;
4. Hilbert phase as ontology;
5. a hand-declared small-switch law as a substitute for
   \(\mathbb P_a^{act}\).

The rule is:

$$
\boxed{
\hbox{switch smallness must be a theorem about }\mathbb P_a^{act}.
}
$$

## 1. The Exact Finite Decision Problem

### Definition 1.1: Switch-Small Side

The actual finite law is on the switch-small side if

$$
\mathbb E_a^{act}S_a\to0.
$$

Equivalently,

$$
{\mathsf Det}_{HHH,a}\to0
$$

in \(L^2(\mathbb P_a^{act})\).

### Definition 1.2: Weak Switch Floor

There is a weak switch floor if there are \(\delta>0\), \(\rho>0\), and a
subsequence \(a_k\downarrow0\) such that

$$
\mathbb P_{a_k}^{act}(S_{a_k}\ge\delta)\ge\rho.
$$

This says that switch-visible configurations retain positive probability.

### Definition 1.3: High-Probability Switch Floor

There is a high-probability switch floor if there exists \(\delta>0\) such
that

$$
\mathbb P_a^{act}(S_a\ge\delta)\to1.
$$

This is stronger than a weak floor.

### Theorem 1.4: Exact Small-Or-Weak-Floor Dichotomy

Assume \(S_a\ge0\) and the detector family is uniformly integrable under
\(\mathbb P_a^{act}\).  In particular, this holds if the detector is
normalized so that

$$
S_a\le M
$$

with \(M\) independent of \(a\).  If

$$
\mathbb E_a^{act}S_a\not\to0,
$$

then a weak switch floor exists.

Proof.

If the expectation does not tend to zero, there are \(\epsilon>0\) and a
subsequence \(a_k\) such that

$$
\mathbb E_{a_k}^{act}S_{a_k}\ge\epsilon.
$$

If for every \(\delta>0\)

$$
\mathbb P_{a_k}^{act}(S_{a_k}\ge\delta)\to0
$$

along that subsequence, then \(S_{a_k}\to0\) in probability.  Since each
space is finite and the detector family is uniformly integrable, convergence
in probability to zero gives

$$
\mathbb E_{a_k}^{act}S_{a_k}\to0,
$$

contradiction.  Therefore some \(\delta>0\) has nonvanishing upper
probability.  Passing to a further subsequence gives \(\rho>0\).  `square`

### Proposition 1.5: High-Probability Floor Does Not Follow From Failure Of
Smallness

Failure of switch smallness does not imply a high-probability switch floor.

Proof.

Let \(\Omega_a=\{0,1\}\), let \(S_a(0)=0\), \(S_a(1)=1\), and let

$$
\mathbb P_a^{act}(0)=\mathbb P_a^{act}(1)=1/2.
$$

Then

$$
\mathbb E_a^{act}S_a=1/2,
$$

so smallness fails.  But for every \(0<\delta<1\),

$$
\mathbb P_a^{act}(S_a\ge\delta)=1/2,
$$

not \(1\).  `square`

### Verdict 1.6

The honest decision is not binary unless an anti-intermittency principle or
support certificate is added.  The exact finite fork is:

$$
\boxed{
\hbox{small switch}
\quad\hbox{or}\quad
\hbox{weak floor/intermittency}.
}
$$

The high-probability floor is a stronger negative theorem and must be
proved separately.

## 2. Positive Route I: Switch Stein Coercivity

The most direct positive theorem is an \(L^2\) estimate for the switch
vector itself.

### Definition 2.1: Switch Vector

Choose a finite list of normalized switch tests

$$
\tau=(N,M,L,G)
$$

large enough to realize the detector supremum up to the declared regulator
error.  Define the switch vector

$$
{\mathcal S}_a(q)
:=
\left(
{\mathsf SW}_{HHH,a}(N,M,L)G(q)-G(q)
\right)_{\tau}
\in W_a.
$$

Then

$$
S_a(q)\le C_a\|{\mathcal S}_a(q)\|^2
$$

and, when the test list separates the detector,

$$
\|{\mathcal S}_a(q)\|^2\le C'_a S_a(q)
$$

on the tested sector.

### Definition 2.2: Switch Stein Pair

A switch Stein pair consists of:

1. a finite comparison graph \(G_a^{sw}\) on \(\Omega_a\);
2. finite antisymmetric currents \(J_{e,\tau}\);
3. finite differences \(\nabla_e f=f(q')-f(q)\);
4. a switch defect vector \(B_a(q)\);

such that for every finite test function \(f\) and every switch coordinate
\(\tau\),

$$
\mathbb E_a^{act}
\left[
{\mathcal S}_{a,\tau} f
\right]
=
\mathbb E_a^{act}
\left[
\sum_e J_{e,\tau}\nabla_e f
\right]
+
\mathbb E_a^{act}[B_{a,\tau}f].
$$

### Definition 2.3: Switch Stein Coercivity

The switch Stein pair is coercive at scales \(\alpha_a,\beta_a\) if

$$
\mathbb E_a^{act}
\left[
\sum_\tau
\left(\sum_eJ_{e,\tau}\nabla_e f_\tau\right)^2
\right]
\le
\alpha_a
\mathbb E_a^{act}\sum_\tau f_\tau^2
$$

for all finite vector tests \(f_\tau\), and

$$
\mathbb E_a^{act}\|B_a\|^2\le\beta_a.
$$

### Theorem 2.4: Switch Stein Coercivity Implies Switch Smallness

If a switch Stein pair exists with

$$
\alpha_a\to0,
\qquad
\beta_a\to0,
$$

and the detector/test-vector equivalence constants are controlled, then

$$
\mathbb E_a^{act}S_a\to0.
$$

Proof.

Apply the Stein identity with \(f_\tau={\mathcal S}_{a,\tau}\) and sum over
\(\tau\).  By Cauchy-Schwarz and coercivity,

$$
\mathbb E_a^{act}\|{\mathcal S}_a\|^2
\le
\left(\sqrt{\alpha_a}+\sqrt{\beta_a}\right)
\sqrt{\mathbb E_a^{act}\|{\mathcal S}_a\|^2}.
$$

Thus

$$
\mathbb E_a^{act}\|{\mathcal S}_a\|^2
\le
\left(\sqrt{\alpha_a}+\sqrt{\beta_a}\right)^2
\to0.
$$

The detector/test-vector equivalence then gives

$$
\mathbb E_a^{act}S_a\to0.
$$

`square`

### Proposition 2.5: Current-Corpus Stein Status

The current corpus does not construct a switch Stein pair.

Proof.

Papers 7 through 12 define comparison maps, residuals, source-response
functions, and Bianchi-Hodge targets.  They do not construct finite currents
whose integration-by-parts identity returns the three-normal switch vector
\({\mathcal S}_a\), and they do not prove the coercive estimate in
Definition 2.3.  `square`

### Definition 2.6: Feynman Repair Graph For The Switch

The Feynman attack on switch Stein coercivity is to look for the smallest
finite repair move that actually changes a visible switch defect.

A switch repair graph consists of:

1. a finite graph \(E_a^{rep}\) on \(\Omega_a\);
2. edge rates \(c_a(q,q')\ge0\);
3. an exchangeable edge law

   $$
   \mathbb P_a^{act}(q)c_a(q,q')
   =
   \mathbb P_a^{act}(q')c_a(q',q);
   $$

4. a repair drift estimate for the switch vector:

   $$
   \left\|
   \mathbb E[
   {\mathcal S}_a(Q')-{\mathcal S}_a(Q)\mid Q=q]
   +\lambda_a{\mathcal S}_a(q)
   \right\|
   \le b_a(q);
   $$

5. a finite jump-energy estimate

   $$
   \mathbb E\|{\mathcal S}_a(Q')-{\mathcal S}_a(Q)\|^2
   \le e_a.
   $$

Here \(Q\sim\mathbb P_a^{act}\), and \(Q'\) is sampled from the repair edge
law conditional on \(Q\).

Plainly: the graph contains the finite moves that would repair a cyclic
normal-switch defect, and the drift says the repair move points back toward
zero switch.

### Theorem 2.7: Repair Graph Criterion For Switch Moment Smallness

Assume a switch repair graph exists with

$$
\lambda_a\ge\lambda_*>0,
\qquad
\mathbb E_a^{act}b_a(Q)^2\to0,
\qquad
e_a\to0.
$$

Then

$$
\mathbb E_a^{act}\|{\mathcal S}_a\|^2\to0.
$$

Consequently, if the switch vector and switch detector are equivalent on
the tested sector, then

$$
\mathbb E_a^{act}S_a\to0.
$$

Proof.

By exchangeability,

$$
\mathbb E
\langle
{\mathcal S}_a(Q),
{\mathcal S}_a(Q')-{\mathcal S}_a(Q)
\rangle
=
-\frac12
\mathbb E\|
{\mathcal S}_a(Q')-{\mathcal S}_a(Q)
\|^2.
$$

Using the repair drift,

$$
\begin{aligned}
\lambda_a
\mathbb E\|{\mathcal S}_a(Q)\|^2
&\le
\frac12
\mathbb E\|
{\mathcal S}_a(Q')-{\mathcal S}_a(Q)
\|^2\\
&\quad+
\mathbb E\|{\mathcal S}_a(Q)\|\,b_a(Q).
\end{aligned}
$$

Let

$$
X_a:=\sqrt{\mathbb E\|{\mathcal S}_a\|^2}.
$$

Then

$$
\lambda_*X_a^2
\le
\frac12e_a
+X_a\sqrt{\mathbb E b_a^2}.
$$

Since \(e_a\to0\) and \(\mathbb E b_a^2\to0\), this forces

$$
X_a\to0.
$$

`square`

### Proposition 2.8: Repair Graph Implies A Switch Stein Pair

A switch repair graph satisfying Definition 2.6 canonically produces a
finite switch Stein pair with defect controlled by \(b_a\) and jump energy
controlled by \(e_a\).

Proof.

For an oriented edge \(e=(q,q')\), define

$$
\nabla_e f=f(q')-f(q).
$$

Use the exchangeable edge measure

$$
\mu_a(q,q'):=\mathbb P_a^{act}(q)c_a(q,q')
$$

and set the current in switch coordinate \(\tau\) to be the finite
antisymmetric edge observable induced by

$$
{\mathcal S}_{a,\tau}(q')-{\mathcal S}_{a,\tau}(q).
$$

The drift identity in Definition 2.6 is exactly the finite
integration-by-parts identity for \({\mathcal S}_{a,\tau}\), with residual
defect \(b_a\).  The jump-energy estimate supplies the small current term
needed in Theorem 2.4.  `square`

### Proposition 2.9: The Tiny Repair Countertest

If the actual law admits two switch-visible record states \(q_0,q_1\) with

$$
{\mathcal S}_a(q_0)=0,
\qquad
\|{\mathcal S}_a(q_1)\|\ge c>0,
$$

and if the current-corpus constraints allow

$$
\mathbb P_a^{act}(q_1)\ge\rho>0
$$

without any repair edge whose drift points from \(q_1\) toward smaller
switch, then switch Stein coercivity cannot be proved from those
constraints.

Proof.

On \(q_1\), the switch vector is bounded away from zero.  If no allowed
repair edge produces negative drift in the switch direction, then the drift
condition in Definition 2.6 fails with \(b_a\) bounded away from zero on a
set of probability at least \(\rho\).  Hence

$$
\mathbb E b_a^2\nrightarrow0.
$$

The repair-graph criterion and the associated Stein pair cannot be sourced
from the current constraints.  `square`

### Verdict 2.10: Feynman And Einstein Attacks On Stein

The Feynman attack on switch Stein coercivity is:

$$
\boxed{
\hbox{find the finite repair move that reduces a visible switch defect.}
}
$$

The Einstein attack is:

$$
\boxed{
\hbox{derive that repair move from the finite normal-response principle,
not from an invented smoothing dynamics.}
}
$$

Thus the next Stein subproblem is concrete.  Either construct a
Barandes-aligned repair graph with contraction and small jump energy, or
produce a tiny repair countertest showing that the current constraints allow
switch-visible states with no restoring finite move.

## 3. Positive Route II: Finite Equivalence Response

The Einstein-style route is not to estimate the switch after the fact, but
to make it impossible by a finite response principle.

### Definition 3.1: Switch Equivalence Response

The actual law satisfies switch equivalence response at scale \(\epsilon_a\)
if, for every normalized triple \(N,M,L\) and every normalized metric readout
\(G\),

$$
\mathbb E_a^{act}
\left[
\left\|
{\mathsf W}_{N|ML,a}
{\mathsf W}_{M|LN,a}
{\mathsf W}_{L|NM,a}G-G
\right\|_{{\mathcal O}_a}^2
\right]
\le
\epsilon_a.
$$

This is exactly the finite statement that the metric response under a normal
comparison is the same response that is required by the \(HH\to D\) bracket,
tested cyclically.

### Theorem 3.2: Equivalence Response Is Exactly Switch Smallness

If switch equivalence response holds with \(\epsilon_a\to0\), and the tested
metric readouts realize the detector supremum up to \(o(1)\), then

$$
\mathbb E_a^{act}S_a\to0.
$$

Proof.

The left side in Definition 3.1 is exactly the square of each switch
detector coordinate.  Taking the finite supremum over the detector test
family and using the declared approximation of the supremum gives the
claim.  `square`

### Proposition 3.3: Dynamical Covariance Alone Does Not Give Switch
Equivalence Response

Paper-7 dynamical covariance of individual normal comparison maps does not
imply switch equivalence response.

Proof.

Dynamical covariance compares

$$
\Gamma_a^{tot}H_a[N]
\quad\hbox{with}\quad
H_{a'}[N']\Gamma_a^{tot}.
$$

This is a projective compatibility statement for one normal comparison at a
time.  The switch detector is a cyclic statement about commutators of
normal and tangential comparison maps:

$$
{\mathsf C}(H_a[N],D_a[\beta_a(g;M,L)]).
$$

One-map projective compatibility does not determine these commutators.  In a
finite-dimensional vector space, one may choose comparison maps that are
separately projectively compatible with \(\Gamma_a^{tot}=I\) but whose
commutator is nontrivial on metric observables.  Thus the covariance axiom
does not logically imply switch smallness.  `square`

### Proposition 3.4: Stress Ward Alone Does Not Give Switch Equivalence
Response

The finite stress-response Ward identity does not by itself imply switch
smallness.

Proof.

Stress Ward identities constrain first source responses.  The switch
detector is a cyclic second/third comparison response involving normal
metric motion through the geometry-dependent \(\beta\) structure function.
As in Paper 12's centered residual example, a first-response identity can
hold while a quadratic detector has positive expectation.  Therefore stress
Ward is necessary for a GR-like law but not sufficient for
\(\mathbb E_a^{act}S_a\to0\).  `square`

### Definition 3.5: Feynman Minimal Switch Table

The Feynman attack on switch equivalence response is to reduce the
principle to the smallest finite table that can falsify it.

A minimal switch table consists of:

1. a finite metric-record alphabet \(X_a^{met}\);
2. one separating metric readout \(G:X_a^{met}\to\mathbb R\);
3. three lapse labels \(N,M,L\);
4. the three finite switches

   $$
   {\mathsf W}_{N|ML,a},
   \qquad
   {\mathsf W}_{M|LN,a},
   \qquad
   {\mathsf W}_{L|NM,a};
   $$

5. the cyclic product

   $$
   {\mathsf SW}_{HHH,a}
   =
   {\mathsf W}_{N|ML,a}
   {\mathsf W}_{M|LN,a}
   {\mathsf W}_{L|NM,a}.
   $$

The table passes if

$$
{\mathsf SW}_{HHH,a}G=G.
$$

It fails if

$$
\|{\mathsf SW}_{HHH,a}G-G\|_{{\mathcal O}_a}>0.
$$

### Proposition 3.6: Two-State Switch Falsifier

Switch equivalence response is not a consequence of finite comparison maps
alone.

Proof.

Let the metric alphabet be

$$
X^{met}=\{0,1\},
$$

and let

$$
G(x)=x.
$$

Choose finite comparison maps so that

$$
{\mathsf W}_{N|ML}=T,
\qquad
{\mathsf W}_{M|LN}=I,
\qquad
{\mathsf W}_{L|NM}=I,
$$

where \(T(0)=1\) and \(T(1)=0\).  Then

$$
{\mathsf SW}_{HHH}=T
$$

and

$$
\|{\mathsf SW}_{HHH}G-G\|>0.
$$

All objects are finite.  Thus the mere existence of \(H\), \(D\), \(\beta\),
and metric readouts does not force equivalence response.  A new compatibility
principle is needed.  `square`

### Definition 3.7: Finite Single-Rule Normal Response

The Einstein attack is to require that the normal response of the metric
readout and the normal response of the \(HH\to D\) beta shift are one finite
rule.

A finite single-rule normal response consists of maps

$$
{\mathfrak R}_{N,a}
$$

on the algebra generated by tested metric readouts, lapse labels, and beta
shifts such that:

1. on metric readouts,

   $$
   {\mathfrak R}_{N,a}{\mathsf I}^{ij}_a
   =
   H_a[N]{\mathsf I}^{ij}_a;
   $$

2. on beta shifts,

   $$
   {\mathfrak R}_{N,a}\beta_a(g;M,L)
   =
   \beta_a({\mathfrak R}_{N,a}g;M,L)
   $$

   up to regulator error;

3. on the normal-tangential switch,

   $$
   {\mathsf C}(H_a[N],D_a[\beta_a(g;M,L)])
   =
   H_a[-{\mathcal L}_{\beta_a(g;M,L),a}N]
   +E_{N|ML,a}
   $$

   on tested metric observables;

4. the cyclic product error satisfies

   $$
   \mathbb E_a^{act}
   \left\|
   (I+E_{N|ML,a})(I+E_{M|LN,a})(I+E_{L|NM,a})-I
   \right\|_{{\mathcal G}^{met}_a}^2
   \to0.
   $$

### Theorem 3.8: Single-Rule Normal Response Implies Switch Equivalence

If a finite single-rule normal response exists, then switch equivalence
response holds.

Proof.

The corrected switch

$$
{\mathsf W}_{N|ML,a}
$$

is the product of the normal-tangential commutator and the predicted inverse
normal label.  By item 3 in Definition 3.7, its action on metric observables
is

$$
I+E_{N|ML,a}
$$

up to regulator error.  Therefore the cyclic product is

$$
(I+E_{N|ML,a})(I+E_{M|LN,a})(I+E_{L|NM,a}),
$$

again up to regulator error.  Item 4 says exactly that this cyclic product
acts trivially on metric observables in \(L^2(\mathbb P_a^{act})\).  This is
switch equivalence response.  `square`

### Proposition 3.9: Relation Between Equivalence Response And Stein

Finite single-rule normal response is stronger than switch Stein coercivity
as a geometric principle, but it can source the repair graph used by the
Stein route.

Proof.

If the single-rule response holds, the defect \({\mathcal S}_a(q)\) measures
failure from that response rule.  A finite repair move can be chosen as the
operation that replaces the metric-response entry in \(q\) by the
single-rule response entry, when such replacement is an admissible finite
record move.  That move points toward smaller switch by construction.  Thus
the Einstein principle can generate the Feynman repair graph.  Without the
principle, the repair graph has no geometric source and would be an invented
smoothing dynamics.  `square`

### Verdict 3.10: Feynman And Einstein Attacks On Equivalence Response

The Feynman attack on equivalence response is:

$$
\boxed{
\hbox{build the minimal switch table and see whether the cyclic product
is forced to be identity.}
}
$$

The Einstein attack is:

$$
\boxed{
\hbox{source and prove one finite normal-response rule for metric
readouts and beta shifts.}
}
$$

The two-state switch table shows that finite comparison maps alone do not
force equivalence response.  The single-rule normal response would force it,
and would also explain the Stein repair graph.  The current corpus does not
yet prove that single-rule response.

### Theorem 3.11: Single-Rule Response Is The First Positive Target

Within the positive side of Paper 13, the single-rule normal-response route
strictly precedes the repair-graph route in explanatory strength:

$$
\boxed{
\mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}
\Longrightarrow
\mathrm{V4P13\text{-}SWITCH\text{-}EQUIV\text{-}RESPONSE}
\Longrightarrow
\mathrm{V4P13\text{-}THREE\text{-}NORMAL\text{-}SWITCH\text{-}SMALLNESS}.
}
$$

If, in addition, the single-rule response replacement is an admissible
finite record move and can be made exchangeable under
\(\mathbb P_a^{act}\), then

$$
\boxed{
\mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}
\Longrightarrow
\mathrm{V4P13\text{-}SWITCH\text{-}REPAIR\text{-}GRAPH}.
}
$$

The converse implication is false in general: a repair graph can express
statistical relaxation of switch defects without identifying the normal
metric response and the \(HH\to D\) beta response as one finite rule.

Proof.

The first implication is Theorem 3.8.  The second is Theorem 3.2.  The
repair implication is Proposition 3.9 plus the additional admissibility and
exchangeability hypotheses needed to make the replacement move into a
Barandes-aligned finite repair edge.

For non-converse, take a finite system with a switch variable \(S(q)\) and a
reversible repair graph whose drift contracts \(S\).  Such a graph can be
defined using only the scalar value of \(S\), without specifying how
\({\mathsf I}^{ij}_a\), \(\beta_a(g;N,M)\), and the normal comparison maps
share one response rule.  It may prove an analytic relaxation estimate, but
it does not reconstruct the geometric identity required by Definition 3.7.
`square`

### Corollary 3.12: Priority Rule

The next positive attack should begin with

$$
\boxed{
\mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}.
}
$$

The repair graph should be pursued next only as:

1. a corollary of single-rule response;
2. a fallback if single-rule response is too strong;
3. or a negative diagnostic via the tiny repair countertest.

### Protocol 3.13: Einstein-Feynman Attack Order

The positive side of Paper 13 must be attacked in the following order.

1. First attack

   $$
   \mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}.
   $$

   This is the geometric principle: the normal response of metric readouts
   and the normal response of the \(HH\to D\) beta shift are one finite
   rule.

2. Use the Feynman minimal switch table to test or falsify the proposed
   rule.  The immediate finite question is:

   $$
   {\mathsf SW}_{HHH,a}G=G
   $$

   for the smallest separating metric alphabet and tested normal labels.

3. If the single-rule response survives the minimal table and is sourced
   under \(\mathbb P_a^{act}\), derive

   $$
   \mathrm{V4P13\text{-}THREE\text{-}NORMAL\text{-}SWITCH\text{-}SMALLNESS}
   $$

   by Theorem 3.8 and Theorem 3.2.

4. Then derive

   $$
   \mathrm{V4P13\text{-}SWITCH\text{-}REPAIR\text{-}GRAPH}
   $$

   as an analytic corollary, using Proposition 3.9 and the admissibility of
   the single-rule replacement move.

5. Attack the repair graph directly only if the single-rule response is
   falsified, too strong, or not yet sourceable.  In that case the repair
   graph is a fallback analytic mechanism, and the tiny repair countertest
   is the first falsification check.

This is both the Einstein order and the Feynman order.  Einstein starts with
the unifying finite response rule.  Feynman immediately tests that rule on
the smallest switch table.  Neither starts with an abstract repair graph
unless the geometric rule fails.

### Theorem 3.14: Protocol Correctness

Protocol 3.13 is the strongest positive attack order available in Paper 13.

Proof.

The single-rule normal response implies switch equivalence response by
Theorem 3.8, and switch equivalence response implies switch smallness by
Theorem 3.2.  Under admissibility and exchangeability of the replacement
move, the same single-rule response sources the repair graph by Proposition
3.9.  Thus the single-rule route implies both positive mechanisms.

The reverse implication from repair graph to single-rule response is false
by Theorem 3.11.  Therefore beginning with the repair graph would start from
the weaker and less geometric object.  The minimal switch table is the
correct immediate falsification test because Proposition 3.6 shows that
finite comparison maps alone can fail it.  Hence the stated order is the
least indirect positive route and the sharpest falsification route.  `square`

### Definition 3.15: Minimal Single-Rule Table

The minimal single-rule table for a triple \(N,M,L\) and a separating metric
readout \(G\) consists of:

1. the three corrected switch factors

   $$
   {\mathsf W}_{N|ML,a},
   \qquad
   {\mathsf W}_{M|LN,a},
   \qquad
   {\mathsf W}_{L|NM,a};
   $$

2. their metric-visible error operators \(E_{N|ML,a}\), \(E_{M|LN,a}\),
   \(E_{L|NM,a}\), defined by

   $$
   {\mathsf W}_{N|ML,a}G
   =
   (I+E_{N|ML,a})G
   $$

   and cyclically;

3. the cyclic error operator

   $$
   {\mathsf E}^{cyc}_{NML,a}
   :=
   (I+E_{N|ML,a})(I+E_{M|LN,a})(I+E_{L|NM,a})-I.
   $$

The table is switch-flat on \(G\) if

$$
{\mathsf E}^{cyc}_{NML,a}G=0.
$$

It is switch-small at scale \(\epsilon_a\) if

$$
\mathbb E_a^{act}
\|{\mathsf E}^{cyc}_{NML,a}G\|_{{\mathcal O}_a}^2
\le\epsilon_a
$$

for every tested triple and metric readout.

### Theorem 3.16: Minimal Table Pass/Fail Criterion

For the minimal single-rule table,

$$
{\mathsf SW}_{HHH,a}G=G
$$

if and only if

$$
{\mathsf E}^{cyc}_{NML,a}G=0.
$$

Similarly,

$$
\mathbb E_a^{act}S_a\to0
$$

follows if the cyclic error is switch-small uniformly over the finite
detector test family.

Proof.

By definition,

$$
{\mathsf SW}_{HHH,a}
=
{\mathsf W}_{N|ML,a}
{\mathsf W}_{M|LN,a}
{\mathsf W}_{L|NM,a}.
$$

On the tested readout \(G\), each factor is \(I+E\).  Therefore

$$
{\mathsf SW}_{HHH,a}G-G
=
{\mathsf E}^{cyc}_{NML,a}G.
$$

The pointwise equivalence follows.  The \(L^2\) statement follows by taking
the finite supremum over the detector family.  `square`

### Corollary 3.17: Exact Cyclic Flatness Is The Weakest Table Condition

On the minimal table, the weakest condition that forces switch invisibility
on the tested readout is cyclic flatness:

$$
\boxed{
{\mathsf E}^{cyc}_{NML,a}G=0.
}
$$

Full single-rule normal response is a geometric source of cyclic flatness,
but cyclic flatness itself is weaker: it only asks that the cyclic product
act trivially on tested metric readouts.

Proof.

Theorem 3.16 says cyclic flatness is equivalent to the table passing.  Any
weaker condition would permit some table with
\({\mathsf E}^{cyc}_{NML,a}G\ne0\), and then the switch detector sees a
leftover.  Full single-rule response implies cyclic flatness by Theorem
3.8, but it also requires one finite response rule for metric readouts and
beta shifts, so it contains more information than the table identity alone.
`square`

### Proposition 3.18: Cyclic Flatness Rules Out The Two-State Falsifier

The two-state switch falsifier of Proposition 3.6 fails precisely because it
violates cyclic flatness.

Proof.

In the falsifier,

$$
{\mathsf W}_{N|ML}=T,
\qquad
{\mathsf W}_{M|LN}=I,
\qquad
{\mathsf W}_{L|NM}=I.
$$

Hence

$$
{\mathsf SW}_{HHH}=T.
$$

Since \(G(0)=0\) and \(G(1)=1\), the flip \(T\) does not fix \(G\).  Thus

$$
{\mathsf E}^{cyc}_{NML}G=(T-I)G\ne0.
$$

Therefore cyclic flatness is exactly the missing condition in the tiny
counterexample.  `square`

### Theorem 3.19: Single-Rule Response Is The Natural Geometric Source Of
Cyclic Flatness

The hierarchy of conditions on the positive side is:

$$
\boxed{
\mathrm{single\text{-}rule\ normal\ response}
\Longrightarrow
\mathrm{cyclic\ flatness}
\Longleftrightarrow
\mathrm{minimal\ switch\ table\ passes}.
}
$$

The first implication is geometric.  The equivalence is table-theoretic.

Proof.

Single-rule normal response identifies the metric response under a normal
comparison with the response of the \(\beta\)-shift entering \(HH\to D\).
By Theorem 3.8, the corrected cyclic product is then identity on tested
metric readouts up to the declared \(L^2\) error.  This is cyclic flatness.
The equivalence between cyclic flatness and the minimal table passing is
Theorem 3.16.  `square`

### Verdict 3.20: What The Minimal Table Teaches

The exact minimal condition for the detector is cyclic flatness:

$$
\boxed{
{\mathsf E}^{cyc}_{NML,a}G=0.
}
$$

But cyclic flatness by itself is just the detector equation.  It is not yet
a dynamical principle.  The best geometric source remains:

$$
\boxed{
\mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}.
}
$$

Thus the next positive theorem should not merely declare cyclic flatness.
It should prove cyclic flatness from one finite normal-response rule.

### Definition 3.21: The Four Source Subgates For Single-Rule Response

To attack the single-rule normal response without smuggling in GR, split it
into four finite same-law subgates.

The first is metric-readout functoriality:

$$
\mathrm{V4P13\text{-}SR\text{-}METRIC\text{-}FUNCTORIALITY}.
$$

It asks for one finite response operator \({\mathfrak R}_{N,a}\) such that,
on tested inverse-metric readouts,

$$
{\mathfrak R}_{N,a}{\mathsf I}^{ij}_a
=
H_a[N]{\mathsf I}^{ij}_a
+o_a(1)
$$

in \(L^2(\mathbb P_a^{act})\).

The second is beta naturality:

$$
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}.
$$

It asks that the same response operator commute with the finite
metric-dependent structure function:

$$
{\mathfrak R}_{N,a}\beta_a(g;M,L)
=
\beta_a({\mathfrak R}_{N,a}g;M,L)
+o_a(1)
$$

in the tested tangential vector record norm.

The third is the normal-tangential commutator law:

$$
\mathrm{V4P13\text{-}SR\text{-}HD\text{-}COMMUTATOR}.
$$

It asks that the finite normal comparison and the finite tangential
comparison obey the GR deformation identity on metric observables:

$$
{\mathsf C}(H_a[N],D_a[\beta_a(g;M,L)])
=
H_a[-{\mathcal L}_{\beta_a(g;M,L),a}N]
+E_{N|ML,a}
$$

with the cyclic product defect

$$
\left\|
(I+E_{N|ML,a})(I+E_{M|LN,a})(I+E_{L|NM,a})-I
\right\|_{{\mathcal G}^{met}_a}
\to0
$$

in \(L^2(\mathbb P_a^{act})\).

The fourth is actual-law support:

$$
\mathrm{V4P13\text{-}SR\text{-}ACTUAL\text{-}SUPPORT}.
$$

It asks that the record states carrying the three preceding identities have
probability tending to one under the actual finite ISP law:

$$
\mathbb P_a^{act}
\left(
\mathrm{SR\text{-}METRIC}
\cap
\mathrm{SR\text{-}BETA}
\cap
\mathrm{SR\text{-}HD}
\right)
\to1.
$$

### Theorem 3.22: Source Audit Necessity And Sufficiency

The four subgates in Definition 3.21 imply

$$
\mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}.
$$

Conversely, any proof of single-rule normal response which remains
Barandes-aligned must source, explicitly or implicitly, beta naturality, the
normal-tangential commutator law, and actual-law support.  Metric
functoriality alone is insufficient.

Proof.

Metric-readout functoriality gives a finite candidate for the normal
response on the readouts that define the detector.  Beta naturality says the
same rule also transports the metric-dependent vector

$$
\beta_a(g;M,L)=I_a(g)^{ij}(M\partial_jL-L\partial_jM).
$$

The normal-tangential commutator law then identifies the discrepancy between
normal response and the \(HH\to D\) beta shift with the explicit residual
operators \(E_{N|ML,a}\).  The cyclic product bound on those residuals is
exactly the \(L^2\) form of cyclic flatness from Definition 3.15 and
Theorem 3.16.  Actual-law support upgrades the pointwise/table identity to
the same-law statement under \(\mathbb P_a^{act}\).  Therefore the
single-rule response holds.

For the converse, note what each missing piece permits.  Without beta
naturality, the normal response can move inverse-metric readouts while the
structure function \(\beta_a\) is updated by an unrelated rule.  Without the
\(HD\) commutator, separately meaningful \(H_a[N]\) and \(D_a[X]\) maps can
still have the wrong finite commutator on metric readouts.  Without
actual-law support, an identity may hold on an auxiliary or selected table
while the actual record law places mass on violating states.  These are
precisely the no-smuggling exclusions required by the Barandes-style
finite-record ontology.  `square`

### Proposition 3.23: What The Current V4 Corpus Actually Sources

The current corpus sources only the weakest part of Definition 3.21:
metric readout functoriality as a notation for how a declared normal
comparison acts on tested metric observables.  It does not yet source beta
naturality, the \(HD\) commutator law, or actual-law support.

Proof.

Papers 5 and 6 show that finite records can carry metric data and that
fixed-background metric readouts can be made operationally meaningful.  That
supports the existence of finite metric observables
\({\mathsf I}^{ij}_a\) and finite normal comparison maps acting on them.
It does not determine how the metric-dependent beta shift must transform.
Indeed, Paper 6 explicitly leaves open many geometry dynamics with the same
metric readouts.

Paper 7 supplies finite tangential comparison maps \(D_a[X]\), finite normal
comparison maps \(H_a[N]\), and projective compatibility for individual
normal maps.  But projective compatibility for one map at a time is not a
commutator identity.  The switch detector requires the mixed law

$$
{\mathsf C}(H_a[N],D_a[\beta_a(g;M,L)])
=
H_a[-{\mathcal L}_{\beta_a(g;M,L),a}N]
+E_{N|ML,a},
$$

and this is not proved by one-map covariance.

Finally, none of Papers 5-12 proves that the actual finite law
\(\mathbb P_a^{act}\) concentrates on the records satisfying these
single-rule identities.  Reset/random-walk diagnostic kernels and tiny
switch tables remain allowed unless a switch-relevant same-law axiom or
theorem excludes them.  Hence the current corpus does not prove the full
single-rule response.  `square`

### Corollary 3.24: The Exact Missing Primitive

The positive Paper-13 route has now been reduced to the following primitive
same-law theorem:

$$
\boxed{
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}
\quad+\quad
\mathrm{V4P13\text{-}SR\text{-}HD\text{-}COMMUTATOR}
\quad+\quad
\mathrm{V4P13\text{-}SR\text{-}ACTUAL\text{-}SUPPORT}.
}
$$

Metric-readout functoriality is not the bottleneck.  The bottleneck is
whether the actual finite geometry law uses one response rule for metric
readouts, beta shifts, and normal-tangential commutators, with high
probability.

### Proposition 3.25: Minimal Falsification Table For The Source Audit

The source audit can be falsified by a three-entry table.

Let \(X_a^{met}=\{0,1\}\), let \(G(0)=0\), \(G(1)=1\), and let a normal
response candidate satisfy

$$
{\mathfrak R}_{N,a}G=G.
$$

Let the beta record \(B\) have two values \(b_0,b_1\), and define a beta
update rule which flips \(B\) while fixing \(G\):

$$
{\mathfrak R}_{N,a}B=b_{1-B}.
$$

Then metric functoriality holds on \(G\), but beta naturality fails unless
\(\beta_a(G;M,L)\) is insensitive to the flip.  If, in addition, the finite
\(D\)-move reads \(B\), the cyclic switch can be nontrivial while all metric
readouts appear individually well-defined.

Proof.

The table fixes \(G\) under \({\mathfrak R}_{N,a}\), so metric functoriality
on the tested metric observable is satisfied.  But beta naturality compares
the response of the beta record with the beta built from the responded
metric:

$$
{\mathfrak R}_{N,a}\beta_a(G;M,L)
\quad\hbox{against}\quad
\beta_a({\mathfrak R}_{N,a}G;M,L).
$$

The right side equals \(\beta_a(G;M,L)\), while the left side flips the beta
record.  Thus the two disagree.  Since the \(D\)-move uses the beta record,
the switch product may fail even though individual metric response looks
harmless.  This is the smallest table showing why beta naturality cannot be
skipped.  `square`

### Verdict 3.26: Source Audit Result

The next positive attack is no longer vague.  It is not:

$$
\hbox{prove that the switch is small.}
$$

It is:

$$
\boxed{
\hbox{prove that the actual finite geometry law carries one normal-response
rule through metric readouts, beta shifts, and \(HD\) commutators.}
}
$$

If that succeeds, single-rule normal response follows, cyclic flatness
follows, and three-normal switch smallness follows.  If it fails on the
minimal table, the positive route must move to the repair graph or the
negative LP/Farkas floor certificate.

### Definition 3.27: Minimal Beta-Naturality Decision Table

The first Feynman test of the source audit is the smallest table that can
decide whether beta is a derived metric response or an independent channel.

Fix lapse labels \(M,L\).  Let

$$
C_{ML,a,j}:=M_a\nabla_{a,j}L_a-L_a\nabla_{a,j}M_a
$$

be the finite label-covector determined by the chosen finite derivative
stencil.  Let \(J_a\) denote the finite metric-jet record needed to read the
inverse metric \(I_a^{ij}\).  Define the finite beta map

$$
{\mathsf B}_{ML,a}(J_a)^i
:=
I_a^{ij}(J_a)C_{ML,a,j}.
$$

A beta table consists of:

1. a finite metric-jet alphabet \(X_a^J\);
2. a finite beta alphabet \(X_a^\beta\);
3. a stored beta record \(B_{ML,a}:X_a^J\times X_a^\beta\to X_a^\beta\);
4. a normal response on metric jets,

   $$
   {\mathfrak R}_{N,a}^J:X_a^J\to X_a^J;
   $$

5. a normal response on stored beta records,

   $$
   {\mathfrak R}_{N,a}^\beta:X_a^\beta\to X_a^\beta.
   $$

The beta-naturality defect is

$$
\Delta^\beta_{N|ML,a}(q)
:=
{\mathfrak R}_{N,a}^\beta B_{ML,a}(q)
-
{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^J J_a(q)).
$$

The beta subgate holds if

$$
\mathbb E_a^{act}
\|\Delta^\beta_{N|ML,a}\|^2
\to0
$$

uniformly over the tested lapse triples.

### Proposition 3.28: Feynman Break Table For Beta Naturality

Metric-readout functoriality alone does not imply beta naturality.

Proof.

Choose a one-point metric-jet alphabet \(X_a^J=\{J_*\}\).  Let

$$
b_*:={\mathsf B}_{ML,a}(J_*).
$$

Choose two beta values \(b_*,b_1\) with

$$
\|b_1-b_*\|=c>0.
$$

Let the metric-jet response be the identity,

$$
{\mathfrak R}_{N,a}^J J_*=J_*,
$$

and let the beta response flip the stored beta value:

$$
{\mathfrak R}_{N,a}^\beta b_*=b_1.
$$

Put the actual-law mass on the record \(q_*=(J_*,b_*)\).  Then all metric
readouts are preserved by the normal response, so metric functoriality holds
on this table.  But

$$
\Delta^\beta_{N|ML,a}(q_*)
=
b_1-{\mathsf B}_{ML,a}(J_*)
=
b_1-b_*,
$$

and therefore

$$
\mathbb E_a^{act}\|\Delta^\beta_{N|ML,a}\|^2=c^2.
$$

Thus beta naturality is falsified while metric-readout functoriality remains
true.  `square`

### Corollary 3.29: The No-Go/Floor Meaning Of The Break Table

If the current-corpus constraint polytope permits the break table of
Proposition 3.28 with probability at least \(\rho>0\), then the current
corpus cannot prove

$$
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}.
$$

Moreover, if the tangential comparison reads beta with switch sensitivity
\(\sigma>0\), in the sense that the switch detector satisfies

$$
S_a(q)
\ge
\sigma\|\Delta^\beta_{N|ML,a}(q)\|^2-r_a(q)
$$

with \(\mathbb E_a^{act}r_a^+\to0\), then the same table gives the switch
floor

$$
\liminf_a\mathbb E_a^{act}S_a
\ge
\rho\sigma c^2.
$$

Proof.

The first claim is immediate from Proposition 3.28: a law satisfying all
current constraints but having beta defect \(c\) on probability \(\rho\)
prevents any derivation of \(L^2\)-small beta defect from those constraints.

For the second claim, integrate the displayed sensitivity inequality:

$$
\mathbb E_a^{act}S_a
\ge
\sigma\mathbb E_a^{act}\|\Delta^\beta_{N|ML,a}\|^2
-\mathbb E_a^{act}r_a^+.
$$

The break table contributes at least \(\rho c^2\) to the beta-defect
second moment.  Letting \(a\) tend to the continuum scale gives the floor.
`square`

### Definition 3.30: Einstein Metric-Jet Beta Lock

The Einstein repair of the break table is not to add a new beta axiom.  It
is to refuse the independent beta channel.

The actual law satisfies metric-jet beta lock at error \(\eta_a\) if there
is a finite metric-jet record \(J_a\) such that, with
\(\mathbb P_a^{act}\)-probability at least \(1-\eta_a\),

$$
B_{ML,a}(q)
=
{\mathsf B}_{ML,a}(J_a(q))
$$

and the normal response preserves this graph:

$$
{\mathfrak R}_{N,a}^\beta B_{ML,a}(q)
=
{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^J J_a(q))
+e^\beta_{N|ML,a}(q),
$$

where

$$
\mathbb E_a^{act}\|e^\beta_{N|ML,a}\|^2\le\eta_a.
$$

This is a finite-record statement.  It says that beta is not a hidden
continuum object and not an independent stochastic update.  It is the
finite readout obtained from the same metric-jet record that supplies the
inverse metric.

### Theorem 3.31: Metric-Jet Beta Lock Implies Beta Naturality

If metric-jet beta lock holds with \(\eta_a\to0\), and the beta alphabet is
uniformly bounded in the tested norm, then

$$
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}
$$

holds.

Proof.

Let \(G_a\) be the high-probability event on which the stored beta record is
the graph readout of the metric jet and the response preserves the graph.
On \(G_a\),

$$
\Delta^\beta_{N|ML,a}
=
e^\beta_{N|ML,a}.
$$

On \(G_a^c\), the defect is bounded by a uniform constant \(K\), because the
tested beta alphabet is finite and uniformly bounded.  Hence

$$
\mathbb E_a^{act}\|\Delta^\beta_{N|ML,a}\|^2
\le
\mathbb E_a^{act}\|e^\beta_{N|ML,a}\|^2
+
K^2\mathbb P_a^{act}(G_a^c).
$$

Both terms are \(O(\eta_a)\).  Therefore the beta-naturality defect tends
to zero.  `square`

### Theorem 3.32: Beta-Naturality Decision Theorem

For the beta subgate of Paper 13, the current proof attempt has the
following exhaustive decision tree.

First, the positive lock:

$$
\boxed{
\mathrm{V4P13\text{-}METRIC\text{-}JET\text{-}BETA\text{-}LOCK}.
}
$$

Then beta naturality follows by Theorem 3.31.

Second, an allowed independent beta wiggle with positive actual or
constraint-polytope mass:

$$
\boxed{
\mathrm{V4P13\text{-}BETA\text{-}WIGGLE\text{-}COUNTERTABLE}.
}
$$

Then beta naturality is false as a current-corpus derivation by Proposition
3.28, and it becomes a floor route if the switch reads the beta defect with
positive sensitivity as in Corollary 3.29.

Third, neither condition has been sourced.  Then the beta subgate remains
genuinely open; it cannot be closed by metric-readout functoriality alone.

Proof.

If the actual law locks beta to the finite metric jet, Theorem 3.31 proves
the positive subgate.  If the current constraints allow an independent beta
wiggle, Proposition 3.28 gives a finite model satisfying metric functoriality
but violating beta naturality; therefore no proof from those constraints can
exist.  If neither a lock nor a wiggle certificate has been sourced, the
available data do not decide whether beta is derived or independent.  These
three alternatives exhaust the finite beta table.  `square`

### Theorem 3.33: Beta Lock Supplies The First Nontrivial Part Of
Single-Rule Normal Response

Assume metric-readout functoriality and metric-jet beta lock.  Then the
single-rule normal response is proved on the metric and beta entries:

$$
\mathrm{SR\text{-}METRIC\text{-}FUNCTORIALITY}
\quad+\quad
\mathrm{V4P13\text{-}METRIC\text{-}JET\text{-}BETA\text{-}LOCK}
\Longrightarrow
\mathrm{SR\text{-}METRIC/BETA\text{-}RESPONSE}.
$$

The remaining unsourced positive gates are the \(HD\) commutator and
actual-law support for the full single-rule response.

Proof.

Metric-readout functoriality supplies the action of the finite normal
response on inverse-metric readouts.  Metric-jet beta lock says the beta
record is the finite function \({\mathsf B}_{ML,a}\) of the same metric-jet
record and that the response preserves this graph.  By Theorem 3.31, the
response commutes with the beta construction in \(L^2(\mathbb P_a^{act})\).
This proves exactly the metric and beta parts of Definition 3.21.  The
\(HD\) commutator is a separate comparison-map identity, and actual-law
support for all subgates is a separate same-law concentration statement.
`square`

### Verdict 3.34: Symbolic Completion Of The Feynman-Einstein Beta Attack

At the symbolic beta-table level, the beta subgate is reduced.

Feynman says:

$$
\boxed{
\hbox{if beta can wiggle independently of the metric jet, beta naturality
is false.}
}
$$

Einstein says:

$$
\boxed{
\hbox{if beta is the finite derived structure function of one metric-jet
record, beta naturality is automatic.}
}
$$

Thus the first positive candidate is not a new switch estimate.  It is the
same-law symbolic lock

$$
\boxed{
\mathrm{V4P13\text{-}METRIC\text{-}JET\text{-}BETA\text{-}LOCK}.
}
$$

The next audit must check whether this symbolic lock also locks the
operational map \(D_a[\beta]\) under normal comparison.  That is the
stronger issue addressed next.

### Definition 3.35: Symbolic Beta Versus Operational Beta

The V4 corpus already defines the symbolic beta label as a derived finite
metric expression:

$$
\beta_a(g;M,L)^i
=
I_a(g)^{ij}(M\partial_jL-L\partial_jM).
$$

This is the symbolic beta table.

But the switch detector does not only use the symbol
\(\beta_a(g;M,L)\).  It uses the operational tangential comparison map

$$
D_a[\beta_a(g;M,L)]
$$

and asks how this map behaves when transported through a normal comparison
\(H_a[N]\).  Thus the real beta-lock question is operational:

$$
H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
\stackrel{?}{\simeq}
D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)].
$$

The left side is how the actual finite comparison maps transport the
tangential beta move.  The right side is the tangential beta move rebuilt
from the normally updated metric jet.

### Proposition 3.36: Corpus Audit Of Where Beta Lives

In the current V4 corpus, beta is symbolically derived but not yet
operationally locked.

Proof.

Paper 12 defines

$$
[H(N),H(M)]_a=D(\beta_a(g;N,M))
$$

with

$$
\beta_a(g;N,M)^i
=
I_a(g)^{ij}(N\partial_jM-M\partial_jN).
$$

Paper 13 imports the same definition.  Therefore beta is not introduced as
an independent continuum object, and not as an independent symbolic
structure function.

However, the dynamical obstruction in Paper 12 is exactly
\({\mathsf NorMet}_a\): whether the actual normal comparison transports the
metric-dependent structure function consistently.  Paper 6 also proves that
the same one-time metric readout can coexist with frozen, random-walk, and
reset geometry kernels.  Therefore the current corpus fixes the symbolic
formula for beta, but it does not yet prove that the actual operational map
\(D_a[\beta]\) is transported by \(H_a[N]\) as the beta rebuilt from the
updated metric jet.  That missing statement is precisely operational beta
lock.  `square`

### Definition 3.37: Operational Metric-Jet Beta Lock

The actual law satisfies operational metric-jet beta lock at scale
\(\eta_a\) if, for every tested triple \(N,M,L\),

$$
\mathbb E_a^{act}
\left[
\left\|
H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
-
D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)]
\right\|_{{\mathcal G}^{met}_a}^2
\right]
\le
\eta_a,
$$

with

$$
\eta_a\to0.
$$

This is stronger than symbolic beta lock.  It says not only that beta is
computed from the metric jet, but that the finite tangential operation
labelled by beta is transported as that computed object.

### Proposition 3.38: Operational Wiggle Table Survives Symbolic Beta

Symbolic beta being derived does not by itself rule out an operational beta
wiggle.

Proof.

Take one metric-jet state \(J_*\).  Then the symbolic beta value is fixed:

$$
b_*={\mathsf B}_{ML,a}(J_*).
$$

Let the normal response fix the metric jet:

$$
{\mathfrak R}_{N,a}^JJ_*=J_*.
$$

Let the finite effect space carry two tangential comparison maps

$$
D_a[b_*],
\qquad
D_a[b_1],
$$

which agree on all already tested one-map constraints but differ on a
switch-visible metric readout.  Choose a normal comparison map satisfying

$$
H_a[N]D_a[b_*]H_a[N]^{-1}=D_a[b_1].
$$

Then the symbolic beta table remains derived from \(J_*\), because
\({\mathsf B}_{ML,a}(J_*)=b_*\).  But operational beta lock fails, because

$$
D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ_*)]
=
D_a[b_*],
$$

whereas normal transport gives \(D_a[b_1]\).  Thus the wiggle is not an
extra symbolic beta variable.  It is a failure of the operational
comparison maps to transport the beta-labelled tangential move as a
metric-derived move.  `square`

### Corollary 3.39: Current-Corpus Beta Verdict

The Feynman beta-wiggle test is live at the operational level.

More precisely, the current corpus proves:

$$
\boxed{
\hbox{symbolic beta is metric-derived.}
}
$$

It does not prove:

$$
\boxed{
\hbox{the actual map }D_a[\beta]\hbox{ is transported by }H_a[N]
\hbox{ as metric-derived beta.}
}
$$

Therefore the next positive theorem must be operational beta lock:

$$
\boxed{
\mathrm{V4P13\text{-}OPERATIONAL\text{-}METRIC\text{-}JET\text{-}BETA\text{-}LOCK}.
}
$$

If operational beta lock fails and the difference is visible to the switch
detector, the beta-wiggle table becomes a genuine floor route.

### Theorem 3.40: Exact Positive Source For The Beta Gate

Assume the following three finite facts.

1. **No independent symbolic beta channel:** the only beta label admitted in
   the \(HH\to D\) table is

   $$
   {\mathsf B}_{ML,a}(J)=I_a^{ij}(J)C_{ML,a,j}.
   $$

2. **Faithful tangential representation:** for the tested beta labels,

   $$
   D_a[v_1]\simeq D_a[v_2]\hbox{ on metric readouts}
   \quad\Longrightarrow\quad
   v_1\simeq v_2
   $$

   modulo the declared tangential gauge.

3. **Operational beta transport:** \(H_a[N]\) conjugates beta-labelled
   tangential comparisons according to the normal response of the metric
   jet:

   $$
   H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
   \simeq
   D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)].
   $$

Then

$$
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}
$$

holds in the tested same-law \(L^2\) sense.

Proof.

The first assumption makes beta a finite function of the metric jet.  The
third assumption says the operational tangential move labelled by that beta
is transported through \(H_a[N]\) exactly as the beta rebuilt from the
updated metric jet.  The second assumption prevents the equality of
operations from hiding a different beta label behind a nonfaithful
tangential representation.  Therefore the response of the beta label is the
beta of the responded metric jet, which is precisely beta naturality.
`square`

### Verdict 3.41: Execution Of The Feynman-First Test

The Feynman test does not kill the positive route, but it does expose the
exact hinge.

It is not enough to say:

$$
\beta_a(g;M,L)
=
I_a(g)^{ij}(M\partial_jL-L\partial_jM).
$$

That formula is already in the corpus.  The missing theorem is that the
finite operation \(D_a[\beta]\), under actual normal comparison by \(H_a[N]\),
is transported as the metric-derived beta of the updated metric jet.

Thus Einstein's principle becomes the finite operational statement:

$$
\boxed{
\hbox{normal response acts on the whole deformation rule, not merely on
metric readouts one at a time.}
}
$$

This is the precise target to attack before the \(HD\) commutator gate.

### Definition 3.42: Minimal Operational Beta-Wiggle Table

A minimal operational beta-wiggle table consists of:

1. one metric-jet state \(J_*\);
2. the symbolic beta value

   $$
   b_*={\mathsf B}_{ML,a}(J_*);
   $$

3. a second tangential label \(b_1\) in the same tested beta alphabet;
4. two finite tangential comparison maps

   $$
   D_*:=D_a[b_*],
   \qquad
   D_1:=D_a[b_1];
   $$

5. a finite normal comparison map \(H:=H_a[N]\);
6. a tested metric observable \(G\);
7. the symbolic metric response

   $$
   {\mathfrak R}_{N,a}^JJ_*=J_*;
   $$

8. the operational wiggle identity

   $$
   HD_*H^{-1}=D_1;
   $$

9. switch visibility

   $$
   \|(D_1-D_*)G\|\ge c
   $$

   for some \(c>0\).

The table passes all symbolic beta tests, because \(b_*\) is still computed
from \(J_*\).  It fails operational beta lock, because normal conjugation
transports the operation \(D_a[b_*]\) to \(D_a[b_1]\), while the updated
metric jet still rebuilds \(b_*\).

### Proposition 3.43: A Two-Dimensional Feynman Witness

There is a two-dimensional finite operational beta-wiggle table satisfying
Definition 3.42.

Proof.

Let \(V=\mathbb R^2\) with basis \(u,w\).  Let the tested metric observable
be

$$
G=w.
$$

Let

$$
H=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
D_*=
I+\epsilon E_{12}
=
\begin{pmatrix}
1&\epsilon\\
0&1
\end{pmatrix},
$$

where \(E_{12}w=u\) and \(E_{12}u=0\).  Then

$$
HG=G
$$

at the symbolic metric-jet level, because \(H w=w\).  But

$$
HD_*H^{-1}
=
I+2\epsilon E_{12}
=:D_1.
$$

Thus

$$
(D_1-D_*)G
=
\epsilon u,
$$

so the wiggle is visible with \(c=\epsilon\|u\|\).  The symbolic beta value
has not moved, because the metric jet is a one-point state \(J_*\).  Only
the operational tangential map has moved under normal conjugation.  This is
the smallest concrete realization of the Feynman countertable.  `square`

### Corollary 3.44: Current-Corpus Non-Exclusion Of The Wiggle

The current corpus does not exclude the operational beta-wiggle table by
symbolic beta lock, one-map projective covariance, or metric-readout
functoriality.

Proof.

Symbolic beta lock only says \(b_*={\mathsf B}_{ML,a}(J_*)\).  The table
satisfies this.

Metric-readout functoriality for the one-point metric jet only asks that
the normal response preserve the declared metric-jet readout.  The table
satisfies this because \(J_*\) is fixed and \(H\) fixes the tested readout
\(G=w\).

One-map covariance tests \(H\), \(D_*\), and \(D_1\) separately.  The
violation is not in any one map.  It is in the conjugation relation

$$
HD_*H^{-1}\stackrel{?}{=}D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ_*)].
$$

The right side is \(D_*\), while the left side is \(D_1\).  No current
one-map assumption forbids this.  Therefore the operational wiggle is a live
current-corpus countertable unless an additional deformation-functoriality
principle is proved.  `square`

### Definition 3.45: Finite Deformation Functoriality

Finite deformation functoriality is the Einstein principle suggested by the
Feynman wiggle.

The actual law satisfies finite deformation functoriality at scale
\(\theta_a\) if, for every tested normal label \(N\), tangential label \(v\),
and metric-jet record \(J\), there is a finite transported tangential label

$$
H_{a,N,*}(v;J)
$$

such that

$$
\mathbb E_a^{act}
\left[
\left\|
H_a[N]D_a[v]H_a[N]^{-1}
-
D_a[H_{a,N,*}(v;J)]
\right\|_{{\mathcal G}^{met}_a}^2
\right]
\le
\theta_a,
$$

and, for the beta labels generated by a lapse pair \(M,L\),

$$
H_{a,N,*}({\mathsf B}_{ML,a}(J);J)
=
{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)
+r^\beta_{N|ML,a}(J),
$$

with

$$
\mathbb E_a^{act}\|r^\beta_{N|ML,a}\|^2\le\theta_a.
$$

The scale satisfies

$$
\theta_a\to0.
$$

This principle does not insert a hidden continuum deformation algebra.  It
is a finite statement about the declared comparison maps on the declared
finite record/effect spaces.

### Theorem 3.46: Deformation Functoriality Forbids The Operational Wiggle

Finite deformation functoriality with \(\theta_a\to0\) rules out any
positive-mass operational beta wiggle with fixed visibility \(c>0\).

Proof.

Apply Definition 3.45 to

$$
v={\mathsf B}_{ML,a}(J).
$$

Then

$$
H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
\simeq
D_a[H_{a,N,*}({\mathsf B}_{ML,a}(J);J)]
$$

and

$$
H_{a,N,*}({\mathsf B}_{ML,a}(J);J)
\simeq
{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ).
$$

Thus

$$
H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
\simeq
D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)]
$$

in the tested metric-observable norm.  A positive-mass wiggle with fixed
visibility \(c>0\) would keep this norm bounded below on a set of positive
probability, contradicting \(\theta_a\to0\).  `square`

### Theorem 3.47: Deformation Functoriality Implies Operational Beta Lock

Assume finite deformation functoriality, symbolic metric-jet beta lock, and
uniform continuity of the finite tangential representation \(v\mapsto
D_a[v]\) on the tested beta alphabet.  Then operational metric-jet beta lock
holds.

Proof.

By finite deformation functoriality,

$$
H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
=
D_a[H_{a,N,*}({\mathsf B}_{ML,a}(J);J)]
+o_{L^2}(1).
$$

The beta part of functoriality gives

$$
H_{a,N,*}({\mathsf B}_{ML,a}(J);J)
=
{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)
+o_{L^2}(1).
$$

Uniform continuity of \(D_a[\cdot]\) transfers this label error to an
operator error on metric readouts.  Hence

$$
H_a[N]D_a[{\mathsf B}_{ML,a}(J)]H_a[N]^{-1}
=
D_a[{\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)]
+o_{L^2}(1),
$$

which is Definition 3.37.  `square`

### Corollary 3.48: Deformation Functoriality Closes The Beta Gate

Under the hypotheses of Theorem 3.47 and the faithfulness hypothesis of
Theorem 3.40,

$$
\mathrm{V4P13\text{-}FINITE\text{-}DEFORMATION\text{-}FUNCTORIALITY}
\Longrightarrow
\mathrm{V4P13\text{-}OPERATIONAL\text{-}METRIC\text{-}JET\text{-}BETA\text{-}LOCK}
\Longrightarrow
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}.
$$

Proof.

The first implication is Theorem 3.47.  The second implication is Theorem
3.40.  `square`

### Proposition 3.49: Current-Corpus Status Of Deformation Functoriality

Finite deformation functoriality is not yet proved by the current V4 corpus.

Proof.

Papers 5 and 6 provide finite geometry records, finite metric readouts, and
examples of admissible finite geometry dynamics.  They do not force one
unique transport law for tangential comparison maps under normal comparison.

Paper 7 supplies finite normal and tangential comparison maps and one-map
projective compatibility.  But one-map compatibility does not imply the
conjugation law

$$
H_a[N]D_a[v]H_a[N]^{-1}
\simeq
D_a[H_{a,N,*}(v;J)].
$$

Paper 12 identifies the missing \(HHH\) term as normal-geometry response.
That is exactly the same obstruction in Jacobi language.  Therefore finite
deformation functoriality is a valid positive primitive, not a theorem
already in hand.  `square`

### Verdict 3.50: Feynman And Einstein After The Operational Audit

Feynman has produced the exact countertable:

$$
\boxed{
HD_a[b_*]H^{-1}=D_a[b_1],
\qquad
b_*={\mathsf B}_{ML,a}(J_*),
\qquad
{\mathfrak R}_{N,a}^JJ_*=J_*.
}
$$

Einstein has produced the exact principle that forbids it:

$$
\boxed{
H_a[N]D_a[v]H_a[N]^{-1}
\simeq
D_a[H_{a,N,*}(v;J)].
}
$$

Thus the next primitive positive theorem is:

$$
\boxed{
\mathrm{V4P13\text{-}FINITE\text{-}DEFORMATION\text{-}FUNCTORIALITY}.
}
$$

If that theorem is sourced by the actual finite ontology, the beta gate
closes.  If the operational wiggle survives the current constraint polytope
with switch visibility, the positive route must yield to an LP/Farkas floor
certificate.

### Definition 3.51: Finite Hypersurface-Deformation Groupoid

A finite hypersurface-deformation groupoid at regulator \(a\) consists of:

1. a finite hypersurface-record alphabet \({\mathcal X}_a^\Sigma\);
2. a finite groupoid \({\mathcal G}_a^\Sigma\rightrightarrows
   {\mathcal X}_a^\Sigma\) with source, target, composition, identities, and
   inverses;
3. a finite representation on tested observables,

   $$
   \rho_a:{\mathcal G}_a^\Sigma\to{\mathsf Iso}({\mathcal O}_a),
   $$

   satisfying

   $$
   \rho_a(\gamma_2\circ\gamma_1)=\rho_a(\gamma_2)\rho_a(\gamma_1),
   \qquad
   \rho_a(\gamma^{-1})=\rho_a(\gamma)^{-1}
   $$

   whenever the arrows are composable;
4. declared normal arrows \(h_a[N;J]\) and tangential arrows \(d_a[v;J]\)
   based at the metric-jet record \(J\);
5. representation compatibility

   $$
   \rho_a(h_a[N;J])=H_a[N],
   \qquad
   \rho_a(d_a[v;J])=D_a[v]
   $$

   on the tested sector;
6. a finite label-transport map \(h_{a,N,*}(v;J)\) defined by conjugation in
   the groupoid:

   $$
   h_a[N;J]\,
   d_a[v;J]\,
   h_a[N;J]^{-1}
   =
   d_a[h_{a,N,*}(v;J);J_N],
   $$

   where \(J_N={\mathfrak R}_{N,a}^JJ\).

This is not a hidden Markov factorization through unrecorded hypersurfaces.
It is a finite algebra of declared record transformations, with every arrow
and every represented action living in the finite ontology.

### Definition 3.52: Minimal Feynman Square For The Groupoid

The minimal square testing whether \(H\) and \(D\) come from one finite
deformation groupoid is:

$$
\begin{array}{ccc}
J & \xrightarrow{\ d_a[v;J]\ } & J_v\\
\downarrow h_a[N;J] & & \downarrow h_a[N;J_v]\\
J_N & \xrightarrow{\ d_a[h_{a,N,*}(v;J);J_N]\ } & (J_N)_{h_*v}
\end{array}
$$

The same condition is recorded as the conjugation defect

$$
{\mathsf Sq}_{N,v,a}(q)
:=
\left\|
H_a[N]D_a[v]H_a[N]^{-1}
-
D_a[h_{a,N,*}(v;J)]
\right\|_{{\mathcal G}^{met}_a}^2.
$$

The square passes on the actual law if

$$
\mathbb E_a^{act}{\mathsf Sq}_{N,v,a}\to0
$$

uniformly on the tested normal and tangential labels.

For the beta gate, put

$$
v={\mathsf B}_{ML,a}(J).
$$

Then the square is exactly the operational beta-lock square.

### Theorem 3.53: A Finite Groupoid Sources Deformation Functoriality

Assume:

1. finite hypersurface-deformation groupoid data as in Definition 3.51;
2. representation compatibility holds in \(L^2(\mathbb P_a^{act})\) with
   error \(\epsilon_a\to0\);
3. the actual law is supported with probability \(1-\epsilon_a\) on records
   where the arrows are composable;
4. the beta labels are transported by the groupoid according to the metric
   jet:

   $$
   h_{a,N,*}({\mathsf B}_{ML,a}(J);J)
   =
   {\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)+r^\beta_{N|ML,a}(J),
   $$

   with

   $$
   \mathbb E_a^{act}\|r^\beta_{N|ML,a}\|^2\to0.
   $$

Then

$$
\mathrm{V4P13\text{-}FINITE\text{-}DEFORMATION\text{-}FUNCTORIALITY}
$$

holds.

Proof.

On the high-probability composable sector, groupoid conjugation gives

$$
h_a[N;J]d_a[v;J]h_a[N;J]^{-1}
=
d_a[h_{a,N,*}(v;J);J_N].
$$

Applying the finite representation \(\rho_a\) and using representation
compatibility yields

$$
H_a[N]D_a[v]H_a[N]^{-1}
=
D_a[h_{a,N,*}(v;J)]
+o_{L^2}(1).
$$

For \(v={\mathsf B}_{ML,a}(J)\), the fourth assumption identifies the
transported label with the beta rebuilt from the updated metric jet, up to
vanishing \(L^2\) error.  This is exactly Definition 3.45.  `square`

### Corollary 3.54: The Groupoid Route Closes The Beta Gate

Under the hypotheses of Theorem 3.53, plus the uniform-continuity and
faithfulness hypotheses used in Theorems 3.47 and 3.40,

$$
\mathrm{V4P13\text{-}FINITE\text{-}HYPERSURFACE\text{-}DEFORMATION\text{-}GROUPOID}
\Longrightarrow
\mathrm{V4P13\text{-}FINITE\text{-}DEFORMATION\text{-}FUNCTORIALITY}
\Longrightarrow
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}.
$$

Proof.

The groupoid gives finite deformation functoriality by Theorem 3.53.
Finite deformation functoriality gives operational beta lock by Theorem
3.47.  Operational beta lock gives beta naturality by Theorem 3.40.
`square`

### Proposition 3.55: The Operational Wiggle Falsifies The Groupoid Route

The two-dimensional Feynman witness of Proposition 3.43 cannot be embedded
in a finite hypersurface-deformation groupoid satisfying metric-jet beta
transport.

Proof.

In the witness, the metric jet is fixed:

$$
{\mathfrak R}_{N,a}^JJ_*=J_*.
$$

Therefore metric-jet beta transport requires

$$
h_{a,N,*}(b_*;J_*)=b_*,
$$

because

$$
b_*={\mathsf B}_{ML,a}(J_*).
$$

But the operational witness has

$$
HD_a[b_*]H^{-1}=D_a[b_1],
$$

with \(D_a[b_1]\) switch-visible distinct from \(D_a[b_*]\).  If the finite
tangential representation is faithful on the tested readout, this forces

$$
h_{a,N,*}(b_*;J_*)=b_1,
$$

contradicting \(h_{a,N,*}(b_*;J_*)=b_*\).  Hence the witness falsifies the
groupoid route whenever it is allowed by the current constraint polytope.
`square`

### Proposition 3.56: Current-Corpus Status Of The Groupoid Route

The current V4 corpus does not yet prove the finite hypersurface-deformation
groupoid route.

Proof.

Paper 8 states a conditional full deformation Ward route: if a finite source
law is covariant under the full finite deformation groupoid, then Ward
differentiation gives algebra residual identities.  It also says this full
deformation covariance is not currently sourced.

Paper 10 uses a smooth compatible packet whose finite comparison maps
approximate the smooth hypersurface-deformation groupoid.  That is a
realizability certificate for selected smooth packets, not a proof that the
actual finite law is supported on such groupoid-compatible records.

Paper 7 supplies \(D_a[v]\) and \(H_a[N]\) and one-map covariance conditions,
but it does not construct a common groupoid whose representation contains
both as composable arrows and whose conjugation transports tangential labels.

Therefore the groupoid route is a legitimate Einstein-style source theorem,
not a theorem already contained in the corpus.  `square`

### Verdict 3.57: Groupoid Fork

The next positive fork is now exact:

$$
\boxed{
\mathrm{V4P13\text{-}FINITE\text{-}HYPERSURFACE\text{-}DEFORMATION\text{-}GROUPOID}^{act}
}
$$

with actual-law support and faithful representation, implies the beta gate.

The matching negative fork is:

$$
\boxed{
\mathrm{V4P13\text{-}OPERATIONAL\text{-}BETA\text{-}WIGGLE\text{-}COUNTERTABLE}
}
$$

with positive current-polytope mass and switch visibility.

Feynman's square says exactly how to falsify the groupoid.  Einstein's
groupoid says exactly how to forbid the square.  This is the cleanest
current form of the beta obstruction.

### Definition 3.58: Actual-Law Groupoid Support Event

Fix a tolerance \(\epsilon>0\).  Let

$$
{\mathsf GrpSupp}_a(\epsilon)
\subset\Omega_a
$$

be the event that the record \(q\) carries, for every tested normal label
\(N\), tangential label \(v\), and metric-jet record \(J\), all of the
following finite data and estimates:

1. composable arrows \(h_a[N;J]\), \(d_a[v;J]\), identities, and inverses;
2. representation compatibility:

   $$
   \|\rho_a(h_a[N;J])-H_a[N]\|_{{\mathcal G}^{met}_a}
   \le\epsilon,
   \qquad
   \|\rho_a(d_a[v;J])-D_a[v]\|_{{\mathcal G}^{met}_a}
   \le\epsilon;
   $$

3. square coherence:

   $$
   \left\|
   H_a[N]D_a[v]H_a[N]^{-1}
   -
   D_a[h_{a,N,*}(v;J)]
   \right\|_{{\mathcal G}^{met}_a}
   \le\epsilon;
   $$

4. beta transport:

   $$
   \|h_{a,N,*}({\mathsf B}_{ML,a}(J);J)
   -
   {\mathsf B}_{ML,a}({\mathfrak R}_{N,a}^JJ)\|
   \le\epsilon.
   $$

The actual law has groupoid support if there exists \(\epsilon_a\to0\) such
that

$$
\mathbb P_a^{act}({\mathsf GrpSupp}_a(\epsilon_a))\to1.
$$

This is the precise meaning of the superscript in

$$
\mathrm{V4P13\text{-}FINITE\text{-}HYPERSURFACE\text{-}DEFORMATION\text{-}GROUPOID}^{act}.
$$

### Theorem 3.59: Actual-Law Groupoid Support Sources The Beta Gate

If the actual law has groupoid support in the sense of Definition 3.58, and
the tested tangential representation is uniformly continuous and faithful on
the beta-label battery, then

$$
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}
$$

holds.

Proof.

On \({\mathsf GrpSupp}_a(\epsilon_a)\), the square-coherence and beta
transport estimates give finite deformation functoriality with error
\(O(\epsilon_a)\).  The complement has probability \(o(1)\).  Uniform
boundedness of the finite test battery makes the complement contribution
negligible in \(L^2\).  The result then follows from Corollary 3.54.
`square`

### Definition 3.60: Minimal Noncommuting-Square Falsifier

The Feynman falsifier for actual-law groupoid support is a finite record
table with four visible corners:

$$
J,\qquad J_v,\qquad J_N,\qquad J_{\square},
$$

and arrows

$$
d:J\to J_v,
\qquad
h:J\to J_N,
\qquad
h_v:J_v\to J_{\square},
\qquad
d_N:J_N\to J_{\square}'.
$$

It is a noncommuting-square falsifier if:

1. the one-arrow records are individually admissible;
2. the two routes have the same declared boundary labels;
3. the represented actions disagree on a tested metric readout:

   $$
   \|\rho_a(h_v)\rho_a(d)G-\rho_a(d_N)\rho_a(h)G\|\ge c
   $$

   for some \(c>0\);
4. the table is not excluded by the current-corpus constraint polytope.

When \(d=D_a[{\mathsf B}_{ML,a}(J)]\), this is the groupoid-level version of
the operational beta-wiggle table.

### Proposition 3.61: Noncommuting Squares Are Not Excluded By One-Arrow
Data

One-arrow admissibility and one-map covariance do not exclude the
noncommuting-square falsifier.

Proof.

The falsifier requires each of \(h,d,h_v,d_N\) to be an admissible finite
arrow and each represented map to satisfy its individual tests.  None of
those tests compares the composite

$$
\rho_a(h_v)\rho_a(d)
$$

with

$$
\rho_a(d_N)\rho_a(h).
$$

The defect is exactly a two-route defect.  Therefore it is invisible to
one-arrow and one-map assumptions.  Excluding it requires a square principle:
either groupoid support, finite deformation functoriality, or an equivalent
finite path-independence law.  `square`

### Proposition 3.61A: A Concrete Two-Route Feynman Square

There is a two-dimensional finite square in which all one-arrow maps are
invertible and individually admissible, the two routes have the same
declared labels, and the represented routes disagree on a metric readout.

Proof.

Let \(V=\mathbb R^2\) with basis \(u,w\), and let the tested readout be

$$
G=w.
$$

Let the normal arrow and tangential arrow be represented by

$$
H=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
D=
I+\epsilon E_{12}
=
\begin{pmatrix}
1&\epsilon\\
0&1
\end{pmatrix},
$$

where \(E_{12}w=u\) and \(E_{12}u=0\).  Both \(H\) and \(D\) are invertible
for every \(\epsilon\), and each can satisfy any one-arrow admissibility
test that only checks finite invertibility, boundedness, declared label
membership, support/collar compatibility, or one-map covariance.

Declare the two protocols to have the same boundary labels:

$$
\gamma_1=h_v\circ d,
\qquad
\gamma_2=d_N\circ h,
$$

with

$$
\rho(h)=\rho(h_v)=H,
\qquad
\rho(d)=\rho(d_N)=D.
$$

Then

$$
\rho(\gamma_1)G
=
HDw
=
H(w+\epsilon u)
=
w+2\epsilon u,
$$

whereas

$$
\rho(\gamma_2)G
=
DHw
=
Dw
=
w+\epsilon u.
$$

Therefore

$$
\|\rho(\gamma_1)G-\rho(\gamma_2)G\|
=
\epsilon\|u\|.
$$

The two routes disagree even though each individual arrow is perfectly
finite and invertible.  The only missing condition is a square/path
equivalence principle.  `square`

### Definition 3.61B: Square-Blind Current Polytope

Let

$$
{\mathcal P}^{sq\text{-}blind}_a
$$

be the finite probability polytope cut out by all current-corpus constraints
that involve only:

1. one-arrow admissibility;
2. one-map covariance;
3. symbolic beta derivation from metric-jet records;
4. declared boundary-label matching;
5. normalization and positivity.

It deliberately excludes any two-route condition of the form

$$
\rho_a(h_v)\rho_a(d)
\simeq
\rho_a(d_N)\rho_a(h).
$$

### Proposition 3.61C: The Feynman Square Is Admissible In The Square-Blind
Polytope

The two-route square of Proposition 3.61A defines a point of
\({\mathcal P}^{sq\text{-}blind}_a\), but not a point of the finite
equivalence-of-deformation sector.

Proof.

Put unit probability on the finite record carrying the four arrows of
Proposition 3.61A.  Each arrow is invertible and belongs to the declared
finite arrow alphabet.  The two protocols have the same declared normal and
tangential labels.  The symbolic beta record, if present, can be taken to be
the metric-derived value of the single metric jet, so symbolic beta
derivation is also satisfied.

Since \({\mathcal P}^{sq\text{-}blind}_a\) contains no two-route equality
constraint, the unit-mass law is feasible in that polytope.

However, finite equivalence of deformation would require

$$
\rho(\gamma_1)G=\rho(\gamma_2)G+o(1)
$$

on tested readouts.  Proposition 3.61A gives a fixed discrepancy
\(\epsilon\|u\|\).  Hence the witness is outside the finite-equivalence
sector whenever \(\epsilon\|u\|\) is bounded below.  `square`

### Corollary 3.61D: Switch-Floor Consequence Of A Visible Square

Let

$$
Q_a(q;G)
:=
\|\rho_a(h_v)\rho_a(d)G-\rho_a(d_N)\rho_a(h)G\|^2
$$

be the square defect.  Suppose that, for some \(c,\rho,\sigma>0\), the
current constraint polytope allows probability at least \(\rho\) on records
with

$$
Q_a(q;G)\ge c^2,
$$

and suppose the switch detector reads the square defect:

$$
S_a(q)\ge\sigma Q_a(q;G)-r_a(q),
\qquad
\mathbb E_a^{act}r_a^+\to0.
$$

Then

$$
\liminf_a\mathbb E_a^{act}S_a
\ge
\rho\sigma c^2.
$$

If the same lower bound holds on a current-polytope sector that exhausts
probability, it gives the corresponding high-probability LP/Farkas floor
route.

Proof.

Integrate the displayed domination:

$$
\mathbb E_a^{act}S_a
\ge
\sigma\mathbb E_a^{act}Q_a(q;G)
-\mathbb E_a^{act}r_a^+.
$$

The allowed visible-square mass contributes at least \(\rho c^2\) to the
expectation of \(Q_a\).  Letting \(a\) tend to the continuum limit gives the
claim.  The high-probability version is the same finite convex-duality
upgrade used in the LP/Farkas route: one must prove that good-square records
have vanishing feasible mass in the current polytope.  `square`

### Verdict 3.61E: Answers To The Three Feynman Questions

The three Feynman questions now have exact answers.

Can the two routes disagree while all one-arrow tests pass?

$$
\boxed{\hbox{Yes: Proposition 3.61A.}}
$$

Does the current corpus forbid that?

$$
\boxed{\hbox{Not by one-arrow, one-map, or symbolic-beta constraints:
Proposition 3.61C.}}
$$

Can the disagreement be made switch-visible?

$$
\boxed{\hbox{Yes, exactly when the switch dominates the square defect as in
Corollary 3.61D.}}
$$

Thus the next fork is concrete: prove finite equivalence of deformation, or
turn the visible noncommuting square into an LP/Farkas floor certificate.

### Definition 3.61F: Square-Defect Battery

Let \({\mathcal T}^{sq}_a\) be the finite battery of tested two-route
deformation squares.  An element

$$
\tau=(h,d,h_v,d_N,G)
$$

has square defect

$$
Q_{a,\tau}(q)
:=
\|\rho_a(h_v)\rho_a(d)G-\rho_a(d_N)\rho_a(h)G\|^2.
$$

Define the aggregate square defect

$$
\overline Q_a(q)
:=
\max_{\tau\in{\mathcal T}^{sq}_a}Q_{a,\tau}(q).
$$

The max is finite.  Therefore all square-defect questions are finite
questions on the actual record law.

### Theorem 3.61G: Square Smallness Is Finite Equivalence On The Battery

The actual law satisfies finite equivalence of deformation on the tested
square battery if and only if

$$
\mathbb E_a^{act}\overline Q_a\to0.
$$

Proof.

If finite equivalence holds on the battery, then the square defects vanish
uniformly over the tested battery:

$$
\sum_{\tau\in{\mathcal T}^{sq}_a}
\mathbb E_a^{act}Q_{a,\tau}\to0.
$$

The maximum is bounded by the finite sum:

$$
\overline Q_a
\le
\sum_{\tau\in{\mathcal T}^{sq}_a}Q_{a,\tau}.
$$

Hence \(\mathbb E_a^{act}\overline Q_a\to0\).

Conversely, if \(\mathbb E_a^{act}\overline Q_a\to0\), then for every
\(\tau\),

$$
Q_{a,\tau}\le\overline Q_a,
$$

so every tested square defect has expectation tending to zero.  This is
exactly finite equivalence of deformation on the battery.  `square`

### Definition 3.61H: Square LP/Farkas Floor Certificate

A square LP/Farkas floor certificate at level \(c>0\) is a proof that, for
some \(\epsilon_a\to0\),

$$
\sup_{P\in{\mathcal P}^{cur}_a}
P(\overline Q_a<c^2)
\le
\epsilon_a.
$$

Here \({\mathcal P}^{cur}_a\) is the current-corpus constraint polytope of
Definition 4.1 below.

Equivalently, finite LP duality asks for multipliers for the current-corpus
constraints such that the good-square indicator

$$
1_{\{\overline Q_a<c^2\}}
$$

is dominated by an affine combination whose constraint expectation is
\(\epsilon_a\).

### Theorem 3.61I: Square Floor Certificate Gives Actual Square Floor

If a square LP/Farkas floor certificate holds at level \(c>0\), then

$$
\mathbb P_a^{act}(\overline Q_a\ge c^2)\to1
$$

and therefore

$$
\liminf_a\mathbb E_a^{act}\overline Q_a\ge c^2.
$$

Proof.

Since \(\mathbb P_a^{act}\in{\mathcal P}^{cur}_a\),

$$
\mathbb P_a^{act}(\overline Q_a<c^2)
\le
\sup_{P\in{\mathcal P}^{cur}_a}
P(\overline Q_a<c^2)
\le
\epsilon_a.
$$

Thus \(\mathbb P_a^{act}(\overline Q_a\ge c^2)\to1\).  The expectation
bound follows because \(\overline Q_a\ge c^2\) on that event.  `square`

### Corollary 3.61J: Square Floor Plus Switch Domination Gives Switch Floor

Assume a square LP/Farkas floor certificate at level \(c>0\).  If the switch
detector dominates the aggregate square defect:

$$
S_a(q)\ge\sigma\overline Q_a(q)-r_a(q),
\qquad
\mathbb E_a^{act}r_a^+\to0
$$

for some \(\sigma>0\), then

$$
\liminf_a\mathbb E_a^{act}S_a
\ge
\sigma c^2.
$$

Proof.

Integrate the domination inequality and use Theorem 3.61I:

$$
\mathbb E_a^{act}S_a
\ge
\sigma\mathbb E_a^{act}\overline Q_a
-\mathbb E_a^{act}r_a^+.
$$

Taking \(\liminf\) gives the claim.  `square`

### Theorem 3.61K: Honest Square-Defect Decision

The square-defect attack has three and only three current possibilities.

First, the positive Einstein side:

$$
\boxed{
\mathbb E_a^{act}\overline Q_a\to0.
}
$$

Then finite equivalence of deformation holds on the tested battery by
Theorem 3.61G, and the groupoid route can proceed.

Second, the negative Feynman floor side:

$$
\boxed{
\mathrm{V4P13\text{-}SQUARE\text{-}LP\text{-}FLOOR}
\quad+\quad
S_a\ge\sigma\overline Q_a-r_a.
}
$$

Then the switch has a positive floor by Corollary 3.61J.

Third, neither square smallness nor a square floor certificate has been
sourced.  Then the current corpus has not decided the square defect.

Proof.

The first branch is exactly the definition of finite equivalence on the
tested square battery, by Theorem 3.61G.  The second branch is exactly the
finite convex-duality route of Theorem 3.61I plus the switch-domination
transfer of Corollary 3.61J.  If neither branch is sourced, then the current
assumptions neither force small square defect nor force a positive square
floor.  Since failure to prove smallness is not itself a floor theorem, no
third mathematical conclusion is available.  `square`

### Verdict 3.61L: What Feynman And Einstein Would Do Now

Feynman would try to certify the second branch:

$$
\boxed{
\mathrm{V4P13\text{-}SQUARE\text{-}LP\text{-}FLOOR}
\quad\hbox{and}\quad
S_a\ge\sigma\overline Q_a-r_a.
}
$$

Einstein would try to prove the first branch:

$$
\boxed{
\mathbb E_a^{act}\overline Q_a\to0,
}
$$

because that is exactly finite equivalence of deformation on the tested
finite protocols.

The square-defect problem is therefore the first place in Paper 13 where the
next theorem is a numerical same-law statement rather than another
definition.

### Proposition 3.61M: A Zero-Square Witness Is Also Square-Blind Feasible

The square-blind current polytope also contains a zero-square witness.

Proof.

Use the same finite two-dimensional readout space \(V=\mathbb R^2\), but set

$$
H=I,
\qquad
D=I.
$$

Let all four arrows in the square be represented by the identity:

$$
\rho(h)=\rho(h_v)=\rho(d)=\rho(d_N)=I.
$$

Then every one-arrow admissibility test is satisfied: the maps are finite,
invertible, bounded, support-preserving, and label-compatible.  The two
routes have the same declared boundary labels by construction.  Symbolic
beta, if present, can again be taken to be the metric-derived value of the
single metric jet.

For every tested readout \(G\),

$$
\rho(h_v)\rho(d)G
=
G
=
\rho(d_N)\rho(h)G.
$$

Thus

$$
\overline Q_a=0
$$

on this witness.  Since square-blind constraints contain no two-route
condition beyond boundary-label matching, this zero-square witness is
feasible in \({\mathcal P}^{sq\text{-}blind}_a\).  `square`

### Theorem 3.61N: Square-Blind Constraints Decide Neither Side

The square-blind current polytope proves neither finite square-defect
smallness nor a square LP/Farkas floor.

Proof.

By Proposition 3.61C, \({\mathcal P}^{sq\text{-}blind}_a\) contains a
noncommuting-square witness with

$$
\overline Q_a\ge c^2
$$

for some fixed \(c>0\).  Hence the square-blind constraints cannot imply

$$
\mathbb E_a^{act}\overline Q_a\to0.
$$

By Proposition 3.61M, the same square-blind polytope contains a zero-square
witness with

$$
\overline Q_a=0.
$$

Therefore it cannot imply a square floor of the form

$$
\mathbb P_a^{act}(\overline Q_a\ge c^2)\to1
$$

for any \(c>0\).  Thus one-arrow, one-map, symbolic-beta, and boundary-label
constraints leave the square defect undecided.  `square`

### Corollary 3.61O: What The Feynman Floor Attempt Really Proves

The concrete noncommuting-square witness proves non-exclusion of large
square defect.  It does not prove a square floor from the current
square-blind constraints.

To get a floor, one must add a genuine finite separator:

$$
\boxed{
\mathrm{V4P13\text{-}SQUARE\text{-}LP\text{-}FLOOR}.
}
$$

To get the positive side, one must add a genuine same-law path-independence
estimate:

$$
\boxed{
\mathbb E_a^{act}\overline Q_a\to0.
}
$$

No amount of one-arrow auditing decides between these two witnesses.  The
remaining problem is truly a two-route same-law theorem.

### Definition 3.61P: Finite Protocol Holonomy

For a tested two-route protocol

$$
\tau=(\gamma_+,\gamma_-,G),
$$

where \(\gamma_+\) and \(\gamma_-\) have the same declared finite boundary
deformation data, define the finite protocol holonomy on the readout \(G\)
by

$$
{\mathsf Hol}_{a,\tau}(q;G)
:=
\rho_a(\gamma_+)G-\rho_a(\gamma_-)G.
$$

For the square

$$
\gamma_+=h_v\circ d,
\qquad
\gamma_-=d_N\circ h,
$$

this is

$$
{\mathsf Hol}_{a,\tau}(q;G)
=
\rho_a(h_v)\rho_a(d)G-\rho_a(d_N)\rho_a(h)G.
$$

Thus

$$
Q_{a,\tau}(q)
=
\|{\mathsf Hol}_{a,\tau}(q;G)\|^2.
$$

Protocol holonomy is the finite operational curvature of the protocol
decomposition.  It is not a continuum curvature assumption: it is just the
difference between two recorded finite protocols acting on the same finite
readout.

### Definition 3.61Q: Finite Protocol-Gauge Invariance

The actual law satisfies finite protocol-gauge invariance on the tested
battery if, whenever two recorded protocols \(\gamma_+,\gamma_-\) have the
same declared finite boundary deformation data,

$$
\mathbb E_a^{act}
\|{\mathsf Hol}_{a,\tau}(\cdot;G)\|^2
\to0
$$

uniformly over tested readouts and tested protocol pairs.

Equivalently, with \(\overline Q_a\) from Definition 3.61F,

$$
\mathbb E_a^{act}\overline Q_a\to0.
$$

The word "gauge" here has the finite operational meaning: the route used to
decompose a declared boundary deformation is not itself an observable record
unless the finite law explicitly makes it observable.

### Theorem 3.61R: Protocol-Gauge Invariance Is Exactly The Einstein Side

Finite protocol-gauge invariance on the square battery is equivalent to
finite equivalence of deformation on that battery, and hence to square
smallness:

$$
\mathrm{V4P13\text{-}FINITE\text{-}PROTOCOL\text{-}GAUGE\text{-}INVARIANCE}
\quad\Longleftrightarrow\quad
\mathbb E_a^{act}\overline Q_a\to0.
$$

Proof.

By Definition 3.61P, the square defect is the squared norm of the protocol
holonomy.  Finite protocol-gauge invariance says that this squared norm has
vanishing expectation uniformly on the tested protocol pairs.  Theorem
3.61G proves that this is exactly finite equivalence of deformation on the
battery, equivalently \(\mathbb E_a^{act}\overline Q_a\to0\).  `square`

### Definition 3.61S: Protocol Holonomy LP/Farkas Floor

A protocol holonomy LP/Farkas floor at level \(c>0\) is the square-floor
certificate written in holonomy language:

$$
\sup_{P\in{\mathcal P}^{cur}_a}
P\left(
\max_{\tau\in{\mathcal T}^{sq}_a}
\|{\mathsf Hol}_{a,\tau}\|^2<c^2
\right)
\le
\epsilon_a,
$$

with

$$
\epsilon_a\to0.
$$

This is exactly a finite dual certificate saying that the current
constraints force nonzero protocol holonomy.

### Theorem 3.61T: Protocol Holonomy Decision

The protocol-holonomy formulation has the same honest fork as the
square-defect formulation.

The positive branch is:

$$
\boxed{
\mathrm{V4P13\text{-}FINITE\text{-}PROTOCOL\text{-}GAUGE\text{-}INVARIANCE}
}
$$

or equivalently

$$
\boxed{
\mathbb E_a^{act}\overline Q_a\to0.
}
$$

The negative branch is:

$$
\boxed{
\mathrm{V4P13\text{-}PROTOCOL\text{-}HOLONOMY\text{-}LP\text{-}FLOOR}
\quad+\quad
S_a\ge\sigma\overline Q_a-r_a.
}
$$

If neither branch is sourced, protocol holonomy is undecided by the current
corpus.

Proof.

The positive equivalence is Theorem 3.61R.  The negative branch is
Definition 3.61S together with Corollary 3.61J.  The undecided branch is
Theorem 3.61K: non-exclusion of holonomy is not a floor, and existence of a
zero-holonomy witness blocks any floor proof from square-blind constraints.
`square`

### Verdict 3.61U: First-Principles Reframing

The primitive finite object is now:

$$
\boxed{
{\mathsf Hol}_{a,\tau}
=
\rho_a(\gamma_+)G-\rho_a(\gamma_-)G.
}
$$

Feynman's question is whether the actual finite constraints force nonzero
protocol holonomy on a switch-visible sector.

Einstein's question is whether protocol decomposition is finite gauge, so
that only the declared boundary deformation can affect finite predictions.

Both questions are Barandes-aligned: they concern only finite records,
finite protocols, finite represented actions, finite readouts, and the
actual finite law.  The paper has therefore reached a genuinely numerical
same-law problem, not a request for another formal abstraction.

### Definition 3.61V: Boundary-Protocol Quotient

Let \({\mathsf Prot}_a\) be the finite set of recorded deformation protocols
in the tested battery.  Let

$$
\partial_a:{\mathsf Prot}_a\to{\mathsf BdDef}_a
$$

assign to each protocol its declared finite boundary deformation data.

Two protocols are boundary-equivalent if

$$
\gamma_+\sim_{\partial}\gamma_-
\quad\Longleftrightarrow\quad
\partial_a\gamma_+=\partial_a\gamma_-.
$$

The boundary-protocol quotient is the finite quotient set

$$
{\mathsf Prot}_a/\!\sim_{\partial}.
$$

The philosophical content is small but important: the primitive recorded
process is the boundary deformation class, not the chosen internal route,
unless the finite ontology explicitly records route as an observable.

### Definition 3.61W: Protocol-Quotient Support

Let

$$
{\mathsf QuotSupp}_a(\epsilon)
$$

be the event that the represented action of every tested protocol factors
through the boundary quotient up to error \(\epsilon\):

$$
\gamma_+\sim_{\partial}\gamma_-
\quad\Longrightarrow\quad
\|\rho_a(\gamma_+)G-\rho_a(\gamma_-)G\|^2\le\epsilon
$$

for every tested readout \(G\), uniformly over the tested protocol battery.

The actual law satisfies protocol-quotient support at scale \(\epsilon_a\)
if

$$
\mathbb P_a^{act}({\mathsf QuotSupp}_a(\epsilon_a))\ge1-\epsilon_a.
$$

The scale satisfies

$$
\epsilon_a\to0.
$$

This is stronger than saying that a nice reference quotient exists.  It is a
same-law support statement about the records selected by
\(\mathbb P_a^{act}\).

### Theorem 3.61X: Protocol-Quotient Support Implies Protocol-Gauge
Invariance

If protocol-quotient support holds and the tested readout norms are
uniformly bounded, then

$$
\mathrm{V4P13\text{-}FINITE\text{-}PROTOCOL\text{-}GAUGE\text{-}INVARIANCE}
$$

holds.  Equivalently,

$$
\mathbb E_a^{act}\overline Q_a\to0.
$$

Proof.

On the quotient-support event, every boundary-equivalent pair has squared
readout discrepancy at most \(\epsilon_a\).  On the complement, the squared
discrepancy is bounded by a finite battery constant \(K\).  Thus, for every
tested protocol pair,

$$
\mathbb E_a^{act}
\|{\mathsf Hol}_{a,\tau}\|^2
\le
\epsilon_a
+K\mathbb P_a^{act}({\mathsf QuotSupp}_a(\epsilon_a)^c).
$$

Both terms tend to zero.  Taking the finite maximum over the controlled
battery gives \(\mathbb E_a^{act}\overline Q_a\to0\).  By Theorem 3.61R,
this is finite protocol-gauge invariance.  `square`

### Definition 3.61Y: Route-Distinguishing Detector

A route-distinguishing detector is a finite readout \(G\) and a pair of
boundary-equivalent protocols \(\gamma_+,\gamma_-\) such that

$$
\|\rho_a(\gamma_+)G-\rho_a(\gamma_-)G\|\ge c
$$

for some \(c>0\) on a set of actual or current-polytope mass at least
\(\rho>0\).

It is switch-visible if, for some \(\sigma>0\),

$$
S_a(q)\ge
\sigma\|{\mathsf Hol}_{a,\tau}(q;G)\|^2-r_a(q),
\qquad
\mathbb E_a^{act}r_a^+\to0.
$$

### Theorem 3.61Z: Route-Distinguishing Detector Gives The Feynman Floor
Route

If a route-distinguishing detector exists with actual mass at least
\(\rho>0\) and is switch-visible, then

$$
\liminf_a\mathbb E_a^{act}S_a
\ge
\rho\sigma c^2.
$$

If the detector is certified by a current-polytope LP/Farkas separator that
forces route-distinguishing mass tending to one, then it gives the
high-probability switch floor route.

Proof.

The proof is the protocol-holonomy version of Corollary 3.61D.  On the
route-distinguishing event,

$$
\|{\mathsf Hol}_{a,\tau}(q;G)\|^2\ge c^2.
$$

Switch visibility gives

$$
\mathbb E_a^{act}S_a
\ge
\sigma\mathbb E_a^{act}\|{\mathsf Hol}_{a,\tau}\|^2
-\mathbb E_a^{act}r_a^+.
$$

The event contributes at least \(\rho c^2\), and the error term vanishes.
The LP/Farkas high-probability variant is finite convex duality applied to
the complement of the route-distinguishing event.  `square`

### Proposition 3.61AA: Current-Corpus Status Of Protocol Quotient

Protocol-quotient support is not yet proved in the current corpus.

Proof.

The square-blind constraints admit both the zero-square witness and the
noncommuting-square witness.  Hence they do not force represented actions to
factor through the boundary-protocol quotient.  The current corpus also does
not provide an LP/Farkas separator forcing route-distinguishing mass.  Thus
the actual law is not yet known to treat route as gauge, and it is not yet
known to make route observable with positive switch-visible mass.  `square`

### Verdict 3.61AB: Route Is Gauge Versus Route Is Observable

The first-principles fork is now:

$$
\boxed{
\mathrm{V4P13\text{-}PROTOCOL\text{-}QUOTIENT\text{-}SUPPORT}
\Longrightarrow
\mathbb E_a^{act}\overline Q_a\to0
}
$$

or

$$
\boxed{
\mathrm{V4P13\text{-}ROUTE\text{-}DISTINGUISHING\text{-}DETECTOR}
\quad+\quad
\mathrm{switch\ visibility}
\Longrightarrow
\mathrm{switch\ floor}.
}
$$

Einstein would try to prove that route is finite gauge.  Feynman would try
to build a route-distinguishing detector and certify its actual or
current-polytope mass.  Both routes now act directly on the finite
protocol-holonomy object.

### Definition 3.61AC: Feynman-First Route Detector LP

Fix a finite two-route battery \({\mathcal T}^{route}_a\).  For
\(\tau=(\gamma_+,\gamma_-,G)\), set

$$
Q_{a,\tau}^{route}(q)
:=
\|\rho_a(\gamma_+)G-\rho_a(\gamma_-)G\|^2.
$$

For \(c>0\), define the route-good event

$$
{\mathsf RouteGood}_a(c)
:=
\left\{
q:
\max_{\tau\in{\mathcal T}^{route}_a}
Q_{a,\tau}^{route}(q)<c^2
\right\}.
$$

The Feynman-first LP asks whether the current constraint polytope forces
the complement of this event:

$$
\sup_{P\in{\mathcal P}^{cur}_a}
P({\mathsf RouteGood}_a(c))
\to0.
$$

If yes, route is observably nontrivial on the tested battery.  If no, the
tested constraints still permit a law in which boundary-equivalent routes
are operationally indistinguishable.

### Proposition 3.61AD: The Minimal Detector Exists As A Feasible Witness

The two-dimensional square of Proposition 3.61A is a route-distinguishing
detector for the battery containing the single square

$$
\tau=(h_v\circ d,d_N\circ h,G).
$$

Its detection value is

$$
c=\epsilon\|u\|.
$$

Proof.

Proposition 3.61A gives

$$
\rho(h_v)\rho(d)G-\rho(d_N)\rho(h)G
=
\epsilon u.
$$

Therefore

$$
Q^{route}_{a,\tau}
=
\epsilon^2\|u\|^2.
$$

The two protocols have the same declared boundary data by construction.
Thus the witness is exactly a route-distinguishing detector in the sense of
Definition 3.61Y.  `square`

### Proposition 3.61AE: The Minimal Detector Is Not A Current-Corpus Floor

The detector of Proposition 3.61AD does not by itself give a current-corpus
LP/Farkas floor.

Proof.

The detector proves feasibility of route distinction.  A floor requires
forced route distinction.  But Theorem 3.61N proves that the same
square-blind constraints admit a zero-square witness with

$$
Q^{route}_{a,\tau}=0
$$

for the same boundary-equivalent square type.  Hence for every \(c>0\),

$$
\sup_{P\in{\mathcal P}^{sq\text{-}blind}_a}
P({\mathsf RouteGood}_a(c))
=1.
$$

So no LP/Farkas separator built only from square-blind constraints can prove
that route holonomy has positive mass.  `square`

### Theorem 3.61AF: Feynman-First Attack Result

The Feynman-first attack settles exactly this:

$$
\boxed{
\hbox{route distinction is finitely possible but not currently forced.}
}
$$

More explicitly:

1. route-distinguishing tables exist;
2. route-quotient tables also exist;
3. square-blind constraints decide neither side;
4. switch visibility converts forced route distinction into a switch floor;
5. protocol-quotient support converts route non-observability into the
   positive groupoid/equivalence route.

Proof.

Item 1 is Proposition 3.61AD.  Item 2 is the zero-square witness of
Proposition 3.61M.  Item 3 is Theorem 3.61N and Proposition 3.61AE.  Item 4
is Theorem 3.61Z.  Item 5 is Theorem 3.61X followed by Theorem 3.61R and
Theorem 3.63.  `square`

### Definition 3.61AG: Einstein Route-Quotient Principle

The Einstein route-quotient principle is the finite operational assertion
that internal decomposition route is not an observable unless it is
explicitly recorded as part of the finite configuration law.

In equations, for every fixed tested route battery,

$$
\max_{\tau\in{\mathcal T}^{route}_a}
Q_{a,\tau}^{route}
\to0
$$

in the actual law, either in \(L^1\) or, equivalently under uniform boundedness
of the finite battery, in probability.

This is not a continuum covariance axiom.  It is the finite statement that
the actual records identify protocols by their boundary deformation class
when route is not itself a recorded variable.

### Theorem 3.61AH: No Fixed Detector Is Equivalent To Quotient Support On
Finite Batteries

Assume the route battery is finite and all tested readout discrepancies are
uniformly bounded.  Then the following are equivalent:

1. protocol-quotient support holds along some scale \(\epsilon_a\to0\);
2. for every fixed \(c>0\),

   $$
   \mathbb P_a^{act}
   \left(
   \max_{\tau\in{\mathcal T}^{route}_a}
   Q_{a,\tau}^{route}\ge c^2
   \right)
   \to0;
   $$

3. no route-distinguishing detector has fixed positive actual mass on the
   tested battery.

Proof.

If protocol-quotient support holds, then outside a set of probability
\(\epsilon_a\), the maximum route discrepancy is at most \(\epsilon_a\).
Thus every fixed threshold \(c^2\) is eventually missed except on a set of
vanishing probability.

Conversely, if every fixed threshold has vanishing probability, then the
finite maximum \(Q_a^{route}:=\max_\tau Q_{a,\tau}^{route}\) converges to
zero in probability.  Since the battery is uniformly bounded,
bounded-convergence gives

$$
\mathbb E_a^{act}Q_a^{route}\to0.
$$

Choosing a decreasing deterministic scale \(\epsilon_a\to0\) along a
standard subsequence/diagonal extraction yields quotient support at that
scale on the finite battery.  The equivalence with absence of a fixed
positive-mass detector is just the negation of the threshold statement.
`square`

### Verdict 3.61AI: What Feynman And Einstein Would Do Now

Feynman would not declare victory from the noncommuting square.  He would
say: the detector exists, but the zero-square witness kills the LP floor
unless an actual-law constraint forces detector mass.

Einstein would not declare quotient support from elegance.  He would say:
if route is not a finite recorded observable, then quotient support is the
right primitive, but it must be proved as a same-law support theorem.

The exact next theorem is therefore one of:

$$
\boxed{
\mathrm{V4P13\text{-}ACTUAL\text{-}ROUTE\text{-}DETECTOR\text{-}MASS}
\quad+\quad
\mathrm{V4P13\text{-}SWITCH\text{-}VISIBILITY}
}
$$

or

$$
\boxed{
\mathrm{V4P13\text{-}PROTOCOL\text{-}QUOTIENT\text{-}SUPPORT}.
}
$$

The first makes route observable and gives a floor.  The second makes route
gauge and gives the positive finite-equivalence/groupoid path.  There is no
third structural escape inside the current battery.

### Definition 3.61AJ: Finite Route Record Algebra

Let \((\Omega_a,{\mathcal A}_a,\mathbb P_a^{act})\) be the actual finite
record law on the tested battery.  Let

$$
\partial_a:\Omega_a\to{\mathsf BdDef}_a
$$

be the recorded boundary-deformation map.  The boundary algebra is

$$
{\mathcal B}_a:=\sigma(\partial_a,\hbox{non-route tested record labels}).
$$

A route variable is a finite map

$$
\Gamma_a:\Omega_a\to{\mathsf Prot}_a
$$

with

$$
\partial_a\Gamma_a=\partial_a.
$$

Route is recorded on the battery if \(\Gamma_a\) is
\({\mathcal A}_a\)-measurable and is not, up to \(o(1)\), measurable with
respect to \({\mathcal B}_a\).  Route is unrecorded on the battery if every
tested readout action factors through \({\mathcal B}_a\) up to \(o(1)\).

This is the ontology audit in finite form.  It does not ask whether a
continuum route "exists."  It asks whether the actual finite configuration
law contains route as a record variable.

### Definition 3.61AK: Feynman Route-Comparison Experiment

A Feynman route-comparison experiment is a finite record that contains:

1. a boundary class \(b\in{\mathsf BdDef}_a\);
2. two recorded protocols \(\Gamma_a^+,\Gamma_a^-\) with
   \(\partial_a\Gamma_a^+=\partial_a\Gamma_a^-=b\);
3. a tested readout \(G\);
4. the route-comparison score

   $$
   Q_a^{cmp}
   :=
   \|\rho_a(\Gamma_a^+)G-\rho_a(\Gamma_a^-)G\|^2.
   $$

The experiment has detector mass \((c,\rho)\) if

$$
\mathbb P_a^{act}(Q_a^{cmp}\ge c^2)\ge\rho
$$

for constants \(c,\rho>0\) independent of \(a\).

This is the operational version of "route is observable": not merely that a
noncommuting square can be written down, but that the actual law gives
positive mass to a finite apparatus comparing the two routes.

### Theorem 3.61AL: Feynman Way From Route Spread To Floor

Assume:

1. a Feynman route-comparison experiment exists;
2. \(0\le Q_a^{cmp}\le K\) uniformly on the finite battery;
3. for some \(v>0\),

   $$
   \mathbb E_a^{act}Q_a^{cmp}\ge v;
   $$

4. the switch sees the comparison score:

   $$
   S_a(q)\ge\sigma Q_a^{cmp}(q)-r_a(q),
   \qquad
   \mathbb E_a^{act}r_a^+\to0.
   $$

Then the comparison experiment has detector mass

$$
c^2=v/2,
\qquad
\rho\ge {v\over 2K},
$$

and

$$
\liminf_a\mathbb E_a^{act}S_a
\ge
\sigma v.
$$

Proof.

Since \(0\le Q_a^{cmp}\le K\), if
\(\mathbb P(Q_a^{cmp}\ge v/2)<v/(2K)\), then

$$
\mathbb E Q_a^{cmp}
<
{v\over2}
+K{v\over2K}
=v,
$$

contradicting the route-spread lower bound.  Hence the detector mass bound
holds.  Integrating switch visibility gives

$$
\mathbb E_a^{act}S_a
\ge
\sigma\mathbb E_a^{act}Q_a^{cmp}
-\mathbb E_a^{act}r_a^+
\ge
\sigma v-o(1).
$$

Taking the lower limit proves the floor.  `square`

### Definition 3.61AM: Einstein Boundary Factorization

Einstein boundary factorization at scale \(\eta_a\) means that, for each
tested readout \(G\), there is a finite boundary function

$$
\Phi_{a,G}:{\mathsf BdDef}_a\to{\mathcal O}_a
$$

such that, on an event of actual probability at least \(1-\eta_a\),

$$
\|\rho_a(\gamma)G-\Phi_{a,G}(\partial_a\gamma)\|^2\le\eta_a
$$

for every tested protocol \(\gamma\) in the battery.

Here \({\mathcal O}_a\) is the tested readout space.  The meaning is direct:
if route is not recorded, the readout action is a function of the boundary
deformation class.  This is the finite Doob-Dynkin principle, not a
continuum covariance postulate.

### Theorem 3.61AN: Einstein Boundary Factorization Gives Quotient Support

If Einstein boundary factorization holds with \(\eta_a\to0\), then
protocol-quotient support holds.  More precisely, for boundary-equivalent
protocols \(\gamma_+\sim_\partial\gamma_-\), on the factorization event,

$$
\|\rho_a(\gamma_+)G-\rho_a(\gamma_-)G\|^2
\le
4\eta_a
$$

for every tested readout \(G\).  Therefore

$$
\mathbb P_a^{act}({\mathsf QuotSupp}_a(4\eta_a))\ge1-\eta_a,
$$

and hence

$$
\mathbb E_a^{act}\overline Q_a\to0.
$$

Proof.

If \(\gamma_+\sim_\partial\gamma_-\), then
\(\partial_a\gamma_+=\partial_a\gamma_-\).  On the factorization event,

$$
\rho_a(\gamma_+)G
=
\Phi_{a,G}(\partial_a\gamma_+)+e_+,
\qquad
\rho_a(\gamma_-)G
=
\Phi_{a,G}(\partial_a\gamma_-)+e_-,
$$

with \(\|e_+\|^2,\|e_-\|^2\le\eta_a\).  The boundary terms are equal, so

$$
\|\rho_a(\gamma_+)G-\rho_a(\gamma_-)G\|
\le
\|e_+\|+\|e_-\|
\le
2\sqrt{\eta_a}.
$$

Squaring gives \(4\eta_a\).  The probability statement is exactly
protocol-quotient support, and Theorem 3.61X gives
\(\mathbb E_a^{act}\overline Q_a\to0\).  `square`

### Theorem 3.61AO: Route-Ontology Dichotomy On A Finite Battery

Assume the route battery is finite and route-comparison scores are uniformly
bounded.  Exactly one of the following two regimes holds after passing to a
subsequence:

1. Feynman regime: there exist \(c,\rho>0\) such that

   $$
   \mathbb P_a^{act}
   \left(
   \max_{\tau\in{\mathcal T}^{route}_a}
   Q_{a,\tau}^{route}\ge c^2
   \right)
   \ge\rho;
   $$

2. Einstein regime: for every \(c>0\),

   $$
   \mathbb P_a^{act}
   \left(
   \max_{\tau\in{\mathcal T}^{route}_a}
   Q_{a,\tau}^{route}\ge c^2
   \right)
   \to0.
   $$

In the Feynman regime, switch visibility gives a floor.  In the Einstein
regime, Theorem 3.61AH gives protocol-quotient support on the finite
battery, hence the positive finite-equivalence/groupoid route.

Proof.

Let

$$
Q_a^{route}:=
\max_{\tau\in{\mathcal T}^{route}_a}Q_{a,\tau}^{route}.
$$

For each rational \(c>0\), either
\(\limsup_a\mathbb P(Q_a^{route}\ge c^2)>0\), or the probability tends to
zero along a subsequence.  Diagonalize over rational \(c>0\).  If the first
alternative holds for some \(c\), pass to a subsequence with positive lower
mass \(\rho\).  This is the Feynman regime.  If it fails for every rational
\(c>0\), it fails for every real \(c>0\), giving the Einstein regime.

The consequences are Theorem 3.61Z for the first regime and Theorem 3.61AH
for the second.  `square`

### Proposition 3.61AP: Current Outcome Of Trying Both Ways

The current corpus does not yet decide which route-ontology regime holds.

Proof.

The Feynman route has a feasible detector by Proposition 3.61AD, but not
actual detector mass by Proposition 3.61AE.  The Einstein route has a clean
factorization theorem by Theorem 3.61AN, but the current corpus has not
proved Einstein boundary factorization for the actual finite law.

Thus both ways have been tried to their current limit.  The new primitive
information must be one of:

$$
\boxed{
\mathrm{V4P13\text{-}ACTUAL\text{-}ROUTE\text{-}SPREAD}
\quad+\quad
\mathrm{V4P13\text{-}SWITCH\text{-}VISIBILITY}
}
$$

or

$$
\boxed{
\mathrm{V4P13\text{-}EINSTEIN\text{-}BOUNDARY\text{-}FACTORIZATION}.
}
$$

The first proves route is an observable finite distinction.  The second
proves route is finite gauge.  `square`

### Verdict 3.61AQ: Feynman First, Einstein Cleanly

Feynman's way is now an actual experiment:

$$
\boxed{
\hbox{record two boundary-equivalent routes and measure their readout
spread.}
}
$$

Einstein's way is now an actual quotient principle:

$$
\boxed{
\hbox{if route is not recorded, readout action factors through boundary
deformation data.}
}
$$

The two ways are not rivals anymore.  They are the two sides of the finite
ontology audit.  If the finite law records route, measure route spread and
push to a switch floor.  If the finite law does not record route, prove
boundary factorization and obtain protocol-quotient support.

### Definition 3.61AR: Route Conditional Variance

Let \(Y_{a,G}\) be the finite readout-action random variable

$$
Y_{a,G}(q):=\rho_a(\Gamma_a(q))G,
$$

where \(\Gamma_a\) ranges over the tested route variable in the finite
battery and \(G\) is a tested readout.  Let \({\mathcal B}_a\) be the
boundary algebra of Definition 3.61AJ.  Define the boundary predictor

$$
\widehat Y_{a,G}
:=
\mathbb E_a^{act}(Y_{a,G}\mid{\mathcal B}_a),
$$

and the route conditional variance

$$
{\mathsf Var}^{route}_a(G)
:=
\mathbb E_a^{act}
\left[
\|Y_{a,G}-\widehat Y_{a,G}\|^2
\right].
$$

For a finite readout battery \({\mathcal G}_a^{test}\), define

$$
\overline{\mathsf Var}^{route}_a
:=
\max_{G\in{\mathcal G}_a^{test}}
{\mathsf Var}^{route}_a(G).
$$

This is the single scalar form of the route-ontology audit.  It is zero
exactly when the tested route readout is a boundary-data function, and it is
positive exactly when route contributes readout spread beyond boundary data.

### Lemma 3.61AS: Conditional Two-Copy Identity

Let \(Y\) be a bounded finite readout random variable and
let \({\mathcal B}\) be a finite subalgebra.  Let \(Y'\) be a conditionally
independent copy of \(Y\) over \({\mathcal B}\).  Then

$$
\mathbb E\|Y-Y'\|^2
=
2\mathbb E\|Y-\mathbb E(Y\mid{\mathcal B})\|^2.
$$

Proof.

Condition on \({\mathcal B}\).  On each boundary atom, \(Y\) and \(Y'\) are
independent draws from the same finite conditional law.  Expanding the
squared norm gives

$$
\mathbb E(\|Y-Y'\|^2\mid{\mathcal B})
=
2\mathbb E(\|Y\|^2\mid{\mathcal B})
-2\|\mathbb E(Y\mid{\mathcal B})\|^2.
$$

The right side is twice the conditional variance.  Taking expectation gives
the identity.  `square`

### Theorem 3.61AT: Feynman Conditional-Variance Route

Assume that for some tested readout \(G\),

$$
{\mathsf Var}^{route}_a(G)\ge v>0
$$

along a subsequence, and assume the paired route-comparison score is
uniformly bounded:

$$
\|Y_{a,G}-Y'_{a,G}\|^2\le K.
$$

Then the same-law conditional two-copy experiment has detector mass

$$
c^2=v,
\qquad
\rho\ge {v\over K}.
$$

If, in addition, the switch sees the paired route spread,

$$
S_a(q,q')\ge
\sigma\|Y_{a,G}(q)-Y'_{a,G}(q')\|^2-r_a(q,q'),
\qquad
\mathbb E r_a^+\to0,
$$

then

$$
\liminf_a\mathbb E S_a\ge 2\sigma v.
$$

All expectations in this theorem are taken under the same-law conditional
two-copy experiment over the boundary algebra.  No new dynamical law is
introduced.

Proof.

By Lemma 3.61AS,

$$
\mathbb E\|Y_{a,G}-Y'_{a,G}\|^2
=
2{\mathsf Var}^{route}_a(G)
\ge
2v.
$$

Since the score is bounded by \(K\), the event
\(\|Y_{a,G}-Y'_{a,G}\|^2\ge v\) has probability at least \(v/K\); otherwise
the expectation would be \(<v+K(v/K)=2v\), with a harmless strict/limit
adjustment.  This gives detector mass.  Integrating switch visibility gives

$$
\mathbb E S_a
\ge
\sigma\mathbb E\|Y_{a,G}-Y'_{a,G}\|^2
-\mathbb E r_a^+
\ge
2\sigma v-o(1).
$$

Taking the lower limit proves the claim.  `square`

### Theorem 3.61AU: Einstein Conditional-Variance Route

Assume

$$
\overline{\mathsf Var}^{route}_a\to0.
$$

Then Einstein boundary factorization holds for the tested finite battery.
Consequently,

$$
\mathrm{V4P13\text{-}PROTOCOL\text{-}QUOTIENT\text{-}SUPPORT}
$$

holds, and

$$
\mathbb E_a^{act}\overline Q_a\to0.
$$

Proof.

For each tested readout \(G\), define the boundary function

$$
\Phi_{a,G}(b)
:=
\mathbb E_a^{act}(Y_{a,G}\mid{\mathcal B}_a=b).
$$

Then

$$
\mathbb E_a^{act}\|Y_{a,G}-\Phi_{a,G}(\partial_a)\|^2
=
{\mathsf Var}^{route}_a(G).
$$

Since the battery is finite and the maximum variance tends to zero, Markov's
inequality and a union bound give, after enlarging the deterministic scale
if necessary, an event of probability \(1-\eta_a\) on which all tested
readouts satisfy

$$
\|Y_{a,G}-\Phi_{a,G}(\partial_a)\|^2\le\eta_a,
$$

for some deterministic \(\eta_a\to0\).  This is Einstein boundary
factorization.  Theorem 3.61AN gives protocol-quotient support, and Theorem
3.61X gives \(\mathbb E_a^{act}\overline Q_a\to0\).  `square`

### Theorem 3.61AV: Route Conditional-Variance Decision

On a finite tested route-readout battery, after passing to a subsequence,
exactly one of the following holds:

1. Feynman variance branch:

   $$
   \liminf_a\overline{\mathsf Var}^{route}_a>0;
   $$

2. Einstein variance branch:

   $$
   \overline{\mathsf Var}^{route}_a\to0.
   $$

In the Feynman branch, Theorem 3.61AT turns route variance plus switch
visibility into a floor.  In the Einstein branch, Theorem 3.61AU turns
vanishing route variance into protocol-quotient support and finite
equivalence.

Proof.

The nonnegative scalar sequence
\(\overline{\mathsf Var}^{route}_a\) has subsequences on which either the
lower limit is positive or the value tends to zero.  The two consequences
are Theorems 3.61AT and 3.61AU.  `square`

### Proposition 3.61AW: Current-Corpus Status Of Route Variance

The current corpus does not source the numerical value of
\(\overline{\mathsf Var}^{route}_a\).

Proof.

The noncommuting-square witness proves that positive route variance is
feasible.  The zero-square witness proves that zero route variance is also
feasible under square-blind constraints.  Hence current constraints do not
force either

$$
\liminf_a\overline{\mathsf Var}^{route}_a>0
$$

or

$$
\overline{\mathsf Var}^{route}_a\to0.
$$

The missing input is therefore a genuine same-law estimate of conditional
variance relative to the boundary algebra.  `square`

### Verdict 3.61AX: The Feynman-Einstein Synthesis

The route problem has now been compressed to one finite scalar:

$$
\boxed{
\overline{\mathsf Var}^{route}_a.
}
$$

Feynman's reading is:

$$
\boxed{
\overline{\mathsf Var}^{route}_a\ge v>0
\quad\Longrightarrow\quad
\hbox{route is operationally visible.}
}
$$

Einstein's reading is:

$$
\boxed{
\overline{\mathsf Var}^{route}_a\to0
\quad\Longrightarrow\quad
\hbox{route is finite gauge.}
}
$$

This is the cleanest current formulation: not a new ontology by assertion,
but a finite conditional-variance question inside the actual record law.

### Definition 3.61AY: Recorded-Route Gate

The recorded-route gate is the assertion

$$
\mathrm{V4P13\text{-}RECORDED\text{-}ROUTE\text{-}GATE}
$$

that the route variable

$$
\Gamma_a:\Omega_a\to{\mathsf Prot}_a
$$

is an actual \({\mathcal A}_a\)-measurable finite record variable on the
tested battery.

If this gate holds, then \(Y_{a,G}=\rho_a(\Gamma_a)G\) is an actual finite
random variable and \(\overline{\mathsf Var}^{route}_a\) is a same-law
quantity.

If this gate fails, then \(\Gamma_a\) is not an actual record.  It may still
be used as an external comparison label in a countertable, but it may not be
treated as a hidden random variable sampled by \(\mathbb P_a^{act}\).

### Theorem 3.61AZ: Hidden Route Sampling Is Not Barandes-Aligned

If the recorded-route gate fails, then the route conditional variance of
Definition 3.61AR is not a legitimate same-law observable.

Proof.

The conditional variance is defined from the random variable

$$
Y_{a,G}(q)=\rho_a(\Gamma_a(q))G.
$$

This requires \(\Gamma_a\) to be \({\mathcal A}_a\)-measurable.  If
\(\Gamma_a\) is not part of the actual finite record algebra, then replacing
it by an unrecorded random choice of protocol would enlarge the actual law
to a hidden extension.  That is exactly what the Barandes rule forbids: the
paper may use finite records and finite readouts, but not unrecorded
intermediate histories as if they were sampled states.

Therefore, when the recorded-route gate fails, route variance is not a
same-law value to be estimated.  The Barandes-aligned move is to quotient
route and attempt boundary factorization.  `square`

### Theorem 3.61BA: Unrecorded Route Forces The Einstein Target

Assume the recorded-route gate fails and the tested readout action is
defined on the actual record law only through boundary deformation data:
for each tested \(G\), there exists a finite boundary function

$$
\Phi_{a,G}:{\mathsf BdDef}_a\to{\mathcal O}_a
$$

such that

$$
\rho_a(\gamma)G
=
\Phi_{a,G}(\partial_a\gamma)
$$

for every tested protocol label \(\gamma\) compatible with the same actual
finite record.  Then Einstein boundary factorization holds with
\(\eta_a=0\), hence protocol-quotient support holds exactly on the tested
battery.

Proof.

If readout action depends only on \(\partial_a\gamma\), then any two
boundary-equivalent protocol labels \(\gamma_+\sim_\partial\gamma_-\) give

$$
\rho_a(\gamma_+)G
=
\Phi_{a,G}(\partial_a\gamma_+)
=
\Phi_{a,G}(\partial_a\gamma_-)
=
\rho_a(\gamma_-)G.
$$

Thus the route discrepancy is zero on the tested battery.  This is
Einstein boundary factorization with zero error, and Theorem 3.61AN gives
protocol-quotient support.  `square`

### Proposition 3.61BB: Current-Corpus Route-Record Audit

The current corpus has not proved the recorded-route gate.

Proof.

Papers 11 and 12 define actual finite laws on finite record spaces and
explicitly forbid hidden Markov substeps or unrecorded intermediate
histories.  They do not introduce a finite actual route variable
\(\Gamma_a\) selecting an internal protocol decomposition inside the
whole-slab law.

Paper 13 introduces finite protocols, two-route batteries, and protocol
holonomy as tested comparison objects.  That is Barandes-aligned when the
protocols are recorded labels or external finite tests.  But it does not by
itself prove that the actual law samples a route variable with positive
mass.  Hence the recorded-route gate remains a new primitive if one wants
the Feynman route-spread branch.

Therefore the current-corpus audit leaves two honest options:

$$
\boxed{
\mathrm{V4P13\text{-}RECORDED\text{-}ROUTE\text{-}GATE}
\quad+\quad
\liminf_a\overline{\mathsf Var}^{route}_a>0
\quad+\quad
\mathrm{V4P13\text{-}SWITCH\text{-}VISIBILITY}
}
$$

or

$$
\boxed{
\mathrm{V4P13\text{-}EINSTEIN\text{-}BOUNDARY\text{-}FACTORIZATION}.
}
$$

The first is the Feynman apparatus route.  The second is the Einstein
quotient route.  `square`

### Verdict 3.61BC: The Recorded-Route Audit

The conditional-variance scalar is decisive only after the recorded-route
gate.  Without that gate, treating route as a random hidden variable would
violate the finite-record discipline.

Thus the true final fork is:

$$
\boxed{
\hbox{record route, then estimate conditional route variance}
}
$$

or

$$
\boxed{
\hbox{do not record route, then prove boundary factorization}.
}
$$

This is the cleanest Feynman-Einstein synthesis so far.  Feynman demands an
apparatus before route is observable.  Einstein quotients route away when no
apparatus records it.

### Definition 3.61BD: Pure Boundary Readout Measurability

Let

$$
{\mathcal B}_a^{\partial}:=\sigma(\partial_a)
$$

be the pure boundary-deformation algebra.  The actual finite readout action
is purely boundary-measurable on the tested battery if, for every tested
readout \(G\), the actual readout-action variable \(Y_{a,G}^{phys}\) is
\({\mathcal B}_a^{\partial}\)-measurable.

This definition deliberately does not mention a route variable.  It is the
Einstein-side statement one is allowed to make when route is not recorded:
the actual physical readout depends on the boundary deformation record and
not on an unobserved decomposition.

### Lemma 3.61BE: Finite Doob-Dynkin Factorization

Let \(\Omega\) be finite, let \(X:\Omega\to E\) be a finite record map, and
let \(Y:\Omega\to F\) be a finite readout map.  If \(Y\) is
\(\sigma(X)\)-measurable, then there exists a finite function

$$
\Phi:E\to F
$$

such that

$$
Y=\Phi\circ X.
$$

Proof.

Because \(\Omega\) is finite, \(\sigma(X)\)-measurability says precisely
that \(Y\) is constant on every fiber of \(X\).  Define \(\Phi(x)\) to be
that constant value on the fiber \(X^{-1}(x)\).  `square`

### Theorem 3.61BF: Einstein-First Closure From Boundary Measurability

Assume:

1. the recorded-route gate fails;
2. pure boundary readout measurability holds on the tested battery;
3. the tested protocol labels \(\gamma\) are external descriptions of the
   same actual boundary record, not actual sampled route states.

Then Einstein boundary factorization holds exactly, hence
protocol-quotient support holds exactly on the tested battery.

Proof.

By pure boundary readout measurability and Lemma 3.61BE, for each tested
readout \(G\) there exists a finite function

$$
\Phi_{a,G}:{\mathsf BdDef}_a\to{\mathcal O}_a
$$

such that the actual readout action satisfies

$$
Y_{a,G}^{phys}
=
\Phi_{a,G}(\partial_a).
$$

If two external protocol labels \(\gamma_+\) and \(\gamma_-\) have the same
boundary deformation data, they name the same actual boundary record.  Since
there is no recorded route variable, there is no further actual label on
which a physical readout can depend.  Therefore

$$
\rho_a(\gamma_+)G
=
\Phi_{a,G}(\partial_a\gamma_+)
=
\Phi_{a,G}(\partial_a\gamma_-)
=
\rho_a(\gamma_-)G.
$$

This is Einstein boundary factorization with zero error.  Theorem 3.61AN
then gives protocol-quotient support.  `square`

### Proposition 3.61BG: Feynman Veto Audit Of The Current V4 Corpus

The current V4 corpus does not contain an actual recorded route apparatus.

Proof.

The audit is finite and syntactic-conceptual:

1. Papers 11 and 12 import \(\mathbb P_a^{act}\) as a law on finite record
   spaces and explicitly prohibit hidden Markov substeps inside the
   indivisible whole-slab law.
2. Occurrences of \(\Gamma_a\) in Papers 6, 7, 8, and 13 before the
   route-variance section denote stochastic kernels, comparison maps, or
   projective compatibility maps.  They are not maps
   \(\Omega_a\to{\mathsf Prot}_a\) selecting a route decomposition as an
   actual record variable.
3. Paper 13 introduces finite two-route batteries and protocol holonomy as
   tests.  These are legitimate finite comparison objects.  They do not
   prove that \(\mathbb P_a^{act}\) samples one route rather than another.

Therefore the Feynman branch has not passed the apparatus test.  It remains
available only if a later theorem or enrichment proves

$$
\mathrm{V4P13\text{-}RECORDED\text{-}ROUTE\text{-}GATE}.
$$

Until then, the Barandes-aligned default is the Einstein-first target:
prove pure boundary readout measurability, hence boundary factorization.
`square`

### Verdict 3.61BH: Einstein First With Feynman Veto

At this point, the Feynman and Einstein instructions are no longer symmetric.
Feynman vetoes hidden route sampling: without a recorded route apparatus,
route variance is not a same-law observable.  Einstein supplies the positive
replacement: prove that physical readouts are boundary-measurable.

The next theorem should therefore be:

$$
\boxed{
\mathrm{V4P13\text{-}PURE\text{-}BOUNDARY\text{-}READOUT\text{-}MEASURABILITY}
}
$$

unless and until the corpus proves:

$$
\boxed{
\mathrm{V4P13\text{-}RECORDED\text{-}ROUTE\text{-}GATE}.
}
$$

This is not giving up on Feynman.  It is taking Feynman seriously: no
apparatus, no route observable.

### Definition 3.62: Finite Equivalence Of Deformation

Finite equivalence of deformation is the Einstein principle behind actual
groupoid support.

It says that if two finite deformation protocols:

$$
\gamma_1,\gamma_2
$$

have the same declared finite boundary deformation data and are built from
the same finite hypersurface record, then their represented actions agree on
the tested readout algebra:

$$
\mathbb E_a^{act}
\left[
\|\rho_a(\gamma_1)G-\rho_a(\gamma_2)G\|^2
\right]
\to0
$$

uniformly over tested \(G\).

For the minimal square this becomes

$$
\mathbb E_a^{act}
\left[
\|\rho_a(h_v)\rho_a(d)G-\rho_a(d_N)\rho_a(h)G\|^2
\right]
\to0.
$$

This is finite and operational: it only compares two recorded finite
protocols with the same declared boundary data.  It does not assume a
continuum hypersurface algebra or unrecorded intermediate states.

### Theorem 3.63: Finite Equivalence Of Deformation Implies Groupoid
Support Under Closure And Faithfulness

Assume:

1. the finite record space contains declared arrows, identities, inverses,
   and partial composition for the tested deformation protocols;
2. finite equivalence of deformation holds for all generating squares;
3. the representation \(\rho_a\) is faithful on the tested deformation-label
   battery modulo declared gauge;
4. the actual law gives probability \(1-o(1)\) to records where the
   generating arrows are composable;
5. beta labels are symbolically metric-derived from the metric jet.

Then the actual law has groupoid support in the sense of Definition 3.58.

Proof.

Assumption 1 supplies the candidate finite groupoid operations.  Assumption
4 gives actual-law support for composability.  Finite equivalence of
deformation says that every generating square has vanishing represented
defect on the tested readout algebra.  By faithfulness, represented square
coherence identifies the transported label modulo declared gauge.  Since
the beta label is symbolically built from the metric jet, the transported
beta label must agree, on the tested battery, with the beta rebuilt from the
transported metric jet.  These are exactly the four clauses defining
\({\mathsf GrpSupp}_a(\epsilon_a)\), with \(\epsilon_a\to0\).  `square`

### Corollary 3.64: Einstein Route To The Beta Gate

Under the hypotheses of Theorem 3.63,

$$
\mathrm{V4P13\text{-}FINITE\text{-}EQUIVALENCE\text{-}OF\text{-}DEFORMATION}
\Longrightarrow
\mathrm{V4P13\text{-}FINITE\text{-}HYPERSURFACE\text{-}DEFORMATION\text{-}GROUPOID}^{act}
\Longrightarrow
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}.
$$

Proof.

The first implication is Theorem 3.63.  The second is Theorem 3.59.
`square`

### Proposition 3.65: Current-Corpus Status Of Finite Equivalence

Finite equivalence of deformation is not yet proved in the current corpus.

Proof.

The current corpus contains finite comparison maps, one-map covariance
conditions, smooth-witness realizability certificates, and conditional full
deformation Ward statements.  None of these says that the actual law gives
probability tending to one to records where two finite protocols with the
same boundary deformation data have the same represented action.

The minimal noncommuting square of Definition 3.60 is therefore not excluded
unless a new same-law path-independence theorem is added.  `square`

### Verdict 3.66: Feynman-Einstein Next Target

Feynman now tests:

$$
\boxed{
\mathrm{V4P13\text{-}NONCOMMUTING\text{-}SQUARE\text{-}FALSIFIER}.
}
$$

Einstein now formulates:

$$
\boxed{
\mathrm{V4P13\text{-}FINITE\text{-}EQUIVALENCE\text{-}OF\text{-}DEFORMATION}.
}
$$

The exact next fork is:

$$
\boxed{
\mathrm{finite\ equivalence}
\Rightarrow
\mathrm{actual\ groupoid\ support}
\Rightarrow
\mathrm{beta\ gate}
}
$$

or

$$
\boxed{
\mathrm{noncommuting\ square\ survives}
\Rightarrow
\mathrm{groupoid\ route\ falsified\ as\ current\ derivation}.
}
$$

This is the clean operational form of the next problem.

## 4. Negative Route: LP/Farkas Switch Floor

The clean negative route is finite convex duality.

### Definition 4.1: Current-Corpus Constraint Polytope

Let \({\mathcal F}_a\) be the finite list of current-corpus actual-law
constraints available at regulator \(a\): normalization, positivity,
declared finite source responses, projective marginal constraints, and any
already proved Ward constraints.  Let

$$
{\mathcal P}_a^{cur}
$$

be the finite polytope of probability laws on \(\Omega_a\) satisfying those
constraints.

The actual law belongs to this polytope:

$$
\mathbb P_a^{act}\in{\mathcal P}_a^{cur}.
$$

### Definition 4.2: Good-Switch Event

For \(\delta>0\), define

$$
{\mathsf SwGood}_a(\delta)
:=
\{q:S_a(q)<\delta\}.
$$

### Definition 4.3: Switch LP Floor Certificate

A switch LP floor certificate at level \(\delta\) and error \(\varepsilon_a\)
is a proof that

$$
\sup_{P\in{\mathcal P}_a^{cur}}
P({\mathsf SwGood}_a(\delta))
\le
\varepsilon_a,
$$

with

$$
\varepsilon_a\to0.
$$

### Theorem 4.4: Switch LP Certificate Implies High-Probability Floor

If a switch LP floor certificate exists, then

$$
\mathbb P_a^{act}(S_a\ge\delta)\to1.
$$

Proof.

Since \(\mathbb P_a^{act}\in{\mathcal P}_a^{cur}\),

$$
\mathbb P_a^{act}({\mathsf SwGood}_a(\delta))
\le
\sup_{P\in{\mathcal P}_a^{cur}}
P({\mathsf SwGood}_a(\delta))
\le
\varepsilon_a.
$$

Thus

$$
\mathbb P_a^{act}(S_a\ge\delta)
=
1-\mathbb P_a^{act}({\mathsf SwGood}_a(\delta))
\to1.
$$

`square`

### Theorem 4.5: Farkas Dual Form

Because \({\mathcal P}_a^{cur}\) is finite-dimensional, the LP certificate
is equivalent to a finite dual certificate: multipliers for the current
constraints and a scalar \(b_a\) such that

$$
1_{{\mathsf SwGood}_a(\delta)}(q)
\le
b_a+\sum_r\lambda_{a,r}F_{a,r}(q)
$$

for every \(q\in\Omega_a\), while the constraint values imply

$$
b_a+\sum_r\lambda_{a,r}c_{a,r}
\le
\varepsilon_a.
$$

Proof.

This is finite linear-programming duality.  The primal maximizes mass on
\({\mathsf SwGood}_a(\delta)\) over the finite probability simplex cut by
affine constraints.  The displayed inequality is the dual domination of the
indicator by an affine combination of constraints.  `square`

### Proposition 4.6: Current-Corpus Floor Status

The current corpus does not contain a switch LP/Farkas floor certificate.

Proof.

No paper has yet enumerated the actual finite constraint polytope
\({\mathcal P}_a^{cur}\) at the level of the switch detector, and no paper
has supplied dual multipliers that dominate the good-switch indicator.  Thus
the high-probability switch floor is not proved.  `square`

## 5. Why The Current Corpus Does Not Decide The Switch

### Theorem 5.1: Same Coarse Constraints Can Permit Different Switch Mass

Let \({\mathcal F}_a\) be any finite constraint list that does not separate
the switch variable \(S_a\).  Then there exist two finite full-support laws
\(P_a^0,P_a^1\) satisfying the same \({\mathcal F}_a\)-constraints but with
different switch expectations.

Proof.

If \({\mathcal F}_a\) does not separate \(S_a\), then there are probability
directions \(\mu_a\) in the nullspace of all constraint functionals such
that

$$
\sum_q\mu_a(q)S_a(q)\ne0.
$$

Choose a strictly positive law \(P_a\) in the relative interior of the
constraint polytope.  For sufficiently small \(t\), the laws

$$
P_a^\pm=P_a\pm t\mu_a
$$

remain strictly positive and satisfy the same constraints.  But

$$
\mathbb E_{P_a^+}S_a-\mathbb E_{P_a^-}S_a
=
2t\sum_q\mu_a(q)S_a(q)\ne0.
$$

`square`

### Corollary 5.2: A Switch-Relevant Constraint Is Necessary

The current-corpus constraints can decide the switch only if they include,
imply, or dual-separate switch-relevant information.  Generic projective
compatibility, source centering, and fixed-background algebra are not enough.

### Proposition 5.3: Reset/Random-Walk Geometry Kernels Remain Diagnostic

The reset/random-walk kernels from earlier V4 no-go tests remain diagnostic:
unless the actual-law axioms exclude them by a switch-relevant condition,
they can preserve coarse finite record alphabets while failing the
three-normal switch.

Proof.

Such kernels can be arranged to preserve declared finite record spaces and
some marginals while changing the response of the metric readout under
normal comparisons.  Since the switch detector is exactly a metric-response
test, these kernels can produce a positive switch value unless excluded by
additional response identities.  `square`

### Verdict 5.4

The switch detector is not a bookkeeping object.  It is the first finite
place where dynamical geometry has to be selected by the actual law.

## 6. Conditional Closure Of The Paper-7 Jacobi Gate

### Theorem 6.1: Switch Smallness Closes The \(HHH\) Jacobi Gate

Assume:

1. \(HH\) pair residuals are \(L^2(\mathbb P_a^{act})\)-small on metric
   observables;
2. \(DHH\) tangential metric naturality is
   \(L^2(\mathbb P_a^{act})\)-small;
3. metric readout observables separate tested metric records with controlled
   constants;
4. three-normal switch smallness holds:

   $$
   \mathbb E_a^{act}S_a\to0.
   $$

Then

$$
\mathbb E_a^{act}J_{HHH,a}^2\to0.
$$

Proof.

Apply Paper 12 Theorem 11.6O pointwise and square the resulting finite
inequality.  The first three assumptions control the pair, tangential, and
separation errors.  The fourth controls the detector term.  `square`

### Corollary 6.2: Conditional Paper-7 Step-1 Closure

If, in addition, \(DDD\) and \(DDH\) close kinematically and \(DHH\)
tangential metric naturality is small, then the full Step-1 finite
label-Jacobi gate closes:

$$
\mathbb E_a^{act}
\left(
J_{DDD,a}^2+J_{DDH,a}^2+J_{DHH,a}^2+J_{HHH,a}^2
\right)
\to0.
$$

Proof.

Combine Paper 12's four-sector evaluation with Theorem 6.1.  `square`

## 7. Current-Corpus Decision

### Theorem 7.1: Current-Corpus Three-Normal Switch Verdict

The current corpus proves neither

$$
\mathbb E_a^{act}S_a\to0
$$

nor

$$
\mathbb P_a^{act}(S_a\ge\delta)\to1
$$

for any fixed \(\delta>0\).

Proof.

The positive side would follow from switch Stein coercivity or switch
equivalence response, but neither is proved in the current corpus.  The
Feynman repair graph and the Einstein single-rule normal response sharpen
those two routes, but neither object has been constructed from the current
actual-law assumptions.  The source audit in Proposition 3.23 shows the
precise positive obstruction: beta naturality, the \(HD\) commutator law,
and actual-law support are not yet sourced.  The negative side would follow
from a switch LP/Farkas floor certificate, but no such certificate is
present.  The available structural assumptions do not determine the switch
variable by Theorem 5.1 unless augmented by switch-relevant constraints.
`square`

### Corollary 7.2: What Has Been Settled

Paper 13 settles the decision architecture, not the actual side of the
decision.  The first positive live target is:

$$
\boxed{
\mathrm{V4P13\text{-}SINGLE\text{-}RULE\text{-}NORMAL\text{-}RESPONSE}.
}
$$

The source audit reduces that target to three unsourced primitive gates:

$$
\boxed{
\mathrm{V4P13\text{-}SR\text{-}BETA\text{-}NATURALITY}
\quad+\quad
\mathrm{V4P13\text{-}SR\text{-}HD\text{-}COMMUTATOR}
\quad+\quad
\mathrm{V4P13\text{-}SR\text{-}ACTUAL\text{-}SUPPORT}.
}
$$

Metric-readout functoriality is already available as the weak finite
language of response; it is not the hard part.

The first of those gates has now been sharpened to a decision:

$$
\boxed{
\mathrm{V4P13\text{-}FINITE\text{-}EQUIVALENCE\text{-}OF\text{-}DEFORMATION}
\Longrightarrow
\mathrm{V4P13\text{-}FINITE\text{-}HYPERSURFACE\text{-}DEFORMATION\text{-}GROUPOID}^{act}
\Longrightarrow
\mathrm{V4P13\text{-}FINITE\text{-}DEFORMATION\text{-}FUNCTORIALITY}
\Longrightarrow
\mathrm{V4P13\text{-}OPERATIONAL\text{-}METRIC\text{-}JET\text{-}BETA\text{-}LOCK}
\quad\hbox{or}\quad
\mathrm{V4P13\text{-}OPERATIONAL\text{-}BETA\text{-}WIGGLE\text{-}COUNTERTABLE}.
}
$$

The corpus already has symbolic metric-derived beta.  The lock asks for the
stronger operational statement: \(D_a[\beta]\) must be transported through
\(H_a[N]\) as the beta rebuilt from the updated metric jet.  The wiggle
falsifies beta naturality as a current-corpus derivation, and gives a floor
if the switch reads the beta defect with positive sensitivity.  Finite
deformation functoriality is the immediate positive primitive that forbids
the wiggle; the finite hypersurface-deformation groupoid is the Einstein
source for that functoriality; finite equivalence of deformation is the
same-law path-independence principle that would source the actual groupoid
support.

Its minimal table shadow is cyclic flatness:

$$
\boxed{
\mathrm{V4P13\text{-}MINIMAL\text{-}SWITCH\text{-}CYCLIC\text{-}FLATNESS}.
}
$$

Cyclic flatness is necessary and sufficient for the tested switch table to
pass, but it should be sourced from single-rule response rather than
declared as an isolated identity.

Its analytic corollary or fallback is

$$
\boxed{
\mathrm{V4P13\text{-}SWITCH\text{-}REPAIR\text{-}GRAPH}.
}
$$

Their tiny falsification tests are:

$$
\boxed{
\mathrm{V4P13\text{-}TINY\text{-}REPAIR\text{-}COUNTERTEST}
}
$$

and

$$
\boxed{
\mathrm{V4P13\text{-}TWO\text{-}STATE\text{-}SWITCH\text{-}FALSIFIER}.
}
$$

The negative high-probability target remains

$$
\boxed{
\mathrm{V4P13\text{-}SWITCH\text{-}LP\text{-}FLOOR\text{-}CERTIFICATE}
}
$$

for the negative side.

## 8. Final Settlement

The three-normal switch detector is the smallest finite operational
experiment for the \(HHH\) normal-geometry Jacobi obstruction.

The positive theorem would say:

$$
\boxed{
\hbox{actual normal metric response is cyclically invisible to finite
metric readouts.}
}
$$

The negative theorem would say:

$$
\boxed{
\hbox{actual finite constraints force a visible cyclic normal-switch
defect.}
}
$$

The current corpus proves neither.  This is not a failure of formulation;
it is a successful reduction.  The V4 GR route has reached a finite
actual-law fork:

$$
\boxed{
\mathrm{V4P13\text{-}THREE\text{-}NORMAL\text{-}SWITCH\text{-}DECISION}^{cur}
\quad\hbox{open}.
}
$$

The next work should not add more formal labels.  It should either prove
that route is finite gauge, concretely by proving protocol-quotient support,
hence finite protocol-gauge invariance and square-defect smallness

$$
\mathbb E_a^{act}\overline Q_a\to0,
$$

hence finite equivalence of deformation and actual groupoid support, and
then the \(HD\) commutator/support gates; or prove that route is an
observable finite distinction, concretely by upgrading the noncommuting-square
witness of Proposition 3.61A to a route-distinguishing detector with actual
or LP/Farkas-certified mass and switch domination of the corresponding
protocol holonomy.

The Feynman-first detector test has answered the local falsification
question sharply: route distinction is finitely possible, but not currently
forced.  The square-blind constraints allow both zero-square and
noncommuting-square witnesses by Theorem 3.61N, and Proposition 3.61AE
therefore kills any LP/Farkas floor built only from those constraints.

The remaining issue is therefore the numerical same-law protocol-holonomy
decision of Theorem 3.61T, refined by Verdicts 3.61AB, 3.61AI, 3.61AQ,
3.61AX, 3.61BC, and 3.61BH into a recorded-route audit.  If route is
recorded, the decisive scalar is

$$
\boxed{
\overline{\mathsf Var}^{route}_a.
}
$$

The Feynman primitive is:

$$
\boxed{
\mathrm{V4P13\text{-}RECORDED\text{-}ROUTE\text{-}GATE}
\quad+\quad
\liminf_a\overline{\mathsf Var}^{route}_a>0
\quad+\quad
\mathrm{V4P13\text{-}SWITCH\text{-}VISIBILITY}
}
$$

The Einstein primitive is:

$$
\boxed{
\mathrm{V4P13\text{-}PURE\text{-}BOUNDARY\text{-}READOUT\text{-}MEASURABILITY}.
}
$$

The first says route is an actual recorded apparatus variable and has
conditional readout spread beyond boundary data, yielding a floor once the
switch sees the spread.  The second says that, in the absence of a recorded
route apparatus, physical readouts are measurable with respect to boundary
deformation data.  Finite Doob-Dynkin factorization then gives Einstein
boundary factorization, protocol-quotient support, and finite
equivalence/groupoid support.  It is not further one-arrow bookkeeping, and
it is not a hidden route sample.
