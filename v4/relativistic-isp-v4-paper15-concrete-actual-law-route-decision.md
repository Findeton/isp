# Relativistic ISP V4 Paper 15: Concrete Actual-Law Route Decision

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-27

Status: Paper-14 support-hinge follow-up.  Tests the five selected concrete
actual-law routes and then fuses the two live routes into one finite
instrument/Ward support table:

$$
\boxed{
\mathrm{P15\text{-}01}
\quad
\mathrm{P15\text{-}03}
\quad
\mathrm{P15\text{-}05}
\quad
\mathrm{P15\text{-}08}
\quad
\mathrm{P15\text{-}10}.
}
$$

The current-corpus verdict is sharp: the uniform and residual-minimum laws
are useful bounding models but not sourced as actual laws; finite rectangle
holonomy is the clean Einstein target but remains unproved; Ward constraints
and instrument support are the two most plausible non-tautological ways to
fill the support table without hidden route sampling.  The row-certificate
attack below also proves two useful exclusions: label-only instruments do
not count, and hyp-only Ward defects cannot select a singleton row.  The
instrument-outcome pass then shows that a current-corpus instrument outcome
is not an independent source unless it contributes a genuinely new finite
operational record.  The rectangle pass then reduces the best Einstein
geometry candidate to a sharp same-\(H^{NN}\) fork.  The final audit reduces
that fork to actual rectangle-fiber masses and, if those remain undecided,
to the residual row-defect record.

## Abstract

Paper 14 reduced the three-normal switch obstruction to one support hinge.
For a positive-mass hypersurface fiber \(h\), let

$$
\boxed{
{\mathcal A}^{NN}_{a,ij}(h)
}
$$

be the formally admissible NN values, and let

$$
\boxed{
{\mathcal S}^{NN}_{a,ij}(h)
:=
\{u:\mu^{NN}_{a,ij,h}(u)>0\}
}
$$

be the actually supported NN values.

Paper 14 proved that a two-valued actual support fiber gives a Feynman
floor, while singleton support gives Einstein hyp determinacy, with
rectangle singleton support giving the stronger finite holonomy theorem.
It did not determine the actual masses.

This paper tests five concrete route families.  Each route is judged by the
same finite support table:

$$
\boxed{
{\mathcal T}^{NN}_{a,ij}(h)
=
\{(u,A_u,m_u,\ell_u)\}_u,
\qquad
m_u=\mu^{NN}_{a,ij,h}(u).
}
$$

The decision rule is simple:

$$
\boxed{
\begin{array}{c}
\hbox{two positive }m_u
\Longrightarrow
\hbox{Feynman floor},\\[1mm]
\hbox{one positive }m_u\hbox{ for a licensed reason}
\Longrightarrow
\hbox{Einstein support selection}.
\end{array}
}
$$

The honest result is that no current-corpus route fills the table
unconditionally.  But Paper 15 does reduce the next useful work to one
shared finite decision target with two theorem projections, and then runs
the minimal two-row mask audit for that target:

$$
\boxed{
\mathrm{P15\text{-}IW\text{-}TABLE\text{-}REALIZATION}
\quad\hbox{with}\quad
\mathrm{P15\text{-}WARD\text{-}SUPPORT\text{-}THEOREM}
\quad\hbox{or}\quad
\mathrm{P15\text{-}INSTRUMENT\text{-}SUPPORT\text{-}THEOREM}.
}
$$

These are preferable to another abstract fork because they force Feynman's
row-by-row experiment and Einstein's invariant explanation to inspect the
same finite object.

## 0. Imports And Discipline

### Import 0.1: Paper-14 Support Hinge

For fixed \(a,i,j,h\), Paper 14 defines:

$$
\boxed{
{\mathcal A}^{NN}_{a,ij}(h)
\quad\hbox{and}\quad
{\mathcal S}^{NN}_{a,ij}(h).
}
$$

The support hinge is:

$$
\boxed{
{\mathcal A}^{NN}_{a,ij}(h)
\quad\hbox{versus}\quad
{\mathcal S}^{NN}_{a,ij}(h).
}
$$

Formal admissibility is not actual support.  This is the key discipline of
Paper 15.

### Import 0.2: Barandes Alignment

Every route must use only:

1. actual finite records;
2. actual conditional probabilities under \(\mathbb P^{act}_a\);
3. licensed finite instruments;
4. finite constraints explicitly represented in the record ontology.

No route may use hidden sampled histories, hidden Markov transitions,
unrecorded continuum moves, or formal variables not realized as finite
same-law records.

### Import 0.3: V3 Warning

V3 repeatedly found the same failure mode:

$$
\boxed{
\hbox{formal coordinate freedom}
\not\Longrightarrow
\hbox{same-law value information}.
}
$$

In particular, source-response, residual, reflection-positive, and
Ward/Stein rewrites were useful only when paired with an actual same-law
theorem: a support theorem, exclusion theorem, Ward identity, score bound,
instrument protocol, or sign-coherent floor.

Paper 15 uses V3 only as a filter.  A route is deprioritized if it would
also have failed to source the V3 missing same-law values.

## 1. Universal Five-Step Route Test

Each route is tested by the following finite procedure.

### Definition 1.1: Minimal Two-Value Formal Fiber

A minimal two-value formal fiber is a positive-mass hyp value \(h\) such
that

$$
\boxed{
{\mathcal A}^{NN}_{a,ij}(h)
=
\{u_0,u_1\},
\qquad
u_0\ne u_1.
}
$$

Larger formal fibers are reduced to two-value subtests.

### Definition 1.2: Route Verdicts

A route is **Feynman-positive** if it proves

$$
\boxed{
\mu^{NN}_{a,ij,h}(u_0)>0,
\qquad
\mu^{NN}_{a,ij,h}(u_1)>0.
}
$$

A route is **Einstein-positive** if it proves exactly one value survives for
a licensed finite reason:

$$
\boxed{
{\mathcal S}^{NN}_{a,ij}(h)=\{u_*\}
}
$$

and the zero row is explained by a finite support-kernel record, a Ward
constraint, a rectangle loop record, or an explicit instrument obstruction.

A route is **model-only** if it defines a possible law but does not derive
that law from the current ontology.

A route is **not aligned** if it relies on hidden route sampling, unrecorded
noise, or an unlicensed selection principle.

### Lemma 1.3: Five-Step Route Test

For every route in this paper, it is enough to answer:

1. What is the law for \(m_u=\mu^{NN}_{a,ij,h}(u)\)?
2. Are both \(m_{u_0}\) and \(m_{u_1}\) positive?
3. If not, which licensed finite record forces the zero?
4. Does the proof use only actual finite records?
5. Would the same logic have supplied the missing V3 same-law values?

Proof.

Paper 14 proves the consequences of the support table.  Therefore Paper 15
does not need another structural fork; it needs only the table entries and
their licensed explanation.  `square`

## 2. Route P15-01: Uniform Admissible-Row Law

### Definition 2.1: Uniform Law

The uniform admissible-row law is

$$
\boxed{
\mu^{unif}_{a,ij,h}(u)
=
\frac{\mathbf 1_{\{u\in{\mathcal A}^{NN}_{a,ij}(h)\}}}
{\left|{\mathcal A}^{NN}_{a,ij}(h)\right|}.
}
$$

### Theorem 2.2: Uniform Law Is Feynman-Positive On Any Two-Value Fiber

If

$$
\boxed{
\left|{\mathcal A}^{NN}_{a,ij}(h)\right|\ge2,
}
$$

then the uniform law gives a Feynman two-row certificate.

For any two distinct admissible values \(u,v\),

$$
\boxed{
\mu^{unif}_{a,ij,h}(u)
=
\mu^{unif}_{a,ij,h}(v)
=
\frac{1}{\left|{\mathcal A}^{NN}_{a,ij}(h)\right|}
>0.
}
$$

Thus

$$
\boxed{
{\mathsf V}^{NN,ij\mid hyp}_a>0
}
$$

whenever the embedding distance between the two NN values is positive.

Proof.

Immediate from the definition of \(\mu^{unif}\) and Paper 14 Theorem 28.3.
`square`

### Proposition 2.3: Current-Corpus Status

The uniform law is not sourced by the current corpus.

It is a valid Feynman baseline, but it is not a theorem about
\(\mathbb P^{act}_a\).  It assumes the conclusion that all admissible rows
have actual support.

V3 input makes this suspect: V3 repeatedly showed that formal admissibility
or coordinate freedom did not produce same-law value information.

Thus:

$$
\boxed{
\mathrm{P15\text{-}01}
\hbox{ is model-valid and Feynman-positive, but current-corpus unsourced.}
}
$$

`square`

### Verdict 2.4

Use P15-01 only as a baseline.  If a later instrument or Ward theorem
proves relative full support, P15-01 becomes the correct finite-support
approximation.  By itself it does not unblock the theory.

## 3. Route P15-03: Zero-Temperature Minimum-Residual Law

### Definition 3.1: Minimum-Residual Law

Let

$$
\boxed{
R_{a,ij}(u,h)
}
$$

be a licensed finite residual score on admissible NN rows.  The
zero-temperature residual law is

$$
\boxed{
\mu^{min}_{a,ij,h}(u)>0
\Longleftrightarrow
u\in
\arg\min_{v\in{\mathcal A}^{NN}_{a,ij}(h)}
R_{a,ij}(v,h).
}
$$

When the minimizer set has \(k\) elements, the simplest normalized version is

$$
\boxed{
\mu^{min}_{a,ij,h}(u)
=
\frac{\mathbf 1_{\{u\in\arg\min R_{a,ij}(\cdot,h)\}}}
k}.
}
$$

### Theorem 3.2: Minimum Residual Gives Exact Selection/Floor Dichotomy

Under the minimum-residual law:

1. if the minimizer is unique, then Einstein hyp support selection holds;
2. if there are two or more minimizers with distinct NN values, then the
   Feynman floor holds.

Proof.

The support set is exactly the minimizer set.  Singleton support gives
Paper 14 hyp determinacy.  Multi-valued support gives Paper 14 local
support and positive conditional spread.  `square`

### Proposition 3.3: Current-Corpus Status

P15-03 is not proved by the current corpus.

Two separate inputs are missing:

1. \(R_{a,ij}(u,h)\) must be a licensed actual finite record or score;
2. the actual law must concentrate exactly on residual minimizers.

V4 Paper 8 already gave the analogous lesson for residual-penalty selection:
low-temperature concentration on residual minimizers is a conditional
selection theorem, not a current actual-law theorem.  V3 similarly warned
that residual scores were useful only after actual residual/Jacobian values
or Ward-score envelopes were sourced.

