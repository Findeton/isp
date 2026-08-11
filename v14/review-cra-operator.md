# CR-A PANEL — THE OPERATOR SEAT (K1)

**Unit under review:** CR-A, `v14/paper-05-accumulation.md` (paper-05,
REFINEMENT BY ACCUMULATION), delivered and committed as-is at `94df5ad`
(v14 ledger #41, 2026-08-09).
**Panel:** launched v14 ledger #174; protocol in-entry; this is row **K1
— OPERATOR**: rebuild the delivered verdict and its census from nothing
with independent machinery, verify the blocked verdict's mechanism,
check `MUT-CRA-BRIDGE`, audit prose against receipt.
**Reviewer disciplines observed:** read-only git; every run off-tree in
a scratch mirror; one repo write (this file); no LOG/STATUS/RUNBOOK
edit; no read of any concurrent worker's uncommitted state.

**Object, hash-verified before use (sha256-12):**

| artifact | sha256-12 | pin says |
|---|---|---|
| `v14/paper-05-accumulation.md` | `af0058432b79` | `af0058432b79` ✓ |
| `v14/code/cra_accumulation_exact.py` | `e289d3afc852` | `e289d3afc852` ✓ |
| `v14/code/cra_accumulation_output.txt` | `f398959da079` | `f398959da079` ✓ |
| `v14/code/cra_accumulation_receipt.json` | `5f68bac811bd` | `5f68bac811bd` ✓ |
| `v14/note-cr-batch-pins.md` (the pin, read first as law) | `1cfee4fc0891` | `1cfee4fc0891` ✓ |

---

## GRADE: **ACCEPT-WITH-FIXES (AWF)**

The verdict is **sound and reproduces exactly**. Every number in the
delivered head, in the census, in the selector table, in the trajectory
census and in the receipt was re-derived here by machinery that shares
no code, no data structures and no loop order with the delivered
instrument, and **not one number moved**. The blocked-verdict mechanism
— the pinned layer treats geometry as static — is confirmed, and the
central theorem is confirmed at a **strictly wider scope** than the
delivery measured (below, §2).

The AWF is carried by one MAJOR: the head-selecting variable of the
verdict is a **typed literal**, not a measured count, and so is the
`INVENTORY=i:0,ii:0` pair. The delivered head is nevertheless the right
one — the two quantities that justify it are separately and genuinely
measured by two other gates — so the repair moves no number and the
verdict string is byte-identical after it. But under this programme's
own engraving ("counts computed, never typed; heads DERIVED") the
delivered chain does not earn its head, and that must be fixed before
TERMINAL.

---

## 1. THE REPRODUCTION LEDGER

Independent rebuild written from the pin + paper + the pinned I7 source
alone (`scratchpad/cra-op/arena_common.py`, `rebuild.py`, `rebuild2.py`,
`rebuild3.py`): own site indexing, records carried as count-triples
rather than dict-of-dicts, own readout/positive-definiteness predicates,
own drag construction, own sequence classifier. Exact arithmetic
(`int`/`Fraction`) throughout. **142 recomputations of delivered
quantities, 0 disagreements** (full tally with the audit and hostile
probes in §6: 197).

**Arena and the I7 anchors (74 recomputations).** 9 admissible records
with `G-INDEF`/`G-SINGULAR` rejected; 12 lapse profiles; 132 ordered
pairs; the 5-record diagonal sector by name; record-IS-metric
re-encoding 81/81; the link-locality lattice 361 / 5100 / 781; the
closure census **54 cells, every cell equal to I7's own receipt value**;
`A-axis` closing exactly on the 5 diagonal records and `A-chart` on
`G-FLAT` alone; the lapse-pair rank 2 at 9 of 9 sites.

**Section A — the anchor observation (6).** `s` bit-identical after
`H_a[N]` and its inverse at **2376 of 2376** instances, 0 violations;
the pinned move monoid's s-image at depth 4 = **1 point over 341
visited nodes** (= 1+4+4²+4³+4⁴, i.e. no truncation and no collision);
the positive control with one geometry-writing generator = **5 points
over 781 nodes**. The singleton is a property of the pinned move set,
not of the instrument — confirmed.

**Sections B–D — the census and the inventory (14).** Probe cells 1010
(LIN) and 809 (BIL), each a deduplication of the same 3888-cell
(record, lapse, front, site) product; **LIN 4096 → 1752 advancing →
1209 admissible; BIL 4096 → 1224 → 23; total 8192 / 2976 / 1232.** The
per-link stabilizer space 262144, **133120 orbits, 4096 fixed points,
4096 chart-equivariant, 64 uniform**. Forced set = 2 (the identity, one
per family), forced-advancing = 0. (The forced set itself I audited by
reading rather than rebuilding — it is a presence test on the clause
table, not a derivation of `Δ = 0` from clause content; see MINOR-3's
neighbourhood. It is not counted among my recomputations.)

I confirm the two-route independence claim has real content: the
delivered admissibility predicate (`A>0, B>0, 4AB−Q²>0`) omits the
diagonal-count positivity that the second route checks explicitly, and
the two agree because `n_d = A+B+Q > (√A−√B)² ≥ 0` follows from strict
positive definiteness. My rebuild checked all three counts explicitly
and reproduced 1209 / 23 regardless.

**Sections E–H — selectors, theorem, trajectories, controls (48).**
Selector fibers 2976 / 1232 / 4096 / **4** / 0 / 0 / 0; the closure
fiber's **exact membership** re-derived — `LIN[0,0,0,0,0,1]`,
`LIN[0,0,0,0,0,2]`, `BIL[0,0,1,0,0,0]`, `BIL[0,0,2,0,0,0]`, i.e.
exactly the dilations `Δ = c·n_ℓ` and `Δ = c·N(x)n_ℓ`, `c ∈ {1,2}`, as
§6 states. 11 rules, 9 count-reading, 2 count-blind (`A-chart`,
`B-chart`), exactly 2 distinct read-link sets. Two-route commutation
defect: **2916 cells, 0 disagreements**. Trajectories: **972 cells →
531 / 117 / 108 / 216**, **27** distinct exact limit classes, 216
declinations all accounted, 486 (mover, schedule, record) cells with
**216 normalization flips**, doubled-horizon recheck **648 cells, 0
disagreements**. The mover-blind limit `(1/27, −1/54, 1/27)` reached by
exactly `M-CLOSED, M-FIAT, M-FRONT, M-SOURCE, M-TARGET` over **90
cells**, all six schedules, `NORM-INT` only. `M-FIAT` converges at 108
of 108 and diverges at none. Coupling profiles reproduce row for row;
FOREIGN 1/1, coupled 7. Discriminator **36 pairs, 29 separated**, and
the 7 unseparated pairs are exactly `M-DILATE|M-LAPDIL` plus all six
pairs inside `{M-FIAT, M-FRONT, M-SOURCE, M-TARGET}` — as §9 says.

**Byte-reproduction.** The committed instrument, run off-tree in a
scratch mirror with the repo sources symlinked read-only, produced
`cra_accumulation_output.txt` = `f398959da079` and
`cra_accumulation_receipt.json` = `5f68bac811bd` — **byte-identical to
the committed artifacts and to their pinned hashes** (`cmp` clean).

**Receipt and prose surface.** All 11 receipt-rendered sentences appear
**verbatim** in the paper; the paper's blockquoted verdict, the output's
verdict and `receipt["verdict"]` are the **same string**; counts
`gates 47 / anchors 31 / mutants 39 / disclosures 6 /
never-falsified 42` match the receipt object; the memo audit
`138195 hits / 13140 misses / 486 bypasses / 486 comparisons /
0 disagreements` matches. My own independent number sweep of the paper
found **191 numeric tokens, 58 distinct, 0 unbacked by the receipt** —
identical to the instrument's own sweep.

---

## 2. THE BLOCKED VERDICT'S MECHANISM — CONFIRMED

The verdict claims the pinned layer treats geometry as **frozen
background**, so accumulation-refinement has nothing to iterate. Three
independent legs, all confirmed here:

1. **Measured, not asserted.** `H_a[N]` and its inverse leave `s`
   bit-identical at 2376/2376 instances, and the whole pinned move
   monoid's s-image is a single point at depth 4 with an instrument that
   demonstrably sees 5 points when a writer is added.
2. **The only pinned clause that speaks to s-evolution says there is
   none.** `C-FROZEN` is verbatim in `v13/paper-ha-successor.md`
   (checked against the file myself), and it sets `Δ ≡ 0`.
3. **The missing object is the pinned source's own word.** Both §10
   quotes — "**No geometry-update law is constructed**" (§12 item 7) and
   the §14 opens line — are verbatim in the HA paper. The verdict's
   `MISSING=A-GEOMETRY-UPDATE-LAW` is not this unit's coinage.

### The static-geometry theorem holds — and I confirm it wider than delivered

The delivered instrument defines the commutation fiber by a **sufficient**
condition (`Δ = 0` on the rule's read links, plus all front-atom
coefficients zero), not by commutation itself. That is a real gap in
principle: a mover could commute without satisfying it. I closed it by
measuring the **true** defect.

- The front-blindness predicate is **exactly equivalent** on the
  admissible advancing set: true-zero s-defect = 116 movers, predicate
  = the same 116, **0 movers wrongly excluded**. (For BIL the predicate
  is formally stronger — true front-blindness is `c₀=c₄=0, c₁=−c₃`
  rather than all four zero — but no such mover is admissible and
  advancing, so nothing is lost.)
- Computing the **actual** m-defect `w[N,n;Λ(s)] − w[N,n;Λ(s+Δ)]` over
  every declared (record, lapse, front, site), the true commuting-and-
  advancing fiber is **0 at every one of the 9 count-reading rules** —
  `A-axis`, `A-linkframe`, `A-linkhalf`, `A-insert`, `A-insert-x`,
  `A-insert-2x`, `A-notransport`, `B-axis`, `B-all`. The delivery
  measured two directly and censused the other seven through the
  read-link argument; the direct measurement agrees at all nine.

**The theorem is therefore stronger than its delivered evidence, not
weaker.** I recommend the successor cite the direct nine-rule
measurement rather than the two-plus-census form.

I also probed §6's two-sided reading ("the count-blind exception buys
nothing"): **no** admissible advancing mover leaves `G-FLAT` untouched
at every declared cell (0 of 1232), so the exception is indeed bought
out. Claim holds.

---

## 3. `MUT-CRA-BRIDGE` — STILL DIES, AND ITS CLAIM WAS TRUE AT COMMIT DATE

Run off-tree from a copy of `v14/code/gmain_exact.py`
(`--mutant MUT-CRA-BRIDGE`, writes nothing):

```
predicate, clean object   : True
predicate, mutated object : False
reaches target (MEASURED) : True
killed                    : True          files written: 0
```

**It still dies at `T6-CRA`.** The gate's predicate
`cra_ok(mv, shared, forced) = mv > 0 and shared == 0 and forced ==
'FORCED=2|FORCED-ADVANCING=0'` turns false when the planted declaration
raises the measured map count to 1.

**Was the "zero maps, measured over every pinned source" claim true at
its commit date?** Yes, and provably so. I re-implemented `bridge_scan`
independently and ran it over gmain's 24 pinned source bodies, each read
`git show <sha>:<path>` at its pinned commit: **all 24 hash-verified
against their declared sha256-12, 118194 lines scanned, 0 bridge hits.**
Because every body is read at a pinned sha rather than from the
worktree, the measurement is commit-date-stable by construction — the
value I measure today *is* the value at `4747b47`. I also confirm
`_shared` is a genuine measurement (`_shared = len(_shared_hits)`,
gmain L3652), not a literal.

**Cross-unit caveat (gmain's row, not CR-A's, recorded for the panel).**
The detector is **line-local**: it requires an LHS needle, an RHS needle
and a relation needle on **one** line. The corpus is hard-wrapped at
~72 columns and carries 165 LHS-lines, 145 RHS-lines and 138 REL-lines
with zero triple-hits. The planted synthetic line is a single line and
is caught; of three realistic wrapped phrasings I constructed, **two
evade the scanner entirely**. Sensitivity is therefore established for
single-line declarations only. This does not touch CR-A's own numbers
— gmain's `T6-CRA` reads CR-A's verdict segments by path-value and they
are correct — but the "measured over every pinned source" phrasing
should be qualified as *line-local* wherever it is repeated.

---

## 4. FINDINGS

*Section references of the form "§N" inside the findings below name
sections of the reviewed paper, not of this review.*

### MAJOR-1 — the head-selecting variable is typed, not measured

`v14/code/cra_accumulation_exact.py` L1867:

```python
motivated = motivated_count(0)          # <- the argument is a literal
```

`motivated_count(class_i)` returns its argument unchanged in a plain
run. `motivated` is then the sole selector of the verdict **head**
(`build_verdict`, L1277: `if P["motivated"] == 0: head =
"CRA-BLOCKED-AT-STATIC-GEOMETRY"`). Two further verdict inputs are
literals in the same payload (L2406, L2417): `"class_ii": 0` and
`"motivated_all_converge": False`; and the receipt carries typed
`"class_ii_selected": 0` (L1880) and typed `"selected": 0` inside
`G-CLASS-II-SELECTS-NOTHING`'s evidence (L1858).

Consequences, stated exactly:

- The verdict segment `INVENTORY=i:0,ii:0,iii:1232` has **one** measured
  component. `i:0` and `ii:0` are typed.
- The plain-run **head cannot come out otherwise**. Had the census found
  a forced advancing mover or a stabilizer-selected one, the head would
  still have read `CRA-BLOCKED-AT-STATIC-GEOMETRY`.
- `G-CLASS-III-FIBER`'s second conjunct (`motivated == 0`) is `0 == 0`
  in every plain run.
- The declared falsifier `motivated-inject` does not repair this: it
  forces `motivated = 1`, which kills `G-CLASS-III-FIBER` before the
  verdict is built, so no run ever demonstrates the head moving on a
  *measured* input. `G-VERDICT-ALL-THREE-HEADS-REACHABLE` shows the
  **derivation** can emit all three heads, but only on synthetic
  payloads — it does not make the delivered head a measurement.
- The independent verdict comparator does not close the gap either. It
  rebuilds the `INVENTORY` segment from
  `inv["class_i_motivated_movers"]` and `inv["class_ii_selected"]`
  (L1349-1351) — which are the *same* typed literals written at L1880.
  The comparator is genuinely independent and genuinely sensitive (the
  per-segment flip test at L2436-2453 perturbs every field and confirms
  each segment moves), but on these two components it checks
  consistency between two copies of a typed 0, never correctness.

**Why the verdict nevertheless stands:** both quantities that justify
`motivated = 0` are genuinely measured elsewhere and separately gated —
`len(forced_adv) = 0` is computed from the clause table and the
admissible census and gated by `G-FORCED-ADVANCING-EMPTY`, and the
class-(ii) fact is gated by `G-CLASS-II-SELECTS-NOTHING`, whose
*predicate* (unlike its evidence dict) is measured. The delivered head
is the correct head.

**Exact repair (no number moves; the verdict string stays byte-identical):**

```python
# L1842-1843 already compute `uniform`; add the measured selection count:
selected_ii = len([pc for pc in uniform if chart_act(pc) != pc])   # == 0, measured
# L1858 evidence:
{"per_link": len(perlink), "chart_equivariant": len(equivariant),
 "uniform": len(uniform), "selected": selected_ii}
# L1867:
motivated = motivated_count(len(forced_adv) + selected_ii)
# L1880:
"class_ii_selected": selected_ii,
# L2406 / L2417 payload:
"class_i": len(forced_adv), "class_ii": selected_ii,
"motivated_all_converge": all(r["type"] == "CONVERGES" for r in traj_rows
                              if r["mover"] in motivated_movers),
```

I verified the repaired values: `len(forced_adv) = 0`, `selected_ii = 0`
(all 64 uniform points are chart-fixed), so `motivated = 0`, the head is
unchanged and `INVENTORY=i:0,ii:0,iii:1232` is unchanged. A new
falsifier should plant a *forced advancing* mover and confirm the head
turns to a non-blocked value through the measured path.

### MINOR-1 — §7 mis-characterizes 45 of the 108 undefined cells

§7 states: *"The 108 undefined cells are `M-NONE` and `M-TILT` at
`NORM-INT`, where nothing is written into any interval and the
denominator is zero."*

That is right for `M-NONE` and for `M-TILT` at `SCH-CONST` (where the
front is uniform, so the tilt vanishes), and **wrong for the other 45
cells** (`M-TILT` × the five non-constant schedules × 9 records). `M-TILT`
writes `Δ_ℓ(x) = n(x+ℓ) − n(x)`, which is emphatically nonzero there —
measured over 6 steps of `SCH-RAMP0` from `G-FLAT`: **90 nonzero writes,
total absolute magnitude 360, the record demonstrably changed** — but
the writes **telescope to zero** on the 3-torus, so `NORM-INT`'s
denominator vanishes. The count 108 and the verdict segment `UNDEF:108`
are correct; only the stated mechanism is wrong, and it is wrong in the
direction that hides a real fact (a mover can rewrite the whole geometry
while the per-event normalizer registers nothing).

This sentence is hand-written prose, not a receipt-rendered blockquote,
so the number sweep could not catch it — it carries no numeral of its
own beyond `108`.

**Exact repair** — replace the clause with:

> The 108 undefined cells are `M-NONE` and `M-TILT` at `NORM-INT`. For
> `M-NONE` nothing is written into any interval. For `M-TILT` the writes
> are nonzero wherever the front is not uniform, but the tilt telescopes
> on the torus, so the NET count of events written into intervals is
> zero: the denominator vanishes while the record moves. In both cases
> the normalization is undefined, not the limit — and the `M-TILT` case
> is a second instance of the normalization-relativity of §7.

### MINOR-2 — §3's "quoted verbatim" is verbatim up to emphasis and math spacing

§3 says both pinned answers are "quoted verbatim". The `C-INGREDIENTS`
quote as rendered in the paper drops the source's inline emphasis and
re-spaces the math: the HA source reads
`the **front tilt** $n(x+e)-n(x)$ … the **eventwise lapse value** $N(x)$`;
the paper renders `the front tilt $n(x+e) - n(x)$ … the eventwise lapse
value $N(x)$`. The instrument's gated needle *is* the true verbatim
string and does verify against the file, so this is a rendering slip,
not a false gate. (§10's two quotes and §5's `C-FROZEN` quote are
verbatim up to sanctioned whitespace/line-join normalisation.)

**Exact repair:** restore `**front tilt**`, `**eventwise lapse value**`
and `$n(x+e)-n(x)$` in §3, or change "quoted verbatim" to "quoted
(emphasis omitted)".

### MINOR-3 — `EXPRESSIBLE=12/13` counts a typed column

`ATOM_TABLE` carries the expressibility boolean as a literal per row,
and `G-ATOM-EXPRESSIBILITY` checks only that exactly one atom is banned
and that every admitted atom **names** a licensing clause — never that
the named clause's quoted text licenses that atom. The verdict segment
is therefore a count over a declaration plus a structural consistency
check. The paper is substantially honest about this (§3 declares the
negative control; deviation 1 and disclosure X-BOX declare the design
space as arena data), but the segment reads like a measurement.

**Exact repair:** either add a gate that matches each atom's prose
against its licensing clause's verbatim text (`n(x)`/`n_ℓ(x)` →
`C-PERMITTED`'s "event counts and record adjacency"; `N(x)` →
`C-INGREDIENTS`'s "eventwise lapse value"), or annotate the segment in
§3 and §12 as `EXPRESSIBLE` = declared-and-consistency-checked.

### MINOR-4 — cross-unit, recorded only

The line-local sensitivity of `MUT-CRA-BRIDGE`'s scanner (§3 above).
Belongs to gmain's row; noted here because this panel was asked to check
the mutant.

---

## 5. WHAT I TRIED TO BREAK AND COULD NOT

Recorded so the next round does not repeat the work:

- **The advancing/admissible censuses** — re-derived with an explicit
  three-link positivity test instead of the determinant short-circuit:
  identical (1752/1209, 1224/23).
- **The commutation predicate's necessity** — the delivered sufficient
  condition is exactly equivalent to true commutation on the admissible
  advancing set (116 = 116, 0 excluded), and the true fiber is empty at
  all nine count-reading rules, not just the two measured.
- **The count-blind exception** — 0 of 1232 admissible advancing movers
  fix `G-FLAT` at every declared cell; the paper's §6 "buys nothing"
  holds. (74 of 59136 (mover, lapse, front) slices are individually
  zero at `G-FLAT`, but no mover is zero across all of them.)
- **The classifier** — reimplemented independently; the 216 declinations,
  the 27 limit classes and the 648-cell doubled-horizon recheck all
  reproduce, with 0 recheck disagreements.
- **The hexagonal limit** — the `(1/27, −1/54, 1/27)` value is exactly
  the link-equalizing metric `[[2,−1],[−1,2]]` normalized by
  `|X|·|L| = 27`; independently derived, and its mover-blindness (5
  movers including the foreign one, 90 cells) confirmed.
- **The paper's numeric surface** — my own tokenizer and my own receipt
  walk agree with the instrument's sweep exactly (191 / 58 / 0).
- **Off-tree byte-reproduction** — clean, in a git-less scratch mirror.

## 6. RECOMPUTATION COUNT (honest)

| block | recomputations |
|---|---|
| arena + I7 anchors (incl. 54 closure cells, 9 rank sites) | 74 |
| section A (frozen s, both orbits, node counts) | 6 |
| sections B–D (probe cells, both censuses, stabilizer space) | 14 |
| sections E–H (7 selector fibers + membership, read-link census, two-route defect, 972-cell trajectory census, limits, flips, coupling, discriminator) | 48 |
| — *subtotal: delivered quantities re-derived* | **142** |
| receipt/prose audit (11 rendered sentences, verdict identity ×2, 5 counts, 5 memo values, 3 sweep values, 6 quotes, 2 byte-identities) | 34 |
| hostile probes beyond the delivered scope (true commutation at 9 rules, BIL front-blindness algebra, G-FLAT fixing ×2, bridge scan ×7, s-defect equivalence ×2) | 21 |
| **total** | **197** |
| **disagreements with the delivered numbers** | **0** |

## 7. FALSIFIER REGISTRY AND CLI CONTRACT — EXERCISED

Run in the scratch mirror with the committed artifacts placed alongside,
so the "artifacts unchanged" arm of the test is non-vacuous:

```
SELFTEST PASS (39 mutants)     39/39 DIED-CORRECTLY at their named gates
                               0 SURVIVED, 0 ARTIFACTS MOVED
```

After all 39 mutant subprocesses the two artifacts still hash
`f398959da079` / `5f68bac811bd` — unmoved. CLI contract (#82) holds:
`--bogus`, `--mutant nosuchmutant` and a bare `--mutant` each exit 2
and write nothing.

The registry's own honesty limits are declared by the unit itself
(deviations 9 and 10: one anchor mutant covers the source-hash class,
and the census-drop/fiber-corrupt falsifiers are declared at LIN only,
with the BIL twins carried in the never-falsified census). I confirm
those two clauses match what the code does, and that the 42 objects
named as never-falsified are named in the receipt rather than merely
counted.

---

**Seat verdict: AWF.** Fix MAJOR-1 before TERMINAL; MINOR-1 is a
substantive prose repair and should ride with it. Nothing found here
moves the head, the census, the theorem or any delivered number.

*Nothing in this file is a re-scoping of the unit's meaning post-Γ; that
is the effectus seat's row.*
