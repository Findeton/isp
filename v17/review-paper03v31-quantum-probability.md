# Paper 03 v3.1 hostile review — Seat Q

## Quantum instruments, probability, histories, and Bell

Date: 2026-08-22

Status: **FROZEN INDEPENDENT REPORT**

## 0. Verdict

```text
VERDICT: ACCEPT-WITH-SCOPE
FIRST DECISIVE SEMANTIC COUNTEREXAMPLE: none
EARLIEST SUPPORTED RUNG:
P03V31-CAUSAL-FRONTIER-INTEGRATED-DUAL-SEMANTICS-CONSTRUCTED
STRONGEST SUPPORTED RUNG:
P03V31-RELATIVISTIC-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

The frozen candidate constructs the promised hybrid operational
representation at its declared scope. In particular, it does not replace a
complete record-bearing instrument by either one branch or its nonselective
restriction; it keeps exact samples in `Ev`; it represents only dominated
continuous ensembles as normal hybrid states; and its path theorem is an
ensemble-level induction over compatible primitive pairs. The continuous
result is conditional admission, not a theorem that NEP alone supplies all
of the remaining data. Generic nonatomic point restart, an infinite-history
law, actuality, a local Bell ontology, emergent spacetime, and gravity remain
unconstructed.

Two wording scopes should be made explicit in adjudication but do not change
an object, map, probability, target, product coordinate, or rung:

1. For a path beginning at a non-source boundary, iterating `Ev` produces a
   history **kernel**. It becomes a probability measure only after fixing an
   input predictive value \(x\) or admitted input law \(\Lambda\). Thus the
   notation \(\Gamma_p\) in Definition 18.1 is read as the already supplied
   conditional family \(\Gamma_{p,x}\), or as
   \(\Gamma_{p,\Lambda}\) after integration. No parameter-free history law is
   selected.
2. Definition 8.4(8) is an admission proof obligation. Theorem 8.5 and the
   continuous arm of Theorem 11.2 therefore establish closure of the admitted
   category; they do not derive ensemble compatibility from NEP, target
   landing, or posterior measurability alone.

These are binding interpretations of the printed conditional quantifiers,
not repairs to v2 physics.

## 1. Authentication, chronology, and independence

The review began at exact HEAD
`1bade102ed6c3b9537b3af155e403d1cec0fd86e`; its parent is
`7161c3cca1d904d25601e7e6af8350c32f1ba988`. The protocol commit adds only
the result-neutral hostile-review protocol to that parent. All bound files
were authenticated before scientific judgment.

| Bound artifact | SHA-256 authenticated | LF lines | bytes |
|---|---:|---:|---:|
| `v17/note-paper03v31-hostile-review-protocol.md` | `66342f937de99b4a8450f1e8fe10c0156af13f697ad488a0f6495d8caeba7094` | 558 | 22604 |
| `v17/note-paper03v31-integrated-hybrid-semantics-pin.md` | `b7ec12ad25c3ac6327cb242ad39ba03e1af541e544f11d32cb86dbce908b5fca` | 760 | 30236 |
| `v17/note-paper03v31-pin-audit-category.md` | `86eb3e42782e36685e5017b74fd790215b5296287a96bbb5d72d420f80d8a761` | 827 | 37425 |
| `v17/note-paper03v31-pin-audit-quantum.md` | `a25cf562d4f25b8fccebd3546e19ecccfde8fe3aac975ae047051c2c2319cb78` | 745 | 36220 |
| `v17/note-paper03v31-pin-audit-adjudication.md` | `613c006a5933db29cd29e3d1c6e3594fa044c4f1fb150d6f904882768588c96f` | 464 | 19099 |
| `v17/paper-03v31-integrated-hybrid-relativistic-adequacy.md` | `f808455f4ad240e2cd2751eccad32aa59ecb6e941caba8e9d4324fda3959b533` | 1632 | 62503 |
| `v17/note-paper03v31-construction-audit.md` | `7341381b74c1f92540d4d2a1fc386fdec3de0886e26fd61803276dae7307a992` | 570 | 25539 |
| `v17/note-paper03v2-hostile-review-adjudication.md` | `74303ddd93b4aac35d3368760da4a0ad3d442570cb16320467076aa5f93ea358` | 476 | 22617 |
| `v17/note-paper02v2-hostile-review-adjudication.md` | `37e1ada87f17723c248896f77ce03012d809f088632abb50ed01d1b166bed135` | 381 | 19166 |
| `v17/note-paper01-hostile-review-adjudication.md` | `3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1` | 314 | 13844 |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | 476 | 21268 |

I read the complete immutable corpus, reconstructed the candidate rather
than treating its author audit as evidence, and consulted the relevant
primary sources listed in Section 11 below. I did not inspect, name, infer,
or communicate about any sibling review. My sole writable path was this
report. I did not edit an authority, candidate, ledger, or evaluator and did
not stage or commit any file.

The authenticated chronology is:

```text
Paper 03 v2 terminal REVISE
  -> v3 pin rejected before construction
  -> sole v3.1 integrated-semantics pin
  -> two independent pin audits
  -> joint pre-construction adjudication
  -> one mathematics construction
  -> result-neutral construction audit
  -> frozen hostile-review protocol
  -> this mutually blind report
