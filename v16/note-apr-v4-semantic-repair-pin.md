# APR Paper 12 — v4 minimal semantic-repair pin

**Date:** 2026-08-19

**Status:** BINDING SCORER-ONLY DELTA; NO V4 SCORER OR ARTIFACT EXISTS

**Parent failure:** `v16/note-apr-v3-verification-failure.md`

## 1. Scope and immutability

During implementation, only the scorer below may move:

```text
v16/code/apr_score.py
```

The APR pins, core, fixtures, protocols, law/preparation/calibration data,
outcome vocabulary and precedence, committed v1--v3 scorer snapshots and
artifacts, and all failure/exposure records remain immutable. After the v4
scorer bytes freeze, exactly one new
`v16/note-apr-v4-scorer-freeze.md` is authorized to record those bytes before
their commit. The robust scoped primary
`APR-BLOCKED-AT-BOUNDARY-GLUING` is not an implementation target and may not
be hard-coded or preserved by fiat.

This delta adds no APR process, tensor, overlap selector, probe compiler,
contact schedule, regional `Tau`, quantum law, ontology, geometry, or
empirical datum. The exact internal laws below test the scorer's generic
positive paths only. They may never enter the APR receipt as evidence.

One rule governs every promotion:

> Evidence is computed from one typed semantic object; it is never asserted
> by a Boolean, copied equation, hash equality, root label, or provenance path.

## 2. Exact internal types

Use exact rational matrices for classical tests and exact Gaussian-rational
matrices for quantum tests. No floating-point tolerance is permitted.

The internal classical process types are:

```text
Boundary(B, X_B)
Arrow(f: B -> C, T_f: Q^(X_B) -> Q^(X_C))
Instrument(q: B -> C, {T_q,j}, {flag_j})
Factorization(h, [f_n, ..., f_1])
VerticalMap(j: B -> B', J_j)
```

Each frontier `X_B` is finite, unique, and explicitly indexed. Each arrow,
factorization, tensor term, vertical map, record, and readout belongs to one
active semantic root. Equal root strings are necessary typing data, never
evidence of an equation.

For the positive naturality gate, a `VerticalMap` belongs to the frozen
admissible comparison class of frontier-typed permutation matrices, verified
entrywise together with their permutation inverses. Zero or rank-deficient
comparisons are inadmissible and
cannot make a square pass vacuously. The positive comparison must be genuinely
nonidentity and move a calibrated state/effect under the declared transport;
an identity comparison cannot satisfy that witness.

A plain mapping containing `present:true`, `valid:true`, `positive:true`,
`mass_preserving:true`, caller-supplied `lhs/rhs`, or a prose proof cannot be
consumed as a measurement object. Promotion functions accept only internally
constructed typed results returned by named measurement functions.

An `Arrow` is unconditioned and mass-preserving. An `Instrument` has
subnormalized positive branch maps with

```text
T_q,j[i,k] >= 0
sum_j 1_C^T T_q,j = 1_B^T.
```

Its stacked flagged arrow is mass-preserving. A selected conditioning branch
may be substochastic; it is never silently retyped as an `Arrow`.

## 3. Typed classical process gate

For each arrow, the scorer must verify:

```text
T_f[i,j] >= 0
1_C^T T_f = 1_B^T
shape(T_f) = (|X_C|, |X_B|)
```

Thus positivity and mass preservation are derived from the matrix on the
declared frontiers. Linearity retains the zero vector, and zero-probability
ports remain elements of the output frontier.

`HORIZONTAL-CLASSICAL` requires all of the following inside one typed object
graph and active root:

1. a total frontier constructor over its declared active-boundary grammar;
2. every assigned arrow dimensioned and indexed by its declared frontiers;
3. `T_id(B)=I_(X_B)` for every active object, attached to the empty process;
4. at least one registered two-step word with two typed nonidentity arrow
   occurrences `f:A->B`, `g:B->C`, one registered whole `h:A->C`, and
   recomputed `T_h=T_g T_f`; the two occurrences may use the same generator
   or matrix, but a single standalone occurrence is insufficient;
5. at least two registered cuts/factorizations of one whole, each matrix
   product recomputed from arrow references and equal to the whole;
6. a symbolic tensor constructor using the fixed left-major lexicographic
   ordering on `X_B x X_C`, with `T_(f tensor g)=T_f tensor T_g`; explicit
   associator and symmetry permutation matrices; recomputed unit and
   associativity after transport by the associator; and the nontrivial
   interchange identity
   `(T_g tensor T_h)(T_f tensor T_k)=(T_g T_f) tensor (T_h T_k)` on typed
   composable arrows;