Thus:

$$
\boxed{
\mathrm{P15\text{-}03}
\hbox{ is the clean Einstein selection model, but current-corpus unsourced.}
}
$$

`square`

### Verdict 3.4

P15-03 is worth keeping because it is the simplest selected-support
alternative to the uniform law.  It should be tested by computing minimizer
degeneracy on the minimal formal fiber.  But it does not solve the problem
unless the residual score is itself actual and the law really is
zero-temperature selection.

## 4. Route P15-05: Finite Holonomy/Rectangle Law

### Definition 4.1: Rectangle Determinacy Law

The finite holonomy/rectangle law is

$$
\boxed{
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
=
K^{NN,loop}_{a,ij}(H^{NN,ij}_a)
}
$$

on actual support.

### Theorem 4.2: Rectangle Law Is Strong Einstein Determinacy

If the finite holonomy/rectangle law holds, then

$$
\boxed{
{\mathsf V}^{NN,ij\mid loop}_a=0,
\qquad
{\mathsf V}^{NN,ij\mid hyp}_a=0.
}
$$

Consequently no same-hyp different-NN Feynman witness exists for this
coordinate.

Proof.

This is Paper 14 rectangle determinacy.  If NN is a function of
\(H^{NN,ij}_a\), then it is also determined by any hyp packet containing or
determining the rectangle loop shadow.  `square`

### Proposition 4.3: Falsifier For The Rectangle Route

P15-05 is falsified by actual support for two rows \(q_0,q_1\) such that

$$
\boxed{
H^{NN,ij}_a(q_0)=H^{NN,ij}_a(q_1),
\qquad
\chi^{NN}_{a,ij}(C^{GCR,sw}_a(q_0))
\ne
\chi^{NN}_{a,ij}(C^{GCR,sw}_a(q_1)).
}
$$

This is stronger than a same-hyp witness because it freezes the rectangle
loop shadow itself.

### Proposition 4.4: Current-Corpus Status

The current corpus does not prove P15-05.

Paper 14 defined the normal rectangle loop shadow and proved the conditional
determinacy theorem, but it did not prove that \(H^{NN,ij}_a\) is complete
for the NN coordinate.  V3 finite holonomy and Peter-Weyl routes suggest
this is the right geometric object to test, but they do not supply the
missing same-law support table.

Thus:

$$
\boxed{
\mathrm{P15\text{-}05}
\hbox{ is the best GR-facing Einstein route, but open.}
}
$$

`square`

### Verdict 4.5

P15-05 should be attacked by building the minimal rectangle table:

$$
\boxed{
{\mathcal T}^{NN,loop}_{a,ij}(\ell)
=
\{(u,m^\ell_u)\}_u.
}
$$

If every positive-mass \(\ell\)-fiber is singleton, Einstein wins.  If one
rectangle fiber has two NN values, P15-05 is falsified and Feynman gets a
stronger witness.

## 5. Route P15-08: Ward-Identity Constrained Law

### Definition 5.1: Ward-Constrained Support

Let

$$
\boxed{
W_{a,ij}(u,h)
}
$$

be a licensed finite Ward, conservation, or constraint defect.  The
Ward-constrained support law is

$$
\boxed{
\mu^{Ward}_{a,ij,h}(u)>0
\Longleftrightarrow
u\in{\mathcal A}^{NN}_{a,ij}(h)
\quad\hbox{and}\quad
W_{a,ij}(u,h)=0.
}
$$

### Theorem 5.2: Ward Law Gives Support-Exclusion Or Feynman Floor

Assume \(W_{a,ij}\) is a licensed actual finite record and that the
Ward-constrained support law holds.

If the zero set

$$
\boxed{
{\mathcal W}_{a,ij}(h)
:=
\{u\in{\mathcal A}^{NN}_{a,ij}(h):W_{a,ij}(u,h)=0\}
}
$$

has one element, then Einstein support selection holds.

If it has at least two distinct NN values, then the Feynman floor holds.

Proof.

Under the Ward-constrained law, the actual support fiber is exactly
\({\mathcal W}_{a,ij}(h)\).  Singleton support gives determinacy; multi-value
support gives local support.  `square`

### Proposition 5.3: Why This Route Is More Promising Than Uniform Support

P15-08 does not assume all formal rows are actual.  It gives a possible
reason why some formal rows have zero mass.

This matches the V3 lesson.  Paper 31's source-response calculus says
Ward identities can replace missing values only when the Ward score is an
actual same-law object and the Ward error is controlled.  Paper 30's
Ward/Stein route similarly remained valid but unsourced until the actual
residual-score pairings were supplied.

Thus P15-08 is not solved by V3, but it is exactly the kind of route V3
recommends.

### Proposition 5.4: Current-Corpus Status

The current V4 corpus does not print a specific \(W_{a,ij}\) whose zero set
equals the actual NN support fiber.

Therefore:

$$
\boxed{
\mathrm{P15\text{-}08}
\hbox{ is high-priority but open.}
}
$$

It becomes a proof only after one writes the finite Ward record and verifies
the equality

$$
\boxed{
{\mathcal S}^{NN}_{a,ij}(h)
=
\{u\in{\mathcal A}^{NN}_{a,ij}(h):W_{a,ij}(u,h)=0\}.
}
$$

`square`

### Verdict 5.5

P15-08 is the best analytic route.  It can prove either side and it respects
Barandes alignment, but it needs a concrete finite Ward identity.  Paper 15
therefore promotes the next analytic target:

$$
\boxed{
\mathrm{P15\text{-}WARD\text{-}SUPPORT\text{-}THEOREM}.
}
$$

## 6. Route P15-10: Empirical/Instrument Support Law

### Definition 6.1: Instrument Support

Let

$$
\boxed{
{\mathfrak I}_{a,ij}(h,u)
}
$$

be the finite set of licensed instrument protocols that realize a record
with hyp value \(h\) and NN value \(u\).

The instrument support law is

$$
\boxed{
\mu^{inst}_{a,ij,h}(u)>0
\Longleftrightarrow
{\mathfrak I}_{a,ij}(h,u)\ne\varnothing.
}
$$

### Theorem 6.2: Instrument Support Directly Fills The Table

If the instrument support law holds, then:

1. if there exist \(u\ne v\) with

   $$
   \boxed{
   {\mathfrak I}_{a,ij}(h,u)\ne\varnothing,
   \qquad
   {\mathfrak I}_{a,ij}(h,v)\ne\varnothing,
   }
   $$

   the Feynman floor holds;

2. if for every positive-mass \(h\) there is exactly one \(u\) with
   \({\mathfrak I}_{a,ij}(h,u)\ne\varnothing\), Einstein support selection
   holds.

Proof.

The instrument law identifies support with explicit operational
realizability.  The two cases are exactly the two cases of the Paper-14
support hinge.  `square`

### Proposition 6.3: Barandes Alignment

P15-10 is Barandes-aligned if and only if each protocol in
\({\mathfrak I}_{a,ij}(h,u)\) is a finite record-labelled instrument with
ordinary settings and outcomes.

It is not aligned if the "instrument" is merely a hidden route sampler or an
unrecorded normal history.

This matches the review notes: raw comparison maps, operational stochastic
instruments, and observables/effects must stay distinct.  Instrument support
is valid only at the operational instrument layer.

### Proposition 6.4: Current-Corpus Status

The current corpus has the operational-instrument framework, but it does not
construct a finite instrument protocol realizing two NN values in one hyp
fiber, nor does it prove that all such protocols are singleton.

Thus:

$$
\boxed{
\mathrm{P15\text{-}10}
\hbox{ is the best reality-check route, but open.}
}
$$

`square`

### Verdict 6.5

P15-10 is the most decisive route because it can fill the table by
construction.  Paper 15 promotes the operational target:

$$
\boxed{
\mathrm{P15\text{-}INSTRUMENT\text{-}SUPPORT\text{-}THEOREM}.
}
$$

## 7. Cross-Route Decision Table

The five selected routes now have the following status.

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{route} & \hbox{what proves it} & \hbox{what falsifies it} & \hbox{status}\\
\hline
\mathrm{P15\text{-}01} &
\hbox{declare uniform support} &
\hbox{no ontology for uniformity} &
\hbox{model-only}\\
\mathrm{P15\text{-}03} &
\hbox{actual zero-temperature residual selection} &
\hbox{mass on non-minimizer} &
\hbox{open/model}\\
\mathrm{P15\text{-}05} &
\chi^{NN}=K(H^{NN}) &
\hbox{same }H^{NN}\hbox{, different NN} &
\hbox{open}\\
\mathrm{P15\text{-}08} &
{\mathcal S}=\{W=0\} &
\hbox{Ward zero set mismatches support} &
\hbox{high-priority open}\\
\mathrm{P15\text{-}10} &
{\mathcal S}=\hbox{instrument realizability} &
\hbox{instrument set mismatches support} &
\hbox{high-priority open}
\end{array}
}
$$

The useful conclusion is that only P15-08 and P15-10 look like genuine
ways to add information without simply choosing a measure by fiat.

## 8. V3 Back-Propagation Test

A route is credible only if it would also have helped with the V3 problem:
missing same-law quantitative value information.

### Proposition 8.1: V3 Filter

The V3 corpus favors routes that supply actual finite source, Ward, or
instrument data.  It disfavors routes that merely reweight formal
admissible rows.

Consequently:

1. P15-01 would have solved V3 only by assuming full support, so it is weak.
2. P15-03 matches residual-minimum selection but still needs an actual
   residual selection theorem.
3. P15-05 is geometrically meaningful but does not address generic V3
   residual value gaps.
4. P15-08 matches V3's Ward/source-response lesson.
5. P15-10 matches V3's operational-instrument discipline.

Proof.

This is a structural comparison with V3 Papers 31, 32, 34, and the review
notes.  Those papers repeatedly conclude that passive reformulations do not
source missing same-law values; actual Ward identities, source controls,
instrument records, or sign-coherent floors are needed.  `square`

## 9. Shared Instrument/Ward Support Table

The previous sections leave two live routes:

1. Feynman's route: build the operational table and see which rows actually
   occur.
2. Einstein's route: find the invariant Ward/constraint reason why only
   those rows occur.

They should not be pursued as separate stories.  They should be forced onto
the same finite table.

### Definition 9.1: The Instrument/Ward Table

For fixed \(a,i,j,h\), define:

$$
\boxed{
{\mathcal T}^{IW}_{a,ij}(h)
:=
\{(u,A_u,I_u,W_u,m_u):u\in{\mathcal A}^{NN}_{a,ij}(h)\}.
}
$$

Here:

$$
\boxed{
\begin{array}{rl}
A_u &: \hbox{the formal admissibility witnesses for }u,\\
I_u &:=
\mathbf 1_{\{{\mathfrak I}_{a,ij}(h,u)\ne\varnothing\}},\\
W_u &:=
\mathbf 1_{\{W_{a,ij}(u,h)=0\}},\\
m_u &:=
\mu^{NN}_{a,ij,h}(u).
\end{array}
}
$$

\({\mathfrak I}_{a,ij}(h,u)\) is the set of finite operational instruments
whose record law produces the NN value \(u\) in fiber \(h\).  \(W_{a,ij}(u,h)\)
is the finite Ward/constraint defect assigned to that row.

The instrument support set is:

$$
\boxed{
{\mathcal S}^{inst}_{a,ij}(h)
:=
\{u\in{\mathcal A}^{NN}_{a,ij}(h):I_u=1\}.
}
$$

The Ward-zero set is:

$$
\boxed{
{\mathcal S}^{Ward}_{a,ij}(h)
:=
\{u\in{\mathcal A}^{NN}_{a,ij}(h):W_u=1\}.
}
$$

The desired actual-law identification is:

$$
\boxed{
{\mathcal S}^{NN}_{a,ij}(h)
=
{\mathcal S}^{inst}_{a,ij}(h)
=
{\mathcal S}^{Ward}_{a,ij}(h).
}
$$

This single equation is the sharpened target.  It says:

1. a row has positive same-law mass exactly when an operational finite
   record instrument realizes it;
2. the same row is allowed exactly when the Ward/constraint defect vanishes;
3. there is no hidden route sampler between operational support and invariant
   constraint support.

### Theorem 9.2: Shared Table Dichotomy

Assume the instrument/Ward table is complete and satisfies

$$
\boxed{
{\mathcal S}^{NN}_{a,ij}(h)
=
{\mathcal S}^{inst}_{a,ij}(h)
=
{\mathcal S}^{Ward}_{a,ij}(h)
}
$$

for every positive-mass \(h\).  Then:

1. if some \(h\) has at least two distinct rows in
   \({\mathcal S}^{inst}_{a,ij}(h)\), the Feynman floor route holds;
2. if every positive-mass \(h\) has exactly one row in
   \({\mathcal S}^{inst}_{a,ij}(h)\), the Einstein support-selection route
   holds;
3. if the singleton row is a function of the finite rectangle holonomy
   \(H^{NN}_{a,ij}(h)\), the GR-facing rectangle route holds.

Proof.

By the table identity, instrument-realized rows, Ward-zero rows, and
positive-mass actual rows are the same rows.  Paper 14's support hinge then
applies.  Two supported rows give a floor; singleton support gives
determinacy; rectangle-indexed singleton support gives finite holonomy
determinacy.  `square`

### Proposition 9.3: Current-Corpus Status

The current corpus does not prove the table identity.  More precisely:

1. it has the operational language needed to define
   \({\mathfrak I}_{a,ij}(h,u)\);
2. it has Ward/source-response language sufficient to name
   \(W_{a,ij}(u,h)\);
3. it does not provide the finite protocol catalogue needed to compute
   \(I_u\);
4. it does not provide the finite Ward defect formula needed to compute
   \(W_u\);
5. it does not prove that either computed set equals the actual mass support.

Thus the path is not solved, but it is no longer vague.  The obstruction has
become two finite construction problems and one equality check.

### Corollary 9.4: What Would Count As Real Progress

The next genuine advance is any one of the following:

$$
\boxed{
\begin{array}{ll}
\mathrm{P15\text{-}IW\text{-}TABLE\text{-}REALIZATION}:&
\hbox{compute all }I_u\hbox{ and }W_u\hbox{ for the minimal NN fibers},\\
\mathrm{P15\text{-}INSTRUMENT\text{-}SUPPORT}:&
{\mathcal S}^{NN}={\mathcal S}^{inst},\\
\mathrm{P15\text{-}WARD\text{-}SUPPORT}:&
{\mathcal S}^{NN}={\mathcal S}^{Ward},\\
\mathrm{P15\text{-}WARD\text{-}EXPLAINS\text{-}INSTRUMENT}:&
{\mathcal S}^{inst}={\mathcal S}^{Ward}.
\end{array}
}
$$

The fourth target is the best bridge target: it can be proved before the
actual masses are known.  If operational realizability and Ward admissibility
already agree on the finite table, then the actual-law problem is reduced to
one support theorem instead of two unrelated support theorems.

## 10. Feynman First, Einstein Second On The Same Table

The practical order should now be:

1. run Feynman's finite-row experiment;
2. only then ask for Einstein's invariant explanation of the rows that
   survived.

### Step 10.1: Feynman's Experiment

For each minimal positive-mass fiber \(h\), list the formal NN rows:

$$
\boxed{
u_1,\ldots,u_N\in{\mathcal A}^{NN}_{a,ij}(h).
}
$$

For each row \(u_r\), try to construct a finite record instrument

$$
\boxed{
{\mathfrak I}_{a,ij}(h,u_r)\ne\varnothing.
}
$$

This is deliberately concrete.  A proposed instrument must specify:

1. finite input records;
2. finite output records;
3. the operational stochastic map;
4. the readout producing \(u_r\);
5. the same-law status of the protocol.

If two different \(u_r\)'s pass, stop trying to force singleton
determinacy; Paper 14 gives the floor route.  If exactly one \(u_r\) passes,
ask whether that singleton is structural or merely an artifact of the chosen
protocol class.

### Step 10.2: Einstein's Explanation

After the instrument pass, define \(W_{a,ij}(u,h)\) so that it is:

1. finite;
2. invariant under allowed record relabellings;
3. local to the same boundary/normal data used by the table;
4. not an additional hidden selector.

Then test:

$$
\boxed{
{\mathcal S}^{inst}_{a,ij}(h)
\stackrel{?}{=}
\{u:W_{a,ij}(u,h)=0\}.
}
$$

If this equality holds, the Einstein route has explained the Feynman table.
If it fails, the mismatch is not a philosophical problem; it is an explicit
row-level defect.  Either the instrument catalogue is too narrow, the Ward
defect is wrong, or the actual law contains extra finite support data.

### Theorem 10.3: The Unblocking Criterion

The Paper-15 path is unblocked exactly when one of the following finite
outcomes is obtained:

$$
\boxed{
\begin{array}{ll}
\hbox{Feynman-positive:} &
\exists h,\ |{\mathcal S}^{inst}_{a,ij}(h)|\ge 2,\\
\hbox{Einstein-positive:} &
{\mathcal S}^{inst}_{a,ij}(h)
=
{\mathcal S}^{Ward}_{a,ij}(h)
\hbox{ is singleton for every }h,\\
\hbox{support-exclusion:} &
{\mathcal S}^{inst}_{a,ij}(h)
\ne
{\mathcal S}^{Ward}_{a,ij}(h)
\hbox{ for a minimal row }h.
\end{array}
}
$$

In the first case, the project advances by accepting a positive floor.  In
the second case, it advances by deriving support selection.  In the third
case, it advances by falsifying the current instrument/Ward support
proposal and forcing a new concrete law.

Proof.

These are exactly the three ways the shared table can stop being unknown.
Multiple instrument rows trigger the Paper-14 Feynman branch.  Singleton
instrument rows explained by Ward zeros trigger the Einstein branch.  A row
mismatch is a finite counterexample to the current support proposal.  `square`

### Verdict 10.4

The best next work is therefore not "Feynman versus Einstein."  It is:

$$
\boxed{
\hbox{Feynman builds the rows; Einstein explains the same rows.}
}
$$

That is the first place in V4 where the two styles become complementary
rather than alternative.

## 11. Minimal Two-Row Table Run

Now run the Paper-15 test on the smallest nontrivial fiber:

$$
\boxed{
{\mathcal A}^{NN}_{a,ij}(h)=\{u_0,u_1\},
\qquad
u_0\ne u_1,
\qquad
h\hbox{ has positive actual mass.}
}
$$

This section is intentionally finite.  It does not introduce a new route.
It asks what the shared instrument/Ward table can already decide.

### Definition 11.1: Two-Row Instrument/Ward Mask

For \(r=0,1\), define:

$$
\boxed{
I_r
:=
\mathbf 1_{\{{\mathfrak I}_{a,ij}(h,u_r)\ne\varnothing\}},
\qquad
W_r
:=
\mathbf 1_{\{W_{a,ij}(u_r,h)=0\}}.
}
$$

The minimal table is:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{row} & \hbox{formal} & \hbox{instrument mask} & \hbox{Ward mask}\\
\hline
u_0 & 1 & I_0 & W_0\\
u_1 & 1 & I_1 & W_1
\end{array}
}
$$

The instrument mask is \(I=(I_0,I_1)\).  The Ward mask is \(W=(W_0,W_1)\).

### Definition 11.2: Licensed Instrument Row

A proof of \(I_r=1\) must exhibit a finite operational protocol:

$$
\boxed{
{\mathfrak p}_r
=
(\Omega^{in}_r,\Omega^{out}_r,P_r,R_r)
}
$$

where:

1. \(\Omega^{in}_r\) and \(\Omega^{out}_r\) are finite record sets;
2. \(P_r(\omega^{out}\mid\omega^{in})\) is a stochastic instrument, not a raw
   comparison map;
3. \(R_r:\Omega^{out}_r\to\{(h,u_0),(h,u_1),\bot\}\) is the readout;
4. some positive-probability output record satisfies
   \(R_r(\omega^{out})=(h,u_r)\);
5. the protocol is same-law licensed and does not sample an unrecorded hidden
   route.

This is the Barandes-aligned operational layer: records and instruments are
allowed; hidden trajectory sampling is not.

### Definition 11.3: Licensed Ward Row

A proof of \(W_r=1\) must exhibit a finite defect expression:

$$
\boxed{
W_{a,ij}(u_r,h)
=
{\mathcal W}_{a,ij}(C^{bdry}_a,h,u_r)
}
$$

such that:

1. \({\mathcal W}_{a,ij}\) is built from finite actual records;
2. \({\mathcal W}_{a,ij}\) is invariant under allowed relabellings of those
   records;
3. \({\mathcal W}_{a,ij}=0\) is a constraint, conservation, or Ward identity,
   not a post hoc selector;
4. \({\mathcal W}_{a,ij}\) is evaluated on the same finite boundary/hyp data
   used by the instrument table.

