# AUTOGLUE (paper-45) — K1 OPERATOR review

**Seat:** K1 OPERATOR, three-seat hostile panel, v15 AUTOGLUE.
**Object, hash-verified at open and at close:**

| file | sha256-12 (open) | sha256-12 (close) |
|---|---|---|
| `v15/paper-45-autoglue.md` | `09ee568a4bba` | `09ee568a4bba` |
| `v15/code/autoglue_exact.py` | `d750a64f153c` | `d750a64f153c` |
| `v15/code/autoglue_output.txt` | `1a287adcaead` | `1a287adcaead` |
| `v15/code/autoglue_receipt.json` | `34606049f1ef` | `34606049f1ef` |
| `v15/note-autoglue-pin.md` | `88c04df52c19` | `88c04df52c19` |

All six sources the paper's §2.1 table declares were re-hashed against the
tree and match: `v14/note-sec-adjudication.md` `7a82ffe7168a`,
`v14/paper-19-r3-weld.md` `50bb81e67942`, `v15/note-autoglue-pin.md`
`88c04df52c19`, `v14/paper-32-sec.md` `f3f43d94cd75`,
`v14/paper-40-sec2.md` `4fe88602280c`, `v14/code/era_template.py`
`d04a3eb58fbc`. 6/6.

Authority read: HANDOFF-PROMPT §4/§9, RUNBOOK §§13–15 through E-33,
v15/PLAN.md (W1/W2/W3), v15/LOG.md #2–#20 (the four reviews' orders).
Parents SEC/SEC-2/ARITY read at HEAD `32e184c4`. No in-flight worktree file
was opened.

**Method.** Everything below was rebuilt from the parents' definitions in a
scratch tree with **no code, no constant, no literal and no intermediate
shared** with `autoglue_exact.py`. Different primitives throughout: actors are
integers `0..14` rather than `('A', (i, j))` tuples; the union's relabelling
group is **constructed in closed form** from the arena's part structure rather
than searched, and then cross-checked against an independent backtracking
enumerator; the weld is decided by an edge-set theorem proved here and
cross-checked against a brute isomorphism search; the seam form is handled by
explicit 4×4 symmetric matrices over `Fraction`. Exact arithmetic end to end,
no float. Repo access read-only; this file is the sole write; only my own PIDs
were killed.

**Between delivery and adjudication every headline here — the object's and
mine — is a candidate reading.**

---

## GRADE: **ACCEPT WITH FIXES (AWF)**

**Zero false numbers.** Every mandated measurement reproduced exactly on first
rebuild. 47 of 47 receipt aggregates agree; so does every published table row
— all 24 distinct incidence rows at all four window cells, all 26 form-census
rows, all 4 fourth-direction rows, all 11 inventory rows, all 8 coverage rows,
all 8 extremal rows with all four of their columns, both multiplicity rows,
both whole-state fiber rows, all 5 price rows, all 5 two-step rows. **241
delivered quantities independently recomputed, 0 discrepancies**, over
≈ 0.8 M object-level evaluations.

All four verdict segments survive. The obstruction theorem survives. The Q50
disjointness survives, including under a base-map sweep that the unit did not
run. The derivation attempt survives in every cell.

Five MAJORs. None is a computational error and none moves a verdict; four are
prose or gate-description defects and one is an unpublished fiber. The grade is
AWF rather than A because **MAJOR-1 is a stated mechanism that is false at
every one of the 108 objects it explains**, and because MAJOR-3 shows two
published table columns are not properties of the objects the table keys on —
in both cases the paper asserts more than the run measured.

---

## What reproduced, exactly

### The update-window census (M1) — and it is a theorem, not a census

| creation rule | events alive | seam-spanning alive | refused | K1 |
|---|---|---|---|---|
| NONE | 54 | 0 | 401 | identical |
| CROSS-ONLY | 270 | 216 | 185 | identical |
| WITHIN-ONLY | 167 | 0 | 288 | identical |
| ALL-NEW | 455 | 288 | 0 | identical |

