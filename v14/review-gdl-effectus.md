# GDL (paper-25) — K2 EFFECTUS-LENS hostile review

**Seat:** K2 (EFFECTUS), ledger v14 #222. **Object at `4c85ca4`:**
`v14/paper-25-gdl.md` `e98003841378`, `v14/code/gdl_exact.py` `81595d600575`,
`v14/code/gdl_output.txt` `39128fafc7bf`, `v14/code/gdl_receipt.json`
`b87016e96285`; pin `v14/note-gdl-pin.md` `fe9533371046`. **All five hashes
verified at open and at close of this review; unchanged.** Interpreter
`/opt/homebrew/bin/python3.13`. Read-only; this file is the seat's one repo
write.

**GRADE: AWF (ACCEPT WITH FIXES).** **243 independent recomputations, zero
false numbers found.** Every published *number* in this unit survived. What
does not survive is the **verdict word**, three prose sentences in the two
sections the paper itself flags as its deepest, and the prediction row's
scope. The instrument is in excellent condition: exact arithmetic throughout,
the walls hold under my own scan, the fiber census is honest, the VACUOUS
stamping is real, and the paper→receipt numeral sweep is clean but for one
derivable denominator. The repairs below are all textual plus one small
re-measurement (M5); none requires re-running the machine.

---

## 1. What I recomputed

| # | recomputation | result |
|---|---|---|
| 1 | 5 object hashes at open, 5 at close | all match |
| 2 | frozen-arm support ladder, both occupancy predicates, 5 steps | 10 rows, see M4 |
| 3 | unitarity of all 6 declared coins over `Z[w]` | 6/6 exactly unitary |
| 4 | co-occupancy threshold, frozen arm, all 6 coins, both predicates | 12 determinations |
| 5 | frozen `D1`/`D2`/`D3` ladders, exact fractions | 15/15 reproduce |
| 6 | site-marginal blindness under site-**dependent** unitary coins, 48 randomized foreign records | 4 aggregate results |
| 7 | mod-3 record degeneracy, `n ∈ {1,2,3,4,7}` × 3 functionals | 15 values |
| 8 | arithmetic identities (`11044`, `9751`, `10954`, `10959`, `164310`, `54770`, `98586`, `177 = 155 + 22`, …) | 17/17 |
| 9 | paper→receipt numeral sweep, 313 numerals | 1 finding (m2) |
| 10 | passing-class recount on all 28 PARTIAL cells | 28, see M6 |
| 11 | coupled↔frozen verdict-word comparison, all 28 PARTIAL cells | 28, see M1 |
| 12 | the 90 grid rows (45 coupled + 45 frozen) re-censused | 90 |
| 13 | fiber rows: signature, ladder, frozen-distinct | 7/7 |

**Total: 243.** The frozen ladders reproduce to the last digit: `D1 = 1,
11/27, 619/2187, 40411/177147, 81857/531441`; `D2 = 0, 0, 128/729,
33920/177147, 184192/531441`; `D3 = 2/9, 2/9, 266/729, 602/2187, 2654/6561`.
The domination witnesses of §8 are therefore anchored on my side too.

---

## 2. MAJOR findings

### M1 — THE HEAD'S GRAMMAR. The licensed word is `GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR`, not `GDL-PARTIAL`. (decisive row)

I rule on the pin's own text, and the ruling is carried by three independent
legs, any one of which is sufficient.

**Leg 1 — TEXTUAL.** The pin's outcome grammar is
`GDL-LAW-FORCED` / `GDL-LAW-COIN-RELATIVE` / `GDL-PARTIAL` / `GDL-DECOUPLED`
(*"no functional relation — first-class and informative"*) / `GDL-BLOCKED-AT`.
The question is whether "functional relation" means *any* relation or
*gravitational* relation. **Every arm carries the `GDL-` prefix**, and the pin
defines the `G` in `GDL` itself, in §4: *"a relation that holds identically
frozen is NOT a gravitational-decoherence relation."* The prefix therefore
scopes the gloss: `GDL-DECOUPLED` means *no gravitational-decoherence
functional relation*. The pin's own head-noun ("THE GRAVITATIONAL-DECOHERENCE
LAW") and its own §"THE QUESTION" ("this unit measures whether **the
relation** exists", where *the relation* is the one between decoherence and
geometry growth) say the same. The delivered measurement is
`gravitational_count = 0`. The DECOUPLED arm is therefore *satisfied*, not
merely available.

