# ECC (paper-46) — EFFECTUS seat review (K2): LICENSURE

**Seat:** K2 / EFFECTUS. Jurisdiction: whether every sentence, word and label in
the delivered paper is licensed by what was actually measured — overclaim,
underclaim, scope smuggling, unlicensed vocabulary, unstated dependencies.
**Reviewed:** 2026-08-16, against v15 ledger #44/#45.
**Unit verified at the committed digests** (sha256-12, all recomputed by this
seat before reading): paper-46-ecc.md `61d330d13fe0`; code/ecc_exact.py
`4d2034429d21`; code/ecc_output.txt `3034f0028bb3`; code/ecc_receipt.json
`ea24c1fc2340`; note-ecc-pin.md `04874b01e241`; parents 43/47/44/45 at
`0c8d1a687b14` / `5da53943c6f7` / `0d677a4cbe97` / `fa0268d99524`. Charter:
v15/PLAN.md as amended through #40.

**Method.** Word-by-word head audit against the receipt's primitive tables,
independent of the instrument's own comparator; line-by-line licensure sweep
of §1–§14 against gates and receipt paths; code audit of every gate my charge
names; a plant battery against a full mirror of the unit under my scratch
(`scratchpad/ecc_k2/mirror/`, never the repo): 8 fresh paraphrases of the
five forbidden claims, 2 gate-mechanism probes, 2 mechanism-isolation twins
and 4 in-pattern controls, all through the committed instrument's own
`--verify-paper`; 6 targeted `--mutant` deaths and the full 73-recipe
`--selftest`, on the mirror, write-nothing, one process per probe. No unit
file was modified; my only repo write is this review.

## VERDICT: ACCEPT-WITH-FIXES

No false measured number anywhere: every numeral, fraction and hyphenated
count in all five head segments and in §1–§12 prose re-derives exactly from
the receipt's primitive row tables where those exist. The order disciplines
the pin demands (seam before Born; normalization sealed before any
feasibility row) hold in the ledger and in the actual call order. The
findings are licensure findings: two MAJOR — both false sentences about the
instrument's own guarantees, not about physics — two NEW wall-bypass species
measured by this seat's plants, and a set of minor wording/labelling
repairs. Nothing requires re-measurement; no head numeral moves.

---

## Findings

**E-1 (MAJOR). §11's outcome-feasibility clause is false of the
instrument.** paper-46-ecc.md:678–683: "…so no outcome of the
pre-registration is a word this instrument cannot emit." Several
pre-registered not-reached words have no emission path at all:
`SEAM-PERSISTENT-SUPPORTED`, `PSI-ONTIC` and
`ECC-CIRCULARITY-UNTYPABLE-AT-THE-TABLE` occur in the code only as strings
of the prereg pair table (ecc_exact.py:3049, 3057, 3065; 3079 for
`ECC-BLOCKED-AT-THE-CARRIER`), and the delivery gates hard-require the
reached arm: G-SEAM-DECISION requires the word to start with
`SEAM-DECISION-UNDERDETERMINED-AT-` (3897–3906), G-PSI-EQUAL requires
agreements == rows and separating == 0 (4050–4057), G-INTERFACE requires
every row's class among the four words (3925–3927), and G-LP-COMMITTED pins
the committed row's word AND value (INFEASIBLE, qmax 4/9; 4105–4110) — so
even ECC-LP-UNIQUE, though demonstrated on real rows elsewhere, could never
be emitted as the committed verdict. A run in which any other arm is
measured ends as a REFUSAL, not as the other verdict word. The clause claims
a #299 word-emitability the instrument does not have. The rest of the same
sentence is true and gated (stems located by G-OUTCOME-FEASIBILITY; both
arms' predicates and witnesses at receipt `outcome_prereg.pairs`; all four
LP words fire — `outcome_prereg.lp_words_fired` 4/4). Fix: restrict the
clause to the four LP words, or state that the not-reached arms are
refusal-shaped by construction.

