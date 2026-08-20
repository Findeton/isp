# Paper 14 hostile review — Seat O: dependency, order, and valuation

Date: 2026-08-20
Seat: O
Grade: **REJECT**
First exact scientific counterexample: **whole-history presentation quotient versus the 16-row reciprocal law**, Section 3 below
Earliest affected product coordinate: **the law/referent prerequisite `P14-DECLARED-POINT-FREE-HISTORY-LAW`**; consequently the claimed intrinsic `Gamma` valuation does not descend
Highest independently surviving Seat-O coordinates: **`P14-LOCALLY-FINITE-BUNDLE-POSET` and `P14-UNIT-COUNTING-MEASURE`**
normalized_self_sha256: d34a8287a935fa402e4919b88bc68c031682175316ea5dcc9894024aa89d0971

The normalized self-hash convention is: replace the 64 lowercase hexadecimal
characters after `normalized_self_sha256:` by 64 ASCII zeroes, change no other
byte, and take ordinary SHA-256 of the complete UTF-8 file. The ordinary file
SHA-256 is recorded externally after freeze.

## 1. Authentication and review order

I authenticated repository `HEAD` as
`ed258111d2ff604de97816266be2184fd1d06c63` and the complete hostile protocol
as
`7eba533fea4bb96370ed27aa46f9f6c933b207317495d9a4955c7868f89f5fed`
before scientific work. The frozen inputs independently matched:

| object | ordinary SHA-256 |
|---|---|
| result-neutral pin | `0dc92112e5db39bb9e1a8c51a018119e783f347505d3e5bf03debf47fe31ef44` |
| source | `1a1d9a7acc3ef4ba62a9e9b0f6101263dde3b72dd9d407918ea0be653d5d628e` |
| paper | `ffc3dca2863bf9f36c9fe62e8dff80628c59c8837b3d96006e449329dee05ec1` |
| construction note | `e6d59fd49e5af805df96f8b3a4c2db5676dafaa3c552ecadb0779ca690887253` |
| fresh cases | `4f5d8d21bb66d5e7c41a9c34a35a26ec955b03497d9682564efd23df681126c7` |
| official output | `95a38ebbb6d2e9c85c2a2f66ca3275fd1f4205761dfcc5eae6a1d9ea2b233993` |
| official receipt | `2d320edc0eb152d5fcb6ffdf1444e8071d9466c5773c13be51ad438036c2fa4c` |
| verification note | `c8aec2ef51008d5a80637ce4bca74e1bd984d7f6a23e1491a85f30eed9233dc4` |

The pin and paper were read completely. Before the source, construction note,
fresh cases, output, receipt, or verification note were inspected, I froze an
off-tree reconstruction from the pin and paper alone. It reconstructed the
writer, minimal history, reciprocal law, four-product frontier family,
correlated and screened diamonds, rooted-tree counts, growth formulae, and
five presource attacks. Only afterward did I inspect implementation evidence
and invoke public CLI modes as black boxes. The candidate source was never
imported by either independent reconstruction.

The source-freeze and official-result commits named by the protocol are
ancestors of authenticated `HEAD`. No corpus-integrity discrepancy was found.

## 2. Independent reconstruction summary

The exact writer uses

\[
R=\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix},\qquad
B=R\odot R=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\]

In the four-dimensional output carrier, `V_0` has the first output row equal
to the first row of `R`, `V_1` has the fourth output row equal to the second
row of `R`, and all other rows vanish. Thus
`V_0^T V_0 + V_1^T V_1 = I_2`. The record-sector projectors satisfy
`P_r V_s = delta_rs V_s`. Each sealed future is
`F_k = I_2 tensor R^k`, `k=0,...,5`; it commutes with both record projectors,
and the two transported branches stay orthogonal. The record flip
`X tensor I_2` fails the intertwining relation.

Independent enumeration gives five states, seven words
`epsilon,U,C,UC,CU,UCD,CUD`, and five trace classes after `UC ~ CU`. The raw
dependency closure has edges

\[
a\leftrightarrow b,\qquad a\to d,\qquad b\to d,\qquad c\to d,
\]

so its mutual-dependence quotient is exactly
`({a,b},{c},{d})` with `{a,b}<{d}`, `{c}<{d}`, and
`{a,b} || {c}`. Both diamond serializations reach `{a,b,c}`.

The reciprocal law

\[
\Gamma(a,b,g,y)=\frac14 B_{g\mid a\mathbin\oplus b}B_{y\mid g}
\]

