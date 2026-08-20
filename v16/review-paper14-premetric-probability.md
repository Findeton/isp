# Paper 14 hostile review — Seat P: probability, stability, and division

- Date: 2026-08-20
- Protocol status: frozen mutually blind hostile review
- Grade: **REJECT**
- Earliest affected product coordinate: **stable-happening identity; the submitted promotion cannot pass beyond `P14-ONSET-GERMS-PRESENTATION-ONLY` because its mandatory eraser discriminator is false**
- First exact scientific counterexample: **H4 `RECORD-ERASER`; the submitted map is a reversible sector permutation, not an eraser**
- Ordinary SHA-256: reported externally after freeze
- Normalized self-hash convention: replace exactly the 64 lowercase hexadecimal characters on the line beginning `normalized_self_sha256:` by 64 ASCII zeroes, preserving every other byte.
normalized_self_sha256: ebdf6a2883ed4535b485b9643041610ca8101e8deff47ac6fe298c12db3a5188

## 1. Disposition

The declared reciprocal law, the six-generator sealed-word theorem, the two
full division frontiers, the projected-frontier refusal, and the native
nondivision example all reconstruct exactly.  In particular, this review does
not turn a stable record into an automatic Markov step, and it does not treat
an enlarged history carrier as a repair of a failed native cut.

The submission nevertheless fails a mandatory scientific control.  Its H4
object is

\[
E=X\otimes I_2,
\]

an orthogonal permutation of the two record sectors.  The implementation
tests only the fixed-projector equations `P_r E = E P_r` and, because those
equations fail, calls `E` an eraser.  But the paper and pin state the typed
criterion with transported projectors,

\[
P_r^{\rm out}F=F P_r^{\rm in}.
\]

For the submitted `E`, define

\[
Q_r=E P_r E^\dagger.
\]

Then, for both record values,

\[
Q_rE=EP_r.
\]

Indeed `Q_0=P_1`, `Q_1=P_0`, `E^\dagger E=I_4`, and

\[
(EV_0)^\dagger(EV_1)=V_0^\dagger V_1=0.
\]

The map neither merges the alternatives nor destroys their readability; it
only swaps the carried sector names.  Under the candidate's own functorial
record-transport definition this is a required non-kill.  Thus H4's published
`killed=true`, `STABILITY-FAILS-CHANGED-GRAMMAR`, and the downstream
`all_registered_attacks_killed=true` are scientifically false.  Repair would
require a different mathematical object that genuinely removes the semantic
record algebra, not a wording or serialization edit.  That excludes
`ACCEPT-WITH-FIXES` under the frozen protocol.

The exact invalid promotion slice is:

```text
E = X tensor I
  -> fixed P_0 commutation is false
  -> eraser_outside_grammar = true
  -> H4 killed = true
  -> all_registered_attacks_killed = true
  -> ELIGIBLE-GREEN-UNREVIEWED
```

The first arrow does not establish erasure because it omits the licensed
output transport `Q_r=E P_r E^dagger`.  No earlier registered attack survives.

## 2. Authentication, blindness, and reconstruction order

`HEAD` authenticated as
`ed258111d2ff604de97816266be2184fd1d06c63`.  The binding commit objects named
by the protocol exist.  I read the protocol, pin, paper, construction note,
fresh controls, official result, receipt, and verification note completely.
I did not inspect or communicate with either other review seat and did not
inspect any other hostile report.

