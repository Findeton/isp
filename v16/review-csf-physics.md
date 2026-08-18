# CSF hostile review — relational locality, no-signalling, and physical ontology

Status: **FROZEN INDEPENDENT HOSTILE REPORT**  
Seat: **P — relational locality, no-signalling, and physical ontology**  
Target: v16 Paper 6, candidate commit
`61c32d884d688f49f29d3863fe5959d1053d382e`  
Grade: **REJECT**  
Proposed adjudicated primary: **`CSF-BLOCKED-AT-HISTORY-INDIVIDUATION`**

## 1. Immutable-target and hash audit

I read the complete frozen CSF protocol before substantive work, then the
complete pin, generic-core freeze, physical fixture/refusal/repair freeze,
candidate verification, core, scorer, fixture, transcript, receipt, and Paper
6. I did not read, list, request, infer, or communicate with either other CSF
review seat.

All immutable hashes reproduce:

| object | bound SHA-256 | observed |
|---|---:|---:|
| pin | `c953618c66685b20705bef7436ebfa29d4b0370b076493bc1997aea898e1bcba` | equal |
| generic core | `93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4` | equal |
| physical fixture | `8c10210b6fee0a5477f3f70593cca080c26a4c91d678ad60bf691f6d853fbd37` | equal |
| repaired scorer | `d3adf994e1c89fca5b53a0969cf0eed256488790b361477116b7cd1a76da84ba` | equal |
| freeze/refusal/repair record | `b2a140a123cab91fe1aba19a87aa2ee9d9c09c97992260338123b3bd7be1ddf1` | equal |
| transcript | `59077d8ad0f9e9ba4cf5afc0a44fea242d7a6032f1d998e088b3433cf4541785` | equal |
| receipt | `7ae9b4a17fd38883bbff39b212f0edf819e2edf17942c9d54f8cf9f772414fdc` | equal |
| Paper 6 | `543a2c927ecc7bd184fc758e4d72ebd4d4974327ae5ae2bb279d1fe33086c5d9` | equal |
| candidate verification | `c0b3e7072ae2ba5a5fe45e1a26c988d36fe989b33cb02e71e57490db077b7cd5` | equal |

The chronology is valid. The first physical invocation refused without
artifacts on an absent anchor adjective; the frozen one-token repair changes
`erasable` to the existing `eraser` anchor. It does not change a scientific
object.

A clean scratch run reproduces all three artifacts byte for byte. I
independently recomputed the eight receipt seals, 30 passing gates, 12
one-occurrence claims, exact outer hashes, and zero float literals. All 36
registered mutants refuse without artifact writes at their bound gate.

## 2. Independent method and tools

The source-free exact reconstruction is
`/private/tmp/csf-physics-review.ZaYo3G/independent_check.py`. It imports no CSF
module and reads no CSF artifact. It solves the Hermitian-coordinate systems,
JCV kernels, calibrated factorizations, and Bell marginal with exact
`Fraction` arithmetic.

Primary-source type checks used here are:

