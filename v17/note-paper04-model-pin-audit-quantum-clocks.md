# Paper 04 model-pin audit — Seat Q

## Finite quantum clocks, relational instruments, and retained records

Date: 2026-08-23

Status: **FROZEN MUTUALLY BLIND MODEL-PIN AUDIT**

Verdict:

```text
ACCEPT-FOR-ONE-CONSTRUCTION-WITH-BINDING-SCOPE
```

First exact semantic or implementability blocker: **none**

Scientific result awarded: **none**

Model construction or evaluation performed: **no**

## 0. Authentication, authority, and blindness

I authenticated exact committed HEAD
`7aad87a4cc80f239abf4456d72298c306016c5bf` before judgment. The model pin
`v17/note-paper04-two-clock-parent-construction-pin.md` has:

```text
ordinary SHA-256:
8adb5def4c927dd55eba4c2360782b1b6d9370fcf3f5d5c76f5458b1a0fbca4e

normalized self-SHA-256:
29e14feae49cc7a88f1da878623c83fead437d82381fe7ce003f10a877480f85

exact size:
758 LF / 34,071 bytes
```

It ends in one LF and has no trailing horizontal whitespace. I authenticated
and read every Section-0 authority completely:

| Authority | Observed SHA-256 | LF / bytes |
|---|---|---:|
| Paper-04 generic adjudication | `d683901fb1fba9da1b21839839cd955270f1c7c7e2405e7948b7b9b3d0b106b5` | 465 / 19,476 |
| Paper-04 generic pin | `da48bc95bf02c93393697ad6b447605ab89879ff45a1be6896abf6ce6a276b0c` | 1,016 / 45,152 |
| Paper-04 generic Seat M audit | `2151bee5c6ac9b93f315047f2164c995a7fdbc6726a431ebd992814071d0d204` | 837 / 41,302 |
| Paper-04 generic Seat Q audit | `3440dd49b51ae8245070c23963c7a51fc43fe5c02a5c54d4308b4cefd71ec8f2` | 825 / 52,916 |
| Paper-04 generic Seat O audit | `76c2a5d412f56b031ff4e0bbce87a22f9c7ea65a4fe24f62289fbcc12be6defd` | 916 / 59,146 |
| Paper-03 v3.2 terminal adjudication | `b42fcf6201e249f03772ae2f1e037c2c945e98e4221c89a629d744de937e6104` | 502 / 21,215 |
| Paper-03 v3.2 paired candidate | `469ae61c849573c9fe7c70871ca6b60843a080082d07f6850b48213b86d6f7d6` | 1,320 / 56,462 |
| v17 era charter | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | 476 / 21,268 |

The sole unrelated untracked v16 handoff note was not opened, modified,
staged, or used. I did not inspect, infer, contact, or discuss either sibling
model-pin audit or its path. This report is my sole writable path. I did not
construct the model, calculate a registered result, fit the affine map,
evaluate a source probability, or edit any bound artifact or register.

## 1. Verdict and decisive quantum-instrument question

The finite parent is coherent enough for exactly one frozen construction. Its
most dangerous point is also the right physical test: a bare phase PVM is not
a Dirac observable on the constrained parent. The pin does not conceal this.
It explicitly forbids an absolute phase beable and a gauge-trivial classical
record, and makes the covariant record dilation or reduction/lift theorem a
construction gate.

That gate is feasible in principle. For clock B, let a seven-valued record
carry the regular shift

$$
T^{R_B}_g|\beta\rangle=|\beta+2g\rangle.
$$

The recorded Lüders isometry

$$
V_B=\sum_{\beta\in\mathbb F}
E_B(\beta)\otimes|\beta\rangle_{R_B}
$$

obeys the intertwining relation

$$
(U_g\otimes T^{R_B}_g)V_B=V_BU_g.
$$

Thus an invariant input can land in an invariant enlarged clock--record
state, while each reduced branch carries a coordinate-bearing outcome. The
record dephasing is covariant because the group permutes its seven branches.
No invariant physical claim attaches to one bare numeral.

For clock A, the interaction makes the shift conditional on Q charge. A
state-independent seven-label action on the record alone is therefore wrong,
but a complete controlled action exists:

$$
T^{R_A}_g
=\sum_{q\in\mathbb F}|q\rangle\langle q|_Q
 \otimes T_{(1+q)g}^{R_A}.
$$

With this action, the analogous $V_A$ is an intertwiner on the complete
A--Q--record packet, including coherent Q sources. This is precisely why the
full frame lineage and UCOH control are load bearing.

These existence witnesses do not award M4, M5, or M10. The construction must
prove the exact complete arrows, target constraints, memory exposure, and
all-reader identities. They do show that the registered instruments are not
impossible merely because their clock-coordinate outcomes are gauge
covariant.

The first suspected counterexample therefore becomes a binding fork rather
than a kill:

```text
compress the bare PVM to H_phys or use a gauge-trivial record
  -> M4 fails immediately;

construct the complete covariant record dilation/reduction-lift packet
  -> instrument feasibility remains open for the one construction.
```

The pin has frozen the latter requirement and permits failure to print. Hence
the required verdict is acceptance for one construction with the scopes in
Section 3.

## 2. Independent feasibility reconstruction

