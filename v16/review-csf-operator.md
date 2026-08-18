# Independent hostile review of CSF — operator algebra and convex law geometry

Date: 2026-08-18  
Seat: O — operator algebra and convex law geometry  
Target: v16 Paper 6, `Completeness spectrahedra and calibrated record fibers`  
Verdict: **ACCEPT-WITH-FIXES**

## 1. Immutable-target and hash audit

I audited candidate commit
`61c32d884d688f49f29d3863fe5959d1053d382e` and verification commit
`9f98e5aa5817c3001f8fe396f909d43c974a77b5`.  Before substantive work I read
the full runbook, frozen CSF pin and hostile protocol, both freeze notes, the
first-refusal/one-token-repair chronology, generic core, data-only fixture,
repaired scorer, transcript, complete receipt, generated Paper 6, verification
note, and the frozen antecedents.  I did not read or consult another CSF
review.

The immutable bindings reproduce exactly:

| object | frozen and observed SHA-256 |
|---|---|
| pin | `c953618c66685b20705bef7436ebfa29d4b0370b076493bc1997aea898e1bcba` |
| generic core | `93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4` |
| physical fixture | `8c10210b6fee0a5477f3f70593cca080c26a4c91d678ad60bf691f6d853fbd37` |
| repaired scorer | `d3adf994e1c89fca5b53a0969cf0eed256488790b361477116b7cd1a76da84ba` |
| refusal/repair freeze | `b2a140a123cab91fe1aba19a87aa2ee9d9c09c97992260338123b3bd7be1ddf1` |
| transcript | `59077d8ad0f9e9ba4cf5afc0a44fea242d7a6032f1d998e088b3433cf4541785` |
| receipt | `7ae9b4a17fd38883bbff39b212f0edf819e2edf17942c9d54f8cf9f772414fdc` |
| Paper 6 | `543a2c927ecc7bd184fc758e4d72ebd4d4974327ae5ae2bb279d1fe33086c5d9` |
| candidate verification | `c0b3e7072ae2ba5a5fe45e1a26c988d36fe989b33cb02e71e57490db077b7cd5` |

The generic core predates the physical fixture.  The fixture/scorer freeze
predates every result artifact.  The first official invocation refused
without artifacts because its anchor requested `erasable` where the immutable
paper contains `eraser`; the frozen repair changes only that token.  The
operator equations, contexts, dictionaries, gates, classifier, claims, and
renderer are unchanged.

A true no-`.git` archive replay in `/private/tmp/csf_operator_replay`, launched
from `/private/tmp`, regenerates transcript, receipt, and paper byte-identically
at the hashes above.  All eight payload seals, 30 gate rows, 12 one-occurrence
claims, outer hashes, and read-path hashes reconcile.  I invoked all 36 frozen
mutants independently.  Each exited `1` at its bound gate or promotion check,
emitted no traceback, and wrote zero artifact files.  The core/scorer ASTs and
fixture contain no float.

These checks authenticate the delivery.  They do not validate the physical
meaning of the recurrence dictionary or the held-out claim.

## 2. Independent method and tools

I reconstructed the fixed-history algebra without importing either candidate
implementation.  My independent exact program is
`/private/tmp/csf_operator_independent.py`; it uses only `Fraction`, an
independent Gaussian-rational type, direct Gram products, and rational row
reduction.  It rebuilds all JCV kernels and port probabilities, the five
context systems, the stacked and exchange-fixed dimensions, the held-out row
rank, the selected record factorizations, and the nonnormal control.

I also derived the CP/channel identities, PSD geometry, coefficient lifting,
port gauge, and extremality criterion analytically.  Countercontrols below are
not imported from the scorer.

## 3. Exact recomputation table

