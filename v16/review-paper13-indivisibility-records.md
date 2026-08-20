# Paper 13 hostile review — Seat I

**Seat:** I — stochastic indivisibility, division, records, and Barandes scope
**Review interval:** 2026-08-20T00:28Z–2026-08-20T01:06Z
**Authenticated repository HEAD:** `73dd8326a20abe802cec021e5d1f7e7c6cb03332`
**Authenticated candidate commit object:** `317f3b58627a06539a470509b07259aebe15be7f`
**Verdict:** no scientific kill; eligible-cap rung survives with exact scope controls

## 1. Seat identity and mutual blindness

I performed the Seat I audit independently. Mutual blindness was preserved
throughout: I did not access, enumerate, request, receive, or infer any other
current reviewer's report or scratch work, and I did not communicate scientific
results to another reviewer. All scratch work was private and off-tree at
`/private/tmp/p13-seat-i.RUvdJO`. I edited no repository path except this report.
I did not import or call any scientific function from the frozen evaluator; it
was used only as a subprocess and later inspected as source.

The first decisive scientific counterexample is **none**. The native
nondivision calculation, lawful record division, and their required scope
controls all survive independent exact reconstruction.

## 2. Complete read/open ledger

All times are UTC. A byte-authentication read is distinguished from a
scientific content read. Historical files in the manifest were authentication
anchors only and supplied no scientific conclusion.

### 2.1 Gate authentication

| Time | Path/object | Role | Authentication result |
|---|---|---|---|
| 2026-08-20T00:28Z | `HEAD` | dispatch identity | exact `73dd8326a20abe802cec021e5d1f7e7c6cb03332` |
| 2026-08-20T00:28Z | commit object `317f3b58627a06539a470509b07259aebe15be7f` | candidate object | present |
| 2026-08-20T00:28Z, complete; 2026-08-20T00:58Z, schema recheck | `v16/note-paper13-hostile-review-protocol.md` | frozen review protocol | ordinary `1914ef55118c8261f55d271a7431cf5bc7e5aa90689d39f4b927e6c39fe8bd58`; normalized `a425fb70a6e0b2b93a02558e32557ab4d92e1e4b1bcf58384a446492b1e985d9` |
| 2026-08-20T00:29Z; 2026-08-20T00:58Z recheck | `v16/paper13_code/manifest.json` | manifest | ordinary `373406f606ed495baffed160d233ef65d56cec96ba6423bac95b8e72ddcd3430`; independently canonicalized payload `2c748cdf7437f4b18a9b9a6c7964d0f7fc3061dfc5ceb885083d3a325736660a` |

The manifest closure was opened for byte authentication at
2026-08-20T00:29Z–00:30Z. Every size and ordinary SHA-256 matched:

| Path | Manifest role | Size | SHA-256 | Content use |
|---|---|---:|---|---|
| `RUNBOOK.md` | paper-and-integrity-rules | 119844 | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` | authentication only |
| `v16/note-apr-one-gamma-paper-review-gate.md` | methodology-and-ontology-gate | 23123 | `06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51` | complete contract read after black-box replay |
| `v16/paper-12-atomless-regions-and-the-missing-gluing-law.md` | predecessor-negative-and-scope-anchor | 19039 | `56cddeacbfe477d1af244b310e9a26b5622ef540b82deea5a96158819ba972f7` | authentication only |
| `v16/note-apr-paper12-final-adjudication.md` | predecessor-disposition-anchor | 13669 | `5ef1440064b703bd04bf97f1774f7f5e03efe537aeee2669bd1471f0a402799e` | authentication only |
| `v16/code/apr_paper12_exact.py` | predecessor-authentication-only-source | 50150 | `c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7` | authentication only |
| `v16/code/apr_paper12_receipt.json` | predecessor-authentication-only-receipt | 24687 | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` | authentication only |
| `v16/note-paper13-one-gamma-construction-pin.md` | result-neutral-construction-contract | 37592 | `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35` | complete contract read after black-box replay |
| `v16/note-paper13-stageA-support-split-forward-repair-pin.md` | support-split-forward-repair-contract | 16297 | `8ae54ada2a97f347a18b90adcab86dcb2e7c18c04c748cc5e0779b8251449a36` | complete contract read after black-box replay |
| `v16/note-paper13-gamma-source-freeze.md` | historical-source-freeze-authentication-only | 6802 | `d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5` | authentication only |
| `v16/review-paper13-stageA-source-physics.md` | historical-source-audit-authentication-only | 3649 | `20a054cd6542fd02f556b461408f48d75ead0c69ec06abd76c9eed3ce3c3d352` | authentication only; no conclusion read |
| `v16/review-paper13-stageA-source-records.md` | historical-records-audit-authentication-only | 3622 | `7c5b14a04f938de05b64750f6c8ae454eb4bbe8d0824e9eaaa0016532ab52ed4` | authentication only; no conclusion read |
| `v16/note-paper13-stageA-source-audit-adjudication.md` | historical-source-audit-adjudication-anchor | 5258 | `bd089458ef1d4c4fe8f9dc13fc21134695aba552b95b20f023e4d2f9f34dfb74` | authentication only |
| `v16/code/p13_gamma_exact.py` | frozen-master-evaluator | 389487 | `3da3161c7eef63b90da9c6cb85f7bc918d6e5c99fa431f07d273efd1f18e519e` | source inspection only after reconstruction freeze |
| `v16/code/p13_gamma_fresh_cases.json` | nonce-bound-fresh-input | 2406 | `2ac664c94a6b29c5b73fd8047e97a2e086ac45defc9c3431bc1ded66f011dd29` | serialized primitives after black-box replay |
| `v16/code/p13_gamma_output.txt` | official-construction-output | 6632 | `7f544c79f60d91c84e5805541313ec9d7ac068cdf0ee4f6184947cf44f43886f` | comparison target after reconstruction |
| `v16/code/p13_gamma_receipt.json` | official-machine-reconstructible-receipt | 43360610 | `83bd33028c81e9dd555a44e9e7721d5ace298d522e0c069409118bdbf51c6c48` | lineage audit only after reconstruction freeze |
| `v16/note-paper13-gamma-verification.md` | independent-no-import-verification | 6779 | `faf508650c8d5f4c8691b334ea8877505ac49f2c26cdcc526bc3e309179295b8` | authentication only; conclusion not evidence |
| `v16/paper-13-one-relational-gamma.md` | result-known-paper-candidate | 23473 | `db2f9f9a84f423bd8d23429ce567bc2e9236ea8deb3076f113c6aa692bd32446` | complete claim read after black-box replay |
| `v16/paper13_code/run_all.py` | master-authentication-and-replay-runner | 18626 | `b99a458f76c90be19e396b5f332db8219298e8d3f875cb97328f89aa83d595a4` | source inspection after black-box replay |
| `v16/paper13_code/receipts_table.json` | paper-number-and-claim-lineage-table | 10193 | `60430a794a87d8478f69205e97d637eb9751c21a53da1959f0b3e9155b7d8206` | claim-lineage audit after reconstruction |
| `v16/paper13_code/RUN.txt` | clean-and-off-tree-regeneration-instructions | 2559 | `9296b317bdfe468d31ad7025ce807534a5ff9ae6a142cea4a8b9e6714188ff47` | replay instructions |

