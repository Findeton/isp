# ISP v17 R1 independent review — Seat P joint disposition

## Joint physical-source and physical-reader report

**Seat axis:** P, comprising separately reviewed P-S source/optics and P-R
reader/detector subreports  
**Reviewer task:** `/root/r1_review_physics`  
**Review object:** the immutable R1/native-source-gap bundle pinned by
`v17/note-r1-native-source-gap-independent-review-pin.md`  
**Review mode:** read-only, exact-source, mutually blind from Seats M and O  
**Signed joint recommendation:** **D3 — ACCEPT-WITH-SCOPE**

This is a third standalone report object. It does not replace the separately
signed P-S and P-R evidence. I inspected no sibling-seat report, communicated
with no other seat, and made no repository edit, stage, or commit.

---

## 1. Joint authentication

### 1.1 Pin and chronology

- Review began at repository `HEAD`
  `befe415017d0ea1f13ed965f07ebb39236864497`, exactly the pin commit.
- The pin was 534 LF lines and 26,150 bytes.
- Its ordinary SHA-256 was
  `617223214d37fb37a2e896b9ac6b019b0d7040b4dcef6c9410d52abfebb8c9e8`.
- Its independently recomputed normalized self-SHA-256 was
  `91c5451004d7f8a5988310084402629f305dabf73ccab0934743d209ec7c5bff`,
  matching the printed signature.
- All sixteen repository review objects matched the exact section-2 hashes
  (16/16): one lead, eight direct dependencies, and seven secondary
  dependencies. P-S/P-R scientific inspection used only the authenticated
  lead and their load-bearing dependencies.

### 1.2 Twenty-one exact PDF receipts

Every source was rehashed directly from the freshly retrieved files in
`/tmp/isp-r1-review-sources.6Tgm6Y`. No mismatch or byte normalization
occurred.

| exact PDF | bytes | SHA-256 | result |
|---|---:|---|---|
| `0807.3533v3.pdf` | 209986 | `5e711d3cc54fd900d9b66f06c6333bf12b17accd5b82a855f9f58319373cc151` | match |
| `0904.4483v2.pdf` | 602175 | `18f8af26f5da951f44ec971038c5bbbfd06773f9ad009dce8d654f54e760f558` | match |
| `1001.2472v1.pdf` | 143551 | `f9a860fa106b952fcc61e8a8eb045cb176a7331a492ab31b1668282064945eff` | match |
| `1011.6451v3.pdf` | 816822 | `71bc890fc29e1ea180306b387ae27982735fd73243492f01ad85cc8737a31d20` | match |
| `1109.6193v1.pdf` | 137174 | `e7752704fa2bcc3b8bc7f101c76191172aefbeca469853342aec1fc89d7f5b4a` | match |
| `1301.3337v2.pdf` | 1823254 | `08a63685f214d390f5c20a7c7e6966f865edebed874a1867f45b5c3283c1ce19` | match |
| `1702.02813v1.pdf` | 2020132 | `41c1d9987342691124014f7c5f704b153fdb593756c3dcaa4d611d92372bd859` | match |
| `1807.10885v1.pdf` | 1816147 | `6e44fb0b890cc726fbc54dbe5c86983cbc38968aec77efb3e4029bac55b162a3` | match |
| `2010.00517v1.pdf` | 4136988 | `223f0531c8ad72d2b550bbc9191bf9086d3b319d9391cd1fc1ca1491aaa05155` | match |
| `2110.10484v1.pdf` | 455830 | `446c204ba680f736ac3e13454aa5a6ab21c27753f3d82ef69ff9990b9a7e4bae` | match |
| `2206.04032v2.pdf` | 1030040 | `d3c05804da500d65066711b23339babf939ff64cc57fe0529ca66aff609184a4` | match |
| `2302.10778v3.pdf` | 737089 | `5248a25174f6149b1aeafdaf4ce225708123f608e489ff8132beed3f8d2bcd48` | match |
| `2306.00781v3.pdf` | 3406402 | `d4a2794f3bcfe0024242d00a69ae276ba10ba81515555f487c5798c80551db8e` | match |
| `2309.03085v2.pdf` | 671602 | `6a6eda580939e6859f2ea47f05d5490640e2ad87a97aab3f2e57dff4a86f863b` | match |
| `2501.13791v3.pdf` | 26618133 | `802398f49122a43d237d3e405aada43e44cc20799fd62145d1d517f8d8bba08a` | match |
| `2503.02062v1.pdf` | 204499 | `296638b24cafbb2e6df50829e2e67a65fa23b475e7ddc72b0b1ecf51bf5fa2ee` | match |
| `2503.17146v1.pdf` | 2147662 | `bcfbd9a5ece27e5c1e6055dfbc00e55d962f4134d2bf8d318962916430015822` | match |
| `2507.21192v1.pdf` | 717067 | `109cfcf80e59f10023673395c4f5200d5a3e5894b9a3a99855d7f402edf064aa` | match |
| `2608.04354v1.pdf` | 401093 | `54f24d6bafb8af235223f2e7076b725090cfe0502525cca2dccf33c68f7858a5` | match |
| `mtrl-th_9508006v1.pdf` | 122831 | `4aeba0566cdbe18c5acab78db1cedb308f072bb53e8384e0c07194a7569c3d31` | match |
| `quant-ph_0206125v1.pdf` | 287960 | `c41f2157ad1ad5967ab378416b0a02449750e9b5b318c88fd2016d7163f04448` | match |

