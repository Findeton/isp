# Paper 12 hostile review — Seat P: process, cospans, boundary gluing, and overlaps

**Date:** 2026-08-19  
**Seat:** P — process, cospans, boundary gluing, overlapping laws  
**Protocol:** `v16/note-apr-paper12-hostile-review-protocol.md`, commit
`6ee3588f0f12488f257a5b93950676a55cb4b3e4`, SHA-256
`8fcc47af49b99e0781c41a2ee1f8b326853bad13b127aa52d3b8f64c5f4a197f`  
**Verdict:** `ACCEPT-WITH-FIXES`  
**Recommended strict primary:** `APR-BLOCKED-AT-BOUNDARY-GLUING`

## 1. Seat identity and mutual blindness

I performed only Seat P under protocol Sections 1–5, 7, and 9–14. I did not
read, list, request, receive, or infer either sibling report or private
scratch, and I did not communicate with another review seat. I did not import
or call any function from `apr_paper12_exact.py`. The frozen source was used
only as authenticated text and as a subprocess. Independent arithmetic,
graphs, pushouts, global completions, controls, and classifier checks were
implemented in `/private/tmp`.

The candidate paper, transcript, receipt, verification note, and source
conclusions were treated as claims or audit targets, never as scientific
oracles.

## 2. Complete read set and authentication

All immutable review-corpus bytes matched before scientific work.

| Role | Path | SHA-256 | Result |
|---|---|---:|---|
| ONE-GAMMA gate | `v16/note-apr-one-gamma-paper-review-gate.md` | `06d171a3eea8109e177e2dfa3cb5536fe3785043e676f735c36e91d03834cb51` | match |
| construction pin | `v16/note-apr-paper12-negative-candidate-pin.md` | `6341a1184426f3a6be0ad619d9f02340124a76e5484bb94609462d5d765a6ebd` | match |
| exact source | `v16/code/apr_paper12_exact.py` | `c209486a94016c00921c3b9edfeb2f53eef7d005180eb3c1d95153e56fec86a7` | match |
| transcript | `v16/code/apr_paper12_output.txt` | `7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f` | match |
| receipt | `v16/code/apr_paper12_receipt.json` | `d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39` | match |
| scientific candidate | `v16/paper-12-atomless-regions-and-the-missing-gluing-law.md` | `cdb212c57c8b80099f9fc17eb0b1c5ed90c38ae2f5db7c50eb3038eb893f4de8` | match |
| candidate verification | `v16/note-apr-paper12-candidate-verification.md` | `0ee0e22879f2c1d086f8ca13d53bed4fc6f5261301865674d2d4368cec136e70` | match |
| hostile protocol | `v16/note-apr-paper12-hostile-review-protocol.md` | `8fcc47af49b99e0781c41a2ee1f8b326853bad13b127aa52d3b8f64c5f4a197f` | match |

The canonical receipt payload, after removing `payload_sha256`, independently
hashed to
`1c6ded1e366cd4e3863a2774285ade5663f80e5228ed4077d0eb5b33bb0286f5`,
matching both the receipt and protocol.

The source's authenticated, non-evidential v5 inputs were also read for
integrity/off-tree replay:

| Path | SHA-256 |
|---|---:|
| `v16/note-apr-v5-verification.md` | `d2eae0fdc187317d7ee39c8efaca8fa2a94b6b8f06a3a0524cee0289396a077d` |
| `v16/apr_output_v5.txt` | `68374ea18576466ccc40553f8b221360fdfce3fc43d5b555a6eeb0d2827a2f56` |
| `v16/apr_receipt_v5.json` | `ab9ea941fceebf5b57c7955d483730f3a5f0b317bb5a21da9cc0820331919a61` |
| v5 canonical payload | `04a1e370c601f9d7e3d5310f9bf20296d7be5c5428010f0f7af6c073d0b438d8` |

