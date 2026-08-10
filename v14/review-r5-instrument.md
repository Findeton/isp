# R5 (paper-18, the gauge rung) — HOSTILE REVIEW, K5 THE INSTRUMENT

**Reviewer:** instrument seat (K5), v14 ledger #138 panel.
**Object:** paper `3800959353b4`, code `37c232de91a6`, output `e86be9a581a7`,
receipt `1c072956ac7b`, all at commit `a504243`; pin `b53adba0eee0`; protocol
`16f86f0eabd2`. All six hashes verified against the working tree **and** against
`git diff a504243 HEAD` — the R5 objects are byte-identical across `a504243`,
`b215e6c` and `33b1d06`, no drift. The **nine** hash-pinned runtime inputs were
re-hashed independently and all nine match their frozen digests.
**Interpreter:** `/opt/homebrew/bin/python3.13`.
**Disciplines observed:** read-only git (`log`/`show`/`diff`/`status`/`rev-parse`
only); every run on scratch copies under `…/scratchpad/r5-in/`; no in-repo
execution; this file is my sole repo write.
**Concurrent workers disclaimed:** during the review HEAD advanced
`b215e6c → 7a4eda6 → 33b1d06` and the working tree gained a modified
`v14/code/giter_exact.py` and four untracked `u4b_*`/`paper-17` files. **None of
the six R5 objects moved** (re-hashed at the end of the review; all six
identical). The R5 operator seat froze at `33b1d06` while I was measuring; I
read one line of it, for attribution only, after my own measurement closed.

---

## GRADE: **AWF** (accept with fixes)

