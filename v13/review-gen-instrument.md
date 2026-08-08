# GEN — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens.
**Object under review:** `v13/paper-gen-generality-check.md` (sha256-12 `4baf4e22c1aa`),
`v13/code/gen_generality_exact.py` (`78baf5eb3ef6`),
`v13/code/gen_generality_output.txt` (`9dc0ff7ed387`),
`v13/code/gen_generality_receipt.json` (`af0c41c573ee`).
**Protocol:** `v13/note-gen-hostile-protocol.md` (frozen 2026-08-08, v13 #215),
kill-shots K1–K5. Primary weight on **K5** and **K3**.
**Pin:** `v13/note-gen-generality-pin.md`.
**Method:** repo read-only; all work in the session scratchpad; independent
rebuild of base G **from the paper's prose only** — no object of the unit is
imported anywhere in my instrument. No repo file was modified. NO git.
**Interpreter:** `/opt/homebrew/bin/python3.13`.

**SHA verification — all four match, on disk, before anything else was read:**

| file | declared | measured |
|---|---|---|
| `v13/paper-gen-generality-check.md` | `4baf4e22c1aa` | `4baf4e22c1aa` |
| `v13/code/gen_generality_exact.py` | `78baf5eb3ef6` | `78baf5eb3ef6` |
| `v13/code/gen_generality_output.txt` | `9dc0ff7ed387` | `9dc0ff7ed387` |
| `v13/code/gen_generality_receipt.json` | `af0c41c573ee` | `af0c41c573ee` |

**Independent recomputations performed: 71.** Listed in §9.

**Grade: `ACCEPT-WITH-FIXES`** (stated last, §10, with the reasoning).

---

## 0. Summary for the adjudicator

I could not break a single number. Every count, every group, every membership
cell, every class count, every probe and both controls reproduce **exactly** on
an instrument I wrote from the paper's prose. A full delivery-mode rerun on a
clean scratch copy produced `gen_generality_output.txt` and
`gen_generality_receipt.json` **byte-identical** to the committed artifacts.
Three deliberate breakages — one external source, two pinned self-declarations —
each killed the run with exit code 1 and the right anchor named.

What I did break is smaller and sharper than a number, and there are four
things of it.

1. **The completion map the protocol demanded is absent, and the one
   comparator the paper does exhibit is the rarest member of its own family.**
   I swept the declared completion family exhaustively (40,320 members) and
   rebuilt the base in full on a declared 18-member sample. Geometry is
   **generic** — 99.76% of the family carries a non-trivial preparation
   defect; the bare Householder of §7.2 is one of 96 exceptions (0.24%). That
   *strengthens* the unit and it is not reported. But the **Klein four-group is
   not generic**: across the sample the group order runs 4, 6, 8, 10, 12, 30,
   with element orders up to 15, and only the ≈2% sub-family whose defect fixes
   45 configurations reproduces Klein-four. P2's headline is completion-
   selected. That is not reported either. (MAJOR, §2.)
2. **One statement the receipt makes about its own instrument is false.** The
   `GEN-SPECIES` gate claims the `anchor-record` mutant "must die at the
   injectivity clause **and at the decomposition clause**". It does not die at
   the decomposition clause: that clause compares a constructor with a verbatim
   copy of itself, through the *same* mutated `pointer_shift`, and I measured it
   to stay `True` under the mutation. §2.2's "every declared local leg is
   measured equal, entry by entry, to that sum" is the #38→#40 failure verbatim.
   (MAJOR, §3.)
3. **§8's epigram is false for 7 of its 12 agreeing rows.** "The differences
   are the flesh; the agreements are the geometry" credits geometry with four
   rows that are copied design choices and three that are pure graph
   combinatorics. (MAJOR, §4.)
4. A cluster of forced-or-vacuous clauses carried as must-pass, in a unit whose
   own doctrine says forced clauses are disclosures — and which correctly
   disclosed exactly one of them. (MINOR ×4, §5.)

None of this moves a computed value, and none of it defeats
`GEN-STRUCTURE-REPRODUCES`. The verdict's decision rule is P1–P5 at the
declared base, the completion is part of the declared base, and the pin
authorises exactly that. What the findings require is a scope tag at P2, a
corrected sentence at §2.2 and §8, and the completion sweep entered as the
second dimension of §7.2.

---

## 1. What survived — the affirmative record

I state this first because the failures below are legible only against it.

### 1.1 The base declaration, rebuilt from prose (K4)

Working only from §2 of the paper — the quaternions, the Euler–Rodrigues rule,
ψ's coefficients, `V = H·Q` with H the Householder carrying `e_(0,0)` to ψ and Q
the transposition of `|0,1⟩` and `|0,2⟩`, and the index map — my constructor
reproduces:

- the three rotation matrices, **entry by entry**, against the paper's printed
  R₀/R₁/R₂, each exactly orthogonal over ℚ;
- the **full 9×9 completion V, all 81 entries, zero mismatches** against the
  matrix printed in §2.3; column 0 exactly ψ; V exactly orthogonal over ℚ;
  ψ of unit norm, exchange-invariant, Schmidt rank **3**;
- the Born shadow of V measured **not** exchange-symmetric while that of the
  bare H **is** — the fact §2.3 and `GEN-COMPLETION-IS-LOAD-BEARING` turn on.

So A01–A03 and A07 are honest self-anchors against a declaration that a third
party can rebuild. The disclosure in D1 — that most anchors are self-anchors
because a new base has no prior committed numbers — is the right disclosure and
the mechanism does what it says: it catches constructor drift. I broke it
deliberately and it died (§7).

### 1.2 The arena (K4)

| quantity | paper | my independent count |
|---|---|---|
| declared relabelling scope | 162 | **162** (generated 162, deduplicated 162) |
| declared extension | 216 | **216** (162 ∪ 72, overlap 18) |
| admitted after the j₀ filter | 2 | **2**, and the set is exactly `{1, W}` |
| admitted at the extension | 8 | **8** |
| scope closed under composition | yes | **yes** (162² compositions checked) |
| `W = X_S · X_P` | yes | **yes**, both orders |
| fixed points W / X_S / X_P | 9 / 27 / 27 | **9 / 27 / 27** |
| switching group per setting | 2⁹ = 512, 2¹³ = 8192 | **512 / 8192** |
| checkpoint subgroup | 2⁸⁻¹ = 128 | **128** |

The 216 is a genuine union arithmetic (162 + 72 − 18) and not a typed number;
the 8 is the j₀-survivor count of the extension (the pointer transposition fixes
the ready state where the 3-cycles do not). Both reproduce.

### 1.3 The admission table, the path space, the five patterns (K2)

Implementing §3's four-clause predicate myself over the 2-element admitted
scope, I get the §3 table **cell for cell**: FULL draws at **18** cells, REAL at
**8**; the leg-prefix alignment profile is aligned at t = 1 and t = 3 and
divergent at t = 2 at **every** setting.

| quantity | paper | mine |
|---|---|---|
| links / id-links / cycle rank, GP-A…D | 9 / 3 / 2 | **9 / 3 / 2** |
| links / id-links / cycle rank, GP-E/F | 13 / 7 / 6 | **13 / 7 / 6** |
| total reduced paths | 34,024 | **34,024** |
| path pairs sharing both endpoints | 4,972,096 | **4,972,096** |
| closed paths, GP-A…D / GP-E/F | 56 / 2,820 | **56 / 2,820** |
| closed paths at F1@t0 | 8 / 364 | **8 / 364** |
| P1 non-flat closed paths, GP-E and GP-F | 1,896 of 2,820 | **1,896 of 2,820** (both) |
| P1 non-flat, GP-A…D | 0 of 56 | **0 of 56** (all four) |
| P1 not-signed-permutation, all base points | 600 / 820 | **600 (GP-E) / 820 (GP-F)** |
| P2 value set / group order / closure | 4 / 4 / closed | **4 / 4 / closed** |
| P2 abelian, element orders | yes, {1,2} | **yes, {1,2}** → Klein four |
| P2 element fixed points | 81 / 45 / 9 / 9 | **81 / 45 / 9 / 9** |
| GP-E class counts | 82 / 86 / 90 / 106 | **82 (1) / 86 (W) / 90 (D) / 106 (WD)** |
| D = P_W U⁻¹ P_W U | signed perm, order 2, 45 fixed | **signed perm, order 2, 45 fixed**, all signs +1 |
| D vs 1, W, X_S, X_P | none of them | **none of them** |
| GP-E / REAL sub-connection | 10 links, rank 3, 18 closed, 1×10 + D×8, group 2 | **exactly that** |
| GP-E / FULL sub-connection | 9 links, rank 2, 8 closed, 1×8, group 1 | **exactly that** |
| GP-A…D / REAL | 6 links, 0 closed | **6 links, 0 closed** (cycle rank −1: graph disconnected; the paper's "—" is honest) |
| W intertwines the prep leg | no | **no** |
| P5 membership: 1, W | in all four collections | **in all four** |
| P5 membership: D, W·D | outside all four | **outside all four** |
| X_S, X_P in the 162-scope / in the group | no / no | **no / no** |

**Both directions of the P4 and P5 gates verified independently:** D is an
element at GP-E/F and is *not* an element at GP-A…D (whose group is `{1}`);
`outside` is 2 at GP-E/F and 0 at GP-A…D.

### 1.4 The probes, the controls, the flip-test (K5)

| probe | paper | mine |
|---|---|---|
| canonical loop, all six | the identity | **the identity**, all six |
| positive control (two same-endpoint paths) | equal at the amplitude layer | **equal**, all six |
| aligned-prefix bigon t=0 | the wing exchange | **the wing exchange** |
| prefix-crossing loop t=1↔2 | the identity | **the identity** |
| twisted comparator, GP-A…D | not a signed permutation | **not a signed permutation** |
| twisted comparator, GP-E/F | "another permutation" | **W·D** (see N2) |
| direction flip | reversed = inverse | **reversed = inverse** |

### 1.5 The instrument layer (K5)

- **85,760 is exactly right and is not a typed number.** The swept set is
  `declared_loops(sp, G)` filtered to those carrying an edge list: 1 canonical
  loop at each of GP-A…D, and at each symmetric setting 1 canonical + 3 aligned-
  prefix bigons (t = 0, 1, 3) + 1 prefix-crossing loop = 5. That is
  **14 loops**, matching the 14 rows in `gauge_selftest.per_loop`. The
  comparison count is then 4·1·(512 + 128) + 2·5·(8192 + 128) = 2,560 + 83,200 =
  **85,760**. Deviations 0, non-signed-permutations 0, sign-moves under the
  checkpoint subgroup 0, and the sweep is measured complete
  (`switchings_swept == switching_group_order`) at every setting.
- **The D6 memoisation cross-check is real and is in fact stronger than D6
  claims.** `loop_matrix_fresh` builds through `mm_memo` (which memoises the
  field's `+` and `×` in `_KMUL`/`_KADD`); clause (1) of `GEN-GAUGE-COVARIANCE`
  compares that output, exactly, against `H0` built by the plain `mm` scaled by
  the switching's global sign — on **every one** of the 85,760 instances, not
  only on the all-positive ones. D6's "an all-positive switching is an exact
  equality test between them" understates its own gate.
- **The completion flip-test is a genuine full rebuild, not a stub.**
  `with_completion` swaps `VCOMP`, clears `_FIXTURE`, `_INTERN`,
  `_INTERN_VALUE`, `_HOL_CLASS`, recomputes the prefix profile, the admission
  table over all 24 cells, all six graphs, `enumerate_paths` and
  `based_holonomy` per setting, and `prep_defect()`; it restores in a `finally`,
  so nothing leaks upward. My own independent rebuild on the bare Householder
  reproduces **every** cell of §7.2's table: Born shadow symmetric (yes);
  identification links 3/3/3/3/**5**/**5**; holonomy group order **1 at all six
  settings**; preparation defect **the identity, 81 fixed points**. I also
  confirmed the stated mechanism: at GP-E/F the bare completion makes FULL admit
  **two** permutations at t ∈ {0,1,3} (so those links are refused for want of
  uniqueness) while admitting one at t = 2 — 4 REAL links + 1 FULL link = the 5.
- **No fixture of the first base is imported.** AST + grep over the whole
  module: the only imports are `argparse, ast, hashlib, itertools, json, sys,
  time, fractions.Fraction, pathlib.Path` (+ `subprocess`,
  `concurrent.futures` inside `run_mutant_table`). The only external file read
  is `nt_transport_receipt.json`, at one call site (`_nt()`), consumed for five
  scalar/pair lookups. §10.11's claim holds.
- **Determinism.** An independent `--falsification-selftest` run in a clean
  scratch directory produced artifacts **byte-identical** to both committed
  files (`diff` empty on each).

### 1.6 K5(a) — the AST no-mutant-exemption gate

The gate's own result reproduces: **zero** `MUTANT != …` comparisons. I then
ran a *wider* sweep than the instrument's, because a gate that counts only
`ast.NotEq` does not enforce its own headline:

| exemption pattern | occurrences in the committed source |
|---|---|
| `MUTANT != …` (`NotEq`) | **0** |
| `MUTANT not in …` (`NotIn`) | 1, at line 3491 — `if MUTANT and MUTANT not in MUTANTS:` in `main()`, the CLI validity check. Not a gate predicate. |
| `MUTANT is not …` (`IsNot`) | **0** |
| `not (<expr referencing MUTANT>)` | **0** |
| `MUTANT ==` (the permitted injection form) | 28, every one at a computation site |
| **`gate()` / `anchor()` call sites whose arguments reference `MUTANT` anywhere** | **0 of 41** |

That last row is the check the gate should be making and is the strongest form
of the claim: no gate predicate, claim string or value expression in the module
reaches the mutant flag at all. It passes. `exempt-lax` registers one comparison
and dies at `GEN-NO-MUTANT-EXEMPTION` — confirmed in my own rerun's mutant
table. The gate's *predicate* is nonetheless narrower than its *claim* (F8).

### 1.7 K5(b) — census honesty

| clause | value in the receipt | my reading |
|---|---|---|
| `never_falsified` | `[]` | **EMPTY**, confirmed |
| `must_pass_gate_denominator` | 24 | correct: 25 must-pass gates at the time of the census, minus `GEN-FALSIFICATION` |
| `falsified_by_some_mutant` | 24 | both denominators printed |
| `falsified_by_a_computation_mutant` | 23 | both denominators printed |
| `falsified_only_by_a_waiver` | `['GEN-VOCABULARY']` | **the waiver-carried gate is named** |
| gate excluded from the denominator | `GEN-FALSIFICATION` | named, with the reason (it does not run inside a mutant — verified: mutants are spawned with `--mutant m --quiet` and no `--falsification-selftest`) |
| mutants / died | 26 / 26 | confirmed in my own rerun |
| kinds | 23 computation, 3 waiver | confirmed against `MUTANT_DECL` |

The census is honest and the arithmetic is right. `control-lax` and `flip-lax`
are waivers whose gates are *also* killed by computation mutants
(`orient-flip`, `id-lax`, `readtime-conflate`, `anchor-rot`, `completion-Q`,
`anchor-completion`), so `GEN-VOCABULARY` really is the only waiver-carried
gate.

**Two mutants reconstructed from the receipt's prose alone** (the protocol asks
for two; I did four), each rebuilt inside *my* instrument and run against *my*
computations:

| mutant, reconstructed from its prose | my measured kill | receipt's recorded kill |
|---|---|---|
| `defect-order` — "the preparation's swap-defect composed in the wrong order" | the mutated defect is **not a signed permutation at all**, hence not an element of the P2 group (the honest D is) | `GEN-P4-DEFECT-IS-A-GROUP-ELEMENT` ✔ |
| `label-collapse` — "the holonomy value set counted as name labels, not permutations" | value set collapses **4 → 3** (`{identity, wing exchange, "another permutation"}`), so `value_set_size == group_order` fails | `GEN-P2-GROUP-COMPUTED` ✔ |
| `prefix-lax` — "the leg prefix read as the whole declared leg list" | the profile becomes **constant** (1 distinct verdict instead of 2) | `GEN-ADMISSION-TABLE` ✔ |
| `scope-gen` — "the scope generated from a truncated generator" | scope **162 → 72**, and the truncated set is **not closed under composition** | `GEN-ARENA` ✔ |

All four reproduce. The prose is sufficient to rebuild the mutant.

### 1.8 K5(d) — the 12 anchors

**Seven self-anchors.** A01 (three rotations entry by entry), A02 (ψ as column
0 of V), A03 (the pinned 9×9, all 81 entries), A04 (orthogonality at every
(setting, frame) — 36 cells), A05 (the wings commute at all nine rotation
pairs), A06 (the pointer shift injective), A07 (V orthogonal, ψ unit norm). I
rebuilt every one from prose (§1.1) and every one holds.

**Five external anchors, each traced to its source value in the committed NT
terminal receipt:**

| anchor | typed literal | source path in `nt_transport_receipt.json` | value there |
|---|---|---|---|
| A08 | `4` | `findings.holonomy_group.per_setting.SP-E.generated_group_order` | 4 |
| A09 | `[4, True]` | same node: `value_set_size`, `the_value_set_is_closed_under_composition` | 4, true |
| A10 | `[2, 2]` | `tables.structure_group.elements_outside_every_declared_scope.{SP-E, SP-F}` | 2, 2 |
| A11 | `[34024, 4972096]` | `tables.path_space.{_total_paths, _total_pairs}` | 34024, 4972096 |
| A12 | `[18, 2]` | `tables.mechanism.single_rule_subconnections["SP-E/REAL"].{closed_paths_at_F1_t0, generated_group_order}` | 18, 2 |

Each traces exactly. Note the direction: the *declared* side is the typed
literal and the *computed* side is the JSON lookup, so what these five assert is
"the committed NT receipt still says what this unit believes it says". That is
the correct construction for a reuse anchor and the paper describes it that way
("the only thing read from it is its committed receipt's reported numbers").

**Exit-1-only, proven by deliberate breakage in scratch (three of them, on
copies; the repo was not touched):**

| breakage | result |
|---|---|
| the **external** source: `_total_paths` 34024 → 34025 in a scratch copy of the NT receipt | **exit 1**, `failed_anchors: ["A11"]`, `failed_gates: ["GEN-COMPARISON"]` |
| a **pinned self-declaration**: one entry of `PINNED_ROT["R2"]` 5/13 → 6/13 | **exit 1**, `failed_anchors: ["A01"]`, `failed_gates: ["GEN-BASE-PINNED", "GEN-COMPARISON"]` |
| a **pinned self-declaration**: one entry of `PINNED_V` −4/9 → −5/9 | **exit 1**, `failed_anchors: ["A03"]`, `failed_gates: ["GEN-BASE-PINNED", "GEN-COMPARISON"]` |

Exit-1-only holds for both kinds of anchor.

---

## 2. FINDING F1 — MAJOR (K1): the completion map is missing, and the one comparator exhibited is the rarest member of its own family

**Severity: MAJOR.** No number moves; the scope layer is materially incomplete
and the reader is led to the wrong conclusion about what the completion buys.

### 2.1 What the protocol asked and what the paper answers

K1: *"Map the completion-dependence: sweep completions of ψ (as feasible,
declared) — is the pinned completion generic or special among geometry-bearing
ones? Attack D2's honesty: the completion was CHOSEN so the base is of the
species — legitimate scoping or verdict-steering?"*

The paper exhibits **one** alternative completion, the bare Householder, and
reports that the geometry vanishes there. That is a flip-test, not a map.

### 2.2 What I measured

The declared family is forced by the paper's own construction: `V = H·Q` where H
is fixed by ψ and Q is a permutation of the nine system-pair basis indices that
**fixes index 0**, so that `V e_(0,0) = ψ` for every member. That family has
**8! = 40,320** members and it is exhaustively sweepable, because the defect
factorises: with the wing exchange `P_W = Σ ⊗ Σ` and `U_prep = V ⊗ I₉`,

> `D = P_W U_prep⁻¹ P_W U_prep = (Σ Vᵀ Σ V) ⊗ I₉`,

so the whole question lives at 9×9 and `fixed(D) = 9 · fixed(Σ Vᵀ Σ V)`. I
verified this factorisation against the declared V (5 fixed points at 9×9 → 45
at 81) before using it.

**Exhaustive screen over all 40,320 members:**

| class | count | share |
|---|---|---|
| Born shadow of V **asymmetric** and D a **non-identity** signed permutation | **40,224** | **99.76 %** |
| Born shadow of V **symmetric** and D **= the identity** (geometry cannot arise) | **96** | **0.24 %** |

The bare Householder (Q = identity) is one of the 96.

**Distribution of `fixed(D)` over the 40,224:**

| fixed(D) | 9 | 18 | 27 | 36 | **45** | 54 |
|---|---|---|---|---|---|---|
| completions | 16,704 | 11,520 | 5,376 | 4,608 | **864** | 1,152 |

**Full rebuilds of the entire base (GP-E, and GP-A as the flat control) on a
declared 18-member sample — the lexicographically first three Q in each
`fixed(D)` class:**

| fixed(D) | identification links (GP-E) | **based holonomy group order** | element orders | abelian |
|---|---|---|---|---|
| 9 | 7 | **30** | 1, 2, 3, 5, 15 | no |
| 18 | 7 | **12** | 1, 2, 3, 6 | no |
| 27 | 7 | **8** (2 of 3), **6** (1 of 3) | 1,2,4 / 1,2,3 | no |
| 36 | 7 | **10** | 1, 2, 5 | no |
| **45** | 7 | **4** | **1, 2** | **yes — Klein four** |
| 54 | 7 | **6** | 1, 2, 3 | no |

GP-A gave group order 1 in all 18, as expected. The declared completion
(Q = [0,2,1,3,4,5,6,7,8]) sits in the `fixed(D) = 45` class; the sampled member
Q = [0,1,2,3,4,5,7,6,8] — a *different* transposition — also gives Klein-four.

### 2.3 What follows

**In the unit's favour, and unreported.** Geometry is **generic** in the
declared family: 99.76 % of the completions of the *same* ψ carry a non-trivial
preparation defect. §7.2's comparator is one of the 0.24 % where it does not.
So the honest reading of D2 is *stronger* than the paper's: the transposition Q
was not needed to *find* a geometry-bearing completion — almost every Q is one.
The verdict-steering charge in K1 is **refuted** at this level, and refuted by
measurement rather than by argument.

**Against the unit, and also unreported.** The **Klein four-group is not
generic**. It appears in my sample only in the `fixed(D) = 45` class, 864 of
40,320 ≈ **2.14 %** of the family. Elsewhere the same graph, the same seven
identification links and the same ψ produce groups of order 6, 8, 10, 12 and
30, non-abelian, with elements of order up to 15. So:

- the abstract's "the same isomorphism type the first base earns, on a base
  that shares none of its flesh" is, as measured, a property of the ≈2 %
  sub-family the designer selected, not of the species;
- §9's "it is the Klein four-group, measured closed" needs the completion scope
  tag that §6.2 does not carry;
- the abstract's own hedge, "The group is a function of the base's declared
  data, completion included", is *correct* but is evidenced only by a 4 → 1
  collapse. The real variation is 4 → {6, 8, 10, 12, 30} **with the geometry
  intact**, which is a different and more interesting fact.

This is exactly the free-choice-predetermines-a-pattern risk K3 names, landing
on P2 rather than on P1.

### 2.4 Repair

1. Enter the sweep in §7.2 as its **second dimension** (the unit can recompute
   it cheaply through the 9×9 factorisation above; a `[SWEEP]` tag with the
   family size 40,320 declared, exhaustive at the screen and `[SAMP]`-tagged at
   the full rebuild with the sample rule stated).
2. Add to §6.2, verbatim:

   > The isomorphism type is a reading **at the declared completion**. Swept
   > over the declared completion family $V = H\cdot Q$ with $Q$ any permutation
   > of the nine system-pair indices fixing the initial one — 40,320 members,
   > every one of which has $\psi$ as its first column — a non-trivial
   > preparation defect is measured at **40,224** of them, so the *existence* of
   > the geometry is generic in the family and the bare Householder of §7.2 is
   > one of **96** exceptions. The **group**, however, is not: on a declared
   > eighteen-member sample, three from each measured defect class, the based
   > holonomy group order at GP-E is 30, 12, 8, 10, 4 and 6, and the Klein
   > four-group appears only in the class whose defect fixes 45 configurations —
   > 864 of the 40,320. Klein-four is therefore a property of the declared
   > completion and not of the species, and it is reported as one.

3. Amend §9's derived paragraph so that "the pattern is the theory's; the
   elements are the base's" reads "**the existence of the geometry is generic in
   the declared completion family; the group — its order and its isomorphism
   type, not only its elements — is a function of the base's declared
   completion**".
4. Add a non-claim at §10.3: "the *group* is completion-selected; only the
   existence of a non-trivial group is measured generic in the declared family."

**On the verdict.** I do **not** ask for `REPRODUCES-AT-DECLARED-COMPLETION`.
The pin says "the second base (declared, all completions PINNED as data)" and
"a DIFFERENT preparation with its completion DECLARED EXPLICITLY as data" — the
completion is part of the declared base by the pin's own construction, and the
decision rule is P1–P5 at the declared base. `GEN-STRUCTURE-REPRODUCES` stands.
What it needs is the P2 scope tag above, not a retitled tag.

---

## 3. FINDING F2 — MAJOR (K5): the receipt makes a false statement about its own instrument

**Severity: MAJOR.** This is failure #38→#40 from the RUNBOOK's own catalogue
("'independently rebuilt' — the rebuild was gated EQUAL → describe mechanisms as
measured, not as intended"), reproduced exactly.

### 3.1 The claim

`GEN-SPECIES`, clause (3), states:

> "…every local leg is measured to be exactly the sum over outcomes of a
> rank-one projector tensored with the pointer shift of that outcome … The
> `anchor-record` mutant collapses two outcomes onto one shift and must die at
> the injectivity clause **and at the decomposition clause**."

§2.2 of the paper states the same thing:

> "The decomposition is measured, not assumed: … every declared local leg is
> measured **equal, entry by entry**, to that sum."

### 3.2 The measurement

`run_base_declaration` computes `shifts = [pointer_shift(o) for o in range(NS)]`
and then rebuilds each `U_local` with a loop that is a **verbatim copy** of
`U_local`'s own body, using `shifts[o]` where `U_local` uses `pointer_shift(o)`.
Under `anchor-record`, `pointer_shift(2)` returns 1 — and `shifts` becomes
`[0, 1, 1]` **for both**. Constructor and "rebuild" are mutated identically.

I demonstrated this in an independent minimal implementation:

| `anchor-record` | shifts | `shift_injective` | `record_ok` (rebuild == U_local) |
|---|---|---|---|
| off | `[0, 1, 2]` | True | **True** |
| **on** | `[0, 1, 1]` | **False** | **True** |

`record_ok` is **blind to its own declared falsifier**. The receipt's own mutant
table corroborates: `anchor-record` kills `['A06', 'GEN-BASE-PINNED',
'GEN-SPECIES', 'GEN-COMPARISON']` — `GEN-SPECIES` dies at `shift_injective`,
which is A06's clause, and nowhere else.

The substantive record property *is* carried — by A06's injectivity, which is a
real measurement with a real killer. What is not carried is the decomposition,
which is a constructor compared with a copy of itself: the W6 circularity
catalogue's "a 'second' gate that recomputes the first".

### 3.3 Repair

Either (a) make the clause independent — rebuild `U_local` from the **pinned**
rotation matrices `PINNED_ROT` and an **independently declared** shift table
(e.g. `SHIFT_DECLARED = (0, 1, 2)` typed as data), so a mutation of
`pointer_shift` moves one side and not the other; or (b) delete the clause and
the sentence. If (a), the clause becomes a genuine falsifier and the
`GEN-SPECIES` claim text becomes true as written.

Meanwhile, replace §2.2's sentence verbatim with:

> The decomposition is declared, and the two properties it is used for are
> measured: the projectors are measured orthonormal and the outcome shift map is
> measured **injective** (A06) — which is what makes the pointer value at the
> final division event a **record** of the outcome. The entry-by-entry
> identification of each declared leg with that sum is a restatement of the
> constructor and is reported as one.

And strike "and at the decomposition clause" from the `GEN-SPECIES` claim
string, or repair the clause per (a).

---

## 4. FINDING F3 — MAJOR (K3, §8): "the agreements are the geometry" is false for 7 of the 12 agreeing rows

**Severity: MAJOR.** It is the sentence a reader carries out of the unit's
central comparison, and it is not true.

§8's arithmetic is right — I checked it: of 21 rows, **9 differ and 12 agree**.
But the epigram assigns all 12 agreements to geometry. Auditing them by
provenance:

| § 8 row | agrees because |
|---|---|
| settings 6 / 6 | **a copied design choice** — the pin permits "its own six-setting family **or a declared smaller family**"; six was free |
| symmetric settings 2 / 2 | **a copied design choice** — the family was built with exactly two symmetric members |
| admitted after the j₀ filter 2 / 2 | **a consequence of the scope design** — the j₀ filter kills every cyclic relabelling, leaving `{1, W}` on both bases by construction |
| admitted at the extension 8 / 8 | same |
| total reduced paths 34,024 | **graph combinatorics** — the paper says so in the next paragraph |
| path pairs 4,972,096 | same — the paper says so |
| realized-rule sub-connection: closed paths 18 | **graph combinatorics** — the REAL-only subgraph has 10 links, rank 3 on both bases (NT receipt: `SP-E/REAL` links 10, `cycle_rank` 3, `closed_paths_at_F1_t0` 18); the count follows from the graph and the bound alone. **Not caveated anywhere.** |
| holonomy group order 4 | geometry |
| group structure Klein four | geometry (with the F1 scope tag) |
| value set closed at the bound | geometry |
| elements outside every declared collection 2 | geometry |
| realized-rule sub-connection: group order 2 | geometry |

So **five of the twelve are geometry**, three are graph combinatorics (two of
which are caveated, one not), and four are copied design choices that are never
flagged.

### Repair

Replace §8's closing sentence verbatim with:

> Of the twenty-one compared coordinates, **nine** are measured different and
> **twelve** measured the same — but the twelve are not of one kind, and the
> distinction is the point. **Four** of them (the setting count, the symmetric-
> setting count, and the two admitted-set sizes) agree because this base's
> family and scope were *designed* with those shapes, and they carry no
> information about the geometry. **Three** (the total reduced paths, the path
> pairs, and the realized-rule sub-connection's eighteen closed paths) agree
> because the two path graphs are isomorphic, and are counts of combinatorics
> both bases happen to share. The remaining **five** — the group order, its
> isomorphism type, the closure of the value set at the declared bound, the two
> elements outside every declared collection, and the realized-rule sub-
> connection's group order — are the geometric agreements, and they are what the
> verdict rests on.

---

## 5. MINOR findings

### F4 — MINOR (K3, D5): the stated reason for the class-count agreement is measurably insufficient

§8 and D5 say the class counts 82 / 86 / 90 / 106 agree "because the group is
Klein-four in both and the word structure of the loops is fixed by the graph."

The holonomy map is a homomorphism π₁(graph, F1@t0) ≅ F₆ → ℤ₂×ℤ₂, so a closed
walk's class is determined by the parities with which it traverses the six
non-tree edges. I verified this model on **all 364** based closed walks at
GP-E — zero disagreements with the directly computed holonomy — and then swept
**all 4⁶ = 4,096** assignments of the six cycle generators, of which **3,906**
have surjective image (both groups Klein-four, same graph, same bound).

**Result: 78 distinct class-count multisets arise. `{82, 86, 90, 106}` occurs in
96 of the 3,906 — about 2.5 %.** Others include `{78, 90, 94, 102}` (384
assignments), `{80, 88, 96, 100}` (228), and degenerate ones such as
`{2, 10, 10, 342}`.

So "isomorphic graph + Klein-four group" does **not** determine the counts. The
true reason is stronger and is available from the committed NT receipt, which I
checked: the first base's `identification_multiplicity` at SP-E/SP-F assigns
**FULL ↦ the identity at t ∈ {0,1,3}** and **REAL ↦ the wing exchange at
t ∈ {0,1,2,3}** — cell for cell the same rule-to-permutation assignment as base
G — and its preparation defect enters through the same realized-rule cycles.
That is what fixes the homomorphism, and hence the counts.

D5's *direction* is right (the agreement is not independent confirmation), so
this understates rather than overstates. Replace D5's second sentence verbatim
with:

> 34,024 paths and 4,972,096 pairs agree because the two path graphs are
> isomorphic. The class counts 82 / 86 / 90 / 106 need more than that: the
> counts are fixed by the images of the six independent cycles in the group, and
> over the 3,906 surjective assignments on this graph they take 78 distinct
> values, of which these four occur in about one in forty. They agree because
> the two bases' admission tables coincide *cell for cell in the permutation each
> rule draws* — the identity for the full-leg rule at t ∈ {0,1,3}, the wing
> exchange for the realized rule at every checkpoint — so the two holonomy
> homomorphisms coincide. That is reported as a consequence of the shared
> admission structure, not as independent confirmation.

### F5 — MINOR (K5): `GEN-READ-TIME-COORDINATE` clause (2) is a contradiction predicate

`run_read_time` computes

```
if r["start"][1] != r["end"][1] and r["start"] == r["end"]: mismatched += 1
```

`r["start"] == r["end"]` entails `r["start"][1] == r["end"][1]`, so `mismatched`
is **identically zero for every input**, mutated or not. The gate's claim — "the
count of pairs whose two endpoints carry different read times is gated at zero"
— reports a clause that cannot fail. Clause (1) (`cross == 0` with `same > 0`)
*is* a real, falsifiable measurement, and `readtime-conflate` dies there; the
gate as a whole is sound. But by the unit's own §14-addendum doctrine — which it
applies correctly to `GEN-GAUGE-PERMUTATION-FORCED` — clause (2) is a
disclosure, not a must-pass clause.

**Repair:** either delete clause (2), or make it measure what it says by
recomputing it over the *pair table*: for every pair in `by_ends`, that both
members' `start` and `end` agree — which is also structural, so deletion with a
one-line disclosure ("the matched table is grouped by endpoint pair, so matched
coordinates are structural, not measured") is the honest route.

### F6 — MINOR (K5/D6): `GEN-FRESH-EVAL`'s zero-hit clause is vacuous in the honest run

`_memo` is called from exactly one site (`loop_matrix_fresh`), which is called
from exactly one site (`run_gauge_selftest`), where `_FRESH` is `True`
throughout. In the honest run the branch that writes `_MEMO` is therefore
**never reached**, `_MEMO` stays empty for the whole run, and `hits == 0` is
forced by static reachability, not measured.

§7.1's sentence — "the value cache bypassed … so the bypass is a **measured
fact** and not an absence" — overstates: there is no populated cache for the
sweep to bypass. What *is* measured, and is worth stating, is the **85,760
misses**: they evidence that 85,760 fresh evaluations occurred. And the gate
does die under `memo-lax` (the checkpoint subgroup re-visits sign vectors the
full phase already computed), so the gate is not toothless.

I record this as MINOR because RUNBOOK §14's addendum *explicitly instructs*
gating the hit count at zero, and the unit is obeying an instruction. The fix is
in the prose:

> Every holonomy in the sweep is rebuilt from the link variables; the phase's
> **85,760 cache misses** are the measurement that it was, and the cache-hit
> count is gated at zero as §14 requires. Because the instrument's only
> transported-value cache is written nowhere except inside this phase, in the
> honest run there is no populated cache to bypass; the zero-hit clause is
> disclosed as forced and the `memo-lax` mutant, which lets the phase read the
> cache and registers hits, is what gives the clause its teeth.

### F7 — MINOR (K5): `GEN-NO-MUTANT-EXEMPTION` is narrower than its own headline

The gate's claim is "NO GATE PREDICATE REFERENCES MUTANT IDENTITY"; its
predicate counts only `ast.NotEq` comparisons. `MUTANT not in ("x",)`,
`MUTANT is not "x"`, and `not (MUTANT == "x")` all express the same exemption
and are all invisible to it. I ran the wider sweep (§1.6) and the module is
**clean under every one of them**, so no defect exists today — but the gate does
not enforce what it claims and would not catch the next one.

**Repair:** widen the predicate to `NotEq | NotIn | IsNot` plus negated `Eq`,
and add the reachability check I used: for every `gate(...)`/`anchor(...)` call
site, walk its argument expressions and count any `ast.Name` with
`id == "MUTANT"` — measured **0 of 41** today. That last check is the direct
statement of the headline. Keep the existing `!=` count as one clause of it and
keep `exempt-lax` as its falsifier.

### F8 — MINOR (K5): `GEN-VOCABULARY` is analytically forced, and its claim exceeds its predicate

Two things, both disclosed only in part.

(a) Every branch of `run_verdict` builds the verdict from a pre-registered
template, so `any(verdict.startswith(x) for x in PREREGISTERED)` is true by
construction. §11 says so plainly and the census names it — this is the most
honestly handled forced clause in the unit. But the RUNBOOK §14 addendum the
unit cites says forced clauses are *disclosures*, and this one is carried as a
must-pass. Reclassifying it would give a cleaner census: denominator 23, all 23
falsified by computation mutants, `never_falsified` still empty, no
waiver-carried gate at all.

(b) The claim string says the gate measures "that the emitted verdict begins
with one of the pre-registered names **and that it is the one the rule selects
from the recorded gate results**". The predicate checks only the first. Nothing
independently derives the verdict and compares.

**Repair:** either derive the verdict a second time inside the gate from
`FINDINGS["pattern_gates"]` and compare (which makes the second conjunct real),
or strike it from the claim string. My preference is the former plus
reclassification of the residue as a disclosure.

### F9 — MINOR (K4/K5): the NT receipt is read by path with no hash assertion

`NT_RECEIPT = HERE / "nt_transport_receipt.json"`. The five external anchors
verify its *contents* at five points; nothing verifies it is the committed NT
terminal artifact. `BASE_COMMIT = "fceb614"` is a typed string that is printed
and never checked. The NT receipt itself carries `source_sha256 =
8cb7607d2ba18c…` — which I verified equals the sha256 of
`v13/code/nt_transport_exact.py` — and GEN never reads it.

**Repair:** add a thirteenth anchor:

```
anchor("A13", "the committed NT terminal receipt",
       "the NT receipt's own recorded generator hash",
       "8cb7607d2ba18c358f12ca22e69d5d398e3e840a998ad8316ef33dc2963670e7",
       _nt()["source_sha256"])
```

and, better, a sha256 of the receipt file itself (`d256891b479a…`). Then "the
immutable base fceb614" is an assertion rather than a caption.

### F10 — MINOR: §4's path table mixes two path conventions in one row set

The instrument's `enumerate_paths` emits the length-0 path at each of the 8
nodes, so "reduced paths 422 / 16,168" and the total **34,024** *include* 48
empty paths; `based_holonomy` and `closed_path_census` skip them
(`not path["len"]`), so "closed paths 56 / 2,820" and "364 based there"
*exclude* them. Both conventions are internally consistent and I reproduced
both exactly (my counts without the empty path: 414 / 16,160 / 33,976, and 64 /
2,828 / 365 closed with it) — but the §4 table presents them side by side
without saying so.

**Repair:** add to §4, after the table: "The reduced-path counts include the
length-zero path at each node; the closed-path and based-path counts exclude
it, since a length-zero loop carries no transport content. Both conventions are
stated because both appear in this table."

### F11 — MINOR (K2): P1's both-ways property is printed but not gated

The paper says of P1: "the gate is a measurement that comes out both ways on one
base, and not a fixture of the instrument." The predicate is
`len(nontrivial) > 0 and all(closed_paths_based_there > 0)`. The "0 of 56 at the
other four settings" reading lives in the gate's *value*, not in its predicate —
unlike P4 (`all(not inpg[sp] for sp not in nontrivial)`) and P5
(`all(outside[sp] == 0 for sp not in nontrivial)`), which both gate their
negative half explicitly.

**Repair:** add the conjunct `and all(nonflat[sp] == 0 for sp in SETTING_ORDER
if sp not in nontrivial)` to the P1 predicate. It is true on this base (I
measured 0 at all four), it can fail, and it makes the sentence in §6.1 a
description of the gate rather than of the table beside it.

I also note for §6.1's disclosure: the 1,896 non-flat closed paths at GP-E
**include** the 600 whose holonomy is not a signed permutation (820 at GP-F);
the two numbers are printed against different denominators and their
relationship is not stated. One clause fixes it: "of those 1,896, 600 are
holonomies that are not signed permutations at all."

---

## 6. NOTES

**N1 — a failing delivery run clobbers the frozen artifacts.** `main()` writes
`OUT_TXT` and `OUT_JSON` under `if a.falsification_selftest and not a.mutant`
*before* computing the exit code, so a delivery run made after a bad edit
overwrites the committed receipt with a failing one and then exits 1. Suggest
gating the writes on `fail == 0`, or writing to a temp path and renaming.
(I ran all my breakage tests on copies, so nothing in the repo moved.)

**N2 — the negative control's holonomy at the symmetric settings is W·D.** The
receipt prints "another permutation" because `run_probes` executes before
`run_patterns` registers `W·D` in `PERM_NAME`. I computed it independently: at
GP-E and GP-F the twisted comparator's holonomy is exactly `W·D`, an element of
the group under study. It is still a valid negative control (the requirement is
"not the identity", and it is not), but naming it would be more informative and
would let a reader see that the injected twist lands *inside* the holonomy
group at the symmetric settings while landing outside the signed permutations
entirely at the four flat ones. A one-line reorder (register the names from
`prep_defect()` before `run_probes`) fixes the printout.

**N3 — P4's negative half is forced once P3 has fired.** `inpg[sp]` at a
trivial setting is `D ∈ {identity}`, and P3 already gates
`not D["is_the_identity"]`. So the "second half is what makes the first a
measurement rather than a tautology" is true only relative to P3's clause. Worth
one clause of acknowledgement; not a defect.

**N4 — the pin's "one wing enlarged".** The pin asks for "different wing
dimensions (one wing enlarged, e.g. qutrit-or-higher system side or enlarged
pointer side)". Base G enlarges *both* wings and *both* the system and the
pointer (3,3,3,3). This is a defensible reading — an asymmetric base would have
no wing exchange at all and the species clause could not be posed — and it
satisfies the pin's intent a fortiori. But no deviation note records the
reading, and D-notes exist for smaller departures. Suggest a one-paragraph D9.

**N5 — D3 is PIN-COMPLIANT (K5(f)).** The pin's P1–P5 name identification
multiplicity and the preparation's swap-defect; the composition defect is named
nowhere in the pin, in the outcomes, or in the discipline clause. Dropping it is
therefore within scope, and D3 scopes the omission correctly ("Nothing is
claimed about the composition defect on base G, and no result of this unit rests
on it"). I checked that no gate, no pattern predicate and no comparison row
reads it. The one thing I would add: §10's non-claims never mention it, and §10
is where a reader looks for the boundary. Suggest adding to §10.2: "…and it does
not re-measure the first base's third transported object, the composition defect
of the law's own factorisation, which is out of the pin's scope and is not
carried here (D3)."

**N6 — on K3's steering audit.** Forced by the pin: two wings; a preparation;
commuting local legs; records at the final division event; enlarged wing
dimension; a different preparation with its completion declared as data; a
six-setting or declared-smaller family with the size computed. Free: `NS = NP =
3`; the three quaternions; ψ; **Q**; the six-setting family and *how many of it
are symmetric*; the scope generators; `L_max = 2·NLEGS + 2`. Of the free
choices, two predetermine reported agreements — the family shape (F3) and Q
(F1). Neither predetermines P1, which I measured to be generic across the
completion family. That is the substance of the steering audit and it comes out
mostly in the unit's favour, but it is not written down anywhere in the paper.

---

## 7. Attempts that failed to break anything

Recorded so the adjudicator knows where the attack surface was probed and held.

- Trying to find a fixture import from W6/NT: none exists; AST + grep over 3,606
  lines; one external read, five scalar lookups.
- Trying to make the admission table come out differently by implementing the
  four clauses in a different order or with a different leg-key canonicalisation:
  same table, 24/24 cells.
- Trying to make the path counts differ by a different reduced-path convention:
  the only difference is the empty path, and both conventions are internally
  consistent (F10).
- Trying to find a switching outside the swept group: the sweep is
  `itertools.product((1,-1), repeat=len(links))`, complete by construction, and
  `switchings_swept == switching_group_order` is gated.
- Trying to find a loop with an edge list that is *not* swept: 14 loops
  declared, 14 rows in `per_loop`, and the one excluded probe (the twisted
  comparator, which has `edges = None`) is named in the receipt, in §5, in §7.1
  and in §10.9. Coverage is stated four times.
- Trying to make the byte-identical claim fail: it does not; my clean-room
  delivery rerun matched both artifacts exactly.
- Trying to find a float: none. AST sweep finds zero float literals and zero
  `float(` calls; every operator entry is a `Fraction`; `is_orthogonal` and
  `signed_perm` compare against exact `ONE`/`ZERO`.
- Trying to make an anchor fail silently: all three deliberate breakages exit 1
  with the anchor named in `KILL-JSON`.

---

## 8. What I would ask the repair worker to do, in order

1. **F2** — repair or delete the decomposition clause; strike the false half of
   the `GEN-SPECIES` claim; replace §2.2's sentence (verbatim text at §3.3).
2. **F1** — run the completion sweep (the 9×9 factorisation makes it cheap),
   enter it in §7.2, add the P2 scope tag and the §9/§10.3 amendments (verbatim
   text at §2.4). No number in §6.2 moves.
3. **F3** — replace §8's closing sentence (verbatim text at §4).
4. **F4** — replace D5's second sentence (verbatim text at §5/F4).
5. **F5, F6, F7, F8, F11** — instrument repairs, each local; the receipt is
   regenerated once at the end and the census re-run.
6. **F9, F10, N1, N2, N5** — one-line additions.

**No number in the paper may move.** I recomputed 71 of them and none is wrong.
If any number moves during the repair, the repair is wrong.

---

## 9. Independent recomputation ledger — 71

Base declaration (18): R₀, R₁, R₂ each vs the pinned matrix and for exact
orthogonality (1–3); the Householder H from ψ (4); V = H·Q entry by entry vs the
printed 9×9, 81 entries (5); column 0 = ψ (6); V exactly orthogonal over ℚ (7);
ψ unit norm (8); ψ exchange-invariant (9); ψ Schmidt rank 3 (10); scope 162
generated and deduplicated (11); extension 216 (12); admitted = 2 = {1, W} (13);
admitted extension 8 (14); scope closed under composition (15); W = X_S·X_P
(16); fixed points 9/27/27 (17); Born shadow of V asymmetric, of H symmetric
(18).

Admission and paths (8): the 24-cell admission table, both rules (19); the
alignment profile at all 18 (t, setting) cells (20); links/id-links/cycle rank
per setting (21); reduced path counts 422 / 16,168 (22); total 34,024 (23);
pairs 4,972,096 (24); closed paths 56 / 2,820 (25); based closed paths 8 / 364
(26).

P1–P5 (13): non-flat 1,896/2,820 at GP-E and at GP-F (27); 0/56 at GP-A…D
(within 27); not-signed-permutation 600 / 820 (28); value set 4 and closure
(29); abelian, orders {1,2} (30); element fixed points 81/45/9/9 (31); class
counts 82/86/90/106 (32); D signed, order 2, 45 fixed, ≠ 1/W/X_S/X_P (33);
GP-E sub-connections FULL, REAL, FULL+REAL (34); GP-A REAL 6 links 0 closed
(35); W does not intertwine the prep leg (36); P4 both directions (37); P5
membership table all 16 cells (38); X_S/X_P outside the scope and outside the
group (39).

Probes, controls, flip (6): canonical loop = identity ×6 (40); positive control
×6 (41); twisted comparator ×6 (42); bigon at t=0 (43); prefix-crossing loop
(44); direction flip = inverse (45).

Instrument (8): the 14-loop swept set derived from `declared_loops` (46);
85,760 = 4·640 + 10·8,320 (47); 512 / 8192 / 128 (48); the wider AST exemption
sweep incl. gate-argument reachability (49); `_MEMO` never written in the honest
run, by static reachability (50); `record_ok` blind to `anchor-record` (51);
`mismatched` identically zero (52); byte-identical delivery rerun of both
artifacts (53).

Mutants reconstructed from prose (4): `defect-order` (54); `label-collapse`
(55); `prefix-lax` (56); `scope-gen` (57).

External anchors (3): A08–A12 traced to their NT receipt paths (58); the NT
admission maps FULL↦identity / REAL↦wing exchange at matching coordinates (59);
the NT class counts 82/86/90/106 (60).

Deliberate breakage (3): external NT value (61); pinned R₂ entry (62); pinned V
entry (63).

Completion analysis (5): the bare-Householder rebuild, all four rows of §7.2
(64); the bare completion's per-cell admission counts (65); the exhaustive
40,320-member screen (66); the `fixed(D)` distribution (67); 18 full rebuilds
at GP-E (68).

D5 / K3 (3): the cycle-parity model verified on all 364 based walks (69); the
3,906-assignment sweep, 78 multisets, 96 hits (70); no fixture import, by AST
and grep (71).

---

## 10. Grade

Everything the unit *computes* is right. I checked 71 quantities against an
instrument built from the prose and not one of them moved. The delivery is
deterministic to the byte, the anchors are exit-1 in both directions, the census
is honest at both denominators with the waiver-carried gate named, the
no-mutant-exemption result survives a sweep wider than the one the instrument
runs, the 85,760 sweep is complete and correctly counted, the flip-test is a
genuine rebuild, and no object of the first base is imported.

Three things must be fixed before this is terminal. One statement the receipt
makes about its own instrument is **false** (F2, the decomposition clause and
its mutant). One summary sentence in the central comparison is **false for seven
of its twelve rows** (F3). And the completion map the frozen protocol
specifically demanded is **absent**, with the consequence that the paper's
sharpest positive result — that the *existence* of the geometry is generic
across 99.76 % of the declared completion family — goes unreported, while its
headline group is completion-selected at about 2 % and carries no scope tag
(F1). None of these is a computational error and none defeats the verdict; all
three are repairable without moving a number.

> **`ACCEPT-WITH-FIXES`**
>
> Fixes required: F1, F2, F3 (MAJOR); F4–F11 (MINOR); N1–N6 (notes, at the
> repair worker's discretion except N5, which should be entered in §10).
> `GEN-STRUCTURE-REPRODUCES` stands, at the committed finite scope, at the
> declared admission scope, **and at the declared completion** — with P2 carrying
> the completion scope tag F1 specifies.