| object | candidate | reviewer | status |
|---|---:|---:|---|
| JCV first kernel | `diag(16/25,9/25)` | same | PASS |
| JCV second kernel | same as first | same | PASS |
| JCV first retained probability | `0` | `0` | PASS |
| JCV second retained probability | `49/625` | `49/625` | PASS |
| JCV third kernel | `diag(25/169,144/169)` | same | PASS |
| third unconditioned channel | moves | off-diagonal multiplier `-119/169` versus `7/25` | PASS |
| five affine-hull dimensions | `2,2,1,1,2` | `2,2,1,1,2` | PASS |
| independent training dimension | `5` | product dimension `2+2+1=5` | PASS |
| identity-recurring dimension | `1` | `1` | PASS |
| exchange-fixed dimension | `0` | `0` | PASS |
| exchange-fixed kernel | `I/2` | `I/2` | PASS |
| held-out rank increment | not printed | **zero** | NEW LOAD-BEARING CHECK |
| selected-kernel port probabilities | `1,9/25` | `1,9/25` | PASS |
| nonnormal relative map | `[[0,3/5],[0,4/5]]` | same | PASS |
| nonnormal affine dimension | `1` | `1` by full operator equation | PASS |
| rich cross moment | forced zero | `m=0`, trace one, bias free | PASS |
| flag overlaps | `1,3/5,0` | same | PASS |
| reconverged overlap | `1` | `1` | PASS |
| endpoint/selected/restricted tangents | `0/0/1` | `0/0/1` | PASS |
| selected rank | `2` | `2` | PASS |
| fixed-Bob marginal | `I/2 -> I/2` | same | PASS |
| amplifier marginal | `2I` | same | PASS |
| distinct complete kernels, same channel | untested | explicit exact counterexample exists | NEW CONTROL |

For the context rows, write

$$
M=\begin{pmatrix}p&r+is\\r-is&q\end{pmatrix}.
$$

The `phase-sign` system is `p+q=1,r=0`; the `quarter-sign` system is
`p+q=1,s=0`; and every rich three-phase row is
`p+q=1,r=s=0`.  Their feasible PSD parts have the same relative dimensions as
their affine hulls: two filled ellipses/disks, then line segments.  The
reported numbers are therefore correct here, although affine dimension and
PSD-face dimension are not synonymous in general.

## 4. Theorem and proof audit

### 4.1 Factorization through the history kernel

For `K_j=sum_h c[j,h]V_h` and

$$
M_{hk}=\sum_j\overline{c_{jh}}c_{jk},
$$

direct expansion gives

$$
\sum_jK_j^\dagger K_j
=\sum_{h,k}M_{hk}V_h^\dagger V_k=L_V(M),
$$

and, with the candidate's index orientation,

$$
\Phi_M(\rho)
=\sum_{h,k}M_{hk}V_k\rho V_h^\dagger.
$$

The orientation is correct.  If `M` is PSD over `C`, a factorization
`M=C^dagger C` exists, with at least `rank(M)` and at most the history count
of unobserved ports in a minimal complex factorization.  Hence `Phi_M` is
completely positive.  `L_V(M)=I` makes it trace preserving for every input;
linearity gives affinity, and complete positivity/trace preservation survive
tensoring with an arbitrary ancilla.

Thus, at fixed finite histories over unrestricted complex coefficients,

$$
\mathcal S_V=\{M\succeq0:L_V(M)=I\}
$$

is exactly an affine slice of the PSD cone: a spectrahedron.

Two qualifications are required.

First, fixed exact field and port resources matter.  A complex square root may
leave `Q(i)`, and a factorization may need more ports than the declared
catalogue.  The scalar positive kernel `[7/5]`, for example, has no one-port
`Q(i)` factor because `7/5` is not a sum of two rational squares, although

$$
\frac75=|1+3i/5|^2+|1/5|^2
$$

gives a two-port realization.  Therefore the full spectrahedron is the
complex mathematical design space; the exact grammar-realizable subset also
depends on allowed flag dimension/port refinement unless arbitrary complex
coefficients are licensed.

Second, `M -> Phi_M` need not be injective.  With two coincident histories
`V_1=V_2=I`, both

$$
M_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
M_2=\frac12I
$$

are PSD and complete and induce the identity channel, yet `M_1 != M_2`.
Consequently `M` is an unconditioned-law coordinate above a possible further
history-to-channel null quotient.  In the registered recurring rich segment,
the surviving diagonal bias does move `Phi_M`, so this counterexample does not
erase the measured `1 -> 0` reduction; it limits the generic ontology.

### 4.2 JCV base and calibrated fiber

The three coefficient matrices give, exactly,

$$
M_1=M_2=\operatorname{diag}(16/25,9/25),\qquad
M_3=\operatorname{diag}(25/169,144/169).
$$