7. at least one full nonidentity naturality diagram
   `f:B->C`, `f':B'->C'`, `J_B:B->B'`, `J_C:C->C'`, with
   `J_C T_f = T_f' J_B` recomputed;
8. any record/effect claim typed to those same objects and arrows.

The scorer builds every product, Kronecker product, factorization, and square.
Packages may not provide their results.

### 3.1 Required positive construction

A compact internal existence law may use two-state frontiers and two typed
occurrences of the exact bit-flip generator, `f=X`, `g=X`, with registered
whole `h=I`, so `T_g T_f=T_h`; a second typed identity-route cut; a genuine
spectator tensor term in the frozen product ordering; and a conjugated
nontrivial naturality square. It must reach `HORIZONTAL-CLASSICAL`.

### 3.2 Required failures

Each of these independently demotes or refuses:

- a frontier/domain or frontier/codomain mismatch;
- a missing intermediate frontier or noncomposable pair;
- no registered two-step nonidentity word, including the case where only one
  standalone occurrence is available;
- a wrong whole or one altered cut;
- a negative matrix entry or a column sum different from one;
- a dropped zero port;
- a wrong tensor frontier, unit, associator transport, symmetry, or
  interchange product;
- identity-only or disconnected naturality, or a changed `J_C`/`f'` matrix
  that makes the naturality residual nonzero;
- a zero or rank-deficient vertical comparison presented as admissible;
- a duplicate or missing active identity;
- removing the typed arrows/factorizations and replacing them by the same
  opaque copy-oracle object.

Adding or changing unused opaque proof fields on an otherwise valid typed law
must be inert. The v3 copy-oracle attack is a kill only when opaque objects are
used in place of missing typed data.

## 4. Typed quantum extension

A quantum test extends the same boundary/arrow grammar and active root with
exact amplitude transports. The scorer composes them to derive every history
class operator `K_h`; a free Gram matrix or history table is not evidence.

For each registered division port `j`, derive

```text
L_j = sum_h C[j,h] K_h
```

from exact coefficients and the same registered histories. Recompute:

1. strong positivity for every positive input from the exact Gram identity
   `D(h,h';rho)=Tr(K_h rho K_h'^dagger)`: for every coefficient vector `z`,
   `z^dagger D z=Tr(A_bar_z rho A_bar_z^dagger)>=0`, where
   `A_bar_z=sum_h conjugate(z_h) K_h`; a finite spanning-input positivity
   census cannot substitute for this operator proof;
2. unit-normalized all-input completeness
   `sum_j L_j^dagger L_j = I_(H_in)` exactly;
3. the dilation `W=sum_j |j>_F tensor L_j`, exact `W^dagger W=I`, orthogonal
   flag projectors, and continuation-stable division over a finite closed
   continuation semigroup containing at least one nonidentity flag-preserving
   map, with reader recovery recomputed for every word;
4. coherent cut/refinement equality by recomposing the same arrows;
5. an operational interference witness: on one exact input and output port,
   the coherent probability differs from the incoherent history sum and the
   cross operator is nonzero.

### 4.1 Required positive construction

An exact two-history construction may use

```text
K_0 = I/2
K_1 = X/2
L_+ = K_0 + K_1
L_- = K_0 - K_1
```

Then `L_+^dagger L_+ + L_-^dagger L_-=I`. On the exact rational density
matrix `rho_+=(I+X)/2`, the coherent `+` probability is one while the
incoherent history sum is `1/2`. These histories must be derived from the
registered arrow grammar. With typed flags, recovery, and cuts, the package
must reach `HORIZONTAL-QUANTUM`.

A second exact control must contain the phase matrix `P=diag(1,i)`. It must
verify `P^dagger P=I` while `P^T P!=I`, so every load-bearing adjoint is a
Gaussian-rational conjugate transpose rather than an ordinary transpose.
The Gram check must separately use a complex history coefficient vector, for
example `z=(1,i)`, and verify the displayed `A_bar_z` identity, so history
index/conjugation orientation is tested rather than inferred from `P` alone.
The closed flag-continuation control may use `{I_F,Z_F}`; the delayed flag
reader must recover the outcome after every word.

### 4.2 Required failures

Each of these demotes to classical or refuses:

- a supplied/free Gram with no typed histories;
- histories on another root or frontier;
- branches summing to `2I`, or to any supplied nonunit total;
- a supplied matrix with a negative eigenvalue presented as a Gram, which
  must be ignored or refused because it is not derived from histories;
