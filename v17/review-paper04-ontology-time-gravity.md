# Paper 04 hostile review — Seat O

## Ontology, time, relativity, Barandes, and gravity

Date: 2026-08-23

Status: **FROZEN MUTUALLY BLIND SCIENTIFIC REVIEW**

Seat: **O — ontology, time, relativity, Barandes, and gravity**

Verdict:

```text
REJECT
```

First decisive semantic counterexample:

```text
H8 / M4 — the Q-controlled A-pointer action is a unitary action on a
quantum pointer, but it is not an action on the claimed Paper-03 classical
record algebra. UCOH makes the mismatch unavoidable.
```

Earliest failed rung:

```text
P04-CLOCK-A-PHYSICAL-PACKET-UNCONSTRUCTED
```

The finite constraint, physical Hilbert space, global B reduction, restricted
A coordinate reduction, B clock packet, B-relative USEQ law, coherent
state-level frame map, scalar-sufficiency no-go, recurrence/stoppage facts,
and permanent ontology/gravity refusals survive as noncompensatory salvage.
They do not supply the claimed complete two-clock classical-record parent.

No candidate edit, semantic repair, or successor is authorized or proposed by
this report.

## 0. Authentication, corpus, and blindness

I authenticated exact review HEAD
`8faa5b83d1a3a7cb0a33ae9e5b470c8c075785a4` and read every bound artifact
completely before judgment.

| Artifact | Observed ordinary SHA-256 | LF / bytes |
|---|---|---:|
| `v17/note-paper04-hostile-review-protocol.md` | `d763bb685003312e4529b62e29cceebd7eb0182d2a4ca3fbb3f6c118176715e9` | 269 / 12,524 |
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

The hostile protocol's ordinary and normalized hashes are respectively
`d763bb685003312e4529b62e29cceebd7eb0182d2a4ca3fbb3f6c118176715e9`
and `4775f0a5aebfc7f72367caed61b72574c5eadafc74dcdfd24ad0052e860f8c4f`.
The candidate's normalized self-hash reproduces
`5f5e2aebd8b7382df97e07914ee552a3d95ffebd9103f8da5ffbf7377fabe600`.

I did not inspect, name, contact, infer, or communicate with either sibling
hostile-review seat or report. I used no implementation as evidence. I edited
no candidate, protocol, authority, ledger, plan, or register. This report is
my sole writable path and remains unstaged and uncommitted.

## 1. Decisive counterexample: a controlled quantum pointer is not a classical record

Paper 03 fixes a finite retained-record boundary as the hybrid algebra

$$
\mathcal O_A
=\mathcal B_A\,\overline\otimes\ell^\infty(\mathbb Z_7)
\cong\bigoplus_{\alpha\in\mathbb Z_7}\mathcal B_A.
$$

Its record projectors

$$
z_\alpha=I_{\mathcal B_A}\otimes|\alpha\rangle\langle\alpha|
$$

are minimal central projections. Any reversible action on this declared
hybrid object must preserve its center, hence permute the $z_\alpha$ by one
record permutation independent of the internal quantum state.

The candidate instead defines

$$
T_g^{R_A}
=\sum_q|q\rangle\langle q|_Q\otimes T_{(1+q)g}^{R_A}.
$$

For nonzero $g$,

$$
T_g^{R_A}z_\alpha(T_g^{R_A})^\dagger
=\sum_q|q\rangle\langle q|_Q\otimes
z_{\alpha+(1+q)g}.
$$

This is not central in
$\mathcal B_A\overline\otimes\ell^\infty(\mathbb Z_7)$: it fails to
commute with an admitted Q-coherence operator
$|q\rangle\langle q'|\otimes I$ whenever $q\ne q'$ and the two shifts differ.
Therefore the displayed $T_g^{R_A}$ is not an automorphism of the claimed
classical-record boundary.

The same failure is visible directly on the frozen UCOH source. In the
$\alpha=1$ A branch it contains the off-diagonal term between the q=0 and
q=1 contributions. Appending the claimed classical record gives a term

$$
|x,0\rangle\langle y,1|\otimes|1\rangle\langle1|.
$$

At $g=1$, the controlled pointer action sends this to

$$
|x',0\rangle\langle y',1|\otimes|2\rangle\langle3|,
$$

which lies outside the block-diagonal classical-record state space. Keeping
that off-diagonal pointer term makes $W_A$ a coherent premeasurement into a
quantum pointer, not the promised retained seven-valued classical Lüders
record. Dephasing the pointer restores a classical output but is not covariant
under the controlled action and destroys the UCOH coherence that later gives
the candidate's exact $1$ versus $1/2$ reader discriminator.

Thus the candidate has proved a perfectly legitimate intertwining isometry on
a quantum pointer Hilbert space. It has not proved the simultaneously claimed
classical A record, coherent Q-controlled covariance, and UCOH preservation.
The three requirements cannot all hold in the frozen constant-fiber Paper-03
record type. Replacing the record algebra by a quantum pointer/crossed-product
object, superselecting Q, or dephasing UCOH would change a frozen semantic
object. This is not a certificate or prose defect.

The Q-phase record described in Section 4.3 has the analogous controlled-by-A
problem on any A-charge-coherent source. The B and M records avoid this exact
obstruction because their shifts are state-independent permutations.

This counterexample controls H8, M4, M5, H17/M12/M14 at complete-packet
level, M18's record-resource claim, and the strongest rung. It does not undo
the finite parent or the B-relative salvage.

## 2. Independent finite and physical reconstruction

### 2.1 Constraint and reductions

