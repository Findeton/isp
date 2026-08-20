# Paper 13 typed-groupoid source audit — records and integrity seat

## 1. Disposition

**Stage-C disposition: `NO-GO`.**

**Earliest affected outcome rung: `P13-REFERENT-PRESENTATION-ONLY`.**

The first decisive counterexample is an acceptance gap in the native
CREATE/MERGE/UNCHANGED certificate rows.  The field named
`certificate_transport_exact` checks only that both independently rebuilt
certificate collections are nonempty/final and have the same cardinality.
It neither transports and compares corresponding certificates nor emits the
uncached transformed certificate bytes required by the forward pin.  An
independent no-import probe changes the transformed certificate evidence to
four malformed non-certificate strings; the native row remains `all_exact`
and the groupoid promotion predicate remains `true`.  Measurement, claim,
and seal hashes all move, but the gate is not killed.

This is a source/receipt-readiness failure.  It does not overturn the exact
native nondivision, history control, division, reciprocal, or matching
calculations recorded below.  It does bar fresh generation and official
publication from these source bytes.

## 2. Authentication, isolation, and stopping rule

Before any scientific action I authenticated dispatch HEAD as
`2ee5fba54e7336e3aab80a401c976f8d2fbe670e` and completely read the two
frozen governing notes.  The pinned ordinary hashes were, and at report
freeze remain:

| object | ordinary SHA-256 |
|---|---|
| forward repair pin | `08f7f64efca6210eee356852ad9e9b59487ea62a55aeaf85a483f6a70b85b004` |
| frozen source | `b56383236a2aa0ff484aaa4c9082393beb4e4dd3ceb4d2724e4332bf68b6cba1` |
| source-freeze note | `33ff983e6c9b8f4bab6aa98abfea18f0f27d609b572c7980e05e7e63e80e51f7` |

During the audit the shared HEAD advanced to
`891c514ccae7eaac66c34b4090210b53f58705fe`.  The coordinator identified
that as the authorized separate commit of the already-frozen operator audit.
I did not inspect that commit or any sibling report path.  Reauthentication
showed that all three candidate bytes above were unchanged, so the bookkeeping
advance is not a corpus-integrity block.

Mutual blindness was maintained.  I did not read, list, infer, or message the
sibling source-audit report or its auditor.  I imported no function from the
candidate, rejected evaluator, fixture, scorer, or artifact.  All independent
work lived under `/private/tmp/p13-source-records.DqdUrN`.  I never invoked
`--generate-fresh` or `--run`, never read or created a future v2 artifact, and
made no publication write.  Candidate, pin, freeze note, ledgers, status
boards, PLAN, LOG, Git, and all non-report repository paths were left
unchanged by this seat.

Scientific work stopped when the certificate-transport acceptance gap became
reproducible.  The remaining actions were evidence hashing, report writing,
and integrity checks.

## 3. Black-box source runs and deterministic boundary

The only frozen-candidate executions were `--selftest` and named development
mutants.  Root, alien-CWD, and a true source-only off-tree tree with no `.git`
all returned zero and produced byte-identical stdout:

| run | exit | real time | stdout bytes | stdout SHA-256 |
|---|---:|---:|---:|---|
| repository root | `0` | `54.57 s` | `113764060` | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` |
| alien CWD `/private/tmp` | `0` | `63.92 s` | `113764060` | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` |
| true source-only off-tree | `0` | `65.21 s` | `113764060` | `23b10056e99432471dabe6dfc8f502b58e9e0cc9857eab4809040899a23e8938` |

The canonical selftest payload reports:

```text
status                         PASS
source bytes                   464013
source LF lines                11790
checks                         46 / 46
registered/executed/killed     112 / 112 / 112
registry SHA-256               3397140b241465181b73434a6798f971492801aff2a38b1488a4109544ddbee6
synthetic seal entries         155
normalized payload SHA-256     2b7372afe4dd63b72ad8da0c58293e6f6b88128ebd7da495bfc44e950a31afbf
selftest repair label          REPAIR-GREEN-UNREVIEWED
fresh cases read               false
official artifacts read        false
publication writes             0
```

The last label is the frozen source's development result, not this audit's
disposition.