**E-2 (MAJOR). §12's comparator claim is false at nine head positions.**
paper:707–710: the comparator "…reads no summary scalar: every count in
every segment is re-derived from the receipt's primitive row tables" — and
the pin's standard (note-ecc-pin.md:131–133) engraves the same. In
`reconstruct()` at least nine head numerals are READ from receipt summary
scalars, not re-derived: `cited_free` = the second 15 of
FREE-DECLARATIONS-CARRIED (ecc_exact.py:3201), `actor_cycle` = 4 (3208),
`probes` = 11 and `relation_values` = 2 (3222–3223), `faces` = 3 (3251),
`distinct_targets` = 39 (3255), `undefined_targets` = 2 (3276),
`scale` = 3 and `covered` = 27 (3277–3279). For several of these the
receipt carries no primitive table from which the value COULD be re-derived
(the probe list, the target list, the dependency-edge list and CONTRACT's
parsed free count are not serialised), so at those positions the
"independent" rendering reads the same stored value the builder measured —
the de-twinning provides no independence there, and a corruption of that
scalar between measurement and head would pass the comparator. The majority
of head positions ARE genuinely re-derived from row tables (objects,
backings, senses, categories, arms, maps, state components, blindness,
fiber min/max, differs, stamp count, psi agreements, LP words, dims,
committed rows, ceiling exceptions, carrier predicates, W3 counts — all
verified by this seat), and the debt/normalization primitives are scalars
by nature; the false part is the universal. Fix: serialise the missing
primitives and re-derive, or scope the sentence (and the paper's echo of
the pin standard) to the positions where it is true. Note in the same
sentence: "shares no code and no literal" is defensible only as "no shared
constant object" — the two template texts are separately typed but share
their verdict-word content by necessity.

**E-3 (minor; the REGISTERED condition, measured here). Fresh paraphrases
of all five forbidden claims survive the full battery.** 8 of 8 fresh
plants pass `--verify-paper` on the mirror (table below), covering
Born-derived, seam-measured, parents-unified, gauge-pre-observable and
continuum. This is the registered programme-wide known weakness
(#10/#25/#30), reconfirmed at ECC; the walls do fire on in-pattern text (my
4 controls all die at their declared gates). Note especially F5 — "The
parents unify as written at the committed row." — the paper's central
verdict inverted in fresh words survives: G-PAPER-POLARITY scans five
canned inversions only (ecc_exact.py:4565–4571) and no wall owns the
unification-claim family. Recommend a polarity entry for it at repair.

**E-4 (minor, NEW species). NEG-guard bypass: an in-pattern forbidden claim
passes when an incidental negation word opens the sentence.** Measured:
"The gauge redundancy is established here." → REFUSED at G-WALLS; "No
reader will doubt that the gauge redundancy is established here." → PASS.
Mechanism: Wall.scan's excuse loop (ecc_exact.py:836–846) excuses any
negative-pattern hit whenever NEG (766–767) matches in the sentence lead
and neither REASSERT (769–772) nor the clause exclusion fires; "No reader…"
is neither idiom nor clause. The guard built to excuse negated mentions
excuses an asserted violation. Register alongside #10/#25/#30 as its own
species.

**E-5 (minor, NEW species). Licence-token laundering: one stapled licence
word flips a licence-leg violation to licensed.** Measured: "The
reproduction derives the Born rule outright." → REFUSED at G-WALLS; "The
reproduction, being gated, derives the Born rule outright." → PASS (licence
`\bgated\b`, ecc_exact.py:3371–3375). Licence tokens are lexical, not
semantic; `declared` is a licence on five of the nine walls, `theorem` on
W3, `branch`/`fork` on the event-fork wall. Register as its own species.

**E-6 (minor). The receipt's psi stamp label misattributes the mechanism
for 197 of 215 stamped rows.** Receipt `stamps.stamp.psi =
"FACE-INDEPENDENT-BY-BYTE-EQUALITY"` blankets all 215 rows (`stamps.rows`:
156 lp.row.* + 39 lp.branch.* + 18 psi.row.* + carrier.family +
debt.census), but byte equality was measured only at the 18 psi rows
(`psi.rows`; records R0/ROUND-A/ROUND-B), while the LP consumes
uniform-amplitude targets at all 36 round fields (ecc_exact.py:4094–4096).
For every non-psi row the honest mechanism is the reach audit
(`stamps.audit`; 2946–2988) — which is what the paper itself says (352–355,
403–404) and what the G-STAMPS why-string says. Fix in the receipt label or
by one paper sentence. Related observation: the "one accessor"
`born_target` (2483) is arithmetic-identical to the ontic face
`psi_ontic_q` (1336) by inspection, but no gate compares the accessor to
any face at any row; the identification of the accessor's output with "the
Born functional" of the three faces is inspection-licensed, not
gate-licensed.

