# Relativistic QFT Reconstruction And No-Go Tests For ISP

Author: Felix Robles Elvira

V2 Paper 6 investigation draft

Date: 2026-05-16

Status: theorem-framework draft with a scoped positive theorem. This document
asks whether the relativistic ISP data developed in Papers 1-5 can reconstruct
ordinary local quantum field theory, or whether the stochastic-kernel layer is
necessarily underdetermined without adding extra coherent, algebraic, or
representation data.

The current conclusion is deliberately sharp but Barandes-aligned:

1. Markovized component-shadow transition data cannot reconstruct QFT.
2. Operational detector statistics alone cannot reconstruct a unique local
   QFT net unless the detector family is tomographically and compositionally
   complete.
3. A finite epsilon-stable reconstruction theorem is available for enriched ISP
   data, and the Paper 5 open-chain gauge benchmark instantiates it at fixed
   cutoff.
4. A genuine QFT reconstruction needs additional structure: coherent
   composition, local algebra/factorization data, covariance, sector/center
   handling, and a vacuum or state-selection principle.

The scope decision for this paper is now fixed:

> Paper 6 proves no-go results for Markovized component-shadow reconstruction,
> proves finite operational reconstruction for enriched whole-process/record
> data, and gives the open-chain gauge benchmark as a fixed-cutoff positive
> example. It does not attempt continuum relativistic QFT reconstruction.

This is not a failure of the program. It is the first clean ontology test:
probabilities, records, amplitudes, and local algebras are different layers of
structure. Paper 6 must say which layers ISP can derive and which layers must
be supplied or operationally reconstructed.

## 1. Purpose

Papers 1-5 built a controlled stochastic and operational framework:

1. free stochastic-curvature benchmarks;
2. projective hypersurface-kernel dynamics;
3. interacting comparison-map locality and exchange-defect control;
4. detector instruments, operational exchange, record sectors, and
   underdetermination;
5. center-resolved gauge benchmarks with cutoff and boundary-center control.

Paper 6 asks the next question:

> Are these stochastic and operational axioms restrictive enough to select
> ordinary relativistic QFT universality classes?

There are two possible honest outcomes.

**Positive outcome.** An enriched ISP data set reconstructs a known QFT class,
for example a free scalar, free fermion, or open-chain Abelian gauge benchmark,
up to the expected equivalences.

**No-go outcome.** The stochastic/operational data are provably insufficient,
and Paper 6 identifies the missing structure precisely.

The investigation currently points to a mixed answer:

- Markovized `Gamma`-only component reconstruction fails by a simple
  coherent-composition obstruction.
- finite operational reconstruction is possible only after adding
  tomographically complete instruments and composition contexts.
- full local QFT reconstruction requires still more structure than Papers 1-5
  are allowed to export.

## 2. Barandes Alignment: Whole Processes First

The local Barandes papers put a strong constraint on Paper 6's language.
Indivisible stochastic processes are not Markov chains in disguise. The primary
objects are ordinary finite configuration spaces, ordinary probabilities, and
transition laws for whole processes or declared division events.

Therefore Paper 6 should obey the following rules.

1. **Whole-process kernels are primary.** A coherent laboratory circuit may
   have a single endpoint kernel for the entire undivided process. It need not
   factor through every intermediate component.
2. **Division events are physical structure.** A split into intermediate
   stochastic stages is legitimate only when the model declares a real division
   event, such as a stable detector record, reset, conditioning event, or other
   physical boundary condition.
3. **Hilbert-space lifts are representational.** A time-evolution operator,
   Kraus representation, dilation, or local algebra may be useful and even
   theorem-guaranteed in finite settings, but it is not the primary ontology.
4. **Schur-Hadamard gauge is real gauge.** Phases in a chosen lift are not
   automatically physical beables. Empirical phase sensitivity belongs to the
   whole stochastic process and to the measurement context, not to an isolated
   ontic phase entry.
5. **Measurement devices are subsystems.** A measurement is not an unexplained
   collapse postulate. It is an ordinary physical interaction whose final
   device configuration is a record.
6. **Existence is not uniqueness.** The stochastic-quantum theorem gives a
   broad route from finite indivisible stochastic processes to unistochastic or
   dilated quantum representations. Paper 6's harder questions are uniqueness,
   locality, covariance, and QFT promotion.
7. **Local QFT structure must be earned.** Local algebras, covariance, vacuum
   sectors, and continuum limits are not automatically present just because a
   finite ISP has a Hilbert representation.

In this alignment, Paper 6 is not trying to defeat stochastic ontology. It is
trying to identify which representational structures are fixed by finite
indivisible stochastic data and which require extra choices.

## 3. Export Ledger From Papers 1-5

Paper 6 may use the following, subject to the hypotheses and limits proved or
declared in the earlier papers.

| Source | Exported To Paper 6 | Not Exported |
| --- | --- | --- |
| Paper 1 | Free one-particle stochastic-curvature benchmark and normalized exchange-coefficient control in its scoped regime. | Full interacting QFT, multiparticle Fock reconstruction, or unique Hilbert lift. |
| Paper 2 | Projective state spaces, coarse-graining maps, naturality residuals, and refinement bookkeeping. | Lorentz covariance, physical continuum uniqueness, or a QFT representation. |
| Paper 3 | Raw comparison maps `J_R`, exchange defects `E_{R,S}`, anchored locality, inverse-control hypotheses, and exchange-corridor estimates. | Detector effects, POVMs, observable algebras, or probabilities directly from raw maps. |
| Paper 4 | Operational instruments, record sectors, finite phase-completeness tests, locality transfer conditions, no-signaling, and operational underdetermination. | Unique Hilbert-space reconstruction or unique local algebraic net. |
| Paper 5 | Center-resolved gauge-sector states, cutoff-stable local gauge statistics, gauge-compatible detector instruments, operational exchange bounds, and compact-rotor cutoff transfer or obstruction. | Full local QFT reconstruction, non-Abelian gauge theory, continuum compact `U(1)` without `K -> infinity`, or raw exchange defects as observables. |

Therefore Paper 6 must not silently assume:

1. a Hilbert space;
2. complex amplitudes;
3. a local tensor factorization;
4. a net of local `*`-algebras;
5. unitary microscopic dynamics;
6. Lorentz covariance;
7. a vacuum representation;
8. a stress-energy tensor;
9. a renormalization group fixed point;
10. equivalence to standard QFT.

Each one must be derived, added as input, or explicitly left outside scope.

## 4. Reconstruction Targets

There are several inequivalent meanings of "reconstruct QFT." Paper 6 should
not blur them.

### Tier 0: stochastic ISP reconstruction

Input:

- configuration or endpoint state spaces;
- whole-process stochastic kernels and explicitly declared division-event
  kernels;
- projective coarse-graining maps;
- comparison maps and exchange defects;
- operational detector records where available.

Output:

- projective consistency;
- controlled local statistics;
- raw and operational exchange bounds.

This is the layer Papers 1-5 already develop.

### Tier 1: operational quantum reconstruction

Input:

- preparations;
- effects;
- instruments;
- controlled composition contexts;
- tomographically complete settings;
- enough coherent phase-sensitive experiments to distinguish lifts.

Output:

- a finite-dimensional process representation, when it exists;
- states, effects, and channels up to operational equivalence;
- possibly a Hilbert-space model up to unitary or antiunitary gauge.

This is not yet relativistic QFT. It is finite or regulated operational
quantum theory.

### Tier 2: local algebra reconstruction

Input:

- operational data plus a declared or reconstructed region assignment;
- factorization or net-inclusion structure;
- locality and commutation tests;
- sector and center handling;
- compatibility under refinement.

Output:

- a net `R -> A(R)` of local algebras or a regulated approximation to one;
- state restrictions on regions;
- locality/microcausality at the algebraic level.

This is closer to algebraic QFT, but it still does not supply a continuum
relativistic representation unless covariance, spectrum, and state-selection
conditions are added.

### Tier 3: relativistic QFT reconstruction

Input:

- Tier 2 data;
- Poincare or hypersurface-deformation covariance;
- a vacuum or sector-selection principle;
- spectrum/energy positivity;
- continuum/refinement limit;
- renormalized local fields or observables;
- gauge constraints and centers where present.

Output:

- a known relativistic QFT representation or universality class;
- uniqueness up to the expected equivalences;
- local covariance and physical locality.

Paper 6 should aim for either:

1. a Tier 1 or Tier 2 conditional theorem in a finite/free/gauge benchmark; or
2. a Tier 0-to-Tier 3 no-go theorem showing exactly why stochastic ISP alone
   cannot reconstruct QFT.

## 5. Ontological Split

From first principles, four objects must be kept distinct.

**1. Records.** A record is a stable outcome in the ISP operational layer. It
is what a detector writes. Records support probabilities and irreversible
conditioning in the effective description.

**2. Stochastic kernels.** A kernel `\Gamma` maps endpoint laws to endpoint
laws. It tells us transition probabilities or pseudo-probability transport in
the chosen regulated description.

**3. Coherent amplitudes.** A unitary or path-amplitude lift carries phases.
It predicts interference under coherent composition. A `\Gamma` matrix may be
the squared modulus of such a lift, but it usually does not determine the lift.

**4. Local algebras.** A QFT net knows which operations belong to which
spacetime regions and which operations commute at spacelike separation. This
is not contained in a bare global transition matrix.

The key question is not "can stochastic probabilities imitate quantum
probabilities?" They can. The key question is:

> What additional structure is needed for those probabilities to determine
> coherent composition and local relativistic operator structure?

## 6. No-Go A: Markovized Component-Shadow Reconstruction Fails

This is the first theorem Paper 6 should formalize. It is simple, concrete,
and fatal to any claim that component-level `Gamma` shadows can be multiplied
as if they were Markov stages of an indivisible process.

### Definition 1: Markovized Gamma-only component data

Fix a finite configuration set `X`. A Gamma-only component model consists of:

1. a finite list of component labels `a`;
2. a stochastic matrix `\Gamma_a:X\to X` for each component;
3. a word category whose morphisms are finite strings
   `w=a_k\cdots a_1`;
4. the composition rule
   ```math
   \Gamma_w:=\Gamma_{a_k}\cdots\Gamma_{a_1}.
   ```

It contains no complex amplitudes, no phase labels not visible in
`\Gamma_a`, no Hilbert-space lift, and no additional coherent composition
rule.