### 2.1 Constraint, phase covariance, and the physical subspace

The printed diagonal phases define a representation because
$D\in\mathbb Z_7$ and

$$
\omega^{gD}\omega^{hD}=\omega^{(g+h)D}.
$$

Finite group averaging is consequently an orthogonal projector. Every
triple $(k_A,k_M,k_Q)$ fixes a unique $k_B$ because two is invertible in
$\mathbb Z_7$. This makes the claimed physical dimension and the B reduction
algebraically feasible without a distributional rigging ambiguity.

The same observation exposes the bare-clock trap. On the physical subspace,
the other three charges fix one B charge, so

$$
P_{\rm phys}E_B(\beta)P_{\rm phys}
=\frac17P_{\rm phys}.
$$

On a fixed good Q sector the corresponding statement holds for A. Therefore
compression of a kinematic phase effect is not a physical clock instrument:
it is uniform and loses the conditional state information. Likewise,
$E_B(\beta)\rho E_B(\beta)$ alone does not remain in
$\mathcal H_{\rm phys}$. The complete covariant record or relational lift is
not optional notation; it is the first construction theorem.

### 2.2 Source family and phase-reference status

Each declared source is a normalized projection of a fixed kinematic seed.
At pin level none is forced to be zero: each seed has support on at least one
solution of $D=0$, and in fact the linear B charge permits support in every
registered fixed-charge sector. Construction must prove positivity and print
the source-dependent normalization rather than call the projection a
postselected laboratory success.

The phase labels in the seeds do not by themselves introduce an external
phase beable after projection. Their physical content is in relative phase
correlations. UAO and UBO are valid independence controls only if the
projected sources remain operationally distinguishable by complete
relational readers. A preparation device that simply writes their absolute
kinematic phase from an external oscillator would instead fail M3/M16 and
must appear as the hidden-reference mutant.

### 2.3 B and A reductions

For fixed $(k_A,k_M,k_Q)$ there is one physical $k_B$. The factor
$\sqrt7\,{}_B\langle\beta|$ removes the Fourier coefficient of magnitude
$1/\sqrt7$ and leaves only a phase. Hence a unitary B-coordinate reduction
onto the printed $A\otimes M\otimes Q$ target is feasible.

For $q\ne6$, $1+q$ is invertible, so fixed $(k_B,k_M,q)$ determines one
$k_A$ and the same Fourier argument makes the A reduction feasible on the
printed direct sum. At $q=6$, the constraint no longer contains $k_A$;
phase evaluation cannot be the same unitary coordinate map. The pin correctly
keeps that rank-loss/stoppage sector rather than defining a pseudoinverse.

These are coordinate maps, not clock-readout instruments. State, observable,
record, instrument, posterior, and guard transport must separately descend
through them.

### 2.4 Complete physical instruments without an external phase standard

A covariant recorded PVM can exist without a gauge-trivial phase standard
because the pointer transforms and the full system--pointer state is
invariant. The construction must nevertheless satisfy four noncompensatory
conditions:

1. every outcome branch is the pinned Lüders branch in the named reduced
   frame;
2. the complete direct-sum arrow retains the coordinate record and its group
   action;
3. the target boundary contains all apparatus memory needed by later guards;
   and
4. every operational reader is relational or is explicitly confined to the
   externally referenced laboratory comparator.

A gauge-trivial record of $\beta$ would be an exact hidden phase reference.
Conversely, merely declaring that the record transforms is insufficient: the
instrument must intertwine the source and target gauge actions and remain
complete in the Paper-03 sense.

For A on UCOH, the record transformation is Q-controlled. Measuring Q to
choose a classical A-clock rate would destroy the frozen coherence. The
controlled action must remain coherent in the complete packet. A scalar
seven-cycle permutation independent of Q cannot certify UCOH.

### 2.5 Sequential and adaptive law

The USEQ sequence is a genuine discriminator because it retains the first M
result, uses it in a later guard, performs a second readout, and compares the
complete joint law and posterior. The supplied path order remains comparator
input; Paper 04 does not derive it.

The absolute-looking predicates $\beta=2$, $\beta=6$, and the printed parity
partition are allowed only as coordinates of the B-relative operational
context. The entire clock record, M record, parity guard, operation, and
later reader must be lifted together. If the construction applies the parity
rule to a gauge-trivial M numeral, or transforms record labels without the
guard partition, it has imported an external phase origin.

There are two conceptually different Page--Wootters measurement routes in
the primary literature: invariant/twirled operators and a dynamical purified
measurement in the constraint. They can differ for nonideal clocks. The
present discrete orthogonal clock makes an exact relational route feasible,
but construction may not choose whichever route yields the desired answer.
It must use one frozen complete arrow realizing the pinned Lüders packet and
show any alternative is all-reader equivalent. If no such equivalence is
proved, M10 fails rather than being repaired.

### 2.6 Coherent source and full temporal-frame transport

UCOH prevents a sector-by-sector classical mixture from masquerading as a
quantum frame transformation. The A rate is correlated coherently with Q,
so the full map must transport Q coherence, A/B records, M/Q observables,
posteriors, guard memory, and all later readers. Dephasing Q before applying
$\mathcal S_{A\leftarrow B}$ changes the source and fails X6.

