# ARITY-16 (paper-50) — K3 INSTRUMENT-SEAT REVIEW (FROZEN)

**Seat:** K3, the INSTRUMENT seat (a two-continuation seat — the first
predecessor was killed by a session limit mid-harness, v15/LOG.md #54; the
second by the weekly limit with its campaign essentially done, v15/LOG.md
#59; this continuation re-verified its scratch and finished the last five
results). **Jurisdiction:** whether `v15/code/arity16_exact.py`'s gates
actually catch what they claim, under live hostile injection, in off-tree
mirrors only. **Method:** a git-less `rsync` mirror (`.git` / `__pycache__`
excluded) at the seat scratch `a16_k3b/`. The repository was read-only to
this seat except this one review file. Every injection edited a hardlinked
mirror copy only (atomic-replace so the frozen snapshot is never touched),
ran one process, was scored for death gate + rc + whole-tree hash, and the
committed snapshot held its whole-tree hash `467c225ac202e614` throughout.
Only this seat's own PIDs were signalled; sibling scratches (`a16_k1b`,
`a16_k2b`) were never touched.

**Continuation reconciliation.** The predecessor's scratch (31 injection
logs, tsv score rows, mirrors) was adopted only after verification: every
log exists, every tsv row's gate name matches its own `.err` REFUSED line,
and every survivor's promoted artifact was re-opened and its contradiction
re-read from disk. Three of its claimed kills were **re-run from the
injected mirrors by this continuation** — K3-01 (`G-PAPER-CLAIMS`, tree
`928b42f85b4dd4bb` unchanged), K3-10 (`G-PAPER-CLAIMS`, tree
`83eb67dab1885873` unchanged), K3-22 (`T-SEAL-PROMOTION`, rc 1, tree
unchanged) — all identical to the predecessor's rows: the harness was
honest. The five results the predecessor never saw (K3-24, K3-25, K3-27,
K3-28, TAMPER — their processes finished after its death) were scored fresh,
and the two in-process proofs (the F-2 wall proof and the five-recipe
move-proof) plus `--selftest` and the two-seed mutant determinism probe were
re-executed by this continuation.

## UNIT UNDER REVIEW (digests verified at open, and again at close — unchanged)

| file | committed sha256-12 | verified |
|---|---|---|
| v15/paper-50-arity16.md | c86ea5edcfec | yes |
| v15/code/arity16_exact.py | 613e05fc7ff0 | yes |
| v15/code/arity16_output.txt | 837333a85fcb | yes |
| v15/code/arity16_receipt.json | 52f600389933 | yes |
| v15/note-arity16-pin.md (pin) | 1dac6a35ddc5 | yes |

Pinned sources recomputed live and matched: `0d677a4cbe97` (paper-44),
`e90a41eed544` (arity_receipt), `e2293b8c3858` (paper-39), `29216cea946f`
(ndep_receipt). Committed ledger head `630f7508679f5550`. A clean baseline
write-run in the mirror reproduced the committed receipt `52f600389933c64f`
and output `837333a85fcbd1b1` **byte-for-byte** and left the whole tree at
`467c225ac202e614`.

---

## VERDICT: ACCEPT-WITH-FIXES

**The measurement, head, seal, wall and determinism CORE is sound, and it is
measurably stronger than its parent ARITY's** (this seat could move no
delivered receipt number; the three structural ARITY findings — a
set-membership verdict comparator, a discarded falsifier-coverage result, and
a post-`os.replace` seal window — are all closed here: the head is a
positional comparator with independent resolvers, `G-FALSIFIERS` forces its
own coverage, and the sealed-key edit window is caught *before* any write.
The two ECC-registered wall escapes E-4/E-5 are **cured** at this arena).

**Every forged table cell, every forged registered-claim numeral, every
flipped head/table word, every direction flip, the sealed-key edit window,
the six registry mutants, the on-disk receipt tamper, the builtin-hash ban,
the whole 10-form hostile CLI, and clean cross-seed reproduction all behave
exactly as claimed.** No delivered number, no verdict token, no fence, and no
*sealed committed* receipt value could be moved without a gate firing.

