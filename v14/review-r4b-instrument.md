# R4b (paper-15, momentum) — HOSTILE REVIEW, K5 THE INSTRUMENT

**Reviewer:** instrument seat (K5), v14 ledger #111 panel.
**Object:** paper `5f8ec142319c`, code `53a10e87ec19`, output `d33412225949`,
receipt `00e7f6ea0f90`, all at commit `10c8d17`; pin `bcd12bbe6fd8`; protocol
`b9cd2133d961`. All six hashes verified against the working tree **and** against
`git show 10c8d17:` — identical, no drift. The eight hash-pinned runtime inputs
were re-hashed independently and all eight match their frozen digests.
**Interpreter:** `/opt/homebrew/bin/python3.13`.
**Disciplines observed:** read-only git (`log`/`show`/`rev-parse`/`status` only);
every run on scratch copies under `…/scratchpad/r4b-in/`; no in-repo execution;
this file is my sole repo write.

---

## GRADE: **AWF** (accept with fixes)

The unit is not R, and not close to it. Every delivered number reproduces under
an independent recomputation in a different representation of the field; the
off-tree, git-less plain run is **byte-identical to the committed artifacts on
the first attempt**, and again from a foreign CWD under a changed
`PYTHONHASHSEED`; all 66 declared mutants die at their **named** gate with the
artifacts byte-unchanged; the 67/66/3 denominators are honest and machine-checked;
and the unit ships the first working **#20 instrument in v14** — it caught every
numeral drift I could plant, including all three of the protocol's surprise
numbers. On the CLI clause, on #34, on #91 and on comparator independence this is
the strongest v14 unit audited to date, by a wide margin over weld-2.

The unit is not A. **Nineteen reviewer-designed injections were run; nine were
caught and ten survived** — including a post-gate verdict-head flip that delivers
`R4B-**NO-MOTION**<MOTION=MOVING=0-OF-58;STATIC=58-OF-58;…>` in both artifacts at
exit 0, 67/67 gates, 66/66 mutants, while the *same receipt* carries 57 census
rows reading `MOVES` and a `G-MOTION-TWO-WAY` detail string reading
`MOVES=57 STATIC=1`; a verbatim window truncated to the four bytes `"the "` with
`r4b_momentum_output.txt` **byte-identical to the committed artifact**; and two
prose inversions that deliver **both artifacts byte-identical to the committed
ones** while the paper asserts the negation of what was measured.

**Calibration of my harness:** the same scratch harness ran the 66 declared
mutants and registered 66/66 on-target kills, and caught 9 of my own 19
injections. My battery therefore targets the complement of the declared surface,
and the surviving complement is one seam wide: **everything between the last gate
and the bytes on disk.**

---

## 1. WHAT I EXECUTED — honest counts

| class | count |
|---|---|
| program invocations | **130** |
| — plain off-tree, git-less (no `.git` anywhere in the mirror) | 1 |
| — plain, foreign CWD, `PYTHONHASHSEED=987654` | 1 |
| — `--no-write` | 1 |
| — `--verify-paper` (bogus path; a different file) | 2 |
| — `--selftest` (writes-nothing proved by hash manifest) | 1 |
| — `--break-anchor` (all 8 sources, plus one repeat) | 9 |
| — hostile argv battery | 20 |
| — declared mutants (66 distinct, one repeated for timing) | 67 |
| — reviewer injection runs | 28 |
| independent recomputations of delivered quantities | **215** |
| — from a different field representation, off the parent's receipt | 106 |
| — three-way paper ↔ output ↔ receipt sweep and registry re-derivations | 109 |
| disagreements with the delivered artifacts | **0** |
| reviewer-designed injections (valid) | **19** |
| — caught | **9** |
| — survived | **10** |
| — discarded as harness errors (disclosed in §3) | 5 |
| declared mutants confirmed dead at their **named** gate | **66 / 66** |
| declared mutants leaving artifacts byte-unchanged | **66 / 66** |