The scalar-sufficiency fork is correctly result neutral. A reading-only
kernel may work on diagonal fixed-q sources and fail on UCOH. That failure is
information loss or clock-choice dependence, not a reason to classicalize
the source.

### 2.7 Resources, recurrence, and stoppage

All four microscopic factors and all clock outcome alphabets are finite.
The model therefore avoids an unprinted infinite-energy clock but does not
make readout free. Construction must include:

- the charge means and variances for every source;
- charge support and the declared six-unit bandwidth convention;
- every seven-valued clock and matter record;
- guard memory and controller operation;
- the minimal dilation/environment dimensions or an operationally equivalent
  complete instrument resource;
- preparation and projection/group-averaging lineage;
- recurrence at seven gauge steps; and
- the Q=6 failure probability and domain wherever A is used.

Calling modular charge a positive energy or treating the group parameter as
elapsed microscopic time would exceed the pin.

### 2.8 Reciprocal response

The bilinear term is capable in principle of producing both response
directions: it makes the A phase action depend on Q charge and the Q phase
action depend on A charge. This is only structural feasibility. M19 still
requires nonzero differences in the exact frozen A and Q reader laws under
U0/U1 and UA0/UA1, and the deletion mutant must alter or remove them without
retuning. A phase in an unobserved amplitude or a difference visible only in
a newly chosen reader cannot pass.

## 3. Binding scope for the sole construction

The following conditions are mandatory readings of the frozen model. They
do not award an outcome or change a coefficient.

1. **Covariant recorded instrument.** Never compress a bare phase PVM and
   call the result physical. Construct one complete gauge-covariant recorded
   Lüders arrow or a reduction/lift arrow proved equivalent on every reader.
2. **Nontrivial record action.** B and M records carry their induced shifts;
   A and Q records carry the appropriate complete controlled shifts. A
   gauge-trivial numerical record is the hidden-reference mutant.
3. **No instrument-route selection after results.** Twirled, reduced/lifted,
   and purified measurement realizations are interchangeable only after an
   exact all-reader theorem. Otherwise the one route fixed before evaluation
   is the model and the others are different models.
4. **Whole-context covariance.** A coordinate change transports outcome
   labels, record actions, guard partitions, operations, source lineage,
   probabilities, and later readers. Transforming only $\beta$ or $r$ fails.
5. **Coherent A-clock transport.** UCOH remains coherent. The Q-controlled
   A-record action and frame map may not be replaced by fixed-q classical
   conditioning.
6. **Complete apparatus memory.** Minimal dilation environments may be
   quotiented only after complete future equivalence. Every guard-readable
   or later-reader-readable memory remains in the Paper-03 boundary.
7. **Clock outcome versus clock coordinate.** The parent prediction is a
   complete law over clock records and correlations. A reduction parameter
   may label a coordinate chart; it may not be substituted for a sampled
   record or an autonomous trigger.
8. **Physical controller.** The USEQ guard consumes the retained relational
   M record. Program position, comparator $s$, or a gauge-trivial phase table
   cannot activate it.
9. **Sequential disturbance.** Both clock and matter Lüders disturbances
   propagate through the second opportunity. Reusing the undisturbed orbit
   state after the first readout changes the process.
10. **Source preparation lineage.** Projected source states are legitimate
    declared parent states; any operational claim about preparing them must
    print the projection/group-averaging mechanism and cannot use an external
    phase oscillator invisibly.
11. **Good-sector domain.** Every A-frame statement is restricted to
    $Q\ne6$ including coherent support. USTOP is never assigned a global A
    inverse or deleted.
12. **Full quantum frame map.** State, observable, instrument, record,
    posterior, memory, source, and reader transport are all required. A
    scalar reading kernel is an additional theorem, not the map definition.
13. **Finite resources.** Record, environment, controller, preparation,
    charge/coherence, recurrence, and failure resources appear at the exact
    theorem level used.
14. **Operational reciprocal response.** Both frozen arms and the exact
    interaction-deletion mutant must be separated by the predeclared readers.
15. **No reference-by-calibration.** Laboratory $s$ and an external phase
    standard may train the comparator only. They cannot enter the physical
    source, record action, lift, controller, or held-out predictor.
16. **No causal promotion.** The supplied path order may type the two
    opportunities; neither the gauge orbit nor increasing clock labels
    derives an arrow.

## 4. Model targets M1--M24

`FEASIBLE` means the frozen object admits a coherent theorem attempt. It does
not mean that the theorem was evaluated or awarded.

