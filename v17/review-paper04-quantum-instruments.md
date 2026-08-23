# Paper 04 hostile review — Seat Q

## Quantum instruments, histories, and operational comparison

Date: 2026-08-23

Status: **FROZEN MUTUALLY BLIND SCIENTIFIC REVIEW**

Verdict:

```text
REVISE
```

First decisive semantic counterexample:

```text
The claimed A-frame analogue of the parent-to-laboratory orbit identity is
false for UCOH at alpha=1.  The A reduction coherently combines the q=0
orbit component at s=1 and the q=1 orbit component at s=4.  No single member
rho_lab(s) of the frozen, classically s-indexed comparator has that support or
coherence.
```

Earliest affected mandatory theorem: **H14**.

Earliest affected model target: **M6/M13**, followed independently by the
complete-packet defects at **M5/M10/M21**.

Earliest controlling registered rung:

```text
P04-PHYSICAL-CLOCK-UNCONSTRUCTED
```

Exact coordinate salvage below that controlling rung:

```text
FINITE-PARENT/PHYSICAL-SOURCES/B-REDUCTION/A-GOOD-SECTOR-REDUCTION/
B-FRAME-COMPARATOR-BRIDGE/STATE-LEVEL-A-B-FRAME-MAP
```

The candidate's stronger external-parameter-redundancy product is not earned
as printed.  The finite parent, exact reductions, B-frame comparator bridge,
calibration values, response values, and reduced-frame USEQ arithmetic remain
valuable salvage.  The verdict is `REVISE`, not `REJECT`, because the frozen
parent is consistent and the counterexample narrows an overclaimed bridge;
it does not destroy the finite representation itself.

No candidate edit, repair, implementation, or successor is authorized by
this report.

## 0. Authentication, corpus, and blindness

I first authenticated exact HEAD
`8faa5b83d1a3a7cb0a33ae9e5b470c8c075785a4` and the complete protocol at
ordinary SHA-256
`d763bb685003312e4529b62e29cceebd7eb0182d2a4ca3fbb3f6c118176715e9`.
I then read every protocol-bound artifact completely before freezing the
judgment.

| Bound artifact | Observed ordinary SHA-256 | LF / bytes |
|---|---|---:|
| `v17/paper-04-finite-relational-clock-parent.md` | `25d6771bd4bbfb658a54da7f65cdcc9620b0769f6d7be6075103ff5d44230dc6` | 1,197 / 45,211 |
| `v17/note-paper04-construction-audit.md` | `d596f2a6c0ed7240d655780b61927eef71b908b14b1bc905f6418cef76bbc484` | 283 / 12,759 |
| `v17/note-paper04-two-clock-parent-construction-pin.md` | `8adb5def4c927dd55eba4c2360782b1b6d9370fcf3f5d5c76f5458b1a0fbca4e` | 758 / 34,071 |
| `v17/note-paper04-model-pin-audit-mathematics.md` | `a2fd150f75557c992a746e78b1e9b3b209bc7d0adca0ca8cee5bcb192d7a9ce9` | 881 / 41,768 |
| `v17/note-paper04-model-pin-audit-quantum-clocks.md` | `69c7deae38b115fd60d31006e5b5f79f5167e8e655bf9f3a0c7867ebbd809c1d` | 821 / 40,765 |
| `v17/note-paper04-model-pin-audit-ontology-relativity.md` | `ebd1fa98640accbe036d8097802f27e050875a09771f0d646ed7027e302bf0d6` | 866 / 52,036 |
| `v17/note-paper04-model-pin-audit-adjudication.md` | `f0d2ae0142192683192a5e033c572d0c5906feb546d14268f7525f1b9a0a42cc` | 500 / 20,123 |
| `v17/note-paper04-relational-clock-external-time-pin.md` | `da48bc95bf02c93393697ad6b447605ab89879ff45a1be6896abf6ce6a276b0c` | 1,016 / 45,152 |
| `v17/paper-03v32-complete-boundary-relativistic-adequacy.md` | `469ae61c849573c9fe7c70871ca6b60843a080082d07f6850b48213b86d6f7d6` | 1,320 / 56,462 |
| `v17/note-paper03v32-hostile-review-adjudication.md` | `b42fcf6201e249f03772ae2f1e037c2c945e98e4221c89a629d744de937e6104` | 502 / 21,215 |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | 476 / 21,268 |

The candidate and protocol use LF endings, end in one LF, and have no
trailing horizontal whitespace.  The unrelated untracked v16 handoff note
was not opened or used.  I did not inspect, infer, contact, or discuss either
hostile sibling report or its path.  This report is my sole writable path.  I
did not run the private verifier, use implementation output as evidence,
stage a file, commit a file, or edit any bound artifact or register.

## 1. Decisive reconstruction

### 1.1 The exact UCOH parent state

The normalized UCOH physical vector is

$$
|\Psi_{\rm UCOH}\rangle
=\frac1{\sqrt{14}}\sum_{s\in\mathbb Z_7}
\left(
 |s,2s,s\rangle_{ABM}|0\rangle_Q^k
 +|2s,2s,s\rangle_{ABM}|1\rangle_Q^k
\right).
$$

The two components share B reading $2s$, so B conditioning selects one
common $s$ and preserves their Q coherence.  This proves the candidate's
global B-frame comparator identity, including UCOH.

At A reading $\alpha=1$, however, the two sectors solve different equations:

$$
s=1\quad(q=0),
\qquad
2s=1\Longrightarrow s=4\quad(q=1).
$$

Therefore

$$
\mathcal R_A(1)|\Psi_{\rm UCOH}\rangle
=\frac{|B=2,M=1,q=0\rangle
       +|B=1,M=4,q=1\rangle}{\sqrt2}
=:|+\rangle.
$$

This is the candidate's own state in Theorem 9.1.

### 1.2 No frozen laboratory comparator member equals it

The frozen laboratory comparator is not a coherent quantum control over
$s$; it is the classical family

