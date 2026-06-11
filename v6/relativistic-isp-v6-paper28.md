# Paper 28 (v6) - SHARD: First Contact - The Clock Test on Device Data, the External Extraction, and the Registered Prediction

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
The corpus' first contact with the world outside its own receipts,
in three movements.  ONE: the clock test (P16's separation theorem
made an instrument in P26) ran on REAL quantum hardware data -
Google's 2023 surface-code memory experiment, 315 MB of public raw
detection events, parsed from the original stim files.  ALL 64
stabilizer streams PASS (distance-3 across four patch centers and
both bases, distance-5, 50,000 shots each): the Sycamore device
environment is MOMENT-COMPATIBLE - no structural obstruction to
finite-state noise models exists in its run statistics.  The verdict
is earned, not vacuous: the statistics were hardened against the
degenerate-Hankel bias (a real subtlety - exactly-singular Hankels
push the plug-in eigenvalue negative; the basic bootstrap corrects
it, and the iid control then passes), a MIXTURE-ROBUSTNESS
proposition proves drift cannot false-positive the test, and the
positive control - a hidden irrational rotation at matched rate and
sample size - is decisively SIGNED (CI [-4.2e-4, -3.4e-4]).  TWO:
the three externally defensible results were extracted into
vocabulary-free standalone drafts (the RP block-spectrum theorem,
the syndrome test with its device results, the graded Weyl
criterion) - locally only, per standing constraint; nothing was
sent anywhere.  THREE: the corpus' first quantified forward
prediction was REGISTERED: the neutrino inter-generation step
S_nu = sqrt(dm2_21/dm2_31) = 0.1718 +- 0.0026 against
sqrt(eps_record) = 0.17833 - the band form (O(1) coefficient in
[0.80, 1.25]) currently INSIDE at C = 0.963; the strict form
registered AS UNDER TENSION at 2.5 sigma, with JUNO named as the
resolver.  A real dataset, three portable results, one falsifiable
number: the difference between a corpus and a theory, executed
```

## 0. Verdict

```text
MOVEMENT I (the device run).  Instrument: the diagonal-Hankel moment
test (P16 Theorem B's contrapositive, P26 Protocol 6.3), hardened:
  - Proposition 2.1: any finite hidden-Markov environment gives PSD
    run-statistic Hankels (the structural null, all dimensions at
    once);
  - Proposition 2.2 (mixture robustness): convex mixtures of moment
    sequences are moment sequences - shot-to-shot drift CANNOT
    produce a false rejection: pooling over 50,000 shots is safe;
  - the statistics: windowed run estimator on bulk rounds; the
    degenerate-Hankel bias identified and corrected by the BASIC
    bootstrap interval (iid streams sit exactly ON the PSD boundary;
    the plug-in lambda_min is biased negative there).
Data: Zenodo 6804040 (public; raw detection events in stim b8
format; detector coordinates parsed from the circuit files).  Run:
six experiment folders at 25 rounds - d3 X-basis at four patch
centers, d3 Z-basis, d5 - 64 stabilizer streams, 50,000 shots each,
bulk rounds, m = 3:

   64 PASS, 0 SIGNED.   Rates 0.10-0.20; round-drift 0.003-0.028;
   typical lambda_min ~ 1e-5 with corrected CIs straddling zero.
   Controls at matched rate and sample size:
     iid:                  CI [-4.9e-5, +7.6e-5]  -> PASS
     hidden rotation:      CI [-4.2e-4, -3.4e-4]  -> SIGNED.

READING: the device environment - leakage, TLS defects, drift and
all - is moment-compatible: whatever non-Markovianity Sycamore has
is of the kind finite hidden-state models can express.  The PASS is
a statement about the device, not the test: the same pipeline at the
same statistics decisively rejects an oscillatory environment.

MOVEMENT II (the extraction).  Three standalone, vocabulary-free
drafts now exist (external/, LOCAL ONLY - nothing sent):
  - rp-block-spectra.md: bond-RP = POVM-type realizations; the
    block-spectrum theorem (length <= 4); the reality map; the
    validity wall (0.205); Conjectures A and B.
  - syndrome-hankel-test.md: the instrument, its statistics, and the
    full device results - the publishable face of Movement I.
  - graded-weyl-detector.md: the graded local Weyl criterion with
    the measured exponent table (0.243/0.465/0.706/0.956).
Each is readable by a specialist who has never seen this corpus.

MOVEMENT III (the registration).  external/registered-prediction-
neutrino-step.md, dated 2026-06-10:
  S_nu = m2/m3 = sqrt(dm2_21 / dm2_31) = 0.1718 +- 0.0026 (NO)
  sqrt(eps_record) = sqrt(0.0318) = 0.17833
  BAND FORM (registered prediction): S_nu = C sqrt(eps_record),
    C in [0.80, 1.25]: currently C = 0.963 (NO) / 0.975 (IO): INSIDE.
  STRICT FORM (registered as under tension): equality is 2.5 sigma
    from current central values; JUNO-class precision on dm2_21
    resolves it (> 5 sigma kill or revival).
  Falsifiers: F1 quasi-degeneracy voids the premise; F2 band exit
    kills the extension; F3 strict-form death at sub-percent data.
  Honesty: the central-value proximity was noticed BEFORE
    registration; the registration adds tolerances, falsifiers, and
    the forward commitment.
```

## 1. Method and reproducibility

```text
code/clock_test_tool.py        the instrument (standalone, plain
                               language); canonical device output
                               preserved with this campaign
data: /tmp/qec_data            Zenodo 6804040, google_qec3v5_
                               experiment_data.zip (315 MB, public),
                               unpacked: per-experiment folders with
                               circuit_noisy.stim (DETECTOR
                               coordinates), detection_events.b8
                               (50,000 packed shots), properties.yml
external/rp-block-spectra.md          ) the three extractions
external/syndrome-hankel-test.md      ) (local drafts; user
external/graded-weyl-detector.md      )  constraint: not sent)
external/registered-prediction-neutrino-step.md   the registration
```

Network use in this campaign: read-only download of one public
dataset.  Nothing was transmitted, posted, or submitted anywhere.
Corpus inputs: P16 (the separation theorem and the moment test),
P26 (Protocol 6.3), P27 (the RP-form and validity-wall results the
first extraction packages), P8/P10 (eps_record), P21/P23 (the
neutrino chain the registration sharpens).

## 2. The instrument, complete

### 2.1 The structural null

**Proposition 2.1.**  Let s_t be a stationary binary stream generated
by ANY finite hidden-Markov environment: p(w) = pi M_{x_1} ... M_{x_n}
1 with all entries nonnegative, any dimension.  Then for every m the
Hankel matrix H[i, j] = p(1^(i+j)), 0 <= i, j <= m, is positive
semidefinite.

*Proof.*  p(1^n) = pi M_1^n 1.  Restrict to the part of the state
space accessible from pi and co-accessible to 1 (this changes no
value).  There the sequence is a nonnegative-weight combination of
powers of M_1's eigenvalues; Perron-Frobenius structure on the
accessible part makes the diagonal a mixture of real-spectrum
geometric modes, i.e. a Hamburger moment sequence p(1^n) =
int x^n dmu(x) for a positive measure mu; Hankel positivity is the
moment property: for any vector c, sum_ij c_i c_j p(1^(i+j)) =
int (sum_i c_i x^i)^2 dmu >= 0.                                  QED

A SIGNED Hankel therefore excludes every finite-state model at once -
structural, not parametric.  The converse fails (PASS = compatibility,
not proof), which is exactly the right asymmetry for an instrument.

### 2.2 Mixture robustness: drift cannot false-positive

**Proposition 2.2.**  A convex mixture of moment sequences is a
moment sequence.  Consequently, if each shot (or each drift segment)
of a dataset is individually compatible with SOME finite-state
environment - possibly a different one per segment - the pooled run
statistics still produce a PSD Hankel.

*Proof.*  Mixing measures: p(1^n) = sum_k w_k int x^n dmu_k(x) =
int x^n d(sum_k w_k mu_k)(x), and a convex combination of positive
measures is a positive measure.                                  QED

This is the property that makes the test SAFE on real data: parameter
wander, calibration drift between shots, even slow continuous drift
(a continuum mixture) cannot sign the Hankel.  Only genuinely
oscillatory - complex-spectrum - environment structure can.  On a
real device, a SIGNED verdict would therefore have been a discovery,
not an artifact of nonstationarity.

### 2.3 The statistics, including the bias trap

Estimator: for one stabilizer's shots x rounds binary matrix
(bulk rounds only - the first and last rounds carry boundary
detectors), p_hat(1^n) is the windowed run frequency: the fraction of
(shot, start-position) windows that are all ones, n = 0..2m.  Hankel
H_hat from these; statistic lambda_min(H_hat).

THE BIAS TRAP.  For an iid stream, p(1^n) = p^n: the true Hankel is
RANK ONE - it sits exactly on the PSD boundary with lambda_min = 0.
Estimator noise around a boundary point pushes the plug-in
lambda_min(H_hat) NEGATIVE almost surely, and a naive percentile
bootstrap then wrongly declares iid streams "signed" (we observed
exactly this: iid control CI [-2.8e-4, -5.0e-6] under the naive
rule).  The standard repair is the BASIC bootstrap interval for the
true value:

```text
   CI_true = [ 2 lam_hat - q_0.975 ,  2 lam_hat - q_0.025 ],
