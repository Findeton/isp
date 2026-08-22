# Paper 02 hostile review — Seat O: ontology, gauge, actuality, and Barandes scope

Date: 2026-08-22

Status: **INDEPENDENT BLIND REVIEW — FROZEN REPORT; CANDIDATE UNCHANGED**

Verdict: **REVISE**

First decisive semantic counterexample: **the separated source category
$\mathcal Q$ identifies operationally equivalent preparation procedures before
$J_R$ acts, while the claimed preparation-contextual fiber inflation requires
$J_R$ to remember which such procedure occurred. A functor cannot distinguish
two source arrows that are equal.**

First affected coordinates: `contract`, `fibers`, `context`, `barandes`, and
the proposed rung-6 ceiling. The canonical operational quotient survives at a
strictly smaller scope.

Ordinary SHA-256: reported externally after these bytes freeze.

Normalized self-hash convention: replace exactly the 64 lowercase hexadecimal
characters after `normalized_self_sha256:` below by 64 ASCII zeroes, preserving
every other byte, and apply SHA-256.

normalized_self_sha256: 9ad8a3bd4fa6cebbfd576dab4cc3ea378a40902d90033ba2cfb800f39e26f53c

## 1. Independence and corpus authentication

This was a mutually blind Seat O review. I did not inspect or communicate with
either sibling seat and did not inspect either forbidden sibling report path:

- `v17/review-paper02-mathematics-quotient.md`;
- `v17/review-paper02-quantum-foundations.md`.

I used no implementation, evaluator, fit, or generated numerical artifact. At
review start the repository HEAD was exactly
`5340b5c71b0f0cfdb7e424d5ac21f5cd3bbb1efc`. The protocol is bound to
construction commit `bfaddd50a5006ea90933a5a6eb6f89e345a98315`.

| Artifact | Required SHA-256 | Recomputed SHA-256 | Result |
|---|---|---|---|
| `v17/note-paper02-operational-quotient-ontology-residue-pin.md` | `e26b91b7126046d4b9c8f579fa6147f48922dc7fb711851b5a0fe3501a2c49cf` | `e26b91b7126046d4b9c8f579fa6147f48922dc7fb711851b5a0fe3501a2c49cf` | authenticated |
| `v17/paper-02-operational-quotient-ontology-residue.md` | `55edf811b2d80a628cae1d871994383e0013ec58dd77b70d340eebb836c93eec` | `55edf811b2d80a628cae1d871994383e0013ec58dd77b70d340eebb836c93eec` | authenticated |
| `v17/note-paper02-construction-audit.md` | `6d3b63dad6866c725ee8cc621e2d5792c1532683de295b6fec3c45b72283627c` | `6d3b63dad6866c725ee8cc621e2d5792c1532683de295b6fec3c45b72283627c` | authenticated |
| `v17/note-paper01-hostile-review-adjudication.md` | `3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1` | `3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1` | authenticated |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | authenticated |

The protocol itself recomputed as
`4c032bc72696bc17375fb7b05e07771301205e1f7990c3cf847925580c7da532`.
The pin had 654 LF / 29,191 bytes and the candidate had 1,456 LF / 63,328
bytes, matching the frozen construction audit.

## 2. Executive assessment

Paper 02 contains a sound central idea: complete future profiles define the
canonical operational quotient, and arbitrary idle fibers show why experiment
does not select every extra microscopic variable. Its five-way warning against
calling every unobserved variable “gauge” is physically valuable. The phase,
record, actuality, and no-chronology scopes are also disciplined.

The submitted packet nevertheless erases procedure context one step too early.
Section 2.1 defines $\mathcal Q$ so that two operationally equivalent
preparation or transformation procedures are literally the same arrow. Section
2.2 then represents $\mathcal Q$ through $J_R$. Section 4.2 later requires a
preparation-contextual completion in which two such procedures leave different
latent values. That object cannot be the image of a well-defined $J_R$ from the
declared $\mathcal Q$.

This is not an objection to contextual ontology. It is the opposite: a theory
that aims to classify contextual ontology must retain a typed category of
laboratory procedures above its operational quotient. Spekkens's foundational
definition does exactly that. Paper 02 presently starts with the quotient and
therefore cannot express the context dependence it invokes.

The defect is bounded but semantic. A successor or authorized repair needs a
prequotient procedure category $\mathcal P$, an operational quotient functor