Static AST inspection found standard-library-only imports, no float literal,
no tolerance, no `eval`/`exec`, no dynamic import, no network, no random/time
source, no Git query, no CWD query, and no expected-answer table.  Source
rooting is relative to `__file__`.  The strict parser exposes exactly
`--selftest`, `--mutant NAME`, `--generate-fresh` with its three named
arguments, and `--run` with its three named arguments; its internal negative
census refuses absent, unknown, extra, duplicate, incompatible, and relative
publication arguments.  Publication destinations are absent-path-only,
basename-whitelisted, and transactionally linked after staged-byte checks.

All nine future paths enumerated by the freeze note were absent by exact-path
metadata checks.  No directory-wide inspection of a sibling report path was
performed.

## 4. Independent no-import reconstruction

The independent reconstruction script is
`/private/tmp/p13-source-records.DqdUrN/records_reconstruct.py`, ordinary
SHA-256
`74360a3723187f634e68a7d2b6a94c8a143fda9946f4e6db083e23f033326c42`.
It was frozen before source inspection and does not import the candidate.  It
returned zero in `2.92 s`.  Its one-line output has `2154` bytes and ordinary
SHA-256
`31cef15365afe446e36befd6a8ddddd400fdf18ff7f98d11dbce9185a0bc63c3`.

It independently rebuilt and matched:

- all `46` selftest evidence hashes and all `112` old/new mutation-object
  hashes, change predicates, kill predicates, and ordered registry hash;
- all `34` total bijections for carrier sizes zero through four and all
  `14050` associativity triples, including mixed identity completion;
- all `13` native presentation rows, both identities, both inverses,
  associativity, total maps, presentation transport, source-key movement,
  object-action flags, and uncached operator/endpoint residuals;
- `72` ambient Boolean representatives and `42` contextual classes;
- `12` generator families, `312` source columns, `468` bound nonzero
  transitions, and `156/156/156` CREATE/MERGE/UNCHANGED counts;
- exact `R`, `B`, `C`, `B2`, `K`, the `527/175` interval certificate, writer
  and record controls, history control, reciprocal joint, matching class,
  source lineages, claim keys, and all `155` synthetic seal entries.

The exposed exact matrices were unchanged:

```text
R  = [[3/5, -4/5], [4/5, 3/5]]
B  = [[9/25, 16/25], [16/25, 9/25]]
C  = [[49/625, 576/625], [576/625, 49/625]]
B2 = [[337/625, 288/625], [288/625, 337/625]]
K  = [[351/175, -176/175], [-176/175, 351/175]]
```

## 5. Mandatory G1 and G18 changed-source controls

Both required real mutations were private source-only copies invoked only
with `--selftest`.  A separate no-import semantic probe supplied the law,
gate, outcome, and dependency evidence; crashes were not treated as the
semantic evidence.

### G1 — empty left identity

The exact private patch replaces iteration over every complete source-carrier
label by iteration over only the explicit left rows:

```diff
-        sources = _carrier_names(source_carrier, role_carrier)
         composed = tuple(
             (
                 source,
-                right_map.get(left_map.get(source, source), left_map.get(source, source)),
+                right_map.get(target, target),
             )
-            for source in sources
+            for source, target in left
         )
```

The mutant source SHA-256 is
`96ef980a0f4d66e13a3723c930f87237cd00d5ed9a9cd691ae6faed36ae22fab`.
It exited `2` after `1.28 s`, emitted empty stdout
(`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`),
and emitted stderr SHA-256
`9cfd5f98743338a6c0d4de2300b9df7c90c03b61f5bfe1edb7c710d1fa1588ee`
with the refusal `groupoid role map omits a nonidentity source`.

Independently, `id_A` followed by `w:A->B` gives the correct total map
`[(A,B)]`; the old first-row-only loop gives no sparse row, whose completion
is `[(A,A)]`.  The exact law residual is `1`.  Outcome index moves `12 -> 1`
and the earliest rung is `P13-REFERENT-PRESENTATION-ONLY`.  Independent
old/new hashes were:

| dependency | frozen | G1 mutant |
|---|---|---|
| measurement | `c10f1539b3ee0ea38dee5b0e785e6de8f4c7baee6019e23f9d6fc4416c38da48` | `13eea1474eea86f19a93f15e931a6579994cdb02d8914238744c24682d092be7` |
| lineage | `bc934cd21cdc81995803ee9a1f4288d5732cd6578cf2e142f81a31859fb35484` | `1b9cfa258508775900e0ca06d8347c27ed59f6d38a225c06026289051580f4e7` |
| claim | `5c567bbceab518757fdcd8a7cc9c017bad20e1c95f07c182fd8038dea14e93e5` | `92a6b378fb74902814df439495fe1bf31fd3ae32313541c9d0955e0eeb764669` |
| seal | `564ae98b15bbee23ddc7cbeb7dfe23593bb25bd94c7c0620fbb100db23b7fb31` | `3b6c3b1dc8aedd9b25fbd30d25ef841304ce31ec3896fd2c8a5a15f0667579d6` |

### G18 — copied aggregate Boolean

The exact private patch replaces the full native conjunction with
`return groupoid["all_exact"]`.  Its SHA-256 is
`fc3967b58ff07286c45822b33a0ed07bf8c322944f2a813555774696ea7200d8`.
It exited `1` after `53.05 s`, emitted empty stdout, and emitted stderr SHA-256
`95c58c1e2baf0bd32b73b719e98284c6c19822853be3e111b02dd15d8f8d3dab`
with `seal manifest coverage is incomplete`.

For a copied aggregate held `true` while native left identity is `false`, the
frozen predicate returns `false` and the mutant returns `true`.  The native
row dependency is unchanged; the consumer AST, measurement, claim, and seal
move.  Outcome index moves `12 -> 0`, rendering
`P13-SPECIFICATION-INCONSISTENT`.

| dependency | frozen | G18 mutant |
|---|---|---|
| consumer AST | `12291b9af5e6c91aeee4d299981e20a624bc3d6944fae121bfe929ab9d70a554` | `1f516e87af5c13c11a2ab83caf76abf7ec1145eda530eb1ebf6f3c1bd566b5d1` |
| measurement | `96d057d9f936302dfe21dc021653607ed6e25b3e4bcd52ec3b3ff746f5bf357d` | `fdca6162f666c09ca552cdbab48ceccae18631fb0833372a1486c73004a94ba0` |
| claim | `1280e411e82b010986105852b5bff03b31b1fc7b38cd3d3e9033e76a3b078213` | `9ed9d9c56d137cd9efff6ac5d8c350e1c41b481437fbea38f8d62ecc998a1e23` |
| seal | `e5d5a2718e3a2875a33517203770df5925a5b24e4df1daecbcace3f2ce817fcd` | `d92e5b6bd899fd53faacfefd4580538aa9c924619d7a5e04c9553296c7ce0da2` |

The combined no-import acceptance probe is
`/private/tmp/p13-source-records.DqdUrN/source_acceptance_probe.py`, SHA-256
`26f9b31abf19a02cdd302c4b353652ede8b25c0c714a2a0530f18388f70eadf5`.
It returned zero in `8.81 s`.  Its `7728`-byte output SHA-256 is
`0d910b5676da16f5154149ac457a5722c52b7c4fca6d270d33e2d5457b4a0d1f`
and its independently verified normalized payload SHA-256 is
`9a3e0d4c6ba03f9df995bfa14b1b7fecf792e2cc910e3c0848eada377ad3cac3`.

## 6. Decisive counterexample: certificate transport is not in the gate

The forward pin requires the completed witness to act exactly on
`BoundSplitCertificate` objects and classifier-consumed hashes.  It requires
uncached identity, inverse, nontrivial-pair, and three-witness checks and says
explicitly that a transported hash without transported bytes is non-evidence
(pin lines 158--186).  Its receipt contract again requires uncached old/new
bytes, residuals, and dependency hashes for every object in that action
surface (pin lines 352--379).

The frozen implementation does something weaker:

1. Source lines 5345--5379 independently enumerate original and transformed
   certificate collections and serialize only operation, counts, two hash
   lists, two all-final Booleans, and count preservation.
2. Source lines 5412--5417 define `certificate_transport_exact` solely as
   `all_original_final && all_transformed_final && count_preserved` (or
   vacuous `true` when no certificate row exists).
3. Source lines 5420--5437 copy that Boolean into native `all_exact`.
4. Source lines 5910--5924 make promotion consume that same Boolean.  The
   original/transformed hash lists are not in its backward slice.