**E-7 (minor). §5 carries an unlicensed counterfactual, and "delivered
row" is used at two extents.** paper:405–407 "a measurement that separates
the faces would need more than the one-step windows the corpus commits" —
no gate proves this, and the byte-equality census covers 18 rows, not all
one-step windows (non-uniform amplitudes at 34 of the 36 round fields were
never face-compared). The head is honest at the payload level (ROWS=18
names the byte-equality basis; the reach leg is named AUDITED beside it);
this sentence extends past both. Also paper:396–399 uses "every delivered
row" twice in one sentence for the 18-row family defined inline, while §3
and the receipt use "downstream"/"stamped" for 215 rows — one phrase, two
extents. The trilemma is nowhere claimed resolved (head and §5 both say
UNRESOLVED): that leg passes.

**E-8 (minor). The W3 self-description overstates the instrument.**
paper:612–614 "the labels are computed, never typed": in `w3_labels`
(ecc_exact.py:2891–2923) four of five labels are typed literals; only the
LP segment's label is computed (from `ceiling_exceptions == 0`), and
G-W3-LABELS (4223–4231) requires the other four to equal the typed
constant. The error's direction is conservative (member-specific is the
weaker label), and the instrumentation itself is real — the gate exists,
MUT-W3 dies at it (verified on the mirror: REFUSED at G-W3-LABELS, member 5
family 0), labels are rendered into §11 from the receipt with fibres
disclosed — but the sentence is false as written. Same family: paper:667
"holding at every row with a derivation leg" — no machine derivation leg
exists; the ceiling derivation lives in §6 prose and the G-LP-CEILING
why-string, and the gate checks exceptions == 0 plus one structural premise
(4135–4141). Likewise the two-routes normalization identity is measured at
E-BLOCK only (2644–2651) while paper:424–427 says "wherever every event
writes 3 cells, measured as matrix equality" (E-LINE-DECLARED satisfies the
premise, unmeasured; trivially provable, but "measured" it was not), and
the free-two-stage vacuity is a machine-checked coverage premise plus a
prose expressibility step (2652–2659).

**E-9 (minor). "Carried by no fibre" and the compressed family-level label
push past the qualifier.** paper:490–492: the ceiling VALUE one-third is
arity-carried (scale C(a,2)=3 at a=3; the branch census itself shows the
constraint trivialise at a=2); the theorem FORM (q ≤ 1/scale for 0/1
incidence) is what is fibre-free, and the head's own normalization token
says so (…WHERE-EVERY-EVENT-WRITES-3-CELLS). The head also compresses the
qualified label FAMILY-LEVEL-ACROSS-THE-TARGET-FAMILY (receipt
`w3.labels[3]`; §11 table paper:662) to "1-FAMILY-LEVEL" (paper:49); the W3
charter's "family-level" is the ISP fibre family, which was NOT varied (one
arena, a=3, q=3, the committed chart) — the qualifier is the licence and
should survive into the head token or a head-adjacent sentence.

**E-10 (minor). §3's corpus-completeness universals are unlicensed.**
paper:276–277 "every record functional the committed corpus defines at the
union window" and paper:303–305 "The one completion-sensitive quantity the
corpus carries at this window is a lawfulness relation…". The 8-member menu
is this instrument's own constant (`OBSERVABLE_MENU`, ecc_exact.py:
1920–1927); no anchor or gate binds it to a parent-defined exhaustive list.
The verdict word is properly menu-scoped
(…AT-THE-COMMITTED-OBSERVABLE-MENU), so the verdict stands; these two prose
universals are the un-gated bridge from menu to corpus and should be
scoped or cited.

**E-11 (minor). Head token label/value mismatches (values receipt-true).**
(a) `TARGET-UNDEFINED-AMPLITUDES=2` (paper:45) counts target ROWS — one
amplitude, two orders (receipt `lp.undefined_targets` = 2; the paper's own
prose is right at 508–509: "its 2 target rows -- one per coin order"); the
natural reading "2 amplitudes are target-undefined" is false (only the zero
amplitude is). (b) `SEAM-COMPONENT=READING-CONDITIONAL` (paper:33) against
the interface table's and the wall's pinned token READING-RELATIVE
(paper:149–150, 628–629): one concept, two tokens, the head's token pinned
nowhere else.

