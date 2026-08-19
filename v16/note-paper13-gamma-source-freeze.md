# Paper 13 ONE-GAMMA Stage-A source freeze

Status: **SOURCE-FROZEN / DEVELOPMENT-ONLY / RESULT-NEUTRAL**

This note records the Stage-A development freeze required by
`v16/note-paper13-one-gamma-construction-pin.md`.  It is not an official
Paper 13 scientific result, does not award a rung on the outcome ladder, and
does not authorize a paper draft.  Stage B must use the exact committed source
bytes recorded here; any later source edit invalidates this freeze cycle.

## Binding and scope

- Base commit: `83da0f950659bf062b92edb2c5c090ece3fa21a2`.
- Construction pin SHA-256:
  `4b2c6f305430dffa329758e81cf82dd295800359b808136cae9c5f8ca3b94c35`.
- RUNBOOK SHA-256:
  `5629dd083da923e216143c249ce0246da3238ddb9475bd6d67954ce0aa8aac58`.
- Methodology/ontology gate SHA-256:
  `06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51`.
- Authoritative Stage-A source: `v16/code/p13_gamma_exact.py`.
- Source SHA-256:
  `c699fc0316295e230c2cd0ef50601f631b195ad2237bebc2c42a75a2163f1aaf`.
- Source size: 303,528 bytes and 7,792 logical lines as reported by the
  evaluator's own development payload and independently by filesystem tools.
- Python used for the recorded development executions:
  `/opt/homebrew/bin/python3.13`, with bytecode writing disabled.

Only the Stage-A source and this freeze note were authorized task outputs.
No private exploratory Paper 13 file, APR scorer, APR fixture, or APR receipt
conclusion was imported or used as physics.  The evaluator is self-contained
and uses Python standard-library exact arithmetic, principally
`fractions.Fraction`.

## Development self-test evidence

The current source completed the fixture-denied `--selftest` path.  This is
permanently exposed advisory development evidence, not Stage-B confirmation.

- Status: `PASS`.
- Checks: 36 registered, 36 passed.
- Mutations: 81 registered, 81 executed, 81 killed.
- Mutation registry SHA-256:
  `1607b2888b2d25eacedf0fa1f0f1e6ce927937abd6aca915165a6de697a3c077`.
- Normalized self-test payload SHA-256:
  `d2ab9fef21119c769418697349e619130f850b58260539280d6f08596ce38b76`.
- Serialized stdout SHA-256:
  `a217f96d3d8bb92c214a4235ed7ac3e7a9c5a954557a01820176f489c778c6a2`.
- Serialized stdout size: 26,134,100 bytes, one canonical-JSON line.
- Separation fields: `scientific_fixture_evaluated:false`,
  `fresh_cases_read:false`, `official_artifacts_read:false`, and
  `publication_writes:0`.

The exact check names, in emitted order, were:

1. `AST-AND-STATIC-SOURCE-CLEAN`
2. `FRACTION-ONLY-SCIENTIFIC-COORDINATES`
3. `ESSENTIAL-SUPPORT-BOOLEAN-QUOTIENT`
4. `PUBLIC-PRIMITIVE-LANGUAGE-CLOSED`
5. `FOUR-PRIMITIVE-LEGS-ON-FULL-TYPED-CHAIN`
6. `ZERO-AMPLITUDE-TARGETS-RETAINED`
7. `COHERENT-R-B-C-EXACT`
8. `CATEGORY-IDENTITY-COMPOSE-TENSOR-SYMMETRY`
9. `TOTAL-NORMALIZED-PRIMITIVE-DOMAIN`
10. `COMPLETE-SOURCE-KEY-SUFFICIENCY`
11. `NEUTRAL-PRESENTATION-INVARIANCE`
12. `SOURCE-GROUPOID-COVARIANCE`
13. `ONE-PRIMITIVE-ROOT-LINEAGE`
14. `ACTIVE-SUPPORT-CHANGE-AND-INVERSE-MERGE`
15. `RECIPROCAL-SAME-LAW-READER`
16. `WRITER-ALL-INPUT-NORMALIZATION`
17. `ACTIVE-TO-CARRIED-GENERATOR-INTERTWINING`
18. `ALL-WORD-CONTINUATION-RECOVERY`
19. `ALTERNATE-RECORD-CUT-EXACT`
20. `REACTIVATED-CARRIED-PORT-ERASES-RECORD`
21. `NATIVE-NONDIVISION-NEGATIVE-FACTOR`
22. `RATIONAL-INTERVAL-CERTIFICATE`
23. `HISTORY-CONDITIONED-POSITIVE-CONTROL`
24. `BLIND-RESOURCE-PARITY-AND-INDUCTION`
25. `SAME-ROOT-MATCHING-RESPONSE-SEPARATION`
26. `EXACT-SCOPE-COORDINATES-AND-WALLS`
27. `ORDERED-MEASUREMENT-PROGRAMME`
28. `OUTCOME-LADDER-CAP-AND-INDEPENDENT-COMPARATOR`
29. `MUTANT-REGISTRY-UNIQUE-AND-COMPLETE`
30. `ALL-REGISTERED-MUTATIONS-KILLED`
31. `SYNTHETIC-ANCHOR-CORRUPTION-IS-INTEGRITY-ONLY`
32. `STRICT-CLI-FORMS-AND-REFUSALS`
33. `READ-LEDGER-ORDER-AND-ANCHOR-BINDING`
34. `SEAL-MANIFEST-TOTALITY-RECOMPUTED`
35. `STAGE-WHITELIST-EXACT`
36. `FIXTURE-AND-OFFICIAL-ARTIFACT-SEPARATION`

