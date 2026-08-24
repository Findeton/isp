# ISP v17 R1 independent review — Seat P-R

## Microscopic reader and detector-physics subreport

**Seat:** P-R (physical reader / detector)  
**Reviewer task:** `/root/r1_review_physics`  
**Review object:** the immutable R1/native-source-gap bundle pinned by
`v17/note-r1-native-source-gap-independent-review-pin.md`  
**Review mode:** read-only, source-first, independent  
**Signed recommendation:** **D3 — ACCEPT-WITH-SCOPE (P-R axis)**

I inspected no sibling report and communicated with no other review seat. I
made no repository edit, stage, or commit. This report is a logically separate
P-R object; neither the P-S conclusion nor a future root conclusion was used
to determine it.

---

## 1. Authentication

### 1.1 Chronology and pin

- Repository `HEAD` during review was exactly
  `befe415017d0ea1f13ed965f07ebb39236864497`.
- The pin contained 534 LF-terminated lines and 26,150 bytes.
- Ordinary SHA-256 of the pin was
  `617223214d37fb37a2e896b9ac6b019b0d7040b4dcef6c9410d52abfebb8c9e8`.
- Independent normalization of the pin's signature lines produced
  `91c5451004d7f8a5988310084402629f305dabf73ccab0934743d209ec7c5bff`,
  exactly its printed normalized self-SHA-256.
- The pin was LF-only, ended in exactly one LF, and had no trailing horizontal
  whitespace.

### 1.2 Repository bundle

I directly rehashed all sixteen pinned repository objects; all sixteen matched
section 2 of the pin byte for byte. I read the lead synthesis and the
P-R-load-bearing preparation, microscopic-reader, common-parent, and R1-member
objects at those authenticated bytes. I did not inspect sibling reports. The
untracked v16 handoff note was unrelated and was not inspected.

### 1.3 Exact source receipts

I directly rehashed all twenty-one PDFs in
`/tmp/isp-r1-review-sources.6Tgm6Y`; every byte count and SHA-256 matched the
pin (21/21). The P-R packet used below authenticated as follows:

| exact PDF | bytes | SHA-256 |
|---|---:|---|
| `2501.13791v3.pdf` | 26618133 | `802398f49122a43d237d3e405aada43e44cc20799fd62145d1d517f8d8bba08a` |
| `1702.02813v1.pdf` | 2020132 | `41c1d9987342691124014f7c5f704b153fdb593756c3dcaa4d611d92372bd859` |
| `2503.17146v1.pdf` | 2147662 | `bcfbd9a5ece27e5c1e6055dfbc00e55d962f4134d2bf8d318962916430015822` |
| `2110.10484v1.pdf` | 455830 | `446c204ba680f736ac3e13454aa5a6ab21c27753f3d82ef69ff9990b9a7e4bae` |
| `quant-ph_0206125v1.pdf` | 287960 | `c41f2157ad1ad5967ab378416b0a02449750e9b5b318c88fd2016d7163f04448` |
| `1301.3337v2.pdf` | 1823254 | `08a63685f214d390f5c20a7c7e6966f865edebed874a1867f45b5c3283c1ce19` |
| `2206.04032v2.pdf` | 1030040 | `d3c05804da500d65066711b23339babf939ff64cc57fe0529ca66aff609184a4` |

No detector conclusion below relies on an author summary instead of these
exact PDFs.

---

## 2. Independent reconstruction

### 2.1 What Simon et al. actually predict

Simon et al. `2501.13791v3` makes real microscopic progress. It computes
material-specific electron-phonon spectral information using DFPT, evolves
mean quasiparticle and phonon distributions, couples those distributions to
order-parameter dynamics, and predicts a detection-current threshold
`I_det` for the modeled SNSPD regime. Figure 4 compares the resulting
threshold controls with prior data and with phenomenological models.

The source is not an event-level detector law:

1. it begins after photon absorption with an approximate phonon-bubble
   initial condition;
2. the initial deposited energy is taken spatially uniform in a declared
   cylindrical region, and diffusion is treated at a bounded level;
3. the calculated quasiparticle/phonon equations are mean distribution
   equations, not a full counting-statistics kernel for individual cascades;
4. the paper predicts the threshold current, not the full below-threshold
   internal-efficiency curve;
5. Fano fluctuations, timing jitter, dark counts, optical absorption, spatial
   inhomogeneity, electrothermal/circuit propagation, and retained-record
   statistics are explicitly future work or external modeling; and