The FIXES qualifier rests on four coverage gaps in the vouching layer (none
moves a committed sealed value, none appears in the committed paper — all
are hostile transplants):

1. **F-1 — prose-restatement coverage (MEDIUM; RECURRENCE of ECC F-1/F-2).**
   A prose sentence that restates a receipt-backed finding but is (a) not a
   registered `CL.claim`, and (b) carries no coverage-visible false numeral —
   because it has no numeral, or its integers are all in-universe, or it is a
   slash-rational the numeral regex splits — is neither claim-bound nor
   coverage-caught nor referent-caught, so it promotes and the receipt is
   regenerated to bless the forged paper. Four transplants survived at rc 0
   (K3-06, K3-13, K3-18, K3-21), each producing a paper whose prose
   contradicts its own verdict fence/receipt.
2. **F-2 — licence-leak-across-heading (MEDIUM; NEW disease).** The semantic
   walls' sentence splitter does not treat a markdown heading (which lacks
   terminal punctuation) as a sentence boundary, so a **licence token inside a
   heading laundries a policed claim placed as the first body sentence of that
   section** — for any of the ten walls. Demonstrated against the unit's
   flagship new wall: a reading-merge placed under the §9 heading "…the
   division-forcing thesis, which splits on the reading" (whose tail
   "splits on the reading" is a `W-NO-READING-MERGE` licence) promotes clean
   (K3-17b), although the identical sentence in isolation is caught.
3. **F-3 — unsealed-key edit window (LOW; self-detecting).** In the main()
   window between `run_measurements` and `promote`, `promote`'s seal check
   re-verifies only *sealed* keys; the declared-unsealed `ledger_head`, the
   `ledger` rows and the transcript's narrative digest lines are not
   re-derived, so a forged head (K3-23), a forged ledger row (K3-25) and a
   dropped object-under-test digest line (K3-24) all promote — but the
   published rows/chain remain recomputable, so every one of the three
   forgeries is detected by any chain recomputation. The published integrity
   *summary* is forgeable; the source of truth is not.
4. **F-4 — determinism policing is call-level only (LOW–MEDIUM; NEW).**
   `G-HASH-BAN` bans `hash`/`id` *calls*; nothing polices set/dict-iteration
   order or `os.listdir` order reaching the receipt. K3-27 (a set-iteration
   probe into the receipt's cache block) and K3-28 (raw `os.listdir` into the
   **sealed** totals) both promote at rc 0, and the K3-27 mutant was proven
   **hash-seed-variant**: under `PYTHONHASHSEED=0` vs `12345` the promoted
   receipts differ in `cache.probe_order` — seed-dependent content can be
   promoted, and even *sealed*, in an artifact whose premise is byte-identical
   off-tree reproduction (the clean unit is seed-invariant: `--render`
   byte-identical across both seeds, `7681fe3e4b7d0a2e`).

None is a false theorem; none moves a committed sealed value or a verdict
token; all are paper-surface, self-detecting, or require editing the code
itself. F-1 is a recurrence; F-2/F-3/F-4 are registered below for TPL-2.
Fixing the four lifts the unit to ACCEPT.

---

## THE INJECTION TABLE

Legend: **tree** is the whole-tree sha256-16 of the mirror after the run,
compared to the pre-run hash (INTACT = write-nothing; CHANGED = the run
promoted, rewriting paper+receipt+output). "caught" = died at a gate with
tree INTACT; "SURVIVED" = promoted at rc 0.

### (1) Forged values