For fixed charges, $D=a+2b+m+q+aq$ is a $\mathbb Z_7$ character exponent,
so $U_gU_h=U_{g+h}$, $U_g^\dagger=U_{-g}$, and the character average is an
orthogonal projector. Since $2^{-1}=4$, every $(a,m,q)$ fixes exactly one
$b=-4(a+m+q+aq)$; hence the physical dimension is $7^3=343$.

Every frozen seed has a sharp B phase. Its seven B-phase orbit values differ
by the bijective translation $2s$, so only the identity orbit term contributes
to $\langle\phi|P|\phi\rangle$. Each of the nine denominators is therefore
$1/7$, including USTOP and both coherent seeds.

$\sqrt7\,{}_B\langle\beta|$ maps the physical orthonormal basis bijectively
to the A--M--Q basis with unit phases and is globally unitary. When $q\ne6$,
$1+q$ is invertible and the A reduction has the same property. At $q=6$ the
constraint is independent of $a$; seven allowed $(b,m)$ pairs each carry
seven A charges, while phase contraction supplies one vector per pair. Its
rank is exactly 7 on a 49-dimensional sector. The candidate correctly refuses
a global A inverse.

For B, uniqueness of the physical B charge also gives
$PE_B(\beta)P=P/7$. The branches
$V^B_\beta=7^{-1/2}\mathcal R_B(\beta)$ form a normalized instrument and
the state-independent record permutation $\beta\mapsto\beta+2g$ preserves
the classical direct-sum type. That is a genuine surviving B-clock packet.

### 2.2 Two relational degrees of freedom

On q=0, $\Delta_A=\tau_A-\tau_M$ and
$\Delta_B=\tau_B-2\tau_M$ are gauge invariant. UAO, UBO, and U0 give
$(1,0)$, $(0,1)$, and $(0,0)$. The two origin operations therefore do not
collapse to one quotient operation. This is a valid relational independence
witness for two candidate clock degrees of freedom. It does not cure the
missing complete classical A instrument, so it cannot by itself establish
two complete physical clock packets.

### 2.3 B-relative adaptive history

The all-branch controller can be reconstructed without runtime $s$. For a
first B record $b$, define $h=4(b-2)$,
$\widetilde r_1=r_1-h$, and $b_2=b+4$. Under a gauge translation,
$(b,r_1,h)\mapsto(b+2g,r_1+g,h+g)$, so $\widetilde r_1$ and
$b_2-b$ are invariant. The numeral 2 is a canonical gauge-slice coordinate,
not by itself an invariant beable.

On the canonical slice, the USEQ matter state is
$(|1\rangle+|2\rangle)/\sqrt2$. The first Lüders read gives 1 or 2 with
probability $1/2$. The original guard and two-step translation give
$(1,3)$ and $(2,5)$; the opposite guard gives $(1,4)$ and $(2,4)$, all with
the printed probabilities. A normalized B-relative Kraus family can be
formed from the first M projectors, the record-controlled translation,
$\mathcal R_B(b+4)\mathcal R_B(b)^{-1}$, and the second projectors. Hence the
B-relative history is meaningful.

Its two opportunities and their direction are still supplied by the
Paper-03 laboratory frontier. The difference-four trigger replaces runtime
$s$ with a relational clock condition inside this declared context; it does
not make the context autonomous or derive chronology.

### 2.4 Parent/comparator bridge and exact controls

Conditioning the invariant source by the global B reduction selects the same
relative A--M--Q component as the co-designed kinematic orbit after deleting
the B factor. Thus the state-level B bridge and its B-relative complete
contexts do not consume runtime $s$. This is a prefit structural identity,
not empirical selection of the parent and not proof that no temporally richer
ontology exists.

U0 gives $(\tau_A,\tau_B,\tau_M)=(s,2s,s)$. Points 0 and 1 fix the affine
law; points 2 and 3 pass without winding. The no-clock conditional M law is
uniform and has TV distance $6/7$ from a sharp target. The mistuned-B control
is sharply wrong at registered held-out records and reaches TV one.

At B record 2, U0/U1 produce A readings 1/2, while UA0/UA1 produce Q
readings 1/2. Deleting $aq$ collapses both pairs to equality. These are exact
bidirectional source-response correlations under fixed readers. They neither
orient influence nor define energy transfer, metric response, or gravity.

The common-sector state map
$\mathcal R_A(\alpha)\mathcal R_B(\beta)^{-1}$ is unitary. On UCOH, the
coherent A-relative reader $F_+$ belongs to the full finite nonrecord algebra
and distinguishes the coherent state (probability 1) from the reading-only
mixture (probability $1/2$). This exact no-go survives. What fails is the
candidate's stronger statement that the state map automatically transports
the frozen classical A-record/history packet.

## 3. Mandatory theorem reconstruction H1--H30