- a nonpositive input presented as a state, which must type-refuse;
- a zero cross term or no operational probability difference;
- missing or disconnected flags/recovery, or a continuation catalogue with
  no nonidentity typed flag-preserving word;
- coherent cuts assembled from different arrows;
- arbitrary equal recovery/cut payloads.

## 5. Generated causal influence and contact

An internal influence law contains:

```text
mu in Delta(X_0)
typed schedule T_1, ..., T_n
distinct interventions I_a at one typed slot k
typed later reader R
```

The scorer derives, never accepts,

```text
p(y|a) = R T_n ... T_(k+1) I_a T_(k-1) ... T_1 mu.
```

`causal_order` requires typed before/after order and
`p(.|a) != p(.|a')` for some alternatives. Its one-system positive control
may use reset-to-zero versus reset-to-one interventions, identity
continuation, and a later bit reader.

`generated_contact` additionally requires a typed product carrier
`X_S x X_T`; independently nonzero, disjoint source and target factors;
interventions proven source-local by the factorization
`I_a=reset_a tensor I_T` (in the frozen `X_S x X_T` ordering); a reader that
factors through the target; and a nontrivial typed propagation between them.
Its positive control starts at `|00>` on two bits, inserts the source-local
reset, applies the exact copy/CNOT propagation `S->T`, and reads the target,
deriving `(1,0)` versus `(0,1)`. Support/locality is computed from tensor
factor action, not region labels. Provenance records the computed chain but
cannot create it.

Mandatory negatives are: identical or unused alternatives; reader before the
intervention; arbitrary supplied before/after tables; noncomposable carrier;
disconnected root; overlapping or merely labeled supports for the contact
arm; an intervention that also acts on the target; a reader that consumes the
source directly; identity propagation paired with a supplied changed target
response; and provenance without a computed response. Causal order must not
alias contact.

## 6. No bare capability census

The classifier accepts one immutable primitive-law object, invokes its named
evaluators, and only then constructs a `CapabilityCensus` as output. Each
measurement carries the primitive payload hash, the exact primitive IDs it
consumed, and independently reconstructible residuals/certificates. The
classifier recomputes every arithmetic and typing residual from the primitive
payload; hashes bind primitive bytes and never validate a residual. Nominal
dataclass membership is insufficient. A mapping, a forged
dataclass wrapping booleans, a result without primitive witnesses, or a shared
root/hash without the relevant dependency and equation refuses.

The compact positive primitive law must instantiate every rung exactly:

1. **Normalization and raw atomlessness.** The uniform compiler
   `compile(A)={Q_A,Q_notA}` acts on the full prefix Boolean algebra, retains
   both ports, and proves `Q_A+Q_notA=I`. For each nonzero canonical antichain,
   the generic child split supplies two proper nonzero parts.
2. **Boundary/gluing.** Use the typed classical process of §3 and a two-member
   `ABC` overlap family with identical uniform `AB` and `BC` marginals. Select
   the unique Markov extension by recomputing, for every cell,
   `P(abc)P(b)-P(ab)P(bc)=0`: the uniform independent extension passes and the
   `A=C`, `B`-independent extension has a nonzero residual. No order/hash/
   sparsity convention may select it.
3. **Future completeness.** Apply the same target-independent compiler to a
   fresh held-out region such as `cyl(000)`, not present in the seed list, and
   recompute its separation profile. A whitelist or appended target-specific
   effect fails.
4. **Regional congruence and physical-image atomlessness.** With faithful
   support preparations and the complete generated compiler, reconstruct the
   theorem that contextual equality is literal equality. Recompute descent of
   meet, join, complement, and process composition. The quotient is therefore
   canonically the prefix algebra; run the symbolic proper-split constructor
   after the quotient. A finite leaf census is insufficient.
5. **Comparison.** Use an exact permutation comparison `P`, conjugated process
   `T'=P T P^-1`, transported state/effect, and two registered cuts. Recompute
   naturality, calibration equality, and cut equality. Altering the comparison
   matrix must produce a nonzero residual.
6. **Locality/support.** On the left-major two-bit carrier `(s,t)`, construct
   `Kin(S)=span{(1,1,0,0),(0,0,1,1)}` from `s` effects,
   `Kin(T)=span{(1,0,1,0),(0,1,0,1)}` from `t` effects, and
   `Kin(ST)=Q^4`. Independently generate exterior replacements and compute
   fixed/equalizer spaces `Dyn(S)`, `Dyn(T)`, and `Dyn(ST)`; each must equal
   its corresponding `Kin`. Recompute the strict inclusions
   `Kin(S),Kin(T) proper-subset Kin(ST)` and both non-inclusions
   `Kin(S) not-subset Kin(T)`, `Kin(T) not-subset Kin(S)`, plus nonconstancy
   and faithfulness. Supplied row spaces or equal ranks do not count.