All 21 exact source receipts therefore passed.

---

## 2. Joint independent reconstruction

### 2.1 The physical chain that is actually earned

The authenticated material/source papers support the following conditional
chain:

1. measured geometry plus a supplied causal linear response determine a
   retarded Green tensor and the MQED loss/noise representation;
2. a supplied nonlinear susceptibility, real pump/reference, and boundary
   state determine a nonlinear pair kernel under standard QFT;
3. in the undepleted quadratic/Gaussian regime, the common kernel determines
   relative phase, mode/gain data, vacuum/one/multipair weights, and lossy
   quantum propagation;
4. a fully specified normalized quantum instrument determines an ordinary
   positive complete record law; and
5. the exact one-mode R1 member instantiates step 4 with independently supplied
   local efficiencies, dark probabilities, and an independent-reader premise.

This is a real reduction relative to importing a target wavefunction, target
transfer matrix, target fringe, fitted heralded state, POVM, or click table.
The source phase and the destructive output are computed by one common
boundary law rather than inserted per apparatus.

### 2.2 The chain that is not earned

The exact detector papers do not jointly generate the full reader in step 4
from microscopic material data. Simon et al. supplies mean
quasiparticle/phonon dynamics and a threshold-current control after an assumed
absorption/phonon-bubble start. Separate sources model or reconstruct Fano
smearing, jitter, detector POVMs, empirical intrinsic response, realistic
quantum trajectories, and recovery memory. Several contain fitted or
independently calibrated parameters. They are not one mutually validated
event-level cascade for a fabricated device.

Likewise, the stable-record objects print physically meaningful requirements
for amplification, persistence, future sufficiency, erasure, uncertainty,
crosstalk, reset, and resource accounting, but no pinned implementation has
passed those tests. The full physical chain is therefore an effective
architecture plus one exact conditional member, not a complete microscopic
reader law or a real-apparatus division certificate.

### 2.3 Composition and ontology remain supplied

Chiribella, D'Ariano, and Perinotti `0904.4483v2` supplies the quantum-comb
and link-product framework for composing already quantum states, channels,
measurements, and memory channels. `1011.6451v3` reconstructs finite-dimensional
quantum theory from a substantial operational-probabilistic substrate and
explicit principles, including purification. Neither paper derives its
physical system types, circuit order, readers, material source, or actual
configuration law from the R1 boundary packet.

