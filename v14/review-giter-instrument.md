# Γ-ITERATION (paper-16) — INSTRUMENT REVIEW (K5, at the full era)

**Seat:** instrument. **Frozen:** 2026-08-10.
**Protocol:** `v14/note-giter-hostile-protocol.md` (`9f54f1083f21`).
**Object — all six hashes verified at my own hands before anything ran:**
paper `fd2f25d40002`, code `fab2cdc1893e`, output `58ddd86a52f2`,
receipt `8d28b5f2f807`, pin `aa161f8f8e9d`, protocol `9f54f1083f21`.

## GRADE: AWF (ACCEPT-WITH-FIXES)

**Executions:** 57 — 2 full clean plain runs (off-tree default seed;
`PYTHONHASHSEED=4242`), 7 full injected runs, 1 `--mutant` run, 2
`--selftest` runs, 17 hostile-argv invocations, 3 real source-corruption
runs, 3 truncated hash-seed probes, 22 reviewer programs.
**Recomputations:** ≈640. **False computed numbers found: ZERO.** Every
number I could reach independently — with my own partition refinement,
my own spanning-forest holonomy, my own rational-rank routine, my own
eq-22 route, my own leg scan — reproduced the delivery exactly.

Eight MAJOR and six MINOR findings, all bounded and mechanical; none
moves a delivered number. Two of them change what the instrument can do:
**the pre-registered outcome `GITER-DEVIATION` is unreachable**, and
**the seam is nine wide.**

Work was scratch-only under `…/scratchpad/git-in/`; git was read-only;
concurrent workers (`u4_*`, `u4b_*`, `r5_*`) disclaimed and untouched.
The repository's four Γ-iteration files are byte-identical to `9e481db`
at the end of this review.

---

## 1. HEADLINE

| | |
|---|---|
| **THE SEAM RULING** | **NINE WIDE.** 11 injections; 2 caught, 9 survive. Every survivor is one mechanism: *there is no gate-time seal, so the receipt is built from live objects at 3242 and verified against itself at 227.* Calibration: R4b 10-wide pre-repair, weld-2 12-wide, U4 9-wide one layer down. |
| **THE UNREACHABLE OUTCOME** | `FLAGS` at 2800 is not a partition; the one branch that selects `GITER-DEVIATION` sets two flags, which `check_verdict` then rejects. The pin's R3 "first-class finding" can only ever appear as a refused run. |
| **THE #82 CLI** | 18/18 argv verdicts correct. `--selftest` exit 1, hash-proven to write nothing, report matches the corruption it made; 3 real source corruptions also refuse before measurement and do not even create the out-dir. |
| **#91 BOTH LEGS** | Byte-identical at my own hands: off-tree, `.git`-less mirror, `--out-dir` redirected, default random hash seed → `58ddd86a52f2…` / `8d28b5f2f807…`; and again under a **fourth** interpreter hash seed (4242). |
| **THE EXCLUSION** | paper-13 declared-and-not-read: **clean** on three independent routes (textual, AST, runtime audit hook). |
| **HONEST DENOMINATORS** | 58 registered gates = 17 anchors + 41 gates, of which **36 can independently fail**; 54 falsifiers of which **49 are substantive** and **51 reach the gate they name**. |

---

## 2. MAJOR FINDINGS

### MAJOR-1 — THE PRE-REGISTERED OUTCOME `GITER-DEVIATION` IS UNREACHABLE

`giter_exact.py:2800`

```python
FLAGS = [_law_ok, (not _law_ok) and ID_VIOL == 0, not _law_ok]
```

The three flags are not a partition. Enumerated exhaustively, driving
the delivery's own `check_verdict` lifted verbatim out of its source:

| `_law_ok` | `ID_VIOL` | FLAGS | true | head selected | comparator |
|---|---|---|---|---|---|
| True | 0 | `[T,F,F]` | 1 | GITER-LAW-CONFIRMED | passes |
| True | 3 | `[T,F,F]` | 1 | GITER-LAW-CONFIRMED | passes |
| **False** | **0** | **`[F,T,T]`** | **2** | GITER-DEVIATION | **`the outcome selector is not single-valued` → DELIVERY REFUSED** |
| False | 3 | `[F,F,T]` | 1 | GITER-BLOCKED-AT | passes |

The only branch that selects `GITER-DEVIATION` sets two flags;
`check_verdict` (2943) rejects a multi-valued selector; `V_FAIL` is
non-empty; 3383 refuses. **`GITER-DEVIATION` can never be written.**

That branch is exactly the one the pin calls a first-class finding.
R3: "on CONG-185 the adjudicated expectation is agreement … a deviation
HERE is a first-class finding, not a failure", with
`GITER-DEVIATION-<located>` pre-registered in OUTCOMES. A located
deviation — the holonomy head failing while the deviation identity still
holds — *is* `_law_ok False, ID_VIOL == 0`. This is the honest answer to
K3's two-way question: **a deviation here would have looked like a
refused run, not like a located deviation.**

No delivered number moves; every conjunct of `_law_ok` is independently
reproduced in §11, so the head that was written is the right one. But it
was selected by a selector that is not a partition, and the alternative
the paper says the gate could have reached was never reachable.

**REPAIR (one line, 2800):**
```python
FLAGS = [_law_ok, (not _law_ok) and ID_VIOL == 0, (not _law_ok) and ID_VIOL != 0]
```
plus a falsifier that evaluates the selector on all four
`(_law_ok, ID_VIOL)` combinations and asserts exactly one flag in each —
which turns "both branches reachable" from a sentence into a measurement.

### MAJOR-2 — THE SEAM: NO GATE-TIME SEAL, AND THE WRITE PRECEDES THE INTEGRITY GATE

Three mechanisms, all measured by the battery in §5.

*The output stream is sealed at emission, and that seal works.*
`emit()` (132–134) folds every line into `DIGEST` as it is emitted;
`finish()` (222–225) compares the disk bytes against both the joined
`body` and `DIGEST`. INJ-2 is caught, loudly. The paper is right to
claim this, and it is what keeps the width from being twelve.

*The receipt is not sealed at all.* `finish()` (226–227):

```python
flat = json.loads(json.dumps(RECEIPT, sort_keys=True, default=str))
ok_rec = (rback == flat)
```