$$
\rho^{\rm lab}_{\rm UCOH}(s)
=U_s|\phi_{\rm UCOH}\rangle\langle\phi_{\rm UCOH}|U_s^\dagger.
$$

At a fixed $s$, its two terms have the same B and M labels $(2s,s)$ and A
labels $s$ and $2s$.  Removing A gives, for $s\ne0$, a mixture because those
A phase kets are orthogonal.  At $s=0$ it gives a coherent Q superposition
supported at $(B,M)=(0,0)$.  Neither case is $|+\rangle\langle+|$, whose
support is split between $(B,M)=(2,1)$ and $(1,4)$.

Equivalently, conditioning any one laboratory member on $A=1$ selects only
the q=0 component when $s=1$, only the q=1 component when $s=4$, and no
component otherwise.  It never selects their coherent sum.

Thus candidate lines 403--409 cannot be an identity analogous to the B
identity on UCOH.  A coherent superposition of different external-$s$
comparator members would be a new object, not one member of the frozen
classically indexed comparator.  The correct scope is:

```text
B-to-lab orbit identity: all nine frozen sources;
A-to-lab single-orbit identity: fixed-q good components only;
UCOH A reduction: a valid parent-relative quantum frame, but not one
  classically s-indexed laboratory orbit member.
```

This is exactly the multiple-choice/coherence phenomenon the candidate
correctly detects later.  It may not simultaneously be called an analogous
single-orbit laboratory identity.

### 1.3 Independent complete-arrow defect

Even after narrowing the UCOH bridge, the printed complete-instrument product
is not yet established at the accepted Paper-03 quantifier.

The candidate gives useful ingredients:

$$
W_B,\quad V^B_\beta,\quad W_A,\quad V^A_\alpha,
$$

and proves normalization/covariance of the finite branch families.  It does
not print the complete certified Paper-03 pair

$$
(g,D,E,K,\Phi)
$$

with source/target packet, exact sample kernel, direct-sum normal UCP map,
old-record append, complete target memory, and all-reader identity.  The
$q=6$ A output is described as a STOP flag while its still-readable phase
PVM is mentioned, but the joint phase-plus-STOP branch arrow and posterior
are not defined.

The same problem is decisive in USEQ.  The displayed reduced-frame values are
correct, but no single arrow of the binding form

```text
reduction -> first complete M instrument -> r1 append -> invariant guard
-> full A/M/Q transport -> second complete M instrument -> lift/target
```

is written.  In particular, the candidate does not define

$$
W^B_{b+4\leftarrow b}
=\mathcal R_B(b+4)\mathcal R_B(b)^{-1},
$$

its action on every retained record and non-M degree of freedom, the lift to
the perspective-neutral boundary, or the resulting Heisenberg reader map.
The assertion that “conjugation and direct-sum functoriality” transports every
instrument and history is not the all-reader theorem required by B5/B8/B10.

This is not a Python complaint.  Distinct dilations can share the printed
M-outcome table while leaving different future-readable apparatus states.
Paper 03 accepts them as one arrow only after target-memory and all-reader
equivalence are proved.  That proof is absent.

The four record/division examples have the same defect.  They are prose
schemas with no frozen source/target packets, licensed continuation families,
kernels, UCP maps, or explicit separating readers.  In case 2 a memory is
said to be omitted while still controlling a future translation; that is a
counterexample to boundary completeness, not by itself an instantiated
Paper-03 process object.  H23/M21 therefore remain unconstructed.

## 2. Exact finite reconstruction

### 2.1 Constraint and reductions

For

$$
D(a,b,m,q)=a+2b+m+q+aq\pmod7,
$$

$U_gU_h=U_{g+h}$ and $U_g^\dagger=U_{-g}$.  Character orthogonality makes
$P=7^{-1}\sum_gU_g$ a self-adjoint idempotent.  Since $2^{-1}=4$,

$$
b=-4(a+m+q+aq)
$$

is unique, so the physical dimension is $7^3=343$.

Every frozen seed has sharp B phase.  Its seven orbit components have
distinct B labels, hence every denominator is $1/7$ and no source is removed.

On the physical charge basis,

$$
\mathcal R_B(\beta)|a,m,q\rangle_{\rm phys}
=\omega^{-b(a,m,q)\beta}|a,m,q\rangle,
$$

so B reduction is globally unitary.  For $q\ne6$, fixed $(b,m,q)$ fixes
$a=-(1+q)^{-1}(2b+m+q)$ and A reduction is unitary.  At $q=6$ its 49
dimensional domain maps with rank 7.  These claims pass exactly.

### 2.2 Covariant records

The B record action has the correct sign.  Since

$$
U_gE_B(\beta)=E_B(\beta+2g)U_g,
$$

the same-sign record shift gives

$$
(U_g\otimes T_g^{R_B})W_B=W_BU_g.
$$

The branch effects are $(V^B_\beta)^\dagger V^B_\beta=I/7$, so their sum is
$I$.  For A, the controlled action

$$
C_g=\sum_q|q\rangle\langle q|\otimes T_{(1+q)g}
$$

obeys $C_gC_h=C_{g+h}$ and preserves coherent q sectors.  Replacing it by a
fixed shift or measuring q would change UCOH.  These state/isometry-level
claims pass.  The failure is their promotion to a fully tagged complete
Paper-03 packet without constructing the packet.

### 2.3 USEQ values

In the canonical B chart, the first M state is

$$
(|1\rangle+|2\rangle)/\sqrt2.
$$

The retained measurement yields $r_1=1,2$ with probability $1/2$.  The
original guard and two-step reduced transport give

$$
(r_1,r_2)=(1,3),(2,5),
$$

and the opposite guard gives $(1,4),(2,4)$, each with weights $1/2$.

For arbitrary B coordinate $b$,

$$
h=4(b-2),\qquad \widetilde r_1=r_1-h
$$

