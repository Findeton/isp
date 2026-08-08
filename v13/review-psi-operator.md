# PSI — HOSTILE REVIEW R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator/algebraic lens.  **Date:** 2026-08-08.
**Protocol:** `v13/note-psi-hostile-protocol.md` (frozen, v13 #251), kill-shots
K1–K5.  Repo read-only; no git; no child agents; all recomputation from my own
code in the session scratchpad; nothing imported from the unit.

## 0. Object verification (SHA-256, first 12)

| file | required | measured | |
|---|---|---|---|
| `v13/paper-psi-curvature.md` | `e79d0ff48933` | `e79d0ff48933` | match |
| `v13/code/psi_curvature_exact.py` | `49b3c980e7d8` | `49b3c980e7d8` | match |
| `v13/code/psi_curvature_output.txt` | `8ea66d096ec8` | `8ea66d096ec8` | match |
| `v13/code/psi_curvature_receipt.json` | `443cf2460dba` | `443cf2460dba` | match |

All four match; the review proceeds against the frozen object.

## 1. Method and recomputation count

I rebuilt base G from the published prose of `paper-gen-generality-check.md`
§§2–8 and `paper-psi-curvature.md` §§2–6 in an independent module
(`r1_core.py`, 12 driver scripts), exact `fractions.Fraction` throughout,
importing nothing from `psi_curvature_exact.py`: my own Euler–Rodrigues
constructor, my own local legs, my own 162-element scope generator, my own
Householder/completion, my own four-clause admission predicate, my own graph,
my own reduced-walk enumeration, my own holonomy accumulation.

**Recomputation count: ≈1,450 distinct claimed quantities independently
recomputed**, plus **2,184 loop holonomies rebuilt twice** (364 loops × 3
members × 2 routes: an accumulating DFS and a plain left-to-right product with
no shared accumulator).

**No claimed number in the paper, the output or the receipt was found to be
wrong.** Every headline reproduced exactly. What follows attacks the
sentences, the scopes and the gates.

### 1.1 The independent numbers table (mine vs claimed)

| quantity | claimed | mine |
|---|---|---|
| $R_0,R_1,R_2$ from the quaternions vs the pinned matrices | equal | equal, 27/27 entries |
| $V(\psi_G)=H Q$ vs GEN's pinned $9\times9$ | equal | equal, 81/81 entries; orthogonal |
| declared scope / closure / admitted | 162 / 26,244 / 2 | 162 / 26,244 with 0 outside / 2 = $\{1,W\}$ |
| declared extension / admitted | 216 / 8 | 216 / 8 |
| family: members / invariant / non-inv / Born-symmetric / distinct | 11 / 7 / 4 / 9 / 11 | identical |
| Schmidt ranks among the invariant members | $\{1,2,3\}$ | $\{1,2,3\}$ |
| §2.3 per-member rank, support, invariance, Born symmetry | as printed | 11/11 rows reproduced |
| admission draws, 9 members / `psi-N3`,`N4` | 18 / 8 and 18 / 0 | identical, at all 48 cells |
| admission cells that move vs the reference | 0 (8 members), 8 (`N3`,`N4`) | identical; the 8 are exactly REAL at $t\in\{0,1,2,3\}$ at GP-E and GP-F |
| links per setting | (9,9,9,9,13,13) / (9,…,9) | identical |
| reduced paths / closed paths / based loops | 34,024 / 5,864 / 760 and 2,532 / 336 / 48 | identical |
| based loops at GP-E and GP-F: nine members / `psi-N3`,`N4` | 364 / 8 | identical |
| `psi-N1`: common / Born-differ / perm-differ / flat→non-flat | 364 / 206 / 206 / 2 | 364 / **206** / 206 / **2**, at GP-E *and* GP-F |
| `psi-N2`: Born-differ | 196 | **196**, at GP-E and GP-F |
| the shortest differing loop | length 4, `(id,0,FULL)⁻¹ (leg,F2,1) (id,1,REAL) (leg,F1,1)⁻¹` | identical |
| the flat→non-flat witness | the doubled realized prep bigon, length 8 | identical; **exactly 2 such loops**, the two traversal directions of that bigon |
| positive control: group order per setting | 1,1,1,1,4,4 | identical |
| value set at GP-E: size, closure, abelian, orders | 4, closed, abelian, $\{1,2\}$ | identical |
| fixed configurations of the four elements | $\{9,9,45,81\}$ | identical |
| the defect: order, fixed configurations, group member | 2, 45, yes | identical |
| $\psi$-law $=$ direct $81\times81$, entry by entry | at all 11 | **11/11** |
| $E(\psi)=I \iff$ invariant $\iff D=D_{\text{GEN}}$ | coincide | all three lists coincide, both directions |
| sign-flip census: patterns / move / agree / mismatches | 48 / 26 / 22 / 0 | **48 / 26 / 22 / 0**; per member 8,8,2,4,16,8,2 |
| Q-negA: $\operatorname{ord}\delta$, order, abelian, links, loops | 3, 6, no, 13, 364 | identical |
| Q-negB: $\operatorname{ord}\delta$, order, abelian, links, loops | 1, 1, yes, 11, 52 | identical |
| switching self-test arithmetic | 66,560 / 65,544 / 8 | $2\cdot4\cdot(8192{+}128)$, $8+2\cdot4\cdot8192$, $2\cdot4$ — all consistent |
| anchors | 146 = 109 + 37 | 146 rows, 109 self / 37 external, all passed |
| float literals / `float()` calls / gate ids / call sites | 0 / 0 / 21 / 37 | 0 / 0 / 21 / 37 (my own AST sweep) |

Two further checks the unit does not make, both clean:

- **The "flat" reading is sound.** All **82** loops whose permutation part is
  the identity at $\psi_G$ have holonomy matrix exactly $\pm I$ — a global
  scalar — so reading flatness off the permutation part drops nothing here.
- **Nothing is silently dropped from the 206.** The Born shadow is defined on
  every one of the 364 rows; the 206 count is taken over the full common set
  with no filter.

---

## 2. Findings

### F1 [MAJOR] §6.2's census mechanism is false off GP-E, and 8 of the unit's own 48 patterns are the counterexample

**Claim under attack (§6.2, and the same wording in the `PSI-SIGNFLIP-CENSUS`
gate):**

> Three things are measured at every one of the 48. The **Born shadow** is
> unchanged by a sign pattern, so no Born-level declaration can see the flip.
> The **loop space** is unchanged, so every loop is common and the comparison
> is total.

The inference in the first sentence — the predicate reads Born-level data
only, *therefore* two preparations with the same Born shadow present the same
Born-level data — does not hold, and the unit's own census sub-family refutes
it. The node law at checkpoint $t\ge 2$ is **not** a function of
$\lvert\psi\rvert$: it is
$\bigl\lvert U_X(g)\,(\psi\otimes e_0)\bigr\rvert^2$, and a local leg
superposes distinct support entries of $\psi$ unless it happens to be a
permutation matrix.

**Measured, on my instrument, over the unit's own 48 census patterns:**

| | count of the 48 |
|---|---|
| patterns that move a **node law** at some setting | **21** |
| patterns that move an **admission cell** at some setting | **8** |

All 8 move exactly the cells `(GP-F, t=2, REAL)` and `(GP-F, t=3, REAL)` — so
at GP-F their **loop space is not the reference's**, and "every loop is
common" is false there. Explicit counterexample: `psi-I4` with the sign
flipped at $\lvert 1,0\rangle$ alone (a census member: `psi-I4`'s support does
not contain $e_{(0,0)}$, so all 16 of its patterns are swept). It has the same
$\lvert\psi\rvert$ and the same $\lvert V\rvert$ entry by entry as `psi-I4`,
and different node laws at (GP-C, F1, $t{=}2$), (GP-C, F1, $t{=}3$), (GP-C,
F2, $t{=}3$) and the same three at GP-F.

**Why the census's own numbers survive:** the census rebuilds only at GP-E,
where both local legs come from $R_0$ and *are* permutation matrices, so
entrywise absolute values are preserved through every checkpoint. I reproduce
26 / 22 / 0 exactly. **No delivered number moves.** What is wrong is the
stated mechanism and an unscoped sentence.

**Repair (replacement text for §6.2, verbatim):**

> Three things are measured at every one of the 48, at the declared setting
> GP-E. The **Born shadow** of $\psi$ and of $V$ is unchanged by a sign
> pattern — by algebra, since $V(\varepsilon\psi)=S\,H\,S\,Q$ with
> $S=\operatorname{diag}(\varepsilon)$, and left or right multiplication by a
> diagonal $\pm1$ and a column permutation preserve entrywise absolute
> values. At GP-E both local legs are permutation matrices, so every
> downstream Born-level datum — the occupied sets, the node laws at all four
> checkpoints, the Born key of every declared and realized leg — is likewise
> unchanged, and the **loop space** is therefore identical and every loop is
> common. Both of these are consequences of the declaration rather than
> contingent measurements, and they are recorded as such. Off GP-E the first
> does not follow: a local leg that is not a permutation superposes distinct
> support entries of $\psi$, and 21 of the 48 patterns move a node law at some
> setting while 8 of them move two admission cells at GP-F. The census's
> reading is a GP-E reading and is stated at that scope. The one contingent
> measurement is the third: the **holonomy** agrees with the reference on
> every common loop **if and only if** the flipped state is still
> exchange-invariant.

The same qualifier is needed in the `PSI-SIGNFLIP-CENSUS` gate claim string.

### F2 [MAJOR] The verdict is not gated as §13-addendum #234 requires; a branch-order swap emits a false verdict with a clean receipt

`PSI-VERDICT` is listed by the unit itself as falsified **only by a waiver**,
which the protocol flags as a mandatory decision point. Reading the code
settles it against the unit:

```
    if curvature:  v = "PSI-CURVATURE-EXISTS"
    elif path_space: v = "PSI-PATH-SPACE-DEPENDENCE"
    else: v = "PSI-DECLARATION-ONLY"
    ...
    qual = "-AT-FIXED-BORN-SHADOW"
    full = v + qual
    inv  = v in PREREGISTERED
    gate("PSI-VERDICT", ..., inv, {...})
```

Three defects:

1. **The gate predicate is `inv` alone** — membership in the pre-registered
   vocabulary. It does not compare the emitted string with anything re-derived
   from the measurements.
2. **The derivation is outside the gate.** §9 says "The verdict string is
   re-derived inside its own gate from the recorded measurements and measured
   to be the string the rule selects." No re-derivation occurs inside the
   gate; `v` is computed once, above it.
3. **The qualifier is typed, not derived.** `-AT-FIXED-BORN-SHADOW` is a
   literal appended unconditionally. Nothing measures that the witness
   actually sits at a fixed Born shadow before that qualifier is printed —
   even though the unit *has* that measurement (`the_born_shadow_of_the_
   completion_agrees`, `the_born_level_keys_of_every_leg_agree`).

Both `curvature` and `path_space` are True in this run, so the rule's branch
**order** is load-bearing and is exactly what #234 says a mutant must be able
to break. `verdict-lax` does not test it — it overwrites the string after the
derivation, which only exercises clause (1).

**Demonstration, run.** I copied the frozen instrument into the scratchpad
(byte-identical, sha `49b3c980e7d8…`), swapped the two branches of the
decision rule and nothing else — a computation perturbation, no gate
predicate touched — and called `run_verdict` on both copies with this run's
own measured inputs (2 witness pairs; movers `psi-N3`, `psi-N4`; curv
`psi-N1`, `psi-N2`):

| copy | verdict emitted | `PSI-VERDICT` |
|---|---|---|
| frozen | `PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW` | **PASS** |
| branch-swapped | `PSI-PATH-SPACE-DEPENDENCE-AT-FIXED-BORN-SHADOW` | **PASS** |

I then ran the swapped copy **end to end**. It finished
`146 anchors, 20 gates, 0 must-pass failures`, **exit code 0**, 20 `[PASS]`
and 0 `[FAIL]`, and printed as its headline:

```
VERDICT: PSI-PATH-SPACE-DEPENDENCE-AT-FIXED-BORN-SHADOW
```

The swapped verdict is **false by the pin's own vocabulary** — the outcome
named `PSI-PATH-SPACE-DEPENDENCE` requires every common loop's holonomy to be
$\psi$-invariant, which this run refutes on 206 loops. The gate passes anyway;
its claim string still reads "The verdict string is re-derived inside this
gate from the recorded measurements and measured to be the string the rule
selects"; and its own printed value carries the refutation two fields away
from the wrong verdict:

```
value: {a_common_loop_differs:True, ... ,
        verdict:PSI-PATH-SPACE-DEPENDENCE-AT-FIXED-BORN-SHADOW}
```

An ungated verdict is, in the runbook's words, a typo away from fiction. Here
it is a two-line edit away, and the resulting receipt is indistinguishable in
form from the delivered one.

**Repair.** (a) Re-derive the full string inside the gate from the recorded
table values and gate `emitted == re-derived`. (b) Derive the qualifier:
`qual = "-AT-FIXED-BORN-SHADOW" if <the witness member shares the reference's
Born shadow of psi, of V, of every leg key and of every node law> else ""`,
with those four booleans read from `TABLES["flip_tests"]`. (c) Add a
**computation** mutant `verdict-order` that swaps the branch order, and a
second `verdict-qualifier` that forces the qualifier on; both must die at
`PSI-VERDICT`. (d) Amend §11's list of waiver-only gates accordingly. Until
(a)–(c) are done, §9's sentence must be replaced by: "The verdict string is
selected by the pre-registered decision rule from the recorded measurements;
the gate measures that the string lies in the pre-registered vocabulary."

### F3 [MAJOR] Only one of the two reported witness pairs is at a fixed Born shadow — and the family contains a second one the unit never forms

§10.3: "The existence claim the verdict makes needs one witness and has two."
The receipt reports `witness_pairs: 2` — `(psi-G, psi-N1)` and
`(psi-G, psi-N2)`. But the verdict is qualified `-AT-FIXED-BORN-SHADOW`, and
**`psi-N2` does not share `psi-G`'s Born shadow**: measured on my instrument,
$\lvert\psi_{N2}\rvert \neq \lvert\psi_{G}\rvert$ and
$\lvert V_{N2}\rvert \neq \lvert V_{G}\rvert$ entrywise. At the verdict's own
scope the unit has **one** witness pair, not two. The receipt's witness table
does not record which pairs are at a fixed Born shadow, so a reader takes both
as qualifying.

**This is repairable in a way that strengthens the paper, using no new
member.** The pair `(psi-I4, psi-N2)` *is* at a fixed Born shadow. Measured:

| clause | `psi-I4` vs `psi-N2` |
|---|---|
| $\lvert\psi\rvert$ entrywise | equal |
| $\lvert V\rvert$ entrywise | equal |
| Born key of every declared leg, every (setting, frame) | equal |
| Born key of every realized leg, every (setting, frame) | equal |
| node law at every node of every setting | equal |
| admission table, all 48 cells | equal |
| based loops at GP-E / GP-F | 364 / 364, all common |
| **common loops whose Born holonomy differs** | **196** at GP-E and **196** at GP-F |
| $\langle\psi_{I4}\mid\psi_{N2}\rangle$ | **0** |

So the family carries a second fixed-Born-shadow witness pair, at Schmidt rank
2 rather than 3, on a different support, and between two states that are
**orthogonal** — a sharper illustration than the reference pair, whose overlap
is $1/9$. The paper's abstract is already correct ("indistinguishable *from
the reference*"); what needs fixing is §10.3 and the receipt's witness table.

**Replacement for §10.3's clause, verbatim:**

> The existence claim the verdict makes needs one witness at a fixed Born
> shadow and has two pairs: $(\psi_G,\psi_{N1})$, differing on 206 of 364
> common loops, and $(\psi_{I4},\psi_{N2})$, differing on 196 — the second
> between two states that are orthogonal and yet identical in every
> Born-level object the model builds. The pair $(\psi_G,\psi_{N2})$ is a
> witness for the existence claim but not at a fixed Born shadow, since
> $\psi_{N2}$ and $\psi_G$ have different Born shadows, and it is not counted
> at the verdict's qualified scope.

### F4 [MAJOR] §6.1 asserts a false fact about the paper's own new object

> $E(\psi)$ is a symmetric orthogonal involution, and conjugating $\Sigma$ by
> a Householder generically leaves the signed-permutation class.

$E(\psi)=\Sigma H\Sigma H$ satisfies $E^{\mathsf T}=H\Sigma H\Sigma=E^{-1}$,
so it is orthogonal — always. It is **not** symmetric and **not** an
involution off the invariant locus, and symmetry and involutivity are the same
condition here ($E=E^{\mathsf T}=E^{-1}\iff E^2=I$). Measured at the four
non-invariant members:

| member | $E$ symmetric | $E^2=I$ |
|---|---|---|
| `psi-N1` | **no** | **no** (no order $\le 400$) |
| `psi-N2` | yes | yes |
| `psi-N3` | **no** | **no** |
| `psi-N4` | **no** | **no** |

I print $E(\psi_{N1})$ exactly: its $(1,3)$ entry is $80/81$, its $(0,0)$
entry is $-7/9$, it is not symmetric, and $E^2\neq I$ with no order at or
below 400. The symmetric orthogonal involution in this
construction is $H(\psi)$, not $E(\psi)$ — the sentence reads as `H` mistyped
as `E`. It is not load-bearing (no gate or number uses it; the code and the
receipt do not repeat it), but it is a false mathematical statement inside the
paper's own theorem section about its own central new object.

**Replacement, verbatim:** "$H(\psi)$ is a symmetric orthogonal involution and
$E(\psi)=\Sigma H\Sigma H$ is orthogonal with $E^{\mathsf T}=E^{-1}$, but
$E(\psi)$ is itself an involution only where it is the identity together with
`psi-N2`; conjugating $\Sigma$ by a Householder generically leaves the
signed-permutation class."

### F5 [MAJOR, scoping] "Born-level indistinguishable" is never scoped to the declared basis, and the two states are nearly orthogonal

K1's explicit requirement. The paper's strongest formulations are scoped to
the model — abstract: "indistinguishable from the reference by every Born-level
object **the model contains**"; §9: "invisible to every Born-level declaration
**the model contains**"; §10.9 defines "Born shadow" as entrywise squares of
declared vectors. But §5.2's own note paragraph says, unqualified,
"`psi-S1` and `psi-N1` are Born-level indistinguishable from the reference"
and "**They differ only in a sign**", and the word *basis* occurs in the paper
only to name the declared basis states and fix their ordering (§2.2, §2.3),
never to scope a claim. Nowhere does the paper say that the reading is
basis-relative and that in full quantum mechanics the sign structure is
measurable in other bases.

It is measurably not a small difference:
$\langle\psi_G\mid\psi_{N1}\rangle = 1/9$, so a projective measurement onto
$\psi_G$ separates the two states in one shot with probability $80/81$.
Meanwhile $\langle\psi_G\mid\psi_{N3}\rangle = 14/15$ — `psi-N3` is far
*closer* to the reference than the witness is, and it is `psi-N3` that
collapses the arena. "Differ only in a sign" invites exactly the wrong reading.

**Replacement sentence for §5.2, verbatim:**

> They differ in one sign of one coefficient in the declared basis, and that
> is the whole of the difference the model's Born-level objects can see. It is
> not a small difference between the states: $\langle\psi_G\mid\psi_{N1}
> \rangle = 1/9$, so a projective measurement in another basis separates them
> in a single shot with probability $80/81$. "Born-level indistinguishable"
> here means indistinguishable by the entrywise squares in **this declared
> basis**, which is the only Born-level datum any declaration of this model
> reads; it is not a claim that the two preparations are operationally
> indistinguishable in quantum mechanics, and no such claim is made anywhere
> in this paper.

An added non-claim in §10 should say the same in one line.

### F6 [MINOR] The negative control is presented as a prediction test, but both of its transpositions lie inside GEN's exhaustively rebuilt sub-family — and the free external anchors were not taken

§7.2: "The pin requires that a **declaration** change move the holonomy, and
that the amount be **predicted rather than observed**." Both alternative
transpositions are single transpositions of the nine system-pair labels fixing
the first, i.e. members of GEN §8.4's 28-member sub-family, **every one of
which GEN rebuilt in full**. GEN's committed receipt — the very file PSI
hash-pins — records them per member:

| GEN `completion_rebuilds.per_member` | measured order at GP-E | abelian | $\operatorname{ord}\delta$ | id links |
|---|---|---|---|---|
| `Q = (1 4)` (= PSI's `Q-negA`) | 6 | false | 3 | 7 |
| `Q = (1 3)` (= PSI's `Q-negB`) | 1 | true | 1 | 5 |

PSI measures 6 / non-abelian / 13 links and 1 / abelian / 11 links — the same
values (13 = 6 leg links + 7; 11 = 6 + 5). So the control is a *reproduction
of a committed measurement* as well as a check of the law, and none of PSI's
37 external anchors covers it. The paper leans on external anchoring to make
the positive control "a reproduction rather than a rebuild"; the identical
argument was available here and was not used.

**Repair:** add two external anchors against
`gen_generality_receipt.json → tables.completion_rebuilds.per_member["Q = (1 4)"]`
and `["Q = (1 3)"]` (group order, abelianness, defect order, identification
links), and replace §7.2's opening with: "The pin requires that a declaration
change move the holonomy by an amount fixed in advance. Both alternative
transpositions lie inside the completion sub-family GEN rebuilt exhaustively,
so their group orders are committed values and are anchored exit-1 here as
well as predicted by the dihedral law — the control is at once a prediction
test and a reproduction."

### F7 [MINOR] Cell-completeness is printed but ungated (#234)

`cells_per_member: 48` is a printed value. The `PSI-ADMISSION-PER-PSI`
predicate is
`both and len({draws[nm]["REAL"] …}) > 1 and all(v["n_admitted"] <= 1 or not
v["drawn"] …)` — it never compares `cells` to
`len(SETTING_ORDER)*len(CHECKPOINTS)*len(ID_RULES)`, and no mutant drops a
cell. Because `admtab` is built by a comprehension over the declared lists, a
dropped cell disappears from *every* member's table and from the delta
comparison in `run_comparison` (which iterates
`sorted(admtab[PSI_REFERENCE])`), so it would be invisible everywhere.
§13-addendum #234: "a cell-completeness gate must catch a dropped cell."
**Repair:** gate
`cells == len(SETTING_ORDER)*len(CHECKPOINTS)*len(ID_RULES)` and add a
`cell-drop` computation mutant.

### F8 [MINOR] The "permutation part" column of §5.2 is not a second reading

Measured: at `psi-N1`, of the 364 common loops **158** are readable at both
members, and the number of those whose permutation part differs is **0**. All
206 "permutation part differs" rows are precisely the 206 readability flips —
the same set, three times over (`common_loops_whose_born_holonomy_differs`,
`…_permutation_part_differs`, `…_where_readability_flips` are all 206 at GP-E
and GP-F; the same holds at 196 for `psi-N2`). §1 advertises "the holonomy is
read twice, and both readings are gauge-invariant" and §5.2's table prints two
columns; D7 and §10.5 disclose the underlying fact, but the table itself reads
as corroboration by a second instrument when it is not.
**Repair:** in §5.2, add a footnote row or a sentence: "The permutation-part
column is not an independent reading here: every one of these rows is a row
where the permutation part is undefined at the second member, and the count of
common loops whose permutation parts are both defined and different is zero."

### F9 [NOTE] The witness's "independent route" is independent of the accumulation only

`loop_matrix_fresh(..., memoised=False)` shares `W.link_variable` and `mm`
with `enumerate_paths`; what it does not share is the interning, the step memo
and the value cache — which is exactly what §11 and the gate claim say, so the
text is accurate. But §14-addendum (#219) asks for a comparator built
independently of the audited component, and the link variables are the
audited component's own inputs. My fully independent rebuild (separate module,
separate multiply, separate constructors) agrees on all 2,184 holonomies, so
nothing is at risk; the disclosure should nevertheless say which layer the
independence covers.

### F10 [NOTE] Two silent-drop paths in the self-test and the flip-test

`named_edges` returns `None` when a declared probe's links are absent, and
both `run_switching_selftest` and `run_flip_tests` then `continue`. Nothing
gates that all `len(SWEEP_MEMBERS) * len(DECLARED_PROBES) = 8` (member, probe)
pairs were realized: `complete` is `bool(rows) and all(...)`, and
`cache_entries_primed: 8` is reported but never compared with $2\times4$. A
probe that silently vanished would shrink the sweep and pass. **Repair:** gate
`primed == len(SWEEP_MEMBERS)*len(DECLARED_PROBES)` and
`len(rows) == primed`, and gate `flips == primed` in the flip-test.

### F11 [NOTE] `flat_to_non_flat_witnesses: 1` in the receipt vs "2" in the paper

The receipt's `PSI-WITNESS` value reports `flat_to_non_flat_witnesses: 1`; the
paper's §5.2 table and §5.3 report **2**. Both are right and they count
different objects — the receipt counts extracted (member, setting) witness
*records* and `break`s after the first setting; the paper counts *loops* at
GP-E. The per-setting table does carry `2` at GP-E and at GP-F. A reader
collating the two documents sees a contradiction that is not one.
**Repair:** rename the receipt key to
`flat_to_non_flat_witness_records_one_per_member` and add
`flat_to_non_flat_loops_at_GP_E`.

### F12 [NOTE] Two of the census's three "measurements" are analytically forced

For any sign pattern fixing $e_{(0,0)}$, $H(\varepsilon\psi)=S H S$ with
$S=\operatorname{diag}(\varepsilon)$, hence $V=SHSQ$ and
$\lvert V\rvert$ is entrywise unchanged — a column permutation and diagonal
$\pm1$ factors on either side preserve entrywise absolute values. At GP-E both
local legs are permutation matrices, so every downstream Born-level datum is
unchanged too. So clause (1) "the Born shadow is unchanged" and clause (2)
"the loop space is unchanged" cannot come out otherwise at GP-E. Per
§14-addendum (#208), analytically forced clauses are **disclosures, not
must-pass measurements**. This is folded into F1's replacement text.

### F13 [NOTE / round contribution] The $\psi$-law is the commutator identity — the K2 cross-unit question answers yes

Since $P_W$ is an involution, $D=P_W U_{\text{prep}}^{-1}P_W U_{\text{prep}}$
**is** the group commutator $[P_W, U_{\text{prep}}]$ exactly; and
$U_{\text{prep}}=V\otimes I_9$ gives $D = [\Sigma,V]\otimes I_9$ with
$[\Sigma,V]=\Sigma V^{\mathsf T}\Sigma V$. Substituting $V=HQ$ into the
standard identity $[a,xy]=[a,y]\cdot y^{-1}[a,x]\,y$ at $a=\Sigma$, $x=H(\psi)$,
$y=Q$ gives the paper's law in one line, with

$$D_{\text{GEN}} = [\Sigma,Q]\otimes I_9, \qquad E(\psi) = [\Sigma,H(\psi)].$$

I verified all three identities at all 11 members (33 exact matrix equalities).
So the $\psi$-term is not a discovery but a forced factor of the commutator,
and the paper's own observation that $E$ has "the same four-factor form as $D$,
one level down" is exactly this. **Recommended addition to §6.1:** state the
law as the commutator identity; it shortens the proof to one line, explains why
the $\psi$-term must appear conjugated by $Q$, and — answering the cross-unit
question directly — identifies PSI's law as the same commutator law with $\psi$
restored rather than a second law. (I could not check the XBA unit's own
phrasing: its files are being written in parallel and are outside my scope.)

### F14 [NOTE] What the GEN invariant reads at the witness member should be printed

Measured at `psi-N1`, GP-E: **158** of 364 loops readable, taking only **2**
distinct permutation values — the identity and $W$ (9 fixed configurations) —
and **206** unreadable. The 9 distinct holonomy matrices modulo global sign are
**not** closed under composition at the declared bound (8 products land
outside), consistent with $\operatorname{ord}D(\psi_{N1})>200$: there is no
finite group to report at the witness member. D7 says the permutation part is
undefined where the witness lives; it is worth printing the positive form —
"GEN's invariant, applied at $\psi_{N1}$, reads a group of order 2 and drops
206 of 364 loops" — because that is what makes the Born shadow necessary rather
than merely convenient.

---

## 3. Kill-shot disposition

**K1 — THE WITNESS: passes on the numbers, needs one scoping sentence.**
Every clause of the Born-level indistinguishability of `psi-N1` from `psi-G`
verified independently: same $\lvert\psi\rvert$; same $\lvert V\rvert$
entry by entry; same Born key of every declared and every realized leg at all
12 (setting, frame) pairs; same node law at all 48 nodes; same admission table
at all 48 cells; same loop space (364 common, 0 only-ref, 0 only-here). Exactly
**two** members of the eleven meet all of it — `psi-S1` and `psi-N1` — as
claimed. The 206 and the 2 recomputed by two routes each. **Scoping: F5** —
the claim must be, and is not, scoped to the declared basis.

**K2 — THE LAW: passes entirely.** The law reproduces the direct $81\times81$
four-factor product entry by entry at all 11 members; the iff holds in both
directions with $\{E=I\}=\{\text{invariant}\}=\{D=D_{\text{GEN}}\}$; the
census is 26 / 22 / 0 and the split is exactly "$\varepsilon$ non-constant on
some $\Sigma$-pair of the support" (4,4,0,2,12,4,0 non-invariant per member);
Q-negA gives order 6 and non-abelian as the dihedral law requires. Cross-unit:
**F13**, the law is the commutator law with $\psi$ restored. Framing:
**F6**, the negative control is inside GEN's exhaustive rebuild.

**K3 — FAMILY AND COMPARATOR: the comparator choice is right; two disclosures
missing.** D7's choice of the Born shadow as primary is forced and correct —
at `psi-N1` the permutation part is undefined on 206 of 364 loops (F14). The
split's *gauge* behaviour is properly gated —
`loops_whose_readability_moved_under_a_switching` is a must-pass zero in the
self-test — but the split itself is **reported and not gated**: no must-pass
predicate constrains `common_loops_where_readability_flips`, the cross-$\psi$
count that carries the whole finding. Nothing is dropped, though: I verified
the 206 over the full 364-row common set with no filter, and the Born shadow
is defined on every row. Steering: the
family is `[SAMP]`-tagged, the sizes are computed, and the in-family negative
controls (`psi-S1`, `psi-S2`) do real work — the table comes out both ways.
**F8** (the permutation column is not a second reading) and **F3** (only one
reported pair is at fixed Born shadow) are the honest-scope repairs.

**K4 — THE SECOND PHENOMENON: verified; the split is the honest reading.**
The 8 moving cells reproduce and are exactly the realized rule at
$t\in\{0,1,2,3\}$ at GP-E and GP-F; $364\to 8$ based loops and $13\to 9$ links
reproduce. D10's decision — report `PSI-PATH-SPACE-DEPENDENCE` beside the
verdict rather than folded into it — is correct on the pin's own vocabulary,
which makes that outcome require every common loop's holonomy to be
$\psi$-invariant, a condition this family refutes. No finding.

**K5 — INSTRUMENT: #234 compliance fails in two places.** The 146 anchors are
present and all pass, 37 of them external with three pinning the receipt
itself; the exactness sweep is clean on my own AST pass (0 float literals, 0
`float()` calls, no numpy); the refusal mechanism is real — the memo key is
`(member, setting, probe)` and carries no switching, so a live cache would
return the unswitched matrix for all 8,192 switchings and the odd-sign ones
would fire `deviations`, which is exactly what `memo-lax` demonstrates; the
priming/re-read bookkeeping makes the zero-hit reading non-vacuous.
**PSI-VERDICT is noncompliant (F2)** — waiver-only is a symptom, the disease
is that the gate predicate tests vocabulary rather than derivation and the
qualifier is a typed literal. **Cell-completeness is ungated (F7).** Two
silent-drop paths (F10). No silent drops found in the readable-split handling.

## 4. Reproduction of the delivered artifacts

I copied the frozen instrument and its pinned GEN receipt into the scratchpad
(byte-identical, `sha256 49b3c980e7d8…`) and ran it there — no repo file is
touched, because the artifacts are written only under
`--falsification-selftest`, which I did not pass.

**The frozen instrument reproduces its delivered artifact.** My run ended
`146 anchors, 20 gates, 0 must-pass failures`, verdict
`PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW`. Comparing gate blocks against
`psi_curvature_output.txt`: **20 of 20 shared gates identical — same PASS
status and byte-identical `value:` lines, with zero differences.** The single
gate absent from my run is `PSI-FALSIFICATION`, which exists only under
`--falsification-selftest` (the 34-mutant table), which I did not run because
other agents were saturating the machine with one. So the delivered receipt is
reproducible on an independent invocation, and the claim of determinism holds
in the only part I could test.

**Instrument-hygiene item, confirmed as disclosed.** §11's disclosure is
accurate and matters: a delivery-mode run writes `psi_curvature_output.txt`
and `psi_curvature_receipt.json` **before** it computes its exit code
(`build_receipt()` → `write_text()` → `fail = …`), so a failing delivery run
would replace a good artifact pair with a failing one. Disclosing it is right;
moving the two writes below the exit-code computation costs two lines and
should be done in the repair.

---

## GRADE

**ACCEPT-WITH-FIXES.**

The unit's physics survives my instrument intact. I rebuilt base G from the
prose and reproduced every load-bearing number — the family table, all 528
admission cells, the whole path space (34,024 / 5,864 / 760), the 206 and the
196 and the 2, the $\psi$-law entry by entry at all 11 members, the iff in both
directions, the 48-member census at 26 / 22 / 0, and both Q controls. I found
**no false number anywhere in the paper, the output or the receipt**, and the
central claim — that at a fixed Born shadow of the declared basis, with every
declaration held identical and the loop space measured identical, a named loop
carries different holonomy at two preparations — is true, twice over (I added a
second, orthogonal-state witness pair the unit did not form).

It is not an ACCEPT because four things must change before this is citable:
a stated mechanism that its own census refutes off GP-E (F1); a verdict gate
that does not do what §9 says it does and that a branch swap defeats (F2); a
witness count that does not hold at the verdict's own qualified scope (F3);
and a false statement about $E(\psi)$ in the theorem section (F4). F5's
basis-scoping sentence is required by the frozen protocol. F6–F8 are
straightforward, and F13 is offered as a construction the repair may take with
credit.

None of the required repairs moves a number.
