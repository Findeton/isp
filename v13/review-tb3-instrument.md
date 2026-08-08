# TB3 — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens.  **Protocol:** `v13/note-tb3-hostile-protocol.md`
(FROZEN, v13 #279), kill-shots K1–K5, primary weight on **K5**.
**Object reviewed, SHA-256 verified before reading:**

| artifact | declared | measured | ok |
|---|---|---|---|
| `v13/paper-tb3-third-base.md` | `0a9c5dff0e92` | `0a9c5dff0e9245fa1282f305971d90ca…` | yes |
| `v13/code/tb3_third_base_exact.py` | `0fe72a05970b` | `0fe72a05970b2f85ef2e3df5bf08bc6b…` | yes |
| `v13/code/tb3_third_base_output.txt` | `a14684073857` | `a14684073857c64b885de3fc87a1b050…` | yes |
| `v13/code/tb3_third_base_receipt.json` | `3cd7981d173e` | `3cd7981d173ea379ff3f9fe107cca63d…` | yes |

**Independent recomputations and probes performed: 51.**  All scratch work in
the session scratchpad; no repository file was modified other than this review.
Recomputation was done from the paper's declarations in a deliberately
different representation (dense exact-rational matrices against the
instrument's sparse-column `Mat`), without importing the instrument, except
where a probe is explicitly a *scope* probe of the instrument's own
measurement and is labelled as such.

---

## 0. Summary

The **measurements are sound**.  I could not find a false number anywhere I
was able to reach, and the heaviest independent recomputations — all 576
completion entries, the 5,040-completion ord census, deviation 1's order-7
claim, the four rule-selected completions, the S7 sample, the 384 → 6 arena —
reproduce **exactly**.  The delivered artifacts reproduce **byte for byte**.

What fails is the instrument's **account of itself**, in three places, each
verified by a probe that survives when the paper says it should die:

1. the computed qualifiers are **not gated**, though §10 says they are (MAJOR);
2. the holonomy "two independent routes" is **one route**, shares the whole
   graph, and is measured to catch **nothing** (MODERATE);
3. §12 claims a receipt field that **does not exist** (MODERATE).

Two further scope overstatements (§2.8's clause 1; §1's control-coverage
sentence) and four minor labelling items follow.  None moves a physics number.

**Grade: ACCEPT-WITH-FIXES** (stated in full at the end).

---

## 1. MAJOR — F1. The computed qualifiers are ungated; two probes survive

**Claim under test.** §10: "Every verdict string, **the qualifiers included**,
is re-derived inside its own gate from the recorded measurements by an
evaluation that does not call the emitter, and gated against the string that
was emitted."  §6.3: "the qualifier is not a literal — it is **appended
exactly when** the census measures a pair meeting all three conditions."

**Evidence.**  Two source perturbations, run to completion:

| probe | perturbation | tables | result |
|---|---|---|---|
| **P1** | A2's qualifier counts typed false: `53 of 54 cells`, `at 99`, `the 7 involutions` | untouched, still 54/54, 36, 4 | **exit 0**, `failed_gates: []`, `failed_anchors: []` |
| **P2** | A4's `-AT-FIXED-BORN-SHADOW` appended unconditionally **and** the witness list emptied | untouched | **exit 0**, `failed_gates: []`, `failed_anchors: []` |

What is actually re-derived is the verdict **word**, never the qualifier:

- `TB3-A2` re-derives `re_form ∈ {HOLDS-VERBATIM, GENERALIZES, FAILS}` from
  `tab["form_hits"]` and gates `re_form == form` (lines 2004–2011, 2031).  The
  qualifier string built at lines 1965–1969 is never rebuilt or compared.
- `TB3-A4`'s predicate is `dev == 0 and cells == 54 and len(prows) ==
  forced_pairs` (line 2592).  It never reads `qual`.  Its **claim text**
  nevertheless asserts the qualifier is appended "exactly when the census
  measures a pair that … — three measured conditions, all required".  That is
  a gate whose prose describes a check its predicate does not perform.
- `TB3-VERDICT`'s `axis_vocab` (lines 3457–3460) checks only
  `a1_verdict, a3_verdict, a5_verdict` — a2 and a4, the two carrying
  qualifiers, are excluded.

The mutant §10 names as covering this — `verdict-nowitness` — truncates
`returned` inside `run_verdict` (line 3442).  It is a **unit-verdict** mutant;
despite its name it never touches A4's witness census.  So no declared mutant
proves the qualifier derivation can fail, which is precisely what RUNBOOK §13
addendum (#234) requires: "an ungated verdict is a typo away from fiction."
Here it is two probes away.

**Severity: MAJOR** — as a claim.  The underlying measurements (54/54, 36,
4 involutions, one witness pair) are all independently correct; what is
overstated is the guarantee attached to how they are printed.

**Repair.**
(a) In `TB3-A2`, rebuild the qualifier string from `tab` inside the gate and
gate it against `FINDINGS["a2_verdict"]`.
(b) In `TB3-A4`, gate `qual == ("-AT-FIXED-BORN-SHADOW" if tab["witness_count"]
else "")` **and** `FINDINGS["a4_verdict"].endswith(qual)`.
(c) Declare two mutants — `qual-typed`, `qual-free` — so the falsification
census records that the derivation can fail.
(d) Failing (a)–(c), delete "the qualifiers included" from §10 and the
"appended exactly when" sentence from §6.3.

---

## 2. MODERATE — F2. The holonomy "two independent routes" is one route

**K5(c), decided.**  Per #234 ("a pair related by an algebraic identity is one
route, and a cell-completeness gate must catch a dropped cell") the second
holonomy route does **not** qualify as independent.

**They share the substantive intermediate object.**  `group_two_routes` calls
`build_graph` **once** and hands the same `nodes, links` — every link matrix
included — to both routes (lines 1678–1681).  §11.8 says "'Two routes' here
means two computations that **share no intermediate value**", and the
`closure_right` docstring repeats it.  Measured: they share all of it.

**The closure difference is an algebraic identity.**  `closure_left(S)` and
`closure_right(S)` both return the subgroup ⟨S⟩.  Verified directly: on route
A's own 121 generators both return the same set, order 2160.  The only
residual difference is the generating set, and ⟨S_A⟩ = ⟨S_B⟩ is the standard
spanning-tree-independence theorem — a theorem, not a second measurement.

**The dropped-walk probe (demanded by the brief).**  At the reference instance
(30 nodes, 150 links, rank 121, |Hol| = 2160):

| probe | result |
|---|---|
| drop one of route A's **121 generators**, compare against route B's group | group stays 2160 and the routes still agree at **121 of 121** |
| drop one of the **150 links** from the shared graph, recompute both routes | routes still agree at **150 of 150**; \|Hol\| unchanged at **150 of 150** |

The gate is blind to a dropped generating walk everywhere, and blind to a
dropped link by construction, since corrupting the shared object moves both
routes identically.  No declared mutant perturbs one holonomy route only.

**And the independence property is false at one delivered target.**
`different_cotrees` appears at exactly two code sites (1697, 1744), is
**gated nowhere**, and is recorded only at the four A1 targets — where it is
**`False` at the ord-1 target**.  There the second route uses the *same*
spanning tree and the *same* generators, so only the closure side differs,
i.e. the identity above.  §3.2 states without qualification that the two trees
are "measured to have a **different cotree**, hence different generators and
different loops", and deviation 7 repeats it.  Both are false at 1 of 4.

**Not all routes are like this — the contrast is instructive and should be
kept.**  The ord census's route 2 (label formula `σ⁻¹q⁻¹σq`, **no matrix at
all**) is genuinely independent; the walk census's route 2 (transfer recursion
that counts without building a walk) is a genuinely different algorithm and
`reduce-lax` kills it differentially; the triangle census's two routes are
differentially falsified by `tri-cell-drop`.  The holonomy group is the one
census where the second route is a re-parameterisation.

**Repair.**  Scope §11.8's "share no intermediate value" to the ord and walk
censuses.  Describe the holonomy second route as what it is — a spanning-tree
and closure-direction re-derivation — and print its measured power (0/150
link drops, 0/121 generator drops detected).  Gate `different_cotrees`, or
drop the "measured to have a different cotree" claim, which is false at the
ord-1 target.  Add a route-differential mutant (drop one cotree generator in
route A only); if it cannot die, report that as the finding.

---

## 3. MODERATE — F3. §12 claims a receipt field the receipt does not contain

§12: "the `carrier-lax` mutant, which makes the carrier index non-injective
and then cannot proceed, is recorded as falsifying `TB3-CARRIER` **and as
aborted**."

Measured, by running the mutant:

```
pipeline aborted: RuntimeError('order overflow')
KILL-JSON {"failed_anchors": [], "failed_gates": ["TB3-CARRIER"], "aborted": true}
```

The subprocess **does** emit `aborted`.  But `_run` (lines 3596–3607) reads
only `failed_anchors`, `failed_gates` and `crashed`; the `aborted` key is
discarded.  The delivered receipt records
`carrier-lax → crashed_before_reporting: False`, and the string `aborted`
occurs **nowhere** in `tb3_third_base_receipt.json`.

So the capability the paragraph advertises — "the census can distinguish
'died at a gate' from 'died at a traceback'" — is not realised in the
delivered census: **0 of 42** rows carry the distinguishing datum, and
`crashed_before_reporting` (which is `False` for all 42) means something else
entirely (no KILL-JSON at all).

**Repair.**  Propagate `kill.get("aborted", False)` into the row and into the
receipt, or delete the sentence.

---

## 4. MODERATE — F4. Clause 1 is analytically forced, not measured inert

**K5(d), part 1.**  §2.8 tabulates all four predicate clauses as measurements
and glosses the result: "only the leg-key clause is load-bearing; the other
three are **measured inert**, their content already implied by it."  For
clause 1 that is a misattribution.

The predicate quantifies over `sp.PERMS` — the **six wing symmetries**
(`Species.__init__`, line 737).  For every one of them σ_π(0) = 0, because the
all-zero triple is symmetric, hence `PCARR[π][J0] = idx(0,0) = J0` identically.
Measured over all six: the j0 clause excludes **0 of 6**, by algebra.  Its
"0 of 10 cells change" row could not have come out any other way.  Clause 1 is
not redundant *because clause 2 implies it*; it is a tautology at this
quantifier, and clause 2 has nothing to do with it.

This is exactly the case RUNBOOK §14 addendum (#208) names:
"Analytically-forced clauses (true by algebra for every input) are
**disclosures**, not must-pass gates."  Here it sits in a table of
measurements, indistinguishable from clauses 3 and 4, which are contingently
inert.

**Distinguish the sound use.**  On the **declared 384-element relabelling
scope** the same filter *is* substantive: I independently constructed the
scope (wing permutations × system bit-flips × pointer bit-flips) and applied
the filter, getting **384 → 6**, measured to be exactly S₃ — reproducing §2.7
entry for entry.  §2.7 is sound; §2.8's clause-1 row quantifies over the 6,
not the 384, and the two roles of "the j0 filter" are conflated.

**Repair.**  Mark clause 1 as analytically forced at this quantifier with the
one-line reason, and keep clauses 3 and 4 as the measured-inert rows.

**F4b (LOW) — the inertness is measured at one world and stated at base
scope.**  `run_clause_census` builds a single
`World(sp, psi-G1, Q, ("R0","R0","R0"))`.  §2.8 states the result as a fact
about "this base".  I re-ran the same measurement at six instances:

| instance | links | c1 | c2 | c3 | c4 |
|---|---|---|---|---|---|
| psi-G1 / TB-000 (the world the paper measures) | 252 | 0/10 | **10/10** | 0/10 | 0/10 |
| psi-W1 / TB-000 | 132 | 0/10 | **10/10** | 0/10 | 0/10 |
| psi-W3 / TB-000 | 102 | 0/10 | **5/10** | 0/10 | 0/10 |
| psi-G1 / TB-001 (partially symmetric) | 132 | 0/10 | **10/10** | 0/10 | 0/10 |
| psi-G1 / TB-012 (asymmetric) | 102 | 0/10 | **5/10** | 0/10 | 0/10 |
| psi-P / TB-000 | 118 | 0/10 | **5/10** | 0/10 | 0/10 |

The generalisation **holds** — clauses 1, 3, 4 are inert at all six.  So the
conclusion is right; it was measured once and stated unscoped, which is the
#40 F1/F2 rule ("scope tags at the claim, not just the receipt").  Report the
sweep or scope the sentence.

**On the mutant re-targeting (K5(d), part 2): the re-targeting is CORRECT and
should stand.**  A mutant dropping an inert clause cannot die and would have
inflated the census with a falsifier that falsifies nothing; deviation 9 says
exactly this and it is right.  `legkey-lax` targets clause 2, the clause
measured able to fire, and it dies at four named gates plus six XBA anchors.
No gate predicate references mutant identity (`TB3-NO-MUTANT-EXEMPTION`
sweeps the AST for it and `exempt-lax` kills it), so #208's other half is
honoured.  The one cost — that clauses 1, 3, 4 are now untested by any
mutant — is real but unavoidable and is not concealed.

---

## 5. MODERATE — F5. §1's coverage sentence exceeds the two-wing control

**K5(b), decided.**  §1 states: "The machinery is written generic in the wing
count, so the positive control is the same code at two wings and **a defect in
the three-wing measurement is a defect in the two-wing anchor**."  That is a
universal coverage claim.  Measured, it is false for every axis-specific
defect.

**What the control anchors.**  It realises defect orders **1 and 3 only**.
Its 22 external anchors resolve to three committed instances, which I traced
by hand into the source receipts:

| anchor block | source location |
|---|---|
| A-XBA-NODES/LINKS/RANK/IDLINKS/WALKS/WALKS-ROUTE2/WALKS-ALL/REDUCED-ALL | `xba…/tables/arena/*` (= XBA's **base T**, ord 3) |
| A-XBA-PROFILE-ord3, A-XBA-GROUP-ord3 | `xba…/tables/the_commutator_law/base T/` |
| A-PSI-*-ord3 | `psi…/tables/negative_control/per_control/Q-negA` |
| A-PSI-*-ord1 | `psi…/tables/negative_control/per_control/Q-negB` |

XBA's own committed instance set is **{6 × ord-2, 1 × ord-1, 1 × ord-3}**, so
the control reproduces XBA at **1 of its 8 instances**, and the Klein profile
`82/86/90/106` with |⟨W,D⟩| = 4 — XBA's *modal* case — is read out of the
receipt (`class_count_profiles_by_defect_order["2"]`) but never anchored.

**Mutant-coverage measurement.**  Of the 42 declared mutants, **8** are caught
by an external XBA/PSI **value** anchor (`anchor-record`, `legkey-lax`,
`id-lax`, `scope-lax`, `readtime-conflate`, `loopname-collapse`, `reduce-lax`,
`orient-flip`); 3 by a self-anchor; 1 by a hash pin; 30 by gates alone.  Every
one of the **12 axis-specific mutants** — `a1-drop`, `ordcensus-half`,
`form-order`, `cocycle-drop`, `cocycle-subsample`, `a3-drop`, `tri-cell-drop`,
`efactor-lax`, `pair-drop`, `a5-drop`, `survive-lax`, `s7-lax` — is caught by
internal gates with **zero external-anchor coverage**.

**Structurally the control cannot reach the loci the findings live on.**  At
two wings the wing symmetry group is Z/2: there are **no non-involution
cells**, so A2's entire finding (F1 vs F3 differ at the three-cycles, 36/54
against 54/54) is outside the control's reach; there are 2 frames, not 6, so
A3's atlas and triangle census are never exercised at two wings; and GHZ/W
does not exist below three wings, so A4 is unreachable.

**What is honest and should be kept.**  §8.2's per-axis control map does **not**
overclaim — it correctly names A2's, A3's and A4's positive controls as
*internal* (the involution sub-locus, the two centralising instances,
`psi-G3`), and only A1's and A5's as anchored.  Deviation 3 and §8.1 disclose
the ord-2 gap accurately, print the computed reason, and make no order-2
claim.  §11.4 states the self-anchor limitation correctly.  **The defect is
confined to §1's sentence** and the framing it licenses.

**Answering the brief's question directly — does any claim's scope exceed what
the control covers?**  Yes, exactly one: §1's "a defect in the three-wing
measurement is a defect in the two-wing anchor."  No table, no verdict and no
deviation depends on it.

**Repair.**  Replace §1's sentence with the measured version: the control
anchors the wing-count-generic machinery — legs, record injectivity, admission
rules, walk enumeration, orientation, reduction, scope, read time, link naming
— at two realised defect orders; it does not reach the non-involution,
six-frame or multipartite loci, and 12 of 12 axis-specific mutants are caught
internally.

---

## 6. MINOR findings

**F6 (LOW) — the 12 rotation anchors are self-anchors and are not labelled as
such.**  `ROT_PINNED` (typed, line 382) is compared against `rotation(g)`
built from `ROT_PYTH` (typed, line 380, same file) — structurally identical to
the 576 completion self-anchors.  Their `source` field reads `"this file,
pinned data"` while the completions read `"SELF-ANCHOR (this file, pinned
completion)"`.  §12's totals row — "610 — 576 completion self-anchors, 12
rotation anchors, 4 receipt hash-pins, 10 XBA anchors, 8 PSI anchors" —
invites reading the remaining 34 as external.  The honest partition is **588
self-anchors and 22 external** (4 hash pins + 10 XBA + 8 PSI).  §2.2's prose
("pinned as data and anchored entry by entry **against the constructor**") is
accurate; only the aggregate framing is loose.  *Repair:* label them
SELF-ANCHOR and print the 588/22 split.

**F7 (LOW) — two of the four hash pins guard nothing.**  GEN and COC are
hash-pinned and gated, but no value from either enters any anchor or table
(`TABLES["external"]` is read only for XBA at 2639/2811 and PSI at 2812).
§12's "The four committed receipts this unit **anchors against**" is true of
two of them.  All four pins do fire (§8 below), so this is a provenance
nicety, not a defect.  *Repair:* "hash-pinned; XBA and PSI additionally supply
anchored values."

**F8 (LOW) — the paper's one-law verdict is not the gated string.**  Receipt:
`TB3-ONE-LAW-GENERALIZES-<D_P = F3_group_commutator_Pinv_u reproduces …>`.
Paper: `TB3-ONE-LAW-GENERALIZES-⟨D_P = [P⁻¹, u] reproduces …⟩`.  The
translation is faithful (F3 = [P⁻¹,u] per §4.1) but for a unit whose
discipline is gated verdict strings, the paper should quote the gated string
verbatim or state that it renders the internal form name.

---

## 7. K1 and K4 at the depth the brief assigns

**K1 — one independent recomputation of the ord census distribution.**  From
scratch, enumerating all 7! label permutations fixing label 0 and taking the
order of `σ⁻¹q⁻¹σq` at P\* = the lex-first non-identity element of S₃:

| ord | 1 | 2 | 3 | 4 | 5 | 6 | total |
|---|---|---|---|---|---|---|---|
| completions | 48 | 384 | 1728 | 1152 | 1152 | 576 | **5040** |

Identical to §3.1.  P\* is independently confirmed to be `ACB`, the
transposition of wings B and C, with σ = (0,2,1,3,4,6,5,7).  Maximum at P\* is
**6**.  Deviation 1's claim verified independently: sweeping every element of
S₃, order **7 occurs at the two 3-cycles (`BCA`, `CAB`) and at no
transposition** — so "the maximum the carrier admits" is 6 at P\* and 7 at a
3-cycle, and both numbers are printed as the deviation says.  The four
rule-selected completions reproduce exactly: ord 1 → identity, ord 2 →
`(0,1,2,3,5,4,7,6)`, ord 3 → `(0,1,2,3,4,5,7,6)`, ord 6 → `(0,1,3,2,5,4,7,6)`,
matching §3.2's table.

**K4 — the witness pair's equalities re-verified.**  For (`psi-W1`, `psi-W4`):

| # | equality | measured |
|---|---|---|
| 1 | Born shadows equal | **yes** — independently recomputed; the *only* two Born-shadow-sharing pairs in the family are (G1,G3) and (W1,W4), reproducing §2.5 |
| 2 | admission tables agree cell for cell | **yes**, all 10 (checkpoint, rule) cells |
| 3 | links | **90 = 90** |
| 4 | cycle rank | **61 = 61** |
| 5 | Born-shadow stabiliser | **2 = 2** (while wing stabilisers differ, 2 vs 1 — independently reproduced, including psi-W4's 1/2 asymmetry) |
| 6 | common named loops / of which Born holonomy differs | **61 / 14** — against the in-family negative control (G1,G3) at **121 / 0** |

`psi-W4`'s holonomy order is recorded `null`, not a number; deviation 8 is
honoured, and §11.7's refusal to substitute a readable subgroup is carried in
the receipt.  The 14 differing loops are the same 14 on which W4's generators
leave the permutation class (61 − 47 readable), which is what §6.3 says.

---

## 8. Verified with no defect found (recorded so the panel need not repeat it)

- **Frozen hashes.** All four SHA-256s match the pin exactly.
- **The four external pins.** Each receipt's SHA-256 matches its typed
  constant, verified outside the instrument.  **Corrupt-and-fire on all four**
  (one appended byte each, run separately): each fires **its own** named
  anchor — `A-PIN-XBA` / `A-PIN-GEN` / `A-PIN-COC` / `A-PIN-PSI` — plus
  `TB3-EXTERNAL-PINS`, exit 1.  The delivered `pin-hash` mutant tests XBA
  only; the other three now have evidence.
- **The external anchors genuinely read external bytes.**  Patching
  `xba…/tables/arena/links` 13 → 14 and `psi…/…/Q-negB/links` 11 → 12 **and
  re-pinning both hashes so the hash gate passes** fires exactly
  `A-XBA-LINKS` and `A-PSI-LINKS-ord1`, plus `TB3-POSITIVE-CONTROL`, exit 1.
  The XBA/PSI numbers are read, not typed.
- **Anchors are fatal.** `build_receipt` folds failed anchors into
  `must_pass_failures` (line 3672), so "610 anchors, all exit-1" is true, and
  the probe above demonstrates it.
- **The 576 completion self-anchors are not circular in the damaging sense.**
  An independent implementation of the *declared rule* — Householder
  `I − 2wwᵀ/wᵀw` with `w = ψ − e₀`, then the lex-first transposition (i,j),
  1 ≤ i < j < 8, whose completion has a Born shadow invariant under no
  non-identity wing symmetry — independently selects **Q = (0,3,2,1,4,5,6,7)**
  and reproduces **576 / 576** entries of `PINNED_V`, including all 20
  declared spot checks.  All 9 completions are exactly orthogonal with ψ as
  first column, and all 9 are printed in full in the output artifact as
  claimed.  §2.5's table (class, 3-tangle 576/625, wing stabiliser,
  Born-shadow stabiliser) reproduces entry for entry.  The self-anchors buy
  what §2.6 and §11.4 say they buy, no more, and the limitation is stated
  correctly.
- **The [SAMP]s are honest (K5(f)).**  *S7:* my independently computed
  lex-first five completions at the modal order (3, with 1,728 members) are
  **exactly** the receipt's five; `S7_sample_declared_size` 5 =
  `S7_sample_size` 5, both printed; the measured answer — holonomy orders
  {72, 72, 72, 72, 2160} — is a **refutation**, which a larger sample can only
  strengthen, as deviation 5 argues correctly.  `s7-lax` (sample shrunk to one,
  so a collision cannot occur) dies at `TB3-A5`.  *A3:* 5 declared instances,
  5 measured, both recorded, scope printed with the table and repeated in
  §11.3 and deviation 4.
- **Mutant census (K5(e)).**  All **42 die** (exit 1), 38 computation + 4
  waivers as declared.  `never_falsified` is **EMPTY** at honest denominators:
  26/26 must-pass gates falsified by some mutant, 24/26 by a computation
  mutant, both denominators reported, the two waiver-only gates
  (`TB3-EXACTNESS`, `TB3-NO-MUTANT-EXEMPTION`) **named** rather than averaged
  away, and the single excluded gate (`TB3-FALSIFICATION`, which cannot run
  inside a mutant) named.  This is the correct treatment.
- **Verdict-in-gate, unit level (K5(e)).**  `TB3-VERDICT` re-derives the unit
  verdict from the count of axis **tables** recorded, while the emitter counts
  axis **verdict strings** — genuinely different quantities, so a perturbation
  of either moves one side only.  The flip probe is real: `verdict-order`
  (branch order swapped), `verdict-nowitness` (emitter input truncated,
  tables intact) and `verdict-lax` (out-of-vocabulary) all die there.  This
  satisfies #234 for the unit verdict.  It is only the **qualifiers** that
  escape (F1).
- **Cell completeness (K5(e)).**  Nine forced-vs-measured counts, each
  computed from the declaration (a factorial, a product, a binomial) and
  gated: 270, 54, 36, 4, 5, 5040, 8, 576, 54 — all matching.  The three
  censuses the brief names each have a working dropped-cell catcher:
  ord census → `ordcensus-half` (kills `TB3-A1-ORDCENSUS` **and**
  `TB3-CELLS`); pair census → `pair-drop` (`TB3-A4` + `TB3-CELLS`);
  triangle census → `tri-cell-drop`, which drops a checkpoint from **route 1
  only** and dies on the route differential at `TB3-A3`.  That last one is
  the model the holonomy routes lack (F2).
- **Symmetry self-test (§9, RUNBOOK §14).**  Every number reproduces:
  18,150 cells = 150 switchings × 121 generators, 0 Born-shadow readings
  moved, 0 permutation parts moved, **366** generators whose sign the
  switching flips (non-vacuous), 121/121 rebuilt from their own directed link
  path by code sharing nothing with the spanning-tree construction, 121/121
  matching an independently read parity of which **84** are negative, 0
  fresh-mode cache hits against a cache measured **populated (8 primed)**,
  **read (8 reads returned a stored value)** and **exercised (8 fresh requests
  for a key already cached)**.  The #219 addendum — "a zero-hit cache gate
  must also gate that the cache path is exercised" — is satisfied, and
  `memo-lax`, `gauge-sign`, `gauge-subsample`, `orient-flip` all die here.
- **Declaration order.**  `TB3-FREEZE` is gate 0 with the transport-datum
  counter at zero; `TB3-DECLARATION-ORDER` gates that every declaration gate
  precedes the first transport gate; `order-lax` and `freeze-lax` die.  §2's
  disclaimer — that this records ordering *within one execution* and is not
  offered as proof the declarations preceded fixture truth — is the correct
  and honest statement.
- **Negative controls (§8.3)** reproduce exactly: reference 150/121/**2160**;
  equivariant 99/70/**1**; a different declared transposition 111/82/**18**;
  asymmetric setting 75/46/**1**.  `negcontrol-lax` kills them.
- **Byte-identical delivery.**  My independent run reproduces
  `tb3_third_base_output.txt` and `tb3_third_base_receipt.json` **byte for
  byte**, md5 `ad50b739c5936a875fdccfd324202c6f` and
  `2197c13ba96bfcffe1385b618bef8c61`, exactly as §12 declares.

---

## 9. Grade

**ACCEPT-WITH-FIXES.**

I tried to refute the numbers and failed: every quantity I could recompute
independently — 576 completion entries, the 5,040-completion census and its
full distribution, the maximum order at P\*, the order-7 behaviour at the
3-cycles, the four rule-selected completions, the S7 sample, the 384 → 6
arena, the Born-shadow pair census, the family's classes and stabilisers —
reproduces exactly, and the delivered artifacts reproduce byte for byte.  The
external anchoring is real: the values are read from the committed receipts,
the anchors are fatal, and all four pins fire when corrupted.  The [SAMP]s are
honest, the denominators are honest, `never_falsified` is genuinely empty, and
the unit's disclosure discipline — deviations 1, 3, 4, 5, 7, 8, 9, §11's
non-claims — is unusually good.  Nothing in this review moves a physics
number.

What must be fixed is the instrument's self-description, where three claims
are measurably stronger than the instrument:

1. **F1 (MAJOR).** §10's "the qualifiers included" is false; A2's qualifier
   counts and A4's `-AT-FIXED-BORN-SHADOW` both survive deliberate corruption
   with exit 0 and zero failed gates.  Gate them and declare the two mutants,
   or withdraw the claim.
2. **F2 (MODERATE).** The holonomy "two independent routes" shares the entire
   graph, differs by an algebraic identity plus a tree choice, is measured to
   detect 0 of 121 dropped generators and 0 of 150 dropped links, and its
   stated independence property (`different_cotrees`) is ungated and **false
   at the ord-1 target**.  Restate, gate, and add a route-differential mutant.
3. **F3 (MODERATE).** §12 asserts a receipt field (`aborted`) that the
   collector discards and the receipt does not contain.  Propagate it or
   delete the sentence.

Plus two scope repairs — **F4** (clause 1 is analytically forced, not measured
inert; and the clause census is a one-world measurement stated at base scope,
though I verified it generalises to six) and **F5** (§1's "a defect in the
three-wing measurement is a defect in the two-wing anchor" is false for 12 of
12 axis-specific mutants) — and four minor labelling items (**F6**–**F8**).

None requires re-running the science.  F1, F3, F4, F5, F6, F7 and F8 are prose
or bookkeeping repairs plus small gate additions; only **F2** needs real work —
either a genuinely independent third route for the holonomy group (an orbit or
Schreier construction not routed through a spanning tree) or an honest
restatement of what the second route does and does not test.  With those, the
unit is sound.