is invariant because $b\mapsto b+2g$, $r_1\mapsto r_1+g$, and
$h\mapsto h+g$.  The second-record difference is the invariant value four.
This proves covariance of the displayed controller rule and removes branch
postselection at the level of the reduced direct sum.  It does not by itself
construct the complete perspective-neutral sequential arrow.

### 2.4 Calibration, responses, and baselines

U0 gives $(A,B,M)=(s,2s,s)$.  Training at $s=0,1$ uniquely fixes
$B=2A$; held-out $s=2,3$ give $(2,4)$ and $(3,6)$.  These values pass.

At B record 2, U0/U1 give sharp A records 1/2; deleting $aq$ makes both 1.
UA0/UA1 give sharp Q records 1/2; the same deletion makes both 1.  Both TV
distances are one and both deletion distances are zero.  The result is
reciprocal source response only.

The independent-uniform clock leaves the U0 M law uniform conditional on the
record, at TV $6/7$ from the sharp target.  The coefficient-three comparator
mutant is sharply wrong at a held-out reader, so its maximum TV distance is
one.  These values pass.

### 2.5 Resources and domain losses

The dimensions, period seven, record cardinalities, USEQ M-charge law, mean
$5/2$, and printed variance formula reconstruct.  One omission matters:
UA0 and UA1 have Q phase seeds, hence each has q=6 support probability
$1/7$.  The candidate's common-sector round trip is valid only on their
subnormalized good support (or after an explicitly declared conditioning),
not as an unqualified normalized all-source statement.  USTOP has stopped-A
probability one; the other fixed-q sources have zero.  B16 required every
failure probability, but this source-by-source stop ledger is not printed.

## 3. Mandatory theorem reconstruction H1--H30

| ID | Seat-Q disposition | Reconstruction |
|---|---|---|
| H1 | PASS | Character law gives a representation; finite averaging gives an orthogonal projector. |
| H2 | PASS | Unique B charge gives dimension 343. |
| H3 | PASS | B-phase orbit orthogonality gives all nine denominators $1/7$. |
| H4 | PASS | $\mathcal R_B(\beta)$ is a basis permutation with unit phases. |
| H5 | PASS | A is unitary exactly at q-not-6 and has rank 7 from dimension 49 at q=6. |
| H6 | PASS | Bare compression is $P/7$ and the bare branch is not a physical endomorphism. |
| H7 | PASS AT ISOMETRY LEVEL / PACKET PROOF INCOMPLETE | B branch normalization and covariance are exact; the full Paper-03 tagged pair is not printed. |
| H8 | PASS AT GROUP-ACTION LEVEL / PACKET PROOF INCOMPLETE | The coherent Q-controlled action is a representation and has the correct sign. |
| H9 | PASS | $\Delta_A,\Delta_B$ give $(1,0),(0,1),(0,0)$ and survive the quotient on q=0. |
| H10 | FAIL AS PRINTED | No single normalized fully tagged joint law over all source/context packets is constructed; $K_h^c$ is assumed as an unspecified complete context instrument. |
| H11 | PARTIAL | The translated guard predicate is invariant, but the one complete parent-level arrow is absent. |
| H12 | PASS FOR BRANCH COVARIANCE / INCOMPLETE FOR FULL LINEAGE | The canonical slice is a gauge coordinate, not postselection; runtime-free target activation is not certified as a paired arrow. |
| H13 | NUMERICAL PASS / COMPLETE-LAW FAIL | Both history tables are correct; complete posterior and all-reader equality are not constructed. |
| H14 | FAIL | The A-to-lab analogue is false for UCOH; the B bridge and fixed-q A bridge survive. |
| H15 | PASS | Training, held-out points, target zero loss on registered U0/B and USEQ reduced tables, and baselines reconstruct. |
| H16 | PASS AS AN A-FRAME COHERENCE WITNESS / UNIVERSAL KERNEL SCOPE INCOMPLETE | $F_+$ is an admitted finite effect and gives 1 versus 1/2 after actual B-branch dephasing; the candidate does not fully define the universal reading-only kernel comparison. |
| H17 | PASS FOR STATE/OBSERVABLE UNITARY / COMPLETE-HISTORY PROOF INCOMPLETE | $\mathcal S$ round-trips on q-not-6; complete instruments and records are asserted by functoriality. |
| H18 | PASS | Both response arms and deletion values are exact. |
| H19 | PASS | No-clock $6/7$ and mistuned-B maximum 1 are exact. |
| H20 | PASS WITH FINITE SCOPE | Full pushforward preserves finite probabilities; no continuum diffeomorphism follows. |
| H21 | PASS AT PRINTED DEPENDENCY SIGNATURE | $s$ is absent from the parent formula; supplied context/order and calibrated constants remain declared inputs. |
| H22 | REVISE | Main resource numbers pass, but source-specific A-stop probabilities and a complete dilation/target-memory ledger do not print. |
| H23 | FAIL | Four prose sketches are not four typed Paper-03 process objects. |
| H24 | PASS WITH STRUCTURAL SCOPE | The parent froze pre-result but is co-designed with the comparator and not empirically selected. |
| H25 | PASS | The Paper-03 causal order remains supplied. |
| H26 | PASS | No lattice/discrete ontology is promoted. |
| H27 | PASS | Response is not called gravity in the interpretive sections. |
| H28 | PASS | No probability law selects an actual history. |
| H29 | FAIL | Coordinates 2--4, 8, 13--14, 18, and 22 are over-awarded at their complete-packet quantifiers. |
| H30 | FAIL FOR STRONGEST RUNG / PASS FOR WALLS | The maximum rung requires the failed complete bridge and adaptive-packet gates; permanent walls are respected. |

## 4. Binding conditions B1--B20

