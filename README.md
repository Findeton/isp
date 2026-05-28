# Relativistic ISP: An Indivisible Stochastic Geometry

Author: Felix Robles Elvira

This repository contains a developing research corpus on **Relativistic
Indivisible Stochastic Processes** (ISP): an indivisible stochastic geometry
and probability-first attempt to
reconstruct quantum, relativistic, gauge, and gravitational structure from
finite stochastic transports between hypersurface records.

The central thesis is:

> Quantum phase is not a primitive add-on to probability.  It is the geometric
> curvature, or exchange defect, of real stochastic transports across
> incompatible Cauchy hypersurfaces.

Put more simply: the framework asks whether quantum interference can be
understood as the holonomy of probability transport itself.

## The Core Idea

Standard quantum theory begins with complex amplitudes.  A state has the form

```math
\psi = r e^{i\theta},
```

and the phase \(e^{i\theta}\) is part of the primitive formalism.  Probabilities
are recovered later by the Born rule:

```math
P = |\psi|^2.
```

ISP reverses the question.  It asks:

> What if the bottom layer contains only real stochastic data: finite records,
> probability distributions, and stochastic kernels?

In the relativistic setting there is no preferred global clock.  A physical
state is represented on a Cauchy hypersurface, and evolution is represented by
transport from one hypersurface to another.  Since local regions can be
advanced in different orders, one must compare finite localized deformations:

```text
advance region A, then region B
```

against

```text
advance region B, then region A.
```

In a flat classical Markov picture these two procedures would agree whenever
the regions are spacelike separated.  In the ISP picture, the finite stochastic
comparison maps need not commute.  The mismatch is the **exchange defect**.

That defect is the central geometric object.

## Exchange Defect As Stochastic Curvature

In differential geometry, curvature can be detected by parallel transporting a
vector around a small loop.  If the vector comes back rotated, the loop has
holonomy; the holonomy measures curvature.

ISP applies the same idea to probability transport.

The objects being transported are not vectors in a primitive Hilbert space.
They are finite probability records and stochastic kernels.  But the same
logic appears:

1. Start with a finite record distribution on a hypersurface.
2. Apply one localized stochastic deformation.
3. Apply another localized stochastic deformation.
4. Reverse the order.
5. Compare the two resulting transports.

If the two orders disagree, the stochastic transport has curvature.

The thesis is that the complex phase behavior of quantum mechanics is the
effective shadow of this stochastic curvature.  Interference is not inserted
as a mysterious complex rule at the beginning.  It is recovered as the
observable effect of noncommuting finite probability transports.

In slogan form:

```text
quantum phase = stochastic holonomy
```

or:

```text
quantum mechanics = stochastic geometry plus finite-record descent
```

## Why This Is Not Just Classical Probability

ISP is not saying that quantum theory is an ordinary hidden-variable Markov
process.  A basic Markov process has a single update order, or a commuting
family of updates, and therefore has no exchange curvature.

The nonclassical structure enters through three ingredients:

- **indivisible process level:** the transition kernel is fundamental, not
  decomposed into independent microscopic jumps;
- **hypersurface dependence:** different Cauchy slices and local deformations
  are compared rather than reduced to one global time;
- **exchange defect:** incompatible local transports leave a measurable
  finite mismatch.

The complex Hilbert-space formalism is then treated as an effective
representation of this finite stochastic geometry, not as the primitive
ontology.

## Barandes Alignment

The corpus is written to stay aligned with the Barandes-style finite stochastic
ontology:

- actual finite records come first;
- stochastic maps between records are primitive;
- Hilbert-space, QFT, gauge, and continuum objects are reconstructed or
  represented as effective descriptions;
- non-Markovianity is allowed at the level of whole process kernels;
- continuum fields are not assumed as primitive objects when a finite-record
  descent statement is intended.

This matters because many papers distinguish sharply between:

- a finite ISP theorem;
- a conditional continuum descent theorem;
- an external calibration against known GR/QFT/Yang-Mills data;
- a no-go result showing that a proposed reconstruction is underdetermined.

The guiding discipline is: do not silently import the structure the theory is
trying to explain.

## How To Read The Corpus

The papers live mostly in `physics/`.  There are four broad generations.

## V1: Finite Exchange-Defect Foundations

V1 is the original finite benchmark arc.  It develops the core machinery before
the explicit V2/V3/V4 naming becomes dominant.

Main role:

- introduce localized finite deformations;
- define stochastic comparison maps;
- compute exchange defects in exact finite models;
- show how a noncommuting stochastic transport can produce curvature-like
  structure;
- build first gauge, Fock, detector, causality, and interacting benchmarks.

Main Markdown sequence:

- `relativistic-isp-v1-paper0-relativity-indivisible-rewrite.md`
- `relativistic-isp-v1-paper1-collar-excision-exchange-defect.md`
- `relativistic-isp-v1-paper2-exact-localized-finite-deformations-free-dirac-exchange-defect.md`
- `relativistic-isp-v1-paper3-general-supports-higher-coefficients-bond-centered-thin-slab-law.md`
- `relativistic-isp-v1-paper4-universality-regulator-stability-bond-centered-thin-slab-law.md`
- `relativistic-isp-v1-paper5-higher-coefficients-strip-moment-closure-bond-centered-thin-slab-law.md`
- `relativistic-isp-v1-paper6-broader-regulator-stability-across-support-prototypes.md`
- `relativistic-isp-v1-paper7-explicit-higher-coefficients-first-nontrivial-singleton-strip-moments.md`
- `relativistic-isp-v1-paper8-explicit-regulator-comparison-first-non-leading-singleton-order.md`
- `relativistic-isp-v1-paper9-variable-particle-number-fock-space-lift-sector-changing-dynamics.md`
- `relativistic-isp-v1-paper10-minimal-u1-gauge-coupling-holonomy.md`
- `relativistic-isp-v1-paper11-dynamical-abelian-gauge-field-gauss-law-sectors.md`
- `relativistic-isp-v1-paper12-localized-controls-detectors-operational-relativity.md`
- `relativistic-isp-v1-paper13-einstein-causality-bridge-exchange-defect-haag-kastler.md`
- `relativistic-isp-v1-paper14-boundary-flux-resolved-einstein-causality.md`
- `relativistic-isp-v1-paper15-minimal-interacting-gauge-matter-benchmark.md`
- `relativistic-isp-v1-paper16-truncated-u1-gauge-matter-benchmark.md`
- `relativistic-isp-v1-paper17-theorem-level-scope-synthesis-limits.md`

Additional HTML-era companions were also converted as
`relativistic-isp-v1-paper18` through `relativistic-isp-v1-paper22`.

Conceptual status:

V1 establishes that the exchange-defect idea is not merely verbal.  It can be
implemented in exact finite stochastic systems.  But V1 is still mainly a
finite benchmark program; it does not yet supply full continuum relativistic
QFT or gravity.

## V2: Continuum Viability And Projective Hypersurfaces

V2 asks whether the finite exchange-defect machinery survives refinement.

Main question:

> Can finite stochastic kernel dynamics reproduce foliation-independent
> relativistic evolution in a regulator-stable continuum limit?

Main role:

- promote finite exchange defects to stochastic curvature limits;
- define projective hypersurface kernels;
- control refinement, coarse-graining, and inverse maps;
- investigate operational observables;
- test free QFT matching, Lorentz covariance, and metric-data obstructions.

Core files:

- `physics/relativistic-isp-v2-paper1-free-stochastic-curvature-theorem.md`
- `physics/relativistic-isp-v2-paper2-projective-hypersurface-kernel-dynamics.md`
- `physics/relativistic-isp-v2-paper3-interacting-comparison-map-locality.md`
- `physics/relativistic-isp-v2-paper4-operational-observable-reconstruction.md`
- `physics/relativistic-isp-v2-paper5-continuum-gauge-benchmark.md`
- `physics/relativistic-isp-v2-paper6-qft-reconstruction-no-go-investigation.md`
- `physics/relativistic-isp-v2-paper7-free-qft-promotion-from-stochastic-curvature-investigation.md`
- `physics/relativistic-isp-v2-paper8-free-qft-matching-equivalence-benchmarks-investigation.md`
- `physics/relativistic-isp-v2-paper9-lorentz-covariant-free-qft-completion-investigation.md`
- `physics/relativistic-isp-v2-paper10-metric-data-from-stochastic-exchange-curvature-investigation.md`

Conceptual status:

V2 is the first major viability gate.  It separates finite algebraic success
from continuum physics.  It also identifies a major theme that returns later:
bare finite Gamma-level data are often too poor to reconstruct all continuum
geometry without enriched operational records.

## V3: QFT, Non-Abelian Gauge Theory, And Yang-Mills Source Campaigns

V3 moves from free and Abelian benchmarks toward interacting QFT,
non-Abelian gauge sectors, Wilson-loop readouts, Yang-Mills dynamics, mass
gap, confinement, and actual-source problems.

Main role:

- reconstruct QFT-like structures from enriched finite ISP data;
- build finite non-Abelian gauge sectors;
- introduce projective Peter-Weyl and Wilson-loop machinery;
- test nonperturbative Yang-Mills closure routes;
- analyze mass gap and confinement gates;
- expose where actual same-law numerical/source information is missing.

Early V3 core:

- `physics/relativistic-isp-v3-paper1-minimal-enriched-isp-data-qft-reconstruction.md`
- `physics/relativistic-isp-v3-paper2-primitive-smooth-lapse-hypersurface-kernels.md`
- `physics/relativistic-isp-v3-paper3-interacting-projective-kernel-inverse-control.md`
- `physics/relativistic-isp-v3-paper4-two-branch-interacting-stochastic-curvature.md`
- `physics/relativistic-isp-v3-paper5-wilson-standard-qft-benchmark.md`
- `physics/relativistic-isp-v3-paper6-no-wilson-detail-preserving-new-physics-branch.md`
- `physics/relativistic-isp-v3-paper7-foliation-independence-interacting-projective-kernels.md`
- `physics/relativistic-isp-v3-paper8-continuum-qft-reconstruction-no-go.md`
- `physics/relativistic-isp-v3-paper9-finite-nonabelian-gauge-sectors.md`
- `physics/relativistic-isp-v3-paper10-projective-nonabelian-gauge-continuum.md`

Yang-Mills and confinement arc:

- `physics/relativistic-isp-v3-paper11-continuum-yang-mills-nonabelian-rg-closure.md`
- `physics/relativistic-isp-v3-paper12-renormalized-unsmeared-wilson-loop-functionals.md`
- `physics/relativistic-isp-v3-paper13-nonperturbative-continuum-yang-mills-functional.md`
- `physics/relativistic-isp-v3-paper14-finite-block-yang-mills-entry-gates.md`
- `physics/relativistic-isp-v3-paper15-connected-polymer-kp-creutz-margin.md`
- `physics/relativistic-isp-v3-paper16-nonperturbative-yang-mills-closure.md`
- `physics/relativistic-isp-v3-paper17-yang-mills-mass-gap-gates.md`
- `physics/relativistic-isp-v3-paper18-confinement-area-law-isp-yang-mills.md`
- `physics/relativistic-isp-v3-paper19-actual-source-constants-confinement.md`

Actual-source campaign:

- `physics/relativistic-isp-v3-paper20-actual-heat-kernel-coefficient-loss-estimates.md`
- `physics/relativistic-isp-v3-paper21-sel2-tree-rate-source-falsification.md`
- `physics/relativistic-isp-v3-paper22-continuum-yang-mills-confinement-continuation.md`
- `physics/relativistic-isp-v3-paper23-adaptive-branch-a-source-campaign.md`
- `physics/relativistic-isp-v3-paper24-full-object-rpf-dual-certificate-campaign.md`
- `physics/relativistic-isp-v3-paper25-actual-law-screened-conditional-influence-campaign.md`
- `physics/relativistic-isp-v3-paper26-actual-law-finite-template-data-extraction.md`
- `physics/relativistic-isp-v3-paper27-actual-law-rn-mixamp-smallness-or-floor-campaign.md`
- `physics/relativistic-isp-v3-paper28-rn-mixamp-spectral-tail-campaign.md`
- `physics/relativistic-isp-v3-paper29-rn-mixamp-low-mode-value-extraction.md`
- `physics/relativistic-isp-v3-paper30-actual-law-signed-bridge-amplitude-or-floor-campaign.md`
- `physics/relativistic-isp-v3-paper31-same-law-source-response-calculus.md`
- `physics/relativistic-isp-v3-paper32-heat-bad-source-neutrality-curvature-or-floor.md`
- `physics/relativistic-isp-v3-paper33-same-law-bootstrap-of-live-scalars.md`
- `physics/relativistic-isp-v3-paper34-reflection-positive-moment-bootstrap.md`
- `physics/relativistic-isp-v3-paper35-scalar-ray-detector-theorem.md`
- `physics/relativistic-isp-v3-paper36-nongauge-ward-stein-raycut.md`
- `physics/relativistic-isp-v3-paper37-actual-scalar-field-admissibility-or-kernel-floor.md`

Conceptual status:

V3 learns that many formal gauge/QFT structures can be represented in the ISP
language, but full nonperturbative closure depends on actual same-law source
information.  It turns missing constants, margins, tails, and conditional
influence estimates into explicit falsifiable gates instead of hiding them.

## V4: Geometry, GR, Value Sources, And Effective Descent

V4 begins as an ISP-GR track and later folds the GR/QFT/Yang-Mills results
back into a finite-source and effective-descent architecture.

Main role:

- test whether metric and curvature data can be recovered from finite
  exchange-curvature records;
- distinguish bare Gamma-level information from enriched operational records;
- add geometry as a finite configuration component;
- analyze finite constraint dynamics and residual minimization;
- source actual-law packet estimates;
- build finite value-source generators;
- reconnect GR/SM calibration, operational readouts, and Barandes-aligned
  finite actual records;
- reconstruct effective GR and relativistic QFT/QCD as finite descents;
- formulate continuum Yang-Mills confinement as an ISP descent theorem.