| # | injection | site | expected | observed (gate, rc) | tree | verdict |
|---|---|---|---|---|---|---|
| K3-01 | lattice count 7→8 | readings table | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught (re-run: identical) |
| K3-02 | lattice count 67→66 | §1 prose (registered claim) | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-03 | saturation-selects-2 → 4 | §11 prose (registered claim) | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-04 | modulus rung set 2,4,9 → 2,4,8 | §8 prose (registered claim) | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-05 | DP total 2627625 → 2627626 | §3 prose | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| **K3-06** | **transport tally 3/3 → 4/2** | **§12 synthesis prose** | (coverage) | **NONE, rc 0** | **CHANGED** | **SURVIVED — F-1** |
| K3-07 | certified floor 10 → 9 | crystallization table | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-08 | obstruction column 4 → 3 @a=5 | sec-2 table | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-09 | fidelity 505920 → 505921 | §5 prose | G-PAPER-COVERAGE | G-PAPER-COVERAGE, rc 1 | INTACT | caught |

### (2) Flipped words

| # | injection | site | observed | tree | verdict |
|---|---|---|---|---|---|
| K3-10 | A16-CONDITIONAL-READING-DEPENDENT → -TRACKS-THE-FIELD | verdict head | G-PAPER-CLAIMS, rc 1 | INTACT | caught (re-run: identical) |
| K3-11 | A16-MODULUS-THEOREM-HOLDS → -FALSIFIED-AT-AG(2,4) | verdict head | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-12 | LAW-IN-A ↔ BREAKS (division-forcing) | statement table | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| **K3-13** | **"published as capped, never as empty" → "…as empty"** | **§8 prose** | **NONE, rc 0** | **CHANGED** | **SURVIVED — F-1** |
| K3-14 | idle-arity "refused" → "0/0/0 holds" | forcing table | G-PAPER-CLAIMS, rc 1 | INTACT | caught |

### (3) Reading-merge

| # | injection | site | observed | tree | verdict |
|---|---|---|---|---|---|
| K3-15 | merged-tally sentence ("the two readings agree…") | appended prose | G-PAPER-POLARITY, rc 1 | INTACT | caught |
| K3-16 | abstract 35 moved into the linear-window claim | §9 registered claim | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| K3-17 | A16-FORCING-READING-SPLIT → -FORCING-SPLIT | verdict head | G-PAPER-CLAIMS, rc 1 | INTACT | caught |
| **K3-17b** | **reading-merge as §9's first body sentence** | **§9 prose (under the licence-bearing heading)** | **NONE, rc 0** | **CHANGED** | **SURVIVED — F-2** |

### (4) The four ECC-panel species

| # | species | observed | tree | verdict |
|---|---|---|---|---|
| **K3-18** | prose slash-rational forge (6/35, true 5/35) | **NONE, rc 0** | **CHANGED** | **SURVIVED — ECC F-1 reproduces (REGISTERED-AT-ECC)** |
| K3-19 | "No reader will doubt that … is selected" | G-WALLS / W-NO-SELECTION, rc 1 | INTACT | **caught — ECC E-4 CURED** |
| K3-20 | ", being gated, … is selected" | G-WALLS / W-NO-SELECTION, rc 1 | INTACT | **caught — ECC E-5 CURED** |
| K3-20b | ", being a candidate, … is selected" | G-WALLS / W-NO-SELECTION, rc 1 | INTACT | caught (this-wall licence token) |
| K3-20c | long-wedge ", being … at this arena, is selected" | G-WALLS / W-NO-SELECTION, rc 1 | INTACT | caught (hard negative) |
| **K3-21** | bare "The event size is derived here." | **NONE, rc 0** | **CHANGED** | **SURVIVED — ECC F-2 reproduces (REGISTERED-AT-ECC)** |

### (5) Seal / integrity

