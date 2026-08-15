# EPR (PAPER-38) — K3 INSTRUMENT REVIEW

*Three-seat hostile panel, K3 INSTRUMENT seat. Object frozen at
`v14/paper-38-epr.md` 550e3c8fff93, `v14/code/epr_exact.py` 9ed817d9649d,
`v14/code/epr_output.txt` 1b30c6761281, `v14/code/epr_receipt.json`
a51326de11a8, pin `v14/note-epr-pin.md` b1e4cf9a8b9f. Authority:
HANDOFF-PROMPT.md §4/§9, RUNBOOK.md E-22/E-23/E-24, the #267 checklist.
All five digests verified at open AND at close (§8). Execution was
scratch-only, in rsync mirrors under
`.../scratchpad/epr_k3/`, absolute paths, per-run trees deleted, peak
under 5 G. This file is the seat's SOLE repository write.*

**Between delivery and adjudication every finding here is a CANDIDATE
READING.**

---

## GRADE: AWF — ACCEPT WITH FIXES

**No measured quantity is wrong.** Every structural and census number I
could re-derive independently — from first principles, without the
instrument's code — reproduces exactly: 27 cells, the 27-pair bijection,
six cells per actor, the link-graph theorem at 72 of 72 ordered site
pairs, the 512-subset census (490 / 19 / 0), 5,184 concatenations, 5,856
histories, 105,408 link-disjoint pairs, 421,656 block pairs, 316,224 and
1,265,112 certified, 18 and 54 at the record's own localization, and both
E4 fibre distributions summing to their pair counts. The
AST-frozen-predicate digest **f791c8dc0877** re-derives byte-for-byte,
per predicate and combined. All twenty-four published counts check
against live registries with zero mismatches. The 30-falsifier sweep is
**30/30 on target, one fresh process and one fresh tree each, artifacts
byte-unchanged, no staging residue**. Byte ×2 reproduces off-tree,
git-less, at two hash seeds, from artifact-deleted trees. The selftest
writes nothing by whole-tree hash. The argv whitelist holds 12/12.

**The defects are all perimeter, and most are template-shaped.** Seven
majors. Four of them are the diseases the corpus already named at #267
and #269 — full-table rendering, containment-versus-multiset, full
transcript integrity, falsifier-description honesty — recurring here in
new clothes. The three that are EPR-specific are worse than routine
because they land on this unit's *mandatory* wall: the Bell desiderata
table is ungated, the Bell wall is a seven-string blacklist defeated by
re-voicing, and the paper may delete its own wall sentence and pass.

The head — `EPR-CRITERION-INAPPLICABLE-AT-THE-PAIR-LOCALIZED-BLOCK-QUANTITY`,
second word `EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE` — is, as far as this
seat can measure, correctly derived and correctly scoped. What is not
earned is the paper's §12 account of its own guards. Five sentences there
claim protection the instrument does not provide.

**Counts.** 100 instrument executions; 239 independent recomputations; 47
corruption injections plus 16 hostile-argv forms; 30/30 falsifier sweep;
7 MAJOR, 10 MINOR; zero false measured numbers.

---

## 1. MAJORS

### MAJOR-1 — The §9 Bell desiderata table is not rendered. The unit's wall table is ungated.

`paper_render` builds **four** tables (T-ARMS, T-CONTROLS, T-REDUCTIONS,
T-READINGS). The paper carries **five**. The unrendered one is the §9
table at lines 351–358 — desideratum × D-RECORD × D-SHADOW ×
Bell-constrained — the table that carries this unit's Bell obligations.
It is measured into the receipt at `R["bell"]["desiderata"]` and then
never matched against the paper's bytes.

The paper's §12 says: *"Every table above is rendered from the receipt
with its headers included, so a header swap that leaves every number
correct dies at a gate."* That sentence is false for one table in five.

Establishing injections, all **exit 0, gates all PASS**:

| tag | injection | result |
|---|---|---|
| P1b | §9 headers swapped: `D-RECORD` ↔ `D-SHADOW` | PASSED |
| P1c | E1 row inverted: D-RECORD `not met`, D-SHADOW `met on the measured arms` | PASSED |
| P1d | both `Bell-constrained` `yes` flags (E3, E6) flipped to `no` | PASSED |

P1a — the same header swap on the *rendered* §5 table — dies correctly at
`G-PAPER-TABLES-WITH-HEADERS`, which is what shows the gate works and
simply does not cover this table.

E-22 ("tables render as claims") is violated on the one table where the
wall lives.

**Repair.** Add a fifth entry to `paper_render`'s `tables` list built from
`R["bell"]["desiderata"]`, with the paper's own lower-case cell text
rendered from the receipt rows (the receipt currently stores `"MET on the
measured arms"` where the paper prints `met on the measured arms`; render
one and match it, do not type both).

