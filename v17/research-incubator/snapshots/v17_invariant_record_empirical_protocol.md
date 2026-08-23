# PRIVATE EMPIRICAL PROTOCOL — invariant relational records

Date: 2026-08-23

Status: **PRIVATE / OFF-TREE / NO PLATFORM SELECTED / NO DATA**

This protocol translates the private invariant-record theorem package into a
falsifiable laboratory programme. It does not reopen Paper 04, authorize a
successor, select a native ontology, or test gravity. Every ideal prediction below
is ordinary finite-dimensional quantum mechanics. The scientific purpose is to
test the record typing, resource accounting, and architecture discriminators on
real apparatus rather than letting them remain formal conveniences.

## 1. Experimental question

Can one physical apparatus:

1. form a classical record of an invariant relational bit;
2. preserve coherence between alternatives carrying the same recorded value;
3. lose that coherence when a noninvariant raw coordinate is recorded;
4. recover it when the raw interaction is coherently reversed before
   amplification;
5. expose the roles of quantum memory, controller classicalization, and a physical
   reference through independent interventions; and
6. create redundantly readable output fragments without calling agreement an
   actualization or division theorem?

The primary object is the complete instrument and its later-reader behavior, not
one terminal truth table.

## 2. Logical carrier

Use system qubits $(q,a,b)$ and record qubit $r$. Optional fragment qubits are
$f_1,f_2$. The registered physical symmetry is

$$
U_g=\operatorname{CNOT}_{q\to a}X_b,
$$

and the invariant is

$$
y=a\oplus qb.
$$

The invariant premeasurement is

$$
V_y=\operatorname{TOFFOLI}_{q,b\to r}
    \operatorname{CNOT}_{a\to r}.
$$

The order convention is frozen as written, although these two controlled flips
commute on the computational basis. A hardware decomposition must retain a full
phase-aware process model; matching the classical truth table is insufficient.

Define

$$
|\phi_0\rangle=\frac{|000\rangle+|111\rangle}{\sqrt2},
\qquad
|\phi_1\rangle=\frac{|010\rangle+|101\rangle}{\sqrt2},
$$

and

$$
|\Psi_\pm\rangle
=\frac{|\phi_0\rangle\pm|\phi_1\rangle}{\sqrt2}.
$$

The full source is $|\Psi_+\rangle$. The source is asymmetric under $U_g$ and is
therefore a declared preparation/reference resource, not a gauge-invariant vacuum.

## 3. Three experimental tiers

### Tier A — coherent terminal calibration

Requires four coherent qubits, arbitrary final-basis measurement, and the inverse
of every registered gate. It tests source preparation, $U_g$, $V_y$, raw recording,
coherent erasure, and the incompatible quantum-memory reader. It does not earn an
operational classical record because no post-record future is tested.

### Tier B — retained instrument

Adds a genuine mid-circuit record operation with the system retained, followed by
registered future readers. It tests the complete classical and quantum outputs of
the instrument, not merely readout fidelity. This tier can earn a scoped
operational classical-record coordinate.

### Tier C — redundant objective output

Adds at least two independently addressable fragment carriers, sequential or
spacelike-separated read controls within the supplied laboratory description, and
later disturbance tests. It can earn a scoped operational broadcast coordinate.
It cannot earn native actuality, a Barandes conditioning division, strong
screening, chronology, or spacetime.

## 4. Frozen experimental arms

### E0 — preparation and gate calibration

Tomographically or witness-validate $|\phi_0\rangle$, $|\phi_1\rangle$,
$|\Psi_+\rangle$, $U_g$, and $V_y$. Estimate coherent phases, leakage, crosstalk,
and target disturbance. This arm fixes the noise model on calibration data only.

### E1 — invariant within-fiber record

For each independently prepared $|\phi_y\rangle$, apply $V_y$, expose the $Z_r$
record as required by the tier, and apply the complete reader
$F_y^+=|\phi_y\rangle\langle\phi_y|$ to the retained system.

Ideal prediction:

$$
p_{\rm inv}^{(y)}
=\Pr(F_y^+\mid r=y,\phi_y)=1.
$$

The event $r=y$ must not be postselected away when record errors occur. Report the
joint distribution, the unconditional success probability, and the conditional
reader probability with its support.

### E2 — invariant cross-fiber record

Prepare $|\Psi_+\rangle$, apply $V_y$, take the complete nonselective $Z_r$
output, and read $|\Psi_+\rangle\langle\Psi_+|$ on the system.

