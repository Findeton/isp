# Paper 13 Stage-A support-split forward repair pin

Status: **RESULT-NEUTRAL FORWARD REPAIR PIN / NO SOURCE EDIT YET**

## 1. Question and immutable base

Can the Paper 13 evaluator certify the pin-defined point-free horizontal split
without mistaking a coextensive child name, forgetful retraction, cell-count
padding, or raw role-count change for new physical support?

This is a bounded instrumentation repair.  It does not change the candidate
law, physical arena, exposed numbers, outcome vocabulary, eligible ceiling,
fresh protocol, or ontology walls.

Immutable inputs are:

| artifact | SHA-256 / identity |
|---|---|
| adjudicated base commit | `41b529f94931d8e97d1ed1e61064e4e7d82b6137` |
| original construction pin | `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35` |
| flawed #192 evaluator | `c699fc0316295e230c2cd0ef50601f631b195ad2237bebc2c42a75a2163f1aaf` |
| flawed source-freeze note | `d717f97832efe05996ae5f94249629376ddbe916fc837e0d5d16984bd7a13ad5` |
| `v16/review-paper13-stageA-source-physics.md` | `20a054cd6542fd02f556b461408f48d75ead0c69ec06abd76c9eed3ce3c3d352` |
| `v16/review-paper13-stageA-source-records.md` | `7c5b14a04f938de05b64750f6c8ae454eb4bbe8d0824e9eaaa0016532ab52ed4` |
| `v16/note-paper13-stageA-source-audit-adjudication.md` | `bd089458ef1d4c4fe8f9dc13fc21134695aba552b95b20f023e4d2f9f34dfb74` |
| RUNBOOK | `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58` |

The #192 evaluator, its note, both reports, and the adjudication never move.
The repair changes the worktree path `v16/code/p13_gamma_exact.py` only in a
new forward commit with a new hash and adds a new freeze note.

## 2. Exact split object

Let a finite typed context `X` have nonzero cell set `S`, let `P` be a
nonzero Boolean formula total on `X`, and let `N` be a fresh relational role.
The only registered horizontal extension is

```text
E(X,P,N).roles = X.roles disjoint-union {N}
E(X,P,N).cells =
    S union { s union {N} : s in S and P(s)=1 }.
```

`N` is fresh by exact typed identity/name, has type `RELATION`, and is absent
from every old role and cell.  Every old role occurs exactly once in the
target with its old type; no other role is permitted.  The original source
cell is retained in every case.

The forgetful map `f_N:E(X,P,N)->X` removes `N`.  Define the literal target
fiber

```text
F_s = {t in cells(E) : t minus {N} = s}.
```

Every target cell must belong to exactly one `F_s`, and
`cells(E)=disjoint-union_{s in S} F_s`.  No ambient or unprojected target cell
is allowed.  A machine-reconstructible split certificate must establish, for
every `s in S`, the exact set equality:

```text
P(s)=0  =>  f_N^-1(s) = {s},             child bits = {0}
P(s)=1  =>  f_N^-1(s) = {s,s union {N}}, child bits = {0,1}.
```

Consequently it must recompute all of:

```text
|cells(E)| = |S| + |{s in S : P(s)=1}|
forget_N(E) = X
P and N is nonzero
P and not N is nonzero
N is not extensionally equal to P or to any old Boolean formula on E
```

The count identity follows from the exhaustive disjoint fiber union; it is not
a substitute for it.  The last row is established by the two-element fiber
over every satisfying source cell, not by enumerating formula names.  A role-
count increase, target hash change, inverse merge, or total cell-count increase
alone is never a split certificate.

The implementation must expose one immutable exact `SplitFiberCertificate`
or an equivalently typed object.  Its identity binds all of:

```text
law identity
source boundary and source configuration hashes
complete Arrow, occurrence, and presentation/source key
selected output matter bit and port sector
actual port branch parent P=parent_b and actual child N
actual target boundary and target configuration hashes
operation kind in {CREATE,MERGE,UNCHANGED}
```