### Theorem 11.4: Exhaustive Two-Row Decision Table

For the minimal two-row fiber, the shared instrument/Ward audit has exactly
the following outcomes:

$$
\boxed{
\begin{array}{c|c|c}
I & W & \hbox{decision}\\
\hline
00 & 00 & \hbox{empty support; impossible for positive-mass }h\\
00 & 10,01,11 & \hbox{instrument catalogue too small or Ward overadmits}\\
10 & 10 & \hbox{Einstein singleton }u_0\\
01 & 01 & \hbox{Einstein singleton }u_1\\
11 & 11 & \hbox{Feynman two-row floor}\\
10 & 00,01,11 & \hbox{instrument/Ward mismatch}\\
01 & 00,10,11 & \hbox{instrument/Ward mismatch}\\
11 & 00,10,01 & \hbox{Ward overkills an instrument-realized row}
\end{array}
}
$$

Here \(10\) means \(u_0\) passes and \(u_1\) fails; \(01\) means \(u_1\)
passes and \(u_0\) fails; \(11\) means both pass.

Proof.

There are four possible instrument masks and four possible Ward masks.  If
\(I=W\), then the common mask is the proposed support set.  The common mask
\(11\) gives two supported rows and hence the Paper-14 floor.  The common
masks \(10\) and \(01\) give singleton support and hence support selection,
with the Ward zero explaining the exclusion.  The common mask \(00\) cannot
represent a positive-mass hyp fiber.  If \(I\ne W\), operational
realizability and invariant Ward admissibility disagree row by row, so the
proposed instrument/Ward bridge is not a theorem for that fiber.  `square`

### Proposition 11.5: What The Current Corpus Actually Fills

For the two-row fiber, the current corpus fills the formal column but not the
two decisive masks:

$$
\boxed{
\begin{array}{c|c|c|c}
\hbox{row} & \hbox{formal} & I_r & W_r\\
\hline
u_0 & 1 & ? & ?\\
u_1 & 1 & ? & ?
\end{array}
}
$$

Consequently:

$$
\boxed{
\mathrm{P15\text{-}IW\text{-}TABLE\text{-}REALIZATION}
\hbox{ is not proved by the current corpus.}
}
$$

This is not a failure of the mask audit.  It is exactly what the audit was
meant to reveal: the missing data are not more route names; they are the
four row entries \(I_0,I_1,W_0,W_1\).

Proof.

Paper 14 supplies the formal support hinge and Paper 15 supplies the
instrument/Ward definitions.  Neither paper constructs a finite instrument
protocol for \(u_0\) or \(u_1\), and neither paper writes a finite Ward defect
whose zero set can be evaluated on the two rows.  Therefore every decisive
mask entry remains unknown.  `square`

### Corollary 11.6: Minimal Certificates Needed Next

The two-row problem is settled as soon as one of the following finite
certificates is produced:

$$
\boxed{
\begin{array}{ll}
\mathrm{P15\text{-}TWO\text{-}ROW\text{-}INSTRUMENT\text{-}FLOOR}:&
I=(1,1),\\[1mm]
\mathrm{P15\text{-}SINGLETON\text{-}INSTRUMENT\text{-}WARD}:&
I=W=(1,0)\hbox{ or }I=W=(0,1),\\[1mm]
\mathrm{P15\text{-}INSTRUMENT\text{-}WARD\text{-}MISMATCH}:&
I\ne W.
\end{array}
}
$$

The first certificate proves the Feynman branch.  The second proves the
Einstein branch.  The third falsifies the current support bridge and forces
a different concrete law.

### Verdict 11.7

The finite run does not magically manufacture \(I_0,I_1,W_0,W_1\).  It does
something more disciplined: it proves that there are only four missing bits.

Thus the next real work inside this project is not another conceptual
fork.  It is a row certificate:

$$
\boxed{
\hbox{construct or exclude }
{\mathfrak I}_{a,ij}(h,u_0),
{\mathfrak I}_{a,ij}(h,u_1),
W_{a,ij}(u_0,h),
W_{a,ij}(u_1,h).
}
$$

Once those four entries are known, the branch decision is automatic.

## 12. Row-Certificate Attack

Now actually attack the four bits.

The target is:

$$
\boxed{
I_0,\ I_1,\ W_0,\ W_1.
}
$$

Feynman's side tries to construct \(I_0,I_1\).  Einstein's side tries to
construct \(W_0,W_1\).  The danger is that both sides can cheat if the paper
allows circular row labels.  This section blocks those cheats and isolates
the one noncircular path.

### Attempt 12.1: The Label-Only Instrument

The tempting fake proof of \(I_r=1\) is:

$$
\boxed{
\Omega^{out}_r=\{\omega_r\},
\qquad
P_r(\omega_r\mid\omega^{in})=1,
\qquad
R_r(\omega_r)=(h,u_r).
}
$$

This would appear to realize any chosen row \(u_r\).

### Theorem 12.2: Label-Only Instruments Are Not Certificates

The label-only construction does not prove \(I_r=1\).

Proof.

The output record \(\omega_r\) has no physical content except the desired row
label.  The readout \(R_r(\omega_r)=(h,u_r)\) therefore imports the row
choice instead of measuring it from a finite actual record.  This is exactly
the hidden-route sampler excluded by the Paper-15 alignment discipline and
by the review-note separation between raw comparison maps, operational
instruments, and observables/effects.

Thus:

$$
\boxed{
\hbox{arbitrary row labelling}
\not\Longrightarrow
I_r=1.
}
$$

`square`

### Attempt 12.3: The Noncircular Instrument Certificate

A valid proof of \(I_r=1\) must instead exhibit a row-sensitive finite
record:

$$
\boxed{
E^{row}_{a,ij}
}
$$

and a finite readout map:

$$
\boxed{
\rho^{row}_{a,ij}:
\mathrm{Range}(E^{row}_{a,ij})\to
\{u_0,u_1,\bot\}
}
$$

such that, under the same actual law conditioned on \(h\),

$$
\boxed{
\mathbb P^{act}_a
\left(
\rho^{row}_{a,ij}(E^{row}_{a,ij})=u_r
\mid h
\right)>0.
}
$$

This gives a noncircular instrument certificate because the row is read from
a finite actual record, not inserted into the readout label.

### Proposition 12.4: Feynman Pass Result

The current corpus does not construct \(E^{row}_{a,ij}\).  Therefore it does
not prove \(I_0=1\), \(I_1=1\), \(I_0=0\), or \(I_1=0\).

However, the Feynman pass has made a real reduction:

$$
\boxed{
I_r=1
\Longleftrightarrow
\hbox{there is a noncircular finite row readout with positive mass at }u_r.
}
$$

within the instrument route.

Proof.

The forward implication is the definition of a licensed instrument row after
excluding label-only instruments.  The reverse implication is obtained by
using the finite record \(E^{row}_{a,ij}\) as the output record and
\(\rho^{row}_{a,ij}\) as the readout.  `square`

### Attempt 12.5: The Hyp-Only Ward Defect

The tempting cheap Einstein proof is to choose a Ward defect that only sees
the hyp fiber:

$$
\boxed{
W_{a,ij}(u,h)=\widehat W_{a,ij}(h).
}
$$

This is invariant and finite, but it has no row sensitivity.

### Theorem 12.6: Hyp-Only Ward Cannot Select A Singleton Row

If \(W_{a,ij}(u,h)=\widehat W_{a,ij}(h)\), then

$$
\boxed{
W_0=W_1.
}
$$

Consequently the Ward mask is either \(00\) or \(11\).  It cannot be \(10\)
or \(01\), so it cannot prove Einstein singleton support on the two-row
fiber.

Proof.

Both rows have the same \(h\).  A hyp-only defect therefore gives the same
defect value on \(u_0\) and \(u_1\).  Hence the zero indicator is equal on
both rows.  `square`

### Attempt 12.7: The Row-Sensitive Ward Certificate

A valid Einstein proof needs a row-sensitive finite defect:

$$
\boxed{
W_{a,ij}(u,h)
=
{\mathcal W}_{a,ij}
\left(E^{row}_{a,ij},h,u\right)
}
$$

with:

$$
\boxed{
{\mathcal W}_{a,ij}(E,h,u)=0
\quad\Longleftrightarrow\quad
u=\rho^{row}_{a,ij}(E)
}
$$

or, in the rectangle-deterministic version,

$$
\boxed{
{\mathcal W}_{a,ij}(E,h,u)=0
\quad\Longleftrightarrow\quad
u=K^{NN,loop}_{a,ij}(H^{NN,ij}_a).
}
$$

The first version explains support by a finite row record.  The second
explains support by normal-rectangle holonomy.

### Proposition 12.8: Einstein Pass Result

The current corpus does not construct a row-sensitive Ward defect of the
form above.  Therefore it does not prove \(W=10\), \(W=01\), or \(W=11\).

But it does prove the following no-go:

$$
\boxed{
\hbox{any Ward proof of singleton support must use row-sensitive finite data.}
}
$$

Hyp-only, boundary-name-only, or post hoc row-label Ward functions cannot do
the job.

Proof.

The hyp-only case is Theorem 12.6.  A boundary-name-only function has the
same defect on all rows in a fixed boundary/hyp cell unless it contains an
additional row-sensitive record.  A post hoc row-label function is just the
Ward analogue of the label-only instrument and is not a licensed finite
constraint.  `square`

### Theorem 12.9: Common Row-Record Hinge

Assume there exists a finite actual row record \(E^{row}_{a,ij}\) and a
readout \(\rho^{row}_{a,ij}\) such that:

$$
\boxed{
\rho^{row}_{a,ij}(E^{row}_{a,ij})
\in
\{u_0,u_1\}
}
$$

on the tested hyp fiber, and assume the instrument and Ward certificates are
both built from this same record:

$$
\boxed{
I_r=1
\Longleftrightarrow
\mathbb P^{act}_a(\rho^{row}_{a,ij}(E^{row}_{a,ij})=u_r\mid h)>0,
}
$$

$$
\boxed{
W_r=1
\Longleftrightarrow
\exists E\hbox{ in actual support over }h
\hbox{ with }\rho^{row}_{a,ij}(E)=u_r.
}
$$

Then \(I=W\).  Moreover:

1. if both row values occur with positive conditional mass, then
   \(I=W=11\) and the Feynman floor follows;
2. if exactly one row value occurs, then \(I=W=10\) or \(I=W=01\) and
   Einstein support selection follows;
3. if \(\rho^{row}\) factors through \(H^{NN,ij}_a\), the rectangle route
   follows.

