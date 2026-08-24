# SPB v2 contract review — Seat M (mathematics/statistics)

Date: 2026-08-24

Seat: M — mutually blind mathematics/statistics review

Frozen pin: `v17/note-spb-v2-sufficient-physical-boundary-contract-review-pin.md`

Frozen commit: `7221d777cc341b9e5f9ee010f44f642d5a45d4ea`

Frozen parent: `915f1c2bad3c97337b0e7b74d1f97e9f8f16cce8`

Review mode: read-only, independent, no sibling v2 report inspected or contacted

Scientific result awarded: none

## 1. Independence, chronology, and authentication

I performed this review read-only. I did not inspect, request, receive, or
communicate with a sibling v2 reviewer or sibling v2 report. I made no
repository edit. The unrelated untracked
`v16/note-handoff-prompt-2026-08-22.md` was excluded. The only file created by
this seat is this report in `/tmp`.

Authentication preceded scientific inspection.

- Repository `HEAD` resolved exactly to
  `7221d777cc341b9e5f9ee010f44f642d5a45d4ea`.
- Its sole parent resolved exactly to
  `915f1c2bad3c97337b0e7b74d1f97e9f8f16cce8`.
- The commit tree is `5b96277ff23bb22cbb132cfa1868cd8a6cf38f4f`.
- The pin commit adds the v2 pin and has subject
  `Freeze SPB v2 contract review pin`.
- The working bytes of the pin and all seven frozen scientific objects are
  byte-identical to `HEAD`.
- The only worktree difference was the excluded untracked v16 handoff note.

The v2 pin has 560 LF lines, 26,284 raw bytes, and raw SHA-256
`f2f982e55f8b4d9cc26626f830fc2bd5b99dc0fd5067539ac3611183303fa1d7`.
Its Section 8.1 normalization recomputes
`8d46d1a7c499a4f9f11b534142d9ae5815dfcf41e12ce8942d77917278bf2425`,
exactly the value printed in the pin. It ends in one LF and has no trailing
horizontal whitespace. Chronology and pin authentication pass.

### 1.1 Frozen v2 repository identities

Counts are LF line counts and raw bytes.

| frozen object | lines | bytes | observed SHA-256 | result |
|---|---:|---:|---|---|
| `v17/note-foundational-assumption-deletion-programme.md` | 557 | 26173 | `ae4e40f17997519c0a9e0e51272e1714e163df4242304e5e2e0d615d6df8536f` | match |
| `v17/research-incubator/active/assumptions/v17_assumption_parallel_synthesis_and_next_gates.md` | 837 | 33196 | `6c7dabbe3cc673e0410ce5b3a04d4ea61b20fa08c97e3b6903c3cb013f6775a8` | match |
| `v17/research-incubator/active/spb/v17_spb_primary_source_receipt_manifest.md` | 106 | 6491 | `5e5ebeb8afbb8a14dbf725b9d4d238fca4e200e03cd7e4da53fd222188833041` | match |
| `v17/research-incubator/active/spb/v17_spb_p0_physical_platform_and_source_audit.md` | 457 | 21897 | `f0e093acc14bb578b40f274996d65e4446e512e9009ba0060fb8c328c9a41a44` | match |
| `v17/note-spb-sufficient-physical-boundary-contract-review-adjudication.md` | 702 | 27687 | `5f7719af388afedf962282ba9b29924bfa6da6af917219ecdde6cd6f5aeff5ac` | match |
| `v17/research-incubator/active/spb/v17_spb_v2_result_neutral_gate_contract.md` | 1282 | 47642 | `71990429c4c3d8c8ed841298950bf142895a9754f4184532ca31e975c57d9775` | match |
| `v17/research-incubator/active/spb/v17_spb_v2_root_readiness_and_countermodel_audit.md` | 555 | 19752 | `fc5dcfee9dd32572c1cb8cfe059d617a195bedee1883dbd31acb6e67b17fe63b` | match |

I read all seven objects end-to-end.

### 1.2 Terminal v1 dependency identities

All seven terminal v1 dependencies match their pin identities.

