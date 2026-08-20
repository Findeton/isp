# Paper 14 hostile review — Seat R (referent and ontology)

Date: 2026-08-20

Status: **FROZEN HOSTILE REPORT**

## 1. Verdict

```text
GRADE: ACCEPT-WITH-FIXES
FIRST EXACT SCIENTIFIC COUNTEREXAMPLE: none
EARLIEST AFFECTED PRODUCT COORDINATE: none
EARLIEST SUPPORTED LAW/REFERENT COORDINATE: P14-DECLARED-POINT-FREE-HISTORY-LAW
STRONGEST SUPPORTED GEOMETRIC COORDINATE: P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
LAW PROVENANCE: DECLARED-NEW-LAW-POSTULATE
```

The mathematical referent survives.  It is the isomorphism class of the
complete onset-incidence/value/law/record structure, with distinct incidence
nodes retained even when an automorphism exchanges them.  The construction
does not count printed labels, addresses, serialization rows, or node orbits.
Possible stable types, actual occurrences selected by an external `rho`, and
complete division frontiers remain different types.

The three fixes in Section 12 are bounded ontology/certificate clarifications.
They do not change a mathematical object, a number, or any product coordinate.

The supported product vector is:

```text
law:         P14-DECLARED-POINT-FREE-HISTORY-LAW
record:      P14-INDIVISIBLE-STABLE-HAPPENING-BUNDLES
actuality:   P14-ACTUAL-STABLE-HAPPENINGS-CONDITIONAL-ON-ACTUALIZATION
dependency:  P14-LOCALLY-FINITE-BUNDLE-POSET
frontier ab: P14-COMPLETE-DIVISION-FRONTIER
frontier abg:P14-COMPLETE-DIVISION-FRONTIER
frontier a:  P14-FRONTIER-INCOMPLETE
valuation:   P14-INTERVAL-FINITE-ATOMIC-MEASURE
geometry:    P14-PREMETRIC-ORDER-AND-INTERVAL-MEASURE
```

This is a theorem of one declared model law.  It is not law selection,
actualization, chronology, a causal-cone theorem, topology, dimension, scale,
volume calibration, metric, curvature, gravity, continuum physics, or QFT.

## 2. Authentication and blindness

Pre-science authentication gave:

```text
HEAD ed258111d2ff604de97816266be2184fd1d06c63
protocol 7eba533fea4bb96370ed27aa46f9f6c933b207317495d9a4955c7868f89f5fed
pin      0dc92112e5db39bb9e1a8c51a018119e783f347505d3e5bf03debf47fe31ef44
source   1a1d9a7acc3ef4ba62a9e9b0f6101263dde3b72dd9d407918ea0be653d5d628e
paper    ffc3dca2863bf9f36c9fe62e8dff80628c59c8837b3d96006e449329dee05ec1
note     e6d59fd49e5af805df96f8b3a4c2db5676dafaa3c552ecadb0779ca690887253
fresh    4f5d8d21bb66d5e7c41a9c34a35a26ec955b03497d9682564efd23df681126c7
output   95a38ebbb6d2e9c85c2a2f66ca3275fd1f4205761dfcc5eae6a1d9ea2b233993
receipt  2d320edc0eb152d5fcb6ffdf1444e8071d9466c5773c13be51ad438036c2fa4c
verify   c8aec2827778a0f31645a374eebfa03c82563da9a7395ef6b5af708c1ee9ae42
```

The binding pin, source-freeze, and official-result commits are respectively
`9687d59c2faa29efd53993643deb92b3f5c5a025`,
`dda7a01e80a17883a039bd0e33a3453b0601af3f`, and
`44c23725559dda2d00f6dc482088d8a97e5b6964`.

I read the protocol, pin, paper, construction note, fresh input, output,
receipt, and verification note completely.  I did not import the candidate.
The no-import reconstruction was frozen before source inspection.  Mutual
blindness was preserved throughout.

## 3. Clean-room reconstruction

The independent oracle reconstructed, rather than accepted, the following.

1. With
   `R=((3,-4),(4,3))/5`, `R^T R=I`.  The writer maps place branch 0 in
   record sector 0 and branch 1 in record sector 1, giving
   `V0^T V0+V1^T V1=I` and `P_r V_s=delta_rs V_s` on both inputs.
2. Each of the six generators `I_record tensor R^e`, `e=0,...,5`, commutes
   with both record projectors.  Generator-wise intertwining therefore gives
   every finite word by induction.  The record flip does not commute.