And the bound fiber: CROSS-ONLY and ALL-NEW admit **the same 162 events, 108 of
them crossings** — not merely the same cardinality, the **same set** (verified
by set equality on my own actor labels). 162 = 54 + 108, the profiles
`[0,0,3]` and `[1,0,2]`.

I can strengthen this row for the unit. The census is **forced**, and the proof
is two lines the paper does not have:

> At every one of the 455 × 4 transitions the geometry's incidence is a
> **subset** of the record's support (verified, 1820/1820) — the base cells are
> record pairs and the created cells are exactly pairs the event deposits.
> Two graphs on the same 15 vertices with one contained in the other are
> isomorphic iff they are equal. Hence **the weld is alive iff the rule creates
> every new pair the event opens**, and the four rows follow by counting
> profiles: `within = ∅` gives 270, `cross = ∅` gives 167, both give 54,
> neither constraint gives 455.

Checked against a brute isomorphism search at 108 (event, rule) pairs: 0
disagreements. This is liftable and it upgrades §3 from a census to a
proposition.

The same proof kills the reading and count-leg axes — see MINOR-1.

### The three rule gates

- **Blindness**: 1820 rule evaluations, 0 disagreements — reproduced, but the
  gate does not test what §1 and §3 say it tests. See MAJOR-2.
- **Equivariance**: reproduced and **far exceeded**. The unit swept 64 of the
  31,104 chart-preserving relabellings at 65 of 455 events. I swept **all 455
  events against 65 relabellings (118,300 checks) and all 62,208 relabellings
  at 5 events (311,040 checks)**: 0 exceptions in 429,340. The property is much
  more robust than the delivered sample licenses; deviation 5 can be retired.
- **Source audit**: I re-read the four rule bodies out of the file myself. Four
  bodies found, none containing `weld`, `fate`, `ALIVE`, `successors`,
  `verdict` or `detect`. Confirmed.

### The arena and its group

15 carriers, 54 realised pairs, none doubled, 9 fourth-class pairs per chart
(15 in the union), 36 cross pairs, 455 groups in 9 orbits, 288 seam-spanning
(two independent routes). All confirmed.

|Aut| = **62,208 by two structurally independent routes**: an explicit
backtracking enumeration, and a closed-form construction. The closed form is
worth having, and it is not in the unit:

> The declared-pair graph of one AG(2,3) chart is the complement of its fourth
> parallel class (three disjoint triangles), i.e. the complete tripartite graph
> K(3,3,3). The aligned k = 3 union glues two such charts **along one whole
> part**. The shared part is setwise fixed (its vertices are the only degree-12
> ones); each chart may exchange its two remaining parts; the charts may be
> exchanged. So |Aut| = 3! · (3!·3!·2)² · 2 = 6 · 72 · 72 · 2 = **62,208**, and
> the chart-preserving subgroup is the index-2 subgroup of order 31,104.

That also gives 1296 = |Aut(K₃,₃,₃)| its place, and makes the "index two"
clause of the equivariance statement a theorem rather than a measurement.

### The form leg (M2)

rank 6 on 10 unknowns, kernel 4; lattice 31, invariant under widening the box
by one; 31/31 positive definite; 18 cross directions per seam, 2 pairs per
index at every seam. All confirmed. The 31 and the 31 → 8 cut are both
hand-countable and I counted them by hand as well as by machine (1 + 8 + 12 +
8 + 2 = 31; fixing one entry to +1 leaves 1 + 3 + 3 + 1 = 8).

All 26 form-census rows reproduced exactly, including the `[1,0,2]` split
(4,8,8 / 8,4,8 / 8,8,4 / 8,8,8 at 27 each) and the `[2,0,1]` split
(0,4,4 / 4,0,4 / 4,4,0 at 36 each). 162 form-lawful, 108 crossings, 27 needing
no state move.

