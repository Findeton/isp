# Relativistic ISP V4 Paper 18: Support-Stability Consequences And The Value Frontier

Author: Felix Robles Elvira

Date: 2026-05-27

Status: Consequence paper after V4 Paper 17.  Paper 17 closed the current
licensed two-row support question under finite record covariance and finite
support stability.  This paper records what that closure buys, what it does
not buy, how it changes the V4 support hinge, and why the remaining V3-style
obstructions are value-level rather than support-level.

## Abstract

Paper 17 converts the missing-law problem from an unknown-value problem into
a support-stability problem.  Exact zeros are not allowed to appear silently
inside a licensed soft chamber.  Therefore, if both live rows are hard-in
with positive reference support and finite score, finite ISP predicts
two-row support unless a licensed hard support-killer is printed.

This paper explores the consequences.  It proves that the V4 support hinge is
closed at the current licensed level: the live rows have positive actual
mass under the finite support-stability law.  It also proves the limit of
this result: support-stability does not supply quantitative same-law values,
low-mode entries, Peter-Weyl tails, curvature constants, residual amplitudes,
or Ward/Stein coefficients.  It closes exact-zero ambiguity, not value
estimation.

The resulting frontier is sharp:

$$
\boxed{
\hbox{support questions are decided by hard support data;}
\qquad
\hbox{value questions require same-law value theorems.}
}
$$

## 0. Imports From Paper 17

### Import 0.1: Finite Support-Stability Closure

Paper 17 proves the conditional support closure:

$$
\boxed{
\mathrm{FINITE\text{-}RECORD\text{-}COVARIANCE}
+
\mathrm{FINITE\text{-}SUPPORT\text{-}STABILITY}
+
\mathrm{CURRENT\text{-}LICENSED\text{-}HARD\text{-}TABLE}
\Longrightarrow
\widehat m_0>0,\quad \widehat m_1>0.
}
$$

The current licensed hard table is:

$$
\boxed{
\begin{array}{c|c|c|c|c|c}
\hbox{row} & C & \rho & S^{eff} & B_{\mathrm{bdry/source}}
& Q_{\mathrm{quot}}\\ \hline
q_0 & 0 & >0 & <\infty & \hbox{in} & \hbox{in}\\
q_1 & 0 & >0 & <\infty & \hbox{in} & \hbox{in}.
\end{array}
}
$$

### Import 0.2: Exhaustive Escape List

Paper 17 also proves that avoiding two-row support requires exactly one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{E1}:&\hbox{print a hard support-killer }C,\rho,S,B,Q,\\[1mm]
\mathrm{E2}:&\hbox{deny the full-support anchor},\\[1mm]
\mathrm{E3}:&\hbox{deny support stability},\\[1mm]
\mathrm{E4}:&\hbox{add a hidden non-record support mask},\\[1mm]
\mathrm{E5}:&\hbox{show the two rows are not in one conditioned finite support
problem}.
\end{array}
}
$$

There is no sixth route.

### Import 0.3: Support Versus Value

The support-stability theorem decides whether a row has zero or positive
mass.  It does not decide the numerical mass:

$$
\boxed{
\widehat m_b>0
\quad\not\Longrightarrow\quad
\hbox{a useful lower floor, value, derivative, or coefficient estimate.}
}
$$

This distinction is the central discipline of Paper 18.

## 1. Einstein Consequence: Exact Zeros Are Structural

Einstein's lesson from Paper 17 is:

$$
\boxed{
\hbox{exact zero support is structural, not soft.}
}
$$

### Principle 1.1: Structural-Zero Principle

In finite ISP, a physical exact zero must be encoded by licensed finite
support data:

$$
\boxed{
P^{act}(q\mid R)=0
\quad\Longrightarrow\quad
C(q)\ne0
\hbox{ or }\rho(q)=0
\hbox{ or }S^{eff}(q)=\infty
\hbox{ or }B(q)=\hbox{out}
\hbox{ or }Q(q)=\hbox{out}.
}
$$

Equivalently, a hard-in finite record cannot be silently deleted.

### Theorem 1.2: Structural-Zero Principle Is Equivalent To No Hidden Support Mask

Assume finite record covariance and a full-support reference anchor on every
licensed hard chamber.  Then the following are equivalent:

1. finite support stability;
2. hard-support completeness;
3. no hidden support mask.

Proof.  Paper 17 proves support stability plus a full-support anchor implies
hard-support completeness.  Hard-support completeness says every hard-in row
is positive, so the support is exactly the licensed hard support set; hence
there is no hidden support mask.  Conversely, if there is no hidden support
mask, support is fixed by the licensed hard data.  Inside a licensed soft
chamber the hard data do not change, so support is stable.  `square`

### Corollary 1.3: The Actual Law Is Not Arbitrary Finite Probability

An arbitrary finite probability law may set

$$
\boxed{
P(q_0)=1,\qquad P(q_1)=0
}
$$

even when both rows are hard-in.  Such a law is not automatically a physical
finite ISP law.  It becomes physical only if the zero is licensed as hard
support data, or if finite ISP is enlarged by a hidden support-mask ontology.

This is the exact point where V4 stops being mere finite probability theory
and becomes a proposed physical law.

## 2. Feynman Consequence: The Smallest Stress Test

Feynman's test is the two-row chamber:

$$
\boxed{
K=\{q_0,q_1\},
\qquad
C_0=C_1=0,
\qquad
\rho_0,\rho_1>0,
\qquad
S_0,S_1<\infty,
\qquad
B_0=B_1=Q_0=Q_1=\hbox{in}.
}
$$

### Theorem 2.1: The Silent Singleton Is The Unique Minimal Falsifier

On the two-row chamber, a claimed physical law with

$$
\boxed{
P(q_0)>0,\qquad P(q_1)=0
}
$$

falsifies support stability unless it prints one hard support-killer for
\(q_1\).

Proof.  Since the chamber contains a full-support anchor, support stability
requires both rows to remain in support throughout the chamber.  A singleton
law changes support.  Therefore a hard wall must have been crossed.  The only
hard walls are \(C,\rho,S,B,Q\).  `square`