| terminal dependency | lines | bytes | observed SHA-256 | result |
|---|---:|---:|---|---|
| `v17/note-spb-sufficient-physical-boundary-contract-review-pin.md` | 489 | 22169 | `b5491cd698af90f6603f1597a8724f9614d0d255fef5b0da0c9b54686ac6c75d` | match |
| `v17/review-spb-contract-mathematics-statistics.md` | 443 | 23617 | `1b80d6ef86a3983ec9a9a40da23b4ef8c918010ed1ffcab55d2826628f1ee998` | match |
| `v17/review-spb-contract-physical-temporal.md` | 278 | 17034 | `631a68aefa628f355fb5ae1616a0e389b7cd98cad9074c9495c3532cf9289fff` | match |
| `v17/review-spb-contract-physical-regional.md` | 279 | 17144 | `5ca35981cfef951d0c875c34e1c8d03a8a59627a739f085e7a1828dc7b439d81` | match |
| `v17/review-spb-contract-physical-joint.md` | 245 | 15277 | `c986d3359071b8aa5e9f37411b2f5641b594a63756b67af8195fe93ff02e2a74` | match |
| `v17/review-spb-contract-foundations-ontology.md` | 373 | 19859 | `fd29f31e809b64490fce332875c13ec32e11e63c138973b7b595721ec10abaa2` | match |
| `v17/note-spb-sufficient-physical-boundary-contract-review-adjudication.md` | 702 | 27687 | `5f7719af388afedf962282ba9b29924bfa6da6af917219ecdde6cd6f5aeff5ac` | match |

I consumed the terminal pin, all terminal reports, and the adjudication to
reconstruct the v1 defects. I did not treat any v1 conclusion as a v2 result.

### 1.3 Exact source and author-repository identities

All six accessible scholarly bytes independently reproduce the frozen
receipts.

| source | exact local object | bytes | observed SHA-256 | result |
|---|---|---:|---|---|
| `SPB-S1` | `/private/tmp/spb_t_pollock.pdf` | 896695 | `cb2c596d96b0352a716cd919faacc266efcc0fd4e23c6e604bd62b87cd93c1dc` | match |
| `SPB-S2` | `/private/tmp/spb_t_giarmatzi_v3.pdf` | 6601486 | `ce0c1dc116b0394dce9b526e7d230b89b69a27726641c9c4110905fc7ddadc28` | match |
| `SPB-S3` | `/private/tmp/spb_t_xiang_v2.pdf` | 1276514 | `cca4a2cdc32c3bb05e3ee35b45b62eab2f6e4b743099c375f00f3a614211f242` | match |
| `SPB-S4` | `/private/tmp/spb_r_isoscattering.pdf` | 1835223 | `597818056d697ed4b8c264547de550ce50c88757074bd9030aee977dd6b7d0c5` | match |
| `SPB-S5` | `/private/tmp/spb_r_star_product.pdf` | 307827 | `1c9a49fff423439c7eaeaa8aadd08b503aee0dddc68af869b9f87cf22b73382e` | match |
| `SPB-S6` | `/private/tmp/spb_r_isoscattering_equal_oneport.pdf` | 3291194 | `dcc126a0910c2c7c2f91f9cd580bc81ea3a11020837adb8e3c12d4c25f14a88f` | match |

The local `NMN-tomo` checkout has origin
`https://github.com/Christina-Giar/NMN-tomo.git`, is clean, and resolves to
`154235f8bbf5e70eb71c325370a67b1894490452`. Its four selected objects match:

| path | bytes | observed SHA-256 |
|---|---:|---|
| `README.md` | 904 | `fcd27b514890614b03a26f7ec84a879962feccdb846fd00de103b9631c46a593` |
| `All codes.ipynb` | 1399666 | `b0a2e041ef1616f8c0cff8e2536a892a260820d16fbd8343d22e898b0441c2a1` |
| `NMN_lab_rslts.json` | 20177 | `b52afa57cced174839059e6438e17dc49ead33ae6687c44f58f6f2c664dcdc43` |
| `NMN_tomog_rerun.json` | 176825 | `450db9360fbd162fd12e5be13655e45e1d19f29049f96c9fdb2ab6616b00c657` |

The local `qucse` checkout has origin
`https://github.com/xlelephant/qucse.git`, is clean, and resolves to
`81998e861ae43541d03738c15d7c60715be37309`. Its tracked tree has 79 files and
contains no DataVault object. The pinned absence therefore also authenticates.

No source substitution, network retrieval, later version, or unpinned object
was used.