**Leg 2 — INSTRUMENTAL, and this is the finding I would not have expected.**
`GDL-DECOUPLED` **could not have fired**. The selector (`gdl_exact.py`
`outcome_word`, and its independent twin at the head builder) is:

```
if gravitational:                                        -> LAW-FORCED / LAW-COIN-RELATIVE
if not exact and not partial and not identities and not moves -> DECOUPLED
else                                                      -> PARTIAL
```

Three of DECOUPLED's four conjuncts are **gate-forbidden in any run that
writes an artifact**: `identities` is forced TRUE by `G-PURITY-SPLIT`,
`G-RATE-IS-BORN` and `G-RATE-TOTAL` (each requires `violations == 0`), and
`moves` is forced `> 0` by the two-way gate `G-BLINDNESS-D3` (its declared
mutant `MUT-D3-READS` sets `d3_moves` to `0` and "must die"). So DECOUPLED
requires the run to be simultaneously *broken* and *empty*. **The pin's
"first-class and informative" arm is a dead branch**, and `G-REACHABILITY`
does not cover it — it certifies falsifier reachability, not outcome-word
reachability.

Consequently **§13's sentence "The pin's `GDL-DECOUPLED` outcome was
available and is not what was measured" is FALSE**, and §1's "Five outcomes
were pre-registered, including `GDL-DECOUPLED` as a first-class finding. The
delivered outcome is `GDL-PARTIAL`" misrepresents a forced default as a
selection. The word was never chosen against DECOUPLED; DECOUPLED was
unreachable.

**Leg 3 — MEASURED. `PARTIAL` is a word the null control also earns.** I
re-censused both grids:

- frozen grid: **38 PARTIAL, 6 VACUOUS, 1 EXACT** of 45;
- **26 of the 28 coupled PARTIAL cells carry the identical verdict word
  `PARTIAL` on the frozen control** (the two exceptions are `RES-BRANCH ×
  G5 × D2` and `× D3`, VACUOUS there).

The frozen control is the stage whose record never grows and which the paper
itself says "cannot testify at all". A head word that the null control earns
at 38 of its own 45 cells is not reporting a finding. Add the paper's own
`GRAVITATIONAL-CELLS=0` in the same head and the tension is internal.

**And the zero is FORCED, not contingent** — see M7. The one exact cell is
`D1 × G5-RATE-SITE`. `G5 = eps(x) = p(x)` is the site marginal, and the site
marginal is record-blind **by theorem**. So *both sides* of the one exact
identity are functions of a record-blind quantity: the identity **could not
have failed** on the frozen stage. The frozen exclusion of the only exact cell
was not a measurement that came out one way; it was compelled. And the genuine
record functionals `G1`–`G4` produce no exact cell at any resolution.

**REPAIR (exact).** Replace the third head segment's word and open its
brackets with the bar and with what survives it:

```
GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR-<THE GRID=MEASURED-NOT-FITTED(45 CELLS
PER ARM ... 2 EXACT, 28 PARTIAL, 15 VACUOUS AND STAMPED) -- FROZEN-EXCLUSION=2
OF 2 EXACT CELLS EXCLUDED, AND FORCED: BOTH SIDES OF THE ONE EXACT IDENTITY
ARE FUNCTIONS OF THE SITE MARGINAL, WHICH IS RECORD-BLIND BY THEOREM --
GRAVITATIONAL D=f(G) CELLS=0 -- THE 28 PARTIAL CELLS ARE NOT ADJUDICATED
GRAVITATIONAL BY ANY GATE: THE BAR IS INAPPLICABLE TO A RELATION THAT DOES NOT
HOLD, 26 OF THE 28 CARRY THE IDENTICAL WORD ON THE FROZEN CONTROL, AND 11 OF
THE 28 HAVE ZERO PASSING NON-SINGLETON CLASSES -- WHAT SURVIVES THE BAR IS
BETWEEN-ARM, NOT WITHIN-ARM: THE SEPARATION LADDER D3@3 / D1@4 / D2@4
IDENTICAL ACROSS 7 OF 7 FIBER MEMBERS, AND D1 COUPLED-DOMINATES AT BOTH ITS
SEPARATING STEPS WITH EXACT WITNESSES (D2, D3 NO-DOMINATION) -- ...>
```