has 16 positive labeled rows and total one. Direct/cut reconstruction gives,
in `(parity,y)` order `(0,0),(0,1),(1,0),(1,1)`,

\[
337/625,\quad 288/625,\quad 288/625,\quad 337/625
\]

on both sides. The hidden `g=1` profiles at fixed exposed `a` are `16/25`
and `9/25`; the local residuals are `7/25,7/25` and the integrated residual
is `49/625`. The four logical stable/unstable by complete/incomplete cases are
all realized.

The correlated-antichain branch `(0,0)` has weak products
`(1/2)(4/5)=(3/5)(2/3)=2/5`, while its individual factors move. The screened
fork reconstructs eight positive histories, covariance `1/45`, the example
probability `3/20`, and all eight strong screening rows.

For the published labeled presentation, I independently generated every one
of the 38 finite uniform rows. The rooted-shape counts for `n=1,...,4` are
`(1,1,1,1)` at `q=1`, `(1,1,2,3)` at `q=2`, and `(1,1,2,4)` at `q=3`.
Every local 16-entry kernel is positive and normalized; reverse-leaf
elimination proves every finite labeled product normalized. Bundle and raw
record counts are `4n` and `5n`. Section 3 explains why the printed `16^n`
count is a labeled-presentation count rather than the declared physical
whole-history count.

All six fresh objects were reconstructed directly from their raw parameters:
profiles `2/7,5/7`; correlated joint `1/10,2/10,3/10,4/10`; the screened
`2/5,3/5` root fork; capacity `100 < 4^4=256`; the three-item presentation
permutation; and the SCC `({u,v},{w},{z})`. Their aggregate exactly matches the
official object.

## 3. First decisive counterexample: the probability law does not descend to the declared physical history quotient

This failure uses the candidate's own presentation groupoid and positive law;
it is not a label clone, node-orbit count, malformed input, or implementation
edge case.

The paper declares that the physical history is the isomorphism class of the
complete incidence-and-value structure, and that the presentation groupoid may
exchange the two incomparable matter bundles `A` and `B`. On one reciprocal
cell the group action is therefore

\[
\tau(a,b,g,y)=(b,a,g,y).
\]

Among the 16 printed rows, the eight rows with `a=b` are fixed and the eight
rows with `a!=b` form four two-element orbits. The physical whole-history
quotient consequently has

\[
8+8/2=12
\]

incidence-and-value classes, while still retaining two root bundle
occurrences. This is quotienting whole presentations; it is not the forbidden
operation of replacing two physical nodes by one node orbit.

There are only two ordinary probability choices, and neither is the claimed
object:

1. Because `Gamma` is invariant under `tau`, assign each physical class its
   representative's printed probability. The fixed (`a=b`) classes carry
   total mass `1/2`; one representative from every off-diagonal pair carries
   total mass `1/4`. The purported physical law normalizes to `3/4`, not one.
2. Push the labeled probability forward to physical classes. This normalizes,
   but each off-diagonal class has twice the printed probability. For
   `(a,b,g,y)=(0,1,0,0)`, the printed row is `36/625`, whereas the physical
   orbit has probability `72/625`.

The same obstruction appears before `G` and `Y`. The physical unordered fair
root-pair law is

\[
P\{0,0\}=1/4,\qquad P\{0,1\}=1/2,\qquad P\{1,1\}=1/4.
\]

Any positive atom factors forced by the equal pairs obey
`q(0)^2=q(1)^2=1/4`, hence `q(0)=q(1)=1/2`; their mixed product is `1/4`, not
the physical mixed-class probability `1/2`. Equivalently, on every
off-diagonal complete history the printed sum of local surprisals differs from
the pushforward whole-history surprisal by `log 2`. The presentation
multiplicity is contextual to the complete orbit, so it cannot be an intrinsic
weight of either incomparable occurrence.

Consequences:

- the 16-row object is a normalized law on labeled presentations, not the
  declared normalized law on physical whole-history classes;
- the advertised `16^n` physical-history count already fails at `n=1`
  (`12`, not `16`) and receives further orbit corrections on symmetric graft
  shapes;
- strong diamonds in a chosen labeled representative do not by themselves
  prove descent of `Gamma`-surprisal atoms through the whole-history groupoid;
- the locally finite occurrence poset, its multiplicities, and unit counting
  measure are unchanged.

