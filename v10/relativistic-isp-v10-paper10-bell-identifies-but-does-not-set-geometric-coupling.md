# Relativistic ISP v10 Paper 10: Bell Identifies a Minimal SCIR Packet but Does Not Set Its Geometric Coupling

## Exact partial-iSWAP histories, gauge-relative tomography, a validation-gated dimension repair, and blind refutation of the one-coupling universe

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** D9 completed anti-tuning campaign, 2026-07-11.  The minimal packet,
Bell targets, coupling identification, dimension-repair requirements, and
holdout verdicts were frozen before any D9 executable or geometry run.

**Receipts:**

- `v10/code/d9_minimal_bell_packet_exact.py` — 126/126 exact and reproducible
  finite-sample checks;
- `v10/code/d9_drift_matched_dimension.py` — 21/21 validation gates on
  synthetic latent dimensions 2–6;
- `v10/code/d9_frozen_packet_geometry.py` — 24-seed primary holdout, three
  influence pairs, and a 12-seed-per-rung scale ladder at `N=2048,4096,8192`.

## Abstract

V10 Paper 9 supplied a complete local quantum record rulebook but left its
finite grammar and couplings as primitive physics.  This paper performs the
next test: identify the smallest fully numeric SCIR packet from quantum data,
freeze it, and ask whether the same coupling predicts the V9 spacetime
geometry without tuning.

The packet has five rule types—root, two-port transfer, independent setting,
local measurement, and seal—and one continuous coupling.  Its interaction is
a partial-iSWAP `U_theta`.  In the one-excitation sector, a local output gauge
turns `U_theta|10>` into a two-qubit Bell source.  Within this frozen packet
family, maximal Bell entanglement fixes `theta=pi/4`.  The same-gate hypothesis
then predicts the classical transfer shadow

$$
g=\sin^2\theta=\frac12.
$$

Using exact arithmetic over `Q(sqrt(2),i)`, the complete setting/outcome
history law is positive and normalized, has uniform no-signalling marginals,
gives the correlator table

$$
(E_{00},E_{01},E_{10},E_{11})
=
(1,1,1,-1)/\sqrt2,
$$

and saturates CHSH at exactly `2 sqrt(2)`.  Disjoint measurement instruments
commute.  Terminal deletion recovers every setting cylinder, and independent
setting tokens factor exactly from the source.  In the declared real-qubit
gauge, the four correlators reconstruct Bob's two unit measurement vectors.
A context-dependent attack produces an exact norm defect `3/4` and is
rejected.  Reproducible 200,000-shot-per-context samples recover the frozen
coefficients within their registered tolerance.

Before examining the `g=1/2` web, D9 repairs the dimension instrument.  On
synthetic latent dimensions 2–6, scale drift matching the V9 nonstationarity
drives a true `d=4` control to the legacy estimator's `d=6` ceiling.  A local
same-window scale calibration instead returns `4.013` at 1.55-fold drift and
`4.138` at 1.94-fold drift, passing all 21 preregistered gates.

The blind geometry result refutes the one-coupling hypothesis.  On 24 fresh
`g=1/2` webs, `F_dom=1.3348 +/- 0.0313`, which lies **above** its line by
`+3.15 SE`; `F_m4=1.2393 +/- 0.0190` is also above its line, though only by
`+1.44 SE`.  The corrected volume proxy is `2.709`, not four.  All 24 webs
refuse dimension two and contain verified `S4` witnesses, showing again that
order dimension and continuum-volume behavior differ.  The perturbation
reaches all 32 slots in all three influence pairs, so coupling exists.  But
the scale ladder worsens: from `N=2048` to `8192`, `F_dom` rises by `2.54 SE`,
`F_m4` by `4.18 SE`, and the corrected proxy falls from `2.73` to `2.19`.

The conclusion is narrow and strong.  SCIR is not refuted.  The identification
of one microscopic coupling as both the Bell entangler and geometric diffusion
strength is refuted.  A viable theory needs distinct couplings, a derived
renormalization map to a smaller effective geometric coupling, a different
classical shadow, or a different geometry builder.  No post-hoc `g` sweep is
performed.

## 1. Question and anti-tuning design

Paper 9's finite SCIR packet is analogous to a Lagrangian: the generative
rules are complete, while interaction types and couplings must be specified.
D9 asks whether the smallest possible identification is viable:

> Can one two-port quantum coupling explain both Bell entanglement and the
> gentle record transfer that generated the best V9 cones?

The identification data contain no cone measurements.  The frozen sequence is:

```text
Bell tables -> theta -> g_shadow -> geometry holdout.
```