The 81 attacks are the exact source-declared registry, grouped as 8 boundary,
20 public-language/type, 1 post-init law identity, 4 presentation/source-key,
4 lineage, 8 primitive-law, 8 output/shadow, 5 record, 8 metadata/blinding,
10 scope, 3 static/integrity/outcome, and 2 groupoid attacks.  Every emitted
row contains the complete canonical old/new primitive bytes, changed path,
affected claim, evidence and evidence hash, recomputed evidence object,
outcome drop, and kill predicate.  Two strict single-mutant CLI spot checks
also passed:

- `FORGED-UNIT-CONTEXT`, stdout SHA-256
  `dbc5469e6427a8a34495ea52374b5b0cc70426fea6cf87ace284cffdc080e085`.
- `RESET-WRITER-CHAIN`, stdout SHA-256
  `c7cb74eebf7a498dc76ec4158244290bfaf3f3e331534076abc1fb7fc3f6d6a6`.

## Determinism and isolation replay

Three executions of the same source bytes produced exactly the same
26,134,100-byte stdout and both hashes recorded above:

| execution | source placement | working directory | wall time |
|---|---|---|---:|
| repository root | repository source | repository root | 23.42 s |
| alien CWD | repository source by absolute path | private alien directory | 21.27 s |
| true off-tree | source-only copied tree with no `.git` | separate private alien directory | 21.75 s |

The off-tree source copy independently hashed to the authoritative source hash.
Its source-only tree contained no `.git`, `__pycache__`, or `.pyc` path.  The
repository-root, alien-CWD, and off-tree payloads each reported 36/36 checks,
81/81 mutation kills, identical registry and normalized payload hashes, and
the same fixture/fresh/artifact/publication separation fields.

## Static and artifact audit

Independent AST parsing passed.  The evaluator's source scan reported:

- zero float-literal nodes;
- zero forbidden scientific calls;
- zero forbidden imports;
- zero Git-query literals;
- zero expected-answer-table names;
- exact visitation of all 17 registered public primitive-language types;
- complete referent census, full typed target catalogues, and retained zero
  targets;
- a recomputed total seal manifest and exact Stage-A/Stage-B path whitelist.

The source imports only Python standard-library modules.  Development runs
used `-B`; no `p13_gamma_exact` bytecode artifact remains in the repository
(unrelated pre-existing cache files were not touched).

At freeze time all official or result-known paths were absent:

- `v16/code/p13_gamma_fresh_cases.json`
- `v16/code/p13_gamma_output.txt`
- `v16/code/p13_gamma_receipt.json`
- `v16/note-paper13-gamma-verification.md`
- `v16/paper-13-one-relational-gamma.md`

Neither `--generate-fresh` nor official `--run` was invoked.  No fresh nonce or
fresh case was generated, selected, inspected, or published.  The only next
scientific event, after an authoritative commit of these frozen source bytes,
is the separately authorized Stage-B protocol using one mutually blind nonce.