**Byte-identity, twice.** A mirror at `…/r4b-in/repo/` containing only this
unit's paper, its code and the eight pinned sources — no `.git`, no repository,
no sibling files — produced `d33412225949…` / `00e7f6ea0f90…`: **exactly the
committed bytes**, first run, exit 0. A second mirror run from CWD `/tmp` under
`PYTHONHASHSEED=987654` produced the same two hashes. The docstring's
off-tree/git-less claim (#91) is therefore **measured, not asserted**, and so is
hash-seed independence, which the paper does not even claim.

**Independent recomputation.** I rebuilt the census from the *parent's* receipt
(the opponent object, never the unit's own artifacts) over Q(i, √2) as 4-tuples
`p + qi + r√2 + si√2` — a different basis from the instrument's power basis
(1, z, z², z³), with different multiplication rules. 106 checks: the 928-cell
eigen-equation, μ₈ membership and unit modulus (928/928 each); 58 distinct
reduced dispersions; 57 non-constant with C004 the unique constant; parity
invariance 58/58; 1856 velocity cells all even; 320 aliased in 19 families;
speed spectrum {0,1,2} and VMAX 2; reach 8/14/36 with every overshoot aliased;
the full 3×3 agreement matrix (58 | 39 39 33 33 32 32 25 25); the 9-row fiber
table; both support-drift tables (16|12, 18|0, 24|0 and 16|15, 18|10, 24|8);
monomial 16, nonzero-winding 12 all monomial, interfering 42 all moving with zero
drift **and** zero winding; 1792 = 64² − 48²; all six §3 sample rows; all 19 §5
class rows; and a field-by-field comparison of my census against all 58 receipt
rows across 8 fields. **Zero disagreements.** No delivered number is wrong.

---

## 2. THE #82 CLI CONTRACT, CLAUSE BY CLAUSE

Handler at L2090–2133 (`parse_args`, hand-rolled — no `argparse`, so none of the
weld-2 abbreviation blemishes exist). **Verdict: the three required clauses are
MET; a fourth, documented flag is dead (MAJOR-4).**

### 2.1 "an argv-parsed CLI that rejects unknown flags (exit 2)" — **PASS**

20 hostile invocations, all exit 2, all with a usage line on stderr, and a
before/after hash manifest of the whole run directory showing **no writes**:

| argv | exit | | argv | exit |
|---|---|---|---|---|
| `--badflag` | 2 | | `--break-anchor BOGUS` | 2 |
| `--selftests` (typo) | 2 | | `--help` | 2 |
| `--list-gates` | 2 | | `-h` | 2 |
| `--list-mutants` | 2 | | `--no-write --badflag` | 2 |
| `-x` | 2 | | `--self` (abbrev) | 2 |
| `positional` | 2 | | `--selft` (abbrev) | 2 |
| `--mutant` (no value) | 2 | | `--no` (abbrev) | 2 |
| `--mutant BOGUS` | 2 | | `--mut MUT-ANCHOR` (abbrev) | 2 |
| `--mutant=MUT-ANCHOR` (flag=value) | 2 | | `--verify-paper --badflag` | 2 |
| `--break-anchor` (no value) | 2 | | `""` (empty arg) | 2 |

Prefix abbreviation is **off** (the parser is exact-match), and `--help`/`-h`
correctly exit 2 because neither is a declared flag. Both weld-2 MINOR-2
blemishes are absent.

### 2.2 "a `--selftest` that corrupts one anchor, confirms exit 1, writes nothing" — **PASS, and genuinely numeric**

Writes-nothing: **proven by hash manifest** — every file in `v14/code/` hashed
before and after; `diff` of the manifests empty. Exit 1. The report reads
`SELFTEST: died at G-BYTE-ANCHORS -- as required.`

The report matches reality, and I checked it the hard way. Unlike weld-2's
selftest — which asked `c + 1 != c` and could not fail — this one calls
`build_state(target)` with `SOURCES[0]`'s expected digest replaced by
`"000000000000"` and **requires a real `GateFail`**. It re-enters the whole
derivation. I sample-corrupted every anchor myself via `--break-anchor` (8 runs,
one per source): **all 8 die at `G-BYTE-ANCHORS`, exit 1, writing nothing**. And
I corrupted a pinned source's *bytes on disk* (INJ10, appending a comment to
`review-r4-operator.md`): also dead at `G-BYTE-ANCHORS`. The falsification path
is real.

### 2.3 "a `--mutant NAME` harness" — **PASS, cleanly**

66/66 die at their **declared target gate** — I verified the kill site
independently against the source's `MUTANTS` table rather than trusting the
receipt's `on_target` field. 66/66 leave both artifacts byte-unchanged (hash
manifest before and after the whole sweep). Unknown names exit 2 and never
report SURVIVED. `--mutant` and `--break-anchor` both come out of the parser with
`write=False`, which `G-SELFTEST-WRITES-NOTHING` measures rather than asserts.

There is no `--list-mutants`/`--list-gates`; the registries are dumped into the
receipt instead (`mutants` 66 rows, `gates` 66 rows, `waiver_ledger` 67 rows), so
unlike weld-2 the figures *are* checkable without running. Source and receipt
registries agree exactly.

### 2.4 The fourth flag — **`--verify-paper [PATH]` IS DEAD (MAJOR-4)**

`parse_args` accepts `--verify-paper`, stores `opts["verify_paper"]`, sets
`write=False` — and **`main()` never reads the key.** Measured:

- `--verify-paper /nonexistent/NOPE.md` → exit **0**, full delivery-shaped run,
  the non-existent path silently swallowed;
- `--verify-paper v14/note-r4-adjudication.md` → transcript **identical** to the
  previous one;
- both are **byte-identical to a plain `--no-write` run**.

The docstring (L39–42) promises "Reports the paper-claim rendering and numeral
coverage against PATH". It does nothing of the kind. `G-CLI-CONTRACT`'s probe
`(["--verify-paper"], False)` asserts only that the flag is *accepted*.

This is the registered #82 disease in its next dress: not "silently ignores an
unknown flag" but "silently ignores a **known** flag and its argument." Impact is
bounded — the docstring itself says the flag "is a report, not the enforcement",
and the enforcement (`G-PAPER-CLAIMS`, `G-PAPER-NUMERAL-COVERAGE`,
`G-PAPER-COVERAGE-FINAL`) genuinely runs inside the delivery run and genuinely
bites (§3). No delivered claim depends on the flag. But a documented CLI clause
that is a no-op on an argument it accepts is exactly the shape #82 outlaws.

**CLI VERDICT in the contract's terms: COMPLIANT on all three required clauses,
with one undeclared-by-the-contract but documented flag dead (MAJOR-4).**

---

## 3. THE INJECTION BATTERY

Each row is a single-edit variant of the committed source (or of the paper), run
plain in its own scratch mirror. "Survived" = exit 0, 67/67 gates, 66/66 mutants,
artifacts written.

