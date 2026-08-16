# REVIEW — HOR (paper-42) — K3 INSTRUMENT SEAT

**Grade: AWF** (accept with fixes). Four false cardinalities are published in
the sealed receipt and in a PASS transcript line; the E-31 syntax leg scans
106 of the 238 strings it is said to scan and reaches none of the evidence
strings where those four numbers live; and three of three semantic walls pass
a banned claim written as a paper would write it, because all three of their
own controls are derived from their own patterns. Against that: no measured
physics number moved under any probe, the 43-mutant sweep is 43/43 clean at
declared gates with artifacts byte-unchanged, byte reproduction holds twice
from off-tree git-less artifact-deleted trees, every hostile argv exits 2
writing nothing, and all eight direction flips and all five #125 wrappings
died. This is a strong instrument with a measurable and liftable seam.

**Everything below is a candidate reading until adjudication.**

Seat: K3 INSTRUMENT. Authority: HANDOFF-PROMPT.md §4/§9, RUNBOOK through E-33,
`v14/TEMPLATE.md` (`809ebe3514ad`), `v14/code/era_template.py` (`d04a3eb58fbc`).
Execution: scratch only, `/private/tmp/.../scratchpad/hor_k3/`, absolute paths,
rsync mirrors excluding `.git`. Repo writes: this file only.

---

## 1. OBJECT VERIFICATION

Five hashes, re-verified at open and again at close of this seat, unchanged:

| artifact | sha256-12 | lines |
|---|---|---|
| `/Users/felixrobles/workspace/isp/v14/paper-42-hor.md` | `376e29746e39` | 583 |
| `/Users/felixrobles/workspace/isp/v14/code/hor_exact.py` | `00c985939230` | 4932 |
| `/Users/felixrobles/workspace/isp/v14/code/hor_output.txt` | `87ea30df2a92` | 194 |
| `/Users/felixrobles/workspace/isp/v14/code/hor_receipt.json` | `df3549596b4e` | 4695 |
| `/Users/felixrobles/workspace/isp/v14/note-hor-pin.md` | `0cf8515e184f` | 5 |

The two pinned template artifacts also verify at the digests RUNBOOK E-25…E-33
names: `v14/tpl_runbook_addenda.md` `e46c1abf25b2`, `v14/code/era_template.py`
`d04a3eb58fbc`.

## 2. THE CLAIMED COUNTS, VERIFIED FROM LIVE REGISTRIES

| claim | measured | verdict |
|---|---|---|
| 44 gates | ledger 42 rows + `G-FALSIFIER-MOVES` + `G-FALSIFIER-COVERAGE` = 44; `coverage.gates` 44 | TRUE |
| 42 falsified + 2 machine-checked waivers | 43 falsifiers over 42 distinct gates (`G-THE-CONE` carries two); 2 waivers | TRUE as counts; both forcings are tautologies — see MAJOR-5 |
| 43/43 mutants | 43 declared; full out-of-harness sweep, one process each: 43/43 exit 1 at the DECLARED gate, artifacts byte-unchanged | TRUE |
| 18 verbatim anchors, all consumed | `verbatim_anchors.anchors` 18, `consumed` 18; consumption gated | TRUE |
| 30 path-value anchors, all consumed | 30 declared and all value-gated; **13 are never subscripted anywhere after the anchoring loop** | FALSE — see MAJOR-4 |
| 17 reads = 17 recorded, 0 exemptions | `runtime_inputs`: declared 17, `reads_recorded` 17, `distinct_paths` 17, `exemptions_carried` 0 = 15 sources + own source + paper | TRUE as counted; the counter carries an undeclared `.tmp` exemption class — MINOR-6 |
| nine template checks parsed from the reference's own family table, set equality gated | `FAMILIES` in `era_template.py` declares 9 `T-` ids; `implemented_checks()` returns the 9 `CHECK` attributes; set equality is the gate predicate | TRUE |
| S-1 by construction: comparator shares no function, aggregate or literal | AST profile of `build_head` vs `rebuild_head`: 0 shared functions, 0 shared string literals, 0 shared numeric literals, **1 shared module global (`SEGMENT_SEP`)**, 4 head numbers read as builder scalars rather than re-aggregated | Materially sound; the sentence overstates — MINOR-1 |

Receipt shape as delivered: 56 top-level keys, 47 sealed, 8 declared unsealed,
77 measured names, 15 pinned sources.