---

### MAJOR-2 — The three verdict fences are never matched against the receipt. Six head forgeries pass.

`FENCE_RE` (line 2610) is used at exactly one site, line 2818, and its
output feeds only a numeral count (`in_fenced_blocks: 50`). The receipt
carries `R["verdict"]["segment_1"]`, `segment_2`, `segment_3`; each
appears **twice** in the paper (lines 15–25 and 477–487); **no gate
compares them.** The only thing standing between the fence and a forger
is `G-PAPER-NUMERAL-COVERAGE`, which asks only that each numeral appear
somewhere in the run's registry — so any swap between two registered
values is invisible, and any change to a *word* is invisible outright.

Establishing injections, all **exit 0**, all applied to **both** copies:

| tag | injection into the verdict fences | result |
|---|---|---|
| P2a | `SECOND-WORD=EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE-…` → `…RECORD-INCOMPLETE-…` | PASSED |
| P2b | `E5-RECORD-MOVES=0-OF-105,408` → `105,408-OF-105,408` | PASSED |
| P2c | `LOC-PAIR-x-SEP-LINK-DISJOINT=EPR-CRITERION-INAPPLICABLE-…` → `=EPR-BOTH-COMPLETE-…` | PASSED |
| P2g | `SUBSETS-WITH-BOTH=0` → `SUBSETS-WITH-BOTH=512` | PASSED |
| P2i | `PREMISE-AT-THE-RECORD-LOCALIZATION=0` → `=105,408` | PASSED |
| P2h | `;NO-LOCAL-REALISM-CLAIM` deleted from both fences | PASSED |

P2h is the sharpest: the head's own no-local-realism stamp can be struck
out of both published verdict blocks and the run promotes clean.

E-22's multiset rule is not implemented anywhere in this instrument. The
fences are not containment-gated either — they are **not gated at all**.

**Repair.** Render `segment_1..3` as claims and gate the fenced blocks by
**multiset equality** against the receipt's segments: `Counter(canon(b) for
b in FENCE_RE.findall(paper_text)) == Counter({canon(seg): 2 for seg in
segments})`. Containment is what E-22 was bought to forbid.

---

### MAJOR-3 — Claims are containment-gated; five of sixteen are duplicated and their twins are forgeable.

`G-PAPER-CLAIMS` asks `canon(txt) not in hay` — presence, not count.
Five claims occur **twice** in the paper: C02, C04, C05, C07, C08.
Forging one copy leaves the other to satisfy the gate. This is verbatim
the disease E-22 was bought for ("the clean copy satisfied a containment
gate while its twin was forged"), reappearing on the claims leg.

Establishing injections, all **exit 0**:

| tag | injection | forged text now in the paper |
|---|---|---|
| P9e | C02 twin, in "The short of it" | `512 of 512 subsets … own a record quantity and a conditioning region sharing no link with them` |
| T-C04 | C04 twin, in "The short of it" | `… 18 carry a record quantity at the block, and 18 carry both` |
| T-C07 | C07 twin, §4 | `the corpus carries 36 distinct records and the shadow can separate at most 36 of them` |
| T-C05 | C05 twin, §3 | `in the state's own localization the same predicates return 0 instances of the premise` |

P9e is the worst of these: it plants the **exact inverse of the head
finding** into the paper's own summary paragraph, and
`G-SENTENCE-REFERENT-BINDING` waves it through because `512` and `512`
both live in the SUBSETS universe.

