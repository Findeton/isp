# Paper 13 v3 typed-groupoid source audit — records and integrity seat

## 1. Disposition

**Stage-C disposition: `NO-GO`.**

**Earliest affected outcome rung: `P13-REFERENT-PRESENTATION-ONLY`.**

The first decisive counterexample is a keyed-attachment survivor in the
complete `468`-transition certificate-action census.  In two distinct
identity rows I swapped the entire target packet: the literal-transport
reference, independent-rebuild reference, and transported pairing key.  The
object store, counts, source keys, target multiset, and every copied equality
coordinate remain unchanged.  Both identity actions are now false, but the
exact predicate used by `groupoid_promotion_predicate` still returns `true`.

This defeats the claim that the promotion backward slice consumes the
key-to-object action rather than only content-address membership, target
self-equality, and trusted coordinates.  It also shows that the registered
`CERTIFICATE-KEY-ATTACHMENT-SWAP` is too weak: that mutant swaps only the
rebuild reference, so it is killed by the much easier
`literal_transport_ref == independent_rebuild_ref` check and never tests a
wrong but internally self-consistent target packet.

The failure is limited to source adjudication and receipt readiness.  It does
not change the independently reconstructed nondivision, history,
record/division, reciprocal, or matching values and scope controls below.
Fresh generation and official publication remain barred for these source
bytes.

## 2. Authentication, isolation, and stopping rule

Before scientific work I authenticated dispatch HEAD as
`8a272e98fb83e0a42cb4931173acc0d76b29afe2`, authenticated the three pinned
objects, and read the complete delta pin and freeze note.  At report freeze
the candidate bytes remain:

| object | LF lines | bytes | ordinary SHA-256 |
|---|---:|---:|---|
| `v16/code/p13_gamma_exact_v3.py` | `14941` | `595989` | `cecf46061df95f57e63b491c380f015fdce297b6ac52dd78f79792495eafb111` |
| `v16/note-paper13-typed-groupoid-source-freeze-v3.md` | `380` | `18271` | `02e22f32ce44d46104377d77469cefc1e7c3ca82445f119ede2056c9b8d16028` |
| `v16/note-paper13-typed-groupoid-source-delta-pin.md` | `784` | `39364` | `44fe6f86eeb6990537b36760eda68da5ccdc31fd8d15dfe003b42e6d4324a154` |

The delta pin's normalized SHA-256 is
`354b28c183622d61dcf643df4e1c654130f50e8c2ab5be9b34bbe4da357ab76a`.

During the audit the shared HEAD advanced to
`ec3100ef38ff782bb146edba70061d1f2236c27f`.  The coordinator identified
this as the authorized separate commit of the other seat's single report.
I did not inspect or list that path.  Reauthentication showed that the
source, freeze note, and delta pin bytes were unchanged, so the bookkeeping
advance is not a corpus-integrity block.

Mutual blindness was maintained.  I did not read, list, infer, or message the
sibling v3 report or reviewer.  I imported no candidate, evaluator, fixture,
scorer, or artifact function.  All independent work lived under
`/private/tmp/p13-v3-records.IZcNIs`.  I never invoked `--generate-fresh` or
`--run`, created no nonce or future artifact, and made no publication write.
Candidate, notes, PLAN, LOG, STATUS, Git, and all non-report repository paths
were left unchanged by this seat.

Scientific work stopped when the target-packet swap became exactly
reproducible.  Subsequent work was limited to evidence hashing, source-line
localization, report writing, and report-integrity checks.

## 3. Independent reconstruction and black-box boundary

The independent reconstruction was completed before implementation
inspection.  The standard-library-only script
`/private/tmp/p13-v3-records.IZcNIs/independent_reconstruction.py` has
ordinary SHA-256
`4652b97b5f93a681bf68a7dc9a17f058e982089e9a7e7247e7ad9c32be53f5f7`.
Its canonical reconstruction SHA-256 is
`3cdd90f7acd32dc1c476ad4040e6b9490cedf57d5650909c1f2ce752700abb9d`.
It independently obtained:

- `34` total bijections and `14050` composable triples;
- `72` ambient representatives and `42` contextual classes, with per-context
  counts `3/3`, `15/15`, `14/7`, `14/7`, `14/7`, and `12/3`;
- all `13` configuration-row counts, summing to `988`;
- `12` generator families, `312` source columns, `468` bound transitions,
  and `156/156/156` CREATE/MERGE/UNCHANGED operations;
- `149` attacks as `112 + 16 + 21`;
- the exact matrices, native bound, and reciprocal joint recorded in Section
  6.

The only frozen-candidate executions were `--selftest` and named development
mutants.  Root, alien-CWD, and a true one-file directory with no `.git`
returned zero within the `300 s` cap and emitted byte-identical stdout:

| run | exit | real time | stdout bytes | stdout SHA-256 |
|---|---:|---:|---:|---|
| repository root | `0` | `227.45 s` | `234018261` | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` |
| alien CWD, absolute source | `0` | `273.59 s` | `234018261` | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` |
| true one-file/no-`.git` | `0` | `275.14 s` | `234018261` | `d81fe81c497471a0e8c87c5729f592f7ec5be614616f51dec768f7b2d1f4df52` |

All three emitted progress within each sixty-second boundary.  The alien
working directory stayed empty.  The off-tree directory retained exactly
the pinned source copy and no `.git` or generated file.

The canonical payload reports `49/49` checks, `149/149` mutations killed,
registry SHA-256
`bf00b70045431960356b8a1a0032a1aea2a598ddca750f98d6c1f15867ac5d12`,
normalized payload SHA-256
`43aa7476d76315329bb7bd464131c8f3ac35e797c1fef249decc63b4c29d7955`,
no fixture or official-artifact read, and zero publication writes.  I
independently recomputed that normalized payload hash from the raw stdout.
The source's `REPAIR-GREEN-UNREVIEWED` label is a development result, not this
audit's disposition.

## 4. Positive action, byte-store, and registry controls

The following positive controls passed before the counterexample was found:

- A no-import byte-store verifier rehashed `8511` emitted rows comprising
  `252` `BoundaryNode`, `812` `Configuration`, `528`
  `CertificateActionInput`, and `6919`
  `NormalizedConfigurationTransport` objects.  There were `8171` unique
  objects and zero errors; the aggregate verification SHA-256 was
  `406f4b5743e3237394e9d0b817ceced3b7177299ea885adaf485e18c5ea3ae34`.
- The same verifier reconstructed every inherited certificate hash,
  classifier-consumed byte string, law identity, address-bound node,
  source/target coordinate, operation, proof, child, and presentation-identity
  byte string.  All normalized transport self-hashes also recomputed.
- An independent pairing verifier recomputed `1728` emitted key attachments
  from raw `CertificateActionInput` bytes.  It covered all `468` global row
  keys and identity targets, the `12` nontrivial family targets, and every
  native certificate law triple.  All were exact; aggregate SHA-256
  `918e04e54e319556816c0d1d82aca3aed93e18dc6a9655fef4610fd202c488e4`.
- Reference closure and final-object equality passed for all `13` native
  configuration censuses, all `3` CREATE/MERGE/UNCHANGED certificate
  censuses, and the tensor row.  Identity, inverse, composition, and
  associativity outputs agreed in every clean row.
- All `37` v3 mutation records had independently valid old/new object hashes,
  changed predicates, evidence hashes, kill statuses, and registered outcome
  drops.  Their aggregate record SHA-256 was
  `c8e3d6c0509c83df0d79cd400a8339de66913baea3a82eec33eef03d54b3534b`.

