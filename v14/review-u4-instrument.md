# U4 / paper-14 — INSTRUMENT-LENS HOSTILE REVIEW (K5, full era)

**Reviewer:** instrument lens, 1 of 3.  **Protocol:**
`v14/note-u4-hostile-protocol.md` (`c4f2b33aa315`, #114), K5.
**Object, hashes verified before any work and unchanged after:**
paper `7e6db49f0e6e`, code `c1ae8ec7fdbe`, output `d1bfbbca40c9`,
receipt `ae7a4ce48538`, pin `06b62ecb60a9`, protocol `c4f2b33aa315`.

**GRADE: AWF (accept with fixes).**

**Executions:** 49 program runs (1 plain off-tree, 16 hostile argv,
1 `--selftest`, 12 mutants, 1 outside-the-repo, 18 injections).
**Independent recomputations:** 350 (267 paper↔output↔receipt cells,
40 stabilizer quantities by a third route, 1 head by a fourth route,
42 anchor→v10-source-line traces).  **False computed numbers found: 0.**

**Injections:** 17 attacks — **8 caught, 9 survived**; 6 of the 9
survivors are the gate-to-disk seam class.

---

## 0. What holds (FOUND, at my own hands)

- **#91, both legs.**  *Off-tree:* a copy whose derived repo root
  contains no `v10/v11/v14` fails at all 17 `G-PROV[...]` gates and at
  `G-PROV-ROOT`, exit 1, **nothing written** — loud and by design, as
  claimed.  *Git-less:* a mirror at
  `…/scratchpad/u4-in/mirror/` (no `.git` anywhere on the path,
  sources reached by symlink, the program never invokes git)
  reproduced **both artifacts BYTE-IDENTICAL** — `d1bfbbca40c9` /
  `ae7a4ce48538`, `cmp` clean.
- **#82 contract.**  16/16 hostile argv forms (`--help`, `-h`,
  flag pairs, `--mutant` with no name / empty / lowercase / extra
  token / doubled, `--selftest=1`, `--`, a path, an invented `--out`)
  exit **2** with the artifacts sha-unchanged.  Unknown mutant name
  exits 2 **and prints the whole registry**.  Registry complete in
  both directions: 12 registered, 12 hooked, **no orphan hook and no
  unhooked name**.
- **12/12 mutants** die at named gates with artifacts sha-unchanged
  (re-verified by sha256 after the batch, not by the program's own
  print).
- **The MUT-NOT-FORCED fix is confirmed independently.**  It dies at
  exactly `G-FORCED[DOUBLE-GRID(3,2)]` **and carries 10 anchor
  failures with it** — non-silent, as the ledger claims — and the
  "all 12 re-run" claim reproduces at my hands.
- **`--selftest`** exits 0, artifacts sha-unchanged, **no stray or
  `.tmp` file left behind**.  I did not take the program's word: I
  corrupted a *different* committed number myself (A05, the control's
  d=2 mean overlap, 101/258 → 101/259) and the run refused at SEC 4
  with nothing written.
