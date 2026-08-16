# REVIEW — REC (paper-41), K3 INSTRUMENT SEAT

*The era audit: seal, coverage, injections, CLI, #91 at its own hands, and the
seam ruling. Object verified open and close. Everything below is a candidate
reading until adjudication.*

---

## GRADE: **ACCEPT-WITH-FIXES (AWF)**

No measured physics quantity is wrong, and I could not move the verdict. The
reconstruction, the residue index, the minimality census and the obstruction
all survive every attack I could build. The instrument reproduces
byte-identically twice off-tree from artifact-deleted, git-less trees using
`--run`; `--selftest` writes nothing, proved by tree hash; the CLI whitelist
holds at 18 of 18 hostile argv; there are **no vacuous modes**; and all 38
falsifiers die at their declared gate, one process each.

Against that: the **wall family is defeated 11 times out of 11** by paraphrase;
the **falsifier family's honesty legs are imported and not called**, and the
unit's own move-proof is a tautology that cannot fail — six of the 38 recipes
do not move the target they name; a **wholly fictitious falsifier row ships at
exit 0**; the **sole waiver is untrue** (I built the falsifier it says cannot
exist and it dies at the waived gate); the **S-1 AST check is name-based** and
four separate leaks walk past it; the head is bound to the receipt at 12 of its
26 numerals, so `9-OF-9`, `0-SURVIVE` and `3-OF-6` can each be moved in the
renderer and the paper together at exit 0 with a byte-identical transcript; and
one **sealed leaf publishes a proxy that differs from the quantity its own name
and the paper's sentence denote** (`certified_reconstructions_refused = 3`;
the comparator, actually run, refuses 4).

Twelve majors, seventeen minors. Every one is a perimeter repair of one to
eight lines. None touches a physics number.

**SEAM RULING.** The seam this unit sits on — *the first unit built on
`era_template.py`* — is **ADOPTED IN MECHANISM, PARTIAL IN EXERCISE**. Six of
the nine families are imported *and used with teeth against this unit's own
object*: (a) seal, (b) transcript, (d) anchors, (e) claims, (f) referents, (i)
read-set. Family (e) is the strongest implementation I have probed in the
corpus — seven distinct forgery shapes all die. Families (c) and (h) are
imported and **carried rather than used**: (c)'s ten patterns are a
finite blacklist wearing a regex's clothes, and (h)'s two honesty legs
(`FalsifierHarness.run_one`, `FalsifierHarness.audit_descriptions`) are never
called — `audit_descriptions`, run by me against `rec_exact.py`, flags three of
this unit's own hooks. Family (g) is adopted at the `stmt` door and open at
every other door. **Per LOR #269, I state the leg for every ABSENT below.**

---

## 0. THE OBJECT, VERIFIED OPEN AND CLOSE

| artifact | claimed | measured (open) | measured (close) | lines |
|---|---|---|---|---|
| `v14/paper-41-rec.md` | 58b08940d04c | 58b08940d04c | 58b08940d04c | 360 |
| `v14/code/rec_exact.py` | ba77c08c81a2 | ba77c08c81a2 | ba77c08c81a2 | 2,703 |
| `v14/code/rec_output.txt` | 16b7a64c6156 | 16b7a64c6156 | 16b7a64c6156 | 39 |
| `v14/code/rec_receipt.json` | 2428d901e5c5 | 2428d901e5c5 | 2428d901e5c5 | 1,162 |
| `v14/note-rec-pin.md` (pin) | 0b51e47b7b4b | 0b51e47b7b4b | 0b51e47b7b4b | 5 |

Five for five, both ends. The repo tree was untouched by this seat except for
this file.

### Every claimed count, recomputed from the live registries

I instantiated `full_run(write=False)` in-process and read the registries
themselves, never the receipt's own report of them.

| claim | live registry | verdict |
|---|---|---|
| 37 gates | `len(LD.rows)` = 37; names unique; 37 `[PASS]` lines | ✓ |
| 37 sealed + 0 declared-unsealed | `len(SEAL.seals)` = 37, `len(SEAL.unsealed)` = 0; payload − sealed − manifest = ∅ | ✓ |
| 38 falsifiers | `len(MUTANTS)` = 38, 38 distinct names | ✓ |
| 38/38 die at their declared gate | 38 subprocesses, exit 0, `died == declared` on all | ✓ |
| 38/38 with move-proofs | **the move-proof cannot fail; 6 of 38 do not move their target** | ✗ (MAJOR-2) |
| 1 waiver with forcing | 1 waiver; **the forcing is the literal `True`, and the waived gate is falsifiable** | ✗ (MAJOR-4) |
| 7 anchors located + consumed | 7; needles 64–146 chars against the 40-char floor; each consumer ∈ `read_by` | ✓ |
| 2 walls / 10 patterns / 3 standing sentences | 2 / 10 / 3 | ✓ (but see MAJOR-1) |
| 6 referent universes / 45 occurrences | 6 / 45 | ✓ |
| 144 paper numerals, 0 unbacked | 144 / 0 | ✓ (but see MINOR-6/7) |
| S-1 regions builder-24 / reconstructor-9 / comparator-6 / stripper-4 | `{builder: 24, comparator: 6, reconstructor: 9, stripper: 4}` | ✓ |
| S-1 AST-disjoint, MUT-S1 | violations ∅; MUT-S1 dies at `G-S1-DISJOINT-CODE` with the target moved | ✓ (but see MAJOR-6) |
| JSON round-trip gated | `json_round_trip_stable: true`, inside `G-RECEIPT-EXACT`'s predicate | ✓ |
| (also) 28 table rows / 8 claims / 3 fences | 28 / 8 / 3 | ✓ |
| (also) seal manifest | 37 sealed keys over 35 distinct gates, 0 unsealed | ✓ |

---

## 1. THE BATTERIES RUN

All work off-tree at `…/scratchpad/rec_k3/` (peak 460 MB, well under 5 G),
absolute paths, `/opt/homebrew/bin/python3.13`.

- **Byte reproduction ×2** — `seedA`, `seedB`: `rsync` mirrors with `.git`
  excluded, `rec_output.txt` and `rec_receipt.json` **deleted**, run with
  `--run`. Both emit `16b7a64c6156` / `2428d901e5c5`. No git, no network, no
  repo path. #91 holds at this unit's own hands.
- **`--selftest` writes nothing** — tree hash of 1,100+ files before and after:
  `c76af9530a71b973` both times. Its three legs are real (forged transcript row
  → `T-TRANSCRIPT-BOUND`; post-seal add → `T-SEAL-PROMOTION`; sealed value edit
  → `T-SEAL-PROMOTION`).
- **The full 38-falsifier sweep, out of harness, one process each** — 38
  subprocesses, all exit 0, all `died == declared`, all `hook True`. Table in §5.
