# External hostile review — final RQ0-L0 certification cycle

## Verdict

\[
\boxed{\texttt{ACCEPT INVALID DELIVERY WITH DOCUMENTATION FIXES}}
\]

The committed outcome is correctly classified as:

\[
\boxed{\texttt{RQ0-L0-INVALID}}
\]

with scientific outcome `null`.

The timeout is not evidence for or against independently operable address factors. Therefore neither a positive L0 rung nor `RQ0-L0-BLOCKED-AT-ADDRESS` is warranted.

The documentation fixes below should be applied only as scope corrections in adjudication. The registered stopping rule forbids modifying the estimator, shrinking or replacing the fixture, or opening another scoring cycle.

## Independent audit results

### Git chronology and immutability

Verified:

- `4366531` is an ancestor of `3b9d88a`.
- `3b9d88a` is an ancestor of `56baf60`.
- All five delivery paths were absent at estimator freeze:
  - fixture;
  - scorer;
  - text receipt;
  - JSON receipt;
  - delivery note.
- The estimator and proof blobs are identical between freeze and delivery.
- SHA-256 values independently reproduced:
  - estimator: `c1d3c3b36df71ed80b9ca9152be3d5a97f4d4c1c88ab9f3b0defd360ed14a5c3`;
  - soundness proof: `acb1ccbcf893f26424bc2868af9354fe9cb3d038ff18917c3602f9c32775ec1d`;
  - public receipt: `3a6dcbc2ba51a0583a8818f7a59f549dc7d263e92762d52c28ffe92ac051839b`;
  - fixture: `b2901029d8533af2b90aa5eddbff6ed583c218bec8476a9dd55dc116ed581b14`;
  - scorer: `2fab9d403d7f740206e2a8c5cf4287cfb98cd5709257c82fd4b19db565f461a0`;
  - JSON receipt: `c3dfe72c199dd9036f3e4966035805a89d80713a6b788d32451d03fbe589e852`;
  - text receipt: `ce5c3bedd42a188bd12f409f55ea01f9e476fd9baae69e0e9dac6f066398cb8b`.
- The post-delivery hostile-dispatch commit changes only `RUNBOOK.md` and `v13/LOG.md`; no estimator, fixture, or scorer modification followed truth opening.

The stopping rule was obeyed.

### Public estimator suite

The frozen public suite independently reran byte-for-byte identically:

\[
29/29.
\]

The hostile `S_3\times C_2` selectability result was also independently rebuilt without the estimator:

- with all classes selectable, the order-six and order-two factors are independently generated;
- when the nontrivial `C_2` coset is composite-only, the candidate `C_2` factor’s selectable closure has order one, not two;
- the composite-only factor is therefore correctly rejected.

The declared-collapse and genuine multiplication-collision controls are distinct. The latter gives two different tuples mapping to the same result.

The address-factor soundness argument is coherent at its declared scope. I found no counterexample to the conditional P1–P8 theorem or to completeness for at most eight commuting normal direct factors within the registered finite caps. This does not establish anything about arbitrary quantum subsystem notions.

### New fixture

The post-freeze fixture is genuinely new.

I independently rebuilt the stated composition law and exhaustively checked:

- group order: `192`;
- identity;
- associativity on all \(192^3=7{,}077{,}888\) triples;
- intended factor orders: `(2,3,4,8)`;
- independently selectable closures: `(2,3,4,8)`;
- all six pairwise factor intersections have order one.

It cannot be an encoding or relabelling of `S3^3`, whose order is 216.

The serialized fixture independently regenerated:

- 192 operations;
- 36,864 complete ordered rows;
- carrier dimension 32;
- six independently selectable classes;
- five contexts;
- four record candidates;
- serialized-input SHA-256 `759d7c0ac774943cf220526751b54d9c5aaa8dcfd4ef98b344758a09cf61d322`.

An independent row checker verified all 36,864 rows separately for:

- boundary/context type;
- implemented status;
- result-class membership;
- supplied-law presence and dimension;
- exact equality with physical amplitude composition;
- gauge agreement with the result representative;
- operational-signature agreement.

All four fresh record witnesses separately pass the W3 preserve/erase/no-write decision procedure. This remains fixture-construction evidence, not a recovered regional atlas.

The hidden five-context meet calculation is internally consistent: nine intended nonempty meets, eight nonempty pair instances, three nonvacuous triple instances, and empty universal intersection. These remain held-out intended facts because the estimator never returned them.

### Bounded timing audit

I did not initiate another 360-second score.

Two shorter hostile reproductions were performed:

- a 45-second capped worker run built `192/36864/32` and did not return from address analysis;
- a separate 20-second stack capture found execution inside exact represented-algebra construction called by `certify_factor_tuple`.

This independently corroborates the committed slow path and the note’s stated code location. It does not independently reproduce a full 360-second timeout and is not promoted as a partial scientific result.

## Ranked findings

### F1 — MAJOR — the scorer is fail-closed on the observed timeout branch, but not a complete or total outcome resolver

The worker in `rq0_l0_certification.py:82–111` stops after `analyze_addressability`. It never invokes:

- regional-atlas construction;
- `RegAddr`;
- `FactIface` or `Rec`;
- main gauge/phase comparisons;
- main mutants;
- positive receipt regeneration.

Therefore “complete main pipeline” is too broad. More precisely, the addressability stage exhausted the complete official time budget before returning, so downstream stages were unreachable.

There is also a latent success-branch defect. If the worker returned zero, lines 197–201 would emit:

- status `UNEXPECTED-RETURN`;
- procedural outcome `None`;
- scientific outcome `None`;

and line 324 would exit zero. Under the pin, a returned run with no resolved outcome should itself be `RQ0-L0-INVALID` and exit one.

This latent branch did not execute and cannot invalidate the observed timeout classification. It does mean the scorer should only be described as fail-closed for the branch actually exercised.

Replacement adjudication wording:

> The official scorer failed closed on the observed timeout branch and suppressed every scientific outcome. Its unexercised return branch is not a complete outcome resolver and supports no general fail-closed claim.

### F2 — MAJOR — the public `RegAddr` calibration is weaker than the strict pinned arrow type

`RegionalArrow.row_map` carries row endpoints, source/target statuses, and source/target laws. It does not carry:

- row context `tau`;
- explicit source and target result classes;
- observed row signatures.

The result square is checked during construction, but the result data are not part of the returned arrow. The context map is a pair of structural hashes rather than an executable map of a complete context object.

Thus the public calibration supports substantial regional restriction machinery, but not the claim that every complete composition-row field is carried by the arrow exactly as pinned.

This does not affect the invalid main outcome because no main `RegAddr` object was returned.

Replacement adjudication wording:

> Public calibration establishes operation projection, implemented-row law/status compatibility, result-square commutation, selectability and structural field lifts. It does not instantiate the pin’s complete row-arrow type carrying `tau`, explicit results and observed signatures.

### F3 — MAJOR — the public twisted-triple pair validity is syntactic rather than a full instrument-isomorphism test

`_typed_pair_isomorphism_valid` checks mainly:

- that each declared field contains one entry;
- selectability flags;
- carrier dimension;
- the two-atom projector permutation.

It does not validate those maps against actual regional objects, composition rows, amplitude laws, preparations, contexts, record dynamics, or gauge actions.

The constructed loop genuinely has identity-by-identity disagreeing with a direct swap, but “all three pairwise regional maps are full typed isomorphisms” is too strong.

Again, this weakens only surviving calibration wording. No main triple-descent claim exists.

Replacement adjudication wording:

> The public control is a typed two-atom loop-holonomy calibration with individually bijective presentation maps; it is not an independently reconstructed triple of full amplitude-instrument isomorphisms.

### F4 — MINOR — provenance checks are partly recorded rather than authenticated

The scorer computes the proof hash but does not compare it with a frozen expected value. It authenticates the estimator hash, not the proof hash.

It checks absence of the fixture and scorer at freeze, but not all five delivery paths. The complete five-path absence was verified in this hostile review.

Receipt gate `R09` reads the fixture’s own Boolean declaration `old_s3_cubed_imported=False`; that gate is circular. The non-`S3^3` result is nevertheless independently secure because:

- the estimator has no fixture import or prohibited old constructor;
- the new group has order 192 rather than 216;
- its exact law and factor orders were independently rebuilt.

Replacement wording:

> The scorer records the proof hash and authenticates the frozen estimator plus two path absences. Full five-path chronology, proof-byte identity and non-`S3^3` status were established separately by hostile review.

### F5 — MINOR — only one full timeout is represented in the canonical receipt

The JSON receipt directly represents the official timeout. The earlier irreversible 360-second attempt is recorded narratively in the note and ledger, not by a separate canonical runtime artifact.

The independent bounded audit corroborates the same slow code path but does not establish a second 360-second measurement.

This does not change the outcome: one official cap exhaustion is sufficient for `RQ0-L0-INVALID`.

Replacement wording:

> One canonical official run records the 360-second timeout. A prior attempt is contemporaneously reported, and hostile bounded sampling independently corroborates the same represented-algebra bottleneck.

## Evidence that survives

The following evidence survives hostile review:

- correct Git chronology and estimator immutability;
- all future delivery paths absent at freeze;
- exact conditional address-factor soundness/completeness within the declared finite class;
- byte-identical public 29/29 output;
- independently enforced selectability and the hostile composite-only rejection;
- separate declared-collapse and true-collision controls;
- exact handle-invariant public fact diagrams under full record-handle renaming;
- a record-bearing public ambiguity calibration, with its full-instrument scope kept narrow;
- successful construction of a genuinely new 192-class heterogeneous fixture;
- exact validation of every one of its 36,864 supplied rows;
- four fresh W3 record seams;
- the observed runtime bottleneck;
- complete suppression of scientific outcomes.

## Unearned claims

The following are unearned:

- recovered main factor orders `(2,3,4,8)`;
- a main factor certificate;
- a main localization groupoid;
- a main regional atlas;
- main `RegAddr` or `Rec`;
- main triple descent;
- main gauge, phase, handle, map or projector mutants;
- deterministic positive receipt regeneration;
- `RQ0-L0-BLOCKED-AT-ADDRESS`;
- any terminal positive L0 status;
- topology, influence, causality, spacetime, fields, or gravity.

The intended factor and atlas values are legitimate hidden fixture truth only.

## Final adjudicative recommendation

The one-shot construction cycle is closed under its registered stopping rule. No estimator optimization, fixture shrinkage, replacement fixture, hidden rescore, or automatic retry is authorized.

The correct scientific status remains:

\[
\boxed{\text{no scientific RQ0-L0 verdict}}
\]

and the correct procedural status remains:

\[
\boxed{\texttt{RQ0-L0-INVALID}}
\]

No terminal scientific L0 status is warranted. `RQ0-T1` and `RQ0-C1` remain prohibited.
