# Paper 04 model-pin audit — Seat M

## Finite constraint, reductions, probability, and exact feasibility

Date: 2026-08-23

Status: **FROZEN INDEPENDENT MODEL-PIN AUDIT**

Seat: **M — finite constraint and reductions**

Verdict: **ACCEPT-FOR-ONE-CONSTRUCTION-WITH-BINDING-SCOPE**

Scientific result evaluated: **none**

Candidate constructed or fitted: **no**

First decisive semantic or implementability blocker: **none**

Sole audited model pin:

- v17/note-paper04-two-clock-parent-construction-pin.md
- ordinary SHA-256:
  8adb5def4c927dd55eba4c2360782b1b6d9370fcf3f5d5c76f5458b1a0fbca4e
- normalized self-SHA-256:
  29e14feae49cc7a88f1da878623c83fead437d82381fe7ce003f10a877480f85
- 758 LF lines and 34,071 bytes

Protocol HEAD authenticated before review:

    7aad87a4cc80f239abf4456d72298c306016c5bf

This report audits whether the frozen finite model is a coherent mathematical
object that can receive one construction. It does not compute the registered
scientific product, fit the affine relation, evaluate a response tensor, or
award operational redundancy.

## 0. Authentication, authority, and blindness

I authenticated the model pin and every authority named in its Section 0
before judging feasibility.

| Authority | Authenticated SHA-256 | LF | Bytes | Disposition |
|---|---|---:|---:|---|
| Paper-04 generic adjudication | d683901fb1fba9da1b21839839cd955270f1c7c7e2405e7948b7b9b3d0b106b5 | 465 | 19,476 | exact |
| Paper-04 generic pin | da48bc95bf02c93393697ad6b447605ab89879ff45a1be6896abf6ce6a276b0c | 1,016 | 45,152 | exact |
| Paper-04 generic Seat-M audit | 2151bee5c6ac9b93f315047f2164c995a7fdbc6726a431ebd992814071d0d204 | 837 | 41,302 | exact |
| Paper-04 generic Seat-Q audit | 3440dd49b51ae8245070c23963c7a51fc43fe5c02a5c54d4308b4cefd71ec8f2 | 825 | 52,916 | exact |
| Paper-04 generic Seat-O audit | 76c2a5d412f56b031ff4e0bbce87a22f9c7ea65a4fe24f62289fbcc12be6defd | 916 | 59,146 | exact |
| Paper-03 v3.2 adjudication | b42fcf6201e249f03772ae2f1e037c2c945e98e4221c89a629d744de937e6104 | 502 | 21,215 | exact |
| Paper-03 v3.2 accepted candidate | 469ae61c849573c9fe7c70871ca6b60843a080082d07f6850b48213b86d6f7d6 | 1,320 | 56,462 | exact |
| v17 era charter | a9f8456763447eaa25a6b840e8f221f51d961ecd9c3ced649ae35a8616457cbe | 476 | 21,268 | exact |

The present report was absent at authentication. I did not inspect, name,
contact, or infer either sibling model-pin report. I edited no candidate,
authority, register, plan, log, or ledger. The only writable artifact used by
this seat is this report.

## 1. Executive mathematical judgment

The frozen parent is finite, exact, and internally constructible. The
essential reason is unusually clean: the coefficient of k_B in the modular
constraint is the unit 2 in Z_7. Consequently each triple
(k_A,k_M,k_Q) has one and only one compatible k_B. This proves that the group
average has a 7^3-dimensional image and makes every B reduction a unitary
coordinate chart. On q not equal to 6, the coefficient 1+q of k_A is also a
unit, making every A reduction a unitary chart on exactly the printed good
sector. At q=6 that coefficient vanishes and the A chart necessarily loses
rank. The stopped sector is therefore a real mathematical boundary, not a
zero-probability nuisance.

The source family is nonempty. In fact every frozen seed has a normalized
uniform B-phase factor. For every charge tuple supported by its remaining
factors, exactly one B charge survives the projector and has nonzero
amplitude. Orthogonality of distinct charge tuples forbids cancellation.
Every frozen normalization denominator is therefore positive; the common
value is 1/7 under the printed normalized seed conventions.

There is also no in-principle obstruction to a physical retained clock
record. What is feasible is not a bare absolute phase measurement asserted
to be a Dirac observable. For B, define the branch map

$$
V^B_\beta=7^{-1/2}\mathcal R_B(\beta).
$$

Then

$$
\sum_{\beta\in\mathbb Z_7}(V^B_\beta)^\dagger V^B_\beta=I_{\rm phys}.
$$

Thus the direct-sum channel whose beta branch is
$V^B_\beta\rho(V^B_\beta)^\dagger$ is a normalized complete instrument into
the B-relative output family. Its classical record is coordinate-bearing and
must transform together with its frame lineage. An analogous construction is
available on the A good sector. This establishes feasibility only. The
construction still owes the complete Paper-03 packet, covariance,
posterior/reader transport, and the exact sequential lift.

The pin therefore passes its halt rule, subject to the binding scopes below.
The strongest possible later result remains a bounded, conditional,
model-level redundancy result. No conclusion about fundamental time,
chronology, spacetime, gravity, ontology, or actuality is made feasible merely
by these algebraic facts.

## 2. Independent finite reconstruction

### 2.1 Representation and projector