### Algorithm 2.2: Feynman Support-Killer Search

For any future singleton claim:

1. print the row table \(C,\rho,S^{eff},B,Q\);
2. if one row is hard-out, accept Einstein singleton selection;
3. if both rows are hard-in, reject singleton support;
4. if the claimed killer is \(U\) alone, reject selector bias;
5. if the claimed killer is residual/Bianchi/Ward, require a theorem that it
   is actual hard support data.

This is a finite checklist.  No path integral, hidden trajectory, or
intermediate Markov process is involved.

## 3. What V4 Now Closes

### Theorem 3.1: Current V4 Support Hinge Closure

Under finite record covariance and finite support stability, the V4
same-rectangle two-row support hinge is closed:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

Proof.  Paper 17 prints the final licensed hard table with both rows hard-in.
Apply Paper 17's support-stability closure theorem.  `square`

### Corollary 3.2: Instrument Readouts Are Not Support Sources

The Paper-16 write-register instrument remains a support microscope, not a
base support source.  Once support-stability gives

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0,
}
$$

the instrument can read both rows.  But it did not create their base support.

### Corollary 3.3: Soft Residual Penalties Do Not Kill Rows

Any finite residual penalty of the form

$$
\boxed{
e^{-\lambda{\mathcal A}(q)}
}
$$

with finite \(\lambda\) and finite residual \({\mathcal A}(q)\) reweights but
does not kill a row.  It becomes a support-killer only in a hard limit:

$$
\boxed{
\lambda=\infty
\quad\hbox{or}\quad
{\mathcal A}(q)=\infty
\quad\hbox{or}\quad
{\mathcal A}(q)=0\hbox{ is declared as }C(q)=0.
}
$$

### Corollary 3.4: Boundary/Source Endpoints Are The Only Soft-Looking Singleton Route

A source condition can create singleton support only when it is not merely a
finite soft weight but a boundary-face constraint:

$$
\boxed{
f\in\partial\operatorname{conv}F(K)
}
$$

and the active face meets only one row fiber.  Interior source points give
two-row support.

## 4. What V4 Does Not Close

Support-stability does not estimate values.

### No-Go 4.1: Positivity Does Not Give A Uniform Floor

From

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0
}
$$

one cannot infer a cofinal lower bound

$$
\boxed{
\widehat m_b\ge M_*>0.
}
$$

Finite positive masses may tend to zero along a refinement sequence without
ever becoming exactly zero.

### No-Go 4.2: Positivity Does Not Give Signed Or Scalar Values

Support-stability does not determine:

$$
\boxed{
m,\quad t,\quad \lambda_+,\quad \lambda_-,
\quad \hbox{RN-MIXAMP entries},
\quad \hbox{Peter-Weyl tails},
\quad \hbox{Ward/Stein coefficients}.
}
$$

These are value-level objects.  They require same-law estimates, not support
postulates.

### No-Go 4.3: Positivity Does Not Prove GR Dynamics

The support-stability theorem does not derive:

$$
\boxed{
\hbox{Einstein equations, finite constraint algebra closure, residual decay,
or continuum metric dynamics.}
}
$$

It only says which finite records are possible under the actual law.

## 5. What This Does To The V3 Obstruction

V3 repeatedly needed same-law numerical information.  Paper 18 now separates
the V3 obstruction into two classes.

### Definition 5.1: Support-Class Obstruction

A support-class obstruction asks whether a finite row is possible:

$$
\boxed{
P^{act}(q)>0\quad ?
}
$$

Support-stability can decide this when the hard table is printed.

### Definition 5.2: Value-Class Obstruction

A value-class obstruction asks for a numerical estimate:

$$
\boxed{
|m|<\epsilon,\quad t\ne0,\quad
\Theta+\kappa<\theta_{crit},\quad
\hbox{tail}\le\delta,\quad
\hbox{floor}\ge M_*.
}
$$

Support-stability does not decide these.

### Theorem 5.3: V3 Scalar-Ray Gaps Remain Value-Class

The scalar-ray obstruction \(B=cI_2\) is not solved by support-stability.
Even if the relevant rows are all positively supported, the scalar value
\(c\) may remain arbitrary without a Ward, residual, structural coupling, RP,
or floor theorem.

Proof.  Support-stability gives membership in support, not the value of a
same-law expectation or response coefficient.  The scalar ray is a value
degeneracy inside the supported sector.  `square`

### Theorem 5.4: V3 Same-Law Source-Response Remains Necessary For Values

Paper 31's source-response calculus remains necessary for value-level
questions.  Support-stability can say that the measure has support on the
rows being probed; it cannot bound the derivative of the source pressure:

$$
\boxed{
\partial_s\log\mathbb E^{act}e^{sV}\big|_{s=0}.
}
$$

Therefore V3's same-law value frontier is not erased.  It is correctly
classified.

## 6. Consequence For Residual, Bianchi, And Ward Routes

Residual, Bianchi, and Ward objects now have two possible roles.

### Role 6.1: Hard Support Data

They may act as hard support data only if the theory proves:

$$
\boxed{
\eta(q)=0
\quad\hbox{or}\quad
C^{Bianchi}(q)=0
\quad\hbox{or}\quad
C^{Ward}(q)=0
}
$$

is an actual admissibility condition defining the hard set.

Then they belong in \(C\).

### Role 6.2: Soft Score Or Diagnostic

If they enter only through finite penalties or finite readouts, then they are
soft:

$$
\boxed{
e^{-\lambda\eta(q)^2},\qquad
\lambda<\infty.
}
$$

They may reweight rows but cannot remove support.

### Theorem 6.3: Residual Hardness Is The Next Singleton Gate

Any future Einstein singleton route through residual/Bianchi/Ward must prove:

$$
\boxed{
\mathrm{ACTUAL\text{-}HARDNESS}
:
\hbox{the defect is part of the hard support definition, not merely a score.}
}
$$

Without actual hardness, the route cannot contradict Paper 17's two-row
support conclusion.

## 7. The New V4 Decision Tree