7. **Causality/contact.** Use the derived measurement objects of §5, including
   the two-factor contact chain.
8. **Law selection.** Evaluate the finite, explicitly printed two-member
   family of complete primitive-law bundles `{L_I,L_X}`. Both instantiate the
   same frozen schema and reference every measured component above; they
   differ only at the registered transition `I` versus `X`. Against an exact
   calibration generated through the registered schedule, for example
   `delta_0 -> delta_1`, recompute every residual; `L_X` is the unique
   zero-residual survivor. This is selection only within that finite test
   family. A `law_selected` literal or target identifier is forbidden.

The primitive payload must reference the actual shared transitions, compiler,
regions, comparisons, interventions, replacements, and calibration rows used
above. Construct a typed primitive-ID-to-measurement dependency graph from
those actual references and require it to be connected. Hash equality alone
cannot weld disconnected subpackages. The full positive ladder is assembled
only from the recomputed measurement outputs.
Deleting or corrupting each primitive witness must return the earliest
compatible frozen primary. A separately instantiated forged census dataclass
and a plain mapping must both refuse. When generated contact alone is missing,
the exact word remains

```text
APR-DYNAMIC-ATOMLESS-REGIONAL-REFERENT-CONSTRUCTED-LAW-UNSELECTED
```

with wall `missing generated_contact`.

The full-ladder drop battery must additionally: remove the Markov selector or
make both overlap candidates survive; replace the compiler by a seed
whitelist; substitute the scalar-volume noncongruence control; apply the
ultrafilter two-element atomic quotient; alter the comparison permutation;
delete or merge exterior replacements so one required inclusion and one
required non-inclusion fail; rewire one rung to a byte-identical but distinct
transition ID so the dependency graph disconnects; and produce zero or two
zero-residual candidate laws. Each changed primitive is serialized in the
self-test payload, its residual is recomputed, and the classifier stops at the
registered earliest compatible rung.

## 7. Same-law ontology-role ladder

`ontology_candidate` remains classifier-inert. The measured role consumes the
same typed process object:

- `STATIC-RESPONSE`: APR baseline; no horizontal process;
- `FIXED-ALGEBRA-CONDITIONING`: the typed law derives the question instrument
  `{Q_A,Q_notA}` and its flagged stochastic arrow on the same algebra; an
  individual conditioned branch remains explicitly subnormalized;
- `RECORD-WRITING-ON-FIXED-ALGEBRA`: the preceding process plus a same-law
  writer, delayed reader, closed continuation set, and recomputed recovery;
- `REGION-REWRITING`: a typed rewrite changes the canonical regional
  object/support, transports the state, and a later probe compiled from that
  output region yields a response computed by composition.

The record positive uses the deterministic writer
`W:Delta(S)->Delta(S x F)`, `W|s>=|s,s>`, a reader factoring through `F`, and
the nontrivial closed continuation semigroup
`{I_(SxF), X_S tensor I_F}`. Recompute that the delayed flag reader recovers
the original `s` after every continuation word.

The rewrite positive uses a typed two-to-three carrier map from
`G_2={0,1}` to `G_3={0,1,n}`. On input `|1>`, the rewrite transports mass to
the created support `|n>`. The target-independent compiler derives the
new-support effect from `G_3`; composing it after the rewrite gives one. The
registered no-rewrite/passive-inclusion control gives zero. The output
regional object, state transport, compiled probe, and response all come from
the same primitive law and typed composition.

Supplied before/after tables, changed-region labels, semantic-action strings,
or equal root names cannot promote. Explicit attacks use an identity carrier
map plus the label `record-write`, and a changed region/table with no rewrite
composition; both must fail. Every synthetic rung must be reached and then
demoted when its load-bearing typed object is deleted. Changing/removing the
ontology candidate leaves all measured coordinates invariant.

## 8. Frozen APR baseline

V4 must reconstruct, without internal synthetic evidence entering the APR
receipt:

- `APR-BLOCKED-AT-BOUNDARY-GLUING` through the registered precedence, not a
  literal expected word;
- `process=STATIC-RESPONSE-ONLY`;
- only the B0 assigned identity, with B1--B3 absent;
- contact/causality `PRICED`, one-law provenance `UNCONSTRUCTED`;
- the exact `AB/BC` ambiguity (`1/4` local marginals and
  `P(A=C)=1/2` versus `1`);