| ID | Independent disposition |
|---|---|
| H1 | **PASS.** The character law and orthogonal projector follow exactly. |
| H2 | **PASS.** Unique B charge gives dimension 343. |
| H3 | **PASS.** All nine denominators are $1/7$ by B-phase orbit orthogonality. |
| H4 | **PASS.** Every B reduction is a global unitary coordinate map. |
| H5 | **PASS.** A is unitary on q-not-6; its q=6 rank is 7 of 49. |
| H6 | **PASS.** Bare B compression is $P/7$ and is not the clock instrument. |
| H7 | **PASS.** The B direct-sum instrument is normalized and its state-independent record shift preserves the classical target type. |
| H8 | **FAIL — decisive.** The Q-controlled shift is a quantum-pointer action, not an action on the classical record algebra; UCOH prevents superselection or dephasing. |
| H9 | **PARTIAL PASS.** Relative readers distinguish the A and B quotient operations, but a complete physical A clock is blocked by H8. |
| H10 | **FAIL AT A/Q PACKET.** A common law over the promised complete classical records is unconstructed. The B-relative sublaw survives. |
| H11 | **PASS FOR B CONTEXT.** The all-branch invariant controller can be typed from $b,r_1,h$ and the complete M instruments. |
| H12 | **PASS WITH SUPPLIED-CONTEXT SCOPE.** No B branch is postselected and runtime $s$ is absent; the declared opportunity pair remains supplied. |
| H13 | **PASS.** The canonical and opposite-guard histories reconstruct exactly. |
| H14 | **PARTIAL.** The B state/relative-context bridge passes; an all-clock complete-packet bridge fails with H8. |
| H15 | **PASS.** The fit split and finite TV values are exact. |
| H16 | **PASS.** $F_+$ is in the admitted full finite nonrecord algebra and gives 1 versus $1/2$. |
| H17 | **FAIL AT COMPLETE PACKET.** State/observable round trip passes; direct-sum functoriality does not transport the classical A record under the controlled action. |
| H18 | **PASS WITH LANGUAGE SCOPE.** Both response values and deletion values are exact correlations. |
| H19 | **PASS.** Both baselines are exact and separated by time-sensitive readers. |
| H20 | **PASS AT FINITE COORDINATE LEVEL.** Whole-interface pushforward is a taut but valid finite relabeling result, not diffeomorphism covariance. |
| H21 | **PASS NARROWLY.** The explicit B predictor/controller contains no runtime $s$ or lookup table; the predeclared generator still encodes the co-designed relational law. |
| H22 | **PARTIAL/FAIL COMPLETENESS.** Dimensions and recurrence are exact, but the resource ledger does not resolve quantum pointer versus classical record or the required decohering/reference apparatus. |
| H23 | **FAIL.** Section 16 describes four patterns but does not define exact boundary algebras, arrows, memories, reset/entangler, licensed futures, or prove future sufficiency for them. |
| H24 | **PASS.** The parent is prefit and structural, not empirically or ontologically selected. |
| H25 | **PASS.** The adaptive order remains expressly supplied. |
| H26 | **PASS.** The finite phase group is not promoted to an event lattice or discrete ontology. |
| H27 | **PASS.** Operational reciprocity is not promoted to gravity. |
| H28 | **PASS.** Neither probabilities nor records select an actual history. |
| H29 | **FAIL AS PRINTED.** The product wrongly awards the complete A/two-clock/full-packet and division coordinates. |
| H30 | **FAIL.** The strongest rung requires H8/H10/H17 and therefore is not earned. |

## 4. Paired controls C1--C42

Both arms were reconstructed independently.

| C | Positive arm / negative arm disposition |
|---:|---|
| C1 | B is a physical packet; A's claimed classical packet fails H8. A scalar path index still has no packet. |
| C2 | Relative-origin readers defeat rename/copy mutants, but do not repair A-record typing. |
| C3 | B branches normalize. A branch effects normalize algebraically, but the claimed covariant classical instrument does not exist on UCOH. |
| C4 | B/M records are retained; A cannot be both classical and coherently controlled. Ephemeral records still fail USEQ. |
| C5 | Every used finite conditional has positive support; zero-support normalization is correctly refused. |
| C6 | Diffuse conditioning is honestly untested; null-point promotion remains refused. |
| C7 | One constrained quantum source contains both coordinate systems; the complete classical-record joint law is blocked. Separate fitted tables remain invalid. |
| C8 | Two training and two held-out points are disjoint; fit-on-test fails. |
| C9 | Same comparator path is supplied; different-path equality is correctly refused. |
| C10 | Both finite injective relabelings preserve a pushed-forward interface; partial/noninjective maps do not. |
| C11 | No winding is claimed; a hidden cycle counter is excluded. |
| C12 | The primary window precedes recurrence; ignoring recurrence fails. |
| C13 | q=6 stops A as a frame only; B/M/Q remain available. |
| C14 | Seven-outcome resolution is explicit; no continuous ideal clock is claimed. |
| C15 | Finite system resources print, but A-record classicalization resources are missing; cost-free accuracy remains refused. |
| C16 | USEQ includes M Lüders disturbance; the nondisturbing mutant changes the history. |
| C17 | Both correlation arms and the deletion control pass; they do not establish causal response. |
| C18 | The B-relative history retains $r_1$, guard, and posterior; Markovization fails. |
| C19 | One parent yields both state frames, but complete-record frame equivalence is blocked; independent tables still fail. |
| C20 | The constraint froze before results; a decorative post-fit constraint is refused. |
| C21 | The physical inner product normalizes sources; kinematic normalization is insufficient. |
| C22 | B has a covariant classical phase record. A has only a coherent quantum-pointer dilation as written; an ideal-time import remains refused. |
| C23 | USEQ supplies two-step statistics; one-time conditioning is insufficient. |
| C24 | State/observable transport passes. Complete classical A-record transport fails; scalar relabeling also fails on UCOH. |
| C25 | State-map round trips pass on the common sector; all-context packet round trips do not. |
| C26 | Scalar information loss is printed exactly and is not called full equivalence. |
| C27 | Runtime $s$ occurs only in the comparator bridge; a predictor that reads it fails lineage. |
| C28 | The B/M guard consumes retained relational records; an external program switch is correctly rejected. |
| C29 | The causal frontier remains supplied; clock labels do not derive arrows. |
| C30 | Serialization is declared presentation only; source order is not time. |
| C31 | Sources/clocks froze before outcomes; outcome-selected clocks are rejected. |
| C32 | One fixed $D$ governs all sources; clock-indexed retuning is rejected. |
| C33 | The conceptual distinctions are correct, but the four exact process cases are not typed; tick-equals-division remains false. |
| C34 | No material state is said to select a foliation. |
| C35 | The source-response calculation uses the same law and is not called GR. |
| C36 | The admitted $F_+$ reader detects UCOH coherence; clock-only readers would be too weak. |
| C37 | The state-level map retains Q coherence, but the classical A-record instrument cannot; forced factorization is still wrong. |
| C38 | Stoppage, recurrence, and source dependence are printed; success-window censorship is absent. |
| C39 | Comparator order/path/geometry remain labeled supplied; emergence is refused. |
| C40 | Coordinates print separately, but several positive values are false after H8/H23; a scalar success word remains forbidden. |
| C41 | Parent inputs froze before calculation; a fitted movie wrapper would be formal only. |
| C42 | B-side runtime redundancy is finite and operational; fundamental timelessness does not follow, while the two-clock strongest rung is blocked. |