The support side of V4 now has a clean decision tree.

### Tree 7.1: Support Decision

For a proposed live row \(q\):

1. Is \(q\) in the conditioned finite record problem?
2. Is \(C(q)=0\)?
3. Is \(\rho(q)>0\)?
4. Is \(S^{eff}(q)<\infty\)?
5. Is \(q\) inside the boundary/source face?
6. Is \(q\) inside the quotient/superselection sector?

If yes to all:

$$
\boxed{
P^{act}(q)>0
}
$$

under finite record covariance and support stability.

If no to any:

$$
\boxed{
P^{act}(q)=0
}
$$

with the failed column as the hard support-killer.

### Tree 7.2: Value Decision

After support is decided, value questions require a different tree:

1. identify the same-law observable;
2. write its source pressure or conditional expectation;
3. prove a Ward/Stein, Dobrushin, Peter-Weyl, KP, RP, or dual-floor theorem;
4. otherwise classify the quantity as value-unsourced.

Support-stability is not a substitute for this tree.

## 8. What Einstein And Feynman Would Do Next

### Einstein Next

Einstein would make finite support stability an explicit physical principle
of V4:

$$
\boxed{
\hbox{physical exact zeros are invariant hard structure.}
}
$$

Then he would ask whether this principle follows from a deeper continuity
or covariance requirement in the projective/refinement limit.

The next Einstein theorem is:

$$
\boxed{
\mathrm{V4P18\text{-}PROJECTIVE\text{-}SUPPORT\text{-}STABILITY}.
}
$$

It should say that support chambers are preserved under refinement maps
unless a hard wall is crossed.

### Feynman Next

Feynman would try to falsify support stability by constructing an explicit
finite family:

$$
\boxed{
P_\epsilon(q_0)>0,\qquad
P_\epsilon(q_1)>0
\quad(\epsilon>0),
\qquad
P_0(q_1)=0,
}
$$

and then ask whether \(\epsilon=0\) crossed a hard wall.  If yes, good:
print it.  If no, finite support stability is false.

The next Feynman theorem is:

$$
\boxed{
\mathrm{V4P18\text{-}NO\text{-}SILENT\text{-}ZERO\text{-}LIMIT}.
}
$$

It should distinguish real hard limits from arbitrary zero masks.

## 9. Paper 18 Verdict

Paper 18's conclusion is:

$$
\boxed{
\hbox{Paper 17 closes the V4 support hinge, not the V3 value frontier.}
}
$$

More explicitly:

$$
\boxed{
\begin{array}{ll}
\hbox{Closed:}&\hbox{current licensed two-row support under support stability},\\[1mm]
\hbox{Not closed:}&\hbox{same-law values, floors, tails, scalar rays, and GR
dynamics}.
\end{array}
}
$$

At this stage the next useful work should not re-open the support table.  It
should either:

$$
\boxed{
\begin{array}{ll}
\mathrm{A}:&\hbox{derive projective support stability from refinement
covariance},\\[1mm]
\mathrm{B}:&\hbox{prove residual/Bianchi/Ward actual hardness},\\[1mm]
\mathrm{C}:&\hbox{return to value-level same-law theorems with the support
issue removed}.
\end{array}
}
$$

This is the cleanest map after the support-stability breakthrough.

Sections 10--14 now execute item A and the matching Feynman falsifier.  After
that execution, only items B and C remain as live directions.

## 10. Four-Step Closure Pass

This section executes the four-step program:

1. prove the Einstein support-stability theorem in the finite projective
   setting;
2. run the smallest Feynman falsifier;
3. promote support stability from a conditional assumption to a derived law
   whenever the projective hypotheses hold;
4. hand off the remaining work to value-level same-law estimates.

The point is to stop asking the same support question under new names.

## 11. Einstein Route: Projective Support Stability

### Definition 11.1: Finite Projective Record System

A finite projective record system is a directed family

$$
\boxed{
\left(
Q_a,\ \pi_{ab}:Q_b\to Q_a,\ H_a,\ \rho_a,\ S_a
\right)_{a\le b}
}
$$

where:

1. \(Q_a\) is the finite record set at scale \(a\);
2. \(\pi_{ab}\) is the record-forgetting or coarse-graining map;
3. \(H_a\subseteq Q_a\) is the hard admissible set;
4. \(\rho_a(q)\ge 0\) is the reference support density;
5. \(S_a(q)\in[0,\infty]\) is the effective finite score.

The actual law at scale \(a\) is

$$
\boxed{
P_a(q)
=
\frac{1}{Z_a}\,
1_{H_a}(q)\rho_a(q)e^{-S_a(q)}.
}
$$

A row is hard-live exactly when

$$
\boxed{
q\in H_a,\qquad \rho_a(q)>0,\qquad S_a(q)<\infty.
}
$$

### Definition 11.2: Projective Hard-Set Compatibility

The hard sets are projectively compatible when

$$
\boxed{
H_a=\pi_{ab}(H_b)
\qquad(a\le b).
}
$$

This says that refinement may reveal why a coarse row is impossible, but it
may not silently remove a coarse hard-live row.  If a row disappears under
refinement, the disappearance must be visible as a hard-set failure.

### Definition 11.3: Positive RN Transport

The reference-score package has positive Radon-Nikodym transport when, for
every \(a\le b\) and \(q\in H_a\) with \(\rho_a(q)>0\) and \(S_a(q)<\infty\),

$$
\boxed{
\sum_{r\in \pi_{ab}^{-1}(q)\cap H_b}
\rho_b(r)e^{-S_b(r)}
>0.
}
$$

Equivalently: a hard-live coarse row has at least one hard-live refined
realization.

### Definition 11.4: Projective Law Covariance

The actual laws are projectively covariant when

$$
\boxed{
(\pi_{ab})_*P_b=P_a
\qquad(a\le b).
}
$$

This is the finite ISP version of saying that changing resolution changes
description, not ontology.

### Theorem 11.5: Projective Support Stability

Assume:

1. finite projective record system;
2. projective hard-set compatibility;
3. positive RN transport;
4. projective law covariance.