| ID | Disposition |
|---|---|
| B1 | PASS: group, factors, polynomial, sources, windows, and readers are unchanged. |
| B2 | PASS: representation, projector, dimension, inner product, and all source denominators are proved before use. |
| B3 | PARTIAL: covariant isometries and normalized branches are given, but the exact tagged output pair and q=6 phase-plus-STOP packet are not. |
| B4 | PASS AT STATE LEVEL: UCOH remains coherent and the A record action is Q controlled. |
| B5 | FAIL: no all-reader equivalence theorem selects one complete reduction/lift/dilation route. |
| B6 | PASS: q=6 is retained and no A inverse is used there. |
| B7 | PASS: quotient-level relative readers distinguish A and B. |
| B8 | FAIL: the candidate gives a reduced calculation, not one complete perspective-neutral adaptive arrow. |
| B9 | PASS: chronology and two opportunities are explicitly supplied by Paper 03. |
| B10 | PARTIAL: state-level full quantum transport is exact; instrument/record/history transport is asserted rather than constructed. |
| B11 | PASS for frozen arithmetic; complete-law zero loss is not established beyond the displayed registered readers. |
| B12 | PASS: both baselines use frozen changed objects and informative M readers. |
| B13 | PASS WITH SCOPE: no runtime $s$ appears, but the scheduled context and fixed record difference remain declared physical inputs. |
| B14 | PASS AS FINITE PUSHFORWARD: every listed interface component is said to be pushed; this is not a continuum theorem. |
| B15 | PASS: both operational response values and deletion controls reconstruct. |
| B16 | REVISE: apparatus target maps and source-specific A-stop probabilities are absent. |
| B17 | FAIL: record/division cases are not complete process objects. |
| B18 | PASS: co-design and nonselection ceiling are printed. |
| B19 | PASS: causal order, geometry, and gravity stay supplied/unconstructed. |
| B20 | PASS: implementation is not used as evidence. |

## 5. Paired controls C1--C42

Each row was reconstructed in both directions; a positive arm marked
`PARTIAL` inherits the complete-arrow defect rather than being silently
awarded.

| ID | Positive/neutral arm | Hostile arm |
|---|---|---|
| C1 | PASS: A/B are factors with relative records. | Slot/path scalar has no physical packet; killed. |
| C2 | PASS: relative-origin controls separate A/B. | Rename/copy gives one clock; killed. |
| C3 | PARTIAL: finite branches normalize. | Reading table without posterior is incomplete; killed. |
| C4 | PARTIAL: records are declared retained. | Ephemeral result cannot guard USEQ; killed. |
| C5 | PASS: all used finite events have positive support. | Zero-support normalization refused. |
| C6 | PASS AS REFUSAL: diffuse case unclaimed. | Null-point promotion refused. |
| C7 | FAIL AT FULL PACKET: common parent exists, one complete joint arrow does not print. | Separate fitted tables are not a parent. |
| C8 | PASS: two train/two held-out. | Fit-on-test refused. |
| C9 | PASS WITH SUPPLIED PATH. | Different paths may not be forced equal. |
| C10 | PASS on two finite bijections. | Noninjective/nonmonotone change is physical. |
| C11 | PASS: no winding record. | Hidden cycle count refused. |
| C12 | PASS: primary window ends before recurrence. | Ignoring wrap kills finite scope. |
| C13 | PASS: only A stops. | Stopped-universe inference refused. |
| C14 | PASS: seven outcomes retained. | Perfect-continuous-clock claim refused. |
| C15 | PARTIAL: principal resources print. | Cost-free/unbounded accuracy refused. |
| C16 | PASS numerically: M Lüders disturbance drives USEQ. | Nondisturbing replacement changes histories. |
| C17 | PASS: both response arms are nonzero. | Deleting $aq$ removes both. |
| C18 | PARTIAL: distinct reduced histories retained. | Markovized current-reading law fails. |
| C19 | PASS at state level: one invariant parent yields both charts. | Independent tables fail common-parent scope. |
| C20 | PASS: constraint froze first. | Decorative post-fit constraint refused. |
| C21 | PASS: inherited finite physical inner product. | Kinematic/formal norm refused. |
| C22 | PASS at covariant-isometry level. | Ideal external time operator refused. |
| C23 | PARTIAL: exact reduced two-step values exist. | One-time conditioning is insufficient. |
| C24 | PARTIAL: full state map exists. | Scalar relabel fails on UCOH. |
| C25 | PARTIAL: state map round trip is universal on common support. | One-state certification refused. |
| C26 | PASS: scalar information loss is reported. | Lossy mixture is not called full equivalence. |
| C27 | PASS at formula signature. | Predictor reading $s$ fails lineage. |
| C28 | PARTIAL: invariant guard rule is explicit. | External timer/program switch refused. |
| C29 | PASS: causal frontier remains supplied. | Clock labels derive no arrow. |
| C30 | PASS: serialization is nonphysical. | Source order as time refused. |
| C31 | PASS: sources/clocks froze before results. | Outcome-selected clock refused. |
| C32 | PASS: one fixed $D$. | Clock-indexed retuning refused. |
| C33 | FAIL POSITIVE INSTANTIATION: distinctions are correct but cases untyped. | Tick-equals-division inference refused. |
| C34 | PASS: no material foliation. | KMS/fundamental-frame claim refused. |
| C35 | PASS with operational language. | Imported GR correction refused. |
| C36 | PASS for the finite $F_+$ witness; universal scalar-kernel type needs clarification. | Clock-only reader family is incomplete. |
| C37 | PASS: UCOH coherence retained. | Forced factorization/dephasing changes source. |
| C38 | PASS: stop/recurrence/dependence print. | Success-window-only report refused. |
| C39 | PASS: comparator structure labeled supplied. | Emergence promotion refused. |
| C40 | FAIL AS CANDIDATE PRODUCT: rows over-awarded. | Scalar success word remains forbidden. |
| C41 | PASS chronology: parent inputs froze. | Post-fit wrapper is only formal. |
| C42 | PASS in prose: finite operational scope stated. | Fundamental timelessness inference refused. |