## 5. Generic hostile attacks 1--68

The following table keeps every attack distinct and in numerical order.
`PASS` means the candidate detects/refuses the mutant at its honest scope;
`FAIL` identifies an attack that exposes a candidate defect.

| # | Seat-O reconstruction |
|---:|---|
| 1 | PASS — causal-slot rank has no clock packet. |
| 2 | PASS — path length is supplied geometry, not a clock. |
| 3 | PASS — source-code order has no physical lineage. |
| 4 | PASS — a run counter is a hidden schedule. |
| 5 | PASS — pure presentation permutation leaves the physical formulas fixed. |
| 6 | PASS — relative readers defeat the A/B rename mutant. |
| 7 | PASS — copied A outcome is a channel, not B. |
| 8 | PASS — affine A postprocessing is not an independent subsystem. |
| 9 | PASS — fitting held-out points is leakage. |
| 10 | PASS — post-result window choice is retuning. |
| 11 | PASS — output-selected clock reverses lineage. |
| 12 | PASS — future-outcome clock definition is acausal conditioning. |
| 13 | PASS — zero-support normalization is refused. |
| 14 | PASS/INAPPLICABLE — diffuse-null posterior earns no finite coordinate. |
| 15 | PASS/INAPPLICABLE — null-version changes are not new finite physics. |
| 16 | PASS — dropping $r_1$ makes the guard unavailable. |
| 17 | FAIL IN A PACKET — the candidate itself leaves the classical/quantum A-pointer target unresolved; hidden apparatus generally fails completeness. |
| 18 | PASS — one-time marginals cannot certify USEQ. |
| 19 | PASS — deleting Lüders disturbance changes USEQ. |
| 20 | PASS — equal current readings do not license Markovization. |
| 21 | PASS — separate parent states are not a frame change. |
| 22 | PASS — separate system laws are retuning. |
| 23 | PASS — a constraint appended after results is formal only. |
| 24 | PASS — target-adapted factorization changes the model. |
| 25 | PASS — clock-indexed law changes are dependence, not gauge. |
| 26 | PASS — the kinematic norm is not the physical inner product. |
| 27 | PASS — Page--Wootters language without exact solutions/reductions proves nothing. |
| 28 | PASS — one-time conditioning is insufficient for USEQ. |
| 29 | PASS — finite reference-frame results apply only on proved domains. |
| 30 | PASS — no ideal self-adjoint time operator is imported. |
| 31 | PASS — an infinite clock cannot prove this finite result. |
| 32 | PASS — seven-state clocks cannot receive unlimited runtime. |
| 33 | PASS — wraparound is explicitly bounded. |
| 34 | PASS — path position cannot supply winding. |
| 35 | PASS — phase reuse across cycles needs new memory. |
| 36 | PASS — q=6 cannot be passed through an A inverse. |
| 37 | PASS — noninjective relabeling is coarse graining, not gauge. |
| 38 | PASS — orientation reversal is outside the registered covariance. |
| 39 | PASS — label-only transport is incomplete. |
| 40 | PASS — effect-only transport omits the interface. |
| 41 | PASS — different comparator paths are not forced equal. |
| 42 | PASS — proper-time differences cannot be fitted away; none is derived here. |
| 43 | PASS — increasing readings do not derive causal order. |
| 44 | PASS — category direction is syntax until operationally earned. |
| 45 | PASS — one local clock is not global time. |
| 46 | PASS — no KMS/material frame becomes a fundamental foliation. |
| 47 | PASS — deleting $aq$ removes both exact source-response contrasts. |
| 48 | PASS — a one-arm deletion cannot earn reciprocity. |
| 49 | PASS FOR USEQ / FAIL FOR A TYPE — disturbance matters, but the A classical record remains unconstructed. |
| 50 | PASS — compensating retuning is refused. |
| 51 | FAIL PARTIALLY — the ledger omits the resource/type needed to turn the controlled A quantum pointer into a classical covariant record. |
| 52 | PASS — forced factorization destroys constraint/coherence. |
| 53 | PASS — UCOH may not be dephased during a frame change. |
| 54 | PASS — q=6 loss is not called invertible. |
| 55 | FAIL AT COMPLETE PACKET — all-state unitary mapping does not certify the invalid A-record action. |
| 56 | PASS — incomplete clock-only readers cannot certify UCOH equivalence. |
| 57 | PASS — renaming $s$ or a target index is not a physical clock. |
| 58 | PASS CONCEPTUALLY / FAIL CONSTRUCTION — a record need not be a division, but exact cases are not instantiated. |
| 59 | PASS CONCEPTUALLY / FAIL CONSTRUCTION — a division need not be a tick, but exact cases are not instantiated. |
| 60 | PASS — the paper does not factor every indivisible history at a reading. |
| 61 | PASS — the constrained representation is not promoted to unique ontology. |
| 62 | PASS — affine agreement is not called a metric. |
| 63 | PASS — supplied opportunity order is not called emergent chronology. |
| 64 | PASS — no GR dilation is imported. |
| 65 | PASS WITH FORMAL CEILING — a target-wrapped parent would be formal; the present co-designed bridge remains only structural. |
| 66 | PASS NARROWLY — no runtime table is printed in the B controller; a predeclared law necessarily contains its own correlations. |
| 67 | PASS — the parent froze before held-out evaluation. |
| 68 | PASS — parameter-free notation is not promoted to timeless ontology. |

