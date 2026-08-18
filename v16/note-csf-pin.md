# CSF — completeness spectrahedra, record fibers, and recurring-context selection

Status: **PIN — FROZEN BEFORE CONSTRUCTION**.

Authorization: on 2026-08-18 the user explicitly instructed “go ahead” after
the proposed Paper 6 scope was separated from the nine-item ontology ledger.
This starts Paper 6 as a separate v16 continuation. It does not edit, repair,
review, rescore, or terminalize Papers 3, 4, or 5.

Immutable base commit: `5cba6f79270e6662d2e739a67cfe50eeaa465c58`.

## One boxed question

> For a fixed, record-individuated family of typed history maps, do all-input
> complete unconditioned laws form an exact positive-semidefinite affine
> slice; how do calibrated record-resolving instruments sit above that slice;
> and does requiring one covariantly identified history law to recur across
> independently constructed overlap contexts select a unique law, reduce its
> freedom, make it inconsistent, or leave it underdetermined?

For typed histories `V_h : H_in -> H_out` and calibrated output ports `j`, the
candidate object is

```text
K_j = sum_h c[j,h] V_h,
C   = (c[j,h]),
M   = C^dagger C,
L_V(M) = sum_h,k M[h,k] V_h^dagger V_k.
```

The all-input completeness condition is `L_V(M)=I`. Under this convention the
unconditioned channel is

```text
Phi_M(rho) = sum_h,k M[h,k] V_k rho V_h^dagger.
```

Thus the proposed unconditioned law space at fixed typed histories is

```text
S_V = { M Hermitian positive semidefinite : L_V(M)=I }.
```

The unit calls this a **completeness spectrahedron** only at that fixed-history
scope. A factorization `C^dagger C=M` is an **instrument-realization fiber**.
Two factorizations in one fiber have the same unconditioned channel, but they
need not be physically equivalent when their port labels are calibrated and
retained as records.

## External proposal: adopted claims and frozen corrections

The user supplied an exact scratchpad report proposing the spectrahedral
formulation, a two-history rich-spectrum decoherence theorem, partially
overlapping order flags, an embedding of JCV, and an extreme-point selection
speculation. Those scripts and their results are motivation only. They are
excluded from the runtime read set and must be reconstructed after the generic
core freezes.

The pin pre-registers these corrections before construction:

1. `M` is the unconditioned base, not the whole outcome-resolved instrument.
   A calibrated `C` can move a retained port statistic while `M` stays fixed.
2. `M[h,k]=0` proves absence of that cross-history term in the unconditioned
   law. It does not prove that an order was actualized, durably recorded, or
   ontologically classical.
3. Orthogonal flag states are present distinguishability, not permanence.
   Durability requires the continuation census inherited from Paper 3.
4. A spectrahedron's extreme points need not be rank one or unique, and
   extremality need not survive restriction, coarse-graining, spectators, or
   catalogue enlargement. “No unearned decoherence” is a conjecture to attack,
   not a principle to assume.
5. Equating `M` across contexts is a recurring-history-law hypothesis. It is
   not automatically vertex locality. The cross-context dictionary and its
   gauge covariance are measured objects, and doctrine-sensitive selection is
   a first-class outcome.

## Immutable antecedents and path-value anchors

Runtime code may read only the committed paths below through the immutable
base commit. Every read product must be consumed by a named anchor gate. The
user-supplied scratchpad paths, scripts, calculations, and prose are not
runtime inputs and are not evidence.