5. The sole detailed `split_certificate_covariance` object covers one
   representative certificate.  It does not supply paired CREATE, MERGE, and
   UNCHANGED bytes for the twelve certificates claimed by the three native
   rows.

The black-box selftest confirms that each of the three rows has original and
transformed count `4`, both all-final flags `true`, count preservation `true`,
and `certificate_transport_exact=true`.  No row contains original or
transformed certificate bytes.

The independent probe replaced the CREATE row's four
`transformed_classifier_hashes` by four copies of
`NOT-A-TRANSPORTED-CERTIFICATE`.  Recomputing the source's literal predicate
gave:

```text
transport evidence valid                  false
certificate_transport_exact               true
native row all_exact                       true
groupoid promotion before                  true
groupoid promotion after                   true
```

The mutation is not invisible to hashing:

| dependency | frozen | malformed transformed evidence |
|---|---|---|
| measurement | `a5b99c91f04966c020fc28f31de96e95f16826578c9dd54d517e28cc735b911d` | `d84b7843a4b5a1d345c601f7d7b802c0a638933f7e62356b83fbf9117b257568` |
| referent claim | `7774704022b5aab690ad5484ce87bda142ad6c94890dcc9ba8455beca0a2537a` | `a9f1d2d34680ec2a41271b65eca99ceb2aae3b9ec60f1d2219e81dd5298c33d7` |
| seal | `1063e0fba02ce17cf60b178751dcec106708537723b639a6280e49d53c4ceb1c` | `125f2c6bb8bae54ba011b32fd01972b16335e8ee5cbc3efedd45d66e9949c84e` |

Thus the seal records that some bytes changed, but the scientific gate still
accepts the changed object.  Coverage hashing is not a proof of functorial
certificate action.  This defeats the universal native groupoid/receipt
claim at the referent gate and is the report's decisive `KILL-1`.

## 7. Preserved records, division, reciprocal, and scope controls

The following are independent `NON-KILL` controls, completed before the
decisive gap was identified.

### Native nondivision is not ontological incompleteness

`B` is invertible and the unique native source-independent factor is

```text
K = [[351/175, -176/175], [-176/175, 351/175]].
```

Its two off-diagonal entries are `-176/175`; therefore no positive
source-independent restart kernel exists on the declared native
configuration carrier.  The rational interval proof is exact on
`1/3 <= g <= 1/2`, uses the correctly named
`derivative_sign_witness`, and gives the universal lower bound `527/175 > 1`.

This is native stochastic nondivision, not a missing, unreal, or ontologically
incomplete intermediate state.  The frozen sentence correctly says that a
definite configuration may still be actual there and excludes only an
autonomous Markov restart conditioned on that configuration.

### History/enlarged-carrier control is mandatory and nonfatal

The history-conditioned joint is independently `B(a|q) C(b|q)`.  Both
normalizations are exactly `1`, every coordinate is nonnegative, and eight
coordinates are positive.  This is the required positive Markovization on an
enlarged/history carrier.  It neither refutes native nondivision nor licenses
calling native nondivision a state defect.  The registered
`HISTORY-PASSED-OFF-AS-NATIVE-K` and `NONDIVISION-AS-STATE-DEFECT` controls
both returned zero and were killed.

### Record-relative division

The writer is normalized on all four blank input states.  The recorded cut
gives the exact `B2` above, all `16` alternate-cut rows have zero residual,
and all zero-amplitude targets remain present (`32` in the representative
recorded chain).  The continuation grammar contains six exact generator
letters.  Base, composition step, and the depth-two enumeration of `43`
licensed words have zero intertwining residual.  Reactivating the carried
record port and applying the inverse toggle erases it exactly.

This establishes division only relative to the frozen writer, record
projectors, continuation grammar, and alternate cut.  It is not an automatic
division theorem for arbitrary continuations.

### Reciprocal and matching scope

The reciprocal writer-to-reader joint is exactly

```text
{00: 9/25, 01: 0, 10: 144/625, 11: 256/625}.
```

The opposite-incidence counterfactual zero is preserved.  Both development
matching members use one direct global Gamma call, have exact resource and
blind-prefix parity, share the prior-record law and primitive root, and have
unequal exposed responses.  This excludes only the frozen incidence-erased
transducer class.

