# ISP v17 — PTS-0 pre-pin differential closure audit

## Common-opportunity causality, control descent, physical parents, and resolution

Date: **2026-08-24**

Status: **AUTHOR-SIDE DIFFERENTIAL CLOSURE / EXECUTABLE QA PASS-WITH-SCOPE**

Authority: **none**

Immutable pin: **not authorized / absent**

Independent review or acquisition: **not authorized / absent**

Scientific result: **none**

---

## 0. Authorization and invariant scientific question

The user authorized one author-side PTS-0 pre-pin differential closure audit.
This file closes only the six named pre-pin defects in the author design. It
does not open a pin, review, apparatus packet, acquisition, empirical result,
PTS-1, regional composition, candidate lattice, ontology, chronology,
spacetime, gravity, or successor.

The following objects do not change:

```text
candidate boundaries:  B0=S, B1=S+M;
B0 histories:          H-M0, H-M1 after the same S causal break;
B1 histories:          P-LOOP and P-CONTROLLER pairs;
future policies:       PI-EX, PI-PHASE, PI-NULL;
reported vector:       (D_M,S_B0,S_B1).
```

The differential law replaces cell-specific realized-schedule comparisons,
makes every control descend into the result, defines reader aggregation,
separates core memory descent from instrument quality, supplies coherent
finite physical parents, and gives the thresholds and trace projection an
operational meaning.

---

## 1. Findings against the first author package

Root reproduces all six pre-pin findings.

| code | first-package defect | disposition here |
|---|---|---|
| `D1` | concentration around different cell-specific time averages does not itself identify a common causal comparison under drift | common-opportunity paired randomization replaces the estimand |
| `D2` | eight controls are counted but do not have a total lift | every control receives direction, evidence state, affected coordinates, and route |
| `D3` | the max over boundary readers has no interval map | simultaneous max-interval rule is frozen |
| `D4` | point masses establish simplex nonemptiness but not physical joint realizability | six separate coherent finite-dimensional parent models are constructed |
| `D5` | the all-24 conjunction measures an ideal instrument suite, not memory existence | `D_M` becomes a core causal-memory predicate and the all-24 conjunction becomes a printed diagnostic |
| `D6` | thresholds and one-bit exterior trace have only author choice, not an operational role | guessing advantages, a trace veto, and a finite-refinement bound are frozen |

These are semantic repairs before any pin. None is classified as a Rust-only
defect.

---

## 2. Common-opportunity causal law

### 2.1 Pair-specific microblocks

There are still 148 unique assigned cell **types** and 80 registered
total-variation comparisons. Acquisition is now indexed by comparison edge,
not by separately timed cell type.

For each registered edge `e=(c0,c1)`, create `J` two-opportunity microblocks.
The two physical slots in microblock `j` are labelled `k=0,1` before treatment
assignment. One fair random bit assigns `(c0,c1)` or `(c1,c0)` to those two
slots. Thus both arms occur exactly once in every microblock and face the same
pair of physical opportunities.

The 80 edge schedules may be interleaved, but no outcome is reused across two
registered edges. This deliberately trades attempts for an unambiguous causal
target. Within each of 32 macroblocks every edge receives the same number of
microblocks; edge order and within-edge arm order are randomized from recorded
independent seeds.

### 2.2 Slot potential laws and no-interference boundary

For outcome subset `A`, let

$$
p^a_{e j k}(A)
=P\!\left(Y_{e j k}(a)\in A\mid\mathcal F_{e j}^{-}\right),
\qquad a\in\{0,1\},
\tag{2.1}
$$

where `F^-_(ej)` is the complete registered past before the random order bit
of microblock `j`. `Y_(ejk)(a)` is the potential registered outcome if arm
`a` occupies slot `k`.

This type requires:

1. the order bit is exogenous conditional on `F^-_(ej)`;
2. both arm--slot assignments have probability `1/2`;
3. the outcome in a slot is consistent with its literal assigned arm;
4. washout/reset makes one slot's treatment unable to alter the other slot's
   potential law; and
5. omissions, order leakage, carryover, or failed washout route the affected
   edge `INVALID`.

Predictable apparatus drift may change every `p^a_(ejk)` with `j` and `k`.
Treatment-dependent carryover is not called drift and is not licensed.

### 2.3 Common target and estimator

Both arms are compared on the same opportunities:

$$
P^\star_{e,a}(A)
=\frac1{2J}\sum_{j=1}^{J}\sum_{k=0}^{1}p^a_{e j k}(A).
\tag{2.2}
$$

If `K_j(a)` is the randomly assigned slot of arm `a`, define

$$
\widehat P_{e,a}(A)
=\frac1J\sum_{j=1}^{J}
\mathbf1\!\left\{Y_{e j K_j(a)}\in A\right\}.
\tag{2.3}
$$

Conditional on the pre-microblock past,

$$
E\!\left[
\mathbf1\{Y_{e j K_j(a)}\in A\}
\mid\mathcal F_{e j}^{-}
\right]
=\frac12\sum_{k=0}^{1}p^a_{e j k}(A).
\tag{2.4}
$$

The order randomization and physical outcome randomness are therefore both in
one bounded martingale difference. The estimand is not the law at the times
that happened to receive one cell. It is each arm's law averaged over the same
two slots in every paired opportunity.

The registered causal distance is

$$
d_e^\star=d_{\rm TV}(P^\star_{e,0},P^\star_{e,1}).
\tag{2.5}
$$

No comparison between different edge schedules is used in a PTS decision.

### 2.4 Simultaneous coverage and revised attempt count

For the 32-cell primary alphabet and `a=0.0125`, bounded martingale
concentration gives

$$
P\!\left[
d_{\rm TV}(\widehat P_{e,a},P^\star_{e,a})>a
\right]
\le 2(2^{32}-2)e^{-2Ja^2}.
\tag{2.6}
$$

There are 160 edge-arm laws. Hence

$$
2\times160\times(2^{32}-2)e^{-2Ja^2}\le0.01.
\tag{2.7}
$$

The smallest integer is

$$
J_{\min}=104{,}174.
\tag{2.8}
$$

The smallest multiple of 32 macroblocks is

$$
J=104{,}192=32\times3{,}256
\tag{2.9}
$$

microblocks per comparison edge. The total issued attempts are

$$
80\times 2\times104{,}192=16{,}670{,}720.
\tag{2.10}
$$

The simultaneous bound is approximately `0.00994218`. Every distance interval
retains radius `r=2a=0.025`. This is an author-side mathematical number, not a
runtime or apparatus-feasibility claim.

---

## 3. Boundary-reader aggregation

For a boundary pair, every reader `v` has a simultaneous interval

$$
[L_{m,v},U_{m,v}]
\tag{3.1}
$$

for its common-opportunity distance. If any required interval is malformed or
empty, the row is `INVALID`. Otherwise the exact max interval is

$$
L_m=\max_{v\in V_B}L_{m,v},
\qquad
U_m=\max_{v\in V_B}U_{m,v}.
\tag{3.2}
$$

On the simultaneous event,

$$
\max_v m_{B,v}\in[L_m,U_m].
\tag{3.3}
$$

The three `B0` and nine `B1` readers define the operational coordinate. PTS-0
does **not** convert this maximum into trace distance, claim equality of an
underlying two-qubit density matrix, or consume a tomography inversion bound.
The result language is permanently “matched at the frozen registered reader
resolution.”

---

## 4. Total control descent

### 4.1 Evidence states

Each of the eight paired controls has an expected direction and exactly one
evidence state:

```text
INVALID       malformed/empty interval or causal/procedural failure;
SATISFIED     expected-absent with U<=0.10, or expected-present with L>=0.25;
CONTRADICTED  expected-absent with L>=0.25, or expected-present with U<=0.10;
UNRESOLVED    otherwise.
```

### 4.2 Frozen roles

| control | direction | coordinates | contradicted route |
|---|---|---|---|
| `A0 B0-PASS-NULL` | absent | `S_B0` | `INVALID` — a known-null comparison produces a large difference |
| `A1 B0-FAIL-SENS` | present | `S_B0` | `UNDERDETERMINED` — sensitivity not established |
| `A2 B1-PASS-NULL` | absent | `S_B1` | `INVALID` |
| `A3 B1-FAIL-SENS` | present | `S_B1` | `UNDERDETERMINED` |
| `A4 M-READER-SENS` | present | `D_M` | `UNDERDETERMINED` |
| `A5 RNG-TO-S-NULL` | absent | all three | `INVALID` — assignment path contaminates `S` |
| `A6 INJECTED-SENTINEL` | present | all three | `UNDERDETERMINED` |
| `A7 REFERENCE-A/B-NULL` | absent | all three | `INVALID` — nominally identical paths are distinguishable |