`flat` is derived from the same live `RECEIPT` dict that was serialised
one line earlier, so `ok_rec` compares **disk against live memory**,
never against a gate-time seal. Every object the receipt publishes at
3242–3331 is mutable between the gate that read it and the write.
INJ-1, INJ-3, INJ-5 and the five-way INJ-COMBO all ship with
`gate_failures 0`, `mutants_dead 0`, `verdict_audit []` and the
integrity line reading `output True, receipt True`. This is the U4
pattern (#123 MAJOR-3) recurring one unit later — the disease #119
generalises.

*And the write precedes the check.* `finish()` writes both files
(210–216) and only then re-reads them (220–227). On mismatch it prints
`ARTIFACT INTEGRITY GATE FAILED` and exits 1 **with the corrupt
artifacts left on disk** — no staging, no temporary, no `os.replace`.
INJ-2 demonstrates it: exit 1, and `giter_output.txt` sits in the
out-dir at 50444 bytes carrying `GITER-DEVIATION-<`, beside a receipt
whose `verdict` still says `GITER-LAW-CONFIRMED`. §3's sentence "Every
failure path writes nothing" is false for this one path. It is true for
all the others, which I confirmed by hashing (`--selftest`) and by three
real source corruptions — those do not even create the out-dir.

**REPAIR:** lift R4b's #119-native implementation verbatim (commit
`6d32993`, `v14/code/r4b_momentum_exact.py`: `SEALED_PATHS`,
`Seal.take`, staged write + `os.replace` after matching the seal). For
this unit the seal list is `verdict/string`, `verdict/head`,
`verdict/record`, `gates`, `mutants`, `anchors`, `totals`,
`quantum/eq22_rows`, `holonomy`, `deviation`, `targets`, `carrier`,
`anchor`, `law`, `provenance`, `supply`, `paper_sweep` — seal each when
its gate passes, build the receipt **from the sealed objects**, write to
a temporary, `os.replace` only after the disk bytes match the seal.

### MAJOR-3 — `G-OFFTREE-READY` IS GATED BY A TAUTOLOGY

`giter_exact.py:3051`

```python
_abs_ok = all(os.path.isabs(os.path.join(REPO, p)) for p in _reads)
```

`REPO` is absolute by construction, and `os.path.join(<absolute>, s)` is
absolute **for every string `s`** — including `''`, `'../../etc/passwd'`,
`'./rel'` and an already-absolute path. I checked eight shapes; all
eight give `isabs=True`. **`_abs_ok` cannot be False.**

So the predicate `_abs_ok and not _banned and not _movingref` reduces to
`not _banned and not _movingref`, which is `G-EXACT-AND-STATIC` minus its
float conjunct. The gate that claims

> "the run therefore reproduces byte for byte from any directory and
> with no version-control system present, and the property is a property
> of the code rather than of the checkout"

measures nothing about off-tree readiness. The clause that *would* have
meant something —
`sum(1 for p in _reads if os.path.exists(os.path.join(REPO, p)))` —
lives in the printed detail string only, never in the predicate.

**The property itself holds**, and I proved it twice empirically (§9).
Only the gate is empty.

**REPAIR:** replace `_abs_ok` with a predicate that can fail —
`all((not os.path.isabs(p)) and '..' not in p.split('/') and
os.path.exists(os.path.join(REPO, p)) for p in _reads)` — and register
`MUT-OFFTREE-RELATIVE` (a declared read path made absolute, or made to
escape the root) against **this gate's own name**.

### MAJOR-4 — COVERAGE IS COUNTED BY NAMING, THE STANDARD §11 SAYS IT DOES NOT USE

§11: "Coverage is measured by **reach** … a gate counts as covered only
when a declared falsifier turns that gate's own predicate from true to
false … Every MUST gate carries at least one such falsifier."

`G-COVERAGE` (3098) tests `len(NOFALS) == 0` where
`NOFALS = [g for g in MUSTS if not g['falsifiers']]` — the gate's own
*declaration list*, not the falsifier registry. Two measurements against
the delivered receipt instead:

**(a) The reach ledger has two holes.** 38 MUST gates; 54 falsifiers
registered against **37** distinct targets; reach histogram
`{1: 27, 2: 7, 3: 1, 4: 1, 6: 1}`. Two MUST gates have no falsifier
registered against them: `G-ATOM-BLOCK-SCOPE` declares
`MUT-DELTA-CARRIER-SWAP`, which is registered against
`G-COARSENING-LEMMA`; `G-OFFTREE-READY` declares `MUT-MOVING-REF`, which
is registered against `G-EXACT-AND-STATIC`. (Combined with MAJOR-3 this
is one finding: the gate advertising the #91 property both borrows its
falsifier and carries a vacuous conjunct.)

**(b) Three falsifiers evaluate a predicate that is not their gate's.**
I compared every mutant's `clean` expression to its target gate's `ok`
expression, resolving aliases: **21 are the gate's predicate verbatim,
30 are a conjunct of it, and 3 are neither** —

| falsifier | its clean predicate | its gate's predicate |
|---|---|---|
| `MUT-PATH-DRIFT` → `G-PROVENANCE` | `_pd` (a file-existence check) | `_bt_ok and _vb_ok and _probe_ok and _vb_drift` — carries no path conjunct |
| `MUT-RENEWAL-SCOPE-DROP` → `G-ANCHOR-RENEWAL-ROOT` | `VERBATIM[16][3] in _p09` | grading ∧ returns ∧ block entries — carries no quotation conjunct |
| `MUT-REPRICE-WAIVER` → `G-KERNEL-PROPER` | `_pr1 == 0 and _pos3 >= 0`; mutated `_pos3 == 0` | `_pr1 == 0 and _pr2 == 0` — `_pos3` is not in it |

The protections these three model are real (a drifted path raises at
`read_text`; a dropped quotation dies at the P0 precheck; a zeroed price
does break positivity) — but the registered pair is not a reach
demonstration of the named gate, which is the standard §11 sets.

**REPAIR:** strengthen `G-COVERAGE` to
`{g['name'] for g in MUSTS} <= {m['target'] for m in MUTANTS}`; add the
two missing registrations; and re-point the three off-target falsifiers
at gates whose predicates they actually turn false (or add the missing
conjunct to those gates).

### MAJOR-5 — ONE FALSIFIER IS A TAUTOLOGY, AND FIVE OF THE 41 NON-ANCHOR GATES CANNOT INDEPENDENTLY FAIL

*The tautology.* `MUT-WROUTE-UNCERTIFIED` (2266):

```python
mutant('MUT-WROUTE-UNCERTIFIED', 'G-B3-COUPLED', …,
       all(B3CPL[k]['certified'] for k in B3CPL),
       not all(B3CPL[k]['certified'] for k in B3CPL), …)
```

