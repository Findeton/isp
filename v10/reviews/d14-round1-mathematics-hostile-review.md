# D14 hostile round-1 mathematics / category / decoherence review

**Date:** 2026-07-11  
**Reviewer:** independent mathematics/category/decoherence referee  
**Verdict:** **MAJOR REVISION / INCOMPLETE-INVESTIGATION**  
**Free-SMC evaluation theorem:** confirmed  
**Finite coherent/projective witness:** confirmed at its executed scope  
**Protected-record theorem and frozen bridge verdict:** not yet established

## Decision first

D14's categorical core is sound.  Once `FSDiam(Sigma)` is **defined** as the
free strict symmetric-monoidal category on a finite typed signature, any
assignment of matrices to generators extends uniquely to a strict
symmetric-monoidal matrix functor.  Finite tensor contractions are independent
of topological evaluation schedule, and the exact interference, frame,
decoherence, projectivity, memory, and no-signalling cells reproduce.

The submitted positive verdict nevertheless fails its own frozen protocol.
The protected algebra

$$
M=\sum_r |r\rangle\langle r|_R\otimes M_r
$$

preserves record **labels**, but arbitrary linear `M_r` do not preserve record
**probabilities**.  Branch-dependent norms or postselection can reweight the
record sectors without flipping a label.  The exact witness uses one unitary
system map, so that cell is fine; the general theorem is missing the required
branchwise isometry/trace-preservation hypothesis.

Moreover, the executable constructs an overwrite morphism successfully and
only observes that a predicate returns false; overwrite is not rejected by the
morphism constructor or composition API.  Two mandatory countercontrols are
absent: no dead/missing-collar continuation failure is executed, and no
memory-deletion process is compared with the non-Markov process.  Finally B12
is necessarily pending in a pre-hostile-review draft.  Under the frozen verdict
table, missing controls and hostile closure force `INCOMPLETE-INVESTIGATION`.

The bridge is repairable.  It is not refuted.

## Frozen artifacts and independent reproduction

```text
0e74122e9a5a5c1213a5257783cfb263af16c9e37e9993cd35492d683a3ed32a  note-d14-action-to-record-bridge-protocol.md
355724ee87561c161545dfbc0a383985ab7fd50c505f7e6c95698b2823c9b3c9  note-d14-finite-action-record-bridge-theorem.md
c0e00e196c8db029f62ea571dfcf0b81f420c97ab53f287fbd8e0432b43bd339  relativistic-isp-v10-paper15-from-action-to-records-without-a-global-clock.md
287c47f8cee8593956918b62f1c4786506b2af6dd5d9e5568acea73e7051c84f  code/d14_action_record_bridge_exact.py
9217316b6a98b3b8d42920214933c1d5832137abeb72fedee65a7fbcffc51c5f  data/d14-action-record-bridge-exact.json
```

Normal and optimized Python produced byte-identical stdout and JSON:

```text
checks                         = 30/30
stdout SHA-256 normal/-O       = 05edee685a6905408d331cb3546db4edbc2bdaeae6fd154d6f0ec8d2bc80bdbe
semantic SHA-256               = 3a1c766d1f82986f667b1897b817f44b51250db204659503592f545ce9807490
source SHA-256                 = 287c47f8cee8593956918b62f1c4786506b2af6dd5d9e5568acea73e7051c84f
D13 dependency SHA-256         = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
generated JSON SHA-256         = 9217316b6a98b3b8d42920214933c1d5832137abeb72fedee65a7fbcffc51c5f
```

No executable arithmetic failure was found.  The grade concerns theorem
hypotheses, enforcement, and missing frozen controls.

## Fatal/major opening ledger