**§4.1's "27" mechanism is exactly right, and it is a biconditional.** I
measured it: over the 108 crossings, `state may stay` ⟺ `no doubling of this
event lands on a seam's own forward cell`, 27 with zero forward-doublings (all
stay), 54 with one and 27 with two (none stays). Clean; the paper may state it
as an iff.

**The fourth direction**: 468 readings, 0 agreements, with the four rows
`[1,1,1]→3`, `[1,1,2]→2`, `[1,2,1]→5`, `[2,1,1]→5` at 360/36/36/36. Confirmed,
including the kernel-zero claim (three declared directions on the three
unknowns of a 2-dimensional chart: rank 3, kernel 0) and the `[1,1,3] → 1`
counterfactual (2·1 + 2·1 − 3 = 1).

### Preparedness, the transition relation, the second step

29,791 states; best 9; 20,100 ready for none; the full coverage histogram
(0:20100, 1:6804, 2:2034, 3:622, 4:153, 5:18, 6:52, 9:8) reproduced row by row;
the best state carries the same completion at all three seams (mine is
(1,−1,0,1)³). Per-seam multiplicities 4:81 / 8:243 over 324 slots; whole-state
fiber 256:81 / 512:27; **0 crossings with a unique successor over all 288**.
Memoryless totality 162; persistent 9,691. All exact.

The two-step table reproduced **exactly** — 43/127/260/23/2, n₂ = 25, frozen 2
— from a first event chosen under my own, completely different labelling. See
MAJOR-5 for what that hides.

### Motivation, the price, the derivation attempt

All 11 inventory rows exact, including the parent's two hand-priced crossings
at (3, 9, 4)/1728 and (1, 3, 2)/576 and the event-free union at (1,1,1)/62208.
Motivated 77, lawful 162, overlap 0.

The Q50 chain, implication by implication, at every object:

| implication | K1 |
|---|---|
| no doubling ⟹ weld forced (the argued direction) | holds, 77/77 |
| weld forced ⟹ no doubling (the load-bearing direction) | holds, 77/77 — census only |
| three new pairs ⟹ a pair inside a sector | holds, 77/77 |
| no triple has three cross pairs (the two-colouring) | holds, max = 2 over 455 |
| a within-sector cell is refused by the form | holds, 468/468 |

Disjointness confirmed. See MINOR-3 on which direction the paper's mechanism
sentence actually argues.

All five price rows exact: 401 → 293, 0 → 3, 31 → 8, 0 → 15, 288 → 1.

All 8 extremal functionals exact in all four columns; every one of the 18 cross
directions cuts 31 → 8 (cut sizes are a singleton set); the direct sum survives
0 cuts and realises 0 crossings; the post-event determinant criterion is
4-valued; positivity 31/31; the convention-free price takes 1 value (36); the
one-sided minimiser equals the cut of **exactly 1** cross direction — and I can
name it: index (i=2, j=2, sign +1), the forward pairing of the two charts'
third declared directions, which is the direction SEC-2's driven crossing
occupies. The paper's "it IS the constraint one crossing imposes" is correct
and can be made specific.

### Text and provenance

All eight quotations the paper takes from the pin, SEC-2, paper-19 and the SEC
adjudication located verbatim in their pinned sources under
whitespace/markdown/unicode normalisation. The four verdict fences appear
twice each in the paper (head and §11) and match the four verdict lines of
`autoglue_output.txt` as a multiset. 69 distinct integer numerals appear in the
paper; the only two not traceable to a measurement are `19` and `32`, both
paper numbers in citations.

---

## MAJOR findings

### MAJOR-1 — §4.1's death mechanism for the 108 two-crossing events is false at all 108 objects

§4.1 says:

> Two crossings from one actor fix two entries of a seam's cross block, and at
> one of the three seams the entry that is their sum then leaves the range the
> readout admits