This changes a scientific prerequisite and defeats the proposed point-free
law/intrinsic-valuation product. It is therefore a rejection rather than a
certificate-only fix.

## 4. Common claim matrix C1--C14

| ID | disposition | exact evidence |
|---|---|---|
| C1 | **PASS** | The independently reconstructed `V_0,V_1` give `V_0^T V_0+V_1^T V_1=I_2`; all four `P_r V_s=delta_rs V_s` branch/sector rows hold. |
| C2 | **PASS** | Every `F_k=I_2 tensor R^k`, `k=0,...,5`, commutes with both `P_r`. Closure under multiplication proves every finite sealed word; the record flip fails. |
| C3 | **FAIL** | Onset and bundle identity are correctly whole-structure based, but the declared whole finite law does not follow that identity: `A<->B` turns 16 labeled rows into 12 physical history classes, with normalization/factor descent failure as in Section 3. |
| C4 | **PASS** | `Gamma` governs possible histories; only external `rho` can select an actual history; stability is a transport property and is never used as actuality. |
| C5 | **PASS** | All four direct/cut rows are exactly `337/625,288/625,288/625,337/625`; the full `(a,b)` and `(a,b,g)` frontiers are sufficient in the declared reciprocal grammar. The quotient issue does not change parity-conditioned future kernels. |
| C6 | **PASS** | Exact four-product: stable-complete, stable-incomplete, nonstable-complete, nonstable-incomplete. No implication between coordinates is used. |
| C7 | **PASS** | Producer edges require unique typed provenance, counterfactual influence, covariance, and entailment. `UC` and `CU` have one physical trace. Mere appearance order, rank, and perfect correlation are excluded. |
| C8 | **PASS** | SCC quotient is `({a,b},{c},{d})` with edges `0<2,1<2`. In the uniform family dependency depth strictly increases and out-degree is finite at fixed `q`, so every closed interval is finite. |
| C9 | **PASS** | Unit measure counts nodes of the whole bundle-poset structure after mutual-dependence quotient. One `{a,b}` onset is one bundle; two anonymous incomparable siblings remain two occurrences even when exchanged by an automorphism. Additivity is asserted only for disjoint regions. |
| C10 | **FAIL** | Strong factors descend in the labeled product, but not through the declared whole-history quotient. The unordered fair root pair has masses `1/4,1/2,1/4`, inconsistent with occurrence-only factors; off-diagonal surprisal has a contextual `log 2` orbit term. |
| C11 | **FAIL** | Fresh bundle/record sectors and unbounded carrier growth are genuine, but the exact evidence `16^n` physical histories is false under the required presentation quotient: one cell has 12 physical classes. Thus the claim's published whole-family history certificate is not exact, although fixed-memory obstruction and growth survive. |
| C12 | **PASS** | In the accurate premetric sense, parity changes the valuation/relational response (`16/25` versus `9/25`) and `g` changes the later response, with integrated residual `49/625`. The underlying Hasse order does **not** change, and the paper does not promote the response to geometry. |
| C13 | **PASS** | Every law-relative construction is explicitly marked `DECLARED-NEW-LAW-POSTULATE`; no inherited or selected law is claimed. Provenance honesty does not cure the descent failure. |
| C14 | **PASS** | Dependency is not chronology; count is not volume; depth is not proper time; `q` is not dimension; no topology, signature, metric, curvature, stress-energy, entropy, gravity, continuum, or QFT is promoted. |

## 5. Semantic dispositions H1--H26

Each row below is a reconstruction of the changed mathematical object, not an
acceptance of the printed `killed` flag.