```text
M1  MAJOR     Block-diagonal label preservation does not imply record-probability preservation.
M2  MAJOR     Protected-record membership is diagnostic only; overwrite Mor is constructed successfully.
M3  MAJOR     Mandatory missing/dead-collar continuation countercontrol is absent.
M4  MAJOR     Mandatory memory-deletion/change-of-process countercontrol is absent.
M5  MAJOR     Recorded decoherence notation conflates bare system class operators with record-extended ones.
M6  MODERATE  Executable models evaluated matrices, not the syntactic free source category or its quotient.
M7  MODERATE  History-record attachment is not integrated with the local seal/birth morphism in one network.
M8  MINOR     Nonnegativity predicate is weaker than its label for general Q(sqrt(2)) values.
M9  FATAL-TO-CURRENT-VERDICT
              Missing frozen controls plus pending B12 require INCOMPLETE-INVESTIGATION.
```

## 1. `FSDiam` and the free symmetric-monoidal theorem

### What passes

There is no algebra error in the abstract theorem if the source category is
defined as stated.  The free strict symmetric-monoidal category on typed
generators has:

- typed words as objects;
- circuit/string diagrams as morphisms modulo strict symmetric-monoidal
  relations;
- composition by typed gluing;
- tensor by concatenation/disjoint union;
- identities and typed permutations.

The universal property then gives one and only one strict symmetric-monoidal
functor into the chosen matrix skeleton after generator matrices are supplied.
Kronecker product, matrix multiplication, identities, and permutation matrices
satisfy the needed relations.  The exact cells for units, three-map
associativity, strict tensor associativity, interchange, symmetry naturality,
and involution are all correct.  Ill-typed composition raises `ValueError`.

Calling the category **free** is a definition, not a derivation that physical
diamonds obey only those equivalences.  Paper 15 states that scope correctly.

### Opening M6 — the receipt does not instantiate the syntactic source category

`Mor` stores a source object, target object, name, and already evaluated matrix.
Composition immediately multiplies matrices.  Thus two different free circuit
expressions with coincident matrices become observationally indistinguishable
inside the executable.  The code implements a subcategory of `Mat_C` with
typed wrappers, not the syntactic free category and its expression quotient.

This does not invalidate the universal-property proof, but the receipt's B0/B1
coverage is representational rather than a construction of `FSDiam` itself.

**Repair:** either (a) state that B0/B1 are proved abstractly and the code tests
their matrix image, or (b) add a syntax tree for generators/composition/tensor/
symmetry plus a normalization or relation checker before evaluation.  Define
`Mat_C` explicitly as the strict chosen-basis matrix skeleton.

## 2. Coherence and construction-order gauge

**Confirmed at the stated finite free-circuit scope.**

The displayed disjoint schedules compute the same map by interchange.  More
generally, any two linear extensions of a finite dependency poset are connected
by adjacent swaps of incomparable elements.  In a fixed free circuit,
incomparable generator evaluations occur on disjoint tensor factors, while
different finite contraction orders are related by associativity,
distributivity, and commutation of scalar sums/products.  Therefore the final
matrix/tensor contraction is schedule-independent.

This removes an arbitrary total evaluation order.  It does not quotient the
causal order of generators sharing a wire, and the paper does not claim that it
does.  No global physical commit clock is introduced by the proof.

The one exact two-schedule cell is illustrative rather than exhaustive; the
finite-poset argument supplies the universal finite step.

## 3. Coherent gluing

**Confirmed.**

Matrix multiplication is the finite internal-label sum

$$
(GF)_{ba}=\sum_k G_{bk}F_{ka}.
$$

The code checks one component against that sum.  The Hadamard control is also
correct: two coherent Hadamards return `|0>` with probability one, while
inserting an orthogonal record between them gives probability `1/2`.  Hence
unresolved alternatives must be added at amplitude level.

The local row-normalization counterexample is arithmetically valid for its
chosen nonzero row sums.  It shows that normalizing each supplied local array
before composition is not the same operation as composing first and then
normalizing.  It is a countercontrol, not a proposed physical normalization
rule.

## 4. Boundary frames and positive-cone pairing

**Confirmed at the declared scope.**

For unitary endpoint frames, the internal factors cancel:

$$
(G_c K_2G_b^\dagger)(G_bK_1G_a^\dagger)
=G_cK_2K_1G_a^\dagger.
$$