## 3. WHAT I RAN

- **Byte reproduction ×2**, two seeds, off-tree, git-less, artifacts deleted
  before the run (`tree_A`, `tree_B`; no `.git` in either). Both produced
  `hor_receipt.json` `df3549596b4e` and `hor_output.txt` `87ea30df2a92`,
  byte-identical to the committed artifacts and to each other. 15s per run.
- **The full 43-mutant sweep out of harness**, one process per mutant, from a
  tree holding the committed artifacts. 43/43 exited 1, each at the gate its
  own `Falsifier` row declares, with both artifacts byte-unchanged after all
  43. Independent re-proof: the mutated gate's evidence string differs from
  the clean run's for 42 of 43 (`MUT-STRATUM` moves `per_stratum` detail the
  evidence line does not expose — the sealed target still moves).
- **Hostile argv**, 21 forms (`--help`, `-h`, `--HELP`, `""`, `--`, doubled
  flags, `--mutant` with 0/2 operands, `--mutant=NAME`, `--LIST-GATES`,
  `; rm -rf /`, `--verify-paper` with 0/2 operands and on a missing path).
  Every one exits 2 except the two that exit 1 with a named refusal. Tree
  hash `d39f6b157ba42428` before and after all 21: nothing written.
- **`--selftest` write-nothing by tree hash**: same tree hash before and
  after; refusal message names `T-ANCHOR-CONSUMED`.
- **76 live injections** across four batteries.

## 4. TEMPLATE CONFORMANCE — VERDICT PER FAMILY

Probed against the unit's own implementations, using the published controls in
`v14/TEMPLATE.md` §§2–10. The #269 caveat is honoured: each ABSENT names the
leg probed.

| family | check id | verdict | established by |
|---|---|---|---|
| (a) seal integrity | `T-SEAL-PROMOTION` | **CONFORMS, one leg open** | ADD, EDIT, POST-CLOSE, PHANTOM-GATE all die; the side artifact's promotion window is open (MAJOR-1) |
| (b) transcript bound | `T-TRANSCRIPT-BOUND` | **CONFORMS** | row deleted, PASS→FAIL, twin row, forged-into-`body0`: 4/4 die |
| (c) semantic walls | `T-WALL-SEMANTIC` | **GAP** | re-voiced infinity, re-voiced continuum, hyphenated policed token: 3/3 pass at exit 0 (MAJOR-3); positive leg carried by a parent's quote (MINOR-3) |
| (d) anchors consumed | `T-ANCHOR-CONSUMED` | **CONFORMS on all three published controls** | phantom consumer, consumer-never-reads, wrong-source all die; obligation 6 (meaning not existence) is met by construction but not machine-checked (MINOR-2), and the path-value family carries no consumption check at all (MAJOR-4) |
| (e) claims by equality | `T-CLAIMS-EQUAL` | **CONFORMS** | header swap, row transplant, row swap between two tables, twin claim, unbound extra table: 5/5 die. Greedy header matching is not live here — all 8 paper table headers are distinct |
| (f) referent binding | `T-REFERENT-BOUND` | **GAP** | two cross-universe plants pass at exit 0; 25 of 67 prose numerals fall outside every universe (MAJOR-6) |
| (g) no typed counts | `T-NO-TYPED-COUNTS` | **GAP** | the AST leg scans 106 of 238 handed strings and no evidence string; typed integer offsets publish four false cardinalities (MAJOR-2). Obligation 6 is met: zero numeric literals shared between builder and comparator |
| (h) falsifiers poison | `T-FALSIFIER-POISONS` | **CONFORMS, two legs open** | no-op probe dies; obligation 3 is delegated to the CLI and discharged 43/43 externally, but a neutered real branch leaves the in-process run green (MAJOR-7); both waiver forcings are tautologies (MAJOR-5); obligation 7 fails with (c) |
| (i) read set | `T-READ-SET` | **CONFORMS, one leg open** | RAW-OPEN, DECLARED-NEVER-READ, UNUSED-EXEMPTION, VACUOUS-MODE, ABSENT-OBJECT all die; the comparison is taken three gates early and as a set, not a multiset (MINOR-6) |