Ideal prediction:

$$
p_{\rm cross}=\frac12.
$$

This is the required negative control: a purported record that preserves all
cross-fiber coherence is only an incomplete premeasurement.

### E3 — raw-coordinate record

Prepare $|\phi_y\rangle$ separately for $y=0,1$. Copy $a$ into $r$, take the
complete nonselective $Z_r$ output, and apply $F_y^+$. The label $y$ is preparation
provenance, not a simultaneous postselected measurement.

Ideal prediction:

$$
p_{\rm raw}^{(y)}=\frac12.
$$

### E4 — coherent raw eraser

Prepare $|\phi_y\rangle$, coherently copy $a$ into $r$, apply the exact inverse
before amplification, verify that $r$ returned to its ready state, and apply
$F_y^+$.

Ideal prediction:

$$
p_{\rm erase}^{(y)}=1.
$$

This is an uncomputation result, not evidence that an already amplified classical
fact was destroyed.

### E5 — quantum-memory reader

Prepare $|\Psi_+\rangle$ and apply coherent $V_y$ without $Z_r$ amplification.
Measure $r$ in the $X$ basis. Conditional on outcome $s\in\{+,-\}$, apply the
reader $|\Psi_s\rangle\langle\Psi_s|$.

Ideal prediction:

$$
\Pr(\Psi_s\mid X_r=s)=1.
$$

Repeat after an explicit $Z_r$ dephasing channel with its environment and discarded
or inaccessible output printed. The conditional phase-reader success on $r$ and
the system then becomes

$$
\Pr(\Psi_s\mid X_r=s,\mathcal D_{Z_r})=\frac12.
$$

The contrast tests coherent memory versus a dephased negative control. It does not
by itself prove that the dephased boundary is a complete classical record; that
requires the Tier B all-reader and central-output tests. It also does not make the
memory algebra fundamental.

### E6 — controller-classicalization control

Dephase $q$ in its computational basis before $V_y$ while preparing
$|\phi_y\rangle$. Apply the invariant record and $F_y^+$.

Ideal prediction:

$$
p_{\rm C}^{(y)}=\frac12.
$$

This arm must expose the physical dephasing channel or environment. Uncontrolled
phase drift may not be relabeled superselection.

### E7 — physical-reference intervention

Run two paired interventions.

1. Apply the full joint transformation $U_g$ and transport the source reader with
   it. The invariant output is unchanged.
2. Apply $X_b$ alone before $V_y$. For either $|\phi_y\rangle$, the two coherent
   alternatives then carry opposite invariant values, so the ideal $r$ distribution
   is uniform.

The first arm tests covariance; the second proves that $b$ is a physical reference
resource entering the relation. Neither arm promotes the registered symmetry to a
fundamental gauge symmetry.

### E8 — redundant fragments

After $V_y$, copy the orthogonal $Z_r$ label to $f_1$ and $f_2$. At Tier C, use a
complete instrument or an explicitly inaccessible orthogonal register so the
accessible output is classical. Test:

- $Z_{f_1}=Z_{f_2}=Z_r$ agreement;
- independent addressability rather than aliases of one readout channel;
- both read orders;
- later $F_y^+$ behavior before and after each fragment read;
- leakage of $q$ or raw $a$ into any fragment;
- the global coherent control in which amplification is omitted.

Terminal three-bit agreement alone does not establish objective broadcasting.

### E9 — adaptive endpoint transcript

Program a physical controller to choose a later reader from an earlier apparatus
record. Carry the policy label, earlier record, chosen setting, later outcome, and
controller memory into the final transcript. Compare the complete endpoint law
with the operational quantum-instrument prediction.

This is not a stochastic restart and assigns no probability to unrecorded native
intermediate configurations. If a theory claims a conditional endpoint law from
the intermediate boundary itself, that boundary requires a separately admitted
Barandes division.

### E10 — exact algebra audit

The four occupied basis configurations give:

| configuration | source fiber | raw $a$ | $y=a\oplus qb$ | $y$ after $X_b$ |
|---|---:|---:|---:|---:|
| $000$ | 0 | 0 | 0 | 0 |
| $111$ | 0 | 1 | 0 | 1 |
| $010$ | 1 | 1 | 1 | 1 |
| $101$ | 1 | 0 | 1 | 0 |

Hence each $\phi_y$ contains opposite raw-$a$ values but one invariant value,
whereas $X_b$ alone splits that invariant value. The coherent memory identity is

