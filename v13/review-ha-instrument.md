# HA — HOSTILE REVIEW R3 (INSTRUMENT LENS)

**Status:** FROZEN review, 2026-08-08.  **Protocol:** `v13/note-ha-hostile-protocol.md`
(frozen before dispatch, v13 #240); primary weight **K5**, with K1/K2/K4 at lower depth.
**Object reviewed (SHA-256 verified at the start of the review and again at the end,
unchanged both times):**

| artifact | sha256-12 | verified |
|---|---|---|
| `v13/paper-ha-successor.md` | `4e7589da58fe` | yes |
| `v13/code/ha_successor_exact.py` | `19dad19b01ee` | yes |
| `v13/code/ha_successor_output.txt` | `fda287ee86c3` | yes |
| `v13/code/ha_successor_receipt.json` | `7d74bea76760` | yes |

**Method.** No repo file was modified. All probes ran in
`scratchpad/ha/`, against a symlink mirror of the repository whose only real
directory is a scratch `v13/code/` (so that anchors A01–A08 still resolve against the
true trees while every probe writes outside the repo). All physics numbers were
recomputed by a **from-scratch reimplementation written from the paper's prose**
(`scratchpad/ha/indep.py`), which imports nothing from the audited instrument, uses a
different linear-algebra route (cofactor expansion rather than Gauss–Jordan), and
carries **no memoization at all**. Independent recomputation count is stated in §9.

---

## 1. Reproduction

- `ha_successor_exact.py --falsification-selftest`, run in place (writes nothing),
  reproduces `ha_successor_output.txt` **byte-identically, all 408 lines**, including
  the full 25-row mutant harness. Exit 0.
- The mirror run differs at **exactly one line** — the X01 live-tree count
  (`v13/code carries 1` vs `37`), an artifact of the mirror, not of the instrument.
- The four frozen artifacts' SHAs are unchanged after every probe.

---

## 2. K5(a) — the anchor set

**All 16 anchors reproduce, independently.**

- **A01–A04** recomputed by shell (`ls`/`grep -lw`) and again by a second tokenizer:
  353, 273, 137, 101, 84, 9, 8, 7, 3, 1; root `.py` = 3; `lapse` in **12** of `code/`'s
  files; **0** in each of the nine other frozen trees. These match
  `note-gw1-metric-from-closure.md` §4's census list verbatim.
- **A05/A06** hash pins recomputed by `shasum`.
- **A07/A08** recomputed from the pinned NT receipt (34 024; orders (1,1,1,1,4,4)).
- **A09–A16** rebuilt **from scratch**: my own Σ (pair-label exchange on
  `a = 3s_A + s_B`), my own defect `D = ΣQ⁻¹ΣQ`, my own 8! enumeration. Every value
  reproduces — 40 320 / 96 / 40 224 / `[0,2,1,6,4,5,3,7,8]` / 45 / the full order
  spectrum `{1:96, 2:1440, 3:4224, 4:4608, 5:4608, 6:6912, 7:9216, 15:9216}` / the full
  fixed-configuration spectrum / 0 dihedral failures. I then cross-checked all eight
  against **both** `paper-gen-generality-check.md` §8.1–8.3 **and**
  `gen_generality_receipt.json` `tables.completion_census`. This is a genuine
  rebuild-from-prose, not a read of the receipt, and it is the strongest part of the
  anchor set.

**Pins tested by scratch corruption — both fire.** Rewriting the NT receipt with
different whitespace (identical JSON, different bytes) gives
`ANCHOR FAILURE A05`, **exit 1**; the same for GEN gives `ANCHOR FAILURE A06`,
**exit 1**. Exit-1-only behaviour confirmed by deliberate breakage.

Reservation (F9, low): six anchor mutants cover A01, A03, A05, A07, A09, A12; ten
anchors (A02, A04, A06, A08, A10, A11, A13–A16) carry no declared falsifier. Mitigated
by the two hand corruptions above and by the fact that all sixteen reproduce.

---

## 3. K5(b) — the mutant table

- 25 mutants declared, 25 spawned, **0 survivors**, every one exits 1 with a named kill.
- `never_falsified` is **EMPTY with an honest denominator**: I recomputed the
  denominator from the receipt — the 21 must-pass gate ids are
  G01–G09, G08B, G10, G10B, G11–G15, G21–G24, and the union of the mutants' named
  kills covers **all 21** (22 gate ids in total, including the recorded G19). No
  must-pass gate is unfalsified.
- Every mutation is a mutation of an instrument helper; I confirmed by AST that no
  gate-registering function names `MUTANT`, `MUTANTS`, a `_M_*` switch, or a
  mutant-name literal.

**Five mutants reconstructed from the paper's prose**, in my own implementation
(the protocol asks for ≥3). Every one reproduces the paper's named kills exactly:

| reconstructed | paper's named kills | my reconstruction kills |
|---|---|---|
| `sign-flip` | G05 | G05 |
| `omega-asym` | G05, G13 | G05, G13 |
| `transport-off` | G05 (also G04, G19 in-instrument) | G05 |
| `readout-local` | G07, G09, G12, G21 | G07, G09, G12, G21 |
| `beta-flat` | G06, G12, G21 (also G08) | G06, G12, G21 |

The gates are the **right** gates: `readout-local` kills G09 because a link-local
surrogate destroys the counterexample G09 exhibits, and kills G07 because a diagonal
`I` makes the cross-term-flip control `A-insert-x` indistinguishable from `A-insert`.
These are mechanism-appropriate deaths, not collateral.

One reservation (F11, low): G03's only falsifier, `rank-lax`, replaces the whole lapse
family with constant profiles, driving ω ≡ 0 and collaterally killing G07/G08/G08B/
G10/G12. Per RUNBOOK §14 a wholesale-replacement mutant does not establish that the
*right* invariant is computed.

---

## 4. K5(c) — the chart self-test and the cache

**The numbers are right.** My memoization-free reimplementation reproduces the chart
self-test at **4 860 comparisons / 0 violations** exactly. The cache counters
(283 133 hits / 1 377 misses / 486 fresh bypasses) reproduce byte-identically. The
cache **is** exercised, so the §14/#219 "zero hits of zero lookups is vacuous" trap is
avoided.

**One violation reconstructed.** Applying the chart map to the record but not to the
field index (the `chart-shift` mechanism, rebuilt in my own code) yields **102
violations of 4 860**, with an explicit witness at `G-CURVOFF`, σ = (1,0), shift (0,0),
site (0,0): LHS `(-1/6, 1/3)` against RHS `(1/3, -1/6)`. G14 therefore detects the
failure mode it names.

**But the compliance claim is wrong as coded (F4).** §7.4 states "the self-test
evaluates fresh". It does not. The 486 fresh evaluations
(`lambda_of("A-axis", r, x, fresh=True)`) are computed on the **original** record and
their return values are **discarded**; the self-test's own comparands `f1` and `f2` are
both produced by `residual_field_closed`, which reaches `lambda_of` with `fresh=False`
— i.e. through the memo. Two probes settle it:

- **Probe D** — delete the fresh-evaluation loop entirely: G14 still reports
  **4 860 / 0 PASS**; only G15 flips (bypasses 0 → FAIL). The 486 bypasses are a
  counter that feeds nothing.
- **Probe C** — alias the memo so the chart-transformed record is served the original
  record's cached weight (the canonical bug #185 exists to catch): **G14 FAILS**
  (148 violations) while **G15 still PASSES** (hits 283 619, misses 891, bypasses 486).

So the hazard is not realised — G14 has real teeth and the value is memo-independent —
but G15 cannot distinguish a correct cache from an aliased one, and the sentence
"the self-test evaluates fresh" describes something the code does not do.

**Repair.** Evaluate `f1`/`f2` with `_LAMBDA_CACHE` cleared (or thread `fresh=True`
through `residual_field_closed`) so the self-test's own quantity is cache-free; reword
§7.4 to "the cache path is separately exercised and gated" rather than "the self-test
evaluates fresh".

---

## 5. K5(d) — §13-addendum verdict-gate compliance: **THE PRINCIPAL FINDING**

### F1 (MODERATE — repair required). The printed verdict is not derived inside a gate, and no verdict-flip mutant exists.

At lines 2118–2122 the verdict is assembled from measured booleans and then simply
printed. No gate compares the printed string to the measurement, and `verdict-flip` is
absent from the 25 declared mutants.

**Probe A (deliberate breakage).** Replacing the two derivation lines with a
hand-typed literal `verdict = ["HA-RUNNABLE", "HA-BRIDGE-POSABLE"]` produces a run in
which:

```
        BRIDGE VERDICT: NOT POSABLE   (G22 PASS)
  ...
  must-pass gates 21;  failures 0 []
  HA-RUNNABLE + HA-BRIDGE-POSABLE
```

— all **21 must-pass gates PASS**, **exit 0**, and the same output file asserts
"NOT POSABLE" at §12 and "BRIDGE-POSABLE" at §15. The receipt would carry
`"verdict": [... "HA-BRIDGE-POSABLE"]` alongside `tables.bridge.posable = false`.
This is exactly the "an ungated verdict is a typo away from fiction" failure the
addendum names.

**On the protocol's parenthetical "built before the addendum":** the ledger does not
support it. The §13 addendum originates at **v13 #234**; HA was delivered at **#236**;
and #235 dispatched the sibling COC re-derivation with an explicit order for
"verdict-inside-a-gate w/ the verdict-flip mutant; genuinely independent census routes
+ cell-completeness gate". HA carries none of the three. The pin predates #234, so
this is a timing casualty rather than a disregarded order — but it is a repair, not a
waiver.

**Does it move the verdict?** No. I re-derived every input to `ha_runnable`
(g04, g05, g10, g10b, g11, `len(failed)==0`) and to `posable` (carrier_match,
in_spectrum, ha_dih) and each is independently confirmed. **The delivered verdict
`HA-RUNNABLE + HA-BRIDGE-NOT-POSABLE` is correct.** What is missing is the gate that
would make it *provably* correct.

**Repair.** Add G25: derive the verdict string inside a gate from the measured counts
and compare it to the printed string; add a `verdict-flip` mutant that perturbs the
derivation and must die at G25.

### F2 (MODERATE). No cell-completeness gate on the census.

The addendum's second clause — "a cell-completeness gate must catch a dropped cell" —
is unmet. **Probe E:** deleting `A-linkhalf` from `DECL["rules"]` silently shrinks the
closure table from 99 cells to 90 and the sector-law grid from 72 to 63, with **all 21
must-pass gates PASS and exit 0**. The instrument already knows the pattern — G07
carries `len(brk) == len(DECL["broken_rules"])` — it is simply not applied to the main
census.

**Repair.** Gate `len(results) == len(DECL["rules"]) × len(ADM)` and
`len(sector) == |arch-A rules| × len(ADM)`, and gate the d=3 grid likewise.

### F8 (LOW). "Two independent routes", stated precisely.

G05's two routes are genuinely independent in the operative sense — the literal
five-map composition and the closed form share no code, and `sign-flip`, `order-swap`,
`omega-asym` and `transport-off` each move one side only (three of these I rebuilt
from prose and each killed G05). I also derived the closed form by hand and confirm it
is the exact register displacement of the composition, so the check is sound.
**But both routes call the same `beta()`**, so a common-mode β error is invisible to
G05 — confirmed twice: `beta-flat` is not among G05's killers in the frozen harness,
and in my reconstruction `beta-flat` left G05 passing. β is in fact policed by
G06/G08/G12/G21, so nothing is unguarded; the addendum's honesty clause simply argues
for saying which route checks what.

---

## 6. K5(e), K5(f), K5(g)

**(e) The density-weight sweep — verified, exactly.** My independent sweep reproduces
the §7.5 table cell for cell: at w=1, `G-DIAG2` 0→96, `G-ANISO` 0→96, `G-ANISO2` 0→96,
`G-CURVED` 0→92, `G-FLAT` 0→0, and the four cross-term records unchanged at 96.
**Exactly 4 cells move**, and they are the four named. The convention-relativity is
reported as the declared convention's cost, not buried — this is well handled.

**(f) Negative controls, float sweep, injection controls — all verified.**

- G02 is genuinely **two-sided**: it rejects both degenerate readouts (`G-SINGULAR`,
  det q = 0; `G-INDEF`, det q = −3) **and** requires all nine others to be accepted.
  `posdef-lax` correctly dies on the indefinite one only (the singular one is caught by
  the inverse's non-existence regardless) — and the paper says exactly that.
- The three broken variants all fail closure, on 4 / 9 / 9 records respectively; the
  "4" for `A-insert-x` is correct and correctly explained (flipping the sign of a zero
  cross term is a no-op).
- Independent AST sweep of the source: **zero** float/complex literals, **zero**
  `float()`/`complex()`/`round()` calls, no `math`/`numpy`/`decimal` import. The
  injection control is real (the decoy `0.5 + float(1)` produces the 2 hits G24
  requires), and I re-ran the AST-guard injection myself — the `MUTANT`-reading decoy
  is flagged.

**(g) Deviations 4–11 — spot-audited.**

- **Deviation 11 / A01 exclusion-with-counts: correct and honest.** GW1 §4's census
  lists twelve rows; `FROZEN_TREES` takes ten of them, A02 takes `<repository root>`,
  and `v12/code` (census 5) is excluded **by declaration with its current count
  printed** (now 7), together with `v13/code` (now 37, not in the census at all). The
  exclusion is by declaration, not by outcome, exactly as X01 says. I verified all
  counts independently.
- **Deviation 3 / the direction-labelled adjacency's measured equivariance — F7 (low).**
  The mitigation is real but the scope tag overstates. `DECL["chart_group"]` declares
  9 translations × 2 relabellings = **18** elements; the loop runs `shifts[:3]`, i.e.
  **6 of 18** group elements and 10 of 132 lapse pairs, while G14's claim string says
  "every declared chart translation and direction relabelling". The receipt is honest
  (`"translations": 3`); the claim string and §7.4 are not. **I checked the claim
  anyway and it holds:** the full 18-element group over all 132 lapse pairs gives
  **192 456 comparisons, 0 violations**. (It is also true by group generation — σ
  conjugates the tested translation (0,1) to the untested (1,0) — but the unit does not
  make that argument.) Repair: run the full group, or state the tested subset in the
  claim.
- **Deviation 4** (address-register tangential sector, R_DD/R_DH out of scope) is
  honest: §13 explicitly declines `V4P7-FIN-ALG-CLOSE` and states the abelian
  tangential class as a declared choice with its consequences measured (G19, G18).
  Deviations 7 (frozen geometry sector), 8 (reduced operator carrier, 33 undefined
  reductions printed), 9 (G16/G19 recorded not must-pass — confirmed in the receipt)
  and 10 (G08 excludes the frozen-front variant by declaration, measured separately at
  G08B) are all as described. **Deviation 10 in particular is a strength**: the
  excluded row is still printed (9/0 everywhere) rather than hidden.

### F6 (MINOR). G06 is an analytically-forced must-pass gate.

G06 reads `results`, which is the **closed form** only, where `Λ = rec.I ⟹
ρ = (Λ − I)ω ≡ 0` — the same identity X02 discloses for G08. Per §14 (#208),
analytically-forced clauses are disclosures, not must-pass gates. It is falsifiable
only by mutating β's *definition* (`beta-flat`), not by any input. The literal
five-map cancellation, which *would* be a genuine measurement, is measured — but by
G05, not by G06. **Repair:** extend X02 to name G06 (and G12/G21's `A-insert` clause),
or re-base G06 on `residual_field_literal`.

### F5 (MINOR). The AST guard does not cover its own disclosed exception.

I injected four decoy gate-registering functions and ran the instrument's own
`ast_mutant_scan` on each:

| decoy gate predicate reads | flagged? |
|---|---|
| `MUTANT` | **yes** |
| `DELIVERY_RUN` | **no** |
| `SELFTEST_ONLY` | **no** |
| `sys.argv` | **no** |

`DELIVERY_RUN = (MUTANT is None)` is mutant identity under another name, and X03's
claim that "no gate predicate reads it" is therefore **asserted, not measured**.
I verified by exhaustive grep that the claim is **true** in the delivered source — the
only reads are at lines 2141 and 2197, both outside every gate — so nothing is
currently exploited. Separately, line 1055's
`switches = {n for n in dir() if n.startswith("_M_")}` is dead **and vacuous**
(`dir()` inside a function returns locals, so it is the empty set) and is never read:
a line that looks like it enforces something and does not, inside the very guard the
addendum demands. **Repair:** add `DELIVERY_RUN`/`SELFTEST_ONLY`/`WRITE_ARTIFACTS`/
`sys.argv` to the offender predicate, add those three decoys to G23's injection
control, and delete or fix line 1055.

### F10 (LOW, process). X01 reads live trees.

The delivered `output.txt` embeds counts of `v12/code` (7) and `v13/code` (37), which
four concurrent cycles are writing to. It reproduces today — my in-place re-run is
byte-identical — but the delivery artifact is not stably reproducible by construction.
**Repair:** print the live counts to the receipt only, or pin them as declared data
with the census date.

---

## 7. K1 / K2 / K4 at the protocol's lower depth

**K1 — the construction.** Verified analytically and numerically.
`H_a[N](n,m) = (n+N, m+w[N,n])` is a skew product over the front, so the front is
recovered first and the drag is then determined: the closed-form inverse
`(n−N, m−w[N,n−N])` is exact, not declared. I re-derived the residual by hand:

> register displacement of `H[N]H[M]H[N]⁻¹H[M]⁻¹D[−β]`
> `= Λ^{ij}(N∂_jM − M∂_jN) − β^i = (Λ − I)^{ij} ω_j`,

and the front returns to `n₀` identically — which my independent literal composition
confirms at every one of the 1 188 comparison cells. The transported second step is
**load-bearing, not cosmetic**: the two surviving terms exist only because the M-step's
drag is read at the advanced front `n+N`; freezing the front cancels all four drag
terms and leaves `ρ = −β`, which is exactly the measured `A-notransport` row (Λ = I at
9/9 sites, residual zero at 0/9 — reproduced independently).

**No-smuggling audit.** I scanned `lambda_of` by AST: the rules that read the
record-read metric `rec.I` are **exactly** the four declared insertion/control rules
(`A-insert`, `A-notransport`, `A-insert-x`, `A-insert-2x`). All seven record-native
rules (`A-chart`, `A-axis`, `A-linkframe`, `A-linkhalf`, `B-axis`, `B-all`, `B-chart`)
read `rec.counts` only. Nothing metric-shaped enters the record-native path silently.

**K2 — the two-sided closure.** Recomputed independently, everywhere:

- The **entire** §6.1 closure table (99 cells) reproduces exactly, including
  `A-chart`'s 70/84, `B-all`'s 78/114, and the `A-axis` row.
- **Diagonal closure at one record:** `G-CURVED`, the *inhomogeneous* diagonal record —
  `A-axis` CLOSES at all 132 ordered pairs and 9/9 sites. So does `G-DIAG2`,
  `G-ANISO`, `G-ANISO2`, `G-FLAT`.
- **Cross-term anomaly at one record:** `G-OFFDIAG` — 96 of 132 pairs nonzero,
  `Λ − I = (−1/6, 1/3, −1/6)` at (0,0), `max|ρ| = 2`. The whole gap table reproduces,
  including `40/33` and `20/33`.
- **CLOSURE-IS-INSERTION:** 63 transported-rule cells, **0 mismatches**, including the
  delicate `A-chart | G-CURVED` cell at **1/1** (the single site where the counts are
  unity). X02's forcing disclosure is correct and correctly scoped.
- **G09** — the witness reproduces: `G-CURVOFF` and `G-DIAG2` share `n_{e₁}(0,0) = 2`
  while the readout demands `I¹¹ = 2/3` and `1/2`. The stated mechanism
  (`I^{jj} = adj(q)^{jj}/det q`, `det q` a joint function) is correct.
- **G08B, G10/G10B/G11, the detector:** operator layer 1 089 attempts → 1 056 built,
  33 undefined, 0 non-bijective, 0 mismatches; G11 76/76; the `prime-single` witness
  `A-linkframe | G-OFFDIAG2` reproduces exactly — exact residual `(35/132, 7/660)`,
  **undefined mod 5**, `(0,0)` mod 7, `(11,2)` mod 13. The three-normal detector
  reproduces at 108/108 trivial commutator, 0 Jacobi violations, **81 of 108** SW_HHH
  ≠ id, 27 of 36 for each of the three rules, and both named witnesses (`max|reg| = 2`
  at `A-insert|G-ANISO|(9,10,0)`, `1/64` at `A-insert|G-ANISO2|(0,3,9)`).

**Zero numerical discrepancies were found anywhere in the unit.**

**K4 — the bridge negative.** The order-5 group recomputed from scratch on a
625-element carrier I built myself: order **5**, element orders **{1,5}**, abelian —
confirmed. `ΣRΣ = R⁻¹` is **False** at the declared loop by permutation-level
computation; GEN's own defect satisfies it (order 2, relation True). Carrier match
False, spectrum membership False. The `HA-BRIDGE-NOT-POSABLE` verdict is sound, and
the paper is correctly careful in §13 ("no nonexistence theorem about bridges is
claimed").

### F3 (MODERATE). "The dihedral relation ... holds at 17 of them" does not measure the dihedral relation.

The code does not test `ΣRΣ = R⁻¹` over the 24 further pairs. It tests the scalar
surrogate `ρ₁ + ρ₂ == 0` **over ℚ**. Three findings, all independently computed:

1. The surrogate is algebraically equivalent to the relation **where Σ exists** —
   I derived this (R is a uniform register translation by ρ, Σ swaps the register
   components, so `ΣRΣ = R⁻¹ ⟺ ρ₂ ≡ −ρ₁ mod p`) — and I confirm the surrogate gives
   **17/24** and agrees with the mod-5 statement on all 24 pairs. So the number itself
   is not wrong.
2. **But the chart involution Σ is defined on the corresponding carrier for only 4 of
   the 24 pairs.** On the other 20, "the same relation" has no referent — the carrier
   for those lapses does not admit Σ, and the instrument never builds it.
3. Counting only the cells where the relation is posable: it holds at **3 of 4**.

The paper's inference — "so it is a coordinate coincidence at this arena, not a
structural property of `R_HH`" — therefore rests on 20 cells at which the statement is
not posable. **Verdict impact: none.** `bridge_posable` requires
`carrier_match ∧ in_spectrum ∧ ha_dih`, and I confirm all three are False at the
declared loop independently of the 17/24; the figure lives in G22's *detail*, not its
predicate. **Repair:** either report "3 of the 4 pairs at which the chart involution is
defined", or build the reduced carrier per lapse pair and test the relation properly;
and stop calling the surrogate "the same relation".

---

## 8. What I could not refute

Stated deliberately, because a hostile report that lists only defects misreports the
object:

- Byte-identical reproduction of a 408-line artifact including the mutant harness.
- 16/16 anchors reproduced, eight of them by a genuine from-prose rebuild cross-checked
  against two independent sources; both hash pins fire on corruption with exit 1.
- 25 mutants, 0 survivors, `never_falsified` empty **with the denominator checked**.
- Five mutants rebuilt from prose, all reproducing their named kills.
- Every physics number in the paper — the 99-cell closure table, the 63-cell sector
  law, the gap table, the rank, the w-flip, D-TOT, d=3, the operator layer, the
  detector, the bridge group — recomputed by disjoint code and reproduced **exactly**.
- The no-smuggling audit is clean: the record-native rules never touch the metric.
- The float discipline is real, and its injection control works.
- The negative controls have teeth in both directions.
- §7.5, §6.5, §7.6 and §13 are unusually honest about what the unit does not have —
  the convention-relativity is reported as a cost, the diagonal closure is explicitly
  attributed to arithmetic coincidence rather than design, and G16/G19 are demoted to
  recorded because they are forced.

---

## 9. Recomputation count

**60 independent recomputations**, of which **6 were deliberate-breakage probes**
(NT pin corruption; GEN pin corruption; Probe A verdict fiction; Probe C cache
aliasing; Probe D fresh-path deletion; Probe E dropped census cell). The 54
non-probe recomputations comprise: 16 anchor reproductions plus 2 cross-source checks
(GEN paper, GEN receipt); the §4.1 record table; the identifiability rank; the 99-cell
closure table; the 1 188-cell literal-vs-closed comparison; the 72-cell sector law and
the 9-cell G08B row; the gap/`max|ρ|` table; the density-weight sweep; the D-TOT
census; the d=3 grid; the operator layer (1 089 attempts) and its two comparators; the
G10B blindness census; the `prime-single` witness; the chart self-test (4 860) and its
reconstructed violation (102); the full 18-element chart group over all 132 pairs
(192 456 comparisons); the three-normal detector (108 cells); the bridge carrier,
group and Σ-relation; the 17/24 surrogate audit; five from-prose mutant
reconstructions; an independent float AST sweep; the `lambda_of` no-smuggling AST scan;
the four-decoy AST-guard coverage test; the GW1 §4 census cross-check; the receipt
denominator audit; and the full in-place byte-identity re-run.

---

## 10. Findings, ranked

| # | severity | finding | verdict impact |
|---|---|---|---|
| F1 | **MODERATE** | The printed verdict is not derived inside a gate and no `verdict-flip` mutant exists (Probe A: a hand-typed `HA-BRIDGE-POSABLE` passes all 21 must-pass gates, exit 0, contradicting §12 of its own output) | none — the delivered verdict is independently confirmed correct |
| F2 | **MODERATE** | No cell-completeness gate on the census (Probe E: dropping `A-linkhalf` shrinks the table 99→90 silently, all gates pass) | none |
| F3 | **MODERATE** | §10.2's "17 of 24" is a scalar surrogate, not the dihedral relation; Σ is defined on only **4** of the 24 carriers, and the relation holds at **3 of 4** where posable | none — G22's predicate does not read it |
| F4 | MINOR–MOD | §7.4's "the self-test evaluates fresh" is false as coded: the 486 bypasses are discarded and the comparands go through the memo (Probes C and D) | none — value confirmed memo-independent |
| F5 | MINOR | G23's scanner is blind to `DELIVERY_RUN`/`SELFTEST_ONLY`/`sys.argv`, so X03's exception is asserted not measured; line 1055's `switches` is dead and vacuous | none — claim verified true today |
| F6 | MINOR | G06, a must-pass positive control, is analytically forced by the same identity X02 discloses for G08 | none |
| F7 | LOW | G14's claim says "every declared chart translation"; 6 of 18 group elements are tested (receipt honest at `translations: 3`). I verified the full group: 192 456 comparisons, 0 violations | none — claim independently confirmed true |
| F8 | LOW | G05's two routes share `beta()`; a common-mode β error is invisible to G05 (β is policed by G06/G08/G12/G21 instead) | none |
| F9 | LOW | Ten of sixteen anchors have no declared falsifier | none — A05/A06 corrupted by hand, both fire |
| F10 | LOW | X01 embeds live-tree counts, so byte-identity depends on directories other cycles write to | none |
| F11 | LOW | G03's only falsifier is a wholesale lapse-family replacement (§14's caution) | none |

**None of the eleven findings moves a number, and none moves the verdict.** F1–F4 are
gate-architecture and reporting repairs; F5–F11 are hardening. The unit's substantive
claims — a record-native `H_a[N]` exists and is invertible by construction; the GW1
residual runs; closure holds exactly on the diagonal sector and fails at the cross
term; closure is insertion site by site; transport is independently necessary; no
link-local record-native weight can close; and the stitching-geometry bridge is not
posable at the committed coordinates — all survived every attempt I made to refute
them, and every one of their numbers reproduced under a disjoint implementation.

---

## 11. Grade

**ACCEPT-WITH-FIXES.**

Required before TERMINAL:

1. **F1** — derive the verdict string inside a gate (G25) and add a `verdict-flip`
   mutant that must die there.
2. **F2** — add cell-completeness gates to the closure table, the sector-law grid and
   the d=3 grid.
3. **F3** — restate §10.2 as "3 of the 4 pairs at which the chart involution is
   defined" (or build the carrier per pair and measure the relation properly); stop
   describing the surrogate as "the same relation".
4. **F4** — make the chart self-test's own comparands cache-free, and reword §7.4.

Recommended: F5 (extend the AST guard to the run-mode booleans; remove the vacuous
`switches` line), F6 (disclose G06's forcing or re-base it on the literal route),
F7 (run the full declared chart group — it costs 192 456 comparisons and passes).