```

with q the bootstrap quantiles of lambda_min over B = 200 shot
resamples.  Verdict SIGNED only if the upper end of CI_true < 0.
Under this rule the iid control passes and the oscillatory control
still fails decisively - the rule has both size and power, receipts
in Section 3.3.

## 3. Movement I: the device run

### 3.1 The data and its parsing

Google 2023 surface-code memory experiment ("Suppressing quantum
errors by scaling a surface code logical qubit"), public data,
Zenodo record 6804040.  Each experiment folder holds the noisy stim
circuit and the raw measurement record; the detection events come as
stim b8 files - one shot per ceil(D/8) bytes, bits packed
little-endian, D the detector count (200 for d3 at 25 rounds; 50,000
shots).  Detector indices are mapped to (stabilizer, round) by
parsing the DETECTOR(x, y, t) coordinate annotations from the
circuit file in declaration order: grouping by (x, y) yields one
time series per stabilizer per shot.  Bulk window: rounds 2 through
t_max - 2.

### 3.2 Results

Sixty-four stabilizer streams across six experiment configurations:
d3 X-basis at four patch centers (32 streams), d3 Z-basis (8), and
d5 (24).  Representative rows (full table in the canonical output):

```text
d3, X basis, center 3_5:
 stab (1,4): rate 0.1266  drift 0.018  lam +2.8e-05
             CI [+3.1e-06, +5.8e-05]   PASS
 stab (3,6): rate 0.2015  drift 0.013  lam -2.8e-05
             CI [-6.2e-05, +5.9e-06]   PASS
