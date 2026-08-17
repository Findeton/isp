# SCOUT-PAIR — SINGLE HOSTILE VERIFIER SEAT (FROZEN)

**Seat:** v15 ledger #89 battery + one verifier seat, per the pin class.
**Object under review (committed #88, digests re-verified by this seat
before any read):** v15/note-scoutpair.md `0fdebdfb99a8`;
v15/code/scoutpair_exact.py `2004930898ed`;
v15/code/scoutpair_output.txt `ecbf670f5899`;
v15/code/scoutpair_receipt.json `265389e7f820`; bound snapshots
`c86ea5edcfec` / `573cb2c55e5c` / `7c3655632bc4`.  Charter: pin
`67e6082b445a` + the #85 in-LOG addendum + `b3aa0f973ae1` (#86) +
`1d17712118b3` (#87), all digest-verified.  This seat modified no unit
file; its only repo write is this review.  All rebuild code and the
injection mirror live outside the repo (session scratchpad,
`scoutpair_verify/`, git-less, mirror path contains a space).

## VERDICT: ACCEPT-WITH-FIXES

All four verdict lines reproduce exactly from an independent rebuild.
Zero numerical discrepancies in ~4,900 independent recomputations.
Both artifacts regenerate byte-identically in a git-less alien-CWD
mirror at four PYTHONHASHSEED values with the six declared-not-read
legs physically absent — proving they are never opened.  The four-
addenda compliance audit is clean.  One instrument-strength gap is the
ordered fix (F1); everything else is minor or a registered condition.

## 1. OPERATOR — recomputation ledger (own code, own ring arithmetic)

Rebuilt from scratch: the Z[w] ring (my own multiplication, verified
w^3=1, 1+w+w^2=0, |1-w|^2=3), the arena, the committed walk (coin
order G.D confirmed against the pinned parent snapshot
`edb60bccd22e`), the B_c transport components, all windows.  Checks:
48/48 pass; recomputation count 4,846 in the operator script alone.

S1 (a): 27 cells rebuilt as unordered 2-actor pairs with the
pair<->cell map verified a bijection (the unit never states
bijectivity; it holds); every cell exactly 2 actors; every actor in
exactly 6 cells; 84 triples; 27 triangles; footprint census
{0:3, 2:54, 3:27} — every triangle writes exactly 3 pair atoms.
a = a(a-1)/2 has the unique solution a=3 on 2..9.  Sweep: my own
regex recount reproduces the total 234 and every per-file count;
the 13 non-dial classified lines are exactly the set of non-dial
occurrence lines (set equality, no unclassified remainder); class
counts 222/9/2/1 reproduce; the dial-file breaker scan is empty under
my own scan.  Eyeballed sites confirm the semantics: scout-bridge 128
and 409 are footprint-sense ("arity" scored by cells written), 416 is
the correct-split sentence (emitted co-division pair vs declared
arity); the paper-19/33 carrier sites and paper-39 event-size sites
read as classified.

S2: record-write flatness — the arena-general argument verified (the
count-field record space is the free commutative monoid N^C for ANY
cell set; writes are +e_c; addition commutes — nothing arena-specific
enters), machine-checked 729/729.  Transport census: classes
{fwd 81, rev 81, shared-nil 108, disjoint-nil 432}; nonzero ordered
defects 162 (81 unordered); defect Frobenius^2 values exactly 1/9
(54 straight) and 4/9 (108 turning); third-actor 162/162, disjoint
nonzero 0.  Six hand-checked instances with explicit defect matrices
(e.g. cells (0,9), straight, D entries (1,-2,-2)·w^0 at the shifted
row, |D|^2 = 9/81 = 1/9; shared-source pairs (0,1),(0,2),(1,2)
correctly land both-nil).  Decomposition licence re-verified at 5
probe (state, record) pairs of my own choosing, including ones the
unit never used.  Phase probe: all 1620 magnitude checks (not just
100) — invariant; matrix moved at exactly 450.  Full-step reading:
computed DIRECTLY as the operator difference
step(step(psi1,e1),e12) − step(step(psi1,e2),e12) for all 702
ordered pairs — never via the unit's closed formula — census
0:552, 1/3:48, 4/3:96, 5/3:4, 8/3:2 reproduced AND the unit's
formula d^2 = 3(q'(c1)+q'(c2)) verified as an identity at all 702;
90 disjoint-actor ordered pairs non-commuting.  Both controls
reproduce (0 and 702).

S3: 486 positive histories, unit mass; W3 supports disjoint (so 0
ambiguous two-write cuts — the cut census at W3 is support-carried
exactly as scoped); witness law verified at all 486.  W4: 477
reachable cuts, 9 ambiguous (all exactly 2 orders), 9/9 violate;
every one of the 9 two-row certificates verified ENTRYWISE against my
own q4map (orders, order probabilities, gap cell, row values, max
gap); first gap 224/729 at cut {0,12,13} orders (0,12,13)/(0,13,12).
Mechanism confirmed structurally: every ambiguous cut is {a,x,y},
a in sup1, x,y in {12,13,14} — two same-site writes at the returned
site (1,1).  Vacuous null reproduces with unit mass.  Controls: 0
synthetic violations, planted agreement lowers 9 to 8.  Clocked
expansion: 7 first events rebuilt; all 6 orders per event walked
through my own stepper; refusal at 7/7 via my own exact simplex-
membership solver; gap census {16/81: 5 events, 592/2187: 2}; the
receipt's per-event rows (distinct profiles 1/1/2/2/1/1/2, gaps)
match.  Unclocked: verified NON-tautologically — the 6 permutation
records collapse to one count field at every event (see F2).
Tomography: 378 = C(28,2), 3654 = C(29,3), 27 reached of 378, 3177
unreached of 3654 — all recomputed.  Grains: psi separates all 9
collision classes (states recomputed and compared).

S4: premise gate — the 9 collision classes' count fields compared as
serialized BYTES, 9/9 equal; geometry the one fixed chart by
construction; the paper-41 anchored seed verified at source
(`RECORD-COLLISIONS=39-CLASSES-180-HISTORIES`, and the verbatim
anchor "The record therefore cannot be injective on histories, and
is not" present at `c5fbc9acbd76`).  9/9 classes insufficient with
differing next-write distributions; first witness gap 224/729;
through W3 no two distinct positive histories share a count field
(0 collisions, support-carried).  The S3/S4 join (same nine cuts) is
exact: the ambiguity classes and the collision classes are the same
object in both censuses.

## 2. EFFECTUS — compliance audit

Four-addenda compliance: PASS on every point.  The #87 outcome words
are used exactly (SPAIR-ORDER-DEFECT-NONZERO always accompanied by
GEOMETRIC-INTERPRETATION-UNTESTED-FIXED-G; the positive S4 word is
NO-INSUFFICIENCY-WITNESS-THROUGH-W3 and the note never says
"SUFFICIENT" positively — every bare "sufficient" occurrence in the
note is inside a negation, a definition, or the wall; the S3 verdict
carries the three-way split including
SPAIR-INTERVENTION-SEMANTICS-UNBUILT; every refusal and feasibility
is two-sided-scoped and names its grain).  The at-receipt disclosures
(§2 items 1–5) are present and coherent.  The frozen source table is
bound exactly: all 17 pinned digests re-verified by this seat; the
three bound snapshots verify at the committed digests and DIFFER from
their live worktree successors (paper-50 live `3e01a1ce1b39`,
scoutk note `cc4d31ce7740`, scoutpsi note `5c46b34a4de9`) — the
mid-repair versions were NOT adopted; the six declared-not-read legs
all differ from their live copies too, consistent with the
disclosure, and the mirror run proves their bytes are never opened.
Tomographic deficiency published with the exact counts.  The
interpretation wall is present with history / trigger memory /
ontic psi / n-body beable named and none chosen.  The status-table
framing is the #86 form; "already instantiates" is absent; the
KINEMATIC-SHAPE sentence is carried verbatim.

Numeral totality, measured: 62 distinct integer numerals in the note;
every one is either receipt-backed or on the layout allowlist; zero
unbacked.  Layout-only occurrences are paper numbers, ledger entry
numbers, source line numbers, the seed 424242, and exactly one
substantive count — "30 gates" — which this seat verified true
against the receipt (30 ledger rows; 27 falsifiers also true).  The
registry is 29 rows in the note's §9 and 29 entries in
NUMERAL_FIELD_MAP, mutually consistent, every binding recomputed by
the operator rebuild.  (The verifier charge said "31-row"; the
delivered object is 29-row on both sides — a charge-text slip, not a
unit defect.)  All note slash-rationals are in the receipt inventory.

Paraphrase probes (10, of which 8 fresh): dead controls all caught.
Survivors: curvature-as-measured with a fresh verb and a determiner
shift; pair-beables-refuted; higher-arity-concluded in fresh words;
sequencing-refuted-generally; ontology-decided with a fresh subject;
psi-promotion in fresh words — 7 fresh survivors, all the REGISTERED
#46/#61 fresh-paraphrase condition (syntactic subject/predicate
walls do not catch semantics).  The fresh kernel-nonexistence
paraphrase was CAUGHT (the ported NEG-guard works).  Zero NEW wall
species.  The note itself contains none of the forbidden claims
under my own scans.

## 3. INSTRUMENT — injection table (git-less mirror, path with a space)

Baseline: delivery regenerates BOTH artifacts byte-identically to the
committed digests at PYTHONHASHSEED 0/1/424242 and after artifact
deletion at seed 7; the six declared-not-read files and LOG.md are
absent from the mirror and the run is green — they are never read.
--selftest: 27/27 falsifiers die at their declared gates with move
proofs, artifacts untouched, rc 0.

| # | injection | expected | observed | tree |
|---|---|---|---|---|
| I3 | one byte appended to bound snapshot paper50 | die at its digest gate | rc 3, G-PIN-DIGESTS | intact |
| I4 | forge a defect value (census denominator 81→80 in code) | die at S2 census | rc 3, G-S2-TRANSPORT | intact |
| I5 | flip NONZERO→ZERO in the note's S2 verdict | verification refuses | rc 3, kit sentence missing (--verify-paper) | intact |
| I6 | forge premise-gate equality (perturb one class field) | die at premise gate | rc 3, G-S4-PREMISE | intact |
| I7 | plant "the curvature is measured…" in note | wall flags | rc 3, curvature-scope wall | intact |
| I8 | plant fresh paraphrase "measures the arena's own curvature directly" | survivor (registered) | rc 0, SURVIVED — registered species | intact |
| I8b | plant "the ontology is settled: pair relations are all that exists" | survivor (registered) | rc 0, SURVIVED — registered species | intact |
| I9 | serialize live LOG.md digest into the receipt | die at G-ENV-EXCLUSION per the note's licence sentence | **rc 0, SURVIVED — finding F1** | intact |
| I10 | bare set-iteration function injected live | die at determinism gate | rc 3, G-AST-DETERMINISM | intact |
| I15 | corrupt load-bearing numeral in note (477→478) | verification refuses | rc 3, numeral not receipt-backed | intact |
| I11 | --mutant MUT-THIRD | die at declared gate | rc 3, G-S2-THIRD-ACTOR | intact |
| I12 | --mutant MUT-W4 | die at declared gate | rc 3, G-S3-W4 | intact |
| I13 | --mutant MUT-PREMISE | die at declared gate | rc 3, G-S4-PREMISE | intact |
| I14 | 5 hostile argv (unknown flag; bare --mutant; bare --verify-paper; positional junk; --kit extra) | rc 2 each | rc 2, 2, 2, 2, 2 | intact |

13 live injections beyond baseline/selftest; every intentional edit
restored and the mirror tree digest re-verified after each.

## 4. Findings

**F1 — MEDIUM (the ordered fix).  G-ENV-EXCLUSION is a canary, not
the property.**  The note's §2 disclosure says "no unpinned file's
digest enters the receipt [LIC:G-ENV-EXCLUSION]", but the gate only
scans for the scout-bridge canary digest.  Injection I9 (a live
LOG.md digest serialized into the receipt payload) passes all 30
gates and delivers rc 0.  The claim itself is TRUE of the delivered
artifact — this seat inventoried every 12-hex token in the committed
receipt (26 tokens) and all lie inside the pinned + declared + self
(object/source/determinism) set — but the licence citation implies
enforcement the gate does not provide.  Fix (either suffices): extend
the gate to a receipt-wide hex-12 inventory scan against
PINNED ∪ DECLARED_NOT_READ ∪ self-digests, or reword the disclosure
to say the gate runs a canary and the full property is
seat-verified.  No number moves.

**F2 — MINOR.  The `unclocked_matches` receipt field is tautological.**
s3_clocked computes `target = born(psi1, nfield(B))` and then
`unclocked_ok = born(psi1, nfield(B)) == target` — the same
expression compared to itself.  The substantive unclocked claim (all
6 write orders yield one record, hence one profile, the committed
one) is genuinely carried by record-write flatness (G-S2-REC-FLAT)
and was verified non-tautologically by this seat over the actual 6
permutations at all 7 events.  The claim is true; the field is
decorative.  Optional fix: compute the 6 unclocked records
explicitly.

**F3 — NOTE, REGISTERED.  Fresh paraphrases pass the walls.**  7 of 8
fresh paraphrases of the forbidden claims survive (I8/I8b plus the
in-memory probes PP1–PP7).  All are the registered #46/#61
syntactic-wall condition; the kernel wall's NEG-guard caught the
fresh kernel paraphrase; zero NEW species.  The note itself is clean.

**F4 — COSMETIC.**  The S1 kit sentence ("The record's own arity of 2
is never called an arity anywhere in the swept corpus…") appears
twice consecutively in note §3 (lines 158–162) — a paste artifact;
the kit check requires presence, so the duplicate is inert.

**F5 — NOTE (for the ledger).**  The seat's charge said "the 31-row
binding"; the delivered registry is 29 rows, consistent between note
§9 and the instrument.  Also for the record: the layout allowlist
whitelists 0–61 wholesale, so small substantive numerals ride it in
principle; measured, the only substantive rider in this note is
"30 gates", verified true.

**Positive findings worth engraving:** the full-step defect formula
d^2 = 3(q'(c1)+q'(c2)) was re-derived by this seat as a direct
operator computation and holds as an identity at all 702 pairs — the
unit's closed form is not an unverified shortcut; the pair<->cell map
is a genuine bijection (27 against 27), strengthening S1's atom
census; and the S3/S4 "one measurement, two predicates" join is
exact — the ambiguity classes and the collision classes coincide as
sets.

## 5. Summary

The delivered SCOUT-PAIR unit survives a full hostile rebuild: every
load-bearing number in all four verdict lines — 27/27 atoms, the
a=3 fixed point, sweep 234 = 222+9+2+1, record flatness 729/729,
transport 162/81 with values 1/9 and 4/9 and the 162/162 third-actor
law, phase-only record motion 1620/450, full-step census
552/48/96/4/2 with 90 disjoint non-commuting (re-derived by direct
operator composition), W3 486/0-ambiguous, W4 477/9/9 with all nine
certificates entrywise-exact and first gap 224/729, clocked refusal
7/7 with gaps 16/81 and 592/2187, tomography 27/378 and 477/3654,
psi-separation 9/9, premise gate 9/9 byte-equal, insufficiency 9/9 —
reproduced independently with zero discrepancies (~4,900
recomputations); the artifacts regenerate byte-identically under
alien conditions with the declared-not-read sources deleted; the
falsifier registry, walls, argv discipline and write-nothing selftest
all behave as declared; the four-addenda vocabulary, scoping, and
disclosure obligations are met exactly; the single instrument-
strength gap is that G-ENV-EXCLUSION enforces a canary rather than
the receipt-wide no-unpinned-digest property its licence sentence
suggests (the delivered receipt itself is clean — verified), which
with one tautological receipt field and one duplicated kit sentence
is the whole defect list — hence ACCEPT-WITH-FIXES, the F1 repair
ordered, F2/F4 optional, and the four CANDIDATE READINGS otherwise
confirmed at their delivered scope.