6. material/device coordinates remain informed inputs or approximations.

The source's calibration/adjustment ledger matters. The value `eta = 0.2`
described as the best fit in Figure 4(a) belongs to the *phenomenological
diffusive-hotspot comparator*, not the ab-initio curve. The ab-initio
calculation itself uses device/material choices such as assumed diffusion
coefficients, approximate table values, an NbN strong-coupling rescaling
`2.1/1.76`, and NbN gap/critical-temperature values chosen to resemble a
disordered polycrystalline film. Its statement that the resulting threshold
comparison has no free fit parameters is compatible with those informed
inputs; it does not mean an end-to-end detector law is parameter-free.

This independently reproduces the frozen microscopic-reader audit's central
scope, with the source-precision qualification in P-R-01 below.

### 2.2 Fano, jitter, and switching laws remain additional physics

Kozorezov et al. `1702.02813v1` models stochastic energy partition and Fano
smearing of SNSPD threshold curves. It explicitly uses an effective Fano
factor as a fitting parameter where credible microscopic estimates are not
available and performs fitted comparisons to photoresponse curves. It is a
valuable stochastic-cascade control, but it does not uniquely provide all
distribution tails, switching mechanisms, circuit behavior, or storage.

Sidorova et al. `2503.17146v1` builds a quantitative multi-photon timing model
that combines local detection fluctuations with thermoelectric-domain
dynamics. Its abstract and fit section state that the observed arrival-time
histograms are described using three fitting parameters: a mean-time scale
and Gaussian and exponential jitter components. It is not a target-blind
microscopic origin of those parameters.

No audited paper uniquely selects among vortex entry, phase slip, hotspot,
thermal, quantum, fabrication-defect, and dark/background switching hazards
for the complete R1 detector. The normalized competing-risk formula in the
frozen reader packet is therefore exact only *given* supplied hazards; it does
not derive them.

### 2.3 Realistic detector dynamics consume quantum nomology and
phenomenological device rates

Warszawski and Wiseman `quant-ph/0206125v1` treats the quantum system and a
classical detector state jointly and includes efficiency, dark counts, APD
response time, dead time, photoreceiver bandwidth, and electronic noise. It
shows why the conditioned quantum system alone is generally non-Markovian
after realistic detector dynamics are included. But its quantum master/
trajectory framework, efficiencies, transition rates, dark rates, reset
times, and noise/circuit parameters are model inputs. It is a composition
framework under standard quantum theory, not a material-to-actuality source.

The frozen R1 use of this paper as a conditional detector framework is
accurate.

### 2.4 Detector tomography describes the target; it does not source it

Fitzke et al. `2110.10484v1` reconstructs time-dependent POVMs from detector
data with adaptive regularization. It tests seven free-running InGaAs SPADs
and finds, across devices/settings, that the simple dead-time plus one-jitter
model does not reproduce the measured intensity-dependent temporal response.
The paper explicitly concludes that no single reconstructed jitter
distribution can explain the relevant high-intensity shapes. This is evidence
against assuming that a plausible low-parameter model is complete; its
tomographic POVM is nevertheless a fitted description of the target device.

Renema et al. `1301.3337v2` uses detector tomography to factor optical
absorption from intrinsic multi-photon detection probabilities and observes a
bias-energy universal response curve for one NbN nanodetector. The count data
are fitted to reconstruct the detection probabilities and linear efficiency.
That empirical curve is a strong device control, not an origin law or
cross-device no-refit transfer.

The frozen R1 bundle uses both sources in exactly this hostile/control role. I
found no target POVM, click table, fitted detector curve, or detector-tomography
object relabeled as a derived microscopic instrument.

### 2.5 Recovery and memory defeat a generic memoryless reader

Uzunova and Semenov `2206.04032v2` models SNSPD dead time and smoothly
recovering efficiency. For continuous-wave acquisition, the state of recovery
after the last pulse in earlier measurement windows changes the probabilities
in the current window. Equations (60)--(75) make the resulting POVM depend on
current and previous window amplitudes; the paper emphasizes the resulting
nonlinear dependence on the density operator. A Markovian approximation
requires an explicit small dead-plus-relaxation time relative to the window
and a sufficient memory state. Independent windows can instead be enforced by
darkening/postselection, which is a different physical protocol.

