# ISP v17 R1 independent review — Seat P-S

## Macroscopic QED, source, and nonlinear-optics subreport

**Seat:** P-S (physical source / optics)  
**Reviewer task:** `/root/r1_review_physics`  
**Review object:** the immutable R1/native-source-gap bundle pinned by
`v17/note-r1-native-source-gap-independent-review-pin.md`  
**Review mode:** read-only, source-first, independent  
**Signed recommendation:** **D3 — ACCEPT-WITH-SCOPE (P-S axis)**

I inspected no sibling report and communicated with no other review seat. I
made no repository edit, stage, or commit. This report is a logically separate
P-S object; agreement with P-R or root cannot substitute for the evidence
below.

---

## 1. Authentication

### 1.1 Chronology and pin

- Repository `HEAD` during review was exactly
  `befe415017d0ea1f13ed965f07ebb39236864497`, the commit that adds the pin.
- The pin contained 534 LF-terminated lines and 26,150 bytes.
- Ordinary SHA-256 of the pin was
  `617223214d37fb37a2e896b9ac6b019b0d7040b4dcef6c9410d52abfebb8c9e8`.
- I independently normalized the three self-signature lines according to the
  pin's rule and obtained
  `91c5451004d7f8a5988310084402629f305dabf73ccab0934743d209ec7c5bff`,
  exactly the printed normalized self-SHA-256.
- The pin was LF-only, ended in exactly one LF, and had no trailing horizontal
  whitespace.

### 1.2 Repository bundle

I directly rehashed all sixteen pinned repository objects: the lead synthesis,
all eight direct dependencies, and all seven secondary dependencies. Every
digest matched section 2 of the pin byte for byte (16/16). I then read the lead
and the P-S-load-bearing material, preparation, reader-interface, common-parent,
and R1-member objects at those authenticated bytes. The later untracked
`v16/note-handoff-prompt-2026-08-22.md` was unrelated and was not inspected.

### 1.3 Exact source receipts

I directly rehashed all twenty-one PDFs in
`/tmp/isp-r1-review-sources.6Tgm6Y`; all byte counts and hashes matched the pin
(21/21). The P-S packet used below authenticated as follows:

| exact PDF | bytes | SHA-256 |
|---|---:|---|
| `1109.6193v1.pdf` | 137174 | `e7752704fa2bcc3b8bc7f101c76191172aefbeca469853342aec1fc89d7f5b4a` |
| `0807.3533v3.pdf` | 209986 | `5e711d3cc54fd900d9b66f06c6333bf12b17accd5b82a855f9f58319373cc151` |
| `2306.00781v3.pdf` | 3406402 | `d4a2794f3bcfe0024242d00a69ae276ba10ba81515555f487c5798c80551db8e` |
| `mtrl-th_9508006v1.pdf` | 122831 | `4aeba0566cdbe18c5acab78db1cedb308f072bb53e8384e0c07194a7569c3d31` |
| `1001.2472v1.pdf` | 143551 | `f9a860fa106b952fcc61e8a8eb045cb176a7331a492ab31b1668282064945eff` |
| `1807.10885v1.pdf` | 1816147 | `6e44fb0b890cc726fbc54dbe5c86983cbc38968aec77efb3e4029bac55b162a3` |
| `2503.02062v1.pdf` | 204499 | `296638b24cafbb2e6df50829e2e67a65fa23b475e7ddc72b0b1ecf51bf5fa2ee` |
| `2010.00517v1.pdf` | 4136988 | `223f0531c8ad72d2b550bbc9191bf9086d3b319d9391cd1fc1ca1491aaa05155` |

No author summary was used as a substitute for these exact PDFs.

---

## 2. Independent reconstruction

### 2.1 What the macroscopic-QED layer really supplies

Buhmann, Butcher, and Scheel `1109.6193v1`, especially the constitutive
equation and Green-tensor construction in its field-quantization section,
starts with a causal conductivity kernel/tensor and derives the corresponding
Green tensor, noise current, field operators, and fluctuation-dissipation
relations for general linear absorbing media, including nonlocal and
Onsager-violating response. The conductivity is not derived by that paper.
Nor does it supply a nonlinear susceptibility, a pump state, a source-body
preparation, or a detector.

Therefore the R1 map

`geometry + causal linear response -> retarded Green tensor + loss/noise`

is a genuine conditional output, while geometry, causal response, background
spacetime/time, field quantization, and the environment state remain inputs.
This is the distinction printed in C1, C10, C11, and C12.