The four exact Barandes sources establish broad stochastic/Hilbert
representation capacity and articulate an indivisible-stochastic ontology.
They begin with a configuration space and stochastic dynamical law or a
stochastic matrix, and then construct/associate Hilbert, Born, or unitary
representations. The Born/unistochastic dilation in `2608.04354v1` is
explicitly nonunique at the representation level. These results do not give
the reverse, target-blind physical map

`material descriptors -> the actual indivisible stochastic law`.

Therefore R1's C11 conclusion is correctly open rather than negative: the
native source law is absent from this bundle, but Barandes's ontology is not
refuted.

---

## 3. Joint generated/supplied/fitted/proposed ledger

For this disposition, **supplied** includes independently measured,
independently calibrated, effective-calculation, and assumed nomological
inputs; the more specific subtype is printed where important.

| coordinate | joint status | physical reading |
|---|---|---|
| background dimension, causal geometry, distance, external lab time | supplied/assumed | not emergent |
| geometry, boundaries, assembly, wiring | supplied/independently measured | contingent apparatus packet |
| linear conductivity/constitutive response | supplied/measured or effective | MQED premise |
| retarded Green tensor and linear loss response | generated conditionally | Maxwell/MQED output |
| MQED quantization, FDT completion, Born/instrument composition, `hbar` | supplied nomology | not generated by positive records |
| nonlinear susceptibility | supplied/measured or effective | TDDFT controls do not make it fundamental |
| real pump waveform/reference | supplied/independently calibrated | contingent physical source |
| incoming vacuum/thermal quantum state | supplied/assumed | state-selection law absent |
| nonlinear pair kernel and relative phase | generated conditionally | common physical boundary calculation |
| mode/gain data and Gaussian pair-number law | generated conditionally | undepleted quadratic domain |
| absolute brightness | proposed generated transfer coordinate | corrected convention; no scored transfer |
| target transfer matrix/fringe/state/process | fitted/reconstructed forbidden input | no evidence of leakage |
| detector material, bias, bath, circuit, comparator | supplied/independently characterized | contingent reader packet |
| mean quasiparticle/phonon/order-parameter dynamics | generated conditionally | not event-level process |
| detector threshold-current control | generated conditionally | Simon scope only |
| Fano distribution/tails | fitted/effective or proposed microscopic output | not uniquely generated |
| jitter/timing distribution | fitted or independently calibrated input | not uniquely generated |
| switching/dark hazards | supplied/calibrated/fitted or proposed | normalized formula does not derive rates |
| efficiency and per-window dark probabilities | supplied/independently calibrated | explicitly charged in C2 |
| recovery/dead-time/memory kernel | supplied/calibrated or proposed | memoryless law nongeneric |
| circuit/noise waveform | generated conditionally from supplied circuit/noise model | no universal circuit descent |
| storage/persistence/reset/eraser law | proposed and/or supplied physical interface | not implementation-validated |
| complete bounded threshold-click law | generated conditionally | exact C2 member given local inputs |
| general complete detector event law | proposed conditional architecture | microscopic kernels not all earned |
| stable-record division | proposed physical boundary plus supplied/derived sector assumptions | no apparatus error budget |
| actual selected microscopic history | absent | amplification is not actuality |
| separately built no-refit transfer | absent/proposed | not run |
| native ordinary-positive source-complete law | absent/open | no universal no-go claimed |
| spacetime, gravity, unification | absent | C12 correct |

**Joint classification result:** the frozen bundle correctly identifies every
load-bearing coordinate as generated, supplied/independently calibrated,
fitted/forbidden, assumed, or proposed, provided that C1's phrase "complete
bounded record law" is read through the explicitly frozen conditional reader
contract. That qualification is already present in the lead's sections 5,
15, 17, 20, and 22 and in the reader/common-parent dependencies; it is not a
new repair.

---