Therefore the one-mode R1 formula's independent per-window Bernoulli reader is
a valid bounded control, not a generic SNSPD law. The frozen reader packet
correctly requires recovery, latching, drift, thermal relaxation, and later
record variables to be carried in the reader state when relevant.

### 2.6 Component composition and normalization

The frozen microscopic-reader packet writes a typed factorization through
absorption, stochastic cascade, switching, circuit/noise, comparator, and
storage kernels. Its normalization theorem is mathematically valid if every
kernel is nonnegative and normalized and the logic map is total. The seven
exact detector sources do not jointly supply one experimentally identified,
compatible set of all those kernels for a fabricated device. Mean
quasiparticle equations, a fitted Fano model, a fitted timing law, a realistic
quantum-trajectory framework, and a storage label do not automatically become
one event-level process merely by multiplication.

Accordingly, R1 contains two different and correctly separated achievements:

- an exact complete *effective* threshold-click member given local
  efficiencies, dark probabilities, the independent-reader premise, and
  standard quantum propagation; and
- a proposed material reader architecture whose full microscopic stochastic
  closure is absent.

The phrase "complete record law" in C1/C2 is acceptable only at the first,
conditional level. It does not mean that Simon et al. plus the remaining
papers already produce a no-refit fabricated SNSPD law.

### 2.7 Stable records, persistence, uncertainty, erasure, and reset

The frozen reader and common-parent objects do more than attach a label: they
require an amplified carrier, a readable map, persistence under a typed stable
future grammar, an eraser outside that grammar, future sufficiency or residual
memory, uncertainty/crosstalk bounds, and energy/entropy/reset accounting.
They also distinguish a calculation coordinate from a physical division.

However, those conditions are an architecture and test contract. No pinned
apparatus result demonstrates for a real detector that the retained record
sector satisfies all persistence, future-sufficiency, crosstalk, eraser, and
reset tests with an error budget. The stable-record boundary is therefore
physically motivated and nontrivial, but not implementation-validated. The
lead itself says microscopic reader closure, stable-division transfer, and
no-refit transfer remain incomplete.

---

## 3. Coordinate classification

The status words below mean: **generated** = an output of the frozen R1 rule
conditional on its inputs; **independently calibrated** = a contingent
empirical input measured outside the held-out score; **fitted** = inferred
from target-equivalent output and therefore only a control/forbidden payload;
**assumed** = nomology, sectorization, domain, or stochastic premise; and
**proposed** = a physically typed construction step not yet sourced or
implementation-validated.

| load-bearing coordinate | P-R classification | reason |
|---|---|---|
| incident quantum field packet | generated upstream conditionally / assumed quantum boundary | not detector-origin physics |
| absorption channel and absorbed-sector instrument | proposed/generated only if the supplied field-material channel is complete | Simon starts after absorption |
| electron-phonon spectral functions | generated by declared DFPT approximation or independently calibrated input | serious material calculation, not exact ontology |
| material geometry, bias, bath, diffusion, gap, escape times | independently calibrated or assumed effective inputs | several are informed/approximate in Simon |
| phonon-bubble initial condition | assumed approximation | not dynamically derived |
| mean quasiparticle/phonon distributions and order parameter | generated conditionally | do not fix individual-event statistics |
| detection-current threshold `I_det` | generated conditionally at Simon's scope | not full efficiency distribution |
| below-threshold internal efficiency | proposed / absent microscopically; may be independently calibrated effectively | not generated by current source packet |
| Fano energy-partition law and tails | fitted/effective input or proposed microscopic output | first two moments do not select tails |
| stochastic cascade kernel `K_C` | proposed / absent | mean kinetics insufficient |
| photon-assisted switching hazard | proposed or fitted/independently calibrated | mechanism/rate not uniquely selected |
| dark/background hazard or per-window dark probability | independently calibrated/fitted input | explicitly charged in R1 |
| timing/jitter law | independently calibrated or fitted input | Sidorova retains three fit parameters |
| recovery, dead time, latching, afterpulse, drift memory | independently calibrated/proposed kernel | Uzunova shows nonlocal window dependence |
| circuit/filter/noise law | independently characterized input; waveform generated conditionally | no universal detector circuit descent |
| comparator threshold, timestamp, veto, saturation logic | independently calibrated/supplied physical input | deterministic reader map once supplied |
| threshold efficiencies `eta_j` and dark rates `d_j` in C2 | independently calibrated phenomenological inputs | not microscopic outputs |
| independent local Bernoulli-reader premise | assumed bounded model | not generic under memory/shared baths |
| target POVM/click table/fitted response curve | fitted forbidden payload / hostile control | no evidence of use in R1 |
| complete normalized event law | generated conditionally if all component kernels/instrument branches are normalized | component sources do not yet earn premises |
| storage, persistence, crosstalk, reset, eraser kernels | proposed and/or independently characterized inputs | typed, not implementation-validated |
| stable-record division | proposed physical boundary plus assumed/derived sector separation | no real error-budget test run |
| separately built/cross-device no-refit transfer | proposed / absent | expressly not run |
| microscopic detector actuality and one selected history | absent | no source supplies it |