## 6. Model-specific attacks X1--X24

| X | Independent disposition |
|---:|---|
| X1 | Changing 7 changes the model, recurrence, and invertibility; refused. |
| X2 | Changing B coefficient 2 changes the model and comparator; refused. |
| X3 | Deleting $aq$ collapses both response contrasts exactly. |
| X4 | A scalar interaction supplies no registered relational response. |
| X5 | USTOP has positive norm and is retained. |
| X6 | Dephasing UCOH changes $F_+$ from 1 to $1/2$; it also exposes the decisive A-record incompatibility. |
| X7 | U0 alone cannot test reciprocity or coherent frame transport. |
| X8 | Relative readers prevent identification of A/B origins, though A's complete record still fails. |
| X9 | Copying A into B makes a channel, not a second subsystem. |
| X10 | Four-point fitting consumes the held-out test. |
| X11 | Dropping either point weakens the frozen gate. |
| X12 | Exact finite arithmetic needs no tolerance. |
| X13 | Replacing B by $s$ fails physical lineage. |
| X14 | An encoded $s\mapsto U_s$ controller is hidden time. |
| X15 | Program-position triggering fails the relational controller gate. |
| X16 | Erasing $r_1$ makes the guard unavailable. |
| X17 | PVM effects alone omit posterior disturbance. |
| X18 | q=6 cannot be silently renormalized out. |
| X19 | A winding register would be a new physical subsystem. |
| X20 | Identity-only covariance is nondiscriminating. |
| X21 | Label-only pushforward is incomplete. |
| X22 | Increasing U0 readings leave order supplied. |
| X23 | Modular charge is not semibounded physical energy. |
| X24 | Finite conditional success cannot select ontology, spacetime, or gravity. |

## 7. Binding conditions B1--B20

| B | Candidate disposition |
|---:|---|
| B1 | PASS — frozen $\mathbb Z_7$ parent and sources are unchanged. |
| B2 | PASS — representation, projector, dimension, and denominators are proved. |
| B3 | **FAIL** — B has a covariant classical record; A has only a coherent quantum-pointer action, not the promised classical record. |
| B4 | **FAIL** — coherent A action and classical retained record cannot both occupy the frozen hybrid algebra on UCOH. |
| B5 | **FAIL** — the candidate treats premeasurement isometry and direct-sum Lüders instrument as equivalent without an all-reader/covariance theorem. |
| B6 | PASS — A's q-not-6 domain and q=6 rank loss are explicit. |
| B7 | PARTIAL PASS — relative readers establish distinct quotient operations; two complete clock packets are not established. |
| B8 | PASS FOR B-RELATIVE USEQ — all branches, $r_1$, guard, transport, and second reader can be reconstructed. |
| B9 | PASS — the laboratory frontier remains supplied. |
| B10 | **FAIL AT COMPLETE PACKET** — state/observable transport passes; classical A record/history transport does not. |
| B11 | PASS — training and held-out values remain disjoint and exact. |
| B12 | PASS — both baselines are informative under complete M readers. |
| B13 | PASS NARROWLY — explicit B prediction has no runtime $s$; the comparator remains supplied. |
| B14 | PASS WITH FINITE SCOPE — the two full-interface relabelings are coordinate covariance only. |
| B15 | PASS WITH LANGUAGE SCOPE — both source-response arms and deletion values are exact. |
| B16 | **FAIL COMPLETENESS** — the unresolved classicalization/reference apparatus is absent from the resource ledger. |
| B17 | **FAIL CONSTRUCTION / PASS ACTUALITY WALL** — four exact process cases are described but not typed; no outcome is actualized. |
| B18 | PASS — the prose observes the conditional structural ceiling. |
| B19 | PASS — geometry, chronology, and gravity remain unconstructed. |
| B20 | PASS — no implementation selects or repairs the physics. |

## 8. Fresh Seat-O semantic countermodels O1--O24

These are independent physical/type attacks, not source-code mutations.

### O1 — controlled action violates the classical center

The exact UCOH/center calculation in Section 1 is decisive. The controlled
shift does not act on $\mathcal B\overline\otimes\ell^\infty(R_A)$.

**Result:** kills H8/M4 first.

### O2 — dephase the pointer after the coherent isometry

Apply record dephasing to make $R_A$ classical. It fails to commute with the
Q-controlled gauge action and removes the cross-sector coherence detected by
$F_+$.

**Result:** H8 and H16 cannot both survive this route.

### O3 — keep the full quantum pointer

Retain all off-diagonal pointer operators so covariance is well defined. The
target is then $\mathcal B\overline\otimes\mathcal B(\mathbb C^7)$, not the
frozen classical record algebra; no actual classical outcome has been written.

**Result:** semantic target replacement, not a repair of M4.

### O4 — wrong sign in the B record action

Use $\beta\mapsto\beta-2g$. Direct substitution into the intertwiner gives
opposite labels and fails except at $g=0$.