Proof.

Both masks are defined from the same finite row record and the same positive
conditional support test.  Hence their zero/nonzero entries agree.  The
three branch conclusions are Theorem 11.4.  `square`

### Verdict 12.10

The row-certificate attack does advance the state of Paper 15:

$$
\boxed{
\begin{array}{ll}
\hbox{proved exclusion:} &
\hbox{label-only instruments do not fill }I_r,\\
\hbox{proved exclusion:} &
\hbox{hyp-only Ward defects cannot select one row},\\
\hbox{new hinge:} &
\hbox{a finite row record }E^{row}_{a,ij}\hbox{ would decide both masks.}
\end{array}
}
$$

So the next theorem is no longer merely
\(\mathrm{P15\text{-}IW\text{-}TABLE\text{-}REALIZATION}\).  It is the more
specific theorem:

$$
\boxed{
\mathrm{P15\text{-}FINITE\text{-}ROW\text{-}RECORD\text{-}HINGE}.
}
$$

That theorem is the current shortest path forward.

## 13. Candidate Row-Record Sieve

We now test the named candidates for \(E^{row}_{a,ij}\).  This is the
Feynman/Einstein split in finite form:

1. Feynman asks whether a candidate record varies across rows in one hyp
   fiber.
2. Einstein asks whether that variation is lawful geometry or illicit row
   bookkeeping.

### Definition 13.1: Row-Sensitive Candidate

Let \(E_a\) be a finite actual record and let

$$
\boxed{
\rho_E:\mathrm{Range}(E_a)\to\{u_0,u_1,\bot\}
}
$$

be a finite readout.  \(E_a\) is row-sensitive on the tested hyp fiber \(h\)
if:

$$
\boxed{
\mathbb P^{act}_a(\rho_E(E_a)=u_0\mid h)>0
\quad\hbox{or}\quad
\mathbb P^{act}_a(\rho_E(E_a)=u_1\mid h)>0.
}
$$

It is two-row-sensitive if both conditional probabilities are positive.
It is singleton-sensitive if exactly one is positive.

It is **support-sourcing** only if \(E_a\) is not merely the target row under
another name.  A support-sourcing row record must be finite, actual,
noncircular, and licensed before the NN row support is known.

### Lemma 13.2: Hyp-Factoring Candidates Cannot Separate Rows

If \(E_a=\Phi(h)\) on the tested fiber, then no readout \(\rho_E(E_a)\) can
distinguish \(u_0\) from \(u_1\) inside that fiber.

Proof.

On the event conditioned by \(h\), \(E_a\) is constant.  Therefore every
function of \(E_a\) is constant.  A constant readout cannot take both row
values, and cannot choose one row for a reason internal to row variation.
`square`

### Candidate 13.3: Normal Rectangle Holonomy \(H^{NN,ij}_a\)

Candidate:

$$
\boxed{
E_a=H^{NN,ij}_a.
}
$$

Einstein's desired certificate is:

$$
\boxed{
\rho_H(H^{NN,ij}_a)=K^{NN,loop}_{a,ij}(H^{NN,ij}_a)
=\chi^{NN}_{a,ij}(C^{GCR,sw}_a).
}
$$

This is the cleanest geometric candidate because it would source the row
from a normal rectangle loop shadow instead of from a row label.

Decision:

$$
\boxed{
\begin{array}{ll}
\hbox{if }\chi^{NN}=K(H^{NN})\hbox{ and one value occurs per }h,&
\hbox{Einstein rectangle route};\\
\hbox{if }\chi^{NN}=K(H^{NN})\hbox{ and two }H^{NN}\hbox{ values occur per }h,&
\hbox{Feynman floor};\\
\hbox{if }H^{NN}\hbox{ factors through }h,&
\hbox{not row-sensitive};\\
\hbox{if same }H^{NN}\hbox{ supports two NN rows},&
\hbox{rectangle determinacy falsified}.
\end{array}
}
$$

Current-corpus result.  Paper 14 defines \(H^{NN,ij}_a\) and proves the
conditional rectangle determinacy consequences, but it does not prove
\(\chi^{NN}=K(H^{NN})\) or compute the actual rectangle support table.

Verdict:

$$
\boxed{
H^{NN,ij}_a
\hbox{ is the best Einstein candidate, but not yet a proved row record.}
}
$$

### Candidate 13.4: GCR Switch Packet \(C^{GCR,sw}_a\)

Candidate:

$$
\boxed{
E_a=C^{GCR,sw}_a.
}
$$

This packet is larger than the rectangle shadow.  It can carry row
information through the coordinate:

$$
\boxed{
\chi^{NN}_{a,ij}(C^{GCR,sw}_a).
}
$$

But there is a trap: if \(C^{GCR,sw}_a\) is used only because it already
contains the NN coordinate, it detects the row but does not source the row
support.

Decision:

$$
\boxed{
\begin{array}{ll}
C^{GCR,sw}_a\hbox{ detects rows} &
\hbox{if }\chi^{NN}_{a,ij}(C^{GCR,sw}_a)\hbox{ is an actual coordinate},\\
C^{GCR,sw}_a\hbox{ sources rows} &
\hbox{only if finite GCR compatibility/readout sufficiency is proved},\\
C^{GCR,sw}_a\hbox{ fails as source} &
\hbox{if it merely packages }\chi^{NN}\hbox{ after the fact}.
\end{array}
}
$$

Current-corpus result.  Paper 14 made finite GCR compatibility precise, but
left it as a primitive or a fork.  Therefore \(C^{GCR,sw}_a\) is currently a
row detector, not a row support source.

Verdict:

$$
\boxed{
C^{GCR,sw}_a
\hbox{ is licensed as a finite packet, but needs GCR compatibility to
become }E^{row}.
}
$$

### Candidate 13.5: ADM Normal-Response Packet \(X^{sw,ADM}_a\)

Candidate:

$$
\boxed{
E_a=X^{sw,ADM}_a.
}
$$

This is the most natural finite-GR candidate before passing to full GCR.
It asks whether ADM normal-response data determine the row.

The decision fork is:

$$
\boxed{
\begin{array}{ll}
\chi^{NN}_{a,ij}=\rho_{ADM}(X^{sw,ADM}_a) &
\hbox{ADM row record found},\\
X^{sw,ADM}_a(q_0)=X^{sw,ADM}_a(q_1),\
\chi^{NN}(q_0)\ne\chi^{NN}(q_1) &
\hbox{ADM packet not sufficient},\\
X^{sw,ADM}_a=\Phi(h) &
\hbox{not row-sensitive inside }h.
\end{array}
}
$$

Current-corpus result.  Paper 14 repeatedly reduces ADM routes to finite
readout sufficiency or two-row falsifiers.  It does not prove ADM
sufficiency for the NN row.

Verdict:

$$
\boxed{
X^{sw,ADM}_a
\hbox{ is a serious finite-GR candidate, but currently open.}
}
$$

### Candidate 13.6: Switch Readout Signature \(Z^{sw}_a\)

Candidate:

$$
\boxed{
E_a=Z^{sw}_a.
}
$$

This candidate is operationally tempting because it is a tested physical
readout signature.  But it is close to the measured effect itself.

Decision:

$$
\boxed{
\begin{array}{ll}
Z^{sw}_a\hbox{ may certify a Feynman witness} &
\hbox{if two same-}h\hbox{ rows have different }Z^{sw},\\
Z^{sw}_a\hbox{ may not certify Einstein support} &
\hbox{unless a prior finite law makes }Z^{sw}\hbox{ admissible},\\
Z^{sw}_a\hbox{ is circular as source} &
\hbox{if it is just the target switch effect under another name}.
\end{array}
}
$$

Current-corpus result.  \(Z^{sw}_a\) is a good falsifier/readout, not a
noncircular support source by itself.

Verdict:

$$
\boxed{
Z^{sw}_a
\hbox{ is Feynman-useful as a visibility witness, but not Einstein-sufficient.}
}
$$

### Candidate 13.7: Residual Row Defect \(\eta^{NN}_{a,ij}\)

Candidate:

$$
\boxed{
E_a=\eta^{NN}_{a,ij}
}
$$

from the decomposition:

$$
\boxed{
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
=
K^{NN,loop}_{a,ij}(H^{NN,ij}_a)
+
\eta^{NN}_{a,ij}.
}
$$

This is the most surgical candidate.  It asks whether the failure of
rectangle determinacy is itself a finite actual record.

Decision:

$$
\boxed{
\begin{array}{ll}
\eta^{NN}=0\hbox{ or }\eta^{NN}=\Phi(H^{NN}) &
\hbox{Einstein rectangle repair},\\
\eta^{NN}\hbox{ has two actual values in one }h\hbox{ fiber} &
\hbox{Feynman floor},\\
\eta^{NN}\hbox{ is only a formal residual} &
\hbox{not licensed}.
\end{array}
}
$$

Current-corpus result.  Paper 14 names this residual possibility but does
not prove that \(\eta^{NN}_{a,ij}\) is a finite actual record.

Verdict:

$$
\boxed{
\eta^{NN}_{a,ij}
\hbox{ is the sharpest Feynman candidate, but still unsourced as actual.}
}
$$

### Candidate 13.8: Finite Instrument Outcome Records

Candidate:

$$
\boxed{
E_a=O^{inst}_{a,ij}
}
$$

where \(O^{inst}_{a,ij}\) is a genuine output record of a licensed finite
instrument.

This is the most operational candidate.  It avoids the GCR/ADM completeness
problem by directly building a finite procedure whose outputs are records.

Decision:

$$
\boxed{
\begin{array}{ll}
\rho_O(O^{inst})=u_0,u_1\hbox{ both occur over }h &
\hbox{Feynman floor},\\
\rho_O(O^{inst})\hbox{ has one value over }h\hbox{ and Ward explains it} &
\hbox{Einstein support selection},\\
O^{inst}\hbox{ merely names the requested row} &
\hbox{label-only exclusion}.
\end{array}
}
$$

Current-corpus result.  Paper 15 rules out label-only instruments but does
not yet construct a genuine outcome record.

Verdict:

$$
\boxed{
O^{inst}_{a,ij}
\hbox{ is the best Feynman construction target.}
}
$$

### Theorem 13.9: Sieve Verdict