the mutated predicate is literally `not clean`. It injects nothing, it
cannot fail while the gate passes, and it reports `G-B3-COUPLED`'s
certificate conjunct as covered on the strength of a truth-table entry.
`MUT-EQ22-SIGN` (1938) is the same class one step weaker — its mutated
predicate is `[0, 0, 0, 0] == [36, 104, 108, 164]`, a
constant-versus-constant comparison consulting no measured object.
`MUT-REPRICE-WAIVER`'s clean side carries a vacuous conjunct
(`_pos3 >= 0`, always true of a count).

*The gates that cannot independently fail.*

| gate | why |
|---|---|
| `G-QUANTUM-STAMPED` (2025) | its `ok` argument is the literal `True` (disclosed under a waiver) |
| `G-OFFTREE-READY` (3052) | reduces to `G-EXACT-AND-STATIC`'s conjuncts once `_abs_ok` is seen to be a tautology (MAJOR-3) |
| `G-ATOM-BLOCK-SCOPE` (2493) | its predicate is a **strict sub-conjunct** of `G-COARSENING-LEMMA`'s (2465–2472) |
| `G-ANCHOR-PATH` (2589) | `ANCHOR_PATH == 'SEDIMENTARY'` is implied by `G-ANCHOR-RENEWAL-ROOT ∧ G-UNREACHABILITY-STAMP ∧ G-COARSENING-LEMMA`, which supply all four selector inputs |
| `G-SIX-PROPERTIES` (1396) | the conjunction of six gates already registered one at a time, and strictly weaker than three of them |

`G-SIX-PROPERTIES` is redundant by design and I do not object to it —
but it belongs in the denominator count.

**Honest denominators: 58 registered = 17 anchors + 41 gates, of which
36 can independently fail; 54 falsifiers, 51 reaching the gate they name
and 49 substantive.** Nothing else moves; the paper should print these
rather than "58 gates, 54 falsifiers". §11's clause "the only gates
without one are the two theorem-passes and the one disclosure" is also
wrong in part: `G-KERNEL-PROPER` is a theorem-pass and *does* carry
`MUT-REPRICE-WAIVER`.

### MAJOR-6 — THE #125 CLASS RECURS: BOTH PROHIBITION SCANS ARE CONTIGUOUS-LITERAL, AND THE BANNED-NAME AST SCAN NEVER LOOKS AT IMPORTS

This unit predates #125 and the engraving bites it in three places. All
measured on the delivered bytes.

**(a) The moving-reference guard (578) is whitespace-brittle, 4/4.**
`_movingref` is a raw substring scan of the file's own text for
`'git show HEAD:'`, `'HEAD~'`, `'origin/'`.

| spliced text | needle hits | verdict |
|---|---|---|
| `git  show HEAD:` (two spaces) | `[]` | **EVADED** |
| `git\tshow HEAD:` | `[]` | **EVADED** |
| `git show  HEAD:` | `[]` | **EVADED** |
| `git show\nHEAD:` | `[]` | **EVADED** |

*Repair (2 lines):* scan a whitespace-normalised haystack,
`re.sub(r'\s+', ' ', _src_text)`, against whitespace-normalised needles.

**(b) The census-shadow token scan (1624) is whitespace-brittle on one
of its nine tokens, 2/2.** `'MENU['` misses `MENU [h]` and `MENU\t[h]`,
both valid Python. (`GAM_C`, `GAM_M`, `CONG`, `IDX_C`, `holonomy_of`,
`gamma_family`, `CLOSED`, `MASS_C` are identifiers and are robust.)
*Repair:* strip whitespace from `_reg` before the scan, or ban `MENU`
bare.

**(c) `_banned` (566–572) never sees an import.** It collects only
`ast.Name.id` and `ast.Attribute.attr`; `ast.alias` names are never
collected. Measured evasions, 5/5:

| spliced | `_banned` | verdict |
|---|---|---|
| `import subprocess as sp` / `sp.run(['ls'])` | `[]` | **EVADED** |
| `from math import sqrt` / `x = sqrt(2)` | `[]` | **EVADED** |
| `import numpy as np` / `y = np.array([1])` | `[]` | **EVADED** |
| `from subprocess import check_output as co` / `co(['ls'])` | `[]` | **EVADED** |
| `from random import random as rr` / `z = rr()` | `[]` | **EVADED** |

Bare `import subprocess` also scores `[]` unless the name is later used.
*Repair (3 lines), inside the `ast.walk` loop at 566:*
```python
if isinstance(_nd, (ast.Import, ast.ImportFrom)):
    _names.update(a.name.split('.')[0] for a in _nd.names)
    _names.add((getattr(_nd, 'module', '') or '').split('.')[0])
```

**The substantive properties hold**, re-measured here: the file's imports
are exactly `ast, hashlib, json, os, re, sys, time,
collections.{Counter, defaultdict}, fractions.Fraction`; its tree carries
0 float constants; and a runtime audit hook over the whole provenance
layer records file `open` events only, never a process spawn. Only the
instrument is weaker than its statement.

### MAJOR-7 — THE COMPARATOR RE-AUDITS THE HEAD; IT DOES NOT RE-DERIVE IT

`G-VERDICT-EQUALITY` (2997) states that the head and every segment are
"RE-DERIVED BY AN INDEPENDENT RECONSTRUCTION that shares no code, no
input and no typed literal with the builder."

Two clauses hold, one does not. It shares no code (nothing in
`check_verdict` calls `segment` or reads `ALPHABET`) and no typed literal
— the outcome vocabulary is taken from the record and checked for
membership in the pin's own bytes, which is a genuinely good move. But it
does share the input: `_rec_json` is `json.dumps(RECORD)` and `RECORD` is
the builder's own output, and `SEGVAL` is
`[[str(v), text.count(str(v))] for v in values]` — the expected
occurrence counts are computed **from the very text the comparator then
counts**.

So it proves VERDICT ↔ RECORD consistency, exact span coverage, and
pin-membership of the alphabet. It cannot detect a wrong measured value
handed to `segment()`, because string and record would both carry it —
which is why all six `MUT-VERDICT-*` falsifiers mutate the string or the
record and none mutates a measurement. INJ-1 makes the point from the
other side: flipping `HEAD` after the comparator has run leaves
`verdict_audit []`.

**REPAIR:** reword to "re-audited by a reconstruction that shares no code
and no typed literal with the builder and re-parses a serialised record";
and add one conjunct that re-derives the head *selector* (`_law_ok`) from
the receipt's own published numbers rather than from `FLAGS` — which,
given MAJOR-1, is the same repair twice.