| committed path | SHA-256 at immutable base | binding use |
|---|---|---|
| `v16/paper-05-overlap-gram-instrument-variety.md` | `89a6ad8b10b97351d71a499ebbb36b2cf5a89f32d5ec9d005f9b4a68dab16b31` | common-boundary history maps, exact port completeness, unitary spectral classifier, nonnormal refusal, and the unselected overlap-law result |
| `v16/code/ovg_receipt.json` | `4ba954430acd0772da62c8df16b2c6b08bca9e76fd7b25d3b5b72fcc43ce2852` | exact OVG regression values, not Paper 6 conclusions |
| `v16/note-ovg-candidate-verification.md` | `12774e1a2d9d72d147a67e066679bc6e376e29f4acecc453f3d164ce19ba37e5` | replay and scope status; Paper 5 remains green-unreviewed |
| `v16/paper-02-joint-comparison-fixed-point.md` | `e06e7ce1ec59397e05ccafa1e51d3bf78e888d0c0b72c214144deb9ba92e9e39` | real `I/Z` boundary-instrument equations and the local weight variety |
| `v16/note-jcv-adjudication.md` | `6499650c474c6f8ed6e2701ebf113fbbf956360ccb3f22a426cba3a2a5e859a1` | exact same-channel/different-record witness pair and the third channel-moving witness |
| `v16/paper-03-contextual-pullbacks-permanent-records.md` | `ca7b06e9e5540d81afb4a401beb66cb2834e3e74033fd742ac5257108a19654f` | continuation-stable null quotient, eraser/permanence distinction, and record-individuated histories |
| `v16/paper-04-support-rewrite-weld.md` | `f61dde79e5fc0e10db1e5dbe13dec25dceaff9842d5e0c5c06ba2ae90eb4bcae` | typed bundle morphism, configuration catalogue, local coupling, and recurrence debts |
| `v16/paper-01-joint-relational-history-law.md` | `98489edb6a83919199c11b14b92c423965d1a08ad7652a1c1915d5402f9e6003` | all-input CP-instrument obligation, fixed-factor no-signalling, and law-selection scope |
| `v12/paper1-composition-defect.md` | `81bdab5673fb67b63cd10c08fbb80870f8aa01088047718c5b4bf447e1669128` | configuration-individuated histories, record/composition theorem, and reduced boundary gauge |
| `v15/note-homonym-audit.md` | `4dbdb8f932e1b4e3d3813c7dcb9d2905f37b4c42819cc14537afa993e2ce51d9` | E-34 term separation and complete-successor sample-space discipline |

No v15 SCOUT-T path belongs to the read, cite, write, stage, or archive set.

## Term-binding table

| term | bound object | explicitly not identified with |
|---|---|---|
| **typed history map** | one record-individuated complete-history operator `V_h` with independently fixed domain, codomain, and relational-event label | an arbitrary Kraus column; an ontic microscopic trajectory; a history chosen after solving completeness |
| **history coordinate** | one basis element of the frozen relational history-event algebra modulo the continuation-stable null relation admitted by the fixture | an arbitrary linear recombination of configuration-distinct events |
| **port coefficient matrix** | `C=(c[j,h])`, resolving fine histories into mutually exclusive complete output ports | the unconditioned law by itself; a selected measurement implementation |
| **history Gram law** | `M=C^dagger C`, a positive-semidefinite kernel on the typed history coordinates | the wavefunction; spacetime geometry; the complete calibrated instrument |
| **completeness spectrahedron** | the affine PSD slice `S_V={M>=0:L_V(M)=I}` for fixed typed `V_h` | the union over changing catalogues, transports, or history dictionaries; a selected physical law |
| **instrument-realization fiber** | all exact `C` with `C^dagger C=M`, quotienting only port transformations unobservable under the declared calibration | the older v7/v15 uses of “record fiber”; automatic gauge under arbitrary port mixing |
| **calibrated port record** | an outcome label with an independently declared readout whose resolved statistics are retained | a Kraus label ignored by every observable; a durable record without a future census |
| **unconditioned history coherence** | a nonzero off-diagonal component of the physical kernel after the admitted history gauge/null quotient, evidenced in `Phi_M` | coherence inside one chosen factorization `C` whose cross terms cancel after ports are forgotten |
| **flag overlap** | the derived inner product `w=<f|g>` of two typed tag states attached to histories | durable which-order information; actualization |
| **recurring-history law** | one covariantly identified `M`-parameter packet required to satisfy several independently constructed contexts | same local QFT vertex; same numeral reused in fixtures; a derived law of nature |
| **recurrence dictionary** | the predeclared event-algebra and gauge-covariant map identifying history coordinates and law parameters between contexts | a comparison selected after seeing which intersection is smallest |
| **vertex-local law** | a rule deriving each context's history kernel from shared elementary-event couplings and local relational data | equality of full `M` matrices across contexts unless separately proved |
| **extreme point** | an extreme element of the fixed affine PSD set, certified by the tangent-support criterion | a pure ontic law; a rank-one matrix in general; a uniquely preferred law |
| **law selection** | one empirically equivalent law class forced by independently justified recurrence, symmetry, completeness, and composition constraints | choosing one extreme; finding a nonempty spectrahedron; conditional uniqueness under an arbitrary dictionary |
| **actualization** | the separate postulate that one complete recorded successor occurs | factorizing `M`, decoherence, conditioning, or extremality |