Note what the repair *gains*: the unit's real gravitational content is the
**between-arm** content (ladder + `D1` domination — the latter an admissible
claim form under the pin's §3, and immune to the frozen bar because it is a
coupled-vs-frozen statement). The delivered `PARTIAL` both over-reports (28
un-adjudicated cells read as partial gravitational relations) and
under-reports (the two surviving between-arm claims are not in the word). The
repaired head fixes both directions. **Also repair §1 and §13's availability
sentences**, and add `G-OUTCOME-REACHABILITY`: every arm of the declared
outcome grammar must be shown reachable by a witness configuration, or the arm
is declared dead in the receipt.

### M2 — §7's "the two ψ-internal values are blind too" is FALSE by the paper's own instrument, in the same section.

§7 closes: *"paper-20's staleness-blindness theorem said no closure internal
to the state at a single time can distinguish a frozen stage from a coupled
one. This is the quantitative form of the same fact: **the two ψ-internal
values are blind too**, and only the third functional — the one that reads the
record — is not."*

Three paragraphs earlier the same section measures `D2` moving at **54,593 of
54,770** object-and-field pairs. Under §7's own operational definition of
blindness (`moves` under a declared foreign count field) `D2` is **not** blind.
The sentence also conflates two different measured facts — record-blindness
(§7) and first-separating-step (§8) — which are not the same thing; in the
separation sense the contrast is a *one-step delay*, not blindness.

The paper-20 citation itself is accurate (I checked §8.3 verbatim: the
theorem quantifies over closures that are properties of `(ψ, U(n))` uniformly
in `n`).

**REPAIR (exact) — and this is a stronger result than the one deleted.**

> paper-20's theorem is about the **form** of closures: a single-time
> ψ-internal closure that holds uniformly in `n` holds on both stages. This
> unit measures the **values**, and the value-level statement is strictly
> finer: it *separates two functionals the closure theorem does not separate*.
> The inherited observable's value is `n`-constant unconditionally (`0` of
> `164,310`); the off-diagonal mass's value is `n`-constant exactly on the
> objects with no co-occupancy pair and moves elsewhere (`54,593` of
> `54,770`); the record-reading functional is never blind. Blindness is
> graded, and the grading is what the closure theorem cannot see.

### M3 — §7 names the WRONG predicate for the measured threshold, and the one it names fires a step earlier.

§7: *"the co-occupancy threshold is step 4 on both arms. It is a property of
the walk — **when its support first revisits a site along two different
links**."*

The code's predicate (`cooccupancy`, line 1142) is the **pair** predicate:
sites `x ≠ y` with `|O(x) ∩ O(y)| ≥ 2`. The prose describes the **single-site**
predicate `|O(x)| ≥ 2`. These are different, and they do not fire together. I
recomputed the frozen-arm support ladder exactly, for all six coins:

| coin | first step with `|O(x)| ≥ 2` | first step with `|O(x) ∩ O(y)| ≥ 2` |
|---|---|---|
| all 6 declared members | **3** | **4** |

So the sentence explains a step-4 threshold by an event that first occurs at
step 3. The distinction is not cosmetic: the single-site predicate is what
makes the *cell* masses record-dependent, hence what makes the **next** step's
ψ differ between arms — it is the actual mechanism of the separation ladder,
and it explains the "one step" delay §8 reports without explaining.

**REPAIR.** State both, and connect them:

> Two occupancy thresholds govern this unit, and they differ by one step. A
> site occupied on **two** links first appears at step `3`: from there the
> record moves the cell masses, so the arms' states differ from step `4` — and
> `D1` and `D2` separate at exactly `4`. A **pair** of sites sharing two
> occupied links first appears at step `4`: that is the predicate `D2`'s
> off-diagonal blindness turns on, and it is the one measured in the table
> above.