### 2.2 Scientific and audit content reads

| Time | Paths | Purpose |
|---|---|---|
| 2026-08-20T00:39Z–00:43Z | ONE-GAMMA gate, both Paper 13 construction pins, candidate paper, fresh JSON | reconstruct primitive packet and claims without implementation access |
| 2026-08-20T00:45Z–00:47Z | runner and evaluator sources | post-freeze AST, CLI, publication, and scientific-lineage audit |
| 2026-08-20T00:47Z–00:51Z | official output, receipt, receipts table | compare independent results; recompute seals, reads, claims, registry, and mutations |
| 2026-08-20T00:58Z–01:06Z | protocol schema, manifest, receipts table, candidate nondivision/reference spans | report-only completeness recheck |

Primary-source attribution reads were made at 2026-08-20T00:52Z–00:54Z:

| Source | Stable locator | Exact implication checked |
|---|---|---|
| Jacob A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,” arXiv:2507.21192v1 (2025) | <https://doi.org/10.48550/arXiv.2507.21192> and <https://arxiv.org/html/2507.21192v1> | the primary paper uses a given configuration space, permits division events/conditioning only at selected times, allows pseudo-stochastic intermediate factors with negative entries, and treats Hilbert-space machinery as secondary representation |
| Rafael D. Sorkin, “Quantum Mechanics as Quantum Measure Theory,” *Modern Physics Letters A* **9** (1994), 3119–3128 | <https://doi.org/10.1142/S021773239400294X> and <https://arxiv.org/abs/gr-qc/9401003> | histories/quantum-measure theory is broader context for quadratic amplitude-to-measure rules; it does not supply this candidate's finite law |

The candidate's attributions are accurate and restrained. It explicitly says
that its changing catalogue differs from Barandes's fixed-configuration
starting point, does not inherit Barandes's physical adequacy, calls endpoint
squaring a postulate, and calls its finite rule its own construction. Neither
source supplies ISP support change, division grammar, locality, actualization,
or the numerical law.

### 2.3 Private evidence ledger

