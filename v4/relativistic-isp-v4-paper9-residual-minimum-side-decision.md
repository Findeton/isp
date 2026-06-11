# Relativistic ISP V4 Paper 9: Residual-Minimum Side Decision

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed five-route side-decision audit.

## Abstract

V4 Paper 8 proves the correct residual-minimum dichotomy.  After projective
compatibility is imposed, the finite residual minimum

$$
a_a^*:=\min_{q\in C_a^{tot}}{\mathcal A}_a(q)
$$

either tends to zero or has a positive lower floor.

Paper 9 asks which side can be proved from the present V4 corpus.  It fully
explores the five live routes:

1. construct residual-small witnesses;
2. prove a positive residual floor;
3. reduce the problem to local finite jet algebra;
4. linearize around flat geometry;
5. run certified finite search.

The verdict is precise.

First, a smooth projective finite deformation calculus gives a conditional
zero-side theorem:

$$
\boxed{
\mathrm{V4P9\text{-}SMOOTH\text{-}WITNESS\text{-}ZERO}^{cond}.
}
$$

If the finite geometry/comparison architecture is a projectively compatible
discretization of smooth hypersurface deformation transports, then

$$
a_a^*\to0.
$$

Second, a universal positive floor cannot be true over every Barandes-aligned
finite geometry architecture, because the smooth-witness architecture is an
allowed finite stochastic architecture and has residual-small witnesses.

Third, this does not by itself prove dynamical GR.  The unconstrained minimum
may be made small by a flat or kinematic sector.  The real GR-facing target is
therefore the source-conditioned residual minimum

$$
a_a^*({\mathcal B})
:=
\min_{q\in{\mathcal B}_a}{\mathcal A}_a(q),
$$

where \({\mathcal B}_a\) fixes the finite metric/source/boundary data one wants
the geometry law to realize.

Fourth, Paper 9 gives exact positive and negative certificate frameworks for
that conditioned problem:

$$
\boxed{
\mathrm{V4P9\text{-}JET\text{-}CERTIFICATE\text{-}REDUCTION}
\quad\hbox{and}\quad
\mathrm{V4P9\text{-}DUAL\text{-}FLOOR\text{-}CERTIFICATE}.
}
$$

The current-corpus actual side is still not sourced:

$$
\boxed{
\mathrm{V4P9\text{-}ACTUAL\text{-}CONDITIONED\text{-}SIDE}^{cur}
\quad\hbox{not sourced}.
}
$$

This is progress, not a retreat: Paper 9 removes the wrong global floor
question and identifies the exact next theorem.  One must either prove
source-conditioned smooth realizability for the declared finite
matter-geometry architecture, or produce a finite dual certificate proving a
positive conditioned residual floor.

## 0. Imports And Discipline

### Import 0.1: Paper-8 Residual Penalty

Paper 8 defines finite residuals

$$
R_{DD,a},\qquad R_{DH,a},\qquad R_{HH,a},
$$

and the covariance error \({\mathcal E}_{cov,a}\).  For finite test sets it
defines

$$
{\mathcal A}_a(q)
:=
\sum_{DD}\|R_{DD,a}^q\|^2
+\sum_{DH}\|R_{DH,a}^q\|^2
+\sum_{HH}\|R_{HH,a}^q\|^2
+\|{\mathcal E}_{cov,a}^q\|^2.
$$

The residual minimum is

$$
a_a^*:=\min_{q\in C_a^{tot}}{\mathcal A}_a(q).
$$

### Import 0.2: Paper-8 Dichotomy

Paper 8 proves that the raw dichotomy can fail for arbitrary regulator
sequences, but that:

1. the tail-refinement envelope always has a zero/floor dichotomy;
2. the original minima have the desired zero/floor dichotomy under projective
   residual-minimum compatibility.

### Import 0.3: What Paper 9 Must Decide

Paper 9 does not need to reprove the dichotomy.  It must decide whether the
finite architecture lies on the zero side or the floor side.

### Barandes Rule 0.4

Paper 9 may use:

1. finite record spaces;
2. finite stochastic kernels;
3. finite comparison maps and finite residuals;
4. declared finite source and boundary records;
5. continuum smooth geometry only as an approximation theorem for finite
   records, never as primitive ontology.