Two component models are Gamma-equivalent if they have the same configuration
set, the same component stochastic matrices, and the same word category after
identifying components with equal stochastic shadows.

A Markovized Gamma-only reconstruction is prediction-faithful only if
Gamma-equivalent inputs always give the same reconstructed operational
predictions. This is the minimal invariance condition: a reconstruction cannot
use data that are not in its input.

**Indivisibility warning.** Definition 1 is deliberately a reconstruction
foil. It is not the ontology of an indivisible stochastic process. In
Barandes' language, an ISP assigns transition laws to whole processes or to
declared division events; it does not license composing arbitrary partial
component shadows as if the dynamics were Markovian or divisible. The theorem
below therefore refutes a Markovized Gamma-only reconstruction strategy, not
the stochastic-quantum correspondence itself.

### Theorem 1: Mach-Zehnder obstruction to Markovized component shadows

Let

```math
H={1\over \sqrt 2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
D_\phi=
\begin{pmatrix}
1&0\\
0&e^{i\phi}
\end{pmatrix}.
```

Let the stochastic shadow of a unitary `U` be

```math
\Gamma(U)_{ij}:=|U_{ij}|^2.
```

Then

```math
\Gamma(H)=
\begin{pmatrix}
1/2&1/2\\
1/2&1/2
\end{pmatrix},
\qquad
\Gamma(D_\phi)=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
```

for every phase `\phi`. Therefore all values of `\phi` have the same
component-level stochastic data.

If one composes only the stochastic shadows, then

```math
\Gamma(H)\Gamma(D_\phi)\Gamma(H)
=
\begin{pmatrix}
1/2&1/2\\
1/2&1/2
\end{pmatrix}.
```

So the Markovized Gamma-only composition rule predicts a `50/50` output after
two balanced beam splitters and an internal phase shifter.

But the coherent quantum composition is

```math
U_\phi=H D_\phi H.
```

Starting from input port `0`, the output probabilities are

```math
P_\phi(0|0)
=
\left|{1+e^{i\phi}\over 2}\right|^2
=
{1+\cos\phi\over 2}
=
\cos^2(\phi/2),
```

and

```math
P_\phi(1|0)
=
\left|{1-e^{i\phi}\over 2}\right|^2
=
{1-\cos\phi\over 2}
=
\sin^2(\phi/2).
```

Thus:

- `\phi=0` gives output port `0` with probability `1`;
- `\phi=\pi` gives output port `1` with probability `1`;
- `\phi=\pi/2` gives `50/50`.

The same one-step stochastic component data produce different coherent
composition predictions.

Therefore no Gamma-only reconstruction that composes partial component shadows
by stochastic matrix multiplication, in the sense of Definition 1, can be
prediction-faithful for the coherent two-path circuit family `H D_\phi H`.

### Proof

For every value of `\phi`, the Gamma-only component input is identical:
`\Gamma(H)` is the balanced stochastic matrix and `\Gamma(D_\phi)=I`. Hence
all phases are Gamma-equivalent. Definition 1 forces any Gamma-only
reconstruction to assign the same predictions to all `\phi`.

But the coherent quantum circuit assigns different predictions:
`P_0(0|0)=1`, while `P_\pi(0|0)=0`. Therefore a Gamma-only reconstruction
cannot reproduce the coherent predictions for both `\phi=0` and `\phi=\pi`.

This contradiction proves the theorem.

This theorem does not refute ISP. It refutes the stronger claim that the
stochastic layer, when broken into component shadows and composed as a
Markov chain, contains all of QFT. A genuine ISP reconstruction may instead
use the whole-process kernel for the entire coherent circuit, or specify
which intermediate interactions are actual division events.

### Proposition 1B: whole-process ISP kernel gives the correct circuit law

For the undivided coherent circuit, define the whole-process kernel

```math
\Gamma_{\mathrm{whole}}^\phi:=\Gamma(H D_\phi H).
```

Then

```math
\Gamma_{\mathrm{whole}}^\phi
=
\begin{pmatrix}
\cos^2(\phi/2)&\sin^2(\phi/2)\\
\sin^2(\phi/2)&\cos^2(\phi/2)
\end{pmatrix}.
```

Thus a whole-process stochastic description can encode the phase-dependent
output statistics exactly. The problem is not stochasticity. The problem is
using only the separate component shadows

```math
\Gamma(H),
\qquad
\Gamma(D_\phi),
\qquad
\Gamma(H)
```

and then multiplying them as if the intermediate stages were genuine division
events.

This is the Barandes-compatible reading of Theorem 1:

> indivisible stochastic processes may assign a transition law to the whole
> coherent process; they do not require, and generally forbid, arbitrary
> Markovian factorization through unrecorded intermediate stages.

### Definition 1C: division events and records

A division event is a declared physical event at which the model is allowed to
condition, reset, coarse-grain, or restart the stochastic description. In an
operational setting, the cleanest division event is a stable detector record:
a final configuration of a measurement device that can be conditioned on in
later predictions.

A reversible marker is not automatically a division event. A phase shifter,
ancilla coupling, or path tag counts as a division event only if the enlarged
process includes a stable record or an explicit physical boundary condition
that destroys the coherent whole-process description.

Paper 6 should therefore treat every proposed factorization

```math
\Gamma_{2\leftarrow 0}
\stackrel{?}{=}
\Gamma_{2\leftarrow 1}\Gamma_{1\leftarrow 0}
```

as an additional physical hypothesis. It is not licensed by the existence of
an intermediate time, region, component, or circuit diagram alone.

### Definition 1D: epsilon-division criterion

Fix a declared norm `\|\cdot\|_{\mathrm{op}}` on stochastic kernels between
finite endpoint spaces. A proposed intermediate event at stage `1` is an
`\epsilon_{\mathrm{div}}`-division event for the process from stage `0` to
stage `2` if the following data are supplied.

1. **Intermediate configuration data.** A finite intermediate configuration
   space `X_1` and kernels
   ```math
   \Gamma_{1\leftarrow 0}:X_0\to X_1,
   \qquad
   \Gamma_{2\leftarrow 1}:X_1\to X_2.
   ```
2. **Whole-process comparison.** A whole-process kernel
   `\Gamma_{2\leftarrow 0}:X_0\to X_2` satisfying
   ```math
   \left\|
   \Gamma_{2\leftarrow 0}
   -
   \Gamma_{2\leftarrow 1}\Gamma_{1\leftarrow 0}
   \right\|_{\mathrm{op}}
   \leq
   \epsilon_{\mathrm{div}}.
   ```
3. **Record partition or boundary condition.** If the division is selective,
   `X_1` contains a record partition
   ```math
   X_1=\bigsqcup_o X_{1,o}
   ```
   or an equivalent boundary condition specifying which event is being
   conditioned on.
4. **Outcome-floor condition.** For selective conditioning, the outcome
   probability is bounded below on the declared preparation sector:
   ```math
   \Pr(o|p)\geq q_{\min}>0.
   ```
5. **Reset/coarse-graining rule.** If the post-event description forgets
   microscopic apparatus details, the corresponding coarse-graining or reset
   map is part of the data.
6. **Stability.** The record variable is stable under the later readout
   procedure to the declared tolerance.

When `\epsilon_{\mathrm{div}}=0`, the division is exact in the declared
description. When `\epsilon_{\mathrm{div}}>0`, all downstream reconstruction
claims inherit this residual.

This criterion is deliberately operational. It does not say that every
laboratory interaction is a division event. It says what extra data are needed
before Paper 6 may replace a whole-process kernel by a product of partial
kernels.

### Interpretation

The phase shifter has no visible effect at the stochastic component level:
`\Gamma(D_\phi)=I`. Yet it controls the final interference pattern. Therefore
phase is not an optional bookkeeping convention. It is operationally real when
coherent recombination is allowed.

For ISP, the lesson is:

- if a detector record is written before recombination, interference is
  suppressed and the Gamma-level description can be sufficient;
- if the branches remain coherent, the stochastic endpoint shadow is
  insufficient when it is only a component shadow and is composed by a
  Markovized product rule;
- Paper 6 must identify where ISP stores or reconstructs coherent phase data,
  or else declare the whole-process kernel or coherent lift structure as part
  of the enriched input.

## 7. No-Go B: Phase Fibers Over A Stochastic Kernel

The Mach-Zehnder theorem uses composition. Even before composition, a single
stochastic matrix usually has many coherent lifts.

### Proposition 2: diagonal phase ambiguity

Let `U` be an `n x n` unitary matrix and let `D_1,D_2` be diagonal unitary
matrices. Define

```math
U' = D_1 U D_2.
```

Then

```math
\Gamma(U')_{ij}=|U'_{ij}|^2=|U_{ij}|^2=\Gamma(U)_{ij}.
```

Hence `\Gamma(U)` cannot determine `U` as a complex unitary matrix.

### Consequence

Some of these phases are gauge choices if they can be absorbed into basis
definitions consistently across all contexts. Others become measurable when
different components are recombined. A reconstruction theorem must therefore
distinguish:

1. phase gauge;
2. physically measurable relative phase;
3. coherent composition data;
4. detector records that destroy or preserve coherence.

Without that distinction, "QFT reconstruction" is not well-posed.

### Proposition 3: component-kernel-derived maps do not repair phase underdetermination

Let a reconstruction produce maps from a component-shadow kernel family by
algebraic operations:

```math
F(\{\Gamma_a\})
```

where `F` may use matrix products, inverses on a declared test sector,
projective maps, comparison maps `J_R`, or exchange defects `E_{R,S}`, but
does not use extra coherent lift data or the whole-process circuit kernel.

If two enriched coherent theories have the same declared component-shadow
kernel family `\{\Gamma_a\}`, then every such component-kernel-derived map is
identical for the two theories.

Consequently comparison maps and exchange defects built only from component
shadows cannot, by themselves, recover the missing Mach-Zehnder phase `\phi`.

#### Proof

Every object in the hypothesis is a function only of the declared
component-shadow kernel family and the fixed projective/test-sector
bookkeeping. Equal component-shadow kernel families therefore give equal values
for all such derived maps. In the Mach-Zehnder family, all `D_\phi` have the
same stochastic shadow, so any map built only from those shadows is independent
of `\phi`. The whole-process coherent kernel `\Gamma(H D_\phi H)` is not
independent of `\phi`. Hence the component-kernel-derived layer cannot
reconstruct the coherent phase-sensitive prediction.