An `INVALID` control interval invalidates every coordinate to which it is
assigned. An unresolved control makes those coordinates underdetermined. A
satisfied control leaves the provisional coordinate unchanged. These lifts
are applied in the priority order

```text
INVALID control route;
UNDERDETERMINED control route;
provisional scientific decision.
```

Thus a control never creates `PASS` or scientific `FAIL`. It only validates or
withholds the interpretation of the registered comparison. The three-result
vector remains unchanged; the eight control states must be printed beside it.

---

## 5. Core memory descent and instrument-quality diagnostics

### 5.1 Core coordinate `D_M`

`D_M` now means bounded causal descent of the proposed memory, not perfection
of all seven instruments. It requires:

1. the main `H-M0/H-M1` terminal-M reader separation is satisfied;
2. the `M-ID` pattern is satisfied: `PI-EX` and held-out `PI-PHASE` carry the
   history effect, while `PI-NULL` does not;
3. all four `M-X` versus `M-ID` causal-toggle effects are satisfied; and
4. at least one of `M-RAND-U`, `M-RESET`, or `M-ISO` is a qualifying removal
   family: both history-to-`S` residuals are absent and its intervention differs
   from `M-ID` under both memory-sensitive policies at the frozen `H-M1`
   sensitivity anchor.

Each removal family aggregates its four intervals as `INVALID` if any interval
is invalid, `SATISFIED` if all four are satisfied, `CONTRADICTED` if none is
invalid and at least one is contradicted, and `UNRESOLVED` otherwise.

The core aggregation is:

```text
INVALID
  a mandatory core interval is invalid, or no removal family is evaluable;

FAIL
  a mandatory reader/baseline/toggle duty is contradicted, or all three
  removal families are contradicted;

PASS
  every mandatory reader/baseline/toggle duty is satisfied and at least one
  removal family is satisfied;

UNDERDETERMINED
  otherwise.
```

More explicitly: a satisfied removal family witnesses the existential removal
duty even if an optional alternative family is invalid. If none is satisfied,
three contradicted families give `FAIL`, three invalid families give `INVALID`,
and every other mixture gives `UNDERDETERMINED`. Mandatory unresolved evidence
always leaves the core underdetermined.

The coordinate-specific controls from Section 4 are then lifted into this
provisional decision.

### 5.2 Diagnostic suite `Q_M`

The original all-24 conjunction is retained verbatim as

$$
Q_M^{\rm suite}
\tag{5.1}
$$

and printed as a non-coordinate diagnostic. It includes the `M-READ` versus
`M-ID` low-backaction duties, every removal branch, and `M-RESET-ISO`.

A real, causally manipulable memory may have `D_M=PASS` and
`Q_M^{suite}=FAIL` because its reader is invasive or one optional removal
instrument is poor. Conversely, a polished instrument suite cannot fill
`D_M` unless the core history write, causal toggle, removal, and held-out
transfer duties pass. `Q_M` never fills `S_B0` or `S_B1`.

---

## 6. Operational thresholds and exterior-trace projection

### 6.1 Total variation as guessing performance

For equal prior probabilities, the optimal one-shot probability of guessing
which of two laws generated a record is

$$
p_{\rm guess}=\frac{1+d_{\rm TV}}2.
\tag{6.1}
$$

The registered constants therefore mean:

| TV distance | optimal guessing probability |
|---:|---:|
| `0.05` power-pass interior | `0.525` |
| `0.10` match/pass decision ceiling | `0.55` |
| `0.25` fail decision floor | `0.625` |
| `0.30` power-fail interior | `0.65` |

PTS-0 does not call `0.10` exact equality. It asks whether residual history
improves an optimal registered-record guess by at most five percentage points,
or by at least twelve and one-half points. The grey region is intentional and
pre-data. These are operational architecture thresholds, not constants of
nature. A future physical packet would still have to show that calibration,
reader conditioning, and block lifetime can resolve them.

### 6.2 `G` is a veto, not an exterior-state quotient

Let `Y_tilde` be the finite predeclared trace refinement that distinguishes
which registered controller, seed, resonator, reservoir, heat, old-state,
latency, or lineage bin fired. The 32-cell score `Y=K(Y_tilde)` keeps the
terminal code and collapses that refinement to `G=0/1`.