| ID | semantic disposition | reconstructed effect |
|---|---|---|
| H1 | **KILLED / required non-kill** | A label clone with identical support, provenance, event, and future has one occurrence class; unit measure remains `1`. |
| H2 | **KILLED** | A neutral two-arrow split with zero intermediate record growth remains one onset/happening. |
| H3 | **KILLED / required non-kill** | `UC` and `CU` reach `{a,b,c}`, have one trace, one law, one dependency output, and equal measure. |
| H4 | **KILLED** | Adding `X tensor I_2` changes the grammar; it does not commute with `P_0`, so the record theorem no longer applies. |
| H5 | **KILLED** | Stable exposed `a` remains stable, while hidden `b` moves the `g=1` profile between `16/25` and `9/25`; native frontier incomplete. |
| H6 | **KILLED** | Recomputed SCC bundle count is `3`, independent of a corrupted cached value `4`. |
| H7 | **KILLED, evidence qualified** | Fixed capacity `8` still collides by two cells even after the presentation quotient; the printed `256` is a labeled count and is not valid physical evidence. Fresh persistent sectors nevertheless give more than eight physical histories. |
| H8 | **KILLED** | At fixed probability `9/25`, changing the formal reciprocal from `25/9` to `25/16` is not `Gamma`-derived. |
| H9 | **KILLED** | The same two-node antichain supports `p00=1/4` or `2/5`; order and unit count stay fixed while law valuation moves. |
| H10 | **KILLED** | Chain and antichain each contain two occurrences, but only the chain contains a strict relation. |
| H11 | **KILLED** | Crossing multiplicity `(2,1)` violates exactly-once even if coverage is exhaustive; cut-cell probabilities overcount. |
| H12 | **KILLED** | Covered mass `3/4` omits positive mass `1/4`; exhaustiveness fails separately. |
| H13 | **KILLED** | Correlated antichain has equal weak products `2/5` but factor pairs `(1/2,4/5)` and `(3/5,2/3)`; only history surprisal survives. |
| H14 | **KILLED** | A fixed interval containing a countably infinite chain directly violates local finiteness; finite prefixes do not save it. |
| H15 | **KILLED** | Without transport to one common Boolean boundary, a multi-record meet/product is untyped. |
| H16 | **KILLED** | An edge with neither event entailment nor calibrated intervention effect is refused by both producer gates. |
| H17 | **KILLED / enlarged-carrier non-kill** | A complete-past hash changes the carrier/source type and cannot retroactively make the native `a` projection sufficient. |
| H18 | **KILLED** | Coordinates can orient an antichain only by imported structure; intrinsic relation stays empty. |
| H19 | **KILLED** | Swap-symmetric `(0,0)->(1,1)` has two raw facts but SCC `{a,b}` and one mutual-dependence bundle. |
| H20 | **KILLED** | An automorphism exchanging two anonymous nodes preserves two occurrence nodes; node-orbit counting is rejected. Section 3 instead quotients complete decorated presentations and does not collapse nodes. |
| H21 | **KILLED** | Weak chain-rule equality alone leaves local factors context dependent; no intrinsic atom allocation. |
| H22 | **KILLED / positive control** | Conditioning on typed root `R` screens `A,B`; all eight strong rows pass, covariance remains `1/45`, and `(1,1,0)` has probability `3/20`. |
| H23 | **KILLED, evidence qualified** | Replacing fresh sectors by finitely reusable slots forces a finite collision. Linear `4n,5n` occurrence/record growth is enough; the separate printed `16^n` physical-history formula is not. |
| H24 | **KILLED / required non-kill** | Shape reordering and pointwise `A/B` relabeling preserve the labeled kernel and incidence. This covariance is real but does not establish normalized probability on whole-history isomorphism classes. |
| H25 | **KILLED** | The exact four-product contains both stable-incomplete and nonstable-complete cases, so `stable implies division` is false. |
| H26 | **KILLED** | Dependency depth is a proof rank only. Opposite serializations of incomparable events have the same trace, so rank/list order cannot become physical time. |

## 6. Mandatory new controls N1--N12

| ID | exact reconstructed output | disposition |
|---|---|---|
| N1 | Duplicating a complete onset row while preserving its transported event, support, provenance, and full future profile changes presentation multiplicity `1->2` but physical occurrence count and `mu_1` stay `1`. | Required non-kill. |
| N2 | At exposed stable `a=0`, hidden `b=0,1` gives `P(g=1)=16/25,9/25`. | Stability passes; frontier refuses. |
| N3 | For the fully `S_3`-symmetric onset `(0,0,0)->(1,1,1)`, mutual edges form one SCC `{a,b,c}`. Raw fact count `3`, bundle count `1`; no invariant orientation exists. | Three-way bundle positive control. |
| N4 | Replacing `o` by `identity; o` with zero intermediate record increment leaves the minimal onset class and unit count at `1`. | Neutral-refinement non-kill. |
| N5 | Independent insertions `X,Y` give `XY(empty)=YX(empty)={x,y}`; both serializations have one trace and unit measure `2`. | No hidden clock. |
| N6 | Six independently persistent binary records require `2^6=64` states; a dormant carrier of `32` states collides. | Finite-memory refusal. |
| N7 | With histories of mass `1/2,1/2`, let frontier cell `F_1` contain both histories and `F_2` contain the first. Coverage is exhaustive, but crossings are `(2,1)` and cell masses sum to `3/2`. | Exactly-once refusal separate from exhaustiveness. |
| N8 | A two-node chain and two-node antichain both have `mu_1=2`; relation counts are `1` and `0`. | Valuation equal, order unequal. |
| N9 | On one fixed two-node antichain, uniform `p00=1/4` and the strictly positive correlated law `p00=2/5` leave `mu_1=2` fixed. | Law valuation can move while order/unit measure do not. |
| N10 | Correlated law `(2/5,1/10,1/5,3/10)` has weak products `2/5` in both orders, but local factors move as `(1/2,4/5)` versus `(3/5,2/3)`. | Contextual history weight only. |
| N11 | The typed screened fork has eight positive histories, covariance `1/45`, example branch `3/20`, and all eight strong equalities. | Intrinsic-weight positive control on a typed labeled poset. |
| N12 | Adding ranks `(0,1)` to an intrinsic two-node antichain produces a total order exchanged by the node swap; the intrinsic relation remains empty. | Imported structure quarantined. |