#### Consequence for Papers 3-4

Paper 3's `J_R` and `E_{R,S}` are powerful locality and exchange-control
objects, but they are algebraic relative-dynamics maps. Paper 4 already
requires an operational projection before they become measurable. Paper 6 must
add one more distinction: maps built from a declared kernel family inherit the
information content of that family. If the family contains only Markovized
component shadows, the derived maps do not recover the missing whole-process
coherence. If the family contains whole-process kernels, the derived maps may
carry more information, but they still do not automatically supply a unique
Hilbert lift, local algebra, or QFT representation.

## 8. No-Go C: Local Factorization Is Not A Global Matrix Property

A QFT is not merely a transition law. It is local. It knows which observables
live in which spacetime regions.

### Definition: finite local factorization

A two-region factorization of a finite endpoint set `C` is a triple
`(A,B,\theta)`, where `A` and `B` are finite sets and
`\theta:A\times B\to C` is a bijection.

Given such a factorization, a deterministic kernel `K_f` is `A`-local when
there is a map `f_A:A\to A` such that

```math
\theta^{-1} f \theta(a,b)=(f_A(a),b).
```

It is product-local when there are maps `f_A:A\to A` and `f_B:B\to B` such
that

```math
\theta^{-1} f \theta(a,b)=(f_A(a),f_B(b)).
```

For stochastic kernels, replace deterministic maps by stochastic matrices:
`K` is product-local relative to `(A,B,\theta)` when it is conjugate by
`\theta` to `K_A\otimes K_B`, and it is `A`-local when it is conjugate to
`K_A\otimes I_B`.

This is the finite endpoint analogue of declaring a local net. The bare set
`C` is not yet two regions; it becomes two regions only after the factorization
map is supplied.

### Theorem 4: local-factorization no-go

A global stochastic kernel on a finite endpoint set does not determine its
local two-region structure. More sharply, the same global deterministic kernel
can be one-region local relative to one factorization and non-product relative
to another factorization.

#### Explicit four-state example

Let

```math
C=\{(0,0),(0,1),(1,0),(1,1)\}.
```

Use the first factorization `F` with coordinates `(a,b)` and identity
identification `\theta_F(a,b)=(a,b)`. Define the deterministic map

```math
f(a,b)=(0,b).
```

This is an `A`-local reset relative to `F`: it resets the first coordinate and
leaves the second coordinate untouched.

The associated stochastic kernel is

```math
K_f(c',c)=1_{\{c'=f(c)\}}.
```

Now use a second factorization `F'` with coordinates `(u,v)` defined by

```math
\theta_{F'}(u,v)=(u,u\oplus v).
```

where `\oplus` is addition modulo `2`. In the `F'` coordinates the same global
map becomes

```math
\theta_{F'}^{-1} f \theta_{F'}(u,v)=(0,u\oplus v).
```

The first output coordinate is constant, while the second output coordinate
depends on both input coordinates. Therefore this same map is not product-local
relative to `F'`.

#### Proof of non-product locality

If the `F'`-coordinate map were product-local, there would be maps
`g_U,g_V:\{0,1\}\to\{0,1\}` such that

```math
(0,u\oplus v)=(g_U(u),g_V(v))
```

for all `u,v`. The second coordinate would then depend only on `v`. But

```math
0\oplus v \ne 1\oplus v
```

for each `v`, so `u\oplus v` depends on `u`. Contradiction.

Thus the same deterministic stochastic kernel is local in one declared
two-region structure and nonlocal in another.

### Example 4B: two-qubit local algebra ambiguity

The same point appears in Hilbert-space language. Let

```math
\mathcal H=\mathbb C^4
```

with the standard factorization

```math
F:\mathcal H=\mathcal H_A\otimes\mathcal H_B,
\qquad
|a,b\rangle_F.
```

Let `W` be the controlled-not change-of-basis unitary

```math
W|u,v\rangle_F=|u,u\oplus v\rangle_F.
```

Use it to define a second factorization `F'` by declaring

```math
|u,v\rangle_{F'}:=W|u,v\rangle_F.
```

The local algebras in the two factorizations are therefore different:

```math
\mathcal A_A^F=B(\mathcal H_A)\otimes I_B,
\qquad
\mathcal A_A^{F'}=W\mathcal A_A^F W^\dagger,
```

and similarly for the second region.

Now consider the global unitary

```math
U=I_A\otimes R_z(\theta),
\qquad
R_z(\theta)=
\begin{pmatrix}
e^{-i\theta/2}&0\\
0&e^{i\theta/2}
\end{pmatrix}.
```

Relative to `F`, this is strictly `B`-local. Relative to `F'`, its coordinate
form is

```math
U_{F'}=W^\dagger U W
=
\exp\!\left(-{i\theta\over 2} Z_A Z_B\right).
```

For `\theta\notin \pi\mathbb Z`, this is not a product unitary
`U_A\otimes U_B`. To see this, note that its diagonal phases are

```math
(e^{-i\theta/2},e^{i\theta/2},e^{i\theta/2},e^{-i\theta/2}).
```

If this were a product diagonal unitary, the phases would obey

```math
\lambda_{00}\lambda_{11}=\lambda_{01}\lambda_{10}.
```

Here the left side is `e^{-i\theta}` and the right side is `e^{i\theta}`.
They are equal only when `e^{2i\theta}=1`, i.e. when
`\theta\in\pi\mathbb Z`.

Thus the same abstract global unitary is a local one-qubit operation in one
declared tensor factorization and an entangling two-qubit operation in another.

The local algebra is therefore not recovered from the abstract global operator
or its stochastic shadow. It is recovered only from the operator together with
the declared factorization/local-net structure.

### Theorem 4C: dimension-counting locality obstruction

Let `|A|=m`, `|B|=n`, with `m,n >= 2`, and let `N=mn`. For a fixed
factorization `C\simeq A\times B`, the space of all column-stochastic kernels
on `C` has dimension

```math
N(N-1)=mn(mn-1).
```

The product-local kernels `K_A\otimes K_B` form a subset of dimension at most

```math
m(m-1)+n(n-1),
```

and the `A`-local kernels `K_A\otimes I_B` form a subset of dimension at most

```math
m(m-1).
```

Both are proper lower-dimensional subsets of the full stochastic-kernel space.
Therefore product-locality and one-region locality are not generic properties
of a global kernel; they are extra properties relative to a chosen
factorization.

Moreover, for every `m,n >= 2`, there exist two factorizations of the same
finite set and a deterministic kernel that is `A`-local in one factorization
and not product-local in the other.

#### Proof

A column-stochastic `N x N` matrix has `N` entries in each column and one
normalization constraint per column, hence dimension `N(N-1)`.

A column-stochastic matrix on `A` has dimension `m(m-1)`, and one on `B` has
dimension `n(n-1)`. The parametrization `(K_A,K_B)\mapsto K_A\otimes K_B`
therefore has image dimension at most `m(m-1)+n(n-1)`. Since

```math
m(m-1)+n(n-1)<mn(mn-1)
```

for `m,n >= 2`, product-local kernels form a proper lower-dimensional family.
The `A`-local claim is immediate because `m(m-1)<mn(mn-1)`.

For the explicit non-invariance statement, choose distinct
`a_0,a_1\in A` and `b_0,b_1\in B`. Let `f(a,b)=(a_0,b)`, which is `A`-local
in the original factorization. Define a second factorization by a relabeling
`T:A\times B\to A\times B` of the form

```math
T(a,b)=(a,\tau_a(b)),
```

where `\tau_{a_0}` is the identity and `\tau_{a_1}` swaps `b_0` and `b_1`.
Then in the new coordinates the same global map is

```math
T^{-1} f T(a,b)=(a_0,\tau_a(b)).
```

The second coordinate depends on `a`, so the map cannot be product-local in
the new factorization. This proves that local structure is not an invariant of
the global kernel alone.

### Consequence

The bare global kernel `K_f:C\to C` does not determine:

1. the local subsystem decomposition;
2. the local algebra inclusion maps;
3. the spacelike commutation relation;
4. whether an apparent interaction is local or nonlocal relative to the
   intended spacetime regions.

The local structure must be imported from:

- projective region maps;
- detector anchoring;
- a declared lattice/hypersurface structure;
- a local circuit/lift;
- or an operational locality test family.

It cannot be read off uniquely from a bare global transition matrix.

This is the QFT version of the phase no-go. Just as `\Gamma` does not contain
coherent phase composition, a global `\Gamma` also does not contain the
spacetime localization map.

## 9. Gauge Centers As A Reconstruction Gate

Paper 5 makes the local reconstruction problem harder but cleaner. In gauge
theory, a region does not have a naive tensor factorization because boundary
Gauss constraints create centers and superselection labels.

Paper 6 must therefore treat the gauge benchmark as a gate:

1. matter-only statistics are not enough;
2. unresolved boundary centers can mimic mixtures;
3. local gauge algebras require center resolution or an explicitly chosen
   extended-Hilbert-space convention;
4. operational exchange bounds must be center-resolved;
5. continuum or growing-cutoff claims require the compact-rotor theorem or
   obstruction from Paper 5.

This is useful for reconstruction. If a proposed QFT recovery theorem ignores
centers, it is not reconstructing gauge QFT.

### Proposition 5: Paper 5 gives a regulated gauge-input gate, not QFT

Assume the Paper 5 open-chain Abelian gauge benchmark hypotheses hold at fixed
cutoff:

1. bounded charge alphabet;
2. center-resolved gauge-sector states;
3. cutoff-stable local gauge operational statistics;
4. gauge-compatible detector instruments;
5. center-resolved operational exchange bounds.

Then Paper 6 may use those data as a regulated gauge-operational net input.
It may not conclude that a continuum local gauge QFT has been reconstructed.

The missing steps are:

1. a reconstruction theorem from the center-resolved operational net to a
   local gauge algebra or equivalent Hilbert representation;
2. compatibility of that reconstruction with refinement and cutoff growth;
3. covariance or hypersurface-deformation control;
4. spectrum or energy positivity;
5. a state-selection principle, such as a vacuum or declared sector family;
6. a compact-rotor `K -> infinity` theorem where compact `U(1)` is claimed.

