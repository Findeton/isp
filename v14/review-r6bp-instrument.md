# R6b′ (paper-09) — HOSTILE REVIEW, REVIEWER R3 (INSTRUMENT LENS)

**Object.**  The frozen R6b′ delivery, hashes verified before and after
all work: paper `68c20d1fdae4`, code `8e188dd3ab70`, output
`42a39fcaf194`, receipt `50f63b3ba362`.  Protocol
`v14/note-r6bp-hostile-protocol.md` `1cf5fc8b3272`; pin
`v14/note-r6bprime-transport-pin.md` `17111fd19022`.  All work on
copies in scratch; one repo write (this file); no git writes.

**GRADE: ACCEPT-WITH-FIXES.**

Every physics number in the delivery reproduces exactly by my own
route — `61` independent exact recomputations, **zero false numbers in
the receipt or the output**.  The verdict rebuilds byte-for-byte from
the receipt alone.  All `31` declared mutants die, each by its named
gate, with no tracebacks.  Two runs are byte-identical.  What fails is
the *instrument's account of itself*: the never-falsified census
carries `21` false coverage claims over its `46` rows, the
verbatim-context anchor mechanism — this unit being its first at-scale
deployment — is demonstrably existence-binding only with all three of
the #34 modifications inert, four false paper numbers and three
inverted paper quotations survive at exit 0, and the delivery is **not
re-runnable in the repository as it now stands**.  Two of these are
recurrences of already-engraved diseases and are therefore MAJOR by
default (§13 addendum, v13 #313).

---

## Execution counts

| | |
|---|---|
| instrument subprocess executions | `133` |
| — plain delivery runs (scratch mirrors) | `4` |
| — `--selftest` (spawning `31` subprocess mutant runs) | `1` (+`31`) |
| — `--mutant` runs over the `31` declared mutants | `62` (two full sweeps) |
| — targeted R3 injections | `26` |
| — source/paper/pin corruption runs | `6` |
| — CLI-contract probes (`--list-mutants`, float guard) | `3` |
| independent recomputations | `205` |
| — exact arithmetic recomputed from the pinned sources | `61` |
| — census rows re-derived from measured mutant deaths | `46` |
| — distinct backticked paper tokens traced (`135` occurrences) | `59` |
| — verdict segments rebuilt from the receipt alone | `7` |
| — paper quotations checked against the pinned sources | `8` |
| — verbatim anchor rows audited | `24` |
| false numbers found in receipt or output | `0` |
| injection classes proven to SURVIVE undetected (exit 0) | `4` |

**Reproduction of the delivery.**  I rebuilt the run environment in
scratch (a fresh git repo whose `HEAD` carries the R6a receipt bytes
the pin names, `022c3f488a93`) and reproduced the delivered
`output.txt` **byte-identically except for three occurrences of one
string**: the disclosed working-tree hash `94adec72ab11`.  The receipt
differs at the same three places and nowhere else.  Two consecutive
runs in the mirror are byte-identical in both artifacts.

**CLI contract.**  Verified in code and by execution: plain run writes
both artifacts and exits `0`; `--selftest` writes nothing and exits `0`
iff every mutant dies by its named target; `--mutant NAME` writes
nothing; `--list-mutants` prints `31` names.  Exit `2` on anchor
failure and exit `3` on the float guard are both reachable and were
both observed (`3` by an injected float literal).  Exit `1` on gate
failure observed `28` times.  `--mutant` does not validate its
argument against `MUTANTS`, which is what let me drive targeted
injections without perturbing `mutant_count`.

---

## M1 (MAJOR) — the delivery is not re-runnable: the provenance mechanism binds to *mutable* git state, and the disclosed bytes no longer exist anywhere

The unit reads the R6a receipt at its **committed** bytes via
`subprocess.run(["git","-C",REPO,"show","HEAD:"+rel])` and anchors the
result against `022c3f488a93`.  `HEAD` is not a pin.  Commit
`d5fb2a5` (v14 #52, "R6a repair committed as-is") moved that blob to
`856f6e810ab5`.

**Measured, by execution.**  A mirror whose `HEAD` carries the current
blob — i.e. the repository as it stands today — exits `2`:

```
[ANCHOR-FAIL] A-R6A: v14/code/r6a_refinement_receipt.json
              expected 022c3f488a93 got 856f6e810ab5
ANCHOR FAILURES: 1
```

The anchor behaves correctly: it dies loudly and emits no verdict.  But
the consequence is that **no one can regenerate this delivery**, and
the RUNBOOK §5 adjudicator re-run is now impossible without rewriting
the code.  Worse, the delivered artifacts print `94adec72ab11` as the
working-tree disclosure, and that blob is unrecoverable: I scanned the
object store by size band around both candidate sizes (`102 994` and
`210 693` bytes) and it is not present, not in any commit, not
dangling, not stashed.  The delivered `output.txt` and `receipt.json`
therefore contain a hash of a file that no longer exists in any form.

**The three-part mechanism, audited separately.**

* *committed-bytes-via-git-show* — **fails**.  `HEAD:` is exactly the
  "mutable repo state" the #46 engraving forbids.  A commit-pinned read
  (`git show <sha>:<path>`, the sha written into the unit's frozen
  declaration) would be immune, would have produced the identical
  bytes, and would still be re-runnable today.
* *dual-hash disclosure* — **fails as delivered**.  Disclosing the hash
  of an uncommitted file makes the delivery's own bytes depend on an
  object that is never preserved.  A disclosure must be of something
  recoverable, or it must not enter the artifacts.
* *the path-value stability gate* — **passes, and is the good part**.
  I measured it at `24` consumed path-values (not `12`; the protocol's
  figure is low).  It survives a strictly harder test than the one it
  was written for: re-run with R6a's **TERMINAL** receipt
  `856f6e810ab5` as the working-tree file, all `24` path-values are
  still identical, `0` moved.  The substantive claim — that nothing
  R6b′ consumes from R6a moved across the repair — holds at R6a's final
  bytes, which the delivery could not have known.

**Provenance recommendation: MODIFY, do not adopt as the standard.**
Adopt the stability gate as written.  Replace the `HEAD:` read with a
commit-sha read declared in the unit's own frozen text, and require
that any hash printed into a delivered artifact be the hash of a
committed object.  With those two changes the mechanism is the right
standard for concurrent-unit reads; as delivered it trades
reproducibility for disclosure and loses both.

---

## M2 (MAJOR, recurrence of the R3 M1 class → #46) — a must-pass gate's outcome is a function of another unit's uncommitted working file

`load_json_worktree(R6A_RECEIPT)` reads the live working tree.  Its
result decides `G-R6A-REPAIR-DELTA`, a **must-pass** gate: had any of
the `24` consumed path-values differed in R6a's in-flight tree, the
unit would have exited `1` and produced no verdict.  The unit's own
compliance sweep does not carry a #46 row at all — the engraving is
the most recent of the eight and the sweep lists fifteen rules, none of
them #46 — yet the paper's header claims "all seven 2026-08-09
engravings gated at birth" while the RUNBOOK carries **eight**
2026-08-09 engravings.  The missing one is precisely the one this gate
violates.

This is the disease R3 M1 named and #46 engraved: *"reading mutable
repo state (ledgers, STATUS, **other units' working files**) is
forbidden — a verdict segment depending on an unanchored read is an
ungated verdict."*  Here the dependence is on a must-pass gate rather
than a verdict segment, which is the same failure with a louder
failure mode.

**Exact repair.**  Compare the pin-named committed bytes against a
second **committed** revision (R6a's own delivered receipt and its
terminal receipt, both by sha).  Delete the working-tree read.  The
measured content of the claim is unchanged — I verified it holds
against `856f6e810ab5`.

---

## M3 (MAJOR, recurrence of R6a M5) — the verbatim-context anchor binds EXISTENCE only; all three #34 modifications are inert in their first at-scale deployment

R6a M5 found the verbatim-text anchor "binds EXISTENCE only" and
recommended ADOPT WITH MODIFICATION.  #34 adopted it with three
binding modifications.  I tested each by execution.  All three are
cosmetic.

### (i) "evaluated before byte anchors" — true only as list order

`register_anchors()` calls the `24` `anchor_verbatim` rows before the
`16` `anchor_file` rows, so a failure appears first in
`FAILED_ANCHORS`.  There is no short-circuit: the run proceeds, every
gate is evaluated, the exit code is `2` either way.  Measured (A1,
needle broken inside the window in a scratch copy of paper 31):

```
[ANCHOR-FAIL] V-S1-SCOPE: context window absent from …paper31…md
[ANCHOR-FAIL] A-S1-PAPER31: …expected 7ac66f3fe74d got c36f5c859c85
```

Both fire.  "Before" buys ordering in a list, nothing else.

### (ii) the R6a T1 disease — **SURVIVES UNDETECTED at exit 0**

Injection **A2**: in a scratch copy of paper 31 I preserved the
`V-S1-SCOPE` window byte-for-byte and inverted its meaning around it —
prefixed *"The following paragraph was WITHDRAWN in erratum E-9 and is
reproduced here only as a superseded claim; it does NOT state this
section's scope"*, and appended *"CORRECTED STATEMENT: the class
structure of §3.2 IS stable under the transport grammar; the scope seam
named above does not exist."*  I then re-pinned `A-S1-PAPER31` to the
corrupted file's hash, which is the honest model of the case that
matters: a pinned artifact whose quoted sentence is faithful and whose
standing is the opposite of what the unit says it is.

**Result: exit `0`.  All `75` anchors hold, all `48` gates pass, and
the unit emits**

```
R6BP-BLOCKED-AT-THE-SCOPE-SEAM<…|S1-DECLARES-THE-CLASS-STRUCTURE-NOT-STABLE-ACROSS-IT>
```

against a source that now declares the exact opposite.  A context
window is a longer fragment.  It binds that a string occurs; it cannot
bind that the string is in force.

The "context window" framing is also not what ships.  Measured over
the `24` rows: `min 44`, `max 220`, `mean 106` characters, `2 546`
total.  These are fragments by size; the protocol's "480-byte-class"
description does not match the delivery.

### (iii) "each row bound to a named consumer gate" — **SURVIVES UNDETECTED at exit 0**

The `consumer_gate` field is written into the receipt and read by
nothing.  Injection **R3-CONSUMER-UNBIND** rewrites *every* verbatim
row's consumer to `G-NO-SUCH-GATE-AT-ALL`.  **Exit `0`.**  No gate, no
census, no sweep compares the field against the gate list.

The binding is not merely unchecked; it is largely pointed at gates
that cannot fail:

* `7` of `24` verbatim rows name a consumer gate whose predicate is the
  **literal `True`** — `V-S1-SCOPE`, `V-S2-SCOPE`, `V-S3-GAMMA`,
  `V-S3-POSIT`, `V-S4-RENEWAL`, `V-S5-CHOSEN`, `V-S5-CHOSEN2`.
* `12` of `24` name a consumer gate that **no declared mutant ever
  falsifies** (see M4).
* Under A1, with the bound text physically absent from the pinned
  source, both `G-SCOPE-SEAM` and `G-DELIVERY-FREE-SCOPE` — the two
  gates that carry the seam headline and the scope qualifier — printed
  `[PASS]`.

**Verbatim-anchor recommendation for the era: KEEP, but only as a
QUOTE-FIDELITY anchor, and MODIFY the standard.**  The mechanism has
one real and worthwhile function, which it discharges: it proves the
unit's quotations are not fabricated.  Keep it for that and say so.
The three #34 modifications should be replaced by two that bite:

1. **Bind the paper, not the code.**  Every quotation the *paper*
   prints must be an anchored window (see M5: three paper quotations
   can be inverted at exit 0 today).  This closes the surface the #20
   engraving opened for numbers but not for quotes.
2. **A consumer binding must be a predicate, not a label.**  Require
   that the named consumer gate exist in the gate list, that its
   predicate be non-literal, and that at least one declared mutant
   falsify it.  Any row failing this is a DISCLOSURE row and may not be
   counted among the must-pass anchors.

Do not claim that a context window binds meaning to use.  It does not,
and A2 is the measurement.

---

## M4 (MAJOR) — the waiver audit at the #34 standard: `21` of the `46` census rows make a FALSE coverage claim, `18` gates are falsified by no declared mutant, and the WAIVED-VERIFIED branch is dead code

The unit's headline is *"Never-falsified census: `0` unwaived"* over
`46` rows, all `46` classed `FALSIFIER-REACHES-IT`.  The predicate that
produces that status is

```python
killers = [mn for mn in sorted(mutant_names) if mn in g["injection_falsifier"]]
if killers: status = "FALSIFIER-REACHES-IT"
```

— a **substring test on a declared string**.  It verifies that the
gate's falsifier field is spelled like a declared mutant.  It never
checks that the mutant makes the gate fail.  That is the #34 disease
verbatim (*"the named mutant must reach and be killed by the gate"*),
recurring at the very census the #34 engraving created.

I rebuilt the census from **measured deaths**: `31` mutant executions,
every `[FAIL] <GATE>` line collected, `46` rows re-derived.

**Result: `21` of `46` rows are false.**  `18` of those gates fail
under *no* declared mutant at all; `3` fail only under a mutant other
than the one they name.

| gate (census says FALSIFIER-REACHES-IT) | declared falsifier | actually fails under |
|---|---|---|
| `G-S1-HARMONIC` | INJ-S1-ROUTE-DRIFT | — (drift hits route C; the gate reads route P) |
| `G-AS-TERMINATION` | INJ-DEFECT-ARITHMETIC | — (`ret=7/8` still satisfies `ret<1`) |
| `G-DELIVERY-FREE-SCOPE` | INJ-VERBATIM-DRIFT | — (literal `True`) |
| `G-SCOPE-SEAM` | INJ-VERBATIM-DRIFT | — (literal `True`) |
| `G-TYPE-CENSUS` | INJ-VERBATIM-DRIFT | — (literal `True`) |
| `G-S5-DISCLAIMER` | INJ-VERBATIM-DRIFT | — (literal `True`) |
| `G-SCOPE-HONESTY` | INJ-VERBATIM-DRIFT | — (literal `True`) |
| `G-PIN-BOUND` | INJ-FILE-ANCHOR-DRIFT | — (literal `True`; the mutant drifts `A-S1-PAPER31`, not `A-PIN`) |
| `G-POSITIONAL-STRATUM-EMPTY-AT-3` | INJ-VERBATIM-DRIFT | — |
| `G-COVER-DISSOLVED` | INJ-VERBATIM-DRIFT | — |
| `G-BRIDGES-READING` | INJ-ARENA-CENSUS | — |
| `G-CRB-SIMPLEX` | INJ-PATH-DRIFT | — |
| `G-TRANSVERSE-LINKS-UNFORCED` | INJ-PATH-DRIFT | — |
| `G-FRONT-RULE-INTEGRAL` | INJ-PATH-DRIFT | — |
| `G-R6A-RECLASSIFICATION` | INJ-PATH-DRIFT | — |
| `G-EXTREMAL-INTRINSIC` | INJ-PATH-DRIFT | — |
| `G-METRIC-RESTRICTION-REVERIFIED` | INJ-ADDITIVITY | — |
| `G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD` | INJ-FIBER-REBUILD | — |
| `G-POSITION-INDEPENDENCE-AT-DELIVERY-FREE-SCOPE` | INJ-S2-PROFILE | INJ-POSITION-MAP |
| `G-COLLAPSE-IS-DISTRIBUTION-NOT-VALUE` | INJ-S2-PROFILE | INJ-POSITION-MAP |
| `G-EXTREMAL-NOT-RATIFIED` | INJ-S2-PROFILE | INJ-POSITION-MAP |

Three further defects in the same block:

* **`6` must-pass gates have the literal `True` as their predicate** —
  `G-DELIVERY-FREE-SCOPE`, `G-SCOPE-SEAM`, `G-TYPE-CENSUS`,
  `G-S5-DISCLAIMER`, `G-SCOPE-HONESTY`, `G-PIN-BOUND`.  Per the #208
  addendum these are disclosures, not must-pass gates; they are counted
  inside the paper's "`48` must-pass gates, `0` failures".  They carry
  the delivery-free scope qualifier, the scope-seam head, the C1 type
  error, S5's disclaimer, the not-constructed declaration, and the pin
  binding.
* **The `WAIVED-VERIFIED` branch is never reached.**  The `ANALYTIC`
  set names `21` gates, and `0` rows take that branch, because every
  gate's falsifier string happens to spell a declared mutant.  The
  waiver text — a single boilerplate paragraph asserting that a listed
  injection perturbs the gate "through its consumer anchor" — is
  therefore dead code that was never evaluated, and would have been
  false for `18` of the `21` had it been.  A gate no execution path
  evaluates may not appear as waived (#34); here the *waiver machinery
  itself* is that dead path.
* **The census omits `2` of the `48` gates.**  `census_rows` is built
  from `GATES` before `G-WAIVER-CENSUS` and `G-GATE-COUNT` are
  registered.  Both happen to be killable, so nothing is hidden, but
  the coverage claim is `46` of `48`.

**Kills I obtained against the shadowed gates.**  `G-AS-TERMINATION` is
the one carrying `TERMINATES-A-S=TRUE`.  Its predicate is
`ret < 1 and defect > 0`; conditional on `G-RENEWAL-DEFECTIVE` passing
(`ret == 13/16`) it is analytically forced.  Driving `defect → 0`
directly does not produce a gate failure — it produces a
`ZeroDivisionError` in the gate's own detail string (`1/defect`), i.e.
the gate cannot be falsified without crashing the run.  `G-PIN-BOUND`:
I appended a line to the pin in a mirror; `A-PIN` fired (exit `2`) and
`G-PIN-BOUND` printed `[PASS]` — the gate is inert and no declared
mutant drifts the pin.  `G-COVER-DISSOLVED` fails if
`rows_pinning_cover_objects` is flipped, but see M7: that variable is
typed, never measured.

**Exact repair.**  Compute the census from measured deaths, not from
declared strings: run the mutant set (or consume the selftest's
per-mutant `[FAIL]` sets) and set `FALSIFIER-REACHES-IT` only when the
gate is observed to fail.  Then `18` rows become `UNWAIVED` and must be
given real falsifiers or demoted to disclosures.

---

## M5 (MAJOR) — four false paper numbers and three inverted paper quotations survive at exit 0; the #20 engraving is closed for absence but not for substitution

`G-PAPER-CLAIMS` checks that each of `25` receipt values appears
*somewhere* in the paper as a backticked token.  `G-PAPER-NUMBER-SWEEP`
whitelists every stringified receipt value anywhere in the receipt,
plus a `~40`-element structural literal set.  Neither binds a number to
the sentence that carries it.

**Injection A6b — SURVIVES UNDETECTED, exit `0`.**  In a scratch copy of
the paper I swapped four numbers, all of which remain receipt values:

* §13: "`16` file-bytes … `24` verbatim-text" → "`24` file-bytes …
  `16` verbatim-text";
* §6, the fiber-collapse table: "no split (count 1) `29`" ↔ "kernel
  hole (count 2) `50`".

Exit `0`; `unmatched_numbers` empty; `claims_found 25 of 25`.  The
second swap falsifies the paper's central classification table — the
`50`-interval support hole becomes `29` — and the instrument is silent.
(The verdict block's own `50` is protected, because
`G-PAPER-VERDICT` compares the seven segments verbatim.  The prose
table is not.)

**Injection A5 — SURVIVES UNDETECTED, exit `0`.**  I inverted three of
the paper's eight italic quotations:

* S1's caveat → *"At NO scope will the picture change…"*;
* S4's theorem tag → *"[THEOREM at ALL scopes, including transport]"*;
* S5's disclaimer → *"the coefficients 1/4 are DERIVED, not chosen"*.

Exit `0`.  The three inversions destroy the delivery-free scope
qualifier, the scope seam, and the chosen-not-derived carry — the three
things the unit says it carries everywhere — and the `24` verbatim
anchors do not see them, because they anchor the *code's* windows, not
the paper's renderings.

**Audit of the delivered paper's quotations (a positive).**  All `8`
italic quotations are byte-exact substrings of their pinned sources
under markdown normalisation.  Two notes: the S1 block quote runs
`~110` characters past the end of the anchored `V-S1-SCOPE` window
(that tail is quoted but unanchored), and it truncates the source's
"(§7, successor 2)" without an ellipsis.  The receipt's
`transport_scope_caveat_verbatim` is a hand-typed `340`-character
string; it *is* a byte-exact substring of the source, but only its
first `204` characters are anchored.

**Exact repair.**  Bind claims positionally (a short context string
around each number, or render the paper's numeric spans from the
receipt), and add the paper's quotations to the anchor set.

---

## M6 (MEDIUM) — two "RE-VERIFIED" gates are tautologies; one survives garbage input at exit 0

`G-ADDITIVITY-REVERIFIED` counts violations of `n1 + n2 != n` where
`n2` is *defined* as `n - n1` two lines above.  The predicate is
unsatisfiable over the integers; `add_viol` is `0` for every possible
input.  Its only real content is `add_checks > 0`, which is exactly
what `INJ-ADDITIVITY` (which sets `add_checks = 0`) tests.  The paper's
"`647` split constraints … with `0` violations" is an algebraic
identity, not a verification.

`G-METRIC-RESTRICTION-REVERIFIED` is the same shape: `q11 = Fr(a)`,
`q22 = Fr(bb)`, `q12 = Fr(c-a-bb, 2)`, then it checks `q11 == a`,
`q22 == bb`, `q11 + 2*q12 + q22 == c`.  All three hold by construction.

**Injection R3-ADDITIVITY-GARBAGE — SURVIVES UNDETECTED, exit `0`.**  I
replaced the counts feeding the restriction re-verification with
`7n + 1` garbage.  `G-METRIC-RESTRICTION-REVERIFIED` printed `[PASS]`
at `67 of 67` and the run exited `0`.  This is the #219 class: the
comparator is routed through the object under test.

The paper's sentence "the readout recovers every censused count from
the rebuilt form, `67` of `67`" should read as a stated identity.  A
real gate would rebuild the counts from an independently expressed
readout and compare against the receipt's `record_family`.

---

## M7 (MEDIUM) — typed-not-measured verdict fields, and the comparator is not independent for them

The §13 engraving is "counts computed, never typed", and the unit's
compliance sweep asserts it MET.  Four verdict fields are typed
literals:

```python
variational_rows = 0            # -> EXTREMAL-BAR<…|VARIATIONAL-ROWS-0-OF-6|…>
rows_pinning_cover_objects = 0  # -> COVER=DISSOLVED<ROWS-PINNING-COVER-OBJECTS-0-OF-6|…>
rows_deperiodizing_the_arena = 0
"TERMINATES-A-S=TRUE"           # typed in verdict AND comparator
```

Nothing enumerates the six pinned rows to establish that none declares
a variational principle, pins a cover object, or de-periodises the
arena.  `COVER=DISSOLVED` is entirely a self-consistency check on typed
zeros, and **no declared mutant flips the COVER segment** (measured
over all `31`).

The independent-comparator claim is true for the measured fields and
false for these.  Measured, by variable identity: the comparator shares
`variational_rows`, `rows_pinning_cover_objects`,
`rows_deperiodizing_the_arena`, and `closed` with the emitted side, so
`INJ-CLOSED-CLASS` is caught by `G-CLOSED-CLASS` and `G-PAPER-VERDICT`
but **not** by `G-VERDICT-EQUALITY`.  The architecture is right where
it is used — `INJ-CONTROL` dies at `G-VERDICT-EQUALITY` precisely
because the emitted CONTROLS segment is typed while the comparator
reads the measured qualifiers — which shows the shared-variable cases
are an omission, not a design.

**Segment-flip matrix over the `31` declared mutants** (fields, not
head names): KERNEL-DERIVED `3`, TRANSPORT-UNMOTIVATED `4`,
KERNEL-DEFECTIVE `4`, BLOCKED-AT-THE-SCOPE-SEAM `1` (`INJ-S2-PROFILE`
only), EXTREMAL-BAR `2`, COVER `0`, CONTROLS `0` in the emitted string.
All four heads' fields are flippable; I flipped each again with
targeted inputs (`R3-CRB-SIMPLEX-DRIFT`, `R3-TV-ZERO`,
`R3-DEFECT-13-16`, `R3-CENSUS-DROP`), all killed.

**No head NAME is selected by measurement.**  All four
`R6BP-*` head strings and the `BLOCKED-AT-THE-SCOPE-SEAM` fact name are
typed unconditionally on both sides.  `INJ-VERDICT-CLASS` proves the
comparator catches a *post-hoc* class swap; it does not show that any
measurement could have produced a different class.  This is a real
limit on "every segment flippable" and should be stated in the paper
rather than left implicit.

---

## M8 (MEDIUM) — the identification inventory's class labels have no gate of their own

`G-IDENTIFICATION-CENSUS` checks `len(candidates) == 5`,
`len(motivated) == 0`, and that each qualifier agrees with its own
inventory.  It does not check any item's class.

**Injection R3-IDENT-RELABEL**: relabel one genuinely-free item of C2 as
FORCED (C2 keeps `4` free items, so it stays UNMOTIVATED).
`G-IDENTIFICATION-CENSUS` printed `[PASS]`.  The run died **only** at
`G-PAPER-VERDICT`, because the verdict's `FREE-ITEMS=…C2-…:5` string is
copied into the paper.  The paper is the sole witness for the
inventory numbers `3/1/2/1/0` forced, `1/0/0/0/1` stabilizer,
`3/5/1/3/1` free — a witness that would be regenerated alongside any
future change.  The inventory is the unit's core measurement (the pin's
registered measurement 1) and it needs a gate that reads the item
classes.

---

## M9 (MINOR) — dead and no-op control code

* NC2's exclusion check is `if path in json.dumps(R.get("anchors", []))[:0]`
  — the `[:0]` slice is the empty string, so the condition is always
  false and `excluded_reached` is always `0`.  The variable is then
  never used.  (The *effective* check, `excluded_cited`, does work: it
  compares the four named exclusions against the anchor artifacts and
  correctly returns `[]`.)
* NC3's "measured cardinality mismatch" is not measured:
  `if (n + 1) - 1 != n` is unsatisfiable and
  `mismatch_type_ok = False` is typed.  The paper's "fails on a
  measured cardinality mismatch, not on taste" overstates a typed
  Boolean.

---

## M10 (MINOR) — the "two genuinely independent routes" are two transcriptions of one computation

Route P parses paper 31's fenced `6×6` block; route C AST-extracts
`T_REF` from d43b.  Both are **hard-coded literals**.  Neither
recomputes the transfer.  d43b's own terminal run gated
`rows == T_REF` against a real enumeration of the `215` length-`≤3`
histories, so the value is well-founded — but the unit's routes verify
*transcription fidelity between two renderings of one verified
object*, not two derivations.  `G-S1-ROUTE-PROVENANCE` tests only that
the two files differ (`route_c_source != P31` and their hashes differ),
which `INJ-S1-ROUTE-SAME-SOURCE` duly kills.  The paper's "rebuilt by
two genuinely independent routes" should read "read from two distinct
pinned artifacts and cross-checked entry by entry".

Related, and to the unit's credit: `R3-HOLE-BOTH-ROUTES` (fill `f(2)`
in the closed form **and** in the taboo iteration, consistently) still
dies — but at the explicit `closed_form[1] == 0` clause, not by route
disagreement.  The two-route agreement is not what catches it.

---

## K1–K5 at instrument depth

**K1 — the derived kernel.**  Re-derived by my own route from the
pinned chain, `61` exact recomputations, all agreeing:
`T f = 2 f` at `f = (4,4,3,7,3,3)/3`; row sums `(2,2,2,5/2,2,2)`;
paper 31's fenced block equals d43b's `T_REF` entry for entry; `q′`
normalises on all six rows; conflict row `{0: 1/7, 3: 3/4, 5: 3/28}`;
one closed class `{2,4,5}`, transient `{0,1,3}`; `h[1] = 1/4`,
`h[3] = 4/7`, `h[2]=h[4]=h[5]=0`; return `13/16`, defect `3/16`, visits
`16/3`; the first-return law agrees termwise with an exact taboo
iteration at all `400` terms; `f(1)=3/4`, `f(2)=0`, `f(3)=1/256`,
`f(4)=3/512`; total mass `13/16` **analytically**
(`3/4 + (1/256)·Σ m(3/4)^{m-1} = 3/4 + 16/256`); defective mean `21/16`
**analytically** (`3/4 + (112 + 2·16)/256`), conditional mean `21/13`.
Purity: the completed-chain convention `q′ = T_ij f_j / (2 f_i)`, the
state ordering and the first-return definition are all read from S1's
own artifacts and are gated by `V-S1-QP`/`G-KERNEL-CONFLICT-ROW`.  I
found no undeclared import.  The `400`-term cap is honest: the residual
tail is `ret − Σ` and is gated `< 1e-40`.

**K2 — the fiber collapse.**  `37` of `201` reproduced independently
from the R6a committed receipt: `7` homogeneous admissible records at
`9` sites × `3` links plus `2` inhomogeneous at the `2` printed sites
= `189 + 12 = 201`; count census `{1:29, 2:50, 3:20, 4:37, 5:27, 6:10,
9:9, 10:1, 12:9, 13:9}`; non-trivial `122`.  G-DIAG2 is the unique
record with every splittable interval at count `4`; its raw fiber
`19 683` rebuilds as `3^9` from the counts alone and equals the receipt
at `admissible_at_images`.  CR-B's `2 → 0` and the cross-unit
`TV = 2/21` (uniform vs binomial at count `4`) both reproduce.  All
value gates on these bind: `R3-EQUIV-DRIFT` dies at
`G-R6A-FIBER-REBUILD`, `R3-CRB-SIMPLEX-DRIFT` dies at `G-CRB-SIMPLEX`,
`R3-CENSUS-DROP` (silently dropping the whole count-3 cell) dies at
`G-ARENA-BASELINE` against an independently expressed
`7·9·3 + 2·2·3` expectation, `R3-TV-ZERO` dies at
`G-POSITION-DEPENDENCE-AT-TRANSPORT-SCOPE`.  Instrument verdict on the
scope question: **count-4-only is an artifact of S2's censused lengths,
and the instrument says so honestly** — `65` of `201` intervals are
labelled `UNCENSUSED-BY-S2 (count ≥ 5)` in the receipt's own class
table, and §12 declares the cap.  Nothing in the instrument reaches
count `5`.

**K3 — defective renewal and the seam.**  The termination arithmetic is
exact and reproduces (above).  The support hole at `2` costing `50` of
`201` reproduces.  The seam's *numbers* reproduce: transport
`(3/7,1/7,3/7)` and `(4/9,1/9,4/9)`, `TV = 2/63`; delivery-free uniform
at both censused positions, `TV = 0`; delivery-free mass `3/7` and
`1/3`.  The seam's *evidence*, however, rests on `G-SCOPE-SEAM`
(literal `True`) and on two verbatim anchors whose meaning A2 shows is
unbound.  The seam is measured where it is arithmetic and asserted
where it is textual.

**K4 — composed heads and re-classifications.**  All four heads are
mutually consistent and rebuild from the receipt alone (`7 of 7`
segments, exact).  The R6a re-classification figures reproduce: `54` of
`108` free transverse links, `30` of `81` non-integral cells, lift-pair
fiber `2`, `972`/`0` and `324`/`324` anchored as path-values with no
ratio formed against this unit's `647`/`67`.  Two soft spots:
`G-R6A-RECLASSIFICATION` tests a typed `lift_pair_fiber = 2` rather
than the anchored `P-R6A-LIFT-PAIR` it has in hand, and
`G-NEW-FRONTS-RECLASSED`'s integrality test is `isinstance(n1, int)`
over `range()` — a tautology, and the paper's "integral everywhere …
by construction" is at least candid about it.  The extremal
countermodel reproduces exactly: `MAX-DET → [2]`, `MAX-|q12| → [1,3]`,
`MAX-LEFT-COUNT → [3]`, `MAX-BALANCE → [2]`; `4` functionals, `3`
distinct selections; the derived law ratifies max-det at `1/3`;
`det`-blindness follows from the anchored readout string and I7's
`density_weight = 0`.

**K5 — instrument.**  Covered above and summarised below.

---

## Injection ledger (proven-executed only)

| injection | result |
|---|---|
| `31` declared mutants, two full sweeps | all die, each by its named gate/anchor, `0` tracebacks |
| **A2** meaning inverted around a preserved needle | **SURVIVES, exit `0`** |
| **A5** three paper quotations inverted | **SURVIVES, exit `0`** |
| **A6b** four false paper numbers (two census-table rows swapped) | **SURVIVES, exit `0`** |
| **R3-CONSUMER-UNBIND** every verbatim consumer → nonexistent gate | **SURVIVES, exit `0`** |
| **R3-ADDITIVITY-GARBAGE** garbage counts to the restriction re-verification | **SURVIVES** (gate `[PASS]`, exit `0`) |
| A1 needle broken inside the window | dies (`V-S1-SCOPE` then `A-S1-PAPER31`); consumer gates still `[PASS]` |
| A3 pin drifted | dies at `A-PIN`; `G-PIN-BOUND` still `[PASS]` |
| A6 `48 → 42` gate count in the paper | dies at `G-PAPER-CLAIMS` |
| R3-DEFECT-13-16 (`13/16 → 15/16`, consistent) | dies at `G-RENEWAL-DEFECTIVE` +6 |
| R3-HOLE-BOTH-ROUTES (`f(2) ≠ 0` in both routes) | dies at `G-FIRST-RETURN-LAW` +5 |
| R3-TV-ZERO (`2/63 → 0`) | dies at `G-POSITION-DEPENDENCE-AT-TRANSPORT-SCOPE` +4 |
| R3-CENSUS-DROP (count-3 cell removed) | dies at `G-ARENA-BASELINE` +3 |
| R3-EQUIV-DRIFT (fiber anchor) | dies at `G-R6A-FIBER-REBUILD` |
| R3-CRB-SIMPLEX-DRIFT (`2 → 1`) | dies at `G-CRB-SIMPLEX` +3 |
| R3-COVER-TYPED | dies at `G-COVER-DISSOLVED` (typed variable, see M7) |
| R3-VERBATIM-DROP (anchor removed) | dies only at `G-PAPER-NUMBER-SWEEP`, incidentally |
| R3-IDENT-RELABEL (class (iii) → (i)) | dies only at `G-PAPER-VERDICT` (M8) |
| R3-AS-TERMINATION-ONLY | not falsifiable without a `ZeroDivisionError` (M4) |
| post-write receipt corruption (the S1 class) | **undetectable by construction**; and detection-by-re-run is currently blocked by M1 |
| re-run at today's repository `HEAD` | **exit `2`**, `A-R6A` (M1) |

---

## What is right, recorded

* Zero false numbers in the receipt or the output; `61` exact
  recomputations, all agreeing, including two closed forms I re-derived
  analytically rather than by truncation.
* Two-run byte identity, and independent reproduction of the delivered
  `output.txt` byte-for-byte except for the three occurrences of the
  unrecoverable disclosure hash.
* `31/31` mutants die by their **named** target — the selftest's own
  standard is genuinely enforced (it prints `[DIED-OFF-TARGET]`
  otherwise), and it is a stronger check than the census that sits
  beside it.
* The verdict rebuilds exactly from the receipt alone; `7/7` segments
  verbatim in the paper and in the output.
* `G-VERDICT-EQUALITY` is a complete-string equality against a
  comparator rebuilt from measured values — no containment anywhere —
  and the three verdict mutants die on it.
* The path-value stability claim is **stronger than delivered**: `24`
  of `24` values unmoved against R6a's TERMINAL receipt
  `856f6e810ab5`, which the delivery could not have seen.
* The named exclusions are honoured: `0` excluded artifacts cited,
  verified independently against the anchor set; u1c appears only as a
  registered lead with its status printed.
* Declared caps are real and printed, not silent: the `65`
  uncensused-by-S2 intervals, the `7` uncensused sites of each
  inhomogeneous record, the un-rebuilt `G-CURVOFF` fiber, the `400`-term
  cap with an exact tail bound.

---

## Repairs, in priority order

1. Replace `git show HEAD:` with a commit-sha read declared in the
   frozen text; delete the working-tree read that feeds a must-pass
   gate; disclose only committed objects.  Re-run and re-freeze.
2. Compute the never-falsified census from measured deaths.  Expect
   `18` `UNWAIVED` rows; give each a real falsifier or demote it.
3. Demote the `6` literal-`True` gates to disclosures; recount the
   must-pass total.
4. Add a paper-quotation anchor set and positional binding for paper
   numbers.
5. Require consumer-gate bindings to name an existing, non-literal,
   mutant-falsified gate; state plainly that a verbatim window binds
   quote fidelity and nothing else.
6. Measure the four typed verdict counts (`variational_rows`, the two
   cover counts) from the six pinned rows; build the comparator from
   independent expressions for them.
7. Rebuild the additivity and restriction checks against independently
   expressed comparators; restate `647`/`67` as identities until then.
8. Give the identification inventory a gate that reads item classes.
9. Fix the `[:0]` no-op in NC2 and the unsatisfiable predicate in NC3.
10. Restate "two genuinely independent routes" as a transcription
    cross-check; add the missing #46 compliance row and correct
    "seven 2026-08-09 engravings" to eight.

---

## Confirmations

* Repo hashes re-verified **unchanged** after all work: paper
  `68c20d1fdae4`, code `8e188dd3ab70`, output `42a39fcaf194`, receipt
  `50f63b3ba362`, protocol `1cf5fc8b3272`, pin `17111fd19022`.
* Single repo write: `v14/review-r6bp-instrument.md`.  No git writes.
  No imports.  All mutant, injection and corruption work on copies
  under the scratch directory; the live worktrees (paper-11, `gprep_*`,
  `r3_*`, `crd_*`) and the other reviews were not touched.
