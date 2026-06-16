# Paper 1 (v6) — Indivisible Causal-Set Gravity: discharging the hypersurface-deformation residue on the division-event network

Preprint, not peer reviewed, version 2026-06-08.

**Author:** Felix Robles Elvira
**Status:** Program + feasibility probe (markdown draft). This is **not** a derivation of general
relativity and **not** a solution of the relativistic-QFT reconstruction problem. It proposes one
specific extension of the indivisible-stochastic-processes (ISP) program aimed at the single obstruction
that v4/v5 localized, argues why it could keep ISP's quantum reconstruction intact while reaching
gravity, runs a quick numerical feasibility probe of the geometry side, and states the one decisive open
calculation and the criteria that would kill it. Claims are tagged **[EST]** (established external
result), **[ARG]** (argued here), **[PROBE]** (numerically checked here, small-scale), **[OPEN]**.

Builds directly on: the **hypersurface-deformation obstruction** map (`publishable/paper2-…`), the
**unimodular / non-conserved-matter** sourcing result (`publishable/paper4-…`), and the **magic ≠
indivisibility** numerical finding (`code/magic_vs_indivisibility.py`).

---

## 0. The proposal, in one page

ISP reformulates quantum mechanics as an **indivisible** (non-Markovian) stochastic process over a
definite configuration space: the transition law does not factorize through intermediate times,

```math
\Gamma(t_2,t_0)\;\neq\;\Gamma(t_2,t_1)\,\Gamma(t_1,t_0),
```

except at isolated **division events**, where the process momentarily factorizes (Chapman–Kolmogorov
holds) — the loci of effective measurement and **record formation**. Non-relativistic QM is reconstructed
exactly; the relativistic interacting case and gravity are open.

