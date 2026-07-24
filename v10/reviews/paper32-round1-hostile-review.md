# Paper 32 round 1 — hostile review (*The boundary of closure*)

**Reviewer:** hostile referee, round 1 (the round the paper's own status
line declares "NOT YET COMMISSIONED"; commissioned now, LOG #376 object).
**Object:** `v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md`
(423 lines, commit 1610689, working tree clean at review time;
md5 18103a45b41a1c88da0d1e68986448fe).
**Authoritative sources consulted:** the eight terminal units and their
receipts/.outs (`v10/code/`, `v10/data/`: d44a #368, d44b #374, d44c #355,
d44d #353, d44e #364, d44f #372, d45a #362, d45b #367); the frozen rounds
and delta sections `v10/reviews/d44{a,b,c,d,e,f}-round1-hostile-review.md`,
`d45{a,b}-round1-hostile-review.md`; the pins/notes `note-d44a`..`note-d44f`,
`note-d45a`, `note-d45b`, `note-d44-d45-campaign-synthesis.md`;
`v10/relativistic-isp-v10-paper30-*.md`, `...-paper31-*.md`;
`v10/LOG.md` ##346–389.

---

## VERDICT: REVISE — 1 BLOCKER / 9 MAJOR / 10 minor / 3 nit

**The number sweep is CLEAN.** Sixty-one distinct quantitative claims were
checked against the receipts/.outs and eleven key reductions were recomputed
independently; **zero false numbers, zero arithmetic mismatches, zero
mis-transcriptions.** The campaign's own "zero false numbers" record survives
its conversion into a paper. Every PASS count in §7's receipt surface matches
its `.out` `[SUMMARY]` line exactly (30/14/15/17/49/29/22/49).

**The unreviewed-ladder hazard is CLEAN.** No D46 unit (#380 D46a, #382 D46c,
#384 D46b, #386 D46d, #388 D46f, #389 D46e) is cited, alluded to, or leaked
anywhere in the paper: the string `d46`/`D46` does not occur, no ladder result
is stated, and §6's residue ledger is exactly the #375 successor list
(H1 open; Martin/R-theory named-not-started; the dimension ladder as a
question; smeared-interacting; reception dynamics; the embedded-head
obligation still *standing*, correct as of #376 — it was discharged only at
#378). The single item that could have leaked — §6 item 3's typicality
question — is verbatim the campaign synthesis's successor 3 (#375, "does the
measure favor the courier structures it prices at 1/212-class weights?"), not
D46d's finding. **No repair needed on this axis.**

**The scope/quantifier discipline is largely honoured and then broken in four
specific places.** The paper is disciplined exactly where the d44b delta's
binding flags aimed it: H1-conditionality is paired with "transport closure
OPEN" in the abstract, §2.2, §4.3 and §6.1; "escape is not non-stabilization"
is stated as such; the transport six is an ECHO; no depth-5+ prediction is
made; the order-dimension doctrine is declared binding. What the paper then
does *not* cap: the funnel lemma's provenance (BLOCKER-1), the S_n width
formula (MAJOR-7), the slab collapse's lattice-size coverage (MAJOR-8), and
two campaign-wide method claims in §7 that are false of two of the eight
receipts (MAJOR-1, MAJOR-2).

**What fails hardest is provenance, not arithmetic.** §1 defines
"referee-carried" for facts "verified in a frozen review record rather than
gated in a receipt" — and then the paper's single strongest dimension claim
(the funnel lemma), the count that opens §3.1 (1,124,884), and the
"every constructor state" clause are all referee-carried facts printed
without the tag, two of them carrying a `[THEOREM]` label instead.

---

## Findings

### BLOCKER-1 — the FUNNEL LEMMA is printed as a gated six-clause law and tagged `[THEOREM]`; it is referee-carried, and D44c's terminal delta named an explicit paper-grade promotion condition that this paper does not meet

**What the paper says** (§3.1, and again in the abstract):

> "The mechanism is the COMPONENT-CONFINEMENT LAW (gated, zero violations):
> arbitration pools form a laminar family; ... and — the round's sixth clause
> — incomparable arbitrations share no upper bound, yielding the FUNNEL
> LEMMA: the crown S3 is impossible as an induced subposet at EVERY width and
> depth [THEOREM for the S3 pattern; tested-scale scope remains for non-crown
> 3-irreducible patterns]."

Abstract: "a six-clause component-confinement law, with a funnel lemma making
the crown pattern impossible at every width and depth".

**What the artifacts say.** The receipt gates **five** clauses, not six:
`v10/data/d44c_arb_dimension_exact.out` AG3 states the law as
"(i) LAMINARITY … (v) VNAME FRESHNESS" and gates
"zero violations of (i)-(v) across 1,213,372 label-level histories". The
sixth clause and the funnel lemma exist only in the frozen round and the pin's
record of it — `note-d44c-multiauthor-arb-dimension.md` §6 **B4** is titled
"the round's positive deliveries — **referee-carried, cited as such**", and
its item (iii) reads: "The five clauses are provably ALL-SCALE theorems, plus
a stronger SIXTH clause … (0 violations mechanically) — yielding the round's
FUNNEL LEMMA".

**And the terminal delta attached a condition.** LOG #355 (D44c TERMINAL):

> "the referee-carried citation ACCEPTED for terminal/pin/successor use with
> the **PAPER-GRADE promotion condition named**: an in-receipt gate of the
> sixth clause + up-cone confinement (round T2/T3) over the committed
> families + the lemma as a theorem-with-proof-note — the d43d-NG3b path"

None of the three conditions is met: there is no in-receipt sixth-clause gate,
no up-cone confinement gate, and no proof note for the funnel lemma anywhere
in `v10/` (contrast D45b, which *did* write its §8 all-n proof note before
paper 32 cited its schema as `[THEOREM, all n]`). Paper 32 is precisely the
"paper-grade" use the delta was gating, and it performs the promotion
silently: it moves a referee-carried claim into a `[THEOREM]` tag, folds the
ungated sixth clause into a law it describes as "(gated, zero violations)",
and puts the lemma in the abstract.

**Why BLOCKER and not MAJOR.** §3.1 is the load-bearing half of the paper's
second headline ("dimension is mechanized and ceiling-free"): the no-go side
is what makes transport's mechanism *unique*, and the scale-freeness of the
S3 obstruction is the only part of that no-go which is not cap-limited. A
public record that presents an ungated, unproved lemma as a theorem, against
its own terminal ledger's explicit instruction, cannot go out.

**Prescribed fix — any one of (a)/(b), plus (c):**
(a) *Demote in place.* §3.1 → "The mechanism is the COMPONENT-CONFINEMENT
LAW (five clauses, gated in-receipt, zero violations across …): … The frozen
round adds a sixth clause — incomparable arbitrations share no upper bound
(0 violations, **referee-carried**) — and derives from it the FUNNEL LEMMA:
S3 is impossible as an induced subposet at every width and depth
[**referee-carried**; not receipt-gated and not proof-noted — LOG #355's
paper-grade promotion condition (in-receipt sixth-clause + up-cone gates, plus
a theorem-with-proof-note) is OPEN]." Abstract: same demotion, or drop the
funnel lemma from the abstract entirely and keep only "a six-clause
component-confinement law (five gated, one referee-carried)".
(b) *Meet the condition before publishing:* execute the #355 promotion path
(a repair rev of d44c or a small successor receipt gating clause (vi) +
up-cone confinement over the committed families, plus a §8-style proof note in
`note-d44c`), then the `[THEOREM]` tag stands as written.
(c) Add the funnel lemma's status to §6's ledger either way — as it stands the
ledger implies nothing is outstanding on the dimension no-go side.

---

### MAJOR-1 — §7 asserts a method property that one of the eight receipts demonstrably violates: "dimension-witness branches are genuine exit-0 outcomes"

**Paper §7:** "Purity gates use the allow-list walk form; **dimension-witness
branches are genuine exit-0 outcomes**; negative controls are gates, not
narration."

**D44c, LOG #354 (forward-correction F1, MAJOR, owned):**

> "the receipt's witness horn was UNREACHABLE AT EXIT 0 — a witness would have
> tripped the census PASS conjuncts and exited 1 mislabeled as breakage; the
> banner's 'either horn exits 0' was false of the code and the witness-horn
> verdict print is dead code … **successor dimension receipts must wire the
> witness branch as a real exit-0 outcome**."

`note-d44c` §6 B1 records it identically and adds "receipt frozen per the
round's own disposition". So the property §7 states as a campaign fact is
(i) false of D44c, and (ii) a *binding on successors* created **because** it
was false — honoured by D45b (ZG6.3, "#354 binding … witness and ceiling are
both exit-0 delivered outcomes") and by nothing else. §7 converts an owned,
logged defect into a uniform methodological virtue. That is exactly the class
of sentence a hostile external reader will check first.

**Prescribed fix:** replace with — "dimension-witness branches are genuine
exit-0 outcomes **from D45b onward: D44c's witness branch was unreachable at
exit 0 (a decision-procedure defect owned at LOG #354 and binding on all
successor dimension receipts; the delivered obstruction outcome is unaffected,
the absence of a witness being independently referee-verified beyond the
caps)**".

---

### MAJOR-2 — §7's blanket "every quantitative claim is bound to a committed exit-1-by-design receipt" is false for the D44d constants the paper cites in §5

**Paper §7:** "Every quantitative claim is bound to a committed
exit-1-by-design receipt, deterministic …".

**D44d's own banner** (`v10/data/d44d_slab_kappa_exact.out` lines 9–12):

> "Round-1 minor-2, stated as designed: clean-cell collapse CONSTANTS and all
> verdict lines are **DELIVERED-VERDICT content, not exit gates** — their
> integrity rides on byte-identical determinism of this .out (SG5); the
> exit-gated layer is anchors/extraction/recognition/collapse-form only."

The frozen round (`d44d-round1-hostile-review.md`, minor-2) demonstrates the
teeth: "my M5 mutant (smear normalization dropped) passes **17/17 PASS,
exit 0**, with the damage visible only as `[KG1 THEOREM] … FAILED at composite
cells` … it means byte-diff of the .out against the committed record is
LOAD-BEARING verification, not a nicety", with the prescribed fix "record in
the conversion note that the verification protocol for this unit is exit code
+ byte-identity".

§5 cites exactly such content: the block arm's "exact ((w+1)/2)^2
normalization law" is `.out` line 131, a `[KG1 BLOCK ARM]` verdict line, not a
`[PASS]` gate; likewise the per-cell collapse constants at w >= 2. The paper's
§7 promise does not hold for them.

**Prescribed fix:** §7 — "Every quantitative claim is bound to a committed
exit-1-by-design receipt — **with one declared exception: D44d's per-cell
collapse constants (and its verdict lines) are delivered-verdict content at
exit 0 by design (the pin's 'any w-dependence is a delivered finding, not a
failure'); their verification protocol is exit code plus byte-identity of the
committed .out, and the exit-gated layer there is
anchors/extraction/recognition/collapse-form only**."

---

### MAJOR-3 — §7's correction taxonomy is materially incomplete and its "each repaired" is false

**Paper §7:** "Across the campaign's rounds and deltas: hundreds of
independently recomputed values, zero false numbers; **the corrections were
quantifiers, vacuous gates, and print-only facts — each repaired and logged.**"

The three-item taxonomy is the campaign synthesis's (`note-d44-d45-campaign-
synthesis.md` §2), where it is offered as a description of *what the rounds
corrected repeatedly*, not as an exhaustive class list. As an exhaustive claim
in a paper it is false twice over:

1. **The campaign had one BLOCKER** — d44f BLOCKER-1: "MG1's sweep does not
   span its declared tilt space: the sign sector slips all four gates", whose
   receipt-side consequence was that "the pinned 'every non-trivial tilt is
   convicted' lemma was FALSE as stated" (`.out` MG1-e). A false lemma is not
   a print-only fact; whether it counts as a "quantifier" is a stretch the
   paper should not be making silently.
2. **"each repaired" is false of D44c's F1**, which was *not* repaired: the
   receipt was frozen and the defect forward-corrected only (#354; `note-d44c`
   B1). D44e's M-2 likewise produced a **corpus obligation**
   (`d42b1@pre-#300` merge pricing, 1/16 vs 1/24 — LOG #363), which is neither
   a quantifier, a vacuous gate, nor a print-only fact; the paper carries it in
   §6.6 but excludes its class from §7.

**Prescribed fix:** "the corrections were over-broad quantifiers, vacuous
gates, print-only facts promoted to anchors, **one blocker-level scope error
(the D44f tilt-space sweep), one decision-procedure defect owned rather than
repaired (D44c's unreachable witness branch, #354), and one discovered corpus
obligation (D44e's embedded transport head, #363 — §6.6 here)** — each logged,
and each repaired except where the round's own disposition froze the receipt."

---

### MAJOR-4 — §1.3's supersession of paper 31 §7 item 7 misdescribes what paper 31 said, and misses the actual correction

**Paper 32 §1:** "paper 31 §7 item 7's zero-crossing successor is discharged
with the crossing correctly characterized (**the LT operator's vanishing
point, not a rule-agreement point**)."

**What paper 31 §7 item 7 actually says** (lines 734–741):

> "compute `kappa(m)` as an exact function and locate its zero crossing — **the
> mass at which the LT rule's identified transport operator vanishes at this
> order** (the sign flip's guaranteed crossing), a distinguished point of the
> fixture. (Whether `kappa(m) = 1` — agreement with the EXC constant — occurs
> anywhere is a separate question, not established either way by the record.)"

Paper 31 already characterises the crossing as the LT operator's vanishing
point, and already quarantines the rule-agreement (kappa = 1) reading as a
distinct, unresolved question. There is nothing to correct on that axis; the
supersession sentence manufactures an error in the committed record and takes
credit for fixing it. This is the one place where the paper's supersession
prose is not merely incomplete but **wrong about its own predecessor**.

**What the real supersession is.** Item 7 presupposes *one* crossing
("its zero crossing", "the sign flip's guaranteed crossing"; likewise §2.5
line 300, "the location of its zero crossing"). D44d/D45a deliver **two**
exact crossings, m² = 1/3 and m² = 4/3, only the first of which lies inside
the pinned sign bracket (KG2 VERDICT; `.out` line 176: "the other crossing
(m² = 4/3) lies outside the pinned bracket — delivered"). That, plus the
channel-anatomy split (D45a YG3), is what supersedes item 7.

**Also now decidable and unmentioned.** Item 7's parenthetical is no longer a
"separate question, not established either way": with D45a's all-m identity
144·kappa(m) = (3m²−1)(3m²−4), kappa(m) = 1 reduces to 9x² − 15x − 140 = 0 in
x = m², discriminant 5265 (not a perfect square), i.e. a single positive real
root x = (15 + √5265)/18 ≈ 4.8645, m ≈ 2.2056 — outside D44d's grid hull
[1/16, 2] but inside the identity's declared all-m fixture scope
(*referee computation, exact-rational + `math.isqrt`; not a receipt fact —
if the paper states it, it must be tagged accordingly or re-gated*).

**Prescribed fix:** §1 → "paper 31 §7 item 7's zero-crossing successor is
discharged, and its singular framing corrected: kappa(m) is an exact quartic
in m with **two** rational-in-m² crossings (m² = 1/3, m² = 4/3), only the
first inside the pinned sign bracket, with different channel anatomies (§5).
Item 7's parenthetical kappa(m) = 1 question is no longer 'not established
either way' — the all-m identity reduces it to a quadratic in m², whose root
lies outside the D44d grid hull; the paper states this as [referee-carried /
receipt-gated] as the author elects."

---

### MAJOR-5 — §1.3's supersession list is incomplete: three further paper-31 statements are rendered stale and go unrecorded

The brief's completeness test. Scanning papers 30 and 31 against the eight
terminals turns up three items §1.3 does not carry:

1. **Paper 31 §7 item 2's entry condition** — "(i) a commutation or
   consistency theorem for the family at overlapping joins, **or a
   counterexample forcing a foliation choice**" — is *discharged by D44f*:
   FG2-a/FG2-c deliver exactly that counterexample (the two cut-advance orders
   are unequal; the fork is forced by carrier licensing). §4.2 reports the
   result but §1.3 never records that item 2's open face closed. Paper 31 §4.4
   ("Whether the family extends to a commuting/foliation-consistent assignment
   at overlapping visibility is the standing arm of horn 2, **untouched**") is
   stale in the same way.
2. **Paper 31 §7 item 5's entry-condition addition** — "decide whether
   arbitration alone generates dimension" — is *decided by D44c* (it does not).
   §1.3 is silent; §6.7 compounds the omission (MAJOR-6).
3. **Paper 31 §7 item 1's "Entry condition: prove the induction; no
   computation remains at this scope"** — falsified. D44a's delivered route
   required a new enumeration space (BFS on sigma), a 36-state/176-edge
   closure, and a 145,408-history out-of-sample level. §1.3 records the
   *route* supersession (pumping → quotient) but not that the ledger's
   no-computation-remains entry condition was wrong; that is the more
   instructive half.

**Prescribed fix:** add the three bullets to §1.3, in the §1.3 style of paper
31 (each stated where the mathematics lives: item 2 → §4.2; item 5 → §3.1;
item 1's entry condition → §2.1).

---

### MAJOR-6 — §6's ledger drops paper 30's residue 6 and mis-reports the breadth item as unchanged

**Paper §6 item 7:** "Paper 30's residues 3 (fine-vs-coarse sealing,
empirical), 4 (mid-chain drift), and its breadth items stand unchanged."

Paper 30 §9 has **six** residues; residue 6 is the `h12` dead-component
pricing constraint (paper 30 §4.4, §9 item 6: "the extended grammar must price
dead-component inflation"), carried forward unchanged by paper 31 §7 item 6.
Paper 32's ledger — the paper's public accounting of what remains open —
**omits it entirely**. A residue that is silently dropped from a ledger reads,
to any downstream reader, as a residue that was closed.

Second, "its breadth items stand unchanged" is inaccurate: paper 31 §7 item 5
*sharpened* residue 5 with an explicit entry-condition addition ("decide
whether arbitration alone generates dimension"), and D44c decided it. The
breadth item's two halves (carrier-level third grammar; superset-generator
condition at transport depths) stand; the addition does not.

**Prescribed fix:** §6 item 7 → "Paper 30's residues 3 (fine-vs-coarse
sealing, empirical), 4 (mid-chain drift), **and 6 (`h12` dead-component
pricing)** stand unchanged; residue 5's two breadth halves stand, **while the
entry-condition addition paper 31 attached to it — decide whether arbitration
alone generates dimension — is discharged by §3.1 (it does not)**."

---

### MAJOR-7 — §3.2 carries "width 2n − 1" into a schema sentence the receipt explicitly refuses to make all-n

**Paper §3.2:** "…realizes S_n as an induced subposet of an admissible
pure-transport record at every n in {3, 4, 5, 6} …(actors n^2 + 3n, events
2n^2, **width 2n − 1**, every event admission-priced at the uniform exact
weight 1/(4(n^2 + 3n − 1)); … [EXACT]. **The all-n statement is a theorem at
the schema level** … [THEOREM, all n, at the schema level]."

**The receipt** (`d45b_sn_ladder_exact.out` line 387):

> "width measured at the base cases: f(3) = 5, f(4) = 7, f(5) = 9, f(6) = 11
> [**MEASURED = 2n − 1 at all four base cases**; each >= n as dim <= width
> requires; **the all-n width formula is NOT claimed**]"

ZG3.1 gates the closed forms for actors, events, crown selection and per-event
weight — and *not* width. The all-n proof note (`note-d45b` §8) likewise
proves admissibility, the cone topology and the incomparabilities, and states
its closed forms as "actors n² + 3n, events 2n², uniform weight
1/(4(n² + 3n − 1))" — no width. Paper 32 places "width 2n − 1" in the same
parenthesis as three schema-gated formulas and then, one sentence later,
promotes the schema to a theorem for all n. A reader carries the width across;
the receipt forbids it. This is the campaign's signature failure mode
(over-broad quantifier by adjacency) reappearing in the paper.

**Prescribed fix:** move width out of the schema parenthesis —
"(actors n^2 + 3n, events 2n^2 and the uniform exact weight
1/(4(n^2 + 3n − 1)), all three gated as closed forms; the realized widths are
5, 7, 9, 11 — 2n − 1 at all four base cases [MEASURED; the all-n width formula
is not claimed])".

---

### MAJOR-8 — §5's "(widths 1-4, both lattice sizes, both masses)" overstates the slab collapse; at L = 12 the LT collapse is gated only for w <= 2

**Paper §5:** "The slab-smeared identification collapses, at every wrap-clean
cell (**widths 1-4, both lattice sizes, both masses**), onto the singleton ray
with the singleton constant — slab-width independence, the fixture-scale
content of the finite-slab theorem [EXACT]".

**The receipt's own careful form** (`[KG1 THEOREM]`, `.out` line 130):

> "every wrap-clean cell collapses to the SINGLETON ray and constant — EXC = 1
> and LT = kappa(m) at ALL w in {1,2,3,4} (**all w at L=16; w <= 2 plus all EXC
> at L=12**): slab-width INDEPENDENCE"

Eight cells — (L=12, m ∈ {1/2, 1}, w ∈ {3, 4}, COMPOSITE|BLOCK), LT — are
wrap-contaminated, excluded from the theorem gate, and carry *different*
constants (3229/278784, 151/2304, 7643/288000, 1079/9216, −277/34848,
53/1152, 1409/72000, 281/2304 — `[KG1 WRAP RECORD]`). The paper's parenthetical
is defensible only if read as "the sweep grid was widths 1–4 × both L × both
m"; every natural reading is "the collapse holds at widths 1–4 at both lattice
sizes", which is false. 48 of 56 cells are clean.

**Prescribed fix:** "(the 56-cell sweep is widths 1–4 × both lattice sizes ×
both masses; **48 cells are wrap-clean and all 48 collapse — all widths at
L = 16, and at L = 12 all EXC cells plus LT at w <= 2; the 8 declared L = 12
LT wrap cells at w = 3, 4 are finite-seam artifacts excluded from the theorem
gate, their L = 16 twins clean**)".

---

### MAJOR-9 — §3.1's two headline facts are referee-carried and are printed as receipt facts

§1 establishes the convention: "'referee-carried' marks facts verified in a
frozen review record rather than gated in a receipt." §3.1 then states, with no
tag:

1. **"Zero failures of two-dimensionality across 1,124,884 distinct
   admissible proposal/arbitration histories".** The number 1,124,884 appears
   in **no receipt**: `d44c_arb_dimension_exact.out` prints 1,213,372 (AG3,
   `[VERDICT]`). 1,124,884 is the frozen round's F2 correction
   (`d44c-round1-hostile-review.md` lines 95–112, "1,213,372 is the number of
   history-CHECKS … Distinct histories = 1,124,884"), carried at #354/#355 and
   re-derived here by both routes (see the sweep). It is a *correct* number,
   referee-derived, and the paper's own convention requires the tag.
2. **"plus every constructor state at widths 3-6".** `note-d44c` §6 **B3**:
   "The verdict's 'every constructor state' clause: the 340 F-CROSS post-X
   states were **never dim-checked in-receipt** (AG2c's label says so). The
   referee rebuilt and dim-checked all 340: ZERO failures — **the claim is
   TRUE, referee-carried**; the gate's absence is recorded."

Compare §4.2 and §4.3, where the paper *does* apply the tag correctly ("gated
4-of-8 in-receipt with all 8 referee-carried"; "its {+-1}^3 exhaustiveness
characterization is referee-carried") — so the convention is understood and
simply not applied where the stakes are highest.

**Prescribed fix:** "Zero failures of two-dimensionality across 1,124,884
distinct admissible proposal/arbitration histories (**the distinct count is
referee-carried: the receipt prints 1,213,372 history-checks, which
triple-counts the 44,244 no-idle width-3 <= 6-event histories shared by the
three families; forward-corrected at LOG #354**) … plus every constructor
state at widths 3-6 (**referee-carried: the 340 F-CROSS post-X states were
dim-checked in the frozen round, not in-receipt**)". Related: §3.1's
"gated, zero violations" should also note the dense dedup audit (0 mismatches
over all 1,131,500 arb-containing histories) is referee-carried (B4(i)).

---

### minor-1 — §2.1 mislabels the depth-7 level as a family "at depth <= 7"

"verified exhaustively over the ENTIRE families at depths **<= 6 and <= 7**
(34,375 and 145,408 histories; 179,783 in all)". 34,375 is the cumulative
depth-0..6 family (SG0: [1,7,39,215,1191,6471,34375]); 145,408 is the
depth-7 **level** (CG7a: "children of the 27,904 depth-6 cache members"). The
family at depth <= 7 is 179,783. **Fix:** "over the entire family at
depth <= 6 (34,375 histories) and the full depth-7 level (145,408; 179,783 in
all)".

### minor-2 — §2.1 calls H0's content "provably … gated"; §2.2 lists it as an unproved hypothesis

§2.1: "each actor's non-superseded holding (**provably** singleton-or-empty at
this scope, gated)". §2.2: "(H0) the view invariants … all exhaustively
verified through depth 7 (**evidence for the hypothesis, never a premise of
the argument**)". `note-d44a` §8 is explicit that H0 is a depth-indexed
hypothesis, not a lemma. "Provably" contradicts the paper's own next
subsection. **Fix:** "verified family-wide at the gated depths (this is H0 of
§2.2's conditional, not a proved lemma)".

### minor-3 — §2.3 "agrees blockwise at its computable lookaheads" hides the one disagreement

`d44b` TG1: "blockwise agreement P_t vs P_(t+1) per window: **t=0 on len<=3
(521 h): False**; t=1 on len<=2 (69 h): True; t=2 on len<=1 (9 h): True; t=3
… [TRIVIAL WINDOW]". The receipt says "agrees blockwise at t = 1 and t = 2 on
their (shallow) windows"; the t = 0 → 1 step genuinely splits (the exhibited
pair [pA0] vs [pA0, dABv0], equal menu shapes, differing rows) — and the
d44b round declared STAB = *two* blockwise agreements precisely because the
d43b three-consecutive standard is unmeetable at this cap (`note-d44b` B4).
**Fix:** "agrees blockwise at t = 1 and t = 2 on their shallow windows (the
t = 0 → 1 refinement genuinely splits — the criterion is the declared
two-agreement form, the d43b three-consecutive standard being unmeetable at
this cap)".

### minor-4 — §6.2's rendering of the binding d44b flag changes its content

**Paper §6.2:** "(Nothing at transport scope may cite the delivery-free
per-candidate distinction as load-bearing: at the tested cap it is
extensionally null there — recorded.)"

**The flag** (`note-d44b` §6 B5): "the **per-class-aggregate mutant** is
EXTENSIONALLY NULL at this cap (recorded so no successor cites d44b as proof
**the per-candidate distinction bites** at transport scope — it does not,
here, by measurement)". The null object is the per-candidate-vs-aggregate
*operator distinction*, and the prohibition is on citing d44b as *proof that
it bites*. The paper's phrasing forbids treating the per-candidate refinement
as load-bearing at transport scope — which contradicts d44b's own TG2 verdict
("the intrinsic refinement is load-bearing, the d44a per-candidate lesson
carried"). **Fix:** "(No successor may cite d44b as proof that the
per-candidate-versus-aggregate operator distinction bites at transport scope:
at the tested cap the aggregate mutant is extensionally null there —
recorded. The intrinsic refinement itself *is* load-bearing at transport
scope: menu shape does not factorize the transfer, 2/9 classes.)"

### minor-5 — §4.1 omits the census-vs-gating completeness split and the three declared residual grains

RG4-d gates the two notions separately and the receipt's verdict carries both:
"CENSUS-completeness = 11/11 types …; GATING-completeness = 9/11 types
amplitude-gated with firing controls + 2/11 receptionless-classical gated
(n, v0); ungated TYPES: 0; **declared residual GRAINS: 3** (|C| >= 3 chains,
re-merge, transport depth)". The paper says "census-complete" (true) and flags
the dynamics arm (true), but never states that gating-completeness is narrower
by exactly three declared grains — including that the full d42b1 depth-4
transport family was **not** enumerated (RG4-c). Given the abstract's "the
per-type reception census is complete at fixture scope", the grains belong in
the body. **Fix:** append to §4.1 — "gating-completeness is narrower than
census-completeness by exactly three declared grains (|C| >= 3 click chains,
merge-of-merge, transport depth — the d/m types are censused and gated at the
SIG-chain fixture grain, the full transport family unenumerated)".

### minor-6 — §5's ((w+1)/2)^2 sentence drops the half that makes it a finding

Paper: "the literal block-region variant carries an exact ((w+1)/2)^2
normalization law while the ray never moves." The receipt's finding is
sharper and has a third clause: "**EXC** = ((w+1)/2)^2 exactly (1, 9/4, 4,
25/4; mass- and L-independent) — the literal block-region EXC normalization
carries the collar-length square **while its ray is unchanged and the LT
constant is untouched**". As written the paper suggests a normalization law on
the block arm generally; it is EXC-only, and the LT constant's invariance is
the point. **Fix:** "the literal block-region variant carries an exact
((w+1)/2)^2 normalization on its **EXC** constant (1, 9/4, 4, 25/4; mass- and
L-independent) while its ray is unchanged and the **LT** constant is
untouched".

### minor-7 — §8's coda drops both caps in the sentence immediately before "Every claim above carries its cap"

"The quantum layer no longer floats: **its weights are the completion's**, its
foliation freedom is one tag of authorship". §4.3's actual statement is
"FORCED … **at verified-depth scope**; the all-depth form is conditional on
H1, and transport-scope closure remains open", all at **fixture scale**
(MG3-a: "NO CONTINUUM CLAIM"). A coda that drops both caps one sentence before
asserting that every claim carries its cap is the quotable sentence a hostile
reader will lift. **Fix:** "its weights are the completion's at verified depth
and fixture scale".

### minor-8 — §2.1's blockwise equality is stated flatly; its len <= 5 leg is referee-carried

`note-d44a` §8: "blockwise equality of the pullback with the committed
intrinsic partition is **COMPUTED at len <= 4 in-receipt and len <= 5 by the
frozen round's referee**; the four minlen-6 sigma-states are classified only
via the conditional argument." §2.1 says "blockwise equal to the committed
intrinsic partition" with no scope. **Fix:** "blockwise equal to the committed
intrinsic partition (computed at len <= 4 in-receipt, len <= 5 referee-carried;
the four minlen-6 states are classified by the conditional argument alone)".

### minor-9 — references: two entries are unused, one used source is dropped, one is bibliographically bare

- **FLP 1985 and Ben-Or 1983** (reference 3, "the consensus/vector-clock
  imports") are cited nowhere in paper 32's body — the words "consensus",
  "Fischer", "Ben-Or" do not occur outside the reference list. They are
  paper 31's imports (its §4.2 visibility-vs-scheduling disanalogy), carried
  over vestigially. Either cite them where the disanalogy is used or drop them.
- **Aldous–Lyons** (paper 31 reference 10, "the mass-transport principle") is
  *used* — §2.1 and the abstract both assert "mass transport exact with
  pi = (1,1,2)/4" — and is **absent** from paper 32's list. Restore it.
- **Charron-Bost** is the only external source doing real work in §3.3 and is
  the only one with no title, venue or year ("the Charron-Bost size-of-clocks
  line [LITERATURE]"). Give it the same treatment as Meyer/FFT: title, journal,
  year (`note-d45b` §3 states the content being ported).

### minor-10 — §1 declares two provenance labels the paper never uses, and does use MEASURED content untagged

"[MEASURED]" and "[POSITED]" are declared in §1 and appear nowhere in the
body, while genuinely MEASURED quantities are present and untagged — the S_n
widths (MAJOR-7), d44b's escape/diverged censuses (descriptors at a declared
cap), d44c's class/mass distributions. Either apply the labels or trim the
declared set to those in use.

### nit-1 — §3.3 "248 reach order dimension 3"

The gate is `dim<=2 == False` (ZG1S.2), i.e. dimension >= 3; the receipt's own
verdict prose says "reach dimension 3", so the paper inherits it faithfully,
but ">= 3" is free and exact.

### nit-2 — §4.3 "a seven-row gated dictionary"

MG3-a: "the dictionary was PRINTED (7 rows) and **each substantive row** is
gated (FG0-d bare weights; MG2-b multipliers; MG2-c normalizers and ratios)".
"Seven-row dictionary, its substantive rows gated" is the exact form.

### nit-3 — §1 "LOG ##353-374"

Double hash; elsewhere the series writes "LOG #NNN". Also the eight terminals
span #353–#374 but the campaign's own closing entry is #375 — consider
"(LOG #353–#374; synthesis #375)".

---

## Number-sweep inventory

**61 quantitative claims checked; 0 mismatches.** Independent recomputation of
11 reductions (exact `Fraction` / integer arithmetic; script and commands in
the reproduction appendix). Every claim below was traced to a `[PASS]` line, a
delivered-verdict line, or a frozen-review line, and the provenance recorded.

| # | Paper claim (§) | Source | Verdict |
|---|---|---|---|
| 1 | 179,783 histories (abs, §2.1, §2.2) | d44a `.out` CG1+CG7a; note §8 | ✅ recomputed 34,375 + 145,408 = 179,783 |
| 2 | 34,375 depth-<=6 family (§2.1) | d44a SG0 `[1,7,39,215,1191,6471,34375]` | ✅ |
| 3 | 145,408 depth-7 (§2.1) | d44a CG7a | ✅ (but see minor-1 on "<= 7") |
| 4 | 27,904 depth-6 parents (implicit) | d44a CG7a | ✅ 34,375 − 6,471 = 27,904 |
| 5 | 36 states (abs, §2.1) | d44a CG3a | ✅ |
| 6 | 176 edges (§2.1) | d44a CG3a "traversed edges = 176" | ✅ |
| 7 | 176 abstract keys (§2.1) | d44a CG7c (160 cached + 16 new) | ✅ total |
| 8 | six-class quotient (abs, §2.1) | d44a CG3c/CG3f trajectory [4,5,6,6] | ✅ |
| 9 | lambda = 2 rational (§2.1) | d44a CG5b | ✅ |
| 10 | det 3/32 M-matrix certificate (§2.1) | d44a CG5c | ✅ |
| 11 | f = (4,4,3,7,3,3)/3 (§2.1) | d44a CG5b/c f = (4/3,4/3,1,7/3,1,1) | ✅ recomputed identical |
| 12 | pi = (1,1,2)/4 (§2.1) | d44a CG5e (1/4,1/4,1/2) | ✅ recomputed identical |
| 13 | root = renewal as one sigma-state (§2.1) | d44a CG5d, SG3 | ✅ |
| 14 | 3,969 ARM-1T histories (§2.3) | d44b TG0a | ✅ |
| 15 | 3,969 transport menus, 0 d42a matches (§2.3) | d44b TG6b "0/3969" | ✅ |
| 16 | three-actor arm depth 3, census only (§2.3) | d44b TG1s/TG7 (3,424) | ✅ |
| 17 | 1,044 diverged histories (abs, §2.3) | d44b TG3a | ✅ |
| 18 | 124 reconverging pairs (abs, §2.3) | d44b TG3b | ✅ |
| 19 | 84 distinct diverged prefixes (abs, §2.3) | d44b `note` B3 / gate | ✅ |
| 20 | 4 distinct minimal 3-event chains (abs, §2.3) | d44b `note` B3 | ✅ |
| 21 | weight 1/256 (abs, §2.3) | d44b TG3 witness | ✅ |
| 22 | every reconverging pair-history ends non-diverged | d44b B3 | ✅ |
| 23 | delivery row into non-diverged class (§2.3) | d44b TG3c (1/8 branch) | ✅ |
| 24 | six classes on len <= 2 (abs, §2.3) | d44b TG1 | ✅ |
| 25 | 68 escaping transitions (abs, §2.3) | d44b TG4 | ✅ |
| 26 | 5 above-window classes [6,7,8,9,10] (abs, §2.3) | d44b TG4 | ✅ |
| 27 | menu-shape factorization fails, 2/9 (§2.3) | d44b TG2 | ✅ |
| 28 | 1,124,884 distinct histories (§3.1) | **review** F2 / LOG #354 | ✅ recomputed **both** routes: 1,213,372 − 2×44,244 = 1,124,884 and 551,928 + 180,336 + (436,864 − 44,244) = 1,124,884 — **provenance untagged, MAJOR-9** |
| 29 | width 3 to 6 events with idles (§3.1) | d44c AG1 cap | ✅ |
| 30 | to 7 without (§3.1) | d44c AG1b cap | ✅ (recomputed 6+30+180+1356+7176+35496 = 44,244 overlap) |
| 31 | width 4 to 6 without (§3.1) | d44c AG2b cap | ✅ |
| 32 | every constructor state widths 3-6 (§3.1) | **note B3, referee-carried** | ✅ true — **untagged, MAJOR-9** |
| 33 | six-clause law "gated" (§3.1) | d44c AG3 gates **five** | ❌ provenance — **BLOCKER-1** |
| 34 | funnel lemma [THEOREM] (abs, §3.1) | **note B4(iii), referee-carried** | ❌ provenance — **BLOCKER-1** |
| 35 | S_n at n ∈ {3,4,5,6} (§3.2) | d45b ZG2.3–2.6 | ✅ |
| 36 | actors n^2 + 3n (abs, §3.2) | d45b ZG3.1 | ✅ recomputed 18/28/40/54 |
| 37 | events 2n^2 (abs, §3.2) | d45b ZG3.1 | ✅ recomputed 18/32/50/72 |
| 38 | width 2n − 1 (§3.2) | d45b line 387 **MEASURED, all-n NOT claimed** | ✅ values 5/7/9/11 — **scope, MAJOR-7** |
| 39 | weight 1/(4(n^2+3n−1)) (§3.2) | d45b ZG2.Na, ZG3.1 | ✅ recomputed 1/68, 1/108, 1/156, 1/212 |
| 40 | comparability matrices = S_n exactly (§3.2) | d45b ZG2.Nc | ✅ |
| 41 | whole posets fail dim<=2 (§3.2) | d45b ZG2.Nd | ✅ |
| 42 | all-n schema [THEOREM] (§3.2) | `note-d45b` §8 proof note | ✅ (proof note exists; contrast BLOCKER-1) |
| 43 | 8! = 40,320 (§3.3) | d45b ZG1S.2 | ✅ recomputed |
| 44 | 248 dim>2 schedules (§3.3) | d45b ZG1S.2 | ✅ |
| 45 | minimum 4 violations (§3.3) | d45b ZG1S.3 (N = 4) | ✅ |
| 46 | no induced S3 in the sweep (§3.3) | d45b ZG1S.4 | ✅ |
| 47 | bare deliveries never escape (§3.3) | d45b ZG1S.6 | ✅ |
| 48 | CB ports dim<=2 at N = 3,4,5 (§3.3) | d45b ZG1.3/4/5 | ✅ |
| 49 | 11 record types (abs, §4.1) | d44e RG0a-iii | ✅ (8 kinds + 3 version constructors) |
| 50 | 6,567 instances (abs, §4.1) | d44e RG0 / RG0-ANCHOR | ✅ (4,502 + 1,939 + 90 + 36) |
| 51 | 1,191-member depth-4 family (§4.1) | d44e RG0b-i | ✅ |
| 52 | (actor,base) key 0/1,191 (§4.1) | d44e RG0b-iii | ✅ |
| 53 | exactly 4 multi-creator versions (§4.1) | d44e RG2-v.arb / RG2-ANCHOR | ✅ |
| 54 | mutual exclusion 4-of-8 gated, 8 referee-carried (§4.2) | d44f FG2-c + review nit-1 | ✅ **correctly tagged** |
| 55 | seven-row dictionary (§4.3) | d44f MG3-a | ✅ (nit-2 on "gated") |
| 56 | (1/2, 1/4, 1/4) sector conditional (abs, §4.3) | d44f MG2-d/d2 | ✅ recomputed from (2/23, 1/23, 1/23) |
| 57 | gated at depths 4 and 5 (§4.3) | d44f MG2-d, MG2-d2 | ✅ |
| 58 | {+-1}^3 exhaustiveness referee-carried (§4.3) | d44f review r-n3 | ✅ **correctly tagged** |
| 59 | ((w+1)/2)^2 = 1, 9/4, 4, 25/4 (§5) | d44d `[KG1 BLOCK ARM]` | ✅ recomputed — **not exit-gated, MAJOR-2** |
| 60 | kappa(m) = (9m^4−15m^2+4)/144 = (3m^2−1)(3m^2−4)/144 (abs, §5) | d45a YG1; d44d KG2-D | ✅ recomputed: expansion identity exact; kappa(1/2) = 13/2304, kappa(1) = −1/72; roots x = 1/3, 4/3 |
| 61 | 1/16 vs 1/24 merge price (§6.6) | d44e RG0b-iv (D2H) | ✅ |
| — | PASS surface 30/14/15/17/49/29/22/49 (§7) | eight `.out` `[SUMMARY]` lines | ✅ all eight exact |

**Mismatches: none.** Every discrepancy in the Findings above is a scope,
provenance, ledger-completeness or supersession-accuracy defect, not a wrong
number. The paper's "hundreds of independently recomputed values, zero false
numbers" survives this round at paper level.

**One referee-computed addition** (not a receipt fact, offered for MAJOR-4):
kappa(m) = 1 ⟺ 9x² − 15x − 140 = 0 in x = m², discriminant 5265 (not a perfect
square), single positive root x = (15 + √5265)/18 ≈ 4.8645 (m ≈ 2.2056),
outside D44d's grid hull [1/16, 2] and inside D45a's all-m identity scope.

---

## Attack surfaces that did NOT convict

- **Ladder hazard (#380–#389).** Zero leakage; §6's ledger is exactly the #375
  successor list at #376 state. §6.6's "standing corpus obligation" is correct
  as of #376 (discharged at #378, after the draft).
- **H1 pairing.** Every citation of the decision carries "transport closure
  OPEN" (abs; §2.2's "always and everywhere this decision is cited"; §4.3;
  §6.1; §8). The H0/H1/H2 non-implication and the "evidence, never a premise"
  clause are reproduced faithfully from `note-d44a` §8.
- **"Escape is not non-stabilization"** (§2.3) — stated verbatim in the
  receipt's sense, with "No claim is made about closure at deeper caps".
- **The transport six as ECHO** (abs, §2.3: "a transport-scope ECHO of the
  delivery-free six, a different object") — exact.
- **Initiator-ERASED invariance** (§4.2) — matches the d44f review's
  prescribed fix word for word, including "the residual foliation datum is
  ITSELF RECORD DATA (it propagates into future version names)". No trace of
  the retracted "the physics is foliation-invariant".
- **Census-vs-dynamics split** (§4.1) — "NOT layer-semantic reception
  dynamics: the dynamics arm is typed and remains open"; R6 correctly
  described as discharged on its census arm (§4.1 + §6.5). (minor-5 is about
  the *grains*, not the split.)
- **Interacting divergence grain-inherited** (§5) — "but grain-inherited (the
  g = 0 control is also divergent) … whether RAY-level universality survives
  interaction is undecided" — exactly D44d's MAJOR-1 rescope, with the g = 0
  column assigned to the successor.
- **Order-dimension doctrine** (§3.4) — the strongest section in the paper:
  the round-cone/infinite-DM-dimension statement, "necessary … and NOT
  sufficient", "never a spacetime-dimension estimator", and the explicit
  hand-off of Minkowski certificates to successors, all matching `note-d45b`
  §1 verbatim in content.
- **Single-threaded voice.** No round is catalogued, no referee is named, no
  correction history is narrated as such; §7's meta-sentence is the only
  process statement and it is a methods claim (its content is MAJOR-3's
  problem, not a voice problem). Passes the series style rule.
- **Precision statements (§7)** — exact rationals where claimed; dps 50 /
  1e-30 for D44d; dps 50 / 1e-40 where the operator family enters (d44e,
  d44f); zero floats for D45a (YG4-A/B). Determinism + hash-seed variation is
  independently recorded per unit in the frozen rounds (PYTHONHASHSEED 0/7
  reruns in d44a/b/c/d/e and d45b review appendices).
- **Internal PASS-count consistency** — abstract, body, §6, §7 agree; no
  count appears twice with different values anywhere in the paper.

---

## Disposition

**REVISE.** BLOCKER-1 must be cleared before any external circulation: either
demote the funnel lemma to referee-carried (cheap, textual) or meet LOG #355's
paper-grade promotion condition (a small receipt + proof note). The nine
MAJORs are all textual except MAJOR-6's ledger restoration, and none of them
touches a number. Once BLOCKER-1 and MAJOR-1/2/3 (the §7 methods block),
MAJOR-4/5/6 (the supersession/ledger block) and MAJOR-7/8/9 (the three
uncapped/untagged claims) are applied, this paper is accurate to its
artifacts — and it will be the first paper in the series whose number sweep
came back clean at paper level on the first round.

Recommended round-2 scope: verification of the applied repairs only (a delta),
plus a re-scan of §1.3/§6 against papers 30 and 31 after the additions, since
supersession completeness is the one axis where a repair can introduce a new
gap.

---

## Reproduction appendix

All commands from `/Users/felixrobles/workspace/isp` (working tree clean at
review time; `git log -1 --oneline -- v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md`
→ `1610689 v10 paper 32 FULL DRAFT (LEDGER #376)`).

```bash
# 1. the object and its integrity
md5 -q v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md
#   18103a45b41a1c88da0d1e68986448fe
git status --porcelain          # empty

# 2. the eight PASS surfaces (§7 table)
grep -H "SUMMARY" v10/data/d44{a_closure_theorem,b_transport_invariance,\
c_arb_dimension,d_slab_kappa,e_reception_census,f_foliation_measure}_exact.out \
                 v10/data/d45{a_symbolic_kappa,b_sn_ladder}_exact.out
#   30 / 14 / 15 / 17 / 49 / 29 / 22 / 49  — all match

# 3. the 1,124,884-vs-1,213,372 provenance (MAJOR-9)
grep -rn "1,124,884\|1,213,372" v10/data/ v10/reviews/ v10/LOG.md v10/note-d44c-*.md
#   .out prints only 1,213,372; 1,124,884 lives in the review, the note, the LOG

# 4. the five-vs-six clause count (BLOCKER-1)
grep -n "(i)\|(v)\|SIXTH\|sixth\|FUNNEL" v10/data/d44c_arb_dimension_exact.out
grep -n "SIXTH\|FUNNEL\|referee-carried" v10/note-d44c-multiauthor-arb-dimension.md
sed -n '/D44c TERMINAL (LEDGER #355)/,/D45 AUTHORIZED/p' v10/LOG.md   # promotion condition

# 5. the slab coverage (MAJOR-8)
grep -n "KG1 THEOREM\|KG1 WRAP RECORD\|WRAP\]" v10/data/d44d_slab_kappa_exact.out

# 6. the width-2n-1 scope (MAJOR-7)
grep -n "MEASURED = 2n - 1\|NOT claimed\|ZG3.1" v10/data/d45b_sn_ladder_exact.out
```

Independent recomputation (exact integer / `Fraction` arithmetic, no
tolerances):

```bash
python3 - <<'PY'
from fractions import Fraction as F
import math
assert 34375 + 145408 == 179783                      # sweep #1
assert 34375 - 6471 == 27904                         # sweep #4
assert sum([6,30,180,1356,7176,35496]) == 44244      # AG1b overlap
assert 551928 + 224580 + 436864 == 1213372           # receipt's checks count
assert 1213372 - 2*44244 == 1124884                  # route A
assert 551928 + 180336 + (436864 - 44244) == 1124884 # route B
assert math.factorial(8) == 40320                    # sweep #43
for n,(a,e,w,q) in zip((3,4,5,6),
        ((18,18,5,F(1,68)),(28,32,7,F(1,108)),(40,50,9,F(1,156)),(54,72,11,F(1,212)))):
    assert (n*n+3*n, 2*n*n, 2*n-1, F(1,4*(n*n+3*n-1))) == (a,e,w,q)   # sweep #36-39
k = lambda x: F(9*x*x - 15*x + 4, 144)               # x = m^2
assert k(F(1,4)) == F(13,2304) and k(F(1)) == F(-1,72)                # sweep #60
assert all((3*x-1)*(3*x-4) == 9*x*x-15*x+4 for x in (F(a,7) for a in range(-20,20)))
assert k(F(1,3)) == 0 and k(F(4,3)) == 0
assert [F(w+1,2)**2 for w in (1,2,3,4)] == [F(1),F(9,4),F(4),F(25,4)]  # sweep #59
tot = F(2,23)+F(1,23)+F(1,23)
assert (F(2,23)/tot, F(1,23)/tot) == (F(1,2), F(1,4))                  # sweep #56
assert [F(4,3),F(4,3),F(1),F(7,3),F(1),F(1)] == [F(c,3) for c in (4,4,3,7,3,3)]
assert [F(1,4),F(1,4),F(1,2)] == [F(c,4) for c in (1,1,2)]
print("11 reductions reproduced, 0 mismatches")
PY
```

Ladder-hazard scan (attack surface 4):

```bash
grep -n "d46\|D46\|Martin-at-transport\|Minkowski certificate\|typicality" \
     v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md
#   single hit: line 343, §6.3's typicality QUESTION — verbatim the #375
#   synthesis successor 3, not a D46d result. No D46 unit referenced.
```

Supersession scan (attack surface 3):

```bash
sed -n '688,760p' v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md  # §7 ledger
sed -n '131,163p' v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md  # §1.3
grep -n "^\*\*[0-9]\." v10/relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md
#   paper 30 §9 residues 1..6; residue 6 = h12 dead-component pricing (MAJOR-6)
```
