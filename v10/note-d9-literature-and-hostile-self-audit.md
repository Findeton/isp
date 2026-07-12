# D9 literature comparison and hostile self-audit

**Date:** 2026-07-11.  This audit was written after the packet and anti-tuning
protocol were frozen and after the blind holdout returned
`REFUTED-ONE-COUPLING`.

## 1. Literature comparison

### 1.1 Bell saturation and self-testing

Mayers and Yao showed that a specified family of Bell-type probability tables
can identify a Bell source and local measurements up to local isomorphism:

- D. Mayers and A. Yao, [Self testing quantum
  apparatus](https://arxiv.org/abs/quant-ph/0307205), 2004.

McKague, Yang, and Scarani showed robust self-testing near the Tsirelson bound:

- M. McKague, T. H. Yang, and V. Scarani, [Robust Self Testing of the
  Singlet](https://arxiv.org/abs/1203.2976), 2012.

These results support D9's claim that maximal/near-maximal Bell records constrain
the EPR state and measurement observables up to local isometry.  They do **not**
identify a unique source circuit.  A partial-iSWAP, Hadamard/CNOT, or another
locally equivalent preparation can produce the same record statistics.

Therefore D9 identifies `theta=pi/4` only inside its frozen one-partial-iSWAP
model family.  It does not device-independently prove that nature implements
that microscopic gate.

### 1.2 Process tomography

Unitary and low-Kraus-rank channels can be identified with reduced measurement
resources when their model class is supplied:

- G. Gutoski and N. Johnston, [Process tomography for unitary quantum
  channels](https://arxiv.org/abs/1309.0840), 2013.
- M. Branderhorst et al., [Simplified Quantum Process
  Tomography](https://arxiv.org/abs/0910.4609), 2009.
- S. Ahmed, F. Quijandria, and A. F. Kockum, [Gradient-descent quantum process
  tomography by learning Kraus operators](https://arxiv.org/abs/2208.00812),
  2022.

D9's finite reconstruction is much narrower: in a fixed real-qubit gauge with
the source correlation tensor and Alice axes declared, the four correlators
recover Bob's two planar unit vectors.  It is a correct model-relative
tomography receipt, not general black-box Kraus reconstruction.

## 2. Hostile openings

### Opening 1 — “Bell data derive the partial-iSWAP gate”

**Rejected.**  Bell self-testing determines the state/measurements up to local
isometry, not the preparation circuit.  Paper language must say:

```text
within the one-partial-iSWAP packet, maximal Bell entanglement fixes theta;
the packet family itself is a hypothesis.
```

### Opening 2 — measurement independence

SCIR's independent fair setting tokens enforce
`P(x,y|source)=P(x)P(y)` by construction.  Bell/no-signalling data alone do not
derive this independence.  It is a declared operational condition and a
falsifiable record-factorization assumption.

### Opening 3 — incomplete context test

The exact attack changes one remote-context correlator and is detected because
the inferred `B0` vector has norm squared `3/4`.  This does not prove that all
possible contextual devices are detected by four CHSH contexts.  General
device tomography needs additional probes.  The valid claim is that one fixed
packet fits all four frozen contexts and the exhibited drift attack fails.

### Opening 4 — unjustified Bell-to-geometry coupling identity

Correct: the equality

$$
g_{geometry}=\sin^2\theta_{Bell}
$$

is not derived by SCIR, quantum theory, or the literature.  D9 froze it as the
strongest one-coupling hypothesis precisely to make a risky prediction.  The
holdout refuted it.  No post-hoc replacement by `g=0.18` is allowed.

### Opening 5 — corrected dimension is still a proxy

The new instrument passed a real prerequisite: on synthetic latent dimensions
2–6 with injected scale drift, it recovered all dimensions within the frozen
tolerance, while the legacy ruler drove true `d=4` controls to the `d=6`
ceiling.  However, the calibration ensemble is iid ballistic confetti and the
web is correlated growth.  Therefore `d=2.7087` is a validated
drift-corrected **volume proxy**, not a theorem assigning manifold dimension.

The negative result does not depend only on that proxy.  At `g=1/2`:

```text
F_dom is above its line at +3.15 SE;
F_dom worsens by +2.54 SE from N=2048 to 8192;
F_m4 worsens by +4.18 SE;
the corrected proxy falls from 2.73 to about 2.19.
```

Thus multiple independent legs reject the frozen cross-domain identification.

### Opening 6 — structural dimension witnesses contradict d about 2.7

No contradiction.  `S4` proves order dimension at least four.  The corrected
relation fraction estimates continuum volume behavior.  Finite-facet or
growth-correlated orders can have high order dimension while their volume
scaling is unlike a four-dimensional sprinkling.  V9 already established this
separation.

### Opening 7 — full influence spread is a success

Yes, but insufficient.  The marked perturbation reaches all 32 slots in all
three paired runs.  SCIR's local transfer does create collective coupling.
The coupling strength is nevertheless too large for the desired geometric
universality class under the tested mapping.

## 3. Robust conclusion

The strongest defensible result is:

```text
EXACT-BELL-PACKET-PASS
+ GAUGE-RELATIVE-TOMOGRAPHY-PASS
+ DRIFT-INSTRUMENT-VALIDATED-ON-SYNTHETICS
+ BELL-FROZEN-g=1/2
+ FULL-INFLUENCE-COUPLING
+ GEOMETRY-AND-SCALE-HOLDOUT-FAIL
= REFUTED-ONE-COUPLING
```

This does not refute the SCIR rulebook architecture.  It proves that the
smallest identification was too strong.  A viable SCIR theory requires at
least one of:

1. distinct matter-entanglement and pregeometric-transfer couplings;
2. a derived coarse-graining/RG map from `theta` to a smaller effective `g`;
3. a different microscopic transfer rule whose diagonal shadow is not
   `sin^2(theta)`;
4. rejection of the V9 diffusion builder as the SCIR geometric shadow.

Choosing among these is a new physical question.  D9 does not open a tuning
sweep after the holdout.