$$
q:\mathcal P\longrightarrow\mathcal Q,
$$

and representations defined on $\mathcal P$. Only then can two procedures
$P,P'$ satisfy $q(P)=q(P')$ while their ontic images differ. The current frozen
candidate cannot be repaired by changing terminology alone.

## 3. First decisive counterexample

### 3.1 The two parity preparations

Use the candidate's parity-oblivious states. Let the even and odd mixed
preparation procedures be

$$
P_{\rm e}=\frac12(P_{00}+P_{11}),
\qquad
P_{\rm o}=\frac12(P_{01}+P_{10}).
$$

Operationally both prepare $I/2$. Under the definition in candidate Section
2.1,

$$
P_{\rm e}=P_{\rm o}
\quad\text{as arrows of }\mathcal Q.
$$

A functor or well-defined map on $\mathcal Q$ must therefore obey

$$
J_R(P_{\rm e})=J_R(P_{\rm o}).
$$

But the preparation-correlated inflation in Section 4.2 is supposed to retain
which operationally equivalent procedure was used. In its sharpest form it
requires, for example,

$$
\nu(dz\mid P_{\rm e})=\delta_{m e}(dz),
\qquad
\nu(dz\mid P_{\rm o})=\delta_{m o}(dz),
$$

so its represented preparations are unequal. Hence $J_R^Z$ is not well
defined on $\mathcal Q$.

There are only three possible escapes, and each changes the submitted claim.

1. Retain the implementation/coin label as a registered operational record.
   Then $P_{\rm e}\neq P_{\rm o}$ in $\mathcal Q$ and this is not a
   preparation-contextual fiber over one operational class.
2. Put the two procedures among extra native arrows of $\mathcal S_R$ outside
   the image of $J_R$. Then the claimed inflation is not constructed uniformly
   from the declared $\mathcal Q$-representation and the quotient theorem does
   not establish its contextual bridge.
3. Let $J_R$ depend on an implementation label absent from its source arrow.
   Then $J_R$ is not a function on the declared source category and the label
   is an untyped hidden input.

The same problem recurs for transformation contextuality. The five convex
decompositions of $T$ are equal as transformations in the separated
$\mathcal Q$, yet a transformation-contextual ontology must be permitted to
represent those laboratory procedures differently.

### 3.2 Why this matters physically

The primary definition in Spekkens begins with preparation, transformation,
and measurement **procedures**, defines operational equivalence among them,
and then asks whether their ontological representations depend only on the
equivalence class. Context is precisely the information lost by the quotient.
One cannot study this dependence after replacing the procedure domain by its
equivalence classes unless a prequotient lift is retained.

Primary source checked:

- R. W. Spekkens, [Contextuality for preparations, transformations and unsharp measurements](https://arxiv.org/html/quant-ph/0406166), Sections II--III.

The standalone parity, six-rotation, Peres--Mermin, and Bell contradictions may
remain mathematically valid with their printed premises. What fails is the
bridge claiming that the submitted adequate-representation contract contains
and classifies the contextual microscopic models used to evade those
conjunctions.

## 4. A second semantic overreach: the Barandes row

Barandes's ontology has more structure than an idle fiber on record strings.
For each model it asserts a fixed configuration space, contingent standalone
probabilities, indivisible transition laws at target/conditioning times, and
one actual configuration trajectory. Its minimalist transition laws may leave
many compatible non-Markovian realizers.

The accepted Paper 01 result explicitly did **not** construct a complete
microscopic configuration trajectory. Paper 02's static bit, Cantor/Lebesgue,
and hold/flip fibers add hidden coordinates to laboratory record histories,
but the manuscript does not prove that any such packet supplies:

1. one fixed configuration space across the full experiment family;
2. Barandes's typed target and conditioning-time transition law;
3. a consistent complete trajectory referent through unrecorded cuts; and
4. the complete Q0--Q3 contextual apparatus interface from that one law.

Theorem 9 is therefore justified up to “not selected and not refuted,” but not
up to the positive assertion that a Barandes-style configuration ontology is
already “represented as an admissible completion.” The adequate-class
definition allows such a completion if one is supplied; it does not construct
one.

Primary source checked:

- J. A. Barandes, [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/html/2507.21192v1), especially Sections 2, 3, and 5.

The proper frozen classification is therefore
`BARANDES-ONTOLOGY-ADMISSIBLE-BUT-UNCONSTRUCTED-AND-UNSELECTED`, not yet
`REPRESENTED`. This is independent of whether Barandes's broader physical
proposal ultimately succeeds.

## 5. Reconstructed complete lineages

### 5.1 Operational profile and quotient

Consider the identity channel and $Z$ conjugation. Both have the same immediate
single-outcome effect $I$. On input $|+\rangle$, however, a later $X$ reader
gives $+1$ with certainty after identity and $-1$ with certainty after $Z$.
Thus the immediate scalar is insufficient. Their complete profiles differ:

$$
\Phi_R(x_{\mathrm{id}})\neq\Phi_R(x_Z).
$$

For any adequate representative $x$, the quotient class $[x]_R$ records its
entire future profile, and $\overline K_R([x]_R)$ decodes the corresponding
quantum channel. The lineage is

```text
typed boundary -> represented channel -> all ancillary future profiles
-> equivalence class -> decoded operational channel
```

This lineage supports Theorems 1--2 on the declared reachable image. It does
not require a microscopic interpretation of the representative.

### 5.2 Fiber inflation, reduction, and conditional factorization

Start with a record representative $h$ and attach a static bit $z$ with
$\Pr(z=0)=\Pr(z=1)=1/2$. Every inherited reader ignores $z$, so

$$
\sum_z\Gamma^Z(h,z)=\Gamma(h).
$$

The projection $\pi_Z(h,z)=h$ is many-to-one. It is not coordinate gauge. It
is an empirically sufficient forgetting map in the frozen domain. A family
$I_R$ declared natural under this projection obeys

$$
I_{R^Z}(h,z)=I_R(h),
$$

so it cannot select $z$. This factorization is correct because invariance under
the forgetting map is an explicit premise. It proves conditional
nonidentifiability, not nonexistence.

### 5.3 Equal immediate data and phase-complete prediction

The preparations

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}
$$

have the same $Z$ diagonal. A common Hadamard continuation maps them to
$|0\rangle$ and $|1\rangle$. Hence their complete profiles differ and a
diagonal-only predictive state fails. The operational quotient must retain an
equivalent phase-complete structure, without thereby selecting complex numbers
as substances.

### 5.4 Record event and microtrajectory ambiguity

Let $h_{\rm rec}$ be one actual record string. The static-bit inflation gives
two candidate microscopic completions $(h_{\rm rec},0)$ and
$(h_{\rm rec},1)$ with identical registered profiles. Hold and flip dynamics
give further unequal multi-boundary microhistories with the same records.
Therefore the record event descends operationally while the complete
microtrajectory does not.

This establishes

$$
\text{actual record}\nRightarrow\text{selected microscopic trajectory}.
$$

It does not establish that either hidden completion is physically real.

## 6. Gauge, redundancy, contingency, and physical difference

The submitted five-way taxonomy is conceptually sound when its maps are
actually typed.

| Case | Repeatable control | Correct status |
|---|---|---|
| invertible coordinate gauge | relabel $z\mapsto1-z$ while pushing forward the full state, law, histories, and readers | one world in different coordinates |
| dilation presentation gauge | rotate inaccessible Kraus/environment coordinates while preserving the CP map and all readers | one represented operation; no new record |
| empirical redundancy | project $(h,z)\mapsto h$ in the frozen reader domain | many-to-one underdetermination, not coordinate gauge |
| contingent hidden structure | assert that $z$ is a real but currently unread fact with its own law | physically possible, neither selected nor refuted |
| physical difference | add a predeclared calibrated $D_Z$ that separates $z$ values | different theories in the enlarged experiment class |

An inaccessible variable becoming readable later does not prove that it was
nonphysical before. It shows that empirical equivalence is relative to a
frozen experiment domain. Conversely, inventing a new coupling after seeing
the models does not retrospectively select one; the enlarged experiment and
predictions are new physical inputs.

The category defect in Section 3 prevents this otherwise useful taxonomy from
being fully applied to procedure-contextual fibers. Static and dynamically
idle fibers remain valid controls.

## 7. Mandatory Seat O fresh attacks