### MAJOR-8 — THE MECHANISM SENTENCE IS UNGATED

The `MECHANISM=` verdict segment and the abstract's "the whole signature
is carried by the 4 multi-target labelled edges … which sit on the 4 menu
classes that recur across depth cuts" are never machine-checked.
`_mt_src` (1976–1984) and `DEPTHPURE['MENU-113'][0]` (1955–1961) are
computed independently and **never intersected**; `_carrier_rel` (1986)
is four counts about CK failures and multi-target edges, none of which
touches recurrence.

I computed the containment myself: 4 multi-target edges on 4 distinct
MENU source classes, each occurring at depths `[1, 2, 3, 4]` and each of
size 313; 45 of 113 MENU classes recur; **4 of 4 source classes lie
inside the recurring set — the claim HOLDS.** It is carried by prose
alone.

**REPAIR (one conjunct):**
```python
_dep_menu = defaultdict(set)
for h in CARRIER:
    _dep_menu[MENU[h]].add(len(h))
_mech_ok = _mt_src <= {c for c, ds in _dep_menu.items() if len(ds) > 1}
```
add `and _mech_ok` to `_carrier_rel`, with a falsifier running the same
containment against the depth-*pure* classes, where it fails.

---

## 3. MINOR FINDINGS

**MINOR-1 — the pre-registered target triple is a typed literal with no
anchor to the pin.** `TARGET = [Fr(15, 38), Fr(5, 19), Fr(13, 38)]`
(1588). The pin does carry "(15/38, 5/19, 13/38)" (verified) and is
byte-anchored, and `check_verdict` reads the pin — but only for the
outcome alphabet. Nothing binds the literal to the bytes that
pre-registered it. *Repair:* one conjunct on `G-LAW-VALUE`,
`'(15/38, 5/19, 13/38)' in SRC['S-PIN']`, or a 20th verbatim window.

**MINOR-2 — "bound to a *registered* consumer gate" is a declaration,
not a binding.** All 19 consumer names do resolve to registered gates (I
checked each), but no gate predicate consults its own window, and only 8
of the 19 windows are ever quoted into the output. The mechanical
binding is the source's byte anchor, which is sound. §3 should read
"each declared against a registered consumer gate".

**MINOR-3 — the census-shadow scan is a nine-token list.** The
substantive property is clean and I corroborated it two further ways: I
enumerated every identifier inside the marked region (it references only
`CACHE`, `candidates_for`, `Fr`, `sk`, `is_R4` and its own locals) and
re-ran the scan with a 30-token ban list including `W[`, `MU[`, `G[`,
`kern(`, `PRICE`, `refine(`, `TARGET`, `SHADOW`, `EDGES`, `READ[`,
`DEPTHPURE` — 0 hits either way. **The #82 disease is provably absent**;
only the published instrument is narrower than the sentence.

**MINOR-4 — the receipt-only publication surface is 190 of 2046 scalar
leaves.** Values in `giter_receipt.json` with no counterpart anywhere in
`giter_output.txt`: 102 in `gates` (the `statement` prose), 54 in
`mutants` (the `injects` prose), 14 in `provenance`, 5 in `supply`, 2 in
`verdict_record`, and **8 in `quantum.eq22_rows`** — the `labels` cells
135 and 167 for the CONG-185 completions. With MAJOR-2 this is the whole
undefended surface: no gate binds them and no output line contradicts
them.

**MINOR-5 — `MUT-REPRICE-WAIVER`'s clean side carries a vacuous conjunct**
(`_pos3 >= 0`). Harmless; drop it.

**MINOR-6 — §3's "Every failure path writes nothing" is false for one
path** (the artifact-integrity path; MAJOR-2, INJ-2). All other failure
paths do exit before `finish()`.

---

## 4. THE SEAM RULING

**THE SEAM IS NINE WIDE.** Eleven injections; two caught, nine survive.
Every survivor is on the receipt side of one mechanism: *there is no
gate-time seal, so the receipt is built from live objects at 3242 and
verified against itself at 227.*

Calibration: R4b was 10-wide before its repair, weld-2 12-wide, U4
9-wide one layer down. This unit sits with them and for the same reason —
it predates #119.

Two things are genuinely defended and belong on the record, because they
are what keeps the width from being larger:

1. **The output stream is sealed at emission.** Any post-emission rewrite
   of `OUT_LINES` is caught by `DIGEST`. INJ-2 demonstrates it — this is
   the one thing this unit does that R4b and weld-2 did not.
2. **The registry-consistency check before the write** (3373–3381)
   catches tampering with `GATES`, `MUTANTS` or `COUNTS` **as counts**,
   cleanly and with nothing written. INJ-9 demonstrates it.

What is undefended is every *value* the receipt publishes.

## 5. THE INJECTIONS TABLE

Each injection was applied to a scratch copy of the delivered bytes and
run to completion as a full plain run with `--out-dir` redirected.
"Receipt leaves moved" is a leaf-by-leaf diff of the shipped receipt
against my clean run's, excluding `code_sha256_12` (which always moves,
because the injected file's own bytes differ — a property that is only
useful to someone comparing it against the pin by hand).

| # | injection | exit | files written | caught by | receipt leaves moved | verdict |
|---|---|---|---|---|---|---|
| INJ-1 | **post-gate head flip**: `HEAD = 'GITER-DEVIATION'` after `G-VERDICT-EQUALITY` | **0** | 2 | **nothing** | 1 | **SURVIVED** |
| INJ-2 | the emitted verdict line rewritten in `OUT_LINES` after emission | 1 | **2 (corrupt output left on disk)** | `DIGEST` — `ARTIFACT INTEGRITY GATE FAILED` | 0 | **CAUGHT — bytes still reached disk** |
| INJ-3 | **published quantum-table cell moved**: `EQ22['MENU-113','identity',(1,2,3)]` `negatives 36 → 99`, `most_negative '-1/97' → '-99'`, after `G-EQ22-STAMPED` | **0** | 2 | **nothing** | 2 | **SURVIVED** |
| INJ-4 | **post-write receipt corruption**: bytes appended after the artifact-integrity re-read | **0** | 2 | **nothing** | receipt **no longer parses as JSON** | **SURVIVED** |
| INJ-5 | **a control datum under a census label**: `READ[('CONG-185','q')] = READ[('REC','q')]` | **0** | 2 | **nothing** | **11** | **SURVIVED** |
| INJ-7 | a passed MUST gate's published `detail` rewritten to the opposite of what it measured | **0** | 2 | **nothing** | 1 | **SURVIVED** |
| INJ-8 | a published anchor row's `measured` value fabricated | **0** | 2 | **nothing** | 6 | **SURVIVED** |
| INJ-9 | **`COUNTS['gates'] = 999`** (positive control) | 1 | **0** | the final registry-consistency check | — | **CAUGHT, cleanly** |
| INJ-10 | `RECORD['segment_count'] = 99` after the comparator ran | **0** | 2 | **nothing** | 1 | **SURVIVED** |
| INJ-11 | `LAW2 = SHADOW2` — the census shadow published as the leg-2 law value | **0** | 2 | **nothing** | 3 | **SURVIVED** |
| INJ-12 | a verdict segment rewritten (`HOLONOMY=AGREES` → `LOCATED`) after the reconstruction ran | **0** | 2 | **nothing** | 1 | **SURVIVED** |