Thus the Paper 5 benchmark is exactly the right first positive test for Paper
6, but only at the regulated operational level.

### Definition 5B: Paper 5 reconstruction input package

For Paper 6, the Paper 5 open-chain gauge benchmark should be repackaged as
the finite reconstruction input

```math
\mathcal D_{\mathrm{gauge}}^{K,L}
=
(
\mathcal R_L,
\mathcal Z_{\partial R},
\Omega_{R,z}^{K,L},
E_{R,z}^{K,L},
\mathsf I_{R,z}^{K,L},
\Gamma_{\alpha,z}^{K,L},
\mathcal P_{L\to L'},
\mathcal C_{R,S}^{K,L},
\varepsilon_{K,L}
).
```

Here:

- `K` is the compact-rotor or electric-field cutoff;
- `L` is the finite chain length;
- `\mathcal R_L` is the finite interval/region system;
- `\mathcal Z_{\partial R}` is the boundary-center label set for each region;
- `\Omega_{R,z}^{K,L}` is the center-resolved operational state space;
- `E_{R,z}^{K,L}` is the center-resolved effect space;
- `\mathsf I_{R,z}^{K,L}` is the gauge-compatible detector-instrument family;
- `\Gamma_{\alpha,z}^{K,L}` are the sectorwise kernels or operational
  transformations;
- `\mathcal P_{L\to L'}` are refinement, restriction, or coarse-graining maps;
- `\mathcal C_{R,S}^{K,L}` are the operational exchange/corridor bounds
  inherited from Papers 3-5;
- `\varepsilon_{K,L}` is the total cutoff, leakage, refinement, and calibration
  residual budget.

This package is the first serious positive reconstruction input because it
contains exactly the data QFT locality usually hides:

1. region assignment;
2. center labels;
3. operational states and effects;
4. detector instruments;
5. refinement maps;
6. exchange/locality bounds;
7. explicit cutoff dependence.

It still does not contain a continuum QFT. It is a regulated operational gauge
net candidate.

### Paper 5-to-Paper 6 test

The first positive gauge test should be:

> Given `\mathcal D_{\mathrm{gauge}}^{K,L}` satisfying the Paper 5 hypotheses,
> reconstruct a finite center-resolved operational gauge net up to operational
> equivalence, with errors controlled by the tomography factor
> `\kappa_{K,L}\eta_{K,L}` plus the Paper 5 gauge residual budget.

Success would mean Paper 6 can reconstruct the regulated operational local
structure of the Paper 5 benchmark. It would not mean that compact continuum
`U(1)` QFT has been reconstructed.

### Definition 5C: Paper 5 tomography constants

Fix `K,L`, a finite region family `\mathcal F_L\subset\mathcal R_L`, and a
boundary-center label `z` for each tested region. Let
`X_{R,z}^{K,L}` be the finite physical center-resolved local configuration
space in the mixed site-link collar of `R`, after imposing the Gauss law and the
electric cutoff. Write

```math
V_{R,z}^{K,L}:=\ell^1(X_{R,z}^{K,L})
```

for the signed operational state space generated by that finite block. A chosen
preparation family `\{p_a\}_{a\in A_{R,z}}` and effect family
`\{e_b\}_{b\in B_{R,z}}` define the finite tomography maps

```math
P_{R,z}^{K,L}:\mathbb R^{A_{R,z}}\to V_{R,z}^{K,L},
\qquad
c\mapsto \sum_a c_a p_a,
```

and

```math
E_{R,z}^{K,L}:V_{R,z}^{K,L}\to \mathbb R^{B_{R,z}},
\qquad
v\mapsto (e_b(v))_b .
```

Define the preparation and effect frame constants by

```math
q_{R,z}^{K,L}
:=
\inf\{\|Q\|_{1\to1}:P_{R,z}^{K,L}Q=I_{V_{R,z}^{K,L}}\},
```

and

```math
\ell_{R,z}^{K,L}
:=
\inf\{\|L\|_{1\to1}:L E_{R,z}^{K,L}=I_{V_{R,z}^{K,L}}\}.
```

If no such `Q` or `L` exists, the corresponding constant is `+\infty` and the
data are not tomographically complete on that finite block. Otherwise set

```math
\kappa_{R,z}^{K,L}:=
q_{R,z}^{K,L}\ell_{R,z}^{K,L},
\qquad
\kappa_{K,L}(\mathcal F_L):=
\sup_{(R,z)\in\mathcal F_L}\kappa_{R,z}^{K,L}.
```

The canonical microscopic record frame is the point-mass/indicator frame

```math
p_x=\delta_x,
\qquad
e_x(y)=\mathbf 1_{\{x=y\}},
\qquad
x,y\in X_{R,z}^{K,L}.
```

With the `\ell^1` coordinate norm, `P=E=I`, hence

```math
q_{R,z}^{K,L}=1,
\qquad
\ell_{R,z}^{K,L}=1,
\qquad
\kappa_{R,z}^{K,L}=1.
```

This is the mathematically clean frame for the fixed-cutoff theorem. A
coarse-grained or noisy detector frame is also allowed, but only if its response
matrix is injective on the tested quotient. If the observed record channel is

```math
M_{R,z}^{K,L}:\ell^1(X_{R,z}^{K,L})\to\mathbb R^{B_{R,z}},
```

then the effect-frame constant is the left-inverse condition number

```math
\ell_{R,z}^{K,L}=\inf\{\|L\|_{1\to1}:LM_{R,z}^{K,L}=I\}.
```

Thus bad detector conditioning is not hidden. It appears explicitly as
`\kappa_{K,L}`.

### Proposition 5C.1: coarse-detector conditioning trichotomy

Let `V=\ell^1(X)` be a finite center-resolved configuration block and let

```math
M:V\to \mathbb R^B
```

be the response map of a coarse or noisy detector frame. Define the operationally
null subspace

```math
N_M:=\ker M
```

and the quotient `\overline V_M:=V/N_M` with the quotient norm. For a fixed
finite block, the first two alternatives identify the reconstructible domain.
Along a refinement family, the third alternative is the failure mode that makes
the theorem non-uniform.

1. **Microscopic or uniformly separated frame.** If `N_M=0` and there is
   `s_M>0` such that
   ```math
   \|Mv\|_1\ge s_M\|v\|_1
   \qquad
   \hbox{for all }v\in V,
   ```
   then `M` has a left inverse `L` on its image with
   ```math
   \|L\|_{1\to1}\le s_M^{-1}.
   ```
   The reconstruction theorem holds on `V`, with detector contribution
   `\ell\le s_M^{-1}`.
2. **Coarse but separating on a quotient.** If `N_M\ne0` but the induced map
   ```math
   \overline M:\overline V_M\to \operatorname{im}M
   ```
   satisfies
   ```math
   \|\overline M\overline v\|_1
   \ge
   s_M\|\overline v\|_{\overline V_M},
   ```
   then reconstruction holds only on the operational quotient
   `\overline V_M`, with `\ell\le s_M^{-1}`. Microstates inside the same
   detector fiber are not reconstructible and must not be claimed.
3. **Ill-conditioned refinement family.** If the best separation constant
   on the chosen reconstructible domain tends to zero along the tested
   refinement family, then the tomography constant diverges and Theorem 5E
   becomes non-uniform unless the theory is explicitly quotiented further or new
   detector effects are added.

In particular, if `M=I+N` on the microscopic frame and

```math
\|N\|_{1\to1}\le \epsilon<1,
```

then `M` is invertible and the Neumann bound gives

```math
\ell\le {1\over 1-\epsilon},
\qquad
\kappa\le {q\over 1-\epsilon}.
```

If `M=RC` is a noisy coarse-graining through a deterministic partition
`C:V\to\mathbb R^C`, then no reconstruction inside the fibers of `C` is
available. The correct state space is the quotient separated by `C`, followed
by the response conditioning of `R`.

Proof. On a finite-dimensional normed space, injectivity with lower separation
constant `s_M` gives a bounded inverse from `\operatorname{im}M` to the domain
with norm at most `s_M^{-1}`. If `M` has a kernel, the same argument applies to
the induced injective map on the quotient. If the lower separation constant
vanishes, every left inverse has norm at least `s_M^{-1}` on the tested
subspace, so the reconstruction error bound amplifies tomography noise without
uniform control. The Neumann estimate is the standard inverse series
`(I+N)^{-1}=\sum_{n\ge0}(-N)^n`. `square`

### Definition 5D: Paper 5 residual budget for reconstruction

For a finite region family `\mathcal F_L`, define the fixed-cutoff gauge
residual budget

```math
\varepsilon_{\mathrm{gauge}}^{K,L}(\mathcal F_L)
:=
\varepsilon_{\mathrm{ker}}
+
\varepsilon_{\mathrm{rec}}
+
\varepsilon_{\mathrm{cut}}
+
\varepsilon_{\mathrm{cent}}
+
\varepsilon_{\mathrm{G}}
+
\varepsilon_{\mathrm{loc}} .
```

Here:

1. `\varepsilon_{\mathrm{ker}}` is the primitive kernel/refinement residual;
2. `\varepsilon_{\mathrm{rec}}` is the detector record-sector residual;
3. `\varepsilon_{\mathrm{cut}}` is the electric-cutoff bad-event mass;
4. `\varepsilon_{\mathrm{cent}}` is boundary-center mismatch or unresolved
   center mixing;
5. `\varepsilon_{\mathrm{G}}` is Gauss-sector leakage;
6. `\varepsilon_{\mathrm{loc}}` is the declared operational locality or
   exchange-corridor residual on the tested region family.

For the explicit Paper 5 detector protocol, Theorem 4E gives the conservative
record bound

```math
\varepsilon_{\mathrm{rec}}
\leq
2\epsilon_R
+
\epsilon_{\mathrm{cent}}
+
2\epsilon_{\mathrm{cut}}
+
\epsilon_{\mathrm{G}}.
```

Consequently one may use the fully expanded budget

```math
\varepsilon_{\mathrm{gauge}}^{K,L}(\mathcal F_L)
\leq
\varepsilon_{\mathrm{ker}}
+
2\epsilon_R
+
3\epsilon_{\mathrm{cut}}
+
2\epsilon_{\mathrm{cent}}
+
2\epsilon_{\mathrm{G}}
+
\varepsilon_{\mathrm{loc}}.
```

