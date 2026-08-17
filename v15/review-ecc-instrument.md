# ECC (paper-46) — K3 INSTRUMENT-SEAT REVIEW (FROZEN)

**Seat:** K3, the INSTRUMENT seat. **Jurisdiction:** whether
`v15/code/ecc_exact.py`'s gates actually catch what they claim to catch,
under live hostile injection. **Method:** off-tree `rsync` mirror
(`.git` excluded) at
`/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/ecc_k3/`.
The repo was read-only to this seat except this one review file. Every
injection edited a mirror copy only, ran one process, was checked for
death gate + whole-tree hash, then restored; the mirror returned to its
baseline whole-tree hash `77513e0220f9d8f76d769f10fecf7bffa9be6a8a661a8bf82ecbe4ae5bc1c5e6`
after every injection and at campaign end.

## UNIT UNDER REVIEW (digests verified at start)

| file | committed sha256-12 | verified |
|---|---|---|
| v15/paper-46-ecc.md | 61d330d13fe0 | yes |
| v15/code/ecc_exact.py | 4d2034429d21 | yes |
| v15/code/ecc_output.txt | 3034f0028bb3 | yes |
| v15/code/ecc_receipt.json | ea24c1fc2340 | yes |
| v15/note-ecc-pin.md | 04874b01e241 | yes |

Baseline `--verify-paper v15/paper-46-ecc.md` in the mirror: PASS, rc 0.

---

## VERDICT: ACCEPT-WITH-FIXES

The instrument's **core is sound**. Every forged value, flipped word,
direction flip, seal-window edit, both integrity windows, object-under-test
drop, and determinism (repr / builtin-hash) mutant dies at its correct
declared gate with the tree byte-intact; all 12 hostile argv forms exit
rc 2 writing nothing; the 73-recipe registry `--selftest` sweep is
write-nothing and each recipe dies at its declared gate; the comparator is
genuinely de-twinned from disk (a disk-forged receipt leaf cannot reach the
head); clean delivery is byte-identical across three `PYTHONHASHSEED`
values and reproduces the committed artifact hashes exactly.

Two **paper-surface prose-scanner coverage gaps** survived and are the
basis for the FIXES qualifier; neither touches the measurement / seal /
determinism / verdict machinery, and neither construct appears in the
paper as committed (both are hostile transplants):

1. **F-1 (severity MEDIUM, NEW disease):** a slash-rational `a/b` planted
   in prose escapes `G-PAPER-COVERAGE` because the numeral scanner splits
   it into integers `a` and `b`, each backed elsewhere — even though the
   receipt carries the atomic rational string. Demonstrated to stand a
   false **committed Born weight** (`4/9`→`5/9` in the prose of §6),
   producing a fence/table-vs-prose contradiction the instrument does not
   catch.
2. **F-2 (severity MEDIUM):** the bare sentence *"The Born rule is derived
   here."* passes every wall and the polarity blocklist — `WALL-W1`'s
   negative leg requires the "…derived **from the record**" form and its
   licence-leg subject requires a reproduction word, so a naked derivation
   claim about a policed noun falls in the coverage hole between them.

Plus one LOW scoped note (F-3, `G-DETERMINISM` AST scope) and one
by-design observation (K3-36). None of these rises to MAJOR-REPAIRS: the
load-bearing verdict positions (tables, fences, registered claims,
sealed values, the head) are all defended, as the 35 killed injections
show. A fix pass closing F-1 and F-2 lifts this to ACCEPT.

---

## THE FULL INJECTION TABLE (39 live injections)

Legend: tree-intact `yes` = whole-tree hash unchanged across the run
(failing runs write nothing). `NO*` = a **passing** run (rc 0) whose only
artifact delta is the object-under-test digest correctly re-recording the
edited paper (proven below: only `object_under_test`, `seal_manifest`,
`transcript_digest` move; no measured value moves). Mirror restored to
baseline after every row.