Probabilities normalize over mutually exclusive complete ports. Fine histories
inside a port are coherent contributions, not separately normalized outcomes.

## Arena coordinates

| coordinate | frozen declaration |
|---|---|
| **boundary** | finite exact common-boundary history families, primarily two-history unitary sectors plus one nonnormal/dimension-changing control |
| **relational arena** | at least three independently constructed overlap contexts carrying the same declared ordered history grammar, plus one held-out context and relabel/gauge controls |
| **family** | exact Hermitian kernels over `Q(i)`, exact affine operator constraints, PSD certificates by exact minors/factorizations, and calibrated finite port factorizations |
| **law** | `M` at unconditioned grain and `C` at retained-record grain; elementary history transports remain frozen inputs rather than selected outputs |
| **state** | all-input operator identities and ancilla-stable channel equality primary; selected-state screens are secondary witnesses |
| **gauge** | event-algebra-preserving history permutations/rephasings, boundary frames, null dilations, and unobserved port isometries; calibrated port mixing and arbitrary history mixing are not presumed gauge |
| **recurrence doctrine** | identity, gauge-conjugate, exchange-covariant, and one deliberately inequivalent cross-context dictionary are separately tested |
| **provenance** | immutable base `5cba6f79270e6662d2e739a67cfe50eeaa465c58`; external scratchpads excluded |
| **runtime** | 300 seconds per ordinary or mutant invocation; exact arithmetic only |

## Four-gate audit for new objects

| object | referent | necessity | no-smuggling | discriminator |
|---|---|---|---|---|
| spectrahedral base | exact Hermitian history kernel constrained by the fixed `V_h` | completeness is quadratic in `C` but linear in `M`; the quotient must be tested rather than assumed | `M` is computed from symbolic Gram coordinates before physical witnesses are known | two `C` with one `M`, a third `M`, a non-PSD affine solution, and a completeness mutant separate the cases |
| record-resolution fiber | exact factorizations of one `M` with declared port calibration | JCV already has same unconditioned channel and different retained outcomes | port equivalence is determined by calibration, not by equality of unconditioned channels | unobserved port rotation leaves all admitted data fixed; calibrated rotation moves a retained statistic |
| history-gauge quotient | event-preserving rephasings/permutations and continuation-stable null directions | raw off-diagonal coordinates are representation-dependent | the permitted group is fixed from the event algebra before coherence is read | rephase/permutation covariance passes; forbidden event mixing and null-reactivation controls fail |
| rich-spectrum cross-moment test | exact two-history completeness equation for a unitary relative operator with at least three distinct eigenphases | the proposed ensemble theorem locates the residue of the refuted port-level no-go | every Hermitian `M`, not selected coefficient points, is solved | scalar, two-phase, rich-phase, and nonnormal controls return different real-linear ranks |
| flag attenuation | common-boundary histories tensored with independently specified tag states | tests whether partial order distinguishability suppresses the ensemble cross term | `w` is measured from tag vectors; durability is not inserted | `w=1`, partial `w`, `w=0`, and an eraser continuation separate overlap from permanence |
| recurrence dictionary | typed identification of history coordinates and kernel parameters between contexts | an intersection is meaningless without knowing which parameters recur | fixed before context constraints are solved and tested under its own gauge action | identity, rephase, exchange, and inequivalent dictionaries are compared by gauge-invariant predictions |
| recurring-context intersection | exact intersection of the pulled-back spectrahedra under one frozen dictionary | a single compatibility surface cannot select a law | every context is constructed independently; no context is chosen because it removes a desired dimension | one-context, two-context, rich-context, symmetry, and held-out rows measure successive dimension changes |
| exchange symmetry | declared automorphism interchanging the two record-individuated histories and their calibrated roles | the rich-spectrum intersection otherwise retains diagonal bias | imposed only where the relational/context data carry the automorphism; asymmetric control forbids it | symmetric context fixes equal diagonal weights; calibrated asymmetry moves under the swap and blocks the reduction |
| extreme-point assay | exact tangent-support nullspace at a feasible `M` | tests the proposed “no unearned decoherence” route without assuming it | extremality is computed, never identified with rank or purity | rank-one/non-rank-one controls and restriction/coarse-graining/spectator maps test stability |