3. The minimal grammar has exactly five reachable states, seven legal words,
   and five trace classes.  Its dependency SCCs are `({a,b},{c},{d})`, with
   quotient edges `{a,b}<{d}` and `{c}<{d}` and `{a,b} || {c}`.
4. The law
   `Gamma(a,b,g,y)=1/4 B[g,a xor b] B[y,g]`,
   `B=((9,16),(16,9))/25`, has 16 positive histories and total mass one.
   It gives `P(g=1|p)=(16/25,9/25)`,
   `P(y=1|g)=(16/25,9/25)`, and
   `P(y=1|p)=(288/625,337/625)`.
5. Direct and cut rows are exactly
   `(337,288,288,337)/625`.  The two local residuals are `7/25`; the
   integrated residual is `49/625`.
6. The correlated antichain has weak product `2/5` in both serializations,
   while the local factors move from `(1/2,4/5)` to `(3/5,2/3)`.  Strong
   descent therefore fails.
7. The screened fork has covariance `1/45`, all eight conditional-screening
   equalities exact, and `Gamma(1,1,0)=3/20`; strong descent passes.
8. An independent rooted-tree enumeration reproduced all 12 shape-census
   rows and all 38 finite rows.  Every `n`-cell row has `4n` bundles, `5n`
   raw record components, `16^n` positive histories, and exact normalization.
   The finite-branching/dependency-depth proof makes each direct-limit closed
   interval finite.
9. All six fresh cases were recomputed directly from their raw parameters;
   no printed disposition was used as evidence.

The private frozen reconstruction is
`/private/tmp/p14-seat-r-cleanroom.DsmZdg/cleanroom_reconstruction.md`, SHA-256
`6783714616970c9b1251fcad24f63db673e58915346d840ed8b6a51a44d9d392`.
The independent verifier is
`/private/tmp/p14-seat-r-cleanroom.DsmZdg/independent_verifier.py`, SHA-256
`c60e40c212c894fd543ee54cd008445fbeced05269e101dd3ca865241c867edd`.
Its canonical stdout SHA-256 is
`bfc2931ff2c67b2fc455ef01f73c1a1ea3bdfaeaedc67d4f2276bc7645878116`.
It exited zero in 9.25 seconds.

## 4. Common claim matrix

| ID | result | exact evidence |
|---|---|---|
| C1 | PASS | `R^T R=I`; the two branch maps have disjoint projector ranges and their adjoint products sum to `I` on both inputs. |
| C2 | PASS | All six sealed generators intertwine both projectors.  The displayed induction composes the relation for every finite word; the record flip is an explicit grammar-changing negative. |
| C3 | PASS | Equality is complete marked onset-incidence isomorphism plus neutral refinement, not name/hash/address equality.  Whole-structure bijections preserve nodes and incidence; RNEW4, RNEW6, and RNEW7 distinguish changes that a label quotient must not erase. |
| C4 | PASS | `Gamma` types possible histories; `rho` alone selects at most one actual history; stability quantifies over licensed continuations.  RNEW2 and RNEW3 realize actual/nonstable and stable/nonactual separately. |
| C5 | PASS | The full `(a,b)` and `(a,b,g)` interfaces are sufficient for their declared futures.  All four direct/cut rows agree.  Projecting to `a` leaves hidden `b` profiles `16/25` and `9/25`, so that native cut refuses. |
| C6 | PASS | The exact four-product contains all four pairs `(stable,complete)=(0,0),(0,1),(1,0),(1,1)`. |
| C7 | PASS | Co-onset dependence is symmetric.  Essential dependence requires unique typed producer provenance, a counterfactual change, covariance, and occurrence entailment.  `U` and `C` commute; `D` consumes all three upstream facts.  No edge is read from word position. |
| C8 | PASS | SCC quotient gives the three-node minimal poset.  In the uniform family every generating dependency raises intrinsic depth and has finite branching, so every fixed comparable interval is finite. |
| C9 | PASS | Unit measure counts nodes of the whole bundle-poset representative.  Two exchanged anonymous nodes still give measure two, while the two raw components inside `{a,b}` give one bundle occurrence. |
| C10 | PASS | Correlated antichain rejects atomic descent despite equal products.  The screened fork and uniform local factors satisfy the strong equalities after the complete typed predecessor assignment. |
| C11 | PASS | Each fresh cell supplies five persistent record components and 16 positive assignments; `n` cells distinguish `16^n` histories.  A fixed capacity collides at a finite `n`; no old sector or port is reused. |
| C12 | PASS | At fixed law, parity changes the relational distribution by `7/25`; `g` changes the later response by `7/25`; the integrated response is `49/625`.  The incidence order stays relational and premetric; the law valuation changes. |
| C13 | PASS | `DECLARED-NEW-LAW-POSTULATE` is explicit in paper, output, receipt, and outcome prerequisite.  No accepted prior law is claimed. |
| C14 | PASS | The candidate expressly leaves actualization, law selection, chronology, dimension, topology, scale, metric, curvature, gravity, continuum, and QFT unconstructed.  Port branching and derived depth are not promoted to geometry. |