| id | edit | declared/expected gate | observed (gate, rc) | tree-intact |
|---|---|---|---|---|
| K3-01 | committed-row qmax 4/9→5/9 in T-COMMITTED table | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-02 | census count INFEASIBLE 136→137 in T-LPWORDS | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-03 | census count UNIQUE 8→7 in T-LPWORDS | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-04 | census count MANY 6→5 in T-LPWORDS | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-05 | two-step fiber cell 25\|9→25\|10 in T-FIBER | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| **K3-06** | **gap 7/3→5/3 in prose (digits 5,3 both covered)** | (predicted survive) | **NONE, rc 0** | **NO\*** |
| K3-06b | interface OBJECTS=23→24 in state-contract fence | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-07 | INFEASIBLE→FEASIBLE at committed E-LINE-COSET row | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-08 | UNDERDETERMINED→MEASURED at seam verdict fence | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-09 | INDEPENDENT→RESOLVED at psi verdict fence | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-10 | UNSELECTED→SELECTED at carrier verdict fence | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| K3-11 | direction flip PERSIST-FIT-DIFFERS 108-OF-108→0-OF-108 (fence) | G-PAPER-CLAIMS | G-PAPER-CLAIMS, rc 1 | yes |
| **K3-12** | **plant "The Born rule is derived here."** | (predicted survive) | **NONE, rc 0** | **NO\*** |
| K3-13 | plant "the Born rule is derived from the record" | G-WALLS | G-WALLS, rc 1 | yes |
| K3-14 | plant seam-persistence as measured | G-WALLS | G-WALLS, rc 1 | yes |
| K3-15 | plant family-level label on member-specific claim | G-WALLS | G-WALLS, rc 1 | yes |
| K3-16 | plant bare-negation "not" into a wall licence list (code) | G-WALLS | G-WALLS, rc 1 | yes |
| K3-17 | plant spelled fraction "two thirds of the rows" unjustified | G-PAPER-FRACTION | G-PAPER-FRACTION, rc 1 | yes |
| K3-18 | take a seal AFTER SL.close() (post-final-gate window) | G-SEAL-TOTAL | G-SEAL-TOTAL, rc 1 | yes |
| K3-19 | edit sealed value (chart) after last gate, before door | G-INTEGRITY | G-INTEGRITY, rc 1 | yes |
| K3-20 | edit sealed value (coin) after door verify, before serialize | G-INTEGRITY | G-INTEGRITY, rc 1 | yes |
| K3-21 | drop the object-under-test line from the transcript | G-OBJECT-UNDER-TEST | G-OBJECT-UNDER-TEST, rc 1 | yes |
| K3-22 | add builtin-hash-keyed sort to scanned source (MUT-HASH species) | G-DETERMINISM | G-DETERMINISM, rc 1 | yes |
| K3-23 | add bare-repr-keyed sort to scanned source (MUT-SORT species) | G-DETERMINISM | G-DETERMINISM, rc 1 | yes |
| **K3-24** | **genuine os.listdir-order dependence in a census sort** | (predicted survive gate) | **NONE, rc 0** | **yes** |
| K3-25 | registry mutant MUT-SIMPLEX | G-LP-COMMITTED | G-LP-COMMITTED, rc 1 | yes |
| K3-26 | registry mutant MUT-CEILING | G-LP-CEILING | G-LP-CEILING, rc 1 | yes |
| K3-27 | registry mutant MUT-VERDICT | G-VERDICT-RECON | G-VERDICT-RECON, rc 1 | yes |
| K3-28 | registry mutant MUT-SEAMWORD | G-SEAM-DECISION | G-SEAM-DECISION, rc 1 | yes |
| K3-29 | registry mutant MUT-OBJECT | G-OBJECT-UNDER-TEST | G-OBJECT-UNDER-TEST, rc 1 | yes |
| K3-30 | registry mutant MUT-A2 | G-LP-DEGENERATE | G-LP-DEGENERATE, rc 1 | yes |
| K3-31 | registry mutant MUT-HASH | G-DETERMINISM | G-DETERMINISM, rc 1 | yes |
| K3-33 | reflexive of-fraction "18 of 18" in prose | G-PAPER-REFERENT | G-PAPER-REFERENT, rc 1 | yes |
| K3-34 | cross-universe pair "27 of the 288" in prose | G-PAPER-REFERENT | G-PAPER-REFERENT, rc 1 | yes |
| K3-35 | period-blind-spot probe: 4242 at sentence end | G-PAPER-COVERAGE | G-PAPER-COVERAGE, rc 1 | yes |
| **K3-36** | **spelled cardinal "ten" (=10) in prose** | (predicted G-PAPER-SPELLED) | **NONE, rc 0** | **NO\*** |
| K3-37 | polarity: "the lp is feasible after all" in prose | G-PAPER-POLARITY | G-PAPER-POLARITY, rc 1 | yes |
| K3-38 | forge receipt leaf on disk then --verify-paper | PASS (head must not consume it) | PASS, rc 0 | yes |
| K3-39 | delete object line from output.txt on disk then --verify-paper | PASS (not consumed) | PASS, rc 0 | yes |

