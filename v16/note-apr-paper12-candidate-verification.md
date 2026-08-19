# Paper 12 negative-candidate verification

**Date:** 2026-08-19

**Status:** GREEN — CANDIDATE UNREVIEWED

**Binding pin:** `v16/note-apr-paper12-negative-candidate-pin.md`, commit
`5f52758`, SHA-256
`6341a1184426f3a6be0ad619d9f02340124a76e5484bb94609462d5d765a6ebd`.

**Source freeze:** commit `22ba8a1` (`v16 #182`).

This note verifies the standalone exact reconstruction and the scientific
candidate.  It does not review the candidate and does not promote any positive
physical `Gamma`, region quotient, process, record, geometry, or successor
law.

## 1. Frozen files and hashes

| role | path | SHA-256 | bytes |
|---|---|---:|---:|
| exact source | `v16/code/apr_paper12_exact.py` | `c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7` | `50150` |
| transcript | `v16/code/apr_paper12_output.txt` | `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f` | `635` |
| receipt | `v16/code/apr_paper12_receipt.json` | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` | `24687` |
| scientific candidate | `v16/paper-12-atomless-regions-and-the-missing-gluing-law.md` | `cdb212c57c8b80099f9fc17eb0b1c5ed90c38ae2f5db7c50eb3038eb893f4de8` | `18626` |

The receipt's canonical payload SHA-256 is
`1c6ded1e366cd4e3863a2774285ade5663f80e5228ed4077d0eb5b33bb0286f5`.
Removing the `payload_sha256` field and canonicalizing the remaining JSON
reproduces that value.  The receipt's transcript hash equals the ordinary
transcript hash above.

## 2. Source isolation and exactness

The source imports neither `apr_score` nor `apr_fixtures`.  Its only imports
are Python standard-library modules.  AST inspection found:

- `68` top-level syntax nodes;
- zero float literals;
- zero forbidden scorer/fixture imports;
- no randomness, network, Git, subprocess, runtime CWD, tolerance, or sleep
  dependency;
- no source-created bytecode under `python3 -B`;
- no whitespace error under `git diff --no-index --check`.

The source was committed before either publication destination existed.  The
official run then authenticated the immutable ONE-GAMMA gate, the frozen v5
verification note, the v5 transcript, the v5 receipt, and the v5 receipt's
canonical payload.  It never reads the frozen primary as a classifier input.

## 3. Fixture-free self-test

Command:

```text
python3 -B v16/code/apr_paper12_exact.py --selftest
```

Result: exit `0`, `13/13` checks passed, no scientific artifact written.
The self-test witness SHA-256 is
`c72319705d52c67d4fd6ae308bf06f66e1e7cc6f307a577ca5347cfb666703b3`.

The checks are:

1. canonical prefix Boolean identities;
2. a fresh all-depth split constructor;
3. positive complete restriction questions;
4. retained zero port;
5. uniform and adaptive frontier completeness;
6. three tagged graph pushouts;
7. active identity-assignment domain;
8. exact overlap underdetermination;
9. typed capability classification;
10. refusal of a forged mapping in place of a capability object;
11. all fifteen registered controls;
12. transactional rollback after an injected second-publication failure;
13. transactional success.

A true off-tree copy containing only the source and no `.git` produced
byte-identical self-test stdout.

## 4. CLI and publication discipline

The following all refused without creating a target:

| invocation class | exit |
|---|---:|
| no mode | `2` |
| unknown option | `2` |
| self-test with a publication path | `1` |
| run without both destinations | `1` |
| run with relative destinations | `1` |

Publication accepts only distinct, absent, absolute paths whose parent
directories exist.  The injected failure after the first rename removes both
the staged files and the first published file.  Existing targets are never
overwritten.

## 5. Deterministic full replay

The first full run used the source frozen in commit `22ba8a1` and the two
authorized absent destinations.  A second run was made in
`/private/tmp/apr-paper12-run.DB268q`, which contained the same relative
`v16/code` layout and only the authenticated immutable inputs required by the
source.  The copy had no `.git` directory.

Both runs returned:

```text
strict_primary = APR-BLOCKED-AT-BOUNDARY-GLUING
payload_sha256 = 1c6ded1e366cd4e3863a2774285ade5663f80e5228ed4077d0eb5b33bb0286f5
```

The transcript files were byte-identical.  The receipt files were
byte-identical.  Their respective ordinary SHA-256 values are those in
Section 1.

## 6. Independent arithmetic cross-check

A separate standard-library `Fraction` calculation imported no bundle
function.  It independently reproduced:

- contextual volumes `(1/2,1/2)` before and `(1/2,0)` after the meet context;
- uniform frontier sizes `(1,2,4,8)`;
- total dyadic weight `1` for every uniform frontier;
- total dyadic weight `1` for `{0,10,110,111}`;
- `15` vertices and `14` edges in the complete depth-three binary tree;
- identical `AB` and `BC` marginals for the two displayed global laws;
- every marginal cell equal to `1/4`;
- `P(A=C)=(1/2,1)`.

The source independently constructs tagged unions and a union-find quotient
for each of the three pushouts.  Each quotient has the direct tree's exact
node labels and edges, not merely matching counts.

## 7. Capability evidence and precedence

Every classifier input is a frozen `Capability` object with a primitive hash.
A bare mapping is refused.  Capability absences are derived from a constructed
interface inventory and requirement sets; no later gate enters as a literal
absence table.

The first two measured prerequisites pass:

| capability | status | evidence |
|---|---|---|
| normalization | present | all restriction rows positive and complete |
| raw atomlessness | present | zero Boolean failures and nine displayed proper splits |

Boundary gluing is the first missing capability.  Its exact computed missing
interfaces are:

1. adaptive-frontier factory;
2. identities at every active boundary;
3. filling-to-process assignment;
4. tensor-process factory;
5. nontrivial vertical-horizontal naturality;
6. regional-overlap selector.

The finite graph pushouts are separately present and do not set the process
coordinate.  The classifier therefore returns
`APR-BLOCKED-AT-BOUNDARY-GLUING`.  Deleting normalization moves the result
earlier to `APR-INCONSISTENT`; supplying a complete abstract gluing capability
moves it later to `APR-BLOCKED-AT-TWO-ARROW-TYPING`.  This proves that the
registered primary is produced by precedence rather than a terminal literal.

## 8. Registered changed-object controls

All `15/15` controls pass.  Every row carries different canonical before/after
hashes.

| control | licensed conclusion |
|---|---|
| `RAW-ATOMLESS` | a fresh deep cylinder splits properly |
| `ATOMIC-CHARACTER` | an operational image of raw syntax can be atomic |
| `VOLUME-NONCONGRUENCE` | scalar-volume equality is not a Boolean congruence |
| `ZERO-PORT` | dropping a zero branch changes the instrument type |
| `AVERAGE-BRANCHES` | averaging produces `I/2`, not `I` |
| `FRESH-PROBE` | a depth whitelist is not a complete compiler |
| `ADAPTIVE-FRONTIER` | uniform-depth boundaries omit a valid adaptive cover |
| `IDENTITY-DOMAIN` | raw identity-like or replacement graphs do not become active identities |
| `PUSHOUT-NOT-PROCESS` | graph composition cannot promote the process coordinate |
| `CACHED-MARGINAL` | a global mutation exposes stale cached regional shadows |
| `ARBITRARY-SELECTOR` | selecting one completion adds law data |
| `SYNTHETIC-LAW-EXCLUSION` | generic executable-law plumbing supplies no physical baseline |
| `RAW-NODE-ONTOLOGY` | neutral node relabeling moves no physical coordinate |
| `PRIMARY-PRECEDENCE` | earlier and later classifier movement is reachable |
| `ANCHOR-FAILURE` | an immutable-input mismatch refuses before science |

## 9. Paper-to-receipt map

| paper statement | receipt key or proof |
|---|---|
| zero registered Boolean failures | `paper_numbers.boolean_failure_count` |
| nine displayed proper splits | `paper_numbers.raw_split_count` |
| all-depth raw atomlessness | in-paper Theorem 1 proof plus generic split constructor |
| `(1/2,1/2)` and `(1/2,0)` volume control | `paper_numbers.volume_before`, `volume_after_meet` |
| atomic image size `2` | `paper_numbers.atomic_image_size` |
| positive complete restriction instrument | `questions.rows`, Theorem 2 proof |
| frontier sizes `1,2,4,8` | `paper_numbers.uniform_frontier_sizes` |
| adaptive frontier `{0,10,110,111}` | `paper_numbers.adaptive_frontier` |
| tree counts `15/14` | `paper_numbers.direct_tree_counts` |
| three exact pushouts | `paper_numbers.pushout_count`, `boundaries.pushouts` |
| all `AB` and `BC` masses `1/4` | `paper_numbers.AB_cells`, `BC_cells` |
| `P(A=C)=1/2` and `1` | `paper_numbers.p_a_equals_c` |
| blocked at boundary gluing | `strict_primary`, `strict_primary_walls` |
| fifteen controls pass | `controls`, `paper_numbers.control_count` |

No displayed scientific number lacks either a receipt key or an explicit
paper proof.

## 10. Scientific and ontology audit

The candidate's title, abstract, conclusion, tables, and captions remain
negative at the measured scope.  It distinguishes:

- presentation regions from physical regions;
- raw atomlessness from post-quotient atomlessness;
- restriction conditioning from regional rewrite;
- graph pushout from process composition;
- simultaneous `AB/BC` gluing from transition dynamics;
- one-law dataflow plumbing from a physical indivisible law;
- a candidate actual history from a derived actualization mechanism;
- representation objects from ontology.

The exact coordinates are:

```text
atomlessness = SYNTAX-ONLY
process = STATIC-RESPONSE-ONLY
ontology_role = STATIC-RESPONSE
physical_regional_referent = UNCONSTRUCTED
regional_congruence = UNCONSTRUCTED
one_law_provenance = UNCONSTRUCTED
locality = UNCONSTRUCTED-PROMOTION-FAILURE
contact = PRICED
causality = PRICED
law_selection = UNSELECTED
actualization = POSTULATED-NOT-DERIVED
```

The paper makes no metric, curvature, gravity, continuum, GR, QFT, particle,
Hamiltonian, vacuum, constant, or empirical-prediction claim.

## 11. Successor discipline

The candidate incorporates the methodological correction without constructing
the successor.  It states that a future positive investigation must first
freeze one explicit parameterized `Gamma_lambda` family.  Candidate memory is
not called a record before same-law recovery, and raw relational structure is
not called geometry before calibrated readings are generated and consumed.

This statement changes no Paper 12 coordinate.  No physical `Gamma`, new
fixture, metric, curvature, or gravity object appears in the source, receipt,
or paper.  A successor remains separately pinned and unauthorized until Paper
12 is terminal.

## 12. Candidate disposition

The exact bundle and candidate satisfy the construction pin.  Their status is
**GREEN — CANDIDATE UNREVIEWED**.

The next lawful step is to freeze a hostile-review protocol, then commission
three mutually blind reviews.  This verification note cannot substitute for
that review.
