# Relativistic ISP V5 Paper 1: Finite Record Horizons And Black-Hole Ontology

Preprint, not peer reviewed, version 2026-05-29.

Author: Felix Robles Elvira

Status: V5 consequences paper after the V4 GR/QFT/QCD/YM descent stack.

## Abstract

This paper begins the V5 consequences track.  The question is not whether the
V4 descent stack can reproduce the effective GR description of a black hole at
large scales.  The question is what a black hole *is* in the finite-record ISP
ontology.

The central claim is that a black hole should not be introduced as a literal
single point of physical discontinuity.  In classical GR, the event horizon is
not a local discontinuity, and the singularity is better understood as
geodesic incompleteness or curvature blow-up in the continuum effective
description.  In ISP, the primitive objects are finite records and stochastic
hypersurface transports.  Therefore the primitive black-hole object is not a
point \(r=0\).  It is an exterior-accessibility structure: a finite region whose
interior record distinctions fail to propagate back into the exterior
operational record algebra.

The V5 ontology is:

$$
\boxed{
\hbox{black hole}
=
\hbox{finite record horizon plus exterior many-to-one compression.}
}
$$

The GR singularity becomes:

$$
\boxed{
\hbox{singularity}
=
\hbox{failure of smooth GR descent beyond the licensed finite-record regime.}
}
$$

Thus the first ISP answer to the question "is there a single point with a
discontinuity?" is no.  The horizon is not a discontinuity, and the singularity
is not primitive ontology.  Any point singularity belongs to an overextended
continuum reconstruction, not to the finite stochastic process itself.

Searchable paper tag:

`V5P1-FINITE-RECORD-HORIZON-BLACK-HOLE-ONTOLOGY`.

## 0. Purpose

V1 through V4 built the finite stochastic geometry:

$$
\boxed{
\hbox{finite records}
\to
\hbox{exchange defects}
\to
\hbox{effective phase/fields/geometry}
\to
\hbox{GR/QFT/QCD/YM descent.}
}
$$

V5 changes the question.  It asks what the effective physics *means* once the
ontology is finite-record ISP rather than continuum-first geometry.

The first consequence target is the black hole, because black holes are where
GR most visibly asks to be interpreted:

$$
\boxed{
\hbox{event horizon is regular in GR, but singularity signals breakdown.}
}
$$

ISP should not copy the breakdown as primitive ontology.  It should explain
what finite-record structure descends to that GR description.

## 1. Imports From V4

The relevant V4 imports are:

$$
\boxed{
\begin{array}{c|l}
\hbox{source} & \hbox{import}\\
\hline
\mathrm{P25} & \hbox{effective GR descent from finite admissible records}\\
\mathrm{P26} & \hbox{relativistic QFT/QCD as finite descent extension}\\
\mathrm{P27} & \hbox{finite QCD dynamics certificate}\\
\mathrm{P28} & \hbox{continuum YM confinement as ISP descent theorem}
\end{array}
}
$$

For black holes, the most important import is P25:

$$
\boxed{
\hbox{GR is an effective descent, not the primitive ontology.}
}
$$

Therefore the V5 black-hole rule is:

$$
\boxed{
\hbox{do not identify the black hole with a continuum metric artifact
before checking the finite record source.}
}
$$

## 2. The GR Contrast

Classical GR gives two different black-hole features that are often confused.

First, the event horizon:

$$
\boxed{
\hbox{the event horizon is not a local curvature singularity.}
}
$$

For an infalling observer crossing a sufficiently large classical horizon, the
metric need not have a local discontinuity at the crossing event.  The horizon
is global and causal: it marks which events can send signals to future null
infinity.

Second, the singularity:

$$
\boxed{
\hbox{the classical singularity is a breakdown of the continuum solution.}
}
$$

In ideal Schwarzschild language this is associated with \(r=0\).  More
invariantly, singularity theorems diagnose geodesic incompleteness and, in
many examples, curvature invariants diverge.  That is not the same as saying
that nature literally contains an infinitely sharp point object.

The first V5 distinction is therefore:

$$
\boxed{
\begin{array}{c|c}
\hbox{GR feature} & \hbox{ISP interpretation}\\
\hline
\hbox{horizon} & \hbox{record-accessibility boundary}\\
\hbox{singularity} & \hbox{failure of smooth metric descent}\\
\hbox{infinite curvature} & \hbox{invalid extrapolation of effective geometry}
\end{array}
}
$$

## 3. Primitive ISP Black-Hole Data

Let \({\mathcal C}_\Sigma\) be the finite record configuration space on a
hypersurface \(\Sigma\), and let:

$$
\boxed{
\Gamma_{\Sigma_1\leftarrow\Sigma_0}
:
\Delta({\mathcal C}_{\Sigma_0})
\to
\Delta({\mathcal C}_{\Sigma_1})
}
$$

be the finite stochastic transport.

Split records into exterior and interior-readable components relative to an
exterior observer class:

$$
\boxed{
{\mathcal C}_\Sigma
\xrightarrow{\ \pi^{ext}_\Sigma\ }
{\mathcal E}_\Sigma.
}
$$

Here \({\mathcal E}_\Sigma\) is not "the outside of space" as a primitive
continuum region.  It is the algebra of records accessible to exterior
preparations, controls, and detectors.

The exterior channel induced by the full finite law is:

$$
\boxed{
\Gamma^{ext}_{\Sigma_1\leftarrow\Sigma_0}
=
(\pi^{ext}_{\Sigma_1})_\#
\Gamma_{\Sigma_1\leftarrow\Sigma_0}
\iota^{ext}_{\Sigma_0},
}
$$

where \(\iota^{ext}_{\Sigma_0}\) is the declared exterior preparation lift or
reference embedding.

The key point:

$$
\boxed{
\Gamma
\hbox{ may be globally finite and regular while }
\Gamma^{ext}
\hbox{ is lossy, irreversible, or many-to-one.}
}
$$

That is the black-hole opening.

## 4. Definition: Finite Record Horizon

Searchable definition tag:

`V5P1-FINITE-RECORD-HORIZON`.

A finite record horizon for an exterior observer class \({\mathsf O}_{ext}\)
is a triple:

$$
\boxed{
{\mathcal H}_{rec}
=
({\mathcal C}_\Sigma,\pi^{ext}_\Sigma,\Gamma_{\Sigma_1\leftarrow\Sigma_0})
}
$$

such that:

1. the full transport \(\Gamma_{\Sigma_1\leftarrow\Sigma_0}\) is an admissible
   finite ISP law;