PTS-0 no longer treats equality of `G` rates as evidence that exterior traces
are equal. A boundary row may receive `ROW-MATCHED-PASS` only if, for both
future arms,

$$
U\big(P(G=1)\big)\le \tau_G=0.05.
\tag{6.2}
$$

The trace interval is the single-arm subset interval
`[max(0,p_hat_G-a),min(1,p_hat_G+a)]`, not the two-arm distance interval; it is
covered by the same all-subsets simultaneous event.

An empty/malformed trace interval invalidates the row. If the coarse future
distance passes but either trace interval is not certified clean, the row is
`ROW-MATCHED-UNRESOLVED`, not pass. A coarse matched-fail remains a fail because
coarse-graining cannot increase total variation.

If `K` is injective on `G=0`, then for any two refined laws

$$
d_{\rm TV}(\widetilde P,\widetilde Q)
\le d_{\rm TV}(K\widetilde P,K\widetilde Q)
+\min\{\widetilde P(G=1),\widetilde Q(G=1)\}.
\tag{6.3}
$$

Consequently a coarse pass plus the trace veto bounds the finite refined
distance by `0.15`, corresponding to guessing probability at most `0.575`.
The trace-clean power interior requires true trace probability at most `0.025`;
the per-law radius `a=0.0125` then certifies (6.2) on the simultaneous event.

No claim is made about distinctions inside unregistered continuous nominal
bins. Raw records remain stored, and a future physical review must assess the
bins. This is a quantified finite-resolution ceiling, not “complete universe”
sufficiency.

---

## 7. Six globally coherent finite-dimensional parents

### 7.1 Common carrier and maps

Each alternative is generated by one parent over

$$
\mathcal H_S\otimes\mathcal H_M\otimes\mathcal H_E\otimes\mathcal H_R
=(\mathbb C^2)^{\otimes4},
\tag{7.1}
$$

plus finite classical assignment and failure registers. `E` is a declared
exterior controller/resonator memory. `R` is an explicitly inaccessible sink
that carries information exported by a relaxation or reset but is not a
registered reader; its omission is printed resource debt, not global erasure.
The same typed interface is used in all six parents:

- preparations are CPTP replacement channels;
- the `S` break replaces only `S` by the assigned stabilizer state;
- `M-X`, controlled exchange, and controlled phase are unitary channels;
- `M-RAND-U` is the equal mixture of `I_M` and `X_M` with the seed retained in
  the exterior audit register;
- `M-RESET` is a CPTP replacement of `M` by `|0>` with the old logical state
  transferred, not cloned, to an exterior destination;
- `M-ISO` selects futures with no `M--S` interaction;
- readers are finite projective instruments with failure outcomes; and
- `PI-NULL` acts on `S` without consulting `M` or `E`.

The primitive channels are explicit:

$$
\mathcal U_V(\rho)=V\rho V^\dagger,
\qquad
\mathcal R_M(\rho)=\tfrac12\rho+\tfrac12X_M\rho X_M,
\qquad
\mathcal P_\sigma(\rho)=\sigma\,\operatorname{tr}\rho.
\tag{7.2}
$$

Unitary conjugation, a convex mixture of unitaries, and a replacement channel
are completely positive and trace preserving. The ideal reader instrument has
Kraus operators `K_b=|b><b|` in its assigned basis. Reset and the B0 natural
relaxation use a `SWAP_(MR)` dilation with `R` initialized in `|0>`; the old
state moves to `R` and is never cloned or destroyed. The B1-fail response uses
`CNOT_(E->S)`. The loop is exactly `U_SM^dagger U_SM=I_SM`. Hence all laws in
the table below are compositions of one printed preparation, channel and
instrument grammar, not independently chosen normalized vectors.

All 148 unique cell types are generated by these shared maps. No law is
assigned independently to obtain a desired distance. The ideal parents use
zero failure probability and `G=0` except where an exterior carrier is the
explicit mechanism; adjoining a common failure instrument preserves the
relations and fills all failure cells.

### 7.2 Separate alternatives