- **An independent re-proof of the move-proof** — 39 in-process runs plus 9
  fresh-process re-runs, digesting each declared target with my own digest
  function against a clean baseline (MAJOR-2).
- **84 code- and paper-side injections** across four batteries.
- **18 hostile argv**, **16 vacuous-mode runs**, **10 declared scrambles**.

Total: **219 instrument executions** and roughly **60 independent static
recomputations** (AST scans, numeral censuses, allow-set reconstructions,
API-surface diffs).

---

## 2. MAJOR FINDINGS

### MAJOR-1 — The reading walls are defeated by paraphrase, 11 times out of 11 · family (c) · `T-WALL-SEMANTIC`

`WALL_DERIVED` (6 patterns) and `WALL_PARENTS` (4) are regexes, case-folded and
#125-normalised — the template's obligations 1–3 and 5 are met, and the vacuity
leg holds. But the patterns are a **finite phrase list with alternation**, and
every natural re-voicing of a delivered finding walks through. I appended one
sentence to the paper per probe; nothing else changed.

| appended sentence | inverts | result |
|---|---|---|
| `A single history suffices to reconstruct the cast.` | `PER-HISTORY=0-OF-5,856` | **PASS, exit 0** |
| `The actors are derived, and nothing is left to declare.` | the residue index 12 | **PASS, exit 0** |
| `The record names the direction classes.` | the named obstruction | **PASS, exit 0** |
| `The counts alone recover the cast.` | the level-zero arm | **PASS, exit 0** |
| `The cast was derived in full.` | the qualifier | **PASS, exit 0** |
| `The reconstruction leaves no residue.` | the residue | **PASS, exit 0** |
| `EPR's audit makes the record a complete description of the history.` | the parent-scope wall | **PASS, exit 0** |
| `The bare record determines the coordinate.` | §2's fifth row | **PASS, exit 0** |
| `Every actor can be read off one history's record.` | the corpus-level fact | **PASS, exit 0** |
| `No declaration is needed at all.` | the whole §5 | **PASS, exit 0** |
| `The reconstruction is complete: the coordinate comes back too.` | the headline | **PASS, exit 0** |
| `Nothing whatever is declared.` (control) | — | dies, `G-PAPER-WALLS` |
| `The whole theory is derived.` (control) | — | dies, `G-PAPER-WALLS` |
| `Local realism is restored on the measured arms.` (control) | — | dies, `G-PAPER-WALLS` |
| the same, blockquoted (`> …`) (control) | — | dies (#125 leg good) |
| the same, line-wrapped in house style (control) | — | dies (#125 leg good) |

**11 of 11 paraphrases pass; 5 of 5 literal forms die.** The mechanism is
alive; its coverage is a blacklist. The mechanics that the panels bought — case
fold, markdown prefixes, line wrapping — all hold; what does not hold is the
pattern set.

**The #269 caveat, at its sharpest here:** the unit's only wall falsifier,
`MUT-WALL`, truncates the paper's own standing sentence — which is derived from
the wall's own positive pattern, and which happens to land on negative pattern
1. So the sweep's green badge on `G-PAPER-WALLS` exercises **one of ten**
patterns and **zero of three** standing sentences as a deletion. No control is
written by another hand (obligation 7, unmet).

**Repair.** (i) Widen each pattern to the verb/tense/number families a paper
uses: `is|was|are|were|has been`, `cast|actors|theory|arena|coordinate`,
singular *and* plural of `coordinate(s)|direction(s)`, and the
`suffices|is enough|is sufficient|recovers` family with the subject on either
side (`X suffices to reconstruct Y` as well as `reconstruct Y from X`).
(ii) Add one falsifier per pattern, each phrased as a paper would phrase it and
written from the *finding*, not from the regex. (iii) Add one falsifier that
deletes a standing sentence entirely (both copies) so the positive leg is
exercised on its own.

---

### MAJOR-2 — The E-32 move-proof is a tautology; 6 of 38 recipes do not move the target they name · family (h) · `T-FALSIFIER-POISONS`

`run_mutant()` (line 2581) reads:

```python
    try:
        R, _TR, _LD, _SEAL, _d = full_run(write=False, mutant=name)
        after = ET.digest(R.get(target))
    except ET.CheckFail as exc:
        died = exc.check
        after = "REFUSED-BEFORE-THE-KEY-WAS-PUBLISHED"
    moved = (after != before)
```

`Ledger.gate` raises `CheckFail` on any failing gate, and **every falsifier is
designed to fail a gate**. So the `try` branch never completes, `after` is
always the literal string, and `moved` is **unconditionally True**. The
move-proof E-32 was bought for cannot fail at this unit's hands.

I measured what it would have caught. I exported the payload as it stood when
the gate refused (a one-line patch in a scratch copy) and digested each
declared target with my own function against a clean baseline:

| recipe | declared target | independently measured |
|---|---|---|
| `MUT-CAST` | `reconstruction` | **NO — SENTINEL** (moves only the local `cast_exact`; the key was sealed 16 lines earlier at 1216) |
| `MUT-WALL` | `walls` | **NO — SENTINEL** (`R["walls"]` is `w.seal_value()` — the pattern list, independent of the scan) |
| `MUT-SEAL-ADD` | `verdict` | **NO — SENTINEL** (adds `R["forged_finding"]`; `verdict` is untouched) |
| `MUT-TARGETS` | `anchors` | **ABSENT AT DEATH** (dies at gate 12; `anchors` first exists at gate 31) |
| `MUT-ANCHOR` | `anchors` | **ABSENT AT DEATH** (dies at gate 2) |
| `MUT-TRANSCRIPT` | `transcript` | **ABSENT AT DEATH** (`R["transcript"]` is assigned *after* its own gate, line 2426) |
| the other 32 | — | **YES**, all verified with an independent digest |

Each of the six was re-confirmed in a **fresh process** (my first pass ran them
in one process and `MUT-ANCHOR-CONSUMER`'s global mutation contaminated five
later rows — see MINOR-13, which that accident proves).

So: 32 of 38 are honest falsifiers by the era's own definition; 6 name a target
their recipe does not move, and the harness reports `moved True` for all six.

**Repair.** (i) In `run_mutant`, compute `after` from the payload as it stood at
refusal (export `R` to a module attribute, or have `full_run` attach the partial
payload to the `CheckFail`), so `moved` can be False. (ii) Re-point the six:
`MUT-CAST` → move `reconstruction` (e.g. drop an actor from `rec["cast"]`
*before* the seal, which is what `MUT-TAU` already does — so re-target
`MUT-CAST` to a key it does move, or delete it as a duplicate of `MUT-TAU`);
`MUT-WALL` → declare target `paper_claims`/`paper_coverage`, or publish a scan
result in `R["walls"]` so the key can move; `MUT-SEAL-ADD` → declare its target
as the added key, or add a `seal_manifest` leaf; the three ABSENT-AT-DEATH rows
→ declare a target the run has already published at their gate (`sources` for
`MUT-ANCHOR`, `disjoint_code` or `arena` for `MUT-TARGETS`, `read_set` for
`MUT-TRANSCRIPT`), or move the target's assignment above its gate.

---

### MAJOR-3 — A wholly fictitious falsifier ships at exit 0 · family (h)

I added one row to `MUTANTS` — `("MUT-SENTINEL", "G-THE-CONNECTION",
"connection", "a sentinel that names a target it never moves")` — and wrote **no
implementation at all**: no `mut("MUT-SENTINEL")` call anywhere in 2,703 lines.

**Exit 0.** All 37 gates green. The delivered receipt publishes 39 falsifier
rows and `T-FALSIFIER-COVERAGE` reports the higher count. `G-PROVENANCE` checks
only that the named gate is in `allowed` and that the target string is
non-empty; nothing checks that a hook exists for the name.

The CLI does catch it (`--mutant MUT-SENTINEL` would report `died None`), but
the **delivery path does not**, and the delivery path is what produces the
sealed artifact.

**Repair, four lines.** In the provenance gate, AST-scan the module for the set
of string constants passed to `mut(...)` and require it to equal
`{m[0] for m in MUTANTS}` — both directions, so an orphaned hook also dies.

---

### MAJOR-4 — The unit's one waiver is untrue, and its "machine-checked forcing" is a typed `True` · family (h) obligation 6

```python
    waivers = {"T-FALSIFIER-COVERAGE": "the coverage gate is inside its own denominator"}
    cov2 = HARNESS.coverage(LD, waivers, {"T-FALSIFIER-COVERAGE": True})
```

The template requires "waivers carry machine-checked forcings, not
descriptions". The forcing here is the boolean literal `True`, and
`coverage()` only tests its truthiness. Nothing computes anything.

**And the waiver's claim is false.** I built the falsifier it says cannot
exist: withhold one row (`MUT-CONNECTION`) from the harness list, so a fired
gate is left uncovered. Result: **dies at `T-FALSIFIER-COVERAGE`**, exit 1,
and it moves `R["falsifiers"]` (mutants 38→37, falsified 37→36). That is a
textbook honest falsifier for the waived gate: it names a target, moves it, and
dies at the declared gate. So the gate is falsifiable and the waiver is not
forced.

I also flipped the forcing to `False` as a control: dies at
`T-FALSIFIER-COVERAGE` — the flag is load-bearing as a flag, which is precisely
the problem.

**Repair.** Delete the waiver, add `MUT-COVERAGE-GAP` implementing the recipe
above, and the unit reaches 38 of 38 fired gates falsified with **zero**
waivers. (This is the rare case where the repair *strengthens* a published
count rather than shrinking it.)

---

### MAJOR-5 — The template's own falsifier-honesty AST leg is imported and never called, and it flags three of this unit's hooks · family (h) obligation 4

`FalsifierHarness.audit_descriptions` is the leg the template carries for
E-23's "descriptions matched against code, by AST". `rec_exact.py` never calls
it. I ran it against `rec_exact.py`:

```
line 1006: constant-append sentinel   ->  drifted.append("injected")        # MUT-SOURCE-DRIFT
line 2209: constant-append sentinel   ->  cov.append("injected")            # MUT-COVERAGE
line 2284: constant-append sentinel   ->  bad_types.append("/injected")     # MUT-FLOAT
```

Two of the three have **descriptions that invert their code**:

- `MUT-COVERAGE` is published as *"a numeral backed by nothing is admitted to
  the paper's coverage census"* — the code appends the **non-numeral string**
  `"injected"` to the offender list. No numeral is ever planted in the paper.
- `MUT-FLOAT` is published as *"a non-integer leaf is admitted to the published
  receipt"* — the code appends a **string** to `bad_types`. No float ever
  enters `R`; the recursive type walk is never exercised on a real float.

This is verbatim the SEC-2 MAJOR-7 shape the template quotes
(`floats + ["injected"]` — *"they prove the gate raises when handed a False,
not that it detects the corruption it advertises"*). `MUT-SOURCE-DRIFT` is
half-honest: it also reverses a real digest, so the append is redundant rather
than substitutive.

**Repair.** Call `HARNESS.audit_descriptions(src)` and gate on it (two lines).
Rewrite the two recipes to corrupt the object: `MUT-COVERAGE` plants a numeral
in the paper text handed to `paper_numerals`; `MUT-FLOAT` puts a genuine
`0.5` into a receipt leaf. Both are one-line changes and both then exercise the
real predicate.

---

### MAJOR-6 — The S-1 disjointness check is name-based; four independent leaks walk past it

`audit_regions` flags an `ast.Name` inside an `r_*`/`k_*` function whose id
starts with a forbidden prefix or sits in a **hand-typed** arena blacklist.
Both tests are on identifiers. Each of the following was appended to
`rec_exact.py` and the run **completed at exit 0 and wrote its artifacts**:

| injection | what it does | result |
|---|---|---|
| `_ALIAS_BUILDER = b_declared_actors` + `def r_leaks_via_alias(): return _ALIAS_BUILDER()` | a reconstructor calls the builder through a module-level alias | **PASS, exit 0**, artifacts written |
| `def _bridge_to_the_builder(): return b_declared_actors()` + `def r_leaks_via_bridge(): return _bridge_to_the_builder()` | a one-hop helper | **PASS, exit 0** |
| `def r_knows_the_answer(rec): return len(rec["cast"]) == 9 and len(rec["tokens"]) == 27` | the declared arena's numbers **typed** into a reconstructor | **PASS, exit 0** |
| `def r_reads_the_declared_collinearity(): return B_COLLINEAR_FLAT` | a module-level builder constant carrying the declared classes `("ROW","COL","DIA","DIA")` — **not in the blacklist** | **PASS, exit 0** |
| `_K_ALIAS = b_declared_actors` + `def k_leaks_via_alias(): return _K_ALIAS()` | the comparator calls the builder through an alias | **PASS, exit 0** |

The blacklist is `{SITES, SITE_INDEX, NACT, I7_LINKS, CLASS_NAMES, CLASS_DIR,
CLASSES, CELLS, CELL_INDEX, DIM, ACTORS, SCRAMBLE_MULT, SCRAMBLE_ADD, _RAW,
_B_PERMS}`. Two module-level builder constants are missing from it:
`B_COLLINEAR_FLAT` (line 217) and `B_SEEDS_PER_ROUND` (line 219). `ACTORS` and
`_RAW` are listed and do not exist in the module — the list is maintained by
hand and has already drifted in both directions.

Also unpoliced: `region_census` counts reconstructor functions (9) and the gate
statement interpolates that count, but **no gate compares it to anything**, so
adding a tenth reconstructor changes only the published number.

**One genuine strength of record.** The *load-bearing* form of the typed-literal
attack does die: replacing the derived clique-size selection
`if len(c) == top` with the declared constant `if len(c) == 6` **dies at
`G-CONTROL-SYNTHETIC-SUCCEEDS`**, because the 2+2+2 / 4+4+4 / 5+5+5 synthetic
arms have casts of other sizes. The synthetic control arm has real teeth
against arena constants smuggled into the live path. That is the best-designed
control in the unit and it should be said plainly.

**Repair.** (i) Derive the arena set instead of typing it: every module-level
assignment above the `SECTION B` marker, by AST. (ii) Add a reachability leg:
compute the *call closure* of each `r_*`/`k_*` function through module-level
names and flag any `b_*`/`s_*` reached at any depth, and any name bound to a
`b_*`/`s_*` function object. (iii) Flag integer constants inside `r_*` bodies
that equal a live arena cardinality (`NACT`, `DIM`, `2*DIM//NACT`, `len(I7_LINKS)`).

---

### MAJOR-7 — The head is bound to the receipt at 12 of 26 numerals; three headline fields move at exit 0

`G-VERDICT-EQUALITY` parses 12 declared `HEAD_FIELDS` back out of the emitted
string and compares each with the receipt leaf it names. That leg is real and
`MUT-HEAD` exercises it. But the three verdict segments carry **26 numeral
positions**, and `k_parse_head` takes only the *first* digit group per field, so
fourteen are unchecked — including `SITE-SET=9-OF-9`, `LINK-STRUCTURE=27-OF-27`,
`MENU=3-OF-6`, the `108-ARENA-COHERENT` half of `NAMING`,
`LEVEL-0-COUNT-FIELD=36`, `BLOCK-MINIMAL=27-OF-27-…-0`,
`COLLAPSE-THRESHOLDS`, `CRYSTALLIZATION…=5`, `RECORD-COLLISIONS=39-…-180`,
`SURPLUS=1-4-4` and the whole of `CONTROLS=261-…-0-SURVIVE-AND-4-OF-7`.

For each, moving the value in the **renderer and the paper together** passes
every gate:

| injection | delivered head says | receipt says | result |
|---|---|---|---|
| `SITE-SET=9-OF-9` → `9-OF-8` (renderer + paper) | 9 of 8 | `arena.sites` 9 | **PASS, exit 0**; transcript **byte-identical** to the committed `16b7a64c6156` |
| `CONTROLS=…-0-SURVIVE` → `3-SURVIVE` (renderer + paper) | 3 scrambles survived | `control_scrambled.survivors` **0** | **PASS, exit 0**; transcript byte-identical |
| `MENU=3-OF-6` → `4-OF-6` (renderer + paper) | 4 of 6 | `menu.matched` has **3** entries | **PASS, exit 0**; transcript byte-identical |

The `0-SURVIVE` case is the sharpest: the delivered verdict block asserts that
three scrambled records reached the declared cast, while
`G-CONTROL-SCRAMBLED-FAILS` passes on `survivors == 0` two hundred lines
earlier, and the two artifacts are shipped side by side without contradiction.

Paper-side-only flips of the same fields die correctly at `G-PAPER-CLAIMS` (the
fence multiset leg is good — `9-OF-9`→`8-OF-9`, `0-SURVIVE`→`3-SURVIVE`,
`RESIDUE-INDEX=12`→`11`, `CAST-SIZE=9-DERIVED`→`9-DECLARED` all die). The hole
is specifically the renderer↔receipt binding.

**Repair.** Extend `k_parse_head` to return *all* digit groups per field and
extend `HEAD_FIELDS` to name a receipt leaf for each of the 26 positions. This
is mechanical and the parser already exists.

---

### MAJOR-8 — A sealed leaf publishes a proxy, and the proxy is not the quantity its name denotes

```python
    teeth = [r for r in syn_rows
             if r["certificate"] == "CERTIFIED" and r["cast_size"] != NACT]
```

The receipt publishes `comparator_teeth.certified_reconstructions_refused = 3`
and the paper's §6 says *"three reconstructions carry the reconstructor's own
certificate and are still refused by the comparator, because their casts are
not this arena's"* — immediately after *"the teeth are measured, not asserted"*.

The comparator is **never asked**. The synthetic arm calls
`k_agree_sets(rr["cast"], sstars)` — against each synthetic arena's *own*
stars — and `teeth` is then inferred from a cardinality (`cast_size != 9`),
which is #87's own prohibition (gates bind objects, not cardinalities).

I ran the comparator against the declared cast, which is what the sentence
describes:

| arm | certificate | cast size | `k_agree_sets(cast, dec_cast)` |
|---|---|---|---|
| 2+2+2 | CERTIFIED | 6 | False — refused |
| 3+3+3 | CERTIFIED | 9 | **False — refused** |
| 4+4+4 | CERTIFIED | 12 | False — refused |
| 5+5+5 | CERTIFIED | 15 | False — refused |

**Four**, not three. The 3+3+3 arm certifies with a cast of nine that is *not
this arena's nine*, and it is exactly the case the paper's clause ("because
their casts are not this arena's") is about; the cardinality proxy silently
drops it.

Under the reading the key name and the paper's sentence carry, `3` is a wrong
delivered number. Under the narrower reading "certified reconstructions whose
cast size differs from nine", `3` is right and the key is misnamed. Either way
the leaf and its prose do not describe the same set. **This is the one candidate
false delivered numeral I found in the unit**, and I flag it as such for the
adjudicator rather than settling it from this seat.

**Repair, two lines.** Compute `teeth` by actually calling
`k_agree_sets(rr["cast"], dec_cast)` per arm and counting `cert and not agree`.
The published number becomes 4, the paper's "three" becomes "four", and the
sentence "the teeth are measured, not asserted" becomes true.

---

### MAJOR-9 — Nothing binds the transcript's numerals to the receipt · family (b)

`Transcript.bind` reconciles the transcript against the **ledger**, both ways,
evidence included — that leg is real (`MUT-TRANSCRIPT` and a dropped-row
injection both die at `G-TRANSCRIPT-BOUND`). But the ledger's evidence strings
and the receipt's leaves are two independent renderings of the same
measurements, and **nothing compares them**.

I changed one evidence expression —
`"reconstructing histories %d of %d" % (depth_hits, len(corp))` →
`… len(corp) - 1` — so the delivered `rec_output.txt` reads
`reconstructing histories 0 of 5855` while `R["minimality_per_history"]`
reads `slots: 5856`.

**Exit 0.** Both artifacts promoted, mutually contradicting, all 37 gates
green. This is NDEP MAJOR-2's shape exactly (*"the transcript says 99 where the
receipt says 45; the two published artifacts contradict each other on the
unit's own headline census and nothing notices"*), reproduced in the first unit
built on the template written to kill it.

**Repair.** Give `gate()` the same treatment `G-VERDICT-EQUALITY` gives the
head: parse the numerals out of each finished evidence line and require each to
be a value the gate's own sealed key carries. Twelve lines, and the machinery
(`k_parse_head`) already exists.

---

### MAJOR-10 — Typed numerals: the concatenation dodge, and five in the §4 table · family (g)

`REG.stmt` refuses a template that types a numeral, and `MUT-TYPED` dies
correctly — a directly typed numeral inside a `stmt` call dies at
`T-NO-TYPED-COUNTS`. Two doors are open beside it.

**(a) Concatenation.** `("… it refuses 3 reconstructions …") + REG.stmt("{teeth} …")`
passes both the runtime guard (which only inspects the template it is handed)
and `audit_module` (which only inspects string constants that are **direct
arguments** to `stmt`/`claim`). **Exit 0**, with a typed numeral inside a
published, sealed gate statement.

**(b) The tables and fences are outside the scan.** `audit_module` is called as
`REG.audit_module(src, statement_callers=("stmt", "claim"))` — `CL.table` and
`CL.fence` are not in the tuple. The §4 depths table (line 2025) carries five
typed numerals in string literals plus two typed integer keys:

```python
    [("crystallization time", "the naming, given the cast",
      com(c_by[("C1", 5)]) + " at 5", com(c_by[("C2", 5)]) + " at 5", "stratified"),
     ("collapse threshold", "coherence width, given the cast",
      com(w_by[("C1", 4)]) + " at 4", com(w_by[("C2", 4)]) + " at 4", "3, 4, 5"),
     …
```

`"3, 4, 5"` is the whole C3 column of the collapse-threshold row — a hand-typed
literal where `", ".join(str(w) for w in w_vals)` is available and already
measured. This is SEC-2's realized harm in the same shape (a typed table
column); here the values are true, so nothing has moved, but the paper's §8
claim — *"no typed numeral in anything the unit vouches for"* — is over-broad,
and the unit vouches for these rows by gating them against the paper.

**Repair.** Add `"table"`, `"fence"` and `"row"` to `statement_callers`;
interpolate the five; make the counts arrive from `w_vals` and the two
distributions.

---

### MAJOR-11 — The published control denominator 261 is a function of the declared scramble, and the SWAP arm is silently capped

The paper states *"261 corruptions of these bytes were run through the
reconstructor and its comparator"* and the head carries
`CONTROLS=261-SCRAMBLES-…`. I recomputed the arm across ten declared
arena-blind coordinates:

| `(mult, add)` | REPLACE | DROP | SWAP | total |
|---|---|---|---|---|
| (5, 11) — **the declared one** | 54 | 27 | 180 | **261** |
| (1, 0) | 54 | 27 | 173 | 254 |
| (2, 5) | 54 | 27 | 180 | 261 |
| (4, 1) | 54 | 27 | 173 | 254 |
| (7, 3) | 54 | 27 | 180 | 261 |
| (8, 17) | 54 | 27 | 179 | 260 |
| (10, 2) | 54 | 27 | 176 | 257 |
| (13, 25) | 54 | 27 | 176 | 257 |
| (20, 7) | 54 | 27 | 176 | 257 |
| (25, 26) | 54 | 27 | 177 | 258 |

The REPLACE and DROP arms are invariant; the SWAP arm — and therefore the
published total — is **not**. `G-STRIPPING-EQUIVARIANT` prices the coordinate
for the derived *cast* (12 trials, 0 failures) and the paper says *"the
permutation the strip chose is therefore priced, not trusted"*. That price is
not paid for the control denominators. Under §15 the number 261 is
arena-relative and is not marked as such.

**And there is a silent cap.** The SWAP loop carries `if u > 8: break`, so it
tries 180 of the **315** swaps available at the declared coordinate. The
honest denominator for the whole arm is 54 + 27 + 315 = **396**, of which 261
are run. Neither the cap nor the number 396 appears in the paper or the
receipt. Standing discipline: no silent caps.

**Repair.** Either lift the cap (`if u > 8` → no cap; the arm is cheap) and
publish the full denominator, or declare the cap in the receipt with its reason
and disclose it in §6; and label the control counts arena-relative, or index
the swap arm by something coordinate-free.

---

### MAJOR-12 — Direction-bearing prose outside the claim registry is unbound; three inversions ship byte-identical

Six claims and three fences are licensed, and their occurrence counts are
exact — the twin-claim probe (flip one of the two copies of the standing
sentence) dies correctly at `G-PAPER-CLAIMS`. Everything else in the prose is
bound only by the walls (MAJOR-1) and the referent registry (numerals only).

| paper edit | inverts | result |
|---|---|---|
| *"The first three rows are **set equality, not isomorphism**"* → *"**isomorphism, not set equality**"* | §2's central methodological claim — the difference between "the same sets" and "merely isomorphic ones", which is the paper's own headline distinction | **PASS, exit 0, artifacts BYTE-IDENTICAL** |
| *"it is that the record **does not carry** them"* → *"**does carry** them"* | §7's statement of the residue — the unit's verdict qualifier | **PASS, exit 0, artifacts BYTE-IDENTICAL** |
| *"**Overlap** is what carries identity, and overlap is **waste**"* → *"**Disjointness** is what carries identity, and overlap is **cheap**"* | §4's explanation of why no history reconstructs | **PASS, exit 0, artifacts BYTE-IDENTICAL** |

Byte-identical delivery means these are invisible to every downstream check
including the byte-reproduction battery.

Related and equally unbound: **the anchor's meaning can be inverted around a
byte-perfect window** (r6bp M3's shape). I rewrote §1's framing —
*"Which is why the object EPR measured is the **right** frame… Two structures
decide everything, and both are measured:"* → *"the **wrong** frame… **Neither**
structure decides anything, and **neither** is measured, **contrary to**:"* —
leaving the two quoted anchors untouched. **PASS, exit 0, byte-identical.**

**Repair.** Promote the load-bearing direction sentences of §§2, 4, 5 and 7
into `CL.claim(...)` (they are already single-threaded sentences; six to ten
additions), and add a wall pattern for the set-equality/isomorphism pair.

---

## 3. MINOR FINDINGS

**MINOR-1 — `G-STRIPPING-TOTAL`'s statement over-claims, and the leak it names walks past it.** The
statement says the strip leaves *"no actor, no site (a PAIR of integers) and no
direction"*. A site is a pair of integers only in the *unindexed*
representation; `SITE_INDEX[x]` is a single integer. I made the strip emit, per
event, the three **site indices** — depth 3, integer leaves, the whole cast
handed over in the clear. `G-STRIPPING-TOTAL` **passes**; the run dies two gates
later at `G-STRIPPING-EQUIVARIANT` (12 trials, 12 failures). The gate that
claims totality does not have it; a different gate saves the unit. *Repair:*
add a leg that the emitted token alphabet has cardinality `DIM` and that no
block has size outside the measured block-size census, or state the gate's
actual guarantee (types and depth) in its statement.

**MINOR-2 — The eraser's own non-triviality is ungated.** Setting
`SCRAMBLE_MULT, SCRAMBLE_ADD = 1, 0` makes `pi` the identity, so the "scrambled"
token ids *are* the cell indices. `R["stripping"]["scramble_is_a_permutation"]`
is still true and no strip gate objects; the run dies only at `G-PAPER-CLAIMS`,
and only because a *control denominator* moved (261→254, MAJOR-11). §1's claim
that the indices are "permuted by a declared arena-blind map" would be false
while every strip gate was green. The equivariance leg limits the harm to
presentation. *Repair, one line:* gate `pi != tuple(range(DIM))` and publish the
derangement count.

**MINOR-3 — The eight declared coverage exemptions are all decorative, and one is dead code.**
`EXEMPT = {33, 35, 38, 41, 21, 373, 14, 25}` — I recomputed the set of paper
numerals not in `backing`: it is **empty**. Every one of the eight is already
backed, so **no exemption is load-bearing**, and nothing gates that an
exemption is used (family (i) obligation 3, family (g) obligation 4). The
dictionary also contains `33000: "unused"` followed immediately by
`EXEMPT.pop(33000)`. *Repair:* gate that every declared exemption is used, and
delete the ones that are not, and the dead entry.

**MINOR-4 — The coverage allow-set is polluted by digest fragments.** `harvest()`
mines `\d+` out of every string in the receipt, including 18 digest-like
strings. Of the 96 admitted values, **30 are produced by no integer
measurement**, and **18 come from digest fragments alone** — 16, 22, 47, 58,
77, 81, 331, 550, 615, 5884, 6156, 7135, 7442, 8813, 8940, 281289, 6696223,
9879984. Two probes exploit it: appending *"Only 5,884 remain."* or *"The
instrument counted 615 of these."* passes at exit 0 (the run reports 145
numerals and objects to none). A sentence carrying a universe noun is caught by
the referent gate instead (*"The corpus holds 5,884 slots."* dies), so the two
gates partly cover each other — but a nounless sentence slips both. This is
family (f) obligation 6's disease one gate over. *Repair:* harvest integers
from integer leaves only; whitelist digest-shaped strings explicitly.

**MINOR-5 — 91 spelled numerals in the paper's prose are scanned by nothing.**
`paper_numerals` matches digits. The prose carries 91 number words, several
load-bearing: *"a cast of six, nine, twelve and **fifteen** actors"* (the
synthetic cast sizes, which the receipt carries as 6/9/12/15 — and the digit
`15` **appears nowhere in the paper**, so that delivered value exists only as a
word), *"one history — **twelve** division events long"*, *"**three**
reconstructions carry the reconstructor's own certificate"* (the MAJOR-8
number), *"its **nine** record blocks are pairwise disjoint"*, *"an
**eight**-block record reconstructing a **six**-actor cast"*, *"FAC's
admissible menu has **six** members"*. This is ACT MAJOR-5's finding. *Repair:*
add a spelled-numeral alternation to `NUM`, or a second census over number
words.

**MINOR-6 — `paper_numerals` misses 50 of 194 digit tokens, concentrated in the verdict blocks.**
The lookbehind `(?<![\w.,/-])` excludes any numeral preceded by a hyphen, which
is most of the hyphenated head. Per fence: 10 of 15 counted, 6 of 14, 6 of 12 —
**18 of 41 verdict-block numerals are uncounted**, including `108`, `145`,
`180`, `5,856` and both `0`s. The gate's own statement says *"every one of the
paper's 144 numerals — fenced blocks, verdict blocks and tables included"*,
which is true of the 144 it counts and misleading about the census's reach.
(The fences are separately bound by multiset equality, so nothing escapes
*undetected*; the census is what over-states.) *Repair:* allow a hyphen in the
lookbehind, or state the exclusion.

**MINOR-7 — Two windows after the read-set gate are open.** `G-READS-AT-THE-ACCESSOR`
is gate 35 of 37. I planted (a) a raw `open()` **after** `RS.gate_at_close(...)`
and before `RS.active = False`, and (b) a read of the live 453 KB `v14/LOG.md`
after `RS.active = False`. **Both pass at exit 0**, artifacts byte-identical.
Nothing in the delivered instrument reads there, so this is latent, but it is
LOR MAJOR-4's shape one gate later and it is a #91 hole. *Repair, one line:*
move `RS.active = False` below the last gate and re-gate the read set at
`T-FALSIFIER-COVERAGE`.

**MINOR-8 — `require_object`'s absent-object leg is unreachable.** Line 1018 reads
the paper; line 1020 calls `ET.require_object("--run", path, paper)`. The
`os.path.exists` branch can therefore never fire — a missing paper crashes at
the read with an uncaught `FileNotFoundError` (exit 1, no artifacts touched); a
directory gives `IsADirectoryError`. The template's `ABSENT-OBJECT` positive
control is dead at this unit's hands. The **empty**-object leg *is* live and
correct: every mode refuses (see §5). *Repair:* call `require_object` before
`read_text`.

**MINOR-9 — `require_object` is passed the literal `"--run"` in every mode**, so
`--no-write` and `--selftest` both report *"`--run` ran on empty text"*.
Cosmetic; misleads a reader of the refusal.

**MINOR-10 — The side artifact is verified after `os.replace`, with no rollback.**
`ET.promote` re-verifies the **receipt** from disk (`verify_after_promotion`),
and REC adds its own re-read of `rec_output.txt` in `main()` — a good addition
that the template does not supply. But it runs *after* promotion. I forged a
transcript line into the promoted text: the corrupted `rec_output.txt`
**reached disk** (`9ad792993ced`), the run then refused with
*"promoted transcript bytes differ from the gate-time seal"*, exit 1 — and the
corrupted artifact **stays there**, with both `.tmp` files already unlinked in
the `finally`. This is SMU MAJOR-3's shape (TEMPLATE §11's registered
extension). *Repair:* verify the side artifact from the staged `.tmp` before
`os.replace`, as the receipt is; or keep a rollback copy.

**MINOR-11 — `falsifiers.falsified = 37` counts gate *names*, one of which never fires.**
`coverage()` returns `len({f.gate for f in rows})` = 37 distinct gate names
targeted — including `T-SEAL-PROMOTION`, which is a family check id, not a
ledger gate. The honest statement is: 37 gates fired, **36** carry a falsifier,
1 is waived. The sealed leaf reads as though all 37 were falsified. Inherited
from the template's return shape; REC publishes it. *Repair:* return
`len(targeted & fired)`.

**MINOR-12 — `G-RECONSTRUCTION-TARGETS-TOTAL` publishes a regex artifact and types a spelled count.**
Its evidence is `"targets %d" % len(re.findall(r"the [a-z ]+", a_pin))` — a
count of `the <lowercase words>` runs in the anchor, which happens to be 5 and
is not a count of targets. Its statement (a raw string, not `REG.stmt`) types
the spelled numeral *"five"*, which `DIGITS` cannot see. *Repair:* count the
five required tokens found, and interpolate.

**MINOR-13 — The mutant harness is not re-entrant.** `MUT-ANCHOR-CONSUMER`
assigns `ANCHORS[0].consumer = "G-CORPUS-SHAPE"` on the **module-level** list,
and nothing restores it. Running two mutants in one process poisons every later
one: in my first move-proof pass, five subsequent recipes all died at
`G-ANCHORS-CONSUMED` instead of their own gates. The CLI runs one mutant per
process so the delivered battery is safe, but any future in-process sweep is
not. *Repair:* deep-copy `ANCHORS` inside `full_run`, or restore in a `finally`.

**MINOR-14 — Three referent universes are padded with obfuscated constants.**
`CELLS` admits `len(pi) // len(pi)` (= 1) and `len(rec["cast"]) // 3` (= 3);
`CAST` admits a bare literal `2`. These are typed constants wearing a
measurement's clothes, they are invisible to `G-NO-TYPED-COUNTS` (which scans
only `stmt`/`claim` arguments), and each one widens the set of numerals that
can be written about cells and actors. *Repair:* name them through
`REG.measured` with a real provenance, or drop them.

