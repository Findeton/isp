# Paper 2 (v6) — Spatial direction, flow-drift, and interacting Tomonaga-Schwinger integrability

**Author:** Felix Robles Elvira

**Status:** Research investigation, numerical probes, and sharpened derivation target. This combined Paper 2 keeps both v6 legs in one place: Part I extracts the oriented spatial frame and GR flow-drift observable from causal order; Part II analyzes the interacting covariance residue, the division-event memory law, and the A/B fork for whether `g(s²)` is derived or postulated. It is not a derivation of GR and not a completed relativistic collapse model.

Builds on: Paper 1 v6. Part I addresses the antichain-dynamics leg after the correction in Paper 1 §5.15: the down-set commutator is blind to the GR tangential shift, so the right observable is flow-drift of slice labels or carried fields. Part II addresses the scalar-rate / Tomonaga-Schwinger integrability leg from Paper 1 §6/§10: the memory must be a Lorentz-invariant, microcausal, positive-type interval object with finite stress-energy response.

## The v6 hinge

Paper 1 reduces the v6 program to two linked questions.

First, the causal set must contain enough spatial information for the
hypersurface-deformation bracket. This is the dynamics leg. The needed object
is not merely a scalar distance; it is an oriented spatial frame and an inverse
spatial metric on antichains, so that the antisymmetric lapse product can become
a tangential flow-drift.

Second, the division-event process must be a Lorentz-invariant physical record
process. This is the covariance leg. The needed object is not merely a colored
noise or a finite memory time; it is a Tomonaga-Schwinger-integrable correlation
law:

```math
G(x,y)=g((x-y)^2)
```

with positive type, microcausality, no vacuum flashes, and finite stress-energy
response.

The hinge is that these two legs must refer to the same objective events. The
events that define causal-set density and antichain geometry must also be the
events whose memory law supplies scalar rates and gravity-source records.
Therefore the decisive A/B fork is:

| question | branch A | branch B |
|---|---|---|
| memory form | derived from invariant record formation | selected as an admissible collapse kernel |
| memory scale | fixed by finite-record stability | free phenomenological smearing scale |
| event rate | computed as invariant threshold-crossing density | free collapse rate |
| gravity source | same record event defines geometry/source | added flash source channel |

Part I tests the spatial-frame side of this hinge. Part II tests the
memory-law side. The paper is strongest only if both sides close on the same
event criterion.

## Part I. Spatial direction and flow-drift from causal order

### 0. The reduced question

Paper 1 v6 isolates the dynamics leg into three ingredients:

1. a finite-difference lapse gradient on an antichain;
2. the inverse spatial metric extracted from causal interval counts;
3. an oriented spatial direction or frame on the antichain.

The first two are already available in Paper 1. This paper asks whether the
third is recoverable from causal order and counting alone, and whether the
resulting frame can express the GR tangential drift:

```math
\xi^i=g^{ij}(N\partial_jM-M\partial_jN).
```

The important correction is that a vanishing down-set commutator is not a
Carrollian no-go. In GR the commutator of two normal deformations is tangential;
it slides labels on the slice while leaving the final down-set unchanged. The
test must therefore look for tangential drift, not for a changed set of events.

### 1. State of the art

Timelike distance from causal order is standard: interval cardinality estimates
Lorentzian volume, and therefore proper time. Spacelike distance is harder.
Rideout-Wallden style common-future constructions give noisy spacelike distance
and adjacency information. Thickened antichains can recover topology, and
spatial Laplacians can be built on causal-set hypersurfaces.

Those are scalar or unoriented structures. The GR bracket needs a vector
structure: a signed direction along which the antisymmetric lapse gradient can
point. The question here is whether the spatial adjacency graph carries that
orientation.

### 2. Oriented frame recovery

The tested construction is:

1. choose a thin antichain-like slice;
2. build a spatial graph using causal data only;
3. connect nearby slice events by earliest common-future meeting height;
4. compute low eigenvectors of the graph Laplacian;
5. compare the recovered eigen-coordinates to the true simulation coordinates
   only after the construction is complete.

Global spectral embedding gives a clean signal:

| test | metric | result |
|---|---|---|
| 1+1 | Fiedler coordinate versus true slice coordinate | mean correlation 0.94 |
| 2+1 | first two nontrivial eigenvectors versus true coordinates | R-squared 0.95 and 0.92 |

The local version uses per-event neighbourhood MDS from meeting-height data,
then aligns to the true local positions only for evaluation. It is real but
noisy:

| local test | result |
|---|---|
| Procrustes frame score | mean 0.78, median 0.83 |
| fraction above 0.8 | 0.56 |

Verdict: the oriented spatial frame is recoverable from order and counts,
cleanly in global spectral form and noisily in local finite form.

### 3. Flow-drift: the correct observable

The down-set commutator cannot see the GR structure function. The right
observable is the tangential drift of labels under two normal deformations.

In a noise-free grid test, push each slice point along the local unit normal by
a small lapse-dependent amount. A tilted slice has a tilted normal, so applying
two lapse pushes in opposite orders creates a second-order tangential drift.
The measured drift matches the GR prediction with correlation 1.0000 and slope
1.001 after the expected sign and step-size normalization.

On a causal set, use the recovered frame from §2 to estimate lapse gradients and
form the drift observable. Over five sprinklings:

| metric | result | gradient-blind null |
|---|---|---|
| correlation of drift with GR profile | 0.63 | near 0 |
| enrichment at high predicted drift | 1.38 | about 0.8 |

This is not an exact closure theorem. It is a positive signal that the recovered
frame can express the GR tangential drift, where the earlier down-set observable
was blind.

### 4. Curved coefficient and tensor structure

Flat space cannot distinguish GR from a constant-coefficient or Hořava-like
theory, because the inverse spatial metric is constant. Curved tests are needed.

For a two-dimensional conformal metric, the clean mechanism predicts that the
flow-drift coefficient is the inverse spatial metric. The grid test separates
GR from a flat-normal/Hořava rule: the GR coefficient dips with curvature, the
flat-normal coefficient does not.

On a causal sprinkling, the coefficient is extracted from order and number by
proper-time chains and local density. The chain-derived coefficient tracks the
curved inverse metric with correlation 0.99, and the chain and density channels
agree with correlation 0.99. The density channel is partly tautological because
the sprinkling density encodes the conformal factor; the chain channel is the
load-bearing independent check.

In higher-dimensional grid tests, the drift vector tracks the full inverse
spatial tensor, not just a scalar magnitude:

| case | tensor agreement | isotropic-scalar comparison | rotation |
|---|---|---|---|
| 2+1 | cosine 1.0000 | cosine 0.973 | 13.4 degrees |
| 3+1 | cosine 1.0000 | cosine 0.974 | 13.1 degrees |

So the construction is sensitive to the full tensor structure of the GR
structure function in the clean mechanism. The remaining causal-set task is the
full event-by-event tensor extraction in 3+1, not merely the grid mechanism.

### 5. Honest status

What is now in hand:

- causal data support a spatial adjacency graph;
- low graph-Laplacian modes recover oriented spatial coordinates;
- local frames are recoverable but noisy;
- the correct tangential flow-drift observable is identified;
- in clean tests, the assembled normal-flow mechanism produces the GR drift;
- in causal-set tests, the recovered frame carries a positive drift signal;
- curved and tensor tests show the coefficient should be the inverse spatial
  metric, not a constant scalar.

What remains open:

- build the actual direction-coupled antichain deformation rule, not just the
  diagnostic formula;
- prove exact bracket closure in the continuum limit;
- reduce local-frame noise enough for a robust finite construction;
- repeat full event-by-event curved and 3+1 causal-set tensor tests;
- combine this dynamics leg with the scalar-rate / Tomonaga-Schwinger
  integrability leg developed in Part II of this paper.

The result is therefore not "GR derived." It is the removal of a specific
missing-ingredient objection: causal order and counts do contain an oriented
spatial frame capable of expressing the GR tangential drift.

## Part II. Interacting covariance residue and memory derivation target

**Status of this part:** Research program, literature review, sharpened question, and receipt plan. This part is not a proof that the indivisible reconstruction is Lorentz-covariant for interacting fields. It identifies the exact open question: whether the division-event memory is forced by the v6/ISP substrate or selected as a covariant collapse kernel.

### 0. The question, in one paragraph

Paper 1 reduced **the entire v6 program** to one residue: does the *interacting* indivisible reconstruction
deliver a **Lorentz-invariant, microcausal correlation** for its division-event process — equivalently, is the
indivisible interacting evolution **Tomonaga–Schwinger integrable** (path-independent between arbitrary
spacelike slices, `[𝓗(x),𝓗(y)]=0` for spacelike `x,y`)? Paper 1 §6 argued energy-finiteness is *downstream* of
covariance; §4 here **sharpens and partly corrects** that — covariance is necessary, but finiteness *also*
requires the memory spectrum to decay in the **spacelike** region. The quartic template
`ĝ(q²)=e^{−q⁴/β⁴}` passes this test, while the covariant Gaussian does not. So the question is the covariance
of the division-event process — its first-order data *and* its
memory. This part asks it precisely **within ICS** (division events = a causal set, memory = the indivisible
non-Markovian law, target = a covariant `g(s²)`), reviews the literature it inherits, runs a covariance probe
(**§3**, which relocates the binding constraint to the **localization observable**), and **ports the 2025
covariant-collapse recipe into ICS (§4)** — a local field operator `:φ̂²:` that resolves the observable (sharp
*and* covariant), a quartic admissible memory template, and normal-ordering = no vacuum flashes. The honest
landing: as ported, v6
is a **covariant collapse model whose flashes source semiclassical gravity** — coherent and concrete, but not
(yet) a derivation of GR from a pure ISP reconstruction; the residue is whether the memory is ISP-*derived* or
*postulated*, plus the gravity coupling. Section 5 turns that A/B residue into a precise derivation target:
which part of `g(s²)` is forced by covariance/integrability, which part is fixed by energy and vacuum receipts,
and which part would still be an added collapse parameter.

---

### 1. The literature this residue inherits [EST]

The residue is not new to ICS — it is the central open problem of *relativistic* objective-collapse / primitive-
ontology models, plus the Lorentz-invariance theory of causal sets. ICS inherits both. The state of the art:

#### 1.1 The free case is solved; the interacting case is *reduced*, not solved
- **Tumulka, "A relativistic version of the GRW model" (2006, quant-ph/0406094) [EST].** A manifestly
  Lorentz-invariant **flash** process for `N` *non-interacting* distinguishable particles. The free division-
  event substrate exists and is covariant. (This is Paper 1 §5.4's "existence.")
- **Tumulka, "A Relativistic GRW Flash Process With Interaction" (2020, arXiv:2002.00482) [EST].** Extends to
  *interacting* particles — **but** the construction takes as **input** a *given* interaction-local
  (microcausal) **Tomonaga–Schwinger** unitary evolution, and inserts collapses into it. It *assumes* "no
  interaction at spacelike separation." So the interacting flash model **reduces** the covariance question to
  *having a microcausal TS evolution* — it does not construct one. **This is exactly our residue:** the
  TS-integrable interaction-local evolution is the missing input, not an output.
- Crucially, both are **Markovian** (Poisson flashes). ICS is **non-Markovian** (indivisible) — the genuinely
  new content lives in the memory.

#### 1.2 The collapse-model obstruction: energy divergence, and the "colored ⇒ frame-dependent" pessimism
- **Pearle, relativistic CSL [EST].** White (Markovian, `δ`-correlated) collapse noise coupled to a quantum
  field produces a **UV-divergent rate of energy production** — the relativistic-CSL energy catastrophe.
- **Adler & Bassi, "Collapse models with non-white noises" (2007, arXiv:0708.3624) [EST]**, and the standard
  reading: avoiding the divergence requires **colored** (finite-correlation-time) noise; but colored-in-*time*
  noise selects a preferred frame, hence is **frame-dependent / non-relativistic**. The pessimistic standard
  conclusion has been: *finiteness forces frame-dependence* — the best one can do is non-relativistic CSL.
  (Paper 1 §6's frame-fixed `τ_c` probe is exactly this trap, and exhibits it: heating ratio `3.10` between
  frames.)

#### 1.3 The 2025 turn: a covariant *interval-colored* correlation does work
The pessimism above was about coloring in a frame's **time**. The escape — coloring in the **invariant
interval** — is precisely Paper 1 §6's `f(s²)`, and the 2025 literature is converging on it:
- **Bedingham, "Relativistic State Reduction Dynamics" (2011, arXiv:1003.2774; Found. Phys. 41, 686) [EST].** A
  **mediating field** whose relativistic propagator smears the coupling: the *same* object both regulates the
  energy *and* makes the dynamics "Lorentz covariant, frame independent, and free of divergent behavior." One
  object does both — exactly Paper 1 §6's unification.
- **"Towards relativistic generalization of collapse models" (2025, arXiv:2507.06954) [EST].** For a collapse
  operator that is a **quadratic local field operator**, a collapse noise with a **non-Markovian
  Lorentz-invariant correlation**, plus a **normal-ordering** prescription, is *free of the previous problems*
  and has CSL-like behavior non-relativistically. **This is the existence-template for our `f(s²)`:** a
  non-Markovian covariant correlation is not only allowed, it cures the obstruction — with two extra
  ingredients (quadratic operator, normal ordering) ICS must reckon with.
- Related recent: a relativistic collapse model with **quantized time variables** (2025, arXiv:2506.07959);
  **non-Hermitian colored-noise** relativistic localization (2025, arXiv:2501.07050).

#### 1.4 The nonlinear no-go — and why linearity matters for ICS
- **"Relativistic Covariance and Nonlinear Quantum Mechanics: Tomonaga–Schwinger Analysis" (2025,
  arXiv:2511.15935) [EST]** (with an active 2026 comment, arXiv:2602.06845). It derives the operator
  integrability conditions for foliation independence including the **Fréchet-derivative terms from
  state-dependence**, and finds that **nonlinear (state-dependent) modifications violate them at spacelike
  separation**. Deterministic nonlinear collapse that suppresses superpositions seems to *force* nonlocality →
  breaks TS integrability.
- **Why this matters for ICS [ARG].** ISP is **not** a nonlinear modification of the Schrödinger equation; it
  is a **linear stochastic process that reconstructs standard QM** (Barandes). The state-dependence that
  trips the nonlinear no-go is absent at the level of the reconstructed (linear, unitary) dynamics. ICS can
  therefore *aim* to sit on the side the no-go does **not** rule out — provided the division-event layer does
  not smuggle in an effective state-dependent nonlinearity (the caveat of §2.3).

#### 1.5 Causal sets: discreteness *can* be Lorentz-invariant, and the memory must be infinite-valency
- **Bombelli, Henson & Sorkin, "Discreteness without symmetry breaking: a theorem" (gr-qc/0605006; MPLA 24
  (2009) 2579) [EST].** A **Poisson sprinkling** of Minkowski admits **no equivariant measurable map to a
  preferred direction** — a sprinkled causal set breaks no Lorentz symmetry. Decisively: **no finite-valency
  graph can be associated to a sprinkling Lorentz-invariantly.** So a covariant memory/correlation on the
  division-event causal set **cannot be nearest-neighbour** — it must be a function of the **invariant
  interval over all causal relations**, i.e. exactly `f(s²)`. (This is Paper 1 §4B's substrate condition and
  the geometric reason the memory must be `f(s²)`, fused.)

#### 1.6 ISP and its open relativistic extension
- **Barandes, "The Stochastic-Quantum Correspondence" (2023, arXiv:2302.10778) [EST]** and **"Quantum Systems
  as Indivisible Stochastic Processes" (2025, arXiv:2507.21192) [EST].** Quantum systems ↔ **indivisible**
  (non-Markovian) stochastic processes; the empirical content is fixed by the **first-order conditional
  probabilities**, while the process is an **equivalence class** that may differ in higher-order conditionals.
  The relativistic-QFT extension (incl. the Standard Model) is **explicitly an open problem**.
- **The lever hiding here [ARG]:** if only the first-order conditionals are empirically fixed, the
  higher-order **memory structure is partly gauge** — leaving freedom to *choose a Lorentz-covariant
  representative* of the memory (a covariant `f(s²)`), provided the first-order conditionals are themselves
  covariant. ICS would then *select* covariance from within the equivalence class rather than impose it.

---

### 2. Sharpening the question within ICS / v6

#### 2.1 Which side is v6 on? (It inherits the problem — it does not evade it.) [ARG]
A pure ISP *reconstruction* reproduces unitary QM exactly, conserves energy, and adds no physical collapse —
so the relativistic-collapse energy/covariance obstruction would not even apply. **But v6 needs more:** the
division events must be **physical** — they *source gravity* (flashes build the metric; Paper 1 §2, §5.5,
cross-referencing the Tilloy–Diósi / paper-4 sourcing). A physical, mass-localizing division event is a
**flash in the GRW sense**, with real effects. Therefore **v6 sits on the physical-flash side and inherits the
relativistic-collapse covariance problem in full.** This is the honest fork:

> **Reconstruction vs modification.** If division events are pure bookkeeping, there is no covariance problem
> but it is unclear they can source gravity (gravity needs a real stress-energy locus). If they are physical
> gravity sources, v6 inherits the relativistic-flash covariance problem. **v6 requires the second.** So the
> §10 residue is genuinely the relativistic-collapse integrability problem — now to be solved with ICS-specific
> structure, not dissolved.

#### 2.2 The residue, stated precisely
> **Central question (ICS interacting TS integrability).** Does the interacting indivisible reconstruction
> admit a division-event process whose memory is a **Lorentz-invariant, microcausal correlation `f(s²)` on the
> division-event causal set**, consistent with (i) the standard microcausal interacting QFT unitary evolution
> as its first-order/empirical content, and (ii) the division events as the mass-localizing gravity source?

By Paper 1 §6 this single object delivers covariance *and* energy-finiteness. By §1.3 such an object **exists**
for relativistic collapse (quadratic operator + non-Markovian covariant correlation + normal ordering). The
ICS-specific task is whether the *indivisible reconstruction itself* produces it.

#### 2.3 The ICS-specific levers (stated with their caveats) [ARG]
1. **Linearity (vs the §1.4 no-go).** ISP is linear-stochastic, so it aims past the nonlinear-collapse
   integrability no-go (2511.15935). *Caveat:* a physical division event that localizes mass is effectively a
   state-dependent event; v6 must show the *gravity-sourcing* coupling does not reintroduce the forbidden
   state-dependent nonlinearity at spacelike separation. **This is the sharpest internal tension.**
2. **Intrinsic non-Markovianity (vs §1.2 pessimism).** The covariant `f(s²)` correlation that §1.3 needs is
   *added by hand* in CSL; in ICS it is **intrinsic** — indivisibility *is* the non-Markovian memory. ICS does
   not postulate the memory; it must *derive its covariance*.
3. **Causal-set substrate (with §1.5).** BHS guarantees a Poisson division-event set is Lorentz-invariant and
   forces the memory to be infinite-valency = `f(s²)`. So the geometric substrate and the required correlation
   form are the *same* condition (Paper 1 §4B = §6, fused).
4. **Equivalence-class freedom (§1.6).** ISP fixes only first-order conditionals; the higher-order memory is
   gauge, so a covariant representative may be *selectable*. *Caveat:* the first-order conditionals must
   themselves be covariant — which is the microcausal-QFT input of §1.1 (Tumulka's assumed interaction-local
   TS evolution). The freedom helps with the *memory*, not the *first-order* layer.

#### 2.4 What would settle it — the decisive sub-questions
- **(Q1) [RESOLVED IN FORM — §3 probe]** Is the first-order division-event data covariant (`f(s²)`)? **Yes, iff
  the localization observable uses the Lorentz-invariant measure `dp/2ω`** (Newton–Wigner / Wightman), not
  naive position eigenstates (which the probe shows are frame-dependent, CV 0.44). A covariant first-order
  substrate exists. *Open part:* its interacting/continuum form (does covariant localization survive
  interactions — the §1.3 quadratic-operator + normal-ordering recipe).
- **(Q2) [SECONDARY]** Can the higher-order memory be chosen covariant within the equivalence class? Once Q1's
  covariant observable is fixed, the first-order data are already `f(s²)`, so a covariant memory completion is
  immediate — lever 4 is no longer the binding constraint.
- **(Q3) [OPEN — now the central tension, *sharpened* by §3]** Does the gravity-sourcing coupling preserve
  microcausality (no spacelike state-dependence)? §3 tightens this: a covariant localization is **non-sharp**
  (Hegerfeldt tails), in tension with a point-localized gravity source. Can v6's flashes be covariantly
  localized yet localized *enough* to source gravity?
- **(Q4) [OPEN]** Do the §1.3 ingredients (quadratic localization operator, normal ordering) have ICS-natural
  counterparts on the division-event causal set?

§3 discharges Q1 in form and demotes Q2; the residue now concentrates on **Q3** (covariant-but-localized-enough
gravity sourcing, vs the nonlinear no-go) and Q4 (the interacting recipe).

---

### 3. First probe: the binding constraint is the *observable*, not the memory [PROBE]

I set out to test lever 4 (can the equivalence-class memory be *chosen* covariant). The computation
(`code/v6_p2_covariance_feasibility.py`) shows the binding constraint is **upstream of the memory** — it is the
**first-order localization observable (Q1)**. For a 1+1 relativistic particle (`H=√(p²+m²)`), the Born
transition `Γ(a,t)=|⟨x₂|U|x₁⟩|²` was computed under **boosts at fixed `s²`** (same invariant interval) for two
localization choices:

| localization (measure) | `Γ` along boost orbit — **1+1** | `Γ` along boost orbit — **3+1** (physical) | covariant? |
|---|---|---|---|
| naive position (`dp`) | varies, CV **0.44** (`s²=6`) | varies, CV **0.48** (`s²=6`); 0.73 at `s²=2` | **NO — frame-dependent** |
| invariant (`dp/2ω`) | const, CV ~**0.01** | const, CV **7×10⁻⁴** (`s²=6`) | **YES — a genuine `f(s²)`** |

The result is **dimension-robust** — 3+1 (`code/v6_p2_covariance_feasibility_4d.py`) confirms 1+1, and the
covariant measure is even cleaner at moderate `s²` (CV `7×10⁻⁴`). The one honest wrinkle: near the light cone
(`s²=2`) the invariant-measure CV grows to `4.7×10⁻²` — this traces to the **frame-fixed Gaussian smearing**
of the records (a fixed-frame `σ`, itself not boost-invariant), which bites where `σ` competes with `√s²`; it
is an artifact of the regulator, not the `dp/2ω` measure (which is exactly covariant unsmeared).

**The binding constraint is Q1, not lever 4.** Naive-position first-order data are frame-dependent, and *no*
higher-order memory freedom can repair *fixed* first-order data. The fix is a **covariant localization** — the
Lorentz-invariant measure `dp/2ω` (the Klein–Gordon inner product; Newton–Wigner localization; the field
Wightman two-point function) — which makes `Γ` a genuine `f(s²)` (the small residual `CV≈0.01` is the
frame-fixed Gaussian smearing of the records, not the measure). So a covariant choice **exists**, and it is the
*known* one — the same covariant-localization structure behind Tumulka's covariant flashes. The residue's gate
is the **division-event observable**, and it has a concrete covariant answer.

**But this *sharpens* Q3 (the gravity tension) [ARG].** Covariant localization is **not sharply local**:
covariantly-localized states have superluminal tails (Hegerfeldt's theorem; the Newton–Wigner position
operator is non-local). v6 wants division events sharp enough to source gravity at a *point* (a flash). So the
probe **resolves Q1 in form** (covariant first-order data exist, via `dp/2ω`) while **tightening Q3**: a
covariant division event is non-sharp, in tension with a point-localized gravity source. The open question
becomes whether v6's flashes can be covariantly localized (a smooth `f(s²)`) yet localized *enough* to source
gravity — the smooth-vs-sharp tension that runs through the entire relativistic-flash program (and the reason
Tumulka builds flashes from a microcausal evolution rather than from sharp position collapses).

*What remains unrun:* the higher-order memory feasibility LP (lever 4) is now secondary — it only matters once
a covariant observable is fixed, and with the covariant observable the first-order data are *already* `f(s²)`,
so a covariant memory completion is immediate. The genuinely open analytic core is Q3 (gravity coupling vs
microcausality) together with Q1's continuum/interacting form (does the covariant localization survive
interactions — the §1.3 quadratic-operator + normal-ordering recipe).

---

### 4. Porting the 2025 covariant-collapse recipe into ICS [ARG + PROBE]

The §1.3 existence-template (arXiv:2507.06954) gives a *concrete* covariant interacting recipe. Porting it
onto the division-event setting both **discharges the §3 tension** and **supplies an admissible memory
template** — and exposes the remaining structural gap honestly.

**The recipe (verified).** (i) Collapse/division operator `Q̂(x) = ½α:φ̂²(x):` — a **local, quadratic,
normal-ordered scalar field operator**, a Lorentz scalar, whose non-relativistic limit is the **mass-density
operator**. (ii) A non-Markovian, **Lorentz-invariant** noise correlation `G(x−y) = g(s²)`. (iii)
**Normal-ordering** removes the vacuum `δ(0)` (divergent vacuum particle production). (iv) Microcausality from
the locality of `Q̂` + time-ordering of the double-commutator dissipator `[Q̂(x₂),[Q̂(x₁),·]]`.

**The ICS mapping.**

| recipe ingredient | ICS / v6 counterpart | what it settles |
|---|---|---|
| `Q̂=½α:φ̂²:` (local scalar field op) | the **division-event observable** | Q1 + Q3-localization |
| `G(s²)`, non-Markovian, `Ĝ(q)=e^{−q⁴/β⁴}` | the **indivisible memory** (Paper 1 §6 `f(s²)`) | constrains the memory class (corrects §6) |
| normal-ordering (`:·:`) | **no vacuum division events** | matches AS4 and the §5.5 vacuum receipt |
| locality + time-ordering | causal-set microcausality | matches §4B and the §5.12 TS-loop target |

**1. The local field operator dissolves the §3 Hegerfeldt tension.** §3 found the covariant localization
(`dp/2ω`) is *non-sharp* (Hegerfeldt) — a problem only in the **first-quantized** position description. The
recipe's `:φ̂²(x):` is a **local field operator**: simultaneously *sharp* (built at a point, smeared), *covariant*
(a Lorentz scalar), *microcausal* (commutes at spacelike separation), **and** its non-relativistic limit is the
mass density — the gravity source v6 needs. So moving from single-particle position flashes to QFT local
operators **resolves Q1 and the localization horn of Q3 at once**; the smooth-vs-sharp tension was a
first-quantized artifact. (This is also why Tumulka builds interacting flashes from a microcausal field
evolution, not from sharp position collapses.)

**2. The quartic memory class is admissible — correcting Paper 1 §6.** A covariant memory `g(s²)` has a
spectrum `ĝ(q²)` that must decay as `q²→±∞` — in *both* the timelike and **spacelike** regions, because the
heating samples `Ĝ` at on-shell momentum sums/differences spanning both. Paper 1 §6's frame-fixed Gaussian
`S(ω)=e^{−(ωτ)²}` was non-covariant; its covariant analogue `ĝ(q²)=e^{−q²/β²}` **blows up spacelike**
(`q²<0 ⇒ e^{+}`). The probe (`code/v6_p2_porting_quartic_memory.py`) confirms it: the covariant Gaussian's
heating **diverges** (doubling ratio `~10³¹ → ∞`), while the recipe's **quartic** `ĝ(q²)=e^{−q⁴/β⁴}`
**converges** (ratio `→1`). So the ICS division-event memory is constrained to a positive-type Lorentz-
invariant class with two-sided ultraviolet decay; the quartic-damped kernel is the clean template checked
here, not a uniqueness theorem. This is a sharper statement than §6, and a self-correction: *the covariant
indivisible memory cannot be Gaussian in the interval.*

**3. Normal-ordering = no spontaneous vacuum division events**, exactly the AS4 / §5.5 vacuum receipt (an
inertial detector in the vacuum does not flash). The vacuum-`δ(0)` removed by `:·:` is the field-theoretic
version of "no records form from nothing."

**The honest remaining gap: reconstruction vs modification (the A/B fork, §2.1).** The recipe is a **collapse
model** — it *modifies* QM: a dissipator with a free rate `γ`, genuine decoherence, energy production `∝N`, and
free parameters `(γ,β)`. ISP, by contrast, *reconstructs* QM exactly. Porting therefore lands v6 concretely on
the **modification/physical-flash side**: *a covariant collapse model (2507.06954-type) whose flashes are the
division events and source semiclassical gravity (Tilloy–Diósi / paper 4), with ISP/indivisibility supplying
the non-Markovian covariant memory `g(s²)`.* That is a coherent, concrete proposal — but it is **weaker** than
"GR from a pure ISP reconstruction": the free `(γ,β)` and the `∝N` energy production are markers of a genuine
modification, not a derived reconstruction. **Whether the ISP indivisible reconstruction *itself* produces this
dissipator structure (so `g(s²)` is the reconstruction's own correlation rather than an added collapse) is
unproven** — and is the precise, sharpened form of the residue after porting.

**Still open after porting:** (a) the A/B fork above — is `g(s²)` ISP-derived or postulated? (b) the
**gravity-coupling horn of Q3** — coupling `:φ̂²:` localizations to the metric semiclassically (Tilloy–Diósi)
with its own decoherence/consistency, not done here; (c) whether ISP fixes `(γ,β)` rather than leaving them
free. Porting has, however, **removed the localization obstruction (Q1/Q3-local) and identified an admissible
two-sided memory class, with quartic damping as the worked template** — the residue is now the A/B status of
`g(s²)` and the gravity coupling, not the observable.

---

### 5. The A/B fork as a derivation problem [ARG + PROBE-PLAN]

The post-§4 situation is sharp enough to state as a fork rather than a mood.

**Fork A — ISP-derived memory.** The division-event memory is not added. It is the higher-order correlation
structure of the indivisible stochastic process after imposing relativistic record covariance, Tomonaga-
Schwinger path independence, no-vacuum-record normalization, and finite stress-energy production. In this
branch `g(s²)` is an output: its invariant form, spectral falloff, and scale are fixed by the record law.

**Fork B — postulated collapse memory.** The model adds a covariant collapse kernel and collapse parameters to
standard QFT. This is coherent and may be physically valuable: it gives a relativistic flash model whose
events can source semiclassical gravity. But it is not a pure ISP reconstruction unless the kernel and its
parameters are derived from the indivisible process rather than supplied as a new law.

The aim is therefore not merely to write a good `g(s²)`. The aim is to prove which pieces of `g(s²)` are forced
by the v6 ontology, and which pieces remain extra collapse-model data.

#### 5.1 Memory object and admissibility class

Let `Q_a(x)` denote the local scalar record operators used to generate division events. The index `a` labels
typed record channels, such as mass-density, detector, or curvature-source channels. The two-event memory is
the bilinear kernel appearing in the record influence functional:

```math
{\mathcal I}_G[J]
=
\exp\!\left[
-{1\over 2}
\sum_{a,b}
\int d^4x\,d^4y\,
J_a(x)G_{ab}(x,y)J_b(y)
\right].
```

For a physical record process, `G` must satisfy four non-negotiable conditions:

1. **positive type:** every finite test-source packet has nonnegative variance;
2. **Poincare covariance:** no foliation or inertial frame is named by `G`;
3. **TS compatibility:** changing the spacelike slicing used to compose local record operations does not
   change the joint event law;
4. **finite stress-energy response:** coupling to local field operators does not produce an ultraviolet
   divergent energy rate.

In a flat, homogeneous vacuum sector, these conditions reduce the scalar-channel kernel to an invariant
distribution:

```math
G_{ab}(x,y)=G_{ab}(x-y).
```

Poincare covariance then decomposes the typed scalar part into invariant spectral channels:

```math
\widehat G_{ab}(q)=
\sum_r P^{(r)}_{ab}\,F_r(q^2),
```

where `P^{(r)}` are positive matrices on typed record channels. In the single-channel case this is the
familiar form:

```math
G(x-y)=g((x-y)^2),
\qquad
\widehat G(q)=F(q^2).
```

This is the first important distinction. The interval form is not an aesthetic choice; it is the covariance
class of a scalar two-record memory. But a covariance class is not yet a unique kernel.

#### 5.2 A-Form theorem target

**Theorem target A-Form.** Suppose a relativistic indivisible record process has:

1. **objective division events:** the event set is an observer-independent physical point process, not a
   foliation bookkeeping artifact;
2. **covariant first-order records:** the one-record law is generated by local Lorentz-scalar observables and
   agrees with standard microcausal QFT first-order content;
3. **Tomonaga-Schwinger integrability:** joint record probabilities are independent of the spacelike
   hypersurface path used to compute them;
4. **spacelike microcausality:** record generators commute, or their dissipative influence functionals commute,
   at spacelike separation;
5. **same empirical first-order content:** different higher-order memory representatives may not change the
   empirical one-record law;
6. **no vacuum flashes:** the inertial vacuum has no spontaneous division-event density after the chosen
   normal-ordering or vacuum subtraction;
7. **finite stress-energy production:** the record process injects finite energy into a finite-energy state,
   uniformly under removal of the ultraviolet cutoff.

Then every admissible two-event scalar memory representative is Lorentz-invariant and positive type. In the
flat vacuum sector it has the interval form above, and its spectral density must have two-sided ultraviolet
decay strong enough to control both the timelike and spacelike momentum regions sampled by local scalar record
operators.

**Lemma A1 — covariance forces interval dependence.** Conditions 1 through 4 forbid a preferred slicing in
the two-record law. Translation invariance gives dependence only on `x-y`; Lorentz invariance gives dependence
only on invariant separation and typed internal labels. On a causal set this also forbids a finite-valency
nearest-neighbour memory: by the Bombelli-Henson-Sorkin no-preferred-frame theorem, no Lorentz-equivariant
finite-valency graph can be selected from a Poisson sprinkling.

**Lemma A2 — record positivity gives positive type.** Since the memory is a covariance of record fluctuations
or an influence-kernel variance, finite source packets must obey:

```math
\sum_{a,b}\int d^4x\,d^4y\,
\overline{f_a(x)}G_{ab}(x,y)f_b(y)
\ge 0.
```

This is the precise mathematical difference between an admissible stochastic memory and an arbitrary
Lorentz-invariant distribution.

**Lemma A3 — TS integrability eliminates frame-colored memory.** A frame-colored kernel can make energy finite
in one frame, but it makes the record influence functional depend on the chosen foliation. Therefore it fails
condition 3 even if it satisfies a nonrelativistic colored-noise bound.

**Lemma A4 — finite energy tests the spacelike spectral tail.** For quadratic local record operators, the
heating functional samples sums and differences of on-shell momenta. Those samples enter both timelike and
spacelike large-`q²` regions. Therefore a covariant Gaussian written as `exp(-q²/β²)` is inadmissible: it
decays in one invariant direction and grows in the other.

**Lemma A5 — quartic damping is an admissible representative, not a uniqueness theorem.** The quartic class:

```math
F(q^2)=\exp[-(q^2)^2/\beta^4]
```

passes the two-sided tail test in the §4 probe. But the theorem should not claim quartic uniqueness. The
admissible class is:

```math
\hbox{positive-type Lorentz-invariant spectral kernels with two-sided ultraviolet decay.}
```

The quartic kernel is the clean template currently known to pass the receipts. A different positive-type
function with comparable two-sided decay would be equally admissible unless a later variational or
record-stability principle selects the quartic representative.

**Conditional conclusion.** A-Form is proved only up to the following live analytic input: the positive-type
two-sided spectral tail must be derived from the indivisible stochastic reconstruction itself. If that input
is supplied, the memory form is no longer postulated. Without it, the paper has selected an admissible
covariant collapse kernel, not derived the ISP memory.

#### 5.3 A-Scale theorem target

Even if A-Form is supplied, a free scale remains unless ISP fixes it. This is
the fork-breaker. A covariant memory kernel with adjustable constants is still
branch B; a memory kernel whose constants are forced by finite record formation
is branch A.

**Theorem target A-Scale.** Let `R_x` be the local record channel assigned to a
small invariant diamond `D_x`, and let `E_x` denote the proposition that this
channel has become an objective division event. The event-rate constant and
memory-scale constant are ISP-derived only if there is a scalar record
functional:

```math
{\mathcal S}_R(D_x)
```

and a universal threshold:

```math
S_*
```

such that:

```math
E_x
\quad\Longleftrightarrow\quad
{\mathcal S}_R(D_x)\ge S_*.
```

The constants are then not fitted. They are:

```math
\gamma
=
\lim_{V\to\infty}
{1\over V}
{\mathbb E}
\left[
\#\{x\in V:{\mathcal S}_R(D_x)\ge S_*\}
\right],
```

and:

```math
\beta^{-1}
=
\inf
\left\{
\ell>0:
\left|
\mathrm{Corr}(E_x,E_y)
\right|
\le e^{-1}
\hbox{ whenever } (x-y)^2=\ell^2
\right\}.
```

These formulas are not yet proofs. They state what must be proved for A-Scale.

**Definition: finite-record stability functional.** The candidate functional
must measure the irreversible separation between the actual local record and
all same-actual refinements that still preserve empirical first-order quantum
content. A useful abstract form is:

```math
{\mathcal S}_R(D_x)
=
\inf_{\rho'\sim_1\rho}
{\mathcal D}_{D_x}
(
\rho_{R_x},
\rho'_{R_x}
),
```

where `~_1` means same first-order empirical content, and `D` is a finite
distinguishability or stability divergence on the local record algebra. The
functional is admissible only if it satisfies four tests:

- it is a Lorentz scalar on diamonds;
- it is monotone under refinement of the record algebra;
- it vanishes for vacuum bookkeeping fluctuations;
- it is positive for stable detector records that can be copied into the
  causal-set history.

**Lemma target AS1: scalar threshold.** If the local record algebra is assigned
to invariant diamonds and the stability divergence is built from
Tomonaga-Schwinger-invariant joint record probabilities, then `S_R(D_x)` is
independent of foliation. Therefore the threshold crossing event `E_x` is an
objective causal-set event rather than a frame-dependent update.

What must still be supplied: a construction of the local record algebra and the
divergence with enough regularity to compare overlapping diamonds.

**Lemma target AS2: rate from threshold crossings.** If threshold crossings form
a stationary Lorentz-invariant point process with finite second moment and no
equivariant preferred direction, then the crossing density `gamma` exists and is
the same in all frames.

The proof route is causal-set native: use the BHS no-preferred-frame result to
rule out a reconstructed rest frame, then use ergodicity of invariant diamonds
to replace ensemble averages by four-volume frequencies.

What must still be supplied: an ergodic theorem for the actual record-stability
process, not just for a Poisson sprinkling.

**Lemma target AS3: memory scale from record correlations.** The memory scale is
derived only if the threshold-event correlation has a unique finite invariant
correlation length. In spectral language, the same scale must be the first
nonzero decay scale of the positive-type kernel:

```math
\widehat G(q^2)
```

and the decay extracted from event correlations must match the decay used in
stress-energy receipts.

What must still be supplied: a proof that the finite-record correlation
function is positive type, has two-sided ultraviolet decay, and has no hidden
long-range tail that would make `beta` ambiguous.

**Lemma target AS4: no-vacuum normalization without free constants.** Vacuum
subtraction is allowed only if it is fixed by the record criterion itself. The
condition is:

```math
{\mathcal S}_R(D_x)=0
\quad
\hbox{for inertial vacuum fluctuations}
```

and:

```math
{\mathcal S}_R(D_x)>0
```

for stable detector records above threshold. Normal ordering is then not an
extra collapse convention; it is the algebraic implementation of the rule that
vacuum fluctuations are not objective records.

What must still be supplied: a local field-theoretic record criterion that
separates vacuum fluctuations from detector records without inserting a
preferred frame.

**Lemma target AS5: gravity-source identity.** The event counted by `gamma`
must be the same event that sources the v6 geometry. There cannot be one
threshold for flashes and another threshold for gravity. The required identity
is:

```math
E_x^{\rm record}
=
E_x^{\rm source}
=
E_x^{\rm causal\ set}.
```

If this identity fails, the theory has added a gravity-source channel and is
branch B.

**A-Scale receipt table.**

| receipt | quantity measured | branch-A requirement |
|---|---|---|
| detector record | threshold crossing frequency | gives the same `gamma` in every frame |
| two-record memory | event-event correlation length | gives `beta^{-1}` |
| heating | stress-energy production | finite using the same `beta` |
| vacuum | inertial no-record channel | fixes subtraction with no new parameter |
| gravity source | flash/source density | uses the same threshold event |
| foliation loop | two spacelike threshold operations | no ordering residue |

**Current A-Scale status.** The paper has not yet proved A-Scale. It has only
identified the theorem whose proof would convert v6 from a covariant collapse
extension into an ISP-derived memory theory. The decisive next calculation is a
finite detector-record model in which `S_R`, `gamma`, and `beta` are computed
from the same local record channel and then checked against the heating,
vacuum, and gravity-source receipts.

#### 5.4 Feynman receipt program

The memory law must be checked by independent finite receipts. The same `(G,\gamma,\beta)` should appear in
five calculations:

| receipt | calculation | A-branch pass condition |
|---|---|---|
| detector clicks | two-click correlations of an Unruh-DeWitt-style record register | same invariant `G` and same `β` |
| heating | stress-energy production under local scalar record coupling | finite and frame-independent with same `G` |
| vacuum | inertial vacuum division-event rate | zero after the same normal-ordering / record criterion |
| gravity source | two-flash metric/source correlation | same event law sources the causal-set density |
| foliation loop | two local source operations composed along different spacelike slicings | same joint law, no ordering residue |

This is the real Feynman move: not a toy model, but multiple physical receipts for one object. If the receipts
merely tolerate a family of kernels, the kernel is postulated. If they force the same kernel and constants, it
is derived.

#### 5.5 Finite A-Scale receipt execution [PROBE]

The first execution is deliberately finite and unforgiving. It defines one
scalar threshold model, then asks whether the same threshold event supplies the
rate, memory width, heating regulator, vacuum rule, gravity-source count, and
foliation-loop commutativity.

Code:

```text
code/v6_p2g_ascale_receipts.py
```

The model uses an invariant proper-time record profile and a smooth two-sided
memory kernel. A local event occurs when the scalar stability profile crosses a
threshold. From the same event law the script computes:

| receipt | computed quantity | result |
|---|---|---|
| detector record | threshold crossing density | `gamma = 0.14583` |
| memory width | correlation e-fold length | `beta^{-1} = 1.69991` |
| heating | finite spectral integral | numerical/analytic ratio `1.000000` |
| vacuum | threshold crossings | `0` |
| gravity source | source count versus event count | `7 = 7` |
| foliation loop | scalar projector commutator | `0.000e+00` |

The finite coherence verdict is a pass: one threshold event law can feed all
receipts without an immediate contradiction. But this is not an A-Scale proof.
The script prints the decisive line:

```text
A-Scale derivation: OPEN
```

because the threshold and memory width were visible inputs. The execution
therefore supports a precise statement:

```text
finite receipt coherence is branch-A-compatible;
finite receipt coherence is not branch-A derivation.
```

The value of the probe is that it localizes the missing theorem. To close
A-Scale, the next paper-level proof must derive the threshold and the memory
width from the finite record channel itself, then rerun the same receipts with
no free `S_*` or `ell`.

#### 5.6 No-free-parameter audit

The branch-A claim should be audited by asking where a scale, threshold, or
event criterion entered the construction. The current state is:

| object | current status | branch-A demand |
|---|---|---|
| local record algebra | constrained by covariance and locality | derive from finite ISP record channel |
| diamond/cell size | selected in probes | derive from invariant record resolution |
| threshold `S_*` | selected | derive as canonical record-stability boundary |
| event rate `gamma` | computed after `S_*` is selected | compute with no free threshold |
| memory width `beta^{-1}` | computed after `ell` is selected | derive from record correlations |
| memory form `g(s²)` | constrained; quartic is a template | derive positive-type two-sided tail |
| no-vacuum rule | matched by normal-ordering | derive from record criterion |
| gravity-source rule | identified by construction | prove same event sources geometry |
| TS loop | finite diagonal receipt passes | prove for interacting local record operators |

This table is the honest fork map. The current v6 Paper 2 has moved several
objects from "unconstrained" to "constrained", but the decisive branch-A
objects remain unproved:

```text
S_*,
gamma,
beta,
event = source = geometry.
```

If any of these remain selected rather than derived, v6 is branch B: a coherent
covariant collapse-source theory using ISP-compatible ontology.

#### 5.7 Three candidate `S_R` attacks [PROBE]

The natural next move is to try to derive the finite-record stability
functional itself. The probe:

```text
code/v6_p2h_srecord_candidates.py
```

tests three candidates on the same finite detector-record trace.

**Candidate 1: minimum same-first-order distinguishability.** Define `S_R` as a
local log-likelihood or KL/Chernoff distance from the nearest same-first-order
null record. This is attractive because it uses ISP's equivalence-class
language directly: a record is stable if it cannot be erased by a same-actual
refinement without paying distinguishability cost.

Result: it detects all planted records, but the threshold is not fixed. In the
probe, changing the evidence threshold changes the event count and rate:

| threshold | event count | `gamma` | planted records hit |
|---|---:|---:|---:|
| `0.2500` | `1737` | `28.9500` | `6/6` |
| `0.6931` | `1256` | `20.9333` | `6/6` |
| `1.5000` | `776` | `12.9333` | `6/6` |

So this candidate gives a good scalar score, but not a canonical event
boundary. A threshold of zero counts noise; a positive threshold is a choice
unless finite-record theory fixes it.

**Candidate 2: redundant-copy stability.** Define `S_R` as the amount of
redundant mutual information copied into independent record channels. This is
physically attractive because objective records are copyable and robust.

Result: it also detects the planted records, but it requires a redundancy
target. In the probe:

| threshold | event count | `gamma` | planted records hit |
|---|---:|---:|---:|
| `0.5000` | `1912` | `31.8667` | `6/6` |
| `1.0000` | `1670` | `27.8333` | `6/6` |
| `2.0000` | `1077` | `17.9500` | `6/6` |

"One bit" sounds natural, but it is still a convention unless the local record
channel itself proves that one bit, or some other value, is the invariant
division threshold.

**Candidate 3: irreversibility / non-refinability.** Define `S_R` by irreversible
growth of the local record, i.e. by a positive record-formation arrow that
cannot be undone by same-first-order refinements.

Result: this candidate is promising because it looks event-like rather than
state-like, but it depends on a coarse-grained derivative/window. In the probe:

| threshold | event count | `gamma` | planted records hit |
|---|---:|---:|---:|
| `0.7500` | `1` | `0.0167` | `1/6` |
| `1.5000` | `28` | `0.4667` | `5/6` |
| `3.0000` | `46` | `0.7667` | `6/6` |

This is the sharpest failure: the event count is sensitive not only to a
threshold but also to the derivative smoothing convention.

**Verdict of the `S_R` attack.** All three candidates can be made useful. None
derives A-Scale. The audit result is:

```text
S_R is constrained but not canonical;
S_* is not fixed;
gamma moves with S_*;
beta moves with the score/correlation convention.
```

This does not kill v6. It clarifies the next theorem. Branch A needs a
selection principle internal to finite ISP record formation, not merely a good
stability score.

#### 5.8 A-Scale regraduation no-go [THEOREM]

The three probes above are not just unlucky choices of `S_R`. They expose a
general obstruction.

**Theorem: no canonical numerical A-Scale threshold from the listed axioms.**
Assume the available structure is only:

- same-first-order ISP data;
- covariance of the local record assignment;
- monotonicity under record strengthening;
- refinement invariance under same-actual refinements;
- vacuum zero as a distinguished bottom class.

Then no nontrivial numerical threshold `S_*` is canonically selected. More
precisely, if a scalar record score `S_R` is admissible, then for every strictly
increasing regraduation:

```math
h:[0,\infty]\to[0,\infty],
\qquad
h(0)=0,
```

the score:

```math
\widetilde S_R=h\circ S_R
```

is equally admissible and has the same same-first-order content, covariance,
monotonicity, refinement order, and vacuum bottom class. Therefore any proposed
interior numerical threshold can be moved without changing the listed
structure.

**Proof.**

Same-first-order ISP data fix empirical first-order transition probabilities.
They do not fix a numerical coordinate on a stability scale. A stability score
is therefore at most a representative of an ordered record-strength structure.

Let `S_R` be any admissible representative. Since `h` is strictly increasing,
it preserves all comparisons:

```math
S_R(D_x)\le S_R(D_y)
\quad\Longleftrightarrow\quad
h(S_R(D_x))\le h(S_R(D_y)).
```

So monotonicity under record strengthening is unchanged. Since `h(0)=0`, the
vacuum bottom class remains the bottom class. Since `h` is applied pointwise to
a Lorentz scalar, covariance is unchanged. Since same-actual refinements only
compare record strengths and preserve first-order empirical content, refinement
invariance is unchanged. Thus `S_R` and `h∘S_R` satisfy exactly the same listed
axioms.

Now suppose those axioms canonically select a nontrivial numerical threshold
`S_*` in the interior of the score range. Because `S_R` and `h∘S_R` represent
the same listed structure, the selected threshold cannot depend on which
representative was chosen. But for the threshold event set to be representative
independent one would need:

```math
\{D_x:S_R(D_x)\ge S_*\}
=
\{D_x:h(S_R(D_x))\ge S_*\}.
```

For arbitrary strictly increasing `h` fixing only zero, this equality fails for
every interior `S_*`. Equivalently, if one lets the threshold transform
naturally, the transformed threshold is `h(S_*)`, not `S_*`; hence the number
itself was a coordinate choice, not a canonical value. The only thresholds fixed
by all such regraduations are the trivial endpoints: the bottom threshold that
counts any positive fluctuation, or the top threshold that counts nothing.

Therefore the listed axioms cannot select a nontrivial numerical `S_*`.
Consequently `gamma`, which is computed only after the event set is selected,
and `beta`, which is extracted only after a numerical/correlation convention is
chosen, cannot be derived from those axioms alone.

**Corollary: branch-A needs an extra selector.** A-Scale can still be closed,
but not from same-first-order data, covariance, monotonicity, and refinement
invariance alone. It needs an additional physical principle that breaks the
regraduation symmetry. Examples include:

- a criticality condition for the threshold-event process;
- a gravity-source density matching condition;
- a vacuum-zero / detector-survival boundary condition that picks a unique
  boundary;
- a canonical information unit supplied by the finite record channel;
- a dynamical TS-integrability condition that fails except at one threshold.

Those are not cosmetic additions. They are exactly the kind of extra principle
needed to convert branch B into branch A.

**Status after the no-go.** The theorem proves a negative result for a precise
input set. It does not prove v6 is branch B. It proves only that branch A cannot
get a nontrivial numerical `S_*`, and hence cannot get `gamma` and `beta`, from
the currently listed principles alone. Any branch-A closure must now print the
additional selector explicitly.

#### 5.9 A-Scale selector candidates after the no-go [PROBE]

After the regraduation no-go, the right question is not "which score feels
natural?" but "which extra selector legitimately breaks the regraduation
symmetry?" The selector must do more than make receipts coherent. It must fix
the event set, and preferably `gamma` and `beta`, without smuggling in a
collapse parameter.

Code:

```text
code/v6_p2i_ascale_selectors.py
```

The probe scans thresholds on the same finite record trace and tests the main
selector candidates one by one.

| selector | breaks regraduation? | fixes `S_*`? | fixes `gamma`? | fixes `beta`? | status |
|---|---|---|---|---|---|
| gravity-source density matching | yes, if source density is fixed | no, gives plateau | yes, by target density | no | useful but not unique |
| vacuum-zero plus detector-survival | yes, through physical boundary conditions | no, gives interval | no | no | admissibility filter |
| criticality / percolation | yes, if critical observable is canonical | grid-local point | not reliably | no | finite-size sensitive |
| minimal heating / disturbance | yes, if disturbance functional is canonical | boundary of interval | indirectly | indirectly | needs prior admissible set |
| TS-integrability fixed point | yes in principle | no in finite scalar model | no | no | nonselective here |
| canonical information unit | yes, if unit is derived | yes by convention | yes after threshold | no | externally calibrated unless unit is proved |

**1. Gravity-source density matching.** The most v6-native selector is:

```text
threshold-event density = causal-set/source density.
```

In the finite probe, the target source count is six. The selector finds:

```text
S_* in [0.1552, 2.3208]
```

with `354` threshold grid points giving the same event count. So gravity-source
matching fixes the count and therefore `gamma` once the source density is known,
but it does not select a unique numerical threshold. It is an event-density
selector, not yet an A-Scale selector.

**2. Vacuum-zero plus detector-survival.** The physical boundary condition is:

```text
vacuum event rate = 0,
detector records survive.
```

The probe finds:

```text
S_* in [0.0943, 2.3540]
```

with `409` grid points satisfying both conditions. This is a strong
admissibility filter: it rules out many bad thresholds. But it gives an
interval, not a point. To become a selector it needs an additional boundary
rule, such as minimal disturbance or maximal margin.

**3. Criticality / percolation.** A criticality selector would choose a
threshold at a phase transition of the event graph. This is attractive because
critical points can be scale-setting without arbitrary units.

The finite one-dimensional proxy finds a susceptibility peak at:

```text
S_* = 0.0500
```

but this point has `54` events, only `5/6` detector hits, and `94` vacuum
events. That is not acceptable as a division-event threshold. The verdict is
not that criticality is impossible; it is that the naive finite percolation
observable is not the right selector.

**4. Minimal heating / minimal disturbance.** This selector chooses the least
disturbing threshold among thresholds that already satisfy physical
admissibility. In the finite probe, minimizing the heating proxy over the
vacuum/detector-admissible interval chooses:

```text
S_* = 0.1552.
```

This is sharp, but only after the admissible interval has already been supplied.
It is therefore a secondary selector. It could become branch-A-native if the
disturbance functional is derived from ISP record formation, rather than chosen
as a variational preference.

**5. TS-integrability fixed point.** In principle this is beautiful: perhaps
all thresholds except one create a spacelike ordering residue, and the
TS-integrable threshold is forced.

The finite scalar model does not do this. Its threshold projectors commute for
every threshold:

```text
S_* in [0.0500, 2.3706].
```

So TS-integrability is nonselective in the present finite scalar receipt. It
remains a possible selector only in the harder interacting local-operator
theorem.

**6. Canonical information unit.** A one-bit rule gives a sharp numerical
threshold in the finite redundant-record score. The probe reports that the
nearest `S_*=1` grid point has six events, six detector hits, zero vacuum
events, and the target event density.

This is tempting. It is not yet a derivation. It becomes branch-A-native only
if "one finite record unit" is derived from the indivisible record channel
itself. Otherwise it is a convention that happens to work in the finite model.

**Selector verdict.** No tested selector closes A-Scale by itself:

```text
gravity matching: plateau;
vacuum/detector: interval;
criticality: wrong finite point;
minimal heating: boundary after prior filter;
TS fixed point: nonselective in finite scalar model;
information unit: sharp only if independently canonical.
```

The strongest branch-A path is therefore a combined selector:

```text
gravity-source density
+
vacuum-zero / detector-survival
+
ISP-native information unit or disturbance principle.
```

That combination would be an extra physical principle beyond the no-go input
set, but it could still be intrinsic to finite record formation if each piece
is derived rather than stipulated.

#### 5.10 Combined-selector criterion [THEOREM]

The selector scan shows that no single obvious selector closes A-Scale. A
combined selector is therefore the next plausible branch-A route. But a
combination is legitimate only if it is more than a pile of preferences.

**Definition: selector.** Given a record score `S_R`, each threshold defines an
event set:

```math
E_\sigma=\{x:S_R(D_x)\ge \sigma\}.
```

A selector is a condition on the family of event sets and their physical
readouts. Examples are:

```text
density(E_sigma) = source density,
vacuum(E_sigma) = 0,
detector survival(E_sigma) = 1,
heating(E_sigma) is minimal,
TS residue(E_sigma) = 0.
```

A selector is **event-invariant** if it depends only on the event set and its
physical readouts, not on the numerical label `sigma`. It is **unitized** if it
uses a numerical score only after a canonical unit has been derived from the
finite record channel itself.

**Theorem: combined-selector legitimacy criterion.** A combined selector can
legitimately evade the A-Scale regraduation no-go only if it satisfies all of
the following conditions.

| condition | requirement | failure mode |
|---|---|---|
| C1 event-invariance | each selector is stated in terms of event sets/readouts, not raw score labels | threshold is coordinate choice |
| C2 canonical unit | any numerical score threshold uses a unit derived from finite records | information unit is external convention |
| C3 isolated intersection | the intersection of selector conditions is a single event set or isolated threshold modulo regraduation | plateau/interval remains |
| C4 stability | the selected event set persists under small perturbations of detector strength, noise, cell size, and sampling | finite artifact |
| C5 scale completeness | the selected event set fixes both `gamma` and `beta`, not just event count | memory scale remains free |
| C6 one-event identity | the selected events are simultaneously record, source, causal-set, and antichain-density events | coupled branch-B source channel |

If C1-C6 hold, then the combined selector is a legitimate branch-A theorem
target. If any one fails, the combination may still define a coherent
branch-B law, but it has not derived the A-Scale constants from the ISP record
formation structure.

**Proof.**

The no-go theorem acts by regraduation:

```math
S_R\mapsto h\circ S_R,
```

where `h` is any strictly increasing map fixing the vacuum bottom class. This
changes numerical threshold labels but preserves the ordered family of event
sets:

```math
E_\sigma(S_R)=E_{h(\sigma)}(h\circ S_R).
```

Therefore any condition that refers only to event sets and physical readouts is
regraduation-invariant. Such a condition can select an event set, or a plateau
of equivalent thresholds, without choosing a score coordinate.

However, a nontrivial numerical threshold is selected only if the intersection
of all event-invariant selector conditions is isolated, or if an independently
derived score unit turns the ordered event-set boundary into a number. This is
C2 and C3. Without C2, a numerical threshold changes under `h`; without C3,
there remains a continuum or finite interval of equally admissible event sets.

Stability C4 is needed because an isolated point in one finite trace may be a
sampling artifact. If a small perturbation of detector strength, noise,
diamond/cell size, or record sampling changes the selected event set
discontinuously, the selector is not a continuum record law.

Scale completeness C5 is needed because A-Scale is not just an event-count
problem. Gravity-density matching can fix `gamma` while leaving the memory
correlation length, and therefore `beta`, free. A legitimate branch-A selector
must also select the threshold-event correlation law that feeds the same
heating and memory receipts.

Finally, C6 is needed because v6 is a one-event ontology. If the selected
record events are not the same events that source gravity and define causal-set
density, the selector has added a second physical event process. That is branch
B by definition.

These conditions are therefore necessary. They are also sufficient for the
limited A-Scale task: if C1-C6 are proved, the selected event law is
regraduation-invariant, stable, scale-complete, and identified with the v6
geometric/source events. Then `S_*`, `gamma`, and `beta` are no longer free
collapse parameters; they are readouts of a single finite-record selector.

**Immediate consequence for Paper 2.** The finite selector scan in §5.9 does
not yet satisfy the criterion. Gravity matching fails C3 for threshold
uniqueness and C5 for `beta`; vacuum/detector survival fails C3; criticality
fails C4; minimal heating depends on a prior interval and still needs a
canonical disturbance functional; TS fixed point fails C3 in the finite scalar
model; the information-unit selector satisfies C2 only if the unit is derived.
Thus the combined-selector theorem target is now precise, but not closed.

#### 5.11 Likelihood-ratio event-law selector [THEOREM TARGET]

The combined-selector criterion says what a branch-A selector must do. This
section gives the strongest presently visible candidate. The central move is
to stop selecting a numerical threshold on an arbitrary score and instead
select an event law from finite history measures.

The construction is deliberately non-Markovian. It is stated on finite
down-set histories and their conditional record laws, not on an instantaneous
Poisson rate. This keeps the proposal aligned with the Barandes/indivisible
stochastic-process picture: empirical content is carried by finite conditional
distributions over histories, and memory is a property of the process, not a
Markov update appended afterward.

**1. Canonical likelihood coordinate.** Fix a finite causal diamond `K` and
let `A_K` be the finite record algebra generated by covariant local record
readouts in the down-sets of events in `K`. Let `P^0_K` be the vacuum/no-record
reference law on `A_K`, after quotienting null events. Let `P^a_K` be the
activated law obtained by coupling a covariant detector/source probe `a` to
the same local record algebra.

The first required finite theorem is absolute continuity on the physical
quotient:

```text
LR1: for every admissible probe a, P^a_K is absolutely continuous with respect
to P^0_K on the finite physical record algebra, after removing common null
classes. Any singular active component is declared an event with infinite
evidence and is handled as a boundary case.
```

When LR1 holds, the record coordinate is the log Radon-Nikodym ratio:

```math
\ell_a(H)=\log {dP^a_K\over dP^0_K}(H).
```

Here `H` is the finite down-set history, not a Markov state. The unit of
`ell_a` is fixed by probability itself: nats, or bits after division by
`log 2`. Therefore the unit is not an arbitrary convention. This is the
candidate answer to C2.

This does not yet select the threshold. It only gives a canonical coordinate
in which threshold questions can be asked.

**2. Event-readout constraint map.** A candidate event law on `K` is a
covariant finite process `p`, assigning event weights or deterministic event
indicators to histories in `A_K`. From `p` compute the physical readout vector:

```text
R_K(p) =
(
vacuum event rate,
detector survival,
gravity-source density,
Tomonaga-Schwinger holonomy residue,
irreversible record information,
two-event memory covariance
).
```

Every component of `R_K` is a readout of the event law, not of the raw score
label. The vacuum component is computed in `P^0_K`; the detector component is
computed in the activated laws `P^a_K`; the source density is computed from
the same selected events; the TS component compares spacelike orderings of the
same local threshold operation; the information component is the likelihood
cost; and the memory component is the two-event covariance of the selected
event process.

The target readout set is:

```text
vacuum event rate = 0,
detector survival is nonzero and finite,
gravity-source density equals the causal-set/source density,
TS holonomy residue = 0 for spacelike loops,
irreversible record information is minimal among laws satisfying the above,
memory covariance is positive type with finite two-sided spectral tail.
```

This is the Einstein part of the construction: all selector conditions are
invariant facts about events and their physical readouts.

**3. Variational/free-boundary selector.** Define `C_K` to be the set of
finite event laws satisfying the vacuum, detector, source, TS, and
positive-type memory constraints. On `C_K`, minimize the irreversible record
cost:

```math
J_K(p)=D(p\Vert p^0_K),
```

where `p^0_K` is the null event law induced by the vacuum record process, and
`D` is relative entropy on the finite event algebra. If the deterministic
event-set version is used, `J_K` is the lower semicontinuous envelope obtained
by Bernoulli relaxation and then taking extreme points.

The finite selector theorem target is:

```text
LR2: C_K is nonempty and compact.
LR3: J_K is strictly convex on the quotient by physically null event
directions.
LR4: the constraint Jacobian of R_K has full rank at the minimizer.
LR5: the constrained Hessian of J_K is positive on the tangent kernel.
```

Under LR2-LR5, the minimizer `p*_K` is unique modulo null event relabeling.
The threshold boundary in the likelihood coordinate is then not chosen by
hand. It is the KKT free boundary of the finite record problem:

```math
\nabla J_K(p^*_K)+\lambda\cdot\nabla R_K(p^*_K)=0.
```

The multiplier vector `lambda` is fixed by the physical readout constraints.
This is where the arbitrary `S_*` disappears. The score coordinate supplies
units; the event law is selected by the invariant readout intersection.

**4. Scale extraction.** Once `p*_K` is selected, the A-Scale constants are
readouts:

```math
\gamma_K={1\over |K|}\sum_{x\in K} p^*_K(x),
```

and `beta_K` is the inverse correlation scale of the positive-type covariance:

```math
C^*_K(x,y)=\mathrm{Cov}_{p^*_K}(E_x,E_y).
```

A finite selector closes C5 only if the following isolation theorem holds:

```text
LR6: the spectral width / correlation length extracted from C*_K has a single
stable value under refinement, and the density gamma_K and memory scale beta_K
converge together along the same selected event law.
```

This is the Feynman part of the construction. The constants are not named;
they are printed by receipts. Detector clicks, vacuum suppression, source
density, TS loops, heating, and memory tail must all evaluate the same
selected event process.

**5. One-event identity.** The final selector is branch-A-native only if the
selected process is used once:

```text
selected record events
= selected source events
= causal-set sprinkling events
= antichain-density events.
```

This is not a slogan. It is a consistency condition on the maps out of
`p*_K`. Let `G_rec`, `G_src`, `G_cset`, and `G_slice` be the four readout maps
from the selected finite process to records, stress-energy source, causal-set
elements, and antichain density. The one-event theorem target is:

```text
LR7: the four maps factor through the same quotient event algebra and agree
on the selected support of p*_K.
```

If LR7 fails, the model may still be coherent, but it is branch B: a collapse
flash process has been coupled to a separate geometry/source process.

**Theorem: likelihood selector implies C1-C6.** Suppose LR1-LR7 hold for a
cofinal family of finite diamonds, with the constants in LR3-LR6 bounded away
from zero and infinity under refinement. Then the likelihood-ratio event-law
selector satisfies the combined-selector criterion C1-C6.

**Proof.**

C1 follows because the selector is stated entirely in terms of event laws and
readouts. A monotone regraduation of any auxiliary score leaves the finite
measures, event sets, and readout map unchanged.

C2 follows from LR1. The coordinate used for evidence is the log
Radon-Nikodym derivative of two finite record laws. Its unit is the natural
unit of distinguishability in the record channel.

C3 follows from LR2-LR5. Compactness gives a minimizer, strict convexity on
the physical quotient removes flat null directions, and the full-rank
constraint Jacobian plus positive constrained Hessian gives an isolated KKT
solution.

C4 follows by the finite implicit-function theorem. Small perturbations of
detector coupling, sampling, cell size, and noise perturb the KKT system
continuously; the nondegenerate solution persists.

C5 follows from LR6. The selected event law prints both event density and
memory correlation scale. Neither is a separate parameter once the cofinal
limit is proved.

C6 follows from LR7. All four physical roles factor through the same selected
event algebra.

Therefore the selector would evade the regraduation no-go for the right
reason: not by smuggling in a preferred numerical score, but by deriving a
single stable event law from finite non-Markovian record measures.

**Execution of the five LR steps.** The preceding theorem names LR1-LR7. The
following is the concrete proof program. It is deliberately written in finite
history language so that no Markov approximation is being slipped in.

**Step 1: finite non-Markovian history measures for LR1.** For a finite
diamond `K`, let `Omega_K` be the finite set of down-set histories resolved by
the record algebra `A_K`. A history is not a time-slice state; it is the whole
finite causal past pattern available in `K`. Let `N_K` be the common null ideal:

```text
N_K = {B in A_K : P^0_K(B)=0 and P^a_K(B)=0 for all admissible probes a}.
```

Work on the quotient algebra:

```text
A^phys_K = A_K / N_K.
```

On each atom `omega` of `A^phys_K`, define:

```text
p0(omega) = P^0_K(omega),
pa(omega) = P^a_K(omega).
```

The finite Radon-Nikodym coordinate is:

```text
ell_a(omega) = log(pa(omega) / p0(omega))
```

whenever `p0(omega) > 0`. If `p0(omega) = 0 < pa(omega)`, the atom is a
singular active atom and is placed in the event boundary with infinite
evidence. If both vanish, it has already been removed by `N_K`.

Thus LR1 is automatic at fixed finite `K` after the physical quotient and
singular active boundary split. The cofinal theorem still needs one extra
condition:

```text
LR1-ref: under refinement K -> K', the conditional expectation from A^phys_K'
to A^phys_K sends ell_a,K' to ell_a,K up to a uniformly vanishing martingale
error.
```

This is the non-Markovian replacement for a local rate law. The likelihood is
a martingale coordinate on finite histories, not an instantaneous Poisson
intensity.

**Step 2: compact event-law set for LR2.** Let `m_K` be the number of candidate
local event cells in `K`. A relaxed event law is a probability measure `q` on
`{0,1}^{m_K}`. Deterministic event sets are the extreme points. The admissible
set `C_K` is the intersection of the probability simplex with the finite
constraints:

```text
vacuum event expectation = 0,
detector response lies in a fixed finite nonzero interval,
source density equals the causal-set/source target,
TS holonomy residues vanish for the finite spacelike loop basis,
finite covariance matrix of event indicators is positive semidefinite,
two-sided memory moments obey the admissible tail bounds.
```

The simplex is compact. The listed constraints are closed: equalities and
inequalities are polynomial or linear in the atom weights of `q`, and the
positive-type memory condition is a finite positive-semidefinite matrix
condition. Therefore `C_K` is compact if nonempty.

Nonemptiness is not free. A finite witness law must be supplied. In the branch-A
program the witness is not an arbitrary collapse process; it must be built from
the same finite record histories and must pass the vacuum/source/detector/TS
checks. This is the first place the selector can honestly fail.

**Step 3: response Fisher-Gram isolation for LR3-LR5.** Choose local
coordinates `theta` on the physical quotient of the event-law simplex near a
candidate minimizer. Let:

```text
J_K(theta) = relative entropy to the null event law,
r_K(theta) = vector of active constraints.
```

At an interior relaxed minimizer, define the Hessian and receipt Jacobian:

```text
H_K = second derivative of J_K,
B_K = derivative of r_K.
```

The receipt rows of `B_K` are:

```text
vacuum row,
detector row,
source-density row,
TS-loop rows,
information-cost row,
memory-width / tail rows.
```

On the physical quotient, `H_K` is the Fisher information matrix of the finite
event law. The receipt Gram matrix is:

```math
G_K = B_K H_K^{-1} B_K^T.
```

The finite isolation criterion is:

```text
LR-Gram(K): the smallest nonzero eigenvalue of G_K is bounded below by m_K > 0
after removing redundant receipt rows and null event directions.
```

If LR-Gram(K) holds, then the receipt constraints are independent in the
metric supplied by the record information geometry. Equivalently, no hidden
finite direction can change the threshold, event density, or memory width while
leaving all physical receipts unchanged.

This gives LR3-LR5:

- strict convexity of `J_K` on the quotient gives a positive `H_K`;
- full row rank of `B_K` gives an isolated constraint surface;
- positivity of `G_K` gives a positive constrained Hessian in the KKT system.

The cofinal version is the real theorem:

```text
LR-Gram-cofinal: along the refinement family, the reduced matrices G_K have a
uniform lower eigenvalue bound m_* > 0 and a uniform upper condition bound.
```

If `m_*` collapses to zero, branch A has not derived the selector. That would
mean the receipts tolerate a hidden family of event laws.

**Step 4: cofinal scale extraction for LR6.** For the selected law `q*_K`,
define:

```text
gamma_K = event count expectation divided by invariant volume,
C_K(x,y) = covariance of selected event indicators,
beta_K = inverse correlation scale extracted from C_K.
```

The correlation scale must be defined from the same Lorentz-invariant memory
object used in the covariance leg. A convenient finite definition is the
least positive scale `beta_K` for which the normalized two-sided spectral tail
obeys the admissibility bound:

```text
tail_K(beta_K) = fixed canonical tail fraction.
```

Equivalently, one may use a second-moment width if the finite spectrum has a
single tight scale. Both definitions are acceptable only if they agree in the
cofinal limit.

The LR6 theorem is:

```text
gamma_K -> gamma,
beta_K -> beta,
and the limiting pair is independent of the cofinal refinement path.
```

This requires three receipts:

```text
tightness of selected event densities,
tightness of two-event memory spectra,
uniqueness of the limiting memory scale.
```

It is not enough for `gamma_K` to converge. If `beta_K` still varies over a
family, A-Scale is not closed.

**Step 5: one-event factorization for LR7.** Let `Q_K` be the quotient support
of the selected event law. Define four maps:

```text
G_rec   : Q_K -> finite detector/record events,
G_src   : Q_K -> finite stress-energy source cells,
G_cset  : Q_K -> causal-set elements,
G_slice : Q_K -> antichain-density events.
```

LR7 says these are not four ontological channels. They must factor through the
same selected support:

```text
G_rec = i_rec o pi_K,
G_src = i_src o pi_K,
G_cset = i_cset o pi_K,
G_slice = i_slice o pi_K,
```

where `pi_K` is the single selected-event projection. The test is operational:
for every event atom in `Q_K`, deleting it must change all four readouts in the
corresponding finite way; changing a record event without changing the source
or causal-set event is forbidden in branch A.

The finite one-event determinant is the Jacobian of these four readout maps
restricted to `Q_K`. LR7 at fixed `K` is the statement that this determinant
has no kernel after quotienting null readouts. The cofinal LR7 theorem is a
uniform lower bound on that determinant, or equivalently a uniform lower
singular value for the one-event readout matrix.

**Selector closure criterion.** The likelihood-ratio selector satisfies LR1-LR7
cofinally if and only if the following finite receipts have uniform refinement
limits:

```text
history likelihood martingale bound,
nonempty compact admissible event-law set,
positive response Fisher-Gram lower bound,
cofinal density and memory-scale convergence,
positive one-event readout singular bound.
```

This is the maximally concrete branch-A target. It remains compatible with
Barandes because the primitive object is a finite conditional history law. It
is also hard in the right place: a failure of the Gram or one-event singular
bound means the constants are genuinely not derived.

**Finite decisive-test execution.** The finite diagnostic script:

```text
code/v6_p2j_lr_decisive_tests.py
```

executes the response-Gram and one-event singular tests on a refinement family
with 16, 32, 64, and 128 candidate event cells. The script is intentionally
standard-library only. It tests two branches:

```text
branch-A toy: record/source/causal-set/slice readouts share one selected event support;
branch-B countercase: source readout is split into a separate channel.
```

The branch-A toy gives:

| cells | response-Gram min | one-event min singular | martingale error | gamma | beta |
|---:|---:|---:|---:|---:|---:|
| 16 | 0.104848 | 0.970000 | 0.050067 | 0.30254 | 11.4052 |
| 32 | 0.001066 | 0.970000 | 0.007221 | 0.29240 | 11.1785 |
| 64 | 0.141806 | 0.970000 | 0.002738 | 0.29259 | 11.1121 |
| 128 | 0.010421 | 0.970000 | 0.000500 | 0.29213 | 11.0955 |

The branch-B countercase keeps a positive response-Gram lower bound but loses
the one-event singular bound:

| cells | response-Gram min | one-event min singular |
|---:|---:|---:|
| 16 | 0.097225 | 0.000000 |
| 32 | 0.102277 | 0.000000 |
| 64 | 0.099980 | 0.000000 |
| 128 | 0.096288 | 0.000000 |

The same script also sweeps the input memory-scale parameter in the branch-A
toy over three values. Across 32, 64, and 128 cells, the stress receipt gives:

```text
memory-scale stress response-Gram lower bound: 0.000169
memory-scale stress one-event singular lower bound: 0.970000
memory-scale stress extracted beta span: [9.7682, 12.6051]
```

This does not prove LR6-beta. It says the finite Gram and one-event tests are
not artifacts of one memory-scale value. It also shows something more
uncomfortable and more useful: the response-Gram floor can become numerically
small under refinement. Therefore `c_*` is not a cosmetic constant. It is a
real cofinal theorem target.

The script now runs three adversarial floor probes. First it makes the source
receipt nearly detector-redundant. The reduced Fisher-Gram lower eigenvalue
falls with the redundancy parameter:

| epsilon | response-Gram min | condition number |
|---:|---:|---:|
| 1.000 | 0.005363 | 88.0805 |
| 0.300 | 0.000911 | 483.1705 |
| 0.100 | 0.000110 | 3773.0788 |
| 0.030 | 0.000010 | 40449.3973 |
| 0.010 | 0.000001 | 360887.1958 |

This is the finite falsifier for the `c_*` floor. If the physical receipts are
nearly redundant in the cofinal theory, the likelihood selector does not
isolate a unique event law.

Second it pinches one source-role singular value while keeping a nominal
common support:

| source floor | one-event min singular | condition number |
|---:|---:|---:|
| 1.000 | 0.970000 | 1.0825 |
| 0.300 | 0.315000 | 3.3333 |
| 0.100 | 0.105000 | 10.0000 |
| 0.030 | 0.031500 | 33.3333 |
| 0.000 | 0.000000 | infinite |

This is the finite falsifier for the `s_*` floor. A role can share the same
event labels formally while becoming invisible to one physical channel.

The same S-floor test is also printed as a deletion-density receipt. For each
role map, the deletion sensitivity of one selected event atom is the squared
column norm of that role map. With counting measure as the finite reference
measure, the lower density predicts the rolewise singular floor:

| case | min density | max density | predicted singular floor | no-merge proxy | role KL |
|---|---:|---:|---:|---:|---:|
| branch-A | 0.940900 | 1.102500 | 0.970000 | 1.000000 | 0.000000 |
| source 0.3 | 0.099225 | 1.102500 | 0.315000 | 1.000000 | 0.005430 |
| source 0.1 | 0.011025 | 1.102500 | 0.105000 | 1.000000 | 0.007402 |
| source zero | 0.000000 | 1.102500 | 0.000000 | 1.000000 | 0.007843 |
| branch-B | 0.000000 | 2.205000 | 0.000000 | 1.000000 | 0.010830 |

This is the finite version of the S-floor theorem. The support can look common
at the level of labels, but the deletion-derived role measure detects whether
one role has zero or vanishing physical visibility.
The final column is the finite role-bookkeeping KL cost after normalizing each
role measure. The unpinched one-event branch carries no extra role
bookkeeping; the source-thinned and branch-B cases do.

Third it tests the derivative of a spectral-tail crossing used to extract the
memory scale:

| tail model | beta crossing | derivative proxy |
|---|---:|---:|
| single-scale | 9.1244 | 0.151932 |
| two-scale | 8.4235 | 0.088450 |
| flat-mixture | 10.9408 | 0.051107 |

This is the finite falsifier for the `k_*` floor. A flat or multiscale memory
tail can leave the event law well-defined while making the extracted memory
scale unstable.

This is exactly what the decisive tests should do. The response-Gram test
detects whether the physical receipts isolate an event law; the one-event
singular test detects whether the selected support really feeds record,
source, causal-set, and antichain-density readouts as one event. A split source
channel can keep finite response rows healthy while failing LR7. Near
redundant receipts, role invisibility, and flat memory tails are the three
ways branch A can still fail.

The execution therefore gives a finite receipt:

```text
finite LR decisive tests: PASS for the constructed one-event toy branch;
decoupled-source branch-B countercase: FAILS LR7;
adversarial probes: identify the c_*, s_*, and k_* failure modes;
cofinal LR1-LR7 theorem: OPEN.
```

**Cofinal closure attack for the five decisive steps.** The finite execution is
not enough. The following lemmas are the sharp cofinal form of the branch-A
attack. They say exactly which facts would close the likelihood selector, and
where a hostile reviewer should press.

**Lemma LR1-ref: likelihood martingale from projective finite histories.** Let
`K_n` be a cofinal family of finite diamonds, with quotient record algebras
`A^phys_n` and refinement maps:

```text
pi_{n+1,n}: A^phys_{n+1} -> A^phys_n.
```

Assume the vacuum and activated finite-history laws are projectively
compatible:

```text
(pi_{n+1,n})_* P^0_{n+1} = P^0_n,
(pi_{n+1,n})_* P^a_{n+1} = P^a_n.
```

Let:

```math
L^a_n={dP^a_n\over dP^0_n}.
```

Then `L^a_n` is an exact finite-history martingale under the vacuum law:

```math
E_{P^0_{n+1}}\!\left[L^a_{n+1}\mid A^phys_n\right]=L^a_n.
```

Proof. For every event `B` in `A^phys_n`,

```math
\int_B E_{0}[L^a_{n+1}\mid A^phys_n]\,dP^0_n
=
\int_{\pi^{-1}B} L^a_{n+1}\,dP^0_{n+1}
=
P^a_{n+1}(\pi^{-1}B)
=
P^a_n(B)
=
\int_B L^a_n\,dP^0_n.
```

Since this holds for every finite record event `B`, the conditional
expectation identity follows. The log-likelihood coordinate is therefore not
itself a martingale, but its drift is the conditional KL increment:

```math
E_0[\log L^a_{n+1}\mid A^phys_n]-\log L^a_n
=
-D(P^0_{n+1|n}\Vert P^a_{n+1|n})
```

on each coarse atom where the conditional laws are absolutely continuous. A
uniform summable bound on these conditional KL increments is exactly the
cofinal LR1-ref receipt. This is the non-Markovian Barandes-aligned statement:
the primitive object is a compatible family of finite conditional histories,
not an instantaneous flash rate.

**Lemma LR-Gram: response separation is equivalent to a positive Gram floor.**
Let `T_n` be the physical tangent space of finite event laws at the candidate
selector, after quotienting null event directions. Let the Fisher inner product
be:

```math
\langle u,v\rangle_{H_n}=u^T H_n v.
```

Let `B_n` be the receipt differential:

```text
B_n v =
(
vacuum response,
detector response,
source response,
TS response,
information response,
memory response
).
```

Then the following are equivalent at fixed `n`:

```text
there is c_n > 0 such that ||B_n v|| >= c_n ||v||_{H_n} for every v in T_n;
the reduced response Gram G_n = B_n H_n^{-1} B_n^T has smallest positive
eigenvalue at least c_n^2.
```

Proof. Put `A_n = B_n H_n^{-1/2}`. Then:

```math
G_n=A_nA_n^T.
```

The nonzero eigenvalues of `G_n` are the squared nonzero singular values of
`A_n`. The inequality `||B_n v|| >= c_n ||v||_{H_n}` is exactly the statement
that the smallest nonzero singular value of `A_n` is at least `c_n`. Thus the
Gram floor is not a decorative statistic; it is the finite theorem that no
physical tangent direction can move the event law while all receipts remain
silent.

The cofinal LR-Gram theorem is therefore:

```text
there exists c_* > 0 such that the above separation holds for all sufficiently
large n.
```

If `c_*` does not exist, branch A has not derived `S_*`, `gamma`, and `beta`.

**Lemma LR7-cofinal: one-event factorization is a rolewise singular floor.**
For each finite diamond, let:

```text
A_rec,n, A_src,n, A_cset,n, A_slice,n
```

be the four readout maps from the selected event support `Q_n` to record,
source, causal-set, and antichain-density readouts. Branch A requires more
than injectivity of the stacked map. Each role must see the same selected
support. Therefore LR7 is the rolewise bound:

```math
\min_j \sigma_{\min}(A_{j,n}|_{Q_n}) \ge s_n > 0.
```

At fixed `n`, this is equivalent to saying no nonzero selected event atom is
invisible to any one of the four physical roles. The decoupled-source
countercase in the finite script is built precisely to show the difference:
the receipt Gram can remain positive while the source role map develops a
kernel. The cofinal one-event theorem is:

```text
there exists s_* > 0 such that s_n >= s_* for all sufficiently large n.
```

This is the clean branch-A/branch-B knife edge. If the source channel has its
own support, `s_*` is zero.

**Lemma LR6-beta: memory scale uniqueness from strict positive-type tail
crossing.** Let `C_n` be the positive-type covariance kernel of the selected
event law and let `T_n(beta)` be a normalized two-sided spectral tail
functional. Fix a canonical tail fraction `eta` in `(0,1)`. Suppose:

```text
T_n(beta) is continuous and strictly decreasing near its crossing with eta;
there are beta_min,beta_max with beta_min < beta_n < beta_max;
|dT_n/dbeta| >= k_* > 0 at the crossing;
T_n converges uniformly on [beta_min,beta_max] to T.
```

Then the equation:

```math
T_n(\beta_n)=\eta
```

has a unique stable solution for all large `n`, and `beta_n` converges to the
unique solution of `T(beta)=eta`.

Proof. Uniform convergence plus the derivative lower bound gives the usual
implicit-function stability estimate:

```math
|\beta_n-\beta|
\le
k_*^{-1}\sup_{\beta\in[\beta_{\min},\beta_{\max}]}
|T_n(\beta)-T(\beta)|.
```

Thus `beta` is not a free smearing parameter if the selected event covariance
has a strict cofinal spectral-tail crossing. If the derivative lower bound
fails, the memory scale is not derived.

**Theorem LR-KKT: cofinal selector closure from the five tests.** Assume:

```text
projective finite-history measures and LR1-ref;
nonempty compact admissible event-law sets C_n;
uniform response-Gram floor c_* > 0;
strict cofinal beta crossing with derivative floor k_* > 0;
uniform one-event rolewise singular floor s_* > 0.
```

Then the likelihood-ratio selector gives a cofinal branch-A event law. More
precisely, after passing to the projective limit of finite history laws, the
selected event process is:

```text
event-invariant,
unitized by log-likelihood distinguishability,
isolated by the response-Gram floor,
stable by the KKT implicit-function theorem,
scale-complete by the beta-crossing theorem,
one-event by the rolewise singular floor.
```

Therefore it satisfies C1-C6 and computes `S_*`, `gamma`, and `beta` as
readouts of one finite-record process.

Proof. LR1-ref supplies the canonical non-Markovian likelihood coordinate and
unit. Compactness gives finite minimizers. The response-Gram floor is the
full-rank, positive-Hessian KKT nondegeneracy condition, hence the minimizers
are isolated and stable under finite perturbations. The beta-crossing theorem
gives a unique cofinal memory scale from the selected covariance. The rolewise
singular floor identifies record, source, causal-set, and antichain-density
events on the same support. These are exactly C1-C6.

**Caution.** LR-KKT is a closure theorem conditional on five visible analytic
inputs. The finite decisive script supports the shape of the theorem; it does
not prove the cofinal floors. The next genuine branch-A proof must establish
`c_*`, `k_*`, and `s_*` from the actual indivisible finite-history dynamics.

**Three cofinal floor targets.** The finite tests show which constants matter.
The next proof should not try to select `S_*` directly. It should prove the
three floors below. If all three hold, `S_*`, `gamma`, and `beta` are readouts
of the same event-law variational problem. If any one fails, the branch-A
selector remains underdetermined.

**S-floor theorem target: rolewise support equivalence.** Let `Q_n` be the
selected finite event support in a diamond `K_n`. Let:

```text
mu_rec,n, mu_src,n, mu_cset,n, mu_slice,n
```

be the four finite positive measures induced on `Q_n` by deleting an event and
measuring, respectively, the record change, stress-source change, causal-set
element change, and antichain-density change. The branch-A support theorem is:

```text
there is one reference measure mu_n on Q_n and constants 0 < a <= b < infinity,
independent of n, such that each role measure has a Radon-Nikodym density
r_j,n = dmu_j,n / dmu_n with a <= r_j,n <= b on the selected support.
```

In the finite `L^2(Q_n,mu_n)` norm, multiplication by `r_j,n^{1/2}` has lower
norm at least `sqrt(a)`. If the role readout partition has a refinement
Jacobian lower bound `j_* > 0`, meaning it does not merge distinct selected
atoms under refinement, then:

```text
||A_j,n f|| >= j_* sqrt(a) ||f||
```

after quotienting common null directions. Therefore:

```text
s_* >= j_* sqrt(a).
```

The proof is elementary once the measure statement is available. The lower
density bound prevents invisibility of a selected event in any role; the upper
density bound prevents a singular concentration from hiding a collapsing
singular value under refinement. The real work is therefore not linear
algebra. It is proving common support and mutual absolute continuity for the
four role measures from the finite history dynamics.

The sharp failure mode is now explicit. If the source role can put zero
measure on an event that the record or causal-set role sees, then `a = 0`,
`s_* = 0`, and branch A collapses into branch B.

**S-floor proof package.** The preceding paragraph names the target. The
following is the concrete theorem to prove first.

For each selected atom `q` in `Q_n`, define four deletion functionals:

```text
Delta_rec,n(q)   = norm of the record-readout change after deleting q,
Delta_src,n(q)   = norm of the stress-source change after deleting q,
Delta_cset,n(q)  = norm of the causal-set incidence change after deleting q,
Delta_slice,n(q) = norm of the antichain-density change after deleting q.
```

These induce role measures:

```text
mu_j,n({q}) = Delta_j,n(q)^2.
```

The finite S-floor theorem is:

```text
Assume:
S1 common support: Delta_j,n(q) > 0 for every selected q and every role j;
S2 uniform visibility: Delta_j,n(q)^2 >= a_n mu_n({q}) with a_n > 0;
S3 no role blow-up: Delta_j,n(q)^2 <= b_n mu_n({q}) with b_n < infinity;
S4 no-merging: the refinement/readout Jacobian on selected atoms has lower
   singular value j_n > 0 after quotienting common null directions.

Then the rolewise one-event singular floor satisfies:
s_n >= j_n sqrt(a_n).
```

Proof. Put the finite role map in deletion coordinates. Its diagonal
visibility part is multiplication by `Delta_j,n(q)` in `L^2(Q_n,mu_n)`. By S2,
this multiplication operator has lower norm at least `sqrt(a_n)`. The
remaining refinement/readout map has lower singular value at least `j_n` by
S4. The product lower singular value is bounded below by the product of the
two lower bounds. Common null directions have already been quotiented, so no
additional kernel is present.

The cofinal S-floor theorem is the same statement with:

```text
inf_n a_n > 0,
inf_n j_n > 0,
sup_n b_n < infinity.
```

Then:

```text
s_* >= (inf_n j_n) sqrt(inf_n a_n) > 0.
```

This theorem is deliberately narrow. It does not prove the event law, the
response-Gram floor, or the memory scale. It proves only that one selected
event support is physically one support. That is why it should be attacked
first.

The proof now has three nontrivial subtargets:

```text
S-common: deleting one selected atom changes all four role readouts;
S-visible: the four deletion changes have a uniform lower normalization;
S-refine: refinement maps cannot merge selected atoms differently by role.
```

`S-common` should be derived from indivisibility: a selected event is not a
record plus a separately coupled source plus a separately counted causal-set
element. It is the one finite history atom whose deletion changes all these
readouts. `S-visible` is the quantitative part; it needs finite local
normalization bounds on record, source, incidence, and antichain readouts.
`S-refine` is the cofinal stability part; it prevents a role from becoming
blind only in the limit.

This is also the cleanest hostile test. If a proposed branch-A construction
cannot print the four deletion measures and their uniform lower densities, it
has not proved one-event ontology. It has only named four roles for one label.

**No-go from bare v6/ICS suppositions.** Can the S-floor be proved from the
currently stated indivisible-causal-set suppositions alone? No. The existing
suppositions give:

```text
ICS1 division events form the causal-set support;
ICS2 order and number give geometry;
ICS3 the event intensity must be scalar/covariant;
ICS4 record events are objective finite-history atoms;
ICS5 source, causal-set, and antichain readouts must be tied to those events
     for branch A, but no pointwise deletion-density lower bound is stated.
```

These assumptions force common event labels only at the kinematic level. They
do not force a uniform lower Radon-Nikodym density for every physical role.

**Theorem: S-floor independence from bare ICS.** There are cofinal finite
event models satisfying ICS1-ICS5 in the weak label/counting sense, with fixed
total source normalization and scalar event intensity, for which the S-floor
constant is zero.

Proof. Let `Q_n` be any cofinal family of finite causal-set event supports,
with reference counting measure `mu_n`. Put:

```text
Delta_rec,n(q) = 1,
Delta_cset,n(q) = 1,
Delta_slice,n(q) = 1
```

for every event atom `q`. Thus records, causal-set elements, and antichain
density are all carried by the same support. Now define a source deletion
functional:

```text
Delta_src,n(q_bad) = epsilon_n,
Delta_src,n(q) = sqrt((|Q_n| - epsilon_n^2) / (|Q_n| - 1)) for q != q_bad,
```

where `epsilon_n > 0` and `epsilon_n -> 0`. The total source normalization is
unchanged:

```text
sum_q Delta_src,n(q)^2 = |Q_n|.
```

The causal set, the record support, the event count, the scalar event
intensity, and the averaged source density are therefore the same as in the
unweighted model. If one does not want to choose a labelled `q_bad`, choose it
by an exchangeable auxiliary tag or by a covariant local scalar feature of the
finite history; the distributional law is still relabeling/covariance
compatible unless the axioms explicitly forbid such role-thinning. The current
bare ICS suppositions do not.

But the source role measure has density:

```text
r_src,n(q_bad) = epsilon_n^2.
```

Hence:

```text
inf_q r_src,n(q) -> 0.
```

The rolewise singular lower bound therefore obeys:

```text
s_n <= epsilon_n,
```

so no positive cofinal `s_*` exists. Taking `epsilon_n = 0` gives an even
sharper split-source countermodel: the same event label can remain in the
record/causal-set ledger while being invisible to the source role.

Thus the S-floor is not a theorem of bare v6/ICS. It requires an additional
principle:

```text
Role-faithfulness / deletion-faithfulness:
every selected division event has a uniformly nonzero deletion effect in each
of the record, source, causal-set, and antichain-density readouts, and
refinement maps preserve that lower effect.
```

With role-faithfulness added, the preceding S-floor proof package proves
`s_* > 0`. Without it, S-floor can fail while the causal-set substrate and the
scalar event law still pass their present checks.

This is not bad news. It tells us exactly what branch A must add or derive.
Indivisibility gives the candidate one event; role-faithfulness says that the
event is not merely one label but one physical deletion across all roles.

**Least-role-bookkeeping derivation route.** The natural way to avoid adding
role-faithfulness by hand is to make it the minimizer of an invariant
bookkeeping functional. This is the Einstein move in finite form: do not allow
extra role weights unless an invariant receipt forces them.

Let the role densities be:

```text
r_j,n(q) = dmu_j,n / dmu_n(q),
```

normalized by:

```text
average_mu_n r_j,n = 1.
```

Define the role-bookkeeping cost:

```text
B_n(r) = sum_j D(r_j,n mu_n || mu_n)
       = sum_j average_mu_n [ r_j,n log r_j,n ].
```

Here `j` runs over record, source, causal-set, and antichain-density roles.
The role-bookkeeping selector is:

```text
among all role densities satisfying the invariant finite receipts, choose the
one minimizing B_n.
```

**Theorem: no-extra-bookkeeping gives S-floor in the role-neutral case.** If
the finite receipts constrain only the common event support and the total
normalization of each role measure, then the unique minimizer is:

```text
r_j,n(q) = 1 for every role j and selected atom q.
```

Therefore:

```text
a_n = b_n = 1,
s_n >= j_n.
```

Proof. For one role, `x log x` is strictly convex. Under the single constraint
`average r = 1`, Jensen gives:

```text
average [r log r] >= (average r) log(average r) = 0,
```

with equality only when `r = 1` on the support. Summing over roles gives the
claim.

**Theorem: bounded invariant constraints give a positive S-floor.** Suppose
the finite receipts impose moment constraints:

```text
average_mu_n [ r_j,n F_alpha,n ] = m_alpha,n
```

where all finite features satisfy:

```text
|F_alpha,n(q)| <= F_max
```

and the Lagrange multipliers of the entropy minimizer satisfy:

```text
sum_alpha |lambda_alpha,j,n| <= Lambda
```

uniformly in `n`. Then the minimizer has exponential form:

```text
r_j,n(q) = exp( sum_alpha lambda_alpha,j,n F_alpha,n(q) - psi_j,n ).
```

After normalization, the density obeys:

```text
exp(-2 Lambda F_max) <= r_j,n(q) <= exp(2 Lambda F_max).
```

Therefore the S-floor is positive:

```text
s_* >= (inf_n j_n) exp(-Lambda F_max).
```

Proof. Strict convexity of relative entropy gives the usual finite
Euler-Lagrange equation. The uniform feature and multiplier bounds imply the
displayed upper and lower exponential bounds after subtracting the normalizing
constant `psi_j,n`. Insert the lower density bound into the S-floor theorem.

This is the strongest clean route presently visible:

```text
bare ICS -> no S-floor;
bare ICS + least role-bookkeeping with role-neutral receipts -> uniform roles;
bare ICS + least role-bookkeeping with bounded invariant moments -> positive S-floor;
unbounded multipliers or zero-forcing constraints -> S-floor can still fail.
```

So the next mathematical pressure point becomes precise. Branch A must either
prove the bounded-multiplier entropy projection theorem for the actual
finite-history receipts, or explicitly adopt role-faithfulness as a new
physical equivalence principle. Anything weaker leaves the source-thinning
countermodel alive.

**Bounded-multiplier S-floor closure.** The previous theorem assumed bounded
multipliers. The next three lemmas state exactly when that assumption is
derived.

For each role `j`, collect the invariant receipt features into a finite vector:

```text
F_n(q) = (F_1,n(q), ..., F_d,n(q)).
```

The role density minimizer solves:

```text
minimize average_mu_n [ r log r ]
subject to average_mu_n r = 1,
           average_mu_n [ r F_n ] = m_j,n,
           r >= 0.
```

Here `m_j,n` is the vector of role receipts for that role. The dimension `d`
is the number of active role-faithfulness receipts, not the number of events.
The cofinal theorem needs `d` fixed, or at least uniformly bounded, after
discarding redundant receipt rows.

**Lemma BM1: uniform Slater/interior feasibility.** Suppose the finite feature
vectors obey:

```text
|F_n(q)| <= F_max
```

and the target moment `m_j,n` lies at distance at least `delta > 0` from the
boundary of the convex hull:

```text
m_j,n in Conv{F_n(q): q in Q_n},
dist(m_j,n, boundary Conv{F_n(Q_n)}) >= delta.
```

Then there exists a feasible density `r^0_j,n` with full support and with no
zero-forcing role constraint. Equivalently, the admissible role-density set has
nonempty relative interior uniformly under refinement.

Proof. The distance-to-boundary condition means `m_j,n` is an interior point of
the finite moment polytope with a uniform ball around it, in the affine span of
the features. By finite-dimensional convex geometry, an interior point of a
finite convex hull is represented by a probability vector with all active
atoms positive after removing redundant atoms outside the affine support. The
uniform margin rules out the representation being forced onto a face. Pulling
this probability vector back to `r^0_j,n mu_n` gives a full-support feasible
density on the selected support, after quotienting common null atoms.

This lemma is the exact place where zero-forcing constraints are excluded. If
the source receipt demands zero deletion response on some event class, the
moment target sits on a face and `delta = 0`.

**BM1 finite receipt.** The diagnostic script also prints a moment-polytope
interior test using a fixed two-component coarse feature vector. It computes
the distance from each role target moment to the boundary of the convex hull
of the feature vectors:

| case | BM1 margin | target norm |
|---|---:|---:|
| branch-A | 0.441950 | 0.000000 |
| source 0.1 | 0.434284 | 0.011022 |
| source zero | 0.434206 | 0.011134 |
| branch-B | 0.441950 | 0.000000 |
| boundary-forced | 0.000000 | 0.979961 |

The lesson is important. A fixed coarse feature vector can certify that a
coarse role moment is interior while still missing a pointwise source pinch.
The source-zero and branch-B rows retain a positive coarse BM1 margin even
though the deletion-density S-floor has already failed. The boundary-forced
row shows the intended zero-forcing behavior, but only when the target moment
is driven to an exposed face visible to the chosen features.

Therefore BM1 must be proved for a role-complete local feature frame, not for
a decorative handful of coarse moments. Coarse BM1 is necessary, but not
sufficient, for pointwise `s_* > 0`.

**Lemma BM2: uniform feature normalization.** Suppose each role receipt used in
`F_n` is a normalized deletion readout:

```text
record deletion,
source deletion,
causal-set incidence deletion,
antichain-density deletion,
and any finite local invariant moments used to compare them.
```

Assume the readouts are normalized by their own finite reference variances or
finite Lipschitz constants on `Q_n`. Then:

```text
|F_n(q)| <= F_max
```

with `F_max` independent of `n`, provided:

```text
the number of active role receipts d is uniformly bounded;
each normalized deletion functional has bounded finite-history Lipschitz norm;
refinement maps are contraction or uniformly bounded on these normalized
finite readouts.
```

Proof. Each component is divided by the finite norm in which its deletion
effect is measured. The Lipschitz bound gives a componentwise bound. The
uniformly bounded number of active receipt rows converts the componentwise
bound into a vector bound. Uniformly bounded refinement maps preserve the same
bound along the cofinal family.

This is not automatic from bare ICS. It is a real finite-history estimate. If
the number of independent role receipts grows without a frame/Riesz bound, or
if a normalized readout develops unbounded local spikes, `F_max` fails and the
entropy projection can concentrate.

**Lemma BM3: multiplier compactness.** Assume the hypotheses of BM1 and BM2, and
assume redundant features have been quotiented so the moment map has no exact
flat directions. Then the entropy-projection multipliers are uniformly
bounded:

```text
sum_alpha |lambda_alpha,j,n| <= Lambda(d,F_max,delta)
```

for every role `j` and all sufficiently large `n`.

Proof. The entropy minimizer, if it exists in the interior, has exponential
form:

```text
r_lambda(q) =
exp(lambda · F_n(q) - psi_n(lambda)).
```

Its moment is:

```text
M_n(lambda) = average_mu_n [ r_lambda F_n ].
```

Assume toward contradiction that `|lambda_k| -> infinity` for a sequence of
refinements and roles. Pass to a subsequence with direction:

```text
u_k = lambda_k / |lambda_k| -> u.
```

Because `F_n(q)` is uniformly bounded, the tilted measures concentrate on the
exposed face where `u · F_n(q)` is maximal. Therefore every limit point of
`M_n(lambda_k)` lies on the boundary of the corresponding moment polytope.
But BM1 keeps the target moments at distance at least `delta` from that
boundary. This is a contradiction. Hence the multipliers are uniformly
bounded. The bound depends only on `d`, `F_max`, and `delta`.

**Theorem: derived S-floor from entropy projection.** If BM1, BM2, and BM3 hold
for the actual finite-history role receipts, and if the role refinement
Jacobian has cofinal lower bound:

```text
inf_n j_n > 0,
```

then the least-role-bookkeeping selector derives role-faithfulness and hence:

```text
s_* > 0.
```

Proof. BM3 gives the uniform multiplier bound needed in the bounded-constraint
S-floor theorem. BM2 gives the uniform feature bound. Therefore every
entropy-projection role density has a uniform lower bound. Insert that lower
bound into the deletion-density S-floor theorem, together with the no-merging
lower bound `inf_n j_n > 0`.

**What remains after BM1-BM3.** The open work is no longer philosophical. It is
to prove three finite-history facts:

```text
the role receipt targets stay uniformly inside their role-complete local
moment polytopes;
the normalized deletion features form a uniformly bounded finite frame that
can see pointwise role pinches, not only coarse moments;
the refinement Jacobians do not merge selected atoms by role.
```

If these are proved, S-floor is derived. If any fails, branch A needs
role-faithfulness as a new equivalence principle rather than a theorem.

**Local role-complete deletion frame.** The BM1 receipt showed the trap:
coarse finite moments can be interior while pointwise role visibility fails.
The missing middle object is a local deletion frame. This is the Feynman
receipt version of the Einstein equivalence idea: surround one event by local
apparatus, delete it, and check that every physical role responds through the
same local actuality measure.

**1. Definition of the local deletion frame.** For a finite selected support
`Q_n`, let:

```text
Phi_n = {Phi_n,k : k in I_n}
```

be local probes in `L^2(Q_n,mu_n)`. Each `Phi_n,k` is supported in a bounded
causal neighborhood of one selected event, or in a bounded overlap of such
neighborhoods, and is normalized in the finite record norm. The frame analysis
operator is:

```text
T_n f = ( <f, Phi_n,k> )_k.
```

The local actuality measure induced by the probes is:

```text
a_n(q) = sum_k |Phi_n,k(q)|^2.
```

This is the finite operational content of "the event is there": it is the
total local deletion sensitivity seen by the role-neutral probe frame.

**2. Local Riesz/frame bound.** The local frame theorem target is:

```text
A ||f||^2 <= sum_k |<f, Phi_n,k>|^2 <= B ||f||^2
```

for all `f` in the selected event quotient, with `0 < A <= B < infinity`
independent of refinement. This is the non-circular replacement for a
pointwise delta basis. It says local probes are complete enough to see every
selected event direction, but not so singular that refinement creates
unbounded bookkeeping.

If `A = 0`, then some selected event direction is invisible to all local
probes. No role theorem can recover S-floor from that.

**3. Role tensor factorization.** Each physical role must factor through the
same actuality measure:

```text
Delta_role,n(q)^2 = W_role,n(q) a_n(q).
```

Here `role` is record, source, causal-set incidence, or antichain density. The
role tensor theorem target is:

```text
0 < w_min <= W_role,n(q) <= w_max < infinity
```

uniformly in `role`, `q`, and `n`. This is the quantitative form of the
division-event equivalence principle. The four roles may have different
response tensors, but none may vanish on a selected event and none may hide a
singular concentration under refinement.

**4. S-floor from local frame plus role tensors.** Let `A` be the cofinal lower
frame bound, `w_min` the cofinal lower role-tensor bound, and `j_*` the
cofinal no-merging lower bound for refinement/readout maps. Then every role
analysis operator has lower bound:

```text
||T_role,n f||^2 >= j_*^2 A w_min ||f||^2.
```

Consequently:

```text
s_* >= j_* sqrt(A w_min).
```

Proof. The role operator is the local frame analysis operator followed by
multiplication by `sqrt(W_role,n)` in the event quotient, up to the finite
no-merging refinement map already isolated in the S-floor theorem. The frame
bound gives `A`; the multiplier lower bound gives `w_min`; the refinement
lower singular bound gives `j_*`; composing lower bounds gives the displayed
estimate.

**Finite local-frame receipt.** The diagnostic script tests a nontrivial local
ring frame: each probe sees one event and its two nearest selected neighbors.
The resulting finite frame and role tensor bounds are:

| case | frame A | frame B | min W | max W | derived floor |
|---|---:|---:|---:|---:|---:|
| branch-A | 0.314937 | 1.778499 | 0.940900 | 1.102500 | 0.544357 |
| source 0.1 | 0.314937 | 1.778499 | 0.011025 | 1.102500 | 0.058925 |
| source zero | 0.314937 | 1.778499 | 0.000000 | 1.102500 | 0.000000 |
| branch-B | 0.314937 | 1.778499 | 0.000000 | 2.205000 | 0.000000 |

This is exactly the right behavior. The local frame itself has a healthy lower
bound in every case. The failure of branch-B and source-zero is not a frame
failure; it is a role tensor failure, `w_min = 0`. Thus the next genuine proof
is not "find more coarse moments." It is:

```text
prove a cofinal local deletion-frame lower bound A > 0;
prove cofinal role tensor bounds 0 < w_min <= W_role <= w_max;
prove refinement no-merging for the same local frame.
```

If all three hold, S-floor is derived from local finite receipts. If the role
tensor lower bound fails, branch A still needs role-faithfulness as an added
equivalence principle.

**Same-local-generator route for the role tensor.** The local-frame theorem
reduces the problem to `w_min > 0`, but it does not by itself explain why the
four roles must have the same lower event support. The cleanest branch-A
attempt is to make every role derivative come from one local history law. This
keeps the Barandes-style non-Markovian reading intact: the primitive object is
not a transition probability at an instant, but a probability for a finite
causal history collar around the event.

**1. Local event generator.** For each selected event `q in Q_n`, let
`H_n,q^loc` be the finite local history consisting of:

```text
the bounded causal predecessor/successor collar of q;
the record incidences touching q;
the source marks touching q;
the antichain/slice incidences touching q;
the finite memory links whose endpoints lie in the collar.
```

Let `theta` be a finite coordinate chart for local deformations of this
history law, with role coordinates for record, source, causal incidence, and
slice density. Define the local negative log-likelihood:

```text
L_n,q(theta) = - log P_n( H_n,q^loc | theta ).
```

Refinement compatibility means that if `m > n`, then the refined generator
pushes forward to the old one up to the already isolated martingale error:

```text
L_m,r(theta_m) = L_n,q(theta_n) + epsilon_mn(q)
```

whenever the refined atom `r` lies over `q`, with:

```text
sup_q |epsilon_mn(q)| -> 0.
```

This is the same-first-order condition in generator form. It does not select
a scale by itself; it only says that the event generator is the same local
object through refinement.

**2. Role deletions as derivatives of the same generator.** Let `theta_0` be
the selected law, let `u_n,q` be the tangent vector corresponding to deleting
or infinitesimally weakening event `q`, and let:

```text
ell_role,n,q = d_theta_role L_n,q(theta_0).
```

The role deletion response is:

```text
Delta_role,n(q) = | ell_role,n,q( u_n,q ) |.
```

Thus the four role responses are not four independent receipts. They are four
components of the same local likelihood differential. If a role can be made
zero while the generator remains elliptic, then branch A has failed: the local
history law exists, but it does not force role-faithfulness.

**3. Ellipticity is necessary but not sufficient.** Let:

```text
H_n,q = d^2_theta L_n,q(theta_0).
```

The uniform ellipticity target is:

```text
m ||v||^2 <= <v,H_n,q v> <= M ||v||^2
```

with `0 < m <= M < infinity` independent of `n` and `q`. Define generator
actuality by:

```text
a_gen,n(q) = <u_n,q,H_n,q u_n,q>.
```

To connect the generator to the local deletion frame, require uniform
equivalence of actualities:

```text
c_a a_frame,n(q) <= a_gen,n(q) <= C_a a_frame,n(q).
```

Here `a_frame,n(q)` is the local-frame actuality from the preceding theorem.
This condition says the same event is being measured by the generator and by
the deletion probes.

But ellipticity alone does not give `S-floor`. An elliptic generator may still
have one role covector orthogonal to the deletion direction. The real branch-A
condition is role transversality:

```text
| ell_role,n,q(u_n,q) |^2 >= eta_role a_gen,n(q).
```

The required cofinal lower bound is:

```text
eta_* = inf_role,n,q eta_role > 0.
```

This is the precise version of the missing selector. If `eta_* = 0`, no
covariance, monotonicity, or refinement argument can rescue branch A, because
one physical role has a cofinal invisible deletion direction.

**4. Role tensor bound from the generator.** Under the generator hypotheses:

```text
uniform ellipticity;
frame/generator actuality equivalence;
role transversality;
refinement no-merging.
```

the role tensor in the local-frame theorem satisfies:

```text
W_role,n(q) =
Delta_role,n(q)^2 / a_frame,n(q)
```

and therefore:

```text
W_role,n(q) >= eta_* c_a.
```

Consequently:

```text
w_min >= eta_* c_a
```

and the S-floor lower bound becomes:

```text
s_* >= j_* sqrt(A eta_* c_a).
```

Proof. By role transversality,
`Delta_role,n(q)^2 >= eta_* a_gen,n(q)`. By actuality equivalence,
`a_gen,n(q) >= c_a a_frame,n(q)`. Dividing by `a_frame,n(q)` gives
`W_role,n(q) >= eta_* c_a`. Insert this lower multiplier bound into the
local-frame theorem and compose with the no-merging lower singular bound
`j_*`.

This does not smuggle in a numerical threshold. The constants are not chosen
by hand; they are the least singular/ellipticity constants of one finite local
history generator and its refinement system. The selector is successful only
if those constants have positive cofinal lower limits.

**Finite same-local-generator receipt.** The diagnostic script now separates
Hessian ellipticity from role coupling. In all four cases the local Hessian is
healthy; what fails in source-thinning and branch-B is the role
transversality floor.

| case | Hessian m | Hessian M | min coupling | max coupling | transversality |
|---|---:|---:|---:|---:|---:|
| branch-A | 0.900000 | 1.150000 | 0.940900 | 1.102500 | 0.818174 |
| source 0.1 | 0.900000 | 1.150000 | 0.011025 | 1.102500 | 0.009587 |
| source zero | 0.900000 | 1.150000 | 0.000000 | 1.102500 | 0.000000 |
| branch-B | 0.900000 | 1.150000 | 0.000000 | 2.205000 | 0.000000 |

The lesson is sharp. A same-local generator plus ellipticity is still too
weak. A successful branch-A proof must show that the same generator has a
positive role-coupling floor. That is exactly the finite-history theorem to
attack next.

**Eta-floor no-go from bare v6/ICS.** The preceding theorem identifies the
last S-floor constant:

```text
eta_* = inf_role,n,q eta_role.
```

The question is whether bare v6/ICS already proves `eta_* > 0`. Here "bare"
means:

```text
same finite causal order;
same selected events;
same local history collars;
same refinement martingale law;
same covariance, monotonicity, and first-order generator ellipticity.
```

It does not include a separate lower Fisher angle between the physical role
covectors.

**Theorem: eta-floor independence from bare ICS.** Bare v6/ICS does not imply
`eta_* > 0`.

Proof. Fix any branch-A finite history system whose local generator has a
uniformly elliptic Hessian. Keep the causal order, selected support, local
collar law, refinement maps, memory links, and generator Hessian fixed. Now
replace only the source-role covector by:

```text
ell_source,epsilon = epsilon ell_source.
```

This changes no bare causal order, no event support, no monotonicity
statement, and no refinement compatibility statement. It preserves local
generator ellipticity because the Hessian is unchanged. But the source
deletion response becomes:

```text
Delta_source,epsilon(q)^2 =
epsilon^2 Delta_source(q)^2.
```

Therefore the role transversality lower bound is at most order
`epsilon^2`. Letting `epsilon -> 0` gives a cofinal family satisfying the
bare suppositions but with `eta_* = 0`.

There is an even harsher version. Replace the source covector by a covector
parallel to the record covector:

```text
ell_source = lambda ell_record.
```

The local generator is still elliptic and the source receipt can still be
nonzero, but the four role covectors no longer form an independent role
frame. The role-Fisher determinant vanishes. Thus bare ICS cannot distinguish
"source as its own physical role" from "source as a disguised record row"
without an extra role-separation principle.

This proves independence. The missing condition is not a numerical scale
choice; it is a role-indivisibility condition.

**Minimal role-indivisibility principle.** The least additional principle that
closes this gap is:

```text
Local Role-Indivisibility.
Every selected event that is actual in the local generator must be visible,
with a cofinal positive Fisher angle, to each physical role: record, source,
causal incidence, and antichain/slice density.
```

Equivalently, role is not optional bookkeeping attached to a causal atom. If
an event is selected as physically actual, it cannot be actual as causal
order while becoming cofinally invisible as source, record, or slice density.

This is stronger than covariance and weaker than postulating the full
S-floor. It does not choose `s_*` directly. It says that the finite
same-event generator must couple the event-deletion direction to all role
covectors with a lower angle that survives refinement.

**Measurable role-Fisher packet.** Let the local role covector matrix at
event `q` be:

```text
E_n,q =
[ ell_record,n,q ;
  ell_source,n,q ;
  ell_causal,n,q ;
  ell_slice,n,q ].
```

Let the local generator Hessian be `H_n,q`. Define the role-Fisher matrix:

```text
G_role,n(q) =
E_n,q H_n,q^{-1} E_n,q^T.
```

The receipt has two parts:

```text
lambda_min( G_role,n(q) ) >= eta_F > 0;
min_role |ell_role,n,q(u_n,q)|^2 / a_gen,n(q) >= eta_D > 0.
```

The first inequality says the four physical role covectors do not collapse
into a lower-dimensional bookkeeping family. The second says the actual
event-deletion direction is not orthogonal to any physical role. Together
they imply:

```text
eta_* >= eta_D.
```

and therefore, with the frame/generator actuality comparison:

```text
s_* >= j_* sqrt(A c_a eta_D).
```

This is the finite measurable form of branch A. A reviewer can now attack a
specific matrix estimate rather than an ontology slogan.

**Finite role-Fisher falsifier.** The diagnostic script tests the independence
theorem directly. It keeps the same local Hessian window and changes only the
role covectors.

| case | rank | full minimum | reduced minimum | condition |
|---|---:|---:|---:|---:|
| branch-A | 4 | 0.896095 | 0.896095 | 1.2399 |
| source 0.1 | 4 | 0.011025 | 0.011025 | 100.7811 |
| source zero | 3 | 0.000000 | 0.896095 | infinity |
| source redundant | 3 | 0.000000 | 0.896095 | infinity |

The reduced minimum in the last two rows stays healthy because the surviving
three roles remain independent. But the full role-Fisher minimum is zero:
one physical role has vanished or become redundant. That is exactly why rank
on surviving receipts is not enough. Branch A needs the full role-Fisher
floor and the deletion-direction transversality floor.

**Route I: derivation by a same-local vertex.** The derivation route tries to
replace Local Role-Indivisibility with a computed local interaction/readout
functional. A single generator is not enough; the no-go above already showed
that. What is needed is a single local vertex whose role Jacobian can be
computed.

Let `z` be the finite local event variable in the collar of `q`, and let
`theta` be the four role source coordinates. Around the selected law, write:

```text
L_n,q(z,theta) =
L_n,q(0,0)
+ 1/2 <z,H_n,q z>
- <theta,J_n,q z>
+ 1/2 <theta,R_n,q theta>
+ O_3(z,theta).
```

Here:

```text
H_n,q is the local event Hessian;
J_n,q is the four-role Jacobian;
row_i(J_n,q) is ell_role_i,n,q;
u_n,q is the common deletion direction.
```

The normal form has two different claims, and confusing them is the main
danger.

**Generic rank theorem.** In the finite normal form, full role rank is generic
but not uniform. The determinant:

```text
det J_n,q
```

is a polynomial in the allowed second-order vertex coefficients. It is not
identically zero, because the diagonal vertex:

```text
J_n,q = diag(j_record,j_source,j_causal,j_slice)
```

with all four diagonal entries nonzero is allowed by the same local role
bookkeeping. Therefore the rank-deficient vertices lie in the algebraic zero
set:

```text
det J_n,q = 0.
```

This proves that full role rank is a generic property of the normal form. It
does not prove `eta_* > 0`. A cofinal sequence can approach the determinant
zero set while keeping the same causal order, same Hessian ellipticity, and
same first-order refinement law. This is the Feynman distinction: generic
rank is cheap; a uniform floor is physics.

**Uniform normal-form certificate.** A computable sufficient condition is
strict role diagonal dominance plus deletion-direction support. Define:

```text
d_n,q = min_i |J_n,q(ii)|;
r_n,q = max_i sum_{k != i} |J_n,q(ik)|;
delta_n,q = d_n,q - r_n,q;
chi_n,q = min_i |(J_n,q u_n,q)_i| / ||u_n,q||.
```

If:

```text
delta_* = inf_n,q delta_n,q > 0;
chi_* = inf_n,q chi_n,q > 0;
H_n,q <= M I;
```

then:

```text
lambda_min( J_n,q H_n,q^{-1} J_n,q^T )
>= delta_*^2 / (4 M)
```

and:

```text
min_role |ell_role,n,q(u_n,q)|^2 / a_gen,n(q)
>= chi_*^2 / M.
```

Proof. Strict row diagonal dominance gives invertibility by the
Levy-Desplanques theorem. Varah's inverse bound gives:

```text
||J_n,q^{-1}||_infty <= 1 / delta_n,q.
```

In four role dimensions this implies:

```text
s_min(J_n,q) >= delta_n,q / 2.
```

Since `H_n,q <= M I`, `H_n,q^{-1} >= M^{-1} I`, which gives the Fisher lower
bound. The deletion bound follows directly from the definition of `chi_n,q`
and `a_gen,n(q) <= M ||u_n,q||^2`.

This is stronger than generic full rank and weaker than postulating S-floor.
It is a finite coefficient inequality inside the local vertex normal form.

**Cofinal interval vertex class.** The previous certificate is still
pointwise. To close the derivation route cofinally, define an admissible
normal-form class `V(d_*,r_*,u_*,u^*,M)` by:

```text
|J_n,q(ii)| >= d_*;
sum_{k != i} |J_n,q(ik)| <= r_*;
|u_n,q(i)| >= u_* ||u_n,q|| for every role i;
max_i |u_n,q(i)| <= u^* ||u_n,q||;
H_n,q <= M I.
```

The interval class earns the role floor if:

```text
d_* > r_*;
d_* u_* > r_* u^*.
```

Then:

```text
lambda_min( J_n,q H_n,q^{-1} J_n,q^T )
>= (d_* - r_*)^2 / (4 M)
```

and:

```text
min_role |ell_role,n,q(u_n,q)|^2 / a_gen,n(q)
>= (d_* u_* - r_* u^*)^2 / M.
```

Proof. The first inequality is the same diagonal-dominance argument as above.
For the deletion direction, each role row satisfies:

```text
|(J_n,q u_n,q)_i|
>= |J_n,q(ii)| |u_n,q(i)|
- sum_{k != i} |J_n,q(ik)| |u_n,q(k)|.
```

Insert the interval bounds to obtain:

```text
|(J_n,q u_n,q)_i|
>= (d_* u_* - r_* u^*) ||u_n,q||.
```

Finally use `a_gen,n(q) <= M ||u_n,q||^2`.

This is the cofinal version of Feynman's calculation. It does not say "the
event is role-complete by fiat." It says: here is a compact class of local
vertices, here are interval coefficient inequalities, and here is the
resulting floor.

**Refinement transport for the actual v6 vertex.** The remaining question is
whether the actual v6 local vertex stays inside such a robust interval class
as the finite causal history is refined. Let `J_n,q`, `H_n,q`, and `u_n,q` be
the vertex data at resolution `n`. A refinement to a finer atom `r` over `q`
has transport maps on event variables and role source coordinates. In the
role-normalized basis, write the transported coefficient comparison as:

```text
J_m,r = J_n,q + E_J,mn(q);
H_m,r = H_n,q + E_H,mn(q);
u_m,r = u_n,q + e_u,mn(q).
```

This is not a Markov transition law. It is a finite-history coefficient
martingale for the local vertex. The same-first-order condition supplies
small drift of finite likelihoods; the additional work here is to require it
at the vertex-coefficient level:

```text
max_ik |E_J,mn(q)(ik)| <= epsilon_J;
||E_H,mn(q)|| <= epsilon_H;
||e_u,mn(q)||_infty <= epsilon_u ||u_n,q||.
```

**Actual-v6 robust-transport theorem.** Suppose at some resolution the actual
v6 local vertex lies in `V(d_*,r_*,u_*,u^*,M)`. Under the above transport
errors, every finer transported vertex lies in the degraded class:

```text
d' = d_* - epsilon_J;
r' = r_* + 3 epsilon_J;
u' = u_* - epsilon_u;
U' = u^* + epsilon_u;
M' = M + epsilon_H.
```

If:

```text
d' > r';
d' u' > r' U';
```

then the refined actual vertex remains robust and:

```text
lambda_min( J_m,r H_m,r^{-1} J_m,r^T )
>= (d' - r')^2 / (4 M')
```

while:

```text
min_role |ell_role,m,r(u_m,r)|^2 / a_gen,m(r)
>= (d' u' - r' U')^2 / M'.
```

Proof. Each diagonal coefficient can shrink by at most `epsilon_J`, and each
row has three off-diagonal entries, each of which can grow by at most
`epsilon_J`. Hence the diagonal and off-row bounds degrade to `d'` and `r'`.
The deletion vector component bounds degrade to `u'` and `U'`. The Hessian
upper bound degrades to `M'`. Insert these degraded constants into the
cofinal interval vertex theorem.

Thus the actual v6 local vertex stays in a robust interval class under
refinement if its one-scale margin beats the accumulated coefficient drift.
This is the derivational replacement for the suspicious axiom:

```text
one-scale robust vertex + summable coefficient transport
=> cofinal role-Fisher floor
=> eta_* > 0.
```

**AV1: actual local coincidence vertex.** Now print the finite law. In the
local collar of `q`, let:

```text
z =
(z_record,z_source,z_causal,z_slice)
```

be the role-normalized local sufficient-statistic vector. These are not four
events. They are the four local readout coordinates of one candidate division
event:

```text
record formation;
source/stress localization;
causal incidence in the finite collar;
antichain/slice crossing.
```

Let `theta` be the four conjugate source coordinates. The actual local
coincidence law is the centered finite-history negative log law:

```text
L_q(z,theta) =
L_q(0,0)
+ 1/2 z^T H_q z
- theta^T J_q z
+ 1/2 theta^T R_q theta
+ O_3(z,theta).
```

The v6 coincidence hypothesis is not merely that this law exists. It is that
the four role coordinates are separate sufficient statistics of the same
collar. In the role-normalized basis this means:

```text
J_q = D_q + R_q;
D_q is diagonal with |D_q(ii)| >= d_*;
row off-sums of R_q are at most r_*;
the common deletion direction u_q has all role components bounded below.
```

Thus AV1 supplies the actual `H`, `J`, and `u` needed by the preceding
theorem. The diagonal terms are the unavoidable first-order couplings of the
event to its four roles. The off-diagonal terms are leakage through shared
collar/memory correlations.

**AV1 theorem.** If the actual local coincidence law has separated sufficient
statistics with:

```text
|D_q(ii)| >= d_* > 0;
sum_{k != i} |R_q(ik)| <= r_*;
d_* > r_*;
|u_q(i)| >= u_* ||u_q||;
max_i |u_q(i)| <= u^* ||u_q||;
d_* u_* > r_* u^*;
H_q <= M I,
```

then the actual v6 local vertex lies in the robust interval class
`V(d_*,r_*,u_*,u^*,M)` and earns:

```text
eta_* >= (d_* u_* - r_* u^*)^2 / M.
```

Proof. This is exactly the cofinal interval vertex theorem applied to the
coincidence law's computed coefficients. No role-indivisibility axiom is used;
the lower bound comes from separated local sufficient statistics and a common
deletion direction.

**AV2: Schur-complement transport under refinement.** A refinement of the
local collar splits the local variable into coarse and internal coordinates:

```text
z = (x,y).
```

The second-order refined law has the block form:

```text
L_ref(x,y,theta) =
1/2 x^T H_cc x
+ x^T H_ci y
+ 1/2 y^T H_ii y
- theta^T J_c x
- theta^T J_i y
+ higher terms.
```

Eliminating the internal variable by conditional minimization or Gaussian
integration gives the finite Schur complement:

```text
H_eff = H_cc - H_ci H_ii^{-1} H_ic;
J_eff = J_c - J_i H_ii^{-1} H_ic.
```

Therefore if:

```text
H_ii >= lambda I;
||H_ci|| <= kappa;
||J_i|| <= beta;
```

then:

```text
||H_eff - H_cc|| <= kappa^2 / lambda;
||J_eff - J_c|| <= beta kappa / lambda.
```

The common deletion vector is transported by the same conditional expectation
map, so its component error is bounded by the same finite-history drift scale:

```text
||u_eff - u_c||_infty <= epsilon_u ||u_c||.
```

If the quantities `kappa^2/lambda`, `beta kappa/lambda`, and `epsilon_u` are
summable along refinement, the coefficient transport errors used in the
actual-v6 robust-transport theorem are cofinally small.

This is the concrete AV2 proof. It does not assume Markovian dynamics. It is
only finite conditional likelihood algebra: eliminate internal refined
history variables and read the effective local vertex.

**AV3: distance from the bad variety.** The bad set for branch A is:

```text
B =
{ det J = 0 }
union { min_i |(J u)_i| = 0 }
union { d <= r }
union { d u_* <= r u^* }.
```

The first component is role-frame collapse. The second is deletion-direction
invisibility. The third and fourth are failure of the robust interval
certificate. Define the visible distance proxy:

```text
Delta_bad =
min(
  d-r,
  d u_*-r u^*,
  sqrt(lambda_min(J H^{-1} J^T)),
  sqrt(min_i |(J u)_i|^2 / a_gen)
).
```

If `Delta_bad > 0`, then any coefficient perturbation smaller than a fixed
fraction of `Delta_bad` leaves the vertex outside the bad set. Thus AV2 plus
positive `Delta_bad` proves the actual vertex stays robust under refinement.

**AV1-AV3 finite receipt.** The diagnostic script prints the actual
coincidence vertex, the Schur transport bounds, and the bad-distance proxy.

| case | diagonal minimum | off maximum | DD margin | Fisher minimum | eta_D | bad distance |
|---|---:|---:|---:|---:|---:|---:|
| v6 robust | 0.970000 | 0.087300 | 0.882700 | 0.848135 | 0.215925 | 0.464677 |
| source 0.1 | 0.105000 | 0.009450 | 0.095550 | 0.011018 | 0.002530 | 0.050300 |
| source zero | 0.000000 | 0.087300 | -0.087300 | 0.000000 | 0.000000 | 0.000000 |
| source redundant | 0.029100 | 1.058200 | -1.029100 | 0.000000 | 0.215925 | 0.000000 |
| overmixed | 0.970000 | 1.164000 | -0.194000 | 0.333087 | 0.082616 | 0.000000 |

The Schur transport receipt is:

| case | internal coupling | internal floor | eps_J | eps_H | deletion margin | eta lower bound |
|---|---:|---:|---:|---:|---:|---:|
| weak internal | 0.020 | 0.800 | 0.0125 | 0.0005 | 0.402821 | 0.141039 |
| moderate | 0.060 | 0.800 | 0.0375 | 0.0045 | 0.323889 | 0.090865 |
| near wall | 0.120 | 0.800 | 0.0750 | 0.0180 | 0.200803 | 0.034522 |
| bad internal | 0.250 | 0.800 | 0.1562 | 0.0781 | -0.085181 | 0.000000 |

This closes AV1-AV3 for the finite local coincidence class. A robust local
coincidence vertex stays a robust local coincidence vertex under refinement
when the Schur transport errors are smaller than the bad-distance margin.

The remaining physical question is not algebraic. It is whether the actual v6
division-event law is indeed this role-separated local coincidence law. If
yes, the derivation route supplies `eta_* > 0`. If no, the paper must fall back
to the definition route or keep branch A open.

**ACV: minimal physical division-event model.** The v6 physical event is not a
bare causal-set atom. Paper 1 already uses division events as record/flash
events that source geometry. The minimal finite model therefore has one local
click and four sufficient statistics:

```text
T_record = committed record/pointer formation;
T_source = localized stress/source response;
T_causal = causal collar incidence of the click;
T_slice = antichain/slice crossing of the click.
```

Let `X` be the finite local history collar containing the click and define the
exponential finite-history law:

```text
P_theta(X | click) =
P_0(X | click)
exp(
  theta_record T_record(X)
+ theta_source T_source(X)
+ theta_causal T_causal(X)
+ theta_slice T_slice(X)
- Psi(theta)
).
```

The event variable `z` is the centered vector of these sufficient statistics
under the clicked law. The local negative log-likelihood has the normal form:

```text
L(z,theta) =
L(0,0)
+ 1/2 z^T H z
- theta^T J z
+ 1/2 theta^T R theta
+ O_3.
```

The physical content of ACV is that a real division event is a click whose
four sufficient statistics are directly sensitive to the same local
coincidence. Quantitatively, let:

```text
self_i = |J(ii)|;
leak_i = sum_{k != i} |J(ik)|.
```

The minimal physical event model satisfies:

```text
min_i self_i >= sigma_* > 0;
max_i leak_i <= ell_*;
sigma_* > ell_*;
the common click-deletion direction has every role component bounded below.
```

This is not Local Role-Indivisibility by declaration. It is a direct
finite-event statement: each of the four measured facts is a separate
sufficient statistic of the same click, and leakage through shared memory or
collar correlations is smaller than direct self-sensitivity.

**ACV normal-form theorem.** If the minimal physical division-event model has:

```text
sigma_* > ell_*;
sigma_* u_* > ell_* u^*;
H <= M I;
```

then the actual v6 local vertex lies in the robust interval class with:

```text
d_* = sigma_*;
r_* = ell_*;
```

and:

```text
eta_* >= (sigma_* u_* - ell_* u^*)^2 / M.
```

Proof. The centered sufficient-statistic law prints the local vertex
coefficients. Direct role self-sensitivity gives the diagonal lower bound;
cross-role leakage gives the row off-sum bound; the common click-deletion
direction gives `u_*` and `u^*`. Apply the cofinal interval vertex theorem.

**ACV refinement theorem.** Under refinement, split the clicked collar into
coarse sufficient statistics and internal refined substatistics. If the
internal block satisfies:

```text
H_ii >= lambda I;
||H_ci|| <= kappa;
||J_i|| <= beta;
```

then Schur elimination gives:

```text
epsilon_H <= kappa^2 / lambda;
epsilon_J <= beta kappa / lambda.
```

If the accumulated refinement errors obey:

```text
sigma_* - epsilon_J > ell_* + 3 epsilon_J;
(sigma_* - epsilon_J)(u_* - epsilon_u)
>
(ell_* + 3 epsilon_J)(u^* + epsilon_u),
```

then the actual v6 physical event stays in the robust interval class under
refinement and ACV supplies:

```text
eta_* > 0.
```

Thus ACV is closed for physical division events whose direct role
self-sensitivities dominate leakage and whose internal refined variables are
Schur-controlled. It fails for source-zero, source-redundant, or near-collapse
events.

**ACV finite receipt.** The diagnostic script prints the finite physical
event model:

| case | self | leakage | eps_J | DD margin | deletion margin | eta lower bound | bad distance |
|---|---:|---:|---:|---:|---:|---:|---:|
| physical | 0.970 | 0.0873 | 0.0125 | 0.832700 | 0.402821 | 0.141039 | 0.375551 |
| thin source | 0.105 | 0.0095 | 0.0125 | 0.045550 | 0.021032 | 0.000384 | 0.019608 |
| high leak | 0.970 | 0.6000 | 0.0375 | 0.220000 | 0.048313 | 0.002022 | 0.044964 |
| near collapse | 0.970 | 0.9000 | 0.0750 | -0.230000 | -0.266500 | 0.000000 | 0.000000 |
| no source | 0.000 | 0.0000 | 0.0125 | -0.037500 | -0.019219 | 0.000000 | 0.000000 |

This is the cleanest derivation-route status. For a real physical click with
strong direct role self-sensitivity, ACV earns `eta_*`. For a thin-source
event it technically earns a floor, but the floor is weak. For near-collapse
or no-source events, ACV fails and branch A does not derive S-floor.

**Hostile ACV review: where the detector model can fail.** ACV is useful
because it is falsifiable. A hard reviewer should attack exactly these points:

1. The source statistic may be too weak. The thin-source receipt has a positive
   floor, but it is so small that downstream constants could be unusable.

2. The source statistic may be redundant with record formation. Then the
   deletion direction can still respond while the role-Fisher matrix loses
   rank. This is not a physical four-role event; it is record bookkeeping with
   a source label pasted on.

3. The antichain statistic may be pure coordinate bookkeeping. It counts for
   ACV only if it is a direct sufficient statistic of the local click, not a
   later slicing convention.

4. The causal-collar statistic may be inherited from the ambient sprinkling
   rather than from the event law. It counts for ACV only when perturbing the
   clicked event changes the collar statistic in the local finite-history law.

5. Schur drift can overwhelm the finite margin. A robust finite vertex is not
   enough; internal refined variables must have a uniformly positive Hessian
   block and bounded coarse-internal coupling.

6. High leakage or near-collapse kills the theorem. The table shows this
   explicitly: when leakage approaches direct self-sensitivity, the diagonal
   and deletion margins disappear.

Thus ACV does not rescue branch A by rhetoric. It survives only for physical
source-record clicks with direct role self-sensitivity, bounded leakage, and
Schur-stable refinement.

**Minimal physical source-record click theorem.** Let a v6 event be generated
by a finite local click law with four sufficient statistics: record, source,
causal collar, and antichain crossing. Assume:

```text
min_i self_i >= sigma_* > 0;
max_i leak_i <= ell_*;
sigma_* > ell_*;
sigma_* u_* > ell_* u^*;
H <= M I;
epsilon_H <= kappa^2 / lambda;
epsilon_J <= beta kappa / lambda;
```

and assume the accumulated Schur errors obey the refinement-margin
inequalities printed above. Then the event has a positive role-response floor:

```text
eta_* >= (sigma_* u_* - ell_* u^*)^2 / M > 0
```

after replacing `sigma_*`, `ell_*`, `u_*`, and `u^*` by their Schur-transported
cofinal bounds. Combining this with the frame/generator comparison and
no-merging refinement theorem gives:

```text
s_* >= j_* sqrt(A c_a eta_*).
```

So branch A is closed for the minimal physical source-record click class.
This is not a theorem of bare ICS. It is a theorem of the v6 physical event
ontology once "division event" means a local source-record click rather than
an untyped causal atom.

**Actual branch-A event-law audit.** The previous theorem is only as strong as
the actual event law. To prove that the concrete branch-A division-event model
satisfies ACV, one must compute the local collar response matrix and the
refinement Schur constants.

Given the clicked finite collar law, turn on four independent role sources and
measure:

```text
J_ij =
d E[T_i] / d theta_j at theta = 0.
```

In an exponential finite-history law this is the role covariance/cumulant
matrix. Define:

```text
sigma = min_i |J_ii|;
ell = max_i sum_{j != i} |J_ij|;
lambda = lambda_min(H_ii);
kappa = ||H_ci||;
epsilon_J = beta kappa / lambda.
```

Let `u` be the common click-deletion direction. The actual event law passes
ACV only if the following two margins are positive cofinally:

```text
sigma - epsilon_J - ell - 3 epsilon_J > 0;
min_i |(J u)_i| - 4 epsilon_J > 0.
```

This is the proof route. The disproof route is equally sharp. Branch A fails
as a derivation if some cofinal refinement has one of:

```text
sigma -> 0;
ell >= sigma;
lambda -> 0;
kappa / lambda not summable;
min_i |(J u)_i| -> 0.
```

These alternatives have direct physical meanings: source-free events,
record/source redundancy, slice bookkeeping, unstable internal refinements, or
a role that does not respond to deletion of the common click.

**Actual event-law audit receipt.** The diagnostic script prints the finite
collar response-matrix test:

| case | sigma | leakage | direct margin | lambda | kappa | eps_J | deletion margin | Schur margin | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| source-click | 0.9700 | 0.0873 | 0.882700 | 0.800 | 0.0200 | 0.0125 | 0.478650 | 0.832700 | PASS |
| weak source | 0.1050 | 0.0873 | 0.017700 | 0.800 | 0.0200 | 0.0125 | 0.046150 | -0.032300 | FAIL |
| source redundant | 0.0291 | 1.0282 | -0.999100 | 0.800 | 0.0200 | 0.0125 | 0.478650 | -1.049100 | FAIL |
| slice bookkeeping | 0.0800 | 1.4200 | -1.340000 | 0.800 | 0.0200 | 0.0125 | 0.478650 | -1.390000 | FAIL |
| bad refinement | 0.9700 | 0.0873 | 0.882700 | 0.800 | 0.2500 | 0.1562 | -0.096350 | 0.257700 | FAIL |

The table shows what "actual" must mean. A source-record click with strong
direct role response and weak internal coupling passes. A weak source has a
positive raw response but fails after Schur drift. A redundant source, a slice
bookkeeping channel, or an unstable refinement fails. Therefore the real v6
branch-A event model is proved only by printing this audit for its actual
finite collar law and showing that the margins have positive cofinal lower
bounds.

**ACV audit theorem.** If the actual branch-A division-event law has a cofinal
finite-collar audit with positive lower bounds for `sigma - ell`,
`lambda`, and `min_i |(J u)_i|`, and a summable upper bound for
`kappa / lambda`, then the actual event model satisfies direct
self-sensitivity, bounded leakage, and Schur-stable refinement. Consequently
the minimal physical source-record click theorem applies and branch A derives
S-floor.

Conversely, if every candidate event law has a cofinal subsequence failing one
of the displayed margins, then branch A cannot derive S-floor from that event
law. It must either adopt the definition route or leave the S-floor open.

**Can ACV be derived from bare ICS?** No, not from order, number, scalar
intensity, covariance, and refinement invariance alone. The obstruction is a
forgetful-map obstruction.

Let `F` be the map:

```text
F: role-complete local click law -> bare causal-set event law
```

which forgets the role statistics `T_record`, `T_source`, `T_causal`, and
`T_slice`, retaining only the causal order, event count, scalar intensity, and
refinement map of the clicked support. ACV is a statement about the role
response matrix `J` and the internal Schur blocks. These data live in the
fiber of `F`; they are not determined by the image `F(P)`.

**Theorem: ACV independence from bare ICS.** There exist finite role-complete
local click laws `P_good` and `P_bad` such that:

```text
F(P_good) = F(P_bad);
P_good satisfies ACV;
P_bad fails ACV.
```

Therefore no theorem using only bare ICS data can prove that the actual
division-event law has direct self-sensitivity, bounded leakage, and
Schur-stable refinement.

Proof. Fix any finite causal collar, for example a four-event diamond, with
the same order, count, scalar rate, and refinement map. Define two
role-complete laws over that same clicked support.

For `P_good`, choose role statistics whose response matrix is diagonally
dominant:

```text
sigma = 0.9700;
ell = 0.0873;
epsilon_J = 0.0125.
```

Then:

```text
sigma - ell - 4 epsilon_J = 0.8327 > 0.
```

For `P_bad`, keep the same clicked support and scalar event law but choose a
role statistic that is source-free, source-redundant, or slice-bookkeeping.
The bare causal-set data are unchanged, because the support, order, count,
and scalar rate have not changed. But the role response matrix changes. In
the source-free case, `sigma = 0`; in the redundant and bookkeeping cases,
`ell >= sigma`. Hence the ACV margin is nonpositive.

Thus ACV is not a consequence of bare ICS. It is a consequence of bare ICS
plus a physical source-record click law whose role statistics are part of the
event ontology.

**Bare-ICS independence receipt.** The diagnostic script prints the finite
fiber counterexample:

| same bare ICS | role law | count | scalar rate | sigma | leakage | Schur margin | ACV |
|---|---|---:|---:|---:|---:|---:|---|
| diamond-4 | source-click | 4 | 1.000 | 0.9700 | 0.0873 | 0.832700 | PASS |
| diamond-4 | source-free | 4 | 1.000 | 0.0000 | 0.0873 | -0.137300 | FAIL |
| diamond-4 | source-redundant | 4 | 1.000 | 0.0291 | 1.0282 | -1.049100 | FAIL |
| diamond-4 | slice-bookkeeping | 4 | 1.000 | 0.0800 | 1.4200 | -1.390000 | FAIL |

The same `diamond-4` causal-set law supports all four role laws. Bare ICS
therefore cannot select ACV.

**Positive derivation theorem from physical ICS.** ACV can be derived if the
primitive is strengthened from bare causal-set atoms to scalar local
source-record clicks. A physical ICS event law consists of:

```text
bare causal-set support;
Lorentz-scalar click intensity;
four local sufficient statistics for record, source, causal collar, and slice;
finite-collar Hessian and role-response matrices;
Schur-stable refinement maps.
```

If these data obey the cofinal inequalities:

```text
sigma_n - ell_n - 4 epsilon_J,n >= m0 > 0;
min_i |(J_n u_n)_i| - 4 epsilon_J,n >= d0 > 0;
lambda_min(H_ii,n) >= lambda0 > 0;
sum_n epsilon_J,n < infinity,
```

then the actual event law satisfies ACV and branch A derives S-floor.

This is the rigorous endpoint. Bare ICS cannot prove ACV because the role
response matrix is forgotten. Physical ICS can prove ACV because the role
response matrix is printed and controlled.

**Completion: scalar source-record detector law.** The remaining way to avoid
mere definition is to give an actual physical click law whose response matrix
is computed. The minimal v6 law has one scalar click mode and four private
role-detector modes:

```text
T_i = C + R_i + E_i.
```

Here `C` is the common local click fact, `R_i` is the private detector channel
for role `i`, and `E_i` is residual leakage. The four roles are:

```text
record;
source;
causal collar;
antichain crossing.
```

Assume the clicked finite collar law has centered second moments:

```text
Var(C) <= c_plus;
Var(R_i) >= p_minus;
sum_{j != i} |Cov(E_i,E_j)| <= e_plus;
|Cov(C,R_i)| = 0;
|Cov(R_i,R_j)| = 0 for i != j;
lambda_min(H_ii) >= lambda0;
epsilon_J <= beta kappa / lambda0.
```

Then the role response matrix obeys:

```text
sigma >= p_minus + Var(C);
ell <= 3 c_plus + e_plus.
```

Hence ACV follows if:

```text
p_minus - 2 c_plus - e_plus - 4 epsilon_J >= m0 > 0;
1/2 (p_minus + 4 c_minus) - e_plus - 4 epsilon_J >= d0 > 0;
sum_n epsilon_J,n < infinity.
```

Proof. In the exponential finite-history law, differentiating the four role
sources gives:

```text
J_ij = Cov(T_i,T_j).
```

The common click mode contributes the same covariance to all entries. The
private role detector contributes only to its own diagonal entry. The residual
term contributes at most `e_plus` to the off-row leakage. Thus the direct
self-sensitivity and leakage bounds are exactly the displayed estimates. The
common click-deletion direction has all four role components, so each row
response to deleting the clicked event is bounded below by the second
displayed inequality. Schur refinement subtracts at most `epsilon_J` per role
source and at most `4 epsilon_J` from the two ACV margins. Summability of
`epsilon_J,n` gives cofinal stability.

This is the maximal derivation route. It derives ACV from a physical detector
law, not from the bare causal set. It also says exactly how the route dies:
if private detector variance is too small, if common-click covariance dominates
the private channels, if residual leakage is large, or if the internal Schur
drift is not summable.

**Source-record detector receipt.** The diagnostic script prints the finite
certificate:

| case | common | private min | eps_J | sigma | leakage | Schur margin | deletion margin | ACV |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| physical SRD | 0.030 | 0.900 | 0.0125 | 0.9300 | 0.0900 | 0.790000 | 0.460000 | PASS |
| common-heavy | 0.300 | 0.200 | 0.0125 | 0.5000 | 0.9000 | -0.450000 | 0.650000 | FAIL |
| weak source | 0.030 | 0.050 | 0.0125 | 0.0800 | 0.0900 | -0.060000 | 0.035000 | FAIL |
| slice-only | 0.030 | 0.000 | 0.0125 | 0.0300 | 0.0900 | -0.110000 | 0.010000 | FAIL |
| leaky residual | 0.030 | 0.900 | 0.0125 | 0.9300 | 0.6600 | 0.220000 | 0.745000 | PASS |
| bad Schur | 0.030 | 0.900 | 0.1562 | 0.9300 | 0.0900 | 0.215000 | -0.115000 | FAIL |

The `leaky residual` row is intentionally included. Leakage is not fatal by
itself; it is fatal only when it consumes the printed margin. The `bad Schur`
row shows the other failure mode: a good local detector law can still fail if
refinement drift destroys the deletion response.

**Exhaustion of the actual-event path.** We have now exhausted the
possibilities:

```text
bare ICS alone:
no, because the role response matrix is forgotten;

physical ICS as source-record detector law:
yes, if private detector response dominates common covariance, residual
leakage, and Schur drift;

definition route:
yes by ontology, if "division event" is defined to mean a role-complete
source-record click;

everything else:
open or false, depending on the audit margins.
```

So branch A is no longer a vague axiom. It is either a theorem of the
source-record detector law, or it is not available from the proposed event
model.

The vertex has earned the role floor only if the following constants have
positive cofinal lower bounds:

```text
m I <= H_n,q <= M I;
J_n,q = D_n,q + R_n,q;
s_min(D_n,q) >= d0;
||R_n,q||_op <= rho d0 with rho < 1;
|(D_n,q u_n,q)_i| >= d0 zeta ||u_n,q|| for every role i;
|(R_n,q u_n,q)_i| <= rho d0 zeta ||u_n,q|| for every role i.
```

The first line is ordinary local generator ellipticity. The next two lines
say the role Jacobian is diagonally dominant in the physical role basis. The
last two lines say the common deletion direction actually has nonzero
components in all four role channels.

**Same-local vertex theorem.** Under the preceding vertex hypotheses:

```text
lambda_min( J_n,q H_n,q^{-1} J_n,q^T )
>= d0^2 (1-rho)^2 / M
```

and:

```text
min_role |ell_role,n,q(u_n,q)|^2 / a_gen,n(q)
>= d0^2 zeta^2 (1-rho)^2 / M.
```

Consequently:

```text
eta_* >= d0^2 zeta^2 (1-rho)^2 / M.
```

Proof. Since `H_n,q <= M I`, we have `H_n,q^{-1} >= M^{-1} I` in the
quadratic-form order. Since `J_n,q = D_n,q + R_n,q`,

```text
s_min(J_n,q) >= s_min(D_n,q) - ||R_n,q||_op
>= d0(1-rho).
```

Therefore the role-Fisher matrix has lower eigenvalue at least
`d0^2(1-rho)^2/M`. For deletion transversality, the componentwise bounds give:

```text
|(J_n,q u_n,q)_i|
>= d0 zeta (1-rho) ||u_n,q||.
```

Also `a_gen,n(q) = <u_n,q,H_n,q u_n,q> <= M ||u_n,q||^2`. Dividing gives the
displayed deletion lower bound.

This theorem is the Feynman route made precise: do not assert indivisibility;
print the local vertex and compute `H`, `J`, `D`, `R`, `zeta`, and `rho`. If
those constants survive refinement, `Local Role-Indivisibility` has been
derived. If any of them vanishes, the route fails.

**Finite same-local-vertex receipt.** The diagnostic script implements this
matrix test. It keeps one local Hessian and varies the role Jacobian.

First, the normal-form diagonal certificate:

| case | diagonal minimum | off-row maximum | DD margin | Fisher minimum | eta_D |
|---|---:|---:|---:|---:|---:|
| good vertex | 0.970000 | 0.087300 | 0.882700 | 0.848135 | 0.215925 |
| source 0.1 | 0.105000 | 0.009450 | 0.095550 | 0.011018 | 0.002530 |
| source zero | 0.000000 | 0.087300 | -0.087300 | 0.000000 | 0.000000 |
| source redundant | 0.029100 | 1.058200 | -1.029100 | 0.000000 | 0.215925 |
| overmixed | 0.970000 | 1.164000 | -0.194000 | 0.333087 | 0.082616 |

The diagonal certificate is sufficient, not necessary. `Overmixed` fails the
certificate but still has positive Fisher minimum and deletion response. For
the theorem we need a certificate that survives refinement, so sufficient
cofinal inequalities are more valuable than accidental finite full rank.

The class-level interval certificate is:

| class | diagonal floor | off ratio | DD margin | Fisher lower bound | eta lower bound |
|---|---:|---:|---:|---:|---:|
| robust | 0.970000 | 0.090000 | 0.882700 | 0.169382 | 0.169382 |
| source 0.1 | 0.105000 | 0.090000 | 0.095550 | 0.001985 | 0.001985 |
| near wall | 0.970000 | 0.970000 | 0.029100 | 0.000184 | 0.000184 |
| overmix | 0.970000 | 1.200000 | -0.194000 | 0.000000 | 0.000000 |
| source zero | 0.000000 | 0.090000 | 0.000000 | 0.000000 | 0.000000 |

This table is the derivation route's current best form. A robust interval
class gives a visible positive floor. A near-wall class is technically
positive but almost degenerate. Overmixing and source-zero fail the sufficient
cofinal certificate. Thus the next physical calculation is not "show generic
rank"; it is "show the actual v6 local vertex lives in a robust interval
class under refinement."

The refinement-transport certificate is:

| case | eps_J | eps_u | DD margin | deletion margin | Fisher lower bound | eta lower bound |
|---|---:|---:|---:|---:|---:|---:|
| robust tail | 0.020 | 0.010 | 0.802700 | 0.390377 | 0.137677 | 0.130251 |
| source-thin | 0.020 | 0.010 | 0.015550 | 0.006230 | 0.000052 | 0.000033 |
| near wall | 0.020 | 0.010 | -0.050900 | -0.044959 | 0.000000 | 0.000000 |
| overmix | 0.020 | 0.010 | -0.274000 | -0.158740 | 0.000000 | 0.000000 |
| source zero | 0.020 | 0.010 | -0.060000 | -0.030600 | 0.000000 | 0.000000 |

This is the first real bridge from finite normal form to cofinal refinement.
It says exactly what must be checked in the actual v6 vertex: its diagonal and
deletion-support margins must dominate coefficient drift. A source-thin
vertex is not forbidden, but it gives a nearly useless floor; a robust vertex
gives a floor stable enough to use downstream.

Second, the full vertex test:

| case | rank | Fisher minimum | eta_D | row floor |
|---|---:|---:|---:|---:|
| good vertex | 4 | 0.848135 | 0.215925 | 0.947955 |
| source 0.1 | 4 | 0.011018 | 0.002530 | 0.105138 |
| source zero | 3 | 0.000000 | 0.000000 | 0.000000 |
| source redundant | 3 | 0.000000 | 0.215925 | 0.947955 |
| overmixed | 4 | 0.333087 | 0.082616 | 1.159663 |

The table separates the two ways a derivation can fail. In `source zero`, the
deletion direction and role frame both fail. In `source redundant`, the common
deletion direction still responds, but the role frame is not full: source has
become disguised record. The `overmixed` row is useful too. Mixing is not
itself fatal; what matters is the actual singular value and deletion
component bounds of the computed vertex.

**Exhaustion of the derivation route.** AV1-AV3 are now closed as finite
normal-form mathematics for the local coincidence class:

```text
AV1: a role-separated local coincidence law prints H, J, and u;

AV2: finite refinement transport is a Schur-complement estimate;

AV3: distance from the bad variety protects the robust interval class.
```

ACV is now closed for the minimal physical-click class:

```text
physical division event =
role-separated local click law
+ direct self-sensitivity dominates leakage
+ Schur refinement errors are summable
=> eta_* > 0
=> S-floor.
```

This is not the suspicious Local Role-Indivisibility axiom. It is an explicit
finite-history identification theorem. The remaining live check is empirical
and model-theoretic: the concrete v6 division-event model used for gravity and
interacting integrability must satisfy the printed direct-sensitivity,
leakage, and Schur-transport inequalities. If it does, branch A derives
S-floor. If it does not, branch A has not derived S-floor from bare v6/ICS.

**Route II: definition by identity criterion.** The definition route does not
try to derive role visibility from a bare causal atom. It changes the
primitive. A v6 physical division event is not:

```text
a causal-set point plus optional record/source/slice labels.
```

It is:

```text
a local finite-history generator whose causal, record, source, and slice
roles are jointly nondegenerate.
```

Formally, define a physical division event to be a refinement-stable local
generator satisfying:

```text
finite local collar;
uniform local Hessian ellipticity;
frame/generator actuality equivalence;
positive role-Fisher lower bound;
positive deletion-direction transversality;
refinement no-merging.
```

Under this definition, Local Role-Indivisibility is not an extra dynamical
axiom. It is the identity criterion for what counts as a physical event. A
bare causal atom that fails the role-Fisher or deletion-transversality test is
not a v6 division event; it is only a kinematic atom in an enlarged
bookkeeping model.

**Definition-route theorem.** If the v6 causal set is, by ontology, a causal
set of physical division events in the above sense, then S-floor follows.

Proof. The definition supplies `eta_D > 0`, the role-Fisher floor, the
frame/generator comparison, and no-merging. The local-frame theorem then gives:

```text
s_* >= j_* sqrt(A c_a eta_D).
```

No further selector is needed. The cost is conceptual: branch B is no longer
an alternative physical ontology; it is an embedding into a larger bookkeeping
space containing nonphysical causal atoms.

**Exhaustion of the definition route.** This route is clean but must be stated
openly. It does not prove branch A from bare ICS. It says v6's primitive is
not bare ICS. The primitive is a causal set of role-complete division events.
That is Einstein's route: define the event by coincidence of its physical
roles. The kill criterion is equally clear. If a theory or experiment needs
physically actual events with a vanishing source, record, causal, or slice
role, this definition is too strong.

**Status after exhausting both routes.** We have not proved S-floor from bare
v6/ICS. We have proved the opposite: bare v6/ICS permits role-covector
pinching and role redundancy. The two honest closures are:

```text
bare v6/ICS + Same-Local Vertex Theorem
=> eta_* > 0
=> w_min > 0
=> S-floor;

or:

v6 physical division event = role-complete local generator
=> eta_* > 0
=> w_min > 0
=> S-floor.
```

The first route is derivational and harder. The second route is ontological
and cleaner, but must be advertised as an identity criterion, not as a theorem
of bare causal order.

**C-floor theorem target: sector-complete receipt frame.** Let `T_n` be the
finite physical tangent space of event laws at the selected law, with Fisher
metric `H_n`. Let `B_n` be the differential of the complete receipt map:

```text
vacuum,
detector,
source,
Tomonaga-Schwinger,
information,
memory.
```

The cofinal receipt-frame theorem is:

```text
there exists c_* > 0 such that ||B_n v|| >= c_* ||v||_{H_n}
for every physical tangent v and all sufficiently large n.
```

Equivalently, the reduced Fisher-Gram matrices have their smallest nonzero
eigenvalues bounded below by `c_*^2`. This theorem is stronger than finite
rank. It says no refinement tail, no sector residue, and no nearly redundant
receipt row can carry a physical tangent direction that all receipts miss.

A useful proof strategy is two-stage. First prove the estimate on a fixed
low-dimensional dangerous subspace spanned by the known candidate degeneracies:
score regraduation, density rescaling, source splitting, TS phase, and memory
width. Then prove a cofinal Riesz-frame estimate for the remaining packet
directions, using the finite-history Fisher metric and the sector-complete
receipt algebra. If the dangerous subspace or the packet tail has a hidden
kernel, `c_*` fails.

The finite adversarial sweep demonstrates exactly this failure: a source row
that becomes detector-redundant drives the Gram lower bound to zero. Therefore
`c_*` must be proved from independent physical receipts, not assumed from the
presence of many rows.

**K-floor theorem target: strict memory-tail crossing.** Let `C_n` be the
selected two-event covariance and let `T_n(beta)` be the normalized two-sided
spectral-tail functional used to read the memory scale. The scale theorem is:

```text
there are beta_min, beta_max, eta, and k_* > 0, independent of n, such that
T_n(beta_n) = eta has one solution beta_n in [beta_min,beta_max] and
|dT_n/dbeta| at beta_n is at least k_*.
```

Together with uniform convergence of `T_n`, this gives the stable scale
estimate:

```text
|beta_n - beta| <= k_*^{-1} sup |T_n - T|.
```

The right way to seek `k_*` is not to fit a quartic memory kernel by taste.
It is to derive the spectral tail from the selected event covariance and then
show that the tail crossing is active and transverse. A possible route is an
information-projection theorem: among positive-type covariance laws satisfying
finite energy, two-sided tail, and same-event source constraints, the entropy
minimizer has an active tail constraint. The KKT multiplier for that active
constraint then supplies the crossing scale. If the constraint is inactive, or
if the spectral tail has a plateau, `beta` remains free.

The finite adversarial tail sweep shows the exact danger. A single-scale tail
has a healthy derivative proxy, while a flat multiscale mixture weakens the
crossing. The cofinal proof must exclude that flattening from the actual
selected covariance, not by decree but by the same event-law variational
problem.

**Attack order.** Prove `s_*` first, because it is the ontology knife edge:
without one-event role support there is no branch A. Prove `c_*` second,
because once support is common the receipt frame must isolate the selected
law. Prove `k_*` third, because the memory scale should be extracted only
after the event support and receipt isolation are already fixed. This order is
the cleanest Einstein/Feynman path: identify the invariant object, print
independent receipts for it, and only then read off the constants.

**Honest status.** This is not yet a proof of branch A. It is the cleanest
branch-A construction target now visible. The hard work is LR1-LR7, especially
the construction of projective finite-history measures, the cofinal response
Fisher-Gram floor `c_*`, the cofinal beta-crossing floor `k_*`, and the
one-event singular floor `s_*`. If those fail, branch B remains the honest
interpretation: `g(s²)`, `gamma`, and `beta` are admissible collapse data, not
derived ISP constants.

#### 5.12 Direct Tomonaga-Schwinger loop attack [PROBE-TARGET]

The fastest way to expose a hidden preferred frame is a spacelike loop. Choose
two spacelike record cells, assign each a scalar threshold operation, and
compose the two operations in opposite orders. A TS-integrable event law must
give no ordering residue:

```math
P_xP_y-P_yP_x=0
```

for spacelike-separated threshold projectors. The finite execution realizes
this as diagonal scalar projectors on two local record cells and obtains zero
commutator norm. That result is intentionally modest. It proves only that a
scalar threshold rule can be TS-compatible in a finite record model.

The full theorem still has to prove three harder statements:

- the threshold operation is built from local field/record operators that are
  microcausal;
- the operation does not smuggle in state-dependent nonlinear Fréchet terms;
- the same joint law is obtained for arbitrary spacelike hypersurface
  interpolations, not just for two finite commuting projectors.

This is the direct TS-integrability target for branch A:

```text
spacelike threshold operations commute because they are scalar local record
operations inside a microcausal indivisible process.
```

If the proof instead requires a preferred slicing, branch A fails.

#### 5.13 One-event synthesis: tying Part I and Part II

The combined Paper 2 should be read as a one-event constraint. Part I and Part
II are not two independent constructions. They must identify the same objective
event:

```math
E_x^{\rm record}
=
E_x^{\rm source}
=
E_x^{\rm causal\ set}
=
E_x^{\rm antichain\ density}.
```

Part I uses the causal-set events to recover spatial adjacency, frame, inverse
metric, and flow-drift. Part II uses the division-event law to recover scalar
rates, memory, vacuum normalization, and source events. A successful v6 theory
cannot keep these as separate ledgers. The geometry event, the detector-record
event, and the stress-energy source event must be the same event under different
readouts.

This gives a clean kill criterion. If the spatial causal set is generated by
one process, while the memory/source flashes are generated by another, then v6
has become a coupled collapse-source model. That may be coherent, but it is
branch B. Branch A requires a single finite-record threshold law whose event
set supports both the Part I geometry and the Part II memory/source receipts.
The S-floor no-go in §5.11 sharpens this: current v6/ICS suppositions can force
one support only as a label/counting statement. To get a theorem, branch A must
add or derive role-faithfulness, namely a uniform deletion effect of each
selected event in the record, source, causal-set, and antichain-density
readouts.

#### 5.14 Hostile branch-A review after the execution

The executions, the no-go theorem, the selector scan, the combined-selector
criterion, and the likelihood-ratio event-law target strengthen Paper 2, but a
hostile reviewer should still attack ten points.

1. **Threshold not derived.** The scalar threshold `S_*` is currently an input.
   A-Scale needs a finite-record theorem that fixes it.
2. **Memory width not derived.** The probe computes `beta^{-1}` from an input
   correlation length. A-Scale needs the finite record channel to select that
   length.
3. **Vacuum rule still partly conventional.** The finite model sets vacuum
   stability to zero. The full theory must prove that the record criterion
   makes vacuum fluctuations non-events without choosing a preferred
   normal-ordering convention.
4. **TS loop is finite and diagonal.** The zero commutator check is a receipt,
   not a field-theoretic theorem. The full proof must handle interacting local
   record operators and arbitrary hypersurface loops.
5. **Gravity-source identity is imposed.** The probe equates source count and
   event count by construction. Branch A needs this identity to follow from the
   same finite-record threshold that defines the causal set. In the language of
   §5.11, it needs role-faithfulness; bare v6/ICS labels do not prove the
   S-floor.
6. **`S_R` candidates are useful but noncanonical.** The three candidate
   stability scores detect records, but each leaves a visible threshold or
   smoothing convention. Branch A needs an internal selection theorem.
7. **The no-go is structural.** Same-first-order data, covariance, monotonicity,
   and refinement invariance are invariant under monotone regraduations of
   `S_R`. They cannot select an interior numerical threshold. Branch A needs an
   extra selector.
8. **Single selectors do not close A-Scale.** Gravity matching, vacuum/detector
   survival, criticality, minimal disturbance, TS fixed point, and information
   units have all been tested at finite level. Each is useful, but none closes
   the threshold and scale alone.
9. **The combined-selector criterion is not satisfied yet.** C1-C6 are now the
   correct theorem target, but no combined selector has proved isolated,
   stable, scale-complete, and one-event in the finite record channel.
10. **The likelihood selector is a theorem target, not closure.** LR1-LR7 name
    the needed finite-measure, response-Gram, memory-scale, and one-event
    theorems. The finite decisive-test script passes a one-event toy branch
    and rejects a decoupled-source branch-B countercase, but until the bounds
    are proved cofinally, `gamma` and `beta` remain underived.

The current branch status is therefore:

```text
A-Form: constrained, but positive-type/tail derivation still open.
A-Scale: finite coherent execution exists, but threshold and scale are not derived.
S_R: three candidates tested; none is canonical yet.
A-Scale no-go: listed axioms cannot select a nontrivial numerical threshold.
A-Scale selectors: tested one by one; no single selector closes A-Scale.
Combined selector: C1-C6 criterion stated; finite probes do not satisfy it yet.
Likelihood selector: finite decisive tests pass in a toy branch; cofinal LR1-LR7 proof open.
TS loop: finite scalar receipt passes, full interacting theorem open.
Part I/II synthesis: criterion stated, identity not proved.
Branch verdict: branch A not closed; branch B remains the honest fallback.
```

That is the correct pressure map. It is also useful: it names exactly which
lemmas would turn v6 from a covariant collapse-compatible ontology into a
derived ISP event theory.

#### 5.15 A/B discriminants

The fork is experimentally and mathematically distinguishable.

| receipt | branch A expectation | branch B expectation |
|---|---|---|
| memory form | forced by TS integrability + record covariance | chosen as a covariant collapse kernel |
| rate `γ` | computed from record-stability threshold | free phenomenological parameter |
| scale `β` | computed from indivisible memory / finite clock scale | free smearing/correlation parameter |
| vacuum events | absent by record criterion | absent by imposed normal-ordering |
| energy production | bounded as a theorem of record covariance | bounded by selected kernel |
| gravity coupling | same division events define geometry/source | added semiclassical flash source |

The quickest falsifier for A is simple: if two inequivalent values of `(γ,β)` give the same ISP first-order
record law and no internal finite-record criterion selects one, then `g(s²)` is not derived. The quickest
support for A would be a detector calculation where the record-stability threshold fixes the same `(γ,β)` that
makes the covariant energy, vacuum, and gravity-source receipts work.

#### 5.16 Einstein and Feynman discipline

Einstein discipline. The memory law must be a consequence of invariant facts. Division events are objective
facts; their order is invariant; no observer's simultaneity convention may enter the correlation. This almost
forces the form `g(s²)`, but it does not fix the scale. A free `β` is a sign that the principle is incomplete.

Feynman discipline. The memory law must be visible in receipts. Compute the same object through detector
clicks, energy injection, two-flash gravity sourcing, vacuum normalization, and foliation loops. If all five
require the same kernel and constants, the kernel is derived. If they merely tolerate a family of kernels, it
is postulated.

#### 5.17 Detector-threshold calculation: the whole branch-A bottleneck

The preceding sections leave one missing calculation. It is not another
selector scan. It is the detector calculation that must fix the same
`gamma` and `beta` used by the energy, vacuum, gravity-source, and
Tomonaga-Schwinger receipts.

The cleanest mathematical form is a likelihood detector. Let `Y_x` be the
finite local detector record in a physical source-record collar. Compare two
local hypotheses:

```text
H_0 = vacuum / no objective record;
H_1 = stable source-record click.
```

Define the canonical detector score:

```text
L_x =
log dP(Y_x | H_1) / dP(Y_x | H_0).
```

Then the threshold is no longer arbitrary. With equal prior cost for false
record and missed record, the Bayes boundary is:

```text
S_* = 0.
```

This is the first real progress beyond the no-go. A monotone regraduation of a
generic score cannot pick an interior threshold, but a log-likelihood ratio has
a canonical zero because it compares two physical hypotheses. The event law is:

```text
E_x = { L_x >= 0 and the positive component is stable under refinement }.
```

From the same detector law, branch A must then compute:

```text
gamma = density of connected positive components of L_x;
beta^{-1} = e^{-1} width of the selected two-event covariance;
vacuum event density = 0;
gravity source count = selected event count;
TS loop residue = 0 for spacelike local threshold operations.
```

**Detector-threshold theorem target.** Branch A is closed only if the actual
physical source-record detector law has a cofinal likelihood-ratio
calculation satisfying:

```text
S_* = 0 is the unique stable detector threshold;
gamma_n -> gamma > 0;
beta_n -> beta in (0,infinity);
energy_bound(gamma_n,beta_n) <= C;
vacuum_events_n = 0;
source_events_n = geometry_events_n;
TS_residue_n -> 0.
```

Moreover `beta` must be isolated. If two inequivalent detector widths give the
same first-order record law and pass the receipts, the memory scale remains
free and branch A is not closed.

**Finite bottleneck receipt.** The diagnostic script adds a likelihood-ratio
threshold calculation. It fixes `S_* = 0` from the detector hypotheses and
then computes the receipts:

| case | S_* | events | gamma | beta inverse | vacuum events | source match | heating | verdict |
|---|---:|---:|---:|---:|---:|---|---:|---|
| canonical | 0.0 | 7 | 0.14583 | 1.7000 | 0 | yes | 0.02993 | PASS |
| same-th wider | 0.0 | 7 | 0.14583 | 2.4000 | 0 | yes | 0.00754 | PASS |
| weak detector | 0.0 | 0 | 0.00000 | 0.0000 | 0 | yes | infinite | FAIL |
| high vacuum | 0.0 | 0 | 0.00000 | 0.0000 | 0 | yes | infinite | FAIL |

The table is decisive in both directions. It shows that the likelihood route
can fix the threshold without an arbitrary `S_*`. But it also shows that
fixing the threshold is not enough: the `same-th wider` row passes the visible
receipts while giving a different `beta`. Therefore the remaining branch-A
core is exactly:

```text
derive the detector width / memory scale from the finite record channel.
```

If the actual detector law fixes the width, branch A can compute `gamma` and
`beta`. If the detector width is a freely variable parameter, v6 has a
covariant Physical-ICS collapse model, not a derived ISP event theory.

#### 5.18 Negative beta theorem under the current receipts

The preceding table already contains the decisive obstruction. It can be
promoted from a warning to a finite theorem.

**Theorem: beta is not selected by the current visible receipts.** The data
consisting of:

```text
likelihood threshold S_* = 0;
selected event count / gamma;
vacuum no-event rule;
source-count equals selected-event count;
finite heating;
finite scalar TS commutator residue;
```

do not determine the memory width `beta^{-1}`. There is a finite
detector-width family with identical values of these receipts and different
`beta`.

**Proof.** Fix seven source-record centers:

```math
t_a\in\{4.0,10.3,16.1,22.7,29.0,35.4,42.2\}
\subset [0,48].
```

For each detector width `ell>0`, define the local log-likelihood trace:

```math
L_\ell(t)
=
\sum_a A\exp\!\left(-{|t-t_a|^4\over \ell^4}\right)-B,
\qquad A=2.40,\quad B=1.00.
```

The Bayes likelihood threshold is `S_*=0` for every `ell`; no threshold
parameter has been moved. For the four widths printed below, direct finite
evaluation gives exactly one positive component of `{L_ell >= 0}` around each
center and no component merger. On those four detector laws:

```text
events = 7;
gamma = 7/48;
vacuum trace = -B < 0, hence vacuum events = 0;
source count = selected event count by the same event support;
finite scalar threshold projectors commute at spacelike separation;
heating beta^4/4 is finite for every listed ell.
```

But the selected local two-event covariance width is `ell`, hence
`beta=ell^{-1}` changes with `ell`. Therefore `beta` is not a function of the
listed receipts. The separated-bump model also has an open stability region of
widths, but the negative theorem needs only the four explicit laws.

The diagnostic script prints an explicit finite family:

| width | S_* | events | gamma | beta inverse | vacuum events | source match | heating | verdict |
|---:|---:|---:|---:|---:|---:|---|---:|---|
| 1.10 | 0.0 | 7 | 0.14583 | 1.1000 | 0 | yes | 0.17075 | PASS |
| 1.30 | 0.0 | 7 | 0.14583 | 1.3000 | 0 | yes | 0.08753 | PASS |
| 1.70 | 0.0 | 7 | 0.14583 | 1.7000 | 0 | yes | 0.02993 | PASS |
| 2.40 | 0.0 | 7 | 0.14583 | 2.4000 | 0 | yes | 0.00754 | PASS |

This proves a negative theorem for the current assumptions. It does not prove
that branch A is impossible. It proves that branch A needs a stronger input
than the visible receipts listed above.

**Beta Lock target.** A positive beta theorem must add a derived mechanism that
removes the width family. The mechanism must be built from the same finite
source-record event law and must select an isolated width cofinally. Two
plausible routes remain:

```text
1. a derived record-transfer operator K_n with an isolated first memory scale;
2. a derived physical cost functional whose information-per-cost optimum is unique.
```

If neither object is derived from the event law, `beta` is a free model
parameter. In that case v6 remains a covariant Physical-ICS collapse theory,
not a pure branch-A derivation of the memory kernel.

#### 5.19 Beta Lock audit: what would have to be computed

The negative theorem says what fails. The positive target is now precise. A
`Beta Lock` is not another selector name; it is a finite calculation with one
of two forms.

**Transfer form.** The event law itself constructs a finite record-transfer
operator:

```math
K_n:\mathcal R_{n,x}\to\mathcal R_{n,x}
```

on the source-record packet, and `K_n` has a cofinally isolated first memory
scale. The selected detector covariance must use the same scale:

```math
\beta_n^{-1}
=
\ell(K_n)
=
\ell_{\rm det}(L_n).
```

**Cost form.** The event law itself constructs the physical cost functional:

```math
C_n(\ell)
=
C_n^{\rm heat}(\ell)
+C_n^{\rm loc/gravity}(\ell),
```

and the information-per-cost objective has a unique stable interior maximizer:

```math
\ell_n=\arg\max_\ell {I_n(\ell)\over C_n(\ell)},
\qquad
\beta_n=\ell_n^{-1}.
```

In either form, the lock is invalid if the operator `K_n` or the cost
functional `C_n` is chosen from a family after the event support has already
been selected. That would merely reintroduce the free width under a new name.

The diagnostic script makes this distinction explicit:

| case | input fixed by event law | beta span | margin | verdict |
|---|---|---:|---:|---|
| support-only | no | 1.3000 | 0.0000 | FAIL |
| derived K toy | yes: transfer K | 0.0000 | 0.2500 | PASS |
| free K family | no | 0.1532 | 0.0000 | FAIL |
| derived cost toy | yes: cost C | 0.0000 | 0.0909 | PASS |
| free cost family | no | 0.2400 | 0.0909 | FAIL |

This is the Einstein/Feynman discipline in finite form. Einstein's demand is
that `beta` be tied to an invariant event-law object, not to a measuring
convention. Feynman's demand is that the same local calculation which produces
detector clicks also produce the scale used by energy, vacuum, gravity-source,
and TS receipts.

**Dichotomy.** Under the current v6/ICS data, `beta` is not derivable from
support-only event information. A positive branch-A theorem must therefore
prove one of:

```text
K-lock: the event law derives K_n with a cofinal spectral isolation margin;
C-lock: the event law derives C_n with a cofinal interior-curvature margin.
```

If both fail, the memory scale is an admissible physical parameter rather than
a derived ISP quantity.

**Minimal source-record channel calculation.** The Feynman test is to write
one concrete detector channel and ask what it actually computes. Let a local
collar record be a finite Poisson count vector with hypotheses:

```math
H_0:\quad \mu_i^{(0)}=B,
\qquad
H_1(\ell):\quad
\mu_i^{(1)}(\ell)
=
B+A\exp\!\left(-{|x_i|^4\over \ell^4}\right).
```

For a supplied `ell`, the likelihood over candidate widths is:

```math
\mathcal L(\ell'\mid \mu(\ell))
=
\sum_i \mu_i(\ell)\log\mu_i(\ell')-\mu_i(\ell'),
```

and the width Fisher information is:

```math
I(\ell)
=
\sum_i {1\over \mu_i(\ell)}
\left({\partial \mu_i(\ell)\over \partial \ell}\right)^2.
```

The diagnostic gives:

| true width | MLE width | Fisher | support events | log-likelihood margin | result |
|---:|---:|---:|---:|---:|---|
| 1.1000 | 1.1000 | 273.972 | 7 | 0.01360 | IDENT |
| 1.7000 | 1.7000 | 177.276 | 7 | 0.00882 | IDENT |
| 2.4000 | 2.4000 | 125.569 | 7 | 0.00626 | IDENT |

This is useful but not closure. It proves that finite records can identify a
width after the event law supplies one. It does not prove that the event law
selects the width. The same event support and the same threshold receipts are
compatible with three distinct supplied widths. Therefore likelihood
identifiability is a branch-B measurement of a parameter unless it is joined to
`K-lock` or `C-lock`.

**Induced transfer-spectrum attack.** Now build the transfer operator directly
from the same supplied source-record width:

```math
K_\ell(i,j)
=
{1\over Z_\ell}
\exp\!\left(-{d(i,j)^4\over \ell^4}\right),
```

with `d(i,j)` the finite collar distance. Let:

```math
g_K(\ell)=1-\lambda_1(K_\ell),
\qquad
\iota_K(\ell)=\lambda_1(K_\ell)-\lambda_2(K_\ell),
\qquad
\beta_K(\ell)=g_K(\ell)^{-1/2}.
```

The finite calculation gives:

| width | support events | gap | isolation | beta_K | verdict |
|---:|---:|---:|---:|---:|---|
| 1.10 | 7 | 0.00430 | 0.01283 | 15.250 | COND |
| 1.30 | 7 | 0.00509 | 0.01519 | 14.013 | COND |
| 1.70 | 7 | 0.00822 | 0.02435 | 11.030 | COND |
| 2.40 | 7 | 0.01656 | 0.04849 | 7.771 | COND |

Each supplied width gives a transfer operator with a positive isolation
margin. But the same visible support family has:

```text
beta_K span = 7.480.
```

Thus the transfer spectrum reads the supplied width. It does not by itself
select the width. `K-lock` becomes a real branch-A theorem only if the finite
event law derives one particular `K_n` before the spectral readout is made.

**Causal-collar transition-frequency attack.** One might object that the
previous `K_ell` still smuggles in a smooth kernel. Remove that choice. Let the
causal collar supply only a nearest-neighbor adjacency graph and define a
row-stochastic transition operator by observed move frequency:

```math
K_p(i,i)=1-2p,
\qquad
K_p(i,i\pm1)=p.
```

The graph, degree, event support, and causal collar are now fixed. Only the
transition frequency `p` changes. On a ring collar with `n=48`, the first
spectral gap and shell isolation are:

```math
g_K(p)=4p\sin^2(\pi/n),
\qquad
\iota_K(p)=4p\{\sin^2(2\pi/n)-\sin^2(\pi/n)\}.
```

The finite receipt is:

| move probability | degree | support events | gap | isolation | beta_K | verdict |
|---:|---:|---:|---:|---:|---:|---|
| 0.05 | 2 | 7 | 0.00086 | 0.00255 | 34.189 | COND |
| 0.10 | 2 | 7 | 0.00171 | 0.00510 | 24.175 | COND |
| 0.20 | 2 | 7 | 0.00342 | 0.01021 | 17.095 | COND |
| 0.35 | 2 | 7 | 0.00599 | 0.01786 | 12.922 | COND |

The same causal collar has:

```text
collar-frequency beta_K span = 21.267.
```

Thus causal adjacency supplies a graph, not a clocked transition law. If the
event law does not fix the transition frequency `p`, the causal-collar
transfer operator also reads a supplied scale rather than deriving one.

#### 5.20 Route 1: spectral-gap beta selection

The first serious way to derive `beta` is to make it a spectral property of
the finite source-record channel, rather than a detector-smearing choice.

Let `K_n` be the finite record-transfer operator on the local physical event
packet after the likelihood threshold has selected the event law. The
spectral route asks for an isolated first nonzero memory shell:

```text
lambda_0,n = 1;
lambda_1,n is the first nontrivial record-transfer shell;
lambda_1,n - lambda_2,n >= k_gap > 0;
1 - lambda_1,n >= g_gap > 0.
```

Then the memory scale is read from the gap:

```text
beta_n = gap_scale(K_n).
```

The precise normalization of `gap_scale` is conventional until the continuum
record channel is specified, but the existence of an isolated first scale is
not conventional. If the first shell is not isolated, or if two different
transfer operators with the same first-order record law give different
isolated first shells, then `beta` remains free.

**Spectral-gap theorem target.** Branch A derives `beta` by this route only if:

```text
K_n is built from the same finite source-record event law;
K_n has a cofinal isolated first nonzero spectral scale;
the selected detector covariance has the same scale;
the scale is stable under refinement.
```

**Spectral-gap receipt.** The diagnostic script tests positive finite transfer
channels with a first spectral shell and a competing second shell:

| case | mode1 | mode2 | gap | isolation | beta gap proxy | verdict |
|---|---:|---:|---:|---:|---:|---|
| isolated | 0.300 | 0.050 | 0.7000 | 0.2500 | 1.1952 | PASS |
| free rescale | 0.450 | 0.050 | 0.5500 | 0.4000 | 1.3484 | PASS |
| near plateau | 0.220 | 0.210 | 0.7800 | 0.0100 | 1.1323 | FAIL |
| no memory | 0.000 | 0.000 | 1.0000 | 0.0000 | 1.0000 | FAIL |

This route is powerful but conditional. `Near plateau` and `no memory` show
the real failure modes. `Free rescale` is subtler: it passes as a spectral
operator but gives a different scale. Therefore spectral-gap selection closes
branch A only when the operator `K_n` itself is derived from the event law.

#### 5.21 Route 2: Fisher-information / cost beta selection

The second route is operational. The detector width is selected as the width
that maximizes real record distinguishability per physical cost. Let `ell` be
the candidate detector width and define:

```text
I(ell) = Fisher information separating H_1 from H_0;
C(ell) = heating cost + localization / gravity blur cost;
Phi(ell) = I(ell) / C(ell).
```

Then `beta` is derived if `Phi` has a unique refinement-stable interior
maximizer:

```text
ell_* = argmax Phi(ell);
beta = ell_*^{-1}.
```

The route fails if the optimum is at a boundary, if there is a plateau of
nearly optimal widths, or if the cost functional contains an externally chosen
blur coefficient. In that case `beta` has merely moved from the detector
kernel to the cost functional.

**Fisher/cost theorem target.** Branch A derives `beta` by this route only if:

```text
I_n and C_n are computed from the same source-record event law;
Phi_n has one interior maximizer ell_n;
the curvature at ell_n has a cofinal lower bound;
ell_n converges under refinement;
the resulting beta_n passes the energy, vacuum, gravity, and TS receipts.
```

**Fisher/cost receipt.** The finite diagnostic scans widths and tests whether
information-per-cost has a stable interior optimum:

| case | blur cost | width_* | objective | near one-percent count | verdict |
|---|---:|---:|---:|---:|---|
| balanced | 0.0500 | 1.7200 | 9.7459 | 11 | PASS |
| weak blur | 0.0050 | 2.5000 | 66.4011 | 16 | FAIL |
| no blur | 0.0000 | 4.0000 | 4096.0000 | 1 | FAIL |
| strong blur | 0.1200 | 1.4800 | 4.6991 | 9 | PASS |

This shows the promise and the danger. A balanced physical cost can select an
interior width. But changing the blur cost changes the selected width. Thus
the Fisher route closes branch A only if the heating and localization costs
are themselves fixed by the finite source-record channel and gravity-source
identity.

**C-lock coefficient-family attack.** The no-free-coefficient target is now
sharp. `C_n(ell)` must not merely contain a localization/gravity term with a
nice optimum. The coefficient of that term must itself be fixed by the same
finite event law. Otherwise the cost route has only moved `beta` from the
detector kernel into the cost functional.

Hold the detector support fixed at the same seven likelihood events and vary
only the blur/localization coefficient. Each row has a conditional interior
optimum, but the optimum moves:

| blur coefficient | support events | width_* | beta_* | objective | near one-percent count | verdict |
|---:|---:|---:|---:|---:|---:|---|
| 0.030 | 7 | 1.8600 | 0.5376 | 14.9187 | 12 | COND |
| 0.050 | 7 | 1.7200 | 0.5814 | 9.7459 | 11 | COND |
| 0.120 | 7 | 1.4800 | 0.6757 | 4.6991 | 9 | COND |
| 0.250 | 7 | 1.3000 | 0.7692 | 2.5489 | 8 | COND |

The coefficient-family span is:

```text
width span = 0.560;
beta span = 0.232.
```

Therefore C-lock is not proved by an interior optimum alone. Branch A must
derive the finite gravity/localization response coefficient from the same
one-event source-record law. If that coefficient is free, the Fisher/cost
route is branch B with a more physical-looking parameter.

**One-event gravity-response coefficient attack.** The natural attempted
reply is that the gravity-source identity fixes the coefficient. It does not,
at least not from support data alone. Source identity fixes which events count
as sources and fixes the source density. It does not automatically fix the
response amplitude by which one event contributes to the localization/gravity
cost.

Write the blur coefficient as:

```text
c_G = kappa_G gamma.
```

Now hold the likelihood event support, source match, and `gamma=7/48` fixed.
Vary only the per-event gravity-response amplitude `kappa_G`:

| kappa_G | gamma | blur coefficient | support events | source match | width_* | beta_* | verdict |
|---:|---:|---:|---:|---|---:|---:|---|
| 0.2057 | 0.14583 | 0.030 | 7 | yes | 1.8600 | 0.5376 | COND |
| 0.3429 | 0.14583 | 0.050 | 7 | yes | 1.7200 | 0.5814 | COND |
| 0.8229 | 0.14583 | 0.120 | 7 | yes | 1.4800 | 0.6757 | COND |
| 1.7143 | 0.14583 | 0.250 | 7 | yes | 1.3000 | 0.7692 | COND |

The response-amplitude family has:

```text
beta span = 0.232.
```

So the missing object is not merely "same source count." It is a finite
one-event response theorem:

```text
kappa_G,n = deletion/source response amplitude of one selected event;
kappa_G,n -> kappa_G in (0,infinity);
c_G,n = kappa_G,n gamma_n;
Phi_n(ell) built with c_G,n has one stable interior maximizer.
```

If `kappa_G` is chosen after the event set is known, C-lock is branch B. If
`kappa_G` is derived from the same local deletion/source response that proves
role-faithfulness, C-lock becomes a real branch-A route.

**Kappa Lock audit.** The preceding attack reduces Beta Lock to a sharper
object:

```text
Kappa Lock = derive kappa_G from the same one-event deletion/source response.
```

In a finite toy normalization, take `kappa_G` to be the positive
deletion/source response margin of the same local role-faithful event law.
This normalization is not claimed as final. The point of the audit is whether
the amplitude is fixed by the event law before the cost optimum is computed.

| case | fixed by event law | ACV | kappa_G | blur coefficient | width_* | beta_* | beta span/drift | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| support-only | no | no | -- | -- | -- | -- | 0.232 | FAIL |
| role-faithful free | no | yes | free | free | -- | -- | 0.232 | FAIL |
| derived kappa toy | yes | PASS | 0.4600 | 0.0671 | 1.6200 | 0.6173 | 0.000 | PASS |
| small Schur drift | yes | PASS | 0.3600 | 0.0525 | 1.7000 | 0.5882 | 0.029 | PASS |
| large Schur drift | yes | PASS | 0.0600 | 0.0088 | 2.2800 | 0.4386 | 0.179 | FAIL |
| split-source amp | no | FAIL | 0.4786 | 0.0698 | 1.6200 | 0.6173 | 0.000 | FAIL |

This table says what the next theorem must prove. Support-only information
does not determine `kappa_G`. Role-faithfulness without a fixed amplitude does
not determine `kappa_G`. A derived deletion/source margin can fix `kappa_G` in
a toy case, and small refinement drift can preserve the selected width. But
large drift destroys the cost selection, and a split-source law can fake a
positive amplitude while failing one-event role faithfulness.

Thus the branch-A closure chain has become:

```text
likelihood threshold -> gamma;
one-event deletion/source response -> kappa_G;
c_G = kappa_G gamma;
Phi(ell; c_G) -> unique ell_*;
beta = ell_*^{-1};
same beta passes energy, vacuum, gravity-source, and TS receipts.
```

If any arrow is supplied from outside the event law, the construction is
branch B.

**Kappa refinement scan.** A pointwise Kappa Lock is still not a cofinal
theorem. The response amplitude must remain stable under refinement. The
finite scan reads `kappa_G,n` from the deletion/source response margin at four
successive refinement levels, then checks whether ACV, cost selection, and the
selected `beta` remain stable:

| case | ACV | cost | kappa_0 | kappa_N | beta_0 | beta_N | beta span | tail drift | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| stable derived | PASS | PASS | 0.4100 | 0.4725 | 0.6024 | 0.6173 | 0.0149 | 0.0000 | PASS |
| large drift | PASS | FAIL | 0.0600 | 0.4600 | 0.4386 | 0.6173 | 0.1787 | 0.0290 | FAIL |
| vanishing kappa | FAIL | FAIL | 0.0000 | 0.1100 | 0.2500 | 0.4854 | 0.2354 | 0.0468 | FAIL |
| split-source | FAIL | PASS | 0.4286 | 0.4911 | 0.6098 | 0.6173 | 0.0075 | 0.0000 | FAIL |

This scan adds an important warning. Convergence of `beta` is not enough. The
split-source row has stable `beta` but fails ACV, so it is branch B. A cofinal
branch-A Kappa Lock must prove all of:

```text
ACV_n passes cofinally;
kappa_G,n -> kappa_G > 0;
c_G,n = kappa_G,n gamma_n;
Phi_n(ell; c_G,n) has a stable interior maximizer;
beta_n -> beta with vanishing tail drift;
split-source response amplitudes are excluded.
```

The positive row is therefore only a receipt. The theorem is the cofinal
stability of one-event deletion response.

#### 5.22 Current verdict after the derivation target is stated

This part proves neither A-Form nor A-Scale as final theorems. It does something weaker but useful:

- it shows the first-order observable must be covariant before memory freedom can help;
- it imports a known covariant-collapse recipe that supplies a local scalar observable, vacuum subtraction,
  and a quartic memory template;
- it shows why frame-colored memory and covariant Gaussian memory fail;
- it makes quartic damping an admissible representative, not a uniqueness claim;
- it isolates the exact remaining pure-ISP task: derive the positive-type two-sided interval memory and its
  constants from finite record formation.
- it executes a finite A-Scale receipt model showing that the five physical receipts and the foliation-loop
  check can be made mutually coherent, while exposing that the threshold and memory width are still inputs.
- it attacks three concrete `S_R` candidates and finds that all are useful but none fixes the threshold and
  scale without an additional principle.
- it proves a regraduation no-go: the currently listed axioms cannot select a nontrivial numerical threshold,
  so branch A needs an additional selector.
- it tests the obvious selectors one by one and finds that none closes A-Scale alone; the strongest path is a
  combined gravity-density, vacuum/detector, and ISP-native information/disturbance selector.
- it states the combined-selector legitimacy criterion C1-C6 and records that the current finite probes do
  not yet satisfy it.
- it proposes the likelihood-ratio event-law selector as the strongest current branch-A construction target:
  a non-Markovian finite-history selector whose closure is exactly LR1-LR7, including a response-Gram
  lower-bound test and a one-event singular-value test.
- it executes those two decisive finite tests in a toy branch-A model and a decoupled branch-B countercase:
  the one-event toy passes, while the split-source countercase fails LR7.
- it isolates the final detector-threshold bottleneck: the likelihood ratio
  can fix `S_* = 0`, but `beta` remains underived unless the detector width is
  selected by the finite source-record channel.
- it proves a negative beta theorem for the current visible receipts: threshold,
  event density, vacuum no-events, source identity, finite heating, and scalar
  TS residue can be held fixed while `beta` varies.
- it states and executes a Beta Lock audit: support-only event information
  fails, while transfer/cost routes become legitimate only when the transfer
  operator or cost functional is derived from the same event law.
- it executes a minimal Poisson source-record channel calculation: records can
  identify a supplied width, but identifiability alone is not a derivation of
  that width.
- it executes a source-record K-lock attack: the induced transfer spectrum has
  isolated scales, but those scales move across a same-support width family.
- it executes a causal-collar K-lock attack: fixed adjacency and event support
  still leave transition-frequency freedom unless the event law fixes the
  clocked transition probabilities.
- it executes two beta-selection attacks: spectral-gap selection and
  Fisher-information/cost selection. Both can select a scale only when their
  operator or cost functional is fixed by the same physical event law.
- it executes a C-lock coefficient-family attack: fixed detector support and
  stable interior cost optima still give different `beta` values when the
  gravity/localization coefficient is varied.
- it executes a one-event gravity-response coefficient attack: source identity
  fixes event support and density, but not the per-event response amplitude
  `kappa_G` needed by C-lock.
- it executes a Kappa Lock audit: support-only data, free amplitudes, large
  refinement drift, and split-source amplitudes fail; only a deletion-response
  amplitude fixed by the same one-event law can conditionally close C-lock.
- it executes a Kappa refinement scan: stable derived response can preserve
  `beta`, but large drift, vanishing response, and split-source response fail.
- it states the remaining cofinal one-event response theorem, proves a positive
  finite OER theorem in the symmetric source-record response class, and runs a
  focused five-case audit: only the fixed, ACV-passing, refinement-stable
  deletion response conditionally supports branch A.
- it investigates the actual-event OER target and finds that strict symmetric
  response is sufficient but not necessary: a stable anisotropic deletion
  vector can still derive `kappa_G` and `beta`, while free amplitudes, drift,
  common-heavy coupling, weak source, and split-source response fail.
- it executes generalized OER bounds: if common click response, private role
  responses, residual leakage, and Schur errors are fixed by the event law and
  converge, `beta` is derived; but a same-support source-amplitude family keeps
  all visible margins positive while moving `kappa_S` and `beta`.
- it executes a full-law `p_source` audit: same support or hidden-source
  extensions leave `d_source` free, but the same full role-complete likelihood
  law fixes `J`, hence fixes `d_source` and `beta`; changes in nominal
  `p_source` with unchanged `J` are decomposition gauge.
- it decides the role-completeness question under the current assumptions:
  reduced support data prove the negative result, namely role-completeness and
  `beta` are not derived; the positive result holds only after the event law is
  strengthened or proved to be full role-complete.
- it tests the one-generator route: a full role generator fixes source response
  and `beta`, but fixing only record, causal, and antichain roles does not
  derive the source row; A-full therefore requires source to be part of the
  generator, not an extension after support selection.
- it sharpens the one-generator route into a full-Gram theorem: the invariant
  object is `J=A A^T`, not the displayed latent coordinates of `A`; orthogonal
  generator gauge changes source-row coordinates without changing `beta`, while
  fixed non-source Gram data still do not determine the source response.
- it defines the four canonical local role statistics and executes the full
  role-Gram derivation gate: only laws that produce record, source, causal, and
  antichain statistics before thresholding derive `J_n`; support-only,
  record-only, geometry-only, post-selected source, nonconvergent full-Gram, and
  weak-source candidates fail.
- it executes the local-operator origin gate: even a stable full Gram fails
  pure branch A if the source row comes from an independent source operator;
  all four roles must be readouts of the same local scalar operator family.
- it executes the microcausal TS gate: local spectral threshold projectors give
  zero spacelike loop residue, while diagonal-only receipts, nonlocal source
  tails, preferred-slice couplings, post-source updates, and nonlinear rules
  fail.
- it executes the nonlinear Fréchet gate: fixed linear local scores pass, while
  nonlinear local scores, adaptive thresholds, hidden nonlinear source terms,
  nonlocal cross terms, and record-only scores fail before the scale theorem.
- it executes a final finite closure ledger: every currently actionable
  branch-A loophole has a finite gate; only finite A-full toy laws survive all
  gates, and those remain conditional on deriving the actual interacting ISP
  event law.
- it executes the physical receipt closure gate: the same derived `beta` must
  pass energy, vacuum, source/geometry identity, TS residue, and convergence
  checks; the finite A-full survivors pass, while missing beta, source mismatch,
  vacuum leakage, nonlocal TS residue, overheating, and nonconvergent beta fail.
- it executes a construction-exhaustion audit against known local-QFT,
  locally covariant stress/RCE, relativistic collapse/flash, causal-set-first,
  and coupled-source routes. Each known route leaves at least one branch-A row
  external unless the full four-role Gram is supplied as an ansatz.
- it runs a first-principles invariant-law guess search. The only surviving
  non-tautological form is an invariant deletion action: a local
  log-Radon-Nikodym or relative-entropy increment for retaining rather than
  deleting one event in its causal collar, whose four deformation derivatives
  are exactly the four roles.
- it executes the seven-step IDA proof/falsification program for finite
  Physical ICS. It proves local deletion and Radon-Nikodym existence under
  finite positivity, verifies invariance/slice-freeness as symmetry gates,
  proves the Fisher/Hessian full-Gram identity for a regular IDA germ, and
  falsifies scalar-only IDA by a same-`A_x(0)`/different-`beta` family.
- it attacks full IDA-germ uniqueness. The same Physical-ICS base data
  `P_n,D_x,A_x(0)` can carry different source rows, role rotations, source
  units, or drifting refinement germs. Thus full IDA-germ is not derived
  unless the four score directions are canonical, labeled, normalized, and
  convergent.
- it follows that residue to a canonical-germ lock. A finite lock works only
  if the deletion-score tangent space has four isolated one-dimensional role
  sectors, Fisher-unit normalization, positive source orientation, and cofinal
  convergence. Degenerate sectors, free units, sign ambiguity, drift, and weak
  source all fail.
- it attacks the origin of the role-sector operator itself. External isolated
  sectors, automorphism-degenerate sectors, Hessian eigenbasis-only sectors,
  source-external sectors, drifting intrinsic sectors, and weak-source sectors
  fail. The final finite residue is an intrinsic Physical-ICS deletion-dynamics
  operator `L_x`.
- it constructs the intrinsic candidate `L_x=G_x^{-1}Q_x`, where `G_x` is the
  IDA Fisher metric and `Q_x` is the deletion Dirichlet form. This derives
  sectors only when the generalized spectrum is isolated, correctly labeled,
  source-positive, and refinement-convergent.
- it follows the label problem to intrinsic signatures. Isolated eigenmodes are
  role-labeled only when Physical ICS derives a full-rank, diagonally dominant,
  refinement-stable signature quartet: record/source/causal/antichain.
- it freezes the signature theorem and decides it. Bare Physical ICS data
  `(order, record measure, deletion)` do not derive the signature quartet. A
  finite unlabeled four-channel collar has the same allowed data but no
  invariant source label, and different source assignments move `beta`.

Therefore the honest status is:

```text
form of g(s²): forced up to the positive-type/tail derivation;
quartic spectral class: admissible and receipt-supported, not unique;
threshold S_*: fixed by likelihood ratio only if the detector hypotheses are part of the event law;
parameter γ: computed after the likelihood threshold is fixed, not yet cofinally derived;
parameter β: not selected by the current visible receipts; a Beta Lock input is required;
beta no-go: finite detector-width family has the same S_*, gamma, vacuum/source/TS receipts and different beta;
Beta Lock target: prove K-lock spectral isolation or C-lock cost curvature from the event law;
source-record channel: beta can be measured from records once supplied, but is not thereby derived;
K-lock attack: induced K_n reads a supplied width; it does not select beta unless K_n itself is fixed;
causal-collar K-lock: fixed adjacency does not fix the transition frequency or beta_K;
spectral-gap beta route: works only with a derived isolated transfer operator;
Fisher/cost beta route: works only with a derived cost functional and unique interior optimum;
C-lock attack: a free gravity/localization coefficient moves the selected beta;
gravity-response bottleneck: source identity fixes count, not kappa_G;
Kappa Lock target: derive kappa_G from the same deletion/source response that proves role-faithfulness;
Kappa refinement target: prove ACV, kappa_G,n convergence, cost stability, and beta_n convergence cofinally;
one-event response theorem: positive finite OER theorem holds in the symmetric source-record class; full interacting cofinal proof open;
actual-event OER investigation: strict symmetry is overstrong; fixed positive deletion-vector convergence is the live cofinal target;
generalized OER bounds: derived event-law bounds close A-Scale conditionally; free source-private response leaves beta physical/free;
full-law p_source audit: same full role-complete law fixes d_source; same support does not;
role-completeness decision: negative under current reduced assumptions; positive only for full role-complete event law;
full role-generator audit: source row not derived from other three roles; A-full requires it inside the generator;
full-generator theorem: fixed/convergent full Gram law fixes beta; support plus non-source Gram does not;
full role-Gram derivation gate: only pre-threshold four-role laws pass; source-absent/post-selected laws fail;
local operator origin gate: independent source operators fail even with stable beta;
microcausal TS gate: local spectral projectors pass; nonlocal tails and preferred slicing fail;
nonlinear Frechet gate: adaptive/nonlinear/state-dependent thresholds fail;
finite closure ledger: only A-full toy laws survive all finite gates; interacting derivation still open;
physical receipt closure: A-full finite survivors pass same-beta receipts; physical pathologies fail independently;
construction exhaustion: known fixed-background/collapse/causal-set/coupled-source routes do not derive the full Gram;
best invariant-law guess: invariant deletion action / modular causal-diamond atom;
IDA proof program: finite positive Physical ICS gives D_x and RN action; scalar-only IDA fails; full IDA germ remains the target;
IDA-germ uniqueness attack: P,D,A_x(0) do not determine the germ; labels, units, and convergence are necessary;
canonical IDA-germ lock: isolated 1D role sectors with Fisher normalization are the surviving theorem target;
role-sector origin attack: L_x must be intrinsic to Physical-ICS deletion dynamics, not externally chosen;
intrinsic L_x construction: L_x=G_x^{-1}Q_x works conditionally; missing Q, degeneracy, wrong labels, drift, and weak source fail;
eigenlabel/signature origin: Physical ICS must derive a stable full-rank signature quartet;
frozen signature theorem: false for bare Physical ICS; marked quartet is extra input, not derivation;
record functional S_R: constrained but noncanonical;
A-Scale threshold: no-go from same-first-order/covariance/monotonicity/refinement alone;
A-Scale selectors: single-selector closure failed in finite probes;
combined selector: criterion stated, not satisfied yet;
likelihood event-law selector: finite decisive tests pass for the toy one-event branch; cofinal proof open;
detector-threshold bottleneck: finite likelihood receipt fixes S_* but exposes β-family freedom;
A/B fork: open only to a new interacting full-Gram theorem; all specified and known construction classes fail.
```

That is progress, but it is not yet a pure ISP derivation of the division-event memory. The remaining theorem
can now be stated without another selector scan.

#### 5.23 The remaining theorem: cofinal one-event response

At this point branch A has one remaining scale theorem. It is not another
selector. It is a deletion-response theorem.

For a selected event `e` in a finite source-record collar, define the four
role responses:

```text
Delta_e R_n = record response when e is removed;
Delta_e S_n = source response when e is removed;
Delta_e C_n = causal-set response when e is removed;
Delta_e A_n = antichain-density response when e is removed.
```

Collect them as:

```text
D_n(e) = (Delta_e R_n, Delta_e S_n, Delta_e C_n, Delta_e A_n).
```

Branch A closes A-Scale only if `D_n(e)` has one common deletion direction,
positive role floors, bounded leakage, bounded Schur refinement drift, and a
convergent source/gravity component:

```text
kappa_G,n = source/gravity component of D_n(e);
kappa_G,n -> kappa_G > 0.
```

Then the cost coefficient and scale are no longer free:

```text
c_G,n = kappa_G,n gamma_n;
ell_n = argmax_ell Phi_n(ell; c_G,n);
beta_n = ell_n^{-1};
beta_n -> beta.
```

This is the remaining theorem:

```text
cofinal one-event response derives kappa_G,
and kappa_G locks C_n,
and C_n locks beta.
```

**Positive finite OER theorem in the symmetric source-record class.** There is
a real positive theorem at finite level. It does not prove the full interacting
theory, but it proves that OER1-OER4 are mutually consistent and sufficient in
the local response class used by the finite receipts.

Let the four roles be:

```text
record, source, causal-set, antichain-density.
```

Let the untransported finite response Jacobian for one selected event have the
symmetric role form:

```math
J_n^0
=
p_n I
+ c_n {\bf 1}{\bf 1}^T,
```

where `p_n` is the private one-event response, `c_n` is the common scalar
click response, and:

```text
p_n -> p,
c_n -> c,
p > 2c >= 0.
```

Let the finite refinement transport from the full source-record collar back to
the four role variables have an ACV error certificate `eps_n -> 0`. The
certificate is used only through the explicit inequalities:

```text
sigma_n >= p_n + c_n - eps_n;
lambda_n <= 3c_n + 3 eps_n;
max_{r,s} |(J_nu)_r-(J_nu)_s| <= 8 eps_n;
kappa_G,n = min_r(J_nu)_r - 4 eps_n.
```

Here `sigma_n` is the least own-role response, `lambda_n` is the greatest
off-role leakage, and `J_n` is the transported role Jacobian. The finite script
uses this same conservative bookkeeping: one Schur error is subtracted from the
own-role floor, three from the off-role leakage, and four from the common
deletion response.

Use the common deletion direction:

```math
u={1\over2}{\bf 1}.
```

Then OER1-OER4 hold.

**OER1: common deletion direction.** Before refinement transport,

```math
(p_n I+c_n{\bf 1}{\bf 1}^T)u
=
{p_n+4c_n\over2}{\bf 1}.
```

The deletion response is exactly common across the four roles. After transport
the certified row spread is at most `8 eps_n`, hence the response direction
converges to the common one-dimensional deletion line.

**OER2: positive role floors and bounded leakage.** The diagonal role response
has floor:

```text
sigma_n >= p_n + c_n - eps_n,
```

while the off-role leakage is bounded by:

```text
lambda_n <= 3c_n + 3 eps_n.
```

Therefore:

```text
sigma_n - lambda_n >= p_n - 2c_n - 4 eps_n.
```

Since `p>2c`, this margin is positive for all sufficiently large refinements.

**OER3: Schur-stable refinement transport.** Eliminating internal collar
variables perturbs the role Jacobian and Hessian by the Schur bounds already
used in the ACV audit. The transported role margin is certified by:

```text
m_n = p_n - 2c_n - 4 eps_n.
```

Since `m_n -> p-2c > 0`, ACV survives cofinally. This is the precise content
of Schur stability here: internal variables may renormalize the collar, but
their transported error cannot close the role gap.

**OER4: convergent source/gravity response.** Define the finite per-event
gravity/source response amplitude by the certified transported deletion
margin:

```math
\kappa_{G,n}
=
\min_r (J_nu)_r - 4\epsilon_n.
```

In the symmetric source-record class,

```math
\left|
\min_r (J_nu)_r
-
{p_n+4c_n\over2}
\right|
\le 4\epsilon_n.
```

Therefore:

```math
\left|
\kappa_{G,n}
-
{p_n+4c_n\over2}
\right|
\le 8\epsilon_n,
```

and:

```math
\kappa_{G,n}
\longrightarrow
{p+4c\over2}
>0.
```

Thus `kappa_G` is not fitted in this finite class. It is the limiting
one-event deletion response.

Now insert this into the cost route:

```text
c_G,n = gamma_n kappa_G,n.
```

For the finite Fisher/cost proxy used in the receipts,

```math
\Phi_n(\ell)
=
{\ell\over {1\over 4\ell^4}+c_{G,n}\ell^2}
=
{4\ell^5\over 1+4c_{G,n}\ell^6}.
```

For `c_G,n>0`,

```math
{d\Phi_n\over d\ell}
=
{4\ell^4(5-4c_{G,n}\ell^6)\over(1+4c_{G,n}\ell^6)^2}.
```

Also `Phi_n(ell) -> 0` as `ell -> 0+` and as `ell -> infinity`. The derivative
is positive before the critical point and negative after it, so `Phi_n` has
exactly one positive critical point and it is the global maximum:

```math
\ell_n^6={5\over4c_{G,n}},
\qquad
\beta_n=\ell_n^{-1}
=
\left({4c_{G,n}\over5}\right)^{1/6}.
```

Since `gamma_n -> gamma` and `kappa_G,n -> kappa_G>0`, the selected scale
converges:

```math
\beta_n
\longrightarrow
\left({4\gamma\kappa_G\over5}\right)^{1/6}.
```

This proves the finite positive implication:

```text
OER1-OER4 + the stated cost proxy => derived beta.
```

The executable certificate for the symmetric source-record response class is:

| common | private | deletion spread | role margin | eps_J,N | kappa_N | Schur_N | beta grid | beta exact | verdict |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0.030 | 0.900 | 0.000000 | 0.840000 | 0.0094 | 0.4725 | 0.8025 | 0.6173 | 0.6169 | PASS |

This is the strongest positive result currently in the paper. It proves OER
inside a finite role-faithful source-record response class. It does **not**
prove that the actual interacting ISP event law has this response form. That
is the remaining full branch-A theorem.

The focused diagnostic script:

```text
code/v6_p2k_one_event_response.py
```

tests exactly the five cases that can fool the argument:

| case | fixed | ACV | cost | sigma | leak | kappa_N | beta_N | beta span | tail drift | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| support-only label | no | FAIL | FAIL | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2316 | 0.2316 | FAIL |
| free amplitude | no | PASS | PASS | 0.9300 | 0.0900 | 0.4725 | 0.6173 | 0.0149 | 0.0000 | FAIL |
| honest one-event | yes | PASS | PASS | 0.9300 | 0.0900 | 0.4725 | 0.6173 | 0.0149 | 0.0000 | PASS |
| large drift | yes | PASS | FAIL | 0.9300 | 0.0900 | 0.4600 | 0.6173 | 0.1787 | 0.0290 | FAIL |
| split-source | no | FAIL | PASS | 0.0291 | 1.0282 | 0.4911 | 0.6173 | 0.0075 | 0.0000 | FAIL |

The audit separates four tempting false closures:

- support-only labels do not give a response amplitude;
- a role-faithful response with a free amplitude does not derive `kappa_G`;
- large refinement drift can keep ACV alive while breaking cost stability;
- split-source response can produce a stable-looking `beta` while failing ACV.

The only finite positive row is the honest one-event case: fixed amplitude,
ACV, cost stability, small beta span, and vanishing tail drift. That row is
not a proof. It names the proof:

```text
prove cofinally that one selected event has one stable deletion response.
```

If this theorem fails, branch A is not merely incomplete. A-Scale belongs to
branch B: a covariant Physical-ICS collapse/source theory with free physical
scale constants. If the theorem succeeds, the branch-A closure chain is:

```text
likelihood threshold -> gamma;
cofinal one-event deletion response -> kappa_G;
c_G = kappa_G gamma;
C-lock -> beta;
same beta passes energy, vacuum, gravity-source, and TS receipts.
```

#### 5.24 Full OER investigation: strict symmetry is not the real target

Section 5.23 proved the cleanest positive theorem in the symmetric response
class:

```math
J_n^0=p_n I+c_n{\bf 1}{\bf 1}^T.
```

That class is useful because every constant can be read off explicitly. But a
hostile reviewer should immediately ask whether the actual interacting
source-record law has to be exactly role-symmetric. It probably does not. The
record, source, causal-collar, and antichain-density readouts need not have the
same private detector variance. Exact equality of all four private responses
would require an extra role-isotropy theorem.

The correct object is slightly weaker and more physical. Let:

```math
d_n=J_nu_n,
```

where `u_n` is the deletion direction of one selected event and `J_n` is the
transported four-role response matrix. The actual-event OER target is:

```text
OER1': d_n -> d with every component of d positive;
OER2:  sigma_n - lambda_n - 4 eps_n >= m0 > 0;
OER3:  eps_n -> 0 with Schur-stable refinement;
OER4': kappa_G,n = (d_n)_source - 4 eps_n -> kappa_G > 0.
```

This is enough. If also `gamma_n -> gamma > 0`, then:

```text
c_G,n = gamma_n kappa_G,n -> gamma kappa_G > 0,
```

and the same Fisher/cost calculation gives:

```math
\beta_n
\longrightarrow
\left({4\gamma\kappa_G\over5}\right)^{1/6}.
```

So branch A does not need the equal deletion ray. It needs a deletion vector
that is fixed by the event law, positive in all four roles, Schur-stable, and
convergent in its source/gravity component.

**Generalized positive OER theorem.** Suppose a finite interacting
source-record event law has transported role matrices `J_n`, deletion vectors
`u_n`, Schur errors `eps_n`, and detector rates `gamma_n` satisfying:

```text
d_n = J_n u_n -> d;
min_i d_i > 0;
sigma_n - lambda_n - 4 eps_n >= m0 > 0;
eps_n -> 0;
gamma_n -> gamma > 0.
```

Then OER1'-OER4' hold, the per-event gravity/source response is derived by:

```text
kappa_G = d_source,
```

and the C-lock proxy selects:

```math
\beta
=
\left({4\gamma d_{\rm source}\over5}\right)^{1/6}.
```

Proof. OER1' is the assumed convergence of the deletion vector. OER2 and OER3
are the displayed ACV and Schur margins. OER4' follows because:

```text
|kappa_G,n - d_source| <= |(d_n)_source-d_source| + 4 eps_n -> 0.
```

The cost objective is the one already differentiated in §5.23, so it has one
interior global maximizer. This proves the scale formula.

**Strict symmetry independence.** Strict symmetric OER is not forced by ACV or
by the scalar source-record detector law. Take:

```math
J_n^0
=
\operatorname{diag}(p_{1,n},p_{2,n},p_{3,n},p_{4,n})
+c_n{\bf 1}{\bf 1}^T,
```

with:

```text
p_{i,n} -> p_i > 0;
p_i - 2c > 0 for every i;
not all p_i are equal.
```

Then the ACV role margins can be positive cofinally, and:

```math
d_n
=
{1\over2}(p_{1,n}+4c_n,\ldots,p_{4,n}+4c_n)
\longrightarrow
{1\over2}(p_1+4c,\ldots,p_4+4c),
```

which has every component positive. Thus generalized OER holds. But the
deletion response is not the equal role ray unless all `p_i` are equal.
Therefore exact symmetry is an additional role-isotropy theorem, not a
consequence of ACV alone.

The focused actual-event diagnostic is:

```text
code/v6_p2l_oer_actual_event_investigation.py
```

It tests strict symmetry against generalized OER:

| case | fixed | strict | genOER | ACV | cost | sym spread | dir drift | kappa_S | beta_N | beta span | Schur_N | verdict |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| strict symmetric | yes | PASS | PASS | PASS | PASS | 0.0000 | 0.0000 | 0.4725 | 0.6169 | 0.0144 | 0.8025 | PASS |
| stable anisotropic | yes | FAIL | PASS | PASS | PASS | 0.1000 | 0.0036 | 0.4725 | 0.6169 | 0.0144 | 0.7225 | PASS |
| anisotropic free | no | FAIL | FAIL | PASS | PASS | 0.1000 | 0.0036 | 0.4725 | 0.6169 | 0.0144 | 0.7225 | FAIL |
| source drift | yes | FAIL | FAIL | PASS | PASS | 0.3300 | 0.0986 | 0.2025 | 0.5357 | 0.0668 | 0.2625 | FAIL |
| common-heavy | yes | FAIL | FAIL | FAIL | PASS | 0.0000 | 0.0000 | 0.6625 | 0.6527 | 0.0107 | -0.4375 | FAIL |
| weak source | yes | FAIL | FAIL | FAIL | FAIL | 0.4250 | 0.0344 | 0.0475 | 0.4207 | 0.1707 | -0.0475 | FAIL |
| split-source | no | FAIL | FAIL | FAIL | PASS | 0.0000 | 0.0000 | 0.4911 | 0.6209 | 0.0139 | -1.0366 | FAIL |

The table changes the theorem target. The symmetric row proves the clean
sufficient class. The stable anisotropic row proves that exact role equality is
not necessary. The anisotropic-free row shows that a stable-looking response
still fails if the amplitudes are not fixed by the event law. The source-drift
row shows that ACV can remain alive while `beta` drifts. The common-heavy row
has a positive deletion response but fails ACV because off-role common
covariance overwhelms private role response. The weak-source row fails both
Schur margin and cost stability. The split-source row can fake a stable
source amplitude while failing one-event ACV.

The actual interacting branch-A theorem is therefore:

```text
derive a fixed positive deletion vector d from the local event law,
not necessarily an exactly equal role ray.
```

If a role-isotropy theorem later proves `d` is proportional to `(1,1,1,1)`,
then the symmetric §5.23 theorem applies as a special case. If no such
isotropy exists, branch A can still close A-Scale through generalized OER,
provided the source component of `d` is derived and cofinally stable. If the
source component is free or drifting, branch A fails A-Scale and the theory is
branch B with a physical collapse scale.

#### 5.25 Generalized OER bounds: what would force `d_source`

The preceding section identifies the real target but does not yet force it.
This section asks what finite local event-law data are sufficient to derive
the source component of the deletion vector.

Use the scalar source-record normal form:

```text
T_i = C + R_i + E_i,
```

where `C` is the common scalar click, `R_i` is the private detector response
for role `i`, and `E_i` is residual leakage. Let:

```math
J_n
=
\operatorname{diag}(p_{1,n},p_{2,n},p_{3,n},p_{4,n})
+c_n{\bf 1}{\bf 1}^T
+B_n,
```

with:

```text
c_n = common click covariance;
p_i,n = private role response;
max_i sum_{j != i} |B_ij,n| <= 3 r_n;
|(B_n u)_i| <= 3 r_n / 2;
eps_n = Schur role-source error.
```

For the common deletion vector `u=(1/2)1`, the conservative finite bounds are:

```text
sigma_n - lambda_n - 4 eps_n
>=
p_min,n - 2 c_n - 3 r_n - 4 eps_n;

(J_n u)_source - 4 eps_n
>=
1/2 p_source,n + 2 c_n - 3/2 r_n - 4 eps_n.
```

Therefore the actual event law forces generalized OER if it proves:

```text
p_min,n - 2 c_n - 3 r_n - 4 eps_n >= m0 > 0;
1/2 p_source,n + 2 c_n - 3/2 r_n - 4 eps_n >= s0 > 0;
c_n -> c;
p_i,n -> p_i;
B_n u -> b;
eps_n -> 0;
gamma_n -> gamma > 0.
```

Then:

```math
d_n=J_nu
\longrightarrow
d
=
{1\over2}(p_1,\ldots,p_4)
+2c{\bf 1}
+b,
```

and:

```math
d_{\rm source}
=
{1\over2}p_{\rm source}
+2c
+b_{\rm source}
>0.
```

The selected scale is:

```math
\beta
=
\left({4\gamma d_{\rm source}\over5}\right)^{1/6}.
```

This is a positive theorem, but it is conditional in exactly the right place.
It does not ask for role-isotropy. It asks for a derived private source
response, derived residual leakage, and Schur-stable refinement.

**Same-support source-amplitude obstruction.** If `p_source,n` is not fixed by
the event law, generalized OER still does not close A-Scale. Hold the event
support, likelihood threshold, common click, residual leakage, and Schur error
fixed, and vary only `p_source`. The ACV and source bounds can all remain
positive while `d_source` and `beta` move.

The diagnostic script:

```text
code/v6_p2m_generalized_oer_bounds.py
```

prints the finite bounds:

| case | fixed | ACV | cost | ACV lower | source lower | kappa_S | beta_N | beta span | direction drift | Schur_N | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| derived generalized | yes | PASS | PASS | 0.5720 | 0.3780 | 0.4770 | 0.6179 | 0.0087 | 0.0040 | 0.7135 | PASS |
| role isotropic | yes | PASS | PASS | 0.7400 | 0.4100 | 0.4725 | 0.6169 | 0.0144 | 0.0000 | 0.8025 | PASS |
| free source amp | no | PASS | PASS | 0.6510 | 0.4055 | 0.4770 | 0.6179 | 0.0143 | 0.0036 | 0.7135 | FAIL |
| source drift | yes | PASS | PASS | 0.2435 | 0.1930 | 0.2020 | 0.5354 | 0.0681 | 0.0979 | 0.2435 | FAIL |
| common dominated | yes | FAIL | PASS | -0.3600 | 0.5200 | 0.6425 | 0.6493 | 0.0110 | 0.0000 | -0.2975 | FAIL |
| weak source | yes | FAIL | FAIL | -0.1190 | -0.0195 | 0.0520 | 0.4271 | 0.1771 | 0.0323 | -0.0565 | FAIL |
| residual drift | yes | PASS | PASS | 0.1425 | 0.1425 | 0.8025 | 0.6739 | 0.0714 | 0.0000 | 0.1425 | FAIL |

The same-support source-amplitude family is sharper:

| p_source | ACV lower | source lower | kappa_S | beta | ACV | cost |
|---:|---:|---:|---:|---:|---|---|
| 0.350 | 0.2435 | 0.1930 | 0.2020 | 0.5354 | PASS | PASS |
| 0.550 | 0.4435 | 0.2930 | 0.3020 | 0.5726 | PASS | PASS |
| 0.750 | 0.6435 | 0.3930 | 0.4020 | 0.6005 | PASS | PASS |
| 0.950 | 0.7135 | 0.4930 | 0.5020 | 0.6232 | PASS | PASS |
| 1.200 | 0.7135 | 0.6180 | 0.6270 | 0.6467 | PASS | PASS |

The family has:

```text
source kappa span = 0.4250;
beta span = 0.1113.
```

So the investigation has a precise endpoint. Branch A can close A-Scale by
deriving the common/private/residual/Schur bounds from the physical event law.
But if the source-private response is a free detector amplitude, then even
generalized OER is branch B: `beta` remains a physical collapse parameter.

The next proof is therefore not "prove symmetry." More invariantly, it is not
even "prove the label `p_source`" unless the normal-form decomposition has
already been fixed. It is:

```text
prove the full role-complete event law fixes J_n and hence fixes
d_source,n=(J_n u_n)_source, because source response is a sufficient
statistic of the same finite local click that defines the record, causal
collar, and antichain-density roles.
```

When the decomposition `J_n=diag(p_i,n)+c_n 11^T+B_n` is itself derived,
this is equivalently a theorem fixing `p_source,n`, `c_n`, and the source row
of `B_n`. Without that decomposition, `d_source` is the invariant object.

#### 5.26 Full-law audit: `p_source` label versus `d_source` invariant

The strongest counterexample to branch A would be two laws with the same full
role-complete local likelihood law and different `d_source`. That
counterexample cannot exist once "full law" includes the four role sufficient
statistics.

Let the local clicked law include the joint finite distribution of:

```text
T_record, T_source, T_causal, T_antichain.
```

In the exponential finite-history law, the role response matrix is the
cumulant/Jacobian:

```math
J_{ij}
=
{\partial \mathbb E[T_i]\over\partial\theta_j}\bigg|_{\theta=0}
=
\operatorname{Cov}(T_i,T_j\mid click).
```

The deletion response is:

```math
d=Ju.
```

Therefore:

```text
same full role-complete law => same J => same d_source => same beta.
```

This is almost tautological, but it is the tautology branch A needs. It says
where the source scale lives. It lives in the full role-complete local law, not
in the support alone.

There is one subtlety. The normal-form symbol `p_source` can be a decomposition
coordinate. If two decompositions give the same `J`, they give the same
`d_source` and the same `beta`; the nominal change in `p_source` is then gauge,
not physics. The invariant question is whether `J` changes.

The diagnostic script:

```text
code/v6_p2n_full_law_p_source_audit.py
```

prints the finite audit:

| case | support | full law | role full | ACV | p span | kappa span | beta span | verdict |
|---|---|---|---|---|---:|---:|---:|---|
| same support only | yes | no | yes | PASS | 0.850 | 0.4250 | 0.1113 | FAIL |
| identical full law | yes | yes | yes | PASS | 0.000 | 0.0000 | 0.0000 | PASS |
| decomposition gauge | yes | yes | yes | PASS | 0.850 | 0.0000 | 0.0000 | PASS |
| hidden source ext | yes | no | no | PASS | 0.850 | 0.4250 | 0.1113 | FAIL |

The result is decisive in a narrow sense:

```text
same support does not fix beta;
same reduced receipts do not fix beta;
same full role-complete law fixes beta;
hidden-source extensions do not count as full laws;
nominal p_source variation is harmless only when J is unchanged.
```

Thus the remaining branch-A proof is not to rule out all same-support
counterfamilies. Those counterfamilies are real. The remaining proof is to show
that the actual v6 event law is role-complete in the strong sense: the source
statistic is not an optional extension, but part of the full local likelihood
law that defines the selected event. If that is true, `d_source` is no longer a
free parameter. If the source statistic is added after the record/causal event
is selected, branch A fails and the model is branch B.

#### 5.27 Decision theorem: role-completeness is not derived from reduced data

The request at this point is binary: prove role-completeness or prove its
opposite. The finite answer is:

```text
role-completeness is not derivable from the current reduced event data.
```

The positive theorem is also true, but only under stronger assumptions:

```text
full role-complete event law => J fixed => d_source fixed => beta fixed.
```

The current reduced data are weaker. They include event support, threshold
selection, scalar rate, same causal collar, and the visible receipts. They do
not include the joint role distribution of:

```text
T_record, T_source, T_causal, T_antichain.
```

Therefore they do not determine the role cumulant matrix `J`.

**Negative theorem.** Let `R` be the reduced event law that remembers the
selected support, likelihood threshold, scalar event rate, causal collar, and
visible ACV/cost pass/fail receipts, but forgets the full role-complete
likelihood law. Then `R` does not determine `d_source=(Ju)_source`, hence does
not determine `beta`.

Proof. Fix the same seven-click support, the same threshold, the same common
click, the same residual leakage, and the same Schur error. Vary only the
source row of the role cumulant matrix in a family that preserves positive ACV
and cost margins. The finite family in §5.25 has:

```text
p_source in {0.350,0.550,0.750,0.950,1.200};
ACV = PASS for every row;
cost = PASS for every row;
source kappa span = 0.4250;
beta span = 0.1113.
```

All rows have the same reduced support data, but different `d_source` and
different `beta`. Thus no function of the reduced event law can compute
`beta`. Role-completeness is independent of the reduced data.

**Positive theorem.** If the event law is instead the full role-complete
likelihood law, then it includes the joint distribution of the four role
sufficient statistics. In the exponential finite-history normal form this
fixes:

```math
J_{ij}
=
\operatorname{Cov}(T_i,T_j\mid click).
```

Thus it fixes:

```math
d=Ju,
\qquad
d_{\rm source}=(Ju)_{\rm source},
```

and, once `gamma` is fixed by the likelihood threshold:

```math
\beta
=
\left({4\gamma d_{\rm source}\over5}\right)^{1/6}.
```

So the positive theorem is tautological but legitimate: a full role-complete
law fixes the source deletion component because that component is a cumulant of
the law. The reduced law does not.

The finite decision script is:

```text
code/v6_p2o_role_completeness_decision.py
```

It prints:

| theorem | assumptions | beta determined? | beta span | conclusion |
|---|---|---|---:|---|
| negative | reduced support law | no | 0.1113 | role-completeness independent |
| positive | full role law | yes | 0.0000 | `J` fixes `d_source` |
| gauge | same `J`, relabeled `p_source` | yes | 0.0000 | label change is not physics |
| negative | hidden source extension | no | 0.1113 | source added too late |

This proves the opposite under the current reduced assumptions. Branch A is
not dead as a theory, but A-Scale is not derived from the current reduced
event law. To revive branch A, v6 must prove or adopt:

```text
physical division event = full role-complete local likelihood law.
```

If that equality is merely stipulated, branch A becomes a sharpened ontology
postulate. If it is derived from the interacting ISP event law, branch A has a
real closure path. Without it, the honest verdict is branch B for the scale:
`beta` is a physical collapse/source parameter.

#### 5.28 One-generator audit: source is not forced by the other three roles

There remains one possible escape. Perhaps the source statistic is not an
extra role at all. Perhaps it is forced by the same local generator that
already produces record, causal-collar, and antichain-density roles.

Test this directly. Let a clicked local generator have a latent finite feature
vector `Z` with:

```text
Cov(Z)=I,
```

and let the four role sufficient statistics be:

```math
T=A Z.
```

Then:

```math
J
=
\operatorname{Cov}(T)
=
A A^T.
```

If the full generator matrix `A` is part of the event law, up to latent
coordinate gauge, then the response matrix `J`, the deletion component
`d_source`, and `beta` are fixed. This is the A-full positive route.

But if only the other three rows of `A` are fixed:

```text
record row;
causal-collar row;
antichain-density row;
```

then the source row can vary while those three roles, the support, and the
visible ACV/cost receipts remain fixed. Therefore source response is not
derived from the other three roles. It must be part of the full generator.

The finite script:

```text
code/v6_p2p_full_role_generator_audit.py
```

prints:

| case | same 3 roles | full generator | role full | ACV | source span | kappa span | beta span | verdict |
|---|---|---|---|---|---:|---:|---:|---|
| same full generator | yes | yes | yes | PASS | 0.0000 | 0.0000 | 0.0000 | PASS |
| three-role source sweep | yes | no | yes | PASS | 0.6000 | 0.5550 | 0.1226 | FAIL |
| hidden source row | yes | no | no | PASS | 0.6000 | 0.5550 | 0.1226 | FAIL |
| convergent generator | no | no | yes | PASS | 0.0300 | 0.0315 | 0.0060 | PASS |

This proves the final finite distinction:

```text
same full generator => source response fixed;
same three non-source roles => source response not fixed;
hidden source row => branch B;
convergent full generator family => A-full remains viable.
```

Thus the opposite is proved for the reduced and three-role data. Record,
causal, and antichain readouts do not force the source row. Branch A can close
only as A-full:

```text
the source row is a primitive or derived row of the same local generator that
selects the event.
```

If the interacting ISP construction derives such a generator, A-full can still
derive `beta`. If not, the scale belongs to branch B.

#### 5.29 Full-generator theorem: the invariant object is the Gram law

The preceding section used the phrase "full generator," but the literal matrix
`A` is not itself invariant. A change of latent feature basis

```math
A\mapsto A O,
\qquad
O O^T=I,
```

changes the displayed source-row coordinates while leaving:

```math
J
=
A A^T
```

unchanged. Therefore the exact branch-A object is not a coordinate choice for
`A`. It is the full role-response Gram law:

```text
J_n = Cov(T_record,T_source,T_causal,T_antichain | click).
```

This gives the clean theorem.

**Full-generator theorem target.** Suppose the interacting event law determines
a role-complete local Gram law `J_n` on the four event readouts, with:

```text
J_n -> J;
d_n = J_n u -> d;
d_source > 0;
ACV margin and cost curvature stay positive.
```

Then `gamma_n` is fixed by the likelihood threshold and:

```math
\beta_n
=
\left({4\gamma_n(d_n)_{\rm source}\over5}\right)^{1/6}
\longrightarrow
\left({4\gamma d_{\rm source}\over5}\right)^{1/6}.
```

The proof is short. `J_n` is part of the same local event law, so `d_n=J_n u`
is fixed. The source component is positive and convergent by hypothesis. The
C-lock/OER cost map is continuous on the positive-margin region, hence the
selected width and `beta_n` converge. Orthogonal changes of latent coordinates
leave `J_n`, `d_n`, and `beta_n` invariant.

The opposite is also sharp. Fixing the support and the non-source Gram block:

```text
record;
causal-collar;
antichain-density;
```

does not fix `J_n`. The source row and source column can vary while that
non-source block is unchanged. Since:

```math
d_{\rm source}
=
(J_n u)_{\rm source},
```

`beta` can move. Thus a theorem based on support plus three readouts cannot
close A-Scale.

The finite audit is:

```text
code/v6_p2q_full_generator_theorem.py
```

It prints:

| case | role complete | support | ACV | J span | non-source J span | A source span | kappa span | beta span | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| orthogonal gauge | yes | yes | PASS | 0.0000 | 0.0000 | 0.7763 | 0.0000 | 0.0000 | PASS |
| same full Gram | yes | yes | PASS | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | PASS |
| three-role only | yes | yes | PASS | 1.0200 | 0.0000 | 0.6000 | 0.5550 | 0.1226 | FAIL |
| hidden source | no | yes | PASS | 1.0200 | 0.0000 | 0.6000 | 0.5550 | 0.1226 | FAIL |
| convergent full Gram | yes | yes | PASS | 0.0561 | 0.0384 | 0.0300 | 0.0315 | 0.0060 | PASS |
| nonconvergent Gram | yes | yes | PASS | 1.0200 | 0.0000 | 0.6000 | 0.5550 | 0.1226 | FAIL |
| weak source row | yes | yes | FAIL | 0.0020 | 0.0000 | 0.0200 | 0.0025 | 0.0000 | FAIL |

The important row is `orthogonal gauge`: raw source-row coordinates move by
`0.7763`, but `J`, `kappa`, and `beta` do not move. Therefore the positive
theorem must be stated in terms of the full Gram law, not a preferred latent
basis. The important negative row is `three-role only`: the non-source Gram
block is fixed, ACV passes, and the support is the same, but the source row of
`J` moves and so does `beta`.

The branch-A closure condition is now exact:

```text
A-full = the event law derives a cofinal full role Gram J_n,
not merely event support, not merely three non-source roles, and not a
post-selected source extension.
```

This does not prove that the actual interacting ISP law has such a `J_n`. It
proves what would be enough, and it proves that the weaker data are not enough.

#### 5.30 Full role-Gram derivation gate

The next step is no longer to invent a selector. It is to say exactly what a
candidate event law must output before thresholding.

Fix a finite local collar `C_x` around a candidate event `x`. Let `Z_x` be the
centered finite collar fluctuation vector under the clicked local law. The four
canonical role statistics are:

```text
T_record    = stable detector-record likelihood contrast;
T_source    = one-event stress/source deletion response;
T_causal    = causal-collar incidence/deletion response;
T_antichain = antichain-density deletion response.
```

In finite linear response form:

```math
T_r
=
\langle a_r,Z_x\rangle,
\qquad
r\in\{record,source,causal,antichain\}.
```

The full role Gram is:

```math
J_{rs,n}
=
\operatorname{Cov}(T_r,T_s\mid click)
=
\langle a_r,a_s\rangle.
```

A candidate law passes the derivation gate only if all four `T_r` are produced
by the same local law before the event support is threshold-selected. It fails
if `T_source` is absent, inferred only from count identity, or added as a
post-selected source channel.

The finite gate is:

```text
code/v6_p2r_full_role_gram_derivation.py
```

It tests the candidate classes currently alive in the paper:

| candidate | source stage | full J | ACV | J span | kappa min | beta span | extension beta span | verdict |
|---|---|---|---|---:|---:|---:|---:|---|
| full LR/OER Gram | pre | yes | PASS | 0.0561 | 0.5361 | 0.0060 | 0.0000 | PASS |
| exact full Gram | pre | yes | PASS | 0.0000 | 0.5664 | 0.0000 | 0.0000 | PASS |
| support only | absent | no | FAIL | inf | 0.0000 | inf | 0.1226 | FAIL |
| record only LR | absent | no | FAIL | inf | 0.0000 | inf | 0.1226 | FAIL |
| geometry three-role | absent | no | FAIL | inf | 0.0000 | inf | 0.1226 | FAIL |
| post-selected source | post | no | FAIL | inf | 0.0000 | inf | 0.1226 | FAIL |
| nonconvergent full | pre | yes | PASS | 1.0200 | 0.2363 | 0.1226 | 0.0000 | FAIL |
| weak full source | pre | yes | FAIL | 0.0020 | -0.0181 | 0.0000 | 0.0000 | FAIL |

The two passing cases are exactly the A-full cases: the full role Gram is
internal and fixed or convergent. The failing cases divide cleanly:

```text
support only: no role Gram;
record only LR: no source/geometry role Gram;
geometry three-role: no source row;
post-selected source: source exists too late;
nonconvergent full: source exists but does not converge;
weak full source: source exists but has no positive deletion margin.
```

This gives the promised no-go.

**No-source theorem.** Any finite event law whose pre-threshold sufficient
statistics omit `T_source` cannot derive `beta`.

Proof. Hold fixed the event support, likelihood threshold, scalar rate, and
the non-source role statistics:

```text
T_record,\quad T_causal,\quad T_antichain.
```

Since `T_source` is not part of the pre-threshold law, extend the same reduced
law by a family of source rows `a_source(α)` after the support is known. These
extensions preserve the reduced law and its non-source Gram block, but change:

```math
d_{\rm source}(α)
=
(J(α)u)_{\rm source}.
```

The explicit finite family in the diagnostic has:

```text
same non-source roles;
source extension kappa span = 0.5550;
source extension beta span  = 0.1226.
```

Thus two laws with the same reduced pre-threshold data can have different
`beta`. Therefore no function of the source-absent law determines `beta`.

This proves all three requested points in finite form:

```text
1. canonical roles = record/source/causal/antichain collar statistics;
2. actual candidate gate = only full pre-threshold Gram laws pass;
3. no-source no-go = source-absent or post-selected laws cannot derive beta.
```

The remaining open theorem is now maximally local:

```text
Does the interacting ISP event law itself generate
T_record,T_source,T_causal,T_antichain
before thresholding, with a cofinal full Gram J_n?
```

If yes, branch A has a live derivation of `beta`. If no, the scale is branch B.

#### 5.31 Local-operator origin gate

The full role Gram is necessary but not quite enough. A coupled model could
assemble a stable full Gram by giving the source row to a second operator. That
would still pass some covariance and scale checks, but it would not be one
indivisible event. Branch A needs:

```text
T_record,T_source,T_causal,T_antichain
are readouts of the same local scalar field/record operator family.
```

The finite diagnostic is:

```text
code/v6_p2s_local_operator_origin.py
```

It tests whether the four roles are pre-threshold readouts of one operator
origin `O`, rather than record/geometry coming from `O` and source coming from
a separate `Q_source`:

| candidate | roles | one operator | source pre | ACV | J span | kappa min | beta span | verdict |
|---|---|---|---|---|---:|---:|---:|---|
| exact single local O | yes | yes | yes | PASS | 0.0000 | 0.5664 | 0.0000 | PASS |
| convergent single O | yes | yes | yes | PASS | 0.0561 | 0.5361 | 0.0060 | PASS |
| independent source Q | yes | no | yes | PASS | 0.0000 | 0.5664 | 0.0000 | FAIL |
| post-selected source | yes | yes | no | PASS | 1.0200 | 0.2363 | 0.1226 | FAIL |
| record-only O | no | no | no | FAIL | inf | 0.0000 | inf | FAIL |
| nonconvergent single O | yes | yes | yes | PASS | 1.0200 | 0.2363 | 0.1226 | FAIL |
| weak source single O | yes | yes | yes | FAIL | 0.0020 | -0.0181 | 0.0000 | FAIL |

The crucial row is `independent source Q`. It has a stable full Gram and a
stable `beta`, but it fails the local-operator origin condition. This is the
finite version of the branch-B warning: a separate source operator can be
covariant and numerically stable without making source a readout of the same
event.

Thus the A-full theorem target becomes:

```text
one local scalar operator family -> four pre-threshold role statistics
-> cofinal full Gram J_n -> beta.
```

#### 5.32 Microcausal TS gate

Branch A also has to strengthen the old diagonal TS receipt. It is not enough
that two hand-built diagonal scalar projectors commute. The threshold
projectors must be spectral projectors of local microcausal operators, and any
spacelike ordering loop must give the same joint operation.

The finite diagnostic:

```text
code/v6_p2t_microcausal_ts_gate.py
```

uses three spacelike cells and checks the maximum pairwise commutator norm and
the maximum residue over all products:

```text
P_{pi(1)}P_{pi(2)}P_{pi(3)}.
```

It prints:

| candidate | roles | source | local | nonlinear | comm norm | loop residue | verdict |
|---|---|---|---|---|---:|---:|---|
| local full scalar | yes | pre | yes | no | 0.000e+00 | 0.000e+00 | PASS |
| local rotated scalar | yes | pre | yes | no | 0.000e+00 | 1.397e-16 | PASS |
| diagonal receipt only | no | absent | yes | no | 0.000e+00 | 0.000e+00 | FAIL |
| nonlocal source tail | yes | pre | no | no | 1.000e+00 | 7.071e-01 | FAIL |
| preferred-slice update | yes | pre | no | no | 8.660e-01 | 6.124e-01 | FAIL |
| post-source local | yes | post | yes | no | 0.000e+00 | 0.000e+00 | FAIL |
| state nonlinear local | yes | pre | yes | yes | 0.000e+00 | 0.000e+00 | FAIL |

This separates three facts:

```text
local microcausal threshold projectors => TS loop residue zero;
diagonal finite receipts alone do not prove full branch A;
nonlocal source tails or preferred-slice updates generate finite residues.
```

The TS theorem target is now:

```text
the same local scalar operator family that generates J_n also generates
microcausal threshold projectors on spacelike-separated collars.
```

#### 5.33 Nonlinear Fréchet gate

The last hidden loophole is state-dependent nonlinearity. A threshold score can
look scalar and local at a point while moving its boundary with the state, or
while adding a nonlinear source term to the score map. Branch A needs fixed
linear local response at the event-law level.

The finite diagnostic:

```text
code/v6_p2u_nonlinear_frechet_gate.py
```

checks:

```text
second-difference Fréchet residue of the score map;
two-operation order residue for x/y threshold updates;
whether the threshold is adaptive/state-dependent.
```

It prints:

| candidate | roles | source | local | adaptive | Fréchet residue | order residue | verdict |
|---|---|---|---|---|---:|---:|---|
| fixed linear local | yes | pre | yes | no | 8.540e-15 | 0.000e+00 | PASS |
| linear nonlocal cross | yes | pre | no | no | 0.000e+00 | 0.000e+00 | FAIL |
| nonlinear local score | yes | pre | yes | no | 1.269e+00 | 0.000e+00 | FAIL |
| adaptive threshold | yes | pre | yes | yes | 0.000e+00 | 0.000e+00 | FAIL |
| hidden nonlinear source | yes | post | yes | no | 9.138e-01 | 0.000e+00 | FAIL |
| record-only linear | no | absent | yes | no | 8.540e-15 | 0.000e+00 | FAIL |

The adaptive row matters. It can have zero second-difference residue in this
finite probe because the adaptive boundary is linear, but it still fails
branch A because the threshold is not fixed by the local event law. The
nonlinear row matters for the opposite reason: it is local and pre-threshold,
but its Fréchet residue is finite.

Thus branch A requires:

```text
fixed linear local score;
no state-dependent threshold boundary;
no hidden nonlinear source term.
```

#### 5.34 Final finite branch-A closure ledger

The finite campaign can now be summarized as a ledger. The diagnostic:

```text
code/v6_p2v_branch_a_closure_ledger.py
```

aggregates the full-Gram, local-operator, microcausal TS, and nonlinear
Fréchet gates:

| candidate | Gram | operator | TS | linear | beta span | verdict | status |
|---|---|---|---|---|---:|---|---|
| finite A-full toy | PASS | PASS | PASS | PASS | 0.0060 | COND | finite pass; interacting derivation open |
| exact A-full toy | PASS | PASS | PASS | PASS | 0.0000 | COND | finite pass; interacting derivation open |
| support-only reduced | FAIL | FAIL | FAIL | FAIL | inf | FAIL | no source/full Gram |
| post-selected source | FAIL | FAIL | FAIL | FAIL | inf | FAIL | source too late |
| independent source operator | PASS | FAIL | PASS | PASS | 0.0000 | FAIL | coupled source, not one local operator |
| nonlocal TS tail | PASS | PASS | FAIL | PASS | 0.0000 | FAIL | microcausality fails |
| state nonlinear rule | PASS | PASS | FAIL | FAIL | 0.0000 | FAIL | Fréchet linearity fails |
| adaptive threshold rule | PASS | PASS | PASS | FAIL | 0.0000 | FAIL | threshold moves with state |
| nonconvergent full law | FAIL | FAIL | PASS | PASS | 0.1226 | FAIL | cofinal beta stability fails |
| weak-source full law | FAIL | FAIL | PASS | PASS | 0.0000 | FAIL | positive source floor fails |

This is as far as the finite branch-A investigation can honestly go. Every
currently actionable loophole now has a gate:

```text
full pre-threshold role Gram;
same local scalar operator origin;
microcausal spacelike threshold projectors;
fixed linear nonadaptive score;
positive source deletion floor;
cofinal beta stability.
```

Only A-full toy laws survive all finite gates. They remain conditional because
the actual interacting ISP event law has not been derived. The final theorem is
therefore singular:

```text
derive the full pre-threshold four-role Gram from one local microcausal
linear scalar operator family in the interacting ISP event law.
```

If that theorem is proved, branch A closes at finite theorem level. If it is
not, branch B is the honest theory: covariant collapse/source dynamics with a
physical but underived scale.

#### 5.35 Physical receipt closure gate

After all derivation gates pass, the same `beta` still has to be used in the
physical receipts. This is not an extra selector. It is a final consistency
gate:

```text
same beta -> energy bound, vacuum no-events, source/geometry identity,
TS residue zero, beta convergence.
```

The diagnostic is:

```text
code/v6_p2w_physical_receipt_closure.py
```

It prints:

| candidate | heating | energy | vacuum | source | TS | beta | verdict |
|---|---:|---|---|---|---|---|---|
| finite A-full toy | 0.0364 | PASS | PASS | PASS | PASS | PASS | PASS |
| exact A-full toy | 0.0362 | PASS | PASS | PASS | PASS | PASS | PASS |
| support-only no beta | inf | FAIL | PASS | FAIL | PASS | FAIL | FAIL |
| source mismatch | 0.0364 | PASS | PASS | FAIL | PASS | PASS | FAIL |
| vacuum leak | 0.0364 | PASS | FAIL | PASS | PASS | PASS | FAIL |
| nonlocal TS residue | 0.0364 | PASS | PASS | PASS | FAIL | PASS | FAIL |
| hot beta | 1.6384 | FAIL | PASS | PASS | PASS | PASS | FAIL |
| nonconvergent beta | 0.0364 | PASS | PASS | PASS | PASS | FAIL | FAIL |

This closes the finite receipt side. The A-full survivors use the same derived
scale in all finite receipts. Every visible physical pathology fails
independently:

```text
missing beta;
source/geometry mismatch;
vacuum events;
TS residue;
overheating;
nonconvergent beta.
```

The only remaining work is not another finite selector. It is the actual
interacting theorem:

```text
interacting ISP law -> one local microcausal linear operator family
-> full pre-threshold four-role Gram -> positive cofinal source response
-> beta -> physical receipts.
```

#### 5.36 Construction exhaustion and the fixed-background no-go

The finite gates now isolate the remaining branch-A object. It is natural to
ask whether the object is already supplied by a known construction class. The
answer is no, unless the full four-role Gram is added as an ansatz.

The relevant literature classes are strong in different directions. Locally
covariant QFT gives local fields and a stress-energy response through relative
Cauchy evolution. Relativistic collapse and flash models give covariant event
or source dynamics when built over a Tomonaga-Schwinger evolution. Causal-set
sprinkling gives intrinsic order data without a preferred Lorentz frame. But
branch A needs one object that does all four jobs before thresholding:

```text
local operator law -> record/source/causal/antichain role statistics -> J_n.
```

The diagnostic is:

```text
code/v6_p2x_operator_construction_exhaustion.py
```

It prints the construction-class audit:

| candidate | rec/src | geom | oneO | micro | linear | fullJ | missing input | verdict |
|---|---|---|---|---|---|---|---|---|
| fixed-background QFT scalar | yes | no | yes | yes | yes | no | geometry rows | FAIL |
| stress/RCE locally covariant QFT | yes | no | yes | yes | yes | no | background metric/geometry | FAIL |
| relativistic collapse/flash | yes | no | no | yes | no | no | stochastic source law | FAIL |
| causal-set geometry first | no | yes | no | yes | yes | no | source/operator rows | FAIL |
| coupled source + geometry | yes | yes | no | yes | yes | no | operator identity | FAIL |
| A-full finite ansatz | yes | yes | yes | yes | yes | yes | interacting derivation | COND |
| unknown interacting ISP theorem | yes | yes | yes | yes | yes | no | not yet proved | OPEN |

It also prints the finite extension freedom:

| family | fixed reduced data | extensions | J span | kappa span | beta span | verdict |
|---|---|---:|---:|---:|---:|---|
| geometry extension | record/source local operator | 4 | 0.4107 | 0.0165 | 0.0031 | FAIL |
| source extension | record/causal/antichain roles | 4 | inf | 0.5550 | 0.1226 | FAIL |

These two rows give the no-go in its most compact form.

**Fixed-background local-operator no-go.** Suppose a candidate branch-A law
starts with a local microcausal linear operator family on a fixed background,
and suppose its pre-threshold local statistics determine at most the
record/source rows. If the causal and antichain-density rows are not generated
by the same operator law before thresholding, then the full response Gram
`J_n` is not determined by the law. The same record/source operator data admit
distinct geometry completions with different full Grams. Therefore branch A
cannot derive the one-event geometry/source identity from that construction.

The same argument applies in the source direction. If record, causal, and
antichain rows are fixed but the source row is attached afterward, the source
extension family has:

```text
kappa span = 0.5550;
beta span  = 0.1226.
```

Thus `beta` is not a function of the reduced law.

**Proof.** The first extension family fixes the record/source rows and varies
only the causal and antichain rows. All variants have the same reduced local
operator data, but the full Gram changes by span `0.4107`. Hence there is no
map from the fixed-background record/source law to the full four-role Gram.
The second extension family fixes the non-source rows and varies only the
source row. It gives positive ACV-compatible completions with different
`kappa_G` and different `beta`. Hence there is no map from reduced
geometry/record data to the source response or memory scale. In both cases,
one can preserve the visible reduced law while changing the branch-A object
that is supposed to be derived. This contradicts branch-A closure.

This is not an absolute impossibility theorem for every conceivable ISP
ontology. It is stronger and narrower:

```text
Branch A is impossible for the known fixed-background, collapse/flash,
causal-set-first, and coupled-source construction classes under the current
assumptions, unless they add the full pre-threshold four-role Gram as a new
primitive.
```

The only surviving route is therefore not a selector and not a known collapse
recipe. It is a new interacting ISP theorem:

```text
one local microcausal linear operator family
derives record/source/causal/antichain statistics before thresholding.
```

If that theorem is proved, the finite OER/C-lock and same-beta physical
receipts give a branch-A route to `beta`. If it is not proved, branch A is not
closed; the honest theory is branch B, with a covariant event/source law and a
physical but underived memory scale.

#### 5.37 Best guess: invariant deletion action

The preceding no-go says what the known routes lack. The next question is what
an Einstein-style invariant law would have to look like if the four roles are
really one fact.

The strongest guess is:

```text
event = an invariant deletion atom in a finite causal record collar.
```

Let `C_x` be the finite causal collar around a candidate event `x`, selected
from causal order, not from a spatial slice. Let `P_n` be the finite
interacting record-history measure. Define a deletion action by the local
Radon-Nikodym contrast:

```math
\mathcal A_{n,x}
=
\log
{dP_n(C_x\mid x\ {\rm retained})
\over
dP_n(C_x\mid x\ {\rm deleted})}.
```

Equivalently, in a modular/relative-entropy reading, `A_{n,x}` is the finite
relative-entropy increment of retaining one local atom in its causal diamond.
The event threshold is then not a free scalar convention:

```text
E_x = { A_{n,x} >= 0 and the positive deletion component is stable }.
```

The four roles become four invariant deformation derivatives of the same
scalar action:

```math
T_r
=
\partial_{\theta_r}\mathcal A_{n,x}\big|_{\theta=0},
\qquad
r\in\{record,source,causal,antichain\}.
```

Here the four deformation directions are:

```text
record     = local record-evidence / detector-likelihood deformation;
source     = metric, modular-energy, or stress-response deformation;
causal     = causal-link / Alexandrov-collar deformation;
antichain  = cross-section density / antichain-cut deformation.
```

The full role Gram is no longer an independent object. It is the Fisher or
Hessian matrix of the same deletion action:

```math
J_{rs,n}
=
\operatorname{Cov}(T_r,T_s\mid E_x)
=
\partial_{\theta_r}\partial_{\theta_s}
\log Z_{n,x}(\theta)\big|_{\theta=0}.
```

This is the first candidate law that makes the four roles the same fact
without simply naming four ledgers. The finite diagnostic is:

```text
code/v6_p2y_invariant_law_guess_search.py
```

It prints:

| candidate | scalar | delete | rec | src | caus | anti | sameF | locality | beta/status | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| local scalar threshold | yes | no | yes | yes | no | no | no | yes | free beta | FAIL |
| stress/RCE response | yes | no | no | yes | no | no | no | yes | external geometry | FAIL |
| causal-set atom | yes | yes | no | no | yes | yes | no | yes | source absent | FAIL |
| entanglement equilibrium diamond | yes | no | no | yes | yes | yes | yes | local only in first-law limit | record event absent | NEAR-MISS |
| null modular/QNEC atom | yes | no | yes | yes | yes | yes | yes | null/Rindler-local, not generic | conditional | NEAR-MISS |
| invariant deletion action | yes | yes | yes | yes | yes | yes | yes | assumed theorem target | derived from Hessian | PASS-TARGET |

And the Hessian audit:

| candidate | roles | sameF | ACV | J span | kappa min | beta span | verdict |
|---|---|---|---|---:|---:|---:|---|
| invariant deletion action | yes | yes | PASS | 0.0561 | 0.5361 | 0.0060 | PASS-TARGET |
| source-free scalar action | no | yes | FAIL | 1.0200 | 0.0000 | inf | FAIL |
| assembled four-ledger action | yes | no | FAIL | 0.0561 | 0.0000 | inf | FAIL |

The near-misses are informative. Jacobson-style entanglement equilibrium ties
causal diamonds, area/entropy density, and stress response to one variational
principle, but it does not by itself define an objective finite record event.
Null modular/QNEC arguments get closer: they relate entropy deformation and
stress on null cuts, and local modular Hamiltonians can be available for
Rindler/null settings. But they are still not a generic finite event law on an
interacting causal record collar.

Thus the best branch-A conjecture is:

```text
Invariant Deletion-Action Law (IDA):
the indivisible event is a stable positive atom of local deletion
relative entropy in a causal collar.
```

The theorem target is precise.

**IDA closure theorem target.** Suppose the interacting ISP law supplies a
cofinal family of finite local record measures `P_n` with:

```text
IDA1. a local deletion Radon-Nikodym action A_{n,x};
IDA2. causal-collar covariance, with no preferred slicing;
IDA3. spacelike microcausal factorization of deletion actions;
IDA4. four internal fixed linear score directions record/source/causal/antichain;
IDA5. regular Fisher-Hessian identity for J_n;
IDA6. positive ACV and source deletion floor;
IDA7. cofinal convergence of J_n and beta_n.
```

Then branch A closes at the scale level. The likelihood threshold is
`A_{n,x}=0`, `gamma_n` is the density of stable positive deletion atoms, the
full role Gram is:

```math
J_{rs,n}
=
\operatorname{Cov}(\partial_r A_{n,x},\partial_s A_{n,x}\mid E_x),
```

and:

```math
\beta_n
=
\left(
{4\gamma_n(J_nu)_{\rm source}\over5}
\right)^{1/6}
\longrightarrow
\beta.
```

The proof is now only bookkeeping. IDA1-IDA5 put the full four-role Gram
inside one invariant scalar law before thresholding, with fixed linear score
directions rather than adaptive state-dependent boundaries. IDA3 gives the TS
commutation gate. IDA6 gives the positive source response needed by C-lock/OER.
IDA7 gives scale convergence. The physical receipt gate then reuses the same
`beta`.

This is the closest thing in the current search to "the law." It is not yet a
proof that the actual interacting ISP has such a deletion action. It is the
law one would now try to derive.

#### 5.38 IDA proof/falsification program for Physical ICS

The seven-step program can now be executed cleanly in finite Physical ICS. The
main result is a sharpening: the scalar deletion value `A_x(0)` is not enough.
Branch A needs the full local deletion-action germ:

```text
A_x(theta), dA_x, Hess A_x
```

in the four fixed internal directions.

The diagnostic is:

```text
code/v6_p2z_ida_physical_ics_proof_program.py
```

It implements:

1. a local deletion map `D_x`;
2. local Radon-Nikodym existence under finite positivity;
3. causal-order invariance and slice-freeness checks;
4. internal four-role deformation directions;
5. Fisher/Hessian equality with the full role Gram;
6. positive source floor and refinement convergence;
7. same-`A_x(0)`/different-`beta` counterexamples.

It prints:

| candidate | D_x | RN | inv | roles | Fisher | source | counter | beta span | verdict |
|---|---|---|---|---|---|---|---|---:|---|
| full IDA germ Physical ICS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 0.0060 | PASS-TARGET |
| bare ICS order only | PASS | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | inf | FAIL |
| zero-support deletion law | PASS | FAIL | PASS | PASS | PASS | PASS | PASS | 0.0000 | FAIL |
| label-colored deletion | PASS | PASS | FAIL | PASS | PASS | PASS | PASS | 0.0000 | FAIL |
| slice-colored deletion | PASS | PASS | FAIL | PASS | PASS | PASS | PASS | 0.0000 | FAIL |
| source-external IDA | PASS | PASS | PASS | FAIL | FAIL | FAIL | FAIL | inf | FAIL |
| scalar-only IDA | PASS | PASS | PASS | FAIL | FAIL | FAIL | PASS | inf | FAIL |
| weak-source IDA germ | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | 0.0000 | FAIL |
| nonconvergent IDA germ | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | 0.1226 | FAIL |

The same-scalar counterexample is:

```text
same scalar A_x(0) span       = 0.0000;
different Hessian beta span   = 0.1226.
```

This proves that IDA cannot mean only:

```text
event = A_x(0) >= 0.
```

That scalar threshold is useful, but it does not determine the memory scale.
Two Physical-ICS laws can have the same deletion action value at the event
while having different Hessians, different source response, and different
`beta`. Therefore the real branch-A object is:

```text
the local IDA germ, not the local IDA value.
```

The finite theorem is:

**Finite IDA-germ theorem.** Let a finite Physical ICS supply:

```text
(C_n,prec_n,R_n,P_n,D_x)
```

where `D_x` removes `x` from the causal collar by induced order restriction
and record restriction. If the deleted collar measure has positive support on
the retained collar image, then the local Radon-Nikodym deletion action exists:

```math
A_{n,x}
=
\log {dP_n(C_x\mid x\ {\rm retained})
\over dP_n(D_xC_x\mid x\ {\rm deleted})}.
```

If, in addition, `P_n` and `D_x` are causal-order covariant and do not depend
on a chosen linear extension, then `A_{n,x}` is relabeling invariant and
slice-free. If the local deformation germ `A_{n,x}(theta)` is a regular finite
exponential family with four fixed internal score directions
`record/source/causal/antichain`, then:

```math
\partial_r\partial_s \log Z_{n,x}(\theta)\big|_{\theta=0}
=
\operatorname{Cov}(T_r,T_s\mid E_x)
=
J_{rs,n}.
```

Thus IDA-germ supplies the full role Gram internally. If:

```text
(J_nu)_source has a positive cofinal floor;
J_n converges under refinement;
beta_n from C-lock/OER converges;
```

then:

```math
\beta_n
=
\left(
{4\gamma_n(J_nu)_{\rm source}\over5}
\right)^{1/6}
```

is derived by the same Physical-ICS event law.

**Proof.** Deletion is well-defined because induced suborders of finite
partial orders are partial orders, and record restriction is a finite map.
Local RN existence is the finite absolute-continuity statement; strict deleted
support positivity is sufficient. Relabeling invariance follows because the
action is a function of the isomorphism class of the causal collar and its
records, not event names. Slice-freeness follows because `D_x` and `P_n` are
defined on the causal collar, not on a chosen linear extension. The
Fisher/Hessian identity is the standard finite exponential-family identity:
the Hessian of log partition equals score covariance. The remaining scale
claim is the already proved C-lock/OER continuity on the positive-margin
region.

**Scalar-only no-go.** If only `A_x(0)` is fixed, IDA does not derive `beta`.
The explicit same-scalar family has identical event-threshold value but
different Hessians and:

```text
beta span = 0.1226.
```

Thus any proof that stops at a deletion threshold has not closed branch A. The
interacting theorem must derive the four-direction local deletion germ.

#### 5.39 Full IDA-germ uniqueness attack

The previous section still leaves a possible sleight of hand. A full IDA germ
would close the finite gates, but is the germ determined by the finite
Physical-ICS data:

```text
P_n,\quad D_x,\quad A_x(0)?
```

The answer is no. The scalar Physical-ICS deletion law does not by itself
select the four deformation directions, their role labels, their units, or
their refinement transport.

The diagnostic is:

```text
code/v6_p2aa_ida_germ_uniqueness_attack.py
```

It prints:

| candidate | same ICS | A0 | dirs | labels | units | conv | beta span | verdict |
|---|---|---|---|---|---|---|---:|---|
| base P,D,A only | yes | yes | no | no | no | no | 0.1226 | FAIL |
| unlabeled score subspace | yes | yes | yes | no | no | no | 0.0250 | FAIL |
| free source units | yes | yes | yes | yes | no | no | 0.1297 | FAIL |
| drifting canonical-looking germ | yes | yes | yes | yes | yes | no | 0.1226 | FAIL |
| weak-source canonical germ | yes | yes | yes | yes | yes | yes | inf | FAIL |
| canonical normalized germ | yes | yes | yes | yes | yes | yes | 0.0060 | PASS-TARGET |

This proves the next no-go.

**IDA-germ nonuniqueness theorem.** The data `P_n,D_x,A_x(0)` do not determine
the full role Gram. Holding those data fixed, one can vary:

```text
the source score row;
the role basis inside an unlabeled score subspace;
the normalization of the source parameter;
the refinement transport of the germ.
```

These variations change `J_n` and `beta`. Therefore Physical ICS plus scalar
IDA does not derive branch A. The full local germ must be canonical.

The row `unlabeled score subspace` is especially important. Even if the
deletion law determines a four-dimensional tangent subspace, branch A still
fails if it does not identify which direction is source. A rotation in the
record/source plane keeps the same abstract score subspace but moves:

```text
beta span = 0.0250.
```

Likewise, even labeled directions fail if the source parameter has free units:

```text
beta span = 0.1297.
```

Thus the remaining theorem is no longer merely:

```text
derive a full IDA germ.
```

It is:

```text
derive a canonical normalized four-role IDA germ.
```

#### 5.40 Canonical IDA-germ lock

The natural way to make the germ canonical is to make the four roles isolated
sectors of the deletion-score tangent space. Let `T_x` be the finite tangent
space of local deletion-action deformations at `x`, with Fisher inner product
`G_x`. A canonical-germ lock would supply a self-adjoint role-sector operator:

```math
L_x:T_x\to T_x
```

whose four relevant eigenspaces are:

```text
record, source, causal, antichain.
```

If these eigenspaces are one-dimensional and spectrally isolated, then the
directions are labeled by invariant sector data rather than by a chosen probe.
The Fisher metric fixes their units:

```math
G_x(T_r,T_r)=1,
```

and positive deletion response fixes source orientation.

The diagnostic is:

```text
code/v6_p2ab_canonical_ida_germ_lock.py
```

It prints:

| candidate | sectors | gap | labels | units | orient | floor | conv | beta span | verdict |
|---|---|---:|---|---|---|---|---|---:|---|
| isolated sector lock | 1D isolated | 0.2400 | yes | yes | yes | PASS | PASS | 0.0060 | PASS-TARGET |
| degenerate source/record sector | degenerate | 0.0000 | no | yes | yes | PASS | FAIL | 0.0250 | FAIL |
| free Fisher units | 1D isolated | 0.2400 | yes | no | yes | PASS | FAIL | 0.1297 | FAIL |
| unoriented source sign | 1D isolated | 0.2400 | yes | yes | no | FAIL | FAIL | inf | FAIL |
| nonconvergent sector lock | 1D isolated | 0.2400 | yes | yes | yes | PASS | FAIL | 0.1226 | FAIL |
| weak-source sector lock | 1D isolated | 0.2400 | yes | yes | yes | FAIL | PASS | inf | FAIL |

This is the strongest surviving branch-A theorem target.

**Canonical-germ lock theorem target.** Branch A needs Physical ICS to derive:

```text
1. a finite deletion-score tangent space T_x;
2. a Fisher metric G_x;
3. a self-adjoint role-sector operator L_x;
4. four isolated one-dimensional sectors record/source/causal/antichain;
5. Fisher-unit normalization and positive source orientation;
6. cofinal convergence of L_x, G_x, J_x, and beta_x.
```

If the sectors are degenerate, role rotations move `beta`. If units are free,
source rescaling moves `beta`. If orientation is not fixed, the source floor
can fail. If the sectors drift under refinement, `beta` drifts. If the source
sector is weak, C-lock fails.

Therefore the live A theorem is now exact:

```text
Physical ICS -> canonical normalized IDA germ -> full role Gram -> beta.
```

Without the canonical lock, IDA is still branch B with an elegant invariant
score. With the lock, IDA becomes a genuine branch-A route.

#### 5.41 Role-sector origin attack

The canonical lock still has one possible escape hatch: perhaps the
role-sector operator `L_x` is chosen externally. Then even isolated
one-dimensional sectors would not close branch A. The sector operator itself
must be derived from Physical-ICS deletion dynamics.

The diagnostic is:

```text
code/v6_p2ac_role_sector_origin_attack.py
```

It prints:

| candidate | L | intrinsic | isolated | labels | source | conv | beta span | verdict |
|---|---|---|---|---|---|---|---:|---|
| no role-sector operator | no | no | no | no | no | no | 0.1226 | FAIL |
| external isolated L | yes | no | yes | no | yes | no | 0.0250 | FAIL |
| automorphism-degenerate L | yes | partial | no | no | yes | no | 0.0250 | FAIL |
| hessian eigenbasis only | yes | partial | yes | no | no | no | inf | FAIL |
| source-external sector | yes | no | yes | yes | no | no | 0.1226 | FAIL |
| intrinsic L with drift | yes | yes | yes | yes | yes | no | 0.1226 | FAIL |
| intrinsic weak-source L | yes | yes | yes | yes | yes | yes | inf | FAIL |
| intrinsic canonical L | yes | yes | yes | yes | yes | yes | 0.0060 | PASS-TARGET |

The new no-go is:

**External-sector no-go.** A sector operator with isolated eigenspaces does not
derive branch A unless it is intrinsic to the Physical-ICS event law. Holding
the same Physical-ICS base data fixed, externally chosen isolated sector
operators can rotate the source direction and move:

```text
beta span = 0.0250.
```

If `L_x` is only the Hessian eigenbasis, the source label is not derived. If
`L_x` comes only from automorphism invariance, degenerate sectors can remain.
If the source sector is attached by a separate source operator, the same old
source-extension freedom returns.

The final finite theorem target is therefore:

```text
Physical ICS
-> intrinsic deletion-dynamics operator L_x
-> four isolated role sectors
-> Fisher-normalized IDA germ
-> full role Gram
-> beta.
```

Everything before the last actual interacting theorem has now been attacked:

```text
scalar A_x(0): not enough;
full germ without canonicity: not enough;
canonical sectors with external L_x: not enough;
intrinsic canonical L_x with positive source floor and convergence: sufficient
at finite theorem-target level.
```

This is the end of the finite campaign. Branch A now depends on one
interacting Physical-ICS theorem: derive `L_x` intrinsically from the same
deletion dynamics that defines the event.

#### 5.42 Intrinsic `L_x` from the deletion Dirichlet form

The role-sector origin attack suggests a constructive answer. Physical ICS
already has two local structures:

```text
P_n = local record-history measure;
D_x = deletion map.
```

From the IDA germ, define the Fisher metric on the deletion-score tangent
space:

```math
G_x(u,v)
=
\operatorname{Cov}(u,v\mid E_x).
```

From the deletion map, define the deletion Dirichlet form:

```math
Q_x(u,v)
=
\mathbb E\left[
\big(u(C_x)-u(D_xC_x)\big)
\big(v(C_x)-v(D_xC_x)\big)
\mid E_x
\right].
```

Then the intrinsic candidate is:

```math
L_x
=
G_x^{-1}Q_x,
```

understood as the self-adjoint generalized eigenproblem:

```math
Q_x u
=
\lambda G_x u.
```

This construction uses no external sector operator if `G_x` and `Q_x` are
computed from `P_n` and `D_x`.

The diagnostic is:

```text
code/v6_p2ad_intrinsic_lx_dirichlet_derivation.py
```

It prints:

| candidate | intrinsic | labels | eigvals | gap | isolated | source | beta span | verdict |
|---|---|---|---|---:|---|---|---:|---|
| intrinsic Dirichlet Lx | PASS | PASS | [0.18,0.47,0.82,1.21] | 0.2900 | PASS | PASS | 0.0060 | PASS-TARGET |
| no deletion Q | FAIL | FAIL | [0.00,0.00,0.00,0.00] | 0.0000 | FAIL | FAIL | 0.0000 | FAIL |
| degenerate Dirichlet Lx | PASS | FAIL | [0.18,0.18,0.82,1.21] | 0.0000 | FAIL | PASS | 0.0000 | FAIL |
| external Q choice | FAIL | FAIL | [0.22,0.49,0.81,1.20] | 0.2700 | PASS | PASS | 0.0000 | FAIL |
| wrong role ordering | PASS | FAIL | [0.47,0.18,0.82,1.21] | 0.2900 | PASS | PASS | 0.0000 | FAIL |
| nonconvergent Dirichlet Lx | PASS | PASS | [0.18,0.47,0.82,1.21] | 0.2900 | PASS | PASS | 0.1226 | FAIL |
| weak-source Dirichlet Lx | PASS | PASS | [0.18,0.47,0.82,1.21] | 0.2900 | PASS | FAIL | inf | FAIL |

Thus `L_x=G_x^{-1}Q_x` is the first intrinsic construction of the sector
operator. But it is still conditional. It works only if:

```text
Q_x is the deletion Dirichlet form, not an external quadratic form;
the generalized spectrum has four isolated one-dimensional sectors;
the sectors are correctly role-labeled;
the source sector has a positive floor;
the spectral data converge under refinement.
```

Missing `Q_x`, degeneracy, external `Q_x`, wrong labels, drift, and weak source
all fail. Therefore the next follow-up is unavoidable: eigenvalue isolation
does not itself label the modes.

#### 5.43 Eigenlabel derivation

An isolated eigenmode is not yet a physical role. The role label must be read
from intrinsic Physical-ICS signatures, not from a table added afterward.

Let the four signature functionals be:

```text
record evidence signature;
source deletion amplitude;
causal-link sensitivity;
antichain-density sensitivity.
```

Let `S_{ar}` be the response of eigenmode `r` under signature functional `a`.
The labels are canonical only if the signature matrix is full-rank and
diagonally dominant after ordering by the intrinsic signatures.

The diagnostic is:

```text
code/v6_p2ae_lx_eigenlabel_derivation.py
```

It prints:

| candidate | isolated | rank | margin | source | conv | beta span | verdict |
|---|---|---:|---:|---|---|---:|---|
| intrinsic signature labels | yes | 4 | 0.8500 | PASS | PASS | 0.0060 | PASS-TARGET |
| swapped source/causal signatures | yes | 4 | -0.8800 | FAIL | PASS | 0.0060 | FAIL |
| degenerate signatures | yes | 4 | 0.0000 | FAIL | PASS | 0.0060 | FAIL |
| missing source signature | yes | 4 | 0.0100 | PASS | FAIL | inf | FAIL |
| signature drift | yes | 4 | 0.8500 | PASS | FAIL | 0.1226 | FAIL |
| unisolated modes no labels | no | 4 | 0.8500 | PASS | PASS | 0.0060 | FAIL |

This makes the label theorem exact:

```text
isolated modes + full-rank stable signature matrix
=> canonical role labels.
```

Swapped signatures, degenerate signatures, missing source signature, signature
drift, and unisolated modes all fail.

#### 5.44 Signature-origin audit

One last possible transfer remains. The signature functionals themselves must
be intrinsic to Physical ICS. Otherwise the labels have merely moved from
`L_x` to the signature table.

The diagnostic is:

```text
code/v6_p2af_signature_origin_audit.py
```

It prints:

| candidate | rec | src | caus | anti | rank | margin | stable | beta span | verdict |
|---|---|---|---|---|---:|---:|---|---:|---|
| intrinsic signature quartet | yes | yes | yes | yes | 4 | 0.8500 | PASS | 0.0060 | PASS-TARGET |
| no source signature | yes | no | yes | yes | 3 | 0.0000 | FAIL | inf | FAIL |
| external source signature | yes | no | yes | yes | 4 | 0.2200 | FAIL | 0.1226 | FAIL |
| source/causal ambiguous | yes | yes | yes | yes | 4 | 0.0000 | PASS | 0.0060 | FAIL |
| weak source signature | yes | yes | yes | yes | 4 | 0.8500 | FAIL | inf | FAIL |
| signature refinement drift | yes | yes | yes | yes | 4 | 0.8500 | FAIL | 0.1226 | FAIL |

The final theorem target is now fully explicit:

```text
Physical ICS
-> IDA deletion germ
-> Fisher metric G_x
-> deletion Dirichlet form Q_x
-> L_x=G_x^{-1}Q_x
-> isolated eigenmodes
-> intrinsic stable signature quartet
-> record/source/causal/antichain labels
-> full role Gram
-> beta.
```

This is as far as the finite campaign can be pushed. The remaining open
statement is no longer a vague scale selector. It is a concrete interacting
Physical-ICS theorem:

```text
derive the intrinsic signature quartet and the isolated Dirichlet spectrum
of L_x from the same local deletion dynamics.
```

#### 5.45 Frozen signature theorem: counterexample

At this point the target has to stop moving. Freeze the theorem:

```text
Bare Physical ICS data
=
(finite causal order, record measure, deletion map)
derive the record/source/causal/antichain signature quartet.
```

Allowed derived objects are automorphism-invariant functions of exactly that
data. No external role marks, no source tag, no added signature table.

The diagnostic is:

```text
code/v6_p2ag_frozen_signature_theorem_audit.py
```

It enumerates all record-channel permutations preserving the finite
Physical-ICS data and computes the invariant orbits. It prints:

| candidate | automorphisms | orbits | marked | quartet | source | beta span | verdict |
|---|---:|---|---|---|---|---:|---|
| bare symmetric Physical ICS | 24 | 0123 | no | no | no | 0.0000 | FAIL |
| bare distinct but unlabeled ICS | 1 | 0;1;2;3 | no | no | no | 0.2003 | FAIL |
| bare three-signature ICS | 1 | 0;1;2 | no | no | no | 0.0000 | FAIL |
| marked signature quartet | 1 | 0;1;2;3 | yes | yes | yes | 0.0000 | PASS-EXTRA |
| wrong marked quartet | 1 | 0;1;2;3 | yes | no | no | 0.2003 | FAIL |

The counterexample is the second row. The finite collar has four distinct
invariant singleton channels:

```text
orbits = 0;1;2;3.
```

So this is not a mere degeneracy of automorphisms. The bare data distinguish
four channels as channels. But the data do not say which singleton is
`source`. Assigning the source role to different singletons is compatible with
the same bare Physical-ICS data and gives:

```text
beta span = 0.2003.
```

Therefore the source signature is not a function of:

```text
finite causal order + record measure + deletion map.
```

**Frozen-signature no-go.** There is no theorem deriving the labeled
record/source/causal/antichain signature quartet from bare Physical ICS data
alone.

**Proof.** In the bare distinct collar, the automorphism group is trivial, so
each primitive channel is individually invariant. However, trivial
automorphism orbits do not supply role semantics. The maps:

```text
channel 0 -> source;
channel 1 -> source;
channel 2 -> source;
channel 3 -> source
```

are all compatible with the same allowed data because no role marks are part of
that data. The C-lock/OER beta computed from these different source choices
has nonzero span. Hence no automorphism-invariant function of the bare data
selects a unique source signature. Without a unique source signature, there is
no unique signature quartet and no derived full role Gram. The symmetric and
three-signature rows show the easier failures: too much symmetry or too few
channels. The marked quartet passes only because the role marks are included
as extra input.

Thus pure branch A, in the frozen sense, fails:

```text
Bare Physical ICS does not derive the signature quartet.
```

The honest fork is:

```text
Branch A-pure: false under the current bare Physical-ICS data.
Enriched Physical ICS: possible if the signature quartet/role marks are added
or derived by additional physical structure not present in the bare data.
Branch B: covariant event/source model with the role/signature structure as
physical input.
```

This closes the moving-target loop. No further finite lock is introduced.
The missing object is not another selector; it is extra structure beyond bare
Physical ICS.

#### 5.46 Enriched object campaign: modular diamond record instrument

The frozen no-go should not be read as a demand to paste four role labels onto
the old object. That would pass only as bookkeeping. The Einstein/Feynman
question is sharper:

```text
Is there a simpler physical object whose invariant structure already contains
the four roles as conjugate readouts?
```

The campaign tests that question directly. The diagnostic is:

```text
code/v6_p2ah_enriched_physical_object_campaign.py
```

It compares bare ICS, marked quartets, independent ledgers, partial
instruments, and causal-diamond instruments. The surviving object is:

```text
modular causal-diamond record instrument.
```

This is not:

```text
causal set + four labels.
```

It is one finite local diamond object:

```text
MCDI_x =
(
  C_x, prec_x, D_x,
  A_x,
  sigma_x,
  I_x,
  chi_x,
  N_x,
  S_x
).
```

Here:

- `C_x,prec_x` is the finite causal collar/diamond around the candidate event;
- `D_x` is deletion of the candidate atom by induced causal and record
  restriction;
- `A_x` is the local record algebra;
- `sigma_x` is the local vacuum/reference state on that algebra;
- `I_x` is a local record instrument, with a clicked branch state `rho_x`;
- `chi_x` is the diamond-preserving modular flow, with generator
  `K_x=-log sigma_x` in the finite model;
- `N_x` is the interval-volume/order count of the diamond;
- `S_x` is the screen/antichain entropy count.

The scalar action is the deletion relative-entropy/free-action germ:

```math
\mathcal F_x(\theta)
=
\log Z_x(\theta),
\qquad
Z_x(\theta)
=
\mathbb E_{\sigma_x}
\exp\{
\theta_R T_R+\theta_M T_M+\theta_V T_V+\theta_S T_S
\}.
```

Equivalently, in the relative-entropy reading:

```math
S(\rho_x\|\sigma_x)
=
\Delta\langle K_x\rangle-\Delta S_x,
```

with the causal-diamond first-law split supplying the volume and screen
terms. The event is the stable positive deletion atom of this one action:

```text
E_x = { deletion free action >= 0 and the positive component is stable }.
```

The four roles are no longer named channels. They are the four conjugate
derivatives of the same local diamond action:

| derivative | physical readout | branch-A role |
|---|---|---|
| `T_R = ∂_{theta_R} F_x` | record-instrument outcome likelihood | record |
| `T_M = ∂_{theta_M} F_x` | modular/RCE stress response | source |
| `T_V = ∂_{theta_V} F_x` | interval-volume / order response | causal-set |
| `T_S = ∂_{theta_S} F_x` | screen / antichain entropy response | antichain density |

This is the first enrichment that is both stronger than bare Physical ICS and
simpler than a four-ledger ontology. The primitive is not the quartet. The
primitive is one local modular instrument on one causal diamond. The quartet
is its finite first-law response basis.

The finite campaign prints:

| candidate | primitive | oneF | vars | rank | margin | FL-res | source floor | beta span | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| bare Physical ICS | ledger/base | no | `--VS` | 3 | 0.0000 | 0.6058 | 0.0000 | 0.0000 | FAIL |
| marked signature quartet | marks | no | `RMVS` | 4 | 0.7800 | 0.0000 | 0.9500 | 0.0000 | PASS-EXTRA |
| four independent ledgers | diamond-instrument | no | `RMVS` | 4 | 0.7800 | 0.0000 | 0.9500 | 0.0000 | FAIL |
| record-only instrument | partial-action | yes | `R---` | 1 | 0.0000 | 1.4142 | 0.0000 | 0.0000 | FAIL |
| stress/RCE without record | partial-action | yes | `-M--` | 1 | 0.0000 | 0.9194 | 0.9500 | 0.0000 | FAIL |
| diamond action without screen | partial-action | yes | `RMV-` | 3 | 0.0000 | 0.6058 | 0.9500 | 0.0000 | FAIL |
| degenerate modular-volume law | diamond-instrument | yes | `RMVS` | 4 | -0.0800 | 0.0000 | 0.9500 | 0.0000 | FAIL |
| source units free diamond | diamond-instrument | yes | `RMVS` | 4 | 0.7800 | 0.0000 | 0.5500 | 0.1226 | FAIL |
| wrong first-law orientation | diamond-instrument | yes | `RMVS` | 4 | 0.7800 | 1.1547 | 0.9500 | 0.0000 | FAIL |
| weak-source diamond instrument | diamond-instrument | yes | `RMVS` | 4 | 0.7800 | 0.0000 | 0.0600 | 0.0000 | FAIL |
| nonconvergent diamond instrument | diamond-instrument | yes | `RMVS` | 4 | 0.7800 | 0.0000 | 0.9500 | 0.1226 | FAIL |
| modular diamond record instrument | diamond-instrument | yes | `RMVS` | 4 | 0.7800 | 0.0000 | 0.9500 | 0.0024 | PASS-TARGET |

The failure modes are the theorem. Bare ICS still lacks record and modular
source conjugates. A marked quartet passes only because the marks are present
as extra input. Four independent ledgers fail because there is no one scalar
action. Record-only and stress-only partial actions each miss the other half
of the event. A diamond without screen/antichain data has rank three. A
degenerate modular-volume law cannot separate source from causal response.
Free source units move `beta`. Wrong first-law orientation swaps the physical
sign of the modular source. Weak source response fails C-lock. Nonconvergent
diamond data reopen the beta drift.

The positive finite statement is therefore:

**Modular diamond instrument theorem target.** If the actual interacting
Physical ICS supplies a cofinal local modular causal-diamond record instrument
`MCDI_x` such that:

```text
1. the event action is one deletion relative-entropy/free-action germ;
2. the local record instrument supplies the record likelihood derivative;
3. the diamond modular generator supplies the stress/source derivative;
4. interval volume and screen/antichain counts are intrinsic diamond
   functionals;
5. the first-law orientation is fixed:
      delta F = delta K_chi + p delta V - T delta S_screen
   up to the chosen finite normalization;
6. the four signature derivatives form a full-rank diagonally dominant
   response matrix;
7. the modular source derivative has a cofinal positive deletion floor;
8. the Fisher units and response matrix converge under refinement;
```

then the four roles are intrinsic. The full role Gram is:

```math
J_{ab,x}
=
\partial_a\partial_b\log Z_x(\theta)\big|_{\theta=0}
=
\operatorname{Cov}(T_a,T_b\mid E_x),
\qquad
a,b\in\{R,M,V,S\}.
```

The source row is the modular/RCE row, not a chosen role label. Hence the
C-lock/OER scale is fixed by the same object:

```math
\beta_x
=
\left(
{4\gamma_x (J_x u_x)_M\over 5}
\right)^{1/6}.
```

This is a real enrichment, not a rescue by notation. It says that the physical
primitive was chosen too small. The bare causal-record-deletion triple is the
shadow. The local modular diamond record instrument is the candidate physical
germ.

**Minimality no-go around the candidate.** Any proposed enrichment that omits
one of:

```text
record instrument,
modular/RCE source conjugate,
interval-volume conjugate,
screen/antichain conjugate,
one scalar action,
first-law orientation,
fixed Fisher units,
positive source floor,
cofinal convergence
```

falls into one of the failing rows of the audit and cannot derive `beta`.

The honest status after this campaign is:

```text
bare branch A: false;
role-mark enrichment: possible but ugly / PASS-EXTRA;
modular diamond record instrument: best branch-A-enriched primitive;
actual theorem still open: derive MCDI_x from interacting ISP rather than
postulating it.
```

#### 5.47 Einstein audit: causal set as order-shadow

The conceptual correction can now be made without metaphor. The causal set is
not the full physical object. It is the order-shadow:

```math
\pi_{\rm order}(MCDI_x)=(C_x,\prec_x).
```

This is why the frozen-signature theorem failed. Projecting to order forgets
the conjugate record, modular-source, interval-volume, and screen responses.
The causal set still builds geometry, but it is not the whole event germ.

Einstein's test is a deletion test:

```text
delete one primitive event;
the same deletion must change record, modular source, interval volume, and
screen/antichain entropy as one constrained first-law response.
```

The diagnostic is:

```text
code/v6_p2ai_einstein_order_shadow_audit.py
```

It tests whether the candidate primitive is one deletion atom, one action, and
one correctly oriented first-law response. It prints:

| candidate | primitive | same | oneF | floor | FL-res | beta span | verdict |
|---|---|---|---|---:|---:|---:|---|
| bare causal-set order shadow | order-shadow | yes | no | 0.0000 | 0.6058 | 0.0000 | FAIL |
| role-marked causal atom | marked-atom | yes | no | 0.9000 | 0.0000 | 0.0000 | PASS-EXTRA |
| split source geometry | two-atom | no | yes | 0.9000 | 0.0000 | 0.0000 | FAIL |
| record click without modular source | partial-diamond | yes | yes | 0.0000 | 0.6058 | 0.0000 | FAIL |
| modular diamond without record | partial-diamond | yes | yes | 0.0000 | 0.0000 | 0.0000 | FAIL |
| wrong first-law shadow | diamond-germ | yes | yes | -0.9000 | 1.1547 | 0.0000 | FAIL |
| free source-unit diamond | diamond-germ | yes | yes | 0.9000 | 0.0000 | 0.1021 | FAIL |
| nonconvergent MCDI shadow | MCDI | yes | yes | 0.9000 | 0.0000 | 0.1226 | FAIL |
| modular diamond record instrument | MCDI | yes | yes | 0.9200 | 0.0000 | 0.0024 | PASS-TARGET |

The row `role-marked causal atom` is the branch-B warning in invariant form:
the same atom can be given all four labels, but the labels are not produced by
one action. The row `split source geometry` has all four numbers but not one
event. The partial-diamond rows show that record without modular source, or
modular source without record, is still not the v6 event. The wrong-orientation
and free-unit rows are the old beta/role ambiguity in first-law language.

The positive object is therefore not a causal-set atom. It is:

```text
one deletion atom of a modular causal-diamond record instrument,
whose order projection is the causal-set event.
```

Paper 1 can keep the causal-set geometry slogan only in this shadow sense:

```text
events build the causal set,
but the physical event is the modular record-diamond germ;
the causal set is its order readout.
```

This is the cleanest enriched branch-A fork found so far.

#### 5.48 MCDI reference-state campaign

The modular diamond record instrument found the right kind of object, but it
also exposed a new bottleneck. Modular structure is not free. It depends on
the local reference state:

```math
K_x=-\log\sigma_x.
```

Therefore the next frozen question is:

```text
Do fixed click/order/deletion data determine sigma_x, K_x, the modular source
response, and beta?
```

The answer is no. The diagnostic is:

```text
code/v6_p2aj_mcdi_reference_state_campaign.py
```

It builds a finite diagonal MCDI model. The clicked state `rho_x`, the
order/screen counters, and the deletion support are held fixed. Only the
full-rank reference state `sigma_x` is varied. For each `sigma_x` it computes:

```math
K_x=-\log\sigma_x,
```

```math
S(\rho_x\|\sigma_x)
=
\Delta\langle K_x\rangle-\Delta S_x,
```

and the C-lock/OER `beta` from the modular source response
`\Delta\langle K_x\rangle`.

The finite campaign prints:

| candidate | rule | fixed | Dspan | Kspan | Kfloor | beta span | FL-res | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| same data free sigma family | none | no | 0.3384 | 0.5081 | 0.3395 | 0.0962 | 0.0000 | FAIL-FREE-SIGMA |
| marked MCDI reference | supplied role marks/reference | no | 0.0000 | 0.0000 | 0.4775 | 0.0000 | 0.0000 | PASS-EXTRA |
| max-entropy sigma | maximum entropy | yes | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | FAIL |
| KMS temperature free | Gibbs form, free temperature | no | 0.3093 | 0.4254 | 0.2681 | 0.0963 | 0.0000 | FAIL-FREE-SIGMA |
| derived KMS diamond sigma | derived diamond KMS | yes | 0.0000 | 0.0000 | 0.4232 | 0.0000 | 0.0000 | PASS-TARGET |
| nonconvergent derived sigma | drifting KMS | yes | 0.0529 | 0.0725 | 0.3507 | 0.1226 | 0.0000 | FAIL |

The counterexample is the first row. The same finite click state, the same
order/screen counters, and the same deletion support admit a family of
full-rank reference states. The relative-entropy identity holds exactly in
every row:

```text
FL-res = 0.
```

Nevertheless:

```text
Delta<K_x> span = 0.5081;
beta span       = 0.0962.
```

So MCDI is not derived from click/order/deletion data alone. The reference
state is now the live object.

The second row is branch-B in modular clothing: a supplied reference closes
the finite calculation, but only because the reference was inserted. The
maximum-entropy row is instructive. It is canonical, but:

```text
sigma_x = uniform
=> K_x = constant
=> Delta<K_x> = 0,
```

so it has no source floor. A Gibbs/KMS form is not enough either if the
temperature or modular generator is free; beta moves. A derived KMS diamond
state can pass the finite target, but only conditionally:

```text
the enriched ICS event law must derive the diamond Hamiltonian/modular flow and
the KMS parameter before the source row is computed.
```

The new lock is therefore:

```text
Reference-state lock:
derive sigma_x from the same interacting modular record-diamond law.
```

The enriched branch-A closure chain becomes:

```text
enriched Physical ICS
-> local diamond algebra A_x
-> canonical reference state sigma_x
-> K_x=-log sigma_x
-> record instrument I_x and clicked state rho_x
-> deletion relative entropy
-> four first-law derivatives
-> full role Gram
-> beta.
```

If `sigma_x` is free, MCDI is branch B. If `sigma_x` is maximum entropy without
a nontrivial modular generator, source response vanishes. If `sigma_x` is a
derived, stable diamond KMS/reference state, MCDI remains the best enriched
branch-A route.

#### 5.49 Intrinsic ICS reference-state law: Dirichlet-KMS sigma

The reference-state no-go does not mean `sigma_x` is hopeless. It says exactly
what must be intrinsic. The enriched ICS diamond must supply:

```text
H_x = oriented deletion/Dirichlet Hamiltonian;
T_x = diamond KMS temperature fixed by first-law normalization.
```

Then `sigma_x` is not chosen. It is the unique finite free-energy minimizer:

```math
\sigma_x
=
\arg\min_{\sigma}
\left\{
\langle H_x\rangle_\sigma
-T_x S(\sigma)
\right\}.
```

For a finite full-support diamond algebra this gives:

```math
\sigma_x
=
{e^{-H_x/T_x}\over Z_x}.
```

This is a genuine intrinsic ICS reference-state law if, and only if, `H_x`
and `T_x` are themselves derived from the causal-diamond deletion germ. The
diagnostic is:

```text
code/v6_p2ak_ics_reference_state_law.py
```

It tests maximum entropy, external Hamiltonians, free temperature, wrong
orientation, degenerate spectra, refinement drift, and the intrinsic
Dirichlet-KMS law:

| candidate | rule | H_int | T_fix | stat | gap | Kfloor | beta span | verdict |
|---|---|---|---|---:|---:|---:|---:|---|
| maximum entropy | `H=0` | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0.0000 | FAIL |
| external Hamiltonian KMS | external H | no | yes | 0.0000 | 0.2000 | 0.5140 | 0.0000 | FAIL-EXTERNAL-H |
| intrinsic H free temperature | Dirichlet H, free T | yes | no | 0.0000 | 0.2500 | 0.2681 | 0.0963 | FAIL-FREE-T |
| reversed deletion orientation | wrong sign H | yes | yes | 0.0000 | 0.2500 | 0.0000 | 0.0000 | FAIL |
| degenerate deletion spectrum | degenerate H | yes | yes | 0.0000 | 0.0000 | 0.4756 | 0.0000 | FAIL |
| nonconvergent Dirichlet KMS | drifting H | yes | yes | 0.0000 | 0.2000 | 0.3507 | 0.1226 | FAIL |
| intrinsic Dirichlet-KMS sigma | Dirichlet H, fixed T | yes | yes | 0.0000 | 0.2500 | 0.4232 | 0.0000 | PASS-TARGET |

The `stat` column checks the finite variational equation:

```math
H_i+T(\log\sigma_i+1)={\rm constant}.
```

The positive row passes because the enriched ICS germ supplies the Hamiltonian
and the KMS temperature before the reference state is computed. The failures
are the theorem's guardrails:

- maximum entropy is canonical but has no modular source floor;
- an external Hamiltonian gives a good Gibbs state but is extra input;
- free temperature moves `beta`;
- wrong deletion orientation kills the positive source response;
- a degenerate deletion spectrum cannot isolate the modular source sector;
- refinement drift reopens the beta span.

Thus the strongest enriched branch-A theorem target is now:

```text
Dirichlet-KMS Reference-State Theorem.
Given a finite enriched Physical ICS diamond whose deletion germ derives an
oriented, spectrally isolated, refinement-stable Dirichlet Hamiltonian H_x and
a fixed diamond KMS temperature T_x, the canonical local reference state is
sigma_x = exp(-H_x/T_x)/Z_x.
```

With that law, the MCDI chain becomes:

```text
enriched ICS diamond/deletion germ
-> H_x, T_x
-> sigma_x
-> K_x=-log sigma_x
-> modular source row
-> full role Gram
-> beta.
```

This does not restore bare branch A. It gives a concrete positive route for
enriched branch A. The remaining open theorem is now one level deeper and
sharper:

```text
derive H_x and T_x intrinsically from the enriched ICS causal-diamond deletion
germ.
```

#### 5.50 Intrinsic `H_x,T_x` law: shell work and screen temperature

The previous section left a precise task. The enriched ICS causal-diamond
deletion germ must derive:

```text
H_x = deletion Hamiltonian;
T_x = diamond KMS temperature.
```

The frontal finite construction is:

```text
H_x = cumulative oriented deletion work across the diamond shells;
T_x = |delta V_x| / delta S_screen,x.
```

Here `delta V_x` is the interval-volume/order response of the same deletion
atom, and `delta S_screen,x` is the screen/antichain entropy response. The
Hamiltonian is built from the deletion/Dirichlet germ that already produced
`L_x=G_x^{-1}Q_x`: if `w_i>0` are the oriented deletion-work increments
between consecutive diamond shells, set:

```math
H_0=0,
\qquad
H_k=\sum_{i<k}w_i.
```

The temperature is the finite first-law normalization:

```math
T_x=
{|\delta V_x|\over \delta S_{{\rm screen},x}}.
```

Thus no external Hamiltonian, external temperature, or reference state is
chosen. The diagnostic is:

```text
code/v6_p2al_ics_ht_law_campaign.py
```

It attacks the construction by supplying external `H,T`, zero work, wrong
orientation, degenerate work, free work scale, free screen/volume temperature,
and refinement drift:

| candidate | rule | H_int | T_int | Hspan | Tspan | gap | Kfloor | beta span | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| external H,T supplied | external | no | no | 0.0000 | 0.0000 | 0.2500 | 0.4232 | 0.0000 | FAIL-EXTERNAL-H |
| zero deletion work | `H=0` | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | FAIL |
| wrong deletion orientation | wrong orientation | yes | yes | 0.0000 | 0.0000 | 0.2500 | 0.0000 | 0.0000 | FAIL |
| degenerate shell work | degenerate H | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0.4756 | 0.0000 | FAIL |
| free deletion-work scale | free H scale | no | yes | 0.4800 | 0.0000 | 0.1750 | 0.2610 | 0.0958 | FAIL-FREE-H-SCALE |
| free screen-volume temperature | free T | yes | no | 0.0000 | 0.6596 | 0.2500 | 0.2671 | 0.0874 | FAIL-FREE-T |
| nonconvergent shell work | drifting H | yes | yes | 0.1500 | 0.0000 | 0.2000 | 0.3507 | 0.1226 | FAIL |
| intrinsic shell-work temperature | shell work + V/S | yes | yes | 0.0000 | 0.0000 | 0.2500 | 0.4232 | 0.0000 | PASS-TARGET |

This is a positive finite derivation under explicit enriched-ICS data. The
passing row uses only:

```text
oriented deletion-work increments w_i;
screen/volume first-law responses delta V_x and delta S_screen,x.
```

The failure rows show minimality. An external `H` closes numerically but is
branch B. Zero work is maximum entropy again and has no source response. Wrong
orientation kills the positive modular source. Degenerate work loses spectral
isolation. Free work scale and free screen/volume temperature move `beta`.
Nonconvergent shell work reopens the refinement drift.

The finite theorem target can now be stated without placeholders:

**Shell-work temperature theorem.** Let an enriched finite Physical ICS
diamond provide a deletion/Dirichlet germ whose oriented shell-work increments
`w_i` are positive, scale-fixed, spectrally isolated, and refinement-stable,
and whose interval-volume and screen/antichain responses satisfy
`\delta S_screen>0`. Then:

```math
H_0=0,
\quad
H_k=\sum_{i<k}w_i,
\quad
T_x={|\delta V_x|\over\delta S_{{\rm screen},x}},
\quad
\sigma_x={e^{-H_x/T_x}\over Z_x}
```

are intrinsic finite functions of the enriched ICS causal-diamond deletion
germ. The resulting modular source row and `beta` are fixed on the positive
margin region.

This is the strongest branch-A-enriched result so far. It still does not
restore bare branch A. It says exactly what the enriched object must contain:

```text
not just order + deletion,
but oriented deletion work + screen/volume first-law normalization.
```

#### 5.51 Shell-work proof campaign

The previous section still sounded like an assumption unless the work and
temperature are explicitly recovered from the deletion germ. The frontal proof
campaign freezes the question:

```text
Can enriched ICS derive oriented shell-work increments and screen/volume
normalization from the causal-diamond deletion germ itself?
```

The finite proof route is:

```text
1. use causal order to form canonical nested diamond shells;
2. compute the local log Radon-Nikodym deletion action A_k on retained shells;
3. define shell work by action increments w_i=A_{i+1}-A_i;
4. fix the action scale because A_k is a log likelihood / RN action;
5. use count-normalized screen entropy and interval volume to set
   T_x=|delta V_x|/delta S_screen,x.
```

The diagnostic is:

```text
code/v6_p2am_ics_shell_work_proof_campaign.py
```

It tests order-only shells, external action tables, ambiguous shell
filtrations, nonmonotone action, free RN action scale, free screen entropy
unit, refinement drift, and the RN shell-work proof:

| candidate | rule | shells | RN | scale | wfloor | Hspan | Tspan | beta span | verdict |
|---|---|---|---|---|---:|---:|---:|---:|---|
| order-only shells | no action | yes | no | yes | 0.0000 | 0.0000 | 0.0000 | 0.0000 | FAIL-NO-RN |
| external shell action | external A | yes | no | yes | 0.2500 | 0.0000 | 0.0000 | 0.0000 | FAIL-NO-RN |
| ambiguous shell filtration | no rank lock | no | yes | yes | 0.2500 | 0.0000 | 0.0000 | 0.0000 | FAIL-SHELLS |
| nonmonotone deletion action | negative work | yes | yes | yes | -0.1000 | 0.0000 | 0.0000 | 0.0000 | FAIL |
| free RN action scale | free log unit | yes | yes | no | 0.1750 | 0.4800 | 0.0000 | 0.0958 | FAIL-FREE-A-SCALE |
| free screen entropy unit | free entropy unit | yes | yes | no | 0.2500 | 0.0000 | 0.6307 | 0.0885 | FAIL-FREE-S-UNIT |
| nonconvergent shell action | drifting A | yes | yes | yes | 0.2000 | 0.1500 | 0.0000 | 0.1226 | FAIL |
| RN shell-work proof | ranked RN A + count S | yes | yes | yes | 0.2500 | 0.0000 | 0.0000 | 0.0000 | PASS-THEOREM |

Thus the theorem can be stated positively.

**RN shell-work theorem.** Let an enriched finite Physical ICS diamond provide:

```text
1. a canonical causal-rank shell filtration of the local diamond;
2. a finite log Radon-Nikodym deletion action A_k on the nested retained
   shell collars;
3. positive action increments A_{k+1}-A_k >= w_* > 0;
4. fixed count entropy units for the screen/antichain readout;
5. intrinsic interval-volume and screen responses with delta S_screen>0;
6. refinement-stable shell action and screen/volume responses.
```

Then:

```math
w_k=A_{k+1}-A_k,
\qquad
H_0=0,\quad H_j=\sum_{k<j}w_k,
\qquad
T_x={|\delta V_x|\over\delta S_{{\rm screen},x}}
```

are intrinsic finite functions of the enriched ICS causal-diamond deletion
germ. Feeding them into the Dirichlet-KMS reference-state law gives:

```math
\sigma_x={e^{-H_x/T_x}\over Z_x}
```

and fixes the modular source row and `beta` on the positive-margin region.

The proof is finite bookkeeping. A canonical shell filtration makes the
nested collars invariant. The RN action supplies scale-fixed logarithmic units
in nats, so multiplying `A_k` by a free constant is not allowed. Positive
increments orient the Hamiltonian and give a source floor. Count entropy fixes
the screen unit, so the screen/volume ratio fixes `T_x`. Refinement stability
passes these finite values to the cofinal limit.

The failure rows show that every clause is load-bearing. Order-only shells do
not supply work. External action tables are branch B. Ambiguous shells do not
define a unique Hamiltonian. Nonmonotone action has no positive source
orientation. Free log units or entropy units move `beta`. Drift reopens the
scale family.

This is the first finite proof that the enriched ICS deletion germ can derive
the full modular reference chain, provided the germ is genuinely RN-shell
structured:

```text
canonical shells
-> RN deletion action A_k
-> shell work w_k
-> H_x
-> T_x from screen/volume counts
-> sigma_x
-> modular source row
-> beta.
```

#### 5.52 Modular Deletion Profile theorem campaign

The shell-work theorem can now be compressed into one invariant candidate. Do
not start with `H_x`, `T_x`, `sigma_x`, or `beta`. Start with the finite
causal-diamond deletion profile itself.

Let `\mathcal F_{x,k}` be the canonical nested causal-rank shell algebra of
the diamond around `x`. Let `P_x` be the retained-event local law and
`P_{\setminus x}` the deleted-event local law on the same retained collar
image. Define:

```math
M_x(k)
=
D_{\rm KL}
\!\left(
P_x|_{\mathcal F_{x,k}}
\;\|\;
P_{\setminus x}|_{\mathcal F_{x,k}}
\right).
```

This is the **Modular Deletion Profile**. Its local RN coordinate is:

```math
A_{x,k}
=
\log
{dP_x|_{\mathcal F_{x,k}}
\over
dP_{\setminus x}|_{\mathcal F_{x,k}}}.
```

The finite diagnostic is:

```text
code/v6_p2an_modular_deletion_profile_campaign.py
```

It tests order-only data, singular deletion, ambiguous shell order,
total-only deletion entropy, non-isolated profiles, free screen entropy units,
refinement drift, and the full modular deletion profile:

| candidate | rule | MDP | RN | chain | iso | wfloor | chainerr | beta span | verdict |
|---|---|---|---|---|---|---:|---:|---:|---|
| order-only ICS | no P/Q contrast | no | yes | yes | no | 0.0000 | 0.0000 | 0.0000 | FAIL-NO-MDP |
| singular deletion | P not << Q | yes | no | no | no | inf | inf | 0.0000 | FAIL-SINGULAR |
| ambiguous shell order | two filtrations | yes | yes | yes | yes | 0.1494 | 0.0000 | 0.0033 | FAIL-FILTRATION |
| total deletion entropy | only M(K) | no | yes | yes | no | 0.0500 | 0.0000 | 0.0044 | FAIL-TOTAL-ONLY |
| non-isolated MDP | flat shell profile | yes | yes | yes | no | 0.2200 | 0.0000 | 0.0000 | FAIL-NO-ISOLATION |
| free screen entropy unit | free count unit | yes | yes | yes | yes | 0.1494 | 0.0000 | 0.0825 | FAIL-FREE-S-UNIT |
| refinement-drifting MDP | profile drift | yes | yes | yes | yes | 0.1494 | 0.0000 | 0.1226 | FAIL-DRIFT |
| modular deletion profile | finite KL chain | yes | yes | yes | yes | 0.1494 | 0.0000 | 0.0000 | PASS-THEOREM |

The key finite identity is not a new physical assumption; it is the chain rule
for relative entropy. For a finite canonical filtration with:

```math
P_x|_{\mathcal F_{x,k}}
\ll
P_{\setminus x}|_{\mathcal F_{x,k}},
```

one has:

```math
M_x(k+1)-M_x(k)
=
\mathbb E_{P_x}
\left[
D_{\rm KL}
\!\left(
P_x(S_{k+1}\mid\mathcal F_{x,k})
\;\|\;
P_{\setminus x}(S_{k+1}\mid\mathcal F_{x,k})
\right)
\right]
\ge 0.
```

Thus the shell work is forced:

```math
w_{x,k}=M_x(k+1)-M_x(k).
```

The logarithmic unit is fixed because `M_x` is a KL/RN object, not a
regraduated stability score. This is exactly the invariant that covers the
load-bearing parts of the previous theorem:

```text
canonical shells        = the filtration F_{x,k};
RN deletion action      = A_{x,k}=log dP_x/dP_{\setminus x};
shell work              = w_{x,k}=M_x(k+1)-M_x(k);
positive orientation    = conditional relative entropy;
Hamiltonian             = H_j=sum_{k<j} w_{x,k};
temperature             = |delta V_x|/delta S_screen,x on the same shell algebra;
reference state         = sigma_x=exp(-H_x/T_x)/Z_x;
source/beta             = modular source response, if the profile has an isolated first scale.
```

This gives the positive finite theorem.

**Modular Deletion Profile theorem.** Let an enriched finite Physical ICS
diamond supply:

```text
1. a canonical causal-rank shell filtration F_{x,k};
2. retained and deleted local laws P_x and P_{\setminus x} on the same
   retained collar image;
3. local absolute continuity P_x|F_{x,k} << P_{\setminus x}|F_{x,k};
4. strict positive conditional entropy increments w_{x,k} >= w_* > 0;
5. an isolated first profile scale;
6. fixed count entropy units and intrinsic screen/volume responses;
7. refinement convergence of M_{n,x}(k), screen response, and volume response.
```

Then `M_x(k)` intrinsically derives `A_{x,k}`, `w_{x,k}`, `H_x`, `T_x`,
`\sigma_x`, the modular source row, and `beta` on the positive-margin region.

The failure rows are the important part. Bare causal order does not define a
retained/deleted likelihood contrast. Singular deletion has no finite local RN
coordinate. Ambiguous filtrations produce different profiles. A scalar total
`M_x(K)` is too weak: the script prints two laws with the same total deletion
entropy,

```text
M=(0.0,0.05,0.30,0.75), w=(0.05,0.25,0.45);
M=(0.0,0.25,0.50,0.75), w=(0.25,0.25,0.25),
```

and different modular readouts. A flat profile has positive deletion entropy
but no isolated first scale. Free count units move `T_x` and `beta`. Drift
reopens the scale family.

So the theorem/refutation boundary is now exact:

```text
Full MDP + canonical shells + finite RN + isolated profile scale + fixed
screen/volume units + convergence: positive enriched branch-A theorem.

Order-only ICS, singular deletion, total-only deletion entropy, non-isolated
profile, free count unit, or drifting profile: refuted as branch-A closure.
```

This is not another mutated target. It is the compressed theorem behind the
last several sections. The open Physical-ICS problem is now only whether the
actual enriched event germ supplies this modular deletion profile cofinally.

#### 5.53 Attack on the actual missing assumption

The remaining assumption is now explicit:

```text
Does the proposed Physical ICS primitive intrinsically supply
F_{x,k}, P_x, and P_{\setminus x}?
```

Here:

```text
F_{x,k}          = canonical causal-diamond shell filtration;
P_x              = retained-event local law;
P_{\setminus x}  = deleted-event local law on the retained collar image.
```

The finite diagnostic is:

```text
code/v6_p2ao_mdp_missing_assumption_attack.py
```

It holds the order/deletion shadow fixed and varies only the objects that a
bare causal set does not determine:

| candidate | rule | order | F | P | Q | RN | Mspan | beta span | verdict |
|---|---|---|---|---|---|---|---:|---:|---|
| bare order/deletion shadow | order only | yes | no | no | no | yes | 0.0000 | 0.0000 | FAIL-NO-MDP |
| same order, P varies | P not derived | yes | yes | no | yes | yes | 0.4475 | 0.0720 | FAIL-P-FREE |
| same order, Q varies | deleted law free | yes | yes | yes | no | yes | 0.4550 | 0.0265 | FAIL-Q-FREE |
| same law, F varies | filtration free | yes | no | yes | yes | yes | 0.3849 | 0.0078 | FAIL-FREE-F |
| singular deleted support | P not << Q | yes | yes | yes | yes | no | 0.0000 | 0.0000 | FAIL-NO-RN |
| non-isolated profile | flat profile | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | FAIL-NO-ISOLATION |
| free count unit | screen unit free | yes | yes | yes | yes | yes | 0.0000 | 0.0898 | FAIL-FREE-COUNT |
| refinement-drifting law | not cofinal | yes | yes | yes | yes | yes | 0.1066 | 0.1226 | FAIL-DRIFT |
| Modular Physical ICS | primitive MDP | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | PASS-CONDITIONAL |

The same-shadow witnesses are decisive. With the same order shadow and same
deleted-law shadow, changing only the retained local law gives:

```text
M=(-0.0,0.1494,0.4842,1.0184), w=(0.1494,0.3348,0.5343), beta=0.5828;
M=(-0.0,0.2580,0.4418,0.5710), w=(0.2580,0.1838,0.1292), beta=0.5108.
```

With the same order shadow and same retained law, changing only the deleted
law gives:

```text
M=(-0.0,0.1494,0.4842,1.0184), w=(0.1494,0.3348,0.5343), beta=0.5828;
M=(0.0,0.2835,0.7091,1.2434), w=(0.2835,0.4256,0.5343), beta=0.6093.
```

With the same retained/deleted laws, changing only the shell filtration gives
different profiles:

```text
M=(-0.0,0.1494,0.4842,1.0184), w=(0.1494,0.3348,0.5343);
M=(-0.0,0.5343,0.8691,1.0184), w=(0.5343,0.3348,0.1494).
```

This proves the negative half:

```text
Bare order/deletion shadow does not determine the Modular Deletion Profile.
```

No manipulation of causal order alone derives `P_x`, `P_{\setminus x}`, or
the canonical shell algebra used by the MDP. Therefore bare ICS is not the
right branch-A base if "ICS" means only a locally finite partial order with
deletion. The surviving object is richer:

```text
Modular Physical ICS =
causal order projection
+ canonical causal-diamond shell filtration
+ retained/deleted local record laws
+ finite RN deletion profile
+ fixed screen/volume count response.
```

Equivalently, the primitive is a **causal-diamond deletion germ**; the causal
set is its order shadow.

#### 5.54 Consolidated branch-A-enriched theorem

The previous sections should now be read as audit history for one theorem,
not as a growing list of selectors. The base is renamed:

```text
Bare ICS:
    a locally finite causal order, possibly with induced deletion.

Modular Physical ICS:
    a finite causal-diamond deletion germ whose order projection is a causal
    set and whose retained/deleted local laws define an MDP.
```

The consolidated theorem is:

**Branch-A-enriched MDP theorem.** Suppose a cofinal family of finite Modular
Physical ICS germs supplies, for each candidate event `x`:

```text
1. canonical causal-diamond shell algebras F_{n,x,k};
2. retained/deleted local laws P_{n,x} and P_{n,\setminus x};
3. finite RN absolute continuity on each shell;
4. the modular deletion profile
   M_{n,x}(k)=D(P_{n,x}|F_{n,x,k} || P_{n,\setminus x}|F_{n,x,k});
5. strict positive conditional increments w_{n,x,k}=M_{n,x}(k+1)-M_{n,x}(k);
6. an isolated first profile scale;
7. fixed screen/volume count units;
8. spacelike factorization of local deletion actions;
9. cofinal convergence of M, screen response, volume response, and the
   modular source row.
```

Then the event law, source law, and memory scale are finite functions of the
same invariant object:

```text
event threshold     = positive stable deletion component;
gamma_n             = density of positive stable components;
A_{n,x,k}           = log dP_{n,x}/dP_{n,\setminus x};
w_{n,x,k}           = M_{n,x}(k+1)-M_{n,x}(k);
H_{n,x}             = cumulative shell work;
T_{n,x}             = |delta V_{n,x}|/delta S_screen,n,x;
sigma_{n,x}         = exp(-H_{n,x}/T_{n,x})/Z_{n,x};
kappa_G,n           = modular/source deletion response;
beta_n              = isolated first memory scale from the same MDP;
TS residue          = 0 in the spacelike factorization limit.
```

In this theorem, the four roles are not four ledgers:

```text
record     = retained/deleted distinguishability;
source     = modular deletion response;
causal     = shell/order profile;
antichain  = screen-count response.
```

They are readouts of `M_{n,x}` and its fixed local derivatives. The proof is
finite measure theory plus the previous finite gates. The KL chain rule gives
positive shell work and fixes the logarithmic action scale. The Dirichlet-KMS
law gives `sigma`. The modular source response gives `kappa_G`. The isolated
first profile scale gives `beta`. Spacelike factorization gives the TS gate.
Cofinal convergence gives a physical limit.

The audit history now has a precise role. Sections §5.23-§5.53 do not keep
changing the target theorem. They show why every assumption in the theorem is
load-bearing:

```text
support-only data fail;
scalar A_x(0) fails;
full germ without canonical role sectors fails;
order-only ICS fails;
free reference state fails;
free H/T fails;
free RN shell action fails;
total-only deletion entropy fails;
free retained law, deleted law, or shell filtration fails.
```

Therefore the branch verdict is:

```text
Bare branch A: refuted under current assumptions.
Branch A-enriched: alive exactly as the Modular Physical ICS / MDP theorem.
Branch B: required if P_x, P_{\setminus x}, F_{x,k}, fixed count units, or
isolated profile scale are supplied externally.
```

#### 5.55 Origin closure for `P_x`, `P_{\setminus x}`, and `F_{x,k}`

The final repair attempt is to ask whether the three missing objects can be
derived after all:

```text
P_x:             retained-event local law;
P_{\setminus x}: deleted-event local law;
F_{x,k}:         causal-diamond shell filtration.
```

The finite diagnostic is:

```text
code/v6_p2ap_pqf_origin_closure_campaign.py
```

It tests direct order-only, deletion-pushforward, same-shadow families, chosen
rank-shell functors, competing shell functors, and the full Modular Physical
ICS germ:

| target | candidate | rule | derives | unique | internal | Mspan | beta span | verdict |
|---|---|---|---|---|---|---:|---:|---|
| P | order-only maximum entropy | uniform/order law | no | yes | no | 0.0000 | 0.0000 | FAIL-NO-P |
| P | same order P-family | P varies | no | no | no | 0.4475 | 0.0720 | FAIL-NONUNIQUE-P |
| P | retained record law in germ | P primitive | yes | yes | yes | 0.0000 | 0.0000 | PASS-CONDITIONAL |
| Q | deletion pushforward | Q=D_*P | no | yes | no | 0.0000 | 0.0000 | FAIL-NO-Q |
| Q | same order Q-family | Q varies | no | no | no | 0.2250 | 0.0265 | FAIL-NONUNIQUE-Q |
| Q | deleted RN law in germ | Q primitive | yes | yes | yes | 0.0000 | 0.0000 | PASS-CONDITIONAL |
| F | chosen order-rank functor | rank shells chosen | yes | yes | no | 0.0000 | 0.0000 | PASS-F-ONLY |
| F | competing shell functors | rank choice free | yes | no | no | 0.3849 | 0.0078 | FAIL-NONUNIQUE-F |
| F | canonical shell functor in germ | F primitive | yes | yes | yes | 0.0000 | 0.0000 | PASS-CONDITIONAL |

The three outcomes are different.

**Retained law `P_x`.** Bare order cannot derive a probability law. On the
same order, same deleted law, and same shell filtration, the script gives:

```text
M=(-0.0,0.1494,0.4842,1.0184), w=(0.1494,0.3348,0.5343), beta=0.5828;
M=(-0.0,0.2580,0.4418,0.5710), w=(0.2580,0.1838,0.1292), beta=0.5108.
```

Thus `P_x` is not a function of order. A maximum-entropy or uniform law is a
convention, not the physical retained-event law, and it carries no deletion
contrast unless a deleted law is added.

**Deleted law `P_{\setminus x}`.** The deletion map alone is only a map of
collars. It is not a probability law on the deleted collar. The pushforward
choice `Q=D_*P` gives no event contrast. On the same order, same retained law,
and same shell filtration, a different deleted law gives:

```text
M=(-0.0,0.1494,0.4842,1.0184), w=(0.1494,0.3348,0.5343), beta=0.5828;
M=(0.0,0.2835,0.7091,1.2434), w=(0.2835,0.4256,0.5343), beta=0.6093.
```

Thus `P_{\setminus x}` is not a function of the deletion shadow. It must come
from a physical deleted-event dynamics or from the same modular deletion germ.

**Shell filtration `F_{x,k}`.** This is the only partial positive result.
Once an order-rank shell functor is specified, `F_{x,k}` is a finite
order-invariant construction. But bare order does not select the physical
functor. With the same retained/deleted laws and same order shadow:

```text
M=(-0.0,0.1494,0.4842,1.0184), w=(0.1494,0.3348,0.5343);
M=(-0.0,0.5343,0.8691,1.0184), w=(0.5343,0.3348,0.1494).
```

So `F_{x,k}` is derivable only after a canonical shell/rank rule is part of
the physical germ or proved by a stronger order principle. Order alone gives
many invariant shell functors, not the one used by the MDP.

This fully closes the repair campaign:

```text
P_x from bare order: falsified.
P_{\setminus x} from deletion shadow: falsified.
F_{x,k} from bare order: partial positive after a chosen shell functor,
but unique physical F is not selected by bare order.
```

The only full positive row is:

```text
Modular Physical ICS:
P_x, P_{\setminus x}, and F_{x,k} are intrinsic parts of one
causal-diamond deletion germ.
```

This is not a cosmetic rename. It is the minimal base left after the finite
no-gos. Bare ICS cannot be repaired into the full branch-A theorem by clever
postprocessing of order and deletion. The physical law must either derive the
Modular Physical ICS germ from a still deeper record dynamics, or accept it as
the branch-B-enriched primitive.

#### 5.56 Honest ISP base campaign: upstream of ICS

The previous result says that bare ICS is the wrong base. The next question is
not how to rescue causal order, but what a real ISP base would have to be so
that Modular Physical ICS is generated rather than postulated.

The finite diagnostic is:

```text
code/v6_p2aq_honest_isp_base_campaign.py
```

It compares candidate bases by whether they actually generate:

```text
P_x;
P_{\setminus x};
F_{x,k};
gravity/source response;
fixed beta selector;
spacelike TS factorization;
cofinal convergence.
```

The audit is:

| candidate | rule | P | Q | F | grav | fixed | TS | iso | beta span | verdict |
|---|---|---|---|---|---|---|---|---:|---:|---|
| bare ICS | order shadow | no | no | no | no | no | yes | 0.0000 | 0.0000 | FAIL-NO-PROCESS |
| Poisson causal set | geometry law | yes | no | yes | no | no | yes | 0.0000 | 0.0000 | FAIL-NO-DELETION-LAW |
| collapse flash kernel | free kernel | yes | yes | yes | yes | no | yes | 0.0742 | 0.0720 | FAIL-NO-ACTION |
| Modular Physical ICS | MDP primitive | yes | yes | yes | yes | yes | yes | 0.1995 | 0.0000 | PASS-ENRICHED-PRIMITIVE |
| free local record instrument | free action coeff | yes | yes | yes | yes | no | yes | 0.0742 | 0.0720 | FAIL-FREE-COEFF |
| free gravity response action | free grav coeff | yes | yes | yes | yes | no | yes | 0.1086 | 0.0265 | FAIL-FREE-COEFF |
| non-isolated modular process | flat profile | yes | yes | yes | yes | no | yes | 0.0000 | 0.0000 | FAIL |
| nonfactorizing record process | TS fail | yes | yes | yes | yes | yes | no | 0.1995 | 0.0000 | FAIL-TS |
| nonconvergent record process | not cofinal | yes | yes | yes | yes | yes | yes | 0.1254 | 0.1226 | FAIL-DRIFT |
| Cofinal Modular Record Process | fixed variational law | yes | yes | yes | yes | yes | yes | 0.1995 | 0.0000 | PASS-BASE-TARGET |

The surviving upstream target is:

```text
Cofinal Modular Record Process (CMRP).
```

This is the first honest ISP-shaped base in the campaign. Its primitive is not
a causal set. Its primitive is a cofinal family of finite covariant record
processes on causal diamonds:

```text
R_n(D)          = finite local record algebra of a causal diamond D;
P_n             = covariant record-history measure;
D_x             = local deletion/disintegration operation;
F_{n,x,k}       = canonical causal-diamond shell functor;
I_n             = fixed modular record-gravity action;
P_{n,x},Q_{n,x} = retained/deleted laws from the minimizer/disintegration;
M_{n,x}(k)      = deletion relative-entropy profile.
```

The intended derivation chain is:

```text
Cofinal Modular Record Process
-> local process measure P
-> deletion/disintegration law P_delete
-> canonical causal-diamond shell functor F
-> Modular Deletion Profile M(k)
-> event threshold, gamma, H, T, sigma, kappa_G
-> isolated first profile scale beta
-> ICS as order projection
-> gravity as screen/volume modular response.
```

The finite theorem target is:

**CMRP theorem target.** Suppose a cofinal family of finite record processes
has:

```text
1. local covariance of the record algebras R_n(D);
2. a fixed, coefficient-free, modular record-gravity action I_n;
3. a unique stable minimizer/stationary law P_n;
4. intrinsic deletion/disintegration kernels D_x producing Q_{n,x};
5. canonical causal-diamond shell functors F_{n,x,k};
6. finite RN absolute continuity P_{n,x}|F << Q_{n,x}|F;
7. strict positive and isolated MDP increments;
8. fixed screen/volume count response in the same action;
9. spacelike factorization of deletion actions;
10. cofinal convergence.
```

Then CMRP derives Modular Physical ICS and the full branch-A-enriched MDP
chain. In that case:

```text
ICS is not the physical base.
ICS is the order projection of the stable deletion atoms of CMRP.
```

The failure rows are the warning. A Poisson causal set supplies geometry but
not a retained/deleted record law. A collapse flash kernel supplies events but
leaves kernel parameters free. A local record instrument with free coefficients
is branch B in more elegant clothing. A modular process without isolated
profile leaves `beta` free. A nonfactorizing process fails TS integrability.
Drift kills the limit.

Thus the campaign's answer is:

```text
Real branch-A revival, if any, is not ICS -> physics.
It is CMRP -> Modular Physical ICS -> ICS order shadow -> geometry.
```

This does not prove CMRP exists in the established ISP reconstruction. It
names the exact deeper law that would have to be proved. If the fixed
variational record-gravity action is not derived, then the honest theory is
branch B with a physically motivated modular record kernel.

#### 5.57 CMRP action derivation campaign

The previous section left one precise missing object:

```text
a fixed covariant modular record-gravity action for CMRP.
```

This cannot be a decorative action written after the event law has already
been selected. It must generate the retained law `P_x`, the deleted law
`P_{\setminus x}`, the shell filtration `F_{x,k}`, the modular deletion
profile, the screen/volume gravity response, and the isolated scale. The
finite diagnostic is:

```text
code/v6_p2ar_cmrp_action_derivation_campaign.py
```

The audit compares action candidates by whether they have:

```text
local covariance;
finite record algebra;
intrinsic deletion/disintegration;
KL/RN record term;
count-normalized screen/volume gravity term;
fixed coefficients;
spacelike additivity;
isolated profile scale;
cofinal stability;
upstream status relative to Modular Physical ICS.
```

The finite result is:

| candidate | rule | cov | del | KL | grav | coeff | TS | iso | beta span | verdict |
|---|---|---|---|---|---|---|---|---:|---:|---|
| entropy-only action | max entropy | yes | no | no | no | yes | yes | 0.0000 | 0.0000 | FAIL-NO-DELETION |
| order-volume action | geometry only | yes | no | no | yes | yes | yes | 0.0000 | 0.0000 | FAIL-NO-RECORD |
| record KL only | no gravity term | yes | yes | yes | no | yes | yes | 0.1995 | 0.0000 | FAIL-NO-GRAV |
| collapse kernel action | kernel chosen | yes | yes | no | yes | no | yes | 0.0742 | 0.0720 | FAIL-NO-KL |
| free record coefficient | record weight free | yes | yes | yes | yes | no | yes | 0.0742 | 0.0720 | FAIL-FREE-COEFF |
| free gravity coefficient | gravity weight free | yes | yes | yes | yes | no | yes | 0.1086 | 0.0265 | FAIL-FREE-COEFF |
| nonlocal action | nonadditive | yes | yes | yes | yes | yes | no | 0.1995 | 0.0000 | FAIL-TS |
| non-isolated fixed action | flat MDP | yes | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | FAIL-NO-ISOLATION |
| drifting fixed action | not cofinal | yes | yes | yes | yes | yes | yes | 0.1254 | 0.1226 | FAIL-DRIFT |
| Modular Physical ICS action | action input | yes | yes | yes | yes | yes | yes | 0.1995 | 0.0000 | PASS-ENRICHED-INPUT |
| fixed CMRP action | KL + count action | yes | yes | yes | yes | yes | yes | 0.1995 | 0.0000 | PASS-ACTION-TARGET |

The only upstream passing target is the fixed CMRP action. Its skeleton is:

```text
I_D(P,D_x,F)
= KL/RN deletion record action
+ count-normalized screen/volume gravity response
+ spacelike-additive locality constraint
+ cofinal stability constraint.
```

In shell form this is the same invariant already isolated by the Modular
Deletion Profile campaign:

```math
M_x(k)
=
D\!\left(P_x|F_{x,k}\,\|\,P_{\setminus x}|F_{x,k}\right),
\qquad
w_x(k)=M_x(k+1)-M_x(k).
```

The record part is fixed by finite Radon-Nikodym deletion action in logarithmic
units. The gravity part is fixed only if the screen/volume response is counted
in the same finite entropy units. Spacelike additivity is not optional: without
it the action cannot be TS-integrable. Cofinal stability is also not optional:
without it the selected scale drifts under refinement.

This gives a conditional positive theorem:

**CMRP fixed-action theorem target.** If a cofinal finite record process has
local covariant record algebras, intrinsic deletion disintegrations,
canonical shell functors, finite RN absolute continuity, KL/RN additivity,
count-normalized screen/volume response, no tunable action coefficients,
spacelike factorization, isolated positive MDP increments, and cofinal
convergence, then the action form above derives the Modular Physical ICS germ
and fixes the branch-A-enriched chain:

```text
P_x, P_{\setminus x}, F_{x,k}
-> M_x(k)
-> gamma, sigma_x, H_x, T_x, kappa_G
-> beta
-> geometry/source/screen readouts.
```

The same audit gives the refutation boundary. Entropy-only and geometry-only
actions do not produce retained/deleted record laws. KL without the gravity
term cannot source the screen response. A collapse kernel or any free record
or gravity coefficient reintroduces the same-beta problem under a new name.
Nonlocal action fails the spacelike loop. Non-isolated profiles leave `beta`
unselected. Drifting profiles fail the continuum limit.

Therefore the action campaign does not prove that established ISP dynamics
already contains CMRP. It proves the exact branch-A price:

```text
CMRP must derive the KL/RN deletion action and the count-normalized
screen/volume gravity response as one coefficient-free covariant action.
```

If any record weight, gravity weight, kernel width, temperature unit, or
screen count unit is chosen after the fact, the construction is branch B.

#### 5.58 Sealed causal-diamond deletion experiment

The previous campaigns are technically precise, but they risk hiding the
physical idea under notation. The Einstein-style version is this:

```text
Put the observer inside a closed causal diamond.
Give them records, order, source receipts, and screen/volume counts.
Do not give them an external slicing, sector labels, or a detector kernel.
Ask what invariant remains when one event x is deleted.
```

The finite diagnostic is:

```text
code/v6_p2as_sealed_diamond_invariant_campaign.py
```

It asks whether four candidate readouts:

```text
record, source, causal-order, screen/volume
```

are the same physical event only by label, or because they have the same
internal deletion response. The tested invariant is the full shell profile:

```math
M_x(k)
=
D\!\left(P_x|F_{x,k}\,\|\,P_{\setminus x}|F_{x,k}\right).
```

The audit is:

| candidate | rule | del | shell | blind | slice | units | role gap | total gap | iso | beta span | verdict |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| order-only sealed diamond | same order | no | no | yes | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0.0000 | FAIL-NO-DELETION |
| same count, split roles | role labels | yes | yes | no | yes | yes | 0.1144 | 0.1144 | 0.1665 | 0.0130 | FAIL-SECTOR-LABELS |
| same total entropy | total only | yes | yes | yes | yes | yes | 0.0907 | 0.0000 | 0.2203 | 0.0013 | FAIL-ROLE-SPLIT |
| same order, different profile | order shadow | yes | yes | yes | yes | yes | 0.0407 | 0.0000 | 0.2203 | 0.0024 | FAIL-ROLE-SPLIT |
| preferred slicing diamond | time shell | yes | yes | yes | no | yes | 0.0000 | 0.0000 | 0.2203 | 0.0000 | FAIL-PREFERRED-SLICE |
| free screen unit diamond | unit chosen | yes | yes | yes | yes | no | 0.0000 | 0.0000 | 0.2203 | 0.0000 | FAIL-FREE-UNITS |
| non-isolated deletion profile | flat shell work | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | 0.0000 | 0.0000 | FAIL-NO-ISOLATION |
| refinement-drifting profile | not cofinal | yes | yes | yes | yes | yes | 0.1664 | 0.1664 | 0.1800 | 0.1226 | FAIL-DRIFT |
| sealed deletion profile | role-blind MDP | yes | yes | yes | yes | yes | 0.0000 | 0.0000 | 0.2203 | 0.0000 | PASS-SEALED-INVARIANT |

The result is the finite version of the intended equivalence principle:

```text
Inside a closed causal diamond, external sector labels and external slicings
are not observables. Two descriptions are physically equivalent only when
their full deletion profiles agree on the intrinsic shell filtration.
```

This is the ISP analogue of the enclosed-space move. The observer cannot ask
whether `x` is "really" a detector click, source flash, causal-set atom, or
screen unit. They can only compare the closed-diamond laws with and without
`x`. If the deletion profile is the same under all four readouts, the four
roles are one fact. If the profiles differ, the roles are merely coupled
sectors.

This explains why the earlier weaker invariants failed:

```text
same causal order          does not give P_x or P_{\setminus x};
same event count           does not give the source/screen response;
same total deletion entropy does not give shell work or beta;
same sector labels         do not make the four roles one event;
same profile without fixed units still leaves branch-B coefficients;
same profile without isolation leaves beta unselected;
same profile without cofinal stability drifts under refinement.
```

Thus the candidate principle is:

```text
Sealed-diamond deletion equivalence:
one physical event is an indivisible deletion fact whose local modular
deletion profile is invariant under readout, sector decomposition, and
spacelike hypersurface interpolation.
```

If true, it is the conceptual source of the CMRP action packet:

```text
sealed deletion equivalence
-> role-blind MDP
-> KL/RN deletion action
-> shell work, H_x, T_x, sigma_x
-> kappa_G and beta
-> one event with record/source/causal/screen readouts.
```

This is not yet a proof that CMRP exists. It is the cleanest invariant
principle found so far for why CMRP, rather than bare ICS or a collapse kernel,
is the right branch-A-enriched target. Paper 3 develops this target as a
separate ontology: modular record diamonds generated by a sealed CMRP, with
ordinary ICS as the order shadow. Its Feynman-route audit further sharpens
the ontology: the scalar MDP is an action/readout, while the complete local
object is the full sealed deletion germ `(P_x,P_{\setminus x},F_{x,k},...)`.

---

### 6. What this part does not claim

It does not prove the interacting indivisible reconstruction is Lorentz-covariant; it does not construct a
relativistic interacting ISP; it does not solve the A/B fork or couple to gravity. It **reframes** Paper 1's
§10 residue as the central open problem of relativistic collapse models *with* ICS structure; **runs §3** (Q1
gated by the localization observable, in 1+1 and 3+1); and **ports the 2025 covariant recipe into ICS (§4)**,
which: dissolves the §3 Hegerfeldt tension by using a **local field operator `:φ̂²:`** (sharp + covariant +
microcausal + mass-density limit, resolving Q1 and the localization horn of Q3); **selects a worked
quartic template** `ĝ(q²)=e^{−q⁴/β⁴}` inside the broader admissible two-sided decay class (correcting Paper 1
§6, whose Gaussian was non-covariant); and matches
normal-ordering to "no vacuum division events" (AS4 / §5.5). What it does **not** do: it does not establish that the
recipe is an ISP *reconstruction* rather than a *modification* — the recipe is a collapse model (free `(γ,β)`,
energy `∝N`), so **v6, as ported, is a covariant collapse model whose flashes source semiclassical gravity, not
a derivation of GR from pure QM reconstruction.** The honest standing: **the observable is fixed and the
memory class is constrained; `β` is conditionally derived from finite OER/C-lock for a full pre-threshold
role-Gram law, but the current reduced event data provably do not derive that full Gram law or `β`. The finite
closure ledger now gates all currently actionable loopholes: support-only, post-source, independent-source,
nonlocal-tail, nonlinear, adaptive-threshold, nonconvergent, and weak-source variants all fail. The final
construction-exhaustion audit adds a conditional no-go: known fixed-background local-QFT, locally covariant
stress/RCE, relativistic collapse/flash, causal-set-first, and coupled-source routes do not derive the required
full Gram unless it is added as a primitive. The best surviving invariant-law guess is the IDA/modular
causal-diamond atom: a local deletion relative-entropy action whose four deformation derivatives are the four
roles and whose Fisher/Hessian matrix is the full Gram. The IDA proof program sharpens this further:
`A_x(0)` alone is falsified by same-scalar/different-beta counterexamples, so the live object is the full local
IDA germ. The full-germ attack sharpens it again: `P_n,D_x,A_x(0)` do not determine the germ unless the four
score directions are canonical, labeled, normalized, and convergent. The role-sector origin attack sharpens it
one final time: the canonical sector operator `L_x` must itself be intrinsic to Physical-ICS deletion dynamics,
not externally chosen. The Dirichlet campaign gives the first intrinsic construction:
`L_x=G_x^{-1}Q_x`, with `G_x` the IDA Fisher metric and `Q_x` the deletion Dirichlet form. It also shows the
remaining conditions: isolated eigenmodes, intrinsic stable signature labels, positive source floor, and
refinement convergence. The frozen signature audit decides the final question for bare data: finite causal
order, record measure, and deletion do not derive the labeled signature quartet. A marked quartet can pass only
as extra input. Therefore pure branch A fails under the current bare Physical-ICS assumptions. The enriched
object campaign then searches for the least ugly replacement and finds one serious candidate: a modular
causal-diamond record instrument, where record, source, causal, and antichain roles are conjugate derivatives
of one deletion relative-entropy/free-action germ. This is no longer a pure derivation from the bare data, but
it is not a four-label patch either. The Einstein order-shadow audit then fixes the ontology language: the
causal set is the order projection of the physical modular-diamond event, not the whole primitive. The
MCDI reference-state campaign then finds the next hard lock: the same click/order/deletion data admit different
full-rank reference states `sigma_x`, hence different modular source responses and different `beta`. A derived
KMS/diamond reference can close the finite target; a free reference, free temperature, maximum-entropy state, or
drifting reference fails. The intrinsic ICS reference-state campaign supplies the positive finite law:
`sigma_x = exp(-H_x/T_x)/Z_x`, uniquely, if the enriched ICS germ derives an oriented deletion/Dirichlet
Hamiltonian `H_x` and fixed diamond KMS temperature `T_x`. The H/T campaign then gives the finite intrinsic
law: `H_x` is cumulative oriented deletion-shell work and `T_x=|delta V_x|/delta S_screen,x`. External
Hamiltonians, zero work, wrong orientation, degenerate shell work, free work scale, free screen/volume
temperature, and refinement drift all fail. Thus the enriched branch-A route is now explicit at finite level:
MCDI plus intrinsic shell work and screen/volume normalization derive `sigma_x`, the modular source row, and
`beta` on the positive-margin region. The RN shell-work proof then removes the last placeholder: if the
enriched diamond has canonical causal-rank shells and a log Radon-Nikodym deletion action `A_k`, the work is
`w_k=A_{k+1}-A_k` and the action scale is fixed in logarithmic units; count entropy fixes the screen unit.
Order-only shells, external actions, ambiguous shell filtrations, nonmonotone action, free log units, free
entropy units, and drift all fail. The Modular Deletion Profile campaign compresses these conditions into one
finite invariant:
`M_x(k)=D(P_x|F_{x,k} || P_{\setminus x}|F_{x,k})`. Its relative-entropy chain rule derives the RN action,
positive shell work, and logarithmic scale. It also proves the refutation boundary: order-only ICS, singular
deletion, scalar total deletion entropy, non-isolated profile, free screen unit, and drifting profile do not
close branch A. The missing-assumption attack then proves the key negative result: the order/deletion shadow
does not determine `F_{x,k}`, `P_x`, or `P_{\setminus x}`. Same-order families with different retained laws,
deleted laws, or shell filtrations give different MDPs and different `beta`. The P/Q/F origin closure then
settles the repair attempt: `P_x` from bare order is falsified, `P_{\setminus x}` from deletion shadow is
falsified, and `F_{x,k}` is only partially derivable after a shell functor has been chosen; bare order does not
select the physical functor. The final consolidated theorem therefore renames the base: bare ICS is only a
locally finite order shadow, while Modular Physical ICS is a causal-diamond deletion germ with intrinsic MDP.
Bare branch A is refuted under the current assumptions. Branch A-enriched remains alive exactly as the Modular
Physical ICS / MDP theorem. If the retained/deleted laws, canonical shells, fixed count units, or isolated
profile scale are supplied externally, the construction is branch B. The honest ISP-base campaign then moves
one layer upstream and finds the only plausible branch-A revival target: a Cofinal Modular Record Process
(CMRP), a fixed covariant finite-record variational process whose stable deletion atoms generate Modular
Physical ICS and whose order projection is ICS. The fixed-action campaign then sharpens CMRP itself: the only
upstream passing action target is a coefficient-free KL/RN deletion record action plus count-normalized
screen/volume gravity response, spacelike additivity, and cofinal stability. Free kernels, free record weights,
free gravity weights, missing gravity, nonlocal action, non-isolated profile, and refinement drift all fail.
The sealed causal-diamond campaign then gives the Einstein-style invariant principle behind this target:
inside a closed diamond, external sector labels and slicings are not observables, and record/source/causal/screen
descriptions are one event only when their full deletion profiles agree on the intrinsic shell filtration. Same
order, same count, same total deletion entropy, preferred slicing, free screen units, non-isolation, and drift
all fail. This is not proved by current ISP; it is the exact deeper law that would have to replace ICS as the
base; Paper 3 is the dedicated ontology paper for that law. If the CMRP action or its gravity/scale
coefficients are free, the theory is branch B with a modular record kernel.**

---

## References / pointers

### Spatial-frame and flow-drift leg


External: Rideout-Wallden, *Spacelike distance from discrete causal order*,
CQG 26, 155013 (2009), arXiv:0810.1768; Major-Rideout-Surya, *Spatial
Hypersurfaces in Causal Set Cosmology*, gr-qc/0506133; Eichhorn-Mizera-Surya,
*Spectral dimension on spatial hypersurfaces in causal set quantum gravity*,
arXiv:1905.13498; Brightwell-Gregory on timelike distance; Belkin-Niyogi on
Laplacian eigenmaps; Hojman-Kuchar-Teitelboim on the hypersurface-deformation
algebra.

Internal: Paper 1 v6 §5.15-§5.20; `code/v6_p2_spatial_direction.py`;
`code/v6_p2b_local_frame.py`; `code/v6_p2c_flow_drift.py`;
`code/v6_p2d_curved_coefficient.py`; `code/v6_p2e_3d_tensor_coefficient.py`;
`code/v6_p2f_4d_tensor_coefficient.py`.

### Interacting covariance and memory leg


External (web-verified): Barandes, *The Stochastic-Quantum Correspondence*, arXiv:2302.10778 (2023);
*Quantum Systems as Indivisible Stochastic Processes*, arXiv:2507.21192 (2025). Tumulka, *A relativistic
version of the GRW model*, quant-ph/0406094 (2006); *A Relativistic GRW Flash Process With Interaction*,
arXiv:2002.00482 (2020). Bedingham, *Relativistic State Reduction Dynamics*, arXiv:1003.2774, Found. Phys. 41
(2011) 686. Pearle, relativistic CSL (energy-production problem). Adler & Bassi, *Collapse models with
non-white noises*, arXiv:0708.3624 (2007). *Towards relativistic generalization of collapse models*,
arXiv:2507.06954 (2025); *Relativistic Collapse Model with Quantised Time Variables*, arXiv:2506.07959 (2025);
*Relativistic … non-Hermitian colored noise*, arXiv:2501.07050 (2025). *Relativistic Covariance and Nonlinear
Quantum Mechanics: Tomonaga–Schwinger Analysis*, arXiv:2511.15935 (2025), + comment arXiv:2602.06845 (2026).
Brunetti-Fredenhagen-Verch, *The generally covariant locality principle*, arXiv:math-ph/0112041; Sanders,
*The locally covariant Dirac field*, arXiv:0911.1304; Bruinsma-Fewster-Schenkel, *Relative Cauchy evolution for
linear homotopy AQFTs*, arXiv:2108.10592.
Jacobson, *Entanglement Equilibrium and the Einstein Equation*, arXiv:1505.04753. Jacobson-Visser,
*Gravitational Thermodynamics of Causal Diamonds in (A)dS*, arXiv:1812.01596. Casini-Huerta-Myers,
*Towards a derivation of holographic entanglement entropy*, arXiv:1102.0440. Bousso-Fisher-Koeller-
Leichenauer-Wall, *Proof of the Quantum Null Energy Condition*, arXiv:1509.02542. Koeller-Leichenauer-
Levine-Shahbazi Moghaddam, *Local Modular Hamiltonians from the Quantum Null Energy Condition*,
arXiv:1702.00412. Bousso-Casini-Fisher-Maldacena, *Entropy on a null surface for interacting quantum field
theories and the Bousso bound*, arXiv:1406.4545. Holroyd-Soo, *Insertion and Deletion Tolerance of Point
Processes*, arXiv:1007.3538. Georgii-Yoo, *Conditional Intensity and Gibbsianness of Determinantal Point
Processes*, arXiv:math/0401402. Cronie, *New density/likelihood representations for Gibbs models based on
generating functionals of point processes*, arXiv:2406.07075.
Bombelli, Henson & Sorkin, *Discreteness without symmetry breaking: a theorem*, gr-qc/0605006, MPLA 24 (2009)
2579.

Internal: paper 1 v6 §4B (substrate Poisson condition), §5.7 (Unruh–DeWitt interacting rate), §6/§10 (the
single-object reduction; `code/v6_10_indivisibility_covariance.py`, `code/v6_10b_covariant_correlation.py`);
`code/v6_p2_covariance_feasibility.py`, `code/v6_p2_covariance_feasibility_4d.py` (the §3 probe in 1+1 and 3+1:
first-order covariance gated by the localization measure); `code/v6_p2_porting_quartic_memory.py` (the §4
porting check: the quartic-damped template `e^{−q⁴/β⁴}` passes the two-sided tail test, while the
Gaussian-in-`s²` does not); `code/v6_p2g_ascale_receipts.py` (the §5.5 finite A-Scale receipt execution:
coherent finite receipts pass, but the threshold and memory width remain visible inputs);
`code/v6_p2h_srecord_candidates.py` (the §5.7 `S_R` candidate attack: three plausible stability scores detect
records, but none fixes the threshold or memory width); `code/v6_p2i_ascale_selectors.py` (the §5.9
post-no-go selector scan: gravity matching, vacuum/detector survival, criticality, minimal disturbance, TS
fixed point, and information-unit selectors tested one by one); `code/v6_p2j_lr_decisive_tests.py` (the §5.11
response-Gram and one-event singular-value decisive finite tests); `code/v6_p2k_one_event_response.py` (the
§5.23 focused cofinal one-event deletion-response audit); `code/v6_p2l_oer_actual_event_investigation.py`
(the §5.24 strict-symmetric versus generalized OER investigation);
`code/v6_p2m_generalized_oer_bounds.py` (the §5.25 generalized OER bounds and same-support
source-amplitude obstruction); `code/v6_p2n_full_law_p_source_audit.py` (the §5.26 full-law
`p_source`/`d_source` audit); `code/v6_p2o_role_completeness_decision.py` (the §5.27 reduced-law
negative theorem and full-law positive theorem decision); `code/v6_p2p_full_role_generator_audit.py`
(the §5.28 one-generator source-row audit); `code/v6_p2q_full_generator_theorem.py` (the §5.29
full-Gram theorem audit); `code/v6_p2r_full_role_gram_derivation.py` (the §5.30 canonical-role
derivation gate and no-source no-go); `code/v6_p2s_local_operator_origin.py` (the §5.31 local-operator
origin gate); `code/v6_p2t_microcausal_ts_gate.py` (the §5.32 microcausal TS gate);
`code/v6_p2u_nonlinear_frechet_gate.py` (the §5.33 nonlinear Fréchet gate);
`code/v6_p2v_branch_a_closure_ledger.py` (the §5.34 final finite closure ledger);
`code/v6_p2w_physical_receipt_closure.py` (the §5.35 same-beta physical receipt closure gate);
`code/v6_p2x_operator_construction_exhaustion.py` (the §5.36 construction-class exhaustion and
fixed-background no-go); `code/v6_p2y_invariant_law_guess_search.py` (the §5.37 invariant deletion-action
guess search); `code/v6_p2z_ida_physical_ics_proof_program.py` (the §5.38 seven-step IDA-germ
proof/falsification program); `code/v6_p2aa_ida_germ_uniqueness_attack.py` (the §5.39 full IDA-germ
nonuniqueness attack); `code/v6_p2ab_canonical_ida_germ_lock.py` (the §5.40 canonical IDA-germ sector-lock
target); `code/v6_p2ac_role_sector_origin_attack.py` (the §5.41 intrinsic role-sector operator origin attack);
`code/v6_p2ad_intrinsic_lx_dirichlet_derivation.py` (the §5.42 intrinsic Dirichlet construction
`L_x=G_x^{-1}Q_x`); `code/v6_p2ae_lx_eigenlabel_derivation.py` (the §5.43 eigenlabel/signature derivation);
`code/v6_p2af_signature_origin_audit.py` (the §5.44 signature-origin audit);
`code/v6_p2ag_frozen_signature_theorem_audit.py` (the §5.45 frozen-signature counterexample/no-go);
`code/v6_p2ah_enriched_physical_object_campaign.py` (the §5.46 enriched-object campaign and modular
diamond record instrument target); `code/v6_p2ai_einstein_order_shadow_audit.py` (the §5.47 causal-set
order-shadow audit); `code/v6_p2aj_mcdi_reference_state_campaign.py` (the §5.48 MCDI reference-state
counterexample and derived-KMS target); `code/v6_p2ak_ics_reference_state_law.py` (the §5.49 intrinsic
Dirichlet-KMS reference-state law); `code/v6_p2al_ics_ht_law_campaign.py` (the §5.50 intrinsic
shell-work/temperature law); `code/v6_p2am_ics_shell_work_proof_campaign.py` (the §5.51 RN shell-work proof
campaign); `code/v6_p2an_modular_deletion_profile_campaign.py` (the §5.52 Modular Deletion Profile theorem
and refutation boundary); `code/v6_p2ao_mdp_missing_assumption_attack.py` (the §5.53 attack on whether bare
order/deletion derives the MDP prerequisites); `code/v6_p2ap_pqf_origin_closure_campaign.py` (the §5.55
origin closure for `P_x`, `P_{\setminus x}`, and `F_{x,k}`);
`code/v6_p2aq_honest_isp_base_campaign.py` (the §5.56 search for an upstream ISP base and CMRP theorem target);
`code/v6_p2ar_cmrp_action_derivation_campaign.py` (the §5.57 fixed CMRP action derivation/refutation audit);
`code/v6_p2as_sealed_diamond_invariant_campaign.py` (the §5.58 sealed causal-diamond deletion invariant audit);
Paper 3 v6, `relativistic-isp-v6-paper3-modular-record-diamonds.md`, and
`code/v6_p3a_cmrp_ontology_closure.py`, `code/v6_p3b_cmrp_axiom_independence.py`,
`code/v6_p3c_cmrp_observable_derivation.py`, `code/v6_p3d_feynman_record_channel.py`,
`code/v6_p3e_mdp_completeness_attack.py`, `code/v6_p3f_germ_origin_uniqueness_audit.py`,
`code/v6_p3g_canonical_germ_generation.py`, `code/v6_p3h_germ_origin_decision.py`,
`code/v6_p3i_isp_do_delete_no_go.py`, `code/v6_p3j_isp_do_delete_derivation_audit.py`,
`code/v6_p3k_do_delete_decision.py`, `code/v6_p3l_einstein_reality_campaign.py`,
`code/v6_p3m_self_deleting_completeness_campaign.py`, `code/v6_p3n_nx_origin_campaign.py`,
`code/v6_p3o_intrinsic_collar_separator_theorem.py`, `code/v6_p3p_tx_origin_campaign.py`,
`code/v6_p3q_eventless_defect_campaign.py`, `code/v6_p3r_intrinsic_rx_units_resolution.py`,
`code/v6_p3s_imfd_genericity_campaign.py`, `code/v6_p3t_fixed_cmrp_imfd_dynamics.py`,
`code/v6_p3u_spectrum_flow_origin_campaign.py`, `code/v6_p3v_k0_origin_campaign.py`,
`code/v6_p3w_sealed_work_profile_campaign.py`, `code/v6_p3x_feynman_wx_receipts.py`,
`code/v6_p3y_full_branch_a_target_campaign.py`, `code/v6_p3z_underlying_change_law_campaign.py`,
`code/v6_p3aa_current_rho_origin_campaign.py`, `code/v6_p3ab_q_origin_einstein_campaign.py`,
`code/v6_p3ac_screen_bridge_theorem_campaign.py`,
`code/v6_p3ad_minimal_complete_screen_campaign.py`,
`code/v6_p3ae_record_completeness_closure_campaign.py`,
`code/v6_p3af_no_silent_seam_origin_campaign.py`,
`code/v6_p3ag_rn_action_conservation_campaign.py`,
`code/v6_p3ah_canonical_reference_campaign.py`,
`code/v6_p3ai_count_functor_origin_campaign.py`,
`code/v6_p3aj_leibniz_record_functor_campaign.py`,
`code/v6_p3ak_record_field_equation_campaign.py`,
`code/v6_p3al_field_equation_candidate_campaign.py`,
`code/v6_p3am_stronger_rigidity_campaign.py`,
`code/v6_p3an_whole_diamond_action_campaign.py`,
`code/v6_p3ao_action_selection_invariant_campaign.py`,
`code/v6_p3ap_relational_field_equation_campaign.py`,
`code/v6_p3aq_field_equation_origin_closure.py`,
`code/v6_p3ar_score_geometry_campaign.py`,
`code/v6_p3as_conditional_score_origin.py`,
`code/v6_p3at_pc_origin_campaign.py`,
`code/v6_p3au_pd_principle_campaign.py`,
`code/v6_p3av_process_law_boundary_campaign.py`,
`code/v6_p3aw_pd_contradiction_campaign.py`,
`code/v6_p3ax_unique_process_law_no_go.py`
(the dedicated CMRP ontology, Feynman-route, sealed-germ origin, do-delete, and
Einstein-real-enough/completeness, `N_x(B_x)` origin, collar-separator,
`T_x` origin, eventless-defect, intrinsic `R_x`/RN-unit, IMFD genericity,
fixed spectrum-flow dynamics/origin, `K0` scalar no-go, sealed KL work-profile
theorem, finite Feynman `W_x` receipt campaign, and full branch-A target
audit/Dirac-Hessian falsifier, underlying possible-change-law/current-cocycle campaign,
`C/rho` origin/refinement-functor campaign, and Einsteinian `Q`/two-screen
record-bridge origin campaign, and intrinsic screen-bridge/RN-sufficiency
composition campaign, minimal complete RN screen-closure campaign, and
record-completeness/no-silent-seam closure campaign, and no-silent-seam
origin/action-conservation campaign, and RN action conservation/log-uniqueness
campaign, canonical compositional-reference/count-functor campaign, and sealed
finite record-algebra functor origin campaign, and sealed Leibniz
record-functor necessity campaign, and sealed record field-equation/dynamics
campaign, candidate field-equation invariance campaign, and stronger
record-field rigidity campaign, and non-Markovian whole-diamond action
unification campaign, invariant whole-action selection/no-go campaign, and
relational record field-equation/Hodge-Poisson campaign, and origin-closure
no-go for `L_D`, `rho_D`, and exactness, and intrinsic score-geometry /
conditional score-space origin campaign, `P_D`/`C_D` origin campaign, and
invariant `P_D` principle/process-law boundary campaign, and `P_D`
contradiction/complete-record-identity campaign, and unique nontrivial
process-law no-go);
§5.10-§5.11 of this paper (the C1-C6
combined-selector criterion and the LR1-LR7 likelihood-ratio event-law theorem target). On covariant
localization: Newton–Wigner (1949); Hegerfeldt's theorem (no sharp covariant localization).