Paper 9 may not use:

1. Einstein equations as an axiom;
2. Hilbert phase as ontology;
3. hidden Markov time slices inside a whole finite slab;
4. a continuum action as a physical source unless it is encoded by a finite
   same-law score.

The discipline is:

$$
\hbox{finite records first; smooth geometry only after finite approximation
data earn it.}
$$

## 1. Route 1: Construct Residual-Small Witnesses

The most direct way to prove the zero side is to exhibit configurations
\(q_a\) such that

$$
{\mathcal A}_a(q_a)\to0.
$$

### Definition 1.1: Witness Family

A residual-small witness family is a sequence \(q_a\in C_a^{tot}\) for which

$$
{\mathcal A}_a(q_a)\to0.
$$

If such a family exists, then \(a_a^*\le{\mathcal A}_a(q_a)\to0\).

### Proposition 1.2: Labels Alone Cannot Be Witnesses

Adding finite geometry labels alone does not produce a residual-small
witness family.

Proof.

The residuals test comparison maps, bracket closure, covariance, and
geometry-update behavior.  A label \(g\in C_a^{geom}\) with no compatible
transport and update law does not determine these maps.  Papers 6 and 7
already show that the same labels allow reset and random-walk kernels whose
normal covariance residuals are generically nonzero.  Therefore labels alone
do not source \({\mathcal A}_a(q_a)\to0\).  `square`

### Definition 1.3: Smooth Projective Finite Deformation Calculus

A finite architecture has a smooth projective deformation calculus if, for a
regular refinement sequence, it supplies:

1. finite geometry records \(g_a[h]\) approximating smooth spatial metrics
   \(h\) on compact coordinate patches;
2. finite tangential comparison maps \(D_a[v]\) approximating pullback by the
   flow of \(v\);
3. finite normal comparison maps \(H_a[N]\) approximating normal hypersurface
   deformation by lapse \(N\);
4. finite geometry-update maps compatible with those comparisons;
5. finite observable readout maps separating the tested effects;
6. projective prolongations \(P_{a\to b}\) satisfying

   $$
   P_{a\to b}D_a[v]\simeq D_b[v]P_{a\to b},
   \qquad
   P_{a\to b}H_a[N]\simeq H_b[N]P_{a\to b};
   $$

7. total approximation error

   $$
   \epsilon_a^{def}
   :=
   \epsilon_a^{cmp}+\epsilon_a^{proj}+\epsilon_a^{br}+\epsilon_a^{obs}
   \to0.
   $$

Here \(\epsilon_a^{cmp}\) measures comparison-map error,
\(\epsilon_a^{proj}\) projective error, \(\epsilon_a^{br}\) bracket truncation
error, and \(\epsilon_a^{obs}\) observable readout error.

### Theorem 1.4: Smooth-Witness Zero Side

Assume a smooth projective finite deformation calculus and finite test sets
whose vector fields and lapses are sampled from a fixed compact smooth test
class.  Then for every smooth background metric \(h\) in the tested regular
class there exists a witness family \(q_a[h]\) such that

$$
{\mathcal A}_a(q_a[h])
\le
C_h(\epsilon_a^{def})^2.
$$

Consequently,

$$
a_a^*\to0.
$$

This is the conditional theorem

$$
\boxed{
\mathrm{V4P9\text{-}SMOOTH\text{-}WITNESS\text{-}ZERO}^{cond}.
}
$$

Proof.

The continuum hypersurface-deformation calculus satisfies the tangential,
mixed, and normal closure identities on smooth data:

$$
[D[v],D[w]]=D[[v,w]],
$$

$$
[D[v],H[N]]=H[v(N)],
$$

and

$$
[H[N],H[M]]
=
D[h^{ij}(N\partial_jM-M\partial_jN)].
$$

The finite maps approximate the continuum maps on the tested observable class
with error \(\epsilon_a^{cmp}\).  Their projective prolongations commute with
refinement up to \(\epsilon_a^{proj}\).  Their finite commutators approximate
the continuum commutators up to \(\epsilon_a^{br}\).  The observable readout
adds \(\epsilon_a^{obs}\).  Each Paper-7 residual is therefore bounded by
\(C_h\epsilon_a^{def}\) on the finite test set.  Squaring and summing gives
the displayed estimate.  Since \(\epsilon_a^{def}\to0\), the residual penalty
of the witness tends to zero, and the minimum is no larger than the witness
value.  `square`