**The adoption gate measures identifiers, not teeth.** `G-TEMPLATE-CONFORMANCE`
compares the nine `CHECK` strings against the nine parsed from the reference.
I gutted `SemanticWall.scan`'s negative leg to `hits = []` and
`AnchorSet.verify_consumption`'s to `unconsumed = []`, leaving both `CHECK`
ids in place: both runs completed at exit 0 with the conformance gate green.
This is not charged as a defect — it is exactly what `v14/TEMPLATE.md` §13
says the mechanism cannot do, and the unit quotes that caveat in the paper and
consumes it in the gate's own predicate. It is recorded so the phrase
"adoption is a measurement rather than a claim" is read at its true scope: the
*identifier set* is measured; the *binding* is not.

One latent narrowing: the parse is `re.findall(r'\("[a-i]", ...)`. The
character class caps the family count at nine. A tenth family in a future
reference would be invisible to the parse and the set equality would still
pass. Not live-injectable at the pinned sha — which is itself the correct
defence — but it is a typed cap inside the gate that vouches against typed
counts.

## 5. MAJORS

### MAJOR-1 — the side artifact's promotion window is open; four artifacts' worth of integrity language covers one file
`v14/code/hor_exact.py` `promote()` stages both artifacts, reads both back,
compares both against the sealed render, `os.replace`s both — and then calls
`SEAL.verify_after_promotion(receipt_path, ...)`, which re-reads **only the
receipt**.

Injection E25e — append one line to the staged `hor_output.txt` between the
read-back and `os.replace`, the exact window
`era_template.Seal.verify_after_promotion`'s own docstring names ("a
corruption landed between the read-back and os.replace promotes clean without
it"): **exit 0**, output on disk `ad24ad3fbc86` instead of `87ea30df2a92`.
Injection E25d — the same edit after `os.replace`, before the verify: **exit
0**, output `23c08555b010`. The run then prints
`[PASS] G-ARTIFACT-INTEGRITY :: the promoted receipt was re-read from disk and
every gate-time seal re-verified; receipt <d>, transcript <d>` — and the
second digest is of the in-memory bytes, never of the file.

Compounding it: the receipt's `transcript.digest` is `b2d2b3675d29`, while
`sha256-12(hor_output.txt)` is `87ea30df2a92`. They differ because the sealed
digest is taken over `body0`, the render built **before** `measure_falsifiers`
appends the last two transcript rows — a strict prefix of the promoted bytes.
`G-TRANSCRIPT-BOUND`'s own statement says "the whole transcript rather than a
prefix is digested". No digest of the promoted `hor_output.txt` appears
anywhere in the receipt.

**Provenance ruling.** `era_template.promote` is identical on this point
(`seal.verify_after_promotion({"receipt": receipt_path}, ...)`), and HOR's
`verify_after_promotion` is a faithful copy of the reference's body. Per
TEMPLATE §1 and §11 this is a **template-level residual with HOR exposure**,
not a defect of HOR's own hand. It should be routed to the successor register
and fixed in the reference; HOR's own liftable repair is smaller.

**Repair.** (i) Re-verify the side artifact from its promoted path — compare
`sha256(open(side_path,'rb').read())` against the digest of `ttxt` after
`os.replace`. (ii) Publish that digest as a sealed receipt key. (iii) Either
recompute `transcript.digest` over the promoted `body`, or rename it to
`transcript_prefix_digest` and say which prefix, and drop the word "prefix"
from the gate statement.

### MAJOR-2 — four false published cardinalities, from typed integer offsets the E-31 leg cannot see
`hor_exact.py:4737-4738` publishes
`"published_keys": len(payload) + 9` and `"sealed": len(SEAL.seals) + 8`, and
`:4760` re-evaluates the same two expressions for the gate's evidence string.
Both offsets are over by one at their own evaluation point, and the second
evaluation compounds it because `seal_shape` has since been inserted into
`payload` and sealed.

| quantity | `seal_shape` says | `G-SEAL-TOTALITY` evidence says | the promoted file has |
|---|---|---|---|
| published receipt keys | 57 | **58** | **56** |
| sealed keys | 48 | **49** | **47** |

The transcript line at `hor_output.txt:190` reads
`[PASS] G-SEAL-TOTALITY :: published keys 58, sealed 49, declared unsealed 8, undeclared 0`
about a file with 56 keys and 47 seals. This is LOR MAJOR-3's shape ("seals 37
vs 36") and NDEP MAJOR-1's shape, cited in `v14/TEMPLATE.md` §8 and §2, inside
a unit claiming full E-25…E-33 conformance.

