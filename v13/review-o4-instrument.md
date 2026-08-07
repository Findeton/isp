# O4 DISCRIMINATOR — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer lens:** THE INSTRUMENT — does the code measure what the paper
claims, and would the gates catch it if it did not.
**Protocol:** `v13/note-o4-hostile-protocol.md` (frozen, v13 #192); primary
weight on K5 and K4.
**Date:** 2026-08-07. **Lean:** none. **Git:** none used.
**Scratch:** all probes in the session scratchpad; no repository file was
modified other than this review.

---

## 0. Freeze verification

| object | declared sha256-12 | measured | verdict |
|---|---|---|---|
| `v13/paper-o4-discriminator.md` | `e45c090f226f` | `e45c090f226f` | ok |
| `v13/code/o4_discriminator_exact.py` | `240a6e05dce7` | `240a6e05dce7` | ok |
| `v13/code/o4_discriminator_output.txt` | `fd1cb9273951` | `fd1cb9273951` | ok |
| `v13/code/o4_discriminator_receipt.json` | `b791ec7e2d30` | `b791ec7e2d30` | ok |

All four match. Review proceeds against the frozen object.

**Reproduction.** The frozen source was copied byte-identical into an
isolated mirror (a scratch tree whose `v12` is a symlink to the repository's,
so `REPO/v12/...` imports resolve and all writes land in scratch) and run in
delivery mode, `--falsification-selftest`. Both artifacts came out
**byte-identical to the committed ones** (`diff` clean on
`o4_discriminator_output.txt` and on `o4_discriminator_receipt.json`),
from a different absolute path, in a different process tree. That is a
stronger determinism result than the paper's §12 claims, and it carries all
27 anchors, all 21 gates and all 23 mutants with it.

**Recomputations performed: 30.** Enumerated in §8.

---

## 1. K5(a) — the §14 fresh-eval self-test. **REAL, AND MEASURED AT FULL
## STRENGTH.**

The addendum's requirement is that the self-test evaluate fresh and that its
cache-hit count itself be gated. The instrument does this in the
`rq0_synth_census_exact.py` pattern verbatim: `_memo` bypasses `_MEMO` when
`_FRESH`, counting a miss; `O4-ST-FRESH` gates `hits == 0 and misses > 0`;
`memo-lax` removes the bypass and must die there.

A structural objection is available and I pressed it: in the honest path
`hits == 0` is *true by construction*, so the gate cannot fail except under
its own mutant. The question that decides whether the gate is load-bearing or
decorative is not whether it can fail but **whether the bypass is protecting
anything** — i.e. how many of the self-test's fresh lookups would have hit the
cache had the bypass not been there. I instrumented `_memo` in a scratch copy
to count exactly that.

> **Measured: 1320 of 1320.** `would_have_been_hits=1320`,
> `would_have_been_misses=0`, against the receipt's `value_cache_misses=1320`.

Every single value the symmetry self-test reads was already in the cache.
Without the bypass the self-test would have measured *nothing* — it would have
read one cached object back under every element of the group. The gate is
protecting the whole of the self-test, not a corner of it. This is the
strongest possible reading of the §14 addendum and the unit earns it.

I also checked for cache leakage the bypass does not reach. The self-test path
is `run_selftest → edge_transports → _chart_and_datum(_memo) →
TRANSPORT[fid] → W6.phi_set / W6.sp_conj / W6.leg_match`. `W6._ISO_CACHE` is
consulted **only** when `iso_maps` is called with a `cache_key`, and this
module never passes one; `transports_rec` builds its `isos` inline. `Composite`
and `W6.Chart` carry no memo — `Chart.__init__` recomputes occurrence,
availability and the law every time. `_SHARED` and `CHARTS` are never read on
the self-test path. **No hidden cache leaks into the fresh phase.**

`O4-ST-TEETH`'s arithmetic checks out: `instances_tested = 600 =
2 classes × 5 candidates × 6 settings × (2 + 8)`, and
`instances_where_the_action_is_nontrivial = 480 = 2 × 5 × 6 × (1 + 7)`. The
1320 lookups reconcile: `600 × 2 + 60 × 2`. The tested set is fixed by
declaration and is not selected by the verdicts under audit.
`O4-ST-INVARIANCE`'s reconciliation against the covariance gate's own counts
is a genuine second reader, and `covar-lax` dies on it.

---

## 2. K5(d) — D1. **DECIDED: 288 IS RIGHT. THE DIAGNOSIS IS CONFIRMED BY
## CONSTRUCTION. THE CLOSING SENTENCE IS NOT.**

This was the assignment's hardest item, and it decomposes into three separate
questions. I answered all three with an implementation that shares no code
with the unit: my own Born map, my own sparse-as-dense product, my own
4×4 → 36×36 lift.

**(i) Is 288 a false number?** No. On the committed
`v12/paper1_code/model_composite.py` preparation operator the residual
`D₂₁₀ = Γ(3←0) − Γ(3←2)Γ(2←0)` differs in **288 of 1296 entries** at SP-C,
SP-D and SP-F in both frames, spread over **18 columns × 16 entries**, and
`‖r‖₀ = (0,0,16,16,0,16)` on the j₀ column. The value censuses come out
`(4 distinct, 0 rational)` at SP-C and `(6, 8)` at SP-F. Every one of those
numbers reproduces the unit's, independently.

**(ii) Is the completion the cause?** Yes, and I constructed the completion
that gives W5's number. The committed `V` completes the singlet column with
the triplet **and two computational basis vectors** (`e₀`, `e₃`). A column of
`D` is nonzero exactly when the preparation puts that column into
superposition, so the two basis columns contribute 18 identically-zero
columns. Completing the *same* declared j₀ column by the **Bell basis** —
which is what "rebuilt from the singlet dictionary" most naturally produces —
gives `(0,0,576,576,0,576)`, exactly W5's A3, in both frames, at exactly
SP-C/SP-D/SP-F.

I then swept this systematically: **192 orthogonal completions of the same
committed j₀ column** (48 signed permutations of the complement basis, and
those composed with three π/4 rotations; all 192 verified orthogonal and all
carrying the singlet as column 0).

| SP-C matrix count | columns that differ | per-column | ‖r‖₀ | completions |
|---|---|---|---|---|
| **288** | 18 | 16 | 16 | 48 |
| 432 | 27 | 16 | 16 | 96 |
| **576** | 36 | 16 | 16 | 48 |

- The matrix count is **completion-dependent**, taking at least three values,
  and both 288 and 576 are realized. D1's diagnosis is confirmed.
- `‖r‖₀ = 16` and "every differing column differs in exactly 16 entries" are
  **completion-invariant across all 192**. A25 and A26 are therefore
  genuinely the surviving, completion-independent anchors, exactly as D1
  says. The SP-C `(4,0)` and SP-F `(6,8)` censuses are invariant too.

**Verdict on D1: a right 288, and a finding about W5.** I would state the
finding harder than the paper does. W5's own M1 anchors *only* the j₀ column
of `U_prep`; its A3/G4 matrix census is therefore **not determined by anything
W5 anchors** — it is a property of W5's private completion, not of "the
committed BC2 model". The o4 unit is entitled to say so.

**(iii) The closing sentence of D1 is refuted by measurement.** D1 ends: *"It
is also an independent confirmation, from a second direction, of the base's
finding that `U_prep`'s arbitrary completion off j₀ is doing work."* Two
measurements say otherwise.

- W6's own quantity — anchor A18, `w·U_prep·w` against `U_prep`, `(False,
  True, False, False, 9, 8)` — is **invariant across all 192 completions**. The
  base's finding does not move under the change that moves 288 to 576.
- W6's committed note says the opposite in terms: *"The obvious deflation is
  ruled out: this is not an artifact of `U_prep`'s arbitrary orthogonal
  completion, because the time-independent reachable restriction … still
  breaks the symmetry at every setting and at every level."*

The two facts are about different quantities. **Finding F5 (MEDIUM):** delete
or rewrite D1's last sentence; it attributes to the base a claim the base
explicitly disowns, and my sweep shows the base's measured quantity is
invariant under precisely the perturbation D1 invokes.

---

## 3. K4 — the arena, and D3's group shrinkage. **THE SHRINKAGE DOES NOT
## HOLLOW THE CLAIMS.**

Recomputed from scratch, importing nothing from the unit: charts rebuilt from
`Composite` + W6 primitives, supports computed directly from the propagators.

- `|base scope| = 72` (all 72 distinct), `|extension total| = 96` (all
  distinct), `|admitted| = 2`, `|admitted on the extension| = 8`. The admitted
  2 is exactly `{identity, pure wing exchange}`. A04–A07 confirmed.
- `|arena| = 6 × 2 × 2 × 8 = 192`. Confirmed.
- **D3 confirmed and sharpened.** The 96-element extension is not closed under
  conjugation (**1856 offending (g,h) pairs of 9216**) — and it is not even
  closed under composition (**3072 failures of 9216**). The base 72 *is* a
  group (0 failures of 5184 on both tests). The admitted 2 and the admitted 8
  are both groups. D3's statement is true and understated: the 96-set is not a
  group at all, so drawing an action from it would test a candidate's declared
  search scope, exactly as D3 says.
- **QA1**: 4 distinct truth-value vectors over the arena; moves under setting,
  frame, relabelling; **not** under switching; **orbit 2 at all twelve
  charts**. **QA2**: 2 distinct values; moves under setting only; **orbit 1 at
  all twelve charts**. Both reproduced exactly.

So the shrinkage does not hollow the orbit claims: the surviving nontrivial
element is the **wing exchange**, which is the very identification the base is
about, and it is contained in every candidate's declared search scope. The
per-coordinate discipline of §15 is respected in the claims.

**But the §8 comparison is not like-for-like at the relabelling coordinate.**
QA1 is a **name-indexed** 36-bit vector; QA2 is a **name-quotiented** set of
value tuples. A relabelling permutes the index set of the first and cannot
touch the second. I built the exactly parallel name-indexed *record-side*
quantity — the occupied support at the **final** time, the time F-REC's datum
is read — and swept it through the same 192-point arena:

| quantity | moves under | orbit per chart |
|---|---|---|
| occupied support at t=2 (= QA1) | setting, **frame**, relabelling | 2 (all 12) |
| occupied support at t=3 (record-side, name-indexed) | setting, relabelling | 1 or 2 |

The record-side name-indexed quantity **also moves under the relabelling** and
**does not move under the frame**. The discriminating coordinate is therefore
the **frame alone**; the relabelling coordinate separates *quantity types*, not
fact classes — and it is the same sensitivity the unit's own negative control
F-CTRL is *defined* by.

**Finding F6 (MEDIUM).** `O4-ARENA-RELATIVE` survives intact — it requires only
that F-CFG's truth-values move where F-REC's do not, and the frame coordinate
supplies that decisively (the frames' t=2 supports are disjoint; their t=3
supports are **equal at every setting**, `|∩|` full). But §8's "move under both"
and §10's "with the frame and with the admitted relabelling — while record
truth-values do not" overstate. Repair: restrict the discriminating claim to
the frame coordinate and disclose that any name-indexed quantity, record-side
included, moves under the relabelling.

---

## 4. K5(b) — the 23 mutants. **ALL DIE WITH NAMED KILLS; TWO REAL DEFECTS.**

All 23 reproduced in my run with kill lists identical to the receipt, all
`exit 1`, none crashing before reporting, `not_falsified_by_any_mutant = []`
at denominator 17.

**D6's census exception is legitimate.** `run_mutant_table()` is called before
`run_verdict()`, so `O4-VOCABULARY` does not exist when the census is taken;
the denominator is 17 and the set is empty at that denominator. The eighteenth
gate is covered — `verdict-lax` falsifies `O4-VOCABULARY` and the kill is in
the mutant table. Disclosing rather than reordering is right: reordering would
move the receipt. **No objection.**

**Two mutants reconstructed from the receipt's prose, independently** (no
import of the unit; transport rule, identity-leg normalisation and level
census rebuilt from the paper's own descriptions):

| reconstruction | measured | receipt |
|---|---|---|
| NOSLICE: C1 NAIVE-SLICE identified at | **0 of 12** charts | fails at all 12 |
| NOSLICE: C2 / C3 identified at | **12 of 12** each | pass |
| `global-now-smuggler` (C2 with identity legs kept) | **0 of 12** → corridor inside emptied | dies at `O4-CORRIDOR-CENSUS` |
| level census, F-REC switching failures: exact / sign / born | **24 / 0 / 0** | `24 / 0 / 0` |

Both kills reproduce exactly. I also verified `support-lax`'s premise
independently: at the **final** time the two frames' occupied supports are
**equal at every one of the six settings**, so reading the datum there really
does turn every intersection from 0 to full and `O4-OBSTRUCTION-NAMED` really
must die. Three reconstructions, three confirmations.

### F2 (MEDIUM) — the LTP gate has no falsification coverage.

`ltp-lax` is advertised in §12 as "a stubbed LTP gate". It does two unrelated
things: it zeroes the residual vector in `ltp_residuals` **and** it stubs
`bare = []` in `ltp_gate`. Its entire kill (`A25`, `A27`) comes from the
first. I built the pure stub — `bare = []` in `ltp_gate` only, residual and
anchors untouched — and ran the whole suite:

> **`exit 0`. `KILL-JSON {"failed_anchors": [], "failed_gates": []}`.
> 27 anchors, 20 gates, 0 must-pass failures.**

A stubbed LTP gate passes the suite silently. The corrupted value reaches the
paper: the aggregate flips from `LTP-BARE` to `LTP-BARE-UNWITNESSED`, which is
what §9.1 prints as C4's "LTP gate **LTP-BARE**". The LTP clause is a
*mandatory* gate of the pin, and nothing in the suite can falsify it. Repair:
a mutant that perturbs the LTP selector alone (e.g. inverting the
`forced_bare` / `shared` precedence, or forcing `LTP-LAWFUL`), plus a gate
that reconciles the aggregate against the per-setting strings.

### K3-adjacent, in this lens: LTP-LAWFUL **is** genuinely reachable.

The paper asserts reachability but exhibits no witness, and no mutant proves
it. I supplied one. Driving `ltp_gate` with the real residuals and a forced
shared record partition:

- with `shared > 0`: **SP-E emits `LTP-LAWFUL`** (the residual vanishes there,
  so the forcing branch does not fire);
- with `shared > 0` and the residual zeroed: the aggregate is **`LTP-LAWFUL`**.

The verdict is emittable, so "measured never to obtain" is a measured
negative, as the paper says. **F9 (LOW):** the selector tests `forced_bare`
*before* `shared > 0`, so a coordinate carrying both a nonzero residual and a
shared record law would be reported `LTP-BARE` and could never be
`LTP-LAWFUL`. Moot on this base (`shared = 0` at all six settings, A14) but
undeclared; it should be stated as a scope clause.

### F3 (MEDIUM) — §12's claim about the mutants' construction is false.

§12: *"each perturbing a **computation** — none overwrites a computed field
after the fact"*. Seven of the twenty-three do exactly that:

| mutant | what it overwrites, after computation |
|---|---|
| `covar-lax` | `ok, moved_relabel, moved_switch = True, 0, 0` |
| `cert-lax` | `ok = {sp: True …}` |
| `ctrl-pass` | `neg_fails = {cid: [] …}` |
| `ltp-lax` | `bare = []` |
| `canon-lax` | `moved = []` |
| `verdict-lax` | `v = "O4-UNDECIDED-…"`, `unit = "O4-UNDECIDED"` |
| `float-lax` | `lits.append(-1)` |

Six of the seven still falsify their gate (and `covar-lax` is caught by the
self-test's independent reconciliation, which is good design). The seventh —
`ltp-lax`'s waiver half — is inert, which is F2. The defect is the **claim**,
not most of the mutants: a waiver proves the gate's predicate is load-bearing
for the exit code, not that the gate would catch a computational defect, and
§12 asserts the stronger property for all 23. Repair: state the split
honestly (16 computation-perturbing, 7 waivers) or convert the waivers.

### F4 (MEDIUM) — three gate texts name mutants their own table shows do not
### kill them.

| gate text says | mutant table says |
|---|---|
| `O4-ARENA-TEETH`: "the `action-weaken` mutant collapses the action and must die here" | `action-weaken` kills `A05, A17, O4-ARENA-FAMILY, O4-LEVEL-CENSUS, O4-ST-TEETH` — **not** `O4-ARENA-TEETH`. It cannot: the *setting* coordinate still moves, so `moved_under` stays non-empty and the gate passes. `O4-ARENA-TEETH` is killed by `canon-lax`. |
| `O4-ST-TEETH`: "the `action-weaken` and `gauge-subsample` mutants shrink it and must die here" | `gauge-subsample` kills `O4-ARENA-FAMILY, O4-LEVEL-CENSUS` — **not** `O4-ST-TEETH`. It cannot: the gate's expected count is `… × (|group| + |switchings|)`, which shrinks in step with the sweep, so the equality still holds. |
| `O4-LEVEL-CENSUS`: "the sign/orientation mutants must die here" | `sign-flip` does; `orient-flip` kills `A17` only. |

Every gate is still covered by *some* mutant, so `never falsified []` stands.
But the receipt's own prose is falsified by the receipt's own table, and one
of the two (the `gauge-subsample` case) exposes a gate whose predicate is
constructed so that the named perturbation cannot move it. Repair: correct the
three texts to name the mutants that actually kill, and — for `O4-ST-TEETH` —
gate the sweep size against the **declared** arena rather than against a
formula that shrinks with it.

---

## 5. F1 (MEDIUM-HIGH) — the realized restriction is missing from
## `triple_descent`: two published cells are wrong.

`edge_transports` and `pair_transports` both apply
`if cand.get("realized"): ca, cb = realized_of(ca), realized_of(cb)`.
`triple_descent` calls `TRANSPORT[fid](charts[a], data[a], …)` **directly and
does not**. C4 REALIZED-ONLY is the only candidate carrying `realized: True`,
and its remaining parameters (`born`, order-free, drop-identity, base perms)
are **identical to C2's**. So C4's TRI and GLUE rows are literally C2's rows —
the receipt shows the two triples byte-for-byte identical (`SET-AMALGAM`,
families 1, orbits 1, all six edge counts 1), while C4's own F-REC transport
count at SP-A is **0**.

I applied the one-line repair in a scratch copy and remeasured:

| C4 / F-REC triple | published | with the realized restriction applied |
|---|---|---|
| verdict | `SET-AMALGAM` | `ABSENT-PAIR` |
| edge counts | all 1 | `F1←F2: 0, F1←F2π: 0, F2←F1: 0, …` |
| **TRI** | **PASS** | **fail** |
| **GLUE** | **PASS** | **fail** |

**Two cells of §5's gate table are false as published** (row "C4
REALIZED-ONLY / F-REC", columns TRI and GLUE), and the receipt carries the
same two cells at `tables.gate_table.C4.F-REC`. It is also a like-for-like
violation of exactly the kind K2 exists to catch — one candidate's gates
computed under another candidate's rule — and **no gate catches it**:
`O4-LIKE-FOR-LIKE` tests that the three *classes* carry the same gate keys and
that the three transport functions share a signature, never that a
candidate's ten gates are all computed with that candidate's rule.

**Impact on the verdicts: none.** `passes(row, sp)` requires
`counts[sp] == 1` first, and C4's counts at SP-A are 0 for every class, so
`per["SP-A"]` is `O4-BLOCKED-AT-<no certified transport for either class>`
either way; the corridor reads only COVAR/NAMEBLIND/NOSLICE; `O4-CTRL-POS` and
`O4-TRIPLE-EXERCISED` both read C2. C4's published verdict, the per-candidate
table and the unit verdict are unchanged. §5's reading 3 ("the record class
under the realized restriction is ABSENT at the four asymmetric settings and
FORCED at the two…") is about the *counts*, which are computed correctly.

`certify()` likewise does not apply the realized restriction, but that is
**declared** in D4 ("its value depends on the fact-class and the setting but
not on the candidate"), so it is disclosed rather than defective.

Repair: two lines in `triple_descent`, and reprint the two cells. Under
FREEZE-ON-DELIVERY this is an errata item for the adjudication, not a silent
edit.

---

## 6. K5(c) — the 27 anchors. **ALL TRACED. EXIT-1-ONLY CONFIRMED BY
## DELIBERATE BREAKAGE. ONE ANCHOR IS VACUOUS.**

Every anchor was located in a committed source; 25 of 27 match **verbatim**:

| anchors | source, located |
|---|---|
| A01–A03 | `v12/code/w6_output.txt:106–108` — `8`, `9`, `True`, with the `sec4_records.py:516/524/505` cites carried across |
| A04–A07 | `v12/note-w6-record-coreference.md` SCOPE clause: "**72**-element permutation scope", "admits **exactly two**", "a **96**-element scope of which **8** survive" |
| A08–A10 | same note W6-A: "**56** of 144", "**0** violations", "**32** … accidental agreements" (so 24 same-experiment), "class sizes {2,4,6}" |
| A11–A12 | W6-B; `w6_output.txt:116,126` — `[2]` / `[1,1,1,1,1,1]` |
| A13–A14 | M4; `w6_output.txt:145` — `([1]×6, [0]×6)`; "0 shared partitions at t=2" |
| A15 | `w6_output.txt:113` — `[270, 270, 432, 432, 108, 432]` verbatim |
| A16 | `w6_output.txt:135` — `[(False,2,8),(False,2,8),(False,8,8),(False,8,8),(False,2,2),(False,8,8)]` verbatim |
| A17 | `w6_output.txt:137` — the exact/sign/Born token-map table verbatim |
| A18 | `w6_output.txt:139` — `(False, True, False, False, 9, 8)` verbatim |
| A19 | note: "the other **35** columns" — but see below |
| A20–A24 | `v12/paper2_code/RUN.txt` §3–§5, line by line: the five verdicts, `(4,1,2,True)`, `0`, `(4,4,1,1,(0,1),(1,0))`, `P = (0,2,1,4,3)` |
| A25–A27 | `v12/note-w5-barandes-recast.md` §3.3: `‖r‖₀ = 16/16` at SP-C/D/F both frames; G5 `(4, 0 of 16)`; G5b `(6, 8 of 16)` |

**Exit-1-only, tested by deliberate breakage.** I perturbed the *committed*
constant of A08 — an anchor no mutant touches — in a scratch copy:

> `KILL-JSON {"failed_anchors": ["A08"], "failed_gates": []}`, **exit 1**.

`build_receipt` adds every failing anchor to `must_pass_failures` and `main`
returns 1 on any failure, so this is structural for all 27, not just the 8
that mutants happen to reach (`A04, A05, A07, A17, A18, A25, A26, A27`).

**F7 (LOW) — A19 is vacuous.** `anchor("A19", …, "the never-occupied block of
U_prep has 35 columns", 35, NC - 1)`. The computed side is `NC - 1`. It asserts
`36 − 1 = 35` and never reads `U_prep`, never reads occupancy, and can only
fail if the carrier size changes. It is the one anchor of the 27 that measures
nothing about the quantity it names. (A04 is weakly of this kind too —
`len(base)` is `2·3·3·2·2` by loop construction, and distinctness of the 72 is
not checked; I verified independently that all 72 *are* distinct, so the count
is sound.)

**A26 is a re-scoping, and the paper says so.** W5's G4 asserts `16 × 36 =
576` — thirty-six columns. A26 asserts only "every column that differs at all
differs in exactly 16 entries", which is what survives; the weakening is
declared in D1 and in `O4-COMPLETION-DISCLOSURE`. My 192-completion sweep
confirms the weakened form is invariant and the strong form is not. Correct
handling.

**F13 (COSMETIC).** A15–A18's committed values are cited to the W6 *note* but
appear verbatim only in `v12/code/w6_output.txt` (lines 113/135/137/139). Cite
the receipt line as well as the note.

---

## 7. Exhaustiveness and [SAMP]

| sweep | claimed | measured |
|---|---|---|
| the arena (§2, §8) | 192 points | exhaustive; I enumerated all 192 independently |
| checkpoint-phase switchings | `2³ = 8`, one sign per leg | exhaustive; leg count read off the fixture |
| admitted isomorphisms | 2 (of 72), 8 (of 96) | exhaustive; enumerated and verified as groups |
| level census | 3 levels × (2 relabellings + 8 switchings) × 6 settings | exhaustive; reproduced |
| AST float sweep | whole module | exhaustive; `float_literal_lines = []`, `float_call_lines = []`, `rows_carrying_a_float = []` |
| **NAMEBLIND** | "a pure configuration relabelling" | **one** element, `build_perm(0,0,0,1,1)` |
| **the descent triple** | "F2 on a relabelled configuration set" | the **same** single element |
| EXIST/FORCED "on every declared edge" | — | the six same-setting `F1←F2` edges only, not the 144 ordered pairs |

The two single-element choices are the only [SAMP] exposures, and I closed
them by brute force. Sweeping the **whole** declared scope:

| candidate / class | NAMEBLIND passes at |
|---|---|
| C2 F-REC, C2 F-CFG | **72 of 72** |
| C3 F-REC, C3 F-CFG | **96 of 96** |
| C2 F-CTRL | 1 of 72 (the identity only) |
| C3 F-CTRL | 1 of 96 (the identity only) |

The single-element choice is **not load-bearing**: the corridor verdict is
uniform over the entire declared scope, and the negative control fails
everywhere except at the trivial element. **F10 (LOW):** the robustness is my
measurement, not the unit's — the receipt should carry the sweep, or the gate
should be labelled `[SAMP: one declared relabelling]`.

**F11 (LOW).** `INV` has no mutant coverage and is not read by any verdict;
`EXIST`/`FORCED` are covered only indirectly through `O4-CTRL-POS`
(`rec-uncut`). More importantly, the falsification census covers the **21
`O4-*` receipt gates**, never the **ten descent gates** of §3.2. §12's "18 are
must-pass" and §3.2's "ten gates" are different objects and a reader will
conflate them; say so.

---

## 8. What I recomputed (30)

1. sha256 of all four frozen objects · 2. delivery-mode rerun →
`output.txt` byte-identical · 3. same run → `receipt.json` byte-identical ·
4. all 27 anchors re-evaluated by that run · 5. all 23 mutants re-run, kill
lists identical · 6. residual census under the committed completion (own Born,
own product) · 7. Bell-basis completion → 576 · 8. third completion → 576 ·
9. 192-completion systematic sweep → {288:48, 432:96, 576:48} · 10. A18 split
across all 192 → invariant · 11. SP-C/SP-F value censuses across completions ·
12. fresh-eval probe → 1320/1320 would-be cache hits · 13. pure LTP-gate stub
→ exit 0 · 14. LTP-LAWFUL reachability witness (three cases) · 15. scope
enumeration 72/96/2/8 + admitted = {id, wing swap} · 16. D3 closure tests
(conjugation 1856/9216, composition 3072/9216, base 0/5184) · 17. arena size
192 · 18. §6 occupied-set table, all six rows, intersections and unions ·
19. QA1 dependence, orbit and distinct-value count · 20. QA2 dependence, orbit
and distinct-value count · 21. name-indexed record-side quantity at t=3,
swept through the arena · 22. final-time supports equal in both frames at all
six settings · 23. NOSLICE reconstruction (C1 0/12, C2 12/12, C3 12/12,
smuggler 0/12) · 24. level-census reconstruction (24/0/0) · 25.
`triple_descent` repair probe → C4/F-REC TRI, GLUE actually fail · 26.
deliberate A08 break → exit 1 naming A08 · 27. NAMEBLIND swept over all 72 and
all 96 relabellings · 28. §5 gate table and transport counts cross-checked
cell by cell against the receipt · 29. gate/anchor/mutant counts and the class
census against §12 · 30. anchor source trace against `w6_output.txt`, the W6
note, `RUN.txt` and the W5 note.

---

## 9. Findings, ranked

| # | sev | finding | repair |
|---|---|---|---|
| **F1** | MED-HIGH | `triple_descent` does not apply C4's realized restriction; C4/F-REC **TRI and GLUE are published PASS and are actually fail**; C4's triple is C2's triple. No gate catches it. Verdicts unaffected. | two lines in `triple_descent`; reprint two cells; extend `O4-LIKE-FOR-LIKE` to check candidate-rule consistency across gates |
| **F2** | MED | The **LTP gate has no falsification coverage**. A pure `bare = []` stub runs the whole suite green (exit 0). `ltp-lax`'s kill comes entirely from its residual half. | a mutant perturbing the LTP selector alone; a gate reconciling the aggregate against the per-setting strings |
| **F3** | MED | §12's "each perturbing a computation — none overwrites a computed field after the fact" is **false for 7 of 23** (`covar-lax`, `cert-lax`, `ctrl-pass`, `ltp-lax`, `canon-lax`, `verdict-lax`, `float-lax`). | state the 16/7 split, or convert the waivers |
| **F4** | MED | Three gate texts name mutants their own table shows do not kill them: `O4-ARENA-TEETH`←`action-weaken`, `O4-ST-TEETH`←`gauge-subsample`, `O4-LEVEL-CENSUS`←`orient-flip`. `O4-ST-TEETH`'s predicate shrinks in step with the sweep it gates. | correct the texts; gate the sweep size against the declared arena, not a co-shrinking formula |
| **F5** | MED | D1's closing sentence claims the divergence confirms "the base's finding that `U_prep`'s completion is doing work". Measured: A18 is **invariant across 192 completions**, and W6's note says "this is **not** an artifact of `U_prep`'s arbitrary orthogonal completion". | delete or rewrite the sentence; keep the (correct) diagnosis and the (stronger) point that W5's A3 is not determined by anything W5 anchors |
| **F6** | MED | §8/§10's **relabelling** clause is not like-for-like: QA1 is name-indexed, QA2 name-quotiented; the parallel name-indexed record quantity also moves under relabelling. The **frame** coordinate carries the result alone. | restrict the discriminating claim to the frame; disclose the measurement |
| **F7** | LOW | **A19 is vacuous**: committed `35` against computed `NC - 1`. Measures arithmetic, not `U_prep`. | compute the never-occupied block from occupancy |
| **F8** | LOW | Receipt field `coordinates_forced_bare` contains SP-E, which the same gate's own per-setting string declares **not** forced (`LTP-BARE-UNWITNESSED`). Field name falsified by its content; §7's table is right. | rename, or split forced / unwitnessed |
| **F9** | LOW | LTP precedence (`forced_bare` before `shared > 0`) is undeclared; a coordinate with both could never read `LTP-LAWFUL`. Moot here (`shared = 0` ×6). | state as a scope clause |
| **F10** | LOW | NAMEBLIND and the descent triple are decided at **one** relabelling. I swept all 72/96 and the verdict is uniform — but the unit does not measure that. | carry the sweep, or tag `[SAMP]` |
| **F11** | LOW | `INV` unmutated; the falsification census covers the 21 `O4-*` gates, never the ten descent gates of §3.2. | disambiguate "gates" in §12; add an INV mutant |
| **F12** | LOW | "two delivery-mode runs are byte-identical, **verified**" carries no gate. (True — I verified it across directories.) | add a determinism gate, or attribute the verification |
| **F13** | COSM | A15–A18 cited to the W6 note; verbatim only in `w6_output.txt:113/135/137/139`. | cite both |

### What survived, and should be recorded as having survived

- **Byte-identical reproduction** of both artifacts from an independent path.
- **27/27 anchors trace**, 25 verbatim; **exit-1-only proven by deliberate
  breakage**.
- **23/23 mutants die with named kills**; `never falsified []`; **D6's census
  exception is legitimate**.
- **The §14 fresh-eval gate is load-bearing at full strength** — 1320 of 1320
  self-test lookups would otherwise have been cache hits; no hidden W6 or
  model cache leaks into the fresh phase.
- **D1's 288 is a right number**, its diagnosis is confirmed by explicit
  construction of a completion yielding 576, and A25/A26/A27 are verified
  completion-invariant over 192 completions.
- **LTP-LAWFUL is genuinely reachable** (witness exhibited).
- **The arena, the orbits (QA1 = 2, QA2 = 1 at all twelve charts), the
  192-point family and D3's shrinkage** all reproduce from scratch; the
  shrinkage does **not** hollow the claims.
- **§6's obstruction table reproduces exactly**, and `support-lax`'s premise
  (equal supports at the final time) is real.
- **§5's 15×9 gate table and 15 transport-count rows match the receipt cell
  for cell**, F1's two cells excepted.
- No false *physics* number was found. The unit verdict
  `O4-DISCRIMINATED-RECORD-ACTUALISM + O4-ARENA-RELATIVE` is unaffected by
  every finding above.

---

## 10. Grade

Two cells of a published gate table are wrong because one candidate's gates
are computed under another candidate's rule, and no gate catches it (F1). A
gate the pin declares **mandatory** — the LTP clause — has no falsification
coverage at all, and the mutant advertised as covering it does not (F2). The
paper makes a false claim about how its own falsification suite is built (F3),
three gate texts are falsified by their own mutant table (F4), one deviation's
interpretive claim is contradicted by measurement and by its own source (F5),
and one of the two coordinates carrying `O4-ARENA-RELATIVE` is not earned as a
class discriminator (F6).

None of these is a false number in the findings, and none moves a verdict. The
instrument's hardest parts — the fresh-eval self-test, the anchor battery, the
obstruction, the arena census and the D1 diagnosis — hold under independent
recomputation, and D1 in particular comes out *stronger* than the paper claims
once the 192-completion sweep is in hand. But six substantive repairs are
required before this is terminal, two of them to published values or to a
mandatory gate.

> # **ACCEPT-WITH-FIXES**

Required before terminal status: **F1, F2, F3, F4, F5, F6**.
Recommended: F7, F8, F9, F10, F11, F12.

**Recomputation count: 30.**