Then support is stable under refinement:

$$
\boxed{
P_a(q)>0
\quad\Longleftrightarrow\quad
\exists r\in Q_b:
\pi_{ab}(r)=q,\ P_b(r)>0
}
$$

for every \(a\le b\).  In particular, an exact finite zero can appear only
through one of the printed hard columns:

$$
\boxed{
q\notin H_a
\quad\hbox{or}\quad
\rho_a(q)=0
\quad\hbox{or}\quad
S_a(q)=\infty.
}
$$

Proof.  If some refined row \(r\) has \(P_b(r)>0\) and \(\pi_{ab}(r)=q\),
then projective covariance gives

$$
P_a(q)=\sum_{r'\in\pi_{ab}^{-1}(q)}P_b(r')\ge P_b(r)>0.
$$

Conversely, if \(P_a(q)>0\), then \(q\in H_a\), \(\rho_a(q)>0\), and
\(S_a(q)<\infty\).  Positive RN transport gives a refined hard-live
\(r\in\pi_{ab}^{-1}(q)\cap H_b\).  For such \(r\),
\(\rho_b(r)>0\) and \(S_b(r)<\infty\), hence \(P_b(r)>0\).  This proves
the equivalence.

The final statement follows from the finite exponential form.  A finite
positive factor cannot turn a hard-live row into an exact zero.  Therefore a
zero must come from \(H\), \(\rho\), or \(S=\infty\). \(\square\)

### Corollary 11.6: No Silent Support Loss

Under Theorem 11.5, a row cannot be live at one finite description and dead
at a compatible finite description unless a hard support-killer is printed.

Thus:

$$
\boxed{
\mathrm{V4P18\text{-}PROJECTIVE\text{-}SUPPORT\text{-}STABILITY}
\quad\hbox{is proved under the finite projective hypotheses.}
}
$$

### Remark 11.7: What This Does Not Prove

The theorem does not say that a sequence of positive probabilities cannot
tend to zero:

$$
\boxed{
P_a(q_a)>0,\qquad P_a(q_a)\to0.
}
$$

That is a value-asymptotic statement, not a finite support statement.  It
becomes a support statement only if the limiting object is declared to be a
new hard finite law.  Then the limit must print the new hard wall.

## 12. Feynman Route: The Minimal Falsifier

Feynman's test is brutally small.  Take two coarse rows

$$
\boxed{
Q_0=\{q_0,q_1\}
}
$$

and one refinement

$$
\boxed{
Q_1=F_0\sqcup F_1,\qquad
\pi(F_i)=\{q_i\}.
}
$$

Try to make \(q_1\) vanish while every finite hard column says it is live.

### Test 12.1: Two-Row Two-Refinement Counterexample Attempt

Assume:

$$
\boxed{
q_1\in H_0,\qquad \rho_0(q_1)>0,\qquad S_0(q_1)<\infty.
}
$$

Assume also that the refined fiber is hard-live:

$$
\boxed{
\exists r\in F_1:
r\in H_1,\quad \rho_1(r)>0,\quad S_1(r)<\infty.
}
$$

Then the counterexample

$$
\boxed{
P_0(q_1)=0
}
$$

is impossible.

Proof.  The displayed refined row has \(P_1(r)>0\).  Projective covariance
therefore gives

$$
P_0(q_1)=\sum_{r'\in F_1}P_1(r')\ge P_1(r)>0.
$$

Contradiction. \(\square\)

### Test 12.2: The Only Feynman Escape

The minimal falsifier can work only by making one of the assumptions false.
Therefore it must print at least one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{F1}:&q_1\notin H_0,\\[1mm]
\mathrm{F2}:&\rho_0(q_1)=0,\\[1mm]
\mathrm{F3}:&S_0(q_1)=\infty,\\[1mm]
\mathrm{F4}:&F_1\cap H_1\hbox{ has no positive finite-score point},\\[1mm]
\mathrm{F5}:&(\pi_{01})_*P_1\ne P_0.
\end{array}
}
$$

These are not decorative exceptions.  They are the entire support-loss menu.

### Theorem 12.3: No-Silent-Zero Limit, Finite Version

In a finite projective system satisfying Theorem 11.5, there is no finite
silent zero.  More precisely, if a row has zero actual support at any finite
stage, then at that same stage or at a compatible refinement one can print a
hard support-killing column:

$$
\boxed{
P_a(q)=0
\quad\Longrightarrow\quad
q\notin H_a\ \hbox{or}\ \rho_a(q)=0\ \hbox{or}\ S_a(q)=\infty.
}
$$

Proof.  This is the contrapositive of the finite exponential law plus
positive RN transport.  If \(q\in H_a\), \(\rho_a(q)>0\), and
\(S_a(q)<\infty\), then \(P_a(q)>0\).  Therefore a zero requires failure of
one of those conditions. \(\square\)

### Corollary 12.4: The Feynman Falsifier Fails On The Current Paper-17 Table

Paper 17 prints the current hard-support table:

$$
\boxed{
\begin{array}{c|ccccc}
\hbox{row}&C&\rho&S^{eff}&B&Q\\
\hline
q_0&0&>0&<\infty&\mathrm{in}&\mathrm{in}\\
q_1&0&>0&<\infty&\mathrm{in}&\mathrm{in}.
\end{array}
}
$$

No Feynman singleton falsifier is available from this table.  A future
singleton theorem must add a new hard column and print its value.

## 13. Promotion To A Derived V4 Support Law

The conditional support-stability assumption can now be replaced by a derived
law whenever the finite projective hypotheses are part of the theory.

### Law 13.1: Finite Projective Support Law

For finite ISP record systems with:

1. projective finite records;
2. projectively compatible hard sets;
3. positive RN transport on hard-live rows;
4. projective law covariance;

the support of the actual law is exactly:

$$
\boxed{
\operatorname{supp}P_a
=
\{q\in Q_a:
q\in H_a,\ \rho_a(q)>0,\ S_a(q)<\infty\}.
}
$$

This is now a theorem inside that class, not a taste or ansatz.