Named black-box replays of A1, C1, C4, C17, and C18--C21 all returned
`PASS/KILLED` and changed their recorded objects.  In particular, the clean
source has the intended closed signatures
`act_configuration(source_node, configuration, witness)`,
`assert_configuration_target(source_node, asserted_target_node, witness)`,
and `act_certificate(witness, certificate_action_input)`.  The
`CertificateActionInput` constructor and factory do bind the law, complete
presentation identity, generator address/subpresentation, nodes, Arrow,
occurrence, port, configurations, proof bytes, classifier bytes, and nonzero
coefficient.  These are important non-kill facts.  The defect is in the
serialized promotion consumer, after those correct objects are built.

## 5. Decisive counterexample: a wrong keyed identity packet promotes

The no-import reproducer is
`/private/tmp/p13-v3-records.IZcNIs/test_identity_packet_swap.py`, ordinary
SHA-256
`90cfbf3af2c3913dee5b2afe291854859a360075139363751a15dd8ba570b6c0`.
It mirrors the literal conditions of source functions
`_certificate_triple_reference_exact` and
`_complete_certificate_action_census_exact`; it does not import or call the
candidate.  Its one-line `1311`-byte result has ordinary SHA-256
`7924512877543815ec4f61ca487d96924273804cb7786942ed68c69da7962c2e`
and reports `counterexample_exact=true`.

The mutation uses global generator family `0`, identity rows `0` and `1`:

```text
row 0 input  344071d781ad56d73f2568269959a7eea4c94aaed8f324e19c8643af83a1b60b
row 1 input  d7e62bac853cc9e5e08b31e198cfeeb159aa6b8d51e620ae9f2c4b4a566f76e3
```

For those two rows only, it exchanges as one packet:

```text
literal_transport_ref
independent_rebuild_ref
transported_pairing_key
```

The input rows and original pairing keys stay fixed.  The two target objects
remain present exactly once, their complete bytes and content hashes remain
valid, literal and rebuild still agree within each row, every stored equality
coordinate remains `true`, and the target multiset and all `468`/`312`/
`156x3` counts are preserved.  The complete-action object changes from

```text
2dc822de1dfcc90ac33105e09a8e1f758660999faa12a6d6f81d56df5c60bcc9
```

to

```text
fb0f81baa8e1a2e091dcf19de024c13c10bc258fe39427a94cf1facaee705f3b
```

while both the source-equivalent complete-census predicate and every
complete-certificate clause of the promotion predicate remain `true` before
and after.  Yet the identity law now fails twice:

```text
row 0 target = d7e62bac... while input = 344071d7...
row 1 target = 344071d7... while input = d7e62bac...
```

The corresponding original/transported pairing-key hashes are also crossed:

```text
296a64a9ac0110e206d950a5aaaf70403c8b3e2fa3040ae47ef4d87469f673b9
f38d5d5feeb238744ba70b8d570b4625d3ed713513f4cb352a9c260864404ebf
```

The implementation gap is exact:

1. Source lines `6573--6607` require content-address membership,
   `literal_transport_ref == independent_rebuild_ref`, trusted `true`
   equality coordinates, and a trusted `exact=true`.  They never recompute a
   pairing key from the referenced complete bytes and never check the
   original-to-target action.
2. Lines `6703--6737` check only
   `identity_triple.original_ref == input_ref`.  They do not require either
   identity target reference to equal `input_ref`, do not require the
   transported pairing key to equal the row/original key, and do not consume
   the row's independently computed `exact` field.
3. Lines `8033--8057` repeat the same incomplete tests in
   `groupoid_promotion_predicate`, so all other unchanged groupoid clauses
   leave the full promotion result `true`.
4. The registered C4 implementation at lines `10819--10824` swaps only
   `independent_rebuild_ref`.  That is rejected by line `6596`, but it does
   not test a self-consistent wrong target packet attached to a different
   source key.
5. The static promotion slice at lines `11629--11663` binds the consumer and
   helper functions but omits the producer
   `measure_complete_certificate_action_census`.  A producer-side packet swap
   therefore does not fall through the source-AST specification gate.