The **integrity partition is sound** — I recomputed it: `set(receipt) − (sealed
∪ unsealed ∪ {seal_manifest})` is empty and no sealed key is absent, so
obligation 3 of family (a) is genuinely met. Only the cardinalities are false.
`totals.gates = len(LD.rows) + 5` = 44 happens to be correct.

Why nothing caught it: `CountRegistry.audit_module` walks `ast.Call` nodes
named `stmt`/`claim`/`gate` and inspects `node.args` for
`isinstance(arg, ast.Constant)`. These offsets are integer literals in a dict
literal — outside the scan entirely — and the evidence string that carries
them is a `%`-BinOp, also outside it. Injections E31c/E31d changed `+5`→`+500`
and `+9`→`+900`: **both runs exit 0** and publish the fabricated numbers.

**Repair.** Compute both at the door from the live objects
(`len(body)`, `len(SEAL.seals)`) after the manifest is attached, and derive the
evidence line from the same two values. Register the three offsets as measured
names so E-31 governs them.

### MAJOR-3 — three of three semantic walls pass a banned claim in the paper's own voice, and all three controls are written from their own patterns
The negative legs are fixed regex blacklists of 13, 12 and 1 patterns. Two
sentences a paper would actually write, appended to `paper-42-hor.md` and run
through the delivery path:

- *"Taken over all patches at once the family has a completed member, an arena
  of unbounded extent that contains every finite patch as a sub-patch, and that
  totality is what the laws above are ultimately about."* → **exit 0**
  (`WALL-NO-ACTUAL-INFINITY` green). This is an explicit actual-infinity claim,
  the one thing the pin bans outright and R1's seal forbids.
- *"As the spacing is refined without bound the lattice becomes a smooth arena
  and the tick becomes a derivative, so the ordinary field-theoretic
  description is recovered."* → **exit 0** (`WALL-NO-CONTINUUM` green).
- *"Influence travels four sites per-tick on this arena."* → **exit 0**. The
  identical sentence with a space instead of the hyphen dies. The policed
  token is the literal `per tick`; `canon()` folds whitespace and markdown but
  not hyphens.

The cause is family (c) obligation 7, which HOR does not meet: `MUT-WALL-INFINITY`
injects *"The values converge to a limit of the family…"*, `MUT-WALL-CONTINUUM`
injects *"This is the continuum limit…"*, `MUT-WALL-LICENCE` injects *"…four
sites per tick here."* — each is written from the pattern that catches it.
Zero of three walls carries a control phrased as a paper would phrase it, so
all three green badges are LOR #269 badges.

What *is* solid: the #125 legs are strong. The same banned sentence
line-wrapped, blockquoted, list-item-prefixed, emphasis-marked and
capital-initial all die (5/5), and a policed sentence carrying no rendered
claim dies, as does one carrying a rendered claim plus a false extra value.

**Repair.** Add one control per wall written against the disease rather than
the pattern — the three sentences above will do. Widen the infinity leg to
noun forms (`completed member`, `unbounded extent`, `totality`, `all patches at
once`) and the continuum leg to `refined without bound`, `becomes a derivative`,
`smooth arena`. Normalise `-` to a space in `canon()` before the policed-token
match, or make the token a regex `per[- ]tick`.

### MAJOR-4 — thirteen of thirty path-value anchors are never consumed, and the family has no consumption gate
`AnchorSet.verify_consumption` binds the 18 verbatim windows to their named
consumer gates. The 30 `(path, value)` pairs get no equivalent. Thirteen occur
exactly once in the whole 4932-line source — in the declaration table itself —
and are never subscripted by any measurement:

`PV-POT-PLACEMENTS`, `PV-POT-SHAPES`, `PV-POT-BL`, `PV-POT-BL-MERGED`,
`PV-POT-BL-ORBITS`, `PV-POT-BL-IDENT`, `PV-POT-BL-SHAPES`, `PV-R5-CONNECTIVE`,
`PV-R5-CIRCULANTS`, `PV-ACT-IDX-L2`, `PV-ACT-IDX-L4`, `PV-ACT-IDX-L8`,
`PV-ACT-IMAGE`.