### Theorem 13.2: Paper-17 Support Closure Becomes Derived

Under Law 13.1, the Paper-17 two-row conclusion follows without separately
postulating hard-support completeness:

$$
\boxed{
\widehat m_0>0,\qquad \widehat m_1>0.
}
$$

Proof.  Paper 17 prints \(q_0,q_1\) as hard-live in the current licensed
table.  Law 13.1 says hard-live is equivalent to positive actual support.
Therefore both rows have positive support. \(\square\)

### Corollary 13.3: What A Singleton Claim Must Now Do

Any future claim of singleton support must prove at least one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{S1}:&q_1\notin H,\\[1mm]
\mathrm{S2}:&\rho(q_1)=0,\\[1mm]
\mathrm{S3}:&S(q_1)=\infty,\\[1mm]
\mathrm{S4}:&q_1\hbox{ is outside the boundary/source face},\\[1mm]
\mathrm{S5}:&q_1\hbox{ is outside the quotient/superselection sector},\\[1mm]
\mathrm{S6}:&q_0,q_1\hbox{ were never in the same finite conditioned
problem}.
\end{array}
}
$$

If none of these is printed, singleton support is not a theorem.  It is an
unlicensed mask.

## 14. Handoff To The Value Frontier

Support work is now complete modulo explicit hard support-killers.

The remaining problems are value problems.  Their generic form is:

$$
\boxed{
\hbox{both rows live}
\quad\Longrightarrow\quad
\hbox{estimate their weights, signs, responses, tails, or curvatures}.
}
$$

The next papers should therefore attack one of the following value-level
primitive theorems.

### Target 14.1: Same-Law Scalar Ratio

Prove an actual same-law estimate of the form

$$
\boxed{
\frac{P(q_1)}{P(q_0)}
=
\frac{\rho(q_1)}{\rho(q_0)}
\exp\{-(S(q_1)-S(q_0))\}
}
$$

with the right controlled scalar entries, not merely positivity.

### Target 14.2: Ward/Stein Value Control

Prove a finite identity or inequality:

$$
\boxed{
|\mathbb E[Lf]-\mathbb E[\Gamma f]|
\le \varepsilon_a
}
$$

where the operator and error are licensed by the actual same-law finite
record law.

### Target 14.3: Residual Value Decay

Prove not just that residual defects are not hard support-killers, but that
their actual expected size decays:

$$
\boxed{
\mathbb E_{P_a}\|R_a\|^2\to0
}
$$

or print a positive residual floor.

### Target 14.4: Peter-Weyl Or Spectral Tail Control

Prove a same-law tail bound:

$$
\boxed{
\sum_{\lambda>\Lambda}
|\widehat P_a(\lambda)|^2
\le C\Phi(\Lambda,a)
}
$$

with \(\Phi\to0\) in the correct regime.

### Target 14.5: Source-Response Curvature

Prove that finite source derivatives compute the desired curvature or
response value:

$$
\boxed{
\partial_s^2\log Z_a(s)\big|_{s=0}
=
\hbox{licensed finite curvature/response}
+o(1).
}
$$

### Final Verdict 14.6: Stop Reopening Support

The Paper-18 closure pass gives the operational rule:

$$
\boxed{
\hbox{No hard support-killer printed?  Then support is closed.  Work on
values.}
}
$$

That is the Einstein/Feynman synthesis.  Einstein supplies the finite
projective support law.  Feynman supplies the smallest falsifier and shows
it cannot fire on the current table.  The next honest frontier is numerical
same-law control.

## 15. Value-Law Route: The Missing Object

The support problem is closed inside the finite projective class.  The value
problem asks for a different object.

The missing object is not another support table.  It is a finite calibrated
generating law:

$$
\boxed{
Z_a(J)
=
\sum_{q\in Q_a}
1_{H_a}(q)\rho_a(q)
\exp\{-S_a^{cal}(q)+\langle J,O_a(q)\rangle\}.
}
$$

Here:

1. \(H_a\) is the hard support set already controlled by Paper 17--18;
2. \(\rho_a\) is the positive reference support density;
3. \(S_a^{cal}\) is the calibrated finite value score;
4. \(O_a\) is the licensed finite source observable vector;
5. \(J\) is the finite source.

The corresponding law is:

$$
\boxed{
P_{a,J}^{cal}(q)
=
\frac{1}{Z_a(J)}
1_{H_a}(q)\rho_a(q)
\exp\{-S_a^{cal}(q)+\langle J,O_a(q)\rangle\}.
}
$$

This is the natural value analogue of the support ansatz.  The question is:
can it be made non-tautological?

Paper 17 answered the support version by requiring hard support data to be
licensed before the row signs are queried.  The value version must require
the same discipline:

$$
\boxed{
\hbox{the score and sources must be licensed before the desired value is
queried.}
}
$$

Otherwise any desired value can be fitted after the fact by hiding it in
\(S_a^{cal}\) or \(O_a\).

## 16. Einstein Route: Finite Least-Bias Value Principle

Einstein's move is to search for the principle that makes the value law
inevitable.  The finite candidate is relative entropy projection on the
already-closed hard support.

### Principle 16.1: Finite Least-Bias Value Principle

Fix a finite hard-live support set

$$
\boxed{
L_a=\{q\in Q_a:q\in H_a,\ \rho_a(q)>0,\ S_a^0(q)<\infty\}.
}
$$

Let the pre-calibrated prior be

$$
\boxed{
\mu_a^0(q)
=
\frac{1}{Z_a^0}1_{L_a}(q)\rho_a(q)e^{-S_a^0(q)}.
}
$$

Given licensed finite source observables

$$
\boxed{
O_a=(O_{a,1},\dots,O_{a,n})
}
$$

and licensed target values \(m_a\), the actual calibrated value law is the
least biased law among all laws \(P\) on \(L_a\) satisfying

$$
\boxed{
\mathbb E_P O_a=m_a.
}
$$

"Least biased" means minimizing relative entropy:

$$
\boxed{
D(P\|\mu_a^0)
=
\sum_{q\in L_a}P(q)\log\frac{P(q)}{\mu_a^0(q)}.
}
$$

This is not a support principle.  It is a value principle on the already
known support.

### Theorem 16.2: Finite Least-Bias Uniqueness

Assume:

1. \(L_a\) is finite and nonempty;
2. \(\mu_a^0(q)>0\) on \(L_a\);
3. the target \(m_a\) lies in the relative interior of the convex hull

$$
\boxed{
{\mathcal C}_a=\operatorname{conv}\{O_a(q):q\in L_a\}.
}
$$

Then there is a unique least-bias law \(P_a^*\).  It has exponential form:

$$
\boxed{
P_a^*(q)
=
\frac{1}{Z_a(\lambda)}
\mu_a^0(q)e^{\langle\lambda,O_a(q)\rangle}
}
$$

for a unique \(\lambda\), modulo source directions invisible on \(L_a\), with

$$
\boxed{
\nabla_\lambda\log Z_a(\lambda)=m_a.
}
$$

Proof.  The finite simplex on \(L_a\) is compact and
\(D(P\|\mu_a^0)\) is lower semicontinuous and strictly convex on the affine
constraint face modulo identical observable directions.  Since \(m_a\) is in
the relative interior of \({\mathcal C}_a\), the constraint face contains an
interior distribution and the minimizer has full support on \(L_a\).  The
Lagrange equations for minimizing \(D(P\|\mu_a^0)\) subject to normalization
and \(\mathbb E_P O_a=m_a\) give

$$
\log\frac{P(q)}{\mu_a^0(q)}
=
\alpha+\langle\lambda,O_a(q)\rangle,
$$

hence the displayed exponential form.  Strict convexity gives uniqueness of
the distribution. \(\square\)

### Corollary 16.3: The GR/SM Ansatz Becomes A Value Law If Calibration Is Licensed

If the licensed observables \(O_a\) and target values \(m_a\) are the finite
GR/SM calibration data, then the least-bias law is exactly the GR/SM-informed
finite exponential law:

$$
\boxed{
P_a^{GRSM}(q)
=
\frac{1}{Z_a}
1_{H_a}(q)\rho_a(q)
\exp\{-S_a^{GRSM}(q)\}.
}
$$

This is non-tautological only if \(O_a,m_a\), or equivalently
\(S_a^{GRSM}\), are licensed independently of the value being proved.

### No-Go 16.4: Least Bias Cannot License Its Own Constraints

The least-bias theorem does not tell us which observables \(O_a\) or targets
\(m_a\) are physically licensed.  If they are chosen after seeing the desired
answer, the theorem becomes a fitting lemma.

Therefore:

$$
\boxed{
\hbox{least bias closes the value-law form, but not the calibration source.}
}
$$

The remaining primitive is:

$$
\boxed{
\mathrm{VALUE\text{-}SOURCE\text{-}LICENSE}.
}
$$

## 17. Feynman Route: The Minimal Value Counterexample

Feynman's test is to show exactly why support cannot determine values.

Take the smallest hard-live support:

$$
\boxed{
L=\{q_0,q_1\}.
}
$$

Let

$$
\boxed{
H=L,\qquad S(q_0)=S(q_1)=0.
}
$$

For any \(r>0\), define a positive reference density

$$
\boxed{
\rho_r(q_0)=1,\qquad \rho_r(q_1)=r.
}
$$

Then

$$
\boxed{
\frac{P_r(q_1)}{P_r(q_0)}=r.
}
$$

Both rows are always live:

$$
\boxed{
P_r(q_0)>0,\qquad P_r(q_1)>0.
}
$$

But the value ratio is arbitrary.

### Theorem 17.1: Support Does Not Determine Same-Law Values

There is no theorem of the form

$$
\boxed{
\operatorname{supp}P=L
\quad\Longrightarrow\quad
\frac{P(q_1)}{P(q_0)}=\hbox{fixed number}
}
$$

without additional value data.

Proof.  The family \(P_r\) above has the same hard support for every
\(r>0\), but realizes every positive ratio \(r\). \(\square\)

### Corollary 17.2: The V3 Obstruction Reappears Exactly Here

The old v3 obstruction was not fundamentally "do the rows exist?"  It was:

$$
\boxed{
\hbox{what same-law mechanism fixes the relevant value?}
}
$$

Paper 18 has removed the support ambiguity.  It has not removed the value
freedom demonstrated by \(P_r\).

### Feynman Verdict 17.3

The value problem cannot be solved by staring harder at the support table.
It requires one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{V1}:&\hbox{a licensed finite score difference},\\[1mm]
\mathrm{V2}:&\hbox{a licensed source derivative of }\log Z,\\[1mm]
\mathrm{V3}:&\hbox{a Ward/Stein identity},\\[1mm]
\mathrm{V4}:&\hbox{a residual coercivity or floor theorem},\\[1mm]
\mathrm{V5}:&\hbox{a spectral/Peter-Weyl regularity theorem},\\[1mm]
\mathrm{V6}:&\hbox{a GR/SM calibration principle}.
\end{array}
}
$$

This is the complete Feynman menu for value control.

## 18. Source-Response Completeness

The imaginative move is to stop asking for individual values directly and
ask whether all relevant values are derivatives of one finite generating
object.

### Definition 18.1: Licensed Source Algebra

Let \({\mathcal O}_a\) be a finite vector space of licensed observables on
\(L_a\).  A value functional \(V_a\) is source-visible if there exists
\(O_V\in{\mathcal O}_a\) such that

$$
\boxed{
V_a(P)=\mathbb E_P O_V.
}
$$

It is second-source-visible if there exist \(O_1,O_2\in{\mathcal O}_a\) such
that

$$
\boxed{
V_a(P)=\operatorname{Cov}_P(O_1,O_2)
}
$$

or an equivalent second derivative of \(\log Z_a(J)\).

### Theorem 18.2: Finite Source Derivative Identities

For the calibrated law

$$
P_{a,J}(q)
=
\frac{1}{Z_a(J)}
\mu_a^0(q)e^{\langle J,O_a(q)\rangle},
$$

