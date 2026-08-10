# WELD 2 (paper-13, the carrier census) — HOSTILE REVIEW, K5 THE INSTRUMENT

**Reviewer:** instrument seat (K5), v14 ledger #93 panel.
**Object:** paper `535e288ff412`, code `290149118b9d`, output `5e35e7a0115f`,
receipt `bacdb7a5e985`, all at commit `58195da`; pin `9d19515cb3ae`;
protocol `e7b99e05557d`. All six hashes re-verified against the working
tree **and** against `git show 58195da:` — identical, no drift.
**Interpreter:** `/opt/homebrew/bin/python3.13`.
**Disciplines observed:** read-only git (`log`/`show`/`rev-parse`/`status`
only); every run on scratch copies under
`…/scratchpad/w2-in/`; no in-repo execution; this file is my sole repo write.

---

## GRADE: **AWF** (accept with fixes)

The unit is not R. Every delivered number reproduces, the 826-character
verdict string is byte-exact between paper and receipt, the plain run
byte-reproduces twice from a foreign repo root, the argv whitelist is
real, and all 13 declared mutants die at their named gates with
artifacts untouched. Nothing false is claimed about the census result.

The unit is not A. **Twelve reviewer-designed injections were run and
twelve survived** — including a verdict-head flip that delivers
`WELD2-**FOUND**-AT-THE-DECLARED-FAMILY` at 32/32 gates, 18/18 anchors,
exit 0; a moving-ref bypass that makes the receipt's own provenance
statement demonstrably false in a passing run; and a post-gate receipt
corruption whose `w2_census_output.txt` is **byte-identical to the
committed artifact** while the receipt claims 7 gate failures.

**Calibration of my harness:** the same scratch harness ran the 13
declared mutants and registered 13/13 kills. My battery therefore
targets the *complement* of the declared surface, and that complement is
undefended.

---

## 1. WHAT I EXECUTED — honest counts

| class | count |
|---|---|
| program invocations | **49** |
| — plain off-tree, git available | 1 |
| — plain off-tree, git-less | 1 |
| — plain off-tree, `PYTHONHASHSEED=987654` | 1 |
| — `--selftest` (clean source, writes-nothing harness) | 1 |
| — `--selftest` (on the typed-anchor injection) | 1 |
| — argv whitelist battery | 19 |
| — `--list-mutants` standalone | 1 |
| — declared mutants | 13 |
| — reviewer injections (plain runs) | 11 |
| independent recomputations of delivered quantities | **~179** |
| disagreements with the delivered artifacts | **0** |
| reviewer-designed injections (11 executed + 1 static-proved) | **12** |
| injections caught | **0** |
| declared mutants confirmed dead at their named gate | **13 / 13** |
| declared mutants leaving artifacts unchanged | **13 / 13** |

Byte-identity, twice: an off-tree run under `…/w2-in/repo/` (a mirror
whose `v10–v13` are symlinks, `v14/code` real, `.git` symlinked) produced
`5e35e7a0115f…` / `bacdb7a5e985…` — **exactly the committed bytes**, and
so did a second run at `PYTHONHASHSEED=987654`. The hash-seed-independence
claim in the module docstring is therefore **measured, not asserted**.

---

## 2. THE #82 CLI CONTRACT, CLAUSE BY CLAUSE