**E-12 (minor). Small unlicensed or imprecise prose.** (a) paper:122 "and
the two lists differ" (this table vs CONTRACT's census) — no gate or
receipt path compares the lists. (b) paper:507–508 "which is why 136 of the
156 rows read infeasible" — the record fiber accounts for 132 of the 136;
the other 4 are the committed row's class-rows (receipt `lp.rows`: fiber
INFEASIBLE = 132, primary INFEASIBLE = 4). (c) paper:546 "the corpus never
exercises a coherence between branches" — a universal beyond the measured
basis (distinct branch records = 3 at the delivered one-step window).
(d) §10's taxonomy (paper:632–637; also the SCOPE block, 25) — "a count …
or an exact rational Born weight" — does not cover the infeasibility gaps
4|4|3|7/3 (paper:484), which are neither. (e) paper:585–586 "unit mass at
every non-zero declared amplitude" — the debt census counts this at R0
under the delivered order only (ecc_exact.py:2827–2834); G-BORN's
sum-to-one over all defined targets covers the general fact, but §8 does
not say where its 4-of-4 was counted.

**E-13 (minor). The fifth segment's outcome word is pin-anchored by one
verb; the head suffixes of segments three and four are delivery-time
constructions.** This is the step-verb audit my charge ordered.
G-OUTCOME-FEASIBILITY's stem roots (ecc_exact.py:4268–4274) locate
`ECC-CARRIER-FAMILY-UNSELECTED-AND-THE-DEBT-DECIDED` in the pin by the
single word "decided" (N-PIN-DEBT = the step-4 sentence "…decided, not
narrated"); the pin's OUTCOMES section (note-ecc-pin.md:85–101) carries no
carrier/debt reached-arm vocabulary at all, and
"UNSELECTED"/"THE-FAMILY-PUBLISHED" trace to the LP-MANY parenthesis and
step (3) text. Likewise "-AT-EVERY-DELIVERED-ROW" fills the pin's
`<results list>` slot with a quantifier, and
"-AND-THE-CEILING-IS-A-THEOREM" rides inside the `<scope>` slot as a
conjoined second claim. §11's disclosure ("Every reached word is built on a
stem of the pin's own bytes", paper:678–679) is true only under this
weakest stem-level reading, and "one pre-registered outcome pair per head
segment" overstates the fifth pair (its reached arm was not pre-registered
as a word). The underlying facts are measured and true; the fix is one §11
sentence saying the pin pre-registered stems and slots, not whole words,
and no reached-arm vocabulary for steps (3)/(4). On the ceiling itself:
"AND-THE-CEILING-IS-A-THEOREM" is licensed AS STATED — §6 says both legs
explicitly ("is a theorem and the instrument checks it at all 156 rows with
exceptions none", derivation inline at 485–489), the head carries both
tokens (…IS-A-THEOREM and CEILING=…CHECKED-AT-156-ROWS-EXCEPTIONS-0), the
derivation is mathematically valid, and its premises are gated (G-LP-BUILD
structural counts, 4070–4076; G-NORMALIZATION scale, 4080–4091). The head
matches the paper's stated basis.

**E-14 (minor). EQUIVARIANT-OR-DECLARED: the declared tie-breaks are
counted in a side inventory, not "added to the family count in-paper" as
the pin's wall wording requires.** Pin (note-ecc-pin.md:108–110) and PLAN:
"a non-equivariant tie-break = a NEW DECLARATION added to the family count
in-paper". The unit's registry (§11, paper:641–656; receipt `tiebreaks`)
has 1 equivariance-proved and 3 DECLARED choices; the coin order is already
one of CONTRACT's 15, but the probe-family extras and the canonical
container order are new declarations that appear in no family count — the
head still says FREE-DECLARATIONS-CARRIED=15-OF-15 with no combined figure.
Nothing is silent (G-EQUIV-DECLARED and MUT-TIEBREAK are real and the
window's equivariance is measured), but the letter of the wall — the count
— is not delivered. Fix: a one-line combined count or a charter note.

---

## The fresh-paraphrase table (mirror runs, committed instrument, `--verify-paper`)

Baseline: unmodified mirror paper → PASS (~10 s). Each plant is one
sentence appended as a final prose paragraph to a mirror copy; one process
per probe; the repo untouched.

| id | planted sentence | forbidden family | result | classification |
|---|---|---|---|---|
| F1 | The Born rule follows from the event grammar at this row. | Born derived | **PASS** | REGISTERED #10/#25/#30 |
| F2 | This unit proves the Born weights from first principles. | Born derived | **PASS** | REGISTERED #10/#25/#30 |
| F3 | The census settles the seam question: completions persist between events. | seam measured | **PASS** | REGISTERED #10/#25/#30 |
| F4 | Leg two measures which reading the seam obeys, and the answer is re-solved. | seam measured (as re-solved) | **PASS** | REGISTERED #10/#25/#30 |
| F5 | The parents unify as written at the committed row. | parents unified (verdict inversion) | **PASS** | REGISTERED #10/#25/#30 |
| F6 | At the committed row a single probability assignment carries both the Born weights and the grammar. | parents unified | **PASS** | REGISTERED #10/#25/#30 |
| F7 | Two namings of the cells are one physical situation, and the quotient is the arena. | gauge pre-observable | **PASS** | REGISTERED #10/#25/#30 |
| F8 | As the depth grows the record law goes over to a smooth field equation. | continuum | **PASS** | REGISTERED #10/#25/#30 |
| X1 | No reader will doubt that the gauge redundancy is established here. | gauge, IN-pattern | **PASS** | **NEW** (E-4, NEG-guard bypass) |
| X2 | The reproduction, being gated, derives the Born rule outright. | Born derived, IN-pattern licence leg | **PASS** | **NEW** (E-5, licence-token laundering) |
| X1b | The gauge redundancy is established here. | isolation twin of X1 | REFUSED at G-WALLS | mechanism proof |
| X2b | The reproduction derives the Born rule outright. | isolation twin of X2 | REFUSED at G-WALLS | mechanism proof |
| C1 | Persistence is a measured fact of this corpus. | seam, in-pattern | REFUSED at G-WALLS | control |
| C2 | In the continuum limit the census recovers the continuum description. | continuum, in-pattern | REFUSED at G-WALLS | control |
| C3 | Because the two routes agree, the weights are established beyond the fixture. | W1, licence leg | REFUSED at G-WALLS | control |
| C4 | At the committed row the lp is feasible after all. | polarity inversion | REFUSED at G-PAPER-POLARITY | control |

Fresh-or-bypass survivors 10/10: 8 under the registered condition, 2 NEW
species (E-4, E-5). Controls 4/4 dead at their declared gates: the walls
and the polarity gate work as specified on in-pattern text.

## Charge-by-charge disposition

1. **The head, word by word: PASS (with E-2, E-11, E-13 caveats).** Every
numeral and hyphenated token in all five segments re-derived by this seat
from receipt primitives, independently of the committed comparator: seg-1
23 / 18 / 5 / 6 / 15-of-15 / 6 categories / 2 arms / 3 maps / 2+1 / 4
edges; seg-2 8, 8-of-8, 11, 2, 3, 108, 25–43, 108-of-108 twice, 215; seg-3
3, 18, 18-of-18, 0; seg-4 4 + branch, 39, 156, 136 / 8 / 6 (max dim 8) / 6,
39-of-39, 2, qmax 4/9, gaps 4|4|3|7/3, 156 / 0 exceptions, scale 3,
27-of-27; seg-5 4, 4/2/0-of-4, 0-of-36, 0-of-288, 4-of-4, 4+1 labels. Zero
mismatches. ECC-LP-INFEASIBLE-AT-THE-COMMITTED-ROW claims exactly the four
measured class-rows and no more; the CEILING tokens carry their checked
basis in the head itself.
2. **W3: PASS with E-8/E-9.** Instrumented as a GATE (G-W3-LABELS, ledger
row 41; MUT-W3 dies there — re-verified on the mirror), not prose; the one
family-level label is data-conditional and qualified
ACROSS-THE-TARGET-FAMILY with fibres disclosed (varied: 39 targets × 4
classes — amplitude, record, coin order, class; NOT varied: the arena
fibres); the other four headlines are labelled member-specific in §11 and
the receipt.
3. **The seam reading: PASS with E-6.** DECLARED-NOT-MEASURED stands in the
head (37), §3 (349–352) and the receipt (`seam.chosen_reading_status`); all
215 downstream rows are enumerated from the live row tables and gated for
totality (G-STAMPS; MUT-STAMP dies at 214 — verified); no sentence treats
the reading as a result, and §14 forbids inheriting the verdict as a
decision between readings. Seam-before-Born holds in the ledger
(G-SEAM-DECISION row 19 < first emission functional at G-MAPS-TYPED row 23
< G-BORN row 25; G-STEP-ORDER row 26) and in `full_run`'s call order.
4. **PSI-STATUS: PASS with E-7.** The quantifier is honest at the payload
level (ROWS=18 names the byte-equality basis; the reach-audit leg is named
AUDITED beside it); there ARE delivered LP rows outside the 18 (34 round
fields never face-compared) and their independence rests on the reach
audit, which the paper says; no sentence claims the trilemma resolved.
5. **The §13 deviations (my charge says four; the file carries five):
PASS.** Each is disclosed at point of use or stamped in the verdict segment
(one-arena in SCOPE and the seg-5 SCOPE token; the round-generated window
named where used in §6; the persist predicates declared in §3 leg two; the
six FEASIBLE-AT-THE-FIBER-ROW rows carry the disclosure in their own word;
the debt scope stamped in seg-5). None silently load-bearing.
6. **Pre-registration integrity: PASS with E-1/E-13.** Normalization sealed
at G-NORMALIZATION (ledger row 31) before every feasibility row
(G-LP-COMMITTED row 32; the order enforced inside G-LP-CENSUS;
`measure_lp` called after the gate in `full_run`); the pin's N-PIN-NORM
parsed, not re-typed; declared-but-never-consumed = none (49/49,
G-DECLARED-CONSUMED); 32/32 anchors consumed; read set
stray/external/never-read all empty.
7. **The walls: PASS with E-3/E-4/E-5.** Nine walls, licence legs on all,
no bare-negation/hedge licence tokens (the constructor refuses them,
ecc_exact.py:793–797); 54 independent controls die in the committed run and
my in-pattern controls die in mirror runs. Fresh-paraphrase survivorship as
tabled.
8. **Load-bearing prose licensure: PASS with the E-10/E-12 list.**
Everything else in §1–§12 that bears load traces to a named gate or receipt
path; the §3 substrate rebuild is correctly reported as a gated
reproduction (W1), and the quoted parent sentences are QUOTED anchors the
run locates on both sides.
9. **Outcome-vocabulary construction: audited — E-13.**

Also verified on the mirror: MUT-W3, MUT-STAMP, MUT-CEILING, MUT-PREREG,
MUT-SEAMWORD, MUT-WALL each die at their declared gates; full `--selftest`:
recipes 73, deaths at the declared gate 73, moves proved 73, artifacts
unchanged True, exit 0.

## Seat summary

ECC's five-segment head is numerically exact against its receipt to the
last token this seat could re-derive, its order-critical disciplines (seam
before Born, normalization sealed before any feasibility row, stems located
in the frozen pin) hold in ledger and call order alike, and its verdict
words claim their measured scopes — the committed row, the committed
observable menu, the declared reading, the target family — with the one
family-level statement earned by an arithmetic that is genuinely a theorem
and checked exceptionlessly at all 156 rows. Against that, the licensure
debits are real but reparable in wording and labels: §11 claims an
outcome-emitability the instrument's own gates refute (MAJOR — the
not-reached arms are refusal-shaped, not emittable), §12 claims a
no-summary-scalar comparator while nine head positions read stored scalars,
several of which have no receipt primitive to re-derive from (MAJOR); the
receipt stamps 197 rows with a byte-equality label whose honest mechanism
is the reach audit; a handful of prose universals (menu completeness,
"carried by no fibre", "labels are computed, never typed", the §5
counterfactual) outrun their gates; and the fifth segment's verdict word
hangs on a one-verb pin stem. My plants confirm the registered
fresh-paraphrase condition at full strength — all eight fresh restatements
of the five forbidden claims survive, including the paper's central no-go
inverted in plain words — and add two NEW bypass species to register: the
NEG guard excuses asserted violations behind an incidental "No…", and a
single stapled licence token launders an in-pattern derivation claim.
ACCEPT-WITH-FIXES: every fix is a sentence, a label, or a contained
comparator/receipt upgrade; no measured number moves.

*K2 / EFFECTUS — frozen. Scratch (mirror, plants, results) at
`scratchpad/ecc_k2/`; the repo received only this file.*