Let

$$
D(a,b,m,q)=a+2b+m+q+aq\pmod 7.
$$

Because D is a Z_7-valued diagonal function,

$$
U_gU_h|a,b,m,q\rangle
=\omega^{(g+h)D(a,b,m,q)}|a,b,m,q\rangle
=U_{g+h}|a,b,m,q\rangle.
$$

Also $U_g^\dagger=U_{-g}$. Character orthogonality gives

$$
P_{\rm phys}|a,b,m,q\rangle
=
\begin{cases}
|a,b,m,q\rangle,&D(a,b,m,q)=0,\\
0,&D(a,b,m,q)\ne0.
\end{cases}
$$

Therefore $P_{\rm phys}=P_{\rm phys}^\dagger=P_{\rm phys}^2$. This is a
genuine finite group projector, not an assumed rigging map.

### 2.2 Physical dimension

Since $2^{-1}=4$ in Z_7, the unique compatible B charge is

$$
b(a,m,q)=-4(a+m+q+aq)\pmod 7.
$$

The vectors

$$
e_{a,m,q}=|a,b(a,m,q),m,q\rangle
$$

are an orthonormal basis of the physical space. Hence

$$
\dim\mathcal H_{\rm phys}=7^3=343.
$$

This argument uses neither a fit nor a numerical search.

### 2.3 Source normalization

Write any frozen seed as

$$
|\phi_u\rangle
=7^{-1/2}\sum_b|b\rangle_B\otimes|\xi_u\rangle_{AMQ},
$$

where the separately printed coherent factors are normalized. For each
charge component of $|\xi_u\rangle$, precisely one b survives. Distinct
surviving charge tuples remain orthogonal. Thus

$$
\langle\phi_u|P_{\rm phys}|\phi_u\rangle=\frac17
$$

for U0, U1, USTOP, UA0, UA1, USEQ, UCOH, UAO, and UBO. The construction must
still print this source-by-source rather than import the audit as an emitted
candidate result.

### 2.4 B reduction

With the printed phase convention,

$$
\sqrt7\,{}_B\langle\beta|e_{a,m,q}\rangle
=\omega^{-\beta b(a,m,q)}|a,m,q\rangle.
$$

This sends an orthonormal physical basis to the standard target basis up to
unit phases. Therefore every $\mathcal R_B(\beta)$ is unitary onto
$\mathcal H_A\otimes\mathcal H_M\otimes\mathcal H_Q$. Its inverse is exact
and finite.

### 2.5 A reduction and the stopped sector

For q not equal to 6,

$$
a(b,m,q)=-(2b+m+q)(1+q)^{-1}\pmod 7
$$

is unique. The same basis argument proves that
$\mathcal R_A(\alpha)$ is unitary from the printed physical good sector to
$\mathcal H_B\otimes\mathcal H_M\otimes\mathcal H_Q^{Q\ne6}$.

For q=6,

$$
D(a,b,m,6)=2b+m+6
$$

is independent of a. The physical q=6 sector has dimension 49, but the
partial A phase bra retains only the seven combinations satisfying
$m=-2b-6$. Its image has rank 7 inside the 49-dimensional kinematic
B--M target at fixed q=6. No inverse can exist. This is precisely the
registered A-stoppage/rank-loss branch; it must not be extrapolated to B, M,
or Q.

### 2.6 Printed phase-response identities

Multiplication of a charge component by $\omega^{gc k}$ sends the printed
phase state $|\tau\rangle$ to $|\tau+gc\rangle$. Consequently the frozen
convention yields, on a q eigenstate,

$$
\tau_A\mapsto\tau_A+g(1+q),\quad
\tau_B\mapsto\tau_B+2g,\quad
\tau_M\mapsto\tau_M+g,
$$

and, on an a eigenstate,

$$
\tau_Q\mapsto\tau_Q+g(1+a).
$$

The sign and rate conventions are internally consistent. These identities
are feasibility checks, not awards of operational backreaction.

### 2.7 Temporal-frame map

The common domain in B coordinates is not the whole B-frame target. It is

$$
\mathcal R_B(\beta)\mathcal H_{\rm phys}^{Q\ne6}
=\mathcal H_A\otimes\mathcal H_M\otimes
\mathcal H_Q^{Q\ne6}.
$$

On this subspace,

$$
\mathcal S_{A\leftarrow B}(\alpha,\beta)
=\mathcal R_A(\alpha)\mathcal R_B(\beta)^{-1}
$$

is a unitary from the restricted B-frame space to the printed A-frame
space. It has no global extension as an A-frame equivalence through q=6.
The construction must show the inclusion or support projector explicitly
before transporting packets.

### 2.8 Complete clock-record lift

The kinematic phase PVM $E_B(\beta)$ does not commute with the constraint and
is not, by itself, an endomorphism of the physical Hilbert space. Calling it
a bare Dirac observable would be false. Nevertheless, the reduction maps
make a covariant complete instrument feasible:

$$
V^B_\beta=7^{-1/2}\mathcal R_B(\beta),\qquad
\sum_\beta(V^B_\beta)^\dagger V^B_\beta=I.
$$

The output is the tagged direct sum over beta of B-relative Hilbert spaces,
with the complete posterior and a retained classical beta record. A frame
change acts on both quantum fibers and record/frame tags. The same formula
works for A after restricting and normalizing on the q-not-6 sector; the
q=6 loss branch must remain separately typed.