### Barandes Audit 1.5

Theorem 1.4 is Barandes-aligned only as a finite approximation theorem.  The
finite maps \(D_a,H_a,P_{a\to b}\) and finite records \(g_a[h]\) are the
primitive objects.  Smooth \(h\), vector fields, and lapses are used as a
coherent external naming scheme for those finite records, not as hidden
ontology inside the stochastic law.

### Verdict 1.6

Route 1 succeeds conditionally.  It proves the zero side if the finite
architecture is declared or identified as a smooth projective deformation
calculus.

It does not yet prove that the actual V4 matter-geometry law has this
architecture.

## 2. Route 2: Prove A Positive Residual Floor

The floor side would assert that no admissible finite configuration can make
the residuals arbitrarily small.

### Definition 2.1: Positive Residual Floor

An architecture has a positive residual floor if

$$
\liminf_a a_a^*>0.
$$

For a source-conditioned sector \({\mathcal B}_a\subseteq C_a^{tot}\), define

$$
a_a^*({\mathcal B})
:=
\min_{q\in{\mathcal B}_a}{\mathcal A}_a(q).
$$

The conditioned floor is

$$
\liminf_a a_a^*({\mathcal B})>0.
$$

### Proposition 2.2: Universal Floor Is False Across Admissible
Architectures

There is no theorem of the form "every Barandes-aligned finite geometry
architecture has a positive residual floor."

Proof.

The smooth projective architecture of Definition 1.3 is finite,
record-based, and Barandes-aligned.  Theorem 1.4 gives residual-small
witnesses for it.  Hence a universal floor over all admissible finite
architectures is false.  `square`

### Definition 2.3: Dual Floor Certificate

Let

$$
{\mathcal R}_a(q)
:=
\bigl(R_{DD,a}^q,R_{DH,a}^q,R_{HH,a}^q,{\mathcal E}_{cov,a}^q\bigr)
$$

be the total residual vector in a finite normed residual space \(V_a\).  A
dual floor certificate on \({\mathcal B}_a\) is a linear functional
\(\Lambda_a\in V_a^*\) and a number \(\delta>0\) such that

$$
\|\Lambda_a\|_*\le1
$$

and

$$
\Lambda_a({\mathcal R}_a(q))\ge\delta
\qquad
\hbox{for all }q\in{\mathcal B}_a
$$

for all sufficiently fine \(a\).

### Theorem 2.4: Dual Certificate Implies Positive Floor

If a dual floor certificate exists on \({\mathcal B}_a\), then

$$
\liminf_a a_a^*({\mathcal B})\ge\delta^2.
$$

Proof.

For every \(q\in{\mathcal B}_a\),

$$
\delta
\le
\Lambda_a({\mathcal R}_a(q))
\le
\|\Lambda_a\|_*\|{\mathcal R}_a(q)\|
\le
\|{\mathcal R}_a(q)\|.
$$

Since \({\mathcal A}_a(q)=\|{\mathcal R}_a(q)\|^2\) in the chosen finite
residual norm, \({\mathcal A}_a(q)\ge\delta^2\).  Taking the minimum over
\({\mathcal B}_a\) gives the claim.  `square`

### Proposition 2.5: Current-Corpus Floor Is Not Sourced

The current V4 corpus does not contain a dual floor certificate for the
actual finite geometry/comparison architecture.

Proof.

Papers 4 and 5 construct enriched fixed-background metric and curvature
diagnostics.  Paper 6 allows finite geometry variables.  Paper 7 defines the
residuals.  Paper 8 defines the residual penalty.  None of these papers gives
a separating functional \(\Lambda_a\) that is positive on the residual vector
for every admissible configuration in a fixed source-conditioned sector.
Moreover, Theorem 1.4 shows that any attempted global floor must exclude or
condition away from smooth projective witnesses.  `square`

### Verdict 2.6

Route 2 fails as a universal theorem, but it remains valid as an
architecture-relative route.  To prove a floor one must exhibit an explicit
finite dual certificate for the declared architecture and sector.

## 3. Route 3: Reduce To Local Jet Algebra