| # | injection | class | result | proof of execution |
|---|---|---|---|---|
| INJ01 | **post-gate verdict-head flip** | verdict-head | **SURVIVED** | delivered head `R4B-NO-MOTION`, verdict `MOVING=0-OF-58;STATIC=58-OF-58`, in **both** artifacts, exit 0, 67/67; same receipt still carries 57 rows `MOVES` and `G-MOTION-TWO-WAY` detail `MOVES=57 STATIC=1`; out `32dac192e3c2` json `b00a6d495241` |
| INJ02b | **motion-table cell move** (#87) | fate/motion cell | **SURVIVED** | `dispersion_census[1].motion` `MOVES`→`STATIC`, `max_speed` `1`→`0`; receipt now has 56 `MOVES` rows against `counts.moving = 57`; exactly 3 leaves differ from the committed receipt; json `ad6f0164d603` |
| INJ03 | post-gate receipt corruption | receipt corruption | **SURVIVED** | `gates[0].passed=False`, `mutants[0].killed=False`, `totals.mutants_killed=7`; the run prints `ALL GATES PASSED (67/67); ALL MUTANTS DEAD (7/66)` and exits 0 |
| INJ04 | post-gate **output-text** corruption | output corruption | **SURVIVED** | `output.txt` reads `non-constant dispersions 58 of 58` and `MOVING=58` while the receipt reads 57 and `R4B-DISPERSION-READ`; the integrity gate compares `back_txt == text`, i.e. the corrupted text against itself |
| INJ05b | verbatim window shrunk to `"the "` (VB-DISPERSION-57) | #62 | **CAUGHT** | `G-MUTANTS-ON-TARGET`, `killed 65 of 66; off target [('MUT-VERBATIM','G-VERBATIM-ANCHORS',None)]` — caught **indirectly**, see MAJOR-2 |
| INJ06 | prose numeral drift `320 of 1856`→`321 of 1857` | #20 | **CAUGHT** | `G-PAPER-NUMERAL-COVERAGE`, nothing written |
| INJ07 | prose numeral drift `1792`/`64²−48²`→`1793`/`65²−48²` | #20 surprise number | **CAUGHT** | `G-PAPER-NUMERAL-COVERAGE`, nothing written |
| INJ08 | prose numeral drift `best other 39 of 58`→`38 of 58` | #20 surprise number | **CAUGHT** | `G-PAPER-NUMERAL-COVERAGE`, nothing written |
| INJ09b | **arena-artefact swap** | control under a census label | **SURVIVED** | `dispersion_census[55]` (C055) publishes the **brickwork control B058's** radius, `2`→`1`; `output.txt` **byte-identical to the committed artifact**; json `02ccc825c779` |
| INJ10 | pinned source drifted on disk (#91) | moving ref | **CAUGHT** | `G-BYTE-ANCHORS`, nothing written |
| INJ11 | head law flipped in **both** "independent" copies | comparator | **CAUGHT** | `G-HEAD-LAW-RESPONSIVE` — the zeroed-census two-way probe defeats a coordinated flip |
| INJ12 | prose inversion `57 of 58 families MOVE`→`fail to MOVE` (§1) | #20 polarity | **SURVIVED** | **both artifacts byte-identical to the committed ones** — the claim string still occurs in §3 and §9 |
| INJ12b | prose inversion `16 monomial`→`16 non-monomial` (§8) | #20 polarity | **SURVIVED** | **both artifacts byte-identical**; the paper now asserts the negation of "Only the monomials transport" |
| INJ13 | post-gate ceiling-disclosure corruption | receipt corruption | **SURVIVED** | `path_value_anchors[8]` (the 16-of-16 separations ceiling) rewritten to `12/12` in the delivered receipt, exit 0 |
| INJ14 | integrity-gate failure | write-on-failure | **CAUGHT**, but **wrote anyway** | `G-ARTIFACT-INTEGRITY` fires, exit 1 — and both artifacts are left on disk, the `output.txt` ending `ALL GATES PASSED (67/67) … EXIT 0` |
| INJ15 | prose inversion `18 of the 19 circulant classes move`→`0 of the 19` (§1) | #20 polarity | **SURVIVED** | **both artifacts byte-identical to the committed ones** |
| INJ16 | §10 instrument prose `66 declared mutants, all dead`→`65 dead` | #20 | **CAUGHT** | `G-PAPER-NUMERAL-COVERAGE` — §10 *is* covered |
| INJ17 | **verbatim window shrunk to `"the "` (VB-PROPAGATOR)** | #62 | **SURVIVED** | the parent's propagator sentence — the anchor §6 is built on — reduced to 4 bytes; `output.txt` **byte-identical to the committed artifact**; the only receipt witnesses are `verbatim_anchors[4].chars 138 → 4` and two byte-count strings |
| INJ19 | single unconditional family head flip | #87 control | **CAUGHT** | `G-MOTION-HEAD-PER-FAMILY` — the per-family binding is real |

**Run 19 / caught 9 / survived 10.**

*Discarded as harness errors, disclosed for honesty:* INJ02 (edited row 0, which
is C004 and already `STATIC` — a semantic no-op), INJ05 (edited only one string
literal of a multi-literal window, mangling rather than truncating it — superseded
by INJ05b/INJ17), INJ09 and INJ18 and INJ20 (my edits raised tracebacks rather
than exercising a gate). None is counted above.

---

## 4. FINDINGS

### MAJOR-1 — the gate/artifact seam: every gate closes on an in-memory object that is then mutated into the artifact (#234, the R4-F1/weld-2-MAJOR-1 disease in its next form)

This is the finding that decides the era ruling, and it is the more serious for
how well defended everything upstream of it is.

The unit's verdict machinery is, at gate time, the best in v14: `derive_head`
(Path A, L1730) and `reconstruct_from_serialized` (Path B, L1818) are genuinely
independent formatters — **no shared numeric literal, no shared helper** (Path B
calls only its own `g` lambda and `str`; it never calls `derive_head` or any
formatter above it), and `G-VERDICT-RECONSTRUCTED` compares the **complete**
1242-character string character for character. `G-HEAD-LAW-RESPONSIVE` exercises
the law in both directions and defeats even a coordinated flip of both copies
(INJ11). All 56 verdict values carry individual flip probes.

And all of it is spent by the time the artifact exists. `run_receipt_gates`
returns `R`; `main()` then mutates `R` freely for ~50 lines before
`payload = json.dumps(R, …)` at L2963. The terminal `G-ARTIFACT-INTEGRITY` does
**not** compare against any value fixed at gate time — it re-reads the bytes it
just wrote and calls `reconstruct_from_serialized(back_json)`, i.e. it re-derives
the head **from the corrupted counts**. It therefore *confirms* the corruption:

```python
    R["counts"]["moving"] = 0
    R["counts"]["static"] = R["counts"]["families"]
    R["verdict"]["head"] = "R4B-NO-MOTION"
    R["verdict"]["string"] = reconstruct_from_serialized(
        json.dumps(R, indent=1, sort_keys=True))
    emit_report(R, S)
```

Four lines, inserted after the last gate, deliver
`R4B-NO-MOTION<MOTION=MOVING=0-OF-58;STATIC=58-OF-58;CONTROL=C004-IDENTITY-TWO-WAY;…>`
in **both** artifacts at exit 0, with `G-VERDICT-RECONSTRUCTED` reporting
`reconstruction equal (1242 chars)` and `G-HEAD-LAW-RESPONSIVE` passing — while
the same receipt's `dispersion_census` still carries 57 rows reading `MOVES` and
`G-MOTION-TWO-WAY`'s own detail string reads `MOVES=57 STATIC=1`. INJ03, INJ04
and INJ13 are the same seam in three other places (gate rows, mutant rows,
totals; the output transcript; the inherited ceiling disclosure).

**Repair (liftable), three parts:**

1. **Freeze the verdict at gate time.** In `run_receipt_gates`, after
   `G-VERDICT-RECONSTRUCTED` passes, take `SEALED = (R["verdict"]["string"],
   hashlib.sha256(Rjson.encode()).hexdigest())` and return it. In `main()`,
   require `json.loads(back_json)["verdict"]["string"] == SEALED[0]` — a value
   the post-gate window cannot reach — instead of `R["verdict"]["string"]`.
2. **Seal the counts.** Extend the integrity gate to require
   `json.loads(back_json)["counts"] == SEALED_COUNTS`, the dict as it stood when
   the census gates closed. INJ01, INJ03 and INJ13 all die on this.
3. **Seal the transcript.** Take the `LOG` length and digest at the same moment
   and require the written text to match, so INJ04 dies too.

Then register `MUT-POSTGATE-HEAD`, `MUT-POSTGATE-COUNT` and `MUT-POSTGATE-LOG`
targeting the extended gate. Note the integrity gate is already a declared
forcing whose registered mechanism is "two-way by construction"; the two-way
half (the corrupted probe file) works and I fired it (INJ14). It is the
*reference value* that is missing, not the machinery.

### MAJOR-2 — #62 is bare substring presence, and the parent's window hash was dropped

`vb_rows` tests `w in texts[sid]` (L687) and records only `{"id", "source",
"consumer_gate", "present", "chars"}`. There is no length check, no uniqueness
check, and — the sharp part — **no digest**. The *parent* R4 receipt records
`window_sha256_12` on every verbatim anchor; this unit removed the field.

INJ17 truncates `VB-PROPAGATOR` — the parent's "the local family lives exactly
where the propagator cannot be resolved", the sentence §6 of this paper is built
on — from 138 bytes to the 4 bytes `"the "`. The run passes 67/67 with
`r4b_momentum_output.txt` **byte-identical to the committed artifact**. Only
`MUT-VERBATIM` has a text-dependent hook, and it targets `VB-DISPERSION-57`
alone; that is why INJ05b was caught (as a *mutant survival*, at
`G-MUTANTS-ON-TARGET`) and INJ17 was not. **12 of the 13 windows are reducible to
a 4-byte decoration undetected.**

The paper's §10 sentence "each verbatim window bound to the named gate that
consumes it" is true only as *naming*: `G-ANCHOR-CONSUMERS-EXIST` checks the
named gate exists and is evaluated, which I confirmed for all 13 — but no
consumer gate's *condition* reads its window.

**Repair (liftable):** restore the parent's field —
`"window_sha256_12": hashlib.sha256(w.encode()).hexdigest()[:12]` — carry the 13
frozen digests in the declaration, and gate
`all(r["window_sha256_12"] == FROZEN[r["id"]] for r in vb_rows)`; additionally
require `texts[sid].count(w) == 1`. Add `MUT-QUOTE-<VID>` rows for all 13 (or one
parameterised `MUT-VERBATIM` that walks the list) so the mutant/gate ratio stops
carrying a single window.

### MAJOR-3 — #87 binds the *objects* but not the *published rows*

The internal binding is real and I verified it adversarially: `G-MOTION-HEAD-PER-FAMILY`
re-derives `want` from `disp[n]` for each of the 58 families and lists
disagreements, and an unconditional single-family flip dies on it (INJ19). Two
independent routes (non-constant phase; some nonzero cell speed) are required to
agree per family, with an inline `GateFail` if they do not. That is a genuine
#87 pass, and materially better than weld-2's aggregate-only census.

But `build_receipt` (L1909–1934) *renders* 58 rows × 14 fields into
`R["dispersion_census"]`, and **no gate re-reads them**. The flip probes cover
only `counts` keys named in `SEGMENT_KEYS`. So:

- INJ02b moves one published row `MOVES`→`STATIC`: the receipt ships 56 `MOVES`
  rows against `counts.moving = 57`, exit 0;
- INJ09b publishes the brickwork control **B058's** radius under the census label
  **C055**: `output.txt` byte-identical to the committed artifact, exit 0.

The same gap covers `path_value_anchors` (INJ13 rewrote the 16-of-16 ceiling
disclosure to 12/12 in the delivered receipt), `class_rows`, `velocity_fiber`
and `agreement_matrix`.

**Repair (liftable):** one terminal gate that re-derives the published tables
from `S` and compares field by field —

```python
gate("G-PUBLISHED-ROWS-BOUND", …,
     all(row == _render_row(S, row["family"]) for row in R["dispersion_census"])
     and R["class_rows"] == _render_classes(S)
     and [a["measured"] for a in R["path_value_anchors"]]
         == [jpath(R4, a["path"]) for a in PATH_VALUE_ANCHORS],
     {...})
```

with `MUT-ROW-FIELD` and `MUT-ROW-SWAP`. Folded into the sealed-payload repair of
MAJOR-1 this is one mechanism, not two.

### MAJOR-4 — `--verify-paper [PATH]` is a documented flag that does nothing

Measured in §2.4: `main()` never reads `opts["verify_paper"]`; the flag's runs
are byte-identical to `--no-write`; a non-existent PATH is silently swallowed.

**Repair (liftable):**

```python
    if opts["verify_paper"]:
        p = os.path.join(REPO, opts["verify_paper"]) \
            if not os.path.isabs(opts["verify_paper"]) else opts["verify_paper"]
        if not os.path.exists(p):
            print("error: no such paper: %s" % p, file=sys.stderr); sys.exit(2)
        paper_text = read_text(p)
```

and print `paper_coverage` for that text, exiting 1 on any `missing`/`uncovered`.
Then extend `G-CLI-CONTRACT`'s probe list with
`(["--verify-paper", "/nonexistent"], True)`.

### MINOR-1 — #20 is numeral-complete and polarity-blind

The instrument is real, and it is the era's first: `paper_coverage` extracts
every numeral from the paper and requires each to be rendered from the receipt or
named in a 12-entry declared residue, and it runs as a gate *inside* the delivery
run — plus a final re-run once the instrument's own totals close. My own
independent sweep reproduces its figures exactly (78 distinct numerals, 413
occurrences, 44 claims, zero uncovered, zero declared-but-absent). It caught 4 of
4 numeral drifts I planted, including all three surprise numbers the protocol
names (320/1856, 1792 = 64²−48², 39/58) and a drift inside §10 itself.

What it cannot see is **polarity**. The claim test is substring presence anywhere
in the flattened text, so a sentence can be inverted wherever its claim string
also occurs elsewhere, and inverted freely wherever the inversion introduces no
new numeral. Three demonstrations, all delivering **both artifacts byte-identical
to the committed ones**:

- INJ12: §1 "**57 of 58 families fail to MOVE**" (the claim survives on §3/§9);
- INJ15: §1 "**0 of the 19 circulant classes move**" (the capital-`MOVE` claim
  survives on §5);
- INJ12b: §8 "…are precisely this unit's 16 **non**-monomial families", the
  negation of the section's own headline "Only the monomials transport".

**Repair:** require each claim to occur the number of times the receipt expects
(`flat.count(v) == EXPECTED_OCCURRENCES[k]`, a declared table), and add a small
polarity guard — a declared list of forbidden negators (`not`, `fail`, `no`,
`never`, `non-`) inside a fixed window around each claim occurrence. Neither is
complete; both raise the cost of an inversion from zero.

### MINOR-2 — the #208 laundering probe is `mut()`-shaped, and the file itself uses the other shape

`scan_laundering` (L2636) walks every `LD.gate(...)` call and reports any whose
predicate argument contains a call to `mut(...)`. Real, and `MUT-LAUNDER` kills
it. But it is blind to three other shapes, which I proved statically against the
committed scanner:

| laundering shape | detected |
|---|---|
| `LD.gate(…, not mut("MUT-Z"), …)` — the declared decoy | **yes** |
| predicate reads the module global: `… or MUT == "MUT-Z"` | no |
| predicate reads a flag precomputed from `mut()` | no |
| the value is mutated in place before the gate, no clause at all | no |

The second shape is not hypothetical: `mut`'s docstring calls it "the **ONLY**
mutant switch", yet `paper_claims` (L2228) and `paper_coverage` (L2280) both read
`MUT == "MUT-PAPER-CLAIM"` / `MUT == "MUT-PAPER-NUMERAL"` directly. Those two
uses are honest — they inject, they do not exempt — but they establish the
bypass shape in live code, and the standing probe cannot see them.

**Repair:** extend the scan to flag any `ast.Name` load of `MUT` inside a gate
predicate, and to flag a gate predicate whose free variables are assigned from
`mut(...)` earlier in the same function; or route the two paper hooks through
`mut()` so the docstring's "only switch" is true.

### MINOR-3 — a failing integrity gate still leaves the artifacts on disk

`main()` writes `OUT_JSON` and `OUT_TXT` (L2975–2978) **before** the integrity
comparison, and on failure prints and `sys.exit(1)` with no rollback. INJ14 shows
the consequence: exit 1, and both artifacts sitting on disk with the
`output.txt` ending `ALL GATES PASSED (67/67); ALL MUTANTS DEAD (66/66)` /
`EXIT 0`.

This is far narrower than weld-2's MAJOR-7 — *every other* gate failure raises
`GateFail` and exits before any writer is reached, which I confirmed on 9
`--break-anchor` runs and all 66 mutants (artifacts byte-unchanged throughout).
Only the terminal gate can reach the hole. But in-repo it would clobber
`d33412225949`/`00e7f6ea0f90` with a pair whose text asserts a clean run the
process just denied.

**Repair:** write to `OUT_JSON + ".tmp"` / `OUT_TXT + ".tmp"`, verify, then
`os.replace` both; on failure `os.remove` the temporaries and exit 1.

### MINOR-4 — the receipt carries no digest of the instrument that produced it

There is no `source_sha256` field (the sibling `w2_census_exact.py` has one, and
so does the parent). The only witness anywhere in the artifacts to *which program
ran* is an incidental byte count inside two gate detail strings
(`"subprocess-free source scan over 140587 bytes"`,
`"round trip stable over 70430 bytes"`). With length-matched padding a source
edit leaves the delivered receipt differing from the honest one in **only the
corrupted field** — which is how INJ02b was arranged.

**Repair:** `R["source_sha256"] = hashlib.sha256(source_text().encode()).hexdigest()`,
rendered into the output text, and a paper sentence naming it.

### MINOR-5 — `G-PAPER-COVERAGE-FINAL`'s distinctive content is empty

The forcing registration says the final gate exists because the in-run twins run
before "the instrument's own totals close". But `R["totals"]` is populated with
`gates`, `gates_falsifiable`, `gates_waived`, `anchors`, `byte_anchors`,
`path_value_anchors`, `verbatim_anchors`, `mutants` and `verdict_values` at
L2448–2459, **before** `G-PAPER-CLAIMS` runs at L2463. The only keys added later
are `mutants_killed`, `mutants_on_target` and `gates_passed` — whose values (66,
66, 67) are already rendered by the in-run twins via `totals["mutants"]` and
`totals["gates"]`. I could not construct an edit caught by the final gate and not
by its twins; INJ16, aimed squarely at §10, died at the twin.

The gate is harmless and its forcing is honestly registered — but it is the one
of the three whose registered mechanism does not describe a real gap. Either
move the `totals` update to after the sweep (so the final gate acquires real
content and the prediction check still closes), or re-word the forcing to
"re-runs the same check on the closed totals; its content is confirmatory".

### MINOR-6 — three cosmetic defects in the source

- L366–368: the comment above `FORCINGS` says "the only **two** gates with no
  declared mutant"; the dict has **three** entries and the paper says three. A
  stale comment on a load-bearing structure.
- L1088–1092: `roots = set()` followed by a doubly-nested loop whose body is
  `pass`. It computes nothing, `roots` is never read, and it sits inside the μ₈
  theorem-legs derivation where a reader will take it for a computation.
  `G-MU8-THEOREM-LEGS` in fact tests `dens == {1} and len(MU8) == 8`, which is
  correct and sufficient; delete the loop or make it the check.
- `PENDING_GATES = 10` is a hand-counted constant reconciled against
  `len(LD.rows) + 2`. It closes correctly today (I verified 67 = 66 ledger rows +
  the integrity gate), but two hand-counted numbers must agree for the check to
  mean anything.

---

## 5. COVERAGE AT #34 — honest denominators

Recounted independently from source and from the receipt; the three agree.

- **67 gates.** 67 literal `LD.gate("…"` names in the file, minus the
  `G-DECOY-LAUNDER` inside `_decoy_laundered_gate` (never evaluated), plus
  `G-ARTIFACT-INTEGRITY` (evaluated in `main()`'s writing path, so absent from
  the receipt's 66-row `gates` list but present in the 67-row `waiver_ledger`).
  All names unique — the `Ledger` refuses duplicates.
- **66 mutants**, 66 distinct names, **64 distinct targets**; two gates are
  targeted twice (`G-MOTION-HEAD-PER-FAMILY` by `MUT-MOTION-HEAD` and
  `MUT-MOTION-CONTROL`; `G-VERDICT-RECONSTRUCTED` by `MUT-COUNT-TYPED` and
  `MUT-HEAD-TYPED`).
- **Gates with a declared falsifier: 64 of 67 (96%)** — against weld-2's 34%.
  Every one of the 64 has a non-empty `falsifier` list in the waiver ledger, and
  I confirmed all 66 kills land on their named target.
- **Gates with no falsifier: exactly 3**, and they are exactly the 3 `FORCINGS`.
  `targeted − evaluated` is empty: no mutant names a gate that does not run.

**Are the 3 forcings genuinely forced?** Machine-checked, not author-tagged:

| forcing | registered mechanism | my verdict |
|---|---|---|
| `G-MUTANTS-ON-TARGET` | "its falsifier is the sweep; every surviving or off-target injection fails it" | **FORCED — and I fired it.** INJ05b made `MUT-VERBATIM` survive and the gate died: `killed 65 of 66; off target [('MUT-VERBATIM','G-VERBATIM-ANCHORS',None)]` |
| `G-ARTIFACT-INTEGRITY` | "two-way by construction — a corrupted payload written to a probe path must be detected" | **FORCED — and I fired it.** INJ14 produced `GATE FAILED: G-ARTIFACT-INTEGRITY … (corruption detected=True)`, exit 1. The negative control is real; the *reference value* is not (MAJOR-1) |
| `G-PAPER-COVERAGE-FINAL` | "its in-run twins carry the injection falsifiers and die on every sweep" | **REGISTERED but content-empty** — the twins do die (`MUT-PAPER-CLAIM`, `MUT-PAPER-NUMERAL`, confirmed), but the final gate has no coverage its twins lack (MINOR-5) |

**Assert-unmutated / tautological mutants: none.** All 66 hooks are real edits to
live code paths; none is an `assert True`. 64 are reached through `mut()`; the
two paper mutants read the `MUT` global directly (MINOR-2). Two are edits to
*decoy source text* rather than to the run (`MUT-SUBPROCESS` appends
`SUBPROCESS_DECOY`, `MUT-PARENT-IMPORT` appends `PARENT_IMPORT_DECOY` before the
AST scan) — that is the right shape for testing a scanner, and both die at their
named gate.

**Gates-bind-objects (#87):** the 58 families **are** each bound to their own
dispersion by their own gate, and no aggregate stands in — verified adversarially
(INJ19). The published rows are not (MAJOR-3).

**Comparator independence (#82-strengthened):** the strongest in v14. AST
comparison of `build_verdict` and `reconstruct_from_serialized`: **no shared
numeric literal** (A has none; B has `0`); no shared helper (A calls
`derive_head`, `dict`, `mut`, `str`; B calls only its own `g` and `str`); B never
calls `derive_head`, as its docstring claims. The two read the **same 56 count
keys** and hard-code the **same segment grammar** — which the paper states
explicitly and correctly ("what the two paths necessarily share is the segment
grammar … what they do not share is any value"). The residual is not a false
claim; it is that a corruption of `counts` upstream of both passes both, which is
exactly the seam MAJOR-1 exploits.

---

## 6. PAPER ↔ OUTPUT ↔ RECEIPT — three-way sweep

- **78 distinct numeric tokens over 413 occurrences** in the paper; my
  independent extraction reproduces the gate's own figures exactly. Uncovered:
  **none**. Declared-derived residue: 12 entries, all present. Claims: 44, all
  matched verbatim up to line wrapping.
- **The verdict string**: 1242 characters; the output transcript's 74-column
  wrapping **reassembles character for character** to `payload.verdict.string`.
  The paper deliberately does not print it.
- **The 20 path-value anchors** re-read by me directly from
  `r4_defect_stage_receipt.json` at their frozen JSON paths: all 20 match both
  `expected` and `measured`. **Zero mismatches.**
- **The 13 verbatim windows** re-located by me in their pinned sources: all 13
  present, and — a stricter test than the unit's — all 13 present **exactly
  once**.
- **20 headline reconciliations** paper ↔ receipt, all ok: 57/58 MOVE; C004 the
  control; 928 = cells = eigen-verified = in-μ₈ = unit-modulus; 58 profiles vs 14
  labels; VMAX 2 = diameter 2; spectrum {0,1,2}; 320/1856 in 19 families;
  8/14/36 reach; cone 16/16; interior radii [1]; ceilings 16-of-16 and 2-of-2;
  58/58 under 1 of 9 pairs, best other 39; winding 12, monomial 16, interfering
  42 all moving; markov 0 of 1792 with 64²−48² = 1792; classes 18/19, 3
  not-Bloch, 22 extended; 1856 = 58·16·2; bound without content; fiber 9;
  parity 58/58; 56 verdict values.
- **The §10 instrument claims** all check out against the receipt: 67 gates all
  passed; 64 falsifiable + 3 forced; 66 mutants all dead and all on target; 41
  anchors = 8 + 20 + 13; 56 flip-probed verdict values; every verbatim consumer
  gate an evaluated gate.

**Zero disagreements.** No delivered number is wrong.

---

## 7. THE ERA-BORN-COMPLIANCE RULING

**The claim does not hold. This unit is born-compliant on the #82 contract, on
#20, on #34, on #91 and on comparator independence — and it is the first v14 unit
of which most of that can be said — but it is not born-compliant on the era,
because #234 is satisfied at gate time and vacated at delivery time, and #62 is
satisfied in name only.**

Met, and demonstrated under attack:

1. **#82** — a hand-rolled argv whitelist (20/20 hostile invocations rejected, no
   abbreviation, no flag=value, no positional), a `--selftest` that runs a real
   derivation and whose writes-nothing I proved by hash manifest, a 66/66 mutant
   harness dead at named targets with artifacts untouched, and registries dumped
   into the receipt.
2. **#34** — 64 of 67 gates carry a declared falsifier; the 3 exceptions are
   exactly the 3 registered forcings, and I fired two of the three myself.
3. **#91** — no git, no subprocess, no worktree read outside the 8 hash-pinned
   sources plus the paper-under-test; the run reproduces **byte-identically** in
   a directory with no version control and again under a changed hash seed. The
   moving-ref class that defeated weld-2 cannot arise here.
4. **#20** — a real instrument, not a claim: every paper numeral must render from
   the receipt, enforced as a gate inside the delivery run, and it caught every
   numeral I moved including all three surprise numbers.
5. **#82-strengthened** — the head is genuinely derived twice with no shared
   literal and no shared helper, and the two-way head probe defeats a coordinated
   flip of both copies.

Not met:

1. **#234 / verdict-in-gate — MAJOR-1.** The head *is* derived twice inside a
   complete-string equality gate; the gate then closes, and the payload is
   serialized from a mutable dict fifty lines later. A four-line post-gate edit
   delivers `R4B-NO-MOTION` in both artifacts at exit 0, and the terminal
   integrity gate — the unit's answer to exactly this attack — confirms the
   corruption because it re-derives from the corrupted bytes rather than from a
   value sealed at gate time. This is the single most serious finding, and it is
   the same disease as weld-2's MAJOR-1 one abstraction level up: last time the
   head was never compared; this time it is compared, and then abandoned.
2. **#62 / verbatim anchors — MAJOR-2.** Bare substring presence, no length, no
   uniqueness, and the parent's `window_sha256_12` field deleted. 12 of 13
   windows reduce to `"the "` undetected, with the output artifact byte-identical
   to the committed one.
3. **#87 / gates bind objects — MAJOR-3.** The internal binding is genuine and
   adversarially confirmed; the *published* 58 rows, the class table and the
   path-value anchor table are unbound, and a control's datum can be shipped
   under a census label at exit 0.
4. **#82 / no dead flags — MAJOR-4.** `--verify-paper [PATH]` is documented,
   accepted, and does nothing; a non-existent PATH is silently swallowed.
5. **#20 residual — MINOR-1.** Numeral-complete, polarity-blind: three prose
   inversions deliver artifacts byte-identical to the committed ones.

The honest summary for the ledger: **the first unit to claim era-level
born-compliance earns it everywhere the era wrote a rule about the *run*, and
loses it at the one place the era has not yet written a rule about — the seam
between the last gate and the bytes on disk.** All four MAJOR items are bounded,
mechanical repairs inside `r4b_momentum_exact.py` (MAJOR-1 and MAJOR-3 are one
mechanism: seal the payload at gate time and re-derive the published tables) plus
one docstring correction; **none touches the census, the convention-selection
identity, the cancellation result, or any delivered number.**

A precedent I would set for the era from MAJOR-1: *a gate that fires on an object
which is still mutable when the artifact is built has not gated the artifact.*
The engraving should require the delivered payload to be sealed — value and
digest — at the moment its last gate passes, and the integrity gate to compare
against that seal rather than against itself.

---

## 8. SCOPE OF THIS REVIEW

I did not adjudicate K1–K4. I recomputed their numbers independently and found
none wrong (§1, §6), but whether the 58-vs-14 comparison is between commensurable
objects, whether "selected-not-declared" is the honest classification of the
fiber-9 choice, whether "cancellation" imports an interference ontology the arena
does not measure, and what §15 requires the SCOPE segment to carry are the
operator and effectus seats' rulings, both of which were frozen while I worked
(`v14/review-r4b-effectus.md`, `v14/review-r4b-operator.md`, commits `a0992ef`
and `02fb227`). I have not read them for adjudication and my findings are
independent of theirs; where they report a *reading* correction, nothing in my
numeric sweep contradicts it — every delivered number reproduces, which is
consistent with a defect of labelling rather than of computation.

Two observations handed to those seats rather than ruled on here: (i) the six
declared controls are measured not Bloch-diagonal by a **break-on-first-failure**
loop (L1407–1417), so the receipt records *that* they fail, never *where* —
`G-NOT-BLOCH-CONTROL` counts controls, not momenta; (ii) `G-MU8-THEOREM-LEGS`
carries a dead `roots` loop (MINOR-6) in the middle of the Kronecker argument's
finite legs, which a reader may mistake for the argument's second leg.

**Repo state at close.** The six object files are byte-unchanged —
`5f8ec142319c`, `53a10e87ec19`, `d33412225949`, `00e7f6ea0f90`, `bcd12bbe6fd8`,
`b9cd2133d961` — re-verified after all work, as are all eight pinned sources
(`1063401c7bb5`, `2959c5a6a84b`, `ffd069ff3eb4`, `3dc1393b0df8`, `3b00a9481b28`,
`3828376b49a6`, `f54fa11dfd07`, and the pin). My only repo write is
`?? v14/review-r4b-instrument.md`. `git status` also shows four files modified by
**other agents in flight**, which are not mine and which I disclaim:
`v14/code/w2_census_exact.py`, `v14/code/w2_census_output.txt`,
`v14/code/w2_census_receipt.json`, `v14/paper-13-weld2-carrier-census.md`. That
set churned during this review: at close it also carries the untracked
`v14/code/giter_exact.py` and `v14/paper-16-gamma-iteration.md`, and at open it
carried untracked `u4_crystals_*` and `paper-14-u4-renewal-crystals.md`, which
have since been committed. None of it touches this unit's objects or sources; all
of my runs were on scratch mirrors containing only the eleven files this unit
reads, so no result recorded here depends on which files happen to be drifting.
No LOG or STATUS edit was made. HEAD advanced from `0d73569` to `02fb227` during this
review (ledger #115–#117, other seats); I confirmed by `git show --name-only`
that none of those commits touches any of my six objects or the eight pinned
sources.
