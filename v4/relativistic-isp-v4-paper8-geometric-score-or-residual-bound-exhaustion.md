# Relativistic ISP V4 Paper 8: Geometric Score Or Residual Bound Exhaustion

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed Paper-8 route exhaustion.

## Abstract

V4 Paper 7 reduces the GR-facing problem to a finite source theorem:

$$
\boxed{
\hbox{source a finite geometric score or prove finite algebra residual
decay for the actual matter-geometry law.}
}
$$

Paper 8 exhausts the routes currently visible.

The verdict is precise.

1. **Arbitrary geometric scores fail.**  A Regge, Einstein-Hilbert, entropy,
   curvature, or detailed-balance score can be written down, but unless it is
   sourced from the finite same-law matter-geometry process, it is an external
   selection principle.

2. **Universal finite source scores exist but are tautological.**  Any
   differentiable finite source family has Radon-Nikodym scores, Fisher
   positivity, and Ward identities.  These are real but do not by themselves
   identify GR dynamics.

3. **The canonical current-corpus score is path-space likelihood.**  Given an
   actual finite kernel, one can form log-transition and entropy-production
   scores on two-slab records.  This is fully same-law and Barandes-aligned.
   But without additional symmetry or residual estimates, it does not imply
   finite constraint-algebra closure.

4. **The strongest positive route is a finite residual-penalty score.**  Build
   the score from Paper-7 residuals:

   $$
   {\mathcal A}_a
   :=
   \|R_{DD,a}\|^2+\|R_{DH,a}\|^2+\|R_{HH,a}\|^2
   +\|{\mathcal E}_{cov,a}\|^2.
   $$

   This score is finite, same-object, and does not import Einstein equations.
   A detailed-balance law using \({\mathcal A}_a\) concentrates on the
   residual-minimizing sector.  If the minimum tends to zero, Paper 7's
   conditional GR-like theorem applies.

5. **The current corpus does not prove that the minimum tends to zero for the
   actual law.**  It also does not prove that the actual law is the
   residual-penalty detailed-balance law.

Thus Paper 8 gives the first genuinely positive finite selection theorem:

$$
\boxed{
\mathrm{V4P8\text{-}RESIDUAL\text{-}PENALTY\text{-}SELECTION}^{cond}.
}
$$

It also gives the current-corpus verdict:

$$
\boxed{
\mathrm{V4P8\text{-}ACTUAL\text{-}RESIDUAL\text{-}DECAY}^{cur}
\quad\hbox{not sourced}.
}
$$

The residual-minimum issue has one subtlety.  For an arbitrary sequence of
regulators, the bare alternative "\(a_a^*\to0\) or positive floor" is false:
the minima could oscillate.  Paper 8 therefore proves the correct structural
dichotomy in the form actually needed by V4: after passing to the
tail-refinement envelope, and for projectively compatible residual-minimum
schemes, exactly one of the following holds:

$$
\boxed{
\hbox{residual minima vanish along the refinement system}
\quad\hbox{or}\quad
\hbox{there is a positive residual floor.}
}
$$

What remains after Paper 8 is not the abstract dichotomy.  It is deciding
which side of the dichotomy the actual finite geometry/comparison architecture
occupies.

## 0. Imports And Discipline

### Import 0.1: Paper-7 Residuals

V4 Paper 7 defines finite algebraic residuals

$$
R_{DD,a},\qquad R_{DH,a},\qquad R_{HH,a},
$$

and a dynamical covariance error for the total matter-geometry kernel.  It
proves:

$$
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cond}
$$

under finite algebra closure, dynamical covariance, stress Ward,
projectivity, constraint preservation, and continuum identification.

### Import 0.2: Paper-7 Current-Corpus No-Go

Paper 7 also proves:

$$
\mathrm{V4P7\text{-}GRLIKE\text{-}DYN}^{cur}
\quad\hbox{not sourced}.
$$

The reason is that Papers 4-6 allow many inequivalent geometry kernels,
including reset and random-walk kernels that do not preserve normal
constraint covariance.