Every load-bearing P-R coordinate is explicitly classified in the frozen
bundle, but the word "complete" must retain the conditional qualification in
P-R-02 and P-R-06.

---

## 4. Numbered P-R findings

### P-R-01 — Simon best-fit wording needs its exact comparator scope

- **Severity:** low
- **Type:** physical-source precision
- **Evidence:** Figure 4(a) of `2501.13791v3` says `eta = 0.2` is the best-fit
  value for the *phenomenological diffusive hotspot model*. The ab-initio
  curve is separate, while its Appendix uses strong-coupling rescaling and
  informed/approximate material values.
- **Affected claims:** C1, C10, C11; no central claim is defeated.
- **Finding:** The frozen reader audit's sentence that the "device comparison
  includes a best-fit hotspot parameter" is literally correct, but must not
  be read as saying that `eta = 0.2` was fitted inside the ab-initio curve.
  This narrowing is already entailed by the exact source and by the frozen
  audit's broader input ledger.

### P-R-02 — Complete reader law is conditional; microscopic stochastic
closure is absent

- **Severity:** major scope, non-defeating
- **Type:** physical-source / semantic-scope
- **Evidence:** Simon supplies mean kinetics and `I_det`, not full event
  statistics; Kozorezov and Sidorova retain fitted parameters; the frozen MRD
  theorem proves normalization only if `p_A`, `K_C`, `K_S`, `K_V`, and `K_W`
  are physically earned normalized kernels. The lead balance sheet says
  "microscopic reader cascade: typed architecture; stochastic law
  incomplete."
- **Affected claims:** C1, C2, C10, C11.
- **Finding:** C1/C2 survive only as the frozen effective/conditional
  construction: C2 is exact given independently calibrated `eta_j`, `d_j`
  and the local-reader premise; C1's general instrument law is normalized
  given a descended or independently bounded complete reader. The package
  does not contain a complete microscopic SNSPD process.

### P-R-03 — Phenomenological efficiency and dark inputs are honestly charged

- **Severity:** informational confirmation
- **Type:** input accounting
- **Evidence:** the preparation packet labels efficiencies and per-window dark
  probabilities as independent local physical inputs; the one-mode law keeps
  all dark/no-click/multipair branches. The microscopic reader packet permits
  local calibration only away from the held-out target.
- **Affected claims:** C1, C2.
- **Finding:** I found no hidden claim that efficiency or dark probability is
  generated from Simon's mean equations. The complete threshold law is not a
  detector-origin theorem.

### P-R-04 — Detector tomography and fitted controls are not relabeled as
origin

- **Severity:** informational confirmation
- **Type:** provenance / target-leakage audit
- **Evidence:** `2110.10484v1` reconstructs target POVMs; `1301.3337v2`
  reconstructs target response probabilities/efficiency; `1702.02813v1` and
  `2503.17146v1` retain fitted controls. R1 forbids target POVMs, click tables,
  target-fitted efficiencies, and target-fitted hidden-state models.
- **Affected claims:** C1, C2, C11.
- **Finding:** No target POVM, click table, or fitted complete detector
  response is called independently derived in the pinned object.

### P-R-05 — Memory limits the independent-window one-mode reader

- **Severity:** medium scope, non-defeating
- **Type:** physical-domain / composition
- **Evidence:** `2206.04032v2`, equations (60)--(75), makes the current-window
  count law depend on previous windows under continuous operation; a
  Markovian approximation has explicit recovery/window conditions. The
  frozen reader packet requires a sufficient memory carrier.
- **Affected claims:** C1, C2, C3.
- **Finding:** C2 is a valid explicitly local bounded member, not a generic
  continuous-wave SNSPD law. Extending it without a recovery state would be
  physically false; the frozen bundle does not do so.

