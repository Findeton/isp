# ISP v17 — MG0 B0 platform feasibility and selection gate

**Status:** ACTIVE AUTHOR-SIDE PHYSICS AUDIT / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-24
**Scientific result awarded:** none
**Platform selected:** none

---

## 0. Executive verdict

The B0 platform cannot be chosen by total mass, coherence time, fringe
visibility, or projected gravitational phase separately. The physically
relevant source quantity is the branch-dependent mass distribution together
with its many-body correlation structure. The relevant experimental object is
one complete source--apparatus--probe record law, not a best-of-platform
collage.

This audit derives a conjunctive selection rule and applies it to the current
primary evidence. It produces five conclusions.

1. A newly published 2026 experiment demonstrates center-of-mass
   matter-wave interference of sodium clusters above `170 kDa`, with a
   reported center-of-mass delocalization scale of `133 nm`. The earlier
   generic statement that nanoparticle center-of-mass interference is absent
   is therefore false and is corrected here.
2. That advance remains about `3.54e7` below the `1e-14 kg` microsolid mass
   used in a favorable screened QGEM reference. Even under the deliberately
   unrealistic gift of `1 s` interaction at `35 micrometres`, its symmetric
   two-body Newtonian branch phase is only about `2.08e-20`, versus
   `1.48e-3` for the `1e-14 kg`, `1 micrometre` reference: a phase-scale gap
   of about `7.09e16`.
3. Cold atoms are closer on preparation, control, classical-gravity
   calibration, and readers, but their ordinary coherent many-body state does
   not receive the rigid center-of-mass `M^2` enhancement. The 2026 atom
   proposal itself finds a current-composite SNR near `1e-7` and requires
   substantial simultaneous advances in atom number, squeezing, geometry,
   and interrogation time.
4. No platform satisfies the full `B0-E` source-to-record gate and the later
   common-packet gravity-arena gate in one demonstrated apparatus. The
   candidate-neutral selection outcome is therefore `NO-SELECTION`, not a
   forced cold-atom or microsolid winner.
5. A complete attempted-run calibration law can establish apparatus
   information only after failures, nuisance degeneracy, and cross-run memory
   are included. It cannot establish in advance that unknown future gravity
   entrants differ; exact agreement remains admissible.

The result also sharpens governance. `B0-L4` can establish a transferable
mechanical baseline at one platform scope. It cannot by itself discharge the
terminal admission condition `P-B0-1` unless that same baseline is
authenticated as the mechanical portion of the frozen common MG0 packet.
That binding occurs at `B0-L5`.

```text
B0 PHYSICS FIGURES OF MERIT:         DERIVED AUTHOR-SIDE
B0 PLATFORM ELIGIBILITY RULE:        DERIVED AUTHOR-SIDE
B0 COMPLETE-RECORD INFORMATION:      DERIVED NECESSARY GATE
NEW 2026 NANOPARTICLE EVIDENCE:      INCORPORATED
B0-E PLATFORM SELECTED:              NO
B0-L4 TRANSFER OBJECT:               ABSENT
B0-L5 COMMON PACKET:                 ABSENT
P-B0-1 DISCHARGED:                   NO
```

---

## 1. Authority and no-answer wall

This file consumes the terminal MG0 benchmark and `P-B0-1`, the B0 readiness
audit, and current primary experimental sources. It is an author-side
selection preflight only.

It does not:

1. create or amend an official pin;
2. select a platform;
3. freeze experimental bytes or a public packet;
4. construct a B0 apparatus model;
5. construct or admit a gravity entrant;
6. treat the Newtonian quantum control as fundamental ontology;
7. infer quantized gravity from entanglement;
8. infer a classical metric from a null;
9. authorize hardware, fitting, simulation, or data analysis; or
10. open chronology, spacetime, QFT, GR, or cosmology.

The quantitative controls below ask whether a platform could host the common
experiment. They do not say what gravity is.

---

## 2. Why total mass is not the source coordinate

The phrase “mass in superposition” hides physically inequivalent states.

### 2.1 Rigid center-of-mass alternative

For a solid object whose entire center of mass occupies two branch
configurations, the branch mass-density difference is collective. In the
point-mass approximation, a two-object Newtonian interaction phase can scale
as `M^2`.

### 2.2 Product/coherent atomic alternative