## Mathematical core to construct

For fixed maps `V_1,...,V_n`, the generic core constructs the real-linear map
from Hermitian `n x n` coordinates to Hermitian input operators,

```text
L_V(M) = sum_h,k M[h,k] V_h^dagger V_k.
```

It returns exact affine equations for `L_V(M)=I`, their rank/nullspace, and
exact PSD certificates for the registered finite rows. It must not claim a
general exact semidefinite solver from fixture-specific minor checks.

For `M=C^dagger C`, it independently verifies

```text
sum_j K_j^dagger K_j = L_V(M),
sum_j K_j rho K_j^dagger = Phi_M(rho)
```

on a complete matrix basis and an ancilla extension. This establishes the
unconditioned quotient. Retained outcome maps `rho -> K_j rho K_j^dagger`
remain part of `C` and are compared under the declared port calibration.

For two unitary histories `A,B`, write

```text
M = [[p,m],[conjugate(m),q]],
Omega=A^dagger B.
```

Completeness is

```text
(p+q) I + m Omega + conjugate(m) Omega^dagger = I.
```

The candidate theorem is:

1. one eigenphase leaves a two-dimensional real solution in
   `(p+q,Re(m),Im(m))`;
2. exactly two eigenphases leave one cross-moment direction whose phase is
   fixed modulo pi;
3. at least three distinct eigenphases force `p+q=1` and `m=0`, while leaving
   the diagonal bias `p-q` free subject to PSD;
4. this is a statement about the unconditioned `M`, not every factorization;
5. nonunitary/nonnormal pairs are classified by the full real-linear operator
   equation, never by eigenphase counting.

For flags `f,g`, the effective cross operator is attenuated by
`w=<f|g>`. At rich spectrum, the candidate implication is `m w=0`; only when
both the history cross coefficient and both history weights are independently
nonzero may this be read as forcing `w=0`. Orthogonality is not permanence.

For recurring contexts `c`, each frozen dictionary pulls a common parameter
packet into a context kernel `M_c(theta)`. The exact solution is

```text
R = { theta : M_c(theta)>=0 and L_Vc(M_c(theta))=I for every c }.
```

The instrument must report the dimension and physical prediction movement of
the one-context surfaces, their successive intersections, the exchange-fixed
locus where licensed, and a held-out context. A point modulo gauge is
conditional selection only if the recurrence dictionary and symmetry are
independently typed; otherwise it is declaration-relative compatibility.

An extreme feasible `M` is certified by the standard finite-dimensional
tangent criterion: no nonzero Hermitian perturbation supported on `range(M)`
lies in the homogeneous kernel of `L_V`. The assay must then test whether
extremality survives every registered restriction, coarse-graining, spectator,
and catalogue-embedding map. Failure blocks any selection principle.

## Locked investigation chronology

1. **Pin freeze.** Commit this file plus ledger/plan/question/status updates.
   No CSF implementation, fixture, result, or Paper 6 path may exist first.
2. **Generic core freeze before physical fixture truth.** Implement exact
   Gaussian-rational matrices, Hermitian-coordinate linearization, PSD and
   factorization checks, channel/instrument comparison, affine intersections,
   exact extremality certificates, CLI, seals, and mutants. Run only public
   calibrations whose answers are stated in their constructors. The physical
   fixture, scorer, result, and paper paths remain absent.
3. **Fixture/scorer freeze.** Add one data-only recurring-context fixture and
   verdict-neutral scorer with no expected verdict, dimension, witness,
   selected matrix, or pass count. Freeze both while all result paths are
   absent.
