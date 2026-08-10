# U4b instrument review (K3)

**Object.** paper `2bcba873d78e`, code `2c9b999dea31`, output `8715c46a7b7f`,
receipt `c4a4e8223b64`, at commit `8c2dd98`; pin `d2cff9a274a8`. All five
verified byte-identical at the start and at the end of this review. HEAD moved
`a43748b` → `1aeeef0` while I worked (the other two panel seats freezing);
no commit in that range touches any of the five. Concurrent-worker edits to
`giter_exact.py`, `r5_gauge_exact.py`, `paper-16` are disclaimed and unrelated.

**Grade: AWF** (accept with fixes).

**Effort.** 62 program executions; ~500 independent recomputations and checks;
**zero disagreements with any published number**. Every headline in the paper
was rebuilt from my own code and reproduced exactly. Every finding below is
instrument-lens: none of them moves a number, and none of them is a false
theorem.

---

## 1. What held

**F1 — #91, at my own hands.** I built a mirror containing only the twelve
files the program can reach, in a directory tree with **no `.git` anywhere**,
and ran the delivery with `PYTHONHASHSEED` unset (random per process). Exit 0;
**both artifacts byte-identical to the committed ones** — output
`8715c46a7b7f`, receipt `c4a4e8223b64`, confirmed by `cmp` as well as by
digest. A CPython audit hook over the complete run recorded **314 `open`
events, 18 distinct in-repo paths** (the 10 pinned sources, the file itself,
the paper under test, and its own six outputs/probes/tmps), **2 `os.remove`,
2 `os.rename`, and zero `subprocess` / `exec` / `fork` / `socket` events of any
kind**. No `git`. The claim in §12 is true as written.

**F2 — cited-not-read, verified twice.** AST: no string literal naming
`paper-14`, `u4_crystals_*`, `paper-13` or `w2_census_*` appears anywhere in
the file; the only U4 references are the **adjudication** (`fa991e19ae54`) and
the **effectus review** (`61fb7d9e8471`), both hash-pinned sources. Runtime:
neither commit's files is ever opened (F1's trace). And all ten pinned sources
are byte-identical **at `8c2dd98`, at HEAD, and in the working tree** — no
moving ref, so the pins were correct at construction and still are. The two
un-read commits are registered in `DECLARED_COMMITS` with the reason, and the
claims the paper makes about them check out against git: `paper-14` and
`u4_crystals_*` exist at `06b89fe`; `w2_census_exact.py` has a `SEC 6 — THE
CRYSTAL ARENAS AND THE GENERIC WALK` at `58195da`.

**F3 — the three READ anchors are real reads.** `d66_arbitration_crystal_exact.out`
line 102 carries `GRID(g=3,R=4) n= 66 arbs= 12 … deliveries= 18`, and the
`R=6` row `102 / 18 / 30`; `review-u4-effectus.md` line 263 carries
`| CONFLICT-GRID(3,2) | 1 | 1 | 0 | 1 | 1 | −1 | **0** |`. All three are
regex-parsed out of the pinned texts at run time and compared against the
driven constructor. Not typed. (One disclosure, below at m9: the regex reads
`|q_12| = 1` where the source prints `−1`.)

**F4 — #62.** 10 verbatim anchors, **minimum 57 characters** against a declared
floor of 40, every one found in its pinned source after the declared fold, and
every one naming a consumer that **is** a real gate in the receipt. 10/10.

**F5 — #87 on the measurement gates.** `G-STAB-ROUTES` (7,056 objects, three
routes sharing no code — translation, Z[ω] Fourier annihilator, subgroup
lattice — agreeing element for element), `G-DRIVEN-EQUALS-COMBINATORIAL`
(11,664 objects), `G-FOOTPRINT-CONSTANT` (11,664), `G-FRAGILITY` (12 edits at
each of 540 crystalline window schedules, exceptions collected per schedule),
`G-STRATA-WITNESSED` (20 witnesses, each `maxhits == 1`, no refusal),
`G-CONSTRUCTIBILITY` (11,664, per-object) — all universally quantified over
per-object computations. No aggregate stands in for an object anywhere in the
measurement layer. `G-POSDEF-EMPTY` and `G-I7-STRICT-EMPTY` likewise rest on
exhaustive per-pair, per-site exact-Fraction evaluation.