| Attack | Reconstruction | Disposition |
|---|---|---|
| O1 invertible relabel mistaken for another world | Apply a measurable bijection $f:Z\to Z'$ to histories, laws, and readers with inverse $f^{-1}$ | candidate passes; full-packet isomorphism is coordinate gauge |
| O2 noninvertible forgetting called gauge | $\pi_Z(h,z)=h$ has no inverse when $|Z|>1$ | candidate passes; it calls this empirical reduction, not coordinate gauge |
| O3 inaccessible variable becomes readable in an enlarged domain | Add a calibrated reader $D_Z$ with $p(d\mid z)$ dependent on $z$ | candidate passes; old quotient refines, but this is a new experiment domain |
| O4 contingent hidden variable with no discriminator | Assert a static $z$ and its law while every registered reader ignores it | candidate passes as underdetermined possibility, not selection |
| O5 same records, different actual microtrajectories | Compare hold and prefix-controlled flip paths above the same $h$ | candidate passes; record actuality and microactuality separate |
| O6 renormalization advertised as actualization | Conditioning gives $p(h\mid A)=p(h)/p(A)$ but produces no realized value of $h$ | candidate passes; normalization and conditioning select no event |
| O7 preferred configuration algebra selected by simplicity | A unitary-conjugate or recoded algebra can change description length without changing the complete profile | candidate passes; simplicity is not a physical selector |
| O8 Barandes realizer not fixed by licensed transitions | $R_+$ and $R_-$ may share all licensed one-target laws and disagree on two-target correlation | candidate passes the underdetermination point; it overreaches only by calling a full Barandes completion represented |
| O9 latent discrete fiber promoted to spacetime atom | The bit has no order, interval, clock, adjacency, or metric discriminator | candidate passes; no geometric promotion is made |
| O10 lab slot order promoted to chronology | Independent commuting operations may be serialized in either order while the operational process agrees | candidate passes; supplied control order is not fundamental time |

## 8. Candidate claims 1--13

| # | Claim | Seat O disposition |
|---:|---|---|
| 1 | complete-profile equivalence is a typed congruence | ACCEPT at the registered operational scope |
| 2 | reachable quotient is naturally isomorphic to $\mathcal Q$ on image | ACCEPT-WITH-SCOPE; no extra-native inverse |
| 3 | every adequate representation admits all stated fiber inflations | REVISE: static/countable/Borel idle fibers survive, but preparation-contextual inflation is not typed over the separated $\mathcal Q$ |
| 4 | refinement/reduction-natural invariants factor through quotient | ACCEPT-WITH-SCOPE as a conditional theorem over explicitly admitted maps |
| 5 | gauge/redundancy/contingency/physical difference are distinct | ACCEPT conceptually; procedure-context application incomplete |
| 6 | complete testers force phase-complete predictive states | ACCEPT; scalar ontology not thereby selected |
| 7 | realification preserves predictions with composition cost | ACCEPT-WITH-SCOPE subject to Seat Q's exact scalar audit |
| 8 | positivity survives contextuality and Bell controls | ACCEPT for positive record laws; the contextual-model bridge requires the missing procedure category |
| 9 | resource minima are class-relative | ACCEPT-WITH-SCOPE |
| 10 | records descend while microactuality remains open | ACCEPT |
| 11 | Barandes ontology is represented but unselected | REVISE: it is admissible in principle, unconstructed, unselected, and unrefuted |
| 12 | no registered discriminator selects an extra fiber | ACCEPT for the explicitly constructed idle fibers; this is true by their frozen-profile definition |
| 13 | rung-6 overall ceiling | NOT EARNED until the procedure/context and Barandes bridges are repaired |

## 9. Controls C1--C18