For input `|0>` and histories `(I,Z)`, the retained first-port probability is
the squared modulus of the row sum.  This gives `0` for the first factorization
and `49/625` for the second.  On `|+>`, a diagonal kernel
`diag(p,q)` multiplies off-diagonal coherence by `p-q`, giving `7/25` for the
first kernel and `-119/169` for the third.  The third difference is therefore
not in the history-to-channel null space.

For the selected `M=I/2`, parity coefficients and their declared `3-4-5` port
rotation both factor the same kernel.  Their retained port-zero probabilities
are exactly `1` and `9/25`, while the unconditioned channel is the same.

If the full two-outcome instrument and fixed labels are calibrated, the
residual port gauge of the minimal independent Kraus pair is independent
phase on each Kraus operator, `U(1)^2`; a simultaneous calibrated outcome
permutation is an automorphism only if the apparatus labels are transported.
The fixture actually calibrates one outcome on one preparation, which is
enough to separate the two displayed factorizations but not enough to classify
the entire fiber quotient.  The qualifier should therefore say “these two
factorizations are operationally separated by the registered calibration,”
not that every distinct factorization is physical.

### 4.3 Unrestricted context systems and rich spectrum

For two unitary histories with relative eigenphases `lambda`, completeness is

$$
(p+q)I+m\Omega+\bar m\Omega^\dagger=I.
$$

The five systems were solved over unrestricted Hermitian `M`, not a rational
sample.  Their dimensions are exactly `2,2,1,1,2`.  Three distinct phases
force `p+q=1,m=0`, while PSD leaves `0<=p<=1`.  Thus rich spectrum kills the
unconditioned cross moment but does not select the diagonal bias or any
factorization, outcome, causal order, or durable record.

The nonnormal control is handled correctly.  For

$$
\Omega=\begin{pmatrix}0&3/5\\0&4/5\end{pmatrix},
$$

the off-diagonal equation forces `m=0` and the diagonal fixes `p+q=1`, leaving
one affine/PSD segment.  No normal or eigenphase language is needed.

### 4.4 Extremality

The tangent-support criterion used by the core is correct.  The rich endpoint
`diag(1,0)` has no supported homogeneous tangent and is extreme.  `I/2` has
rank two and is extreme in the exchange-fixed feasible **singleton**; after
the exchange equation is removed, the rich feasible set is a segment and its
tangent nullity is one.  This proves extremality is relative to the constraint
set and that rank two can be extreme.

It is a deliberately modest negative result.  “Restriction sends an extreme
to an interior point” here means deleting a law constraint, not applying a
quantum channel to the kernel.  Spectator and catalogue controls verify
completeness after extension but do not independently compute extremality of
the extended feasible sets.

## 5. Recurrence and gauge audit

### 5.1 What the intersection really selects

The exact reduction is:

```text
independent context laws:  dimension 2 + 2 + 1 = 5
same raw M in all training contexts:          dimension 1
plus swap invariance M = S M S:               dimension 0
```

The first reduction is conditional on the identity recurrence dictionary--a
universality postulate identifying the full kernel coordinates across three
otherwise separate contexts.  The second reduction is wholly caused by the
extra invariance equation.  On the recurring line
`M=diag(p,1-p)`, swap invariance is exactly `p=1/2`.

This distinction matters.  Quotienting by the exchange as gauge would only
identify `p` with `1-p`; it would leave a continuum of physical orbits.
Demanding `SMS=M` is stronger: it postulates an exchange-symmetric **law** and
selects its fixed point.  The paper's prose calls the result conditional, but
the frozen primary `CSF-RECURRING-LAW-SELECTED-MODULO-GAUGE` does not contain
that condition.  The unconditional algebraic result is partial selection to a
one-dimensional segment; the singleton is conditional on imposed exchange
invariance.

The coordinate-rephase control is correct and channel-covariant.  If history
coordinates transform by a diagonal `D`, then

$$
V_h\mapsto d_hV_h,\qquad M\mapsto DMD^\dagger
$$

leaves `L_V` and `Phi_M` invariant.  Raw off-diagonal entries are not
gauge-invariant.  The selected `I/2` is trivially invariant under every
history unitary, so its held-exchange covariance does not by itself validate
the recurrence dictionary.