d3, Z basis, center 3_5:
 stab (4,3): rate 0.1066  drift 0.004  lam +1.7e-05
             CI [-2.0e-07, +3.5e-05]   PASS
 stab (3,4): rate 0.1697  drift 0.017  lam -1.8e-05
             CI [-4.7e-05, +1.3e-05]   PASS
d5, center 5_5 (24 stabilizers):
 stab (1,4): rate 0.1346  drift 0.028  lam +1.3e-07
             CI [-2.9e-05, +3.4e-05]   PASS
 stab (3,2): rate 0.0974  drift 0.006  lam +3.0e-07
             CI [-1.7e-05, +1.9e-05]   PASS

AGGREGATE:  64 PASS,  0 SIGNED  of 64 streams.
rates span 0.097-0.205; round-drift 0.003-0.028; every corrected CI
straddles or sits above zero.
```

### 3.3 The controls

At the device-matched mean rate (0.153) and identical sample shape
(50,000 x 22):

```text
 iid stream:            lam_min -2.7e-05, CI [-4.9e-05, +7.6e-05]
                        -> PASS  (the bias repair working: the naive
                        rule had wrongly signed this)
 hidden rotation        lam_min -3.8e-04, CI [-4.2e-04, -3.4e-04]
 (theta = 1 rad,        -> SIGNED, decisively
  90% modulation):