2. the exterior record channel \(\Gamma^{ext}\) is well-defined;
3. there exist distinct interior record histories \(h,h'\) with:

$$
\boxed{
h\ne h',
\qquad
\pi^{ext}(h)=\pi^{ext}(h'),
}
$$

or, dynamically:

$$
\boxed{
(\pi^{ext}_{\Sigma_1})_\#
\Gamma(\cdot\mid h)
=
(\pi^{ext}_{\Sigma_1})_\#
\Gamma(\cdot\mid h')
}
$$

for all exterior readouts in the licensed exterior algebra;

4. the equivalence is stable under exterior controls:

$$
\boxed{
M^{ext}K^{ext}
(\pi^{ext}_{\Sigma_1})_\#\Gamma(\cdot\mid h)
=
M^{ext}K^{ext}
(\pi^{ext}_{\Sigma_1})_\#\Gamma(\cdot\mid h')
}
$$

for every licensed exterior control \(K^{ext}\) and readout \(M^{ext}\).

Then \(h\sim_{ext}h'\) defines the exterior indistinguishability relation.

The horizon is the boundary of this equivalence becoming stable:

$$
\boxed{
{\mathcal H}_{rec}
=
\partial\{h:\ h\hbox{ has no exterior-distinguishing return channel}\}.
}
$$

This is not a local metric discontinuity.  It is a record-accessibility
transition.

## 5. The Answer To The Point-Discontinuity Question

The ISP answer is:

$$
\boxed{
\hbox{No single primitive point-discontinuity is required.}
}
$$

There are three separate statements.

First:

$$
\boxed{
\hbox{the horizon is an exterior accessibility boundary, not a local break.}
}
$$

Second:

$$
\boxed{
\hbox{the classical singularity is a failure of smooth GR reconstruction.}
}
$$

Third:

$$
\boxed{
\hbox{the finite ISP law may remain regular where the metric descent fails.}
}
$$

Thus \(r=0\) in the effective Schwarzschild chart should not be promoted into
primitive ontology.  It is a marker saying:

$$
\boxed{
\hbox{the continuum GR variables no longer form a licensed effective
description of the underlying finite record process.}
}
$$

## 6. Einstein Move: Find The Invariant Object

Einstein's move is not to stare at coordinates.  It is to ask what invariant
physical statement survives every admissible description.

For V5 black holes, the invariant object is not:

$$
\boxed{
r=2M
\quad\hbox{or}\quad
r=0
}
$$

as coordinate slogans.

The invariant candidate is:

$$
\boxed{
\hbox{the exterior causal/operational accessibility relation.}
}
$$

In ISP form:

$$
\boxed{
h\sim_{ext}h'
\quad\Longleftrightarrow\quad
\hbox{no licensed exterior experiment distinguishes }h\hbox{ from }h'.
}
$$

This equivalence relation is the black-hole invariant at the finite-record
level.

Searchable principle tag:

`V5P1-EINSTEIN-EXTERIOR-ACCESSIBILITY-INVARIANT`.

The Einstein principle is:

$$
\boxed{
\hbox{black-hole ontology is the invariant exterior-accessibility structure,
not a coordinate singularity.}
}
$$

## 7. Feynman Move: Account For Alternatives

Feynman's move is to ask where the alternatives went.

For a black hole, the real ledger is:

$$
\boxed{
\begin{array}{c}
\hbox{incoming exterior records}\\
\downarrow\\
\hbox{horizon-crossing alternatives}\\
\downarrow\\
\hbox{interior record distinctions}\\
\downarrow\\
\hbox{exterior marginal channel}\\
\downarrow\\
\hbox{late outgoing radiation/readout records}
\end{array}
}
$$

The central question is:

$$
\boxed{
\hbox{Are interior alternatives destroyed, hidden, or returned as correlations?}
}
$$

ISP should express this without primitive Hilbert-space mystery:

$$
\boxed{
\Gamma_{full}
\quad\hbox{versus}\quad
\Gamma^{ext}=(\pi^{ext})_\#\Gamma_{full}\iota^{ext}.
}
$$

The full channel may preserve distinctions that the exterior channel loses.
The information paradox becomes a question about the relation between these
two ledgers.

Searchable principle tag:

`V5P1-FEYNMAN-BLACK-HOLE-ALTERNATIVE-LEDGER`.

## 8. Exterior Compression And Entropy

Given the exterior equivalence relation \(h\sim_{ext}h'\), define an exterior
record cell:

$$
\boxed{
[h]_{ext}
=
\{h':h'\sim_{ext}h\}.
}
$$

The finite degeneracy is:

$$
\boxed{
g_{ext}(e)
=
\#\{h:\pi^{ext}(h)=e\}.
}
$$

or, for weighted finite laws:

$$
\boxed{
S_{rec}^{BH}(e)
=
\log
\sum_{h:\pi^{ext}(h)=e}
w(h).
}
$$

This gives the ISP entropy interpretation:

$$
\boxed{
\hbox{black-hole entropy counts exterior-indistinguishable finite record
alternatives.}
}
$$

This is not yet a derivation of the Bekenstein-Hawking area law.  It is the
ontology in which an area law would have to be proved:

$$
\boxed{
S_{rec}^{BH}
\stackrel{?}{\sim}
{A\over 4G}
}
$$

The V5 target is to derive the area scaling from the finite horizon ledger,
not to assume it.

## 9. Evaporation As Exterior Channel Evolution

Let the exterior observer have access to an outgoing radiation record algebra
\({\mathcal R}_{out}\).  The evaporation channel is:

$$
\boxed{
\Gamma^{rad}_{t_2\leftarrow t_1}
:
{\mathcal E}_{t_1}
\to
{\mathcal E}_{t_2}\otimes{\mathcal R}_{out}.
}
$$

The full law is:

$$
\boxed{
\Gamma^{full}_{t_2\leftarrow t_1}
:
{\mathcal C}_{t_1}
\to
{\mathcal C}_{t_2}.
}
$$

The information question is then:

$$
\boxed{
\hbox{Does the map }
{\mathcal C}_{in}
\to
{\mathcal E}_{late}\otimes{\mathcal R}_{out}
\hbox{ become distinguishing on the relevant record classes?}
}
$$

If yes, the full process may be record-preserving even though intermediate
exterior marginals are lossy.

If no, the finite ISP law contains genuine exterior information loss.

The paradox is no longer:

$$
\boxed{
\hbox{unitary Hilbert-space evolution versus thermal radiation.}
}
$$

It becomes:

$$
\boxed{
\hbox{global finite record distinction versus exterior marginal compression.}
}
$$

## 10. Theorem: No Horizon Discontinuity In The Finite Law

Searchable theorem tag:

`V5P1-NO-HORIZON-DISCONTINUITY-THEOREM`.

### Theorem 10.1

Assume:

1. the full finite transport \(\Gamma_{\Sigma_1\leftarrow\Sigma_0}\) is an
   admissible finite ISP law;
2. exterior projection \(\pi^{ext}\) is a fixed finite record map;
3. the horizon is defined by stability of the exterior equivalence relation
   \(h\sim_{ext}h'\);
4. no discontinuity is inserted into the full transition kernel itself.

Then the finite record horizon is not a primitive local discontinuity.  It is a
change in exterior distinguishability.

Proof.  By assumption the primitive dynamics is the finite stochastic map
\(\Gamma\).  The exterior observer sees only the pushed-forward channel
\((\pi^{ext})_\#\Gamma\iota^{ext}\).  The horizon condition states that
distinct full histories become indistinguishable after applying all licensed
exterior controls and readouts.  This condition changes the quotient of record
histories seen by the exterior algebra, but it does not insert a singular
entry, infinite value, or local discontinuity into \(\Gamma\).  Therefore the
horizon is an accessibility boundary of the exterior representation, not a
primitive discontinuity of the finite law.  `square`

Consequence:

$$
\boxed{
\hbox{A smooth GR horizon descends naturally from a finite record horizon.}
}
$$

## 11. Theorem: Singularity As Descent Failure

Searchable theorem tag:

`V5P1-SINGULARITY-AS-DESCENT-FAILURE`.

Let:

$$
\boxed{
D_{GR}:{\mathcal C}_a\to({\mathcal M},g,T,\ldots)
}
$$

be the effective GR descent map from finite records at refinement scale \(a\).

A GR singularity is an ISP descent failure if, along a family of record states
\(c_a\), one or more of the following fails:

$$
\boxed{
\begin{array}{ll}
\mathrm{DF1}:&\hbox{metric readout remains finite and regular}\\
\mathrm{DF2}:&\hbox{curvature source ledger remains bounded}\\
\mathrm{DF3}:&\hbox{geodesic/causal reconstruction remains extendible}\\
\mathrm{DF4}:&\hbox{record refinements remain projectively compact}\\
\mathrm{DF5}:&\hbox{finite exterior/interior quotient remains smooth in GR variables}
\end{array}
}
$$

### Theorem 11.1

If the full finite ISP law remains defined but at least one of DF1-DF5 fails,
then the corresponding GR singularity is not a primitive finite-record
singularity.  It is a failure of the GR descent.

Proof.  The primitive ontology is the finite record law.  The GR object exists
only when the descent map licenses a smooth metric, curvature, and causal
reconstruction.  If the finite law remains defined while the descent conditions
fail, then the singular behavior belongs to the reconstructed GR variables.
The singularity is therefore a breakdown of the effective description, not an
infinite value in the primitive law.  `square`

## 12. Black-Hole Information In ISP Form

There are three possible information statuses.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{status} & \hbox{full law} & \hbox{exterior law}\\
\hline
\mathrm{BH\text{-}U} &
\hbox{record distinctions preserved} &
\hbox{late radiation recovers them}\\
\mathrm{BH\text{-}H} &
\hbox{record distinctions preserved} &
\hbox{exterior algebra never recovers them}\\
\mathrm{BH\text{-}L} &
\hbox{record distinctions not preserved} &
\hbox{genuine finite record loss}
\end{array}
}
$$

Here:

- \(BH\text{-}U\) is unitary-like at the finite record level;
- \(BH\text{-}H\) is hidden-information behavior;
- \(BH\text{-}L\) is true loss in the primitive finite law.

The V5 program must not assume which one is true.  It must identify the
finite channel packet that decides the trichotomy.

Searchable trichotomy tag:

`V5P1-BLACK-HOLE-INFORMATION-TRICHOTOMY`.

## 13. Firewall Reinterpretation

In GR+QFT language, firewall tension appears when one tries to satisfy
simultaneously:

$$
\boxed{
\hbox{smooth horizon}
\quad+\quad
\hbox{unitary evaporation}
\quad+\quad
\hbox{local QFT exterior/interior factorization.}
}
$$

In ISP, the factorization premise is not primitive.  The finite law may have:

$$
\boxed{
{\mathcal C}_{full}
\not\simeq
{\mathcal E}_{ext}\otimes{\mathcal I}_{int}
}
$$

as a strict product across the horizon.

Therefore the firewall question becomes:

$$
\boxed{
\hbox{Does exterior/interior product factorization hold strongly enough to
force a contradiction?}
}
$$

If the horizon is a quotient of finite records rather than a tensor-product
cut, then some firewall assumptions are not licensed at the primitive level.

This does not prove no firewall.  It changes the audit target:

$$
\boxed{
\hbox{audit factorization before deriving paradox.}
}
$$

## 14. Comparison With GR

$$
\boxed{
\begin{array}{c|c|c}
\hbox{question} & \hbox{classical GR} & \hbox{ISP ontology}\\
\hline
\hbox{What is the horizon?} &
\hbox{causal boundary} &
\hbox{exterior record-accessibility boundary}\\
\hbox{Is the horizon singular?} &
\hbox{no, not locally for large smooth horizons} &
\hbox{no, quotient/accessibility change}\\
\hbox{What is }r=0\hbox{?} &
\hbox{classical singularity in ideal solution} &
\hbox{failure of smooth GR descent}\\
\hbox{What is entropy?} &
\hbox{area law in semiclassical gravity} &
\hbox{exterior-indistinguishable record degeneracy}\\
\hbox{What is evaporation?} &
\hbox{QFT channel on curved background} &
\hbox{evolution of exterior radiation record channel}\\
\hbox{What is information loss?} &
\hbox{unitarity versus thermal marginal} &
\hbox{full record distinction versus exterior compression}
\end{array}
}
$$

## 15. Falsifier Gates

Searchable audit tag:

`V5P1-BLACK-HOLE-ONTOLOGY-GATES-BH1-BH9`.

The finite-record black-hole ontology is falsified or forced to revise if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{BH1} &
\hbox{horizon requires a primitive discontinuity in }\Gamma &
\hbox{record-horizon thesis false}\\
\mathrm{BH2} &
\hbox{exterior equivalence } \sim_{ext}\hbox{ is not stable} &
\hbox{no horizon quotient}\\
\mathrm{BH3} &
\hbox{GR singularity occurs while all descent conditions stay regular} &
\hbox{descent-failure reading false}\\
\mathrm{BH4} &
\hbox{entropy cannot be tied to exterior record degeneracy} &
\hbox{record entropy route false}\\
\mathrm{BH5} &
\hbox{evaporation cannot be represented as exterior radiation channel} &
\hbox{channel ontology incomplete}\\
\mathrm{BH6} &
\hbox{full/exterior channel distinction collapses} &
\hbox{information trichotomy ill-posed}\\
\mathrm{BH7} &
\hbox{strong exterior/interior factorization is primitive and unavoidable} &
\hbox{firewall audit changes}\\
\mathrm{BH8} &
\hbox{V4 GR descent cannot recover classical black-hole exterior} &
\hbox{effective GR compatibility fails}\\
\mathrm{BH9} &
\hbox{finite core cannot replace continuum blow-up without new singular law} &
\hbox{finite regularity route fails}
\end{array}
}
$$

## 16. Immediate V5 Consequences

The paper has three immediate consequences.

### 16.1 No Literal Point Ontology

The ISP ontology should not say:

$$
\boxed{
\hbox{a black hole is a point of infinite density.}
}
$$

It should say:

$$
\boxed{
\hbox{a black hole is an exterior-accessibility structure in a finite record
process.}
}
$$

### 16.2 Horizon Smoothness Is Natural

Because the horizon is not a primitive local discontinuity, smooth horizon
crossing is not surprising.  It is what one expects when the full finite law
remains regular and only the exterior quotient changes.

### 16.3 Singularity Resolution Means Descent Replacement

Resolving the singularity does not mean finding a nicer value of \(g_{\mu\nu}\)
at a continuum point.  It means replacing the invalid continuum descent by a
finite record core law:

$$
\boxed{
\hbox{singularity resolution}
=
\hbox{finite core packet plus controlled exterior GR matching.}
}
$$

## 17. Minimal Packet For The Next Paper

The next paper should print a concrete finite black-hole packet:

$$
\boxed{
{\mathcal B}_{BH}
=
({\mathcal C}_{in},{\mathcal C}_{core},{\mathcal E}_{out},
\Gamma_{in\to core},\Gamma_{core\to out},\pi^{ext},M^{ext},S_{rec}).
}
$$

The packet must decide:

$$
\boxed{
\begin{array}{ll}
\mathrm{Q1}:&\hbox{which record classes become exterior-indistinguishable?}\\
\mathrm{Q2}:&\hbox{does entropy scale with the horizon boundary area?}\\
\mathrm{Q3}:&\hbox{does late radiation recover interior distinctions?}\\
\mathrm{Q4}:&\hbox{does the exterior metric descent match GR outside the horizon?}\\
\mathrm{Q5}:&\hbox{does the core avoid infinite curvature by descent failure?}
\end{array}
}
$$

The first question is the foundation question.  Before entropy, evaporation,
or core regularity can be audited, the paper must say exactly which full
finite records the exterior algebra cannot tell apart.

Searchable Q1 audit tag:

`V5P1-Q1-EXTERIOR-INDISTINGUISHABILITY-AUDIT`.

### 17.1 Q1 Einstein Route: Exterior Operational Invariant

The Einstein move is to remove coordinate language and ask for the invariant
operational object.

Do not begin with:

$$
\boxed{
\hbox{which point, radius, or interior coordinate is hidden?}
}
$$

Begin with:

$$
\boxed{
\hbox{which full finite records induce the same exterior operational
relation?}
}
$$

Let \({\mathfrak P}^{ext}\) be the licensed exterior probe family:

$$
\boxed{
{\mathfrak P}^{ext}
=
\{(I^{ext}_a,K^{ext}_a,M^{ext}_a)\}_{a\in A}.
}
$$

Here \(I^{ext}_a\) is an exterior preparation or reference embedding,
\(K^{ext}_a\) is a finite exterior control sequence, and \(M^{ext}_a\) is an
exterior readout.  The Einstein invariant of a full history \(h\) is the
complete exterior response family:

$$
\boxed{
{\mathcal R}^{E}_{ext}(h)
=
\left\{
M^{ext}_a K^{ext}_a
(\pi^{ext})_\#\Gamma(\cdot\mid h)
\right\}_{a\in A}.
}
$$

Then the Einstein equivalence relation is:

$$
\boxed{
h\sim_E h'
\quad\Longleftrightarrow\quad
{\mathcal R}^{E}_{ext}(h)
=
{\mathcal R}^{E}_{ext}(h').
}
$$

This is the black-hole no-hair question in ISP form.  The exterior-visible
labels are exactly those labels that change \({\mathcal R}^{E}_{ext}\).  The
interior labels hidden behind the finite record horizon are exactly those
labels in the kernel of this exterior response map.

Therefore the Einstein answer to Q1 is:

$$
\boxed{
\hbox{exterior-indistinguishable classes are invariant response classes of }
{\mathcal R}^{E}_{ext}.
}
$$

This keeps the ontology honest.  It does not say that the hidden distinctions
do not exist.  It says that, relative to the exterior observer class, they are
not independent exterior facts.

### 17.2 Q1 Feynman Route: Exterior Influence Ledger

The Feynman move is not to guess a small model.  It is to keep the full ledger
of alternatives and only then project it through the exterior channel.

For each full history \(h\), define its exterior influence functional:

$$
\boxed{
{\mathcal I}^{F}_{ext}(h)
=
\left[
\hbox{the complete induced exterior probability law for all licensed
exterior probe histories}
\right].
}
$$

Equivalently:

$$
\boxed{
{\mathcal I}^{F}_{ext}(h)(a,e)
=
\Pr_\Gamma(e\mid h,I^{ext}_a,K^{ext}_a,M^{ext}_a),
\qquad
a\in A,\ e\in{\mathcal E}^{read}_a.
}
$$

Then:

$$
\boxed{
h\sim_F h'
\quad\Longleftrightarrow\quad
{\mathcal I}^{F}_{ext}(h)
=
{\mathcal I}^{F}_{ext}(h').
}
$$

The point of the Feynman route is accounting.  Interior alternatives are not
discarded.  They remain separate entries in the full finite record ledger:

$$
\boxed{
h\ne h'
\quad\hbox{in }{\mathcal C}_{full}
}
$$

but they become one exterior class if their whole influence on exterior
probability records is identical:

$$
\boxed{
{\mathcal I}^{F}_{ext}(h)
=
{\mathcal I}^{F}_{ext}(h').
}
$$

Therefore the Feynman answer to Q1 is:

$$
\boxed{
\hbox{exterior-indistinguishable classes are equal-influence classes in the
full alternative ledger.}
}
$$

This avoids two false shortcuts:

$$
\boxed{
\begin{array}{ll}
\hbox{false shortcut 1:}&\hbox{hidden alternatives do not exist}\\
\hbox{false shortcut 2:}&\hbox{every hidden alternative is exterior-visible in
principle}
\end{array}
}
$$

The ledger allows either outcome, but it requires the outcome to be printed by
the finite channel law.

### 17.3 Einstein-Feynman Agreement Criterion

The two routes agree if the invariant exterior response family and the
influence ledger generate the same quotient:

$$
\boxed{
h\sim_E h'
\quad\Longleftrightarrow\quad
h\sim_F h'.
}
$$

This is the Q1 closure condition:

$$
\boxed{
\ker{\mathcal R}^{E}_{ext}
=
\ker{\mathcal I}^{F}_{ext}.
}
$$

When this holds, the exterior-indistinguishable classes are:

$$
\boxed{
[h]_{BH}
=
\{h'\in{\mathcal C}_{full}:
{\mathcal I}^{F}_{ext}(h')
=
{\mathcal I}^{F}_{ext}(h)\}.
}
$$

The quotient record space seen by the exterior is:

$$
\boxed{
{\mathcal C}_{BH}^{ext}
=
{\mathcal C}_{full}/\sim_{BH}.
}
$$

where:

$$
\boxed{
\sim_{BH}
=
\sim_E
=
\sim_F.
}
$$

Thus Q1 is no longer a verbal question.  It is a kernel computation:

$$
\boxed{
\hbox{Q1 asks for the kernel of the full-to-exterior influence map.}
}
$$

### 17.4 Q1 Record-Class Stratification

The quotient should not be flattened too soon.  The exterior classes split
into four possible strata.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{class} & \hbox{definition} & \hbox{black-hole meaning}\\
\hline
\mathrm{Q1\text{-}H} &
\hbox{distinguished by asymptotic/exterior charges} &
\hbox{exterior hair}\\
\mathrm{Q1\text{-}T} &
\hbox{indistinguishable at finite exterior time but later recovered} &
\hbox{transient compression}\\
\mathrm{Q1\text{-}K} &
\hbox{preserved by the full law but never exterior-distinguished} &
\hbox{hidden finite record sector}\\
\mathrm{Q1\text{-}L} &
\hbox{not preserved by the full finite law} &
\hbox{true finite record loss}
\end{array}
}
$$

The important distinction is between \(\mathrm{Q1\text{-}K}\) and
\(\mathrm{Q1\text{-}L}\).  Both can look identical to an exterior observer.
They are not ontologically identical:

$$
\boxed{
\begin{array}{c|c}
\mathrm{Q1\text{-}K} & \hbox{full record distinction exists, exterior quotient
forgets it}\\
\mathrm{Q1\text{-}L} & \hbox{full record distinction is erased by the finite
law itself}
\end{array}
}
$$

This is the clean ISP version of the information problem.

### 17.5 Candidate Exterior Hair

The Q1 audit should expect some labels to remain visible to the exterior
because changing them changes the exterior response family.  The conservative
candidate list is:

$$
\boxed{
\begin{array}{c|l}
\hbox{candidate exterior label} & \hbox{reason}\\
\hline
M & \hbox{changes exterior gravitational descent and asymptotic energy}\\
J & \hbox{changes rotational/asymptotic frame-dragging records}\\
Q_a & \hbox{changes licensed gauge-charge flux records}\\
{\mathcal M}_{soft} & \hbox{changes licensed asymptotic memory records if
included}\\
{\mathcal R}_{rad}^{late} & \hbox{changes late radiation records if the
evaporation channel is distinguishing}
\end{array}
}
$$

The list is not assumed final.  It is an audit list.  A label is genuine
exterior hair only if:

$$
\boxed{
{\mathcal R}^{E}_{ext}(h)
\ne
{\mathcal R}^{E}_{ext}(h')
}
$$

for histories differing only by that label.

Conversely, an interior distinction is exterior-hidden only if:

$$
\boxed{
{\mathcal R}^{E}_{ext}(h)
=
{\mathcal R}^{E}_{ext}(h')
}
$$

for all licensed exterior probes, including late radiation probes if those are
part of the exterior observer class.

### 17.6 Q1 Falsifier Gates

Searchable Q1 gates tag:

`V5P1-Q1-GATES-EF1-EF7`.

The Q1 classification fails or must be revised if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{EF1} &
{\mathfrak P}^{ext}\hbox{ is not declared before classification} &
\hbox{posterior exterior observer fitting}\\
\mathrm{EF2} &
\pi^{ext}\hbox{ changes with the desired conclusion} &
\hbox{moving exterior quotient}\\
\mathrm{EF3} &
\sim_E\hbox{ and }\sim_F\hbox{ disagree} &
\hbox{invariant/probability ledger mismatch}\\
\mathrm{EF4} &
\hbox{late radiation probes are omitted without a rule} &
\hbox{premature information-loss claim}\\
\mathrm{EF5} &
\hbox{asymptotic charge or memory labels are hidden by hand} &
\hbox{bad no-hair classification}\\
\mathrm{EF6} &
\mathrm{Q1\text{-}K}\hbox{ and }\mathrm{Q1\text{-}L}\hbox{ are identified} &
\hbox{hidden information confused with true loss}\\
\mathrm{EF7} &
\hbox{the quotient is not stable under exterior controls} &
\hbox{no finite record horizon}
\end{array}
}
$$

If EF1-EF7 pass, then Q1 has a precise ISP answer:

$$
\boxed{
\begin{gathered}
\hbox{the exterior-indistinguishable records are exactly the}\\
\sim_{BH}\hbox{-equivalence classes of the full-to-exterior influence map}
\end{gathered}
}
$$

### 17.7 Q1 Verdict For Paper 1

Paper 1 does not yet print the full numerical black-hole packet.  But it does
settle what the packet must compute.

The packet must print:

$$
\boxed{
({\mathfrak P}^{ext},\pi^{ext},\Gamma,
{\mathcal R}^{E}_{ext},{\mathcal I}^{F}_{ext},\sim_{BH},
{\mathcal C}_{BH}^{ext}).
}
$$

Then Q1 is answered by:

$$
\boxed{
\hbox{record classes become exterior-indistinguishable exactly when their
complete exterior influence functionals agree.}
}
$$

That is the Einstein-Feynman synthesis:

$$
\boxed{
\hbox{Einstein supplies the invariant exterior relation; Feynman supplies the
full alternative ledger.}
}
$$

### 17.8 Q2: Area Scaling As An Exterior-Screen Question

Q2 asks:

$$
\boxed{
\hbox{does entropy scale with the horizon boundary area?}
}
$$

The dangerous mistake is to count all interior records as independent exterior
states.  In ISP, black-hole entropy is not first a count of coordinate-volume
bulk points.  It is a count of exterior-distinguishable influence classes.

Searchable Q2 audit tag:

`V5P1-Q2-AREA-ENTROPY-AUDIT`.

The question should therefore be rewritten as:

$$
\boxed{
\hbox{does the full-to-exterior influence map factor through a finite
horizon screen whose capacity is area-extensive?}
}
$$

If yes, the leading entropy is an area law.  If no, the ontology has either a
volume-law black hole or an incomplete exterior-screen principle.

### 17.9 Q2 Einstein Route: The Invariant Horizon Screen

The Einstein move is to replace coordinate volume by an invariant
accessibility cut.

Let \({\mathcal B}_{\mathcal H}\) be the finite horizon-screen record algebra
for the exterior observer class.  It is not assumed to be a literal membrane.
It is the minimal record interface through which all exterior influence of the
black-hole core must pass.

The Einstein screen condition is:

$$
\boxed{
{\mathcal C}_{full}
\xrightarrow{\ \partial_{\mathcal H}\ }
{\mathcal B}_{\mathcal H}
\xrightarrow{\ \Phi^{ext}_{\mathcal H}\ }
{\mathcal E}_{out},
}
$$

with:

$$
\boxed{
{\mathcal I}^{F}_{ext}(h)
=
\Phi^{ext}_{\mathcal H}(\partial_{\mathcal H}h).
}
$$

Thus:

$$
\boxed{
h\sim_{BH}h'
\quad\Longleftrightarrow\quad
\Phi^{ext}_{\mathcal H}(\partial_{\mathcal H}h)
=
\Phi^{ext}_{\mathcal H}(\partial_{\mathcal H}h').
}
$$

The geometric word "area" enters only after the finite screen descends to a
GR horizon cross-section.  Let the screen decompose into finite cells:

$$
\boxed{
{\mathcal B}_{\mathcal H}
\simeq
\bigotimes_{x\in{\mathcal S}_{\mathcal H}}
{\mathcal B}_x,
\qquad
A_{\mathcal H}
=
\sum_{x\in{\mathcal S}_{\mathcal H}} a_x.
}
$$

If each cell has bounded finite capacity:

$$
\boxed{
\log |{\mathcal B}_x|
=
\sigma_x a_x+O(a_x^{sub}),
}
$$

then:

$$
\boxed{
\log |{\mathcal B}_{\mathcal H}|
=
\sum_x \log |{\mathcal B}_x|
=
\sigma_{\mathcal H}A_{\mathcal H}
+O(\partial{\mathcal S}_{\mathcal H}).
}
$$

The Einstein answer to Q2 is:

$$
\boxed{
\hbox{area scaling follows if exterior distinguishability is controlled by an
invariant minimal horizon screen, not by interior coordinate volume.}
}
$$

The coefficient \(\sigma_{\mathcal H}\) is not free decoration.  A fully
calibrated GR match must recover:

$$
\boxed{
\sigma_{\mathcal H}
=
\frac{1}{4G\hbar}
}
$$

in units where the entropy is dimensionless.  Until that coefficient is
derived or calibrated from the finite packet, Paper 1 claims the area mechanism
but not the final numerical Bekenstein-Hawking coefficient.

### 17.10 Q2 Feynman Route: Interior Alternatives As Boundary Weights

The Feynman move is to keep every interior alternative in the ledger.  One
does not throw away the interior.  One groups it by the boundary influence it
actually presents to the exterior.

For a horizon-screen record \(b\in{\mathcal B}_{\mathcal H}\), define:

$$
\boxed{
W(b)
=
\sum_{h:\ \partial_{\mathcal H}h=b}
\mu(h).
}
$$

Here \(W(b)\) is the full interior alternative weight behind the same exterior
screen record.  The exterior probability of a screen class is:

$$
\boxed{
p(b)
=
\frac{W(b)}{\sum_{b'}W(b')}.
}
$$

The exterior entropy is:

$$
\boxed{
S^{ext}_{rec}
=
-\sum_{b\in{\mathcal B}_{\mathcal H}}p(b)\log p(b).
}
$$

The bulk interior histories still matter.  They renormalize \(W(b)\).  But
they do not create new exterior classes unless they change the boundary
influence record:

$$
\boxed{
h,h'\hbox{ create distinct exterior entropy states only if }
\partial_{\mathcal H}h
\not\sim_{\Phi}
\partial_{\mathcal H}h'.
}
$$

where:

$$
\boxed{
b\sim_{\Phi}b'
\quad\Longleftrightarrow\quad
\Phi^{ext}_{\mathcal H}(b)
=
\Phi^{ext}_{\mathcal H}(b').
}
$$

Thus the Feynman answer to Q2 is:

$$
\boxed{
\hbox{area scaling is a statement about the support of the exterior boundary
ledger, not the disappearance of interior alternatives.}
}
$$

The interior volume becomes dangerous only if it generates independent
exterior influence labels not mediated by the screen:

$$
\boxed{
\hbox{volume law threat}
=
\hbox{independent bulk labels that survive the exterior quotient.}
}
$$

### 17.11 Q2 Area-Law Theorem Target

The Q2 theorem target is:

$$
\boxed{
S^{ext}_{rec}
=
\sigma_{\mathcal H}A_{\mathcal H}
+o(A_{\mathcal H}).
}
$$

It follows from four finite-record hypotheses.

$$
\boxed{
\begin{array}{c|l}
\hbox{hypothesis} & \hbox{meaning}\\
\hline
\mathrm{AS1} &
\hbox{all exterior influence factors through }{\mathcal B}_{\mathcal H}\\
\mathrm{AS2} &
\hbox{screen cells compose locally up to controlled edge corrections}\\
\mathrm{AS3} &
\hbox{cell capacities have finite area density }\sigma_{\mathcal H}\\
\mathrm{AS4} &
\hbox{bulk ledger weights }W(b)\hbox{ have no uncontrolled volume-extensive
variation across exterior classes}
\end{array}
}
$$

Under AS1-AS3, the number of possible exterior screen classes satisfies:

$$
\boxed{
e^{\sigma_-A_{\mathcal H}-o(A_{\mathcal H})}
\le
N^{ext}_{\mathcal H}
\le
e^{\sigma_+A_{\mathcal H}+o(A_{\mathcal H})}.
}
$$

If \(\sigma_-=\sigma_+=\sigma_{\mathcal H}\), then:

$$
\boxed{
\log N^{ext}_{\mathcal H}
=
\sigma_{\mathcal H}A_{\mathcal H}
+o(A_{\mathcal H}).
}
$$

AS4 upgrades this support-counting statement into an entropy statement for
the actual exterior probability law:

$$
\boxed{
S^{ext}_{rec}
=
\sigma_{\mathcal H}A_{\mathcal H}
+o(A_{\mathcal H}).
}
$$

If AS4 fails, the theory may still have an area-sized support, but the actual
entropy can be dominated by uneven interior weights.  That is not a small
technicality; it is a real audit gate.

### 17.12 Q2 Falsifier Gates

Searchable Q2 gates tag:

`V5P1-Q2-GATES-AS1-AS8`.

The Q2 area route fails or must be revised if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{AS1} &
\partial_{\mathcal H}\hbox{ is chosen after the entropy target} &
\hbox{posterior screen fitting}\\
\mathrm{AS2} &
\hbox{exterior influence does not factor through }{\mathcal B}_{\mathcal H} &
\hbox{no screen-controlled entropy}\\
\mathrm{AS3} &
\hbox{screen cells do not compose locally} &
\hbox{no area additivity}\\
\mathrm{AS4} &
\log |{\mathcal B}_x|\hbox{ has no finite density per area} &
\hbox{no area capacity law}\\
\mathrm{AS5} &
\hbox{bulk labels create independent exterior classes at volume rate} &
\hbox{volume-law threat}\\
\mathrm{AS6} &
W(b)\hbox{ varies with uncontrolled volume-extensive bias} &
\hbox{boundary support does not control entropy}\\
\mathrm{AS7} &
\sigma_{\mathcal H}\hbox{ cannot be matched to }1/(4G\hbar) &
\hbox{area scaling without GR coefficient}\\
\mathrm{AS8} &
\hbox{late radiation changes the quotient without being included} &
\hbox{premature entropy count}
\end{array}
}
$$

Passing AS1-AS6 gives a genuine ISP area law.  Passing AS7 gives the calibrated
Bekenstein-Hawking coefficient.  Passing AS8 keeps the entropy count consistent
with the information trichotomy.

### 17.13 Q2 Verdict For Paper 1

Paper 1 does not yet prove the numerical entropy coefficient.  It does settle
the route:

$$
\boxed{
\hbox{black-hole entropy should count exterior screen influence classes, not
raw interior volume records.}
}
$$

The next packet must therefore print:

$$
\boxed{
({\mathcal B}_{\mathcal H},\partial_{\mathcal H},
\Phi^{ext}_{\mathcal H},\{ {\mathcal B}_x,a_x\}_{x\in{\mathcal S}_{\mathcal H}},
W(b),S^{ext}_{rec}).
}
$$

Then Q2 is answered by:

$$
\boxed{
\hbox{entropy scales with area exactly when the exterior influence ledger is
screen-local and area-capacitated.}
}
$$

That is the Einstein-Feynman synthesis for Q2:

$$
\boxed{
\hbox{Einstein supplies the invariant screen; Feynman supplies the summed
interior ledger behind each screen record.}
}
$$

### 17.14 Q3: Late Radiation As Quotient Refinement

Q3 asks:

$$
\boxed{
\hbox{does late radiation recover interior distinctions?}
}
$$

This is not first a question about whether each emitted quantum looks thermal.
Thermal one-time marginals can hide correlations.  The real ISP question is
whether the exterior equivalence relation becomes finer when the exterior
observer class is enlarged to include the complete evaporation record.

Searchable Q3 audit tag:

`V5P1-Q3-LATE-RADIATION-QUOTIENT-AUDIT`.

Let:

$$
\boxed{
{\mathfrak A}^{early}_{ext}
=
\hbox{the exterior record algebra before late evaporation readout}
}
$$

and:

$$
\boxed{
{\mathfrak A}^{evap}_{ext}
=
{\mathfrak A}^{early}_{ext}
\vee
{\mathfrak R}^{late}_{rad}
\vee
{\mathfrak M}^{soft}
\vee
{\mathfrak C}^{corr}_{out}.
}
$$

Here \({\mathfrak R}^{late}_{rad}\) is the late radiation record algebra,
\({\mathfrak M}^{soft}\) is any licensed asymptotic memory algebra, and
\({\mathfrak C}^{corr}_{out}\) is the algebra of exterior correlations among
the emitted records.

The Q3 question is:

$$
\boxed{
\sim_{evap}
\quad\hbox{versus}\quad
\sim_{early}.
}
$$

If the late exterior algebra refines the early quotient, radiation recovers
some hidden distinctions.  If it does not refine the quotient, radiation does
not recover them for that exterior observer class.

### 17.15 Q3 Einstein Route: The Complete Exterior Domain

The Einstein move is to define the complete operational exterior before
arguing about information.

For a full record history \(h\), define:

$$
\boxed{
{\mathcal R}^{E}_{early}(h)
=
\hbox{all response probabilities visible in }{\mathfrak A}^{early}_{ext},
}
$$

and:

$$
\boxed{
{\mathcal R}^{E}_{evap}(h)
=
\hbox{all response probabilities visible in }{\mathfrak A}^{evap}_{ext}.
}
$$

Then:

$$
\boxed{
h\sim_{early}h'
\quad\Longleftrightarrow\quad
{\mathcal R}^{E}_{early}(h)
=
{\mathcal R}^{E}_{early}(h'),
}
$$

while:

$$
\boxed{
h\sim_{evap}h'
\quad\Longleftrightarrow\quad
{\mathcal R}^{E}_{evap}(h)
=
{\mathcal R}^{E}_{evap}(h').
}
$$

Since \({\mathfrak A}^{early}_{ext}\subseteq{\mathfrak A}^{evap}_{ext}\),
one has:

$$
\boxed{
\sim_{evap}
\subseteq
\sim_{early}.
}
$$

The Einstein answer to Q3 is therefore a quotient-refinement statement:

$$
\boxed{
\hbox{late radiation recovers information exactly to the extent that }
\sim_{evap}
\hbox{ is strictly finer than }
\sim_{early}.
}
$$

This replaces the vague phrase "information escapes" with an invariant
operational comparison of two exterior equivalence relations.

### 17.16 Q3 Feynman Route: The Full Joint Radiation Ledger

The Feynman move is to keep the whole evaporation ledger, not only the local
thermal marginals.

For a full history \(h\), define:

$$
\boxed{
{\mathcal I}^{F}_{rad}(h)(a,r_1,\ldots,r_N,m,e)
=
\Pr_\Gamma(r_1,\ldots,r_N,m,e
\mid h,I^{ext}_a,K^{ext}_a).
}
$$

Here \(r_1,\ldots,r_N\) are emitted radiation records, \(m\) is a memory or
soft record if licensed, and \(e\) is any remaining exterior readout.

The one-step radiation marginals are:

$$
\boxed{
T_n(h)(r_n)
=
\sum_{\widehat r_n,m,e}
{\mathcal I}^{F}_{rad}(h)(a,r_1,\ldots,r_N,m,e).
}
$$

The crucial ledger warning is:

$$
\boxed{
T_n(h)=T_n(h')\hbox{ for all }n
\quad\not\Rightarrow\quad
{\mathcal I}^{F}_{rad}(h)
=
{\mathcal I}^{F}_{rad}(h').
}
$$

Thus:

$$
\boxed{
\hbox{thermal marginals do not prove information loss.}
}
$$

Loss is licensed only if the complete joint exterior radiation ledger is
independent of the hidden interior distinction:

$$
\boxed{
{\mathcal I}^{F}_{rad}(h)
=
{\mathcal I}^{F}_{rad}(h')
}
$$

for every pair \(h,h'\) whose distinction is under audit.

The Feynman answer to Q3 is:

$$
\boxed{
\hbox{late radiation recovers a distinction exactly when the complete joint
radiation ledger changes with that distinction.}
}
$$

### 17.17 Q3 Recovery Theorem Target

Define the early-hidden sector:

$$
\boxed{
{\mathcal H}_{early}
=
\{(h,h'):
h\sim_{early}h',
\ h\not\sim_{full}h'\}.
}
$$

Here \(h\sim_{full}h'\) means that the full finite law itself makes the two
records identical under all full-record readouts.  It is the primitive
finite-law equivalence, not merely the exterior quotient.

Then Q3 has four clean outcomes:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{status} & \hbox{condition} & \hbox{meaning}\\
\hline
\mathrm{Q3\text{-}U} &
\ker{\mathcal R}^{E}_{evap}\cap{\mathcal H}_{early}=\varnothing &
\hbox{late radiation separates all early-hidden full distinctions}\\
\mathrm{Q3\text{-}P} &
\varnothing\ne
\ker{\mathcal R}^{E}_{evap}\cap{\mathcal H}_{early}
\subsetneq{\mathcal H}_{early} &
\hbox{late radiation gives partial recovery}\\
\mathrm{Q3\text{-}H} &
\ker{\mathcal R}^{E}_{evap}\cap{\mathcal H}_{early}
={\mathcal H}_{early} &
\hbox{distinctions remain exterior-hidden}\\
\mathrm{Q3\text{-}L} &
h\sim_{full}h'\hbox{ for audited distinctions} &
\hbox{true finite record loss}
\end{array}
}
$$

The theorem target is:

$$
\boxed{
\hbox{evaporation is information-preserving on a hidden sector iff }
\ker{\mathcal R}^{E}_{evap}
\hbox{ equals the full-law kernel on that sector.}
}
$$

Equivalently, using the Feynman ledger:

$$
\boxed{
\ker{\mathcal I}^{F}_{rad}
\cap
{\mathcal H}_{early}
=
\ker_{full}
\cap
{\mathcal H}_{early}.
}
$$

### 17.18 Q3 Falsifier Gates

Searchable Q3 gates tag:

`V5P1-Q3-GATES-RQ1-RQ9`.

The Q3 radiation-recovery route fails or must be revised if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{RQ1} &
{\mathfrak A}^{evap}_{ext}\hbox{ is not declared before the audit} &
\hbox{posterior exterior algebra}\\
\mathrm{RQ2} &
\hbox{late radiation records are replaced by one-time marginals only} &
\hbox{correlation ledger erased}\\
\mathrm{RQ3} &
{\mathfrak M}^{soft}\hbox{ or memory records are omitted without a rule} &
\hbox{missing exterior hair}\\
\mathrm{RQ4} &
\sim_{early}\hbox{ and }\sim_{evap}\hbox{ are not compared on the same
full-record sector} &
\hbox{bad quotient comparison}\\
\mathrm{RQ5} &
\hbox{thermal marginal behavior is treated as proof of loss} &
\hbox{invalid inference}\\
\mathrm{RQ6} &
\hbox{full-law loss is confused with exterior-hidden preservation} &
\hbox{Q3-H/Q3-L collapse}\\
\mathrm{RQ7} &
\hbox{radiation backreaction changes }\Gamma\hbox{ but is not included} &
\hbox{incomplete evaporation channel}\\
\mathrm{RQ8} &
\hbox{late exterior probes disturb the class being classified without a rule} &
\hbox{measurement/control ambiguity}\\
\mathrm{RQ9} &
\ker{\mathcal R}^{E}_{evap}\ne\ker{\mathcal I}^{F}_{rad}
\hbox{ on audited records} &
\hbox{Einstein/Feynman mismatch}
\end{array}
}
$$

Passing RQ1-RQ9 gives a well-posed ISP information-recovery audit.  It does
not force recovery or loss.  It tells the packet exactly what must decide the
question.

### 17.19 Q3 Verdict For Paper 1

Paper 1 does not yet prove which of Q3-U, Q3-P, Q3-H, or Q3-L holds for the
physical black-hole packet.  It does settle the form of the question:

$$
\boxed{
\hbox{late radiation recovers interior distinctions exactly when the complete
evaporation exterior algebra refines the early exterior quotient.}
}
$$

The next packet must therefore print:

$$
\boxed{
({\mathfrak A}^{early}_{ext},{\mathfrak A}^{evap}_{ext},
{\mathcal R}^{E}_{early},{\mathcal R}^{E}_{evap},
{\mathcal I}^{F}_{rad},
\sim_{early},\sim_{evap},\sim_{full}).
}
$$

That is the Einstein-Feynman synthesis for Q3:

$$
\boxed{
\hbox{Einstein supplies the complete exterior domain; Feynman supplies the
joint radiation correlation ledger.}
}
$$

### 17.20 Q4: Exterior GR Descent As Operational Geometry

Q4 asks:

$$
\boxed{
\hbox{does the exterior metric descent match GR outside the horizon?}
}
$$

The question is not whether the primitive ontology contains a continuum
metric.  It does not.  The question is whether the exterior finite-record
response admits GR as its effective decoder.

Searchable Q4 audit tag:

`V5P1-Q4-EXTERIOR-GR-DESCENT-AUDIT`.

Let the exterior GR probe ledger be:

$$
\boxed{
{\mathfrak G}^{ext}_{probe}
=
\{\hbox{clock, light, redshift, lensing, orbit, scattering, ringdown,
memory, horizon-approach probes}\}.
}
$$

For each probe \(a\), let:

$$
\boxed{
{\mathcal O}^{ISP}_a
=
\hbox{the finite-record exterior response printed by }\Gamma.
}
$$

The exterior GR descent problem is to decide whether there exists an effective
Lorentzian exterior geometry:

$$
\boxed{
D^{ext}_{GR}({\mathcal R}^{ISP}_{ext})
=
({\mathcal M}_{ext},g^{eff}_{\mu\nu},T^{eff}_{\mu\nu},
M,J,Q,\ldots)
}
$$

such that:

$$
\boxed{
\|{\mathcal O}^{ISP}_a
-
{\mathcal O}^{GR}_a[g^{eff},T^{eff}]\|
\le
\varepsilon_a
\qquad
\hbox{for every licensed exterior probe }a.
}
$$

Q4 passes in the GR regime when the error ledger
\(\{\varepsilon_a\}\) is inside the licensed finite-record correction bounds
from the V4 effective-GR descent.

### 17.21 Q4 Einstein Route: Metric From Exterior Operations

The Einstein move is to reconstruct the exterior metric from operational
relations rather than assuming coordinates.

Define the exterior operational geometry:

$$
\boxed{
{\mathcal G}^{E}_{ext}
=
\left(
{\mathcal C}^{ext},
{\mathcal L}^{ext},
{\mathcal T}^{ext},
{\mathcal A}^{ext},
{\mathcal Q}^{ext}
\right).
}
$$

The entries are:

$$
\boxed{
\begin{array}{c|l}
\hbox{symbol} & \hbox{meaning}\\
\hline
{\mathcal C}^{ext} & \hbox{exterior causal/light-cone order}\\
{\mathcal L}^{ext} & \hbox{lensing and null propagation response}\\
{\mathcal T}^{ext} & \hbox{clock, redshift, and time-delay response}\\
{\mathcal A}^{ext} & \hbox{acceleration, orbit, and geodesic-deviation response}\\
{\mathcal Q}^{ext} & \hbox{asymptotic charges, memory, and ringdown response}
\end{array}
}
$$

The Einstein exterior matching condition is:

$$
\boxed{
{\mathcal G}^{E}_{ext}
\simeq_{\varepsilon}
{\mathcal G}^{GR}_{ext}[g^{eff}_{\mu\nu},T^{eff}_{\mu\nu}].
}
$$

This means all exterior operational relations are decoded by one and the same
effective metric, not by unrelated fitted functions.  In particular:

$$
\boxed{
\begin{array}{ll}
\mathrm{E1}:&\hbox{the light-cone response defines one Lorentzian causal cone}\\
\mathrm{E2}:&\hbox{clock/redshift records agree with the same metric}\\
\mathrm{E3}:&\hbox{orbits and lensing use the same exterior connection}\\
\mathrm{E4}:&\hbox{asymptotic charges determine the stationary exterior sector}\\
\mathrm{E5}:&\hbox{horizon approach is regular in infalling operational records}
\end{array}
}
$$

The conservative target is the Kerr-Newman exterior family when the only
visible exterior labels are mass, angular momentum, and gauge charges:

$$
\boxed{
g^{eff}_{ext}
=
g^{KN}_{ext}(M,J,Q)
+\delta g^{ISP}_{ext}.
}
$$

with:

$$
\boxed{
\|\delta g^{ISP}_{ext}\|_{probe}
\le
\varepsilon_{GR}.
}
$$

The Einstein answer to Q4 is:

$$
\boxed{
\hbox{ISP matches the black-hole exterior of GR iff exterior operations have a
single Lorentzian GR decoder with controlled finite-record corrections.}
}
$$

### 17.22 Q4 Feynman Route: Sum The Core Into An Exterior Influence Law

The Feynman move is to account for the black-hole core by summing it into an
effective exterior influence law.

Let \(c\in{\mathcal C}_{core}\) be finite core records and
\(b\in{\mathcal B}_{\mathcal H}\) be horizon-screen records.  Define:

$$
\boxed{
{\mathcal K}^{BH}_{ext}(e_{out}\mid e_{in})
=
\sum_{c,b}
\Gamma^{out}(e_{out}\mid b,e_{in})
\Gamma^{scr}(b\mid c,e_{in})
\mu_{core}(c\mid e_{in}).
}
$$

This is the exterior ledger after the hidden core alternatives have been
summed.  The core is not ignored.  It contributes exactly through the
effective exterior response functions of \({\mathcal K}^{BH}_{ext}\).

The Feynman exterior-GR question is:

$$
\boxed{
{\mathcal K}^{BH}_{ext}
\in
{\mathfrak U}_{EH}^{BH}
\quad ?
}
$$

where \({\mathfrak U}_{EH}^{BH}\) is the finite-record exterior universality
class whose long-distance decoder is the Einstein-Hilbert black-hole exterior.

Operationally this means:

$$
\boxed{
\begin{array}{ll}
\mathrm{F1}:&\hbox{the summed core ledger contributes only licensed exterior
charges and response functions}\\
\mathrm{F2}:&\hbox{unlicensed core details do not become new exterior hair}\\
\mathrm{F3}:&\hbox{the exterior two-point, scattering, and ringdown responses
match the GR decoder}\\
\mathrm{F4}:&\hbox{absorption and memory records are included in the same ledger}\\
\mathrm{F5}:&\hbox{finite-record corrections are bounded, not hidden by
discarding probes}
\end{array}
}
$$

The Feynman answer to Q4 is:

$$
\boxed{
\hbox{the black-hole exterior is GR-like exactly when the summed core ledger
falls into the Einstein-Hilbert exterior universality class.}
}
$$

If the summed ledger prints extra low-energy exterior response functions, then
Q4 does not fail automatically.  It branches:

$$
\boxed{
\hbox{extra exterior response}
\Rightarrow
\hbox{controlled ISP correction or new black-hole hair.}
}
$$

But it may no longer be pure GR.

### 17.23 Q4 Descent Theorem Target

Q4 has four possible statuses.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{status} & \hbox{condition} & \hbox{meaning}\\
\hline
\mathrm{Q4\text{-}GR} &
{\mathcal G}^{E}_{ext}\simeq_{\varepsilon}{\mathcal G}^{GR}_{ext}
\hbox{ and }{\mathcal K}^{BH}_{ext}\in{\mathfrak U}_{EH}^{BH} &
\hbox{GR exterior recovered}\\
\mathrm{Q4\text{-}CORR} &
\delta g^{ISP}_{ext}\ne0\hbox{ but bounded} &
\hbox{GR plus controlled finite-record corrections}\\
\mathrm{Q4\text{-}HAIR} &
\hbox{extra exterior response labels survive the quotient} &
\hbox{new exterior hair predicted}\\
\mathrm{Q4\text{-}FAIL} &
\hbox{no single GR decoder fits the exterior probes} &
\hbox{black-hole exterior not GR-compatible}
\end{array}
}
$$

The theorem target is:

$$
\boxed{
\begin{gathered}
\hbox{the exterior metric descent matches GR iff the finite exterior}\\
\hbox{influence law has a unique Lorentzian Einstein-Hilbert decoder}\\
\hbox{with black-hole boundary charges }(M,J,Q,\ldots)
\hbox{ and controlled corrections.}
\end{gathered}
}
$$

This requires the following finite-record hypotheses.

$$
\boxed{
\begin{array}{c|l}
\hbox{hypothesis} & \hbox{meaning}\\
\hline
\mathrm{GM1} & \hbox{exterior probe family is declared before fitting}\\
\mathrm{GM2} & \hbox{causal response descends to one Lorentzian cone}\\
\mathrm{GM3} & \hbox{clock, redshift, orbit, and lensing records share one metric}\\
\mathrm{GM4} & \hbox{finite constraints descend to the GR constraint ledger}\\
\mathrm{GM5} & \hbox{asymptotic charges }(M,J,Q,\ldots)\hbox{ are conserved}\\
\mathrm{GM6} & \hbox{core ledger produces no unlicensed exterior low modes}\\
\mathrm{GM7} & \hbox{ringdown, absorption, and memory responses are included}\\
\mathrm{GM8} & \hbox{finite-record corrections are bounded in tested exterior regimes}
\end{array}
}
$$

Under GM1-GM8, the Q4 target is:

$$
\boxed{
D^{ext}_{GR}({\mathcal K}^{BH}_{ext})
=
g^{GR}_{BH}(M,J,Q,\ldots)
+\delta g^{ISP}_{ext},
\qquad
\|\delta g^{ISP}_{ext}\|\le\varepsilon_{GR}.
}
$$

### 17.24 Q4 Falsifier Gates

Searchable Q4 gates tag:

`V5P1-Q4-GATES-GM1-GM10`.

The Q4 exterior-GR route fails or must branch if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{GM1} &
{\mathfrak G}^{ext}_{probe}\hbox{ is chosen after seeing the desired metric} &
\hbox{posterior GR fitting}\\
\mathrm{GM2} &
\hbox{light, clock, orbit, and lensing records require different metrics} &
\hbox{no single exterior geometry}\\
\mathrm{GM3} &
\hbox{causal response is not Lorentzian outside the horizon} &
\hbox{GR exterior fails}\\
\mathrm{GM4} &
\hbox{finite constraints do not descend to GR constraints} &
\hbox{bad dynamics, not merely bad coordinates}\\
\mathrm{GM5} &
\hbox{asymptotic charges are not conserved or not readable} &
\hbox{bad black-hole exterior labels}\\
\mathrm{GM6} &
\hbox{summed core ledger creates unbounded extra exterior hair} &
\hbox{pure GR exterior fails}\\
\mathrm{GM7} &
\hbox{ringdown, absorption, or memory probes are excluded without rule} &
\hbox{incomplete exterior audit}\\
\mathrm{GM8} &
\delta g^{ISP}_{ext}\hbox{ exceeds tested GR bounds} &
\hbox{phenomenological failure}\\
\mathrm{GM9} &
\hbox{horizon regularity requires a primitive discontinuity in }\Gamma &
\hbox{finite-record horizon thesis fails}\\
\mathrm{GM10} &
{\mathcal K}^{BH}_{ext}\hbox{ cannot be generated by summing the finite core
ledger} &
\hbox{Feynman accounting gap}
\end{array}
}
$$

Passing GM1-GM8 gives GR-compatible exterior descent.  Passing GM9-GM10 keeps
that descent aligned with the finite-record black-hole ontology rather than
turning it into a metric-first insertion.

### 17.25 Q4 Verdict For Paper 1

Paper 1 does not yet prove that the physical finite black-hole packet lands in
Q4-GR.  It does settle what Q4 must mean:

$$
\boxed{
\hbox{the exterior black-hole metric matches GR exactly when all licensed
exterior finite-record probes share one controlled GR decoder.}
}
$$

The next packet must therefore print:

$$
\boxed{
({\mathfrak G}^{ext}_{probe},
{\mathcal G}^{E}_{ext},
{\mathcal K}^{BH}_{ext},
D^{ext}_{GR},
g^{eff}_{ext},
(M,J,Q,\ldots),
\delta g^{ISP}_{ext},
\varepsilon_{GR}).
}
$$

That is the Einstein-Feynman synthesis for Q4:

$$
\boxed{
\hbox{Einstein supplies the invariant exterior geometry; Feynman supplies the
summed core influence law that must decode to it.}
}
$$

### 17.26 Q5: Core Regularity And GR Descent Failure

Q5 asks:

$$
\boxed{
\hbox{does the core avoid infinite curvature by descent failure?}
}
$$

This should not be read as:

$$
\boxed{
\hbox{can one assign a smooth GR metric to }r=0?
}
$$

That question already assumes the wrong primitive ontology.  The ISP question
is:

$$
\boxed{
\hbox{does the finite core transition law remain regular while the smooth GR
decoder becomes undefined, nonunique, or divergent?}
}
$$

Searchable Q5 audit tag:

`V5P1-Q5-FINITE-CORE-DESCENT-FAILURE-AUDIT`.

Let the finite core packet be:

$$
\boxed{
{\mathcal C}_{core}^{BH}
=
({\mathcal C}_{core},
\Gamma_{in\to core},
\Gamma_{core\to out},
\mu_{core},
{\mathfrak M}_{core},
D^{core}_{GR}).
}
$$

Here \({\mathfrak M}_{core}\) is the family of licensed finite core readouts,
and \(D^{core}_{GR}\) is the attempted smooth GR decoder applied beyond the
region where the exterior GR descent is already licensed.

Q5 is therefore the comparison:

$$
\boxed{
\Gamma_{core}\hbox{ regular}
\quad\hbox{versus}\quad
D^{core}_{GR}\hbox{ singular or undefined}.
}
$$

### 17.27 Q5 Einstein Route: Invariants Before Continuation

The Einstein move is to separate invariant physics from a bad continuation of
the metric.

Define the finite core operational package:

$$
\boxed{
{\mathcal G}^{E}_{core}
=
({\mathcal T}_{infall},
{\mathcal C}_{causal}^{core},
{\mathcal R}_{tidal}^{core},
{\mathcal Q}_{match}^{ext},
{\mathcal A}_{access}^{core}).
}
$$

The entries are:

$$
\boxed{
\begin{array}{c|l}
\hbox{symbol} & \hbox{meaning}\\
\hline
{\mathcal T}_{infall} & \hbox{finite infalling clock and ordering records}\\
{\mathcal C}_{causal}^{core} & \hbox{finite causal/accessibility relation in
the core packet}\\
{\mathcal R}_{tidal}^{core} & \hbox{licensed finite tidal or relative-motion
readouts}\\
{\mathcal Q}_{match}^{ext} & \hbox{matching data to the exterior GR decoder}\\
{\mathcal A}_{access}^{core} & \hbox{which core records can influence future
exterior records}
\end{array}
}
$$

The finite core is regular if:

$$
\boxed{
\begin{array}{ll}
\mathrm{CR1}:&{\mathcal C}_{core}\hbox{ is finite or projectively compact}\\
\mathrm{CR2}:&\Gamma_{in\to core}\hbox{ and }\Gamma_{core\to out}
\hbox{ are positive, normalized finite kernels}\\
\mathrm{CR3}:&\mathbb E_\Gamma[M]\hbox{ is finite for every }
M\in{\mathfrak M}_{core}\\
\mathrm{CR4}:&\hbox{composition with exterior channels is well-defined}\\
\mathrm{CR5}:&\hbox{the exterior GR match is maintained where Q4 licenses it}
\end{array}
}
$$

The GR decoder fails if a refinement family \(c_a\in{\mathcal C}_{core}\)
has:

$$
\boxed{
D^{core}_{GR}(c_a)
=
(g_a,R_a,\nabla R_a,\ldots)
}
$$

with at least one of:

$$
\boxed{
\begin{array}{ll}
\mathrm{DF\text{-}C1}:&\|R_a\|\to\infty\\
\mathrm{DF\text{-}C2}:&g_a\hbox{ has no projectively stable smooth limit}\\
\mathrm{DF\text{-}C3}:&\hbox{geodesic reconstruction becomes incomplete}\\
\mathrm{DF\text{-}C4}:&\hbox{causal reconstruction loses a Lorentzian decoder}\\
\mathrm{DF\text{-}C5}:&\hbox{different core probes demand incompatible metrics}
\end{array}
}
$$

The Einstein answer to Q5 is:

$$
\boxed{
\hbox{the singularity is resolved when the invariant finite core package
remains regular and only the smooth GR continuation fails.}
}
$$

This is not coordinate evasion.  It is an ontology statement: if the primitive
finite records and kernels remain defined, an infinite curvature scalar in an
overextended decoder is not a primitive physical infinity.

### 17.28 Q5 Feynman Route: The Core Alternative Ledger

The Feynman move is to write the core as a complete finite ledger and ask
whether any actual transition probability becomes ill-defined.

For exterior input \(e_{in}\) and output \(e_{out}\), define the full
in-core/out ledger:

$$
\boxed{
{\mathcal K}^{core}_{out}(e_{out}\mid e_{in})
=
\sum_{\eta\in\Gamma_{core}}
\Gamma_{out}(e_{out}\mid \eta)
\mu_{core}(\eta)
\Gamma_{in}(\eta\mid e_{in}).
}
$$

Here \(\eta\) is a finite core history, not a point in a continuum manifold.
The core is Feynman-regular if:

$$
\boxed{
\begin{array}{ll}
\mathrm{FR1}:&0\le{\mathcal K}^{core}_{out}(e_{out}\mid e_{in})\le1\\
\mathrm{FR2}:&\sum_{e_{out}}{\mathcal K}^{core}_{out}(e_{out}\mid e_{in})=1
\hbox{ or has a declared subchannel loss}\\
\mathrm{FR3}:&\sum_{\eta\in\Gamma_{core}}\mu_{core}(\eta)<\infty\\
\mathrm{FR4}:&\hbox{all licensed readout moments are finite}\\
\mathrm{FR5}:&\hbox{no infinite value is hidden inside }\mu_{core},
\Gamma_{in},\hbox{ or }\Gamma_{out}
\end{array}
}
$$

The ledger can then be finite even when the GR curvature decoder diverges:

$$
\boxed{
{\mathcal K}^{core}_{out}\hbox{ finite}
\quad\hbox{and}\quad
\|R[D^{core}_{GR}(c_a)]\|\to\infty.
}
$$

That is the Feynman answer to Q5:

$$
\boxed{
\hbox{the core is nonsingular in ISP if the complete alternative ledger is
finite, normalized, and readout-regular.}
}
$$

The real accounting danger is not failure to smooth \(r=0\).  It is any hidden
infinite measure, undefined transition, or unlicensed termination inside the
core ledger.

### 17.29 Q5 Outcome Classification

Q5 has five possible statuses.

$$
\boxed{
\begin{array}{c|l|l}
\hbox{status} & \hbox{condition} & \hbox{meaning}\\
\hline
\mathrm{Q5\text{-}REG} &
\Gamma_{core}\hbox{ regular and }D^{core}_{GR}\hbox{ fails} &
\hbox{singularity resolved as descent failure}\\
\mathrm{Q5\text{-}BOUNCE} &
\Gamma_{core}\hbox{ maps to a new exterior or branch} &
\hbox{finite transition beyond classical interior}\\
\mathrm{Q5\text{-}REM} &
\Gamma_{core}\hbox{ leaves a long-lived finite hidden sector} &
\hbox{remnant-like finite record core}\\
\mathrm{Q5\text{-}LOSS} &
\Gamma_{core}\hbox{ declares true finite record erasure} &
\hbox{primitive loss, not mere hiding}\\
\mathrm{Q5\text{-}FAIL} &
\Gamma_{core}\hbox{ itself requires an infinite or undefined primitive} &
\hbox{ISP core singularity}
\end{array}
}
$$

The preferred ISP resolution is \(Q5\text{-}REG\).  But Paper 1 should not
assume it.  It should make clear what packet would decide among the five
statuses.

### 17.30 Q5 Resolution Theorem Target

The theorem target is:

$$
\boxed{
\begin{gathered}
\hbox{the black-hole singularity is resolved in ISP iff the finite core}\\
\hbox{packet is regular while every singular behavior belongs to the failed}\\
\hbox{smooth GR descent }D^{core}_{GR}.
\end{gathered}
}
$$

More explicitly:

$$
\boxed{
\mathrm{Q5\text{-}REG}
\quad\Longleftrightarrow\quad
(\mathrm{CR1\text{-}CR5})
\wedge
(\mathrm{FR1\text{-}FR5})
\wedge
(\mathrm{DF\text{-}C1}\vee\cdots\vee\mathrm{DF\text{-}C5}).
}
$$

This means:

$$
\boxed{
\hbox{finite core regularity}
\ne
\hbox{smooth metric regularity}.
}
$$

The former is primitive in ISP.  The latter is an effective decoder condition.

### 17.31 Q5 Falsifier Gates

Searchable Q5 gates tag:

`V5P1-Q5-GATES-CR1-CR10`.

The Q5 finite-core resolution route fails or must branch if:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{gate} & \hbox{failure} & \hbox{meaning}\\
\hline
\mathrm{CR1} &
{\mathcal C}_{core}\hbox{ hides an infinite continuum state space without
compactness} &
\hbox{not a finite ISP core}\\
\mathrm{CR2} &
\Gamma_{in\to core}\hbox{ or }\Gamma_{core\to out}\hbox{ is undefined} &
\hbox{primitive singular transition}\\
\mathrm{CR3} &
\hbox{kernel positivity or normalization fails without declared loss} &
\hbox{bad finite law}\\
\mathrm{CR4} &
\sum_{\eta}\mu_{core}(\eta)=\infty &
\hbox{divergent core ledger}\\
\mathrm{CR5} &
\hbox{licensed finite readout moments diverge} &
\hbox{actual core singularity}\\
\mathrm{CR6} &
\hbox{exterior GR matching fails outside the intended core regime} &
\hbox{not a black-hole exterior resolution}\\
\mathrm{CR7} &
\hbox{GR descent is abandoned before it actually fails} &
\hbox{premature ontology switch}\\
\mathrm{CR8} &
\hbox{true record loss is relabeled as hidden information} &
\hbox{Q5-LOSS/Q5-REM confusion}\\
\mathrm{CR9} &
\hbox{core branch or bounce lacks a declared exterior channel} &
\hbox{unclosed continuation}\\
\mathrm{CR10} &
\hbox{curvature blow-up occurs while all finite and GR descent data stay
regular} &
\hbox{descent-failure reading falsified}
\end{array}
}
$$

Passing CR1-CR7 gives a finite regular core with controlled GR-domain exit.
Passing CR8-CR9 keeps the information status honest.  Passing CR10 is the hard
test of the central claim: the singularity must really be a decoder failure,
not a primitive finite-record infinity.

### 17.32 Q5 Verdict For Paper 1

Paper 1 does not yet prove that the physical black-hole packet lands in
Q5-REG.  It does settle what singularity resolution means in ISP:

$$
\boxed{
\hbox{the core avoids infinite curvature when the finite core ledger remains
regular and the curvature blow-up belongs only to the failed GR decoder.}
}
$$

The next packet must therefore print:

$$
\boxed{
({\mathcal C}_{core},
\Gamma_{in\to core},
\Gamma_{core\to out},
\mu_{core},
{\mathfrak M}_{core},
{\mathcal K}^{core}_{out},
D^{core}_{GR},
\mathrm{CR/FR/DF\text{-}C\ statuses}).
}
$$

That is the Einstein-Feynman synthesis for Q5:

$$
\boxed{
\hbox{Einstein supplies the invariant finite core criteria; Feynman supplies
the complete core alternative ledger.}
}
$$

Searchable next-packet tag:

`V5P1-BH-RECORD-PACKET-NEXT`.

## 18. Final Paper-1 Verdict

The V5 starting point is:

$$
\boxed{
\hbox{black holes are not primitive metric singularities in ISP.}
}
$$

They are:

$$
\boxed{
\hbox{finite record horizons: exterior many-to-one compression structures
whose smooth exterior descent can reproduce GR.}
}
$$

The horizon is not a discontinuity.  The singularity is not a primitive point.
The information problem is not first a clash between Hilbert-space unitarity
and thermal radiation.  It is a finite-channel question:

$$
\boxed{
\hbox{what does the full record law preserve that the exterior marginal
temporarily or permanently forgets?}
}
$$

For Q1, Paper 1 already fixes the audit target:

$$
\boxed{
\hbox{exterior-indistinguishable classes are kernels of the complete
full-to-exterior influence map.}
}
$$

For Q2, Paper 1 fixes the area-law target:

$$
\boxed{
\hbox{black-hole entropy is area-extensive when exterior influence factors
through a local finite horizon screen.}
}
$$

For Q3, Paper 1 fixes the evaporation target:

$$
\boxed{
\hbox{late radiation recovers information exactly when it refines the early
exterior quotient down to the full-law kernel.}
}
$$

For Q4, Paper 1 fixes the exterior-GR target:

$$
\boxed{
\hbox{the black-hole exterior matches GR exactly when all licensed exterior
probes share one controlled Lorentzian GR decoder.}
}
$$

For Q5, Paper 1 fixes the core-regularity target:

$$
\boxed{
\hbox{the singularity is resolved when the finite core ledger remains regular
and only the smooth GR decoder fails.}
}
$$

The next real V5 work is therefore not to draw a new Penrose diagram.  It is to
print \({\mathcal B}_{BH}\): a finite record packet whose exterior descent
matches the GR black-hole exterior while its core remains a regular finite ISP
process.

## 19. Closure Packet: The Finite Black-Hole Record Law

The missing object advertised above is now fixed as the black-hole record
packet:

$$
\boxed{
{\mathcal B}_{BH}
=
(
{\mathcal R}_{full},
{\mathcal R}_{ext},
{\mathcal R}_{hor},
{\mathcal R}_{core},
\Pi_{ext},
\Pi_{hor},
{\mathcal I}_{core\to ext},
{\mathcal D}_{GR}^{ext},
{\mathcal E}_{evap}
).
}
$$

The entries mean:

$$
\boxed{
\begin{array}{c|l}
\hbox{entry} & \hbox{meaning}\\
\hline
{\mathcal R}_{full} & \hbox{finite full-law record algebra}\\
{\mathcal R}_{ext} & \hbox{finite exterior record algebra}\\
{\mathcal R}_{hor} & \hbox{finite horizon-screen record algebra}\\
{\mathcal R}_{core} & \hbox{finite core record algebra}\\
\Pi_{ext} & \hbox{full-to-exterior quotient map}\\
\Pi_{hor} & \hbox{exterior-to-horizon compression map}\\
{\mathcal I}_{core\to ext} & \hbox{finite core influence kernel}\\
{\mathcal D}_{GR}^{ext} & \hbox{controlled exterior GR decoder}\\
{\mathcal E}_{evap} & \hbox{finite evaporation channel family}
\end{array}
}
$$

### Lemma 19.1: Exterior Indistinguishability Is A Kernel

Two full histories are exterior-identical exactly when they lie in the same
kernel class of the full-to-exterior quotient:

$$
\boxed{
x\sim_{ext}y
\quad
\Longleftrightarrow
\quad
\Pi_{ext}(x)=\Pi_{ext}(y).
}
$$

Proof.  The exterior observer has access only to records in
\({\mathcal R}_{ext}\).  Every such record is obtained by applying the quotient
\(\Pi_{ext}\) to the full record law.  If the quotients agree, every exterior
query has the same value.  If a query differs, that query is an exterior record
that separates the two quotient values.  Thus exterior indistinguishability is
precisely the kernel relation of \(\Pi_{ext}\).

$$
\square
$$

### Lemma 19.2: The Horizon Is A Screen Quotient, Not A Point Discontinuity

The finite horizon is the minimal exterior separating screen:

$$
\boxed{
{\mathcal R}_{hor}
=
\Pi_{hor}({\mathcal R}_{ext})
}
$$

with the property that every future exterior influence of the core factors
through it:

$$
\boxed{
{\mathcal I}_{core\to ext}
=
{\mathcal I}_{hor\to ext}\circ\Pi_{hor}.
}
$$

Proof.  A finite record horizon is defined by causal accessibility, not by a
coordinate singularity.  The only records relevant to an exterior observer are
those that can influence exterior future records.  The quotient
\(\Pi_{hor}\) collects exactly those boundary-compatible exterior records
through which core influence can pass.  Since the factorization is finite and
record-valued, no literal point discontinuity is introduced.

$$
\square
$$

### Lemma 19.3: Area Scaling Is The Local Screen Counting Law

If the horizon screen has uniformly bounded local record capacity per
Planck-scale cell and exterior influence factors through local screen cells,
then the exterior entropy is area-extensive:

$$
\boxed{
S_{ext}
=
\alpha A_{\mathcal H}
+ o(A_{\mathcal H}).
}
$$

Proof.  The factorization in Lemma 19.2 turns exterior distinguishability into
a screen counting problem.  Local finite capacity gives a uniform upper bound
proportional to the number of screen cells.  The existence of independent
cofinal screen cells gives the matching lower bound up to boundary and
curvature corrections.  The number of cells is proportional to the horizon
area.  Therefore the exterior entropy is area-extensive.

$$
\square
$$

### Lemma 19.4: Evaporation Is Quotient Refinement

Late radiation recovers information exactly to the extent that the evaporation
channel refines the exterior quotient:

$$
\boxed{
\ker(\Pi_{ext}^{early})
\supseteq
\ker(\Pi_{ext}^{late}).
}
$$

Full recovery occurs when:

$$
\boxed{
\ker(\Pi_{ext}^{late})
=
\ker(\Pi_{full}).
}
$$

Proof.  Early exterior radiation records generally identify only a coarse
quotient class of the full law.  Each later radiation record adds a finite
constraint.  Adding constraints can only refine the exterior kernel.  If the
late kernel equals the full-law kernel, no full-law distinction remains hidden
from the exterior record history.  If the inclusion is strict, the information
loss is exactly the residual quotient.

$$
\square
$$

### Lemma 19.5: Exterior GR Is A Decoder Theorem

The exterior matches GR exactly when all licensed exterior probes share one
controlled Lorentzian decoder:

$$
\boxed{
{\mathcal D}_{GR}^{ext}
:
{\mathcal R}_{ext}
\longrightarrow
(M,g,T)
}
$$

and the decoded fields satisfy the GR field equations on the exterior domain
within the record resolution of the packet.

Proof.  Paper 25 established that effective GR is a finite readout and
transport reconstruction when the equivalence, source, and metric gates are
passed.  The black-hole exterior packet is a restricted exterior instance of
that reconstruction.  If all exterior probes agree on one decoder, then the
exterior has a single Lorentzian geometry.  If no such decoder exists, the
failure is an exterior record discrepancy, not a hidden point object.

$$
\square
$$

### Lemma 19.6: The Core Is Regular When The Full Law Remains Finite

The black-hole core is regular in the ISP sense when:

$$
\boxed{
{\mathcal R}_{core}
\hbox{ is finite, positive, and dynamically extendible.}
}
$$

The GR singularity is then a decoder failure:

$$
\boxed{
{\mathcal D}_{GR}^{ext}
\hbox{ cannot be extended smoothly through the core quotient.}
}
$$

Proof.  A singularity in the GR descent means that a smooth Lorentzian
manifold decoder has reached the boundary of its domain.  It does not imply
that the underlying finite stochastic record law has a point where it becomes
undefined.  If the core algebra and transition law remain finite and
extendible, the primitive law is regular and only the GR decoder fails.

$$
\square
$$

### Theorem 19.7: Paper 1 Closure

The packet \({\mathcal B}_{BH}\) closes Q1-Q5:

$$
\boxed{
\begin{array}{c|c}
\hbox{question} & \hbox{closed answer}\\
\hline
\mathrm{Q1} & \hbox{exterior classes are quotient kernels}\\
\mathrm{Q2} & \hbox{entropy is local horizon-screen counting}\\
\mathrm{Q3} & \hbox{evaporation is quotient refinement}\\
\mathrm{Q4} & \hbox{exterior GR is a controlled decoder}\\
\mathrm{Q5} & \hbox{core regularity is finite-law extendibility}
\end{array}
}
$$

Proof.  Lemma 19.1 closes Q1.  Lemmas 19.2 and 19.3 close Q2.  Lemma 19.4
closes Q3.  Lemma 19.5 closes Q4.  Lemma 19.6 closes Q5.  Together these
prove that a black hole in this ontology is a finite quotient-and-screen
structure, not a primitive point discontinuity.

$$
\square
$$