`P`, `N`, branch bit, and target are read from the selected occurrence and
derived branch, never caller-selected or found by existential search.  The
certificate also contains the literal target-exhaustiveness result, ordered
source-cell/fiber rows, satisfying-cell count, exact count residual,
properness predicates, and final conjunction.  Every field is recomputed from
the actual source/target contexts and process AST.  Caller booleans, supplied
fiber tables, and a certificate from another branch refuse.

Only nonzero `CREATE` branches demand the forward split certificate.  A
`MERGE` branch consumes the exact inverse certificate belonging to the same
prior creation; `UNCHANGED` is recorded separately and cannot earn support
change.  A valid split elsewhere in the filling cannot decorate a bad branch.

## 3. Positive obligations

The repair must derive and serialize at least these exact controls:

1. From `S={(),(A)}` and `P=A`, obtain
   `E={(),(A),(A,N)}` with fiber sizes `(1,2)` and cell count `2->3`.
2. On the same source with `P=not A`, obtain
   `E={(),(N),(A)}` with fiber sizes `(2,1)` and cell count `2->3`.
3. Exhaust extensional Boolean elements—not formula syntax—on this exact
   finite census (maximum source-role count two, maximum target-role count
   three):

   ```text
   context   nonzero ambient representatives   contextual quotient classes
   C1 roles (A),   cells {(),(A)}                         :  3 /  3
   C2 roles (A,B), cells {(),(A),(B),(A,B)}               : 15 / 15
   C3 roles (A,B), cells {(),(A),(A,B)}                   : 14 /  7
   C4 roles (A,B), cells {(),(B),(A,B)}                   : 14 /  7
   C5 roles (A,B), cells {(),(A),(B)}                     : 14 /  7
   C6 roles (A,B), cells {(),(A,B)}                       : 12 /  3
   ```

   Enumerate the `4` or `16` ambient truth tables and retain the `72`
   representatives nonzero on their context.  Then quotient by equality of
   the truth vector on the context's actual nonzero cells, producing exactly
   `42` physical contextual Boolean classes.  For example, on C3, `B` and
   `A and B` are the same class because the `B`-only cell is zero/absent.
   Record both per-context and total cardinalities.

   Evaluate one native certificate per contextual class and also replay every
   one of the 72 ambient representatives.  Representatives in the same class
   must have identical contextual parent identity, target semantic context,
   split certificate, operator, endpoint law, classifier-consumed lineage,
   and physical source/presentation key.  Raw ambient formula bytes may remain
   distinct provenance only.  Every class must satisfy target exhaustiveness,
   exact fibers, properness, and the derived count identity within the
   300-second mode cap.
4. Forgetting the child recovers the source for every row, but this fact is
   reported separately from proper splitting.
5. A nontrivial source-groupoid relabel transports the source, parent, child,
   target, and full split certificate; identity, inverse, and composition are
   exact and uncached.
6. Every nonzero `CREATE` branch emitted by the candidate Gamma consumes the
   transported certificate bound to its own occurrence, actual parent/child,
   output bit/sector, and literal target in its classifier backward slice.
   `MERGE` and `UNCHANGED` rows carry their distinct inverse/identity evidence.

The `referent_census`, `support_change`, `variable_carrier`, source-groupoid
measurement, gate table, shadow lineage, claim table, and receipt seal must all
consume this same recomputed object.  No gate may infer splitting from
`target_role_count > source_role_count` or inequality of the pair
`(role_count,cell_count)`.

## 4. Mandatory negative controls

All original 81 registered attacks remain live.  Add, at minimum:

### S1. `TAUTOLOGICAL-CHILD`

Use the exact adjudicated source mutation: replace each parent-satisfying cell
by its child-labelled cell instead of retaining both.  On the minimal witness
it gives `(),(A,N)`, roles `1->2`, cells `2->2`, and exact forgetful recovery.
The split certificate must fail because the satisfying fiber has only child
bit `{1}`.  The support gate must be false and the earliest rendered rung no
higher than `P13-SUPPORT-CHANGE-UNPROVEN`.