| immutable object | lines / bytes | independently observed ordinary SHA-256 |
|---|---:|---|
| hostile protocol | 299 / 14,376 | `7eba533fea4bb96370ed27aa46f9f6c933b207317495d9a4955c7868f89f5fed` |
| result-neutral pin | 638 / 26,766 | `0dc92112e5db39bb9e1a8c51a018119e783f347505d3e5bf03debf47fe31ef44` |
| source | 1,411 / 56,229 | `1a1d9a7acc3ef4ba62a9e9b0f6101263dde3b72dd9d407918ea0be653d5d628e` |
| paper | 1,748 / 62,489 | `ffc3dca2863bf9f36c9fe62e8dff80628c59c8837b3d96006e449329dee05ec1` |
| construction note | 186 / 7,052 | `e6d59fd49e5af805df96f8b3a4c2db5676dafaa3c552ecadb0779ca690887253` |
| fresh cases | 61 / 1,535 | `4f5d8d21bb66d5e7c41a9c34a35a26ec955b03497d9682564efd23df681126c7` |
| official output | 1 / 26,103 | `95a38ebbb6d2e9c85c2a2f66ca3275fd1f4205761dfcc5eae6a1d9ea2b233993` |
| official receipt | 1 / 29,695 | `2d320edc0eb152d5fcb6ffdf1444e8071d9466c5773c13be51ad438036c2fa4c` |
| verification note | 155 / 6,476 | `c8aec2827778a0f31645a374eebfa03c82563da9a7395ef6b5af708c1ee9ae42` |

Before source inspection I froze a standard-library-only clean-room program.
It does not import or execute candidate code.

| private clean-room evidence | SHA-256 |
|---|---|
| `/private/tmp/p14_seat_p_cleanroom.py` | `0999f7860a01f634ee79f289c5ad6e4c2739d4ac4f5df26f791de92e0469983c` |
| clean-room canonical payload | `3ed8b4edde5a7361f3169e333e91180557bf75b810d5c35e600e29a34bc8e436` |
| clean-room stdout | `00b63a00cf064300f63b9a2222dd3e9f6e7564d0387bc615f9df52e79c2ed25b` |

After source inspection I froze a separate no-import artifact/attack audit.

| private post-source evidence | SHA-256 |
|---|---|
| `/private/tmp/p14_seat_p_artifact_audit.py` | `1bb9a355790b1da493aaca6db0b9d03b461e74d199631a3874f7b0dcb75097f0` |
| its canonical stdout | `8c773586b70186eee0701860dea0ddf76bff4777fde2c455f13755237e2eca7e` |

## 3. Exact clean-room mathematics

### 3.1 Writer and sealed grammar

The independently reconstructed matrices are

\[
R=\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix},\qquad
B=|R|^2=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\]

For the two writer branches, all four `P_r V_s` rows give
`delta_rs V_s`, and

\[
V_0^\dagger V_0+V_1^\dagger V_1=I_2.
\]

Every submitted sealed generator `I_2 tensor R^k`, `k=0,...,5`, commutes with
the common record projectors and is an isometry.  Therefore the common typed
projector at each word seam exists.  Straight induction, rather than the
finite table, gives for every finite word `U`

\[
P_rU=UP_r,
\qquad
P_rUV_s=\delta_{rs}UV_s.
\]

This positive theorem survives H4.  H4 fails because its extra map also has a
valid transported projector family, not because any sealed generator fails.

### 3.2 Native nondivision is not state unreality

The unrecorded two-step reconstruction gives

\[
R^2=\frac1{25}\begin{pmatrix}-7&-24\\24&-7\end{pmatrix},\qquad
C=|R^2|^2=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix}.
\]

Since `B` is invertible, the only source-independent restart candidate on the
declared two-state carrier is

\[
K=CB^{-1}=\frac1{175}
\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
\]

It satisfies `KB=C` and its columns sum to one, but it is not nonnegative.
Hence this native cut is nondivisible.  The conclusion is only the absence of
a nonnegative restart kernel on this carrier.  It does not say that an actual
intermediate configuration is unreal or ontologically incomplete.  Adding a
whole-history hash, phase, or enlarged carrier can yield a Markov
representation, but that is a changed source type and is a non-kill for the
native result.

With orthogonal records, the distinct law is

\[
B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix},
\]

which factorizes stochastically.  This preserves the required distinction
between native nondivision and a record-induced change of division structure.

### 3.3 Reciprocal law and complete frontiers

I enumerated, rather than accepted, all histories of

\[
\Gamma(a,b,g,y)=\frac14 B_{g\mid a\oplus b}B_{y\mid g}.
\]