**Result:** detected; candidate's B sign is correct.

### O5 — state-independent A shift

Use $\alpha\mapsto\alpha+g$ for q=0 and q=1. It fails on UCOH's q=1 sector,
whose shift is $2g$.

**Result:** detected; motivates but does not solve O1.

### O6 — Q-dephase before controlling A

Measure q, classically choose a record permutation, and discard q. The target
becomes a valid classical mixture but $F_+$ falls from 1 to $1/2$.

**Result:** X6 fires; not allowed.

### O7 — covariant pointer with incomplete target

Keep a gauge-covariant pointer but omit the environment or off-diagonal
pointer degrees from the complete boundary. A later coherence reader can
distinguish the omission.

**Result:** B3/B16 and Paper-03 completeness fail.

### O8 — unmodeled phase origin in the guard

Apply parity directly to the raw $r_1$ label while leaving the set of even
representatives fixed under gauge translation.

**Result:** this mutant fails; the candidate's $\widetilde r_1$ construction
correctly avoids it for B-relative USEQ.

### O9 — two successive bare B projections

Project B kinematically at 2 and 6 without reduction/transport. Each branch
leaves the physical subspace and is not the relational process.

**Result:** candidate avoids this mutant.

### O10 — canonical-branch postselection

Keep only $b=2$ and discard the other six uniform B branches. The printed
conditional table remains but the instrument is not trace preserving.

**Result:** candidate's all-branch extension defeats the mutant.

### O11 — weak diagonal reader family

Restrict readers to q-diagonal observables. The UCOH scalar mixture appears
sufficient by construction.

**Result:** rejected; the complete nonrecord algebra admits $F_+$.

### O12 — genuinely post-hoc coherent reader

Add a reader not in the frozen boundary algebra after seeing a scalar result.
That would change the experiment. Here $F_+$ is already an effect in the
declared full finite algebra and instantiates a predeclared universal
quantifier.

**Result:** candidate passes this attack.

### O13 — state-unitary but history-invalid frame map

Conjugate density operators by $\mathcal S_{A\leftarrow B}$ and assert that
classical records follow functorially. O1 shows the A history algebra is not
preserved even though the state map is unitary.

**Result:** kills H17/M12/M14 at packet level.

### O14 — source-dependent measurement route

Use a classical A instrument on fixed-q sources and a coherent quantum
pointer only on UCOH. That makes the apparatus depend on the source and
prevents one common experiment.

**Result:** M5 fails.

### O15 — one-time-only parent/comparator equality

Match only U0 phase marginals and ignore USEQ records/posteriors. Such a
wrapper cannot earn sequential adequacy.

**Result:** candidate's B-relative USEQ calculation defeats this mutant.

### O16 — encoded $s$ table

Store $s\leftrightarrow\beta$ and the orbit family in controller bytes while
presenting a beta-only signature.

**Result:** forbidden by lineage; no such table is needed by the explicit B
guard, though the parent/comparator remain co-designed.

### O17 — idle temporal extension

Tensor the parent with an unobserved temporal sector and leave every
registered reader unchanged.

**Result:** all operational data agree, so fundamental timelessness and unique
ontology remain unselected exactly as the candidate states.

### O18 — one-clock quotient collapse

Identify UAO and UBO after projection. The invariant pairs $(1,0)$ and
$(0,1)$ are then falsely identified and an admitted relative reader separates
them.

**Result:** candidate defeats the quotient-collapse mutant.

### O19 — silently remove q=6

Condition all sources on q-not-6 and renormalize. This deletes a positive-norm
source and turns local A-frame failure into artificial global success.

**Result:** candidate correctly retains USTOP.

### O20 — add a winding counter

Append a cycle number to distinguish repeated phase labels. This creates a new
clock/reference subsystem and changes the frozen model.

**Result:** refused; recurrence ceiling survives.

### O21 — finite relabeling promoted to diffeomorphism invariance

Push forward seven outcome labels and infer spacetime covariance. No
localization net, manifold, causal cone, or tensor field follows.

**Result:** candidate explicitly refuses the promotion.

### O22 — reciprocal correlation promoted to directed influence

Read the two TV-one source contrasts as two causal arrows. The frozen
intervention order and comparison contexts are supplied, and the contrasts do
not establish counterfactual spacetime influence.

**Result:** candidate's wording remains operational and passes.

### O23 — supplied order promoted to emergent chronology

Treat the declared first/second opportunities or category word order as
physical time orientation.

**Result:** candidate explicitly keeps the frontier supplied.

### O24 — record/division templates mistaken for constructions

Name an omitted latch, reset, and unresolved entangler without fixing their
boundary algebras, channels, licensed futures, and reader laws. The words
realize no future-sufficiency theorem.

**Result:** this is exactly the remaining defect in Section 16; H23/M21 fail.

## 9. Full noncompensatory product

### 9.1 Generic 28-coordinate product