1. Davies and Lewis, *An operational approach to quantum probability*,
   [Commun. Math. Phys. 17, 239 (1970)](https://doi.org/10.1007/BF01647093),
   introduced quantum instruments as outcome-resolved operations. This
   supports CSF's distinction between an unconditioned channel and a retained
   calibrated outcome instrument.
2. Choi, *Completely positive linear maps on complex matrices*,
   [Linear Algebra Appl. 10, 285 (1975)](https://doi.org/10.1016/0024-3795(75)90075-0),
   supplies the finite-dimensional complete-positivity/factorization type. It
   supports the PSD/CP mathematics, not a preferred physical kernel.
3. Hughston, Jozsa, and Wootters, *A complete classification of quantum
   ensembles having a given density matrix*,
   [Phys. Lett. A 183, 14 (1993)](https://doi.org/10.1016/0375-9601(93)90880-9),
   prove that different ensembles of one density matrix can be prepared at a
   distance from a suitable entangled state. This makes CSF's untested remote-
   steering premise physically important rather than optional bookkeeping.
4. Gisin, *Weinberg's non-linear quantum mechanics and supraluminal
   communications*,
   [Phys. Lett. A 143, 1 (1990)](https://doi.org/10.1016/0375-9601(90)90786-N),
   is the primary warning that remotely selectable ensemble structure plus
   decomposition-sensitive nonlinear evolution can signal.
5. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
   [arXiv:2507.21192](https://arxiv.org/abs/2507.21192), makes configuration
   and stochastic process law primary while treating Hilbert-space objects as
   representations. At matched type, CSF selects only a kernel coordinate of
   a declared operator family, not the elementary ontic successor process.

None of these fixed-space results is imported as a fixed-spacetime assumption.

## 3. Exact recomputation table

| quantity | candidate | reviewer | status |
|---|---|---|---|
| context dimensions | `2,2,1,1,2` | exact row ranks give `2,2,1,1,2` | PASS |
| independent training dimension | `5` | sum `2+2+1=5` | PASS, bookkeeping only |
| shared recurrence dimension | `1` | exact stacked rank `3`, dimension `1` | PASS |
| exchange-fixed dimension | `0` | added `p=q` gives rank `4` | PASS |
| selected kernel | `diag(1/2,1/2)` | exact unique solution | PASS |
| held-out contribution | “passes” | adds rank `0`; algebraically redundant with rich training row | MAJOR QUALIFIER |
| JCV first-two kernel | `diag(16/25,9/25)` | exact `C^dagger C` for both | PASS |
| JCV third kernel | `diag(25/169,144/169)` | exact | PASS |
| selected-fiber port statistic | `1` versus `9/25` | exact row-sum probabilities | PASS |
| Bob before/after | `I/2` | `I/2` exactly | PASS |
| amplifier Bob marginal | `2I` | `2I` exactly | PASS |
| doctrine-control prediction | `[1,0]` versus `[0,1]` | literal constants; no state, operator, or probe derives them | FAIL AS PHYSICAL GATE |

Writing `M=[[p,x+iy],[x-iy,q]]`, the three training systems are simply

```text
phase-sign:   p+q=1, x=0,
quarter-sign: p+q=1, y=0,
rich-three:   p+q=1, x=0, y=0.
```

Their common family is already the rich-context family
`diag(p,1-p)`. Exchange invariance then imposes `p=1/2`. The held-out rich
context has the same exact row space and adds no equation. Selection is thus
“rich-spectrum diagonal family plus imposed half-exchange symmetry,” not an
independent multi-context prediction.

For the Bell safety row, the selected local channel is an ordinary dephasing
channel. More generally, any CPTP instrument on a fixed Alice factor obeys

```text
Tr_A sum_j (K_j tensor I_B) rho_AB (K_j^dagger tensor I_B)
= Tr_A rho_AB
```

for every joint input. CSF's one Bell state and amplifier are correct witnesses
of this general fixed-factor, unconditioned theorem.

## 4. Theorem and proof audit

The fixed-history spectrahedral formulation is correct. `M=C^dagger C` is
PSD; completeness is linear in `M`; every finite PSD `M` has a factorization;
and the associated unconditioned map is CP, affine, ancilla-stable, and trace
preserving when `L_V(M)=I`. Outcome-resolved instruments still depend on `C`.

The rich-spectrum theorem is also correct at its scope. Three distinct
eigenphases force the off-diagonal history moment to vanish while leaving the
diagonal bias free. It is ensemble decoherence in one declared history basis,
not actual order, time direction, causal structure, or a permanent record.

The extreme-point negative result is valid: the rank-two singleton is extreme
only after exchange is imposed and becomes interior when that constraint is
forgotten. Extremality is not a context-independent selection principle.

The theorem failure is physical, not algebraic. Nothing in these equations
derives that the same `M` coordinate is one law recurring across the three
contexts, or that the exchange automorphism is a law of nature. Those are the
two assumptions doing the selection.

## 5. Physical-ontology and locality audit

### History individuation is asserted, not built

Each context supplies actor names, two relation pairs, and an anonymous
relative operator. The scorer constructs the history pair as `(I,Omega)`.
Actor names and relation incidence never construct either history map. They
are used only to count three actors/two relations and to check whether a name
swap preserves the bare relation set. The string `tau-binary-neighbor` is not
used to derive a transport or a record.

Therefore the coordinates `left-then-right` and `right-then-left` are named
operator coordinates, not demonstrated configuration-individuated relational
histories. This meets the protocol's earliest blocking outcome. A frozen label
prevents postselection; it does not supply the missing physical referent.

### Recurrence is a universality postulate, not derived locality

Intersecting all context equations in one four-coordinate packet assumes that
the same full kernel recurs. That can be a sensible nomological postulate—the
analogue of requiring the same coupling for independently established copies
of one event type. Here the event-type identity itself is not independently
established by a common bundle, token gluing, or local successor law. Calling
the intersection “recurring locality” would be circular.

Exchange then selects `diag(1/2,1/2)` because it explicitly removes the one
remaining left/right bias. This is conditional symmetry selection of a
maximally unbiased kernel, not derivation of fundamental dynamics.

### The doctrine-control observable is planted

The scorer assigns

```text
{"identity":[1,0], "asymmetric_exchange":[0,1]}
```

directly. It never computes these vectors from a preparation, history maps,
kernel, port coefficients, or calibrated probe. The gate proves two declared
lists differ. It does not prove that recurrence doctrine moves a physical
prediction. The qualifier `RECURRENCE-DOCTRINE-MOVES-PHYSICS` must be killed or
recomputed from a typed observable.

### What CSF actually selects

Conditional on fixed history maps, a common coordinate dictionary, full-
kernel universality, and exchange symmetry, CSF uniquely fixes the
unconditioned coordinate kernel `M=I/2`. It does not select:

- the elementary histories or relational rewrite;
- an ontic stochastic successor law;
- the calibrated instrument `C`;
- a record implementation or permanence;
- actualization; or
- a Hamiltonian representation of repeated dynamics.

In Barandes-inspired terms, `M` is at most a representation-level kernel of a
partially specified process. The claimed ontic object remains missing.

## 6. Counterexamples and unrun controls

### C1 — type-label erasure

Delete every actor and relation name while retaining the five relative
operators and the same shared four-coordinate packet. Every completeness
system, intersection, selected kernel, channel, flag, and safety statistic is
unchanged. What disappears is the claim that the coordinates describe one
recurring relational event. This exact eliminability defeats the history-
individuation gate's physical interpretation.

### C2 — independent-context laws

Assign each token-disjoint context its own PSD kernel. All local completeness
and safety gates still pass, but the five-dimensional product family remains.
No transport-layer principle forbids this. Equality of the kernels is an
additional universality postulate, not a consequence of local completeness.

### C3 — held-out redundancy

Stacking the held-rich system with rich-three changes rank by zero. It cannot
validate the recurrence ansatz out of sample. A genuine held-out test must add
a nonredundant equation or a calibrated screen not already fixed by the rich
training context.

### C4 — derived doctrine probe

Replace the hard-coded polynomial vectors by an exact outcome probability
computed from one common preparation and calibrated port under both recurrence
dictionaries. Until this is done, doctrine sensitivity is an unrun control.

### C5 — steering/no-signalling gate

HJW shows that ensemble decompositions can be remotely selected in standard
entangled systems. CSF has no remote setting, conditional record protocol, or
changing Bob algebra. If a later ISP law makes Bob's future records depend on
which calibrated `C` realizes one unconditioned state, then remote steering
could load the Gisin signalling condition. The present CPTP marginal theorem
does not prevent that; a separate steering-unphrasability or no-signalling
proof remains mandatory.

## 7. Consequence and scope reclassification

| subject | status after review |
|---|---|
| fixed-history spectrahedron | **constructed**, mathematical fixed-map scope |
| rich-spectrum cross moment | **forced zero** at declared unconditioned grain |
| recurring physical law | **blocked** at history individuation/universality |
| exchange-selected `M=I/2` | **conditional** on imposed recurrence and symmetry |
| calibrated instrument | **unselected**; `1` and `9/25` both survive |
| record cell/locality | flag is a Hilbert ancilla; no relational creation map |
| record permanence | **open**; exact reconvergence erases orthogonality |
| actualization | separate postulate, untouched |
| fixed-Bob no-signalling | **proved** only unconditionally on a fixed factor |
| EPR steering | **open**; no remote preparation or operation is typed |
| changing Bob/carrier | **untyped** |
| primitive arity/two-to-`n` | **no result**; three-actor labels imply nothing |
| fields/Fock/species/statistics | **refused** |
| Hamiltonian | **refused**; no repeated selected transport law |
| Lorentz/continuum/gravity | **refused**; no relational rewrite or backreaction |
| affine/cosmological constant | **refused** |
| QFT/GR deviation | **refused** |
| empirical novelty | none; surviving objects are standard finite quantum instruments |

The only calibrated movement, `1` versus `9/25`, demonstrates that the
instrument fiber remains physically nontrivial *if* its external port
calibration is implemented. Because CSF selects no `C`, it predicts neither
number. It organizes candidate-law space rather than reaching phenomenology.

## 8. Grade and surviving finding list

**Grade: REJECT** for the frozen primary. The mathematical core is valuable,
but the protocol's first outcome applies before recurrence selection can be
credited.

Proposed adjudicated list:

1. **`CSF-BLOCKED-AT-HISTORY-INDIVIDUATION`**
2. **`COMPLETENESS-SPECTRAHEDRON-CONSTRUCTED`**
3. **`JCV-UNCONDITIONED-BASE-AND-CALIBRATED-FIBER-EMBEDDED`**
4. **`RICH-SPECTRUM-UNCONDITIONED-CROSS-MOMENT-ZERO`**
5. **`CALIBRATED-INSTRUMENT-FIBER-OPERATIONALLY-NONTRIVIAL-BUT-UNSELECTED`**
6. **`EXCHANGE-FIXES-HALF-KERNEL-CONDITIONAL-ON-DECLARED-RECURRENCE`**
7. **`EXTREME-POINT-SELECTION-UNSTABLE`**
8. **`FLAG-ORTHOGONALITY-CONSTRUCTED-BUT-PERMANENCE-UNPROVED`**
9. **`CONDITIONAL-STEERING-OPEN`**
10. **`ELEMENTARY-TRANSPORTS-REWRITE-AND-CATALOGUE-UNSELECTED`**

Kill `RECURRENCE-DOCTRINE-MOVES-PHYSICS` at the delivered gate. Preserve only
“the declared doctrine labels differ” until an operator-derived probe exists.

## 9. Numbered repairs and kill conditions

1. Replace the primary by `CSF-BLOCKED-AT-HISTORY-INDIVIDUATION`, or construct
   one support/rewrite/transport object that derives each history coordinate
   from the relational event data.
2. State explicitly that full-kernel recurrence across token-disjoint contexts
   is a universality postulate. Do not call it derived vertex locality.
3. Reword selection as: “given the recurrence postulate, rich-spectrum
   completeness leaves diagonal bias; imposed exchange symmetry fixes it to
   one half.”
4. Remove “held-out validation” force. The registered held-out system adds
   rank zero; replace it with a nonredundant context or calibrated observable.
5. Delete the hard-coded doctrine-polynomial gate and derive both competing
   predictions from states, maps, kernels, and retained ports. Until then kill
   `RECURRENCE-DOCTRINE-MOVES-PHYSICS`.
6. Retype `M` as an unconditioned kernel representation conditional on fixed
   history coordinates, not the full physical or ontic law.
7. Retain `C`-fiber movement only conditional on an implemented calibrated
   apparatus; distinguish ancilla factor, local relational cell, durable
   record, and actualization.
8. Promote the general fixed-factor CPTP no-signalling proof, while preserving
   the explicit wall around conditional steering and changing subsystem
   algebras.
9. Require a steering-unphrasability or no-signalling theorem before combining
   decomposition-sensitive future dynamics with an entangled remote protocol.
10. Kill every arity, field, particle, Hamiltonian, gravity, Lorentz,
    continuum, affine-constant, or QFT/GR-deviation promotion until its own
    typed object and invariant calibrated discriminator exist.

## 10. Report SHA-256

Normalized report SHA-256:
`2033a01d7f6d1f3c292644e332c0bb34411db79a186265672904515b3df5918b`.

The normalized digest is SHA-256 of this UTF-8 file after replacing only the
64 hexadecimal characters on the preceding line by 64 ASCII zeroes. This
convention makes the in-file self-digest non-circular.