Transforming the state and effect preserves the closed trace probability.  The
exact matrices used in the receipt satisfy these identities.

For `G=diag(2,1/2)` in `SL(2,C)`, the dual transformation

$$
X\mapsto GXG^\dagger,
\qquad
E\mapsto(G^{-1})^\dagger EG^{-1}
$$

preserves `Tr(EX)`, and congruence preserves positivity.  This is a valid
rank-two boundary-pairing cell.  The paper correctly refuses to infer a smooth
Lorentzian network or emergent metric from it.

## 5. Protected record algebra

### Opening M1 — label preservation is not probability preservation

The theorem note admits the entire block-diagonal linear algebra

$$
M=\sum_r |r\rangle\langle r|_R\otimes M_r.
$$

Such an operator never changes label `r`, but it can change the weight of that
sector.  For example, take two record labels and

$$
M_0=2I,
\qquad M_1=I.
$$

After applying `M` and renormalizing, the relative record probabilities are
reweighted by `4:1`.  Postselected or trace-decreasing branch maps have the
same problem.  Therefore “cannot alter its distribution” does not follow from
block diagonality alone.

The exact `future_system` cell uses a unitary acting identically on record and
collar factors, so its record distribution really is preserved.  The error is
in the general theorem.

**Required repair:** require each controlled branch to be an isometry,
`M_r^dagger M_r=I`, for pure amplitude evolution, or a branchwise
trace-preserving channel/instrument with
`sum_k M_(r,k)^dagger M_(r,k)=I`.  Exclude postselection when claiming
unconditional permanence.  Then prove closure of the licensed class under
composition and tensor.

### Opening M2 — overwrite is detected, not rejected

The code constructs

```python
overwrite_mor = Mor(..., overwrite)
```

successfully.  It then verifies `not preserves_record(overwrite_mor,1,1)`.
This is a useful negative membership test, but the ambient `Mor` constructor
and `compose` function will still accept and evaluate the overwrite map.
Consequently the claim “an explicit record-flip map is rejected by the
protected type rule” is not true of the implemented API.

**Required repair:** define a `LicensedMor`/protected constructor that checks
all sealed input/output correspondences and raises on violation, and make the
network evaluator accept only licensed morphisms.  Alternatively define
`FSDiam_prot` explicitly as the subcategory selected by the predicate and prove
identity/tensor/composition closure; test that attempted insertion of
`overwrite_mor` into a licensed circuit fails.

The seal isometry, live-state output, label-preserving system unitary, repeat
copy, and zero disagreement mass themselves are exact.

## 6. Frozen countercontrols

### Opening M3 — no missing/dead-collar continuation failure

The protocol requires:

```text
omitting a live collar prevents continuation.
```

The receipt proves only that the seal output has collar basis value `1`.  It
does not define a downstream diamond whose source requires the collar, try to
compose without that port, or reject the dead basis state `|0>`.

**Required repair:** add a typed continuation generator consuming
`system + live collar`, compose it after the seal, and provide two negative
controls:

1. omission of the collar port is ill-typed;
2. a dead collar state has zero licensed continuation or is rejected by an
   explicit eligibility projector/rule.

### Opening M4 — no memory-deletion process comparison

The reversible memory circuit correctly gives

$$
P(z=1\mid y=0,x=1)=1,
\qquad
P(z=1\mid y=0,x=0)=0.
$$

But the frozen countercontrol also requires showing that deleting the hidden
memory changes the visible process.  No trace/reset/deletion channel is applied
and no altered conditional is printed.

**Required repair:** insert a CPTP reset/discard-and-reprepare channel on the
memory before the final copy.  Verify that the resulting `Z` conditional no
longer depends on `X`—for example both become zero after reset to `0`, or both
become `1/2` after fair reprepare—and that the new history law differs from the
original.

Both missing controls are promised by the frozen protocol, so they block the
positive verdict even though the positive cells pass.

## 7. Decoherence functional

The explicit calculation is correct for the **record-extended** branch
operators.  For pure `|psi>` the code constructs