(INJ-7, -8, -10, -11, -12 were run together as one job, `INJ-COMBO`,
since they touch disjoint receipt fields and none is expected to be
caught; the shipped receipt carries all five, so each is independently
witnessed. Every survivor's `giter_output.txt` is **byte-identical to my
clean run** — the contradictions live entirely inside the receipt.)

**What the survivors actually shipped**, with `gate_failures 0`,
`mutants_dead 0`, `verdict_audit []` and
`[artifact integrity: output True, receipt True; files written: 2]`:

- **INJ-1:** `receipt['verdict_head'] = "GITER-DEVIATION"` beside
  `receipt['verdict']` beginning `GITER-LAW-CONFIRMED` and
  `outcome_flags [True, False, False]` — the head field contradicts the
  verdict string **inside the same file**.
- **INJ-3:** `eq22_rows["MENU-113|identity|(1, 2, 3)"].negatives = 99`
  while the same receipt's `eq22_menu_negatives` reads
  `[36, 104, 108, 164]`, the output prints
  `negative entries by triple [36, 104, 108, 164]` and the verdict
  segment reads `EQ22-NEGATIVES-36/104/108/164`.
- **INJ-4:** `giter_receipt.json` on disk ends
  `…}\nTAMPERED-AFTER-THE-INTEGRITY-GATE` and **no longer parses as
  JSON** — exit 0. Weld-2's #120 stated ceiling was "post-WRITE
  corruption reaches disk but fails loudly exit-1"; here it reaches disk
  and exits **0** with the integrity line printing `True, True`. That is
  strictly worse than the recorded ceiling.
- **INJ-5:** `holonomy["CONG-185|q"]` becomes the negative control's
  flat row entire — `closes 473` (not 1362), `obstruction 0` (not 44),
  `rank 0` (not 2), `nonunit 0` (not 44), `primes` gone, `selfspec`
  emptied — under the ruled carrier's own label, while the output and
  the verdict both carry the true reading.
- **INJ-7:** `gates[33]` is `G-HOLONOMY-HEAD`, `passed: true`, detail
  `"FABRICATED: r_k = r_q at 0 of 1362, deviations 1362"`.
- **INJ-8:** `anchors[0].measured = [9,9,9,9,9,9]` with **`ok: true`**,
  while the *same receipt's* `gates` row for `A-CENSUS-LEVEL` still reads
  `expected [1, 8, 60, 452, 3448, 26760], measured [1, 8, 60, 452, 3448,
  26760]`. Two published rows for one anchor contradict each other
  inside one file.
- **INJ-11:** `targets.law_value_leg2 = ['4/9','1/9','4/9']` — the
  declared census shadow published as a law value, which is exactly the
  #82 disease this unit was built to avoid, while the output's own line
  reads `leg 2 (15/38, 5/19, 13/38)`.
- **INJ-12:** `receipt['verdict']` carries `HOLONOMY=LOCATED` while the
  output *and the delivered paper* carry `HOLONOMY=AGREES`, and
  `verdict_audit` is `[]`.

## 6. THE #82 CLI UNDER HOSTILE ARGV — 18/18 CORRECT

| argv | exit | behaviour |
|---|---|---|
| `--help` | 0 | usage on stdout |
| `--help --help` | 0 | usage once, idempotent |
| `--list-mutants` | 0 | 54 names + the count |
| `--selftest` | 1 | refuses at the anchor precheck |
| `--selftst` (typo) | 2 | `unknown argument '--selftst'` |
| `--list-gate` (typo) | 2 | rejected |
| `--self` (abbreviation) | 2 | **no prefix matching** |
| `--HELP` (case) | 2 | rejected |
| `-h` (short form) | 2 | rejected |
| `--out-dir=/tmp/x` (flag=value) | 2 | rejected — no `=` form accepted |
| `--` | 2 | rejected |
| `""` (empty string) | 2 | rejected |
| `foo` (bare positional) | 2 | rejected |
| `--mutant` (missing NAME) | 2 | `--mutant needs a NAME` |
| `--out-dir` (missing DIR) | 2 | `--out-dir needs a DIR` |
| `--mutant NOPE` | 2 | `unknown mutant 'NOPE'; see --list-mutants` |
| `--zzz --help` | 2 | **fails on the unknown flag before honouring `--help`** |
| `--selftest --mutant MUT-CONG-COUNT` | 1 | selftest wins, writes nothing |

**`--selftest`, hash-proven.** Exit 1; the report reads `byte anchor
S-LAYER: expected 576275d55ecf, measured 576275d55ec0`, matching exactly
the corruption it made; the delivery is refused before a single
measurement; `shasum -a 256 giter_output.txt giter_receipt.json` is
**byte-identical before and after**, with no new file in the directory.

**And I corrupted anchors for real, not in memory.** Appending one byte
to `v10/note-d74-transport-holonomy-result.md`, then to
`v14/note-gprep-adjudication.md`, then to
`v14/paper-09-renewal-transport.md`, each in a fresh scratch mirror:
3/3 exit 1 at the precheck, each naming the right anchor with its true
measured sha (`0180e21c7127→4fc2b106dd9c`, `fdd8c76d7b29→f5654eefb32d`,
`006f96aaa2ff→c178f9f793ab`), and in all three cases the `--out-dir`
**was never even created**. The report matches reality.

**`--mutant NAME`.** Run to completion on scratch:
`--mutant MUT-HOLONOMY-HEAD --out-dir <watched>` exits **0**, prints
`[mutant MUT-HOLONOMY-HEAD: KILLED at G-HOLONOMY-HEAD; files written: 0]`,
and emits **exactly one** falsifier line —
`[KILLED] MUT-HOLONOMY-HEAD -> G-HOLONOMY-HEAD`, so the isolation is
real and the kill is at the *named* gate. The `--out-dir` had been
seeded with a clean artifact pair, and both files are **byte-identical
before and after**. The property is structural as well as measured:
`WRITES_ALLOWED` is `(not SELFTEST) and (MUT_ONLY is None) and not
LIST_GATES` (127), and `finish()` — the only writer — is reached only
after the `MUT_ONLY` branch has already exited at 3369. Unknown names
exit 2 before any work.