The source blob at commit `22ba8a1` and all four candidate blobs at commit
`7305ebf` reproduced the ordinary hashes above.

### Primary literature checked

1. John C. Baez and Kenny Courser, “Structured Cospans,” arXiv:1911.04630,
   <https://arxiv.org/abs/1911.04630>. Checked implication: under the stated
   categorical hypotheses, structured-cospan horizontal composition uses
   pushouts of apices. This supports the paper's graph-level claim; it does
   not supply a physical filling-to-map functor.
2. Rafael D. Sorkin, “Quantum Mechanics as Quantum Measure Theory,”
   arXiv:gr-qc/9401003, DOI `10.1142/S021773239400294X`,
   <https://arxiv.org/abs/gr-qc/9401003>. Checked implication: generalized
   quantum measure weakens classical additivity, supporting the paper's
   warning that ordinary additive weights on arbitrary reconvergent
   alternatives are not automatic. It supplies no APR process.
3. Jacob A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
   arXiv:2507.21192, <https://arxiv.org/abs/2507.21192>. Checked implication:
   an indivisible stochastic process generally need not admit a positive
   intermediate divisibility factor. It does not construct ISP's catalogue,
   gluing law, records, or relational `Gamma`.

## 3. Integrity replay

### Commands and results

| Audit | Command form | Exit/result |
|---|---|---|
| repository self-test from alien CWD | `python3 -B /abs/.../apr_paper12_exact.py --selftest` | `0`; `13/13` rows; stdout SHA-256 `fa3ad97c3f03181350c573c753d1369b3a90d477f71ac757e48b7300db8a6454` |
| private full replay | `python3 -B /abs/.../apr_paper12_exact.py --run --output /private/tmp/apr_p12_seatp_replay_output.txt --receipt /private/tmp/apr_p12_seatp_replay_receipt.json` | `0` |
| true off-tree self-test | same command on `/private/tmp/apr_p12_seatp_offtree`, which has no `.git` | `0`; stdout byte-identical |
| true off-tree publication | off-tree source from `/private/tmp/apr_p12_seatp_alien` | `0`; both artifacts byte-identical |
| no arguments | source only | `2` |
| unknown argument | `--unknown` | `2` |
| self-test plus publication path | `--selftest --output ...` | `1` |
| partial run arguments | `--run --output ...` | `1` |
| relative destinations | `--run --output relative --receipt relative` | `1`; targets absent |
| missing parent | absolute destinations under absent parent | `1`; targets absent |
| existing targets | two sentinel files | `1`; both byte-identical afterward |
| aliased destinations | two absolute spellings of one path | `1`; target absent |

Private replay hashes:

```text
/private/tmp/apr_p12_seatp_replay_output.txt
7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f

/private/tmp/apr_p12_seatp_replay_receipt.json
d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39

/private/tmp/apr_p12_seatp_offtree_output.txt
7ae34f1fcaf7f8e2739c8e17ac90ee87f629e90713401bc86367524b41f8ab7f

/private/tmp/apr_p12_seatp_offtree_receipt.json
d4e16c262d1c929d6e0507ef482eef4c2ff26c7f41f9dc4bf0bc58b708adfd39
```

The rollback branch is also source-provable: both temporary files are staged
first; after the injected failure, the exception branch removes every staged
path still present and every published path. The black-box self-test reaches
that branch and reports both destinations absent. Existing-target refusal
precedes staging. This is exact for the registered sequential threat model;
the protocol does not test concurrent filesystem races.

### AST and source audit

- imports are standard library only;
- zero float literals, tolerances, randomness, network, Git, subprocess,
  sleep, or runtime-CWD calls occur on substantive paths;
- neither scorer nor fixture module is imported;
- `Path(__file__)`, not the current directory, locates immutable inputs;
- no callable assigns a filling to a positive process map;
- no tensor/Kronecker factory, interchange law, or nontrivial naturality
  callable exists;
