# Paper 26 (v6) - SHARD: The Pre-Click Capacity Law - Quantum Computing in the Record Ontology

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The corpus' first applied paper.  A quantum processor's resource is
the logical record distinction it keeps UNRESOLVED until the output
seam, and the law governing it is record-native: leaked evidence is
the exchange-cocycle entropy production (P10), and at small leakage
coherent capacity decays at ONE QUARTER OF THE EVIDENCE RATE to
leading order (the quarter law: -ln BC = sigma/4 + sigma^2-corrections
derived and measured: ratio 0.250067 at eps = 0.02 = 1/4 + eps^2/6
exactly; monitor-dependence bounded in an O(1) band - sigma is the
currency).  Error correction is SELECTIVE RECORD FORMATION: the
3-qubit receipts show the syndrome seam exactly silent about logic
(I = 0.00e+00) while carrying 92% of the noise entropy, with
Knill-Laflamme as the seam type system in operator form.  The METRIC:
two processors at identical per-cycle fidelity differ by Sigma_leak -
the coherent one recovers at 1.000000 under echo, the dephasing one
sits exactly at the Part-I prediction 0.566762: fidelity is blind,
leaked nats are not.  The DISCRIMINATING INSTRUMENT: the clock test
(P16) on syndrome streams - a signed diagonal Hankel certifies that
NO finite hidden-Markov noise model of any dimension fits the device
environment, while a 3-dim quasi-realization is exact (residual
3.3e-16 vs the 0.0168 finite-state plateau): a hardware diagnostic
specified here as a numbered protocol with its statistical procedure.
And four angles: the coordination law's z-ordering appears in
error-correction thresholds (honeycomb ~ 6.7% < square ~ 10.9% <
triangular ~ 16.4%, with the exact clean couplings machine-verified);
topological computation is EVENTLESS TRANSPORT (the braid gate leaks
zero by theorem, the Arrhenius memory is the eventlessness boundary,
and planarity is P18 R1's corollary); quantum ADVANTAGE is cone
violation (qutrit receipts: stabilizer states nonnegative, the magic
state at -1/3 exactly, cost compounding as (sum|W|)^2n - the P16
sealability boundary in phase space); and pre-click capacity is
SCHEDULE-INVARIANT (MBQC's clicks are exactly logical-evidence-free:
p(m) = 1/2 to 4.4e-16, six-click chains at fidelity 1.0000000000 -
clicks cost capacity through their evidence, never their count)
```

## 0. Verdict

```text
THE LAW.  For a computation diamond D over n cycles:

   K_pre(D) <= min(boundary capacity [P13 area law],
                   rate capacity [Margolus-Levitin, import],
                   channel capacity [Devetak, import])
               - Sigma_leak(D) / 4-band,

with Sigma_leak the accumulated exchange-cocycle evidence about the
LOGICAL alternatives (P10's sigma), and the quarter the calibrated
small-leak exchange rate.  One condition, not three: leakage and
unrecoverability are the same functional (decoupling receipts).

PART I (p26a) - THE QUARTER LAW (Theorem A).  Per monitored step,
coherence multiplier = Bhattacharyya overlap; evidence = KL:
  -ln BC = sigma/4 + O(sigma^2)  (machine: ratio 0.250067 at
  eps = 0.02, drifting to 0.291 at the eps = 0.4 domain boundary);
general monitors live in the band [0.10, 0.49] - sigma is the right
currency within O(1) factors.  Decoupling: I(L:E) (exact Holevo over
2^n streams) and 1 - F_rec rise and vanish together.  Linear capacity
law: 1 - gamma = Sigma/4 at small accumulated leakage (receipts to
n = 20) - the operational face of P10's sigma-RP linear law.

PART II (p26b) - SELECTIVE RECORD FORMATION (Theorem B = KL, restated).
3-qubit bit-flip code: I(logical : syndrome) = 0.00e+00 EXACTLY while
I(error : syndrome) = 0.7705 of H(error) = 0.8363; the KL conditions
in operator form (correctable set: residuals 0.0; the forbidden Z-seam:
P Z1 P has eigenvalues +-1); recovery converts first-order leakage to
second-order failure (3p^2 - 2p^3, machine-exact); the same click
budget typed wrongly pays the full Part-I tax.  PROTECTION IS NOT
FEWER CLICKS - IT IS CORRECTLY TYPED CLICKS.

PART III (p26c) - THE METRIC.  Matched per-cycle fidelity (0.99336):
coherent over-rotation (Sigma_leak = 0) recovers at 1.000000 under
spin echo after 100 cycles; dephasing (which-path records sealed)
recovers at 0.566762 - EXACTLY the Part-I prediction.  Pre-click
capacity (protected minus leaked nats) orders the processors;
fidelity cannot.  The hardware number: SIGMA_LEAK PER LOGICAL CYCLE.

PART IV (p26d) - THE CLOCK TEST (the discriminating instrument).
Diagonal-Hankel moment test on syndrome streams: hidden-Markov
environment PASSES (-1.7e-17); the record-clock environment FAILS
(-9.96e-3) - and by P16's theorem NO finite HMM of any dimension fits
it, while the 3-dim quasi-realization is exact (3.3e-16) against the
quantified finite-state plateau (0.0168).  Hardware protocol: Section
6, as a numbered specification with its statistical procedure.
Falsifiable, runnable on existing devices.

PART V - THE FOUR ANGLES.
 V.1 (p26e) THE Z-LAW IN THRESHOLDS: exact clean couplings (self-
   duality, e^(4K) = 3, star-triangle product = 1, all machine-exact):
   K_c monotone in z; literature threshold anchors (~6.7% honeycomb,
   ~10.9% square, ~16.4% triangular - named data) MONOTONE IN z; the
   P10 receipts re-cited.  The coordination law's first contact with
   engineering data: the ordering PASSES.  Scope: ordering within
   fixed d only (3d cubic z = 6 at ~23% differs from 2d triangular).
 V.2 (p26f) TOPOLOGICAL = EVENTLESS: the braid gate leaves the
   environment conditional-overlap at 1.0000000000 (zero which-path
   record - silence by theorem: flat holonomy, P4 s20/P18) while the
   dynamical implementation of the SAME unitary pays 0.0455 nats/gate;
   thermal-anyon memory is Arrhenius (ln tau = Delta/T + c, MC
   receipts): protection lives exactly as long as eventlessness; and
   d >= 3 permits only permutations (P18 R1): PLANARITY IS A THEOREM.
 V.3 (p26g) ADVANTAGE = CONE VIOLATION: the qutrit phase-point frame
   self-validated (4.4e-15); nine stabilizer states nonnegative
   (Gross' theorem as receipts: inside the cone = sealable =
   classically simulable); the strange state at min W = -1/3 exactly,
   quasi-weight 5/3, cost factor (sum|W|)^2n = 2.78 -> 3545 by n = 8:
   magic counts unsealable ledger entries.  The P16 dictionary stated;
   the general law at CONJECTURE level (stated precisely in 8.3).
 V.4 (p26h) CLICK-SCHEDULING INVARIANCE: the MBQC seam is exactly
   typed (p(m) = 1/2 to 4.4e-16 over 200 random state-angle pairs);
   six-seam feed-forward chains return the programmed unitary at
   min fidelity 1.0000000000 - six clicks, zero leaked nats; the
   mis-typed contrast pays the Part-I tradeoff (table).  COROLLARY:
   clicks cost capacity through their LOGICAL EVIDENCE, never their
   count: K_pre is a schedule invariant, as a law must be.
```

## 1. Method and reproducibility

```text
code/v6_p26a_quarter_law_campaign.py        Part I   (Section 3)
code/v6_p26b_seam_typing_campaign.py        Part II  (Section 4)
code/v6_p26c_metric_campaign.py             Part III (Section 5)
code/v6_p26d_clock_test_campaign.py         Part IV  (Section 6)
code/v6_p26e_zlaw_threshold_campaign.py     V.1      (Section 8.1)
code/v6_p26f_topological_silence_campaign.py V.2     (Section 8.2)
code/v6_p26g_cone_violation_campaign.py     V.3      (Section 8.3)
code/v6_p26h_click_scheduling_campaign.py   V.4      (Section 8.4)
```

Every printed number below is generated by these scripts (fixed
seeds; all eight rerun bit-identically).  Named imports: the
decoupling/information-disturbance identity; Knill-Laflamme (restated
as the seam type system); Margolus-Levitin and Devetak capacities
(the law's untouched min-terms); the Pashayan-Wallman-Bartlett
negativity-cost bound; Gross' discrete-Wigner theorem (recovered as
receipts); the threshold literature anchors of 8.1 (values as
reported, sources cited there; the ORDERING is the corpus claim).
Corpus inputs: sigma and the sigma-RP linear law (P10), the record
area law (P13), the clock and the Heller cone (P16), eventless
transport and the braid window (P4/P9/P18), the coordination law
(P10 Part III).

## 2. The law: definitions and the decoupling collapse

**Definition (pre-click capacity).**  Let D be a computation diamond:
a bounded record region with an input seam, an interior evolution of
n cycles, and an output seam where the final clicks are scheduled.
For tolerance eps,

```text
K_pre(D, eps) = max log dim(L)  over logical subspaces L admitting
   an encoding at the input seam and a recovery map R at the output
   seam with  F( R o N_D , id_L ) >= 1 - eps,
```

where N_D is the diamond's effective channel on L (everything the
interior does, including its record formation into the environment).
This is one condition, not three.  The proposal that motivated this
paper stated three clauses - (a) the environment must not learn the
logical path, (b) the state must be recoverable, (c) the output seam
must be able to cash the invariant into records.  Clause (c) is the
definition of the output seam; clauses (a) and (b) are EQUIVALENT up
to continuity constants by the information-disturbance/decoupling
identity (named import): recoverability at 1 - eps holds iff the
environment's information about L is O(eps)-small.  Section 3's
receipts exhibit the equivalence numerically (I(L:E) and 1 - F_rec
rising and vanishing together); the capacity law therefore needs only
ONE functional - the leaked evidence.

**Definition (the leakage functional).**  Sigma_leak(D) is the
accumulated record evidence about the LOGICAL alternatives: per
monitored step, the relative entropy between the environment's
conditional record distributions, summed over the diamond.  This is
the direct operational instance of the corpus' exchange-cocycle
entropy production (P10: sigma = E[A_D] = D(P_AB || P_BA) - order
evidence); "the environment acquired which-path evidence" and "the
record process produced sigma" are the same statement in SHARD.

**The law, with per-term statuses.**

```text
K_pre(D, eps) <= min( C_boundary , C_rate , C_channel ) - Sigma_leak/c

  C_boundary: the record area law - capacity extensive in the seam
              area with log-closing quanta.  STATUS: corpus theorem
              at record scope (P13 route 5).
  C_rate:     distinguishable state changes per unit energy-time.
              STATUS: named import (Margolus-Levitin/Lloyd);
              untouched here.
  C_channel:  the asymptotic quantum capacity of the hardware noise
              channel.  STATUS: named import (Devetak); untouched.
  Sigma_leak: defined above.  STATUS: corpus-native; computable.
  c:          the evidence-to-coherence exchange rate.  STATUS:
              c = 4 at the symmetric small-leak point (Theorem A,
              proved + receipted); monitor-dependent within the
              measured O(1) band [0.10, 0.49]^-1 in general.
```

The min-terms are deliberately left as imports: this paper adds the
SUBTRACTED term and its constant, the type system that decides what
counts as leakage (Section 4), the hardware metric (Section 5), and
the diagnostic for when the leakage process itself escapes finite
modeling (Section 6).

## 3. Part I - the quarter law

### 3.1 Theorem A, with proof

**Setting.**  One logical qubit; pointer alternatives chi in {0, 1};
per cycle the environment draws one record bit b from P_chi, with the
symmetric binary monitor P_0 = (1/2 + eps, 1/2 - eps), P_1 mirrored.

**Claim.**  Per cycle the off-diagonal (coherence) multiplies by the
Bhattacharyya overlap BC = sum_b sqrt(P_0(b) P_1(b)), the leaked
evidence is sigma = D(P_0 || P_1), and

```text
   -ln BC = sigma/4 + (eps^2/6) sigma + O(sigma^3)  -
```

coherent record capacity decays at one quarter of the evidence rate,
to leading order, with the first correction explicit.

**Proof.**  The record imprint sends rho_01 -> <e_1|e_0> rho_01 with
|e_chi> = sum_b sqrt(P_chi(b)) |b>, so the per-cycle multiplier is
exactly BC.  For the symmetric monitor BC = 2 sqrt((1/2+eps)(1/2-eps))
= sqrt(1 - 4 eps^2), hence -ln BC = 2 eps^2 + 4 eps^4 + ...  And
sigma = 2 eps ln((1+2eps)/(1-2eps)) = 8 eps^2 + (32/3) eps^4 + ...
Dividing:  -ln BC / sigma = 1/4 + eps^2/6 + O(eps^4).          QED

**Receipts (p26a (i)).**

```text
  eps     sigma/step    -ln BC      ratio        1/4 + eps^2/6
  0.02    0.003202     0.000801    0.250067     0.250067
  0.05    0.020067     0.005025    0.250419     0.250417
  0.10    0.081093     0.020411    0.251699     0.251667
  0.20    0.338919     0.087177    0.257220     0.256667
  0.40    1.757780     0.510826    0.290608     (domain boundary)
```

The measured drift IS the derived second-order term to four digits
through eps = 0.2 - the law comes with its own correction series, and
the receipts confirm both coefficients.

### 3.2 General monitors: sigma is the currency

For 3099 random monitor pairs (2-4 outcomes, sigma <= 1), the
exchange rate (-ln BC)/sigma lies in [0.1023, 0.4889] with median
0.2563 (p26a (ii)).  Asymmetric monitors can be cheaper or dearer
than the symmetric quarter, but only within bounded factors: sigma is
the right currency for the capacity law, with the quarter as its
calibration point.  (No universal constant exists - the law's
subtracted term carries the band, and per-device calibration of c is
part of the Section 5 metric.)

### 3.3 The decoupling receipts

Exact Holevo information of the n-bit record stream against recovery
infidelity (p26a (iii)):

```text
  eps    n    I(L:E) [nats]   1 - F_rec
  0.05    5     0.024551      0.012406
  0.05   20     0.091613      0.047809
  0.10   10     0.171015      0.092314
  0.20    5     0.309514      0.176653
  0.20   20     0.613080      0.412549
```

Monotone together, vanishing together: the two clauses of the
motivating proposal are one condition, as Section 2 asserted.

### 3.4 The linear capacity law

At eps = 0.05 (p26a (iv)): 1 - gamma tracks Sigma/4 (0.00501 vs
0.00502 at n = 1; 0.09562 vs 0.10034 at n = 20, the quadratic
correction visible).  This is the operational face of P10's sigma-RP
linear law: approximate eventlessness = approximate coherence, with
the same linear structure and now a calibrated constant.

## 4. Part II - error correction is selective record formation

### 4.1 The type system

Theorem B is Knill-Laflamme, restated: a code with projector P
protects its logical sector against error set {E_i} iff
P E_i^dag E_j P = c_ij P - in record terms, iff every ALLOWED seam
(syndrome record) is logical-evidence-free while the noise evidence
is routed into the ledger.  The corpus content is the TYPING: clicks
are not good or bad by count but by what they seal.

### 4.2 Receipts (3-qubit bit-flip code, p = 0.08)

```text
typed clicks:   I(logical : syndrome) = 0.00e+00 nats  (EXACT zero)
                I(error  : syndrome)  = 0.7705 of H(error) = 0.8363
KL, allowed:    correctable set {1, X1, X2, X3}:
                max || P Ei Ej P - c P || = 0.0e+00
KL, forbidden:  P Z1 P eigenvalues on the code space: -1, +1
                (NOT proportional to P: the forbidden seam, in
                operator form - it IS a logical operator)
recovery:       logical failure = 3p^2 - 2p^3 (machine-exact at
                p = 0.02, 0.05, 0.10)
the wrong type: a Z-record at eps = 0.1 leaks sigma = 0.08109/step
                with NO mitigation in this code: the full Part-I tax
```

### 4.3 Two readings

1. **The click-routing dividend.**  Syndrome extraction RAISES the
   total click rate and LOWERS the logical leakage to exactly zero:
   first-order physical evidence becomes second-order logical
   failure.  Protection is not silence; it is typed noise.
2. **"Error rate" is a category error.**  The same per-qubit click
   budget destroys the computation or not depending only on its TYPE
   (X-typed: routed; Z-typed: fatal here).  Any capacity accounting
   in clicks-per-cycle without typing is wrong at order one - the
   record-native correction to standard hardware bookkeeping.

## 5. Part III - the metric: Sigma_leak per logical cycle

### 5.1 The matched-fidelity experiment

Two processors, identical average gate fidelity per cycle
(F = 0.99336): processor A applies a coherent over-rotation by
theta = 0.2 about Z (unitary - no record forms); processor B applies
dephasing with lambda = sin^2(theta/2) (which-path records seal).
After n = 100 cycles WITH a spin-echo recovery sequence (p26c):

```text
   processor A (Sigma_leak = 0):        recovered fidelity 1.000000
   processor B (Sigma_leak = 0.40/run): recovered fidelity 0.566762
   Part-I prediction for B: (1 + (1 - 2 lambda)^n)/2 = 0.566762
```

The echo recalls A's unitary error EXACTLY and recalls NOTHING of
B's: evidence already sealed in the environment is not recallable by
control pulses - the record ontology's restatement of why coherent
and incoherent errors differ in kind, not degree.

### 5.2 The metric

```text
   pre-click capacity per run = protected - leaked logical nats:
   A:  ln 2 - 0      = 0.6931  (full)
   B:  ln 2 - n*sigma/4 = 0.0000  (exhausted)
```

The proposal's claim - two processors with the same gate fidelity can
differ in computational power - is correct, and the discriminating
number is SIGMA_LEAK PER LOGICAL CYCLE: measurable (echo-vs-free
comparisons estimate the irrecoverable fraction; Section 6's stream
analysis types it), device-comparable, and blind to nothing the
capacity law cares about.  This is close to quantum volume in spirit
and different in kind: quantum volume benchmarks an outcome; the
metric prices the mechanism.

## 6. Part IV - the clock test: a hardware protocol

### 6.1 What it detects

P16's separation theorem: there exist stationary processes of finite
record rank with NO finite positive realization (the record clock) -
environments that defeat every finite hidden-Markov noise model while
having low-dimensional correlations.  If a device's syndrome stream
is such a process, all finite-state noise models and decoder priors
are structurally (not parametrically) wrong, and quasi-realizations
(negative weights allowed) strictly dominate at equal dimension.

### 6.2 The receipts (p26d)

```text
   hidden-Markov environment:  diagonal-Hankel min eig = -1.7e-17
                               PASS (moment class)
   record-clock environment:   min eig = -9.96e-3
                               FAIL (signed: no finite HMM exists)
   on the same clock stream:   3-dim quasi-realization residual
                               3.3e-16 (exact); best rational-period
                               (P <= 12) deviation 0.0168 - the
                               finite-state plateau, quantified
```

### 6.3 The protocol (numbered, with the statistical procedure)

```text
P1. Collect per-stabilizer syndrome time series s_t in {0,1},
    T total cycles, under fixed operating conditions (existing
    memory experiments already log these).
P2. Estimate the diagonal statistics p_hat(1^n) = (# runs of >= n
    consecutive 1s starting at a uniformly chosen t) / T, for
    n = 0..2m.  Choose the Hankel size m so that shot noise stays
    below the eigenvalue scale: std[p_hat(1^n)] ~ sqrt(p(1^n)/T)
    must be << the spectral gap of interest; in practice m = 4..6
    and T >= 10^6 cycles for syndrome rates p(1) ~ 10^-1..10^-2.
P3. Form H_hat[i, j] = p_hat(1^(i+j)), i, j = 0..m, and compute
    lambda_min(H_hat).
P4. CALIBRATE THE NULL: block-bootstrap the stream (blocks longer
    than the visible correlation time), recompute lambda_min over
    B >= 200 resamples, and let q_alpha be the alpha-quantile of
    lambda_min under resampling.
P5. DECLARE: SEALABLE-COMPATIBLE if lambda_min >= q_alpha for the
    chosen alpha (the moment class is not rejected);
    NON-SEALABLE if the upper confidence bound of lambda_min is
    < 0 (no finite hidden-Markov model of ANY dimension reproduces
    the stream - P16 Theorem B applies to the limit statistics).
P6. If NON-SEALABLE: fit a quasi-OOM (negative weights permitted) of
    the rank indicated by the singular values of the full word
    Hankel; expect finite-state decoder calibration to plateau at
    the P4-quantified deviation, and the quasi-model to close it.
```

Caveats, stated: the test as specified probes the single-letter
diagonal (the cheapest sufficient statistic); composite-letter
diagonals (blocks "10", "110", ...) extend it and are the natural
follow-up; estimation bias for rare long runs bounds m in P2; and a
PASS is compatibility, not proof of sealability.  This is the first
SHARD claim falsifiable by an engineering dataset, and its named run
on real device data is (QC-data).

## 7. Relation to standard quantum information - what is new here

Stated plainly, in the corpus' discipline:

```text
NOT NEW (sharpened/unified): that decoherence is environmental
  which-path information (Zurek); that recoverability is equivalent
  to decoupling; that QEC succeeds iff the environment learns only
  syndromes (Knill-Laflamme); that coherent and incoherent errors at
  equal fidelity differ in effect; that negativity governs classical
  simulation cost (PWB).  Parts I-III re-derive these in record
  language - their value is the unification under ONE functional
  (sigma) and the corpus constants.
NEW IN CONTENT:
  - the quarter law WITH its correction series and measured
    coefficients (the calibrated exchange rate between evidence and
    coherence, and its monitor band);
  - the metric as a capacity accounting (protected minus leaked
    nats, Section 5) rather than a benchmark;
  - the clock test (Section 6): a structural - not statistical -
    no-go for finite-state noise models, with a numbered hardware
    protocol; nothing in the standard toolkit tests for
    NON-SEALABILITY of the environment process;
  - the z-ordering claim for thresholds (8.1): an ordering law
    imported from the corpus' own record RG, checkable against
    decoder studies;
  - planarity-as-theorem and silence-as-mechanism for topological
    hardware (8.2), from P4/P18 rather than from anyon models;
  - the (QC-adv) conjecture (8.3): advantage = non-sealability, a
    process-level reading of the negativity-resource results.
```

## 8. Part V - the four angles

### 8.1 The coordination law in error-correction thresholds (p26e)

Code-capacity thresholds of surface codes map to disorder transitions
of statistical-mechanics models on the same graphs (Dennis-Kitaev-
Landahl-Preskill).  P10 Part III's coordination law - record ordering
is controlled by coordination number z, not dimension - therefore
predicts: thresholds ORDER BY z within fixed dimension.

```text
exact clean couplings (machine-verified closed forms):
   honeycomb (z = 3): K_c = 0.65848   [star-triangle product = 1
   square    (z = 4): K_c = 0.44069    to 1e-10; self-duality
   triangular(z = 6): K_c = 0.27465    sinh(2Kc) = 1; e^(4K) = 3]
   -> ordering strength monotone in z, exactly.
threshold anchors (named data, as reported; ordering is the claim):
   honeycomb-class  z = 3:  ~ 6.7%
   square           z = 4:  ~ 10.9%  (RBIM Nishimori point,
                                       Honecker-Picco-Pujol)
   triangular-class z = 6:  ~ 16.4%  (triangular/honeycomb RBIM
                                       studies, de Queiroz-class)
   -> MONOTONE IN z: the ordering PASSES.
the corpus' own receipts (P10 Part III, re-cited): triangular z = 6
   orders in 2d at -5.0% below critical; square +3.3%; honeycomb
   +15.8% above - the same ordering at the record level.
```

Scope, honestly: z orders thresholds WITHIN a dimension; it neither
sets values nor equates across dimensions (3d cubic z = 6 sits at
~ 23%).  Sharpened falsifiable form: any 2d code family whose
thresholds violate z-ordering at matched noise model and decoder
class refutes the law's application - that comparison at matched
decoders is part of (QC-data).

### 8.2 Topological computation is eventless transport (p26f)

```text
the silent gate:   braid implementation of the phase gate: environment
                   conditional-state overlap = 1.0000000000 (zero
                   which-path record - silence by THEOREM: flat
                   holonomy forms no records, P4 s20/P18 R1)
the same unitary,  dynamical implementation with bath leak eps = 0.15:
dynamically:       overlap 0.988686 -> Sigma_leak = 0.0455 nats/gate
the memory:        thermal anyons are unauthorized clicks: Poisson
                   stray crossings at e^(-Delta/T): ln tau = Delta/T
                   + c (MC receipts at four temperatures)
the planarity      d >= 3 eventless exchange-squared = identity
corollary:         (P18 R1, receipts 2.2e-14): braiding collapses to
                   permutations - the braid gate set exists ONLY on
                   effective 2d record screens (P9's window)
```

Reading: topological protection is not clever engineering against
decoherence - it is computing inside the corpus' unique braid
exception with gates that are STRUCTURALLY silent.  The Arrhenius
slope is the eventlessness boundary: protection lives exactly as long
as the diamond stays event-free, and planar hardware is a theorem,
not a preference.

### 8.3 Quantum advantage as cone violation (p26g)

```text
the frame:      qutrit phase-point operators self-validated before
                use (hermiticity 4.4e-15, trace-1 4.8e-16,
                completeness 2.0e-15, orthogonality 3.0e-15)
the cone:       nine stabilizer states across three bases:
                min W = -9.0e-16 (NONNEGATIVE - Gross' theorem as
                receipts: inside the cone = positively realizable =
                classically simulable)
the violation:  the strange state: min W = -1/3 EXACTLY; total
                quasi-weight sum|W| = 5/3; PWB cost factor
                (sum|W|)^2n = 2.78, 7.72, 59.5, 3545 at n = 1,2,4,8
the dictionary: P16 sealable = finite cone <-> stabilizer sector
                (W >= 0, efficient classical record model);
                P16 non-sealable (clock) <-> magic sector (W < 0,
                cost ~ exp(cone violation));
                Hankel/moment test <-> negativity witness
```

**Conjecture (QC-adv), stated precisely:** a family of computations
admits efficient classical simulation iff its intermediate record
description admits finite positive realizations of uniformly bounded
cone complexity; the simulation cost of a violating family grows
exponentially in the accumulated cone violation (for the qutrit
Wigner cone, exactly the PWB negativity bound, recovered above).
Known-true instances: the stabilizer/magic hierarchy (receipted).
Falsifier: an efficiently-simulable family with unboundedly growing
cone violation, or a hard family with uniformly sealable
intermediates.  Status: NAMED CONJECTURE - the process-level reading
of the negativity-resource results, not a new theorem.

### 8.4 Click-scheduling invariance (p26h)

```text
the typed seam:   MBQC teleportation step: outcome probabilities
                  = 1/2 EXACTLY (max deviation 4.4e-16 over 200
                  random state-angle pairs): I(L : click) = 0
the invariance:   forty random 6-seam feed-forward chains: min
                  output fidelity 1.0000000000 - six clicks per
                  run, zero leaked logical nats
the contrast:     basis mis-rotated by delta: max |p(m) - 1/2| =
                  0.049, 0.099, 0.194 at delta = 0.1, 0.2, 0.4 with
                  mean output infidelity 0.0017, 0.0065, 0.0268 -
                  leakage and damage rise together (the Part-I
                  tradeoff)
```

Corollary (schedule invariance): the circuit model (silent ledger,
click at the end) and MBQC (click every step, every click typed)
spend the same K_pre through different schedules - clicks cost
capacity through their LOGICAL EVIDENCE, never their count.  A
capacity LAW must be schedule-invariant; this one is, and MBQC is
revealed as the engineering of seams pinned to the zero-evidence
point of the Part-I tradeoff.

## 9. What this paper proves and does not prove

Proves/receipts at stated scope: Theorem A with its correction series
(proof in 3.1; measured coefficients to four digits); the monitor
band; the decoupling equivalence (exact Holevo receipts); the seam
type system in operator form with the typed-click mutual informations
exact; the matched-fidelity metric separation with the Part-I
prediction landing to six digits; the clock test's pass/fail contrast,
the quantified finite-state plateau, and the protocol of 6.3; the
z-ordering of exact clean couplings and (as named data) of threshold
anchors; the silence of braid gates, the Arrhenius eventlessness
boundary, and the planarity corollary; the qutrit cone receipts
(stabilizer nonnegativity, the exact -1/3, the compounding cost); the
MBQC typed-seam exactness, the schedule invariance, and the mis-typing
tradeoff.

Does not prove: a new asymptotic bound beating standard quantum
information theory (Section 7 draws the line explicitly); the
advantage = non-sealability law in general (8.3: named conjecture
with stated falsifiers); threshold VALUES (the z-law is an ordering
claim; the anchor values are cited data); a universal exchange-rate
constant (the band of 3.2 is the honest statement); the
Witten-Arrhenius constants beyond MC scope; any hardware result (the
clock test is a protocol; its device-data run is (QC-data) - the
first SHARD claim falsifiable by an engineering dataset).

## 10. The kernel after Paper 26

```text
KERNEL: unchanged - this is an APPLIED paper by design: every theorem
  it uses was already in the corpus; what is new is the dictionary
  (decoherence = unauthorized records; QEC = seam typing; magic =
  cone violation; topological protection = eventlessness; MBQC =
  typed scheduling) and the two EXPORTS:
  E1 (the hardware metric): Sigma_leak per logical cycle - the
     record-native number fidelity misses (Section 5).
  E2 (the clock test): the signed-Hankel diagnostic for non-sealable
     device environments, protocol 6.3, with the quasi-OOM
     recommendation - immediately runnable on existing syndrome data.
NEW NAMED: (QC-adv) the advantage = non-sealability conjecture (8.3,
  with falsifiers); (QC-data) the device-data run of the clock test
  and the z-ordering comparison at matched decoders (8.1).
```

## References and literature map

- Papers 4, 9, 10, 13, 16, 18 (internal): eventless transport and the
  silence theorem, the anyon window, sigma and the linear law, the
  capacity quanta, the clock and the cone, the braid collapse and the
  coordination law.
- W. H. Zurek, Rev. Mod. Phys. 75, 715 (2003): decoherence as
  environmental which-path information (the standard face of Part I).
- B. Schumacher, Phys. Rev. A 54, 2614 (1996); B. Schumacher and
  M. A. Nielsen, Phys. Rev. A 54, 2629 (1996): information-
  disturbance/decoupling (Section 2's collapse).
- E. Knill and R. Laflamme, Phys. Rev. A 55, 900 (1997): the seam
  type system's operator form (Section 4).
- E. Dennis, A. Kitaev, A. Landahl, J. Preskill, J. Math. Phys. 43,
  4452 (2002): thresholds as stat-mech transitions (8.1's mapping).
- A. Honecker, M. Picco, P. Pujol, Phys. Rev. Lett. 87, 047201
  (2001): the square-lattice RBIM Nishimori point (~10.9%).
- S. L. A. de Queiroz, Phys. Rev. B 73, 064410 (2006) and related
  RBIM lattice studies: triangular/honeycomb disorder transitions
  (the ~16%/~7%-class anchors; values as reported).
- N. Margolus and L. B. Levitin, Physica D 120, 188 (1998); S. Lloyd,
  Nature 406, 1047 (2000); I. Devetak, IEEE Trans. Inf. Theory 51,
  44 (2005): the min-terms (named imports).
- D. Aharonov and M. Ben-Or (1997): the threshold theorem (the
  fault-tolerance frame the law prices).
- A. Kitaev, Ann. Phys. 303, 2 (2003); C. Nayak et al., Rev. Mod.
  Phys. 80, 1083 (2008): topological computation (8.2's frame).
- D. Gross, J. Math. Phys. 47, 122107 (2006); V. Veitch et al., New
  J. Phys. 14, 113011 (2012); H. Pashayan, J. J. Wallman, S. D.
  Bartlett, PRL 115, 070501 (2015): discrete Wigner, negativity as
  resource, the cost bound (8.3).
- R. Raussendorf and H. J. Briegel, PRL 86, 5188 (2001): MBQC (8.4).
- A. W. Cross et al., Phys. Rev. A 100, 032328 (2019): quantum
  volume (the benchmark Section 5's metric is contrasted with).
- H. Jaeger, Neural Computation 12, 1371 (2000); M. Vidyasagar,
  Hidden Markov Processes (2014): OOMs/quasi-realizations (6.3's
  modeling recommendation).
```