**Not R, and not near it.** No delivered number is wrong. ~550 independent
recomputations — the 21 seal digests rebuilt from the receipt, all 40 anchors
re-verified against the parent artifacts, the whole group ladder recomputed with
my own brute-force closure — produced **zero disagreements** with any computed
quantity. The plain run is **byte-identical to the committed artifacts on the
first attempt**, off-tree, git-less, from CWD `/` under a new hash seed, and
again from `/Users` under `PYTHONHASHSEED=777 TZ=Asia/Tokyo LC_ALL=C`. All 24
declared mutants die at their **named** gate with the artifacts byte-unchanged.
25 hostile argv shapes all exit 2 with no writes. `--verify-paper` is **live**
(R4b's MAJOR-4 dead flag is fixed) and `--selftest` is real and numeric.

**And — this is the headline for the seat — the entire R4b playbook is dead on
arrival.** Six for six: the post-gate verdict-head flip, the moved holonomy
class, the control row under a census label, post-write byte corruption, the
`"the "` window truncation and the drifted pinned source are **all caught**,
most of them by the gate-time seal itself. The R4b MAJOR-1 disease is cured, and
its surviving MAJOR-2 (#62 truncation) is cured with it.

**Not A, on four counts.** Twenty-seven reviewer injections were run; **eleven
caught, sixteen survived**. The four that decide the grade:

1. **The paper ships a stale headline.** Paper line 62 — the verdict string,
   the unit's single most load-bearing published object — is **not** the string
   the instrument delivers. It reads `FAMILY-COVARIANCE-512-OF-512-CHECKS` where
   the receipt reads `4096-OF-4096`, and `EXCLUSIVITY-SURVIVES-0-OF-9-BOTH`
   where the receipt reads `0-OF-18`. The delivered string occurs **nowhere** in
   the paper, verbatim or whitespace-normalised. 61 gates did not notice, because
   **no gate compares them**.
2. **The flagship comparator's segment half is a tautology.** I drifted two
   segment literals and delivered, at exit 0 with 61/61 gates, 24/24 mutants and
   21/21 seals verifying, a verdict string **exactly equal to the paper's stale
   line 62** — while the same receipt's `counts` still read 4096 and 18.
3. **Both must-nots are unswept against the paper.** A paper asserting
   "*A confinement-analog claim IS entered here… the area law follows from it*"
   and a paper asserting "*Curvature DOES imply quantum*" each deliver **both
   artifacts byte-identical to the committed ones**.
4. **36 of 61 gates carry a falsifier that cannot reach them.** Measured: all
   nine `--break-anchor` runs and `--selftest` die at `G-SOURCES-PINNED`, the
   *first* gate.

**Calibration of my harness:** the same scratch harness registered 24/24
on-target kills on the declared mutants and caught 11 of my own 27. It therefore
targets the complement of the declared surface — and the surviving complement is
no longer "everything after the last gate". It is precisely what the manifest
does not cover.

---

## 1. WHAT I EXECUTED — honest counts

| class | count |
|---|---|
| program invocations | **93** |
| — plain, off-tree, git-less mirror, CWD `/`, `PYTHONHASHSEED=20260810` | 1 |
| — plain, second mirror, CWD `/Users`, seed 777, `TZ=Asia/Tokyo`, `LC_ALL=C` | 1 |
| — `--no-write` | 1 |
| — `--selftest` (writes-nothing proved by hash manifest) | 1 |
| — `--break-anchor` (all 9 sources) | 9 |
| — `--verify-paper` (own paper; a different real file) | 2 |
| — hostile argv battery | 25 |
| — declared mutants (24 distinct) | 24 |
| — reviewer injection runs | 29 |
| independent recomputations of delivered quantities | **≈550** |
| disagreements with any delivered **number** | **0** |
| disagreements between the **paper** and the receipt | **1** (MAJOR-1) |
| reviewer-designed injections (valid) | **27** |
| — caught | **11** |
| — survived | **16** |
| — discarded as harness errors (disclosed in §5) | 2 |
| declared mutants dead at their **named** gate | **24 / 24** |
| declared mutants leaving artifacts byte-unchanged | **24 / 24** |

**Byte-identity, twice.** A mirror containing only this unit's paper, its code
and the nine pinned sources — no `.git`, no repository, no sibling files —
produced `e86be9a581a7` / `1c072956ac7b`: **exactly the committed bytes**, first
run, exit 0, from CWD `/`. A second mirror from CWD `/Users` under a different
hash seed, timezone and locale produced the same two hashes. **#91 is measured,
not asserted**, and so are hash-seed, TZ and locale independence, which the
docstring does not even claim.

**A property worth recording:** the receipt file *is* the sealed payload —
`json.dumps(R, indent=1, sort_keys=True)` byte for byte — so the payload digest
printed in the transcript (`payload 1c072956ac7b`) **is the receipt's own file
hash**, and the transcript digest (`transcript e86be9a581a7`) is the output's.
Both are checkable from the artifacts alone, with no run. I verified both.

**Independent recomputation, the substantive legs.**

- **All 21 seal digests rebuilt** from the delivered receipt by my own
  implementation of `digest`/`jpath`: **21/21 exact**, 0 mismatches. The
  published `seal_manifest` is a genuine, externally auditable object.
- **All 40 anchors.** 9 byte anchors re-hashed (9/9); 17 path-value anchors
  re-read out of the *parent* receipts (17/17, including the 3364-pair census,
  the 588 baseline, `B058 → OCC`, the FORCED connective); 14 verbatim windows ×
  4 checks each — present in their source, digest correct, length ≥ the declared
  floor of 20, consumer gate present in this run's ledger — **56/56**.
- **The group ladder, with my own machinery.** I rebuilt the ANTI-X plaquette
  holonomies' site permutations and computed orders by **brute-force closure** —
  a different algorithm from the unit's Schreier-Sims — for every stencil small
  enough: `S1-ONE = 3`, `S2-EDGE = 60`, `S2-CORNER = 9`, `S2-APART = 9`,
  `S3-ROW = 2520`, `S4-BLOCK = 20160`. **6/6 exact**, and each equals my
  independently computed alternating product ∏|Oᵢ|!/2, with evenness on every
  orbit reconfirmed. `S-ALL`: 16!/2 = 10461394944000 by my own factorial =
  published order; A₆₄ at L = 8: my 64!/2 (89 digits) = published order exactly.
  All 8 published ANTIDIAGONAL rows re-derived (class from orbit sizes, order
  from the product, support = Σ orbits): **8/8**.
  *Disclosed harness error:* my supplementary Jordan leg reported `S-ALL` as
  imprimitive. That is my bug — A₁₆ on 16 points is 2-transitive, hence
  primitive. It is not a disagreement with the unit.
- **Three-way paper ↔ output ↔ receipt.** 13 transcript counts against the
  receipt (13/13); all 8 rendered transcript lines re-derived from `counts` and
  found verbatim in `output.txt` (8/8); the verdict string in the transcript
  equals the receipt's; all 49 instrument claims present in the paper with
  correct occurrence counts (49/49); 64 distinct paper numerals over 282
  occurrences, none uncovered. **The only three-way disagreement is MAJOR-1.**

**On the certification route (comparator independence, group side).** The
certificate `even-on-every-orbit ∧ order = ∏|Oᵢ|!/2 ⟹ G = ∏Alt(Oᵢ)` is sound
group theory: parity restricted to an invariant orbit is a homomorphism, so
even generators force G ≤ ∏Alt(Oᵢ), and equal finite cardinality upgrades
containment to equality. Crucially the two sides are **not** produced by the
same routine — the measured order comes from Schreier-Sims, the target from a
factorial formula — so a broken order routine fails the gate rather than
passing it spuriously. My six brute-force closures independently validate the
Schreier-Sims itself. **Set-equality certification here is sound, and the
certifier does not share its literals with the builder.** This clause is clean.

---

## 2. THE #82 CLI CONTRACT, CLAUSE BY CLAUSE

Handler at L3115–3157 (`parse_args`, hand-rolled — no `argparse`, so no
abbreviation blemishes). **Verdict: all four documented flags are COMPLIANT.
No dead flag. This is the strongest CLI in v14 to date.**

### 2.1 Unknown flags exit 2 — **PASS**, 25 shapes

Every one exits 2, prints a usage line plus `error: …` on stderr, and a
before/after hash manifest of the whole run directory shows **no writes**:

| argv | exit | | argv | exit |
|---|---|---|---|---|
| `--badflag` | 2 | | `--break-anchor` (no value) | 2 |
| `--selftests` (typo) | 2 | | `--break-anchor BOGUS` | 2 |
| `--self` / `--selftes` (abbrev) | 2 | | `--break-anchor=A-R4-PAPER` | 2 |
| `-h` / `--help` | 2 | | `--no` (abbrev) | 2 |
| `-x` | 2 | | `--no-write --badflag` | 2 |
| `positional` | 2 | | `--verify-paper /nonexistent/NOPE.md` | 2 |
| `""` (empty arg) | 2 | | `--verify-paper v14/NOPE.md` | 2 |
| `--mutant` (no value) | 2 | | `--verify-paper --badflag` | 2 |
| `--mutant BOGUS` | 2 | | `--verify-paper=…` (flag=value) | 2 |
| `--mutant=MUT-ALPHABET` | 2 | | `-- --no-write` | 2 |
| `--mut MUT-ALPHABET` (abbrev) | 2 | | `--NO-WRITE` (case) | 2 |

Prefix abbreviation is off (exact match). `--no-write --no-write` correctly
exits 0 — an idempotent repeat of a declared flag, not a defect.

### 2.2 `--selftest` — **PASS, and genuinely numeric**

Exit 1. Report: `SELFTEST: died at G-SOURCES-PINNED -- as required.`
Writes-nothing **proved by hash manifest** over the whole run directory, before
and after; `diff` of the manifests empty. It calls `build_state(target)` with
`SOURCES[0]`'s expected digest replaced and *requires* a real `GateFail`,
re-entering the whole derivation. I corrupted every anchor myself via
`--break-anchor` (9 runs, one per source): **all 9 die at `G-SOURCES-PINNED`,
exit 1, writing nothing.** And I drifted a pinned source's *bytes on disk*
(INJ26): also dead at `G-SOURCES-PINNED`. The falsification path is real.

### 2.3 `--mutant NAME` — **PASS, cleanly**

24/24 die at their **declared target gate**. I verified each kill site against
the **source's** `MUTANTS` table extracted by AST — never against the receipt's
`on_target` field. 24/24 leave both artifacts byte-unchanged (hash manifest
before and after the whole sweep: no drift). Unknown names exit 2 and never
report SURVIVED. `--mutant` and `--break-anchor` both come out of the parser
with `write=False`.

Registries are complete and checkable without running: 24 mutants in the source
== 24 rows in the receipt; 61 waiver rows == `totals.gates`; 60 ledger rows ==
`totals.gates_in_receipt`; every mutant target is a gate that exists.

### 2.4 `--verify-paper [PATH]` — **LIVE. R4b's MAJOR-4 is fixed.**

Measured, and this is the repair working:

- `--verify-paper` (own paper) → exit **0**, printing real coverage
  (`48 claims, 64 distinct numerals over 282 occurrences, uncovered []`) and
  real polarity (`7 expected-occurrence claims, 6 guarded, window 64`);
- `--verify-paper v14/paper-10-defect-on-the-stage.md` → exit **1** at
  `G-PAPER-CLAIMS`, naming all 43 missing claims;
- `--verify-paper /nonexistent/NOPE.md` → exit **2** at parse time;
- no writes in any of the three.

`main()` reads the key, resolves the path, and runs the derivation with that
file as the object under test. **It is not a no-op on any argument it accepts.**

**CLI VERDICT: COMPLIANT on all four documented clauses. No findings.**

---

## 3. THE SEAL, UNDER THE R4b PLAYBOOK

The manifest declares **21 sealed objects**, taken at four gates. I rebuilt
every one of the 21 digests from the delivered receipt: **21/21 exact.**

**Six of the R4b playbook's classes, six kills:**

| playbook class | R4b (pre-repair) | R5 |
|---|---|---|
| post-gate verdict-head flip | **SURVIVED** | **CAUGHT** — `SEAL-VERDICT-STRING`, `SEAL-VERDICT-HEAD`, nothing written |
| published-row corruption (a holonomy class moved) | **SURVIVED** | **CAUGHT** — `SEAL-GROUPS`, nothing written |
| a control row under a census label | **SURVIVED** | **CAUGHT** — `SEAL-FLAT-CONTROL`, nothing written |
| post-write byte corruption | **SURVIVED** (Γ-iteration INJ-4, receipt no longer parsed, exit 0) | **CAUGHT** — exit 1 (see MINOR-1) |
| verbatim window truncated to a decoration | **SURVIVED** | **CAUGHT** — `G-VERBATIM-ANCHORS :: present=True floor=False digest …` |
| pinned source drifted on disk | CAUGHT | **CAUGHT** — `G-SOURCES-PINNED` |

**Nothing ships at exit 0 with a non-parsing receipt.** The Γ-iteration disease
is closed: the write path stages both artifacts through `.tmp` files, re-reads
them, checks `digest == payload_sha`, re-verifies all 21 seals against the
*parsed disk object*, and reconstructs the verdict from the disk bytes — all
before `os.replace` — then re-reads from the final paths and repeats the check.

**Count tampering** is caught where the seal reaches it (`SEAL-COUNTS` at
`G-VERDICT-RECONSTRUCTED`; INJ04 died even earlier, at
`G-PAPER-COVERAGE-FINAL`) and **not** where it does not (INJ09, INJ10 — §4,
MAJOR-5).

---

## 4. FINDINGS

### MAJOR-1 — the paper's headline verdict string is STALE, and no gate binds the paper to the delivered verdict

Paper line 62 against `verdict/string` in the receipt — 1321 characters against
1324, two segments apart:

| | receipt (delivered) | paper line 62 |
|---|---|---|
| declared gate | `FAMILY-COVARIANCE-**4096-OF-4096**-CHECKS` | `FAMILY-COVARIANCE-**512-OF-512**-CHECKS` |
| two-excitation | `EXCLUSIVITY-SURVIVES-**0-OF-18**-BOTH` | `EXCLUSIVITY-SURVIVES-**0-OF-9**-BOTH` |

The delivered string occurs **nowhere** in the paper — not verbatim, not
whitespace-normalised. The paper's own prose is **correct**: line 344 reads
"`4096 of the 4096 checks`" and line 437 reads "`0 of 18` rows carry". So the
paper contradicts itself, and its most prominent object is the wrong half.

Why 61 gates missed it: `G-PAPER-CLAIMS` requires 49 claim *fragments* to occur
somewhere in the paper — and they do, at lines 344 and 437.
`G-PAPER-NUMERAL-COVERAGE` requires every paper numeral to be a member of a
*global* rendered set — and `512` is in it (the balanced sector is 512 coins)
and `9` is in it. Neither gate ever looks at the verdict string.

**Proof that the binding is absent, not merely weak (INJ24):** I flipped the
paper's headline to `R5-NO-STABLE-GROUP-<CLASS=ALTERNATING…>` — the *opposite*
pre-registered outcome — and the run delivered **both artifacts byte-identical
to the committed ones** at exit 0, 61/61 gates.

*Independent corroboration:* the R5 operator seat, frozen at `33b1d06` while I
was measuring, independently registers "two paper transcription errors ungated".
Two seats, two routes, one fault.

**Repair (liftable, ~8 lines).** Correct paper line 62 to the delivered string,
and add the gate that would have caught it:

```python
LD.gate("G-PAPER-CARRIES-THE-VERDICT",
        "the delivered verdict string occurs in the paper verbatim up to line "
        "wrapping: the paper's headline IS the instrument's headline, and a "
        "paper quoting an earlier run's verdict dies here",
        flat(string) in flat(paper_text),
        "%d characters matched" % len(string))
```

placed beside `G-PAPER-CLAIMS`, added to `LATE_GATES`, with a falsifier
`MUT-PAPER-VERDICT` that perturbs one character of `string` before the
comparison and targets that gate. Both totals (`61 → 62`, `24 → 25`) move.

### MAJOR-2 — `G-VERDICT-RECONSTRUCTED` is circular on 1306 of the 1324 characters it claims to compare

`reconstruct_from_serialized` (L2694) documents itself as carrying "its OWN copy
of the head law **and its OWN segment renderer**", sharing "no helper, no input
and no typed value with the builder". The head law *is* independently
re-implemented (the five-branch if/elif duplicates `derive_head`). **The segment
renderer does not exist.** L2711 reads:

```python
    s = R["verdict"]["segments"]
    return h + "-<" + "|".join(s) + ">"
```

— the builder's own product, read back and re-joined. `build_verdict` returns
`head + "-<" + "|".join(segs) + ">"` with the *same* list. So the gate compares
the segments against themselves. Only the 18-character head is really checked.

**Proof (INJ15), and it is the decisive injection of this review.** I drifted
two literals inside `build_verdict` only — `c["two_rows"] → 9` and the
covariance pair → `512, 512` — touching nothing else. Result: **exit 0, 61/61
gates, 24/24 mutants on target, 21/21 seals verifying, the seal manifest
self-consistent**, and the delivered verdict string is

> `…FAMILY-COVARIANCE-512-OF-512-CHECKS…EXCLUSIVITY-SURVIVES-0-OF-9-BOTH…`

**exactly, character for character, the paper's stale line 62** — while the same
receipt's `counts.family_covariance_checks` reads 4096, `counts.two_rows` reads
18, and the gate details read `family covariance 4096 checks, 0 failures` and
`cells {'00': 12, '01': 2, '10': 4, '11': 0}`.

This is the gate that was supposed to make MAJOR-1 impossible. It cannot see a
false number in a segment, because the number never leaves the builder.

**Repair (liftable, ~35 lines).** Give the reconstruction a real segment
renderer that reads `R["counts"]` off the serialized receipt and formats the
eight segments itself, sharing no format string with `build_verdict`; compare
that against `R["verdict"]["segments"]` *and* against the string. Cheaper
interim: a second gate re-rendering each segment from `counts` and requiring
equality, with a mutant that drifts one segment literal.

### MAJOR-3 — the two must-nots are never swept against the paper

`G-NO-CONFINEMENT-LANGUAGE` (L3252) has two legs:
`"NO-CONFINEMENT-CLAIM" in string` — a substring of a string the same function
built — and
`not any("confinement" in str(v).lower() for v in paper_claims(R).values())`.
The second sweeps **only the instrument's own 49 rendered claim strings**, which
are assembled from receipt numbers and hard-coded templates and therefore can
never contain the word. **The paper text is not swept.** The gate is, in
substance, cannot-fail.

`G-CURVATURE-DOES-NOT-IMPLY-QUANTUM` (L2307) is not a text gate at all — its
predicate is `linkA["10"] > 0`, a measurement that a converse witness exists.
Sound as a measurement; it constrains no prose.

**Proof.** Both of these deliver **both artifacts byte-identical to the
committed ones** at exit 0:

- **INJ16** — the paper's confinement must-not inverted to
  "*A confinement-analog claim IS entered here, in the prose: the measured
  alternating holonomy is the confining mechanism of the record stage, and the
  area law follows from it.*"
- **INJ17** — the paper's quantum must-not inverted to
  "*The must-not, released. Curvature DOES imply quantum…*"

Note the asymmetry that makes this a real hole rather than a theoretical one:
the *claim* gates are strong (INJ21 and INJ22, ordinary numeral and claim
drifts, both died at `G-PAPER-CLAIMS`), so an author who edits a measured claim
is stopped — but an author who adds or inverts a *must-not*, which carries no
numeral and is not a rendered claim, is not.

**Repair (liftable, ~10 lines).** Sweep the whitespace-normalised paper for the
forbidden vocabulary with a declared allow-list of the must-not-*declaring*
sentences (which are themselves verbatim-anchored, so the allow-list is pinned):

```python
FORBIDDEN_IN_PAPER = ("confinement", "area law", "static potential")
MUSTNOT_SENTENCES = (...)          # the declaring sentences, #62-anchored
hay = flat(paper_text).lower()
for s in MUSTNOT_SENTENCES:
    hay = hay.replace(flat(s).lower(), " ")
LD.gate("G-NO-CONFINEMENT-IN-THE-PAPER", "...",
        not any(w in hay for w in FORBIDDEN_IN_PAPER), "...")
```

plus the same treatment for an inverted `Curvature does not imply quantum`
(an `EXPECTED_OCCURRENCES` entry and a `POLARITY_GUARDS` entry will do it),
each with a mutant.

### MAJOR-4 — the #34 denominators: 36 of 61 gates carry a falsifier that cannot reach them

Machine-checked against the receipt's `waiver_ledger`:

| status | count |
|---|---|
| FALSIFIABLE, named mutant | **22** |
| FALSIFIABLE, generic `--break-anchor` fallback | **36** |
| WAIVED with a registered forcing | **3** |
| total | **61** |

The 36 carry the string *"the anchor break self-test (`--break-anchor`), which
corrupts an input this gate reads and kills the run."* **Measured: all nine
`--break-anchor` runs, and `--selftest`, die at `G-SOURCES-PINNED` — the first
gate.** The run never reaches the other 35, so the mechanism does not exercise
them; it only proves the run can die. And the clause "an input this gate reads"
is simply false for gates that read no anchor: `G-NO-FLOATS-IN-SOURCE`,
`G-NO-SUBPROCESS` (both read `SELF`), `G-CLI-CONTRACT`, `G-VERIFY-PAPER-LIVE`,
`G-CHOICE-INVENTORY`, `G-DECLARATION-SEGMENTS`, `G-PUBLISHED-ROWS-BOUND`.

Several of the 36 are additionally weak on their own terms:

- `G-PUBLISHED-ROWS-BOUND` — predicate is `all(k in R for k in (…))`, a
  key-presence check. Its real work is taking 13 seals immediately afterwards
  (which *is* substantive, and INJ02/INJ03 prove it bites), but the gate's own
  claim — "every published table is bound to the verdict it supports" — is not
  what the predicate tests.
- `G-VERIFY-PAPER-LIVE` — predicate is
  `cli_error_probe(parse_args, ["--verify-paper", "v14/NOPE.md"])`, a verbatim
  duplicate of one clause already inside `G-CLI-CONTRACT`. It does not test
  liveness (I had to test that from the outside, §2.4 — and it passed).
- `G-DECLARATION-SEGMENTS`, `G-NO-CONFINEMENT-LANGUAGE`, `G-SCOPE-INHERITED` —
  substring checks against a string built in the same function.

**Honest denominator: 22 of 61 gates (36%) carry a falsifier that actually
exercises them**, not the 58 of 61 the ledger reads.

**Repair (liftable).** Re-word the fallback to say what it is —
*"no falsifier reaches this gate; `--break-anchor` kills the run upstream at
`G-SOURCES-PINNED`"* — which converts 36 silent FALSIFIABLE rows into honest
disclosures; then add mutants for the gates that *can* be reached (the group,
census, matched and refinement gates mostly already have them) and register
forcings for the rest. This is a bookkeeping repair; it moves no number.

### MAJOR-5 — three seals are taken so late that a pre-seal window exists on the gate ledger and the totals

`SEAL-GATES`, `SEAL-TOTALS` and `SEAL-COVERAGE` are all taken at
`G-PAPER-COVERAGE-FINAL`, at L3688–3690 — the last three statements before
`SEAL.close`. Everything between the objects' construction and that point is
unsealed, and the seal then certifies whatever it finds.

- **INJ09** — `R["gates"][0]["passed"] = False` immediately before
  `SEAL.take("SEAL-GATES")`. **SURVIVED**, exit 0. The shipped receipt carries
  `G-SOURCES-PINNED: passed=False` while `totals.gates_passed_in_receipt` reads
  60, the transcript reads `ALL GATES PASSED`, and the seal manifest verifies
  perfectly against the corrupted contents.
- **INJ10** — `R["totals"]["mutants_killed"] = 99` before `SEAL.take`.
  **SURVIVED**, exit 0, against 24 actually dead.

**Repair (liftable, ~6 lines).** Take `SEAL-GATES` inside `Ledger.gate` (seal
each row as it closes), and compute `totals` in one place with a re-derivation
gate after the seal:
`assert R["totals"]["mutants_killed"] == sum(1 for m in R["mutants"] if m["killed"])`
as a gated identity rather than an assignment.

---

### MINOR-1 — the *second* integrity check leaves the corrupt bytes on disk

INJ12 corrupts `OUT_JSON` after `os.replace` and before the final
`against_the_seal`. It is **caught** — exit 1,
`G-ARTIFACT-INTEGRITY :: the artifacts on disk differ from the gate-time seal` —
but the corrupt file remains. The *first* check (against the `.tmp` files)
correctly `os.remove`s both and writes nothing; the second has no such arm.
Materially milder than R4b's INJ14 (which left a transcript reading
`ALL GATES PASSED … EXIT 0`), because here the exit code is 1 and the corruption
is named. **Repair:** hold `payload`/`text` and rewrite both paths, or restore
from the pre-replace bytes, before `sys.exit(1)`.

### MINOR-2 — the #62 floor is 20 characters and the digest is self-declared

INJ27: the `VB-R4-588` window shrunk to exactly 20 characters
(`"588 of 3364 pairs at"`) with its `WINDOW_DIGESTS` entry re-frozen to match
passes `G-VERBATIM-ANCHORS` and **ships at exit 0**. The floor stops truncation
to a decoration (INJ25, the R4b disease, dies), but it does not stop an author
shrinking an anchor to the floor and re-freezing. Bounded — the receipt
publishes each window's character count, so it is auditable from the artifact.
**Repair:** pin each window's char count in the frozen declaration alongside its
digest, or raise the floor toward the observed minimum (50).

### MINOR-3 — `GateFail` at `SEAL.close` escapes as a traceback

INJ01/02/03 are caught by `SEAL.close`, which raises outside `main()`'s
`try/except GateFail`. Exit code is 1 and nothing is written, so the contract
holds — but the operator sees a Python traceback rather than the clean
`GATE FAILED: … EXIT 1` report every other failure produces. **Repair:** wrap
`SEAL.close` in the same handler.

### MINOR-4 — the polarity apparatus covers 7 and 6 of 49 claims

`EXPECTED_OCCURRENCES` guards 7 claims, `POLARITY_GUARDS` 6, over a declared
64-character window; 42 rendered claims carry neither. All three numbers are
published in the receipt, so the limitation is disclosed rather than hidden, and
the leg does bite (INJ23, a negator inserted ~53 characters ahead of a guarded
claim, died at `G-PAPER-CLAIM-POLARITY`). But a negator beyond 64 characters is
invisible by construction. **Repair:** extend the guard list toward the claims
whose direction is verdict-bearing (`exclusive`, `control_flat`, `infinite`
are guarded; `rank`, `gate_admits`, `covariance`, `global`, `plaq_cells` are
not).

### MINOR-5 — dead code

L3328–3333 is a `for sid in (…13 seal ids…): pass` loop with no effect,
immediately above the gate that then takes those seals in a second loop.
Cosmetic; delete it.

---

## 5. THE INJECTIONS TABLE

Each row is a single edit to a scratch copy of the delivered bytes (or of the
paper), run to completion as a full plain run in its own off-tree mirror.
"Survived" = exit 0, 61/61 gates, 24/24 mutants, both artifacts written.

| # | injection | class | result | proof of execution |
|---|---|---|---|---|
| INJ01 | **post-gate verdict-head flip** | seal / verdict | **CAUGHT** | `G-ARTIFACT-INTEGRITY :: sealed over a broken seal :: ['SEAL-VERDICT-STRING','SEAL-VERDICT-HEAD']`, nothing written |
| INJ02 | **a holonomy class moved** (`holonomy_groups[0].position_class → A99`) | seal / published row | **CAUGHT** | `… broken seal :: ['SEAL-GROUPS']`, nothing written |
| INJ03 | **control row under a census label** (`flat_control.holonomy_group_order → 20160`, `noncommuting → 12`) | seal / control | **CAUGHT** | `… broken seal :: ['SEAL-FLAT-CONTROL']`, nothing written |
| INJ04 | post-gate `counts.noncommuting_configs → 640` | seal / counts | **CAUGHT** | `G-PAPER-COVERAGE-FINAL`, nothing written |
| INJ05 | `balanced_sector.trace_not_an_algebraic_integer → 1` | **unsealed table** | **SURVIVED** | exit 0; `output.txt` **byte-identical**; receipt ships 1 against `counts.balanced_infinite = 512` and a verdict reading `INFINITE-ORDER-512-OF-512`; json `d82a1f04dc6b` |
| INJ06b | `holonomy_rank["S-ALL"].rank → 1` | **unsealed table** | **SURVIVED** | exit 0; ships rank 1 against `counts.global_rank = 8` and a verdict reading `RANK=8-OF-16`; json `94fb75a8a59c` |
| INJ07 | `verdict.segments` replaced wholesale | unsealed sub-key | **CAUGHT** | `G-ARTIFACT-INTEGRITY :: what was about to be written does not match the gate-time seal`; the write-time reconstruction reads segments, so it binds them |
| INJ08 | `source_sha256["A-R4-RECEIPT"] → "000000000000"` | **unsealed provenance** | **SURVIVED** | exit 0; `output.txt` **byte-identical**; receipt ships a false provenance hash beside the *sealed* `byte_anchors` row still reading `3dc1393b0df8`; json `c28e3bc493f0` |
| INJ09 | `gates[0].passed → False` before `SEAL-GATES` | **late-seal window** | **SURVIVED** | exit 0; ships `G-SOURCES-PINNED: passed=False` with `totals.gates_passed_in_receipt = 60` and a transcript reading all-passed; json `afc06cc59c01` |
| INJ10 | `totals.mutants_killed → 99` before `SEAL-TOTALS` | **late-seal window** | **SURVIVED** | exit 0; 99 against 24 actually dead; json `f57879b0883e` |
| INJ11 | `seal_manifest` published with every digest `deadbeefcafe` | **unsealed manifest** | **SURVIVED** | exit 0; the published manifest no longer verifies against its own receipt — self-detecting by an auditor, but it ships; json `ed116fa5ddf3` |
| INJ12 | bytes appended to `OUT_JSON` after `os.replace`, before the final check | post-write | **CAUGHT**, bytes left | `G-ARTIFACT-INTEGRITY :: the artifacts on disk differ from the gate-time seal`, exit 1; corrupt file remains (MINOR-1) |
| INJ13 | bytes appended after the final check | seam boundary probe | **SURVIVED** | exit 0 — but this required *inserting* a statement where the delivered source has none; see the seam ruling |
| INJ14 | `emit_report`'s G1 line rendered from `640` instead of `counts` | transcript prose | **SURVIVED** | exit 0; `output.txt` asserts `640 of 640` against a receipt reading 576; out `c0d2675a4f9a`, json **byte-identical** |
| INJ15 | **two `build_verdict` segment literals drifted** (`two_rows→9`, covariance→`512,512`) | **comparator circularity** | **SURVIVED** | exit 0, 61/61, 24/24, 21/21 seals verify; delivered verdict **exactly equals the paper's stale line 62**; `counts` still read 4096 and 18; out `c4277e077518`, json `15ebce764e12` |
| INJ16 | paper's confinement must-not inverted to an assertion | **#125 must-not** | **SURVIVED** | **both artifacts byte-identical to the committed ones** |
| INJ17 | paper's `Curvature does not imply quantum` → `Curvature DOES imply quantum` | **#125 must-not** | **SURVIVED** | **both artifacts byte-identical to the committed ones** |
| INJ18 | `projective_periods["BALANCED"] → [1]` | unsealed table | **SURVIVED** | exit 0; ships a finite period against the `INFINITE-ORDER` headline; json `872c634c783d` |
| INJ19b | `paper_polarity.inverted → []`, `paper_claims["alternating"]` rewritten | **unsealed #20 output** | **SURVIVED** | exit 0; the instrument's own published verdict on the paper, falsified; json `c608d3163144` |
| INJ20 | `coin_sectors["BALANCED"] → 1` | unsealed table | **SURVIVED** | exit 0; ships 1 against `counts.coins_balanced = 512`; json `f58a80785e77` |
| INJ21 | paper numeral drift `0 of 18` → `0 of 17` | #20 control | **CAUGHT** | `G-PAPER-CLAIMS`, nothing written |
| INJ22 | paper claim `0 of the 52` → `every one of the 52` | #20 unguarded claim | **CAUGHT** | `G-PAPER-CLAIMS`, nothing written |
| INJ23 | negator inserted ~53 chars before a guarded claim | #125 polarity | **CAUGHT** | `G-PAPER-CLAIM-POLARITY`, nothing written |
| INJ24 | **paper's headline verdict head flipped to `R5-NO-STABLE-GROUP`** | **paper ↔ verdict binding** | **SURVIVED** | **both artifacts byte-identical to the committed ones**, exit 0 |
| INJ25 | verbatim window `VB-R4-588` truncated to `"the "` | #62 (R4b's survivor) | **CAUGHT** | `G-VERBATIM-ANCHORS :: present=True floor=False digest 6e5ce6afa65b expected 83942558915a` |
| INJ26 | pinned source drifted on disk (`review-r4-effectus.md`) | #91 moving reference | **CAUGHT** | `G-SOURCES-PINNED :: A-REV-EFFECTUS … expected f54fa11dfd07 measured 3751eefbf522` |
| INJ27 | window shrunk to exactly the 20-char floor, digest re-frozen | #62 residual | **SURVIVED** | exit 0; json `b939e4d08994` (MINOR-2) |

**Run 27 / caught 11 / survived 16.**

*Discarded as harness errors, disclosed for honesty:* **INJ06** (targeted
`list(holonomy_rank.values())[0]`, which is `S1-ONE` whose rank is already 1 — a
semantic no-op, superseded by INJ06b) and **INJ19** (mutated `paper_polarity`
at a point `main()` later overwrites — superseded by INJ19b). Neither is counted
above. My Jordan-primitivity leg on `S-ALL` also mis-fired; disclosed in §1.

---

## 6. THE SEAM RULING

**THE SEAM IS TWELVE WIDE.** Twelve of the sixteen survivors are corruptions of
the receipt or transcript that reach disk after their gate has closed. (The
other four are not seam: INJ16/17/24 are the paper-binding hole, MAJOR-1 and
MAJOR-3; INJ27 is the #62 floor residual, MINOR-2.)

Calibration: **Γ-iteration 9 wide** (pre-#119, no seal at all), **R4b 10 wide
before its repair and 0 after**, **U4 0 after its repair**, **weld-2 12**.

But the raw number is the wrong headline, and reporting it without the
decomposition would misrepresent this unit. **The twelve are a different animal
from the nine.** Γ-iteration's nine were all one mechanism — *there is no
gate-time seal*. R5's twelve are the complement of a seal that works:

| sub-class | count | what it is |
|---|---|---|
| **the unsealed complement** | 7 | `balanced_sector`, `holonomy_rank`, `coin_sectors`, `projective_periods`, `source_sha256`, `seal_manifest`, `paper_claims`+`paper_polarity` — 18 of the receipt's 38 top-level keys carry no seal at all |
| **the late-seal window** | 2 | `gates`, `totals` — sealed at the last gate, so the window before it is open (MAJOR-5) |
| **the transcript's prose** | 1 | `emit_report`'s rendered lines are digested *after* they are composed; no gate compares the transcript's numbers to the receipt's |
| **comparator circularity** | 1 | the verdict segments, never re-derived (MAJOR-2) |
| **the boundary probe** | 1 | INJ13 — and this one is nearly a formality, see below |

**On INJ13 and the true width of the write window.** In the delivered source
there is **no statement between the final `against_the_seal` and `sys.exit(0)`
that can touch the artifacts** — only a `print` to stdout. INJ13 survives solely
because I *inserted* one. Measured strictly, **the post-verification write
window is zero statements wide**, which is the strongest result of its kind in
v14: R4b's repair verified before writing; R5 verifies before writing, again
after `os.replace`, and reconstructs the verdict from the disk bytes in both
checks. I count INJ13 in the twelve for arithmetic honesty, not because it
describes a real exposure.

**What keeps the width from being larger, and belongs on the record:**

1. **The payload is the file.** The receipt on disk is byte-for-byte the sealed
   payload, so its own hash is the payload digest printed in the transcript. No
   re-serialization gap exists.
2. **The published manifest is auditable.** All 21 digests can be, and were,
   recomputed from the delivered receipt with no access to the run. INJ11 is
   therefore self-detecting by anyone who does what I did.
3. **The disk re-read is a real re-read.** `against_the_seal` parses the disk
   bytes, re-verifies all 21 seals against the *parsed disk object*, and
   reconstructs the verdict string from those bytes — twice, once on the
   temporaries and once on the final paths.

**What is undefended is every published value the manifest does not name** — and
that is now the whole finding.

---

## 7. THE BORN-#119 RULING

**The second native seal HOLDS. Its mechanism is sound; its manifest is short.**

The seal itself is the best in v14. Every attack the R4b playbook carries — the
post-gate head flip that survived R4b, the moved published row, the control row
under a census label, post-write corruption, the truncated window that survived
R4b, the drifted pinned source — dies here, six for six, and the four that die
at the seal die *by name*, at `SEAL-VERDICT-STRING`, `SEAL-GROUPS`,
`SEAL-FLAT-CONTROL`. The first #119-native unit (R4b) proved the mechanism could
be built. **The second proves it survives contact with a hostile reviewer who
knows exactly where the first one bled** — and that the frontier has moved.

What the second seal reveals that the first could not: **coverage, not
mechanism, is now the binding constraint.** R4b sealed 18 objects over a smaller
receipt. R5 seals 21 over a receipt with 38 top-level keys, and the 18 it does
not name are exactly where my battery landed — including `source_sha256` (the
provenance an auditor reads first), `seal_manifest` (the seal's own published
account of itself), and the `paper_claims`/`paper_polarity` pair (the #20
instrument's own verdict on the paper). Three of the 21 seals are taken so late
that a pre-seal window exists on the gate ledger and the totals.

And the deepest finding of the review is not about the seal at all. It is that
**the one gate the unit points to as its independent comparator does not compare
what it says it compares** — and that the one published object the seal *does*
protect, the verdict string, is quoted **wrongly in the paper**, where no gate
looks. The seal guards the receipt beautifully. Nothing guards the sentence the
reader will actually read.

**Repair order for a lift to A**, all liftable without moving a single measured
number:

1. Fix paper line 62 to the delivered verdict string; add
   `G-PAPER-CARRIES-THE-VERDICT` + `MUT-PAPER-VERDICT` (MAJOR-1).
2. Give `reconstruct_from_serialized` a real segment renderer, or add a
   segment-re-render gate + mutant (MAJOR-2).
3. Sweep the paper for the two must-nots with a pinned allow-list (MAJOR-3).
4. Re-word the 36 generic waiver rows to disclose that no falsifier reaches
   them (MAJOR-4).
5. Seal `gates` per row and re-derive `totals` under a gate (MAJOR-5).
6. Extend `SEALED_PATHS` over the substantive unsealed tables —
   `balanced_sector`, `holonomy_rank`, `coin_sectors`, `projective_periods`,
   `source_sha256`, `paper_claims`, `paper_polarity` — which alone closes 7 of
   the 12 (the seam ruling).
7. MINOR-1 through MINOR-5.

Items 1–3 are the ones that change what the unit *says*. Items 4–6 are the ones
that change what it can *prove*. None of them touches a measured quantity: after
27 injections and ~550 recomputations, **no delivered number of this unit is
wrong.**
