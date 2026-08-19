# Paper 12 hostile review — Seat R

## 1. Seat identity and mutual blindness

I am **Seat R**, assigned regional algebra, questions, quotient, and
refinement. I followed the hostile-review protocol at commit
`6ee3588f0f12488f257a5b93950676a55cb4b3e4`, ordinary SHA-256
`8fcc47af49b99e0781c41a2ee1f8b326853bad13b127aa52d3b8f64c5f4a197f`.

I did not read, list, request, receive, or infer either other Paper 12 report
or either other seat's scratch. I did not communicate with another review
seat. Candidate prose, the transcript, the receipt, and the candidate
verification conclusions were treated as claims or audit targets, never as
scientific predicates. No candidate function was imported or called.

## 2. Complete read set and authentication

Authentication preceded scientific work. Ordinary hashes were:

| Role | Path | SHA-256 | Result |
|---|---|---|---|
| protocol | `v16/note-apr-paper12-hostile-review-protocol.md` | `8fcc47af49b99e0781c41a2ee1f8b326853bad13b127aa52d3b8f64c5f4a197f` | match |
| ONE-GAMMA gate | `v16/note-apr-one-gamma-paper-review-gate.md` | `06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51` | match |
| construction pin | `v16/note-apr-paper12-negative-candidate-pin.md` | `6341a1184426f3a6be0ad619d9f02340124a76e5484bb94609462d5d765a6ebd` | match |
| exact source | `v16/code/apr_paper12_exact.py` | `c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7` | match |
| transcript | `v16/code/apr_paper12_output.txt` | `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f` | match |
| receipt | `v16/code/apr_paper12_receipt.json` | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` | match |
| scientific candidate | `v16/paper-12-atomless-regions-and-the-missing-gluing-law.md` | `cdb212c57c8b80099f9fc17eb0b1c5ed90c38ae2f5db7c50eb3038eb893f4de8` | match |
| candidate verification | `v16/note-apr-paper12-candidate-verification.md` | `0ee0e22879f2c1d086f8ca13d53bed4fc6f5261301865674d2d4368cec136e70` | match |
| publication dependency | `v16/note-apr-v5-verification.md` | `d2eae0fdc187317d7ee39c8efaca8fa2a94b6b8f06a3a0524cee0289396a077d` | match |
| publication dependency | `v16/apr_output_v5.txt` | `68374ea18576466ccc40553f8b221360fdfce3fc43d5b555a6eeb0d2827a2f56` | match |
| publication dependency | `v16/apr_receipt_v5.json` | `ab9ea941fceebf5b57c7955d483730f3a5f0b317bb5a21da9cc0820331919a61` | match |

Removing `payload_sha256` and independently canonicalizing the Paper 12
receipt gave
`1c6ded1e366cd4e3863a2774285ade5663f80e5228ed4077d0eb5b33bb0286f5`.
The same independent operation on the required v5 receipt gave
`04a1e370c601f9d7e3d5310f9bf20296d7be5c5428010f0f7af6c073d0b438d8`.
The Paper 12 receipt's transcript hash matched the ordinary transcript hash.
There was no integrity mismatch.

## 3. Replays, return codes, and artifact hashes

The frozen source was always executed as a subprocess with `python3 -B`.

| Replay | Command form | RC | Result |
|---|---|---:|---|
| repository self-test | `python3 -B v16/code/apr_paper12_exact.py --selftest` | 0 | 13/13; witness `c72319705d52c67d4fd6ae308bf06f66e1e7cc6f307a577ca5347cfb666703b3` |
| alien-CWD self-test | absolute repository source path, run from private alien directory | 0 | byte-identical stdout |
| true off-tree self-test | source-only/no-`.git` copy, run from `/private/tmp` | 0 | byte-identical stdout |

All three self-test stdout streams had SHA-256
`fa3ad97c3f03181350c573c753d1369b3a90d477f71ac757e48b7300db8a6454`.
The off-tree tree contained only the authenticated source and its four
authenticated required inputs and had no `.git` directory.

Three full publications were made to distinct absent private paths: from the
repository root, from an alien CWD using the repository source, and from the
true off-tree copy. Each returned RC 0 and
`APR-BLOCKED-AT-BOUNDARY-GLUING`. Each output had SHA-256
`7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f`;
each receipt had SHA-256
`d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39`.
All six generated files were byte-identical to their frozen counterparts.

Strict CLI results were:

| Case | RC | Files created |
|---|---:|---:|
| no mode | 2 | 0 |
| unknown option after `--selftest` | 2 | 0 |
| self-test with publication path | 1 | 0 |
| run with one destination missing | 1 | 0 |
| relative destinations | 1 | 0 |
| lexically distinct but resolved-alias destinations | 1 | 0 |
| missing parent | 1 | 0 |
| existing output plus absent receipt | 1 | 0 new; existing output unchanged |

For an independent anchor-failure replay, I changed one byte in a private
off-tree gate copy. The full run returned RC 1 before publication and created
neither destination. For an independent rollback replay, I changed only the
private source's main publication call to inject `fail_after_first=True`.
That source had SHA-256
`bec23e4555fd86e06cb8e0540bea4a3b36b3ee6dbeb757c245d8ed4f52eb88a3`;
it returned RC 1 after the injected first rename and left neither output nor
receipt.

The AST contained 68 top-level nodes, 41 top-level functions, four classes,
and zero float literals. Imports were standard library only. Static searches
found no randomness, network, subprocess, Git, runtime-CWD, tolerance,
scorer, or fixture dependency; the two scorer/fixture strings were negative
declarations, not imports. `classify_capabilities` requires typed
`Capability` instances and refuses a bare mapping. The source reads expected
input hashes only for authentication, not to choose a scientific metric.
Scoped Git-diff checks and repeated corpus hashes confirmed no repository
write from any replay.

The paper had no repository, commit, version, pin, receipt, scorer, fixture,
task, reviewer, or review-history prose. The phrases “unit region” and
“ontology ledger” are scientific uses, not internal workflow references.

## 4. Independent reconstruction method

Private scratch lived off-tree at
`/private/tmp/apr-paper12-seat-r.ddDfXl/seat_r_reconstruct.py`. Its ordinary
SHA-256 is
`4df50f9a02666021a3d15f4e66972aec28590158ae57a0ecb5ae0f2217032911`.
It imported only the Python standard library, used `Fraction` and integers,
and imported no candidate module. It implemented separate prefix-antichain,
matrix, tagged-pushout, marginalization, valuation-transport, and typed-gate
data structures. Its run returned RC 0, status `PASS`, and witness SHA-256
`e75a7b752727715f619197d775437f2946d61879e7c601187732e516e2c196d3`.

The script checked all 256 depth-three clopen elements as a finite
falsification attempt, then used the all-depth split constructor as the
analytical proof. It checked the registered Boolean family, the character
laws, exact restriction matrices through depth five, affine mixtures,
frontiers, three tagged pushouts, the B0-only assignment, both global laws,
fresh marginalization, and classifier movement. The physical quotient and
process absences were audited separately from the raw theorem.

The exact source's primitive scientific domain was searched by AST and source
inspection: it contains `Region`, `Segment`, `UnionFind`, `Capability`, static
restriction matrices, tree/graph constructors, and two finite global
distributions. It contains no physical `Gamma` evaluator, no jointly typed
`(C_pres,G,C,B,Div,Gamma)`, no complete-context quotient, and no
filling-to-process assignment. Occurrences of `Gamma`, records, comparison,
and locality in the source are missing-interface names or `UNCONSTRUCTED`
scope strings. This names both the searched interface and its domain; it is
not an inference from prose silence.

## 5. Claim-by-claim evidence

| Paper locus and claim | Independent evidence | Grade | Disposition |
|---|---|---|---|
| Abstract; finite prefix-cylinder unions form an atomless Boolean algebra | General split proof in Section 6 below | `ANALYTICAL-PROOF` | survives for presentation syntax |
| Abstract; positive finitely additive valuations support a complete two-port restriction instrument | General indicator/finite-additivity proof | `ANALYTICAL-PROOF` | survives as static conditioning |
| Abstract; three displayed tree factorizations are genuine pushouts | Three separately tagged quotients reproduced exact nodes and edges | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives as finite graph composition |
| Abstract and Sections 6–7; two `ABC` laws share `AB/BC` but differ on `A=C` | Exact fresh marginalization: every pair cell `1/4`; `P(A=C)=1/2,1` | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives |
| Abstract and Section 7; earliest result is blocked at boundary gluing | Typed-gate reconstruction moved earlier/later under registered mutations | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives |
| Abstract; physical quotient, horizontal process, locality, and `Gamma` are absent | Complete source-interface search named above | `UNCONSTRUCTED` | correctly negative |
| Sections 1–2; presentation regions are not physical regions | No faithful process/context quotient exists in the primitive domain | `UNCONSTRUCTED` | distinction is necessary and preserved |
| Section 2; antichain reduction canonically represents the finite algebra | Independent normalization and Boolean identities had zero failures | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives |
| Section 2; “point-free” is limited to algebraic presentation, not a physical ontology | Abstract Boolean operations need no primitive point labels; paths remain explanatory semantics | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | adequately qualified |
| Theorem 1; every nonzero presentation element splits | Choose an antichain word `w`; `C(w0)` and the remainder are disjoint, nonzero, and rejoin | `ANALYTICAL-PROOF` | survives all depth |
| Section 3; nine displayed splits | Independently reconstructed nine proper registered splits | `FINITE-CONTROL-ONLY` | consistent with, but not proof of, the theorem |
| Section 3; scalar-volume equality is not meet congruence | `mu(C0)=mu(C1)=1/2`, while meeting with `C0` gives `1/2,0` | `ANALYTICAL-PROOF` | survives |
| Section 3; all-zero evaluation is a Boolean character with atomic image | Complement, meet, and join laws proved; image is `{0,1}` | `ANALYTICAL-PROOF` | survives; receipt pass field was not used |
| Section 3; raw atomlessness does not imply quotient atomlessness | Quotient by equal character has atomic two-element image | `ANALYTICAL-PROOF` | survives |
| Theorem 2; branches are positive and affine | Diagonal characteristic restriction preserves the positive cone and affine combinations | `ANALYTICAL-PROOF` | survives all finite atom depths |
| Theorem 2; `Q1+Q0=I` and zero port retained | Pointwise `1_C+1_notC=1`; exact matrices and zero matrix reproduced | `ANALYTICAL-PROOF` | survives |
| Section 4; averaging gives `I/2`, not `I` | Exact matrix scaling | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives |
| Section 4; restriction does not write a record, create a region, or define a division | No writer, reader, continuation grammar, rewrite, or `Div` primitive exists | `UNCONSTRUCTED` | correctly scoped |
| Section 5; uniform frontiers and `{0,10,110,111}` are complete | Prefix-free tests and dyadic sums exactly equal one | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives |
| Section 5; the displayed adaptive set is the “smallest” reminder | `{0,10,11}` is prefix-free, nonuniform, complete, and has only three leaves | `REFUTED` | editorial repair required; no theorem changes |
| Section 5; full tree has `15/14` and all three tagged pushouts equal it | Independent tagged quotient, not a count-only union | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives |
| Section 5; only B0 has an active identity in the assignment | Exact census `B0={empty}`, `B1=B2=B3=empty` | `FINITE-CONTROL-ONLY` | survives only for the displayed assignment |
| Sections 5 and 7; no filling assignment, tensor, or naturality is constructed | Complete source-interface search | `UNCONSTRUCTED` | correctly blocks process promotion |
| Theorem 3; local shadows do not determine the global law | Two explicit normalized positive countermodels | `ANALYTICAL-PROOF` | survives |
| Section 6; Markov, entropy, sparsity, order, or hash selection adds law data | Equal local input admits at least two outputs, so no function of those shadows alone is fixed | `ANALYTICAL-PROOF` | survives |
| Section 6; the table is simultaneous gluing, not dynamics or a classical fundamental law | Variables have only regional labels; no transition type or division is present | `FINITE-CONTROL-ONLY` | correctly narrowed |
| Section 8; indivisibility was not operationalized | No jointly instantiated ONE-GAMMA primitive or shadow derivations exist | `UNCONSTRUCTED` | correct negative diagnosis |
| Section 8; a future `Gamma_lambda` programme is a requirement, not a result | No such family appears in source or artifacts | `UNCONSTRUCTED` | successor wording does not promote it |
| Section 9 ledger; physical region, record, `Gamma`, geometry, and actualization remain absent/postulated | Primitive inventory and fresh quotient/relabeling controls | `UNCONSTRUCTED` | ledger does not overclaim |
| Section 10 established list | Each finite or analytical item above reconstructed at its stated scope | `INDEPENDENT-EXACT-RECONSTRUCTION` | survives except the word “smallest” |
| Section 10 nonclaim list | No corresponding typed primitive/evaluator was found | `UNCONSTRUCTED` | complete within Seat R's searched domain |

## 6. Analytical proofs used

1. **Canonical Boolean algebra.** Expand two finite antichains to any common
   depth. Union, intersection, and set complement of the finite leaf sets are
   independent of further refinement; sibling reduction returns the unique
   minimal prefix antichain. The registered Boolean identities follow, and
   the same construction is all-depth rather than a depth-three census.

2. **Raw atomlessness.** For nonzero reduced antichain `A`, choose `w in A`.
   `C(w0)` is nonzero and below `A`; `C(w1)` lies in `A`, is nonzero and
   disjoint, so `C(w0)` is proper. This defeated every attempted edge case,
   including the unit and multi-cylinder presentations.

3. **Character and atomic quotient.** Membership of the all-zero path
   commutes with union, intersection, and complement, hence is a Boolean
   homomorphism `chi:B->2`. Its image is the two-element algebra. The raw
   split `1=C(0) join C(1)` maps to `1=1 join 0`, so the image of the unit is
   an atom: proper raw splitting did not descend.

4. **Volume noncongruence.** Equal dyadic values for `C(0)` and `C(1)` become
   unequal after the common meet context `C(0)`. Therefore equality of the
   scalar alone is not compatible with meet and is not a Boolean congruence.

5. **Restriction instrument.** On every common atom basis, `Q_C^1` and
   `Q_C^0` are diagonal multiplication by complementary `0/1` indicators.
   They preserve nonnegativity and affine combinations, and their sum is the
   identity pointwise. A zero diagonal branch remains a typed operator.

6. **Global underdetermination.** Direct marginalization of the uniform and
   `A=C` distributions gives four `1/4` cells in both `AB` and `BC`, while the
   equality event has weights `1/2` and `1`. Thus the restriction map is not
   injective; selecting an inverse requires extra data.

7. **Relabeling covariance.** Swapping `0` and `1` in every word is a Boolean
   automorphism. Transporting a valuation by the inverse automorphism makes
   every restriction response commute with the relabeling. Raw symbols are
   therefore presentation data, not fixed beables.

## 7. Frozen controls and fresh changed objects

### Assigned control reconstruction

| Control | Independently changed/recomputed object | Result | Licensed scope |
|---|---|---|---|
| `RAW-ATOMLESS` | depth-nine cylinder to its two depth-ten children | pass | all-depth proof plus exact witness |
| `VOLUME-NONCONGRUENCE` | unit context to meet-with-`C(0)` | pass | scalar equality is not congruence |
| `ZERO-PORT` | two typed ports to a dropped zero port | pass | dropping changes interface type |
| `ADAPTIVE-FRONTIER` | uniform factory to nonuniform complete code | pass | displayed factory is incomplete |
| `PUSHOUT-NOT-PROCESS` | exact tagged composite with no map assignment | pass | graph composition only |
| `CACHED-MARGINAL` | `P(000)+=1/16`, `P(001)-=1/16` | pass | `AB` fixed, `BC` moves to `5/16,3/16,1/4,1/4` |
| `ARBITRARY-SELECTOR` | two global completions with one local shadow pair | pass | selection is additional law data |
| `SYNTHETIC-LAW-EXCLUSION` | detached synthetic token beside unchanged physical primitive inventory | pass | cannot create a missing physical interface |
| `PRIMARY-PRECEDENCE` | remove normalization; then separately supply abstract boundary package | pass | `APR-INCONSISTENT`, then `APR-BLOCKED-AT-TWO-ARROW-TYPING` |
| `ATOMIC-CHARACTER` | raw algebra to character quotient | pass | image is atomic |
| `FRESH-PROBE` | depth-nine valid target against depth-two whitelist | pass | whitelist is not a complete compiler |

The active B0-only identity, positive branch matrices, all four uniform
frontiers, adaptive frontier, direct `15/14` counts, three tagged pushouts,
and both complete `ABC` objects were also independently rebuilt. Graph
composition and process assignment remained separate coordinates.

### Mandatory fresh changed objects

1. `C(101001011)` is deeper than every registered region and matrix row. It
   split exactly into `C(1010010110)` and `C(1010010111)`.
2. A normalized valuation supported uniformly on `C(0)` assigned zero to the
   nonzero region `C(1)`. It is positive but nonfaithful, and its dark branch
   remained typed.
3. A constant profile collapsed all ten registered regions. An all-zero
   ultrafilter profile had the atomic two-element image. Neither is a
   faithful complete physical future profile.
4. The symbol swap `0<->1`, transported through the supported valuation,
   preserved Boolean operations and every checked response while moving the
   support from `C(0)` to `C(1)`.
5. The quotient `A~B iff chi(A)=chi(B)` took a proper raw split to an atomic
   image, separating raw from post-quotient atomlessness.

The raw-theorem falsification attempt failed: the constructor passed the
finite exhaustive depth-three algebra and the arbitrary depth-nine witness,
and the general proof closes all finite antichains. The separate attempt to
force physical-quotient overclaim succeeded only as a countermodel to any
such promotion; the paper itself already reports that quotient as
unconstructed.

## 8. Findings

**KILL-R-0 — none.** No reproducible K1–K5, K6, K9, K10, or K11 violation
occurs in the candidate's regional claims. No integrity block was found.

**REPAIR-R-1 — remove the unsupported minimality adjective.** Section 5 calls
`{0,10,110,111}` the “smallest” explicit adaptive reminder. The strictly
smaller set `{0,10,11}` is prefix-free, nonuniform, and complete because
`1/2+1/4+1/4=1`. Replace “the smallest explicit reminder” with “an explicit
reminder.” This is editorial and changes no theorem, receipt value,
coordinate, or primary.

**NARROWING-R-1 — raw versus physical atomlessness.** The all-depth theorem is
about the prefix presentation algebra. Physical and post-quotient
atomlessness remain `UNCONSTRUCTED`; the atomic character quotient forbids
automatic descent.

**NARROWING-R-2 — finite probes versus a physical compiler.** The twelve
finite probes separate the registered family, but a constant profile, an
ultrafilter profile, and the fresh depth-nine target show why this does not
construct a target-independent generated physical future grammar.

**NARROWING-R-3 — questions versus dynamics.** Exact `Q1+Q0=I` establishes a
static restriction instrument only. It does not construct a record, lawful
division, regional rewrite, or horizontal process.

**NARROWING-R-4 — graph versus process.** Three genuine pushouts are finite
categorical controls. With no filling-to-map assignment, full identities,
tensor, or naturality, they do not promote the process coordinate.

**NARROWING-R-5 — simultaneous shadows versus law.** The `AB/BC` result is a
nonuniqueness theorem for global completion. It is neither a transition law
nor an indivisibility witness, and it selects no completion.

## 9. Scoped coordinates and recommended primary

| Coordinate | Seat R result |
|---|---|
| normalization | exact positive two-port sum passes |
| raw atomlessness | `SYNTAX-ONLY`; analytical all-depth theorem |
| physical/post-quotient atomlessness | `UNCONSTRUCTED` |
| finite graph gluing | three exact tagged pushouts |
| static response | constructed |
| horizontal process | `STATIC-RESPONSE-ONLY`; filling assignment absent |
| complete future profiles | `UNCONSTRUCTED` |
| Boolean/gluing/process congruence | `UNCONSTRUCTED` |
| comparison and dynamic locality | `UNCONSTRUCTED` |
| causal/contact process | `PRICED`/`UNCONSTRUCTED`, not generated |
| ONE-GAMMA provenance | `GAMMA-UNCONSTRUCTED` |
| law selection | `UNSELECTED` |
| measured ontology role | `STATIC-RESPONSE` |
| candidate ontology | postulated one compatible relational history; not constructed |
| actualization | `POSTULATED-NOT-DERIVED` |

The earliest supported registered primary is
`APR-BLOCKED-AT-BOUNDARY-GLUING`. Normalization and raw atomlessness pass;
the complete boundary/process package is the first absent prerequisite. Later
finite theorems do not override it.

## 10. Ontology, ONE-GAMMA, GR/QFT, and actualization walls

The primitive scientific inputs are prefix antichains, exact valuations and
restriction maps, finite tree/graph presentations, two finite global
distributions, and a typed capability registry. There is no unique
nomological transition root. The ONE-GAMMA audit therefore returns
`GAMMA-UNCONSTRUCTED`. Because the candidate makes no positive `Gamma` claim,
division/nondivision, mutation, severed-shadow, cached-shadow, relabeling, and
held-out changing-support Gamma assays are `NOT-APPLICABLE`, not failed
positive tests. No wrapper Gamma is promoted.

Prefix words and graph nodes remain representations. Static restrictions do
not become region rewriting, adaptive frontiers do not become global time,
and the character/constant-profile controls defeat automatic physical
quotient promotion. The candidate does not construct stable records,
division doctrine, relational change, geometry, metric, curvature,
backreaction, continuum, GR, QFT, particles, Hamiltonian, constants, or
predictions. Normalization and branching do not derive actualization. These
walls are explicit in the abstract, ontology table, and conclusion.

## 11. Candidate-paper grade

**Grade: `ACCEPT-WITH-FIXES`.**

The regional mathematical core and the negative primary survive independent
hostile reconstruction. The only Seat R defect is the non-load-bearing word
“smallest” for the displayed adaptive code. After adjudicator-authorized
editorial correction of that adjective, no regional repair remains. This
grade does not promote a physical quotient, process, `Gamma`, ontology, or
successor construction.

## 12. Report hashes

The normalized hash replaces only the value on the next line by 64 ASCII
zeroes, preserves LF line endings, and hashes the complete bytes.

normalized_sha256: 3d536dbccbf825e8901df5d9bf5f433b808b75aaf8a717afd38fc08d76490760

ordinary_sha256: reported externally after freeze