### P-R-06 — Stable-record physics is a typed contract, not a completed
apparatus result

- **Severity:** major scope, non-defeating
- **Type:** physical-record / empirical-status
- **Evidence:** the frozen reader/common-parent objects require amplification,
  persistence, future sufficiency, eraser, uncertainty/crosstalk, and reset
  accounting, but their outcome ladders place operational division closure
  above the reached author-side level. No pinned device run supplies those
  tests or an error budget.
- **Affected claims:** C1, C3, C10, C11.
- **Finding:** The stable-record boundary is not merely a label, because a
  serious physical criterion is printed. It is nevertheless proposed/assumed
  rather than implementation-validated. C3 is a generic conditional theorem
  on licensed stable prefixes, not a proof that the real SNSPD boundary has
  passed all stability tests.

### P-R-07 — No fabricated-device or cross-device no-refit result exists

- **Severity:** scope-critical, non-defeating
- **Type:** empirical-status
- **Evidence:** none of the seven detector sources supplies the entire frozen
  cascade and stored-record law without target fitting; the lead and MRD
  outcome ladders explicitly say implementation transfer was not run.
- **Affected claims:** C1, C2, C11.
- **Finding:** The bundle earns an effective baseline and exact conditional
  member, not MRD-L3/L4 or SYN-R1-L3 transfer.

### P-R-08 — Amplification does not supply microscopic actuality

- **Severity:** major conceptual scope, non-defeating
- **Type:** physical-source / actuality boundary
- **Evidence:** every detector source predicts or reconstructs responses under
  a supplied quantum/statistical framework. None supplies one
  ordinary-positive, source-complete law selecting a unique microscopic
  history and yielding the instrument as a secondary quotient. The frozen
  reader audit explicitly separates record evidence from latent cause.
- **Affected claims:** C10, C11, C12.
- **Finding:** R1 correctly rejects promotion from a large pulse or durable
  bit to a microscopic ontology or gravity-ready source.

---

## 5. P-R conclusion

The detector chain is physically serious as an architecture. It identifies
the absorber, cascade, switching, circuit, comparator, memory, storage, and
eraser coordinates needed to turn quantum field input into a retained record,
and it proves exact normalization once their kernels are supplied. It does not
currently derive all those kernels from microscopic physics. In particular,
Simon et al. predicts a threshold control, not the complete stochastic reader;
Fano/jitter/memory papers add fitted or effective coordinates; stable-record
closure has not been tested on a fabricated device; and no no-refit transfer
exists.

These are not hidden defects: they are printed limits of the frozen lead and
dependencies. I found one low-severity source-precision issue (which model owns
the Figure 4 best-fit parameter) but no false central P-R claim requiring D1
or D2.

---

## 6. Exact scoped disposition

- **D0 — PROCEDURAL INVALID:** not selected; authentication and independence
  passed.
- **D1 — REJECT:** not selected; no false load-bearing detector/source claim
  defeats the advertised conditional scope.
- **D2 — REVISE-BEFORE-ACCEPTANCE:** not selected; microscopic, stability, and
  transfer debts are already part of the frozen semantics. P-R-01 is a source
  reading constraint, not a required byte repair.
- **D3 — ACCEPT-WITH-SCOPE:** **selected for Seat P-R.** The package
  establishes an effective typed reader architecture and an exact normalized
  bounded threshold-click member given independently calibrated reader
  parameters and supplied quantum composition. It does not establish a
  complete microscopic detector process, validated stable division,
  fabricated-device no-refit transfer, one-run actuality, native ontology,
  gravity, or unification.
- **D4 — ACCEPT:** not selected on this axis because the review must preserve
  the conditional-reader and unvalidated-stability limits above.

**Signed P-R disposition:** `D3 — ACCEPT-WITH-SCOPE`.

## 6.1 Required normalized self-signature

LF line count: 0000000428
Byte count: 0000023717
Normalized self-SHA-256: 4bfd3f434871d8e900c812b1e9af32b920ec3644645fcc97c39fc76db81bd012
Normalization rule: In this report's exact LF-terminated UTF-8 bytes, replace
every ASCII decimal digit on the `LF line count:` and `Byte count:` lines by
zeroes, and replace exactly the 64 lowercase hexadecimal digits on the
`Normalized self-SHA-256:` line by zeroes, preserving every other byte.