**Kill rate at the correct declared gate:** 35/35 of the death-expected
injections. **Survivors (rc 0 where a catch was in question):** K3-06,
K3-12 (real gaps), K3-24 (no-impact scoped blind spot), K3-36 (by-design).

### The `NO*` mechanism (proven, not asserted)

For a passing forged-prose run I diffed the produced receipt against the
committed one: the only keys that move are `object_under_test`,
`seal_manifest` (which carries the object-under-test seal), and
`transcript_digest` (which carries the object line). **No measured value
moved.** So the three `NO*` rows are passing delivery runs that honestly
re-fingerprinted a different paper; the "failing runs write nothing"
property is intact across the whole campaign (every rc-1 row is
tree-intact `yes`).

---

## AUXILIARY BATTERIES (all independent of the 39 above)

**CLI — 12 hostile argv forms, all rc 2, nothing written** (tree hash
unchanged after the whole battery):
`--selftest --numbers`; `--numbers --numbers`; `--mutant MUT-SOURCE
--list-mutants`; `--verify-paper` (missing operand); `--verify-paper
/etc/hosts` (out-of-repo); `--verify-paper v15/code` (directory-as-file);
`--frobnicate`; `--mutant BOGUS`; `--no-write --no-write`; `--mutant
MUT-SOURCE --mutant MUT-SOURCE`; `--selftest --mutant MUT-SOURCE`;
`v15/paper-46-ecc.md` (bare positional). Mode-conflict, repeated-flag,
missing-operand and mutant-plus-listing pairs are all refused with the
usage code; the two out-of-repo / directory cases exit 2 with a specific
message.

**--selftest (mirror):** `recipes 73; deaths at the declared gate 73;
moves proved 73; artifacts unchanged: True; rc 0`. Whole-tree hash after
the sweep equals baseline — the sweep is genuinely write-nothing.

**Determinism (clean):** clean delivery run under `PYTHONHASHSEED` ∈
{1, 3735928559} produced byte-identical `ecc_output.txt` /
`ecc_receipt.json`, both equal to the committed hashes
(`3034f0028bb3…`, `ea24c1fc2340…`).

**Determinism (mutated dies, not varies):** a repr-key sort injected into
the scanned source dies at `G-DETERMINISM` under `PYTHONHASHSEED` ∈
{0, 12345, 2147483647} — it dies rather than silently varying.