**`--list-mutants` is complete.** The printed registry is exactly the 54
names of `MUTANT_REGISTRY`, and the run's own pre-write consistency check
proves `sorted({m['mutant'] for m in MUTANTS}) == sorted(MUTANT_REGISTRY)`
— 54 evaluated, 54 declared, 0 dead, in the delivered receipt and in both
of my clean runs.

## 7. COVERAGE AT #34, AND GATES-BIND-OBJECTS AT #87

**Denominators, from the receipt rather than the prose:** 58 registered
gates = 38 MUST + 17 ANCHOR + 2 THEOREM-PASS + 1 DISCLOSURE, all passed;
54 falsifiers, all killed, 0 dead. After MAJOR-3/4/5: **36 of the 41
non-anchor gates can independently fail; 36 of the 38 MUST gates are
covered by reach; 51 of 54 falsifiers reach the gate they name and 49
are substantive.**

**The three waivers, each forcing machine-checked — verified.**
- `G-SUPPLY-FIFTH-BLOCK`: the waiver claims the (3,3) block's point count
  inside this arena is *measured* to be 0. It is — `(3, 3) not in BLOCKS`
  over the measured holdings-profile census, and I independently
  reproduced that census (`{(1,1): 1365, (2,2): 3788, (2,3): 4,
  (3,2): 4}`, no `(3,3)`). ✓
- `G-KERNEL-PROPER`: the waiver claims re-pricing every priced event
  leaves 0 violations. Measured (`_pr2 == 0`), with a substantive
  companion (`_pos3 > 0` under a zeroed price). ✓ — subject to MAJOR-4(b)
  on where its falsifier is registered.
- `G-QUANTUM-STAMPED`: the waiver claims the four stamped claims each
  carry their own MUST gate and that this gate is not counted as
  evidence. Three gates are named for four claims (Chapman–Kolmogorov
  sits inside `G-CONG-LUMPABLE`), and the gate's own predicate is the
  literal `True`. Honest, but it is the one literally-cannot-fail gate
  and should say so. ✓ with a wording fix.

**#87 — three questions, three answers.**

1. *The six carrier properties, each on its own object?* **YES.** Six
   separate MUST gates, one per property, each with its own falsifier
   evaluated at a contrast object, plus the conjunction. This is the
   cleanest part of the instrument and I reproduced all six independently.
2. *The quantum table, per cell?* **NO — 8 of 32 cells, one field of
   four.** `EQ22` publishes 32 cells (2 carriers × 4 completions × 4
   triples) with up to five fields each. `G-EQ22-STAMPED` binds
   `MENU_NEG == [36, 104, 108, 164]` and the equality of the two speaking
   completions' negatives — 8 cells of the `negatives` field — plus the
   two `EQ_SPEAK` aggregates. **`labels`, `colsums_one`, `most_negative`
   and `certificate` are bound by nothing** at either carrier. I
   recomputed the whole table and every published cell is correct; the
   binding is per-field, not per-cell — and INJ-3 is what that costs.
   *Repair:* extend the gate to `colsums_one` and the label counts, or
   seal `quantum/eq22_rows` per #119.
3. *The 1362 squares, per square or aggregate?* **Aggregate, and
   adequate.** `AGREE['CONG-185'] = (1362, 0)` is a pair of counts, but
   the published claim is `bad == 0`, and a zero-count over a universally
   quantified predicate *is* the per-square conjunction — one deviating
   square increments it. Likewise `ID_VIOL == 0` over 1546 and
   `_atom_bad == 0` over the 72 testable classes. I re-enumerated all
   1546 closed squares and confirm 1362/1362 with 0 deviations and 0
   identity violations. No repair needed.

## 8. THE EXCLUSION AUDIT — CLEAN

paper-13 (`v14/paper-13-weld2-carrier-census.md`, pinned `535e288ff412`)
is declared-and-not-read per #46/#91, and **nothing consumed it.** Three
independent routes:

- *Textual:* exactly two occurrences of `paper-13` in the delivery file,
  both inside the `EXCLUDED` declaration (309–318); no occurrence of
  `weld2`, `WELD2` or `535e288ff412` outside it.
- *AST:* `read_text` has exactly three call sites — the `SOURCES` loop
  (299), the file's own source (563), and paper-16 (3155). `SOURCES`
  does not contain the path; `SRC` never acquires an `S-WELD2-PAPER` key.
- *Runtime:* I ran the provenance layer under `sys.addaudithook` and
  logged every `open`. Result: the 13 declared sources, the file's own
  bytes, and stdlib caches — nothing else. `paper-13 opened: False`.

**The 13 byte anchors:** all 13 recomputed from the committed tree at
`9e481db`; 13/13 match their declared sha256-12.

