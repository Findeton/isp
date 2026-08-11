# R5M / paper-23 — INSTRUMENT REVIEW (seat K3)

**Grade: AWF** — accept with fixes.

**Protocol:** v14 ledger #183, row K3 (full-era unit: 56 gates, 25 mutants
outside the harness, 48 anchors, 31 seals, the withholding mechanism audited
hard, G-MUTANT-REGISTRY-TOTAL swept for siblings, injections, hostile argv,
byte ×2 across seeds, the 199-numeral sweep).
**Object at 33da839, hash-verified at open and at close, unchanged by this
review:** `v14/paper-23-measure.md` `9249dda1c0a3`,
`v14/code/r5m_measure_exact.py` `f7de59960fe6`,
`v14/code/r5m_measure_output.txt` `8ee12d000bad`,
`v14/code/r5m_measure_receipt.json` `1e794bd7f5fb`; pin
`v14/note-r5m-pin.md` `e5e09f65f83b`.  All five re-hashed identical after the
work.  All execution off-tree on a provisioned, git-less mirror built with
`git show 33da839:<path>`; concurrent siblings' uncommitted files never read.

**Counts.** 114 instrument process invocations; 140 complete `run()`
executions counting the internal sweeps (`--all-mutants` 25, `--selftest` 3);
41 independent recomputations.  **No false computed number was found.**  Every
finding below is about the strength of a gate or the accuracy of a sentence,
not about a number the unit published.

---

## 1. What passed, measured

| era item | result |
|---|---|
| byte ×2 off-tree, `PYTHONHASHSEED` 0 and 7919 | output `8ee12d000bad`, receipt `1e794bd7f5fb` on **both**, identical to the committed artifacts |
| 25 mutants, **outside** the harness, one process each | 25/25 **DEAD ON TARGET**, artifacts byte-unchanged after every one |
| surviving-mutant convention | a truly neutered mutant prints `ALIVE (expected death at …)` and exits **1**; an off-target death prints `OFF TARGET (want …)` and exits **1**; `--all-mutants` then prints `SOME SURVIVED OR MISSED` and exits **1** |
| 48 anchors, 11 perturbed by me (3 file-bytes, 3 path-value, 5 verbatim incl. the floor) | 11/11 fatal at the named gate, exit 1, nothing written |
| 31 seals + manifest totality | receipt has 42 top-level keys = 31 sealed + 10 declared-unsealed + `declared_unsealed` itself; **0 unaccounted, 0 manifest rows naming an absent key** |
| seal injections (seal removed, phantom manifest row, undeclared extra key, probe-detector disabled, post-write corruption) | 5/5 caught at `G-SEAL-COMPLETE` / `G-ARTIFACT-INTEGRITY` |
| hostile argv, 18 invocations | every malformed form exits **2** with a message; arity enforced on both `--mutant` and `--verify-paper`, including trailing arguments after a consumed value; artifacts unchanged throughout |
| `--list-gates` / `--list-mutants` vs registry vs receipt vs paper | 56 / 56 / 56 / 56 and 25 / 25 / 25 / 25; 56 unique gate ids, 0 FAIL rows |
| bare copy (instrument alone, empty git-less dir) | exit 1 at `G-SOURCES-PINNED`, **1 file present afterwards** — nothing written |
| `--no-write` twin | stdout byte-identical to the committed `r5m_measure_output.txt` |
| `#125` must-not normalisation | a must-not carried in a blockquote, split across a line break, or inside a list item is **caught** (3/3) |
| the delivered product itself | recursive scan of the receipt at **all depths**: zero expectation-valued keys; must-not sweep over the paper: zero hits |

**The paper gates all work on their real paths** — which matters, because
several of their declared mutants do not exercise those paths (§3.2).  I
supplied the missing falsifiers: an unregistered numeral in a non-claim
sentence dies at `G-PAPER-COVERAGE`; a claim corrupted at *every* occurrence
dies at `G-PAPER-CLAIMS-RENDER`; both polarity occurrences flipped dies at
`G-PAPER-POLARITY`; a real banned key and a real banned-named function die at
`G-NO-WILSON-EXPECTATION`.