| Time | Private path | Role | SHA-256 |
|---|---|---|---|
| 2026-08-20T00:30:51Z | `.../selftest.out` | runner selftest output | `4c24dc0c60cfcb6dafb6ebb7a82713c759dccdbb98a02c7114e6fb197740bbac` |
| 2026-08-20T00:32:53Z | `.../root-replay.out` | root replay output | `3663a0e8b31f1fe979afc0e6d0a5a91d6816c1624311305ae7f1fd9966dc2a0e` |
| 2026-08-20T00:35:24Z | `.../alien-replay.out` | alien-CWD replay output | `3663a0e8b31f1fe979afc0e6d0a5a91d6816c1624311305ae7f1fd9966dc2a0e` |
| 2026-08-20T00:38:28Z | `.../offtree-replay.out` | source-only/no-Git replay output | `3663a0e8b31f1fe979afc0e6d0a5a91d6816c1624311305ae7f1fd9966dc2a0e` |
| 2026-08-20T00:43:42Z | `.../seat_i_reconstruct.py` | independently written exact reconstruction, frozen before evaluator inspection | `026c03041b1e6db6e9fdbe85309018327bc23688cdbc03b26e120b0f0033de40` |
| 2026-08-20T00:44:00Z | `.../reconstruction.out` | canonical independent result | `25b3244bd26bd8b62f35f05cc569eb0e76fb8b879c81ef7a2be7619caf068fa6` |
| 2026-08-20T00:44:53Z | `.../evaluator-selftest.out` | evaluator black-box selftest | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1` |
| 2026-08-20T00:45:49Z | `.../generate-fresh.out` | absent-destination generation | `12c52df7bb27fe103c01ed96ab32796ff650efd48d8a9421aa698fd6771b75f1` |
| 2026-08-20T00:50:25Z | `.../receipt_audit.py` | independently written receipt/seal audit | `ac76a643fee42d0857728d3f3d410e5b99d22444aacd713acbdc1f516227b17d` |
| 2026-08-20T00:50:41Z | `.../receipt-audit.out` | receipt/seal audit result | `fd390311c0f380aa66a798298aa31333d7ce4a4430e5891986ab9345eb931f28` |
| 2026-08-20T00:51:00Z | `.../ast-audit.out` | independent AST inventory | `f42810fcfec7f3c06c9db511b74e8e9178b0921363a6f3b6f086e99a7e06ae8e` |
| 2026-08-20T00:48Z–00:49Z | `.../mutants-i/*.json` | twenty assigned mutation outputs, individually named in Section 8 | canonical path/hash-index `27dfe4bd0053739b428aa5787386578cce11b2b3902ad372eba1ecf5f17e7e41` |
| 2026-08-20T00:45Z–00:46Z | nine strict-CLI/no-overwrite/rollback stderr files | negative-path evidence | canonical path/hash-index `8ac646faca1dcf84c3811307ebfd0e5834bea949b139f88fa986b1e0c5e38a15` |

## 3. Replay commands, return codes, runtimes, and hashes

| Mode/command | CWD | RC | Runtime | Output SHA-256/result |
|---|---|---:|---:|---|
| `python3 v16/paper13_code/run_all.py --selftest` | repository root | 0 | 1.09 s | `4c24dc0c60cfcb6dafb6ebb7a82713c759dccdbb98a02c7114e6fb197740bbac`; 21 files, 12 claims, 29 bindings, 164 numeric tokens, Results A–G in order, deliberate self-anchor failure |
| `python3 v16/paper13_code/run_all.py` | repository root | 0 | 110.68 s | `3663a0e8b31f1fe979afc0e6d0a5a91d6816c1624311305ae7f1fd9966dc2a0e`; fresh/output/receipt byte-equal, temporary destinations removed |
| `python3 /Users/felixrobles/workspace/isp/v16/paper13_code/run_all.py` | `/private/tmp` | 0 | 135.13 s | same canonical replay hash, byte-identical to root |
| `python3 v16/paper13_code/run_all.py` in manifest-closure copy | `/private/tmp/p13-seat-i.RUvdJO/offtree`, no `.git` | 0 | 156.81 s | same canonical replay hash, byte-identical to root |
| `python3 v16/code/p13_gamma_exact.py --selftest` | repository root | 0 | 27.84 s | `8ce3c4afbf1cb99be5f5408155af9a3123a6cdf485a8221248b5f31ec893d3e1`; 42 checks and all 92 mutation names pass their independently checked change/failure predicates |
| strict evaluator unknown, missing, duplicate, incompatible, and relative-path forms | repository root/private scratch | 2 each | <0.2 s each | refused; no destination published |
| `python3 v16/paper13_code/run_all.py --bogus` | repository root | 2 | <0.2 s | argparse refusal; stderr SHA `6889300cbbcc4dedf8590ef836cddaea1c245f77424bb7082aa218e13b360a7d` |
| evaluator `--generate-fresh --nonce ... --source-sha ... --fresh-out /abs/.../p13_gamma_fresh_cases.json` | repository root | 0 | 0.15 s | output SHA `12c52df7bb27fe103c01ed96ab32796ff650efd48d8a9421aa698fd6771b75f1`; generated bytes SHA `2ac664c94a6b29c5b73fd8047e97a2e086ac45defc9c3431bc1ded66f011dd29` |
| same generation with wrong basename | repository root | 2 | <0.2 s | refused, destination absent |
| generation with existing destination | repository root | 2 | <0.2 s | destination unchanged; stderr SHA `137f5d72a44d85fdd47c8146b03fccae295dcd9f78931c33a47b94ae7766f919` |
| evaluator `--run --fresh ... --output ... --receipt ...` with existing output | repository root | 2 | <0.2 s | existing empty output unchanged; receipt absent; same no-overwrite stderr SHA |
| evaluator run with noncanonical mutated fresh input | repository root | 2 | <0.2 s | output and receipt absent; rollback stderr SHA `6937db2bcfd84494a55bfc32ee2076bd4814575f0cc82e1304400d95c11bf2ce` |

The independent receipt audit recomputed ordinary receipt SHA
`83bd33028c81e9dd555a44e9e7721d5ace298d522e0c069409118bdbf51c6c48`,
normalized receipt SHA
`622b21b914ab5056713fe61916b672f25c95cd9de33d045713619f581c1c00e8`,
all 178 seal entries, all 14 read-ledger rows, all 12 claim hashes, the
publication whitelist, the 92-name registry, and all 92 old/new mutation
hashes and change predicates. No bad row was found. No unexpected repository
write or stale temporary artifact was observed.

The evaluator and runner ASTs contain no float literal, tolerance call,
`eval`/`exec`, CWD dependency, network, Git invocation, or scientific
fixture/scorer import. Evaluator imports are standard-library modules only.
Static strings mentioning forbidden mechanisms occur solely inside positive
selftest scans/injections. Inspected `bool(...)` uses were reductions of
reconstructed nonempty exact objects or exact predicates, not promotion of a
supplied Boolean. The direct global matching path makes one Gamma call; its
analytic product formula is only a later verification.

Each run longer than sixty seconds was kept in an active CLI session and
reported with a runner-status checkpoint; no session exceeded the 300-second
cap. A separate paper scan found no internal ledger, task, fixture, scorer,
review-history, or nonexternal-citation prose. Markdown/KaTeX delimiters,
reference resolution, claim spans, all 164 numeric tokens, and receipts-table
coverage were exact. For each printed number I checked the complete lineage
`source -> law -> operator -> endpoint distribution -> comparison -> claim`;
no copied final Boolean or literal answer table supplied a claim.

## 4. Independent reconstruction method

Before evaluator or receipt scientific-path inspection, I wrote and froze
`seat_i_reconstruct.py` (SHA-256
`026c03041b1e6db6e9fdbe85309018327bc23688cdbc03b26e120b0f0033de40`).
It uses only independently defined immutable tuples, exact integer/Fraction
arithmetic, Boolean truth vectors, explicit matrix multiplication, exhaustive
finite loops, and an independent SHAKE/counter/permutation implementation.
It imports no candidate evaluator code and contains no expected-result table.
The 3.60 s run emitted a 4,190-byte canonical result with SHA-256
`25b3244bd26bd8b62f35f05cc569eb0e76fb8b879c81ef7a2be7619caf068fa6`.

The reconstruction proceeded from

```text
(C_pres, G, C, B, Div, Gamma_g, filling grammar, endpoint squaring)
```

and independently classified the packet as follows:

| Coordinate | Reconstructed status |
|---|---|
| `C_pres` | priced typed zero-pattern catalogue |
| `G` | priced typed Boolean relabeling groupoid |
| `C` | derived orbit and candidate relational referent |
| `B` | priced typed boundary grammar |
| `Div` | priced typed, grammar-relative division doctrine |
| `Gamma_g` | postulated one-whole-filling law family |
| filling grammar | priced kinematics |
| endpoint squaring | postulated nomological clause |

The script reconstructed contextual classes and split fibers; the native
screens and complete kernel polytope; the rational interval; history and
enlarged-carrier controls; writer Gram completeness and a branch-sum
counterobject; continuation/projector closure; active-port freshness and
eraser controls; reciprocal data; and the nonce-bound size-twelve global laws.
Only after freezing that output did I compare it with evaluator and receipt
lineage.

## 5. Claim-by-claim evidence for all twelve blocks

The binding counts are respectively 6, 3, 3, 4, 3, 1, 1, 1, 3, 1, 3, and 0,
for a total of 29.

| Claim block | Printed scope | Evidence grade | Seat I finding |
|---|---|---|---|
| ABSTRACT | finite exact class-relative candidate | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | accurate summary of the separately reconstructed scoped results; no overpromotion |
| MOTIVATION | architectural and stochastic-indivisibility distinction | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | Barandes distinction accurately scoped; changing support and physical adequacy not inherited |
| KINEMATICS | finite typed Boolean zero patterns | `INDEPENDENT-EXACT-RECONSTRUCTION` | 6 contexts, 72 ambient nonzero presentations, 42 contextual classes, exact alias/fiber behavior |
| LAW | all admitted finite fillings of the typed process grammar | `ANALYTICAL-PROOF` | one complete typed source argument and isometric composition yield normalized endpoint laws; no arbitrary-cut Markov field is supplied |
| SUPPORT | registered finite generator family with all-context split lemma | `INDEPENDENT-EXACT-RECONSTRUCTION` | exhaustive target and fresh-child/forgetful certificates survive exact finite census |
| NONDIVISION | native declared cut carrier and rational coupling interval | `ANALYTICAL-PROOF` | unique factor is negative; full positive two-state polytope is empty; interval proof exact |
| DIVISION | finite words of the declared continuation grammar | `ANALYTICAL-PROOF` | writer instrument is complete and projectors intertwine every typed generator, hence every finite word |
| RECIPROCAL | finite writer-reader fixture and same-boundary incidence comparison | `INDEPENDENT-EXACT-RECONSTRUCTION` | literal writer output feeds the reader; joint and counterfactual rows match exactly |
| FAMILY | predeclared incidence-blind stochastic transducer class | `ANALYTICAL-PROOF` | blind resources/prefix record law agree and arbitrary-memory induction excludes only the printed class |
| ONTOLOGY | permanent ontology and nonclaim walls | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | table preserves representation/ontology separation and all permanent walls |
| CONCLUSION | finite exact class-relative candidate ceiling | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | supported synthesis at the eligible cap, explicitly short of law selection or geometry |
| REFERENCES | external literature only | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | Barandes and Sorkin checked against primary sources; no candidate-specific construction attributed to them |

## 6. Evidence for Results A through G

| Result | Evidence grade | Exact accepted scope and finding |
|---|---|---|
| A | `INDEPENDENT-EXACT-RECONSTRUCTION` | contextual Boolean equality, split fibers, and typed groupoid on the declared finite contexts |
| B | `ANALYTICAL-PROOF` | normalization and one-root composition for every admitted finite filling; endpoint squaring remains postulated |
| C | `INDEPENDENT-EXACT-RECONSTRUCTION` | proper support change and totality for the registered generator family, including coefficient-zero target sectors |
| D | `ANALYTICAL-PROOF` | no positive source-independent factorization through the unrecorded native two-state cut, throughout the printed rational interval |
| E | `ANALYTICAL-PROOF` | lawful record-bearing division and persistence for all finite words of the frozen continuation grammar, not beyond it |
| F | `INDEPENDENT-EXACT-RECONSTRUCTION` | reciprocal writer-reader response in the finite fixture with nonrelational resources held fixed |
| G | `ANALYTICAL-PROOF` plus finite exact reconstruction | exclusion of the predeclared incidence-blind stochastic-transducer class under equal resource, schedule, and prior-record premises |

## 7. Analytical proofs and exact finite reconstructions

### 7.1 Common finite anchors

Truth-vector canonicalization gives contextual rows

```text
(ambient nonzero / contextual classes)
C1 3/3, C2 15/15, C3 14/7, C4 14/7, C5 14/7, C6 12/3.
```

Thus there are exactly 72 ambient nonzero presentations and 42 contextual
classes. All 72 representative replays have their exact fibers and contextual
aliases. The generator census has 12 families, 312 source columns, and 468
nonzero transitions. The operation certificate is balanced: 156 create, 156
merge, and 156 unchanged transitions. Coefficient-zero targets remain in the
typed carrier.

The independently defined one-occurrence Cayley/structural operators compose
to the whole-filling class operator. Identity, composition, tensor, and typed
structural maps preserve the admitted source/target boundaries. Exact
groupoid transport was checked for complete boundaries, states, fillings,
operators, split certificates, and endpoint laws, not merely for labels. The
same one-root ledger reaches the support rewrite, coherent and recorded
screens, writer/reader, reciprocal response, and complete matching-family
law.

### 7.2 Whole-filling phase and native nondivision

At `g=1/2`, independent amplitude composition gives

$$
R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix},\qquad
B=|R|^2=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix},
$$

and two uninterrupted coherent occurrences give

$$
C=|R^2|^2=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

A separately prepared stochastic future arrow instead produces

$$
B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix},
$$

which is not `C`. This is an experiment/control distinction, not a
contradiction: cutting and re-preparing discards the relative phase belonging
to the uninterrupted complete filling.

For completeness, parameterize every column-stochastic two-state kernel by

$$
K=\begin{pmatrix}a&b\\1-a&1-b\end{pmatrix},\qquad 0\le a,b\le1.
$$

The first row of `C=KB` yields

$$
225a+400b=49,\qquad 400a+225b=576,
$$

so the unique point in the affine solution space is

$$
a=\frac{351}{175},\qquad b=-\frac{176}{175},\qquad
K=\frac1{175}\begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
$$

It is outside the complete positive polytope. This is stronger than merely
checking the advertised matrix: no other positive two-state kernel is hidden
by the parameterization.

For rational `1/3 <= g <= 1/2`, set

$$
t(g)=\frac{1-6g^2+g^4}{(1+g^2)^2}.
$$

The literal derivative is

$$
t'(g)=-\frac{16g(1-g^2)}{(1+g^2)^3}<0,
$$

so `t` runs from `7/25` to `-7/25`. A rational zero would make
`u=g^2` a rational root of `u^2-6u+1`; the rational-root candidates do not
vanish. Therefore, for every rational coupling in the interval,

$$
\left|2t-\frac1t\right|
=\frac1{|t|}-2|t|
\ge \frac{25}{7}-\frac{14}{25}
=\frac{527}{175}>1.
$$

The nontrivial eigenvalue of a positive two-state stochastic kernel lies in
`[-1,1]`, so no such kernel exists anywhere on the declared rational interval.

The required surviving conclusion is:

> The cut is not a lawful stochastic division on the declared configuration
> space: the complete endpoint law admits no positive source-independent
> factorization through it. A definite configuration may still be actual
> there; what is forbidden is an autonomous Markov restart conditioned only
> on that configuration.

### 7.3 Mandatory history and enlarged-carrier controls

The positive joint

$$
P(a,b\mid q)=B_{aq}C_{bq}
$$

is normalized, has marginal `C(b|q)`, and permits a definite value of `a`.
Its conditional future is `P(b|a,q)=C(b|q)`, which retains the earlier source
`q`. Equivalently, the enlarged state `h=(q,a)` admits a positive Markov
transition to `b`. A phase/amplitude vector or complete history also enlarges
the carrier enough to Markovize the calculation.

These are mandatory **non-kills**. They do not furnish a source-independent
`K(b|a)` on the declared native carrier and do not imply that a definite
configuration is impossible. Conversely, native nondivision does not prove
ontological state incompleteness, hidden ontic phase, actualization failure, or
absolute non-Markovizability.

### 7.4 Same-Born/different-filling controls

The exact reflection

$$
S=\begin{pmatrix}3/5&4/5\\4/5&-3/5\end{pmatrix}
$$

has the same entrywise square `B` as `R`, but `S^2=I`, hence its two-leg law is
`C'=I` and

$$
K'=C'B^{-1}=\begin{pmatrix}-9/7&16/7\\16/7&-9/7\end{pmatrix}.
$$

Using the adjoint on the second leg likewise changes the two-leg endpoint law
to `I`. Thus a one-leg Born table cannot substitute for the complete Gamma
law; relative sign, orientation, and whole-filling composition are
load-bearing.

### 7.5 Writer instrument, records, and grammar closure

For every basis input, the writer branch maps retain all branch sectors,
including zero-amplitude branches, and satisfy the exact completeness
identity

$$
\sum_r V_r^\dagger V_r=I.
$$

The carried record sectors are orthogonal. Direct evaluation and every lawful
alternate cut agree for every admitted input. A branch-sum-only substitute can
preserve each basis branch probability while having Gram matrix

$$
\widetilde G=\begin{pmatrix}1&24/25\\24/25&1\end{pmatrix}.
$$

On the normalized superposition `(3/5,-4/5)`, its total is `49/625`, not 1.
This exact counterobject shows why branch probabilities are not a replacement
for the typed branch instrument and projector data.

The continuation reconstruction has 3 record-sector boundary slices, 18
typed generator restrictions, and 108 compatible generator pairs. Every
generator obeys the appropriate projector intertwining identity. Composition
therefore proves the identity for every finite word. The direct and alternate
cuts agree on all inputs, and the delayed reader consumes the literal carried
context.

This permanence is exactly grammar-relative. Adding a reset or inverse-toggle
letter breaks projector intertwining. Reactivating the actual old port permits
erasure. A genuinely fresh port is safe, while merely renaming the carried
port does not make it fresh. Severing the delayed reader changes its probe
probability from `256/625` to 0 and is detected.

### 7.6 Reciprocal and global-law controls

The independently reconstructed reciprocal joint contains the exact entries
`9/25`, `0`, `144/625`, and `256/625`, together with the same-boundary
opposite-incidence row. The comparison holds nonrelational typed resources
fixed and uses the writer's literal output context.

The fresh nonce reconstruction has seed SHA
`51b21dafdb978d85df48d34f2a8bccd70ce3cb872241f2d2225d93c3c7d6e65f`,
selected-block SHA
`cc07ecce3a2e9e7013867c30a45cd49d088edab390d96e78c750ffda3b365416`,
queries `1,8,9,10`, challenge permutation
`[5,11,7,3,2,1,6,4,9,0,10,8]`, size 12, 1,296 endpoint coordinates per
member, and 37 peak cells. Common marginals are all `16/25`; challenge
marginals are `0,0,0,16/25`. Rejection and reroll counts are zero. Blind
resources and prior record laws are exact matches. The complete size-twelve
operator was reconstructed as one global call, not local gadget calls or a
hand-entered product.

## 8. Registered mutations and fresh attacks

### 8.1 Registry-wide and assigned checks

The evaluator selftest executed all 92 registry names. I independently
recomputed every before/after byte hash, evidence hash, change predicate, and
failure predicate; all 92 objects changed and all were killed by their stated
object-level discriminator. The `KILLED` label was never used as the
predicate.

All twenty Seat I assignments were then invoked individually. Every command
returned 0 with status `PASS`, `changed=true`, distinct old/new hashes, and the
indicated independently checked failure route:

| Mutation | Old object SHA-256 | New object SHA-256 | Decisive check |
|---|---|---|---|
| `ABSOLUTE-NONDIVISION` | `b581beec2d7ca39a6f1cad16da7123c9f543d181f4543d645ae8ec8bf5de4915` | `b2fb9e7b95c45388f42b46801e0bcb3c2fceb4ca42cfe598a4a7a622b3c0a71b` | exact scope-wall refusal |
| `AMPLITUDE-TO-ONTOLOGY` | `b581beec2d7ca39a6f1cad16da7123c9f543d181f4543d645ae8ec8bf5de4915` | `b6da86d10d55a36bef558426def21314b5f5ed17cacb1a2f5ae3d6ddc6c8c8a0` | exact scope-wall refusal |
| `BORN-TABLE-AS-GAMMA` | `d83a8da11709db51f8370e30745cd274ed77011e3ea7f7b0494888b457df8edd` | `cf6aa25537a4918451bc22737db40a924fe9faa00a3dd39a65a85f4dc49a6cee` | complete-Gamma type refusal |
| `BRANCH-SUM-ONLY` | `d83a8da11709db51f8370e30745cd274ed77011e3ea7f7b0494888b457df8edd` | `242ac7f8b52bb60e25dd67a43229351924f06cf4f35e468e8fe70e84a899f5c6` | identity branch sum lacks record semantics |
| `CACHED-G-OR-SHADOW` | `d83a8da11709db51f8370e30745cd274ed77011e3ea7f7b0494888b457df8edd` | `062949d5fa6a800c46b60ceab9638bf114e891df9914d08b3248781f74703490` | recomputed shadow hash moves |
| `CARRIED-PORT-STILL-ACTIVE` | `4918036668a32af68a2facf41f9f3bc62dd046b9b6447534f5ad63406d8ece81` | `8972872e7ec2c940385ff18a87ef3c5e7c1c28c3078321a178da1fe6c7adc6a6` | inactive-port selection refusal |
| `COIN-CONTACT` | `04c70dc489f293c2663b331fa243bc12c4e23dec817ead77f61a7c210e182cd3` | `2ed94826068b4e2e606b3c7773d02dacbdc32fca82ba5ddd9dd12824918c778b` | candidate primitive refusal; screens move |
| `DELAYED-READER-SEVER` | `4918036668a32af68a2facf41f9f3bc62dd046b9b6447534f5ad63406d8ece81` | `c4a5949a431648b4e866b3c80ed58c313c9b11e88e9b75fbfd170f21177dc222` | probe moves `256/625 -> 0` |
| `EVENT-ORDER-TO-TIME` | `b581beec2d7ca39a6f1cad16da7123c9f543d181f4543d645ae8ec8bf5de4915` | `700225e8dccac1ca24848498cbd3dc7e86cb5ac63d110a92e465b935c8596e9b` | exact time-wall refusal |
| `HIDDEN-ERASER` | `4918036668a32af68a2facf41f9f3bc62dd046b9b6447534f5ad63406d8ece81` | `c883faaa77f0b685329652b66c9e07a12d0ac38cbe6ea757b5b88703d3abb82d` | grammar closure fails |
| `HISTORY-PASSED-OFF-AS-NATIVE-K` | `b581beec2d7ca39a6f1cad16da7123c9f543d181f4543d645ae8ec8bf5de4915` | `4a53a6b52ba436fac6544c1d514b958724b72389eb4515a14874e71d6049cc4e` | exact native/history scope refusal |
| `NONDIVISION-AS-STATE-DEFECT` | `b581beec2d7ca39a6f1cad16da7123c9f543d181f4543d645ae8ec8bf5de4915` | `b2017092ad017bf0872b4400c61329e75a82d8a5b938f68ed0493cc6b680af54` | exact configuration-sufficiency wall |
| `NORMALIZATION-TO-ACTUALIZATION` | `b581beec2d7ca39a6f1cad16da7123c9f543d181f4543d645ae8ec8bf5de4915` | `9aefbb9489620c5f6ab3940fd4f432c1a585c9327e2571302d29dfe09f72f7f3` | actualization-coordinate refusal |
| `OLD-CHILD-REUSE` | `e62ed4ddce99672847fb854c5428aa6c889810965988416136ccdda8abbba394` | `6aeba18cced686586190a874a1fcf44b7160f8843a0e8cd0b6588a46e7297136` | both same-name and changed-type reuse refused |
| `OUTCOME-FLIP` | `0a5a83336ba4aa258d9b642e120d5a8ef52c9af09913c72e4f5ee94e10efc001` | `9bf82d0c563de12932e05502a99b90a51f8ded716ee49c063f8bc912495f594c` | independent first-failure digest differs |
| `PHASE-REFLECTION-MUTATION` | `04c70dc489f293c2663b331fa243bc12c4e23dec817ead77f61a7c210e182cd3` | `1b5e8786036fd3eac045d9f865366159f644431c89e3bfd05b4ed3e3e1569dba` | same `B`, different `C`; candidate primitive refusal |
| `RESET-WRITER-CHAIN` | `4918036668a32af68a2facf41f9f3bc62dd046b9b6447534f5ad63406d8ece81` | `5335ef3220be8011987f869ff2e33f5e6e49112585164ca64f33e57e8eec8156` | reset primitive refused; projector route broken |
| `RETURN-TO-OLD-PORT` | `4918036668a32af68a2facf41f9f3bc62dd046b9b6447534f5ad63406d8ece81` | `8972872e7ec2c940385ff18a87ef3c5e7c1c28c3078321a178da1fe6c7adc6a6` | inactive-port selection refusal |
| `SAME-BORN-REFLECTION` | `04c70dc489f293c2663b331fa243bc12c4e23dec817ead77f61a7c210e182cd3` | `1b5e8786036fd3eac045d9f865366159f644431c89e3bfd05b4ed3e3e1569dba` | same `B`, different `C`; candidate primitive refusal |
| `TARGET-CONTACT` | `04c70dc489f293c2663b331fa243bc12c4e23dec817ead77f61a7c210e182cd3` | `626362d33a22c2b47a98edbb37238fc258475ea04d2f0e73e71e2a6acdd743e3` | primitive identity refusal even where `B,C` are unchanged |

The duplicate old/new pairs in the two reflection labels and the two
old-port labels are disclosed in `REPAIR-2`; every individual mutation still
has unequal before/after bytes, so this is not an integrity block.

### 8.2 Mandatory fresh attacks

| Fresh object | Invariant targeted | Exact result |
|---|---|---|
| history adjoint and same-Born reflection | whole-filling phase/orientation, not one-leg `B` | `B` is preserved while `C` becomes `I` and `K` moves; candidate survives by binding the complete primitive |
| exhaustive `K=[[a,b],[1-a,1-b]]` | complete positive two-state polytope | unique solution has `a=351/175`, `b=-176/175`; no feasible positive point |
| source-conditioned `K_q(b|a)=C(b|q)` | native source independence | positive and exact, but retains `q`; mandatory non-kill, not a native restart |
| grammar extension by reset/inverse-toggle | record-projector closure/exhaustiveness | projector intertwining fails, so permanence remains correctly grammar-relative |
| renamed carried port and actual old-port return | global freshness/active-port identity | rename is not fresh; actual reactivation permits erasure; both are outside the frozen continuation theorem |
| severed delayed reader/projector | literal record lineage despite cached labels | probe moves from `256/625` to 0; sever detected |
| branch-summed substitute | instrument-level alternate-cut equality | fake Gram has off-diagonal `24/25`; normalized superposition totals `49/625`; substitute killed |

### 8.3 Genuinely new attacks

These object-level attacks were conceived independently; the first three were
frozen in the reconstruction before evaluator-path inspection. No
changed-source attack was used, so no source patch envelope is applicable.

1. **NEAR-IRRATIONAL-RATIONAL-STRESS**, conceived
   2026-08-20T00:41Z. At `g=408/985`, close to the excluded irrational zero,
   exact arithmetic gives
   `t=1607521/1292061882721` and nontrivial factor eigenvalue
   `-1669423908775366910832959/2077016609773544641`; a kernel entry is
   negative. It targets tolerance leakage at an interval's hardest rational
   point. It is not a registered relabel or the endpoint `g=1/2` reflection.
   The candidate survives.

2. **CROSS-COUPLING-DIVISION-SPLICE**, conceived
   2026-08-20T00:42Z. A writer built from `Gamma_(1/2)` and continuation built
   from `Gamma_(1/3)` are separately well typed, but their complete law
   identities differ; the splice is refused. It targets one-law identity
   across a legal cut, not a cached shadow at one coupling. The candidate
   survives.

3. **TWO-STEP-FRESH-ALIAS-RETURN**, conceived
   2026-08-20T00:43Z. The first extension uses a genuinely fresh child; only a
   later compositional step aliases that identity back to an earlier carried
   sector. The global identity ledger rejects it. Unlike registered
   single-step old-child/old-port objects, no individual first step selects an
   old port. The candidate survives.

4. **ONE-STATE-COARSE-CUT**, conceived 2026-08-20T00:55Z. Collapsing the two
   cut states to one makes every factorized endpoint law have identical source
   columns, while the two columns of `C`, `(49,576)/625` and `(576,49)/625`,
   differ. Thus coarse-graining does not restore division. It changes the cut
   carrier and is neither the registered native-history wall nor the mandatory
   two-state-polytope search. The candidate survives.

## 9. Numbered findings

### KILL

**KILL-0 — none.** I found no reproducible instance of `P13K1`–`P13K30` and
no corpus-integrity block. No positive autonomous native kernel exists; no
licensed continuation erases the record; no Barandes or Sorkin overclaim was
found.

### REPAIR

**REPAIR-1 — label the derivative witness exactly.** The receipt field named
`derivative_sign_formula` serializes
`-8*g*(1-g^2)/(1+g^2)^3<0`, whereas the literal derivative of the printed
`t(g)` is
`-16*g*(1-g^2)/(1+g^2)^3<0`. The receipt expression is exactly one-half of
the derivative and therefore a valid sign-equivalent witness. The paper does
not print the wrong formula, and the interval proof is unaffected. A future
certificate should either use `-16` or rename the field
`derivative_sign_witness`.

**REPAIR-2 — diversify semantically distinct registry objects.** The registry
uses the same changed object for `PHASE-REFLECTION-MUTATION` and
`SAME-BORN-REFLECTION`, and likewise the same changed object for
`CARRIED-PORT-STILL-ACTIVE` and `RETURN-TO-OLD-PORT`. Each old/new pair is
genuinely changed and killed, so the integrity rule is satisfied. For stronger
attack diversity, a forward audit should serialize separate adjoint-versus-
reflection and mere-rename-versus-actual-return objects. The mandatory fresh
objects above already test those distinctions and find no scientific failure.

### NARROWING

**NARROWING-1 — native, not absolute, nondivision.** Result D excludes only a
positive source-independent restart through the declared two-state
configuration carrier. It does not exclude history-, amplitude-, or
enlarged-state Markovization.

**NARROWING-2 — no ontological state-defect inference.** The negative native
factor does not imply that a definite configuration cannot be actual, that
the configuration is ontologically incomplete, or that an amplitude/history
coordinate is ontic.

**NARROWING-3 — record permanence is grammar-relative.** Result E covers all
finite words of the frozen continuation grammar. An added reset, inverse
toggle, or actual old-port reactivation can erase the record and is not
licensed by that grammar.

**NARROWING-4 — literature supplies context only.** Barandes supplies the
fixed-configuration stochastic-indivisibility distinction and Sorkin supplies
broader histories/quantum-measure context. Neither supplies this catalogue,
Gamma law, support split, division doctrine, locality, actualization, or
numerical result.

**NARROWING-5 — blind exclusion is class-relative.** The size-twelve result
excludes the predeclared incidence-blind stochastic-transducer class under
equal resource, schedule, prefix-token, and prior-record-law premises. It is
not absolute relational irreducibility or a ban on arbitrary lookup/memory
representations outside the interface.

### NON-KILL

**NON-KILL-1 — positive history-conditioned joint.** `B(a|q)C(b|q)` is a
valid positive joint with marginal `C`; it retains `q` and is therefore the
required scope control, not a native `K(b|a)`.

**NON-KILL-2 — enlarged-carrier Markovization.** Taking `h=(q,a)`, a complete
history, or an amplitude/phase representation yields a positive Markov
description. The paper claims only native configuration-relative
nondivision, so this does not refute it.

**NON-KILL-3 — definite intermediate configuration.** A definite `a` is
compatible with the calculation. Native nondivision restricts legal
autonomous restarting, not actual configuration definiteness.

**NON-KILL-4 — separately prepared future arrow.** `B^2` is positive but is
the law of a cut/re-prepared experiment; it is not the uninterrupted
whole-filling law `C` and hence is not a factorization of that experiment.

**NON-KILL-5 — sign-equivalent receipt factor.** The factor-of-two receipt
wording in `REPAIR-1` preserves the exact derivative sign and every endpoint,
root-exclusion, and eigenvalue bound.

## 10. Earliest outcome rung and orthogonal coordinates

**Earliest supported rung:**
`P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED`.

This is the eligible cap. Neither selector-control rung is earned or implied.

| Orthogonal coordinate | Seat I disposition |
|---|---|
| specification consistency | `CONSISTENT` across paper, source, receipt, bundle, coupling domain, grammar, and outcome ladder |
| point-free referent/presentation | typed contextual Boolean orbit is a candidate referent; raw roles, formulas, Venn cells, and hashes remain presentation/provenance |
| complete Gamma | `SUPPORTED` as one whole-filling evaluator on the frozen finite grammar, not a Born-table wrapper |
| lawful-source sufficiency | `SUPPORTED` for complete typed source arguments at admitted source/division boundaries; not asserted at arbitrary cuts |
| shadow derivation | `SUPPORTED`; support rewrite, screens, writer/reader, reciprocal response, and global family move under load-bearing primitive attacks |
| support change | `SUPPORTED` for the registered finite generator family and all-context split lemma |
| reciprocal chain | `SUPPORTED` in the finite writer-reader fixture with literal output context and matched nonrelational resources |
| division recovery | `SUPPORTED` for all finite words of the declared continuation grammar |
| native nondivision | `SUPPORTED` on the declared two-state carrier and rational interval; history/enlarged carriers explicitly excluded from the native claim |
| blind class | `SUPPORTED` only for the predeclared incidence-blind stochastic-transducer interface with arbitrary memory and equal prefixes/resources/prior law |
| coupling selection | `UNSELECTED`; rational `g` is a law-family parameter |
| law selection | `UNSELECTED` |
| catalogue selection | `UNSELECTED` |
| event/filling grammar selection | `PRICED-KINEMATICS`, not derived |
| division-doctrine selection | `PRICED-TYPED-GRAMMAR-RELATIVE`, not derived |
| representation versus ontology | amplitude/path/Hilbert coordinates are representational; whole-filling phase/composition is nomological; the configuration orbit is only an ontological candidate |
| actualization | `POSTULATED-NOT-CONSTRUCTED`; normalization, branching, and records do not select an outcome |
| later-physics walls | valuation, metric, topology, causality, curvature, continuum, gravity, GR/QFT, and phenomenology are unconstructed |

## 11. Representation, ontology, and permanent walls

The reconstructed ontology ledger is:

| Object | Status |
|---|---|
| typed Boolean zero-pattern orbit | candidate complete relational configuration |
| raw role names, formulas, regulator cells, path labels, and hashes | presentation or provenance |
| amplitude vector and Hilbert coordinates | representation of the law |
| relative phase and complete filling composition class | nomological because they change endpoint probabilities; not thereby ontic state |
| endpoint squaring | postulated law clause, not derived |
| carried child sector | derived record within the declared grammar |
| raw Boolean contact/incidence | relation only; not topology, distance, metric, causal order, or geometry |
| definite configuration at the native cut | allowed; actualization remains postulated |
| coupling, catalogue, grammar, division doctrine, filling, and outcome | unselected |

In particular, stochastic indivisibility is not ontological state
incompleteness. The former is the exact nonexistence of a positive
source-independent factorization on one declared carrier for one complete
endpoint law. The latter would be an additional ontological claim that this
construction neither needs nor establishes.

No result supplies an extensive valuation, length, dimension, metric,
topology, causal order, locality/no-signalling theorem, Lorentz structure,
curvature, continuum limit, stress response, gravitational dynamics, GR,
QFT, particles, Hamiltonian, vacuum, phenomenology, empirical adequacy, law
selection, or actualization mechanism. Filling order, occurrence count,
receipt order, and boundary typing are not emergent time. These are permanent
walls of this review outcome.

## 12. Candidate-paper grade

**Grade: `ACCEPT-WITH-FIXES`.**

The scientific claims survive at their printed finite, native, and
grammar/class-relative scopes. The two fixes are certificate/audit-surface
repairs: one sign-witness label and two pairs of semantically duplicate
registered attack objects. Neither changes a theorem, primary rung, ontology
coordinate, or the paper's correct native-nondivision sentence. No decisive
scientific counterexample exists.

The ordinary SHA-256 is intentionally not embedded in these self-referential
bytes; it is reported externally after freeze.

normalized_sha256: 4afd10431b25e19f806ac8ccacedd4dfcece27ae60b96d086559ca202e2466e1