**F6 — the falsification battery.** `--selftest` exits 1, writes nothing, and
prints the demonstration. K3 asked for other anchors: `--break-anchor` drives
**all ten** to FAIL — each dies at its own `G-PROV[…]`, exit 1, nothing
written. 10/10.

**F7 — the mutant suite, replicated independently.** My own driver, my own
bookkeeping, on a scratch mirror carrying the committed artifacts: **31 of 31
killed, 31 of 31 on target, zero survivors**, and the artifacts byte-unchanged
before and after (`8715c46a7b7f` / `c4a4e8223b64`). Row for row — mutant,
declared target, killing gate — my sweep agrees with the receipt on all 31.

**F8 — the three-way sweep.** 49/49 gate **statements** and 49/49 **evidence**
strings appear verbatim in the transcript; all 15 published claims render in
the paper under the declared ASCII fold; 17/17 headline counts appear in all
three artifacts. Zero drift.

**F9 — independent recomputation, my code, no shared line.** 280 partitions;
78,400 pairs; **747** non-degenerate at all nine sites; posdef max **3**;
strictly-positive **0**; homogeneous **9**; uniform-negative **261**; mixed
**486**; det values `{-1: 855, -1/4: 5238, 1: 108, 3/4: 522}`; 7,056 seed pairs
splitting **6912 / 36 / 108**; crystalline **216 / 36 / 0 = 252**; ×8100 =
**1,749,600 / 291,600 / 0 = 2,041,200**; beyond-coset rate **exactly 1/32** over
**55,987,200**; the four period directions each 63 times. Also 9!/(3!³·3!) = 280,
(280·27)² = 57,153,600, (4·27)² = 11,664, 11,664/57,153,600 = 1/4900. Every
published number reproduced.

**F10 — the seal mechanism itself is sound.** Three of eight injections were
caught, each naming the exact broken row, each writing nothing or refusing to
move the artifacts. `MUT-SEAL-BROKEN` is on target. The write path is
genuinely careful: a deliberately corrupted probe is written and its detection
*measured* before either artifact moves; both files go out as `.tmp` and are
verified against the gate-time seal before `os.replace`; then re-read from disk
and verified again.