```text
1  P04-UPSTREAM-P03V32-PRESERVED:
   PASS — INCLUDING ITS CLASSICAL-RECORD TYPE, WHICH EXPOSES H8

2  P04-CLOCK-A-PHYSICAL-PACKET-CONSTRUCTED:
   FAIL — COHERENT QUANTUM POINTER IS NOT THE CLAIMED CLASSICAL RECORD

3  P04-CLOCK-B-PHYSICAL-PACKET-CONSTRUCTED:
   PASS

4  P04-TWO-CLOCK-JOINT-LAW-CONSTRUCTED:
   FAIL AT COMPLETE RECORD LEVEL

5  P04-FINITE-CLOCK-CONDITIONING-CONSTRUCTED:
   PASS FOR B; A COMPLETE CLASSICAL CONDITIONING PACKET UNCONSTRUCTED

6  P04-DIFFUSE-CLOCK-CONDITIONING-AE-CONSTRUCTED:
   UNTESTED / NOT APPLICABLE TO THIS FINITE PRIMARY MODEL

7  P04-ORDINARY-CLOCK-RELATIVE-ADEQUACY:
   PASS FOR THE FROZEN B-RELATIVE DOMAIN

8  P04-SEQUENTIAL-ADAPTIVE-CLOCK-ADEQUACY:
   PASS FOR THE B-RELATIVE USEQ CONTEXT WITH SUPPLIED ORDER

9  P04-SAME-PATH-AFFINE-AGREEMENT:
   PASS EXACTLY ON BOTH HELD-OUT POINTS

10 P04-CLOCK-FRAME-TRANSFORMATION-CONSTRUCTED:
   PASS AS A QUANTUM STATE/OBSERVABLE MAP ON Q-NOT-6;
   FAIL AS A COMPLETE CLASSICAL-RECORD PACKET MAP

11 P04-CLOCK-ROUNDTRIP-EQUIVALENT:
   PASS FOR QUANTUM STATE/OBSERVABLE MAP ON COMMON SECTOR;
   COMPLETE-CONTEXT ROUNDTRIP UNCONSTRUCTED

12 P04-CLOCK-NEUTRAL-PARENT-CONSTRUCTED:
   PASS AS A FINITE CONSTRAINED QUANTUM PARENT

13 P04-LABORATORY-REDUCTION-FROM-PARENT-CONSTRUCTED:
   PASS FOR B-RELATIVE STATES/CONTEXTS AS A CO-DESIGNED STRUCTURAL BRIDGE;
   FAIL FOR THE CLAIMED ALL-CLOCK COMPLETE PACKET

14 P04-PAGE-WOOTTERS-TRINITY-FINITE-COMPARATOR:
   PARTIAL — STATE-LEVEL FINITE REDUCTION PASS; COMPLETE A INSTRUMENT FAIL

15 P04-POSITIVE-STOCHASTIC-PARENT:
   NOT APPLICABLE — NO BARANDES-TYPE PARENT CONSTRUCTED

16 P04-REPARAMETRIZATION-COVARIANCE-CONSTRUCTED:
   PASS ONLY AS TWO FINITE COMPLETE-INTERFACE COORDINATE PUSHFORWARDS

17 P04-HIDDEN-EXTERNAL-TIME-EXCLUDED:
   PASS FOR THE B-RELATIVE FROZEN PREDICTOR;
   NOT A FUNDAMENTAL-TIME OR ONTOLOGY THEOREM

18 P04-FINITE-CLOCK-LIMITS-CONSTRUCTED:
   PARTIAL — RECURRENCE/STOP PASS; A-RECORD RESOURCE TYPE INCOMPLETE

19 P04-CLOCK-BACKREACTION-CONSTRUCTED:
   PASS ONLY AS BIDIRECTIONAL OPERATIONAL SOURCE-RESPONSE CORRELATIONS

20 P04-STOPPED-RECURRENT-CLOCKS-CLASSIFIED:
   PASS

21 P04-CLOCK-CHOICE-DEPENDENT-DYNAMICS:
   PASS AT STATE/READING LEVEL; COMPLETE TWO-CLOCK PACKET FAILS

22 P04-EXTERNAL-PARAMETER-OPERATIONALLY-REDUNDANT:
   PASS ONLY FOR THE B-RELATIVE CO-DESIGNED FINITE REGISTERED PREDICTIONS;
   THE PRINTED STRONGEST TWO-CLOCK RUNG IS NOT EARNED

23 P04-CAUSAL-ORDER-STILL-SUPPLIED:
   PASS / BINDING

24 P04-ONTOLOGY-SELECTION-UNCONSTRUCTED:
   PASS / BINDING

25 P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED:
   PASS / BINDING

26 P04-GRAVITY-UNCONSTRUCTED:
   PASS / BINDING

27 P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED:
   PASS / BINDING

28 P04-ACTUALIZATION-UNCONSTRUCTED:
   PASS / BINDING
```

### 9.2 Model-selection 14-coordinate product

```text
P04M-MODEL-PIN-AUTHENTIC:
  PASS

P04M-FINITE-GROUP-PARENT-CONSTRUCTED:
  PASS

P04M-PHYSICAL-SOURCE-FAMILY-NONEMPTY:
  PASS — ALL NINE DENOMINATORS 1/7

P04M-B-REDUCTION-GLOBAL:
  PASS

P04M-A-REDUCTION-Q-NOT-6:
  PASS AS A QUANTUM COORDINATE MAP

P04M-A-STOPPED-Q-6:
  PASS — RANK 7 OF 49, SOURCE RETAINED

P04M-COMPLETE-RELATIONAL-INSTRUMENTS-CONSTRUCTED:
  FAIL — A CLASSICAL RECORD INCOMPATIBLE WITH COHERENT CONTROL

P04M-HELDOUT-SEQUENTIAL-LAW-REPRODUCED:
  PASS FOR B-RELATIVE USEQ

P04M-FULL-QUANTUM-FRAME-MAP-CONSTRUCTED:
  PASS FOR STATES/OBSERVABLES ON COMMON SECTOR;
  COMPLETE HISTORY INSTRUMENT DOES NOT FOLLOW

P04M-READING-ONLY-SUFFICIENCY-FAILS-ON-UCOH:
  PASS — 1 VERSUS 1/2

P04M-RECIPROCAL-INTERACTION-PASS:
  PASS AS OPERATIONAL SOURCE-RESPONSE ONLY

P04M-MULTIPLE-CHOICE-DEPENDENT:
  PASS AT THE REGISTERED STATE/READING LEVEL

P04M-HIDDEN-TIME-EXCLUDED-ON-FROZEN-DEPENDENCY-GRAPH:
  PASS FOR THE EXPLICIT B PREDICTOR/CONTROLLER ONLY

P04M-CONDITIONAL-STRUCTURAL-OPERATIONAL-REDUNDANCY:
  DEMOTED TO B-RELATIVE PARTIAL SALVAGE;
  COMPLETE TWO-CLOCK VERSION FAILS
```

