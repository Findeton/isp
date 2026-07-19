# Paper 30 — round 1 hostile review (paper-level)

**Object:** `v10/relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md`
(1,088 lines, LOG #323, HEAD 36bb7aa).
**Standard:** paper review, not receipt review — number fidelity against the
seven committed terminal `.out`s (or, where the paper says so, the committed
LOG/pin record); claim fidelity against the terminal receipts plus the
adjudicated amendments of the nine rounds; single-threaded style with
amendment-shaped qualifiers required IN the statements; §1.1 inherited-demand
honesty against papers 25/28/29 and the d41d receipt; completeness; prose.
**Sources driven:** `v10/data/d42{a,b1,b2,b3,b4,b7,b56}_*.out` (all seven read
in full), LOG #274–#323, the frozen reviews (d42a, d42b1–b4, b7, b56 rounds +
deltas), pins `note-d42*.md` with amendments, papers 20/25/26/27/28/29, the
d41d repair receipt `.out`, v6 paper 1. Every quantitative claim in the paper
was extracted and checked; the sweep table is §4 below.

**Verdict: 0 BLOCKER / 4 MAJOR / 10 minor / 5 nit.  Zero false numbers —
the campaign's streak survives its own paper.  All four MAJORs are
statement-level (scope, formalism, attribution, paraphrase), none numerical.**

---

## 1. MAJOR findings

### F1 — MAJOR (CONFIRMED): the ladder is stated unscoped in the abstract and
### in the §4.1 A7' box, while the paper's own §4.4 declares the general-depth
### ladder FALSE

The adjudicated scope is explicit in the terminal receipt:

> d42b1 `.out` G9: "the ladder IN-FAMILY AT CAPS (C1 re-scope: a
> general-depth ladder theorem is OPEN, d42b3's constraint set)"
> d42b1 `.out` N1: "the general-depth ladder is FALSE under current pricing"

and in LOG #303/#305 (h12 pinned as a completion constraint; "the
general-depth ladder FALSE under current pricing").

The paper, abstract:

> "it forces an honest support-level face of the placement problem:
> per-initiator weight sums sit on the exact quarter-integer ladder
> `1 + k/4`, where `k` counts causally blind join layers."

— unqualified.  And §4.1's boxed law:

> "**A7' (the ladder).**  A per-initiator weight sum at a record point
> equals `1 + k/4`, where `k` counts the additional join components the
> pinned law prices for that initiator beyond its own view."

— unqualified over "a record point."  h12 is an admissible record point of
the grammar (d42b1 N1: "h12 = h11 + one admissible proposal") with a
per-actor sum of `23/24`, which is not of the form `1 + k/4`.  The boxed A7'
is therefore refuted by the paper's own §4.4 ("The general-depth ladder is
therefore *false under current pricing*").  §1.4 and §4.4 carry the caveat;
the abstract and the boxed statement — the two places a referee reads first —
do not.  This is precisely the round-hazard class "the ladder without its
in-family-at-caps scope," and it is also the campaign's founding conviction
class (claims wider than computation) recurring at the paper level.

**Repair (exact text).**  Abstract: "…per-initiator weight sums sit on the
exact quarter-integer ladder `1 + k/4` at every record point of the
enumerated families (and on the constructed deep exhibits h5/h11), where `k`
counts causally blind join layers; one constructed configuration (h12) lies
off the ladder, and the general-depth ladder is false under current pricing —
its reconciliation is carried to the completion problem."  §4.1 box: append
to A7' the scope clause "— at the record points of the enumerated families
(in-family at the declared caps; §4.4 exhibits the off-ladder h12
configuration, and the general-depth ladder is false under current
pricing)."

### F2 — MAJOR (CONFIRMED): §5.1's completion definition makes demand (b)
### vacuous, and §5.2's "forces Z = N" does not typecheck under §5.1's own
### transfer — the paper re-imports a piece of the ill-posedness that was
### d42b3's round-1 BLOCKER

§5.1 defines:

> "A **placement completion** is strictly positive cut data `Z` with the
> transfer `q'(e|h) = q(e|h) . Z(h+e) / Z(h)`, required to be (a) per-cut
> normalized … and (b) foliation-invariant (equal chain products over all
> linear extensions of every history)."

Under this transfer, chain products telescope to `mu(H) · Z(H)/Z(empty)`,
which — given the gated factor invariance (G1) — is equal across all linear
extensions for **any** `Z` that is a function of the cut, exactly as the
adjudicating referee computed:

> d42b3 round-1 review, class (c): "Chain products telescope to
> mu(H) * Z(0)/Z(H) — extension-invariance is AUTOMATIC for any Z; the
> entire content moves to per-cut normalization."