**The 19 verbatim windows:** all 19 re-measured — lengths 44–149
characters (floor 40 satisfied 19/19), located **exactly once** 19/19,
and content-flipping 19/19 under the delivery's own `scramble`, which
perturbs the *last alphanumeric run* and is therefore a content-bearing
edit, not a whitespace edit (the #62 requirement). All 19 consumer names
resolve to registered gates. Caveat at MINOR-2.

**The 11 path-value probes:** all 11 re-resolved directly against the two
pinned receipts; 11/11 resolve and 11/11 match their declared values. An
unresolvable probe does abort (507–512) rather than being swallowed.

## 9. DETERMINISM: THE FIX IS REAL, AND I HUNTED THE CLASS

**The fix.** `G-REFINE-DETERMINISTIC` (826) is the found-and-fixed bug.
`refine()` traverses `sorted(dom, key=sk)` rather than a set, and the
gate compares the forward and reversed traversals **as a set of blocks**
(`blocks_of`, 817) while *disclosing* that the class indices differ —
which is exactly the right pair of statements. `MUT-REFINE-ORDER` turns
the index-level comparison false, so the weaker predicate a hash-seeded
traversal would pass by luck is demonstrably weaker. The fix is correct
and the falsifier is honest.

**The class hunt, by AST over every iteration site in the file:**

- Iteration directly over a set object: **one site**, `check_verdict`
  (2965), `for r in {x for x in runs if len(x) >= 3}` — order-safe,
  because the candidates are then `cands.sort()`ed on `(len(r), r,
  parts)` with `r` drawn from a set and therefore distinct, so `cands[-1]`
  is a total order.
- `next(iter(...))`: **one site**, `rsig` (2297), guarded two lines above
  by `len(nsup['A']) != 1 → return None`.
- `.pop()`: three sites (721, 1489, 1538), all on **lists**; in each case
  the order-dependent product is either summed in exact arithmetic
  (`positional`) or re-sorted (`R2BASES = sorted(...)`, `_sub`/`_uns`).
- Every dict whose insertion order reaches a published value is built by
  iterating `sorted(..., key=sk)` (`gamma_family` 1207, `padded` 1842,
  `_byc` 2451, `_ei` 2745, `SCR` 2705) or is a `Counter` accumulated over
  a sorted list (`hol` in `holonomy_of`, edges sorted at 1042;
  `selfl`/`FACSPEC`/`SPEC_Q` over the sorted `CLOSED`).
- `sk()` is hash-order-free by construction: a `frozenset` becomes
  `("S", tuple(sorted(...)))`.

**Empirically.** I ran the delivery's own source truncated just before
the heavy [B3] LP — covering the carrier, the six properties, holonomy,
Γ, CK, the targets, the census shadow and the whole quantum layer — under
`PYTHONHASHSEED` ∈ {0, 1, 4242} and compared 18 structures per run,
including the `CONG` label map, the `CONG` index multiset, `IDX_C`, the
`GAM_C` key order, the raw-order hash of `CLOSED`, the `EQ22` digest, the
`OUT_LINES` digest and the emitter's own `DIGEST`. **All three seeds give
one identical result block.**

**And end to end.** Two full plain runs, both byte-identical to the
committed artifacts (`58ddd86a52f2…` / `8d28b5f2f807…`): run A off-tree
in a `.git`-less mirror with `--out-dir` redirected and the default
*random* hash seed; run B in the same mirror under
`PYTHONHASHSEED=4242` — **the fourth seed**, the worker having claimed
three. A third reproduction happened at another reviewer's hands: the
repository's `giter_output.txt` and `giter_receipt.json` are unchanged
after a concurrent in-place plain run.

## 10. COMPARATOR INDEPENDENCE (#82-STRENGTHENED)

**The head derivation:** MAJOR-7 — re-audit, not re-derivation, and one
clause of the gate statement is an overclaim. What it does verify it
verifies well: the outcome vocabulary is taken from the pin's own bytes
(2940–2942), the separator is *characterised* rather than quoted
(2954–2977), the spans are proved to cover the string exactly (2980), and
six falsifiers mutate the string or the record in six different ways. All
six kill.

**The census-shadow scan:** clean, corroborated two further ways
(MINOR-3). The #82 disease is provably absent.

**Shared literals hunted:** one found (MINOR-1, `TARGET`). Otherwise the
comparators are pinned bytes (13 sha anchors), pinned receipt values (11
probes), or committed census values typed as `anchor()` expectations —
and I re-derived all **17 anchor expectations** from the pinned layer
myself: `[1, 8, 60, 452, 3448, 26760]`, `[1, 9, 69, 521, 3969, 30729]`,
`3969`, `113`, `2477`, `[1, 5, 17, 49, 113]`, `[1, 5, 13, 45, 113]`,
`['2','4','257/32','1035/64','4173/128']`, `{AB-only 28, BA-only 12,
both-blocked 142, closed 1546}`, `{1/2: 70, 2/3: 2, 3/2: 6, 2: 10}`,
`88`, `3584`, `16`, `256`, `5161`, `1365`, `{(1,1): 1365, (2,2): 3788,
(2,3): 4, (3,2): 4}` — 17 of 17 reproduced.

**The three-way sweep paper ↔ output ↔ receipt.** The paper carries
**exactly 750 numeric tokens, 111 distinct** — the claimed count, with my
own tokeniser. Of the 111 distinct tokens, **108 occur in both the output
and the receipt**; `40` and `3/4` occur in the output only (the "at least
40 characters" disclosure and the first-return law's verbatim quote, both
non-receipt), and `243769` occurs in the receipt only (the excluded d ≤ 6
arena size, inside a `supply.reason` the output prints without its
reason). **Zero paper numerals are absent from both.** On top of that I
ran 44 *semantic* spot checks — "the paper's row X equals the receipt's
field Y", not token presence — across the carrier, law, holonomy,
quantum, [B3], anchor, supply and instrument rows: **44 of 44 agree.**

**The verdict string** is byte-identical in all three artifacts: 3023
characters, 8 segments, present verbatim in the paper (line 496), in the
output, and as `receipt['verdict']`. All 13 declared arena coordinates
appear in the paper's §2 table and every arena value string is echoed in
the output — §15's match-every-coordinate discipline holds.

## 11. WHAT HOLDS, AT MY OWN HANDS

Independently recomputed from the pinned layer bytes upward, with my own
implementations, all agreeing with the delivery:

- **The carrier.** 3969 histories; per-level census `[1, 8, 60, 452,
  3448, 26760]`, cumulative `[1, 9, 69, 521, 3969, 30729]`; CONG-185 =
  **185 classes after 5 refinement rounds**; round trace
  `[(1,162,17), (2,179,5), (3,184,1), (4,185,0), (5,185,0)]` — depth
  purity first reached at round **4 of 5**, the spanning count falling
  17 → 5 → 1 → 0 → 0; dims `[1, 5, 17, 49, 113]`; MENU-113 dims
  `[1, 5, 13, 45, 113]`; REC 2477.
- **The six ruling properties.** Descent multi-valued **0** at CONG
  against **4** at MENU; labelled edges **572, 0 multi-weight, 0
  multi-target** at CONG against **368 with 4 multi-target** at MENU;
  square census `{closed 1546, AB-only 28, BA-only 12, both-blocked
  142}` with **88 defective** and spectrum `{1/2: 70, 2/3: 2, 3/2: 6,
  2: 10}`; CONG closes **44 of 88** and MENU closes 44 with **symmetric
  difference 0** (the set identity, not the count); q-holonomy at CONG
  primes `[2, 3]` **rank 2**, obstruction 44; k-holonomy at CONG primes
  `[2, 3]` **rank 2** against MENU's `[2, 3, 5, 13]` **rank 3** — the
  enlargement does disappear; Chapman–Kolmogorov **0 of 10** at CONG,
  **4 of 10** at MENU with differing cells `[34, 112, 12, 12]`, 0 of 10
  at REC. MENU scores **2 of 6**.
- **The law.** 102 columns over 10 cut pairs, 0 failing to sum to 1, 0
  negative; cut mass exactly 1 at all 5 cuts; flow identity **3968 of
  3968**, 0 violations, and **352 of 596** failing at every other
  admissible horizon.
- **The targets.** 16 renewal-1 bases, **3584** leg-1 legs; COUNT
  `(3/7, 1/7, 3/7)`, RAW `(3/8, 1/4, 3/8)`, **step-normalised
  `(15/38, 5/19, 13/38)`**; `k₁ = q/M` violations **0 of 30728**; `k₂`
  violations **1340 of 3968**; M(h) takes 2 distinct values.
- **Holonomy.** r_k = r_q at **1362 of 1362** closing squares with **0**
  deviations at CONG; 1394 of 1402 with 8 at MENU; deviation identity
  **0 violations of 1546**; **8** non-unit correction factors, spectrum
  `{64/65: 6, 65/64: 2}`, **0 of them on CONG-closing squares and 8 on
  MENU-closing squares**; REC flat at both readings (obstruction 0,
  non-unit self-loops 0, primes `[]`, rank 0, 473 squares closing).
- **The quantum table**, all 32 cells: @MENU-113 identity and cyclic
  **speak** with negatives `[36, 104, 108, 164]` and all column sums 1;
  uniform and marginal **silent**; @CONG-185 **all four silent** at label
  counts `[71, 135, 167, 179]`.
- **The mechanism** (ungated — MAJOR-8): 4 multi-target edges on 4
  distinct MENU source classes, each at depths `[1, 2, 3, 4]` and of size
  313; 45 of 113 MENU classes recur; 4 of 4 source classes inside the
  recurring set.
- **The anchor.** Classes at more than one depth: **0 of 185** at CONG,
  **45 of 113** at MENU; prefix-class returns **0** at CONG, **1900** at
  MENU; R-SIG 5161 points, blocks `{(1,1): 1365, (2,2): 3788, (2,3): 4,
  (3,2): 4}`, R-MENU 1365; **30728** transitions with the (1,1) block
  entered from outside at **0** while (2,2) is entered at 1700 and the
  two small blocks at 4 each — the stamp is a property of one block,
  exactly as the gate says.
- **The instrument's own numbers.** 58 gates (38 MUST + 17 ANCHOR + 2
  THEOREM-PASS + 1 DISCLOSURE), all passed; 54 falsifiers, all killed, 0
  dead; 13 byte anchors, 19 verbatim, 11 path-value; 3 waivers; 750 paper
  numerals, 0 unexplained; 0 float constants; exact-stdlib imports only.