By E-28's own standard ("an anchor is consumed or it is decoration") these
thirteen are decoration. The mitigation is real and should be stated: all 30
*are* value-gated at `G-PATH-VALUES`, so a drift in a parent's receipt at those
paths still kills the run. They are checked but inert, not unchecked.

The paper does not overclaim here — its consumption sentence is scoped to
"window". The **delivery summary's** phrasing "18 verbatim + 30 path-value
anchors ALL consumed" is what is false, and it should be corrected before
adjudication cites it.

**Repair.** Either consume the thirteen (`PV-ACT-IDX-*` are the natural
predicate for the merging-index law the census turns on), or drop them, or add
a `verify_consumption` for the path-value family with a declared inert list
carrying reasons.

### MAJOR-5 — both "machine-checked forcings" are unfalsifiable by construction
`hor_exact.py:4552-4556`:

```
forcings = {"G-FALSIFIER-MOVES": len(moves) == len(F),
            "G-FALSIFIER-COVERAGE":
            "G-FALSIFIER-COVERAGE" in (set(LD.names())
                                       | {"G-FALSIFIER-COVERAGE"})}
```

The second is `X in (S ∪ {X})` — true for every `S`. The first is also always
true when evaluated, because `prove_moves` raises on any failure and therefore
returns exactly `len(F)` rows or does not return. #34 admits waivers "only as
machine-checked forcings"; a predicate that cannot be false is not a check.

I confirmed the *gate* has teeth — forcing the coverage entry to a literal
`False` dies at `T-FALSIFIER-POISONS :: waivers with no machine-checked forcing`
— so the mechanism is live and only its inputs are vacuous.

**Repair.** Force `G-FALSIFIER-COVERAGE` against the denominator `H.coverage`
actually used (return `fired` from `coverage()` and assert membership in the
returned set), and force `G-FALSIFIER-MOVES` on the row-by-row move proofs
rather than on a length that cannot differ.

### MAJOR-6 — a false number rides a foreign noun into the referent gate, and a third of the paper's prose numerals are outside every universe
`ReferentRegistry._universe_of` returns the **first** universe whose noun
matches, in dict insertion order (`THE-CONE`, `THE-STABILITY-SWEEP`,
`THE-CLOSURE-CENSUS`, `THE-ARENA`). Two plants, each a false statement about
the census wearing an earlier universe's noun:

- *"At every depth the census carries 256 sealed laws."* → **exit 0**. `depth`
  binds `THE-CONE`; 256 is a cone value.
- *"Across the arms the census carries 64 sealed laws."* → **exit 0**. `arms`
  binds `THE-STABILITY-SWEEP`; 64 is a stability value.

Coverage, measured with the registry's own regexes over its own `prose_only`
text: 67 prose numerals present, `referents.occurrences_checked` = 42. The 25
unchecked sit in 8 sentences that match no universe noun. Four of those eight
carry load-bearing head numbers (`54`/`10` unmoved-and-moved, `10 of 18`
quantifiable, `5`/`400`/`0` direct-limit, `1`/`13` winding classes) — **all
four are rendered claims and are bound by equality at `G-PAPER-CLAIMS`**, so
the layered defence holds for them. That mitigation is why this is MAJOR-6 and
not the headline. The two genuinely unbound numerals are `#42` and `#373` in
the status block — identity metadata, not measurements.

**Repair.** Check a sentence against **every** universe whose noun it carries,
not the first; and either add a catch-all universe or gate the count of
unbound prose numerals at zero.

### MAJOR-7 — the in-process falsifier badge does not certify death at the declared gate
`FalsifierHarness.prove_moves` digests `f.probe(payload)` — a **re-implementation**
of the mutation — before and after. The reference's `run_one` instead applies
the falsifier and asserts `died_at == f.gate`. HOR's harness therefore proves
that a lambda moves a dict, not that the `mut()` branch in the instrument does
anything at all.

Injection: neuter the real branch (`if False and mut("MUT-REACH"):`) leaving
the probe intact. The delivery run completes at **exit 0** with
`G-FALSIFIER-MOVES` green and `mutants.rows` still crediting `MUT-REACH` with
`dies_at: G-ONE-TICK-REACH`. Only the external CLI catches it
(`--mutant MUT-REACH` → exit 1, "did not die").

