# CYCLE B″ HOSTILE REVIEW — R1, OPERATOR LENS

**Reviewer:** R1 (operator lens). **Primaries:** K2 (joint
unforgeability) and K3 (the cost tower). **Protocol:**
`v13/note-rq0-admissibility-hostile-protocol.md` @ `e5144d4`, frozen
before dispatch; this review is judged against that protocol only.

**Object, SHA-verified against the frozen pin (all four match):**

| artifact | frozen prefix | recomputed |
|---|---|---|
| `v13/paper-rq0-generative-admissibility.md` | `d08a761081a7` | `d08a761081a7e2d8…` ✓ |
| `v13/code/rq0_l2_admissibility_exact.py` | `c81f7f5530d1` | `c81f7f5530d1fd49…` ✓ |
| `v13/code/rq0_l2_admissibility_output.txt` | `4e2c7bf5e5fe` | `4e2c7bf5e5fea81b…` ✓ |
| `v13/code/rq0_l2_admissibility_receipt.json` | `dfd4f9435fd9` | `dfd4f9435fd909b5…` ✓ |

**Method.** Own exact code in a separate scratchpad, nothing imported
from the unit; every object rebuilt from the paper's own Definitions
2.1, 2.2, 4.1, 4.2 and 8.1 as written (partitions, sector supports,
composition, `comp`, `Pres`, `ker`, `Reach`, the four clauses, the
committed families DET/FUNNEL/REV/ALL and the counter-law regenerated
from Cycle B′'s stated algorithm). Exact arithmetic throughout;
`fractions.Fraction` for the tester statistics; no float anywhere.
**33 independent recomputations**, listed in §5.

---

## VERDICT

$$\boxed{\textbf{ACCEPT-WITH-FIXES}}$$

Both registered rungs — `RQ0-L2-GENERATIVE-ATLAS-AXIOM` and
`RQ0-L2-BLOCKED-AT-CARRIER` — are **earned at the declared scope**, and
both honest negatives (`EMPIRICALLY-IDLE`, `CHEAP-LAW-FORGERY`) are
correctly *not* occurring. **Every number the paper states reproduces
by my independent route** — the tower 120/360/1260/3120, the remainders
3005/2765/1865/5, the 240-member closure, σ = 1 vs 3/4, δ = 0 vs 1/16,
the 16 rigidity sweeps, the zero covariance violations, the minimal
witness's clause pattern, and all 45 anchors I sampled. I found **no
false computed number**.

I did find **one false theorem**. Theorem 8.3 (`c = |Obs|`) is stated
for every admitted law and is refuted inside the paper's own committed
law families. The fix is a hypothesis and two sentences; the delivered
tower is unaffected because it runs entirely under DET, where the
hypothesis holds. Theorem 6.1 is *true as literally stated* but is
missing a hypothesis the pin's own scope line makes load-bearing.

**Fixes MAJOR-1, MAJOR-2 and MAJOR-3 are blocking.** If the
adjudication applies the corpus's "no false theorem" line strictly,
MAJOR-1 is REJECT-grade until repaired; I grade ACCEPT-WITH-FIXES
because the repair is local, the instantiated results survive it
untouched, and the paper's own measured guard (`boundary_admissible_
after`) already computes the missing condition — it is simply not in
the theorem.

---

## 1. K3 — THE COST TOWER (primary)

### 1.1 What re-proves cleanly

**The lower bound is sound and fully general.** If `F ∈ Obs(L,π)`
survives in `L̃`, then `F ∈ Pres_L̃(π)` — membership in `Pres` depends
only on `comp(F)`, which is intrinsic to `F` and cannot be changed by
anything else in `L̃` — and `F` separates some `x,y` inside a block of
`π`, so `ker(Pres_L̃(π))` separates them and (i-a) fails. Hence every
member of the obstruction must be deleted, so
`|L △ L̃| ≥ |Obs(L,π)|` **for every** `L̃`, additions included. The
paper's "no addition ever removes one" is correct and is exactly this.

**Lemma 8.2 re-proves.** The paper's argument (a composite lies in the
obstruction only if its right factor does) is right. I found **zero**
closure failures over 687 genuine composition-closed laws at n = 3 and
over DET/REV/ALL at n = 3, 4. One scope gap: the proof is written in
*fibre* language, i.e. for deterministic maps, while Definition 2.1
admits arbitrary left-total relations (the declared ALL family). It
does generalize — if `sup_g(x) = sup_g(y)` then `sup_h(x) = sup_h(y)`,
so `h` separating `x,y` forces `g` to; and any `l ∈ sup_g(x) ∩ sup_g(y)`
puts the non-empty `sup_f(l)` inside both `sup_h(x)` and `sup_h(y)`, so
`comp(g)` refines `comp(h)` refines `π` — but the relational argument
is not the one given (MINOR-8).

**The tower numbers are right, by two independent routes.** Deletions
120 / 360 / 1260 / 3120 and remainders 3005 / 2765 / 1865 / 5, plus the
240-member declared family of member one. My second route is closed-form
combinatorics: `|Pres_DET({01|2|3|4})| = 120 + 120 = 240` (injective, or
exactly the fibre `{0,1}`); `|Pres_DET({0123|4})| = Σ_g (5 − |im g|) =
20·4 + 140·3 + 360·2 + 120·1 = 1280`, obstruction `1280 − 20 = 1260`;
the limit `3125 − 5 = 3120` with the five constant maps remaining, and
those five are composition-closed and do admit the indiscrete boundary.

### 1.2 MAJOR-1 — Theorem 8.3 is false as stated

> `c(B,L) = |Obs(L,A(B))|` — stated for an arbitrary admitted law `L`,
> tagged `[FIN]`, `[EXH-4]`.

**It is refuted by REV, a committed law family, at every non-discrete
boundary in the very range the `[EXH-4]` tag advertises.**

Take `X = {0,1,2}`, `L = REV₃` (all six permutations), `π = {01|2}`.
Every permutation is collision-free, so `comp` is discrete, so
`Pres_L(π) = L`; every permutation separates 0 from 1; therefore
`Obs = L` and `|Obs| = 6`. The complement is **empty**. The empty family
fails (i-a) — `ker(∅)` is the one-atom boundary by the paper's own
convention, not `{01|2}` — and fails (ii-b), and fails the code's
(ii-a). So the boundary is *not* admissible in the complement, and no
`L̃` at distance 6 exists (distance 6 forces `L̃ = ∅`). The cheapest
forgery is **7**: delete all six permutations and **add** the idempotent
`a = (0,0,2)`, under which `{a}` is composition-closed, `Pres = {a}`,
`ker({a}) = {01|2}`, `comp(a) = {01|2}` and reach is full. I verified
this by brute force over all candidate laws of size ≤ 2 drawn from the
full left-total relation family at n = 3.

This is not an isolated pathology. Under REV the obstruction is *all of
REV* for **every** non-discrete boundary, so the true cost is `n! + 1`
via the block-minimum idempotent — **6 → 7 at n = 3 (4 boundaries),
24 → 25 at n = 4 (14 boundaries)**: 18 counterexamples inside the
declared `[EXH-4]` range.

**A second, sharper failure mode: `|Obs|` can be zero for a boundary
that is inadmissible at any price.** Take `L = {const₀}` at n = 3 and
`π = {0|12}`. The images of the two blocks are `{0}` and `{0}` — not
disjoint — so `Pres_L(π) = ∅`, so `Obs = ∅` and Theorem 8.3 returns
`c = 0`, i.e. *already admissible*. It is not: with an empty declared
family (i-a) fails. The true cost is 2 (delete `const₀`, add
`(0,1,1)`). Obs sees only one of the four ways to fail — over-separation
inside a block — and is blind to under-separation between blocks (the
decision procedure's own second witness branch, "two blocks are left
undistinguished by every declared task"), to (ii-a) and to (ii-b).

**Census.** Over 687 genuine composition-closed laws at n = 3 (every law
generated by ≤ 3 deterministic maps) × 4 non-discrete boundaries =
2748 pairs, the complement fails to admit the boundary in **1008**
cases; 927 of them have a non-empty complement, so this is not an
artefact of emptiness. **DET is clean** — 0 failures at n = 3, 4, which
is why the delivered tower is safe — and so is ALL at n = 3.

**Repair (blocking).** Restate as a bound plus a hypothesis:

> **Theorem 8.3.** `c(B,L) ≥ |Obs(L,A(B))|` always. If the patch
> `(B, Pres_{L∖Obs}(A(B)), L∖Obs, X)` is admissible, then
> `c(B,L) = |Obs(L,A(B))|` and no alteration using an addition is ever
> cheaper. Under DET the hypothesis holds at every non-discrete
> boundary at three and four configurations and at all four levels of
> the tower at five — measured. It can fail: under REV the complement
> is empty and the cheapest forgery is `|REV| + 1`, one addition
> included.

Note the unit's code **already computes the missing condition** —
`forging_cost` returns `boundary_admissible_after`, and gate L2-16
requires it — so this is a paper-side repair, not a re-run. But
`forging_cost` returns `"cost": len(O)` unconditionally, i.e. it would
report a wrong cost with a `False` flag beside it if ever pointed at a
law outside DET; the guard is in the gate, not in the function.

### 1.3 MAJOR-2 — the upper-bound step of the proof does not hold

> "Upper bound: Lemma 8.2 exhibits the complement as a law in which the
> boundary is admissible."

Lemma 8.2 exhibits the complement as **composition-closed**. It says
nothing whatever about the boundary being admissible in it — that is a
separate four-clause condition, measured (DET only) and never proved.
This sentence is the exact hole MAJOR-1 enters through, and it is the
one place in the paper where a measured fact is presented as carried by
a proved lemma. Rewrite as: "Upper bound: Lemma 8.2 exhibits the
complement as a law; that the boundary is admissible in it is a
separate condition, which is the theorem's hypothesis and is measured
here for DET at the declared scope."

### 1.4 MODERATE-4 — gate L2-17 does not test its claim

The gate asserts "every member of the obstruction must be deleted —
each one alone makes the declared boundary strictly coarser … checked
here on the first forty members at each level". The code is

```python
fam = [G for G in P if key(G) != key(F)] + [F]
if ker_of_family(fam, n) == part: each_alone = False
```

`fam` removes `F` from `Pres(π)` and immediately appends it: as a set
`fam == P` for every `F`, and `ker_of_family` sorts its input, so the
loop body is **constant in `F`**. The gate re-checks
`ker(Pres(π)) ≠ π` forty times per level and never tests "each one
alone". I verified that the *intended* claim is nevertheless true, on
**all** 120 / 360 / 1260 / 3120 members at the four levels (family =
complement + `{F}`), so no result is false — but the gate is
decorative, and the "first forty members" clause has no place inside a
proof whose argument is general in one line.

### 1.5 MODERATE-6 — "no forgery at any price inside the committed class"

The claim is right and the wording undersells it. The paper derives it
from "every obstruction computed here contains the identity" — measured,
level by level, boundary by boundary. It is a **one-line corollary of
Theorem 3.1**, general over all laws: `comp(id)` is discrete, which
refines every `π`, so `id ∈ Pres_L(π)`; `id` separates every pair, so
`id ∈ Obs(L,π)` whenever `π` is non-discrete; hence *any* admissible
altered law must delete the identity. Two consequences for the prose:
the "committed class" that is actually proved closed to forgery is **the
class of identity-containing laws**, which is larger than the five named
families; and the sentence should not read as a fact about the levels
swept. (I confirmed identity ∈ Obs over DET and REV, all non-discrete
boundaries, n = 3, 4.)

### 1.6 MODERATE-7 — the patch is a triple that needs four components

Definition 2.1 says a patch is a triple `(B, 𝔉, L)`, but clause (ii-b)
and Definition 4.2 both require a declared preparation `X₀`, and
Theorem 4.3's separating witness W3 differs from W1 *only* in `X₀`.
Definition 8.1 then writes the forged patch as a triple with no
preparation at all, while the code silently supplies `X₀ = X`. Either
declare the patch a quadruple or fix `X₀ = X` explicitly in
Definition 8.1.

---

## 2. K2 — JOINT UNFORGEABILITY (primary)

### 2.1 The inclusion, and the quantifier it is valid at

`Pres_L(δ) ⊆ Pres_L(π₁)` **holds for every law `L`, unconditionally and
for a reason stronger than the paper gives**: `δ` is the bottom of the
record lattice, so `comp(F)` refining `δ` forces `comp(F) = δ`, which
refines everything. There is **no escape law** — the inclusion cannot
fail for any `L`, any carrier, any pair with `δ` on the fine side. I
searched for one and can state that the search is unnecessary: the
inclusion is a lattice fact, not a law-dependent one.

**Theorem 6.1's proof is valid at the "single shared `L`" quantifier**
and I re-derived it: member one admissible ⟹ (i-b) gives
`𝔉₁ = Pres_L(π₁)` and (i-a) gives `ker(Pres_L(π₁)) = π₁`, so no member
of `Pres_L(π₁)` separates 0 from 1; a fortiori none of the subset
`Pres_L(δ)` does; so `ker(Pres_L(δ))` merges 0 and 1 and member two
fails (i-a) — and if member two's declared family is anything other
than `Pres_L(δ)` it fails (i-b) instead. Sound.

**Free strengthening (MINOR-11).** The argument never uses that `δ` is
discrete, only that `π ≺ π₁` strictly. The true theorem is: *under one
law, no two strictly comparable boundaries are ever both admissible.*
Measured over the 687-law census at n = 3: 277 laws have more than one
admissible boundary, 357 unordered admissible pairs occur, and **zero**
are comparable. Theorem 6.1 is the `δ` case of a sharper result the
cycle already owns.

### 2.2 MAJOR-3 — the missing hypothesis, with the escape constructed

The abstract says "**no admitted law whatsoever** makes both members
admissible"; §6.1's gate says "There is no law, at any cost, in which
both members of the colluding pair are admissible". Both quantify over
**one** law shared by the two contexts. But the pin's scope line and the
paper's own scope box say: **"one law family per context, declared."**
Under the paper's own declared scope the adversary may declare a law per
context — and then the pair *is* forgeable:

- **Member one** — boundary `π₁ = {01|2|3|4}`, the aligned manufactured
  2+1+1 context — under `L₁ = {a}` with `a = (0,0,2,3,4)`:
  composition-closed (`a∘a = a`, measured), **identity-free**,
  `Pres_{L₁}(π₁) = {a}`, `ker({a}) = {01|2|3|4} = π₁`,
  `comp(a) = π₁`, reach full. **All four clauses pass: ADMISSIBLE.**
- **Member two** — the discrete boundary — under `L₂ = DET`: the
  120-member reversible closure, all four clauses pass, exactly as §6.3
  reports. **ADMISSIBLE.**

So the adversary who declares both contexts *and their laws* — which
is precisely the predecessor's adversary, one level up — holds two
admissible patches. Theorem 6.1's protection is carried entirely by the
shared-law hypothesis, which appears nowhere in the theorem, the
abstract, the gate text, or the verdict section.

This does **not** overturn the theorem: at a common declared law the
result stands, and I confirmed member one inadmissible / member two
admissible under all four committed laws (DET, FUNNEL, REV,
counter-law) and the `(True, False)` flip on the altered 3005-operation
law. What it overturns is the *wording*. Required fix, blocking:

> **Theorem 6.1.** There is no admitted law under which both members of
> the colluding pair are admissible **when both contexts declare the
> same law.**

plus a disclosure sentence in §6.1 and in the abstract naming the
escape: *if each context may declare its own law, member one is
admissible under the identity-free law `{(0,0,2,3,4)}` while member two
is admissible under DET, and the axiom rejects neither; joint
unforgeability is a statement about one law, not about one adversary.*
Whether the predecessor's record-descent attack still runs at `L₁` is a
separate question this cycle has not measured, and the disclosure should
say so rather than guess.

### 2.3 Does the measured verification support "no admitted law whatsoever"?

Not by itself — the measurement covers four committed laws plus the
altered law, five in all, against a claim quantified over every
composition-closed subset of the ALL family at five configurations. The
universal is carried by the **proof**, which is valid. That is
sufficient, but the gate text should say the universal is proved and
the five laws are a check, not the evidence (MINOR-10).

---

## 3. COMMON GATES

- **Paper-vs-receipt sweep (≥ 10).** 33 recomputations in §5; every
  paper number I checked appears in the receipt with the same value
  (tower 120/360/1260/3120, remainders, `Pres_discrete_subset_of_Pres_
  forged: true`, `after_paying…member_2_admissible: false`, 21/21 gates
  passed, 45 anchors, σ and δ as exact rationals). No paper/receipt
  divergence found.
- **Scope tags.** Correct in kind, wrong in one particular: Lemma 8.2
  and Theorem 8.3 carry `[EXH-4]` and the prose says "exhaustively over
  every non-discrete boundary at three and four configurations" — but
  the sweep is **DET only** (`law_det(m)` in `run_cost`), 18 rows, and
  the receipt's `cost_scaling` rows carry no `law` field at all, so the
  restriction is recorded nowhere in the artifacts (MINOR-12). Name the
  law in the prose and add the field.
- **Forbidden vocabulary / no-spacetime line.** Clean. The
  reachability scope line holds in the scope box, Definition 4.2, §10
  and the code's `reach_of` docstring. No locality, region, cone,
  history, causal or spacetime reading anywhere in the cost or
  unforgeability sections. "Atlas" is disclaimed as the programme's
  target in both the scope box and §10.
- **Prose vs gates.** One overstatement (MAJOR-2), one gate that does
  not test its claim (MODERATE-4), one universal asserted by a sampling
  gate but carried by a proof (MINOR-10). Otherwise the prose tracks
  the gates, including the honest halves in §7.1 and the "measured, not
  assumed" flags, which are real.
- **Deviations appendix.** Complete and honest for what it covers — the
  refuted pin expectation (item 2) and the identity-may-be-deleted
  reading of the cost (item 9) are both first-class. It does **not**
  disclose the DET-only cost sweep, and item 9 should also carry
  MAJOR-1's hypothesis.
- **Determinism / floats.** No wall-clock in the receipt or rendered
  output; arithmetic recorded as exact with an AST sweep of this unit
  and both imported terminal modules. My own re-derivation used exact
  integers and `Fraction` only and matched every value, which is
  independent evidence the substantive path is float-free.
- **Single-threaded.** The paper reads as authorship, not as a
  correction log. Compliant.

### MODERATE-5 — FUNNEL is not composition-closed

Definition 2.1 requires an admitted law to be composition-closed, and
the scope box declares FUNNEL a committed law family. But
`f_{0→1} ∘ f_{1→2} = (1,2,2)`, which moves two configurations and is
neither the identity nor an elementary merge. **FUNNEL is
composition-closed at n = 2 only; it fails at n = 3, 4 and 5**
(measured). It is used in 3 of the 16 rigidity sweeps and in the
pair-level table. No verdict changes — I reproduce `{discrete}` for all
16 sweeps and `member_1 = False, member_2 = True` under FUNNEL — but
either FUNNEL should be replaced by its composition closure, or the
scope box should say that FUNNEL is a declared *task family* that is not
composition-closed and therefore not a law in the sense of
Definition 2.1. As it stands, three sweeps and one table row are run on
an object the paper's own definition excludes.

### MINOR-9 — code stricter than paper at (ii-a)

Paper: "(ii-a) `comp(F) = A(B)` for every `F ∈ 𝔉`" — vacuously true on
the empty family. Code: `out["ii_a"] = (not bad) and bool(fam)`. The
code is stricter. It matters exactly at the empty complement of
MAJOR-1, where both readings agree the boundary is inadmissible, so
nothing delivered turns on it — but the paper should add "and the
declared family is non-empty" to (ii-a) to match the decision procedure
whose witness text ("the declared family is empty: the realized process
writes nothing at all") already presumes it.

### MINOR-13 — the erasing task of §7.2 is unnamed

The table reads "the closure plus one erasing task", and 3/4 is only
reproducible for a **total** eraser. The code uses `(0,0,0,0,0)`; a task
merging one pair gives 15/16, not 3/4. Name it: "the closure plus the
total eraser to one configuration."

---

## 4. PER-RUNG CONFIRMATIONS (a)–(f)

**(a) The four verdicts and the measured (i-a)+(ii-a) joint kill —
CONFIRMED.** Natively recomputed under DET at five configurations:

| context | (i-a) | (i-b) | (ii-a) | (ii-b) | admissible |
|---|---|---|---|---|---|
| aligned 2+1+1 `{01\|2\|3\|4}` | ✗ | ✓ | ✗ | ✓ | no |
| aligned 1+1+1+1 (discrete) | ✓ | ✓ | ✓ | ✓ | yes |
| aligned 2+2 `{01\|23\|4}` | ✗ | ✓ | ✗ | ✓ | no |
| tomographic `{0123\|4}` | ✗ | ✓ | ✗ | ✓ | no |

Identical to the paper's table, including the joint (i-a)+(ii-a) kill
with (i-b) and (ii-b) both passing. The declared family of member one
is 240 operations and contains the identity, which separates 0 from 1 —
the witness is as printed.

**(b) Rigidity and its identity-free control — CONFIRMED.** All 16
sweeps (DET/FUNNEL/REV at n = 2..5, ALL at n ≤ 4, counter-law at n = 5)
return the admissible set `{discrete}`, no exceptions. The
identity-free control is genuinely composition-closed (measured, not
asserted) and both proper boundaries `{01|2}` and `{0|12}` are
admissible under it, so rigidity is not a triviality. The control is a
law of the committed class in the only sense that matters here —
composition-closed — and is honestly flagged as identity-free.

**(c) Joint unforgeability (Thm 6.1) — CONFIRMED at the shared-law
quantifier, with MAJOR-3's hypothesis required.** Inclusion holds for
every `L` (lattice fact); the proof is sound; the escape under
per-context laws is constructed in §2.2 and is not covered.

**(d) The Feynman gate and its honest half — CONFIRMED.** σ = exactly 1
for the 120-task closure, exactly 3/4 for the 121-task family with the
total eraser; δ = exactly 0 at the admissible patch and exactly 1/16 at
the forged boundary, all from
`ρ = (1/16,1/16,1/16,1/16,3/4)` in exact rationals. The honest half is
correct and load-bearing: σ does not separate the forgery, and by
Theorem 3.1 there is no admissible comparator at the forged boundary,
so the separation is across boundaries. Both limitations are stated in
§7.1 and not absorbed. (MINOR-13: name the eraser.)

**(e) The cost tower, the exact-|Obs| proof, and pair-level
impossibility — NUMBERS CONFIRMED, THEOREM REFUTED AS STATED.** The
four levels, the remainders, the complement being a law, and the
strict growth all reproduce. The `c = |Obs|` theorem is false in
general (MAJOR-1) and its upper-bound step does not hold (MAJOR-2). The
pair-level termination is confirmed: after paying 120 the altered
3005-operation law makes member one admissible and member two
inadmissible, and `Pres(δ) ⊆ Pres(π₁)` is universal. Theorem 8.5
therefore stands at the shared-law quantifier and inherits MAJOR-3's
hypothesis.

**(f) The rung pair — CONFIRMED as the correct pre-registered
instantiation.** `GENERATIVE-ATLAS-AXIOM` is earned: the axiom is
decidable, covariant (zero violations at n = 3 and n = 4), rejects the
address-aligned forged member the predecessor could not reach, and
certifies the legitimate context. `BLOCKED-AT-CARRIER` is earned and is
correctly registered as the *price*, not as a hedge — Theorem 3.1
proves it and the identity-free control keeps it non-vacuous. The
paper's refusal to claim a carrier (§9, §10) is accurate. Neither
`EMPIRICALLY-IDLE` nor `CHEAP-LAW-FORGERY` occurs, and MAJOR-1 does not
disturb that: the cheapest forgery is not small under any law I
examined, and under the identity-containing class there is none at any
price.

---

## 5. NUMBERS TABLE — CLAIMED vs MINE

33 independent recomputations. 31 agree; 2 disagree — rows 26 and 27,
both refuting Theorem 8.3's general form.

| # | quantity | claimed | mine | |
|---|---|---|---|---|
| 1 | Bell record lattice, n = 1..5 | 1,2,5,15,52 | 1,2,5,15,52 | ✓ |
| 2 | FUNNEL family sizes, n = 2..5 | 3,7,13,21 | 3,7,13,21 | ✓ |
| 3 | \|DET\| at 5 | 3125 | 3125 | ✓ |
| 4 | \|REV\| at 5 | 120 | 120 | ✓ |
| 5 | counter-law: maps / reversibles | 120 / 1 | 120 / 1 | ✓ |
| 6 | counter-law fixes all records | 52 | 52 | ✓ |
| 7 | relabellings preserving counter-law | 1 of 120 | 1 | ✓ |
| 8 | `Pres_DET(π₁)` = member one's family | 240 | 240 | ✓ |
| 9 | tower, record level: cost / remaining | 120 / 3005 | 120 / 3005 | ✓ |
| 10 | tower, boundary level | 360 / 2765 | 360 / 2765 | ✓ |
| 11 | tower, coarser boundary | 1260 / 1865 | 1260 / 1865 | ✓ |
| 12 | tower, the limit | 3120 / 5 | 3120 / 5 | ✓ |
| 13 | `\|Pres_DET({0123\|4})\|` (2nd route) | 1260 + 20 | 1280 | ✓ |
| 14 | complement is a law, 4 tower levels | yes ×4 | yes ×4 | ✓ |
| 15 | boundary admissible in complement (DET) | yes ×4 | yes ×4 | ✓ |
| 16 | rigidity sweeps run | 16 | 16 | ✓ |
| 17 | admissible set in each sweep | `{discrete}` | `{discrete}` ×16 | ✓ |
| 18 | Prop 3.4 control: closed + 2 admissible | yes | yes | ✓ |
| 19 | covariance violations, n = 3 | 0 | 0 | ✓ |
| 20 | covariance violations, n = 4 | 0 | 0 | ✓ |
| 21 | W1 clauses (i-a,i-b,ii-a,ii-b) | ✓✓✓✓ | ✓✓✓✓ | ✓ |
| 22 | W2 clauses | ✓✗✓✓ | ✓✗✓✓ | ✓ |
| 23 | W3 clauses | ✓✓✓✗ | ✓✓✓✗ | ✓ |
| 24 | Example 4.2: closed / fixed records | yes / 4 of 5 | yes / 4 of 5 | ✓ |
| 25 | Example 4.2 collision partitions | 3 | 3 | ✓ |
| 26 | **`c({01\|2}, REV₃)`** | **6** (Thm 8.3) | **7** | **✗** |
| 27 | `c({0\|12}, {const₀})` | 0 (Thm 8.3) | 2 | **✗** |
| 28 | σ: closure vs closure+total eraser | 1 vs 3/4 | 1 vs 3/4 | ✓ |
| 29 | δ: admissible vs forged | 0 vs 1/16 | 0 vs 1/16 | ✓ |
| 30 | `Pres(δ) ⊆ Pres(π₁)` | true | true, ∀L | ✓ |
| 31 | member1/member2 under 4 committed laws | F/T ×4 | F/T ×4 | ✓ |
| 32 | after paying 120: member1 / member2 | T / F | T / F | ✓ |
| 33 | arena clause patterns, 4 rows | see §4(a) | identical | ✓ |

Adversarial constructions not in the paper: 18 REV counterexamples to
Theorem 8.3 at n = 3, 4; 1008 of 2748 (law, boundary) pairs over 687
composition-closed laws at n = 3 where the complement does not admit the
boundary (927 with a non-empty complement); 0 comparable admissible
pairs out of 357 (MINOR-11); FUNNEL closure failures at n = 3, 4, 5;
gate L2-17's test shown constant in `F` while its claim is verified true
on all 4860 obstruction members across the four levels.

---

## 6. SENTENCES TO REWRITE

1. **§8, Theorem 8.3 statement** — as in §1.2 above: bound plus
   hypothesis, with the REV failure named.
2. **§8, Theorem 8.3 proof, upper bound** — "Lemma 8.2 exhibits the
   complement as a law; that the boundary is admissible in it is a
   separate condition, which is the theorem's hypothesis and is
   measured here for DET at the declared scope."
3. **Abstract** — "The minimum number of single-operation alterations …
   is the cardinality of an obstruction set, exactly — every member must
   go, and no addition ever removes one." → "Every member of an
   obstruction set must go and no addition ever removes one, so the cost
   is at least the obstruction's cardinality; under the committed
   deterministic law it is exactly that, because the boundary is still
   admissible in what remains."
4. **§6, Theorem 6.1** — add "**when both contexts declare the same
   law**" to the statement.
5. **Abstract** — "no admitted law whatsoever makes both members
   admissible" → "no single admitted law makes both members admissible"
   + the escape disclosure of §2.2.
6. **§8, after Theorem 8.4** — "Every obstruction computed here contains
   the identity" → "The identity lies in the obstruction of every
   non-discrete boundary under every identity-containing law:
   `comp(id)` is discrete so `id ∈ Pres(π)`, and `id` separates every
   pair. This is Theorem 3.1 in cost form — general, not a fact about
   the levels swept."
7. **§8, Lemma 8.2 measurement sentence** and the `[EXH-4]` tags —
   insert "under DET".
8. **Definition 2.1 / Definition 8.1** — patch as a quadruple including
   the declared preparation, or `X₀ = X` fixed explicitly in 8.1.
9. **Definition 2.2 (ii-a)** — add "and `𝔉` is non-empty".
10. **Scope box, Laws row** — FUNNEL is not composition-closed at
    n ≥ 3; replace it by its closure or say it is a declared family, not
    a law in the sense of Definition 2.1.
11. **§7.2 table** — "the closure plus one erasing task" → "the closure
    plus the total eraser to one configuration".
12. **Appendix A** — add a deviation for the DET-only cost sweep, and
    extend item 9 with Theorem 8.3's hypothesis.

---

## 7. FINDINGS, RANKED

| # | severity | finding |
|---|---|---|
| MAJOR-1 | **blocking** | Theorem 8.3 (`c = \|Obs\|`) is false as stated; refuted by REV at all 18 non-discrete boundaries at n = 3, 4 (cost `n!+1`, an addition required) and by a `\|Obs\| = 0` inadmissible boundary. Lower bound and DET tower unaffected. |
| MAJOR-2 | **blocking** | Theorem 8.3's upper-bound step attributes to Lemma 8.2 a conclusion it does not prove (admissibility in the complement, measured DET-only). |
| MAJOR-3 | **blocking** | Theorem 6.1 / the abstract / gate L2-20 omit the shared-law hypothesis; under the pin's own "one law family per context" both colluding members are admissible, witness `L₁ = {(0,0,2,3,4)}` and `L₂ = DET`. |
| MODERATE-4 | fix | Gate L2-17's test is constant in `F` and does not test "each one alone"; the claim is independently true (verified on all 4860 members). |
| MODERATE-5 | fix | FUNNEL is not composition-closed at n = 3, 4, 5, yet is declared a law; 3 of 16 sweeps and one table row run on it. No verdict changes. |
| MODERATE-6 | fix | "No forgery at any price inside the committed class" is a corollary of Theorem 3.1 for all identity-containing laws, presented as a measured fact about the levels swept. |
| MODERATE-7 | fix | The patch is defined as a triple but needs the declared preparation; Definition 8.1 drops it while the code fixes `X₀ = X`. |
| MINOR-8 | fix | Lemma 8.2's proof is fibre-language (deterministic) while Definition 2.1 admits relations; the relational argument is supplied in §1.1. |
| MINOR-9 | fix | Code's (ii-a) adds `and bool(fam)`; the paper's (ii-a) is vacuous on the empty family. |
| MINOR-10 | note | Gate L2-20 asserts a universal it samples over five laws; the universal is carried by the proof and should say so. |
| MINOR-11 | strengthen | Theorem 6.1 is the `δ` case of "no two strictly comparable boundaries are both admissible under one law" — 0 comparable pairs of 357 over 687 laws. |
| MINOR-12 | fix | `cost_scaling` receipt rows carry no `law` field, so the DET-only scope is unrecorded. |
| MINOR-13 | fix | §7.2's erasing task is unnamed; 3/4 requires the total eraser. |

**Meta.** Zero false computed numbers; one false theorem (MAJOR-1) and
one missing hypothesis (MAJOR-3), both local and both repairable
without a re-run. The paper's discipline where it is honest — the
refuted pin expectation, the entailment stated as a limitation, §7.1's
honest half, §6.6's "reproduces rather than extends", the
`BLOCKED-AT-CARRIER` price — is real and survives this review intact.

*R1, operator lens. Frozen on delivery.*