This is enough to show that a relational complete instrument can exist in
principle. It is not enough to award M4 or M5. The later construction must
prove equality with the intended kinematic phase statistics, normality and
trace preservation on the full packet, and compatibility with every reader
and update.

### 2.9 Sequential/adaptive feasibility

For any two B readings define the exact reduced propagator

$$
W^B_{\beta_2\leftarrow\beta_1}
=\mathcal R_B(\beta_2)\mathcal R_B(\beta_1)^{-1}.
$$

A complete M instrument at beta_1, its retained result, a record-controlled
guard, this unitary transport, and the second complete M instrument at
beta_2 can be composed in the accepted Paper-03 direct-sum packet. The whole
arrow can then be lifted through $\mathcal R_B(\beta_1)^{-1}$ or an equivalent
covariant dilation. This demonstrates in-principle typing.

It does not license two successive bare kinematic Lüders projections of B.
Such a procedure would confuse a frame coordinate with an evolving clock
measurement and could destroy the physical constraint. The construction
must give one reduction--instrument--transport--lift derivation, retain r_1
through the guard, and compare the complete joint law.

### 2.10 Calibration and held-out nonvacuity

The training design has exactly two affine parameters and exactly two
additional registered points. The latter are not used in the fit. The
window $s=0,1,2,3$ is prior to the seven-step recurrence, so no modular
aliasing makes the split vacuous. U0's M reader and the USEQ complete
adaptive reader are additional probability-bearing tests. The no-clock and
mistuned-B baselines have frozen changed objects. Thus the design is
algebraically informative, although exact success or baseline separation is
for the construction to determine.

The affine relation remains a structural consistency test because the
laboratory comparator and constraint share the same predeclared polynomial.
Held-out equality would not empirically select that polynomial.

### 2.11 Sufficiency fork

The full quantum frame map is a unitary on the good sector. It does not imply
that a scalar reading-only stochastic kernel is sufficient. A reading kernel
exists for a specified family of classical readers, but UCOH may retain
off-diagonal phase information inaccessible to that kernel. The frozen fork
is therefore well posed: prove conditional sufficiency for every complete
reader or print exact information loss while preserving the full map.

### 2.12 Recurrence, stoppage, and exact arithmetic

All bare phase responses recur after seven group steps. The declared primary
window ends at step 3, and no winding register exists. The q=6 coefficient
$1+q=0$ gives an exact stopped A sector. All Hilbert spaces, projectors,
probabilities, total-variation comparisons, and reductions are finite
cyclotomic or rational objects, so exact symbolic construction is feasible
without selecting physics through floating-point thresholds.

## 3. Binding scope for the one permitted construction

Acceptance is conditional on all of the following.

**B1 — frozen modular convention.** The construction must use D as a
Z_7-valued charge polynomial and the printed phase convention. Integer
representatives may be used only where the resource ledger explicitly asks
for them.

**B2 — projector proof.** U must be proved a representation before the group
average is used. P must be proved self-adjoint and idempotent; diagonal
enumeration alone is not a substitute.

**B3 — source-by-source denominators.** Every one of the nine physical
sources must print its positive denominator and normalized density. A common
formula may prove them together, but no source may inherit positivity by
assertion.

**B4 — exact reduction domains.** R_B is global. R_A is defined as an
invertible coordinate map only on q not equal to 6. Its q=6 branch must print
the rank loss and must remain in all complete source and failure ledgers.

**B5 — common-sector frame map.** S_A-from-B must display the q-not-6
support projector or restricted domain and codomain. It cannot be applied to
USTOP, even inside a density, instrument, or reader expression.

**B6 — no bare phase PVM as a Dirac endomorphism.** E_A and E_B are
kinematic covariant phase PVMs. A physical clock packet must be obtained by a
proved reduction/lift or equivalent covariant complete instrument. A
kinematic Lüders map that leaves the physical space is not admitted.

**B7 — coordinate-bearing retained records.** A beta or alpha record must
live in a tagged frame output and transform with its lineage. Copying its
bare numeral into a gauge-trivial invariant register is the hidden-origin
mutant, not a covariant record lift.

**B8 — no unpinned parent enlargement.** Paper-03 apparatus memories may
appear as typed output/interface registers with declared gauge and lineage.
They may not be inserted into D, the source family, or the parent dynamics to
repair a result.

**B9 — sequential arrow.** USEQ must be one complete
reduction--instrument--record guard--transport--instrument packet. Program
position, the comparator s, and successive bare B projections are forbidden
triggers.

**B10 — comparator distinction.** U_s is gauge-trivial on physical states.
The laboratory orbit of a kinematic seed is a supplied comparator
description, while parent-relative predictions arise through correlations
and reductions. The construction may not claim that applying U_s evolves a
physical state.

**B11 — full packet transport.** The frame map must transport states,
observables, instruments, posteriors, both clock records, guard memory, and
later readers. Vector-level unitarity does not by itself award M12 or M14.

**B12 — scalar sufficiency is not inherited.** Reading-only sufficiency must
be tested separately for U0, U1, and UCOH on every complete reader. Failure
does not demote the full quantum frame map.