**Zero false computed numbers found anywhere in the delivery.**

## 12. REPAIR ORDERS (liftable, in priority order)

| # | order | where | size |
|---|---|---|---|
| R-GI-1 | make the outcome selector a partition, and gate that it is one on all four `(_law_ok, ID_VIOL)` combinations | 2800 + a new falsifier | 1 line + 1 `mutant()` |
| R-GI-2 | adopt the #119 gate-time seal: seal at gate time, build the receipt **from the sealed objects**, write through a temporary and `os.replace` only after the disk bytes match the seal | `finish()` 205–239, `RECEIPT.update` 3242 | lift `SEALED_PATHS`/`Seal`/staged write from `v14/code/r4b_momentum_exact.py` @ `6d32993` |
| R-GI-3 | give `G-OFFTREE-READY` a predicate that can fail, and register a falsifier against its own name | 3051–3067 | 2 lines + 1 `mutant()` |
| R-GI-4 | make `G-COVERAGE` test **reach**: `{g['name'] for g in MUSTS} <= {m['target'] for m in MUTANTS}`; add the missing registration for `G-ATOM-BLOCK-SCOPE`; re-point `MUT-PATH-DRIFT`, `MUT-RENEWAL-SCOPE-DROP`, `MUT-REPRICE-WAIVER` at gates whose predicates they turn false | 3098–3113 + three `mutant()` rows | 1 predicate + 3 rewrites |
| R-GI-5 | replace the tautological `MUT-WROUTE-UNCERTIFIED` with a real injection (a coupled verdict accepted with a *falsified* Farkas vector); make `MUT-EQ22-SIGN` consult the measured census; drop `_pos3 >= 0` | 2266, 1938, 2785 | 3 rewrites |
| R-GI-6 | whitespace-normalise both prohibition scans; add `ast.Import`/`ast.ImportFrom` names to `_banned` | 566–578, 1620–1624 | 5 lines |
| R-GI-7 | bind the mechanism claim: add `_mt_src ⊆ recurring` to `_carrier_rel` with its own falsifier | 1976–1989 | 1 conjunct + 1 `mutant()` |
| R-GI-8 | anchor the pre-registered target triple to the pin's bytes | 1588 / `G-LAW-VALUE` | 1 conjunct |
| R-GI-9 | extend `G-EQ22-STAMPED` to `colsums_one` and the label counts, so the quantum table is bound per cell rather than per field | 1919–1937 | 1 conjunct |
| R-GI-10 | correct four sentences — §3 "Every failure path writes nothing" (false for the integrity path); §3 "bound to a registered consumer gate" → "declared against"; §11 "the two theorem-passes and the one disclosure" (one carries a falsifier); §11/§13 print the honest denominators (36 independently-falsifiable of 41 non-anchor gates; 51 of 54 falsifiers reaching, 49 substantive) | paper §3, §11, §13 | wording |

None of these moves a delivered number. R-GI-1 and R-GI-2 are the two
that change what the instrument can do.

## 13. WHAT I DID NOT REACH

- **Leg 2 was not independently re-enumerated** (73728 legs over 256
  bases at the pruned scan). I verified leg 1 (3584) from scratch and the
  prune gate's logic by reading; leg 2's value rests on the two
  byte-identical whole-run reproductions.
- **The [B3] LP verdicts were not independently re-solved.** 772 row
  problems and 8 coupled problems in exact rational simplex. I verified
  the solver's certificate discipline by reading (both verdicts
  certified; primal point re-substituted; Farkas vector re-checked) and
  the aggregate counts from the receipt, but did not re-implement the
  simplex. That is the effectus and operator seats' ground.
- **`--list-gates`** was not run end to end (a full ~20-minute run that
  prints a registry I enumerated statically as 41 `gate()` + 17
  `anchor()` = 58, matching the receipt exactly).
- The machine carried heavy concurrent load from other seats throughout;
  wall-clock figures in my runs are not comparable to the delivery's.