In exact finite open-chain blocks with canonical microscopic readout, fixed
center, no cutoff-boundary mass on the tested support, and exact Gauss
preservation, all terms except the intentionally declared operational locality
or exchange residual vanish.

### Theorem 5E: fixed-cutoff open-chain gauge reconstruction

Assume `\mathcal D_{\mathrm{gauge}}^{K,L}` satisfies the Paper 5 fixed-cutoff
open-chain hypotheses on a finite region family `\mathcal F_L`. Assume:

1. for every `(R,z)\in\mathcal F_L`, the declared preparations span
   `V_{R,z}^{K,L}`;
2. the declared effects separate points of `V_{R,z}^{K,L}`;
3. the detector instruments include the declared division/record events or
   whole-process kernels needed for the transformations being reconstructed;
4. the frame constant
   `\kappa_{K,L}(\mathcal F_L)` of Definition 5C is finite;
5. the probability-column tomography error is bounded by
   `\eta_{K,L}(\mathcal F_L)`;
6. the Paper 5 gauge residual budget is
   `\varepsilon_{\mathrm{gauge}}^{K,L}(\mathcal F_L)`.

Then Theorem 8 applies to `\mathcal D_{\mathrm{gauge}}^{K,L}` and reconstructs
a finite center-resolved operational gauge net

```math
(R,z)\mapsto \mathcal T_{R,z}^{K,L}
```

up to operational equivalence with reconstruction residual bounded by

```math
\varepsilon_{\mathrm{rec}}^{K,L}
\leq
\kappa_{K,L}(\mathcal F_L)\eta_{K,L}(\mathcal F_L)
\;+\;
\varepsilon_{\mathrm{gauge}}^{K,L}(\mathcal F_L).
```

For the canonical microscopic record frame,
`\kappa_{K,L}(\mathcal F_L)=1`, so the bound becomes

```math
\varepsilon_{\mathrm{rec}}^{K,L}
\leq
\eta_{K,L}(\mathcal F_L)
\;+\;
\varepsilon_{\mathrm{gauge}}^{K,L}(\mathcal F_L).
```

For exact finite data, exact microscopic readout, exact center matching, exact
Gauss preservation, and no cutoff-boundary mass on the tested support, this is
an exact fixed-cutoff reconstruction theorem. For coarse-grained physical
detectors, the theorem holds only on the operational quotient separated by the
detector frame, and the condition number `\kappa_{K,L}` is part of the claim.

Proof. Definitions 5C and 5D supply exactly the data required by Theorem 8:
finite region spaces, center labels, preparation and effect frames, declared
records or whole-process transformations, and explicit residuals. Theorem 8
then gives the displayed bound. The canonical microscopic frame has `P=E=I`,
so `q=\ell=\kappa=1`. For a noisy record channel, replace `E` by its response
matrix and use the left-inverse norm in Definition 5C. `square`

### Decision 5F: status of the open-chain gauge theorem

Theorem 5E belongs in Paper 6 proper, not only in an appendix. It is the main
positive example showing that the Barandes-aligned reconstruction program is
not merely negative:

1. Markovized component shadows fail;
2. whole-process kernels plus declared records can reconstruct finite
   operational structure;
3. the Paper 5 open-chain gauge package supplies a nontrivial center-resolved
   test case.

The continuum compact-rotor and growing-volume claims should not be promoted to
Paper 6's main theorem. They remain QFT-promotion gates supplied by Paper 5:
cutoff scaling, rotor local limits, covariance, spectrum, and state selection
must still be added before anyone claims continuum compact `U(1)` QFT
reconstruction.

## 10. Conditional Positive Direction

The negative results above do not prevent reconstruction from enriched data.
They only identify what cannot be absent.

### Definition 6: enriched ISP reconstruction data

A finite regulated ISP reconstruction data set should contain:

```math
\mathcal D_{\mathrm{ISP}} =
(
C_R,
P_{R\to S},
\Omega_R,
E_R,
\Gamma_\alpha,
\mathsf I_\beta,
\mathcal C,
\mathcal L,
\mathcal Z,
\mathcal R
).
```

Here:

- `C_R` are finite or regulated configuration spaces attached to regions;
- `P_{R\to S}` are projective/coarse-graining maps;
- `\Omega_R` are state cones or state spaces;
- `E_R` are operational effects;
- `\Gamma_\alpha` are stochastic or pseudo-stochastic transition kernels;
- `\mathsf I_\beta` are detector instruments;
- `\mathcal C` is the allowed composition grammar;
- `\mathcal L` is optional coherent lift data, if supplied;
- `\mathcal Z` stores sectors, charges, and boundary centers;
- `\mathcal R` stores refinement, cutoff, and covariance maps.

The minimal enriched data needed for QFT reconstruction should be one of the
central outputs of Paper 6.

### Proposition 6B: stochastic-quantum theorem as an existence input

For finite systems, the Barandes stochastic-quantum theorem should be used
positively but carefully.

Paper 6 may use the following existence principle:

> A finite indivisible stochastic process can be represented, possibly as a
> subsystem of a larger unistochastic process or via a Hilbert-space dilation.

This means that Hilbert-space methods are available as representation tools
for finite ISP data. It does not mean that a unique Hilbert representation, a
unique tensor factorization, a local QFT net, or a continuum relativistic
theory has been reconstructed.

The theorem therefore changes Paper 6's burden. The hard question is not
whether some Hilbert representation can exist in finite settings. The hard
questions are:

1. which representation data are fixed by the stochastic process;
2. which phases are Schur-Hadamard gauge;
3. which structures are operationally identifiable;
4. which local factorization is physically declared or reconstructible;
5. whether the representation satisfies covariance, spectrum, sector, and
   continuum requirements.

### Schur-Hadamard gauge discipline

Given a chosen time-evolution lift `\Theta` of a stochastic kernel `\Gamma`,
the relation

```math
\Gamma=\overline{\Theta}\odot\Theta
```

is invariant under Schur-Hadamard rephasings

```math
\Theta_{ij}\mapsto e^{i\chi_{ij}}\Theta_{ij}.
```

This is a gauge freedom of the representation. It is not the same thing as a
physical lattice `U(1)` gauge transformation, and it is not the same thing as a
measurable relative phase in an undivided interferometer.

Paper 6 should therefore classify every phase-sensitive statement as one of
the following.

1. **Kernel-level statement.** It is expressed directly in whole-process
   stochastic kernels and is independent of the lift.
2. **Gauge-fixed representation statement.** It uses a chosen lift or dilation
   and is meaningful only after a gauge convention is fixed.
3. **Gauge-invariant representation statement.** It is unchanged under the
   allowed Schur-Hadamard rephasings.
4. **Operational phase statement.** It is tied to a declared whole-process
   experiment or to tomographically complete records, not to an isolated phase
   entry of `\Theta`.

The Mach-Zehnder correction is a kernel-level statement: the whole-process
kernel `\Gamma(H D_\phi H)` changes with `\phi`. The isolated phase gate
shadow `\Gamma(D_\phi)=I` does not carry that information by itself.

### Proposition 6C: representation existence is weaker than reconstruction

Let `\mathcal P` be a finite indivisible stochastic process. A representation
existence theorem asserts that there exists some unistochastic or dilated
Hilbert-space representation of `\mathcal P`.

A reconstruction theorem asserts more: that a specified class of structures is
determined by specified data up to a specified equivalence relation.

Therefore the following implications are invalid without extra hypotheses:

1. representation existence implies unique Hilbert lift;
2. representation existence implies unique tensor factorization;
3. representation existence implies local algebraic QFT net;
4. representation existence implies covariance or spectrum condition;
5. representation existence implies continuum limit.

Paper 6 may use Barandes' stochastic-quantum theorem for finite
representation existence. It must prove any uniqueness, locality, covariance,
or continuum claim separately.

### Theorem 7: finite operational process reconstruction, conditional form

Assume:

1. a finite-dimensional operational state space `V`;
2. a family of preparations `{p_a}` whose linear span is `V`;
3. a family of effects `{e_b}\subset V^*` that separates points of `V`;
4. a declared finite-dimensional transformation subspace
   `\mathcal T\subset \mathrm{End}(V)`;
5. probabilities
   ```math
   p(a,b,\alpha)=e_b(T_\alpha p_a)
   ```
   known for a tomographically complete set of `a,b`;
6. transformations `T_\alpha\in \mathcal T`;
7. a declared composition rule for transformations, whenever compositions are
   claimed.

Then each `T_\alpha` is uniquely determined as a linear map on `V` by the
numbers `e_b(T_\alpha p_a)`.

If the preparations span only a quotient of `V`, or the effects separate only a
quotient, then `T_\alpha` is determined only up to the corresponding
operational equivalence: two maps are equivalent when they give the same
probabilities for all declared preparations, effects, and allowed
compositions.

If, in addition, the operational theory satisfies a complex Hilbert-space
representation theorem's hypotheses and the coherent composition contexts are
included, then one may reconstruct a Hilbert representation up to the standard
unitary, antiunitary, and phase-gauge freedoms.

### Proof

Suppose `T,T'\in\mathcal T` give the same data:

```math
e_b(Tp_a)=e_b(T'p_a)
\qquad\hbox{for all }a,b.
```

Then

```math
e_b((T-T')p_a)=0
\qquad\hbox{for all }a,b.
```

Because the effects separate points of `V`, this implies
`(T-T')p_a=0` for every `a`. Because the preparations span `V`, it follows
that `T-T'=0` on all of `V`. Hence `T=T'`.

If spanning or separation holds only after quotienting by operationally null
directions, the same proof gives equality on that quotient, which is exactly
operational equivalence.

Composition adds no new linear algebra problem; it tells us which products of
the reconstructed maps are physically allowed transformations. A Hilbert lift
still requires extra representation hypotheses that are not consequences of
stochasticity alone.

### Scope warning

Theorem 7 is not a QFT reconstruction theorem. It is a finite operational
reconstruction theorem. QFT reconstruction additionally needs:

1. local net structure;
2. continuum/refinement control;
3. covariance;
4. spectrum or energy positivity;
5. sector and center resolution;
6. a vacuum or state-selection principle.

### Theorem 8: epsilon-stable finite operational ISP-net reconstruction theorem

Assume a finite regulated enriched ISP-net data set with:

1. a finite region poset `\mathcal R`;
2. center labels `z\in\mathcal Z_{\partial R}` where constraints require
   them;
3. finite-dimensional normed operational state spaces `V_{R,z}`;
4. declared restriction maps
   `\rho_{S\to R}:V_{S,z_S}\to V_{R,z_R}` for `R\subset S`;
5. declared division events, record events, or whole-process kernels specifying
   which stochastic transformations are physically legitimate;
6. for each `(R,z)`, a preparation frame
   ```math
   P_{R,z}:\mathbb R^{A_{R,z}}\to V_{R,z},
   \qquad
   c\mapsto \sum_a c_a p_a,
   ```
   which is surjective and has a chosen right inverse `Q_{R,z}` with
   `\|Q_{R,z}\|\leq q_{R,z}`;
7. for each `(R,z)`, an effect frame
   ```math
   E_{R,z}:V_{R,z}\to \mathbb R^{B_{R,z}},
   \qquad
   v\mapsto (e_b(v))_b,
   ```
   which is injective and has a chosen left inverse on its image
   `L_{R,z}` with `\|L_{R,z}\|\leq \ell_{R,z}`;
8. transformation families `T_{\alpha,R,z}` with declared anchoring region
   and composition grammar;
9. measured or specified probability columns
   ```math
   y_{\alpha,a}^{R,z}
   =
   E_{R,z}(T_{\alpha,R,z}p_a)
   +
   \delta_{\alpha,a}^{R,z},
   \qquad
   \|\delta_{\alpha,a}^{R,z}\|\leq \eta_{R,z,\alpha};
   ```
10. compatibility, division, restriction, center, and locality residuals bounded
    in the declared operational norms by `\varepsilon`.

Then the data reconstruct a finite center-resolved operational local net

```math
R\mapsto \mathcal T_{R,z}
```

up to operational equivalence. For each local transformation, define

```math
\widehat T_{\alpha,R,z}p_a
:=
L_{R,z}y_{\alpha,a}^{R,z}
```

and extend linearly by the right inverse `Q_{R,z}`:

```math
\widehat T_{\alpha,R,z}v
:=
\sum_a (Q_{R,z}v)_a \widehat T_{\alpha,R,z}p_a.
```

Then

```math
\|\widehat T_{\alpha,R,z}-T_{\alpha,R,z}\|
\leq
\kappa_{R,z}\eta_{R,z,\alpha},
\qquad
\kappa_{R,z}:=q_{R,z}\ell_{R,z}.
```

The reconstructed restriction, center-refinement, division, and locality
relations inherit the declared residuals with the additional tomography error.
For example, if

```math
\|\rho_{S\to R}T_{\alpha,S,z_S}
-T_{\alpha,R,z_R}\rho_{S\to R}\|
\leq
\varepsilon_{\mathrm{res}},
```

then

```math
\|\rho_{S\to R}\widehat T_{\alpha,S,z_S}
-\widehat T_{\alpha,R,z_R}\rho_{S\to R}\|
\leq
\varepsilon_{\mathrm{res}}
\;+\;
C_{\rho}
(\kappa_{S,z_S}\eta_{S,z_S,\alpha}
 +\kappa_{R,z_R}\eta_{R,z_R,\alpha}),
```

where `C_\rho` is the declared norm constant for the restriction maps. Analogous
triangle-inequality bounds hold for center-refinement and operational locality
relations. Division-event residuals enter additively through
`\epsilon_{\mathrm{div}}`.

If spacelike-separated regions `R,S` satisfy a declared operational locality
condition, for example commuting nonselective instruments or a Paper 3-5
exchange/corridor bound after operational projection, then the reconstructed
net inherits that locality statement in the same operational topology.

### Proof

Apply the finite tomography argument sectorwise. For each preparation `p_a`,
the effect-frame data give

```math
y_{\alpha,a}^{R,z}
=E_{R,z}(T_{\alpha,R,z}p_a)+\delta_{\alpha,a}^{R,z}.
```

Applying `L_{R,z}` yields

```math
\widehat T_{\alpha,R,z}p_a
=T_{\alpha,R,z}p_a+L_{R,z}\delta_{\alpha,a}^{R,z},
```

so

```math
\|\widehat T_{\alpha,R,z}p_a-T_{\alpha,R,z}p_a\|
\leq
\ell_{R,z}\eta_{R,z,\alpha}.
```

For any `v\in V_{R,z}`, write `c=Q_{R,z}v`, so
`v=P_{R,z}c`. By linearity,

```math
\|(\widehat T_{\alpha,R,z}-T_{\alpha,R,z})v\|
\leq
\ell_{R,z}\eta_{R,z,\alpha}\|Q_{R,z}v\|
\leq
q_{R,z}\ell_{R,z}\eta_{R,z,\alpha}\|v\|.
```

This proves the operator-norm reconstruction bound. The restriction, center,
division, and locality bounds follow by inserting
`\widehat T=T+(\widehat T-T)` into each declared compatibility relation and
using the triangle inequality with the declared norm constants.

This proves reconstruction of a finite operational local net. It does not
derive the region poset, the center labels, the division events, or the
locality relation from a bare kernel; those are part of the enriched input.

### Existence versus uniqueness

Theorem 8 should be read together with Proposition 6B.

The stochastic-quantum theorem supplies broad finite representation existence:
one can often pass to a unistochastic or dilated Hilbert representation. Theorem
8 supplies operational uniqueness only at the declared finite-net level:
transformations are fixed up to operational equivalence by the specified
preparations, effects, records, sectors, and compatibility maps.

These are different claims.

**Existence questions:**

1. Does some Hilbert or unistochastic representation exist?
2. Does some dilation realize the finite stochastic process?
3. Does some operational local net represent the declared record structure?

**Uniqueness questions:**

1. Is the Hilbert lift unique modulo Schur-Hadamard gauge?
2. Is the tensor factorization unique?
3. Is the local algebraic net unique?
4. Are covariance, spectrum, and vacuum sector fixed?
5. Are continuum limits unique?

Paper 6's positive theorem may answer finite operational uniqueness relative
to an enriched data set. It must not convert Barandes-style representation
existence into unique QFT reconstruction.

### QFT promotion gates

Theorem 8 is the first positive finite-net theorem Paper 6 can claim. It reconstructs
a finite operational ISP net from whole-process stochastic data, declared
division/record structure, locality maps, sectors, and tomography. To promote
its output to relativistic QFT, one must add and prove the following gates.

**Covariance gate.** There must be a representation or projective action of
the relevant spacetime symmetry or hypersurface-deformation category on the
net, compatible with regions, kernels, instruments, and refinement maps.
Without this, the result is a regulated local operational theory, not a
relativistic one.

**Spectrum gate.** The reconstructed dynamics must satisfy an energy-positivity
or spectrum condition. Without this, one may reconstruct local quantum
dynamics, but not the physical vacuum sector of relativistic QFT.

**Vacuum/sector gate.** A state-selection principle must identify a vacuum,
thermal sector, charge sector, or other physically meaningful representation.
Operational statistics alone can describe many inequivalent sectors.

**Continuum gate.** The reconstruction must be stable under the declared
cutoff/refinement limit. For the Paper 5 gauge benchmark this includes the
compact-rotor `K -> infinity` issue.

**Field/algebra gate.** If one claims reconstruction of a local algebraic QFT,
the finite operational transformations must converge to a net of local
`*`-algebras or an equivalent representation with microcausality.

### Finite-to-QFT promotion checklist

Before Paper 6 or any later paper claims QFT reconstruction, it must fill the
following checklist.

| Gate | Required Data | Minimal Pass Condition | Failure Meaning |
| --- | --- | --- | --- |
| Covariance | Symmetry or hypersurface-deformation action on regions, kernels, records, and restrictions. | Reconstructed nets are naturally equivalent under the declared action. | Only a regulated operational net has been reconstructed. |
| Spectrum | Generator or transfer family with positive-energy/spectrum condition. | Physical sector obeys the declared energy positivity condition. | No relativistic vacuum-sector claim. |
| Vacuum/sector | State-selection rule for vacuum, charge sector, thermal sector, or boundary-center family. | Selected sector is stable under dynamics and refinement. | Operational data remain sector-underdetermined. |
| Continuum | Cutoff/refinement maps and convergence topology. | Reconstructed finite nets converge with controlled residuals. | Fixed-regulator reconstruction only. |
| Local algebra | Candidate local `*`-algebras or equivalent operational algebras. | Inclusion, isotony, positivity, adjoint, and microcausality survive the limit. | No algebraic-QFT reconstruction. |
| Gauge centers | Center labels and Gauss-sector maps. | Boundary centers are resolved or consistently quotiented. | Gauge locality is not reconstructed. |
| Lift/gauge | Hilbert lift plus Schur-Hadamard gauge convention or gauge-invariant observables. | Physical claims are lift-gauge invariant or explicitly gauge-fixed. | Hilbert representation is only auxiliary. |

These gates are not decorative. They are precisely the difference between
"finite operational reconstruction" and "relativistic QFT reconstruction."

### Free benchmark covariance/spectrum/vacuum gate

The simplest test case for QFT promotion is not the open-chain gauge benchmark.
It is the Paper 1 free one-particle `1+1D` Dirac stochastic-curvature theorem.
That theorem already supplies a continuum-facing curvature datum, but it does
not by itself supply a relativistic QFT.

To promote the free benchmark beyond stochastic curvature, Paper 6 would need
the following additional package.

**F1. Sampling and continuum state space.** There must be a sampling family

```math
\mathsf S_a:C_c^\infty(\mathbb R,\mathbb C^2)\to V_a
```

and a reconstruction topology in which the finite operational states/effects
converge on sampled smooth spinors. Paper 1 already uses such smooth sampled
test profiles for its curvature theorem. This is the correct starting point.

**F2. Translation and hypersurface covariance.** Spatial translations, and the
restricted hypersurface-deformation operations already visible in the exchange
curvature, must act naturally on the projective family. A minimal covariance
residual is:

```math
\left\|
P_{a\leftarrow a'}\,T_{g,a'}\Gamma_{a'}
-
T_{g,a}\Gamma_a P_{a\leftarrow a'}
\right\|_{\mathrm{test}}
\le
\epsilon_{\mathrm{cov}}(a',a;g),
```