## 2. Independent reconstruction of the Seat M duties

### 2.1 Attempt type, score, and causal target

The parent type `(C,A,E,Y)` is a real improvement over v1. Context
`C=(j,s,rho,c)` is separated from assigned physical treatment
`A=(h,i,f,z)`, literal execution
`E=(tilde h,tilde i,tilde f,e_C)`, and physical observation
`Y=(b,r,n,q)`. The scored law uses
`Y_star=(E_star,b,r,n_star,q)`, where `E_star=kappa_{C,A}(E)`.

Literal execution is retained archivally; correct executions of different
histories share the `COMPLIANT` value. Noncompliance, retries, latency,
failures, and physical deviations stay in a common taxonomy. A physical trace
accessible to the licensed future must occur in `b` or `n` and cannot be
removed from the score without a physical inaccessibility certificate. Under
those binding restrictions, the new notation does not itself recreate the v1
TV-one defect and does not license erasure of a future-readable record.

The primary kernel is intention-to-treat: noncompliance, substitution,
missingness, and failure stay in the outcome. Compliance-conditioned analysis
is secondary and requires preregistered principal-stratum or causal
assumptions. This distinction survives. Finding M2-01 identifies a remaining
identification overclaim for nonrandom assignment.

### 2.2 Common outcomes and sentinels

Each comparison cell has one measurable space `(Y_c,F_c)`. Branch-absent
fields receive typed sentinels rather than disappearing. The schema must state
which boundary outcomes, records, seeds, waveforms, and nuisance monitors are
scored. The full parent is normalized over every issued attempt. This closes
the v1 undefined-projection defect, conditional on enforcing the physical
access rule for `n_star`.

### 2.3 Presentation, matching, and screening

The exact presentation groupoid acts on the whole fixed physical interface
description. Empirical validation matching is a threshold relation, is
explicitly nontransitive, and is not quotiented. Held-out screening is a third
relation on common future/exterior outcomes. The history-separation lower
bound blocks duplicate-label vacuity; absence of any separated matched pair
routes to underdetermined. The three notions are correctly typed.

### 2.4 Equivalence and multiplicity

For a fixed, scientifically meaningful margin, the local rule is correct:
`U<=epsilon` passes, `L>epsilon` fails, and a straddling interval is
underdetermined. Reader/calibration uncertainty widens the interval rather
than the margin. Candidate pass is a conjunction of mandatory local passes;
candidate fail needs at least one established local failure. One simultaneous
family includes validation selection, candidates, pairs, instruments,
policies, composites, bins, bracketings, and stopping. Finding M2-02 shows that
the contract never makes the margin or matching threshold nonvacuous and does
not bind a nontrivial power target.

### 2.5 Acyclic and feedback composition

Normalized Markov kernels and seam kernels compose by iterated integration in
an acyclic wiring once an initial boundary/preparation probability is supplied.
Ionescu--Tulcea does not create that initial measure. Equation (7.3) omits it,
which is Finding M2-03.

For feedback, normalized local conditional kernels need not be compatible and
need not select a unique joint law. The contract correctly demands a frozen,
target-independent global compatibility construction and keeps direct target
data from selecting a joint or normalization. Its substantive existence,
uniqueness, and normalization distinction is sound. The status list itself is
not disjoint under model failure, as Finding M2-04 records.

### 2.6 Deterministic seam calculus

From

`b_s=S_se a_e+S_ss a_s` and `a_s=V b_s`,

one obtains

`K a_s=V S_se a_e`, with `K=I-V S_ss`.

For every admitted exterior input:

- existence is `Range(V S_se) subseteq Range(K)`;
- internal uniqueness is `Ker(K)={0}`;
- exterior uniqueness is `S_es Ker(K)={0}`; and
- useful prediction additionally needs the frozen conditioning budget.

These conditions are correct. The ordered primary classifier correctly
distinguishes exact no-solution, exterior-nonunique, trapped/internal-only
nonuniqueness, ill-conditioning, and regularity when the exact model
properties are certifiable. Finding M2-05 identifies unresolved and
simultaneous-pivot cases not uniquely routed by the printed statuses.

### 2.7 Transfer, candidate order, direct triples, resources, and rungs