The residuals are local comparison errors.  The natural finite decision
problem is therefore not mystical: it is a finite algebraic problem in the
local data of geometry records, comparison stencils, and source-conditioned
boundary records.

### Definition 3.1: Local Residual Jet

Fix a cell \(x\), a regulator \(a\), and a finite radius \(r\).  The local
residual jet

$$
J_{a,r}(q;x)
$$

is the finite tuple consisting of:

1. geometry record values in the \(r\)-neighborhood of \(x\);
2. comparison-map stencil coefficients in that neighborhood;
3. finite update-kernel entries visible to the Paper-7 residual tests;
4. source and boundary labels imposed by \({\mathcal B}_a\).

Let \({\mathcal J}_{a,r}({\mathcal B})\) be the finite set of local jets
allowed by the conditioned sector.

### Definition 3.2: Gluable Local Jet Field

A gluable local jet field is a finite assignment

$$
{\mathfrak J}_a=\{J_{a,r}(x)\}_{x\in\Lambda_a}
$$

such that:

1. overlapping neighborhoods agree on common geometry labels;
2. overlapping comparison stencils agree on common entries;
3. boundary and source labels match \({\mathcal B}_a\);
4. the field is realized by at least one global configuration
   \(q\in{\mathcal B}_a\), up to the declared tail error.

Let

$$
{\mathfrak J}_{a,r}^{glue}({\mathcal B})
$$

be the finite set of such gluable jet fields.

### Definition 3.3: Local Residual Polynomial

The finite residual map induces a local residual polynomial or table

$$
\rho_{a,r}:{\mathcal J}_{a,r}({\mathcal B})\to V_{a,r},
$$

where \(V_{a,r}\) is the finite local residual vector space.  It is called a
polynomial when the finite labels are embedded into coordinates; otherwise it
is simply a finite table.

### Theorem 3.4: Jet Reduction

Assume:

1. the Paper-7 residuals are \(r\)-local up to a tail \(\theta_a\to0\);
2. the finite residual norm is the sum or supremum of local residual norms;
3. source conditioning is local or has a finite boundary collar.

Then the conditioned residual minimum satisfies

$$
\left|
a_a^*({\mathcal B})
-
d_a({\mathcal B})^2
\right|
\le
C\theta_a,
$$

where

$$
d_a({\mathcal B})
:=
\inf_{{\mathfrak J}\in{\mathfrak J}_{a,r}^{glue}({\mathcal B})}
\left(
\sum_{x\in\Lambda_a}\|\rho_{a,r}({\mathfrak J}(x))\|^2
\right)^{1/2}.
$$

Proof.

By locality, evaluating the global residual on \(q\in{\mathcal B}_a\) differs
from evaluating the residual table on the associated gluable local jet field
by at most \(\theta_a\).  Conversely, by definition, every gluable jet field
is realized by a global configuration up to the same tail error.  Taking
norms and infima over admissible configurations and gluable jet fields gives
the displayed comparison.  The finite boundary collar accounts for the
source-conditioned constraints.  `square`

### Corollary 3.5: Algebraic Zero Certificate

If there are gluable local jet fields
\({\mathfrak J}_a\in{\mathfrak J}_{a,r}^{glue}({\mathcal B})\) such that

$$
\left(
\sum_{x\in\Lambda_a}\|\rho_{a,r}({\mathfrak J}_a(x))\|^2
\right)^{1/2}
\to0,
$$

and if the realizing configurations are projectively compatible, then

$$
a_a^*({\mathcal B})\to0.
$$

### Corollary 3.6: Algebraic Floor Certificate

If there exists \(\delta>0\) such that

$$
\left(
\sum_{x\in\Lambda_a}\|\rho_{a,r}({\mathfrak J}(x))\|^2
\right)^{1/2}
\ge\delta
\qquad
\hbox{for all }{\mathfrak J}\in{\mathfrak J}_{a,r}^{glue}({\mathcal B})
$$

for all sufficiently fine \(a\), then

$$
\liminf_a a_a^*({\mathcal B})\ge\delta^2.
$$

### Verdict 3.7

Route 3 converts the residual-minimum side decision into an exact finite
certificate problem:

$$
\boxed{
\mathrm{V4P9\text{-}JET\text{-}CERTIFICATE\text{-}REDUCTION}.
}
$$

