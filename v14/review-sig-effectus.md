# SIG (paper-24) — K2 EFFECTUS-LENS REVIEW

**Seat:** K2 (EFFECTUS — licensure, head grammar, register, walls, choice
inventory, prose↔receipt). **Protocol:** v14 ledger #266 (row K2).
**Object at `025c4a6`:** `v14/paper-24-sig.md` `72175d6fa85b`,
`v14/code/sig_exact.py` `a41b6d549e14`, `v14/code/sig_output.txt`
`f28b550c151e`, `v14/code/sig_receipt.json` `ca9cd4ceb387`; pin
`v14/note-sig-pin.md` `ab73239daff5`.

**All five hashes verified at the start and at the end of this review, byte
for byte.** Context read at its own pinned sha: `v14/note-r4dec-adjudication.md`
`9927fef9514a` (the #211 adjudication). No sibling's uncommitted state was
opened — `v14/paper-29-perr.md`, `v14/code/perr_*`, `v14/code/sec_exact.py`,
`v14/note-paper23-correction.md` and the `smu` working-tree modifications are
untracked or modified and were **NOT** read.

---

## GRADE

**ACCEPT-WITH-FIXES (AWF).**

**78 delivered or inherited quantities independently re-derived from nothing;
0 numerical disagreements.** Two rebuilds share no code with the unit and
were written from the declared grammar alone — a static one over the round
grammar, and a **clean-room re-implementation of paper-20's coupled quantum
walk**, the latter anchored on six of the parent's own committed rows before
any SIG number was read from it. Enumerations total 280 partitions, 2,197
codes, 16,108,764 five-round multisets, 16,699,200 R = 4 quadruple probes and
~300,000 emission branches in exact `Z[ω]`. **Not one delivered number
moved — including the two masses the entire polarity verdict rests on, which
were recomputed twice by routes sharing no expression.**

Every finding below is a **licensure** finding: a sentence whose measured
content is narrower, or differently shaped, or actually the opposite of, the
sentence printed over it. **Five are MAJOR** — two of them strike the verdict
fences (the outcome word; the floor clause of segment 1), one strikes the
sentence the unit itself calls "this unit's most transportable result", one
strikes the scope of the forcedness claim, one strikes the mod-3
instrument's evidence (not its conclusion). Seven are MINOR.

**No verdict number is overturned. The unit's measurements are excellent and
its reachability census is, in this seat's judgement, the strongest static
result the R-arena line has produced.** What must move is what the unit says
about them — and in **three** of the five MAJORs the corrected sentence is
*stronger* than the delivered one.

**Five recomputations are measurements the unit did not take and this review
supplies** (marked ★): the exhaustive R = 5 *covered-site* code census
(181 / 6 / 3), the independent confirmation of paper-21's max-cell-2 row at
R = 4 by direct search, the two-currency ledger that prices the
walk-versus-grammar comparison, the Born path measure's invariance across the
whole homogeneous locus, and the A4-singular / A5-indefinite coincidence that
exhibits representative-relativity more sharply than anything in the unit.

---

## 1. THE RECOMPUTATION LEDGER (78 / 78 agree)

Rebuilt in `python3.13`, exact integers and `Fraction` only, importing
nothing from the unit and executing nothing of it. Scripts:
`/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/sig-ef/static_rebuild.py`,
`.../sig-ef/r5_census.py`, and the clean-room walk engine
`.../sig-ef/walk/walk_clean.py` with `.../walk/anchor.py`,
`.../walk/sig_check.py`, `.../walk/recompute.py`, `.../walk/extra_probe.py`.

| # | quantity | recomputed | delivered |
|---|---|---|---|
| 1–5 | the five object sha256-12 | 72175d6fa85b / a41b6d549e14 / f28b550c151e / ca9cd4ceb387 / ab73239daff5 | same |
| 6 | the #211 adjudication's sha256-12 | 9927fef9514a | same (prompt) |
| 7 | partitions of nine sites into three triples | 280 | 280 |
| 8 | **deposit theorem — max incidences per cell per round** | **1** | 1 |
| 9 | max incidences per site per round | 2 | 2 |
| 10–14 | the incidence spectrum | 0:1, 4:27, 6:54, 7:162, 9:36 | identical |
| 15 | two-route determinant agreement over the declared box | 2197 codes, 0 disagreements | 2197, 0 |
| 16–17 | cheapest covered SINGULAR code / its 4 det q | (1,1,4) / 0 | (1,1,4) / 0 |
| 18–19 | cheapest covered INDEFINITE code / its 4 det q | (1,1,5) / −5 | (1,1,5) / −5 |
| 20–21 | one ROW round: site code at all nine sites / 4 det q | (1,0,0) at 9 of 9 / −1 | identical |
| 22 | linear maps of AG(2,3) preserving the declared link set | 12 | 12 |
| 23 | orbit of the 27 cells under those × the nine translations | **27 of 27, one orbit** | 27 of 27 |
| 24–25 | saturating (foreign-pair-free) partitions / their incidence totals | 36 / all 9 | 36 / — |
| 26 | partitions depositing on a fixed cell (the pool) | 70 | 70 |
| 27 | multisets of five such rounds, C(74,5) | 16,108,764 | 16,108,764 |
| 28 | **minimum uncovered cells over all of them** (exhaustive b&b) | **2** | 2 |
| 29 | second route: max cells covered by five pool-rounds | 25 of 27 | — (implies 2) |
| 30 | **multisets of five rounds inducing (1,1,5) at the target site** | **2,210,000** | 2,210,000 |
| 31–32 | the exhibited R = 5 witness: zero cells / site code / 4 det q | 13 / (5,1,1) / −5 | 13 / (1,1,5) / −5 |
| 33 ★ | R = 5 reachable site-code set | **181** | — (the #211 origin's) |
| 34 ★ | of those, covered but not posdef | **6** | — (the origin's) |
| 35–36 ★ | of those, det < 0 / which | **3 / (1,1,5) and its two relabellings** | — (the origin's) |
| 37–39 ★ | R = 4: reachable codes / covered-not-posdef / covered det<0 | **105 / 3 / 0** | — (paper-21's) |
| 40 ★ | R = 4 covering record with any cell ≥ 3 (16,699,200 probes) | **none — max cell count is 2** | — (paper-21's row, quoted by SIG) |
| 41–42 | Born polarity ratio, exact / decimal | 675143691622400/6409469116243161 / 0.10534 | identical / "roughly a tenth" |
| 43–44 | record polarity ratio, exact / decimal | 81157120/28166373 / 2.88135 | identical / "nearly three" |
| 45–46 | stage-frozen exceeds coupled, both readings | TRUE / TRUE | "both are larger" |
| 47 | the three Born denominators are pure powers of three | 3²⁵, 3¹⁹, 3¹⁷ | — |
| 48 | A7-to-A4 indefinite-mass factor | 5778.7 | "1" vs 146623744/847288609443 |
| 49 | the collinear rungs, their R, their 4 det q and their region | 7 of 7 identical (A3 3, A4 4, A5 3, A6 0, A7 −5, A8 −12, (2,2,2) 12) | identical |
| 50 | the ladder law R = n₁+n₂+n₃ on the rungs | holds 7 of 7 | holds |
| 51 | receipt leaf keys / `stage_frozen` keys present | 2460 / **exactly 2** | — (see MINOR-2) |
| 52 | receipt `/counts/coins` vs paper-20's `F4` fiber | **5 vs 6** | "a fiber of six … all of them run here" |
| 53 ★ | delivered `BLOCKED-AT` referents censused across v14's papers | **10 of 10 name a missing, empty or zero-admitting object** | — |
| | **— the clean-room walk rebuild (below) —** | | |
| 54–55 | branch counts per level, A3, Born / record menu | 3,27,486,10527,284078 / 3,27,486,11664,314928 | identical |
| 56–57 | exit probability at A3, Born / record menu | 927415552/847288609443 / 37440224/5811307335 | identical |
| 58 | the exit census, code by code | 1,1,4:466 / 1,4,1:471 / 4,1,1:379 | identical |
| 59–60 | max-cell ladder / support schedule | 2,2,3,3,4 / 1,3,6,8,9 | identical |
| 61–62 | inadmissible leaves with exactly one site out / exit mass below step 5 | 1316, all / exactly 0 | identical |
| 63 | paper-20's frozen control branch counts | 3,27,486,9234,212382 and 314928 | identical |
| 64 | **A4 Born-menu indefinite mass** | **146623744/847288609443** | same |
| 65 | **A4 record-menu indefinite mass** | **5072320/1162261467** | same |
| 66–67 | the null (uniform-on-support) masses, Born tree / record tree | 148895641/90632341800 / 53/34992 | identical |
| 68–69 | first indefinite step, A4 / A5 | 5 / 3 | 5 / 3 |
| 70–71 | the stage-frozen arm, both readings | 34816/129140163 / 325184/71744535 | identical |
| 72–73 | paper-20's frozen control / A4 first singular step | 0 / t = 3 | 0 / 3 |
| 74 | A7 indefinite mass | 1 | 1 |
| 75 | the mod-3 instrument, two-way | A4 ≡ A7 path-identical under Born, different under record | identical |
| 76 ★ | **the Born path measure across the homogeneous locus** | **byte-identical for every homogeneous start tested, differences of 1 included** | — (see MAJOR-5) |
| 77–78 ★ | A4's Born **singular** mass vs A5's Born **indefinite** mass, t = 3 / t = 4 | **64/59049 = 64/59049** and **15949136/1162261467 = 15949136/1162261467** | — |

Rows 54–78 come from a **clean-room re-implementation of paper-20's coupled
machine**, written from the parent's declaration, importing nothing and
executing nothing of the unit. It anchors on six of paper-20's own committed
rows including the frozen control — which proves the phase machinery is live,
since coupled 284,078 leaves against frozen 212,382 is a difference the
back-reaction alone produces. Exact `Z[ω]` integer pairs and `Fraction`
throughout, no floats; 11,044 + 12,181 per-node stochasticity checks, 0
violations. **Rows 64 and 65 — the two masses the whole polarity verdict
rests on — were recomputed a second time by a route sharing no expression
with the first** (record rebuilt from the path multiset, region decided by
the Fraction readout instead of the integer Heron form, weights summed
leaf-by-leaf instead of denominator-bucketed). Identical.

**Every dynamic number in this unit is confirmed.** The polarity's sign flip
across the emission reading — the fact MAJOR-1 is about — is real, exact, and
independently reproduced at this seat.

Row 40 deserves a sentence. SIG quotes paper-21's "Across the whole covering
class the maximum cell count is 2" and reasons from it. This seat did not
take it on trust: a direct search over every covering quadruple containing
three rounds on one cell (16,699,200 probes, licensed to one cell by row 23)
finds none. **Paper-21's row is confirmed, independently, at this seat.**

---

## 2. MAJOR-1 — THE HEAD'S GRAMMAR: `BLOCKED` IS NOT THE LICENSED WORD, AND THE OBJECT REFUTES IT ON ITS OWN FACE

**Ruling: `SIG-BLOCKED-AT-THE-EMISSION-READING` is not licensed. The honest
head is READING-STRATIFIED with both polarities first-class — and the
corpus's own pre-registered word for it already exists.**

Four independent grounds, in increasing order of force.

### 2.1 The head refutes itself between segment 3 and segment 4

The pin's outcome grammar is an exclusive list —
`SIG-SELECTED` / `SIG-AVOIDED` / `SIG-NEUTRAL` /
`SIG-BLOCKED-AT-REACHABILITY` / `SIG-BLOCKED-AT-<object>` — closing with
"every polarity word conditional on Stage 0's license." **Stage 0 granted
the license.** The polarity words therefore became emittable, and the unit
emitted them: segment 3 reads `SIG-POLARITY-[BORN MENU AVOIDED … RECORD MENU
SELECTED …]`, with exact masses, coin-invariant and arena-invariant.

Segment 4 then announces that the unit was blocked from emitting a polarity
word. **It is printed one fence below two polarity words.** §7.3's
justification — "There is therefore no single polarity word to emit" — is a
statement about *cardinality*, not about a block: the unit emitted two. A
head cannot claim a block against an act it performs on the same page.

### 2.2 `BLOCKED-AT`'s referent class in this corpus is measured, and this object is not in it

Censused across v14's delivered papers (row 53), every `BLOCKED-AT` names an
object that is **not there**:

| head | the named object | why blocked |
|---|---|---|
| `BLOCKED-AT-GRAMMAR-SOURCE` (paper-04) | an incidence fact | the pinned sources do not supply it |
| `BLOCKED-AT-DIAGONAL-INTERVAL-INCIDENCE` (paper-04, -07) | which site subdivides | 2 candidates, 0 decided |
| `CRA-BLOCKED-AT-STATIC-GEOMETRY<MISSING=…>` (paper-05, -12) | a geometry update law | `MISSING=` in the head |
| `CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW` (paper-06, -09) | a stochastic law | none pinned |
| `BLOCKED-AT-REFERENT` (paper-12) | a declared map | **0** measured over 24 sources |
| `GPREP-ARM-B-BLOCKED-AT-THE-MONOTONE-HOLDINGS-LADDER` (paper-11) | a descent | **0 of 243,768** transitions |
| `BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL` (paper-14) | the control | **empty** |
| `R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8` (paper-15) | the eigenphase | outside the arena |
| `R5-BLOCKED-AT-THE-GATE` (paper-10, -18) | an admitting gate | **0 of 52** admitted |

Ten referents, ten absences. **`THE-EMISSION-READING` is the exact opposite
of every one of them.** It is declared by the parent
(`F10-EMISSION-READING`, DECLARED, fiber 2), it is *present*, it is
*exhausted* — both members run at every arena and at all five coins — and it
is *measured to decide the sign*. A fiber that is present and fully traversed
is the strongest possible measurement outcome, and the corpus has never
called one a block.

### 2.3 The pin's own authority pre-registered the right word, and the pin dropped it

The pin cites as its authority "THE STRATEGIC PLAN (#193, Wave A)".
`v14/PLAN.md` line 188 pre-registers, for this very unit:

> SIGNATURE-SELECTED / SIGNATURE-AVOIDED /
> **SIGNATURE-DECLARATION-RELATIVE** / BLOCKED-AT.

**`DECLARATION-RELATIVE` is a first-class pre-registered outcome of paper-24,
and it names precisely what this unit found.** The pin's five-member list is
a compression of the plan's four-member one and the compression lost exactly
the member the measurement landed on. A pin may narrow a plan; it may not
narrow it *silently* and then force the finding into a slot that misdescribes
it. The plan's word is available, pre-registered, and unused.

### 2.4 The precedent is this seat's own, twice

**W2 (the joint adjudication of the effectus review at #97,
`note-w2-adjudication.md` §1.2):** "**The mechanism is
READING-STRATIFIED** (effectus MAJOR-1, decisive)… the head must carry the
stratification." The resulting terminal head is
`WELD2-EMPTY-AT-THE-DECLARED-FAMILY-READING-STRATIFIED-…`. Same seat, same
shape, same resolution: two admissible readings, both carried, head
stratified — **not** blocked.

**R4b (`note-r4b-adjudication.md` §1.1):** "every BOUND-segment quantity
either carries an invariance gate over the residual fiber **or is stamped
READING-RELATIVE** (effectus MAJOR-2's §15 violation closed)." That is the
declared-arena discipline's own disposal rule for a quantity that moves with
a declared fiber, and the two disposals it offers are *invariance gate* and
*READING-RELATIVE stamp*. Neither is a block.

### 2.5 The repair

Segment 4's word is replaced; **its content is kept verbatim and gains
nothing it did not measure.** Recommended, in the plan's own pre-registered
vocabulary:

```
SIG-DECLARATION-RELATIVE-AT-THE-EMISSION-READING-<POLARITY=BORN:AVOIDED(0.105 OF THE COUNTING MEASURE) / RECORD:SELECTED(2.88) -- BOTH FIRST-CLASS, BOTH EXACT, BOTH COIN-INVARIANT 5 OF 5 AND ARENA-INVARIANT 2 OF 2 | THE SIGN IS A FUNCTION OF THE EMISSION READING ALONE AND OF NOTHING ELSE MEASURED HERE | MOD-3 THEOREM=… | SCOPE=…>
```

`SIG-READING-STRATIFIED-…` is equally admissible and carries the W2
precedent; the adjudicator picks. **This is a strengthening, not a
concession.** A block says *we could not answer*. The stratified head says
*we answered, exhaustively, and the answer is a theorem about which face of
emission is read* — falsifiable, coin-invariant, arena-invariant, and
already fully measured in this object. §7.3's own sentence, "That is a
negative about the *question*, not about the measurement," is true and is
exactly why the outcome word should stop calling the measurement blocked.

**One clause must go with the word.** §7.3 says "paper-20 declared both
readings, ran both, and privileged neither" — true, and it is the *reason*
the outcome is declaration-relative, not the reason it is blocked. Keep the
sentence; change what it concludes.

---

## 3. MAJOR-2 — THE FLOOR "CORRECTION" IS A CLASS SUBSTITUTION; THE INHERITED CLAIM IS TRUE, AND ATTAINED, AT ITS OWN CLASS

**Ruling: the inherited `R = 5 statically` floor is NECESSARY *and
ATTAINED*. `NOT ATTAINED` is true only of a class the inherited claim never
named. The clause is false as printed and stands in verdict fence 1, in the
gate statement of `G-STATIC-FLOOR`, in the section title of §3.3 and in the
ledger at #262.**

### 3.1 What the inherited claim actually says

The claim's **origin** is this seat's own row at paper-21,
`v14/review-r4dec-effectus.md` §5 ("THE ROW SIG'S PIN MUST CARRY"), lines
431–457:

> A **covered site** can first carry det < 0 at **R = 5**, at (1,1,5) and its
> two relabellings (verified: the R = 5 reachable code set is 181, of which 6
> are covered-but-not-posdef and 3 have det < 0). … the floors are **R = 5
> for a covered site** statically, R = 8 for I7's own declared G-INDEF, and
> horizon ≥ 6 dynamically

**The class is named in the words: *a covered site*.** That is exactly SIG's
own "full site" class — "that site's three cells all occupied" (§3.2 table).

I verified the origin's numbers independently (ledger rows 33–36): at R = 5
the reachable site-code set is **181**, of which **90** are covered, **6** are
covered-but-not-posdef and **3** have det < 0 — and those 3 are **(1,1,5) and
its two relabellings**, to the code. The origin is exact.

### 3.2 SIG measures the inherited floor ATTAINED, and says so

SIG's §3.2 identifies the inherited floor correctly and at the right class:

> an indefinite site whose links are all occupied needs R >= 5. **That is the
> inherited floor**, and it is **necessary**.

SIG's §3.3 then measures it:

> **The full-site class is attained at R = 5: 2,210,000 multisets of five
> rounds induce the code (1, 1, 5) at the target site**

**2,210,000 — independently reproduced at this seat (ledger row 30), with the
witness's 13 zero cells and its 4 det q = −5 (rows 31–32).** The inherited
floor is necessary *and attained*, and SIG proves it.

What SIG measures **not** attained at R = 5 is the **covering** class — all
27 cells occupied — which first exists at R = 6 (min uncovered 2 over
16,108,764 multisets; reproduced, rows 27–29). **That class appears nowhere
in the inherited claim.** The origin's sentence quantifies over *one site*;
SIG's refutation quantifies over *the whole record*.

### 3.3 Where the false clause sits

| location | text | status |
|---|---|---|
| verdict fence 1 (§ head and §10) | `THE INHERITED #211 FLOOR R=5 IS NECESSARY AND NOT ATTAINED` | **FALSE as printed** |
| `G-STATIC-FLOOR` sealed gate statement | "That floor is NECESSARY; whether it is ATTAINED is the next gate's question **and the answer is no**" | **FALSE** — the next gate answers about covering records, and this gate's own subject is a covered site |
| §3.3 section title | "The inherited floor is not attained" | **FALSE as a title over a section whose own third paragraph says it is attained** |
| §1 | "one of them turns out to be necessary rather than attained" | **FALSE** |
| §10 readout | "The inherited R = 5 floor is necessary and unattained" | **FALSE** |
| `PL-STATIC-R5` pre-registered polarity, declared FALSE | the pre-registration itself encoded the substitution | see repair |

The `G-STATIC-FLOOR` row is the sharper one, because a gate's published
statement is part of the sealed surface — and the #211 repair order **S5**
was, in its own words, "**the coverage gate's sealed statement made true**".
The same order applies here.

### 3.4 The repair (exact)

Everywhere the clause occurs, the class is named and the *addition* replaces
the *correction*:

> `THE INHERITED #211 FLOOR R=5 IS NECESSARY AND ATTAINED AT ITS OWN CLASS
> (A COVERED SITE: 2,210,000 WITNESSES, 13 OF 27 CELLS EMPTY) AND THE CLASS
> LADDER IS NEW: COVERING FIRST AT R=6 (16,108,764 MULTISETS SCANNED, MINIMUM
> UNCOVERED 2), STRUCTURALLY LIVE AT R=7, I7'S G-INDEF AT R=8`

§3.3's title becomes "**What the inherited floor does not buy: covering**".
`G-STATIC-FLOOR`'s trailing clause becomes "…and the answer is yes at this
gate's own class; the covering class is the next gate's, and there the answer
is no." `PL-STATIC-R5` is re-declared at the covering class, where FALSE is
the correct pre-registration.

**Nothing is lost.** The four-class ladder is a genuinely new and excellent
result — the R = 1 unrestricted row in particular is, as §3.2 says, "the one
nobody had looked at". It simply is not a correction of anything inherited.

### 3.5 THE ROUTING — what needs annotating, and what may not be touched

Located exhaustively. The claim lives in **three** places and **not** in a
fourth:

1. **`/Users/felixrobles/workspace/isp/v14/review-r4dec-effectus.md`**, §5,
   lines 431–457 — **the origin.** Verified exact at this seat
   (181 / 6 / 3 / the three codes). **TRUE. Not to be edited.**
2. **`/Users/felixrobles/workspace/isp/v14/note-r4dec-adjudication.md`**
   (`9927fef9514a`), line 43 — "floors R=5 statically, R=8 for G-INDEF,
   horizon ≥ 6 dynamically". The adoption **compressed away the qualifier
   "for a covered site"**. Read as a floor — a necessary condition — it is
   **TRUE**; SIG confirms the necessity. It is *class-implicit*, not false.
   Note that the same sentence's "R=8 for G-INDEF" is a homogeneous
   structurally-live budget, so the sentence already carries two floors at two
   different classes. That is looseness, not falsehood. **Not to be edited**
   — nothing that is not false may be edited.
3. **`/Users/felixrobles/workspace/isp/v14/note-sig-pin.md`** — carries the
   same compressed sentence. **FROZEN. Not to be edited, under any finding.**
4. **`/Users/felixrobles/workspace/isp/v14/paper-21-r4dec.md`** — **the claim
   is absent.** A grep for `R = 5` / `R=5` over all 1,047 lines returns
   nothing; the paper takes no R = 5 position at all. **Paper-21 owes
   nothing, and this review recommends it be left entirely alone.** This
   matters: the delivered head attributes the floor to "#211", which is the
   adjudication, not the paper — SIG is right about that and should keep
   being right about it.

Also carrying it: `v14/LOG.md` at #262 (line 8075), which repeats "the
inherited #211 floor CORRECTED: 'R=5 statically' is NECESSARY AND NOT
ATTAINED". **The ledger is the adjudicator's; this seat does not edit it and
routes the row.**

**The instrument.** The corpus's precedent for exactly this shape is the pair
of standing notes `note-paper12-scope-annotation.md` and
`note-r4-scope-annotation.md`, both titled "**SCOPE ANNOTATION, NOT AN
ERRATUM**", both written because "the claim was true of its own object" and
a different object gives a different answer, and both explicitly declining to
edit the terminal paper. **That is the correct shape here, and this seat
rules that the annotation is owed FORWARD, not BACKWARD**, for two reasons:
the two subjects (an adjudication note and a frozen pin) are already
immutable by convention and are already read at their pinned shas by SIG's
own provenance gate; and the live consumer of the class-implicit phrasing is
still ahead of us, not behind (see §3.6). The cheapest correct instrument is
therefore **one ruling row in the SIG adjudication**, not a new standing
note. If the adjudicator prefers the standing-note form, the two precedents
supply the exact title and shape.

### 3.6 The forward routing that actually matters

**`v14/note-perr-pin.md` (frozen at #233), row 4, carries the same
class-implicit phrasing:**

> **G-SINGULAR and G-INDEF static reachability at R=5 — THE SIG FEED (this
> row is SIG's Stage-0 input; compute it first and state it separately).**

"Static reachability at R=5" with no class named is exactly the ambiguity
that produced this MAJOR. PER-R is in flight. **The binding row PER-R must
carry is the CLASS LADDER, not a number:** unrestricted / covered-site /
covering / structurally-live, with the R = 5 answer being *yes* at the first
two and *no* at the last two. See §11.

---

## 4. MAJOR-3 — THE WALK-BEATS-GRAMMAR SENTENCE: THE COMPARISON HAS NO DECLARED CURRENCY, AND THE MECHANISM IS REFUTED BY THE UNIT'S OWN 70-POOL

**Ruling: the sentence is licensed only as a two-currency statement with the
currencies named; it is NOT licensed as a channel-superiority claim; and the
mechanism attached to it is false at SIG's own measurements. The corrected
mechanism is sharper and more transportable than the delivered one.**

The sentence, from §5, §10 and the ledger:

> **The walk reaches at R = 4 and horizon 5 a region the grammar cannot reach
> below R = 6.** … The back-reaction … **is a concentration channel the round
> structure does not possess.** … That gap is **this unit's most
> transportable result**.

### 4.1 The mechanism is false, twice, at the unit's own numbers

§5's mechanism reads:

> the grammar feeds a cell at most once per round, so it buys lopsidedness
> only by spending rounds; **the emission channel has no such constraint and
> can put every event it has on one cell.**

Both clauses fail against SIG's own measurements.

- **"the emission channel has no such constraint."** §4.2 states the
  constraint two pages earlier: "**The walk emits exactly one division event
  per step.**" One event per step is *the same cap* as one incidence per cell
  per round. The channels have identical per-unit concentration rates. There
  is no rate asymmetry to name.
- **"can put every event it has on one cell" (as a contrast).** The grammar
  can too. **The 70-pool is precisely the set of rounds that hit a fixed
  cell** (ledger row 26), and SIG's own R = 5 census enumerates the
  16,108,764 multisets drawn from it — every one of which puts all five of
  its rounds on the one cell. The grammar concentrates perfectly well.

### 4.2 What SIG actually measured, which is better

The R = 5 failure is **min uncovered 2** — a *covering* failure, not a
concentration failure. The true mechanism, and it is fully measured in this
object:

> **A round's deposit on the target cell is COUPLED, by the partition, to
> eight other deposits it does not choose; an emission's deposit is
> UNCOUPLED. The grammar therefore cannot concentrate and cover at once, and
> the walk never has to — it inherits the covering from the arena and
> disturbs nothing.**

That is a statement about an *obligation*, not a *rate*, it is exactly what
`min uncovered = 2` measures, and it transports to any round structure built
from partitions. It is strictly the better result.

### 4.3 The comparison has no declared currency — and under a uniform one the grammar wins at every class ★

The delivered comparison prices rounds and ignores steps. Priced uniformly —
one round, one step, one unit — the ledger inverts:

| class of record reached | grammar | the walk, at its **best** pair | winner |
|---|---|---|---|
| covered site, indefinite | **R = 5** = 5 units | A5: 5 rounds + 3 steps = **8** | **grammar** |
| covering, indefinite | **R = 6** = 6 units | A5: 5 + 3 = **8** | **grammar** |
| structurally live, covering, indefinite | **R = 7** = 7 units | A5: 5 + 3 = **8** | **grammar** |

The walk is priced at its *best* pair, not the delivered one: A5 costs 8
units against A4's 9 and A3's 9. Every leaf record in all three arms is
covering and foreign-pair-free — the collinear ladder is both at every rung
(verified here, 7 of 7 rungs) and emissions land only on declared cells — so
all three rows are like-for-like. **Even at the walk's best pair, and even
against the grammar's most expensive class, the grammar arrives first.**

There is no canonical exchange rate between a round and a step; that is the
point. **The unit already knows this**: §5 measures that the cheapest
clearing pair is order-relative, publishes the disagreement, and refuses to
resolve it by fiat. The channel comparison is the same kind of object and
must get the same treatment.

### 4.4 The repair

Stamp the currency, exactly as the cheapest-pair row is stamped:

> **Counted in rounds alone, the walk reaches at R = 4 what the grammar needs
> R = 6 for; counted in rounds-and-steps alike, the grammar reaches every
> class first. There is no declared exchange rate between a round and a step,
> and this unit does not supply one.** What is currency-free is the
> mechanism: a round's deposit is coupled by the partition to eight it does
> not choose, an emission's is coupled to nothing — so the grammar cannot
> concentrate and cover at once, and the walk is never asked to.

§10's "That gap is this unit's most transportable result" becomes "**That
mechanism** is this unit's most transportable result" — which is true, and
survives the currency question entirely. Successor row **S-3** inherits the
corrected form.

---

## 5. MAJOR-4 — THE CHOICE INVENTORY'S ITEM 3 ABSORBS FIVE INHERITED DECLARED FIBERS, ONE OF THEM THE PARENT'S OWN VERDICT-RELEVANT ONE; THE FORCEDNESS CLAIM'S SCOPE IS OVERSTATED

**Ruling: "what is forced at this arena is the coin-independence" is measured
over paper-20's `F4` only. The parent's `F6-COIN-ORDER`, stamped
DECLARED-**VERDICT-RELEVANT** and measured by the parent to move the exit
mass by a factor of 3.15, is neither run nor disclosed anywhere in this
unit.**

SIG's inventory item 3 reads:

> | 3 | the walk, the coin register and the connection | **forced** | 1 | paper-20's, rebuilt and anchored at five rows |

**Fiber 1, FORCED.** Against paper-20's own inventory, that single row
absorbs five *declared* items:

| paper-20 item | status there | fiber | run in SIG? | in SIG's inventory? |
|---|---|---|---|---|
| `F6-COIN-ORDER` (G·D vs D·G) | **DECLARED-VERDICT-RELEVANT** | 2 | **no** | **no** |
| `F7-ORIENT` (+l vs −l) | DECLARED | 2 | no | no |
| `F8-INIT-COIN` | DECLARED | 3 | no | no |
| `F9-INIT-SITE` | MEASURED | 3 | no | no |
| `F12-UPDATE-SEMANTICS` | DECLARED | 2 | no | deviation 7 only |

Product 72. The inconsistency is internal: SIG *unbundles* paper-20's `F4`
(as its own item 8, declared, fiber 5) while bundling these five under
"forced".

**`F6` is the one that bites.** Paper-20 measured, at the full horizon and
on its own sharpest observable:

> the alternative order D.G leaves the admissible class with probability
> 2922723584/847288609443, larger, at the same threshold

— 3.15× SIG's own inherited exit mass, on the very channel through which
SIG's region masses are reached. SIG's forcedness claim is a coin-family
census (`F4`, 5 members). It does not touch `F6`, and **`F6` is the fiber the
parent itself flagged as verdict-relevant.**

This does not damage a number. It damages a *scope word*: "what is forced at
this arena is the coin-independence" reads as coin-independence *simpliciter*
and is coin-*family* independence at the delivered coin *order*.

**Repair.** (a) Item 3 is split: the machine's *forced* half (site carrier,
link set, coin register, connection group — all four genuinely forced or
derived at the parent) stays FORCED; the five inherited declared fibers get a
row of their own, `INHERITED-DECLARED, fiber 2×2×3×3×2, one member each, not
re-opened here`, with `F6` named and its VERDICT-RELEVANT stamp carried.
(b) §7.1's and the head's "coin-invariant" becomes "**invariant across
paper-20's `F4` coin family (5 of 5) at the delivered coin order `G·D`;
`F6-COIN-ORDER`, the parent's own verdict-relevant fiber, is not re-run
here**". (c) A deviation row prices it. (d) A successor row registers it —
the cheapest possible strengthening of this unit is to run `D·G` at A4, which
is one horizon-5 arm.

---

## 5b. MAJOR-5 — THE MOD-3 INSTRUMENT IS CONFOUNDED ON ITS OWN CHOSEN PAIRS: THE MEASURED INVARIANCE IS HOMOGENEITY, AND IT IS STRONGER THAN MOD-3 ★

**Ruling: the mod-3 theorem is TRUE, but the machine check offered for it
does not isolate it. On the family this unit walks, the Born path measure is
identical for *every* homogeneous initial record — including records
differing by ONE — so "3 arena pairs agree at 12 of 12" is evidence of
homogeneity-invariance, not of mod-3. The conclusion survives and
strengthens; the attribution must move.**

§7.2 presents the theorem as measured rather than argued:

> The consequence for a signature question is severe, and it is
> **machine-checked here rather than argued**. **The Born branch measure is a
> function of the record modulo three: 3 arena pairs compared path by path
> agree at 12 of 12 branch-weight maps.**

The three pairs are `(A3,A6)`, `(A4,A7)`, `(A5,A8)` — all six members
homogeneous `(1,1,c)` rungs of the collinear family. This seat's clean-room
engine measured the path→weight map directly across a wider set of starts:

> **Every homogeneous initial record tested — (1,1,c) for c = 0…6, (a,1,1)
> for a = 1…4, plus (1,2,3), (0,0,0), (2,5,7), (3,1,4) — yields a
> byte-identical Born path measure at T = 3 and T = 4. Differences of ONE are
> included.** Off the homogeneous locus mod-3 *is* sharp: bumping a single
> cell by 1 changes the measure; bumping it by 3 does not.

So on the six records the instrument actually compares, agreement is
guaranteed by homogeneity alone and carries no information about the
residue. The mechanism §7.2 names — the parent's derived `ω^{n mod 3}`
register — is what really carries the theorem, and it is an *argument* from
`F5`, not a measurement.

**The conclusion is not damaged; it is sharpened.** The degeneracy is worse
than claimed, and worse in the direction the unit wants:

> **On the collinear family the Born-menu numbers of A3, A4, A5 and A7 differ
> only through the region predicate, never through the measure.**

The decisive exhibit, and it is new (ledger rows 77–78): **A4's Born
*singular* mass equals A5's Born *indefinite* mass exactly** — 64/59049 at
t = 3 and 15949136/1162261467 at t = 4. The same measure, on the same tree,
counted against two *different regions* at two *different arenas*, gives the
same number. Nothing states representative-relativity more sharply than that.

**Standing of this finding.** It is **measured, not proved**, at T ≤ 4, on a
sample of 14 homogeneous starts. This seat states it at exactly that
strength and does not upgrade it.

**Repair.** (a) §7.2's positive arm is restated as what it measures — the
Born path measure is constant across the homogeneous locus of this family,
differences of one included — with the unit re-running it at its own standard
and horizon. (b) The mod-3 attribution is carried by the parent's derivation
(`F5`, DERIVED, `ω^{n mod 3}`) and the machine check is described as
confirming a *consequence*, not as replacing the argument. (c) The instrument
gains **one off-homogeneous pair** — an inhomogeneous record and its
cell-bumped-by-3 partner — which is what actually isolates the residue, and
which this seat measured to be discriminating. (d) The A4-singular /
A5-indefinite coincidence is published; it is the best single exhibit in the
section.

---

## 6. ROW 3 — THE MOD-3 THEOREM: WHAT IS LICENSED, WHAT WOULD ANSWER THE ABSOLUTE QUESTION, AND THE MOTIF REGISTERED

### 6.1 The licensed sentence about absolute signature masses

The theorem is correct, is machine-checked two ways, and this seat has no
quarrel with any of its numbers. What it licenses is exactly:

> **No absolute region mass measured in this unit is a property of the
> dynamics. It is a property of the pair (the dynamics, the chosen
> representative of the record's mod-3 class). The Born branch measure is
> constant on that class; the signature is not; so the two are independent
> coordinates and any absolute mass reports the second while the measure
> reports only the first.**

SIG says this. Its "what may not be inherited" row already forbids the
absolute masses. **Licensed as written — and licensed a fortiori, since
MAJOR-5 finds the measure's degeneracy on this family to be wider than mod-3
rather than narrower.** MAJOR-5 moves the *evidence* for the theorem, not the
theorem and not this consequence.

**One clause must be added, and it costs nothing.** A7 = (1,1,5) is
indefinite at every site *before the walk starts* — 4 det q = −5 at t = 0.
Its indefinite mass of 1 is therefore an **initial condition, not a
dynamical outcome**, and neither §6.3 nor §7.2 says so. The demonstration is
not weakened by saying it — it is sharpened, because the sharpest possible
form of the blindness is that the Born measure cannot distinguish a record
that is *everywhere indefinite from the first step* from one that is
positive definite. **MINOR-1; repair: name the initial condition wherever
the "and 1" appears.**

### 6.2 What would answer the absolute question — and it is not a canonical representative

**A canonical representative would not answer it.** Choosing a
representative is a declaration; the resulting absolute mass would be
declaration-relative, not derived — the corpus has ruled this repeatedly
(v12's `REPRODUCES-AT-DECLARED-COMPLETION`; the completion-relative
exposure of W5's 576). It would convert an honest "representative-relative"
into a dishonest "absolute-at-a-declaration". **This seat rules a canonical
representative OUT as an answer, and IN only as a disclosed convention.**

**The connection is the right target, and it is more expensive than S-1
says.** SIG's S-1 asks for "a connection that consumes the count itself".
But paper-20 item `F5-CONNECTION-GROUP` is stamped **DERIVED**, fiber 1 —
"Z_3, because the arena is over F_3". Over Z₃ the register is ω^{n}, ω a
primitive cube root of unity, and **every such register is a function of
n mod 3 by construction.** So:

> **At this arena the mod-3 blindness is not a defect of a declared choice;
> it is forced by a DERIVED item, and the derivation is the arena's own
> field. The absolute question is therefore not merely unanswered here — it
> is unposable without converting `F5` from DERIVED to DECLARED, or changing
> the field.**

That is a strictly stronger successor statement than S-1's, it is a *price*
rather than a *task*, and it is what the successor register should carry.

**And the corpus has already priced part of that route.** The GDL
adjudication's successor register (`note-gdl-adjudication.md`, §SUCCESSOR
REGISTER) reads: "**GDL-2 (metric-consuming coins) carrying K2's no-go:
raising consumption strength m cannot rescue the blind functional AT ANY m —
the live route is breaking block-diagonality, which re-gates paper-20's
transport**." SIG's S-1 opens the metric-consuming-coin route without citing
the adjudicated no-go attached to it or the live route named beside it.
**MINOR-2; repair: S-1 cites GDL's ruling and inherits its named live route.**

### 6.3 The motif, REGISTERED (a row, not a claim)

**REGISTERED MOTIF — mod 3, third independent appearance.** Not a claim; no
mechanism is asserted to unify the three; each is a separate measurement in
its own unit.

| # | where | the object | the residue's role |
|---|---|---|---|
| 1 | paper-21 / #211, the **weld ladder** | R = n₁+n₂+n₃; a live weld is motivated exactly at **R ≡ 0 mod 3**, record (m,m,m) — which I7 never declares | a *budget* residue: which rungs admit a motivated weld |
| 2 | paper-25 GDL, the **residue channel** (`THEOREM C`, `GDL-THIRD-CHANNEL`) | "the step reads ω^{n mod 3} … every ψ-internal functional sees at most a **Z/3 shadow** of the metric"; verdict `THIRD-CHANNEL-PRESENT-AND-NOT-EXERCISED` | a *state-functional* residue: what the walk's internal observables can see |
| 3 | **paper-24 SIG, this unit** | the **branch measure** is a function of n₀ mod 3 while the **signature** is a function of n₀ | a *measure* residue: what any mass built from the tree can see |

All three trace to the same forced fact — the connection group is Z₃ because
the arena is over F₃ — and each exhibits a different consumer of it: the
grammar's budget, the state's functionals, the tree's measure. **The row is
registered as a motif and nothing is concluded from the coincidence.**

**MINOR-3, and it is an attribution.** SIG's §7.2 presents the residue
blindness as its own machine-checked theorem without citing GDL's `THEOREM
C`, which is earlier, committed, and read by this very run (the unit already
reads GDL at commit `4c85ca4` for constraint B). SIG's contribution is real
and is *the new half* — GDL proved the ψ-internal functionals blind; SIG
proves the **branch measure**, and hence every mass, inherits the blindness
while the signature does not. Repair: cite `THEOREM C`, and say which half is
new.

---

## 7. ROW 5 — THE BACK-REACTION-PUSHES-AWAY ROW: LICENSED AS A TWO-NUMBER COMPARISON AT ONE FIBER POINT, AND NOTHING MORE

The measurement is clean and this seat reproduced its direction at both
readings (ledger rows 45–46): the stage-frozen masses `34816/129140163` and
`325184/71744535` both **exceed** their coupled counterparts. The arm is
well-designed — it differs from the coupled arm in the phase update alone,
with the record still accumulating, so it does isolate the back-reaction from
the accumulation. Paper-20's own frozen control sits beside it at 0 by
theorem. **The design is right.**

**What is not right is the reach.** The receipt carries **exactly two**
`stage_frozen` values (ledger row 51): `/polarity/A/stage_frozen` and
`/polarity/B/stage_frozen`. The coin-fiber table of §7.1 has four columns and
none of them is the frozen arm. So the row is measured at **one arena of
three** and **one coin of five**, while the sentence it supports sits in §6.2
and §10 beside two adjectives — "coin-invariant, arena-invariant" — that were
earned by a *different* census.

**Licensed as:** *a two-number comparison at the clearing arena A4, at the
delivered coin GROVER, at the delivered coin order G·D, at horizon 5, under
both emission readings — an unreplicated measurement whose direction is
exact and whose invariance is untested.*

**Not licensed as:** a property of the back-reaction.

This is the R4b disposal rule verbatim — a bound quantity either carries an
invariance gate over the residual fiber or is stamped READING-RELATIVE.
**MINOR-4; repair:** §6.2's sentence gains "at this arena and at this coin";
§10's closing sentence is split so that "coin-invariant, arena-invariant"
attaches only to the polarity census (which earned them) and not to the
back-reaction clause (which did not); and a successor row registers the
frozen arm across the fiber — it is 4 extra arms and would convert a MINOR
into a result.

---

## 8. ROW 6 — THE ORDER-RELATIVITY OF "CHEAPEST": PROPER, AND AN EXEMPLARY §15 DISPOSAL

**Ruling: proper. This is the best-handled choice in the unit and it should
be left exactly as it is.**

Three cost orders are declared, all three are computed, they disagree, and
the unit publishes the disagreement rather than resolving it by fiat — then
selects A4 on a *measured* property (it is the only pair costing no new
declaration; the receipt's `no-new-declaration pairs ['A4']` is a
uniqueness, not a preference), and re-measures the sign at the other arenas
anyway. The cost order is disclosed in the choice inventory as declared with
fiber 3. That is precisely the declared-arena discipline, and it is the same
disposal the corpus made for the prime's scale-dependence and for
completion-relativity.

**MINOR-5, presentational only.** Neither §5 nor the head says the one thing
a hostile reader notices first: **A4 wins under none of the three declared
cost orders** (A3 takes two, A5 takes one). The unit's position is stronger
when it says so outright — it is the whole reason the selection had to be
made on a non-cost property. Repair: one clause in §5, "and A4 wins under
none of the three, which is why the selection is not a cost selection at
all."

---

## 9. ROW 7 — THE WALLS

**All four walls hold. The signature-resonance wall is, as the unit claims,
the sharpest instance of it in this line, and it is correctly the sharpest
because a determinant has actually gone negative.** Nothing in this seat's
sweep needs a repair.

- **The cosmological/Lorentzian sweep.** Every occurrence of `lorentz`,
  `cosmolog`, `spacetime`, `light cone`, `causal`, `continuum`, `metric` in
  the object (14 lines) is inside a *naming* or *declining* sentence: the
  §SCOPE paragraph, the four wall statements of §8, the two verbatim
  quotations (BHS's sprinkling row; paper-21's own naming sentence), the
  `SCOPE=` clause carried in the fourth fence, and the "what may not be
  inherited" row. **There is no assertive use anywhere.** The unit's own
  title carries no "Lorentzian" although the pin's and the plan's do — that
  is the right call and should be preserved through repair.
- **The naming sentence is derived from the measured floor code, not typed**,
  and a falsifier deletes it. That is stronger than the convention requires.
- **L-1** — argued, then declined, with the retracted sentence's absence
  gated under the #125 normalisation. Correct: this arena's translation
  action on Z₃² is not a covariance group and the unit builds no bridge.
- **BHS** and **Kleitman-Rothschild** — abstentions *measured* against this
  run's own declared measurement surface (32,316 characters), not declared.
  That is the right instrument.
- **The "selection" naming (§8 final paragraph)** is mandatory and present:
  SELECTED/AVOIDED are defined as a comparison against the declared counting
  measure and nothing more. **Note that MAJOR-1's repair makes this wall
  carry more weight**, since the corrected head prints both words on its
  face; the naming paragraph should be reproduced inside the fourth fence's
  `SCOPE=` clause, where it already partly is.
- **E-24.** Every mass in the object is stamped with its menu and its
  measure; three measures are declared in §6.1 and both probability measures
  are gated to sum to one. Discharged.

---

## 10. MINOR FINDINGS (collected)

- **MINOR-1** — A7's indefinite mass of 1 is an initial condition, not a
  dynamical outcome, and neither §6.3 nor §7.2 says so. (§6.1 above.)
- **MINOR-2** — S-1 opens the metric-consuming-connection route without
  citing GDL's adjudicated no-go and the live route named beside it.
  (§6.2 above.)
- **MINOR-3** — the mod-3 result is not attributed to GDL's `THEOREM C`,
  which is earlier, committed, and already read by this run; the genuinely
  new half (the *branch measure*, not the ψ-internal functionals) should be
  named as such. (§6.3 above.)
- **MINOR-4** — the back-reaction row's scope stamp. (§7 above.)
- **MINOR-5** — A4 wins under none of the three declared cost orders; say so.
  (§8 above.)
- **MINOR-6 — the coin fiber is 5 of a declared 6, and §7.1 says "all".**
  Paper-20's `F4` is stamped fiber **6** ("36 solutions … falling into 6
  classes up to a global phase, of which exactly 1 is ± Grover"; the four
  hidden classes are named). SIG's §7.1 opens "a fiber of **six** classes …
  **All of them run here**" and then tables **five**; the receipt's
  `/counts/coins` is 5 and the head says "ALL **5** S_3-COVARIANT CLASSES".
  The five run are Grover plus the four hidden — i.e. all the *non-trivial*
  classes, which is very likely the intended and correct statement. Repair,
  one clause: "a fiber of six classes, five of them non-trivial; all five
  non-trivial members run here." As printed, "all of them" is false of six.
- **MINOR-7 — `G-NULL-MEASURE`'s statement says "per object rather than in
  aggregate" for a check whose evidence is `steps checked 10`.** The check is
  sound and meaningful — each (measure, step) pair separately — but at ten
  checks it is a per-step total, and a per-step total over branches *is* the
  aggregate over branches. Compare `G-WALK-STOCHASTIC`, which earns the same
  phrase at 23,225 per-branch checks. Repair: the statement says "at every
  step of every reading separately" and drops "rather than in aggregate", or
  the check is taken per branch and the phrase is earned.

---

## 11. THE LICENSED CLAIM

After the four MAJOR repairs, this is what the object supports. Everything
here is measured in it and independently confirmed at this seat except where
marked.

1. **STAGE 0, STATIC — a four-class ladder, exhaustive, and it is the unit's
   best result.** Indefiniteness on this lattice is *free* if a record may
   leave links empty (one ROW round is indefinite at all nine sites, 4 det q
   = −1) and *expensive* exactly when links are occupied: a covered site at
   **R = 5** (attained, 2,210,000 witnesses); a covering record at **R = 6**;
   a structurally live covering record at **R = 7**; I7's own declared
   G-INDEF at **R = 8**. The obstruction is two-part and both parts are
   measured: a round deposits at most one incidence per cell (280 partitions,
   exhaustive), and a round's nine deposits are coupled by the partition, so
   concentrating and covering compete.
2. **The inherited #211 floor is NECESSARY AND ATTAINED at its own class.**
   The unit's contribution is the *class ladder above it*, not a correction
   below it.
3. **STAGE 0, DYNAMIC — the region is reached, and paper-20's open question
   is answered.** All three walked arenas occupy the indefinite region, at
   horizons their own event budgets predict, and the gated extension confirms
   the inherited dynamic floor of 6 on paper-20's own arena. This closes two
   of paper-20's three registered open measurements.
4. **STAGE 1 — the clearing pair is selected on a measured uniqueness, not a
   cost.** Cheapness is order-relative and published unresolved; A4 wins
   under none of the three orders and is chosen because it is the only pair
   costing no new declaration.
5. **THE CHANNEL MECHANISM (currency-free).** A round's deposit on a cell is
   coupled by the partition to eight deposits it does not choose; an
   emission's is coupled to nothing. Therefore the grammar cannot concentrate
   and cover at once, and the walk, inheriting a covering arena, is never
   asked to. **No superiority of either channel is licensed** — there is no
   declared exchange rate between a round and a step, and under a uniform one
   the grammar reaches every class first.
6. **STAGE 2/3 — THE POLARITY IS THE EMISSION READING'S, and that is a
   theorem, not a block.** Born menu: AVOIDED at 0.105 of the
   uniform-on-support counting measure on the same tree. Record menu:
   SELECTED at 2.88. Both exact; both invariant across paper-20's `F4` coin
   family, 5 of 5, at the delivered coin order; both invariant across the two
   arenas that clear inside the horizon. **The sign is a function of the
   declared emission reading alone and of nothing else measured here** —
   `SIG-DECLARATION-RELATIVE-AT-THE-EMISSION-READING`, the outcome the
   strategic plan pre-registered for this unit.
7. **What is NOT licensed on the coin axis:** coin-independence *simpliciter*.
   Paper-20's `F6-COIN-ORDER`, its own verdict-relevant fiber measured to
   move the exit mass 3.15×, is not run here.
8. **THE MOD-3 THEOREM — no absolute region mass in this unit is a property
   of the dynamics.** The Born branch measure is constant on the record's
   mod-3 class; the signature is not; so absolute masses are
   representative-relative and only the relative polarity is a candidate
   property of the dynamics. **On the family this unit actually walks the
   degeneracy is wider still** — the Born path measure is identical across the
   whole homogeneous locus, so A3, A4, A5 and A7 differ only through the
   region predicate, and A4's Born *singular* mass equals A5's Born
   *indefinite* mass exactly (64/59049 at t = 3). **And the blindness is
   forced by a DERIVED item**
   — the connection group is Z₃ because the arena is over F₃ — so at this
   arena the absolute question is not merely unanswered but unposable without
   converting `F5` from DERIVED to DECLARED, or changing the field.
9. **CONSTRAINT B — discharged twice, and the measured half is the good one.**
   The ensemble site marginal is identical at A4 and A7 while their
   indefinite censuses are 146623744/847288609443 and 1 (the latter an
   initial condition). GDL's blindness theorem is exhibited on the very
   quantity in question.
10. **SCOPE — and it holds.** A region of *record* space: the sign of a
    two-by-two form built from division counts on a nine-site lattice. Not a
    spacetime signature, not a light cone, not a metric on any continuum. No
    Lorentzian, causal, signature-change or cosmological reading is taken or
    licensed by anything measured here.

---

## 12. THE SUCCESSOR REGISTER

### 12.1 Who inherits the emission-reading question

**Ruling: nobody currently chartered inherits it, and it should not be given
to REQ2, to a SIG-2, or to GDL-1a. It belongs on the ROADMAP as a new named
question, because it is paper-20's `F10` fiber and paper-20 is terminal.**

- **REQ2 (paper-26)** is chartered to build "the HISTORY-DEPENDENT closure
  family the staleness theorem demands (records-theorem-native observables)"
  and re-run the requirement gate. The emission reading is not a closure
  family and forcing it in would blur REQ2's own two-way gate. **Declined.**
- **A SIG-2 at a canonical representative.** **Declined on the merits** — see
  §6.2: a canonical representative converts an honest
  representative-relativity into a declaration-relative absolute, which is
  the corpus's own named failure mode. A SIG-2 that is worth running is a
  SIG-2 at a **different connection**, and that is `F5`-DERIVED, i.e. an
  arena change, not a SIG-2 at all.
- **GDL-1a** is chartered on the two-time rate functional and already carries
  the metric-consuming no-go. It is the right *neighbour*, not the right
  owner. **The reconciliation SIG owes it is MINOR-2, not a handoff.**

**What the question actually is.** Both readings are `q(l|x)` transports of
the same law: reading A takes the post-coin Born weight, reading B takes the
division count. Nothing in the corpus derives either. **The question is
therefore a LAW-TRANSPORT question at paper-20's §4, not a signature
question** — and paper-20 itself pre-registered
`COUPLING-BLOCKED-AT-THE-LAW-TRANSPORT` as a first-class outcome for that
section, then confirmed the transport under *both* readings without
separating them. Registered as:

> **THE EMISSION-READING QUESTION.** Derive the menu from the law, or measure
> a third reading strictly between the two. It is `F10` of paper-20, it is
> verdict-determining for SIG, and it is the only declaration in either unit
> whose two members give opposite signs on the same measurement. First
> cheap probe: a one-parameter family interpolating the two weights, run at
> A4 to horizon 5, asking whether the sign crosses once or is discontinuous.

### 12.2 What PER-R's SIG feed should now carry

**The feed's direction has inverted and the pin should be read accordingly.**
`note-perr-pin.md` row 4 charters PER-R to compute "G-SINGULAR and G-INDEF
static reachability at R=5 — THE SIG FEED (this row is SIG's Stage-0 input)".
SIG has now run that census itself, exhaustively, and one budget further.
PER-R's binding row is therefore:

1. **The class ladder, not a number.** PER-R must state R = 5 reachability at
   the four named classes separately — unrestricted / covered site / covering
   / structurally live. Its pin's own phrasing is class-implicit and that is
   exactly what produced MAJOR-2. **This is the single most important thing
   this review hands forward.**
2. **The R = 5 answers, to be reproduced, not re-derived as a feed:**
   unrestricted YES at R = 1; covered site YES (2,210,000 multisets, witness
   with 13 empty cells); covering NO (16,108,764 multisets, min uncovered 2);
   structurally live NO. Any disagreement is a hard cross-seat conflict.
3. **The deposit theorem as an instrument** (see §12.3), which PER-R's own
   row 5 (is DIA still compulsory at R = 5/6?) needs directly: the 70-pool
   and the 36 saturating partitions are the objects that answer it.
4. **What PER-R must NOT inherit:** the phrase "the inherited floor is not
   attained" in any form, and any single-number statement of R = 5
   reachability.

### 12.3 The deposit theorem's export

**Ruling: it exports at the same level as #211's saturation schema — as a
budget-independent ARENA theorem, not as a SIG result — and it exports as a
PAIR, because one half of it does not do the work alone.**

> **THE DEPOSIT THEOREM (arena-level, budget-independent).** Over all 280
> partitions of the nine sites into three conflict triples: a round deposits
> **at most one** incidence on any one cell and **at most two** on any one
> site; the incidence spectrum is 0:1, 4:27, 6:54, 7:162, 9:36; 36
> partitions are foreign-pair-free and every one of them deposits 9.
> Consequently a cell's count after R rounds is at most R.

This is the **per-cell** sharpening of #211's exported aggregate ("no round
deposits more than 9 link incidences"), and it belongs in the same register
row, cited the same way, by every unit at every budget.

**The pairing, which must travel with it.** The deposit theorem alone does
*not* give paper-21's max-cell-2 row: at R = 4 it permits a cell at 4. This
seat confirmed the row directly instead (ledger row 40, 16,699,200 probes:
no covering quadruple has a cell at 3 or above). **The second half of the
obstruction is the covering obligation** — a round's nine deposits are
coupled by the partition, so a round spent concentrating cannot be spent
covering. It is the *pair* that produces the ladder:

| budget | deposit half permits | covering half forbids | result |
|---|---|---|---|
| R = 4 | a cell at 4 | anything above 2 in a covering record | max cell 2 (paper-21) |
| R = 5 | a cell at 5 | covering at all when 5 rounds sit on one cell | min uncovered 2 (SIG) |
| R = 6 | a cell at 6 | foreign-pair-freeness | covering YES, live NO (SIG) |

**Export both halves or neither.** A successor that carries only the deposit
theorem will re-derive SIG's R = 5 row and get the wrong class — which is
precisely MAJOR-2's failure mode, one budget on.

### 12.4 Registered rows this review adds

- **SR-A** — run `D·G` at A4, horizon 5, both readings. One arm. It closes
  MAJOR-4's scope gap and tests whether the *sign* survives the parent's own
  verdict-relevant fiber. **Cheapest strengthening available to this unit.**
- **SR-B** — run the stage-frozen arm across the coin fiber and the two
  clearing arenas (4 extra arms). Converts MINOR-4 into a result about the
  back-reaction.
- **SR-C** — the currency question of MAJOR-3: is there any *derived*
  exchange rate between a round and a step in this corpus? If there is, the
  channel comparison becomes a theorem; if there is not, that itself is worth
  a row.
- **SR-D** — the R = 6 covering witness is not structurally live and the
  first live one costs another round (SIG's own S-5). Registered as SIG
  wrote it; unchanged.
- **SR-E** — the mod-3 motif's third appearance, registered as a **motif
  row** at §6.3. Nothing is claimed from the coincidence and no successor is
  chartered on it.
- **SR-F** — **the homogeneous-locus degeneracy (MAJOR-5) is a question in
  its own right.** Why is the Born path measure constant across *every*
  homogeneous initial record on this family, including neighbours differing
  by one? A homogeneous record makes `D(x)` site-independent, so the coin
  factorises as `G·D_c·Δ(x)` with `D_c` global — but `G·D_c` is not Grover
  and the invariance is not obvious from that alone. This seat measured the
  fact at T ≤ 4 on 14 starts and did not prove it. **If it is a theorem, it
  is a sharper statement of arena-blindness than the mod-3 one and belongs in
  the register beside it; if it fails at larger T, the mod-3 instrument's
  chosen pairs become diagnostic after all.** Either outcome is worth one
  horizon.

---

## 13. SUMMARY OF REPAIRS (binding list)

| # | class | what moves | where |
|---|---|---|---|
| 1 | MAJOR | the outcome word: `BLOCKED-AT-THE-EMISSION-READING` → `DECLARATION-RELATIVE-AT-THE-EMISSION-READING` (or `READING-STRATIFIED`); content kept verbatim; §7.3's conclusion re-pointed | fence 4 (×2), §7.3, §10, the comparator's conditional |
| 2 | MAJOR | the floor clause: class named, "not attained" → "attained at its own class", the ladder stated as an addition | fence 1 (×2), §1, §3.3 title+body, §10, `G-STATIC-FLOOR`'s sealed statement, `PL-STATIC-R5`'s pre-registration |
| 3 | MAJOR | the walk-beats-grammar sentence gains its currency stamp; the rate mechanism is replaced by the coupling mechanism | §5, §10, S-3 |
| 4 | MAJOR | inventory item 3 split; the five inherited declared fibers disclosed with `F6`'s VERDICT-RELEVANT stamp; "coin-invariant" scoped to `F4` at `G·D` | §9 table, §7.1, fence 4, §11 (new deviation) |
| 5 | MAJOR | the mod-3 instrument's positive arm restated as homogeneity-invariance; one off-homogeneous pair added; the residue attributed to `F5`'s derivation; the A4/A5 coincidence published | §7.2, fence 4's `MOD-3 THEOREM=` clause |
| 6 | MINOR ×7 | as listed in §10 | as listed |

**No delivered number changes. No verdict segment is deleted.** Segments 1–3
survive with their scope words corrected; segment 4 keeps every measurement
it carries and changes only the word printed in front of them and the
evidence clause behind its mod-3 conjunct.

---

## 14. SEAT STATEMENT

This is a strong unit. Its static census is exhaustive where it claims to be,
its dynamic census answers two of its parent's three registered open
questions, its walls are the sharpest in the line and are *measured* rather
than declared, and its instrument is of the standard the era now expects —
45 gates, 38 falsifiers each dying at its own named gate, a total seal, a
head derived twice by routines sharing no numeric literal. **Seventy-eight
independent recomputations moved nothing — including a clean-room rebuild of
the parent's whole coupled machine, which anchored on six of paper-20's
committed rows at the first attempt and then reproduced every dynamic number
in this unit, two of them twice.**

Its five MAJORs share one shape, and it is worth naming: **in each, the unit
measured something excellent and then described it as something else.** It
measured a class ladder and called it a correction. It measured a coupling
obligation and called it a rate. It measured a fiber to exhaustion and called
itself blocked. It inherited five declared fibers and called them forced. It
measured a degeneracy wider than mod-3 and reported mod-3. The repairs return
each sentence to what the object under it actually says, and in three of the
five the returned sentence is the stronger one.

**Hashes re-verified at close: `72175d6fa85b`, `a41b6d549e14`,
`f28b550c151e`, `ca9cd4ceb387`, `ab73239daff5` — all five unchanged.**