**F11 — the gate-count prediction closes.** `totals["gates"]` is predicted
mid-run as `len(LD.rows) + 6` and required to close at `len(LD.rows) + 2`; a
drift exits 1. A real computed-not-typed self-check (#24).

---

## 2. The totality ruling, under the #148 addendum

**NOT TOTAL. Non-compliant on both clauses of the addendum.**

I censused all 23 published receipt keys against the 19-row seal manifest.

| status | keys |
|---|---|
| sealed at a gate | `affine` `anchors` `class_pairs` `constructibility` `counts` `determinant` `family` `fragility` `stabilizer` `strata` `verbatim_anchors` `verdict/{crystal,det,constructibility}` `waiver_ledger` `walls` |
| sealed **at the final gate** (#49 `G-PAPER-COVERAGE-FINAL`) | `gates` `totals` |
| sealed at the penultimate gate (#48) | `mutants` |
| **unsealed and not declared unsealed** | `schema` `paper` `provenance` `paper_claims` `paper_coverage` `paper_polarity` |

Clause 1 — *every published receipt key is sealed at gate time or explicitly
declared unsealed*: **six keys are neither.** There is no unsealed manifest in
the code at all; `grep -i unsealed` over the file returns nothing.

Clause 2 — *seals taken at the final gate are non-compliant*: `SEAL-GATES` and
`SEAL-TOTALS` are taken at gate 49, the last gate.

A third defect, handed to me by the operator (#151) and here **measured**:
`SEALS_IN_RUN` declares 16 in-run seals, but `SEAL-WAIVERS` is taken at gate 44
— three gates *after* `G-SEAL-COMPLETE` at gate 41, the gate whose statement is
"every one of those N in-run seals still verifies here". `Seal.verify` iterates
only *taken* rows filtered by `only=`, so an untaken seal is skipped rather
than broken. The gate's evidence discloses the mismatch (`seals: 15,
declared_in_run: 16`) but its predicate (`not broken`) never requires equality.

**Chronology, stated plainly.** The unit was born at #146; the totality
addendum was engraved at #148 out of R5. This is a retro-application and I rule
it as one: the failure is a **miss against a standard that did not yet exist**,
not a violation of the standard the unit was built to. Against #119 *as
engraved at v14 #119* — seal at gate time, write from the sealed payload,
compare disk bytes to the gate-time seal — the unit is **compliant on the
mechanism and on the write path**, and non-compliant only in that six published
rows were never treated as published rows. The ledger's "the seal caught a real
defect during construction" is corroborated: INJ01 shows the same mechanism
firing on the same class.

---

## 3. The injections

Eight injections, each one line of source in a scratch mirror, each a full
delivery run.

| # | injection | point | measured | verdict |
|---|---|---|---|---|
| INJ01 | `verdict/crystal` GENERIC→SEEDED | 1 stmt before `SEAL.close` | exit 1, **nothing written**, `GateFail … the payload was sealed over a broken seal :: ['SEAL-VERDICT-CRYSTAL']` | **CAUGHT** |
| INJ02 | six unsealed keys forged at once | 1 stmt before `SEAL.close` | **exit 0**, both artifacts written, **transcript BYTE-IDENTICAL to the committed one**, receipt publishes `provenance[A-PIN].ok=false / got="deadbeefcafe"`, `paper="v14/NOT-THE-PAPER.md"`, `schema="INJECTED-SCHEMA"`, `paper_claims[C01]="INJECTED-FALSE-CLAIM"`, `paper_coverage.missing=["INJECTED"]`, `paper_polarity[P1].ok=false` | **SEAM, 6 wide** |
| INJ03 | `totals.gates_passed=999`, `mutants_killed=99` | 1 stmt before `SEAL.take("SEAL-TOTALS")` | **exit 0**, both written, 999/99 published, and the transcript's own manifest publishes the **digest of the lie** (`3629822847d9`) | **SEAM** (final-gate seal) |
| INJ04 | `control_underspecified` replaced by `{candidates:1, prefix:0, initiator:"G22"}` | 1 stmt before `SEAL.take("SEAL-CONSTRUCTIBILITY")` | **exit 0**, both written; the receipt now says the under-specified control matched **one** candidate — i.e. FORCED — while the transcript in the same artifact set says "7 menu candidates match … so the fate is BRANCHING" | **SEAM** (control-row-under-label) |
| INJ05 | `"GARBAGE-NOT-JSON"` appended after `os.replace` | post-write | exit 1 with the correct message — but the corrupted, **non-parsing** receipt is **left on disk**; no rollback | **CAUGHT, not contained** |
| INJ06 | transcript `LINES` head flipped | 1 stmt before `close_transcript` | **exit 0**, **receipt byte-identical to the committed one**, transcript published reading `U4B-CRYSTAL-SEEDED` **everywhere** — the two published artifacts state opposite verdicts | **SEAM** (widest) |
| INJ07 | `SEAL.take("SEAL-WAIVERS")` deleted | — | **exit 0**, **receipt byte-identical**, transcript publishes `seals : 18 objects sealed at gate time` with 18 manifest rows, and `G-SEAL-COMPLETE`'s evidence is **byte-identical to the honest run's** (`{'seals': 15, 'declared_in_run': 16, 'broken': []}`) | **SEAM** (the operator's hand-off, measured) |
| INJ08 | `constructibility.fates.FORCED = 11663` | 1 stmt before `SEAL.close` | exit 1, nothing written, naming `SEAL-CONSTRUCTIBILITY` | **CAUGHT** |

**Playbook scores.** R4b post-gate head flip: **dead** on the sealed head
(INJ01), **alive** on the transcript (INJ06). Census-cell move: **dead** (INJ08).
Control-row-under-label: **alive** (INJ04). Count tampering: **alive** at the
final-gate seal (INJ03). Post-write corruption: **dead** at exit 0 — there is no
non-parsing receipt at exit 0 — but **alive at exit 1**, where the corrupt file
is left in place (INJ05).

### THE SEAM RULING

**Width: ten.** Six published receipt keys outside the seal and undeclared
(`schema`, `paper`, `provenance`, `paper_claims`, `paper_coverage`,
`paper_polarity`); three seals taken at the last two gates (`SEAL-MUTANTS` @48,
`SEAL-GATES` and `SEAL-TOTALS` @49); one declared in-run seal taken three gates
after the completeness gate that certifies it, and droppable without trace. The
**whole transcript** is an eleventh if counted as an object: it is sealed once,
at the end, from mutable state. **Five of the ten are exploitable at exit 0, and
I exploited all five** (INJ02 six-as-one, INJ03, INJ04, INJ06, INJ07).

**Character.** The seam is again **exactly the complement of a working seal** —
R5's sentence, with a different complement — and the complement is not random.
The unit seals **what it measured** and leaves unsealed **what it vouched for**:
`provenance` (its claim about its sources), the four `paper_*` keys (its claim
about its paper), and the transcript (its claim about itself). Everything the
census computed is sealed and every attempt on it died; everything the
instrument *certifies about something other than its own arithmetic* is open,
and every attempt on that succeeded at exit 0. That is the shape of the seam,
and it is the shape a reader should worry about most, because those are the
rows a reader cannot recompute.

The sharpest single fact: **INJ06 and INJ07 both leave the receipt byte-identical
to the committed one.** A reader who verifies the receipt's sha256 — the corpus's
normal check — cannot distinguish either forgery from the honest run.

---

## 4. Findings

### MAJOR

**MAJOR-1 — the totality gap is live at exit 0, six keys wide.**
Evidence: §2 census, INJ02. Paper §12's "every published object is digested at
the moment its gate passes" is false as written.
*Repair:* add `SEAL-PROVENANCE` @`G-PROV-ALL`, `SEAL-PAPER-CLAIMS`
@`G-PAPER-CLAIMS`, `SEAL-PAPER-POLARITY` @`G-PAPER-CLAIM-POLARITY`,
`SEAL-PAPER-COVERAGE` @`G-PAPER-COVERAGE-FINAL`; add a two-row declared-unsealed
manifest for `schema` and `paper` (both fixed before the first gate, both
constants); and add a closing gate `set(R) == sealed_top_level ∪ declared_unsealed`
so a new receipt key cannot enter unsealed and unnoticed. Publish both manifests
into the receipt (m7).

**MAJOR-2 — the final-gate seals are live seams.**
Evidence: INJ03. `gates` and `totals` are sealed at gate 49; anything moved into
them between the last measurement and the take is sealed in and published with a
digest that certifies the lie.
*Repair:* seal `gates` incrementally — a rolling digest extended as each ledger
row is appended, so the manifest's `sealed_at_gate` is true row by row — and
derive `totals` **from the sealed rows** at close rather than from mutable state.
Minimum viable: recompute `gates_passed` from `R["gates"]` and `mutants_killed`
from `R["mutants"]` inside `SEAL.close` and gate the equality.

**MAJOR-3 — a declared seal can be dropped without trace, and the completeness
gate cannot see it.**
Evidence: INJ07; the operator's #151 hand-off, now measured.
*Repair:* two lines. In `Seal.verify`, when `only` is given, treat a declared-but-
untaken sid as **broken**, not as absent. In `G-SEAL-COMPLETE`, require
`len(SEAL.rows) == len(SEALS_IN_RUN)` in the predicate, not merely in the
evidence — and move `SEAL.take("SEAL-WAIVERS")` before gate 41, or declare it a
post-completeness seal in the manifest and verify it at close.

**MAJOR-4 — the control row can be moved under its label.**
Evidence: INJ04. `G-CTRL-BRANCHING` evaluates the live variable `us_hits`; the
row `R["constructibility"]["control_underspecified"]` is assembled afterwards and
never re-read by any gate.
*Repair:* build each control's row **first**, have the gate's predicate read the
row, and seal each control at its own gate (`SEAL-CTRL-REFUSED`,
`SEAL-CTRL-BRANCHING`) rather than folding both into the composite
`SEAL-CONSTRUCTIBILITY` (see m8).

**MAJOR-5 — #34: the coverage ledger is not honest at three rows, and the
denominator is wrong twice.**
(a) **`G-WAIVERS-VERIFIED` is absent from the ledger it verifies.**
`R["waiver_ledger"] = waiver_ledger(LD)` is built one statement *before*
`LD.gate("G-WAIVERS-VERIFIED", …)` appends itself, and the gate is not in
`POST_RUN_GATES`. `WAIVERS` *does* declare an entry for it — that entry is **dead
code, never emitted**: 8 WAIVED declared, 7 published. The gate's own "…, 0
unaccounted" is over a denominator that omits the gate making the claim.
(b) **`G-STAB-FULL-FAMILY` (gate 26) is classified FALSIFIABLE on
`MUT-FAMILY-COUNT`**, which the receipt's own mutant row shows dies at
`G-FAMILY-COUNT` — **gate 18, eight gates earlier**. The falsifier cannot reach
the gate it is credited with driving. This is the R5 reachability lesson,
recurring.
(c) **`G-I7-READOUT` (gate 17) is classified FALSIFIABLE on `MUT-DET-EMPTY`**,
which reaches gate 17 and **passes** it — it dies at gate 27. A mutant that
passes a gate is not that gate's falsifier. No mutant drives `G-I7-READOUT`;
its predicate is the `A-EFF-I7` anchor row that gate 15 already enforces.
**Honest denominators.** The gate universe is **51 distinct names** (49 in the
receipt + `G-ARTIFACT-INTEGRITY` + `G-SELFTEST-WRITES-NOTHING`). It is published
as **50 twice, by two different miscounts that happen to coincide**:
`totals["gates"]=50` omits `G-SELFTEST-WRITES-NOTHING`; `len(waiver_ledger)=50`
omits `G-WAIVERS-VERIFIED`. Corrected: **51 = 41 FALSIFIABLE + 8 WAIVED + 2
UNACCOUNTED**.
*Repair:* build the ledger after the gate (or add `G-WAIVERS-VERIFIED` to
`POST_RUN_GATES`); gate `set(WAIVERS) ⊆ {ledger rows}` so a dead waiver cannot
hide; and — the general repair, which mechanically catches both (b) and (c) —
**gate that every FALSIFIABLE row's named mutant has `killed_at` equal to that
row's own gate.** The receipt already carries both sides of that comparison.

**MAJOR-6 — #125: the prohibition wall is one wrapping convention from the U4
failure.**
`norm()` collapses `\s+` and nothing else. I inserted the 97-character retracted
L-1 sentence into a copy of the paper in eight wrappings. Six are caught
(verbatim; `MUT-WALL-L1`'s line-wrap; double-spaced; tab-separated; hyphen-wrapped;
em-dash-swapped). **Two evade**: as a **markdown blockquote** (`> ` at each line
start) and as a **list item** (`- `). The blockquote is the corpus's own house
style for quoting a prior unit — this paper uses it at §9 to quote the catalog.
So the evading form is the form the corpus actually writes, and `MUT-WALL-L1`
tests only the wrapping the repair already handles.
*Repair:* strip leading markdown line-decorations before collapsing whitespace —
`re.sub(r'(?m)^[ \t]*(?:[>\-*+#]+|\d+[.)])[ \t]*', ' ', s)` then `\s+` — re-run
the eight variants, and add `MUT-WALL-L1-QUOTED` injecting the blockquote form so
the repair ships with its own falsifier.

### MINOR

**m1 — `G-WALL-BHS` is a typed constant wearing a measurement's statement.**
`bhs_run = pick("MUT-WALL-BHS", False, True)`; the predicate is `not bhs_run` and
the evidence `{'sprinkling_computed': False, 'groups_acting': [...]}` is a
literal. The published statement says "**Measured on this program's own source**:
no sprinkling, no boost, no rapidity and no frame is computed anywhere." Measured
at my hands, the source contains `sprinkl`×6, `boost`×3, `rapidit`×1, `frame`×1,
`poisson`×2, `lorentz`×4 — all harmless prose, but the gate looks at neither the
source nor the computation, so it cannot tell prose from a boost. *Repair:*
reword to a declaration and re-classify WAIVED, or make it an actual AST scan.
(`G-WALL-KR` and `G-WALL-DIAGONAL` *are* real text gates; only BHS is the constant.)

**m2 — the comparator shares its input with the builder.**
`R["affine"]["classes"] = strat` is the very object the builder formats from, so
in-run `reconstruct(R)` reads the builder's live dict. The gate's statement —
"shares neither code **nor input** nor typed literal" — over-claims by one word.
What *is* genuinely independent, and worth keeping: the format templates, the
`Fraction` re-derivation of `1/32`, the subgroup re-sort, and the five verdict
**words** (`GENERIC`, `NONZERO-EXISTS`, `POSDEF-EMPTY`, `I7-STRICT-EMPTY`,
`BRANCHING 0; REFUSED 0`) — each a typed literal on the builder side and a derived
branch on the comparator side, so a disagreement is what would catch them.
*Repair:* strike "nor input", or route the in-run comparator through
`reconstruct_from_serialized(json.dumps(R))` as the write path already does.

**m3 — the polarity needles sit below the #62 floor, and one is tuned to the
object under test.** All eight polarity needles are 12–19 characters against a
declared `NEEDLE_FLOOR` of 40, and `paper_polarity` does not route through
`match_needle`, so the floor is never applied. P1's false-form needle is
`"U4B-CRYSTAL-SEEDED-"` **with a trailing hyphen**; the paper's §11 contains
`U4B-CRYSTAL-SEEDED` without it. Measured: drop the hyphen and P1's
`false_present` flips to true and the gate fires on the paper's own honest prose.
The hyphen is defensible — it anchors the *emitted head form* — but it is
undeclared in the gate statement and untested, because `MUT-PAPER-POLARITY` flips
the booleans rather than injecting text. *Repair:* use `"U4B-CRYSTAL-SEEDED-["`,
say why in the statement, and make the mutant inject a genuine SEEDED head into
the paper copy.

**m4 — about thirteen of thirty-one mutants inject at the gate's verdict
variable, not at the measured object.** `bad = [win[0]]`, `disagree =
[route_rows[0]]`, `foot_bad = [win[0]]`, `frag_bad = [win[0]]`, `found = False`,
`ns_ok = False`, `us_ok = False`, `w_ok = False`, `same = False`, `t, f = False,
True`, `bhs_run = True`. These prove the gate's ledger wiring; they do not prove
the per-object loop above them would notice a real corruption. The good
counterexamples in the same suite show the standard is reachable:
`MUT-FAMILY-COUNT` (+1 to a computed count, checked against the closed form),
`MUT-NOT-FORCED` (re-drives the victim schedule with a delivery withheld),
`MUT-WALL-L1` / `MUT-WALL-COSMO` / `MUT-PAPER-CLAIM` / `MUT-PAPER-NUMERAL` (real
text), `MUT-SEAL-BROKEN` (a real post-gate mutation). *Repair:* for the six
per-object gates, corrupt one **object** — one route row's field, one window
record's `init` tuple — rather than the exception list.

**m5 — detection without presentation or containment.** A late flip of a sealed
key is caught (INJ01, INJ08) but as an **uncaught Python traceback**: `SEAL.close`
raises `GateFail` outside any handler, so the operator sees a stack trace after
the transcript has already printed 49 `[PASS]` rows, and the house
`GATE FAILED … EXIT 1` form is not used. Post-replace corruption is caught
(INJ05) but **not rolled back**: a non-parsing receipt is left on disk with only
a stdout line as warning. *Repair:* wrap `SEAL.close` in the same handler as the
rest of `main`; on the post-replace failure, restore the prior artifacts.

**m6 — CLI residues (the verdict is otherwise PASS: see §5).** `--verify-paper`
checks only `os.path.exists`, so a **directory** or the **empty string** is
accepted: `--verify-paper v14` gives an uncaught `IsADirectoryError` at exit 1,
indistinguishable to an operator from "the paper drifted"; `--verify-paper ""`
resolves to the repo root. A repeated `--mutant A --mutant B` silently takes the
last — a permissive-shape residue. And `--selftest --mutant MUT-SELFTEST-WRITES`
is inert, because `selftest()` runs before the global `MUT` is assigned, so that
one pairing violates the contract's "no flag is a no-op". *Repair:* require
`os.path.isfile`; reject a repeated flag; set `MUT` before dispatching `--selftest`.

**m7 — the seal manifest is published only in the transcript.** The receipt
carries **no seal key at all**, and neither artifact carries the payload or
transcript digests (those go to stdout only). A reader holding the receipt cannot
check the addendum's totality requirement even in principle. *Repair:* emit
`R["seals"]` and `R["seals_unsealed"]`, then seal them at close.

**m8 — `sealed_at_gate` is a single label on multi-part objects.**
`R["constructibility"]` is assembled after `G-CTRL-BRANCHING` (gate 22) but carries
`fates` gated at gate 20 and two control rows gated at 21 and 22; the manifest
names one gate. Same for `R["determinant"]` (gates 27/28/29 → one label) and
`R["strata"]`. Not exploitable beyond MAJOR-4, but the manifest's semantics are
looser than the addendum's wording.

**m9 — two small typed/read residues.** (i) `window_builds = len(WD) +
driven_wit + 2` — the `+2` is a **typed addend** in a count the paper (§12)
asserts is computed, and it omits the no-supply control, which *is* a
menu-driven 13-event record. `len(BUILD_CACHE) + len(ANCHOR_CACHE) + controls`
is the computed answer. (ii) The `A-EFF-I7` regex reads `|q_12|`, so the published
`read` row is `[1,1,0,1,1,1,0]` where the source prints `−1`. The gate statement
declares the absolute value, so it is disclosed — but the row is not literally
the source row.

---

## 5. The CLI verdict

**PASS on the #82 minimum, with the two residues at m6.**

Thirty-four argv shapes at the parser plus nine as subprocesses. Every unknown
flag, unknown flag argument and missing flag argument exits 2:
`--not-a-flag`, `-h`, `--help`, `--numbers=1`, `--NO-WRITE`, `--`, `x`, `""`,
`--mutant` (bare), `--mutant ""`, `--mutant NOPE`, `--mutant --break-anchor`,
`--break-anchor` (bare), `--break-anchor NOPE`, `--verify-paper /nope/x.md`.
**No `--list-mutants` flag ships** — named here as the orchestrator asked; the
#82 minimum does not require one, and empty and garbage mutant names exit 2
(confirmed at both the parser and as subprocesses). `MUT-CLI-PERMISSIVE` swaps in
the registered permissive shape and dies on target at `G-CLI-WHITELIST`.

**The write contract holds exhaustively:** across all 34 argv shapes, `write` is
true for the bare invocation **only**; `--no-write`, `--numbers`, `--selftest`,
`--mutant`, `--break-anchor` and `--verify-paper` all set it false. The audit
trace confirms the artifacts are opened for writing only in the delivery run.

`--selftest`: exit 1, wrote nothing, demonstration printed; verified against
**all ten** anchors via `--break-anchor` (F6). All 31 mutants run on scratch,
each at its declared target, artifacts byte-unchanged (F7).

---

## 6. The D60 seed-dependence (K3 item 4)

**The finding is REAL — reproduced at my own hands.** Driving d60's `pick` at
the committed record's first-arbitration prefix under five `PYTHONHASHSEED`
values gives **three distinct winners** (seeds 0 and 1 → one; seed 7 → another;
seeds 12345 and 987654 → a third) and **four distinct sort orders**, while
`maxhits` is invariantly **7**. `sorted(…, key=repr)` over frozensets is
hash-seed dependent exactly as the unit says; the count is not.

**The handling is honest.** Reporting the candidate count only is precisely the
right call, it is stated in the paper §3, in the `G-CTRL-BRANCHING` statement,
and in the receipt row, and the reason is given. **FOUND.** And U4b itself is
clean: every event of every one of its 11,686 records is specified by its full
tuple, so at most one candidate can match and the tie-break is never consulted —
the byte-identity I measured under a random hash seed (F1) is the proof.

**The class, and the corpus-wide registration it needs.** This is a #91-class
defect — a delivery product that is not a function of the inputs — living in a
**committed v10 constructor**, `v10/code/d60_crystal_exact.py` line 131
(`hits = sorted((e for e, q in menu if spec(e)), key=repr)`), inherited by every
unit that drives that builder, d66 included. Two mitigations already exist and
both are partial:

- d60's own `C1` gate asserts `b1.refusal is None and b1.maxhits == 1` for the
  brick, so that record is fully specified and seed-independent;
- d66's `A1(a)` asserts `max menu hits per specification over every step of every
  record == 1` over its whole sweep, and its `arbchain` gate asserts
  `bb.maxhits == 1`.

**But d60's `C2` gate — the 3×3 grid, 46 events — checks only
`b2.refusal is None`. It does not check `maxhits`.** So d60's grid record is not
gated against under-specification, and if any of its picks were under-specified
its published poset profile would be hash-seed dependent. I could not close that
from here (d60 needs d47a/d55c/d58 to run) and it is not a U4b defect; it is a
registration item. I also note d60 line 70 reads
`open('v10/code/d42b1_transport_exact.py')` **relative to the CWD** — a second,
independent #91 residue in the same file.

**Registration wanted, RUNBOOK-level:** *a tie-break over an unordered container
is a hash-seed dependence; any delivery pick must be fully specified
(`maxhits == 1`) and that must be **gated**, not assumed.* With it: a corpus
sweep for `sorted(…, key=repr)`, `sorted(set(…))` and `min`/`max` over frozensets
in every committed constructor; a `maxhits` gate on d60's `C2`; and a
`PYTHONHASHSEED`-varied re-run as a standing delivery check (this unit passes it).

---

## 7. What the adjudication should carry

1. The seam is **ten wide, five exploitable at exit 0, all five exploited**, and
   its character is that the unit **seals what it measured and leaves unsealed
   what it vouched for**. MAJOR-1 through MAJOR-4 are the repairs.
2. **Two forgeries leave the receipt byte-identical** (INJ06, INJ07). The corpus's
   normal integrity check — verify the receipt's sha256 — does not see them. That
   is a corpus-level fact, not only a U4b fact.
3. **MAJOR-5(b)/(c) is the R5 reachability lesson recurring**, and the mechanical
   repair (gate `killed_at == the row's own gate`) is cheap and general. It
   belongs in the RUNBOOK, not only in this unit.
4. **MAJOR-6 is the U4 #125 failure one wrapping convention away**, in the
   corpus's own house style. The repair is two lines and should be lifted
   corpus-wide with the engraving.
5. The D60 registration (§6), which is about a **committed v10 constructor**, not
   about U4b.
6. **Nothing above touches the physics.** I rebuilt the entire headline from my
   own code — 747, 3, 0, 9, 261, 486, the det-value multiset, 6912/36/108,
   216/36/0, 2,041,200, 1/32 over 55,987,200, the four period directions — and
   **not one published number moved**.