**B13 — calibration scope.** Only the two registered training points fit
(a,b); neither held-out point or baseline may tune any object. Exact
agreement is structural consistency in this declared model, not empirical
selection or universal clock law.

**B14 — baseline lineage.** NO-CLOCK and MISTUNED-B must differ only in
their frozen changed objects. Baseline calibration or reader retuning is not
allowed.

**B15 — recurrence and stop.** No winding number, continuation past the
registered window, or deletion of q=6 is permitted. A stopped A clock does
not imply a stopped universe or stopped B/M/Q subsystem.

**B16 — exact comparison.** Positive equivalence requires exactly zero
maximum total-variation loss over every registered complete finite law.
Floating tolerances and approximate post-result success labels are outside
the model.

**B17 — conditioning and division.** Only positive-support finite
conditionals are normalized. A clock record is not automatically a
future-sufficient cut, and a complete division need not contain a clock
record.

**B18 — no scientific evaluation in feasibility code.** Construction may
use exact symbolic verification after the candidate is frozen, but this
audit authorizes no model change, fit, dimension choice, or output-dependent
branch.

## 4. Model theorem-target reconstruction, M1–M24

The word feasible below means that the frozen target is mathematically
well-posed and no pin-level contradiction forces failure. It is not a
scientific award.

| ID | Independent reconstruction | Pin-audit disposition |
|---|---|---|
| M1 | All authorities, HEAD, pin hashes, LF counts, and byte counts authenticated. | satisfied at audit level; construction must repeat |
| M2 | Character law proves U_gU_h=U_g+h; group average is an orthogonal projector. | exactly feasible; no retuning |
| M3 | Unique b gives dimension 343; every frozen source denominator is 1/7. | exactly feasible; candidate must emit source ledger |
| M4 | Reduction-derived direct-sum A/B instruments can be normalized; q=6 requires loss branch. | feasible only under B6–B8 |
| M5 | Finite direct sums and Paper-03 packets admit one joint law with records and contexts. | feasible, not constructed |
| M6 | Kinematic U_s orbit is fixed by the same polynomial, but is comparator rather than physical evolution. | feasible under B10 |
| M7 | R_B is globally unitary and induces packet transport. | state theorem proved feasible; complete paired semantics open |
| M8 | R_A is unitary for q≠6 and rank-deficient for q=6. | exact domain split feasible |
| M9 | U0 has positive support throughout the good window and both reduced charts exist there. | informative and feasible; probabilities unevaluated |
| M10 | W_B plus complete M instruments and retained guard gives a typed route. | feasible only as one complete sequential arrow |
| M11 | Two affine parameters use two training points; two distinct nonwrapping points are held out. | nonvacuous; pass/fail unevaluated |
| M12 | S_A-from-B is unitary on the restricted common sector. | feasible; full packet map still owed |
| M13 | Full map and scalar kernel are mathematically distinct; UCOH is a registered discriminator. | honest pass-or-loss fork |
| M14 | Finite source/context family permits exhaustive round-trip testing on common support. | feasible; USTOP excluded and printed |
| M15 | Both registered maps are strictly increasing injective Borel maps on finite windows. | exact pushforward feasible |
| M16 | Parent predictor can be defined from projector, sources, records, reductions, and instruments without s. | dependency proof and mutants still owed |
| M17 | Both baselines have precise frozen changed objects and registered sensitive readers. | informative in principle |
| M18 | All dimensions, charge supports, record dimensions, recurrence, and stop domains are finite. | exact ledger feasible |
| M19 | Bilinear term changes A rate with q and Q rate with a under frozen readers. | both operational arms possible; nonzero result unevaluated |
| M20 | U0, U1, and UCOH occupy distinct rate/coherence cases. | multiple-choice fork nonvacuous |
| M21 | Paper-03 output memories, resets, and unresolved arrows can type the four combinations. | feasible; each realization still owed |
| M22 | Pre-fit bytes are independent of this audit's result; later classification remains product-valued. | formal/pre-fit classification feasible |
| M23 | All 28 generic coordinates and 14 model coordinates have distinct slots. | complete product preserved |
| M24 | Every actuality, causal, geometry, ontology, and gravity wall is explicit. | binding and nonwaivable |

## 5. Generic hostile attacks 1–68

Each attack is separately preserved. At pin level the disposition records
whether the frozen model has an exact refusing comparison and which theorem
family it threatens. Actual mutant results remain for construction and review.