## 4. Numbered joint findings

### P-J-01 — The effective source compression is physically real

- **Severity:** positive load-bearing confirmation
- **Type:** physical-source
- **Evidence:** authenticated MQED/SPDC sources and the common-boundary R1
  equations generate Green response, relative phase, modes/gains, multipair
  weights, and the one-mode interference law from narrower material/boundary
  inputs; target transfer/fringe/state/POVM inputs are forbidden and absent.
- **Affected claims:** C1, C2.
- **Finding:** R1 is not merely a click-table compiler at its bounded scope.
  It conditionally generates significant cross-apparatus structure under
  fixed quantum nomology.

### P-J-02 — C1's completeness is conditional on more than detector state and
wiring

- **Severity:** major scope, non-defeating
- **Type:** physical-source / semantic-scope
- **Evidence:** lead section 4's full boundary packet includes reader/storage
  facts, section 5 normalizes only when every reader is a normalized
  instrument, section 15 says microscopic reader closure is incomplete, and
  the R1 member says "given a physically descended or independently bounded
  reader." Exact detector sources do not supply all event kernels.
- **Affected claims:** C1, C2, C10, C11.
- **Finding:** "Detector state and wiring" cannot by itself mean that present
  first-principles detector physics determines the full retained-record law.
  It is shorthand for the frozen boundary/instrument contract, which includes
  independently bounded reader parameters and proposed storage/stability
  structure. With that already printed reading, C1 survives at D3 scope. A
  microscopic/no-refit reading would be false.

### P-J-03 — Reader efficiencies, dark rates, and memory are not hidden outputs

- **Severity:** medium scope, non-defeating
- **Type:** input accounting / detector physics
- **Evidence:** C2 and the preparation packet explicitly supply `eta_j` and
  `d_j`; Uzunova-Semenov demonstrates previous-window recovery memory;
  Simon/Kozorezov/Sidorova do not uniquely generate all detector statistics.
- **Affected claims:** C1, C2, C3.
- **Finding:** The exact one-mode law is complete over its declared alphabet
  and normalized, but it is an effective local-reader member, not a universal
  detector law.

### P-J-04 — Stable-record physics is specified but not certified on hardware

- **Severity:** major scope, non-defeating
- **Type:** physical-record / empirical-status
- **Evidence:** the reader/common-parent objects require amplified carriers,
  persistence, future sufficiency, erasers, uncertainty/crosstalk, reset, and
  energy/resource accounting; their own outcome ladders say operational
  division closure and implementation transfer are not reached.
- **Affected claims:** C1, C3, C10, C11.
- **Finding:** R1 avoids a label-only record definition, but the real physical
  boundary remains proposed/conditional. No one-run actuality follows.

### P-J-05 — One source-precision qualification is required for Simon et al.

- **Severity:** low
- **Type:** source-scope precision
- **Evidence:** in `2501.13791v3` Figure 4(a), the best-fit `eta = 0.2` belongs
  to the phenomenological diffusive-hotspot comparator; the ab-initio curve is
  separate and uses informed/approximate parameters plus a strong-coupling
  rescaling.
- **Affected claims:** C1, C10, C11.
- **Finding:** The frozen phrase "device comparison includes a best-fit
  hotspot parameter" is accurate only with this ownership made explicit.
  This does not alter the lead's conclusions.

### P-J-06 — No target-equivalent source or detector object leaked into R1

- **Severity:** informational confirmation
- **Type:** provenance / hostile-control audit
- **Evidence:** Suess is used as transfer-characterization control; Fitzke and
  Renema are used as detector-tomography controls; fitted Fano/jitter laws are
  not promoted. The frozen input firewall forbids every such payload.
- **Affected claims:** C1, C2, C11.
- **Finding:** No assembled transfer matrix, target fringe/state, fitted POVM,
  click table, or fitted complete detector response is called independently
  generated.

### P-J-07 — Barandes representation capacity does not close the native-source
arrow