## 6. Generic attacks 1--68

| # | Seat-Q reconstruction and disposition |
|---:|---|
| 1 | Slot rank has no subsystem/instrument; kills physical-clock lineage. |
| 2 | Path length is supplied metadata; same refusal. |
| 3 | Source-code order changes under presentation; hidden time detected. |
| 4 | Run counter is an undeclared clock/resource; refused. |
| 5 | Pure serialization permutation leaves the physical formulas invariant. |
| 6 | Renaming A cannot construct B. |
| 7 | Copying A's record constructs a channel, not B. |
| 8 | Affine postprocessing is one clock in new units. |
| 9 | Held-out fitting is leakage; refused. |
| 10 | Post-result window choice is semantic replacement. |
| 11 | Output-selected clock reverses lineage. |
| 12 | Future-defined clock is not an admitted guard. |
| 13 | Zero-support conditional is undefined. |
| 14 | Diffuse null posterior is outside this finite result. |
| 15 | Null-version changes earn no physical coordinate. |
| 16 | Dropping r1 makes the parity guard unavailable. |
| 17 | Hidden readable memory violates Paper-03 completeness. |
| 18 | One-time marginals cannot certify USEQ. |
| 19 | Removing Lüders disturbance changes the instrument. |
| 20 | Same current reading does not permit history Markovization. |
| 21 | Separate A/B parent states destroy one common experiment. |
| 22 | Separate system laws are not frame descriptions. |
| 23 | Post-fit constraint is a formal wrapper. |
| 24 | Adaptive factorization is model selection after results. |
| 25 | Clock-indexed $D$ is multiple laws, not gauge. |
| 26 | Kinematic normalization cannot replace the physical inner product. |
| 27 | Unsolved Page--Wootters state supplies no parent theorem. |
| 28 | One-time Page--Wootters probabilities do not pass sequential adequacy. |
| 29 | Trinity claims outside exact domains are refused. |
| 30 | An incompatible ideal time operator changes the model. |
| 31 | Infinite-clock evidence does not prove the finite theorem. |
| 32 | Seven-state clocks cannot have unlimited certified runtime. |
| 33 | Ignoring wrap destroys the registered domain. |
| 34 | Path-position winding is hidden external time. |
| 35 | Reused phase across cycles needs a physical cycle record. |
| 36 | A q=6 inverse is impossible; B/M/Q remain active. |
| 37 | Noninjective relabel is coarse-graining, not gauge. |
| 38 | Coordinate reversal cannot derive physical time reversal. |
| 39 | Label-only pushforward changes the packet. |
| 40 | POVM-only pushforward changes measure/calibration/readers. |
| 41 | Same-path theorem cannot be exported to different paths. |
| 42 | Proper-time differences cannot be calibrated away here. |
| 43 | Increasing readings do not derive causal order. |
| 44 | Category syntax does not derive time orientation. |
| 45 | One material clock is not global time. |
| 46 | A KMS/material frame is not a fundamental foliation. |
| 47 | Full interaction deletion is the valid response control. |
| 48 | One-arm deletion/censoring fails reciprocal-response gate. |
| 49 | Deleted readout disturbance changes complete histories. |
| 50 | Compensating retune changes the parent. |
| 51 | Hidden records/apparatus/charge costs fail the resource ledger. |
| 52 | Forced factorization dephases/censors constraint correlations. |
| 53 | UCOH dephasing changes the source and full frame map. |
| 54 | Lossy frame channel cannot be called invertible. |
| 55 | One-source round trip does not certify all contexts. |
| 56 | Incomplete readers cannot certify equivalence. |
| 57 | Renaming $s$ or a Barandes target index leaves external time. |
| 58 | A readable record is not automatically a division. |
| 59 | A division/reset is not automatically a tick. |
| 60 | Factorization at every clock reading illicitly Markovizes history. |
| 61 | One representation cannot select ontology. |
| 62 | Affine agreement is not a metric. |
| 63 | Supplied trigger order is not emergent chronology. |
| 64 | Imported GR clock law is comparator input. |
| 65 | Arbitrary history-state wrapping is formal only. |
| 66 | Encoded $s\mapsto U_s$ is hidden schedule data. |
| 67 | Post-held-out parent selection violates the freeze. |
| 68 | Parameter-free notation cannot establish timeless reality. |

Every integer is dispositioned once.  Attacks 17, 18, 28, 53, 55, and 56
remain live against the candidate's missing complete-arrow proofs rather than
being counted as passed by its reduced arithmetic.

## 7. Model attacks X1--X24

| ID | Seat-Q disposition |
|---|---|
| X1 | Changing 7 replaces Hilbert spaces, inverses, sources, and recurrence; refuse. |
| X2 | Changing coefficient 2 replaces parent and calibration; refuse. |
| X3 | Deleting $aq$ changes both frozen response arms from TV 1 to 0; detected. |
| X4 | $cI$ is reader-inert and cannot pass reciprocal response. |
| X5 | USTOP has denominator $1/7$ and cannot be removed. |
| X6 | UCOH dephasing changes $F_+$ from 1 to $1/2$; detected. |
| X7 | U0 alone leaves reciprocity/coherence/dependence untested. |
| X8 | Identifying A/B records kills the relative-origin witness. |
| X9 | Copying A to B is a channel, not a subsystem. |
| X10 | Four-point fit consumes held-out evidence. |
| X11 | Dropping either held-out point removes overidentification. |
| X12 | Positive tolerance is unregistered and unnecessary. |
| X13 | B replaced by $s$ fails record lineage despite fitting. |
| X14 | Hidden lookup of $U_s$ fails the dependency gate. |
| X15 | Program-position USEQ trigger is not a relational controller. |
| X16 | Erasing r1 makes the guard untyped. |
| X17 | POVM effects omit posterior/disturbance. |
| X18 | q=6 has positive registered support; cannot be discarded. |
| X19 | Winding counter adds a physical subsystem. |
| X20 | Identity-only covariance earns no nonidentity result. |
| X21 | Label-only pushforward fails complete covariance. |
| X22 | Increasing U0 labels do not derive an arrow. |
| X23 | Modular charge is not semibounded physical energy. |
| X24 | Finite structural success does not select ontology, time, or gravity. |