- the v5 files flow only into authentication metadata. Boolean, question,
  boundary, overlap, capability, and classifier objects are rebuilt without
  consuming a v5 result word;
- classifier inputs are instances of the typed `Capability` class; a bare
  mapping is rejected;
- the explicit anchor checks can detect a moved reconstruction, but none is
  used to choose the primary. The primary is returned by the ordered
  capability classifier.

All authenticated repository inputs had identical hashes before and after
the subprocess battery. No bytecode was produced under `-B`.

One prose-firewall defect remains: line 390 of the candidate is headed
“Ontology ledger.” The construction pin and protocol prohibit ledger language
in the scientific paper. This is an editorial contract violation, not an
integrity block or a scientific counterexample; see `REPAIR-P1`.

## 4. Independent reconstruction method

The independent verifier is:

```text
/private/tmp/apr_p12_seatp_independent.py
SHA-256 b5d766727e1857e649850dc33395f52d7621a345227f5a3a7ef07650d2675dde

/private/tmp/apr_p12_seatp_independent_result.json
SHA-256 30b32b79c6cb2d3015351c26606c5a0c1df3275083d79f4aa372b477f9735c55

canonical result payload
SHA-256 ac232182aeef0143ba1e929b83ec63c95914c9acffccfb582923b51f3e9b174a
```

It uses independent `Fraction` arithmetic, a separate region normalizer,
separate restriction effects, a tagged disjoint-union/union-find pushout, a
separate boundary-leg implementation, direct marginalization, and an
independent precedence classifier. It imports neither the frozen source nor
its result objects. Result: `PASS`, zero failed predicates.

## 5. Claim-by-claim evidence

| Candidate claim | Grade | Seat-P finding |
|---|---|---|
| Four uniform frontiers are prefix-free and complete | `INDEPENDENT-EXACT-RECONSTRUCTION` | Sizes `1,2,4,8`; every Kraft sum is `1`. |
| `{0,10,110,111}` is a complete adaptive frontier | `INDEPENDENT-EXACT-RECONSTRUCTION` | Prefix-free; weights `1/2+1/4+1/8+1/8=1`. |
| Full depth-three tree has `15/14` vertices/edges | `INDEPENDENT-EXACT-RECONSTRUCTION` | Direct construction gives exactly `15/14`. |
| Three registered factorizations compose by tagged pushout to the direct tree | `INDEPENDENT-EXACT-RECONSTRUCTION` | All three quotients have `15/14`, no mixed-label class, and exact labeled edges. |
| These are structured-cospan-style graph controls | `CONDITIONAL-ON-PRINTED-HYPOTHESES` | Correct finite instance with implicit inclusion legs; not a construction of the full symmetric monoidal double category. |
| Graph pushout is not a process assignment | `ANALYTICAL-PROOF` | The graph codomain is `(nodes, edges, legs)`; a process requires a separately typed positive map plus functorial laws. No such edge exists. |
| Only B0 has an active empty identity assignment | `FINITE-CONTROL-ONLY` | Registry census is `B0=[empty]`, `B1=B2=B3=[]`; the B0 row has no assigned process map, so “process identity” needs narrowing. |
| No total filling-to-process assignment exists | `UNCONSTRUCTED` | Complete interface/source audit finds graph composition and static restriction maps but no `Filling -> PositiveMap` assignment. |
| No tensor/interchange/naturality process law exists | `UNCONSTRUCTED` | No typed objects, maps, or equations instantiate any of the three. Graph relabeling is not process naturality. |
| No arbitrary-frontier process factory exists | `UNCONSTRUCTED` | A generic frontier validator exists; the active boundary/assignment factory is only B0–B3 and does not assign arbitrary adaptive fillings. |
| Static question normalization, tree restriction, and graph pushout are distinct | `ANALYTICAL-PROOF` | Their domains/codomains differ; no provenance map welds them. |
| Both printed `ABC` laws are positive and normalized | `INDEPENDENT-EXACT-RECONSTRUCTION` | Exact sums are `1`; all masses nonnegative. |
| Their `AB` and `BC` shadows coincide cellwise at `1/4` | `ANALYTICAL-PROOF` | Independent marginalization reproduces all eight pair cells. |
| `P(A=C)` is respectively `1/2` and `1` | `INDEPENDENT-EXACT-RECONSTRUCTION` | Exact. |
| Local shadows do not select a global completion | `ANALYTICAL-PROOF` | A continuous positive family with the same pair shadows exists; see Proof B. |
| Markov, entropy, sparsity, order, or hash selection would be extra law data | `ANALYTICAL-PROOF` | Pair data alone are constant over the continuous family; any unique choice depends on an extra functional or axiom. |
| `AB/BC` is simultaneous gluing, not a transition/division/order law | `ANALYTICAL-PROOF` | The primitive variables carry no source/target, intervention, division, or temporal type. |
| Cached pair shadows fail after a global mutation | `INDEPENDENT-EXACT-RECONSTRUCTION` | A positive mutation preserves `AB` while changing `BC`; cached `BC` is detected. |
| Boundary gluing is the earliest failed prerequisite | `INDEPENDENT-EXACT-RECONSTRUCTION` | Normalization and raw algebra pass; missing assignment and identities independently force boundary gluing false. Earlier/later controls move as registered. |
| Process coordinate is `STATIC-RESPONSE-ONLY` | `ANALYTICAL-PROOF` | Restriction questions are static maps on one algebra; no horizontal process is constructed. |
| A physical `(C_pres,G,C,B,Div,Gamma)` exists | `UNCONSTRUCTED` | No such joint primitive occurs. The negative paper correctly denies it. |