For `N` atoms each independently occupying two modes, the state is not a
two-branch rigid-body N00N or center-of-mass cat. The 2026 atom-interferometer
analysis obtains a basic signal proportional to

$$
\frac{G M m t}{\hbar d},
\qquad M=Nm,
$$

with metrological enhancement from squeezing, rather than simply replacing
the source by one point mass `M` and claiming `M^2`. The correlation structure
is part of the physical source.

### 2.3 Mechanical-mode alternative

An acoustic or flexural mode can have a large effective mass while its two
branches differ by an extremely small displacement field. Its gravitational
source cannot be inferred from effective mass alone. One must compute the
branch-dependent material density, including clamps and supports.

### 2.4 Beam-delocalized nanoparticle alternative

A freely propagating nanoparticle can exhibit genuine center-of-mass
matter-wave interference while lacking trapping, hold time, reversible
branch control, an independent nearby probe, or a reciprocal geometry. This
earns source-coherence evidence but not the whole benchmark.

Therefore every platform must publish the state-dependent density functional,
many-body state class, support/controller correlations, and record map. A
single scalar “macroscopicity” cannot substitute for them.

---

## 3. Candidate-neutral Newtonian branch functional

For feasibility only, let two registered matter roles have branch densities
`rho_1^a(x,t)` and `rho_2^b(y,t)`. The fixed-background Newtonian interaction
energy control is

$$
U_{ab}(t)
=
-G\int d^3x\,d^3y\,
\frac{\rho_1^a(x,t)\rho_2^b(y,t)}{|x-y|}.
$$

If standard quantum propagation is used as the openly declared control, each
branch receives

$$
\phi_{ab}
=
-\frac1\hbar\int U_{ab}(t)\,dt.
$$

The local-phase-invariant two-body combination is

$$
\Phi_N
=
\phi_{LL}+\phi_{RR}-\phi_{LR}-\phi_{RL}.
$$

Local phases on either matter role cancel from `Phi_N`. This makes it a useful
feasibility coordinate, not a proof of a quantum mediator.

For identical point masses in a symmetric parallel geometry, with same-branch
separation `d`, transverse branch separation `Delta x`, and hold time `T`,

$$
|\Phi_N|
=
\frac{2Gm^2T}{\hbar}
\left(
\frac1d-
\frac1{\sqrt{d^2+(\Delta x)^2}}
\right).
$$

When `Delta x << d`,

$$
|\Phi_N|
\simeq
\frac{Gm^2T(\Delta x)^2}{\hbar d^3}.
$$

The exact extended-density functional, not this approximation, is required in
an official packet. Controllers, shields, supports, and record stores cannot
be omitted when their branch densities differ.

---

## 4. Four quantitative ledgers

No scalar score may compensate for failure of another ledger.

### 4.1 Source-functional ledger

Freeze:

$$
\mathsf S
=
(\rho^a,\text{many-body class},\Delta x(t),T,
\text{overlap},\text{support state}).
$$

The density must descend from the same apparatus model that generates the
preparation. A target branch density supplied by hand earns no source credit.

### 4.2 Coherence ledger

For an independently calibrated off-diagonal witness `C`, define

$$
\Lambda_{\mathrm{obs}}
=
-\log\left|\frac{C_{\mathrm{out}}}{C_{\mathrm{ideal}}}\right|.
$$

The platform must predict the complete distribution of the witness and its
failures. One fitted visibility is not a decoherence law. Shared phase noise
and common-mode subtraction remain inside the joint nuisance parent.

### 4.3 Complete-record information ledger

The earlier unprofiled one-coordinate Fisher sum is not an eligibility test.
It can remain positive even when an admitted phase drift or nuisance response
exactly reproduces the target score. The complete ledger is instead

$$
\mathsf I_{\rm cal}
=
(\mathcal R,\mathcal C,p_0,\Delta_{\rm cal},\mathcal H_\eta,
\{\mathcal D_{\rm sep}^{(N)}\}_{N\le N_{\rm cap}},
I_{\Delta\mid\eta},q,V,N_{\rm cap}),
$$

with the types and exact bounds derived in the companion complete-record
information gate. All null, failure, drift, overwrite, invalid, support, and
reference records remain inside the joint attempted-run law. Cross-run memory
or drift requires the full joint divergence; multiplying one-run information
by `N` is then forbidden.