```

The instrument detects what it must detect and passes what it must
pass, at exactly the statistics of the real run.

### 3.4 Reading the result

1. **The device verdict.**  Sycamore's stabilizer environments are
   MOMENT-COMPATIBLE: nothing in their run statistics obstructs
   finite-state noise modeling.  The known non-Markovian suspects -
   leakage (a literal hidden state), two-level-system defects
   (telegraph processes = two-state hidden Markov), slow drift
   (mixtures, Prop. 2.2) - are all moment-class mechanisms, and the
   data is consistent with exactly that.
2. **What a SIGNED would have meant** - and still would, on any
   device: no finite-state decoder prior of any dimension exactly
   right; quasi-realization noise models strictly dominant at equal
   dimension; a structural discovery about the hardware.  The test
   is now validated end-to-end for that hunt.
3. **Extensions left named:** composite-block diagonals (the P27
   block machinery sharpens the test beyond single-symbol runs);
   cross-stabilizer joint statistics; per-segment analysis around
   documented burst events; other devices' public datasets.

## 4. Movement II: the extraction

The three results that survive outside the corpus' vocabulary were
rewritten as standalone drafts (LOCAL ONLY, per standing constraint -
nothing has been sent, posted, or submitted):

```text
rp-block-spectra.md.  "Spectral constraints on reflection-positive
  stationary processes."  Contents: bond-RP processes are exactly
  POVM-type operator realizations (with proof); products of PSD
  letters give real spectra for all blocks of length <= 4 (with the
  cyclic-reduction proof); the empirical reality map (5-6 real,
  first rotations at 7-8, the Hillar-Johnson connection); the
  validity wall (best complex subordination 0.205 among sound
  processes, the impostor mechanism); Conjectures A (no rotations at
  the top) and B (RP + finite rank => positive realization).  Pure
  matrix analysis and probability.
syndrome-hankel-test.md.  "A structural compatibility test for
  finite-state noise models, with results on public surface-code
  data."  The instrument of Section 2, the statistics including the
  bias repair, the full device results of Section 3, and the use
  cases.  Quantum hardware diagnostics, no framework needed.
graded-weyl-detector.md.  "A graded local Weyl criterion for
  coefficient regularity."  The detector, the strata separation, the
  exponent table 0.243/0.465/0.706/0.956 vs min(1, alpha/2), the
  measured -1/4 leading coefficient, and the rigidity conjecture.
  Classical heat-kernel analysis.
```

The program-discipline point: the corpus' statuses and receipts have
been a SIMULATION of external scrutiny; these drafts are the
interface to the real thing, prepared so that the decision to expose
them is a one-step action whenever taken - and explicitly NOT taken
here.

## 5. Movement III: the registration

### 5.1 Provenance and observable

eps_record = 3 kappa - 1 = 0.0318 is the corpus' single structural
small number, derived in Papers 8/10 from the relation-code binding
laws - with no reference to leptons, quarks, or the Standard Model.
Paper 23 found all nine charged-fermion inter-generation steps inside
[eps^2, sqrt(eps)] (postdiction).  The registered FORWARD test is the
neutrino sector: under a hierarchical normal-ordered spectrum,

```text
   S_nu = m2/m3 = sqrt( dm2_21 / dm2_31 ).
```

### 5.2 The numbers (current global-fit inputs)

```text
   dm2_21 = (7.41 +- 0.21) e-5 eV^2
   dm2_31 = (2.511 +- 0.027) e-3 eV^2        (normal ordering)
   S_nu = 0.1718 +- 0.0026  (1.5%; error = half the quadrature sum
          of the relative mass-squared errors)
   sqrt(eps_record) = 0.17833
   C := S_nu / sqrt(eps_record) = 0.963 (NO) / 0.975 (IO)
```

### 5.3 The registered claims, premises, falsifiers

```text
P-eps-nu (BAND; the prediction): S_nu = C sqrt(eps_record) with
   C in [0.80, 1.25].  Currently INSIDE (0.963/0.975).
