# ISP v17 — PTS-0 physical temporal sufficiency design

## Evidenced memory and natural fixed-boundary screening on one two-transmon apparatus

Date: **2026-08-24**

Status: **AUTHOR-SIDE DESIGN / NO PIN / NO REVIEW / NO ACQUISITION**

Authority: **none**

Maximum possible claim of this file: **a bounded experiment and inference
design is internally specified; no physical result exists**

> **Current-lineage notice.** This file is the first author design. Its
> cell-specific schedule estimand, unlifted controls, implicit reader
> aggregation, all-24 meaning of `D_M`, point-law witness proof, and raw `G`
> interpretation are superseded by
> `v17_pts0_pre_pin_differential_closure_audit.md`. The scientific question,
> histories, boundaries, policies, and three-coordinate vector are unchanged.
> This file must not be pinned or reviewed without that differential law.

---

## 0. Authorization and route separation

The user authorized one author-side PTS-0 design and executable
semantic/power audit. The authorization does not include an immutable pin,
independent review, apparatus acquisition, empirical evaluation, or successor.

PTS-0 is a new bounded programme. It is not SPB v4 and cannot repair, rename,
or reopen the terminal SPB contract route. It consumes only these exact
surviving propositions:

1. source closure is not causal identification;
2. a system causal break is a physical measure/discard-and-reprepare
   intervention, not observational conditioning;
3. a physical memory must be independently prepared, manipulated, and read;
4. natural-state future sufficiency compares different histories only at an
   independently matched candidate boundary;
5. assigned attempts, failures, leakage, controller records, and stale records
   remain in an intention-to-treat law;
6. boundary coordinates, material carriers, and predictive process objects
   are different types; and
7. finite apparatus success or failure has no automatic ontological,
   chronological, spacetime, gravitational, or universal consequence.

PTS-0 does **not** inherit the SPB candidate lattice, composition/gluing law,
minimality or necessity predicates, classifier hierarchy, outcome ladder, or
scientific rung. Its only scientific subjects are:

- causal descent of one named memory transmon `M`; and
- natural fixed-boundary future sufficiency of `B0=S` and `B1=S+M`.

---

## 1. The corrected physical question

Let `H` be a registered earlier history, `B` a candidate physical boundary at
the cut, `pi` a future intervention policy, and `Y_F` the complete registered
future record. Natural-state future sufficiency is the bounded conditional
independence statement

$$
Y_F \perp H \mid B,\operatorname{do}(\pi).
\tag{1.1}
$$

Equivalently, for boundary-equal histories and every registered future policy,