The formal vector `(D,S,C,I;X_D,X_S,X_C,X_I)` correctly keeps primary
composition in `rho_0` separate from each named transfer duty in `rho_1`.
Direct `ABC` execution is mandatory; pairwise agreement is not substituted.
Connected-target fitting, response tables, and target-sized representations
are anti-controls, and source/resource growth is charged.

The cumulative ladder is internally ordered and its maximum review award is
L0. It does not promote any empirical result to ontology, chronology,
spacetime, gravity, or universality. Candidate necessity and the headline
outcome flags, however, contain the false minimality and duty-routing defects
in Findings M2-06 and M2-07.

## 3. Independent reconstruction of all binding hostile countermodels

### H1 — copied history forces TV one

Let `h` be 0 or 1 and let every genuine post-boundary record have the same law
`R`. Scoring `(h,R)` gives

`TV(delta_0 tensor R, delta_1 tensor R)=1`.

V2 maps both correct executions to `COMPLIANT`; syntax alone then contributes
zero. The literal transcript remains archived. This mutant is caught.

### H2 — deleting a future-readable log gives a false pass

Let a controller register retain `L=h` and let the licensed future read `L`.
If `kappa` maps both treatments to `COMPLIANT` and `n_star` drops `L`, the
scored laws can be identical although the physical future distinguishes them.
With `L` retained in `b` or `n_star`, TV is one. Lines 183--193 forbid the
deletion and make a false inaccessibility claim invalid. This mutant is caught
if the access certificate is enforced.

### H3 — an interval straddles the margin

For `epsilon_sci=0.10` and `[L,U]=[0.02,0.20]`, neither `U<=epsilon` nor
`L>epsilon` holds. The only licensed result is `UNDERDETERMINED`. This mutant
is caught.

### H4 — threshold matching is nontransitive

At radius `delta`, points `0`, `0.75 delta`, and `1.5 delta` make the first
close to the second and the second close to the third, but not the first to
the third. V2 does not quotient this relation. This mutant is caught.

### H5 — equal coherent response, unequal complete laws

Take `S_A=S_B=0`. Module A has noise `eta=0` and no timeout. Module B has
`eta=+sigma` or `-sigma` equiprobably, or has timeout probability `p>0`.
The coherent matrices and all deterministic star products agree, while the
noise example has TV one on its disjoint noise support and the timeout example
has TV at least `p`. `R-B0` receives coherent-control credit only; complete
claims require a stochastic kernel. This mutant is caught.

### H6 — cyclic local kernels with no joint

For binary `X,Y`, impose `X=Y` with probability one conditional on `Y` and
`Y=1-X` with probability one conditional on `X`. No pair satisfies both.
Normalized local kernels exist but no compatible joint does. The correct
status is `COMP-NONEXISTENT` when the model is otherwise valid. This mutant is
caught.

### H7 — cyclic local kernels with multiple joints

Impose `X=Y` in both conditional directions. Every law
`p delta_(0,0)+(1-p) delta_(1,1)` is compatible. Local kernels do not select
`p`. The correct status is `COMP-NONUNIQUE`; target data may not select `p`.
This mutant is caught.

### H8 — nonunique interior, unique exterior

Choose scalar `V=1`, `S_ss=1`, `S_se=0`, and `S_es=0`. Then `K=0`, every
internal seam amplitude solves the equation, and `b_e=S_ee a_e` is unique.
The correct primary status is
`SEAM-INTERNAL-NONUNIQUE-EXTERIOR-UNIQUE`. This mutant is caught.

### H9 — global solve with a singular sequential pivot

The coefficient matrix

`G=[[0,1],[1,1]]`

has determinant `-1`, so the global solve is unique, while elimination through
the upper-left scalar pivot fails. A singular sequential pivot is therefore an
algorithmic outcome, not physical nonexistence. V2 routes this correctly.

### H10 — pairwise-good, direct-triple-bad

Let `P_iid` be uniform on all eight bit triples and `P_even` uniform on the
four even-parity triples. Every one- and two-bit marginal agrees, but

`TV(P_iid,P_even)=1/2`.

The mandatory direct `ABC` comparison detects this mutant.

### H11 — primary composition passes while composition transfer fails

In `rho_0`, let the frozen rule and direct target both be `delta_0`. In
`rho_1`, let the unchanged rule predict `delta_0` while the direct target is
`delta_1`. Then `C=PASS` and `X_C=FAIL`. The formal vector routes this case.