- **Severity:** major conceptual scope, non-defeating
- **Type:** physical-source / ontology boundary
- **Evidence:** the exact Barandes papers begin with an indivisible stochastic
  law or stochastic matrix and construct a secondary Hilbert/Born/unitary
  representation. They do not derive the physical stochastic law from R1's
  material boundary data. Chiribella et al. likewise assumes an operational
  substrate and composition principles.
- **Affected claims:** C9, C10, C11.
- **Finding:** The native-source gap is correctly located. It is not a
  refutation of ordinary-positive ontology and not evidence that Hilbert
  structure is fundamental.

### P-J-08 — No-refit transfer, microscopic actuality, and gravity are absent

- **Severity:** scope-critical, non-defeating
- **Type:** empirical-status / ontology / gravity ceiling
- **Evidence:** no source or pinned construction executes a separately built
  end-to-end transfer; detector amplification does not select one latent
  history; the whole stack assumes background spacetime/time and supplies no
  reciprocal matter-geometry law.
- **Affected claims:** C1, C2, C10, C11, C12.
- **Finding:** The synthesis may validate the map of the fixed-background
  problem, not a native ontology, actuality mechanism, spacetime theory,
  gravity theory, or unification.

---

## 5. Joint physical disposition

The P axis finds a coherent, genuinely useful fixed-background baseline. The
optical source part earns more than curve fitting: relative phase and
multipair/interference structure descend conditionally from a common material
boundary calculation. The detector part earns less than a microscopic reader:
its exact complete member receives local phenomenological reader inputs, and
its more ambitious absorption-to-storage chain remains a typed conditional
architecture. The lead generally preserves this distinction, and its own
balance sheet supplies the necessary narrowing.

No P-S or P-R evidence defeats the synthesis at the frozen advertised scope.
The important qualifications are scope constraints already entailed by its
bytes, not candidate repairs.

---

## 6. Exact joint D0--D4 disposition

- **D0 — PROCEDURAL INVALID:** not selected. Pin, commit, sixteen objects,
  twenty-one exact source receipts, chronology, and independence authenticated.
- **D1 — REJECT:** not selected. No false load-bearing physical-source claim,
  target-payload leak, or source contradiction defeats the conditional
  baseline.
- **D2 — REVISE-BEFORE-ACCEPTANCE:** not selected. The microscopic-reader,
  stable-division, no-refit, actuality, and gravity limitations are already
  explicit frozen semantics. The Simon wording requires source-accurate
  reading, not a new candidate.
- **D3 — ACCEPT-WITH-SCOPE:** **selected jointly.** R1 establishes the frozen
  fixed-background source-to-record baseline and native-source-gap diagnosis,
  conditional on supplied quantum composition, background geometry/time,
  material response, boundary state, and a physically descended or
  independently bounded reader. It includes an exact complete bounded
  threshold-click member. It does not establish a complete microscopic reader
  law, hardware-certified stable division, no-refit transfer, native ontology,
  one-run actuality, spacetime, gravity, or unification.
- **D4 — ACCEPT:** not selected because the P axis must enforce the
  conditional-reader and unexecuted-transfer qualifications above.

**Signed joint disposition:** `D3 — ACCEPT-WITH-SCOPE`.

No repair, successor, ontology promotion, implementation, chronology,
spacetime, or gravity unit follows from this report.

## 6.1 Required normalized self-signature

LF line count: 0000000350
Byte count: 0000019713
Normalized self-SHA-256: a315b6d81f8b2ebf7763e466f5dc234ce1fcf10edb6f29e91f282b881534d4f5
Normalization rule: In this report's exact LF-terminated UTF-8 bytes, replace
every ASCII decimal digit on the `LF line count:` and `Byte count:` lines by
zeroes, and replace exactly the 64 lowercase hexadecimal digits on the
`Normalized self-SHA-256:` line by zeroes, preserving every other byte.