The reverse path is forbidden.  In particular, the previously favorable
`g=0.18` cannot replace the Bell prediction.

## 2. Fully numeric five-rule packet

### 2.1 Grammar

The packet contains:

1. `ROOT`: create a two-port one-excitation state;
2. `TRANSFER`: apply the partial-iSWAP coupling;
3. `SETTING`: independently create fair local setting records `x,y`;
4. `MEASURE`: apply the setting-indexed local projector instrument;
5. `SEAL`: commit a durable `+/-` pointer record.

Identity propagation contains no new parameter.

### 2.2 Source gate

On basis states `|01>,|10>`,

$$
U_\theta=
\begin{pmatrix}
\cos\theta&i\sin\theta\\
i\sin\theta&\cos\theta
\end{pmatrix}.
$$

At `theta=pi/4`, acting on `|10>` gives equal amplitudes.  A fixed local phase
and bit gauge on Bob's port maps the result exactly to

$$
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2}.
$$

The exact receipt verifies both the partial-iSWAP unitarity and this local
gauge equivalence.

### 2.3 Measurements

Use

$$
A_0=Z,
\qquad A_1=X,
$$

$$
B_0=(Z+X)/\sqrt2,
\qquad
B_1=(Z-X)/\sqrt2.
$$

For outcome `a=+/-1`, the local projector is

$$
P_{a|x}=\frac{I+aA_x}{2},
$$

and likewise for Bob.  All four observables are exactly Hermitian involutions.

## 3. Complete Bell history law

Independent setting tokens give

$$
P(x,y)=\frac14.
$$

The sealed conditional law is

$$
P(a,b|x,y)
=
\operatorname{tr}
\left[
(P_{a|x}\otimes P_{b|y})
|\Phi^+\rangle\langle\Phi^+|
\right].
$$

Therefore the full committed history probability is

$$
P(x,y,a,b)=\frac14P(a,b|x,y).
$$

The 16 full cells sum exactly to one.  Summing over terminal outcomes gives
`P(x,y)=1/4`, so the Bell history is a projective SCIR cylinder family rather
than an isolated correlation table.

## 4. Exact quantum gates

The exact algebraic receipt establishes:

```text
partial-iSWAP unitarity;
Bell-source purity and normalization;
all 16 conditional cells nonnegative;
all four conditional rows normalized;
uniform local marginals under every remote setting;
independent setting/source factorization;
commutation of all disjoint A/B outcome projectors;
terminal-cylinder deletion;
exact CHSH 2 sqrt(2);
the CHSH polynomial lambda(lambda^2-8)=0;
all deterministic local assignments at |S|=2;
a product-state quantum control below 2.
```

This is a complete finite Bell experiment generated by the SCIR packet.

## 5. What tomography identifies

For `Phi+`, with Alice fixing the `Z/X` gauge, the planar source correlation
tensor is the identity.  If

$$
B_y=b_{yZ}Z+b_{yX}X,
$$

then

$$
E_{0y}=b_{yZ},
\qquad
E_{1y}=b_{yX}.
$$

The record table therefore reconstructs

$$
B_0=(Z+X)/\sqrt2,
\qquad
B_1=(Z-X)/\sqrt2
$$

exactly, with unit coefficient norms.  A synthetic context attack changing
only `E00` to `1/2` reconstructs a supposed `B0` with norm squared `3/4` and is
incompatible with one fixed projective instrument.