RUNBOOK §14 addendum (v14 #82) requires exactly three things. Verdict:
**the contract's three clauses are MET.** Handler at L2506–2559.

### 2.1 "an argv-parsed CLI that rejects unknown flags (exit 2)" — **PASS**

19 hostile invocations, all as required:

| argv | exit | stderr |
|---|---|---|
| `--badflag` | 2 | `unknown argument(s): --badflag` |
| `--selftests` (typo) | 2 | `unknown argument(s): --selftests` |
| `--list-gates` | 2 | `unknown argument(s): --list-gates` |
| `--no-write` | 2 | `unknown argument(s): --no-write` |
| `-x` | 2 | `unknown argument(s): -x` |
| `positionalarg` | 2 | `unknown argument(s): positionalarg` |
| `--mutant` (no value) | 2 | argparse usage |
| `--mutant=BOGUS` | 2 | `unknown mutant: BOGUS` |
| `--mutant BOGUS` | 2 | `unknown mutant: BOGUS` |
| `--list-mutants --badflag` | 2 | `unknown argument(s): --badflag` |
| `--mutant MUT-QUOTE --badflag` | 2 | `unknown argument(s): --badflag` |
| `--list-mutants=1` | 2 | argparse usage |
| `--list-mutants` | 0 | 13 registry rows |

Two blemishes, both MINOR (see MINOR-2): argparse **prefix abbreviation is
on**, so `--self`, `--selft`, `--m`, `--list`, `--list-mutant` are all
silently accepted as their unique completions; and `--help`, a *declared*
flag, returns **2** because `except SystemExit: return 2` (L2521) swallows
argparse's `SystemExit(0)`.

### 2.2 "a `--selftest` that corrupts one anchor, confirms exit 1, and writes nothing" — **PASS on the letter, hollow on the numeric half**

Writes-nothing: **proven**. I hashed all three files in the run directory
before and after; `diff` of the two hash manifests was empty
(`w2_census_exact.py`, `w2_census_output.txt`, `w2_census_receipt.json`
all byte-identical). Exit-path: **genuinely exercised** — L2584–2588 sets
`ANCHOR_FAIL = live + 1`, calls the real `exit_code()`, restores, and
requires the answer to be 1. Report: `18 anchors (7 numeric, 11
verbatim); 18 of 18 would fail the run; vacuous = []`, exit 0.

But the numeric half cannot fail. For each numeric anchor the selftest
computes `bad = committed + 1` and asks `bad != computed` (L2571–2574).
For a passing anchor `committed == computed`, so this is
`c + 1 != c` — true by integer arithmetic, for every anchor, always. It
never re-enters `anchor()` and never touches a derivation. **Proved by
INJ11:** I replaced `anchor("A02", …, 113, n_menu, …)` with
`anchor("A02", …, 113, 113, …)` — a typed anchor, the exact failure the
selftest is cited against — and the selftest still reported
*"18 of 18 would fail the run; vacuous = []"*, exit 0. The plain run of
that variant emitted `w2_census_output.txt` **byte-identical to the
committed artifact** and the line `[ANCH] A02 … committed=113
computed=113`, indistinguishable from the genuine run.

### 2.3 "a `--mutant NAME` harness" — **PASS, cleanly**

13/13 die at their named gate; 13/13 leave both artifacts byte-unchanged;
unknown names exit 2. Registry dump matches the source `MUTANTS` list
exactly (13 rows, 12 distinct targets — `G-CTRL-EMPTY` is targeted twice).

| mutant | named target | gates that failed | anchors that failed |
|---|---|---|---|
| MUT-PROVENANCE | G-PROVENANCE | G-PROVENANCE | V10 |
| MUT-QUOTE | V01 | — | V01 |
| MUT-MENU-KEY | G-MENU-CLASSES | +G-CONG-CLASSES, G-SCISSORS | A02, A05 |
| MUT-CONG-WRONG | G-CONG-CLASSES | +G-CONG-ROUNDS, P2, P5, SIX | A05 |
| MUT-SQUARE-DROP | G-SQUARES | +G-MENU-CLOSES | A03 |
| MUT-ADDITIVITY | G-ADDITIVITY-972 | G-ADDITIVITY-972 | A07 |
| MUT-DIVPRED | G-DIVISION-PREDICATE | +5 more | — |
| MUT-CRYSTAL-INHOMOG | G-CTRL-FOUND | +G-CTRL-EMPTY-FALSIFIABLE | — |
| MUT-WALK-PLANT | G-CTRL-EMPTY | G-CTRL-EMPTY | — |
| MUT-SMUGGLE-BLIND | G-SMUGGLE-REACHABLE | G-SMUGGLE-REACHABLE | — |
| MUT-CYCLE-PLANT | G-SCISSORS | +G-VERDICT | — |
| MUT-FIBER-LAX | G-CTRL-FOUND-FALSIFIABLE | G-CTRL-FOUND-FALSIFIABLE | — |
| MUT-ARITY-LAX | G-CTRL-EMPTY | +G-VERDICT | — |

`--list-gates` **does not exist** (exit 2). It is not contract-required,
and the paper does not claim it — but sibling units ship it
(`gprep_foundation_exact.py` L5223), and without it the "32 gates" figure
has no registry dump; it is checkable only by running.

**CLI VERDICT in the contract's terms: COMPLIANT.** All three required
clauses hold and are demonstrated under hostile argv. This is the first
v14 unit for which that is true without qualification, and the fourth-
recurrence disease (silent flag-ignoring; a "selftest" that writes) does
**not** recur here.

---

## 3. THE INJECTION BATTERY

Each row is a single-edit variant of the committed source, run plain in
its own scratch mirror. "Survived" = exit 0, 32/32 gates PASS, 18/18
anchors PASS, artifacts written.

| # | injection | edit | result | proof of execution |
|---|---|---|---|---|
| INJ01 | **verdict-head flip** | `WELD2-EMPTY-…` → `WELD2-FOUND-…` (L2448) | **SURVIVED** | delivered head `WELD2-FOUND-AT-THE-DECLARED-FAMILY-…`; `G-VERDICT` PASSES while its own statement reads "the pre-registered outcome string that fires is WELD2-**EMPTY**-AT-THE-DECLARED-FAMILY"; out `21e3b2b4aa4f` |
| INJ02 | obstruction flip | `THE-ARITY-CYCLICITY-SCISSORS` → `NO-OBSTRUCTION-AT-ALL` | **SURVIVED** | head `WELD2-EMPTY-AT-THE-DECLARED-FAMILY-NO-OBSTRUCTION-AT-ALL`; out `10c6ab8e6aa5` |
| INJ03 | **fate-cell corruption** | one cell TYPE-DEAD → ARITY-DEAD | **SURVIVED** | verdict `TYPE-DEAD=35\|ARITY-DEAD=13` (paper: 36/12); carriers now disagree (MENU 17/7/1/5, CONG 18/6/1/5) yet still stamped `@BOTH`; out `9cf81291a47e` |
| INJ04 | carrier disagreement | one CONG cell TYPE-DEAD → STRUCT-DEAD | **SURVIVED** | MENU 18/6/1/5 vs CONG 17/6/1/6, verdict still `@BOTH`; out `472658afd502` |
| INJ05 | **post-gate receipt corruption** | `receipt["gate_count"]=99; ["gate_failures"]=7` before write | **SURVIVED** | `w2_census_output.txt` **byte-identical to committed** (`5e35e7a0115f`) and says "gates: 32, failures: 0", while the receipt says `gate_count 99, gate_failures 7`, exit 0 |
| INJ06 | prose-number drift (#20) | — | **SURVIVED (static)** | the file contains exactly 7 `open()` calls; none reads `paper-13`; `grep -cE "def (verify\|render\|check_paper)"` = **0**. No instrument reads the paper at all |
| INJ07 | verdict-number corruption | `sl_menu = sum(…)` → `sl_menu = 999` | **SURVIVED** | verdict carries `MENU-SELFLOOPS=999`, `G-SCISSORS` PASSES (its condition never reads `sl_menu`); out `6f2ff67ccbe9` |
| INJ08 | **verbatim truncation (#62)** | V03 quote → `"the "` | **SURVIVED** | 18/18 anchors PASS; V03 now binds a 4-byte string instead of "additivity holds at 972 of 972 constraints"; out `ab19f08943e6` |
| INJ09 | arena-artefact swap | verdict's `EMPTY-AT-WALK(…)` fed `ctrl_found` | **SURVIVED** | verdict reads `EMPTY-AT-WALK(FOUND-candidate)` while `G-CTRL-EMPTY` PASSES; out `7b42ccc965bf` |
| INJ10 | post-gate count corruption | `PAYLOAD["candidate_count"]=61`, `fates={"TYPE-DEAD":61}` after `G-CENSUS-COMPLETE` | **SURVIVED** | output.txt **byte-identical to committed** and says 60; receipt says `candidate_count 61` |
| INJ11 | **typed anchor** | `anchor("A02",…,113,n_menu,…)` → `…,113,113,…` | **SURVIVED** | plain run's output.txt **byte-identical to committed**; `--selftest` still reports "18 of 18 would fail; vacuous = []" |
| INJ12 | **moving-ref bypass (#91)** | corrupt the *worktree* copy of `v13/code/ha_successor_receipt.json` (git keeps the pinned bytes) | **SURVIVED** | `G-PROVENANCE` PASSES asserting the file is read "via `git show 95c3b77:` … **never from mutable worktree state**", while `G-I7-ARENA` in the same run reports "**12** declared records" — a value that exists only in the corrupted worktree copy; out `9abbee9969f6` |

**Run 12 / caught 0 / survived 12.**

---

## 4. FINDINGS

### MAJOR-1 — the verdict head is a typed literal that no gate compares (the R4 F1 disease, recurring)

`obstruction` (L2446) and the head `WELD2-EMPTY-AT-THE-DECLARED-FAMILY`
(L2448) are typed into the f-string. `G-VERDICT`'s condition (L2484–2490)
tests only `n_found == 0 and n_unmot == 0 and n_smug == 0`, the fate-sum,
and the allowed fate-name set. There is **no complete-string equality
gate and no independent reconstruction** — R4's F1 at least had a
reconstruction that copied the head; here there is none. INJ01 delivers a
receipt whose verdict says FOUND and whose `G-VERDICT` statement says
EMPTY, at exit 0.

**Repair (liftable):** after `n_found`/`n_smug`/`n_unmot`/`fates` are
computed, add a second function that reads **only `PAYLOAD`** and rebuilds
the entire string field by field —

```python
def _rebuild_verdict(P):
    f = P["fates"]; m = P["mechanism"]; c = P["controls"]
    head = ("WELD2-FOUND-AT-THE-DECLARED-FAMILY" if <found>0> else
            "WELD2-SMUGGLED-AT-THE-DECLARED-FAMILY" if <smug>0> else
            "WELD2-UNMOTIVATED-AT-THE-DECLARED-FAMILY" if <unmot>0> else
            "WELD2-EMPTY-AT-THE-DECLARED-FAMILY")
    …                                    # every field from P, none from locals
```

then `gate("G-VERDICT-EQUALITY", …, _rebuild_verdict(PAYLOAD) == verdict,
{"rebuilt": …, "emitted": verdict})`, and register `MUT-HEAD-FLIP`
(flips the literal) and `MUT-OBSTRUCTION-FLIP` targeting it.

### MAJOR-2 — a moving-ref bypass at L1016 makes the provenance statement false in a passing run (#91, and this unit postdates the engraving)

`i7_arena()` (L1016) does
`json.load(open(os.path.join(REPO, "v13/code/ha_successor_receipt.json")))`
— a raw worktree read that bypasses `read_pinned`. Provenance checks that
path (`PINNED` L238, want `542b8735daf0`) and will happily reroute it
through `git show` when the worktree drifts, while consumption keeps
reading the drifted worktree bytes. INJ12 exhibits both statements in one
receipt: rerouted-via-git in `G-PROVENANCE`, and 12-declared-records in
`G-I7-ARENA`. This is the **only** consumption-side raw repo read in the
file (the other six `open()` calls are provenance hashing, `read_pinned`,
`__file__`, the two writers, and the selftest's vanchor read), so the
repair is one site.

**Repair (liftable):**

```python
body, route = read_pinned("v13/code/ha_successor_receipt.json", "542b8735daf0")
if body is None:
    raise SystemExit("I7 receipt unresolved at its pinned sha")
rec = json.loads(body)
PAYLOAD["i7_receipt_route"] = route
```

plus a gate asserting `PAYLOAD["i7_receipt_route"]` equals the route
recorded in the `G-PROVENANCE` row for that path, and `MUT-I7-ROUTE`
targeting it.

### MAJOR-3 — there is no #20 instrument at all

The paper's front matter says "every number printed here renders from the
receipt" and §10 repeats the discipline; **no code reads the paper**. Zero
`verify_paper`/`render` functions; `paper-13` occurs only in four
docstring/description strings. I performed the sweep by hand instead (§6
below) and it comes back clean — but the claim is unbacked and would not
survive an edit.

**Repair (liftable):** add `verify_paper()` reading
`v14/paper-13-weld2-carrier-census.md`, normalising `1 048 576` and
`\,`, extracting every token matching `(?<![\w.])\d[\d]*(?:/\d+)?`, and
requiring each to occur in `json.dumps(receipt, default=str)` or in a
declared allow-list `CITED_ELSEWHERE = {"89": "ledger ref", "265":
"paper-12 §9", "462": "paper-12 §9"}`; `gate("G-PAPER-RENDERS", …,
unexplained == [])`; add `MUT-PAPER-DRIFT`.

### MAJOR-4 — a false instrument claim: "11 verbatim anchors … each falsified by a mutant"

Paper §10 (L571–573). In fact `vanchor` applies its mutant hook only when
`vid == "V01"` (L128): **1 of 11** verbatim anchors has a falsifier. And
the #62 binding is weak in a second way — INJ08 truncated V03's quote to
`"the "` and the run passed 18/18, because the test is bare substring
presence, with no length or uniqueness requirement. "Consumer-gated" is
also *naming* only: no consumer gate's condition reads its quote (e.g.
V09 = `NO-SEED-AT-THE-CARRIER` is named to `G-VERDICT`, whose condition
never mentions it); the binding is at run level, via `ANCHOR_FAIL`.

**Repair (liftable):** parameterise the hook —
`q = mutate(f"MUT-QUOTE-{vid}", quote, quote + " [corrupted]")` — and add
11 registry rows `("MUT-QUOTE-V01","V01") … ("MUT-QUOTE-V11","V11")`;
strengthen the test to
`body.count(q.encode()) == 1 and len(q) == committed_len` with the
committed length carried in the `vanchor` call. Or, failing that, correct
§10 to "one (V01) is falsified by a declared mutant".

### MAJOR-5 — no gate binds any individual census cell, and the `@BOTH` stamp is unearned (#87)

`G-CENSUS-COMPLETE` (L2381) checks a cardinality that the nested loops
force structurally, plus `all("fate" in r for r in rows)` — key
*presence*, not value. `G-VERDICT` checks the aggregate fate multiset.
**Nothing binds a cell to its fate**, and **nothing compares
`fates_by_carrier["MENU"]` with `fates_by_carrier["CONG"]`** even though
the verdict is carrier-stamped `@BOTH` and §5 asserts "the two carriers
return identical fate distributions". INJ03 and INJ04 both deliver
disagreeing carriers under an unchanged `@BOTH` stamp at 32/32.

**Repair (liftable):** declare the 60-cell fate table as data in the pin
and gate it cell-wise —

```python
gate("G-FATE-PER-CELL", …,
     all(r["fate"] == EXPECTED[(r["carrier"], r["site_gen"],
                                r["link_gen"], r["arity_repair"])]
         for r in rows), {"mismatches": [...]})
gate("G-CARRIER-AGREEMENT", …,
     all(a["fate"] == b["fate"] for a, b in _pair_by_generator(rows)),
     {"menu": fates_by_carrier["MENU"], "cong": fates_by_carrier["CONG"]})
```

with `MUT-FATE-CELL` and `MUT-CARRIER-SPLIT`.

### MAJOR-6 — verdict-bearing numbers with no gate and no comparator

The verdict string carries `336`, `MENU-SELFLOOPS=45`,
`CONG-SELFLOOPS=0`, `ISOS=72`, `I-SITE-ASSIGNMENT-FIBER=6`. None appears
in any gate *condition*: `G-SCISSORS` tests only acyclicity and
zero-cycle-counts; `G-CTRL-FOUND` tests only `fate == "FOUND-candidate"`;
`G-CTRL-FOUND-FALSIFIABLE` only `fate == "UNMOTIVATED"`. INJ07 proves it
for `45`.

**Repair (liftable):** promote each to a numeric anchor (A08…A12) so the
`--selftest` and the receipt cover them, **and** extend the conditions:
`G-SCISSORS … and sl_menu == 45 and sl_cong == 0 and ab_count == 336`;
`G-CTRL-FOUND … and ctrl_found["isomorphisms"] == 72`;
`G-CTRL-FOUND-FALSIFIABLE … and ctrl_falsif["inventory"]["I-SITE-ASSIGNMENT"] == 6`.

### MAJOR-7 — a failing run still overwrites the delivered artifacts, and there is no final integrity gate

`write_artifacts` is called before `exit_code()` is consulted (L2538–2545),
so a run with failed gates still writes. The git-less leg proves it: G-PROVENANCE
FAILS (22 of 24 resolved), exit **1**, and both artifacts are written
anyway with different bytes (`14785c4d…`, `430f6722…`). In-repo that
would clobber `5e35e7a0115f`/`bacdb7a5e985`. Separately, nothing re-reads
what was written: INJ05 and INJ10 both deliver a receipt that contradicts
its own byte-identical output text.

**Repair (liftable):** `if write and exit_code() == 0: write_artifacts(...)`
(else print and return `exit_code()`); and add a terminal
`gate("G-ARTIFACT-INTEGRITY", …)` that re-reads `OUT_TXT`/`OUT_JSON` from
disk after writing and requires `json.load(OUT_JSON)["payload"]["verdict"]`
to equal the emitted verdict and `["gate_count"] == len(GATES)`,
`["gate_failures"] == FAILED`.

### MINOR-1 — the `#82`-strengthened comparator standard is met four times and failed once

Genuinely independent pairs, verified by reading both routes:
menu partition (frozenset-key hashing **vs** pairwise mapping equality,
`str(q)` vs `Fraction`); congruence (signature refinement **vs**
relation pair-splitting bisimulation); squares (admissibility-pair
enumeration **vs** grouping the generated family by (prefix, unordered
last-two) with no `admissible()` call and no `Fraction` arithmetic);
acyclicity (Kahn topological sort — exact at any length — **vs** DFS
simple-cycle enumeration to length 6). No shared typed literal appears
inside any builder/comparator pair; `113`/`185`/`1546`/`88` live only in
the gate conditions and anchors.

The exception is additivity. `add_cmp = len(splittable) * 3 * 2 *
len(X7) * len(links7)` (L2013) re-multiplies **the builder's own loop
bounds** — `for nm in splittable` × 3 `smode` × 2 `fmode` × `X` × `links`
(L1066–1088). It cannot disagree unless the loop structure itself is
edited. The paper calls it "an independent arithmetic comparator …
sharing no construction with the builder"; it shares the construction's
cardinalities exactly. (Impact is limited: `MUT-ADDITIVITY` does kill the
gate, via the violation count and A07.)

**Repair:** recount the constraints from the set of cell-keys actually
compared inside the census loop, not from the loop bounds.

### MINOR-2 — argparse looseness

`allow_abbrev` defaults to True, so `--self`, `--selft`, `--m`, `--list`,
`--list-mutant` are accepted; and `--help` exits 2.

**Repair:** `argparse.ArgumentParser(prog=…, allow_abbrev=False)` and
`except SystemExit as e: return 0 if e.code in (0, None) else 2`.

### MINOR-3 — the git-less leg of #91 does not byte-reproduce

Required by the engraving. Today it cannot, because two of the 24 pinned
sources (`note-weld2-referent-scout.md`, `paper-12-gamma-main.md`) carry
drifted worktree bytes and git is the only route. To the unit's credit the
failure is **loud** (G-PROVENANCE FAIL, exit 1) rather than the Γ-prep
silent-`LEDGER #None` class — the design is right, only the write-on-
failure (MAJOR-7) turns it into damage. Worth recording as a scoped
compliance note rather than a defect of construction.

### MINOR-4 — the paper's deviation-2 disclosure points at the wrong place

§8.2: the grading-theorem shortcut "is marked as such in the receipt's
**waiver census**". The waiver census has exactly 3 entries
(`G-TWO-WAY`, `G-DEAD-LIST-CITED`, `G-U4-REGISTERED`) and none is the
grading theorem. The marking is real but lives elsewhere — per row, in
`census_rows[*].acyclicity_basis`: 12 rows read `measured`, 4 `the
cardinality grading of the Boolean lattice`, 4 `the poset height
grading`, 4 `the address-length grading`, 36 `null` (never reached).

**Repair:** re-word to name `acyclicity_basis`, or add a fourth waiver of
class `ARGUMENT-CARRIED`. Note also that for those 12 rows
`arena_linkrel` returns `{}, True, <grading>` — the acyclicity is a
returned literal, with no mutant exercising that branch
(`MUT-CYCLE-PLANT` plants only in the measured MENU/CONG branch).

### MINOR-5 — `SMUGGLED=0` is structural for census rows, not measured

`detect`'s `count_fn(i7rec)` returns `base_field` regardless of its
argument (L1715–1716), so `classify_smuggling` cannot return True for any
census candidate; and no census row reaches that step anyway. The verdict
reports `SMUGGLED=0` beside `FOUND=0` without that qualifier, though §6
does supply the analogous "not reached" note for the inventory items.

**Repair:** in §5/§7 state that SMUGGLED is structurally unreachable for
candidates of this shape (the count function is built from `rel` alone)
and that the classifier's positive value is exercised only by the declared
probe.

### MINOR-6 — two uncited prose numbers

§8.3's "265 MENU / 462 CONG classes" at $d\le5$ are the only paper numbers
absent from both artifacts. They are `paper-12-gamma-main.md` L789–790
(d74's wider arm) and the sentence explicitly says they are not run, but
they read as measurements.

**Repair:** cite as "(paper-12 §9, d74's $d\le5$ arm)".

### MINOR-7 — three undeclared near-tautological gates

The 3 waivers cover exactly the 3 gates whose condition is the literal
`True` (`G-TWO-WAY`, `G-DEAD-LIST-CITED`, `G-U4-REGISTERED`) — honest, and
each waiver names real backing. But three more are tautological and
**unwaived**: `G-COUNT-SEMANTICS` (`len(COUNT_GENS) == 1`, a fact about a
module constant); `G-INTERIOR-DEAD-ON-ARRIVAL` (`"C1-…-INTERIOR-SPLIT" in
{"C1-…-INTERIOR-SPLIT"}` and `COUNT_GENS[0] not in` it — two typed
strings against a typed set); `G-CENSUS-COMPLETE` (cardinality forced by
the loops, plus key presence). `G-SMUGGLE-REACHABLE` is near-tautological
too — the "grammar-side probe" is `lambda rec: {("g", 0): 7}`, a constant
— though it does exercise the classifier and carries a mutant.

**Repair:** add `waiver={"class": "DECLARATION-CARRIED", …}` to those
three, or give them measured content.

---

## 5. COVERAGE AT #34 — honest denominators

**32 gates** (recounted independently from source: 26 literal `gate("…"`
calls plus 6 emitted by the `G-CONG-P1…P6` loop at L1994; the receipt
carries 32, all names unique). **13 mutants**, **12 distinct targets**
(11 gates + the V01 anchor; `G-CTRL-EMPTY` is targeted twice, by
MUT-WALK-PLANT and MUT-ARITY-LAX).

**Gates with a declared falsifier: 11 of 32 (34%).**
G-PROVENANCE, G-MENU-CLASSES, G-SQUARES, G-CONG-CLASSES,
G-ADDITIVITY-972, G-DIVISION-PREDICATE, G-CTRL-FOUND,
G-CTRL-FOUND-FALSIFIABLE, G-CTRL-EMPTY, G-SMUGGLE-REACHABLE, G-SCISSORS.

**Gates with NO falsifier: 21 of 32**, named in full —
G-MENU-CLOSES, G-CONG-ROUNDS, G-CONG-P1-DESCENT, G-CONG-P2-SINGLE-VALUED,
G-CONG-P3-CURVATURE-44, G-CONG-P4-Q-HOLONOMY, G-CONG-P5-K-HOLONOMY,
G-CONG-P6-LUMPABLE, G-CONG-SIX-PROPERTIES, G-I7-ARENA, G-COUNT-SEMANTICS,
G-CRYSTAL-FORCED, G-CRYSTAL-DIAGONAL-EMPTY, G-TWO-WAY,
G-CTRL-CRYSTAL-AT-I7, G-CTRL-EMPTY-FALSIFIABLE,
G-INTERIOR-DEAD-ON-ARRIVAL, G-DEAD-LIST-CITED, G-U4-REGISTERED,
G-CENSUS-COMPLETE, G-VERDICT.

Three of those are load-bearing for headline claims and should acquire
falsifiers first: **G-VERDICT** (MAJOR-1), **G-CRYSTAL-DIAGONAL-EMPTY**
(the unit's unanticipated measurement — the empty diagonal at 9/9 × 5/5
has no mutant; `MUT-DIVPRED` kills it only incidentally), and the
**six CONG properties**, which carry the "six of six" re-derivation
headline (`MUT-CONG-WRONG` kills P2/P5 incidentally, never P1/P3/P4/P6).

**Assert-unmutated / tautological mutants: none.** All 13 hooks are real
edits to live code paths; none is an `assert True`.

**Waivers: 3, all backed.** G-TWO-WAY's backing (G-CTRL-FOUND,
G-CTRL-EMPTY) are both falsifiable and both die under declared mutants;
G-DEAD-LIST-CITED's backing is the census rows; G-U4-REGISTERED claims
nothing. The 3 waivers coincide exactly with the 3 literal-`True` gates,
which is the honest arrangement — see MINOR-7 for the three that escaped
it.

---

## 6. PAPER ↔ OUTPUT ↔ RECEIPT — three-way sweep

**60 distinct numeric tokens, 438 occurrences** in the paper. Every one
traces to the receipt except `89` (a ledger reference), `9/9` (formatting
over 9s that do trace), and `265`/`462` (MINOR-6). Specifically verified
against `w2_census_receipt.json`:

- verdict string: **byte-exact**, 826 characters, paper §7 block vs
  `payload.verdict`;
- carrier/arena: 3969 histories, 113 MENU (and 113 unweighted), 185 CONG,
  5 rounds, 1546 closed / 88 defective squares, spectrum
  `{1/2:70, 2:10, 3/2:6, 2/3:2}`, MENU closes 1402/44;
- CONG P1–P6: 4 non-constant MENU classes; 0/0 vs 0/4 multi-valued; 44
  defective close, 1362 of 1546, 44 self-loops with spectrum
  `{1/2:26, 2:10, 3/2:6, 2/3:2}` (in the receipt payload, not the output
  text — the paper's claim is "renders from the receipt", so this is
  compliant); q-primes {2,3} rank 2; k {2,3} rank 2 vs MENU {2,3,5,13}
  rank 3; CK 10/10 vs 6/10;
- I7: 9 sites, 3 links, 11 declared / 9 admissible / 6 splittable, 36
  refinements, 972 checks, 0 violations, unsplittable
  `G-ANISO, G-CURVED, G-FLAT`;
- division events: 1536 selected, 1536 tagged, 20 distinct, 8 pair;
- Ulam: 3969 total, by depth 1/8/60/452/3448;
- census: 60 candidates, 36/12/2/10, identical 18/6/1/5 per carrier;
- mechanism: A→B 336, B→A 336, 2 actor objects, 45/0 self-loops, both
  acyclic, 0 simple cycles at every length 2–6;
- controls: crystal FOUND with 72 isomorphisms, fibers 1/1/1, 18 cells all
  count 2; falsifier UNMOTIVATED with fibers 6/2/1; crystal-at-I7
  STRUCT-DEAD; walk 30 events / 4 divisions / 0 on (A,B);
- all five crystals' event, division and per-link count fields
  (72/18, 96/24, 30/6, 66/12, 46/1; diagonal `[[0, 9]]` in 5 of 5);
- provenance: 24 pinned sources, 22 worktree + 2 `git show 95c3b77:`,
  matching §8.5 exactly; `source_sha256` prefix `290149118b9d` = the
  code's own sha256-12.

**Zero disagreements.** No delivered number is wrong.

---

## 7. BORN-COMPLIANT RULING

**The first unit born under the #82 contract does meet the #82 bar, and
does not meet the bar of the standards that surround it.**

Met, and demonstrated under attack: the argv whitelist (19/19), the
mutant harness (13/13 dead at target, 13/13 artifacts untouched), the
`--selftest` writes-nothing and real-exit-path clauses, the mutant
registry's completeness, byte-reproduction twice from a foreign root
including under a changed `PYTHONHASHSEED`, and comparator independence in
4 of the 5 places it is claimed. The disease that produced the engraving —
silently ignored flags, a "selftest" that writes both artifacts — is
absent. On the CLI clause specifically this is the strongest v14 unit
audited to date.

Not met:

1. **#234 / verdict-in-gate** — the head is typed and uncompared
   (MAJOR-1). This is the single most serious finding: the instrument can
   emit `WELD2-FOUND` at exit 0.
2. **#91 / no moving refs** — one consumption-side raw worktree read
   (MAJOR-2), proved to falsify the receipt's own provenance sentence.
3. **#20 / prose renders from the receipt** — claimed, with no instrument
   whatsoever (MAJOR-3).
4. **#87 / gates bind objects** — the 60-cell fate table and the `@BOTH`
   carrier stamp are bound only by aggregates (MAJOR-5).
5. **#62 / verbatim anchors** — 1 of 11 falsified against a claim of 11
   (MAJOR-4), and the substring test admits `"the "`.
6. **#82-strengthened / comparator independence** — one degenerate
   comparator, described in the paper as independent (MINOR-1).

The honest summary for the ledger: **born-compliant on the contract,
not yet born-compliant on the era.** Every one of the seven MAJOR items
is a bounded, mechanical repair inside `w2_census_exact.py` plus three
sentences of paper text; none touches the census, the scissors argument,
or any delivered number.

---

## 8. SCOPE OF THIS REVIEW

I did not adjudicate K1–K4: whether the 60-cell enumeration is exhaustive
over the pin's vocabulary, whether the scissors theorem's quantifier
covers the no-enumeration claim, whether the crystal control's FOUND
standard is the census's standard, or the licensed reading of the empty
diagonal. Two observations are handed to those seats rather than ruled on
here: (i) the STRUCT-DEAD kill uses a **directed** acyclicity test
(`has_distinct_vertex_cycle`) while the FOUND branch uses an
**undirected** Cayley incidence (`graph_isomorphisms`, L1374–1384) — the
two branches of one detector use different notions of incidence, and the
operator seat should rule whether the directed kill is the right standin
for the undirected embedding test; (ii) 12 of the 60 rows have their
acyclicity decided by a returned literal `True` under a grading argument,
with `arena_linkrel` handing back an empty relation `{}` and no mutant
exercising that branch.

**Repo state at close.** The six object files are byte-unchanged
(`535e288ff412`, `290149118b9d`, `5e35e7a0115f`, `bacdb7a5e985`,
`9d19515cb3ae`, `e7b99e05557d` — re-verified after all work). My only
repo write is `?? v14/review-w2-instrument.md`. `git status` also shows
eight files modified by **other agents in flight**, which are not mine
and which I disclaim: `v14/code/gprep_foundation_exact.py`,
`gprep_foundation_output.txt`, `gprep_foundation_receipt.json`,
`r4_defect_stage_exact.py`, `r4_defect_stage_output.txt`,
`r4_defect_stage_receipt.json`, `v14/paper-10-defect-on-the-stage.md`,
`v14/paper-11-transport-foundation.md`. No LOG or STATUS edit was made.

That set **churned during this review**: at open it also included
`gmain_exact.py`, `gmain_output.txt`, `gmain_receipt.json` and
`paper-12-gamma-main.md`, and did not include `paper-11`. This matters to
one recorded result: the git-less and INJ12 runs were taken while
`paper-12-gamma-main.md` was drifted, which is the condition under which
the 2-of-24 reroute (§6) and MINOR-3 were measured. The finding is
structural and does not depend on which files happen to be drifting, but
the exact reroute count is a snapshot of a live tree.