Geometry and GR source arc:

- `physics/relativistic-isp-v4-paper1-geometric-source-coupling-or-no-go.md`
- `physics/relativistic-isp-v4-paper2-fixed-background-metric-data-from-exchange-curvature.md`
- `physics/relativistic-isp-v4-paper3-orientation-sensitive-finite-curvature-or-no-go.md`
- `physics/relativistic-isp-v4-paper4-operational-orientation-quorum-or-enriched-only-metric-diagnostic.md`
- `physics/relativistic-isp-v4-paper5-operational-curvature-compatibility-source.md`
- `physics/relativistic-isp-v4-paper6-dynamical-geometry-configuration-gate.md`
- `physics/relativistic-isp-v4-paper7-finite-constraint-dynamics-or-gr-no-go.md`
- `physics/relativistic-isp-v4-paper8-geometric-score-or-residual-bound-exhaustion.md`
- `physics/relativistic-isp-v4-paper9-residual-minimum-side-decision.md`
- `physics/relativistic-isp-v4-paper10-source-conditioned-smooth-realizability-or-floor.md`
- `physics/relativistic-isp-v4-paper11-actual-law-regular-packet-source.md`
- `physics/relativistic-isp-v4-paper12-residual-source-ward-stein-four-route-decision.md`
- `physics/relativistic-isp-v4-paper13-three-normal-switch-decision-or-floor.md`
- `physics/relativistic-isp-v4-paper14-boundary-sufficiency-or-separator.md`
- `physics/relativistic-isp-v4-paper15-concrete-actual-law-route-decision.md`
- `physics/relativistic-isp-v4-paper16-minimal-actual-law-support-calculation.md`
- `physics/relativistic-isp-v4-paper17-nontautological-grsm-support-ansatz-or-no-go.md`
- `physics/relativistic-isp-v4-paper18-support-stability-consequences-and-value-frontier.md`
- `physics/relativistic-isp-v4-paper19-finite-source-stein-engine-value-control.md`

Value-source and bridge arc:

- `physics/relativistic-isp-v4-paper20-gcr-to-grsm-value-bridge.md`
- `physics/relativistic-isp-v4-paper21-finite-source-equivalence-or-external-calibration.md`
- `physics/relativistic-isp-v4-paper22-source-completion-grid.md`
- `physics/relativistic-isp-v4-paper23-finite-generating-functional-source-values.md`
- `physics/relativistic-isp-v4-paper24-barandes-finite-effective-calibration-bridge.md`

Effective GR, QFT, QCD, and continuum YM descent:

- `physics/relativistic-isp-v4-paper25-finite-descent-reconstruction-of-effective-gr.md`
- `physics/relativistic-isp-v4-paper26-relativistic-qft-qcd-as-v4-finite-descent-extension.md`
- `physics/relativistic-isp-v4-paper27-finite-qcd-dynamics-certificate.md`
- `physics/relativistic-isp-v4-paper28-continuum-yang-mills-confinement-descent.md`

Conceptual status:

V4 is the most ambitious layer.  It does not merely add geometry labels.  It
asks which finite record laws make geometry dynamical, which admissibility
principles recover GR-like behavior, and which source ledgers are sufficient
to descend to QFT/QCD/Yang-Mills results.  Its strongest claims are explicitly
framed as ISP descent results, not as unqualified external proofs independent
of the finite-record hypotheses.

## The Whole Architecture In One Line

```text
V1: finite exchange defects
  -> V2: projective/refinement continuum viability
  -> V3: QFT, non-Abelian gauge, Yang-Mills source gates
  -> V4: geometry, GR, value-source laws, and finite-to-continuum descent
```

Or, conceptually:

```text
real stochastic kernels
  -> noncommuting localized hypersurface transports
  -> exchange defect / stochastic curvature
  -> effective quantum phase and interference
  -> gauge and QFT structures
  -> GR-compatible finite geometry
  -> QCD/Yang-Mills descent under explicit source and compactness gates
```

## Current High-Level Status

The corpus has built a large finite-record framework for recovering structures
normally written in Hilbert-space, QFT, gauge, and GR language.  Its strongest
internal statements are conditional on explicitly named finite source,
compactness, admissibility, and descent hypotheses.

The honest reading is:

- ISP has a coherent finite stochastic ontology;
- quantum phase is modeled as exchange-defect curvature rather than primitive
  complex amplitude;
- many QFT/gauge/GR structures are reconstructed as finite or effective
  descents;
- remaining external acceptance depends on formalizing the active hypotheses
  in standard mathematical language and checking that the finite source
  packets are not merely calibrated restatements of the target physics.

That is the point of the paper architecture: every generation either proves a
piece, names the missing source, or exposes the exact place where the program
would fail.