| # | Changed object | Required model disposition | Primary affected target |
|---:|---|---|---|
| 1 | Clock record replaced by causal-slot rank | refuse supplied-order surrogate | M16, M24 |
| 2 | Clock record replaced by path length | refuse supplied-geometry surrogate | M16, M24 |
| 3 | Clock record replaced by source-code order | permutation control must detect | M16 |
| 4 | Clock record replaced by run counter | hidden schedule; refuse | M16 |
| 5 | Presentation order permuted | physical law invariant; smuggler changes | M16 |
| 6 | B is only a renaming of A | fails distinct subsystem requirement | M4, M5 |
| 7 | A outcome copied into B field | record-copy channel, not second clock | M4, M5 |
| 8 | Affine postprocessing of A called B | coordinate change, not independent clock | M4, M15 |
| 9 | Both calibrations fit on heldout data | leakage; refuse | M11 |
| 10 | Good window selected after residuals | semantic retuning; refuse | M11, M18 |
| 11 | Clock selected after system outcome | future/output leakage; refuse | M5, M20 |
| 12 | Future outcome enters clock definition | acausal conditioning mutant; refuse | M5, M24 |
| 13 | Zero-support event normalized | undefined conditional; refuse | M5 |
| 14 | Convenient diffuse null posterior | inapplicable finite model; generic refusal retained | M23 |
| 15 | Null version called new physics | inapplicable finite model; a.e. wall retained | M23 |
| 16 | First clock record dropped before guard | adaptive packet untyped | M10 |
| 17 | Clock memory hidden outside boundary | completeness/lineage failure | M4, M10 |
| 18 | Only one-time marginals compared | insufficient sequential reader | M10 |
| 19 | Sequential backaction deleted | different instrument; fail | M10 |
| 20 | Same reading histories Markovized | forbidden history loss | M10, M21 |
| 21 | Separate parent states for A/B | violates common-parent source | M5, M12 |
| 22 | Separate system laws for A/B | retuning; refuse | M5, M12 |
| 23 | Constraint appended after target | formal wrapper mutant | M22 |
| 24 | Factorization chosen adaptively | unregistered model replacement | M22 |
| 25 | Hamiltonian changed by clock choice | multiple laws, not frame change | M12, M20 |
| 26 | Kinematic inner product used physically | wrong normalization | M2, M3 |
| 27 | Page–Wootters invoked without solutions | representation claim fails | M2, M7, M8 |
| 28 | Only one-time PW probabilities | M10 remains unconstructed | M10 |
| 29 | Trinity invoked outside hypotheses | source claim refused | M7, M8, M12 |
| 30 | Forbidden ideal sharp time operator | not this finite phase PVM | M4 |
| 31 | Infinite clock proves finite claim | wrong model; refuse | M18 |
| 32 | Finite clock assigned infinite runtime | recurrence control kills | M18 |
| 33 | Wraparound ignored | fail recurrence ledger | M18 |
| 34 | Path position supplies winding | hidden schedule; refuse | M16, M18 |
| 35 | Same phase reused across cycles | global time claim fails | M18 |
| 36 | Stopped A reused as progressing clock | A-domain violation | M8, M18 |
| 37 | Noninjective label map called gauge | lossy coarse graining, not M15 | M15 |
| 38 | Orientation reversed and physical reversal inferred | outside registered gauge | M15, M24 |
| 39 | Labels transformed without PVM | incomplete covariance | M15 |
| 40 | PVM transformed without measure/calibration | incomplete pushforward | M15 |
| 41 | Different paths forced to agree | comparator-scope violation | M11, M24 |
| 42 | Proper-time difference called noise | gravity imported/erased | M24 |
| 43 | Increasing readings yield causal order | supplied-order wall kills | M24 |
| 44 | Category direction yields time orientation | syntax-to-physics fallacy | M24 |
| 45 | One material clock made global | locality/scope overclaim | M24 |
| 46 | KMS/material state made foliation | ontology/relativity overclaim | M24 |
| 47 | Entire interaction deleted | paired no-interaction mutant | M19 |
| 48 | Only system-to-clock arm deleted | reciprocity test must change | M19 |
| 49 | Readout disturbance deleted | different instrument | M4, M10 |
| 50 | System law retuned after disturbance | semantic repair; refuse | M19 |
| 51 | Clock resource cost hidden | ledger failure | M18 |
| 52 | Joint clock law factorized | destroys constraint correlations | M5 |
| 53 | Entanglement discarded in frame change | incomplete quantum transport | M12, M13 |
| 54 | Lossy channel called invertible | exact loss must print | M13, M14 |
| 55 | Round trip tested on one state | all-source/context gate fails | M14 |
| 56 | Incomplete readers certify equality | operational quotient incomplete | M13, M14 |
| 57 | Barandes target index renamed clock | comparator s smuggling | M16, M22 |
| 58 | Every clock record called division | record/division distinction fails | M21 |
| 59 | Every division called tick | converse distinction fails | M21 |
| 60 | Indivisible history factorized at readings | illicit Markovization | M10, M21 |
| 61 | Clock-neutral representation made unique ontology | ontology wall kills | M24 |
| 62 | Affine clock agreement made metric | spacetime wall kills | M24 |
| 63 | Clock ordering made operational chronology | supplied-order wall kills | M24 |
| 64 | GR time dilation imported as result | gravity wall kills | M24 |
| 65 | Arbitrary target wrapped in history state | formal-parametrization classification | M22 |
| 66 | External parameter encoded in generator | dependency mutant must detect | M16 |
| 67 | Constraint selected after heldout inspection | post-fit model replacement | M22 |
| 68 | Parameter-free notation made timeless ontology | fundamental-time wall kills | M24 |

No generic attack is silently merged with an X control. Attacks 14 and 15
are not operationally active in this finite atomic model, but their generic
a.e. refusal remains in the product and source scope.

## 6. Model-specific controls X1–X24