## 6. Analytical proofs used

### Proof A — the three graph composites

For a depth interval `[r,s]`, the segment contains every binary word at depths
`r,...,s` and every parent-child edge in that interval. Tagged pushout
composition identifies only the two tagged copies of each shared boundary
word.

- `[0,1]` and `[1,3]`: `3+14-2=15` vertices and `2+12=14` edges;
- `[0,2]` and `[2,3]`: `7+12-4=15` vertices and `6+8=14` edges;
- `[0,1]`, `[1,2]`, `[2,3]`: `3+6+12-2-4=15` vertices and
  `2+4+8=14` edges.

The quotient class of each boundary word contains two copies of the same
label, so the exact labeled edge set is the direct depth-three tree. A naive
disjoint union of the first pair instead has `17/14`: it leaves two duplicate
boundary vertices. Counts alone are not the proof; the independently computed
quotient labels and edges agree exactly.

### Proof B — a continuum of global completions

For `-1/8 <= t <= 1/8`, define

```text
P_t(a,b,c) = 1/8 + t (-1)^(a+c).
```

The eight masses are nonnegative and sum to one. Summing over `c` cancels the
`t` term, as does summing over `a`, so every `AB` and `BC` cell is `1/4` for
every `t`. Meanwhile

```text
P_t(A=C) = 1/2 + 4t.
```

Thus `t=0` is the uniform law, `t=1/8` is the printed `A=C` law, and the fresh
strictly positive control `t=1/16` has masses `3/16` and `1/16` and
`P(A=C)=3/4`. The local tables therefore cannot determine the global
completion. This is stronger than a two-row counterexample but remains a
static classical extension theorem.

### Proof C — graph composition is not process composition

The graph composite consumes open-graph legs and returns a quotient graph.
The restriction question consumes a valuation and returns two subnormalized
valuations. A horizontal process assignment would instead consume every
typed filling and return a positive map, with identity, sequential
composition, tensor, interchange, and required naturality equations. Equality
of graph apices cannot type-check as any of those map equalities. No common
identifier or matching count changes this domain/codomain mismatch.

### Proof D — an identity label does not create an identity