The candidate sieve reduces the missing object to the following priority
list:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{rank} & \hbox{candidate} & \hbox{status}\\
\hline
1 & O^{inst}_{a,ij} & \hbox{best Feynman construction target}\\
2 & H^{NN,ij}_a & \hbox{best Einstein geometry target}\\
3 & \eta^{NN}_{a,ij} & \hbox{sharpest residual/floor target}\\
4 & X^{sw,ADM}_a & \hbox{finite-GR candidate, open}\\
5 & C^{GCR,sw}_a & \hbox{detector unless GCR compatibility is proved}\\
6 & Z^{sw}_a & \hbox{visibility witness, not support source}
\end{array}
}
$$

Thus:

$$
\boxed{
\hbox{to find }E^{row}_{a,ij},
\hbox{ first try }O^{inst}_{a,ij},
\hbox{ then }H^{NN,ij}_a,
\hbox{ then }\eta^{NN}_{a,ij}.
}
$$

Proof.

The ranking follows from noncircularity.  A genuine instrument outcome can
directly fill \(I_0,I_1\).  A rectangle holonomy can give the clean Einstein
route without row labelling.  A residual defect can expose exactly the
missing row variation.  ADM and GCR records are important but need
additional sufficiency/compatibility theorems before they source support.
The switch readout is useful for visibility, but too close to the target
effect to be a support source by itself.  `square`

### Corollary 13.10: Immediate Next Theorems

The next work should not open six new papers.  It should try these three
finite certificates in order:

$$
\boxed{
\begin{array}{ll}
\mathrm{P15\text{-}INSTRUMENT\text{-}OUTCOME\text{-}ROW\text{-}CERT}:&
O^{inst}_{a,ij}\hbox{ exists and reads }u_0,u_1,\\[1mm]
\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}CERT}:&
\chi^{NN}_{a,ij}=K^{NN,loop}_{a,ij}(H^{NN,ij}_a),\\[1mm]
\mathrm{P15\text{-}RESIDUAL\text{-}ROW\text{-}CERT}:&
\eta^{NN}_{a,ij}\hbox{ is a finite actual row record}.
\end{array}
}
$$

Each certificate has a fast falsifier:

$$
\boxed{
\begin{array}{ll}
O^{inst}\hbox{ falsifier}:&
\hbox{all proposed instruments are label-only or row-blind},\\
H^{NN}\hbox{ falsifier}:&
\hbox{same }H^{NN}\hbox{ supports two NN rows},\\
\eta^{NN}\hbox{ falsifier}:&
\eta^{NN}\hbox{ is not finite actual data or is }h\hbox{-measurable}.
\end{array}
}
$$

This is the concrete way forward.

## 14. Instrument Outcome Row Certificate Attempt

Now attack the first certificate:

$$
\boxed{
\mathrm{P15\text{-}INSTRUMENT\text{-}OUTCOME\text{-}ROW\text{-}CERT}.
}
$$

The question is whether \(O^{inst}_{a,ij}\) is a genuinely new row record, or
whether it merely repackages the already listed candidates.

### Definition 14.1: Current-Corpus Outcome Library

For the tested two-row hyp fiber, define the current licensed output library:

$$
\boxed{
{\mathcal L}^{out}_{a,ij}
:=
\sigma
\left(
h,\,
H^{NN,ij}_a,\,
X^{sw,ADM}_a,\,
C^{GCR,sw}_a,\,
Z^{sw}_a,\,
\eta^{NN}_{a,ij}\hbox{ if actual}
\right).
}
$$

This is not a claim that every listed entry is already support-sourcing.
It is only the current finite menu of records that an operational outcome
could noncircularly expose without inventing a new primitive record.

A current-corpus instrument outcome is any finite record

$$
\boxed{
O^{inst}_{a,ij}=F({\mathcal L}^{out}_{a,ij})
}
$$

for a finite readout function \(F\), together with a stochastic instrument
that produces that record without hidden route sampling.

### Definition 14.2: New Operational Row Record

A genuinely new instrument outcome is a finite record

$$
\boxed{
O^{new}_{a,ij}
}
$$

such that:

1. \(O^{new}_{a,ij}\) is an actual finite operational output;
2. \(O^{new}_{a,ij}\) is not measurable with respect to
   \({\mathcal L}^{out}_{a,ij}\);
3. it has a non-label readout
   \(\rho_{new}(O^{new}_{a,ij})\in\{u_0,u_1,\bot\}\);
4. the output protocol is specified before choosing a desired row.

Only such an \(O^{new}_{a,ij}\) would make the instrument route independent
of the geometric/residual candidates.

### Lemma 14.3: Outcome-Library Reduction

Assume

$$
\boxed{
O^{inst}_{a,ij}=F(E_1,\ldots,E_k)
}
$$

where each \(E_s\) is a finite generator of
\({\mathcal L}^{out}_{a,ij}\).  If \(O^{inst}_{a,ij}\) is row-sensitive in
the tested hyp fiber, then at least one generator \(E_s\) is row-sensitive
in that fiber.

Proof.

If every \(E_s\) is constant on the tested \(h\)-fiber, then the tuple
\((E_1,\ldots,E_k)\) is constant on that fiber, and so every finite function
of that tuple is also constant.  Therefore \(O^{inst}_{a,ij}\) cannot
distinguish \(u_0\) from \(u_1\).  Contrapositively, if the outcome is
row-sensitive, some generator is row-sensitive.  `square`

### Theorem 14.4: Current-Corpus Instrument Outcome Reduction

Within the current corpus, the instrument-outcome certificate has only two
ways to succeed:

$$
\boxed{
\begin{array}{ll}
\hbox{new-output route:} &
O^{new}_{a,ij}\hbox{ is constructed as a genuine operational record},\\
\hbox{reduction route:} &
O^{inst}_{a,ij}\hbox{ reads one of }
H^{NN},X^{ADM},C^{GCR},Z^{sw},\eta^{NN}.
\end{array}
}
$$

If neither occurs, then
\(\mathrm{P15\text{-}INSTRUMENT\text{-}OUTCOME\text{-}ROW\text{-}CERT}\)
is not proved.

Proof.

If the outcome is not new, it is measurable with respect to the current
output library.  Lemma 14.3 says any row sensitivity must already come from
one of the library generators.  If it is new, it must satisfy Definition
14.2.  Label-only outputs are excluded by Theorem 12.2.  These are the only
remaining cases.  `square`

### Corollary 14.5: Instrument Outcome Is Not An Independent Current-Corpus Source

The current corpus does not construct \(O^{new}_{a,ij}\).  Therefore the
instrument outcome route currently reduces to the following candidates:

$$
\boxed{
H^{NN,ij}_a,\quad
X^{sw,ADM}_a,\quad
C^{GCR,sw}_a,\quad
Z^{sw}_a,\quad
\eta^{NN}_{a,ij}.
}
$$

Among these, Paper 15 has already ranked:

$$
\boxed{
H^{NN,ij}_a
\quad\hbox{and}\quad
\eta^{NN}_{a,ij}
}
$$

as the next two noncircular targets, with \(X^{sw,ADM}_a\) and
\(C^{GCR,sw}_a\) needing sufficiency/compatibility theorems and \(Z^{sw}_a\)
serving mainly as a visibility witness.

Thus:

$$
\boxed{
\mathrm{P15\text{-}INSTRUMENT\text{-}OUTCOME\text{-}ROW\text{-}CERT}
\hbox{ is reduced, not solved.}
}
$$

### Fast Falsifier 14.6

The independent instrument route is falsified for the current corpus if:

$$
\boxed{
\begin{array}{l}
\hbox{every proposed }O^{inst}\hbox{ is label-only, row-blind, or}\\
\hbox{measurable with respect to }
\sigma(h,H^{NN},X^{ADM},C^{GCR},Z^{sw},\eta^{NN}).
\end{array}
}
$$

The first two cases are invalid or useless.  The third case reduces the
problem to one of the named generator records.

### Verdict 14.7

The first certificate does not unlock the path as an independent theorem in
the current corpus.  It gives a useful reduction:

$$
\boxed{
\hbox{instrument outcome}
\Longrightarrow
\hbox{new operational row record}
\quad\hbox{or}\quad
H^{NN}/\eta^{NN}/ADM/GCR/Z^{sw}.
}
$$

Therefore the next attack should move to the best noncircular remaining
candidate:

$$
\boxed{
\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}CERT}.
}
$$

If the rectangle certificate fails, the residual certificate
\(\mathrm{P15\text{-}RESIDUAL\text{-}ROW\text{-}CERT}\) becomes the next
target.

## 15. Rectangle Row Certificate Attempt

Now attack the second certificate:

$$
\boxed{
\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}CERT}.
}
$$

The question is whether the normal rectangle loop shadow
\(H^{NN,ij}_a\) is itself the row record.

### Definition 15.1: Rectangle Fiber Support

For a rectangle value \(\ell\), define the actual NN support over that
rectangle fiber:

$$
\boxed{
{\mathcal S}^{NN\mid H}_{a,ij}(\ell)
:=
\left\{
u:
\mathbb P^{act}_a
\left(
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)=u,\,
H^{NN,ij}_a=\ell
\right)>0
\right\}.
}
$$

The rectangle row certificate is:

$$
\boxed{
\left|{\mathcal S}^{NN\mid H}_{a,ij}(\ell)\right|
\le 1
\quad
\hbox{for every positive-mass }\ell.
}
$$

Equivalently, there is a finite map

$$
\boxed{
K^{NN,loop}_{a,ij}
}
$$

such that, on actual support,

$$
\boxed{
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
=
K^{NN,loop}_{a,ij}(H^{NN,ij}_a).
}
$$

### Theorem 15.2: Rectangle Certificate Gives The Row Record

If the rectangle row certificate holds, then

$$
\boxed{
E^{row}_{a,ij}=H^{NN,ij}_a
}
$$

is a licensed finite row record.  Moreover:

1. if a positive-mass hyp fiber \(h\) contains two rectangle values
   \(\ell_0,\ell_1\) whose reconstructed NN values differ, then the Feynman
   floor route opens;
2. if every positive-mass hyp fiber contains exactly one reconstructed NN
   value, then the Einstein support-selection route opens;
3. if the reconstruction is global over actual support, the GR-facing
   rectangle determinacy theorem holds.

Proof.

The certificate says precisely that the NN row is a finite function of
\(H^{NN,ij}_a\) on actual support.  Thus \(H^{NN,ij}_a\) can be used as
\(E^{row}_{a,ij}\) with readout \(K^{NN,loop}_{a,ij}\).  Variation of this
readout inside a hyp fiber gives two supported NN rows and hence the
Feynman branch.  Singleton readout inside every hyp fiber gives Einstein
support selection.  Global reconstruction is rectangle determinacy.
`square`