| # | injection | expected | observed | tree | verdict |
|---|---|---|---|---|---|
| K3-22 | post-final-gate payload edit (sealed `substrate`) | seal catch before write | T-SEAL-PROMOTION ("sealed values moved: ['substrate']"), rc 1 | INTACT | caught (pre-write; re-run: identical) |
| **K3-23** | ledger-head forge → 0000000000000000 | (unsealed) | NONE, rc 0 — promoted receipt carries head `0000000000000000` | CHANGED | **SURVIVED — F-3 (self-detecting)** |
| **K3-24** | object-under-test + ledger-head transcript lines dropped | (narrative, un-policed) | NONE, rc 0 — transcript digest moves to `d1cb4d8b09cffd33`, no gate | CHANGED | **SURVIVED — F-3 (self-detecting)** |
| **K3-25** | ledger row 5 evidence forged after G-CLOSE (unsealed) | (unsealed) | NONE, rc 0 — receipt row 5 reads `{"forged": true}` under the intact head `630f7508679f5550` | CHANGED | **SURVIVED — F-3 (chain recomputation detects)** |
| TAMPER | on-disk receipt tamper (307→308 + head→0000), then a write run | receipt is a pure output, regenerated | run twice (predecessor + this continuation, rc 0 captured on the second): regenerated receipt + output **byte-identical to committed** (`52f600389933c64f` / `837333a85fcbd1b1`); tree returns from the tampered state (`7e7f985c0315bfb0`, then `565ffa9e41d03c72`) to `467c225ac202e614` both times | RESTORED | clean — tamper erased |

### (6) Determinism