## 8. Fresh Seat-Q countermodels QF1--QF24

These are theorem-level semantic tests, not software mutants.

### QF1 — coherent UCOH versus one classical comparator time

At A=1, combine q=0 at s=1 and q=1 at s=4.  No single
$\rho^{\rm lab}(s)$ equals the coherent result.  **Outcome:** kills the
claimed UCOH A-to-lab analogue at H14/M6.

### QF2 — wrong record-action sign

Use $T_g|\beta\rangle=|\beta-2g\rangle$.  Then
$(U_g\otimes T_g)W_B\ne W_BU_g$ for nonzero g.  **Outcome:** H7 fails; the
candidate's plus sign is correct.

### QF3 — fixed A-record shift

Use $\alpha\mapsto\alpha+g$ in every q sector.  The q=1 component requires
two g and UCOH loses covariance.  **Outcome:** H8 fails; controlled action is
load bearing.

### QF4 — Q dephased to choose A rate

Measure q, apply sectorwise record shifts, and forget q.  Charge-diagonal
clock statistics survive but $F_+$ drops from 1 to $1/2$.  **Outcome:** X6
and B4 kill the route.

### QF5 — covariant but incomplete target

Keep the correct $W_B$ intertwiner but discard a first-result latch later
read by the guard.  Covariance survives while the boundary fails Paper-03
completeness.  **Outcome:** demonstrates why H7 covariance alone does not
earn M5/M10.

### QF6 — origin-consuming invariant controller

Compute $\widetilde r_1$ using an unrepresented external phase origin rather
than the retained B record.  The displayed predicate is invariant but its
physical source is absent.  **Outcome:** H11/H21 fail.

### QF7 — successive bare phase projections

Apply $E_B(2)$ and later $E_B(6)$ directly on the constrained Hilbert space.
The first branch leaves it, so the second is not the printed parent arrow.
**Outcome:** H6/B3/B8 refuse the route.

### QF8 — postselect one B branch

Keep only b=2 and normalize, rather than treating it as a gauge coordinate of
the full direct sum.  The success probability is hidden and covariance is
lost.  **Outcome:** H12 fails.  The candidate's h theorem avoids this at the
reduced level.

### QF9 — weak classical UCOH reader family

Restrict readers to charge-diagonal effects.  Coherent and dephased sources
can agree, falsely certifying scalar sufficiency.  **Outcome:** C36 requires
the whole finite algebra.

### QF10 — post-hoc reader outside the licensed algebra

Choose a projector involving an apparatus factor not present at the frozen
boundary.  It cannot refute equivalence in the old packet.  **Outcome:** the
actual $F_+$ is admissible only because it lies in the B/M/Q finite target;
late apparatus readers would define a new packet.

### QF11 — vector frame map, failed history instrument

Conjugate density operators by $\mathcal S$ but leave old record labels and
guard partitions fixed.  Vectors round-trip; USEQ histories do not.
**Outcome:** H17 needs the missing complete-history transport theorem.

### QF12 — source-dependent measurement route

Use the recorded isometry for UCOH but bare reduction for U0/USEQ because
each gives favorable values.  **Outcome:** B5 forbids route selection after
results.

### QF13 — one-time comparator equality only

Match $\sigma^B_u(\beta)$ to one orbit component, then reuse the undisturbed
state after the first M measurement.  All one-time marginals can match while
the guarded posterior changes.  **Outcome:** H14 cannot imply H13.

### QF14 — encoded schedule in lift bytes

Define the lift by a hidden table $(b,b_2)\mapsto(s_1,s_2)$ even though the
public formula has no $s$.  **Outcome:** H21 fails unless the lift itself is
included in the dependency proof; it is not printed in the candidate.

### QF15 — idle temporal extension

Tensor the successful finite parent with an unread continuous clock.  All
registered predictions survive.  **Outcome:** operational redundancy cannot
select fundamental timelessness.

### QF16 — quotient collapse to one clock

Restrict all readers to one affine combination of A and B.  Two tensor labels
then collapse operationally.  **Outcome:** H9's independently shifted
$\Delta_A,\Delta_B$ controls correctly prevent this on q=0.

### QF17 — q=6 silently renormalized out

Condition every A claim on q-not-6 without printing its probability.  UA0
and UA1 each silently lose probability $1/7$, and USTOP loses one.
**Outcome:** H22/B16 detect the missing failure ledger.

### QF18 — hidden winding record

Attach a cycle number to disambiguate repeated phase.  **Outcome:** changes
the packet and parent resources; X19 refuses it.

### QF19 — finite relabel promoted to diffeomorphism

Use the two four-point pushforwards to claim full smooth covariance.
**Outcome:** H20 passes only as finite outcome-coordinate covariance.

### QF20 — reciprocal correlation promoted to directed influence

Read the symmetric constraint responses as a causal arrow.  **Outcome:** H25
and H27 keep the supplied intervention order and deny the promotion.

### QF21 — supplied order promoted to chronology

Treat “first” and “second” in the Paper-03 path as derived from increasing B.
**Outcome:** H25 fails; candidate correctly labels order supplied.

### QF22 — finite success promoted to ontology

Identify seven gauge images with seven real events.  **Outcome:** H26/H28/H30
refuse; the finite group is a reference structure, not an event web.

### QF23 — q=6 STOP without the phase outcome

Use the good $V^A_\alpha$ branches plus only $V_{\rm stop}=\Pi_6$.  USTOP
then has no retained A phase even though the pinned exact phase PVM is sharp
and future-readable there.  **Outcome:** shows why the phase-plus-STOP target
arrow must be printed rather than inferred from “complementary output.”