- `ontology_role=STATIC-RESPONSE` plus the separate postulated candidate;
- the exact syntax-only qualifier and locality/atomlessness scope walls;
- the permanent result-exposure disclosure.

No synthetic package, positive measurement object, test-only root, or
self-test record may be serialized into the APR scientific transcript or
receipt. Synthetic evidence exists only in fixture-free self-test output and
the v4 source-freeze note.

## 9. Exposure and freeze discipline

Before source commit:

1. modify only `v16/code/apr_score.py`;
2. run AST/static/diff checks and fixture-free `--selftest` only;
3. never invoke fixture-loading `--run`, `--mutant`, or `--mutants-all`;
4. exercise every positive and adversarial gate above;
5. run the same self-test from a true off-tree/no-`.git` directory containing
   only the scorer and generic core, with the fixture module/data absent and
   an import-denial sentinel that fails any attempted fixture import;
6. emit machine-readable primitive-witness hashes, exact residuals/operator
   identities, derived coordinates, and every ingredient-drop result, plus
   `scientific_fixture_evaluated:false`; a list of check names is insufficient;
7. verify that the repository and off-tree self-test payloads are byte-identical
   and independently reconstructible without importing scorer functions;
8. after the scorer bytes stop moving, create only
   `v16/note-apr-v4-scorer-freeze.md` and freeze both in a dedicated commit;
9. verify that the new v4 artifact paths do not exist.

V4 artifacts must contain exactly:

```text
blinding_status: RESULT-KNOWN-BEFORE-V4-IMPLEMENTATION
exposure_debt: PERMANENT-PREFREEZE-M01-AND-ALL-MUTANTS-EXPOSURE
v4_source_frozen_before_v4_run: true
```

This preserves the permanent v2 exposure. V4 may be source-frozen before its
own run; it may never be called blind, pre-truth, or mutually blind.

After source freeze, publish once to new absent paths:

```text
v16/apr_output_v4.txt
v16/apr_receipt_v4.json
```

Require repository-root, alien-CWD, and true off-tree/no-`.git` byte identity;
payload/transcript hash reconstruction; no overwrite; no Git/network/random
scientific dependency; and a new independent black-box verifier that imports
no scorer measurement functions. Candidate drafting and the paper panel stay
prohibited until every inherited and v4 gate passes.

## 10. Hard kills

Any one of these invalidates v4 certification:

1. a frontier-mismatched map earns classical process;
2. no genuine composable pair, or arbitrary equal equation tokens, earn
   classical process;
3. a negative/nonconserving map earns classical process;
4. a substochastic instrument branch is retyped as a mass-preserving arrow,
   or incomplete branch sum earns conditioning;
5. a disconnected tensor/naturality declaration or untransported associator
   earns classical process;
6. `2I` or any nonunit total earns quantum process;
7. a free/disconnected Gram or interference table, or transpose in place of
   conjugate transpose, earns quantum process;
8. unused/identical interventions or supplied changed tables earn causal
   influence; or identity propagation from a source factor to a disjoint
   target factor earns generated contact (identity continuation remains lawful
   in the one-system causal-order control where the later reader observes the
   directly changed system);
9. a plain mapping or forged nominal capability object reaches any positive
   rung or joint primary;
10. an identity writer label or supplied rewrite response promotes the
    ontology role;
11. any v3 baseline scientific coordinate or primary changes;
12. fixture/core/protocol/law bytes move, synthetic evidence enters the APR
    result, or a fixture-evaluating mode runs before source freeze;
13. the off-tree self-test can import fixture data or omits reconstructible
    primitive witnesses/residuals;
14. exposure, scope, or ontology-candidate separation is weakened.

## 11. Lawful simplification and ontology ceiling

Silently deleting the registered positive process/ontology/classifier paths,
or short-circuiting the scorer to the known baseline, is not lawful under the
frozen positive-path contract. The minimal lawful implementation deletes
caller-supplied proof fields from promotion logic and uses compact exact
internal laws to establish genuine generic reachability.

APR presently owns one predeclared commutative prefix algebra, exact finite
static restriction responses, and raw syntactic atomlessness. Its candidate
actual partial web of durable relational facts remains a postulate. Nothing in
this repair can establish a horizontal regional process, physical atomless
referent, generated causal/contact order, dynamic locality, geometry,
matter--geometry backreaction, continuum, metric, curvature, GR/QFT,
Hamiltonian, particles, or actualization.