At B0 scope, `Delta_cal` must be a physically generated, preregistered
candidate-neutral calibration direction: for example the independently
metered fixed classical-gravity control, an injected source/probe phase, or a
registered reader response. It is not a guessed difference between future
gravity laws. The necessary calibration gate is

$$
E_{\rm INFO}^{\rm cal}
=
[\mathsf I_{\rm cal}\ \text{is complete}]
\land
[\mathcal D_{\rm sep}^{(N_{\rm cap})}
 \ge d(1-\beta\Vert\alpha)].
$$

For any first-order calibration claim, the frozen context-score audit must
also satisfy

$$
\operatorname{rank}[H\;g]
>
\operatorname{rank}H,
$$

where `g` is the calibration-response score and `H` contains every admitted
nuisance score across the complete context-record space. If this rank gate
fails, only an independently preregistered higher-order finite-separation test
may recover eligibility; positive unprofiled Fisher information may not.

A balanced physical reversal separates an odd target from an even common
drift. It does not separate a target from an electric, magnetic, Casimir,
support, controller, or reader nuisance with the same odd complete-record
score. The reversal parity and rank ledger must therefore include the
actuator, recoil, reference, timing, and failure records.

Passing this gate proves neither that the bound is sufficient nor that future
entrants differ. Candidate-specific separation is calculated only after at
least two complete laws freeze, using the unchanged public packet and common
calibration evidence while retaining each law's gravity-coupled nuisance
dynamics inside its frozen parent. Exact agreement remains an allowed MG0
result.

### 4.4 Nuisance and mechanics ledger

Push the statistical, nongravitational, and transfer uncertainties through
one frozen estimator into the same phase-equivalent coordinate, including
their covariance. A useful reach coordinate is

$$
\mathcal R_N
=
\frac{|\Phi_N|}
{\sqrt{\sigma_{\rm stat}^2+
       \sigma_{\rm nonG}^2+
       \sigma_{\rm transfer}^2}}.
$$

This is not a discovery statistic and no universal pass threshold is set
here. It prevents raw gravitational phase from being compared with only one
noise term, but it cannot replace `E_INFO^cal`: quadrature addition does not
detect exact nuisance degeneracy, non-Gaussian tails, postselection, or
cross-run memory. Large electromagnetic forces are not fatal if their
held-out uncertainty is sufficiently controlled; small nominal forces are not
safe if their tails or correlations are unknown.

The separate hard mechanics vector is

$$
\mathsf C_{\mathrm{mech}}
=
(\text{preparation},\text{support},\text{work},\text{recoil},
\text{backaction},\text{reader},\text{failure},\text{transfer}).
$$

Every coordinate must close. It is not averaged into `R_N`.

---

## 5. Two noninterchangeable eligibility stages

### 5.1 `E_B0` — baseline eligibility

A platform is eligible for a B0-E attempt only if one named apparatus version
can, from public inputs:

1. generate localized, coherent-phase, and mixture controls from one physical
   preparation family;
2. demonstrate an independent coherence witness;
3. implement or physically type temporary marking, coherent uncomputation,
   stable retention, and failures;
4. prepare and read an independent probe;
5. expose supports, work, recoil, heat, backaction, and boundary fluxes;
6. predict complete records with a common correlated nuisance parent;
7. reproduce a fixed external classical-gravity calibration from independent
   source geometry;
8. pass `E_INFO^cal` for a physically generated candidate-neutral calibration
   direction under a frozen attempted-run cap, including the context-rank gate
   or an independently preregistered higher-order separation certificate; and
9. pass at least one preregistered no-refit transfer.

Different papers may establish component plausibility. They cannot jointly
constitute one `E_B0` apparatus.

### 5.2 `E_MG0` — common-arena compatibility

Discharging the terminal pre-entrant gate requires more than a transferable
method on an unrelated device. The same B0-E object must be authenticated as
the mechanical portion of the frozen common packet. Therefore it must also:

1. realize the exact registered source--probe geometry to be consumed by all
   future entrants;
2. freeze its extended branch density and many-body source semantics;
3. freeze the complete record alphabet, context/reversal schedule,
   candidate-neutral calibration-response family, common nuisance evidence and
   classification ledger, and attempted-run resource cap needed to evaluate
   later PG/CP/ME/DD profiles;