There are 16 positive histories; their probability values are exactly
`81/2500`, `36/625`, and `64/625`, and their total is one.

For the full `(a,b)` cut I reconstructed all 16 conditional rows indexed by
four inputs and four `(g,y)` targets.  Every row is positive, each input row
normalizes to one, every history crosses exactly once, and

\[
\Pr(g,y\mid a,b)=B_{g\mid a\oplus b}B_{y\mid g}.
\]

For the full `(a,b,g)` cut I reconstructed all 16 rows indexed by eight inputs
and two `y` targets.  Again every history crosses exactly once, each input
normalizes, and

\[
\Pr(y\mid a,b,g)=B_{y\mid g}.
\]

The fixed-stage cylinder cells are disjoint and exhaustive in both cases.
The exposed tuples include every declared law-relevant degree at their
respective stages, carried records persist, and the factorization quantifies
over the entire finite future algebra, not only printed marginal rows.  Thus
both full cuts are complete division frontiers for the declared grammar.

The projected `a` cut remains stable but incomplete.  At fixed `a`, the two
positive hidden `b` pasts give

| `(a,b)` | `Pr(g=1 | a,b)` |
|---|---:|
| `(0,0)` | `16/25` |
| `(0,1)` | `9/25` |
| `(1,0)` | `9/25` |
| `(1,1)` | `16/25` |

This is failure of future sufficiency caused by an omitted law-relevant
degree.  It is not the same statement as the negative native kernel above.

The four published parity/output cut rows reconstruct exactly as
`337/625`, `288/625`, `288/625`, `337/625`.  The response rows are

```text
Pr(g=1 | parity=0,1) = 16/25, 9/25
Pr(y=1 | g=0,1)      = 16/25, 9/25
Pr(y=1 | parity=0,1) = 288/625, 337/625
```

and the residuals are `7/25`, `7/25`, and `49/625`.

### 3.4 Stable/frontier independence and probability weights

The four models `(stable,complete)`, `(stable,incomplete)`,
`(nonstable,complete)`, and `(nonstable,incomplete)` are all realized.  A
persistent record changes only the stable coordinate; whether hidden `U`
controls the future changes only sufficiency.

The correlated-antichain law

```text
P(00),P(01),P(10),P(11) = 2/5, 1/10, 1/5, 3/10
```

has `P(A0)=1/2`, `P(B0)=3/5`,
`P(B0|A0)=4/5`, and `P(A0|B0)=2/3`.  Both weak path products equal `2/5`,
but the local factors move; only whole-history surprisal descends.

For the screened fork, all eight typed strong-diamond rows pass.  The joint
law normalizes to one, its child covariance is `1/45`, and the example branch
has probability `3/20` with formal reciprocal atoms `3`, `4/3`, and `5/3`.
This is the required positive unequal-weight control.

### 3.5 Histories, bundles, and uniform family

The minimal frame has five reachable states, seven legal words, and five
trace histories.  The mutual-dependence classes are
`({a,b},{c},{d})`, with quotient edges `{a,b}<{d}` and `{c}<{d}`.

I reconstructed all 12 rooted-tree shape-count rows and all 38 finite family
rows.  For every tested shape of `n=1,...,4` cells and `q=1,2,3`, both seed
values normalize exactly and give `4n` bundles, `5n` record components, and
`16^n` positive histories.  The shape counts by `(q,n)` are

```text
q=1: 1,1,1,1
q=2: 1,1,2,3
q=3: 1,1,2,4
```

Reverse-leaf normalization proves the all-finite-shape statement.  Finite
branching plus strict dependency-depth increase proves finite closed
intervals in the direct limit.  Depth is a proof coordinate, not a physical
clock.

## 4. Common claim matrix C1--C14

The statuses below grade the mathematical claim at its stated scope.
Mandatory-control and promotion-integrity failures are separately recorded in
Sections 5 and 8.