| ID | Independent audit | Required construction disposition |
|---|---|---|
| X1 | Changing 7 changes Hilbert spaces, inverses, recurrence, and data design. | refuse as semantic replacement |
| X2 | Changing coefficient 2 changes constraint, B chart, and comparator rate. | refuse after freeze |
| X3 | Deleting aq removes both printed cross-rate mechanisms. | execute paired mutant; no retuning |
| X4 | cI contributes only a sector/global phase and cannot encode reciprocal response. | inert-control refusal |
| X5 | USTOP has denominator 1/7 and cannot be dismissed. | completeness failure if removed |
| X6 | Dephasing UCOH changes the state and can erase frame information. | full-frame/scalar test must detect or report |
| X7 | U0 alone cannot test q or a interventions. | M19/M20 unconstructed |
| X8 | A and B are different tensor factors with different charge coefficients. | lineage collision must fail |
| X9 | A-to-B copy is an output channel, not the frozen B subsystem. | one-clock classification |
| X10 | Four-point fitting consumes the heldout evidence. | fail M11 |
| X11 | Either omitted point removes the frozen overidentification. | fail M11 |
| X12 | Exact finite TV is available; positive tolerance is needless retuning. | refuse |
| X13 | s is not a parent-relative input and must fail lineage/dependency. | hidden-time detection |
| X14 | Lookup bytes reintroduce s even if signature hides it. | hidden-time detection |
| X15 | Program position is not a physical beta record. | fail M10/M16 |
| X16 | r_1 is needed by the parity guard. | adaptive arrow untyped |
| X17 | Effects omit posterior disturbance and cannot define USEQ. | fail M4/M10 |
| X18 | q=6 is a normalized registered source and exact rank-loss sector. | refuse deletion |
| X19 | Winding counter is a new physical subsystem not in the pin. | refuse |
| X20 | Identity has no discriminatory value for covariance. | M15 unconstructed |
| X21 | Partial label pushforward is not packet covariance. | fail M15 |
| X22 | The comparator path supplies order; readings do not derive it. | M24 firewall |
| X23 | Modular representatives are not a semibounded energy theorem. | resource/ontology refusal |
| X24 | Conditional finite-model success does not imply ontology or gravity. | terminal walls |

## 7. Fresh Seat-M semantic countermodels

These attacks are independent of the generic 68 and X1–X24. They are
countermodels or changed-object tests to be retained by construction review.

### F1 — exponent without modular quotient

Interpret D with unreduced integer multiplication while retaining g in
Z_7, then compare representatives after adding 7. The purported U becomes
presentation-dependent unless the exponent is reduced modulo 7.

Disposition: B1; exact modular convention required.

### F2 — composite-modulus lookalike

Keep the formula but replace Z_7 by Z_8. The coefficient 2 is no longer
invertible, so the unique-b proof and global B reduction collapse.

Disposition: demonstrates why X1 is semantic and why M3/M7 must be proved,
not pattern-matched.

### F3 — non-character phase convention

Replace the phase basis by vectors with outcome-dependent nonadditive phases.
The displayed label translations cease to follow from U_g.

Disposition: printed Fourier phase basis is load bearing.

### F4 — omitted square-root normalization

Use the partial bra without the factor sqrt(7). The map is a contraction by
1/sqrt(7), not a unitary reduction, and density traces are wrong.

Disposition: M7/M8 fail.

### F5 — accidental A inverse at q=6

Choose one a representative in each q=6 fiber and call it an inverse. This
is a noncanonical section of a rank-deficient map and discards six
independent directions per compatible (b,m).

Disposition: B4; stoppage must print.

### F6 — unrestricted frame composition

Apply R_A R_B inverse to a B-frame density with q=6 support. R_A is outside
its domain, so the expression is not a channel and any apparent trace loss
is a typing error.

Disposition: B5; explicit common-sector projector required.

### F7 — bare kinematic phase PVM as physical

Apply E_B(beta) rho E_B(beta) to a physical rho and retain the kinematic
posterior as physical. E_B does not commute with P_phys, so the posterior
need not satisfy the constraint.

Disposition: B6; use a reduction-derived or gauge-invariant complete lift.

### F8 — invariant numeral record

Construct the correct direct-sum quantum branches but place beta in a
gauge-trivial classical register that is unchanged under frame transport.
This silently chooses an absolute phase origin.

Disposition: B7; transform the record and frame lineage.

### F9 — branch probabilities without posterior fibers

Keep the uniform beta probabilities from the direct-sum instrument but
replace every conditional output by the same nonselective physical state.
One-time clock counts survive while relational M/Q predictions fail.

Disposition: M4/M5 require complete branch posteriors and later readers.

### F10 — sequential double projection

Project kinematic B sharply at beta_1, apply the guard, and project the same
static B factor at beta_2 without reduced propagation. This is not the
registered relational sequence and generally leaves the constraint space.

Disposition: B9; exact W_B transport and complete lift required.

### F11 — forgotten guard record

Compute the parity branch from r_1, then erase r_1 before the output packet.
The final marginal can be preserved while complete record laws and future
readers differ.

Disposition: M10 fails.

### F12 — comparator gauge action called physical evolution

Apply U_s to rho_phys and claim a changing physical state. Since U_s acts as
the identity on D=0, this construction predicts no evolution and confuses
gauge orbit representatives with relational change.

Disposition: B10; comparator and parent reductions must be separated.

### F13 — coherent-source classicalization

Replace UCOH by the q=0/q=1 mixture only inside the scalar-sufficiency test.
All charge-diagonal clock marginals may agree while frame-sensitive
off-diagonal readers change.

Disposition: B12 and X6.

### F14 — wrapped calibration masquerading as affine