---

## 2. THE WITHHOLDING-MECHANISM VERDICT

**The withholding is honoured in the product and under-gated in the
instrument.**

*Honoured.* The pin bars the Wilson segment outside the DERIVED case.  The
delivered receipt carries **no expectation-valued key at any depth** (recursive
scan, 42 top-level keys, full tree); the instrument defines no function that
computes one; the paper makes no such claim; the must-not sweep is clean.  The
substantive obligation is met.

*Under-gated.* `G-NO-WILSON-EXPECTATION` scans **only the top level of `S`**
(`[k for k in S …]`) and **only `ast.FunctionDef` names**.  Six injections:

| # | injection | caught? |
|---|---|---|
| W1 | `S["wilson_expectations"]` planted in `finish()`, after the gate | **yes** — `G-SEAL-COMPLETE` (unsealed key), exit 1, wrote nothing |
| W2 | `S["loop_averages"]` (renamed) planted before the gate, unsealed | **yes** — `G-SEAL-COMPLETE`, exit 1, wrote nothing |
| W3 | same renamed key, **sealed** with `SEAL.take(…)` | **NO** — exit 0, delivered |
| W4 | `S["census"]["wilson_expectation_of_the_base_plaquette"]` — the banned token literally in the key, nested one level | **NO** — exit 0, delivered |
| W5 | `def plaquette_mean(S)` computing a loop average, called and discarded | **NO** — exit 0, delivered |
| W6 | `wilson_expectation = lambda S: Fraction(3, 8)`, called | **NO** — exit 0, delivered |
| W7 | a real `S["wilson_expectations"]` planted **before** the gate | **yes** — `G-NO-WILSON-EXPECTATION` |
| W8 | a real `def wilson_expectation(S)` | **yes** — `G-NO-WILSON-EXPECTATION` |

W4 is the sharpest: the gate's own regex matches that key name; the scan never
reaches it.  W6 defeats "the instrument's own syntax tree defines no function
that would compute one" with a function that carries the banned word.

*The prose leg is the weakest side.* Injecting into the paper
"The base plaquette's Wilson expectation is 3/8." **delivers clean** (P9,
exit 0).  Two independent blindnesses combine: `wilson` and `expectation` are
absent from `MUST_NOT`, and the coverage regex
`(?<![\w/.-])(\d+)(?![\w/.-])` cannot see a slash-adjacent numeral, so `3/8`
is never scanned.

*And `MUST_NOT` is narrower than the pin's own wording* ("NO area-law,
string-tension, or **potential** claim").  Offline recomputation of the exact
sweep, 11 probes against the delivered text: `area law`, `string tension`,
`quark` are caught; **bare `confinement`, bare `potential`, `linear
potential`, `the potential energy between`, `the law of the area`, `Wilson
loops obey an area scaling`, and inline-emphasised `the *area* law` / `the
string **tension**` are all NOT caught**.  "The static potential grows
linearly with separation" is precisely a potential claim and passes.

---

## 3. FINDINGS

### MAJOR

