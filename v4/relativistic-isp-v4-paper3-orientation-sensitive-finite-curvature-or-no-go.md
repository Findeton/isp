# Relativistic ISP V4 Paper 3: Orientation-Sensitive Finite Curvature Or No-Go

Author: Felix Robles Elvira

Date: 2026-05-26

Status: Completed orientation-sensitivity classification.

## Abstract

V4 Paper 2 proves that fixed-background metric reconstruction is
conditionally possible if finite exchange curvature has the local
Dirac-Schwinger first-jet form.  It also proves the current Gamma-level
obstruction:

$$
\neg\mathrm{V4P2\text{-}GAMMA\text{-}METRIC\text{-}REC}^{cur}.
$$

The obstruction is orientation loss.  Bare endpoint probabilities of the form

$$
\Gamma=|U|^2
$$

do not retain the signed cross-term data needed to reconstruct a rotated
metric component \(h^{12}\).

This paper settles the next question:

$$
\hbox{Can a finite stochastic record retain the missing orientation data
without smuggling Hilbert phase as primitive?}
$$

The answer is:

1. **No** for every passive finite record built functorially from the bare
   Gamma data.
2. **No** for signed labels, independent two-copy records, or oriented loop
   labels if they do not change the actual finite probabilities.
3. **Yes, conditionally**, for finite operational instruments whose settings
   and outcomes are ordinary recorded configurations and whose probabilities
   form an orientation quorum.
4. Such a positive result is **enriched operational metric reconstruction**,
   not bare Gamma-level reconstruction, unless the operational instruments are
   themselves derived from the finite stochastic connection.

Thus Paper 3 settles the issue.  The current Gamma-level ISP-GR route is
blocked.  The only live continuation is an explicitly enriched,
Barandes-aligned operational-instrument track:

$$
\mathrm{V4P3\text{-}OPINST\text{-}ORI\text{-}QUORUM}.
$$

## 0. Imports And Scope

### Import 0.1: Paper-2 Metric Obstruction

Paper 2 imports V2 Paper 10 and records that the current bare Gamma-level
Born-squared rule cannot reconstruct full signed fixed-background metric data
in dimension \(d\ge2\).  In particular, it cannot distinguish rotated
constant frames that have opposite \(h^{12}\) but the same Gamma-level
Born-squared data.

### Import 0.2: Operational Instruments Are Allowed Records

The earlier theorem-level synthesis distinguishes:

1. raw finite kernels;
2. operational instruments, settings, and detector outcomes;
3. induced effect/algebra layers.

Operational instruments are allowed in ISP only when their settings and
outcomes are finite recorded data.  They are not allowed to appear as hidden
wavefunctions or unrecorded phase variables.

### No-Smuggling Rule 0.3

This paper may use an operational instrument only if:

1. all settings and outcomes are finite records;
2. probabilities are part of the declared finite stochastic law;
3. no hidden Markov factorization is introduced;
4. Hilbert amplitudes or phases are not primitive ontology;
5. any use of Hilbert language is marked as an enriched representation.

## 1. The Orientation Ambiguity

### Definition 1.1: Rotated-Metric Ambiguity Pair

An ambiguity pair is a pair of fixed-background frames \(E_+\), \(E_-\) such
that their target inverse metrics satisfy

$$
h_+^{11}=h_-^{11},
\qquad
h_+^{22}=h_-^{22},
\qquad
h_+^{12}=-h_-^{12}\ne0,
$$

but the current bare Gamma-level Born-squared exchange data agree:

$$
\Gamma(E_+)=\Gamma(E_-)
$$

for the tested finite endpoint kernels, comparison maps, and Gamma-level
curvature invariants.

V2 Paper 10 supplies such an ambiguity for the present Born-squared rule.

### Definition 1.2: Orientation-Sensitive Record

A finite record invariant \({\mathcal R}\) is orientation-sensitive for the
ambiguity pair if

$$
{\mathcal R}(E_+)\ne{\mathcal R}(E_-).
$$