### M4 — The prediction row over-scopes: the co-occupancy threshold is not censused across the fiber.

The registered row reads *"…**for every member of the declared coin and
reading fibers**, [the ladder] …; **and the co-occupancy threshold** … is step
4 on BOTH arms."* The scope clause governs the whole sentence. But
`forcedness.rows` carries `separation_ladder` per member and **not** the
threshold; `mechanism.cooccupancy_threshold_{coupled,frozen}` are single
numbers for the delivered member (GROVER, reading A), and `cell_signature`
does not include them. §9's own statement of what each member must reproduce
("all 15 grid cells' verdict words on both arms, the separation ladder, and
every identity") confirms the omission. §10's justification — "one distinct
ladder across seven members" — carries only the ladder.

I supplied the missing evidence for the frozen arm: **the threshold is 4 for
all six coins, 6/6** (table in M3). The **coupled** arm across the fiber
remains uncensused. I also found that the *stronger* form of the claim is
**false**: the co-occupancy pair *count* at step 5 is coin-relative — `16` for
±Grover, `24` for `(-1+w)/3` and `(-2-w)/3`, `33` for `w/3` and `(-1-w)/3`.
Only the *threshold* is invariant.

**REPAIR.** Either (a) add `cooccupancy_threshold_{coupled,frozen}` to
`fiber_row` and to `cell_signature`, re-run, and keep the row as written; or
(b) split the row so the threshold clause carries its own, delivered-member
scope. (a) is preferable and cheap. Either way **record that the co-occupancy
*count* is coin-relative while the *threshold* is not** — that is a real
measured refinement and it sharpens the falsification conditions (below).

### M5 — §5's central table is ambiguous in the direction that inverts the reader.

`| G1-RECORD-CELL | PARTIAL, 3740 of 4080 classes | …` — `3740` is the
**failing** class count. The EXACT row in the same column labels its number
"`130` non-singleton classes", so the parallel reading of "`3740` of `4080`
classes" is a *score*, and a reader takes it as 92 % success. The truth is
92 % **failure**. I recounted every cell:

- **11 of the 28 PARTIAL cells have ZERO passing non-singleton classes** —
  they are total failures stamped PARTIAL. (All of `RES-SITE × G1`, `× G2`,
  `G3×D1`, `G3×D3`, `G4×D1`, `G4×D3`, plus `RES-BRANCH × G3 × D3`.)
- The best passing fraction anywhere in the 28 is `2 of 4` (50 %, on a
  four-class test). The three `RES-BRANCH × G1` cells pass at 8.33 %, 0.96 %
  and 0.15 %.

**REPAIR.** Label the column `failing / non-singleton classes`, publish the
passing count beside it, and add to §5 the sentence the census licenses:
*"eleven of the twenty-eight partial cells carry no partial relation at all —
every non-singleton class fails — and the verdict grammar has no word for
that, so they are stamped PARTIAL."* Consider a fourth verdict word
(`NONE`/`TOTAL-FAILURE`) for `failing == non-singleton`; the honest census is
then `2 EXACT / 17 PARTIAL / 11 NONE / 15 VACUOUS`.

### M6 — The exportable theorem: hypotheses over-strong for `D1`, and a whole blindness channel (mod 3) is missing — including a wraparound EXERCISED inside the delivered horizon.

This is the row the ledger asked me to settle: does the cancellation algebra
license *"every site-uniform unitary coin is record-blind on the site
diagonal"* as a theorem? **It licenses something stronger and simpler, and the
paper states the hypothesis wrong.** I verified the algebra by hand and then
by exact computation.

**THEOREM A (site-marginal blindness) — the exportable one.** Let the state
live on sites × fiber. Let the record-dependent step act as `U(n) = ⊕_x
U_x(n)` — **block-diagonal in the site index**, each block **unitary** on that
site's fiber. Then for every ψ and every `n`, the site marginal
`p(x) = ‖(U(n)ψ)_x‖² = ‖ψ_x‖²` is independent of `n`. Hence **every functional
of the site marginal alone** — `D1 = Σ_x p(x)²`, the Born site menu, the
emission rate `eps(x)`, any Rényi entropy or IPR of `p` — is record-blind at
that step.
**Site-uniformity is NOT a hypothesis.** Neither is the arena, the graph, the
fiber dimension, the horizon, the number of sites, nor the order of `ω`.

Measured: with **site-dependent** unitary coins (a different declared member
at each of the 9 sites) and 12 randomized foreign records, `D1` takes **1**
distinct value (`40411/177147`, the frozen step-4 value) and the whole site
marginal takes **1** distinct value, while `D2` takes **12**.

**THEOREM B (the off-diagonal reduction) — this is where site-uniformity is
needed.** If additionally `U_x(n) = G·D_x(n)` with `G` **site-uniform**
unitary and `D_x(n) = diag(ω^{n_l(x)})` unimodular diagonal in the fiber
basis, then `ρ_xy = Σ_l ω^{n_l(x) − n_l(y)} ψ(x,l) conj(ψ(y,l))`, whence:
for any pair with `|O(x) ∩ O(y)| ≤ 1` the sum has at most one term and
`|ρ_xy|` is record-independent. **Necessity of co-occupancy is therefore a
theorem, not only a measurement** — the paper's 0/54,770 confirms it rather
than establishes it, and the paper should say so.

**THEOREM C (the missing one).** `coin_apply` reads `WPOW[n % 3]`: `ω` is a
primitive **cube** root of unity, so **the record enters the dynamics only as
`n mod 3`**. Every ψ-internal functional therefore sees at most a `Z/3` shadow
of the metric. Measured, at a step-5 state, perturbing one cell:

| `n` at the cell | `D1` | `D2` | `D3` |
|---|---|---|---|
| 1 | `81857/531441` | `184192/531441` | `2654/6561` |
| 4 | `81857/531441` | `184192/531441` | `2894/6561` |
| 7 | `81857/531441` | `184192/531441` | `2974/6561` |
| 2 | `81857/531441` | `150784/531441` | `2198/6561` |

`D1` and `D2` are constant on the residue class; only the record-reading
functional sees the growth. **And the wraparound is not hypothetical: the
paper's own anchored maximum-cell ladder is `[2, 2, 3, 3, 4]`** — at the
declared horizon the metric's most-grown cell reaches `n = 4 ≡ 1 (mod 3)`,
**the welded value**. At those objects the most-grown cell of the geometry
enters the dynamics exactly as if it had never grown.

**REPAIR.** Replace §7's single hypothesis sentence with Theorems A, B and C,
each with its own hypotheses; state that A is arena-independent (which is what
grounds §7's "scope limit on the whole programme" and resolves it against the
SCOPE box, see m5); state that B makes co-occupancy-necessity a theorem; and
add the sentence C licenses:

> The record the machine **writes** is unbounded; the record the coin
> **reads** is `Z/3`. The wraparound is reached inside the horizon this unit
> ran.

### M7 — The choice inventory omits the single most verdict-determining choice.

The bar is applied to **EXACT cells only** (`exclusion.exact_cells_tested =
2`). That is a choice, it is the choice that decides the head, and it is not
one of the eleven items. It is also the correct choice under the pin's letter
(a relation that does not *hold* cannot *hold identically frozen*) — which is
precisely why it must be declared rather than assumed: its consequence is that
**the 28 PARTIAL cells' gravitational status is decided by no gate at all**,
and the frozen control cannot decide it either, being a degenerate 5-object
one-class grid.

**REPAIR.** Add as item 12: `F12-BAR-SCOPE` — **DECLARED**, fiber 1, "the
frozen bar is applied to EXACT cells only; partial cells are not adjudicated
gravitational, and the control is structurally unable to adjudicate them."
Add the same as an explicit sentence in §6. Two further items are missing and
should be added: `F13-COOCCUPANCY-PREDICATE` (pairs sharing ≥ 2 occupied
links, evaluated on the pre-coin ψ) and `F14-DOMINATION-TEST` (per-step
value-set comparison; COUPLED-DOMINATES iff coupled > frozen at every
separating step).

---

## 3. MINOR findings

- **m1.** §7 and claim `C8`: *"at not one **pair** whose occupied-link sets
  meet in at most one link."* The measurement is per **object**
  (`moved_without_a_cooccupancy_pair` counts objects with `cooc == 0`), and
  the verdict head says `OBJECT` correctly. Repair the prose to match the
  head: *"at not one object no two of whose sites share two occupied links."*
- **m2.** `54,770` is published in the head and §7 but is carried by no
  receipt key (derivable as `5 × 10,954`; the receipt carries `32,862` per
  field and `164,310` in total). Add `mechanism.object_field_pairs = 54770`.
  This is the only paper integer of 313 that my sweep could not locate
  literally in the receipt bytes.
- **m3.** The `9,751 → 5` collapse is presented as "a measurement this unit
  adds". The raw count is; the collapse to exactly one object per level is
  **forced** by the frozen update semantics (constant record + deterministic
  unitary ⇒ unique `(t, ψ, n)`). The unit already carries the evidence:
  across the fiber the frozen **raw** count varies (`9751`, `10237`, `12181`)
  while the **distinct** count is `5` at all seven members. Cite it and stamp
  the collapse `DEFINITIONAL-THROUGH-THE-FROZEN-SEMANTICS`.
- **m4.** §11's walls are clean under my independent scan: three mentions of
  Diósi–Penrose, all shape-only; no SI unit, no experimental value, no
  physical rate anywhere in the paper; the three declared-out needles
  (`horizon`, `rate`, `mass`) are correctly declared with reasons. **Wall row
  passes.**
- **m5.** The SCOPE box ("licenses nothing about any other arena") and §7
  ("a scope limit on the whole programme, not on this arena alone") are in
  tension. Theorem A resolves it: the *measurements* are arena-bound, the
  *blindness theorem* is not. Say exactly that.
- **m6.** `RES-STEP`'s 15/15 VACUOUS stamp is honest and correctly reasoned;
  I confirm 5 objects, 5 distinct growth values, no non-singleton class. The
  `EXACT`-with-no-non-singleton-class gate exists and passes. No finding.

---

## 4. THE LICENSED CLAIM

Everything below is what this unit may say after the repairs. Each is checked
against the receipt and, where marked, against my own recomputation.

1. **The head.** `GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR`. Zero D = f(G)
   relations survive the pin's frozen bar; the 28 partial cells are not
   adjudicated by any gate; what survives is between-arm.
2. **The zero is forced, not contingent.** The only exact cell relates two
   functions of the site marginal, and the site marginal is record-blind by
   Theorem A; the identity could not have failed on the frozen stage. The
   genuine record functionals `G1`–`G4` yield no exact cell at any resolution.
   *This is the sentence §6 should end on, and it is stronger than the one
   there now.*
3. **The exportable theorem** (Theorem A above), with its true hypotheses:
   *block-diagonal in the site index, unitary on each block*. Arena-free,
   horizon-free, dimension-free. **This is the unit's exportable result**, and
   it is the strongest thing in the paper.
4. **Blindness is graded, and the grading is new** (M2's repair): `D1`
   unconditional; `D2` exactly off co-occupancy; `D3` never. paper-20's
   staleness theorem separates none of them — the value-level statement is
   strictly finer than the closure-level one. That is the honest
   staleness-quantitative-twin framing.
5. **"The record the machine writes is unbounded; the record the coin reads is
   `Z/3`,"** with the wraparound reached at the delivered horizon
   (`max cell count = 4 ≡ 1`). *Licensed and measured.*
6. **"A frozen stage is one quantum history with a classical ledger written
   beside it."** Licensed — `9,751 → 5` — with the stamp of m3 and the 7/7
   fiber evidence. Keep the sentence; it is the best in the paper.
7. **The domination failure's horizon lesson.** Licensed and important:
   *"A monotone claim would have been available at horizon 4 and is false at
   horizon 5."* I verified the frozen witnesses. Strengthen it with the part
   the paper leaves implicit — **`D1`'s surviving domination is itself tested
   at only two steps, and the two functionals that fail teach exactly that a
   two-step monotone claim can break at the next horizon.** So `D1
   COUPLED-DOMINATES` must be published as HORIZON-LOCAL, never as a law.
8. **Not licensed:** "the two ψ-internal values are blind"; "the
   `GDL-DECOUPLED` outcome was available"; the threshold's mechanism sentence
   as written; the prediction row's fiber scope over the threshold; "PARTIAL"
   as a headline word.

### The prediction row — registration form

**Register as `GDL-PRED-1`, stamped `FORCED-AT-THIS-ARENA` — correctly
stamped, and it must stay stamped.** The delivered row conflates two claims of
different standing; register them separately.

> **`GDL-PRED-1a` (the separation ladder). FORCED-AT-THIS-ARENA.** At the GDL
> arena, at the declared horizon 5, and for **every one of the 7 executed
> members** of the declared coin and reading axes, the record-reading
> decoherence functional separates the coupled stage from the frozen control
> at step **3**, exactly one step before either state-internal functional,
> which separate at step **4**. Evidence: 1 distinct ladder across 7 members,
> `forcedness.rows`, digest `da4248b1a55b`.
> **Falsified by:** any fiber member (any coin, any declared reading) whose
> ladder is not `(D3, D1, D2) = (3, 4, 4)`; any run at the same arena and
> horizon in which the ladder moves. **Not falsified by:** a change of arena,
> of horizon, of the observable set, or of the fiber shape — those are outside
> the stamp and licence nothing against it.
> **Mechanism, and therefore the shape of a refutation** (from M3/M6): the
> ladder is not a coincidence. `D3` separates when the *records* differ;
> `D1`/`D2` separate one step after a site is first occupied on two links
> (step 3), because that is when the record first moves the cell masses. A
> refutation should therefore attack the support geometry, not the coin.

> **`GDL-PRED-1b` (the co-occupancy threshold). DELIVERED-MEMBER-ONLY until
> M4 is repaired.** The pair co-occupancy threshold governing `D2`'s
> off-diagonal blindness is step **4 on both arms**. Evidence for the frozen
> arm across all 6 coins is supplied in this review (6/6); the coupled arm
> across the fiber is **uncensused**. **Falsified by:** any member whose
> threshold is not 4. **Already known to fail in its stronger form:** the
> co-occupancy *count* at step 5 is coin-relative (`16 / 24 / 33`) — so the
> prediction is about the threshold only, and must say so.

Units are substrate-native (step indices and object counts); the DP arc stays
shape-only. Both rows are `SUBSTRATE-NATIVE`, carry no SI quantity, and make
no experimental claim. **Registration approved for 1a as written; 1b subject
to M4.**

---

## 5. SUCCESSOR REGISTER

### `GDL-2` — THE METRIC-CONSUMING COIN. *Recommended wave slot: a Wave-A addendum, launched after `SIG`, not before it.*

This is the unit where a gravitational-decoherence law could still live, and
this review can now specify it precisely rather than gesture at it. §13's
three routes are right but incomplete and unsized; here they are sized.

**What the coin consumes, and the functional form to price.** The inherited
consumption is `D_x(n) = diag(ζ^{n_l(x)})` with `ζ` a primitive **3rd** root
of unity — an unbounded record read through a `Z/3` window. The declared fiber
`GDL-2` must run is the **order `m` of the record phase**: `ζ = ζ_m`,
`m ∈ {3, 4, 6, 9, 12, …}`, exact in `Z[ζ_m]`. Then:

- **Raising `m` removes the wraparound** (Theorem C) — and `m` must exceed the
  maximum cell count at the horizon, which the anchored ladder puts at `4` for
  `T = 5`; so `m ≥ 5` is the first honest choice, `m = 6` the first that keeps
  a small cyclotomic ring.
- **Raising `m` does NOTHING for `D1`.** Theorem A is independent of `m`, of
  `ζ`, and of site-uniformity. **A metric-consuming coin cannot rescue the
  inherited observable at any `m`.** This is the register's hardest entry.
- **Hence the exact price list.** A site-marginal decoherence functional can
  become record-sensitive only by breaking a hypothesis of Theorem A: either
  (i) **break block-diagonality** — a step that moves amplitude between sites
  before the menu is read — which is the same property paper-20's law
  transport consumes, so **GDL-2 on route (i) cannot be run without re-gating
  paper-20's transport**, and that dependency should be written into the pin;
  or (ii) **break unitarity of the site block**, which dismantles the machine.
  There is no third route to `D1`.
- **A tension worth a result of its own.** Any *exactly computable* unimodular
  record consumption of finite order is `m`-periodic; unbounded record
  sensitivity in a ψ-internal functional therefore requires leaving the
  cyclotomic ring (losing exact arithmetic) or leaving unitarity. **Exactness
  and unbounded metric-sensitivity are in tension at this substrate.** That is
  a publishable no-go shape and `GDL-2` should be pinned to decide it.
- **The cheap route stays open and is the one to run first:** keep the
  machine, change the observable — a **two-time** functional (a decoherence
  *rate* between consecutive menus rather than a *value* at one), which
  Theorem A does not touch because it is not a functional of a single site
  marginal. §13 item 1 is correct and is the lowest-cost successor.

**Pre-registered outcome grammar for `GDL-2`** (and this time with a
reachability gate per M1): `GDL2-LAW-FORCED` / `GDL2-LAW-m-RELATIVE` /
`GDL2-DECOUPLED-AT-THE-GRAVITATIONAL-BAR` / `GDL2-BLOCKED-AT-<object>`. The
frozen bar is inherited verbatim, **and its scope is declared** (M7).

### What `SIG` inherits — and this constrains `SIG`'s observable choices

**Theorem A is a constraint on `SIG` before `SIG` chooses anything.** Any
observable `SIG` declares that is a function of the site marginal alone — the
Born site menu, its IPR, its entropy, the emission rate profile — is
**record-blind by theorem at every arena of this class**, not just here. `SIG`
must therefore either (a) declare observables that read off-diagonal structure
(and inherit the co-occupancy gating, hence a step-4 floor at this arena), or
(b) declare observables that read the record directly (and inherit `D3`'s
graded, censused, partial dependence), or (c) declare two-time observables.
**`SIG` should carry Theorem A as an inherited constraint in its pin**, and
should not spend a fiber on site-marginal observables. Route (b) additionally
inherits Theorem C: a record-reading observable is the *only* kind that sees
`n` rather than `n mod 3`.

### What the ladder hands `PER-R`

- The **mechanism** of the ladder, not just its values: `D3` separates when
  the records differ; the ψ-internal functionals separate **one step after the
  first double-occupied site**. `PER-R` inherits a *delay law*, not a table.
- The **falsification shape**: attack the support geometry, not the coin — the
  ladder is coin-invariant across 7 members, and I confirmed the underlying
  occupancy thresholds are coin-invariant across all 6 coins on the frozen
  arm.
- The **negative half**: the co-occupancy *count* is coin-relative
  (`16 / 24 / 33` at step 5). `PER-R` should not build on counts.
- The **horizon caution**: `D2` and `D3`'s dominations reverse between step 4
  and step 5. Any `PER-R` claim that is monotone in the step index must be
  re-taken at the next horizon before it is published.

### Register rows for the era

| row | content | owner |
|---|---|---|
| `GDL-2` | the metric-consuming coin; the `m`-fiber; the exactness/sensitivity tension; route (i) re-gates paper-20's transport | Wave-A addendum, after `SIG` |
| `GDL-1a` | the two-time decoherence *rate* functional — the lowest-cost successor, untouched by Theorem A | may precede `GDL-2` |
| `SIG` | inherits Theorem A as a pin constraint on its observable declarations | `SIG` pin |
| `PER-R` | inherits the delay law and the horizon caution; not the counts | `PER-R` pin |
| instrument | `G-OUTCOME-REACHABILITY` — every arm of a declared outcome grammar must carry a reachability witness or be declared dead | RUNBOOK |
| instrument | verdict grammars need a word for `failing == non-singleton` (total failure), or `PARTIAL` will keep absorbing it | RUNBOOK |

---

*K2 EFFECTUS-LENS, v14 ledger #222. 243 recomputations. Object hashes
re-verified unchanged at close.*
