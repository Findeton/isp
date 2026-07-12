# cg1 — construction-order gauge and the interacting click-law fork

**Status:** pre-receipt design note, 2026-07-11. Reviews ON. This note is the pin for the first campaign after v9 round 48. No result language below may be promoted before the receipts run and the independent hostile review closes. All cancellation-sensitive numerics use `mpmath` with `dps >= 100`; finite covariance and path identities use exact integers/rationals whenever possible.

## 1. The problem exposed by the round-48 builder

The diffusion result is real at its measured scope, but its builder is not the v7 click law. It chooses one committer from a global fleet, chooses global victim/receiver slots, advances a serial index `b`, and uses `b` inside the causal relation. It neither enforces the per-lineage RN/KL evidence law `S(I)=exp(-I)` nor proves that swapping unrelated construction steps leaves the covariant history law unchanged.

The new target is therefore prior to cone shape:

> **Find the most general interacting record law in which (i) every lineage retains the exact v7 evidence-clock marginal, (ii) unrelated construction steps are gauge, (iii) noncommuting steps leave a covariant causal record, and (iv) interactions require no universe-wide physical updater.**

This campaign distinguishes two requirements that must not be conflated:

1. **construction-order gauge:** different linear extensions of one unlabeled record partial order have the same physical weight;
2. **causal sufficiency:** the conditional law of a seal depends only on its ancestor-closed recorded past and explicitly shared joint records, not on an unrecorded global snapshot.

Gauge alone does not imply locality; a globally normalized unlabeled measure can be label-covariant and still require global knowledge. Locality alone does not imply gauge; overlapping local updates can retain an unrecorded scheduler order. The final law needs both.

## 2. The forced theorem targets

### T1 — no-silent-order theorem

If two construction histories evaluate to the same point of the stem spectrum (the same covariant record content), their physical weight must agree. Otherwise the law assigns physical force to a distinction no record contains.

This is a program-internal consequence of record sufficiency, not yet a theorem about every stochastic growth law.

### T2 — adjacent-swap reduction

Any two linear extensions of a finite partial order are connected by adjacent swaps of incomparable elements. Hence construction-order gauge reduces to the elementary diamond identity

`w(C->C+A) w(C+A->C+A+B) = w(C->C+B) w(C+B->C+A+B)`

for every pair of incomparable admissible additions `A,B`. The receipt will prove the combinatorial reduction independently and exhaustively verify it on all finite test orders in scope.

### T3 — recorded-noncommutativity criterion

Let `U_A,U_B` be elementary update maps. The candidate physical rule is:

- `[U_A,U_B]=0` whenever `A,B` are incomparable and share no recorded interaction support;
- `[U_A,U_B] != 0` is licensed only when the difference is readable in the resulting covariant record and therefore inserts an influence relation or a joint seal.

An order-sensitive difference invisible to the stem readout is a kill, not an interaction.

### T4 — exact click marginal under interaction

For every lineage `i`, define its intrinsic accumulated evidence by the RN/KL ledger itself, including any shared evidence channels:

`I_i = sum_{S contains i} I_S`.

The survival law must remain exactly

`P(no seal of i through evidence I_i) = exp(-I_i)`.

No nonlinear regraduation and no fitted rate are allowed. A physical time rate remains scale-walled; the theorem lives in evidence coordinates.

## 3. Candidate law classes to audit

The campaign will not crown a class before the controls run.

### L0 — global scheduler (negative control)

The round-48 style law: one global committer and global victim/receiver choices. Expected failure: scheduler order or global normalization survives after unrelated swaps. This expectation is registered and may be refuted.

### L1 — independent local evidence races (positive gauge/free control)

Each lineage carries its own `Exp(1)` evidence threshold; unrelated local updates commute. Expected: exact click marginal and construction gauge, but no cross-lineage influence.

### L2 — local shared-shock evidence law