Represent phase 6 as minus 1 for one point but as 6 for another, allowing an
output-dependent affine fit across the cycle.

Disposition: B13/B15; fixed integer representatives and nonwrapping window.

### F15 — baseline recalibration

Change B's coefficient to 3 and refit the affine map for the mutant. This can
hide the intended time-sensitive difference by changing both law and
interpretation.

Disposition: B14; mutant calibration remains frozen.

### F16 — global-phase interaction

Replace aq by a constant or by a charge term constant on every tested source
and claim backreaction from a changed generator phase. No registered
complete-reader distribution need change.

Disposition: operational two-arm difference is necessary for M19.

### F17 — extra memory in the parent constraint

Add a seven-state winding or record factor to D so the sequence becomes easy
to order. This changes the frozen parent dimension and injects the missing
clock history.

Disposition: B8/B15; semantic replacement, not implementation.

### F18 — source normalization by postselection

Delete charge components that fail D before applying P_phys and renormalize
the kinematic seed, thereby presenting a hand-selected physical source as
the projected frozen source.

Disposition: B3; exact projector lineage required.

### F19 — unitary vector map but incomplete packet

Prove S is unitary and then leave guard memory, classical records, instruments,
and posterior readers untouched. Coherent vectors round-trip while complete
operational laws need not.

Disposition: B11; M12/M14 remain unconstructed.

### F20 — exact arithmetic replaced by tolerance search

Use floating eigenvectors and choose a total-variation tolerance after
observing residuals. Numerical gauge phases can then manufacture either a
pass or failure.

Disposition: B16/B18; exact finite arithmetic and frozen zero threshold.

## 8. Full product and outcome ceiling

### 8.1 Generic Paper-04 coordinates

This is a pre-construction audit. Except for input authentication and fixed
walls, none of the following scientific coordinates is awarded.

| # | Coordinate | Pin-level disposition |
|---:|---|---|
| 1 | P04-UPSTREAM-P03V32-PRESERVED | binding authority; construction must verify |
| 2 | P04-CLOCK-A-PHYSICAL-PACKET-CONSTRUCTED | open, feasible under B4/B6/B7 |
| 3 | P04-CLOCK-B-PHYSICAL-PACKET-CONSTRUCTED | open, feasible under B6/B7 |
| 4 | P04-TWO-CLOCK-JOINT-LAW-CONSTRUCTED | open, finite packet feasible |
| 5 | P04-FINITE-CLOCK-CONDITIONING-CONSTRUCTED | open; positive-support rule fixed |
| 6 | P04-DIFFUSE-CLOCK-CONDITIONING-AE-CONSTRUCTED | not applicable to primary finite model; generic scope retained |
| 7 | P04-ORDINARY-CLOCK-RELATIVE-ADEQUACY | open |
| 8 | P04-SEQUENTIAL-ADAPTIVE-CLOCK-ADEQUACY | open, nonvacuous |
| 9 | P04-SAME-PATH-AFFINE-AGREEMENT | open, heldout split nonvacuous |
| 10 | P04-CLOCK-FRAME-TRANSFORMATION-CONSTRUCTED | open; good-sector state map feasible |
| 11 | P04-CLOCK-ROUNDTRIP-EQUIVALENT / loss / failure | open; all-context packet test required |
| 12 | P04-CLOCK-NEUTRAL-PARENT-CONSTRUCTED | open; exact finite parent specified pre-fit |
| 13 | P04-LABORATORY-REDUCTION-FROM-PARENT-CONSTRUCTED | open |
| 14 | P04-PAGE-WOOTTERS-TRINITY-COMPARATOR | open under exact finite hypotheses |
| 15 | P04-POSITIVE-STOCHASTIC-PARENT | not applicable unless separately constructed |
| 16 | P04-REPARAMETRIZATION-COVARIANCE-CONSTRUCTED | open; two nonidentity maps feasible |
| 17 | P04-HIDDEN-EXTERNAL-TIME-EXCLUDED | open; dependency mutants fixed |
| 18 | P04-FINITE-CLOCK-LIMITS-CONSTRUCTED | open; recurrence/stop exact |
| 19 | P04-CLOCK-BACKREACTION-CONSTRUCTED | open; both arms possible |
| 20 | P04-STOPPED-RECURRENT-CLOCKS-CLASSIFIED | open; exact q=6 and period-7 structure present |
| 21 | P04-CLOCK-CHOICE-INDEPENDENT / DEPENDENT | open honest fork |
| 22 | OPERATIONALLY-REDUNDANT / FORMAL-ONLY / NOT-REDUNDANT | open; cannot follow from 7/9/16 alone |
| 23 | P04-CAUSAL-ORDER-STILL-SUPPLIED | mandatory wall |
| 24 | P04-ONTOLOGY-SELECTION-UNCONSTRUCTED | mandatory wall |
| 25 | P04-SPACETIME-CHRONOLOGY-UNCONSTRUCTED | mandatory wall |
| 26 | P04-GRAVITY-UNCONSTRUCTED | mandatory wall |
| 27 | P04-FUNDAMENTAL-TIME-STATUS-UNSELECTED | mandatory wall |
| 28 | P04-ACTUALIZATION-UNCONSTRUCTED | mandatory wall |

### 8.2 Model-selection coordinates