### Barandes Rule 0.3

Paper 8 may use:

1. finite record spaces;
2. finite stochastic kernels;
3. Radon-Nikodym scores of finite same-law source families;
4. finite algebraic residuals already defined on record/effect spaces;
5. detailed-balance formulas only as finite probability assignments.

Paper 8 may not use:

1. Einstein-Hilbert or Regge action as an unsourced primitive;
2. Hilbert phase as ontology;
3. hidden Markov substeps inside a whole-process slab;
4. continuum GR equations as axioms;
5. the claim that an arbitrary score is physical because it has a geometric
   name.

The rule is:

$$
\hbox{the score must be finite same-law data, or it is only a benchmark guess.}
$$

## 1. What Counts As A Sourced Geometric Score?

### Definition 1.1: Finite Geometric Score

Let \(C_a^{tot}=C_a^{matter}\times C_a^{geom}\).  A finite geometric score is
a real function

$$
S_a:C_a^{tot}\to\mathbb R
$$

or a path-space function

$$
S_a:C_a^{tot}\times C_{a'}^{tot}\to\mathbb R
$$

whose dependence on \(g\) is nontrivial.

### Definition 1.2: Same-Law Sourced Score

A score \(S_a\) is same-law sourced if one of the following holds:

1. \(S_a\) is the Radon-Nikodym derivative

   $$
   S_a(q)=\partial_\alpha\log p_{\alpha,a}(q)\big|_{\alpha=0}
   $$

   of a declared finite source family on the same record law;

2. \(S_a\) is a log-transition or path likelihood score

   $$
   S_a(q,q')=-\log \Gamma_a(q'\mid q)
   $$

   for the actual finite kernel on the same record space;

3. \(S_a\) is an algebraic finite observable built from the actual finite
   comparison maps and kernels, such as the residual penalty defined in
   Section 5.

If \(S_a\) is merely copied from a continuum geometric action, it is not
same-law sourced.

### Definition 1.3: GR-Useful Score

A same-law score is GR-useful if it yields at least one of:

1. finite algebra residual decay;
2. dynamical covariance;
3. stress-response Ward identities;
4. concentration on an admissible geometry sector whose continuum limit has
   the Paper-7 GR-like structure.

Sourced is not enough.  The score must move one of the residual gates.

## 2. Route A: External Geometric Actions

### Candidate 2.1: Regge Or Einstein-Hilbert Score

One may define a finite score

$$
S_a^{EH}(g)
\approx
\int_\Sigma R(g)\sqrt{g}
$$

or a Regge-like curvature sum on the cell complex.

### Theorem 2.2: External Action Scores Are Not Sourced

The current corpus does not source

$$
\mathrm{V4P8\text{-}SOURCED\text{-}GEOM\text{-}SCORE}^{EH,cur}.
$$

Proof.

Papers 4 and 5 source metric readout and fixed-background operational
curvature.  Paper 6 makes geometry a finite configuration variable.  Paper 7
defines residual tests.  None of these proves that the probability of a
finite geometry record is weighted by a discretized Einstein-Hilbert or Regge
functional.  Importing such a score would choose GR dynamics by external
continuum analogy.  This violates the no-smuggling rule.  `square`

### Corollary 2.3: External Scores Are Benchmarks Only

Regge and Einstein-Hilbert scores may be useful benchmarks for later
comparison, but they do not solve Paper 8.

## 3. Route B: Universal Radon-Nikodym Source Scores

### Definition 3.1: Exponential-Tilt Source Family

Given any positive base law \(p_{0,a}(q)>0\) and any finite geometric
observable \(G_a(q)\), define

$$
p_{\alpha,a}(q)
:=
\frac{e^{\alpha G_a(q)}p_{0,a}(q)}
{\sum_{r}e^{\alpha G_a(r)}p_{0,a}(r)}.
$$

The score at \(\alpha=0\) is

$$
X_a(q)=G_a(q)-\mathbf E_0[G_a].
$$

### Proposition 3.2: Universal Scores Are Always Sourced Once The Source
Family Is Declared

The exponential-tilt family is a finite same-law source family, and its score
is the centered observable \(G_a-\mathbf E_0G_a\).

Proof.

The denominator normalizes the finite probability law.  Differentiating
\(\log p_{\alpha,a}(q)\) at \(\alpha=0\) gives \(G_a(q)\) minus the derivative
of the log partition function, which is \(\mathbf E_0G_a\).  `square`

### Proposition 3.3: Universal Scores Do Not Select GR Dynamics

The existence of the score in Proposition 3.2 does not imply Paper-7
finite algebra closure.

Proof.

The observable \(G_a\) was arbitrary.  Taking \(G_a=0\) gives a valid score
with no dynamical content.  Taking \(G_a\) to be any unrelated geometry label
also gives a valid score.  Therefore the universal source-score construction
is a calculus, not a dynamical selection theorem.  `square`

### Verdict 3.4

Universal finite source scores are real and Barandes-aligned, but they are too
cheap.  They do not exhaust the Paper-8 obstruction.

## 4. Route C: Actual Kernel Path-Space Scores

This is the first genuinely same-law route that does not require declaring an
external source.

### Definition 4.1: Actual Path Action

For an actual positive finite matter-geometry kernel

$$
\Gamma_a(q'\mid q)>0,
$$

define the one-slab path action

$$
{\mathcal L}_a(q,q'):=-\log \Gamma_a(q'\mid q).
$$

For a path \(q_0,\ldots,q_n\), define

$$
{\mathcal A}_a(q_0,\ldots,q_n)
:=
\sum_{k=0}^{n-1}{\mathcal L}_a(q_k,q_{k+1}).
$$

### Proposition 4.2: Path Action Is Same-Law Sourced

The path action is sourced by the actual finite kernel.

Proof.

It is the negative logarithm of the actual transition probability.  It is
defined entirely from the finite whole-process law on total records.  No
continuum action, Hilbert phase, or hidden intermediate factorization is
used.  `square`

### Definition 4.3: Entropy-Production Score

If a reference reverse kernel \(\Gamma_a^\dagger(q\mid q')\) is declared from
the same finite record law, define

$$
\Sigma_a(q,q')
:=
\log\frac{\Gamma_a(q'\mid q)}{\Gamma_a^\dagger(q\mid q')}.
$$

This is a finite path-space score.

### Proposition 4.4: Path Scores Do Not Imply Constraint Residual Decay

Actual path scores do not by themselves prove

$$
\|R_{DD,a}\|+\|R_{DH,a}\|+\|R_{HH,a}\|\to0.
$$

Proof.

Every positive finite kernel has a path action.  Paper 6's reset kernel and
random-walk kernel have path actions.  For generic reset or random-walk
choices, Paper 7's normal covariance and residual closure fail.  Therefore
the existence of an actual path action is not enough to prove residual decay.
`square`

### Conditional Theorem 4.5: Path Action Route

If the actual path action satisfies:

1. projective locality;
2. tangential covariance;
3. a finite variation identity whose Euler residual is Paper-7
   \(R_{DD},R_{DH},R_{HH}\);
4. coercivity forcing the residuals to zero in the refinement limit;

then it sources `V4P8-FIN-ALG-RESIDUAL-BOUND`.

Proof.

The assumptions identify the same-law path action as a finite dynamical
selection principle.  The variation identity relates action stationarity to
Paper-7 residuals, and coercivity turns stationarity into residual decay.
Paper 7's conditional theorem then applies.  `square`

### Verdict 4.6

The path-action route is genuinely same-law, but the current corpus does not
prove the required variation identity or coercivity.

## 5. Route D: Residual-Penalty Score

This is the most constructive route because it uses Paper-7 finite residuals
themselves rather than importing a continuum action.

### Definition 5.1: Finite Residual Penalty

Fix finite test sets \({\mathcal T}_{DD,a},{\mathcal T}_{DH,a},{\mathcal T}_{HH,a}\)
and a finite observable norm.  Define

$$
{\mathcal A}_a(q)
:=
\sum_{(v,w)\in{\mathcal T}_{DD,a}}\|R_{DD,a}^{q}[v,w]\|^2
+\sum_{(v,N)\in{\mathcal T}_{DH,a}}\|R_{DH,a}^{q}[v,N]\|^2
+\sum_{(N,M)\in{\mathcal T}_{HH,a}}\|R_{HH,a}^{q}[N,M]\|^2
+\|{\mathcal E}_{cov,a}^{q}\|^2.
$$

Here \(R^q\) means that the residuals are evaluated in the finite sector
determined by the total record \(q=(m,g)\), and \({\mathcal E}_{cov,a}^q\) is
the Paper-7 dynamical covariance error in that sector.

The penalty is finite, nonnegative, and built entirely from finite comparison
maps and kernels.

### Proposition 5.2: Residual Penalty Is Same-Object And Barandes-Aligned

\({\mathcal A}_a\) is a finite same-object geometric score.

Proof.

It is a finite sum of finite operator norms of finite algebraic residuals
defined on finite record/effect spaces.  It uses the actual comparison maps,
geometry records, and covariance tests.  It does not import a continuum
action, Hilbert phase, or hidden intermediate hypersurface.  `square`

### Definition 5.3: Residual-Penalty Detailed-Balance Kernel

Let \(Q_a(q'\mid q)\) be a finite local proposal kernel preserving the
declared admissible configuration subset.  For \(\tau_a>0\), define

$$
\Gamma_a^{pen}(q'\mid q)
=
Q_a(q'\mid q)
\min\{1,\exp[-({\mathcal A}_a(q')-{\mathcal A}_a(q))/\tau_a]\}
$$

for \(q'\ne q\), with the diagonal chosen so columns sum to one.

### Proposition 5.4: Penalty Kernel Is A Finite Whole-Process Law

\(\Gamma_a^{pen}\) is a finite stochastic kernel on total records.

Proof.

The off-diagonal entries are nonnegative and at most \(Q_a(q'\mid q)\).  The
diagonal entry is defined as one minus the sum of off-diagonal entries in the
column.  Hence every column sums to one and all entries are nonnegative.
`square`

### Definition 5.5: Residual Minimum

Let

$$
a_a^*:=\min_{q\in C_a^{tot}}{\mathcal A}_a(q).
$$

Let

$$
{\mathcal M}_a(\delta)
:=
\{q:{\mathcal A}_a(q)\le a_a^*+\delta\}.
$$

### Theorem 5.6: Residual-Penalty Selection

Assume \(Q_a\) is irreducible on the admissible finite sector and reversible
with respect to a positive reference measure \(\mu_a\).  Then
\(\Gamma_a^{pen}\) is reversible with respect to

$$
\pi_{a,\tau_a}(q)
:=
\frac{\mu_a(q)e^{-{\mathcal A}_a(q)/\tau_a}}
{\sum_r\mu_a(r)e^{-{\mathcal A}_a(r)/\tau_a}},
$$

and this stationary distribution concentrates on residual minimizers as
\(\tau_a\to0\):

$$
\pi_{a,\tau_a}\bigl({\mathcal M}_a(\delta)\bigr)\to1
$$

for every fixed \(\delta>0\).

Proof.

The proposal reversibility identity

$$
\mu_a(q)Q_a(q'\mid q)=\mu_a(q')Q_a(q\mid q')
$$

and the usual Metropolis acceptance ratio imply detailed balance for
\(\pi_{a,\tau_a}\).  Since the admissible sector is finite and \(Q_a\) is
irreducible, this stationary distribution is unique.  The ratio of the total
stationary weight outside \({\mathcal M}_a(\delta)\) to the weight of a
minimizer is bounded by a finite constant times \(\exp[-\delta/\tau_a]\),
which tends to zero.  `square`

### Corollary 5.7: Conditional Residual Decay

If

$$
a_a^*\to0
$$

and \(\tau_a\to0\) slowly enough for the chosen finite sampling/selection
scheme to concentrate on \({\mathcal M}_a(\delta_a)\) with
\(\delta_a\to0\), then

$$
{\mathcal A}_a\to0
$$

in probability under the residual-penalty law.  Consequently the finite
algebra residuals and covariance errors in the tested class vanish in
probability.

Proof.

By Theorem 5.6, the law concentrates on configurations with
\({\mathcal A}_a\le a_a^*+\delta_a\).  If both terms tend to zero, then the
nonnegative residual penalty tends to zero in probability.  Each residual
norm in the finite sum is bounded by \({\mathcal A}_a^{1/2}\), so the
individual tested residuals vanish.  `square`

### Theorem 5.8: Conditional Positive Paper-8 Theorem

If:

1. the residual-penalty law is adopted as the finite matter-geometry law;
2. the admissible finite sector is projectively compatible;
3. \(a_a^*\to0\);
4. the test sets exhaust the Paper-7 compactly supported tests;
5. the continuum identification hypotheses of Paper 7 hold;

then

$$
\mathrm{V4P8\text{-}RESIDUAL\text{-}PENALTY\text{-}SELECTION}^{cond}
$$

and Paper 7's `V4P7-GRLIKE-DYN^{cond}` applies.

Proof.

The residual penalty is a same-object finite score by Proposition 5.2.  The
penalty kernel is a finite whole-process law by Proposition 5.4.  Corollary
5.7 gives finite residual and covariance decay.  The exhaustion of test sets
promotes finite tested decay to Paper-7 finite algebra closure and dynamical
covariance.  Paper 7 then supplies the conditional GR-like conclusion.
`square`

### Verdict 5.9

This is the strongest positive Paper-8 result.  It is not the same as proving
that the pre-existing actual law has GR dynamics.  It constructs a
Barandes-aligned finite selection principle whose success reduces to the
mathematical question \(a_a^*\to0\).

## 5A. Residual-Minimum Dichotomy

The phrase "prove the residual-minimum dichotomy" needs one technical
clarification.  The bare statement is false for arbitrary regulator
sequences, but true for the refinement-compatible object that V4 actually
needs.

### Proposition 5A.1: The Bare Dichotomy Is False Without Refinement Control

For an arbitrary nonnegative regulator sequence \(a_n^*\), it is not true
that either

$$
a_n^*\to0
$$

or

$$
\liminf_n a_n^*>0.
$$

Proof.

Let

$$
a_{2n}^*=0,\qquad a_{2n+1}^*=1.
$$

Then \(\liminf_n a_n^*=0\), so there is no positive floor, but the full
sequence does not converge to zero.  Hence the bare dichotomy has a third
oscillatory possibility.  `square`

### Definition 5A.2: Tail-Refinement Envelope

For a refinement sequence \(a_n\to0\), define the tail envelope

$$
\underline a_n^*
:=
\inf_{m\ge n}a_m^*.
$$

This records the best residual minimum available at any sufficiently fine
regulator.

### Theorem 5A.3: Tail-Envelope Dichotomy

Exactly one of the following alternatives holds:

$$
\underline a_n^*\to0
$$

or

$$
\lim_{n\to\infty}\underline a_n^*>0.
$$

Equivalently, the refinement system either has arbitrarily fine
residual-small configurations or it has a positive tail floor.

Proof.

The sequence \(\underline a_n^*\) is nondecreasing in \(n\), because the tail
set \(\{m:m\ge n\}\) shrinks as \(n\) increases.  It is also nonnegative.
Therefore its limit exists in \([0,\infty]\).  If the limit is zero, the first
alternative holds.  If the limit is positive or infinite, choose any
\(\delta>0\) below that limit; then all sufficiently fine tails have residual
minimum at least \(\delta\).  `square`

### Definition 5A.4: Projectively Compatible Residual-Minimum Scheme

The residual-minimum scheme is projectively compatible if there exists a
sequence \(\omega_n\to0\) such that for all \(m\ge n\),

$$
a_m^*\le a_n^*+\omega_n.
$$

This means that a near-minimizer at a coarse regulator can be prolonged to
all sufficiently fine regulators with only vanishing residual-penalty loss.
It is the residual-minimum analogue of the projective compatibility
conditions already used in Papers 5 through 7.

### Theorem 5A.5: Projective Residual-Minimum Dichotomy

If the residual-minimum scheme is projectively compatible, then exactly one
of the following holds:

$$
a_n^*\to0
$$

or

$$
\liminf_n a_n^*>0.
$$

Proof.

Let \(L:=\liminf_n a_n^*\).  If \(L>0\), the second alternative holds.
Assume \(L=0\).  Fix \(\varepsilon>0\).  By the definition of liminf, choose
\(n\) such that

$$
a_n^*<\varepsilon/2.
$$

Choose \(n\) also large enough that \(\omega_n<\varepsilon/2\).  Then for
every \(m\ge n\), projective compatibility gives

$$
a_m^*\le a_n^*+\omega_n<\varepsilon.
$$

Thus \(a_m^*\to0\).  This proves the first alternative.  The alternatives are
mutually exclusive.  `square`

### Corollary 5A.6: Meaning For Paper 8

Paper 8 proves the structural residual-minimum dichotomy in the form required
for the V4 residual-penalty route:

1. without projective compatibility, the correct object is the tail envelope
   \(\underline a_n^*\);
2. with projective compatibility, the original minima \(a_n^*\) satisfy the
   desired dichotomy:

   $$
   a_n^*\to0
   \quad\hbox{or}\quad
   \liminf_n a_n^*>0.
   $$

The theorem does not decide which side holds.  It removes the oscillatory
loophole and reduces the next step to proving residual-small realizability or
a positive residual floor.

## 6. Route E: Direct Residual Bound For The Actual Law

### Definition 6.1: Actual Residual Decay

Write

$$
\mathrm{V4P8\text{-}ACTUAL\text{-}RESIDUAL\text{-}DECAY}
$$

if the actual finite matter-geometry law satisfies

$$
\|R_{DD,a}\|+\|R_{DH,a}\|+\|R_{HH,a}\|
+\|{\mathcal E}_{cov,a}\|\to0
$$

in the Paper-7 observable topology.

### Theorem 6.2: Direct Residual Decay Would Close The Paper-7 Gate

If `V4P8-ACTUAL-RESIDUAL-DECAY` holds together with metric reconstruction,
projectivity, stress Ward, constraint preservation, and continuum
identification, then `V4P7-GRLIKE-DYN^{cond}` applies to the actual law.

Proof.

This is exactly Paper 7's Hypothesis 5.1 with the algebra and covariance
parts supplied by the direct residual bound.  `square`

### Theorem 6.3: Direct Actual Residual Decay Is Not Sourced By The Current
Corpus

The current corpus does not prove

$$
\mathrm{V4P8\text{-}ACTUAL\text{-}RESIDUAL\text{-}DECAY}^{cur}.
$$

Proof.

Paper 6 exhibits allowed finite geometry kernels such as reset and random
walk kernels.  Paper 7 shows these can violate dynamical covariance and
normal constraint closure.  Papers 4 and 5 do not distinguish them because
they test metric readout and frozen-background curvature.  Therefore the
current corpus does not supply a theorem forcing the actual law's residuals
to vanish.  `square`

### Verdict 6.4

Direct residual decay is the cleanest target, but it is presently an
unsourced primitive theorem.

## 7. Route F: Constraint Projection Or Rejection

### Candidate 7.1: Projection Onto Residual-Small States

Define a subset

$$
{\mathcal K}_a(\epsilon)
:=
\{q:{\mathcal A}_a(q)\le\epsilon\}.
$$

Then reject moves leaving \({\mathcal K}_a(\epsilon)\).

### Proposition 7.2: Projection Preserves A Residual-Small Sector

If the process starts in \({\mathcal K}_a(\epsilon)\) and every move leaving
\({\mathcal K}_a(\epsilon)\) is rejected, then the process remains in
\({\mathcal K}_a(\epsilon)\).

Proof.

Accepted moves land in the set by definition.  Rejected moves leave the
state unchanged.  `square`

### Proposition 7.3: Projection Does Not Prove The Sector Is Nonempty Or
Continuum-GR-Like

Projection is not a source theorem for residual decay unless
\({\mathcal K}_a(\epsilon)\) is nonempty with \(\epsilon\to0\) and the
projected law has the required continuum interpretation.

Proof.

If \({\mathcal K}_a(\epsilon)\) is empty, projection cannot run.  If it is
nonempty only for \(\epsilon\) bounded away from zero, residual closure does
not follow.  If the set is populated by artifacts with no continuum
identification, Paper 7's GR-like conclusion does not apply.  `square`

### Verdict 7.4

Projection is a useful preservation tool, not a source of the residual-small
sector.

## 8. Route G: Stress Ward And Fisher Geometry

### Candidate 8.1: Fisher Metric On Geometry Sources

Given finite source parameters \(\alpha^A\), define scores \(X_A\) and Fisher
matrix

$$
I_{AB}=\mathbf E[X_AX_B].
$$

One may try to interpret \(I_{AB}\) as an information-geometric metric on the
space of finite geometry laws.

### Proposition 8.2: Fisher Positivity Is Too Weak

Fisher positivity and Ward Cauchy-Schwarz bounds do not imply finite algebra
residual decay.

Proof.

Every finite differentiable source family has a positive semidefinite Fisher
matrix.  Families built over reset kernels also have Fisher matrices, while
their normal covariance residuals can be nonzero.  Therefore Fisher geometry
alone does not select GR-like dynamics.  `square`

### Conditional Theorem 8.3: Fisher-Coercive Route

If a finite source family has a Fisher matrix that controls the Paper-7
residual vector \(R_a\) by a coercive inequality

$$
\|R_a\|^2\le C_a\, \mathbf E[X_A I^{AB}X_B]
$$

with \(C_a\) bounded and the right-hand side tending to zero under the actual
law, then actual residual decay follows.

Proof.

The displayed inequality directly bounds residual size by a same-law Fisher
quantity.  If that quantity tends to zero, so does the residual norm.
`square`

### Verdict 8.4

The Fisher route is conditional and potentially powerful, but the coercive
residual-control inequality is not sourced by the current corpus.

## 9. Route H: Noether/Ward Symmetry Alone

### Proposition 9.1: Tangential Symmetry Alone Cannot Force Normal Closure

Even exact finite tangential Ward symmetry does not force \(R_{HH,a}\to0\).

Proof.

Tangential symmetry constrains spatial relabeling.  \(R_{HH,a}\) compares two
normal deformation orders and includes the geometry-dependent structure
function.  A kernel may be tangentially invariant while resetting geometry
independently after each slab.  Such a kernel fails normal dynamical
covariance generically.  `square`

### Conditional Theorem 9.2: Full Deformation Ward Route

If a finite source law is covariant under the full finite deformation groupoid
generated by \(D_a[v]\) and \(H_a[N]\), and if the groupoid commutator
residuals are exactly Paper-7 residuals, then Ward differentiation gives
finite algebra residual identities.

Proof.

Differentiate the finite invariance identities for the whole deformation
groupoid.  The commutator of two infinitesimal deformations produces the
algebra residuals.  If invariance is exact up to vanishing regulator error,
the residual identities vanish in the tested topology.  `square`

### Verdict 9.3

Full deformation covariance would solve the problem, but it is essentially a
restatement of the missing Paper-7 dynamical covariance theorem.  It is not
currently sourced.

## 10. Exhaustion Table

| Route | Result | Why |
|---|---|---|
| External EH/Regge score | rejected as current proof | imports continuum dynamics |
| Universal RN score | true but too weak | arbitrary finite tilts do not select GR |
| Actual path action | same-law true, GR-useful conditional | needs variation/coercivity theorem |
| Residual-penalty score | conditional positive | finite score built from Paper-7 residuals |
| Direct actual residual bound | sufficient but unsourced | reset/random-walk counterfamilies remain |
| Constraint projection | preservation only | does not prove residual-small sector exists |
| Fisher/score geometry | conditional | needs coercive residual-control inequality |
| Tangential Ward alone | insufficient | does not control normal-normal residual |
| Full deformation Ward | sufficient but unsourced | equivalent to missing dynamical covariance |

## 11. Barandes Alignment Audit

### Proposition 11.1: Residual-Penalty Selection Is Barandes-Aligned

The residual-penalty route is Barandes-aligned.

Proof.

The score is built from finite algebraic residuals on finite record/effect
spaces.  The transition law is a finite stochastic whole-process assignment.
No hidden intermediate hypersurface state is assumed.  No Hilbert phase or
continuum Einstein action is primitive.  The continuum GR interpretation is
allowed only after residual decay and Paper-7 gates pass.  `square`

### Proposition 11.2: Residual-Penalty Selection Is Not Yet Actual ISP-GR

The residual-penalty route does not prove that the current actual
matter-geometry law already has GR dynamics.

Proof.

The route defines a candidate selection law.  To identify it with actual
ISP-GR, one must prove that the actual law is this penalty law, or prove
directly that the actual law has the same residual-decay consequence.  Neither
is currently sourced.  `square`

## 12. Final Settlement

### Theorem 12.1: Paper-8 Exhaustion

Paper 8 exhausts the currently visible score/residual routes:

1. external geometric scores are not current-corpus proofs;
2. universal source scores are real but too weak;
3. actual path scores are same-law but need variation/coercivity;
4. residual-penalty score gives a conditional positive selection theorem;
5. direct actual residual decay is sufficient but unsourced;
6. projection preserves residual-small sectors but does not create them;
7. Fisher and Ward routes are conditional unless they control Paper-7
   residuals;
8. the raw residual-minimum dichotomy is false without refinement control;
9. the tail-envelope and projective residual-minimum dichotomies are true;
10. the next theorem is to decide the zero side or the positive-floor side.

Proof.

Items 1 through 8 are Theorems and Propositions 2.2, 3.2, 3.3, 4.2, 4.4,
5.8, 5A.1, 5A.3, 5A.5, 6.2, 6.3, 7.2, 7.3, 8.2, 8.3, 9.1, and 9.2.
`square`

### Final Verdict 12.2

The strongest positive theorem is:

$$
\boxed{
\mathrm{V4P8\text{-}RESIDUAL\text{-}PENALTY\text{-}SELECTION}^{cond}.
}
$$

The current-corpus actual-law theorem is:

$$
\boxed{
\mathrm{V4P8\text{-}ACTUAL\text{-}RESIDUAL\text{-}DECAY}^{cur}
\quad\hbox{not sourced}.
}
$$

Paper 8 also proves the residual-minimum dichotomy, in the only form that is
mathematically valid for a regulator system.  The raw sequence may oscillate,
but the tail envelope always has the zero/floor dichotomy, and the original
minima have the same dichotomy under projective residual-minimum
compatibility:

$$
\boxed{
a_a^*=\min_q{\mathcal A}_a(q)\to0
\quad\hbox{or}\quad
\liminf_a a_a^*>0.
}
$$

Thus the next frontier is no longer to formulate the dichotomy.  It is to
decide which side holds.  If the zero alternative holds and the
residual-penalty law is accepted or identified with the actual law, V4 has a
concrete GR-like finite dynamics route.  If the floor alternative holds, the
residual-penalty strategy is blocked and V4 must either change the finite
geometry alphabet/comparison maps or accept an external-geometry/stochastic
geometry status.