### QF24 — two q=6 completions with different later readers

Compare (i) STOP-only identity on q=6 with (ii) the q=6 A-phase Lüders
instrument followed by STOP append.  Both carry $\Pi_6$ and agree that A is
not invertible, but an A-record reader separates them.  **Outcome:** the
candidate's prose does not by itself certify the complete packet.

## 9. Product-valued result

### 9.1 Generic 28-coordinate product

```text
1  P04-UPSTREAM-P03V32-PRESERVED:
   PRESERVED AS AUTHORITY; PAPER-04 COMPLETE-PAIR INSTANTIATION INCOMPLETE

2  P04-CLOCK-A-PHYSICAL-PACKET-CONSTRUCTED:
   UNCONSTRUCTED AT THE COMPLETE PHASE-PLUS-STOP PAPER-03 PACKET QUANTIFIER;
   COVARIANT ISOMETRY AND GOOD-SECTOR BRANCHES SALVAGED

3  P04-CLOCK-B-PHYSICAL-PACKET-CONSTRUCTED:
   CONSTRUCTED AS A NORMALIZED COVARIANT FINITE BRANCH FAMILY;
   FULL TAGGED-PAIR PROOF NOT PRINTED

4  P04-TWO-CLOCK-JOINT-LAW-CONSTRUCTED:
   UNCONSTRUCTED AS ONE FULLY TAGGED NORMALIZED JOINT LAW

5  P04-FINITE-CLOCK-CONDITIONING-CONSTRUCTED:
   CONSTRUCTED FOR THE EXACT POSITIVE-SUPPORT REDUCED STATES

6  P04-DIFFUSE-CLOCK-CONDITIONING-AE-UNTESTED-FINITE-MODEL

7  P04-ORDINARY-CLOCK-RELATIVE-ADEQUACY:
   CONSTRUCTED FOR U0 AND THE GLOBAL B CHART ON THE FROZEN DOMAIN;
   NOT A COMPLETE ALL-FRAME PACKET RESULT

8  P04-SEQUENTIAL-ADAPTIVE-CLOCK-ADEQUACY:
   REDUCED HISTORY VALUES CONSTRUCTED;
   COMPLETE PERSPECTIVE-NEUTRAL ADAPTIVE ARROW UNCONSTRUCTED

9  P04-SAME-PATH-AFFINE-AGREEMENT:
   EXACT ON BOTH HELD-OUT POINTS WITH SUPPLIED PATH

10 P04-CLOCK-FRAME-TRANSFORMATION-CONSTRUCTED:
   CONSTRUCTED AS A UNITARY STATE/OBSERVABLE MAP ON Q-NOT-6

11 P04-CLOCK-ROUNDTRIP-EQUIVALENT:
   CONSTRUCTED FOR STATES/OBSERVABLES ON COMMON SUPPORT;
   COMPLETE INSTRUMENT/HISTORY ROUNDTRIP UNPROVED;
   UA0/UA1 Q6 LOSS PROBABILITY 1/7 NOT PRINTED

12 P04-CLOCK-NEUTRAL-PARENT-CONSTRUCTED:
   FINITE CONSTRAINED PARENT CONSTRUCTED AS A DECLARED MODEL

13 P04-LABORATORY-REDUCTION-FROM-PARENT:
   B BRIDGE CONSTRUCTED FOR ALL SOURCES;
   FIXED-Q A BRIDGE CONSTRUCTED;
   UCOH A-TO-SINGLE-s LAB BRIDGE REFUTED

14 P04-PAGE-WOOTTERS-TRINITY-FINITE-COMPARATOR:
   STATE-LEVEL FINITE REDUCTIONS CONSTRUCTED;
   COMPLETE SEQUENTIAL INSTRUMENT HYPOTHESIS UNPROVED

15 P04-POSITIVE-STOCHASTIC-PARENT:
   NOT APPLICABLE; QUANTUM CONSTRAINED PARENT USED

16 P04-REPARAMETRIZATION-COVARIANCE:
   CONSTRUCTED FOR TWO FROZEN FINITE-WINDOW PUSHFORWARDS ONLY

17 P04-HIDDEN-EXTERNAL-TIME-EXCLUDED:
   RUNTIME s ABSENT FROM THE REDUCED PREDICTOR;
   COMPLETE LIFT/CONTROLLER DEPENDENCY PROOF INCOMPLETE

18 P04-FINITE-CLOCK-LIMITS:
   PRINCIPAL DIMENSION/RECURRENCE/STOP DATA CONSTRUCTED;
   SOURCE-SPECIFIC STOP AND TARGET-MEMORY LEDGER INCOMPLETE

19 P04-CLOCK-BACKREACTION:
   BIDIRECTIONAL OPERATIONAL SOURCE-RESPONSE CONSTRUCTED ONLY

20 P04-STOPPED-RECURRENT-CLOCKS:
   A Q6 RANK STOP AND PERIOD SEVEN CONSTRUCTED;
   NO GLOBAL TIME CLAIM

21 P04-CLOCK-CHOICE-DEPENDENT-DYNAMICS:
   CONSTRUCTED; UCOH EXHIBITS COHERENT NONSCALAR FRAME RELATION

22 P04-EXTERNAL-PARAMETER-OPERATIONALLY-REDUNDANT:
   NOT EARNED AT THE PRINTED COMPLETE ALL-FRAME PRODUCT;
   B-FRAME BOUNDED STRUCTURAL REDUNDANCY SURVIVES

23 P04-CAUSAL-ORDER-STILL-SUPPLIED
24 P04-ONTOLOGY-SELECTION-UNCONSTRUCTED
25 P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED
26 P04-GRAVITY-UNCONSTRUCTED
27 P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED
28 P04-ACTUALIZATION-UNCONSTRUCTED
```

### 9.2 Fourteen model coordinates