The unit **discloses this**: `mutants.death_at_the_named_gate_is_verified_by`
reads `"THE---MUTANT-NAME-RUNS-WHICH-EXIT-1-AT-THAT-GATE-WRITING-NOTHING"`. And
I discharged it: 43/43 out of harness, at declared gates, artifacts unchanged.
So the obligation is met in fact; what is wrong is that a green in-process badge
reads as if it certified it.

`audit_descriptions` is also weaker than the reference: the reference flags a
mutant branch if **any** statement is a constant-boolean assign or constant
append; HOR flags only if **every** statement in the body is. Two of HOR's own
branches are the shape `v14/TEMPLATE.md` §9 quotes verbatim as sentinel —
`MUT-TYPED`'s `off = off + ["line 0: 'injected typed numeral 7'"]` and
`MUT-FALSIFIER`'s `sentinels = sentinels + ["injected"]` — each injecting into
its detector's own output rather than exercising the detector. Both escape both
audits because the value is a `BinOp`, and the receipt publishes
`sentinel_shaped_branches: 0`.

**Repair.** Adopt the reference's `run_one` (or run the real branch inside
`prove_moves` and assert the gate id), restore the per-statement AST rule, and
replace `MUT-TYPED` with a mutant that plants a numeral in a scanned string.

## 6. MINORS

- **MINOR-1 — the S-1 sentence overstates by one literal and four counts.**
  AST profile: builder and comparator share no function, no string literal and
  no numeric literal, but they do share the module global `SEGMENT_SEP`
  (`" -- "`, `hor_exact.py:3476`), used by both to join segments. Moving it to
  `" ~~ "` moves both renderings identically, so `G-VERDICT-EQUALITY` cannot
  see it — `G-PAPER-CLAIMS` catches it instead. Separately, four head numbers
  are read as builder-computed scalars rather than re-aggregated from rows:
  `arena.coins`, `the_cone.amplitude_supports_escaping_the_cone`,
  `loop_stability.full_family_mismatches`, and the product
  `shapes_compared × coins_in_the_full_sweep`. I tested the sharpest of these
  — a post-seal edit of the escape scalar — and it **died** at
  `G-VERDICT-EQUALITY`, because the builder draws from `CNT` and the comparator
  from the payload. So the mechanism is sound; only "shares … no literal" and
  "recomputes every count by its own aggregation" are false as written.
- **MINOR-2 — "consumed for its existence rather than its meaning stops the
  run" is not machine-checked.** `verify_consumption` tests only
  `consumer ∈ read_by`. Replacing a consumer's `anchor_has(...)` with a bare
  `anchors.read(...)` and a hard-coded `True` runs at **exit 0**. The
  behaviour is met by construction everywhere in this unit; the sentence
  claims a gate that does not exist.
- **MINOR-3 — the infinity wall's positive leg can be carried by a
  quotation.** `positive=[r"not a limit", …]` is matched over the whole paper.
  Deleting the paper's own *"it is not a convergence, not a limit and not an
  object"* leaves R1's blockquote *"The two constant values are not a limit and
  not a convergence."* to satisfy it: **exit 0**. Family (c) obligation 4 asks
  that deleting the wall's own verdict fail. Anchor the positive leg to the
  paper's voice, i.e. to `strip_declaring`'s output with the anchors removed.
- **MINOR-4 — a gate statement can describe a different check.** Prefixing
  `G-HOMOLOGY`'s statement with *"this gate re-derives the arena from the
  parents own bytes and confirms every link operator is unitary"* runs at
  **exit 0**. Statements are digested into the ledger chain (so the receipt
  hash moves and the drift is detectable by comparison against the committed
  artifact) but are published in **neither** artifact — `payload["gates"]`
  carries only `gate`/`passed`/`evidence`. A reader auditing the receipt alone
  cannot see what any gate claims to do.
- **MINOR-5 — `--selftest` returns 1 on pass and 1 on failure.** Both branches
  of `main()`'s selftest arm `return 1`; only the stream text differs. I
  confirmed by making the corrupted anchor not raise: still exit 1. A caller
  cannot distinguish "refused correctly" from "did not refuse" by exit code.
  Return 0 on the refusal.