### H12 — screening transfer passes while composition transfer fails

In `rho_1`, let all compared histories have identical registered one-bit
future laws, but let the rule predict an iid triple while the direct triple is
even parity. Then `X_S=PASS` and `X_C=FAIL`. The formal vector routes this;
the headline flags do not, as Finding M2-07 explains.

### H13 — larger pass, predecessor underdetermined

For a predecessor use `[0.02,0.20]` at margin `0.10`; for a larger candidate
use `[0.01,0.08]`. The larger candidate passes, the predecessor is
underdetermined, and no necessity claim follows. Lines 1066--1069 correctly
block this mutant.

### H14 — active cable permutation is not passive presentation

Let `S=diag(s_1,s_2)` with `s_1!=s_2`. A passive rename transforms source,
response, reader, record, and labels together and changes no experiment. A
physical cable swap changes the fixed-port response to `P S P^-1` relative to
the unchanged cables/readers. V2 types the latter as instrument `P_pi`. This
mutant is caught.

### H15 — reset, randomization, or isolation exports a record

For reset, map `(M,R=0)` to `(M'=0,R'=M)`; for randomization, store seed `Z`
in a controller; for isolation, record its pulse/heat/residual-coupling state.
If the licensed future can read `R'`, `Z`, or the controller state, dropping it
can falsely screen histories. V2 requires each destination, access proof,
failure, and cost. This mutant is caught.

### H16 — target-sized predictor passes prediction but fails descent

For every held-out control word `u`, store its exact law `Q_u` in a lookup
table. Prediction is exact, but the object has target-sized information and
was made from the answer. It fails `D` and the sub-target composition/resource
condition. This mutant is caught.

## 4. Numbered findings

### M2-01 — Blocking — source closure alone does not identify a nonrandom do-law

- Category: mathematical, causal-statistical, semantic.
- Affected claims: V2-C1, V2-C3; contract Sections 2.3--2.4.
- Exact evidence: contract lines 241--248 define
  `Q_{c,a}=P(Y_star in dy | C=c, do(A=a))` and state that it is identified by
  an implemented randomized **or otherwise source-closed** assignment
  mechanism. Lines 268--282 add interleaving, standardization, or
  underdetermination, but never bind positivity/overlap or an equivalent
  identification condition for the nonrandom case.
- Countermodel: let `U` be a fair preassignment bit, use the fully known frozen
  rule `A=U`, and set `Y=U` with no causal arrow from `A` to `Y`. The observed
  conditionals are `P(Y=1|A=1)=1` and `P(Y=1|A=0)=0`, while
  `P(Y=1|do(A=a))=1/2` for both `a`. Even if `U` is registered, there is no
  overlap within `U`; source closure does not create the missing counterfactual
  support. A validated transport model would be an extra causal assumption,
  not a consequence of source identity.
- Consequence: randomized interleaving identifies the intended ITT law, and
  the underdetermined route is sound, but the printed universal identification
  sentence is false for an admitted nonrandom source-closed mechanism. The
  central do/conditioning firewall is therefore not closed as printed.

### M2-02 — Blocking — the matching and equivalence margins admit a tautological pass

- Category: statistical, mathematical, semantic.
- Affected claims: V2-C4, V2-C5; contract Sections 5.2--6.5; the pin's
  nonvacuity and statistical-decidability question.
- Exact evidence: lines 415--420 define matching by `U_B[d_B]<=delta_B` with
  no nontrivial range or resolution constraint on `delta_B`. Lines 472--482
  define a candidate- and comparison-specific `epsilon_sci`, but impose no
  requirement that it be strictly below the diameter of the primary distance.
  Lines 488--497 require adequate power only in the special zero-margin case.
  Section 15.1 names a future power duty but gives no alternative, target
  power, or nonvacuity criterion.
- Decisive countermodel: total variation has diameter one. Set
  `delta_B=1` and `epsilon_sci=1`. Choose genuinely different histories with
  `L_W[d_W]=1>eta_W`, boundary laws at TV one, and future laws at TV one.
  Every valid upper confidence endpoint can be clipped to one, so every pair
  is "matched" and every screening comparison passes. Coverage can be exact
  and sample size arbitrarily large; the answer is forced by the thresholds,
  not the boundary. Calling the predictive use uninformative does not trigger
  the reader clause, because the readers can be perfect in this example.