$$
P(Y_F\mid H=h,B=b,\operatorname{do}(\pi))
=
P(Y_F\mid H=h',B=b,\operatorname{do}(\pi)).
\tag{1.2}
$$

The experiment does not claim nondisturbing access to an unknown quantum state
in one run. Boundary equality is certified on separately randomized validation
copies with an informationally complete reader family. Scored continuation
copies execute the same history preparations without the destructive boundary
read.

Two different propositions are permanently separated:

```text
NATURAL SUFFICIENCY
  different histories, independently matched naturally occurring B,
  then a held-out continuation;

RESTART SUFFICIENCY
  actively erase/reprepare the full B, then continue.
```

Restarting `S+M` may erase exactly the memory being investigated. It is a
useful control but cannot enter the natural-sufficiency score.

### 1.1 Independent memory descent

The variable called `M` earns bounded physical-memory status only if:

1. earlier randomized histories produce distinguishable `M` records while the
   freshly prepared `S` is held fixed;
2. independently randomized `M` operations have their preregistered effects
   on complete future records;
3. reset, inaccessible-seed randomization, and isolation suppress the
   registered history-to-`S` channel where they are designed to suppress it,
   while all `M`, controller, and old-state records remain visible;
4. the effect survives at least one held-out future policy; and
5. controller leakage, assignment leakage, direct pulses on `S`, and unblocked
   carryover are excluded or route the duty invalid.

Memory descent does not imply boundary sufficiency. Boundary sufficiency does
not identify the matter carrying the memory. PTS-0 reports them separately.

---

## 2. Physical platform and source ceiling

The bounded apparatus is one independently addressed pair of neighboring
superconducting transmons:

```text
S  system transmon;
M  candidate memory transmon;
C  tunable/direct coupling path between S and M;
RS readout/control chain assigned to S;
RM readout/control chain assigned to M;
RNG hardware assignment source and immutable attempt ledger;
CB controller/reference registers, resonators, buses, reservoirs, and clocks.
```

`B0` contains `S` and its declared ports. `B1` contains `S+M` and their
declared ports. Inference concerns the state coordinate resolved by the frozen
calibrated reader family; it does not assert microscopic completeness of a
Hilbert-space density operator. `CB`, resonator state, bus state, reservoirs,
and assignment media are registered possible exterior carriers; they are not
silently folded into `B1`.

The exact inherited primary-source receipts establish only:

- an operational causal-break theorem (`SPB-S1`);
- feasibility of complete system-side multi-time tomography and public count
  handling (`SPB-S2`); and
- an engineered two-transmon system--memory predecessor (`SPB-S3`).

No source executes this PTS-0 design. No exact device identifiers, calibration
packet, run records, or public raw-data packet exist. Platform feasibility is
not an empirical PTS result.

---

## 3. Attempts, assignments, and the causal parent

Every issued attempt is typed as

$$
(\Xi,A,E,Y_{\rm raw}),
\tag{3.1}
$$

where:

- `Xi` contains immutable device, block, regime, and calibration lineage;
- `A=(H,s,I_M,pi,v_F)` contains the randomly assigned earlier history,
  system repreparation, memory operation, future policy, and final reader;
- `E` contains literal acknowledgements, pulse executions, timestamps,
  resets, latencies, seeds, controller paths, and deviations; and
- `Y_raw` contains every registered readout, leakage flag, failure, timeout,
  stale record, controller record, and terminal destination.

The hardware randomizer assigns complete cells before their outcomes. Within
each of 32 acquisition blocks, every registered cell receives the same issued
attempt count in a randomly permuted order. The physical randomizer, seed
lineage, device acknowledgement, and assignment-to-pulse map must be validated
without conditioning on successful runs.

The causal identification route is randomized intention to treat. It requires:

1. assignment-source exogeneity relative to the registered device future;
2. positive assignment probability for every registered cell in every block;
3. consistency between assignment, literal execution, and recorded outcome;
4. no postselection on preparation, reset, measurement, or leakage success;
5. bounded or blocked inter-attempt carryover, with washout/reset records; and
6. validation-reader and scored-continuation branches share the same history
   preparation law before their randomized branch point, with branch leakage
   and pre-branch disturbance bounded or invalidating; and
7. no use of descendants of assignment to repair balance or choose a cell.

If any premise fails, the affected duty is `INVALID`. No observational or
transport substitute is included in PTS-0.

---

## 4. The two candidate boundaries and predeclared histories

There are exactly two candidates. They are not a lattice and no minimality or
necessity statement is defined.

| code | candidate | bounded question |
|---|---|---|
| `B0` | freshly prepared `S` | does `S` alone screen the registered histories? |
| `B1` | naturally prepared `S+M` | do matched joint `S+M` states screen the registered histories? |

### 4.1 `B0=S`: memory-different histories

The history pair is

```text
H-M0  prepare/write M=0, then perform the complete S causal break;
H-M1  prepare/write M=1, then perform the same complete S causal break.
```

The break randomly reprepares `S` in each of the four informationally complete
states

$$
|0\rangle,\quad |1\rangle,\quad |+\rangle,
\quad |+i\rangle.
\tag{4.1}
$$

For a fixed assigned state, `S` is intended to be equal while `M` differs.
Separate validation copies measure `S` in the `X`, `Y`, and `Z` bases. A
future difference after certified `S` matching refutes `B0` at the tested
scope and is expected in the engineered memory-positive control.

### 4.2 `B1=S+M`: boundary-equal/history-different pairs

Two pair types are frozen.

```text
P-LOOP
  H-ID:   direct preparation of the assigned S+M boundary state;
  H-LOOP: a calibrated S--M pulse/interaction sequence followed by its
          independently calibrated inverse, ending at the same assigned S+M
          boundary state but with a different earlier physical history.

P-CONTROLLER
  H-C0 and H-C1: distinct controller/reference paths and earlier pulse
  histories engineered to end in the same S+M boundary state.  Controller,
  resonator, and reference records remain outside B1 and in Y_raw.
```

Separate validation copies use the nine local-Pauli product settings

$$
\{X,Y,Z\}_S\times\{X,Y,Z\}_M.
\tag{4.2}
$$

Each setting retains all four joint outcomes and failure sentinels. Reader
informational completeness, inversion conditioning, leakage coverage, and
simultaneous uncertainty are validation duties. Failure to establish them
routes the pair invalid or match-underdetermined; it cannot be hidden inside a
future-screening fail. The scored
continuation copies do not read or reset the candidate boundary before the
future policy. Any row that forces equality by resetting all of `S+M` is
`INVALID` for natural sufficiency and may be reported only as an unscored
restart control.

---

## 5. Memory interventions and future policies

### 5.1 Randomized memory grammar

On the `H-M0/H-M1` family, one of seven physical operations is assigned at the
cut:

| code | operation | registered role |
|---|---|---|
| `M-ID` | no intended change | natural memory carriage baseline |
| `M-READ` | ensemble informational reader on its randomized branch | identifies the memory record and read backaction |
| `M-X` | calibrated toggle/orthogonalizing pulse | causal sensitivity control |
| `M-RAND-U` | Pauli randomization whose seed is inaccessible to the licensed future | operational randomization; seed carrier retained in audit lineage |
| `M-RESET` | active reset to a frozen reference state | bounded reset control; heat, retries, and old-state destination retained |
| `M-ISO` | detune/echo/decouple during continuation | bounded isolation; residual `ZZ`, bus, drive, and resonator coupling retained |
| `M-RESET-ISO` | reset followed by isolation | strongest registered removal control |

`M-READ` is not a nondisturbing single-run revelation. Reset and randomization
do not destroy information globally. Every seed, old-state destination,
reservoir, heat record, retry, and failure remains in `Y_raw` or in declared
inaccessible debt.

Only `M-ID` rows enter natural `B0/B1` sufficiency. Other operations establish
memory descent or serve as restart/removal controls.

### 5.2 Three future policies

| code | role |
|---|---|
| `PI-EX` | exchange-sensitive Ramsey/partial-iSWAP continuation |
| `PI-PHASE` | phase-sensitive Ramsey/CZ continuation; held out from boundary validation and memory-operation calibration |
| `PI-NULL` | memory-parked system continuation expected to be insensitive to the M bit |

The circuit family and analysis rule for `PI-PHASE` are fixed before its
records are opened. No parameter is refit to the held-out policy.

---

## 6. Complete registered outcome model

The raw record is never discarded. For the finite primary inference model,
one frozen projection first maps every issued attempt to exactly one of 16
disjoint terminal codes:

| cell | code |
|---:|---|
| 0 | `OK-S0-M0` |
| 1 | `OK-S0-M1` |
| 2 | `OK-S1-M0` |
| 3 | `OK-S1-M1` |
| 4 | `S-PREP-FAIL` |
| 5 | `M-PREP-FAIL` |
| 6 | `BREAK-FAIL` |
| 7 | `M-OP-FAIL` |
| 8 | `POLICY-FAIL` |
| 9 | `S-READOUT-FAIL` |
| 10 | `M-READOUT-FAIL` |
| 11 | `S-LEAKAGE` |
| 12 | `M-LEAKAGE` |
| 13 | `TIMEOUT` |
| 14 | `STALE-OR-WRONG-RECORD` |
| 15 | `OTHER-REGISTERED-FAILURE` |

For cells 0--3, the two bits are outcomes in the assigned terminal reader
bases; the basis labels are part of `A`. Multiple failure flags use this fixed
priority:

```text
stale/wrong lineage > timeout > S preparation > M preparation > break >
memory operation > future policy > S readout > M readout > S leakage >
M leakage > other registered failure > successful terminal bits.
```

Each terminal code is crossed with one controller/reference-trace bit:

```text
G=0  every predeclared controller, seed, resonator, reservoir, heat,
     old-state, latency, and lineage coordinate is in its registered nominal
     bin;
G=1  at least one such coordinate occupies a registered nonnominal/trace bin.
```

The primary alphabet therefore has `16 * 2 = 32` cells. All continuous raw
coordinates remain stored; `G` is their frozen finite-resolution score, not
permission to delete them. The winning terminal category never deletes
subordinate raw flags. Unknown or malformed
raw records route the relevant classifier `INVALID`; they are not hidden in an
apparently scientific fail cell. The history label itself is an assignment and
is not inserted into the scored future outcome.

The primary statistical model is the full 32-cell probability simplex for
every assigned cell. No equality, Markov, quantum, or desired-answer
restriction is imposed on that simplex.

---

## 7. Boundary matching and future screening estimands

### 7.1 Validation mismatch

For candidate `B`, pair `(h,h')`, and independently assigned validation reader
`v`, let `R_B` be the complete validation outcome. Define

$$
m_{B,v}(h,h')
=d_{\rm TV}\!\left(
P(R_B\mid \operatorname{do}(h),v),
P(R_B\mid \operatorname{do}(h'),v)
\right).
\tag{7.1}
$$

The pair mismatch at the registered operational reader resolution is

$$
m_B(h,h')=\max_{v\in V_B}m_{B,v}(h,h').
\tag{7.2}
$$

Validation uses separate copies and cannot consume scored continuations. An
ill-conditioned or incompletely calibrated reader family cannot certify a
match. `m_B` is not a statement that every microscopic degree of freedom in
the material device is equal.

### 7.2 Natural future screening

For the same history pair and a future policy `pi`, define

$$
s_B(h,h';\pi)
=d_{\rm TV}\!\left(
P(Y_F\mid \operatorname{do}(h),\operatorname{do}(\pi)),
P(Y_F\mid \operatorname{do}(h'),\operatorname{do}(\pi))
\right).
\tag{7.3}
$$

This distance counts the complete 32-cell future law, not a successful-run
conditional. The bounded candidate defect is

$$
\Delta_B
=\max_{(h,h')\in\mathcal P_B}\max_{\pi\in\Pi_+}
s_B(h,h';\pi),
\tag{7.4}
$$

but a row may refute sufficiency only after its corresponding boundary match
is certified. A boundary mismatch means the intended fixed-`B` comparison was
not instantiated; it is not evidence of insufficiency.

### 7.3 Memory-descent distances

Memory descent uses frozen projections of the same complete 32-cell law:

```text
Y_M       terminal M reader and its failure/leakage/trace cells;
Y_S       terminal S reader and its failure/leakage/trace cells;
Y_FULL    the complete 32-cell outcome.
```

The projection is fixed by the obligation and never selected from the result.
An isolation control is expected to remove a history effect from `Y_S`, not
from `Y_M` or `Y_FULL`: an isolated memory may continue to store and reveal the
past. Likewise reset/randomization may export old information into retained
controller or reservoir records. No absence claim is made about the complete
universe or even the complete raw apparatus record.

The memory programme registers 24 distance obligations:

1. one `Y_M` reader separation between `H-M0` and `H-M1` (`present`);
2. three `Y_S` `M-ID` history effects, present for `PI-EX` and held-out
   `PI-PHASE` and absent for `PI-NULL`;
3. four `Y_S` `M-X` versus `M-ID` effects over two histories and the two
   memory-sensitive policies (`present`);
4. two `Y_S` `M-READ` versus `M-ID` QND-backaction controls (`absent` at the
   frozen resolution, with reader outcomes retained in `Y_FULL`);
5. two post-`M-RAND-U` residual history effects on `Y_S` (`absent`);
6. two post-`M-RESET` residual history effects on `Y_S` (`absent`);
7. two post-`M-ISO` residual history effects on `Y_S` (`absent`);
8. two post-`M-RESET-ISO` residual history effects on `Y_S` (`absent`); and
9. six `Y_S` intervention-versus-`M-ID` effects for randomize, reset, and
   isolate under both memory-sensitive policies (`present`).

Every obligation has its own confidence interval and expected direction.
Memory descent passes only if all 24 obligations pass. A confident
contradiction fails the registered memory-descent bundle; an inconclusive or
unexecuted operation is underdetermined. This does not fill either boundary
status.

---

## 8. Total decision semantics

The numerical thresholds are author-side PTS-0 constants:

$$
\epsilon_m=0.10,
\qquad
\epsilon_{\rm pass}=0.10,
\qquad
\epsilon_{\rm fail}=0.25.
\tag{8.1}
$$

For each boundary pair/policy row, let `[L_m,U_m]` and `[L_s,U_s]` be
simultaneous confidence intervals.

### 8.1 Row map

```text
ROW-INVALID
  procedural/causal failure, malformed interval, empty confidence set, or a
  full-candidate reset used to force natural boundary equality;

ROW-MATCHED-PASS
  U_m <= 0.10 and U_s <= 0.10;

ROW-MATCHED-FAIL
  U_m <= 0.10 and L_s >= 0.25;

ROW-MATCHED-UNRESOLVED
  U_m <= 0.10 and neither screening inequality is certified;

ROW-BOUNDARY-MISMATCH
  L_m > 0.10;

ROW-BOUNDARY-MATCH-UNRESOLVED
  the matching interval straddles 0.10.
```

### 8.2 Candidate map

For `B0` or `B1`, exactly one decision is printed:

```text
INVALID
  any mandatory row is invalid;

FAIL
  at least one required pair/policy is ROW-MATCHED-FAIL;

PASS
  every required pair/policy is ROW-MATCHED-PASS;

UNDERDETERMINED
  otherwise, including boundary mismatch or unresolved matching.
```

A single certified matched counterexample refutes the bounded universal
sufficiency statement. A pass requires every registered pair and policy. A
boundary mismatch alone can never produce `FAIL`.

### 8.3 Memory-descent map

For a distance expected `present`:

```text
SATISFIED      L >= 0.25
CONTRADICTED   U <= 0.10
UNRESOLVED     otherwise
```

For a distance expected `absent`, the inequalities are reversed. Malformed or
empty confidence sets and causal/procedural failures are `INVALID`.

The memory bundle is:

```text
INVALID          any obligation is invalid;
FAIL             no obligation is invalid and at least one is contradicted;
PASS             every obligation is satisfied;
UNDERDETERMINED  otherwise.
```

The complete reported object is the vector

$$
\mathcal V_{\rm PTS0}=(D_M,S_{B0},S_{B1}),
\tag{8.2}
$$

not an aggregate scalar. No coordinate fills another.

---

## 9. Finite design cardinalities

The author design contains exactly 148 assigned cell laws.

### 9.1 Validation copies: 60 laws

```text
B0: 2 histories * 4 S preparations * 3 Pauli readers = 24
B1: 4 histories in 2 pairs * 9 joint readers          = 36
```

### 9.2 Scored continuations: 72 laws

```text
B0 natural M-ID: 2 histories * 4 S preparations * 3 policies = 24
memory extra ops: 2 histories * 6 extra M ops * 3 policies    = 36
B1 natural M-ID: 4 histories * 3 policies                     = 12
```

### 9.3 Physical anchors and drift controls: 16 laws

Eight interleaved two-law controls are predeclared:

1. `B0` pass-sensitivity anchor;
2. `B0` fail-sensitivity anchor;
3. `B1` pass-sensitivity anchor;
4. `B1` fail-sensitivity anchor;
5. `M0/M1` reader-separation anchor;
6. randomizer-to-`S` crosstalk null pair;
7. injected-sentinel sensitivity pair; and
8. repeated-reference A/B pair for schedule-drift sensitivity.

The inference family contains 80 registered total-variation distances:

```text
boundary matching       30
natural screening       18
memory descent          24
anchor/drift controls    8
total                   80
```

No additional distance, pair, policy, or outcome may be selected from a
residual under this design.

---

## 10. Simultaneous confidence and exact author-side power calculation

### 10.1 Drift-robust schedule-average law

For assigned cell `c`, issued attempt `t`, and outcome subset `A`, let

$$
p_{c,t}(A)
=P(Y_t\in A\mid\mathcal F_{t-1},A_t=c),
\tag{10.1}
$$

where `F_(t-1)` is the complete registered past. Define the randomized-schedule
average law

$$
\bar P_c(A)=\frac1n\sum_{t=1}^n p_{c,t}(A).
\tag{10.2}
$$

The estimand is this block-balanced schedule-average law. It does not presume
stationarity or independent identically distributed shots. For each subset,
the centered indicator sequence is a bounded martingale difference. Therefore

$$
P\!\left(
d_{\rm TV}(\widehat P_c,\bar P_c)>a
\right)
\le
2(2^{32}-2)e^{-2na^2}.
\tag{10.3}
$$

This permits predictable drift and registered cross-run dependence in the
conditional means. It does not excuse confounded assignment, unregistered
carryover, missing attempts, or future-setting leakage; those are causal
invalidity.

### 10.2 Simultaneous family

Use

$$
a=0.0125,
\qquad
\alpha_{\rm fam}=0.01.
\tag{10.4}
$$

A union bound over 148 assigned cell laws and every nontrivial subset of the
32-cell alphabet gives

$$
2\times148\times(2^{32}-2)e^{-2na^2}\le0.01.
\tag{10.5}
$$

The minimum integer is

$$
n_{\min}=103{,}924
\tag{10.6}
$$

attempts per assigned cell. To use 32 equal acquisition blocks, PTS-0 chooses

$$
n=103{,}936=32\times3{,}248.
\tag{10.7}
$$

The exact issued-attempt count is therefore

$$
148\times103{,}936=15{,}382{,}528.
\tag{10.8}
$$

The computed simultaneous error bound is

$$
0.009962464798987583<0.01.
\tag{10.9}
$$

If every empirical cell law is within `a` of its schedule-average law, each
estimated pair distance is within

$$
r=2a=0.025
\tag{10.10}
$$

of its target. Every distance interval is

$$
[L,U]=
[\max(0,\widehat d-r),\min(1,\widehat d+r)].
\tag{10.11}
$$

### 10.3 Nonvacuous interior power regions

Uniform high power at the exact decision boundary is not generally possible.
PTS-0 therefore separates decision thresholds from predeclared interior power
neighborhoods.

For boundary pass:

$$
\mathcal M_{\rm pass}^{B}
=\{P:m_B\le0.05,\ s_B\le0.05
\text{ for every required row}\}.
\tag{10.12}
$$

For boundary failure:

$$
\mathcal M_{\rm fail}^{B}
=\{P:\text{some required row has }m_B\le0.05,
\ s_B\ge0.30\}.
\tag{10.13}
$$

The analogous memory-pass neighborhood has every `present` distance at least
0.30 and every `absent` distance at most 0.05. A memory-fail neighborhood has
at least one registered obligation confidently reversed by those interior
bounds.

On the simultaneous event, a true distance at most 0.05 has `U<=0.10`, while a
true distance at least 0.30 has `L>=0.25`. Consequently, uniformly over each
registered interior neighborhood,

$$
P(\text{correct PTS decision})
\ge1-0.009962464798987583
>0.99.
\tag{10.14}
$$

Every registered memory projection is a fixed coarse-graining of the 32-cell
law, so total-variation contraction makes the same simultaneous event cover
those projected distances. This guarantee is conditional on the randomized causal parent and complete
record model being valid. It includes every predeclared pair, policy,
validation sample, failure cell, reader, memory-controller record projection,
selection rule, and the registered predictable-drift schedule.

### 10.4 Physically typed witnesses for nonemptiness

The neighborhoods are not populated by answer tables. They have executable
apparatus-mode witnesses:

| witness | physical control mode | ideal relation |
|---|---|---|
| `W-M-PASS` | write `M0/M1`, reset `S`, use partial iSWAP/CZ futures, then execute `M-X`, randomize, reset, and isolate branches | required memory effects present and removal residuals absent |
| `W-M-FAIL` | park `M`, turn off the calibrated S--M channel, execute the same M operations | proposed memory effects absent |
| `W-B0-PASS` | use history-different cancelling S pulses, common parked `M`, and the same fresh `S` | matched S and equal futures |
| `W-B0-FAIL` | write `M0/M1`, reprepare the same `S`, then map M to S by partial iSWAP | matched S and separated futures |
| `W-B1-PASS` | direct preparation versus calibrated `U_SM U_SM^dagger`, no exterior retained flag | matched S+M and equal futures |
| `W-B1-FAIL` | match S+M while retaining a predeclared resonator/controller state outside B1 that later shifts S | matched S+M and separated futures |

At the ideal finite model these give distances zero or one. Their total-
variation balls of radius 0.025 lie inside the 0.05/0.30 power interiors, so
both model neighborhoods are nonempty. These are sensitivity and null
controls, not claims about an acquired device or the unknown target response.

---

## 11. Executable reference semantics

The authorized checker is

```text
v17/research-incubator/active/pts0/check_pts0_semantics.rs
```

It contains no apparatus data and awards no scientific status. It verifies:

1. the exact 148 cell-law and 80 distance counts;
2. the 32-cell complete outcome model constants;
3. the smallest 32-block-compatible sample size and simultaneous error bound;
4. nonempty pass/fail mathematical witnesses tied above to physical modes;
5. every aggregate boundary state on a three-row finite truth table;
6. every aggregate memory state on a four-obligation finite truth table;
7. 19,208 numerical interval/validity/restart combinations;
8. empty confidence sets route `INVALID`;
9. boundary mismatch never routes candidate `FAIL`;
10. full-boundary restart never enters natural sufficiency; and
11. memory descent never fills boundary sufficiency.

The checker is an executable definition and quality-control artifact. A code
failure is a design-conformance failure. Changing the physical question,
thresholds, histories, operations, outcome model, or interpretation is a
semantic change, not a software repair.

---

## 12. Hostile controls

PTS-0 must fail closed on at least these attacks:

1. compare different histories without matching the candidate boundary;
2. call a boundary mismatch candidate insufficiency;
3. reset all of `S+M` and call the result natural-state sufficiency;
4. infer physical memory from improved fit without randomized M operations;
5. call memory descent boundary sufficiency;
6. insert the history label into `Y_F` and obtain distance one by syntax;
7. drop failed reset, leakage, timeout, or stale-record attempts;
8. use a logged schedule without physical randomizer exogeneity;
9. lose positivity in a history/operation/policy cell;
10. use `PI-PHASE` to tune a history, threshold, or memory operation;
11. restrict the model class so a pass or fail alternative is empty;
12. claim high power at a decision boundary without an interior margin;
13. return an empty confidence set and continue scoring;
14. let a confident operation failure disappear inside an aggregate pass;
15. delete accessible seed, controller, resonator, heat, or old-memory records,
    or call absence of an `S` effect global information erasure;
16. treat predictable drift as i.i.d. or compare cells on different schedules;
17. promote one bounded pass into universal Markovianity;
18. promote one bounded failure into Barandes ontology or whole-process
    necessity; and
19. call simulation, checker output, or a source paper an empirical PTS run.

---

## 13. Result vocabulary and ceiling

If a future separately authorized experiment ever exists, only the vector
`(D_M,S_B0,S_B1)` may be reported. Scoped interpretations are:

| result | maximum bounded interpretation |
|---|---|
| `S_B0=PASS` | the fresh `S` screens the registered pasts under all registered futures |
| `S_B0=FAIL`, `D_M=PASS`, `S_B1=PASS` | the evidenced `M` closes the tested non-Markovianity with `S` |
| `D_M=PASS`, `S_B1=FAIL` | operationally matched `S+M` leaves residual history dependence; an unresolved boundary coordinate, another carrier, or a non-cut description is needed at this scope |
| `D_M=FAIL` | the complete registered M-descent bundle fails; the exact reason must be printed |
| boundary mismatch | the intended fixed-boundary comparison was not instantiated |
| any underdetermined coordinate | the design cannot decide that coordinate at the frozen resolution |

No result says:

- all physical dynamics is or is not Markovian;
- a larger physical boundary cannot exist;
- Barandes is selected or refuted;
- Hilbert space is or is not ontic;
- a universal ontology, chronology, spacetime, gravity, or unification law has
  been found.

---

## 14. Author-side claim set

PTS-0 submits no official claim for independent review. Its author-side design
statements are:

- `PTS0-A1` — memory causal descent and boundary sufficiency are different
  estimands and different report coordinates;
- `PTS0-A2` — `B0` uses memory-different/equal-S histories, while `B1` uses
  boundary-equal/history-different natural preparations;
- `PTS0-A3` — full-candidate reset cannot score natural sufficiency;
- `PTS0-A4` — all issued attempts map to one of 32 primary cells while raw
  physical records remain retained;
- `PTS0-A5` — the boundary and memory classifiers are total on their declared
  finite domains and explicitly route empty confidence sets;
- `PTS0-A6` — the full simplex and physical witness modes make both interior
  power regions nonempty;
- `PTS0-A7` — 103,936 attempts per cell give the printed distribution-free
  simultaneous schedule-average bound over 148 cell laws;
- `PTS0-A8` — predictable drift and cross-run dependence do not require an
  i.i.d. fiction, while causal confounding and carryover still fail closed;
- `PTS0-A9` — the design has an apparatus-scoped ceiling and creates no
  physical, ontological, chronological, spacetime, gravity, or unification
  result.

These are author-side statements only. They are not independently accepted.

---

## 15. Present state and stopping rule

```text
PTS-0 AUTHOR DESIGN:          WRITTEN
PTS-0 EXECUTABLE CHECKER:     PASS AUTHOR-SIDE
PTS-0 AUTHOR AUDIT:           COMPLETE PASS-WITH-SCOPE
IMMUTABLE PIN:                NOT AUTHORIZED / ABSENT
INDEPENDENT REVIEW:           NOT AUTHORIZED / NOT BEGUN
DEVICE/RUN PACKET:            ABSENT
APPARATUS ACQUISITION:        NOT AUTHORIZED / NOT BEGUN
EMPIRICAL RESULT:             NONE
AUTOMATIC SUCCESSOR:          FORBIDDEN
```

PTS-0 stops after its author-side semantic/power audit. Pin creation, review,
apparatus construction, acquisition, threshold revision, or a PTS-1 unit
requires new explicit authority.