This is not an enumeration reorder.  Enumeration order is unchanged; the
object attached to each derived original key changes.  It is therefore the
pinned C4 kill condition itself.  Content-address and seal hashes record that
some bytes moved, but the groupoid gate, referent Boolean, typed-groupoid
lineage `all_same_root`, claim result, and outcome index do not fall.  A seal
that faithfully hashes an accepted false action is not a scientific kill.

## 6. Preserved nondivision, records, reciprocal, matching, and scope

These controls were independently completed before `KILL-1` and are not the
reason for `NO-GO`.

### Native nondivision is not ontological state incompleteness

The exact exposed matrices remain

```text
R  = [[3/5, -4/5], [4/5, 3/5]]
B  = [[9/25, 16/25], [16/25, 9/25]]
C  = [[49/625, 576/625], [576/625, 49/625]]
B2 = [[337/625, 288/625], [288/625, 337/625]]
K  = [[351/175, -176/175], [-176/175, 351/175]]
```

The unique native source-independent restart factor has two negative
off-diagonal entries.  The rational interval certificate on
`1/3 <= g <= 1/2` gives the universal lower bound `527/175` outside the
stochastic spectral interval.  Therefore the declared native cut is not an
autonomous positive stochastic division.

That result does **not** say that an intermediate configuration is unreal,
missing, or ontologically incomplete.  The frozen native sentence preserves
the distinction exactly: a definite configuration may still be actual; what
is excluded is a source-independent Markov restart conditioned only on that
configuration.

### History/enlarged-carrier Markovization is mandatory and nonfatal

The history-conditioned joint has two exact normalizations equal to `1`, is
nonnegative, and has `8` positive coordinates.  This is the required positive
history/enlarged-carrier Markovization.  It neither kills native
nondivision nor licenses rebranding native nondivision as a state defect.

### Record-relative division

The writer is normalized on all four blank input states.  The complete target
has `36` states, all `36` are returned, and `32` zero-amplitude targets remain
explicit.  The six-letter continuation grammar, all generator
intertwinings, alternate-cut all-input residual `0`, record projectors, and
active inverse erasure are exact.  This establishes division only relative
to the typed writer, record sectors, grammar, and chosen cut; it is not an
unconditional division theorem.

### Reciprocal and matching scope

The reciprocal joint is exactly

```text
{00: 9/25, 01: 0, 10: 144/625, 11: 256/625}.
```

It normalizes to `1` and retains only the declared raw-relation-mediated
reciprocal-response/proto-backreaction scope.  Matching preserves one-root
lineage, resource parity, blind-prefix equality, prior-record-law equality,
and unequal exposed responses.  The exclusion remains relative to the
declared blind-transducer class, never absolute.

The source prints the permanent walls: event filling is
`PRICED-KINEMATICS`; division is
`TYPED-CANDIDATE-AND-GRAMMAR-RELATIVE`; actualization is `POSTULATED`; and
valuation, metric, curvature, continuum, and GR remain `UNCONSTRUCTED`.
Nothing here selects a law, coupling, catalogue, event filling, division
doctrine, actual outcome, topology, metric, curvature, gravity, continuum,
GR/QFT, particle, or phenomenology claim.

## 7. CLI, chronology, source mutations, and artifact integrity

Static inspection found standard-library-only imports, exact
`fractions.Fraction` arithmetic, and no scientific float, tolerance,
network, random/time, Git, CWD query, fixture import, prior-source import, or
expected-answer table.  Source rooting uses `__file__`.  The strict parser
and internal negative census accept only the four pinned forms; this seat ran
only `--selftest` and registered mutants.

All nine future v3 paths named by the delta pin were absent, including fresh,
output, receipt, verification, paper, and bundle paths.  The selftests report
zero publication writes, no fresh read, no official artifact read, and no
fixture evaluation.