### Theorem 15.3: Same-Rectangle Two-Row Witness Falsifies Rectangle Certification

If there exist \(q_0,q_1\) in actual support such that

$$
\boxed{
H^{NN,ij}_a(q_0)=H^{NN,ij}_a(q_1),
\qquad
\chi^{NN}_{a,ij}(C^{GCR,sw}_a(q_0))
\ne
\chi^{NN}_{a,ij}(C^{GCR,sw}_a(q_1)),
}
$$

then \(\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}CERT}\) is false.

If, in addition, \(q_0,q_1\) lie in the same positive-mass hyp fiber \(h\),
then the Feynman floor route opens.

Proof.

The displayed pair has the same rectangle value and different NN values.
No function of \(H^{NN,ij}_a\) can take two different values on the same
\(H^{NN,ij}_a\)-fiber.  Thus rectangle reconstruction is impossible.  If the
pair also lies in one hyp fiber, Paper 14's two-row support theorem gives
the floor.  `square`

### Proposition 15.4: Current-Corpus Rectangle Status

The current corpus proves neither side of the rectangle fork.

It proves:

$$
\boxed{
H^{NN,ij}_a
\hbox{ is a finite normal-rectangle loop shadow.}
}
$$

It also proves the conditional consequences:

$$
\boxed{
\chi^{NN}=K(H^{NN})
\Longrightarrow
\hbox{rectangle determinacy/support selection consequences.}
}
$$

But it does not prove:

$$
\boxed{
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
=
K^{NN,loop}_{a,ij}(H^{NN,ij}_a),
}
$$

and it does not exhibit an actual same-rectangle witness:

$$
\boxed{
H^{NN,ij}_a(q_0)=H^{NN,ij}_a(q_1),
\qquad
\chi^{NN}(q_0)\ne\chi^{NN}(q_1).
}
$$

Therefore:

$$
\boxed{
\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}CERT}
\hbox{ is open in the current corpus.}
}
$$

Proof.

This is exactly the status imported from Paper 14 and restated in Sections
4 and 13 of Paper 15: the rectangle shadow is defined, and the conditional
determinacy theorem is proved, but the actual same-law rectangle support
table is not filled.  `square`

### Corollary 15.5: Rectangle Attack Surface

The rectangle route is now reduced to exactly two finite tests:

$$
\boxed{
\begin{array}{ll}
\hbox{Einstein test:}&
\hbox{prove every positive-mass }H^{NN}\hbox{-fiber is NN-single-valued},\\[1mm]
\hbox{Feynman test:}&
\hbox{find a positive-mass same-}H^{NN}\hbox{, different-NN pair}.
\end{array}
}
$$

There is no third rectangle-specific issue.  Missing actual masses remain
the only obstruction.

### Verdict 15.6

The rectangle certificate is the cleanest geometric route, but Paper 15
cannot close it from the current corpus.  It leaves a crisp next theorem:

$$
\boxed{
\mathrm{P15\text{-}RECTANGLE\text{-}FIBER\text{-}SIDE\text{-}DECISION}.
}
$$

This theorem must prove one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{P15\text{-}RECTANGLE\text{-}SINGLETON}:&
\left|{\mathcal S}^{NN\mid H}_{a,ij}(\ell)\right|\le1
\hbox{ for all positive-mass }\ell,\\[1mm]
\mathrm{P15\text{-}RECTANGLE\text{-}TWO\text{-}ROW}:&
\exists \ell,\ u_0\ne u_1
\hbox{ both actual over }H^{NN}=\ell.
\end{array}
}
$$

If neither side can be sourced, then the next independent target is the
residual row certificate:

$$
\boxed{
\mathrm{P15\text{-}RESIDUAL\text{-}ROW\text{-}CERT}.
}
$$

## 16. Rectangle Fiber Decision Audit

The previous section named the two rectangle sides.  This section runs the
finite audit that would decide them.

### Definition 16.1: Formal And Actual Rectangle Fiber Tables

For a rectangle value \(\ell\), define the formal rectangle fiber:

$$
\boxed{
{\mathcal A}^{NN\mid H}_{a,ij}(\ell)
:=
\left\{
u:
\exists q\hbox{ formally admissible with }
H^{NN,ij}_a(q)=\ell,\ 
\chi^{NN}_{a,ij}(C^{GCR,sw}_a(q))=u
\right\}.
}
$$

The actual rectangle mass vector is:

$$
\boxed{
m^{H}_{\ell,u}
:=
\mathbb P^{act}_a
\left(
H^{NN,ij}_a=\ell,\,
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)=u
\right).
}
$$

Thus:

$$
\boxed{
{\mathcal S}^{NN\mid H}_{a,ij}(\ell)
=
\{u:m^{H}_{\ell,u}>0\}.
}
$$

The rectangle problem is not the formal fiber.  It is the actual mass vector
\(m^{H}_{\ell,u}\).

### Lemma 16.2: Formal Rectangle Fibers Do Not Decide Actual Rectangle Fibers

If \(\left|{\mathcal A}^{NN\mid H}_{a,ij}(\ell)\right|\ge2\), this does not
by itself imply a same-rectangle two-row witness.  If
\(\left|{\mathcal A}^{NN\mid H}_{a,ij}(\ell)\right|=1\), then rectangle
singleton holds on that \(\ell\)-fiber formally.

Proof.

A formal two-row fiber only says two rows are admissible.  It does not say
both have positive actual mass.  A formal singleton fiber has only one
admissible row, so actual support, being a subset of admissible support, is
singleton or empty.  `square`

### Theorem 16.3: Rectangle Fiber Side Decision

For every positive-mass rectangle value \(\ell\), exactly one of the
following holds:

$$
\boxed{
\begin{array}{ll}
\hbox{singleton side:}&
\left|{\mathcal S}^{NN\mid H}_{a,ij}(\ell)\right|\le1,\\[1mm]
\hbox{two-row side:}&
\exists u_0\ne u_1,\ 
m^{H}_{\ell,u_0}>0,\ m^{H}_{\ell,u_1}>0.
\end{array}
}
$$

If the singleton side holds for all positive-mass \(\ell\), then rectangle
row certification holds.  If the two-row side holds for some \(\ell\), then
rectangle row certification is false.  If the two-row side also occurs
inside one positive-mass hyp fiber, then the Feynman floor route opens.

Proof.

The finite set \({\mathcal S}^{NN\mid H}_{a,ij}(\ell)\) has either at most
one element or at least two elements.  The latter is exactly the displayed
two-positive-mass condition.  The consequences are Theorems 15.2 and 15.3.
`square`

### Proposition 16.4: Current-Corpus Rectangle Audit Result

The current corpus does not provide the mass vector

$$
\boxed{
\left(m^{H}_{\ell,u}\right)_{\ell,u}.
}
$$

Therefore it does not decide the rectangle fiber side.

What it currently provides is only the decision template:

$$
\boxed{
\begin{array}{c|c|c}
\hbox{data supplied} & \hbox{rectangle conclusion} & \hbox{status}\\
\hline
\left|{\mathcal A}^{NN\mid H}(\ell)\right|=1\hbox{ for all }\ell &
\hbox{formal rectangle singleton} &
\hbox{not shown}\\
m^{H}_{\ell,u_0},m^{H}_{\ell,u_1}>0 &
\hbox{same-rectangle two-row witness} &
\hbox{not shown}\\
\left|{\mathcal S}^{NN\mid H}(\ell)\right|\le1\hbox{ for all }\ell &
\hbox{rectangle row certificate} &
\hbox{not shown}
\end{array}
}
$$

Thus:

$$
\boxed{
\mathrm{P15\text{-}RECTANGLE\text{-}FIBER\text{-}SIDE\text{-}DECISION}
\hbox{ remains open because }m^{H}_{\ell,u}\hbox{ is not sourced.}
}
$$

### Corollary 16.5: Rectangle Audit Handoff

If no actual rectangle mass vector can be sourced, the next noncircular
question is not another rectangle reformulation.  It is:

$$
\boxed{
\hbox{is the failure of rectangle determination itself a finite actual record?}
}
$$

That is the residual row certification problem.

### Attempt 16.6: Minimal Rectangle Mass Vector

Fix the smallest nontrivial rectangle fiber:

$$
\boxed{
{\mathcal A}^{NN\mid H}_{a,ij}(\ell)=\{u_0,u_1\},
\qquad
u_0\ne u_1.
}
$$

The target table is:

$$
\boxed{
\begin{array}{c|cc}
\hbox{rectangle value} & u_0 & u_1\\
\hline
\ell & m^{H}_{\ell,u_0} & m^{H}_{\ell,u_1}
\end{array}
}
$$

This is the concrete Feynman table.  It is also the concrete Einstein table:
Einstein needs a licensed reason why one entry must vanish, unless both
entries vanish because \(\ell\) has zero actual mass.

### Lemma 16.7: What Can Fill The Minimal Rectangle Mass Vector

For a positive-mass rectangle value \(\ell\), the two-row vector

$$
\boxed{
\left(m^{H}_{\ell,u_0},m^{H}_{\ell,u_1}\right)
}
$$

can be sourced only by one of the following finite inputs:

$$
\boxed{
\begin{array}{ll}
\hbox{relative positivity:}&
m^{H}_{\ell,u_r}>0\hbox{ for every admissible row }u_r,\\
\hbox{support exclusion:}&
m^{H}_{\ell,u_r}=0\hbox{ because a licensed finite record forbids }u_r,\\
\hbox{direct instrument mass:}&
\hbox{a licensed instrument estimates or realizes }(\ell,u_r),\\
\hbox{Ward/constraint mass:}&
\hbox{a finite Ward/constraint zero set equals the actual support}.
\end{array}
}
$$

Formal admissibility alone does not fill the vector.

Proof.

The entries are actual probabilities.  A proof that an entry is positive is
a positivity theorem, an operational realization theorem, or a support law
identifying positivity with a finite zero condition.  A proof that an entry
vanishes is a support-exclusion theorem.  Formal admissibility supplies only
membership in \({\mathcal A}^{NN\mid H}\), not positive actual mass.  `square`

### Theorem 16.8: Minimal Rectangle Vector Decision

For the minimal two-row rectangle fiber:

1. if

$$
\boxed{
m^{H}_{\ell,u_0}>0,
\qquad
m^{H}_{\ell,u_1}>0,
}
$$

then the same-rectangle two-row side holds and rectangle row certification
is false;

2. if exactly one entry is positive, then the rectangle fiber is singleton
provided the zero entry has a licensed support-exclusion reason;