**Recipe realism (no no-op falsifier):** inspected `MUT-SIMPLEX` —
genuinely zeroes the LP target RHS `b`, which flips E-LINE-COSET to
feasible (the zero-writer cosets carry the mass), moving a real
measurement, not a counter. Noted: `MUT-CEILING` and `MUT-DEBT` are
counter-bump recipes (`ceiling_exceptions += 1`, `in_cross += 1`); they do
move a **sealed, published** scalar the gate reads and the clean-run value
of that scalar is honestly recomputed from primitive rows at the gate — so
they are legitimate gate-liveness recipes, not no-ops, though thinner than
`MUT-SIMPLEX`.

**Comparator de-twinning / receipt-leaf forge:** the head consumes only
freshly-built in-memory primitive tables — a receipt leaf forged **on
disk** cannot reach it (K3-38 PASS), and `MUT-VERDICT`/K3-27 confirms the
comparator recomputes the head from primitive rows and dies when they are
moved. A subsequent real delivery run overwrites the disk-forged receipt
back to the committed bytes; the artifact-integrity guarantee lives in the
delivery run + pin digest, not in `--verify-paper`.

---

## FINDINGS

### F-1 — slash-rational in prose escapes coverage (MEDIUM; NEW disease for TPL-2)

`G-PAPER-COVERAGE` scans paper numerals with `NUM_RE`, which tokenizes
`"5/3"` into the integers `5` and `3`; `collect_ints` backs each integer
independently from the receipt, so any prose slash-rational whose
numerator and denominator are separately covered passes — **even though
the receipt carries the atomic rational string** (e.g. the committed E-TRIPLE
gap `"7/3"` and the committed weight `"4/9"` are both present verbatim in
`ecc_receipt.json`).

Live confirmations (each `--verify-paper` PASS, rc 0):
- `gap 7/3 → 5/3` in §6 prose ("exact infeasibility gaps 4, 4, 3 and 7/3")
  — the K3-06 campaign row.
- **Escalation:** the committed Born weight `4/9 → 5/9` in §6 prose
  ("post-coin weight of 4/9 on each of two cells") — passes while the
  verdict fence (`QMAX-4/9`) and the T-COMMITTED table still read `4/9`, an
  internal contradiction the instrument does not surface. The same forge
  **inside the fence or the table** dies at `G-PAPER-CLAIMS` (K3-01, K3-07),
  so only the prose restatement is unguarded.

This is distinct from the registered "spelled fractions/proportions"
species (word fractions like "two thirds", caught by `G-PAPER-FRACTION`,
K3-17) and from the "period-regex numeral blind spot" (closed, K3-35):
it is a **compound-token split** — the scanner never forms `a/b` as an
atomic value, so the receipt's atomic rationals are never compared against
the paper's. **Suggested fix:** add a leg to `G-PAPER-COVERAGE` (or a
sibling gate) that scans the paper for `\d+/\d+` slash-rationals and
requires each to equal a rational string present in the sealed receipt
(the Born-weight / gap tables already carry them).

### F-2 — bare "X is derived here" escapes the reconstruction wall (MEDIUM)

*"The Born rule is derived here."* passes all nine walls and the polarity
blocklist (K3-12, PASS rc 0). `WALL-W1-RECONSTRUCTION`'s negative leg
matches only the "…is derived **from the record**" form (so the paraphrase
K3-13 correctly dies at `G-WALLS`), and its licence leg only fires for
sentences whose subject is a reproduction word
(`reproduc*|reconstruct*|identifiab*` / "two routes agree"). A naked
derivation claim about a **policed noun** ("the Born rule … derived"),
without "from the record" and without a reproduction subject, falls in the
gap between the two legs; no other wall pairs subject *Born* with policed
*derived*, and the phrase is not on the `G-PAPER-POLARITY` blocklist
(which does catch "the lp is feasible after all", K3-37). **Suggested
fix:** broaden `WALL-W1`'s negative leg to
`the (born rule|cast|state|seam|carrier) (is|was|are) derived\b` without
requiring "from the record", or add the bare form to the polarity
inversion list.

### F-3 — determinism gate AST scope is repr/hash only (LOW; scoped clarification)