Every recorded interaction support `S` (single lineage, pair, or finite hyperedge) carries a nonnegative additive evidence process `I_S`. A firing of the `S` clock writes a joint record on `S`. The lineage evidence is `I_i=sum_{S contains i} I_S`, so the marginal survival is exponential in the total intrinsic evidence while shared clocks generate genuine correlations. This is a finite common-shock/Marshall-Olkin-type candidate, used here as a construction to test, not imported as a uniqueness theorem.

### L3 — continuous conservative local transport plus L2 seals

Between seals, record content is transported by a graph-local conservative semigroup generated by an interaction Laplacian. The **content** ledger and the **seal evidence** ledger remain typed separately: transport may redistribute committed/uncommitted content, but it may not regraduate the RN/KL evidence coordinate. Disjoint-edge generators must commute exactly; overlapping-edge noncommutativity must be recorded by the local state and consequent ancestry. This is the candidate bridge to the round-48 diffusion discovery.

## 4. Receipts and preregistered gates

### Receipt `cg1_order_gauge_exact.py` — exact finite algebra

- **G0 enumeration control:** reproduce canned posets, their linear extensions, and the adjacent-swap connectivity theorem through the registered finite scope.
- **G1 diamond gauge:** L1/L2 pass every disjoint construction diamond exactly; L0 is measured, with no assumption that it must fail.
- **G2 relabeling covariance:** all permutations in the small-system census give identical unlabeled weights exactly.
- **G3 locality:** changing a disconnected component leaves a target local hazard/update exactly unchanged for L1/L2/L3; a deliberately global-normalized control must be detected.
- **G4 recorded noncommutativity:** disjoint supports commute; overlapping supports either commute or produce an explicitly different local record/ancestry. Invisible noncommutativity is a kill.
- **G5 conservation:** L3 preserves total transported content exactly under rational test steps; destructive and teleport controls print their distinct ledgers.

### Receipt `cg2_click_marginals_mp.py` — high-precision law

- **C0 scalar survival:** `-log S(I)-I` below `1e-90` on a fixed evidence grid at `dps >= 100`.
- **C1 interacting marginal:** for L2, every lineage marginal equals `exp(-sum I_S)` below `1e-90`, while a shared-support covariance is strictly nonzero.
- **C2 composition:** splitting every evidence segment into two or five pieces changes no survival/joint law above `1e-90`.
- **C3 scheduler/Trotter gauge:** disjoint local generators agree under AB, BA, and symmetric splittings below `1e-90`; the overlapping control is classified by its recorded state difference.
- **C4 no-signaling toy gate:** a declared local setting changes joint correlations but not the remote marginal below `1e-90`. Failure blocks any “entanglement-compatible” language but does not erase the classical interacting law.

### Receipt `cg3_covariant_click_census.py` — covariant finite readout

- **S0 labeled/unlabeled separation:** construction labels change while the canonical unlabeled order and stem signature do not.
- **S1 order-gauge readout:** alternate linear extensions of the same generated partial order yield identical stem signatures and exact total weight.
- **S2 influence readability:** an overlapping interaction that changes a later click changes a finite stem statistic; a label-only scheduler change does not.
- **S3 current-builder audit:** run a reduced round-48 update family under alternate schedulers and classify which differences survive unlabeled/stem reduction. This is an audit, not a retrofit and not a cone receipt.

## 5. Decision semantics

- **GAUGE-ONLY:** construction covariance passes, but every interacting class fails locality, exact click marginals, or covariant influence readability.
- **LOCAL-CLASSICAL:** an interacting asynchronous law passes construction gauge, causal sufficiency, exact click marginals, conservation, and stem readability, but the no-signaling correlation gate or quantum extension remains open.
- **JOINT-CLICK-CANDIDATE:** LOCAL-CLASSICAL plus the finite no-signaling joint-record gate. This licenses a candidate law and a paper, not a uniqueness claim and not a derivation of Bell-quantum correlations.
- **REFUSED:** no interacting class survives the conjunction. The paper becomes a no-go/localization result.