This identification is deliberately narrow.  Bell self-testing literature
shows that ideal or near-ideal correlations constrain an EPR pair and local
measurements up to local isometry—see [Mayers–Yao](https://arxiv.org/abs/quant-ph/0307205)
and [McKague–Yang–Scarani](https://arxiv.org/abs/1203.2976).  It does not select
a unique preparation circuit.  D9 fixes `theta` only within the declared
one-partial-iSWAP family.

Likewise, the receipt is a fixed-model coefficient tomography, not arbitrary
Kraus-process tomography.  General unitary/low-rank process tomography exists
with explicit identifiability assumptions, for example
[Gutoski–Johnston](https://arxiv.org/abs/1309.0840).

## 6. Frozen cross-domain prediction

The one-coupling hypothesis identifies the partial-transfer probability with
the diagonal shadow of the same gate:

$$
g_{\rm shadow}=\sin^2\theta.
$$

Bell saturation inside the packet fixes

$$
\theta=\frac\pi4
\quad\Longrightarrow\quad
g_{\rm shadow}=\frac12.
$$

This is the only downstream coupling tested.  The equality is an explicit
physical conjecture, not a theorem of SCIR.

## 7. Repairing the dimension ruler

### 7.1 Failure mechanism

The V9 legacy instrument calibrates

$$
\tau\propto\frac{s_D}{s_b}
$$

in the first quarter of the history and applies it to a later dimension
window.  If the content/dipole scale grows, the later relation uses a ruler
calibrated on a smaller object.

### 7.2 Matched instrument

D9 estimates `tau` on the same retained window whose relation fraction is
measured.  Before any `g=1/2` web is read, the method is calibrated on
stationary synthetic latent dimensions `d=2..6` and tested on 24 fresh seeds
per dimension under scale ratios `1`, `1.55`, and `1.94`.

For true `d=4`:

| injected drift | legacy reading | matched reading |
|---:|---:|---:|
| `1.00` | `4.140` | `4.008` |
| `1.55` | `6.000` ceiling | `4.013` |
| `1.94` | `6.000` ceiling | `4.138` |

All latent dimensions pass the frozen `0.35` recovery tolerance.  The matched
number remains a volume proxy because correlated growth is not iid confetti,
but the specific scale-mismatch failure is repaired.

## 8. Blind `g=1/2` holdout

### 8.1 Primary 24-seed result

The SHA-256-pinned V9 diffusion builder is changed only at the pre-frozen
coupling/seed tuple.  It returns:

| leg | result | reading |
|---|---:|---:|
| `F_dom` | `1.3348007 +/- 0.0313421` | `t=+3.152` above line |
| `F_m4` | `1.2393044 +/- 0.0189780` | `t=+1.439` above line |
| corrected relation fraction | `0.1605202` | — |
| corrected volume proxy | `2.7087302` | outside 4D band |
| observed scale drift | `1.7741` | nonstationary |
| dimension-2 refusals | `24/24` | pass structural lower bound |
| verified `S4` | `24/24` | pass structural lower bound |

The strict roundness conjunction fails.  The corrected volume proxy is not
close to four.

### 8.2 Influence

The paired marked-world experiment reaches all 32 slots in all three runs.
Thus the frozen transfer is not free or disconnected.  It creates collective
influence, but at the wrong strength for the tested geometric class.

### 8.3 Scale ladder

With no parameter changes:

| `N` | `F_dom` | `F_m4` | corrected `d` | drift |
|---:|---:|---:|---:|---:|
| `2048` | `1.3711` | `1.2536` | `2.7338` | `1.756` |
| `4096` | `1.5585` | `1.3919` | `2.1997` | `2.584` |
| `8192` | `1.6782` | `1.4873` | `2.1898` | `2.566` |

The `N=2048 -> 8192` worsening is `+2.54 SE` under `dom` and `+4.18 SE` under
`m4`.  This is the opposite of the desired collective averaging prediction.

## 9. Verdict

The registered verdict is

```text
REFUTED-ONE-COUPLING.
```

The refuted statement is:

> The same microscopic partial-iSWAP angle that produces maximal Bell
> entanglement directly supplies the V9 pregeometric diffusion fraction.

The following remain intact:

```text
SCIR as a complete local rulebook architecture;
the exact Bell packet;
Born/no-signalling/concurrency/projectivity;
the existence of conservative local diffusion shadows;
the need for collective coupling;
the drift-matched synthetic instrument validation.
```

## 10. Physical consequence

A viable SCIR theory now requires at least one additional distinction:

1. a matter/entanglement coupling and a separate geometric-transfer coupling;
2. a renormalization map
   `g_effective = R(theta, scale, state)` that makes the macroscopic transfer
   substantially smaller than `sin^2(theta)`;
3. a different local transfer channel whose diagonal shadow is not the raw
   partial-swap probability;
4. a different geometric builder.

This is not an invitation to tune `g`.  The next candidate must state the
distinction or RG map before seeing new geometry data and must make another
cross-domain holdout prediction.

## 11. Final boundary

```text
MINIMAL-NUMERIC-SCIR-BELL-PACKET-FOUND
+ EXACT-BORN-TSIRELSON-NOSIGNALLING
+ GAUGE-RELATIVE-TOMOGRAPHY
+ THETA-PI/4-WITHIN-PARTIAL-ISWAP-FAMILY
+ G-SHADOW-1/2-FROZEN-BEFORE-GEOMETRY
+ DRIFT-MATCHED-DIMENSION-CONTROL-PASS
+ FULL-INFLUENCE-COUPLING
+ SHAPE-DIMENSION-SCALE-HOLDOUT-FAIL
= REFUTED-ONE-COUPLING
+ SCIR-NOT-REFUTED
```