- **MINOR-6 — the read set is compared three gates early, as a set, with an
  undeclared exemption class.** `G-READS-DECLARED` is ledger row 41 of 42;
  `G-TRANSCRIPT-BOUND`, `G-FALSIFIER-MOVES` and `G-FALSIFIER-COVERAGE` fire
  after it, and `READS.active` is set `False` at it, so the whole promotion
  path's I/O is outside the recorder. A repo read planted after that point runs
  at **exit 0**. `gate_at_close` builds a `Counter` and then compares
  `set(seen)` against `set(want)`, so a second read of an already-declared path
  is invisible (**exit 0**, both artifacts moved) — while the gate statement
  says "the multiset of relative paths is compared with the declaration". And
  `not p.endswith(".tmp")` silently exempts a whole suffix class beside a
  published `exemptions_carried: 0`. **All three are inherited verbatim from
  `era_template.ReadSet.gate_at_close`**, whose own docstring makes the same
  multiset claim; HOR's body differs only in the exception class, the type
  annotations and one return key. Route to the successor register.

## 7. INJECTION LEDGER

76 injections. 60 caught, 13 uncaught, 3 inconclusive (patch anchor missed or
raised before reaching a gate; re-run or superseded). Every "uncaught" below
completed at exit 0.

| # | injection | leg probed | result |
|---|---|---|---|
| 1–4 | seal: post-close edit / post-close add / seal-after-close / phantom gate | (a) 1–5 | 4 CAUGHT |
| 5 | staged side-artifact tamper before `os.replace` | (a) 6 | **UNCAUGHT** |
| 6 | side-artifact edit after `os.replace` | (a) 6 | **UNCAUGHT** |
| 7–10 | transcript: row deleted / PASS→FAIL / twin row / forged into `body0` | (b) | 4 CAUGHT |
| 11 | re-voiced actual-infinity claim | (c) 1,7 | **UNCAUGHT** |
| 12 | re-voiced continuum claim | (c) 1,7 | **UNCAUGHT** |
| 13 | policed token hyphenated | (c) 1,3 | **UNCAUGHT** |
| 14 | positive leg satisfied by the parent's quote | (c) 4 | **UNCAUGHT** |
| 15–19 | banned sentence flat / line-wrapped / blockquote / list item / emphasis | (c) 3 | 5 CAUGHT |
| 20 | banned sentence, capital initial, re-voiced | (c) 2 | CAUGHT |
| 21–22 | policed sentence with no rendered claim / with a false extra value | (c) 6 | 2 CAUGHT |
| 23–24 | phantom consumer gate / consumer that never reads | (d) 2,3 | 2 CAUGHT |
| 25 | anchor needle pointed at the wrong pinned source | (d) 4 | CAUGHT |
| 26 | existence-only consumption (read, discard, hard-code True) | (d) 6 | **UNCAUGHT** |
| 27–31 | header swap / row transplant / row swap between tables / twin claim / unbound extra table | (e) | 5 CAUGHT |
| 32–33 | cross-universe plant via `depth` / via `arms` | (f) | 2 **UNCAUGHT** |
| 34 | numeral in a sentence with no universe noun | (f) | **UNCAUGHT** |
| 35 | typed numeral in a `claim()` string | (g) 5 | CAUGHT |
| 36 | typed numeral in a `%`-formatted evidence string | (g) 5 | **UNCAUGHT** |
| 37–38 | `+5` offset → `+500`; `+9` offset → `+900` | (g) 2,5 | 2 **UNCAUGHT** |
| 39 | no-op falsifier probe | (h) 2 | CAUGHT |
| 40 | neutered real mutant branch, probe intact | (h) 3 | **UNCAUGHT** in process; CAUGHT by the CLI |
| 41 | waiver forcing set to literal `False` | (h) 6 | CAUGHT |
| 42 | raw `open()` of an undeclared repo file inside the window | (i) 1 | CAUGHT |
| 43 | declared-but-never-read source | (i) 4 | CAUGHT |
| 44 | exemption carried and never used | (i) 3 | CAUGHT |
| 45 | duplicate read of an already-declared path | (i) 2 | **UNCAUGHT** |
| 46 | repo read after the read gate | (i) 2 | **UNCAUGHT** |
| 47 | read of a `*.tmp` repo path | (i) 3 | **UNCAUGHT** |
| 48–50 | `--verify-paper` on empty / on another unit's paper / on a JSON receipt | (i) 5 | 3 CAUGHT |
| 51–58 | direction flips: headline word; `0`→`3` mismatches in the fence; the same in prose; `9`→`17` VERBATIM in the fence; the same in prose; census row dropped; `CLOSURE-ARTIFACT`→`SURVIVES-VERBATIM`; `NOT-A-RELATIVITY-CLAIM` deleted | #20, (e), (f) | **8 CAUGHT, 8/8** |
| 59 | `SEGMENT_SEP` moved | S-1 | CAUGHT (by `G-PAPER-CLAIMS`, not by the comparator) |
| 60 | post-seal edit of the one head scalar the comparator does not re-aggregate | S-1 | CAUGHT |
| 61 | gate statement replaced by a description of a different check | E-26 | **UNCAUGHT** |
| 62 | `SemanticWall.scan` negative leg gutted, `CHECK` id kept | template adoption | **UNCAUGHT** |
| 63 | `verify_consumption` gutted, `CHECK` id kept | template adoption | **UNCAUGHT** |
| 64–76 | 21 hostile argv forms (13 distinct refusal paths) + `--selftest` write-nothing | #82 | all exit 2 or a named exit 1; tree hash unchanged |