$$
|\Psi_\alpha\rangle
=C_\alpha|\psi\rangle\otimes|\alpha\rangle,
$$

so

$$
\langle\Psi_\beta|\Psi_\alpha\rangle
=\delta_{\alpha\beta}
\langle\psi|C_\alpha^\dagger C_\alpha|\psi\rangle.
$$

The depth-one through depth-three values match the independently computed
history probabilities, normalize, and are exactly diagonal.  Born weighting
is not applied a second time.

### Opening M5 — distinguish bare and record-extended class operators

For bare system class operators, the ordinary decoherence functional is

$$
D_0(\alpha,\beta)=\operatorname{Tr}
(C_\alpha\rho C_\beta^\dagger),
$$

which is not made diagonal merely by writing a label beside it.  The diagonal
functional actually computed corresponds to extended operators such as

$$
\widetilde C_\alpha
=C_\alpha\otimes|\alpha\rangle\langle0|.
$$

Then

$$
D_R(\alpha,\beta)
=\operatorname{Tr}(\widetilde C_\alpha\rho_0
\widetilde C_\beta^\dagger)
=\delta_{\alpha\beta}D_0(\alpha,\alpha).
$$

The note's branch-vector derivation implies this, but its notation first names
`C_alpha` as though it were the bare system operator and then writes the delta
inside the same `D`.  Make the extension explicit and state that exact
decoherence is conditional on the supplied orthogonal record isometry.  This
prevents an accidental claim that arbitrary unrecorded histories decohere.

### Opening M7 — the executable's history record is not the local seal circuit

The repeated one-qubit histories are formed by `class_operator` and then
tensoring a complete history basis vector in `recorded_branch`.  The separately
tested `seal_birth_mor` is a four-level system/record/collar generator and is
not composed at each one-qubit history step.

The abstract construction is implementable, so this is not a refutation.  But
the receipt combines two witnesses rather than exhibiting one integrated
FSDiam network that emits each record bit and live collar locally.

**Repair:** build depths one through three by repeated typed seal/instrument
generators inside the circuit category, carrying the protected records and a
live collar at every step.  Show that its reduced branch vectors equal the
current `recorded_branch` values.

## 8. Projectivity and all-depth extension

**The finite induction is correct under the stated completeness hypothesis.**

For a future instrument applied after history `alpha`, cyclicity gives

$$
\sum_z p(\alpha z)
=\operatorname{Tr}\left[
C_\alpha\rho C_\alpha^\dagger
\sum_z M_z^\dagger M_z\right]
=p(\alpha).
$$

This proves adjacent prefix consistency at every finite depth when the
instrument is complete.  The exact H/projector tower verifies depths one,
two, and three.  The selected conditional is a cylinder ratio with positive
denominator.

An infinite history measure additionally needs a fixed measurable projective
system/standard-Borel or compact finite-alphabet setting.  Paper 15 says “under
the usual projective-extension hypotheses,” so it does not overclaim that
step.  The finite theorem is unaffected.

### Opening M8 — nonnegativity test is not generic over `Q(sqrt(2))`

The executable checks `p.re.a >= 0` but does not assert `p.re.b == 0`.  For a
general `Q2(a,b)=a+b sqrt(2)`, the sign is not determined by `a` alone.  The
actual history probabilities in this H/projector witness are rational, so the
printed conclusion is true.

**Repair:** assert `p.im==0` and either `p.re.b==0 and p.re.a>=0` for this
witness, or implement an exact sign comparator for quadratic rationals.  This
is a receipt hardening, not a theorem failure.

## 9. Visible memory and no-signalling

The 16-by-16 memory circuit is an exact permutation unitary.  Starting from the
equal mixture of `0000` and `1000`, it generates visible histories `000` and
`101` with equal mass, yielding the stated non-Markov conditionals.  The
enlarged state contains the needed memory locally.  Opening M4 concerns only
the required deletion control.

The Bell marginal cell is also exact: a local Hadamard on the first subsystem
does not alter the second reduced density matrix.  This is a finite
no-signalling check, not continuum microcausality.  The paper preserves that
boundary.