```

## 2. Independent reconstruction

### 2.1 Finite and integrated boundary semantics

`FINITE/ATOMIC-EXACT-CONTROL` — For a finite result set, the hybrid algebra
is the direct sum \(\bigoplus_r\mathcal A\). Evaluation in a retained branch
is a normal central-summand functional. If
\(\mathcal J_r:\mathcal A_E\to\mathcal A_D\) are normal CP and
\(\sum_r\mathcal J_r(1)=1\), then

$$
\widehat{\mathcal J}((A_r)_r)=\sum_r\mathcal J_r(A_r)
$$

is normal, CP at every matrix level, and unital. Inserting into one central
summand gives a generally nonunital branch; diagonal restriction gives the
nonselective channel. Neither retains the complete classical output.

`CONDITIONAL-ON-NAMED-HYPOTHESES` — At an integrated boundary, an admitted
law \(\Lambda\) has record marginal
\(\eta=\mathsf r_*\Lambda\ll\nu\). With \(h=d\eta/d\nu\) and the supplied
strongly measurable conditional normal-state barycenter \(\bar\rho_r\),

$$
g(r)=h(r)\bar\rho_r\in L^1(R,\nu;\mathcal A_*) ,
\qquad \int\lVert g(r)\rVert\,d\nu=1.
$$

Hence

$$
\operatorname{Ens}(\Lambda)(F)
=\int\langle g(r),F(r)\rangle\,d\nu(r)
$$

is positive, normalized, normal, and independent of the representative of
the \(L^\infty\) class. The strong predual field is a genuine admission
hypothesis; a scalar dominated marginal alone would not establish it.

`REFUSAL/NONIMPLICATION` — If \(\nu(\{r\})=0\), point evaluation is not a
well-defined functional on \(L^\infty(R,\nu)\), and therefore cannot be a
normal hybrid restart state. This does not delete the exact sample \(r\)
from the standard-Borel `Ev` space. A positive event, or a declared atom,
can be conditioned; a null singleton cannot.

### 2.2 Null ideals, instruments, and feedback

`FOR-EVERY-ADMITTED-PACKET` — A deterministic pullback \(u\mapsto u\circ f\)
is representative independent exactly when \(f_*\nu_D\ll\nu_E\). A
stochastic record kernel must send every target null set to probability zero
for \(\nu_D\)-almost every source record. Both conditions compose. Output
ensemble closure is separately required at every primitive, so the
finite-path induction never silently exits its state class.

`FINITE/ATOMIC-EXACT-CONTROL` — For a binary instrument followed by the
record-controlled policy \(0\mapsto I,1\mapsto X\), the complete Heisenberg
composition is

$$
\mathcal J_0(A)+\mathcal J_1(XAX).
$$

A branch-only replacement is nonunital/incomplete. A nonselective
\(\mathcal J_0+\mathcal J_1\) replacement has erased the guard and cannot in
general reproduce this expression.

`CONDITIONAL-ON-NAMED-HYPOTHESES` — A retained continuous instrument is
admitted only with its countably additive normal CP measure, one
state-independent normal UCP target-landing extension, NEP or a stronger
result, one jointly measurable posterior kernel, deterministic and
stochastic null-ideal preservation, state/ensemble closure, and the exact
all-ensemble compatibility identity. This is deliberately stronger than
statewise posterior existence. A measurable decomposable feedback field
then composes at ensemble level; a.e.-equal policies have equal predictions
for every reachable dominated input without becoming pointwise-equal frozen
kernels.

`EXISTS-ONE-NAMED-COMPARATOR` — For the uniform qubit/Lebesgue control,

$$
\widehat{\mathcal J}(F)=\int_0^1U^*F(r)U\,dr
$$

is normal UCP and target landing. For each normal input state \(\rho\) and
each hybrid reader \(F\), the `Ev` side is

$$
\int_0^1(\rho\circ\operatorname{Ad}_{U^*})(F(r))\,dr,
$$

which equals the Heisenberg evaluation
\(\rho(\widehat{\mathcal J}(F))\). With feedback
\(V_r=e^{-irZ}\), both sides become
\(\int\rho(U^*V_r^*AV_rU)\,dr\). The example is nonvacuous as an exact
continuous record and control; it is not an informative measurement, a QFT
construction, or a point restart.

### 2.3 One-step and path duality

`FOR-EVERY-ADMITTED-PACKET` — A primitive physical arrow is paired with its
exact kernel \(K_g\) and normal UCP hybrid map \(\Phi_g\). Compatibility is
equality of normal states on the complete target hybrid algebra:

$$
\operatorname{Ens}_E(\Lambda K_g)
=\operatorname{Ens}_D(\Lambda)\circ\Phi_g
$$

for every admitted input ensemble, not equality for one state, scalar
outcome, or incomplete reader family. Identity, preparations, channels,
finite instruments, record transformations, guards, trusted randomization,
discard, coarse-graining, localized couplings, and admitted continuous
instruments each use their named duality and closure obligation.

For \(p:D\to E\) and a compatible next primitive \(g:E\to F\), the induction
is exact:

$$
\begin{aligned}
\operatorname{Ens}_F(\Lambda\operatorname{Ev}(p)K_g)
&=\operatorname{Ens}_E(\Lambda\operatorname{Ev}(p))\circ\Phi_g\\
&=\operatorname{Ens}_D(\Lambda)\circ
  \operatorname{Heis}(p)\circ\Phi_g.
\end{aligned}
$$

Kernel associativity and reverse Heisenberg composition give every admitted
finite path. No limiting/infinite-stream theorem follows.

### 2.4 Histories, memory, and division

`FOR-EVERY-ADMITTED-PACKET` — Starting from a specified input \(x\), or an
admitted input law \(\Lambda\), iterating complete normalized kernels gives a
normalized measure on finite cylinders. Integrating a complete suffix gives
one at every preceding step, hence the performed-prefix marginal. The same
primitive instrument data identify registered cylinder/reader laws. Exact
continuous sample values remain sample coordinates even though their
singleton hybrid evaluations may be undefined.

Equal final `Ens` states need not imply equal full history-cylinder laws.
The candidate does not identify them: registered history readers and every
future-readable decomposition/memory coordinate must remain in the boundary
or the relevant continuation is refused. Future sufficiency concerns all
licensed future reader profiles; it is not conferred by a frontier, one
record, conditioning, or normalization.

`REFUSAL/NONIMPLICATION` — The positive history is global, contextual,
memory-bearing, packet-indexed, and unselected. It is not a local hidden
variable, an actual trajectory, or an ontology. Adding an independent idle
fiber preserves registered predictions and therefore proves only scoped
nonselection.

### 2.5 Relativistic operational claims

`CONDITIONAL-ON-NAMED-HYPOTHESES` — No-signalling uses the complete
nonselective localized operation and the named system-probe localization
theorem, not commutativity alone. Selected positive-support subensembles may
steer; comparison requires the classical record. Bell factorization also
requires a setting-independent source and conditional outcome factorization.
The finite split-qubit \(2\sqrt2\) control and existential QFT Bell results do
not imply a universal localized realization of every ideal Bell observable.

Certified concurrency requires equality of complete frozen kernels and
complete Heisenberg maps, with record permutation, multiplicity, source, and
memory lineage, in every reachable adaptive context. Integrated a.e.
equality, one-state equality, or one initial square is insufficient. The
slot partial order is declared laboratory protocol, not microscopic time.

## 3. V31-T1--V31-T24 disposition

The status vocabulary is exactly the protocol vocabulary.

| Target | Status | Quantifier and independent reason |
|---|---|---|
| V31-T1 | `CONSTRUCTED` | `FINITE/ATOMIC-EXACT-CONTROL`: inherited finite lower-set path category; typed endpoints exclude timelike reversal. |
| V31-T2 | `CONDITIONAL` | `FOR-EVERY-ADMITTED-PACKET`: one tagged object contains boundary, regime, algebra, class, sample, ensemble, state field, and memory data. |
| V31-T3 | `CONSTRUCTED` | `FINITE/ATOMIC-EXACT-CONTROL`: direct-sum complete instrument is normal UCP. |
| V31-T4 | `CONDITIONAL` | `FINITE/ATOMIC-EXACT-CONTROL`: finite points exact; countable restart only at declared atoms. |
| V31-T5 | `CONDITIONAL` | `INTEGRATED-ENSEMBLE-ONLY`: common domination and supplied strong conditional predual field make `Ens` normal. |
| V31-T6 | `REFUSED` | `REFUSAL/NONIMPLICATION`: generic nonatomic point evaluation/restart is not well defined. |
| V31-T7 | `CONDITIONAL` | `CONDITIONAL-ON-NAMED-HYPOTHESES`: each deterministic map owes nonsingularity; composition then closes. |
| V31-T8 | `CONDITIONAL` | `CONDITIONAL-ON-NAMED-HYPOTHESES`: continuous instruments owe all eight admission items; NEP alone is insufficient. |
| V31-T9 | `CONSTRUCTED` | `FOR-EVERY-ADMITTED-PACKET`: tagged normal-UCP hom-sets, identities, matched composition, and skip distinction form a category. |
| V31-T10 | `CONSTRUCTED` | `FOR-EVERY-ADMITTED-PACKET`: reverse composition defines the contravariant `Heis` functor. |
| V31-T11 | `CONDITIONAL` | `INTEGRATED-ENSEMBLE-ONLY`: all-reader primitive equality plus class closure inducts over every finite admitted path. |
| V31-T12 | `CONDITIONAL` | `INTEGRATED-ENSEMBLE-ONLY`: measurable decomposable policy, target landing, memory, and class closure required. |
| V31-T13 | `CONSTRUCTED` | `FOR-EVERY-ADMITTED-PACKET`: discard/coarse targets remove the unavailable coordinate; later fine read is untyped. |
| V31-T14 | `CONSTRUCTED` | `FINITE/ATOMIC-EXACT-CONTROL`: positive events and atoms condition; null singleton normalization is refused. |
| V31-T15 | `CONDITIONAL` | `CONDITIONAL-ON-NAMED-HYPOTHESES`: only full packet transport, including classes, kernels, fields, memory, sources, and multiplicity. |
| V31-T16 | `CONDITIONAL` | `FOR-EVERY-ADMITTED-PACKET`: operational congruence is proved on the reachable constructor-complete context family only. |
| V31-T17 | `CONDITIONAL` | `FOR-EVERY-ADMITTED-PACKET`: exchange requires complete exact two-layer certificate. |
| V31-T18 | `CONDITIONAL` | `CONDITIONAL-ON-NAMED-HYPOTHESES`: schedule equality only if every reachable co-enabled swap is certified. |
| V31-T19 | `CONDITIONAL` | `CONDITIONAL-ON-NAMED-HYPOTHESES`: localized nonselective no-signalling, selected steering, and Bell premises remain distinct. |
| V31-T20 | `CONSTRUCTED` | `FOR-EVERY-ADMITTED-PACKET`: finite conditional history kernels are normalized and prefix coherent; fixing input gives the printed measure. |
| V31-T21 | `REFUSED` | `REFUSAL/NONIMPLICATION`: no universal density matrix, touching split, gauge factorization, interacting model, or UV theorem. |
| V31-T22 | `CONSTRUCTED` | `REFUSAL/NONIMPLICATION`: record, conditioning, future-sufficient division, and actuality are distinct predicates. |
| V31-T23 | `UNCONSTRUCTED` | `UNCONSTRUCTED`: no selected Barandes configuration space, transition law, state, or trajectory. |
| V31-T24 | `UNCONSTRUCTED` | `UNCONSTRUCTED`: ontology, internal time, spacetime emergence, dynamics of geometry, and gravity absent. |

## 4. Quantifier ledger

| Claim family | Required quantifier | What is not inferred |
|---|---|---|
| finite direct sums, branches, nonselective restriction, I/X | `FINITE/ATOMIC-EXACT-CONTROL` | universal continuous or QFT implementation |
| atomic point states | `FINITE/ATOMIC-EXACT-CONTROL` | evaluation at a generic nonatomic sample |
| `Ens`, feedback, path duality | `INTEGRATED-ENSEMBLE-ONLY` | exact pointwise equality or canonical null posterior |
| integrated boundary/instrument/category | `FOR-EVERY-ADMITTED-PACKET` | admission of every CP instrument or state |
| continuous instrument theorem | `CONDITIONAL-ON-NAMED-HYPOTHESES` | compatibility from NEP alone |
| uniform qubit/Lebesgue control | `EXISTS-ONE-NAMED-COMPARATOR` | informative measurement or localized QFT model |
| localized AQFT instrument/no-signalling | `CONDITIONAL-ON-NAMED-HYPOTHESES` | claim for arbitrary CP maps |
| split-qubit Bell value | `EXISTS-ONE-NAMED-COMPARATOR` | universal QFT probe realization |
| QFT Bell theorem | `CONDITIONAL-ON-NAMED-HYPOTHESES` | Bell locality, measurement independence, or actual ontology |
| full packet transport | `CONDITIONAL-ON-NAMED-HYPOTHESES` | forward state extension along a proper embedding |
| null-point, infinite-stream, ontology, gravity walls | `REFUSAL/NONIMPLICATION` or `UNCONSTRUCTED` | any positive physical construction |

## 5. C1--C34 two-way controls

| ID | Positive arm | Hostile arm | Independent disposition |
|---|---|---|---|
| C1 | complete finite direct-sum record | branch list | `PASS`: only the sum map on the central direct sum is UCP and complete. |
| C2 | binary result then I/X | nonselective sum as guard | `PASS`: only the retained record yields \(\mathcal J_0(A)+\mathcal J_1(XAX)\). |
| C3 | complete arrow unital | each branch unital | `PASS`: only \(\sum_s\mathcal J_s(1)=1\) is required. |
| C4 | atomic point normal | nonatomic evaluation | `PASS`: central atom versus representative-dependent point value. |
| C5 | dominated joint law | nonatomic Dirac | `PASS`: the latter is outside the admitted ensemble class. |
| C6 | a.e. posterior field | canonical null posterior | `PASS`: only the former is operationally defined. |
| C7 | one common boundary class | per-route classes | `PASS`: the latter are different tagged objects. |
| C8 | nonsingular pullback | merely measurable constant map | `PASS`: target-null preimage test rejects the latter. |
| C9 | graph-compatible append | blind product class | `PASS`: an append graph needs a dominating target class. |
| C10 | equivalent measure classes | singular replacement | `PASS`: only equivalence preserves the tagged null ideal. |
| C11 | faithful technical domination | physical prior/selector | `PASS`: no state or actuality is selected. |
| C12 | tagged skip | empty identity path | `PASS`: distinct endpoints/slot consumption survive an identical underlying map. |
| C13 | present result guards future | future result guards past | `PASS`: the hostile source lacks the record. |
| C14 | measurable decomposable field | nonmeasurable/unbounded field | `PASS`: the hostile policy is not a normal decomposable arrow. |
| C15 | all future memory exposed | hidden cache | `PASS`: refine the boundary or refuse the continuation. |
| C16 | discard removes coordinate | later read of it | `PASS`: hostile read is absent from target type. |
| C17 | positive-event conditioning | null singleton normalization | `PASS`: only the former defines a normal conditional state. |
| C18 | all-reader state identity | one scalar outcome | `PASS`: compatibility is equality on the complete hybrid algebra. |
| C19 | complete map/kernel exchange | one-state equality | `PASS`: the latter cannot certify a natural transformation or all-context swap. |
| C20 | all reachable swaps certified | one initial square | `PASS`: adjacent-swap proof needs each reachable adaptive context. |
| C21 | explicit output permutation | silent record reorder | `PASS`: hostile certificate is incomplete. |
| C22 | exposed product source | hidden correlation | `PASS`: the latter is a different joint mechanism. |
| C23 | class/field/null/multiplicity transport | coordinate relabel only | `PASS`: hostile transport is not full packet transport. |
| C24 | full packet isomorphism | proper embedding state push | `PASS`: only pullback is canonical for the latter. |
| C25 | nonselective remote marginal | selected steering | `PASS`: conditioning and classical-record cost distinguish them. |
| C26 | physical KMS/material frame | law-level foliation | `PASS`: contingent state covariance is not fixed-state invariance. |
| C27 | normal type-III functional | universal density/trace | `PASS`: core formulas require neither trace nor regional density matrix. |
| C28 | split with collar | touching/gauge tensor split | `PASS`: hostile factorization is refused. |
| C29 | record retained by typed future | erasure/discard | `PASS`: persistence is grammar relative. |
| C30 | future-sufficient complete boundary | frontier/sample alone | `PASS`: omitted memory/source gives the hostile countermodel. |
| C31 | law of possible records | actual sample selection | `PASS`: no actuality map is present. |
| C32 | finite laboratory slot protocol | microscopic event web/time | `PASS`: no ontic promotion is made. |
| C33 | declared comparator spacetime | emergent geometry | `PASS`: comparator remains an input. |
| C34 | frozen v2 physical input | parameter retuning | `PASS`: construction only adds representation data and admission tests. |

## 6. Mandatory attacks 1--52

| Attack | Result and exact reason |
|---:|---|
| 1 | `PASS`: two representatives differing at one Lebesgue-null point refute uniform point evaluation. |
| 2 | `PASS`: domination makes a null representative swap invisible to every admitted `Ens`. |
| 3 | `PASS`: a nonatomic Dirac input is outside the integrated ensemble class, though the exact sample remains in `Ev`. |
| 4 | `PASS`: a positive coarse event has a normalized conditional ensemble. |
| 5 | `PASS`: a declared atom gives the exact central-summand normal state. |
| 6 | `PASS`: no sigma-finite class dominates uncountably many mutually singular routes; split schemas or refuse. |
| 7 | `PASS`: constant Lebesgue pullback produces a singular delta and fails nonsingularity. |
| 8 | `PASS`: blind product measure makes a deterministic append graph null; a graph-dominating class or new schema is required. |
| 9 | `PASS`: equivalent classes preserve a null ideal; singular replacement changes the tagged object. |
| 10 | `PASS`: a faithful technical state/class is not promoted to a prior or selector. |
| 11 | `PASS`: a continuous instrument without exact NEP-or-stronger data is refused from retained continuous control. |
| 12 | `PASS`: approximate NEP gives only an approximate comparator, never exact admission. |
| 13 | `PASS`: an ambient-only extension that misses the target hybrid algebra is refused. |
| 14 | `PASS`: statewise posteriors without one jointly measurable kernel do not define `Ev`. |
| 15 | `PASS`: equal `Ens` with delayed decomposition access forces boundary refinement or refusal. |
| 16 | `PASS`: equality of scalar record marginals cannot hide different quantum predual fields from all-reader duality. |
| 17 | `PASS`: the complete finite instrument gives the exact I/X controlled law. |
| 18 | `PASS`: a branch is generally nonunital and lacks the complete central output. |
| 19 | `PASS`: the nonselective channel erases the record needed by the adaptive guard. |
| 20 | `PASS`: old record fibers are retained unless a separately typed discard consumes them. |
| 21 | `PASS`: a skip consumes a slot and has different tags even if its algebra map is identity. |
| 22 | `PASS`: mismatched target schemas are not parallel arrows. |
| 23 | `PASS`: future-result guard is untyped at the source frontier. |
| 24 | `PASS`: read after discard is absent from the target interface. |
| 25 | `PASS`: fine read after coarse-graining is absent unless separately retained. |
| 26 | `PASS`: a nonmeasurable continuous guard is not an admitted decomposable map. |
| 27 | `PASS`: a singular preparation that exposes a previously null version requires a new class/schema; it cannot alter the old prediction. |
| 28 | `PASS`: `Ens` integrates evaluated normal states, and the predual calculation establishes the functional. |
| 29 | `PASS`: equality for one reader is weaker than equality as normal states on the complete algebra. |
| 30 | `PASS`: presentation transport carries occurrence multiplicity and does not collapse occurrences. |
| 31 | `PASS`: transport omitting the measure class is not a full packet isomorphism. |
| 32 | `PASS`: a proper embedding canonically pulls states back but does not push them forward. |
| 33 | `PASS`: a one-state exchange equality is not a complete map/kernel certificate. |
| 34 | `PASS`: omitting the output permutation leaves the exchange certificate incomplete. |
| 35 | `PASS`: a hidden correlated source changes the joint mechanism and invalidates the product-source premise. |
| 36 | `PASS`: certification only in the initial context cannot prove adaptive schedule equality. |
| 37 | `PASS`: uncertified incomparable serializations remain distinct paths. |
| 38 | `PASS`: antichain status alone gives no schedule theorem. |
| 39 | `PASS`: selected steering is not a change of the remote nonselective marginal. |
| 40 | `PASS`: microcausal commutation alone is not the complete operation-locality identity. |
| 41 | `PASS`: existential QFT Bell observables are not claimed to have a universal exact localized-probe realization. |
| 42 | `PASS`: normal states on type-III algebras are not universally represented by intrinsic regional density matrices. |
| 43 | `PASS`: arbitrary touching/gauge tensor splits are refused. |
| 44 | `PASS`: a KMS/material/apparatus rest frame is contingent physical data, not a fundamental scheduling foliation. |
| 45 | `PASS`: record availability ends under typed erasure, discard, or coarse-graining. |
| 46 | `PASS`: a continuous sample is not a division; future sufficiency and the point-state split remain separate. |
| 47 | `PASS`: conditioning updates predictions and does not actualize an outcome. |
| 48 | `PASS`: slot count and record count are not promoted to duration or volume. |
| 49 | `PASS`: the hybrid algebra/history is explicitly representation-level and unselected. |
| 50 | `PASS`: no v16 geometry, selector, FLRW carrier, or fusion input enters the construction. |
| 51 | `PASS`: no physical parameter, instrument probability, state update, or source is retuned. |
| 52 | `PASS`: downstream time/spacetime/gravity work remains closed. |

## 7. Fresh Seat-Q attacks

### Q1 — complete binary instrument under delayed I/X

`FINITE/ATOMIC-EXACT-CONTROL` — Choose branch maps for which
\(\mathcal J_0(A)\neq\mathcal J_0(XAX)\) and
\(\mathcal J_1(A)\neq\mathcal J_1(XAX)\). The complete arrow followed by the
guard yields \(\mathcal J_0(A)+\mathcal J_1(XAX)\). A branch-only map loses
normalization and one alternative; a nonselective map cannot decide which
conjugation applies. The candidate passes.

### Q2 — continuous qubit/Lebesgue reader-by-reader reconstruction

`EXISTS-ONE-NAMED-COMPARATOR` — For a simple field
\(F=\sum_k A_k\chi_{\Delta_k}\), both sides equal
\(\sum_k\lambda(\Delta_k)\rho(U^*A_kU)\). Normal monotone convergence extends
the equality to every positive \(F\in M_2\bar\otimes L^\infty[0,1]\), then
linearity gives every reader. No point evaluation is used. The candidate
passes.

### Q3 — continuous CP instrument with no NEP/target landing

`REFUSAL/NONIMPLICATION` — A countably additive CP instrument whose only
extension is state dependent, ambient, or nonnormal does not enter the
retained category. Its probability measure may exist, but the v3.1 hybrid
arrow and exact feedback theorem do not. The refusal is correct.

### Q4 — statewise posterior versions without a joint kernel

`REFUSAL/NONIMPLICATION` — Existence of a posterior version for each input
state does not supply one measurable \(K(x,dr\,d\rho')\). State-dependent
choices cannot compose into the frozen Markov functor. Definition 8.4(5)
blocks the attack.

### Q5 — one primitive escapes the target ensemble class

`REFUSAL/NONIMPLICATION` — Let an admitted input be sent to a singular target
record marginal or to a posterior field outside the declared state class.
The first step may have scalar probabilities but the next induction line is
undefined. Proposition 6.4 refuses the primitive instead of extrapolating
Theorem 11.3.

### Q6 — equal barycentric states with delayed hidden-memory read

`FOR-EVERY-ADMITTED-PACKET` — Two preparation ensembles can have the same
density operator but different decompositions. A later apparatus that reads
the preparation label distinguishes them only if that label is a real input
port/memory coordinate. The candidate requires it to be exposed; otherwise
the continuation is refused. It does not identify ontic decompositions from
equal `Ens` states.

### Q7 — positive coarse event with null constituent points

`INTEGRATED-ENSEMBLE-ONLY` — For uniform \(r\in[0,1]\), the interval
\([0,1/2]\) has positive probability and conditions normally, while each
singleton in it remains null. Conditioning on the interval does not promote
any contained point to a normal hybrid restart. The candidate passes.

### Q8 — post-hoc null posterior selection

`REFUSAL/NONIMPLICATION` — Two Borel posterior versions can differ on a null
record. Choosing the favorable value after that record is requested is not
part of the frozen packet and would be detectable only through a singular new
preparation. The old dominated ensemble predictions remain version
independent.

### Q9 — steering misreported as nonselective signalling

`CONDITIONAL-ON-NAMED-HYPOTHESES` — In an entangled control, conditioning on
Alice's retained event changes Bob's conditional state; summing Alice's
complete outcome instrument leaves Bob's registered spacelike marginal
unchanged. The classical outcome is required to sort the subensemble. The
candidate states precisely these different predicates.

### Q10 — Bell comparator with measurement dependence

`REFUSAL/NONIMPLICATION` — If \(\lambda\) is correlated with \(x,y\), or if the
two probes share an undeclared source, an observed CHSH value does not test
the printed setting-independent Bell factorization. The candidate records
source and correlation lineage and treats the altered source as a different
mechanism.

### Q11 — equal final hybrid states, unequal history cylinders

`FOR-EVERY-ADMITTED-PACKET` — Two erasing procedures can reach the same final
hybrid state while having distinct earlier retained cylinders. Final-state
equality proves only future-reader equality after the erasing boundary; it
does not identify their history measures. The candidate keeps exact kernels
and registered history contexts separate from the final `Ens` state, so the
attack does not collapse histories.

### Q12 — finite induction promoted to an infinite stream

`UNCONSTRUCTED` — Normalization of every finite cylinder does not by itself
establish one infinite object with the required topology, tightness,
projective consistency across all packet changes, or a limiting normal
hybrid state. Corollary 11.4 expressly refuses the promotion.

### Q13 — compatibility hidden inside admission

`CONDITIONAL-ON-NAMED-HYPOTHESES` — Construct a NEP instrument with a
measurable posterior and target landing, but choose an `Ev` posterior update
inconsistent with the Heisenberg instrument. Items 1--7 alone do not force
the printed identity. Item 8 rejects this pairing. Therefore Theorem 8.5 is
a valid closure theorem for certified pairs, but not an independent
derivation of compatibility from NEP. This is the principal scope bound.

### Q14 — a path without a fixed initial law

`REFUSAL/NONIMPLICATION` — A composite Markov kernel
\(K_p:X_D\to\operatorname{Prob}(X_E)\) is not a single probability measure
until \(x\in X_D\) or \(\Lambda\in\mathfrak E_D\) is fixed. Reading
\(\Gamma_p\) as \(\Gamma_{p,x}\) or \(\Gamma_{p,\Lambda}\) makes the normalized
history theorem exact. Reading it as an unconditioned law selected by the
formalism would be ill typed and would contradict the candidate's own
nonselection wall. The former is the only admissible reading.

### Q15 — normal hybrid state outside the `Ens` image

`CONDITIONAL-ON-NAMED-HYPOTHESES` — The hybrid algebra may possess normal
states not represented by the restricted class \(\mathfrak E_D\). The path
duality theorem quantifies over admitted ensembles, not every abstract normal
state. No surjectivity of `Ens` is claimed or needed.

### Q16 — adaptive policy probes an a.e.-null difference

`INTEGRATED-ENSEMBLE-ONLY` — If all reachable record laws are dominated by
\(\nu\), two policy fields equal \(\nu\)-a.e. have equal integrated predictions.
A later singular route that concentrates on the exceptional set violates
class/null-ideal closure and requires a new tagged boundary. Exact frozen
kernel equality is not inferred.

### Q17 — outcome relabeling merges multiplicity

`FOR-EVERY-ADMITTED-PACKET` — A bijective label transport can preserve
probabilities while a many-to-one coarse-graining merges occurrences. Only
the former is presentation gauge; the latter is a typed physical
coarse-graining with a changed reader interface. The candidate distinguishes
them.

### Q18 — contextual preparation procedure name as hidden variable

`REFUSAL/NONIMPLICATION` — Orthogonal \(Z\)- and \(X\)-basis mixtures have the
same barycenter but distinct preparation procedures before quotient. A
procedure label becomes physical only if a licensed future can read an
exposed port. The candidate neither erases procedural contextuality nor
inserts an unread name tag into the ontology.

## 8. Complete 36-coordinate product

| Coordinate | Status | Exact quantum/probability boundary |
|---|---|---|
| input | `BOUND` | exact v2 probabilities/instruments/sources unchanged |
| slot-skeleton | `DECLARED-LABORATORY-PROTOCOL` | finite packet input, not microscopic order |
| frontier | `CONSTRUCTED-TYPE` | lower set; not automatically a division |
| boundary | `CONSTRUCTED-TAGGED` | complete ports, records, classes, samples, states, memory |
| sample-semantics | `CONSTRUCTED-INHERITED` | exact standard-Borel `Ev` kernels and frozen versions |
| ensemble-semantics | `CONSTRUCTED-CONDITIONALLY` | dominated laws plus strong conditional predual field |
| hybrid-object | `CONSTRUCTED-CONDITIONALLY` | finite exact; integrated only for admitted packet data |
| heisenberg-functor | `CONSTRUCTED` | contravariant normal-UCP composition |
| integrated-compatibility | `CONSTRUCTED-CONDITIONALLY` | certified primitive pairs, all admitted ensembles/readers, finite paths |
| point-restart | `FINITE/ATOMIC-CONSTRUCTED; NONATOMIC-GENERIC-UNCONSTRUCTED` | exact sample does not imply normal point state |
| presentation | `CONSTRUCTED` | full tags, fields, kernels, maps, memory, occurrence multiplicity |
| quotient | `CONSTRUCTED-SCOPED` | reachable constructor-complete contexts only |
| covariance | `CONSTRUCTED-CONDITIONALLY` | jointly transported full packet; no canonical state push |
| state-class | `CONDITIONAL-ADMISSION` | common class, normal evaluation, and path closure |
| instrument | `FINITE-CONSTRUCTED; CONTINUOUS-CONDITIONAL` | eight continuous proof obligations, not NEP alone |
| causal-factorization | `CONSTRUCTED-CONDITIONALLY` | named localization, complete maps, typed sources |
| certified-schedule | `CONSTRUCTED-CONDITIONALLY` | exact certificates in all reachable adaptive contexts |
| no-signalling | `CONSTRUCTED-SCOPED` | complete nonselective localized operation only |
| steering | `CONSTRUCTED-CONTROL` | selected positive event; record and conditioning cost retained |
| bell | `CONSTRUCTED-EXISTENTIAL-COMPATIBILITY` | premises explicit; no universal probe realization |
| positive-model | `CONSTRUCTED-WITH-COSTS` | conditional finite histories, contextual/global/memory-bearing/unselected |
| context | `CONSTRUCTED-SCOPED` | registered procedures and complete reader contexts |
| fibers | `CONSTRUCTED-SCOPED` | idle-extension nonselection, not existence proof |
| type-III | `REFUSAL/MODEL-SPECIFIC` | normal functionals/maps; no universal density/trace |
| split | `CONDITIONAL-CONTROL` | collar and type-I intermediate factor/exact substitute |
| gauge | `TYPED-UNSELECTED` | no universal factorization or selected sector ontology |
| particles | `TYPED-UNSELECTED` | no preferred Fock representation or particle ontology |
| continuum | `ABSTRACT-COMPARATOR-CONDITIONAL` | no interacting \(3+1\) model constructed |
| UV | `SCOPED-REFUSAL` | no cutoff removal or convergence theorem |
| preferred-frame | `NO-UNDECLARED-SCHEDULING-FRAME` | contingent material/KMS/apparatus frames allowed |
| record | `CONSTRUCTED-OPERATIONALLY` | exact sample; normal point state iff finite/declared atomic |
| division | `FUTURE-SUFFICIENCY-TEST-REQUIRED` | no promotion from frontier, record, or conditioning |
| actuality | `UNCONSTRUCTED` | no selected result or trajectory |
| barandes | `COMPATIBLE-BUT-INCOMPLETE` | no selected configuration space/law/state/trajectory |
| ontology | `GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED` | representation is not beable selection |
| downstream | `CLOSED` | no internal time, spacetime, matter-geometry dynamics, or gravity |

## 9. Outcome ladder

| Rung | Disposition | Reason |
|---:|---|---|
| 1 `P03V31-HYBRID-BOUNDARY-TYPE-FAILURE` | surpassed | tagged finite/integrated regimes are coherent under admission hypotheses |
| 2 `P03V31-COMMON-DOMINATION-FAILURE` | surpassed conditionally | one common class is a boundary admission requirement and its null ideal is preserved |
| 3 `P03V31-HYBRID-OPERATION-CATEGORY-UNCONSTRUCTED` | surpassed | tagged normal-UCP arrows form a category |
| 4 `P03V31-HEISENBERG-FUNCTOR-UNCONSTRUCTED` | surpassed | reverse composition is functorial |
| 5 `P03V31-INTEGRATED-DUAL-SEMANTICS-INCOMPATIBLE` | surpassed conditionally | exact all-reader primitive certificates induct over finite paths |
| 6 `P03V31-CERTIFIED-CONCURRENCY-UNCONSTRUCTED` | surpassed conditionally | only fully certified reachable swaps are quotiented |
| 7 `P03V31-CAUSAL-FRONTIER-INTEGRATED-DUAL-SEMANTICS-CONSTRUCTED` | supported | earliest unconditional-on-ontology positive rung |
| 8 `P03V31-RELATIVISTIC-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT` | supported with scope | declared AQFT packets, conditional continuous admission, exact finite programs |
| 9 `P03V31-RELATIVISTIC-LOCAL-MICROONTOLOGY-CONSTRUCTED-WITH-COSTS` | impossible/refused | no local beable selection or actual history |
| 10 `P03V31-EMPIRICALLY-DISCRIMINATED-RELATIVISTIC-ONTOLOGY` | impossible/refused | no empirical discriminator |

The earliest supported positive rung is 7 and the strongest is the
protocol-permitted ceiling, rung 8. Rung 8 must always retain the qualifiers
“declared comparator packet,” “admitted continuous instruments,” “finite
program,” and “global ontology debt.”

## 10. Semantic repairs versus bounded wording

### Semantic repairs required

```text
none
```

No probability, instrument, posterior, category object, map, physical
parameter, theorem quantifier, product coordinate, or physical
interpretation must be changed for the verdict above.

### Bounded wording/citation scopes

1. Index the history law by its fixed initial predictive value or ensemble,
   or call it the conditional history kernel before that input is fixed.
2. Keep “continuous duality” explicitly conditional on the independently
   checked Definition 8.4(8) identity; NEP is not advertised as sufficient.
3. Keep “quantum agreement” restricted to the same frozen packet,
   registered readers, and common instrument/posterior data.
4. Keep the continuous qubit/Lebesgue witness labeled as a nonvacuity control,
   not a localized informative measurement model.
5. Keep the Bell source claim existential and hypothesis-bound; do not turn
   algebraic Bell observables into universal system-probe implementations.

## 11. Primary-source scope

The following primary sources were checked at their stated scopes.

1. K. Okamura and M. Ozawa, [Measurement theory in local quantum
   physics](https://arxiv.org/abs/1501.00239). The paper supports the use of
   CP instruments, NEP, measuring-process realizability, and—under its stated
   von Neumann/standard-Borel hypotheses—the relation between NEP and
   strongly measurable posterior families. It also supplies non-NEP
   instruments and approximate-NEP results. It does **not** imply target
   landing, packet class closure, null-ideal preservation, or the candidate's
   exact `Ens` compatibility automatically.
2. C. Fewster and R. Verch, [Quantum fields and local
   measurements](https://arxiv.org/abs/1810.06512). This supports localized
   system-probe coupling, induced observables/instruments, causal
   factorization, and order independence for properly separated couplings
   under the paper's hypotheses. It does not cover arbitrary CP maps or
   supply the v3.1 measure-class interface.
3. C. Fewster and R. Verch, [Measurement in Quantum Field
   Theory](https://arxiv.org/abs/2304.13356). This supports conditional and
   nonselective updates and their relativistic causality/covariance scope. It
   does not select outcomes or a local ontology.
4. R. Brunetti, K. Fredenhagen, and R. Verch, [The generally covariant
   locality principle](https://arxiv.org/abs/math-ph/0112041). This supports
   the locally covariant functorial setting and contravariant state pullback,
   not a canonical forward state extension or emergent geometry.
5. B. Coecke, C. Heunen, and A. Kissinger, [Categories of quantum and
   classical channels](https://arxiv.org/abs/1305.3821). This supports
   careful classical/quantum channel typing. It does not supply the
   candidate's physical packet or ontology.
6. C. Fewster, [The split property for locally covariant quantum field
   theories](https://arxiv.org/abs/1601.06936). This supports split
   inclusions only under their collar/nuclearity-type hypotheses, not a
   universal tensor factorization of touching or gauge-constrained regions.
7. C. Fewster and R. Verch, [Dynamical locality and
   covariance](https://arxiv.org/abs/1106.4785). This supports the named
   covariance/locality distinctions, not metric dynamics or gravity.
8. S. Summers and R. Werner, [Maximal violation of Bell's inequalities is
   generic in quantum field theory](https://doi.org/10.1007/BF01207366).
   This is an existential algebraic Bell result under its net/state
   hypotheses. It is not a theorem that every ideal Bell observable has an
   exact localized probe realization in the candidate packet.

None of these sources selects actuality, an indivisible universal law,
internal time, spacetime, or gravity.

## 12. Final reauthentication and freeze

Immediately before freezing this report, the protocol parent, exact HEAD,
and every bound corpus hash in Section 1 were rechecked. The only pre-existing
unrelated item observed at dispatch was outside v17; this seat wrote only its
assigned report path. No sibling material was inspected. This report is
unstaged and uncommitted.

Report LF line count: `000702`

Report byte count: `043341`

Report ordinary SHA-256: reported externally after the final byte is fixed;
no circular ordinary hash is embedded.

Report normalized self-SHA-256: `7c36159be34eee7197aab5b7dfab575c405628445354be8e7aa1078e2a8a689b`

Normalization rule: replace the 64 hexadecimal characters on the preceding
line by 64 ASCII zeroes, preserve every other byte, and compute SHA-256. The
report ends in one LF and contains no trailing horizontal whitespace.