## 7. Additional independently invented controls

These are separate from the registered and fresh tables. Controls O1, O4,
and O6 are primary-lens attacks; O1 and O4 are required non-kills.

| ID | changed object and exact output | disposition |
|---|---|---|
| O1 — SCC representative | Raw edges `a<->b,a->d` imply `b->d` in transitive closure. Using `a` or `b` as representative produces the same quotient edge `{a,b}<d`. | Required non-kill; quotient well defined. |
| O2 — three-way hidden dependence | Set `p(a,b,c)=1/8(1+(1/2)(-1)^(a xor b xor c))`: even parity rows are `3/16`, odd rows `1/16`; every pair marginal is uniform `1/4`, but `P(A=0|C=0)=1/2` and `P(A=0|B=0,C=0)=3/4`. | Testing only base pair diamonds is insufficient; the full ideal-lattice strong test correctly refuses. |
| O3 — overlap additivity | For bundle regions `A={U,D}`, `B={C,D}`, `mu(A)=mu(B)=2`, `mu(A union B)=3`, and `mu(A intersection B)=1`. | Only disjoint additivity may be used; no candidate overclaim found. |
| O4 — three-event trace | Three completely commuting onsets have all six serializations `XYZ,XZY,YXZ,YZX,ZXY,ZYX` and one final incidence/law/measure object. | Required non-kill; pairwise trace swaps must generate the full `S_3` class. |
| O5 — zero support | A factorized binary law with probabilities `(1/2,0,0,1/2)` keeps a valid two-occurrence unit measure, but `-log q` is not finite on null branches. | Strict positivity is necessary; unit measure survives. |
| O6 — whole-history groupoid descent | `A<->B` gives 12 physical classes from 16 labeled rows. Representative mass is `3/4`; pushforward mass is one but maps `36/625` to `72/625` off diagonal; unordered root mass `1/2` disagrees with atom product `1/4`. | **Decisive counterexample:** point-free `Gamma` law and intrinsic atom weights do not simultaneously descend. |

## 8. Source, result, receipt, and runtime reconstruction

The independent verifier reproduced, without importing the source:

- all matrices, six generators, four projector/branch rows, and eraser failure;
- the complete five-state/seven-word/five-trace frame and SCC quotient;
- all 16 reciprocal rows, all four direct/cut rows, hidden profiles, and the
  stability/frontier four-product;
- the complete correlated and screened laws;
- all 12 rooted-shape census entries and all 38 finite uniform labeled rows;
- all six fresh objects from raw parameters;
- the old/new canonical preimage hashes, evidence, and dispositions for all
  H1--H26;
- canonical output and receipt bytes, five input identities, all 17 scientific
  seals, all nine receipt-core seals, normalized payload hash, and receipt-core
  hash.

Exact reconstructed aggregates are:

| object | SHA-256 |
|---|---|
| normalized payload | `292b9c9dad12785cdb0b233a7d56237500fd716e38b740ad3772a1f6969e8ecf` |
| receipt core | `0d71fd0eed5a2fe399fc7b6f9321c46c91b06e03c68f878dd626407175937914` |
| measurements | `962340352d502c8e5a8056c57dcb7df559543cef5741607b8863beb3c802d2f0` |
| registered attacks | `fd593caf97a61e3ee4572295dccd25e72c15eed13c08f87eed4819bf9c2ad23f` |
| fresh aggregate | `c47fc41ee44b1434e2e51d2b936863b7091e77eecd81012294f079bcd6e24abd` |