It does not choose the side by itself.  It tells us what a proof of either
side must look like.

## 4. Route 4: Linearize Around Flat Geometry

Flat geometry is the fastest diagnostic because it tests whether the residual
floor is already visible before curvature appears.

### Definition 4.1: Flat Sector

A flat sector is a sequence \(q_a^{flat}\) whose geometry records approximate
the Euclidean spatial metric \(\delta_{ij}\), whose finite tangential
comparisons approximate translations and rotations, and whose normal
comparisons have the Euclidean structure-function coefficient

$$
h^{ij}(N\partial_jM-M\partial_jN)
$$

with \(h^{ij}=\delta^{ij}\) in the tested coordinate patch.

### Proposition 4.2: Flat Smooth Witness Has Vanishing Residual

In the smooth projective finite deformation calculus of Definition 1.3,

$$
{\mathcal A}_a(q_a^{flat})\to0.
$$

Proof.

Apply Theorem 1.4 to \(h=\delta\).  `square`

### Corollary 4.3: The Unconditioned Minimum Has A Flat Trap

If flat sectors are allowed in \(C_a^{tot}\) and the architecture admits
smooth projective witnesses, then

$$
a_a^*\to0
$$

even before one proves anything about nonflat dynamical geometry.

Proof.

The minimum is bounded above by the flat witness value.  Proposition 4.2
shows that this value tends to zero.  `square`

### Meaning 4.4: Why This Matters

The unconditioned zero side may be too easy.  It could mean only that the
finite architecture contains a nearly flat kinematic sector.  That does not
prove that the finite law realizes nontrivial GR dynamics, matter coupling,
or source-dependent geometry.

Therefore the meaningful side decision is:

$$
\boxed{
a_a^*({\mathcal B})\to0
\quad\hbox{or}\quad
\liminf_a a_a^*({\mathcal B})>0
}
$$

for source-conditioned sectors \({\mathcal B}_a\) encoding nontrivial metric,
matter, boundary, or curvature data.

### Definition 4.5: Linearized Residual Map

Let

$$
h_{ij}=\delta_{ij}+\varepsilon k_{ij}.
$$

For a compatible finite family \(q_a[\varepsilon k]\), expand the residual
vector:

$$
{\mathcal R}_a(q_a[\varepsilon k])
=
{\mathcal R}_{a}^{(0)}
+\varepsilon{\mathcal L}_a k
+O(\varepsilon^2).
$$

Here \({\mathcal L}_a\) is the finite linearized residual operator.

### Theorem 4.6: Linearized Side Test

For a source-conditioned class \({\mathcal B}_a(k)\) forcing the first-order
metric perturbation \(k\):

1. if \(\|{\mathcal R}_{a}^{(0)}\|\not\to0\), then there is a flat-level
   floor;
2. if \({\mathcal R}_{a}^{(0)}\to0\) but there exists a dual functional
   \(\Lambda_a\) with \(\|\Lambda_a\|_*\le1\) and

   $$
   \Lambda_a({\mathcal L}_a k)\ge\delta
   $$

   for all admissible \(k\) in the conditioned class, then there is a
   first-order floor of order \(\varepsilon^2\delta^2\);
3. if \({\mathcal R}_{a}^{(0)}\to0\) and \({\mathcal L}_a k\to0\) for a
   projectively gluable family realizing the conditioned \(k\), then the
   linearized zero route passes.

Proof.

The first item is immediate from the residual penalty.  The second item is
the dual certificate theorem applied to the linear term, with the residual
norm scaling as \(\varepsilon\delta\).  Squaring gives the
\(\varepsilon^2\delta^2\) floor.  The third item supplies a witness family
whose residual vector is \(o(1)\) at the demanded order.  `square`

### Verdict 4.7

Route 4 is decisive about the wrong question and diagnostic about the right
one:

1. it kills any universal unconditioned floor once flat smooth witnesses are
   admitted;
2. it reveals that Paper 9 must use source-conditioned minima;
3. it reduces the first nontrivial obstruction to the finite linearized
   operator \({\mathcal L}_a\) and its dual cokernel.

## 5. Route 5: Certified Finite Search

Every regulator problem is finite.  That makes the side decision, at each
fixed \(a\), a finite optimization problem.