No result in this campaign licenses 3+1 geometry, a round cone, physical proper time, or an absolute scale. Those are downstream retests only after the law exists.

## 6. Hostile-review discipline

After the receipts and first paper draft:

1. independent referee A attacks theorem logic, gauge versus locality, and hidden global normalization;
2. independent referee B rebuilds the finite receipts with different representations and attacks numerical precision/certification;
3. independent referee C attacks ontology, no-signaling language, stem readability, and whether the proposed “local” supports presuppose geometry.

Every concrete opening is investigated before the next review round. New receipts require a written amendment committed before execution. A favorable result receives no softer standard than a refusal.

## 7. Known risks registered before code

1. The shared-shock law may preserve exponential marginals but fail to produce genuinely quantum rather than classical correlations.
2. Graph-local support may merely relocate the missing law into an assumed interaction graph.
3. Exact construction gauge may force a global normalization/Doob transform, defeating locality.
4. L3 diffusion may be local only relative to slot labels and vanish on the stem spectrum.
5. The v7 law fixes evidence survival, not placement; a surviving law may still leave the interaction supports and initial seed as physical inputs.
6. One-at-a-time simulation is harmless only if simultaneous/joint seals are represented as composite events and all unrelated orderings are gauge.

## 8. Paper target

Working title: **“Construction-order gauge and the interacting record click law.”**

The paper must separate:

- forced: no-silent-order gauge, adjacent-swap reduction, exact evidence marginal;
- constructed/measured: any surviving L2/L3 law;
- posited: the interaction-support graph/hypergraph unless derived;
- open: uniqueness, quantum/Bell completeness, 3+1 channel manifold, influence-cone equivalence, and absolute scale.

## 9. Round-1 hostile review — MAJOR REVISION, promotion refused

Three independent referees reproduced every printed arithmetic result and independently rejected the promotion. The paper's `JOINT-CLICK-CANDIDATE` grade is superseded by **NOT-CERTIFIED / conditional common-shock template** until the openings below run.

The convergent findings are adopted:

1. G1 multiplied unnormalized activities (`4/3 * 3/2 = 2`); it was not a stochastic diamond. Equal raw AB/BA race probabilities are not the general meaning of gauge. Independent clocks with unequal hazards can have unequal temporal order probabilities while their unordered marked-history pushforward is perfectly covariant.
2. G3 confused a Gillespie/next-event normalization with physical nonlocality. The correct locality test is disjoint-union factorization of the component marginal process.
3. L2 survival, L3 transport, and C4 outcomes were three modules, not one recurrent generator.
4. RN/KL additivity over overlapping supports was named, not derived. Static exposure identities do not prove the v7 ledger after arbitrary prior seals.
5. Overlap noncommutativity changed hidden vectors; the receipt inserted a separate order edge by hand. Bare stems omit support, joint-event, evidence/content, outcome, and parent marks.
6. The support hypergraph `H` relocates the interaction law and cannot merge disconnected components under a strictly support-local rule.
7. The no-signaling table was uncoupled and Bell-local (`CHSH_max=1.25`, independently computed). High precision certified arithmetic identities, not ontology.

### Round-1 correction to T1/T2

The forced statement is quotient-level:

> The physical law must push forward to a well-defined measure on covariant marked histories. Raw scheduler/race presentations inside one fiber may carry unequal proposal densities; only their summed/pushforward physical measure is observable.

The strong equal-path diamond is a sufficient optional gauge fixing, not forced by record sufficiency. It is retained only when `w` is already a normalized physical labeled-path kernel with a fixed reference measure.

## 10. Round-2 opening pin — one integrated recurrent process

No next hostile round begins until the following amended receipts run.

### O1 — normalized recurrent support process (`cg4`)

Define independent unit-rate Poisson processes in each support's **intrinsic evidence coordinate**. Each firing is an atomic marked seal event. Singleton supports give private seals; multi-lineage supports give common-cause joint seals. Primitive support clocks renew by independent increments, so after every stopping history the no-incident-seal survival of lineage `i` over new total incident evidence `Delta I_i` is exactly `exp(-Delta I_i)`.