**M1 — "the head is derived twice by disjoint routes" is materially false;
the head law is single-sourced, and a corrupted head law delivers clean.**
`head_law()` is one function called by the builder (L2030), by the
reconstruction (L2147) and by the reachability demonstration; its own
docstring says so ("one function, used by the builder, by the reconstruction
and by the reachability demonstration alike").  The paper says the opposite,
twice: the verdict preamble ("derives the head by its own copy of the head
law") and §10 ("carries its own copy of the head law … sharing no format
string, **no helper** and no typed value with the builder").
Demonstrated: corrupting one character inside `head_law`'s format
(`ORBITS`→`ORBITZ`) leaves **`G-HEAD-STRING-EQUALITY` passing** — both
"disjoint" routes move together — and the run dies only because the *committed*
paper still carries the old string (`G-PAPER-CARRIES-THIS-RUNS-VERDICT`).  With
the paper regenerated to match, exactly as a delivery worker would produce it,
**the corrupted head law passes all 58 gates and delivers** (H2, exit 0,
artifacts written).  What *is* genuinely doubled is real and should be claimed
instead: every segment is re-rendered independently, and the census's
`derives` flags are re-inferred from each candidate's own `free_items` rather
than read from the builder's rows.
*Repair:* either (a) give `reconstruct_verdict` a literal second
implementation of the head law — different structure, no shared helper — and
gate the two heads for equality; or (b) rewrite both sentences to
"every **segment** is re-rendered by an independent route and the census's
derive-inference is recomputed; the head **law** is single-sourced and is
gated instead by `G-HEAD-LAW-REACHABILITY`", and rename the gate to
`G-VERDICT-SEGMENTS-AGREE`.  (b) costs nothing and is honest; (a) is stronger.

**M2 — the withholding gate is not total (see §2).**  *Repair:* walk the
payload recursively for banned keys instead of `for k in S`; extend the AST
scan to `ast.AsyncFunctionDef` and to `ast.Assign` targets whose value is an
`ast.Lambda`; add `wilson`, `expectation`, `loop average`, bare `potential`
and bare `confinement` to `MUST_NOT` (bare `confinement` needs one more
`DECLARING` entry for §8's own quoted sentence, and the existing
`NO-CONFINEMENT-CLAIM` already covers the verdict); strip inline `*`/`**`
before the must-not sweep; and make the coverage regex see fractions
(`(?<![\w.-])(\d+)(?:/(\d+))?(?![\w.-])`).  Replace `MUT-WILSON-SEGMENT` —
which currently plants the gate's *finding* (`banned_keys = [...]`), not a key
— with a mutant that actually inserts `S["wilson_expectations"]`, i.e. W7.
The registry's own description of it ("an expectation-valued key appears in
the receipt") describes W7, not the code.

**M3 — six published fractions of the null-dependence table are bound by no
gate; §7 is the unit's "not innocuous" claim.**  The paper contains 12
distinct prose/table fractions; **6 are covered by neither a rendered claim
nor the verdict string**: `79/80`, `25/26`, `23/24` (the NON-FLAT row) and
`1/10`, `4/13`, `3/10` (the DIAGONAL row and the sentence that repeats them).
The coverage regex cannot see slash-adjacent numerals, so none of the 12 is
ever scanned; only the four in `paper_claims` and the seven inside the verdict
string are protected.  Demonstrated from both sides: editing the paper's
NON-FLAT row `79/80`→`78/80` delivers clean (P5); editing the DIAGONAL prose
`1/10`→`1/11`, `4/13`→`4/14` delivers clean (P6); and corrupting the measured
row in the code so the receipt publishes `78/80` while the paper still reads
`79/80` **also delivers clean** (C2).
*Repair:* render all four rows × three columns of the §7 table as claims (12
fragments, e.g. `"| NON-FLAT | %d | %s | %s | %s |"` built from
`measure_comparison`), and make the coverage regex fraction-aware.

**M4 — `G-MUTANT-REGISTRY-TOTAL` is not total.**  It collects only
`mut(<Constant>)` call sites.  Two evasions deliver clean: `_gn = "MUT-" +
"GHOST"; if mut(_gn):` (R2, exit 0) and `if MUT == "MUT-GHOST":` (R3, exit 0)
— the latter also breaks the invariant `mut()`'s own docstring asserts ("the
ONLY mutant switch").  Both directions of the *declared* half are sound: an
unregistered `mut("MUT-GHOST")` dies (R1) and a registry row with no branch
dies (R4), both at the named gate, both writing nothing.
*Repair:* fail on any `mut()` call whose argument is not an `ast.Constant`,
and on any `ast.Compare` whose operand is `ast.Name(id="MUT")` outside the
body of `mut` itself.

**M5 — `G-CHOICE-INVENTORY` binds a cardinality, not rows (#87).**  Its
predicate is `len(vd) == 3 and not bad`.  Moving the verdict-determining flag
off `WHICH CHART GROUP IS DECLARED` and onto `the sets weighed against the
nulls` keeps the count at 3 and **delivers clean** (C1, exit 0).  The whole
table — every fibre and every flag — is a typed literal; `MUT-CHOICE-INVENTORY`
flips one typed flag and is caught only by the same cardinality.
*Repair:* gate per row against a measured predicate — a row is
verdict-determining iff re-running the affected measurement under its other
declared instance moves a published number (both instances are already
measured for the chart group, the carrier and the null, so the predicate is
computable from what the run already has).

### MINOR

- **m1 — the instrument's module docstring says "seven candidate sources"**
  (L6); the census is 8, in the verdict, the paper and the receipt.  A stale
  count of exactly the class the worker self-caught.  *Repair:* render it, or
  say "the census runs the pin's three candidates and five more".
- **m2 — `S["totals"]["late_gates"] = 2` is typed and goes stale silently.**
  Adding a third closing gate leaves the receipt publishing `late_gates: 2`
  with 2 named closing gates while 3 actually close (R5, exit 0).
  `closing_gates["names"]` is typed too.  *Repair:*
  `late_gates = len(LD.rows) - len(S["gates"])` computed after the closing
  gates, or derive both from one list.
- **m3 — "56 gates" understates the true total, which is 58.**  The two
  closing gates are disclosed in the same section, so this is a wording fix,
  not a false number.  *Repair:* "56 gates in the sealed ledger and two
  closing gates that cannot be inside it".
- **m4 — the waiver ledger's fourth class is unreachable.**  §10 says the
  ledger is published "in four classes"; the run publishes **three**
  (27 NO-FALSIFIER-REACHES-IT, 23 COVERED-BY-A-DECLARED-MUTANT, 6
  REGISTERED-FORCING).  `COVERED-BY-THE-ANCHOR-BREAKER` can never be reached:
  all three of its gates are also declared-mutant targets and the `if/elif`
  puts mutant coverage first, so the selftest's coverage is never recorded.
  *Repair:* make the class a list per gate rather than a single label, so a
  gate covered by both a mutant and the anchor-breaker says so.
- **m5 — the exit-code conventions are disclosed nowhere in the unit.**
  `--selftest` exits 0 on success and `--mutant` exits 0 on DEAD-ON-TARGET —
  the inversion of the usual reading, and the ledger calls it "this unit's
  disclosed convention", but it appears in no docstring, no `USAGE`, no
  receipt key and no paper sentence (§10 discloses only "Unknown flags exit
  2").  *Repair:* one sentence in §10, one line in `USAGE`, one receipt key.
- **m6 — 6 of the 31 manifest rows vouch themselves to a gate that had not
  passed at seal time.**  `gates`, `mutants`, `waiver_ledger`, `schema`,
  `transcript_head`, `totals` are all taken at `G-SEAL-COMPLETE`, which closes
  after them; §10 says the manifest names "the gate whose passing took it".
  *Repair:* label those six `TAKEN-UNCONDITIONALLY-BEFORE-THE-CLOSING-GATE`
  and say so, as the closing-gate warrant already does for the ledger.
- **m7 — the claim and polarity gates are presence-anywhere, not
  per-occurrence.**  `8 candidate sources` occurs 3×, `207-dimensional
  simplex` 2×, `119 independent numbers` 2×, `no measure on the configurations
  derives` 2×.  Corrupting one occurrence delivers clean (P2: §6's fibre price
  reading `206-dimensional`; P3: §9 reading `9 candidate sources` — and `9` is
  additionally forgiven as a structural literal, `range(0, 24)`); corrupting
  all of them dies at the named gate (P17, P18, P20).  *Repair:* gate the
  occurrence **count** (`hay.count(needle) == expected`), as the verbatim
  anchors already do.
- **m8 — the hyphen blindness is disclosed only for the verdict block.**  It
  is real in ordinary prose too: 421 digit-runs in the paper, 199 scanned, 222
  skipped (63 slash-adjacent, 62 hyphenated, 97 word/dot-adjacent).  P2 above
  is a hyphen-blind corruption of a headline number outside the fence.
  *Repair:* say so in §10, and extend the regex as in M2/M3.
- **m9 — the fixed-locus denominator covers one direction only.**  655360 =
  640 × 32 × 32 checks establish that every uniform configuration *is* fixed;
  "**exactly** the 640 uniform configurations" needs the converse, which comes
  from the gated transitivity plus the no-reversal fact, not from the
  655360.  *Repair:* attribute the two halves separately in §3 and §9.
- **m10 — `G-ARTIFACT-INTEGRITY` leaves the corrupted bytes in place.**
  Corruption injected between `os.replace` and the final read is detected
  (exit 1, `REFUSED`) but the damaged artifacts stay on disk with no rollback
  (S1).  Pre-`replace` corruption is handled correctly (the temp is removed).
  *Repair:* keep the previous bytes and restore them on failure, or write to
  the final path only after the post-replace read.
- **m11 — `assert a and sym` (L2313) is a bare assert** and vanishes under
  `python -O`.  Cosmetic here (it guards nothing), but the era forbids
  gate-shaped logic in asserts.

### 3.2 The mutant census, classified (context for M1–M5)

Of the 25 switch sites, **9 poison the gate's own predicate variable rather
than the object the gate measures**: `MUT-HEAD-CONSTANT` (`ok = False`),
`MUT-PAPER-CLAIM` / `MUT-MUST-NOT` / `MUT-PAPER-NUMERAL` (`… = ["planted"]`),
`MUT-WILSON-SEGMENT` (`banned_keys = [...]`), `MUT-FIXED-LOCUS`
(`failures = 1`), `MUT-CROSS-INVARIANCE` (`cross_bad = 1`),
`MUT-FLOAT-SNEAK` (`floats + [1]`, no float literal planted),
`MUT-BORN-STOCHASTIC` (`ds -= 1`).  Those nine prove their gate *can* fail;
they do not prove the measurement path carries the defect to it, which is what
`#34` reachability asks.  The other 16 mutate a real object.  I supplied the
missing object-level falsifiers for the six that matter most (W7, W8, P16,
P17, P18, and the file-byte perturbations A1–A3) and **all six fire at the
declared gate** — so this is a coverage-accounting defect, not a broken gate.
*Repair:* convert the nine to object mutations (each is a one-line change) or
mark them in the registry as `PREDICATE-PROBE` and re-class them in the waiver
ledger, so `COVERED-BY-A-DECLARED-MUTANT` means what it says.

---

## 4. THE INJECTIONS TABLE

Every row: built by me, run off-tree, one process each.  "wrote" is measured
by hashing both artifacts before and after.

| # | injection | where | caught by | exit | wrote |
|---|---|---|---|---|---|
| W1 | expectation key planted post-gate | `finish()` | `G-SEAL-COMPLETE` | 1 | nothing |
| W2 | renamed expectation key, unsealed | `run()` | `G-SEAL-COMPLETE` | 1 | nothing |
| W3 | renamed key, **sealed** | `run()` | *(none)* | 0 | **delivered** |
| W4 | banned key nested in `census` | `run()` | *(none)* | 0 | **delivered** |
| W5 | neutrally-named computing fn | module | *(none)* | 0 | **delivered** |
| W6 | `wilson_expectation` **lambda** | module | *(none)* | 0 | **delivered** |
| W7 | real banned key, pre-gate | `run()` | `G-NO-WILSON-EXPECTATION` | 1 | nothing |
| W8 | real banned `def` | module | `G-NO-WILSON-EXPECTATION` | 1 | nothing |
| R1 | unregistered `mut("MUT-GHOST")` | `run()` | `G-MUTANT-REGISTRY-TOTAL` | 1 | nothing |
| R2 | `mut(_gn)`, non-constant arg | `run()` | *(none)* | 0 | **delivered** |
| R3 | `MUT == "MUT-GHOST"` bypass | `run()` | *(none)* | 0 | **delivered** |
| R4 | registry row with no branch | `MUTANTS` | `G-MUTANT-REGISTRY-TOTAL` | 1 | nothing |
| R5 | a third closing gate added | `finish()` | *(none — `late_gates` stays 2)* | 0 | **delivered** |
| I1 | verdict flipped after the equality gate | `run()` | `G-PAPER-CARRIES-THIS-RUNS-VERDICT` | 1 | nothing |
| I2 | census rows swapped after the seal | `run()` | `G-SEAL-COMPLETE` | 1 | nothing |
| I3 | control-under-label: the two null columns swap | `measure_invariance` | `G-PAPER-CLAIMS-RENDER` | 1 | nothing |
| H1 | one char changed inside `head_law` | module | `G-PAPER-CARRIES-THIS-RUNS-VERDICT` (**not** the equality gate) | 1 | nothing |
| H2 | H1 **with the paper regenerated** | module+paper | *(none)* | 0 | **delivered** |
| C1 | verdict-determining flag moved between rows | `build_choices` | *(none)* | 0 | **delivered** |
| C2 | NON-FLAT masses corrupted in the code | `measure_invariance` | *(none)* | 0 | **delivered** |
| A1–A3 | bytes appended to pin / giter receipt / weld-3 paper | mirror | `G-SOURCES-PINNED` | 1 | nothing |
| A4–A6 | declared value moved for PV-LINKS / PV-ALPHABET / PV-BAL | `PATH_VALUES` | `G-PATH-VALUE-ANCHORS` | 1 | nothing |
| A7–A9 | needle perturbed for VB-PIN-WILSON / VB-GI-DESCRIPTION / VB-W3-CONSTANT | `VERBATIM` | `G-VERBATIM-ANCHORS` | 1 | nothing |
| A10 | a window shortened below the 50-char floor | `VERBATIM` | `G-VERBATIM-ANCHORS` | 1 | nothing |
| A11 | the floor raised to 400 | `VERBATIM_FLOOR` | `G-VERBATIM-ANCHORS` | 1 | nothing |
| S1 | **post-write** corruption after `os.replace` | `finish()` | `G-ARTIFACT-INTEGRITY` | 1 | corrupt bytes left (m10) |
| S2 | a `SEAL.take` removed | `run()` | `G-SEAL-COMPLETE` | 1 | nothing |
| S3 | manifest row for a key never published | `run()` | `G-SEAL-COMPLETE` | 1 | nothing |
| S4 | the corrupted-probe detector disabled | `finish()` | `G-ARTIFACT-INTEGRITY` | 1 | — |
| S5 | undeclared extra payload key | `finish()` | `G-SEAL-COMPLETE` | 1 | nothing |
| P1 | head flipped in the fenced verdict block | paper | `G-PAPER-CARRIES-THIS-RUNS-VERDICT` | 1 | nothing |
| P2 | §6 fibre price `207`→`206` (one of two) | paper | *(none)* | 0 | **delivered** |
| P3 | §9 census `8`→`9` (one of three) | paper | *(none)* | 0 | **delivered** |
| P4 | §7 NON-COMMUTING cells swapped under their labels | paper | *(none)* | 0 | **delivered** |
| P5 | §7 NON-FLAT `79/80`→`78/80` | paper | *(none)* | 0 | **delivered** |
| P6 | §7 DIAGONAL prose `1/10`,`4/13` moved | paper | *(none)* | 0 | **delivered** |
| P7 | "The area law is visible here." | paper | `G-MUST-NOT-VOCABULARY` | 1 | nothing |
| P8 | `16 sites`→`4242 sites` | paper | `G-PAPER-CLAIMS-RENDER` | 1 | nothing |
| P9 | "The base plaquette's Wilson expectation is 3/8." | paper | *(none)* | 0 | **delivered** |
| P10 | polarity flipped at one of two occurrences | paper | *(none)* | 0 | **delivered** |
| P11–P13 | must-not in a blockquote / split across a line / in a list item | paper | `G-MUST-NOT-VOCABULARY` | 1 | nothing |
| P14–P15 | must-not under inline emphasis (`*area* law`, `string **tension**`) | paper | *(none)* | 0 | **delivered** |
| P16 | bare unregistered numeral in a non-claim sentence | paper | `G-PAPER-COVERAGE` | 1 | nothing |
| P17 | census claim corrupted at **all 3** occurrences | paper | `G-PAPER-CLAIMS-RENDER` | 1 | nothing |
| P18 | polarity flipped at **both** occurrences | paper | `G-PAPER-POLARITY` | 1 | nothing |
| P20 | fibre price corrupted at **both** occurrences | paper | `G-PAPER-CLAIMS-RENDER` | 1 | nothing |

**33 caught at a named gate with exit 1 and nothing written; 14 delivered.**
Of the 14, 4 are the withholding gate's blind spots (W3–W6), 3 the registry's
(R2, R3, R5), 2 the head law's (H1's equality-gate blindness, H2), 1 the
choice inventory's (C1), and 5 the paper coverage's (P2–P6, P9, P10, P14,
P15 — counted as the paper class).

---

## 5. THE SEAM RULING

The seam this unit had to hold is **pin → product**: the pin licenses a
Wilson-expectation segment only in the DERIVED case, the measurement returns
DECLARATION-REQUIRED, and the segment must therefore not exist.  **The seam
holds in the product and should be stated more modestly in the paper.**  The
receipt is clean at every depth, the instrument computes nothing of the kind,
and the verdict declares the withholding in three clauses that a reader can
check against the pin's own bytes (VB-PIN-WILSON, located exactly once, is the
right anchor for it).  What the unit over-claims is the *enforcement*: §8 says
"the discipline is enforced on the product rather than promised in prose", and
the enforcement is a depth-1 key scan plus a `FunctionDef` name scan, either of
which a one-line rename walks past.  With M2's repair the sentence becomes
true as written.

Two further seam notes for the adjudicator.  First, the pin's must-not is
inherited "verbatim from R5" but the *vocabulary list* implementing it is
narrower than the pin's words — bare `potential` and bare `confinement` are
unbanned — so a future unit inheriting this list inherits a weaker wall than
the pin wrote.  Second, `G-PAPER-CARRIES-THIS-RUNS-VERDICT` is the load-bearing
paper gate: it is the only one that reaches the numerals the coverage regex
cannot see, which is why M3's uncovered fractions are exactly the ones that
live outside the fence.

---

## 6. WHAT I COULD NOT FAULT

The seal is genuinely total and I could not get an unsealed or undeclared key
past it — the 42 = 31 + 10 + 1 arithmetic closes exactly, `reverify` compares
disk against gate-time digests and not against a re-serialisation, and the
corrupted probe is written and detected before either artifact is staged.  The
anchor construction is above era standard: every verbatim window carries a
digest, a frozen character count, a declared floor **and** a
perturb-and-must-vanish flip, and the floor itself is live in both directions.
The `#91` posture is clean — the needles are assembled rather than spelled, no
moving reference survives the scan, and the run reproduces byte-for-byte in a
directory with no version control and no siblings.  Twenty-five mutants died
on target in twenty-five separate processes with the artifacts untouched
after every one, and the CLI refuses every malformed argv I could construct.
Those are the parts of the era's contract this unit discharges without
argument.
