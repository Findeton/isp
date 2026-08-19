# Hostile review of Paper 12 — Seat O

## 1. Seat identity and mutual blindness

I served as **Seat O: ontology, ONE-GAMMA, indivisibility, and scientific
scope** under the frozen Paper 12 protocol. I did not read, list, request,
receive, or infer either sibling Paper 12 report or its scratch work. I did not
communicate with either sibling seat. The candidate, receipt, transcript, and
candidate verification were treated as claims and audit targets, never as
scientific evidence.

Immediate construction verdict:

```text
STATIC-RESPONSE / PRESENTATION-GLUING ONLY
strict primary: APR-BLOCKED-AT-BOUNDARY-GLUING
ONE-GAMMA status: GAMMA-UNCONSTRUCTED
```

Separate ontology verdict:

```text
one actual compatible relational record web: POSTULATED CANDIDATE
physical region, durable record, actual history, and geometry: UNCONSTRUCTED
candidate ontology: neither established nor refuted by this negative unit
```

## 2. Complete read set and authentication

I read the following frozen files completely and authenticated their ordinary
bytes before scientific work:

| role | path | independently measured SHA-256 |
|---|---|---|
| review protocol | `v16/note-apr-paper12-hostile-review-protocol.md` | `8fcc47af49b99e0781c41a2ee1f8b326853bad13b127aa52d3b8f64c5f4a197f` |
| ONE-GAMMA gate | `v16/note-apr-one-gamma-paper-review-gate.md` | `06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51` |
| construction pin | `v16/note-apr-paper12-negative-candidate-pin.md` | `6341a1184426f3a6be0ad619d9f02340124a76e5484bb94609462d5d765a6ebd` |
| exact source | `v16/code/apr_paper12_exact.py` | `c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7` |
| transcript | `v16/code/apr_paper12_output.txt` | `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f` |
| receipt | `v16/code/apr_paper12_receipt.json` | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` |
| paper | `v16/paper-12-atomless-regions-and-the-missing-gluing-law.md` | `cdb212c57c8b80099f9fc17eb0b1c5ed90c38ae2f5db7c50eb3038eb893f4de8` |
| candidate verification | `v16/note-apr-paper12-candidate-verification.md` | `0ee0e22879f2c1d086f8ca13d53bed4fc6f5261301865674d2d4368cec136e70` |

The receipt's canonical JSON after removal of `payload_sha256` hashes to
`1c6ded1e366cd4e3863a2774285ade5663f80e5228ed4077d0eb5b33bb0286f5`,
matching the protocol. The receipt's claimed transcript hash independently
recomputes to `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f`.
The repository was at candidate review commit
`6ee3588f0f12488f257a5b93950676a55cb4b3e4`; the source and candidate commits
were respectively `22ba8a1b6fc9833fe516ca1696e38531d7a0ea39` and
`7305ebf723ceb4c9c3965dc0a32622559ea693d8`.

I also authenticated the source's four required anchors:

| path | SHA-256 |
|---|---|
| `v16/note-apr-v5-verification.md` | `d2eae0fdc187317d7ee39c8efaca8fa2a94b6b8f06a3a0524cee0289396a077d` |
| `v16/apr_output_v5.txt` | `68374ea18576466ccc40553f8b221360fdfce3fc43d5b555a6eeb0d2827a2f56` |
| `v16/apr_receipt_v5.json` | `ab9ea941fceebf5b57c7955d483730f3a5f0b317bb5a21da9cc0820331919a61` |
| v5 canonical receipt payload | `04a1e370c601f9d7e3d5310f9bf20296d7be5c5428010f0f7af6c073d0b438d8` |

Primary-source checks were limited to claims the candidate actually makes:

- Jacob A. Barandes, [“Quantum Systems as Indivisible Stochastic
  Processes”](https://arxiv.org/html/2507.21192v1), especially section 2.2.
- John C. Baez and Kenny Courser, [“Structured
  Cospans”](https://arxiv.org/html/1911.04630), especially Theorem 2.3.
- Rafael D. Sorkin, [“Quantum Mechanics as Quantum Measure
  Theory”](https://arxiv.org/html/gr-qc/9401003v2).

## 3. Replay commands, return codes, and artifact hashes

All scratch paths were beneath
`/private/tmp/apr-paper12-seat-o.tmvry9`; no frozen source function was
imported or called.

| replay | command summary | rc | result |
|---|---|---:|---|
| fixture-free selftest | `python3 -B v16/code/apr_paper12_exact.py --selftest` | 0 | 13/13 checks; witness `c72319705d52c67d4fd6ae308bf06f66e1e7cc6f307a577ca5347cfb666703b3` |
| full publication | `python3 -B ... --run --output /private/tmp/.../output.txt --receipt /private/tmp/.../receipt.json` | 0 | output and receipt byte-identical to frozen artifacts |
| alien CWD | from `/private/tmp`, run absolute repository source | 0 | byte-identical |
| true off-tree | copied only source plus four authenticated inputs under an off-tree `v16/`; verified no `.git`; ran from unrelated CWD | 0 | byte-identical |
| default invocation | source with no mode | 2 | refused |
| unknown argument | source with `--unknown` | 2 | refused |
| missing publication paths | `--run` alone | 1 | refused |
| path on selftest | `--selftest --output ...` | 1 | refused |
| relative destination | one relative publication path | 1 | refused; no partial receipt |
| aliased destinations | output equals receipt | 1 | refused; no file |
| absent parent | both outputs below a missing parent | 1 | refused; no parent or partial file |
| overwrite | both destinations already existed | 1 | refused; both hashes unchanged |
| partial overwrite | output existed, receipt absent | 1 | refused; existing output unchanged and receipt absent |
| injected second-write failure | off-tree source copy changed only to pass `fail_after_first=True` | 1 | both final files and staging files absent |
| corrupted anchor | off-tree gate changed by one heading suffix | 1 | authentication refused before publication; both outputs absent |

Artifact hashes:

| artifact | SHA-256 |
|---|---|
| captured selftest JSON | `fa3ad97c3f03181350c573c753d1369b3a90d477f71ac757e48b7300db8a6454` |
| repository/alien/off-tree output (each) | `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f` |
| repository/alien/off-tree receipt (each) | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` |
| rollback-mutated source | `bec23e4555fd86e06cb8e0540bea4a3b36b3ee6dbeb757c245d8ed4f52eb88a3` |
| corrupted gate | `80075f84c40a82b70ec436aa66150a01d39f9260816c1da095406482568427a2` |