## 5. Registered hostile controls H1--H26

Each row below is a semantic reconstruction, not acceptance of the printed
`killed` flag.

| ID | semantic disposition and exact output |
|---|---|
| H1 | KILLED / required non-kill: duplicate label, identical complete onset/support/provenance/future; one marked type and unit measure `1 -> 1`. |
| H2 | KILLED / required non-kill: insert a neutral arrow with zero intermediate record growth; the minimal physical onset and happening count remain one. |
| H3 | KILLED / required non-kill: `UC` and `CU` both end at `{a,b,c}` and one trace class; the quotient has `U || C`, and product-law/measure data are unchanged. |
| H4 | KILLED: the record flip fails the projector intertwiner, so the enlarged grammar contains a possible but nonstable onset type. |
| H5 | KILLED: fixed `a` with hidden `b=0,1` gives future `g=1` profiles `16/25` and `9/25`; the `a` record stays stable while the cut is incomplete. |
| H6 | KILLED: corrupting cached `3` to `4` does not change the recomputed SCC set of cardinality three. |
| H7 | KILLED: two uniform cells require `16^2=256` distinct positive histories; fixed capacity eight collides. |
| H8 | KILLED: at fixed probability `9/25`, the derived formal-log atom is `log(25/9)`, not the hand-inserted `log(25/16)`. |
| H9 | KILLED / controlled change: a two-node antichain keeps the same order and unit measure while changing `p00` from `1/4` to `2/5`; the law valuation may move. |
| H10 | KILLED: a two-node chain and two-node antichain both have unit count two but have respectively one and zero strict order edges. |
| H11 | KILLED: crossing multiplicity two violates exactly-once crossing; no complete frontier/kernel follows. |
| H12 | KILLED: coverage `3/4` leaves positive mass `1/4` omitted, so exhaustiveness fails. |
| H13 | KILLED: weak path products are both `2/5`, but individual factors move; only contextual whole-history surprisal survives. |
| H14 | KILLED: a countably infinite set strictly between fixed endpoints makes that closed interval infinite. |
| H15 | KILLED: without common-boundary transport, two typed record events inhabit different Boolean algebras and their meet/product is undefined. |
| H16 | KILLED: if occurrence of `f` does not entail `e` and neutralizing `e` has no operational effect on `f`, the proposed dependency edge is refused. |
| H17 | KILLED / required carrier-change non-kill: adding a whole-history hash may define an enlarged Markov carrier; it does not alter the native `16/25` versus `9/25` insufficiency. |
| H18 | KILLED: appending coordinates to an intrinsic antichain leaves its intrinsic edge set empty; the coordinate order is quarantined. |
| H19 | KILLED: symmetric `(0,0)->(1,1)` co-creates two raw facts and gives mutual edges, hence one two-component SCC/bundle and no orientation. |
| H20 | KILLED: a two-node structure with a swap automorphism has one node orbit but two occurrence nodes; unit measure is two. |
| H21 | KILLED: the correlated antichain's weak diamond is automatic, while `1/2 != 2/3` and `3/5 != 4/5`; intrinsic atom descent fails. |
| H22 | KILLED / positive control: conditioning on typed root `R` makes all eight screening equalities exact; covariance is `1/45` and branch `(1,1,0)` has mass `3/20`. |
| H23 | KILLED: replacing fresh sectors by eight reusable slots cannot retain the 256 histories already present at two cells, so genuine-growth evidence fails. |
| H24 | KILLED / required non-kill: a sibling permutation is an isomorphism of the complete decorated tree, not node deletion; the product law, order, and multiplicity transport unchanged. |
| H25 | KILLED: the four-product explicitly contains stable/incomplete and nonstable/complete rows, so stability cannot be identified with division. |
| H26 | KILLED: intrinsic depth is a proof grading only.  It does not orient `U || C`, whose serializations share one physical trace and output. |

## 6. Protocol controls N1--N12