### Definition 5.1: Finite Upper Certificate

An upper certificate for \(a_a^*({\mathcal B})\) is an admissible
configuration \(q\in{\mathcal B}_a\) together with interval-certified
residual evaluations proving

$$
{\mathcal A}_a(q)\le U_a.
$$

If \(U_a\to0\) along a projectively gluable certificate family, the zero side
holds.

### Definition 5.2: Finite Lower Certificate

A lower certificate is either:

1. exact enumeration of all \(q\in{\mathcal B}_a\);
2. a dual certificate \(\Lambda_a\);
3. a branch-and-bound certificate over local jets;
4. a convex or semialgebraic relaxation with certified remainder;

proving

$$
{\mathcal A}_a(q)\ge L_a
\qquad
\hbox{for all }q\in{\mathcal B}_a.
$$

If \(L_a\ge\delta>0\) for all sufficiently fine \(a\), the floor side holds.

### Algorithm 5.3: Certified Residual-Minimum Search

For each regulator \(a\):

1. define the finite conditioned sector \({\mathcal B}_a\);
2. compute or generate the finite residual table
   \({\mathcal R}_a(q)\);
3. search for an upper witness \(q_a\);
4. search for a lower dual or local-jet certificate;
5. prolong successful upper witnesses to the next regulator;
6. lift successful lower certificates through refinement.

### Theorem 5.4: Finite Certificate Soundness

If Algorithm 5.3 produces a projectively compatible sequence of upper
certificates \(U_a\to0\), then

$$
a_a^*({\mathcal B})\to0.
$$

If it produces lower certificates \(L_a\ge\delta>0\) stable under refinement,
then

$$
\liminf_a a_a^*({\mathcal B})\ge\delta.
$$

Proof.

Upper certificates are explicit witnesses, so the minimum is at most \(U_a\).
Lower certificates bound every admissible configuration from below, so the
minimum is at least \(L_a\).  Projective compatibility turns fixed-regulator
certificates into regulator-limit statements.  `square`

### Proposition 5.5: Computation Alone Is Not A Continuum Proof

Finite computation at finitely many regulators does not decide the continuum
side unless it produces a symbolic or projectively stable certificate family.

Proof.

A finite list of regulators can always be followed by different behavior at
later regulators.  Paper 8's oscillating sequence example already shows this
danger.  The certificate must therefore include either a prolongation rule for
upper witnesses or a refinement-stable lower certificate.  `square`

### Verdict 5.6

Route 5 is the practical engine for Route 3.  It can settle a declared finite
architecture, but only with certified asymptotic structure.  Numeric evidence
without a projective certificate is evidence, not a theorem.

## 6. The Conditioned Minimum Is The Correct Target

### Definition 6.1: Source-Conditioned Sector

A source-conditioned sector \({\mathcal B}_a\subset C_a^{tot}\) is a finite
subset defined by ordinary finite records:

1. boundary metric readouts;
2. matter/source labels;
3. curvature-probe labels;
4. orientation-quorum records;
5. fixed finite support and regularity constraints;
6. projective compatibility conditions.

No continuum equation is imposed.  The sector only says which finite records
the law is asked to realize.

### Definition 6.2: Conditioned Residual Side Decision

The meaningful Paper-9 side decision is:

$$
\boxed{
\mathrm{V4P9\text{-}COND\text{-}ZERO}({\mathcal B})
\quad\hbox{or}\quad
\mathrm{V4P9\text{-}COND\text{-}FLOOR}({\mathcal B}).
}
$$

That is:

$$
a_a^*({\mathcal B})\to0
$$

or

$$
\liminf_a a_a^*({\mathcal B})>0.
$$

### Theorem 6.3: Why Conditioning Is Necessary

If flat smooth witnesses are admissible, the unconditioned minimum can vanish
without proving nontrivial GR-like dynamics.  Therefore any theorem intended
to support dynamical ISP-GR must be stated for source-conditioned sectors
whose records force the desired nontrivial geometry or matter response.

Proof.

Corollary 4.3 proves the unconditioned flat trap.  A vanishing unconditioned
minimum then may only show that the finite architecture contains a flat or
kinematic sector.  Paper 7's GR-like conclusion requires continuum
identification and dynamical covariance in the target sector.  Those
requirements are not guaranteed by an unconstrained minimum.  Conditioning is
the finite-record way to state the target sector without importing continuum
equations.  `square`

