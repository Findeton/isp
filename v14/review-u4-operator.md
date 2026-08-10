# U4 (paper-14, renewal-only crystals) — OPERATOR-LENS HOSTILE REVIEW

**Grade: AWF (accept with fixes).**

**Object, hashes verified at read time and again at write time:** paper
`v14/paper-14-u4-renewal-crystals.md` `7e6db49f0e6e`, code
`v14/code/u4_crystals_exact.py` `c1ae8ec7fdbe`, output
`v14/code/u4_crystals_output.txt` `d1bfbbca40c9`, receipt
`v14/code/u4_crystals_receipt.json` `ae7a4ce48538`, all at commit `06b89fe`;
pin `v14/note-u4-pin.md` `06b62ecb60a9`; protocol
`v14/note-u4-hostile-protocol.md` `c4f2b33aa315` (commit `ab2bc83`); scout of
record `v14/note-routeA-successor-scout.md` `88375db9cec2`. All **17** of the
unit's pinned sources hash-match their declarations, including the four v10
constructors the protocol names — d60 `684cdb76552b`, d66 `3d0516ab106e`,
d67 `e80edf851d93`, d63 `89e170f40579`. **The pin's R1 sha for d66
(`3d0516ae106e`) is a typo**; the scout-verified `3d0516ab106e` is the true
one and the paper and code use it. The pin instructs "abort on mismatch and
report" — reporting it here; no abort, the object is right.

**Recomputations: 249**, all exact-arithmetic (integers and
`fractions.Fraction`; no float anywhere in my chain either), all against a
from-scratch rebuild that imports nothing from `u4_crystals_exact.py`. Plus
**24 whole-program runs** (2 plain, 12 mutants, 1 selftest, 4 argv-rejections,
1 off-tree, 2 paper injections, 2 repair verifications). **Zero false numbers
found. Every delivered number in the paper, the output and the receipt
reproduces exactly.** Not one finding below moves a computed value, and
neither verdict string changes.

**Disclosure.** Concurrent workers are active. HEAD moved from `e610e25` to
`1831644` during this review; every file I read was read through `git show` at
its pinned commit and I read no uncommitted state. I have **not** read
`review-u4-effectus.md` or `review-u4-instrument.md`. I did see the subject
line of commit `1831644` while re-verifying hashes at write time, and it
records that the instrument lens independently reached two of the findings
below (F3, the L-1 wrap defeat; F4, no mutant reaching VARIES) and
independently confirmed the stabilizers by a third route. Everything below is
from my own rebuild and was reached before I saw that line. My only repository
write is this file. All scratch work is under
`…/scratchpad/u4-op/`; the plain run was executed only there, on a
git-less copy of the pinned tree.

---

## 1. What I rebuilt differently

**A different grammar route, and it is the stronger one.** The unit
*re-derives* d42b1's transport grammar inside its own file (its SEC 2, "no
import"). I did the opposite: I loaded the **committed d42b1 source itself**
by text slice at `576275d55ecf` and drove it with my own builder. So the
unit's records and mine are produced by two different implementations of the
menu law, and the FORCED claim — every event *offered by the committed layer's
own menu* — is on my side checked against the actual committed layer, not
against a re-typing of it. The two agree event for event on all five records.

**My own builder, my own constructors.** `Rec.put` is mine; the five
constructors are re-typed from the v10 definitions (`double_grid`,
`conflict_grid` at d66 `3d0516ab106e`; `B`/`mint_and_spread`/CRYSTAL-2D at d60
`684cdb76552b`) rather than AST-extracted. On the control I additionally
derived `V1` twice — once as d60 does (off the menu) and once directly as
`vname(V0, {(G00,V0,0)}, G00)` — and gated the two equal.

**Three marking predicates, not two.** Tag (`e[0]=='r'`); the unit's tuple
*shape* predicate, re-typed; and a third of my own — the register footprint of
an arbitration is the only footprint that contains a **minted version name**
beside actor names, since `regs_of` adds `vname(...)` for kind `'r'` and for
nothing else. All three select the identical index set on all five records.