```text
P04M-MODEL-PIN-AUTHENTIC:
  AUTHENTICATED

P04M-FINITE-GROUP-PARENT-CONSTRUCTED:
  CONSTRUCTED

P04M-PHYSICAL-SOURCE-FAMILY-NONEMPTY:
  CONSTRUCTED; ALL NINE DENOMINATORS 1/7

P04M-B-REDUCTION-GLOBAL:
  CONSTRUCTED

P04M-A-REDUCTION-Q-NOT-6:
  CONSTRUCTED

P04M-A-STOPPED-Q-6:
  CONSTRUCTED AS RANK 7 OF 49;
  COMPLETE STOPPED READOUT PACKET INCOMPLETE

P04M-COMPLETE-RELATIONAL-INSTRUMENTS-CONSTRUCTED:
  UNCONSTRUCTED AT THE FULL PAPER-03 PAIRED-ARROW QUANTIFIER

P04M-HELDOUT-SEQUENTIAL-LAW-REPRODUCED:
  REDUCED OUTCOME TABLE REPRODUCED;
  COMPLETE HISTORY LAW UNCONSTRUCTED

P04M-FULL-QUANTUM-FRAME-MAP-CONSTRUCTED:
  CONSTRUCTED FOR STATES/OBSERVABLES ON Q-NOT-6;
  FULL INSTRUMENT PACKET TRANSPORT UNPROVED

P04M-READING-ONLY-SUFFICIENCY-FAILS-ON-UCOH:
  COHERENCE WITNESS VALID;
  UNIVERSAL KERNEL TYPE REQUIRES CLARIFICATION

P04M-RECIPROCAL-INTERACTION-PASS:
  PASS AS OPERATIONAL SOURCE-RESPONSE

P04M-MULTIPLE-CHOICE-DEPENDENT:
  PASS

P04M-HIDDEN-TIME-EXCLUDED:
  PASS FOR EXPLICIT RUNTIME s;
  COMPLETE LIFT DEPENDENCY UNPROVED

P04M-CONDITIONAL-STRUCTURAL-OPERATIONAL-REDUNDANCY:
  SUPPORTED FOR THE GLOBAL B REDUCTION ON THE REGISTERED FINITE TASKS;
  NOT SUPPORTED AS THE CANDIDATE'S COMPLETE TWO-FRAME PRODUCT
```

The earliest failed generic rung is `P04-PHYSICAL-CLOCK-UNCONSTRUCTED` at
the complete A-packet quantifier.  If root treats the global $W_A$ formula as
sufficient to infer that missing packet, the next noncompensatory failure is
the one-joint-law/complete-adaptive-arrow rung, and H14's UCOH laboratory
identity remains an exact scope counterexample in either reading.

## 10. Primary-source scope

No new external literature was needed to decide the finite counterexample.
The bound primary-source ledger is used only within its hypotheses:

1. Page--Wootters motivates stationary conditional dynamics, not complete
   measurement histories, a unique factorization, or ontology.
2. Höhn--Smith--Lock supports reduction/Dirac/relational equivalence only on
   exact clock, constraint, physical-inner-product, and domain hypotheses.
   It does not turn a coherent superposition of different comparator times
   into one classical comparator time.
3. Finite-Abelian QRF results support the state-level reductions and warn
   that aligned-frame dynamics does not automatically lift to one physical
   perspective-neutral operation.
4. Quantum-frame covariance requires state, observable, instrument, record,
   memory, and dynamics transport; vector unitarity alone is insufficient.
5. Interacting-clock work supports source-dependent/nonlocal relational
   dynamics, not deletion of the interaction or automatic scalar time.
6. Finite/periodic-clock work supports explicit recurrence, resource, and
   cycle-local scope; it supplies no winding memory.
7. Paper 03 supplies a complete paired-arrow standard on a supplied causal
   comparator.  Paper 04 must instantiate that standard; citing it does not
   instantiate an arrow.
8. Barandes distinguishes conditional laws, divisions, and an actual
   trajectory.  The present Hilbert parent constructs none of his universal
   ontic objects or time-index derivation.

No source selects $p=7$, the charge polynomial, the factorization, the
sources, a fundamental clock, an actual history, spacetime, or gravity.

## 11. Final judgment

The candidate contains a good exact finite calculation.  Its representation,
projector, source normalization, two reduction domains, coherent record
action, relative-clock witness, B-frame orbit bridge, affine held-out values,
history arithmetic, interference witness, response controls, baselines, and
finite walls mostly withstand hostile reconstruction.

It nevertheless overstates that calculation in two noncompensatory ways.
First, its A-relative UCOH state is not any single member of the frozen
classically parameterized laboratory orbit, so the asserted analogous bridge
is false.  Second, state-level isometries and a reduced outcome table are
promoted to complete Paper-03 clock and history packets without printing the
paired arrows, target memory, and all-reader identities that the pin made the
central construction gate.  The four division controls are likewise only
schemas.

Therefore:

```text
REVISE
```

This verdict does not authorize an automatic repair.  A later authority may
decide whether the surviving finite theorem should be terminally scoped or
whether a separately authorized candidate should type the missing arrows and
narrow the UCOH laboratory statement without changing the frozen
probabilities.

## 12. Freeze authentication

Immediately before freeze I reauthenticated every protocol-bound artifact.
Only this report was written.  It remains unstaged and uncommitted, uses LF
endings, ends in one LF, and contains no trailing horizontal whitespace.

Report LF line count: `000920`

Report byte count: `042107`

Report ordinary SHA-256: reported externally after freeze; embedding an
ordinary self-hash would be circular.

Report normalized self-SHA-256:
`0cd66411a2181189199311a68c5aa0146d01fe11823e8c959f4d90a226a66afa`

Normalization rule: replace the six decimal digits on each report count line
and the 64 hexadecimal characters on the report normalized-self line by
ASCII zeroes, preserve every other byte, and compute SHA-256.  The report
uses LF endings, ends in one LF, and contains no trailing horizontal
whitespace.