### 2.2 Low-gain and high-gain nonlinear source domains

Mitchell `0807.3533v3` derives narrow-band paraxial SPDC amplitudes and
absolute single-spatial-mode brightness by a Green-function/mode-overlap
method, and relates SPDC to the corresponding classical sum-frequency
conversion efficiency. The scope is explicitly narrow-band and paraxial; the
nonlinear response, pump, modal boundary conditions, and quantum field rule are
supplied.

Krstić, Setzpfandt, and Saravi `2306.00781v3` supplies the stronger
arbitrary-gain Green-function treatment for open, lossy, dispersive
structures. Its exact ceiling is equally explicit: arbitrary gain is only
within an undepleted *classical* pump approximation. The worked formulation
also assumes an isotropic system and a real, nondispersive `chi(2)` response;
nonlinear material noise and pump depletion/quantization are outside the
member. Vacuum is the initial state used for the evaluated correlation
functions, although the formalism discusses non-vacuum generalization.

Thus R1 correctly distinguishes:

- perturbative/narrow-band/paraxial controls;
- arbitrary linear loss and dispersion;
- arbitrary parametric gain under a quadratic Gaussian and undepleted-pump
  premise; and
- the unearned pump-depleted, quantized-pump, nonlinear-noise, and general
  interacting-QFT regimes.

No PDF supports reading "high gain" as "arbitrary pump depletion."

### 2.3 Susceptibility is effective input, not secretly derived ontology

Dal Corso, Mauri, and Rubio `mtrl-th_9508006v1` computes static `chi(2)` in
LDA and a time-dependent GaP control in TD-LDA, with pseudopotential,
exchange-correlation, lattice, and band-gap limitations. Luppi, Hübener, and
Véniard `1001.2472v1` derives a TDDFT second-order-response formalism and
compares GaAs spectra with experiment, but the implemented comparison uses a
0.8 eV scissor shift and a model long-range `alpha/q^2` kernel to recover the
excitonic magnitude. These are serious first-principles/effective controls;
they are not a derivation of the fabricated source's complete nonlinear
response from an ontology-free law.

The frozen R1 classification of `chi(2)` as "independently
measured/effective" is therefore correct. Calling either paper a no-input
fabricated-device descent would be false; the reviewed bundle does not do so.

### 2.4 Relative phase, gain, modes, and number statistics

Given one common geometry, Green tensor, real pump/reference, `chi(2)`,
boundary state, mode convention, and standard quantum composition, the R1
source kernel is a common-boundary calculation. Its relative phases are not a
separate fringe table. A Schmidt/Bloch-Messiah reduction then yields modes and
gains, and the undepleted Gaussian source yields the product of two-mode
squeezed-vacuum number laws.

Schneeloch et al. `1807.10885v1` explicitly derives the two-mode-squeezed
description, geometric pair-number statistics, multimode products, absolute
rate formulae, and the limit of the undepleted-pump treatment. These support
the one-mode R1 law only after its supplied pump, susceptibility, boundary,
mode, and quantum premises are charged. They do not source the Born rule or
the contingent vacuum state.

I found no evidence that R1 imports a target fringe, target state, target
phase, fitted source gain, or target click table into the source calculation.
The source phase/gain/number coordinates are generated *within R1*, not native
outputs from premise-free positive physics.

### 2.5 Brightness convention and correction

Schneeloch `2503.02062v1` corrects the earlier conflation of quantization
dimensions with nonlinear-medium dimensions and derives a refractive-index
dependent, order-unity correction to absolute pair rates. The paper says the
quantization-volume factors disappear on transformation to continuous
Gaussian spatial modes, and prints device-dependent corrections (including
roughly 1.006, 1.092, and 1.030 in its comparison table).

The frozen R1 member requires the field/mode normalization in its
`C_QED` convention to be fixed and forbids repairing brightness by a target
fit. It also says no implementation transfer has been run. That is consistent
with the correction source. The review bundle does not present a numerical
absolute-brightness prediction whose propagation I could independently score;
brightness remains an unexecuted transfer coordinate rather than a false
validated claim.

### 2.6 Assembled transfer characterization is a hostile control

Suess et al. `2010.00517v1` reconstructs the rows of a linear-optical transfer
matrix from coherent illumination and intensity data by PhaseLift. Each row is
recovered only up to an output-row phase. The experiment also states that
absolute circuit loss cannot be separated from detector efficiency in that
setup; only relative row losses are reconstructed. Its two-photon comparison
and polar/gauge alignment yield high circuit fidelity, but the object is
target-characterization data.