one has:

$$
\boxed{
\partial_{J_i}\log Z_a(J)=\mathbb E_{a,J}[O_{a,i}]
}
$$

and

$$
\boxed{
\partial_{J_i}\partial_{J_j}\log Z_a(J)
=
\operatorname{Cov}_{a,J}(O_{a,i},O_{a,j}).
}
$$

Proof.  Differentiate the finite sum defining \(Z_a(J)\). \(\square\)

### Corollary 18.3: Value Control Reduces To Source Completeness Plus Bounds

If every desired same-law value is source-visible or second-source-visible,
then all desired values are generated by \(Z_a(J)\).  Quantitative control
then reduces to bounding:

$$
\boxed{
\log Z_a(J),\qquad \nabla\log Z_a(J),\qquad \nabla^2\log Z_a(J)
}
$$

in the relevant source domain.

This is the Feynman-style viewpoint shift: the impossible value becomes a
source response.

### No-Go 18.4: Source Response Does Not Help Invisible Values

If a desired value functional \(V_a\) is not in the algebra generated by
licensed source observables, then \(Z_a(J)\) cannot determine it.

Proof.  Choose two laws on the same support with identical pushforward to
the source sigma-algebra generated by \({\mathcal O}_a\) but different
\(V_a\).  They have identical \(Z_a(J)\) for all licensed \(J\), but different
desired values. \(\square\)

Therefore the next primitive is:

$$
\boxed{
\mathrm{SOURCE\text{-}COMPLETENESS}.
}
$$

## 19. Ward/Stein Route

Source completeness tells us where values live.  Ward/Stein identities tell
us how to estimate them.

### Definition 19.1: Finite Stein Pair

A finite Stein pair for \(P_a\) is a pair \(({\mathcal L}_a,\Gamma_a)\) such
that, for a class \({\mathcal F}_a\),

$$
\boxed{
\mathbb E_{P_a}[{\mathcal L}_a f]
=
\mathbb E_{P_a}[\Gamma_a f]
}
$$

or, with defect,

$$
\boxed{
\left|
\mathbb E_{P_a}[{\mathcal L}_a f]
-
\mathbb E_{P_a}[\Gamma_a f]
\right|
\le \varepsilon_a\|f\|_{{\mathcal F}_a}.
}
$$

### Theorem 19.2: Stein Coercivity Gives Value Control

Assume a target value \(V_a\) admits a Stein equation

$$
\boxed{
{\mathcal L}_a f_a-\Gamma_a f_a
=
V_a-\bar V_a
}
$$

with

$$
\boxed{
\|f_a\|_{{\mathcal F}_a}\le C_a.
}
$$

If the Stein defect is \(\varepsilon_a\), then

$$
\boxed{
\left|\mathbb E_{P_a}V_a-\bar V_a\right|
\le C_a\varepsilon_a.
}
$$

Proof.  Insert \(f_a\) into the finite Stein defect inequality. \(\square\)

### No-Go 19.3: Ward Centering Alone Is Not Value Control

The identity

$$
\boxed{
\mathbb E_{P_a}R_a=0
}
$$

does not imply

$$
\boxed{
\mathbb E_{P_a}|R_a|^2\to0.
}
$$

The two-point law \(R=\pm1\) with equal probability has zero mean and unit
second moment.

Thus Ward centering must be strengthened to Stein coercivity, variance
control, or a spectral gap.

## 20. Residual Value Route

Residuals are now value objects unless they are promoted to hard
constraints.  The value theorem one wants is:

$$
\boxed{
\mathbb E_{P_a}{\mathcal A}_a\to0
}
$$

where \({\mathcal A}_a\) is the finite residual action or defect.

### Theorem 20.1: Residual Moment Equivalence

For nonnegative residual action \({\mathcal A}_a\), the following are
equivalent:

$$
\boxed{
\mathbb E_{P_a}{\mathcal A}_a\to0
\quad\Longleftrightarrow\quad
P_a({\mathcal A}_a>\delta)\to0
\quad\hbox{for all }\delta>0
}
$$

provided \({\mathcal A}_a\) is uniformly integrable.

Without uniform integrability, small probability high residual spikes can
destroy the moment.

### Theorem 20.2: Residual Penalty Gives Value Control Only At Low Temperature

If the actual law contains the residual penalty

$$
\boxed{
P_{a,\lambda}(q)
\propto
\mu_a^0(q)e^{-\lambda_a{\mathcal A}_a(q)}
}
$$

and if the reference law has residual-small witnesses with entropy cost
sublinear in \(\lambda_a\), then

$$
\boxed{
\mathbb E_{P_{a,\lambda}}{\mathcal A}_a
\le
\inf {\mathcal A}_a+o(1)
}
$$

as \(\lambda_a\to\infty\) in the admissible regime.

But if \(\lambda_a\) is finite or not part of the actual law, this theorem
does not apply.

### No-Go 20.3: Residuals As Soft Diagnostics Do Not Force Decay

A finite diagnostic \(R_a(q)\) can be measured without being suppressed.
Therefore:

$$
\boxed{
\hbox{residual visibility}\not\Rightarrow\hbox{residual decay}.
}
$$

The missing primitive is a residual score, residual Ward/Stein coercivity,
or residual Lyapunov principle.

## 21. Spectral/Peter-Weyl Route

If the value problem is a tail problem, the missing theorem is regularity.

### Definition 21.1: Finite Spectral Regularity

Let

$$
\boxed{
P_a=\sum_{\lambda}\widehat P_a(\lambda)\phi_{a,\lambda}
}
$$

be the finite Peter-Weyl or spectral expansion.  A regularity estimate is:

$$
\boxed{
\sum_{\lambda>\Lambda}
|\widehat P_a(\lambda)|^2
\le \Phi_a(\Lambda)
}
$$

with \(\Phi_a(\Lambda)\to0\) in the target regime.

### Theorem 21.2: Spectral Gap Plus Energy Bound Gives Tail Control

If a finite positive operator \(\Delta_a\) has eigenvalues \(\lambda\) and