> **The v6 idea.** Do **not** try to build spacetime geometry from the *continuous* beable history — that
> is where the obstruction lives (it is frame-dependent and has no trans-foliation joint distribution) and
> where one would need a quantum resource ISP lacks. Build it from the **division events** instead. A
> record is a *frame-independent physical fact*, and the causal order among records is Lorentz-invariant.
> Promote the **division-event causal network to the fundamental geometric substrate** (a *causal set*):
> its order fixes the light-cone/conformal structure and its counting fixes the volume ("order + number =
> geometry"). Represent the hypersurface-deformation (Dirac–Schwinger) algebra on *foliation-invariant
> antichains* of this network; the spacetime **dynamics is then forced to general relativity** — either by
> the Hojman–Kuchař–Teitelboim uniqueness theorem (the algebra's unique realization is GR), or
> equivalently by Jacobson's thermodynamic derivation with record-counting supplying the horizon entropy.
> ISP's distinctive contribution is that it **derives the sprinkling law** that causal-set theory must
> otherwise postulate.

**v6/Paper 2 terminology update.** The phrase "division-event causal
network" should not be read as a bare causal set carrying the whole physical
law. Paper 2's branch-A audit refutes that thinner reading: finite causal
order plus deletion shadow does not determine the retained/deleted local
record laws, the canonical shell filtration, the modular source response, or
the memory scale. The intended primitive is therefore richer:

```text
Modular Physical ICS =
physical causal-diamond deletion germ whose order projection is a causal set.
```

The causal set remains the geometric order/volume shadow. The physical event
is the local modular record-diamond fact whose deletion changes record,
source, causal-collar, and antichain/screen readouts together.

Paper 2's final upstream repair goes one step further. If branch A is to be
revived, the base is not even Modular Physical ICS as a primitive. The base
would have to be a **Cofinal Modular Record Process**: a covariant finite
record process with a fixed modular record-gravity action whose stable
deletion atoms generate Modular Physical ICS, and whose order projection is
the causal set. In that reading:

```text
Cofinal Modular Record Process
-> Modular Physical ICS event germs
-> causal-set order shadow
-> geometry / antichain dynamics.
```

If the modular record-gravity action or its coefficients are supplied rather
than derived, this is the honest branch-B route.

Paper 2's fixed-action audit narrows this further. The only surviving
branch-A-enriched action target is a coefficient-free KL/RN deletion record
action plus count-normalized screen/volume gravity response, spacelike
additivity, and cofinal stability. Free record weights, gravity weights,
kernel widths, temperature units, or screen count units all return the theory
to branch B.

The conceptual test is the sealed causal-diamond deletion experiment: inside a
closed diamond, record, source, causal, and screen descriptions are the same
physical event only if deleting the event gives the same intrinsic modular
profile in all four readouts. Causal order alone is only the geometric shadow
of that stronger invariant. Paper 3 develops this as the CMRP / modular
record-diamond ontology and then sharpens it: the full sealed deletion germ is
the local physical object; its scalar MDP is the modular action/readout.

This routes gravity through **consistency and thermodynamics**, not through a quantum resource — which is
exactly what the magic result (§1.3) says is required.

---

## 1. The diagnosis we are building on

### 1.1 Everything reduces to one residue [EST, from v-paper2]
The hypersurface-deformation obstruction map showed that reconstructing interacting QFT *and*
reconstructing effective-GR kinematics both reduce to the **same** problem: a *foliation-independent
representation of the Dirac–Schwinger (hypersurface-deformation) algebra on a frame-dependent, indivisible
substrate*. The field-theory "killers" — energy non-conservation, **Wigner negativity**, Haag's theorem,
Tomonaga–Schwinger integrability — are each clearable, leaving a single covariance residue.
**Indivisibility is the one ISP-specific lever** distinguishing this residue from the obstruction that
blocks covariant Bohmian field theory. The geometry branch carries two extra items: the **Einstein
coupling** (dynamics, not kinematics) and a methodological circularity.

### 1.2 HKT collapses the two geometry items into the one residue [EST]
The two extra items are not independent of the residue:

> **Hojman–Kuchař–Teitelboim (1976).** Under natural assumptions (the canonical variables are a spatial
> metric and its conjugate momentum; ultralocality), the hypersurface-deformation algebra has an
> *essentially unique* realization, and it **is** general relativity.

So *if* the Dirac–Schwinger algebra can be represented on the substrate (the residue), HKT delivers the
Einstein coupling automatically. **GR-from-RISP reduces to the single residue.** That is the target.

### 1.3 The magic result fixes the *kind* of solution allowed [PROBE, code/magic_vs_indivisibility.py]
We tested whether ISP's headline resource (indivisibility) is the "gravity" resource of the
holographic "magic gives gravity" picture. It is **not**: Barandes' computational-basis indivisibility is
large even for zero-magic Clifford dynamics (`H·H`: indiv = 2.0, magic = 0; correlation over 600 random
circuits = +0.08), while magic = Wigner negativity lives in the phase-space representation where Clifford
acts by positive permutations. **Conclusion:** indivisibility is the *coarse / geometry* resource, not the
*magic / dynamical* one. Therefore an emergence route for gravity in ISP cannot run through a quantum
resource; it must run through **consistency (HKT) or thermodynamics (Jacobson)** — routes on which the
magic obstruction does not bite. v6 is built to be exactly such a route.

---

## 2. The mechanism: records are the foliation-invariants

**The obstruction is a property of the continuous layer.** Indivisibility *is* the statement that the
continuous beable history has no consistent joint distribution across foliations. Trying to lay a metric on
that history inherits the obstruction.

**The division-event layer evades it.** Two facts:
1. A division event (a record) is an **objective, frame-independent** occurrence — all foliations agree a
   record formed, even when they disagree about the configuration between records.
2. The **causal order** among division events is **Lorentz-invariant**: timelike order is frame-independent,
   spacelike pairs are unordered (which a causal set permits).

So the division events form a **causal set** `(C, \prec)` — the natural foliation-invariant object — on
which the geometry can be reconstructed:

- **Kinematics — "order + number = geometry" [EST, Sorkin].** The causal order `\prec` recovers the
  conformal (light-cone) structure; the event count recovers the volume; together they fix the metric up to
  the discreteness scale. (Probed in §4.)
- **Covariance residue — represent Dirac–Schwinger on antichains [ARG].** A spatial slice is a maximal
  *antichain* (a maximal set of mutually unrelated events) — a foliation-invariant combinatorial object.
  Deformations of antichains are the discrete analogue of hypersurface deformations. The proposal is to
  represent the Dirac–Schwinger algebra on antichain deformations, where the trans-foliation joint-history
  obstruction is *absent by construction* (one never invokes the forbidden continuous joint).
- **Dynamics — forced to GR [EST templates]:**
  - *HKT route:* if the antichain-deformation algebra reproduces Dirac–Schwinger, GR is its unique
    realization.
  - *Jacobson route (1995):* division-event **counting** across a local causal horizon supplies the entropy,
    the record energy-flux supplies the heat, and `\delta Q = T\,\delta S` yields Einstein's equations. The
    holographic (area-law) input lives precisely in "how many records a horizon can carry."

**Why this is ISP's to claim, not borrowed causal sets.** Causal-set theory must *postulate* its sprinkling
(random Poisson) and struggles to supply dynamics. **ISP derives the division-event statistics from the
indivisible process** — it provides the missing dynamical law. This is the operational use of the
"indivisibility lever" that v-paper2 identified as the one ISP-specific angle.

---

## 3. Feasibility I — does v6 keep ISP's reconstruction of (relativistic, interacting) QM?

**Non-relativistic QM: untouched [ARG].** The modification is **purely additive**. It reinterprets an object
ISP *already has* (division events) as the geometric substrate; it does **not** alter the inter-event
stochastic dynamics from which the Hilbert space, unitary group, and Born rule are reconstructed. Between
records, nothing changes. So the established non-relativistic reconstruction is preserved verbatim.

**Relativistic interacting QFT (the §10 / v-paper2 residue): plausibly *eased*, not worsened [ARG].** This is
the key synergy. v-paper2 proved the QFT branch and the geometry branch reduce to the *same* covariance
residue. v6 attacks that residue at the **discrete** level: it demands foliation-invariance only of the
*record network and its causal order*, not of the continuous field history. That is a strictly weaker and
more structured demand — discrete causal order is manifestly Lorentz-invariant, whereas a continuous
trans-foliation joint history is exactly what indivisibility forbids. So the same move that supplies the
gravity substrate is a candidate discharge of the QFT covariance residue. v6 does **not** solve §10, but it
does not trade it away either, and it gives a concrete new handle on it.

**Wigner negativity stays clear [ARG, consistent with v-paper2 + §1.3].** v-paper2 already listed Wigner
negativity as clearable, and §1.3 shows magic/negativity is a *separate* resource from indivisibility. v6 is
consistent with both: the **matter sector remains a positive indivisible process** (Barandes, no negative
probabilities), and the **geometry sector is built from record order and counting** (combinatorics), which
needs no negativity. The two resources are kept in their own sectors.

**Verdict I:** v6 is conservative on the quantum side (✅ non-relativistic reconstruction intact) and is, if
anything, **favorable** to the open relativistic reconstruction (🟡 it attacks the common residue at the
discrete level).

---

## 4. Feasibility II — does v6 reach GR/gravity? (numerical probe)

Probe code: `code/v6_causal_set_feasibility.py`. It tests the geometry-side claims; it does **not** test
whether ISP's *actual* division events sprinkle correctly (that is the open calculation, §5).

**(A) "order + number = geometry" works [PROBE].** Poisson-sprinkling flat Minkowski causal diamonds and
recovering the dimension from the causal order alone (Myrheim–Meyer):

| true `d` | ordering fraction | recovered `d` |
|---|---|---|
| 2 | 0.4945 (theory 0.5000) | **2.01** |
| 3 | 0.2381 (theory 0.2286) | **2.95** |
| 4 | 0.0966 (theory 0.1000) | **4.04** |

The causal order of the events alone encodes the spacetime dimension/geometry. The "records → metric" step
is geometrically sound. ✅

**(B) The single make-or-break Lorentz condition [PROBE].** A regular lattice has preferred directions
(a preferred frame → breaks Lorentz); a Poisson sprinkling is isotropic in every frame
(Bombelli–Henson–Sorkin). 4-fold anisotropy of nearest-neighbour links, rest frame and after a boost
`β=0.6`:

| substrate | anisotropy (rest) | anisotropy (boosted) | verdict |
|---|---|---|---|
| regular lattice | 1.000 | 1.000 | **preferred frame — breaks Lorentz** |
| Poisson sprinkle | 0.003 | 0.005 | **isotropic — Lorentz-OK** |

So the substrate is Lorentz-invariant **iff the division events Poisson-sprinkle.** This isolates the
*entire* feasibility of the geometry side into one checkable condition on ISP's division-event statistics.
🔶

**(B′) The kill-test, made operational [PROBE].** "Poisson-sprinkle" is not directly checkable on a uniform
intensity — a *uniform-rate* flash process is *already* Lorentz-invariant (Lebesgue measure is boost-invariant),
so a crude marginal test would wrongly pass naive GRW. The genuine Bombelli–Henson–Sorkin criterion is whether
a **preferred frame can be reconstructed** from the events. Code: `code/v6_4b_division_event_lorentz_kill.py`.
A frame-reconstruction estimator scans trial boosts `β` and measures the frame-dependence of the `t'`-marginal
(Fano factor of time-slab counts); the discriminant is the *`β`-dependence* (signal `S` = peak − baseline
Fano, mean over 10 realizations) — flat = no preferred frame, a peak at some `β` = that frame is preferred:

| candidate division-event process | signal `S` | recovered frame | verdict |
|---|---|---|---|
| Poisson per 4-volume | 0.21 (null) | — (flat) | **PASS — no preferred frame** |
| synchronized shells (a global clock) | 76.9 | `β=0` (rest) | **KILL — preferred frame** |
| regular-clocked (lattice in time) | 79.2 | `β=0` (rest) | **KILL — preferred frame** |

And along an *accelerated* worldline, between two **fixed** spacetime events, only a **per-proper-time
(scalar) rate** gives a frame-invariant division-event count (`12.00` in rest *and* boosted frames); a
per-coordinate-time rate is frame-dependent (`14.1 → 16.3`). So the §4B condition is now operational, and it
is *the same* as the rate-leg condition (§5.7–5.8): **the division events survive iff they are
Poisson-per-proper-4-volume = the scalar rate.** The naive global-time ISP default (synchronized/clocked) is
*killed*; whether the full *interacting* reconstruction delivers the scalar rate is the one shared open
residue (§10). This **unifies the two feasibility legs into a single criterion.** 🔶

**Dynamics [EST templates, not computed].** Given a Lorentz-invariant causal set, the dynamics route is
HKT (unique realization = GR) or Jacobson (`\delta Q=T\delta S`); the causal-set d'Alembertian
(Benincasa–Dowker 2010) gives the Einstein–Hilbert action in the continuum. The deep input — entropy ∝
horizon area — is *assumed*, as it is in every thermodynamic-gravity derivation; v6 does not derive it.

**Verdict II:** the geometry substrate is internally consistent (✅ encodes geometry) and Lorentz-compatible
**conditionally** (🔶 iff Poisson sprinkling); the dynamics has rigorous external templates but rests on an
unproven holographic input. §5 sharpens the conditional into a precise, tested criterion — and **(B′) shows
that criterion is identical to the rate-leg's scalar-rate condition**, so both feasibility legs collapse to a
single open residue (the scalar division rate, §10).

---

## 5. The decisive test: is the division-rate a Lorentz scalar? [PROBE + ARG]

Probe code: `code/v6_division_event_lorentz_test.py`.

### 5.1 Which division events? The dense record/"flash" events
The causal-set substrate needs a **dense** set of events, which means the **record/localization events of
open or interacting dynamics** — the ISP analogue of GRW **"flashes"** — not the sparse, deterministic
division *times* of a *closed* system (a free closed field forms no records, hence no flashes). This ties
the substrate to two existing structures: the **flash ontology** (Bell; GRW) — collapse/record events *are*
a spacetime point process — and your **paper 4 / Tilloy–Diósi**, where the *localized* (recorded) mass
density already **sources** gravity. v6 promotes "flashes *source* the metric" to "flashes *build* it."

### 5.1a Physical division events are source-record clicks [ARG]
Paper 2 sharpens this point into the ACV criterion. The v6 event used for
gravity is not a bare causal-set atom with optional labels. It is a local
source-record click: one finite occurrence whose record, source, causal-collar,
and antichain-crossing roles are all directly measurable facts of the same
local event.

The minimal physical event therefore carries four finite sufficient
statistics:

```text
record formation;
localized stress/source response;
causal collar incidence;
antichain or slice crossing.
```

The ACV bridge in Paper 2 proves the following conditional statement. If the
direct self-sensitivity of these four roles dominates cross-role leakage, and
if refinement only changes the local vertex by a summable Schur-complement
drift, then the role-floor needed by branch A follows. If a candidate event is
only a causal atom, a slice marker, a source-free record, or a redundant label,
then the ACV test fails and v6 has not derived the required event floor.

This is the ontology-level clarification. v6 should not claim that every
causal-set point is automatically a physical division event. It should claim
that the causal set is built from those division events that pass the
source-record click test. Paper 2 turns this into a finite collar audit:
compute the role response matrix of the actual event law, bound leakage, and
check that Schur refinement drift is smaller than the direct response margin.
It also proves the no-go: bare causal-set data alone cannot force this audit,
because the same order, count, scalar rate, and refinement map can carry
different role-response laws. The gravity substrate therefore needs physical
ICS events, not untyped causal-set atoms. Paper 2 sharpens the constructive
route to a modular causal-diamond record instrument. The causal-set atom is
then the **order-shadow** of the physical event, not the whole primitive. The
physical deletion atom is a local diamond record germ whose same deletion
changes:

```text
record-instrument evidence;
modular/stress source response;
interval-volume/order count;
screen/antichain entropy count.
```

Thus the slogan "events build the causal set" should be read as:

```text
physical modular record-diamond events build the causal set through their
order projection.
```

Equivalently, the branch-A-enriched base is **Modular Physical ICS**, not
bare ICS. A bare ICS atom is only the order shadow. A physical atom is a
causal-diamond deletion germ with a finite retained/deleted record law and a
Modular Deletion Profile:

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

If that profile is intrinsic, canonical, finite, isolated, fixed-unit, and
refinement-stable, Paper 2 gives the enriched branch-A route. If the profile
or its units are added after choosing the causal-set point, the construction
is branch B.

The deeper branch-A target is therefore not:

```text
ICS -> event law.
```

It is:

```text
cofinal modular record dynamics -> event law -> ICS order shadow.
```

If the modular/source and screen responses are merely labeled after the
causal-set point is chosen, the construction is branch B rather than a pure
branch-A derivation.

### 5.2 The reduction (the real content)
A record point process is Lorentz-invariant **iff its intensity is a Lorentz-scalar measure** — a rate per
invariant proper-time / 4-volume — **not** a rate "per slice" (per coordinate time in a preferred frame).
Non-relativistic ISP defines division events as special **times in a frame** — a *per-slice* notion. So the
naive relativistic lift is frame-dependent; the covariant fix is a **scalar** rate. The vague "do the events
Poisson-sprinkle?" thus becomes the sharp, checkable question: **is the division rate a Lorentz scalar?**

### 5.3 The computation
The one frame-invariant diagnostic is **flashes per unit proper time** of a worldline. For a worldline at
`v=0.5` in frame `S`, boosted to `S'` (`β=0.6`, so `v'=−0.143`), generating flashes by each rule and
comparing the rate generated in `S` against the rate generated natively in `S'`:

| rule | flashes / proper-time in `S` | in `S'` | frame ratio | verdict |
|---|---|---|---|---|
| **scalar** (proper-time) | 0.9975 | 0.9975 | **1.000** | Lorentz-invariant ✓ |
| **per-slice** (coord-time) | 1.154 (`=λγ_v`) | 1.012 (`=λγ_{v'}`) | **1.14** | frame-dependent ✗ |

The scalar rate yields **one physical flash set in all frames**; the per-slice rate (ISP's default) yields
**different sets in different frames** — a preferred frame, breaking Lorentz invariance. And since the scalar
rule is exactly **Poisson-in-4-volume**, the §4A dimension recovery (`d=2→2.01, 3→2.95, 4→4.04`) applies
directly: **scalar-rate division events are a valid Lorentz-invariant geometry.**

### 5.4 Criterion, existence, and the located open step
- **Criterion (sharp):** the relativistic-ISP construction must produce a division rate that is a **Lorentz
  scalar** (per proper 4-volume). This is the entire feasibility of the geometry side, reduced to one
  property.
- **Existence (free case) [EST]:** Tumulka's relativistic GRW (rGRWf, 2006) constructs precisely such a
  **Lorentz-invariant flash process for free systems** — so the substrate provably *exists*, not merely in
  principle.
- **Open step [OPEN]:** the **interacting** derivation of the scalar rate from the indivisible process. This
  is the *same residue* as the §10 / v-paper2 QFT-covariance problem, and the same place interacting rGRW is
  open. **v6's gravity hinge and ISP's QFT hinge are literally the same open problem** — which is encouraging
  bookkeeping: one breakthrough discharges both.

### 5.5 Consistency cross-check with paper 4
The flash rate that *sources* gravity in paper 4 (Tilloy–Diósi) and the rate v6 needs to be a *scalar* are
the **same object**. So internal consistency of the corpus already *requires* that rate to be a Lorentz
scalar — §5's criterion is simultaneously a consistency condition on paper 4's relativistic completion.

### 5.6 Kill-test
If the interacting (§10) division rate comes out **per-slice** (frame-dependent), v6 is dead — and so is a
Lorentz-invariant flash ontology for ISP generally. The test is decisive and binary.

### 5.7 Layer 3 — an *interacting* toy: the record rate is a Lorentz scalar (Unruh–DeWitt) [PROBE]
Probe code: `code/v6_layer3_unruh_detector.py`. The minimal interacting relativistic system in which records
actually form is an **Unruh–DeWitt detector**: a two-level *record register* linearly coupled to a free
scalar field along a worldline; a detector click **is** a committed record (a division event). Its flash
rate is the response function — defined **per unit proper time** and built entirely from the worldline-
pulled-back field correlator — so "is the rate a scalar?" is directly computable:

| check | result |
|---|---|
| detector invariant (proper acceleration `a`) | boost-invariant: `1.0000` (rest) = `1.0000` (boosted); inertial = `0` |
| pulled-back two-point function | **stationary & thermal**: `Δt²−Δx² = (4/a²)sinh²(aΔτ/2)` to `10⁻¹¹` |
| KMS periodicity `W(Δτ−i2π/a)=W(Δτ)` | holds to `10⁻¹⁶` → **thermal at the Unruh temperature `T=a/2π`** |
| inertial detector, vacuum | no spontaneous flashes (`F(ω>0)=0`), in every frame |

So for a concrete *interacting* relativistic system the record rate **is a Lorentz scalar** — a
per-proper-time rate depending only on Lorentz invariants (the proper acceleration `a`, the field state),
with the covariant Unruh/KMS structure. This **extends the scalar-rate property from the free case (rGRW,
§5.4) to an interacting detector.** The *only* way to force a per-slice (frame-dependent) rate is a
**non-covariant coupling** (a preferred-frame environment / GRW absolute-time collapse, giving `λγ` per
proper time) — a modeling choice, not a necessity; the covariant coupling is the natural one and carries no
obstruction.

**Bonus — the two legs of v6 meet in one quantity.** The flash rate's Unruh temperature `T=a/2π` is *exactly*
the temperature in Jacobson's `δQ=T δS` derivation of Einstein's equations (§2). So the same object that
satisfies v6's **kinematic** criterion (a scalar record rate) also supplies the **dynamical** route's key
input. The record rate and the gravitational dynamics are not two hopes but one structure.

**Still open [OPEN].** This is linear coupling to a *free* field. §5.8 removes the "free" caveat.

### 5.8 Does the scalar rate survive *self-interactions*? Yes — by covariance, not freeness [PROBE + ARG]
Probe code: `code/v6_task1_interacting_robustness.py`. The detector rate is linear in the field's Wightman
function, and the **Källén–Lehmann** representation writes *any* interacting two-point function as a
**positive** superposition of free ones, `W_int = ∫dμ² ρ(μ²) W_free(·;μ²)`, `ρ≥0`. Each term depends on the
points only through the invariant interval, which on the accelerated worldline is `Z(Δτ)=(4/a²)sinh²(aΔτ/2)`.
Two theory-independent facts, checked numerically:

| check | result |
|---|---|
| **engine:** `Z(Δτ)` periodic in imaginary proper time, period `2π/a` | to `10⁻¹⁴` → *any* covariant `W=W(Z)` is KMS at `T=a/2π` |
| **interactions:** Källén–Lehmann (pole + continuum, `ρ≥0`) | stationary (origin spread `=0` → scalar rate) **and** KMS to `10⁻¹⁴` → thermal at the *same* `T` |
| **what breaks it:** a non-covariant (preferred-frame) coupling | non-stationary (spread `1.25` vs `0`) → not a per-proper-time scalar |

**Result:** the scalar *and* thermal record rate **survives arbitrary self-interactions**, because both
properties follow from Lorentz *covariance* (Källén–Lehmann) plus the worldline geometry — not from the
field being free. **Interactions are not an independent obstruction.** The entire gravity hinge collapses to
the single question "does ISP's reconstruction stay Lorentz-invariant for interacting fields?" = the §10
residue. (Free-vs-interacting is no longer a separate worry.)

### 5.9 The dynamics leg (HKT): antichain deformations carry the locality skeleton [PROBE, PARTIAL]
Probe code: `code/v6_task2_antichain_deformations.py`. A spatial slice is a maximal antichain (the boundary
of a down-set `D`); a local **normal deformation** advances it by absorbing one event (the available moves
are the minimal elements of `D`'s complement). The defining *locality* signature of the Dirac–Schwinger
algebra is that **normal deformations at spacelike-separated points commute** (the ultralocal
`{H_⊥(x),H_⊥(y)}` structure) while **timelike-related ones are sequenced** by causality. Across sprinklings
(`N=80…200`, several slices, hundreds of pairs each):

| check | result |
|---|---|
| available deformations mutually spacelike (an antichain) | **True**, all trials |
| spacelike deformations **commute** | **True**, all trials |
| timelike pairs **sequenced** by causal order | **True**, all trials |

So the antichain-deformation moves **realize the locality skeleton of the Dirac–Schwinger algebra natively**
— the necessary structural feature for the HKT route.

**Honest scope [OPEN].** This is the *commutation skeleton only*. The part that makes the algebra *general
relativity* — the metric **structure function** `g^{ij}` in `{H_⊥,H_⊥}=g^{ij}H_j` (the HKT uniqueness input)
— is **not** obtained here; it requires the local metric read off the causal data (which §4A shows is
present in the order). §5.10 now carries out that extraction on flat space.

### 5.10 Extracting the structure function `g^{ij}` from causal data [PROBE]
Probe code: `code/v6_task2b_metric_extraction.py`. By "order + number = geometry," the **cardinality of a
causal interval** `I(p,q)={r: p≺r≺q}` estimates its spacetime volume, which fixes the Lorentzian interval
`τ(p,q)` between events *purely from counting*; fitting those intervals as a quadratic form in the
coordinate separations **recovers the metric tensor**. On a flat sprinkling:

| case | recovered `g_{μν}` (normalized `g_tt=1`) | vs Minkowski |
|---|---|---|
| 2D | `g_tt=+1.00, g_tx=+0.01, g_xx=−1.01`  (interval↔count corr `0.98`) | `+1, 0, −1` ✓ |
| 2D, boosted `β=0.5` | `+1.00, −0.00, −1.01` | still Minkowski ✓ (boost-covariant) |
| 3D | `diag(+1.00, −1.00, −0.96)`  (corr `0.95`) | `+1, −1, −1` ✓ |

The induced spatial metric on a slice is the spatial block `h_{ij}=−g_{ij}=δ_{ij}`, so the **HKT structure
function `g^{ij}=δ^{ij}` is recovered from causal data alone** — to a few percent, and boost-covariantly.

So the dynamics leg now has *both* the locality skeleton (§5.9) **and** the structure function extracted
from the order+number (§5.10). **Remaining [OPEN]:** (i) a *curved* test — repeat on a curved sprinkling and
recover the curved `g^{ij}`; and (ii) the final **HKT closure** — verify the antichain-deformation bracket
`{H_⊥,H_⊥}` actually closes on `g^{ij}H_j` with this extracted metric. Step (ii) is what turns "ingredients
present" into "GR derived," and it remains genuinely hard. §5.11 does the curved test of (i).

### 5.11 Curved test: the causal data carries curvature, not just the flat metric [PROBE, noisy]
Probe code: `code/v6_task2c_curved_metric.py`. Does the extractor *see curvature*, or did §5.10 just recover
a fixed flat metric? Coordinate-free test using the two independent causal-data measures — interval
cardinality `|I|` (volume) and longest-chain length `L` (geodesic proper time) — whose flat relation
`|I|∝L^d` acquires a curvature **deficit**. Sprinkling a 2D conformal bump `Ω(x)=1+0.8 e^{−x²/2·0.8²}`
(order = flat-conformal, proper density `∝Ω²`, known `R(x)=2Ω^{−2}(lnΩ)''`):

| | result |
|---|---|
| **flat control** | `|I| ∝ L^{1.85}` (≈ `d=2`: dimension + volume law recovered coordinate-free — a *second* method, independent of §4A); deficit flat across position |
| **curved** | deficit `|I|/L²` correlates with the local `R`: `corr = +0.34`; mean deficit `0.88` where `R<0` vs `1.03` where `R>0` |

So the causal data is **curvature-sensitive**: order+number recovers not just the flat metric but its
curvature, the deficit cleanly separating regions by the sign of `R`.

**Honest caveats.** Causal-set curvature estimators are intrinsically **noisy** at these `N` — the signal is
the *correlation and sign-separation* (`+0.34`; `0.88` vs `1.03`), not a precise `R` value, and the flat
exponent `1.85` runs a few percent low from discreteness/boundary effects. The exact deficit↔curvature
coefficient involves the *directional* Ricci `R_{00}` along the diamond axis, not the scalar `R` alone, so I
claim only demonstrated **sensitivity**, not a calibrated curvature readout.

**Net for the dynamics leg.** The geometric input the HKT route needs — the *curved* `g^{ij}` — is present
in the causal data (flat recovery near-exact, §5.10; curvature detected, §5.11). The single remaining step
is the **bracket closure** `{H_⊥,H_⊥}=g^{ij}H_j` with this extracted metric. §5.12 attacks it directly —
and finds a **negative**.

### 5.12 The bracket closure — an honest negative: order alone gives the Carrollian limit [PROBE]
Probe code: `code/v6_task2d_bracket_closure.py`. The decisive dynamics test: do two *varying-lapse* normal
deformations, applied in both orders relative to the current (tilted) slice, close on the GR form
`{H_⊥[N1],H_⊥[N2]}=H_i[ξ]`, `ξ=g^{ij}(N1∂_jN2−N2∂_jN1)`? Across four sprinklings (`N=3000…6000`, band scales
6–10):

| check | result |
|---|---|
| control `N1=N2` | commutator `=0` **exactly**, every run (the necessary `{H,H[N=N]}=0`) ✓ |
| `N1≠N2` commutator | at the **discretization-noise floor** (~0.2–0.5% of events) |
| localization vs the GR `ξ` profile | **no correlation** (mean `−0.26 ≈ 0`) — it does *not* pile up at the lapse gradients |

**Honest verdict — negative.** The naive order-based deformations do **not** reproduce the GR structure
function. The tiny nonzero commutator is noise, not the geometric `ξ`; the construction sits at the
**abelian / ultralocal (Carrollian)** limit `{H_⊥,H_⊥}≈0`. This makes the obstruction explicit: the GR term
`g^{ij}H_i` is the *metric-dependence of "normal,"* which the bare causal **order cannot supply**. The
metric (extracted from the *number*, §5.10/5.11) is exactly the missing datum — but **"order + metric →
exact Dirac–Schwinger" is not achieved here.** That is the genuine open core, it is hard, and this probe
shows it is *not* fakeable by the naive construction. A finer construction (the metric defining the normal
direction, with the bracket closing to Dirac–Schwinger in the continuum limit) is the real unfinished work.
§5.13 diagnoses *why* the naive one fails and whether scaling could rescue it.

### 5.13 Why it fails — structural (gradient-blindness), not noise [PROBE]
Probe code: `code/v6_task2e_AvsB_diagnostic.py`. Is the §5.12 null because the GR term is structurally
*absent* (A), or merely *subleading and noise-swamped* (B, fixable by resolution)? Hold the physical
deformation fixed (band scale `s∝N`) and raise `N`, averaging over realizations; signal metric =
**enrichment** `=⟨|ξ|⟩` over commutator events `/ ⟨|ξ|⟩` over deformation-touched events (>1 and rising ⇒ B;
≈1 flat ⇒ A):

| `N` | commutator/real | enrichment | hist corr |
|---|---|---|---|
| 1500 | 8.5 | 0.83 | −0.67 |
| 3000 | 14.2 | 0.92 | −0.32 |
| 6000 | 18.3 | 0.73 | −0.76 |
| 10000 | 25.0 | 0.84 | −0.54 |

(control `N1=N2`: commutator `=0` exactly, all `N`.)

**Verdict: (A), structural.** Enrichment sits at ~0.8 (`≤1`, no climb) and the correlation stays negative
across a 7× range of `N` — the GR shift is *not* subleading-but-present, it is absent at every resolution.
**Scaling cannot fix it.**

**Mechanism — a mini no-go for the pointwise class.** The naive deformation is a *pointwise function of the
lapse value* `N(x)` and the local count-height; it has **no dependence on the lapse gradient `∂N` or the
slice tilt**. Two pointwise-value rules commute by construction, so `{H_⊥,H_⊥}=0` is *forced* — the
Carrollian limit is structural for the entire class. The negative correlation confirms it: the residual
commutator is boundary noise piling up at the lapse *extrema* (where `∂N≈0`, so `|ξ|` is small) — it is
**value-driven, not gradient-driven**.

**Consequence.** The GR term `g^{ij}(N∂_jM − M∂_jN)` is intrinsically a *gradient × metric-direction*
effect, which no pointwise-value rule can produce. Lifting Carrollian → GR therefore requires a deformation
that (i) is sensitive to the slice tilt / lapse gradient and (ii) leans along a spatial direction set by the
metric — a genuinely non-pointwise, direction-coupled construction, which in turn needs a *combinatorial
notion of spatial direction* (an open causal-set problem). So the honest fork is resolved: **scaling is out;
the path is the directional construction, or a full no-go theorem for `k`-local order+count deformations.**
§5.14 proves that no-go for the gradient-blind class and pins the one missing ingredient.

### 5.14 No-go theorem: gradient-blind deformations are Carrollian [THEOREM + PROBE]

**Setup.** A causal set `(C,≺)`; a down-set `D` (the past of a slice); a *lapse field* `N(e)≥0`; a
*deformation* `Φ_N: D ↦ Φ_N(D) ⊇ D`. Define the class **𝒫** (pointwise-additive height-threshold):
- **(H1) threshold form** — there is a height field `h(e,D)≥0` (remaining proper-time/volume from the slice
  to `e`, `∝` interval count) with `Φ_N(D) = D ∪ { e∉D : h(e,D) ≤ s·N(e) }`, scale `s>0`;
- **(H2) pointwise additivity** — advancing by `N` reduces the remaining height *at `e` by exactly* `s·N(e)`:
  `h(e, Φ_N(D)) = h(e,D) − s·N(e)`, i.e. the height's lapse-dependence is *pointwise* (`N(e)` only).

**Theorem.** For all `N, M, D`:
```math
\Phi_M(\Phi_N(D)) \;=\; \Phi_N(\Phi_M(D)) \;=\; D \cup \{\, e : h(e,D) \le s\,(N(e)+M(e)) \,\},
```
so `[Φ_N, Φ_M] = 0` identically, and the induced bracket is the **Carrollian (ultralocal)** one,
`{H_⊥[N], H_⊥[M]} = 0` — *not* general relativity.

**Proof.** `Φ_N` absorbs `A_N={e∉D: h(e,D)≤sN(e)}`. Applying `Φ_M` to `D∪A_N`, by (H2) the remaining height
is `h(e,D)−sN(e)`, so it absorbs `{e: h(e,D)−sN(e) ≤ sM(e)} = {e: h(e,D) ≤ s(N(e)+M(e))}`. The union is
`{h(e,D) ≤ s(N+M)}`, symmetric under `N↔M`; hence both orders coincide. ∎

**Why this is exactly the GR obstruction.** In the continuum `{H_⊥[N],H_⊥[M]}=H_i[ξ]`,
`ξ^i = g^{ij}(N∂_jM − M∂_jN)`: the shift is the **metric-raised antisymmetric lapse gradient**. Hypothesis
(H2) — height reduced by exactly `s·N(e)` — is precisely the statement that the slice advances along the
*un-raised* gradient `∂_μT` with **no tilt**. The GR term appears only when the second push is normal to the
*tilted* slice, i.e. when the height reduction picks up a correction coupling `N` at *neighbouring* events
through `∂_jN` and the inverse spatial metric `g^{ij}`. In one line: **the GR structure function is the
operator `∂_jN ↦ g^{ij}∂_jN` (the normal tilt); a rule whose lapse-dependence is pointwise never forms
`∂_jN`, a fortiori never `g^{ij}∂_jN`, so `ξ=0`.**

**Numerical confirmation** (`code/v6_task2f_nogo_confirm.py`):

| `N` (events) | ideal pointwise-additive `|comm|` | §5.12 recomputed-`ha` `|comm|` |
|---|---|---|
| 2000 | **0** | 19 |
| 4000 | **0** | 13 |
| 8000 | **0** | 31 |

The ideal class commutes *exactly* (the theorem); §5.12's small residual is the (H2)-violating boundary
discreteness, which §5.13 showed is gradient-blind noise. The empirical Carrollian result is now a theorem.

**Corollary — the one missing ingredient, isolated.** Escaping the Carrollian class *requires* violating
(H2) with a genuine neighbour-lapse coupling, which needs three things: (i) a finite-difference **lapse
gradient `∂N`** — `k`-local, trivially available; (ii) the **inverse spatial metric `g^{ij}`** to raise it
— *available*, extracted from interval counts (§5.10 flat, §5.11 curved); (iii) a combinatorial **spatial
direction** on the slice to contract `g^{ij}∂_jN` — the (then-)open ingredient. **Two of the three are in
hand; the entire obstruction reduces to the combinatorial spatial-direction problem** — which §5.16 below
shows is *recoverable* from order+counts, closing the reduction.

**Honest scope (what this does and does not show).** It rules out the *gradient-blind* (pointwise-additive)
class — the natural/naive one, and the one §5.12 used — proving it is *necessarily* Carrollian. It does
**not** rule out gradient-coupled `k`-local deformations (those violating (H2) by design); by the Corollary
that is exactly where GR could live. So this is **not** "causal sets cannot do GR dynamics"; it is a sharp
theorem that *kinematics-blind* evolution cannot, and a precise reduction of the open problem to ingredient
(iii). (A full no-go would need to show *no* `k`-local rule can supply a consistent combinatorial spatial
direction — and §5.16 finds the opposite: the direction *is* recoverable, so the full no-go does **not** hold
by this route.)

### 5.15 Correction: what the down-set commutator does — and does not — measure [IMPORTANT REVISION]

A re-examination corrects the *interpretation* of §5.12–5.14 (the theorems and numbers stand; the reading of
them does not). Those probes measured the **down-set commutator** — does `N`-then-`M` absorb a different set
of events than `M`-then-`N`? But in canonical GR the commutator of two pure normal deformations is
`{H_⊥[N],H_⊥[M]} = H_i[ξ]`, a **purely tangential** deformation: it slides points *within* the hypersurface,
leaving the surface **as a point-set — and hence its causal past (down-set) — invariant**. Consequences:

- **The down-set commutator vanishes in GR too**, not only in the Carrollian limit. It is *blind* to the
  tangential structure function `g^{ij}`. So it cannot distinguish GR from Carrollian — both give `≈0`.
- §5.14's *exact* down-set commutativity for pointwise-additive rules is therefore **not** a Carrollian
  no-go. It is the statement that the final slice is **path-independent** — i.e. **refoliation invariance /
  integrability**, which is a *hallmark of* the GR hypersurface-deformation algebra (Teitelboim
  embeddability). That is **GR-consistent good news**, not an obstruction.
- The genuine GR-vs-Carrollian distinction lives in the **tangential flow** — how the slice's *labeling*
  (or fields carried on it) is dragged by `ξ = g^{ij}(N∂_jM − M∂_jN)` — which the bare-set tests never access.

**Revised reading.** §5.12–5.14 actually establish that the causal-set normal deformations are *integrable /
refoliation-invariant* (consistent with GR), and that the structure function is invisible to the bare-set
observable — **not** that the algebra is Carrollian. The correct test is the **flow-drift** test: does the
commutator drag the slice labeling tangentially by `ξ = g^{ij}(N∂_jM − M∂_jN)`, with the coefficient the
extracted `g^{ij}`? This requires a spatial frame recovered from the
causal data (§5.16) and is carried out in §5.17. (I flag this as a correction of my own earlier
over-interpretation: "commutator → 0" was wrongly read as "Carrollian"; it is the refoliation-invariance the
algebra requires.)

### 5.16 Ingredient (iii): is the oriented spatial direction recoverable from causal data? [PROBE]

The no-go (§5.14) reduced the GR structure function to three ingredients, of which (i) `∂N` and (ii) `g^{ij}`
(§5.10–5.11) are in hand; the open one was (iii) an **oriented spatial direction** on the slice. This is not
spatial *distance* (a scalar) nor the spatial *Laplacian* (an unoriented scalar operator) — both of which the
literature provides — but a *vector* structure: the antisymmetric `N∂M − M∂N` needs *oriented* gradients.

**State of the art [EST].** Timelike distance is solved (interval cardinality, §5.10). Spacelike distance is
"surprisingly difficult" (Rideout–Wallden 2009, from discreteness + Lorentz invariance), but finite-region
estimators via the common future `J⁺(p)∩J⁺(q)` give a *spatial nearest-neighbour* relation; thickened
antichains recover spatial *topology* (Major–Rideout–Surya) and a spatial *Laplacian* (spectral-dimension
work). So a spatial *adjacency graph* is available — but an *oriented* frame was not established.

**The test (`code/v6_p2_spatial_direction.py`).** A spatial adjacency graph that reflects proximity should,
by spectral graph theory (Laplacian eigenmaps), carry the spatial coordinates in its low Laplacian
eigenvectors. Build the slice graph from causal data only — connect `p,q` if their earliest common-future
"meeting height" (`min_{z∈J⁺(p)∩J⁺(q)}` of the count-height of `z` above the slice, `∝` spatial distance) is
small (`k`-local) — spectral-embed, and correlate the eigen-coordinates with the *true* slice coordinates
(which the construction never sees):

| test | metric | result |
|---|---|---|
| 1+1: recover `x` from Fiedler `v₂` | `|corr(v₂, x_true)|`, 6 trials | mean **0.94** (0.84–0.99) |
| 2+1: recover `(x,y)` from `{v₂,v₃}` | `R²` of `x`,`y` on the embedding | **0.95**, **0.92** |

The low eigenmodes **are** the spatial coordinates: an oriented frame (up to the `O(d)` tangent-frame gauge)
is recovered *cleanly* from order+counts. A `k`-**local** version (per-event classical MDS on the
meeting-height neighbourhood, Procrustes-aligned to true local positions; `code/v6_p2b_local_frame.py`)
recovers the local frame too, but **noisily**: mean `0.78`, median `0.83`, 56% of neighbourhoods `> 0.8`.

**Result.** The oriented spatial direction **is** recoverable from order+counts — cleanly globally, noisily
locally. **Ingredient (iii) is available; not a no-go.** All three ingredients of `g^{ij}∂_jN` are now
present in the causal data. (Caveat: the local estimator is noisy — the known spacelike-distance difficulty;
and this supplies the *frame*, not yet the assembled deformation, which §5.17 takes up.)

### 5.17 The flow-drift test — the correct observable [PROBE]

§5.15 established the down-set commutator is blind to the structure function; the right observable is the
tangential **flow-drift** under the commutator of two normal deformations — GR predicts
`ξ = g^{ij}(N∂_jM − M∂_jN)` (1+1 flat: `NM'−MN'`), Carrollian predicts `0`.

**Part 1 — noise-free grid (mechanism)** (`code/v6_p2c_flow_drift.py`). Push each slice point along the local
unit normal `n=(1,T')/√(1−T'²)` by `ε·lapse`; a tilted slice's normal leans spatially, so the two orders
drift comoving labels differently. The commutator drift vs the GR prediction `−ε²(NM'−MN')` has **corr =
+1.0000**, slope/(−ε²) = **1.001**. The assembled normal-flow reproduces the GR tangential drift `ξ`
*exactly* — the three ingredients (`∂N`, `g^{ij}`, oriented normal) combine into the GR structure function.
**Mechanism confirmed.**

**Part 2 — causal set, recovered frame (noisy).** Give slice events the recovered coordinate `u` (§5.16),
estimate lapse gradients from the recovered frame, form the drift commutator from those causal-frame
quantities, and test against the *true* GR profile. Over 5 sprinklings (`|A|~85`):

| metric | result | §5.12 gradient-blind null |
|---|---|---|
| `corr(`drift, `−ξ_true)` | **+0.63** (per-trial 0.33–0.84) | ~0 |
| enrichment of `|`drift`|` at high `|ξ|` | **1.38** | ~0.8 |

The flow-drift built on the **recovered** frame **tracks the GR profile `ξ`** — noisily (corr 0.63) but
**clearly above the §5.12 null**. The recovered frame is good enough to *express* the GR tangential drift.

**Verdict.** The correct observable gives a **positive (noisy) signal**: mechanism exact (grid), and on real
causal data the drift carries the GR structure where the bare-set observable was blind. With §5.15, the
dynamics leg reads: *refoliation-invariant (GR-consistent)* **and** *the GR structure function is recovered in
the tangential flow.* **Honest caveats:** (a) Part 2 forms the drift via the mechanism *formula* with
frame-estimated gradients — it tests whether the recovered frame can *express* `ξ` (yes, noisily), not a full
event-by-event flow; (b) **flat only** — the `g^{ij}` *coefficient* (GR vs a rescaled/Hořava theory) is not
tested here; that is **§5.18** below; (c) noisy; (d) continuum limit and *exact* closure open. *Suggestive
evidence that the directional deformation reproduces GR — not a proof.*

### 5.18 The curved-coefficient test — GR vs Hořava [PROBE]

§5.17 was flat, where `g^{ij}=δ^{ij}`, so the coefficient is trivially constant — flat space *cannot*
distinguish GR (structure function = the curved spatial metric) from a rescaled/Hořava theory (structure
function a constant, or anisotropic). Curved space can. Take the 2D conformal metric
`ds² = Ω²(x)(−dt²+dx²)`, inverse spatial metric `g^{xx}=1/Ω²(x)`. Analytic mechanism (the `Ω'` terms cancel):
the commutator of two curved-normal deformations drifts a tracer by `Δx = −ε² (1/Ω²)(NM'−MN')`, so the
**coefficient is `C(x)=1/Ω²(x)=g^{xx}(x)`** — the curved metric (GR). Code: `code/v6_p2d_curved_coefficient.py`.

**Part 1 — clean grid (the discriminator has power).** Pushing along the geometric curved unit normal
`n^μ=(1/Ω)(1,T')/√(1−T'²)`: `corr(C, 1/Ω²)=+1.0000`, centre/wing `C = 0.239` (GR target `0.232`). A "Hořava"
flat-normal push (ignore `Ω`): `corr=+0.01`, centre/wing `1.000` (flat). The test cleanly **separates** them
— GR dips with the curvature, Hořava stays flat. (This leg *uses* `Ω` to define the target; its job is to
prove the discriminator distinguishes and to set the profile the causal set must reproduce.)

**Part 2 — causal set, `Ω` never inserted.** The coefficient `C=1/Ω²=(1/Ω)²` is the squared proper-time
Jacobian, and the causal set supplies proper time via **longest chains** (no `Ω` inserted). On a conformal
sprinkling (density `∝Ω²`, proper-uniform) extract, from order+number only, two **independent** channels at
each `x` (binned on the true `x`, used as an evaluation axis only): (A) `Ω_chain(x)` from the longest chain in
a thin coordinate-time slab (`∝` proper time `∝ Ω`); (B) `Ω_dens(x)` from the local number density (`∝ Ω²`).
Over 6 sprinklings (`|·|~60k`):

| quantity | result | meaning |
|---|---|---|
| `corr(C_chain, 1/Ω²_true)` | **+0.99** | flow-drift coefficient (chains) tracks the **curved** metric |
| centre/wing of `C_chain` | **0.21** (GR `0.16`; Hořava `1.00`) | dips with curvature — **not constant** |
| `corr(C_chain, C_dens)` | **+0.99** | proper *time* and proper *volume* agree → **isotropic (Lorentzian, z=1)** |

So the coefficient recovered from causal data **is the curved inverse metric `g^{ij}` (GR), not a constant
(Hořava)**, and the two independent geometric channels agreeing rules out anisotropic (Lifshitz `z≠1`)
scaling — a genuinely non-trivial cross-check (proper time `∝Ω` vs volume `∝Ω²` is local Lorentz invariance).

**Honest caveats.** (a) Part 2 measures the proper-time *Jacobian* that the Part-1 mechanism *proves* equals
the coefficient — it is not a full event-by-event flow (same class of caveat as §5.17). (b) The `C_dens`
channel is **near-tautological** (density `∝Ω²` was the sprinkling rule), so the load-bearing result is
`C_chain` and the **chain-vs-density agreement**. (c) The centre dip is slightly shallow (`0.21` vs `0.16`) —
finite-slab / finite-`N` smoothing. (d) **Scope (the key limit):** this shows the v6 *construction* is
**GR-faithful in curved space** — order+number deliver the curved metric as the structure function — *given a
Lorentzian (proper-uniform) sprinkling*. It does **not** show the *dynamics* **selects** GR over Hořava; the
causal set faithfully encodes whatever is sprinkled, so "is the substrate forced to be such a sprinkling"
reduces to the **already-identified** Lorentz-invariance residues (§4B Poisson hypothesis, §10 reconstruction).

**Higher dimensions — the tensor coefficient (2+1 and the physical 3+1).** 2D is degenerate: the slice is 1D,
so `g^{xx}` is a *scalar* — Parts 1–2 test its *magnitude* and time/space isotropy, but not the *tensor*
character (anisotropy, off-diagonal rotation) where a Hořava/Lifshitz structure function would differ. The
mechanism is dimension-agnostic: `Δx^a = −ε² h^{ab}(N∂_bM − M∂_bN)`, with `h^{ab}` the **full inverse spatial
tensor** (`2×2` in 2+1, `3×3` in 3+1). On an anisotropic, fully off-diagonal metric the measured two-step
drift *vector* tracks the tensor prediction to `cos = 1.0000`, **rotated away from the isotropic-scalar
direction** by exactly the tensor's predicted angle:

| case | code | `cos(meas, tensor)` | `cos(meas, isotropic)` | rotation (pred = meas) |
|---|---|---|---|---|
| 2+1 (`2×2`, planar) | `v6_p2e_3d_tensor_coefficient.py` | 1.0000 | 0.973 | 13.4° |
| **3+1 (`3×3`, SO(3))** | `v6_p2f_4d_tensor_coefficient.py` | 1.0000 | 0.974 | **13.1°** |

So in the physical 3+1 case the structure function is the **full `3×3` spatial metric tensor (GR)**, not its
scalar part — an isotropic/scalar (or wrong-tensor Hořava/Lifshitz) coefficient is *excluded by the SO(3)
rotation*. (Leading-order grid mechanism, as in Part 1; the causal-set extraction of the 3D spatial-metric
*tensor* was shown in §5.10, diag recovered to a few %.)

**Verdict.** The flow-drift coefficient **scales with the curved `g^{ij}` (GR), not a constant (Hořava)** —
the §5.17 next-probe lands positive, in both the 2D magnitude and the 2+1 tensor structure. The dynamics leg now reads: refoliation-invariant (§5.15), GR tangential
drift recovered (§5.17), and that drift carries the **curved metric** as its coefficient (§5.18, conditional
on a Lorentzian sprinkling). The remaining dynamics-leg openness is no longer "is the coefficient the metric?"
but the *same* substrate-Lorentz-invariance question as the rate leg (§4B/§10) plus the continuum/exact closure.

---

## 6. The covariance residue (§10): does indivisibility clear the interacting obstruction? [PROBE + ARG]

Everything above reduces to **one** residue: does the relativistic ISP reconstruction stay Lorentz-covariant
for *interacting* fields (§4B/§5)? This section attacks it as far as is honestly computable and locates the
irreducible analytic core.

**State of the problem [EST].** The *free* case exists — Tumulka's rGRWf (2006) is a manifestly
Lorentz-invariant flash process for non-interacting systems. The *interacting* case is the long-standing open
problem of relativistic collapse models. §1.1's "killers" (energy non-conservation, Wigner negativity, Haag's
theorem, Tomonaga–Schwinger integrability) reduce to a single covariance residue, with **indivisibility the
one ISP-specific lever**. The most concrete obstruction is the **energy-production divergence**: white
(Markovian) collapse noise couples to a quantum field and injects energy at *every* frequency → a UV-divergent
heating rate (Pearle's relativistic CSL; regulated in the literature only by Bedingham's mediating-field
smearing or Adler–Bassi colored noise).

**The lever, made quantitative [PROBE].** Indivisibility *is* non-Markovianity: the indivisible process has
memory — a finite noise correlation time `τ_c` (the same `τ_c` that turns paper1/v5p2 gravitational
decoherence into a Gaussian onset). Finite memory ⇒ a noise power spectrum `S(ω)` that decays at high `ω`, so
it cannot excite arbitrarily high field modes. For a 3D massless field the heating rate is
`dE/dt ∼ ∫₀^Λ ω³ S(ω) dω`. Code: `code/v6_10_indivisibility_covariance.py`.

| noise (correlation structure) | spectrum `S(ω)` | heating `dE/dt` | `H(2Λ)/H(Λ)` |
|---|---|---|---|
| white (Markovian) | `1` | `∝ Λ⁴` — **divergent** | 16.0 |
| exponential-correlation (OU) | `1/(1+(ωτ)²)` | `∝ Λ²` — still **divergent** | 4.0 |
| **smooth / indivisible** | `exp(−(ωτ)²)` | `→ 1/(2τ⁴)` — **finite, cutoff-independent** | 1.0 |

The smooth (Gaussian-spectrum) indivisible correlation makes the interacting heating **finite and
`Λ`-independent** (`H = 1/(2τ⁴)` to numerical precision, `→0` as the memory `τ_c` grows) — removing the
relativistic-collapse energy catastrophe. A sharp sub-finding: **colored alone is not enough** —
exponential-correlation (Lorentzian spectrum) still diverges *quadratically* in 3D; the regulator must be
**smooth** (faster-than-power-law spectral decay). *(Correction, sharpened in v6 Paper 2 Part II §4: this `τ` is a
frame-fixed temporal scale. The **covariant** memory is a function of the interval `g(s²)`, whose spectrum
`ĝ(q²)` must decay in the **spacelike** region too; a Gaussian-in-`s²` blows up spacelike, while the
quartic template `ĝ(q²)=e^{−q⁴/β⁴}` passes the two-sided tail test. The finiteness conclusion stands; the
specific Gaussian form does not, and quartic damping is an admissible template rather than a uniqueness
theorem.)*

**But this regulation was frame-fixed — and that exposes the real structure of §10 [PROBE].** The `τ_c` above
is a Gaussian in *one frame's* time: a **preferred-frame** smoothing. It makes the energy finite but is **not
covariant** — sampled along a boosted worldline its correlation time shrinks by time dilation, so the heating
is frame-dependent (`H_boost/H_rest = 3.10` at `v=0.6`; `code/v6_10b_covariant_correlation.py`). The fix is
*exactly* the covariance requirement: a **Lorentz-invariant** correlation `C = f(s²)` (function of the
invariant interval). Along *any* inertial worldline `s² = (proper time)²`, so `f(s²)` is automatically
frame-independent — and the probe confirms the heating is then identical in every frame (`H_boost/H_rest =
1.000`) *and* finite. **So smoothness and covariance are not two assumptions — they are two faces of one
object: a Lorentz-invariant, microcausal indivisible correlation.** Demanding integrability (covariant,
microcausal coupling) makes the correlation a function of `s²` with a single proper-time scale, which delivers
the finite *frame-independent* heating **as a corollary**. Establishing interacting integrability would
therefore *derive* the smoothness, not add it as a separate conditional — answering "is smoothness an extra
assumption?": **no, it is downstream of integrability.**

**What this does and does not settle.** §10 collapses to **one object**: does the *interacting* indivisible
reconstruction produce a **Lorentz-invariant correlation `f(s²)` with fast-enough falloff**? The energy/heating
facet (one §1.1 killer) is then automatic — finiteness and frame-independence both follow from that single
covariant correlation (shown above for a model `f(s²)`). What is **not** constructed here is that the
interacting indivisible reconstruction *actually yields* such a correlation — i.e. the full
**Tomonaga–Schwinger integrability**: that the evolution be path-independent between arbitrary spacelike slices
(`[𝓗(x),𝓗(y)]=0` for spacelike separation — microcausality of the coupling). That
is the genuinely analytic problem — the same one that gates interacting rGRW — and it is **not** closed here.
**§10 now reads as a *single* residue: produce a Lorentz-invariant microcausal indivisible correlation
`f(s²)` — energy-finiteness comes free with it once the two-sided tail condition is supplied; that is the
interacting Tomonaga–Schwinger integrability, the one open analytic core** (taken up, with its literature and
decisive sub-questions, in **v6 Paper 2 Part II**).

---

## 7. Honest status: open steps, kill-criteria, the first real calculation

**Open steps (increasing hardness):**
1. **[the rate leg — now reduced to covariance alone]** Does the relativistic-ISP construction give a
   division rate that is a **Lorentz scalar** (per proper 4-volume)? Free case: **exists** (rGRW).
   Interacting detector (§5.7) and **arbitrary self-interactions** (§5.8, via Källén–Lehmann): **scalar ✓** —
   covariance and thermality follow from Lorentz invariance, *not* freeness, so interactions add no
   obstruction. **Sole remaining question:** does ISP's reconstruction *stay Lorentz-invariant* for
   interacting fields? — the §10 residue, now **sharpened in §6** to a single object: produce a
   Lorentz-invariant microcausal indivisible correlation `f(s²)` (the energy-finiteness then comes free, not
   as a separate assumption). That is interacting Tomonaga–Schwinger *integrability* — the one open analytic
   core.
2. **[the substrate-Lorentz leg — kill-test now operational, §4B(B′)]** Is the division-event *set*
   genuinely **frame-invariant** (Poisson per 4-volume, no reconstructable preferred frame)? The
   frame-reconstruction kill-test **passes** a Poisson process (signal `S=0.21`, no preferred frame) and
   **kills** any synchronized/clocked global-time process (`S≈77`, rest frame recovered), and shows this
   condition is *identical* to step 1's scalar rate: the events survive **iff** Poisson-per-proper-4-volume =
   scalar rate. So steps 1 and 2 are **one** residue (§10), not two — the kill-criterion is now sharp and
   tested; what is unproven is only whether the interacting reconstruction *meets* it.
3. **[the dynamics leg — ingredients present, but the closure FAILS naively → Carrollian]** Antichain
   deformations reproduce the **commutation skeleton** of the Dirac–Schwinger algebra (§5.9), and the
   **structure function `g^{ij}` is extractable from causal data** — flat `δ^{ij}` near-exact (§5.10),
   curvature detected (§5.11); and the **spatial direction (iii) is recoverable** (§5.16: spectral
   clean `corr 0.94`/`R² 0.93`, local MDS noisy median 0.83). The down-set commutator vanishes for the naive
   class (§5.12–5.14) — **but §5.15 corrects the reading**: that vanishing is **refoliation invariance**
   (path-independent slice = integrability), which is *GR-consistent*, **not** Carrollian (the bare-set
   observable is blind to the tangential `g^{ij}`). **No no-go remains.** The genuine observable is the
   **flow-drift** (does the commutator drag the slice *labeling* by `ξ = g^{ij}(N∂_jM − M∂_jN)`?), and
   **§5.17 finds a positive (noisy) signal**: the assembled mechanism reproduces `ξ` *exactly* in
   the noise-free grid (corr +1.00), and on the recovered frame the drift *tracks* `ξ` (corr +0.63,
   enrichment 1.38) — far above the §5.12 null. **§5.18 then settles the coefficient (GR vs Hořava):** in
   *curved* space the flow-drift coefficient recovered from order+number tracks the **curved inverse metric
   `1/Ω²` (corr +0.99), not a constant** — and proper-time (chains) vs proper-volume (counts) agree (corr
   +0.99 → isotropic, Lorentzian `z=1`). So the structure function **is** the curved metric (GR), *given a
   Lorentzian sprinkling*. Remaining: the continuum limit, the *exact* closure, and — the only deep residue —
   whether the substrate **is** such a sprinkling (= the §4B/§10 Lorentz-invariance question, shared with the
   rate leg).
4. **[OPEN]** The causal-set **continuum limit / inverse problem**.

**Kill-criteria (what would falsify v6):**
- If ISP's division events are **lattice-like or frame-dependent**, the substrate breaks Lorentz invariance
  (§4B) and the program is dead as stated.
- If antichain deformations **cannot** close into the Dirac–Schwinger algebra, HKT does not apply and the
  Einstein coupling is not delivered (one might land on a Hořava-type modified gravity instead — a different,
  weaker outcome).

**Where the calculation stands — both legs probed, two precise residues left.** *Rate (kinematic) leg:* the
hinge is a scalar division-rate; this now holds for free (rGRW), an interacting detector (§5.7), and
**arbitrary self-interactions** (§5.8) — covariance, not freeness, is what carries it, so the *only*
remaining question is whether ISP's reconstruction stays Lorentz-invariant (= **§10**). *Dynamics
(geometry) leg:* all three *ingredients* are present — locality skeleton (§5.9), structure function `g^{ij}`
extracted from causal data (flat §5.10, curvature §5.11), and the oriented **spatial direction** (§5.16,
recoverable). The down-set commutator vanishes for the naive class (§5.12–5.14) — **and §5.15 corrects
its reading**: that vanishing is **refoliation invariance** (the final slice is path-independent), a
*GR-consistent* property the bare-set observable shares with both GR and Carrollian; it is **not** a
Carrollian no-go (my earlier reading was wrong). The genuine GR-vs-Carrollian distinction is the **tangential
flow-drift** — does the commutator drag the slice labeling by `ξ = g^{ij}(N∂_jM − M∂_jN)`? — which **§5.17
now tests with a positive (noisy) signal** (mechanism exact in the noise-free grid, corr +1.00;
recovered-frame drift tracks `ξ`, corr +0.63, enrichment 1.38, vs the §5.12 null), and **§5.18 then settles
the GR-vs-Hořava coefficient**: in *curved* space the coefficient recovered from order+number tracks the
**curved inverse metric `1/Ω²` (corr +0.99), not a constant**, with proper-time (chains) and proper-volume
(counts) agreeing (corr +0.99 → isotropic, Lorentzian). The two legs are tied by one fact (the record rate's
Unruh temperature is Jacobson's `δQ=TδS` input). Honest summary: the **rate leg is in good shape** — scalar
rate confirmed (free/interacting/self-interacting), *sole* residue §10. The **dynamics leg** has *no
surviving no-go*: its deformations are refoliation-invariant (GR-consistent), all ingredients are present,
the **flow-drift shows positive (noisy) evidence** that the bracket carries the GR structure `ξ`, and its
**coefficient is the curved metric `g^{ij}` (GR, not Hořava)** — *given a Lorentzian sprinkling*. So the
dynamics leg's only deep residue is no longer the coefficient but the **same substrate-Lorentz-invariance
question as the rate leg** (§4B/§10), plus the continuum limit and the *exact* closure. And that shared
residue is **itself sharpened in §6** to a single object: a Lorentz-invariant microcausal indivisible
correlation `f(s²)` — with the energy-finiteness shown to be *downstream* of covariance, not a separate
assumption (frame-fixed smoothing heats frame-dependently, `ratio 3.10`; the covariant `f(s²)` gives
`ratio 1.000` and finite). So v6 is **two legs that both reduce to one shared residue (substrate Lorentz
invariance, §4B/§10), now sharpened to producing a covariant indivisible correlation, with positive evidence
everywhere it has been probed** — not a derivation of GR, but a precisely-mapped frontier with no no-go
standing, both legs pointing the same way, and the single remaining open core named (interacting
Tomonaga–Schwinger integrability).

---

## 8. What this paper does not claim

It does not derive general relativity; it does not solve the relativistic-QFT reconstruction; it does not
derive the holographic area law; it does not show ISP's division events Poisson-sprinkle. In particular, the
§5.18 curved-coefficient result shows the *construction* is GR-faithful — order+number deliver the curved
metric as the structure function, not a constant (Hořava) — **conditional on a Lorentzian sprinkling**; it
does **not** show the *dynamics* **selects** an isotropic (GR) substrate over an anisotropic one (that is the
§4B/§10 Lorentz-invariance question). It proposes a specific, obstruction-aware extension of ISP, argues it
preserves the quantum reconstruction (and may ease the open relativistic residue), verifies the geometry-side
mechanism numerically at small scale, and reduces the gravity question to one decisive, bounded test. The fallback, if full GR is out of reach, is the
**unimodular** sourcing already in v-paper4 — to which v6 adds one conjecture: that unimodularity's fixed
volume form is the geometric shadow of the indivisible process's conserved probability measure.

---

## References / pointers

Internal: Paper 2 v6 for the relativistic event-law/branch-A audit; Paper 3
v6, `relativistic-isp-v6-paper3-modular-record-diamonds.md`, for the CMRP
and sealed modular record-diamond ontology.

External (dressing, defined as needed): Barandes, *The stochastic-quantum correspondence/theorem*
(arXiv:2302.10778, 2309.03085); Sorkin, causal sets ("order + number = geometry"); Bombelli–Henson–Sorkin
(Lorentz invariance ⇒ Poisson sprinkling); Myrheim 1978 / Meyer (dimension estimator); Hojman–Kuchař–
Teitelboim, *Geometrodynamics regained* (1976); Jacobson, *Thermodynamics of spacetime* (1995);
Benincasa–Dowker (2010), causal-set d'Alembertian. *For the spatial-direction recovery (§5.16):*
Brightwell–Gregory (timelike distance); Rideout–Wallden, *Spacelike distance from discrete causal order*,
CQG **26**, 155013 (2009), arXiv:0810.1768; Major–Rideout–Surya, *Spatial Hypersurfaces in Causal Set
Cosmology*, gr-qc/0506133; Eichhorn–Mizera–Surya, *Spectral dimension on spatial hypersurfaces in causal set
quantum gravity*, arXiv:1905.13498; Belkin–Niyogi (Laplacian eigenmaps). *For the covariance residue (§6/§10):*
Tumulka, *A relativistic version of the GRW flash model* (J. Stat. Phys. 2006, quant-ph/0406094); Pearle,
relativistic CSL & the energy-production problem (e.g. Phys. Rev. D **91**, 105012, 2015); Bedingham,
*Relativistic state reduction dynamics* (Found. Phys. 2011, arXiv:1003.2774, mediating field); Adler–Bassi,
colored/non-white CSL noise; Tomonaga–Schwinger integrability.

Internal: `publishable/paper2-hypersurface-deformation-obstruction.md` (the residue this paper targets);
`publishable/paper4-unimodular-gravity-from-nonconserved-matter.md` (the fallback + non-conservation);
`code/magic_vs_indivisibility.py` (magic ≠ indivisibility, §1.3); `code/v6_causal_set_feasibility.py`
(the §4 probe); `relativistic-isp-v6-paper2-spatial-direction-and-interacting-integrability.md` (combined Paper 2:
spatial-frame/flow-drift plus the interacting TS-integrability and A/B memory-derivation leg);
`code/v6_p2_spatial_direction.py`, `code/v6_p2b_local_frame.py` (the §5.16 spatial-direction
recovery, global + `k`-local); `code/v6_p2c_flow_drift.py` (the §5.17 flow-drift test);
`code/v6_p2d_curved_coefficient.py` (the §5.18 curved-coefficient GR-vs-Hořava test);
`code/v6_p2e_3d_tensor_coefficient.py`, `code/v6_p2f_4d_tensor_coefficient.py` (the §5.18 tensor-coefficient
extension, 2+1 and 3+1); `code/v6_4b_division_event_lorentz_kill.py` (the §4B(B′) kill-test:
frame-reconstruction + worldline rate); `code/v6_10_indivisibility_covariance.py` (the §6/§10 probe:
indivisibility regulates the interacting heating divergence); `code/v6_10b_covariant_correlation.py`
(the §6 refinement: covariance and energy-finiteness are one object — `f(s²)` heats frame-independently).