| Coordinate | Pin-level disposition |
|---|---|
| P04M-MODEL-PIN-AUTHENTIC | authenticated by this audit |
| P04M-FINITE-GROUP-PARENT-CONSTRUCTED | open; coherent exact target |
| P04M-PHYSICAL-SOURCE-FAMILY-NONEMPTY | feasibility proved; candidate award open |
| P04M-B-REDUCTION-GLOBAL | feasibility proved; complete packet award open |
| P04M-A-REDUCTION-Q-NOT-6 | feasibility proved; complete packet award open |
| P04M-A-STOPPED-Q-6 | exact rank-loss mechanism present; classification open |
| P04M-COMPLETE-RELATIONAL-INSTRUMENTS-CONSTRUCTED | open; covariant lift possible |
| P04M-HELDOUT-SEQUENTIAL-LAW-REPRODUCED | open |
| P04M-FULL-QUANTUM-FRAME-MAP-CONSTRUCTED | open; restricted state map possible |
| P04M-READING-ONLY-SUFFICIENCY-PASS-OR-FAIL | open honest fork |
| P04M-RECIPROCAL-INTERACTION-PASS-OR-FAIL | open honest fork |
| P04M-MULTIPLE-CHOICE-PASS-OR-DEPENDENT | open honest fork |
| P04M-HIDDEN-TIME-EXCLUDED-OR-DETECTED | open discriminator |
| P04M-FORMAL-ONLY-OR-OPERATIONAL-REDUNDANCY | open terminal classification |

### 8.3 Earliest rung and ceiling

No pin-level inconsistency forces the first three failure rungs. No positive
scientific rung is awarded. The construction begins at authenticated input
with a feasible two-clock parent target, and its earliest actual failed rung
must control its result.

Even a perfect later finite product cannot exceed:

> One independently frozen finite constrained parent supplies equivalent
> complete clock-relative predictions on a bounded registered domain, with
> the external comparator parameter operationally unused there.

It cannot establish a seven-state universe, a fundamental gauge time,
chronology, causal order, Lorentzian geometry, gravity, a unique ontology, or
an actual history.

## 9. Primary-source scope audit

The pin uses the cited primary literature conservatively.

- Page and Wootters supplies the stationary-parent/conditional-dynamics idea,
  not unique factorization, an ontology, or sequential adequacy for free.
- Höhn, Smith, and Lock supplies equivalence of relational reductions only
  under constraint, clock, physical-inner-product, and domain hypotheses.
  The present finite basis proof makes those hypotheses testable rather than
  presumed.
- Höhn, Krumm, and Müller supports finite-Abelian group averaging and
  internal-frame reductions. It does not turn a finite reference frame into
  time or make all frame changes globally valid.
- Giovannetti, Lloyd, and Maccone makes complete sequential probabilities a
  load-bearing test; it does not license the double-projection mutant F10.
- Smith and Ahmadi supports interaction-dependent relational dynamics; it
  does not award reciprocal operational response merely because aq appears
  in D.
- Giacomini, Castro-Ruiz, and Brukner supports transforming complete quantum
  states, observables, and dynamics, which is why B11 is binding.
- Periodic-clock results support cycle-relative scope and do not supply the
  missing winding record.
- Barandes retains external conditioning/target time indices in the cited
  framework. Renaming one of those indices beta would not solve this paper's
  problem.

None of the sources selects p=7, the charge polynomial, the source family,
the external comparator, a preferred clock, or a timeless ontology. Exact
agreement in this model would remain a conditional structural result.

## 10. Final verdict

**ACCEPT-FOR-ONE-CONSTRUCTION-WITH-BINDING-SCOPE**

The model pin is algebraically coherent, its source family is nonempty, its
B and good-sector A reductions have exact finite inverses, its stopped sector
is honestly exposed, its calibration/heldout split is nonvacuous, and a
covariant complete record lift exists in principle. No implementation or fit
is needed to establish this feasibility.

The most important restriction is physical, not cosmetic: the bare clock
phase PVM is not itself a Dirac endomorphism of the constrained physical
space. The admissible construction must derive complete clock packets through
reduction/lift or an equivalent gauge-covariant instrument, and must transport
the coordinate-bearing record with its frame lineage. If that theorem fails
for the complete Paper-03 packet, M4/M5/M10 fail scientifically; the frozen
parent may not be enlarged or repaired.

First exact semantic counterexample: **none**.

First possible construction-level failure to watch: inability to extend the
state-level reduction instrument to one complete covariant sequential packet
with retained record lineage. This is an open theorem target, not a pin
contradiction.

## 11. Freeze metadata

Protocol/model-pin HEAD authenticated:
7aad87a4cc80f239abf4456d72298c306016c5bf

Model pin ordinary SHA-256:
8adb5def4c927dd55eba4c2360782b1b6d9370fcf3f5d5c76f5458b1a0fbca4e

Report LF line count: 000881

Report byte count: 041768

Report normalized self-SHA-256:
e4db2a28790b87f02350e2c822a2586701d16a30877fc90330821ea22bf9ed8e

Normalization rule: replace the six decimal digits on each report count line
and the 64 hexadecimal characters on the report normalized-self line by
ASCII zeroes, preserve every other byte, and compute SHA-256. The report uses
LF endings, ends in one LF, and has no trailing horizontal whitespace.