- Consequence: the history-separation certificate blocks duplicate labels but
  does not make boundary matching or screening scientifically nonvacuous. The
  frozen bytes permit maximal physical disagreement to be declared
  equivalence. This is a false-equivalence countermodel and a power duty cannot
  cure it after the margin has made all alternatives equivalent.

### M2-03 — Blocking — acyclic composition omits the initial boundary law

- Category: mathematical, stochastic typing, semantic.
- Affected claims: V2-C11, V2-C12; contract equations (7.1)--(7.3), temporal
  Section 8.7, and the assertion of normalized complete composition.
- Exact evidence: lines 535--549 type every piece kernel conditionally on
  `x_k^in`; lines 559--569 pass only the piece kernels, seam kernels, and the
  nuisance/reference law `Lambda` to `Comp`. Lines 571--573 claim normalization
  follows by Ionescu--Tulcea. The separately typed `Prep_B` coordinate at
  lines 291--312 is not an argument of (7.3), and no law for `x_A^in` appears.
- Decisive countermodel: let `x_A^in` be binary; let each normalized piece and
  seam copy its input deterministically; and let the final reader output that
  bit. With trivial `Lambda`, both the all-zero law and all-one law satisfy all
  printed kernels. If one integrates against counting measure instead, total
  mass is two. Ionescu--Tulcea extends an **initial probability plus** kernels;
  it does not supply the initial probability.
- Consequence: equation (7.3) is at best a family conditional on an unstated
  initial boundary value, not the one normalized `Q_hat_ABC` claimed on the
  direct-attempt schema. Interpreting `K_A` as also performing preparation
  changes its printed conditional type; interpreting `Lambda` as the initial
  carrier law changes its printed nuisance/reference role.

### M2-04 — Major — the feedback compatibility statuses are not a disjoint routing classifier

- Category: mathematical, semantic, outcome routing.
- Affected claims: V2-C11; contract Sections 7 and 10.3.
- Exact evidence: lines 578--594 list `COMP-NONEXISTENT`, `NONUNIQUE`,
  `UNRESOLVED`, and `MODEL-INVALID` without a priority order. Lines 946--954
  require every regional prediction to print one `COMP-*` status. In contrast,
  the deterministic seam classifier explicitly supplies an order.
- Countermodel: take the incompatible binary kernels from H6 and also fail a
  registered stationarity or domain validation. The local/seam specifications
  admit no joint, satisfying `COMP-NONEXISTENT`, while the assumptions fail,
  satisfying `COMP-MODEL-INVALID`. If model failure prevents certification,
  `COMP-UNRESOLVED` also applies literally. No printed rule selects the one
  required status.
- Consequence: the substantive warning about feedback is correct, but its
  report codomain overlaps. This can route one physical record to different
  procedural/scientific interpretations.

### M2-05 — Major — the seam/bracketing taxonomy lacks a certifiability route and a simultaneous-pivot state

- Category: mathematical, statistical, outcome routing.
- Affected claims: V2-C11; contract Sections 10.1--10.2.
- Exact evidence: lines 881--912 require exactly one primary seam status.
  `SEAM-ILL-CONDITIONED` requires that the global solve exists, while no status
  covers inability to certify existence or exterior uniqueness. Lines
  919--925 list left-pivot and right-pivot singular states separately but do
  not state whether both may be printed or provide a both-singular/global-
  defined state.
- Countermodel 1: in the scalar equation `theta a_s=1`, let a simultaneous
  confidence set contain `theta=0` and small nonzero `theta`. Model validation
  can pass. At zero there is no solution; away from zero there is a unique but
  unstable solution. The data establish neither `NO-SOLUTION` nor existence,
  so `ILL-CONDITIONED`'s stated premise is not certified. The primary
  classifier has no unresolved status even though the general decision system
  admits underdetermination.
- Countermodel 2: `G=[[0,1],[1,0]]` is globally invertible while both scalar
  diagonal pivots are singular. The list contains no unambiguous single label
  for both sequential bracketings in this case.
- Consequence: the exact range/kernel mathematics survives, but the asserted
  classifier is not exhaustive at finite resolution and its bracketing flags
  are not declared jointly composable.

### M2-06 — Blocking — predecessor failure proves poset minimality, not that an incomparable carrier is required