The source AST contains 58 function definitions and four classes, no float
literals, no scorer/fixture imports, no random/network/Git calls, and no
`Gamma` evaluator. Imports are confined to the standard library. Repository
root is derived from `__file__`, not the runtime CWD. The source does contain
expected immutable-input hashes and the frozen outcome ladder; neither is a
scientific lookup. Its capability rows are an interface inventory, so the
paper's analytical/source-level absence argument—not a receipt boolean—is
required for the negative primary.

## 4. Independent reconstruction method and private script hash

I wrote an independent exact script at the private path
`/private/tmp/apr-paper12-seat-o.tmvry9/seat_o_reconstruction.py`. It uses only
Python standard-library integers and `Fraction`, does not import the frozen
source, and separately rebuilds:

1. prefix-antichain canonicalization and Boolean operations;
2. the symbolic cylinder split and the registered Boolean census;
3. the volume and ultrafilter controls;
4. finite restriction projectors;
5. uniform/adaptive frontiers and a tagged pushout;
6. the two complete `ABC` distributions and all pair marginals;
7. first-failure precedence;
8. all seven Seat-O fresh changed objects;
9. a syntax-only AST audit of the frozen source.

The final script SHA-256 is
`7cf5b4e22da0158791e4b4125a31fe4765f4e22967f1bee1408949d311979df3`.
Its exact JSON result SHA-256 is
`099525a5b377b951e75ec8fe8a08d213ef6a5a2b48162a8c337d18497085f295`.

## 5. Claim-by-claim evidence table