Singleton claims are properly guarded — P2e and P2f (forging C09's
"carries 0 of them" and C10's "certifies 0 elements") both die at
`G-PAPER-CLAIMS`, which is what shows the gate itself is sound.

**Repair.** Count occurrences: require `hay.count(canon(txt))` to equal a
per-claim declared multiplicity, and publish the multiplicities. Same fix
serves MAJOR-2.

---

### MAJOR-4 — Falsifier descriptions are never matched against behaviour. A description-inverted falsifier passes.

The paper's §12 says: *"30 falsifiers are declared, each naming the gate
it must die at and each carrying a hook located in the instrument by AST
and matched against the statement that describes it, so a
description-inverted falsifier cannot pass."*

`hook_carriers()` matches the **carrier function name** and nothing else:
`ok = all(any(w == g for g in got) for w in want)`. The statement string
is never consulted. A description-inverted falsifier passes trivially.

Establishing injection **C/descinv**, exit 0: two published descriptions
inverted in place —
`"link-disjointness is granted to every pair"` → `"link-disjointness is
REFUSED to every pair"` and `"the certainty predicate is made constantly
true"` → `"…constantly FALSE, so no element is ever certified"` — clean
run, `description mismatches none`.

Separately, and already true of the shipped object: **MUT-REFERENT's
published description does not describe its code.** The description says
*"a fraction is left without a common referent universe"*; the code
(line 2873) is `if mut("MUT-REFERENT"): fbad.append("planted")` — a
direct append to the failure list that never constructs a fraction and
never exercises the universe lookup. The gate's real machinery is
demonstrated only by this seat's P9a/P9b/P9d, not by its own falsifier.
That is E-23's "false waiver wearing a green badge" one step removed.

**Repair.** Either drop the §12 sentence, or implement it: keep a small
per-falsifier expectation (a gate-evidence substring or a signed
direction) and check the mutant run's evidence against the description.
And re-cut MUT-REFERENT so it plants an actual unbound fraction into
`paper_text`, the way MUT-PAPER-NUMERAL and MUT-BELL-PLANT do.

---

### MAJOR-5 — THE ACT DISEASE, both forms, live.

**(a) Post-snapshot key ADD.** `G-SEAL-TOTALITY` computes
`published = sorted(k for k in R if k not in DECLARED_UNSEALED)` when it
runs, and nothing re-checks `R` afterwards. A key inserted between that
gate and `json.dumps` is published unsealed, unlisted and undetected.

Injection **A1**, exit 0, promoted:
`R["headline_summary"] = {"verdict": "EPR-BOTH-COMPLETE", "certified":
316224}` — a fabricated headline contradicting the unit's own head,
sitting in the receipt with no seal and no declaration.

**(b) Declared-unsealed forgery.** `DECLARED_UNSEALED` names four keys
that are never sealed and never re-derived. Two of them are testimony.

- Injection **A3**, exit 0: `R["arithmetic"]` rewritten to
  `"float64 throughout; numpy used for the census"` — promoted. The
  receipt now testifies against its own exactness while
  `G-NO-FLOAT-IN-SOURCE` still passes, because that gate scans the source
  and this key is prose.
- Injection **A4**, exit 0: `DECLARED_UNSEALED` grown by one name and a
  fresh forged key published under it.

**(c) A seal may name a gate that never ran** — and the shipped receipt
already does. `SEALED_PATHS`' last row is
`("SEAL-TRANSCRIPT", "transcript_head", "G-TRANSCRIPT-SEALED-WHOLE")`,
but the gate that runs is named `G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT`.
**`G-TRANSCRIPT-SEALED-WHOLE` does not exist in this instrument.** One of
39 published seals claims provenance from a phantom gate, and no gate
validates `sealed_at_gate`. Injection **A5** confirms the general case:
re-pointing SEAL-VERDICT at `G-A-GATE-THAT-NEVER-RAN` runs clean at exit 0.

Sealed-key *edits* are caught — injection **A2** (editing
`R["verdict"]["head"]` after sealing) dies correctly at
`G-ARTIFACT-INTEGRITY` via `SEAL.close`. The hole is additions and the
unsealed list, not mutations.

**Repair.** Move the `published`/`unsealed` computation to immediately
before `SEAL.close`, or recompute and compare `set(R)` at close against
the set seen at G-SEAL-TOTALITY. Seal `arithmetic` and `python` (they are
vouching, and #119 says seal what you vouch). Validate every
`sealed_at_gate` against the ledger's gate names, and fix
`G-TRANSCRIPT-SEALED-WHOLE` → `G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT`.

---

### MAJOR-6 — Transcript integrity is nominal: the "gate-time seal" is recomputed at promotion.

In `finish()`, after `SEAL.close`:

```
text   = "\n".join(LINES) + "\n"
seal_t = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
```

`seal_t` is a hash of the **live** `LINES` taken at promotion time, not a
digest sealed at gate time. The staged bytes are written from the same
`text`. The comparison therefore cannot fail on content — it proves only
that the file write round-tripped. The genuine gate-time digest,
`R["transcript_head"]["sha256_12"]` (sealed as SEAL-TRANSCRIPT), is never
compared with the promoted bytes, although its own note in the receipt
says *"the whole transcript's own digest is compared with the staged
bytes at G-ARTIFACT-INTEGRITY."* And `G-ARTIFACT-INTEGRITY`'s statement
claims the staged bytes are compared with *"the digests of the objects
sealed at gate time."*

Establishing injections, all **exit 0, promoted**:

| tag | injection | result |
|---|---|---|
| X1 | `[PASS] G-LOCAL-REALISM-RESTORED` appended to `LINES` **after** the transcript seal | promoted into `epr_output.txt` |
| X2 | `[PASS] G-BELL-EVASION-CERTIFIED` injected **before** the seal | promoted; digest agrees, since the seal is taken over the forged text |
| X3 | `Ledger.gate` made to print `[PASS]` unconditionally | clean run (no gate fails), and nothing cross-checks the printed word against `passed` |

X1 is the LOR M5 finding recurring: a forged staged line promoted beside
a byte-perfect receipt. There is no gate asserting that every
`[PASS] G-…` line in the transcript corresponds to a ledger row with
`passed: true`, nor that the number of such lines equals
`len(LD.rows)`.

**Repair.** Compare the promoted transcript's **prefix** against
`transcript_head/sha256_12` (the first `lines_at_the_seal` lines), and add
a gate that parses `[PASS]/[FAIL] G-…` out of the finished transcript and
requires exact multiset agreement with the ledger's `(gate, passed)` rows
plus the four declared post-snapshot gates.

---

### MAJOR-7 — The Bell wall is a seven-string blacklist with no positive leg.

The pin makes the wall **mandatory**: *"no sentence may claim local
realism or Bell evasion."* The implementation is
`hits = [s for s in BANNED if canon(s) in hay]` over seven fixed strings.

Establishing injections, all **exit 0**:

| tag | sentence planted / removed | result |
|---|---|---|
| B1 | `On the measured arms this restores local realism.` | PASSED — the blacklist holds `"local realism is restored"`, not the active voice |
| B3 | `The Bell theorem does not apply to this corpus, and the record is a local hidden variable.` | PASSED |
| B5 | the paper's **own** wall sentence deleted (`ISP cannot satisfy Bell local causality … It is Bell-nonlocal`) | PASSED |

B5 is the structural one. The wall has no positive requirement: nothing
obliges the paper to *state* the standing verdict. The two anchors that
carry it, A-BELL-E1 and A-BELL-E2, are matched in **v5 paper-14's** bytes,
never in this paper's — so a paper-38 that silently drops its Bell
section passes every gate.

B2 (the exact banned string `local realism is restored`) dies correctly at
`G-WALLS-SCAN-THE-PAPER`, so the gate fires; it is the surface that is
thin.

**Repair.** Add a positive leg: require A-BELL-E1 and A-BELL-E2 to be
matched **in paper-38's own bytes** (they already are present at lines
346–349, so this costs nothing today and forbids their deletion
tomorrow). Broaden BANNED to voice-normalised patterns — regex over
`restor\w+ local realism`, `local realism .{0,20}restor`, `evad\w+ Bell`,
`Bell .{0,20}evad`, `local hidden.variable` — and publish the patterns,
not just the seven literals.

---

## 2. MINORS

**MINOR-1 — the coverage census is blind to 5 of the 40 gates
(DISCLOSED DEFECT, STILL PRESENT).** `closing_battery` builds
`ran = [g["gate"] for g in LD.rows] + list(DECLARED_LATE_GATES)` = 35, but
40 gates run. The five it never sees are `G-FALSIFIER-COVERAGE`,
`G-FALSIFIER-REACHABILITY`, `G-READS-DECLARED`,
`G-SWEEP-IS-EXECUTION-BOUND`, `G-CLOSING-BATTERY-RAN`. Each has a waiver
written in the source dict, but because `uncovered` is drawn from `ran`,
those waivers are never published: **14 waiver entries exist in source, 7
are emitted, 7 are dead.** On the published surface, 28 gates have a
falsifier and 7 have a waiver — 35 of 40 — leaving five gates with
neither, which is exactly E-23's unguarded row. *Fix: build `ran` from
`{g["gate"] for g in LD.rows} | set(DECLARED_LATE_GATES) |
set(POST_SNAPSHOT_GATES)` after the ledger is complete, or move the census
into `finish()`.*

**MINOR-2 — the declared-late check is vacuous for the four closing
gates.** `allran = {g["gate"] for g in LD.rows} | set(POST_SNAPSHOT_GATES)`
unions in the very set it then tests membership against, so
`late += [g for g in DECLARED_LATE_GATES if g not in allran]` can never
fire for `G-TRANSCRIPT-SEALED-AT-THE-SNAPSHOT`, `G-RECEIPT-IS-EXACT`,
`G-SEAL-TOTALITY` or `G-ARTIFACT-INTEGRITY`. *Fix: drop the union.*

**MINOR-3 — `data_shadow` is frozen but never exercised.**
`PREDICATE_NAMES` has twelve entries and all twelve are located, digested
and published; `predicate_totality` exercises **eleven**. `data_shadow`
appears in no probe. The gate says *"every predicate is then exercised on
every argument combination of a declared probe set"*; the 210 probes cover
11/12. *Fix: add `data_shadow(row, region, psi_site)` to the subset ×
testrow loop; the probe count becomes 210 + 30.*

**MINOR-4 — the spelled-numeral scan covers only a 26-word map.**
`words = [w for w in re.findall(r"[a-z]+", …) if w in WORDNUM]` collects
only known words, so an unknown spelled numeral is not scanned at all.
Injection **P8a** (`The census ran at forty-two pairs across ninety
blocks.`) passes at exit 0. And a mapped word with a wrong referent passes
whenever its value happens to be registered somewhere else: **P8b**
(`nineteen histories`), **P8c** (`thirty declared readings`), **P8d**
(`Eleven windows are declared`), **P8e** (`Thirteen banned sentences`) all
pass. The gate claims *"spelled numerals included; anything outside the
run's registry … fails."* Also `WORDNUM["thirty_six"]` is unreachable —
`[a-z]+` never yields an underscore. *Fix: extend the map through the
tens and hundreds and fail on any `[a-z]+` token in a declared
number-word shape that is not in the map.*

**MINOR-5 — a typed spelled numeral in the sealed surface, wrong.**
`G-PAPER-CLAIMS`' statement reads *"Fifteen claims, each built out of
receipt values rather than typed"* while its own evidence field on the
same row reads `claims 16`. The gate statement is sealed and published
and contradicts its own measurement. (Companion, source-only: the
SECTION 2 comment says *"Seven committed files are read as SOURCES"*
against `len(SOURCES) == 6`.) This is #267 M3's typed-count disease in
miniature. *Fix: interpolate `%d` from `len(claims)`, as
`G-FALSIFIER-COVERAGE` already does for its falsifier count.*

**MINOR-6 — rendered tables are containment-gated too.** The gate checks
that every rendered header and row is present; it never checks that the
paper's tables contain nothing else. Injection **P1e** appends a
fabricated fifth row to the §5 census table
(`| LOC-WALK | SEP-LINK-DISJOINT | 105,408 | 316,224 | 316,224 | 0 |
EPR-BOTH-COMPLETE |`) — exit 0. Injection **P1f** appends a fabricated row
to the §7 readings table — exit 0. Both fabrications use only registered
numerals, so the numeral gate is silent. *Fix: multiset equality over the
paper's table rows, per table.*

**MINOR-7 — referent binding checks membership, not truth.** Injection
**P9c** (`The shadow separates 36 of 36 records.`) passes: both members
are in the RECORDS universe. This is honest to the gate's own statement,
but §12's *"every fraction is resolved against the receipt"* reads
stronger than what is done. Cross-universe pairings are genuinely caught
— **P9a** (`36 of 512`), **P9b** (`105,408 of 5,856`) and **P9d** (a
cross-universe fraction planted *inside* a fence) all die at
`G-SENTENCE-REFERENT-BINDING`. *Fix: soften the §12 sentence, or require
the numerator to be ≤ the denominator within the universe and the pair to
appear as an actual receipt (value, bound) pair.*

**MINOR-8 — TOCTOU between read-back and `os.replace`.** Injections
**S2** and **S3** corrupt the staged receipt / transcript after the
read-back comparison and before promotion; both promote corrupted bytes
at exit 0. This requires editing the instrument, so it is not a live hole,
but `G-ARTIFACT-INTEGRITY`'s *"and only then does os.replace promote
them"* is doing less work than it sounds. *Fix: re-read and re-compare
after `os.replace`, on the promoted paths.*

**MINOR-9 — `PAPER_LITERALS` overlaps measured quantities.** The 43
declared structural literals include `19`, `20`, `21`, `22`, `23`, `24`,
`27`, `32`–`35`, `38` and `47` — tokens that are simultaneously runbook
/ paper identifiers and measured values in this unit (19 far-nonempty
subsets, 27 cells, 22 table rows, 23 READ-RECORD-MENU cells). A forgery
using one of those is whitelisted twice over. *Fix: scope the literal
allow-list to the contexts that need it (a `#NN` or `paper-NN` or year
shape) rather than the bare token.* **Note the good news:** `NUMREG`
itself is clean — `reg()`'s string branch admits **zero** non-numeric
tokens in this run, so #267 M6's digest-token whitelist is **ABSENT** here.

**MINOR-10 — anchor `consumed_by` is decorative (see PROBE 6).** Carried
as a minor rather than a major because the anchors themselves are all
genuinely matched in their sources' bytes and above the #62 floor; what is
absent is any binding between the anchor and the gate it names.

---

## 3. THE NINE PROBES — PRESENT / ABSENT

| # | probe | verdict | evidence |
|---|---|---|---|
| 1 | header swaps + fabricated table rows | **PRESENT** | §9 Bell table entirely unrendered: header swap (P1b), inverted E1 row (P1c), both Bell-constrained flags flipped (P1d) — all exit 0. Fabricated rows appended to rendered tables also pass (P1e, P1f). Control: P1a dies at `G-PAPER-TABLES-WITH-HEADERS`. → MAJOR-1, MINOR-6 |
| 2 | direction flips | **PRESENT** | In the verdict fences: `RECORD-COMPLETE`→`RECORD-INCOMPLETE` (P2a), `0-OF-105,408`→`105,408-OF-105,408` (P2b), head word→`EPR-BOTH-COMPLETE` (P2c), `SUBSETS-WITH-BOTH=0`→`512` (P2g), premise `0`→`105,408` (P2i) — all exit 0. **E3 horns swapped in §7 prose (P2d) — exit 0.** `certifies 0`→`certifies all` is **caught** on the singleton claims C09/C10 (P2e, P2f die at `G-PAPER-CLAIMS`) but **not** on duplicated claims (P9e, T-C04, T-C05, T-C07). → MAJOR-2, MAJOR-3 |
| 3 | THE ACT DISEASE, both forms | **PRESENT** | Post-seal key ADD promoted (A1); declared-unsealed forgery of `arithmetic` promoted (A3); unsealed-list growth promoted (A4); phantom `sealed_at_gate` accepted (A5) — **and already shipped**: SEAL-TRANSCRIPT names `G-TRANSCRIPT-SEALED-WHOLE`, a gate that does not exist. Post-seal EDIT of a sealed key **is** caught (A2). → MAJOR-5 |
| 4 | THE BELL WALL | **PRESENT** | `On the measured arms this restores local realism.` passes (B1). Bell-evasion paraphrase passes (B3). The paper's own wall sentence can be deleted (B5). A licensed-looking sentence with wrong counts (B4) died — but at `G-SENTENCE-REFERENT-BINDING`, on the fraction, **not** on the counts; with an in-universe fraction it would have passed. Control: exact banned string dies (B2). → MAJOR-7 |
| 5 | transcript integrity incl. forged PASS lines | **PRESENT** | Forged `[PASS]` line after the seal is promoted (X1); before the seal is promoted (X2); unconditional `[PASS]` printing is uncross-checked (X3). The "gate-time seal" `seal_t` is recomputed at promotion. → MAJOR-6 |
| 6 | phantom consumers | **PRESENT** | `consumed_by` is written at line 548 and **never read again** — one occurrence in 3,511 lines. Rewriting all 14 anchors' consumer gates to a single unrelated gate (`G-NO-FLOAT-IN-SOURCE`) runs clean at exit 0; rewriting them to `G-A-GATE-THAT-DOES-NOT-EXIST` also runs clean at exit 0. Confirmed by inspection: `G-BELL-DESIDERATA-BOUND` (named consumer of A-BELL-E1, A-BELL-E2, A-E6) tests only `len(des) == 6` and the constrained count, and never touches the anchor text. The POT hole is here: **the anchors are matched, but nothing they are matched for consumes them.** → MINOR-10 |
| 7 | read-back before `os.replace`; staging cleanup on refusal | **ABSENT (clean)** | `MUT-INTEGRITY` in the write path fires `G-ARTIFACT-INTEGRITY`, exit 1, artifacts byte-unchanged, staging removed. All 30 sweep rows leave no `.tmp` residue. The one-bit-flip control rejects. TOCTOU after the comparison is MINOR-8, not this probe. |
| 8 | spelled numerals | **PRESENT** | Unmapped spelled numerals unscanned (P8a: `forty-two`, `ninety`). Mapped-but-wrong values pass on registry collision (P8b/c/d/e). A wrong spelled numeral sits in the shipped sealed surface today: `G-PAPER-CLAIMS` states "Fifteen claims" against evidence `claims 16`. → MINOR-4, MINOR-5 |
| 9 | referent binding across the census's universes | **PARTLY ABSENT (mostly clean)** | Cross-universe pairings are genuinely caught, including inside a fenced block: 512-subset ↔ 421,656-pair (P9a) and 105,408-pair ↔ 5,856-history (P9b, P9d) all die at `G-SENTENCE-REFERENT-BINDING`. What is **not** caught is an in-universe falsehood (P9c) — MINOR-7 — and a cross-universe forgery written with hyphens or uppercase `OF`, which `NOF_RE` (`([\d,]+)\s+of\s+([\d,]+)`) does not match; every fence uses exactly that shape (`0-OF-105,408`). |

---

## 4. THE STANDING DISCIPLINES

**E-22 (inline spans; blocks by multiset) — VIOLATED.** Inline code spans
*are* scanned for numerals (the registry sees all 220, 50 of them fenced).
But there is no multiset gate on fenced blocks anywhere in the
instrument; the three verdict fences appear twice each and are matched
zero times (MAJOR-2). Tables do not all render as claims (MAJOR-1), and
those that do are containment-gated (MINOR-6), as are duplicated claims
(MAJOR-3).

**E-23 (falsifier honesty) — VIOLATED on two legs.** All 30 published
descriptions were read against their code sites. Twenty-nine are
substantively honest — the ones that flip a counter or a flag say so
("is reported as", "is asserted", "is declared"). **MUT-REFERENT is not**:
its description promises a planted fraction and its code appends a
sentinel to the failure list. And the *check* that would catch such a
thing does not exist: `hook_carriers` matches function names only, so an
inverted description passes (MAJOR-4). On the coverage leg, five gates
carry neither a published falsifier nor a published waiver (MINOR-1).

**E-24 (measure-relativity) — SATISFIED.** `measure_relativity/stamp`
reads `COUNTING-ONLY: no count in this unit is a probability, and no
fraction is a frequency (E-24)`; `certainty/window` carries the same
stamp; §11 of the paper repeats it; all six windows are declared with
their bounds and the complete one says it is complete. No fraction in the
paper is presented as a frequency. The one place a measure enters —
"probability equal to unity" — is rendered measure-free and then checked
against two declared full-support measures in both directions at 1,080
probes, 1,080 agreements.

**#82 CLI contract — SATISFIED.** Twelve hostile argv forms all exit 2
(`--sweepx`, `-x`, bare `--mutant`, `--mutant=NOPE`, `--mutant NOPE`,
`--quiet --bogus`, `--list-gates --oops`, `--selftest --sweep`,
`--SWEEP`, doubled `--mutant=`, bare `--`, `--quiet=1`), a positional
argument exits 2, and the clean forms exit 0. `--selftest` corrupts A-E2,
dies at `G-VERBATIM-ANCHORS-IN-SOURCE`, and **writes nothing verified by
whole-tree hash** (`15de24fd0c93` before and after) — and again with the
artifacts deleted (`a0a97adcdc12` before and after; it does not recreate
them).

**#91 no moving refs / off-tree / git-less — SATISFIED.** Two seeds
(`PYTHONHASHSEED` 0 and 31337), each in a tree with **no `.git` anywhere
at or above the run root**, `PATH=/nonexistent` so the `git` binary is
genuinely unavailable, and **both artifacts deleted before the run**:
both reproduce `a51326de11a8` / `1b30c6761281` exactly. No subprocess is
invoked. The abstention from the drifted FAC receipt is provable at the
I/O layer — `read_set` records 7 reads and FAC is not among them.

**#34 reachability — SATISFIED.** 30/30 falsifiers reached and died at
their declared gates, one fresh process and one fresh tree each, run
outside the instrument's own `--sweep` harness. All six pre-registered
outcome words are emitted by the real head law on declared data,
including `EPR-BOTH-COMPLETE` and `EPR-RECORD-ALSO-INCOMPLETE` on
synthetic descriptions and `EPR-SHADOW-INCOMPLETE-RECORD-COMPLETE` on a
synthetic one-direction arena where the premise exists at 35,136
instances — which is what makes the head's arena-relativity a measurement
rather than an assertion.

---

## 5. THE 30-FALSIFIER SWEEP, OUT OF HARNESS

One fresh process and one fresh 50 MB tree per falsifier, `--mutant NAME`,
artifacts hashed on disk afterwards, staging inspected, tree deleted.

**30 declared, 30 executed, 30 died at their declared gate, 0 off target,
30/30 artifacts byte-unchanged (`a51326de11a8` / `1b30c6761281`), 0
staging residue.**

Every gate that a falsifier targets fires on its own object. The
description-honesty leg is MAJOR-4 and the coverage leg is MINOR-1; the
*execution* leg is clean.

---

## 6. RE-PROBE OF THE TWO DISCLOSED DEFECTS

**MUT-INTEGRITY reachability — NOT REPRODUCIBLE; the defect is closed.**
Forced on in the real promoting path (`write=True`, not the sweep's dry
run), it fires:

```
[FAIL] G-ARTIFACT-INTEGRITY :: receipt staged eed695177a21 seal a51326de11a8;
transcript staged 1b30c6761281 seal 1b30c6761281;
one-bit-flip control rejects True; promoted False
```

exit 1, artifacts byte-unchanged, staging removed. Reachable in both the
dry and the promoting path.

**Coverage census seeing late gates — STILL PRESENT.** 40 gates run; the
census counts 35; five are invisible to it; 7 of the 14 source waiver
entries are never published. Carried as MINOR-1 with the exact repair.

---

## 7. WHAT THE SEAT COULD NOT FAULT

Recorded because the negative results are part of the finding:

- **No false measured number anywhere.** 239 recomputations, including
  full first-principles rebuilds of the arena, the carrier, the
  512-subset lattice and the block-pair census, none using the
  instrument's code. The one apparent anomaly — 1,265,112 ≠ 3 × 421,656
  — resolves **exactly**: 421,632 singleton-block pairs at 3 quantities
  plus 24 line-block pairs at 9 gives 1,265,112, and 5,856 × 72 + 4 × 6
  gives 421,656. The `18` at LOC-PAIR × SEP-ACTOR-DISJOINT is likewise
  exactly 3 histories × 6 ordered pairs, three and not four because the
  ANT line owns no cell — which is the unit's own theorem applied to its
  own count.
- **The AST-frozen-predicate digest re-derives.** All twelve per-predicate
  sha256-12s and the combined **f791c8dc0877** reproduce from an
  independent AST walk. The 210 probe count reproduces by hand
  (72 + 18 + 90 + 30).
- **All 24 published counts verified from live registries, zero
  mismatches**: 40 gates (36 + 4), 39 seals (35 at the snapshot), 30
  falsifiers, 14 anchors, 12 predicates, 210 probes, 6 windows, 16
  claims, 4 tables, 5 polarity axes, 6 referent universes, 6 sources, 7
  banned sentences, 1,080 measure probes, 6 control arms, 5 readings, 8
  class words.
- **The head is genuinely derived twice** and the routes agree on every
  count of every arm and on every arm word; the head word is required to
  lie in the vocabulary parsed from the pin's bytes, and
  `MUT-OUTCOME-TYPED` proves the parse is load-bearing.
- **The gates that exist, work.** P1a, P2e, P2f, P9a, P9b, P9d, B2 and A2
  all die at the right gate on the right object. Nothing here is a
  green badge over a broken predicate — the failures are of *coverage*,
  not of *correctness*.
- **The E5 test-declaration duty is genuinely discharged**: `MUT-E5-LEAK`
  routes the reading index into both `record_at_B_under` and
  `shadow_at_B_under` and dies at `G-E5-RECORD-DOES-NOT-MOVE`, so the
  zero at 105,408 probes is a measurement and not a blind spot.
- **The scope stamps are honest.** COUNTING-ONLY throughout, kinematic
  separation named as kinematic and explicitly not spacelike, FAC and SEC
  carried as candidate-under-repair in-paper, the drifted parent cited
  rather than read with the abstention provable at the I/O layer, and the
  site-constancy the whole census rests on disclosed as a property of the
  window rather than a law.

---

## 8. DIGESTS RE-VERIFIED AT CLOSE

| object | sha256-12 | at open | at close |
|---|---|---|---|
| `v14/paper-38-epr.md` | 550e3c8fff93 | ✓ | ✓ |
| `v14/code/epr_exact.py` | 9ed817d9649d | ✓ | ✓ |
| `v14/code/epr_output.txt` | 1b30c6761281 | ✓ | ✓ |
| `v14/code/epr_receipt.json` | a51326de11a8 | ✓ | ✓ |
| `v14/note-epr-pin.md` | b1e4cf9a8b9f | ✓ | ✓ |

All five unchanged. No repository file was modified by this seat except
this review.

---

## 9. RECOMMENDATION

**AWF.** The measurement stands; the perimeter needs eight repairs, in
this order:

1. Render the §9 Bell table and gate it (MAJOR-1).
2. Render the three verdict fences and gate fenced blocks by **multiset**
   (MAJOR-2).
3. Gate claims and table rows by **occurrence count**, not containment
   (MAJOR-3, MINOR-6).
4. Give the Bell wall a positive leg and voice-normalised patterns
   (MAJOR-7).
5. Close the post-snapshot key window; seal `arithmetic` and `python`;
   validate `sealed_at_gate`; fix `G-TRANSCRIPT-SEALED-WHOLE` (MAJOR-5).
6. Compare the promoted transcript's prefix against the sealed digest and
   add a `[PASS]`-line-versus-ledger multiset gate (MAJOR-6).
7. Either implement or withdraw the §12 sentence about
   description-matched falsifier hooks, and re-cut MUT-REFERENT
   (MAJOR-4).
8. Fix the coverage census's `ran` set, add `data_shadow` to the totality
   probes, derive "Fifteen claims" from `len(claims)`, and extend the
   spelled-numeral map (MINOR-1, -3, -5, -4).

**Four of the seven majors are TEMPLATE-SHAPED, not EPR-shaped** —
MAJOR-1 (full-table rendering), MAJOR-3 (containment vs multiset),
MAJOR-4 (falsifier-description honesty) and MAJOR-6 (full transcript
integrity) are the four diseases the corpus named at #267 and swept at
#269, recurring in a unit built after that sweep. MAJOR-2 is E-22's own
founding disease, unimplemented. This seat recommends the orchestrator
treat the fence-multiset and claim-occurrence gates as **corpus-wide
template repairs**, not paper-38 repairs, and re-sweep the siblings built
on the same template.

**Every headline in this review is a candidate reading until
adjudication.**