| Target | Model-pin audit | Seat-Q disposition |
|---|---|---|
| M1 | AUTHENTICATED | Exact HEAD, pin, authority hashes, counts, and whitespace pass. |
| M2 | FEASIBLE | Finite diagonal character law supports an exact representation/projector proof. |
| M3 | FEASIBLE WITH PROOF GATE | Every source has potential physical support; positivity and normalization remain to be proved. |
| M4 | FEASIBLE WITH BINDING SCOPE | Requires the covariant complete recorded instruments of Section 3; bare compression fails. |
| M5 | FEASIBLE WITH BINDING SCOPE | One finite joint law must include transforming records, all sources, controllers, and complete contexts. |
| M6 | FEASIBLE / FORMAL CONTROL | The orbit comparator is frozen from the same U; no parent retuning is allowed. |
| M7 | FEASIBLE | The unique B charge makes a global B coordinate reduction possible; complete semantics remain open. |
| M8 | FEASIBLE | A reduction is possible on Q-not-6; Q=6 is an explicit rank-loss/stoppage test. |
| M9 | OPEN OUTCOME | Parent-relative held-out M laws must be derived from each valid clock. |
| M10 | FEASIBLE WITH BINDING SCOPE | Use one complete relational measurement route, retained records, disturbance, and physical guard. |
| M11 | NONVACUOUS OPEN TEST | Two fit points and two distinct held-out points overidentify the affine relation. |
| M12 | FEASIBLE ON COMMON DOMAIN | Full A/B map only on Q-not-6 and with complete record transport. |
| M13 | HONEST FORK | Scalar sufficiency may pass or exact information loss must print, especially for UCOH. |
| M14 | FEASIBLE QUANTIFIER | Every registered common-sector source and complete context must round-trip; one-state equality is insufficient. |
| M15 | FEASIBLE | Both fixed nonidentity maps are Borel bijections on the declared finite windows; push forward the whole interface. |
| M16 | FEASIBLE PROMOTION GATE | Dependency graph must include source projection, record actions, controllers, lift maps, and model bytes. |
| M17 | FEASIBLE BUT MARGINAL-TRIVIALITY CONTROL | Uniform bare clock marginals cannot separate NO-CLOCK; time-sensitive complete correlations must do so. |
| M18 | FEASIBLE WITH EXPANDED LEDGER | Four finite factors are fixed; apparatus/record/controller resources must also print. |
| M19 | STRUCTURALLY FEASIBLE / OUTCOME OPEN | The bilinear generator can affect both named phases; exact reader response remains untested. |
| M20 | OPEN RESULT | U0/U1/UCOH dependence must print without sector dephasing or retuning. |
| M21 | FEASIBLE AS FOUR CASE ATTEMPTS | Each complete boundary must be instantiated; unavailable cases print unconstructed rather than asserted. |
| M22 | WELL-POSED CLASSIFICATION | Independent pre-fit, formal-only, or failed remain distinct. |
| M23 | REQUIRED | All 28 generic coordinates plus the model coordinates must print noncompensatorily. |
| M24 | BINDING | Ontology, supplied order, spacetime, gravity, fundamental time, and actuality stay closed. |

No target is pre-awarded. The earliest possible construction failure is M4
if the complete covariant clock packet cannot be realized from the frozen
instrument.

## 5. Generic hostile attacks 1--68

Each attack changes a distinct object. `REFUSE` means the mutant cannot earn
the affected positive coordinate; an allowed negative branch remains part of
the scientific output.