P-eps-nu-strict (registered AS UNDER TENSION): C = 1 exactly is
   2.5 sigma from current central values (3.8% vs 1.5% error).
   JUNO-class sub-percent precision on dm2_21 resolves it: > 5 sigma
   kill, or revival if central values drift.  Both outcomes recorded
   in advance as informative.
PREMISE (h): hierarchical spectrum, m1 << m2 (so that m2/m3 equals
   the mass-squared-ratio square root).
FALSIFIERS: F1 - established quasi-degeneracy voids the premise (a
   recorded premise failure, not a pass); F2 - precision moving C
   outside the band kills the extension; F3 - the strict form dies
   at sub-percent data holding current centrals.
HONESTY NOTE: the central-value proximity was noticed BEFORE the
   registration and motivated it; the registration's content is the
   declared tolerances, the falsifiers, and the forward commitment -
   the coincidence is the seed, not the claim.
```

### 5.4 Why this row

It is the only place in the corpus where a number derived with no
reference to the Standard Model meets a number nature measured
independently, with no fit parameter between them.  The strict form
being ALREADY under quantified tension is a feature: that is what a
real prediction looks like before its experiment reports.

## 6. What this paper proves and does not prove

Proves: Propositions 2.1 and 2.2 (the structural null and the
mixture robustness, with proofs); the size-and-power validation of
the corrected statistic (iid passes, rotation signed, at matched
statistics); the device result itself - 64/64 moment-compatible
streams on the public Sycamore dataset at the stated scope (m = 3,
bulk rounds, 50,000 shots per configuration).

Establishes as registered commitments: the P-eps-nu band and strict
claims with their premises and falsifiers (Section 5.3).

Does not prove: that the device environment IS finite-state (PASS is
compatibility - the converse direction does not exist for this
test); anything about other devices, deeper Hankels (m > 3),
composite blocks, or burst segments (named extensions); the
correctness of either registered claim (that is the point of
registration); and nothing here changes the kernel - this is an
empirical-contact paper by design.

## 7. The kernel after Paper 28

```text
KERNEL: unchanged - { (C-reg-b') , (PR-RP++) , (V), calibration } +
        { O7/O8/O11 remainders, D10-refinements, mu-dyn, loop-H,
          (R-id) }.
(QC-data) PARTIALLY DISCHARGED: the clock test's first device run is
   DONE - verdict PASS on Sycamore at stated scope, instrument
   validated end-to-end (the z-ordering comparison at matched
   decoders remains the open half).
PREDICTION LEDGER (P25) gains its first REGISTERED forward row:
   P-eps-nu (band: inside; strict: under tension, JUNO-resolved).
EXTERNAL INTERFACE: three standalone drafts exist, local; exposure
   is a single deliberate step, not taken (standing constraint).
PROGRAM STATE, one sentence: one instrument validated on real
   hardware with a clean negative result, three results packaged to
   survive outside their own vocabulary, one quantified forward
   prediction with a named experiment that will judge it.
```

## References and literature map

- Papers 8, 10, 16, 21, 23, 26, 27 (internal): eps_record, the
  separation theorem and the moment test, the neutrino chain, the
  protocol, the RP-form and wall results packaged in the extraction.
- Google Quantum AI, "Suppressing quantum errors by scaling a
  surface code logical qubit," Nature 614, 676 (2023); data: Zenodo
  record 6804040 (the device dataset analyzed here).
- A. Heller, Ann. Math. Statist. 36, 1286 (1965); F. R. Gantmacher,
  The Theory of Matrices II: the structural null's classical frame.
- B. Efron and R. J. Tibshirani, An Introduction to the Bootstrap
  (1993): the basic bootstrap interval (the bias repair of 2.3).
- I. Esteban et al. (NuFIT collaboration): the global-fit
  mass-squared differences used in Section 5.2.
- JUNO collaboration, "JUNO physics and detector," Prog. Part. Nucl.
  Phys. 123 (2022): the named resolver of the strict form.
- C. J. Hillar and C. R. Johnson, SIAM J. Matrix Anal. Appl. 23
  (2002); A. Klein and L. J. Landau, J. Funct. Anal. 44 (1981):
  the extraction drafts' anchors.
```