After final repaired-source freeze, repeat this as a real source-only off-tree
mutation.  Record old/new source hashes, exact patch, exit code, serialized
certificate residual, gate/rung effect, and stdout hash.  The old adjudicated
mutant hash `a6cd95e0...4c5668` is provenance only; the repaired-source mutant
gets a newly authenticated hash.

### S2. `COEXTENSIVE-CHILD-OBJECT`

Supply source `(),(A)` and target `(),(A,N)` directly while retaining correct
types, a fresh child name, and inverse merge.  Native certificate construction
must refuse or return false before classifier promotion.

### S3. `FORGET-ONLY`

Give any target with `forget_N(target)=source` but a wrong fiber.  Recovery
alone must not earn splitting.

### S4. `CELL-COUNT-PADDING`

Use the exact set-valued counterobject

```text
source roles {A}, cells {(),(A)}, P=A
target roles {A,N}, cells {(),(N),(A,N)}.
```

The target has the expected scalar count three and its forgetful image equals
the source, but the fiber over `()` has child bits `{0,1}` while the fiber over
`(A)` has only `{1}`.  Exact fiber equality and branch binding must fail.

### S5. `ROLE-COUNT-ONLY`

After final source freeze, make a real source-only off-tree mutation replacing
the certificate predicate by the #192 inequality of
`(role_count,cell_count)`.  A certificate drop or swap must change or invalidate
the independently computed measurement, gate, primary outcome index, lineage,
claim row, and receipt seal.  No consumer may ingest a copied final boolean.

### S6. `TRANSPORT-SPLIT-SEVER`

Relabel the source and target but leave the parent, child, or one fiber row
untransported.  Groupoid covariance must fail with a nonzero exact residual or
typed refusal.

### S7. `SUPPLIED-SPLIT-BOOLEAN`

Attach `split_valid:true` to a coextensive target.  The field is inert; only
the native certificate may promote the gate.

### S8. `CERTIFICATE-PORT-SWAP`

Let the actual occurrence/branch use `P=not A` while attaching the otherwise
valid certificate for `P=A`; repeat with the child or target configuration
from another output branch.  Exact occurrence/source-key/port/bit/target
binding must refuse at lineage construction, before classification.

### S9. `OLD-CHILD-REUSE`

Reuse an old role name as the child, including a same-name role with a changed
type.  Exact disjoint role identity and old-type preservation must refuse.

### S10. `AMBIENT-TARGET-PADDING`

Add an extra target role or a cell that projects to no declared source cell.
The target-exhaustiveness and disjoint-fiber-union gates must refuse even if
the expected scalar cell count is restored elsewhere.

### S11. `CONTEXTUAL-BOOLEAN-ALIAS`

On C3, use `B` and `A and B` as the actual parent/query in otherwise identical
occurrences.  They differ as ambient formulas but agree on every nonzero C3
cell.  Their contextual parent key, Arrow/source identity, target context,
certificate, operator, endpoint law, and classifier lineage must be identical.
A raw-formula-key distinction is presentation-only and cannot promote or
split the physical source argument.

Each negative changes a physical/type object, not an expected answer.  Its
record contains old/new canonical bytes, changed path, consumed coordinate,
recomputed residual, kill predicate, and outcome effect.

## 5. Result-neutral regression wall

The repaired baseline must retain, exactly:

- the rational domain `g in Q intersect [1/3,1/2]`;
- the one contact-Cayley whole-filling primitive and Born clause;
- exposed `R`, `B`, `C`, `B2`, `K`, `527/175`, and reciprocal joint;
- native nondivision wording and positive history-conditioned control;
- the finite continuation grammar, all-input writer/cut rows, and active-reuse
  eraser control;
- matching resources, blind projection/class limitation, and fresh generator;
- source-groupoid doctrine, source identity, strict CLI, transactionality,
  receipt schema, outcome ladder, eligible cap, and every scope wall.