It is metric-useful only if the sign distinction survives the refinement and
exchange-curvature normalization used in Paper 2.

## 2. Passive Gamma-Functor No-Go

### Definition 2.1: Passive Gamma-Functor Record

A passive Gamma-functor record is any finite record, statistic, label, or
post-processing map of the form

$$
{\mathcal R}=F(\Gamma,J,E,\mathfrak C),
$$

where the inputs are only the bare Gamma-level finite kernels, comparison
maps, exchange loops, and normalized curvature data already available in
Paper 2.

### Theorem 2.2: Passive Gamma-Functor Records Cannot Recover Orientation

For the ambiguity pair \(E_+,E_-\), every passive Gamma-functor record has

$$
{\mathcal R}(E_+)={\mathcal R}(E_-).
$$

Therefore passive Gamma-functor records cannot reconstruct the signed
cross-term \(h^{12}\).

Proof.

By Definition 1.1, the bare Gamma-level data agree for \(E_+\) and \(E_-\).
Any passive Gamma-functor record is a function of exactly those data.  Equal
inputs give equal outputs.  But the target metrics have opposite \(h^{12}\).
Thus no such record can determine the signed cross term.  `square`

### Corollary 2.3: Bare Gamma-Level ISP-GR Is Blocked

The current bare Gamma-level ISP-GR metric reconstruction route is blocked:

$$
\neg\mathrm{V4P3\text{-}GAMMA\text{-}ORI\text{-}REC}^{cur}.
$$

This is not merely "not sourced."  It is a no-go for the current passive
Gamma-level information class.

## 3. Candidate Records, One By One

### Candidate A: Signed Detector Labels

Suppose the endpoint outcomes are relabeled by a sign

$$
s:C_{\Sigma_a}\to\{-1,+1\}.
$$

The signed statistic is

$$
\mathbf E_\Gamma[s].
$$

If \(s\) is only a post-processing label on the same endpoint probabilities,
then it is a passive Gamma-functor statistic.

### Proposition 3.1: Passive Signed Labels Fail

Passive signed detector labels do not recover the missing orientation.

Proof.

The expectation \(\mathbf E_\Gamma[s]\) is a function of the endpoint
probabilities and the chosen label function.  If the Gamma data agree for
\(E_+\) and \(E_-\), the signed expectation agrees as well.  `square`

### Candidate B: Independent Two-Copy Records

Let the two-copy record be the product kernel

$$
\Gamma^{(2)}:=\Gamma\otimes\Gamma.
$$

### Proposition 3.2: Independent Two-Copy Records Fail

Independent two-copy records do not recover the missing orientation.

Proof.

If \(\Gamma(E_+)=\Gamma(E_-)\), then
\(\Gamma(E_+)\otimes\Gamma(E_+)=
\Gamma(E_-)\otimes\Gamma(E_-)\).  Any statistic of independent two-copy
Gamma data is therefore equal on the ambiguity pair.  `square`

### Candidate C: Oriented Exchange-Loop Labels

Suppose each exchange loop receives an orientation label \(o\in\{-1,+1\}\),
but the finite probabilities and comparison maps are unchanged.

### Proposition 3.3: Labels Without New Probabilities Fail

Oriented exchange-loop labels do not recover metric orientation unless the
actual finite probabilities depend on the orientation label.

Proof.

If the label is only appended after the fact, every orientation statistic is
a passive post-processing of the same Gamma-level data.  Theorem 2.2 applies.
To be useful, the orientation must be part of a non-passive operational record
law whose outcome probabilities differ between \(E_+\) and \(E_-\).  `square`

### Candidate D: Finite Interference Instruments

A finite interference instrument has settings \(\theta\), outcomes \(o\), and
probabilities

$$
p(o\mid\theta;E)
$$

as part of the declared finite record law.  The outcomes are ordinary
configuration/readout records.

### Proposition 3.4: Interference Instruments Are Not Gamma-Level, But Can Be
Barandes-Aligned

