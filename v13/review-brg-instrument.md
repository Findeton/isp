# BRG — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens.  **Date:** 2026-08-08.
**Protocol:** `v13/note-brg-hostile-protocol.md` (FROZEN, v13 #268), kill-shots
K1–K5 binding; primary weight on **K5**, K1–K3 at lower depth.
**Object reviewed (SHA-256 verified before and after the review, unchanged):**

| file | sha256-12 | verified |
|---|---|---|
| `v13/paper-brg-bridge.md` | `3191e39da0b1` | ✓ |
| `v13/code/brg_bridge_exact.py` | `6f288deb3ee9` | ✓ |
| `v13/code/brg_bridge_output.txt` | `e27aae1c48e0` | ✓ |
| `v13/code/brg_bridge_receipt.json` | `bf1b51d5e806` | ✓ |

The unit's own five hash pins were also verified against disk and all five match
`DECL["pins"]` exactly: pin `56ce4a7e2dee…`, HA `542b8735daf0…`, NT
`d256891b479a…`, GEN `e0b2f444f6a9…`, XBA `6015708df2a4…`.

**Method.** Repo read-only; no git; all work in the session scratchpad. Nothing
was imported from the unit: the two sides were rebuilt from the published prose
(Σ, `D = ΣQᵀΣQ`, `W = Σ⊗Σ`, the dihedral presentation, HA's translation action)
in my own code. In-source probes were run against **scratch copies** of the
repo tree, never the repo. Every probe below is an *undeclared* mutant of my own
design — none is on the unit's 47-mutant list.

**Recomputation count: 152 independent recomputations of committed quantities,
plus 36 adversarial runs** (30 undeclared-mutant probes, 5 corrupt-and-fire
tests on the real pinned files, 1 full delivery rerun).

---

## 0. What reproduced, before the findings

The unit is arithmetically sound and I could not move a single published number.

- **A full independent delivery rerun reproduces `brg_bridge_output.txt`
  byte-identically** (zero-byte diff, exit 0). All 47 declared mutants died,
  `mutant_survivors` 0, `never_falsified` empty — reproduced in my run.
- **All 77 anchors pass**, and **all five hash pins fire exit-1 with the correct
  anchor named when the real file is corrupted** (K5(a), see §5).
- Independently rebuilt and matching: the 40,320-member family; the defect order
  spectrum `{1:96, 2:1440, 3:4224, 4:4608, 5:4608, 6:6912, 7:9216, 15:9216}`;
  the fixed-configuration spectrum `{9:16704, 18:11520, 27:5376, 36:4608,
  45:864, 54:1152, 81:96}`; 96 identity-defect / 40,224 geometry-bearing; 0
  dihedral-relation failures; **12** distinct (order, fixed) classes; ρ mod p at
  all seven primes; carriers p⁴ and orbits p³; non-reducible primes exactly
  `{2,3}`; determinant 2; base G's `D = [0,2,1,6,4,5,3,7,8]` with 45/9 fixed and
  |⟨W,D⟩| = 4; base T 3/6; base S′ 2; species 4 192/16/4 and its 120-member
  split 12/60/48; base 1's 6/18/12.
- **K1 reproduced.** The obstruction is correct as elementary group theory and
  as a census: |hom(ℤ/p, D_n)| = gcd(n,p) for odd p (a non-trivial image needs
  an element of order p; Lagrange forbids it unless p | 2·ord(D)), and Ab(D_n)
  has order 2·gcd(2,n) ∈ {2,4} — a 2-group at every cell, so the reverse census
  is trivial for every odd prime with no prime-dependence at all. Over my own
  140 cells: **137 empty / 3 live, coextensive with gcd(p,|⟨W,D⟩|) = 1 in both
  directions.** Scope 1: 56 cells, 0 forward, 0 reverse. Scope 2: 84 cells, 14
  non-trivial forward, living exactly at (5, ord 5), (5, ord 15), (7, ord 7)
  with 4/4/6.
- **K3 reproduced.** ρ = (1/6,1/6) fails to reduce at exactly {2,3}; the
  denominator is 6 = 2·3.
- **K4 answered YES on the arithmetic.** The formula-vs-brute-force validation
  reproduces at all three cells: 16/16, 18/18, 4/4. The ambiguity sets are
  **whole given their stated constraints**: 2 candidates for base 1 (all giving
  |⟨W,D⟩| = 4) and 864 for base S (= the (ord 2, 45 fixed) class in my own
  classification). Probes P19/P20 confirm G04 fires when either constraint is
  loosened or changed. See MINOR-2 and MINOR-3 for the two qualifications.
- **K5(c) answered.** Both reachability mutants reconstructed and traced:
  `found-block` drops the synthetic target to order 2 so ℤ/3 admits only the
  trivial map → dies at G21 (also G22, G24, G31); `empty-block` sets the
  incompatible source prime to 3, making it compatible with the order-6 target
  (3 homs, 2 non-trivial) → dies at G25 (also G31). Each outcome is genuinely
  reachable and each falsifier dies at its own gate.
- **K5 prime-tracking quarantine reproduced.** F3 survives at {5,7} and dies at
  {11,13,17,19,23}; my independent scope-2 census puts the live cells at exactly
  those primes, so G13's measured coincidence is real, and A77 anchors it
  against HA. G14's intersection reading holds at every instance of both scopes.
- **K5(g) SP teeth reproduced exactly.** Non-hom rejected at **10 of 25**
  composition cells. BREAK-A rejected at **2,500 of 3,125** equivariance cells
  **while the same carrier map with φ: R ↦ R² is accepted at 0 of 3,125** — the
  φ-swap acceptance is real, and I verified the mechanism analytically (2g ≡ g
  mod 5 only at g = 0).

The verdict `BRG-EMPTY-AT-CARRIER` is, in my judgement, **correct and correctly
scoped**. Every finding below is an instrument finding. **No number moves.**

---

## FINDINGS, most severe first

### MAJOR-1 — The verdict's qualifier table is ungated, and one of its counts is typed

**Evidence.** G31's predicate is `verdict == recomputed and verdict in
DECL["outcomes"][:2]`. The `qualifiers` dict is passed as *detail* only; no
clause of any gate reads any of its values. Probe **P11** replaced
`"instances": len(rows1)` with `"instances": 999`:

```
exit=0   gate-FAILs=-   VERDICT: BRG-EMPTY-AT-CARRIER
OUT>       instances                                    999
RECEIPT verdict_qualifiers: {... "instances": 999 ...}
```

All 31 gates PASS, and the corrupted qualifier is printed directly under the
`VERDICT:` line and written verbatim into `receipt.tables.verdict_qualifiers`.
Probe **P10** did the same for `prime_tracking_candidates_excluded` (set to 99)
with the same result. Separately, `"prime_tracking_candidates_excluded": 1` is a
**hard-typed literal** in the source — a count that is typed, not computed
(RUNBOOK §4, failure #24).

**Why it matters.** §10's qualifier table *is* the paper's scope statement for
the verdict — "primes 7 / instances 8 / directed cells 112 / …". RUNBOOK §13
addendum #234 put the verdict string inside a gate precisely so it could not be
"a typo away from fiction"; the eleven qualifiers that scope that string sit
outside every gate.

**Repair.** Fold the qualifiers into G31's predicate, each recomputed inside the
gate from its own source — e.g. `qualifiers["instances"] ==
len({c["instance"] for c in cells1})`, `qualifiers["directed_cells"] ==
2*len(cells1)`, `qualifiers["completion_family_members"] == fam_cells` — and
derive the excluded-candidate count by counting the declared functors whose
declaration carries the prime-tracking marker instead of typing 1:

```python
prime_tracking_candidates_excluded = sum(
    1 for v in DECL["functors"].values() if "PRIME-TRACKING" in v)
```

Add a declared `qualifier-typo` mutant that perturbs one qualifier and must die
at G31.

---

### MAJOR-2 — G31's "independent expression" shares all five inputs; a one-line corruption of a shared input flips the printed verdict at exit 0

**Evidence.** `derive_verdict(...)` and the inline `recomputed` expression are
algebraic rewrites of the same boolean formula over the same five variables
(`empty_everywhere`, `complete`, `invariant`, `g21`, `g25`). Probe **P8**
inverted one shared input at one line:

```python
empty_everywhere = not (nt_fwd1 == 0 and nt_rev1 == 0)
```

Result: **exit 0, all 31 gates PASS, `VERDICT: BRG-MORPHISM-FOUND`** — while §8's
own printed table in the same output still reports 0 non-degenerate morphisms at
all 56 cells and G26 still reports 137 empty / 3 live. The receipt is internally
contradictory and the run exits clean. Probe **P9** (hand-typing `recomputed` to
a constant) also survives at exit 0.

The declared `verdict-flip` mutant corrupts *inside* `derive_verdict`, which is
the one and only place the mirror expression can see. So the mutant table proves
exactly the narrowest thing the design can prove.

**Why it matters.** §10 says the verdict is "recomputed there by an independent
expression over the same counts which must agree — so a hand-typed verdict
cannot survive". That is true of a hand-typed *verdict* and false of a corrupted
*input*; "independent" is doing work the expression does not do.

**Repair.** (a) Give G31 a genuinely independent leg by re-deriving the counts
inside the gate from the cell tables rather than reusing the cached scalars:

```python
recount_fwd = sum(c["nontrivial_forward"] for c in cells1)
recount_rev = sum(c["nontrivial_reverse"] for c in cells1)
# gate clause: (verdict == "BRG-EMPTY-AT-CARRIER") == (recount_fwd == 0 and recount_rev == 0)
```

(b) Add a declared `count-flip` mutant that corrupts `empty_everywhere` and must
die at G31. (c) Replace the §10 sentence verbatim with:

> derived **inside gate G31** from the measured counts, and cross-checked there
> against a second expression over the same five booleans together with a
> re-summation of the non-trivial-morphism counts taken directly from the cell
> tables — so neither a hand-typed verdict nor a corrupted count survives.

---

### MAJOR-3 — The §14 symmetry self-tests (G15) measure a quantity the arena action cannot move, and one leg never consumes its arena at all

**Evidence, leg 1 (the three action self-tests).** All four self-tests read the
acceptance verdict of the **degenerate** functor (`deg_phi`, `deg_Phi`). The
receipt records `verdict: false` for all four. But NT1
(`any(v != tgt_identity …)`) and NT2 (`len(set(Phi)) > 1`) are label-independent
by construction: a constant Φ stays constant under any relabelling of either
carrier, and a trivial φ stays trivial under any conjugation. The verdict is
therefore **False identically**, and its invariance is analytically forced.

Probes confirm the vacuity:

| probe | change | result |
|---|---|---|
| **Q2** | the source relabelling applied *wrongly* (`rl` for `pinv(rl)`) | exit 0, **G15 PASS** |
| **Q5** | conjugation by a different carrier permutation | exit 0, **G15 PASS** |
| **Q3** | one self-test verdict forced to flip (positive control) | exit 1, **G15 FAIL** |

Q3 shows the `matches_base` clause is wired; Q2 and Q5 show that nothing the
arena action actually does can trip it.

**Evidence, leg 2 (the generator sweep) — this one is strictly vacuous.** The
loop builds `gen2 = perm_pow(gen0, j, fresh=True)` and an `arena` from it, and
then **never uses either**:

```python
gen2 = perm_pow(gen0, j, fresh=True)
arena = make_cyclic_arena(p0, src0["npts"], gen2, fresh=True)   # discarded
els, mul, e = dihedral_abstract(2)
inv_counts.append(homs_route_a(p0, els, mul, e))                # depends on (p0, 2) only
```

The receipt records `generator_change_counts: [1, 1, 1, 1]` — four copies of one
constant that no generator change can move. Probe **Q1** replaced the swept
generators with the **identity permutation**: exit 0, G15 PASS.

Note also that the declared mutants `relabel-lax` and `conj-lax` kill G15
through the `all(v > 0 for v in moved.values())` clause — i.e. through "did the
declared action move any points", not through the invariance measurement. **No
declared mutant falsifies `matches_base`.**

**Why it matters.** RUNBOOK §14 requires an instrument enforcing a
symmetry-invariant quantity to "carry a self-test that measures the quantity's
invariance under the symmetry's own action"; §36/#36 requires every gate to be
"a measurement that could have come out otherwise". §6 of the paper states the
self-tests as though the census's verdict and counts were put at risk under the
arena action. They were not.

**Repair.** (a) Run the three action self-tests on an **accepted, non-degenerate**
candidate — the identity self-morphism of §7, or G07's accepted pair
(the register doubling with φ: R ↦ R²) — transported consistently through each
action, so the verdict genuinely could move; keep the degenerate candidate as a
second row. (b) Make the generator-change leg consume its arena: recompute the
committed-scope census cell under `R → R^j` against `arena`, not a constant.
(c) Add a declared `selftest-blind` mutant that mis-applies one action and must
die at G15's invariance clause specifically. (d) Replace the §6 sentence with
one that says what is measured, e.g.:

> The predicate's verdict is measured invariant under the arena's own action —
> relabelling either carrier, conjugating the transport action, and replacing the
> source generator by `R^j` — on an accepted non-degenerate candidate and on the
> degenerate one alike, with the census cell recomputed inside each relabelled
> arena.

---

### MAJOR-4 — The functor-level census (35 cells) has no cell-completeness gate

**Evidence.** G17's predicate is `orb_ok and len(functor_rows) > 0`. That is the
only gate the 35-cell scope has.

| probe | change | result |
|---|---|---|
| **P5** | one of the 35 functor cells dropped | exit 0, all gates PASS |
| **P6** | **34 of 35 dropped** (one cell survives) | exit 0, all gates PASS, verdict unchanged |

§5 claims the count is "computed exactly as an integer at each of **35** cells".
Nothing enforces 35. RUNBOOK §13 addendum #234 requires that "a cell-completeness
gate must catch a dropped cell", and the unit's other three scopes do — I
verified each with an *interior* dropped-cell probe that preserves the visit
count:

| probe | scope | result |
|---|---|---|
| **P1** | scope-1 interior cell swapped (56 visits, 55 distinct) | exit 1, **G09/G11/G31 FAIL** |
| **P2** | scope-2 interior class swapped (84 visits, 83 distinct) | exit 1, **G11/G31 FAIL** |
| **P3** | family sweep: one member twice, one dropped | exit 1, **G02 FAIL + anchor A21/A22** |
| **P4** | one of the 504 spectrum cells dropped | exit 1, **G19/G31 FAIL** |

So four of the five declared scopes are genuinely gated and the fifth is not.

**Consequence bounded.** `nondeg_total` is 0 and cannot move under a cell drop,
so no published number changes — this is a missing gate, not a wrong result.

**Repair.** Extend G17:

```python
expect_f = len(primes) * len(perm_orders)
g17 = gate("G17", "... and the cell count is computed from the declared sets ...",
           orb_ok and len(functor_rows) == expect_f
           and len({(r["p"], r["instance"]) for r in functor_rows}) == expect_f,
           {...})
```

and declare a `functor-cell-drop` mutant. The same applies, more weakly, to the
tiny-cell set: probe **P7** dropped TINY-B and survived at exit 0 (G18's
predicate is satisfied by any two cells straddling the nd > 0 / nd = 0 line), so
`len(tiny_rows) == len(DECL["tiny_cells"])` should be added too.

---

### MINOR-1 — The held-out verification cannot discriminate among rotation-valued extensions; E-ROT's pass is analytically forced

**Evidence.** I rebuilt the whole construction independently and reproduced it
exactly: **27 orbits, FIT = 1 orbit / 3 points touched, HELD = 26 orbits / 234
cells, E-ROT 0 violations, E-REF 54 violations.** I then re-ran the construction
under five different rotation rules:

| extension rule | E-ROT violations / 234 | E-REF violations / 234 |
|---|---|---|
| the declared `(δ₀ + 2δ₁ + c) mod 3` | **0** | **54** |
| the constant `0` | **0** | **54** |
| `(2δ₀ + δ₁ + 2c) mod 3` | **0** | **54** |
| `δ₀ mod 3` | **0** | **54** |
| `(7δ₀ + 5c) mod 3` | **0** | **54** |

In-source probes agree: **P16** (a different rotation rule) and **P17** (the rule
replaced by the constant 0) both leave exit 0 with every gate passing.

**Mechanism.** With `t = D^r` the held-out equation is
`D^r·D^{j+g}·y₀ = D^g·D^r·D^j·y₀` — an identity in the abelian ⟨D⟩ for *any* r.
With `t = W·D^r` it fails exactly when `D^{2g} ≠ e`, i.e. at 2 of 3 g-values on
each of the 9 reflection-valued held orbits: 9 × 3 × 2 = **54**. Both numbers are
forced by the group law, not by the fit.

**What survives.** The bookkeeping is honest — the construction really does touch
only 3 points, and probe **P18** (moving y₀ off a free D-orbit) correctly kills
G21/G22, so the gate is not inert. And G22's contrast is a genuine two-sided
control. What the 234 cells do *not* do is test the declared extension rule:
the check discriminates rotation-valued from reflection-valued extensions and is
blind to which rotation is declared. Under RUNBOOK §14 addendum #208, an
analytically-forced clause is a disclosure.

**Repair.** Add a disclosure and rescope two sentences. Replace §2.5's
"Equivariance on the HELD orbits is therefore a **prediction**, not an
imposition." with:

> Equivariance on the HELD orbits is therefore verified, not imposed; what it
> discriminates is the rotation-valued extension from the reflection-valued one,
> and it is insensitive to which rotation rule is declared (measured: 0
> violations under every rotation rule swept, 54 under every reflection-valued
> one).

and add:

> **X07** — For a rotation-valued extension the held-out equations hold
> identically, because ⟨D⟩ is abelian; the 234-cell check is therefore a
> two-valued measurement (rotation vs reflection) rather than a test of the
> declared extension formula. Measured under five rotation rules and five
> reflection rules.

---

### MINOR-2 — TINY-A is mis-declared, and the brute-force validation set does not cover the formula's hypothesis

**Evidence.** `tinies = [("TINY-A", 2, 4, 2, 4), …]` builds the source generator
as `[(i + 1) % 4]` — a **4-cycle** — while declaring p = 2. I measured
`gen_order = 4`. So DECL's "source Z/2 acting freely on 4 points" and §5's table
row "Z/2 on 4 points" describe an object the code does not build: ℤ/2 does not
act at all (act(1, act(1, x)) ≠ x), and the orbit count is 1, not the 2 that a
free ℤ/2 action on 4 points would give.

The numbers are nevertheless right *for what is built* (16 = 16, independently
reproduced) — because every element of the Klein-four target with g² = e also
satisfies g⁴ = e. The agreement is accidental.

**The hypothesis is real.** The formula `|C_TR|^{#orbits}` per group map is valid
only when the source action is a genuine free ℤ/p action. I built the
counterexample — p = 2, generator a 3-cycle on 3 points, target D₃ regular on 6:

> **formula 24, brute force 6.**

So a cell whose source generator's order differs from p *does* break the formula,
and TINY-A is exactly such a cell yet passes.

**Consequence bounded.** In the committed census the source action IS free —
translation by ρ ≢ 0 — and G17 measures the orbit count twice (union-find and
n_src/p) and gets p³ at every cell. §5's use of the formula is sound; only the
validation set is under-covering.

**Repair.** Either fix TINY-A to a genuine free ℤ/2 action on 4 points
(generator `(0 1)(2 3)`; formula and brute force then both become 64), or
relabel the row honestly and add a fourth tiny cell whose source generator's
order differs from p, so the validation set contains a case the formula gets
wrong and the brute force catches. Correct §5's TINY-A row either way.

---

### MINOR-3 — Two committed numbers defining the ambiguity sets are typed, not read and anchored

**Evidence.** The base-1 ambiguity set is filtered by
`pfixed(tensor(dd, pident(9))) == 18` and the base-S set by
`fam_class[tuple(q)] == (2, 45)`. Both constraint values are **typed literals**.
Both are *correct* — I located them at
`XBA.tables.bases["base 1 @ SP-E"].D_fixed = 18` and
`XBA.tables.third_instances["base S"].D_fixed = 45` — but **none of the 77
anchors ties either constraint to those fields**, so a change in XBA would send
the sweep silently to the wrong class. `len(amb_S) == 864` in G04 is likewise a
typed literal.

RUNBOOK §4: "every committed number a unit reuses gets an assertion that kills
the run loudly on mismatch"; "counts must be computed, never typed".

**This does not touch K4's answer.** The sets are whole *given* those
constraints — 2 and 864, both independently reproduced, both with invariant
group order 4 — and probes **P19** (base S widened to defect order only) and
**P20** (base 1's constraint changed 18 → 12) both kill G04. It is a provenance
finding, not a numerical one.

**Repair.** Read both values from the pinned XBA receipt and anchor them exit-1
alongside A33–A40; compute 864 from the family classification
(`sum(1 for q in fam if fam_class[tuple(q)] == (2, base_S_fixed))`) rather than
typing it into the gate.

---

### MINOR-4 — Small typed values inside gate details

`G09`'s detail carries `"directions": 2` and `G14`'s carries
`"instances_admitting_EVERY_declared_prime": 0` — both typed; G14's gate
*predicate* does compute the corresponding boolean, but the number it reports
does not come from the computation. G09's predicate also compares the computed
`expect1` against a typed `7 * 8`; that literal is load-bearing (it is what makes
`cell-drop` die), which is a legitimate declared-scope assertion, but §4's
sentence "the cell count is COMPUTED from the declared sets" should add "and is
asserted against the declared scope constant". Report the computed values.

---

## NOTES

**NOTE-1 — The two forward census routes are one criterion computed twice; the
reverse pair earns the word, the forward pair does not.**
Route A tests `g^p = e`; route B builds each element's cyclic span and keeps
spans with `p % |S| == 0`. These are the same predicate `ord(g) | p` via a
definitional identity, over a **shared group model** — #234's "a pair related by
an algebraic identity is one route" applies in the letter. That said, the
dropped-cell probes the protocol asks for come out well:

| probe | change | result |
|---|---|---|
| **P13** | forward route A only (off-by-one power) | exit 1, **G10 FAIL** |
| **P14** | forward route B only (divisibility reversed) | exit 1, **G10 FAIL** |
| **P15** | reverse route A only (one generator dropped) | exit 1, **G10 + G27 FAIL** |

So the pair has real *implementation* independence and catches a single-route
error in either direction. The residual shared dependency is the group model
itself: **P12**, corrupting `dihedral_abstract`'s `mul`, is not caught by G10
(both routes consume it). But **P22** — replacing D_n by the cyclic group ℤ/2n
of the *same order* — **is** caught, by G27's abelianisation clause. So the
shared-model risk is covered, by a different gate. Recommend §4 say so rather
than claim an independence the forward pair does not have: "two implementations
of the count, agreeing at every cell, with the group model itself audited at
G27" is the accurate sentence. The reverse pair (word evaluation in G vs.
construction of the abelianisation and its own quotient table) is genuinely two
different computations and needs no rewording.

**NOTE-2 — `sys.set_int_max_str_digits` verified: a no-op, with no precision
effect (K5(i) answered).** I removed the line and re-ran: output lines 1–240 are
**byte-identical** to the committed `brg_bridge_output.txt` (the only difference
is the mutant-harness section my probe stubs out). Nothing in the run stringifies
an integer above the 4,300-digit default — the functor counts are reported via
`.bit_length()` (793 to 97,337 bits, both reproduced) and the largest
string-formatted integer is the 42-digit dictionary space. Deviation 5's claim
("this raises a printing limit, never a precision one; the arithmetic is exact
integer arithmetic throughout") is **correct**, and the AST float scanner
(validated by its synthetic injection, G28) confirms no float or complex literal
and no `float()`/`complex()` call anywhere in the source. Optional tidy: the line
can be deleted, or the deviation reworded to say the raise is precautionary.

**NOTE-3 — Two cache figures appear in the receipt.** `G16.detail.cache` records
`lookups 100 / hits 5 / bypass 35 / selftest_hits 0` (the gate-time snapshot,
which is what §6 quotes, correctly), while `tables.cache` records the end-of-run
`lookups 118 / hits 10 / bypass 35 / selftest_hits 0`. Not an error; worth a
one-clause note in §6 so a reader comparing the two is not misled.

---

## Scope of this review

I did not re-derive the physics: HA's, NT's, GEN's and XBA's own results are
taken as given and were checked only where BRG reproduces them (all 77 anchors).
K2's live-cell feasibility question and the prose-strength audits of K1 and K3
belong to the operator and effectus lenses; I touched them only far enough to
confirm the numbers. Nothing in this review disputes the verdict.

---

## Summary table

| # | severity | finding | number moved? |
|---|---|---|---|
| MAJOR-1 | MAJOR | verdict qualifiers ungated; one count typed | no |
| MAJOR-2 | MAJOR | G31's "independent expression" shares all inputs; P8 flips the verdict at exit 0 | no |
| MAJOR-3 | MAJOR | G15's self-tests measure a forced-constant quantity; the generator leg discards its arena | no |
| MAJOR-4 | MAJOR | the 35-cell functor census has no cell-completeness gate | no |
| MINOR-1 | MINOR | held-out check is blind to the rotation rule; E-ROT's pass is forced | no |
| MINOR-2 | MINOR | TINY-A mis-declared; validation set misses the formula's hypothesis | no |
| MINOR-3 | MINOR | ambiguity-set constraints (18, 45, 864) typed, not anchored | no |
| MINOR-4 | MINOR | typed values in G09/G14 details | no |
| NOTE-1 | NOTE | forward "two routes" are one criterion; shared model covered by G27 | no |
| NOTE-2 | NOTE | int-str limit is a verified no-op, no precision effect | no |
| NOTE-3 | NOTE | two cache figures in the receipt | no |

Four MAJOR findings, all instrument-side: three gates that cannot fail on the
account they advertise (G15 both legs, the absent functor cell-completeness
gate, the ungated qualifier table) and one claim of independence the instrument
does not have (G31). Every one is repairable by a local, mechanical fix plus a
scope sentence. **No published number is wrong; the verdict stands.** The unit's
arithmetic survived 152 independent recomputations without a single discrepancy,
and its five hash pins, its four scoped cell-completeness gates, its SP-predicate
teeth, its φ-swap acceptance, its reachability mutants and its E-REF teeth all
behaved exactly as advertised under adversarial probing.

---

# GRADE: ACCEPT-WITH-FIXES