R1 uses this source as an assembled-transfer *control* and expressly forbids
a target transfer matrix or information-equivalent effective response as an
input. It does not call the PhaseLift reconstruction native material descent.

### 2.7 No-refit transfer

No exact source in this packet reports the frozen R1 stack, with independently
fixed material/source/reader inputs, predicting the complete retained-record
law of a separately built held-out apparatus without refit. The R1 lead and
dependencies state this explicitly. C1 and C2 are therefore construction and
conditional-member claims, not SYN-R1-L3 empirical-transfer claims.

---

## 3. Coordinate classification

The status words below mean: **generated** = an output of the frozen R1 rule
conditional on its inputs; **independently calibrated** = a contingent
empirical input measured away from the held-out score; **fitted** = inferred
from target-equivalent output and therefore a control/forbidden payload;
**assumed** = nomology, boundary condition, or approximation premise; and
**proposed** = a physically motivated construction step not yet executed or
validated in a no-refit implementation.

| load-bearing coordinate | P-S classification | reason |
|---|---|---|
| laboratory dimension, causal order, distance, external time | assumed / independently measured | background laboratory structure, not an output |
| source-body geometry, ports, boundaries, wiring | independently calibrated input | metrology/fabrication packet |
| causal linear conductivity/constitutive response | independently calibrated or effective input | MQED starts from it |
| retarded Green tensor and linear loss channels | generated conditionally | solution of supplied Maxwell response problem |
| MQED noise-current completion | generated conditionally under assumed QFT/FDT | not classical-material ontology |
| nonlinear susceptibility `chi(2)` | independently calibrated or effective-calculation input | LDA/TDDFT controls retain approximations |
| real pump waveform and phase reference | independently calibrated contingent input | not a target fringe |
| positive-frequency pump representation | generated conditionally | Green propagation of the real source |
| incoming vacuum/thermal quantum boundary state | assumed contingent quantum state | preparation law remains open |
| quantum composition, complex orientation/real-J equivalent, Born rule, `hbar` | assumed fixed nomology | native-source gap |
| nonlinear pair kernel and relative optical phase | generated conditionally | one common boundary calculation |
| Schmidt/Bloch-Messiah modes and gain parameters | generated conditionally, with numerical truncation proposed/controlled | no click-fit permitted |
| geometric/multimode pair-number statistics | generated conditionally in Gaussian undepleted regime | strong-pump completion open |
| pump depletion, quantized pump, nonlinear material noise | proposed / absent | outside frozen member |
| absolute brightness | proposed generated quantity; not transfer-validated | corrected normalization required; no scored prediction |
| linear-optical transfer matrix from a target device | fitted/reconstructed hostile control | Suess PhaseLift; forbidden as R1 input |
| loss-reservoir state | assumed contingent input | loss propagation generated only after it is supplied |
| regulator, bandwidth, basis, mesh, mode cutoff | assumed computational/approximation inputs | error/resource bounds required |
| separately built no-refit source prediction | proposed / absent | expressly not run |
| target fringe, fitted state, fitted gain, click table | fitted forbidden payload | no evidence of use in R1 |

Every load-bearing P-S coordinate is classified consistently in the frozen
bundle, subject to the scope findings below.

---

## 4. Numbered P-S findings

### P-S-01 — Macroscopic-QED descent is conditional, not material-law generation

- **Severity:** scope-critical, non-defeating
- **Type:** physical-source / source-scope
- **Evidence:** `1109.6193v1` begins with the conductivity kernel and derives
  the Green/noise-field representation; R1 lead sections 4 and 17 list causal
  response, geometry, QFT, and boundary state as inputs.
- **Affected claims:** C1, C10, C11, C12.
- **Finding:** The frozen package states this boundary correctly. C1 must not
  be read as deriving constitutive physics, QFT, spacetime, or the quantum
  boundary state.

### P-S-02 — "Arbitrary gain" does not cross the undepleted/Gaussian wall

- **Severity:** scope-critical, non-defeating
- **Type:** physical-domain
- **Evidence:** `2306.00781v3` repeatedly restricts the arbitrary-loss,
  arbitrary-dispersion, arbitrary-gain formalism to an undepleted classical
  pump and a quadratic interaction; `1807.10885v1` separately analyzes the
  depletion boundary. R1 lead sections 6 and 17 print the Gaussian and
  undepleted scope.
- **Affected claims:** C1, C2.
- **Finding:** The domain is correctly bounded. No pump-depleted or universal
  high-field source claim is earned.