So for "cut data" `Z`, (b) as printed is vacuous, and the trilemma's second
leg carries no load in the paper's own formalization.  (The leg's real
content, per the record and per the paper's own §5.5, is
**class-constancy** — a sequence-attached `Z` breaks the diamond check at 51
diamonds — but §5.1 forecloses that reading by declaring `Z` cut data
up front.)

§5.2 then derives:

> "If `q'` must preserve within-cut ratios, then `Z(h+e)/Z(h)` is constant
> across the candidates at `h`, and per-cut normalization forces `Z = N`,
> the frontier sum."

Under §5.1's transfer, ratio preservation plus (a) forces
`Z(h+e)/Z(h) = 1/N(h)` — a constraint on `Z`'s *increments*, whose global
unsolvability (no cut function has those increments; 36/202 diamonds) is the
theorem.  "`Z = N`" is the conclusion of the **divisor** formalism, which is
how the adjudicated computation actually posed the class:

> d42b3 round-1 review, class (b): "A per-cut uniform divisor with
> Sigma_e q/Z(c) = 1 forces Z(c) = N(c), uniquely."

Setting `Z = N` inside §5.1's transfer gives `q' = q·N(h+e)/N(h)`, which is
per-cut normalized nowhere in general — a type mismatch.  The abstract's
phrasing ("ratio preservation forces the frontier-sum normalizer, and 36 of
the 202 canonical diamonds … refute its chain consistency") is correct;
§5.1–5.2's formalization of it is not.  Every number in §5 is right; the
posing is not the decided one.  Given that d42b3's round-1 BLOCKER was
exactly "T3 as pinned was ill-posed (normalization clause never stated)"
(LOG #302), the terminal paper must not reintroduce a mis-posed version of
the same object.

**Repair (exact text).**  Either (i) pose the ratio-preserving class in the
divisor convention: "A *ratio-preserving* completion is a per-cut divisor
`Z(h) > 0` with `q'(e|h) = q(e|h)/Z(h)`; per-cut normalization forces
`Z = N`, the frontier sum, and foliation-invariance of the completed chain
products then requires `N`'s chain products to be foliation-independent —
which 36 of the 202 canonical diamonds refute [EXACT]"; and keep §5.1's
h-transform transfer for the gradient class only (where (a) is the harmonic
equation and invariance is the telescoping theorem of §5.5).  Or (ii) keep
one transfer and restate §5.2 as: "ratio preservation forces
`Z(h+e)/Z(h) = 1/N(h)`; no cut function has these increments, because `N`'s
chain products are foliation-dependent: 36 of the 202 canonical diamonds
refute integrability."  In either case, restate (b) so it binds: "the
completed conditional is a function of the record alone (class-constant) —
equivalently, chain products agree across the linear extensions of every
history," and note that for class-constant `Z` the gradient form makes this
automatic (§5.5's telescoping theorem).

### F3 — MAJOR (CONFIRMED): the paper's source-binding claim is wider than
### the truth — five quantities appear in no receipt `.out`

Status header: "Every quantitative claim is bound to one of seven committed
terminal receipts (…; outputs under `v10/data/`)."  §9.1: "Every
quantitative claim in this paper is bound to a committed exit-1-by-design
receipt…"

Checked against all seven `.out`s, the following quantities appear in **no
receipt output**; they live only in the committed campaign record:

1. **313** (boundary freedom) — abstract, §5.3, §5.7, §9 item 1.  Source:
   d42b3 round-1 frozen review ("the finite-depth solution set is a
   313-parameter family"; classes "1 + 6 + 23 + 84 + 313 by depth") and
   LOG #302.  Not in `d42b3_placement_exact.out`.
2. **175 / 31** (structural / exact isomorphism census) — §5.6.  Source: pin
   B4 (`note-d42b56-rootfree-action-shadows.md`: "331 … 175 structural, 31
   exact, censused") and the d42b56 frozen review.  The `.out` prints only
   the 331.
3. **"two canonical components"** for the 36 violations — §5.2.  Source:
   d42b3 round-1 review ("exactly 2 bad diamond-connected components") and
   LOG #302.  Not in the `.out`.
4. **"rank 114 of 427"** — §5.7.  No committed statement anywhere uses
   "rank"; the number is the arithmetic complement 427 − 313 = 114 (and 114
   is receipt-anchored as the interior-class count), but the rank *claim*
   is derived, not committed.

The paper knows how to do this correctly — §4.4 flags its one LOG-sourced
decomposition in-line ("the sector decomposition per the committed ledger
record, LOG #304") — which itself contradicts the blanket receipt-binding
sentence two sections later.  All five quantities are TRUE and committed;
the defect is attribution, which is exactly what the methods note exists to
make checkable.

**Repair (exact text).**  Status header and §9.1: "Every quantitative claim
is bound to one of seven committed terminal receipts (outputs under
`v10/data/`) or, where stated, to the committed campaign record (LOG,
pins, frozen review files)."  Add in-line source tags at the four unflagged
sites: §5.2 "…lying in two diamond-connected components [per the committed
review record]"; §5.3 and §5.7 and §9 item 1 "…313-parameter boundary
freedom [per the committed review record, LOG #302]"; §5.6 "…175 are
structurally isomorphic to it, and 31 exactly so [pin B4]".  §5.7: replace
"the constraint system has rank 114 of 427" with "the backward recursion
determines the 114 interior classes from the 313 terminal ones (LOG #302),
leaving the 313 boundary freedoms of §5.3."

### F4 — MAJOR (CONFIRMED): §1.1 misparaphrases paper 29's isolated target,
### trimming exactly the clauses this campaign did not deliver

Paper 30 §1.1:

> "Paper 29's architecture audit then isolated the next object: the
> smallest record-closed generator in which content, conflict, and durable
> records are one executable object."

Paper 29 §17 (verbatim):

> "It is the smallest record-closed **quantum** generator in which content,
> conflict, **entangling interaction, dynamic adjacency** and durable
> records are one executable object."

The paraphrase silently drops "quantum," "entangling interaction," and
"dynamic adjacency" — precisely the three clauses the campaign did *not*
discharge: the lift's arbitration layer is OPEN (the paper's own §6.2), no
entangling interaction exists in the grammar, and the adjacency/dimension
front is a declared verdict-free pilot (§7.2).  As written, §1.1 makes the
delivered classical object appear to meet paper 29's full specification.
The d41d entry-condition claim in the same paragraph is accurate (d41d R7:
eight items; item 7 "opportunity struct IRREDUCIBLE (D42's entry)"), and
the demand the paper says it discharges ("What a proposal *is*, when it
*may* be made, and when arbitration *may* act") is the honest one — the
paper-29 paraphrase above it is not.

**Repair (exact text).**  "Paper 29's architecture audit then isolated the
next object: 'the smallest record-closed quantum generator in which
content, conflict, entangling interaction, dynamic adjacency and durable
records are one executable object.'  This paper builds the classical core
of that object — content, conflict, and durable records as one executable
grammar — and locates exactly where its quantum completion begins (§6);
the entangling-interaction and adjacency clauses are the arbitration-layer
residue and the dimension pilot respectively (§9 item 2, §7.2)."

---

## 2. minor findings

**m1 (CONFIRMED).** §5.2 "the violations lying in two canonical
components": the committed term is "diamond-connected components" (d42b3
review); "canonical component" is defined nowhere in the paper and
collides with "canonical class."  Use the review's term.

**m2 (CONFIRMED).** §4.1 "(the d34b inheritance declared in §1.2)" is a
dangling cross-reference: §1.2 never mentions d34b (grep: d34b occurs only
at §4.1).  The declaration lives in the receipt banners ("joint-placement
normalization is d34b's problem, INHERITED").  Either name d34b in §1.2's
"Still supplied, declared" paragraph or point at the receipts.

**m3 (CONFIRMED).** d34a (§4.3), d34b (§4.1) and the NSE acronym (§2.5,
§6.3, §9) are unresolvable from the reference list: reference 10 covers
D22/D23/D25/D26/D27 only, and "NSE" is never expanded (a reader must infer
it from reference 10's "No Silent Erasure").  Expand NSE at first use and
add the d34a/d34b provenance (corpus notes or LOG pointer) to reference 10.

**m4 (CONFIRMED).** §1.1 quote splice: "remain alternative supplied
kernels" is quoted from paper 25 §10.1, whose sentence is "…so K1, K2 **and
K3** remain alternative supplied kernels."  Attaching the quotation to "K1
and K2" alone silently drops K3 (paper 25 §10.4's hard-core family).  The
inherited-kernel claim is still true; mark the splice ("with K3") or drop
the quotation marks on the second phrase.

**m5 (CONFIRMED).** Abstract "— bases are boundary choices —" and §6.1 "The
lift-basis choices are exactly the classical boundary choices [EXACT]"
overreach their own table: the coherent aggregation (Z = 6) is "the one
non-gradient object," not a boundary choice, and §9 item 3 calls all three
options "lift basis."  Say "the class and sequence bases are the two
classical boundary choices" in both places (as §9 item 3 correctly does).

**m6 (CONFIRMED).** §7.1 first bullet claims "opportunity generation and
extension closure (iff-sweeps, enabled-set gauge invariance) [EXACT]" for
both grammars without the gate's scope: GG1 ran "on the depth<=2 slice"
(93 candidate-set points — the `.out`'s own words); full-depth
closure-membership was referee-verified in the frozen round only (501/965).
Add "(depth <= 2 slice, 93 points; the iff-sweeps family-wide)".

**m7 (CONFIRMED).** §7.2 "Paper 20's dynamic-adjacency fork": paper 20
contains no such name (grep: zero hits for "adjacency"); its own names are
the covariance fork (O7) and the **dynamic-metric** fork / successor arm
(2) ("dynamic-metric interacts (edge-insertion)").  The phrase is the
committed d42b7 pin's coinage, so it is adjudication-consistent — but at
paper grade the citation should resolve: "paper 20's dynamic-metric fork
(its successor arm (2)), posed for generated adjacency in the d42b7 pin."

**m8 (CONFIRMED).** §9 "The campaign closes with six open items" is
narrower than the campaign's own named carried set: the d42b4 pin's carried
list also names "the forced-click ontology; the D24/D26 g-numeric binding
(d42c class)"; LOG #316 carries "the referee's (actor,base) census-key
upgrade (corpus-wide note)"; and LOG #307 carried "the actor-factored
round-2 target" to d42b5/6, where it was never discharged (grep: absent
from the d42b56 pin, receipt, review, and this paper).  Either add a
closing line ("Pin-level carried obligations — the forced-click ontology,
the D24/D26 g-binding (d42c class), the (actor,base) census-key upgrade,
and the actor-factored intermediate completion class (subsumed by residue
1's finite-depth side if the authors so adjudicate) — remain recorded in
the pins and LOG") or scope the sentence to "six paper-level residues."

**m9 (CONFIRMED).** §5.7's sentence conflates levels: "A stationary
completion is a positive-eigenvector solution … on this quotient; at
finite depth the constraint system has rank 114 of 427, leaving the 313
boundary freedoms" — 114/427/313 are canonical-class counts, not
quotient counts (the quotient has 17 states).  Split: state the
eigen-problem on the quotient, then give the class-level count in its own
sentence (with the F3 repair's sourcing).

**m10 (CONFIRMED).** Abstract: "reduces one-way into a single
infinite-volume positive-harmonic residue on a 17-state bisimulation
quotient" attaches the depth-4 state count to the infinite-volume object;
the quotient grows with depth (§9 item 1: "at growing depth (the depth-4
quotient has 17 states…)").  Say "on the bisimulation quotient (17 states
at the decided depth)."

---

## 3. nits

**n1.** §6.3 "at violation `0.2599...`": the digits are 0.25989…, so
"0.2599..." is a rounded value wearing a truncation ellipsis.  Print
"0.25989…" or "0.2599 (rounded)"; LOG #309 prints 0.2599 without ellipsis.

**n2.** §9.2 "Three papers ago the program had a coordination protocol…":
the protocol is paper 25's (five papers back) and the d41d audit verdict
postdates paper 29 (one paper back); "three papers ago" fits neither.
"Five papers ago the program had a coordination protocol …; one audit ago,
an identified low-energy law's opportunity structure was declared
irreducible."

**n3.** §9 item 3 coins "the aggregation-trilemma boundary choice" — the
name "aggregation trilemma" is never introduced in §6.1 (which says "three
normalizations … observably inequivalent"), and the paper already carries
§5's decided trilemma and §6.2's three-horn pincer.  Introduce the name in
§6.1 or drop it in §9.

**n4.** §6.3 "(The numerical coincidence with §3.1's total-variation
distance — both `1/6` — is an artifact of `3! = 6` on the path…)": the
coherence half is committed (per-click amplitudes multiply to sqrt(1/6),
d42b4 review), but the TV half's "artifact of 3! = 6" is an uncommitted
gloss (TV = 4/6 − 3/6).  The load-bearing clause ("the two are distinct
observables") is right; soften to "both equal `1/6` on this fixture; the
two are distinct observables…".

**n5.** §8.1 "an interacting covariant generator with a generated
opportunity complex": at first use "covariant" reads as spacetime
covariance; the earned sense is §8.2's (internal `Z2 x Z2` + foliation
gauge).  Add "(covariant in the §8.2 sense)".

---

## 4. The number-fidelity sweep

Method: every quantitative claim in the paper was listed and checked
against its committed source.  **226 claim instances swept (≈170 distinct
quantities).  226/226 match their committed sources.  0 mismatched.
218 instances trace to the seven terminal `.out`s; 8 instances trace only
to the committed campaign record (LOG/pins/frozen reviews), of which 1 is
source-flagged in the paper (§4.4 → LOG #304) and 7 are not (→ F3).**

| Paper site | Claims | Source | Verdict |
|---|---|---|---|
| Status/§9.1 | 7 receipts; PASS 18/18, 21/21, 8/8, 8/8, 8/8, 9/9, 4/4 | the seven `.out` summaries | MATCH |
| Abstract | 1+k/4; 36/202; 215; 21/114 root incl.; 17; 2/3–1/3; 1/6 vs 0; six residues; 1/k boundary | d42b3/d42b56/d42b4 `.out`s | MATCH (ladder scope → F1; 313 → F3; 17-attachment → m10) |
| §1.2 | sector budgets 1/4×3; genesis idle 1/2; all-open 1/4; K1 2/3 vs K2 1/2; merge click 1/2; \|C\|! | d42b1 banner/battery; d42a G5b; pin #290 | MATCH |
| §1.3 | 0/13,060; 0/7,393 | d42a L1; d42b1 L1 | MATCH |
| §1.4 | 2,875 pts / 856 histories; 7,509 / 3,638; h5, h11 all-1; h12 | d42a G1/G1b; d42b1 G1/G1b/F1/N1 | MATCH |
| §1.5 | 6,471; 6,589; census 4; mu 1/64; 3,316 | d42a G0/G2a/G2b | MATCH |
| §2 | 3,969; 3,424; census 4; 1/64; 60 serialized; forks 424/72; 3,032/0; 8-event chain, 3 observer pasts; delivery-free 0; in-family two-arb 0 (5-event note); merge 2 options @1/8; vacuity 0; {(vD0,v_m)}; 1/4; 1/8; orphans 1,960/2,088/464/72; rescue 1/8; 0 anomalies; joins 3,096/384/8,250 | d42b1 banner, P1–P4, G2, G3/G4, P2/P4, §2-chain, G6; d42a G4b/G4c/G6 | MATCH |
| §3 | 2/3, 1/3; 1/2, 1/2; TV 1/6; 1/3072; 1/4096; 12,552; star 2/3; 6 chains @1/6 (1/3, 1/2, 1); 1/#MIS; 1/8 ×12 extensions; 3 interleavings (1/8×2, 1×4); 1/16 = (1/4)/2×1/2 (arb and merge); 5 shapes (1,1,3); 3 iso; triangle-free; ternary conditionals 1/3, 2/3; (P,Q,R)/(P,R,Q); ternary K1=K2=1/3 | d42a G5b/G5c/G7; d42b1 G5; d42b2 E1/E4/CENSUS/CLICK/CONCURRENT/SECTOR/E6; d42b7 GG4 | MATCH |
| §4 | 5/4; ARM-1 {11,926, 1,016}; ARM-2 {16,539, 1,824, 936, 468}; ARM-1T {7,514, 424}; ARM-2T {9,588, 576, 72, 36}; W6 18,210/0; density 2,382/0, {0: 2,134, 1: 248}; sums 1 vs 5/4; extra 1/4 over 2; mu 1/256; 1/2048 vs 1/2560; N (2,2,2)/(2,2,5/2); 0/427; 23/24; 1/12 + 1/8 = 5/24 | d42a G9; d42b1 G9/N1; d42b3 G-L2/G-T1/D3/G-T2/D2; LOG #304 (flagged) | MATCH (spectra sum to the family×actor counts exactly — internal consistency verified) |
| §5 | 1,191; 427; 202; 36; 1037/64 (recip. 64/1037); 215; 1/2074; 21/114 root incl.; 133/2074, 771/2074 (recip. 16/133, 32/257 — reciprocal arithmetic re-derived and exact); 28/0 @1/8; ladder 0/36/0; probe 0/202; sequence-Z 51 (representative-dependent); 325/64; 21/325 vs 1/16; 133/2074 vs 1/16; 331; 4 shapes; 17; 4→9→14→16→17(+17); 0/427 | d42b3 D1(i)/D1(ii)/G-L1; d42b56 S1/S2/S3; LOG #307/#320/#321 | MATCH (313, 175/31, two components, rank-114 → F3) |
| §6 | 32 seq; 23 classes; Z_class 3; 253 pairs (=C(23,2)); dps 80/1e-60; 3/4/6; menus 2@1 vs 4@5/4, 2 inadmissible; (2/3, 1/3) norm 1; 15 pairs, 7@1/6, 8@0; sqrt(1/6)·sqrt(1/6); fiber 4; 6+4 checks; 10 distances; 0.2599 vs 1/100 | d42b4 E2/E3/ENDPOINT/PINCER/KERNEL/1-6/D23/NSE; review l.426 | MATCH (ellipsis → n1) |
| §7 | 215; 405; 4→12; 1/64→1/144 (1/8→1/12); binary {374, 56}; ternary {642, 168} (both sum to 2×215 / 2×405 exactly); 1/4 blind groups; ternary 0–2 pair; 4/18, 0; fork-freeness 0; 36 K3 @1/1728 = 1/48; paths 108 ternary / 36 binary (per #315/#316 reconciliation, #323 flag 3); 4×1/8; mass 14; 5 LIFTED / 3 TOY / SHAPE; 386/771; 290/579; 1/1542; 1/1158 (excess arithmetic re-derived exact); baseline 1 @ mu 3/128; {1/3, 2/3, 1} | d42b7 banner/GG2/GG3/GG3b/GG3c/GG4a/GG4/GG5/GG6 | MATCH (LOG-only join masses correctly omitted per #323 flag 5) |
| §8 | 36/202 recap; internal Z2×Z2; 0/1,191 each generator | d42b56 S1/S4 | MATCH |
| §9 | six items; 17; 23/24; 1/6 vs 0; 3/4/6 | ledger cross-refs | MATCH (completeness → m8) |

Cross-document verification: paper 25 quotes (§11.1 verbatim; §10.1 spliced
→ m4); paper 28 ("Five chosen D34b histories generate no transaction
proposal with a typed participant base version and hence no contended
conflict cell.  Their induced arbitration law is vacuous." — §1.1 CONFIRMED
near-verbatim; H1 typed causal certificate CONFIRMED; §5.3 rooting cite
CONFIRMED as the adjudicated load-bearing form per d42b56-F6); paper 29
(§17 target — misparaphrased → F4; eight-slot table CONFIRMED at §9.2);
d41d `.out` (R7 scorecard: eight items, item 7 opportunity IRREDUCIBLE =
D42's entry, item 8 preferred durable algebra IRREDUCIBLE — §1.1 and §3.3
CONFIRMED); v6 paper 1 (title exact; the two coupled residues verbatim —
§8.1 CONFIRMED); d42b3 code (witness pair `E1 = [pA0, SELFA, pB1]`,
`E2 = [pA0, pB1, SELFA]` — §4.3 CONFIRMED); references 11–20 (external
citations spot-checked: Tomonaga PTP 1 (1946) 27–42; Schwinger PR 74 (1948)
1439–1461; Dirac PRSA 136 (1932) 453–464; Hegerfeldt PRD 10 (1974)
3320–3321; Kung–Robinson TODS 6 (1981) 213–226; Lamport CACM 21 (1978)
558–565; BLMS PRL 59 (1987) 521–524; Larsen–Skou I&C 94 (1991) 1–28 — all
correct); all eight pin filenames in reference 8 exist; the d41d receipt
path in reference 9 exists.

---

## 5. Claim-fidelity audit against the known hazard classes

- headline wider than computation: **fails at one site** (the ladder — F1);
  everywhere else the scoping held (TS "decided at fixture depth" ✓).
- "generated" for constructed objects: **clean** — every constructed chain
  (SIG-FM, the ten-event chain, h5/h11/h12) is called constructed; the
  merge-opportunity "generated at the two-fork past" is the receipt's own
  adjudicated language for the prefix-exact iff on SIG-FM.
- universality beyond two-of-two: **clean** — "two-of-two … and no more is
  claimed" in the abstract and §7.1; "universal" appears only in §7's scoped
  sense (grep-verified).
- trilemma-evasion for the lift: **clean** — retraction honored ("no evasion
  of §5's trilemma," gradient-in-Hilbert-dress at the 1/k boundary per LOG
  #312, pincer + arb-layer OPEN).
- telescoping separating content = class-constancy: **present** (abstract,
  §5.5, coda); the 36's class-invariance vs the 51's representative-
  dependence stated per the #321 adjudication.
- one-way reduction: **present** (abstract, §5.7, §9 item 1; "no claim in
  either direction").
- dimension pilot affine-readout-no-verdict: **present** (§7.2, bolded).
- sprinkling scope internal Z2×Z2 + foliation gauge: **present** (§8.2,
  "*not* spacetime symmetry").
- Hegerfeldt pre-registration: **present** (§6.3, §8.3, §9.1-adjacent).
- residue ledger six items with entry conditions: **present and correct as
  stated** (completeness question → m8).
- T1 positivity/support-preservation hypothesis: **present in the theorem
  statement**, with the zero-class exclusion and its reason (both committed:
  d42b3 D3 + review F3, including "restores sums to 1 by exactly the
  density" — review-verbatim).
- A7's three faces: **present** (§1.4: generator, pricing, conduct beyond
  caps — each bound to its gate).
- canonical class-1/k = 1/#linearizations: **present** (§5.6 parenthesis,
  per #320/#321).
- single-threaded style: **clean** — no round narration; the methods note's
  "adversarially reviewed to terminal status" is the sanctioned single
  sentence; "reconvicted" (§4.3) references the corpus-level d34a lineage,
  not this campaign's rounds.

## 6. What survives

Everything numerical: 226/226 claim instances match their committed
sources, zero false numbers — the paper preserves the campaign's
nine-round streak.  The paper's architecture is the adjudicated one: the
generated-vs-supplied split (Result 1 with the kernel law / genesis /
completion declared supplied), the five transport phenomena, the click
refinement with the join-typed opening click, the ladder censuses and
h12, the decided trilemma's verdicts and every §5 exhibit, the honest
endpoint-lift identification with the pincer and the four established
lift results, the two-of-two second-grammar discipline, the verdict-free
pilot, the v6 correspondence at named scope, and a residue ledger whose
six items carry correct entry conditions.  §1.1's paper-25/paper-28/d41d
claims check against their documents (paper-29 excepted — F4).  The
reference list is accurate throughout.  With F1–F4 repaired (all
statement-level; no computation is touched), the paper is terminal-fit.

## 7. Prescribed repair order

1. F1: abstract sentence + A7' box scope clause (text above).
2. F2: §5.1/§5.2 reformalization (either arm above; the divisor arm is
   closest to the committed computation).
3. F3: status/§9.1 binding sentence + four in-line source tags + the §5.7
   rank rewording.
4. F4: §1.1 paper-29 quotation restored with the honest delivery clause.
5. m1–m10, n1–n5 as listed; none touches a number.

— frozen, paper-level round 1.

---

# Delta-verification (round 1 repairs, HEAD f34ced1, paper 1,120 lines)

**Scope:** the #325 repair commit checked edit-by-edit against the round-1
prescriptions; the two applier placement judgments adjudicated; the grep
battery rerun; every quantity introduced by the repairs re-verified at
source.  Round-1 body above untouched (zero diff since the #324 commit).

## Verdict: DELTA-CLEAN — 0 findings / 4 notes (one a carried round-1 nit).
## Paper 30 is terminal-fit.

## Repair verification

- **F1 — VERIFIED.**  The abstract's ladder sentence and the §4.1 A7' box
  carry the prescribed scoped text exactly (enumerated families + h5/h11;
  h12 off-ladder; general-depth false; reconciliation carried to the
  completion problem).
- **F2 — VERIFIED (arm ii).**  §5.2 now reads "Ratio preservation forces
  `Z(h+e)/Z(h) = 1/N(h)`; no cut function has these increments, because
  `N`'s chain products are foliation-dependent: 36 of the 202 canonical
  diamonds refute integrability" — the prescribed increment restatement,
  with m1's "diamond-connected components" and the F3 source tag folded
  in.  Demand (b) is restated as class-constancy with the telescoping
  note, verbatim per prescription; (b) now binds.
- **F3 — VERIFIED.**  Status header and §9.1 carry the campaign-record
  clause; the four in-line tags are placed (§5.2 review-record; §5.3 and
  §9 item 1 LOG #302; §5.6 pin B4); §5.7's rank sentence is replaced with
  the prescribed backward-recursion text and split per m9 (quotient
  sentence and class-level sentence now separate).  The abstract's
  untagged 313 is acceptable: abstract numbers recapitulate tagged body
  claims, and the binding sentence's "where stated" points at the body
  sites.
- **F4 — VERIFIED.**  The paper-29 §17 quotation is restored verbatim
  (checked word-for-word against paper 29) with the prescribed
  honest-delivery clause (§6 pointer; entangling-interaction and
  adjacency assigned to §9 item 2 and §7.2).
- **m1–m10 — ALL VERIFIED** against the prescriptions: diamond-connected
  components (m1); "declared in the receipt banners" (m2); NSE expanded
  at §2.5 first use + reference-10 provenance (m3 — adjudicated below);
  "(with K3)" splice repair (m4); "the class and sequence bases are the
  two classical boundary choices" at both the abstract and §6.1 (m5);
  "(depth `<= 2` slice, 93 points; the iff-sweeps family-wide)" (m6 —
  93 re-verified against the GG1 `.out`); "Paper 20's dynamic-metric
  fork (its successor arm (2)), posed for generated adjacency in the
  d42b7 pin" (m7 — arm (2) re-verified against paper 20's successor-arm
  list); the pin-level carried-obligations paragraph after item 6 (m8 —
  voice note D-N2 below); m9 via the F3 split; "(17 states at the
  decided depth)" (m10).
- **Nits: n1 ("0.25989..." — matches the `.out` digits), n2 ("Five
  papers ago … one audit ago"), n4 ("both equal `1/6` on this fixture"),
  n5 ("(covariant in the §8.2 sense)") — VERIFIED.  n3 was not applied
  (carried; note D-N4).**

## Adjudication 1 (coordinator item 2): §5.1 "strictly positive cut data
## `Z`" → "strictly positive data `Z`" — the deletion is CORRECT

The applier's reasoning is the round-1 F2 analysis itself: the round-1
body says of the original (b) that "the definition says 'cut data',
killing that reading."  Under arm (ii), (b)-as-class-constancy is a
*constraint* only if `Z` a priori ranges over prefix-attached data; an
up-front cut-data declaration would make (b) tautological again and
would also contradict §5.5's negative control (a sequence-attached `Z`
failing 51 diamonds is only expressible if sequence-attached `Z` is in
the candidate class).  §5.1 does not need a different opening — it needs
one more word of typing (note D-N1): the bare "data `Z`" leaves the
domain implicit (the transfer's `Z(h)`/`Z(h+e)` usage and §5.5's
cut-attached/sequence-attached taxonomy recover it, but the noun should
say it).

## Adjudication 2 (coordinator item 6): the A7' scope clause at the END
## of the box — ACCEPTED, and in fact REQUIRED

The applier's observation is substantively correct and repairs a gap in
the round-1 prescription itself.  At h12 the box's *second* sentence is
also violated: B's own-view-priced arbitrate-and-merge sector prices
`1/12 + 1/8 = 5/24` (LOG #304), so B's own-view sectors sum to `23/24`,
not 1 — the own-view sentence is exactly as h12-exposed as the ladder
sentence.  A clause placed adjacent to the ladder sentence only (the
round-1 wording "append to A7'" read narrowly) would have scoped
sentence 1 and left sentence 2 as a new unqualified false claim.
End-of-box placement scopes the own-view sentence grammatically, and the
ladder sentence is scoped by the clause's own content ("the
general-depth ladder is false under current pricing"), which forecloses
any unqualified reading of sentence 1.  Optional strengthening (not
required): open the clause "— both statements at the record points of
the enumerated families …".

## Adjudication 3 (coordinator item 5): reference-10's d34a/d34b
## provenance via the committed receipts — ACCEPTABLE

No `note-d34a`/`note-d34b` files exist; the receipts are the units'
committed carriers, and both were verified to carry the cited content:
`d34a_harris_lemma_exact.py` carries the lottery/census-denominator
lineage in its gate text, and `d34b_exponential_clocks_exact.py` carries
the placement content ("cylinders carry clock-placement factors"; the E3
PASSIVE-RECEPTION PLACEMENT gate).  Citing through receipts is the
established pattern of reference 9 (d41d).  Correct as applied.

## Grep battery + voice check — CLEAN

No review-round narration in the paper's voice: the only
"convict"-family hits are the round-1-cleared d34a-lineage usages
(§4.3 "reconvicted", "census-denominator conviction" — corpus lineage,
not campaign narration); "universal" remains confined to §7's scoped
sense; the "[per the committed review record …]" tags are source
citations sanctioned by the amended binding sentences, not narration;
the methods note's "adversarially reviewed to terminal status" remains
the one sanctioned sentence.  Quantities introduced by the repairs all
re-verified at source (93; 0.25989...; successor arm (2); the two d34a/
d34b receipt paths exist).  LOG #324/#325 present; report round-1 body
byte-identical since #324.

## Notes (none blocks terminal; apply or carry per the #298 precedent)

- **D-N1.**  §5.1: "strictly positive data `Z`" → "strictly positive
  data `Z` on record prefixes".  Types the domain the arm-(ii) reading
  needs; one phrase, no claim change.
- **D-N2.**  §9 pin-level paragraph: "(subsumed by residue 1's
  finite-depth side if the authors so adjudicate)" is review-voice
  inside the paper — the round-1 prescription's parenthetical shipped
  verbatim (the round's own defect, not the applier's).  Adjudicate it:
  "(a completion-class sharpening of residue 1's finite-depth side)".
- **D-N3.**  §9.1: "…adversarially reviewed to terminal status — or,
  where stated, to the committed campaign record" momentarily parses as
  "reviewed … to the record".  Smooth: "— or bound, where stated, to
  the committed campaign record".
- **D-N4 (carried round-1 n3).**  "the aggregation-trilemma boundary
  choice" (§9 item 3) is still never introduced in §6.1.  One-line fix:
  in §6.1, "The three normalizations are observably inequivalent (the
  aggregation trilemma); …" — or drop the name in item 3.

## Terminal statement

All four MAJORs and all applied minors/nits land exactly on the
prescriptions or improve them (Adjudication 2); zero new numbers, zero
scope changes, zero narrative leaks.  **DELTA-CLEAN.  On this stamp
paper 30 is TERMINAL-FIT as repaired**; the four notes are wording
polish at the authors' discretion and require no re-review.

— delta appended; round-1 body untouched.
