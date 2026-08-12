# ACT (paper-34) — INSTRUMENT REVIEW (K3)

**Seat:** INSTRUMENT-LENS — gates, mutants, anchors, seals, transcripts, walls;
the six PER-R template probes with live injections; the #267 checklist;
referent-binding; the CLI and #91 contract. **Object at `b3417e1`** (`v14 #290`),
verified at open and at close.

**GRADE: AWF** — accept with fixes. **No measured quantity of this unit is
wrong.** Every headline number I could reach was recomputed here by routes the
instrument does not use — including a from-scratch rebuild of the arena in a
different representation of $\mathbb{Q}(\zeta_8)$ (4-tuples of `Fraction` in
$\mathbb{Q}[x]/(x^4+1)$ rather than the instrument's integer 5-tuple), which
reproduced the alphabet, the 640 coins, the 64/64/512 split, plaquette
independence on the carrier, the 11 trace values, the $[0,4]$ and $[-1,1]$
ranges and **the null expectation $13/10$ exactly** — and all agreed. The unit
is byte-reproducible off-tree, git-less, at two hash seeds. **All five majors
are perimeter defects: things the instrument or the paper SAYS it binds and
does not.** Three of the six PER-R template diseases are PRESENT and three are
ABSENT — and the three that are absent are absent because this unit *fixed*
them, which is a real improvement on PER-R.

---

## 0. HASHES — VERIFIED AT OPEN AND AT CLOSE

| object | declared (sha256-12) | at open | at close |
|---|---|---|---|
| `v14/paper-34-act.md` | `3fbf109f0d9b` | `3fbf109f0d9b` | `3fbf109f0d9b` |
| `v14/code/act_exact.py` | `02df3f00f788` | `02df3f00f788` | `02df3f00f788` |
| `v14/code/act_output.txt` | `9299f80db2d8` | `9299f80db2d8` | `9299f80db2d8` |
| `v14/code/act_receipt.json` | `f0617d1687a0` | `f0617d1687a0` | `f0617d1687a0` |
| `v14/note-act-pin.md` (pin) | `766c603c6dbc` | `766c603c6dbc` | `766c603c6dbc` |

All execution was off-tree in scratch mirrors built by `rsync --exclude .git`.
Sibling working-tree drift (SIG, SEC) was neither read nor touched. Repo writes
by this seat: **one** — this file.

**Counts.** **128 instrument executions**: 3 full delivery runs off-tree
(`PYTHONHASHSEED` 0 and 99991, both byte-identical to the committed artifacts,
plus one echoing run), 49 out-of-harness `--mutant` runs one process each, 33
paper-injection runs, 13 write-path probe runs, 18 hostile-argv invocations, 5
source/anchor corruption runs, 3 code-injection runs, 3 tree-hash battery runs
(`--no-write`, `--selftest`, clean), 1 bare-copy run. **44 novel injections of
my own design** plus the 49 registry mutants = **93 corruption events**, each
observed to its terminating gate. **≈ 265 independent recomputations** of
published quantities (itemised in §3), zero disagreements.

---

## 1. THE SIX PER-R PROBES — EACH ANSWERED, WITH THE INJECTION

| # | PER-R template disease | ACT verdict | the measurement |
|---|---|---|---|
| 1 | **unbound table headers** | **PRESENT — MAJOR-1** | 5 of 5 semantically-opposed header swaps survive at exit 0 and are DELIVERED. 34 of 34 table data rows are bound to a rendered claim; **0 of 5 header rows are**. 4 of 4 data-cell control forgeries die at `G-PAPER-CLAIMS`. |
| 2 | **transcript-integrity whitelist forgery** | **ABSENT** | There is no whitelist and no tail clause. `G-ARTIFACT-INTEGRITY` compares the staged transcript byte-for-byte (`open(tmp).read() == outtxt`). A forged nine-space-indented line carrying a closing gate name, appended to the staged file, **dies at `G-ARTIFACT-INTEGRITY` with nothing promoted** (W1). |
| 3 | **phantom consumers** | **PRESENT — MAJOR-3** | `consumer` occurs 4 times in 4,519 lines, all in producers. All **53** consumer names rewritten to `G-DOES-NOT-EXIST` → exit 0, and the delivered receipt carries `G-DOES-NOT-EXIST` on all 53 anchor rows against a 45-row ledger that contains no such gate. The paper vouches "each bound to the gate that consumes it" **twice**. |
| 4 | **honest denominator** | **ABSENT** | 47 gate ids; **46 carry a declared mutant, 1 (`G-ARTIFACT-INTEGRITY`) a registered forcing, 0 uncovered**. The ledger's published denominator is 37, and all 10 omissions are named in `late_gates_declared` — I checked each of the 10 and every one is mutant- or forcing-covered. This is PER-R MAJOR-5 **fixed**. (MINOR-3 on the presentation.) |
| 5 | **wall surface** | **ABSENT** | The declared surface is "this paper's own text", and the sweep covers it in full: 5 of 5 plants die — plain, inside a blockquote, under emphasis, **line-wrapped across a newline**, and inside an inline code span — all with artifacts unchanged. There is no "every published receipt key" over-claim to be unmeetable. I additionally swept all 9 banned words over the receipt and the transcript by hand: **every hit is inside a withholding/declaring string or the mutant registry's own description — no breach.** (MINOR-5.) |
| 6 | **closing-gates warrant** | **ABSENT** | `closing_gates` is a bare two-name list carrying **no warrant prose**, so there is no false sealed sentence to inherit. Clause 1 is moot: the delivered transcript carries no gate rows at all and nothing claims it does. Clause 2 is **FIXED**: `G-ARTIFACT-INTEGRITY` is evaluated on the staged temporaries and raises **before** `os.replace`; W3 (forged sealed key) and W4 (forged verdict string) both die with the published artifacts untouched. (MINOR-7 on the residual staging window.) |

**Three of six PER-R diseases reproduce; three are repaired.** The two
repaired-and-verified ones (4 and 6) are the two PER-R named as the hardest.

---

## 2. THE #267 TEMPLATE-CHECKLIST AUDIT (the pin's WALLS name it by item)

| #267 item (pin WALLS) | measured | verdict |
|---|---|---|
| paper-scanning walls | 5 plants, 5 deaths, all on the paper leg, artifacts unchanged | **COMPLIANT** |
| all tables rendered | 34 of 34 data rows bound; **0 of 5 header rows bound** | **NOT COMPLIANT** (MAJOR-1) |
| no typed counts | 47/45/49/64/36/85/26/19/13 all derived from live registries (`len(LD.rows)`, `len(MUTANTS)`, `len(SOURCES)+len(PATH_VALUES)+len(VERBATIM)`, `len(SEAL.man)`, `len(claims)`, `len(trows)`, `len(quotes)`, `len(S["fibre"]["rows"])`) — I re-derived every one | **COMPLIANT** |
| full-transcript integrity | full-text byte equality at the disk boundary; W1 dies | **COMPLIANT ON THE TRANSCRIPT, NOT ON THE RECEIPT** (MAJOR-2) |
| digest-free whitelists | no whitelist exists; the numeral scan removes backticked 12-hex digests but each digest is separately bound as a rendered claim — NUM-3 and NUM-6 (one-character digest typos) both die at `G-PAPER-CLAIMS` | **COMPLIANT** |
| spelled numerals | the scanner is `\d`-only; **no number-word is scanned at all** | **NOT COMPLIANT** (MAJOR-5) |

Four of six pin-named checklist items hold.

---

## 3. WHAT I RECOMPUTED, AND BY WHAT ROUTE

**(a) The arena, rebuilt from scratch** (`scratchpad/indep_arena.py`, 177 lines,
no import from the instrument, $\mathbb{Q}(\zeta_8)$ carried as 4-tuples of
`Fraction` in $\mathbb{Q}[x]/(x^4+1)$ — a *different representation* from the
instrument's integer 5-tuple with a common denominator, and independent matrix
code). It reproduced, from 10,240 holonomy evaluations:

- alphabet **25**; admissible rows **80**; coin family **640**
- sectors **64 / 64 / 512**, summing to 640 with nothing left over
- **0** column-unitarity failures (the second route)
- 16 sites, 32 links, 16 plaquettes
- **0** of 640 carrier configurations plaquette-dependent
- **11** distinct trace values, all in $\mathbb{Q}(\sqrt2)$
- rational-part range **$[0,4]$**; surd coefficients $\{-1,-\tfrac12,0,\tfrac12,1\}$ → surd range **$[-1,1]$** — the two unpinned falsifier rows
- **$E_{\text{counting}}[\mathrm{tr}] = 13/10$ exactly**, surd part 0 — the published null expectation

**(b) 43 arithmetic identities across the census, Gibbs, price and falsifier
tables, all agreeing**, including: couplings $=$ orbits $-1$ at all 6 rows;
reachable dimension $=$ classes $-1$ at all 6; fibre $=$ couplings $-$ reachable
at all 6; $208-72=136$ and $120-40=80$; $207-135=72$ and $119-79=40$;
vertices $+$ midpoints $= 64+72 = 136 =$ classes; vertices $=$ orbits $-2\times$pairs;
pinned indicators $= 2\times$merged pairs at both readings ($144=2\cdot72$,
$80=2\cdot40$); exponents $=$ links / plaquettes / sites ($32/16/16$).

**(c) The density witness, exactly.** $(101275/100000)^{32}-3/2 = 6.631\times10^{-5}$
(computed as an exact `Fraction`): below $10^{-4}$ and **not** below $10^{-5}$.
The published bound is the tight one.

**(d) The mechanism behind the whole price, by hand.** A constant twist $k$ is
realisable iff $4k\equiv 0 \pmod 8$ iff $k$ even — the paper's claim, confirmed.
`gauge_twist(m,k) = (a, z^k b, z^{-k} c, d)`, so the off-diagonal fourth powers
acquire $z^{4k}=(-1)^k$: **odd twists reverse the quartic sign, even twists
preserve it.** The falsifier's headline mechanism is exactly what the paper says
it is.

**(e) The chained ledger, recomputed.** `digest({"prev": prev, "row": row})`
over the 45 published rows: **45 of 45 match, zero mismatches**, all `passed`,
all `kind = MEASURED`.

**(f) The paper-side scanners, reimplemented.** 19 blockquote groups, 5 header
rows, 34 data rows of which 26 carry a numeral, 343 numerals after the declared
removals, 36 inline spans with a numeral, 2 fence markers, 85 rendered claims
**each located at exactly its declared occurrence count** — every figure in the
prompt's list reproduced from the registries.

**(g) E-23, three-legged.** 49 of 49 published mutant tokens located in the
source; **0** gate predicates reference `mut()`; 49 of 49 mutant targets are real
`LD.gate` call sites; 48 call sites in the tree, 47 on the clean path.

**(h) The 49-mutant sweep, outside the harness.** Registry read from the source
text (not the receipt). 49 separate processes, `--mutant NAME` each:
**49 of 49 DEAD-ON-TARGET, `artifacts unchanged True` on every one**, and the
whole mirror (artifacts + instrument) byte-identical before and after.

---

## 4. THE INJECTIONS

| # | injection | outcome |
|---|---|---|
| INJ-1..5 | swap semantically-opposed header pairs: `orbits`↔`couplings` (§3); `reachable dimension`↔`fibre` (§6); `over the invariant simplex`↔`over the reachable set` (§8); `class-constant`↔`full support` (§7); `pre-registered outcome`↔`measured` (§1) | **5/5 SURVIVE at exit 0 and are DELIVERED** — MAJOR-1 |
| CTRL-A..D | data-cell forgery (136→137); row-verdict swap (`REACHABLE`→`UNREACHABLE-BY-SUPPORT`); falsifier verdict flip (`pinned`→`unpinned`); prose numeral off-by-one (72→73) | 4/4 die at `G-PAPER-CLAIMS`, artifacts unchanged |
| INJ-6 | all 53 anchor `consumer` names → `G-DOES-NOT-EXIST` | **SURVIVES, delivered** — MAJOR-3 |
| WALL-1..5 | banned vocabulary planted plain / in a blockquote / under emphasis / line-wrapped / in an inline code span | 5/5 die at `G-MUST-NOT-VOCABULARY` |
| NUM-1 | `twenty-five elements` → `twenty-six elements` (the alphabet count, anchored at `PV-ALPH`) | **SURVIVES** — MAJOR-5 |
| NUM-2 | `a ten-dimensional sliver` → `a fourteen-dimensional sliver` (the Wilson dimension, in the verdict) | **SURVIVES** — MAJOR-5 |
| NUM-3, NUM-6 | one-character typo in a backticked 12-hex digest (pin; SMU paper) | 2/2 die at `G-PAPER-CLAIMS` |
| NUM-4 | unbacked numeral `987654321` planted in prose | dies at `G-PAPER-NUMERAL-COVERAGE` |
| NUM-5 | numeral mutated **inside the fenced verdict block** (`ORBITS=136`→`137`) | dies at `G-PAPER-VERDICT-EQUALITY` |
| E22-1..3 | delete the fence; duplicate the fence; move an inline numeral inside it | 3/3 die at `G-PAPER-VERDICT-EQUALITY` (multiset, both directions) |
| POL-1 | declared negator inserted before a polarity fragment | dies at `G-PAPER-POLARITY` |
| VB-1 | invert a quoted parent definition (`ordered product`→`unordered sum`) | dies at `G-PAPER-TABLES-AND-QUOTES-ARE-BOUND` |
| VB-2 | forge a blockquote lying in no pinned window | dies at `G-PAPER-TABLES-AND-QUOTES-ARE-BOUND` |
| HEAD-1 | `**The form is not forced.**` → `**The form is forced.**` (§10 bullet 1) | **SURVIVES** — MAJOR-4 |
| HEAD-2 | swap a pre-registered outcome LABEL in the §1 table | dies at `G-PAPER-CLAIMS` |
| HEAD-3 | `measured **not** transitive` → `measured **transitive**` (§5.1) | **SURVIVES** — MAJOR-4 |
| HEAD-4 | `**The falsifier hits...` → `**The falsifier misses...` (§8) | **SURVIVES** — MAJOR-4 |
| SCOPE-1 | §13 scope disclosure inverted (`on the carrier` → `on the full datum space`) | **SURVIVES** — MAJOR-4 |
| W1 | forged line appended to the STAGED transcript before the gate | dies at `G-ARTIFACT-INTEGRITY`, nothing promoted |
| W2 | forge the UNSEALED `gates` / `totals` keys in the staged receipt | **SURVIVES — delivered at exit 0** — MAJOR-2 |
| W3 | forge a SEALED key (`arena.coins`) in the staged receipt | dies at `G-ARTIFACT-INTEGRITY` |
| W4 | forge the verdict string in the staged receipt | dies at `G-ARTIFACT-INTEGRITY` |
| W5 | corrupt the staged receipt AFTER the gate, before `os.replace` | promoted (MINOR-7 — the window is empty in the delivered source) |
| W6 | forge a summary line into `LOG` before the transcript is built | promoted, self-consistently (MINOR-2 — the transcript is by definition the log) |
| SRC-1..3 | pinned source deleted; one byte appended to a pinned receipt; the pin corrupted | 3/3 die at `G-SOURCE-BYTES`, **no traceback**, artifacts unchanged |
| SRC-4 | the paper deleted | dies at `G-PAPER-PRESENT`, no traceback |
| SRC-5 | a verbatim window inverted inside a parent paper | dies at `G-SOURCE-BYTES` (the file-bytes anchor dominates — defence in depth) |
| BARE | the instrument alone in an empty directory | refuses at `G-SOURCE-BYTES`, **exit 1, no traceback** (PER-R's MINOR-6 fixed) |

---

## 5. MAJOR FINDINGS

### MAJOR-1 — REFERENT BINDING: EVERY TABLE'S COLUMN HEADERS ARE UNBOUND

`verify_paper` collects header rows into `theads`, counts them, publishes
`table_header_rows_excluded: 5` — and never matches one. The gate statement
concedes it: *"Header rows are the declared exception and are counted and
published rather than silently skipped."* Disclosure is not binding, and the pin
names "all tables rendered" as a wall.

Measured: **34 of 34 data rows are bound to a claim rendered from the receipt;
0 of 5 header rows are.** Five swaps of semantically opposed columns all survive
at exit 0 and are written into the delivered artifacts:

- §3: `orbits`↔`couplings` makes 136 the coupling count and 135 the orbit count
  — inverting the paper's own central identity, "rank = orbits minus one", which
  the verdict string states as `RANK-ORBITS-MINUS-ONE`.
- §6: `reachable dimension`↔`fibre` makes the link grain's fibre 135 and its
  reachable dimension 0 — the exact inverse of the headline, and of
  `THE-FIBRE-IS-EXACTLY-THE-NORMALISATION-AT-THE-LINK-GRAIN-DIMENSION-0`.
- §8: `over the invariant simplex`↔`over the reachable set` turns the falsifier
  inside out: the pinned $[0,0]$ becomes the range over the *parent's* simplex
  and $[-2,2]$ the range over the reachable set — i.e. the action route *widens*
  the observable instead of pinning it. This is the unit's headline finding,
  reversed, at exit 0.
- §7: `class-constant`↔`full support` reassigns which target fails by support.
- §1: `pre-registered outcome`↔`measured` inverts the outcome table.

The controls prove the gate is otherwise sound (CTRL-A..D, 4/4 dead).

**REPAIR R-ACT-1.** Render each table's header row from the receipt alongside
its data rows and require it to occur exactly once. Every column name is already
a receipt key or a published label — `orbits`, `coupling_count`,
`reachable_dimension`, `fibre_dimension`, `range_over_the_invariant_simplex`,
`range_over_the_reachable_set`, `class_constant`, `full_support` — so the header
renders from the receipt with no new declaration. Then re-point `MUT-TABLE-ROW`
(or add `MUT-TABLE-HEADER`) at a header swap.

### MAJOR-2 — THE DISK-BOUNDARY CHECK COVERS THE 36 SEALED KEYS AND NOT THE 15 DECLARED-UNSEALED ONES; THE GATE LEDGER CROSSES UNGUARDED

`G-ARTIFACT-INTEGRITY` does two things: full byte equality for the transcript
(`open(tmps[0][0]).read() == outtxt`) and `SEAL.reverify(back)` for the receipt.
`reverify` walks `SEAL.man` — **the 36 sealed keys only**. The 15 keys in
`DECLARED_UNSEALED` reach disk with nothing compared to them, and they include
`gates` (the entire ledger with every verdict and every evidence string),
`gate_digests` (its chain), `totals`, `mutants`, `closing_gates` and
`transcript_head`.

Demonstrated (W2): a patched writer edited the staged receipt between the write
and the read-back, setting `totals["gates"] = 4242`, `gates[0]["passed"] = false`
and `gates[0]["detail"] = "FORGED: 0 of 11 source digests match"`. Result:
**`G-SEAL-INTEGRITY` PASS, `G-ARTIFACT-INTEGRITY` PASS, exit 0, both artifacts
promoted** — a receipt declaring its own provenance gate FAILED, beside a
17-line transcript that says nothing is wrong. The transcript, being a summary
with no gate rows, contains no contradiction a reader could catch.

This is PER-R MAJOR-7's second clause recurring in a new location. Two honest
qualifications, both measured: (i) no gate *statement* is false — the gate says
"every **sealed** object", which is exactly what it checks; (ii) my particular
W2 forgery is externally detectable, because I edited `gates` and not
`gate_digests`, and I confirmed the committed chain verifies 45/45. A forgery
consistent across both keys would not be.

**REPAIR R-ACT-2.** One line: keep `blob` and assert
`open(tmps[1][0]).read() == blob` beside the existing `txt_ok`, giving the
receipt the same total byte check the transcript already gets. Add
`MUT-DISK-UNSEALED` planting a forged `gates` row in the staged file.

### MAJOR-3 — THE ANCHOR "CONSUMER" REGISTER HAS A PRODUCER AND NO CONSUMER

The paper says it twice — in the front matter (*"each bound to the gate that
consumes it"*) and in §11 (*"and each bound to the gate that consumes it"*) —
and the gate statements repeat it: `G-PATH-VALUE-ANCHORS` says *"each is bound
to the gate that consumes it"*, `G-VERBATIM-ANCHORS` says *"and is bound to the
gate that consumes it"*.

`consumer` appears at exactly **4 lines in 4,519**: the two tuple unpacks
(1143, 1169) and the two dict writes (1151, 1181). No gate predicate reads it,
no cross-check compares it against `LD.ids`, and nothing requires the named gate
to exist or to have closed.

Demonstrated (INJ-6): all **53** consumer names rewritten to `G-DOES-NOT-EXIST`.
Exit 0; the delivered receipt carries `{"G-DOES-NOT-EXIST": 53}` across
`path_value_anchors` and `verbatim_anchors`, against a 45-row ledger in which
that name does not occur. This is LOR MAJOR-4 / PER-R MAJOR-4 in its pure form.

**The same disease has a second instance.** §11 says *"The gate ledger is
chained row by row, so a row edited after its gate closed no longer matches the
digest of its own predecessor."* The chain is built (`Ledger.gate` appends
`digest({"prev": prev, "row": row})`) and published — and **never verified**:
`digests` occurs only at its three producer lines and at the payload assignment.
The stated protection is real arithmetic that nothing in the instrument
performs. I performed it: 45 of 45 clean.

**REPAIR R-ACT-3.** (a) Add a gate requiring
`{r["consumer"] for r in rows} ⊆ LD.ids` at the point where the ledger is
complete (the late-gate slot), with a mutant pointing one consumer at a
nonexistent gate. (b) Add a chain-verification gate that recomputes
`digest({"prev": prev, "row": row})` over `LD.rows` and compares to `LD.digests`
element by element, and re-take it inside `G-ARTIFACT-INTEGRITY` against the
bytes read back from disk (which R-ACT-2 makes possible).

### MAJOR-4 — DIRECTION-BEARING HEADLINE SENTENCES ARE UNBOUND OUTSIDE A FOUR-FRAGMENT POLARITY LIST

`POLARITY` carries four fragments. §10's "Decided" list carries seven bullets
and the body carries many more direction claims. Four survive inversion at exit
0 and are delivered:

- **HEAD-1**: `- **The form is not forced.**` → `- **The form is forced.**`.
  This is §10's *first* decided bullet and the negation of the unit's own
  verdict head `ACT-FORM-RELATIVE-...-NOTHING-IS-FORCED`.
- **HEAD-3**: `the gauge group is measured **not** transitive on a single link's
  coin` → `**transitive**`. This inverts §5.1's entire reason the Wilson shape
  is not forced, and it directly contradicts the verdict string printed 250
  lines above it: `NOT-TRANSITIVE-ON-A-LINKS-OWN-DATUM`. A paper can now assert
  a proposition and its negation and pass.
- **HEAD-4**: `**The falsifier hits, and it hits at the strongest setting...` →
  `**The falsifier misses, and it misses at...`, against a verdict reading
  `FALSIFIER=HIT`.
- **SCOPE-1**: §13's third scope disclosure inverted from `reported **on the
  carrier**` to `on the full datum space` — deleting the very limitation the
  paragraph exists to record.

The polarity gate is sound where it reaches (POL-1 dies); the defect is reach.

**REPAIR R-ACT-4.** Render §10's seven decided bullets and §13's five scope
sentences as claims from the receipt (each has a receipt field behind it:
`form_census`, `wilson.why`, `falsifier.verdict`,
`wilson.dimension_of_the_wilson_family_on_the_carrier`), and extend `POLARITY`
to cover them. Cheapest sufficient fix: require the verdict's own polarity
tokens (`NOTHING-IS-FORCED`, `NOT-TRANSITIVE`, `HIT`) to have a consistent prose
rendering located in the body.

### MAJOR-5 — SPELLED NUMERALS ARE NOT SCANNED AT ALL; TWO LOAD-BEARING COUNTS ARE FREE

The pin's WALLS name "spelled numerals" as a #267 checklist item. The coverage
scanner is `re.findall(r"\d+(?:/\d+)?(?:\.\d+)?", scan)` — digits only. No
number-word is scanned, in either direction.

Two live inversions, both surviving at exit 0 and delivered:

- `The coefficient alphabet returns **twenty-five** elements` → `twenty-six`.
  25 is a path-value anchor (`PV-ALPH`, `counts/alphabet`) verified against R5's
  pinned receipt; the paper can misreport it freely.
- `a **ten**-dimensional sliver` → `a **fourteen**-dimensional sliver`. 10 is
  the Wilson family's dimension on the carrier and appears in the verdict as
  `SPANS-10-OF-135-COUPLINGS`. Note that the corrupted form, "fourteen", is
  *above twelve* — precisely the class #267 requires to be scanned.

The paper contains exactly one spelled numeral above twelve ("twenty-five"),
so the fix is cheap and the exposure is small — but it is exposure on an
anchored count.

**REPAIR R-ACT-5.** Add a number-word alphabet (`thirteen`…`ninety`, `hundred`,
`thousand`, and the hyphenated compounds) to the coverage scan, mapped to
integers and matched against the same `allowed` pool; render the two occurrences
as claims (`"returns %s elements" % numword(ar["alphabet"])`,
`"a %s-dimensional sliver"`). Add `MUT-SPELLED-NUMERAL`.

---

## 6. MINOR FINDINGS

**MINOR-1 — `--list-gates` lists 46 mutant targets, not the 47 gates.**
`for gx in sorted({m[1] for m in MUTANTS})`. `G-ARTIFACT-INTEGRITY` — the gate
that guards the disk boundary — appears in no listing. Undisclosed convention;
PER-R MINOR-5 recurring. *Fix:* list `LD.ids` after a `--no-write` run, or
document the convention in `USAGE`.

**MINOR-2 — the run's own totals line is echoed but not delivered.**
`say("GATES %d (+%d closing) :: MUTANTS %d :: ANCHORS %d :: SEALED %d")` runs
*after* `seal_and_write` has already built
`transcript = "\n".join(LOG) + "\n" + verdict + "\n"`. The terminal prints
`GATES 45 (+2 closing) :: MUTANTS 49 :: ANCHORS 64 :: SEALED 36`; the delivered
`act_output.txt` is 17 lines and ends at the verdict. A reader of the artifact
never sees the tallies. *Fix:* build the transcript after the summary line, or
move the summary before `seal_and_write`.

**MINOR-3 — the coverage ledger's 37 is honest but unpriced.** `gates_closed: 37`
with `late_gates_declared` naming the 10 omissions is a genuine improvement on
PER-R, but the receipt does not say that 9 of the 10 carry mutants and 1 a
forcing. A reader sees 37/37 and ten bare names. *Fix:* publish
`late_gate_coverage` mapping each of the 10 to its mutant or forcing, and
restate the evidence as `gates 47 of 47`.

**MINOR-4 — a waiver that can never fire, disclosed.** `FORCINGS` carries
`G-MUTANTS-ON-TARGET`, whose own text says *"no such gate exists in this
instrument"*. The count excludes it (`forced = 1`), so nothing is inflated — but
it is a dead row in a registry the seal vouches. *Fix:* move it to a separately
named `EXTERNAL_BATTERY` note.

**MINOR-5 — the wall holds on the receipt as a fact, not as a guarantee.** The
must-not sweep runs on the paper only. I swept all 9 banned words over the
delivered receipt and transcript by hand: every occurrence is inside a
withholding string (`NO-AREA-LAW-...`, `must_not`, `NO-CONFINEMENT-CLAIM`) or
inside `MUT-MUST-NOT`'s own published description. Clean today; ungated
tomorrow. *Fix:* run the same sweep over the serialized receipt with the
withholding keys and the mutant registry excluded by key, as a gate.

**MINOR-6 — `G-PAPER-PRESENT` is a 48th gate id invisible to every total.**
There are 48 `LD.gate` call sites and 47 on the clean path. `G-PAPER-PRESENT`
(a constant-`False` refusal gate reached only when the paper is absent — SRC-4
shows it fires and is fatal) appears in `totals.gates`, in the waiver ledger,
and in `--list-gates` **nowhere**. Not a coverage defect (it never closes), but
the honest gate inventory is 48 possible / 47 on the clean path.

**MINOR-7 — the integrity comparison is against the staged path, not the
promoted bytes.** `G-ARTIFACT-INTEGRITY` reads `tmps[i][0]`; `os.replace` then
promotes that *file*. In the delivered source there is no statement between the
two, so the window is empty — but W5 shows the invariant is positional rather
than structural. *Fix:* promote from the verified string (write, verify,
re-write the verified bytes to the temp, replace), or re-read the promoted path
and exit non-zero on mismatch.

**MINOR-8 — §11's "the one place" is contradicted by the unit's own registry.**
§11: *"the field the weights live in is DECLARED-BY-THE-PIN and flagged
verdict-determining … the one place this unit's negative rows depend on a
declaration rather than on the arena."* The `fibre` registry flags **five** rows
verdict-determining, and one of them is `THE-NAMED-TARGETS`
(`DECLARED-AND-DISCLOSED`, fibre `UNBOUNDED`, 6 instances built) — the very
declaration the negative rows `UNREACHABLE-BY-*` are relative to. *Fix:* "the
one place the arena's own combinatorics is not what decides" or name both.

**MINOR-9 — the witness denominator is the search denominator, not the
witness's.** §5.2 says *"at denominator 100000 the error is below 1/10^4"*; the
published witness is `101275/100000`, which reduces to `4051/4000`. The receipt
publishes numerator and denominator separately so nothing is hidden, and the
bound is exact and tight (I recomputed: $6.631\times10^{-5}$, below $10^{-4}$
and not below $10^{-5}$). Wording only.

---

## 7. WHAT I COULD NOT BREAK

- **Byte reproducibility (#91).** Two off-tree, git-less delivery runs at
  `PYTHONHASHSEED` 0 and 99991 produced artifacts byte-identical to the
  committed `9299f80db2d8` / `f0617d1687a0`. A bare copy of the instrument in an
  empty directory refuses at a **named gate** with exit 1 and no traceback —
  PER-R's uncaught-traceback minor is fixed here.
- **The mutant sweep.** 49 of 49 dead at their declared target gates, out of
  harness, one process each, with `artifacts unchanged True` on every run and
  the mirror byte-identical before and after.
- **`--selftest` and `--no-write` write nothing.** Proved by an independently
  computed whole-subtree hash over `v14/` (`1f429a15b6bb0122` before and after
  both). Selftest is fatal at all three anchor classes.
- **Hostile argv.** 12 of 12 malformed forms exit 2 — unknown flag, short flag,
  `--flag=value`, missing `--mutant` argument (arity), `--mutant --quiet`
  (flag-as-name), trailing positional, and every combination with a good flag.
  6 of 6 legitimate forms behave as documented.
- **The seal at value-close.** 36 objects, each taken at the gate that vouches
  its own values, manifest total against the payload (`unsealed` empty), and
  `MUT-SEAL` (an object edited after its gate closed) dead on target.
- **The multi-way outcome selector's control arms.** `G-HEAD-LAW-REACHABILITY`
  hands the one head law four synthetic censuses inside the delivery run and
  requires all four pre-registered outcomes to be emitted, by both laws, as four
  *distinct* strings. I read both laws: genuinely different branch structure
  (`if all(...)` vs `len([...]) == 0`), no shared format string, and the second
  recomputes its own ordering from `GRAINS`. `MUT-REACHABILITY` (collapse the
  probes) and `MUT-HEAD` (type the head) both dead on target.
- **The verdict comparator.** `reconstruct_verdict` reads only the serialized
  receipt (`json.loads(json.dumps(...))`) and re-renders every segment from the
  primitive tables. `MUT-VERDICT-COMPARATOR` dead on target; W4 (forging the
  verdict at the disk boundary) dies at `G-ARTIFACT-INTEGRITY`.
- **E-22 fences by multiset.** Deleting the single fence, duplicating it, and
  perturbing a numeral inside it all die. `MUT-VERDICT-TWIN` dead on target.
- **E-22 quotations.** All 19 blockquotes lie inside pinned verbatim windows;
  inverting a quoted parent definition and forging a new blockquote both die.
- **E-24.** Six per-row `COUNTING-ONLY` stamps plus the header stamp
  `COUNTING-ONLY-E-24-NO-COUNT-BECOMES-A-PROBABILITY-WITHOUT-A-DECLARED-MEASURE`
  on `gibbs`; the three published expectations each carry
  `CONDITIONAL-ON-THE-DECLARED-WEIGHTS` and each is measured inside the
  observable's own $[0,4]$ range. No count is presented as a probability.
- **E-23.** 49 of 49 published tokens located in the source; 0 gate predicates
  reference `mut()`; 49 of 49 mutant targets are real call sites; the sweep is
  stamped `AN-EXTERNAL-BATTERY-RESULT-THE-DELIVERY-RUN-DOES-NOT-PRODUCE-IT`
  rather than implied.
- **The AST clause the unit adds.** No float literal, no banned import, and no
  call to `log`, `exp` or `sqrt` anywhere in 4,519 lines — I re-parsed and
  confirmed. `MUT-AST-BLIND` (a real float planted into the parsed text) dead on
  target. The pin's multiplicative framing is a property of the source.
- **Provenance layering.** Every real parent drift I could stage (deleted file,
  one byte appended, corrupted pin, edited verbatim window inside a parent) dies
  at `G-SOURCE-BYTES` before the finer anchors are consulted — defence in depth,
  with the finer gates reached by in-memory mutants as #34 requires.

---

## 8. THE SEAM RULING

**MAJOR-1, MAJOR-2, MAJOR-3 and MAJOR-4 are template diseases**, not ACT's own
inventions: MAJOR-1 is PER-R MAJOR-1 verbatim (headers rendered but unmatched),
MAJOR-2 is PER-R MAJOR-7's second clause relocated from the transcript to the
receipt's unsealed keys, MAJOR-3 is LOR MAJOR-4 / PER-R MAJOR-4 in its pure
form, and MAJOR-4 is the polarity-reach limit the corpus has not yet engraved.
**MAJOR-5 is ACT's own**, and it is the only finding that touches a pin wall by
name.

**No major puts a false measured number in the paper.** Every defect is a
binding that is claimed and absent; none is a computation that is wrong. The
three PER-R diseases this unit *repaired* — the honest denominator (47 of 47,
every omission named and covered), the closing-gates warrant (no false sealed
prose; the integrity gate raises before `os.replace`), and the transcript
whitelist (abolished in favour of full byte equality) — are repairs I verified
by injection, not by reading, and they are the reason this is an AWF and not a
REJECT.

**Candidate rulings until adjudication.** The headline physics of this unit —
ACT-FORM-RELATIVE, the grain-relative coupling count, the reduced-not-evaded
price, and the falsifier HIT — survived every check I could bring to it, and the
falsifier's mechanism (odd twists reverse the off-diagonal quartic sign; the
torus closes only at even twists) I re-derived by hand and confirm.

---

## 9. REPAIRS, LIFTABLE, IN PRIORITY ORDER

1. **R-ACT-2** (one line): `open(tmps[1][0]).read() == blob` in
   `G-ARTIFACT-INTEGRITY`, plus `MUT-DISK-UNSEALED`.
2. **R-ACT-1**: render every table's header row from the receipt at exactly one
   occurrence; add `MUT-TABLE-HEADER`.
3. **R-ACT-3**: a consumer-existence gate over `LD.ids` and a chain-verification
   gate, each with a mutant.
4. **R-ACT-4**: render §10's seven decided bullets and §13's five scope
   sentences as claims; extend `POLARITY`.
5. **R-ACT-5**: number-word coverage in the numeral scan; render the two spelled
   counts as claims; add `MUT-SPELLED-NUMERAL`.
6. Minors 1–9 as stated; MINOR-2 and MINOR-3 are one-line each.

---

**Review file:** `v14/review-act-instrument.md`.
**Executions:** 128. **Corruption events:** 93 (44 novel injections + 49
registry mutants). **Independent recomputations:** ≈ 265, zero disagreements.
**Repo writes by this seat:** 1.