**MINOR-15 — `MUT-CAST` is a near-duplicate of `MUT-TAU`.** Both are credited to
`G-CAST-DERIVED` with target `reconstruction`; `MUT-TAU` moves the key and
`MUT-CAST` does not (MAJOR-2). Two rows, one honest falsifier. The published
count 38 is therefore 37 distinct honest recipes at best.

**MINOR-16 — `CountRegistry.exempt_token` is never called** and
`typed_counts.exemptions` ships as `[]` — correct, but the published field then
proves nothing, and the parallel `EXEMPT` dictionary (MINOR-3) is maintained
outside the registry that exists for it.

**MINOR-17 — The `--render` mode returns before every paper gate.** It is a
faithful renderer (its four tables reproduce the paper's byte for byte, which I
checked) and it refuses on an empty paper, so it is not a vacuous mode. But it
exits at line 2065 having fired 26 of 37 gates, and it is not labelled as a
partial mode in the CLI usage string. Cosmetic.

---

## 4. TEMPLATE CONFORMANCE — PRESENT / ABSENT PER FAMILY

Per §1 of `TEMPLATE.md` and the #269 caveat: **the leg probed is named for
every ABSENT.**

| family | check | verdict at REC | leg probed |
|---|---|---|---|
| **(a) SEAL INTEGRITY** | `T-SEAL-PROMOTION` | **ABSENT** (the disease is not present) | All four lethal forms die: a top-level key added after `verify_at_promotion` → `T-SEAL-PROMOTION`; a sealed value edited after its gate → `T-SEAL-PROMOTION`; a **post-close** edit injected through `promote`'s `tamper` hook, between read-back and `os.replace` → `T-SEAL-PROMOTION` (i.e. `verify_after_promotion` is live); a seal naming a gate that never ran → `T-SEAL-PROMOTION`. 37 sealed / 0 unsealed, totality recomputed at the door from the live key set. **Residual:** the side artifact (MINOR-10). |
| **(b) TRANSCRIPT BOUND** | `T-TRANSCRIPT-BOUND` | **PARTIALLY PRESENT** | Forged row → dies; **dropped** row → dies; chain recomputed from the rows. But the *receipt↔transcript* leg is absent: a forged evidence numeral ships in both artifacts contradicting the receipt at exit 0 (**MAJOR-9**). |
| **(c) SEMANTIC WALLS** | `T-WALL-SEMANTIC` | **PRESENT** | 11 of 11 re-voiced/paraphrased violations pass; 5 of 5 literal controls die. Mechanics (regex, case fold, #125 wrapping, non-vacuity, positive leg) all good; **coverage** is the defect, and no control is written by another hand (**MAJOR-1**). |
| **(d) ANCHORS CONSUMED** | `T-ANCHOR-CONSUMED` | **ABSENT** for the named legs | 7 anchors, both sides gated under one canonicalisation, needles 64–146 chars over a 40-char floor, one accessor, `read_by` recorded, consumption verified against the ledger. All consumers rewritten to a gate that **ran but never subscripted** → dies; a needle truncated to 24 chars → dies at `G-ANCHORS-LOCATED`. Six of the seven enter a real predicate (`carrier_nums[0] == DIM`, `w_vals == anchor_w`, `c1c2 == anchor_c`, the `"three"`/`"six"` and `"does not declare"` tests). **Residual:** meaning inverted *around* a byte-perfect window (MAJOR-12's second half). |
| **(e) CLAIMS BY EQUALITY** | `T-CLAIMS-EQUAL` | **ABSENT** | The strongest family here. Header swap → dies; row transplanted between tables → dies; a duplicated legitimate row → dies; an extra fence → dies; a **deleted** fence → dies; an unrendered table added to the paper → dies (`paper tables bound by nothing`); one copy of a twice-licensed claim forged → dies (exact occurrence counts, not a floor of one). Info-string change on a fence correctly tolerated. |
| **(f) REFERENT BINDING** | `T-REFERENT-BOUND` | **ABSENT** for the named legs | Cross-universe plant (*"The cast holds 5,856 actors"*) → dies; an unmeasured `A of B` pair → dies; an in-universe value the run never measured → dies; the same plant wrapped as a list item and as a blockquote → both die. Prose-only, **and** rendered table rows stripped as well — a genuine strengthening over the template. **Residuals:** spelled numerals (MINOR-5), padded universes (MINOR-14). |
| **(g) NO TYPED COUNTS** | `T-NO-TYPED-COUNTS` | **PRESENT** | A numeral typed directly into a `stmt` template dies. But the concatenation dodge passes at exit 0, and `table`/`fence` are outside `statement_callers` — five typed numerals live in the §4 table (**MAJOR-10**); spelled and integer literals are unscanned everywhere (MINOR-5, MINOR-14). |
| **(h) FALSIFIERS POISON** | `T-FALSIFIER-POISONS` | **PRESENT, most exposed family** | `run_one` never called; `audit_descriptions` never called and flags 3 hooks, 2 with inverted descriptions (**MAJOR-5**); the move-proof is unconditionally True and 6 of 38 recipes do not move their target (**MAJOR-2**); a falsifier with no implementation ships (**MAJOR-3**); the one waiver is untrue and its forcing is a literal (**MAJOR-4**). **What is right:** all 38 die at their declared gate and never earlier, one process each; the coverage denominator does include the coverage gate itself. |
| **(i) READ SETS** | `T-READ-SET` | **ABSENT** for the named legs | `sys.addaudithook` installed at the accessor; a raw `open()` outside the helper is seen (`MUT-READ` dies); declared-but-never-read also fails; multiset comparison at the last gate that reads. **No vacuous modes** — every mode refuses on an empty paper and touches no artifact. No subprocess, no git, no unpinned repo read. **Residuals:** the two closing windows (MINOR-7), the unreachable absent-object leg (MINOR-8). |

**Import usage, audited adversarially.** REC calls 33 of the template's 45
public members and reaches four more transitively through `ET.promote`
(`Seal.close`, `Seal.manifest`, `Seal.verify_at_promotion`,
`Seal.verify_after_promotion`) — so the seal family is genuinely exercised, not
merely imported. Genuinely uncalled: `FalsifierHarness.run_one`,
`FalsifierHarness.audit_descriptions` (both MAJOR-5/MAJOR-2),
`CountRegistry.exempt_token` (MINOR-16), `ReadSet.exempt`,
`Seal.declare_unsealed` (correct — nothing is unsealed), `Ledger.pass_rows`.
The verdict on the question as posed: **the unit uses the template's checks in
seven families and carries them in two**, and the two it carries are the two
whose mechanisms live in methods it never calls.

---

## 5. WHAT IS STRONG — POSITIVES OF RECORD

These should not be lost in the list of majors.

1. **Byte reproduction ×2, off-tree, git-less, artifact-deleted, using `--run`.**
   `16b7a64c6156` / `2428d901e5c5` from both seeds. #91 clean.
2. **`--selftest` writes nothing**, proved by a whole-tree hash
   (`c76af9530a71b973` before and after), and its three legs are real refusals,
   not prints.
3. **The CLI whitelist holds at 18/18.** Every one of `""`, `--RUN`,
   `--run --no-write`, `--run extra`, `--mutant` alone, `--mutant BOGUS`,
   `--mutant mut-cast` (case), `--mutant MUT-CAST extra`, `-`, `--`,
   `--verify-paper`, `--render x`, `--list-gates x`, `--selftest --run`,
   `--rün`, `--run ` (trailing space), and an empty-string argument exits **2**.
4. **No vacuous modes.** Empty paper: `--run`, `--no-write`, `--selftest`,
   `--render`, `--list-gates` all refuse; `--list-mutants` exits 0 without
   touching the paper, correctly. Missing paper and a directory-as-paper both
   fail closed. **No artifact is touched by any failing mode** (verified by
   hash after each).
5. **38/38 falsifiers die at their declared gate and no earlier**, one process
   each, with `hook_used` true — the reachability half of E-32/#34 is sound
   even though the move half is not.
6. **The synthetic control arm has real teeth against smuggled arena
   constants.** Replacing the derived clique-size threshold with the declared
   literal `6` dies at `G-CONTROL-SYNTHETIC-SUCCEEDS`. This is the best control
   in the unit: it prices the reconstructor's generality rather than asserting
   it, and it caught the one S-1 attack that was actually load-bearing.
7. **Family (e) is the strongest claims implementation I have probed** —
   seven forgery shapes, all dead, including the two (deleted fence,
   unrendered table) that defeated EPR and NDEP.
8. **The referent gate strips rendered table rows as well as fences** before
   the prose scan, and says so in a comment with its reason. That is a genuine
   improvement on the template, and it is why the §2/§4/§6 tables are bound
   *more* tightly rather than less.
9. **`G-VERDICT-EQUALITY` binds the verdict word both ways** — the qualifier is
   owed-iff-carried, and the four pre-registered outcome words are shown
   distinguishable on declared probes. #299's feasibility obligation is met: all
   four pin outcomes are in the range of `head_word_of`.
10. **The seal partition is total and clean**: 37 keys, every one sealed at a
    gate that ran, zero declared-unsealed, and the payload minus the manifest is
    exactly the sealed set.
11. **`--render` reproduces the paper's four tables byte for byte**, so the
    prose-renders-from-the-receipt discipline is real and checkable by hand.

---

## 6. THE COUNTS, AS MEASURED

```
gates fired                     37   (ledger rows, names unique, 37 [PASS] lines)
sealed keys                     37   declared-unsealed 0   manifest total ✓
falsifier rows                  38   distinct names 38
  die at declared gate          38/38   (out of harness, one process each)
  move their declared target    32/38   (independently digested; 6 do not)
waivers                          1   forcing = the literal True; the gate IS falsifiable
anchors                          7   located 7, consumed 7, needles 64–146 chars
walls / patterns / positives     2 / 10 / 3
  patterns exercised by a falsifier      1 of 10
  paraphrases that evade                11 of 11
referent universes / occurrences 6 / 45
paper numerals / unbacked      144 / 0
  digit tokens the census skips  50 of 194   (18 of 41 inside the verdict fences)
  spelled numerals unscanned     91
coverage allow-set               96 values, 30 backed by no integer measurement
                                          (18 of those from digest fragments)
regions  builder/recon/comp/strip  24 / 9 / 6 / 4   AST-disjoint by the name test
table rows / claims / fences     28 / 8 / 3
head numerals / bound to a leaf  26 / 12
scramble control trials         261 of 396 available; 254–261 across 10 coordinates
JSON round-trip                gated inside G-RECEIPT-EXACT ✓
```

---

## 7. RECOMPUTATIONS, AND WHAT I DID NOT TEST

**219 instrument executions** and ≈60 independent static recomputations. Every
number in this review was computed by this seat; none was copied from the
receipt except where I name it as the receipt's own claim in order to dispute
it. Where my own harness contaminated a measurement (the in-process move-proof
sweep), I say so and re-ran the affected rows in fresh processes.

**Not tested, and named so the adjudicator can order it:** the physics itself
at a second arena; the reconstruction rule's behaviour on non-multipartite
casts beyond the three refusing synthetic arms; whether the residue index 12
is stable across corpora; concurrent promotion; and the parents' own receipts
beyond the 24 quantities REC consumes.

**Every headline in this review is a candidate reading until adjudication**,
including the grade and including MAJOR-8's charge of a wrong delivered number,
which turns on a reading of the leaf's name that the adjudicator should settle
rather than this seat.