The process is defined without a physical global next-event selector. A simulation may merge clock events using an auxiliary scheduler; the physical output is the marked partial order obtained by retaining ancestry through shared lineages and quotienting relative order of disjoint events.

Gates: normalization/generating functional; recurrent marginal after an adaptive finite past; disjoint-union semigroup factorization; quotient probability invariant under scheduler presentations; non-explosion at every finite total support exposure.

### O2 — integrated local outcomes (`cg4`)

A shared ancestor/joint seal carries a classical hidden common-cause mark `h`. Later local settings act only on the descendant's local response kernel. The outcome family must be normalized, positive, no-signaling in both directions, sequentially composable, and explicitly Bell-local. This replaces the grafted C4 table. No entanglement language is licensed.

### O3 — support bootstrap theorem and closure (`cg5`)

Prove exactly: a rule whose new supports are subsets of existing connected support components can never merge initially disconnected components. Test the covariant closure in which one root record branches into descendants and creates their common-ancestor support; later supports may be inherited/refined only from recorded joint ancestry. The seed/root remains an explicit boundary input.

### O4 — marked histories and end-to-end readability (`cg5`)

Define finite marked histories carrying event support, parent events, event type, rational content/evidence mark, and outcome mark. Canonicalize under both event and lineage relabeling. Verify:

- disjoint AB/BA scheduler presentations have one canonical marked history;
- overlapping events have recorded ancestry and distinct marked histories exactly when their local state/order differs;
- event-based conservative transfer is written into the joint seal, so no hidden vector difference is used as evidence;
- bare-stem equality may coexist with marked-stem inequality (the old gap printed explicitly).

### O5 — explicit RN/KL support accounting (`cg6`)

Construct finite forward/reverse likelihood blocks. Prove the conditional chain-rule decomposition when support observations are conditionally factorized and counted once. Print two counterexamples: marginal KL can miss pure correlation evidence; assigning one shared observation to two supports double-counts its KL. The repaired ledger assigns shared evidence once to the joint support and uses conditional KL for dependent sequential blocks.

### O6 — transport semantics (`cg5/cg6`)

Fundamental transport in this round is event-based: a joint seal applies a rational conservative local transfer and records the post-transfer mark. Continuous graph diffusion is only a downstream many-small-event limit. No unexplained global `dt`, no finite operator-splitting commutator interpreted as physics.

### O7 — nonuniqueness census (`cg6`)

Exhibit at least two inequivalent interacting shared-support laws satisfying the corrected finite gates (e.g. distinct positive shared-evidence allocations/couplings). Unless a new principle selects one, the paper must prove an underdetermination theorem rather than claim the final law.

### O8 — full old-builder audit (deferred downstream, not allowed to promote this law)

The reduced S3 result establishes a possible hidden scheduler dependence only. A production-scale alternate-scheduler audit of round 48 is required before any claim about prevalence or effect on `F`; it is separate from the foundational law receipts and remains in the review-prescribed cone queue.

## 11. Round-2 opening results — all receipts green, uniqueness refuted

The amended receipts ran after the §10 pin.

- `cg4_recurrent_marked_process_mp.py`: **6/6** at `dps=120`. Normalized recurrent Poisson support law; stopping-history renewal residual `4.84e-121`; unequal raw race orders `0.2353/0.7647` push forward to one unordered result; disconnected semigroup factorization residual `2.42e-122`; integrated two-sided no-signaling local-common-cause outcomes (`CHSHmax=0.7`); finite-exposure nonexplosion bound `1.29e-45` for `N>=100` in the printed cell.
- `cg5_marked_history_exact.py`: **6/6**, exact. Support no-bootstrap theorem checked over 501 finite cases; common-ancestor branch seed; disjoint AB/BA canonical equality; overlap ancestry inequality; rational event-based conservation `(4,2)->(3,3)`; bare-order equality with marked-content inequality.
- `cg6_rn_chainrule_nouniqueness_mp.py`: **6/6** at `dps=120`. Conditional chain rule residual `2.42e-122`; pure-correlation joint KL `0.368064...` against marginal sum `0`; shared-block double count `0.192744... -> 0.385489...`; typed repair residual `9.68e-122`; same-marginal interacting covariances `0.0299636/0.1371965`; unselected conservative transfers `g=0.1/0.3`.
- `cg7_refinement_projective_mp.py`: **5/5** at `dps=120`. Poisson refinement residual `9.68e-122`; projective support restriction exact; normalized adaptive common-ancestor branch kernel; atomic joint seal distinguished from recorded private decomposition; locally finite incident-exposure certificate.