| candidate claim | independent result | evidence grade |
|---|---|---|
| finite prefix-antichain operations form the stated Boolean algebra | zero failures on the registered family; canonical operations rebuilt | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| raw prefix algebra is atomless | for every nonzero antichain choose one cylinder `C(w)` and its proper nonzero child `C(w0)`; not merely a nine-row census | `ANALYTICAL-PROOF` |
| scalar volume equality is not contextual congruence | `nu(C0)=nu(C1)=1/2`, but after meet with `C0` the values are `1/2,0` | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| an ultrafilter quotient may be atomic | all-zero-path character is a Boolean homomorphism with image `{0,1}` | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| restriction is a positive complete two-port static instrument | exact diagonal reconstruction plus symbolic finite-additivity proof; `Q1+Q0=I`; unit's zero port retained | `ANALYTICAL-PROOF` |
| displayed frontiers are complete | sizes `1,2,4,8`; `{0,10,110,111}` is prefix-free with Kraft sum one | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| the depth-three tree and registered pushout compose as graphs | direct `15/14`; explicit tagged `0→1` plus `1→3` quotient has `17` tagged nodes, identifies two boundary nodes, and yields `15/14` | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| graph composition is not a process assignment | source inventory has tree segments and graph quotienting but no total filling-to-map evaluator, tensor factory, or nontrivial naturality evaluator; B0 alone has an assigned identity | `UNCONSTRUCTED` |
| the two global laws share `AB` and `BC` | every pair cell is exactly `1/4` for both laws | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| global completion is unselected | `P_U(A=C)=1/2`, `P_E(A=C)=1`; the same two local shadows therefore cannot choose between them | `ANALYTICAL-PROOF` |
| earliest primary is boundary gluing | normalization and raw atomlessness pass; the first required interface inventory missing is boundary gluing; promoting that gate alone moves first failure to two-arrow typing | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| measured role is static response only | restrictions answer static Boolean questions; graphs compose as presentations; `ABC` tables are simultaneous distributions; none evaluates a transition between complete configurations | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| presentation region is not yet physical region | no generated physical future equivalence, quotient `C_pres/G`, descended operations, or faithful held-out operational compiler is present | `UNCONSTRUCTED` |
| no indivisible `Gamma` exists | complete primitive inventory below has no unique transition root, division doctrine, or derived-shadow ledger | `UNCONSTRUCTED` |
| records and divisions are absent | no writer/continuation/reader recovery family and no same-law division/nondivision witnesses | `UNCONSTRUCTED` |
| geometry/backreaction is absent | graph adjacency is presentation data; no calibrated distance, curvature, changed-support law, response dependence, or blind-adversary exclusion exists | `UNCONSTRUCTED` |
| actual relational history is an ontology candidate | all frozen mathematical coordinates remain fixed under a distinct operational ontology; the candidate is explicitly a postulate | `CONDITIONAL-ON-PRINTED-HYPOTHESES` |
| actualization is not derived | normalization and branching assign weights only; no selection mechanism exists | `UNCONSTRUCTED` |
| successor requires a preregistered `Gamma_lambda` family | the paper gives requirements only and does not instantiate, select, or test such a family | `UNCONSTRUCTED` |

### ONE-GAMMA primitive-input inventory

| gate object | what actually exists | status |
|---|---|---|
| `C_pres` | prefix-antichain syntax and separate finite labelled trees | `PRESENTATION`, not one complete configuration catalogue |
| `G` | one finite relabeling-shape control | no full gauge group/action or canonical quotient |
| `C=C_pres/G` | nothing | `UNCONSTRUCTED` |
| `B` | four uniform frontiers, one adaptive example, B0 assignment | incomplete presentation boundary data |
| `Div` | nothing | `UNCONSTRUCTED` |
| `Gamma` | nothing | `GAMMA-UNCONSTRUCTED` |
| regional shadows | two `ABC` restrictions supplied as a diagnostic | not derived from a transition root |
| instrument | static Boolean restrictions | not a lawful-division shadow |
| record/reader | nothing | `UNCONSTRUCTED` |
| comparison/transport/rewrite | graph pushout only | no physical dynamics |
| Hilbert/Hamiltonian representation | nothing | not used |