| # | First model coordinate | Seat-Q disposition |
|---:|---|---|
| 1 | M4/M16 | Causal-slot rank has no phase instrument or subsystem; refuse. |
| 2 | M4/M16 | Path length is supplied metadata, not a clock record; refuse. |
| 3 | M16 | Source-code order is detected by presentation permutation. |
| 4 | M16 | Run counter is hidden schedule unless physically represented and resourced. |
| 5 | M15/M16 | Pure serialization change leaves every physical packet prediction invariant. |
| 6 | M4/M5 | Renaming A supplies no B subsystem or instrument. |
| 7 | M4/M5 | Copying A record produces a channel, not clock B. |
| 8 | M4/M11 | Affine postprocessing of A remains one clock. |
| 9 | M11 | Joint held-out calibration is leakage; refuse. |
| 10 | M11/M18 | Post-result window selection is semantic retuning. |
| 11 | M20 | Outcome-selected clock is postselection. |
| 12 | M10/M16 | Future outcome in clock definition violates source lineage. |
| 13 | M5 | Zero-support clock branch has no normalized posterior. |
| 14 | M5 | Convenient diffuse null posterior is not relevant in this finite model and earns no physics. |
| 15 | M5 | Null-version change cannot alter integrated predictions; finite packet remains exact. |
| 16 | M10 | Dropping r1 before the guard makes the adaptive arrow untyped. |
| 17 | M4/M5/M10 | Hidden apparatus memory fails Paper-03 completeness. |
| 18 | M10 | One-time marginals cannot earn the USEQ joint-law target. |
| 19 | M10 | Deleting Lüders backaction substitutes a different instrument. |
| 20 | M10/M21 | Equal current reading does not license Markovization. |
| 21 | M5/M12 | Separate parent states destroy the common experiment. |
| 22 | M5/M12 | Separate system laws destroy the common parent. |
| 23 | M22 | Constraint appended after target inspection is formal only. |
| 24 | M4/M20/M22 | Target-adapted factorization is not an independently physical clock. |
| 25 | M12/M20 | Clock-indexed law change is dependence, not gauge. |
| 26 | M2/M3 | Kinematic norm cannot replace the finite physical inner product. |
| 27 | M2/M7/M8 | Page--Wootters without the physical solution/reductions is unconstructed. |
| 28 | M10 | One-time PW conditioning cannot pass sequential adequacy. |
| 29 | M7/M8/M12 | Trinity invoked beyond the exact constraint/sector/instrument hypotheses is refused. |
| 30 | M4 | The declared finite phase PVM is used; no incompatible ideal time operator may be inserted. |
| 31 | M18 | Infinite ideal clock cannot prove the finite model result. |
| 32 | M18 | Seven-state clocks have recurrence; unlimited runtime is refused. |
| 33 | M18 | Ignoring the seven-step wrap invalidates the domain. |
| 34 | M16/M18 | Path-derived winding is hidden time. |
| 35 | M18/M20 | Reusing a phase across cycles requires extra physical memory or prints ambiguity. |
| 36 | M8/M18 | Q=6 ends A-clock adequacy; it does not freeze M/Q/B. |
| 37 | M15 | Noninjective reading map is coarse-graining, not gauge. |
| 38 | M15/M24 | Orientation reversal does not derive physical time reversal. |
| 39 | M15 | Label-only transformation fails complete covariance. |
| 40 | M15 | POVM-only transformation without records/calibration/readers fails. |
| 41 | M11/M24 | The affine test is restricted to the supplied same path. |
| 42 | M11/M24 | Proper-time differences cannot be fit away. |
| 43 | M24 | Increasing clock values do not derive causal order. |
| 44 | M24 | Source/target syntax does not derive time orientation. |
| 45 | M24 | One local material clock does not create a global time. |
| 46 | M24 | A KMS state does not select a law-level foliation. |
| 47 | M19 | Interaction deletion is the frozen mutant and must change the response if M19 passes. |
| 48 | M19 | Removing only system-to-clock response fails reciprocity. |
| 49 | M4/M10/M18 | Deleting readout disturbance changes the complete instrument. |
| 50 | M19/M22 | Retuning the system law to hide disturbance changes the model. |
| 51 | M18 | Omitted charge, record, or apparatus cost fails the ledger. |
| 52 | M5 | Entangled/constrained clocks may not be force-factorized. |
| 53 | M12/M14 | Dephasing UCOH in a frame change changes the source. |
| 54 | M12/M14 | A lossy map is not invertible; exact loss must print. |
| 55 | M14 | One-state round trip cannot certify the complete context family. |
| 56 | M13/M14/M20 | Incomplete readers cannot certify clock equivalence. |
| 57 | M16/M22 | Renaming comparator s or a Barandes target index leaves external time. |
| 58 | M21 | Readable record need not be a complete division. |
| 59 | M21 | Complete reset/division need not make a tick. |
| 60 | M10/M21 | Factorization at every clock reading violates indivisible-history scope. |
| 61 | M22/M24 | One constrained representation does not select ontology. |
| 62 | M24 | Affine clock agreement is not a metric. |
| 63 | M24 | Clock order is not derived operational chronology. |
| 64 | M24 | Imported GR dilation is comparator input, not gravity. |
| 65 | M22 | Target-wrapped history state is formal parametrization only. |
| 66 | M16/M22 | Schedule encoded in source/controller/model bytes fails lineage. |
| 67 | M22 | Parent selected after held-out inspection is not pre-fit. |
| 68 | M24 | Parameter-free notation cannot select fundamental timelessness. |

All 68 attacks have an exact model-level disposition. The physical-object
mutants, not source-code mutation names, must be executed in construction.

## 6. Model-specific controls X1--X24

| ID | Seat-Q disposition |
|---|---|
| X1 | A larger post-result prime changes clocks, sources, recurrence, and records; refuse. |
| X2 | Changing the B coefficient changes calibration and the parent; refuse. |
| X3 | Exact interaction-deletion mutant is required; both response arms must alter if positive. |
| X4 | A scalar interaction gives only a global phase and cannot pass M19. |
| X5 | USTOP is a registered source; deleting it censors the A-clock domain failure. |
| X6 | Classicalizing UCOH changes coherent source and controlled A-record covariance. |
| X7 | U0 alone cannot test reciprocity, clock choice, or coherent frame transport. |
| X8 | Identifying A/B records collapses two subsystem lineages into one. |
| X9 | Copying A into B is a retained record channel, not independent B dynamics. |
| X10 | Fitting all four points destroys the two held-out tests. |
| X11 | Dropping either held-out point weakens the frozen overidentification. |
| X12 | Positive post-result tolerance changes the exact theory; refuse. |
| X13 | Replacing B by s should fit superficially and fail M16. |
| X14 | A controller lookup table containing U_s is hidden model-time data. |
| X15 | Program-position USEQ trigger fails the physical-record controller gate. |
| X16 | Dropping r1 makes the parity guard physically unavailable. |
| X17 | POVM effects alone omit disturbance and posterior; sequential law changes. |
| X18 | Q=6 has a registered positive source and cannot be called null by convenience. |
| X19 | Winding count enlarges the model after freeze and imports hidden history. |
| X20 | Identity-only pushforward leaves M15 unconstructed. |
| X21 | Label-only pushforward fails record, guard, measure, and reader covariance. |
| X22 | Increasing U0 readings cannot derive the supplied causal arrow. |
| X23 | Modular charge has no proved positive-energy interpretation. |
| X24 | Finite conditional success cannot select timeless ontology or gravity. |

## 7. Fresh Seat-Q countermodels FQ1--FQ18