with `\epsilon_{\mathrm{cov}}\to0` for the tested symmetry/deformation family.
For the free benchmark, the first target is not full Lorentz covariance. It is
controlled covariance of the sampled tangential action
`N\partial_xM-M\partial_xN` under translations and allowed compactly supported
reparameterizations. Full boosts require a separate theorem.

**F3. Spectrum condition.** A selected Hilbert or unistochastic lift must carry
a generator of time translations whose continuum spectrum is bounded below, or
whose physical sector satisfies the usual positive-energy condition after the
appropriate field-theoretic construction. The one-particle lattice Dirac
benchmark alone does not prove this. It has a useful finite lift, but a QFT
spectrum condition belongs to a chosen representation and sector.

**F4. Vacuum/sector selection.** The free one-particle theorem has no vacuum.
At most it selects a one-particle sector. To claim free QFT reconstruction one
must add a zero-particle state, a Fock/CAR or equivalent field construction, and
a vacuum or sector-selection rule stable under refinement. Without this, Paper
6 may claim only one-particle operational reconstruction plus curvature data.

**F5. Local field/algebra net.** A QFT claim needs local algebras or equivalent
field operators:

```math
I\mapsto \mathcal A(I),
```

with isotony, adjoint/positivity structure, and microcausality in the continuum
limit. Paper 1's exchange-defect operator is evidence for the hypersurface
deformation bracket, not a construction of a Haag-Kastler net.

**F6. Continuum stability.** The covariance, spectrum, sector, and local-algebra
claims must survive the same projective/refinement limit. It is not enough that
one coefficient-level exchange-curvature limit exists.

Therefore the free benchmark can be used in Paper 6 as the first QFT-promotion
test:

```text
Paper 1 curvature datum
-> sampled one-particle operational reconstruction
-> covariance/spectrum/sector/local-algebra gates
-> possible free-QFT reconstruction
```

Current status: Paper 1 supplies the first arrow. Paper 6 does not yet supply
the remaining arrows.

### Decision: defer free-QFT promotion

Paper 6 should not attempt to prove the remaining arrows. The free benchmark
promotion problem should be deferred to a dedicated later paper, tentatively:

```text
Free-QFT Promotion From ISP Stochastic Curvature
```

That follow-up would ask a different question from Paper 6:

> Can the Paper 1 one-particle stochastic-curvature datum, plus explicit
> sampling, covariance, spectrum, vacuum/Fock sector, and local algebra data,
> reconstruct a standard free relativistic QFT representation?

Paper 6 may prepare that problem by listing the gates above. It should not bury
a Fock/CAR construction, a positive-energy theorem, and a local algebra theorem
inside a paper whose main job is to separate stochastic, operational, and QFT
reconstruction layers.

### Papers 1-5 Markovization audit

Barandes alignment imposes one rule on the previous papers:

> A product of stochastic kernels is physical time composition only when a
> division event, record, reset, or declared operational composition domain has
> been supplied. Otherwise products must be read as algebraic relative maps,
> tensor-factor identities, or Hilbert-lift calculations before Born squaring.

Audit result:

| Source | Risk Location | Verdict | Action |
| --- | --- | --- | --- |
| Paper 1 | finite exchange-defect group commutators and finite-slab comparison maps | Safe. These are algebraic comparison-map products for endpoint kernels, not Markov restarts through intermediate records. | No change needed. |
| Paper 2 | projective naturality and path compatibility | Safe. Paper 2 explicitly says naturality is not a Markov-composition axiom and warns against hypersurface divisibility. | No change needed. |
| Paper 3 | product cancellation and finite-depth circuit laboratory | Mostly safe, but easy to misread as circuit-layer Markovization. | Added an explicit caveat: the circuit lab is a representation-level endpoint factorization or auxiliary lift, not arbitrary partial-kernel composition. |
| Paper 4 | operational families, records, and sequential composition domains | Safe. Composition is tied to declared operations, detector records, controls, and readout schemes. | No change needed. |
| Paper 5 | local gate strings used for no-truncation and cutoff bounds | Mostly safe, but easy to misread as stochastic divisibility through gates. | Added an explicit caveat: gate strings are declared Hilbert-lift operations used before Born squaring; the stochastic object is the whole declared operation unless gate records are physical division events. |

This audit matters because it keeps the V2 stack internally consistent. The
program may use algebraic products, relative maps, inverses, commutators,
Hilbert-lift gates, and declared operational strings. What it may not do is
quietly replace an indivisible endpoint kernel by a product of unrecorded
partial stochastic shadows.

## 11. Candidate Main Claims For Paper 6

Paper 6 should now be organized around one main thesis with two parts:

> Relativistic ISP treats whole-process stochastic laws and declared division
> events as primary. It rejects Markovized reconstruction from component
> shadows unless real division events are supplied. It can reconstruct regulated
> operational ISP nets only from whole-process kernels, declared records,
> tomographic instruments, locality maps, and sector data.

This thesis is strong enough to be publishable because it is neither vague nor
purely negative. It identifies a precise obstruction and a precise route around
it.

### Main No-Go N: Markovized component shadows do not reconstruct QFT

Claim:

> Component-level stochastic shadows, when composed as if the process were
> Markovian/divisible, do not determine a unique coherent quantum composition
> law or local QFT representation.

Evidence:

1. Mach-Zehnder obstruction;
2. diagonal phase fibers over `\Gamma`;
3. local factorization underdetermination;
4. gauge center ambiguity;
5. Paper 4 operational underdetermination.

Expected theorem form:

> There exist two enriched coherent theories with identical declared
> component-shadow data on a chosen benchmark family but different predictions
> for coherent undivided experiments. Hence no functor from Markovized
> component-shadow data to QFT representations can be faithful on operational
> predictions.

### Main Conditional Reconstruction R

Claim:

> If ISP is enriched by whole-process kernels or declared division events,
> tomographically complete instruments, projective locality, and sector/center
> resolution, then a regulated operational ISP net can be reconstructed up to
> operational equivalence. Under additional QFT axioms, this may be represented
> as a local algebraic QFT candidate.

Expected theorem form:

1. finite operational process theorem, now Theorem 7;
2. finite center-resolved operational local-net theorem, now Theorem 8;
3. gauge open-chain theorem using the Paper 5 input package
   `\mathcal D_{\mathrm{gauge}}^{K,L}`;
4. no continuum claim unless refinement, covariance, spectrum, and sector
   gates are proved.

### Decision for the draft

The draft should not choose between No-Go N and Reconstruction R as if only one
can survive. The clean architecture is:

1. prove No-Go N unconditionally for Markovized component-shadow data;
2. prove Reconstruction R conditionally for enriched whole-process/record
   operational data;
3. use the gap between them to define the missing ontology of QFT:
   coherent phases, local algebras, covariance, sectors, and state selection.

This is the honest Paper 6 thesis.

## 12. First Concrete Test Cases

### Test case A: two-path coherent recombination

Purpose:

- prove No-Go N in the smallest possible setting by showing that a Markovized
  component-shadow reconstruction fails;
- separate record-writing from reversible phase marking;
- show why stochastic shadows do not encode interference.

Expected result:

- Markovized component-shadow composition predicts `50/50`;
- the whole-process coherent kernel predicts `\cos^2(\phi/2)` and
  `\sin^2(\phi/2)`.

This is the clean pedagogical example for the paper.

### Test case B: finite detector tomography

Purpose:

- prove Theorem 7 in a regulated operational setting;
- show exactly what extra data Paper 4 must supply.

Expected result:

- process maps are reconstructible if preparations/effects are separating;
- without separating instruments, multiple lifts remain equivalent.

### Test case C: open-chain Abelian gauge benchmark

Purpose:

- test whether the Paper 5 gauge package can support local algebra
  reconstruction at fixed cutoff and open boundary.

Expected result:

- center-resolved local operational statistics are reconstructible;
- matter-only statistics are insufficient;
- full continuum compact `U(1)` remains conditional on the `K -> infinity`
  theorem or obstruction.

### Test case D: exchange-defect operational projection

Purpose:

- determine whether the raw exchange curvature from Paper 3 can be converted
  into a QFT-relevant local commutator or curvature observable.

Expected result:

- only projected operational coefficients are measurable;
- raw `E_{R,S}` is not itself an observable;
- Paper 6 must not identify exchange defects with QFT commutators without a
  reconstruction theorem.

## 13. Relation To Experiments

Paper 6 should be careful about experimental language.

The Mach-Zehnder example is not proposed as a new test of QFT. It is a
diagnostic of what information a reconstruction scheme must contain. Standard
quantum optics already demonstrates phase-sensitive coherent composition.

An ISP-vs-QFT experimental difference can only be claimed after specifying:

1. the ISP record criterion;
2. which laboratory interaction is reversible marking and which is an
   irreversible ISP record;
3. the operational instruments;
4. the null QFT prediction;
5. the ISP prediction;
6. unknown constants or thresholds;
7. whether a null result rules out the model or only the chosen record
   threshold.

This prevents Paper 6 from mistaking a reconstruction no-go for an empirical
anomaly.

## 14. Publication Shape

Paper 6 should now be converted from investigation notes into a publication
draft with the following spine.

1. **Abstract and thesis.** State the mixed result: Markovized component shadows
   do not reconstruct QFT; enriched whole-process/record data reconstruct finite
   operational nets; continuum QFT needs extra gates.
2. **Barandes alignment.** Whole-process kernels, declared division events,
   representational Hilbert lifts, and Schur-Hadamard gauge.
3. **Export ledger.** What Papers 1-5 supply and what they do not supply.
4. **No-Go N.** Mach-Zehnder obstruction, whole-process correction,
   epsilon-division criterion, phase-fiber ambiguity, and component-derived map
   failure.
5. **Locality/factorization no-go.** Four-state reset example, two-qubit
   factorization example, and dimension-counting obstruction.
6. **Positive reconstruction theorem.** Theorem 7 and Theorem 8 with explicit
   frame constants and residual propagation.
7. **Gauge benchmark.** Paper 5 input package, detector condition-number
   trichotomy, fixed-cutoff open-chain gauge reconstruction, and the explicit
   decision that continuum compact `U(1)` QFT is not claimed.
8. **QFT promotion gates.** Covariance, spectrum, vacuum/sector, continuum,
   local algebra, gauge centers, lift-gauge discipline, and the free benchmark
   deferral.