## 10. Count/hash semantics

The receipt is reproducible and materially stronger than a check-count-only
artifact:

- dependency source hash is frozen and checked before arithmetic;
- expected check count is frozen;
- expected semantic hash is frozen;
- generated JSON includes source and dependency hashes;
- normal and optimized stdout/JSON are byte-identical.

The semantic payload records scope, count, depths, non-Markov conditionals,
and verdict, but not every individual gate result.  The source hash binds the
actual checks, so this is acceptable provided the external final receipt
freezes the reviewed source/stdout hashes after repair.

## 11. Frozen B-gate verdict

```text
B0  PARTIAL  typed matrices/ill-typed rejection pass; protected overwrite not enforced
B1  PASS     abstract free-SMC laws plus exact matrix-image cells
B2  PASS     finite schedule theorem and nontrivial exact cell
B3  PASS     coherent path sum and normalization controls
B4  PASS AT STATED SCOPE  unitary frames plus one dual SL(2,C) cone cell
B5  FAIL/OPEN  general protected algebra lacks branchwise norm/TP condition;
               overwrite is diagnostic only; dead-collar control absent
B6  PASS WITH NOTATION REPAIR  record-extended functional is exactly diagonal
B7  PASS FINITELY  depths 1–3 plus valid completeness induction
B8  PASS POSITIVE CELL; required deletion countercontrol absent
B9  PASS AT FINITE CELL SCOPE
B10 PASS  primitive inputs are listed; no selection claim
B11 PASS  action-to-record/web/unit dictionary is explicit
B12 PENDING  this is the first hostile round
```

The protocol defines:

```text
FINITE-ACTION-TO-RECORD-BRIDGE-PROVED
  B0–B10 and B12 pass on the frozen FSDiam class; B11 is explicit.
```

Those conditions are not met.  The protocol also defines
`INCOMPLETE-INVESTIGATION` when a promised gate, control, receipt, or review is
missing.  That is the required current verdict.

### Opening M9 — current positive verdict violates the frozen grading rule

The theorem note, Paper 15, executable semantic JSON, and stdout all say
`FINITE-ACTION-TO-RECORD-BRIDGE-PROVED` before B12 and despite the missing
controls.  This is fatal to the current verdict, not to the candidate bridge.

**Required repair:** change the provisional verdict to
`INCOMPLETE-INVESTIGATION`; repair M1–M5 and execute both missing controls;
rerun hostile closure; only then promote the bridge if all B-gates pass.

## Claims that survive unchanged

- The abstract free strict symmetric-monoidal evaluation theorem is correct.
- Finite matrix/tensor-network evaluation is independent of topological
  contraction schedule.
- The internal coherent path sum and interference controls are exact.
- Independent unitary boundary frames cancel on glued edges.
- The dual `SL(2,C)` state/effect pairing and the tested positive-cone cell are
  exact.
- The supplied seal isometry emits an orthogonal label and live collar in the
  finite witness.
- Orthogonal protected history strings produce an exactly diagonal recorded
  decoherence functional.
- Complete instruments give projective finite cylinder laws at all depths;
  depths one through three reproduce exactly.
- The visible memory and finite no-signalling cells are correct.
- Functoriality composes supplied kernels but does not select types, kernels,
  states, record instruments, protected algebra, or physical units.
- No V9 cone or dimension holdout is licensed from this bridge alone.

## Final decision

**MAJOR REVISION.**  Preserve the free-SMC evaluation theorem, coherent
contraction, finite recorded-history construction, and downstream refusal.
Strengthen the protected algebra to branchwise isometric/trace-preserving maps,
enforce protected membership in the API, execute the dead-collar and
memory-deletion controls, distinguish bare from record-extended class
operators, and integrate the repeated history records with local seal/birth
morphisms.  Until those repairs and hostile closure are complete, the frozen
protocol requires `INCOMPLETE-INVESTIGATION`, not
`FINITE-ACTION-TO-RECORD-BRIDGE-PROVED`.