| parent | single physical law | registered consequence |
|---|---|---|
| `W-B0-PASS` | `H-M0/H-M1` write orthogonal `M` at the cut and the `S` break matches `S`; every natural future ignores `M` and the same target-independent unitary transfer moves the old `M` value to inaccessible `R`, leaving the later registered `M` record common | boundary reader distances and the complete registered B0 future distances are zero without a scored full-boundary restart; `R` still carries the past |
| `W-B0-FAIL` | same boundary preparation, while `PI-EX` swaps/maps `M` into `S` and `PI-PHASE` maps the `M` bit to an orthogonal Ramsey phase | `B0` matches exactly and at least one future distance is one |
| `W-B1-PASS` | direct preparation and `U_SM` followed by `U_SM^dagger` end at the same `S+M`; `E` is fixed and futures depend only on `S+M` | all nine reader laws and all registered futures agree |
| `W-B1-FAIL` | both controller histories end at the same `S+M`, but write distinct `E`; a later controlled operation from `E` to `S` is part of the frozen future | `B1` reader distances are zero and a controller-pair future distance is one |
| `W-M-PASS` | `M0/M1` are orthogonal, exchange and Ramsey-phase futures read them, `M-X` toggles them, `PI-NULL` ignores them, and reset or isolation removes the history-to-`S` channel | every core memory duty passes, including held-out phase and a qualifying removal family |
| `W-M-FAIL` | both histories leave the proposed `M` in the same parked state and the `M--S` channel is off | main memory-reader separation is zero and core descent fails |

These are six different possible worlds fixed before evaluation, not one world
required to pass and fail simultaneously. Each world defines every named
history, operation, future, reader, control, and failure branch on the same
finite carrier. Open total-variation balls of radius `0.025` around their
registered laws remain in the relevant `0.05/0.30` interiors. This establishes
physical-model nonemptiness without claiming that an acquired transmon realizes
any parent.

---

## 8. Required executable hostile audit

The differential checker is

```text
v17/research-incubator/active/pts0/check_pts0_differential.rs
```

It was written only against Sections 2--7 and checks:

1. exact common-opportunity identity under both order assignments for every
   binary two-slot potential-outcome pattern;
2. the revised 160 edge-arm union bound and 16,670,720-attempt count;
3. reader max-interval aggregation, including empty and malformed inputs;
4. all `4^8` control-evidence vectors for all three coordinate routes;
5. trace-veto routing and the `0.15` refinement ceiling;
6. separate core-memory and all-24 suite decisions, including
   `D_M=PASS,Q_M=FAIL`;
7. normalized laws for all 148 cell types under each of the six parents;
8. B0/B1/memory pass and fail distances derived from those parents; and
9. the unchanged mismatch, restart, empty-set, and coordinate-separation
   firewalls.

Executable success remains author QA, not physical evidence.

Compiled with warnings denied, the checker prints:

```text
PTS0-DIFFERENTIAL-CHECK: PASS
unique_cell_types=148
registered_edges=80
edge_arm_laws=160
common_opportunity_binary_cases=16
minimum_microblocks_per_edge=104174
chosen_microblocks_per_edge=104192
total_issued_attempts=16670720
simultaneous_error_bound=0.009942177412159
distance_ci_radius=0.025000
control_route_cases=196608
finite_parent_models=6
generated_parent_cell_laws=888
reader_aggregation=MAX_INTERVAL_EXECUTABLE
trace_projection=VETO_WITH_REFINED_TV_CEILING_0.15
trace_refinement_grid_pairs=225
memory_output=CORE_COORDINATE_PLUS_SUITE_DIAGNOSTIC
assignment_randomness=INCLUDED
predictable_drift=COMMON_OPPORTUNITY_AVERAGED
authority=AUTHOR_SIDE_QA_ONLY
```

Its eight named tests pass. The historical first checker remains retained only
to reconstruct the pre-differential package; it is not the current executable
semantics for `D1--D6`.

---

## 9. Differential disposition and stop

The mathematical differential and root rebuild inside the author task close
`D1--D6` at author-side design scope. This is not independent review. It does not establish
that the selected transmon platform can implement the schedule, sustain the
attempt count, realize the parent maps, calibrate the reader family, or keep
trace occupancy below the veto threshold.

```text
PTS-0 PRE-PIN DIFFERENTIAL LAW:  COMPLETE AUTHOR-SIDE
EXECUTABLE CONFORMANCE:          PASS-WITH-SCOPE AUTHOR QA
IMMUTABLE PIN:                   ABSENT / NOT AUTHORIZED
INDEPENDENT REVIEW:              ABSENT / NOT AUTHORIZED
APPARATUS OR EMPIRICAL RESULT:   ABSENT / NOT AUTHORIZED
```

No automatic action follows.