The freeze note's A-SOURCE-CORE, A-SOURCE-ASSERT,
C-SOURCE-PROMOTION, and C-SOURCE-ACTION evidence has the required source,
probe, capture, dependency, exit, and zero-write hashes, and records the
claimed specification/outcome/lineage/claim/seal movement.  Those attacks are
orthogonal to `KILL-1`.  They mutate the core/action/consumer signatures.  The
survivor changes a complete-action producer attachment while leaving those
signatures and all positive counts unchanged, and that producer is absent
from the static backward-slice binding.

The future receipt is structurally capable of serializing the complete
measurement, action stores, mutation rows, reads, claims, lineage, scope, and
seal.  It is not scientifically ready because its candidate promotion check
accepts the wrong keyed identity action above.  A future no-import verifier
must not inherit that acceptance rule.

## 8. Findings ledger

1. **`KILL-1 — COMPLETE-IDENTITY-TARGET-PACKET-ATTACHMENT-UNVALIDATED`.**
   Two target packets can be crossed between distinct identity rows while
   preserving complete bytes, target multiset, counts, literal/rebuild
   equality, and every current promotion clause.  Earliest rung:
   `P13-REFERENT-PRESENTATION-ONLY`.
2. **`REGISTRY-GAP-1 — C4-TESTS-ONLY-REBUILD-MISMATCH`.**  The named C4
   mutant proves that unequal literal/rebuild references are rejected; it
   does not test the pinned wrong keyed attachment with an internally
   self-consistent target packet.
3. **`NON-KILL-1 — COMPLETE-INPUT-BINDING-PRESERVED`.**  Clean
   `CertificateActionInput` literals, raw hashes, addresses, and all `1728`
   inspected key attachments reconstruct exactly.
4. **`NON-KILL-2 — FUNCTOR-LAW-ROWS-PRESERVED`.**  Clean identity, inverse,
   composition, associativity, configuration, certificate, and tensor rows
   close exactly; the kill is the receipt-side attachment consumer.
5. **`NON-KILL-3 — NATIVE-NONDIVISION-PRESERVED`.**  Native stochastic
   nondivision is exact and is not ontological state incompleteness.
6. **`NON-KILL-4 — HISTORY-CONTROL-PRESERVED`.**  Positive
   history/enlarged-carrier Markovization is mandatory scope evidence, not an
   automatic kill.
7. **`NON-KILL-5 — RECORD/DIVISION/RECIPROCAL/MATCHING-SCOPE-PRESERVED`.**
   The exact values and their class-relative limitations remain unchanged.

## 9. Literal repair and final gate

At minimum, each global identity row must be rejected unless

```text
row.exact is true
identity_triple.original_ref
  == identity_triple.literal_transport_ref
  == identity_triple.independent_rebuild_ref
  == row.input_ref
identity_triple.original_pairing_key
  == identity_triple.transported_pairing_key
  == row.pairing_key
```

The generic triple consumer must also decode the referenced complete inputs
and recompute both pairing keys from their raw bytes, rather than merely
checking that supplied keys and `true` coordinates exist.  Nontrivial and
functor-law rows must validate the corresponding original-to-target action
attachment and chain, not only target self-equality.  The promotion static
slice must bind the complete-action producer as well as its consumer.

C4 must then swap the full target packet between two derived original keys,
preserve the target multiset and counts, feed that changed complete census
through the actual promotion/gate/lineage/claim/outcome path, and require the
referent gate to fall.  A pure enumeration reorder must continue to pass.

Until that repair is separately pinned, frozen, and independently audited,
the records/integrity disposition is **`NO-GO`**, fresh generation remains
barred, and the earliest defensible scientific outcome is
**`P13-REFERENT-PRESENTATION-ONLY`**.

The ordinary SHA-256 is intentionally not embedded in these self-referential
bytes; it is reported externally after freeze.

normalized_sha256: e58661b3e691e4acb0dd6502123471cb62690512b3d232175501c1634e0eaaa4