4. expose every candidate-independent classical and nongravitational channel;
5. remain byte-identical when candidate laws are later attached; and
6. permit future entrant agreement, nonidentifiability, or infeasibility
   without changing the apparatus or calibration model.

The conjunction is

$$
\mathsf{Eligible}_{\rm packet}
=
E_{B0}\land E_{MG0}.
$$

`E_B0` success elsewhere is valuable B0-L4 evidence. Only common-packet
binding at B0-L5 can discharge `P-B0-1` for entrant admission.

Neither eligibility stage asserts that unknown future entrants are
distinguishable. B0 certifies one complete calibration-bearing apparatus;
candidate-specific information is a later comparison output, with
gravity-coupled nuisance dynamics kept inside each entrant's parent.

---

## 6. Primary-source update

No source bytes are frozen by this author-side file.

### 6.1 Demonstrated metal-nanoparticle center-of-mass interference

Pedalino *et al.*, [“Probing quantum mechanics with nanoparticle matter-wave
interferometry”](https://doi.org/10.1038/s41586-025-09917-9), report
interference of sodium clusters above `170,000 Da`, more than 7,000 atoms,
with center-of-mass delocalization on a `133 nm` scale. The experiment uses
three photoionizing UV gratings and a mass-selective ion-counting reader. Its
Talbot--Lau state is a multipath near-field state, not automatically the
benchmark's two-branch held source. It reports
dark-count, velocity, mass-distribution, polarizability, alignment,
vibration, gas-scattering, and thermal-radiation obligations, and uses one
global `0.78` scale factor for the compared quantum and classical curves.

This is genuine B0 source/readout evidence. It is not a held nearby pair, a
reversible path-marker/eraser experiment, or a reciprocal gravity apparatus.
At higher reported masses, quantum and classical near-field predictions
converge in the present geometry, so high visibility alone cannot certify the
same quantum witness.

### 6.2 Screened microsolid reference remains prospective

Schut and Mazumdar, [“Parameter scanning in a quantum-gravity-induced
entanglement of masses experiment with electromagnetic
screening”](https://arxiv.org/abs/2502.12474v1), analyze a favorable reference
with masses near `1e-14 kg`, separation near `35 micrometres`, hold time near
`1 s`, micron-scale superposition, and decoherence rates around `1e-3 Hz`.
The paper is a parameter scan, not a demonstration of the source cat or
complete apparatus.

Schut *et al.*, [“Micrometer-size spatial superpositions for the QGEM
protocol via screening and
trapping”](https://doi.org/10.1103/PhysRevResearch.6.013199), derive how
screening and trapping relax spatial requirements while explicitly retaining
shield forces, heavy-apparatus gravitational decoherence, acceleration noise,
blackbody, collision, and spin-control debts. Again, these are physical design
constraints, not a completed platform.

### 6.3 Cold-atom proposal exposes its own composite gap

Howl, Cooper, and Hackermueller,
[“Gravitationally induced entanglement in atom
interferometry”](https://doi.org/10.1103/l62d-gz5c), analyze two parallel
many-atom interferometers. The paper states that combining then-current
best-case values from different experiments yields SNR near `1e-7`. Its
illustrative routes to order-one SNR require combinations such as
`1e12--1e13` atoms, roughly `35--40 dB` squeezing, millimetre separations,
and `1e2--1e3 s` interrogation, or still larger atom numbers and times. It
also leaves the particular physical implementation open.

This is a serious prospective route and an especially good many-body control.
It is not one demonstrated B0-E packet.

### 6.4 Nanodiamond progress is component progress

Recent nanodiamond work has advanced trapping, spin control, neutralization,
rotational modelling, and high-vacuum operation. But a 2026 accepted noise
analysis, Moorthy *et al.*,
[“Random acceleration noise on Stern--Gerlach interferometry in a harmonic
trap”](https://doi.org/10.1103/3jjv-vwmv), still treats a proposed
`1e-15 kg`, `1 nm`, `0.015 s` interferometer and derives demanding
acceleration and tilt-noise constraints. This supports the nuisance gate; it
does not report a closed-loop nanodiamond center-of-mass superposition.

### 6.5 Ontology ceiling remains binding

The above Newtonian quantum controls do not make mediator entanglement an
ontology theorem. The accepted MG0 rule remains class-relative: alternative
matter mechanisms, classical-channel models, nonlinearities, hidden
non-gravitational channels, and reader assumptions must be excluded within
the frozen entrant class before any inference about gravity is made.

---

## 7. Exact calculation receipt

Use

$$
G=6.67430\times10^{-11}\ {\mathrm{m^3\,kg^{-1}\,s^{-2}}},
\qquad
\hbar=1.054571817\times10^{-34}\ {\mathrm{J\,s}}.
$$

For the screened point-mass comparison geometry:

| case | `m` | `Delta x` | `d` | `T` | `abs(Phi_N)` |
|---|---:|---:|---:|---:|---:|
| favorable microsolid reference | `1e-14 kg` | `1e-6 m` | `35e-6 m` | `1 s` | `1.47523e-3` |
| same, four-micrometre branch | `1e-14 kg` | `4e-6 m` | `35e-6 m` | `1 s` | `2.33893e-2` |
| demonstrated `170 kDa` sodium-cluster mass, gifted reference geometry | `2.82292e-22 kg` | `133e-9 m` | `35e-6 m` | `1 s` | `2.08075e-20` |

The sodium line is intentionally **not** a prediction for the published beam
experiment. It gives that demonstrated mass and separation a fictitious
one-second nearby hold, so it is generous by construction. Even then,

$$
\frac{1.47523\times10^{-3}}
     {2.08075\times10^{-20}}
\simeq
7.09\times10^{16}.
$$

The calculation is a reach diagnostic only. Extended densities, actual
trajectories, finite sizes, shields, state class, noise, and readers govern a
real experiment.

---

## 8. Platform dispositions under the conjunctive rule

| platform | strongest demonstrated coordinate | decisive missing `E_B0` coordinate | `E_MG0` status | disposition |
|---|---|---|---|---|
| atom interferometer / BEC | mature coherent control, complementary reads, classical-gravity calibration | one apparatus combining required atom number, squeezing, duration, independent probe, complete nuisance and transfer | prospective many-body signal; source class must remain explicit | no selection |
| sodium metal-cluster beam | genuine `170 kDa`, `133 nm`-scale COM interference and mass-resolved counts | held/two-branch/reversible source, marker/eraser, independent paired probe, work/support ledger, gravity calibration in same apparatus | optimistic phase still negligible | source-control frontier only |
| levitated silica/nanodiamond | COM cooling, spin, trapping, high vacuum, position/rotation component control | demonstrated closed-loop large COM branch generation and recombination with full records | promising mass, severe acceleration/EM/rotation constraints | no selection |
| large molecule beam | demonstrated high-mass interference and environmental decoherence | held paired geometry, reversible branch control, independent probe and gravity sensitivity | far below reciprocal scale | hostile coherence control |
| acoustic mechanical cat | nonclassical mode of large effective mass | branch material-density functional, supports, independent gravity channel | point-COM substitution forbidden | mode control only |
| torsion/mechanical gravity sensor | measured gravity from small classical masses | coherent source family | classical only | calibration control |

No row passes both `E_B0` and `E_MG0`. Component achievements cannot be
multiplied across rows.

---

## 9. Frozen-form selection algorithm for a future pin

A future pin should freeze this order before choosing a platform.

1. **Evidence date and exact source versions.** No later result may be used
   selectively after the winner is known.
2. **Referent test.** Identify the actual coherent degree of freedom and its
   branch density; reject effective-mass substitution.
3. **Single-apparatus test.** Map every B0 preparation, controller, reader,
   nuisance, and failure to one apparatus version; reject component collage.
4. **Demonstration labels.** Mark each edge `DEMONSTRATED`, `SOURCE-FIXED
   MODEL`, `PROPOSED`, or `ABSENT`. A proposal cannot satisfy a demonstrated
   edge.
5. **B0 closure.** Require all `E_B0` gates conjunctively.
6. **Candidate-neutral information.** Require a physically generated
   calibration direction, complete joint attempted-run law, nuisance family,
   error targets, resource cap, and complete context-score rank audit. Reject
   unprofiled Fisher information, postselected counts, i.i.d. scaling under
   cross-run memory, and reversals whose target score remains in the nuisance
   span.
7. **Arena compatibility.** Require the same apparatus and packet to pass
   `E_MG0`; do not swap platforms after B0 review.
8. **No target-conditioned score.** Do not choose using the sign or magnitude
   favored by one gravity entrant. Use the declared Newtonian interaction
   scale, calibration information, and candidate-independent nuisance envelope
   only. Do not promise separation of unknown entrants.
9. **No compensating average.** Extra mass cannot buy a missing reader;
   visibility cannot buy missing recoil; projected SNR cannot buy absent
   source generation.
10. **Permit no selection.** If no row passes, terminate with the frontier and
   keep entrant admission closed.
11. **Freeze before construction.** Only the selected exact apparatus version
    may enter B0-E construction.

This rule currently returns `NO-SELECTION`.

---

## 10. Hostile controls added by this audit

1. Replace branch-density difference by total mass.
2. Apply rigid-COM `M^2` scaling to an independent-atom coherent state.
3. Call effective mechanical-mode mass a displaced source mass.
4. Use metal-cluster beam interference as if it were a held reciprocal pair.
5. Combine best atom number, squeezing, time, and density from different
   apparatuses into one demonstrated device.
6. Count a theoretical noise bound as measured nuisance closure.
7. Use raw force dominance instead of uncertainty after held-out calibration.
8. Omit correlations created by a common laser, shield, trap, or clock.
9. Select cold atoms for mature readers, then silently replace them with a
   microsolid for gravity strength.
10. Select a microsolid for projected phase, then borrow atomic coherence and
    readout performance.
11. Let B0-L4 on an unrelated platform discharge the common-packet gate.
12. Require a positive gravity result to select the apparatus.
13. Let a null select classical gravity without entrant and nuisance scope.
14. Infer a quantum mediator from entanglement without the frozen theory-class
    premises.
15. Treat `NO-SELECTION` as procedural failure and lower a hard gate.
16. Use unprofiled `I_Phi,Phi` when the phase score lies in the nuisance span.
17. Convert detected-event counts into attempted-run reach without the success
    and failure law.
18. Multiply one-run divergence by `N` despite shared drift, memory, or
    adaptive feedback.
19. Call a symbolic sign flip a gravity-isolating reversal when an admitted
    electromagnetic or controller nuisance has the same complete
    context-record score; matching parity alone is a warning, while matching
    score is the exact first-order obstruction.
20. Select an apparatus by a predicted difference between future candidates
    that have not yet been frozen.

---

## 11. Correction to the B0 outcome ladder

The earlier author-side readiness audit said B0-L4 was the minimum level at
which adjudicators might discharge `P-B0-1`. That is incomplete when detached
from the terminal common-experiment requirement.

The relation below is the conservative author-side ladder proposed for a
future B0 pin and review. It does not amend the terminal MG0 adjudication or
award either level:

$$
\begin{aligned}
\text{B0-L4}
&\Longrightarrow
\text{transferable baseline at one platform scope},\\
\text{B0-L5}
&\Longrightarrow
\text{same baseline authenticated inside the common packet},\\
\text{P-B0-1 discharged for entrant admission}
&\Longrightarrow
\text{B0-L5 plus independent terminal review}.
\end{aligned}
$$

A separate B0-L4 artifact is still useful and publishable. It just cannot
prove common-experiment identity until the exact platform, apparatus version,
and public packet are bound.

---

## 12. Maximum legitimate author-side claim

> Current primary evidence now includes genuine center-of-mass matter-wave
> interference of `170 kDa` metal nanoparticles on a `133 nm` delocalization
> scale, correcting any
> blanket claim that nanoparticle COM interference is absent. The physically
> relevant gravity reach nevertheless depends on the full branch-density
> functional and many-body state class, not total or effective mass. Exact
> Newtonian controls show that the demonstrated cluster scale remains many
> orders below a favorable screened microsolid reference, while the 2026
> cold-atom proposal requires several large parameters to coexist in one
> apparatus and does not receive rigid-body `M^2` scaling. No audited platform
> presently closes the conjunctive B0 source-to-record and common-arena gates.
> The only candidate-neutral outcome is no selection; B0-L4 alone does not
> discharge `P-B0-1` until the same baseline is bound and reviewed as the
> mechanical portion of the B0-L5 common public packet.
