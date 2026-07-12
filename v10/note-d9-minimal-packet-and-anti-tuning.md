# D9 — minimal numeric SCIR packet, tomography, and anti-tuning protocol

**Status:** frozen before D9 executables, literature search, or geometry runs,
2026-07-11.

## 1. Objective

D8 supplied a complete rulebook architecture but left the finite local
interaction packet primitive.  D9 asks whether one smallest fully numeric
packet can be identified from quantum records and then predict geometry
without retuning.

The campaign separates:

```text
identification data:
  finite Bell histories only;

frozen microscopic packet:
  source gate, local measurement instruments, and one coupling;

holdout predictions:
  conservative transfer strength, V9 shape, dimension, scale, influence.
```

No cone or dimension result may change the frozen packet.

## 2. Minimal packet

The port state is one real/complex qubit.  The grammar has exactly five
physical rewrite types:

```text
ROOT       : empty -> one excitation carried by two output ports;
TRANSFER   : two-port partial-iSWAP U_theta;
SETTING    : independent local fair setting record x or y;
MEASURE    : local two-outcome projective instrument;
SEAL       : pointer outcome -> durable +/- record.
```

Propagation without interaction is identity and is not counted as a separate
coupling.

### 2.1 One-coupling hypothesis

On the one-excitation sector,

$$
U_\theta|10\rangle
=
\cos\theta|10\rangle+i\sin\theta|01\rangle,
$$

with the inverse rotation on `|01>`.  The same `theta` controls:

1. source entanglement in the Bell experiment;
2. the classical diagonal transfer shadow
   `g=sin^2(theta)` used downstream.

This identification is a strong physical hypothesis, not a consequence of
SCIR.  It is frozen because it creates a real cross-domain prediction.

### 2.2 Bell identification target

Maximal CHSH requires a maximally entangled source in this packet, fixing

$$
\theta=\frac\pi4,
\qquad
g=\sin^2\theta=\frac12.
$$

The source phase `i` is removable by a local port gauge.  Use the equivalent
real Bell state for probability calculations.

The local observables are frozen as

$$
A_0=Z,
\qquad A_1=X,
$$

$$
B_0=\frac{Z+X}{\sqrt2},
\qquad
B_1=\frac{Z-X}{\sqrt2}.
$$

For the `Phi+` gauge, the expected correlators are

$$
E_{00}=E_{01}=E_{10}=\frac1{\sqrt2},
\qquad
E_{11}=-\frac1{\sqrt2},
$$

and

$$
S=E_{00}+E_{01}+E_{10}-E_{11}=2\sqrt2.
$$

Settings are produced by independent fair local tokens after source creation.
Measurement independence is part of this operational packet and must be
tested as a record factorization, not inferred from no-signalling.

## 3. Exact Bell gates

The fully numeric packet must pass:

1. every setting pair has probability `1/4`;
2. every setting-conditioned outcome table is normalized and nonnegative;
3. both local marginals are exactly uniform for all remote settings;
4. the correlator table is the frozen table above;
5. CHSH is exactly `2 sqrt(2)`;
6. the Tsirelson operator identity gives norm bound `2 sqrt(2)`;
7. the `A` and `B` instruments commute exactly on disjoint ports;
8. terminal outcome deletion recovers the setting cylinder;
9. source-setting factorization holds exactly;
10. a product-state/control packet cannot exceed the classical bound.

Calculations should use exact algebraic arithmetic in `Q(sqrt(2))` where
possible and at least 100 decimal digits for trigonometric cross-checks.

## 4. Tomography and context-independence gates

The point of tomography is not merely to reproduce probabilities.  It must
show that one packet works in all four contexts.

Within the declared minimal real-qubit gauge:

```text
source T_XZ = identity correlation tensor;
A0 and A1 define the Z/X gauge;
B_y = b_yZ Z + b_yX X;
```

the two correlators involving each `B_y` reconstruct its coefficient vector.
The required results are:

$$
b_0=(1/\sqrt2,1/\sqrt2),
\qquad
b_1=(1/\sqrt2,-1/\sqrt2),
$$

up to the frozen coefficient ordering.

Tomography gates:

1. exact recovery of all four coefficients;
2. unit norm of both reconstructed observables;
3. one `B_y` reconstruction shared across both remote `x` contexts;
4. source state positive and normalized;
5. synthetic finite-sample recovery with uncertainty coverage;
6. a context-dependent remote-instrument attack must be detected;
7. a source/measurement gauge transform may change matrices but not records;
8. no full-history lookup: parameter count remains fixed as samples grow.

The claim is gauge-relative identifiability, not absolute Hilbert-space
ontology.  Saturating CHSH may later be compared with device-independent
self-testing literature.

## 5. Parameter freeze

If the exact Bell and tomography gates pass, freeze:

```text
theta = pi/4;
g_shadow = 1/2;
the five-rule grammar;
the four local measurement observables;
the unit-exponential SCIR seal clock.
```

No downstream result may replace `g=1/2` by V9's favorable `g=0.18`.

If the `g=1/2` geometry fails, the **one-coupling identification** fails.  It
does not by itself refute SCIR with distinct matter and geometric couplings.

## 6. Geometry protocol

### 6.1 Instrument repair before grading

The old dimension proxy is nonstationary because it calibrates `tau` on an
early content scale and measures a later, larger scale.  D9 must:

1. build synthetic latent dimensions `d=2..6` through the identical relation
   and subsampling pipeline;
2. inject known time-dependent spatial/content scale drift;
3. show that the legacy estimator moves under drift;
4. construct a local/drift-matched calibration;
5. recover the known synthetic dimension within a frozen tolerance before
   looking at the `g=1/2` web;
6. report ambiguity rather than choose the favorable convention.

### 6.2 Frozen-packet holdout

Run at least 24 fresh seeds at `g=1/2`.  Report both shape conventions, strict
`t <= -2.33` shape bars, dimension refusals, `S4` witnesses, corrected
dimension, influence spread, and scale behavior.  The geometry verdict is:

```text
SUPPORTED:
  both shape conventions pass, corrected dimension is in its frozen 4D band,
  witnesses pass, and no scale reversal occurs;

MIXED:
  some independent legs pass and some fail;

REFUTED-ONE-COUPLING:
  corrected dimension/shape decisively exits the target or the scale trend
  worsens under the frozen packet.
```

## 7. Claim ceiling

A positive result identifies one minimal effective packet, not the Standard
Model or Newton's `G`.  A negative result is scientifically useful: it shows
that the Bell entangling coupling cannot also be the geometric diffusion
coupling in this simplest mapping.