A finite interference instrument can be Barandes-aligned if its settings and
outcomes are finite records and no hidden intermediate Markov process is
assumed.  However, unless its probabilities are derived from the bare Gamma
connection, it is an enriched operational layer, not Gamma-level metric
reconstruction.

Proof.

The instrument is a finite stochastic object: it assigns probabilities to
recorded outcomes.  This is compatible with the Barandes ontology of ordinary
configuration-space stochastic records.  But the probabilities
\(p(o\mid\theta;E)\) are additional operational data beyond the bare endpoint
kernel \(\Gamma=|U|^2\).  Therefore they may carry orientation information,
but that information is not recovered from bare Gamma alone.  `square`

### Candidate E: Operational Effect Kernels

An operational effect kernel is a family of finite setting/outcome maps

$$
{\mathcal I}_{\theta,o,a}
$$

inserted between preparation and readout hypersurfaces, with probabilities
recorded in the same finite experiment.

### Proposition 3.5: Effect Kernels Are The Minimal Viable Orientation Route

Operational effect kernels are the minimal viable orientation-sensitive route.
They can distinguish the ambiguity pair only if there exists a statistic
\(W(\theta,o)\) such that

$$
\sum_{\theta,o}W(\theta,o)p(o\mid\theta;E_+)
\ne
\sum_{\theta,o}W(\theta,o)p(o\mid\theta;E_-).
$$

This is a new finite operational fact, not a consequence of bare Gamma-level
endpoint probabilities.

Proof.

The displayed inequality is exactly orientation sensitivity.  If no such
statistic exists, the instrument cannot distinguish the ambiguity pair.  If it
does exist, the instrument carries the missing orientation information as
finite recorded probabilities.  Since those probabilities are not functions of
the old Gamma data, the route is operationally enriched.  `square`

## 4. Orientation Quorum

### Definition 4.1: `V4P3-OPINST-ORI-QUORUM`

Write

$$
\mathrm{V4P3\text{-}OPINST\text{-}ORI\text{-}QUORUM}
$$

if there is a finite family of operational instruments
\(\{{\mathcal I}_{\theta,o,a}\}\) and finite statistics \(W^{ij}\) such that:

1. all settings and outcomes are finite records;
2. the family is support-respecting and hypersurface-compatible;
3. it does not require hidden Markov factorization;
4. it distinguishes every rotated-metric ambiguity pair in the tested class;
5. its extracted quantities \(C^{ij}_{op}\) obey tensoriality, symmetry,
   positivity, and regulator stability;
6. in the fixed-background benchmark, \(C^{ij}_{op}\to h^{ij}\) or the
   declared inverse metric density.

### Lemma 4.2: Orientation Quorum Implies Enriched Metric Reconstruction

If `V4P3-OPINST-ORI-QUORUM` holds, then fixed-background metric data are
reconstructed at the enriched operational level.

Proof.

The quorum supplies the missing signed/cross-term data by finite recorded
probabilities.  Conditions 5 and 6 provide the metric-identification gates
from Paper 2.  The result is enriched because the operational instrument
family is part of the input data.  `square`

### Proposition 4.3: Orientation Quorum Does Not Prove Gamma-Level
Reconstruction

`V4P3-OPINST-ORI-QUORUM` does not imply
`V4P2-GAMMA-METRIC-REC`.

Proof.

The quorum uses operational instrument probabilities beyond the bare endpoint
kernel.  Gamma-level reconstruction demands that the metric be determined by
bare finite kernels, comparison maps, and exchange curvature alone.  These are
different information levels.  `square`

## 5. Finite Tomography Benchmark

This section explains why the enriched operational route is mathematically
plausible without claiming it has already been sourced.

### Definition 5.1: Finite Process Quorum

A finite process quorum is a finite list of preparations and effects whose
probabilities determine the finite process on the tested support up to the
declared gauge equivalence.