- Category: mathematical logic, semantic, candidate ordering.
- Affected claims: V2-C13; contract Sections 8.2 and 12.1; outcomes T2--T4 and
  R3--R4.
- Exact evidence: lines 1066--1068 call a passing candidate "required" when
  all applicable strict predecessors fail. Lines 1069--1071 separately permit
  incomparable passing candidates and print a minimal antichain. The outcome
  codes nevertheless call each such carrier `REQUIRED`. Lines 1043--1049 also
  assert `T-B1<T-B3`, although the candidate table at lines 646--649 types
  `T-B1` as physical `S+M` and `T-B3` only as a retained response history; no
  inclusion map or order on the multidimensional cost vector is defined.
- Decisive countermodel: let `p<x` and `p<y` with `x` and `y` incomparable.
  Let `p` fail and both `x` and `y` pass the same duty bundle. The printed test
  calls both `x` and `y` required. But `y` is a passing alternative that does
  not contain `x`, so `x` is not necessary; symmetrically, `y` is not
  necessary. What is established is a minimal passing antichain and the need
  for **some** augmentation beyond `p`, not either carrier individually.
- Consequence: the antichain caveat blocks unique ontology selection but does
  not make the word `required` true. The defect directly affects physical
  outcome flags and resource-necessity claims. The asserted `T-B1<T-B3`
  relation can additionally manufacture a predecessor obligation between
  candidates whose physical carriers are not typed as nested.

### M2-07 — Major — headline outcomes recreate an aggregate transfer flag and leave "only" claims unguarded

- Category: semantic, mathematical logic, outcome routing.
- Affected claims: V2-C6, V2-C13; contract Sections 4.2 and 12.2--12.3.
- Exact evidence: lines 338--345 forbid a scalar `X`; lines 383--388 require
  every transfer coordinate to name its exact duty. Lines 1073--1075 say every
  flag names its candidate and duty bundle. Nevertheless T6 and R7 at lines
  1086 and 1106 say only `SECOND-REGIME TRANSFER FAILS`, without `X_D`, `X_S`,
  `X_C`, or `X_I`. T7 and R9 say `ONLY TARGET-BUILT...PREDICTS` without a rule
  requiring every proper candidate to fail rather than remain
  underdetermined, invalid, or unrun.
- Transfer countermodel: let `C=PASS`, `X_C=PASS`, `X_S=PASS`, `X_I=PASS`, and
  `X_D=FAIL`. The sentence "second-regime transfer fails" is true on an
  existential reading but falsely suggests composition transfer failure; on
  an `X_C` reading the flag is false. The full vector exposes the ambiguity but
  does not define the flag's truth condition.
- Universal countermodel: let a target-built table predict, one proper
  candidate fail, and another proper candidate have an interval straddling its
  margin. The proper candidate may predict; it is unknown. T7/R9's word
  `ONLY` is not established. The careful predecessor-underdetermination guard
  in Section 12.1 is not applied to these universal flags.
- Consequence: the local vector is sound, but the mandatory summary layer can
  again switch transfer subjects or overstate an unknown as a target-built-
  only result.

### M2-08 — Moderate — the context value and comparison-cell component share one symbol

- Category: mathematical notation, semantic/editorial.
- Affected claims: V2-C1, V2-C3; equations (2.2), (2.8), and (2.10).
- Exact evidence: lines 108--115 define `C=(j,s,rho,c)` and explicitly reserve
  `c` for the fourth component, the comparison cell. Lines 241--244 then write
  `Q_{c,a}=P(...|C=c,do(A=a))`, equating the tuple-valued `C` to the
  cell-valued `c`.
- Consequence: prose makes the intended conditioning on a complete frozen
  context recoverable, so this does not independently control the disposition.
  As printed, however, the main estimand overloads two different types and an
  evaluator cannot tell from the formula whether `j,s,rho` are fixed by the
  kernel subscript or marginalized.

## 5. Attacks that survive

The following v2 repairs are substantive and survived independent attack.

1. Literal treatment syntax is not scored, while physical traces,
   noncompliance, and failure remain observable under a frozen access graph.
2. The primary law is intention-to-treat on a common sentinel-completed space;
   successful postselection is not the scientific parent.
3. Exact presentation, statistical matching, and held-out screening are three
   distinct relations; threshold matching is not a quotient.