## 7. Full Five-Route Settlement

### Theorem 7.1: Paper-9 Five-Route Settlement

The five routes have the following outcomes.

| Route | Result | Settlement |
|---|---|---|
| Construct witnesses | conditional positive | smooth projective finite deformation calculus gives \(a_a^*\to0\) |
| Prove floor | no universal floor; conditional floor possible | requires finite dual certificate on a conditioned sector |
| Local jet algebra | exact reduction | zero/floor becomes local finite table or polynomial certificate |
| Flat linearization | exposes flat trap | unconditioned zero may be trivial; conditioned linearized operator is the first real test |
| Certified finite search | sound certificate engine | proves either side only with projective upper or lower certificates |

Proof.

The witness route is Theorem 1.4.  The floor route is Proposition 2.2 and
Theorem 2.4.  The local algebra route is Theorem 3.4.  The flat route is
Corollary 4.3 and Theorem 4.6.  The computational route is Theorem 5.4 and
Proposition 5.5.  `square`

### Corollary 7.2: Current-Corpus Actual Side Is Not Sourced

The current corpus does not prove either

$$
\mathrm{V4P9\text{-}ACTUAL\text{-}CONDITIONED\text{-}ZERO}^{cur}
$$

or

$$
\mathrm{V4P9\text{-}ACTUAL\text{-}CONDITIONED\text{-}FLOOR}^{cur}.
$$

Proof.

The smooth witness theorem is conditional on identifying the declared finite
architecture with a projectively compatible deformation calculus.  The floor
route requires a dual certificate.  The local jet and computational routes
give certificate formats but not the missing certificate.  Therefore the
actual conditioned side is not yet sourced.  `square`

## 8. What Paper 9 Leaves As The Next Theorem

Paper 9 does not leave a vague obstruction.  It leaves a sharp fork.

### Positive Fork

Prove:

$$
\boxed{
\mathrm{V4P10\text{-}SOURCE\text{-}CONDITIONED\text{-}SMOOTH\text{-}REALIZABILITY}.
}
$$

Plainly: for each finite source-conditioned sector \({\mathcal B}_a\) that is
supposed to represent admissible nontrivial geometry/matter data, construct
projectively compatible smooth-witness configurations \(q_a\in{\mathcal B}_a\)
with

$$
{\mathcal A}_a(q_a)\to0.
$$

### Negative Fork

Prove:

$$
\boxed{
\mathrm{V4P10\text{-}DUAL\text{-}FLOOR\text{-}CERTIFICATE}.
}
$$

Plainly: construct finite dual functionals \(\Lambda_a\) proving that every
configuration in the target conditioned sector has residual penalty bounded
away from zero.

### Computational Fork

Build the local jet table and certificate search for the chosen finite
architecture:

$$
\boxed{
\mathrm{V4P10\text{-}JET\text{-}TABLE\text{-}CERTIFY}.
}
$$

This is not a third mathematical side.  It is the finite mechanism that can
prove either the positive fork or the negative fork.

## 9. Final Verdict

Paper 9 settles the five visible routes.

The unconditioned residual minimum can vanish in a Barandes-aligned finite
architecture by smooth or even flat witnesses.  Therefore a global positive
floor is not the right theorem.

The meaningful GR-facing theorem is conditioned:

$$
\boxed{
a_a^*({\mathcal B})\to0
\quad\hbox{or}\quad
\liminf_a a_a^*({\mathcal B})>0.
}
$$

The positive route is now concrete: prove source-conditioned smooth
realizability.  The negative route is also concrete: prove a finite dual
floor certificate.  The local jet and computational routes are the exact
certificate engines for those two outcomes.

The current-corpus status is:

$$
\boxed{
\mathrm{V4P9\text{-}ACTUAL\text{-}CONDITIONED\text{-}SIDE}^{cur}
\quad\hbox{not sourced}.
}
$$

But the attack surface is smaller and cleaner than after Paper 8.  The next
paper should no longer ask whether residual minima have an abstract
zero/floor dichotomy.  It should pick the target source-conditioned sector and
either build the smooth witness family or produce the dual floor certificate.