### Lemma 5.2: A Process Quorum Can Recover Orientation In An Enriched
Benchmark

In a finite-dimensional benchmark, a tomographically complete process quorum
can distinguish two unitary or channel representations that have the same
endpoint transition probabilities but different rotated metric cross terms.

Proof.

Endpoint probabilities in one configuration basis are only a subset of the
finite process data.  A tomographically complete quorum uses additional
preparations/effects or operational contexts.  By definition it determines the
finite process up to gauge.  If the two benchmark processes differ by the
orientation/cross-term data needed for \(h^{12}\), the quorum distinguishes
them.  `square`

### Corollary 5.3: This Is Enriched, Not A Bare Gamma Rescue

The finite tomography benchmark shows that orientation can be recorded by
finite probabilities.  It does not show that the old endpoint Gamma kernel
already contained that information.

## 6. Current-Corpus Status

### Proposition 6.1: The Current Corpus Does Not Print An Orientation Quorum

The current corpus does not prove `V4P3-OPINST-ORI-QUORUM`.

Proof.

The operational stack establishes finite localized controls, detector
instruments, no-signaling, and induced effect-space locality under explicit
hypotheses.  It does not print a finite instrument family whose probabilities
distinguish the V2 Paper-10 rotated-metric ambiguity pair and then pass the
metric-identification gates of Paper 2.  `square`

### Proposition 6.2: The Current Corpus Proves The Passive No-Go

The current corpus proves the passive no-go:

$$
\neg\mathrm{V4P3\text{-}PASSIVE\text{-}ORI\text{-}REC}^{cur}.
$$

Proof.

This is Theorem 2.2 plus the V2 Paper-10 ambiguity pair.  Any passive record
constructed from the current bare Gamma-level data is identical on the pair
and cannot recover the signed cross term.  `square`

## 7. Final Classification

| Candidate | Status | Reason |
| --- | --- | --- |
| Passive Gamma functions | false | same Gamma data on rotated ambiguity pair |
| Signed detector labels only | false | post-processing of same probabilities |
| Independent two-copy records | false | \(\Gamma\otimes\Gamma\) preserves ambiguity |
| Oriented labels only | false | labels without probability change carry no data |
| Finite interference instruments | conditionally viable | finite outcomes can carry orientation, but enriched |
| Operational effect kernels | conditionally viable and minimal | can define orientation quorum, but not Gamma-level |
| Enriched Dirac/principal-symbol data | viable diagnostic | recovers metric from representation input, not bare stochastic kernels |

## 8. Paper-3 Settlement

### Theorem 8.1: Orientation-Sensitive Finite Curvature Is Enriched-Only At
Current-Corpus Level

The issue opened by Paper 2 is fully settled at the current-corpus level:

1. Passive finite records built from bare Gamma-level data cannot recover the
   missing metric orientation.
2. The natural passive candidates, signed labels, independent two-copy
   records, and oriented labels, all fail.
3. Orientation-sensitive finite records are possible only as non-passive
   operational instruments or enriched representation data.
4. The current corpus does not print the needed orientation quorum.
5. Therefore the active V4 verdict is

   $$
   \mathrm{V4P3\text{-}ENRICHED\text{-}ONLY}^{cur}.
   $$

Proof.

Items 1 and 2 are Theorem 2.2 and Propositions 3.1 through 3.3.  Item 3 is
Propositions 3.4 and 3.5 plus Lemma 4.2.  Item 4 is Proposition 6.1.  Item 5
is the combination of the passive no-go with the absence of an orientation
quorum.  `square`

### Final Verdict 8.2

The ISP-GR track is not dead, but bare Gamma-level endpoint probabilities are
not enough.  The next honest route is not another passive invariant.  It is:

$$
\boxed{
\mathrm{V4P3\text{-}OPINST\text{-}ORI\text{-}QUORUM}
}
$$

as an enriched operational theorem, or else an explicit decision that
fixed-background metric reconstruction belongs to the enriched
representation layer rather than the bare stochastic connection.