There is therefore no unique nomological transition root. Under ONE-GAMMA
section 10, positive division, mutation, severed-edge, and nondivision tests
are `NOT-APPLICABLE`, not candidate failures. The honest current rung is
`GAMMA-UNCONSTRUCTED`; this preserves the scoped negative paper.

### Primary-source audit

| source claim in candidate | primary-source result |
|---|---|
| Barandes makes ordinary first-order transition probabilities fundamental while generic intermediate positive factorization can fail | supported: §2.2 defines stochastic `Gamma(t←t0)`, allowed conditioning times/division events, and shows the inferred intermediate matrix is generically pseudostochastic |
| Hilbert objects can be secondary/representational in Barandes | supported by the abstract and stochastic-quantum dictionary |
| Barandes supplies ISP's point-free/changing-support ontology | candidate explicitly says he does not; supported limitation: Barandes's configuration space is a fixed model ingredient and his division events are system-relative conditioning times |
| structured cospans compose open systems by pushout | supported: Baez–Courser Theorem 2.3 composes horizontal cells by chosen pushouts, with explicit categorical hypotheses |
| that precedent itself supplies a physical process map here | candidate explicitly denies this; the source does not imply such a map |
| quantum measure theory distinguishes history-level generalized measure from ordinary additivity | supported: Sorkin's `I2` interference may be nonzero while the grade-two `I3=0` sum rule holds |

No source derives the missing Paper 12 catalogue, `Gamma`, durable record,
changing geometry, locality, actualization, or numerical law.

## 6. Analytical proofs used

1. **All-depth raw atomlessness.** Put a nonzero finite prefix antichain in
   canonical form and choose any member `w`. `C(w0)` is nonempty, is contained
   in `C(w)`, and excludes `C(w1)`, so it is a proper nonzero subregion. This
   proves the theorem for every antichain, independently of the finite census.

2. **Restriction completeness.** For every finitely additive positive
   valuation, distributivity gives
   `E=(E meet C) join (E meet not-C)` as a disjoint join. Hence
   `(Q_C^1+Q_C^0)nu(E)=nu(E)`. Positivity and affinity follow directly; no
   branchwise normalization is allowed.

3. **Global-extension ambiguity.** Let `U(a,b,c)=1/8`. Let
   `E(a,b,c)=1/4` if `a=c`, otherwise zero. Summing either over the omitted
   coordinate gives `1/4` in every `AB` and `BC` cell, while summing the event
   `a=c` gives respectively `1/2` and `1`. Thus any selector needs additional
   law data.

4. **Wrapper insufficiency.** A wrapper exposing only those identical pair
   shadows has identical output on `U` and `E` while the complete laws differ.
   It therefore cannot be a complete-law evaluator. Choosing one completion
   after observing the shadows is exactly forbidden retrofit, not derivation.

5. **Raw-label nonontology.** Transport the full tree edge relation along a
   bijection `w -> neutral-i`. The in/out-degree multiset and every unlabelled
   graph fact remain fixed, while the predicate “node named `0` exists” changes
   from true to false. A raw name is therefore not a gauge-invariant beable.

6. **Named memory is not a durable record.** Take writer `W(b)=b`, a licensed
   candidate reset continuation `Phi(m)=0`, and reader `R(m)=m`. Then
   `R Phi W(1)=0`, not `1`. In the absence of a same-law closed future grammar
   excluding this continuation or a recovery theorem, renaming `K` as a
   record earns nothing.

7. **Adjacency does not determine metric or curvature.** The same tree edge
   set admits edge length one and edge length two. All delivered Boolean,
   question, pushout, and marginal results are unchanged. No calibration
   selects either assignment, and curvature is not even typed.

8. **Alternative laws are not co-actual histories.** `U` and `E` are rival
   probability laws over the same triples, not two triples sampled from one
   law. Combining them requires a new mixing weight `lambda`; at
   `lambda=1/2`, `P(A=C)=3/4`, and varying `lambda` gives a continuum of new
   laws. A change of noun cannot supply the missing actualization or history
   doctrine.

## 7. Frozen controls and fresh changed objects

### Common and assigned frozen controls