The fresh same-boundary control uses `B1={0,1}` and one apex with input legs
`0->x0,1->x1` but output legs `0->x1,1->x0`, while labelling the row
“identity.” A boundary-fixed cospan isomorphism to the identity would be
forced by the input legs to fix `x0,x1`, then would fail both output triangles.
Hence the graph is not the identity despite its label. The candidate's B0 row
is harmless only when described as an identity-labelled assignment rather
than an earned physical process identity.

## 7. Frozen controls and fresh changed objects

### Common and assigned frozen controls

| Control | Independent result | Grade |
|---|---|---|
| `RAW-ATOMLESS` | Fresh depth-seven cylinder splits into two nonzero disjoint children | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| `VOLUME-NONCONGRUENCE` | `(1/2,1/2)` becomes `(1/2,0)` after the left meet context | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| `ZERO-PORT` | Unit question has an exactly zero branch; deleting it changes the two-port type | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| `ADAPTIVE-FRONTIER` | Registered adaptive cover is valid and absent from uniform-depth rows | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| `PUSHOUT-NOT-PROCESS` | All graph pushouts pass while no filling-to-map assignment exists | `ANALYTICAL-PROOF` |
| `CACHED-MARGINAL` | Fresh global mutation keeps `AB` and moves `BC` | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| `ARBITRARY-SELECTOR` | Continuous completion family survives the same local data | `ANALYTICAL-PROOF` |
| `SYNTHETIC-LAW-EXCLUSION` | Source dataflow never supplies v5 objects to physical capability construction | `ANALYTICAL-PROOF` |
| `PRIMARY-PRECEDENCE` | Baseline/earlier/later are boundary-gluing/inconsistent/two-arrow | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| `IDENTITY-DOMAIN` | B0-only registry reproduced; fake B1 identity label rejected | `FINITE-CONTROL-ONLY` plus fresh countercontrol |

### Mandatory fresh objects

| Fresh object | Exact result |
|---|---|
| adaptive `{00,01,1}` | prefix-free; `1/4+1/4+1/2=1` |
| second adaptive `{0,100,101,11}` | prefix-free; `1/2+1/8+1/8+1/4=1` |
| four-stage factorization `[0,1][1,2][2,3][3,4]` | exact direct depth-four tree, `31/30` |
| same four-stage factorization with the depth-two `00/01` boundary leg exchanged | two mixed-label quotient classes; not boundary-fixed equal to the direct tree |
| naive union for `[0,1]` and `[1,3]` | `17/14`, versus tagged pushout `15/14` |
| positive parity perturbation `t=1/16` | same `AB/BC=1/4`, `P(A=C)=3/4` |
| global mutation `000 += 1/16`, `001 -= 1/16` | positive; `AB` unchanged, `BC` changed |
| same-boundary swap graph presented as identity | fails boundary-fixed identity condition |

## 8. KILL, REPAIR, and NARROWING findings

### KILL-P1 — no hard scientific kill triggered

No candidate claim triggers `K6`–`K10` at its stated scope. In particular, the
paper explicitly refuses to promote graph pushouts to processes and explicitly
types `AB/BC` as simultaneous static gluing. The fake-identity, changed-leg,
and cached-shadow attacks would kill stronger promotions, but the paper does
not make them.

### REPAIR-P1 — remove internal ledger language

Rename `## 9. Ontology ledger` to `## 9. Ontology table`. This is required by
the frozen prose firewall and changes no theorem, coordinate, or primary.

### REPAIR-P2 — narrow the B0 identity sentence

Replace “only the one-port boundary has an active empty-process identity” with
substantially:

> Only B0 carries an active identity-labelled empty graph assignment. Because
> no filling-to-process map is assigned, this row is not yet an earned
> physical process identity.

The registry census is exact, but the word `identity` currently outruns its
map-level equations.

### NARROWING-P1 — keep finite pushout scope explicit