### P-S-03 — Phase/gain/number data are generated only after quantum premises

- **Severity:** major conceptual scope, non-defeating
- **Type:** physical-source / nomology accounting
- **Evidence:** the common Green/source integral and Schmidt reduction in the
  authenticated R1 member generate relative phase and gain from supplied
  geometry/pump/response; `1807.10885v1` supports the conditional squeezed
  number law. The same member explicitly supplies quantum composition and the
  boundary state.
- **Affected claims:** C1, C2, C10, C11.
- **Finding:** These coordinates are not target-equivalent payloads, but
  neither are they a native ordinary-positive source law. The lead gets this
  distinction right.

### P-S-04 — Brightness is methodologically bound but empirically unexecuted

- **Severity:** low
- **Type:** source-scope / calibration
- **Evidence:** `2503.02062v1` prints the refractive-index/quantization-volume
  correction; the R1 member freezes `C_QED`, forbids brightness fitting, and
  reports no implementation transfer.
- **Affected claims:** C1, C2.
- **Finding:** There is no inconsistent scored brightness value in the bundle.
  A later transfer would have to propagate the corrected convention and its
  uncertainty; this review cannot award that transfer now.

### P-S-05 — Transfer-matrix tomography is not misreported as descent

- **Severity:** informational confirmation
- **Type:** source-provenance
- **Evidence:** `2010.00517v1` reconstructs a target transfer matrix from
  intensity/count data, retains row-phase gauge, and cannot separate absolute
  circuit loss from detector efficiency. R1 lists assembled transfer matrices
  and target-equivalent responses as forbidden inputs.
- **Affected claims:** C1, C11.
- **Finding:** I found no transfer-matrix, target-fringe, target-state, or
  fitted complete response leakage into the frozen source calculation.

### P-S-06 — No separately built no-refit source result exists

- **Severity:** scope-critical, non-defeating
- **Type:** empirical-status
- **Evidence:** the authenticated R1 member and lead both say implementation
  transfer was not run; none of the eight exact P-S sources supplies that R1
  test.
- **Affected claims:** C1, C2, C11.
- **Finding:** The package may earn the conditional baseline and exact bounded
  member, but not empirical transfer or universal source completion. This
  limitation is already entailed by the frozen text.

---

## 5. P-S conclusion

The source/optics chain is scientifically useful and honestly priced. It is
more than a fitted fringe compiler: once its material, pump, boundary, and
quantum premises are supplied, one common calculation generates the Green
response, relative source phase, mode/gain data, multipair statistics, and
interference relation. It is less than a native material ontology: linear and
nonlinear response, quantum composition, the boundary state, background
spacetime/time, and approximation data remain payloads, and no held-out
implementation transfer has occurred.

I found no false load-bearing P-S source claim, no concealed target response,
and no source-paper contradiction that requires D1 or D2. The necessary
narrowing is already printed throughout the frozen bundle.

---

## 6. Exact scoped disposition

- **D0 — PROCEDURAL INVALID:** not selected; authentication and independence
  passed.
- **D1 — REJECT:** not selected; no load-bearing false P-S claim was found.
- **D2 — REVISE-BEFORE-ACCEPTANCE:** not selected; the domain and source debts
  are already semantic parts of the frozen object rather than omitted repairs.
- **D3 — ACCEPT-WITH-SCOPE:** **selected for Seat P-S.** The package
  establishes a fixed-background, effective Maxwell--MQED--nonlinear-optics
  source baseline and an exact bounded conditional member. It does not earn
  constitutive-law origin, native positive nomology, pump-depleted completion,
  no-refit transfer, spacetime, gravity, or unification.
- **D4 — ACCEPT:** not selected on this axis because the review necessarily
  enforces the printed effective/Gaussian/undepleted/no-transfer scope and
  records the source limitations above.

**Signed P-S disposition:** `D3 — ACCEPT-WITH-SCOPE`.

## 6.1 Required normalized self-signature

LF line count: 0000000353
Byte count: 0000018648
Normalized self-SHA-256: 5afa3a75cfba431f1b9a7c365415fe17f114e26577dd5fdec8022bd1dcc0302d
Normalization rule: In this report's exact LF-terminated UTF-8 bytes, replace
every ASCII decimal digit on the `LF line count:` and `Byte count:` lines by
zeroes, and replace exactly the 64 lowercase hexadecimal digits on the
`Normalized self-SHA-256:` line by zeroes, preserving every other byte.