3. if neither positivity nor exclusion is sourced, then the minimal
rectangle vector is undecided.

Proof.

These are the three possible actual-support statuses for a two-row
positive-mass rectangle fiber.  The first gives two actual NN values over
the same \(H^{NN}\).  The second gives singleton rectangle support, but only
with a licensed reason for the zero if it is to be an Einstein certificate.
The third is exactly absence of actual-law information.  `square`

### Proposition 16.9: Current-Corpus Minimal Vector Result

The current corpus does not source any of:

$$
\boxed{
m^{H}_{\ell,u_0}>0,\qquad
m^{H}_{\ell,u_1}>0,\qquad
m^{H}_{\ell,u_0}=0,\qquad
m^{H}_{\ell,u_1}=0.
}
$$

It supplies the formal row labels and the rectangle coordinate, but not the
actual rectangle-row mass vector.  Therefore:

$$
\boxed{
\mathrm{P15\text{-}MINIMAL\text{-}RECTANGLE\text{-}MASS\text{-}VECTOR}
\hbox{ is not proved by the current corpus.}
}
$$

Proof.

Sections 15 and 16 prove the rectangle consequences conditional on the mass
vector, but neither Paper 14 nor Paper 15 supplies relative positivity,
support exclusion, direct instrument mass, or Ward/constraint support
identification for the two rectangle rows.  `square`

### Verdict 16.10

The minimal rectangle mass-vector attempt is completed, and its result is
negative as a current-corpus derivation:

$$
\boxed{
\hbox{the missing primitive is actual rectangle-row positivity or exclusion.}
}
$$

Thus the next theorem cannot be another rectangle table rewrite.  It must be
one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}POSITIVITY}:&
m^{H}_{\ell,u_r}>0\hbox{ for the tested row},\\[1mm]
\mathrm{P15\text{-}RECTANGLE\text{-}ROW\text{-}EXCLUSION}:&
m^{H}_{\ell,u_r}=0\hbox{ for a licensed finite reason},\\[1mm]
\mathrm{P15\text{-}RESIDUAL\text{-}ACTUAL\text{-}RECORD}:&
\eta^{NN,K}_{a,ij}\hbox{ is finite actual data}.
\end{array}
}
$$

## 17. Residual Row Certification Audit

The residual route begins only after the rectangle route fails to close.
It asks whether the leftover from the best rectangle predictor is itself a
finite actual record.

### Definition 17.1: Residual Defect Relative To A Rectangle Predictor

Let

$$
\boxed{
K:\mathrm{Range}(H^{NN,ij}_a)\to{\mathsf Val}^{NN}_{a,ij}
}
$$

be any finite rectangle predictor.  Define the residual defect by:

$$
\boxed{
\eta^{NN,K}_{a,ij}
:=
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
-
K(H^{NN,ij}_a),
}
$$

when the NN value space has a signed affine difference.  If it does not,
replace the difference by the pair-valued defect:

$$
\boxed{
\eta^{NN,K}_{a,ij}
:=
\left(
K(H^{NN,ij}_a),
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
\right).
}
$$

The residual is a row certificate only if
\(\eta^{NN,K}_{a,ij}\) is a finite actual record before the desired row is
chosen.  A residual computed by first reading \(\chi^{NN}\) and then calling
the difference "data" is circular unless \(\chi^{NN}\) itself is already a
licensed finite readout.

### Definition 17.2: Residual Outcomes

The residual audit has four outcomes:

$$
\boxed{
\begin{array}{ll}
\hbox{zero residual:}&
\eta^{NN,K}_{a,ij}=0\hbox{ on actual support},\\
\hbox{rectangle-repair residual:}&
\eta^{NN,K}_{a,ij}=\Phi(H^{NN,ij}_a)\hbox{ on actual support},\\
\hbox{floor residual:}&
\eta^{NN,K}_{a,ij}\hbox{ has two actual values in one }h\hbox{-fiber},\\
\hbox{unsourced residual:}&
\eta^{NN,K}_{a,ij}\hbox{ is not finite actual data}.
\end{array}
}
$$

### Theorem 17.3: Residual Audit Consequences

For any finite rectangle predictor \(K\):

1. zero residual gives rectangle determinacy;
2. rectangle-repair residual gives an enlarged rectangle predictor
   \(K+\Phi\) in the signed case, or a finite repaired map from
   \(H^{NN,ij}_a\) in the pair-valued case;
3. floor residual gives a Feynman row record if the two residual values have
   positive mass in one hyp fiber;
4. unsourced residual does not prove anything about actual support.

Proof.

If the residual is zero, \(\chi^{NN}=K(H^{NN})\).  If it is a function of
\(H^{NN}\), then \(\chi^{NN}\) is still a function of \(H^{NN}\), after
absorbing the residual into the predictor.  If the residual is finite actual
data with two values in one hyp fiber, it is a row-sensitive record and
triggers the Paper-14 two-row/floor mechanism.  If it is not actual finite
data, it is only bookkeeping.  `square`

### Proposition 17.4: Current-Corpus Residual Status

The current corpus names the residual possibility:

$$
\boxed{
\chi^{NN}_{a,ij}(C^{GCR,sw}_a)
=
K^{NN,loop}_{a,ij}(H^{NN,ij}_a)
+
\eta^{NN}_{a,ij}.
}
$$

But it does not prove that \(\eta^{NN}_{a,ij}\) is a finite actual record.
It also does not prove that \(\eta^{NN}_{a,ij}=0\), that it is
\(H^{NN}\)-measurable, or that it has two actual values in one hyp fiber.

Thus:

$$
\boxed{
\mathrm{P15\text{-}RESIDUAL\text{-}ROW\text{-}CERT}
\hbox{ is open in the current corpus.}
}
$$

### Corollary 17.5: Final Residual Target

The residual route has exactly one useful next theorem:

$$
\boxed{
\mathrm{P15\text{-}RESIDUAL\text{-}ACTUAL\text{-}RECORD\text{-}DECISION}.
}
$$

It must prove one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{P15\text{-}RESIDUAL\text{-}ZERO}:&
\eta^{NN,K}_{a,ij}=0,\\[1mm]
\mathrm{P15\text{-}RESIDUAL\text{-}REPAIR}:&
\eta^{NN,K}_{a,ij}=\Phi(H^{NN,ij}_a),\\[1mm]
\mathrm{P15\text{-}RESIDUAL\text{-}FLOOR}:&
\eta^{NN,K}_{a,ij}\hbox{ has two actual values in one }h\hbox{-fiber},\\[1mm]
\mathrm{P15\text{-}RESIDUAL\text{-}UNSOURCED}:&
\eta^{NN,K}_{a,ij}\hbox{ is not finite actual data}.
\end{array}
}
$$

This is the last noncircular route left by Paper 15.

## 18. Final Verdict

Paper 15 does not prove the final support side.  It does something smaller
and more useful: it prevents the next work from branching endlessly.

The route ranking after the five tests is:

$$
\boxed{
\begin{array}{cl}
1. & \mathrm{P15\text{-}10\text{-}INSTRUMENT\text{-}SUPPORT},\\
2. & \mathrm{P15\text{-}08\text{-}WARD\text{-}CONSTRAINED},\\
3. & \mathrm{P15\text{-}05\text{-}FINITE\text{-}HOLONOMY\text{-}RECTANGLE},\\
4. & \mathrm{P15\text{-}03\text{-}MINIMUM\text{-}RESIDUAL},\\
5. & \mathrm{P15\text{-}01\text{-}UNIFORM\text{-}ADMISSIBLE\text{-}ROW}.
\end{array}
}
$$

The first genuinely new theorem should now be the finite row-record hinge:

$$
\boxed{
\mathrm{P15\text{-}FINITE\text{-}ROW\text{-}RECORD\text{-}HINGE}.
}
$$

Its table-level projection remains:

$$
\boxed{
\mathrm{P15\text{-}IW\text{-}TABLE\text{-}REALIZATION}
\quad\hbox{with}\quad
\mathrm{P15\text{-}INSTRUMENT\text{-}SUPPORT\text{-}THEOREM}
\quad\hbox{and}\quad
\mathrm{P15\text{-}WARD\text{-}SUPPORT\text{-}THEOREM}.
}
$$

The minimal run sharpens this further.  In the first nontrivial fiber, only
four bits remain:

$$
\boxed{
I_0,\ I_1,\ W_0,\ W_1.
}
$$

The row-certificate attack proves that two cheap escapes are invalid:
label-only instruments do not count, and hyp-only Ward defects cannot select
one row.  Therefore the missing object is a real row-sensitive finite record
\(E^{row}_{a,ij}\).  If it gives \(I=W=11\), the Feynman floor route opens.
If it gives \(I=W=10\) or \(I=W=01\), the Einstein support-selection route
opens.  If it cannot be built, then the current instrument/Ward bridge has
no finite support source.

The candidate sieve first ranked the search:

$$
\boxed{
O^{inst}_{a,ij}
\quad\hbox{then}\quad
H^{NN,ij}_a
\quad\hbox{then}\quad
\eta^{NN}_{a,ij}.
}
$$

The instrument-outcome attack then reduced the first item: unless a genuinely
new operational output record \(O^{new}_{a,ij}\) is constructed,
\(O^{inst}_{a,ij}\) is only a wrapper around the remaining candidates.  Thus
the next independent target is:

$$
\boxed{
H^{NN,ij}_a
\quad\hbox{then}\quad
\eta^{NN}_{a,ij}.
}
$$

The rectangle attack then reduced \(H^{NN,ij}_a\) to a two-sided finite
decision:

$$
\boxed{
\hbox{rectangle singleton}
\quad\hbox{or}\quad
\hbox{same-rectangle two-row witness}.
}
$$

The current corpus proves neither side.

The rectangle-fiber audit identifies why:

$$
\boxed{
\hbox{the actual mass vector }m^{H}_{\ell,u}\hbox{ is not sourced.}
}
$$

The minimal rectangle mass-vector attempt sharpens that further:

$$
\boxed{
\hbox{neither positivity nor exclusion is sourced for }
m^{H}_{\ell,u_0},m^{H}_{\ell,u_1}.
}
$$

The residual audit then reduces the last route to:

$$
\boxed{
\hbox{decide whether }\eta^{NN,K}_{a,ij}
\hbox{ is zero, }H^{NN}\hbox{-measurable, two-valued actual, or unsourced.}
}
$$

Thus Paper 15's final state is:

$$
\boxed{
\hbox{stop choosing abstract laws;}
\quad
\hbox{prove rectangle-row positivity/exclusion or decide residual actuality.}
}
$$