| ID | status | exact evidence |
|---|---|---|
| C1 | PASS | Both inputs and both writer branches give completeness `I_2` and all four exact sector equations. |
| C2 | PASS | All six sealed generators share the same typed projectors; induction covers arbitrary finite words.  This does not validate the submitted H4 object. |
| C3 | PASS | Complete incidence/law/support/provenance identity removes label clones and neutral refinements while preserving occurrence multiplicity. |
| C4 | PASS | `Gamma` supplies possible histories; external `rho` alone selects actuality; stability is an all-continuation record property. |
| C5 | PASS | Independent reconstruction gives 16 full-`ab` and 16 full-`abg` rows, positivity, per-input normalization, disjoint/exhaustive/exactly-once cells, all-future sufficiency, and cut equality.  Projected `a` refuses. |
| C6 | PASS | All four stable/nonstable by complete/incomplete combinations are explicit. |
| C7 | PASS | `UC` and `CU` reach the same complete state and trace; dependency comes from record entailment/influence, not serialization. |
| C8 | PASS | The SCC quotient is a poset; finite branching and depth bound every uniform-family interval. |
| C9 | PASS | Unit measure counts physical bundle occurrences, not labels or automorphism orbits; clone and two-node controls preserve the distinction. |
| C10 | PASS | The correlated antichain refuses local descent; the positive screened fork passes every typed strong diamond with positive normalized factors. |
| C11 | PASS | Fresh sectors give `16^n` distinguishable stable histories.  Any fixed finite carrier collides for large `n`; two cells already require 256 histories. |
| C12 | PASS | Matter parity changes `g` by `7/25`; `g` changes `y` by `7/25`; integrated parity-to-`y` response is `49/625`, all pregeometric. |
| C13 | PASS | Every accepted law-relative statement is scoped to `DECLARED-NEW-LAW-POSTULATE`; no Paper 13 law is imported. |
| C14 | PASS | No chronology, dimension, volume calibration, topology, metric, curvature, gravity, GR, continuum, or QFT is promoted. |

## 5. Registered hostile controls H1--H26

I rebuilt the changed mathematical objects and all 52 old/new object hashes;
all old/new pairs differ exactly as sealed.  Hash agreement did not determine
the semantic dispositions below.

| ID | semantic result | disposition |
|---|---|---|
| H1 | PASS | Label clone has one physical occurrence before and after; measure remains one. |
| H2 | PASS | A neutral intermediate arrow exposes no record; onset count remains one. |
| H3 | PASS required non-kill | `UC` and `CU` are one trace, state, law, and measure. |
| H4 | **FAIL — survivor** | `E=X tensor I` is bijective and satisfies `Q_r E=E P_r` for `Q_r=E P_r E^dagger`; it is a sector swap, not an eraser. |
| H5 | PASS | Stable `a` survives while hidden `b` changes the `g=1` profile `16/25 <-> 9/25`; frontier refuses only. |
| H6 | PASS | Corrupting cached `3` to `4` does not move the recomputed three bundles. |
| H7 | PASS | Two cells have 256 positive stable histories, exceeding the declared eight-state dormant carrier. |
| H8 | PASS | Replacing the formal atom for `9/25` by the atom for `16/25` at fixed `Gamma` fails intrinsic descent. |
| H9 | PASS | Uniform and correlated positive laws can share the two-node antichain; order stays fixed while valuation moves. |
| H10 | PASS | A two-node chain and antichain both have unit count two but distinct order. |
| H11 | PASS | An exhaustive candidate cut with crossing multiplicity two fails exactly once and therefore is not complete. |
| H12 | PASS | Coverage `3/4` omits positive mass `1/4`; exhaustiveness fails independently. |
| H13 | PASS | Both weak products are `2/5`, but strong factors move; only contextual history weight survives. |
| H14 | PASS | A countably infinite chain inserted between fixed endpoints makes that closed interval infinite. |
| H15 | PASS | Record events on untransported boundaries have no typed common product. |
| H16 | PASS | A proposed edge with neither event entailment nor calibrated influence is refused. |
| H17 | PASS required scope control | Appending a whole-past hash changes the carrier and may Markovize it; the native projected cut remains incomplete. |
| H18 | PASS | Added coordinates leave the intrinsic antichain unchanged and are quarantined. |
| H19 | PASS | Symmetric co-creation yields two record components in one mutual-dependence bundle, with no orientation. |
| H20 | PASS | Exchanging two anonymous nodes does not reduce two physical occurrences to one automorphism orbit. |
| H21 | PASS | Weak product equality cannot promote context-dependent local factors to intrinsic atoms. |
| H22 | PASS positive control | Conditioning on the typed root screens both children; all eight strong rows pass and covariance remains `1/45`. |
| H23 | PASS | Reusable fixed slots collide with the unbounded `16^n` stable-history census. |
| H24 | PASS required non-kill | Sibling relabeling/reordering has identical canonical physical structure and law. |
| H25 | PASS | The exact four-product table refutes `stable implies division`. |
| H26 | PASS | Opposite serializations of an incomparable pair share one trace; derived depth cannot become global time. |