9. **Audit and claim discipline.** Papers 1-5 Markovization audit, experiment
   caution, claim audit, and current verdict.

This order keeps the paper readable: the reader sees the obstruction first,
then the Barandes-compatible repair, then the strongest positive theorem, and
only then the boundary between finite operational reconstruction and QFT.

### Main theorem list for the publication draft

The paper should advertise only these main formal results.

1. **Theorem A:** Markovized component-shadow reconstruction fails for coherent
   two-path recombination.
2. **Proposition B:** Whole-process kernels avoid the false Markov product.
3. **Definition C:** Epsilon-division criterion for legitimate partial-kernel
   composition.
4. **Theorem D:** Local factorization is not determined by a bare global kernel.
5. **Theorem E:** Finite operational process reconstruction under
   span/separation.
6. **Theorem F:** Epsilon-stable finite operational ISP-net reconstruction.
7. **Theorem G:** Fixed-cutoff open-chain gauge reconstruction from the Paper 5
   package.
8. **Proposition H:** Coarse-detector conditioning trichotomy.
9. **Gate I:** Finite-to-QFT promotion checklist and free-QFT deferral.

Everything else should support these results or be moved into remarks,
examples, or appendices.

## 15. What Paper 6 Should Prove First

The first theorem package is now clear:

1. Definition 1 gives the Markovized Gamma-only component-shadow foil.
2. Theorem 1 proves the Mach-Zehnder obstruction to Markovized component-shadow
   reconstruction.
3. Proposition 1B gives the Barandes-compatible whole-process correction.
4. Definition 1C makes division/record events explicit.
5. Proposition 2 proves phase-fiber ambiguity.
6. Proposition 3 proves that maps derived only from component-shadow kernels do
   not repair the phase gap.
7. Theorem 4 proves local-factorization underdetermination by an explicit
   four-state reset example and a two-qubit local-algebra example.
8. Proposition 5 states the Paper 5 gauge benchmark as a regulated input gate,
   not a full QFT reconstruction.
9. Proposition 6B uses the stochastic-quantum theorem as finite representation
   existence, not QFT uniqueness.
10. Theorem 7 gives the minimal positive finite operational reconstruction
   theorem.
11. Theorem 8 gives an epsilon-stable finite operational local-net
   reconstruction theorem under explicit tomography and residual hypotheses.
12. Definitions 5C and 5D make the Paper 5 frame constants and gauge residual
   budget explicit.
13. Theorem 5E instantiates Theorem 8 on the fixed-cutoff open-chain gauge
   package, and Decision 5F places that theorem in Paper 6 proper.
14. The Schur-Hadamard gauge discipline and Proposition 6C separate finite
   representation existence from physical QFT reconstruction.

The next proof-hardening pass should pursue:

- conversion from investigation notes into the publication spine listed in
  Section 14;
- explicit proof-polishing of Theorem 5E and Proposition 5C.1;
- or a more abstract algebraic no-go theorem beyond finite operational nets.

## 16. Backlog

Completed at investigation level:

1. Markovized `GammaOnlyData` is formalized in Definition 1.
2. No-Go N is proved in Theorem 1 for the Mach-Zehnder family, with Proposition
   1B showing how a whole-process kernel avoids the false Markovized product.
3. Division/record events are isolated in Definition 1C, and the
   epsilon-division criterion is stated in Definition 1D.
4. Component-kernel-derived maps are shown insufficient in Proposition 3.
5. `CoherentISPData` is initiated as enriched ISP reconstruction data in
   Definition 6.
6. The stochastic-quantum theorem is imported as an existence theorem in
   Proposition 6B.
7. Finite operational tomography is proved in Theorem 7 under explicit
   span/separation assumptions.
8. The Paper 5 gauge benchmark is translated into a regulated reconstruction
   gate in Proposition 5.
9. The local-net/factorization no-go is formalized in Theorem 4, including a
   concrete two-qubit example where a one-qubit phase gate in one factorization
   becomes an entangling `ZZ` phase gate in another.
10. Theorem 4C adds the dimension-counting generalization for `m,n >= 2`.
11. Definition 5B translates Paper 5 into a reconstruction input package.
12. Theorem 8 proves the first positive epsilon-stable regulated operational
    local-net reconstruction theorem, with explicit preparation/effect frame
    constants and residual propagation.
13. Definitions 5C and 5D define the Paper 5 tomography constants and residual
    budget, including the canonical microscopic frame with `\kappa=1`.
14. Theorem 5E gives the quantitative fixed-cutoff open-chain gauge
    reconstruction theorem:
    `\varepsilon_{\mathrm{rec}}\le\kappa\eta+\varepsilon_{\mathrm{gauge}}`.
15. Decision 5F puts the open-chain gauge theorem in Paper 6 proper while
    keeping continuum compact-rotor QFT as a promotion gate.
16. Schur-Hadamard lift gauge is separated from physical gauge and operational
    phase statements.
17. Existence and uniqueness are separated after Theorem 8.
18. The covariance, spectrum, vacuum/sector, continuum, and field/algebra gates
    are stated, including the finite-to-QFT promotion checklist.
19. The free benchmark QFT-promotion gate is spelled out: sampling,
    translation/hypersurface covariance, spectrum, vacuum/sector, local algebra,
    and continuum stability are all required beyond the Paper 1 curvature datum.
20. Papers 1-5 have been audited for accidental Markovization. Paper 3 and Paper
    5 now carry explicit caveats where representation-level products could be
    misread as stochastic divisibility.
21. The scope decision is fixed: Paper 6 proves no-go plus finite operational
    reconstruction and does not attempt continuum QFT reconstruction.
22. Proposition 5C.1 gives the coarse-detector conditioning trichotomy: full
    finite-block reconstruction, quotient reconstruction, or failed/unstable
    reconstruction.
23. The free-QFT promotion problem is deferred to a dedicated later paper.
24. Section 14 gives a publication spine and main theorem list.

Remaining proof-hardening tasks:

1. Convert the investigation draft into the publication order of Section 14.
2. Tighten Theorem 5E and Proposition 5C.1 into the notation style of the final
   paper.
3. Decide whether the abstract algebraic no-go should remain as examples or be
   elevated to a standalone theorem beyond finite operational nets.
4. Move the free-QFT promotion theorem target into the next-paper roadmap.

## 17. Claim Audit

| Claim Type | Current Status | Paper 6 Rule |
| --- | --- | --- |
| Markovized Gamma-only reconstruction | No-go theorem drafted. | May claim failure of QFT reconstruction from component shadows composed as if the process were Markovian/divisible. |
| Whole-process ISP kernels | Proposition 1B drafted. | May encode coherent circuit statistics directly; do not replace them by component products without division events. |
| Division/record events | Definitions 1C and 1D drafted. | Any stochastic restart, conditioning, or component composition requires declared physical record/division structure plus an explicit residual budget. |
| Stochastic-quantum theorem | Proposition 6B drafted as existence input. | May use finite unistochastic/dilation existence, but not uniqueness or QFT promotion. |
| Phase/lift recovery | Obstructed for component-shadow data by Mach-Zehnder and phase-fiber examples. | May not claim Hilbert phases without whole-process/coherent composition data. |
| Raw exchange maps | Component-kernel-derived strengthening drafted. | `J_R` and `E_{R,S}` remain algebraic unless operationally projected and inherit only the information in the declared kernel family. |
| Local factorization | No-go theorem, examples, and dimension count drafted. | May not infer local QFT net from a global kernel or operator alone. |
| Finite operational process reconstruction | Theorem 7 proved. | May claim reconstruction under span/separation and declared composition assumptions. |
| Finite operational local-net reconstruction | Theorem 8 proved in epsilon-stable finite form. | May claim conditional reconstruction from enriched finite ISP-net data with explicit tomography and residual assumptions. |
| Paper 5 gauge benchmark | Repackaged as `\mathcal D_{\mathrm{gauge}}^{K,L}` and quantitatively instantiated in Theorem 5E. | May use as regulated fixed-cutoff input, not as continuum QFT output. |
| Coarse/noisy detectors | Proposition 5C.1 drafted. | Full reconstruction requires bounded separation constant; otherwise reconstruct only the quotient or fail. |
| Free benchmark QFT promotion | Gate package drafted. | Paper 1 supplies stochastic curvature only; QFT promotion still needs covariance, spectrum, vacuum/sector, local algebra, and continuum stability. |
| Paper 6 scope | Fixed. | Do not attempt continuum QFT reconstruction in this paper; defer free-QFT promotion. |
| Papers 1-5 Markovization audit | Completed with caveats added to Papers 3 and 5. | Products must be classified as algebraic, tensor-factor, lift-level, or declared operational composition; never silent Markov divisibility. |
| Coherent Hilbert lift | Extra assumption or separate reconstruction theorem. | Must be labeled as lift data, not stochastic data. |
| Relativistic QFT | Requires covariance, spectrum, vacuum/sector, continuum, and algebra gates. | Must not be claimed from finite operational reconstruction alone. |
| Experimental discrepancy | Not established by reconstruction no-go. | Requires separate ISP-vs-QFT model, constants, record criterion, and null prediction. |

This audit is the guardrail for Paper 6. It keeps the paper rigorous even if
the conclusion is mixed: strong no-go for Markovized component shadows,
positive finite reconstruction for enriched whole-process/record data, and
strict gates before any QFT claim.

## 18. Current Verdict

Paper 6 should not try to prove full continuum QFT reconstruction directly.
That would overreach the exports from Papers 1-5.

The rigorous path is now:

1. keep the Markovized component-shadow no-go as the main negative theorem;
2. define whole-process kernels and division/record events as the legitimate
   ISP replacement for arbitrary Markov factorization;
3. use the stochastic-quantum theorem as a finite representation-existence
   input, while separating uniqueness questions;
4. prove finite operational ISP-net reconstruction;
5. use the Paper 5 open-chain gauge package as the main fixed-cutoff positive
   theorem, with detector conditioning made explicit;
6. defer continuum/free-QFT promotion to a later paper with covariance,
   spectrum, vacuum/sector, local algebra, and continuum-limit hypotheses.

This would make Paper 6 valuable even if the answer is negative: it would say
exactly what ISP can reconstruct from whole-process kernels, records, and
declared locality data, and exactly where ordinary QFT contains more
representational structure.