**A third stabilizer route (the protocol's decisive ask).** The unit uses
direct translation and the Fourier annihilator in `Z[ω]`. Mine translates
nothing and computes no character sum: I build **all six subgroups of Z₃² by
closure**, partition the nine sites into cosets of each, and ask whether `n` is
constant on every coset; the stabilizer is the unique maximal such subgroup,
and I gate that the invariant subgroups really do form a lattice with a top
(`assert all(H ≤ big)`) rather than assuming it. **All three routes agree
element for element in all ten cells.**

**My own geometry primitives.** `heights` by memoised longest-path recursion,
`sky` kind B from its definition, `covers`, and d60's `profile`, all re-typed;
then gated event-for-event and depth-for-depth against the committed d47a
`sky`/`heights` and d58 `covers` on all five posets (0 disagreements).

**The tag-drop lattice, which the unit prints only half of.** The unit shows
"drop {d,n} refuses" and "drop {n} rebuilds". I ran the full lattice, including
the direction it does not print.

---

## 2. Confirmed, and what it took to try to break it

Everything in the tables below is my number, not the unit's, computed before
comparison.

**K1 — the arena and the marking.** Five records rebuilt: 72/18, 96/24, 30/6,
66/12, 46/1 events/divisions. All FORCED: `maxhits == 1`, `refusal = None`, per
crystal. Three marking predicates agree index-for-index. **S4's content 61 of
61** — at every marked event, re-derived from the grammar's own `View` on the
prefix, every proposer named in the conflict key holds the newly minted value
immediately after, the superseded base is retired, and the minted value is
created by that very event. **The pair hypothesis is vacuous: 0 pair
arbitrations of 61**; conflict-key sizes are `{1: 13, 3: 48}`, so every key has
size 1 or 3 exactly as §3 says.

**K2 — the ten cells.** All ten fields, supports and stabilizers reproduce
digit for digit, by three routes. The scout refutation is confirmed in every
part: the readings **agree at 2 of 4** arbitration crystals (both DOUBLE-GRIDs)
and **diverge at exactly 2** (both CONFLICT-GRIDs); supports are 6/9 vs 9/9 on
the DOUBLE-GRIDs and 3/9 vs 9/9 on the CONFLICT-GRIDs; the divergence is
**one-directional** (`Stab_initiator ⊆ Stab_footprint` at all five, strict at
the two that move); `⟨(1,1)⟩` lies inside all eight arbitration cells; the
control is trivial at both readings. Both pin-required mutants behave as
claimed when planted in *my* field: the aperiodic division collapses DG32 to
order 1 by all three routes, the full-period control returns Z₃² by all three.

**K3 — geometry.** Chart width: all ten (crystal, depth) cells reproduce as
`(full max, attained, of which marked, restricted max)`, including the control's
two VARIES rows. The **exclusivity sharpening at depth 2 is exact — 3/3, 6/6,
1/1, 3/3, against 0 of 8 on the control** — and it does *not* hold at depth 3
(DG32's depth-3 argmax is 9 events, 6 of them proposals), which the paper
correctly confines to depth 2. Height purity: division layers `[1,8,9,12,13]`,
`[1,8,9,12,13,16,17]`, `[1,5]`, `[1,5,9,13]`, `[1]`; longest chains 14, 18, 6,
14, 21; **mixed layers 0 on all five**; every deficit full. §6.3's twenty
fractions, §6.4's sparse rows (`max|D|` 3,3,0,3,0; chains 5,7,2,4,1; mean ω
exactly 1 where defined and undefined on CG32 and the control), §7's link
counts, leg multisets and coset residues: all reproduce.

**The renewal-only rebuild, isolated in both directions.** Refusals at prefix
12 (`D00->D01`, `D00->D01`, `G00->G10`, `G00->G10`) and prefix 2 (`spread
G00->G01`), each at the crystal's first delivery, with **0 menu hits** at the
refusal. Idle-free rebuilds are event-identical to the committed records on all
five. I add the leg the paper does not print: **dropping *only* the delivery
refuses at the identical prefix and label on all five**, and no idle and no
merge occurs anywhere in any committed record. The isolation is therefore
necessary *and* sufficient — the claim "exactly one kinematic tag blocks the
rebuild, and it is the delivery" is stronger than the evidence the paper shows
for it, and it holds.

**Instrument.** Scratch plain run **byte-identical to both committed
artifacts**, twice; my tree carries no `.git` at all, so the git-less half of
#91 is discharged by the primary run; off-tree the run fails loudly at
`G-PROV-ROOT` with all 17 G-PROV gates red and writes nothing; `--selftest`
passes with artifacts unchanged; all four malformed argv forms exit 2; **all 12
registered mutants die at their advertised gates with artifacts unchanged**
(including the repaired MUT-NOT-FORCED, which dies at `G-FORCED[DOUBLE-GRID(3,2)]`).
147 gates, 0 failed; 42 anchors, 42 passed; 14 verbatim, 14 passed; 22 waivers;
195 registered numbers. The head is derived twice and gated as a complete
string; the reconstruction's site map is built by **enumeration over the sorted
actor set**, never by parsing the name digits, and agrees.

**A corroboration the unit left on the table.** v10's own committed d66 output
exhibits, at L284–286, "THE WIDEST WITNESS IN THE UNIT — DOUBLE-GRID(g=3,R=2),
base event index 42: **r-event** by D00, **height 8**, … |D| = 9, directions
[48…56]". I reproduce it exactly: index 42 is an arbitration, at height 8,
which is one of DG32's division layers. v10 therefore already committed, in
2026-07, a witness to both this unit's exclusivity sharpening and its height
purity — and it is not among the 42 anchors (see F2).

---

## 3. Findings

### MAJOR 1 — the ten-cell table has a one-line mechanism, and the paper does not report it

The headline is presented as a measurement with no reported mechanism. It has
one, it is exact, and it holds at **all ten cells without exception**:

> **On every crystal and at both site readings, the division-event field is
> affine in the indicator of the constructor's own SEED SET:**
> `n = c + m·1_S`, where `S` is the set of arbitrating seeds the constructor
> chooses. Hence `Stab(n) = Stab(1_S)` whenever `m ≠ 0`, and `Stab(n) = Z₃²`
> when `m = 0`.

Measured (my rebuild, all ten cells; `S` read off d66/d60's seed formulas, not
off the field):

| cell | c | m | Stab(n) | Stab(1_S) |
|---|---|---|---|---|
| DG32 initiator / footprint | 0 / 4 | 3 / 1 | ⟨(1,1)⟩ / ⟨(1,1)⟩ | ⟨(1,1)⟩ |
| DG33 initiator / footprint | 0 / 6 | 4 / 1 | ⟨(1,1)⟩ / ⟨(1,1)⟩ | ⟨(1,1)⟩ |
| CG32 initiator / footprint | 0 / 2 | 2 / **0** | ⟨(1,1)⟩ / **Z₃²** | ⟨(1,1)⟩ |
| CG34 initiator / footprint | 0 / 4 | 4 / **0** | ⟨(1,1)⟩ / **Z₃²** | ⟨(1,1)⟩ |
| CTRL initiator / footprint | 0 / 0 | 1 / 1 | 1 / 1 | 1 |

And `S` is a union of *full* `⟨(1,1)⟩` cosets on all four arbitration crystals —
residues of `j − i` are `{0,1}` on the DOUBLE-GRIDs and `{0}` on the
CONFLICT-GRIDs, every class complete — because d66 places its seeds at a
**uniform column offset**: `seeds = [ac[i][i]] + [ac[(j+2)%g][j]]`. On the
control `S` is a single site, an incomplete residue class, which is exactly why
the control returns order 1.

This does not reverse anything: the measurement is right, the two-way
requirement is genuinely discharged, and the mechanism is itself a fact about
the committed constructors, not about this unit's choices. But it changes what
the headline should be *read* as, and the candidate-readings rule is in force,
so the adjudicator should have it. Read with the mechanism, "the division
events of a conflict crystal form a crystal" says, on this arena, **the
constructors seat their arbitrations on a union of full diagonal cosets and
schedule them uniformly across rounds** — which also locates §8's diagonal
counterpoint precisely: the field's period direction is diagonal because d66's
seed rule is a uniform diagonal offset, not because anything about division
events prefers the diagonal. §8's refusal to read the counterpoint is right;
the reason it gives ("different objects") is true but weaker than the reason
available.

**Repair (exact).** (i) Add one measured row to SEC 5 — the affine
decomposition `(c, m, S, Stab(1_S))` per cell, gated per cell at #87 — and one
paragraph to §5 stating the identity and that it makes `Stab(n) = Stab(1_S)`.
(ii) In §8, replace "These are different objects" with the mechanism: the
invariance direction is the stabilizer of d66's seed set, whose cosets are
diagonal by the constructor's `(j+2)%g` offset rule. (iii) Add **S-U4-8**:
whether any conflict-crystal constructor seats its arbitration seeds on
something *other* than a coset union — that, not a new reading, is the test
that would make the headline non-tautological.

### MAJOR 2 — the 42 committed-number anchors are typed literals; the two pinned v10 outputs are hashed but never read for them

`v10/data/d60_crystal_exact.out` and `v10/data/d66_arbitration_crystal_exact.out`
are in `PINNED`, sha-gated, and loaded into `SOURCES`. `SOURCES[...]` is
consumed in exactly three places (the verbatim-anchor machinery and two reads of
the pin) — **never for the anchors**. Every "committed" value in the
`anchor(...)` calls is a typed literal (`Fr(1,2)`, `"0.4444"`, `9`, …) with the
v10 line number carried as a *string*, not as a lookup. So `MUT-ANCHOR` and the
selftest test the *computed* side only; a transcription error on the committed
side is invisible to the run, and the whole mitigation §11 deviation 1 prices
("forty-two committed numbers reproduce, against the zero that reading a
rewritten file would have carried") rests on hand transcription.

I closed it externally. I parsed both pinned `.out` files and checked each
anchor's committed value against the line it cites: **41 of 41 line-referenced
anchors are located verbatim on their cited line**; A34 alone cites "law,
checked at d66's committed rows" where a line reference (`d66 out L64`) exists.
**No number moves.** This is a #91-compliance and future-drift finding, not a
data finding.

**Repair (exact).** Extract each committed value from
`SOURCES["v10/data/…"]` by a line-anchored regex keyed on the citation already
in the table (`"d66 out L64"` → line 64), and gate the extraction against the
computed value directly, dropping the typed literal. Where a literal must
remain (the 4-decimal renderings), gate `literal == extracted` as a third
anchor per row. Give A34 its line reference.

### MAJOR 3 — the L-1 ban gate is whitespace-fragile and cannot fire on this paper's own wrapping

`G-WALL-L1` tests `BANNED in fh.read()` for a **97-character** sentence against
a markdown file whose prose is wrapped at ~72 characters. I injected the
retracted sentence into a scratch copy of paper-14, wrapped exactly as every
other sentence in that file is wrapped:

```
untested and is registered for a successor.  The weaker form is
precisely the form U4 tests, and precisely the form the corpus's
strongest relativity result took.
```

The run **passes G-WALL-L1** with `banned_sentence_hits: []`, exits 0, and
**writes artifacts**. Injected on a single line instead, the gate fails, the
run refuses at SEC 8 and writes nothing. So the wall the pin engraves as a
construction law is enforced only against a reproduction that violates the
file's own formatting convention — i.e. against nothing a real author would
write. §8's "the program gates its absence from both this paper and its own
source" and §13's provenance claim overstate the gate's reach.

**Repair (exact, verified).** Normalise whitespace on both sides:

```python
if re.sub(r"\s+", " ", BANNED) in re.sub(r"\s+", " ", fh.read()):
```

With this two-line change the wrapped injection **fails G-WALL-L1 and writes
nothing**, and on the pristine paper the run's **output and receipt are
byte-identical to the committed ones** — the repair costs zero. (The self-scan
stays safe: the `BANNED` definition's own line split leaves a `" "` between the
two literals, which survives normalisation.)

### MAJOR 4 — no registered mutant can reach the pre-registered VARIES verdict

§11 deviation 5 says "The pre-registered VARIES path is not thereby
unreachable — a mutant drives the run onto it and the string is emitted before
the gate kills the run." Measured: under `--mutant MUT-GEOM-VARIES` the only
string emitted is the *per-row* `VARIES-9->3` inside a gate's prose, and the
**segment verdict is still
`GEOMETRY-INVARIANT-AT-THE-CONTROLLED-ROW-REST-BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL`**.
The cause is at the code's own line 1633: `widths_ok` is recomputed from a
fresh `profile(poset_of(...), [i for i,e in … if is_division(e)])` — the
**unmutated** marked population — so the mutant's `pop` never reaches the
predicate that selects the verdict branch. `GEOMETRY-VARIES-<witness>` is dead
code under every registered mutant.

A second defect sits in the same branch: `varies_witness` is populated by *all*
crystals including the control (the plain run's receipt already carries
`["D60-GRID(3,12)|d=2|max|D|:3->1", "D60-GRID(3,12)|d=3|max|D|:3->2"]`), while
`widths_ok` quantifies over `ARB` only. If the branch ever fired it would emit a
witness list led by the control's *required* variation.

**Repair (exact).** (i) Compute `widths_ok` from the same `pr` the loop
already built (`all(pf[d]["max"] == pr[d]["max"] for arbitration crystals)`),
so the mutant reaches it; re-run `--mutant MUT-GEOM-VARIES` and gate that the
emitted segment verdict starts `GEOMETRY-VARIES-`. (ii) Filter
`varies_witness` to `ARB` at the append site. (iii) Restate §11 deviation 5 to
say which string the mutant emits, at which level.

### MINOR 1 — §2's cross-check coverage claim is false as written

§2 says the rebuild is cross-checked "at **every atlas row and count those runs
printed for these crystals**". It is not. v10's committed outputs print, for
these crystals, at least: DG32's d=3 mean|D| (`2.889`, d66 L344); DG32's and
CG34's d=2 **width histograms** (`{0:10, 1:30, 2:5, 3:22, 4:2, 9:3}` and
`{0:9, 1:25, 2:16, 3:7, 4:3, 5:3, 6:3}`, d66 L279/L275); DG32's **tag census**
`kinds={'d': 12, 'p': 42, 'r': 18}` (d66 L342); DG32's arbitrations **by
proposer count** `{1: 6, 3: 12}` (d67 L135); the excision row `n 72→45` with
`0.5111` / `0.9333` (d66 L254); and the widest-witness row (d66 L284–286).
None is among A01–A42. The enumeration that follows the em-dash *is* accurate;
it is the leading quantifier that is not.

I verified all of these reproduce in my rebuild anyway, so the fix is free.
**Repair.** Either anchor them — the histogram's `9: 3` is literally §6.2's
"attained at 3", and the widest-witness row corroborates the exclusivity
sharpening and height purity at once — or replace "every atlas row and count"
with "the atlas rows and counts enumerated below". Anchoring is the better
buy: it converts 42 anchors into ~50 and picks up v10's own r-event witness.
(d67's committed output `v10/data/d67_k4_double_grid_exact.out` is not pinned at
all, though d67's *code* is; it carries a further direct cross-check of DG32 at
its L85.)

### MINOR 2 — two of the ten cells are constant fields, and a constant field is a vacuous positive

CG32 and CG34 at the footprint reading have `m = 0`: the field is constant (2
everywhere, 4 everywhere). A constant field on *any* finite group has the full
group as stabilizer, whatever record produced it — here it is forced by the
construction, since each round's three arbitrations partition the nine actors
and every site is covered exactly once per round. §5 names the constancy, which
is honest, but §10's "TRUE, two-way, at every one of the ten cells" weighs those
two cells equally with the eight that carry information.

**Repair.** In §5 and §10, say that at those two cells the positive is carried
by a *constant* field and is therefore uninformative about periodicity beyond
the construction's own partition; the informative arbitration cells are 6 of 8.

### MINOR 3 — "enlarges" is not what was measured

§5 and S-U4-5 say the footprint reading "enlarges the stabilizer and never
shrinks it". Measured: it enlarges at 2 of 5 records and leaves it **equal** at
3 of 5. "Never shrinks" is the measurement; "enlarges" is not. **Repair:** "the
footprint stabilizer contains the initiator stabilizer at all five records, with
strict containment at the two CONFLICT-GRIDs."

### NIT 1 — "no code and no typed constant"

`stabilizer` and `stabilizer_by_characters` do share `SITES`, and share the
modulus 3 (spelled `L` in one and `3` in the other). The claim is very nearly
true and the routes are genuinely different; "sharing no algorithm and no
derived input" would be exactly true.

### NIT 2 — the output has no SEC 2

The code's SEC 2 (the rebuilt grammar) emits nothing, so the output runs
SEC 1 → SEC 3. A reader following the numbering sees a gap.

---

## 4. What I ruled on, where the protocol asked for a ruling

**Height purity, and what it forbids.** The measurement is exact on all five
records and I confirm the implication is a **theorem**: the unit's control is
"same size, same height histogram, drawn from unmarked events", and since no
unmarked event sits at any marked height, any height-histogram-matching
population *is* the marked population. The reading is honest, and I can make it
stronger than the paper does. I pooled the unmarked events of **all five
records** and asked at which marked heights a control could be drawn:
heights 5, 8, 9, 12, 13, 16, 17 are available somewhere, **height 1 is
available nowhere** — layer 1 is marked-only on every one of the five records
(6, 6, 3, 3, 1 events, 0 unmarked). Since every record has marked events at
height 1, even a cross-record height-matched control is unbuildable. §6.1's
"cannot be built at any crystal" therefore survives the obvious widening of its
scope, and the paper should say so rather than leave the same-record scope
implicit.

Is "it forbids the reading outright" the honest strength? Yes, at the KR wall's
own terms: the catalog says a dimension reading without a height control is
worthless, and no height control exists. The unit certifies nothing it cannot
control and emits BLOCKED rather than bending the pin's INVARIANT/VARIES pair —
that is the right call, and §11 deviation 5 prices it correctly *except* for the
emittability claim, which is MAJOR 4.

**The chart-width row's logic.** "A maximum over a subset equals the maximum
over the whole set exactly when the maximum is attained on the subset" is
correct, and it is genuinely not a population average, so the empty height
control does not reach it. The row carries the segment. Confirmed.

**The falsifier.** §6.6's refusal to fire paper 0 §10's third falsifier is
right and its reasoning is sound: the falsifier is conditioned on sparse records
*destroying a geometry*, and what is measured is that the sparse record is not
*constructible*. My tag-drop lattice makes the distinction sharper than the
paper does — the block is caused by the delivery alone, in both directions.

**The pin's walls.** L-1 is argued before any test and then declined; the
measurement run is a permutation action inside L-1's own scope guard; no
sprinkling, boost, rapidity or frame appears anywhere in the measurements; the
diagonal is named and not read. All four honoured **in substance**; the L-1 ban
is honoured in substance but not in *enforcement* (MAJOR 3).

---

## 5. Prose audited against the receipt

Every quantitative sentence in §§2–7 and §13 checks out against the receipt and
against my own rebuild: the five-row arena table; "forty-two committed-number
anchors reproduce, none moves" (42/42, and 41/41 located by me in the pinned
v10 text); the event-count laws at every committed family member (72, 120;
66, 102, 174) and their predictions (96, 30); "0 pair arbitrations among the 61
marked events"; "61 of 61"; the ten-cell table; "2 of the 4 … diverge at the
other 2"; the five height-purity rows; the ten chart-width rows and the
exclusivity counts; the twenty §6.3 fractions; the five sparse rows; the five
refusal rows and the five idle-free event counts; the twenty §7 link counts and
the five leg multisets; "Seventeen pinned sources"; "Fourteen verbatim
anchors"; "Twelve registered". `dec4`/`dec2` are exact Fraction renderings —
`float(` appears nowhere in the source, and the four-decimal anchors are string
comparisons against v10's own printed digits.

Three prose claims do not survive: §2's "every atlas row and count" (MINOR 1),
§8/§13's "gates its absence from … its own source" and the L-1 enforcement claim
(MAJOR 3), and §11 deviation 5's emittability claim (MAJOR 4). §11 deviation 1's
mitigation is weaker than it reads (MAJOR 2). Nothing else in the prose
overstates the receipt.

---

## 6. Grade

**AWF.** The object is real, the arena is right, the marking is right, and the
ten-cell table is right by three independent routes. Zero false numbers across
249 recomputations; both verdict strings stand as delivered; byte-identity,
git-lessness and off-tree loudness all confirmed. Two of the four MAJORs are
instrument defects with two-line repairs I verified byte-identical on the
pristine object (MAJOR 3) or single-line (MAJOR 4); one is a #91 compliance gap
that I closed by hand and that no delivered number depends on (MAJOR 2). The
one that reaches the physics is MAJOR 1, and it does not contradict the unit —
it supplies the mechanism the unit measured around, and it is the thing an
adjudicator most needs before ruling on a candidate reading.