- **42/42 anchors reproduce**, and **41 of the 42 appear verbatim at
  the v10 output line they cite** (A34 is the event-count law's own
  fit; its 72 is A28's `d66 out L64` value, so it is anchored too).
- **The ten stabilizer cells survive a third route.**  I enumerated
  the six subgroups of Z₃² from the closure axiom and took the largest
  subgroup on whose cosets the field is constant — sharing no code,
  no constant and no import with either delivered route.  All ten
  names, all ten orders, all ten element sets and all ten supports
  reproduce.  The head reproduces under a **fourth** route built from
  the receipt table plus the pin's outcome name.
- **267 three-way checks, 0 mismatches** — every cell of §2, §3, §5,
  §6.1, §6.2, §6.3, §6.4, §6.5 and §7 traced paper↔output↔receipt,
  including all 40 exact rationals of §6.3 and all 45 bridge cells.
- **The purity ⇒ empty-control implication is real** and
  machine-checkable from the receipt at 5/5 crystals.
- **All 14 verbatim consumers exist as gates.**

---

## 1. MAJOR findings

### MAJOR-1 — The L-1 wall is defeated by the paper's own line wrapping

`G-WALL-L1` (L1793–1799) enforces the pin's engraved ban by
`if BANNED in fh.read()` — a **contiguous** substring scan — over the
program source and over `paper-14`.  The banned sentence is 96
characters; `paper-14` hard-wraps at ~72.

**Measured, both directions:**

| injection | banned sentence in paper-14 | result |
|---|---|---|
| I17 | present, wrapped in the paper's own house style | **147/147 PASS, exit 0, artifacts written** |
| I18 | present, contiguous on one line | `G-WALL-L1` **FAILS**, exit 1, nothing written |

The wall therefore fires only against a form the paper's own house
style never produces.  Three aggravations, all measured:

1. The `BANNED` literal (L1008–1009) is a **typed string with no #62
   anchor of its own**, and it occurs contiguously **nowhere in the
   corpus** — the retracted sentence lives *wrapped* inside the pinned
   paper 0's own erratum (`…v11-paper0…md` L294–296).  A
   mis-transcription would make the gate pass vacuously and nothing
   would notice.
2. It does **not cover the corpus's canonical short fragment**
   `"precisely the form U4 tests"` — the exact string v11's own
   `L1_L0_text_anchors.py` registers as anchor L1-A16.  That fragment
   in the paper would pass unchallenged.
3. Paper §8 states "the program gates its absence from both this paper
   and its own source."  True as written, but the reach is one
   formatting convention wide.

**Repair (liftable).**  Normalise before scanning —
`norm = lambda s: re.sub(r"\s+", " ", s)` applied to **both** needle
and haystack; add `"precisely the form U4 tests"` as a second banned
needle; and bind the needle itself with a `vanchor` against the pinned
paper 0 erratum under the same normalisation.  (I checked the source
does not then self-trigger: the literal's own `" "` split survives
whitespace normalisation as `" " "`.)

### MAJOR-2 — No mutant reaches the geometry segment's VARIES path, and the paper says one does

Pin R4.2 requires `VARIES-<witness>` to be **emittable** and "a mutant
demonstrates the VARIES path"; the OUTCOMES section makes the GEOMETRY
segment a two-valued pre-registration.  Paper §13's final bullet
claims "**one that drives the geometry segment onto the VARIES path**
so that the pin's falsifier is demonstrably emittable."

**Measured, with a probe on a scratch copy under `--mutant
MUT-GEOM-VARIES`:**

```
[GEOMETRY PROBE] widths_ok=True varies_witness=['DOUBLE-GRID(3,2)|d=2|max|D|:9->3',
  'DOUBLE-GRID(3,2)|d=3|max|D|:9->3', 'D60-GRID(3,12)|d=2|max|D|:3->1',
  'D60-GRID(3,12)|d=3|max|D|:3->2']
[GEOMETRY SEGMENT VERDICT] GEOMETRY-INVARIANT-AT-THE-CONTROLLED-ROW-REST-BLOCKED-…
```

The segment verdict stays **INVARIANT** under the mutant that is meant
to flip it.  **Mechanism:** `widths_ok` (L1653–1657) is a *second,
fresh* recomputation — `profile(poset_of(built[nm].H), <the full
division index list>)` — which bypasses the mutated population `pop`
entirely, and it quantifies only over `ARB` while `varies_witness` is
appended for **all five** crystals (L1510–1512).  Consequences:

- (a) Paper §13's bullet is **false as measured**.  §11.5's weaker
  wording ("the string is emitted before the gate kills the run") is
  the true one — the per-crystal gate does emit `VARIES-9->3`.
- (b) In the **plain** run `G-GEOM-SEGMENT` already ships
  `varies_witness = ['D60-GRID(3,12)|d=2|max|D|:3->1',
  'D60-GRID(3,12)|d=3|max|D|:3->2']` beside
  `verdict: GEOMETRY-INVARIANT-…` and `width_row_invariant: true`.
  Two fields of one gate's evidence assert opposite things and **no
  gate binds them**.  The field is not a falsifier witness at all.
- (c) Pin R4.2's demonstration obligation is **not discharged at the
  segment level**.

**Repair (liftable).**  Delete the duplicate recomputation.  Collect
`varies_witness_arb` inside the per-crystal loop (ARB only), set
`widths_ok = not varies_witness_arb`, keep the control's entries in a
separately named `control_varies` field, and add a gate binding
`widths_ok ⟺ varies_witness_arb == []`.  MUT-GEOM-VARIES then does
what the registry and §13 claim.

### MAJOR-3 — The gate-to-disk seam recurs (narrower than R4b, but real)

This unit predates the #119 engraving and it has the disease.
`write_and_verify` (L2103–2131) tests
`b1 == out.encode()`, `rec["output_sha256"] == sha256(b1)`,
`rec["head"] == PAYLOAD["head"]`, `rec["counts"]["gates_failed"] == 0`
— i.e. **disk versus live memory**, and live memory is mutable after
its gate has fired.

**Survived to disk with 147/147 and `gates_failed: 0`:**

| injection | what shipped |
|---|---|
| I03 | a `[DATA]` line in the **output** reading `field=[2,2,2,2,2,2,2,2,2] support=9/9` for CONFLICT-GRID(3,2) initiator (truth: `[2,0,0,0,2,0,0,0,2]`, 3/9) |
| I04 | a **receipt gate row** `G-STAB[CONFLICT-GRID(3,2)\|footprint]` reading stabilizer `<(1,1)>`, order 3, beside a constant field `[2,…,2]` and a `stabilizer_table` cell still reading `Z3^2` — internally contradictory, undetected |
| I05 | `payload.arena[0]` events/divisions = 99 |
| I06 | the **control's row shipped under the CONFLICT-GRID(3,2) label** (field `[1,0,…]`, support 1, stabilizer `1`, kind `CONTROL`) |
| I14 | the published `stabilizer_table` cell flipped away from its own gate's evidence |
| I11 | *(instrument-level control)* a **demonstrably false `G-BRIDGE-DIAG[DOUBLE-GRID(3,2)]` row published as PASSED** — `diag_11: [1,0,…]` under a statement asserting "identically ZERO at 9 of 9 sites" — with counts 147/147 |

**What *is* sealed, and why it is narrower than R4b.**  Four objects
are bound to a *third artifact on disk*: the head and the geometry
verdict are checked into `paper-14` verbatim by
`G-VERIFY-PAPER-CLAIMS`, and the stabilizer-table cells are bound by
`G-READING-DIVERGENCE` and by `G-HEAD-EQUALITY`.  Measured:

- I01 post-gate head flip → **caught** (`G-VERIFY-PAPER-CLAIMS`).
- I02 post-gate geometry-verdict flip → **caught** (same gate).
- I07 single stab-table cell flip → **caught** (`G-READING-DIVERGENCE`).
- I15 *consistent* two-cell flip (both readings of DG33, which passes
  the divergence gate) → **caught** (`G-HEAD-EQUALITY` +
  `G-VERIFY-PAPER-CLAIMS`).

That is an *accidental* seal — it works because a fourth file
independently carries those strings — but it is a real one, and it is
why U4's seam is 5-of-the-published-object wide rather than R4b's
10/10.  Note the answer to the protocol's #87 question: **the
per-cell `G-STAB` gates do NOT bind the published table cell** — they
read `nmS` from their own `S1` and stay truthful while the shipped
cell lies.  The binding comes from the aggregate divergence gate and
the head-equality gate.

**Repair (era-conformant lift).**  Hash each `GATES` and `PAYLOAD`
entry at creation into a running seal digest; record the digest in the
receipt; have the final integrity gate recompute the digest **from the
disk bytes** and compare against the seal — never against the live
objects.

---

## 2. MINOR findings

**MINOR-1 — MUT-SITEMAP's registry entry is false and names the wrong
gate.**  Registry (L106–108): "transposes two actors in the site map —
must die at the site-map bijection gate."  Implementation (L829–831)
is `out[ks[0]], out[ks[1]] = out[ks[1]], out[ks[1]]` — a **collapse**,
not a transposition; it dies at the five `G-SITEMAP` gates because the
image drops to 8.  I implemented the operation the registry *describes*
(I10) and measured it: `G-SITEMAP` **passes** (a transposition is a
bijection) and the mutant dies instead at
`G-STAB[CONFLICT-GRID(3,2)|initiator]`,
`G-DIAGONAL-INVARIANCE[CONFLICT-GRID(3,2)|initiator]` and the
CONFLICT-GRID(3,4) pair — at 2 of 5 crystals, and at **neither
DOUBLE-GRID** (the two swapped sites carry equal counts) **nor the
control** (whose gate expects trivial either way).  The receipt
therefore records a wrong mutant→gate binding.  This is the same
registry-defect class the worker fixed non-silently for MUT-NOT-FORCED
(#113/#115); the fix was not swept across the registry.  *Repair:*
implement the transposition, re-word the entry to name the
CONFLICT-GRID stabilizer gates, and add a separate
`MUT-SITEMAP-COLLAPSE` for the bijection gate.

**MINOR-2 — Coverage, at honest denominators (#34).**  **29 of 147**
gates die to a registered mutant; **118 uncovered**.  Of the 147,
**25 gate instances cannot fail at all** — the verdict argument is the
literal `True`: `G-MARK-POSIT`, `G-CONTROL-DECLARED`,
`G-GEOM-POP-INSTRUMENT`, `G-GEOM-ARMC-REGISTERED`,
`G-GEOM-SPATIAL-TAUTOLOGY`, `G-BRIDGE-SCOPE`, `G-DEAD-LIST-CITED`,
`G-WALL-BHS`, `G-WALL-DIAGONAL`, `G-WALL-L1-PERMUTATION`, plus
`G-GEOM-BLOCKED[*]`×5, `G-GEOM-SUB[*]`×5, `G-BRIDGE-LEGS[*]`×5.
Honest falsifiable denominator: **122; mutant coverage 29/122.**
Uncovered *and* falsifiable, named in full: `G-PROV[*]`×17 and
`G-PROV-ROOT` (covered by my I12 and the off-tree run, by no mutant),
`G-STAB-RECON[*]`×10, `G-GEOM-POP-WIDTH[*]`×8 (2 covered),
`G-DIAGONAL-INVARIANCE[*]`×6, `G-STAB[*]`×6, `G-BRIDGE-AXIS[*]`×5,
`G-BRIDGE-SUPPORT[*]`×5, `G-GEOM-HCTRL[*]`×5,
`G-GEOM-ARMB-IDLEFREE[*]`×5, `G-FORCED[*]`×4, `G-BRIDGE-DIAG[*]`×4,
`G-GEOM-HEIGHTPURE[*]`×4, `G-GEOM-ARMB-RENEWAL[*]`×4,
`G-ARENA-SCOPE`, `G-MARK-SOURCE-ROWS`, `G-V10-XCHECK-LAW`,
`G-READING-DIVERGENCE`, `G-GEOM-SEGMENT`, `G-WALL-KR`, `G-WALL-L1`,
`G-VERIFY-PAPER-NUMERALS`, `G-VERIFY-PAPER-PRESENT`.  Two specifics
worth the register: **all ten `G-STAB-RECON` gates are uncovered** —
no mutant perturbs one stabilizer route without the other, so the
two-route agreement is never adversarially exercised (MUT-APERIODIC-
DIVISION confirms this: it kills `G-STAB` and never `G-STAB-RECON`);
and **`G-FORCED`'s `maxhits == 1` conjunct is untested** — MUT-NOT-
FORCED writes `b.refusal` directly and never produces `maxhits > 1`.
Paper §13 says "Twelve registered, each dying at a named gate" without
a fraction.  *Repair:* print 29/147 (29/122 falsifiable) in receipt
and paper, and label the 25 as declarations.

**MINOR-3 — Waivers: 22/22 stated, 21/22 backed, 3 gates missing one.**
All 22 waivers sit exactly on gates whose verdict is the literal
`True` — a clean correspondence.  The 10 `MEASURED-THEN-DECLINED`
(`G-GEOM-BLOCKED`×5, `G-GEOM-SUB`×5) are backed by `G-GEOM-HCTRL`,
which *is* falsifiable and whose forcing I machine-checked (purity ⇒
empty control, 5/5).  The 5 `SCOPE-DISCLOSED` are backed by the source
law's own scope tag.  `G-CONTROL-DECLARED`'s waiver is genuinely
discharged — I verified the control returns the other value at
`G-STAB`×2, `G-GEOM-POP-WIDTH`×2, `G-BRIDGE-AXIS` and
`G-BRIDGE-SUPPORT`.  `G-GEOM-SPATIAL-TAUTOLOGY`'s exclusion is real
(`geom_verdict` consults only widths).  **One waiver is asserted with
no machine-checked forcing:** `G-DEAD-LIST-CITED` — "No measurement
above re-derives any of them", verdict literal `True`, evidence a
typed `{"dead_items": 5}`; nothing in the program checks it.  And
**three unfalsifiable gates carry no waiver at all** — `G-WALL-BHS`,
`G-WALL-DIAGONAL`, `G-WALL-L1-PERMUTATION` — each with typed-literal
evidence (`sprinkling_grade_LI_tests_run: 0`, `q12: 0`) that reads in
paper §8 as a measurement but is a declaration.  *Repair:* attach
three `DECLARATION-CARRIED` waivers (making 25), and gate the dead
list by name against the receipt's measurement keys.

**MINOR-4 — The selftest prints an unmeasured literal (#24).**
L2180 is `print(f"  wrote nothing: True")` — the "True" is typed, not
measured.  The adjacent `artifacts unchanged: {before == after}` is
the real check.  The convention is sound and I confirmed it two ways
(sha256 before/after; my own independent anchor corruption, I13).
*Repair:* `print(f"  wrote nothing: {before == after}")`, or drop it.

**MINOR-5 — Comparator-independence overclaims (three, all liftable by
wording).**  (a) Paper §5: "Each stabilizer is computed twice by routes
sharing no code and no typed constant."  The two routes share the
**field** (both consume the same `f` from `division_field`), `SITES`
and `L`, and — decisively — **`subgroup_name`**, the function that
produces the printed cell; a fault there corrupts both routes
identically.  `G-STAB-RECON` is an *algorithm* cross-check, not a data
cross-check.  (b) Paper §11.3: "Everything downstream of the record is
unshared: the marking predicate, the site map, the field, the
stabilizer algorithm."  **`regs_of` — the entire content of the
footprint reading — is shared** by both head paths (L1974).  (c)
`reconstruct_head`'s "site map by enumeration" is provably
value-identical to the name-parse for these actor names
(`sorted(D00..D22)[k] ↦ (k//3, k%3)`), so it cannot discriminate a
relabelling consistent with sorted order.  None of this is a false
number — my third and fourth routes confirm every cell and the head —
but the sentences claim more independence than is delivered.  *Repair:*
"the same field by two algorithms", and name `subgroup_name` and
`regs_of` as shared in §11.3.  Credit where due: the **field-level**
independence the §5 sentence promises *is* delivered, one gate later,
by `G-HEAD-EQUALITY`, whose reconstruction rebuilds record, marking and
site map.

**MINOR-6 — #62 anchors are unbounded below.**  `vanchor` (L204–216)
tests `quote in txt` with no minimum specificity.  I truncated V03's
92-character quote to the single character `"R"` (I09); the run shipped
with `verbatim_passed: 14` and 147/147.  The **delivered** object is
clean — all 14 quotes are 20–158 characters and all 14 consumers exist
as gates — but the check is not.  *Repair:* gate a minimum length and
`txt.count(quote) == 1`.

**MINOR-7 — Prose polarity is ungated (#20).**  I inverted
`G-GEOM-HEIGHTPURE`'s statement to the opposite claim ("the marked
events SHARE their layers with unmarked events throughout") while
leaving `len(mixed) == 0` untouched; the run shipped 147/147 with the
inverted statement in **both** artifacts (I08).  Nothing binds a gate's
prose to its boolean.  Era-wide gap; recorded for the denominator, not
as a repair demand on this unit alone.

**MINOR-8 — MUT-NOT-FORCED mutates after SEC 3 has consumed the
record.**  The substitution happens at L1225–1227, after
`G-MARK-TAG`/`G-MARK-ROOT` have already gated the *unmutated* 72-event
record.  Harmless (the run refuses at SEC 4) but the marking gates are
never exercised against a non-forced record, and the receipt under that
mutant would mix rows from two different objects.

---

## 3. The injections table

| # | injection | class | result | caught by |
|---|---|---|---|---|
| I01 | post-gate head flip | seam | **CAUGHT** | `G-VERIFY-PAPER-CLAIMS` |
| I02 | post-gate geometry-verdict flip | seam | **CAUGHT** | `G-VERIFY-PAPER-CLAIMS` |
| I03 | post-gate output `[DATA]` line | seam | SURVIVED | — |
| I04 | post-gate receipt gate statement + evidence | seam | SURVIVED | — |
| I05 | post-gate receipt payload (arena counts) | seam | SURVIVED | — |
| I06 | control row shipped under a crystal label | seam | SURVIVED | — |
| I07 | stabilizer-table cell flip, one cell | #87 | **CAUGHT** | `G-READING-DIVERGENCE` |
| I08 | prose polarity inversion, boolean intact | #20 | SURVIVED | — |
| I09 | verbatim-anchor truncation (92 → 1 char) | #62 | SURVIVED | — |
| I10 | **true** site-map transposition | registry | CAUGHT — at the **wrong** gate | `G-STAB[CONFLICT-GRID(3,*)\|initiator]`, not `G-SITEMAP` |
| I11 | gate-flag forgery (instrument-level control) | seam | SURVIVED | — |
| I12 | moving reference: a pinned sha altered | #91 | **CAUGHT** | `G-PROV[…]` + `G-PROV-ROOT` |
| I13 | my own committed-number corruption (A05) | anchors | **CAUGHT** | anchor stage, SEC 4 checkpoint |
| I14 | post-gate `stabilizer_table` receipt cell | seam | SURVIVED | — |
| I15 | consistent two-cell flip (both DG33 readings) | #87 | **CAUGHT** | `G-HEAD-EQUALITY` + `G-VERIFY-PAPER-CLAIMS` |
| I17 | banned sentence, paper-house wrapping | wall | SURVIVED | — |
| I18 | banned sentence, contiguous | wall | **CAUGHT** | `G-WALL-L1` |

*(I16 was a diagnostic probe, not an attack: it printed `widths_ok`
and `varies_witness` under MUT-GEOM-VARIES and supplied MAJOR-2's
measurement.)*

**17 attacks: 8 caught, 9 survived.**

---

## 4. The CLI verdict, in the contract's terms

**THE #82 CONTRACT HOLDS.**

- *plain* — byte-reproducible, and reproducible **off-tree and
  git-less** to both artifacts' committed sha256-12.
- *`--selftest`* — exit **0** under the confirmation-succeeded
  convention, artifacts sha-unchanged, nothing written, no residue;
  verified by my own hashes and by an independent anchor corruption of
  my own choosing.  One typed literal in its print (MINOR-4).
- *`--numbers`* — present and whitelisted.
- *`--mutant NAME`* — 12/12 die at named gates, artifacts sha-unchanged;
  registry complete both ways; one registry entry names the wrong
  operation and the wrong gate (MINOR-1).
- *everything else* — exit **2**, 16/16, artifacts untouched; unknown
  mutant names exit 2 and print the registry.

---

## 5. THE SEAM RULING

**THE GATE-TO-DISK DISEASE RECURS HERE — AND IT IS NARROWER THAN
R4b's.**

*Width.*  Six of the nine surviving injections are the seam class.
Everything the program publishes is mutable between its gate and
`render()`, and `write_and_verify` compares the disk against **live
memory**, not against a seal taken at gate time.  I shipped, with
`gates: 147, gates_failed: 0` on disk: a falsified output `[DATA]`
line; an internally contradictory receipt gate row; a falsified arena
count; the control's row under a crystal's label; a `stabilizer_table`
cell contradicting its own gate's evidence; and — at instrument level
— a demonstrably false `G-BRIDGE-DIAG` row published as **PASSED**.

*Why it is narrower.*  Four published objects **are** effectively
sealed, because a fourth artifact on disk independently carries them:
`G-VERIFY-PAPER-CLAIMS` binds the head and the geometry verdict to
`paper-14` verbatim, and `G-READING-DIVERGENCE` plus `G-HEAD-EQUALITY`
bind the ten stabilizer cells.  Post-gate flips of the head, of the
geometry verdict, of one table cell and of two consistent table cells
were **all caught**.  R4b's seam admitted ten survivors at the verdict
itself; U4's admits none at the verdict and all of them one layer
down, in the gate rows and payload rows that carry the unit's
evidence.  The seal is accidental — it is a consequence of writing the
head into the paper, not of a sealing discipline — but it is load
bearing, and it should be named as the pattern the engraving
generalises.

*Recommended lift.*  Hash each `GATES`/`PAYLOAD` entry at creation
into a running seal digest, record the digest in the receipt, and have
the final integrity gate recompute it **from the disk bytes** and
compare against the seal.  That converts U4's accidental four-object
seal into the engraving's full one.

---

## 6. Disclaimers

Read-only git throughout; all mutant, injection and off-tree work on
scratch copies under
`/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/u4-in/`.
The six target hashes were verified before any work and are unchanged
after it (`7e6db49f0e6e`, `c1ae8ec7fdbe`, `d1bfbbca40c9`,
`ae7a4ce48538`, `06b62ecb60a9`, `c4f2b33aa315`).  Concurrent workers'
files present in the tree and **not mine, not touched, not reviewed**:
`v14/code/r4b_momentum_exact.py` (modified),
`v14/code/giter_exact.py` and `v14/paper-16-gamma-iteration.md`
(untracked).  My single repo write is this file.  I did not read
`review-u4-operator.md` or `review-u4-effectus.md` before freezing
this one.