| control | independently reconstructed predicate | result/grade |
|---|---|---|
| `RAW-ATOMLESS` | `C(00000)=C(000000) join C(000001)`, disjoint proper children | pass; `ANALYTICAL-PROOF` at all depths |
| `VOLUME-NONCONGRUENCE` | `1/2=1/2` before context; `1/2 != 0` after meet with `C0` | pass |
| `ZERO-PORT` | asking unit gives zero `Q0`, retained in the two-port type | pass |
| `ADAPTIVE-FRONTIER` | `{0,10,110,111}` prefix-free, Kraft sum one, not a uniform row | pass |
| `PUSHOUT-NOT-PROCESS` | tagged graph quotient yields `15/14`; process-assignment inventory remains empty | pass; graph result only |
| `CACHED-MARGINAL` | move `1/16` from `001` to `000`: distribution remains positive; `AB` fixed; `BC` moves | pass |
| `ARBITRARY-SELECTOR` | identical pair shadows coexist with different `P(A=C)` | pass; every named convention is extra law data |
| `SYNTHETIC-LAW-EXCLUSION` | add normalized bit-flip matrix `[[0,1],[1,0]]` disconnected from controls | strict primary remains boundary gluing |
| `PRIMARY-PRECEDENCE` | baseline first false `boundary_gluing`; delete normalization -> `normalization`; supply gluing alone -> `two_arrow_typing` | pass |
| `RAW-NODE-ONTOLOGY` | explicit relabeling preserves transported graph, changes raw-name predicate | pass as finite metamorphic attack; not a full quotient theorem |
| `ANCHOR-FAILURE` | gate hash changed from `06d171...` to `80075f...` | rc 1 before science; no output/receipt |

### Seven mandatory Seat-O fresh changed objects

| changed object | exact observation | disposition |
|---|---|---|
| neutral tree node promoted to beable, then relabelled | graph shape fixed; “`0` exists” changes `true -> false` | raw identifier is representation |
| candidate memory renamed durable record | reset recovery on `{0,1}` is `{0:0,1:0}` | durability unconstructed |
| raw relation renamed distance/curvature | same edges admit all lengths 1 or all lengths 2 | geometry uncalibrated/unconstructed |
| disconnected executable law inserted | bit-flip columns normalize; all original interfaces and primary unchanged | synthetic control is not physics |
| wrapper `Gamma` retrofitted from `AB/BC` | wrapper output identical on `U,E`; complete event changes `1/2 -> 1` | K12/OG wrapper rejected |
| alternative law arguments declared co-actual histories | a half-mixture gives new `P(A=C)=3/4`; mixing weight is new law data | no actual-history inference |
| ontology candidate replaced with an operational-only ontology | candidates differ; independently measured-coordinate hash remains `52713df324890916465f22c8ffc81b571acb7be3b2a0fe98ab22e1ae3d8bfdba` | ontology remains postulated |

These results do not refute the paper. They confirm that its promotion walls
are necessary and that it respects them.

## 8. Numbered KILL, REPAIR, and NARROWING findings

**KILL-0 — no reproducible hard kill applies to the candidate as written.**
The hostile objects do kill several *forbidden stronger readings*: the wrapper
fails K12, named memory fails K13, raw relation fails K14, and a disconnected
law fails K11. The paper expressly declines all four promotions.

**REPAIR-0 — no scientific repair is required.** No theorem, coordinate,
primary, ontology status, or source implication needs alteration.

**NARROWING-1 — “point-free” is presentation-level.** The popular-language
phrase “contains no underlying points” is licensed only in the paper's later
explicit sense: no primitive point labels are needed in the abstract Boolean
algebra, and infinite paths are not physical points. It is not a physical
pointlessness theorem. The title, subtitle, abstract, and §2 already enforce
this qualification.

**NARROWING-2 — the node metamorphic control is finite.** Equality of one
relabelled degree signature is not a complete gauge quotient. My explicit
edge-transport reconstruction supports the registered relabeling only. The
paper correctly leaves `G` and the physical quotient unconstructed.