4. The three-way local and candidate decisions do not force a negative from a
   straddling interval.
5. Calibration/readout uncertainty widens inference and does not, by itself,
   enlarge the scientific margin.
6. Equal coherent `S` is not promoted to equality of stochastic attempt laws.
7. Feedback compatibility and stochastic normalization are separate from the
   deterministic seam solve.
8. The exact seam range/kernel conditions distinguish internal and exterior
   uniqueness.
9. Global prediction controls over a singular sequential pivot, and the two
   bracketings are conformance calculations rather than two experiments.
10. Pairwise-good laws cannot replace one direct triple; the parity mutant is
    detected.
11. The physical port collar is separated from its `S` or stochastic response
    coordinate, and active rewiring is not passive presentation.
12. Memory read, reset, randomization, and isolation retain outcomes,
    backaction, records, destinations, residual coupling, and failures.
13. Target-sized and connected-fit objects can predict but do not earn descent
    or composition credit.
14. An underdetermined predecessor blocks the printed chainwise necessity
    test.
15. The ladder is bounded, arm-specific, source/resource-conditioned, and
    makes no ontology, chronology, spacetime, gravity, or universality award.

## 6. Claim-level audit

| frozen claim | Seat M result | controlling reason |
|---|---|---|
| V2-C1 | survives in structure; notation affected | context/intervention separation is real; M2-08 |
| V2-C2 | survives conditional on access certification | H1--H2; physical records cannot be projected away |
| V2-C3 | does not survive universally | M2-01: nonrandom source closure is not causal identification |
| V2-C4 | survives | exact groupoid, matching, and screening are separated |
| V2-C5 | does not survive as a nonvacuous equivalence contract | M2-02; three-way routing itself survives |
| V2-C6 | formal vector survives; outcome layer does not | M2-07 |
| V2-C7 | survives at fixed-background operational scope | carrier/coordinate and ontology ceiling are explicit |
| V2-C8 | survives | outcomes, backaction, access, destinations, and failures retained |
| V2-C9 | survives | physical collar and complete stochastic coordinate are typed separately |
| V2-C10 | survives | passive presentation and active rewiring/adapters are separated |
| V2-C11 | does not fully survive | M2-03--M2-05 |
| V2-C12 | direct-triple requirement survives | H10 and target-leakage firewall |
| V2-C13 | does not survive | M2-06 and M2-07: minimality is not individual necessity |
| V2-C14 | survives as a preflight/post-run duty | source inventory and multidimensional resource debt remain visible |
| V2-C15 | survives as a bounded governance ladder | no empirical rung is available in this review |
| V2-C16 | survives | all ontology, chronology, spacetime, gravity, and universal promotions barred |

## 7. Disposition, scope, and award

Recommended disposition:

`SPB-D2 — REVISE BEFORE PHYSICAL PIN`

The central SPB question remains nonvacuous in intent, the two physical arms
remain feasible candidate experiments, and v2 genuinely repairs most terminal
v1 defects. Authentication passes, so D0 is not appropriate. The direct
triple, stochastic-interface, physical-record, and no-ontology firewalls also
make rejection of the entire question unwarranted.

The frozen contract nevertheless cannot govern acquisition as printed.
Independently decisive reasons are: a source-closed nonrandom schedule need
not identify its displayed do-kernel; maximal TV thresholds can make both
boundary matching and screening pass under maximal physical disagreement;
and the acyclic composition formula lacks the initial boundary law needed for
the normalization it claims. Candidate “required” flags additionally confuse
minimal passing antichains with necessity, while feedback, seam, and headline
outcome classifiers have overlapping or missing routes.

These are semantic/mathematical/statistical defects, not empirical evidence
for or against a sufficient boundary. They cannot be narrowed away by this
report, repaired in the frozen bytes, or cured by synthetic conformance. A
newly authorized object and pin would be required before any physical SPB
acquisition could be governed.

Award recommendation: none. `SPB-L0` is not earned under D2.

Scientific boundary result: none.

Report LF line count: `000613`

Report byte count: `033833`

Report normalized self-SHA-256:
`1b716ef10af95eff0661b3153285e2d8192882348e1032ec5a90895ca03798f5`

Normalization rule: Normalization replaces decimal digits on the count lines and the 64 hexadecimal digits on the self-hash line by zeroes while preserving every other byte.