Black-box source runs after the clean-room freeze gave:

- repository-CWD `--selftest`: RC `0`, about `11.64 s`;
- alien-CWD absolute-source `--selftest`: RC `0`, about `14.80 s`;
- deliberate `--anchor-failure-selftest`: RC `1` with exact message
  `SCIENTIFIC-FAILURE: DELIBERATE-ANCHOR-FAILURE`;
- nine selected public mutant modes covering the Seat-O lens: every RC `0`
  and each printed its expected semantic disposition.

The official bytes and seals are internally exact. The rejection is therefore
semantic: the faithfully reconstructed artifact certifies a labeled
presentation law that is not the paper's declared physical quotient law.

## 9. Product outcome and ontology audit

The dependency construction itself survives. Essential producer edges are
supported by typed entailment and operational neutralization; mutual SCCs
remove false orientations; incomparable operations commute under trace
reserialization; finite branching plus strictly increasing dependency depth
proves local finiteness for the uniform direct limit. The proof rank is not an
execution order.

The unit measure also survives. It counts occurrence nodes of the complete
unlabeled bundle poset, not raw record components, printed rows, labels, or
node orbits, and it is additive on disjoint physical regions. This supports the
lower Seat-O product

```text
dependency = P14-LOCALLY-FINITE-BUNDLE-POSET
valuation  = P14-UNIT-COUNTING-MEASURE
```

The intrinsic `Gamma` coordinate does not survive. Contextual whole-history
surprisal remains meaningful after a physical quotient law is specified, but
the candidate's labeled local factors acquire presentation-orbit multiplicity
terms on the declared whole-history classes. Thus the strongest supported
valuation is unit counting, not
`P14-INTRINSIC-GAMMA-ATOMIC-WEIGHT` or its claimed interval-finite weighted
extension.

Stable happening and complete division frontier remain logically independent.
The full reciprocal frontiers retain their sufficiency, while a projected
stable record remains incomplete. `rho` is still external; positivity does not
actualize a history. The reciprocal residuals remain a law-relative,
pregeometric response and do not change the underlying bundle order.

No chronology, causal cone, topology, dimension, signature, scale, spatial
volume, proper time, metric, connection, curvature, stress-energy, entropy,
gravity, GR, continuum, or QFT follows. In particular, neither unit count nor
any contextual orbit-corrected surprisal is a spacetime volume without a later
independent calibration theorem.

## 10. Verdict

**REJECT** the proposed full product as frozen. The earliest failure is the
presentation-independent law/referent prerequisite: the normalized 16-row law
is on labeled presentations, whereas the paper declares complete physical
histories to be whole incidence-and-value isomorphism classes. Its natural
physical pushforward changes history probabilities and destroys the claimed
intrinsic atom-factor equality.

This rejection does not erase the independently supported lower result:
presentation-invariant bundle multiplicity, the locally finite dependency
poset, complete/incomplete frontier distinctions, reciprocal conditional
response, and unit occurrence measure all survive. The first decisive exact
counterexample is O6; no earlier corpus-integrity or arithmetic discrepancy
was found.

## 11. Private artifacts

| private artifact | ordinary SHA-256 |
|---|---|
| `/private/tmp/p14_seat_o_cleanroom.py` | `e20070a87ca7c5cc70398072401c44323f953bdce9301dd244398b4a4e2fc64f` |
| `/private/tmp/p14_seat_o_cleanroom.json` | `de225b53e15cca4aa77cc65195a2847a4699d3a6e93cb19e529780c64981d095` |
| `/private/tmp/p14_seat_o_independent_verify.py` | `95a2c42813de583883b3420980ecd569085994e573c9520c0e593c9f846aa2dc` |
| `/private/tmp/p14_seat_o_independent_verify_result.json` | `54f80e68bf4d1fbf3bae06fad8f996ddaef7240a93ada6b7cbaac60b80db2ab7` |
| `/private/tmp/p14_seat_o_groupoid_probability_countermodel.py` | `d0b68f2eb8802745cb636fcb684caf36179b434c10c503a7829fb84e8d08a7e4` |
| `/private/tmp/p14_seat_o_groupoid_probability_countermodel.json` | `78c7654c922dc78fcf2de9b44b2e835ca446ac2e530ce2f9ce2af150e6d96719` |