4. **One official execution.** Run once, render transcript, sealed receipt,
   and Paper 6 from one result object, and commit those bytes as-is before
   replay, mutants, or interpretive edits.
5. **Candidate verification.** Rebuild independently, run two clean replays,
   all mutants, alien-CWD and true no-`.git` archive execution, seal and paper
   reconciliation, exact-math scan, and path-value anchor audit.
6. **Hostile protocol.** Freeze three independent seats: operator/convex
   geometry; records/representation/histories; and relational locality/
   no-signalling/physics. Reviewer dispatch requires a separate explicit user
   request under the active collaboration rule.
7. **Adjudication and repair.** No terminal status is possible without all
   frozen reports, joint adjudication, bounded repair, and terminal replay.

## Mandatory exact fixtures and controls

### A. Base and fiber

1. Reconstruct JCV's real `I/Z` equations as `tr(M)=1` and `Re(M[0,1])=0`,
   with the extra real-slice condition displayed rather than hidden.
2. Reconstruct the two frozen JCV witnesses with the same
   `M=diag(16/25,9/25)` and different calibrated outcome-zero statistics.
3. Reconstruct the third witness with
   `M=diag(25/169,144/169)` and a moved unconditioned channel.
4. An unobserved port isometry preserves `M` and `Phi_M`; retaining its old
   calibrated labels can change the instrument and is not declared gauge.
5. A non-PSD affine solution, a state-only normalized row, and an incomplete
   factorization are rejected.
6. History rephasing/permutation covariance and forbidden relational-event
   mixing are separate controls.

### B. Spectral and nonnormal ensemble strata

1. Scalar, two-eigenphase, and at-least-three-eigenphase unitary relatives.
2. At two phases, a rank-one cross-coherent extreme and an interior incoherent
   point, with the phase constraint and PSD bound computed exactly.
3. At rich spectrum, `p+q=1,m=0` for the complete unconditioned family, while
   parity-like calibrated factorizations may retain conditional coherence.
4. One dimension-changing or nonnormal pair solved by the full operator map.
5. A coefficient-index transpose/conjugation mutant must move the channel or
   completeness result and die.

### C. Flag overlap and records

1. `w=1`, one exact partial overlap, and `w=0` controls.
2. Two-phase partial overlap satisfying the phase line and a real-weight
   failure control.
3. Rich-spectrum nonzero-overlap failure with both branch weights nonzero,
   plus definite-order endpoint controls.
4. An eraser continuation that restores overlap, proving present
   orthogonality is not automatically durable.
5. No created flag is called a relational cell unless support/rewrite typing
   and a graph-computed later probe are actually supplied.

### D. Recurring-context selection

1. At least three independently constructed contexts sharing a predeclared
   two-history event-algebra dictionary, including incompatible two-phase
   directions and one rich-spectrum context.
2. Successive exact intersections: separate laws, identity recurrence,
   gauge-conjugate recurrence, and exchange-fixed recurrence.
3. One inequivalent dictionary that changes a gauge-invariant prediction,
   forcing a declaration-relative qualifier rather than being discarded.
4. One asymmetric context where exchange symmetry is forbidden by a calibrated
   relational distinction.
5. One held-out context not used to choose the recurrence ansatz.
6. Selection of `M` and selection of calibrated `C` are scored separately.
7. A positive-dimensional survivor must include an exact pair moving a
   calibrated statistic; a singleton must carry an independent uniqueness
   certificate modulo the declared gauge.

### E. Extreme-point speculation

1. Rank-one extreme, nonextreme interior, and—if the registered family admits
   one—higher-rank extreme controls; absence is reported rather than planted.
2. Port refinement that leaves `M` fixed.
3. Restriction/coarse-graining or subsystem forgetting that maps a registered
   extreme to a nonextreme point.
4. Idle-spectator and direct-sum catalogue embedding controls.
5. No “pure law” or selection conclusion unless extremality is invariant under
   every registered physical equivalence and composition map.

### F. Operational safety and scope

1. Fixed-subsystem, unconditioned no-signalling under a complete local
   instrument, plus an incomplete amplifier control.
2. Same-`M`/different-`C` conditioning is displayed without claiming remote
   steering unless an entangled preparation and remote instrument are typed.