The existing scientific values must be recomputed, not copied.  Their values
may not move.  The self-test/check/attack registry hashes will move because the
new certificate and attacks are new evidence; this is expected and must be
recorded explicitly.

## 6. Pre-registered dispositions

Earliest applicable disposition governs:

1. `REPAIR-SPECIFICATION-INCONSISTENT` — the source, pin, or certificate types
   disagree, or an attack cannot be instantiated.
2. `P13-REFERENT-PRESENTATION-ONLY` — coextensive child syntax still acquires
   distinct physical support identity before the support gate.
3. `P13-SUPPORT-CHANGE-UNPROVEN` — any positive branch lacks the exact native
   split certificate or any S1--S11 control survives.
4. `REPAIR-GREEN-UNREVIEWED` — the repaired frozen bytes pass all inherited
   gates, all new split gates, independent reconstruction, and source mutation.

`REPAIR-GREEN-UNREVIEWED` restores eligibility to attempt the original Stage B
only.  It does not award
`P13-RELATIONAL-GAMMA-CLASS-RELATIVE-EVENT-GRAMMAR-PRICED` or any other
scientific rung.

## 7. Construction, freeze, and audit discipline

Authorized construction paths are exactly:

```text
v16/code/p13_gamma_exact.py
v16/note-paper13-gamma-source-freeze-v2.md
v16/PLAN.md
v16/LOG.md
STATUS.md
```

The evaluator's internal Stage-A task whitelist is exactly
`(v16/code/p13_gamma_exact.py,
v16/note-paper13-gamma-source-freeze-v2.md)`.  `PLAN`, `LOG`, and `STATUS` are
commit bookkeeping, not evaluator outputs.  The old freeze note and both
reports are authentication-only anchors.  No fresh, output, receipt,
verification, or paper path may exist during repair construction.  Development
self-tests and registered mutants may run; `--generate-fresh` and official
`--run` may not.

The committed repair pin, the two repo-path reports, their adjudication, and
the old freeze note must appear as live observed paths in `ANCHOR_SPECS`, the
ordered read ledger, and the gate-to-disk seal with exact hashes and consumed
keys.  None is scientific input.  The old evaluator hash is historical
provenance cross-checked from the authenticated old freeze note and
adjudication; record it as `historical-unobserved`, never as a successful live
disk anchor.  Do not copy the old evaluator to a new repo path.  The repaired
source authenticates its own current bytes and is bound by the v2 freeze note.

Before delivery, freeze final source bytes.  The v2 freeze note records the
source hash, check and attack counts, exact registry/payload/stdout hashes,
runtimes, static scan, artifact absence, and byte-identical repository-root,
alien-CWD, and true source-only off-tree/no-`.git` replay.  The freeze note does
not attempt to contain its own ordinary hash; that hash is computed only after
the note bytes freeze and is recorded in `LOG` and `STATUS` (or a separately
defined normalized self-hash may be used).  Any later byte change invalidates
the evidence.

After the repaired source commit, at least two independent no-import auditors
must rebuild the split fibers and the preserved scientific anchors.  Both must
replay S1 from the final bytes; at least one must independently construct S2,
S4, S6, S8, S11, and one freshness/ambient attack.  A fresh semantic survivor
blocks Stage B and requires a new adjudication; it is never silently patched
under this pin.

The 300-second per-mode cap, strict CLI, import denial, no-network/no-Git/no-
float rules, progress discipline, exact arithmetic, absent-destination
transactionality, and explicit-path Git staging remain binding.

## 8. Scope

This repair tests whether the evaluator recognizes the already pinned notion
of a proper point-free support split.  It does not show that the candidate
relation is metric geometry, that the law/event/division doctrine is selected,
that configurations actualize, or that the blind family is absolutely
irreducible.  It supplies no valuation, distance, dimension, topology,
curvature, continuum, gravity, GR, QFT, or phenomenology.

The sole next authorized event after this pin commits is the bounded source
repair on the five whitelisted paths.  Stage B and every later unit remain
closed until the repaired source survives independent post-freeze audit.