### 5.2 The held-out context is algebraically redundant

The held-out relative spectrum is `{1,-i,-1}`.  Like the training rich row
`{1,i,-1}`, it imposes exactly

$$
p+q=1,\quad r=0,\quad s=0.
$$

My exact row-space check finds

```text
rank(training + heldout) - rank(training) = 0.
```

Indeed the first two training contexts already impose the same combined
system, so even the training `rich-three` context is redundant after them.
The held-out kernel “passes,” but it supplies no new equation and no
non-vacuous prediction.  It cannot serve as independent confirmation of the
recurrence ansatz or selected point.

### 5.3 The doctrine-movement qualifier is not computed

The gate for `RECURRENCE-DOCTRINE-MOVES-PHYSICS` assigns literal arrays

```text
identity -> [1,0]
asymmetric_exchange -> [0,1]
```

and declares movement because the arrays differ.  Neither polynomial is
derived from a kernel, channel, port, state, or calibrated probe.  The
asymmetric “exchange forbidden” control is likewise the comparison of a
metadata string with `symmetric`; its selected kernel would be complete for
every phase-sign bias.  This is auditable declaration, not an operator
discriminator.

That qualifier must be withdrawn unless a future repair derives both
predictions from typed probes.  The exact identity-recurrence intersection is
unaffected, but the candidate has not measured physical movement across
inequivalent recurrence doctrines.

## 6. Counterexamples and unrun controls

1. **History-to-channel null kernel.** The coincident-history example above
   gives distinct complete PSD kernels with the same unconditioned channel.
   A physical base generally requires quotienting the kernel of
   `M -> Phi_M`, unless future record algebra resolves it.
2. **Exact-field/port-resource control.** `[7/5]` is PSD but lacks a one-port
   `Q(i)` factor; an enlarged two-port factor exists.  Complex feasibility,
   exact grammar feasibility, and minimal flag dimension are different.
3. **Held-out redundancy.** Adding the held context increases constraint rank
   by zero.  Replace it with a context not in the training row span before
   using “held-out” as predictive evidence.
4. **Gauge versus invariance.** Quotienting `p~1-p` leaves a continuum; imposing
   `p=1/2` selects a singleton.  These operations must not share the phrase
   “modulo gauge.”
5. **Port-calibration stabilizer.** Full fixed-label instrument calibration
   leaves Kraus phases, whereas the one-probability calibration leaves a
   larger unmeasured stabilizer.  The candidate separates two points but does
   not classify the fiber.
6. **Doctrine probe absent.** Replace the literal `[1,0]`/`[0,1]` arrays by
   probabilities derived from two frozen recurrence maps and a common
   calibrated state/effect.  Until then the doctrine qualifier has no
   operator content.

## 7. Consequence and scope reclassification

| statement | reviewer classification |
|---|---|
| `M=C^dagger C`, `L_V`, `Phi_M` | theorem at fixed typed histories |
| completeness spectrahedron | theorem over complex PSD kernels; exact grammar resources may restrict realizations |
| JCV base/fiber | exact finite reconstruction |
| rich-spectrum cross moment | theorem for two unitary histories with at least three phases; bias free |
| recurrence `5 -> 1` | conditional exact fact under declared identity recurrence |
| exchange `1 -> 0` | conditional exact fact from imposed law invariance, not gauge quotient |
| held-out pass | algebraically redundant, not predictive validation |
| doctrine moves physics | **not established**; stored arrays are declaration-only |
| calibrated fiber nontrivial | two exact factorizations separated by one registered port witness |
| extreme instability | exact under deletion of exchange constraint; not a general physical-map theorem |
| flag orthogonality | present distinguishability only; reconvergence refutes permanence |
| fixed-Bob no-signalling | general consequence of fixed-factor CPTP, fixture confirms |
| conditional steering/changing Bob | open |
| elementary transports, rewrite, catalogue, actualization | unselected/unconstructed |
| arbitrary `n`, fields, particles, Hamiltonian, gravity, QFT/GR deviations | unconstructed |

Proposed frozen-finding disposition:

1. **Demote/narrow** `CSF-RECURRING-LAW-SELECTED-MODULO-GAUGE` to the compound
   result: identity recurrence partially selects a one-dimensional physical
   family; separately imposed exchange-law invariance conditionally fixes
   `I/2`.  Do not call invariance a gauge quotient.
2. **Preserve** `COMPLETENESS-SPECTRAHEDRON-CONSTRUCTED` at fixed-history,
   complex-PSD scope, with port/field resource caveat.
3. **Preserve** `JCV-UNCONDITIONED-BASE-AND-CALIBRATED-FIBER-EMBEDDED`.
4. **Preserve** `RICH-SPECTRUM-UNCONDITIONED-CROSS-MOMENT-ZERO`.
5. **Preserve with calibration scope**
   `CALIBRATED-RECORD-FIBER-OPERATIONALLY-NONTRIVIAL` for the two displayed
   factorizations.
6. **Preserve and attach to the primary sentence**
   `SELECTION-CONDITIONAL-ON-EXCHANGE-SYMMETRY`.
7. **Kill** `RECURRENCE-DOCTRINE-MOVES-PHYSICS` in this candidate; its alleged
   observables are literals, not derived measurements.
8. **Preserve narrowly** `EXTREME-POINT-SELECTION-UNSTABLE` under registered
   constraint restriction.
9. **Preserve** `FLAG-ORTHOGONALITY-CONSTRUCTED-BUT-PERMANENCE-UNPROVED`.
10. **Preserve** `CONDITIONAL-STEERING-OPEN`.
11. **Preserve** `ELEMENTARY-TRANSPORTS-AND-CATALOGUE-UNSELECTED`.

## 8. Grade

**ACCEPT-WITH-FIXES.**

The operator core is strong: the spectrahedral factorization, index
orientation, unrestricted context ranks, JCV embedding, rich-spectrum theorem,
nonnormal control, calibrated-factorization witness, flag/eraser separation,
and tangent calculations are exact.  The paper also refuses the dangerous
steering, permanence, gravity, QFT, and fundamental-dynamics promotions.

The principal defect is interpretive but load-bearing.  Recurrence alone does
not select a point; exchange invariance explicitly does.  The held-out row is
algebraically redundant, and the doctrine-movement qualifier is unsupported
by computation.  These require a primary-sentence correction and one finding
kill, but not rejection of the spectrahedral advance.

## 9. Numbered repairs and kill conditions

1. Replace the primary everywhere by a compound, conditional sentence:
   “identity recurrence reduces the product family from dimension five to a
   one-dimensional PSD segment; imposing the licensed exchange **law
   invariance** fixes `M=I/2`.”
2. Never equate exchange quotient with exchange invariance.  If exchange is
   only gauge, the family remains continuous modulo `p~1-p`.
3. Label the held-out row algebraically redundant and remove any predictive or
   validation rhetoric.  A successor held-out test must add an independent
   operator equation or calibrated channel statistic.
4. Delete `RECURRENCE-DOCTRINE-MOVES-PHYSICS` and the literal-polynomial gate,
   or replace it only after both doctrine predictions are derived from a
   frozen common probe.
5. State that `M` can have a further channel-null quotient.  For the registered
   recurring line, explicitly retain the exact proof that bias moves the rich
   channel.
6. State factorization existence over `C`; distinguish minimal fixed-port
   `Q(i)` implementation from enlarged-port realization.
7. Restrict the record-fiber claim to the two factorizations separated by the
   retained-port witness; do not claim a complete fiber-moduli classification.
8. Describe extremality instability as constraint-restriction instability,
   not as a theorem under every physical channel, spectator, or catalogue map.
9. Preserve all current walls: orthogonality is not permanence, selected `M`
   is not selected `C`, fixed-factor no-signalling is not steering, and no
   joint rewrite/transport/catalogue law is obtained.

Any counterexample to the factorization/channel equations, unrestricted
context ranks, or rich-spectrum theorem would kill the mathematical core; I
found none.  The exact counterchecks instead kill only the stronger selection
and doctrine rhetoric above.

## 10. Report SHA-256

The canonical SHA-256 of this report, computed after replacing the 64
hexadecimal characters on the next line by 64 ASCII zeroes, is:

`e3fde6cfe5dd98a0b70264126326dc21c9c68afe55134d3edc999a3e7a5cda57`