| ID | exact independent output |
|---|---|
| N1 | Duplicate complete presentation: classes `1 -> 1`, measure `1 -> 1`. |
| N2 | Persistent exposed bit with omitted hidden future bit: `stable=true`, `frontier_complete=false`, two future profiles. |
| N3 | Three pairwise swap-symmetric co-created facts: three raw components, one mutual-dependence bundle, no orientation. |
| N4 | One arrow versus a neutral two-arrow factorization: no intermediate record increment and one happening. |
| N5 | Incomparable `ef` and `fe`: one physical trace, identical law, unit measure two. |
| N6 | Four persistent binary facts require 16 states; capacity eight collides. |
| N7 | Exhaustive cut crossed twice: crossing count two, exactly-once false, frontier refused. |
| N8 | Chain versus antichain: unit measure two in both, strict edge counts one versus zero. |
| N9 | Fixed antichain order with `p00=1/4` versus `2/5`: unit count fixed, intrinsic/history valuation may change. |
| N10 | Correlated antichain: weak total `2/5`, local factors move, intrinsic descent false. |
| N11 | Screened fork: covariance `1/45`, branch mass `3/20`, all strong squares exact. |
| N12 | Coordinate-ranked antichain: intrinsic edge count remains zero; imported orientation quarantined. |

## 7. New Seat-R controls

These controls are not copied from the registered or fresh tables.  The
zero-meet, actuality-separation, nonneutral-refinement, and cocone-holonomy
controls were already present in the pre-source clean-room freeze; the two
local-coincidence controls were added during the subsequent semantic audit.

| ID | changed mathematical object | exact output |
|---|---|---|
| RNEW1-ZERO-MEET-COMPATIBILITY | Two record events each have probability `1/2`, but their common-boundary meet has probability zero. | Both components are individually possible; the family is not compatible and earns no joint happening event. |
| RNEW2-ACTUAL-NONSTABLE | `rho` selects a history containing an onset, while the declared grammar also licenses a later eraser. | `actual=true`, `stable=false`; actual occurrence does not imply stable fact. |
| RNEW3-STABLE-NONACTUAL | A possible onset has probability `1/2` and persists under every licensed continuation, but the selected history omits it. | `stable_type=true`, `actual=false`; stable possibility does not imply actuality. |
| RNEW4-NONNEUTRAL-REFINEMENT | A proposed factorization creates one intermediate semantic record and changes a later probability from `1/3` to `2/3`. | The factorization is nonneutral and may not be quotiented away. |
| RNEW5-COCONE-HOLONOMY | Two transports to one common future send the same record key to distinct keys `r0` and `r1`. | Path independence fails; the compatible meet and presentation-independent occurrence are undefined. |
| RNEW6-STATE-LOCAL-COINCIDENCE | Two onsets have the same source and target record sets but later probabilities `1/3` and `2/3`. | They are different onset germs; state-local coincidence is insufficient identity. |
| RNEW7-SUPPORT-COLLISION | Equal payloads occur at distinct essential supports `left-port` and `right-port` with different producer provenance. | Occurrence count is two; a payload/type quotient must not delete support multiplicity. |

RNEW2 and RNEW3 directly test the possible/actual/stable ontology.  RNEW4,
RNEW5, RNEW6, and RNEW7 directly test the primary whole-referent lens.

## 8. Source, result, receipt, and runtime audit

The independent verifier confirmed:

```text
normalized payload SHA-256 292b9c9dad12785cdb0b233a7d56237500fd716e38b740ad3772a1f6969e8ecf
receipt-core SHA-256       0d71fd0eed5a2fe399fc7b6f9321c46c91b06e03c68f878dd626407175937914
scientific top-level seals 17/17 exact and total
receipt-core field seals   9/9 exact
fresh cases                6/6 independently recomputed
registered attacks         26/26 semantically disposed above
uniform finite rows        38/38 independently reconstructed
```

The output and receipt are canonical JSON with one final LF.  Every receipt
input hash, output byte count/hash, payload hash, core hash, and per-key seal
recomputed exactly.

Permitted black-box selftests gave:

| environment | exit | wall time | canonical stdout SHA-256 |
|---|---:|---:|---|
| repository root | 0 | 9.69 s | `36bda0de588ce4ffdd37b549b581a1b436466f4351e6ddd5714c857a789110d2` |
| alien current directory | 0 | 12.09 s | same |
| true one-file/no-`.git` copy | 0 | 11.83 s | same |

Named referent controls H1, H2, H19, H20, and H24 each exited zero in under
10 seconds.  The deliberate calibration mutation exited one with
`SCIENTIFIC-FAILURE: DELIBERATE-ANCHOR-FAILURE`.  No official publication
mode was invoked.