Because H4 survives semantically, the printed count `26/26` is not a valid
scientific count even though every row carries a distinct changed-object hash.

## 6. Shared new controls N1--N12

| ID | independently constructed object and exact output |
|---|---|
| N1 | Duplicate one complete onset row with identical support, provenance, record, and full future profile: one happening class and unit measure `1 -> 1`. |
| N2 | Hold stable `a` fixed and vary hidden `b`: future profiles are `16/25` and `9/25`; stability remains true and frontier completeness false. |
| N3 | Co-create three swap-symmetric persistent facts with mutual edges: SCC `{a,b,c}`, three record components, one bundle, no admissible orientation. |
| N4 | Factor one onset through a neutral intermediate boundary with zero record increment: happening count remains one. |
| N5 | Independent fair bits `A,B` under orders `AB` and `BA`: four histories each of weight `1/4`, one physical trace law, unit measure two. |
| N6 | Four local histories over four cells require `4^4=256` stable histories; a 100-state dormant carrier collides. |
| N7 | One positive path meets the same exhaustive frontier at two stages: coverage is one but crossing count is two, so the frontier refuses. |
| N8 | Two-node chain versus two-node antichain: both valuations are two, while only the chain has one strict relation. |
| N9 | Hold the antichain fixed and change the law from four `1/4` rows to `(2/5,1/10,1/5,3/10)`: unit measure stays two and law valuation moves. |
| N10 | Correlated antichain: `(1/2)(4/5)=(3/5)(2/3)=2/5`, but both local factors move; atomic descent refuses. |
| N11 | Typed common-cause fork: all eight screening equalities pass; covariance `1/45` does not obstruct descended conditional weights. |
| N12 | Add rank/list coordinates to an intrinsic antichain: intrinsic relation remains empty; the added orientation is nonphysical. |

## 7. Five additional Seat-P controls

These controls were not copied from the registered or fresh tables.  PNEW1--4
attack the primary probability/stability/frontier lens; PNEW5 is a required
non-kill.

### PNEW1 — intermediate-projector seam

Let `P=diag(1,0)`, `P'=diag(0,1)`, `F1=I`, `F2=X`, and choose output `P`.
Then

```text
P F1 = F1 P                       true
P F2 = F2 P'                      true
P = P'                            false
P (F2 F1) = (F2 F1) P             false
```

Two isolated one-generator checks do not imply the word theorem if they use
incompatible projectors at their shared boundary.  The candidate's sealed six
generators pass this control because they use one common typed projector
family at every seam.

### PNEW2 — all-future-event sufficiency trap

Two positive pasts share one exposed state.  After the first past, `(Y,Z)` is
`00` or `11`, each with probability `1/2`; after the second, it is `01` or
`10`, each with probability `1/2`.  The `Y` and `Z` one-coordinate marginals
are both fair for both pasts, but

```text
Pr(Y=Z | past 0) = 1
Pr(Y=Z | past 1) = 0
```