**NARROWING-3 — `contact=PRICED` and `causality=PRICED` in the receipt are
debt labels, not priced physical interfaces.** At the earlier boundary-gluing
failure there is no law relative to which their price could be evaluated. The
paper uses the safer and correct wording “not established/unconstructed.”

**NARROWING-4 — source precedents are typed precedents only.** Structured
cospans license graph-level pushout composition under categorical hypotheses;
Barandes licenses the indivisible stochastic law type on a fixed
configuration space; Sorkin licenses nonadditive history measures. None
supplies ISP's regional law. The candidate already states these limits.

## 9. Scoped coordinates and earliest recommended primary

| coordinate | Seat-O verdict |
|---|---|
| normalization | established for static restriction questions |
| raw atomlessness | `SYNTAX-ONLY`, analytically proved |
| physical atomlessness | `UNCONSTRUCTED` |
| process | `STATIC-RESPONSE-ONLY` |
| graph gluing | three finite pushouts established |
| boundary process gluing | `UNCONSTRUCTED` |
| complete future profiles | `UNCONSTRUCTED` |
| regional congruence | `UNCONSTRUCTED` |
| comparison/dynamic locality | `UNCONSTRUCTED`; no measured physical nonlocality |
| contact/causal order | `UNCONSTRUCTED`; merely later debts |
| ONE-GAMMA provenance | `GAMMA-UNCONSTRUCTED` |
| law selection | `UNSELECTED` |
| measured ontology role | `STATIC-RESPONSE` |
| candidate ontology | `POSTULATE`, neither proved nor falsified |
| actualization | `POSTULATED-NOT-DERIVED` / mechanism absent |
| geometry/gravity | `UNCONSTRUCTED` |

The earliest recommended primary is exactly:

```text
APR-BLOCKED-AT-BOUNDARY-GLUING
```

This is not a negative result about all possible regional laws. It is the
earliest absence in this construction.

## 10. Ontology, GR/QFT, and actualization walls

The delivered ontology is only a candidate declaration: one actual compatible
relational record web, with alternative complete configurations as
counterfactual law arguments. Paper 12 supplies neither the complete
configuration type nor the co-reference/compatibility doctrine that would
turn realized configurations into an actual history. Raw words, node names,
frontier depth, matrix indices, and tree order remain representational. No
universal point, place, clock, tick, or foliation is introduced.

A Barandes-style architectural precedent is supported only at this level:
ordinary first-order transition probabilities can be fundamental, allowed
conditioning times are system-relative division events, arbitrary
intermediate positive factorization can fail, and Hilbert objects can be
secondary. Barandes's cited model uses a fixed configuration space; it does
not derive ISP's changing support, point-free catalogue, records, relational
locality, backreaction, or actualization.

Paper 12 constructs no lawful division, durable record, changing relation,
metric, connection, curvature, reciprocal response, gravity, continuum,
dimension, signature, Lorentz invariance, QFT, particle species, Hamiltonian,
vacuum, constants, empirical prediction, or GR limit. Its normalization and
branching do not select an actual successor. All such walls are printed
clearly in the paper and survive hostile reconstruction.

The proposed successor is correctly only a motivation: freeze an explicit
family `(C_pres,G,C,B,Div,Gamma_lambda)` before seeing its shadows, derive
every claimed regional/instrument/record/rewrite shadow from the one law, and
test both a lawful division and a typed nondivision cut. No `Gamma_lambda` is
claimed to exist here.

## 11. Candidate-paper grade

```text
ACCEPT
```

Reason: every positive result survives at its printed mathematical scope; the
earliest negative primary is independently supported; the paper contains the
required load-bearing indivisibility correction; it cleanly separates
presentation, static response, process, physical referent, candidate ontology,
law selection, and actualization; and all hostile ontology promotions are
explicitly refused. The four narrowings above are interpretive guardrails
already present in the candidate, not repair orders.

## 12. Report hashes

Hash rule: replace only the value below with 64 ASCII zeroes, normalize line
endings to LF, and hash the complete bytes.

normalized_sha256: baf75e10295db6c7f68f6292407b970fff7b79100bb7c213345fc52080076c20

ordinary_sha256: reported externally after byte freeze