## 9. Referent and ontology decision

### Onset equality

The marked onset includes the typed source/arrow/target and every new semantic
record event, minimal relational support, and producer provenance, all
relative to the one complete declared law and continuation grammar.  Equality
is not a state-pair or label test.  RNEW6 shows why the future law must be in
the ambient complete structure; RNEW7 shows why equal payload is insufficient.

### Refinement and multiplicity

Only identity/refinement arrows with no new semantic record and no changed
future law descend.  Whole-structure isomorphisms are bijective on incidence
nodes, so they preserve cardinality even when pointed occurrence types share
one orbit.  The minimal `{a,b}` bundle has two record components but one
bundle occurrence; two exchange-symmetric sibling bundles remain two bundle
occurrences.  These are different quotients and the candidate keeps them
different.

### Bundles and dependency

Symmetric components of one minimal nonfactorizable onset receive both raw
dependency directions and hence one SCC.  No representative is chosen.
Essential producer edges require semantic provenance plus counterfactual
effect and occurrence entailment, so serialization and accidental
correlation do not create order.  The quotient-poset proof is standard and
well typed.

### Actuality

`Gamma` supplies possible-history weights only.  `rho` is an external
selection postulate.  Stability is an all-licensed-future property of a
possible type; an actual stable fact is an occurrence of that type in the
selected history.  RNEW2 and RNEW3 show both nonimplications explicitly.

### Geometry wall

The constructed relation is dependency order, not chronology.  Rooted-tree
incidence is intrinsic relational data, while addresses, sibling order, and
derived rank are presentation/proof data.  Unit and descended `Gamma` weights
are event measures, not spatial volume or duration.  Nothing licenses Paper
15 geometry without a later ensemble, correspondence, calibration, and
convergence theorem.

## 10. Outcome dependency chain

The declared law and its provenance are primitive.  The stable-word theorem
uses only exact writer completeness, sector orthogonality, generator
intertwining, and induction.  Onset identity then quotients complete marked
structures, after which operational dependency and its SCC quotient give
bundle posets.  Finite branching plus intrinsic dependency depth gives local
finiteness.  Unit measure counts bundle occurrences.  Unequal weights enter
only after strong typed-diamond descent.  Frontier coordinates are computed
separately and do not feed back into stable identity.  No downstream
calculation repairs an upstream referent failure; none was found.

## 11. Scope walls

The accepted ceiling is limited to the declared abstract model.  In
particular:

- no history is selected by `Gamma`;
- no fundamental law is derived or selected;
- no universal grammar or universal division doctrine is claimed;
- dependency is not yet chronological or spacetime-causal order;
- unit count and intrinsic surprisal are not calibrated volume or time;
- no topology, dimension, signature, scale, metric, connection, curvature,
  stress-energy, entropy, gravity, GR, continuum, or QFT object exists; and
- stable happenings, their quotient, growth, and valuation are ISP proposals,
  not attributions to Barandes.

## 12. Bounded fixes

1. The abstract says “a stable happening is an actual occurrence,” while the
   later term table and construction also use “stable happening type” for a
   possible persistent onset class.  The literal repair is: “A stable-
   happening type is a possible onset class whose record persists under every
   licensed continuation; relative to `rho`, a stable happening is an actual
   occurrence of such a type.”
2. The opening tuple uses one symbol for stable fact occurrences while the
   uniform family is first a possible shape/history schema.  The literal
   repair is to write `E_T^poss` for a possible incidence structure and
   `E_{omega_*}^act` for the occurrence set in a selected history.  The
   existing conditional-actuality coordinate then remains unchanged.
3. The registered mutant rows are compact schematic certificates, not by
   themselves complete semantic proofs of whole-structure descent.  They are
   acceptable here only because the analytical definitions and the
   independent H/N/R reconstructions above discharge the mathematical
   controls.  The adjudication should describe those rows as sealed control
   summaries rather than as stand-alone referent constructions.

None of these fixes changes the accepted object or requires a retuned law.

## 13. Report hash convention

The ordinary SHA-256 is reported externally after the file is frozen.

For the normalized self-hash, take these exact UTF-8/LF bytes and replace the
64 lowercase hexadecimal characters following `Normalized self-SHA-256:` on
the next line with 64 ASCII zeroes, leaving every other byte unchanged, then
apply SHA-256.

```text
Normalized self-SHA-256: af8dac38a543c4362c01f93b4771aa576d90a95a5282b1bbe8754304410cc5c1
```