### FQ1 — physical compression makes the clock trivial

Compress $E_B(\beta)$ directly with $P_{\rm phys}$. The effect is
$P_{\rm phys}/7$ for every $\beta$. A uniform bare outcome has lost the
relational conditional state and cannot be the promised physical clock
packet. **Required:** use the complete covariant record/lift construction;
otherwise M4 is the first failure.

### FQ2 — gauge-trivial phase record

Apply the kinematic Lüders PVM and copy $\beta$ into a classical register on
which the gauge group acts trivially. The numeral now fixes an absolute phase
origin. **Required:** detect as hidden reference at M4/M16.

### FQ3 — wrong fixed action for the interacting A record

Let the A record shift as $\alpha\mapsto\alpha+g$ for every Q state. In the
$q=1$ component the clock actually shifts by $2g$, and on UCOH the mismatch
is coherent. **Required:** use the Q-controlled record action or fail
M4/M12.

### FQ4 — measure Q to choose the A clock rate

Dephase UCOH in Q charge, apply a sectorwise A-record permutation, and forget
the Q result. The scalar clock looks covariant but a later interference
reader distinguishes it. **Required:** preserve coherent controlled transport;
X6 fires.

### FQ5 — covariant POVM without covariant instrument

Transport the phase effects correctly but reset A or B after each readout
instead of applying the pinned Lüders update. One-time clock statistics agree;
the second USEQ opportunity and later readers differ. **Required:** M4/M10
bind one complete instrument.

### FQ6 — absolute parity guard

Retain a covariant M record but keep the subset `{0,2,4,6}` fixed while
changing clock origin. The record transforms and the controller does not, so
the complete context is not gauge covariant. **Required:** lift or push
forward the guard partition with the frame; M10/M15 otherwise fail.

### FQ7 — undisturbed reuse of the orbit state

After the first clock and M readouts, compute the second outcome from the
original $U_s|\phi\rangle$ as if no measurement occurred. One-time tables can
still match while the complete posterior and adaptive joint law differ.
**Required:** propagate both Lüders disturbances through M10.

### FQ8 — reduction parameter used as a trigger

Call $\mathcal R_B(2)$ because program position says “first” and
$\mathcal R_B(6)$ because it says “second,” with no retained B record or
physical controller. The symbols are chart parameters, not clock outcomes.
**Required:** the predictor consumes physical records and a licensed context,
or M10/M16 fail.

### FQ9 — external oscillator prepares every phase seed

Prepare U0--UBO by an unrepresented laboratory phase oscillator, then project
the displayed system and omit the oscillator. The resulting density operators
are valid formulas but source lineage consumes an external reference.
**Required:** treat projected sources as declared parent states or represent
the preparation reference and its resources; no hidden physical-preparation
claim.

### FQ10 — pseudoinverse through Q=6

Use a Moore--Penrose inverse of $\mathcal R_A$ on USTOP and call the output an
A-frame state. Distinct physical A data collapse to one reduced vector.
**Required:** print stoppage/rank loss; M8/M18 reject the inverse.

### FQ11 — scalar A/B kernel on the coherent source

Replace UCOH by the convex mixture of q=0 and q=1 when calculating a
reading-only frame kernel. All charge-diagonal readers can agree while a
coherent Q reader fails. **Required:** M13 prints scalar insufficiency and
retains the quantum map.

### FQ12 — omitted apparatus representation

Write the seven-valued outcome but give neither the record's gauge action nor
the dilation target constraint. The branch labels cannot be transported and
future guards have no typed physical input. **Required:** M4/M5 fail rather
than letting code choose the representation.

### FQ13 — uniform-marginal false clock

The physical B phase marginal and the NO-CLOCK record can both be uniform.
Comparing only those marginals makes the baseline indistinguishable.
**Required:** M17 must separate through the frozen time-sensitive complete M
correlations and sequential context.

### FQ14 — response only in an unregistered phase

Deleting $k_Ak_Q$ changes a global or off-diagonal phase, while all frozen A
or Q phase-reader probabilities remain equal. Operator difference alone
cannot earn reciprocity. **Required:** M19 prints failure unless the exact
registered complete readers separate both arms.

### FQ15 — controller memory outside the physical parent

The parity bit is computed correctly and stored in an external latch omitted
from the boundary. Later action depends on it. **Required:** expose the latch,
record dimension, and gauge/frame lineage; otherwise M5/M10 fail.

### FQ16 — schedule hidden in a phase-origin table

The held-out interface takes only B records, but a controller contains the
calibrated table $\beta\leftrightarrow s$ and uses the s entry to select the
operation. **Required:** the hidden-controller mutant must fail M16 even when
all ordinary probabilities match.

### FQ17 — source-dependent readout success

A dilation implements the phase PVM only after a source-dependent herald and
discards failures. Conditional record laws can look exact while the complete
instrument is not trace preserving. **Required:** retain every herald/failure
outcome and preparation/readout cost in M4/M18.

### FQ18 — two physically different relational measurement routes