$$
V_y|\Psi_+\rangle|0\rangle_r
=\frac{|\phi_0\rangle|0\rangle_r
       +|\phi_1\rangle|1\rangle_r}{\sqrt2},
$$

which directly yields the E2 and E5 predictions. These identities must be
reconstructed independently from the frozen gate decomposition before any data
are opened.

## 5. Primary estimands

Predeclare at least the following quantities:

$$
\Delta_{IR}
=\frac12\sum_y\left(p_{\rm inv}^{(y)}-p_{\rm raw}^{(y)}\right),
\qquad
\Delta_{ER}
=\frac12\sum_y\left(p_{\rm erase}^{(y)}-p_{\rm raw}^{(y)}\right),
$$

$$
\Delta_{IE}
=\frac12\sum_y\left(p_{\rm inv}^{(y)}-p_{\rm erase}^{(y)}\right),
$$

plus:

- $p_{\rm cross}$;
- the coherent-memory/dephased-memory phase-reader contrast;
- the controller-classicalization contrast;
- the joint-symmetry covariance error;
- the reference-only intervention response;
- fragment disagreement and read-order disturbance;
- complete endpoint-transcript total-variation error;
- leakage and postselection rates.

The ideal vector includes

$$
\Delta_{IR}=\Delta_{ER}=\frac12,
\qquad
\Delta_{IE}=0,
\qquad
p_{\rm cross}=\frac12.
$$

Hardware results are compared with a calibration-frozen noisy-instrument model,
not only with ideal numbers.

## 6. Statistical preregistration

1. Split all shots and calibration epochs into training/calibration, validation,
   and held-out test blocks before opening the held-out outcomes.
2. Randomize arm order and blind the analysis labels where the platform permits.
3. Freeze the complete gate decomposition, pulse compiler version, measurement
   assignment correction, leakage rule, and drift exclusions before held-out data.
4. Report both raw and corrected counts. No mitigation result may replace the raw
   result.
5. Do not discard record-write failures. Any physics-conditioned statistic must
   print its denominator and the corresponding unconditional joint probability.
6. Treat leakage as an outcome in the primary analysis. A predeclared
   computational-subspace conditional analysis is secondary.
7. For $K$ bounded Bernoulli estimands, a conservative design may choose per-arm
   shots

   $$
   N\ge\frac{\log(2K/\alpha)}{2\delta^2}
   $$

   to obtain simultaneous Hoeffding half-width $\delta$ at familywise error
   $alpha$. A platform-specific power calculation may replace this only if frozen
   before held-out data.
8. Freeze equivalence margins separately from difference thresholds. Failure to
   reject a difference is not evidence of equivalence.
9. Replicate any anomaly on a separately calibrated device or platform before
   calling it a failure of the operational quantum theorem.

## 7. Noise and failure taxonomy

The registered noise model must separately expose:

- source infidelity and coherent phase error;
- one-, two-, and three-body gate errors;
- Toffoli decomposition phase errors;
- readout assignment error;
- mid-circuit backaction and residual photons/scattered light;
- controller latency and feed-forward error;
- dephasing and relaxation during the protocol;
- leakage outside the computational space;
- spectator crosstalk;
- fragment aliasing;
- reference degradation and reset;
- drift between calibration and held-out blocks.

A single aggregate circuit fidelity cannot diagnose the record theorem.

## 8. Platform feasibility

### 8.1 Trapped-ion pilot

This is the leading pilot candidate because the logical protocol benefits from
flexible connectivity, coherent multi-qubit control, retained qubits during
ancilla readout, and classical feed-forward. Direct trapped-ion Toffoli gates have
been demonstrated, as have repeated mixed-species correlation readout and
feedback, and more recent mid-circuit measurement/feed-forward many-body
protocols. The pilot must still characterize optical crosstalk, motional heating,
sympathetic recooling, and phase coherence across the eraser arm.

### 8.2 Superconducting replication

Circuit-QED platforms have demonstrated detector tomography and conditioned
process tomography for register-wide multiqubit measurements, as well as quantum-
instrument gate-set tomography for mid-circuit measurement. They are therefore a
strong independent replication route, especially for diagnosing measurement
backaction. Connectivity, coherent Toffoli decomposition, residual readout
photons, leakage, and reset/feed-forward latency must be included explicitly.

### 8.3 Neutral-atom feasibility arm