| # | injection | expected | observed | tree | verdict |
|---|---|---|---|---|---|
| K3-26 | builtin `hash("probe")` at module level | G-HASH-BAN | G-HASH-BAN ("calls_in_module":["hash"]), rc 1 | INTACT | caught (rehearsal claim verified) |
| **K3-27** | set-iteration order → receipt (cache block) | (no iteration-order gate) | NONE, rc 0 — `cache.probe_order` promoted in hash order; ledger head moves | CHANGED | **SURVIVED — F-4** |
| **K3-28** | `os.listdir` order → sealed totals | (no iteration-order gate) | NONE, rc 0 — raw directory order promoted inside `SEAL.seal("totals", …)` | CHANGED | **SURVIVED — F-4** |
| SEED | clean `--render` at PYTHONHASHSEED 0 vs 12345 | byte-identical | identical (`7681fe3e4b7d0a2e`) | INTACT | clean determinism holds |
| SEED-MUT | K3-27 mutant, write run at PYTHONHASHSEED 0 vs 12345 | (if F-4 real: divergence) | both promote at rc 0 with **different receipts**: `probe_order` `theta,gamma,beta,delta,eta,zeta,epsilon,alpha` vs `gamma,alpha,eta,zeta,theta,beta,delta,epsilon`; promoted ledger heads `44b9e71411b9058e` vs `b3212037e5d3d4ef` (the predecessor's un-seeded run had a third order) | CHANGED | **seed-variant content promoted — F-4 proven** |

### (7) Harness honesty

| probe | result |
|---|---|
| MUT-FIDELITY | died at **G-CONSTRUCTOR-FIDELITY**, artifacts unchanged |
| MUT-MENU | died at **G-LAW3-MENU16**, artifacts unchanged |
| MUT-THEOREM | died at **G-MODULUS-THEOREM**, artifacts unchanged |
| MUT-HEAD | died at **G-VERDICT-EQUALITY**, artifacts unchanged |
| MUT-SEAL-EDIT | died at **G-SEAL-TOTALITY**, artifacts unchanged |
| MUT-HASH | died at **G-HASH-BAN**, artifacts unchanged |
| (whole MUT mirror tree after all six) | `467c225ac202e614` — INTACT |
| `--selftest` (re-run by this continuation) | refused at **G-VERBATIM**, artifacts unchanged: True, rc 0, whole-tree INTACT `467c225ac202e614` — the write-nothing sweep is real |
| recipe move-proof (re-run in-process by this continuation) | MUT-ARENA→G-ARENA16, MUT-READING→G-READINGS, MUT-DISAGREE→G-CONDITIONAL, MUT-HEAD→G-VERDICT-EQUALITY, MUT-SEC2-THEOREM→G-LAW6-SEC2-16: every `apply()` target moves under its flag — the poisons are real |

### (8) CLI — 10 hostile argv forms, each rc 2, tree INTACT `467c225ac202e614`

`--frobnicate` · `--mutant` (no name) · `--mutant NOSUCH-MUTANT` ·
`--mutant MUT-HEAD --selftest` · `--run --render` · `--verify-paper` (no path) ·
`--verify-paper /etc/hosts` (outside repo) · `--mutant … --mutant …` (twice) ·
`--verify-paper <a directory>` · `--verify-paper <missing>.md` — all
`CLI ERROR`/`rc 2`, nothing written.

---

## SURVIVORS / FINDINGS (detail)

Nine survivors total: four F-1 (one REGISTERED-AT-ECC ×2), one F-2 (NEW),
three F-3 (self-detecting), two F-4 probes proven by one seed divergence
(NEW). Every survivor's promoted artifact was re-opened from disk by this
continuation and its contradiction confirmed.

### F-1 — prose-restatement coverage (MEDIUM; recurrence — 2 NEW variants + 2 REGISTERED-AT-ECC)

Four transplants promoted at rc 0, each rewriting paper+receipt+output:

- **K3-06 (NEW variant)** replaced §12's "the primary linear tally is 3
  transporting against 3 breaking" with "4 transporting against 2" —
  collapsing the paper's own headline reading-split result to the parent's
  anchored tally. The promoted paper's §12 prose reads 4/2 while its verdict
  **fence** still reads "THE PRIMARY F4-LINEAR STATEMENT TALLY READS 3
  LAW-IN-A AND 3 BREAKS" and the **receipt** `transport/linear/
  statement_words` still reads `{LAW-IN-A: 3, BREAKS: 3}` (re-read from the
  promoted mirror by this continuation). `G-PAPER-CLAIMS`, `-COVERAGE`,
  `-REFERENTS` all PASS.
- **K3-13 (NEW variant)** replaced §8's honesty stamp "published as capped,
  never as empty" with "published as empty", while the SCOPE fence still says
  "EVERY CAPPED ROW SAYS SO". All five paper gates PASS.
- **K3-18 (REGISTERED-AT-ECC)** planted "The linear share is 6/35…" (the true
  share is 5/35). The numeral scanner `(?<![\w.])(\d[\d,]*)(?!\.\d)(?!\w)`
  splits `6/35` into `6` and `35`, each independently in the receipt-number
  set, so `G-PAPER-COVERAGE` PASSES and the atomic rational is never checked.
  ECC's F-1 disease reproducing verbatim.
- **K3-21 (REGISTERED-AT-ECC)** planted the bare "The event size is derived
  here." — `W-NO-SELECTION` polices `select/forc/determin…` for the
  event-size subject but not `deriv`, and `W-NO-RECONSTRUCTION-AS-DERIVATION`
  polices `deriv` but its subject requires `recover/reconstruct/identifiab`,
  so the event-size subject slips between the two walls. ECC's F-2 disease
  reproducing.

Mechanism, common to all four: the prose leg binds only the registered
`CL.claim` sentences and case-folded fence/table renders; a synthesis
sentence that is not registered escapes it, and the referent leg is
membership-only (a swap among in-universe integers is invisible). The receipt
is regenerated to certify whatever the forged paper says. The measurement
layer is untouched — the receipt's own numbers stay correct — so the damage is
an internally-contradictory *published* paper, not a moved measurement.

### F-2 — licence-leak-across-heading (MEDIUM; NEW)

`SemanticWall` canonicalises the paper (`canon`, folding all whitespace incl.
newlines) and its licence leg splits sentences on `(?<=[.!?])\s+`. A markdown
heading has no terminal `.?!`, so it fuses with the first sentence of its
section body. Section 9's heading ends "…the division-forcing thesis, **which
splits on the reading**", and `\bsplits? on the reading\b` is a declared
**licence** of `W-NO-READING-MERGE`. A merge claim placed as §9's first body
sentence therefore inherits that licence and is excused (K3-17b promoted at
rc 0). In-process proof, re-executed against the live wall object by this
continuation:

| sentence | `scan` result |
|---|---|
| "…both readings and either reading give the same answer" (isolated) | `unlicensed` non-empty → **caught** |
| "…either reading **gives** the same answer" (isolated) | hard negative `either reading gives the same` fires → **caught** |
| "…splits on the reading  …both readings…give the same answer" (heading fused) | `violations=[]  unlicensed=[]` → **ESCAPES** |
| "The two readings agree once the census is read correctly." | hard negative fires → **caught** |

The escape defeats the unit's flagship pin-mandated wall at its single most
natural injection site (§9 is the reading-split section). It is bounded — it
needs adjacency to a licence-bearing heading, and the wall catches the same
sentence anywhere else — but it is a genuine wall bypass, distinct from ECC's
E-5 (which laundered with an *in-sentence* token). The hard-negative leg is
not heading-defeatable (hard negatives are not licence-excused); the soft
licence leg is the general defence against paraphrases, and it is the one the
heading defeats — for all ten walls.

### F-3 — unsealed-key edit window (LOW; self-detecting; three routes)

`promote`'s `SEAL.verify_at_promotion` re-verifies sealed keys (so K3-22's
edit of the sealed `substrate` dies at `T-SEAL-PROMOTION` *before* any
`os.replace` — the ARITY post-write seal window is closed here). But the
declared-unsealed integrity summary is not re-derived at promotion, and all
three of its legs are forgeable by a code edit in the
run_measurements→promote window:

- **K3-23**: `ledger_head` forged to `0000000000000000` promotes; the 43
  published rows remain self-consistent and recompute to the true
  `630f7508679f5550`, so any chain recomputation exposes the forged summary.
- **K3-25**: ledger **row** 5's evidence forged to `{"forged": true}` under
  the untouched head promotes; the chained head no longer matches the rows,
  so `Ledger.recompute_chain` detects it.
- **K3-24**: the transcript's two narrative self-identification lines
  ("object under test … c86ea5edcfec", "ledger head …") are dropped and the
  run promotes — the transcript digest moves (`d1cb4d8b09cffd33`) but no gate
  polices the narrative lines' presence.

In all three routes the published integrity *summary* disagrees with its own
recomputable substance: forgeable presentation, intact source of truth.

### F-4 — determinism policing is call-level only (LOW–MEDIUM; NEW; proven seed-variant)

`G-HASH-BAN` polices `hash`/`id` **calls** (K3-26 died exactly there, and
MUT-HASH dies at its declared gate) and the clean unit is genuinely
seed-invariant (`--render` byte-identical across `PYTHONHASHSEED` 0 and
12345, digest `7681fe3e4b7d0a2e`). But nothing polices *iteration order*
reaching the receipt:

- **K3-27**: a set-comprehension `probe_order` inserted into the receipt's
  cache block promotes at rc 0 — and this continuation ran the same mutant
  under `PYTHONHASHSEED=0` and `=12345`: the two promoted receipts carry
  **different** `probe_order` sequences (three distinct orders across three
  runs), and because the cache block is chained into the ledger the promoted
  **ledger heads differ too** (`44b9e71411b9058e` vs `b3212037e5d3d4ef`).
  Seed-dependent bytes promoted into the artifact of a unit whose premise is
  byte-identical reproduction.
- **K3-28**: raw `os.listdir` order inserted into the **sealed** `totals`
  promotes at rc 0 — the seal happily seals environment-dependent content
  (filesystem enumeration order is platform-contingent by contract).

The falsifier discipline is call-site policing; the disease is data-flow. It
requires a code edit (same attacker model as the seal-window probes the
registry does police), and the clean unit is currently deterministic — hence
LOW–MEDIUM, not HIGH.

---

## NEW-DISEASE REGISTRATIONS FOR TPL-2

- **LICENCE-LEAK-ACROSS-HEADING (F-2, NEW).** The semantic-wall sentence
  splitter treats a period-less markdown heading as part of the following
  sentence, so a wall licence token (or, symmetrically, a subject/policed
  token) inside a heading changes the scope verdict of the first body
  sentence — for every wall. Fix: split on heading boundaries (a line
  matching `^#+\s`) as well as on `.?!`, or strip heading lines before the
  wall scan. Demonstrated to launder a `W-NO-READING-MERGE` violation under
  the §9 heading.
- **UNSEALED-KEY PROMOTION WINDOW (F-3, NEW at this arena; three routes).**
  Recompute and re-bind the unsealed self-verifying keys *inside* `promote`
  after the seal check: `ledger_head` from the rows (kills K3-23), the row
  chain itself (kills K3-25), and the transcript's mandatory narrative digest
  lines (kills K3-24) — so a forged summary cannot be promoted even though it
  is detectable downstream.
- **ITERATION-ORDER DETERMINISM (F-4, NEW).** Extend the determinism
  discipline past `hash`/`id` call-sites to data-flow: any set/dict-iteration
  or `os.listdir` order reaching the receipt must be sorted or refused —
  proven live by a seed-divergent promoted receipt (K3-27 under two
  `PYTHONHASHSEED` values) and a sealed raw directory enumeration (K3-28).
- **PROSE-RESTATEMENT COVERAGE (F-1)** is already ECC-registered
  (slash-rational + bare-derivation); this unit shows it recurs and extends to
  in-universe numeral swaps (K3-06) and epistemic-word flips (K3-13) in
  unregistered synthesis prose. Widen the claim registry to bind every
  receipt-restating sentence, or add an atomic-rational + tally-sentence leg.
- **Cross-seat confirmation (K2's HYPHEN-EVASION, registered at K2, not
  double-counted here).** This seat confirmed it at the wall-object level:
  `W-NO-SELECTION.scan("The event-size is uniquely selected …")` returns no
  violation and no unlicensed sentence, while the spaced form is caught by
  both legs — the space-keyed subject/policed regexes are hyphen-blind. One
  canonicalisation fix (fold intra-word hyphens in `canon`) serves both
  registrations.

---

## SEAT SUMMARY (one paragraph)

As the INSTRUMENT seat (completed across three sessions, the predecessor's
campaign re-verified log-by-log and its last five results finished and scored
fresh) I ran 31 live off-tree injections plus a 10-form hostile CLI battery,
a six-mutant registry battery, a five-recipe in-process move-proof, the
`--selftest` write-nothing sweep, a two-seed clean-determinism proof, a
two-seed *mutant* determinism proof, and an on-disk receipt-tamper
regeneration test — each against a hardlinked mirror anchored to the
committed whole-tree hash `467c225ac202e614`, touching no sibling scratch and
signalling only my own PIDs; three of the predecessor's claimed kills were
re-run and reproduced identically, confirming the harness honest. The
instrument's core does what it claims and is stronger than its parent ARITY:
forged table cells, forged registered-claim numerals, flipped head and table
words, and direction flips die at `G-PAPER-CLAIMS`/`-COVERAGE`/`-POLARITY`;
the six registry mutants die at their exact declared gates with the tree
byte-unchanged; the head is a positional comparator (`MUT-HEAD` →
`G-VERDICT-EQUALITY`); the sealed-key promotion edit is caught *before* any
write (`T-SEAL-PROMOTION`, closing ARITY's post-`os.replace` window); an
on-disk receipt tamper is erased by regeneration byte-identical to the
committed artifact; the two ECC-registered wall escapes E-4/E-5 are cured
here; clean delivery is byte-identical across hash seeds. The nine surviving
escapes are all in the paper-surface / summary / code-edit layer and none
moves a committed sealed value: a **prose-restatement coverage** gap (F-1, an
ECC recurrence — a forged tally, an inverted honesty stamp, a
slash-rational, and a bare "derived here" each promote into a paper that
contradicts its own fence/receipt), a **new licence-leak-across-heading**
disease that defeats the pin's flagship `W-NO-READING-MERGE` at its natural
§9 site (F-2), a **self-detecting unsealed-key promotion window** with three
routes (F-3: head, row, transcript line), and a **call-level-only determinism
discipline** proven seed-variant on a mutated mirror (F-4). Grade
**ACCEPT-WITH-FIXES**: no false theorem, no delivered/sealed committed number
moved, seal-head-wall-determinism core intact; closing the four gaps lifts
the unit to ACCEPT.
