# PSI — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Reviewer:** R3, the instrument lens. **Date:** 2026-08-08.
**Protocol:** `v13/note-psi-hostile-protocol.md` (FROZEN, v13 #251), K1–K5 binding.
**Primary weight:** K5. K1/K2/K4 audited at lower depth as instructed.
**Method:** independent recomputation mandatory; scratch only; no repo file modified;
no child agents; no git.

## 0. Hash verification (performed first)

| object | declared sha256-12 | measured | verdict |
|---|---|---|---|
| `v13/paper-psi-curvature.md` | `e79d0ff48933` | `e79d0ff48933…` | MATCH |
| `v13/code/psi_curvature_exact.py` | `49b3c980e7d8` | `49b3c980e7d8…` | MATCH |
| `v13/code/psi_curvature_output.txt` | `8ea66d096ec8` | `8ea66d096ec8…` | MATCH |
| `v13/code/psi_curvature_receipt.json` | `443cf2460dba` | `443cf2460dba…` | MATCH |

The anchor source was verified too: `v13/code/gen_generality_receipt.json` hashes to
`e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292`, which is the
value hard-typed at `psi_curvature_exact.py:1395` as `A-GEN-SHA`. The GEN receipt on
disk is the file the instrument pins.

Baseline reproduction: a clean run of the frozen instrument in scratch returns
**146 anchors, 20 gates, 0 must-pass failures, exit 0** (the 21st gate,
`PSI-FALSIFICATION`, exists only under `--falsification-selftest`).

---

## 1. Findings, ranked

### F1 — CRITICAL, REQUIRED REPAIR. The printed verdict is ungated. RUNBOOK §13 addendum (#234) is VIOLATED.

**The compliance question I was asked to decide: NONCOMPLIANT.**

RUNBOOK §13 addendum (2026-08-08, from v13 #234) is unambiguous:

> the printed verdict string must be derived inside a gate from the measured counts,
> and a verdict-flip mutant must prove that derivation can fail — an ungated verdict
> is a typo away from fiction.

This unit delivered after the addendum, and the census lists `PSI-VERDICT` as
waiver-only. I probed it. It does not comply.

**Mechanism.** `run_verdict` (lines 2597–2634) derives the verdict *outside* every
gate:

```
    curvature = bool(witnesses)
    path_space = bool(movers)
    if curvature:      v = "PSI-CURVATURE-EXISTS"
    elif path_space:   v = "PSI-PATH-SPACE-DEPENDENCE"
    else:              v = "PSI-DECLARATION-ONLY"
    ...
    inv = v in PREREGISTERED
    gate("PSI-VERDICT", "derivation", "…", inv, {…})
```

The gate's entire predicate is `inv = v in PREREGISTERED` — **a vocabulary-membership
test**. No gate anywhere compares the emitted string against the string the
pre-registered rule selects from the recorded measurements.

**The probe (K5(a), performed as instructed).** In scratch I swapped the branch
assignments so that the measured `curvature = True` selects `"PSI-DECLARATION-ONLY"`
and the `else` branch selects `"PSI-CURVATURE-EXISTS"`. Nothing else was touched.
Result of the full run:

- **exit 0**
- **`must_pass_failures 0`**, `must_pass_gates 20`, **all 20 gates `[PASS]`**, including
  `[PASS] PSI-VERDICT`
- the rendered artifact's tenth line reads
  **`VERDICT: PSI-DECLARATION-ONLY-AT-FIXED-BORN-SHADOW`** — the exact negation of the
  unit's finding — under the same four scope clauses

and the falsified verdict sits in the *same evidence line as the measurements that
refute it*:

```
value: {a_common_loop_differs:True, in_the_pre_registered_vocabulary:True,
        members_with_a_differing_common_loop:(psi-N1,psi-N2),
        the_loop_space_moves:True,
        verdict:PSI-DECLARATION-ONLY-AT-FIXED-BORN-SHADOW}
```

A receipt that records `a_common_loop_differs: True` and prints
`PSI-DECLARATION-ONLY` and exits 0 is precisely the artifact #234 was written to
prevent. `FINDINGS["thesis"]` is built from `TABLES` and does not reference the
verdict, so the JSON receipt would carry
"THE PHYSICAL STATE CONTRIBUTES GEOMETRY…" beside `unit_verdict:
PSI-DECLARATION-ONLY-AT-FIXED-BORN-SHADOW` as well.

**Two aggravating factors.**

1. **The gate's own claim text asserts the thing it does not do.** Lines 2624–2625:
   "The verdict string is re-derived inside this gate from the recorded measurements
   and measured to be the string the rule selects." Paper §9 repeats it verbatim.
   Nothing is re-derived. This is not a missing gate — it is a false description of
   an existing gate, carried into the paper.
2. **The §11 justification for the waiver is refuted by the probe.** §11 says
   `PSI-VERDICT` is carried by a waiver alone "because a verdict vocabulary can only
   be violated by emitting a bad string." A well-formed but *wrong* string is the
   failure mode #234 names, and it is reachable by a one-line computation mutant.

**Repair (required).**
(i) Inside `PSI-VERDICT`, recompute the expected string from the *recorded tables*
    (`TABLES["witness_census"]["members_with_a_differing_common_loop"]`,
    `TABLES["path_space_dependence"]["members_whose_admission_table_moves"]`) rather
    than from the local variables, and gate `v == expected` **as well as**
    `v in PREREGISTERED`.
(ii) Declare a **computation**-kind mutant (`verdict-flip`) that swaps the branch
    assignments, and require it to die at `PSI-VERDICT`.
(iii) Re-run the falsification census; `PSI-VERDICT` must leave
    `falsified_only_by_a_waiver`.
(iv) Correct §9 and the gate claim text, or make them true.

---

### F2 — CRITICAL. Cell-completeness is not gated on either census; two dropped-cell probes pass clean.

#234's second clause: "a cell-completeness gate must catch a dropped cell." Probed on
both censuses as instructed.

**(a) The 48-cell admission comparison — DROPPED CELL NOT CAUGHT.**
In `run_comparison` (line 1569) the per-member admission delta is
`[k for k in sorted(admtab[PSI_REFERENCE]) if …]`. I excluded the single cell
`GP-E/t1/REAL` from that comprehension. Result: **exit 0, all 20 gates pass**, and the
rendered table changes from

```
psi-N3   8      8   0  0  0            ->    psi-N3   7      8   0  0  0
psi-N4   8      8   0  0  0            ->    psi-N4   7      8   0  0  0
```

The paper's §5.1 headline "**8 of 48**", §9's "the cells that move are printed", and
the abstract's "lose the realized rule's identifications at **8** cells" are all
ungated. `PSI-PATH-SPACE-DEPENDENCE`'s predicate tests only *link counts*
(`sizes[nm][sp]["links"] != ref[sp]["links"]`), never the delta cell set or its size.

**(b) The 48-member sign-flip census — SUBSAMPLING NOT CAUGHT.**
`PSI-SIGNFLIP-CENSUS`'s only size clause is `total > 2 * len(inv_members)` — i.e.
`> 14`, a lower bound, not a completeness check. I halved the pattern list per member.
Result: **exit 0, all 20 gates pass**, receipt prints `sub_family_size: 26`,
`patterns_that_move_the_holonomy: 13`, while the gate continues to assert
"THE SIGN-FLIP CENSUS IS **EXHAUSTIVE** OVER THE DECLARED SUB-FAMILY" and the paper
continues to call it "the one exhaustive object in the unit" (§10.3).

**What the unit does get right, and it deserves credit.** Dropping a cell from the
admission *table construction* (`run_sweep`, all members) **does** fire: exit 1,
`[FAIL] PSI-POSITIVE-CONTROL`, 2 must-pass failures, and the external anchor tally
moves to **36 of 37 passed** — i.e. exactly one anchor catches it. That anchor is
`A-GEN-ADMISSION`, a dict equality between `mine_cells` and a 48-key dict built
independently from GEN's receipt: a genuine external cell-completeness route, and the
only one in the unit. It covers **only the reference member's table**. The sign-flip
census constructs fresh `World`s and never touches `admtab`; the comparison census
reads `admtab` but its *key set* is the thing I dropped, and `A-GEN-ADMISSION` checks
the table, not the delta. Neither census inherits any protection from it.

**Repair.** Gate `cells == len(SETTING_ORDER)*len(CHECKPOINTS)*len(ID_RULES)`; gate
that each member's delta loop ranges over the reference table's full key set; gate
`total == Σ_members 2^{|support \ {0}|}` computed from the declared family; add a
dropped-cell mutant for each census.

---

### F3 — MAJOR. The stated justification for the `PSI-VERDICT` waiver is a non-sequitur, and it is what conceals F1.

§11 names the three waiver-only gates and justifies each: `PSI-EXACT` and
`PSI-NO-MUTANT-EXEMPTION` "because their input is this module's own source text, which
freeze-on-delivery forbids editing, and the third **because a verdict vocabulary can
only be violated by emitting a bad string**."

The third clause is false, and F1 is the counterexample. A verdict can also be violated
by emitting a **well-formed but wrong** string, which is the failure #234 names, and a
mutant that does so is a one-line, computation-kind perturbation of the derivation.

I audited the six waivers against the unit's own definition ("A waiver overwrites a
gate's computed predicate after the fact"):

| mutant | injection | true predicate overwrite? |
|---|---|---|
| `control-lax` | `if overwrite…: ok = False` (1985–86) | **yes** |
| `witness-lax` | `ok = (… and not overwrite_the_witness)` (2520) | **yes** |
| `flip-lax` | `… and not overwrite_the_flip_test` (2434) | **yes** |
| `float-lax` | `lits.append(0)` (2725) | no — overwrites the AST sweep's *output* |
| `exempt-lax` | `found.append(0)` (2678) | no — same shape |
| `verdict-lax` | `v = "PSI-STATE-CARRIES-GEOMETRY"` (2605–07) | no — overwrites the derivation's *output* |

In fairness to the unit, the last three share one shape — they overwrite a computed
*result* that the predicate then reads, rather than the predicate itself — and calling
all three "waivers" is defensible under that looser reading. **But that reading is
exactly the diagnosis.** `verdict-lax` earns its waiver status *precisely by bypassing
the derivation instead of perturbing it*; the unit then infers from that status that
the gate is unreachable by computation. Under either reading of the taxonomy, the
inference does not follow, and the missing mutant — the one that perturbs the
derivation rather than its output — is the mutant #234 requires by name.

For `PSI-EXACT` and `PSI-NO-MUTANT-EXEMPTION` the parallel justification **is** sound:
their input really is an AST sweep of the frozen source, which cannot be perturbed
without an edit freeze-on-delivery forbids. Those two waivers I accept. A cheap repair
exists for them too — run each sweep over a *parameterised* source string rather than
over `__file__` alone — but I do not score its absence as a defect.

**On the other two waiver-only gates: legitimate.** `PSI-EXACT` and
`PSI-NO-MUTANT-EXEMPTION` both take their input from an AST sweep of
`Path(__file__).read_text()`, which freeze-on-delivery forbids editing. The waiver
argument is sound. A repair exists and is cheap — run each sweep over a *parameterised*
source string (a copy with an injected float / an injected `MUTANT != …`) rather than
over `__file__` alone — but I do not score their absence as a defect.

---

### F4 — MAJOR. The paper's provenance claim for the 81 completion anchors is false; §2.2 contradicts §11.

Paper §2.2: "for GEN's own ψ the constructed V is anchored entry by entry against
**GEN's pinned 9×9 matrix** — **81** anchors — so this unit's completion of the
reference member *is* GEN's completion and not a rebuild of it."

Measured:

- All 81 `A-V-ij` anchors carry `source = "this unit's pinned declaration of base G"`
  and compare the constructor against `PINNED_V_OF_PSI_G`, a matrix **typed at line
  251 of this same file** (`psi_curvature_exact.py:1181–83`).
- I searched GEN's committed receipt exhaustively. **It does not contain V's entries
  at all** — only the string `"V": "H . Q, the pinned matrix of section 1"` and
  derived quantities. External anchoring of V was therefore impossible.
- The inference "*is* GEN's completion and not a rebuild of it" does not follow from a
  self-anchor: a self-anchor proves the constructor agrees with the typed copy, and a
  mistranscribed copy would pass all 81.
- §11 describes the same 81 anchors **correctly** as self-anchors ("109 are
  self-anchors against this unit's own pinned declaration of base G … and the full 9×9
  completion of the reference preparation entry by entry"). The paper contradicts
  itself.

**The value is not in question.** I recomputed `V = H(ψ_G)·Q` from scratch in exact
rationals and reproduced all 81 typed entries with **0 mismatches**; column 0 is ψ_G
and V is exactly orthogonal over ℚ.

**A cheap repair is available and should be taken.** GEN's receipt *does* record
`the_declared_completions_entry.the_defect_permutation = [0,2,1,6,4,5,3,7,8]`, and my
independent computation of δ(Q_pinned) = σQ⁻¹σQ reproduces that permutation exactly.
Anchoring that permutation entry-by-entry would convert the completion's provenance
into a genuine external anchor. `A-GEN-DEFECT` currently anchors only
`[order, fixed_points] = [2, 45]` and leaves the permutation itself unused.

---

### F5 — MODERATE. The headline comparison numbers (206, 196, 2) are printed but not gated, and the flat→non-flat witness is the one witness with no independent rebuild.

`PSI-WITNESS`'s predicate is `len(witnesses) > 0 and rebuilds_ok and invariant_quiet`.
Neither `common_loops_whose_born_holonomy_differs` (206) nor
`common_loops_flat_at_the_reference_and_not_here` (2) enters any gate predicate
anywhere in the instrument.

`run_witness` rebuilds the *born* witness by the declared independent route
(lines 2466–2472: `named_edges` + `loop_matrix_fresh(memoised=False)`, with
`the_independent_rebuilds_differ` measured). The `flat_wit` loop (2490–2498) records
a name and a length and **nothing else** — no rebuild, no comparator. That is the
witness the paper calls "the sharpest form the witness can take" (§5.3) and puts in
the abstract ("**2** of those loops are **flat at the reference and not flat at it**").

**Two mitigations, both real.** First, the doubled realized prep bigon is one of the
four `DECLARED_PROBES`, so its Born shadow is swept complete under the switching group
at both ψ_G and ψ_N1 as part of the 66,560 comparisons. Second, I recomputed it
myself (see §2): the fact is sound. What is missing is the *gate* on the count and the
*rebuild* on the loop.

**Repair.** Require `flat_wit` non-empty whenever `curv` is non-empty; rebuild the
flat witness by the independent route as the born witness is; put the printed counts
into a predicate.

---

### F6 — MODERATE. The negative control's second leg contains a fitted branch, and its "links refused" half is ungated.

`run_negative_control:2051` computes `predicted = 1 if n == 1 else 2*n`. GEN's
dihedral law as the paper states it (§7.2) gives order 2n; for n = 1 that is **2**,
not 1. The `n == 1 → 1` special case is **typed into this instrument** and is not
anchored against GEN's receipt. D3 sources it to GEN §7.2 in prose — links refused for
want of uniqueness on the equivariant locus — but prose is not an anchor, so Q-negB's
"the prediction is met" is partly a branch chosen to match the outcome.

Separately, the compound prediction's second half — "with links refused" — is printed
(13 links at the pinned Q, **11** at Q-negB) but does **not** appear in the gate
predicate, which tests only `the_prediction_is_met` and
`the_holonomy_moved_from_the_pinned_Q`.

**The control still has teeth, because of its other leg.** Q-negA is clean and
genuinely out-of-sample: I independently computed δ(Q-negA) = [0,3,2,4,1,5,6,7,8], of
order 3, so the dihedral law predicts 6 and non-abelian before anything is enumerated;
the instrument's fresh enumeration measures **6** and **non-abelian**. That leg alone
establishes that a declaration change moves this instrument.

**Repair.** Anchor the equivariant-locus branch against GEN's receipt, or state it as
a declared disclosure rather than a prediction; add the link refusal to the predicate.

---

### F7 — LOW (no defect found). The readable/unreadable split: probed for silent drops, none found.

The protocol asked whether unreadability is handled by silent dropping, and whether
D7's Born-shadow comparator is gated with its own falsifier. Measured:

- At ψ-N1: `common_loops_whose_born_holonomy_differs` = 206,
  `common_loops_whose_permutation_part_differs` = 206,
  `common_loops_where_readability_flips` = **206**. All three coincide. Every loop on
  which the permutation part "differs" is a loop on which it becomes **undefined**.
  The permutation column therefore carries no information at the witness independent
  of the readability predicate — the paper's "read twice" is, at the witness, one
  reading plus a readability bit.
- **No silent drop occurs.** `born_shadow_key` is total (entrywise squares of a sparse
  matrix), the comparison `a[l]["born"] != b[l]["born"]` never filters, and it is
  `born_diff` — not the permutation part — that feeds `curv` and the witness. Loops
  whose permutation part is undefined are *counted*, not dropped.
- **D7's comparator is gated with its own falsifier.** `bornhol-lax` replaces
  `born_shadow_key` with the raw matrix (line 544–546) — a quantity the switching
  moves — and dies at `PSI-SWITCHING-SELFTEST`. The Born shadow is measured invariant
  at all 66,560 switchings, 0 deviations.

The paper discloses the collapse honestly at §5.3, §10.4, §10.5 and D7. I record it as
a scope observation, not a defect. The one thing I would ask for: `readability_flips`
is recorded and never gated, and since it equals the headline 206 exactly, gating
their equality would be free and informative.

---

### F8 — LOW. `[SAMP]` does not reach either artifact, and §2.3's quantifier claim is contradicted by §6.1's own theorem.

`[SAMP]` occurs **twice** in the paper (§2.3, §10.3) and **zero** times in
`psi_curvature_output.txt` or `psi_curvature_receipt.json`. The programme rule
(failure catalogue, #40 F1/F2) requires the tag *at the claim*, and it is there, so
this is compliant in the direction the rule cares about; but a reader of the receipt
alone sees `family_size 11` with no sampling caveat. The eleven members' sizes are
genuinely computed, never typed (`family_size = len(PSI_FAMILY)`, `distinct` measured,
ranks measured), and `PSI-FAMILY-DECLARED` gates the pin's composition requirements
(`len(inv) >= 4`, `len(non) >= 3`, `len(ranks_inv) >= 3`) — the [SAMP] discipline is
substantively honest.

One wording defect: §2.3 states "Every quantifier in this paper that ranges over
preparations ranges over these eleven and over the 48 members … **and nowhere else**."
§6.1's own theorem quantifies over all ψ ≠ e_{(0,0)}. That quantifier is licensed by
*proof*, not by the family — I verified the algebra independently and it is correct
(E = I ⟺ ΣH = HΣ ⟺ Σw = ±w ⟺ Σψ = ψ, with Σw = −w forcing ψ = e_{(0,0)}). The honest
wording is "every **measured** quantifier".

---

### F9 — LOW / observation. `PSI-LAW`'s "two independent routes".

The 9×9 law and the direct 81×81 four-factor product are related by the identity under
test, which #234 calls "one route" in the census context. I do not score this as a
#234 violation: it is a theorem check rather than a census, and the two paths differ in
dimension, in operator decomposition (H and Q separately vs. V = HQ composed) and in
inversion path (transpose-free at 9×9 vs. `minv` at 81×81). Two computation mutants,
`psilaw-drop` and `defect-order`, both die there, so the pair is genuinely falsifiable.
The phrase "two independent routes to the same object" (§6.1, §11) nevertheless
overstates what a pair related by the tested identity can buy.

---

## 2. What survived the attack

These I tried hard to break and could not.

**The sweep's refusal mechanism is real, non-vacuous, and the best-built part of the
instrument (K5(c)).** I reproduced both headline numbers by my own arithmetic:
65,544 = 8 probe-instances × 8192 switchings + 8 base calls; 66,560 = 8 × (8192 + 128
checkpoint switchings). The read path is *proved to exist* rather than asserted: the
priming re-read passes a builder that throws
(`_memo(key, lambda: (_ for _ in ()).throw(RuntimeError(...)))`), so a cache that
failed to serve would crash the run, and `reread == primed and primed > 0` is in the
predicate (8/8 measured). Then 65,544 fresh-mode requests for keys that **are** in the
populated cache return `value_cache_hits = 0` against 65,544 measured misses, all
gated. The memo key `(member, setting, probe)` deliberately excludes the switching,
which is exactly what makes `memo-lax` lethal — a cache read would return the
unswitched matrix for all 8192 switchings. This satisfies the §14 addendum (#219)
"zero hits of zero lookups is vacuous" in full.

**Corrupt-and-fire on the hash pin: passes (K5(d)).** Appending one byte to
`gen_generality_receipt.json` in scratch → **exit 1**, `[FAIL] PSI-GEN-PIN`,
`[FAIL] PSI-POSITIVE-CONTROL`, 3 must-pass failures, with `A-GEN-SHA` reporting
`declared=e0b2f444… computed=90698241…`. The pin is load-bearing. Note this is also a
**prose reconstruction of the declared `gen-hash` mutant at a different injection
site**: the unit perturbs the bytes in memory after reading them, I perturbed the file
on disk. Both fire identically, which is the right answer.

**All 37 external anchors trace to the GEN receipt (K5(d)).** Composition: 3 pin
anchors (sha256 / schema / generator hash), 30 per-setting anchors (5 kinds × 6
settings), plus `A-GEN-VALSET`, `A-GEN-FIXPTS`, `A-GEN-ADMISSION` (48 cells),
`A-GEN-DEFECT`. I re-read all 30 per-setting values **straight from the GEN file at the
documented JSON paths** — 0 mismatches — and independently summed GEN's own path-space
table to 34,024 reduced paths, 5,864 closed paths, 760 based loops, links 9,9,9,9,13,13,
group orders 1,1,1,1,4,4, reproducing the paper's §4 first row and §7.1 table. Anchor
totals reconcile exactly: 27 rotations + 1 Q + 81 V + 37 external = **146**.

**`never_falsified` is EMPTY at an honest denominator of 20 (K5(e)).** Both
denominators are printed (20 falsified by some mutant, 17 by a computation mutant),
the 3 waiver-only gates are named rather than averaged away, and the single excluded
gate (`PSI-FALSIFICATION`) is named with its reason. Every gate but the census gate
names at least one declared falsifier in its own claim text — I checked all 21.

**`PSI-NO-MUTANT-EXEMPTION` is honest, verified by my own AST sweep.** I independently
walked the source: **37** gate/anchor call sites (22 `gate` + 15 `anchor` — 22 because
`order-lax` emits an extra `gate(...)` at line 3094), **0** call sites whose argument
expressions reach `MUTANT` at any depth, **0** `MUTANT != …`, **1** `MUTANT not in …`
at line 3076 (argparse validation, outside every call site, correctly disclosed),
**0** float literals. Every number matches the instrument's own report. §14 addendum
(#208) is satisfied.

**Determinism is structurally sound.** `time.time()` appears at exactly two lines: `T0`
and inside `prog()`, which writes to stderr only. No wall-clock value can reach
`build_receipt()` or `render()`; the receipt carries no timestamp field. I did not
re-run delivery mode (it would write into the repo), so the byte-identity claim itself
is unverified by me, but the mechanism that would defeat it is absent.

**The disclosed instrument-hygiene item (§11, artifacts written before the exit code is
computed) is accurate** — `main()` writes `OUT_TXT`/`OUT_JSON` at 3182–84 before `fail`
is read at 3187. Disclosed rather than hidden; I confirm the disclosure is exact.

---

## 3. K1, K2, K4 at the assigned depth — independent recomputation

I rebuilt the algebraic layer from the **paper's declarations only** (quaternion-free:
Σ, Q, the eleven coefficient vectors, the Householder), importing nothing from the
instrument, in exact `Fraction` arithmetic.

**K1 — the witness (independently recomputed).** With Σ the system-pair exchange and
V = H(ψ)Q, the length-4 loop `(id@0,FULL)⁻¹ → (leg,F2,1) → (id@1,REAL) → (leg,F1,1)⁻¹`
has system factor V⁻¹ΣV and the realized bigon has system factor V⁻¹ΣVΣ. Measured by
me:

| member | short loop a signed permutation? | doubled realized bigon = I? | Born shadows differ from ψ_G? |
|---|---|---|---|
| ψ-G | **yes** | **yes** (flat) | — |
| ψ-N1 | **no** | **no** | **yes**, both loops |
| ψ-S1 | yes | yes | no, both loops |
| ψ-N2 | no | **yes** | short yes, doubled **no** |

This reproduces every clause the paper asserts about the witness pair, including the
sharp one: **a loop flat at ψ_G and not flat at ψ_N1**, with all declarations
identical. It also reproduces the receipt's otherwise-unremarked ψ-N2 row
(`common_loops_flat_at_the_reference_and_not_here = 0`) — ψ-N2 moves the short loop but
leaves the doubled bigon flat, which is a non-trivial cross-check of the enumeration.

The scoping demanded by K1 is present and correct in the paper (§10.5, D7): the
witness's holonomy at ψ-N1 is *not a signed permutation*, so the difference is
registered in the Born shadow and the readability predicate — both switching-invariant
— and the paper says so at the claim and not only in the receipt. I did **not** find a
scoping overreach here.

**K2 — the law (independently recomputed at all 11 members, not 3).**
- `E(ψ) = ΣH(ψ)ΣH(ψ) = I` **⟺** ψ exchange-invariant: agreement at **11/11**, both
  directions.
- `D(ψ) = ΣVᵀΣV` equals `D_GEN·QᵀE(ψ)Q` **entry by entry at 11/11**.
- `D = D_GEN` at exactly the 7 invariant members; `D` is a signed permutation at
  exactly those 7. Both lists coincide with the paper's.
- Every V measured exactly orthogonal over ℚ with ψ as column 0 at 11/11.

**The 48-member sign-flip census, recomputed by my own enumeration.** Per member
{ψ-G 8, ψ-I1 8, ψ-I2 2, ψ-I3 4, ψ-I4 16, ψ-S1 8, ψ-S2 2} = **48**; **26** move, **22**
do not, **0** agreement-vs-invariance mismatches. Exactly the paper's §6.2 table. (My
first pass read "fixes the initial coefficient" as "the first non-zero of the support"
and got 32; D4 disambiguates it correctly as ε_{(0,0)} = +1, i.e. the index-0
coefficient, and the instrument implements D4. The §6.2 phrasing is loose but D4 fixes
it — no finding.)

**The negative control's predictor, recomputed.** δ(pinned Q) = [0,2,1,6,4,5,3,7,8],
order 2 → predicts 4; δ(Q-negA) = [0,3,2,4,1,5,6,7,8], order 3 → predicts 6;
δ(Q-negB) = identity, order 1. All three match the receipt. Note that my δ(pinned Q)
also equals GEN's own recorded `the_defect_permutation` — the unused external anchor of
F4.

**K4 — the second phenomenon (verified).** The 8 moving cells at ψ-N3 and ψ-N4 are
exactly `{GP-E, GP-F} × {t0,t1,t2,t3} × REAL` — the realized rule at all four
checkpoints at the two symmetric settings, precisely as §5.1 states. `psi-N1` and
`psi-S1` move **0 of 48**. On D10's two-phenomena-one-verdict split I agree with the
unit: the pre-registered outcomes are exclusive by their own wording
(`PSI-PATH-SPACE-DEPENDENCE` requires every common loop's holonomy to be ψ-invariant,
which this family refutes), so reporting the second phenomenon *beside* the verdict
with its own gate and its own printed cell list is the honest reading. Nothing is
folded. My only reservation is F2(a): the cell list it prints is ungated.

---

## 4. Reconstructed mutants (K5(e): ≥3 from prose)

I audited all 34 declared mutants by reading **every injection site** in the source
against its declared prose and its recorded kill set, and I reconstructed mutants from
their **prose descriptions alone** at injection sites different from the instrument's
own. Completed reconstructions:

**RC1 — `gen-hash`, reconstructed on disk.** Prose: "the external receipt's bytes
perturbed before they are hashed." The unit injects this in memory
(`raw = raw + b"\n"` at line 1390). I instead corrupted the **file on disk** by one
byte and left the source alone. Result: **exit 1**, `A-GEN-SHA` reporting
`declared=e0b2f444… computed=90698241…`, `[FAIL] PSI-GEN-PIN`,
`[FAIL] PSI-POSITIVE-CONTROL`. Fires identically to the declared mutant. **PASS.**

**RC2 — `signflip-lax`, reconstructed at reduced strength — and it does NOT fire.**
Prose: "the sign-flip census subsampled." The declared mutant subsamples to *one*
pattern per member (`pats[:1]`), which drops `total` to 7 and dies only because the
predicate carries `total > 2*len(inv_members)` = 14. I reconstructed the same prose at
half strength (`pats[:max(2, len(pats)//2)]`), giving `total = 26 > 14`. Result:
**exit 0, all 20 gates pass**, receipt printing `sub_family_size: 26` under a gate that
still claims the census is EXHAUSTIVE. **This is the reconstruction that mattered**: it
shows the declared mutant dies against a threshold, not against a completeness check,
and it is the direct evidence for F2(b).

**RC3 — a novel dropped-cell mutant on the admission table** (no declared counterpart).
Removing `GP-E/t1/REAL` from the table construction for all members → **exit 1**, one
external anchor failing (36/37), `[FAIL] PSI-POSITIVE-CONTROL`. Confirms
`A-GEN-ADMISSION` is the unit's only cell-completeness route and localises its reach.

**RC4 — a novel dropped-cell mutant on the admission *comparison*** — the same cell
removed from the delta loop instead → **exit 0, all 20 gates pass**, printed delta
`8 → 7`. Evidence for F2(a).

**RC5 — the verdict-flip mutant #234 requires by name** — F1. **exit 0.**

Three further reconstructions were dispatched (`defect-order` at a different wrong
composition order; `psilaw-drop` injected at the construction of `E` rather than at
`pred9`; and a length-restricted born-difference set to test whether the printed 206 is
gated). They were still executing when this review was frozen, queued behind a
concurrent reviewer's own 34-mutant sweep on the same host. **I do not rest any finding
on them**, and none of them can weaken F1–F9: two are confirmatory of gates that the
frozen table already records as killed by computation mutants (`PSI-LAW`), and the third
would at most add a fourth instance to F5, which is already argued from the source.

**The declared table, audited.** All 34 mutants are recorded exit 1 with a named kill
and `crashed_before_reporting: []` — none dies by crashing, which is the right
discipline. `never_falsified` is `[]` against a denominator of 20. The kill sets are
plausible against the injection sites I read: every `MUTANT ==` comparison in the source
(35 of them, all in computation bodies, none in a gate argument — verified by my own AST
walk) corresponds to a declared mutant. The waiver analysis is F3.

---

## 5. Recomputation count

**190 independent recomputations** completed, plus the mutant work in §4. Per-member
checks are counted per member; nothing here is a re-reading of the unit's own output.

| group | n | what |
|---|---|---|
| artifact integrity | 6 | 4 frozen sha256 + the GEN receipt's sha256 against the typed anchor + a full baseline run |
| the declared family | 56 | norm², Schmidt rank, support, exchange-invariance, Born-shadow symmetry at 11 members, + the six computed sizes |
| the ψ-law (K2) | 46 | E(ψ)=I ⟺ invariance, D(ψ)=D_GEN·QᵀE(ψ)Q entry-by-entry, V orthogonality, V column 0 = ψ — each at 11 members; + the two coincidence lists |
| the witnesses (K1) | 15 | both witness loops at 4 members, the flat→non-flat pair, and the five Born-indistinguishability clauses |
| the sign-flip census (K2) | 5 | total 48, per-member breakdown, 26 moved, 22 unmoved, 0 mismatches |
| the negative control | 4 | δ(Q) and its order at three transpositions + the match to GEN's recorded defect permutation |
| external anchors (K5d) | 40 | 30 per-setting values re-read from the GEN file, schema, generator hash, 48-cell admission, anchor totals, GEN's four path-space totals, links, group orders, V vs the typed matrix |
| instrument arithmetic (K5c) | 3 | 65,544 and 66,560 derived from first principles + the cache ledger |
| AST and hygiene (K5e) | 6 | call sites, MUTANT reachability, exemption forms, float literals, determinism, per-gate falsifier naming |
| falsification probes (K5a,b,d) | 5 | verdict-flip, census-half, delta-cell-drop, admission-cell-drop, receipt corruption |
| K4 and the split | 4 | the three admission deltas + the bookkeeping-split witness list |

---

## 6. Grade

**ACCEPT-WITH-FIXES.**

I want to be exact about why this is not REJECT and not ACCEPT.

**Why not REJECT.** I attacked the substance hard and it held. Rebuilding the algebraic
layer from the paper's declarations alone, in exact rationals, importing nothing from
the instrument, I reproduced: the whole eleven-member family table; the ψ-law
`D(ψ) = D_GEN·QᵀE(ψ)Q` entry by entry at **11/11** members; the characterisation
`E(ψ) = I ⟺ ψ exchange-invariant` in **both** directions at 11/11; the 48-member
sign-flip census at **48 / 26 / 22 / 0**; the negative control's predictor at all three
transpositions; and both witnesses — including the sharp one, a loop **flat at ψ_G and
not flat at ψ_N1** with every declaration identical. I re-read all 37 external anchors
against the committed GEN receipt and found 0 mismatches, and corrupting that receipt
by one byte kills the run. I found **no false number and no false theorem**; I checked
the §6.1 proof sketch's algebra myself and it is correct. As far as I can determine the
verdict `PSI-CURVATURE-EXISTS-AT-FIXED-BORN-SHADOW` is **true**. It is simply not
gated.

**Why not ACCEPT.** The protocol made #234 compliance mandatory for this unit and asked
me to decide it. I decided it by probe, and the answer is **NONCOMPLIANT**: swapping
two branch strings makes the artifact print the negation of its own finding, with all
20 gates passing and exit 0, and with the falsifying measurement sitting in the same
evidence line as the false verdict. Both clauses of the addendum fail — the ungated
verdict (F1) and cell-completeness on both censuses (F2) — and the paper and the gate's
own claim text assert, in terms, that the verdict *is* re-derived inside the gate, which
it is not. That is a repairable instrument defect, not a scientific error, but it is
exactly the defect the addendum names, in a unit delivered after it.

**Blocking, must be repaired and the falsification census re-run before terminal:**

- **F1** — gate the verdict against the string the rule selects from the recorded
  tables; declare a **computation**-kind `verdict-flip` mutant and require it to die
  there; correct §9 and the gate claim text. (~6 lines.)
- **F2** — add cell-completeness gates to both censuses (`cells == 6·4·2`; each member's
  delta loop over the reference table's full key set; `total == Σ 2^{|support\{0}|}`)
  and a dropped-cell mutant for each.

**Required corrections, no re-run needed:**

- **F3** — withdraw the §11 claim that a verdict gate "can only be violated by emitting
  a bad string"; it is false and it is what concealed F1.
- **F4** — correct §2.2: the 81 V-anchors are self-anchors against a matrix typed in
  this file, GEN's receipt does not carry V, and "*is* GEN's completion and not a
  rebuild of it" does not follow. Recommended in the same pass: anchor GEN's recorded
  `the_defect_permutation` entry-by-entry, which would make the claim true.

**Recommended:**

- **F5** — gate the printed comparison counts; rebuild the flat→non-flat witness by the
  independent route, as the born witness already is.
- **F6** — anchor or downgrade the `n == 1 → 1` branch in the negative control; put the
  link refusal into the predicate.
- **F7/F8/F9** — gate `readability_flips` against the born-difference count (free);
  carry `[SAMP]` into the receipt; correct §2.3's "and nowhere else" to "every
  **measured** quantifier"; soften "two independent routes" at §6.1/§11.

**On the parts I could not break, for the record.** The sweep's refusal mechanism is
the best-engineered thing in this unit — the read path is *proved* to exist by an
exception-throwing builder rather than asserted, the memo key deliberately excludes the
switching so that `memo-lax` is genuinely lethal, and 65,544 refusals against 8 primed
entries is a real measurement, not a vacuity. `PSI-NO-MUTANT-EXEMPTION` reproduced
exactly under my own AST sweep. The bookkeeping split is gated in **both** directions
and its witness list is correct. `never_falsified` is genuinely EMPTY at an honest
denominator of 20, with both denominators printed and the waiver-only gates named
rather than averaged away. Two of the three waivers are legitimate. The unit's
disclosures — D1–D10 and the §11 hygiene item — are accurate wherever I checked them,
which is most places.

The instrument is strong and the finding is real. It is let down at exactly one joint:
the place where the measurement becomes a sentence.

— **R3, instrument lens.**