Marginal tests therefore pass while future sufficiency fails.  The paper's
quantification over the complete future-event algebra correctly refuses this
frontier.

### PNEW3 — aggregate cut-cancellation trap

Take the direct per-input rows `(3/4,1/4)` and `(1/4,3/4)`, but use fake cut
rows `(1/2,1/2)` for both inputs.  Under a fair input mixture, direct and cut
both give `(1/2,1/2)`, while equality fails on each input.  This proves that
aggregate equality cannot replace the candidate's all-input gate.

### PNEW4 — signed-kernel equality trap

Let both columns of `B_u` equal `(1/2,1/2)` and

\[
K_s=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

The columns of `K_s` sum to one and `K_s B_u=B_u`, but `K_s` has negative
entries.  Thus equality and normalization do not imply positivity.  This is
the same logical separation used by the native `CB^{-1}` refusal.

### PNEW5 — sufficient-state refinement non-kill

Let a neutral past bit `U` be independent of a fair future bit `Y`, with no
carried `U` record.  A coarse one-state cut and its disjoint refinement into
`U=0,1` cells are both exhaustive, exactly once, and give
`Pr(Y=1)=1/2` in every cell.  Both are complete for this declared grammar.
Completeness is a sufficiency property, not a demand for one unique minimal
serialization.

The private audit output seals these five controls and the H4 matrices under
SHA-256 `8c773586b70186eee0701860dea0ddf76bff4777fde2c455f13755237e2eca7e`.

## 8. Fresh controls, result, receipt, and process integrity

### 8.1 Six fresh controls

All six cases were recomputed directly from the raw parameters.

| case | exact result | canonical case SHA-256 |
|---|---|---|
| frontier profiles `2/7,5/7` | two profiles; incomplete | `41a026a03daf15d3f1d646a744d1984dda7926cd6e254683a531872ae874f42b` |
| correlated joint `1,2,3,4 / 10` | weak products `1/10`; strong false | `68416a2ef022a34bb336dd09b3087a174d1daa3ef87b5745b764db1c80a46937` |
| screened fork | eight positive histories; strong true | `f2cda22e66d882fafdd52226f37524a482a275c260a95a56bc9a7806abedaff3` |
| fixed memory `100,4,4` | `4^4=256>100` | `569e97d829512537ad3a884cbc9cc10be36a9c2504766ee56c716bc8e5b18738` |
| presentation permutation | raw unequal, canonical equal | `eaf39b41c5b3b4485cd2744aaaa51bb0568d30ad80a1e320713877f5790da0d5` |
| dependency bundle | SCCs `{u,v}`, `{w}`, `{z}` | `ade5c35eb09bf61d36750ec61ef9b27c43eae4f6a83a2e0e063c37bbb0f6e8dd` |

### 8.2 Independent receipt reconstruction

The official JSON files are canonical JSON plus one LF.  Removing only the
output's `normalized_payload_sha256` field gives

```text
292b9c9dad12785cdb0b233a7d56237500fd716e38b740ad3772a1f6969e8ecf
```

The receipt core, after removing only `receipt_core_seals` and
`receipt_core_sha256`, gives

```text
0d71fd0eed5a2fe399fc7b6f9321c46c91b06e03c68f878dd626407175937914
```

All five input hashes, the output's 26,103 bytes and ordinary hash, all 17
top-level scientific seals, all nine receipt-core seals, both ledgers, and the
six fresh-case hashes reconstruct.  The measurement, attack, and fresh-result
aggregate seals are respectively

```text
962340352d502c8e5a8056c57dcb7df559543cef5741607b8863beb3c802d2f0
fd593caf97a61e3ee4572295dccd25e72c15eed13c08f87eed4819bf9c2ad23f
c47fc41ee44b1434e2e51d2b936863b7091e77eecd81012294f079bcd6e24abd
```

Seal integrity therefore does not cure H4: it faithfully seals the false
fixed-projector inference.

There is also a bounded but promotive receipt-evidence shortfall.  The
published `DIRECT-CUT-EQUALITY` boolean consumes only four parity/`y`
marginals.  The receipt does not contain the 16 full-`ab` joint-future rows,
the 16 full-`abg` rows, or positive disjoint/exhaustive/exactly-once crossing
objects, and it omits the `R^2,C,CB^{-1}` native-nondivision object entirely.
Those mathematical claims are true by the independent reconstructions above,
but the official receipt does not bind all objects demanded by its frozen
promotion contract.

### 8.3 CLI, determinism, runtime, memory, and transactionality

| run | exit / elapsed | stdout result |
|---|---:|---|
| repository-root `--selftest` | 0 / 12.045 s | 24,299 bytes; SHA `36bda0de588ce4ffdd37b549b581a1b436466f4351e6ddd5714c857a789110d2` |
| alien-CWD `--selftest` | 0 / 15.181 s | byte-identical |
| true one-file, no-`.git` `--selftest` | 0 / 15.028 s | byte-identical |
| separate memory sample | 0 / 9.222 s | maximum RSS 24,985,600 bytes; same stdout SHA |
| named H22 changed-object mode | 0 / 12.321 s | exact screened-fork attack row |
| deliberate anchor failure | 1 / immediate | only `SCIENTIFIC-FAILURE: DELIBERATE-ANCHOR-FAILURE` |
| unknown changed-object ID | 2 | strict parser refusal |

A private copied-corpus publication run completed in 15.717 seconds and
reproduced the committed output and receipt byte for byte.  A second run
refused existing destinations before writing.  An outside-whitelist run
failed before either destination existed.  The source-only directory
contained exactly the copied source file.  All complete runs ended before the
30-second progress threshold.  The source has 1,267 nonblank lines, imports
only the standard library, and contains no float literal, randomness, network,
Git, or Paper 13 dependency.

## 9. Product-valued outcome and scope

The H4 failure is confined scientifically but fatal procedurally to the
submitted global green outcome:

| coordinate | Seat-P determination |
|---|---|
| law | `P14-DECLARED-POINT-FREE-HISTORY-LAW` reconstructs; it remains a postulate, not a derived or selected law. |
| stable-record theorem | Every finite word of the sealed six-generator grammar preserves both record sectors. |
| stable-happening promotion | **Capped at `P14-ONSET-GERMS-PRESENTATION-ONLY` in this submission**, because the mandatory eraser discriminator H4 is a survivor. |
| full `(a,b)` frontier | `P14-COMPLETE-DIVISION-FRONTIER`. |
| full `(a,b,g)` frontier | `P14-COMPLETE-DIVISION-FRONTIER`. |
| projected `a` frontier | `P14-FRONTIER-INCOMPLETE`; stable record is not a sufficient state. |
| unrecorded coherent intermediate cut | Native nondivision: no nonnegative source-independent kernel on the declared carrier. |
| history/carrier enlargement | Changed-carrier non-kill only; it does not alter the native verdict. |
| valuation/order | Independently reconstructed finite results remain intact; this seat makes no cross-seat promotion. |
| geometric ceiling | Not eligible for the submitted global green outcome because `all_registered_attacks_killed` is false.  No metric claim is earned in any event. |

The paper correctly separates its new “stable happening” ontology from
Barandes's stochastic framework.  The primary source defines indivisible
laws on a configuration space and uses division events as conditioning
locations; it does not define them as spacetime atoms or define this paper's
happenings.  See Barandes,
[“Quantum Systems as Indivisible Stochastic Processes”](https://arxiv.org/abs/2507.21192).

Permanent walls remain exact: `rho` is an external actualization postulate;
law selection, chronology, dimension, topology, scale, metric, curvature,
stress-energy, gravity, continuum, GR, and QFT are unconstructed.

## 10. Final verdict

**REJECT.**  First counterexample: H4.  The exact submitted “eraser” is a
transported record-sector permutation, so the semantic attack survives even
though the sealed-word theorem and the separately evaluated frontier and
native-nondivision coordinates remain mathematically valid.