**Decision:** an integrated H-local classical marked-process family exists at finite/projective-template grade, but the nonuniqueness gate fires decisively. The current principles leave a continuum of shared-evidence allocations and transport coefficients. The campaign cannot honestly “find the final unique law.” Its theorem is underdetermination plus the exact interface a future selector must fill.

## 12. Round-2 hostile review — targeted MAJOR REVISION

All three referees accepted the underdetermination direction and independently reproduced the new arithmetic. They refused the advertised adaptive/projective scope. Referee B found a concrete covariance bug: support-indexed outcomes were not permuted with their lineages. All three identified the same remaining gaps: no end-to-end trace generator, quotient pushforward not compared across schedulers, shallow restriction, abstract rather than explicit RN witnesses, and renewal/no-signaling/nonexplosion wording beyond receipt scope.

The corrections/openings were pinned in the review record and executed:

1. marked events are now typed lineage ports `(lineage,parent,content,outcome)` plus event type and RN block ID;
2. `cg5` gained the referee's outcome-permutation regression and now passes 7/7;
3. `cg8_end_to_end_trace_exact.py` builds one exact trace carrying root common cause, local setting/seals, outcomes, RN blocks, joint transfer, parents, and renewal; unequal-rate queue and direct-trace schedulers push forward to the same eight-history canonical distribution of total mass one;
4. `cg8` defines cross-boundary marked restriction, retains projected joint-event/block marks, and verifies scheduler/restriction commutation plus restriction composition;
5. `cg9_likelihood_compensator_mp.py` realizes `c=0.2/0.7` with explicit forward/reverse likelihood blocks of exact target KL, distinguishes conditional realized-compensator renewal from random unconditioned exposure, and tensors both models with the same local outcome/transfer modules.

Results: `cg8` **4/4 exact**; `cg9` **4/4 at dps=120**. The paper is rewritten as one argument; all superseded equal-path and continuous-splitting claims are removed.

Final-pass scope is narrowed explicitly: finite restrictions and pushforwards, conditional predictable-compensator renewal, local nonexplosion only under finite incident exposure, finite marked covariance (not a marked profinite spectrum), classical Bell-local outcomes, and underdetermination within the constructed support family.

## 13. Final hostile verification — PASS at scoped underdetermination result

Final referee A: **PASS-WITH-CORRECTIONS**; the compensator independence hypothesis and `cg9` outcome-module wording were corrected. Final referee C: **PASS** within the explicit finite conditional classical scope. Final referee B found one remaining real blocker: projection provenance was not idempotent (`projected-projected-*`) on a genuine three-way crossing event. The restriction functor was repaired, E3 replaced by the exact three-lineage crossing test, and referee B reran it: direct and successive restrictions are exactly equal with identical parents, block IDs, contents, outcomes, and one `projected-*` tag. **PASS.**

Final campaign grade:

> **ACCEPT as an underdetermination/no-selection theorem and a conditional finite gauge-local classical template. The final unique interacting click law was not found because the present principles provably leave its shared-evidence and transfer coupling unselected within the constructed family.**

Explicit nonclaims: quantum/entanglement law, proper time, relativistic locality, marked profinite completion, global nonexplosion, support/exposure selector, 3+1 geometry, absolute scale, or any revision of Paper 8's diffusion finding.