3. Conditional steering, changing Bob algebra, arbitrary-`n`, continuum,
   QFT, gravity, particles, and actualization remain explicit open scopes.

## Pre-registered outcomes

The scorer emits the earliest applicable primary outcome and every independent
qualifier whose measured predicate holds.

1. `CSF-BLOCKED-AT-HISTORY-INDIVIDUATION` — the proposed `V_h` coordinates
   are only interchangeable Kraus representations and are not bound to the
   declared relational event algebra.
2. `CSF-BLOCKED-AT-RECURRENCE-DICTIONARY` — the contexts have no
   event-preserving, gauge-covariant identification of the coefficient packet.
3. `CSF-SPECTRAHEDRAL-FORMULATION-REFUTED` — completeness or the
   unconditioned channel fails to factor through `M=C^dagger C`, or the fixed
   typed law set is not the registered affine PSD slice.
4. `CSF-RECURRING-LAW-INCONSISTENT` — every registered covariant recurrence
   dictionary has an empty exact intersection.
5. `CSF-RECURRING-LAW-SELECTED-MODULO-GAUGE` — an independently typed
   recurrence and licensed symmetry leave one physical `M` class and the
   held-out context passes.
6. `CSF-RECURRING-LAW-PARTIALLY-SELECTED` — recurrence strictly reduces the
   physical dimension but leaves a prediction-moving family.
7. `CSF-RECURRING-LAW-UNSELECTED` — a nonempty prediction-moving family
   survives without a strict reduction from the registered independent laws.

Independent qualifiers:

- `COMPLETENESS-SPECTRAHEDRON-CONSTRUCTED`;
- `JCV-UNCONDITIONED-BASE-AND-CALIBRATED-FIBER-EMBEDDED`;
- `RICH-SPECTRUM-UNCONDITIONED-CROSS-MOMENT-ZERO`;
- `CALIBRATED-RECORD-FIBER-OPERATIONALLY-NONTRIVIAL`;
- `SELECTION-CONDITIONAL-ON-EXCHANGE-SYMMETRY`;
- `RECURRENCE-DOCTRINE-MOVES-PHYSICS`;
- `EXTREME-POINT-SELECTION-UNSTABLE`;
- `EXTREME-POINT-SELECTION-SURVIVES-REGISTERED-MAPS`;
- `FLAG-ORTHOGONALITY-CONSTRUCTED-BUT-PERMANENCE-UNPROVED`;
- `CONDITIONAL-STEERING-OPEN`;
- `ELEMENTARY-TRANSPORTS-AND-CATALOGUE-UNSELECTED`.

The positive maximum is selection of the unconditioned history kernel `M` at
the registered contexts. It does not select the port law `C`, elementary
transports, relational rewrite, catalogue, actualization, or nature's global
law unless those independent predicates are also constructed.

## Kill conditions

- treating `M` as the complete calibrated instrument;
- calling all `C^dagger C=M` factorizations gauge when retained port statistics
  differ;
- using inconsistent index orientation between completeness and `Phi_M`;
- solving only selected states instead of the all-input operator identity;
- calling an affine solution physical without an exact PSD certificate;
- using the unitary eigenphase theorem for a nonnormal overlap;
- saying rich spectrum selects `M` uniquely while the diagonal bias remains;
- saying `m=0` proves an actual or durable order record;
- calling `w=0` permanent without an eraser/future census;
- equating raw `M` entries across rephased or permuted history coordinates;
- identifying context recurrence by repeated numerals or names rather than a
  typed event-algebra dictionary;
- calling full-`M` recurrence vertex locality without a local derivation;
- adding exchange symmetry in an arena with a calibrated asymmetric role;
- choosing contexts or dictionaries after inspecting which one selects a point;
- identifying extreme with rank one, pure, unique, or physically preferred;
- claiming an extreme-point principle after a registered physical map sends an
  extreme to a nonextreme point;
- promoting same-`M`/different-`C` conditioning to EPR steering without a
  typed remote preparation and operation;
- promoting the finite classifier to arbitrary `n`, QFT, gravity, particles,
  a Hamiltonian, an affine constant, actualization, or empirical deviation;