The three registered results are exact pushouts of finite simple directed
open-tree presentations with inclusion legs. They do not instantiate an
arbitrary structured-cospan category, tensor, interchange, naturality, or a
process semantics. The paper mostly says this already; captions and summary
language should retain “finite graph control.”

### NARROWING-P2 — separate completion nonuniqueness from process axioms

The overlap theorem proves that local pair shadows do not determine a global
distribution. It does not prove that a physical process must contain a
selector that reconstructs `Gamma` from local marginals. Under ONE-GAMMA, the
global object is primitive and the regional tables are derived restrictions.
Therefore `regional-overlap-selector` is best printed as a separate
one-law-provenance/law-selection debt, not a categorical process axiom. The
strict primary does not move: missing filling assignment, nontrivial
identities, tensor, and naturality independently block boundary gluing.

### NARROWING-P3 — adaptive-frontier scope

The fresh covers prove that the uniform B0–B3 family is not an
arbitrary-frontier factory. This is a completeness failure relative to the
declared regional-question target, not a theorem that every legitimate finite
process category must contain every adaptive frontier.

## 9. Scoped coordinates and primary

| Coordinate | Seat-P verdict | Evidence grade |
|---|---|---|
| normalization | passes exactly | `ANALYTICAL-PROOF` |
| raw atomlessness | syntax theorem passes | `ANALYTICAL-PROOF` |
| finite graph gluing | three exact registered pushouts; fresh depth-four positive | `INDEPENDENT-EXACT-RECONSTRUCTION` |
| arbitrary-frontier factory | unconstructed | `UNCONSTRUCTED` |
| active process identities | unconstructed beyond an identity-labelled B0 row | `FINITE-CONTROL-ONLY` |
| filling-to-process assignment | unconstructed | `UNCONSTRUCTED` |
| tensor/interchange/naturality | unconstructed | `UNCONSTRUCTED` |
| overlapping global completion | nonunique; continuum survives | `ANALYTICAL-PROOF` |
| process | `STATIC-RESPONSE-ONLY` | `ANALYTICAL-PROOF` |
| physical regional quotient | unconstructed | `UNCONSTRUCTED` |
| ONE-GAMMA provenance | unconstructed | `UNCONSTRUCTED` |
| law selection | `UNSELECTED` | `ANALYTICAL-PROOF` at this interface |

The earliest supported primary is
`APR-BLOCKED-AT-BOUNDARY-GLUING`. This result does not depend on treating a
global selector as a categorical process axiom: the absence of a total
filling assignment and map-level identities is already decisive.

## 10. Ontology and GR/QFT/actualization walls

The immediate construction role is a static restriction response on a fixed
presentation algebra, accompanied by finite graph presentations and static
joint-distribution controls. It is not a horizontal stochastic process, an
actual history, or a relational rewrite.

The candidate ontology—one actual compatible relational record web—is not
refuted by this negative result. It remains a postulate without co-reference,
same-law record recovery, division doctrine, or actualization mechanism.

Nothing reviewed here constructs dynamic locality, contact, causal order,
reciprocal backreaction, chronology, extensive physical valuation, metric,
connection, curvature, stress response, gravity, continuum, dimension,
signature, Lorentz invariance, GR, QFT, particles, Hamiltonian, vacuum,
constants, empirical predictions, law selection, or actualization. The
structured-cospan, Sorkin, and Barandes precedents do not supply those missing
objects.

## 11. Candidate-paper grade

**`ACCEPT-WITH-FIXES`.**

The negative result, exact finite theorems, underdetermination theorem,
process coordinate, and earliest primary survive hostile reconstruction. The
two required repairs are terminology/prose-scope corrections. The three
narrowings prevent finite graph controls or local-to-global nonuniqueness from
being mistaken for a complete process theorem. None changes a displayed
number, theorem, coordinate, or the strict primary.

## 12. Report hashes

normalized_sha256: 3c3eebff36146fcd95c37133e7b1eff35548fee93713e621676389a3e483704f

ordinary_sha256: reported externally after final-byte freeze