This is not what happens. Measured at every one of the 108 `[2,0,1]` events, at
the failing seam:

| at the failing seam, the two crossings fix | events |
|---|---|
| the **same** cross entry, with opposite signs | 108 |
| two distinct entries (the paper's account) | 0 |

The real mechanism, exhibited at an object and then verified over the whole
family:

> The doubled pair joins two same-sector actors, so they lie on a declared
> line; a declared line meets each fourth-class line once, so its third point
> is **the** shared site collinear with them. Seen from that seam the two
> actors are `s + d_i` and `s − d_i`: **the same direction index at opposite
> signs**. The two crossings therefore impose
> `nA[i] + nB[j] − (+1)·E[i][j] = 1` and `nA[i] + nB[j] − (−1)·E[i][j] = 1`,
> whose sum is `nA[i] + nB[j] = 1` — impossible for positive counts. The seam
> is empty for a **sign contradiction on one entry**, not for a sum leaving
> range.

At the other two seams the two crossings do fix two distinct entries (e.g.
`E[2][2]` and `E[0][2]`) and 4 completions survive — which is the situation the
paper's sentence describes, attached to the wrong seam.

No number moves: the `[0,4,4]` row, the 108, the 162 and the head are all
unaffected. What is defective is the only causal account the paper gives for
why 108 of the 288 crossings die, and it is defective at every object.

**Repair.** Replace the sentence with the collinearity/sign account above; it
is exact, it is checkable at every object, and it explains *which* seam fails
(the one collinear with the two same-sector actors) — which the current
sentence leaves as "depends on where the actors sit". Gate it: at every
`[2,0,1]` event, the failing seam's two cross indices agree in `(i, j)` and
differ in sign, 108/108.

### MAJOR-2 — G-RULE-BLIND is vacuous, and its published description is false

§1: "the rule is recomputed from a footprint carrying no name of the event that
made it". §3: "recomputed from a footprint stripped of every name of the event
that made it, the four rules return what they returned".

The instrument builds the "anonymous" footprint as

```
anon = {"cross": fp["cross"], "within": fp["within"], "doubled": fp["doubled"]}
```

`fp` has exactly four keys — `cross`, `within`, `doubled`, `pairs` — and
`pairs = cross ∪ within ∪ doubled`. So `anon` is `fp` with one **redundant**
key removed and the other three values passed through **unchanged**. Those
values are tuples of `frozenset`s of the actual actors: the footprint carries
every name of the event, before and after. Nothing is stripped. The comparison
`apply_rule(nm, anon) != apply_rule(nm, fp)` can fail in exactly one way — a
rule reading `fp["pairs"]` and raising `KeyError` — which is precisely what the
declared falsifier MUT-RULE-BLIND does.

So the gate tests one true but much smaller proposition: *no rule reads the
`pairs` key*. It cannot test name-blindness, because a rule that returned
`fp["cross"]` only when a named actor is present would pass it unchanged.
(MUT-RULE-NAME does exactly that and dies at G-RULE-EQUIVARIANT, not here.)

This is the E-23 shape — a falsifier/gate whose published description is not
what the code checks — at a gate the paper leans on by name in two sections and
in the licensing argument of §1 ("Three gates hold it to that rather than three
assurances").

**Mitigation, and it is real:** the property the prose claims **is** carried,
by G-RULE-EQUIVARIANT. I verified it far past the delivered sample (429,340
checks, 0 exceptions). So the claim is true; the gate cited for it is the wrong
one.

**Repair.** Either (a) re-describe G-RULE-BLIND as what it is — a
no-hidden-input gate over the footprint's key set — and re-attribute the
name-blindness claim to G-RULE-EQUIVARIANT; or (b) make it real: recompute each
rule from a footprint whose actors are replaced by opaque tokens, map the
result back, and require equality. (b) is preferable and cheap.

### MAJOR-3 — two of the three RSQ fibers published in §5.1 are not properties of the event; they move with the base map, and the parent's control for exactly this was dropped

`inventory()` reads the label and orient fibers at a single base map
`phi = perms2[0]` — the first automorphism the isomorphism search happens to
return for that geometry. SEC-2 guarded precisely this:

> the label and orient fibers are read at a base map, and re-read at a declared
> sweep of 32 of them, constant at every one

AUTOGLUE does not carry the sweep. I ran it. Holding the event fixed and
varying the base map over `Aut(geo)` (300 maps × 3 events per profile family):

| profile | inventory triple(s) seen | free items | verdict |
|---|---|---|---|
| `[0,0,3]` | (54, 3, **1**) and (54, 3, **2**) | **2 or 3** | MOVES |
| `[0,1,2]` | (12/3, **3**, 2) and (12/3, **6**, 2) | 3 | MOVES |
| `[1,0,2]` | (3, 9, 4) only | 3 | stable |
| `[2,0,1]` | (1, 3, 2) only | 2 | stable |
| `[2,1,0]` | (1, 1, 1) only | 0 | stable |
| `[0,3,0]` | (1, 1, 1) only | 0 | stable |

Both values occur for **one and the same event** (confirmed separately at 24
base maps for a single `[0,0,3]` event and a single `[0,1,2]` event). So §5.1's
split of the 54 `[0,0,3]` events into 18 with I-ORIENT 1 (free items 2) and 36
with I-ORIENT 2 (free items 3), and its split of the 108 `[0,1,2]` events
between I-DIRECTION-LABEL 3 and 6, are **base-map-relative partitions**, not
event invariants — a different admissible base map re-partitions the same
events. The `free items` column, published, moves 2 ↔ 3 for a fixed event.

**No verdict moves, and this is the important half.** The two rows that decide
Q50 (`[2,1,0]` and `[0,3,0]`, free items 0) and the two the price table and the
G-INVENTORY gate bind (`[1,0,2]` free 3, `[2,0,1]` free 2) are **stable across
every base map I tried, 900 samples each**. Motivated stays 77, disjointness
stays exact, the price row's 3 stays 3.

**Repair.** Restore the parent's control as a gate — recompute the label and
orient fibers at a declared sweep of base maps and require the value constant —
and it will fail on two rows. So either publish the two moving rows as
base-map-relative (collapsing `[0,0,3]` to one row with an ORIENT fiber
declared 1-or-2, and `[0,1,2]` to two rows keyed on the site-assignment fiber
alone), or define the fiber base-map-invariantly (e.g. as the number of
distinct fields over the whole group action, not at one representative). Either
way §5.1's row structure changes; the head does not. RUNBOOK §14 (symmetry
self-tests) and the #313 repair-propagation clause both bite here: the control
existed in the parent and was not inherited.

### MAJOR-4 — a false proportion in §1, invisible to every numeral gate

§1:

> of the seam-spanning conflict groups the arena admits, a little under half
> leave the dictionary alive once the target declares the cross links the event
> realises

The parent's sentence, which this unit's own instrument parses and this seat
re-read at the pinned bytes, is: *"Of the 288 seam-spanning groups, 216 leave
the dictionary alive once the target declares the cross links the event
realises."* 216 of 288 is **exactly three quarters**, not "a little under half".
(216 of 455 is a little under half — but the sentence's denominator is stated
and it is the seam-spanning groups.)

This is a claim about the paper's own inherited headline number, in its opening
paragraph, and it survives because the quantity is **spelled**: G-PAPER-COVERAGE,
G-PAPER-POLARITY and G-PAPER-REFERENT all scan numerals, and "a little under
half" contains none. This is the ungated-spelled-numeral class CONTRACT K3
found (92 spelled numerals ungated) recurring here — a recurrence of an
engraved disease is a MAJOR by default under the #313 clause.

**Repair.** "three quarters of them" (or "216 of the 288"), plus a spelled-
fraction sweep in the paper instrument covering *half, third, quarter, most,
nearly all, a little under/over*.

### MAJOR-5 — the two-step "25" is the minimum of a 25–43 fiber, chosen by an undeclared labelling-dependent tie-break, and the fiber is not published

§4.5 and §7 both read the second step as a fall: "25 are still form-lawful
where 108 could cross at the first"; "finds the allowed set falling from 108 to
25". Deviation 3 in §12 prices the *successor rule*; deviation 6 prices "the 25
is a property of that event's post-state". Neither publishes the fiber.

The instrument's first event is `sorted(absorb, key=ekey)`'s first `[1,0,2]`
member — an artifact of the actor-naming order, not a declaration. I re-ran the
second step from **all 108 lawful first crossings**:

| (n₂ crossings still form-lawful, n₂ with the state kept) | first events |
|---|---|
| (25, 1) | 3 |
| **(25, 2)** — the delivered cell | **6** |
| (26, 0) | 24 |
| (26, 1) | 12 |
| (27, 0) | 24 |
| (28, 0) | 12 |
| (41, 1) | 6 |
| (41, 2) | 3 |
| (43, 0) | 12 |
| (43, 1) | 6 |

n₂ ranges over {25, 26, 27, 28, 41, 43}. **25 is the minimum**, reached at 9 of
108 first events; the delivered pair (25, 2) at 6 of 108 (5.6%). The maximum,
43, is 72% higher, and "the allowed set falls from 108 to 43" is a materially
weaker sentence than the one shipped.

The 108 lawful crossings are a **single orbit** of the union's relabelling
group, so the spread is not accidental — it is the chart breaking a symmetry the
relation does not, which is precisely the effect §4.1 invokes to justify
censusing at the object. The same discipline applies here and was not applied.

This is the W3 / RUNBOOK §15 shape the DISC adjudication already ruled on
(order Z1: publish the fiber). It is not a number error: 25 is correct for the
event run.

**Repair.** Publish the fiber (the ten-cell table above, or its range), state
the first event as a declared choice rather than an incidental one, and make
§7's sentence read "falling from 108 to between 25 and 43 depending on which
crossing goes first". Gate: the second-step census runs at every lawful first
crossing and the head carries the range.

---

## MINOR findings

**MINOR-1 — two of the three window axes are provably inert, and the head sells
sixteen cells.** The head opens "FOUR LINK-CREATION RULES BY TWO READINGS BY
TWO COUNT LEGS ... AT BOTH ENDS OF EVERY TRANSITION", and §2.2 says "The first
three axes give the sixteen cells every event is run at." I checked the
delivered `incidence_census`: the four (reading, count leg) cells are
**byte-identical** — 12 of the 16 cells are exact copies of the other 4, and no
fate is ever COUNT-DEAD or ARITY-DEAD in any of the 1820 rows. My containment
proof above says why this is forced, not incidental: the geometry is always
inside the record's support, so QUOTIENT can only succeed where EMBEDDING does,
and the pulled-back field can only carry 1s and 2s. SEC-2's parallel table had
a genuine count-leg axis; this one does not, and the paper does not say so.
Disclose the inertness (it is a result — the window is 4 cells wide, not 16) and
either drop the two axes or keep them as a control with the collapse stated.

**MINOR-2 — "at both ends of every transition" is one object checked once.**
G-BASELINE-LAWFUL welds the delivered union onto the delivered geometry at all
four cells — once. Every one of the 1820 transitions starts from that same
pre-state (I confirmed: 1 distinct pre-state over all 455 × 4). The claim is
therefore true but carries no per-transition content, and the head's phrasing
implies 910 weld evaluations where there are 455 + 1. Reword to "from the one
lawful pre-state, at every event's post-state".

**MINOR-3 — the Q50 mechanism sentence argues the direction the theorem does
not use.** §5.1 supports "an event leaves the weld forced exactly when it
doubles nothing" with: "with no doubled pair the induced count field is
constant, and a constant field is moved by no relabelling." That argues
*no doubling ⟹ forced*. The disjointness chain consumes the converse
(*forced ⟹ no doubling ⟹ three new ⟹ within pair ⟹ refused*), and the converse
is established by census at 455 objects, not by argument. I verified both
directions hold (77/77 each way), so nothing is wrong — but the head says "BY A
THEOREM CHECKED AT EVERY OBJECT" and the theorem's load-bearing half is the
unproved one. Say which half is argued and which is enumerated; and note that
the enumerated half is arena-bound, which strengthens the S-1 a = 2 register.

**MINOR-4 — "the sector exchange and nothing else" is a coset of 31,104.** §3:
"the relabellings that do not keep the charts are the sector exchange and
nothing else". Measured: 31,104 chart-preserving and 31,104 chart-mixing maps.
The intended reading (one non-trivial coset) is right; the sentence as written
names one map. Reword to "the chart-mixing relabellings are the single
non-trivial coset of the chart-preserving subgroup, index 2".

**MINOR-5 — the declaration-price row's "1" is a different quantity that agrees
by coincidence.** The row reads "the declaration: objects the route declares |
288 | 1". The update column is computed as
`distinct_laws = len({frozenset(full_alive[nm]) for nm in ("CROSS-ONLY", "ALL-NEW")})`
— the number of *distinct lawful-event sets* produced by the two creating rules.
That is not "objects the route declares" (which is 1: the rule). The two agree
at 1 here; had the two rules differed, the row would have reported "2 objects
declared", which would be false. G-PRICE binds `distinct_laws == 1`, so the gate
inherits the referent error. This is the E-30 referent-binding shape. Compute
the declared-object count directly (it is 1 by construction) and keep
`distinct_laws` where it belongs, in the rule-fiber row.

**MINOR-6 — the CROSS-ONLY ≡ ALL-NEW "equivalence class" is one-sided
degeneration.** Measured: drop the fourth-direction refusal and the two rules
part company immediately — CROSS-ONLY 162, ALL-NEW **275**, not identical. The
equivalence is carried entirely by that one leg: ALL-NEW's extra creations are
all fourth-class cells and all of them are refused. The paper says "once the
form leg binds", so the substance is disclosed; but "the surviving rules form an
equivalence class this arena does not select within" reads as indistinguishability,
where the measurement is "the second rule's extra output is entirely illegal".
State the mechanism and the 162-vs-275 control.

**MINOR-7 — `form_ok` is computed once at the ALL-NEW post-state and reused for
the CROSS-ONLY arm.** In the M2 loop the successor sets and the fourth-direction
readings are taken at `post_cache[(g, "ALL-NEW")]` and the resulting
`form_ok[g]` is then applied to both arms in the rule-fiber computation. It is
harmless — the record update is rule-independent, so the successor sets are too,
and the fourth-direction leg is vacuous wherever CROSS-ONLY is alive at the
incidence (I verified both) — but it means the CROSS-ONLY arm never has its own
form leg evaluated, and the "equivalence" is partly a consequence of sharing one
computation. Disclose, or evaluate per arm.

**MINOR-8 — the 108 → 25 comparison is not like-for-like.** The step-1 standard
is incidence weld **and** non-empty successors **and** the fourth-direction
refusal; the step-2 predicate is non-empty successors alone. Applying the step-1
standard at step 2 leaves the delivered value unchanged (still 25 at that first
event) but moves the fiber's top from 43 to 39, so the defect is small — but the
sentence "25 are still form-lawful where 108 could cross at the first" compares
two different predicates. Match them.

---

## What I could not break

- **The obstruction theorem.** All three legs exact and exhaustive: 0 unique
  successors over all 288 crossings (I checked the full 288, not only the
  lawful 108); best advance declaration 9 of 108 with 20,100 of 29,791 ready
  for none over the complete 31³ state space; 468/468 fourth-direction refusals
  with kernel 0 re-derived independently. The verdict word is earned.
- **Q50 disjointness.** 77 / 162 / 0, and it survives the base-map sweep that
  MAJOR-3 shows the rest of the table does not. The two free-item-zero families
  return (1,1,1) at every one of 900 base-map samples each.
- **Nothing derived.** All 8 functionals, all 4 columns, exact; max-determinant
  selects the direct sum uniquely and the direct sum realises 0 of 18 and
  survives 0 of 18 cuts; the one-sided minimiser is exactly one cut. The
  self-defeating-criterion reading is correct.
- **The head's own numbers.** 108 of 288; 216 with no target; 162 at the bound
  fiber; 455/288/0 and 54/0/401 at the two control arms; 256/512 at 81/27;
  27 needing no move. All exact.
- **Counting-only discipline.** No fraction is published as a probability; every
  ratio carries its denominator. Confirmed by inspection of all 15 tables.

---

## Recomputation count (honest)

| leg | delivered quantities | object-level evaluations |
|---|---|---|
| arena, group, event set | 18 | 62,208 group elements + 62,208 backtracking leaves + 455 orbit sweeps |
| M1 incidence census + window inertness | 37 | 1,820 transitions × 4 window cells; 108 brute isomorphism cross-checks |
| rule gates (blind / equivariant / source) | 4 | 1,820 + 429,340 + 4 |
| M2 seam form, lattice, cuts | 9 | 81 lattice candidates × 18 constraints, by hand and by machine |
| M2 form census + fourth direction | 32 | 455 events × 3 seams × lattice enumeration; 468 fourth readings |
| M2 preparedness + relation + two step | 27 | 29,791 states; 324 slots; 108 re-runs of the 455-event second step = 49,140 |
| M3 inventory, motivation, price | 27 | 455 automorphism-stabiliser computations; 5,400 base-map samples |
| M4 extremal + obstruction | 39 | 8 functionals × 19 domains; 288 crossings × 3 seams |
| provenance, quotes, verdict fences, numerals | 26 | 6 sha + 8 quotations + 4 fences ×2 + 69 numerals |
| new measurements this seat made | 22 | the two-step fiber, the base-map sweep, the `[2,0,1]` mechanism tally, the containment theorem |
| **total** | **241** | **≈ 0.8 M** |

**Discrepancies against delivered values: 0.** Every one of the 241 agreed.

---

## Summary for the adjudicator

The unit is sound where it matters. Four verdict segments, an obstruction
theorem, a disjointness theorem and an eight-functional derivation attempt, and
I could not move any of them; every number in the paper and the receipt is
right, including the ones nobody would check. Two things I built for the attack
turned out to strengthen it and should be lifted into the unit: the containment
proof that makes §3's census a proposition, and the closed form for 62,208 that
makes the equivariance statement's "index two" a theorem.

The five MAJORs are all of one kind: **the paper says more than the run
measured**, in prose (MAJOR-1's mechanism, MAJOR-4's proportion), in a gate's
self-description (MAJOR-2), in a table's row structure (MAJOR-3), and in an
unpublished fiber at whose extreme the delivered number sits (MAJOR-5). None is
arithmetic. MAJOR-1 and MAJOR-4 are one-line prose repairs; MAJOR-2 is a
re-attribution or a twenty-line gate; MAJOR-3 costs §5.1 two rows and buys back
the parent's control; MAJOR-5 costs a ten-cell table and one qualified sentence
in §7.

Recommended disposition: **AWF**, repair without re-measurement except for
MAJOR-3's restored base-map sweep and MAJOR-5's 108-event second step, both of
which I have already run and whose results are printed above.