- using float, tolerance, mutable repository truth, typed result counts, a
  planted witness, a mutant-name exception, or a comparator sharing its builder.

## Receipt, CLI, seals, and falsifiers

- Substantive arithmetic is exact over `Q(i)` and rational Hermitian
  coordinates. PSD at the registered fixtures is certified by exact
  factorization, eigenpolynomial/sign, or complete principal minors as stated.
- The generic core freezes on public calibrations before the physical fixture
  or scorer exists. The data-only fixture contains no `expected`, `verdict`,
  `outcome`, selected matrix, solution dimension, or pass count.
- The CLI rejects unknown flags with exit `2` and supports `--selftest`,
  `--mutant NAME`, `--output PATH`, and `--receipt PATH`.
- `--selftest` corrupts an anchor, exits `1`, and writes nothing.
- Every runtime read is recorded at access and consumed by a named gate.
- Every published field is sealed at gate time. Promotion recomputes total
  seal coverage, exact verdict equality from independent measured fields,
  transcript/receipt/paper claim equality, and term-binding coverage.
- Two worktree runs, alien-CWD execution, and true no-`.git` archive replay
  must be byte-identical.

At minimum these mutants must alter their measured objects and die without
artifact writes:

```text
anchor-corrupt, history-event-mix, gram-index-transpose,
completeness-cross-drop, channel-cross-drop, state-only-normalize,
psd-skip, same-m-different-channel, same-m-call-same-instrument,
calibrated-port-call-gauge, jcv-first-move, jcv-third-same,
rich-spectrum-cross-keep, rich-spectrum-call-record,
nonnormal-spectral-shortcut, flag-overlap-ignore, orthogonal-call-durable,
eraser-drop, recurrence-dictionary-postselect, recurrence-rephase-break,
recurrence-swap-break, asymmetric-swap-impose, context-drop,
heldout-use-in-fit, intersection-dimension-type, singleton-no-certificate,
extreme-equals-rankone, extreme-stability-assume, port-refinement-move-m,
steering-promote, all-n-promote, float-leak, typed-count, verdict-flip,
transcript-forge, seal-after-write
```

Runtime cap: 300 seconds per ordinary or mutant invocation.

## Frozen file whitelist

Only these new CSF paths may be created; programme boards move only with a
named ledger entry:

```text
v16/note-csf-pin.md
v16/code/csf_core.py
v16/code/csf_public_output.txt
v16/code/csf_public_receipt.json
v16/note-csf-core-freeze.md
v16/code/csf_fixture.json
v16/code/csf_score.py
v16/note-csf-fixture-freeze.md
v16/code/csf_output.txt
v16/code/csf_receipt.json
v16/paper-06-completeness-spectrahedra-record-fibers.md
v16/note-csf-candidate-verification.md
v16/note-csf-hostile-protocol.md
v16/review-csf-operator.md
v16/review-csf-records.md
v16/review-csf-physics.md
v16/note-csf-adjudication.md
v16/note-csf-repair-freeze.md
v16/note-csf-repaired-artifacts.md
v16/note-csf-terminal-verification.md
v16/README.md
v16/PLAN.md
v16/QUESTIONS.md
v16/LOG.md
STATUS.md
```

Every git stage names explicit paths. The unrelated untracked v15 SCOUT-T
files remain untouched.

## Scope walls

Paper 6 may establish the fixed-history spectrahedral formulation, distinguish
unconditioned law from calibrated record realization, derive a scoped
rich-spectrum cross-moment theorem, and measure whether one frozen recurrence
doctrine and symmetry reduce the exact law family across several finite
contexts. It cannot derive the history maps, rewrite law, configuration
catalogue, species, universal port law, record permanence beyond the frozen
continuations, conditional steering, changing-factor no-signalling, arbitrary
finite composition, actualization, Lorentz symmetry, continuum spacetime,
gravity, QFT, particles, a Hamiltonian, coupling constants, an affine constant,
or empirical deviations.

A spectrahedron is a lawful design space, not a law of nature. A singleton
under a declared recurrence doctrine is conditional selection, not derivation
of that doctrine. An orthogonal flag is not a durable record. An extreme point
is not automatically pure or preferred. A selected `M` does not select its
calibrated `C` fiber.