## 8. WHAT HELD

Recorded because a hostile seat that reports only the seam misreports the unit.

- **#91 at its own hands.** Two off-tree, git-less, artifact-deleted seeds
  reproduce both artifacts byte-identically. No subprocess, no git, no
  unpinned read whose product a gate consumes; all 15 sources sha-gated at
  `G-SOURCES` before anything else runs; a needle pointed at the wrong pinned
  file dies immediately.
- **The mutant contract.** 43/43, one process each, at the DECLARED gate, exit
  1, artifacts byte-unchanged after the whole sweep. Independently re-proved by
  evidence-string comparison against the clean transcript: 42/43 move the
  gate's own published evidence.
- **#82.** 21 hostile argv forms, no write on any of them, no silently-ignored
  flag, `--verify-paper` refusing on absent, empty and wrong-type objects.
- **The direction-flip defence is the strongest leg in the unit.** All eight
  flips died, including the two that matter most — the headline word and the
  `9-VERBATIM`/`17-VERBATIM` census split — in both the fenced block and the
  prose, through two independent gates.
- **The claims gate is table-sighted and two-way**, and the greedy
  header-matching weakness that SEC-2 found is not live here: all eight paper
  table headers are distinct.
- **#125 normalisation is sound**: 5/5 wrappings of a banned sentence died.
- **The ledger chain recomputes** (`head` = `recomputed` = `48881be707a070ac`),
  and the seal partition is genuinely total — recomputed at the door from the
  live key set, with zero undeclared and zero absent keys.

## 9. THE SEAM RULING

The seam is **the boundary between what the instrument measures and what it
says about what it measures**. Every uncaught injection in §7 falls on the
same side of it: the machinery is honest about numbers it computes and
overstated in the sentences that describe the computing. `G-SEAL-TOTALITY`
partitions the receipt correctly and mis-states its size by two. The read set
is genuinely recorded at the accessor and is compared with the wrong operator,
three gates early. Every falsifier does move something and the badge that says
so certifies a surrogate. The walls do normalise correctly and ban a word list.
The comparator is genuinely independent and the sentence claiming it is false
by one literal.

No physics moved. Across all 76 injections I found no measured quantity of
this unit to be wrong, no theorem mis-stated, and no headline reachable that
the run did not earn. The four false numbers are all cardinalities of the
instrument's own bookkeeping.

Two of the four openings — the side-artifact promotion window and the read-set
comparison — are **inherited verbatim from `v14/code/era_template.py`** and
should be charged to the template and its successor register, not to HOR. The
remaining repairs are local and liftable, and none of them requires re-running
the physics.

**Recommended disposition: AWF.** Repair orders in priority order: MAJOR-2
(false cardinalities), MAJOR-3 (wall controls and patterns), MAJOR-1 (side
artifact, with the template residual routed), MAJOR-6 (referent universes),
MAJOR-4 (inert path-value anchors), MAJOR-5 (waiver forcings), MAJOR-7
(harness), then the six MINORs.

---

*Recomputations performed by this seat: 76 live injections, 43 out-of-harness
mutant runs, 21 hostile argv invocations, 2 off-tree byte reproductions, 1
selftest tree-hash proof, plus static AST and registry measurements of the
receipt, the paper and both instruments. Counts stated above are computed, not
carried. Scratch: `/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/hor_k3/`, under 5G.*
