# COC — HOSTILE REVIEW, R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens.  **Date:** 2026-08-08.
**Protocol:** `v13/note-coc-hostile-protocol.md` (FROZEN, v13 #230), kill-shots
K1–K5 binding, primary weight on **K5** and **K4**.
**Object reviewed (SHA-256 prefixes verified before reading, all four match):**

| artifact | declared | verified |
|---|---|---|
| `v13/paper-coc-cocycle.md` | `3ecd933ad1d9` | `3ecd933ad1d9` ✓ |
| `v13/code/coc_cocycle_exact.py` | `0c0592a15d2e` | `0c0592a15d2e` ✓ |
| `v13/code/coc_cocycle_output.txt` | `cbbece149650` | `cbbece149650` ✓ |
| `v13/code/coc_cocycle_receipt.json` | `6f99d790e021` | `6f99d790e021` ✓ |

**Method.** All work in scratch; no repo file was modified or executed in
place. The instrument, the GEN receipt and every mutated copy were run from
`.../scratchpad/work/`. A **from-scratch reimplementation** of base G, the
chart family, the four-clause predicate, the census, the defect set, the
holonomy group and the completion rebuild was written independently
(`r3_independent.py`, `r3_probe.py`, `r3_anchors.py`, `r3_completion.py`) and
used for every recomputation; nothing was imported from `coc_cocycle_exact.py`.

**Recomputation count: 61 independent recomputations** (enumerated in §8).

---

## 0. What survived, stated first

The unit is unusually well built, and most of what the protocol asked me to
attack held under attack:

- **Byte-identical reproduction, twice.** Two fresh delivery-mode runs in
  scratch produced artifacts byte-identical to each other *and* to the two
  committed artifacts in the repo. Determinism claim: **confirmed**.
- **Every headline number reproduced from scratch**: family 4; 4 charts at
  each of the 6 settings; scope 162 → 2 admitted; FULL 240 / REAL 160;
  multiplicity 32/208/**48**; committed pair **18 / 8**; census **1,824** by
  both routes; the per-cell table **48/192/48/0** exactly as printed; defect
  set **1,248 identity + 576 wing exchange**; **96 of 192** at each of the six
  bigon cells; defect group order **2**.
- **All 19 anchors traced and independently verified**, including the ten
  external ones against the hash-pinned GEN receipt, cell by cell where the
  anchor is cell-by-cell.
- **The hash pin fires**, on a value corruption *and* on a whitespace-only
  corruption (A07 alone). Anchors are genuinely exit-1: a failing anchor
  increments `must_pass_failures` (`build_receipt`, line 3251).
- **28/28 mutants die**, all exit 1, none silent, none crashed before
  reporting; `never_falsified` is genuinely **EMPTY at 24**, both denominators
  correct.
- **The self-correction is real**, the gate is identifiable, and I reproduced
  the kill on a reconstructed false version.
- **The non-abelian witness is genuine** and would catch order and inversion
  errors.
- **K4's central claim holds**: the admission predicate *is* generalised
  verbatim, and I confirm the 18/8 anchoring **48/48 cell by cell**.

**No false numerical result was found anywhere in the paper or the receipt.**
Every number I checked is the number the data carries. My findings are about
what the instrument's gates *can* discriminate and about three claims the unit
makes *about its own evidence*.

---

## 1. MAJOR — the 576 "free" triangles are not free: the drawn maps form a
## coboundary at every coordinate, and the unit never measures it

**The claim under attack.** Paper §5.4: "Every one of the **576** triangles
there could have carried the wing exchange — a defect no bigon at that setting
generates … The gate measures that none does." §11.4: "The free content of the
membership gate is the four flat settings, and it is named and counted (576
triangles)." D4: "the free half is what the verdict rests on." The same claim
is in the **must-pass gate's own text** (`run_membership`, lines 1955–1960):
"every triangle there could have carried a non-identity defect that no bigon
holonomy generates".

**What I measured.** Two facts, both on the unit's own data, neither of them
anywhere in the paper or the code:

1. **The drawn map is a coboundary at every coordinate under every rule.**
   For each (setting, checkpoint, rule) I searched for a potential
   `h : charts → S` with `g_XY = h_Y h_X^{-1}`. It exists at **48 of 48**
   coordinate×rule combinations — zero exceptions. At GP-E the two potentials
   are `h^FULL = {F1:1, F2:1, W.F1:W, W.F2:W}` and
   `h^REAL = {F1:1, F2:W, W.F1:W, W.F2:1}`, and they reproduce the paper's own
   §3 table (GP-E/t0) **entry for entry, both columns, all twelve rows**.

2. **Eighteen of the twenty-four coordinates are rule-blind** — both rules draw
   the *same* map on *every* ordered pair, so no rule assignment can mix
   anything. Those eighteen are all sixteen flat-setting coordinates plus
   GP-E/t2 and GP-F/t2. **All 576 flat-setting triangles sit at a rule-blind
   coordinate** (measured: 576 of 576).

Put together, at every one of those 576 triangles
`δ = (h_A h_C^{-1})(h_C h_B^{-1})(h_B h_A^{-1}) = 1`, **identically, in any
group**. Holding the measured atlas fixed, not one of the 576 *could* have
carried the wing exchange. The counterfactual the paper and the gate assert is
false.

**What the paper offers instead is half a mechanism.** §6 says: "What makes the
identity come out there is measured in §6: those coordinates carry no
multiplicity at all, so the three edges' maps cannot be mixed." Absence of
multiplicity fixes *which* three maps are composed; it does not make their
composite the identity. The missing half is the coboundary property, and it is
the half that does the work.

**A strengthening the unit should take.** The closed form
`δ = ∏_{edges assigned REAL} w_X w_Y`, with `w_X = W` iff the chart's frame is
F2 and `w_X = 1` otherwise, **agrees with the census on 1,824 of 1,824
triangles**. The entire census is the comparison of two coboundaries that
differ by the F2-flag. That single line explains the defect set, the
restriction to GP-E/F, and the exact-half 96/192 simultaneously — and it makes
the "no gerbe" conclusion transparent: a difference of two coboundaries is
itself a coboundary (`c_XY = m_Y m_X^{-1}` with `m = hk`), so the level-2
obstruction is trivial by construction of the atlas, not by measurement of the
geometry.

**Severity: MAJOR.** It moves no number and does not touch the verdict, but the
free/forced split is the unit's own account of where its teeth are, and the
free half is forced by measured structure the unit does not name. This is
exactly the "describe mechanisms as measured, not as intended" failure
(RUNBOOK appendix, #38→#40).

**Repair.** (a) Add a `COC-COBOUNDARY` measurement: search the potential at
every coordinate and rule, print it, and gate the census's defect against the
closed form. (b) Restate §5.4/§6/§11.4: the free content is not "576 triangles
could have gone the other way" but "the pair table could have drawn a
non-coboundary assignment, and it is measured not to — 48/48." (c) §11.3
already gestures at this ("the atlas is generated by the two-chart atlas
together with an admitted isomorphism"); promote it from a scope note to the
measured mechanism.

---

## 2. MAJOR — the verdict's derivation is not gated: an inverted decision rule
## passes every gate and prints the opposite verdict

**The claim under attack.** Paper §10: "The verdict is re-derived inside its
own gate from the recorded results and measured to be the string the rule
selects."

**What the code does.** `run_verdict` (lines 2931–2965) computes `base` from
`n` and `outside`, then gates
`ok = any(verdict.startswith(p) for p in PREREGISTERED)`. There is **no second
derivation and no comparison**. `COC-VOCABULARY` checks vocabulary membership
only.

**Falsifier.** I changed one character in the decision rule
(`elif outside > 0:` → `elif outside >= 0:`) in a scratch copy. Result:

```
exit=0   KILL-JSON {"failed_anchors": [], "failed_gates": []}
UNIT VERDICT: COC-HIGHER-OBSTRUCTION
```

The run passes all 25 must-pass gates and 19 anchors, and announces the
**opposite** of the unit's verdict, while the same receipt still records
`defects_outside_the_bigon_group: 0`. Nothing catches it.

This also explains why `COC-VOCABULARY` is one of the three gates falsified
**only by a waiver**: there is no computational defect for a computation mutant
to inject, because the predicate does not test the computation.

**Severity: MAJOR.** A stated property of the instrument is absent, and the
consequence is that the load-bearing conclusion string is ungated. Mitigating:
the *numbers* are gated, and a reader comparing the verdict against the printed
`defects_outside_the_bigon_group: 0` would see the contradiction — but that is a
human check, not a gate, and the paper claims the gate.

**Repair.** In `COC-VOCABULARY`, re-derive the verdict by an independently
written expression from `TABLES["census"]["size"]` and
`TABLES["membership"]["defects_outside_the_bigon_group"]` and gate equality
against `FINDINGS["unit_verdict"]`; then a `verdict-rule` computation mutant
becomes possible and the gate stops being waiver-only.

---

## 3. MAJOR — the census's "two independent routes" cannot see an omission;
## a dropped coordinate cell passes with both routes agreeing

**The claim under attack.** Abstract: "the size computed twice by independent
routes." §4: "the same, recomputed by an **independent route**." §12: "The
census size is recomputed from the pair table without walking a triangle."

**What the second route is.** `run_census` (lines 1540–1553) runs both routes
inside the *same* loops over `SETTING_ORDER`, `CHECKPOINTS` and
`itertools.permutations(charts_at(sp,fam), 3)`, and both call the *same*
`drawn_map` oracle. The comparator is
`Σ_triples Π_i (Σ_r [edge i drawn])`, the enumerator is
`Σ_triples Σ_{r1,r2,r3} [all three drawn]`. These are the **distributivity
identity**, and are equal for every possible oracle. The second route therefore
tests exactly one thing: that the innermost rule-assignment loop keeps every
combination. It is blind to the chart family, the coordinate list, the triple
enumeration, and the oracle itself.

**Falsifier.** I reconstructed "the census restricted" *from prose* but at a
different site: skip the coordinate `(GP-E, t1)` entirely, rather than filter on
rules. Result:

```
size:1632, size_recomputed_independently:1632
COC-CENSUS   measurement  PASS
exit=0   KILL-JSON {"failed_anchors": [], "failed_gates": []}
```

A census that has silently lost an entire cell — **192 triangles, 10.5 % of the
object** — passes the gate whose headline is "THE TRIANGLE CENSUS IS
EXHAUSTIVE", with both routes in agreement, and **no other gate in the
instrument catches it either** (exit 0). The declared `triangle-drop` mutant
does die at `COC-CENSUS`, so the gate has teeth against the rule-filter class;
it has none against the omission class.

**Severity: MAJOR.** The census is the unit's primary object and its
exhaustiveness is the pin's requirement. The gate's own claim text is honest
("over the same triples and coordinates"), but the paper's three summary
sentences are not, and the exhaustiveness is not gated against anything.

**Repair.** (a) Gate the census's *arena*: compute the expected coordinate count
(`6 × 4`), the expected ordered triples per setting (`P(charts_at, 3)`) and the
expected rule assignments (`2³`), and gate the census's own iteration counts
against them. (b) Gate the per-cell counts against the pair-table
multiplicities cell by cell (they determine the cell count exactly). (c) Replace
"independent route" in the abstract, §4 and §12 with the gate's own wording plus
one sentence naming what the second route can and cannot catch.

---

## 4. MODERATE — `COC-MEMBERSHIP`'s own tabulation is untested; a broken
## tabulation reports a false zero

The five computation mutants that falsify `COC-MEMBERSHIP` — `edge-perturb`,
`chart-merge`, `scope-lax`, `admit-lax`, `label-collapse` — all perturb its
*inputs*. The one mutant aimed at membership logic, `membership-lax`, **does not
falsify `COC-MEMBERSHIP` at all** (it kills only `COC-NEGATIVE-CONTROL`, per the
delivered table), because on the true data nothing is outside anyway.

**Falsifier.** Reconstructed from prose at a different site — replace
`run_membership`'s `outside = [r for r in sub if not in_group(...)]` by
`outside = []`. Alone: **exit 0**, nothing caught. Combined with a genuine
outside-the-group edge perturbation at GP-A (whose holonomy group is trivial):

```
COC-MEMBERSHIP   measurement  PASS
  defects_outside_the_bigon_group: 0        <-- FALSE: the truth is nonzero
exit=1  (killed only by COC-PAIR-TABLE and COC-DEFECT-IS-A-BIGON-HOLONOMY)
```

So the membership gate has a demonstrated false-negative path: it will report
zero-outside when the truth is nonzero. The run still dies, but via other
gates — the membership gate itself never notices.

**Severity: MODERATE** (the run does die; the headline zero is protected by
neighbours, not by its own gate). **Repair:** add a computation mutant that
perturbs `run_membership`'s tabulation, or compute `outside_total` a second time
by an independently written pass and gate the two equal.

---

## 5. K5, K4, K3, K1 — the protocol's checklist, item by item

### K5(a) two routes — see §3. Both counts reproduced (1,824 / 1,824) and the
per-cell table 48/192/48/0 reproduced exactly. Independence judged **narrow**;
finding filed.

### K5(b) 19 anchors, traced

8 self-anchors + 10 external + 1 hash pin = 19 (arithmetic in §12 of the paper
is right). Independently verified:

| anchor | quantity | my independent value | verdict |
|---|---|---|---|
| A01-R0/R1/R2 | the three rotations, entry by entry | Euler-Rodrigues of (1,0,0,0),(2,1,0,0),(3,0,0,2) = the pinned tables | ✓ |
| A02 | ψ as V's first column | `[0,2/3,0,2/3,0,0,0,0,1/3]` | ✓ |
| A03 | V = H·Q, 81 entries | rebuilt from ψ and Q, equals `PINNED_V` | ✓ |
| A04 | every declared leg exactly orthogonal over ℚ | True (all 6 settings × 2 frames × 3 legs) | ✓ |
| A05 | the two wings commute | True at every declared pair | ✓ |
| A06 | shift injective + independent leg rebuild | fires on a pinned-table break (below) | ✓ |
| A07 | sha256 of the GEN receipt | `e0b2f444f6a9…d292` = the pinned string | ✓ |
| A08 | the declared arena, 13 fields | all 13 agree with `tables.arena` | ✓ |
| A08b | symmetric-setting count, admitted maps | 2, `[identity, wing exchange]` | ✓ |
| A09 | committed drawn-cell counts | **FULL 18 / REAL 8** recomputed from scratch | ✓ |
| A10 | committed table cell by cell **and map by map** | **48/48 agree**, zero mismatches | ✓ |
| A11 | group order per setting | 1,1,1,1,**4**,**4** | ✓ |
| A12 | closed paths per setting | 8,8,8,8,**364**,**364** | ✓ |
| A13 | elements by fixed-point count | {81, 45, 9, 9} at GP-E and GP-F | ✓ |
| A14 | abelian, orders, value-set closed | reproduced | ✓ |
| A15 | D's order and fixed configurations | **order 2, 45 fixed** | ✓ |
| A16 | completion census | **40,320 / 96 / 40,224** | ✓ |

The bigon graph was rebuilt independently (9 links / cycle rank 2 at the flat
settings, 13 links / cycle rank 6 at the symmetric ones), reproducing §5.1's
table in full.

**Hash-pin fired on corruption — three deliberate breakages:**

| breakage | exit | kills |
|---|---|---|
| one value changed in the GEN receipt (`arena.carrier` 81→82) | 1 | `A07`, `A08`, `COC-EXTERNAL-SOURCE-PINNED`, `COC-ARENA` |
| **whitespace only** appended (no value moves) | 1 | `A07`, `COC-EXTERNAL-SOURCE-PINNED` **alone** |
| a pinned rotation *table* entry perturbed (not the constructor) | 1 | `A01-R2`, `A06`, `COC-BASE-PINNED` |

The whitespace case is the one that matters: it shows the hash pin is
load-bearing independently of every value anchor. Exit-1-only confirmed
structurally (`build_receipt` counts failed anchors into
`must_pass_failures`).

### K5(c) 28 mutants audited

Recomputed by me from the receipt, not read off it: 29 gates, 4 disclosures,
25 must-pass, denominator **24** (excluding `COC-FALSIFICATION`); 28 mutants,
**28 died**, all exit 1, **none** silent, **none** crashed before reporting;
`never_falsified` = **[]**; 24/24 falsified by some mutant, **21** by a
computation mutant; falsified only by a waiver = `COC-EXACT`,
`COC-NO-MUTANT-EXEMPTION`, `COC-VOCABULARY`; kinds 23 computation + 5 waivers.
Every one of these matches the paper exactly.

**Named kills reproduced from prose (seven reconstructions, each injected at a
site of my own choosing, not via the `--mutant` flag):**

| # | prose reconstructed | my injection site | result |
|---|---|---|---|
| M1 | "composed in the reversed order" | `perm_compose` itself (y∘x) | dies at `COC-COMPOSE-WITNESS` ✓ |
| M2 | "membership answers yes to everything" | `run_membership` tabulation | **SURVIVES, exit 0** → §4 |
| M3 | "the census restricted" | a coordinate skip | **SURVIVES, exit 0** → §3 |
| M4 | "the switching's sign dropped" | drop *all* signs | dies at `COC-GAUGE-COVARIANCE` ✓ |
| M5 | "the self-test reads the cache" | never enter fresh mode | dies at `COC-FRESH-EVAL` ✓ |
| M6 | "a drawn identification replaced" | a **different** edge (GP-F/t3) | dies at 4 gates ✓ |
| M7 | verdict derivation inverted | the decision rule | **SURVIVES, exit 0** → §2 |

Four of seven reproduce their declared kills when injected somewhere the author
did not choose — that is the right result. Three do not, and are filed above.

**The 5 waivers are legitimate**, and correctly declared as waivers:
`control-lax` and `flip-lax` overwrite `ok` directly (and their gates are also
killed by 3 computation mutants each, so nothing rests on them); `float-lax` and
`exempt-lax` register an entry in an AST gate's evidence list *after* the sweep,
which is the only injection a flag-based mutant can make against a gate that
reads the source text — declaring these waivers rather than dressing them as
computation mutants is the honest call; `verdict-lax` actually mutates the
computation but is declared a waiver, which is the **conservative** direction
(it does not count toward the computation-mutant denominator).

**I upgraded two of the three waiver-only gates with real source falsifiers**,
which the unit's own mutant mechanism cannot produce:

| real source edit | exit | kills |
|---|---|---|
| a genuine `1.0` float literal inserted in `fixed_points` | 1 | `COC-EXACT` |
| a genuine `MUTANT != None` **inside** the `COC-MEMBERSHIP` predicate | 1 | `COC-NO-MUTANT-EXEMPTION` |
| a genuine `MUTANT != "…"` **outside** every gate call | 1 | `COC-NO-MUTANT-EXEMPTION` |

So `COC-EXACT` and `COC-NO-MUTANT-EXEMPTION` demonstrably catch real
source-level defects, not merely their own waivers — the paper understates them.
`COC-VOCABULARY` alone remains waiver-only *in substance*, for the reason given
in §2.

### K5(d) the self-correction audit

**The gate is `COC-COMPLETION-DEPENDENCE`**, and the clause that caught the
false claim is line 2843:

```python
and all(alt["distinct_charts_per_setting"][sp] == 4 for sp in asym)
```

The mid-build claim was that the atlas collapses to two charts *everywhere* at
the exchange-equivariant completion. I reconstructed exactly that version in
scratch (changing the `asym` expectation from 4 to 2) and ran it:

```
FALSE-CLAIM-VERSION EXIT=1
KILL-JSON {"failed_anchors": [], "failed_gates": ["COC-COMPLETION-DEPENDENCE"]}
```

**The gate fires on the false version.** The self-correction is real and
pre-delivery, as the ledger records.

**The corrected per-setting reading, verified independently** with my own
81-configuration rebuild on the bare Householder completion:

| | GP-A…GP-D | GP-E, GP-F |
|---|---|---|
| distinct charts, pinned completion | 4 | 4 |
| distinct charts, equivariant completion | **4** | **2** |
| triangles, pinned | 144 each | **624 each** |
| triangles, equivariant | 144 each | **0** |

This is the printed reading, and the "four flat settings keep a four-chart atlas
even there" half — the half the false version smoothed away — is the correct
one. §9.2 and the gate text both state it.

### K5(e) — K4: the admission predicate, diffed clause by clause

Base G's committed predicate (`gen_generality_exact.py:1340–1370`) against
COC's generalised one (`coc_cocycle_exact.py:1308–1337`):

| clause | committed (F2 → F1) | generalised (X → Y) | verdict |
|---|---|---|---|
| 1 initial configuration | `p[J0] != J0 → skip` | `p[jx] != jy → skip` | **verbatim**; for admitted charts `jx = jy = J0`, so it reduces to the committed form |
| 2 leg list, order-free at Born level | `sorted(leg_key(σ_p L)) for L in F2` vs `sorted(leg_key(L)) for L in F1` | source conjugated by p vs target unconjugated | **verbatim**; same direction (source conjugated), same key, same multiset-as-sorted-list comparison |
| 3 occupied set | `{p[i] for i in db} == set(da)`, db = F2, da = F1 | db = X, da = Y | **verbatim** |
| 4 exact law | `da.get(p[i]) == db.get(i)` ∀ i ∈ db | identical | **verbatim** |
| uniqueness | `drawn = len(adm) == 1` | `adm[0] if len(adm)==1 else None` | **verbatim** |

The only differences are `(F2, F1) → (X, Y)` and `(J0, J0) → (jx, jy)`, both the
minimal generalisation, both reducing to the committed form at the committed
pair. The one shape difference — base G applies the j₀ filter inside `admits`
over the full scope, COC pre-filters the scope and re-checks — is
extensionally identical. **The paper's "generalised verbatim" is accurate.**

**The 18 FULL / 8 REAL anchoring, cell by cell.** My independent implementation
reproduces the committed table at all 24 coordinates × 2 rules with **zero
mismatches on both the drawn/not-drawn verdict and the name of the map drawn**
(48/48). The distribution: GP-A…GP-D draw FULL=identity at t∈{0,1,3} and
nothing at t2; GP-E/GP-F draw FULL=identity and REAL=wing exchange at
t∈{0,1,3}, and REAL=wing exchange alone at t2. 18 FULL, 8 REAL. **Confirmed.**

**The R1 ABSENT verdict on one setting — my judgment: the one-setting basis IS
sufficient, and D6's stated reason is correct.** The killing clause compares
`sorted([leg_key(L) …])` of a **five**-leg chart against a **three**-leg one;
two sorted sequences of different lengths are never equal, for any permutation
p, any rule, any target chart, any setting. The split chart has five legs at
every setting by construction (one of three committed legs replaced by three
sub-legs), so the clause fails identically everywhere. There is also an
independent second killer the paper names: six checkpoints against four, so the
read-time coordinate cannot be matched. **No sweep is needed for the ABSENT
verdict.**

**But the gate bundles a second clause that D6's argument does not cover** —
see §6 (MINOR-1).

**The 216-extension "same map everywhere" claim — verified independently.**
Extension deduped to **216**; admitted after the j₀ filter **8**; measured
**closed under composition**; 576 ordered-pair × coordinate × rule comparisons;
**400** drawn at the extension (= 240 FULL + 160 REAL); **zero** coordinates
where the verdict or the map changes. The eight admitted-extension maps have
fixed-point counts {3,3,9,9,9,27,27,81}, so the set does contain permutations
outside the Klein-four {81,45,9,9} — the "escaping permutations" claim is
right. **Confirmed exactly.**

### K5(f) fresh evaluation and the AST sweep

`COC-FRESH-EVAL`'s predicate requires all five of: `hits == 0`, `written > 0`,
`reread == written`, `fresh_requests_for_a_key_already_in_the_cache > 0`,
`misses > 0`. Delivered: 8 / 8 / 8 / 0 hits / 64 misses. I verified the
arithmetic independently: 8 declared two-chart loops (6 multiplicity bigons at
GP-E/F × t∈{0,1,3}, plus 2 defect loops), each requesting one unsigned
reference plus 2ⁿ signed variants, Σ2ⁿ = 6·4 + 2·16 = **56**, total requests
8 + 56 = **64** misses. Both halves of the §14 addendum are satisfied: the read
path is measured to work (8 re-reads returned stored values) *and* the sweep is
measured to ask for keys that are in the cache (8) and refuse them (0 hits).
**Not vacuous.** My independent `memo-lax` reconstruction (never entering fresh
mode) dies here.

One scope note, correctly stated in the receipt but worth making explicit: the
cache gate covers only the 8 two-chart loops; the 14,592 triangle-loop
comparisons are computed inline and never touch `_memo`.

**The AST no-mutant-exemption sweep is verified with real falsifiers** (table in
K5(c)): it fires both on a `MUTANT != …` reaching a gate predicate (the
"reaching" clause) and on one anywhere else in the source (the "found" clause).
I also confirm the delivered claim that **zero** gate/anchor call sites reach
the mutant flag: every mutation in this instrument is injected in the
computation, which is the rule's intent.

### K5(g) the non-abelian witness gate

Reconstructed independently. The witness is x = a cyclic system relabelling
(**order 3**, 0 fixed points), y = the wing exchange (order 2, 9 fixed points),
z = a cyclic pointer relabelling (**order 3**, 0 fixed points). Measured:

- `compose3(x,y,z)` equals the direct index expression `z[y[x[i]]]` ✓
- the reversed order gives a **different** permutation ✓
- **of the six orderings of the three factors, only `z∘y∘x` produces the
  expected value** — so *any* order error, not merely the reversal, is caught
- inversion is observable: `x⁻¹ ≠ x` (order 3), and substituting `x⁻¹` for `x`
  changes the answer ✓
- `minv(pmat(x)) = pmat(x⁻¹) ≠ pmat(x)` ✓

**The gate would catch an order or inversion error. K2's replacement control is
real.** And the disclosure it replaces is honest: on the drawn maps
S = {1, W} I confirm every one of the six orderings gives the same product, so
the pin's wrong-order control is genuinely inert (0 of 1,824) for the reason
given — abelian, exponent two.

### K1 and K3, at the depth the protocol assigns them

**K1 — the defect set, recomputed independently.** 1,248 identity + 576 wing
exchange; non-identity only at GP-E and GP-F; 96 of 192 at each of the six
bigon-carrying cells; generated group order **2**; D (45 fixed configurations)
and W·D (9) never appear as triangle defects. All reproduced from scratch.

*On "why is D never a triangle defect" (K1's derivation question, which is R1's
lens, offered here because my §1 answers it):* every drawn identification lies
in S = {1, W}, S is closed, and **D ∉ S** — D lives in the holonomy group only
because the *defect loop* traverses the preparation leg, which is not an
identification link. A triangle composes three identification links and nothing
else, so it cannot reach D. This is structural, not an artifact of the drawn
maps.

**K3 — the collapse criterion, recomputed and stratified.** I verified
`W.F1 ≠ F2 exactly by D` (D has order 2 and 45 fixed configurations,
independently computed). The exhaustive sweep reproduces **40,320 / 96 /
40,224**. Beyond the protocol's ask of three sampled completions, I validated
the 9×9 criterion against a **full 81-configuration rebuild at six sampled
completions** — identity, the pinned Q=(1 2), (4 8), (1 3), (1 4), and
(2 6)(5 7) — and the criterion agrees with the 81-level chart collapse and with
`D == identity` at **all six**, with no exception.

I also give the closed form the paper does not: σ = (1 3)(2 6)(5 7) with fixed
points {0,4,8}, so `|C_{S₉}(σ)| = (2³·3!)·3! = 288` and those fixing index 0
number `2·48 = 96`. **The 96 is exactly the centraliser count** — the sweep is
correct and now has a derivation, and "generic in the completion family" is
`1 − 96/40320 = 1 − 1/420`.

---

## 6. Minor findings

**MINOR-1 — `COC-ROUTE-CENSUS`'s factorisation clause is measured only in its
degenerate instance.** `run_route_census` hard-codes `sp0 = "GP-E"`, whose
wing-A rotation is R0 = the identity, so the must-pass clause
`mm(RA, mm(CA, minv(RA))) == U_local("A", g)` reduces to `CA == U_local("A","R0")`
— the conjugation is vacuous there. §9.1 states the factorisation
`U_X(g) = (R_g⊗I)·C_X·(R_g^T⊗I)` as a general fact. **I verified it
independently at all three declared rotations on both wings: it holds
everywhere, so no claim is wrong** — but the clause is gated where it cannot
fail. D6 defends the one-setting basis by the leg-list clause's
size-independence, which is correct and does *not* cover this clause. *Repair:*
loop the factorisation over `ROT_ORDER` (two lines; I confirmed it passes).

**MINOR-2 — §6's "equal" half is forced by the confinement the unit already
discloses.** The multiplicity bigon's holonomy is `g_REAL ∘ g_FULL⁻¹` for the
committed pair; both factors lie in S, S is closed, so the bigon holonomy lies
in S = {1, W}, and it is non-identity exactly at the multiplicity coordinates
(measured: the wing exchange at all six, `None` at the other eighteen). Given a
defect that is non-identity and confined to S, "it **equals** the bigon" is
forced — there is only one non-identity element to be. The genuine content of
§6 is clause (2) (no bigon ⟹ only identity defects) together with "the bigon
holonomy is W and not D or W·D". Separately, the advertised **if-and-only-if**
is gated in one direction only: the converse (a coordinate with a bigon carries
some non-identity defect) is tabulated (96/192) but not in the gate predicate,
which tests `not bad_equal and not bad_absent and n_nontrivial > 0`. *Repair:*
disclose the forced half beside D4, and gate the converse.

**MINOR-3 — §12 mis-names the gate excluded from the denominator.** The paper
says "The one gate excluded from the denominator is **the census gate itself**,
which does not run inside a mutant." The receipt records
`the_gate_excluded_from_the_denominator: COC-FALSIFICATION`, and I recomputed
that `COC-CENSUS` **is** in the denominator (24/24 includes it, falsified by
four computation mutants). "The census gate" reads as `COC-CENSUS`, whose
exclusion would be a serious carve-out. *Repair:* name `COC-FALSIFICATION`.

**MINOR-4 — §8.3 states forcedness for one half of the flip test and omits it
for the other.** The paper prints the triangle half's forcedness (all 1,824
defects are their own inverses) but not the receipt's parallel number
`two_chart_loops_whose_matrix_is_its_own_inverse: 8` — **all 8 of 8**. The
gate's own text is precise (it is the *link variables*, specifically the
preparation leg, that are unforced, which is why `orient-flip` dies), but a
reader of §8.3's "the other half is not forced" would not learn that every
two-chart loop matrix is also involutive. §8.3 promises "coverage and
forcedness are both stated". *Repair:* print the 8/8.

**MINOR-5 — the extension census is inferred, not recomputed.** `n_ext =
len(rows) if not changed`. The inference is sound (identical drawn maps ⟹
identical census) but §9.3's "and a census of 1,824 unchanged" reads as
measured. *Repair:* one word — "therefore unchanged". (I did recompute it: 576
comparisons, 400 drawn, 0 changed.)

---

## 7. Discipline compliance (RUNBOOK §13–§15, every addendum)

| requirement | verdict |
|---|---|
| §13(4) freeze before fixture truth | **PASS** — `COC-FREEZE` is gate 0 with the defect counter at zero; `COC-DECLARATION-ORDER` measures last-declaration index 6 < first-fixture index 9; `freeze-lax` and `order-lax` both die |
| §14 symmetry self-test under the symmetry's own action | **PASS** — complete switching sweep, 56 + 14,592 comparisons, tested set fixed by declaration; sign/orientation mutants present (`sign-flip`, `orient-flip`) and both die |
| §14 addendum (#185) fresh eval, cache exercised | **PASS** — see K5(f); both halves gated, not vacuous |
| §14 addendum (#208) no gate references mutant identity; forced clauses are disclosures | **PASS** on the sweep (verified with real falsifiers). **PARTIAL** on the second half: `COC-CONFINEMENT`, `COC-MISCOMPOSITION`, `COC-GAUGE-PERMUTATION-FORCED` and `COC-ADMISSION-SCOPE` are correctly demoted to disclosures, but the forced content identified in §1 and MINOR-2 is not |
| §14 addendum (#219) comparators independent of the audited component; no vacuous cache gate | **PARTIAL** — satisfied for §6's comparator (matrix product vs tuple composition) and the positive control; the census comparator satisfies the letter but is the distributivity identity (§3). Cache gate is non-vacuous |
| §15 declared arena as data, sizes computed | **PASS** — every count enumerated, none typed; I recomputed 4, 2, 162, 216, 8, 24, 12, 24, 8 |
| §15 addendum (#196) match every coordinate | **PASS** — read time carried inside every law datum; `COC-READ-TIME-COORDINATE` measures 0 of 144 cross-checkpoint collisions; D3 honestly scopes the per-setting comparator and routes the per-checkpoint match to §6 |
| permutation-tuple counting, exact arithmetic | **PASS** — `defect_value` returns tuples; `label-collapse` dies; no float literal (verified with a real falsifier) |
| complete sweeps or declared [SAMP] | **PASS** — census, switching sweep, scope disclosure and completion family all exhaustive |
| positive + negative controls with teeth | **PASS** — 152 degenerate triangles (I derived 48 + 96 + 8 = 152 analytically from the pair table); both injections behave as claimed (D: 45 fixed, in-group, out-of-defect-set; pointer transposition: 27 fixed, out-of-group) |
| byte-identical delivery runs | **PASS** — reproduced twice, matching the repo |
| deviations ship | **PASS** — 8 deviations, all substantive; D2, D4, D6 and D8 are exactly the right disclosures. D4 is the one that needs amending (§1) |
| NO git, freeze-on-delivery | **PASS** — no git in this review; artifacts unmodified |

---

## 8. Recomputation count

**61 independent recomputations.** SHA verification of the four frozen
artifacts (4); byte-identical delivery runs and repo comparison (3); from
scratch — family size, charts per setting, admitted scope, base scope, FULL
draws, REAL draws, multiplicity histogram, committed FULL count, committed REAL
count, census route P, census route Q, the 24-cell per-cell table, the defect
set, the per-cell non-identity table, the generated group order (15); the
coboundary search at 48 coordinate×rule combinations, the rule-blindness
classification, the 576-triangle forcedness count, the closed form on 1,824
triangles, the §3 GP-E/t0 table from the two potentials (5); anchors A01, A02,
A03, A04, A05, A07, A08, A09, A10, A11, A12, A13, A15, A16 (14); three anchor
falsifiers (3); the false-claim reconstruction and its kill (1); the completion
criterion against full 81-rebuilds at six sampled completions (6); the
centraliser closed form for 96 (1); the mutant coverage and denominators
recomputed from the receipt (2); three real-source AST falsifiers (3); seven
mutants reconstructed from prose plus the combined false-negative demonstration
(8); the factorisation at three rotations × two wings (1); the 216-extension
disclosure recomputed (1); the 152 degenerate triangles derived (1); the
non-abelian witness with all six orderings and the inversion probe (1); the
fresh-eval arithmetic 8/8/8/0/64 (1); the flip-test and gauge-sweep counts
(1). Zero arithmetic discrepancies with the delivered receipt in any of them.

---

## 9. Grade

Every number in this delivery is correct, the census and its verdict survive an
independent from-scratch rebuild, the anchoring is real and fires on
corruption, the self-correction is genuine and its gate demonstrably bites, and
the mutant table's headline (`never_falsified` EMPTY at 24, both denominators)
is exactly what I recompute. Two of the three waiver-only gates are stronger
than the unit claims. That is a high floor.

Against it: three claims the unit makes **about its own evidence** do not hold
under attack — the 576 "free" triangles are forced by a coboundary structure the
unit never measures (§1); the verdict's derivation is asserted to be re-derived
inside its gate and is not, so an inverted decision rule prints the opposite
verdict at exit 0 (§2); and the census's "independent route" is a distributivity
identity that lets a 192-triangle omission through with both routes agreeing and
no gate anywhere catching it (§3). None of the three moves a number, none
changes `COC-COCYCLE-CLOSES`, and all three are repairable inside the existing
instrument — but all three are the instrument lens's own business, and the first
is a genuine understatement of how narrow the closure result is.

> ### **ACCEPT-WITH-FIXES**

**Required before terminal:** §1 (measure the coboundary; restate the free/forced
split in §5.4, §6, §11.4 and D4), §2 (gate the verdict's derivation), §3 (gate the
census's exhaustiveness against a computed arena; soften "independent route").
**Recommended:** §4 (a mutant against `COC-MEMBERSHIP`'s tabulation), MINOR-1
(sweep the factorisation), MINOR-2, MINOR-3, MINOR-4, MINOR-5.
**Offered for adoption:** the closed form `δ = ∏_{REAL edges} w_X w_Y`
(1,824/1,824), and `96 = |C_{S₉}(σ) ∩ Stab(0)| = 2·48` as the derivation behind
the completion sweep.