### 9.3 Earliest rung and surviving ceiling

The earliest failed coordinate is the A physical clock packet, before the
complete two-clock joint law. No later unitary-frame or calibration success
compensates for it.

The strongest honest surviving statement is:

> The frozen finite constrained parent has a global B-relative clock packet,
> exact B-relative adaptive histories, a restricted A quantum coordinate map,
> and exact state-level temporal-frame identities. Runtime $s$ is unused by
> the B-relative registered predictor on the co-designed finite domain.
> A complete classical A record and hence the claimed complete two-clock
> packet are unconstructed.

## 10. Ontology, Barandes, relativity, and gravity

The candidate is an orthodox finite constrained Hilbert-space construction.
Its conditional frame maps do not constitute an ontology of actual
configurations. Barandes's published indivisible-stochastic framework starts
with ordinary configuration probabilities and time-indexed indivisible
stochastic laws; Hilbert-space objects are secondary representations. It
does not license turning a Page--Wootters reduction parameter into a physical
clock, an actual outcome, or a division event. See Jacob A. Barandes,
[*Quantum Systems as Indivisible Stochastic Processes*](https://arxiv.org/abs/2507.21192).

Paper 04 correctly says it has not constructed or replaced that ontology.
Its B records are operational packet variables. Its probabilities do not say
which history happened. Its Section-16 division templates also cannot inherit
Barandes's conditioning permission merely by being called future sufficient;
their exact licensed future laws must be built, which has not occurred.

The finite Abelian reference-frame literature supports constrained reduction
maps but not identification of a finite gauge group with physical time or
spacetime; see Höhn, Krumm, and Müller,
[*Internal quantum reference frames for finite Abelian groups*](https://arxiv.org/abs/2107.07545).
Likewise, inequivalent relational measurement realizations for nonideal
temporal frames make the instrument route physical rather than cosmetic; see
Hausmann, Schmidhuber, and Castro-Ruiz,
[*Measurement events relative to temporal quantum reference frames*](https://arxiv.org/abs/2308.10967).
That source scope reinforces rather than repairs the H8 failure.

Nothing here supplies a causal order, time orientation, locality net,
dimension, Lorentzian signature, duration scale, metric, curvature,
stress-energy, equivalence principle, Einstein constraint algebra, or
backreaction of geometry. The comparator provides the path and order. The
finite coordinate pushforwards are not diffeomorphisms of spacetime. The
two source-response contrasts are not gravitational reciprocity. The
q=6 stoppage is a failure of one internal frame, not frozen time or a horizon.

The idle-temporal-extension countermodel also remains decisive for ontology:
an empirically invisible temporal factor can be tensored onto the parent
without changing registered probabilities. Therefore even a repaired finite
clock construction could establish operational redundancy only, never the
absence of fundamental time.

## 11. Final judgment

The mathematical parent contains several exact, worthwhile results. The
candidate is also unusually disciplined about supplied order, finite scope,
actuality, spacetime, and gravity. Those virtues do not close the central
type gap.

The frozen construction requires the A record to be simultaneously:

1. a seven-valued classical Paper-03 record;
2. covariant under a Q-dependent shift; and
3. coherence preserving on UCOH.

The controlled-shift counterexample proves that this triple is not a valid
object in the frozen hybrid algebra. The isometry $W_A$ proves a quantum
premeasurement, while the direct-sum branches describe a classical
instrument; the candidate silently equates them at exactly the point where
the controlled action prevents that equivalence. Section 16 independently
asserts rather than constructs its four record/division cases.

Because the missing A packet is central to the advertised two-clock result
and cannot be repaired without changing a frozen boundary type, instrument,
or coherent source, the verdict is:

```text
REJECT
```

First decisive semantic counterexample: **H8/M4, UCOH under the
Q-controlled A-record action**.

No automatic correction or successor follows from this review. Root may
adjudicate the explicit salvage product independently.

## 12. Freeze authentication

Candidate ordinary SHA-256 reauthenticated at freeze:
`25d6771bd4bbfb658a54da7f65cdcc9620b0769f6d7be6075103ff5d44230dc6`

Protocol ordinary SHA-256 reauthenticated at freeze:
`d763bb685003312e4529b62e29cceebd7eb0182d2a4ca3fbb3f6c118176715e9`

Model-pin ordinary SHA-256 reauthenticated at freeze:
`8adb5def4c927dd55eba4c2360782b1b6d9370fcf3f5d5c76f5458b1a0fbca4e`

Report LF line count: `000896`

Report byte count: `044044`

Report ordinary SHA-256: reported externally after freeze; embedding an
ordinary self-hash would be circular.

Report normalized self-SHA-256:
`8039b8bc765aec3d77c8b9a97f7f8087aa5b5cb089753b3c793c8367949b264f`

Normalization rule: replace the six decimal digits on each report count line
and the 64 hexadecimal characters on the report normalized-self line by
ASCII zeroes, preserve every other byte, and compute SHA-256. The report uses
LF endings, ends in one LF, and has no trailing horizontal whitespace.