One construction uses a twirled invariant operation; another modifies the
constraint with a clock-triggered measurement interaction. If their complete
posteriors or sequential readers differ, they are different models even when
one-time probabilities agree. **Required:** freeze one realization before
evaluation and prove any claimed equivalence on all readers. The primary
comparison is Hausmann, Schmidhuber, and Castro-Ruiz,
[*Measurement events relative to temporal quantum reference frames*](https://arxiv.org/abs/2308.10967).

These countermodels are semantic and model-level. FQ1--FQ4 test whether a
clock-coordinate record can be physical without an external reference;
FQ5--FQ8 test complete sequential semantics; FQ9--FQ12 test source, sector,
and dilation typing; FQ13--FQ18 test nonvacuity, reciprocity, hidden schedule,
and measurement-route nonselection.

## 8. Full product and ceiling

No scientific construction coordinate is awarded by this audit.

### 8.1 Generic 28-coordinate product

```text
1  P04-UPSTREAM-P03V32-PRESERVED:
   AUTHENTICATED AND BOUND; CONSTRUCTION MUST PRESERVE
2  P04-CLOCK-A-PHYSICAL-PACKET-CONSTRUCTED:
   OPEN; COVARIANT COMPLETE RECORD BINDING
3  P04-CLOCK-B-PHYSICAL-PACKET-CONSTRUCTED:
   OPEN; COVARIANT COMPLETE RECORD BINDING
4  P04-TWO-CLOCK-JOINT-LAW-CONSTRUCTED:
   OPEN
5  P04-FINITE-CLOCK-CONDITIONING-CONSTRUCTED:
   WELL-TYPED POSITIVE-SUPPORT TARGET; OPEN
6  P04-DIFFUSE-CLOCK-CONDITIONING-AE-CONSTRUCTED:
   NOT NEEDED FOR FINITE MODEL; UPSTREAM A.E. SCOPE PRESERVED
7  P04-ORDINARY-CLOCK-RELATIVE-ADEQUACY:
   OPEN
8  P04-SEQUENTIAL-ADAPTIVE-CLOCK-ADEQUACY:
   OPEN; COMPLETE INSTRUMENT/RECORD/GUARD BINDING
9  P04-SAME-PATH-AFFINE-AGREEMENT:
   OPEN; TWO HELD-OUT POINTS FROZEN
10 P04-CLOCK-FRAME-TRANSFORMATION-CONSTRUCTED:
   OPEN; FULL QUANTUM MAP REQUIRED
11 P04-CLOCK-ROUNDTRIP-EQUIVALENT:
   OPEN ON COMMON Q-NOT-6 DOMAIN; LOSS MUST PRINT
12 P04-CLOCK-NEUTRAL-PARENT-CONSTRUCTED:
   OPEN
13 P04-LABORATORY-REDUCTION-FROM-PARENT-CONSTRUCTED:
   OPEN
14 P04-PAGE-WOOTTERS-TRINITY-COMPARATOR:
   OPEN AT EXACT FINITE CONSTRAINT/INSTRUMENT HYPOTHESES
15 P04-POSITIVE-STOCHASTIC-PARENT:
   NOT APPLICABLE TO THIS SELECTED ROUTE; UPSTREAM OPTION PRESERVED
16 P04-REPARAMETRIZATION-COVARIANCE-CONSTRUCTED:
   OPEN; WHOLE-CONTEXT PUSHFORWARD REQUIRED
17 P04-HIDDEN-EXTERNAL-TIME-EXCLUDED:
   OPEN; RECORD/CONTROLLER/SOURCE LINEAGE REQUIRED
18 P04-FINITE-CLOCK-LIMITS-CONSTRUCTED:
   OPEN
19 P04-CLOCK-BACKREACTION-CONSTRUCTED:
   OPEN; BOTH OPERATIONAL ARMS REQUIRED
20 P04-STOPPED-RECURRENT-CLOCKS-CLASSIFIED:
   OPEN
21 P04-CLOCK-CHOICE-INDEPENDENT-DYNAMICS:
   OPEN; DEPENDENT DYNAMICS IS ADMISSIBLE
22 P04-EXTERNAL-PARAMETER-OPERATIONALLY-REDUNDANT:
   OPEN; FORMAL-ONLY/NOT-REDUNDANT BRANCHES RETAINED
23 P04-CAUSAL-ORDER-STILL-SUPPLIED:
   BINDING
24 P04-ONTOLOGY-SELECTION-UNCONSTRUCTED:
   BINDING
25 P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED:
   BINDING
26 P04-GRAVITY-UNCONSTRUCTED:
   BINDING
27 P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED:
   BINDING
28 P04-ACTUALIZATION-UNCONSTRUCTED:
   BINDING
```

### 8.2 Model-selection coordinates

```text
P04M-MODEL-PIN-AUTHENTIC:
  AUTHENTICATED
P04M-FINITE-GROUP-PARENT-CONSTRUCTED:
  FEASIBLE TARGET; UNCONSTRUCTED
P04M-PHYSICAL-SOURCE-FAMILY-NONEMPTY:
  FEASIBLE TARGET; UNPROVED
P04M-B-REDUCTION-GLOBAL:
  FEASIBLE TARGET; UNPROVED
P04M-A-REDUCTION-Q-NOT-6:
  FEASIBLE TARGET; UNPROVED
P04M-A-STOPPED-Q-6:
  FEASIBLE CONTROL; UNCLASSIFIED
P04M-COMPLETE-RELATIONAL-INSTRUMENTS-CONSTRUCTED:
  FEASIBLE WITH BINDING SCOPE; UNCONSTRUCTED
P04M-HELDOUT-SEQUENTIAL-LAW-REPRODUCED:
  OPEN
P04M-FULL-QUANTUM-FRAME-MAP-CONSTRUCTED:
  OPEN
P04M-READING-ONLY-SUFFICIENCY-PASS-OR-FAIL:
  HONEST OPEN FORK
P04M-RECIPROCAL-INTERACTION-PASS-OR-FAIL:
  HONEST OPEN FORK
P04M-MULTIPLE-CHOICE-PASS-OR-DEPENDENT:
  HONEST OPEN FORK
P04M-HIDDEN-TIME-EXCLUDED-OR-DETECTED:
  HONEST OPEN FORK
P04M-FORMAL-ONLY-OR-OPERATIONAL-REDUNDANCY:
  HONEST OPEN CLASSIFICATION
```

The earliest rung remains controlled by the first construction failure. In
particular, a failure to construct the covariant complete clock instrument
halts at `P04-PHYSICAL-CLOCK-UNCONSTRUCTED`; exact algebraic reductions cannot
compensate.

The maximum possible result is one bounded, conditional theorem that this
frozen seven-state constrained parent reproduces the registered complete
predictions without consuming comparator s in its held-out interface. Even
that would not select the parent, make the gauge group time, derive the
supplied path order, establish a global clock, or construct spacetime or
gravity.

## 9. Primary-source scope

The model pin uses the primary literature conservatively.

1. Page--Wootters supports stationary-parent conditional dynamics, not the
   complete recorded measurement packet or unique clock factorization.
2. Höhn--Smith--Lock supports relational observables, physical-inner-product
   reduction maps, and temporal-frame changes at exact clock/constraint
   hypotheses. A kinematic phase PVM is covariant clock data; its physical
   content comes through the relational observable/reduction, not bare
   compression.
3. Höhn--Krumm--Müller,
   [*Internal quantum reference frames for finite Abelian groups*](https://arxiv.org/abs/2107.07545),
   supports finite group averaging, physical Hilbert spaces, relational
   observables, and internal-frame reductions. It also distinguishes the
   perspective-neutral physical algebra from observables requiring an
   external frame; it does not pre-award a retained clock instrument.
4. Smith--Ahmadi supports interaction-induced clock dependence and temporal
   nonlocality, not deletion of the bilinear interaction or a scalar clock
   map on coherent sectors.
5. Finite-clock resource papers support explicit dimension, energy,
   coherence, runtime, disturbance, and backreaction accounting. They do not
   make a seven-state clock costless.
6. Quantum-reference-frame covariance requires transport of states,
   observables, measurements, and dynamics. It does not license a scalar
   record relabel.
7. Periodic-clock work supports the seven-step local window and refusal of a
   free winding counter.
8. Hausmann--Schmidhuber--Castro-Ruiz shows why physical measurement relative
   to a finite temporal frame needs a specific operational realization:
   invariant/twirled and dynamically purified measurement routes can be
   physically distinct away from their common ideal regime. It strengthens
   binding scope 3 rather than selecting a route for this pin.
9. Barandes keeps a target/conditioning time index in the published
   indivisible law. Renaming that index or the present reduction parameter a
   clock record would not eliminate external time.

No source selects $p=7$, the polynomial, the source family, a fundamental
clock, a timeless ontology, an actual history, chronology, spacetime, or
gravity.

## 10. Final verdict and halt boundary

The model is not rejected merely because bare clock phase is gauge covariant.
A complete transforming record provides an in-principle relational
instrument, while the pin explicitly refuses the hidden absolute record. The
finite constraint and reduction domains are also internally coherent.

The sole construction must stop without repair if it cannot prove the exact
covariant record/lift arrows, if UCOH forces sector dephasing, if the USEQ
guard consumes a gauge-trivial numeral or program position, if apparatus
memory escapes the boundary, or if the reciprocal response is invisible to
the frozen readers. Those are scientific negative outcomes, not Python
defects.

Final verdict:

```text
ACCEPT-FOR-ONE-CONSTRUCTION-WITH-BINDING-SCOPE
```

First exact semantic or implementability blocker:

```text
none
```

No model theorem, fit, response, clock adequacy result, external-time result,
or downstream claim is awarded by this audit.

## 11. Freeze authentication

Immediately before freeze I reauthenticated every bound hash. Only this
report was written. It remains unstaged and uncommitted, uses LF endings,
ends in one LF, and contains no trailing horizontal whitespace.

Report LF line count: `000821`

Report byte count: `040765`

Report ordinary SHA-256: reported externally after freeze; embedding an
ordinary self-hash would be circular.

Report normalized self-SHA-256:
`7a8682a17358da5a7eac393faed927c62e2205c840fac456950ebf2ca7c35760`

Normalization rule: replace the six decimal digits on each count line and
the 64 hexadecimal characters on the normalized-self line by ASCII zeroes,
preserve every other byte, and compute SHA-256. The file must use LF endings,
end in one LF, and contain no trailing horizontal whitespace.