`G-DETERMINISM` scans for bare-repr sort keys and builtin-`hash()` calls;
a genuine `os.listdir`-order dependence injected into a census sort (K3-24)
is **not** flagged (rc 0). It produced **no** artifact change here because
the instrument's pervasive canonicalization (`ekey` sorts everywhere,
`to_json` set-sorting, `json.dumps(sort_keys=True)`) absorbs the ordering
perturbation — output stayed byte-identical (tree-intact `yes`), so there
is no exploitable nondeterminism in this instrument. This is a scope note,
not a live defect: the gate's guarantee is precisely "no repr-key and no
builtin-hash ordering", and `PYTHONHASHSEED`-invariance is separately
demonstrated; an author who later introduced BOTH a filesystem-order
source AND an order-sensitive serialization would escape this gate. No fix
required for acceptance; optionally document the gate's declared scope.

### K3-36 — spelled "ten" passing is BY-DESIGN, not a finding

*"The sweep visited ten arenas here."* passes (rc 0) because the spelled
scanner maps "ten"→10 and `10` is a covered receipt value, so it is backed
exactly as the digit "10" would be. `G-PAPER-SPELLED` is a **value-backing**
check (parity with digits), not a semantic-truth check; the same is true
of any covered digit. This is within the paper's stated coverage contract
("every numeral … backed by a receipt value or a declared exemption") and
is not a defect. It shares the general value-vs-semantics limitation with
F-1, but is not itself an escape — F-1 is, because the slash-rational's
atomic value is never checked at all.

---

## NEW-DISEASE REGISTRATION FOR TPL-2

**SLASH-RATIONAL-IN-PROSE (the compound-token-split coverage species).** A
prose exact rational `a/b` is split by the numeral scanner into integers
`a` and `b`; `G-PAPER-COVERAGE` backs each independently, so a false
rational whose numerator and denominator are each covered elsewhere passes
— while the sealed receipt carries the atomic rational string it should be
compared to. Distinct from spelled-fraction/proportion (word fractions)
and from the period-regex blind spot (both already gated). Gate it by
scanning `\d+/\d+` in the paper and requiring each to match a receipt
rational string, sentence-scoped and hedge-aware like the existing
fraction leg. Demonstrated to admit a false committed Born weight in prose
(`4/9`→`5/9`) contradicting the fence and table.

---

## SEAT SUMMARY (one paragraph)

As the INSTRUMENT seat I ran 39 live off-tree injections plus a 12-form
CLI battery, the 73-recipe `--selftest` sweep, a two-value clean-seed
determinism proof, a three-seed mutated-mirror determinism-death proof,
and two on-disk-tamper de-twinning tests, restoring the mirror to its
baseline whole-tree hash after every one. The instrument's core does what
it claims: forged values, flipped words, and direction flips in every
load-bearing position (tables, fences, registered claims) die at
`G-PAPER-CLAIMS`; the seam/psi/carrier/LP/ceiling/degenerate mutants and
the de-twinned comparator die at their exact declared gates; the
post-final-gate seal window and both freeze/serialize integrity windows
are closed (`G-SEAL-TOTAL`, `G-INTEGRITY`); the object-under-test digest
lives in both artifacts and its loss is caught; determinism is
`PYTHONHASHSEED`-invariant and the repr/hash species are AST-banned; every
hostile argv exits rc 2 and every failing run writes nothing. The only
escapes are in the paper-surface prose scanner: a slash-rational planted
in prose (F-1, a NEW compound-token-split disease that admits a false
committed `4/9`→`5/9` Born weight contradicting the checked fence/table)
and a bare "The Born rule is derived here." that slips the reconstruction
wall's "from the record" negative leg (F-2). Both are real but bounded
coverage gaps that leave the receipt/seal/verdict machinery untouched and
do not appear in the paper as committed; closing them lifts the unit from
**ACCEPT-WITH-FIXES** to ACCEPT.