$$
\boxed{
\mathbb E_{P_a}[\Delta_a]\le E_a,
}
$$

then

$$
\boxed{
\sum_{\lambda>\Lambda}
|\widehat P_a(\lambda)|^2
\le
\frac{E_a}{\Lambda}.
}
$$

This is the finite Markov/Chebyshev spectral bound.

### No-Go 21.3: Peter-Weyl Decomposition Alone Is Empty

Every finite function has a finite spectral expansion.  Without an energy,
Sobolev, heat-kernel, or representation-growth estimate, the expansion gives
no tail control.

The missing primitive is:

$$
\boxed{
\mathrm{SAME\text{-}LAW\text{-}REGULARITY}.
}
$$

## 22. GR/SM Calibration Route

The GR/SM-informed route is legitimate only if used as calibration, not as a
secret answer key.

### Principle 22.1: Finite GR/SM Calibration

The finite calibrated score \(S_a^{GRSM}\) is licensed when it is obtained
from a declared finite approximation to GR/SM data:

$$
\boxed{
S_a^{GRSM}
=
S_a^{EH/Regge}
+S_a^{SM}
+S_a^{gauge\ fixing}
+S_a^{boundary}
+S_a^{counterterm}
}
$$

and each term is fixed before the target same-law value is queried.

### Theorem 22.2: Calibration Transfers Values, It Does Not Derive Them From ISP Alone

If \(S_a^{GRSM}\) is independently licensed and if the actual finite law is
the least-bias calibrated law, then same-law values are computable from
\(Z_a(J)\).  But the numerical GR/SM constants are imported as calibration
data unless a further ISP theorem derives them.

Thus:

$$
\boxed{
\hbox{GR/SM calibration closes the missing law pragmatically, not
ontologically.}
}
$$

This is acceptable if the V4 goal is ISP-GR/SM alignment.  It is not
acceptable if the goal is to derive all GR/SM constants from bare ISP.

### Feynman Test 22.3: Vary The Calibration

Change one calibrated coefficient \(c\) in \(S_a^{GRSM}\).  If all support
and covariance tests still pass but the target value changes, then that
coefficient is a genuine value input, not a derived consequence.

This test distinguishes:

$$
\boxed{
\hbox{structural ISP theorem}
\quad\hbox{from}\quad
\hbox{GR/SM calibrated model choice}.
}
$$

## 23. Exhaustion Theorem For The Value-Law Route

The value-law route is now exhausted in the following precise sense.

### Theorem 23.1: Finite Value Control Exhaustion

Let \(V_a\) be a desired same-law value on the finite hard-live support
\(L_a\).  To prove a nontrivial estimate for \(V_a\), one must supply at
least one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{E1}:&\hbox{licensed score difference }S_a(q_1)-S_a(q_0),\\[1mm]
\mathrm{E2}:&\hbox{source visibility through }Z_a(J),\\[1mm]
\mathrm{E3}:&\hbox{finite Ward/Stein/coercive identity},\\[1mm]
\mathrm{E4}:&\hbox{residual Lyapunov, penalty, or moment theorem},\\[1mm]
\mathrm{E5}:&\hbox{spectral/regularity/tail estimate},\\[1mm]
\mathrm{E6}:&\hbox{GR/SM calibration data plus least-bias law},\\[1mm]
\mathrm{E7}:&\hbox{dual floor or dual value certificate}.
\end{array}
}
$$

If none is supplied, the value is unsourced.

Proof.  The two-row family in Theorem 17.1 shows that support alone cannot
fix the value.  Any value estimate must therefore use information beyond
support.  In a finite law, beyond-support information can enter only through
the score/reference ratio, source observables and derivatives, identities
constraining expectations, regularity/tail estimates, residual moment
principles, calibration data, or finite convex dual certificates.  These are
E1--E7.  If all are absent, two finite laws can be constructed with identical
support and identical licensed data but different \(V_a\), so no theorem can
distinguish them. \(\square\)

### Corollary 23.2: The Current Obstruction Is Not Mysterious

The obstruction has been reduced to a missing value source:

$$
\boxed{
\hbox{find E1--E7, or admit the value is not yet sourced.}
}
$$

This is the same class of obstruction v3 had, but now with the support
ambiguity removed.

## 24. Final Verdict On The Value-Law Route

The Einstein/Feynman value-law campaign gives a clean result.

### What It Proves

It proves:

$$
\boxed{
\begin{array}{l}
\hbox{finite least-bias principles force exponential calibrated laws;}\\
\hbox{source derivatives generate all source-visible values;}\\
\hbox{support alone cannot fix any nontrivial value;}\\
\hbox{any real value theorem must print one of E1--E7.}
\end{array}
}
$$

### What It Does Not Prove

It does not prove:

$$
\boxed{
\begin{array}{l}
\hbox{the GR/SM calibration constants from bare ISP;}\\
\hbox{residual decay without a residual value source;}\\
\hbox{Ward/Stein coercivity without a finite identity;}\\
\hbox{Peter-Weyl tails without same-law regularity;}\\
\hbox{a scalar ratio without a score/source/dual certificate.}
\end{array}
}
$$

### Final Operational Rule

The support rule was:

$$
\boxed{
\hbox{no hard support-killer printed, no singleton support theorem.}
}
$$

The value rule is:

$$
\boxed{
\hbox{no value source printed, no same-law value theorem.}
}
$$

So the next actual mathematical work is no longer generic philosophy.  It is
to pick one E-route and prove it:

$$
\boxed{
\mathrm{E1/E2/E3/E4/E5/E6/E7}.
}
$$

The most promising route, after the present paper, is:

$$
\boxed{
\mathrm{E2+E3}:
\hbox{source-response completeness plus Ward/Stein coercivity.}
}
$$

The most honest fallback is:

$$
\boxed{
\mathrm{E6}:
\hbox{declare GR/SM calibration as the finite value law and test its
consequences.}
}
$$

This closes the value-law route as far as Paper 18 can close it.  Further
progress requires one printed finite value source, not another reformulation
of support.