Neutral-atom arrays offer physical separation and scalable fragment carriers.
Single-site cavity-assisted mid-circuit readout with limited observed disturbance
to a remote atom has been demonstrated. A Tier C implementation would still need
validated coherent three-body logic or an exact decomposition, full fragment-read
independence, and a platform-specific process-instrument characterization. It is a
feasibility route, not the default pilot.

### 8.4 Platform nonselection

No platform is part of the mathematical theorem. A first pilot may be selected by
predeclared capability and error thresholds, not by which device happens to make
the desired contrast look strongest. Cross-platform replication is evidentially
stronger than adding more shots to one co-designed device.

## 9. Architecture dispositions

The data print the feature vector independently:

```text
I  INVARIANT-COMMUTATIVE-OUTPUT: YES | NO | UNTESTED
C  CONTROLLER-CLASSICALIZED:     YES | NO | UNTESTED
N  NONCOMMUTATIVE-MEMORY:        YES | NO | UNTESTED
R  PHYSICAL-REFERENCE-RESOURCE:  YES | NO | UNTESTED
O  OBJECTIVE-BROADCAST:          YES | NO | UNTESTED
```

- I requires covariance, correct fiber selectivity, and a complete retained
  classical output.
- C requires verified loss of controller coherence with an exposed mechanism.
- N requires an incompatible-memory or coherent-reversal witness before
  amplification.
- R requires a separating reference intervention and a resource/backreaction
  ledger.
- O requires disjoint addressability, agreement, nondisturbance, and the complete
  output structure.

These features overlap. No single label is an ontology verdict.

## 10. Result ladder

```text
L0  PLATFORM-OR-INSTRUMENT-ILL-TYPED
L1  COHERENT-CIRCUIT-CALIBRATION-FAILED
L2  INVARIANT-FIBER-PREDICTIONS-DISFAVORED
L3  OPERATIONAL-INVARIANT-RECORD-CONSTRUCTED
L4  QUANTUM-MEMORY/CLASSICAL-OUTPUT-DISCRIMINATED
L5  FINITE-REFERENCE-RESOURCE-RESPONSE-CONSTRUCTED
L6  REDUNDANT-OBJECTIVE-OUTPUT-CONSTRUCTED
```

Every rung remains operational. No rung awards:

```text
NATIVE-CONFIGURATION
NATIVE-ENDPOINT-LAW
NON-MARKOVIAN-REALIZER
NATIVE-ACTUALITY
BARANDES-DIVISION
STRONG-SCREENING
CHRONOLOGY
SPACETIME
GRAVITY
```

## 11. Primary-source routing

- [Monz et al., trapped-ion Toffoli](https://arxiv.org/abs/0804.0082): direct
  coherent three-qubit logic and process characterization; not evidence for
  fundamental discreteness.
- [Negnevitsky et al., repeated trapped-ion readout and feedback](https://arxiv.org/abs/1804.09703): retained-qubit correlation readout and conditional
  feedback; not a native division theorem.
- [Iqbal et al., trapped-ion measurement and feed-forward](https://arxiv.org/abs/2302.01917): deterministic mid-circuit measurement/feed-forward on a
  programmable ion platform; not background-free chronology.
- [Blumoff et al., multiqubit measurement characterization](https://arxiv.org/abs/1606.00817): detector tomography and conditioned process tomography for
  multiqubit measurements; not ontology selection.
- [Rudinger et al., quantum-instrument GST](https://arxiv.org/abs/2103.03008):
  instrument-level characterization of mid-circuit measurement; not a universal
  error model.
- [Deist et al., neutral-atom mid-circuit readout](https://arxiv.org/abs/2205.14138): single-site cavity readout with a remote-atom disturbance control;
  not a completed Tier C implementation.
- [Korbicz et al., spectrum broadcasting](https://arxiv.org/abs/1305.3247):
  structural criterion for redundant objective information; not actualization.

## 12. Present disposition

```text
LOGICAL-PROTOCOL:                 SPECIFIED-PRIVATELY
IDEAL-PREDICTIONS:                DERIVED-ANALYTICALLY
NOISE-MODEL:                      SCHEMA-FROZEN/PARAMETERS-UNSELECTED
PREFERRED-PILOT-CLASS:            TRAPPED-ION-CAPABILITY-MATCH
ACTUAL-HARDWARE/PARTNER:          UNSELECTED
CALIBRATION/HOLDOUT-BYTES:        NONE
DATA:                             NONE
OPERATIONAL-RESULT:               UNTESTED
ONTOLOGY:                         UNSELECTED
OFFICIAL-CYCLE:                   NOT-AUTHORIZED
```