| Control | Result | Reason |
|---|---|---|
| C1 record representation | PASS | quotient decodes its operational quantum object |
| C2 hidden bit | PASS | explicit nonidentifiability control |
| C3 hidden continuum | PASS-IN-SCOPE | mutually singular idle laws can have the same record pushforward |
| C4 latent dynamics mutation | PASS | unequal microcorrelations, equal inherited profiles |
| C5 Kraus rotation | PASS | inaccessible fine labels are presentation variables |
| C6 minimal/padded Stinespring | PASS | restricted minimum is not ontic truth |
| C7 equal density/different preparations | FAILS THE CONTRACT BRIDGE | standalone contextuality witness is valid, but $\mathcal Q$ has already equated the procedures before $J_R$ |
| C8 equal effect/different channel | PASS | complete continuations retain disturbance |
| C9 Peres--Mermin | PASS-WITH-PREMISES | no context-independent sharp product table |
| C10 CHSH | PASS-WITH-PREMISES | measurement independence plus factorization excluded |
| C11 full phase circle | PASS | diagonal-only quotient rejected |
| C12 complex/real | PASS-IN-SCOPE | scalar ontology nonunique; global composition cost printed |
| C13 process memory | PASS | complete future profiles do not Markovize the cut |
| C14 reader removal | PASS | physical domain is fixed independently; one diagnostic does not create ontology |
| C15 program-order permutation | PASS | syntax is not time |
| C16 actual record/absent microtrajectory | PASS | actuality scopes separate |
| C17 readable fiber | PASS | new reader refines the domain and classes |
| C18 simplicity selector | PASS | no invariant physical principle follows from code length |

## 10. Hostile attacks 1--42

| Attack | Disposition |
|---:|---|
| 1 | survives: one terminal reader is not the equivalence test |
| 2 | survives: ancillary continuations are quantified |
| 3 | survives: separation is fixed independently of a representative |
| 4 | survives on image: quotient proof includes the inverse there |
| 5 | survives operationally: tensor/adaptive wiring are included |
| 6 | survives: different boundary types are never merged by a scalar coincidence |
| 7 | survives: the registered reader family is fixed before quotienting |
| 8 | survives with printed scope: no global inverse on extra native objects |
| 9 | survives: many-to-one deletion is not coordinate gauge |
| 10 | survives: idle physicality is not asserted without a discriminator |
| 11 | survives: no uniform law is assigned without a base measure |
| 12 | survives: maximum entropy is coordinate/constraint relative |
| 13 | survives in words, but the preparation-correlated variable is not typed over $\mathcal Q$; semantic repair required |
| 14 | survives: declared fiber kernels do not depend on unperformed future settings |
| 15 | survives: every constructed $Z$ receives an explicit law |
| 16 | survives for the static/dynamic controls; no lookup table is used |
| 17 | survives: complete profiles retain phase |
| 18 | survives: realification prints $J$ and the doubled/global carrier |
| 19 | survives at printed scalar scope: source-independence premises are distinguished |
| 20 | survives: local tomography is an added reconstruction premise |
| 21 | survives: complex scalar ontology is not selected |
| 22 | survives: real coordinates retain equivalent phase structure |
| 23 | survives: Wigner uniqueness is not used as an ontology theorem |
| 24 | survives: reconstruction assumptions remain inputs |
| 25 | survives for records: positivity is not universal noncontextuality; the formal contextual representation class still needs repair |
| 26 | survives: no-signalling is not Bell locality |
| 27 | FAILS structurally: physical procedure context is discussed but absent from the source category of $J_R$ |
| 28 | survives: minimal dilation size is restricted-class only |
| 29 | survives: Markov lower bounds are not applied to non-Markovian realizers |
| 30 | survives: complexity is not an ontology selector |
| 31 | survives: equivalence is exact |
| 32 | survives: one memory realization is not called unique |
| 33 | survives: an actual record is not a microtrajectory |
| 34 | survives: normalization is not actualization |
| 35 | survives: decoherence is not outcome selection |
| 36 | survives: slot order remains laboratory syntax/type |
| 37 | survives: a tensor factor is not space |
| 38 | survives: no hidden order is inserted |
| 39 | survives: discrete fibers are controls, not spacetime atoms |
| 40 | survives: equivalence is not evidence for ISP truth |
| 41 | survives: underdetermination does not make all ontologies equally plausible |
| 42 | survives: no new physical postulate is inserted into the candidate result |

## 11. Exact quantifiers and surviving theorem classes