The native size-twelve row uses the complete 24-role context but only the
disclosed fixed two-query subset `(1,8)`.  That is a valid source-transport
control, not the future post-freeze size-twelve global-law confirmation.  I
record this as `NARROWING-1`, not a kill.

## 8. Registry, lineage, claims, seals, and named attacks

The source constructs source keys from the full typed arrow and source
configuration, re-evaluates operators after transport, and exposes the
expected G1 and G18 dependencies.  Claim keys are two-way equal with the
twelve gates; registered falsifiers must name present changed objects.  The
synthetic seal manifest covers all twelve claims, all scope walls and
coordinates, all `112` mutations, the read row, artifacts, and sealed
top-level keys, for `155` entries.  Those structural checks pass, but they do
not cure `KILL-1`: the certificate transport fact itself is absent from the
predicate.

The following additional named black-box controls all returned `0`, reported
`PASS/KILLED`, changed their objects, and had valid normalized payload hashes:

```text
EMPTY-LEFT-IDENTITY
CERTIFICATE-TRANSPORT-CACHE
COPIED-GROUPOID-BOOLEAN
BRANCH-SUM-ONLY
RESET-WRITER-CHAIN
DELAYED-READER-SEVER
HISTORY-PASSED-OFF-AS-NATIVE-K
NONDIVISION-AS-STATE-DEFECT
FRESH-GLOBAL-RELABEL-SEVER
```

`CERTIFICATE-TRANSPORT-CACHE` is a useful one-certificate stale-cache
control, but it does not test the missing pairwise native CREATE/MERGE/
UNCHANGED action.  Passing the named registry therefore does not answer the
independent acceptance counterexample.

## 9. Findings ledger

1. **`KILL-1 — NATIVE-CERTIFICATE-TRANSPORT-NOT-EVIDENCED`.**  The native
   certificate rows accept finality plus equal counts as exact transport,
   omit paired transformed bytes, and leave their hash lists outside the
   promotion predicate.  A malformed transformed-evidence object survives
   promotion.  Earliest rung: `P13-REFERENT-PRESENTATION-ONLY`.
2. **`NON-KILL-1 — NATIVE-NONDIVISION-PRESERVED`.**  The exact negative
   native factor forbids only a positive source-independent restart on the
   declared carrier.  It does not establish ontological incompleteness.
3. **`NON-KILL-2 — HISTORY-CONTROL-PRESERVED`.**  Positive history/enlarged-
   carrier Markovization is mandatory scope evidence and does not erase the
   native statement.
4. **`NON-KILL-3 — RECORD-DIVISION-PRESERVED`.**  Writer normalization,
   projector-sector division, six-letter continuation grammar, alternate
   cuts, and inverse erasure are exact at their declared scope.
5. **`NON-KILL-4 — RECIPROCAL-AND-BLIND-CLASS-PRESERVED`.**  Reciprocal and
   one-call matching controls are exact and remain class-relative.
6. **`NARROWING-1 — SIZE-TWELVE-DEVELOPMENT-ROW`.**  The complete 24-role
   context with a fixed two-query subset is source-only evidence, not a
   post-freeze fresh/global confirmation.

## 10. Required repair and final gate

Before this source can pass Stage C, every native CREATE, MERGE, and UNCHANGED
certificate row must serialize paired original, literally transported, and
independently rebuilt certificate bytes; verify identity, inverse,
composition, and classifier-consumed lineage on those pairs; expose exact
residuals; and make the referent promotion predicate consume those facts.
An independently changed certificate pairing must then be killed even when
both collections remain final and equipotent.  The receipt and its no-import
verifier must recompute the same action rather than trust a Boolean or hash.

Until that repair is separately pinned, frozen, and independently audited,
the Stage-C records/integrity disposition is **`NO-GO`**, fresh generation is
barred, and the earliest defensible scientific outcome is
**`P13-REFERENT-PRESENTATION-ONLY`**.

The ordinary SHA-256 is intentionally not embedded in these self-referential
bytes; it is reported externally after freeze.

normalized_sha256: 3baf9c6fb42c0595be22d7610ec54aeed360b765b563139c20676f83ddad6a82