| Result | Surviving quantifier and class |
|---|---|
| congruence | every representation well defined on the frozen finite-dimensional, finite-slot, definite-order operational category; all compatible ancillary continuations |
| quotient | the $\mathcal Q$-reachable image only; exact equivalence, not approximate equality |
| fibers | finite, countable, and standard-Borel idle fibers with measurable prefix kernels; preparation/transformation-context fibers not established without a procedure category |
| no-selection | invariants natural under the explicitly admitted inflation and forgetting maps; not every physically meaningful quantity |
| phase | finite-dimensional states/process testers with the complete continuation family |
| scalar | exact realification of matched finite complex experiments, with global-$J$ and tensor/source rules exposed |
| contextuality | standalone no-go witnesses with the printed affinity, distinguishability, sharp-product, independence, and factorization premises; bridge to `Rep(Q)` defective |
| resource minima | only within fixed channel, task, cut, Markov, tensor, and representation classes |
| records | registered typed record values with independently fixed future readers |
| actuality | quotient-record postulate only; no selector or microscopic completion |
| Barandes | primary ontology remains a possible hypothesis; full Q0--Q3 adequate completion not constructed here |
| order/geometry | supplied laboratory order only; no time, space, dimension, or metric conclusion |

## 12. Full 17-coordinate product

```text
contract       P02-ADEQUATE-REPRESENTATION-CLASS-DEFECTIVE
               (missing prequotient procedure/context category)
quotient       P02-OPERATIONAL-QUOTIENT-CANONICAL-SCOPED
               (well-defined representations on the reachable image)
naturality     P02-QUOTIENT-NATURALITY-CONSTRUCTED-SCOPED
fibers         P02-ONTOLOGY-FIBERS-INCOMPLETE
               (idle fibers constructed; procedure-context fibers untyped)
selection      P02-OPERATIONAL-NOSELECTION-THEOREM-SCOPED
               (conditional on admitted inflation/reduction naturality)
phase          P02-PHASE-COMPLETE-PREDICTIVE-STATE-FORCED
scalar         P02-COMPLEX-SCALAR-ONTOLOGY-REPRESENTATION-NONUNIQUE
positivity     P02-POSITIVE-RECORD-LAWS-SURVIVE
context        P02-NONCONTEXTUAL-MICROONTOLOGY-NOGO-WITH-PRINTED-PREMISES
               + P02-CONTEXTUAL-REPRESENTATION-BRIDGE-FAILED
bell           P02-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
memory         P02-RESOURCE-INVARIANTS-CLASSIFIED-SCOPED
gauge          P02-GAUGE-REDUNDANCY-PHYSICAL-DIFFERENCE-CLASSIFIED-SCOPED
record         P02-OPERATIONAL-RECORD-INVARIANT
actuality      P02-RECORD-ACTUALITY-POSTULATED
               + P02-MICROACTUALITY-UNCONSTRUCTED
barandes       P02-BARANDES-ONTOLOGY-ADMISSIBLE-BUT-UNCONSTRUCTED-AND-UNSELECTED
discriminator  P02-EXTRA-ONTOLOGY-DISCRIMINATOR-NONE-FOR-CONSTRUCTED-IDLE-FIBERS
ontology       P02-ONTOLOGY-UNDERDETERMINED-AND-CONTRACT-INCOMPLETE
overall ceiling
               P02-CANONICAL-QUOTIENT-WITH-PHASE-COMPLETE-RESIDUE
```

The submitted rung
`P02-CANONICAL-QUOTIENT-WITH-UNSELECTED-ONTOLOGY-FIBERS` is not earned by the
frozen object because the class over which its contextual ontology claim is
made is not yet coherently typed.

## 13. Verdict, repair boundary, and implementation wall

**REVISE.** The central quotient and phase-residue results survive, but the
full ontology-fiber classification requires changed mathematics.

A bounded honest repair would:

1. define a typed procedure category $\mathcal P$ retaining preparation,
   transformation, measurement, and apparatus contexts;
2. define the complete-continuation quotient
   $q:\mathcal P\to\mathcal Q$;
3. place ontological representations and $\Gamma_R$ on $\mathcal P$, so
   operationally equivalent procedures may have different ontic images;
4. restate the representation morphisms, fiber theorem, and no-selection
   theorem relative to that two-level structure;
5. rerun the affine/monoidal/no-future-setting checks there; and
6. either construct a complete Barandes-style adequate packet or demote its
   row to admissible but unconstructed.

Those changes affect definitions, theorem domains, and product coordinates;
they require explicit post-adjudication authorization under the frozen
protocol. No candidate edit is made here.

No implementation can change this verdict. Python, Rust, or any other code can
only instantiate a well-defined source category; it cannot make a functor
distinguish equal source arrows or construct a missing microscopic referent.

The bound candidate, pin, audit, adjudication, and charter bytes remain
unchanged. This report is left **unstaged and uncommitted** on handoff.
